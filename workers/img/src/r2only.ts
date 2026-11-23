// Workers Free (23. 11. 2026): thumbnails only from R2 (sporteka-thumbs) — no WASM resize, so every request stays far
// under the 10 ms CPU limit. On an R2 miss the visitor gets the shop's original photo (302) instead of a thumbnail.
// The previous resizer (src/index.ts) stays in the repo for rollback: set "main" back to ./src/index.ts.
import { WIDTHS, imageHostAllowed } from '../../../src/lib/image-hosts';
import { hmac16 } from '../../../src/lib/sign';

interface R2Like { get(k: string): Promise<{ body: ReadableStream } | null> }
interface Env { THUMBS?: R2Like; IMG_SECRET?: string }

function b64urlDecode(s: string): string {
  const b = atob(s.replace(/-/g, '+').replace(/_/g, '/') + '='.repeat((4 - (s.length % 4)) % 4));
  return new TextDecoder().decode(Uint8Array.from(b, (c) => c.charCodeAt(0)));
}
const redirect = (to: string) => new Response(null, { status: 302, headers: { location: to, 'cache-control': 'public, max-age=3600' } });
const bad = (msg: string, status = 400) => new Response(msg, { status, headers: { 'content-type': 'text/plain', 'cache-control': 'public, max-age=300' } });

export default {
  async fetch(request: Request, env: Env, ctx: { waitUntil(p: Promise<unknown>): void }): Promise<Response> {
    if (request.method !== 'GET' && request.method !== 'HEAD') return bad('method', 405);
    const m = /^\/img\/(\d+)\/([0-9a-f]{16})\/([A-Za-z0-9_-]{8,1400})\.webp$/.exec(new URL(request.url).pathname);
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
    const rkey = `${width}/${[...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(m[3]!)))].map((x) => x.toString(16).padStart(2, '0')).join('')}.webp`;
    const stored = env.THUMBS ? await env.THUMBS.get(rkey).catch(() => null) : null;
    if (!stored) return redirect(src.toString());
    const res = new Response(stored.body, { headers: { 'content-type': 'image/webp', 'cache-control': 'public, max-age=31536000, immutable', 'access-control-allow-origin': '*', 'x-content-type-options': 'nosniff', 'x-sporteka-img': 'r2' } });
    ctx.waitUntil(cache.put(key, res.clone()));
    return res;
  },
};
