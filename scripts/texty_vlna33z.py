"""sporteka.cz — wave 33z (19. 11. 2026): the parents of the November wave 8 categories and of the wave 33 blog articles
(Sportano / Decathlon / Sportisimo / inSPORTline gap, reports/sporteka/content-gap-2026-11i.md) get one paragraph that links their new sub-categories, the new gender / brand landings with a
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
    'sportovni-obuv': '<p>Pro halové sporty porovnáváme zvlášť <a href="/volejbalova-obuv/">volejbalové boty</a> s gumovou podrážkou a <a href="/boxerske-boty/">boxerské a zápasnické boty</a> s tenkou podešví do ringu.</p>',
    'volejbal': '<p>Boty s pevným bočním vedením a halovou podrážkou najdete ve výpisu <a href="/volejbalova-obuv/">volejbalové boty</a>.</p>',
    'bojove-sporty': '<p>Lehké vysoké boty do ringu a na žíněnky mají vlastní výpis <a href="/boxerske-boty/">boxerské a zápasnické boty</a>.</p>',
    'fitness-pomucky': '<p>Kolečka na posilování břicha, jednoduchá i dvojitá, jsou ve výpisu <a href="/posilovaci-kolecka/">posilovací kolečka</a>. Jak je zapojit do tréninku, ukazuje článek <a href="/cviky-na-bricho/">cviky na břicho</a>.</p>',
    'posilovaci-gumy': '<p>Konkrétní cviky na celé tělo s gumou a jak zvolit odpor popisuje článek <a href="/cviceni-s-posilovaci-gumou/">cvičení s posilovací gumou</a>.</p>',
    'kettlebelly': '<p>Jakou váhu zvolit na začátek a jak správně dělat swing nebo goblet dřep, vysvětluje článek <a href="/kettlebell-cviky/">kettlebell cviky</a>.</p>',
    'spaci-pytle': '<p>Co znamenají teploty komfort a limit a jak vybrat výplň, popisuje článek <a href="/jak-vybrat-spacak/">jak vybrat spacák</a>.</p>',
    'stany': '<p>Na co se dívat u počtu osob, váhy a vodního sloupce, shrnuje článek <a href="/jak-vybrat-stan/">jak vybrat stan</a>.</p>',
    'karimatky-a-matrace': '<p>Co znamená R-hodnota a jakou karimatku vzít do mrazu, vysvětluje článek <a href="/jak-vybrat-karimatku/">jak vybrat karimatku</a>.</p>',
    'softshellove-bundy': '<p>Kdy stačí softshell a kdy potřebujete nepromokavou bundu s membránou, porovnává článek <a href="/hardshell-vs-softshell/">hardshell vs. softshell</a>.</p>',
    'bezecka-obuv': '<p>Podle čeho vybírat tlumení, drop a velikost běžeckých bot, popisuje článek <a href="/jak-vybrat-bezecke-boty/">jak vybrat běžecké boty</a>; před tréninkem se hodí <a href="/rozcvicka-pred-behem/">rozcvička před během</a>.</p>',
    'tenisove-rakety': '<p>Jak zvolit velikost hlavy, váhu a grip, vysvětluje článek <a href="/jak-vybrat-tenisovou-raketu/">jak vybrat tenisovou raketu</a>.</p>',
    'badminton': '<p>Co znamenají váhové třídy, balanc a tvrdost rakety, popisuje článek <a href="/jak-vybrat-badmintonovou-raketu/">jak vybrat badmintonovou raketu</a>.</p>',
    'fotbalove-mice': '<p>Který míč patří do které věkové kategorie, ukazuje článek <a href="/velikosti-fotbalovych-micu/">velikosti fotbalových míčů</a>.</p>',
    'sjezdove-lyze': '<p>Jakou délku a typ lyží zvolit podle výšky a stylu jízdy, vysvětluje článek <a href="/jak-vybrat-sjezdove-lyze/">jak vybrat sjezdové lyže</a>.</p>',
    'snowboardy': '<p>Délku, šířku a profil prkna podle váhy a velikosti bot popisuje článek <a href="/jak-vybrat-snowboard/">jak vybrat snowboard</a>.</p>',
    'horska-kola': '<p>Jakou velikost rámu zvolit podle výšky a délky nohou, ukazuje článek <a href="/velikost-kola/">velikost kola</a>.</p>',
    'detska-kola': '<p>Jakou velikost kol zvolit podle výšky a věku dítěte, shrnuje článek <a href="/jak-vybrat-detske-kolo/">jak vybrat dětské kolo</a>.</p>',
    'joga-a-pilates': '<p>Odkud pilates pochází a jak s ním začít doma, vysvětluje článek <a href="/co-je-pilates/">co je pilates</a>.</p>',
    'fitness': '<p>Krátké tréninky bez stroje popisují články <a href="/tabata/">tabata</a>, <a href="/burpees/">burpees</a> a <a href="/drepy/">dřepy</a>.</p>',
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
