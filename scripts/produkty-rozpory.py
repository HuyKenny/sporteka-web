#!/usr/bin/env python3
"""sporteka.cz — contradictions between a product's name and its shown parameters (quality audit, 20. 11. 2026).

    python3 scripts/produkty-rozpory.py [db=data/live-production.db] [--out reports/…md]

Google's core update of 11/2026 treats a feed catalogue as scaled content; a page that says "červená" in the H1 and
"Barva: Černá" in the table is the kind of error a quality rater flags. Checks on indexable products with offers:
  barva  the colour named at the end of the name (", červená") vs the 'barva' parameter
  pro    pánská/dámská/dětská in the name vs the 'pro' parameter
Prints counts per check and per shop, plus examples. katalog.py name_colors() is the fix for barva."""
import collections
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import katalog as KT  # noqa: E402  (color_of, name_colors)

APP = Path(__file__).resolve().parents[1]
OUT = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == '--out'), None)
args = [a for a in sys.argv[1:] if not a.startswith('--') and a != OUT]
DB = Path(args[0]) if args else APP / 'data' / 'live-production.db'

def main():
    c = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    params = collections.defaultdict(dict)
    for pid, k, v in c.execute("SELECT product_id, key, value FROM product_params WHERE key IN ('barva', 'pro')"):
        params[pid].setdefault(k, set()).add(v)
    rows = c.execute("SELECT id, slug, name, noindex, (SELECT domain FROM offers o WHERE o.product_id = p.id AND o.active = 1 ORDER BY price LIMIT 1) "
                     "FROM products p WHERE status = 'publish' AND offer_count > 0").fetchall()
    n = {'all': 0, 'idx': 0}
    bad = collections.defaultdict(list)
    per_shop = collections.Counter()
    for pid, slug, name, noindex, dom in rows:
        n['all'] += 1
        n['idx'] += not noindex
        ncs = KT.name_colors(name)
        bc = params[pid].get('barva', set())
        if ncs and bc and not bc & set(ncs):
            bad['barva'].append((noindex, slug, name, '/'.join(sorted(bc)), '/'.join(ncs)))
            per_shop[dom] += 1
        ng = KT.name_gender(name)
        pg = params[pid].get('pro', set())
        if ng and pg and ng not in pg and 'Unisex' not in pg:
            bad['pro'].append((noindex, slug, name, '/'.join(sorted(pg)), ng))
    lines = [f'# Rozpory název × parametry ({DB.name})', '',
             f"Produktů s nabídkou: {n['all']:,}, indexovatelných: {n['idx']:,}".replace(',', ' '), '',
             '| kontrola | rozporů celkem | z toho indexovatelných |', '|---|---|---|']
    for k in ('barva', 'pro'):
        lines.append(f"| {k} | {len(bad[k])} | {sum(1 for b in bad[k] if not b[0])} |")
    lines += ['', '## Barva podle obchodu (nejlevnější nabídka)', ''] + [f'- {d}: {x}' for d, x in per_shop.most_common(15)]
    for k in ('barva', 'pro'):
        lines += ['', f'## Příklady: {k}', '']
        lines += [f'- `/{s}/` {nm} — parametr {pv}, v názvu {nv}' for _, s, nm, pv, nv in sorted(bad[k], key=lambda b: b[0])[:25]]
    text = '\n'.join(lines) + '\n'
    if OUT:
        Path(OUT).write_text(text)
    print(text)


if __name__ == '__main__':
    main()
