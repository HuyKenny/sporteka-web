// GET /api/static-cards?ids=1,2,3 — card data for the client-side search index of the static export (scripts/staticky.py
// writes /_s/w/<word>.json from it). Exists only in the local export run (STATIC_EXPORT=1); the live SSR answers 404.
import type { APIRoute } from 'astro';
import { getEnv, isStatic } from '../../lib/server/env';
import { cardsByIds } from '../../lib/db';
import { cena, decode, texturize } from '../../lib/format';
import { thumb } from '../../lib/img';

export const prerender = false;
export const GET: APIRoute = async ({ url }) => {
  if (!isStatic()) return new Response('Not found', { status: 404 });
  const ids = (url.searchParams.get('ids') ?? '').split(',').map(Number).filter((n) => n > 0).slice(0, 90);
  const cards = await cardsByIds(getEnv().DB, ids);
  // [id, slug, name, price text, image 320 px, shops, discount %, in stock]
  const out = cards.map((p) => {
    const shops = p.shop_count || p.offer_count;
    return [p.id, p.slug, texturize(decode(p.name)), p.min_price > 0 ? (shops > 1 ? 'od ' : '') + cena(p.min_price) : '',
      thumb(p.image, 320), shops, p.disc_pct, p.in_stock ? 1 : 0];
  });
  return new Response(JSON.stringify(out), { headers: { 'content-type': 'application/json; charset=utf-8' } });
};
