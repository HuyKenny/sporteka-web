#!/usr/bin/env node
// Deploy an assets-only Worker (no code → every request is a free static-asset request) from a MANIFEST instead of a
// full directory: wrangler needs every file on disk (700k pages ≈ 36 GB), we only keep what changed since the last
// deploy. Unchanged paths carry their stored hash; Cloudflare already has those blobs and asks only for new ones.
//
//   node scripts/cf-assets.mjs <manifest.json>
//
// manifest.json: {
//   "worker": "sporteka-s01", "compatibility_date": "2026-10-01",
//   "config": { "html_handling": "auto-trailing-slash", "not_found_handling": "404-page" },
//   "redirects": "<_redirects text>" | null, "headers": "<_headers text>" | null, "workers_dev": true|false (optional),
//   "files": { "/a/index.html": { "hash": "<32 hex>"?, "size": 123?, "file": "/abs/path"? }, ... }
// }
// A file entry with "file" is hashed here (hash = blake3(base64(content) + extension)[:32], the wrangler algorithm);
// an entry without it must carry hash + size from the previous deploy. Prints JSON {uploaded, bytes, total, hashes} where
// hashes = {path: [hash, size]} for the caller to store. Credentials: see below.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

// blake3-wasm is a wrangler dependency (pnpm keeps it next to the real wrangler directory)
const require = createRequire(fs.realpathSync(path.join(process.cwd(), 'node_modules', 'wrangler', 'package.json')));
const blake3 = require('blake3-wasm');

// Credentials (never printed): CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID from the environment (GitHub Actions, a token
// scoped to Workers Scripts), else <SPT_ROOT>/credentials/.cloudflare-credentials.env (global key, local runs only).
const API = 'https://api.cloudflare.com/client/v4';
const ROOT = process.env.SPT_ROOT || '/home/kenny/ai';
const readEnv = (f) => Object.fromEntries(fs.readFileSync(path.join(ROOT, 'credentials', f), 'utf8').split('\n')
  .filter((l) => l.includes('=') && !l.startsWith('#')).map((l) => { const i = l.indexOf('='); return [l.slice(0, i).replace('export ', '').trim(), l.slice(i + 1).trim().replace(/^["']|["']$/g, '')]; }));
const fileEnv = () => ({ ...readEnv('.sporteka-credentials.env'), ...readEnv('.cloudflare-credentials.env') });
const env = process.env.CLOUDFLARE_API_TOKEN ? {} : fileEnv();
const ACCOUNT = process.env.CLOUDFLARE_ACCOUNT_ID || env.CF_ACCOUNT_ID;
if (!ACCOUNT) throw new Error('CLOUDFLARE_ACCOUNT_ID missing');
const AUTH = process.env.CLOUDFLARE_API_TOKEN ? { Authorization: `Bearer ${process.env.CLOUDFLARE_API_TOKEN}` }
  : { 'X-Auth-Email': env.CF_EMAIL, 'X-Auth-Key': env.CF_GLOBAL_API_KEY || env.CF_API_KEY };

const MIME = { html: 'text/html', css: 'text/css', js: 'application/javascript', json: 'application/json', xml: 'application/xml', txt: 'text/plain',
  svg: 'image/svg+xml', png: 'image/png', jpg: 'image/jpeg', webp: 'image/webp', ico: 'image/x-icon', woff2: 'font/woff2', webmanifest: 'application/manifest+json' };

async function api(method, url, body, headers = {}) {
  for (let attempt = 1; ; attempt++) {
    const r = await fetch(API + url, { method, headers: { ...headers }, body });
    const j = await r.json().catch(() => ({}));
    if (j.success) return j.result;
    if (attempt >= 5 || (r.status < 500 && r.status !== 429)) throw new Error(`${method} ${url.split('?')[0]} → ${r.status} ${JSON.stringify(j.errors ?? '').slice(0, 300)}`);
    await new Promise((s) => setTimeout(s, 2000 * attempt));
  }
}

const m = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const manifest = {};
const local = new Map();   // hash → [path, abs file]
for (const [p, e] of Object.entries(m.files)) {
  if (e.file) {
    const buf = fs.readFileSync(e.file);
    const hash = blake3.hash(buf.toString('base64') + path.extname(p).slice(1)).toString('hex').slice(0, 32);
    manifest[p] = { hash, size: buf.length };
    local.set(hash, [p, e.file]);
  } else {
    if (!e.hash || e.size == null) throw new Error(`no file and no stored hash for ${p}`);
    manifest[p] = { hash: e.hash, size: e.size };
  }
}
if (Object.keys(manifest).length > 100000) throw new Error('more than 100 000 files in one Worker version');

const session = await api('POST', `/accounts/${ACCOUNT}/workers/scripts/${m.worker}/assets-upload-session`, JSON.stringify({ manifest }), { ...AUTH, 'Content-Type': 'application/json' });
let jwt = session.jwt;
const need = (session.buckets ?? []).flat();
let bytes = 0;
const missing = need.filter((h) => !local.has(h));
if (missing.length) {
  // Cloudflare lost (or never had) a blob we thought was there: the caller must re-render these paths
  const byHash = new Map(Object.entries(manifest).map(([p, e]) => [e.hash, p]));
  // process.exit() right after console.log() cut a big list at 256 kB when stdout is a pipe: exit from the write callback
  process.stdout.write(JSON.stringify({ error: 'missing', paths: missing.map((h) => byHash.get(h)) }) + '\n', () => process.exit(3));
  await new Promise(() => {});
}
// buckets as Cloudflare grouped them, 3 in flight (wrangler's BULK_UPLOAD_CONCURRENCY)
const queue = [...session.buckets ?? []];
async function worker() {
  for (let b = queue.shift(); b; b = queue.shift()) {
    const form = new FormData();
    for (const h of b) {
      const [p, file] = local.get(h);
      const buf = fs.readFileSync(file);
      bytes += buf.length;
      form.append(h, new File([buf.toString('base64')], h, { type: MIME[path.extname(p).slice(1)] ?? 'application/null' }), h);
    }
    const res = await api('POST', `/accounts/${ACCOUNT}/workers/assets/upload?base64=true`, form, { Authorization: `Bearer ${session.jwt}` });
    if (res?.jwt) jwt = res.jwt;
  }
}
await Promise.all([worker(), worker(), worker()]);

const meta = {
  assets: { jwt, config: { ...m.config, ...(m.redirects ? { _redirects: m.redirects } : {}), ...(m.headers ? { _headers: m.headers } : {}) } },
  compatibility_date: m.compatibility_date ?? '2026-10-01',
};
const form = new FormData();
form.set('metadata', new File([JSON.stringify(meta)], 'metadata.json', { type: 'application/json' }));
await api('PUT', `/accounts/${ACCOUNT}/workers/scripts/${m.worker}`, form, AUTH);
// workers.dev: on for staging checks, off in production (it would serve the same pages on a second host)
if (typeof m.workers_dev === 'boolean') {
  await api('POST', `/accounts/${ACCOUNT}/workers/scripts/${m.worker}/subdomain`, JSON.stringify({ enabled: m.workers_dev, previews_enabled: false }), { ...AUTH, 'Content-Type': 'application/json' });
}
console.log(JSON.stringify({ worker: m.worker, total: Object.keys(manifest).length, uploaded: need.length, bytes,
  hashes: Object.fromEntries(Object.entries(manifest).map(([p, e]) => [p, [e.hash, e.size]])) }));
