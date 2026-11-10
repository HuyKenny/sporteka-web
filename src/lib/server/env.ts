import { env as cfEnv } from 'cloudflare:workers';

export interface AppEnv {
  DB: D1Database;
  ASSETS?: Fetcher;
  RL_GO?: RateLimit;
  RL_SEARCH?: RateLimit;
  ENVIRONMENT?: string;
  SITE_URL?: string;
  ALLOWED_HOSTS?: string;
  REQUIRE_ACCESS_EVERYWHERE?: string;
  ANALYTICS_ENABLED?: string;
  ACCESS_TEAM_DOMAIN?: string;
  ACCESS_AUD?: string;
  IP_HASH_SALT?: string;
  GO_ALLOWED_HOSTS?: string;
  /** signs /img/ URLs (same value on the sporteka-img Worker) */
  IMG_SECRET?: string;
  /** "1" while scripts/staticky.py snapshots the site into static files: no nonce/CSP, no edge cache, direct shop links */
  STATIC_EXPORT?: string;
}

export function getEnv(): AppEnv {
  return cfEnv as unknown as AppEnv;
}

/** local/test only — never true in staging/production. */
/** Static snapshot build (wrangler dev --var STATIC_EXPORT:1). */
export function isStatic(e: AppEnv = getEnv()): boolean {
  return e.STATIC_EXPORT === '1';
}

export function isLocal(e: AppEnv = getEnv()): boolean {
  return e.ENVIRONMENT === 'local' || e.ENVIRONMENT === 'test';
}

export function allowedHosts(e: AppEnv = getEnv()): string[] {
  return (e.ALLOWED_HOSTS || '').split(',').map((s) => s.trim().toLowerCase()).filter(Boolean);
}
