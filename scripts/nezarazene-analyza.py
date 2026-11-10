#!/usr/bin/env python3
"""sporteka.cz — what is in the feeds but in no category (sport-ish only), grouped by shop path and by head words of titles.

    scripts/nezarazene-analyza.py [N=3] [out.md]     # every N-th feed row

Skips fashion shops' non-sport rows (katalog.py FASHION_SHOPS logic is not repeated here: only rows with SPORTY words or
from sport shops are listed). Output: top unmapped paths (shop · path · count · sample titles) and top head words → new category candidates."""
import collections
import gzip
import json
import re
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP / 'scripts'))
import kategorie as K  # noqa: E402

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('/home/kenny/ai/reports/sporteka/nezarazene-analyza.md')
FASHION = {'Bezvasport cz/sk', 'Answear.cz', 'Spartoo.cz', 'Kokiskashop.cz', 'Allegro.cz', 'Lekarna.cz', 'Benu.cz'}
STOP = set('a i na pro s se z ze do od k o u v ve the and of set sada ks cm mm kg ml g l xl xs m panske damske detske unisex pansky damsky detsky'.split())
shops = json.load(open(APP / 'src/data/obchody.json'))['shops']
paths = collections.defaultdict(lambda: [0, []])
heads = collections.defaultdict(lambda: [0, []])
tot = un = 0
for sh in shops:
    f = APP / 'data/cj' / f"{sh['advertiserId']}.jsonl.gz"
    if not sh.get('enabled') or not f.exists():
        continue
    fashion = sh['name'] in FASHION
    for i, line in enumerate(gzip.open(f, 'rt', encoding='utf-8')):
        if i % N:
            continue
        r = json.loads(line)
        tot += 1
        path = (r.get('pt') or [''])[0]
        own = (r.get('seller') or 'Decathlon') == 'Decathlon'
        cat, _ = K.categorize_ctx(path, r['t'], r.get('gpc', ''), r.get('sport', ''), r.get('nature', ''), own)
        if cat:
            continue
        ft = K.fold(r['t'] + ' ' + path)
        if fashion and not K.SPORTY.search(ft):
            continue
        un += 1
        key = (sh['name'], path[:70])
        p = paths[key]; p[0] += 1
        if len(p[1]) < 4:
            p[1].append(r['t'][:50])
        w = [x for x in re.findall(r'[a-zěščřžýáíéúůďťňó]{4,}', K.fold(r['t'])) if x not in STOP]
        if w:
            h = heads[w[0]]; h[0] += 1
            if len(h[1]) < 3:
                h[1].append(f"{sh['name']}: {r['t'][:45]}")
lines = [f'# Nezařazené sportovní řádky (každý {N}.; {tot} řádků, nezařazeno {un})', '', '## Cesty obchodů', '']
for (s, p), (n, ex) in sorted(paths.items(), key=lambda x: -x[1][0])[:150]:
    lines.append(f'- {n} · {s} · _{p}_ · ' + ' / '.join(ex))
lines += ['', '## První slova názvů', '']
for w, (n, ex) in sorted(heads.items(), key=lambda x: -x[1][0])[:150]:
    lines.append(f'- **{w}** {n} · ' + ' / '.join(ex))
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(tot, un, '→', OUT)
