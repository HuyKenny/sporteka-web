// Read model over D1. Every page is 1–2 db.batch() round trips; the category tree (~170 rows) is memoised per
// isolate for a minute, so breadcrumbs, chips and card labels never hit D1 again.
import { PER_PAGE, POSTS_PER_PAGE } from './site';
import { isStatic } from './server/env';
import texts from '../texts/kategorie.json';

export interface Cat {
  id: number; slug: string; name: string; parent: number; count_total: number; count_direct: number;
  noindex: number; menu_order: number;
}
export interface CatFull extends Cat { description_html: string; second_html: string; seo_title: string; seo_desc: string; seo_robots: string; guide_html: string; faq_json: string }
export interface Card {
  id: number; slug: string; name: string; image: string; min_price: number; offer_count: number; shop_count: number;
  best_domain: string; primary_cat: number; go_slug: string | null; target_url?: string | null; disc_pct: number; in_stock: number;
}
export interface Product extends Card {
  short_html: string; desc_html: string; ean: string; brand_id: number; created_at: string; updated_at: string;
  noindex: number; seo_title: string; seo_desc: string; max_price: number; best_offer_id: number; images: string;
}
export interface Offer {
  id: number; feed: string; title: string; domain: string; price: number; price_old: number; stock: number;
  go_slug: string; target_url?: string; updated_at: string; img: string; delivery_price: number | null; sizes: string; variants: number; extra: string;
}
export interface Brand { id: number; slug: string; name: string; description_html: string; count: number; noindex: number; second_html: string; seo_title: string; seo_desc: string; faq_json?: string }
export interface Post {
  id: number; type: 'post' | 'page'; slug: string; title: string; content_html: string; excerpt: string;
  published_at: string; modified_at: string; cat_id: number; image: string; image_card: string; image_alt: string; image_w: number; image_h: number;
  noindex: number; seo_title: string; seo_desc: string; seo_robots: string; author: string; ld_json: string;
}
export type PostCard = Pick<Post, 'id' | 'slug' | 'title' | 'excerpt' | 'published_at' | 'image' | 'image_card' | 'image_alt' | 'image_w' | 'image_h' | 'cat_id'>;
export interface PostCat { id: number; slug: string; name: string; description: string; count: number }

const CARD_COLS = `p.id, p.slug, p.name, p.image, p.min_price, p.offer_count, p.shop_count, p.best_domain, p.primary_cat, o.go_slug, o.target_url, p.disc_pct, p.in_stock`;
const CARD_JOIN = `LEFT JOIN offers o ON o.id = p.best_offer_id`;

let catMemo: { at: number; byId: Map<number, Cat>; bySlug: Map<string, Cat>; kids: Map<number, Cat[]> } | null = null;
export async function catTree(db: D1Database) {
  if (catMemo && Date.now() - catMemo.at < 60_000) return catMemo;
  const rows = (await db.prepare('SELECT id, slug, name, parent, count_total, count_direct, noindex, menu_order FROM categories').all<Cat>()).results;
  const byId = new Map(rows.map((c) => [c.id, c]));
  const bySlug = new Map(rows.map((c) => [c.slug, c]));
  const kids = new Map<number, Cat[]>();
  for (const c of rows) (kids.get(c.parent) ?? kids.set(c.parent, []).get(c.parent)!).push(c);
  catMemo = { at: Date.now(), byId, bySlug, kids };
  return catMemo;
}
/** Root → … → cat (inclusive). */
export function ancestry(tree: Awaited<ReturnType<typeof catTree>>, id: number): Cat[] {
  const out: Cat[] = [];
  const seen = new Set<number>();
  let c = tree.byId.get(id);
  while (c && !seen.has(c.id)) { out.unshift(c); seen.add(c.id); c = tree.byId.get(c.parent); }
  return out;
}

export async function resolveSlug(db: D1Database, slug: string): Promise<{ kind: string; ref_id: number } | null> {
  return db.prepare('SELECT kind, ref_id FROM slugs WHERE slug = ?').bind(slug).first();
}

