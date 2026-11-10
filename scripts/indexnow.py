#!/usr/bin/env python3
"""IndexNow (Bing, Seznam.cz, Yandex) for sporteka.cz: URLs from the live sitemap, each at most once per 14 days.

    python3 scripts/indexnow.py [--limit 5000]

Key: INDEXNOW_KEY (public by design — the site serves it as /<key>.txt, checked before sending). State of sent URLs:
data/state/indexnow.json (part of the encrypted "web" state). Google does not support IndexNow.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SITE = 'https://sporteka.cz'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; sporteka-indexnow/1.0)'}
STATE = Path(__file__).resolve().parent.parent / 'data' / 'state' / 'indexnow.json'
AGAIN_DAYS = 14


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.read().decode('utf-8', 'replace')


def main():
    limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else 5000
    key = os.environ.get('INDEXNOW_KEY', '')
    if not key:
        sys.exit('INDEXNOW_KEY missing')
    if get(f'{SITE}/{key}.txt').strip() != key:
        sys.exit(f'{SITE}/<key>.txt does not hold the key — IndexNow would answer 403')
    sent = json.loads(STATE.read_text()) if STATE.exists() else {}
    now = time.time()
    sent = {u: t for u, t in sent.items() if now - t < AGAIN_DAYS * 86400}
    urls = []
    for sm in re.findall(r'<loc>([^<]+)</loc>', get(f'{SITE}/sitemap_index.xml')):
        for u in re.findall(r'<loc>([^<]+)</loc>', get(sm)):
            if u not in sent:
                urls.append(u)
            if len(urls) >= limit:
                break
        if len(urls) >= limit:
            break
    if not urls:
        print('indexnow: nothing new')
        return
    body = json.dumps({'host': 'sporteka.cz', 'key': key, 'keyLocation': f'{SITE}/{key}.txt', 'urlList': urls}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, method='POST',
                                 headers={**UA, 'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            st = r.status
    except urllib.error.HTTPError as e:
        st = e.code
    print(f'indexnow: {len(urls)} URLs → HTTP {st}')
    if st in (200, 202):
        sent.update({u: now for u in urls})
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(json.dumps(sent))
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
