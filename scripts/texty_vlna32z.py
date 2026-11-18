"""sporteka.cz — wave 32z (18. 11. 2026): the parents of the November wave 7 categories (small categories competitors earn traffic with,
reports/sporteka/content-gap-2026-11h.md) get one paragraph that links their new sub-categories, the new gender / brand landings with a
hand-written text and the new blog articles. The parent's latest text (earlier waves, same order as texty-export.py) is copied and the
paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem

ADD = {
    'lezecka-lana-a-karabiny': '<p>Dynamická a statická lana porovnáváme zvlášť ve výpisu <a href="/horolezecka-lana/">horolezecká lana</a>, '
                               'zámkové, HMS i malé karabiny na klíče pod <a href="/karabiny/">karabiny</a>.</p>',
    'horolezectvi': '<p>Na led a sníh jsou ve výpisu <a href="/cepiny-a-macky/">cepíny a mačky</a>, lana a karabiny mají vlastní výpisy '
                    '<a href="/horolezecka-lana/">horolezecká lana</a> a <a href="/karabiny/">karabiny</a>.</p>',
    'stanove-doplnky': '<p>Plachty nad hamaku, ke stanu nebo jako samostatný přístřešek najdete ve výpisu <a href="/tarpy/">tarpy a celty</a>. '
                       'Předstany a stany k autu jsou mezi <a href="/strechni-stany/">střešními stany a autostany</a>.</p>',
    'sportovni-tasky': '<p>Tašky na hygienu s háčkem i bez něj porovnáváme ve výpisu <a href="/kosmeticke-tasky/">kosmetické a toaletní tašky</a>, '
                       'vodotěsné vaky s rolovacím uzávěrem pod <a href="/nepromokave-vaky/">nepromokavé vaky a dry bagy</a>.</p>',
    'posilovaci-stroje': '<p>Horní a spodní kladky na zeď i nástavce k věžím a klecím mají vlastní výpis <a href="/posilovaci-kladky/">posilovací kladky</a>.</p>',
    'outdoor-doplnky': '<p>Filtrační láhve, brčka a cestovní filtry na pitnou vodu z přírody jsou ve výpisu <a href="/filtry-na-vodu/">filtry na vodu</a>, '
                       'plachty na bivak pod <a href="/tarpy/">tarpy a celty</a>.</p>',
    'lahve-a-termosky': '<p>Nádoby se širokým hrdlem na polévku a teplý oběd porovnáváme ve výpisu <a href="/termosky-na-jidlo/">termosky na jídlo</a>, '
                        'vaky do batohu a měkké láhve pod <a href="/hydrovaky/">hydrovaky a vaky na vodu</a>.</p>',
    'sportovni-hodinky': '<p>Přesnější měření tepu při intervalech dává hrudní pás. Pásy a snímače s Bluetooth a ANT+ jsou ve výpisu '
                         '<a href="/hrudni-pasy/">hrudní pásy a snímače tepu</a>.</p>',
    'sportovni-ponozky': '<p>Ponožky s membránou do deště, na kolo a do mokré trávy mají vlastní výpis <a href="/nepromokave-ponozky/">nepromokavé ponožky</a>.</p>',
    'cyklo-tasky-a-nosice': '<p>Podle typu porovnáváme zvlášť <a href="/brasny-na-kolo/">brašny na kolo</a> (na nosič, rám, řídítka a pod sedlo), '
                            '<a href="/kosiky-na-kolo/">košíky na kolo</a> a <a href="/cyklisticke-batohy/">cyklistické batohy</a>.</p>',
    'pilates-pomucky': '<p>Domácí a skládací stroje včetně náhradních pružin a dílů jsou ve výpisu <a href="/pilates-reformery/">pilates reformery</a>.</p>',
    'chranice-bojove-sporty': '<p>Mušle a kraťasy s mušlí pro bojové sporty, hokej i míčové hry porovnáváme ve výpisu <a href="/suspenzory/">suspenzory</a>.</p>',
    'trekove-hole': '<p>Hole s botičkou na asfalt a poutkem ve tvaru rukavice mají vlastní výpis <a href="/nordic-walking-hole/">nordic walking hole</a>.</p>',
    'powerbanky-a-nabijeni': '<p>Rozkládací panely, powerbanky se solárním článkem a nabíjecí stanice se solárem jsou ve výpisu '
                             '<a href="/solarni-nabijecky/">solární nabíječky a panely</a>.</p>',
    'masazni-pomucky': '<p>Plošiny s vibrací nebo oscilací pro domácí cvičení porovnáváme ve výpisu <a href="/vibracni-plosiny/">vibrační plošiny</a>.</p>',
    'funkcni-trenink': '<p>Popruhy na cvičení s vlastní vahou, které se zavěsí na dveře, strop nebo strom, mají vlastní výpis '
                       '<a href="/zavesne-systemy-trx/">závěsné systémy TRX</a>.</p>',
    'cepice-a-celenky': '<p>Froté pásky na zápěstí a čelo jsou ve výpisu <a href="/potitka/">potítka</a>. Zimní čepice pro muže porovnáváme ve výběru '
                        '<a href="/panska-cepice/">pánská čepice</a>.</p>',
    'hry-na-zahradu': '<p>Sady koulí pro rekreační i turnajovou hru najdete ve výpisu <a href="/petanque/">pétanque</a>.</p>',
    'mikiny': '<p>Mikiny Jordan s logem Jumpmana mají vlastní výběr <a href="/jordan-mikina/">Jordan mikina</a>.</p>',
    'mikiny-na-zip': '<p>Pánské střihy na zip porovnáváme zvlášť ve výběru <a href="/panska-mikina-na-zip/">pánská mikina na zip</a>.</p>',
    'sportovni-kalhoty': '<p>Pánské tepláky, outdoorové a běžecké kalhoty pohromadě najdete ve výběru <a href="/panske-sportovni-kalhoty/">pánské kalhoty</a>.</p>',
    'kombinezy': '<p>Zimní overaly pro nejmenší porovnáváme ve výběru <a href="/detska-kombineza/">dětská kombinéza</a>, '
                 'finskou značku samostatně pod <a href="/reima-kombineza/">Reima kombinéza</a>.</p>',
    'perove-bundy': '<p>Dámské střihy s péřovou výplní mají vlastní výběr <a href="/perova-bunda-damska/">dámská péřová bunda</a>. '
                    'Jak péřovou bundu vyprat, aby se peří neslepilo, popisuje článek <a href="/jak-prat-perovou-bundu/">jak prát péřovou bundu</a>.</p>',
    'lyzarske-kalhoty': '<p>Pánské lyžařské a skialpové kalhoty porovnáváme zvlášť ve výběru <a href="/panske-lyzarske-kalhoty/">lyžařské kalhoty pánské</a>.</p>',
    'softshellove-bundy': '<p>Pánské softshelly do města i na hory najdete ve výběru <a href="/softshellova-bunda-panska/">pánská softshellová bunda</a>.</p>',
    'zateplene-leginy': '<p>Dámské legíny s počesaným vnitřkem mají vlastní výběr <a href="/damske-termo-leginy/">dámské termo legíny</a>.</p>',
    'nepromokave-bundy': '<p>Pánské bundy s membránou porovnáváme ve výběru <a href="/panska-nepromokava-bunda/">pánská nepromokavá bunda</a>. '
                         'Co znamenají údaje o vodním sloupci a prodyšnosti na visačce, vysvětluje článek '
                         '<a href="/vodni-sloupec/">vodní sloupec a prodyšnost</a>.</p>',
    'lyzarske-helmy': '<p>Helmy v dětských velikostech podle obvodu hlavy jsou ve výběru <a href="/detske-lyzarske-helmy/">dětská helma na lyže</a>.</p>',
    'bezecka-obuv': '<p>Jak poznat, jestli vaše chodidlo při došlapu stáčí dovnitř nebo ven, a co to znamená pro výběr bot, popisuje článek '
                    '<a href="/pronace-a-supinace/">pronace a supinace</a>.</p>',
    'buzoly-a-kompasy': '<p>Rozdíl mezi buzolou a kompasem a postup, jak s nimi určit azimut na mapě, ukazuje článek '
                        '<a href="/buzola-a-kompas/">buzola a kompas</a>.</p>',
    'impregnace': '<p>Jak čistit a impregnovat broušenou kůži na botách, popisuje článek <a href="/nubuk/">nubuk: co to je a jak se o něj starat</a>.</p>',
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
