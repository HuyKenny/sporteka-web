#!/usr/bin/env python3
"""sporteka.cz — catalogue builder (runs on the Pi; D1 only serves).

    scripts/katalog.py build             # data/cj/*.jsonl.gz → data/next.db (stable ids from data/live-<env>.db)
    scripts/katalog.py report            # numbers, unmapped shop paths, a sample per category (reports/sporteka/)
    scripts/katalog.py push --env staging [--dry]
                                         # diff data/next.db against data/live-<env>.db → SQL → wrangler d1 execute;
                                         # on success next.db becomes live-<env>.db

Why on the Pi: at 300k products the nightly passes eroka runs inside the import Worker (category rules, facets,
EAN lookup) read millions of D1 rows. Here everything is computed in a local SQLite copy and D1 receives only
the rows that changed (one weekly import ≈ price changes, not the whole catalogue).

Pipeline of `build`:
  1. feed rows (variants) → categorize (scripts/kategorie.py) → shop groups (itemGroupId / product URL = one shop product)
  2. fashion shops (Bezvasport, Answear): clothing and shoes only from sport brands (brands seen in specialist shops)
  3. groups of different shops → one product: shared EAN, or brand + the same name key in the same section (union-find)
  4. ids, slugs, go slugs and created_at survive from the live copy (product_keys g:/ean:, offers (feed, unique_id))
  5. denormalised columns, cat_products with ancestors, facets/home/sitemaps into site_cache, data_version
"""
import gc
import argparse
import collections
import datetime
import gzip
import hashlib
import html
import json
import os
import re
import shutil
import sqlite3
import statistics
import subprocess
import sys
import time
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kategorie as K
import velikosti as V  # noqa: E402
import fasety as FS  # noqa: E402
import parametry as PM  # noqa: E402
import stranky  # noqa: E402

APP = Path(__file__).resolve().parent.parent
ROOT = Path(os.environ.get('SPT_ROOT') or '/home/kenny/ai')   # workspace root; in CI a temp dir holding credentials/ and reports/
DATA = APP / 'data'
NEXT = Path(os.environ['SPT_NEXT']) if os.environ.get('SPT_NEXT') else DATA / 'next.db'   # SPT_NEXT: a test build must not touch the real one
NODE = os.environ.get('SPT_NODE') or ('/home/kenny/.nvm/versions/node/v22.23.1/bin' if Path('/home/kenny/.nvm').exists() else str(Path(shutil.which('node') or '/usr/bin/node').parent))
BASE = 'https://sporteka.cz'
MAX_PRODUCTS = int(os.environ.get('SPT_MAX') or 700_000)
INDEX_TOP = 300_000  # only the best-scored products are in the sitemap / indexable; the rest is searchable but noindex
PRICE_EXEMPT = {'rybarske-lode-a-elektronika', 'kajaky-a-cluny'}   # legitimately expensive leaves inside floored sections
# tiny hardware nobody searches for as a product (tent guy-line clips …): dropped before clustering, owner's rule 2. 11.
JUNK_TITLE = re.compile(r'(spon\w*|napinac\w*|svork\w*|kovani|kotvic\w*)[^,]{0,40}stanov\w+ lan|stanov\w+ lan\w*[^,]{0,25}(spon|napinac|svork|kovani)')
# small spare parts / fittings under 60 Kč (screws, washers, end caps, springs …): not products people shop for; categories where such things are the normal goods are exempt
JUNK_PART = re.compile(r'\b(sroub\w*|matice|zatk\w*|cepick\w*|koncovk\w*|podlozk\w*|krouzek\w*|pruzin\w*|gumick\w*|objimk\w*|nytk\w*|ventilk\w*|nahradni (dil|pruz|zatk|cep|sroub)\w*|svork\w*|spona|sponk\w*)\b')
JUNK_PART_EXEMPT = {'sipkove-doplnky', 'sipky', 'sportovni-vyziva', 'energeticke-gely-a-tycinky', 'proteinove-tycinky-a-snacky', 'proteiny', 'nastrahy-a-navnady', 'vlasce-a-snury',
                    'muskareni', 'stanove-kolky', 'trampoliny', 'rybarske-doplnky', 'rybarske-pruty', 'posilovaci-gumy', 'fitness-pomucky', 'posilovaci-stroje'}
CHEAP_FLOOR = 100   # Kč
CHEAP_OK = {'sportovni-ponozky', 'lyzarske-ponozky', 'cyklisticke-ponozky', 'lahve-a-termosky'}
# weak cheap add-ons (Kenny 13. 11.): one shop + under WEAK_FLOOR Kč + an accessory / parts / bait category → not on the site,
# unless Google already shows the page (data/gsc.json impressions); a live one leaves as 'retired' with a 301 to its category
WEAK_FLOOR = 300   # Kč
WEAK_CATS = {t[1] for t in K.TREE if re.search(r'doplnk|prislusenstvi|dily|udrzba|pasky|gripy|sedla|nastrahy|vlasce|tkanick|plaste-a|brzdy|pohon|zvonky|blatnik|pumpy|kolik|nahradni', t[1])} \
    - {'ostatni-doplnky-stravy', 'bezecke-opasky'}   # nutrition and running belts are products, not add-ons
# tent repair bits and everyday/baby food that is not sport (owner's rule 2. 11.): dropped before clustering
JUNK_TITLE2 = re.compile(r'stanove naradi|opravn\w+ objimk|coghlans? (airstop|nylon repair)|repair tape|zaplatov\w+ pask|(sada )?uvazk\w+ na stan|stanov\w+ zavesn\w+ system|(sada )?prislusenstvi (pro|ke) stan|tent set\b'
                         r'|nahradn\w+ (tycky|tyce|sada tyci|snur\w+|kolik\w+|patk\w+) (ke|k|pro) (stan|bivak)|^topnatur (?!.*protein)|probio\w* kase|nutrikase|^gerber (cereal|natural|junior|kapsick|krupk|hello|mlicko|nemlecn|mlecn|ovocn|zeleninov|bio )|kase na dobrou noc|nemlecna kase|mlecna kase')
# tent spare parts / add-ons (poles, cords, pegs, footprints) and tubeless sealant: accessories of other products, not shown on their own
JUNK_TITLE3 = re.compile(r"\bstan'?s\b.*\b(tmel|sealant|notubes)|stans? tmel|notubes|stanov(?:y|a|e|ou|ych|emu|eho|em) (\w+ )?prut\w*|(dural\w*|durawrap\w*) prut\w*"
                         r"|stanov(?:y|a|e|ou|ych|emu|eho|em) (kotvic\w+ )?snur\w*|stanov(?:y|a|e|ou|ych|emu|eho|em) (\w+ )?kolik\w*|kolik\w* (do|na|ke|pro|k) stan|(sada )?kolik\w* a napinac\w+ lan"
                         r"|\b(tent|stan\w*) (pegs?|stakes?)\b|guyline|\w-peg\b|\bfootprint\b|stanov(?:y|a|e|ou|ych|emu|eho|em) podlazk\w*|podlazk\w+ (pod|do|ke|k|pro) stan")
PRICE_FLOOR = {'sportovni-obleceni': 30000, 'merino': 30000, 'sportovni-obuv': 22000, 'sportovni-vyziva': 6000, 'rybareni': 45000}   # Kč, see select_and_cluster
NOW = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
TODAY = NOW[:10]
# shops that sell everything fashion: their clothing/shoes only from sport brands
FASHION_SHOPS = {'Bezvasport cz/sk', 'Answear.cz', 'Spartoo.cz', 'Kokiskashop.cz', 'Allegro.cz', 'Lekarna.cz', 'Benu.cz'}
RESERVED = {'znacka', 'go', 'api', 'page', 'hledat', 'a', 'img', 'robots', 'sitemap', 'o-nas', 'kontakt', 'obchody',
            'ochrana-osobnich-udaju', 'podminky-pouziti', 'jak-srovnavame', 'cookies'}


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def slugify(t, n=90):
    s = K.fold(t)
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    if len(s) > n:
        s = s[:n].rsplit('-', 1)[0]
    return s or 'produkt'


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def norm_ean(v):
    d = re.sub(r'\D', '', str(v or ''))
    if len(d) in (8, 12, 13, 14) and set(d) != {'0'}:
        return d.zfill(13) if len(d) == 12 else d
    return ''


# ---------- names ----------
SIZE_TAIL = re.compile(r'''(\s*[-–,/|(]\s*)?(\b(vel(ikost)?\.?|size|eu|uk|us)\s*:?\s*)?
    (\d{2}(\s?[1-2]/3)?|\d{1,2}[.,]5|xxs|xs|s|m|l|xl|xxl|xxxl|[2-5]xl|\d{2,3}\s?cm|uni|onesize|one\ssize)\)?\s*$''', re.I | re.X)
STOP = {'a', 'na', 'pro', 's', 'se', 'z', 'do', 'v', 'the', 'with', 'and', 'for', 'panske', 'damske', 'detske', 'pansky', 'damsky',
        'detsky', 'panska', 'damska', 'detska', 'mens', 'womens', 'men', 'women', 'junior', 'kids', 'unisex', 'jr'}


ATTR_TAIL = re.compile(r'\s+(Varianta|Hmotnost|Délka|Průměr|Velikost|Objem|Nosnost|Rozměr|Rorměr|Příchuť|Barva|Aftma|Počet|Typ|Model)\s*(:.*)?$', re.I)


def clean_title(t):
    t = html.unescape(re.sub(r'\s+', ' ', t or '')).strip()
    t = ATTR_TAIL.sub('', t).strip(' ,')
    for _ in range(2):
        t2 = SIZE_TAIL.sub('', t).strip(' -–,/(:;|')
        if len(t2) >= 6:
            t = t2
    return t


def name_key(name, brand):
    toks = re.findall(r'[a-z0-9]+', K.fold(name))
    b = set(re.findall(r'[a-z0-9]+', K.fold(brand)))
    toks = sorted({w for w in toks if w not in STOP and w not in b and len(w) > 1})
    return ' '.join(toks)


BRAND_PREF = {}   # folded brand → the mixed-case spelling seen in a feed (Decathlon prints every brand in capitals: NIKE → Nike)


# sub-lines and spelling variants of one brand → one brand page (Kenny, 1. 11. 2026: "adidas Performance" and "Adidas" must be one)
BRAND_ALIAS = {
    'adidasperformance': 'Adidas', 'adidasoriginals': 'Adidas', 'adidasterrex': 'Adidas', 'adidasbystellamccartney': 'Adidas', 'adidassportswear': 'Adidas',
    'nikeswim': 'Nike', 'nikesportswear': 'Nike', 'nikeacgallconditionsgear': 'Nike', 'regattaoutdoors': 'Regatta', 'regattagreatoutdoors': 'Regatta',
    'calvinkleinperformance': 'Calvin Klein', 'progresssportswear': 'Progress', 'insportlineelectronics': 'Insportline', 'insportlineisl': 'Insportline',
    'reebokclassics': 'Reebok', 'reebokclassic': 'Reebok', 'swixtextile': 'Swix', 'swixhardgoods': 'Swix', 'hmspremium': 'HMS', 'vikingtechnology': 'Viking',
    'vikingbynorway': 'Viking', 'vikingkids': 'Viking', 'lonsdalelondon': 'Lonsdale', 'bullsnl': "Bull's", 'bullsdarts': "Bull's", 'alpinasports': 'Alpina',
    'filaskates': 'Fila', 'mfhdefence': 'MFH',
}
BRAND_CANON = {}   # spelling-insensitive key (letters and digits only) → the most used spelling (Dare2b / Dare 2B, JetFish / Jet Fish …)
bkey = lambda b: re.sub(r'[^a-z0-9]', '', K.fold(b))


