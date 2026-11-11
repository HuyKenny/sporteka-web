// View models for each page type: data from D1 + SEO meta (title, description, canonical, prev/next, robots, JSON-LD)
// matching the WordPress/Rank Math output. Templates only render what these return.
import { renderNow } from './now';
import {
  ancestry, brandList, catImages, catTree, cardsByIds, facets, listDiscounted, listPosts, listProducts, loadBrand, loadCategory, loadPost, loadProduct,
  postCat, latestPosts, relatedPosts, relatedProducts, searchProducts, siteCache,
  type Card, type Cat, type Offer, type Post, type PostCard,
} from './db';
import { isFiltered, parseFilters, toListQuery, toQuery } from './filters';
import { BASE, OG_DEFAULT, PER_PAGE, POSTS_PER_PAGE, isoPrague } from './site';
import { isStatic } from './server/env';

// the static export renders at most 100 pages per listing (12 000 pages of "sportovni-obuv" are not worth files;
// every product stays reachable through the sitemaps and its categories' first pages)
const STATIC_MAX_PAGES = 100;
const capPages = (n: number) => (isStatic() ? Math.min(n, STATIC_MAX_PAGES) : n);
import { categoryTitle, descFrom, postTitle, productTitle, rmTitle, robots, searchTitle, termTitle } from './seo';
import { cislo, decode, stripTags } from './format';
import { validImage } from './img';

export interface Meta {
  title: string; description: string; canonical?: string; prev?: string; next?: string; robots: string[];
  ogType?: string; ogImage?: string; graph: unknown[]; jsonLd: unknown[]; extraMeta?: Array<{ property?: string; name?: string; content: string }>;
  /** Rank Math prints a short Organization node (no logo) on product-category archives. */
  shortOrg?: boolean;
}
export interface Crumb { name: string; url?: string }

const abs = (p: string) => BASE + p;
const pagePath = (base: string, n: number) => (n <= 1 ? base : `${base}page/${n}/`);
function breadcrumbLd(items: Crumb[]) {
  return {
    '@context': 'https://schema.org', '@type': 'BreadcrumbList',
    itemListElement: items.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c.name, item: abs(c.url ?? '/') })),
  };
}
function itemListLd(url: string, name: string, items: Card[], total = 0) {
  const list = items.slice(0, 24);
  if (!list.length) return null;
  return {
    '@context': 'https://schema.org', '@type': 'ItemList', '@id': url + '#products', name, numberOfItems: Math.max(total, list.length),
    itemListElement: list.map((p, i) => ({ '@type': 'ListItem', position: i + 1, url: abs(`/${p.slug}/`), name: decode(p.name) })),
  };
}
function collection(url: string, title: string) {
  return { '@type': 'CollectionPage', '@id': url + '#webpage', url, name: title, isPartOf: { '@id': BASE + '/#website' }, inLanguage: 'cs' };
}

// ---------- category ----------
import { FACET_TEXTS, hasFacetText } from './facet-texts';
import brandTexts from '../texts/znacky.json';
const BRAND_TEXTS = brandTexts as unknown as Record<string, { seo_title?: string; seo_desc?: string; description_html?: string; guide_html?: string; faq_json?: string }>;
export interface FacetPage {
  id: number; slug: string; base_slug: string; qs: string; h1: string; seo_title: string; seo_desc: string; intro_html: string; second_html: string;
  faq_json: string; keyword: string; volume: number; min_products: number; total: number; noindex: number;
}
/** Facet landing = its base category with a preset filter (fp.qs) and its own texts; filters added by the visitor on top make it noindex like any filtered listing. */
export async function facetView(db: D1Database, id: number, page: number, sp: URLSearchParams) {
  const fp = await db.prepare('SELECT * FROM facet_pages WHERE id = ?').bind(id).first<FacetPage>();
  if (!fp) return null;
  const tree = await catTree(db);
  const base = tree.bySlug.get(fp.base_slug);
  if (!base) return null;
  const merged = new URLSearchParams(fp.qs);
  for (const k of new Set([...sp.keys()])) { merged.delete(k); for (const v of sp.getAll(k)) merged.append(k, v); }
  return categoryView(db, base.id, page, merged, { fp, user: sp });
}

