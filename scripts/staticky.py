#!/usr/bin/env python3
"""sporteka.cz as a static site on assets-only Workers (no code → every request is free; Kenny 8. 11. 2026, variant C).

The pages come from the normal SSR app rendered locally once (astro build + wrangler dev with STATIC_EXPORT=1 over a copy
of the catalogue DB), fetched here and deployed per shard with scripts/cf-assets.mjs. A Worker version holds at most
100 000 files, so the paths are split by their first characters into shards; each shard is its own Worker with routes
sporteka.cz/<prefix>* (the more specific route wins over the main Worker's sporteka.cz/*). Everything not routed —
the home page, tiny prefixes — lives in the main Worker.

  staticky.py gsc                         # page impressions of the last 90 days from Search Console
  staticky.py prepare                     # copy the catalogue for the local SSR + lifecycle rules (SSR must be stopped)
  staticky.py paths                       # count paths per kind
  staticky.py plan [--force]              # compute (or show) the shard map; stored, recomputed only with --force
  staticky.py render --shard s03 [--limit N] [--threads 8] [--only-missing]
  staticky.py search                      # the client-side search index /_s/ (after render: needs the local SSR)
  staticky.py filters                     # listing filter data /_f/ (needs the local SSR too)
  staticky.py deploy --shard s03 [--worker NAME] [--noindex]
  staticky.py routes                      # print the route patterns per shard
  staticky.py parity [--limit N]          # every live sitemap URL → 200 from its shard's workers.dev
  staticky.py cutover [--apply]           # routes to the shard Workers + www redirect rule (backup of the old routes)
  staticky.py rollback backups/<file>     # the old routes back (SSR Worker sporteka)
  staticky.py status [--discord]          # deployed / left per shard (one Discord message when complete)
  staticky.py weekly [--noindex] [--only s01,s02]   # gsc → prepare → build → local SSR → search/filters → render changed + deploy per shard
  staticky.py weekly --texts              # only page 1 of every listing (texts in src/texts/ changed) — minutes, not hours

State (data/static-state.db): shard map, and per path its shard + the asset hash Cloudflare holds, so a deploy can name
unchanged files by hash without keeping 36 GB of HTML on the SD card. Rendered files live in tmp-static/out/ only until
their shard is deployed.
"""
import argparse
import concurrent.futures as cf
import functools
import hashlib
import html
import re
import unicodedata
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
LIVE = APP / 'data' / 'live-production.db'          # the catalogue built by katalog.py
# the copy the local SSR reads (wrangler dev --persist-to tmp-static/state): prepare copies LIVE here and applies the
# lifecycle rules, every other step reads it, so the paths, hashes and pages all come from the same data
CATALOG = APP / 'tmp-static' / 'state' / 'v3' / 'd1' / 'miniflare-D1DatabaseObject' / '9ba2b04bf514d9facfd57ed57d849e77241a7adc99d1c1545d06688b43d84248.sqlite'
# credentials: GitHub Actions passes them as env vars (secrets); local runs read <SPT_ROOT>/credentials/ (never printed)
ROOT = Path(os.environ.get('SPT_ROOT') or '/home/kenny/ai')
GSC_KEY = Path(os.environ.get('GSC_SA_FILE') or '/home/kenny/.config/gsc/service-account.json')


def cred(name, file='.sporteka-credentials.env'):
    """A credential: environment first, then the credentials file; '' when missing."""
    if os.environ.get(name):
        return os.environ[name]
    try:
        for line in open(ROOT / 'credentials' / file):
            k, _, v = line.strip().partition('=')
            if k.replace('export ', '').strip() == name:
                return v.strip().strip('"\'')
    except OSError:
        pass
    return ''
GSC_SITE = 'sc-domain:sporteka.cz'
GRACE_DAYS = 120      # a new product keeps an indexable page this long without any impression
STUB_DAYS = 180       # a retired product without a 301 slot keeps a "no longer sold" stub this long
RULES_PER_SHARD = 1800  # Cloudflare: 2 000 static _redirects rules per Worker version
STATE = APP / 'data' / 'static-state.db'
OUT = APP / 'tmp-static' / 'out'
CLIENT = APP / 'dist' / 'client'
KEEP = APP / 'tmp-static' / 'keep-astro'   # TODO move out of tmp-static before the first production deploy
# a second render worker (own port + own copy of the DB, e.g. in RAM) can take other shards in parallel:
# STATIC_PORT=8798 STATIC_PERSIST=/tmp/sporteka-render2 staticky.py weekly --only s13,s12 (Kenny 9. 11.: as fast as possible)
PORT = os.environ.get('STATIC_PORT', '8799')
PERSIST = os.environ.get('STATIC_PERSIST', 'tmp-static/state')
BASE = f'http://127.0.0.1:{PORT}'
CAP = 80_000          # files per shard (Cloudflare limit 100 000 per Worker version; 20 % headroom for new products)
SPLIT_MIN = 400       # prefixes smaller than this stay in the main Worker (fewer routes)
MAX_PAGES = 100       # listing pages per category / brand / facet (src/lib/views.ts STATIC_MAX_PAGES)
PER_PAGE = 24
MAIN = 'main'
SKIP_CLIENT = {'_headers', '_redirects', '_routes.json', '.assetsignore'}
COMPAT = '2026-10-01'

SECURITY = """/*
  Content-Security-Policy: script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; default-src 'self'; img-src 'self' data: https:; style-src 'self' 'unsafe-inline'; font-src 'self'; connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com https://www.google.com https://stats.g.doubleclick.net; frame-src https://www.youtube.com https://www.youtube-nocookie.com https://challenges.cloudflare.com; media-src 'self'; manifest-src 'self'; worker-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'self'; form-action 'self'; upgrade-insecure-requests
  Cross-Origin-Opener-Policy: same-origin-allow-popups
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), browsing-topics=()
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  X-Permitted-Cross-Domain-Policies: none
/_astro/*
  Cache-Control: public, max-age=31536000, immutable
/fonts/*
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *
/a/*
  Cache-Control: public, max-age=2592000, stale-while-revalidate=604800
/*.xml
  X-Robots-Tag: noindex, follow
"""


def state():
    db = sqlite3.connect(STATE, timeout=600)   # a parallel render worker may hold the lock (deploy writes) for a while
    db.executescript("""
      CREATE TABLE IF NOT EXISTS files (path TEXT PRIMARY KEY, kind TEXT NOT NULL, shard TEXT NOT NULL DEFAULT '',
        hash TEXT NOT NULL DEFAULT '', size INTEGER NOT NULL DEFAULT 0, status INTEGER NOT NULL DEFAULT 0,
        location TEXT NOT NULL DEFAULT '', rendered_at TEXT NOT NULL DEFAULT '', deployed_at TEXT NOT NULL DEFAULT '',
        src TEXT NOT NULL DEFAULT '');
      CREATE INDEX IF NOT EXISTS files_shard ON files(shard);
      CREATE TABLE IF NOT EXISTS shards (prefix TEXT PRIMARY KEY, shard TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS gsc (path TEXT PRIMARY KEY, impressions INTEGER NOT NULL, clicks INTEGER NOT NULL);
      CREATE TABLE IF NOT EXISTS retired (path TEXT PRIMARY KEY, since TEXT NOT NULL);
    """)
    if 'src' not in [r[1] for r in db.execute('PRAGMA table_info(files)')]:
        db.execute("ALTER TABLE files ADD COLUMN src TEXT NOT NULL DEFAULT ''")
    return db