def alias_brand(b):
    b = re.sub(r'\s+', ' ', html.unescape(b or '')).strip()
    return BRAND_ALIAS.get(bkey(b), b)


def nice_brand(b):
    b = alias_brand(b)
    canon = BRAND_CANON.get(bkey(b))
    if canon:
        return canon
    return _nice_brand(b)


def _nice_brand(b):
    """KILPI / kilpi → Kilpi; short acronyms (4F, HMS, UA) and mixed case (adidas Performance, DARE2B) stay."""
    b = re.sub(r'\s+', ' ', html.unescape(b or '')).strip()
    pref = BRAND_PREF.get(K.fold(b))
    if pref and (b.isupper() or b.islower()):
        return pref
    if b.islower() or (b.isupper() and len(b) > 3 and not re.search(r'\d', b)):
        return ' '.join(w if len(w) <= 3 and w.isupper() else w[:1].upper() + w[1:].lower() for w in b.split(' '))
    return b


TYPE_NOUN = {
    'mikiny': 'Mikina', 'fleecove-mikiny': 'Fleecová mikina', 'funkcni-mikiny': 'Funkční mikina', 'sportovni-tricka': 'Tričko', 'funkcni-tricka': 'Funkční tričko',
    'tilka': 'Top', 'polokosile': 'Polokošile', 'sportovni-kalhoty': 'Kalhoty', 'teplaky': 'Tepláky', 'sportovni-kratasy': 'Kraťasy', 'leginy': 'Legíny',
    'soupravy': 'Souprava', 'sportovni-bundy-jaro-podzim': 'Bunda', 'zimni-bundy': 'Zimní bunda', 'sportovni-vesty': 'Vesta', 'cepice-a-celenky': 'Čepice',
    'silnicni-bezecke-boty': 'Běžecké boty', 'trailove-boty': 'Trailové boty', 'trekova-obuv': 'Trekové boty', 'tenisky': 'Tenisky', 'kopacky': 'Kopačky',
    'salova-obuv': 'Sálová obuv', 'treninkova-obuv': 'Tréninková obuv', 'tenisova-obuv': 'Tenisová obuv', 'zimni-obuv': 'Zimní boty', 'sandaly': 'Sandály',
    'pantofle-a-zabky': 'Pantofle', 'basketbalova-obuv': 'Basketbalové boty', 'sportovni-ponozky': 'Ponožky', 'mestske-batohy': 'Batoh',
}
TYPE_WORDS = re.compile(r'mikin|hood|tric|trik|tee|shirt|top|polo|kalhot|pant|teplak|jogger|kratas|sortk|short|legin|tight|souprav|set|bund|jacket|vest|cepic|cap|ksilt|'
                        r'bot|obuv|shoe|tenisk|sneaker|kopack|sandal|pantofl|slide|zabk|ponozk|sock|batoh|backpack|bag', re.I)


def typed_name(name, cat):
    """'Nike Club' (D-Sport names carry only brand + model) → 'Mikina Nike Club'."""
    noun = TYPE_NOUN.get(cat)
    if noun and not TYPE_WORDS.search(K.fold(name)):
        return f'{noun} {name}'
    return name


def brand_case(title, brand):
    """The brand inside the title written like the brand (Hs-sport lowercases it: "bunda kilpi flip-w")."""
    if not brand:
        return title
    return re.sub(r'(?<![\w-])' + re.escape(brand) + r'(?![\w-])', brand, title, flags=re.I)


# ---------- descriptions ----------
class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'br', 'li', 'div', 'h2', 'h3', 'h4', 'tr'):
            self.out.append('\n')

    def handle_data(self, d):
        self.out.append(d)


def clean_desc(raw, limit=900):
    raw = html.unescape(raw or '')
    p = _Text()
    try:
        p.feed(raw)
        text = ''.join(p.out)
    except Exception:
        text = re.sub(r'<[^>]+>', ' ', raw)
    paras = [re.sub(r'\s+', ' ', x).strip() for x in text.split('\n')]
    paras = [x for x in paras if len(x) > 2]
    out, n = [], 0
    for x in paras:
        if n + len(x) > limit:
            if not out:
                cut = x[:limit].rsplit(' ', 1)[0]
                out.append(cut + '…')
            break
        out.append(x)
        n += len(x)
    esc = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return ''.join(f'<p>{esc(x)}</p>' for x in out)


# ---------- colours ----------
COLORS = [
    ('Černá', r'cern|black|anthracit|antracit|schwarz|nero|onyx'), ('Bílá', r'bil[aey]|white|ivory|offwhite|off white|cream|krem|smetan'),
    ('Šedá', r'sed[aey]|grey|gray|silver|stribr|graphit|grafit|charcoal|melange'), ('Modrá', r'modr|blue|navy|tyrky|turquo|azur|petrol|indigo|marine'),
    ('Červená', r'cerven|red(\W|$)|bordo|bordeaux|burgund|vinov|wine|cherry|carmine'), ('Zelená', r'zelen|green|khaki|olive|oliv|mint|militar|army|moss|pine|lime|limet'),
    ('Žlutá', r'zlut|yellow|mustard|horcic'), ('Oranžová', r'oranz|orange|coral|koral|apricot'), ('Růžová', r'ruzov|pink|rose|fuchs|magent|lososov|salmon'),
    ('Fialová', r'fial|purple|violet|lilac|lila|levand|lavend|plum'), ('Hnědá', r'hned|brown|camel|cokolad|chocolat|cognac|koniak|tobacco|kava|coffee|tan(\W|$)'),
    ('Béžová', r'bez(ov)|beige|sand|piskov|nude|tel(ov)|taupe|stone|ecru'), ('Zlatá', r'zlat|gold'),
]
COLOR_RX = [(n, re.compile(rx)) for n, rx in COLORS]


def color_of(v):
    f = K.fold(v)
    if not f:
        return ''
    if re.search(r'multi|vicebar|mix|print|potisk|kombin', f):
        return 'Vícebarevná'
    for n, rx in COLOR_RX:
        if rx.search(f):
            return n
    return ''


GENDER_LABEL = {'muzi': 'Pánské', 'zeny': 'Dámské', 'deti': 'Dětské', 'unisex': 'Unisex'}


# ---------- 1. feed rows → shop groups ----------
def load_groups():
    shops = json.load(open(APP / 'src/data/obchody.json'))['shops']
    groups = {}
    stats = collections.Counter()
    unmapped = collections.Counter()
    cat_cache = {}
    for sh in shops:
        f = DATA / 'cj' / f"{sh['advertiserId']}.jsonl.gz"
        if not sh.get('enabled') or not f.exists():
            continue
        feed = f"{({'decathlon': 'dec', 'xml': 'xml', 'allegro': 'alg'})[sh['source']]}:{sh['advertiserId']}" if sh.get('source') else f"cj:{sh['advertiserId']}"
        for line in gzip.open(f, 'rt', encoding='utf-8'):
            r = json.loads(line)
            stats['rows'] += 1
            if (r.get('cur') or 'CZK') != 'CZK':
                stats['not_czk'] += 1
                continue
            price, list_price = num(r.get('sp')), num(r.get('p'))
            if not price or price >= list_price:
                price, old = list_price, 0.0
            else:
                old = list_price
            if price <= 0 or not r.get('go') or not r.get('img'):
                stats['no_price_link_img'] += 1
                continue
            path = (r.get('pt') or [''])[0]
            title = clean_title(r.get('t'))
            ck = (path, title, r.get('sport', ''), r.get('nature', ''), (r.get('seller') or 'Decathlon') == 'Decathlon')
            if ck not in cat_cache:
                cat_cache[ck] = K.categorize_ctx(path, title, r.get('gpc', ''), r.get('sport', ''), r.get('nature', ''), (r.get('seller') or 'Decathlon') == 'Decathlon')
            cat, fashion = cat_cache[ck]
            if not cat:
                stats['unmapped'] += 1
                unmapped[(sh['name'], ' > '.join(path.split(' > ')[:3]))] += 1
                continue
            url = r.get('url') or ''
            gk = r.get('g') or re.sub(r'[?#].*$', '', url) or r['id']
            key = (feed, gk)
            g = groups.get(key)
            if g is None:
                g = groups[key] = {
                    'feed': feed, 'shop': sh['name'], 'domain': sh['domain'], 'gk': gk, 'rows': [], 'fashion_shop': sh['name'] in FASHION_SHOPS, 'desc': '',
                }
            d_ = r.get('d') or ''
            if len(d_) > len(g['desc']):
                g['desc'] = d_[:900]   # one description per group (rows are memory)
            g['rows'].append({'id': r['id'], 'title': title, 'brand': (r.get('b') or '').strip(), 'ean': norm_ean(r.get('ean')),
                              'path': path, 'cat': cat, 'fashion': fashion, 'price': price, 'old': old, 'go': r['go'], 'url': url,
                              'img': r.get('img') or '', 'imgs': r.get('imgs') or [], 'size': (r.get('size') or '').strip(),
                              'col': r.get('col') or '', 'sex': r.get('sex') or '', 'seller': r.get('seller') or '', 'ship': r.get('ship') or ''})
    stats['groups'] = len(groups)
    return groups, stats, unmapped


def load_prices(since):
    """Daily update, light pass: (feed, group key) → (price, old price) of the shops whose feed file was refreshed at or after
    `since` (epoch seconds). Same group key and price rule as load_groups()/summarize() (cheapest variant, old price only when
    higher) but no categorising, no clustering and no rows kept in memory — groups that are not live are ignored later anyway.
    Returns (prices, files, counts): counts[feed] = number of groups, used to refuse a feed that shrank."""
    shops = json.load(open(APP / 'src/data/obchody.json'))['shops']
    prices, counts, used = {}, collections.Counter(), []
    for sh in shops:
        f = DATA / 'cj' / f"{sh['advertiserId']}.jsonl.gz"
        if not sh.get('enabled') or not f.exists() or f.stat().st_mtime < since:
            continue
        feed = f"{({'decathlon': 'dec', 'xml': 'xml', 'allegro': 'alg'})[sh['source']]}:{sh['advertiserId']}" if sh.get('source') else f"cj:{sh['advertiserId']}"
        used.append(sh['name'])
        for line in gzip.open(f, 'rt', encoding='utf-8'):
            r = json.loads(line)
            if (r.get('cur') or 'CZK') != 'CZK':
                continue
            price, list_price = num(r.get('sp')), num(r.get('p'))
            if not price or price >= list_price:
                price, old = list_price, 0.0
            else:
                old = list_price
            if price <= 0 or not r.get('go') or not r.get('img'):
                continue
            url = r.get('url') or ''
            gk = r.get('g') or re.sub(r'[?#].*$', '', url) or r['id']
            k = (feed, gk)
            cur = prices.get(k)
            if cur is None:
                counts[feed] += 1
            if cur is None or price < cur[0]:
                prices[k] = (price, old)
    return prices, used, counts


