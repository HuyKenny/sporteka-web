#!/usr/bin/env python3
"""sporteka.cz — seasonal guides (Kenny 16. 11. 2026): scripts/pruvodce_vlna*.py → src/texts/pruvodce.json (src/lib/guides.ts).

    python3 -I scripts/pruvodce-export.py            # validate + write
    python3 -I scripts/pruvodce-export.py --check    # validate only

A module defines GUIDES = {slug: dict(name, h1, seo_title, seo_desc, intro_html, sections=[dict(h2, html, cat, n)],
faq=[(question, answer_html)], cats=[...], updated='YYYY-MM-DD')}. Checks: >= 1500 words of visible text, every section
category and every internal link exists (category, facet landing with a text, brand, guide, fixed page), title <= 65 and
description 120-160 characters, no repeated sentence. Later waves override earlier ones (numeric order)."""
import html
import importlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
APP = HERE.parent
sys.path.insert(0, str(HERE))
import kategorie as K  # noqa: E402

CHECK = '--check' in sys.argv
OUT = APP / 'src/texts/pruvodce.json'
FIELDS = {'name', 'h1', 'seo_title', 'seo_desc', 'intro_html', 'sections', 'faq', 'updated'}


def wave_key(p):
    m = re.match(r'pruvodce_vlna(\d+)([a-z]*)', p.stem)
    return (int(m.group(1)), m.group(2)) if m else (0, '')


guides = {}
for p in sorted(HERE.glob('pruvodce_vlna[0-9]*.py'), key=wave_key):
    guides.update(importlib.import_module(p.stem).GUIDES)

cats = {slug for _, slug, _, _ in K.TREE}
facets = set(json.loads((APP / 'src/texts/fasety.json').read_text()))
brands = set(json.loads((APP / 'src/texts/znacky.json').read_text()))
fixed = {'', 'slevy', 'obchody', 'kategorie', 'jak-srovnavame'}
words = lambda h: len(html.unescape(re.sub(r'<[^>]+>', ' ', h)).split())
errors, out = [], {}
for slug, g in guides.items():
    miss = FIELDS - set(g)
    if miss:
        errors.append(f'{slug}: missing {sorted(miss)}')
        continue
    body = g['intro_html'] + ''.join(s['h2'] + s['html'] for s in g['sections']) + ''.join(q + a for q, a in g['faq'])
    n = words(body)
    if n < 1500:
        errors.append(f'{slug}: {n} words (< 1500)')
    if len(g['seo_title']) > 65:
        errors.append(f'{slug}: title {len(g["seo_title"])} chars > 65')
    if not 120 <= len(g['seo_desc']) <= 160:
        errors.append(f'{slug}: description {len(g["seo_desc"])} chars (120-160)')
    for s in g['sections']:
        if s.get('cat') and s['cat'] not in cats:
            errors.append(f'{slug}: section category {s["cat"]} does not exist')
    for c in g.get('cats', []):
        if c not in cats:
            errors.append(f'{slug}: cats {c} does not exist')
    for href in re.findall(r'href="([^"]+)"', body):
        if href.startswith(('http://', 'https://', 'mailto:', '#')):
            if 'sporteka.cz' in href:
                errors.append(f'{slug}: absolute own link {href}')
            continue
        m = re.fullmatch(r'/(?:znacka/([a-z0-9-]+)/|([a-z0-9-]*)/?)', href)
        if not m:
            errors.append(f'{slug}: odd link {href}')
        elif m.group(1) is not None:
            if m.group(1) not in brands:
                errors.append(f'{slug}: brand link /znacka/{m.group(1)}/ has no brand text (may be noindex)')
        elif m.group(2) not in cats | facets | set(guides) | fixed:
            errors.append(f'{slug}: link {href} goes nowhere known')
    sent = [x.strip() for x in re.split(r'(?<=[.!?])\s+', html.unescape(re.sub(r'<[^>]+>', ' ', body))) if len(x.strip()) > 40]
    dup = {x for x in sent if sent.count(x) > 1}
    if dup:
        errors.append(f'{slug}: repeated sentences {list(dup)[:2]}')
    out[slug] = {'name': g['name'], 'h1': g['h1'], 'seo_title': g['seo_title'], 'seo_desc': g['seo_desc'], 'intro_html': g['intro_html'],
                 'sections': [{k: v for k, v in s.items() if k in ('h2', 'html', 'cat', 'n')} for s in g['sections']],
                 'faq_json': json.dumps([{'q': q, 'a': a} for q, a in g['faq']], ensure_ascii=False), 'updated': g['updated'], 'cats': g.get('cats', [])}
    print(f'{slug:28} {n:5} words, {len(g["sections"])} sections, {len(g["faq"])} FAQ')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
if CHECK:
    print('\nOK (check only)')
else:
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(f'\n{len(out)} guides → {OUT.relative_to(APP)}')