/** Unknown slug → a page only when the match is unambiguous: exactly one slug continues it with "-" and the requested
 *  slug is at least half of it (a cut-off or shortened URL). WordPress guessed any prefix match, which sent dead or mistyped URLs to unrelated
 *  products (/vibrator/ → a random vibrator) — Google treats such redirects as soft 404s. */
export async function guessSlug(db: D1Database, slug: string): Promise<string | null> {
  if (slug.length < 8) return null;
  const rows = (await db.prepare("SELECT slug FROM slugs WHERE slug > ? AND slug < ? AND kind IN ('product','category','post','page') ORDER BY slug LIMIT 2")
    .bind(slug + '-', slug + '-￿').all<{ slug: string }>()).results;
  return rows.length === 1 && slug.length >= rows[0]!.slug.length * 0.5 ? rows[0]!.slug : null;
}


/** Dead URL → the closest live page: a brand named in the slug, else a category by keyword, else the homepage (302: temporary, the
 *  fallback is not a real match). Junk paths (files, wp-*, bot probes) stay 404. Returns null when the URL must remain a 404. */
const DEAD_RULES: Array<[RegExp, string]> = [
  [/bezeck|running|beh(-|$)/, 'bezecka-obuv'], [/trek|turistick|hiking/, 'trekova-obuv'], [/kopack/, 'kopacky'], [/tenisk|sneaker/, 'tenisky'],
  [/bund|jacket/, 'sportovni-bundy'], [/mikin|hoodie/, 'mikiny'], [/termo|thermo|funkcni-pradl/, 'termopradlo'], [/legin/, 'leginy'],
  [/kalhot/, 'sportovni-kalhoty'], [/trick|triko/, 'sportovni-tricka'], [/plavk/, 'plavky'], [/batoh/, 'batohy'], [/stan(y)?(-|$)/, 'stany'],
  [/spaci|spacak/, 'spaci-pytle'], [/karimat/, 'karimatky-a-matrace'], [/kolo|kola|cyklo|bike/, 'cyklistika'], [/lyz|ski/, 'zimni-sporty'],
  [/snowboard/, 'snowboarding'], [/brusl/, 'brusle'], [/cink|posil|fitness/, 'fitness'], [/fotbal/, 'fotbal'], [/hokej/, 'hokej'],
  [/rybar|prut|navijak/, 'rybareni'], [/box|mma/, 'bojove-sporty'], [/kolobez/, 'kolobezky'], [/trampolin/, 'trampoliny'], [/kemp|camping/, 'kemping'],
  [/outdoor/, 'outdoor'], [/obuv|boty/, 'sportovni-obuv'], [/obleceni/, 'sportovni-obleceni'],
];
export async function deadUrlTarget(db: D1Database, pathname: string): Promise<{ to: string; status: 301 | 302 } | null> {
  const p = decodeURIComponent(pathname).toLowerCase();
  if (/\.[a-z0-9]{2,5}\/?$/.test(p) || /^\/(wp-|go\/|api\/|\.well-known|feed|xmlrpc|cdn-cgi|_astro|admin)/.test(p)) return null;
  const segs = p.split('/').filter(Boolean).filter((x) => x !== 'znacka' && x !== 'page' && !/^\d+$/.test(x));
  const slug = (segs[segs.length - 1] ?? '').replace(/[^a-z0-9-]/g, '-');
  if (!slug) return { to: '/', status: 302 };
  const toks = slug.split('-').filter(Boolean);
  const prefixes: string[] = [];
  for (let n = Math.min(toks.length, 4); n >= 1; n--) { const c = toks.slice(0, n).join('-'); if (c.length >= 4) prefixes.push(c); }
  if (prefixes.length) {
    const rows = (await db.prepare(`SELECT slug FROM brands WHERE noindex = 0 AND count >= 3 AND slug IN (${prefixes.map(() => '?').join(',')})`).bind(...prefixes).all<{ slug: string }>()).results;
    const hit = prefixes.find((x) => rows.some((r) => r.slug === x));
    if (hit) return { to: `/znacka/${hit}/`, status: 301 };
  }
  for (const [re, cat] of DEAD_RULES) if (re.test(slug)) return { to: `/${cat}/`, status: 301 };
  return { to: '/', status: 302 };
}

