#!/usr/bin/env python3
"""sporteka.cz — facet landing pages (table facet_pages) from Marketing Miner demand + the live catalogue.

Called by katalog.py (finalize) on the freshly built next.db, so the landings travel with the normal diff push:

    fasety.generate(db)          # replaces the whole facet_pages table
    python3 scripts/fasety.py [db] [--show N]    # dry run on a database file: prints the landings it would create

A landing = a category + one preset filter (qs) and its own H1 / title / description / intro / second text / FAQ:
  * gender × category      "dámské běžecké boty"          p_pro=damske
  * brand × category       "nike běžecké boty"            znacka=nike
  * colour × category      "černé mikiny"                 p_barva=cerna
  * sale × category        "běžecké boty sleva"           sleva=1
Demand comes from reports/sporteka/kw/kw-all.json (scripts/kw-harvest.py --report): the volumes of every spelling are summed
(diacritics, word order, singular) and the most searched spelling becomes the H1. A landing needs the volume threshold AND enough products.
No slug of an existing category / product / brand is ever reused (that intent already has its page).
"""
import collections
import hashlib
import json
import re
import statistics
import sys
import unicodedata
from pathlib import Path

# tracked copies (the GitHub Actions build has no workspace): kw-all.json = suggestions of our own category / brand names, kw-gap.json = what
# competitors rank for and we do not (scripts/gap-harvest.py); both are {keyword, volume}
KW_FILES = [Path(__file__).resolve().parent.parent / 'src/data/kw/kw-all.json', Path(__file__).resolve().parent.parent / 'src/data/kw/kw-gap.json']
MIN_PRODUCTS = 6
# 11. 11. 2026: from 250 down to 50 searches a month — a landing only becomes indexable with its hand-written text (src/lib/facet-texts.ts)
MIN_VOL = {'gender': 50, 'brand': 50, 'color': 50, 'sale': 100}
MAX_LANDINGS = 1500
HAND_TEXTS = Path(__file__).resolve().parent.parent / 'src/texts/fasety.json'
MIN_RESULT = 150      # fewer landings than this means the keyword files are missing / broken: keep the old table
GENDERS = [('Pánské', 'panske', 'pansk', 'muži'), ('Dámské', 'damske', 'damsk', 'ženy'), ('Dětské', 'detske', 'detsk', 'děti')]
# category name as people type it, when ours differs
ALT = {
    'bezecka-obuv': ['bezecke boty', 'bezecka obuv'], 'trekova-obuv': ['trekove boty', 'turisticke boty', 'trekingove boty', 'outdoorove boty'],
    'sportovni-obuv': ['sportovni boty', 'sportovni obuv'], 'tenisky': ['tenisky', 'volnocasove boty'], 'sportovni-tricka': ['tricka', 'tricko', 'sportovni tricko'],
    'sportovni-kalhoty': ['kalhoty', 'sportovni kalhoty'], 'sportovni-kratasy': ['kratasy', 'sportovni kratasy'], 'mikiny': ['mikiny', 'mikina'],
    'sportovni-bundy': ['bundy', 'bunda'], 'turisticke-batohy': ['turisticke batohy', 'treking batoh'], 'batohy': ['batohy', 'batoh'],
    'mestske-batohy': ['mestske batohy', 'sportovni batohy'], 'termopradlo': ['termopradlo', 'funkcni pradlo'], 'plavky': ['plavky'],
    'lyzarske-bundy': ['lyzarske bundy', 'lyzarska bunda'], 'sportovni-ponozky': ['ponozky', 'sportovni ponozky'], 'cepice-a-celenky': ['cepice', 'ksiltovky'],
    'leginy': ['leginy', 'legíny'], 'teplaky': ['teplaky'], 'sportovni-podprsenky': ['sportovni podprsenky', 'podprsenky'], 'zimni-obuv': ['zimni boty', 'snehule'],
    'zimni-bundy': ['zimni bundy', 'zimni bunda'], 'softshellove-bundy': ['softshellove bundy', 'softshellova bunda'], 'sandaly': ['sandaly'],
    'sjezdove-lyze': ['sjezdove lyze', 'lyze'], 'lyzarske-boty': ['lyzarske boty', 'lyzaky'], 'lyzarske-kalhoty': ['lyzarske kalhoty'], 'lyzarske-rukavice': ['lyzarske rukavice'],
    'lyzarske-helmy': ['lyzarske helmy', 'helma na lyze', 'prilba na lyze'], 'lyzarske-bryle': ['lyzarske bryle', 'bryle na snowboard', 'bryle na lyze'], 'snowboardy': ['snowboardy', 'snowboard'], 'snowboardove-sety': ['snowboard komplet', 'snowboard s vazanim', 'snowboard set'],
    'spaci-pytle': ['spacak', 'spaci pytel', 'spacaky'], 'perove-spacaky': ['perovy spacak', 'perove spacaky'], 'dekove-spacaky': ['dekovy spacak', 'dekovy spaci pytel'], 'detske-spacaky': ['detsky spacak', 'detsky spaci pytel'],
    'vlozky-do-spacaku': ['vlozka do spacaku'], 'rybarske-spacaky': ['rybarsky spacak', 'rybarsky spaci pytel'], 'nahradni-zorniky': ['zorniky do lyzarskych bryli', 'nahradni zorniky'],
    'snowboardove-boty': ['snowboardove boty'], 'bezecke-lyze': ['bezky', 'bezecke lyze'], 'bezecke-boty': ['boty na bezky'], 'lyzarske-kombinezy': ['lyzarske kombinezy', 'lyzarska kombineza'],
    'skialpove-boty': ['skialpove boty'], 'skialpove-lyze': ['skialpove lyze'], 'detske-lyze': ['detske lyze'], 'lyzarske-termopradlo': ['lyzarske termopradlo'], 'lyzarske-hole': ['lyzarske hole', 'hulky na lyze'],
    'kopacky': ['kopacky'], 'sportovni-bryle': ['sportovni bryle', 'slunecni bryle'], 'barefoot-obuv': ['barefoot boty'],
}


