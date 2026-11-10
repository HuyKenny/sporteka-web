#!/usr/bin/env python3
"""sporteka.cz — Allegro.cz (CJ advertiser 6464420, 7.5 million offers) → only the sport brands that Allegro carries in a manageable number.

    scripts/cj-allegro.py [--dry]         # → data/cj/6464420.jsonl.gz (same slim shape as cj-stahni.py)

CJ filters by keyword only, so for each of our brands (most frequent first, from the live catalogue) the keyword query is run, brands with
BRAND_MIN ≤ offers ≤ BRAND_MAX are downloaded (price bands as in cj-stahni.py) and only exact brand matches in CZK are kept.
Big generic brands (Nike, Adidas …) are skipped on purpose: they would drown the catalogue; marketplace data is noisy anyway.
"""
import gzip
import importlib.util
import json
import os
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("cj", APP / "scripts/cj-stahni.py")
cj = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cj)
ADV = "6464420"
BRAND_MIN, BRAND_MAX, TOP_BRANDS, TOTAL_MAX = 8, 6000, 220, 120_000
fold = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", (s or "").lower()).encode("ascii", "ignore").decode())


def brands():
    # the brand list comes from the live copy of the database: production first, else whatever state this runner restored (staging test)
    live = next((f for f in (APP / "data/live-production.db", APP / "data/live-staging.db") if f.exists()), None)
    if not live:
        print("no live database copy here: Allegro brand list skipped")
        return []
    db = sqlite3.connect(f"file:{live}?mode=ro", uri=True)
    return [r[0] for r in db.execute("SELECT name FROM brands WHERE slug != 'ostatni' ORDER BY count DESC LIMIT ?", (TOP_BRANDS,))]


def main():
    dry = "--dry" in sys.argv
    orig = cj.args_for
    ids = ["p:" + ADV]
    got = {}
    for b in brands():
        if len(b) < 3:
            continue
        cj.args_for = lambda a, lo, hi, kw=b: orig(a, lo, hi) + f', keywords:{json.dumps([kw], ensure_ascii=False)}'
        try:
            total = cj.count(ids, 0, 10_000_000)
        except Exception as e:
            print(f"{b}: count failed {str(e)[:80]}", file=sys.stderr)
            continue
        if total < BRAND_MIN or total > BRAND_MAX:
            print(f"{b}: {total} → skipped", file=sys.stderr)
            continue
        if dry:
            print(f"{b}: {total}", file=sys.stderr)
            continue
        kept = 0
        for lo, hi, n in (band for a, z in [(0, 200_000), (200_000.01, 10_000_000)] for band in cj.bands(ids, a, z)):
            off = 0
            while off < n:
                d = cj.gql("{ shoppingProducts(%s, offset:%d, limit:%d){ count resultList{ %s } } }"
                           % (cj.args_for(ids, lo, hi), off, cj.PAGE, cj.FIELDS % cj.ENV["CJ_PID"]))
                for p in d["resultList"]:
                    r = cj.slim(p)
                    if fold(r["b"]) == fold(b) and r["cur"] == "CZK" and r["id"] not in got:
                        got[r["id"]] = r
                        kept += 1
                if d["count"] < cj.PAGE:
                    break
                off += d["count"]
        print(f"{b}: {total} offers, kept {kept} (total {len(got)})", file=sys.stderr, flush=True)
        if len(got) >= TOTAL_MAX:
            break
    cj.args_for = orig
    if dry or not got:
        return
    tmp = cj.OUT / f".{ADV}.jsonl.gz"
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        for p in got.values():
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    os.replace(tmp, cj.OUT / f"{ADV}.jsonl.gz")
    print(f"allegro: {len(got)} offers → {cj.OUT / (ADV + '.jsonl.gz')}", file=sys.stderr)


if __name__ == "__main__":
    main()
