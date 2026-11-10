/**
 * Affiliate exits /go/<slug>/:
 *  - the target comes ONLY from D1 and is returned byte for byte (signed network links must not be re-encoded);
 *  - https only, host must be an affiliate network or a shop from the catalogue (no open redirect);
 *  - never shared-cached; crawlers/prefetch get 204 without a write; real clicks are logged in waitUntil.
 */
import { sha256Hex } from './http';
import { isLocal, type AppEnv } from './env';

const DEFAULT_ALLOWED_HOSTS = [
  // CJ click domains (all offers of v1 come from CJ), eHub / Dognet / AffiliatePort for the next shops
  'anrdoezrs.net', 'jdoqocy.com', 'tkqlhce.com', 'dpbolvw.net', 'kqzyfj.com', 'emjcd.com',
  'ehub.cz', 'go.dognet.com', 'login.affial.com', 'tracking.affiliateport.eu',
  'sportisimo.cz', 'bezvasport.cz', 'answear.cz', 'footshop.cz', '4camping.cz', 'd-sport.cz', 'azfishing.cz', 'hs-sport.cz',
  'insportline.cz', 'swimaholic.cz', '2sport.cz', 'e-sportshop.cz', 'skinners.cz', 'decathlon.cz', 'spartoo.cz',
];

function isSafeTarget(url: unknown, extra = ''): url is string {
  if (typeof url !== 'string' || url.length === 0 || url.length > 8192) return false;
  if (!/^[\x21-\x7e]+$/.test(url)) return false;
  let u: URL;
  try { u = new URL(url); } catch { return false; }
  if (u.protocol !== 'https:' || u.username || u.password) return false;
  const host = u.hostname.toLowerCase();
  const hosts = [...DEFAULT_ALLOWED_HOSTS, ...extra.split(',').map((s) => s.trim().toLowerCase()).filter(Boolean)];
  return hosts.some((h) => host === h || host.endsWith('.' + h));
}

const CRAWLER = /bot\b|bot\/|crawl|spider|slurp|preview|monitor|lighthouse|pingdom|uptime|whatsapp|telegram|discord|slack|curl\/|wget|python|go-http-client|java\/|okhttp|axios|node-fetch|scrapy|httpclient|headless|bytespider|petalbot|facebookexternalhit/i;
const isCrawlerLike = (ua: string | null) => !ua || CRAWLER.test(ua);
const isPrefetch = (r: Request) => r.headers.get('purpose') === 'prefetch' || (r.headers.get('sec-purpose') ?? '').includes('prefetch');

async function ipHash(ip: string, env: AppEnv): Promise<string> {
  const salt = env.IP_HASH_SALT || (isLocal(env) ? 'local-salt' : '');
  if (!salt) return '';
  return (await sha256Hex(`${salt}|${new Date().toISOString().slice(0, 10)}|${ip}`)).slice(0, 32);
}

const NO_STORE = { 'cache-control': 'private, no-store, max-age=0', 'x-robots-tag': 'noindex, nofollow', 'referrer-policy': 'strict-origin-when-cross-origin' };

export async function handleGo(slug: string | undefined, request: Request, env: AppEnv, waitUntil?: (p: Promise<unknown>) => void): Promise<Response> {
  if (!slug || !/^[a-z0-9-]{3,200}$/.test(slug)) return new Response('Nabídka neexistuje.', { status: 404, headers: { ...NO_STORE, 'content-type': 'text/plain; charset=utf-8' } });
  if (isCrawlerLike(request.headers.get('user-agent')) || isPrefetch(request)) {
    return new Response(null, { status: 204, headers: NO_STORE });
  }
  const ip = request.headers.get('cf-connecting-ip') ?? '0.0.0.0';
  if (env.RL_GO && !(await env.RL_GO.limit({ key: ip })).success) {
    return new Response('Příliš mnoho požadavků, zkuste to za chvíli.', { status: 429, headers: { ...NO_STORE, 'content-type': 'text/plain; charset=utf-8', 'retry-after': '60' } });
  }
  const row = await env.DB.prepare(
    `SELECT o.id, o.product_id, o.domain, o.target_url, o.active, p.slug AS product_slug FROM offers o LEFT JOIN products p ON p.id = o.product_id WHERE o.go_slug = ?`,
  ).bind(slug).first<{ id: number; product_id: number; domain: string; target_url: string; active: number; product_slug: string | null }>();
  let fallback = '/';
  if (!row) return new Response(null, { status: 302, headers: { ...NO_STORE, location: fallback } });
  if (row.product_slug) fallback = `/${row.product_slug}/`;
  if (!row.active || !isSafeTarget(row.target_url, env.GO_ALLOWED_HOSTS)) {
    if (row.active) console.log(JSON.stringify({ level: 'error', event: 'go_unsafe_target', id: row.id }));
    return new Response(null, { status: 302, headers: { ...NO_STORE, location: fallback } });
  }
  const ctx = (new URL(request.url).searchParams.get('ctx') ?? 'go').toLowerCase().replace(/[^a-z0-9_-]/g, '').slice(0, 30) || 'go';
  const log = (async () => {
    await env.DB.prepare('INSERT INTO clicks (offer_id, product_id, domain, context, ip_hash, clicked_at) VALUES (?, ?, ?, ?, ?, ?)')
      .bind(row.id, row.product_id, row.domain, ctx, await ipHash(ip, env), new Date().toISOString()).run();
  })().catch((e) => console.log(JSON.stringify({ level: 'warn', event: 'click_log_failed', message: String(e) })));
  waitUntil?.(log);
  return new Response(null, { status: 302, headers: { ...NO_STORE, location: row.target_url } });
}