export async function categoryView(db: D1Database, catId: number, page: number, sp: URLSearchParams, facet?: { fp: FacetPage; user: URLSearchParams }) {
  const [cat0, tree, fc, brands, imgs, lands] = await Promise.all([loadCategory(db, catId), catTree(db), facets(db, `f:${catId}`), brandList(db), catImages(db),
    facet ? Promise.resolve([] as FacetPage[]) : db.prepare('SELECT * FROM facet_pages WHERE noindex = 0 AND total >= min_products AND base_slug = (SELECT slug FROM categories WHERE id = ?)').bind(catId).all<FacetPage>().then((r) => r.results.filter((x) => hasFacetText(x.slug))).catch(() => [] as FacetPage[])]);
  if (!cat0) return null;
  const fp = facet?.fp;
  // a facet shows its own texts instead of the category's; the icon and the tree position stay the base category's
  // hand-written landing texts (src/texts/fasety.json, no D1 write) replace the generated template
  const ft = fp ? FACET_TEXTS[fp.slug] : undefined;
  const cat = fp ? { ...cat0, name: fp.h1, seo_title: ft?.seo_title ?? fp.seo_title, seo_desc: ft?.seo_desc ?? fp.seo_desc, description_html: ft?.description_html ?? fp.intro_html, second_html: ft ? '' : fp.second_html, guide_html: ft?.guide_html ?? '', faq_json: ft?.faq_json ?? fp.faq_json, seo_robots: '' } : cat0;
  const f = parseFilters(sp);
  const filtered = fp ? isFiltered(parseFilters(facet!.user)) : isFiltered(f);
  // facet landings of this category: filter value → landing slug (the filter links lead to the clean URL)
  const landings: Record<string, string> = {};
  for (const l of lands) { const k = only(parseFilters(new URLSearchParams(l.qs))); if (k) landings[k] = l.slug; }
  // the plain filter of exactly one landing value → 301 to the landing (one indexable URL per combination)
  if (!fp && filtered && page === 1) {
    const one = only(f);
    if (one && landings[one]) return { redirect: `/${landings[one]}/` } as const;
  }
  const q = toListQuery(f, page, brands, fc);
  const { items, total } = await listProducts(db, { cat: cat.id }, q, fp ? undefined : cat.count_total);
  const pages = capPages(Math.max(1, Math.ceil(total / PER_PAGE)));
  if (page > pages) return null;
  const chain = ancestry(tree, cat.id);
  // subcategory tiles: indexable categories with at least 3 products (merged clones are noindex), all of them
  const tile = (c: Cat) => c.count_total >= 3 && !c.noindex;
  let kids = (tree.kids.get(cat.id) ?? []).filter(tile);
  let kidsTitle = 'Podkategorie';
  if (!kids.length && cat.parent) {
    kids = (tree.kids.get(cat.parent) ?? []).filter((c) => tile(c) && c.id !== cat.id);
    kidsTitle = 'Související kategorie';
  }
  kids = kids.sort((a, b) => b.count_total - a.count_total);
  const base = fp ? `/${fp.slug}/` : `/${cat.slug}/`;
  const url = abs(pagePath(base, page));
  const title = categoryTitle(cat.name, cat.seo_title, page, fp || (fc?.lo ?? 0) < 100 ? 0 : fc!.lo);
  const crumbs: Crumb[] = [{ name: 'Domů', url: '/' }, ...chain.map((c) => ({ name: decode(c.name), url: `/${c.slug}/` })), ...(fp ? [{ name: fp.h1, url: base }] : [])];
  // robots as on WordPress (live snapshot at the migration: thin categories outside the priority list are noindex),
  // plus an emptied category
  const noindex = fp ? fp.noindex === 1 || total < fp.min_products || !hasFacetText(fp.slug) : cat.noindex === 1 || cat.seo_robots.includes('noindex') || cat.count_total === 0;
  let faq: Array<{ q: string; a: string }> = [];
  try { faq = page === 1 && cat.faq_json ? JSON.parse(cat.faq_json) : []; } catch { /* broken JSON = no FAQ */ }
  const meta: Meta = {
    title, description: descFrom(cat.seo_desc, cat.description_html, { term: decode(cat.name), clamp: true },
      fc?.n ? `Porovnejte ceny ${cislo(fc.n)} produktů z kategorie ${decode(cat.name)} v ${fc.s.length} ověřených e-shopech.${fc.lo ? ` Ceny od ${cislo(fc.lo)} Kč, velikosti skladem a filtry podle značky.` : ''}` : '', page),
    // filtered / re-sorted listings: noindex, follow and no canonical (the indexable listing is the plain URL)
    ...(noindex || filtered ? {} : { canonical: url }), robots: filtered ? ['noindex', 'follow'] : robots(noindex, cat.seo_robots),
    ...(page > 1 && !filtered ? { prev: abs(pagePath(base, page - 1)) } : {}),
    ...(page < pages && !filtered ? { next: abs(pagePath(base, page + 1)) } : {}),
    // Rank Math + ah-seo.php: the page node is a FAQPage when the category has its FAQ, breadcrumb and item list in the graph
    graph: [
      collection(url, title),
      ...(faq.length ? [{ '@type': 'FAQPage', '@id': url + '#faq', mainEntity: faq.map((x) => ({ '@type': 'Question', name: stripTags(x.q), acceptedAnswer: { '@type': 'Answer', text: stripTags(x.a) } })) }] : []),
      { ...breadcrumbLd(crumbs), '@context': undefined, '@id': BASE + '/#breadcrumb' },
      ...(items.length ? [{ ...itemListLd(abs(base), decode(cat.name), items.slice(0, 24), total)!, '@context': undefined }] : []),
    ],
    jsonLd: [], shortOrg: true, ogType: 'website',
  };
  return {
    meta, cat, crumbs, items, total, page, pages, base, f, qs: toQuery(fp ? parseFilters(facet!.user) : f), kids, kidsTitle, tree, fc, brands, imgs, landings, faq,
    popular: [...lands].sort((x, y) => y.volume - x.volume).slice(0, 12).map((l) => ({ slug: l.slug, h1: l.h1 })),
    guide: page === 1 && !filtered ? cat.guide_html : '',
    isFiltered: filtered,
  };
}

