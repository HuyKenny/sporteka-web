"""sporteka.cz — wave 31z (17. 11. 2026): the parents of the November wave 6 categories (Ahrefs content gap vs 14 shops) get one paragraph
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
    'masazni-pomucky': '<p>Podložky a sady s plastovými hroty mají vlastní výpis <a href="/akupresurni-podlozky/">akupresurní podložky</a>.</p>',
    'behaci-pasy': '<p>Kompaktní pásy na pomalou chůzi, které se vejdou pod pracovní stůl nebo za gauč, porovnáváme zvlášť ve výpisu <a href="/chodici-pasy/">chodicí pásy (walking pady)</a>.</p>',
    'gymnasticke-pomucky': '<p>Nafukovací dráhy pro přemety a skládací žíněnky na doma i do tělocvičny jsou ve výpisu <a href="/airtracky-a-zinenky/">airtracky a žíněnky</a>.</p>',
    'funkcni-trenink': '<p>Měkké dopady pro gymnastiku a akrobacii najdete mezi <a href="/airtracky-a-zinenky/">airtracky a žíněnkami</a>, lehké manžety pro cviky na hýždě a ramena pod <a href="/zavazi-na-kotniky/">závaží na kotníky a zápěstí</a>.</p>',
    'zimni-bundy': '<p>Bundy se švy, které drží výplň v komorách, mají vlastní výpis <a href="/prosivane-bundy/">prošívané bundy</a> s výběrem <a href="/damska-prosivana-bunda/">dámská prošívaná bunda</a>. Volnější střihy se sněžným pasem do mrazu na prkně jsou mezi <a href="/snowboardove-bundy/">snowboardovými bundami</a>.</p>',
    'outdoorove-kalhoty': '<p>Kalhoty s membránou nebo přes-kalhoty do deště porovnáváme zvlášť ve výpisu <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>.</p>',
    'sportovni-kalhoty': '<p>Kalhoty do deště a s membránou mají vlastní výpis <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>, volné zimní kalhoty na prkno jsou mezi <a href="/snowboardove-kalhoty/">snowboardovými kalhotami</a>.</p>',
    'lyzarske-bundy': '<p>Delší a volnější bundy s kapucí přes helmu, jak je nosí snowboardisté, jsou ve výpisu <a href="/snowboardove-bundy/">snowboardové bundy</a>.</p>',
    'lyzarske-kalhoty': '<p>Volnější střihy se zesílenými lemy a často s kšandami mají vlastní výpis <a href="/snowboardove-kalhoty/">snowboardové kalhoty</a>.</p>',
    'doplnky-k-obuvi': '<p>Turistické gamaše, návleky do sněhu i neoprenové návleky na tretry jsou pohromadě ve výpisu <a href="/navleky-na-boty/">návleky na boty a gamaše</a>.</p>',
    'trekova-obuv': '<p>Do sněhu, rosy a bláta se k trekovým botám hodí <a href="/navleky-na-boty/">návleky a gamaše</a>. Boty pro hory v zimě najdete také mezi <a href="/keen-zimni-boty/">zimními botami Keen</a> a <a href="/zimni-boty-salomon/">zimními botami Salomon</a>.</p>',
    'cyklisticke-navleky': '<p>Samotné návleky přes tretry, ale i turistické gamaše, porovnáváme ve výpisu <a href="/navleky-na-boty/">návleky na boty a gamaše</a>.</p>',
    'fotbal': '<p>Branky na zahradu, hřiště i futsal, od skládacích pop-up po ocelové, mají vlastní výpis <a href="/fotbalove-branky/">fotbalové branky</a>.</p>',
    'hygiena-a-repelenty': '<p>Sítě na postel, do stanu i přes hlavu najdete ve výpisu <a href="/moskytiery/">moskytiéry</a>.</p>',
    'chladici-boxy': '<p>Měkké tašky a batohy s izolací, včetně obědových termotašek, mají vlastní výpis <a href="/chladici-tasky/">chladicí tašky a termotašky</a>.</p>',
    'hokejove-chranice': '<p>Rukavice od žákovských po seniorské velikosti, včetně hokejbalových, porovnáváme ve výpisu <a href="/hokejove-rukavice/">hokejové rukavice</a>.</p>',
    'chranice-bojove-sporty': '<p>Chrániče na zuby pro box, MMA, ragby i hokej mají vlastní výpis <a href="/chranice-zubu/">chrániče zubů</a>.</p>',
    'fitness': '<p>Kádě, sudy a skládací vany na ledovou koupel doma nebo na zahradě jsou ve výpisu <a href="/otuzovaci-kade/">otužovací kádě a vany</a>.</p>',
    'jogove-pomucky': '<p>Pěnové, korkové i dřevěné kostky na jógu porovnáváme zvlášť ve výpisu <a href="/joga-bloky/">jógové bloky</a>.</p>',
    'cinky-a-kotouce': '<p>Litinové, pogumované a bumper kotouče i olympijské osy mají vlastní výpis <a href="/kotouce-na-cinky/">kotouče a osy na činky</a>, lehké manžety na nohy a ruce jsou pod <a href="/zavazi-na-kotniky/">závaží na kotníky a zápěstí</a>.</p>',
    'horolezectvi': '<p>Ferratové sety s tlumičem pádu, lonže a rukavice na zajištěné cesty jsou ve výpisu <a href="/via-ferrata/">via ferrata</a>.</p>',
    'lezecka-lana-a-karabiny': '<p>Sety na zajištěné cesty s tlumičem pádu porovnáváme zvlášť ve výpisu <a href="/via-ferrata/">via ferrata: sety, lonže a rukavice</a>.</p>',
    'sportovni-bundy-jaro-podzim': '<p>Podle střihu porovnáváme zvlášť <a href="/panska-podzimni-bunda/">pánské podzimní bundy</a>, <a href="/jarni-a-podzimni-bundy-damske/">dámské jarní a podzimní bundy</a> a <a href="/detska-podzimni-bunda/">dětské podzimní bundy</a>.</p>',
    'rekreacni-brusle': '<p>Samostatný výběr mají <a href="/damske-brusle-na-led/">dámské brusle na led</a> a <a href="/detske-brusle-na-led/">dětské brusle na led</a>, včetně roztahovacích modelů.</p>',
    'turisticke-batohy': '<p>Batohy se zády a popruhy pro ženy najdete ve výběru <a href="/damsky-turisticky-batoh/">dámský turistický batoh</a>, menší modely pro děti pod <a href="/detsky-turisticky-batoh/">dětský turistický batoh</a>.</p>',
    'sportovni-obuv': '<p>Jak si doma změřit chodidlo a jak převést velikost EU na UK, US nebo centimetry, ukazuje <a href="/tabulka-velikosti/">tabulka velikostí bot a oblečení</a>.</p>',
    'tenisky': '<p>Než objednáte tenisky jiné značky, než jakou nosíte, podívejte se do průvodce <a href="/tabulka-velikosti/">tabulka velikostí bot a oblečení</a>: převody mezi EU, UK a US se u výrobců liší.</p>',
    'zimni-obuv': '<p>Podle značky porovnáváme zvlášť <a href="/zimni-boty-adidas/">zimní boty Adidas</a>, <a href="/zimni-boty-salomon/">zimní boty Salomon</a> a <a href="/keen-zimni-boty/">zimní boty Keen</a>.</p>',
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
