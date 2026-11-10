#!/usr/bin/env python3
"""Audit of the LIVE static sporteka.cz (after the 9. 11. 2026 cutover): does everything work without the SSR Worker + D1?

  python3 scripts/staticky_audit.py [--sample 1500] [--links 3000]

Checks (from Malina, like a visitor):
  1. sitemap URLs (random sample): 200, no X-Robots-Tag noindex, canonical = URL, <title>, <h1>, JSON-LD parses
  2. no link on those pages points at the SSR (/go/, /api/) — those die with the SSR Worker
  3. product buy buttons ("Koupit", sticky bar, offer table) go straight to the shop (https://…)
  4. internal links found on the pages (sample) answer 200 or redirect to a 200
  5. assets (/_astro/, /img/) referenced by the pages load
  6. in-browser search (/_s/) and filters (/_f/) data files exist for the sampled listings
  7. retired products (301 in _redirects) land on a 200; 404 page; www → apex
Exit 1 when anything fails.
"""
import argparse
import concurrent.futures as cf
import json
import random
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

SITE = 'https://sporteka.cz'
UA = {'User-Agent': 'Mozilla/5.0 sporteka-audit MalinaCron'}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPEN = urllib.request.build_opener(NoRedirect)


def get(url, body=True):
    for attempt in range(3):
        try:
            with OPEN.open(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.status, r.headers, (r.read().decode('utf-8', 'replace') if body else '')
        except urllib.error.HTTPError as e:
            return e.code, e.headers, (e.read().decode('utf-8', 'replace') if body else '')
        except Exception:  # noqa: BLE001 — network hiccup: retry
            if attempt == 2:
                return 0, {}, ''


def follow(url, hops=4):
    """Status after redirects (same site only) + the chain."""
    chain = []
    for _ in range(hops):
        st, h, _ = get(url, body=False)
        chain.append(st)
        loc = h.get('location') if h else None
        if st in (301, 302, 307, 308) and loc:
            url = urllib.parse.urljoin(url, loc)
            if not url.startswith(SITE):
                return 200, chain   # leaves the site (shop): fine
            continue
        return st, chain
    return 0, chain


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sample', type=int, default=1500)
    ap.add_argument('--links', type=int, default=3000)
    a = ap.parse_args()
    rnd = random.Random(11)
    errors = {}

    def bad(kind, what):
        errors.setdefault(kind, []).append(what)

    # 1. sitemaps
    st, _, idx = get(SITE + '/sitemap_index.xml')
    if st != 200:
        sys.exit(f'sitemap_index.xml: HTTP {st}')
    locs = []
    for sm in re.findall(r'<loc>([^<]+)</loc>', idx):
        s2, _, body = get(sm)
        if s2 != 200:
            bad('sitemap', f'{s2} {sm}')
        locs += re.findall(r'<loc>([^<]+)</loc>', body)
    print(f'sitemaps: {len(locs)} URLs', flush=True)
    sample = rnd.sample(locs, min(a.sample, len(locs)))
    if SITE + '/' not in sample:
        sample.append(SITE + '/')

    links, assets, listings = set(), set(), set()
    buy = {'direct': 0, 'go': 0}

    def page(u):
        return u, get(u)

    with cf.ThreadPoolExecutor(8) as ex:
        for u, (st, h, html) in ex.map(page, sample):
            p = urllib.parse.urlsplit(u).path
            if st != 200:
                bad('page status', f'{st} {p}')
                continue
            if 'noindex' in (h.get('x-robots-tag') or ''):
                bad('noindex header', p)
            if re.search(r'<meta name="robots" content="[^"]*noindex', html):
                bad('noindex meta', p)
            can = re.findall(r'<link rel="canonical" href="([^"]+)"', html)
            if can != [u]:
                bad('canonical', f'{p} → {can}')
            if not re.search(r'<title>[^<]{5,}</title>', html):
                bad('title', p)
            if not re.search(r'<h1[\s>]', html):
                bad('h1', p)
            for js in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
                try:
                    json.loads(js)
                except ValueError:
                    bad('json-ld', p)
            for href in re.findall(r'(?:href|src|action|data-menu)="([^"]+)"', html):
                if href.startswith(('/go/', '/api/')) or href.startswith((SITE + '/go/', SITE + '/api/')):
                    bad('SSR link', f'{p} → {href[:80]}')
                elif href.startswith(('/_astro/', '/img/')):
                    assets.add(href)
                elif href.startswith('/') and not href.startswith('//'):
                    links.add(href.split('#')[0])
            for tag in re.findall(r'<a [^>]*rel="[^"]*sponsored[^"]*"[^>]*>', html):
                href = re.search(r'href="([^"]*)"', tag).group(1)
                if href.startswith('https://'):
                    buy['direct'] += 1
                else:
                    buy['go'] += 1
            if 'data-filtry' in html:
                listings.add(p)
    print(f'pages: {len(sample)} checked; buy links direct {buy["direct"]}, via /go/ {buy["go"]}', flush=True)

    # 4. internal links + 5. assets
    lk = rnd.sample(sorted(links), min(a.links, len(links)))
    with cf.ThreadPoolExecutor(8) as ex:
        for href, (st, chain) in zip(lk, ex.map(lambda x: follow(SITE + x), lk)):
            if st != 200:
                bad('internal link', f'{chain} {href}')
        # /img/ (sporteka-img Worker, R2 only): 302 = the shop's original (no thumbnail yet / not resizable) — fine;
        # 404 = the shop deleted the picture (not a static-site fault, reported apart)
        gone = 0
        for href, (st, chain) in zip(sorted(assets), ex.map(lambda x: follow(SITE + x), sorted(assets))):
            if st == 404 and href.startswith('/img/'):
                gone += 1
            elif st != 200:
                bad('asset', f'{chain} {href}')
    print(f'internal links: {len(lk)} of {len(links)} checked; assets: {len(assets)} ({gone} shop pictures gone)', flush=True)

    # retired products / renamed categories: _redirects + stub pages must land on a 200
    sys.path.insert(0, __file__.rsplit('/', 1)[0])
    import staticky  # noqa: PLC0415
    db = staticky.state()
    rules, _ = staticky.redirect_plan(staticky.shard_map(db))
    rr = [x for lst in rules.values() for x in lst if ':' not in x[0] and '*' not in x[0]]
    rr = rnd.sample(rr, min(60, len(rr)))
    stubs = [p for (p,) in db.execute("SELECT path FROM files WHERE kind = 'stub' AND status = 200 ORDER BY random() LIMIT 30")]
    with cf.ThreadPoolExecutor(8) as ex:
        for (frm, to, code), (st, chain) in zip(rr, ex.map(lambda x: follow(SITE + x[0]), rr)):
            if st != 200 or chain[0] not in (301, 302, 308):
                bad('redirect', f'{chain} {frm} → {to}')
        for p, (st, _, html) in zip(stubs, ex.map(lambda x: get(SITE + x), stubs)):
            to = re.search(r'url=([^"]+)"', html)
            if st != 200 or not to or follow(SITE + to.group(1))[0] != 200:
                bad('retired stub', f'{st} {p}')
    print(f'redirects: {len(rr)} rules, {len(stubs)} stub pages', flush=True)

    # 6. search + filters
    for path in ('/_s/n.json', '/_s/t/bo.json', '/_s/t/ny.json'):
        st, _, body = get(SITE + path)
        if st != 200 or not body.strip().startswith(('[', '{')):
            bad('search data', f'{st} {path}')
    st, _, body = get(SITE + '/_s/t/bo.json')
    try:
        word = json.loads(body)[0][0]
        st, _, body = get(SITE + f'/_s/w/{word}.json')
        if st != 200 or not json.loads(body):
            bad('search data', f'{st} /_s/w/{word}.json')
    except (ValueError, IndexError, TypeError):
        bad('search data', 'bo.json unreadable')
    fl = 0
    for p in sorted(listings)[:60]:
        base = re.sub(r'page/\d+/$', '', p)
        m = re.match(r'^/znacka/([^/]+)/$', base)
        if m:
            key = f'b/{m.group(1)}'
        elif base == '/slevy/':
            key = 'slevy'
        else:
            slug = base.strip('/')
            st, _, body = get(SITE + f'/_f/l/{slug}.json')
            key = json.loads(body)['k'] if st == 200 else f'c/{slug}'
        st, _, body = get(SITE + f'/_f/{key}/a.json')
        fl += 1
        if st != 200:
            bad('filter data', f'{st} /_f/{key}/a.json ({p})')
    print(f'search ok-check done; filter data for {fl} listings', flush=True)

    # 7. edge cases
    st, _, body = get(SITE + '/neexistuje-audit-xyz/')
    if st != 404 or '<html' not in body:
        bad('404 page', f'HTTP {st}')
    st, h, _ = get('https://www.sporteka.cz/kategorie/?a=1', body=False)
    if st != 301 or (h.get('location') or '') != SITE + '/kategorie/?a=1':
        bad('www', f'{st} {h.get("location") if h else ""}')
    st, h, _ = get('http://sporteka.cz/', body=False)
    if st not in (301, 308) or not (h.get('location') or '').startswith('https://'):
        bad('http→https', f'{st}')

    print()
    if not errors:
        print('AUDIT OK')
        return 0
    for k, v in errors.items():
        print(f'{k}: {len(v)}')
        for x in v[:8]:
            print(f'   {x}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
