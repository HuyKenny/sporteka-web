"""sporteka.cz — wave 28z (16. 11. 2026): the parents of the November wave 3 categories get one paragraph that links their new
sub-categories from the text; /tenisky/ and /sportovni-obuv/ get a paragraph linking the shoe-model landings (p_model facet).
The parent's latest text (earlier waves, same order as texty-export.py) is copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem

ADD = {
    'cepice-a-celenky': '<p>Kšilty a snapbacky mají vlastní výpis <a href="/ksiltovky/">kšiltovky</a>, kde jsou modely s rovným i zahnutým kšiltem, trucker síťky i licencované čepice sportovních týmů.</p>',
    'soupravy': '<p>Komplety mikiny a tepláků ze stejné látky porovnáváme zvlášť ve výpisu <a href="/teplakove-soupravy/">teplákové soupravy</a> pro muže, ženy i děti.</p>',
    'teplaky': '<p>Pokud hledáte tepláky rovnou i s mikinou ve stejném provedení, podívejte se na <a href="/teplakove-soupravy/">teplákové soupravy</a>.</p>',
    'tilka': '<p>Zkrácené topy a trička, které končí nad pasem, mají vlastní výpis <a href="/crop-topy/">crop topy</a>.</p>',
    'tasky-pres-rameno': '<p>Malé tašky nošené kolem pasu nebo křížem přes hrudník najdete pohromadě ve výpisu <a href="/ledvinky/">ledvinky</a>.</p>',
    'lahve-a-termosky': '<p>Hrnky s vakuovou izolací a víčkem na pití za chůze jsou ve výpisu <a href="/termohrnky/">termohrnky</a>, odděleně od lahví a jídelních termosek.</p>',
    'vareni-v-prirode': '<p>Na kávu a čaj na cestu slouží <a href="/termohrnky/">termohrnky</a>, které mají vlastní výpis včetně modelů s brčkem a madlem.</p>',
    'karimatky-a-matrace': '<p>Podložky se dvěma typy plnění porovnáváme zvlášť: <a href="/samonafukovaci-karimatky/">samonafukovací karimatky</a> s pěnou uvnitř a <a href="/nafukovaci-matrace/">nafukovací matrace a lehátka</a>, které se plní pumpou nebo vakem.</p>',
    'nafukovaci-hracky': '<p>Nafukovací lehátka do bazénu i matrace na spaní jsou pohromadě ve výpisu <a href="/nafukovaci-matrace/">nafukovací matrace a lehátka</a>.</p>',
    'bandaze-a-ortezy': '<p>Samostatně porovnáváme <a href="/tejpy/">tejpy a kineziologické pásky</a> a <a href="/kompresni-ponozky/">kompresní ponožky a podkolenky</a> pro běh a regeneraci.</p>',
    'zimni-bundy': '<p>Bundy s péřovou výplní mají vlastní výpis <a href="/perove-bundy/">péřové bundy</a>, kde rozdíl dělá plnivost peří a poměr peří a prachového peří.</p>',
    'outdoorove-kalhoty': '<p>Pružné kalhoty do větru a lehkého deště jsou zvlášť ve výpisu <a href="/softshellove-kalhoty/">softshellové kalhoty</a> pro dospělé i děti.</p>',
    'mestske-batohy': '<p>Batohy s polstrovanou kapsou na počítač mají vlastní výpis <a href="/batohy-na-notebook/">batohy na notebook</a>.</p>',
    'damske-plavky': '<p>Podle střihu si vyberete ve výpisech <a href="/jednodilne-plavky/">jednodílné plavky</a> a <a href="/dvoudilne-plavky/">dvoudílné plavky a bikiny</a>, kde jsou i samostatné horní a spodní díly.</p>',
    'plavky': '<p>Dámské plavky dělíme také podle střihu na <a href="/jednodilne-plavky/">jednodílné</a> a <a href="/dvoudilne-plavky/">dvoudílné plavky a bikiny</a>.</p>',
    'kopacky': '<p>Kopačky s nízkými gumovými výstupky na umělou trávu a tvrdý povrch mají vlastní výpis <a href="/turfy/">turfy</a>.</p>',
    'kardio-trenazery': '<p>Malé a skladné <a href="/steppery/">steppery</a> mají samostatný výpis, protože se vejdou i do bytu, kde by rotoped nebo běžecký pás překážel.</p>',
    'sportovni-ponozky': '<p>Ponožky a podkolenky se stupňovaným tlakem pro běh a regeneraci najdete ve výpisu <a href="/kompresni-ponozky/">kompresní ponožky a podkolenky</a>.</p>',
    'aminokyseliny-bcaa': '<p>Arginin, AAKG a citrulin malát porovnáváme zvlášť ve výpisu <a href="/arginin-a-citrulin/">arginin a citrulin</a>.</p>',
    'cyklo-lahve-a-drzaky': '<p>Držáky a pouzdra na telefon na řídítka nebo představec mají vlastní výpis <a href="/drzaky-na-mobil-na-kolo/">držáky na mobil na kolo</a>.</p>',
    'kempingove-doplnky': '<p>Na piknik a do kempu se hodí <a href="/piknikove-deky/">piknikové deky a koše</a>, <a href="/kempingove-zidle/">kempingové židle a křesla</a> a <a href="/kempingove-stoly/">kempingové stoly</a>.</p>',
    'kempingovy-nabytek': '<p>Nábytek do kempu dělíme na <a href="/kempingove-zidle/">kempingové židle a křesla</a> a <a href="/kempingove-stoly/">kempingové stoly</a>, ať snadno porovnáte nosnost, hmotnost i rozměr po složení.</p>',
    'balancni-pomucky': '<p>Desky na válci, kolébce nebo polokouli mají vlastní výpis <a href="/balancni-desky/">balanční desky</a>.</p>',
    'boxerske-rukavice': '<p>Lehké rukavice s volnými prsty pro smíšená bojová umění jsou ve výpisu <a href="/mma-rukavice/">MMA rukavice</a>.</p>',
    'tenisky': '<p>Nejhledanější modely mají vlastní stránku se všemi nabídkami: <a href="/nike-air-force-1/">Nike Air Force 1</a>, <a href="/nike-air-max/">Nike Air Max</a>, <a href="/jordan-4/">Jordan 4</a>, <a href="/jordan-1/">Jordan 1</a>, <a href="/nike-dunk/">Nike Dunk</a>, <a href="/adidas-campus/">Adidas Campus</a>, <a href="/adidas-samba/">Adidas Samba</a>, <a href="/adidas-spezial/">Adidas Spezial</a>, <a href="/adidas-superstar/">Adidas Superstar</a>, <a href="/adidas-gazelle/">Adidas Gazelle</a>, <a href="/new-balance-530/">New Balance 530</a>, <a href="/new-balance-9060/">New Balance 9060</a>, <a href="/new-balance-574/">New Balance 574</a>, <a href="/asics-gel-nyc/">Asics Gel-NYC</a>, <a href="/vans-old-skool/">Vans Old Skool</a> a <a href="/converse-chuck-taylor/">Converse Chuck Taylor</a>.</p>',
    'sportovni-obuv': '<p>Oblíbené modely porovnáváme i samostatně, například běžecké <a href="/nike-vomero/">Nike Vomero</a> a <a href="/asics-gel-kayano/">Asics Gel-Kayano</a>, trailové <a href="/salomon-speedcross/">Salomon Speedcross</a>, turistické <a href="/merrell-moab/">Merrell Moab</a> nebo tenisky <a href="/nike-air-force-1/">Nike Air Force 1</a> a <a href="/adidas-samba/">Adidas Samba</a>.</p>',
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
