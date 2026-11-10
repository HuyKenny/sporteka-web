// sporteka-img: product photo thumbnails for the whole site. The photo is fetched from the partner's feed URL, resized in
// WASM and returned as WebP. Each thumbnail is computed once and kept in R2 (binding THUMBS, bucket lifecycle 180 days — Kenny 3. 11. 2026:
// the WASM resize is what costs CPU money, R2 is free up to 10 GB); the edge cache and the browser keep the result too (immutable, 1 year; the source URL is part of the path, so a new photo = a new URL).
//   GET /img/<width>/<sig>/<base64url(source URL)>.webp
//   width ∈ WIDTHS, sig = HMAC(IMG_SECRET, "<width>/<base64url>") from src/lib/sign.ts, source host ∈ image-hosts.ts
// Guards: signature, host allowlist (also after a redirect), byte cap while streaming, pixel cap read from the image
// header before decoding, rate limit on cache misses. Undecodable files (GIF, AVIF, broken) redirect to the original.
import decodeJpeg, { init as initJpeg } from '@jsquash/jpeg/decode';
import decodePng, { init as initPng } from '@jsquash/png/decode';
import decodeWebp, { init as initWebpDec } from '@jsquash/webp/decode';
import encodeWebp, { init as initWebpEnc } from '@jsquash/webp/encode';
import resize, { initResize } from '@jsquash/resize';
import JPEG_DEC from '../../../node_modules/@jsquash/jpeg/codec/dec/mozjpeg_dec.wasm';
import PNG_DEC from '../../../node_modules/@jsquash/png/codec/pkg/squoosh_png_bg.wasm';
import WEBP_DEC from '../../../node_modules/@jsquash/webp/codec/dec/webp_dec.wasm';
import WEBP_ENC from '../../../node_modules/@jsquash/webp/codec/enc/webp_enc_simd.wasm';
import RESIZE from '../../../node_modules/@jsquash/resize/lib/resize/pkg/squoosh_resize_bg.wasm';

import { WIDTHS, imageHostAllowed } from '../../../src/lib/image-hosts';
import { hmac16 } from '../../../src/lib/sign';

// the codecs construct ImageData, which the Workers runtime does not have
class ImageDataShim {
  constructor(public data: Uint8ClampedArray, public width: number, public height: number) {}
}
(globalThis as unknown as { ImageData: unknown }).ImageData ??= ImageDataShim;

const MAX_BYTES = 8_000_000;
const MAX_PIXELS = 25_000_000;
// the WASM decoder (128 MB isolate) fails on ~4 MP+ photos (Bezvasport serves 2000×3000 JPEGs): those go through Cloudflare Image Resizing instead
const WASM_PIXELS = 3_500_000;
interface R2Like { get(k: string): Promise<{ body: ReadableStream } | null>; put(k: string, v: ArrayBuffer | Uint8Array, o?: unknown): Promise<unknown> }
interface Env { THUMBS?: R2Like; IMG_SECRET?: string; IMG_LEGACY?: string; RL_IMG?: { limit(o: { key: string }): Promise<{ success: boolean }> } }

let ready: Promise<unknown> | null = null;
const init = () => (ready ??= Promise.all([initJpeg(JPEG_DEC), initPng(PNG_DEC), initWebpDec(WEBP_DEC), initWebpEnc(WEBP_ENC), initResize(RESIZE)]));

function b64urlDecode(s: string): string {
  const b = atob(s.replace(/-/g, '+').replace(/_/g, '/') + '='.repeat((4 - (s.length % 4)) % 4));
  return new TextDecoder().decode(Uint8Array.from(b, (c) => c.charCodeAt(0)));
}
const redirect = (to: string) => new Response(null, { status: 302, headers: { location: to, 'cache-control': 'public, max-age=3600' } });
const bad = (msg: string, status = 400) => new Response(msg, { status, headers: { 'content-type': 'text/plain', 'cache-control': 'public, max-age=300' } });

