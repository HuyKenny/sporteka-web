// Sitemaps built on request from D1 and kept in the edge cache by the middleware (key includes data_version, so a new
// import refreshes them). Product files are id ranges (primary-key range scans, never OFFSET): product-sitemap<n>.xml
// = ids ((n-1)·PER_FILE, n·PER_FILE].
import { BASE } from './site';
import { hasFacetText } from './facet-texts';

export const PER_FILE = 5000;
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const HEAD = '<?xml version="1.0" encoding="UTF-8"?>\n';
const day = (s: string | null | undefined) => String(s ?? '').slice(0, 10);
function urlset(urls: Array<[string, string]>): string {
  return HEAD + '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + urls.map(([u, m]) => `\t<url><loc>${esc(u)}</loc>${m ? `<lastmod>${m}</lastmod>` : ''}</url>`).join('\n') + '\n</urlset>';
}

export async function sitemapIndex(db: D1Database): Promise<string> {
  // only product files that hold indexable products (ids span 700k because noindex products are interleaved; empty files 404'd);
  // the list is computed by the catalogue build (site_cache 'sitemap:files'), the MAX(id) range is the fallback
  const files = ['category-sitemap', 'brand-sitemap', 'page-sitemap'];
  let ns: number[] = [];
  try {
    const row = await db.prepare("SELECT value FROM site_cache WHERE key = 'sitemap:files'").first<{ value: string }>();
    if (row) ns = JSON.parse(row.value) as number[];
  } catch { /* fall back below */ }
  if (!ns.length) {
    const max = (await db.prepare('SELECT MAX(id) AS m FROM products').first<{ m: number | null }>())?.m ?? 0;
    for (let n = 1; (n - 1) * PER_FILE < max; n++) ns.push(n);
  }
  for (const n of ns) files.push(`product-sitemap${n}`);
  return HEAD + '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + files.map((f) => `\t<sitemap><loc>${BASE}/${f}.xml</loc></sitemap>`).join('\n') + '\n</sitemapindex>';
}

export async function sitemapFile(db: D1Database, name: string): Promise<string | null> {
  const all = async <T>(sql: string, ...b: unknown[]) => (await db.prepare(sql).bind(...b).all<T>()).results;
  const m = /^product-sitemap(\d+)$/.exec(name);
  if (m) {
    const n = Number(m[1]);
    const rows = await all<{ slug: string; u: string }>("SELECT slug, updated_at AS u FROM products WHERE id > ? AND id <= ? AND status = 'publish' AND noindex = 0 AND offer_count > 0",
      (n - 1) * PER_FILE, n * PER_FILE);
    return rows.length ? urlset(rows.map((r) => [`${BASE}/${r.slug}/`, day(r.u)])) : null;
  }
  if (name === 'category-sitemap') {
    const cats = await all<{ slug: string }>('SELECT slug FROM categories WHERE noindex = 0 AND count_total > 0 ORDER BY menu_order');
    const fps = await all<{ slug: string; u: string }>('SELECT slug, updated_at AS u FROM facet_pages WHERE noindex = 0 AND total >= min_products');
    return urlset([[`${BASE}/`, ''], ...cats.map((c): [string, string] => [`${BASE}/${c.slug}/`, '']), ...fps.filter((f) => hasFacetText(f.slug)).map((f): [string, string] => [`${BASE}/${f.slug}/`, day(f.u)])]);
  }
  if (name === 'brand-sitemap') {
    const rows = await all<{ slug: string }>('SELECT slug FROM brands WHERE noindex = 0 ORDER BY count DESC');
    return urlset(rows.map((r) => [`${BASE}/znacka/${r.slug}/`, '']));
  }
  if (name === 'page-sitemap') {
    const rows = await all<{ slug: string; u: string }>("SELECT slug, modified_at AS u FROM posts WHERE status = 'publish' AND noindex = 0");
    return urlset([[`${BASE}/obchody/`, ''], [`${BASE}/slevy/`, ''], ...rows.map((r): [string, string] => [`${BASE}/${r.slug}/`, day(r.u)])]);
  }
  return null;
}
