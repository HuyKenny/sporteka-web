#!/usr/bin/env python3
"""sporteka.cz — eHub / AffiliatePort XML product feeds (Google Merchant RSS and Heureka SHOPITEM)
-> data/cj/<shop id>.jsonl.gz in the same slim shape as scripts/cj-stahni.py (katalog.py reads them via obchody.json, source "xml").

    scripts/xml-feedy-stahni.py                 # all shops in data/feedy.json, sequentially
    scripts/xml-feedy-stahni.py eh-6bb9cb0e     # just one shop (id from data/feedy.json)

data/feedy.json (gitignored; feed URLs of Mergado/shopycrm carry tokens):
  feeds[]:        {id, name, domain, url, a_aid, a_bid}  eHub shop: link = click.php?a_aid&a_bid&desturl=<urlencoded product url>
                  (a feed link that already is a click.php / tracking link is kept as is)
  affiliateport[]: {id, name, domain, offer, asset}      tracked links come from the feed itself; the key is read from
                  credentials/.affiliateport-credentials.env (never written to disk elsewhere or logged)
                  dognet[]: {id, name, domain, url, chid}  Dognet partner feeds (Heureka / Google XML, bare product URLs);
                  link = https://go.dognet.com/?chid=<chid>&url=<urlencoded product url> (a feed link that already is a go.dognet.com link is kept)
"enabled": false in a feeds[] entry skips that shop (not sport).
A failed download keeps the previous file (same for a feed that shrank below half of the last run).
"""
import gzip
import os
import json
import re
import sys
import time
import urllib.request
from pathlib import Path
from urllib.parse import quote, unquote, urlparse
from xml.etree import ElementTree as ET

APP = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get("SPT_ROOT") or "/home/kenny/ai")
OUTDIR = APP / "data/cj"
UA = "SportekaFeed/1.0 (+https://sporteka.cz)"
EHUB_CLICK = "https://ehub.cz/system/scripts/click.php?a_aid={aid}&a_bid={bid}&desturl="


def env_file(name):
    env = {}
    for line in open(ROOT / "credentials" / name):
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k] = v.strip().strip("\"'")
    return env


def price_of(s):
    """('1 200,00 CZK') -> (1200.0, 'CZK'); currency '' when the feed gives none (Heureka feeds are CZK)."""
    s = (s or "").strip()
    cur = (re.findall(r"[A-Za-z]{3}", s) or [""])[0].upper()
    n = re.sub(r"[^\d,.]", "", s)
    if "," in n and "." in n:
        n = n.replace(",", "")
    n = n.replace(",", ".")
    try:
        return float(n), cur
    except ValueError:
        return 0.0, cur


def sex_of(v, age=""):
    t = f"{v} {age}".lower()
    if re.search(r"kids|child|d[ěe]t|junior|chlap|d[ií]vk|boy|girl", t):
        return "kids"
    men, women = bool(re.search(r"\bmale\b|p[áa]nsk|mu[žz]|\bmen\b", t)), bool(re.search(r"female|d[áa]msk|[žz]en|women", t))
    if "unisex" in t or (men and women):
        return "unisex"
    return "male" if men else "female" if women else ""


def local(tag):
    return tag.rsplit("}", 1)[-1]


def items(resp):
    """Stream (kind, dict) per product: tags without namespace, repeated tags collected into lists."""
    for _, el in ET.iterparse(resp, events=("end",)):
        t = local(el.tag)
        if t not in ("item", "SHOPITEM", "entry"):
            continue
        d = {}
        for ch in el:
            k = local(ch.tag)
            if k == "PARAM":
                d.setdefault("PARAM", []).append(((ch.findtext("PARAM_NAME") or "").strip().lower(), (ch.findtext("VAL") or "").strip()))
            else:
                d.setdefault(k, []).append((ch.text or "").strip())
        el.clear()
        yield ("heureka" if t == "SHOPITEM" else "google"), d


def one(d, k, default=""):
    v = d.get(k)
    return v[0] if v else default


def sport_filter():
    """Fashion shops (Spartoo): only sport-ish items of brands already in the catalogue (katalog.py's SPORTY regex)."""
    import sqlite3
    sys.path.insert(0, str(APP / "scripts"))
    import kategorie as K
    live = next((APP / 'data' / f for f in ('live-production.db', 'live-staging.db') if (APP / 'data' / f).exists()), None)
    if live is None:                       # first run without any state: nothing to match brands against, take no fashion items
        return lambda rec: False
    db = sqlite3.connect(f"file:{live}?mode=ro", uri=True)
    brands = {re.sub(r"[^a-z0-9]", "", K.fold(n)) for (n,) in db.execute("SELECT name FROM brands")}
    return lambda rec: re.sub(r"[^a-z0-9]", "", K.fold(rec["b"])) in brands and bool(K.SPORTY.search(K.fold(rec["t"] + " " + " ".join(rec["pt"]))))