/** `key=value` when the filter state is a single brand or a single parameter value and nothing else, else null. */
function only(f: ReturnType<typeof parseFilters>): string | null {
  if (f.sort !== 'pop' || f.min !== undefined || f.max !== undefined || f.obchod.length || f.skladem || f.kat) return null;
  if (f.sleva) return f.znacka.length || Object.keys(f.p).length ? null : 'sleva=1';
  const ps = Object.entries(f.p);
  if (f.znacka.length === 1 && !ps.length) return `brand=${f.znacka[0]}`;
  if (!f.znacka.length && ps.length === 1 && ps[0]![1]!.length === 1) return `${ps[0]![0]}=${ps[0]![1]![0]}`;
  return null;
}

// ---------- brand ----------
export async function brandView(db: D1Database, slug: string, page: number, sp: URLSearchParams) {
  const [b0, tree, brands] = await Promise.all([loadBrand(db, slug), catTree(db), brandList(db)]);
  if (!b0) return null;
  // hand-written brand texts (src/texts/znacky.json) win over the generic ones
  const bt = BRAND_TEXTS[b0.slug];
  const b = bt ? { ...b0, seo_title: bt.seo_title ?? b0.seo_title, seo_desc: bt.seo_desc ?? b0.seo_desc, description_html: bt.description_html ?? b0.description_html, second_html: bt.guide_html ?? b0.second_html, faq_json: bt.faq_json ?? b0.faq_json } : b0;
  const fc = await facets(db, `fb:${b.id}`);
  const f = parseFilters(sp);
  f.znacka = [];
  const filtered = isFiltered(f);
  const q = toListQuery(f, page, brands, fc, tree);
  const { items, total } = await listProducts(db, { brand: b.id }, q, b.count);
  const pages = capPages(Math.max(1, Math.ceil(total / PER_PAGE)));
  if (page > pages && page > 1) return null;
  const base = `/znacka/${b.slug}/`;
  const url = abs(pagePath(base, page));
  // page 2+ kept Rank Math's plain term title on WordPress (the mu-plugin template only ran on page 1)
  const title = page > 1 ? termTitle(b.name, page) : (b.seo_title ? rmTitle(b.seo_title, decode(b.name)) : brandSeo(b).title);
  // WordPress indexed every brand with a product (Rank Math default); the sitemap lists those with ≥ 3
  const thin = b.noindex === 1 || b.count < 1;
  const crumbs: Crumb[] = [{ name: 'Domů', url: '/' }, { name: decode(b.name), url: base }];
  let faq: Array<{ q: string; a: string }> = [];
  try { faq = page === 1 && b.faq_json ? JSON.parse(b.faq_json) : []; } catch { /* broken JSON = no FAQ */ }
  const meta: Meta = {
    title, description: descFrom(b.seo_desc, '', {}, brandSeo(b).desc, page),
    ...(thin || filtered ? {} : { canonical: url }), robots: filtered ? ['noindex', 'follow'] : robots(thin),
    ...(page > 1 && !filtered ? { prev: abs(pagePath(base, page - 1)) } : {}),
    ...(page < pages && !filtered ? { next: abs(pagePath(base, page + 1)) } : {}),
    graph: [faq.length ? { ...collection(url, title), '@type': 'FAQPage', mainEntity: faq.map((x) => ({ '@type': 'Question', name: stripTags(x.q), acceptedAnswer: { '@type': 'Answer', text: stripTags(x.a) } })) } : collection(url, title)],
    jsonLd: [breadcrumbLd(crumbs), itemListLd(abs(base), decode(b.name), items)].filter(Boolean),
  };
  return { meta, faq, brand: b, crumbs, items, total, page, pages, base, f, qs: toQuery(f), tree, fc, brands, isFiltered: filtered };
}

