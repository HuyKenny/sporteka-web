#!/usr/bin/env python3
"""sporteka.cz — re-file products into a changed category tree WITHOUT a full catalogue build (minutes instead of hours).

Takes data/live-<env>.db, applies the current K.TREE (new categories, parents, order) and re-categorises the products of the
given categories by their title (kategorie.categorize), refreshes counts, facet cache and generic intro texts of the touched
categories, and writes the result to data/next.db. `katalog.py push --env <env>` then sends only the difference.

    python3 -I scripts/kategorie-patch.py stany            # categories (slugs) whose products are re-filed
    SPT_PRODUCTION_APPROVED=yes python3 -I scripts/katalog.py push --env production

Products whose title no longer maps anywhere are retired (301 to their old category), like the build does.
"""
import collections
import html
import json
import re
import shutil
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kategorie as K  # noqa: E402
import katalog as KT  # noqa: E402
import parametry as PM  # noqa: E402

ENV = 'production'
slugs = [a for a in sys.argv[1:] if not a.startswith('--')]
if not slugs:
    raise SystemExit(__doc__)
live = KT.live_path(ENV)
shutil.copyfile(live, KT.NEXT)
db = sqlite3.connect(KT.NEXT)
db.execute('PRAGMA journal_mode=OFF')
db.execute('PRAGMA synchronous=OFF')
cid = {r[1]: r[0] for r in db.execute('SELECT id, slug FROM categories')}
parent_of = {t[1]: t[3] for t in K.TREE}


def anc(slug):
    out = []
    while slug:
        out.append(slug)
        slug = parent_of.get(slug)
    return out


# 1. tree: new categories, parents, order
reparented = []
for i, (c, slug, name, parent) in enumerate(K.TREE):
    pid = next(t[0] for t in K.TREE if t[1] == parent) if parent else 0
    if slug not in cid:
        db.execute('INSERT INTO categories (id, slug, name, parent, menu_order) VALUES (?,?,?,?,?)', (c, slug, name, pid, i))
        clash = db.execute('SELECT kind, ref_id FROM slugs WHERE slug = ?', (slug,)).fetchone()
        if clash:      # a product already owns this URL: it gets "<slug>-<id>", the category takes the clean URL
            assert clash[0] == 'product', clash
            db.execute('UPDATE products SET slug = ? WHERE id = ?', (f'{slug}-{clash[1]}', clash[1]))
            db.execute('UPDATE slugs SET slug = ? WHERE slug = ?', (f'{slug}-{clash[1]}', slug))
            print('  product', clash[1], 'moved to', f'{slug}-{clash[1]}')
        db.execute("INSERT INTO slugs (slug, kind, ref_id) VALUES (?, 'category', ?)", (slug, c))
        cid[slug] = c
        print('new category', slug)
    else:
        if db.execute('SELECT parent FROM categories WHERE id = ?', (c,)).fetchone()[0] != pid:
            reparented.append(slug)
        db.execute('UPDATE categories SET name = ?, parent = ?, menu_order = ? WHERE id = ?', (name, pid, i, c))
