"""sporteka.cz — wave 27e (16. 11. 2026): the parents of the January categories (waves 26 and 27) get one paragraph that links
their new sub-categories from the text, not only from the tiles. The parent's latest text (earlier waves, same order as
texty-export.py) is copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem

ADD = {
    'vitaminy-a-mineraly': '<p>Nejhledanější vitamíny a minerály mají vlastní výpisy: <a href="/vitamin-d/">vitamín D a D3</a>, <a href="/vitamin-c/">vitamín C</a>, <a href="/zinek/">zinek</a>, <a href="/horcik/">hořčík</a> a <a href="/omega-3/">omega-3</a>. Kdo chce všechno v jedné dávce, porovná <a href="/multivitaminy/">multivitamíny</a>.</p>',
    'iontove-napoje': '<p>Pokud hledáte jen minerály bez cukru a kalorií, podívejte se do výpisu <a href="/elektrolyty/">elektrolyty a solné tablety</a>, kde jsou šumivé tablety, kapsle a prášky s vyšším obsahem sodíku.</p>',
    'spalovace-tuku': '<p>Samostatně porovnáváme <a href="/l-karnitin/">L-karnitin</a> v tekuté podobě, v kapslích i v prášku, protože je to nejčastěji hledaná jednosložková látka této skupiny.</p>',
    'ostatni-doplnky-stravy': '<p>Několik doplňků má vlastní výpis s podrobným průvodcem: <a href="/probiotika/">probiotika</a>, <a href="/spirulina-chlorella/">spirulina, chlorella a zelené směsi</a>, <a href="/kurkuma/">kurkuma a kurkumin</a>, <a href="/tribulus/">tribulus (kotvičník)</a> a <a href="/ashwagandha/">ashwagandha</a>.</p>',
    'aminokyseliny-bcaa': '<p>Glutamin jako samostatnou aminokyselinu najdete ve výpisu <a href="/glutamin/">glutamin</a>, odděleně od směsí BCAA a EAA.</p>',
    'funkcni-trenink': '<p>Pro domácí funkční trénink máme zvlášť <a href="/medicinbaly/">medicinbaly a slam bally</a>, <a href="/zatezove-vesty/">zátěžové vesty</a> a <a href="/zebriny/">žebřiny</a>.</p>',
    'hrazdy-a-bradla': '<p>Dřevěné i kovové <a href="/zebriny/">žebřiny</a> s hrazdou nebo nástavci mají vlastní výpis včetně rad k ukotvení do zdi.</p>',
    'cinky-a-kotouce': '<p>Na uložení jednoruček, kotoučů a os slouží <a href="/stojany-na-cinky/">stojany na činky a kotouče</a>, od patrových regálů po nástěnné držáky.</p>',
    'fitness-pomucky': '<p>Mezi pomůckami mají vlastní výpis <a href="/gymnasticke-mice/">gymnastické míče</a>, <a href="/balancni-podlozky-bosu/">balanční podložky a BOSU</a> a <a href="/sejkry/">šejkry na protein</a>.</p>',
    'balancni-pomucky': '<p>Nafukovací čočky, polštáře a polokoule typu BOSU jsou pohromadě ve výpisu <a href="/balancni-podlozky-bosu/">balanční podložky a BOSU</a>.</p>',
    'posilovaci-stroje': '<p>Celé posilovací sestavy na jednom rámu porovnáváme ve výpisu <a href="/posilovaci-veze/">posilovací věže a multistanice</a>.</p>',
    'zimni-sporty': '<p>Do zimy se hodí i <a href="/vyhrivane-obleceni/">vyhřívané rukavice, ponožky a vložky</a>, <a href="/chranice-pater/">chrániče páteře</a> na sjezdovku a <a href="/kluzaky-na-snih/">kluzáky na sníh</a> pro děti.</p>',
    'sane-a-boby': '<p>Plastové kluzáky, talíře a nafukovací snowtuby mají vlastní výpis <a href="/kluzaky-na-snih/">kluzáky na sníh</a>.</p>',
    'nakrcniky-a-satky': '<p>Kukly, které kryjí hlavu, krk i obličej najednou, najdete zvlášť ve výpisu <a href="/kukly/">kukly a balaclavy</a>.</p>',
    'sportovni-vesty': '<p>Vesty s vysokou viditelností pro běh, kolo i děti jsou ve výpisu <a href="/reflexni-vesty/">reflexní vesty</a>.</p>',
    'doplnky-k-obuvi': '<p>Spreje, prací prostředky a vosky pro boty i oblečení s membránou jsou pohromadě ve výpisu <a href="/impregnace/">impregnace a péče</a>.</p>',
    'lahve-a-termosky': '<p>Láhve na míchání proteinu se sítkem nebo kuličkou porovnáváme samostatně ve výpisu <a href="/sejkry/">šejkry na protein</a>.</p>',
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