/** Title/description of brands without their own texts. */
function brandSeo(b: { slug: string; name: string; count: number }): { title: string; desc: string } {
  const name = decode(b.name).replace(/\s*[–-]\s*/g, ' ').trim();
  const n = b.count;
  return {
    title: `${name} – sortiment a srovnání cen | Sporteka`,
    desc: `${name}: ${n} ${n >= 5 ? 'produktů' : n >= 2 ? 'produkty' : 'produkt'} na jednom místě. Porovnejte ceny sportovních e-shopů, vyberte velikost a vyhledejte nabídku s dobrou cenou.`,
  };
}

// ---------- search ----------
export async function searchView(db: D1Database, query: string, page: number) {
  const [tree, brands] = await Promise.all([catTree(db), brandList(db)]);
  const { items, total } = await searchProducts(db, query, page);
  const pages = Math.max(1, Math.ceil(total / PER_PAGE));
  const meta: Meta = { title: searchTitle(query, page, pages), description: '', robots: ['follow', 'noindex'], graph: [], jsonLd: [] };
  const { cats, brs } = matchNames(query, tree, brands);
  return { meta, query, items, total, page, pages, tree, cats, brs };
}

/** Categories and brands whose name contains every typed word (diacritics-insensitive) — search page + suggestions. */
export function matchNames(query: string, tree: Awaited<ReturnType<typeof catTree>>, brands: Awaited<ReturnType<typeof brandList>>) {
  const fold = (t: string) => decode(t).normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const words = fold(query).split(/[^a-z0-9]+/).filter((w) => w.length > 1);
  if (!words.length) return { cats: [] as Cat[], brs: [] as Array<{ slug: string; name: string; count: number }> };
  const hit = (name: string) => { const n = fold(name); return words.every((w) => n.includes(w)); };
  const cats = [...tree.byId.values()].filter((c) => c.count_total > 0 && !c.noindex && hit(c.name)).sort((a, b) => b.count_total - a.count_total).slice(0, 6);
  const brs = [...brands.byId.values()].filter((b) => b.slug !== 'ostatni' && hit(b.name)).sort((a, b) => b.count - a.count).slice(0, 6);
  return { cats, brs };
}

