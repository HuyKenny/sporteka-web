// Titles and descriptions as Rank Math printed them on sporteka.cz (templates from rank-math-options-titles, 27. 10. 2026):
//   product   "{name} – srovnání cen | Sporteka"              category "{term} – srovnání cen a výběr | Sporteka"  (8. vlna 2. 11. 2026: bez „levně“, tón Heureky)
//   blog cat  "{term} | Sporteka"                            post/page "{title} | Sporteka"
// Posts, pages and categories keep the exact texts of the live site (snapshot in seo_title/seo_desc); brands use the
// mu-plugin template (views.ts brandSeo). Paged listings get " — strana N" before the site name (mu-plugin).
import { decode, stripTags } from './format';

const SEP = '|';
const SITE = 'Sporteka';

export interface Vars { title?: string; term?: string; excerpt?: string; page?: number; pages?: number; /** cut a long custom text (product excerpts) */ clamp?: boolean }

function pageSuffix(page = 1, pages = 1): string {
  return page > 1 ? ` - Stránka ${page} z ${pages}` : '';
}

/** Expands the Rank Math variables used on sporteka.cz (unknown ones are dropped like Rank Math does with empty values). */
function rmVars(tpl: string, v: Vars): string {
  const year = String(new Date().getFullYear());
  return tpl
    .replace(/%title%/g, v.title ?? '')
    .replace(/%term%/g, v.term ?? '')
    .replace(/%excerpt%/g, v.excerpt ?? '')
    .replace(/%term_description%/g, v.excerpt ?? '')
    .replace(/%sitename%/g, SITE)
    .replace(/%sep%/g, SEP)
    .replace(/%currentyear%/g, year)
    .replace(/%page%/g, pageSuffix(v.page, v.pages))
    .replace(/%[a-z_]+%/g, '')
    .replace(/\s{2,}/g, ' ')
    .trim();
}

/** " — strana N" before the site name on paged listings (mu-plugin, rank_math/frontend/title). */
export function paged(title: string, page = 1): string {
  if (page <= 1 || title.includes('strana ')) return title;
  return title.replace(/(\s*\|\s*Sporteka)?$/, ` — strana ${page}$1`);
}
/** A Rank Math title template (per-object override) with %title%/%term% filled. */
export function rmTitle(tpl: string, name: string): string {
  return rmVars(tpl, { title: name, term: name });
}
/** Product title: the WordPress template while it fits in the SERP (≤ 65 characters), else a shorter suffix, else the
 *  name alone (audit 28. 10. 2026: 2 493 product titles were over 70 characters and got cut by Google). */
export function productTitle(name: string, custom = ''): string {
  if (custom) return rmVars(custom, { title: decode(name) });
  const n = decode(name);
  for (const tpl of ['%title% – srovnání cen %sep% %sitename%', '%title% %sep% %sitename%']) {
    const t = rmVars(tpl, { title: n });
    if (t.length <= 65) return t;
  }
  return n;
}
/** Category title: the stored one (WordPress snapshot) when present, else keyword first with the lowest price while it fits in
 *  the SERP (≤ 60 characters), else the shorter forms. */
export function categoryTitle(name: string, custom: string, page = 1, lowest = 0): string {
  const term = decode(name);
  if (custom) return paged(rmVars(custom, { term }), page);
  const forms = [...(lowest > 0 ? ['%term% – srovnání cen od ' + String(lowest).replace(/\B(?=(\d{3})+(?!\d))/g, '\u00a0') + '\u00a0Kč %sep% %sitename%'] : []),
    '%term% – srovnání cen a výběr %sep% %sitename%', '%term% – srovnání cen %sep% %sitename%', '%term% %sep% %sitename%'];
  let t = '';
  for (const f of forms) { t = rmVars(f, { term }); if (t.length <= 60) break; }
  return paged(t, page);
}
/** Blog category and the blog itself. */
export function termTitle(name: string, page = 1): string {
  return paged(rmVars('%term% %sep% %sitename%', { term: decode(name) }), page);
}
export function postTitle(title: string, custom = ''): string {
  return rmVars(custom || '%title% %sep% %sitename%', { title: decode(title) });
}
export function searchTitle(q: string, page: number, pages: number): string {
  return rmVars('%search_query% %page% %sep% %sitename%', { page, pages }).replace(/^/, q + ' ').replace(/\s{2,}/g, ' ').trim();
}
/** Meta description: Rank Math override or the object's text, cut to ~155 characters at a word boundary; `fallback`
 *  (a filled-in template) when there is no text at all; "Strana N: " on paged listings. */
export function descFrom(custom: string, html: string, v: Vars = {}, fallback = '', page = 1): string {
  // a per-object description (Rank Math / live snapshot) is printed whole, like Rank Math does
  if (custom) { const c = rmVars(custom, { ...v, excerpt: stripTags(html) }); if (c) return (page > 1 ? `Strana ${page}: ` : '') + (v.clamp ? clamp(c, 158) : c); }
  const text = stripTags(html) || fallback;
  return (page > 1 && text ? `Strana ${page}: ` : '') + clamp(text, page > 1 ? 145 : 160);
}
export function clamp(text: string, max = 155): string {
  const t = text.replace(/\s+/g, ' ').trim();
  if (t.length <= max) return t;
  const cut = t.slice(0, max + 1);
  const i = cut.lastIndexOf(' ');
  return (i > max * 0.6 ? cut.slice(0, i) : t.slice(0, max)).replace(/[\s,;:–(-]+$/, '') + '…';
}

/** Rank Math robots meta: follow/nofollow, index/noindex, extra flags from the object (noimageindex …), max-* defaults. */
export function robots(noindex: boolean, extra = ''): string[] {
  const flags = extra.split(',').map((x) => x.trim()).filter((x) => x && !['index', 'noindex', 'follow', 'nofollow'].includes(x));
  const nofollow = extra.split(',').map((x) => x.trim()).includes('nofollow');
  const head = [nofollow ? 'nofollow' : 'follow', noindex ? 'noindex' : 'index', ...flags];
  return noindex ? head : [...head, 'max-snippet:-1', 'max-video-preview:-1', 'max-image-preview:large'];
}
