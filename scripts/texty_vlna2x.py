"""sporteka.cz — extension of texty_vlna2a.py: brands from the live catalogue (3. 11. 2026), common mistakes, when to buy."""
from texty_vlna1x import B

EXTRA = {}


def X(slug, brands, mistakes, buy, extra=''):
    EXTRA[slug] = dict(guide=f'<h3>Značky v nabídce</h3><p>{brands}</p><h3>Časté chyby při výběru</h3><ul>' + ''.join(f'<li>{m}</li>' for m in mistakes) + f'</ul>{extra}<h3>Kdy se vyplatí koupit</h3><p>{buy}</p>')


X('gravel-kola', f'Největší výběr gravelů mají {B(("van-rysel", "Van Rysel"), ("trek", "Trek"), ("kellys", "Kellys"), ("bottecchia", "Bottecchia"), ("specialized", "Specialized"), ("sava", "Sava"), ("kross", "Kross"))}. Van Rysel je značka Decathlonu, Trek a Specialized patří mezi světové výrobce, Kellys je česká značka.',
  ['Příliš úzké pláště na šotolinu. Kolo pak klouže a pohodlí klesá.', 'Silniční rám bez závitů na nosič, i když plánujete vícedenní cesty.', 'Výběr podle hmotnosti. Pro gravel je důležitější pohodlí a spolehlivost než poslední gramy.'],
  'Gravely se nejvíc slevují na podzim a v zimě, kdy obchody uvolňují místo novým modelům. Slevy se týkají hlavně předchozího ročníku, který se od nového liší hlavně barvou.')
X('silnicni-kola', f'Největší výběr silničních kol mají {B(("van-rysel", "Van Rysel"), ("sava", "Sava"), ("trek", "Trek"), ("pinarello", "Pinarello"), ("lapierre", "Lapierre"), ("kellys", "Kellys"), ("head", "Head"))}. Van Rysel je vlastní značka Decathlonu, Pinarello a Lapierre jsou tradiční silniční značky, Trek patří mezi světové výrobce.',
  ['Nákup agresivní závodní geometrie bez zkušeností. Pro rekreační jízdu je pohodlnější endurance.', 'Vyšší skupina komponentů na úkor kvalitního rámu a velikosti. Správně padnoucí kolo je důležitější.', 'Zapomenuté pedály a příslušenství. Silniční kola se často prodávají bez pedálů.'],
  'Silniční kola jsou nejlevnější na konci sezóny a v zimě. Starší ročník se často liší jen barvou a komponenty o stupeň, proto se vyplatí porovnat nabídky obchodů.')
X('celoodpruzena-horska-kola', f'Největší výběr celoodpružených kol mají {B(("specialized", "Specialized"), ("rockrider", "Rockrider"), ("trek", "Trek"), ("4ever", "4ever"), ("kellys", "Kellys"), ("scott", "Scott"))}. Rockrider je vlastní značka Decathlonu, Specialized, Trek a Scott patří mezi světové výrobce horských kol.',
  ['Příliš velký zdvih pro lesní cesty. Kolo je těžší a pomalejší do kopce, než musí být.', 'Nenastavené odpružení. Bez správného tlaku podle váhy kolo neodpruží, jak má.', 'Šetření na brzdách. U terénního kola jsou kvalitní brzdy bezpečnostní prvek.'],
  'Celoodpružená kola se slevují hlavně na podzim a v zimě. U drahých modelů se vyplatí sledovat předchozí ročník, který bývá výrazně levnější.')
X('mestska-kola', f'Největší výběr městských kol mají {B(("davi", "Davi"), ("author", "Author"), ("storm", "Storm"), ("elops", "Elops"), ("canellini", "Canellini"), ("f-lli-schiano", "F.lli Schiano"), ("dhs", "Dhs"))}. Elops je vlastní značka Decathlonu, Author je česká značka.',
  ['Příliš těžké kolo bez nosiče a blatníků pro denní dojíždění, i když je levné.', 'Zapomenutý kvalitní zámek. Městské kolo je častým cílem krádeží.', 'Špatná velikost rámu. Kolo s příliš velkým rámem se špatně ovládá a špatně se z něj slézá.'],
  'Městská kola jsou nejlevnější na konci léta a na podzim. Základní modely mají dlouhodobě stabilní cenu, vyplatí se sledovat slevy předchozích ročníků.')
X('krosova-kola', f'Největší výběr krosových kol mají {B(("kellys", "Kellys"), ("kross", "Kross"), ("specialized", "Specialized"), ("author", "Author"), ("van-rysel", "Van Rysel"))}. Kellys a Author jsou české značky, Kross polská, Specialized světový výrobce.',
  ['Očekávání terénní jízdy na úzkých pláštích. Na kořeny a kamení je lepší horské kolo.', 'Příliš nízká hmotnost na úkor výbavy. Pro dojíždění se hodí nosič a blatníky.', 'Špatná velikost rámu. U krosových kol záleží na dosahu k řídítkům.'],
  'Krosová kola se nejvíc slevují na konci sezóny. Starší ročník bývá levnější a liší se hlavně barvou.')
X('damska-kola', f'Největší výběr dámských kol mají {B(("storm", "Storm"), ("davi", "Davi"), ("canellini", "Canellini"), ("author", "Author"), ("saveno", "Saveno"))}. Author je česká značka.',
  ['Koupě podle barvy a ne podle velikosti rámu. Nesprávná velikost bolí záda.', 'Příliš těžké kolo na denní dojíždění do schodů. Zvažte hmotnost i nosič.', 'Opomenutí osvětlení a zámku. Světla jsou povinná za tmy.'],
  'Dámská kola jsou nejlevnější na konci léta. Základní modely mívají stabilní cenu, sledujte slevy předchozích ročníků.')