touched = set()
# 2. re-file the products of the given categories
moved, retired = collections.Counter(), []
for s in slugs:
    for pid_, name, created in db.execute('SELECT id, name, created_at FROM products WHERE primary_cat = ? AND status = ?', (cid[s], 'publish')).fetchall():
        if s in ('stanove-kolky',) or KT.JUNK_TITLE3.search(K.fold(name)):   # the pegs section is dropped entirely
            retired.append(pid_)
            continue
        new = K.refine(s, name) if s in K.REFINE else K.categorize('', name, '')[0]   # cycling sections: the title refinement only
        if new is None and s not in K.REFINE:     # the product name alone says nothing ("Craft PRO Endur Distance", "Gumotex Safari 3"): the shops' titles and URLs often do
            for ot, ou in db.execute('SELECT title, orig_url FROM offers WHERE product_id = ? AND active = 1', (pid_,)).fetchall():
                slug_ = K.fold(re.sub(r'^https?://[^/]+/|[/_.-]+', ' ', ou or '').replace('.php', ' ').replace('.html', ' '))
                new = K.categorize('', ot, '')[0] or K.categorize('', slug_, '')[0]
                if new:
                    break
            if new is None:
                fn = K.fold(name)
                if re.search(r'wincraft|(^|\W)(cedule|vlajka|vlajecka|odpadkovy kos|hodiny|otvirak|cinkacka|klicenka|hrnek)(\W|$)|minecraft|(^|\W)lego(\W|$)', fn):
                    new = None
                elif re.search(r'(^|\W)(nike|adidas|skechers|palladium|clarks|merrell|puma|vans|converse|new balance)(\W|$)', fn):
                    new = 'tenisky'
                elif db.execute("SELECT 1 FROM products p JOIN brands b ON b.id = p.brand_id WHERE p.id = ? AND b.slug = 'craft'", (pid_,)).fetchone():
                    new = 'sportovni-obleceni'
                else:
                    new = s                           # unknown: stay where it is rather than vanish
        if new == s:
            continue
        if new is None:
            retired.append(pid_)
            continue
        cp = db.execute('SELECT created_at, min_price, pop, disc FROM cat_products WHERE product_id = ? AND direct = 1', (pid_,)).fetchone()
        if not cp:
            continue
        touched |= {x for (x,) in db.execute('SELECT s.slug FROM cat_products cp JOIN categories s ON s.id = cp.cat_id WHERE cp.product_id = ?', (pid_,))}
        db.execute('DELETE FROM cat_products WHERE product_id = ?', (pid_,))
        db.execute('UPDATE products SET primary_cat = ? WHERE id = ?', (cid[new], pid_))
        for i, a in enumerate(anc(new)):
            db.execute('INSERT OR REPLACE INTO cat_products (cat_id, created_at, product_id, direct, min_price, pop, disc) VALUES (?,?,?,?,?,?,?)',
                       (cid[a], cp[0], pid_, 1 if i == 0 else 0, cp[1], cp[2], cp[3]))
            touched.add(a)
        moved[(s, new)] += 1
for pid_ in retired:
    slug, = db.execute('SELECT s.slug FROM products p JOIN categories s ON s.id = p.primary_cat WHERE p.id = ?', (pid_,)).fetchone()
    touched |= {x for (x,) in db.execute('SELECT s.slug FROM cat_products cp JOIN categories s ON s.id = cp.cat_id WHERE cp.product_id = ?', (pid_,))}
    db.execute("UPDATE products SET status = 'retired', offer_count = 0, shop_count = 0, best_offer_id = 0 WHERE id = ?", (pid_,))
    db.execute('DELETE FROM offers WHERE product_id = ?', (pid_,))
    db.execute('DELETE FROM cat_products WHERE product_id = ?', (pid_,))
    db.execute("DELETE FROM slugs WHERE kind = 'product' AND ref_id = ?", (pid_,))
    db.execute("INSERT OR IGNORE INTO redirects (from_path, to_path, status) SELECT '/' || p.slug || '/', '/' || ? || '/', 301 FROM products p WHERE p.id = ?", (slug, pid_))
# 2b. a category that got a new parent: its products' ancestor rows (cat_products direct = 0) follow the new chain
for slug in reparented:
    n = 0
    for (pid_,) in db.execute('SELECT id FROM products WHERE primary_cat = ? AND status = ?', (cid[slug], 'publish')).fetchall():
        cp = db.execute('SELECT created_at, min_price, pop, disc FROM cat_products WHERE product_id = ? AND direct = 1', (pid_,)).fetchone()
        if not cp:
            continue
        touched |= {x for (x,) in db.execute('SELECT s.slug FROM cat_products cp JOIN categories s ON s.id = cp.cat_id WHERE cp.product_id = ?', (pid_,))}
        db.execute('DELETE FROM cat_products WHERE product_id = ? AND direct = 0', (pid_,))
        for a in anc(slug)[1:]:
            db.execute('INSERT OR REPLACE INTO cat_products (cat_id, created_at, product_id, direct, min_price, pop, disc) VALUES (?,?,?,0,?,?,?)', (cid[a], cp[0], pid_, cp[1], cp[2], cp[3]))
        n += 1
    print('reparented', slug, '->', parent_of[slug], n, 'products')
