// GET /api/suggest?q= — search suggestions for the header: categories, brands (names, in memory) and up to
// 6 products (FTS5). Edge-cached per query for 10 minutes; the data version is part of the cache key.
import type { APIRoute } from 'astro';
import { getEnv } from '../../lib/server/env';
import { dataVersion } from '../../lib/server/versions';
import { clientIp } from '../../lib/server/http';
import { brandList, catTree, suggestProducts } from '../../lib/db';
import { matchNames } from '../../lib/views';
import { cena, decode, texturize } from '../../lib/format';
import { thumb } from '../../lib/img';

export const prerender = false;
const json = (body: unknown, cache = 'public, max-age=300') => new Response(JSON.stringify(body), { headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': cache } });

export const GET: APIRoute = async ({ url, locals, request }) => {
  const q = (url.searchParams.get('q') ?? '').trim().slice(0, 60);
  if (q.length < 2) return json({ cats: [], brands: [], products: [] });
  const env = getEnv();
  const cache = typeof caches !== 'undefined' ? (caches as unknown as { default: Cache }).default : null;
  const key = `https://${url.host}/__sg/${encodeURIComponent(await dataVersion())}/${encodeURIComponent(q.toLowerCase())}`;
  const hit = cache ? await cache.match(key) : null;
  if (hit) return hit;
  if (env.RL_SEARCH && !(await env.RL_SEARCH.limit({ key: clientIp(request) })).success) return json({ cats: [], brands: [], products: [] }, 'no-store');
  const [tree, brands, products] = await Promise.all([catTree(env.DB), brandList(env.DB), suggestProducts(env.DB, q)]);
  const { cats, brs } = matchNames(q, tree, brands);
  const res = json({
    cats: cats.slice(0, 4).map((c) => ({ u: `/${c.slug}/`, n: decode(c.name), c: c.count_total })),
    brands: brs.slice(0, 3).map((b) => ({ u: `/znacka/${b.slug}/`, n: decode(b.name), c: b.count })),
    products: products.map((p) => ({ u: `/${p.slug}/`, n: texturize(decode(p.name)), p: p.min_price > 0 ? (p.offer_count > 1 ? 'od ' : '') + cena(p.min_price) : '', i: thumb(p.image, 160) })),
  });
  if (cache) {
    const store = res.clone();
    store.headers.set('cache-control', 'public, s-maxage=600');
    const put = cache.put(key, store);
    if (locals.cfContext?.waitUntil) locals.cfContext.waitUntil(put); else await put;
  }
  return res;
};