X('detske-trikolky', f'Největší výběr tříkolek mají {B(("petite-mars", "Petite Mars"), ("hypermotion", "Hypermotion"), ("arcore", "Arcore"), ("lionelo", "Lionelo"), ("qplay", "Qplay"), ("coccolle", "Coccolle"), ("smoby", "Smoby"))}. Multifunkční modely 3v1 a 5v1 nabízí hlavně Petite Mars a Lionelo.',
  ['Příliš malá nebo velká tříkolka pro věk dítěte. Dítě pak nedosáhne na pedály nebo se v ní špatně drží.', 'Tříkolka bez vodící tyče pro nejmenší děti, které ještě samy nešlapou.', 'Nákup bez ohledu na bezpečnostní pás a stabilitu. U tříkolky je bezpečnost důležitější než cena.'],
  'Tříkolky se slevují na konci léta a před Vánoci se naopak prodávají za plnou cenu. Porovnání cen je užitečné hlavně u multifunkčních modelů.')
X('mestska-elektrokola', f'Největší výběr městských elektrokol mají {B(("hitway", "Hitway"), ("dyu", "DYU"), ("samebike", "Samebike"), ("ttgo", "Ttgo"), ("moma-bikes", "Moma Bikes"), ("eskute", "Eskute"), ("urlife", "Urlife"))}. U dovážených modelů vždy ověřte výkon motoru, omezení rychlosti a dostupnost servisu.',
  ['Výběr jen podle nejnižší ceny u dováženého modelu. Při první poruše motoru nebo baterie se ukáže, zda existuje servis a náhradní díly.', 'Příliš malá baterie na denní dojíždění. Dojezd je v praxi nižší než v katalogu.', 'Opomenutí zámku. Elektrokolo je častým cílem krádeže.'],
  'Elektrokola jsou nejlevnější na podzim a v zimě. Sledujte i cenu za dopravu a servis a před koupí ověřte záruku na baterii.')
X('trekingova-elektrokola', f'Největší výběr trekingových elektrokol mají {B(("specialized", "Specialized"), ("trek", "Trek"), ("devron", "Devron"), ("corwin", "Corwin"), ("rockrider", "Rockrider"), ("rcb", "RCB"), ("hitway", "Hitway"))}. Specialized a Trek patří mezi světové výrobce, Rockrider je vlastní značka Decathlonu.',
  ['Příliš malá baterie na výlety. Dojezd klesá v kopcích a při protivětru.', 'Nekontrolovaný servis. U elektrokola se vyplatí značka s dostupným servisem motoru.', 'Zapomenuté příslušenství pro cestování, tedy nosič, blatníky a světla.'],
  'Trekingová elektrokola se nejvíc slevují na podzim a v zimě. U drahých modelů porovnejte předchozí ročník, který bývá výrazně levnější.')
X('horska-elektrokola', f'Největší výběr horských elektrokol mají {B(("engwe", "Engwe"), ("specialized", "Specialized"), ("olpran", "Olpran"), ("urlife", "Urlife"), ("ttgo", "Ttgo"))}. Specialized patří mezi světové výrobce horských kol, u dovážených modelů ověřte výkon motoru a servis.',
  ['Příliš slabé brzdy a odpružení na hmotnost elektrokola. Elektrokolo je těžší, proto potřebuje kvalitnější brzdy.', 'Podcenění váhy při přepravě. Horské elektrokolo váží obvykle 20 až 28 kg.', 'Nesprávné nastavení odpružení. Bez něj kolo neodpruží, jak má.'],
  'Horská elektrokola se slevují hlavně na podzim a v zimě. U Specialized a dalších značek se vyplatí hledat předchozí ročník, který je výrazně levnější.')
X('fatbike-elektrokola', f'Největší výběr fatbike elektrokol mají {B(("engwe", "Engwe"), ("hitway", "Hitway"), ("bodywel", "Bodywel"), ("evercross", "Evercross"), ("fafrees", "Fafrees"), ("urlife", "Urlife"))}. Jde většinou o dovážené modely, u kterých vždy ověřte výkon motoru, rychlost a servis.',
  ['Koupě modelu s výkonem motoru nad 250 W bez ověření legálnosti. Takové kolo se nepovažuje za jízdní kolo.', 'Podcenění hmotnosti. Fatbike elektrokolo váží obvykle 25 až 35 kg.', 'Neověřená dostupnost baterie a servisu. U dovážených modelů se to vyplatí zjistit předem.'],
  'Fatbike elektrokola jsou nejlevnější na podzim a v zimě. Porovnejte i cenu dopravy a záruku na baterii.')
X('skladaci-elektrokola', f'Největší výběr skládacích elektrokol mají {B(("fafrees", "Fafrees"), ("engwe", "Engwe"), ("dyu", "DYU"), ("bodywel", "Bodywel"))}. Jde většinou o dovážené modely, u kterých ověřte výkon motoru, rychlost a servis.',
  ['Koupě podle nejnižší ceny bez ohledu na hmotnost. Těžké skládací kolo se špatně nosí.', 'Nezkontrolované skládání. Kloub musí být pevně zajištěný, jinak jde o bezpečnostní riziko.', 'Příliš malá baterie pro dojíždění. Menší rám často znamená i menší baterii.'],
  'Skládací elektrokola jsou nejlevnější na podzim a v zimě. Porovnejte i cenu dopravy a záruku na baterii.')