// ---------- /slevy/ ----------
export async function discountView(db: D1Database, page: number, sp: URLSearchParams) {
  const [tree, brands, fc] = await Promise.all([catTree(db), brandList(db), facets(db, 'f:slevy')]);
  const f = parseFilters(sp);
  const filtered = isFiltered(f);
  const listed = await listDiscounted(db, toListQuery(f, page, brands, fc, tree));
  const items = listed.items;
  // unfiltered: the real number from the facets; the paging itself stops at 200 pages (OFFSET on 50 000 rows is not worth it)
  const total = !filtered && fc?.n ? fc.n : listed.total;
  const pages = capPages(Math.max(1, Math.min(200, Math.ceil(total / PER_PAGE))));
  if (page > pages) return null;
  const base = '/slevy/';
  const url = abs(pagePath(base, page));
  const title = `Slevy na sportovní vybavení a oblečení${page > 1 ? ` – strana ${page}` : ''} | Sporteka`;
  const description = `Největší slevy na sportovní vybavení, oblečení a obuv: ${cislo(fc?.n ?? total)} zlevněných produktů z českých e-shopů, seřazeno podle výše slevy. Filtrujte podle sportu, značky, velikosti a ceny.`;
  const crumbs: Crumb[] = [{ name: 'Domů', url: '/' }, { name: 'Slevy' }];
  const meta: Meta = {
    title, description, ...(filtered ? {} : { canonical: url }), robots: filtered ? ['noindex', 'follow'] : robots(false),
    ...(page > 1 && !filtered ? { prev: abs(pagePath(base, page - 1)) } : {}), ...(page < pages && !filtered ? { next: abs(pagePath(base, page + 1)) } : {}),
    graph: [collection(url, title)], jsonLd: [{ ...breadcrumbLd([{ name: 'Domů', url: '/' }, { name: 'Slevy', url: base }]), '@context': undefined, '@id': BASE + '/#breadcrumb' }], shortOrg: true,
  };
  return { meta, crumbs, items, total, page, pages, f, fc, brands, cats: tree.byId, base, qs: toQuery(f), isFiltered: filtered };
}

