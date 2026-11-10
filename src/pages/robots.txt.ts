import type { APIRoute } from 'astro';
import { getEnv } from '../lib/server/env';

export const prerender = false;
// Only search engines may crawl (Cloudflare WAF enforces it, scripts/zona-boti.py); this file tells them what to skip:
// filtered listings (brand, shop, price, parameters) MAY be crawled by these engines (3. 11. 2026, Kenny): they answer noindex,follow
// and the engines see it; sort orders, search results, affiliate exits and the API stay out. Everybody else gets 403 from the WAF.
const SKIP = `Disallow: /go/
Disallow: /api/
Disallow: /*?*orderby=
Disallow: /*?s=
`;
const GOOD: Array<[string, number]> = [['Googlebot', 0], ['Googlebot-Image', 0], ['Google-InspectionTool', 0], ['Storebot-Google', 0], ['bingbot', 3], ['SeznamBot', 3]];
const PROD = `${GOOD.map(([ua, delay]) => `User-agent: ${ua}\n${delay ? `Crawl-delay: ${delay}\n` : ''}${SKIP}`).join('\n')}
User-agent: *
Disallow: /

Sitemap: https://sporteka.cz/sitemap_index.xml
`;
export const GET: APIRoute = () => {
  const prod = getEnv().ENVIRONMENT === 'production';
  return new Response(prod ? PROD : 'User-agent: *\nDisallow: /\n', { headers: { 'content-type': 'text/plain; charset=UTF-8', 'cache-control': 'public, max-age=3600' } });
};