export type Sort = 'pop' | 'price' | 'price-desc' | 'date' | 'disc';
export interface ListQuery {
  page: number; sort: Sort; min?: number | undefined; max?: number | undefined;
  brands: number[]; shops: string[]; stock: boolean; disc: boolean; kat?: number | undefined;
  /** canonical param filters: exact values or numeric ranges [from, to) */
  params: Array<{ key: string; values?: string[]; ranges?: Array<[number, number]> }>;
}

/** Sort keys live in cat_products (index range scans, see migration 0004); brand listings sort on products. */
function sortSql(s: Sort, cat: boolean): string {
  const t = cat ? 'x' : 'p';
  const price = cat ? 'x.min_price' : 'p.min_price';
  switch (s) {
    case 'price': return cat ? 'x.min_price ASC, x.product_id DESC' : `${price} = 0, ${price} ASC, x.product_id DESC`;  // cat: idx_cp_price (the zero prices are cut off in listProducts)
    case 'price-desc': return `${price} DESC, x.product_id DESC`;
    case 'date': return 'x.created_at DESC, x.product_id DESC';
    case 'disc': return `${cat ? 'x.disc' : 'p.disc_pct'} DESC, ${t}.pop DESC, x.product_id DESC`;
    default: return `${t}.pop DESC, x.product_id DESC`;
  }
}

/** Products of a category (incl. children, as WooCommerce) or a brand: one page of cards + total. */
export async function listProducts(db: D1Database, by: { cat?: number; brand?: number }, q: ListQuery, knownTotal?: number): Promise<{ items: Card[]; total: number }> {
  const [tbl, col, id] = by.cat ? ['cat_products', 'cat_id', by.cat] : ['brand_products', 'brand_id', by.brand!];
  const filt: string[] = [];
  const binds: unknown[] = [id];
  const inList = (n: number) => Array(n).fill('?').join(',');
  if (q.min !== undefined) { filt.push('p.min_price >= ?'); binds.push(q.min); }
  if (q.max !== undefined) { filt.push('p.min_price <= ?'); binds.push(q.max); }
  if (q.brands.length) { filt.push(`p.brand_id IN (${inList(q.brands.length)})`); binds.push(...q.brands); }
  if (q.shops.length) { filt.push(`EXISTS (SELECT 1 FROM offers o2 WHERE o2.product_id = p.id AND o2.active = 1 AND o2.domain IN (${inList(q.shops.length)}))`); binds.push(...q.shops); }
  if (q.stock) filt.push('p.in_stock = 1');
  if (q.disc) filt.push('p.disc_pct >= 10');
  if (q.kat) { filt.push('EXISTS (SELECT 1 FROM cat_products x2 WHERE x2.product_id = p.id AND x2.cat_id = ?)'); binds.push(q.kat); }
  for (const f of q.params) {
    if (f.values?.length) { filt.push(`EXISTS (SELECT 1 FROM product_params pp WHERE pp.product_id = p.id AND pp.key = ? AND pp.value IN (${inList(f.values.length)}))`); binds.push(f.key, ...f.values); }
    else if (f.ranges?.length) {
      filt.push(`EXISTS (SELECT 1 FROM product_params pp WHERE pp.product_id = p.id AND pp.key = ? AND (${f.ranges.map(() => '(CAST(pp.value AS REAL) >= ? AND CAST(pp.value AS REAL) < ?)').join(' OR ')}))`);
      binds.push(f.key, ...f.ranges.flat());
    }
  }
  // sorted by price: products without a price (no offer) are left out so the sort walks idx_cp_price instead of scanning the category (40k reads on /lihoviny/)
  if (by.cat && q.sort === 'price') filt.push('x.min_price > 0');
  const where = `x.${col} = ? AND p.status = 'publish'` + (filt.length ? ' AND ' + filt.join(' AND ') : '');
  const off = (q.page - 1) * PER_PAGE;
  const list = db.prepare(`SELECT ${CARD_COLS} FROM ${tbl} x JOIN products p ON p.id = x.product_id ${CARD_JOIN} WHERE ${where} ORDER BY ${sortSql(q.sort, !!by.cat)} LIMIT ${PER_PAGE} OFFSET ${off}`).bind(...binds);
  if (knownTotal !== undefined && !filt.length) {
    return { items: (await list.all<Card>()).results, total: knownTotal };
  }
  // capped at 100 pages: an exact count over a big section (tens of thousands of rows) on every filtered page is what
  // costs D1 reads, nobody pages beyond 100
  const cnt = db.prepare(`SELECT COUNT(*) AS n FROM (SELECT 1 FROM ${tbl} x JOIN products p ON p.id = x.product_id WHERE ${where} LIMIT ${PER_PAGE * 100})`).bind(...binds);
  const [a, b] = await db.batch([list, cnt]);
  return { items: a!.results as Card[], total: Number((b!.results[0] as { n: number }).n) };
}

