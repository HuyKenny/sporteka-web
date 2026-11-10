"""sporteka.cz — wave 13a (4. 11. 2026): long texts (>= 1650 words) for kemping, nastrahy-a-navnady, teplaky, dresy.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ kemping
NEW['kemping'] = dict(long=True,
    title='Kemping: stany, spacáky, karimatky a vaření | Sporteka',
    desc='Kempingové vybavení pod jednou střechou: stany, spací pytle, karimatky, vaření, nábytek i chlazení. Průvodce výběrem a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Kemping</strong> je soubor věcí, které dohromady nahradí domov na několik nocí pod širým nebem. Skládá se ze čtyř vrstev: přístřešek, spaní, jídlo a pohodlí v táboře. Chyba v kterékoli z nich se pozná hned, a to nejčastěji ve tři ráno, kdy zebe nebo teče stan. Proto má smysl vybavení vybírat jako celek, ne po jednotlivých kouscích.</p>'
          '<p>Na Sportece najdete všechny vrstvy na jednom místě: <a href="/stany/">stany</a>, <a href="/spaci-pytle/">spací pytle</a>, <a href="/karimatky-a-matrace/">karimatky a matrace</a>, <a href="/vareni-v-prirode/">vaření v přírodě</a>, <a href="/kempingovy-nabytek/">kempingový nábytek</a>, <a href="/chladici-boxy/">chladicí boxy</a>, <a href="/hamaky/">hamaky</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>. U každého kusu vidíte nabídky více českých obchodů vedle sebe, takže snadno poznáte, kde je zboží skladem a za jakých podmínek ho doručí.</p>',
    guide='<h2>Jak si sestavit kempingovou výbavu</h2>'
          '<p>Než otevřete první e-shop, odpovězte si na čtyři otázky. Kolik vás pojede? Dojedete až ke stanu autem, nebo ponesete vše na zádech? V jakém ročním období a v jaké nadmořské výšce budete spát? A jak často to budete dělat? Kdo jede dvakrát za léto na kemp u vody, potřebuje jiné věci než ten, kdo plánuje týdenní přechod hor. Odpovědi určují hlavně váhu, objem po složení a to, kolik stojí za to investovat do izolace.</p>'
          '<p>Rozhodující jsou tři kusy, které tvoří základ: stan, spací pytel a podložka. Zbytek je pohodlí a dá se přikupovat postupně. Naopak chybný základ se nedá nahradit nejlepším nábytkem.</p>'
          '<h3>Základ podle způsobu cestování</h3>'
          + T(['Styl', 'Co je důležité', 'Typické vybavení'], [
              ['Auto-kemp na jednom místě', 'prostor a komfort, váha nehraje roli', '<a href="/rodinne-stany/">rodinný stan</a>, dvojitá matrace, židle, stůl, chladicí box'],
              ['Pěší trek na více nocí', 'nízká váha a malý objem', '<a href="/turisticke-stany/">turistický stan</a>, lehký spacák, nafukovací podložka, malý hořák'],
              ['Rychlý výlet nebo festival', 'snadné stavění a nízká pořizovací váha', '<a href="/pop-up-a-plazove-stany/">pop-up stan</a>, deková nebo lehká péřová varianta, karimatka'],
              ['Rodina s dětmi', 'prostor, ochrana před deštěm a bezpečnost', '<a href="/detske-stany/">dětský stan</a> na hraní, <a href="/detske-spacaky/">dětské spacáky</a>, přístřešek'],
              ['Rybáři a dlouhé sezení na místě', 'odolnost proti větru a dešti, teplo při nehybnosti', '<a href="/rybarske-stany/">rybářský stan</a>, <a href="/rybarske-spacaky/">rybářský spacák</a>, lehátko']]) +
          '<h2>Stan: střecha nad hlavou</h2>'
          '<p>Při výběru stanu sledujte hlavně kapacitu, počet vchodů, předsíň a materiál. Údaj „pro čtyři osoby“ označuje, kolik lidí se vejde těsně vedle sebe, bez zavazadel. Pokud chcete mít uvnitř batohy a trochu prostoru, počítejte s kapacitou o jednu osobu vyšší. Vodní sloupec udává odolnost látky proti vodě, ale rozhodují také zalepené švy a kvalitní podlaha. Větší stany mají předsíň, kam se dá odložit obuv a uvařit v dešti, menší jsou lehčí a rychlejší na postavení.</p>'
          '<ul><li><strong>Dvouplášťový stan</strong> má vnitřní prodyšnou část a vnější nepromokavý plášť, mezi nimi proudí vzduch a snižuje se kondenzace.</li>'
          '<li><strong>Tunelový stan</strong> nabízí nejvíc prostoru na kilogram, ale musí se dobře ukotvit.</li>'
          '<li><strong>Kupolový stan</strong> stojí sám i bez kolíků, což se hodí na tvrdé či kamenité podloží.</li>'
          '<li><strong>Tipi a lavvu</strong> mají střed bez příček a hodí se k táboráku nebo na zimní kempování, viz <a href="/tipi-a-lavvu/">tipi a lavvu</a>.</li>'
          '<li><strong>Expediční stan</strong> je určený pro silný vítr a sníh, najdete ho v <a href="/expedicni-stany/">expedičních stanech</a>.</li></ul>'
          '<p>K samotnému stanu často patří drobnosti, které se kupují zvlášť: náhradní <a href="/stanove-kolky/">kolíky</a>, podlážka, opravná sada nebo <a href="/stanove-doplnky/">stanové doplnky</a>. Pokud potřebujete stín nebo zázemí pro společné sezení, existují <a href="/pristresky-a-party-stany/">přístřešky a party stany</a>, na auto zase <a href="/strechni-stany/">střešní stany</a>.</p>'
          '<h2>Spací pytel: teplota je to hlavní</h2>'
          '<p>Spacák se vybírá podle teploty, ne podle vzhledu. Výrobci obvykle udávají tři hodnoty: komfortní, limitní a extrémní. Spolehlivě se orientujte podle komfortní teploty, protože limitní je určená pro ty, kdo vydrží i drobné mrznutí. Pokud jste zimomřivý nebo spíte hůř, vyberte spacák o jeden stupeň teplejší, než byste podle předpovědi potřebovali. Rozdíl pocítíte nejvíc ke konci noci, kdy teplota klesá.</p>'
          '<ul><li><a href="/perove-spacaky/">Péřové spacáky</a> mají nejlepší poměr tepla k váze a malý objem po sbalení, ale nesnášejí vlhkost a vyžadují péči.</li>'
          '<li>Syntetické plnění je těžší a objemnější, ovšem drží teplo i po navlhnutí a snáší běžné praní.</li>'
          '<li><a href="/dekove-spacaky/">Dekové spacáky</a> se dají rozepnout do přikrývky a jsou pohodlné na auto-kemp, kde objem nevadí.</li>'
          '<li><a href="/vlozky-do-spacaku/">Vložky do spacáku</a> chrání pytel před potem, přidávají pár stupňů a dají se prát častěji než samotný spacák.</li></ul>'
          '<h2>Karimatka a matrace: izolace od země</h2>'
          '<p>Země odebírá teplo rychleji než vzduch. Spacák se pod tělem stlačí a přestane izolovat, proto o nočním chladu rozhoduje především podložka. Pěnová karimatka je lehká, odolná a nic ji nepropíchne. Samonafukovací podložka nabízí větší pohodlí a lepší izolaci, nafukovací je nejmenší po složení, ale vyžaduje opatrnost kvůli prasknutí. Rodinné nafukovací matrace a postele pohodlím připomínají domácí lůžko, jenže potřebují pumpu a více místa v autě. Kompletní nabídku najdete v kategorii <a href="/karimatky-a-matrace/">karimatky a matrace</a>.</p>'
          + T(['Typ podložky', 'Výhoda', 'Nevýhoda'], [
              ['Pěnová karimatka', 'nezničitelná, levná na údržbu, nehrozí propíchnutí', 'objemná a tvrdší'],
              ['Samonafukovací', 'dobrý poměr pohodlí a izolace', 'těžší než nafukovací'],
              ['Nafukovací', 'malý objem a nejlepší pohodlí na váhu', 'citlivá na ostré předměty'],
              ['Nafukovací matrace pro auto-kemp', 'výška a velká plocha', 'potřebuje pumpu, studí bez izolace']]) +
          '<h2>Vaření v přírodě</h2>'
          '<p>Jídlo v kempu rozhoduje o náladě. Nejjednodušší je plynový vařič na kartuši, který se zapálí během vteřin a snadno se reguluje. Na delší pobyty se hodí dvouplotýnkový stolní vařič, na pěší túry malý hořák nasazený přímo na kartuši. Při nízkých teplotách se tlak v kartuši snižuje, proto se pro zimu používají směsné plyny nebo jiné typy paliva. V kategorii <a href="/varice-a-kartuse/">vařiče a kartuše</a> najdete všechny varianty, v <a href="/kempingove-nadobi/">kempingovém nádobí</a> pak hrnce, příbory, misky a termosky.</p>'
          '<p>Nezapomeňte na zapalovač, větrnou zástěnu, čisticí houbičku a nádobu na vodu. Dobře si předem rozmyslete, kolik vody budete mít k dispozici, protože ta zásadně ovlivňuje, co můžete vařit. Ke konzervaci chladných potravin slouží <a href="/chladici-boxy/">chladicí boxy a tašky</a>. Pasivní box s dobrou izolací udrží potraviny chladné několik dní, pokud ho nebudete zbytečně otevírat a dáte do něj předem vychlazené věci.</p>'
          '<h2>Nábytek, hamaky a doplňky</h2>'
          '<p>Skládací židle, stůl a lehátko promění tábor v obytný prostor. U <a href="/kempingovy-nabytek/">kempingového nábytku</a> sledujte nosnost, výšku sezení a rozměr po složení. Pro lehké pěší výlety jsou lepší kratší stoličky, pro rodinný kemp pohodlná křesla s opěrkami. <a href="/hamaky/">Hamak</a> je lehká alternativa k lůžku i k židli; potřebuje dva stromy a popruhy, které strom nepoškodí. Mezi <a href="/kempingove-doplnky/">kempingové doplňky</a> patří svítilny, lucerny, nafukovací polštářky, sušáky a drobné organizéry, které šetří prostor.</p>'
          '<ul><li>Čelovka umožní zůstat rukama volný při vaření i cestě na toaletu.</li>'
          '<li>Voděodolný vak ochrání spacák i oblečení před deštěm.</li>'
          '<li>Lékárnička s náplastmi, dezinfekcí a obinadlem patří do každého tábora.</li>'
          '<li>Pro nošení výbavy poslouží <a href="/turisticke-batohy/">turistické batohy</a>, k nápojům <a href="/lahve-a-termosky/">lahve a termosky</a>.</li></ul>'
          '<h2>Značky v kempingové nabídce</h2>'
          '<p>Největší sortiment mají značky ' + B(('husky', 'Husky'), ('yate', 'Yate'), ('quechua', 'Quechua'), ('skandika', 'Skandika'), ('nils', 'Nils'), ('petromax', 'Petromax'), ('naturehike', 'Naturehike'), ('trimm', 'Trimm'), ('sea-to-summit', 'Sea to Summit'), ('pinguin', 'Pinguin'), ('outwell', 'Outwell'), ('thermos', 'Thermos'), ('hannah', 'Hannah')) + '. Husky, Pinguin a Hannah jsou časté mezi stany a spacáky pro turistiku, Skandika a Outwell nabízejí hlavně velké rodinné stany a nábytek, Naturehike a Sea to Summit lehké vybavení pro pěší výlety. Petromax je spojen s petrolejovými lampami a litinovým nádobím, Thermos s nádobami na teplé nápoje a jídlo. Značku porovnávejte vždy na konkrétním modelu, protože i u jedné firmy se úrovně výbavy liší.</p>'
          '<h2>Péče o vybavení po sezóně</h2>'
          '<p>Většinu poškození kempingové výbavy způsobí neopatrné uskladnění. Stan se nikdy nesbaluje mokrý. Pokud musíte, doma ho znovu postavte nebo rozložte a nechte vyschnout. Ve stlačeném mokrém stavu zaplesniví a povlak plátna se začne odlupovat. Spacák skladujte volně v prostorném pytli, ne v kompresním obalu, jinak plnění ztrácí vzdušnost. Kartuše uchovávejte mimo slunce a zdroje tepla. Nafukovací podložku před uložením vysušte a ponechte lehce nafouknutou. Vařiče po použití očistěte od mastnoty a zbytků jídla.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Kupovat stan jen podle ceny a opomenout předsíň a ventilaci.</li>'
          '<li>Podcenit podložku, takže v noci zebe i ve výborném spacáku.</li>'
          '<li>Brát nejlehčí výbavu, ačkoli jedete autem a lehkost nemá smysl.</li>'
          '<li>Neodzkoušet stan doma, takže první stavění probíhá v dešti za tmy.</li>'
          '<li>Spoléhat na extrémní teplotu spacáku místo komfortní.</li>'
          '<li>Nekontrolovat předem, zda se kartuše hodí na zvolený vařič.</li></ul>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Kempingové zboží má sezonní vrcholy a často se mění dostupnost. Na Sportece vidíte nabídky vedle sebe a můžete vybírat podle skladu, termínu doručení i podmínek vrácení. U stanů sledujte přiloženou výbavu, protože některé modely se prodávají bez kolíků nebo podlážky. U spacáků si ověřte délku a šířku, u podložek rozměr po rozložení a po sbalení. Rozsáhlejší výlety plánujte s předstihem, aby bylo čas vše vyzkoušet. Širší přehled turistické výbavy najdete v sekci <a href="/outdoor/">outdoor</a>.</p>',
    faq=[('Co je základ kempingové výbavy?', 'Stan, spací pytel a podložka. Na těchto třech věcech závisí, zda se vyspíte v suchu a v teple. Nábytek, nádobí a další doplňky se dají přikupovat postupně.'),
         ('Jak velký stan koupit?', 'Počítejte s kapacitou o jednu osobu větší, než kolik vás pojede, pokud chcete mít uvnitř zavazadla. Pro auto-kemp se hodí prostorný rodinný stan s předsíní, na pěší túru malý a lehký.'),
         ('Co znamená vodní sloupec stanu?', 'Udává odolnost látky proti pronikání vody. Důležité jsou ale i zalepené švy a podlaha, protože deštivý den prověří celou konstrukci, ne jen plášť.'),
         ('Jakou teplotu spacáku sledovat?', 'Komfortní. Limitní hodnota je hranice, kdy je už zima, extrémní je varování před podchlazením. Zimomřiví lidé by měli volit spacák o něco teplejší, než předpovídá počasí.'),
         ('Je lepší péřový, nebo syntetický spacák?', 'Peří je lehčí a dobře se sbalí, vyžaduje ale suché prostředí a opatrné praní. Syntetika je odolnější vůči vlhkosti a nenáročná na údržbu, zabere však více místa.'),
         ('Proč potřebuji podložku i v létě?', 'Země odebírá teplo, a spacák pod tělem se stlačí a přestane izolovat. Podložka zároveň zlepšuje pohodlí a chrání spacák před vlhkostí.'),
         ('Na co vařit v kempu?', 'Nejjednodušší je plynový vařič na kartuši. Pro skupiny se hodí dvouplotýnkový stolní vařič, na treky malý hořák. V zimě zvažte kartuše s vhodnou směsí plynů.'),
         ('Jak dlouho udrží chladicí box potraviny chladné?', 'Záleží na izolaci, venkovní teplotě a počtu otevření. Dobrý pasivní box vydrží několik dní, když do něj uložíte předem vychlazené potraviny a víko držíte zavřené.'),
         ('Jak uskladnit stan po výletě?', 'Vždy suchý a volně složený na suchém místě. Mokrý stan v pytli za pár dní zaplesniví a povrchová úprava se začne odlupovat.'),
         ('K čemu je hamak v kempu?', 'Slouží jako odpočinkové lehátko i lehká náhrada za lůžko při teplém počasí. Potřebuje dva stabilní stromy a široké popruhy, které kůru neničí.'),
         ('Jak se Sporteka liší od běžného obchodu?', 'Neprodává zboží sama, ale porovnává nabídky českých obchodů. Uvidíte u každého kusu více prodejců, jejich ceny, dostupné varianty i možnosti doručení a nakoupíte přímo u vybraného obchodu.')],
)

# ------------------------------------------------------------------ nastrahy-a-navnady
NEW['nastrahy-a-navnady'] = dict(long=True,
    title='Rybářské nástrahy a návnady: gumy, wobblery, boilies',
    desc='Nástrahy a návnady na dravce i kapry: gumy, wobblery, třpytky, jigy, boilies a pelety. Průvodce výběrem a nabídky českých rybářských e-shopů vedle sebe.',
    intro='<p><strong>Nástrahy a návnady</strong> jsou to, co rybu přiměje zabrat, a proto na nich záleží víc než na ceně prutu. Dělí se na dvě skupiny. Umělé nástrahy, tedy gumy, wobblery, třpytky nebo jigy, napodobují kořist a lovec jimi aktivně vede, aby dravce vyprovokoval k útoku. Návnady a boilies naopak lákají vůní a chutí a rybář čeká, až se ryba nakrmí a najde zavěšený háček.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u jednotlivých nástrah a návnad. K výběru patří vhodný <a href="/rybarske-pruty/">prut</a>, <a href="/rybarske-navijaky/">naviják</a> a <a href="/vlasce-a-snury/">vlasec nebo šňůra</a>, drobnosti jako háčky a závaží najdete v <a href="/rybarske-doplnky/">rybářských doplňcích</a>. Širší přehled je v kategorii <a href="/rybareni/">rybaření</a>.</p>',
    guide='<h2>Jak vybrat nástrahy a návnady</h2>'
          '<p>Při výběru se ptejte ve správném pořadí. Nejdříve na to, jakou rybu chcete chytat, protože štika a kapr mají zcela odlišný jídelníček. Potom, v jaké vodě: řeka, rybník, přehrada nebo kamenitý lom. Nakonec, jaké je roční období a teplota vody, od které se odvíjí aktivita ryb. Teprve potom řešíte barvu, velikost a značku. Většina začátečníků dělá opak a koupí nástrahu podle toho, jak vypadá v krabičce.</p>'
          + T(['Cílová ryba', 'Typ nástrahy nebo návnady', 'Poznámka'], [
              ['Štika', 'větší gumy, wobblery, třpytky', 'vodítko z ocelového nebo fluorocarbonového materiálu'],
              ['Candát', 'gumové rybky na jigu, tvrdší wobblery', 'loví se u dna, často za šera'],
              ['Okoun', 'malé gumy, rotačky, malé wobblery', 'hlavně ve skupinách, často u struktur'],
              ['Pstruh', 'malé třpytky, rotačky, drobné wobblery', 'vhodná je lehká souprava'],
              ['Kapr a amur', 'boilies, pelety, partikly', 'krmení a návnadové lodě'],
              ['Cejn, plotice, karas', 'těstové a práškové návnady, červi, kukuřice', 'method feeder, feeder, položená']]) +
          '<h2>Umělé nástrahy na dravce</h2>'
          '<h3>Gumové nástrahy</h3>'
          '<p>Gumová nástraha je měkká ryba, červ nebo raček z elastického materiálu, která se navazuje na jigovou hlavičku nebo na offsetový háček. Na rozdíl od tvrdých wobblerů ji oživuje pohyb ocasu, který reaguje i na malé trhnutí prutem. Rozlišují se typy jako shady s lopatkovým ocasem, twistry s vlnitým ocasem nebo kopyta a krevetky. Nejdůležitější parametr je velikost a váha jigové hlavičky, protože určuje, jak rychle nástraha klesá a kde ve vodním sloupci loví.</p>'
          '<ul><li><strong>Shad:</strong> přirozeně vypadající rybka, univerzální na štiku, candáta i okouna.</li>'
          '<li><strong>Twister:</strong> ocas se vlní už při pomalém navíjení, hodí se do chladnější vody.</li>'
          '<li><strong>Kopyto a rak (craw):</strong> sedí ke dnu a hodí se na pasivní ryby u překážek.</li>'
          '<li><strong>Červi a stick baity:</strong> bez speciálního hraní, ideální pro vodu s menším tlakem lovu.</li></ul>'
          '<h3>Wobblery</h3>'
          '<p>Wobbler je tvrdá nástraha s lopatkou, která určuje hloubku ponoru a typ pohybu. Plovoucí modely stoupají zpět k hladině, když přestanete navíjet. Potápivé klesají a hodí se pro hlubší vodu. Neutrálně vyvážené (suspending) zůstávají ve stejné hloubce, což oceníte v chladnější vodě, kdy ryby bývají méně aktivní. Delší lopatka znamená hlubší ponor, krátká a strmá naopak mělký. Pro lov u hladiny existují popery a walk-the-dog nástrahy.</p>'
          '<h3>Třpytky, rotačky a jigy</h3>'
          '<p>Kovové nástrahy jsou jednoduché a odolné. Třpytka se při tažení vlní ze strany na stranu a odráží světlo, rotačka má listek, který se otáčí kolem osy a vytváří vibrace. Obojí se používá na pstruhy, okouny i malé štiky. Jigové hlavičky a dropshot závaží nesou měkkou nástrahu u dna, kam se šikovně posílají na hranu skluzu nebo k okraji vodní vegetace. Pro hlubší vody a těžký vítr se hodí těžké pilkry.</p>'
          '<h2>Návnady a boilies na kapry a bílou rybu</h2>'
          '<p>Kaprařina stojí na přípravě místa. Boilie jsou vařené kuličky z těsta, pelety jsou lisované granule a partikly jsou luštěniny a obiloviny jako kukuřice, konopí nebo hrách, které se před použitím musí správně připravit. Boilies existují plovoucí, potápivé i rozpustné. Rozpustné rozkládá voda a vytváří vůňovou stopu, potápivé drží u dna a slouží jako hlavní krmení. Obalovací pasty a boostery posílí atraktivitu zavěšené návnady oproti okolnímu krmení.</p>'
          '<ul><li><strong>Boilies:</strong> základ kaprařiny, volí se velikost od drobných po velké selektivní.</li>'
          '<li><strong>Pelety:</strong> rychle se rozpouštějí a vytvářejí mlhu, dobré pro method feeder.</li>'
          '<li><strong>Partikly:</strong> levný způsob, jak ryby zdržet na místě, ale vyžadují vaření nebo namáčení.</li>'
          '<li><strong>Boostery a dipy:</strong> koncentrované tekutiny pro namáčení návnady na vlasci.</li>'
          '<li><strong>Těstové a práškové směsi:</strong> na cejny, plotice a karasy v rybníce i řece.</li></ul>'
          '<p>Při krmení platí zásada, že málo je často více. Přemíra návnady nasytí ryby dřív, než zabere, a ve studené vodě navíc zůstane nezkonzumovaná. V létě mohou ryby přijímat větší množství, na jaře a na podzim se krmí opatrněji. Správné vybavení pro kaprařinu zahrnuje také <a href="/rybarske-pruty/">kaprové pruty</a>, <a href="/rybarske-navijaky/">navijáky s volnoběhem</a>, <a href="/bivaky-a-kresla/">bivaky a křesla</a> a <a href="/rybarske-tasky/">tašky na vybavení</a>.</p>'
          '<h2>Barva, velikost a hloubka</h2>'
          '<p>V čisté vodě za slunečného dne fungují přirozené barvy, jako je stříbrná, zelená, hnědá a barvy plotice či ouklejky. V kalné vodě, za šera nebo po dešti přidejte kontrast: žlutou, oranžovou nebo kyselou zelenou. Velikost vždy odpovídá potravě, kterou ryby v dané vodě skutečně loví. Pokud chytáte v rybníku s drobnými plůdky, malá guma s pomalým pohybem uspěje víc než velký wobbler. Hloubku volte podle teploty: v chladu loví ryby níže a pomalu, v horku se zdržují u hladiny nebo ve stínu překážek.</p>'
          '<h2>Co k nástrahám potřebujete</h2>'
          '<p>Nástraha je jen jeden článek soupravy. Pro lov na umělou nástrahu se hodí citlivý prut se střední nebo rychlou akcí a naviják s plynulou brzdou. Pletená šňůra přenáší záběry lépe než monofilní vlasec, ale potřebuje fluorocarbonové nebo ocelové návazce, zejména na štiku. U kaprařiny je zase důležité kvalitní vlasec s dobrou odolností proti oděru a bezpečné háčky. Doplňkově přibývají čelovky, podběráky, zavážecí lodě a <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>. Pro muškaře je samostatná sekce <a href="/muskareni/">muškaření</a>, kde se používají zcela jiné umělé mušky.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíc položek mají značky ' + B(('westin', 'Westin'), ('caperlan', 'Caperlan'), ('rapala', 'Rapala'), ('jet-fish', 'Jet Fish'), ('illex', 'Illex'), ('savage-gear', 'Savage Gear'), ('mikbaits', 'Mikbaits'), ('nikl', 'Nikl'), ('mikado', 'Mikado'), ('sema', 'Sema'), ('traper', 'Traper'), ('gunki', 'Gunki'), ('starbaits', 'Starbaits'), ('tb-baits', 'TB Baits'), ('delphin', 'Delphin'), ('shimano', 'Shimano')) + '. Rapala je spjatá s wobblery a Savage Gear s realistickými gumovými rybkami. Illex a Gunki patří mezi výrobce umělých nástrah pro lov dravců, Westin nabízí širokou škálu nástrah pro štiku a okouna. Mikbaits, Nikl, Starbaits a TB Baits se zaměřují především na boilies, pelety a návnady pro kapraře. Caperlan je rybářská značka obchodního řetězce Decathlon. Každý model ale porovnávejte podle konkrétního typu, protože sortiment značek je široký.</p>'
          '<h2>Kdy nástrahy měnit</h2>'
          '<p>Dobrý rybář nenosí do vody jednu nástrahu, ale několik variant a podle záběrů se rozhoduje. Pokud ryby nereagují po několika hodech, změňte rychlost vedení, pak barvu a až nakonec typ. Při jarním oteplování se osvědčují pomalejší vedení a menší nástrahy, v létě rychlejší a hlučnější nástrahy, na podzim větší gumové rybky pro hladové dravce před zimou. Také u kaprařiny platí, že když se nedaří, pomůže změna velikosti boilie, doby krmení nebo místa. Vedení si vždy zapisujte, abyste příště věděli, co fungovalo.</p>'
          '<h2>Skladování a údržba</h2>'
          '<p>Měkké gumy se nesmí ukládat spolu s tvrdými wobblery, protože změkčovadlo z gumy poškodí lak a plast. Vždy je proto držte v oddělených přihrádkách nebo v původním obalu. Kovové nástrahy po rybaření opláchněte, zejména po slané vodě, a nechte vyschnout, aby nezrezivěly háčky. U wobblerů kontrolujte očka a trojháčky a tupé háčky vyměňte nebo naostřete. Boilies skladujte v suchu a chladu, polo-vlhké v uzavřeném sáčku, a mražené ve vhodném množství na jedno použití. Vyšší teplo a vlhkost je nejčastěji zkazí.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kupovat velké množství nástrah bez jasné představy o cílové rybě.</li>'
          '<li>Používat příliš těžkou jigovou hlavičku do mělké vody.</li>'
          '<li>Vést nástrahu pořád stejnou rychlostí, ačkoli ryby reagují na změny.</li>'
          '<li>Zakrmit místo velkým množstvím boilies a pak čekat na záběr.</li>'
          '<li>Neprohlížet háčky a pokračovat s tupými.</li>'
          '<li>Ignorovat místní řád a míry, které určují povolené způsoby lovu.</li></ul>'
          '<h2>Pro koho jaké nástrahy</h2>'
          '<p>Začínající rybář s malým rozpočtem vystačí se sadou drobných gum a několika rotačkami na okouny a pstruhy. Zkušený lovec štik ocení různé modely wobblerů, které pokryjí hloubky od hladiny po několik metrů. Kapraři si sestaví systém návnad a boilies podle sezony a konkrétní vody. Rodiny s dětmi ocení jednoduchou soupravu na bílou rybu s chlebem nebo těstem, kde je dostatek záběrů a málo čekání. Dárek rybáři vybírejte raději podle znalosti jeho oblíbené techniky než podle značky.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Nástrahy se prodávají jednotlivě i v sadách. Sada je výhodná pro začátek, ale časem v ní zůstanou kusy, které nepoužijete. Na Sportece vidíte nabídky obchodů vedle sebe a můžete rychle ověřit dostupnost barvy a velikosti, které potřebujete. Před nákupem si zkontrolujte váhu, délku a počet háčků, protože některé obchody je uvádějí jen v popisu. Při objednávce boilies sledujte datum minimální trvanlivosti a velikost balení.</p>',
    faq=[('Jaké nástrahy koupit na štiku?', 'Střední a větší gumové rybky, wobblery s mělkým i středním ponorem a třpytky. Důležité je ocelový nebo fluorocarbonový předvazec, protože štika přeřízne běžný vlasec.'),
         ('Co je jigová hlavička?', 'Je to olověné závaží s háčkem, na které se navléká gumová nástraha. Její váha určuje rychlost klesání a hloubku, ve které nástraha loví.'),
         ('Jaký je rozdíl mezi plovoucím a potápivým wobblerem?', 'Plovoucí po zastavení stoupá k hladině, potápivý klesá. Neutrální (suspending) zůstává stát v jedné hloubce a hodí se do chladné vody.'),
         ('Kdy použít výrazné barvy?', 'V kalné vodě, za šera nebo po dešti. V čisté vodě za slunce často lépe fungují přirozené odstíny.'),
         ('Co jsou boilies?', 'Kuličky z těsta, které se vaří a suší, aby vydržely ve vodě. Používají se hlavně na kapry a amury a liší se velikostí, vůní a rozpustností.'),
         ('Jak často krmit na kapra?', 'Záleží na teplotě vody a tlaku lovu. Ve studené vodě krmte spíš málo a opatrně, v teplé sezóně lze přidat více, ale přemíra ryby nasytí dřív, než zaberou.'),
         ('Čím se liší pelety od boilies?', 'Pelety jsou lisované granule, které se ve vodě rychle rozpadají a vytvářejí mlhu. Boilies drží tvar déle a rozkládají se pomaleji.'),
         ('Jak uložit gumové nástrahy?', 'Odděleně od tvrdých nástrah, protože změkčovadlo z gumy poškozuje lak a plast. Nejlépe v původním obalu nebo v samostatné přihrádce krabičky.'),
         ('Jaká šňůra se hodí na umělé nástrahy?', 'Pletená šňůra dobře přenáší záběry, protože se neroztahuje. Pro dravce se k ní přidává fluorocarbonový nebo ocelový předvazec.'),
         ('Potřebuji na lov dravců rybářský lístek?', 'Ano, k lovu je v ČR nutný rybářský lístek a povolenka k danému revíru. Podrobnosti, míry a doby hájení určuje rybářský řád platný pro konkrétní vodu.'),
         ('Jak poznám, že nástraha je pro mou vodu vhodná?', 'Zjistěte, čím se tamní ryby živí, a vyberte podobnou velikost i barvu. Nejspolehlivější je vzít do krabičky několik odlišných typů a podle záběrů pochopit, co ryby zrovna chtějí.')],
)

# ------------------------------------------------------------------ teplaky
NEW['teplaky'] = dict(long=True,
    title='Tepláky: pánské, dámské, dětské, zateplené | Sporteka',
    desc='Tepláky na sport i volný čas: zúžené, rovné, baggy, bavlněné i zateplené. Průvodce střihem, materiálem a velikostí a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Tepláky</strong> patří mezi kousky, které se nosí nejčastěji, a přesto se při výběru dělá spousta chyb. Stejné slovo totiž označuje kalhoty na běh, domácí pohodlí, školní tělocvik i městský styl. Liší se střihem, tloušťkou, pružností a tím, jak se chovají po praní. Kalhoty, ve kterých se dobře sedí na gauči, jsou při tréninku často nepraktické a naopak.</p>'
          '<p>Na Sportece najdete tepláky v rámci <a href="/sportovni-kalhoty/">sportovních kalhot</a> a můžete je porovnat u více českých obchodů najednou. Ke kompletnímu outfitu patří <a href="/mikiny/">mikiny</a>, <a href="/sportovni-tricka/">sportovní trička</a> nebo celé <a href="/soupravy/">soupravy</a>. Na ven v zimě pomůže <a href="/termopradlo/">termoprádlo</a> pod teplákovinu, v chladu přidáte <a href="/sportovni-bundy/">sportovní bundu</a>.</p>',
    guide='<h2>Jak vybrat tepláky podle využití</h2>'
          '<p>První otázka zní, k čemu je budete nosit. Na trénink potřebujete pružný, lehký a prodyšný materiál, který se nepřilepí k noze. Na doma a do města je důležitější měkkost a střih. Do chladna sáhnete po zateplené variantě s vnitřní hřejivou vrstvou. Děti zase potřebují odolná kolena a bezpečné šňůrky. Pokud kalhoty využijete do více situací, hledejte kompromis, ne extrém: střední gramáž, rovný nebo mírně zúžený střih a pružný pas s úpravou.</p>'
          + T(['Využití', 'Vhodný střih', 'Vhodný materiál'], [
              ['Běh a trénink', 'zúžený nebo přiléhavý, zip u kotníku', 'lehký polyester s elastanem'],
              ['Posilovna a crossfit', 'zúžený s pružným pasem', 'strečová pletenina, rychleschnoucí'],
              ['Doma a odpočinek', 'volný nebo rovný', 'měkká bavlna nebo směs, froté'],
              ['Město a každý den', 'jogger nebo straight', 'bavlněná směs, která drží tvar'],
              ['Zima venku', 'rovný s manžetou', 'zateplený s fleecem uvnitř'],
              ['Děti a škola', 'rovný s pružným pasem', 'směs s odolnějšími koleny']]) +
          '<h2>Střih a siluety</h2>'
          '<p>Střih ovlivňuje pohodlí i vzhled. Klasický <strong>jogger</strong> má zúžené nohavice zakončené manžetou u kotníku. Hodí se ke sportovním botám, drží se na nohou a nepřekáží při chůzi do schodů. <strong>Straight</strong> neboli rovný střih má stejnou šířku od kolene dolů a vypadá nenápadněji, dobře se kombinuje s různou obuví. <strong>Baggy</strong> a široké tepláky mají volnější stehna i nohavice, nosí se hlavně v městském stylu a při sportu mohou překážet. Pro dynamické aktivity sáhněte po přiléhavých nebo strečových modelech, které se při pohybu nezamotají.</p>'
          '<p>Rozhodující je také délka. Nohavice by neměly zametat zem, ale ani odkrývat polovinu lýtka. U modelů s manžetou se délka řeší tím, jak moc se nohavice nabere. Rovné bez manžety se musí koupit v odpovídající délce nebo zkrátit.</p>'
          '<h2>Materiály a gramáž</h2>'
          '<ul><li><strong>Bavlna</strong> je měkká a příjemná na kůži, ale při pocení těžkne a pomalu schne.</li>'
          '<li><strong>Směs bavlny a polyesteru</strong> drží tvar, méně se mačká a rychleji schne.</li>'
          '<li><strong>Polyester</strong> odvádí vlhkost od těla a je ideální na pohyb, ale někomu se může zdát méně příjemný.</li>'
          '<li><strong>Elastan</strong> přidává pružnost, takže tepláky nesvazují při dřepu a výpadu.</li>'
          '<li><strong>Froté a flís uvnitř</strong> zahřejí, ale v teple se v nich snadno přehřejete.</li>'
          '<li><strong>Tenká pletenina nebo plátno</strong> funguje v létě a při lehčím tréninku.</li></ul>'
          '<p>Gramáž teplákoviny prozradí, kdy je budete nosit. Lehké se hodí na jaro a léto, střední na celý rok a těžké na chladné dny. Na rozdíl od oblečení do deště teplákovina nechrání před větrem a mokrem, proto na ni v zimě vrstvěte větrovku nebo kalhoty nad ni.</p>'
          '<h2>Pas, kapsy a detaily</h2>'
          '<p>Pružný pas se šňůrkou umožňuje upravit velikost podle objemu a nesvírá žaludek. Plochá guma bez šňůrky je rovná a nepůsobí objemně pod tričkem, ale hůř drží, pokud kalhoty zhubnou nebo se vypraly. Kapsy na zip uloží klíče nebo telefon, boční šité kapsy jsou pohodlné pro ruce. Zadní kapsa se hodí na kartu nebo doklady. Reflexní prvky a zipy u kotníků usnadní oblékání přes boty, zesílená kolena zase ocení děti a všichni, kdo často klečí. Pro zajímavost se u některých modelů vyskytuje i vnitřní síťovaná podšívka, která zlepšuje prodyšnost.</p>'
          '<h2>Velikost a střih podle postavy</h2>'
          '<p>Měřte obvod pasu, boků a délku vnitřního švu a porovnejte s tabulkou konkrétní značky. U elastických modelů dává smysl vybrat standardní velikost, u bavlněných a volných raději počítat s drobnou rezervou kvůli smrštění. Tepláky mají výhodu, že pružný pas toleruje drobný rozdíl, ale délka nohavice se nedá změnit. Pokud pracujete s předpokladem, že velikost XL je u různých značek stejná, budete překvapeni. Spolehlivější je změřit kalhoty, které vám sedí, a porovnat je s rozměry produktu.</p>'
          + T(['Údaj', 'Jak změřit', 'Na co dát pozor'], [
              ['Obvod pasu', 'v nejužším místě trupu', 'u pružného pasu stačí mírná rezerva'],
              ['Obvod boků', 'v nejširším místě', 'u těsných střihů je důležitý'],
              ['Délka vnitřního švu', 'od rozkroku ke kotníku', 'rozhoduje o poloze nohavice nad botou'],
              ['Rozkrok', 'výška mezi pasem a rozkrokem', 'baggy střihy mají nižší rozkrok']]) +
          '<h2>Dámské, pánské, dětské a unisex</h2>'
          '<p>Dámské střihy mají typicky užší pas a širší boky, pánské rovnější linii a delší nohavici. Unisex modely se prodávají hlavně ve volnějším střihu a vhodně sedí na různé postavy. Dětské tepláky se vyrábějí s ohledem na rychlý růst a kolena, která se rychle odírají. U dětí se vyplatí vzít spíše o velikost větší s manžetou, kterou lze vyhrnout. U dospívajících sledujte délku, protože rostou zejména do výšky. Pokud nakupujete pro více lidí, projděte také <a href="/sportovni-obleceni/">sportovní oblečení</a> a hledejte komplety.</p>'
          '<h2>Co nosit s tepláky</h2>'
          '<p>K funkčnímu tréninku se hodí <a href="/funkcni-tricka/">funkční trička</a> a <a href="/funkcni-mikiny/">funkční mikiny</a>, které odvádí pot. Pro volný čas k teplákům pasují <a href="/mikiny/">mikiny</a> a <a href="/kabaty-a-parky/">kabáty a parky</a>. Pokud potřebujete kalhoty pro horší počasí, podívejte se po <a href="/outdoorove-kalhoty/">outdoorových kalhotách</a>, a pro cvičení v teple po <a href="/sportovni-kratasy/">sportovních kraťasech</a> nebo <a href="/leginy/">legínách</a>. Pro pohodlnou cestu do práce či domů poslouží <a href="/sportovni-ponozky/">sportovní ponožky</a> a k nim vhodná obuv.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce tepláků nabízejí značky ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('gap', 'Gap'), ('under-armour', 'Under Armour'), ('champion', 'Champion'), ('4f', '4F'), ('nike', 'Nike'), ('guess', 'Guess'), ('fila', 'Fila'), ('lotto', 'Lotto'), ('gymbeam', 'GymBeam'), ('celio', 'Celio'), ('lacoste', 'Lacoste')) + '. Adidas, Puma, Nike a Under Armour jsou typické sportovní značky se střihy pro trénink i volný čas. Champion, Gap, Fila a Lacoste vycházejí spíš z módní a streetwearové tradice. 4F a Lotto nabízejí širší sportovní sortiment, GymBeam se zaměřuje na fitness. Střihy se u každé značky liší, takže vždy kontrolujte tabulku u konkrétního produktu.</p>'
          '<h2>Sezónní výběr</h2>'
          '<p>Na jaře a na podzim se osvědčí střední gramáž s manžetou, která drží teplo u kotníku a snese mírný déšť. V létě sáhněte po tenké pletenině nebo lehkém polyesteru, ideálně se síťovanou podšívkou nebo bočními větracími otvory. V zimě volte zateplený vnitřek, ale nezapomeňte, že teplákovina pod bundou má sloužit jako izolace, ne jako vrchní vrstva proti větru. Při práci venku v mrazu se vyplatí kombinace termoprádla, tepláků a nepromokavých kalhot navrch. Tak můžete jednotlivé vrstvy odkládat podle toho, jak se budete zahřívat.</p>'
          '<h2>Tepláky pro konkrétní aktivity</h2>'
          '<ul><li><strong>Běh:</strong> lehké zúžené kalhoty s kapsou na zip na klíče a s reflexními prvky pro večerní trénink.</li>'
          '<li><strong>Posilovna:</strong> pružný materiál, který nepřekáží při dřepech, a pas, který nesklouzává.</li>'
          '<li><strong>Fotbal a míčové sporty:</strong> tréninkové kalhoty se zipem u kotníku, které se navlečou přes kopačky nebo chrániče.</li>'
          '<li><strong>Cyklistika a turistika:</strong> teplákovina je spíše na doma, na kolo a do terénu existují speciální <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kalhoty</a>.</li>'
          '<li><strong>Jóga a pilates:</strong> měkké, pružné a bez tlačících švů, často s vyšším pasem.</li>'
          '<li><strong>Cesta a spaní:</strong> měkká bavlna a volnější střih, který neomezuje při dlouhém sezení.</li></ul>'
          '<h2>Praní a péče</h2>'
          '<p>Tepláky perte naruby při teplotě uvedené na štítku, nejčastěji 30 až 40 °C. Naruby se chrání potisk a povrchové vlákno, které se tvoří žmolky. Zateplený vnitřek se nesmí žehlit a nejde bez rizika sušit při vysoké teplotě. U funkčních materiálů vynechte aviváž, protože zanáší vlákna a snižuje odvod potu. Barevné a tmavé kusy perte zvlášť, aby neodbarvily světlé oblečení. Při sušení kalhoty vytáhněte do tvaru a nechte schnout na vzduchu, jinak se mohou srazit. Žmolky odstraňte holicím strojkem na textil.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupovat bavlněné tepláky na intenzivní trénink, kde se spotí a stanou se těžkými.</li>'
          '<li>Volit příliš široký střih na běh, v němž nohavice překáží.</li>'
          '<li>Nekontrolovat délku nohavice a pak ji zkracovat.</li>'
          '<li>Prát funkční materiál s aviváží.</li>'
          '<li>Spoléhat na údaj o velikosti, aniž byste porovnali rozměry.</li>'
          '<li>Pořizovat zateplené kalhoty, i když je budete nosit převážně v teple.</li></ul>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Tepláky se často objevují ve slevách, ale ve slevě mizí hlavně běžné velikosti a oblíbené barvy. Na Sportece vidíte nabídky obchodů vedle sebe, a pokud vám v jednom obchodě chybí velikost, najdete ji jinde. Před nákupem zkontrolujte složení, gramáž a pas, a jakmile kalhoty dorazí, vyzkoušejte je s ponožkami a botami, které budete nosit. Pokud zvažujete více kusů, vyplatí se zvolit základní barvy, které se dají střídat.</p>',
    faq=[('Jaké tepláky vybrat na sport?', 'Lehké a pružné z polyesteru s elastanem, s pružným pasem a ideálně se zipem u kotníku. Nechtějte široké střihy, ve kterých se nohavice při pohybu zamotávají.'),
         ('Jaký je rozdíl mezi jogger a straight?', 'Jogger má zúžené nohavice s manžetou u kotníku, straight má rovné nohavice bez zúžení. Jogger dobře sedí ke sportovním botám, straight je nenápadnější a univerzálnější.'),
         ('Jsou lepší bavlněné, nebo polyesterové tepláky?', 'Bavlna je měkčí a příjemná doma, polyester odvádí pot a rychle schne. Směs obou materiálů je kompromis, který drží tvar a hodí se na každý den.'),
         ('Srazí se tepláky v pračce?', 'Bavlněné se při prvním praní mohou mírně srazit, zvlášť při vyšší teplotě a sušení v sušičce. Perte je na doporučených 30 až 40 °C a sušte volně.'),
         ('Jak vybrat velikost?', 'Změřte pas, boky a délku vnitřního švu a porovnejte s tabulkou značky. U bavlněných kalhot počítejte s malou rezervou, u elastických stačí standardní velikost.'),
         ('Co jsou zateplené tepláky?', 'Mají uvnitř huňatou vrstvu, například fleece nebo froté. Hodí se na chladné dny a pobyt venku, ale v teple se v nich snadno přehřejete.'),
         ('Jak dlouho mají nohavice být?', 'Mají končit nad botou nebo se jemně nabírat u kotníku. Neměly by zametat zem, protože se rychle odírají a špiní.'),
         ('Jak odstranit žmolky z teplákoviny?', 'Použijte holicí strojek na textil nebo jemný hřeben. Žmolkům předejdete praním naruby a vynecháním aviváže u funkčních materiálů.'),
         ('Co nosit s teplákami na zimu?', 'Pod ně termoprádlo, nahoře mikinu a nepromokavou nebo větruodolnou bundu. Teplákovina sama větru neodolá, proto jí pomozte svrchní vrstvou.'),
         ('Jak vybrat dětské tepláky?', 'Se zesíleným kolenem, pružným pasem a mírnou rezervou na růst. Manžetu u kotníku lze vyhrnout a nohavice po roce stále poslouží.'),
         ('Mohu tepláky nosit i do práce?', 'Záleží na firemním dress codu. V uvolněném prostředí poslouží jednobarevné tepláky z kvalitní směsi se střihem straight nebo jogger, v oficiálním prostředí se nehodí.')],
)

# ------------------------------------------------------------------ dresy
NEW['dresy'] = dict(long=True,
    title='Dresy: fotbalové, hokejové, basketbalové | Sporteka',
    desc='Dresy klubů, reprezentací a lig: fotbal, hokej, basketbal, americké sporty. Replika, retro i tréninkové dresy, nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Dres</strong> je oblečení, které spojuje sport a identitu: hráč v něm nastupuje na hřiště, fanoušek ho nosí v hledišti i ve městě. Pod jedním slovem se skrývají velmi různé výrobky, od odolného tréninkového trika přes volnou fanouškovskou repliku až po přiléhavý střih, jaký dostávají hráči při zápase. Rozdíl se projeví v pohodlí, materiálu i tom, jak dres vydrží praní.</p>'
          '<p>Na Sportece najdete fotbalové, hokejové, basketbalové a retro dresy a u každého vidíte nabídky více českých obchodů. K hokejovým kouskům patří <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>, ke každodennímu nošení <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/mikiny/">mikiny</a> a <a href="/teplaky/">tepláky</a>. Širší výběr je v kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>',
    guide='<h2>Jaké dresy se prodávají</h2>'
          '<p>Rozhodující je, kdo bude dres nosit a k čemu. Fanoušek na tribunu vybírá jiný kus než hráč, který bude v dresu trénovat. Dítě, které roste, potřebuje jiný střih než dospělý sběratel. Dresy se dělí podle sportu, podle typu výrobku i podle toho, zda jde o aktuální sezónu, nebo retro. Vždy ale stojí za kontrolu, jaký materiál a jaká velikostní tabulka k nim patří.</p>'
          + T(['Sport', 'Co dres obsahuje', 'Kam se hodí'], [
              ['Fotbal', 'lehký prodyšný materiál, znak klubu, číslo a jméno hráče', '<a href="/fotbal/">fotbal</a>, tribuna, trénink, každodenní nošení'],
              ['Hokej', 'delší střih, volnější rukávy, silnější vzorování', '<a href="/hokej/">hokej</a>, ledová plocha i fanzóna'],
              ['Basketbal', 'bezrukávová, nad kolena, široké průramky', '<a href="/basketbal/">basketbal</a>, hala i ulice'],
              ['Americký fotbal a ragby', 'objemné rukávy a výrazné číslování', '<a href="/ragby-a-americky-fotbal/">ragby a americký fotbal</a>'],
              ['Cyklistika', 'krátký nebo dlouhý rukáv, kapsy na zádech, zip', '<a href="/cyklisticke-dresy/">cyklistické dresy</a>']]) +
          '<h2>Replika, autentický dres a retro</h2>'
          '<ul><li><strong>Replika neboli stadium dres</strong> je určena pro fanoušky. Má volnější střih, odolnější materiál a znaky bývají vyšité nebo nažehlené. Nosí se pohodlně celý den.</li>'
          '<li><strong>Autentický (match, authentic) dres</strong> vychází z toho, co mají hráči na hřišti: těsnější střih, lehčí a prodyšnější materiál, často pokročilé technologie odvodu potu. Bývá dražší a citlivější na pračku.</li>'
          '<li><strong>Retro a klasické dresy</strong> kopírují vzhled historických dresů a jsou oblíbeným sběratelským a módním kouskem. Z tohoto segmentu pocházejí například dresy lig NBA a NHL v historických barvách.</li>'
          '<li><strong>Tréninkový dres</strong> je jednodušší, bez složitých znaků a často levnější na obnovu. Hodí se pro týmy a děti, protože snese časté praní.</li>'
          '<li><strong>Brankářský dres</strong> má zesílené rukávy a loketní vycpávky, aby chránil při pádech.</li></ul>'
          '<h2>Fotbalové dresy</h2>'
          '<p>Fotbalový dres je lehké triko s výrazným znakem a sponzorským logem. Domácí a hostující varianty se liší barvou, třetí dres bývá experimentální. Při výběru sledujte rok sezóny, protože dresy se každý rok obměňují a staré se postupně přestávají vyrábět. K dresu se běžně skupují <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>, <a href="/kopacky/">kopačky</a> a <a href="/fotbalove-mice/">fotbalové míče</a>. Pokud nakupujete pro dětský tým, vezměte stejnou variantu pro všechny, aby barvy sedly.</p>'
          '<h2>Hokejové dresy</h2>'
          '<p>Hokejový dres je delší, aby ho šlo zasunout do kalhot, a má široké rukávy, které se nepřetahují přes chrániče. Zápasové modely jsou z tvrdšího materiálu, fanouškovské z lehčího. Hráči, kteří jej budou nosit přes výstroj, potřebují větší velikost než u běžného trika. Další vybavení najdete v kategoriích <a href="/hokejove-chranice/">hokejové chrániče</a>, <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>, <a href="/hokejove-brusle/">brusle</a> a <a href="/hokejove-suveniry-a-karty/">suvenýry a karty</a>. U brankářů pak pomohou <a href="/hokejove-brankarske-vybaveni/">brankářské vybavení</a>.</p>'
          '<h2>Basketbalové dresy</h2>'
          '<p>Basketbalový dres je bezrukávový set se šortkami. Dres bývá volný a dlouhý, aby nepřekážel při skocích a střelbě. Retro dresy z amerických lig se často nosí jako módní doplněk k tričku nebo mikině. Pokud jej chcete nosit ve městě, vyberte větší velikost a kombinujte s volnějšími kalhotami nebo <a href="/sportovni-kratasy/">sportovními kraťasy</a>. K tréninku patří <a href="/basketbalove-mice/">basketbalové míče</a> a <a href="/basketbalova-obuv/">basketbalová obuv</a>.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Velikostní systémy se liší podle značky a sportu. Americké střihy bývají velké a dlouhé, evropské fotbalové užší. Autentické dresy sedí těsněji než repliky, takže se u nich často volí o velikost víc. Spolehlivé je změřit hrudník a délku trupu a porovnat s tabulkou produktu. U dětí počítejte s růstem a zvolte raději větší velikost, protože dres má sedět volněji. U dámských dresů sledujte, zda je střih určen pro ženy, nebo jde o unisex variantu.</p>'
          + T(['Údaj', 'Jak změřit', 'Poznámka'], [
              ['Obvod hrudníku', 'v nejširším místě, pod pažemi', 'určuje základní velikost'],
              ['Délka trupu', 'od ramene po spodní okraj', 'důležité u basketbalu a hokeje'],
              ['Šířka ramen', 'mezi švy rukávů', 'rozhoduje o pohodlí při pohybu'],
              ['Délka rukávu', 'od ramene po manžetu', 'u dlouhých rukávů a brankářů']]) +
          '<h2>Materiály a potisk</h2>'
          '<p>Většina dresů je z polyesteru, který odvádí pot, rychle schne a drží barvu. Fotbalové modely mají lehká síťovaná místa pro lepší větrání, hokejové a basketbalové silnější úplet. Logo a číslování bývají vyšité, nažehlené nebo potištěné. Potisk je lehčí, ale citlivější na teplotu při žehlení a v sušičce. Vyšívané znaky vydrží víc, ale zvyšují váhu. U vlastního jména a čísla na zádech sledujte, zda je potisk oficiální, protože u některých klubů se používá pouze schválený font.</p>'
          '<h2>Dresy podle sezóny a počasí</h2>'
          '<p>Letní fotbalový dres s krátkým rukávem je nejlehčí varianta, ale na podzimní tribunu nestačí. Pod dres s krátkým rukávem si můžete obléct <a href="/funkcni-tricka/">funkční triko</a> s dlouhým rukávem, na něj v chladu přidat <a href="/sportovni-bundy/">sportovní bundu</a> nebo mikinu. Hokejový dres se naopak nosí v chladných halách, kde se hodí silnější materiál. Basketbalový dres bez rukávů je skvělý do tělocvičny, na ven se hodí spíše přes tričko. Pokud dres používáte při běhu nebo sportu v horku, vybírejte lehké síťované varianty a vyhněte se silným nažehlovacím potiskům, které se hůř větrají.</p>'
          '<h2>Dresy v týmu a pro školu</h2>'
          '<p>Při pořizování souprav pro tým je nejdůležitější jednotnost. Všechny kusy by měly pocházet z jedné série, aby se shodovaly odstíny barev a tvar znaků. Počítejte s tím, že hráči mají různou postavu, a objednejte několik velikostí s rezervou. Sady dresů v kombinaci s kraťasy a štulpnami se prodávají jako komplet, což je pro kluby praktické. Pokud si potisk řešíte zvlášť, vybírejte materiál, který potisk snese. Školní soutěže a firemní turnaje často stačí jednoduché barevné dresy bez znaků, které se rozliší čísly. Pro cvičení ve škole se hodí také <a href="/soupravy/">soupravy</a> a <a href="/sportovni-kratasy/">kraťasy</a>.</p>'
          '<h2>Další sporty a doplňky</h2>'
          '<p>Dresy se nenosí jen ve fotbalu a hokeji. V <a href="/florbal/">florbalu</a>, <a href="/volejbal/">volejbalu</a> a <a href="/hazena/">házené</a> se používají lehké týmové dresy, často s číslem na zádech i na hrudi. V <a href="/baseball-a-softball/">baseballu a softballu</a> se nosí knoflíkové dresy a v ragby odolné silnější vzorované svrchní kusy. Fanoušci pak k dresu často přidávají šály, čepice a další doplňky, například <a href="/cepice-a-celenky/">čepice a čelenky</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají značky ' + B(('mitchell-ness', 'Mitchell &amp; Ness'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('fanatics', 'Fanatics'), ('errea', 'Errea'), ('force', 'Force'), ('outerstuff', 'Outerstuff'), ('silvini', 'Silvini'), ('joma', 'Joma'), ('kipsta', 'Kipsta'), ('merco', 'Merco'), ('siroko', 'Siroko')) + '. Mitchell &amp; Ness je spojován s retro dresy amerických lig, Fanatics s licencovaným fanouškovským oblečením. Outerstuff obvykle vyrábí dětské dresy lig. Nike, Adidas a Puma jsou velcí dodavatelé klubů a reprezentací, Errea a Joma často vybavují menší týmy. Silvini a Siroko jsou známé spíše cyklistickým oblečením, Kipsta je značka obchodního řetězce Decathlon a nabízí tréninkové dresy pro amatérské týmy. Stejně jako u každé značky se vyplatí kontrolovat konkrétní model.</p>'
          '<h2>Praní a údržba dresu</h2>'
          '<p>Dres perte naruby ve vlažné vodě, nejlépe na šetrný program a bez aviváže, která zanáší funkční vlákna. Potisk a nažehlené logo nežehlete přímo. Pokud je nutné, žehlete jen naruby při nízké teplotě a přes tenkou látku. Nesušte v sušičce, protože teplo způsobuje zvlnění znaku a smrštění materiálu. Světlé a tmavé dresy perte odděleně, protože polyester snadno přebírá barvu. Sběratelské a retro kusy skladujte rozvěšené na ramínku, ne přeložené na ostrých hranách, kde se zlomí potisk.</p>'
          '<h2>Pro koho jaký dres</h2>'
          '<p>Fanoušek, který chce dres nosit do práce nebo na tribunu, uspokojí replika s volným střihem. Hráč do amatérské ligy bude potřebovat funkční tréninkový nebo zápasový dres se znakem týmu. Sběratel hledá historické modely, často s číslem a jménem legendárního hráče. Rodiče malých fanoušků ocení dětské velikosti a odolný materiál. Pokud nechcete platit za licencovaný dres, existují jednobarevné týmové dresy, které lze doplnit vlastním číslem.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Kupovat autentický dres jen kvůli vzhledu, přestože sedí těsně a hůř se pere.</li>'
          '<li>Neověřit sezónu a koupit starší dres, i když byl požadován aktuální.</li>'
          '<li>Spolehnout se na velikostní označení a nezkontrolovat rozměry.</li>'
          '<li>Prát dres v sušičce a zničit tím potisk.</li>'
          '<li>Objednat dětský dres těsně, bez rezervy na růst.</li>'
          '<li>Nechat si na dres natisknout jméno bez ověření podmínek vrácení.</li></ul>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Dresy se prodávají v různých verzích, a proto stejný klub nabízí několik variant za různé ceny. Na Sportece vidíte nabídky obchodů vedle sebe a můžete porovnat verzi, velikosti skladem a dobu doručení. Při personalizaci jména a čísla zjistěte, zda je možné zboží vrátit. Sledujte také rok sezóny, protože po skončení sezóny se zboží obvykle zlevňuje a zbývají odlišné velikosti.</p>',
    faq=[('Čím se liší replika od autentického dresu?', 'Replika má volnější střih a odolnější materiál a je určená pro fanoušky. Autentický dres odpovídá hráčskému provedení, sedí těsněji a je lehčí. Obě verze mají stejný vzhled, ale liší se pohodlím a technologiemi.'),
         ('Jakou velikost dresu vybrat?', 'Změřte hrudník a délku trupu a porovnejte s tabulkou výrobce. U autentických dresů často vyberte o velikost větší, u replik obvykle stačí obvyklá velikost.'),
         ('Jak prát dres s potiskem?', 'Naruby ve vlažné vodě a šetrném programu, bez aviváže. Potisk nežehlete přímo a nesušte v sušičce, aby se znak nezvlnil.'),
         ('Co jsou retro dresy?', 'Jsou to dresy, které kopírují vzhled historických sezón. Oblíbené jsou u sběratelů i jako módní kousek. Typicky se vyrábějí pro americké ligy (NBA, NFL, MLB, NHL).'),
         ('Jak dres sedí na hokeji?', 'Hokejový dres je delší a volnější, aby ho šlo nosit přes chrániče. Pokud ho nosíte přes výstroj, vybírejte větší velikost.'),
         ('Hodí se basketbalový dres do města?', 'Ano, nosí se jako módní doplněk přes tričko nebo mikinu. Vyberte volnější velikost a kombinujte s kraťasy nebo tepláky.'),
         ('Mohu si dres nechat označit jménem?', 'Většina obchodů nabízí vlastní jméno a číslo. Zjistěte předem, zda je možné zboží s potiskem vrátit, protože personalizované kusy se často nevracejí.'),
         ('Jaký je rozdíl mezi domácím a hostujícím dresem?', 'Domácí dres má klasické barvy klubu, hostující se liší barvou, aby se týmy na hřišti nepletly. Třetí dres bývá odvážnější a limitovaný.'),
         ('Jak dlouho se prodává dres aktuální sezóny?', 'Klub obvykle mění dresy každý rok, takže po skončení sezóny se zboží zlevňuje a postupně mizí. Výprodej se týká zejména méně běžných velikostí.'),
         ('Jaké dresy vybrat pro děti?', 'Odolné, pratelné, s mírnou rezervou na růst. Pro malé hráče stačí tréninková varianta, pro fanoušky licencovaná replika v dětské velikosti.'),
         ('Jak skladovat sběratelský dres?', 'Rozvěšený na ramínku, mimo přímé slunce, ve vzdušné skříni. Přeložený dres se může na ohybu zlomit hlavně v místě potisku.')],
)