def summarize(g):
    rows = g['rows']
    most = lambda xs: collections.Counter(x for x in xs if x).most_common(1)[0][0] if any(xs) else ''
    best = min(rows, key=lambda r: r['price'])
    titles = [r['title'] for r in rows]
    g['title'] = most(titles)
    g['brand'] = alias_brand(most([r['brand'] for r in rows]))
    g['cat'] = most([r['cat'] for r in rows])
    g['fashion'] = any(r['fashion'] for r in rows if r['cat'] == g['cat'])
    g['eans'] = {r['ean'] for r in rows if r['ean']}
    g['price'] = best['price']
    g['old'] = best['old'] if best['old'] > best['price'] else 0.0
    g['go'] = best['go']
    g['url'] = re.sub(r'[?#].*$', '', best['url']) or best['url']
    g['img'] = best['img']
    g['imgs'] = [u for u in dict.fromkeys(best['imgs']) if u and u != best['img']][:5]
    chain, t = [], K.BY_SLUG[g['cat']]
    while t:
        chain.append(t[1])
        t = K.BY_SLUG[t[3]] if t[3] else None
    g['sizes'] = V.norm_sizes([r['size'] for r in rows if r['size']], V.kind_of(g['cat'], chain))
    g['color'] = color_of(most([r['col'] for r in rows]) or g['title'])
    g['gender'] = K.gender(rows[0]['path'], g['title'], most([r['sex'] for r in rows]))
    g['seller'] = best.get('seller', '')
    g['ship'] = num(best.get('ship')) if best.get('ship') else None
    g['nk'] = name_key(g['title'], g['brand'])
    g['section'] = K.section(g['cat'])
    g['variants'] = len(rows)
    del g['rows']
    return g


LETTERS = ['xxxs', 'xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl', '2xl', 'xxxl', '3xl', '4xl', '5xl']


def size_order(s):
    f = s.lower().strip()
    if f in LETTERS:
        return (0, LETTERS.index(f), f)
    m = re.match(r'(\d+(?:[.,]\d+)?)', f)
    if m:
        return (1, float(m.group(1).replace(',', '.')), f)
    return (2, 0, f)


# ---------- 2.–3. selection and clustering ----------
class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def select_and_cluster(groups):
    gs = [summarize(g) for g in groups.values()]
    forms = collections.defaultdict(collections.Counter)
    for g in gs:
        b = (g['brand'] or '').strip()
        if b and not (b.isupper() or b.islower()):
            forms[K.fold(b)][b] += 1
    BRAND_PREF.update({k: c.most_common(1)[0][0] for k, c in forms.items()})
    spell = collections.defaultdict(collections.Counter)
    for g in gs:
        if g['brand']:
            spell[bkey(g['brand'])][_nice_brand(g['brand'])] += 1
    BRAND_CANON.update({k: c.most_common(1)[0][0] for k, c in spell.items() if len(c) > 1 and k})
    # sport brands = brands present in the specialist shops (≥ 3 shop products)
    bc = collections.Counter(K.fold(g['brand']) for g in gs if not g['fashion_shop'] and g['brand'])
    sport_brands = {b for b, n in bc.items() if n >= 3}
    kept, drop = [], collections.Counter()
    # price sanity: complete bikes sorted into "Cyklo příslušenství", e-trikes in "Trička", boat motors in "Rybářské pruty" …
    med = {c: statistics.median(sorted(g['price'] for g in gs if g['cat'] == c)) for c in {g['cat'] for g in gs}
           if K.section(c) in PRICE_FLOOR}
    for g in gs:
        if g['cat'] in ('cyklo-prislusenstvi', 'cyklo-dily') and g['price'] >= 15000:
            g['cat'] = 'elektrokola' if re.search(r'turbo|levo|vado|kenevo|e-?bike|elektr|bosch|(^| )ep\d', K.fold(g['title'])) else 'jizdni-kola'
            g['section'] = K.section(g['cat'])
            drop['bike_reclassified'] += 1
        fl = None if g['cat'] in PRICE_EXEMPT else PRICE_FLOOR.get(K.section(g['cat']))
        if fl and g['price'] > max(fl, 12 * med.get(g['cat'], 0)):
            drop['price_outlier'] += 1
            continue
        if JUNK_TITLE.search(K.fold(g['title'])) or JUNK_TITLE2.search(K.fold(g['title'])) or JUNK_TITLE3.search(K.fold(g['title'])):
            drop['junk_title'] += 1
            continue
        if g['price'] < 60 and g['cat'] not in JUNK_PART_EXEMPT and JUNK_PART.search(K.fold(g['title'])):
            drop['junk_part'] += 1
            continue
        if g['price'] < CHEAP_FLOOR and g['cat'] not in JUNK_PART_EXEMPT and g['cat'] not in CHEAP_OK:
            drop['cheap'] += 1      # owner's rule 3. 11.: no tiny add-ons; long-tail sections (lures, darts, nutrition, fishing) are exempt
            continue
        apparel = g['section'] in K.APPAREL_ROOTS
        if g['fashion'] and apparel:
            drop['fashion_type'] += 1
            continue
        if g['fashion_shop'] and K.fold(g['brand']) not in sport_brands and not K.SPORT_STRONG.search(K.fold(g['title'])):   # bags/caps/glasses too, not only clothing
            drop['fashion_brand'] += 1
            continue
        kept.append(g)
    log(f'groups {len(gs)} → kept {len(kept)}  dropped {dict(drop)}  sport brands {len(sport_brands)}')
    uf = UF()
    by_ean = {}
    by_nk = {}
    for i, g in enumerate(kept):
        uf.find(i)
        for e in g['eans']:
            j = by_ean.get(e)
            if j is None:
                by_ean[e] = i
            elif kept[j]['feed'] != g['feed'] and (not g['brand'] or not kept[j]['brand'] or K.fold(g['brand']) == K.fold(kept[j]['brand'])):
                uf.union(i, j)
        if g['brand'] and len(g['nk']) >= 8:
            k = (K.fold(g['brand']), g['nk'], g['section'], g['color'], g['gender'])
            j = by_nk.get(k)
            if j is None:
                by_nk[k] = i
            elif kept[j]['feed'] != g['feed']:
                uf.union(i, j)
    clusters = collections.defaultdict(list)
    for i, g in enumerate(kept):
        clusters[uf.find(i)].append(g)
    out = list(clusters.values())
    # a cluster must not swallow many products of one shop (a shared "EAN" like 0000…/a shop's dummy code)
    fixed = []
    for c in out:
        per = collections.Counter(g['feed'] for g in c)
        if max(per.values()) > 3:
            fixed.extend([[g] for g in c])
        else:
            fixed.append(c)
    log(f'products (clusters) {len(fixed)}, with ≥2 shops {sum(1 for c in fixed if len({g["feed"] for g in c}) > 1)}')
    return fixed, sport_brands


def score(c):
    shops = len({g['feed'] for g in c})
    lead = c[0]
    return shops * 100 + (20 if any(g['eans'] for g in c) else 0) + (15 if not lead['fashion_shop'] else 0) + min(lead['variants'], 20) + (10 if lead['imgs'] else 0)


# ---------- 4.–5. next.db ----------
def open_db(path, fresh=False):
    if fresh and path.exists():
        path.unlink()
    db = sqlite3.connect(path)
    db.execute('PRAGMA journal_mode=OFF')
    db.execute('PRAGMA synchronous=OFF')
    if fresh:
        sql = (APP / 'migrations/0001_init.sql').read_text()
        sql = re.sub(r'CREATE VIRTUAL TABLE product_fts[^;]*;', '', sql)
        db.executescript(sql)
    return db


def live_path(env):
    return DATA / f'live-{env}.db'


