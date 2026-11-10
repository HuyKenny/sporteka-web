#!/usr/bin/env python3
"""sporteka.cz — where does the product's NAME say one thing and its category another?

    scripts/kategorie-konflikty.py [db] [out.md]      # default: data/live-production.db → reports/sporteka/kategorie-konflikty.md

Every published product is categorised again from its title alone and compared with the category it sits in. Pairs (actual → by title)
that differ and are not parent/child are counted; the biggest pairs are one systematic rule problem each (that is how "Posilovací kolo"
in bicycles, "Mazivo na řetěz" in bicycles, skis in footwear would have shown up). Samples of 3 titles per pair.
"""
import collections
import sqlite3
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP / 'scripts'))
import kategorie as K  # noqa: E402

DB = Path(next((a for a in sys.argv[1:] if a.endswith('.db')), APP / 'data/live-production.db'))
OUT = Path(next((a for a in sys.argv[1:] if a.endswith('.md')), '/home/kenny/ai/reports/sporteka/kategorie-konflikty.md'))
db = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
cats = {i: s for i, s in db.execute('SELECT id, slug FROM categories')}


def lineage(slug):
    out = set()
    t = K.BY_SLUG.get(slug)
    while t:
        out.add(t[1])
        t = K.BY_SLUG.get(t[3]) if t[3] else None
    return out


pairs, samples, total = collections.Counter(), collections.defaultdict(list), 0
for name, cid in db.execute("SELECT name, primary_cat FROM products WHERE status = 'publish'"):
    total += 1
    cur = cats.get(cid)
    if not cur or cur not in K.BY_SLUG:
        continue
    by, _ = K.categorize('', name, '')
    if not by or by == cur:
        continue
    if by in lineage(cur) or cur in lineage(by):
        continue
    pairs[(cur, by)] += 1
    if len(samples[(cur, by)]) < 3:
        samples[(cur, by)].append(name[:80])
lines = [f'# Konflikty název × kategorie ({total} produktů, {sum(pairs.values())} rozporů)', '']
for (cur, by), n in pairs.most_common(120):
    lines.append(f'- **{cur} → {by}** × {n}: ' + ' | '.join(samples[(cur, by)]))
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'{total} products, {sum(pairs.values())} conflicts, {len(pairs)} pairs → {OUT}')
