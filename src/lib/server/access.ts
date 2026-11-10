/**
 * Cloudflare Access JWT verification (the whole staging host; there is no admin route). We verify the signed
 * `Cf-Access-Jwt-Assertion` ourselves — RS256 against the team JWKS, issuer, audience, expiry, not-before —
 * and never trust an e-mail header on its own. Without ACCESS_TEAM_DOMAIN + ACCESS_AUD access is refused.
 */
import type { AppEnv } from './env';

type AdminAuth = { ok: true; email: string; via: 'access' } | { ok: false; status: 401 | 403 | 503; reason: string };

interface Jwk { kid: string; kty: string; n: string; e: string; alg?: string }
let jwksCache: { team: string; at: number; keys: Jwk[] } | null = null;
let lastForced = 0;

function b64urlToBytes(s: string): Uint8Array<ArrayBuffer> {
  const pad = s.length % 4 === 2 ? '==' : s.length % 4 === 3 ? '=' : '';
  const bin = atob(s.replace(/-/g, '+').replace(/_/g, '/') + pad);
  const out = new Uint8Array(new ArrayBuffer(bin.length));
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

async function getJwks(team: string, fetchImpl: typeof fetch, force = false): Promise<Jwk[]> {
  if (!force && jwksCache && jwksCache.team === team && Date.now() - jwksCache.at < 3_600_000) return jwksCache.keys;
  const res = await fetchImpl(`https://${team}/cdn-cgi/access/certs`);
  if (!res.ok) throw new Error(`JWKS HTTP ${res.status}`);
  const data = (await res.json()) as { keys?: Jwk[] };
  const keys = (data.keys ?? []).filter((k) => k.kty === 'RSA');
  jwksCache = { team, at: Date.now(), keys };
  return keys;
}

async function verifyAccessJwt(
  token: string,
  opts: { team: string; aud: string; now?: number; fetchImpl?: typeof fetch; jwks?: Jwk[] },
): Promise<{ ok: true; email: string } | { ok: false; reason: string }> {
  const parts = token.split('.');
  if (parts.length !== 3) return { ok: false, reason: 'malformed token' };
  let header: { alg?: string; kid?: string };
  let payload: { aud?: string | string[]; iss?: string; exp?: number; nbf?: number; email?: string; sub?: string; common_name?: string };
  try {
    header = JSON.parse(new TextDecoder().decode(b64urlToBytes(parts[0]!)));
    payload = JSON.parse(new TextDecoder().decode(b64urlToBytes(parts[1]!)));
  } catch {
    return { ok: false, reason: 'undecodable token' };
  }
  if (header.alg !== 'RS256' || !header.kid) return { ok: false, reason: 'unexpected alg' };
  let keys = opts.jwks ?? (await getJwks(opts.team, opts.fetchImpl ?? fetch));
  let jwk = keys.find((k) => k.kid === header.kid);
  if (!jwk && !opts.jwks && Date.now() - lastForced > 60_000) {
    lastForced = Date.now();
    keys = await getJwks(opts.team, opts.fetchImpl ?? fetch, true);
    jwk = keys.find((k) => k.kid === header.kid);
  }
  if (!jwk) return { ok: false, reason: 'unknown key id' };
  const key = await crypto.subtle.importKey('jwk', { kty: 'RSA', n: jwk.n, e: jwk.e, alg: 'RS256', ext: true }, { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['verify']);
  const valid = await crypto.subtle.verify('RSASSA-PKCS1-v1_5', key, b64urlToBytes(parts[2]!), new TextEncoder().encode(`${parts[0]}.${parts[1]}`));
  if (!valid) return { ok: false, reason: 'bad signature' };
  const now = Math.floor((opts.now ?? Date.now()) / 1000);
  if (payload.iss !== `https://${opts.team}`) return { ok: false, reason: 'wrong issuer' };
  const aud = Array.isArray(payload.aud) ? payload.aud : [payload.aud];
  if (!aud.includes(opts.aud)) return { ok: false, reason: 'wrong audience' };
  if (typeof payload.exp !== 'number' || payload.exp < now - 30) return { ok: false, reason: 'expired' };
  if (typeof payload.nbf === 'number' && payload.nbf > now + 30) return { ok: false, reason: 'not yet valid' };
  // Users carry `email`; Access service tokens (automated checks) carry `common_name` = client id and an empty sub.
  const email = payload.email || (payload.common_name ? `service:${payload.common_name}` : '') || payload.sub || '';
  if (!email) return { ok: false, reason: 'no identity' };
  return { ok: true, email };
}

export async function authenticateAdmin(request: Request, env: AppEnv, fetchImpl?: typeof fetch): Promise<AdminAuth> {
  if (!env.ACCESS_TEAM_DOMAIN || !env.ACCESS_AUD) return { ok: false, status: 503, reason: 'Přihlášení není nastavené.' };
  const token = request.headers.get('cf-access-jwt-assertion');
  if (!token) return { ok: false, status: 401, reason: 'Nepřihlášený.' };
  try {
    const r = await verifyAccessJwt(token, { team: env.ACCESS_TEAM_DOMAIN, aud: env.ACCESS_AUD, ...(fetchImpl ? { fetchImpl } : {}) });
    return r.ok ? { ok: true, email: r.email, via: 'access' } : { ok: false, status: 403, reason: 'Přístup odepřen.' };
  } catch {
    return { ok: false, status: 503, reason: 'Přihlášení se nepodařilo ověřit.' };
  }
}
