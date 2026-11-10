#!/usr/bin/env python3
"""sporteka.cz — Decathlon.cz product feed (Mergado export, 2 GB CSV, ~400 000 SKUs incl. marketplace sellers)
-> data/cj/decathlon.jsonl.gz in the same slim shape as scripts/cj-stahni.py (katalog.py reads both).

    scripts/decathlon-stahni.py            # download + convert (streamed: the SD card has no room for the 2 GB file)
    scripts/decathlon-stahni.py --sample FILE   # convert a local CSV (testing)

Feed URL: credentials/.sporteka-credentials.env DECATHLON_FEED_URL (public HTTP, the old Mergado URL only redirects to an
IP-restricted SFTP). Affiliate (Affilbox): DECATHLON_AFF_QS is appended to every product URL (utm_* + a_box).
Kept: in stock, price > 0, not spare parts, not second-life, not store-only. Seller name and delivery cost go along.
"""
import csv
import gzip
import io
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get("SPT_ROOT") or "/home/kenny/ai")
OUT = APP / "data/cj/decathlon.jsonl.gz"
csv.field_size_limit(10 ** 8)


def creds():
    env = {}
    for line in open(ROOT / "credentials/.sporteka-credentials.env"):
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k] = v.strip().strip("\"'")
    return env


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def sex_of(genders):
    g = (genders or "").upper()
    kids = any(k in g for k in ("JUNIOR", "CHLAPCI", "DÍVKY", "DIVKY", "DĚTI", "DETI", "BATOLATA", "MIMIN"))
    men, women = "MUŽI" in g or "MUZI" in g, "ŽENY" in g or "ZENY" in g
    if kids and not (men or women):
        return "kids"
    if men and women:
        return "unisex"
    return "male" if men else "female" if women else ""


def convert(rows, qs):
    n = kept = 0
    seen = set()
    with gzip.open(OUT.with_suffix(".tmp"), "wt", encoding="utf-8") as out:
        for r in rows:
            n += 1
            if r.get("availability") != "in_stock" or r.get("is_spare_part") == "true" or r.get("is_second_life") == "true" \
                    or r.get("is_sellable_only_in_stores") == "true" or r.get("currency", "CZK") != "CZK":
                continue
            price, ref = num(r.get("price_value_with_taxes")), num(r.get("price_reference_value_with_taxes"))
            url = (r.get("model_url") or "").strip()
            sku = r.get("sku_id") or ""
            if price <= 0 or not url or not sku or sku in seen or not r.get("main_image"):
                continue
            seen.add(sku)
            crumbs = (r.get("breadcrumb_labels") or "").split("|")
            # marketplace sellers sit under "Partnerský prodej - Marketplace|<seller>|…" without a category: use the product nature
            path = " > ".join(crumbs) if crumbs and not crumbs[0].startswith("Partnerský prodej") else (r.get("product_nature_name") or "").title()
            imgs = [u for u in (r.get("product_images") or "").split("|") if u and u != r["main_image"]][:6]
            colors = (r.get("generic_color_names") or "").split("|")
            go = url + ("&" if "?" in url else "?") + qs
            ship = r.get("minimum_delivery_cost_delivery_cost") or ""
            out.write(json.dumps({
                "id": sku, "g": r.get("item_group_id") or sku, "t": r.get("title") or "", "d": (r.get("description") or "")[:900],
                "b": r.get("brand_name") or "", "ean": r.get("ean") or "", "mpn": "", "pt": [path], "gpc": "",
                "p": str(ref if ref > price else price), "cur": "CZK", "sp": str(price) if ref > price else "", "img": r["main_image"], "imgs": imgs,
                "col": colors[0], "size": (r.get("size_label") or "").strip(), "sex": sex_of(r.get("genders")), "age": "", "mat": r.get("main_material") or "",
                "url": url, "go": go, "upd": "", "seller": r.get("seller_name") or "", "ship": ship,
                "sport": r.get("first_sport") or "", "nature": r.get("product_nature_name") or "",
            }, ensure_ascii=False) + "\n")
            kept += 1
    os.replace(OUT.with_suffix(".tmp"), OUT)
    print(f"decathlon: {n} rows read, {kept} kept -> {OUT}", file=sys.stderr)
    return kept


def main():
    env = creds()
    qs = env["DECATHLON_AFF_QS"]
    if "--sample" in sys.argv:
        global OUT
        OUT = APP / "data/dec/sample.jsonl.gz"   # never into data/cj: katalog.py would build from a partial feed
        f = open(sys.argv[sys.argv.index("--sample") + 1], encoding="utf-8", errors="replace", newline="")
        rd = csv.reader(f)
    else:
        req = urllib.request.Request(env["DECATHLON_FEED_URL"], headers={"User-Agent": "SportekaFeed/1.0 (+https://sporteka.cz)"})
        resp = urllib.request.urlopen(req, timeout=300)
        rd = csv.reader(io.TextIOWrapper(resp, encoding="utf-8", errors="replace", newline=""))
    head = next(rd)
    idx = {k: i for i, k in enumerate(head)}

    def rows():
        for r in rd:
            if len(r) == len(head):
                yield {k: r[i] for k, i in idx.items()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    convert(rows(), qs)


if __name__ == "__main__":
    main()