def build(env):
    t0 = time.time()
    groups, stats, unmapped = load_groups()
    log(f'rows {stats["rows"]}, groups {stats["groups"]}, unmapped rows {stats["unmapped"]}, skipped {stats["no_price_link_img"]}')
    clusters, sport_brands = select_and_cluster(groups)
    del groups
    gc.collect()
    for c in clusters:
        c.sort(key=lambda g: (g['fashion_shop'], -g['variants'], g['price']))
    clusters.sort(key=score, reverse=True)
    if len(clusters) > MAX_PRODUCTS:
        log(f'cap: {len(clusters)} → {MAX_PRODUCTS}')
        clusters = clusters[:MAX_PRODUCTS]

    live = live_path(env)
    old = sqlite3.connect(live) if live.exists() else None
    q = (lambda sql, *a: old.execute(sql, a).fetchall()) if old else (lambda *a, **k: [])
    # the previous state is read lazily through the live copy's indexes (key, id, feed+unique_id, slug are all indexed):
    # dictionaries of 2 M keys, 700 k products and 760 k offers cost ~2 GB of Python objects and killed the build on the Pi
    class Lazy:
        def __init__(self, sql, conv=None):
            self.sql, self.conv, self.cache = sql, conv, {}

        def get(self, key, default=None):
            if old is None:
                return default
            if key not in self.cache:
                r = old.execute(self.sql, key if isinstance(key, tuple) else (key,)).fetchone()
                self.cache[key] = self.conv(r) if (r and self.conv) else r
                if len(self.cache) > 50_000:
                    self.cache.clear()
                    self.cache[key] = self.conv(r) if (r and self.conv) else r
            v = self.cache[key]
            return default if v is None else v

        def __contains__(self, key):
            return self.get(key) is not None

        def __getitem__(self, key):
            return self.get(key)

    old_keys = Lazy('SELECT product_id FROM product_keys WHERE key = ?', lambda r: r[0])
    old_prod = Lazy('SELECT id, slug, created_at, min_price, name, updated_at, desc_html, image, last_offer_at FROM products WHERE id = ?',
                    lambda r: r[:6] + (hash(r[6]), r[7], r[8]))
    old_offer = Lazy('SELECT id, go_slug, updated_at, content_hash FROM offers WHERE feed = ? AND unique_id = ?')

    class Slugs:
        def __init__(self):
            self.cache = {}

        def __contains__(self, slug):
            if slug in RESERVED:
                return True
            if old is None:
                return False
            hit = self.cache.get(slug)
            if hit is None:
                hit = old.execute('SELECT 1 FROM slugs WHERE slug = ?', (slug,)).fetchone() is not None
                if len(self.cache) >= 50_000:   # bounded cache; clear BEFORE storing (clearing after lost the entry → KeyError, 10. 11.)
                    self.cache.clear()
                self.cache[slug] = hit
            return hit

        def __ior__(self, other):
            self.extra = getattr(self, 'extra', set()) | set(other)
            return self

        def __iter__(self):
            return iter(())

    class TakenSlug(Slugs):
        def __contains__(self, slug):
            return slug in getattr(self, 'extra', ()) or super().__contains__(slug)

    taken_slug = TakenSlug()
    next_pid = (old.execute('SELECT MAX(id) FROM products').fetchone()[0] or 0) + 1 if old else 1
    next_oid = (old.execute('SELECT MAX(id) FROM offers').fetchone()[0] or 0) + 1 if old else 1
    old_brand = dict(q('SELECT slug, id FROM brands'))
    next_bid = max([0] + list(old_brand.values())) + 1

    db = open_db(NEXT, fresh=True)
    cat_by_slug = {t[1]: t for t in K.TREE}
    for i, (cid, slug, name, parent) in enumerate(K.TREE):
        db.execute('INSERT INTO categories (id, slug, name, parent, menu_order) VALUES (?,?,?,?,?)',
                   (cid, slug, name, cat_by_slug[parent][0] if parent else 0, i))
        db.execute("INSERT INTO slugs (slug, kind, ref_id) VALUES (?, 'category', ?)", (slug, cid))
    cat_slugs = {t[1] for t in K.TREE}
    old_pages = {r[0]: r for r in q('SELECT id, content_html, published_at, modified_at FROM posts')}
    for pid_, slug, title, desc, body in stranky.PAGES:
        op_ = old_pages.get(pid_)
        body = body.strip()
        db.execute("INSERT INTO posts (id, type, slug, title, content_html, excerpt, published_at, modified_at, seo_desc) VALUES (?, 'page', ?, ?, ?, ?, ?, ?, ?)",
                   (pid_, slug, title, body, desc, op_[2] if op_ else NOW, op_[3] if op_ and op_[1] == body else NOW, desc))
        db.execute("INSERT INTO slugs (slug, kind, ref_id) VALUES (?, 'page', ?)", (slug, pid_))
        cat_slugs.add(slug)
    taken_slug |= cat_slugs

    def ancestors(slug):
        out = []
        t = cat_by_slug[slug]
        while t:
            out.append(t[0])
            t = cat_by_slug.get(t[3]) if t[3] else None
        return out

    brands = {}  # slug → [id, name, count]
    used_pids, used_slugs = set(), set(cat_slugs)
    prod_rows, offer_rows, cp_rows, bp_rows, pp_rows, key_rows, slug_rows, hist_rows = [], [], [], [], [], [], [], []
    n_prod = n_off = 0
    db.execute('CREATE TABLE _pk (key TEXT, product_id INTEGER)')

    def flush():
        # batch write: rows of the last few thousand products go to SQLite and leave RAM
        nonlocal n_prod, n_off
        db.executemany(f'INSERT INTO products (id, slug, name, status, short_html, desc_html, image, images, ean, primary_cat, brand_id, created_at, updated_at, noindex, seo_title, seo_desc, source, min_price, max_price, offer_count, shop_count, best_offer_id, best_domain, disc_pct, in_stock, pop, last_offer_at) VALUES ({",".join("?" * 27)})', prod_rows)
        db.executemany(f'INSERT INTO offers (id, product_id, feed, unique_id, title, domain, price, price_old, currency, target_url, orig_url, stock, ean, img, sizes, variants, delivery_price, extra, go_slug, updated_at, active, content_hash) VALUES ({",".join("?" * 22)})', offer_rows)
        db.executemany('INSERT INTO cat_products (cat_id, created_at, product_id, direct, min_price, pop, disc) VALUES (?,?,?,?,?,?,?)', cp_rows)
        db.executemany('INSERT INTO brand_products (brand_id, created_at, product_id) VALUES (?,?,?)', bp_rows)
        db.executemany('INSERT OR IGNORE INTO product_params (product_id, key, value) VALUES (?,?,?)', pp_rows)
        db.executemany('INSERT INTO _pk (key, product_id) VALUES (?,?)', key_rows)
        db.executemany('INSERT INTO slugs (slug, kind, ref_id) VALUES (?,?,?)', slug_rows)
        n_prod += len(prod_rows)
        n_off += len(offer_rows)
        for l_ in (prod_rows, offer_rows, cp_rows, bp_rows, pp_rows, key_rows, slug_rows):
            l_.clear()

    gsc_file = DATA / 'gsc.json'
    gsc_seen = set(json.loads(gsc_file.read_text())['pages']) if gsc_file.exists() else None
    weak_dropped = 0
    for ci, c in enumerate(clusters):
        lead = c[0]
        keys = [f"g:{g['feed']}:{g['gk']}" for g in c] + [f'ean:{e}' for g in c for e in sorted(g['eans'])]
        cand = collections.Counter(old_keys[k] for k in keys if k in old_keys and old_keys[k] not in used_pids)
        pid = cand.most_common(1)[0][0] if cand else None
        if pid is None:
            pid = next_pid
            next_pid += 1
        used_pids.add(pid)
        op = old_prod.get(pid)
        brand = nice_brand(lead['brand'] or next((g['brand'] for g in c if g['brand']), ''))
        name = typed_name(brand_case(lead['title'], brand), lead['cat'])
        if lead['color'] and K.fold(lead['color'])[:4] not in K.fold(name) and lead['domain'] == 'd-sport.cz':
            name = f"{name} {lead['color'].lower()}"
        if op and op[1] not in used_slugs:
            slug = op[1]
        else:
            slug = slugify(name)
            if slug in used_slugs or (slug in taken_slug and not (op and op[1] == slug)):
                slug = f'{slug[:80]}-{pid}'
        if (lead['cat'] in WEAK_CATS and len({g['feed'] for g in c}) == 1 and min(g['price'] for g in c) < WEAK_FLOOR
                and (gsc_seen is not None or not op) and f'/{slug}/' not in (gsc_seen or ())):
            weak_dropped += 1   # without Search Console data only new products are skipped (a live page is never removed blind)
            continue
        used_slugs.add(slug)
        created = op[2] if op else NOW
        bid = 0
        if brand:
            bs = slugify(brand, 60)
            b = brands.get(bs)
            if b is None:
                bid_ = old_brand.get(bs)
                if bid_ is None:
                    bid_ = next_bid
                    next_bid += 1
                b = brands[bs] = [bid_, brand, 0]
            b[2] += 1
            bid = b[0]
        # offers: one per shop group
        offers = []
        for g in c:
            ok = (g['feed'], g['gk'])
            _o = old_offer.get(ok)
            oid, go, o_upd, o_hash = _o if _o else (None, None, None, None)
            if oid is None:
                oid = next_oid
                next_oid += 1
            if not go:
                go = f"{slug[:70]}-{g['domain'].split('.')[0]}-{oid}"
            h = hashlib.md5(json.dumps([g['price'], g['old'], g['go'], g['sizes'], g['title'], g.get('ship'), g.get('seller')], ensure_ascii=False).encode()).hexdigest()[:16]
            # unchanged offers keep their old timestamp: every changed row is a D1 write (rows written are billed), so a weekly push
            # must carry only real changes (prices, new/removed offers), not a fresh NOW on all 760k rows
            offers.append((oid, pid, g['feed'], g['gk'], g['title'], g['domain'], g['price'], g['old'], 'CZK', g['go'], g['url'], 1,
                           next(iter(sorted(g['eans'])), ''), g['img'], json.dumps(g['sizes'], ensure_ascii=False) if g['sizes'] else '',
                           g['variants'], g.get('ship'), json.dumps({'seller': g['seller']}, ensure_ascii=False) if g.get('seller') and g['seller'] != 'Decathlon' else '', go, o_upd if o_hash == h and o_upd else NOW, 1, h))
        offers.sort(key=lambda o: o[6])
        best = offers[0]
        min_price, max_price = best[6], max(o[6] for o in offers)
        disc = int(round((1 - best[6] / best[7]) * 100)) if best[7] > best[6] else 0
        shop_count = len({o[5] for o in offers})
        pop = shop_count * 100 + min(lead['variants'], 30) + (10 if disc >= 10 else 0) + (5 if lead['eans'] else 0)
        desc = clean_desc(lead['desc'])
        ean = next((e for g in c for e in sorted(g['eans'])), '')
        # Sportisimo refuses server-side image fetching (wsrv.nl): another shop's photo of the same product is safer
        pic = next((g for g in c if 'sportisimo' not in g['img']), lead)
        images = json.dumps(pic['imgs'], ensure_ascii=False) if pic['imgs'] else ''
        upd = op[5] if op and op[4] == name and op[6] == hash(desc) and op[7] == pic['img'] else NOW
        prod_rows.append((pid, slug, name, 'publish', '', desc, pic['img'], images, ean, cat_by_slug[lead['cat']][0], bid, created, upd, 1 if ci >= INDEX_TOP else 0, '', '',
                          lead['feed'], min_price, max_price, len(offers), shop_count, best[0], best[5], disc, 1, pop,
                          op[8] if op and op[8] and abs(op[3] - min_price) <= 0.5 else TODAY))   # last_offer_at moves only with a price change (not used by the site)
        offer_rows.extend(offers)
        anc = ancestors(lead['cat'])
        for i, cid in enumerate(anc):
            cp_rows.append((cid, created, pid, 1 if i == 0 else 0, min_price, pop, disc))
        if bid:
            bp_rows.append((bid, created, pid))
        gen = collections.Counter(g['gender'] for g in c if g['gender']).most_common(1)
        if gen:
            pp_rows.append((pid, 'pro', GENDER_LABEL[gen[0][0]]))
        if lead['color']:
            pp_rows.append((pid, 'barva', lead['color']))
        for sz in dict.fromkeys(x for g in c for x in g['sizes'] if V.filterable(x)):
            pp_rows.append((pid, 'velikost', sz))
        for k_, v_ in dict.fromkeys(PM.params(' '.join(K.fold(g['title']) for g in c), lead['cat'], PM.desc_text(desc))):
            pp_rows.append((pid, k_, v_))
        for k in dict.fromkeys(keys):
            key_rows.append((k, pid))
        slug_rows.append((slug, 'product', pid))
        if not op or abs(op[3] - min_price) > 0.5:
            hist_rows.append((pid, TODAY, min_price))
        clusters[ci] = None
        if len(prod_rows) >= 5000:
            flush()
            if (n_prod // 5000) % 20 == 0:
                db.commit()
                log(f'  written {n_prod}/{len(clusters)} products')
    flush()
    del clusters
    gc.collect()

    # an EAN shared by two products points nowhere (it would merge them next time)
    db.execute('INSERT OR IGNORE INTO product_keys (key, product_id) SELECT key, MIN(product_id) FROM _pk GROUP BY key HAVING COUNT(*) = 1')
    db.execute('DROP TABLE _pk')
    for bs, (bid, name, n) in brands.items():
        db.execute('INSERT INTO brands (id, slug, name, count, noindex) VALUES (?,?,?,?,?)', (bid, bs, name, n, 0 if n >= 3 else 1))
    if old:
        old.close()
        db.execute('ATTACH ? AS l', (str(live),))
        db.execute('INSERT OR IGNORE INTO price_history SELECT * FROM l.price_history')
        db.execute('INSERT OR IGNORE INTO redirects SELECT * FROM l.redirects')
        db.execute('INSERT OR IGNORE INTO facet_pages SELECT * FROM l.facet_pages')
        # products that disappeared: kept as 'retired' rows → 301 to their category (lifecycle as alkoholicky)
        db.execute('''INSERT OR IGNORE INTO products SELECT * FROM l.products lp WHERE lp.id NOT IN (SELECT id FROM main.products)''')
        db.execute("UPDATE products SET status = 'retired', offer_count = 0, shop_count = 0, best_offer_id = 0 WHERE id NOT IN (SELECT product_id FROM offers)")
        db.execute("INSERT OR IGNORE INTO redirects (from_path, to_path, status) SELECT '/' || p.slug || '/', '/' || c.slug || '/', 301 FROM products p JOIN categories c ON c.id = p.primary_cat WHERE p.status = 'retired' AND p.slug NOT IN (SELECT slug FROM slugs)")
        # a product back on sale loses its old 301 (else the rule / stub hides the live page)
        db.execute("DELETE FROM redirects WHERE from_path IN (SELECT '/' || slug || '/' FROM products WHERE status != 'retired')")
        # brand pages that were merged (adidas-performance → adidas, dare-2b → dare2b …): the old URL answers with a 301
        new_brands = {r[0] for r in db.execute('SELECT slug FROM main.brands')}
        for bname, bslug in db.execute('SELECT name, slug FROM l.brands').fetchall():
            ns = slugify(nice_brand(bname), 60)
            if ns != bslug and ns in new_brands and bslug not in new_brands:
                db.execute("INSERT OR REPLACE INTO redirects (from_path, to_path, status) VALUES (?,?,301)", (f'/znacka/{bslug}/', f'/znacka/{ns}/'))
        db.commit()
        db.execute('DETACH l')
    db.executemany('INSERT OR IGNORE INTO price_history (product_id, day, min_price) VALUES (?,?,?)', hist_rows)
    finalize(db)
    db.commit()
    db.close()
    log(f'next.db: {n_prod} products, {n_off} offers, {len(brands)} brands in {time.time() - t0:.0f} s; weak cheap add-ons skipped: {weak_dropped}')
    return unmapped


def finalize(db):
    """Counts, facets, homepage blocks, category photos, sitemaps, data_version → site_cache."""
    t_ = [time.time()]

    def lap(name):
        log(f'  finalize {name}: {time.time() - t_[0]:.0f} s')
        t_[0] = time.time()

    db.execute("UPDATE categories SET count_direct = (SELECT COUNT(*) FROM cat_products x WHERE x.cat_id = categories.id AND x.direct = 1), "
               "count_total = (SELECT COUNT(*) FROM cat_products x WHERE x.cat_id = categories.id)")
    db.execute('UPDATE categories SET noindex = CASE WHEN count_total < 5 THEN 1 ELSE 0 END')
    db.execute("UPDATE brands SET count = (SELECT COUNT(*) FROM brand_products x JOIN products p ON p.id = x.product_id WHERE x.brand_id = brands.id AND p.status = 'publish')")
    db.execute('UPDATE brands SET noindex = CASE WHEN count < 3 THEN 1 ELSE 0 END')
    lap('counts')
    FS.generate(db)              # facet landings from the keyword demand + this build's data
    lap('facet landings')
    cache = {}
    # /slevy/: which sections have discounted products (name, count) — one cheap site_cache row for the page
    cache['slevy'] = [[r[0], r[1], r[2]] for r in db.execute(
        "SELECT c.slug, c.name, COUNT(*) FROM cat_products x JOIN categories c ON c.id = x.cat_id AND (c.parent IS NULL OR c.parent = 0) "
        "JOIN products p ON p.id = x.product_id WHERE p.status = 'publish' AND p.in_stock = 1 AND p.disc_pct BETWEEN 10 AND 85 "
        "GROUP BY c.id HAVING COUNT(*) >= 20 ORDER BY 3 DESC").fetchall()]

    def facets(where_sql, args):
        # everything is aggregated by SQLite (the ids of a big section never travel through Python: 700k tuples cost ~150 MB per call)
        db.execute('CREATE TEMP TABLE IF NOT EXISTS _ids (id INTEGER PRIMARY KEY)')
        db.execute('DELETE FROM _ids')
        db.execute(f"INSERT INTO _ids SELECT p.id FROM products p WHERE p.status = 'publish' AND {where_sql}", args)
        n, lo, hi, st, d = db.execute('SELECT COUNT(*), MIN(CASE WHEN p.min_price > 0 THEN p.min_price END), MAX(CASE WHEN p.min_price > 0 THEN p.min_price END), '
                                      'COALESCE(SUM(p.in_stock <> 0), 0), COALESCE(SUM(p.disc_pct >= 10), 0) FROM products p JOIN _ids i ON i.id = p.id').fetchone()
        if not n:
            return None
        bc = db.execute('SELECT p.brand_id, COUNT(*) FROM products p JOIN _ids i ON i.id = p.id WHERE p.brand_id <> 0 GROUP BY p.brand_id ORDER BY 2 DESC, 1 LIMIT 60').fetchall()
        sc = db.execute('SELECT o.domain, COUNT(DISTINCT o.product_id) FROM offers o WHERE o.active = 1 AND o.product_id IN (SELECT id FROM _ids) GROUP BY o.domain ORDER BY 2 DESC').fetchall()
        pc = collections.defaultdict(list)
        for k, v, c_ in db.execute('SELECT key, value, COUNT(*) FROM product_params WHERE product_id IN (SELECT id FROM _ids) GROUP BY key, value ORDER BY 3 DESC'):
            pc[k].append([v, c_])
        return {'n': n, 'lo': int(lo) if lo else 0, 'hi': int(hi + 0.999) if hi else 0,
                'st': st, 'd': d,
                'b': [[b, c_] for b, c_ in bc], 's': [[d_, c_] for d_, c_ in sc], 'p': dict(pc)}

    for cid, in db.execute('SELECT id FROM categories WHERE count_total > 0').fetchall():
        f = facets('p.id IN (SELECT product_id FROM cat_products WHERE cat_id = ?)', (cid,))
        if f:
            cache[f'f:{cid}'] = f
    lap('category facets')
    for bid, in db.execute('SELECT id FROM brands WHERE count >= 3').fetchall():
        f = facets('p.brand_id = ?', (bid,))
        if f:
            # category chips on brand pages: top-level and second-level categories of the brand's products
            f['c'] = [[c, n] for c, n in db.execute('''SELECT x.cat_id, COUNT(*) FROM cat_products x JOIN products p ON p.id = x.product_id
                       WHERE p.brand_id = ? AND x.direct = 1 GROUP BY x.cat_id ORDER BY 2 DESC LIMIT 12''', (bid,))]
            cache[f'fb:{bid}'] = f
    # /slevy/: facets of every discounted product + the categories (sport) to choose from
    fs = facets("p.in_stock = 1 AND p.disc_pct BETWEEN 10 AND 85", ())
    if fs:
        fs['c'] = [[c, n] for c, n in db.execute('''SELECT x.cat_id, COUNT(*) FROM cat_products x JOIN products p ON p.id = x.product_id
                   WHERE p.status = 'publish' AND p.in_stock = 1 AND p.disc_pct BETWEEN 10 AND 85 GROUP BY x.cat_id HAVING COUNT(*) >= 20 ORDER BY 2 DESC LIMIT 30''')]
        cache['f:slevy'] = fs
    lap('brand facets + slevy')
    # category intro from the data (top brands, shops, price range); hand-written texts can replace it later
    bnames = dict(db.execute('SELECT id, name FROM brands'))
    for cid, name in db.execute('SELECT id, name FROM categories WHERE count_total > 0').fetchall():
        f = cache.get(f'f:{cid}')
        if not f:
            continue
        top = [bnames[b] for b, _ in f['b'][:4] if b in bnames]
        shops_n = len(f['s'])
        def kc(x):
            return f"{x:,}".replace(',', '\u00a0') + '\u00a0Kč'
        parts = [f"<p><strong>{html.escape(name)}</strong> — porovnáváme {f['n']:,} produktů".replace(',', '\u00a0')
                 + (f" z {shops_n} sportovních e-shopů" if shops_n > 1 else '') + (f", ceny od {kc(f['lo'])}" if f['lo'] else '') + '.']
        if top:
            parts.append(f" Nejvíc nabídek mají značky {', '.join(html.escape(b) for b in top[:-1])}{' a ' if len(top) > 1 else ''}{html.escape(top[-1])}.")
        if f['d']:
            parts.append(f" Ve slevě je teď {f['d']:,} produktů.".replace(',', '\u00a0'))
        parts.append(' U každého produktu vidíte ceny všech obchodů, velikosti skladem a vývoj ceny.</p>')
        db.execute("UPDATE categories SET description_html = ? WHERE id = ? AND description_html = ''", (''.join(parts), cid))
    # hand-written buying guides + FAQ of the most searched categories (scripts/texty-kategorie.py)
    import importlib.util
    spec = importlib.util.spec_from_file_location('texty_kategorie', APP / 'scripts/texty-kategorie.py')
    tk = importlib.util.module_from_spec(spec); spec.loader.exec_module(tk)
    log(f'category texts: {tk.write(db, None)}')
    lap('category texts')
    # homepage
    deals = [r[0] for r in db.execute("SELECT id FROM products WHERE status = 'publish' AND disc_pct BETWEEN 15 AND 80 AND shop_count >= 1 ORDER BY shop_count DESC, disc_pct DESC, pop DESC LIMIT 12")]
    popular = [r[0] for r in db.execute("SELECT id FROM products WHERE status = 'publish' ORDER BY pop DESC, id LIMIT 12")]
    home = {'deals': deals, 'popular': popular,
            'brands': [list(r) for r in db.execute('SELECT id, count FROM brands WHERE noindex = 0 ORDER BY count DESC LIMIT 24')],
            'shops': [list(r) for r in db.execute('SELECT domain, COUNT(DISTINCT product_id) FROM offers WHERE active = 1 GROUP BY domain ORDER BY 2 DESC')],
            'products': db.execute("SELECT COUNT(*) FROM products WHERE status = 'publish'").fetchone()[0],
            'offers': db.execute('SELECT COUNT(*) FROM offers WHERE active = 1').fetchone()[0]}
    cache['home'] = home
    imgs = {}
    for cid, slug in db.execute('SELECT id, slug FROM categories WHERE count_total > 0').fetchall():
        r = db.execute("SELECT p.image FROM cat_products x JOIN products p ON p.id = x.product_id WHERE x.cat_id = ? AND p.image <> '' ORDER BY x.pop DESC LIMIT 1", (cid,)).fetchone()
        if r:
            imgs[str(cid)] = r[0]
    cache['cats:img'] = imgs
    # product sitemap files that contain at least one indexable product (the sitemap index lists only these)
    cache['sitemap:files'] = [r[0] for r in db.execute("SELECT DISTINCT (id - 1) / 5000 + 1 FROM products WHERE status = 'publish' AND noindex = 0 AND offer_count > 0 ORDER BY 1")]
    lap('homepage + images')
    cache['data_version'] = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # header menu (src/data/menu.json, part of the web build): sections and their categories with ≥ 5 products
    counts = dict(db.execute('SELECT slug, count_total FROM categories'))
    menu = [{'slug': s_[1], 'name': s_[2], 'kids': [{'slug': k[1], 'name': k[2]} for k in K.TREE if k[3] == s_[1] and counts.get(k[1], 0) >= 5]}
            for s_ in K.TREE if not s_[3] and counts.get(s_[1], 0) >= 5]
    if not os.environ.get('SPT_NEXT'):   # a test build (SPT_NEXT) must not overwrite the real menu
        (APP / 'src/data/menu.json').write_text(json.dumps(menu, ensure_ascii=False, indent=1) + '\n')
    db.executemany('INSERT OR REPLACE INTO site_cache (key, value, updated_at) VALUES (?,?,?)',
                   [(k, v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, separators=(',', ':')), NOW) for k, v in cache.items()])