# ---------- lifecycle: Search Console impressions, hidden products, retired products ----------
def gsc_fetch(db, out_file=None):
    """Impressions + clicks per page of the last 90 days (GSC keeps 16 months; the API pages by 25 000 rows).
    With out_file: only write them as JSON (Malina fetches them and hands them encrypted to GitHub Actions, so the
    service account — read access to every site of Kenny's — never leaves Malina)."""
    import jwt  # noqa: PLC0415 — only this step needs PyJWT / requests
    import requests  # noqa: PLC0415
    d = json.loads(GSC_KEY.read_text())
    now = int(time.time())
    a = jwt.encode({'iss': d['client_email'], 'scope': 'https://www.googleapis.com/auth/webmasters.readonly',
                    'aud': 'https://oauth2.googleapis.com/token', 'iat': now, 'exp': now + 3600}, d['private_key'], algorithm='RS256')
    tok = requests.post('https://oauth2.googleapis.com/token', data={'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'assertion': a}, timeout=30).json()['access_token']
    h = {'Authorization': f'Bearer {tok}'}
    sites = [x['siteUrl'] for x in requests.get('https://www.googleapis.com/webmasters/v3/sites', headers=h, timeout=30).json().get('siteEntry', [])]
    if GSC_SITE not in sites:   # a wrong property answers empty rows without an error (memory gsc-spatna-property-tise-lze)
        raise SystemExit(f'GSC: no access to {GSC_SITE}')
    end = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 2 * 86400))
    start = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 92 * 86400))
    rows, start_row = [], 0
    while True:
        r = requests.post(f'https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(GSC_SITE, safe="")}/searchAnalytics/query', headers=h, timeout=120,
                          json={'startDate': start, 'endDate': end, 'dimensions': ['page'], 'rowLimit': 25000, 'startRow': start_row, 'dataState': 'all'})
        if r.status_code != 200:
            raise SystemExit(f'GSC {r.status_code}: {r.text[:200]}')
        part = r.json().get('rows', [])
        rows += part
        if len(part) < 25000:
            break
        start_row += 25000
    out = {}
    for x in rows:
        u = urllib.parse.urlsplit(x['keys'][0])
        if u.netloc.removeprefix('www.') != 'sporteka.cz':
            continue
        p = urllib.parse.unquote(u.path) or '/'
        i, c = out.get(p, (0, 0))
        out[p] = (i + int(x['impressions']), c + int(x['clicks']))
    if out_file:
        Path(out_file).write_text(json.dumps({'start': start, 'end': end, 'pages': out}))
        print(f'GSC {start}..{end}: {len(out)} pages with impressions → {out_file}')
        return
    gsc_store(db, start, end, out)


def gsc_store(db, start, end, out):
    db.execute('DELETE FROM gsc')
    db.executemany('INSERT INTO gsc VALUES (?, ?, ?)', [(p, i, c) for p, (i, c) in out.items()])
    db.execute("INSERT OR REPLACE INTO meta VALUES ('gsc_end', ?)", (end,))
    db.commit()
    print(f'GSC {start}..{end}: {len(out)} pages with impressions')


def gsc_load(db, file):
    d = json.loads(Path(file).read_text())
    gsc_store(db, d['start'], d['end'], {p: tuple(v) for p, v in d['pages'].items()})


def prepare(db):
    """LIVE → the render copy, then the lifecycle rules (Kenny 8. 11.: new products in, products nobody sells or nobody
    finds out): a product older than GRACE_DAYS with one shop and no impression in 90 days becomes noindex (out of the
    sitemap, page stays for visitors); retired products (no offer, katalog.py → redirects table) are tracked with a date."""
    if subprocess.run(['pgrep', '-f', 'port 879[9]'], capture_output=True).returncode == 0:
        raise SystemExit('stop the local SSR (wrangler dev) first: it holds the render copy')
    tmp = CATALOG.with_suffix('.tmp')
    CATALOG.parent.mkdir(parents=True, exist_ok=True)   # a fresh GitHub runner has no tmp-static/state yet (10. 11.)
    shutil.copyfile(LIVE, tmp)
    for suf in ('-wal', '-shm'):
        Path(str(CATALOG) + suf).unlink(missing_ok=True)
    os.replace(tmp, CATALOG)
    c = sqlite3.connect(CATALOG)
    c.execute('ATTACH ? AS st', (str(STATE),))
    # the rule only acts on fresh numbers: stale impressions would hide products that Google meanwhile shows
    gsc_end = (c.execute("SELECT value FROM st.meta WHERE key = 'gsc_end'").fetchone() or [''])[0]
    have_gsc = c.execute('SELECT COUNT(*) FROM st.gsc').fetchone()[0] > 0 and \
        gsc_end >= time.strftime('%Y-%m-%d', time.gmtime(time.time() - 21 * 86400))
    hidden = 0
    if have_gsc:
        hidden = c.execute(f"""UPDATE products SET noindex = 1 WHERE status = 'publish' AND noindex = 0 AND shop_count < 2
            AND created_at < date('now', '-{GRACE_DAYS} days') AND '/' || slug || '/' NOT IN (SELECT path FROM st.gsc)""").rowcount
        files = [r[0] for r in c.execute("SELECT DISTINCT (id - 1) / 5000 + 1 FROM products WHERE status = 'publish' AND noindex = 0 AND offer_count > 0 ORDER BY 1")]
        c.execute("UPDATE site_cache SET value = ? WHERE key = 'sitemap:files'", (json.dumps(files),))
    today = time.strftime('%Y-%m-%d')
    c.execute('INSERT OR IGNORE INTO st.retired SELECT from_path, ? FROM redirects', (today,))
    c.execute('DELETE FROM st.retired WHERE path NOT IN (SELECT from_path FROM redirects)')
    c.commit()
    print(f'render copy ready; {hidden} products hidden (noindex) by the lifecycle rule'
          + ('' if have_gsc else ' — no fresh GSC data (≤ 21 days), rule skipped'))


def redirect_plan(m):
    """shard → [(from, to, status)] as real 301 rules (the most valuable first, ≤ RULES_PER_SHARD) and path → to as stubs."""
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    st = sqlite3.connect(f'file:{STATE}?mode=ro', uri=True)
    imp = dict(st.execute('SELECT path, impressions + 100 * clicks FROM gsc'))
    since = dict(st.execute('SELECT path, since FROM retired'))
    cut = time.strftime('%Y-%m-%d', time.gmtime(time.time() - STUB_DAYS * 86400))
    per = {}
    for frm, to, code in c.execute('SELECT from_path, to_path, status FROM redirects'):
        if frm != to:
            per.setdefault(shard_of(frm, m), []).append((frm, to, code if code in (301, 302) else 301))
    rules, stubs = {}, {}
    for sh, lst in per.items():
        lst.sort(key=lambda r: (-imp.get(r[0], 0), r[0]))
        rules[sh] = sorted(lst[:RULES_PER_SHARD])
        for frm, to, _ in lst[RULES_PER_SHARD:]:
            if imp.get(frm, 0) > 0 or since.get(frm, '9999') >= cut:
                stubs[frm] = to
    return rules, stubs


STUB = """<!doctype html><html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, follow"><meta http-equiv="refresh" content="0; url={to}"><title>Produkt už se neprodává | Sporteka</title></head>
<body><p>Tento produkt už žádný obchod neprodává. <a href="{to}">Podobné produkty najdete tady</a>.</p></body></html>
"""


