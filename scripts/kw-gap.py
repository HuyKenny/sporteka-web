#!/usr/bin/env python3
"""sporteka.cz — keyword gap: which searched phrases (Marketing Miner, kw-all.json) land in no category or in a catch-all bag.

    scripts/kw-gap.py [min_volume=150] [out.md]

Each phrase is run through kategorie.categorize as if it were a product title. Unmapped phrases and phrases that fall into a
catch-all category are grouped by their head words → candidate new categories (volume, example phrases)."""
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kategorie as K  # noqa: E402

MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 150
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('/home/kenny/ai/reports/sporteka/kw/kategorie-gap.md')
BAGS = {'kempingove-doplnky', 'outdoor-doplnky', 'cyklo-prislusenstvi', 'fitness-pomucky', 'ostatni-micove-sporty', 'rybarske-doplnky', 'hry-na-zahradu',
        'lyzarske-doplnky', 'cyklo-dily', 'plazove-doplnky', 'plavecke-pomucky', 'sportovni-tasky', 'jezdecke-doplnky', 'golfove-doplnky',
        'lovecke-vybaveni', 'ostatni-doplnky-stravy', 'sportovni-bryle', 'lahve-a-termosky', 'cepice-a-celenky', 'tenisky'}
# noise: not products (results, TV, clubs, news) — dropped before grouping
NOISE = re.compile(r'\b(dnes|zive|live|vysledky|tabulka|program|prenos|online|stream|zapas|liga|mistrovstvi|fortuna|tipsport|kurzy|sazky|film|hra|hry|navod|pravidla|'
                   r'cena|ceny|akce|sleva|slevy|levne|eshop|obchod|shop|praha|brno|ostrava|plzen|cz|sk|youtube|wiki|forum|recenze|test|zkusenosti)\b')
STOP = set('pro na do od z ze a i s se k v ve the'.split())
rows = json.load(open('/home/kenny/ai/reports/sporteka/kw/kw-all.json'))
unm, bag = collections.defaultdict(list), collections.defaultdict(list)
tot_unm = tot_bag = ok = 0
for r in rows:
    if r['volume'] < MIN:
        continue
    kw = r['keyword']
    if NOISE.search(K.fold(kw)):
        continue
    cat, _ = K.categorize('', kw)
    if not cat:
        unm[kw] = r['volume']; tot_unm += 1
    elif cat in BAGS:
        bag[cat].append((kw, r['volume'])); tot_bag += 1
    else:
        ok += 1
lines = [f'# Kategorie × klíčová slova (min. objem {MIN})', '', f'Zařazeno do konkrétní kategorie: {ok}, v „pytlíku“: {tot_bag}, nezařazeno: {tot_unm}', '']
# group unmapped by last meaningful word (the head noun is usually first or last in Czech product phrases)
groups = collections.defaultdict(list)
for kw, v in unm.items():
    w = [x for x in re.findall(r'[a-zěščřžýáíéúůďťňó]{4,}', kw.lower()) if x not in STOP]
    if w:
        groups[w[0]].append((kw, v))
        if len(w) > 1:
            groups[w[-1]].append((kw, v))
lines.append('## Nezařazené fráze podle klíčového slova')
for w, lst in sorted(groups.items(), key=lambda x: -sum(v for _, v in set(x[1])))[:120]:
    lst = sorted(set(lst), key=lambda x: -x[1])
    lines.append(f'- **{w}** ({sum(v for _, v in lst)}): ' + ', '.join(f'{k} {v}' for k, v in lst[:8]))
lines += ['', '## Fráze v „pytlících“ (kandidáti na podkategorii)']
for c, lst in sorted(bag.items(), key=lambda x: -sum(v for _, v in x[1])):
    lst.sort(key=lambda x: -x[1])
    lines.append(f'- **{c}** ({sum(v for _, v in lst)}): ' + ', '.join(f'{k} {v}' for k, v in lst[:14]))
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'ok {ok}, bag {tot_bag}, unmapped {tot_unm} → {OUT}')
