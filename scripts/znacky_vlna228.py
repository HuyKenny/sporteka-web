"""sporteka.cz — brand texts wave 228 (17. 11. 2026): brand pages link the new gender / brand landings of the November wave 5
(Sportisimo / Decathlon gap). The brand's latest text (earlier waves, export order) is copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem
_a = lambda slug, name: f'<a href="/{slug}/">{name}</a>'

ADD = {
    'napapijri': '<p>Bundy značky včetně anoraku Skidoo porovnáváme zvlášť na stránce <a href="/napapijri-bunda/">Napapijri bunda</a>.</p>',
    'stanley': '<p>Láhve a jídelní termosky řady Classic a Adventure mají vlastní výběr <a href="/stanley-termoska/">Stanley termoska</a>.</p>',
    'crocs': '<p>Nazouváky, slides a žabky značky jsou pohromadě ve výběru <a href="/crocs-pantofle/">Crocs pantofle</a>.</p>',
    'nike': '<p>Nike porovnáváme samostatně také u pantoflí (<a href="/nike-pantofle/">Nike pantofle</a>), teplákových souprav (<a href="/teplakova-souprava-nike/">tepláková souprava Nike</a>) a kšiltovek (<a href="/ksiltovka-nike/">kšiltovka Nike</a>).</p>',
    'adidas': '<p>Pantofle Adilette mají vlastní stránku <a href="/adidas-pantofle/">Adidas pantofle</a>, soupravy s třemi pruhy najdete pod <a href="/adidas-teplakovka/">Adidas teplakovka</a>.</p>',
    'jordan': '<p>Čepice s logem Jumpman porovnáváme na stránce <a href="/jordan-ksiltovka/">Jordan kšiltovka</a>.</p>',
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
