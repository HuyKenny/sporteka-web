// GET /api/health — monitoring: 200 when the catalogue push is fresh and big enough, 503 with reasons otherwise.
// Reads two site_cache rows only (a COUNT over offers would read the whole table on every check).
import type { APIRoute } from 'astro';
import { getEnv } from '../../lib/server/env';

export const prerender = false;
const MAX_AGE_H = 200;   // the CJ import runs weekly (Monday night)
const MIN_OFFERS = 20_000;

export const GET: APIRoute = async () => {
  const db = getEnv().DB;
  const [home, version] = await db.batch([
    db.prepare("SELECT value FROM site_cache WHERE key = 'home'"),
    db.prepare("SELECT value, updated_at FROM site_cache WHERE key = 'data_version'"),
  ]);
  let n = 0;
  try { n = Number(JSON.parse((home!.results[0] as { value: string } | undefined)?.value ?? '{}').offers ?? 0); } catch { /* missing */ }
  const v = (version!.results[0] as { value: string; updated_at: string } | undefined) ?? null;
  const ageH = (s: string | null) => (s ? (Date.now() - Date.parse(s.includes('T') ? s : s.replace(' ', 'T') + '+01:00')) / 3_600_000 : Infinity);
  const reasons: string[] = [];
  if (n < MIN_OFFERS) reasons.push(`only ${n} active offers`);
  if (ageH(v?.updated_at ?? null) > MAX_AGE_H) reasons.push(`no import for ${MAX_AGE_H} h`);
  const body = { ok: reasons.length === 0, reasons, active_offers: n, data_version_at: v?.updated_at ?? null };
  return new Response(JSON.stringify(body), { status: body.ok ? 200 : 503, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' } });
};
