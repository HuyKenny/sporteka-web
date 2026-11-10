#!/usr/bin/env python3
"""sporteka.cz — warm the image cache of the pages people open first.

    scripts/zahrej-obrazky.py            # home, section pages, the biggest categories, /slevy/ → every /img/ thumbnail on them

The first view of a thumbnail costs 0.3–0.7 s (the Worker fetches + resizes); after that it is served from the edge cache. After a
new catalogue is pushed the popular pages are walked once so that visitors get the cached files. Paced (the image Worker limits cache
misses to 300 / min per IP). Run from bin/sporteka-import.sh after the push.
"""
import concurrent.futures as cf
import re
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
BASE = "https://sporteka.cz"
UA = "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 Chrome/131.0 Mobile Safari/537.36"


def get(path, binary=False):
    req = urllib.request.Request(path if path.startswith("http") else BASE + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read() if binary else r.read().decode("utf-8", "replace")


def main():
    db = sqlite3.connect(f"file:{APP / 'data/live-production.db'}?mode=ro", uri=True)
    pages = ["/", "/slevy/", "/slevy/page/2/", "/obchody/"]
    pages += [f"/{r[0]}/" for r in db.execute("SELECT slug FROM categories WHERE count_total >= 30 ORDER BY count_total DESC LIMIT 70")]
    pages += [f"/znacka/{r[0]}/" for r in db.execute("SELECT slug FROM brands WHERE slug != 'ostatni' ORDER BY count DESC LIMIT 25")]
    urls = []
    for p in pages:
        try:
            html = get(p)
        except Exception as e:
            print("page failed", p, str(e)[:60], file=sys.stderr)
            continue
        urls += re.findall(r'(/img/\d+/[0-9a-f]{16}/[A-Za-z0-9_-]+\.webp)', html)
    urls = list(dict.fromkeys(urls))
    print(f"{len(pages)} pages, {len(urls)} thumbnails", file=sys.stderr)
    ok = bad = 0
    t0 = time.time()

    def one(u):
        try:
            get(u, binary=True)
            return True
        except Exception:
            return False
    with cf.ThreadPoolExecutor(4) as ex:
        for i, r in enumerate(ex.map(one, urls)):
            ok += r
            bad += not r
            if i % 4 == 3:
                time.sleep(1.0)          # ≈ 4 requests/s: stays under the Worker's miss limit
    print(f"warmed {ok}, failed {bad} in {time.time() - t0:.0f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
