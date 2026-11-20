#!/usr/bin/env python3
"""sporteka.cz — what the TOP 10 of Google covers and our category text does not (SERP gap, plan 20. 11. 2026).

    python3 scripts/serp-gap.py fetch serp.json      # serp.json: {"keyword": ["url", …]} (Ahrefs serp-overview, CZ)
    python3 scripts/serp-gap.py report serp.json [--out reports/sporteka/serp-gap-2026-11.md]

The SERP itself comes from Ahrefs serp-overview (an MCP tool, no API key in credentials/), saved as JSON by hand.
fetch downloads each competitor page once (polite: one request at a time, plain browser-like UA, 1 s pause, cache in
~/.cache/spt-serp/), report compares per keyword:
  - type of each result (shop listing, comparison site, magazine/guide, marketplace),
  - words and H2/H3 of each result vs our guide + FAQ (src/texts/kategorie.json),
  - subtopics: H2/H3 terms that ≥ 3 results use and our text never mentions,
  - questions in their FAQ / headings ending with "?" that our FAQ lacks.
KEYWORDS maps the phrase to our category slug (B1 of the plan: demand from reports/sporteka/kw/kw-all.json + the
impressions in data/gsc.json, commercial phrases only — "hokej" or "decathlon" are news/navigation queries)."""
import collections
import hashlib
import html
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

import requests

APP = Path(__file__).resolve().parents[1]
CACHE = Path.home() / '.cache' / 'spt-serp'
UA = 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'

KEYWORDS = {
    'kopačky': 'kopacky', 'barefoot boty': 'barefoot-obuv', 'plavky': 'plavky', 'dámské plavky': 'damske-plavky',
    'pánské plavky': 'panske-plavky', 'běžecké boty': 'bezecka-obuv', 'kraťasy': 'sportovni-kratasy', 'tepláky': 'teplaky',
    'mikiny': 'mikiny', 'batohy': 'batohy', 'legíny': 'leginy', 'trekové boty': 'trekova-obuv', 'koloběžky': 'kolobezky',
    'termoprádlo': 'termopradlo', 'stany': 'stany', 'lyžařské brýle': 'lyzarske-bryle', 'lyžařské kalhoty': 'lyzarske-kalhoty',
    'lyžařské bundy': 'lyzarske-bundy', 'sjezdové lyže': 'sjezdove-lyze', 'lyžařské boty': 'lyzarske-boty',
    'lyžařské helmy': 'lyzarske-helmy', 'běžecké lyže': 'bezecke-lyze', 'snowboardy': 'snowboardy', 'inline brusle': 'inline-brusle',
    'boty do vody': 'obuv-do-vody', 'merino ponožky': 'merino-ponozky', 'kreatin': 'kreatin', 'proteiny': 'proteiny',
    'elektrokola': 'elektrokola', 'jízdní kola': 'jizdni-kola', 'boxerské rukavice': 'boxerske-rukavice',
    'brankářské rukavice': 'brankarske-rukavice', 'basketbalové boty': 'basketbalova-obuv', 'holínky': 'holinky',
    'světla na kolo': 'cyklo-svetla', 'fotbalové dresy': 'fotbalove-dresy', 'školní batohy': 'skolni-batohy',
    'zateplené legíny': 'zateplene-leginy', 'lezečky': 'lezecke-boty', 'elektrokoloběžky': 'elektrokolobezky',
    'nafukovací kajak': 'kajaky-a-cluny', 'nesmeky': 'nesmeky', 'boby': 'boby', 'sáně': 'sane-a-boby', 'rotopedy': 'rotopedy',
    'kettlebell': 'kettlebelly', 'hokejky': 'hokejky', 'hokejové brusle': 'hokejove-brusle', 'tenisové rakety': 'tenisove-rakety',
    'softshellové bundy': 'softshellove-bundy', 'spací pytle': 'spaci-pytle', 'turistické batohy': 'turisticke-batohy',
    'cyklistické helmy': 'cyklisticke-helmy', 'trampolíny': 'trampoliny', 'sportovní podprsenky': 'sportovni-podprsenky',
}

STOP = set('a i o u v ve s se z ze k na do pro po od za je jsou to ten ta jak co kde kdy proc nebo ale aby by jako tak '
           'jaky jaka jake jsme jste nas vas jejich vase nase cena ceny nejlepsi top recenze 2024 2025 2026 vse'.split())
fold = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode()).strip()