# ---------- push: diff next.db against the live copy ----------
TABLES = [  # (table, primary key columns); parents first
    ('categories', ['id']), ('brands', ['id']), ('posts', ['id']), ('products', ['id']), ('slugs', ['slug']), ('offers', ['id']),
    ('cat_products', ['cat_id', 'created_at', 'product_id']), ('brand_products', ['brand_id', 'created_at', 'product_id']),
    ('product_params', ['product_id', 'key', 'value']), ('product_keys', ['key']), ('price_history', ['product_id', 'day']),
    ('facet_pages', ['id']), ('redirects', ['from_path']), ('site_cache', ['key']),
]


def lit(v):
    if v is None:
        return 'NULL'
    if isinstance(v, (int, float)):
        return repr(v)
    return "'" + str(v).replace("'", "''") + "'"


def diff_sql(env):
    live = live_path(env)
    if not live.exists():
        open_db(live, fresh=True).close()
    db = sqlite3.connect(NEXT)
    db.execute('ATTACH ? AS l', (str(live),))
    stmts_del, stmts_up, counts = [], [], {}
    for t, pk in TABLES:
        cols = [r[1] for r in db.execute(f'PRAGMA main.table_info({t})')]
        pkc = ', '.join(pk)
        # deleted keys
        dels = db.execute(f'SELECT {pkc} FROM l.{t} EXCEPT SELECT {pkc} FROM main.{t}').fetchall()
        for r in dels:
            stmts_del.append(f'DELETE FROM {t} WHERE ' + ' AND '.join(f'{c} = {lit(v)}' for c, v in zip(pk, r)) + ';')
        ups = db.execute(f'SELECT * FROM main.{t} EXCEPT SELECT * FROM l.{t}').fetchall()
        head = f'INSERT OR REPLACE INTO {t} ({", ".join(cols)}) VALUES '
        buf, size = [], 0
        for r in ups:
            v = '(' + ','.join(lit(x) for x in r) + ')'
            if buf and size + len(v) > 60_000:
                stmts_up.append(head + ','.join(buf) + ';')
                buf, size = [], 0
            buf.append(v)
            size += len(v)
        if buf:
            stmts_up.append(head + ','.join(buf) + ';')
        counts[t] = (len(ups), len(dels))
    # full-text index (contentless_delete): products whose name or brand changed, new ones, removed ones
    fts_del = db.execute('''SELECT id FROM l.products EXCEPT SELECT p.id FROM main.products p JOIN l.products o ON o.id = p.id
                            WHERE o.name = p.name AND o.brand_id = p.brand_id AND o.status = p.status''').fetchall()
    fts_new = db.execute('''SELECT p.id, p.name, COALESCE(b.name, '') FROM main.products p LEFT JOIN main.brands b ON b.id = p.brand_id
                            WHERE p.status = 'publish' AND p.id NOT IN (SELECT o.id FROM l.products o JOIN main.products q ON q.id = o.id
                              WHERE o.name = q.name AND o.brand_id = q.brand_id AND o.status = q.status)''').fetchall()
    fts = [f'DELETE FROM product_fts WHERE rowid = {i};' for i, in fts_del]
    for i in range(0, len(fts_new), 300):
        fts.append('INSERT INTO product_fts (rowid, name, brand) VALUES ' + ','.join(f'({r[0]},{lit(r[1])},{lit(r[2])})' for r in fts_new[i:i + 300]) + ';')
    counts['product_fts'] = (len(fts_new), len(fts_del))
    db.close()
    # deletes child-first, then upserts parent-first; site_cache (data_version) last so pages switch to the new data at the end
    sc = [s for s in stmts_up if s.startswith('INSERT OR REPLACE INTO site_cache')]
    rest = [s for s in stmts_up if not s.startswith('INSERT OR REPLACE INTO site_cache')]
    return list(reversed(stmts_del)) + rest + fts + sc, counts


