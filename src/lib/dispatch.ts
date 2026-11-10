// Resolves every root path:
//   /<slug>/                → product | product category | facet landing | post | page | blog category (slugs table, product wins)
//   /<slug>/page/<n>/       → paged product category / blog category / the blog page
//   /page/<n>/?s=…          → paged search
//   unknown /<slug>/        → 301 to an unambiguous continuation of a cut-off slug (db.guessSlug), else to the most
//                             relevant category/brand by its words (guess.ts), else 404; scanner junk stays 404
import { guessSlug, resolveSlug } from './db';
import { guessListing } from './guess';

const JUNK = /\.[a-z0-9]{2,5}$|^\/(\.|wp-|cgi-bin|admin|administrator|phpmyadmin|xmlrpc|vendor|api\/|_)/i;

export type Route =
  | { kind: 'product' | 'category' | 'facet' | 'post' | 'page' | 'postcat'; id: number; page: number }
  | { kind: 'blog'; page: number }
  | { kind: 'search'; page: number }
  | { kind: 'redirect'; to: string }
  | { kind: 'notfound' };

export async function dispatch(db: D1Database, pathname: string, sp: URLSearchParams): Promise<Route> {
  let path: string;
  try { path = decodeURIComponent(pathname); } catch { return { kind: 'notfound' }; }
  const seg = path.split('/').filter(Boolean);
  let page = 1;
  if (seg.length >= 2 && seg[seg.length - 2] === 'page' && /^\d+$/.test(seg[seg.length - 1]!)) {
    page = Number(seg.pop());
    seg.pop();
    if (page <= 1) return { kind: 'redirect', to: '/' + seg.map(encodeURIComponent).join('/') + (seg.length ? '/' : '') };
  }
  if (seg.length === 0) return sp.has('s') ? { kind: 'search', page } : page > 1 ? { kind: 'redirect', to: '/' } : { kind: 'notfound' };
  if (seg.length !== 1) {
    if (JUNK.test(path)) return { kind: 'notfound' };
    // category URLs with the parent path (/outdoor/stany/) → the flat category URL
    const last = await resolveSlug(db, seg[seg.length - 1]!.toLowerCase());
    if (last && (last.kind === 'category' || last.kind === 'product')) {
      const to = `/${encodeURIComponent(seg[seg.length - 1]!.toLowerCase())}/`;
      return { kind: 'redirect', to: page > 1 && last.kind === 'category' ? `${to}page/${page}/` : to };
    }
    if (page > 1) return { kind: 'notfound' };
    const g = await guessed(db, seg.join('-'));
    // nothing better: the existing first segment (/stany/<gone>/ → /stany/)
    if (g.kind === 'notfound' && await resolveSlug(db, seg[0]!.toLowerCase())) return { kind: 'redirect', to: `/${encodeURIComponent(seg[0]!.toLowerCase())}/` };
    return g;
  }
  const slug = seg[0]!.toLowerCase();
  if (slug !== seg[0]) return { kind: 'redirect', to: `/${encodeURIComponent(slug)}/` };
  const r = await resolveSlug(db, slug);
  if (r) {
    if (r.kind === 'page' && slug === 'blog') return { kind: 'blog', page };
    if (page > 1 && r.kind !== 'category' && r.kind !== 'facet' && r.kind !== 'postcat') return { kind: 'notfound' };
    return { kind: r.kind as 'product', id: r.ref_id, page };
  }
  // facet landings live in their own table (the slugs table has a CHECK on kind); a miss costs one indexed lookup
  const fp = await db.prepare('SELECT id FROM facet_pages WHERE slug = ?').bind(slug).first<{ id: number }>().catch(() => null);
  if (fp) return { kind: 'facet', id: fp.id, page };
  // retired products and renamed categories (scripts/katalog.py writes the redirects table)
  const rd = await db.prepare('SELECT to_path FROM redirects WHERE from_path = ?').bind(`/${slug}/`).first<{ to_path: string }>().catch(() => null);
  if (rd && rd.to_path !== `/${slug}/`) return { kind: 'redirect', to: rd.to_path };
  if (page === 1) {
    const g = await guessSlug(db, slug);
    if (g) return { kind: 'redirect', to: `/${encodeURIComponent(g)}/` };
    if (!JUNK.test(path)) return guessed(db, slug);
  }
  return { kind: 'notfound' };
}

async function guessed(db: D1Database, words: string): Promise<Route> {
  const to = await guessListing(db, words);
  return to ? { kind: 'redirect', to } : { kind: 'notfound' };
}