def fold(s):
    s = unicodedata.normalize('NFKD', str(s or '').lower())
    return re.sub(r'\s+', ' ', ''.join(c for c in s if not unicodedata.combining(c))).strip()


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', fold(s)).strip('-')


def num(n):
    return f'{int(n):,}'.replace(',', ' ')


def load_kw():
    exact = {}    # the same spelling in several files (own suggestions + competitor gap) is one demand, not two: the larger volume wins
    for f in KW_FILES:
        if f.exists():
            for r in json.load(open(f)):
                k = r['keyword'].lower().strip()
                exact[k] = max(exact.get(k, 0), r['volume'] or 0)
    idx, orig = collections.defaultdict(int), {}
    for kw, vol in exact.items():
        k = fold(kw)
        idx[k] += vol                                # spellings with / without diacritics of one phrase add up
        diac = kw != k                               # the spelling with diacritics wins for the H1, whatever its own volume
        if k not in orig or (diac and not orig[k][2]) or (diac == orig[k][2] and vol > orig[k][1]):
            orig[k] = (kw, vol, diac)
    return idx, orig


def singulars(n):
    out = {n}
    w = n.split(' ')
    last = w[-1]
    if last.endswith('ky'):
        out.add(' '.join(w[:-1] + [last[:-2] + 'ka']))
    if last.endswith('y'):
        out.add(' '.join(w[:-1] + [last[:-1] + 'a']))
    if last.endswith('e') and len(last) > 4:
        out.add(' '.join(w[:-1] + [last[:-1] + 'a']))
    return out


def cap(s):
    return s[:1].upper() + s[1:]


def best(idx, orig, phrases):
    """sum of the volumes of all spellings + the most searched spelling (original diacritics)."""
    tot, top = 0, ('', 0)
    for p in phrases:
        v = idx.get(p, 0)
        tot += v
        if v > top[1]:
            top = (orig.get(p, (p, v))[0], v)
    return tot, top[0]


