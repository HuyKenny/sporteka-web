#!/usr/bin/env python3
"""sporteka.cz — Marketing Miner keyword harvest (CZ) for categories and facet landings.

    scripts/kw-harvest.py                 # seeds = every category name + EXTRA seeds, cached in reports/sporteka/kw/<seed>.json
    scripts/kw-harvest.py --only slug     # one category
    scripts/kw-harvest.py --seeds-file F  # seeds from a file (one per line) instead of the category names
    scripts/kw-harvest.py --report        # merge the cache → reports/sporteka/kw/kw-all.json (keyword, volume, seed) sorted by volume

Uses bin/mm.py's session (keyword_suggestions: related searches with monthly volume). Calls are cached per seed and run
one by one (the MCP server throttles); re-running only fetches seeds that are missing.
"""
import hashlib
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, '/home/kenny/ai/bin')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mm  # noqa: E402
import kategorie as K  # noqa: E402

KW = Path('/home/kenny/ai/reports/sporteka/kw')
KW.mkdir(parents=True, exist_ok=True)
# things that have (or should get) a category but whose name is not what people type
EXTRA = [
    'stanové kolíky', 'protein', 'syrovátkový protein', 'kreatin', 'bcaa', 'gainer', 'spalovač tuků', 'energetický gel', 'iontový nápoj', 'proteinová tyčinka',
    'merino triko', 'merino ponožky', 'merino spodní prádlo', 'termoprádlo', 'powerbanka na turistiku', 'čelovka', 'trekové hole', 'spacák', 'karimatka', 'stan',
    'jóga podložka', 'jóga cvičení pomůcky', 'pilates', 'baletní piškoty', 'taneční boty', 'gymnastika', 'jezdecké rajtky', 'jezdecká helma', 'golfové hole',
    'golfové míčky', 'lovecké oblečení', 'dalekohled', 'padel raketa', 'squash raketa', 'kompas', 'lékárnička', 'outdoorový nůž', 'multitool',
    'cyklistické světlo', 'zámek na kolo', 'pumpa na kolo', 'brašna na kolo', 'běžecká vesta', 'běžecký opasek', 'triatlon', 'atletické tretry',
    'sportovní ponožky', 'plavky', 'lyžařské brýle', 'skialpinismus', 'horolezecké vybavení', 'surf', 'potápění', 'šnorchl', 'veslování', 'skateboard',
    'fotbalový dres', 'kopačky', 'florbal hůl', 'hokejová výstroj', 'basketbalový míč', 'volejbalový míč', 'stolní tenis', 'badminton raketa',
    'boxerské rukavice', 'kimono judo', 'MMA rukavice', 'šipky', 'trampolína', 'koloběžka', 'inline brusle', 'rybářský prut', 'karpařina', 'muškaření',
    'trailové boty', 'trekové boty', 'barefoot boty', 'sportovní podprsenka', 'funkční tričko', 'softshellová bunda', 'péřová bunda', 'lyžařská bunda',
]


def seeds():
    out = []
    for _id, slug, name, _p in K.TREE:
        s = re.sub(r'\s*\(.*?\)', '', name).lower().strip()
        out.append((slug, s))
    out += [('extra', e) for e in EXTRA]
    seen, res = set(), []
    for slug, s in out:
        if s not in seen:
            seen.add(s)
            res.append((slug, s))
    return res


def cache_path(seed):
    return KW / (re.sub(r'[^a-z0-9]+', '-', seed.lower().encode('ascii', 'ignore').decode()).strip('-')[:50] + '-' + hashlib.md5(seed.encode()).hexdigest()[:6] + '.json')


def fetch(url, h, seed):
    p = cache_path(seed)
    if p.exists():
        return json.loads(p.read_text())
    for attempt in range(3):
        try:
            res = mm.rpc(url, h, 'tools/call', {'name': 'keyword_suggestions', 'arguments': {'lang': 'cs', 'keyword': seed[:80]}}, timeout=120)
            body = res.get('structuredContent') or json.loads(res['content'][0]['text'])
            data = body['data']['keywords']
            rows = [{'keyword': k['keyword'], 'volume': k.get('search_volume') or 0, 'yoy': k.get('yoy_change')} for k in data]
            p.write_text(json.dumps({'seed': seed, 'keywords': rows}, ensure_ascii=False))
            return {'seed': seed, 'keywords': rows}
        except (Exception, SystemExit) as e:  # throttle / transient
            if isinstance(e, SystemExit):
                raise
            print('retry', seed, type(e).__name__, str(e)[:80], file=sys.stderr)
            time.sleep(10 * (attempt + 1))
    return None


def main():
    if '--report' in sys.argv:
        allk = {}
        for f in KW.glob('*.json'):
            if f.name == 'kw-all.json':
                continue
            d = json.loads(f.read_text())
            for r in d['keywords']:
                k = r['keyword'].lower()
                if k not in allk or r['volume'] > allk[k]['volume']:
                    allk[k] = {'keyword': k, 'volume': r['volume'], 'seed': d['seed']}
        out = sorted(allk.values(), key=lambda r: -r['volume'])
        (KW / 'kw-all.json').write_text(json.dumps(out, ensure_ascii=False))
        tracked = Path(__file__).resolve().parent.parent / 'src/data/kw/kw-all.json'   # the repository copy that fasety.py reads (the Actions build has no workspace)
        tracked.parent.mkdir(parents=True, exist_ok=True)
        tracked.write_text(json.dumps(out, ensure_ascii=False))
        print(len(out), 'keywords')
        return
    only = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
    url, h = mm.session()
    done = 0
    todo = seeds()
    if '--seeds-file' in sys.argv:   # one seed per line (brand names, brand + product head, new category stems …)
        todo = [('file', l.strip()) for l in open(sys.argv[sys.argv.index('--seeds-file') + 1], encoding='utf-8') if l.strip()]
    for slug, s in todo:
        if only and slug != only:
            continue
        if cache_path(s).exists():
            continue
        fetch(url, h, s)
        done += 1
        time.sleep(1.5)
        if done % 25 == 0:
            print('fetched', done, file=sys.stderr, flush=True)
    print('done', done)


if __name__ == '__main__':
    main()
