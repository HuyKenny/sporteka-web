// Product photos are taken from the partners' feeds (alcohol shops) and resized on the fly by wsrv.nl (images.weserv.nl):
// nothing is stored on Cloudflare (Kenny, 27. 10. 2026: šetřit místo). wsrv.nl blocks only adult domains (eroka needed its
// own Worker), the alcohol shops pass. Dead hosts are skipped, the page then shows the placeholder.
import { DEAD_IMAGE_HOSTS, DIRECT_IMAGE_HOSTS, SHOPTET_HOST, WIDTHS, imageHostAllowed } from './image-hosts';
import { hmac16 } from './sign';
import { getEnv } from './server/env';

export { WIDTHS };
export type Width = (typeof WIDTHS)[number];

/** Feeds sometimes put text ("in stock") or a broken host into the image field. */
export function validImage(url: string | null | undefined): string {
  const u = String(url ?? '').trim().replace(/^http:\/\//i, 'https://');
  if (!/^https:\/\/[^\s/]+\.[^\s/]+\//i.test(u) || /%20/.test(u.split('/')[2] ?? '')) return '';
  return u;
}

function b64url(s: string): string {
  const bytes = new TextEncoder().encode(s);
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

/** URL of the photo fitted inside w × w px (never enlarged), WebP: /img/<w>/<sig>/<base64url(source)>.webp, served by our Worker
 *  sporteka-img (cold 0.2–0.5 s, then the edge cache; wsrv.nl needed 1–5 s cold and cannot reach Answear at all). */
export function thumb(url: string | null | undefined, w: Width): string {
  let src = validImage(url);
  if (!src) return '';
  let u: URL;
  try { u = new URL(src); } catch { return ''; }
  if (DEAD_IMAGE_HOSTS.includes(u.hostname)) return '';
  if (DIRECT_IMAGE_HOSTS.includes(u.hostname)) return src;
  if (u.hostname === SHOPTET_HOST && /\/shop\/orig\//.test(u.pathname)) { src = src.replace('/shop/orig/', w > 480 ? '/shop/big/' : '/shop/detail/'); u = new URL(src); }
  if (!imageHostAllowed(u.hostname)) return src;
  const b = b64url(src);
  return `/img/${w}/${hmac16(getEnv().IMG_SECRET ?? '', `${w}/${b}`)}/${b}.webp`;
}

/** src + srcset (1× / 2×) for an image shown at `css` px. */
export function picture(url: string | null | undefined, css: 160 | 240 | 320 | 480): { src: string; srcset: string } | null {
  const pairs: Record<number, [Width, Width]> = { 160: [160, 320], 240: [320, 480], 320: [320, 640], 480: [480, 960] };
  const [a, b] = pairs[css]!;
  const one = thumb(url, a);
  if (!one) return null;
  return { src: one, srcset: `${one} 1x, ${thumb(url, b)} 2x` };
}

/** Fluid photo (w descriptors): the phone downloads the smallest file that still covers its column (capped at 640 px, sharp enough for a 360 px column at 1.8×). */
export function fluid(url: string | null | undefined): { src: string; srcset: string } | null {
  const mid = thumb(url, 480);
  if (!mid) return null;
  return { src: mid, srcset: `${thumb(url, 320)} 320w, ${mid} 480w, ${thumb(url, 640)} 640w` };
}

/** Own uploads (article photos) as site-relative paths, so every host (staging, workers.dev) serves its own copy. */
export const ownUpload = (u: string | null | undefined) => String(u ?? '').replace(/^https?:\/\/(www\.)?sporteka\.cz(?=\/(wp-content|a)\/)/, '');