def convert(shop, resp, link_of):
    keep = sport_filter() if shop.get("sport_only") else None
    seen, n, kept = set(), 0, 0
    tmp = OUTDIR / f"{shop['id']}.tmp"
    with gzip.open(tmp, "wt", encoding="utf-8") as out:
        for kind, d in items(resp):
            n += 1
            if kind == "google":
                pid, title, url, img = one(d, "id"), one(d, "title"), one(d, "link"), one(d, "image_link")
                if one(d, "availability", "in stock").lower().replace("_", " ") not in ("in stock", "instock", "preorder", "backorder"):
                    continue
                price, cur = price_of(one(d, "price"))
                sale, scur = price_of(one(d, "sale_price"))
                if not cur or cur != "CZK" or (sale and scur not in ("", "CZK")):
                    continue
                path = one(d, "product_type") or one(d, "google_product_category")
                rec = {"g": one(d, "item_group_id") or pid, "d": one(d, "description"), "b": one(d, "brand"), "ean": one(d, "gtin"), "mpn": one(d, "mpn"),
                       "gpc": one(d, "google_product_category"), "imgs": d.get("additional_image_link", [])[:6], "col": one(d, "color"), "size": one(d, "size"),
                       "sex": sex_of(one(d, "gender"), one(d, "age_group")), "mat": one(d, "material")}
            else:
                pid, title, url, img = one(d, "ITEM_ID"), one(d, "PRODUCTNAME") or one(d, "PRODUCT"), one(d, "URL"), one(d, "IMGURL")
                price, cur = price_of(one(d, "PRICE_VAT") or one(d, "PRICE"))
                sale = 0.0
                params = {k: v for k, v in d.get("PARAM", [])}
                path = one(d, "CATEGORYTEXT").replace("|", " > ")
                size = next((v for k, v in params.items() if "velikost" in k or k == "size"), "")
                rec = {"g": one(d, "ITEMGROUP_ID") or pid, "d": one(d, "DESCRIPTION"), "b": one(d, "MANUFACTURER"), "ean": one(d, "EAN"), "mpn": one(d, "PRODUCTNO"),
                       "gpc": "", "imgs": d.get("IMGURL_ALTERNATIVE", [])[:6], "col": next((v for k, v in params.items() if "barva" in k or "color" in k), ""),
                       "size": size, "sex": sex_of(next((v for k, v in params.items() if "pohlav" in k or "gender" in k), "")),
                       "mat": next((v for k, v in params.items() if "materi" in k), "")}
            if not (pid and title and url and img and price > 0) or pid in seen:
                continue
            seen.add(pid)
            if "productserve.com" in img:                    # Awin image proxy (200 px): the original file sits in its url= parameter
                m_img = re.search(r"[?&]url=(?:ssl%3A|ssl:)?([^&]+)", img.replace("&amp;", "&"))
                if m_img:
                    img = "https://" + unquote(m_img.group(1))
            plain, go = link_of(url)
            rec.update({"id": pid, "t": title, "d": re.sub(r"<[^>]+>", " ", rec["d"])[:900], "pt": [re.sub(r"\s*[>|/]\s*", " > ", path).strip()],
                        "p": str(max(price, sale)), "cur": "CZK", "sp": str(sale) if sale and sale < price else "", "img": img, "age": "", "url": plain, "go": go, "upd": "",
                        "seller": "", "ship": ""})
            if rec["sp"]:
                rec["p"] = str(price)
            if keep and not keep(rec):
                continue
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            kept += 1
    return tmp, n, kept


def run(shop, url, link_of):
    dest = OUTDIR / f"{shop['id']}.jsonl.gz"
    prev = 0
    if dest.exists():
        prev = sum(1 for _ in gzip.open(dest, "rt", encoding="utf-8"))
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as resp:
                tmp, n, kept = convert(shop, resp, link_of)
            break
        except Exception as e:  # network / XML errors: keep the old file
            last = f"{type(e).__name__}: {str(e)[:80]}".replace(url, "<url>")
            time.sleep(5 * (attempt + 1))
    else:
        print(f"{shop['id']} {shop['name']}: FAILED ({last}), keeping the previous file", file=sys.stderr)
        return 0
    if kept == 0 or (prev and kept < prev * 0.5):
        tmp.unlink(missing_ok=True)
        print(f"{shop['id']} {shop['name']}: {kept} of {n} (previous {prev}) — kept the previous file", file=sys.stderr)
        return prev
    tmp.replace(dest)
    print(f"{shop['id']} {shop['name']}: {n} items, {kept} kept", file=sys.stderr)
    return kept


def main():
    cfg = json.load(open(APP / "data/feedy.json"))
    only = set(a for a in sys.argv[1:] if not a.startswith("-"))
    OUTDIR.mkdir(parents=True, exist_ok=True)
    total = 0
    for s in cfg["feeds"]:
        if (only and s["id"] not in only) or (not only and s.get("enabled") is False):
            continue
        pre = EHUB_CLICK.format(aid=s["a_aid"], bid=s["a_bid"])

        def link_of(u, pre=pre):
            u = u.replace("&amp;", "&")
            return (u, u) if "click.php" in u or "tracking." in u else (u, pre + quote(u, safe=""))
        total += run(s, s["url"], link_of)
    ap = [s for s in cfg.get("affiliateport", []) if not only or s["id"] in only]
    if ap:
        key = env_file(".affiliateport-credentials.env")
        key = key.get("AFFILIATEPORT_API_KEY_FULL") or key.get("AFFILIATEPORT_API_KEY")
        if not key:
            print("AffiliatePort: no API key in the credentials file — skipping its feeds (previous files are kept)")
            ap = []
        for s in ap:
            url = f"https://affiliateport.scaletrk.com/api/v2/affiliate/offers/{s['offer']}/assets/{s['asset']}/download?api-key={key}"

            def link_of(u):
                u = u.replace("&amp;", "&")
                m = re.search(r"deep_link=([^&]+)", u)
                return (m.group(1) if m else u, u)
            total += run(s, url, link_of)
    for s in cfg.get("dognet", []):
        if (only and s["id"] not in only) or (not only and s.get("enabled") is False):
            continue

        def link_of(u, chid=s["chid"]):
            u = u.replace("&amp;", "&")
            return (u, u) if "go.dognet.com" in u else (u, f"https://go.dognet.com/?chid={chid}&url=" + quote(u, safe=""))
        total += run(s, s["url"], link_of)
    print(f"total kept: {total}", file=sys.stderr)


if __name__ == "__main__":
    main()
