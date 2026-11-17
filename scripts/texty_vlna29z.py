"""sporteka.cz — wave 29z (16. 11. 2026): the parents of the November wave 4 categories get one paragraph that links their new
sub-categories from the text.
The parent's latest text (earlier waves, same order as texty-export.py) is copied and the paragraph appended to its guide."""
import copy
import importlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_key = lambda n: (int(re.search(r'vlna(\d+)', n).group(1)), n)
_ME = Path(__file__).stem

ADD = {
    'sane-a-boby': '<p>Podle typu je porovnáváme i zvlášť: plastové <a href="/boby/">boby</a> s volantem i bez něj a dřevěné, kovové či skládací <a href="/sanky/">sáňky a saně</a>.</p>',
    'proteiny': '<p>Dva nejhledanější druhy mají vlastní výpis: syrovátkové <a href="/whey-proteiny/">whey proteiny</a> (koncentrát, izolát, clear) a <a href="/veganske-proteiny/">veganské a rostlinné proteiny</a> z hrachu, sóji nebo rýže.</p>',
    'mikiny': '<p>Podle střihu vybírejte ve výpisech <a href="/mikiny-s-kapuci/">mikiny s kapucí</a> a <a href="/mikiny-na-zip/">mikiny na zip</a>.</p>',
    'cinky-a-kotouce': '<p>Pevné i nakládací jednoručky porovnáváme zvlášť ve výpisu <a href="/jednorucni-cinky/">jednoruční činky</a>.</p>',
    'bandaze-a-ortezy': '<p>Podle kloubu najdete zvlášť <a href="/ortezy-na-koleno/">ortézy a chrániče na koleno</a> a <a href="/ortezy-na-kotnik/">ortézy a bandáže na kotník</a>.</p>',
    'sportovni-tasky': '<p>Velké tašky na cesty, včetně duffle bagů s ramenními popruhy, mají vlastní výpis <a href="/cestovni-tasky/">cestovní tašky a duffle bagy</a>.</p>',
    'dresy': '<p>Repliky klubů a reprezentací i týmové dresy pro amatérské kluby jsou pohromadě ve výpisu <a href="/fotbalove-dresy/">fotbalové dresy</a>.</p>',
    'sportovni-spodni-pradlo': '<p>Funkční a merino prádlo dělíme na <a href="/boxerky/">boxerky a trenky</a> a <a href="/kalhotky/">sportovní kalhotky</a>.</p>',
    'merino-pradlo': '<p>Merino spodní prádlo najdete také ve výpisech <a href="/boxerky/">boxerky a trenky</a> a <a href="/kalhotky/">sportovní kalhotky</a>, kde je spolu s funkčními syntetickými modely.</p>',
    'skateboardy': '<p>Malé plastové cruisery mají vlastní výpis <a href="/pennyboardy/">pennyboardy</a>.</p>',
    'basketbal': '<p>Koše na zeď, přenosné stojany i mini koše na dveře porovnáváme ve výpisu <a href="/basketbalove-kose/">basketbalové koše</a>.</p>',
    'basketbalove-mice': '<p>K míči se hodí i koš: nástěnné, stojanové i dětské modely jsou ve výpisu <a href="/basketbalove-kose/">basketbalové koše</a>.</p>',
    'tenisky': '<p>Vlastní stránku mají i další oblíbené modely: <a href="/adidas-handball-spezial/">Adidas Handball Spezial</a>, <a href="/adidas-stan-smith/">Adidas Stan Smith</a>, <a href="/adidas-forum/">Adidas Forum</a>, <a href="/new-balance-327/">New Balance 327</a>, <a href="/new-balance-2002r/">New Balance 2002R</a>, <a href="/new-balance-1906/">New Balance 1906</a>, <a href="/asics-gel-1130/">Asics Gel-1130</a>, <a href="/puma-suede/">Puma Suede</a>, <a href="/puma-palermo/">Puma Palermo</a> a <a href="/salomon-xt-6/">Salomon XT-6</a>.</p>',
    'sportovni-obuv': '<p>Mezi běžeckými a outdoorovými modely porovnáváme samostatně také <a href="/nike-pegasus/">Nike Pegasus</a>, <a href="/adidas-ultraboost/">Adidas Ultraboost</a>, <a href="/on-cloudmonster/">On Cloudmonster</a> a turistické <a href="/salomon-x-ultra/">Salomon X Ultra</a>.</p>',
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