def wrangler(args, input_=None):
    """Runs wrangler. Auth: CF_API_TOKEN_SPORTEKA (scoped token; env var or credentials file) when present, else the global key."""
    cf, sp = {}, {}
    for f, d in (('.cloudflare-credentials.env', cf), ('.sporteka-credentials.env', sp)):
        p = ROOT / 'credentials' / f
        if not p.exists():
            continue
        for line in open(p):
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                d[k] = v.strip('"\'')
    token = os.environ.get('CF_API_TOKEN_SPORTEKA') or sp.get('CF_API_TOKEN_SPORTEKA')
    env = {**os.environ, 'PATH': f"{NODE}:{os.environ.get('PATH', '')}", 'CLOUDFLARE_ACCOUNT_ID': sp.get('CF_ACCOUNT_ID') or os.environ['CF_ACCOUNT_ID']}
    if token:
        env['CLOUDFLARE_API_TOKEN'] = token
        env.pop('CLOUDFLARE_EMAIL', None)
        env.pop('CLOUDFLARE_API_KEY', None)
    else:
        env.update({'CLOUDFLARE_EMAIL': cf['CF_EMAIL'], 'CLOUDFLARE_API_KEY': cf['CF_GLOBAL_API_KEY']})
    return subprocess.run([f'{NODE}/node', str(APP / 'node_modules/wrangler/bin/wrangler.js'), *args], cwd=APP, env=env,
                          input=input_, capture_output=True, text=True)


def push(env, dry):
    if env == 'production' and os.environ.get('SPT_PRODUCTION_APPROVED') != 'yes':
        sys.exit('production needs SPT_PRODUCTION_APPROVED=yes')
    stmts, counts = diff_sql(env)
    for t, (u, d) in counts.items():
        if u or d:
            log(f'  {t:16} upsert {u:8}  delete {d:7}')
    if not stmts:
        log('nothing to push')
        return
    cap = int(os.environ.get('SPT_PUSH_MAX') or 30_000)   # one multi-row statement ≈ 35 billed D1 rows (2. 11.: 1.0M statements = 34.7M writes); Kenny 3. 11.: no catalogue writes, weekly = `prices`
    if env == 'production' and len(stmts) > cap and os.environ.get('SPT_PUSH_FORCE') != 'yes':
        sys.exit(f'push refused: {len(stmts):,} statements > {cap:,} (D1 writes are billed beyond 50M/month); '
                 'review the diff, then re-run with SPT_PUSH_FORCE=yes')
    out = DATA / f'push-{env}'
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir()
    files, buf, size = [], [], 0
    for s in stmts:
        if buf and (size + len(s) > 30_000_000 or len(buf) >= 2500):
            files.append(buf)
            buf, size = [], 0
        buf.append(s)
        size += len(s)
    files.append(buf)
    for i, b in enumerate(files):
        (out / f'{i:04d}.sql').write_text('\n'.join(b) + '\n')
    log(f'{len(stmts)} statements in {len(files)} files ({sum(f.stat().st_size for f in out.glob("*.sql")) / 1e6:.1f} MB) → {out}')
    if dry:
        return
    for i, f in enumerate(sorted(out.glob('*.sql'))):
        for attempt in range(6):
            target = ['--local', '--persist-to', '.wrangler/state'] if env == 'local' else ['--remote', '--env', env]
            r = wrangler(['d1', 'execute', 'DB', *target, '--file', str(f), '-y'])
            if r.returncode == 0:
                break
            msg = (r.stderr or r.stdout)[-400:]
            log(f'  {f.name} attempt {attempt + 1} failed: {msg.strip()[:300]}')
            time.sleep(10 * (attempt + 1))
        else:
            sys.exit(f'push stopped at {f.name}; files before it are applied — fix and re-run push (the diff is recomputed from live-{env}.db only after success)')
        log(f'  {i + 1}/{len(files)} {f.name} ok')
    shutil.copy(NEXT, live_path(env))
    shutil.rmtree(out, ignore_errors=True)   # the SD card is tight (a push is hundreds of MB of SQL)
    log(f'live-{env}.db updated')


# ---------- update: weekly incremental refresh within the D1 write budget ----------
# Estimated billed D1 rows per change (row + rows of the indexes it touches); calibrate with bin/cf-spotreba.py.
WCOST = dict(offer_upd=3, offer_gone=3, offer_new=4, prod_upd=2, cp_upd=5, hist=1, prod=3, cp=5, bp=2, pp=2, key=2, slug=1, fts=4, redirect=1)


