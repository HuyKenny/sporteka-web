#!/usr/bin/env python3
"""sporteka.cz — download in-stock products of the CJ advertisers in src/data/obchody.json
-> data/cj/<advertiserId>.jsonl.gz (one JSON object per variant, only the fields the catalogue uses).

The CJ Product Search API (GraphQL) serves at most 10 000 rows per query (offset >= 10 000 fails) and the row order
is unstable between pages (offset paging of a 5 000-row band returned only 3 929 distinct ids), so each feed is split
into price bands (lowPrice/highPrice) bisected until a band fits ONE page (<= 1 000 rows); rows are merged by id.
A band that cannot be split further (many items at one price) is paged twice to catch what the first pass missed.

    scripts/cj-stahni.py              # all enabled shops
    scripts/cj-stahni.py 14341702     # only these advertiserIds (or adIds)
    scripts/cj-stahni.py --dry        # only counts per shop, nothing written

The API key and tracking URLs are never printed.
"""
import gzip
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get("SPT_ROOT") or "/home/kenny/ai")
OUT = APP / "data/cj"
BAND_MAX = 1000
PAGE = 1000

FIELDS = ("id itemGroupId title description brand gtin mpn productType googleProductCategory{ id name } "
          "price{ amount currency } salePrice{ amount } imageLink additionalImageLink availability color size gender "
          "ageGroup material link lastUpdated linkCode(pid:\"%s\"){ clickUrl }")


def creds():
    env = {}
    for line in open(ROOT / "credentials/.sporteka-credentials.env"):
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k] = v.strip().strip("\"'")
    return env


ENV = creds()


def gql(query):
    req = urllib.request.Request("https://ads.api.cj.com/query", data=json.dumps({"query": query}).encode(),
                                 headers={"Authorization": "Bearer " + ENV["CJ_API_KEY"], "Content-Type": "application/json"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                x = json.load(r)
            if "errors" in x:
                raise RuntimeError(x["errors"][0].get("message", "")[:200])
            return x["data"]["shoppingProducts"]
        except Exception as e:
            if attempt == 7:
                raise
            # 403 = CJ's short-term rate limit (parallel downloads trip it; it clears after ~30 s)
            time.sleep((30 if "403" in str(e) else 5) * (attempt + 1))
            print(f"  retry {attempt + 1}: {str(e)[:120]}", file=sys.stderr)


def args_for(ad_ids, lo, hi):
    if ad_ids and ad_ids[0].startswith("p:"):            # shop without a Czech feed id: all its products by advertiser id (katalog.py keeps the CZK ones)
        ids = ",".join(f'"{a[2:]}"' for a in ad_ids)
        return f'companyId:"{ENV["CJ_CID"]}", partnerIds:[{ids}], availability:IN_STOCK, lowPrice:{lo}, highPrice:{hi}'
    ids = ",".join(f'"{a}"' for a in ad_ids)
    return f'companyId:"{ENV["CJ_CID"]}", adIds:[{ids}], availability:IN_STOCK, lowPrice:{lo}, highPrice:{hi}'


def count(ad_ids, lo, hi):
    return gql("{ shoppingProducts(%s, limit:1){ totalCount } }" % args_for(ad_ids, lo, hi))["totalCount"]


def bands(ad_ids, lo, hi, n=None):
    """Yield (lo, hi, n) price bands with n <= BAND_MAX. Prices are CZK; bands are inclusive on both ends,
    so consecutive bands use hi and hi + 0.01."""
    n = count(ad_ids, lo, hi) if n is None else n
    if n == 0:
        return
    if n <= BAND_MAX or hi - lo < 0.02:
        yield lo, hi, n
        return
    mid = round((lo + hi) / 2, 2) if hi - lo < 50 else float(int((lo + hi) / 2))
    yield from bands(ad_ids, lo, mid)
    yield from bands(ad_ids, round(mid + 0.01, 2), hi)


def slim(p):
    return {
        "id": p["id"], "g": p.get("itemGroupId") or "", "t": p.get("title") or "", "d": (p.get("description") or "")[:1500],
        "b": p.get("brand") or "", "ean": p.get("gtin") or "", "mpn": p.get("mpn") or "",
        "pt": p.get("productType") or [], "gpc": (p.get("googleProductCategory") or {}).get("name") or "",
        "p": (p.get("price") or {}).get("amount"), "cur": (p.get("price") or {}).get("currency"),
        "sp": (p.get("salePrice") or {}).get("amount"), "img": p.get("imageLink") or "",
        "imgs": (p.get("additionalImageLink") or [])[:6], "col": p.get("color") or "", "size": p.get("size") or "",
        "sex": p.get("gender") or "", "age": p.get("ageGroup") or "", "mat": p.get("material") or "",
        "url": p.get("link") or "", "go": ((p.get("linkCode") or {}).get("clickUrl") or ""), "upd": p.get("lastUpdated") or "",
    }


def fetch_shop(shop, dry):
    ad_ids = shop["adIds"] or ["p:" + shop["advertiserId"]]
    total = count(ad_ids, 0, 10_000_000)
    print(f"{shop['name']}: {total} in stock", file=sys.stderr)
    if dry or not total:
        return total, 0
    got = {}
    # almost everything costs under 200 000 Kč: starting the bisection there saves a dozen empty levels
    split = [(0, 200_000), (200_000.01, 10_000_000)]
    for lo, hi, n in (band for a, z in split for band in bands(ad_ids, a, z)):
        for _ in range(1 if n <= PAGE else 2):
            off = 0
            while off < n:
                d = gql("{ shoppingProducts(%s, offset:%d, limit:%d){ count resultList{ %s } } }"
                        % (args_for(ad_ids, lo, hi), off, PAGE, FIELDS % ENV["CJ_PID"]))
                for p in d["resultList"]:
                    got[p["id"]] = slim(p)
                if d["count"] < PAGE:
                    break
                off += d["count"]
        print(f"  {lo:>10}–{hi:<10} {n:6}  merged {len(got)}", file=sys.stderr)
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = OUT / f".{shop['advertiserId']}.jsonl.gz"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        for p in got.values():
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    os.replace(tmp, OUT / f"{shop['advertiserId']}.jsonl.gz")
    return total, len(got)


def main():
    dry = "--dry" in sys.argv
    only = {a for a in sys.argv[1:] if not a.startswith("--")}
    shops = [s for s in json.load(open(APP / "src/data/obchody.json"))["shops"]
             if s.get("enabled") and not s.get("source") and (not only or s["advertiserId"] in only or set(s["adIds"]) & only)]
    # stalest file first: when a run is cut short (GitHub Actions step limit), the next run continues with the shops
    # that were not refreshed, instead of always redoing the same ones (a shop without a file goes first)
    def age(s):
        f = OUT / f"{s['advertiserId']}.jsonl.gz"
        return f.stat().st_mtime if f.exists() else 0
    shops.sort(key=age)
    summary = []
    for s in shops:
        try:
            summary.append((s["name"], *fetch_shop(s, dry)))
        except Exception as e:
            print(f"{s['name']}: FAILED {str(e)[:200]}", file=sys.stderr)
            summary.append((s["name"], -1, 0))
    for name, total, saved in summary:
        print(f"{name:28} {total:8} {saved:8}")


if __name__ == "__main__":
    main()