/** Width × height from the file header (JPEG SOFn, PNG IHDR, WebP VP8/VP8L/VP8X) — refuse huge images before decoding. */
function headerPixels(b: Uint8Array): number | null {
  if (b[0] === 0x89 && b[1] === 0x50) return ((b[16]! << 24 | b[17]! << 16 | b[18]! << 8 | b[19]!) >>> 0) * ((b[20]! << 24 | b[21]! << 16 | b[22]! << 8 | b[23]!) >>> 0);
  if (b[0] === 0x52 && b[1] === 0x49 && b[8] === 0x57) {
    const t = String.fromCharCode(b[12]!, b[13]!, b[14]!, b[15]!);
    if (t === 'VP8X') return (1 + (b[24]! | b[25]! << 8 | b[26]! << 16)) * (1 + (b[27]! | b[28]! << 8 | b[29]! << 16));
    if (t === 'VP8L') { const v = b[21]! | b[22]! << 8 | b[23]! << 16 | b[24]! << 24; return (1 + (v & 0x3fff)) * (1 + ((v >>> 14) & 0x3fff)); }
    if (t === 'VP8 ') return ((b[26]! | b[27]! << 8) & 0x3fff) * ((b[28]! | b[29]! << 8) & 0x3fff);
    return null;
  }
  if (b[0] === 0xff && b[1] === 0xd8) {
    let i = 2;
    while (i + 9 < b.length) {
      if (b[i] !== 0xff) { i++; continue; }
      const m = b[i + 1]!;
      if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) return (b[i + 5]! << 8 | b[i + 6]!) * (b[i + 7]! << 8 | b[i + 8]!);
      if (m === 0xd8 || m === 0x01 || (m >= 0xd0 && m <= 0xd7)) { i += 2; continue; }
      i += 2 + (b[i + 2]! << 8 | b[i + 3]!);
    }
  }
  return null;
}

/** Fetch the source: manual redirects (max 2, target host re-checked), body read with a byte cap. */
async function fetchSource(src: URL): Promise<ArrayBuffer | 'redirect-original' | 'missing'> {
  let url = src;
  for (let hop = 0; hop < 3; hop++) {
    const r = await fetch(url.toString(), { redirect: 'manual', headers: { 'user-agent': 'Mozilla/5.0 (compatible; sporteka.cz thumbnails)', accept: 'image/webp,image/jpeg,image/png,*/*' }, cf: { cacheTtl: 86400, cacheEverything: true } } as RequestInit);
    if (r.status >= 300 && r.status < 400) {
      const loc = r.headers.get('location');
      if (!loc) return 'redirect-original';
      url = new URL(loc, url);
      if (url.protocol !== 'https:' || url.port || url.username || !imageHostAllowed(url.hostname)) return 'redirect-original';
      continue;
    }
    if (r.status === 404 || r.status === 410) return 'missing';
    if (!r.ok || !r.body) return 'redirect-original';
    if (Number(r.headers.get('content-length') ?? 0) > MAX_BYTES) return 'redirect-original';
    const reader = r.body.getReader();
    const parts: Uint8Array[] = [];
    let n = 0;
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      n += value.byteLength;
      if (n > MAX_BYTES) { await reader.cancel(); return 'redirect-original'; }
      parts.push(value);
    }
    const out = new Uint8Array(n);
    let o = 0;
    for (const p of parts) { out.set(p, o); o += p.byteLength; }
    return out.buffer;
  }
  return 'redirect-original';
}

async function decode(buf: ArrayBuffer): Promise<{ data: Uint8ClampedArray; width: number; height: number } | null> {
  const b = new Uint8Array(buf, 0, 12);
  if (b[0] === 0xff && b[1] === 0xd8) return decodeJpeg(buf);
  if (b[0] === 0x89 && b[1] === 0x50 && b[2] === 0x4e && b[3] === 0x47) return decodePng(buf);
  if (b[0] === 0x52 && b[1] === 0x49 && b[8] === 0x57 && b[9] === 0x45) return decodeWebp(buf);
  return null;
}

/** Cloudflare Image Resizing for what the WASM codec cannot take (too big / odd files); null when it is not available for the zone. */
async function viaCloudflare(src: URL, width: number): Promise<Response | null> {
  const r = await fetch(src.toString(), {
    headers: { 'user-agent': 'Mozilla/5.0 (compatible; sporteka.cz thumbnails)', accept: 'image/webp,image/jpeg,image/png,*/*' },
    cf: { image: { width, height: width, fit: 'scale-down', format: 'webp', quality: 76 } },
  } as RequestInit);
  if (!r.ok || !(r.headers.get('content-type') ?? '').startsWith('image/') || !r.body) return null;
  return new Response(r.body, { headers: { 'content-type': 'image/webp', 'cache-control': 'public, max-age=31536000, immutable', 'access-control-allow-origin': '*', 'x-content-type-options': 'nosniff', 'x-sporteka-img': 'cf' } });
}

