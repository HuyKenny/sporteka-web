#!/usr/bin/env python3
"""sporteka.cz — merge hand-written brand-page texts (scripts/znacky_vlna*.py, NEW[slug] = dict(title, desc, intro, guide, faq)) into
src/texts/znacky.json (used by src/lib/views.ts instead of the template texts). No D1 write — only a deploy.
Usage: python3 scripts/znacky-export.py [--check]
Rules: title <= 60, desc <= 155, intro 100-200 words, guide >= 1000 words, intro+guide+FAQ >= 1500 words, FAQ >= 9, links only to existing
categories / landings / brands, no prices or counts, no sentence (> 60 chars) repeated in another landing or in a category text."""
import collections, importlib, json, pathlib, re, sqlite3, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent
OUT = ROOT / 'src/texts/znacky.json'
CHECK = '--check' in sys.argv
facets = set(json.loads((ROOT / 'src/texts/fasety.json').read_text(encoding='utf-8')))
cslugs = set(json.loads((ROOT / 'src/texts/kategorie.json').read_text(encoding='utf-8')))
bslugs = set((HERE / 'znacky_slugy.txt').read_text().split())
key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
new = {}
for mod in sorted((p.stem for p in HERE.glob('znacky_vlna[0-9]*.py')), key=key):
    new.update(importlib.import_module(mod).NEW)
txt = lambda h: re.sub(r'<[^>]+>', ' ', h or '')
words = lambda h: len(txt(h).split())
sent = collections.defaultdict(set)
for slug, e in json.loads((ROOT / 'src/texts/kategorie.json').read_text(encoding='utf-8')).items():
    for s in re.split(r'(?<=[.!?])\s+', txt(e.get('description_html', '') + ' ' + e.get('guide_html', ''))):
        if len(s) > 60:
            sent[s.strip()].add('cat:' + slug)
for slug, e in json.loads((ROOT / 'src/texts/fasety.json').read_text(encoding='utf-8')).items():
    for s in re.split(r'(?<=[.!?])\s+', txt(e.get('description_html', '') + ' ' + e.get('guide_html', ''))):
        if len(s) > 60:
            sent[s.strip()].add('cat:f-' + slug)
errors, report = [], []
for slug, e in new.items():
    if slug not in bslugs:
        errors.append(f'{slug}: not a brand'); continue
    for f in ('title', 'desc', 'intro', 'guide', 'faq'):
        if f not in e:
            errors.append(f'{slug}: missing {f}')
    if len(e['title']) > 60: errors.append(f'{slug}: title {len(e["title"])} > 60')
    if len(e['desc']) > 155: errors.append(f'{slug}: desc {len(e["desc"])} > 155')
    wi, wg = words(e['intro']), words(e['guide'])
    wt = wi + wg + sum(words(q) + words(a) for q, a in e['faq'])
    if not 100 <= wi <= 200: errors.append(f'{slug}: intro {wi} words')
    if wg < 1000: errors.append(f'{slug}: guide {wg} words')
    if wt < 1500: errors.append(f'{slug}: total {wt} words < 1500')
    if len(e['faq']) < 8: errors.append(f'{slug}: only {len(e["faq"])} FAQ (<8)')
    full = e['intro'] + e['guide'] + ' '.join(q + ' ' + a for q, a in e['faq'])
    for h in re.findall(r'href="/([a-z0-9-]+)/"', e['intro'] + e['guide']):
        if h not in cslugs and h not in facets: errors.append(f'{slug}: link to unknown /{h}/')
    for h in re.findall(r'href="/znacka/([a-z0-9-]+)/"', e['intro'] + e['guide']):
        if h not in bslugs: errors.append(f'{slug}: link to unknown brand {h}')
    if len(set(re.findall(r'href="/([a-z0-9-]+)/"', e['intro'] + e['guide']))) < 8: errors.append(f'{slug}: fewer than 8 internal links')
    if re.search(r'\d[\d\s]*\s?(Kč|CZK|€)', txt(full)): errors.append(f'{slug}: price in text')
    if re.search(r'<(script|iframe|style)|on\w+=', full): errors.append(f'{slug}: forbidden HTML')
    for s in re.split(r'(?<=[.!?])\s+', txt(e['intro'] + ' ' + e['guide'])):
        if len(s) > 60: sent[s.strip()].add(slug)
    report.append((slug, wi, wg, wt, len(e['faq'])))
for s, c in sent.items():
    if len(c) > 1 and any(not x.startswith('cat:') for x in c):
        errors.append(f'sentence repeated in {sorted(c)}: {s[:70]}…')
print(f'{"landing":32} intro guide total faq')
for r in report: print(f'{r[0]:32} {r[1]:5} {r[2]:5} {r[3]:5} {r[4]:3}')
if errors:
    print('\nERRORS:'); print('\n'.join(' - ' + x for x in errors)); sys.exit(1)
if CHECK:
    print(f'\nOK (check only), {len(new)} brands'); sys.exit(0)
out = {s: dict(seo_title=e['title'], seo_desc=e['desc'], description_html=e['intro'], guide_html=e['guide'],
               faq_json=json.dumps([{'q': q, 'a': a} for q, a in e['faq']], ensure_ascii=False)) for s, e in new.items()}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(f'\nwrote {len(out)} brand texts → {OUT}')