# ---------- the list of paths ----------
def listing(base, count):
    """base '/x/' → '/x/', '/x/page/2/', … up to MAX_PAGES."""
    n = min(MAX_PAGES, max(1, -(-count // PER_PAGE)))
    yield base
    for i in range(2, n + 1):
        yield f'{base}page/{i}/'


def fold(t):
    """Same folding as src/scripts/hledat.ts: NFKD, drop combining accents, lower case."""
    return ''.join(ch for ch in unicodedata.normalize('NFKD', t) if not ('\u0300' <= ch <= '\u036f')).lower()


WORD = re.compile(r'[a-z0-9]+')
SEARCH_TOP = 48      # products per word file
SEARCH_MIN = 2       # a word needs at least this many products to get a file


@functools.lru_cache(maxsize=1)
def search_index():
    """word → ids of the SEARCH_TOP most popular products whose name has it; word → product count."""
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    post, count = {}, {}
    for pid, name in c.execute("SELECT id, name FROM products WHERE status = 'publish' AND offer_count > 0 ORDER BY pop DESC, id"):
        for w in set(WORD.findall(fold(html.unescape(name)))):
            if len(w) < 2 or len(w) > 40:
                continue
            count[w] = count.get(w, 0) + 1
            lst = post.setdefault(w, [])
            if len(lst) < SEARCH_TOP:
                lst.append(pid)
    keep = {w for w, n in count.items() if n >= SEARCH_MIN}
    return {w: post[w] for w in keep}, {w: count[w] for w in keep}


FILTER_TOP = 6000     # products per listing in the filter data (most popular first)
CHUNK = 100           # cards per card file


def value_slug(v):
    """src/lib/params.ts valueSlug."""
    return re.sub(r'[^a-z0-9]+', '-', fold(v)).strip('-')


@functools.lru_cache(maxsize=1)
def filter_index():
    """listing key ('c/<slug>', 'b/<slug>', 'slevy') → product ids (most popular first, ≤ FILTER_TOP); landing slug → (key, qs).
    Sequential scans + in-memory sort: one join per listing would read the 2 GB DB at random from the SD card."""
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    pop = {pid: (-pp, pid) for pid, pp in c.execute("SELECT id, pop FROM products WHERE status = 'publish' AND offer_count > 0")}
    cats = dict(c.execute('SELECT id, slug FROM categories WHERE count_total > 0'))
    brands = dict(c.execute('SELECT id, slug FROM brands WHERE count > 1'))
    groups = {}
    for cid, pid in c.execute('SELECT cat_id, product_id FROM cat_products'):
        if cid in cats and pid in pop:
            groups.setdefault('c/' + cats[cid], []).append(pid)
    for bid, pid in c.execute('SELECT brand_id, product_id FROM brand_products'):
        if bid in brands and pid in pop:
            groups.setdefault('b/' + brands[bid], []).append(pid)
    groups['slevy'] = [pid for (pid,) in c.execute("SELECT id FROM products WHERE status = 'publish' AND offer_count > 0 AND disc_pct > 0")]
    out = {k: sorted(set(v), key=pop.__getitem__)[:FILTER_TOP] for k, v in groups.items() if len(v) > 1}
    lands = {slug: ('c/' + base, qs) for slug, base, qs in c.execute('SELECT slug, base_slug, qs FROM facet_pages') if 'c/' + base in out}
    return out, lands


def filter_paths():
    lists, lands = filter_index()
    for k, ids in lists.items():
        yield f'/_f/{k}/a.json'
        for n in range(-(-len(ids) // CHUNK)):
            yield f'/_f/{k}/{n}.json'
    for slug in lands:
        yield f'/_f/l/{slug}.json'


def search_paths():
    post, _ = search_index()
    yield '/_s/n.json'
    for p2 in sorted({w[:2] for w in post}):
        yield f'/_s/t/{p2}.json'
    for w in post:
        yield f'/_s/w/{w}.json'


def all_paths():
    """(path, kind) of every page the static site serves (static files of dist/client come separately)."""
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    yield '/', 'home'
    for p in ('/kategorie/', '/obchody/', '/hledat/', '/api/health', '/robots.txt', '/sitemap_index.xml',
              '/category-sitemap.xml', '/brand-sitemap.xml', '/page-sitemap.xml'):
        yield p, 'page'
    row = c.execute("SELECT value FROM site_cache WHERE key = 'sitemap:files'").fetchone()
    for n in json.loads(row[0]) if row else []:
        yield f'/product-sitemap{n}.xml', 'sitemap'
    disc = c.execute("SELECT COUNT(*) FROM products WHERE status = 'publish' AND offer_count > 0 AND disc_pct > 0").fetchone()[0]
    for p in listing('/slevy/', disc):
        yield p, 'listing'
    for slug, total in c.execute('SELECT slug, count_total FROM categories'):
        for p in listing(f'/{slug}/', total):
            yield p, 'listing'
    for slug, total in c.execute('SELECT slug, count FROM brands WHERE count > 0'):
        for p in listing(f'/znacka/{slug}/', total):
            yield p, 'listing'
    for slug, total in c.execute('SELECT slug, total FROM facet_pages'):
        for p in listing(f'/{slug}/', total):
            yield p, 'listing'
    for (slug,) in c.execute("SELECT slug FROM slugs WHERE kind IN ('page', 'post', 'postcat')"):
        yield f'/{slug}/', 'page'
    for (slug,) in c.execute("SELECT slug FROM products WHERE status = 'publish' AND offer_count > 0"):
        yield f'/{slug}/', 'product'
    for p in search_paths():
        yield p, 'data'
    for p in filter_paths():
        yield p, 'data'
    m = dict(sqlite3.connect(f'file:{STATE}?mode=ro', uri=True).execute('SELECT prefix, shard FROM shards')) if STATE.exists() else {}
    if m:
        for p in redirect_plan(m)[1]:
            yield p, 'stub'


def client_files():
    """path → absolute file of the built static assets (always hashed locally, never stored). Hashed bundles of earlier
    builds (/_astro/*) are kept in KEEP and deployed too: pages rendered by an older build still point at them."""
    out = {}
    KEEP.mkdir(parents=True, exist_ok=True)
    for f in (CLIENT / '_astro').glob('*'):
        if not (KEEP / f.name).exists():
            shutil.copy2(f, KEEP / f.name)
    for f in KEEP.glob('*'):
        out['/_astro/' + f.name] = str(f)
    for f in CLIENT.rglob('*'):
        if f.is_file() and f.name not in SKIP_CLIENT:
            out['/' + f.relative_to(CLIENT).as_posix()] = str(f)
    return out


def file_of(path):
    """URL path → file path inside a shard ('/x/' → '/x/index.html')."""
    return path + 'index.html' if path.endswith('/') else path


# ---------- shard map ----------
def split(prefix, keys, depth=0):
    """Leaves (prefix, count) so that no leaf holds more than CAP keys."""
    if len(keys) <= CAP:
        return [(prefix, len(keys))]
    groups = {}
    for k in keys:
        if len(k) > len(prefix):
            groups.setdefault(k[len(prefix)], []).append(k)
    out = []
    for ch in sorted(groups):
        out += split(prefix + ch, groups[ch], depth + 1)
    return out


def plan(db, force=False):
    have = db.execute('SELECT COUNT(*) FROM shards').fetchone()[0]
    if have and not force:
        return
    keys = [p.lstrip('/') for p, _ in all_paths()] + [p.lstrip('/') for p in client_files()]
    keys = [k for k in keys if k]   # the home page stays in main
    root = {}
    for k in keys:
        root.setdefault(k[0], []).append(k)
    leaves = []
    for ch in sorted(root):
        leaves += split(ch, root[ch])
    # contiguous packing in prefix order: small leaves (< SPLIT_MIN) go to main
    shards, cur, n = [], [], 0
    rest = sum(c for _, c in leaves if c < SPLIT_MIN)
    for pfx, cnt in leaves:
        if cnt < SPLIT_MIN:
            continue
        if n + cnt > CAP and cur:
            shards.append(cur); cur, n = [], 0
        cur.append(pfx); n += cnt
    if cur:
        shards.append(cur)
    db.execute('DELETE FROM shards')
    for i, pfxs in enumerate(shards, 1):
        for p in pfxs:
            db.execute('INSERT INTO shards VALUES (?, ?)', (p, f's{i:02d}'))
    db.commit()
    print(f'{len(shards)} shards + main ({rest} files in small prefixes → main)')


def shard_map(db):
    m = dict(db.execute('SELECT prefix, shard FROM shards'))
    if not m:
        raise SystemExit('no shard map: run plan first')
    return m


def shard_of(path, m):
    k = path.lstrip('/')
    for i in range(len(k), 0, -1):
        s = m.get(k[:i])
        if s:
            return s
    return MAIN


def sync_paths(db):
    """Insert new paths into files, drop paths that no longer exist (their files leave with the next deploy)."""
    m = shard_map(db)
    now = {p: k for p, k in all_paths()}
    old = {p for (p,) in db.execute('SELECT path FROM files')}
    db.executemany('INSERT INTO files (path, kind, shard) VALUES (?, ?, ?)',
                   [(p, k, shard_of(p, m)) for p, k in now.items() if p not in old])
    gone = old - now.keys()
    db.executemany('DELETE FROM files WHERE path = ?', [(p,) for p in gone])
    # after plan --force: move paths to their new shard (their hash stays valid, blobs are per account)
    moved = [(s, p) for p, cur in db.execute('SELECT path, shard FROM files').fetchall() if (s := shard_of(p, m)) != cur]
    db.executemany('UPDATE files SET shard = ? WHERE path = ?', moved)
    db.commit()
    return len(now.keys() - old), len(gone)


# ---------- what changed since the last render ----------
def build_stamp():
    """Templates + assets of this build and the render month: a new value re-renders everything."""
    h = hashlib.sha256()
    for f in sorted((APP / 'dist' / 'server').rglob('*.mjs')):
        h.update(f.read_bytes())
    for f in sorted(CLIENT.rglob('*')):
        if f.is_file():
            h.update(f.name.encode())
    h.update(os.environ.get('DATA_DAY', '')[:7].encode())
    return h.hexdigest()[:16]


def product_hashes():
    """path → hash of everything a product page is built from (src/lib/views.ts productView): the product row (without
    pop), active offers, price history, parameters, categories, brand, and the related neighbours (static mode: the 8
    products added around it in its main category, without prices). Sequential scans, grouped in memory."""
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    cols = [r[1] for r in c.execute('PRAGMA table_info(products)') if r[1] not in ('pop', 'last_offer_at')]
    acc = {}

    def add(pid, *parts):
        h = acc.get(pid)
        if h is not None:
            h.update(repr(parts).encode())
    rows = {}
    for r in c.execute(f"SELECT {', '.join(cols)} FROM products WHERE status = 'publish' AND offer_count > 0"):
        pid = r[0]
        acc[pid] = hashlib.sha1(repr(r).encode())
        rows[pid] = (r[cols.index('slug')], r[cols.index('primary_cat')], r[cols.index('created_at')], r[cols.index('name')],
                     r[cols.index('image')], r[cols.index('shop_count')] or r[cols.index('offer_count')])
    for r in c.execute('SELECT product_id, id, domain, price, price_old, stock, target_url, sizes, delivery_price, title, img, go_slug, variants, extra '
                       'FROM offers WHERE active = 1 ORDER BY product_id, id'):
        add(r[0], 'o', r[1:])
    for r in c.execute('SELECT product_id, day, min_price FROM price_history ORDER BY product_id, day'):
        add(r[0], 'h', r[1:])
    for r in c.execute('SELECT product_id, key, value FROM product_params ORDER BY product_id, key, value'):
        add(r[0], 'p', r[1:])
    # categories of the product + the whole category / brand tables (names and slugs appear in crumbs and links)
    glob = hashlib.sha1()
    for r in c.execute('SELECT id, slug, name, parent, noindex FROM categories ORDER BY id'):
        glob.update(repr(r).encode())
    brand = {bid: repr(r) for bid, *r in c.execute('SELECT id, slug, name, noindex FROM brands')}
    neigh = {}
    for cid, created, pid in c.execute('SELECT cat_id, created_at, product_id FROM cat_products ORDER BY cat_id, created_at, product_id'):
        add(pid, 'c', cid)
        if pid in rows and rows[pid][1] == cid:
            neigh.setdefault(cid, []).append(pid)
    g = glob.hexdigest()
    out = {}
    for cid, lst in neigh.items():
        for i, pid in enumerate(lst):
            rel = [rows[x][0:1] + rows[x][3:] for x in lst[max(0, i - 8):i + 9] if x != pid]
            add(pid, 'r', rel)
    for pid, h in acc.items():
        h.update(g.encode())
        out[f'/{rows[pid][0]}/'] = h.hexdigest()[:16]
    return out


@functools.lru_cache(maxsize=1)
def cached_hashes():
    return product_hashes()


# ---------- render ----------
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def fetch(path):
    req = urllib.request.Request(BASE + path, headers={'User-Agent': 'sporteka-static/1.0'})
    for attempt in range(3):
        try:
            with OPENER.open(req, timeout=120) as r:
                return r.status, r.read(), ''
        except urllib.error.HTTPError as e:
            return e.code, e.read(), e.headers.get('location') or ''
        except Exception:  # noqa: BLE001 — workerd restarts / timeouts: retry
            time.sleep(2 + attempt * 3)
    return 0, b'', ''


def write_out(path, body):
    f = OUT / file_of(path).lstrip('/')
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_bytes(body)


def render(db, shard, limit=None, threads=8, only_missing=False, kind=None, changed=False, sync=True, first_page=False, ignore_stamp=False):
    if sync:
        sync_paths(db)
    sql = "SELECT path, kind, src, hash FROM files WHERE (shard = ? OR ? = 'ALL') AND kind != 'data'" + (" AND hash = ''" if only_missing else '') \
        + (' AND kind = ?' if kind else '') + ' ORDER BY path'
    rows = db.execute(sql, (shard, shard) + ((kind,) if kind else ())).fetchall()
    if first_page:   # texts only show on page 1 of a listing
        rows = [r for r in rows if '/page/' not in r[0]]
    src = {}
    if changed:
        # products only when their data (or the build / month) changed; every other page is rendered (listings show prices)
        stamp = build_stamp()
        src = {p: f'{stamp}:{h}' for p, h in cached_hashes().items()}
        if ignore_stamp:   # daily: only a changed product row / offer / price history re-renders a product, not a new build (that is the weekly run's job)
            rows = [r for r in rows if r[1] != 'product' or not r[3] or src.get(r[0], '').split(':')[-1] != (r[2] or '').split(':')[-1]]
        else:
            rows = [r for r in rows if r[1] != 'product' or not r[3] or src.get(r[0]) != r[2]]   # no hash = never deployed (a failed deploy): render again
    stubs = redirect_plan(shard_map(db))[1]
    stamp0 = time.strftime('%Y-%m-%dT%H:%M:%S')
    for r in [r for r in rows if r[1] == 'stub']:
        write_out(r[0], STUB.format(to=html.escape(stubs.get(r[0], '/'))).encode())
        db.execute('UPDATE files SET status = 200, rendered_at = ? WHERE path = ?', (stamp0, r[0]))
    rows = [r for r in rows if r[1] != 'stub']
    paths = [r[0] for r in rows]
    # products in catalogue id order: their rows (offers, categories, price history) sit next to each other in the DB, so the
    # SD card reads sequentially — 58 ms/page instead of 205 ms in slug order
    ids = dict(sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True).execute("SELECT '/' || slug || '/', id FROM products"))
    paths.sort(key=lambda p: (ids.get(p, 0), p))
    if limit:
        paths = paths[:limit]
    # 404 page of every shard (a path that matches nothing)
    st, body, _ = fetch('/404/')
    if st != 404 or b'<html' not in body:
        raise SystemExit(f'404 page: HTTP {st}')
    (OUT).mkdir(parents=True, exist_ok=True)
    (OUT / '404.html').write_bytes(body)
    t0, done, stats = time.time(), 0, {}
    stamp = time.strftime('%Y-%m-%dT%H:%M:%S')
    full = []
    def chunks():
        for i in range(0, len(paths), 1000):
            if DEADLINE and time.time() > DEADLINE:
                print(f'  deadline reached after {i} pages', flush=True)
                return
            if shutil.disk_usage(OUT).free < DISK_MIN:   # SD card full on 9. 11.: deploy what is rendered, then go on
                if i == 0:
                    raise SystemExit(f'disk full: less than {DISK_MIN / 1e9:.1f} GB free on the SD card before rendering {shard}')
                print(f'  disk nearly full after {i} pages: deploy first', flush=True)
                full.append(i)
                return
            yield from zip(paths[i:i + 1000], ex.map(fetch, paths[i:i + 1000]))
    # rows are written in short bursts (every 100 pages, lock held for milliseconds), so a second render worker
    # (STATIC_PORT/STATIC_PERSIST) can share the state DB; one long transaction per 2000 pages locked it for minutes
    ok, moved, bad = [], [], []
    def flush():
        db.executemany('UPDATE files SET status = 200, location = \'\', rendered_at = ?, src = ? WHERE path = ?', ok)
        db.executemany('UPDATE files SET status = ?, location = ?, hash = \'\', rendered_at = ? WHERE path = ?', moved)
        db.executemany('UPDATE files SET status = ?, hash = \'\', rendered_at = ? WHERE path = ?', bad)
        db.commit()
        ok.clear(), moved.clear(), bad.clear()
    with cf.ThreadPoolExecutor(threads) as ex:
        for path, (st, body, loc) in chunks():
            stats[st] = stats.get(st, 0) + 1
            if st == 200:
                write_out(path, body)
                ok.append((stamp, src.get(path, ''), path))
            elif st in (301, 302, 308):
                moved.append((st, loc, stamp, path))
            else:
                bad.append((st, stamp, path))
            done += 1
            if done % 100 == 0:
                flush()
            if done % 2000 == 0:
                el = time.time() - t0
                print(f'  {done}/{len(paths)}  {el / done * 1000:.0f} ms/page  {stats}', flush=True)
    flush()
    el = time.time() - t0
    print(f'{shard}: {done} paths in {el:.0f} s ({el / max(done, 1) * 1000:.0f} ms/page) {stats}')
    return 'disk' if full else ''


# ---------- search index files (/_s/, read by src/scripts/hledat.ts) ----------
def build_search(db, threads=8):
    sync_paths(db)
    post, count = search_index()
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    names = {
        'c': [[f'/{slug}/', html.unescape(n), t] for slug, n, t in
              c.execute('SELECT slug, name, count_total FROM categories WHERE count_total > 0 AND noindex = 0 ORDER BY count_total DESC')],
        'b': [[f'/znacka/{slug}/', html.unescape(n), t] for slug, n, t in
              c.execute("SELECT slug, name, count FROM brands WHERE count > 0 AND slug != 'ostatni' ORDER BY count DESC")],
    }
    files = {'/_s/n.json': names}
    by2 = {}
    for w, n in count.items():
        by2.setdefault(w[:2], []).append([w, n])
    for p2, lst in by2.items():
        files[f'/_s/t/{p2}.json'] = sorted(lst, key=lambda x: (-x[1], x[0]))
    # card data from the local SSR (thumb signing, price formatting stay in one place: src/pages/api/static-cards.ts)
    cards = fetch_cards({i for lst in post.values() for i in lst}, threads)
    for w, lst in post.items():
        files[f'/_s/w/{w}.json'] = [cards[i] for i in lst if i in cards]
    stamp = time.strftime('%Y-%m-%dT%H:%M:%S')
    for path, data in files.items():
        write_out(path, json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode())
    db.executemany("UPDATE files SET status = 200, rendered_at = ? WHERE path = ?", [(stamp, p) for p in files])
    db.commit()
    print(f'search index: {len(files)} files, {len(cards)} product cards')


# ---------- listing filter data (/_f/, read by src/scripts/filtry.ts) ----------
def fetch_cards(ids, threads):
    def batch(chunk):
        st, body, _ = fetch('/api/static-cards?ids=' + ','.join(map(str, chunk)))
        if st != 200:
            raise SystemExit(f'static-cards: HTTP {st}')
        return json.loads(body)
    cards = {}
    ids = sorted(ids)
    with cf.ThreadPoolExecutor(threads) as ex:
        for rows in ex.map(batch, [ids[i:i + 90] for i in range(0, len(ids), 90)]):
            for r in rows:
                cards[r[0]] = r
    return cards


def build_filters(db, threads=8):
    """Per listing: a.json = {n, b: brand slugs, s: shop domains, p: 'key=value' list, r: [[price, brand, shops, stock, disc,
    day, params]]} in popularity order, and the cards in files of CHUNK (<n>.json, same order)."""
    sync_paths(db)
    lists, lands = filter_index()
    need = {i for ids in lists.values() for i in ids}
    c = sqlite3.connect(f'file:{CATALOG}?mode=ro', uri=True)
    bslug = dict(c.execute('SELECT id, slug FROM brands'))
    attr = {}
    for pid, price, bid, stock, disc, created in c.execute("SELECT id, min_price, brand_id, in_stock, disc_pct, created_at FROM products WHERE status = 'publish' AND offer_count > 0"):
        if pid in need:
            day = int(time.mktime(time.strptime(created[:10], '%Y-%m-%d')) // 86400) if created else 0
            attr[pid] = [round(price), bslug.get(bid, ''), stock, disc, day]
    shops, params = {}, {}
    for pid, dom in c.execute('SELECT product_id, domain FROM offers WHERE active = 1'):
        if pid in need:
            shops.setdefault(pid, set()).add(dom)
    for pid, key, val in c.execute('SELECT product_id, key, value FROM product_params'):
        if pid in need:
            params.setdefault(pid, set()).add(f'{key}={value_slug(val)}')
    cards = fetch_cards(need, threads)
    files = {}
    for k, ids in lists.items():
        ids = [i for i in ids if i in cards]
        bi, si, pi = {}, {}, {}
        idx = lambda d, v: d.setdefault(v, len(d))  # noqa: E731
        rows = []
        for i in ids:
            price, b, stock, disc, day = attr[i]
            sh = [idx(si, d) for d in sorted(shops.get(i, ()))]
            rows.append([price, idx(bi, b), sh[0] if len(sh) == 1 else sh, stock, disc, day, [idx(pi, v) for v in sorted(params.get(i, ()))]])
        files[f'/_f/{k}/a.json'] = {'n': len(ids), 'c': CHUNK, 'b': list(bi), 's': list(si), 'p': list(pi), 'r': rows}
        for n in range(-(-len(ids) // CHUNK)):
            files[f'/_f/{k}/{n}.json'] = [cards[i] for i in ids[n * CHUNK:(n + 1) * CHUNK]]
    for slug, (k, qs) in lands.items():
        files[f'/_f/l/{slug}.json'] = {'k': k, 'q': qs}
    stamp = time.strftime('%Y-%m-%dT%H:%M:%S')
    for path, data in files.items():
        write_out(path, json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode())
    db.executemany('UPDATE files SET status = 200, rendered_at = ? WHERE path = ?', [(stamp, p) for p in files])
    db.commit()
    print(f'filter data: {len(lists)} listings, {len(files)} files, {len(cards)} cards')


# ---------- deploy ----------
def redirects_for(db, shard, m):
    """_redirects of one shard: retired products / renamed categories (catalogue table) + paths that render as 301."""
    rules, _ = redirect_plan(m)
    lines = [f'{frm} {to} {code}' for sh, lst in sorted(rules.items()) if sh == shard or shard == 'ALL' for frm, to, code in lst]
    for path, st, loc in db.execute("SELECT path, status, location FROM files WHERE (shard = ? OR ? = 'ALL') AND status IN (301, 302, 308) AND location != ''", (shard, shard)):
        loc = loc.replace('https://sporteka.cz', '')
        lines.append(f'{path} {loc} 301')
    if shard in (MAIN, 'ALL'):
        lines.append('/produkt/:slug/ /:slug/ 301')
    seen, uniq = set(), []   # Cloudflare refuses a _redirects file with two rules for one path (a retired product is in the catalogue table AND renders as a 301)
    for ln in lines:
        k = ln.split(' ', 1)[0]
        if k not in seen:
            seen.add(k)
            uniq.append(ln)
    lines = uniq
    if len(lines) > 2000:
        print(f'  !! {len(lines)} redirects > 2000: keeping the first 2000', file=sys.stderr)
        lines = lines[:2000]
    return '\n'.join(lines) + '\n'


def deploy(db, shard, worker=None, noindex=False):
    m = shard_map(db)
    worker = worker or worker_name(shard, 'sporteka')
    # shard ALL = every rendered file in one Worker (test deploys of a sample only; ≤ 100 000 files)
    every = shard == 'ALL'
    files = {}
    for p, f in client_files().items():
        if every or shard_of(p, m) == shard:
            files[p] = {'file': f}
    files['/404.html'] = {'file': str(OUT / '404.html')}
    pending = []
    rows = db.execute('SELECT path, hash, size, status FROM files WHERE status = 200') if every else \
        db.execute('SELECT path, hash, size, status FROM files WHERE shard = ?', (shard,))
    for path, h, size, st in rows:
        if st != 200:
            continue
        local = OUT / file_of(path).lstrip('/')
        if local.exists():
            files[file_of(path)] = {'file': str(local)}
            pending.append(path)
        elif h:
            files[file_of(path)] = {'hash': h, 'size': size}
    headers = SECURITY + ('/*\n  X-Robots-Tag: noindex, nofollow\n' if noindex else '')
    manifest = {'worker': worker, 'compatibility_date': COMPAT,
                'config': {'html_handling': 'auto-trailing-slash', 'not_found_handling': '404-page'},
                'redirects': redirects_for(db, shard, m), 'headers': headers, 'files': files, 'workers_dev': noindex}
    mf = APP / 'tmp-static' / f'manifest-{shard}.json'
    mf.write_text(json.dumps(manifest))
    r = subprocess.run(['node', 'scripts/cf-assets.mjs', str(mf)], cwd=APP, capture_output=True, text=True)
    mf.unlink()
    if r.returncode == 3:
        miss = json.loads(r.stdout.strip().splitlines()[-1])['paths']
        # file paths ('/x/index.html') map back to page paths ('/x/'); IN keeps the primary key lookup (OR scanned 820k rows per path)
        db.executemany("UPDATE files SET hash = '', src = '' WHERE path IN (?, ?)",
                       [(p, p[:-len('index.html')] if p.endswith('/index.html') else p) for p in miss])
        db.commit()
        raise MissingBlobs(f'{len(miss)} blobs missing on Cloudflare: render --only-missing and deploy again')
    if r.returncode != 0:
        raise SystemExit(f'cf-assets failed: {r.stderr.strip()[-600:]}')
    res = json.loads(r.stdout.strip().splitlines()[-1])
    stamp = time.strftime('%Y-%m-%dT%H:%M:%S')
    by_file = {file_of(p): p for p in pending}
    for fp, (h, size) in res['hashes'].items():
        p = by_file.get(fp)
        if p:
            db.execute('UPDATE files SET hash = ?, size = ?, deployed_at = ? WHERE path = ?', (h, size, stamp, p))
    db.commit()
    for p in pending:
        (OUT / file_of(p).lstrip('/')).unlink(missing_ok=True)
    print(f'{worker}: {res["total"]} files, {res["uploaded"]} uploaded ({res["bytes"] / 1e6:.1f} MB)')


class MissingBlobs(SystemExit):
    """The state names a file hash Cloudflare no longer holds (those rows are reset to hash ''); weekly re-renders them."""


def deploy_retry(db, sh, worker, noindex, threads):
    """deploy; when Cloudflare misses blobs, render exactly those pages (hash reset by deploy) and deploy again."""
    for attempt in range(3):
        try:
            return deploy(db, sh, worker, noindex)
        except MissingBlobs as e:
            print(f'{sh}: {e} — re-rendering them (attempt {attempt + 1})', flush=True)
            render(db, sh, threads=threads, only_missing=True, sync=False)
    deploy(db, sh, worker, noindex)


# ---------- the whole weekly run ----------
DEADLINE = 0          # epoch seconds: render stops starting new pages after it (weekly --until)
DISK_MIN = 1_500_000_000   # bytes free on the SD card below which render stops and deploys what it has
SHARD_STOP = 95_000   # a shard this full stops the run (plan --force needed); Cloudflare refuses 100 000


def env_file():
    """Env of the local SSR: production mode, static export, render day = first day of the month (pages change monthly
    at most, see GrafCen.astro), IMG_SECRET from credentials/ (never printed)."""
    sec = cred('IMG_SECRET')
    if not sec:
        raise SystemExit('IMG_SECRET missing in credentials/.sporteka-credentials.env')
    f = APP / 'tmp-static' / 'static.env'
    f.write_text(f"ENVIRONMENT=production\nSITE_URL=https://sporteka.cz\nALLOWED_HOSTS=localhost,127.0.0.1\nSTATIC_EXPORT=1\n"
                 f"DATA_DAY={time.strftime('%Y-%m-01')}\nIMG_SECRET={sec}\n")
    os.chmod(f, 0o600)
    return f


def worker_name(shard, prefix):
    return f'{prefix}-{"s00" if shard == MAIN else shard}'


def weekly(db, threads, prefix, noindex, only=None, skip_prep=False, skip_data=False, until='', texts=False, daily=False):
    """texts=True: only the first page of every listing (category, facet landing, brand, /slevy/) — new or changed
    texts in src/texts/ go live in minutes instead of the full render; search / filter data stay as they are."""
    global DEADLINE
    t0 = time.time()
    if until:   # HH:MM today, or tomorrow when already past
        hh, mm = map(int, until.split(':'))
        lt = time.localtime()
        DEADLINE = time.mktime((lt.tm_year, lt.tm_mon, lt.tm_mday, hh, mm, 0, 0, 0, -1))
        if DEADLINE < time.time():
            DEADLINE += 86400
    os.environ['DATA_DAY'] = time.strftime('%Y-%m-01')
    if not skip_prep:
        try:
            if os.environ.get('GSC_FILE'):   # GitHub Actions: numbers fetched on Malina (no Google key in the cloud)
                gsc_load(db, os.environ['GSC_FILE'])
            else:
                gsc_fetch(db)
        except (SystemExit, Exception) as e:  # noqa: BLE001 — prepare skips the rule when the numbers are stale
            print(f'GSC skipped: {e}')
        prepare(db)
        r = subprocess.run(['npx', 'astro', 'build'], cwd=APP, env={**os.environ, 'BUILD_ID': 'static'}, capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f'astro build failed: {r.stderr[-500:]}')
    if texts or daily:
        skip_data = True
    (APP / 'tmp-static').mkdir(exist_ok=True)
    log = open(APP / 'tmp-static' / f'wrangler-{PORT}.log', 'w')
    # wrangler dev keeps a local trace of every request (~27 kB each, 2 GB a day filled the SD card on 9. 11.) unless
    # X_LOCAL_OBSERVABILITY=false (the config's observability switch does not stop it); drop any old trace store
    shutil.rmtree(APP / PERSIST / 'v3/observability', ignore_errors=True)
    # render copy in RAM (STATIC_PERSIST under /tmp, a tmpfs): 19 ms/page instead of ~120 ms from the SD card (9. 11.);
    # refreshed whenever prepare rewrote the copy on the card
    ram = Path(PERSIST)
    if ram.is_absolute() and ram != APP / 'tmp-static/state':
        src_db = CATALOG
        dst_db = ram / CATALOG.relative_to(APP / 'tmp-static/state')
        if not dst_db.exists() or dst_db.stat().st_mtime < src_db.stat().st_mtime:
            shutil.rmtree(ram, ignore_errors=True)
            shutil.copytree(APP / 'tmp-static/state', ram)
            print(f'render copy → {ram}', flush=True)
    srv = subprocess.Popen(['npx', 'wrangler', 'dev', '-c', 'dist/server/wrangler.json', '--local', '--persist-to', PERSIST,
                            '--port', PORT, '--env-file', str(env_file()), '--log-level', 'warn'], cwd=APP, stdout=log, stderr=log, start_new_session=True,
                           env={**os.environ, 'X_LOCAL_OBSERVABILITY': 'false'})
    try:
        for _ in range(120):
            if fetch('/kategorie/')[0] == 200:
                break
            time.sleep(3)
        else:
            raise SystemExit('local SSR did not start (tmp-static/wrangler.log)')
        if not skip_data:
            new, gone = sync_paths(db)
            print(f'paths +{new} -{gone}')
            full = [s for s, n in db.execute('SELECT shard, COUNT(*) FROM files GROUP BY shard') if n > SHARD_STOP]
            if full:
                raise SystemExit(f'shards over {SHARD_STOP} files: {full} — run plan --force (routes change!)')
            build_search(db, threads)
            build_filters(db, threads)
            search_index.cache_clear()
            filter_index.cache_clear()
        shards = [MAIN] + sorted({s for (s,) in db.execute('SELECT DISTINCT shard FROM shards')})
        for sh in (only or shards):
            if DEADLINE and time.time() > DEADLINE:
                print(f'deadline: {sh} and later shards wait for the next run')
                break
            while render(db, sh, threads=threads, changed=not texts, sync=False, kind='listing' if texts else None, first_page=texts, ignore_stamp=daily) == 'disk':
                deploy_retry(db, sh, worker_name(sh, prefix), noindex, threads)   # frees the rendered files, then render the rest
            deploy_retry(db, sh, worker_name(sh, prefix), noindex, threads)
    finally:
        os.killpg(srv.pid, 15)
    print(f'weekly done in {(time.time() - t0) / 3600:.1f} h')


# ---------- cutover / rollback (Worker routes of the zone; rollback = the saved routes back) ----------
ZONE = '9c72125a00cfb703442cca8f7b095819'   # sporteka.cz


def cf_api(method, path, body=None):
    """Cloudflare API: CLOUDFLARE_API_TOKEN (scoped) when set, else the global key from credentials/ (local only)."""
    tok = os.environ.get('CLOUDFLARE_API_TOKEN')
    auth = {'Authorization': f'Bearer {tok}'} if tok else \
        {'X-Auth-Email': cred('CF_EMAIL', '.cloudflare-credentials.env'),
         'X-Auth-Key': cred('CF_GLOBAL_API_KEY', '.cloudflare-credentials.env') or cred('CF_API_KEY', '.cloudflare-credentials.env')}
    req = urllib.request.Request('https://api.cloudflare.com/client/v4' + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={**auth, 'Content-Type': 'application/json'})
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        return json.loads(e.read() or b'{}')


def account():
    return os.environ.get('CLOUDFLARE_ACCOUNT_ID') or cred('CF_ACCOUNT_ID')


def cutover(db, apply=False, only=None):
    """Routes: sporteka.cz/* → sporteka-s00, sporteka.cz/<prefix>* → its shard Worker, /img/* stays on sporteka-img;
    www → apex by a Redirect Rule (the SSR middleware did it). Saves the current routes to backups/ first.
    --only s01,s14: shard by shard while the SSR keeps the rest (/* stays on it); /_astro/* goes to sporteka-s00 at once,
    which also carries the SSR's own bundles (keep-astro), so both kinds of pages find their scripts."""
    want = {'sporteka.cz/_astro/*': worker_name(MAIN, 'sporteka')}   # the SSR Worker + D1 were deleted 10. 11. 2026
    if not only:
        want['sporteka.cz/*'] = worker_name(MAIN, 'sporteka')
    for sh, pfx in db.execute('SELECT shard, prefix FROM shards'):
        if not only or sh in only:
            want[f'sporteka.cz/{pfx}*'] = worker_name(sh, 'sporteka')
    cur = {r['pattern']: r for r in cf_api('GET', f'/zones/{ZONE}/workers/routes')['result']}
    print(f'{len(want)} routes wanted, {len(cur)} now')
    if not apply:
        for pat, w in sorted(want.items())[:8]:
            print(f'  {pat} → {w}' + ('' if pat not in cur else f'   (now {cur[pat].get("script")})'))
        return
    bk = Path('/home/kenny/ai/backups') / f'cf-sporteka-routes-pred-static-{time.strftime("%Y-%m-%d-%H%M")}.json'
    bk.write_text(json.dumps(list(cur.values()), indent=1))
    if only:
        for pat, w in want.items():
            r = cf_api('PUT', f'/zones/{ZONE}/workers/routes/{cur[pat]["id"]}', {'pattern': pat, 'script': w}) if pat in cur \
                else cf_api('POST', f'/zones/{ZONE}/workers/routes', {'pattern': pat, 'script': w})
            if not r.get('success'):
                raise SystemExit(f'route {pat}: {r.get("errors")} — rollback with: staticky.py rollback {bk}')
        print(f'{len(want)} routes live for {only}; backup {bk}')
        return
    rs = cf_api('GET', f'/zones/{ZONE}/rulesets/phases/http_request_dynamic_redirect/entrypoint').get('result') or {}
    rules = [r for r in rs.get('rules', []) if 'www → apex' not in (r.get('description') or '')]
    rules.append({'description': 'www → apex (static sporteka)', 'expression': 'http.host eq "www.sporteka.cz"', 'action': 'redirect', 'enabled': True,
                  'action_parameters': {'from_value': {'status_code': 301, 'preserve_query_string': True,
                                                       'target_url': {'expression': 'concat("https://sporteka.cz", http.request.uri.path)'}}}})
    r = cf_api('PUT', f'/zones/{ZONE}/rulesets/phases/http_request_dynamic_redirect/entrypoint', {'rules': [{k: v for k, v in x.items() if k in ('description', 'expression', 'action', 'enabled', 'action_parameters')} for x in rules]})
    if not r.get('success'):
        raise SystemExit(f'redirect rule: {r.get("errors")}')
    for pat, w in want.items():
        if pat in cur:
            if cur[pat].get('script') != w:
                r = cf_api('PUT', f'/zones/{ZONE}/workers/routes/{cur[pat]["id"]}', {'pattern': pat, 'script': w})
        else:
            r = cf_api('POST', f'/zones/{ZONE}/workers/routes', {'pattern': pat, 'script': w})
        if not r.get('success'):
            raise SystemExit(f'route {pat}: {r.get("errors")} — rollback with: staticky.py rollback {bk}')
    if 'www.sporteka.cz/*' in cur:
        cf_api('DELETE', f'/zones/{ZONE}/workers/routes/{cur["www.sporteka.cz/*"]["id"]}')
    print(f'cutover done; backup {bk}')


def rollback(path):
    old = {r['pattern']: r.get('script') for r in json.loads(Path(path).read_text())}
    cur = {r['pattern']: r for r in cf_api('GET', f'/zones/{ZONE}/workers/routes')['result']}
    for pat, r in cur.items():
        if pat not in old:
            cf_api('DELETE', f'/zones/{ZONE}/workers/routes/{r["id"]}')
        elif r.get('script') != old[pat]:
            cf_api('PUT', f'/zones/{ZONE}/workers/routes/{r["id"]}', {'pattern': pat, 'script': old[pat]})
    for pat, w in old.items():
        if pat not in cur:
            cf_api('POST', f'/zones/{ZONE}/workers/routes', {'pattern': pat, 'script': w})
    print('routes restored (the www redirect rule can stay: the SSR redirects www the same way)')


def parity(db, sample=0, only=None):
    """Every <loc> of the LIVE sitemaps must answer 200 from its static shard (workers.dev of the shard Worker)."""
    m = shard_map(db)
    sub = cf_api('GET', f'/accounts/{account()}/workers/subdomain')['result']['subdomain']
    def get(u):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 sporteka-parity MalinaCron'}), timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, b''
    st, idx = get('https://sporteka.cz/sitemap_index.xml')
    locs = []
    for sm in re.findall(r'<loc>([^<]+)</loc>', idx.decode()):
        locs += re.findall(r'<loc>([^<]+)</loc>', get(sm)[1].decode())
    paths = [urllib.parse.urlsplit(u).path for u in locs]
    if only:
        paths = [p for p in paths if shard_of(p, m) in only]
    if sample:
        import random  # noqa: PLC0415
        paths = random.Random(1).sample(paths, min(sample, len(paths)))
    def check(p):
        w = worker_name(shard_of(p, m), 'sporteka')
        return p, get(f'https://{w}.{sub}.workers.dev{p}')[0]
    bad = []
    with cf.ThreadPoolExecutor(8) as ex:
        for p, code in ex.map(check, paths):
            if code != 200:
                bad.append((p, code))
    print(f'parity: {len(paths)} sitemap URLs, {len(bad)} not 200')
    for p, code in bad[:30]:
        print(f'  {code} {p}')


# ---------- progress + Discord ----------
def discord(text):
    """Message to Kenny: DISCORD_WEBHOOK_URL (GitHub secret; can only post into the one channel), else the bot token on Malina."""
    hook = os.environ.get('DISCORD_WEBHOOK_URL')
    if hook:
        req = urllib.request.Request(hook, method='POST', data=json.dumps({'content': text[:1900]}).encode(),
                                     headers={'Content-Type': 'application/json', 'User-Agent': 'sporteka-static/1.0'})
    else:
        tok = ''
        try:
            for line in open('/home/kenny/Discord/.env', encoding='utf-8'):
                if line.startswith('DISCORD_TOKEN='):
                    tok = line.split('=', 1)[1].strip().strip('"\'')
        except OSError:
            pass
        if not tok:
            print('Discord: no webhook or token')
            return
        req = urllib.request.Request('https://discord.com/api/v10/channels/1519455311558082752/messages', method='POST',
                                     data=json.dumps({'content': text[:1900]}).encode(),
                                     headers={'Authorization': f'Bot {tok}', 'Content-Type': 'application/json', 'User-Agent': 'sporteka-static/1.0'})
    try:
        urllib.request.urlopen(req, timeout=30)
    except Exception as e:  # noqa: BLE001
        print(f'Discord: {type(e).__name__}')


def status(db, notify=False):
    """Staging progress: pages deployed per shard. With --discord: one message when everything is deployed (marker in meta)."""
    rows = db.execute("SELECT shard, COUNT(*), SUM(hash != '' AND status = 200), SUM(status NOT IN (0, 200)) FROM files GROUP BY shard ORDER BY shard").fetchall()
    total = sum(r[1] for r in rows)
    done = sum(r[2] or 0 for r in rows)
    other = sum(r[3] or 0 for r in rows)
    left = total - done - other
    for sh, n, d, o in rows:
        print(f'  {sh}: {d or 0}/{n} deployed, {o or 0} redirect/404')
    print(f'{done}/{total} deployed, {left} left')
    sent = db.execute("SELECT value FROM meta WHERE key = 'done_sent'").fetchone()
    if notify and left == 0 and not sent:
        discord('✅ **sporteka.cz – statická verze je hotová na stagingu** (Claude)\n'
                f'• {done:,} souborů nasazeno do {len(rows)} Workerů (assets-only = 0 $)\n'
                '• hledání a filtry v prohlížeči, týdně se generují jen změněné produkty\n'
                '• živý web zatím jede postaru (SSR + D1)\n'
                'Další krok: kontrola parity a přepnutí rout po shardech (návrat zpět jedním příkazem). Napiš OK a přepnu.'.replace(',', ' '))
        db.execute("INSERT OR REPLACE INTO meta VALUES ('done_sent', ?)", (time.strftime('%Y-%m-%d'),))
        db.commit()
    return left


def main():
    sys.stdout.reconfigure(line_buffering=True)   # cron / background logs show progress as it happens
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['gsc', 'prepare', 'paths', 'plan', 'render', 'search', 'filters', 'deploy', 'routes', 'weekly', 'cutover', 'rollback', 'parity', 'status'])
    ap.add_argument('--shard')
    ap.add_argument('--worker')
    ap.add_argument('--limit', type=int)
    ap.add_argument('--out', help='gsc: write the numbers to this JSON file instead of the state DB')
    ap.add_argument('--threads', type=int, default=8)
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--only-missing', action='store_true')
    ap.add_argument('--noindex', action='store_true')
    ap.add_argument('file', nargs='?', help='rollback: the routes backup')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--discord', action='store_true', help='status: message Kenny once everything is deployed')
    ap.add_argument('--prefix', default='sporteka', help='Worker names <prefix>-s00 (main) … <prefix>-sNN')
    ap.add_argument('--skip-prep', action='store_true', help='weekly: no gsc / prepare / astro build (already done)')
    ap.add_argument('--skip-data', action='store_true', help='weekly: keep the search + filter files of the last run')
    ap.add_argument('--until', help='weekly: HH:MM — stop starting new pages / shards after it')
    ap.add_argument('--only', help='weekly: only these shards (comma list)')
    ap.add_argument('--changed', action='store_true', help='products only when their source data changed')
    ap.add_argument('--daily', action='store_true', help='weekly: the daily price run (no new paths, no search / filter data, a new build alone does not re-render products)')
    ap.add_argument('--texts', action='store_true', help='weekly: only the first page of every listing (texts changed)')
    ap.add_argument('--kind', help='render only this kind (product, listing, page, home, sitemap)')
    a = ap.parse_args()
    db = state()
    if a.cmd == 'gsc':
        gsc_fetch(db, a.out)
    elif a.cmd == 'prepare':
        prepare(db)
    elif a.cmd == 'paths':
        cnt = {}
        for _, k in all_paths():
            cnt[k] = cnt.get(k, 0) + 1
        print(cnt, sum(cnt.values()), '+', len(client_files()), 'static files')
    elif a.cmd == 'plan':
        plan(db, a.force)
        new, gone = sync_paths(db)
        rows = db.execute('SELECT shard, COUNT(*) FROM files GROUP BY shard ORDER BY shard').fetchall()
        for s, n in rows:
            pf = [p for (p,) in db.execute('SELECT prefix FROM shards WHERE shard = ? ORDER BY prefix', (s,))]
            print(f'  {s}: {n:6d} pages  {len(pf)} prefixes  {" ".join(pf[:12])}{" …" if len(pf) > 12 else ""}')
        print(f'paths +{new} -{gone}')
    elif a.cmd == 'routes':
        for s, p in db.execute('SELECT shard, prefix FROM shards ORDER BY shard, prefix'):
            print(f'sporteka-{s} sporteka.cz/{p}*')
    elif a.cmd == 'render':
        render(db, a.shard or MAIN, a.limit, a.threads, a.only_missing, a.kind, a.changed)
    elif a.cmd == 'search':
        build_search(db, a.threads)
    elif a.cmd == 'filters':
        build_filters(db, a.threads)
    elif a.cmd == 'deploy':
        deploy(db, a.shard or MAIN, a.worker, a.noindex)
    elif a.cmd == 'cutover':
        cutover(db, a.apply, a.only.split(',') if a.only else None)
    elif a.cmd == 'rollback':
        rollback(a.file)
    elif a.cmd == 'parity':
        parity(db, a.limit or 0, a.only.split(',') if a.only else None)
    elif a.cmd == 'status':
        status(db, a.discord)
    elif a.cmd == 'weekly':
        weekly(db, a.threads, a.prefix, a.noindex, a.only.split(',') if a.only else None, a.skip_prep, a.skip_data, a.until or '', a.texts, a.daily)


if __name__ == '__main__':
    main()