/** All discounted products (≥ 10 %, in stock; > 85 % is a feed error more often than a sale) with the listing filters — the /slevy/ page. Default order: biggest discount. */
export async function listDiscounted(db: D1Database, q: ListQuery): Promise<{ items: Card[]; total: number }> {
  const filt: string[] = ["p.status = 'publish'", 'p.in_stock = 1', 'p.disc_pct >= 10', 'p.disc_pct <= 85'];
  const binds: unknown[] = [];
  const inList = (n: number) => Array(n).fill('?').join(',');
  if (q.min !== undefined) { filt.push('p.min_price >= ?'); binds.push(q.min); }
  if (q.max !== undefined) { filt.push('p.min_price <= ?'); binds.push(q.max); }
  if (q.brands.length) { filt.push(`p.brand_id IN (${inList(q.brands.length)})`); binds.push(...q.brands); }
  if (q.shops.length) { filt.push(`EXISTS (SELECT 1 FROM offers o2 WHERE o2.product_id = p.id AND o2.active = 1 AND o2.domain IN (${inList(q.shops.length)}))`); binds.push(...q.shops); }
  if (q.kat) { filt.push('EXISTS (SELECT 1 FROM cat_products x2 WHERE x2.product_id = p.id AND x2.cat_id = ?)'); binds.push(q.kat); }
  for (const f of q.params) {
    if (f.values?.length) { filt.push(`EXISTS (SELECT 1 FROM product_params pp WHERE pp.product_id = p.id AND pp.key = ? AND pp.value IN (${inList(f.values.length)}))`); binds.push(f.key, ...f.values); }
  }
  const where = filt.join(' AND ');
  const order = q.sort === 'price' ? 'p.min_price ASC, p.id DESC' : q.sort === 'price-desc' ? 'p.min_price DESC, p.id DESC' : 'p.disc_pct DESC, p.id DESC';
  const off = (q.page - 1) * PER_PAGE;
  const [a, b] = await db.batch([
    db.prepare(`SELECT ${CARD_COLS} FROM products p ${CARD_JOIN} WHERE ${where} ORDER BY ${order} LIMIT ${PER_PAGE} OFFSET ${off}`).bind(...binds),
    db.prepare(`SELECT COUNT(*) AS n FROM (SELECT 1 FROM products p WHERE ${where} LIMIT ${PER_PAGE * 200})`).bind(...binds),
  ]);
  return { items: a!.results as Card[], total: Number((b!.results[0] as { n: number }).n) };
}