export default {
  async fetch(request: Request, env: Env, ctx: { waitUntil(p: Promise<unknown>): void }): Promise<Response> {
    if (request.method !== 'GET' && request.method !== 'HEAD') return bad('method', 405);
    const url = new URL(request.url);
    let m = /^\/img\/(\d+)\/([0-9a-f]{16})\/([A-Za-z0-9_-]{8,1400})\.webp$/.exec(url.pathname);
    // unsigned URLs of the previous site build — only while IMG_LEGACY=1 (switch-over window of a deploy)
    if (!m && env.IMG_LEGACY === '1') { const l = /^\/img\/(\d+)\/([A-Za-z0-9_-]{8,1400})\.webp$/.exec(url.pathname); if (l) m = [l[0], l[1]!, hmac16(env.IMG_SECRET ?? '', `${l[1]}/${l[2]}`), l[2]!] as unknown as RegExpExecArray; }
    if (!m) return bad('not found', 404);
    const width = Number(m[1]);
    if (!(WIDTHS as readonly number[]).includes(width)) return bad('width');
    if (env.IMG_SECRET && m[2] !== hmac16(env.IMG_SECRET, `${width}/${m[3]}`)) return bad('signature', 403);
    let src: URL;
    try { src = new URL(b64urlDecode(m[3]!)); } catch { return bad('source'); }
    if (src.protocol !== 'https:' || src.port || src.username || src.password || !imageHostAllowed(src.hostname)) return bad('host', 403);

    const cache = (caches as unknown as { default: Cache }).default;
    const key = new Request(`https://sporteka-img.cache/${width}/${m[3]}.webp`);
    const hit = await cache.match(key);
    if (hit) return hit;
    // R2: a thumbnail made once is never computed again (any colo, after cache eviction); key = sha256, R2 keys ≤ 1024 B
    const rkey = `${width}/${[...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(m[3]!)))].map((x) => x.toString(16).padStart(2, '0')).join('')}.webp`;
    const HDR = { 'content-type': 'image/webp', 'cache-control': 'public, max-age=31536000, immutable', 'access-control-allow-origin': '*', 'x-content-type-options': 'nosniff' };
    const stored = env.THUMBS ? await env.THUMBS.get(rkey).catch(() => null) : null;
    if (stored) {
      const res = new Response(stored.body, { headers: { ...HDR, 'x-sporteka-img': 'r2' } });
      ctx.waitUntil(cache.put(key, res.clone()));
      return res;
    }
    const keep = (r: Response) => { if (env.THUMBS) ctx.waitUntil(r.clone().arrayBuffer().then((b) => env.THUMBS!.put(rkey, b, { httpMetadata: { contentType: 'image/webp' } })).catch(() => null)); };
    const ip = request.headers.get('cf-connecting-ip') ?? '0.0.0.0';
    if (env.RL_IMG && !(await env.RL_IMG.limit({ key: ip })).success) return new Response('Too many requests', { status: 429, headers: { 'retry-after': '30' } });

    try {
      const buf = await fetchSource(src);
      if (buf === 'missing') return bad('source 404', 404);
      if (buf === 'redirect-original') return redirect(src.toString());
      if (buf.byteLength < 12) return redirect(src.toString());
      const px = headerPixels(new Uint8Array(buf, 0, Math.min(buf.byteLength, 65536)));
      if (px !== null && px > MAX_PIXELS) return redirect(src.toString());
      if (px !== null && px > WASM_PIXELS) {
        const big = await viaCloudflare(src, width);
        if (big) { ctx.waitUntil(cache.put(key, big.clone())); keep(big); return big; }
        return redirect(src.toString());
      }
      await init();
      const img = await decode(buf);
      if (!img) return redirect(src.toString());
      // fit inside width × width, never enlarge
      const scale = Math.min(1, width / img.width, width / img.height);
      const w = Math.max(1, Math.round(img.width * scale)), h = Math.max(1, Math.round(img.height * scale));
      const out = scale < 1 ? await resize(img as ImageData, { width: w, height: h, method: 'lanczos3', fitMethod: 'stretch' }) : img;
      const webp = await encodeWebp(out as ImageData, { quality: 76 });
      const res = new Response(webp, {
        headers: {
          'content-type': 'image/webp', 'cache-control': 'public, max-age=31536000, immutable', 'access-control-allow-origin': '*',
          'x-content-type-options': 'nosniff', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'x-sporteka-img': `${img.width}x${img.height}>${w}x${h}`,
        },
      });
      ctx.waitUntil(cache.put(key, res.clone()));
      keep(res);
      return res;
    } catch (e) {
      const alt = await viaCloudflare(src, width).catch(() => null);
      if (alt) { ctx.waitUntil(cache.put(key, alt.clone())); keep(alt); return alt; }
      console.log(JSON.stringify({ event: 'img.error', src: src.toString(), error: String(e).slice(0, 200) }));
      return redirect(src.toString());
    }
  },
};