// ---------- product ----------
export async function productView(db: D1Database, id: number) {
  const [data, tree] = await Promise.all([loadProduct(db, id), catTree(db)]);
  if (!data) return null;
  const { product: p, offers, catIds, history, brand, params } = data;
  const name = decode(p.name);
  // breadcrumb/category: a noindex category (e.g. "Ostatní") only when the product has no other
  const cats = [p.primary_cat, ...catIds].map((i) => tree.byId.get(i)).filter((c): c is Cat => !!c);
  const primary = cats.find((c) => !c.noindex) ?? cats[0];
  const chain = primary ? ancestry(tree, primary.id) : [];
  const url = abs(`/${p.slug}/`);
  const title = productTitle(p.name, p.seo_title);
  // seo_desc = Rank Math description or the raw (untexturized) short description from the migration
  const prices0 = offers.map((o) => o.price);
  const description = descFrom(p.seo_desc, p.short_html, { title: name, clamp: true },
    offers.length ? `${name}: ${new Set(offers.map((o) => o.domain)).size > 1 ? `porovnejte ceny v ${new Set(offers.map((o) => o.domain)).size} obchodech` : 'cena, velikosti skladem a vývoj ceny'}, ceny od ${cislo(Math.min(...prices0))} Kč.` : '');
  // without any offer the page is thin and a Product snippet without offers is invalid → noindex, no Product node
  const noindex = p.noindex === 1 || offers.length === 0;
  const inStock = offers.filter((o) => o.stock !== -1);
  const best: Offer | undefined = (inStock.length ? inStock : offers)[0];
  const prices = offers.map((o) => o.price);
  const stats = { n: offers.length, shops: new Set(offers.map((o) => o.domain)).size, min: prices.length ? Math.min(...prices) : 0, max: prices.length ? Math.max(...prices) : 0 };
  const img = validImage(p.image);
  const crumbs: Crumb[] = [{ name: 'Domů', url: '/' }, ...chain.map((c) => ({ name: decode(c.name), url: `/${c.slug}/` })), { name, url: `/${p.slug}/` }];
  const skip = new Set(['ostatni', 'nezarazene', 'uncategorized']);
  const relCats = catIds.map((cid) => tree.byId.get(cid)).filter((c): c is Cat => !!c && !skip.has(c.slug)).slice(0, 6);
  const related = await relatedProducts(db, primary?.id ?? 0, p.id, p.min_price || 0, 8, p.created_at);
  let gallery: string[] = [];
  try { gallery = p.images ? (JSON.parse(p.images) as string[]).map(validImage).filter(Boolean) : []; } catch { /* no gallery */ }
  const graph: unknown[] = [
    ...(img ? [{ '@type': 'ImageObject', '@id': img, url: img, inLanguage: 'cs' }] : []),
    { '@type': 'ItemPage', '@id': url + '#webpage', url, name: title, datePublished: isoPrague(p.created_at), dateModified: isoPrague(p.updated_at), isPartOf: { '@id': BASE + '/#website' }, ...(img ? { primaryImageOfPage: { '@id': img } } : {}), inLanguage: 'cs' },
    ...(offers.length ? [{
      '@type': 'Product', '@id': url + '#richSnippet', name, description, sku: String(p.id),
      ...(brand && brand.slug !== 'ostatni' ? { brand: { '@type': 'Brand', name: decode(brand.name) } } : {}),
      ...(primary ? { category: decode(primary.name) } : {}),
      mainEntityOfPage: { '@id': url + '#webpage' },
      ...(p.ean ? { gtin: p.ean } : {}),
      ...(img ? { image: [{ '@type': 'ImageObject', url: img }] } : {}),
      // price comparison: one AggregateOffer over all shops (lowPrice/highPrice/offerCount)
      ...(best ? {
        offers: {
          '@type': 'AggregateOffer', priceCurrency: 'CZK', lowPrice: String(Math.round(stats.min)), highPrice: String(Math.round(stats.max)), offerCount: String(stats.n),
          availability: inStock.length ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock', itemCondition: 'https://schema.org/NewCondition', url,
          // Rank Math filter on WordPress: Google warns about offers without it; prices are refreshed nightly
          priceValidUntil: new Date(renderNow() + 30 * 86400_000).toISOString().slice(0, 10),
        },
      } : {}),
    }] : []),
  ];
  const meta: Meta = {
    title, description, ...(noindex ? {} : { canonical: url }), robots: robots(noindex), ogType: 'product', ogImage: img || OG_DEFAULT, graph,
    jsonLd: [breadcrumbLd(crumbs)],
    extraMeta: [
      { property: 'og:updated_time', content: isoPrague(p.updated_at) },
      ...(best ? [{ property: 'product:price:amount', content: String(Math.round(best.price)) }, { property: 'product:price:currency', content: 'CZK' }, { property: 'product:availability', content: best.stock === -1 ? 'out of stock' : 'instock' }] : []),
    ],
  };
  // mu-plugin C2: context line links the first category with ≥ 3 products
  const ctxCat = catIds.map((cid) => tree.byId.get(cid)).find((c): c is Cat => !!c && c.count_direct >= 3) ?? null;
  return { meta, p, name, offers, best, stats, history, brand, primary, crumbs, relCats, related, tree, img, gallery, params, ctxCat };
}

