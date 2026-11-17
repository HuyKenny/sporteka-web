"""sporteka.cz — brand texts wave 234 (17. 11. 2026): brand pages link the new brand landings of the November wave 6
(Ahrefs content gap vs 14 shops). The brand's latest text (earlier waves, export order) is copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem
_a = lambda slug, name: f'<a href="/{slug}/">{name}</a>'

ADD = {
    'adidas': '<p>Zimní obuv značky, od zateplených tenisek po dětské sněhule a boty Terrex, porovnáváme zvlášť na stránce <a href="/zimni-boty-adidas/">zimní boty Adidas</a>.</p>',
    'salomon': '<p>Zateplené a nepromokavé boty do sněhu i na zimní turistiku mají vlastní výběr <a href="/zimni-boty-salomon/">zimní boty Salomon</a>.</p>',
}

_cur = {}
for _mod in sorted((p.stem for p in HERE.glob('znacky_vlna[0-9]*.py')), key=_key):
    if _key(_mod) >= _key(_ME):
        break
    _new = importlib.import_module(_mod).NEW
    _cur.update({k: v for k, v in _new.items() if k in ADD})

NEW = {}
for _slug, _p in ADD.items():
    if _slug in _cur:
        NEW[_slug] = e = copy.deepcopy(_cur[_slug])
        e['guide'] = e['guide'] + _p
