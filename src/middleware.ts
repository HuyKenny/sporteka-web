/**
 * Every on-demand request:
 *  1. production workers.dev host → 301 to sporteka.cz (only /api/health stays,
 *     the uptime monitor cannot pass Bot Fight Mode on the zone); host allow-list; staging whole host behind Access
 *  2. canonical URL in ONE 301: www → apex, duplicate slashes, lowercase, a few guessed URL shapes, trailing slash and
 *     (the `redirects` table of retired products is looked up only for would-be 404s, dispatch.ts)
 *  3. edge cache (Cache API) for public GET HTML/XML. Key = host + path + normalised listing params (filters.ts) + search
 *     term + data_version + build id. Uncached requests with parameters are rate limited (RL_SEARCH).
 *  4. security headers; HTML gets a strict CSP with a per-response nonce (HTMLRewriter adds it to every <script>);
 *     non-production hosts get X-Robots-Tag noindex.
 */
import { defineMiddleware } from 'astro:middleware';
import { authenticateAdmin } from './lib/server/access';
import { allowedHosts, getEnv, isLocal, isStatic } from './lib/server/env';
import { clientIp } from './lib/server/http';
import { dataVersion } from './lib/server/versions';
import { htmlCsp, securityHeaders } from './lib/security';
import { parseFilters, toQuery } from './lib/filters';
import dofollow from './data/dofollow.json';

const NO_CACHE = [/^\/go\//, /^\/api\//, /^\/wp-content\//, /^\/a\//, /^\/_astro\//];
/** Paths whose case matters (base64 image paths, hashed assets, uploads) are never lowercased. */
const KEEP_CASE = /^\/(wp-content|a|_astro|go)\//;
const CACHE_TTL = 21600;  // 6 h (was 10 min): data_version in the key already invalidates the pages after every nightly import, the TTL only bounds repeat misses

const LEGACY: Array<[RegExp, (m: RegExpExecArray) => string]> = [
  [/^\/(wp-)?sitemap\.xml$/, () => '/sitemap_index.xml'],
  // URL shapes visitors and other comparison sites guess
  [/^\/(produkt|product|kategorie|category)\/([^/]+)\/?$/, (m) => '/' + m[2] + '/'],
  // /hledat/ is the search page of the static export (src/pages/hledat.astro sends the SSR to /?s=)
  [/^\/search\/?$/, () => '/'],
];

/** Final path after all canonicalisation steps, or null when the request is already canonical. */
function canonicalPath(path: string): { to: string; status: number } | null {
  let p = path.replace(/\/\/+/g, '/');
  // lower-case letters only: percent-escapes stay upper case — Cloudflare normalises them (%c2 → %C2), lower-casing
  // them redirected /znacka/…%C2%B7…/ to itself forever (audit 28. 10. 2026)
  if (/[A-Z]/.test(p.replace(/%[0-9A-F]{2}/gi, '')) && !KEEP_CASE.test(p)) p = p.toLowerCase().replace(/%[0-9a-f]{2}/g, (m) => m.toUpperCase());
  // the old theme appended "null" to links: /<anything>/null
  if (/\/null\/?$/i.test(p)) p = p.replace(/\/null\/?$/i, '/');
  for (const [re, to] of LEGACY) {
    const m = re.exec(p);
    if (m) { p = to(m); break; }
  }
  // trailing slash for pages (files like /sitemap_index.xml, /robots.txt, /wp-content/… keep theirs)
  if (!p.endsWith('/') && !/\.[a-z0-9]{2,5}$/i.test(p) && !p.startsWith('/api/')) p += '/';
  // the redirects table (retired products) is consulted only for URLs that would 404 (dispatch.ts), never here:
  // this runs before the edge cache, a D1 read on every request would cost more than the pages themselves
  return p === path ? null : { to: p, status: 301 };
}

export function cacheKey(url: URL, version: string): string {
  const f = toQuery(parseFilters(url.searchParams)).slice(1);
  const s = (url.searchParams.get('s') ?? '').trim().toLowerCase().slice(0, 100);
  const q = [f, s ? 's=' + encodeURIComponent(s) : ''].filter(Boolean).join('&');
  return `https://${url.host}/__kc/${encodeURIComponent(version)}/${__BUILD_ID__}${url.pathname}${q ? '__q/' + encodeURIComponent(q) : ''}`;
}

/** ETag + Last-Modified of a cached page: they change only when the catalogue (data_version, YYYYMMDDHHMMSS) or the build does. */
function validators(version: string): Record<string, string> {
  const out: Record<string, string> = { ETag: `W/"${version}-${__BUILD_ID__}"` };
  const m = /^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})$/.exec(version);
  if (m) { const [y, mo, d, h, mi, se] = m.slice(1).map(Number) as [number, number, number, number, number, number]; out['Last-Modified'] = new Date(Date.UTC(y, mo - 1, d, h, mi, se)).toUTCString(); }
  return out;
}
function notModified(req: Request, v: Record<string, string>): boolean {
  const inm = req.headers.get('if-none-match');
  if (inm) return inm.split(',').some((t) => t.trim() === v.ETag);
  const ims = req.headers.get('if-modified-since');
  return !!(ims && v['Last-Modified'] && Date.parse(ims) >= Date.parse(v['Last-Modified']));
}

