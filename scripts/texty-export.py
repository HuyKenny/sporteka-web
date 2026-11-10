#!/usr/bin/env python3
"""sporteka.cz — merge the hand-written category texts (scripts/texty_vlna*.py) into src/texts/kategorie.json.

The file overrides the database columns when a category is rendered (src/lib/db.ts loadCategory), so changing a text costs no D1
write — only a deploy. Run after editing a texty_vlna*.py file, then commit and deploy:

    python3 -I scripts/texty-export.py            # validate and write
    python3 -I scripts/texty-export.py --check    # validate only

Checks: the slug exists in the tree, every internal link points to an existing category, title ≤ 60, description ≤ 155,
intro and guide have enough words, at least 5 FAQ items, no sentence repeated across categories."""
import collections
import importlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kategorie as K  # noqa: E402

OUT = HERE.parent / 'src/texts/kategorie.json'
CHECK = '--check' in sys.argv
MIN_INTRO, MAX_INTRO, MIN_GUIDE = 100, 200, 450

slugs = {t[1] for t in K.TREE}
new = {}
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)       # numeric wave order: later waves override earlier ones
for mod in sorted((p.stem for p in HERE.glob('texty_vlna[0-9]*[a-wyz].py')), key=_key):
    new.update(importlib.import_module(mod).NEW)
extra = {}
for mod in sorted(p.stem for p in HERE.glob('texty_vlna[0-9]*x.py')):      # longer intro + extra guide sections, appended to the entries above
    extra.update(importlib.import_module(mod).EXTRA)
for slug, x in extra.items():
    if slug in new and not new[slug].get('long'):      # long texts already contain everything
        new[slug] = {**new[slug], 'intro': new[slug]['intro'] + x.get('intro', ''), 'guide': new[slug]['guide'] + x.get('guide', '')}

words = lambda h: len(re.sub(r'<[^>]+>', ' ', h).split())
errors, report = [], []
sent = collections.defaultdict(set)
for slug, e in new.items():
    if slug not in slugs:
        errors.append(f'{slug}: not in the category tree')
        continue
    for field in ('title', 'desc', 'intro', 'guide', 'faq'):
        if field not in e:
            errors.append(f'{slug}: missing {field}')
    if len(e['title']) > 60:
        errors.append(f'{slug}: title {len(e["title"])} > 60')
    if len(e['desc']) > 155:
        errors.append(f'{slug}: description {len(e["desc"])} > 155')
    wi, wg = words(e['intro']), words(e['guide'])
    lo_i, lo_g = (50, 220) if e.get('short') else (MIN_INTRO, MIN_GUIDE)
    if e.get('long'):                      # Kenny 4. 11. 2026: >= 1500 words of visible text per category
        lo_i, lo_g = MIN_INTRO, 1000
        wt = wi + wg + sum(words(q) + words(a) for q, a in e['faq'])
        if wt < 1500:
            errors.append(f'{slug}: total {wt} words < 1500')
    if not lo_i <= wi <= MAX_INTRO:
        errors.append(f'{slug}: intro {wi} words')
    if wg < lo_g:
        errors.append(f'{slug}: guide {wg} words')
    if len(e['faq']) < 5:
        errors.append(f'{slug}: only {len(e["faq"])} FAQ')
    for html in (e['intro'], e['guide']):
        for href in re.findall(r'href="/([a-z0-9-]+)/"', html):
            if href not in slugs:
                errors.append(f'{slug}: link to unknown category /{href}/')
        if re.search(r'<(script|iframe|style)|on\w+=', html):
            errors.append(f'{slug}: forbidden HTML')
    for s in re.split(r'(?<=[.!?])\s+', re.sub(r'<[^>]+>', ' ', e['intro'] + ' ' + e['guide'])):
        if len(s) > 60:
            sent[s.strip()].add(slug)
    report.append((slug, len(e['title']), len(e['desc']), wi, wg, len(e['faq'])))
for s, cats in sent.items():
    if len(cats) > 1:
        errors.append(f'sentence repeated in {sorted(cats)}: {s[:70]}…')

print(f'{"category":24} title desc intro guide faq')
for r in report:
    print(f'{r[0]:24} {r[1]:5} {r[2]:4} {r[3]:5} {r[4]:5} {r[5]:3}')
if errors:
    print('\nERRORS:')
    print('\n'.join(' - ' + x for x in errors))
    sys.exit(1)
if CHECK:
    print('\nOK (check only)')
    sys.exit(0)
data = json.loads(OUT.read_text(encoding='utf-8'))
for slug, e in new.items():
    d = data.setdefault(slug, {})
    d.update(description_html=e['intro'], guide_html=e['guide'], seo_title=e['title'], seo_desc=e['desc'],
             faq_json=json.dumps([{'q': q, 'a': a} for q, a in e['faq']], ensure_ascii=False))
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'\nwrote {len(new)} categories → {OUT}')
