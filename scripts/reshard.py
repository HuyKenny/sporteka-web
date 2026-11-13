#!/usr/bin/env python3
"""sporteka.cz — move prefixes out of shards that are (nearly) full into NEW shards, without touching the other shards or their routes.

    scripts/reshard.py [--apply]      # dry run prints the moves; --apply rewrites `shards` + `files.shard` in data/static-state.db

Why: the weekly run stops when a shard holds more than SHARD_STOP files (Cloudflare refuses 100 000 per Worker version). `plan --force`
would repack EVERYTHING and change most routes; this only splits the overflowing shards: a whole prefix (or the biggest sub-prefix of a
prefix, e.g. 'p' → 'pa') goes to a new shard sNN. Routes: the longest prefix wins in Cloudflare exactly as in shard_of(), so the old
route 'sporteka.cz/p*' stays and 'sporteka.cz/pa*' is added. Printed: the prefix → worker list for `staticky.py cutover --only …`.
Order of operations (no 404 window): reshard --apply → deploy the new shards (hashes exist, nothing is uploaded) → cutover routes →
the next weekly run deploys the shrunk old shards."""
import collections
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import staticky as S  # noqa: E402

TARGET = 70_000     # a shard is split until it holds at most this many files (headroom for growth)
db = S.state()
m = dict(db.execute('SELECT prefix, shard FROM shards'))
cnt = collections.Counter(s for (s,) in db.execute('SELECT shard FROM files'))
over = [s for s, n in cnt.items() if s != S.MAIN and n > S.SHARD_STOP]
keys = collections.defaultdict(list)   # shard -> keys of its files
for p, s in db.execute('SELECT path, shard FROM files'):
    if p.strip('/'):
        keys[s].append(p.lstrip('/'))
new_no = max(int(s[1:]) for s in set(m.values())) + 1
cap_left = {}      # new shard -> files it can still take
moves = []         # (prefix, from, to, files)


def owner_prefix(k, mm):
    for i in range(len(k), 0, -1):
        if k[:i] in mm:
            return k[:i]
    return ''


def put(size):
    global new_no
    for sh, left in cap_left.items():
        if left >= size:
            cap_left[sh] -= size
            return sh
    sh = f's{new_no:02d}'
    new_no += 1
    cap_left[sh] = max(0, TARGET - size)
    return sh


for sh in over:
    left = cnt[sh]
    while left > TARGET:
        groups = collections.Counter()          # candidate prefix -> files
        for k in keys[sh]:
            own = owner_prefix(k, m)
            if m.get(own) != sh:
                continue                        # already moved in this run
            groups[own] += 1
            if len(k) > len(own):
                groups[k[:len(own) + 1]] += 1   # the sub-prefix one level deeper
        # a candidate is a prefix not yet mapped to another shard; whole prefixes of `sh` and their one-level sub-prefixes
        cands = [(n, p) for p, n in groups.items() if n <= 78_000 and (m.get(p) == sh or p not in m)]
        need = left - TARGET
        if not cands:
            print('no candidates', sh, left, sorted(groups.items(), key=lambda x: -x[1])[:6]); break
        ge = sorted(c for c in cands if c[0] >= need)
        n, p = ge[0] if ge else max(cands)
        to = put(n)
        moves.append((p, sh, to, n))
        m[p] = to
        left -= n
db_files = db.execute('SELECT COUNT(*) FROM files').fetchone()[0]
print(f'{len(over)} overflowing shards {over}; {db_files:,} files')
for p, a, b, n in moves:
    print(f'  {p!r:14} {a} → {b}  {n:6,} files   route sporteka.cz/{p}*')
after = collections.Counter()
for p, in db.execute('SELECT path FROM files'):
    k = p.lstrip('/')
    after[S.shard_of(p, m)] += 1
print('after:', dict(sorted(after.items())))
if '--apply' in sys.argv:
    for p, a, b, n in moves:
        db.execute('INSERT OR REPLACE INTO shards VALUES (?, ?)', (p, b))
    db.commit()
    S.sync_paths  # files.shard is moved by the next sync_paths(); do it here without re-listing paths:
    mm = S.shard_map(db)
    db.executemany('UPDATE files SET shard = ? WHERE path = ?', [(s, p) for p, cur in db.execute('SELECT path, shard FROM files').fetchall() if (s := S.shard_of(p, mm)) != cur])
    db.commit()
    print('applied')