/** Split the product description at the empty Content Egg headings ("Porovnání cen …", "Vývoj ceny …"):
 *  their blocks (offer table, price chart) are rendered by the template in the same place. */
export function splitDescription(html: string): { before: string; offersHeading: string; middle: string; historyHeading: string; after: string } {
  const re = (w: string) => new RegExp(`<h3[^>]*>\\s*${w}[^<]*</h3>`, 'i');
  let s = html;
  const mo = re('Kde koupit').exec(s);
  const out = { before: s, offersHeading: '', middle: '', historyHeading: '', after: '' };
  if (mo) {
    out.before = s.slice(0, mo.index);
    out.offersHeading = mo[0];
    s = s.slice(mo.index + mo[0].length);
    out.middle = s;
  }
  const mh = re('Vývoj ceny').exec(mo ? out.middle : out.before);
  if (mh) {
    const src = mo ? out.middle : out.before;
    const head = src.slice(0, mh.index);
    if (mo) out.middle = head; else out.before = head;
    out.historyHeading = mh[0];
    out.after = src.slice(mh.index + mh[0].length);
  }
  return out;
}

// ---------- posts / pages ----------
export async function postView(db: D1Database, id: number) {
  const post = await loadPost(db, id);
  if (!post) return null;
  const url = abs(`/${post.slug}/`);
  const title = postTitle(post.title, post.seo_title);
  const description = descFrom(post.seo_desc, post.excerpt || post.content_html, { title: decode(post.title) });
  const img = post.image;
  // JSON-LD exactly as WordPress printed it (live snapshot at the migration: Rank Math + mu-plugin FAQPage/Recipe/
  // WebApplication/E-E-A-T nodes); built here only for posts written after the migration
  let live: { graph: unknown[]; extra: unknown[] } | null = null;
  try { live = post.ld_json ? JSON.parse(post.ld_json) : null; } catch { live = null; }
  if (post.type === 'page') {
    const meta: Meta = {
      title, description, ...(post.noindex ? {} : { canonical: url }), robots: robots(post.noindex === 1, post.seo_robots), ogImage: img || OG_DEFAULT,
      graph: live?.graph ?? [{ '@type': 'WebPage', '@id': url + '#webpage', url, name: title, datePublished: isoPrague(post.published_at), dateModified: isoPrague(post.modified_at), isPartOf: { '@id': BASE + '/#website' }, inLanguage: 'cs' }],
      jsonLd: live?.extra ?? [],
    };
    return { meta, post, cat: null, related: [] as PostCard[], shopCats: [] as Cat[] };
  }
  const [cat, latest] = await Promise.all([postCat(db, post.cat_id), relatedPosts(db, post, 4)]);
  const related = latest.slice(0, 4);
  const name = post.author || 'Sporteka.cz';
  const author = { '@type': 'Person', '@id': url + '#author', name, worksFor: { '@id': BASE + '/#organization' } };
  const built: unknown[] = [
    ...(img ? [{ '@type': 'ImageObject', '@id': img, url: img, ...(post.image_w ? { width: String(post.image_w), height: String(post.image_h) } : {}), ...(post.image_alt ? { caption: post.image_alt } : {}), inLanguage: 'cs' }] : []),
    { '@type': 'WebPage', '@id': url + '#webpage', url, name: title, datePublished: isoPrague(post.published_at), dateModified: isoPrague(post.modified_at), isPartOf: { '@id': BASE + '/#website' }, ...(img ? { primaryImageOfPage: { '@id': img } } : {}), inLanguage: 'cs' },
    author,
    {
      '@type': 'BlogPosting', headline: title, description, datePublished: isoPrague(post.published_at), dateModified: isoPrague(post.modified_at),
      author: { '@id': author['@id'], name }, publisher: { '@id': BASE + '/#organization' }, ...(img ? { image: { '@id': img } } : {}),
      inLanguage: 'cs', '@id': url + '#richSnippet', isPartOf: { '@id': url + '#webpage' }, mainEntityOfPage: { '@id': url + '#webpage' },
    },
    breadcrumbLd([{ name: 'Domů', url: '/' }, { name: 'Magazín', url: '/blog/' }, { name: decode(post.title), url: `/${post.slug}/` }]),
  ];
  const graph = live?.graph ?? built;
  const meta: Meta = {
    title, description, ...(post.noindex ? {} : { canonical: url }), robots: robots(post.noindex === 1, post.seo_robots), ogImage: img || OG_DEFAULT, graph, jsonLd: live?.extra ?? [],
    extraMeta: [{ property: 'article:published_time', content: isoPrague(post.published_at) }, { property: 'article:modified_time', content: isoPrague(post.modified_at) }],
  };
  return { meta, post, cat, related, shopCats: [] as Cat[] };
}

