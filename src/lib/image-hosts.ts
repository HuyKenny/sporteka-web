// Image sources shared by the site (src/lib/img.ts builds /img/ URLs) and the sporteka-img Worker (workers/img checks them).
// Product photos come from the partners' feeds; every shop domain (and its CDN) is listed, subdomains included.
// A shop added to the feeds needs its image host here (otherwise its photo is shown straight from the shop).
import shops from '../data/obchody.json';

export const IMAGE_DOMAINS: string[] = [
  'mediadecathlon.com', 'myshoptet.com', 'ans-media.com', 'factcool.com', 'spartoo.cz', 'cdn-upgates.com', 'shopify.com', 'kokiska.cz', 'feedyio.com', 'allegroimg.com', 'productserve.com',
  ...shops.shops.map((s) => s.domain),
];
/** Thumbnail widths (fitted inside w × w). */
export const WIDTHS = [160, 320, 480, 640, 960] as const;
/** Hosts that no longer resolve or return 404 for every image — skipped, the page uses another photo. */
export const DEAD_IMAGE_HOSTS: string[] = [];
/** Hosts that refuse server-side fetching (Cloudflare bot protection, 403 for any Worker/wsrv fetch): their photos are loaded by the
 *  visitor's browser straight from the shop (Sportisimo, 31. 10. 2026). The feed already gives 600×600 JPEGs. */
export const DIRECT_IMAGE_HOSTS: string[] = ['www.sportisimo.cz', 'sportisimo.cz', 'www.sport365.cz', 'sport365.cz', 'gymbeam.cz', 'www.gymbeam.cz'];   // sport365 + gymbeam: same 403 for the Worker (3. 11. 2026)
/** Shoptet CDN keeps resized copies next to the original (…/shop/orig/x.jpg → …/shop/detail/x.jpg, 16–70 kB instead of 1.5 MB). */
export const SHOPTET_HOST = 'cdn.myshoptet.com';

export function imageHostAllowed(host: string): boolean {
  const h = host.toLowerCase();
  if (DEAD_IMAGE_HOSTS.includes(h) || DIRECT_IMAGE_HOSTS.includes(h)) return false;
  return IMAGE_DOMAINS.some((d) => h === d || h.endsWith('.' + d));
}
