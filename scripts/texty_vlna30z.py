"""sporteka.cz — wave 30z (17. 11. 2026): the parents of the November wave 5 categories (Sportisimo / Decathlon gap) get one paragraph
that links their new sub-categories and the new gender / brand landings with a hand-written text.
The parent's latest text (earlier waves, same order as texty-export.py) is copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem

ADD = {
    'zimni-obuv': '<p>Vysoké zateplené boty s vodoodolným svrškem mají vlastní výpis <a href="/snehule/">sněhule</a>, nejhledanější jsou <a href="/damske-snehule/">dámské sněhule</a>.</p>',
    'sportovni-kalhoty': '<p>Kalhoty s bočními kapsami na stehnech, ať outdoorové, nebo volnočasové, porovnáváme zvlášť ve výpisu <a href="/cargo-kalhoty/">cargo kalhoty a kapsáče</a>, dámské střihy pod <a href="/cargo-kalhoty-damske/">cargo kalhoty dámské</a>.</p>',
    'outdoorove-kalhoty': '<p>Turistické kapsáče s velkými kapsami najdete také ve výpisu <a href="/cargo-kalhoty/">cargo kalhoty a kapsáče</a>.</p>',
    'teplaky': '<p>Tepláky a joggery s kapsami na stehnech mají vlastní výpis <a href="/cargo-kalhoty/">cargo kalhoty a kapsáče</a>. Komplet s mikinou hledejte mezi <a href="/teplakove-soupravy/">teplákovými soupravami</a>.</p>',
    'leginy': '<p>Na zimní běh, běžky nebo procházky v mrazu jsou určené <a href="/zateplene-leginy/">zateplené a termo legíny</a> s počesanou nebo vlněnou vnitřní stranou.</p>',
    'doplnky-k-obuvi': '<p>Gelové, ortopedické, vyhřívané i barefoot stélky jsou pohromadě ve výpisu <a href="/vlozky-do-bot/">vložky do bot</a>.</p>',
    'plazove-doplnky': '<p>Plážové osušky, rychleschnoucí ručníky z mikrovlákna i ručníky do sauny a fitka mají vlastní výpis <a href="/rucniky/">ručníky a osušky</a>.</p>',
    'pantofle-a-zabky': '<p>Teplé bačkory a papuče na doma, do školky i do školy jsou ve výpisu <a href="/domaci-pantofle/">papuče a domácí pantofle</a>. Samostatně porovnáváme také <a href="/damske-pantofle/">dámské pantofle</a>, <a href="/panske-pantofle/">pánské pantofle</a> a nejhledanější značky: <a href="/birkenstock-pantofle/">Birkenstock</a>, <a href="/crocs-pantofle/">Crocs</a>, <a href="/adidas-pantofle/">Adidas</a> a <a href="/nike-pantofle/">Nike</a>.</p>',
    'stolni-tenis': '<p>Samotné stoly do haly, garáže i na zahradu najdete ve výpisu <a href="/pingpongove-stoly/">pingpongové stoly</a>.</p>',
    'masazni-pomucky': '<p>Hladké i vroubkované válce a masážní tyče pro práci s měkkými tkáněmi mají vlastní výpis <a href="/masazni-valce/">masážní válce</a>.</p>',
    'dalekohledy-a-kompasy': '<p>Turistické a vojenské buzoly i jednoduché kompasy porovnáváme ve výpisu <a href="/buzoly-a-kompasy/">buzoly a kompasy</a>.</p>',
    'obuv-do-vody': '<p>Pro chladnou vodu, surf nebo otužování jsou určené <a href="/neoprenove-boty-a-ponozky/">neoprenové boty a ponožky</a> v různé tloušťce neoprenu.</p>',
    'kempingove-nadobi': '<p>Klasické hliníkové, nerezové i titanové jídelní soupravy mají vlastní výpis <a href="/esusy/">ešusy</a>.</p>',
    'teplakove-soupravy': '<p>Podle střihu a značky porovnáváme zvlášť <a href="/damska-teplakova-souprava/">dámské teplákové soupravy</a>, <a href="/teplakova-souprava-panska/">pánské soupravy</a>, <a href="/teplakova-souprava-nike/">soupravy Nike</a> a <a href="/adidas-teplakovka/">teplákovky Adidas</a>.</p>',
    'kabaty-a-parky': '<p>Kabáty podle střihu najdete ve výpisech <a href="/damsky-kabat/">dámský kabát</a> a <a href="/pansky-kabat/">pánský kabát</a>.</p>',
    'tasky-pres-rameno': '<p>Crossbody tašky a dokladovky pro muže mají vlastní výběr <a href="/panska-taska-pres-rameno/">pánská taška přes rameno</a>.</p>',
    'lahve-a-termosky': '<p>Termosky a hrnky americké značky porovnáváme zvlášť na stránce <a href="/stanley-termoska/">Stanley termoska</a>.</p>',
    'ledvinky': '<p>Menší ledvinky nošené přes hrudník mají samostatný výběr <a href="/damska-ledvinka/">dámská ledvinka</a>.</p>',
    'sportovni-bundy': '<p>Bundy italské značky s vlajkou na rukávu porovnáváme na stránce <a href="/napapijri-bunda/">Napapijri bunda</a>.</p>',
    'ksiltovky': '<p>Podle střihu a značky porovnáváme zvlášť <a href="/panska-ksiltovka/">pánské kšiltovky</a>, <a href="/damska-ksiltovka/">dámské kšiltovky</a>, <a href="/ksiltovka-nike/">kšiltovky Nike</a> a <a href="/jordan-ksiltovka/">kšiltovky Jordan</a>.</p>',
    'perove-bundy': '<p>Samostatný výběr mají <a href="/perova-bunda-damska/">dámské péřové bundy</a> a <a href="/panska-perova-bunda/">pánské péřové bundy</a>.</p>',
    'nepromokave-bundy': '<p>Dámské střihy s membránou najdete ve výběru <a href="/damska-nepromokava-bunda/">dámská nepromokavá bunda</a>.</p>',
    'merino-tricka': '<p>Dámské střihy z merino vlny porovnáváme zvlášť na stránce <a href="/merino-triko-damske/">merino triko dámské</a>.</p>',
}

_cur = {}
for _mod in sorted((p.stem for p in HERE.glob('texty_vlna[0-9]*[a-wyz].py')), key=_key):
    if _key(_mod) >= _key(_ME):
        break
    _new = importlib.import_module(_mod).NEW
    _cur.update({k: v for k, v in _new.items() if k in ADD})

NEW = {}
for _slug, _p in ADD.items():
    if _slug in _cur:
        NEW[_slug] = e = copy.deepcopy(_cur[_slug])
        e['guide'] = e['guide'] + _p
