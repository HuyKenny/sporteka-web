#!/usr/bin/env python3
"""sporteka.cz — read-only site audit (stdlib only, gentle: ~5 requests/s).

Samples sitemap URLs (indexable products, categories, brands, facet landings, pages) plus noindex products from the local
live copy, then checks status codes, redirect chains, title/H1/canonical/robots, JSON-LD validity, duplicate titles,
sitemap × noindex consistency, a few /go/ exits, security headers and robots.txt. Writes a Markdown report.

    python3 -I scripts/audit-web.py [--n 1200] [--out reports/sporteka/audit-YYYY-MM-DD.md]
"""
import argparse
import collections
import concurrent.futures as cf
import datetime
import gzip
import json
import random
import re
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
BASE = 'https://sporteka.cz'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(NoRedirect)
_last = [0.0]


def fetch(url, method='GET', hops=0, timeout=25):
    """One request without following redirects → (status, headers, body, location)."""
    gap = 0.2 - (time.time() - _last[0])
    if gap > 0:
        time.sleep(gap)
    _last[0] = time.time()
    req = urllib.request.Request(url, method=method, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip', 'Accept-Language': 'cs'})
    try:
        r = OPENER.open(req, timeout=timeout)
        body = r.read() if method == 'GET' else b''
        if r.headers.get('content-encoding') == 'gzip':
            body = gzip.decompress(body)
        return r.status, r.headers, body, None
    except urllib.error.HTTPError as e:
        body = e.read() if method == 'GET' else b''
        try:
            if e.headers.get('content-encoding') == 'gzip':
                body = gzip.decompress(body)
        except Exception:
            pass
        return e.code, e.headers, body, e.headers.get('location')
    except Exception as e:  # noqa: BLE001
        return 0, {}, str(e).encode(), None


def locs(xml):
    return re.findall(r'<loc>([^<]+)</loc>', xml.decode('utf-8', 'replace'))


def page_info(html):
    h = html.decode('utf-8', 'replace')
    t = re.search(r'<title>([^<]*)</title>', h)
    can = re.search(r'<link rel="canonical" href="([^"]*)"', h)
    rob = re.search(r'<meta name="robots" content="([^"]*)"', h)
    ld = []
    bad_ld = 0
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', h, re.S):
        try:
            j = json.loads(m.group(1))
            ld.append(j)
        except Exception:  # noqa: BLE001
            bad_ld += 1
    types = set()
    for j in ld:
        for n in (j.get('@graph', [j]) if isinstance(j, dict) else j):
            if isinstance(n, dict):
                tt = n.get('@type')
                types.update(tt if isinstance(tt, list) else [tt])
    return {'title': t.group(1).strip() if t else '', 'h1': len(re.findall(r'<h1[ >]', h)), 'canonical': can.group(1) if can else '',
            'robots': rob.group(1) if rob else '', 'bad_ld': bad_ld, 'types': types, 'bytes': len(html),
            'http_img': len(re.findall(r'(?:src|href)="http://', h))}


def check(url):
    st, hd, body, loc = fetch(url)
    out = {'url': url, 'status': st, 'loc': loc, 'ms': 0}
    if st == 200:
        out.update(page_info(body))
        out['cache'] = hd.get('x-spt-page-cache', '')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=1200)
    ap.add_argument('--out', default=str(APP.parent.parent / 'reports/sporteka' / f'audit-{datetime.date.today()}.md'))
    a = ap.parse_args()
    random.seed(7)
    problems = collections.defaultdict(list)
    st, hd, body, _ = fetch(BASE + '/sitemap_index.xml')
    if st != 200:
        raise SystemExit(f'sitemap_index {st}')
    files = locs(body)
    sm = {'product': [], 'category': [], 'brand': [], 'page': [], 'facet': []}
    sizes = {}
    for f in files:
        s2, _, b2, _ = fetch(f)
        if s2 != 200:
            problems['sitemap file not 200'].append(f'{f} → {s2}')
            continue
        u = locs(b2)
        sizes[f.rsplit('/', 1)[-1]] = len(u)
        key = 'product' if 'product-sitemap' in f else 'category' if 'category' in f else 'brand' if 'brand' in f else 'page' if 'page-sitemap' in f else 'facet'
        sm[key] += u
    total = sum(len(v) for v in sm.values())
    sample = []
    per = {'product': 0.55, 'category': 0.15, 'brand': 0.1, 'page': 0.05, 'facet': 0.15}
    for k, v in sm.items():
        n = min(len(v), max(5, int(a.n * per[k]))) if v else 0
        sample += random.sample(v, n)
    # noindex products (not in sitemap) must answer 200 with robots noindex
    noidx = []
    live = APP / 'data/live-production.db'
    if live.exists():
        c = sqlite3.connect(f'file:{live}?mode=ro', uri=True)
        noidx = [f'{BASE}/{s}/' for s, in c.execute("SELECT slug FROM products WHERE status='publish' AND noindex=1 ORDER BY RANDOM() LIMIT 60")]
        retired = [f'{BASE}/{s}/' for s, in c.execute("SELECT from_path FROM redirects ORDER BY RANDOM() LIMIT 25")] if False else []
        redir = [r for r in c.execute('SELECT from_path, to_path FROM redirects ORDER BY RANDOM() LIMIT 25')]
        c.close()
    else:
        redir = []
    urls = [BASE + '/'] + sample + noidx
    print(f'sitemap URLs {total} (files {len(files)}), checking {len(urls)}…', flush=True)
    res = []
    with cf.ThreadPoolExecutor(2) as ex:
        for i, r in enumerate(ex.map(check, urls)):
            res.append(r)
            if i % 200 == 0:
                print(f'  {i}/{len(urls)}', flush=True)
    titles = collections.defaultdict(list)
    insmap = set(sample)
    for r in res:
        u, s = r['url'], r['status']
        if s != 200:
            if s in (301, 302, 308):
                problems['redirect from sitemap URL'].append(f"{u} → {s} {r['loc']}") if u in insmap else None
            else:
                problems[f'HTTP {s}'].append(u)
            continue
        if not r['title']:
            problems['no <title>'].append(u)
        if r['h1'] != 1:
            problems[f'H1 count {r["h1"]}'].append(u)
        rb = r['robots']
        if u in insmap and 'noindex' in rb:
            problems['in sitemap but noindex'].append(u)
        if u not in insmap and u in set(noidx) and 'noindex' not in rb:
            problems['noindex product without robots noindex'].append(u)
        if 'noindex' not in rb and r['canonical'] and r['canonical'].rstrip('/') != u.rstrip('/'):
            problems['canonical differs from URL'].append(f"{u} → {r['canonical']}")
        if 'noindex' not in rb and not r['canonical']:
            problems['indexable page without canonical'].append(u)
        if r['bad_ld']:
            problems['broken JSON-LD'].append(u)
        if r['http_img']:
            problems['http:// resources (mixed content)'].append(u)
        if u in insmap and '/znacka/' not in u and u.count('/') == 4 and r['title']:
            titles[r['title']].append(u)
    for t, us in titles.items():
        if len(us) > 1:
            problems['duplicate title'].append(f'{t[:70]} ×{len(us)}: {us[0]}')
    # product pages: Product schema
    prod = [r for r in res if r['status'] == 200 and r['url'] in set(sm['product'])]
    noprod = [r['url'] for r in prod if 'Product' not in r['types']]
    if noprod:
        problems['product page without Product JSON-LD'] += noprod[:20]
    # redirects table sample
    for fp, tp in redir:
        s, h, _, loc = fetch(BASE + fp)
        if s not in (301, 308) or not loc or urllib.parse.urlparse(loc).path != tp:
            problems['redirect table entry not served'].append(f'{fp} → {s} {loc} (want {tp})')
    # /go/ exits from a product page
    goproblems = []
    if prod:
        s, h, body, _ = fetch(prod[0]['url'])
        gos = list(dict.fromkeys(re.findall(r'href="(/go/[^"]+)"', body.decode('utf-8', 'replace'))))[:4]
        for g in gos:
            s2, h2, _, loc = fetch(BASE + g)
            goproblems.append(f'{g[:60]} → {s2} {(loc or "")[:70]}')
    # headers + robots
    st, hd, body, _ = fetch(BASE + '/')
    need = ['strict-transport-security', 'content-security-policy', 'x-frame-options', 'x-content-type-options', 'referrer-policy', 'permissions-policy']
    missing = [h for h in need if h not in {k.lower() for k in hd.keys()}]
    rs, _, rb, _ = fetch(BASE + '/robots.txt')
    # fake-bot matrix (what a spoofed Googlebot UA sees)
    matrix = []
    for ua in ['Googlebot/2.1 (+http://www.google.com/bot.html)', 'AhrefsBot/7.0', 'GPTBot/1.0', 'python-requests/2.31', 'curl/8.5.0', UA]:
        req = urllib.request.Request(BASE + '/stany/', headers={'User-Agent': ua})
        try:
            code = OPENER.open(req, timeout=20).status
        except urllib.error.HTTPError as e:
            code = e.code
        matrix.append((ua[:48], code))
    lines = [f'# sporteka.cz — audit {datetime.date.today()}', '',
             f'- Sitemap: {len(files)} files, {total} URLs ({", ".join(f"{k} {len(v)}" for k, v in sm.items())}); largest file {max(sizes.values()) if sizes else 0} URLs',
             f'- Checked pages: {len(urls)} (sample of sitemap + {len(noidx)} noindex products), statuses: {dict(collections.Counter(r["status"] for r in res))}',
             f'- Page cache HIT share (sample): {sum(1 for r in res if r.get("cache") == "HIT") / max(1, len(res)):.0%}',
             f'- robots.txt: HTTP {rs}', f'- Missing security headers on /: {missing or "none"}', '', '## Findings', '']
    if not problems:
        lines.append('No problems found in the sample.')
    for k, v in sorted(problems.items(), key=lambda kv: -len(kv[1])):
        lines.append(f'### {k} ({len(v)})')
        lines += [f'- {x}' for x in v[:12]]
        if len(v) > 12:
            lines.append(f'- … +{len(v) - 12} more')
        lines.append('')
    lines += ['## /go/ exits (first product)', ''] + [f'- {g}' for g in goproblems] + ['', '## User-agent matrix on /stany/', ''] + [f'- `{u}` → {c}' for u, c in matrix]
    Path(a.out).write_text('\n'.join(lines) + '\n')
    print(f'report → {a.out}; problem types: {len(problems)}')


if __name__ == '__main__':
    main()
