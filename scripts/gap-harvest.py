#!/usr/bin/env python3
"""sporteka.cz — content gap from Marketing Miner (CZ): keywords that competitors rank for and sporteka.cz does not.

    scripts/gap-harvest.py                 # website_content_gap for every competitor below (one call each, cached)
    scripts/gap-harvest.py --report        # merge the cache -> src/data/kw/kw-gap.json (keyword, volume, competitors [domain, position, url])

One call returns at most 100 rows (the biggest by volume), so every competitor is asked on its own; the seed list for the next
step (kw-harvest.py --seeds) comes from the unmapped heads of these phrases. Cache: reports/sporteka/gap/<domain>.json.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, '/home/kenny/ai/bin')
import mm  # noqa: E402

CACHE = Path('/home/kenny/ai/reports/sporteka/gap')
OUT = Path(__file__).resolve().parent.parent / 'src/src/data/kw/kw-gap.json'
COMPETITORS = ['sportisimo.cz', 'decathlon.cz', 'intersport.cz', 'insportline.cz', '4camping.cz', 'hudy.cz', 'sportega.cz', 'mastersport.cz',
               'sportano.cz', 'altisport.cz', 'a3sport.cz', 'sportvision.cz', 'exisport.cz', 'martessport.eu', 'sportsdirect.cz', 'hervis.cz',
               'sportobchod.cz', '4fstore.cz', 'bezvasport.cz', 'top4running.cz', 'd-sport.cz', 'rockpoint.cz', 'gymbeam.cz', 'aminostar.cz',
               'heureka.cz', 'zbozi.cz', 'glami.cz', 'footshop.cz', 'eobuv.cz']


def fetch(domain):
    f = CACHE / f'{domain}.json'
    if f.exists():
        return json.loads(f.read_text())
    for attempt in range(4):
        try:
            d = mm.call('website_content_gap', {'lang': 'cs', 'type': 'domain', 'target': 'sporteka.cz', 'other_domain_1': domain, 'limit': 100})
            rows = d['data']['websites']
            f.write_text(json.dumps(rows, ensure_ascii=False))
            return rows
        except BaseException as e:  # noqa: BLE001 — mm.rpc exits with the error JSON
            print(f'  {domain}: attempt {attempt + 1} failed: {str(e)[:150]}', file=sys.stderr)
            time.sleep(15 * (attempt + 1))
    return None


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    if '--report' not in sys.argv:
        for d in COMPETITORS:
            rows = fetch(d)
            print(f'{d}: {len(rows) if rows is not None else "FAILED"} rows', flush=True)
            time.sleep(2)
    merged = {}
    for f in sorted(CACHE.glob('*.json')):
        for r in json.loads(f.read_text()):
            m = merged.setdefault(r['keyword'], {'keyword': r['keyword'], 'volume': r['search_volume'], 'comp': []})
            m['comp'] += [[i['domain'], i['position'], i['url']] for i in r['items']]
    out = sorted(merged.values(), key=lambda x: -x['volume'])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False))
    print(f'{len(out)} keywords -> {OUT}')


if __name__ == '__main__':
    main()