def prices_sql(env, daily_since=None):
    """Weekly incremental update (Kenny 3. 11.: new products in, products nobody sells out, prices + availability — all within
    the Workers Paid D1 write allowance). Compares a fresh, uncapped build (next.db) with the live mirror and emits small
    UPDATE/INSERT/DELETE statements, cheapest and most important first:
      1. price / old price / availability of offers already live; offers gone from a feed → inactive (failed feeds skipped)
      2. new shops' offers for products already live
      3. derived product columns (+ category listing columns, price history); products with no offer left → retired + 301
      4. new products (best `pop` first) until SPT_WEEK_WRITES (estimated billed rows) or SPT_LIVE_MAX products is reached
    The rest of the catalogue (names, texts, categories, params of existing products) stays frozen."""
    live = live_path(env)
    if not live.exists():
        sys.exit(f'{live} missing — run a full push first')
    budget = int(os.environ.get('SPT_WEEK_WRITES') or 4_000_000)
    live_max = int(os.environ.get('SPT_LIVE_MAX') or 800_000)
    daily = daily_since is not None
    if daily:   # Kenny 11. 11.: every day only prices of the feeds refreshed in this run; new / gone offers and products wait for the weekly build
        prices, used, counts = load_prices(daily_since)
        log(f'  daily: {len(prices):,} offer groups from {len(used)} refreshed shops')
        db = sqlite3.connect(':memory:')
        db.execute('CREATE TABLE offers (feed TEXT, unique_id TEXT, price REAL, price_old REAL)')
        db.executemany('INSERT INTO offers VALUES (?, ?, ?, ?)', [(f, g, p, o) for (f, g), (p, o) in prices.items()])
        db.execute('CREATE INDEX offers_k ON offers (feed, unique_id)')
        del prices
    else:
        db = sqlite3.connect(NEXT)
    db.execute('ATTACH ? AS l', (str(live),))
    stmts, est = [], 0
    offer_new = {}                                  # live offer id → (product id, price, old, active) after the update
    added = collections.defaultdict(list)           # live product id → new offers [(price, old, oid, domain)]
    skip_feeds = set()
    if daily:   # a feed that came back with < 50 % of its live offers is broken: leave its prices alone
        live_cnt = dict(db.execute('SELECT feed, COUNT(*) FROM l.offers WHERE active = 1 GROUP BY feed'))
        skip_feeds = {f for f, n in live_cnt.items() if f in counts and counts[f] < 0.5 * n}
        if skip_feeds:
            log('  daily: feeds skipped (< 50 % of live): ' + ', '.join(f'{f} {counts[f]}/{live_cnt[f]}' for f in sorted(skip_feeds)))
    for oid, pid, price, old, feed_ in db.execute(
            '''SELECT lo.id, lo.product_id, n.price, n.price_old, lo.feed FROM l.offers lo JOIN main.offers n ON n.feed = lo.feed AND n.unique_id = lo.unique_id
               WHERE n.price <> lo.price OR n.price_old IS NOT lo.price_old OR lo.active <> 1''').fetchall():
        if feed_ in skip_feeds:
            continue
        stmts.append(f'UPDATE offers SET price = {lit(price)}, price_old = {lit(old)}, stock = 1, active = 1, updated_at = {lit(NOW)} WHERE id = {oid};')
        offer_new[oid] = (pid, price, old, 1)
    n_price = len(stmts)
    est += n_price * WCOST['offer_upd']
    live_n = dict(db.execute('SELECT feed, COUNT(*) FROM l.offers WHERE active = 1 GROUP BY feed'))
    next_n = dict(db.execute('SELECT feed, COUNT(*) FROM main.offers GROUP BY feed'))
    broken = {f for f, n in live_n.items() if next_n.get(f, 0) < 0.5 * n} if not daily else set(live_n)   # daily: nothing is ever "gone"
    if broken and not daily:
        log('  update: feeds skipped for "gone" (missing or < 50 % of live): ' + ', '.join(f'{f} {next_n.get(f, 0)}/{live_n[f]}' for f in sorted(broken)))
    for oid, pid, lprice, lold, feed in db.execute(
            '''SELECT lo.id, lo.product_id, lo.price, lo.price_old, lo.feed FROM l.offers lo WHERE lo.active = 1
               AND NOT EXISTS (SELECT 1 FROM main.offers n WHERE n.feed = lo.feed AND n.unique_id = lo.unique_id)'''):
        if feed in broken:
            continue
        stmts.append(f'UPDATE offers SET stock = 0, active = 0, updated_at = {lit(NOW)} WHERE id = {oid};')
        offer_new[oid] = (pid, lprice, lold, 0)
    n_gone = len(stmts) - n_price
    est += n_gone * WCOST['offer_gone']
    # offers that are new in the feeds, grouped by the product the build put them in
    live_status = dict(db.execute('SELECT id, status FROM l.products'))
    ocols = [] if daily else [r[1] for r in db.execute('PRAGMA main.table_info(offers)')]
    new_by_pid = collections.defaultdict(list)
    if not daily:
      for r in db.execute('''SELECT n.* FROM main.offers n WHERE NOT EXISTS
                            (SELECT 1 FROM l.offers lo WHERE lo.feed = n.feed AND lo.unique_id = n.unique_id)'''):
        new_by_pid[r[1]].append(r)
    ins_offer = f'INSERT OR IGNORE INTO offers ({", ".join(ocols)}) VALUES '
    n_attach = 0
    for pid, rows in new_by_pid.items():
        if live_status.get(pid) == 'publish':
            for r in rows:
                stmts.append(ins_offer + '(' + ','.join(lit(x) for x in r) + ');')
                added[pid].append((r[6], r[7] or 0, r[0], r[5]))
                n_attach += 1
    est += n_attach * WCOST['offer_new']
    # derived product columns for every live product whose offers moved; nothing left on sale → retired
    touched = sorted({v[0] for v in offer_new.values()} | set(added))
    cat_slug = dict(db.execute('SELECT id, slug FROM l.categories'))
    n_prod = n_cp = n_ret = 0
    for i in range(0, len(touched), 500):
        chunk = touched[i:i + 500]
        q = ','.join('?' * len(chunk))
        offers = collections.defaultdict(list)
        for oid, pid, price, old, act, dom in db.execute(f'SELECT id, product_id, price, price_old, active, domain FROM l.offers WHERE product_id IN ({q})', chunk):
            if oid in offer_new:
                _, price, old, act = offer_new[oid]
            if act:
                offers[pid].append((price, old or 0, oid, dom))
        for pid, extra in ((p, added[p]) for p in chunk if p in added):
            offers[pid].extend(extra)
        cp_n = dict(db.execute(f'SELECT product_id, COUNT(*) FROM l.cat_products WHERE product_id IN ({q}) GROUP BY product_id', chunk))
        for pid, slug, status, pcat, mn, mx, oc, sc, bo, bd, dp, st in db.execute(
                f'''SELECT id, slug, status, primary_cat, min_price, max_price, offer_count, shop_count, best_offer_id, best_domain, disc_pct, in_stock
                    FROM l.products WHERE id IN ({q})''', chunk).fetchall():
            if status != 'publish':
                continue
            o = sorted(offers.get(pid, []))
            if not o:   # nobody sells it any more: off the site, its URL 301s to the category
                stmts += [f"UPDATE products SET status = 'retired', offer_count = 0, shop_count = 0, best_offer_id = 0, in_stock = 0 WHERE id = {pid};",
                          f'DELETE FROM cat_products WHERE product_id = {pid};', f'DELETE FROM brand_products WHERE product_id = {pid};',
                          f"DELETE FROM slugs WHERE slug = {lit(slug)} AND kind = 'product';",
                          f"INSERT OR REPLACE INTO redirects (from_path, to_path, status) VALUES ({lit('/' + slug + '/')}, {lit('/' + cat_slug.get(pcat, '') + '/')}, 301);",
                          f'DELETE FROM product_fts WHERE rowid = {pid};']
                est += WCOST['prod'] + WCOST['slug'] + WCOST['redirect'] + WCOST['bp'] + WCOST['fts'] + cp_n.get(pid, 0) * WCOST['cp']
                n_ret += 1
                continue
            b = o[0]
            new = (b[0], max(x[0] for x in o), len(o), len({x[3] for x in o}), b[2], b[3],
                   int(round((1 - b[0] / b[1]) * 100)) if b[1] > b[0] else 0, 1)
            if new != (mn, mx, oc, sc, bo, bd, dp, st):
                stmts.append(f'UPDATE products SET min_price = {lit(new[0])}, max_price = {lit(new[1])}, offer_count = {new[2]}, shop_count = {new[3]}, '
                             f'best_offer_id = {new[4]}, best_domain = {lit(new[5])}, disc_pct = {new[6]}, in_stock = 1 WHERE id = {pid};')
                est += WCOST['prod_upd']
                n_prod += 1
                if (new[0], new[6]) != (mn, dp):   # category listings sort/filter by price and discount
                    stmts.append(f'UPDATE cat_products SET min_price = {lit(new[0])}, disc = {new[6]} WHERE product_id = {pid};')
                    est += cp_n.get(pid, 0) * WCOST['cp_upd']
                    n_cp += 1
                if abs(new[0] - (mn or 0)) > 0.5:
                    stmts.append(f'INSERT OR REPLACE INTO price_history (product_id, day, min_price) VALUES ({pid}, {lit(TODAY)}, {lit(new[0])});')
                    est += WCOST['hist']
    log(f'  update: {n_price} offers repriced/back, {n_gone} offers gone, {n_attach} new offers on live products, '
        f'{n_prod} products repriced ({n_cp} in category lists), {n_ret} products retired — est. {est:,} rows written')
    if est > budget:
        sys.exit(f'update refused: price/availability alone ≈ {est:,} billed rows > budget {budget:,} (SPT_WEEK_WRITES) — check the feeds')
    if daily:
        db.close()
        if stmts:
            stmts.append(f"UPDATE site_cache SET value = {lit(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}, updated_at = {lit(NOW)} WHERE key = 'data_version';")
        return stmts
    # new products (or retired ones that are back): whole product from next.db, best first, while budget + size allow
    n_live = sum(1 for s_ in live_status.values() if s_ == 'publish') - n_ret
    live_slugs = {r[0] for r in db.execute('SELECT slug FROM l.slugs')}
    live_brands = dict(db.execute('SELECT id, slug FROM l.brands'))
    live_brand_slugs = set(live_brands.values())
    next_brands = {r[0]: r for r in db.execute('SELECT * FROM main.brands')}
    bcols = [r[1] for r in db.execute('PRAGMA main.table_info(brands)')]
    cat_ok = {r[0] for r in db.execute('SELECT n.id FROM main.categories n JOIN l.categories o ON o.id = n.id AND o.slug = n.slug')}
    pcols = [r[1] for r in db.execute('PRAGMA main.table_info(products)')]
    n_new = n_skip = 0
    brands_added = set()
    for row in db.execute("SELECT * FROM main.products WHERE status = 'publish' ORDER BY pop DESC").fetchall():
        pid, slug, bid, pcat = row[0], row[1], row[10], row[9]
        if pid not in new_by_pid or live_status.get(pid) == 'publish':
            continue
        if n_live >= live_max:
            break
        offers_n = db.execute('SELECT COUNT(*) FROM main.offers WHERE product_id = ?', (pid,)).fetchone()[0]
        if offers_n != len(new_by_pid[pid]) or slug in live_slugs or pcat not in cat_ok:
            n_skip += 1   # re-clustered from live offers, slug taken or unknown category: wait for a full rebuild
            continue
        cps = db.execute('SELECT * FROM main.cat_products WHERE product_id = ?', (pid,)).fetchall()
        if any(c[0] not in cat_ok for c in cps):
            n_skip += 1
            continue
        st = []
        if bid and live_brands.get(bid) is None and bid not in brands_added:
            nb = next_brands.get(bid)
            if not nb or nb[1] in live_brand_slugs:
                n_skip += 1
                continue
            st.append(f'INSERT OR IGNORE INTO brands ({", ".join(bcols)}) VALUES (' + ','.join(lit(x) for x in nb) + ');')
            brands_added.add(bid)
        elif bid and bid not in brands_added and live_brands.get(bid) != next_brands.get(bid, (0, None))[1]:
            n_skip += 1
            continue
        bps = db.execute('SELECT * FROM main.brand_products WHERE product_id = ?', (pid,)).fetchall()
        pps = db.execute('SELECT * FROM main.product_params WHERE product_id = ?', (pid,)).fetchall()
        kys = db.execute('SELECT * FROM main.product_keys WHERE product_id = ?', (pid,)).fetchall()
        sls = db.execute("SELECT * FROM main.slugs WHERE kind = 'product' AND ref_id = ?", (pid,)).fetchall()
        cost = (WCOST['prod'] + offers_n * WCOST['offer_new'] + len(cps) * WCOST['cp'] + len(bps) * WCOST['bp'] + len(pps) * WCOST['pp']
                + len(kys) * WCOST['key'] + len(sls) * WCOST['slug'] + WCOST['fts'] + WCOST['hist'] + WCOST['redirect'])
        if est + cost > budget:
            break
        st.append(f'INSERT OR REPLACE INTO products ({", ".join(pcols)}) VALUES (' + ','.join(lit(x) for x in row) + ');')
        st += [ins_offer + '(' + ','.join(lit(x) for x in r) + ');' for r in new_by_pid[pid]]
        for t, rows in (('cat_products', cps), ('brand_products', bps), ('product_params', pps), ('product_keys', kys), ('slugs', sls)):
            tc = ', '.join(r_[1] for r_ in db.execute(f'PRAGMA main.table_info({t})'))
            st += [f'INSERT OR IGNORE INTO {t} ({tc}) VALUES (' + ','.join(lit(x) for x in r) + ');' for r in rows]
        bname = (next_brands.get(bid) or (0, '', ''))[2] if bid else ''
        st += [f"DELETE FROM redirects WHERE from_path = {lit('/' + slug + '/')};",
               f'INSERT OR REPLACE INTO price_history (product_id, day, min_price) VALUES ({pid}, {lit(TODAY)}, {lit(row[17])});',
               f'DELETE FROM product_fts WHERE rowid = {pid};',
               f'INSERT INTO product_fts (rowid, name, brand) VALUES ({pid}, {lit(row[2])}, {lit(bname or "")});']
        stmts += st
        est += cost
        live_slugs.add(slug)
        n_live += 1
        n_new += 1
    db.close()
    if stmts:   # pages and sitemaps are cached under data_version: bump it last
        stmts.append(f"UPDATE site_cache SET value = {lit(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))}, updated_at = {lit(NOW)} WHERE key = 'data_version';")
    log(f'  update: {n_new} new products added, {n_skip} skipped (need a full rebuild); live products {n_live:,}; est. {est:,} rows written (budget {budget:,})')
    return stmts