function nonce(): string {
  const b = crypto.getRandomValues(new Uint8Array(16));
  return btoa(String.fromCharCode(...b));
}

/** Every external link gets rel="nofollow noopener" (merged with its own rel); links on the allowlist
 *  (src/data/dofollow.json, approved by Kenny per URL) lose nofollow/sponsored/ugc instead. */
const DOFOLLOW = (dofollow.allow as string[]).map((s) => s.toLowerCase());
function relExternal(e: Element) {
  const href = e.getAttribute('href') ?? '';
  const own = /^(?:https?:\/\/(?:www\.)?sporteka\.cz)?(\/(?!go\/|api\/|wp-content\/|a\/|_astro\/)[^?#]*)(.*)$/i.exec(href);
  if (own && (href.startsWith('/') || /^https?:/i.test(href))) {
    return;
  }
  if (!/^https?:\/\//i.test(href) || /^https?:\/\/(?:[a-z0-9-]+\.)*sporteka\.cz(?:[/?#]|$)/i.test(href)) return;
  const tokens = (e.getAttribute('rel') ?? '').split(/\s+/).filter(Boolean);
  if (DOFOLLOW.some((d) => href.toLowerCase().includes(d))) {
    const keep = tokens.filter((t) => !['nofollow', 'sponsored', 'ugc'].includes(t.toLowerCase()));
    if (keep.length) e.setAttribute('rel', keep.join(' ')); else e.removeAttribute('rel');
    return;
  }
  for (const t of ['nofollow', 'noopener']) if (!tokens.includes(t)) tokens.push(t);
  e.setAttribute('rel', tokens.join(' '));
}

function finish(res: Response, url: URL, extra: Record<string, string> = {}): Response {
  const env = getEnv();
  let out = new Response(res.body, res);
  if ((out.headers.get('content-type') ?? '').includes('text/html') && out.body && isStatic(env)) {
    // static snapshot: same data → same bytes (no per-response nonce); the CSP comes from _headers
    out = new HTMLRewriter().on('a[href]', { element: relExternal }).transform(out);
  } else if ((out.headers.get('content-type') ?? '').includes('text/html') && out.body) {
    const n = nonce();
    out = new HTMLRewriter().on('script', { element(e) { e.setAttribute('nonce', n); } }).on('a[href]', { element: relExternal }).transform(out);
    out.headers.set('Content-Security-Policy', htmlCsp(n));
  }
  for (const [k, v] of Object.entries(securityHeaders())) if (!out.headers.has(k)) out.headers.set(k, v);
  for (const [k, v] of Object.entries(extra)) out.headers.set(k, v);
  if (env.ENVIRONMENT !== 'production' || /^\/(go|api)\//.test(url.pathname)) out.headers.set('X-Robots-Tag', 'noindex, nofollow');
  return out;
}
const redirect = (to: string, status = 301) => new Response(null, { status, headers: { location: to, 'cache-control': 'public, max-age=3600' } });
const tooMany = (msg: string) => new Response(msg, { status: 429, headers: { 'content-type': 'text/plain; charset=utf-8', 'retry-after': '30', 'cache-control': 'no-store' } });

export const onRequest = defineMiddleware(async (ctx, next) => {
  const url = ctx.url;
  if (ctx.isPrerendered) return next();
  const env = getEnv();

  const host = url.hostname.toLowerCase();
  const prod = env.ENVIRONMENT === 'production';
  // the production workers.dev mirror must not duplicate sporteka.cz nor bypass the zone WAF
  if (prod && host.endsWith('.workers.dev') && url.pathname !== '/api/health') return redirect('https://sporteka.cz' + url.pathname + url.search, 301);

  const hosts = allowedHosts(env);
  if (!isLocal(env) && hosts.length && !hosts.includes(host)) {
    return finish(new Response('Not found', { status: 404, headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store' } }), url);
  }

  if (env.REQUIRE_ACCESS_EVERYWHERE === '1') {
    const auth = await authenticateAdmin(ctx.request, env);
    if (!auth.ok) return finish(new Response('Přístup jen pro přihlášené.', { status: auth.status, headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store' } }), url);
  }

  const isGet = ctx.request.method === 'GET' || ctx.request.method === 'HEAD';
  if (isGet) {
    const www = prod && host === 'www.sporteka.cz';
    const c = canonicalPath(url.pathname);
    if (c?.status === 410) return finish(new Response('Gone', { status: 410, headers: { 'cache-control': 'public, max-age=3600' } }), url);
    if (c || www) return finish(redirect((www ? 'https://sporteka.cz' : '') + (c?.to ?? url.pathname) + url.search, c?.status ?? 301), url);
  }

  const cacheable = !isStatic(env) && isGet && !NO_CACHE.some((r) => r.test(url.pathname)) && !ctx.request.headers.has('authorization') && env.REQUIRE_ACCESS_EVERYWHERE !== '1';
  const cache = cacheable && typeof caches !== 'undefined' ? (caches as unknown as { default: Cache }).default : null;
  let key: string | null = null;
  if (cache) {
    try {
      const version = await dataVersion();
      key = cacheKey(url, version);
      const hit = await cache.match(key);
      if (hit) {
        // validators from the catalogue version: unchanged pages answer a crawler's conditional request with a cheap 304
        const v = validators(version);
        const h = { 'X-Spt-Page-Cache': 'HIT', 'Cache-Control': 'public, max-age=0, must-revalidate', ...v };
        if (notModified(ctx.request, v)) return finish(new Response(null, { status: 304 }), url, h);
        return finish(hit, url, h);
      }
    } catch { key = null; }
  }

  // anything rendered from parameters (search, filters, sort) costs D1 queries → rate limit per IP on a cache miss
  if (key?.includes('__q/') && env.RL_SEARCH && !(await env.RL_SEARCH.limit({ key: clientIp(ctx.request) })).success) {
    return finish(tooMany('Příliš mnoho požadavků, zkuste to za chvíli.'), url);
  }

  const res = await next();
  const cc = res.headers.get('cache-control') ?? '';
  const ct = res.headers.get('content-type') ?? '';
  const isHtml = ct.includes('text/html');
  const isXml = ct.includes('xml');
  // HEAD responses have no body — never store them
  if (cache && key && ctx.request.method === 'GET' && res.status === 200 && (isHtml || isXml) && !res.headers.has('set-cookie') && !/private|no-store/.test(cc)) {
    const toStore = new Response(res.clone().body, res);
    toStore.headers.set('Cache-Control', `public, s-maxage=${CACHE_TTL}`);
    const put = cache.put(key, toStore).catch((e: unknown) => console.log('cache.put failed: ' + String(e)));
    if (ctx.locals.cfContext?.waitUntil) ctx.locals.cfContext.waitUntil(put); else await put;
    return finish(res, url, { 'X-Spt-Page-Cache': 'MISS', 'Cache-Control': isXml ? 'public, max-age=3600' : 'public, max-age=0, must-revalidate', ...validators(await dataVersion()) });
  }
  if (isHtml && !res.headers.has('cache-control')) return finish(res, url, { 'Cache-Control': 'public, max-age=0, must-revalidate' });
  return finish(res, url);
});