SPEC_KEYS = {'delka', 'typ', 'membrana', 'flex', 'vlastnost', 'tvar', 'profil', 'tuhost', 'uroven', 'filtr', 'teplota', 'vypln', 'zip', 'vaha'}
# 2c. winter filters (length, type, water column) of every product in the winter section
slug_of = {v: k for k, v in cid.items()}
npar = 0
for pid_, pc, name, desc_ in db.execute("SELECT id, primary_cat, name, desc_html FROM products WHERE status = 'publish'").fetchall():
    cs = slug_of.get(pc)
    if cs is None or not ({'zimni-sporty', 'lyzarske-obleceni', 'spaci-pytle'} & set(anc(cs))):
        continue
    texts = K.fold(name) + ' ' + ' '.join(K.fold(t) for (t,) in db.execute('SELECT title FROM offers WHERE product_id = ?', (pid_,)))
    new = set(PM.params(texts, cs, PM.desc_text(desc_)))
    keys_ = SPEC_KEYS | ({'sezona'} if 'spaci-pytle' in anc(cs) else set())
    new = {x for x in new if x[0] in keys_}
    qs_ = ','.join('?' * len(keys_))
    old = set(db.execute(f"SELECT key, value FROM product_params WHERE product_id = ? AND key IN ({qs_})", (pid_, *keys_)).fetchall())
    if new == old:
        continue
    db.execute(f"DELETE FROM product_params WHERE product_id = ? AND key IN ({qs_})", (pid_, *keys_))
    db.executemany('INSERT OR IGNORE INTO product_params (product_id, key, value) VALUES (?,?,?)', [(pid_, k, v) for k, v in new])
    touched |= {x for (x,) in db.execute('SELECT s.slug FROM cat_products cp JOIN categories s ON s.id = cp.cat_id WHERE cp.product_id = ?', (pid_,))}
    npar += 1
print('winter params refreshed for', npar, 'products')
print('moved', sum(moved.values()), 'retired', len(retired))
for k, v in moved.most_common(20):
    print('  ', k, v)
# 3. counts, noindex, facets and generic intro of every touched category (+ the new ones and their ancestors)
touched |= {t[1] for t in K.TREE if t[1] in cid and db.execute('SELECT description_html FROM categories WHERE id = ?', (t[0],)).fetchone()[0] == ''}
for t in list(touched):
    touched |= set(anc(t))
for slug in touched:
    c = cid[slug]
    db.execute('UPDATE categories SET count_direct = (SELECT COUNT(*) FROM cat_products x WHERE x.cat_id = ? AND x.direct = 1), '
               'count_total = (SELECT COUNT(*) FROM cat_products x WHERE x.cat_id = ?), noindex = 0 WHERE id = ?', (c, c, c))
    db.execute('UPDATE categories SET noindex = CASE WHEN count_total < 5 THEN 1 ELSE 0 END WHERE id = ?', (c,))
bnames = dict(db.execute('SELECT id, name FROM brands'))


