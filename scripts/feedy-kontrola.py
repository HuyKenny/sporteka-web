#!/usr/bin/env python3
"""sporteka.cz — gate before a catalogue build: every enabled shop must have its downloaded feed file.

A build with a missing feed would retire all products of that shop (and 301 them away), so CI stops here instead.
Shops that are known to have no products in their feed (CJ lists them, the API returns 0) are tolerated.

    python3 -I scripts/feedy-kontrola.py        # exit 1 and a list when feeds are missing
"""
import json
import os
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
KNOWN_EMPTY = {'4352963', '4786110'}   # Footshop, 4camping: in CJ with productCount > 0, API returns nothing
shops = json.load(open(APP / 'src/data/obchody.json'))['shops']
missing = [s['advertiserId'] for s in shops if s.get('enabled') and s['advertiserId'] not in KNOWN_EMPTY
           and not (APP / 'data/cj' / f"{s['advertiserId']}.jsonl.gz").exists()]
print(f"enabled shops {sum(1 for s in shops if s.get('enabled'))}, feed files {len(list((APP / 'data/cj').glob('*.jsonl.gz')))}")
if missing:
    print('MISSING feeds:', missing)
    sys.exit(1)
print('all feeds present')