def generate(db, show=0):
    idx, orig = load_kw()
    if not idx:
        raise SystemExit('fasety: no keyword file — refusing to rebuild the landings from nothing')
    # landings that already have a hand-written text keep their slug and H1 (the text was written for them, the page is indexed)
    hand = set(json.load(open(HAND_TEXTS))) if HAND_TEXTS.exists() else set()
    prev = {(r[1], r[2]): (r[0], r[3]) for r in db.execute('SELECT slug, base_slug, qs, h1 FROM facet_pages') if r[0] in hand}
    prev_rows = {r[1]: r for r in db.execute('SELECT * FROM facet_pages') if r[1] in hand}
    taken = {r[0] for r in db.execute('SELECT slug FROM slugs')} | {r[0] for r in db.execute('SELECT slug FROM categories')} | {r[0] for r in db.execute('SELECT slug FROM brands')}
    cats = db.execute('SELECT id, slug, name, count_total FROM categories WHERE count_total >= ? ORDER BY count_total DESC', (MIN_PRODUCTS,)).fetchall()
    out, used = [], set()

    def names_of(slug, name):
        base = {fold(re.sub(r'\s*\(.*?\)', '', name))} | set(ALT.get(slug, []))
        full = set()
        for n in base:
            full |= singulars(n)
        return {n for n in full if len(n) >= 4}

    def add(kind, cid, cslug, cname, qs, phrases, extra_filter, label):
        vol, h1 = best(idx, orig, phrases)
        if vol < MIN_VOL[kind] or not h1:
            return
        if kind == 'gender':        # "Dámská mikina" reads better than "Mikina dámská" when it is searched at least half as often
            first = max(((idx.get(p, 0), orig.get(p, (p,))[0]) for p in phrases if re.match(r'(pansk|damsk|detsk)', p) and p in orig), default=(0, ''))
            if first[0] * 2 >= idx.get(fold(h1), 0):
                h1 = first[1]
        if kind == 'brand':          # brand written the way the brand writes it
            h1 = re.sub(re.escape(fold(label)), label, h1, flags=re.I)
        slug = slugify(h1)
        if (cslug, qs) in prev:
            slug, h1 = prev[(cslug, qs)]
        if not slug or slug in taken or slug in used:
            return
        sql, args = extra_filter
        row = db.execute(f"""SELECT COUNT(*), MIN(p.min_price), MAX(p.min_price) FROM cat_products cp JOIN products p ON p.id = cp.product_id
                             WHERE cp.cat_id = ? AND p.status = 'publish' {sql}""", (cid, *args)).fetchone()
        n = row[0]
        if n < MIN_PRODUCTS:
            return
        used.add(slug)
        out.append(dict(slug=slug, cid=cid, cslug=cslug, cname=cname, qs=qs, h1=cap(h1), vol=vol, n=n, kind=kind, label=label, sql=sql, args=args))

    for cid, cslug, cname, cnt in cats:
        ns = names_of(cslug, cname)
        for gl, gs, stem, who in GENDERS:
            ph = [f'{stem}{e} {n}' for e in 'eay' for n in ns] + [f'{n} {stem}{e}' for e in 'eay' for n in ns]
            ph += [fold(f'{x}') for x in ph if x != fold(x)]
            add('gender', cid, cslug, cname, f'p_pro={gs}', list(dict.fromkeys(ph)), ("AND EXISTS (SELECT 1 FROM product_params q WHERE q.product_id = p.id AND q.key = 'pro' AND q.value = ?)", (gl,)), gl)
        # brands present in this category
        if cnt >= 20:
            for bid, bname, bslug, bn in db.execute("""SELECT b.id, b.name, b.slug, COUNT(*) FROM cat_products cp JOIN products p ON p.id = cp.product_id JOIN brands b ON b.id = p.brand_id
                                                       WHERE cp.cat_id = ? AND p.status = 'publish' AND b.slug != 'ostatni' GROUP BY b.id HAVING COUNT(*) >= ? ORDER BY 4 DESC LIMIT 40""", (cid, MIN_PRODUCTS)):
                bf = fold(bname)
                ph = [f'{bf} {n}' for n in ns] + [f'{n} {bf}' for n in ns]
                add('brand', cid, cslug, cname, f'znacka={bslug}', ph, ('AND p.brand_id = ?', (bid,)), bname)
        # sale
        ph = [f'{n} {w}' for n in ns for w in ('sleva', 'slevy', 'akce', 'vyprodej', 'levne', 've sleve', 'v akci')]
        add('sale', cid, cslug, cname, 'sleva=1', ph, ('AND p.disc_pct >= 10', ()), 've slevě')
        # colour (the keyword has the colour as an adjective: "černá mikina")
        for (cv,) in db.execute("SELECT DISTINCT q.value FROM product_params q WHERE q.key = 'barva' AND q.product_id IN (SELECT product_id FROM cat_products WHERE cat_id = ?) LIMIT 20", (cid,)):
            stem = fold(cv)[:-1] if len(cv) > 4 else fold(cv)
            ph = [k for k in idx if idx[k] >= 100 and any(re.search(rf'(^| ){re.escape(n)}( |$)', k) for n in ns) and re.search(rf'(^| ){re.escape(stem)}\w{{0,3}}( |$)', k)]
            add('color', cid, cslug, cname, f'p_barva={slugify(cv)}', ph, ("AND EXISTS (SELECT 1 FROM product_params q WHERE q.product_id = p.id AND q.key = 'barva' AND q.value = ?)", (cv,)), cv)

    # a hand-written text was written for a candidate of scripts/fasety-export.py (src/data/kw/fasety-kandidati.json: slug, h1,
    # base category, qs, volume). Some of them the demand matching above never finds (brand × parent category: "Alpine Pro
    # bunda" in sportovni-bundy) — such a text still gets its page when the base category has enough products for the filter.
    cand_file = Path(__file__).resolve().parent.parent / 'src/data/kw/fasety-kandidati.json'
    cands = json.load(open(cand_file)) if cand_file.exists() else []
    cat_by_slug = {r[1]: r for r in db.execute('SELECT id, slug, name FROM categories')}
    gender = {gs: gl for gl, gs, _, _ in GENDERS}
    for x in cands:
        slug = x['slug']
        if slug not in hand or slug in used or slug in taken or x.get('base') not in cat_by_slug:
            continue
        cid, cslug, cname = cat_by_slug[x['base']]
        key, _, val = x['qs'].partition('=')
        if key == 'znacka':
            b = db.execute('SELECT id, name FROM brands WHERE slug = ?', (val,)).fetchone()
            if not b:
                continue
            kind, flt, label = 'brand', ('AND p.brand_id = ?', (b[0],)), b[1]
        elif key == 'p_pro' and val in gender:
            kind, label = 'gender', gender[val]
            flt = ("AND EXISTS (SELECT 1 FROM product_params q WHERE q.product_id = p.id AND q.key = 'pro' AND q.value = ?)", (label,))
        elif key == 'p_barva':
            cv = next((v for (v,) in db.execute("SELECT DISTINCT q.value FROM product_params q WHERE q.key = 'barva' AND q.product_id IN "
                                                 "(SELECT product_id FROM cat_products WHERE cat_id = ?)", (cid,)) if slugify(v) == val), None)
            if not cv:
                continue
            kind, label = 'color', cv
            flt = ("AND EXISTS (SELECT 1 FROM product_params q WHERE q.product_id = p.id AND q.key = 'barva' AND q.value = ?)", (cv,))
        elif key == 'sleva':
            kind, flt, label = 'sale', ('AND p.disc_pct >= 10', ()), 've slevě'
        else:
            continue
        n = db.execute(f"SELECT COUNT(*) FROM cat_products cp JOIN products p ON p.id = cp.product_id WHERE cp.cat_id = ? AND p.status = 'publish' {flt[0]}",
                       (cid, *flt[1])).fetchone()[0]
        if n < MIN_PRODUCTS:
            continue
        h1 = prev_rows[slug][4] if slug in prev_rows else x['h1']
        used.add(slug)
        out.append(dict(slug=slug, cid=cid, cslug=cslug, cname=cname, qs=x['qs'], h1=cap(h1), vol=int(x.get('vol') or 0), n=n, kind=kind, label=label, sql=flt[0], args=flt[1]))

    out.sort(key=lambda r: (r['slug'] not in hand, -r['vol']))   # landings with a text never fall off the cap
    out = out[:MAX_LANDINGS]
    missing = sorted(hand - {r['slug'] for r in out} - set(prev_rows))
    print(f'fasety: hand-text landings without a page: {len(missing)} {missing[:20]}', file=sys.stderr)
    if len(out) < MIN_RESULT:   # never replace the table by (almost) nothing: the keyword files are missing or broken
        raise SystemExit(f'fasety: only {len(out)} landings (< {MIN_RESULT}) — keyword files {[str(f) for f in KW_FILES]} missing?')
    db.execute('DELETE FROM facet_pages')
    rows = []
    ids = set()
    new_slugs = {r['slug'] for r in out}
    for r in out:
        t = texts(db, r)
        fid = 1_000_000 + int(hashlib.md5(r['slug'].encode()).hexdigest()[:6], 16)
        while fid in ids:
            fid += 1
        ids.add(fid)
        rows.append((fid, r['slug'], r['cslug'], r['qs'], r['h1'], t['title'], t['desc'], t['intro'], t['second'], json.dumps(t['faq'], ensure_ascii=False), r['h1'].lower(), r['vol'], MIN_PRODUCTS, r['n'], 0, '2026-11-01'))
    kept = [tuple(r) for sl, r in prev_rows.items() if sl not in new_slugs and sl not in {x[1] for x in rows}]
    if kept:   # a text landing whose demand / products fell below the thresholds this week is not dropped (its page is live and indexed)
        print(f'fasety: keeping {len(kept)} landings with hand texts that no longer pass the thresholds', file=sys.stderr)
    db.executemany('INSERT INTO facet_pages (id, slug, base_slug, qs, h1, seo_title, seo_desc, intro_html, second_html, faq_json, keyword, volume, min_products, total, noindex, updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', rows + kept)
    kinds = collections.Counter(r['kind'] for r in out)
    print(f'fasety: {len(out)} landings {dict(kinds)}', file=sys.stderr)
    if show:
        for r in out[:show]:
            print(f"  {r['vol']:>6} {r['n']:>5}  /{r['slug']}/  ← {r['cslug']}?{r['qs']}", file=sys.stderr)
    return len(out)