def kind_of(url):
    u = url.lower()
    if any(x in u for x in ('heureka.', 'zbozi.', 'glami.', 'biano.', 'srovnanicen')):
        return 'srovnávač'
    if any(x in u for x in ('allegro.', 'alza.', 'mall.', 'kaufland.', 'temu.', 'aliexpress')):
        return 'marketplace'
    if any(x in u for x in ('/blog', '/clanek', '/clanky', '/magazin', '/rady', '/poradna', '/jak-', 'idnes.', 'novinky.', 'wikipedia')):
        return 'magazín/průvodce'
    return 'e-shop'


def cached(url):
    return CACHE / (hashlib.sha1(url.encode()).hexdigest() + '.html')


def fetch(serp):
    CACHE.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers.update({'User-Agent': UA, 'Accept-Language': 'cs-CZ,cs;q=0.9'})
    for kw, urls in serp.items():
        for u in urls:
            f = cached(u)
            if f.exists() or 'sporteka.cz' in u:
                continue
            try:
                r = s.get(u, timeout=30)
                f.write_text(r.text if r.ok else '')
                print(r.status_code, u, flush=True)
            except requests.RequestException as e:
                f.write_text('')
                print('ERR', u, e, flush=True)
            time.sleep(1)


def text_of(h):
    h = re.sub(r'<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>', ' ', h or '', flags=re.S | re.I)
    return html.unescape(re.sub(r'<[^>]+>', ' ', h))


def heads(h):
    return [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip() for x in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', h or '', re.S | re.I)]


def terms(s):
    return {w for w in re.findall(r'[a-z0-9]{4,}', fold(s)) if w not in STOP}


def report(serp, out=None):
    texts = json.loads((APP / 'src/texts/kategorie.json').read_text())
    lines = ['# SERP gap kategorií sporteka.cz', '', 'Zdroj SERPu: Ahrefs serp-overview (CZ). Konkurenční stránky stažené jednou, porovnání s `src/texts/kategorie.json`.', '']
    summary = []
    for kw, urls in serp.items():
        slug = KEYWORDS.get(kw, '')
        t = texts.get(slug, {})
        raw = json.loads(t.get('faq_json') or '[]') if isinstance(t.get('faq_json'), str) else (t.get('faq_json') or [])
        faq = [(x['q'], x['a']) if isinstance(x, dict) else (x[0], x[1]) for x in raw]
        ours_html = (t.get('description_html') or '') + (t.get('guide_html') or '') + ' '.join(q + ' ' + a for q, a in faq)
        ours = terms(text_of(ours_html))
        our_words = len(text_of(ours_html).split())
        rows, head_terms, questions = [], collections.Counter(), collections.Counter()
        for pos, u in enumerate(urls, 1):
            f = cached(u)
            h = f.read_text() if f.exists() else ''
            hs = heads(h)
            rows.append(f'| {pos} | {kind_of(u)} | {u[:90]} | {len(text_of(h).split()) if h else "nedostupné (403/chyba)"} | {len(hs)} |')
            for x in set(terms(' '.join(hs))):
                head_terms[x] += 1
            for x in hs:
                if x.endswith('?') and len(x) < 120 and terms(x) & (terms(kw) | terms(slug.replace('-', ' '))):
                    questions[x] += 1
        miss = [w for w, n in head_terms.most_common() if n >= 3 and w not in ours and w not in terms(kw)][:25]
        our_q = {fold(q) for q, _ in faq}
        new_q = [q for q, _ in questions.most_common(15) if fold(q) not in our_q]
        kinds = collections.Counter(kind_of(u) for u in urls)
        summary.append(f'| {kw} | `/{slug}/` | {", ".join(f"{k} {n}" for k, n in kinds.most_common())} | {our_words} | {len(miss)} |')
        lines += [f'## {kw} → `/{slug}/`', '', f'Náš text: {our_words} slov.', '', '| # | typ | URL | slov | H2/H3 |', '|---|---|---|---|---|', *rows, '',
                  '**Podtémata v nadpisech ≥ 3 výsledků, která u nás chybí:** ' + (', '.join(miss) or '—'), '',
                  '**Otázky z nadpisů konkurence, které nemáme ve FAQ:** ' + ('; '.join(new_q) or '—'), '']
    text = '\n'.join(lines[:4] + ['| fráze | stránka | typy v TOP 10 | našich slov | chybějících podtémat |', '|---|---|---|---|---|', *summary, ''] + lines[4:]) + '\n'
    if out:
        Path(out).write_text(text)
    print(text[:4000])


if __name__ == '__main__':
    cmd, path = sys.argv[1], Path(sys.argv[2])
    serp = json.loads(path.read_text())
    if cmd == 'fetch':
        fetch(serp)
    else:
        report(serp, next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == '--out'), None))
