// Security headers. HTML responses get a strict CSP: scripts only with the per-response nonce ('strict-dynamic' lets
// the nonce'd GA4 loader add gtag.js; Cloudflare's injected challenge script picks the nonce from this header). The
// https:/'unsafe-inline' entries are ignored by browsers that support strict-dynamic and keep very old ones working.
// sporteka audit 28. 10. 2026: everything else 'self' — data can leave only to GA4 (connect-src), frames only YouTube
// (one article) and the Cloudflare challenge; images stay https: (articles embed packshots from 14 shop CDNs).
const BASE_CSP = "default-src 'self'; img-src 'self' data: https:; style-src 'self' 'unsafe-inline'; font-src 'self'; "
  + "connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com https://www.google.com https://stats.g.doubleclick.net; "
  + "frame-src https://www.youtube.com https://www.youtube-nocookie.com https://challenges.cloudflare.com; media-src 'self'; manifest-src 'self'; worker-src 'self'; "
  + "object-src 'none'; base-uri 'self'; frame-ancestors 'self'; form-action 'self' https://*.cloudflareaccess.com; upgrade-insecure-requests";

export function htmlCsp(nonce: string): string {
  return `script-src 'nonce-${nonce}' 'strict-dynamic' https: 'unsafe-inline'; ${BASE_CSP}`;
}

export function securityHeaders(): Record<string, string> {
  return {
    'Content-Security-Policy': BASE_CSP,
    'Cross-Origin-Opener-Policy': 'same-origin-allow-popups',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'X-Frame-Options': 'SAMEORIGIN',
    'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=(), usb=(), browsing-topics=()',
    'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
    'X-Permitted-Cross-Domain-Policies': 'none',
  };
}