def facets(cat_id):
    db.execute('CREATE TEMP TABLE IF NOT EXISTS _ids (id INTEGER PRIMARY KEY)')
    db.execute('DELETE FROM _ids')
    db.execute("INSERT INTO _ids SELECT p.id FROM products p WHERE p.status = 'publish' AND p.id IN (SELECT product_id FROM cat_products WHERE cat_id = ?)", (cat_id,))
    n, lo, hi, st, d = db.execute('SELECT COUNT(*), MIN(CASE WHEN p.min_price > 0 THEN p.min_price END), MAX(CASE WHEN p.min_price > 0 THEN p.min_price END), '
                                  'COALESCE(SUM(p.in_stock <> 0), 0), COALESCE(SUM(p.disc_pct >= 10), 0) FROM products p JOIN _ids i ON i.id = p.id').fetchone()
    if not n:
        return None
    bc = db.execute('SELECT p.brand_id, COUNT(*) FROM products p JOIN _ids i ON i.id = p.id WHERE p.brand_id <> 0 GROUP BY p.brand_id ORDER BY 2 DESC, 1 LIMIT 60').fetchall()
    sc = db.execute('SELECT o.domain, COUNT(DISTINCT o.product_id) FROM offers o WHERE o.active = 1 AND o.product_id IN (SELECT id FROM _ids) GROUP BY o.domain ORDER BY 2 DESC').fetchall()
    pc = collections.defaultdict(list)
    for k, v, c_ in db.execute('SELECT key, value, COUNT(*) FROM product_params WHERE product_id IN (SELECT id FROM _ids) GROUP BY key, value ORDER BY 3 DESC'):
        pc[k].append([v, c_])
    return {'n': n, 'lo': int(lo) if lo else 0, 'hi': int(hi + 0.999) if hi else 0, 'st': st, 'd': d,
            'b': [[b, c_] for b, c_ in bc], 's': [[d_, c_] for d_, c_ in sc], 'p': dict(pc)}


def kc(x):
    return f"{x:,}".replace(',', ' ') + ' Kč'


now = KT.NOW
for slug in sorted(touched):
    c = cid[slug]
    f = facets(c)
    if not f:
        db.execute('DELETE FROM site_cache WHERE key = ?', (f'f:{c}',))
        continue
    db.execute('INSERT OR REPLACE INTO site_cache (key, value, updated_at) VALUES (?,?,?)',
               (f'f:{c}', json.dumps(f, ensure_ascii=False, separators=(',', ':')), now))
    name = db.execute('SELECT name FROM categories WHERE id = ?', (c,)).fetchone()[0]
    top = [bnames[b] for b, _ in f['b'][:4] if b in bnames]
    parts = [f"<p><strong>{html.escape(name)}</strong> — porovnáváme {f['n']:,} produktů".replace(',', ' ')
             + (f" z {len(f['s'])} sportovních e-shopů" if len(f['s']) > 1 else '') + (f", ceny od {kc(f['lo'])}" if f['lo'] else '') + '.']
    if top:
        parts.append(f" Nejvíc nabídek mají značky {', '.join(html.escape(b) for b in top[:-1])}{' a ' if len(top) > 1 else ''}{html.escape(top[-1])}.")
    if f['d']:
        parts.append(f" Ve slevě je teď {f['d']:,} produktů.".replace(',', ' '))
    parts.append(' U každého produktu vidíte ceny všech obchodů, velikosti skladem a vývoj ceny.</p>')
    db.execute("UPDATE categories SET description_html = ? WHERE id = ? AND (description_html = '' OR description_html LIKE '<p><strong>%porovnáváme%')", (''.join(parts), c))
# menu data + data version
counts = dict(db.execute('SELECT slug, count_total FROM categories'))
db.execute("INSERT OR REPLACE INTO site_cache (key, value, updated_at) VALUES ('data_version', ?, ?)", (__import__('datetime').datetime.now().strftime('%Y%m%d%H%M%S'), now))
img = json.loads(db.execute("SELECT value FROM site_cache WHERE key = 'cats:img'").fetchone()[0])
for slug in touched:
    c = cid[slug]
    r = db.execute("SELECT p.image FROM cat_products x JOIN products p ON p.id = x.product_id WHERE x.cat_id = ? AND p.image <> '' ORDER BY x.pop DESC LIMIT 1", (c,)).fetchone()
    if r:
        img[str(c)] = r[0]
    else:
        img.pop(str(c), None)
db.execute("INSERT OR REPLACE INTO site_cache (key, value, updated_at) VALUES ('cats:img', ?, ?)", (json.dumps(img, ensure_ascii=False, separators=(',', ':')), now))
if '--facets' in sys.argv:       # landing pages (gender / brand / colour × category) for the new categories too
    import fasety  # noqa: E402
    print('facet landings:', fasety.generate(db))
db.commit()
db.close()
print('touched categories:', len(touched), '→ data/next.db; now: katalog.py push --env production')