export interface BrandLite { id: number; slug: string; name: string; count: number }
let brandMemo: { at: number; byId: Map<number, BrandLite>; bySlug: Map<string, BrandLite> } | null = null;
/** All brands (638 rows), memoised per isolate for 10 minutes — facet labels, suggestions, homepage. */
export async function brandList(db: D1Database) {
  if (brandMemo && Date.now() - brandMemo.at < 600_000) return brandMemo;
  const rows = (await db.prepare("SELECT id, slug, name, count FROM brands WHERE noindex = 0 AND count > 0").all<BrandLite>()).results;
  brandMemo = { at: Date.now(), byId: new Map(rows.map((b) => [b.id, b])), bySlug: new Map(rows.map((b) => [b.slug, b])) };
  return brandMemo;
}

/** Facets precomputed nightly by the importer (workers/import/src/facets.ts). */
export interface Facets { n: number; lo: number; hi: number; st: number; d: number; b: Array<[number, number]>; s: Array<[string, number]>; p: Record<string, Array<[string, number]>>; c?: Array<[number, number]> }
export async function facets(db: D1Database, key: string): Promise<Facets | null> {
  const v = await siteCache(db, key);
  try { return v ? JSON.parse(v) as Facets : null; } catch { return null; }
}
let catImgMemo: { at: number; map: Record<string, string> } | null = null;
/** One product photo per category (nightly, 'cats:img'). */
export async function catImages(db: D1Database): Promise<Record<string, string>> {
  if (catImgMemo && Date.now() - catImgMemo.at < 600_000) return catImgMemo.map;
  let map: Record<string, string> = {};
  try { map = JSON.parse((await siteCache(db, 'cats:img')) ?? '{}'); } catch { /* empty */ }
  catImgMemo = { at: Date.now(), map };
  return map;
}

/** Category texts kept in the repository (src/texts/kategorie.json: slug → description_html / second_html / guide_html / faq_json / seo_title / seo_desc).
 *  They override the database columns, so writing or changing a text costs no D1 write — only a deploy (free). */
const TEXTS = texts as unknown as Record<string, Partial<CatFull>>;
export async function loadCategory(db: D1Database, id: number): Promise<CatFull | null> {
  const c = await db.prepare('SELECT * FROM categories WHERE id = ?').bind(id).first<CatFull>();
  return c ? { ...c, ...(TEXTS[c.slug] ?? {}) } : c;
}

export async function loadProduct(db: D1Database, id: number) {
  const [p, offers, cats, hist, params] = await db.batch([
    db.prepare(`SELECT p.*, o.go_slug, o.target_url, b.slug AS b_slug, b.name AS b_name FROM products p ${CARD_JOIN} LEFT JOIN brands b ON b.id = p.brand_id WHERE p.id = ?`).bind(id),
    db.prepare('SELECT id, feed, title, domain, price, price_old, stock, go_slug, target_url, updated_at, img, delivery_price, sizes, variants, extra FROM offers WHERE product_id = ? AND active = 1 ORDER BY (stock = -1), price ASC').bind(id),
    db.prepare('SELECT cat_id FROM cat_products WHERE product_id = ? AND direct = 1').bind(id),
    db.prepare('SELECT day, min_price FROM price_history WHERE product_id = ? ORDER BY day').bind(id),
    db.prepare('SELECT key, value FROM product_params WHERE product_id = ?').bind(id),
  ]);
  const row = (p!.results[0] as (Product & { b_slug: string | null; b_name: string | null }) | undefined) ?? null;
  if (!row) return null;
  const { b_slug, b_name, ...product } = row;
  const brand = product.brand_id && b_slug ? { id: product.brand_id, slug: b_slug, name: b_name ?? '' } : null;
  const prm: Record<string, string[]> = {};
  for (const r of params!.results as Array<{ key: string; value: string }>) (prm[r.key] ??= []).push(r.value);
  return {
    product: product as Product,
    offers: offers!.results as Offer[],
    catIds: (cats!.results as Array<{ cat_id: number }>).map((r) => r.cat_id),
    history: hist!.results as Array<{ day: string; min_price: number }>,
    brand,
    params: prm,
  };
}

