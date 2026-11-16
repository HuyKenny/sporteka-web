"""sporteka.cz — brand texts wave 226 (16. 11. 2026): the brand pages of the shoe-model landings (p_model facet, scripts/parametry.py
MODELS) get one paragraph that links the brand's most searched models. The brand's latest text (earlier waves, export order) is
copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem
_a = lambda slug, name: f'<a href="/{slug}/">{name}</a>'

ADD = {
    'nike': '<h2>Nejhledanější modely Nike</h2><p>Některé modely mají vlastní stránku se všemi nabídkami obchodů: '
            f'{_a("nike-air-force-1", "Air Force 1")}, {_a("nike-air-max", "Air Max")}, {_a("nike-dunk", "Dunk")}, {_a("nike-cortez", "Cortez")}, '
            f'běžecké {_a("nike-vomero", "Vomero")} a oblečení {_a("nike-tech-fleece", "Tech Fleece")}. Basketbalové legendy najdete pod {_a("jordan-1", "Jordan 1")} a {_a("jordan-4", "Jordan 4")}.</p>',
    'jordan': '<h2>Nejhledanější modely Jordan</h2><p>Dvě nejžádanější siluety mají vlastní stránku s nabídkami obchodů: '
              f'{_a("jordan-1", "Air Jordan 1")} ve verzích Low, Mid a High a {_a("jordan-4", "Air Jordan 4")}.</p>',
    'adidas': '<h2>Nejhledanější modely Adidas</h2><p>Klasiky z řady Originals porovnáváme každou zvlášť: '
              f'{_a("adidas-samba", "Samba")}, {_a("adidas-spezial", "Spezial")}, {_a("adidas-campus", "Campus")}, {_a("adidas-gazelle", "Gazelle")} '
              f'a {_a("adidas-superstar", "Superstar")}.</p>',
    'new-balance': '<h2>Nejhledanější modely New Balance</h2><p>Vlastní stránku s nabídkami obchodů mají modely '
                   f'{_a("new-balance-530", "530")}, {_a("new-balance-9060", "9060")}, {_a("new-balance-574", "574")} a {_a("new-balance-550", "550")}.</p>',
    'asics': '<h2>Nejhledanější modely Asics</h2><p>Samostatně porovnáváme městský model '
             f'{_a("asics-gel-nyc", "Gel-NYC")} a běžeckou řadu {_a("asics-gel-kayano", "Gel-Kayano")}.</p>',
    'vans': f'<h2>Vans Old Skool</h2><p>Nejznámější model značky má vlastní stránku se všemi nabídkami: {_a("vans-old-skool", "Vans Old Skool")}.</p>',
    'converse': f'<h2>Converse Chuck Taylor</h2><p>Plátěnky Chuck Taylor All Star i Chuck 70 porovnáváme na samostatné stránce {_a("converse-chuck-taylor", "Converse Chuck Taylor")}.</p>',
    'puma': f'<h2>Puma Speedcat</h2><p>Nízký model inspirovaný motorsportem má vlastní stránku s nabídkami: {_a("puma-speedcat", "Puma Speedcat")}.</p>',
    'salomon': f'<h2>Salomon Speedcross</h2><p>Trailovou klasiku s hlubokým vzorkem porovnáváme samostatně na stránce {_a("salomon-speedcross", "Salomon Speedcross")}.</p>',
    'merrell': f'<h2>Merrell Moab</h2><p>Nejprodávanější turistické boty značky mají vlastní stránku se všemi verzemi: {_a("merrell-moab", "Merrell Moab")}.</p>',
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