def texts(db, r):
    """H1-specific copy built from the live data of the landing (count, prices, brands, shops, discounts)."""
    base = f"""FROM cat_products cp JOIN products p ON p.id = cp.product_id WHERE cp.cat_id = ? AND p.status = 'publish' {r['sql']}"""
    a = (r['cid'], *r['args'])
    prices = sorted(x[0] for x in db.execute(f'SELECT p.min_price {base} AND p.min_price > 0', a))
    n = len(prices) or r['n']
    lo, hi, med = (int(prices[0]), int(prices[-1]), int(statistics.median(prices))) if prices else (0, 0, 0)
    brands = db.execute(f"SELECT b.name, COUNT(*) c {base.replace('WHERE', 'JOIN brands b ON b.id = p.brand_id WHERE', 1)} AND b.slug != 'ostatni' GROUP BY b.id ORDER BY c DESC LIMIT 4", a).fetchall()
    shops = db.execute(f"SELECT o.domain, COUNT(DISTINCT o.product_id) c {base.replace('WHERE', 'JOIN offers o ON o.product_id = p.id AND o.active = 1 WHERE', 1)} GROUP BY o.domain ORDER BY c DESC LIMIT 5", a).fetchall()
    disc = db.execute(f'SELECT COUNT(*) {base} AND p.disc_pct >= 10', a).fetchone()[0]
    h1, low = r['h1'], r['h1'].lower()
    nshops = len(db.execute(f"SELECT DISTINCT o.domain {base.replace('WHERE', 'JOIN offers o ON o.product_id = p.id AND o.active = 1 WHERE', 1)}", a).fetchall())
    bt = ', '.join(f'{b[0]} ({b[1]})' for b in brands[:3])
    title = f'{h1} – srovnání cen ({num(n)} produktů)'
    if len(title) > 62:
        title = f'{h1} – srovnání cen a nákup'
    desc = f'{h1}: porovnejte ceny {num(n)} produktů ve {nshops} e-shopech. Ceny od {num(lo)} Kč, velikosti skladem a slevy na jednom místě.'[:158]
    intro = (f'<p>Vybíráte <strong>{low}</strong>? Porovnáváme {num(n)} produktů ze {nshops} českých e-shopů. Ceny začínají na {num(lo)} Kč, '
             f'typická cena je kolem {num(med)} Kč a nejdražší kousky stojí {num(hi)} Kč.</p>') if lo else f'<p>Porovnáváme {num(n)} produktů: {low}.</p>'
    second = f'<h2>Jak vybrat {low}</h2>'
    if r['kind'] == 'gender':
        second += (f'<p>Střih, velikost i barevnost se u {low} liší podle výrobce, proto u každého produktu ukazujeme všechny dostupné velikosti '
                   f'a obchody, které je mají skladem. Filtrem vlevo zúžíte výběr podle značky, ceny nebo barvy.</p>')
    elif r['kind'] == 'brand':
        second += f'<p>Nabídku značky {r["label"]} v této kategorii sbíráme z více obchodů najednou, takže vidíte, jak se u stejného modelu liší cena.</p>'
    elif r['kind'] == 'sale':
        second += f'<p>Ve slevě je teď {num(disc)} z {num(n)} produktů (sleva alespoň 10 %). Řaďte podle největší slevy nebo podle ceny.</p>'
    else:
        second += f'<p>Barva {r["label"].lower()} patří k nejhledanějším. Filtrem upřesníte velikost, značku nebo cenu.</p>'
    if bt:
        second += f'<p>Nejvíc nabídek mají značky {bt}.</p>'
    faq = [
        {'q': f'Kolik stojí {low}?', 'a': f'Ceny začínají od {num(lo)} Kč, typický produkt stojí kolem {num(med)} Kč, nejdražší {num(hi)} Kč (podle aktuálních nabídek ve {nshops} obchodech).'},
        {'q': f'Kde koupit {low}?', 'a': 'U každého produktu vidíte ceny ze všech obchodů vedle sebe i s dopravou. ' + (f'Nejvíc nabídek mají {", ".join(s[0] for s in shops[:3])}.' if shops else '')},
        {'q': f'Jak často se ceny aktualizují?', 'a': 'Ceny a dostupnost načítáme z e-shopů pravidelně každý týden. Před nákupem si cenu a velikost ověřte v obchodě.'},
    ]
    return dict(title=title, desc=desc, intro=intro, second=second, faq=faq)


if __name__ == '__main__':
    import sqlite3
    path = next((a for a in sys.argv[1:] if a.endswith('.db')), str(Path(__file__).resolve().parent.parent / 'data/live-production.db'))
    con = sqlite3.connect(f'file:{path}?mode=ro', uri=True)
    con.row_factory = None
    mem = sqlite3.connect(':memory:')
    con.backup(mem)
    k = sys.argv.index('--show') + 1 if '--show' in sys.argv else 0
    generate(mem, show=int(sys.argv[k]) if k else 40)
    for row in mem.execute('SELECT slug, h1, seo_title, seo_desc, total FROM facet_pages ORDER BY volume DESC LIMIT 3'):
        print(row, file=sys.stderr)