/** Similar products: same primary category, closest in price (two range scans on idx_cp_price), with offers. */
export async function relatedProducts(db: D1Database, catId: number, exclude: number, price: number, n = 8, created = ''): Promise<Card[]> {
  if (!catId) return [];
  // static export: neighbours in the PK order (date added, then id — the whole first import shares one date), not by price — a neighbour's price change must not change this
  // page, so only really changed products are rendered and uploaded every week (the cards show no price there)
  const [older, newer] = await db.batch(isStatic() && created ? [
    db.prepare(`SELECT ${CARD_COLS} FROM cat_products x JOIN products p ON p.id = x.product_id ${CARD_JOIN} WHERE x.cat_id = ? AND (x.created_at, x.product_id) < (?, ?) AND p.status = 'publish' ORDER BY x.created_at DESC, x.product_id DESC LIMIT ?`).bind(catId, created, exclude, n),
    db.prepare(`SELECT ${CARD_COLS} FROM cat_products x JOIN products p ON p.id = x.product_id ${CARD_JOIN} WHERE x.cat_id = ? AND (x.created_at, x.product_id) > (?, ?) AND p.status = 'publish' ORDER BY x.created_at ASC, x.product_id ASC LIMIT ?`).bind(catId, created, exclude, n),
  ] : [
    db.prepare(`SELECT ${CARD_COLS} FROM cat_products x JOIN products p ON p.id = x.product_id ${CARD_JOIN} WHERE x.cat_id = ? AND x.min_price > 0 AND x.min_price < ? AND p.status = 'publish' ORDER BY x.min_price DESC LIMIT ?`).bind(catId, price, n),
    db.prepare(`SELECT ${CARD_COLS} FROM cat_products x JOIN products p ON p.id = x.product_id ${CARD_JOIN} WHERE x.cat_id = ? AND x.min_price >= ? AND p.status = 'publish' ORDER BY x.min_price ASC LIMIT ?`).bind(catId, price, n + 1),
  ]);
  const a = older!.results as Card[];
  const b = newer!.results as Card[];
  const out: Card[] = [];
  for (let i = 0; out.length < n && (i < a.length || i < b.length); i++) {
    if (a[i] && a[i]!.id !== exclude) out.push(a[i]!);
    if (out.length < n && b[i] && b[i]!.id !== exclude) out.push(b[i]!);
  }
  return out;
}

export async function cardsByIds(db: D1Database, ids: number[]): Promise<Card[]> {
  if (!ids.length) return [];
  const rows = (await db.prepare(`SELECT ${CARD_COLS} FROM products p ${CARD_JOIN} WHERE p.id IN (${ids.slice(0, 90).map(() => '?').join(',')}) AND p.status = 'publish'`).bind(...ids.slice(0, 90)).all<Card>()).results;
  const by = new Map(rows.map((r) => [r.id, r]));
  return ids.map((i) => by.get(i)).filter((x): x is Card => !!x);
}

export async function loadBrand(db: D1Database, slug: string): Promise<Brand | null> {
  return db.prepare('SELECT * FROM brands WHERE slug = ?').bind(slug).first<Brand>();
}

export async function loadPost(db: D1Database, id: number): Promise<Post | null> {
  return db.prepare('SELECT * FROM posts WHERE id = ? AND status = \'publish\'').bind(id).first<Post>();
}