def adopt(env, dry=False):
    """Weekly, after `build` (Kenny 11. 11.: new / gone products AND new categories + landings once a week, prices daily).
    The static site renders from the mirror data/live-production.db; since D1 is gone nothing has to be diffed into small writes any
    more: the freshly built next.db (stable ids, retired products kept as 301s, categories, facet landings, sitemaps …) simply BECOMES
    the mirror — after sanity checks that refuse a half-built catalogue (a feed outage must not wipe the site)."""
    live = live_path(env)
    if not NEXT.exists():
        sys.exit(f'{NEXT} missing — run build first')
    n = sqlite3.connect(f'file:{NEXT}?mode=ro', uri=True)
    q = lambda c, sql: c.execute(sql).fetchone()[0]
    new = dict(products=q(n, "SELECT COUNT(*) FROM products WHERE status = 'publish'"), offers=q(n, 'SELECT COUNT(*) FROM offers'),
               categories=q(n, 'SELECT COUNT(*) FROM categories'), brands=q(n, 'SELECT COUNT(*) FROM brands WHERE noindex = 0'),
               landings=q(n, 'SELECT COUNT(*) FROM facet_pages'))
    old = {}
    if live.exists():
        o = sqlite3.connect(f'file:{live}?mode=ro', uri=True)
        old = dict(products=q(o, "SELECT COUNT(*) FROM products WHERE status = 'publish'"), offers=q(o, 'SELECT COUNT(*) FROM offers'),
                   categories=q(o, 'SELECT COUNT(*) FROM categories'), brands=q(o, 'SELECT COUNT(*) FROM brands WHERE noindex = 0'),
                   landings=q(o, 'SELECT COUNT(*) FROM facet_pages'))
        gone_cats = [r[0] for r in o.execute('SELECT slug FROM categories') if r[0] not in {x[0] for x in n.execute('SELECT slug FROM categories')}]
        o.close()
    else:
        gone_cats = []
    n.close()
    log(f'adopt: new {new} / live {old or "none"}')
    problems = []
    for k, floor in (('products', 0.9), ('offers', 0.85), ('brands', 0.9), ('landings', 0.9)):
        if old.get(k) and new[k] < floor * old[k]:
            problems.append(f'{k}: {new[k]:,} < {int(floor * 100)} % of {old[k]:,}')
    if old.get('categories') and new['categories'] < old['categories']:
        problems.append(f'categories: {new["categories"]} < {old["categories"]} (lost: {", ".join(gone_cats[:8])})')
    if problems:
        sys.exit('adopt refused: ' + '; '.join(problems) + ' — check the feeds / the build log (the old mirror stays)')
    if dry:
        log('adopt --dry: checks passed, nothing replaced')
        return
    tmp = live.with_suffix('.adopting')
    shutil.copyfile(NEXT, tmp)
    for suf in ('-wal', '-shm'):
        Path(str(live) + suf).unlink(missing_ok=True)
    os.replace(tmp, live)
    log(f'adopt: {live.name} replaced by the new catalogue')


def push_prices(env, dry, daily_since=None):
    if env == 'production' and os.environ.get('SPT_PRODUCTION_APPROVED') != 'yes':
        sys.exit('production needs SPT_PRODUCTION_APPROVED=yes')
    stmts = prices_sql(env, daily_since)
    if not stmts:
        log('nothing to push')
        return
    # the write budget is enforced in prices_sql (SPT_WEEK_WRITES, estimated billed rows)
    out = DATA / f'prices-{env}'
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir()
    files = [stmts[i:i + 5000] for i in range(0, len(stmts), 5000)]
    for i, b in enumerate(files):
        (out / f'{i:04d}.sql').write_text('\n'.join(b) + '\n')
    log(f'{len(stmts)} statements in {len(files)} files → {out}')
    if dry:
        return
    live = sqlite3.connect(live_path(env))
    # SPT_MIRROR_ONLY=yes (Kenny 8. 11.: nothing may cost money): the statements go only into the local mirror, which the
    # static export (scripts/staticky.py) renders from; D1 — and the old SSR site — keep the last pushed data
    mirror_only = os.environ.get('SPT_MIRROR_ONLY') == 'yes'
    for i, f in enumerate(sorted(out.glob('*.sql'))):
        for attempt in range(0 if mirror_only else 6):
            target = ['--local', '--persist-to', '.wrangler/state'] if env == 'local' else ['--remote', '--env', env]
            r = wrangler(['d1', 'execute', 'DB', *target, '--file', str(f), '-y'])
            if r.returncode == 0:
                break
            log(f'  {f.name} attempt {attempt + 1} failed: {(r.stderr or r.stdout)[-300:].strip()}')
            time.sleep(10 * (attempt + 1))
        else:
            if not mirror_only:   # range(0): the else runs at once, mirror-only goes on to the mirror
                live.commit()
                sys.exit(f'update stopped at {f.name}; earlier files are applied (and mirrored into live-{env}.db) — re-run update')
        # keep the local mirror equal to D1 so the next diff is right (the mirror has no FTS table)
        live.executescript('\n'.join(x for x in files[i] if 'product_fts' not in x[:40]))
        live.commit()
        log(f'  {i + 1}/{len(files)} {f.name} ok')
    live.close()
    shutil.rmtree(out, ignore_errors=True)
    log(f'live-{env}.db updated (incremental)')


# ---------- report ----------
def report(unmapped=None):
    db = sqlite3.connect(NEXT)
    rep = ROOT / 'reports/sporteka'
    rep.mkdir(parents=True, exist_ok=True)
    lines = [f'# sporteka katalog — {NOW}', '']
    n = db.execute("SELECT COUNT(*), SUM(shop_count > 1) FROM products WHERE status = 'publish'").fetchone()
    lines += [f'- produkty: **{n[0]}**, z toho ve ≥ 2 obchodech **{n[1]}**',
              f'- nabídky: {db.execute("SELECT COUNT(*) FROM offers").fetchone()[0]}, značky: {db.execute("SELECT COUNT(*) FROM brands WHERE noindex = 0").fetchone()[0]} (≥ 3 produkty)', '']
    lines += ['## Obchody', '', '| obchod | produkty |', '|---|---|']
    for d, c in db.execute('SELECT domain, COUNT(*) FROM offers GROUP BY domain ORDER BY 2 DESC'):
        lines.append(f'| {d} | {c} |')
    lines += ['', '## Kategorie (počet, vzorek názvů)', '']
    for cid, slug, name, parent, total in db.execute('SELECT id, slug, name, parent, count_total FROM categories ORDER BY menu_order'):
        ind = '  ' if parent else ''
        sample = [r[0] for r in db.execute('SELECT p.name FROM cat_products x JOIN products p ON p.id = x.product_id WHERE x.cat_id = ? AND x.direct = 1 ORDER BY x.pop DESC LIMIT 4', (cid,))]
        lines.append(f'{ind}- **{name}** `{slug}` {total}' + (f' — {" · ".join(sample)}' if sample else ''))
    if unmapped:
        lines += ['', '## Nezařazené cesty obchodů (top 150)', '']
        for (shop, path), c in unmapped.most_common(150):
            lines.append(f'- {c} · {shop} · {path or "(prázdná)"}')
    f = rep / ('katalog.test.md' if os.environ.get('SPT_NEXT') else 'katalog.local.md')
    f.write_text('\n'.join(lines) + '\n')
    log(f'report → {f}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cmd', choices=['build', 'report', 'push', 'update', 'prices', 'daily', 'adopt', 'all'])
    ap.add_argument('--since', type=float, default=0, help='daily: epoch seconds — only feed files refreshed at or after it count (default: the last 20 h)')
    ap.add_argument('--env', default='production', choices=['local', 'staging', 'production'])
    ap.add_argument('--dry', action='store_true')
    a = ap.parse_args()
    unmapped = None
    if a.cmd in ('build', 'all'):
        unmapped = build(a.env)
    if a.cmd in ('build', 'report', 'all'):
        report(unmapped)
    if a.cmd in ('push', 'all'):
        push(a.env, a.dry)
    if a.cmd in ('update', 'prices'):   # weekly cron: incremental update within the D1 write budget (needs a fresh, uncapped build in next.db)
        push_prices(a.env, a.dry)
    if a.cmd == 'adopt':   # weekly: the new build replaces the mirror (new / gone products, categories, landings)
        adopt(a.env, a.dry)
    if a.cmd == 'daily':   # daily cron: prices + availability of the refreshed feeds only (no build, no new / gone products)
        push_prices(a.env, a.dry, a.since or time.time() - 20 * 3600)


if __name__ == '__main__':
    main()
