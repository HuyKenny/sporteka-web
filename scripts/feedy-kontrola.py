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
# A shop whose download was attempted and failed (e.g. its WAF refuses GitHub's IPs) and that never had a feed file has no
# products on the site, so nothing can be retired: warn and go on. A shop that was not even attempted (missing secret) still stops CI.
try:
    failed = set(json.load(open(APP / 'data/cj/_failed.json')))
except (OSError, ValueError):
    failed = set()
warn = [m for m in missing if m in failed]
missing = [m for m in missing if m not in failed]
if warn:
    print('WARNING: download failed and no feed file yet (shop has no products on the site), skipped:', warn)
if missing:
    print('MISSING feeds:', missing)
    sys.exit(1)
print('all feeds present')
