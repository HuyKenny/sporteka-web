// Listing filters and sort in the URL (category, brand): parse → ListQuery for db.ts, serialise back for links.
//   ?orderby=price|price-desc|date|disc   (default = popularity; WooCommerce "popularity" is accepted)
//   ?min_price= &max_price=  ?znacka=a,b  ?obchod=ruzovyslon.cz  ?skladem=1  ?sleva=1  ?kat=<slug> (brand pages)
//   ?p_barva=cerna,ruzova  ?p_delka=12-16 …
// Any filter or a non-default sort makes the page noindex (views.ts) — the indexable listing is the plain URL.
import type { BrandLite, Cat, Facets, ListQuery, Sort } from './db';
import { BUCKETS, PARAM_ORDER, valueSlug, type ParamKey } from './params';

export interface FilterState {
  sort: Sort; min?: number | undefined; max?: number | undefined;
  znacka: string[]; obchod: string[]; skladem: boolean; sleva: boolean; kat: string;
  p: Partial<Record<ParamKey, string[]>>;
}
export const SORTS: Array<[Sort, string]> = [['pop', 'Nejoblíbenější'], ['price', 'Cena: od nejnižší'], ['price-desc', 'Cena: od nejvyšší'], ['disc', 'Největší sleva'], ['date', 'Nejnovější']];

const list = (v: string[] | string | null, max: number, re: RegExp) => [...new Set((Array.isArray(v) ? v.join(',') : v ?? '').split(',').map((x) => x.trim().toLowerCase()).filter((x) => re.test(x)))].slice(0, max);

export function parseFilters(sp: URLSearchParams): FilterState {
  const o = sp.get('orderby') ?? '';
  const sort: Sort = o === 'popularity' ? 'pop' : (SORTS.some(([k]) => k === o) ? o as Sort : 'pop');
  const num = (k: string) => { const v = sp.get(k); if (v === null || v.trim() === '') return undefined; const n = Number(v); return Number.isFinite(n) && n >= 0 ? Math.floor(n) : undefined; };
  const p: FilterState['p'] = {};
  for (const k of PARAM_ORDER) { const v = list(sp.getAll('p_' + k), 10, /^[a-z0-9-]{1,40}$/); if (v.length) p[k] = v; }
  return {
    sort, min: num('min_price'), max: num('max_price'),
    znacka: list(sp.getAll('znacka'), 20, /^[a-z0-9-]{1,80}$/), obchod: list(sp.getAll('obchod'), 10, /^[a-z0-9.-]{3,60}$/),
    skladem: sp.get('skladem') === '1', sleva: sp.get('sleva') === '1', kat: list(sp.get('kat'), 1, /^[a-z0-9-]{1,120}$/)[0] ?? '', p,
  };
}

export const isFiltered = (f: FilterState) => f.sort !== 'pop' || f.min !== undefined || f.max !== undefined || f.znacka.length > 0
  || f.obchod.length > 0 || f.skladem || f.sleva || !!f.kat || Object.keys(f.p).length > 0;

/** Query string in a stable order (pagination, sort tabs, chips). */
export function toQuery(f: FilterState): string {
  const sp = new URLSearchParams();
  if (f.sort !== 'pop') sp.set('orderby', f.sort);
  if (f.min !== undefined) sp.set('min_price', String(f.min));
  if (f.max !== undefined) sp.set('max_price', String(f.max));
  if (f.znacka.length) sp.set('znacka', f.znacka.join(','));
  if (f.obchod.length) sp.set('obchod', f.obchod.join(','));
  if (f.skladem) sp.set('skladem', '1');
  if (f.sleva) sp.set('sleva', '1');
  if (f.kat) sp.set('kat', f.kat);
  for (const k of PARAM_ORDER) if (f.p[k]?.length) sp.set('p_' + k, f.p[k]!.join(','));
  const s = sp.toString().replace(/%2C/g, ',');
  return s ? '?' + s : '';
}
/** Copy of the state with one change applied (chips "×", sort tabs). */
export function withFilter(f: FilterState, change: Partial<FilterState>): FilterState {
  return { ...f, ...change, p: change.p ?? f.p };
}

/** FilterState → ListQuery (slugs resolved to ids / canonical values through the brand list and the facets). */
export function toListQuery(f: FilterState, page: number, brands: { bySlug: Map<string, BrandLite> }, fc: Facets | null, tree?: { bySlug: Map<string, Cat> }): ListQuery {
  const params: ListQuery['params'] = [];
  for (const k of PARAM_ORDER) {
    const want = f.p[k];
    if (!want?.length) continue;
    const b = BUCKETS[k];
    if (b) { const r = b.filter(([id]) => want.includes(id)).map(([, , a, z]) => [a, z] as [number, number]); if (r.length) params.push({ key: k, ranges: r }); continue; }
    const vals = (fc?.p[k] ?? []).map(([v]) => v).filter((v) => want.includes(valueSlug(v)));
    if (vals.length) params.push({ key: k, values: vals });
  }
  return {
    page, sort: f.sort, min: f.min, max: f.max,
    brands: f.znacka.map((s) => brands.bySlug.get(s)?.id).filter((x): x is number => !!x),
    shops: f.obchod, stock: f.skladem, disc: f.sleva, kat: f.kat && tree ? tree.bySlug.get(f.kat)?.id : undefined, params,
  };
}