export async function blogView(db: D1Database, page: number, catId?: number) {
  const { items, total } = await listPosts(db, page, catId);
  const pages = Math.max(1, Math.ceil(total / POSTS_PER_PAGE));
  if (page > pages && page > 1) return null;
  const cat = catId ? await postCat(db, catId) : null;
  const base = cat ? `/${cat.slug}/` : '/blog/';
  const url = abs(pagePath(base, page));
  // titles/descriptions of the live site (snapshot, src/data/postcat-seo.json)
  const seo = null as { title: string; desc: string; h1: string } | null;
  const title = termTitle(cat ? cat.name : 'Rádce', page);
  const meta: Meta = {
    title, description: descFrom(seo?.desc ?? '', cat ? cat.description : '', {}, cat ? `Články z rubriky ${decode(cat.name)} v rádci Sporteka.cz.` : 'Rádce Sporteka.cz: jak vybrat sportovní vybavení.', page),
    canonical: url, robots: robots(false),
    ...(page > 1 ? { prev: abs(pagePath(base, page - 1)) } : {}),
    ...(page < pages ? { next: abs(pagePath(base, page + 1)) } : {}),
    graph: [collection(url, title)], jsonLd: [],
  };
  return { meta, items, total, page, pages, base, cat, h1: seo?.h1 ?? '' };
}

export interface HomeBlocks { deals: number[]; popular: number[]; brands: Array<[number, number]>; shops: Array<[string, number]>; products: number; offers: number }
export async function homeView(db: D1Database) {
  const [tree, brands, imgs, raw, mag] = await Promise.all([catTree(db), brandList(db), catImages(db), siteCache(db, 'home'), latestPosts(db, 4)]);
  let home: HomeBlocks = { deals: [], popular: [], brands: [], shops: [], products: 0, offers: 0 };
  try { if (raw) home = JSON.parse(raw) as HomeBlocks; } catch { /* nightly block missing */ }
  const cards = await cardsByIds(db, [...home.deals, ...home.popular]);
  const by = new Map(cards.map((c) => [c.id, c]));
  const pick = (ids: number[]) => ids.map((i) => by.get(i)).filter((x): x is Card => !!x);
  return { tree, brands, imgs, home, deals: pick(home.deals), popular: pick(home.popular), mag };
}

export type { Card, Cat, Post, PostCard };