const POST_CARD = 'id, slug, title, excerpt, published_at, image, image_card, image_alt, image_w, image_h, cat_id';
export async function listPosts(db: D1Database, page: number, catId?: number): Promise<{ items: PostCard[]; total: number }> {
  const where = "type = 'post' AND status = 'publish'" + (catId ? ' AND cat_id = ?' : '');
  const b = catId ? [catId] : [];
  const [a, c] = await db.batch([
    db.prepare(`SELECT ${POST_CARD} FROM posts WHERE ${where} ORDER BY published_at DESC LIMIT ${POSTS_PER_PAGE} OFFSET ${(page - 1) * POSTS_PER_PAGE}`).bind(...b),
    db.prepare(`SELECT COUNT(*) AS n FROM posts WHERE ${where}`).bind(...b),
  ]);
  return { items: a!.results as PostCard[], total: Number((c!.results[0] as { n: number }).n) };
}
export async function postsBySlugs(db: D1Database, slugs: string[]): Promise<PostCard[]> {
  if (!slugs.length) return [];
  const rows = (await db.prepare(`SELECT ${POST_CARD} FROM posts WHERE type = 'post' AND status = 'publish' AND slug IN (${slugs.map(() => '?').join(',')})`).bind(...slugs).all<PostCard & { slug: string }>()).results;
  const by = new Map(rows.map((r) => [r.slug, r]));
  return slugs.map((s) => by.get(s)).filter((x): x is PostCard => !!x);
}
export async function latestPosts(db: D1Database, n = 4): Promise<PostCard[]> {
  return (await db.prepare(`SELECT ${POST_CARD} FROM posts WHERE type = 'post' AND status = 'publish' ORDER BY published_at DESC LIMIT ?`).bind(n).all<PostCard>()).results;
}
export async function relatedPosts(db: D1Database, post: Post, n = 4): Promise<PostCard[]> {
  return (await db.prepare(`SELECT ${POST_CARD} FROM posts WHERE type = 'post' AND status = 'publish' AND id <> ? AND cat_id = ? ORDER BY published_at DESC LIMIT ?`).bind(post.id, post.cat_id, n).all<PostCard>()).results;
}
export async function postCat(db: D1Database, id: number): Promise<PostCat | null> {
  return db.prepare('SELECT * FROM post_categories WHERE id = ?').bind(id).first<PostCat>();
}
/** FTS5 product search (name + brand), diacritics-insensitive. Prefix match on every term. */
export async function searchProducts(db: D1Database, query: string, page: number): Promise<{ items: Card[]; total: number }> {
  const terms = query.toLowerCase().normalize('NFKC').split(/[^\p{L}\p{N}]+/u).filter((t) => t.length > 1).slice(0, 6);
  if (!terms.length) return { items: [], total: 0 };
  const match = terms.map((t) => `"${t.replace(/"/g, '')}"*`).join(' ');
  const off = (page - 1) * PER_PAGE;
  const [ids, cnt] = await db.batch([
    db.prepare(`SELECT rowid AS id FROM product_fts WHERE product_fts MATCH ? ORDER BY rank LIMIT ${PER_PAGE} OFFSET ${off}`).bind(match),
    db.prepare('SELECT COUNT(*) AS n FROM product_fts WHERE product_fts MATCH ?').bind(match),
  ]);
  const list = (ids!.results as Array<{ id: number }>).map((r) => r.id);
  return { items: await cardsByIds(db, list), total: Number((cnt!.results[0] as { n: number }).n) };
}

export async function siteCache(db: D1Database, key: string): Promise<string | null> {
  return (await db.prepare('SELECT value FROM site_cache WHERE key = ?').bind(key).first<{ value: string }>())?.value ?? null;
}

/** Search suggestions: up to 6 products (FTS prefix match) as small cards. */
export async function suggestProducts(db: D1Database, query: string): Promise<Card[]> {
  const terms = query.toLowerCase().normalize('NFKC').split(/[^\p{L}\p{N}]+/u).filter((t) => t.length > 1).slice(0, 6);
  if (!terms.length) return [];
  const match = terms.map((t) => `"${t.replace(/"/g, '')}"*`).join(' ');
  const ids = (await db.prepare('SELECT rowid AS id FROM product_fts WHERE product_fts MATCH ? ORDER BY rank LIMIT 6').bind(match).all<{ id: number }>()).results.map((r) => r.id);
  return cardsByIds(db, ids);
}
