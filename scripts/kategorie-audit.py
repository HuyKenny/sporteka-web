#!/usr/bin/env python3
"""sporteka.cz — audit of the category rules on the real feeds (no DB, no build).

    scripts/kategorie-audit.py [N] [out.md]     # every N-th feed row (default 6) → report with counts and sample titles per category

For each category: row count, 14 random sample titles (shop · title · feed path) and — for the catch-all categories
(doplnky / příslušenství / ostatní) — the most frequent head words of the titles, which is where new sub-categories come from
(this is how "stanové kolíky" was found). Review the samples: anything that does not belong is a rule to fix in kategorie.py.
"""
import collections
import gzip
import json
import random
import re
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP / 'scripts'))
import kategorie as K  # noqa: E402

N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('/home/kenny/ai/reports/sporteka/kategorie-audit.md')
CATCH_ALL = {'kempingove-doplnky', 'outdoor-doplnky', 'cyklo-prislusenstvi', 'fitness-pomucky', 'ostatni-micove-sporty', 'rybarske-doplnky',
             'hry-na-zahradu', 'lyzarske-doplnky', 'cyklo-dily', 'plazove-doplnky', 'plavecke-pomucky', 'sportovni-tasky', 'jezdecke-doplnky',
             'golfove-doplnky', 'lovecke-vybaveni', 'ostatni-doplnky-stravy'}
STOP = set('a i na pro s se z ze do od k o u v ve the and of set sada ks cm mm kg ml g l xl xs m s'.split())
rnd = random.Random(1)
shops = json.load(open(APP / 'src/data/obchody.json'))['shops']
by = collections.defaultdict(list)
prices = collections.defaultdict(list)   # slug → [(price, shop, title)] for the price-desc check
cnt = collections.Counter()
total = unmapped = 0
heads = collections.defaultdict(collections.Counter)
for sh in shops:
    f = APP / 'data/cj' / f"{sh['advertiserId']}.jsonl.gz"
    if not sh.get('enabled') or not f.exists():
        continue
    for i, line in enumerate(gzip.open(f, 'rt', encoding='utf-8')):
        if i % N:
            continue
        r = json.loads(line)
        total += 1
        path = (r.get('pt') or [''])[0]
        own = (r.get('seller') or 'Decathlon') == 'Decathlon'
        cat, _ = K.categorize_ctx(path, r['t'], r.get('gpc', ''), r.get('sport', ''), r.get('nature', ''), own)
        if not cat:
            unmapped += 1
            continue
        cnt[cat] += 1
        try:
            pr = float(r.get('sp') or r.get('p') or 0)
        except ValueError:
            pr = 0.0
        prices[cat].append((pr, sh['name'], r['t'][:70]))
        if len(by[cat]) < 400:
            by[cat].append((sh['name'], r['t'][:80], path[:60]))
        if cat in CATCH_ALL:
            w = [x for x in re.findall(r'[a-zěščřžýáíéúůďťňó]{4,}', K.fold(r['t'])) if x not in STOP]
            if w:
                heads[cat][w[0]] += 1
                heads[cat][w[1] if len(w) > 1 else w[0]] += 1
lines = [f'# Audit kategorií (každý {N}. řádek, {total} řádků, nezařazeno {unmapped})', '']
for slug, n in cnt.most_common():
    lines.append(f'## {slug} — {K.BY_SLUG[slug][2]} ({n} × {N})')
    for sh, t, p in rnd.sample(by[slug], min(14, len(by[slug]))):
        lines.append(f'- {sh} · {t} · _{p}_')
    if slug in heads:
        lines.append('- **top slova:** ' + ', '.join(f'{w} {c}' for w, c in heads[slug].most_common(25)))
    lines.append('')
# priciest items per category after the build's price sanity (katalog.py PRICE_FLOOR) — wrong items hide at the top of "price descending"
import statistics  # noqa: E402
FLOOR = {'sportovni-obleceni': 30000, 'merino': 30000, 'sportovni-obuv': 22000, 'sportovni-vyziva': 6000, 'rybareni': 45000}
lines.append('# Nejdražší produkty v kategoriích (po cenových limitech)')
for slug, n in cnt.most_common(70):
    pl = sorted(prices[slug], reverse=True)
    if K.section(slug) in FLOOR:
        med = statistics.median(x[0] for x in pl)
        pl = [x for x in pl if x[0] <= max(FLOOR[K.section(slug)], 40 * med)]
    if slug in ('cyklo-prislusenstvi', 'cyklo-dily'):
        pl = [x for x in pl if x[0] < 15000]
    lines.append(f'## {slug}')
    lines += [f'- {x[0]:.0f} · {x[1]} · {x[2]}' for x in pl[:6]]
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'{total} rows, unmapped {unmapped}, {len(cnt)} categories → {OUT}')
