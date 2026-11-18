"""sporteka.cz — wave 32a (18. 11. 2026): long texts for tarpy, kosmeticke-tasky, nepromokave-vaky, filtry-na-vodu, hydrovaky,
termosky-na-jidlo. General true facts only, no prices, no product counts. Product figures are quoted as the maker's own data.
Water filters: the text says what a filter removes and what it does not, follows the makers' data and never promises safe
water. Brands linked only if present in src/texts/znacky.json, the rest plain text.

Sources:
- Mil-Tec Tarp PE ripstop 3 x 3 m (military.eu listings): PVC-coated polyester, about 1.6 kg, 19 attachment points
- Sea to Summit Ultra-Sil Nano Tarp Poncho (seatosummit.com): 15D, 145 x 265 cm, 230 g, hood, tarp or rain gear
- Sea to Summit support article "How should I correctly close a dry bag roll top closure": fold over the seal strip, roll at
  least two more times, clip the buckle; Big River product page: avoid submersion, water can seep through any roll-top;
  Big River: 420D nylon with TPU laminate, white interior, D-rings
- IP code (IEC 60529) summaries: IPX4 splashing, IPX6 powerful jets, IPX7 temporary immersion up to 1 m, IPX7 does not imply IPX6
- Letiště Praha "Letiště do kapsy" (June 2026) + novinky.cz / echo24.cz: 100 ml containers in one resealable transparent bag of
  max. 1 l; Terminal 2 (Schengen) allows one container up to 2 l since 1. 10. 2025
- Deuter Wash Bag II (deuter.com): stow-away hook, removable mirror, 2.5 l; Sea to Summit Ultra-Sil Hanging Toiletry Bag:
  hook, shatterproof detachable mirror, 30D siliconised Cordura nylon, zips and seams not waterproof
- Sawyer FAQ: 0.1 micron hollow fibre stops bacteria and protozoa, not viruses; a wetted filter that may have frozen should be
  replaced; Katadyn BeFree: 0.1 micron hollow fibre, about 2 l/min, about 1000 l (maker's claim); LifeStraw Go 2.0: membrane
  about 4000 l, activated carbon about 100 l (maker's claim)
- Katadyn Micropur Forte MF 1T: chlorine (DCCNa) + silver, 1 tablet per litre, 30 min for bacteria and viruses, 2 h for Giardia
  or very cold water, for clear water only; CDC: Cryptosporidium is very resistant to chlorine
- Deuter Streamer / Streamer II reservoirs: 1.5 / 2.0 / 3.0 l, slide closure, full-width opening, Streamer II made by HydraPak
  for Deuter, reversible; CamelBak care page: tablets or baking soda, brushes, dry disassembled, freezer if it cannot dry
- Salomon Soft Flask 500 ml: TPU, bite valve, collapses as you drink, 42 mm and 28 mm neck variants
- Thermos: preheat with boiling water about 5 minutes, never microwave stainless steel; Stainless King 470 ml food jar about
  9 h hot / 14 h cold; FUNtainer 290 ml about 5 h hot / 7 h cold (maker's data via retailers)
Left out (not verifiable): dimensions of the Czechoslovak celta vz. 60, hydrostatic head of individual tarps, IP ratings of
individual dry bags, dishwasher safety of Deuter reservoirs, heat retention of Esbit, Zopa and Nils Camp jars, lifetime of
Sawyer and Quell filters, whether Micropur Forte works against Cryptosporidium (the maker gives no figure).
"""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ tarpy
NEW['tarpy'] = dict(long=True,
    title='Tarpy a celty – plachty na kemp a nad hamaku',
    desc='Tarpy, celty a plachty nad hamaku: tvary, rozměry, materiály a jak je napnout. Porovnejte nabídky českých obchodů na jednom místě.',
    intro='<p><strong>Tarp</strong> je samostatná plachta s poutky po obvodu, kterou napnete mezi stromy, trekové hole nebo na kolíky. Chrání před deštěm a sluncem, ale nemá podlahu ani stěny jako stan. Proto je lehčí, rychleji se staví a pod ním se dá vařit, sedět nebo spát s výhledem ven. Česky se mu často říká celta, hlavně pokud jde o odolnou plachtu ve vojenském stylu. Menší tarpy se kupují jako střecha nad hamaku, větší jako přístřešek pro celou skupinu.</p>'
          '<p>V kategorii jsou lehké tarpy z tenkého silikonovaného nylonu, pevné celty z polyesteru s nátěrem, plachty nad hamaku i pončo, které se dá rozložit na přístřešek. Zastoupené jsou značky jako Sea to Summit, Mil-Tec, MFH, Robens, Jurek, Cocoon nebo '
          + B(('husky', 'Husky')) +
          '. Ke každé plachtě uvidíte nabídky českých e-shopů. Tarpy patří mezi <a href="/stanove-doplnky/">stanové doplňky</a> a hodí se ke <a href="/hamaky/">hamakám</a> i ke <a href="/stany/">stanům</a>.</p>',
    guide='<h2>Tarp, celta, nebo stan?</h2>'
          '<p>Stan je uzavřený prostor s podlahou a obvykle i s moskytiérou. Tarp je jen střecha. Výhodou je hmotnost a volnost: na stejnou plochu stačí zlomek materiálu a pod plachtou se dá stát, sedět u vařiče nebo sušit věci. Nevýhodou je, že při větru s deštěm může voda přijít z boku a že vás nechrání před hmyzem. Kdo spí pod tarpem na zemi, potřebuje podložku pod sebe, ideálně karimatku a kus fólie, a v létě často i <a href="/moskytiery/">moskytiéru</a>.</p>'
          '<p>Slovo celta se v češtině používá volně. Někdo tak říká každé plachtě na kempování, jiný jen vojenským plachtám s maskovacím vzorem. V obchodech najdete pod názvem celta i lehké turistické tarpy, takže se vyplatí číst parametry, ne jen název. Rozhodující je rozměr, materiál, počet úchytů a hmotnost.</p>'
          '<h2>Tvary a rozměry</h2>'
          + T(['Tvar', 'Typický rozměr', 'Kdy se hodí'], [
              ['Čtverec', '3 × 3 m', 'nejvíc způsobů postavení, přístřešek pro dva až tři lidi'],
              ['Obdélník', 'kolem 3 × 2 m nebo 3 × 4 m', 'jednoduché A nad jedním spáčem, skupinová střecha'],
              ['Šestiúhelník (hex)', 'délka kolem 3,5 m', 'nad hamaku, kryje konce a odvádí vodu'],
              ['Diamant / asymetrický', 'úhlopříčka kolem 3 m', 'lehká střecha nad hamaku nebo bivakem'],
              ['Pončo-tarp', 'zhruba 1,5 × 2,5 m', 'pláštěnka na cestu a nouzová střecha večer']]) +
          '<p>Čtvercová plachta tři krát tři metry je univerzální. Dá se z ní postavit stříška, klasické áčko, „stan“ uzavřený z jedné strany i nízký úkryt proti větru. Obdélník je jednodušší a nad jedním člověkem stačí. Šestiúhelníkový tarp se dělá hlavně pro hamaku: je delší než síť a jeho cípy se dají stáhnout dolů, aby voda nestékala po lanech do spacáku.</p>'
          '<p>Rozměr volte podle toho, co pod plachtou chcete mít. Jeden člověk na karimatce vystačí s menším obdélníkem. Pro hamaku je potřeba, aby plachta přesahovala síť na obou koncích, jinak boční déšť zatéká. Pro společné vaření a sezení s přáteli dává smysl velký čtverec nebo plachta 3 × 4 m.</p>'
          '<h2>Materiály a hmotnost</h2>'
          '<p>Nejlehčí tarpy jsou z tenkého nylonu napuštěného silikonem, často s označením 15D nebo 20D podle tloušťky vlákna. Sea to Summit například uvádí u modelu Ultra-Sil Nano Tarp Poncho rozměr 145 × 265 cm a hmotnost 230 g. Taková plachta se vejde do kapsy batohu, ale je citlivější na oděr a jiskry z ohně. Silikonovaný nylon se navíc za mokra mírně natahuje, takže se během noci vyplatí šňůry dotáhnout.</p>'
          '<p>Na opačném konci jsou plachty z polyesteru s nátěrem PVC nebo PU. Jsou odolnější, snesou hrubé zacházení a obvykle mají víc úchytů. Mil-Tec Tarp 3 × 3 m má podle údajů prodejců 19 úchytných bodů a váží kolem 1,6 kg. Na tábor nebo k autu to nevadí, na několikadenní přechod s batohem už ano. Mezi tím jsou polyesterové tarpy s PU nátěrem, které se nenatahují a snesou víc než ultralehký nylon.</p>'
          '<p>U nepromokavosti výrobci uvádějí vodní sloupec v milimetrech. Pro střechu, ze které voda stéká, stačí nižší hodnota než u podlahy stanu. Důležitější je, zda jsou švy podlepené nebo utěsněné a zda jsou úchyty v rozích zesílené. Právě v rozích plachta při větru trpí nejvíc.</p>'
          '<h2>Jak tarp napnout</h2>'
          '<ol><li>Mezi dva stromy natáhněte hřebenovou šňůru ve výšce zhruba prsou. U nízkých úkrytů stačí výška kolen.</li>'
          '<li>Přes šňůru přehoďte plachtu nebo ji zavěste za poutka uprostřed, aby byla rovnoměrně rozložená.</li>'
          '<li>Rohy vypněte kotevními šňůrami ke kolíkům. Začněte protilehlými rohy, aby se plachta netočila.</li>'
          '<li>Dotáhněte šňůry tak, aby plachta neměla záhyby, ve kterých se drží voda.</li>'
          '<li>Stranu proti větru stáhněte níž k zemi, závětrnou nechte otevřenou.</li></ol>'
          '<p>Bez stromů se tarp staví na trekové hole nebo na teleskopické tyče, které se prodávají zvlášť. Hodí se posuvné uzly, například prusík na hřebenové šňůře, nebo plastové napínáky. Díky nim jde plachtu posunout a dotáhnout bez rozvazování. Kolíky a šňůry bývají v balení jen u některých modelů, další najdete mezi <a href="/stanove-kolky/">stanovými kolíky</a>.</p>'
          '<h2>Tarp nad hamakou</h2>'
          '<p>Hamaka a tarp jsou častá dvojice pro lehké spaní v lese. Plachta se věší výš než síť, aby se pod ní dalo pohodlně vlézt, a napíná se na vlastní šňůru, ne na lana hamaky. Kapky stékající po laně se zastaví o takzvané odkapávací šňůrky nebo o kousek látky uvázaný na lano. Kdo chce mít klid i za bouřky, vybírá šestiúhelníkový tarp nebo plachtu s „dveřmi“, které se dají zavřít na koncích. Plachty a doplňky ke spaní ve visu najdete v kategorii <a href="/hamaky/">hamaky</a>.</p>'
          '<h2>Bezpečnost a pravidla</h2>'
          '<p>Než plachtu napnete, podívejte se nahoru. Suché větve nad místem spaní mohou ve větru spadnout. Pod tarpem se nesmí rozdělávat oheň, jiskry propálí nylon i polyester a plachta může chytit. Vařič používejte na okraji, kde odchází pára a spaliny. Pamatujte také, že spaní venku a nocování mimo kempy upravují místní pravidla, v chráněných územích bývají přísnější.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Mokrou plachtu po návratu rozložte a nechte uschnout. Sbalená vlhká látka plesniví a nátěr se odlupuje. Bláto po zaschnutí oklepejte nebo opláchněte vodou, saponát a pračku použijte jen tehdy, když to výrobce dovoluje. Drobnou díru po jiskře přelepte opravnou páskou určenou pro daný materiál. Silikonované tkaniny potřebují jiné lepidlo než polyester s PU nátěrem.</p>'
          '<h2>Co k tarpu přibalit</h2>'
          '<p>Samotná plachta nestačí. Počítejte s hřebenovou šňůrou o délce aspoň osm až deset metrů a se čtyřmi až šesti kotevními šňůrami po dvou až třech metrech. Hodí se tenká lanka z dyneemy nebo polyesteru, která se ve vlhku málo natahují. K tomu lehké kolíky a dva nebo tři napínáky. Kdo spí na zemi, dá si pod karimatku tenkou fólii nebo podlážku, aby neležel v rose a blátě. Na kolo a na vodu se tarp balí do nepromokavého obalu, aby se nenasákl dřív, než ho postavíte.</p>'
          '<p>Šňůry si nachystejte doma. Na rohy plachty je uvažte předem a na konce udělejte smyčky, do kterých jde vsunout kolík. V lese pak stavba trvá pár minut i za tmy. Reflexní šňůry jsou v noci lépe vidět a nikdo o ně nezakopne. Pro skupinu se vyplatí jedna velká plachta nad ohništěm a vařičem a každý spí pod vlastní menší, aby v noci nikoho nerušil.</p>'
          '<p>Na krátké přestávky stačí tarp hodit přes šňůru a dva rohy zatížit kameny. Na noc ho ale vždy pořádně vypněte, protože vítr se v noci často otočí. Pokud čekáte silný déšť, otočte nižší stranu proti směru, odkud mraky přicházejí.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Při srovnání se dívejte na rozměr po rozložení, hmotnost bez obalu a šňůr, materiál, počet úchytů a to, co je v balení. Pozor na názvy: slovo tarp se objevuje i u věcí, které nejsou přístřeškem, například u tréninkových plachet na hokej nebo u bot. Tropika přes stan nebo moskytiéru je určená k jednomu konkrétnímu výrobku a jako samostatný tarp se nehodí. Kdo chce nocovat úplně bez stanu, spojí tarp s <a href="/karimatky-a-matrace/">karimatkou</a> a <a href="/spaci-pytle/">spacákem</a>, případně s bivakovacím vakem.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Plachta napnutá vodorovně, bez spádu. Voda se v ní drží a při větru plachta tluče.</li>'
          '<li>Šňůry uvázané natvrdo bez možnosti dotažení, nylon se v noci povolí.</li>'
          '<li>Příliš malý tarp nad hamaku, konce zůstanou mokré.</li>'
          '<li>Vaření nebo oheň přímo pod plachtou.</li>'
          '<li>Sbalení mokré celty na několik dní.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi tarpem a celtou?', 'V praxi žádný pevný. Celtou se často myslí odolná plachta ve vojenském stylu, tarpem lehká turistická plachta. Rozhodují parametry, ne název.'),
        ('Jak velký tarp potřebuji?', 'Pro jednoho člověka na zemi stačí menší obdélník. Nad hamaku volte plachtu delší než síť. Pro skupinu se hodí čtverec 3 × 3 m nebo větší.'),
        ('Může tarp nahradit stan?', 'V létě a za klidného počasí ano, pokud vám nevadí hmyz a otevřený prostor. Při větru s deštěm a v zimě je stan pohodlnější.'),
        ('Na co tarp uvázat, když nejsou stromy?', 'Na trekové hole nebo teleskopické tyče a šňůry ke kolíkům. Některé tarpy mají vyztužené otvory přímo pro hrot hole.'),
        ('Proč se nylonový tarp v noci povolí?', 'Silikonovaný nylon se za vlhka mírně natahuje. Pomůže napínák nebo posuvný uzel, kterým šňůru dotáhnete bez rozvazování.'),
        ('Dá se pod tarpem vařit?', 'Na vařiči na okraji plachty ano, s dobrým větráním. Otevřený oheň pod plachtu nepatří, jiskry ji propálí.'),
        ('Jak tarp postavit nad hamaku?', 'Na samostatnou šňůru výš než síť, s přesahem na obou koncích. Na lana hamaky dejte odkapávací šňůrku, aby po nich nestékala voda.'),
        ('Jak se o tarp starat?', 'Po použití ho nechte vyschnout rozložený, nečistoty opláchněte vodou a díry lepte páskou určenou pro daný materiál.'),
        ('Co je pončo-tarp?', 'Pláštěnka s kapucí, kterou lze po rozepnutí napnout jako malou plachtu. Hodí se jako nouzová střecha pro jednoho.'),
        ('Kde koupit tarp nebo celtu?', 'Sporteka u každé plachty ukáže nabídky českých e-shopů, nákup dokončíte u vybraného obchodu.'),
    ])

# ------------------------------------------------------------------ kosmeticke-tasky
NEW['kosmeticke-tasky'] = dict(long=True,
    title='Kosmetické a toaletní tašky na cesty',
    desc='Toaletní a kosmetické tašky na cesty, do posilovny i na kemp: s háčkem, zrcátkem a kapsami. Velikosti, materiály a tekutiny v letadle.',
    intro='<p><strong>Toaletní taška</strong> drží pohromadě kartáček, pastu, šampon, holení a drobnou kosmetiku, aby se nic nerozlilo po batohu a vše bylo po ruce v koupelně. Cestovní modely bývají ploché, mají několik oddílů a háček, za který se dají zavěsit na dveře, věšák nebo větev. Menší kosmetické taštičky slouží na make-up, léky nebo nabíječky. Sportovci je nosí v tašce do posilovny, turisté v batohu a vodáci v nepromokavém pytli.</p>'
          '<p>Sporteka vedle sebe ukazuje nabídky českých obchodů. Najdete tu toaletní tašky na zavěšení, rozkládací modely, lehké taštičky z tenkého nylonu i voděodolné tašky. Prodávají je značky '
          + B(('deuter', 'Deuter'), ('fjallraven', 'Fjällräven'), ('helly-hansen', 'Helly Hansen')) +
          ', Rains, Sea to Summit, LifeVenture nebo Eleven. Kategorie patří ke <a href="/sportovni-tasky/">sportovním taškám</a>, dobře se kombinuje s <a href="/cestovni-tasky/">cestovními taškami</a> a s rychleschnoucími <a href="/rucniky/">ručníky</a>.</p>',
    guide='<h2>Typy toaletních tašek</h2>'
          + T(['Typ', 'Jak vypadá', 'Pro koho'], [
              ['Závěsná rozkládací', 'plochá, rozbalí se do výšky, háček nahoře', 'kemp, hostely, sdílené koupelny'],
              ['Klasická na zip', 'obdélník s jedním nebo dvěma oddíly', 'víkendy, posilovna, služební cesty'],
              ['Ultralehká', 'tenký nylon, minimum kapes', 'turistika, kolo, cesta s batohem'],
              ['Voděodolná', 'pogumovaná látka, svařované nebo podlepené švy', 'vodáci, mokré šatny, déšť'],
              ['Kosmetická taštička', 'malé pouzdro, často kufříkový tvar', 'make-up, léky, drobnosti']]) +
          '<h2>Háček, zrcátko a kapsy</h2>'
          '<p>Na cestách se nejvíc osvědčí háček. V kempu nebo na chatě nebývá kam věci položit a umyvadla jsou mokrá. Tašku zavěsíte na dveře, sprchovou tyč nebo větev a vše máte před sebou. Deuter u modelu Wash Bag II uvádí háček, který se dá zastrčit do tašky, odnímatelné zrcátko a objem 2,5 litru. Sea to Summit u závěsné tašky Ultra-Sil Hanging Toiletry Bag popisuje háček pro zavěšení v koupelně, na větvi nebo na zrcátku auta a nerozbitné odnímatelné zrcátko.</p>'
          '<p>Kapsy rozhodují o tom, jestli taška pomáhá, nebo jen schovává nepořádek. Síťové kapsy jsou průhledné, takže vidíte, co v nich je, a vlhké věci v nich lépe vysychají. Gumičky drží lahvičky ve stoje. Oddělená kapsa na zip se hodí na holicí strojek nebo léky. Kdo cestuje s kontaktními čočkami, ocení malé pevné pouzdro, aby se nic nepromáčklo.</p>'
          '<h2>Velikost podle délky cesty</h2>'
          '<p>Na víkend nebo do posilovny stačí malá taška na kartáček, deodorant a gel. Na týden je potřeba místo na šampon, krém, opalovací přípravek a lékárničku pro běžné potíže. Rodina na dovolené často volí jednu velkou rozkládací tašku a několik malých pouzder, která se dají rozdělit do zavazadel. Objem udávaný v litrech je jen orientační. Lépe se porovnávají vnější rozměry a počet oddílů.</p>'
          '<p>Na dlouhé trasy s batohem se vyplatí každý gram. Ultralehké tašky z tenkého nylonu váží desítky gramů, ale látka není nepromokavá a zipy propustí vodu. Sea to Summit u zmíněného modelu výslovně uvádí, že zipy a švy nejsou nepromokavé. Pokud chcete mít kosmetiku opravdu v suchu, dejte ji do <a href="/nepromokave-vaky/">nepromokavého vaku</a>.</p>'
          '<h2>Materiály</h2>'
          '<p>Nejčastější je polyester nebo nylon, někdy s nátěrem na vnitřní straně. Snadno se otírá a rychle schne. Tašky s pogumovaným povrchem, jaké dělá například Rains, odolají vodě zvenčí a dobře se myjí. Bavlněné a kožené kosmetické taštičky vypadají pěkně, ale špatně snášejí vylitý šampon a vlhko. Uvnitř sportovní tašky, kde se potkají mokré boty s ručníkem, je lepší syntetika.</p>'
          '<h2>Tekutiny v příručním zavazadle</h2>'
          '<p>Kdo letí jen s kabinovým zavazadlem, musí počítat s pravidly bezpečnostní kontroly. Obecně platí, že tekutiny, gely a spreje se nosí v nádobkách do 100 ml a všechny musí být v jednom průhledném uzavíratelném sáčku o objemu nejvýš 1 litr. Letiště Praha uvádí, že na Terminálu 2 je od října 2025 navíc povolena jedna nádoba až do 2 litrů. Na Terminálu 1 a na řadě jiných letišť ale platí původní limit. Pravidla se liší podle letiště i aerolinky, proto si je před odletem ověřte na jejich webu.</p>'
          '<p>Pro toaletní tašku z toho plyne praktický závěr. Do kabiny si připravte samostatný průhledný sáček s malými lahvičkami, který jde při kontrole snadno vyndat. Velkou toaletní tašku dejte do odbaveného zavazadla. Tuhé alternativy, například mýdlo nebo šampon v kostce, se do limitu tekutin nepočítají a ušetří místo.</p>'
          '<h2>Jak tašku sbalit, aby nic neteklo</h2>'
          '<ol><li>Lahvičky naplňte jen do tří čtvrtin. V letadle i v horách se mění tlak a plné lahve se snadno otevřou.</li>'
          '<li>Pod víčko dejte kousek fólie nebo lahvičky s pojistkou otočte do zavřené polohy.</li>'
          '<li>Tekutiny dejte do jedné kapsy a suché věci do druhé.</li>'
          '<li>Holicí strojek a nůžky zakryjte krytkou, aby nepropíchly látku.</li>'
          '<li>Po cestě tašku vybalte a nechte otevřenou vyschnout.</li></ol>'
          '<h2>Do posilovny a na kemp</h2>'
          '<p>Ve sportovní tašce se taška na drogerii dostane do styku s mokrým ručníkem a botami. Volte proto snadno omyvatelný materiál a síťovou kapsu, ve které se věci po sprše nezapaří. Malé tašky se dají připnout karabinkou k popruhu. V kempu se hodí taška, která stojí sama, nebo naopak závěsná, protože podlaha sprch bývá mokrá. Na vodácké výpravy patří drogerie do vaku, který přežije převržení lodi.</p>'
          '<h2>Co patří do toaletní tašky na túru</h2>'
          '<p>Na vícedenní túru s batohem se balí jinak než na dovolenou u moře. Méně věcí a menší balení. Základ tvoří kartáček, malá pasta, kousek mýdla, deodorant, opalovací krém, balzám na rty a malý rychleschnoucí ručník. K tomu kapesníky, vlhčené ubrousky, repelent a pár náplastí. Léky, které užíváte pravidelně, mějte v samostatném pouzdře, aby nebyly roztroušené mezi kosmetikou. Lékárničku na celou skupinu je lepší nosit zvlášť, výbavu do ní najdete v kategorii <a href="/prvni-pomoc/">první pomoc</a>.</p>'
          '<p>Mycí prostředky v přírodě používejte s rozmyslem. Mydlinky nepatří přímo do potoka ani jezera, i když je přípravek označený jako biologicky odbouratelný. Vodu si naberte do hrnce, umyjte se v dostatečné vzdálenosti od břehu a vodu vylijte do půdy. Kartáček a pastu použijte stejně. Prázdné obaly odneste s sebou.</p>'
          '<p>Pro delší pobyt mimo civilizaci si spočítejte, kolik čeho opravdu spotřebujete. Pasta na týden se vejde do malé cestovní tuby, šampon do lahvičky s objemem pár desítek mililitrů. Opalovací krém je naopak potřeba víc, než se zdá, hlavně na horách a u vody.</p>'
          '<h2>Rodina a děti</h2>'
          '<p>Při cestování s dětmi se osvědčí jedna velká taška na společnou drogerii a malé taštičky pro každé dítě. Dítě má svůj kartáček, hřeben a krém a samo se o ně stará. Barvy nebo jména pomohou, aby se věci nepletly. Do velké tašky pak patří šampon, sprchový gel a opalovací krém pro všechny. Kdo cestuje s miminkem, potřebuje zvláštní tašku na pleny a ubrousky, ta ale patří spíš do přebalovací tašky než do toaletní.</p>'
          '<h2>Oddělte, co nemá být spolu</h2>'
          '<p>Toaletní taška by neměla být odkladištěm na všechno. Nabíječky, sluchátka a powerbanku dejte do samostatného pouzdra, vylitý šampon by je poškodil. Doklady a peníze do toaletní tašky nepatří vůbec, protože ji necháváte v koupelně nebo ve sdílené sprše. Ostré věci, jako jsou nůžky, pinzeta nebo pilník, mějte v pevném pouzdře. Do kabiny letadla je ostatně nemusíte smět vzít, pravidla upravuje letiště.</p>'
          '<p>Na kole a na lodi se hodí taška bez tvrdých dílů, která se přizpůsobí místu v brašně nebo ve vaku. Zrcátko a výztuhy přidávají váhu i objem. Pro sportovce, kteří chodí do bazénu nebo do sauny, je dobrá taška s průhlednou kapsou nebo celá z omyvatelného materiálu, kterou jde vzít až pod sprchu.</p>'
          '<p>Při dlouhé cestě se vyplatí mít kosmetiku rozdělenou do dvou tašek. V malé jsou věci na každý den, ve velké zásoby na doplňování. Malou nosíte do sprchy, velká zůstane v zavazadle. Taška tak vydrží čistší a nemusíte ji každý večer vybalovat celou.</p>'
          '<h2>Péče</h2>'
          '<p>Vylitý šampon nebo krém vytřete hned, než zaschne v kapsách. Většinu syntetických tašek stačí vymýt vlažnou vodou s trochou mýdla a nechat uschnout otevřené. Pračku používejte jen tehdy, když to výrobce povoluje, zrcátko a vyztužení dna ji obvykle nesnášejí. Zipy občas promažte, sůl a zbytky mýdla je časem zaseknou.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte rozměry, počet oddílů, přítomnost háčku a zrcátka, materiál a hmotnost. U stejného modelu se často liší jen barva. Pozor na tašky, které mají ve jménu slovo „kosmetická“, ale jsou spíš kabelkou nebo pouzdrem na nabíječky. Hledáte-li sadu kosmetiky na cesty nebo repelent, podívejte se do kategorie <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>. Na větší cesty se hodí také <a href="/cestovni-tasky/">cestovní tašky</a> s oddělenou kapsou na boty.</p>',
    faq=[
        ('Jak velkou toaletní tašku vybrat?', 'Na víkend stačí malá taška na základní drogerii. Na týden a víc volte model s několika oddíly, rodina obvykle ocení velkou rozkládací tašku.'),
        ('K čemu je háček na toaletní tašce?', 'Tašku zavěsíte na dveře, věšák nebo větev, takže ji nemusíte pokládat na mokré umyvadlo nebo zem.'),
        ('Kolik tekutin smím vzít do příručního zavazadla?', 'Obecně nádoby do 100 ml v jednom průhledném sáčku do 1 litru. Některá letiště pravidla uvolňují, proto je před letem ověřte u letiště a aerolinky.'),
        ('Je toaletní taška nepromokavá?', 'Většina ne. Látka může vodu odpuzovat, ale zipy a švy ji propustí. Na vodu patří taška do nepromokavého vaku.'),
        ('Jak zabránit vytečení šamponu?', 'Lahvičky plňte jen částečně, pod víčko dejte fólii a tekutiny držte v jedné kapse odděleně od suchých věcí.'),
        ('Jakou tašku do posilovny?', 'Menší omyvatelnou tašku se síťovou kapsou, ve které věci po sprše vysychají.'),
        ('Dá se toaletní taška prát v pračce?', 'Jen pokud to výrobce dovoluje. Obvykle stačí vymýt vodou s mýdlem a nechat otevřenou uschnout.'),
        ('Jaký je rozdíl mezi toaletní a kosmetickou taškou?', 'Toaletní taška je na drogerii pro celou cestu. Kosmetická taštička bývá menší, na make-up, léky nebo drobnosti.'),
        ('Kam dát léky na cestu?', 'Do samostatného pouzdra, odděleně od kosmetiky. Pravidelně užívané léky mějte v příručním zavazadle, ne v odbaveném kufru.'),
        ('Kde koupit toaletní tašku?', 'Sporteka u každé tašky zobrazí nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ nepromokave-vaky
NEW['nepromokave-vaky'] = dict(long=True,
    title='Nepromokavé vaky a dry bagy',
    desc='Nepromokavé vaky, dry bagy a lodní pytle s rolovacím uzávěrem: objemy, materiály, správné zavření a co znamená IPX. Nabídky e-shopů.',
    intro='<p><strong>Nepromokavý vak</strong>, anglicky dry bag, je pytel z vodotěsné látky, který se zavírá srolováním horního okraje a zacvaknutím přezky. Chrání oblečení, spacák, doklady a elektroniku na lodi, na paddleboardu, na kole i v batohu za deště. Vodáci mu říkají lodní vak. Malé vaky slouží jako obal na mobil a klíče, velké pojmou celou výbavu na několikadenní splutí řeky.</p>'
          '<p>V kategorii jsou lehké vaky do batohu, odolné lodní pytle s popruhem, vodotěsné batohy, kompresní vaky i sady několika barevných obalů. Nabízejí je '
          + B(('osprey', 'Osprey'), ('deuter', 'Deuter'), ('husky', 'Husky')) +
          ', Sea to Summit, Silva, Highlander, Aqua Marina nebo Yate. U každého vaku vidíte nabídky českých e-shopů. Hodí se k <a href="/kajaky-a-cluny/">kajakům a člunům</a>, k <a href="/paddleboardy/">paddleboardům</a> a jako vnitřní obal do <a href="/turisticke-batohy/">turistických batohů</a>.</p>',
    guide='<h2>Jak funguje rolovací uzávěr</h2>'
          '<p>Vak nemá zip, protože ten by vodu nezastavil. Okraj se několikrát přeloží a sroluje, tím vznikne těsnění, a konce se spojí přezkou. Sea to Summit ve svém návodu radí přeložit okraj přes těsnicí pásek a pak ho srolovat ještě nejméně dvakrát stejným směrem. Teprve potom se zacvakne přezka. Méně otočení znamená, že voda může projít.</p>'
          '<p>Před zavřením z vaku vytlačte vzduch. Vak se pak lépe vejde do batohu a na lodi méně překáží. Pokud chcete, aby plaval, nechte v něm trochu vzduchu. Výrobci ale upozorňují, že rolovací uzávěr není určen k dlouhému ponoření. Sea to Summit u vaku Big River píše, že při ponoření může voda proniknout uzávěrem jakéhokoli dry bagu.</p>'
          '<h2>Typy vaků</h2>'
          + T(['Typ', 'Typický objem', 'Použití'], [
              ['Ultralehký vak', '1–35 l', 'vnitřní obal v batohu, třídění věcí'],
              ['Lodní vak s popruhem', '5–40 l', 'kajak, raft, paddleboard, pláž'],
              ['Vodotěsný batoh', '20–60 l', 'vodácké výpravy, kolo v dešti'],
              ['Kompresní vak', '5–35 l', 'spacák a oblečení zmenšené na minimum'],
              ['Pouzdro na mobil', 'velikost telefonu', 'mobil a doklady u vody']]) +
          '<p>Ultralehké vaky jsou z tenkého silikonovaného nylonu a slouží hlavně uvnitř batohu. Chrání před deštěm a vlhkem, ale ostré předměty a hrubý povrch skal je mohou prodřít. Lodní vaky jsou z tlustší látky s laminací, mívají D-kroužky na připoutání k lodi a popruh přes rameno. Vodotěsné batohy mají nosný systém, takže se s nimi dá i chodit.</p>'
          '<p>Na řece se kromě vaků používají i pevné plastové barely se šroubovacím víkem. Jsou tuhé, takže chrání křehké věci a jídlo před rozmáčknutím. Na záda nebo do batohu se ale hodí hůř než měkký vak.</p>'
          '<h2>Materiály</h2>'
          '<p>Lehké vaky se šijí z nylonu napuštěného silikonem nebo s PU nátěrem. Odolné vaky jsou z polyesteru nebo nylonu laminovaného TPU nebo PVC. Sea to Summit například uvádí u řady Big River nylon 420D s laminací TPU, bílý vnitřek, ve kterém se věci lépe hledají, a D-kroužky na uchycení. PVC je těžší a tužší, TPU bývá pružnější a za mrazu tolik netvrdne. Svařované švy jsou spolehlivější než šité a podlepené.</p>'
          '<p>Průhledné okénko pomáhá najít správný vak bez otvírání. Na delší výpravy je praktické mít vaky různých barev: jeden na spaní, druhý na oblečení, třetí na jídlo. Kdo nechce kupovat jednotlivě, vybere sadu tří menších vaků.</p>'
          '<h2>Co znamená IPX</h2>'
          '<p>Některé vaky a pouzdra mají označení podle normy IEC 60529. Druhá číslice za písmeny IP udává ochranu před vodou. IPX4 znamená odolnost proti stříkající vodě z jakéhokoli směru, IPX6 proti silnému proudu vody a IPX7 proti dočasnému ponoření do hloubky zhruba jednoho metru. Vyšší číslo neznamená automaticky splnění nižších stupňů: výrobek s IPX7 nemusí vydržet silný proud. Většina rolovacích vaků žádné IP označení nemá a výrobce jen popisuje, k čemu jsou určené. Řiďte se jeho údaji.</p>'
          '<h2>Jak vybrat objem</h2>'
          '<p>Na mobil, klíče a peněženku stačí vak do 5 litrů. Na náhradní oblečení a ručník na jednodenní splutí volte 10 až 20 litrů. Spacák se vejde do 10 až 15 litrů podle typu, péřový méně, syntetický víc. Na několikadenní výpravu lodí je lepší víc menších vaků než jeden obří, který se špatně připevňuje a v němž nic nenajdete. Při výběru počítejte s tím, že část výšky vaku spotřebuje rolování, takže plný objem nevyužijete.</p>'
          '<h2>Na lodi, na kole a v batohu</h2>'
          '<p>Na lodi přivažte vak k lodi karabinou nebo popruhem za D-kroužek. Při převržení tak neuplave. Na paddleboardu se vak dává pod gumy na přídi. Na kole se používají speciální vaky do brašen nebo samotné nepromokavé brašny, které najdete mezi <a href="/brasny-na-kolo/">brašnami na kolo</a>. V batohu slouží lehký vak jako vložka: do ní dáte spacák a suché oblečení na večer, a i když batoh promokne, zůstanou suché. Vodákům se kromě vaku hodí <a href="/plovaci-vesty/">plovací vesta</a> a <a href="/neoprenove-boty-a-ponozky/">neoprenové boty</a>.</p>'
          '<h2>Jak sbalit výbavu na vodu</h2>'
          '<p>Na vodácký výlet rozdělte věci podle toho, kdy je budete potřebovat. Do malého vaku patří mobil, klíče, peníze a doklady, ten mějte připnutý přímo u sedačky. Do středního vaku náhradní oblečení, bundu a ručník pro případ, že se loď převrhne. Do velkého vaku spacák, karimatku a věci na večer. Jídlo a nádobí dejte zvlášť, aby se nemísilo s oblečením. Při každé přestávce pak otevíráte jen jeden vak a ostatní zůstanou zavřené a suché.</p>'
          '<p>Těžké věci ukládejte do lodi nízko a doprostřed, lehké vaky dopředu a dozadu. Vaky připoutejte, ale tak, aby se daly rychle odepnout, pokud by bylo potřeba loď vyprázdnit. Delší popruhy a lana, ve kterých by se mohla zamotat noha, na lodi nenechávejte volně ležet.</p>'
          '<p>Doklady, telefon a autoklíč zabalte ještě do malého pouzdra nebo uzavíratelného sáčku uvnitř vaku. I když se do velkého vaku dostane trocha vody, nejcennější věci zůstanou suché. Klíče od auta mívají elektroniku, kterou voda zničí, a jejich náhrada bývá drahá a zdlouhavá.</p>'
          '<h2>Jak vak vyzkoušet</h2>'
          '<p>Nový vak si před výpravou otestujte doma. Dejte dovnitř suchý papírový ubrousek, vak správně srolujte a na chvíli ho pod sprchou polévejte ze všech stran. Pak ho na pár sekund ponořte do vany. Když je ubrousek suchý, víte, že vak i váš způsob zavírání fungují. Stejnou zkoušku zopakujte u starších vaků na začátku sezóny, protože laminace a těsnicí pásek časem stárnou.</p>'
          '<p>Na raftech a při organizovaných sjezdech řek bývá výbava pro skupinu převážena v barelech a velkých vacích. Zeptejte se půjčovny, co poskytuje, a s sebou si vezměte jen menší osobní vak na věci, které chcete mít u sebe. Kdo jede na vodu poprvé, ocení i rady od zkušenějších. Například že ručník a suché ponožky na večer jsou důležitější než druhé tričko.</p>'
          '<p>Na kajaku se vaky ukládají do úzkých prostor v přídi a zádi. Tam se lépe hodí protáhlé vaky menšího průměru než široké válce. Některé mají tvar kužele, aby se do špičky lodi dobře zasunuly. Před cestou si vyzkoušejte, kolik vaků se do lodi vejde a jak se vytahují.</p>'
          '<h2>Vak v batohu a ve stanu</h2>'
          '<p>Mimo vodu má nepromokavý vak víc využití, než se zdá. Do batohu ho dejte jako vložku a zabalte do něj spacák, který by mokrý nehřál. Ve stanu oddělí mokré věci od suchých. Naplněný oblečením poslouží jako polštář. Na kole zase ochrání věci v brašně, která není úplně vodotěsná. Na pláži pojme mokré plavky a ručník, aby nenamočily zbytek tašky. Díky různým velikostem se dá vak použít jako organizér, ve kterém má každá věc své místo.</p>'
          '<h2>Péče</h2>'
          '<p>Po splutí vak opláchněte sladkou vodou, hlavně po moři, a nechte ho uschnout otevřený a obrácený naruby. Uvnitř zavřeného vlhkého vaku se rychle objeví plíseň a zápach. Vak neskladujte složený na stejném místě roky, v přehybech se laminace časem láme. Malé díry v lehkém nylonu se dají zalepit opravnou páskou, u PVC lepidlem pro daný materiál.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Okraj srolovaný jen jednou nebo dvakrát.</li>'
          '<li>Vak přeplněný až k okraji, takže se nedá pořádně srolovat.</li>'
          '<li>Spoléhání na lehký vak při plavání nebo dlouhém ponoření.</li>'
          '<li>Ostré předměty bez obalu, které látku propíchnou.</li>'
          '<li>Vak uložený mokrý a zavřený.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Srovnávejte objem, materiál a tloušťku látky, typ švů, úchyty a popruhy, hmotnost a to, zda výrobce uvádí odolnost proti ponoření. Pozor na zboží s „dry bag“ v názvu, které je ve skutečnosti brašna na kolo nebo pouzdro na telefon. Pro kemp a delší výpravy se hodí i další <a href="/kempingove-doplnky/">kempingové doplňky</a>.</p>',
    faq=[
        ('Kolikrát se má dry bag srolovat?', 'Výrobci obvykle radí přeložit okraj a srolovat ho ještě nejméně dvakrát, celkem tedy zhruba třikrát, a pak zacvaknout přezku.'),
        ('Dá se nepromokavý vak ponořit?', 'Krátké namočení většina lodních vaků vydrží, dlouhé ponoření ne. Rolovacím uzávěrem může voda časem proniknout.'),
        ('Co znamená IPX7 u vaku?', 'Že výrobce deklaruje odolnost proti dočasnému ponoření zhruba do jednoho metru podle normy IEC 60529. Většina rolovacích vaků toto označení nemá.'),
        ('Jak velký vak na vodu potřebuji?', 'Na mobil a klíče do 5 litrů, na oblečení na den 10–20 litrů. Na delší výpravu je lepší víc menších vaků.'),
        ('Plave nepromokavý vak?', 'Pokud v něm necháte vzduch, obvykle ano. Na lodi ho ale vždy přivažte, aby při převržení neuplaval.'),
        ('Jaký je rozdíl mezi lehkým a lodním vakem?', 'Lehký vak je tenký a slouží hlavně v batohu. Lodní vak je z tlustší laminované látky s úchyty a popruhem.'),
        ('Můžu do vaku dát elektroniku?', 'Ano, ale raději v dalším menším obalu a s vytlačeným vzduchem. Na mobil u vody se hodí samostatné pouzdro.'),
        ('Jak vak vyčistit?', 'Opláchněte ho sladkou vodou, otočte naruby a nechte uschnout otevřený. Skladujte suchý.'),
        ('Potřebuji vak, když mám nepromokavý batoh?', 'Na vodu ano. Batoh odolá dešti, ale při převržení lodi nebo dlouhém dešti se voda dostane dovnitř zipem nebo švy. Spacák a doklady proto balte do vaku.'),
        ('Kde koupit nepromokavý vak?', 'Sporteka u každého vaku ukáže nabídky českých e-shopů a nákup dokončíte v obchodě podle své volby.'),
    ])

# ------------------------------------------------------------------ filtry-na-vodu
NEW['filtry-na-vodu'] = dict(long=True,
    title='Filtry na vodu na turistiku a cesty',
    desc='Outdoorové filtry na vodu, filtrační láhve, brčka i tablety. Co odstraní, co ne, jak je používat a čistit. Nabídky českých obchodů.',
    intro='<p><strong>Filtr na vodu</strong> do přírody propouští vodu přes membránu s velmi malými otvory, která zachytí bakterie a prvoky z potoka nebo studánky. Existují kapesní filtry na našroubování na láhev, filtrační láhve, brčka, gravitační vaky i tablety, které vodu chemicky dezinfikují. Každý typ si poradí s něčím jiným. Žádný z nich neudělá z jakékoli vody bezpečnou pitnou vodu, a proto je dobré vědět, co přesně umí.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů na filtry a tablety značek Katadyn, LifeStraw, Sawyer, Highlander, Quell nebo Water-to-GO. Najdete tu i náhradní filtrační vložky a aktivní uhlí. Filtry patří k <a href="/outdoor-doplnky/">outdoorovým doplňkům</a> a doplňují výbavu na <a href="/vareni-v-prirode/">vaření v přírodě</a>. Údaje v textu vycházejí z informací výrobců.</p>',
    guide='<h2>Co filtr zachytí a co ne</h2>'
          '<p>Většina outdoorových filtrů používá dutá vlákna, tedy svazek tenkých trubiček s póry kolem 0,1 až 0,2 mikrometru. Výrobce Sawyer vysvětluje, že bakterie a prvoci jsou větší než póry jeho filtru, a proto je membrána zachytí. Viry jsou ale menší a filtrem s póry 0,1 mikrometru projdou. Totéž platí pro většinu podobných filtrů: jsou to filtry, ne čističky vody.</p>'
          + T(['Druh znečištění', 'Membránový filtr', 'Tablety na bázi chloru'], [
              ['Bakterie', 'zachytí podle údajů výrobce', 'zničí po předepsané době'],
              ['Prvoci (např. Giardia)', 'zachytí podle údajů výrobce', 'Giardie až po delším působení'],
              ['Cryptosporidium', 'zachytí podle údajů výrobce', 'chlor na něj téměř nepůsobí'],
              ['Viry', 'běžný filtr nezachytí', 'zničí po předepsané době'],
              ['Chemikálie, kovy, soli', 'neodstraní', 'neodstraní'],
              ['Kal a písek', 'zanese filtr', 'sníží účinnost']]) +
          '<p>Chemické látky, jako jsou pesticidy, ropné produkty, těžké kovy nebo dusičnany, membránový filtr neodstraní. Filtry s aktivním uhlím zlepší chuť a výrobci uvádějí, že sníží obsah chloru a některých organických látek. Kontaminovanou vodu z kanálu nebo z potoka pod polem či továrnou ale ani uhlík neopraví. Mořskou vodu žádný z běžných outdoorových filtrů neodsolí.</p>'
          '<h2>Typy filtrů</h2>'
          '<p><strong>Kapesní filtr</strong> se našroubuje na láhev nebo na měkký vak. Vodu do vaku naberete z potoka a pak ji mačkáním protlačíte filtrem. Sem patří Sawyer Mini nebo filtr Katadyn BeFree, u kterého výrobce uvádí póry 0,1 mikrometru, průtok kolem 2 litrů za minutu a životnost zhruba 1000 litrů.</p>'
          '<p><strong>Filtrační láhev</strong> má filtr přímo ve víčku. Naplníte ji z potoka a pijete přes náustek. Je to nejjednodušší řešení na výlet a na cesty. LifeStraw u láhve Go 2.0 uvádí životnost membrány kolem 4000 litrů a uhlíkové vložky kolem 100 litrů. Uhlík se tedy mění mnohem častěji.</p>'
          '<p><strong>Filtrační brčko</strong> se ponoří přímo do vody a pije se přes něj. Je lehké a levné, ale nedá se jím naplnit láhev na vaření a pití z kaluže vleže není pohodlné. <strong>Gravitační filtr</strong> je vak, který pověsíte na větev, a voda protéká filtrem do čisté láhve sama. Hodí se pro skupinu nebo do kempu. <strong>Filtrační kanystr</strong> funguje podobně, jen má pevné stěny.</p>'
          '<h2>Tablety a kapky</h2>'
          '<p>Tablety vodu nefiltrují, ale dezinfikují. Katadyn u tablet Micropur Forte MF 1T uvádí kombinaci chloru a stříbra, jednu tabletu na litr a dobu působení 30 minut na bakterie a viry. Proti Giardiím nebo ve velmi studené vodě je potřeba čekat dvě hodiny. Tablety jsou určené do čiré vody, kalnou je potřeba nejdřív přefiltrovat nebo nechat usadit. Na parazita Cryptosporidium chlor podle hygienických institucí téměř nepůsobí, tady pomůže membránový filtr nebo převaření.</p>'
          '<p>Proto se často kombinuje filtr a tablety: filtr zachytí prvoky a kal, tableta vyřeší viry. To má smysl hlavně na cestách mimo Evropu nebo u vody, kde se pohybují lidé a zvířata. Pozor na záměnu: některé tablety a kapky obsahují jen stříbro a slouží ke konzervaci už pitné vody v kanystru, ne k dezinfekci vody z potoka. Čtěte, k čemu je přípravek určen.</p>'
          '<h2>Převaření</h2>'
          '<p>Nejjednodušší a nejspolehlivější způsob, jak zničit mikroorganismy, je vodu převařit. Potřebujete ale <a href="/varice-a-kartuse/">vařič</a>, palivo a čas. Převaření neodstraní chemikálie a kal. Kdo vaří večer jídlo, může zároveň převařit vodu na čaj a filtr používat přes den na pití.</p>'
          '<h2>Jak vybírat vodu</h2>'
          '<ul><li>Berte vodu z tekoucího pramene nebo potoka, ne z kaluže a stojatých tůní.</li>'
          '<li>Vyhněte se úsekům pod obcemi, pastvinami, poli a průmyslem.</li>'
          '<li>Kalnou vodu nechte usadit nebo ji přelijte přes šátek, filtr se pak tak rychle neucpe.</li>'
          '<li>Neplňte láhev filtrovanou vodou rukama, kterými jste předtím brali vodu z potoka.</li>'
          '<li>Pokud si nejste jistí, raději vodu převařte nebo nepijte.</li></ul>'
          '<h2>Čištění a zamrznutí</h2>'
          '<p>Filtr se zanáší a průtok postupně klesá. Kapesní filtry se čistí zpětným proplachem čistou vodou, u některých stačí filtrem zatřást v čisté vodě. Postupujte podle návodu výrobce, protože tlak nebo kartáček mohou membránu poškodit. Až je průtok i po vyčištění malý nebo uplyne udávaná životnost, filtr vyměňte.</p>'
          '<p>Na zimní túry pozor na mráz. Sawyer uvádí, že filtr, který už byl jednou mokrý, může zamrznutím prasknout a poškození není vidět. Pokud máte podezření, že filtr zmrzl, doporučuje ho vyměnit. V chladu ho noste u těla a v noci si ho vezměte do spacáku. Stejné pravidlo se týká i filtračních lahví.</p>'
          '<h2>Filtrace z potoka krok za krokem</h2>'
          '<ol><li>Vyberte tekoucí, co nejčistší místo a naberte vodu do špinavé láhve nebo vaku.</li>'
          '<li>Pokud je voda kalná, nechte ji chvíli stát, aby se kal usadil na dno.</li>'
          '<li>Našroubujte filtr a vodu protlačte nebo nechte protéct do čisté nádoby.</li>'
          '<li>Dávejte pozor, aby se kapky z neupravené vody nedostaly na náustek nebo do čisté láhve.</li>'
          '<li>Po použití filtr podle návodu propláchněte a nechte ho oschnout, než ho na delší dobu uklidíte.</li></ol>'
          '<p>Mějte vždy dvě nádoby, jednu na neupravenou a druhou na upravenou vodu, a nepleťte si je. Pomůže barevné označení nebo různé typy lahví. Ruce si před manipulací s čistou lahví umyjte nebo očistěte gelem. Většina nákaz na cestách nevznikne z filtru, ale z rukou a nádobí.</p>'
          '<p>Filtrovanou vodu pijte co nejdřív a nádoby udržujte čisté. Upravená voda ponechaná v teple několik dní v láhvi s neumytým hrdlem znovu nabere bakterie. Na vícedenní túře proto láhve a vaky občas vypláchněte horkou vodou a nechte vyschnout.</p>'
          '<h2>Filtrační láhev ve městě a na cestách</h2>'
          '<p>Některé filtrační láhve se kupují hlavně do města, kde je voda z kohoutku pitná, ale člověku nechutná. Filtr s aktivním uhlím zlepší chuť a pach chloru. Takové láhve nejsou určené na potok, proto si u výrobce ověřte, na jakou vodu je model stavěný. Na cesty do zemí, kde voda z vodovodu není pitná, si zjistěte doporučení pro konkrétní zemi. Často se tam kombinuje filtr s tabletami nebo se pije balená voda.</p>'
          '<p>Filtr se hodí i doma jako součást nouzové výbavy pro případ výpadku vodovodu nebo povodní. Pamatujte ale, že voda po povodni může obsahovat chemikálie a ropné látky, které membrána nezachytí. V takové situaci se řiďte pokyny hygienické stanice a obce, ne jen filtrem. Pro nouzovou zásobu jsou vhodné i kanystry s pitnou vodou a tablety na její konzervaci.</p>'
          '<p>Se psem nebo s dětmi na výletě počítejte s větší spotřebou vody. Filtrační láhev pro jednoho pak nestačí a hodí se spíš gravitační vak nebo kapesní filtr s větším měkkým vakem. Pes by neměl pít z kaluží a stojatých tůní, protože i pro něj je taková voda riziková.</p>'
          '<h2>Náhradní vložky</h2>'
          '<p>U filtrační láhve nebo kapesního filtru počítejte s tím, že vložka je spotřební materiál. Při nákupu zjistěte, zda jsou náhradní vložky běžně k dostání a kolik vydrží. Uhlíková část se mění častěji než membrána. Starý filtr se pozná podle toho, že voda teče pomalu i po vyčištění, nebo že výrobce udávaný počet litrů už překročil. Na delší výpravu se vyplatí mít náhradní vložku nebo tablety jako zálohu, kdyby se filtr ucpal nebo zmrzl.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte velikost pórů, deklarovaný průtok, životnost v litrech, cenu náhradních vložek a to, zda filtr pasuje na běžné lahve. Ověřte, jestli je v balení i měkký vak nebo láhev. Filtrační láhve na kolo se liší objemem a tím, jestli je lze mačkat. U tablet sledujte, na jaký objem vody jsou určené a jak dlouho musí působit. Na pití po celý den se hodí i <a href="/hydrovaky/">hydrovak</a>, na teplé nápoje <a href="/lahve-a-termosky/">láhve a termosky</a>. Filtr nepatří mezi zdravotnické prostředky a výsledek vždy závisí na zdroji vody.</p>',
    faq=[
        ('Odstraní filtr na vodu viry?', 'Běžné outdoorové filtry s póry kolem 0,1 mikrometru viry nezachytí. Na viry se používají tablety, převaření nebo speciální čističky.'),
        ('Je voda po filtraci vždy pitná?', 'Ne. Filtr zachytí bakterie a prvoky, ale ne chemikálie, kovy ani soli. Výsledek záleží na zdroji vody a na správném použití.'),
        ('Jak dlouho vydrží filtr?', 'Výrobci udávají životnost v litrech, například Katadyn BeFree kolem 1000 l. Ve skutečnosti záleží na čistotě vody a údržbě.'),
        ('Jak dlouho působí tablety na čištění vody?', 'Katadyn u Micropur Forte uvádí 30 minut na bakterie a viry a dvě hodiny proti Giardiím nebo ve velmi studené vodě.'),
        ('Můžu filtr nechat zamrznout?', 'Raději ne. Mokrá membrána může mrazem prasknout bez viditelné známky. Výrobce Sawyer pak doporučuje filtr vyměnit.'),
        ('Co je lepší, filtrační láhev, nebo kapesní filtr?', 'Láhev je pohodlnější na jednodenní výlet. Kapesní filtr s vakem je lehčí a dá se jím naplnit víc nádob.'),
        ('K čemu je aktivní uhlí ve filtru?', 'Zlepšuje chuť a podle výrobců snižuje chlor a některé organické látky. Mikroorganismy nezachytí a mění se častěji než membrána.'),
        ('Mohu filtrovat mořskou vodu?', 'Ne. Běžné outdoorové filtry ani tablety sůl neodstraní.'),
        ('Je potřeba vodu po filtraci ještě převařit?', 'V Evropě u čistých horských pramenů obvykle stačí filtr. Pokud může voda obsahovat viry, přidejte tablety nebo ji převařte.'),
        ('Kde koupit filtr na vodu?', 'Sporteka u každého filtru a balení tablet ukáže nabídky českých e-shopů, nákup dokončíte u vybraného obchodu.'),
    ])

# ------------------------------------------------------------------ hydrovaky
NEW['hydrovaky'] = dict(long=True,
    title='Hydrovaky a měkké láhve na vodu',
    desc='Hydrovaky do batohu, vaky na vodu a soft flasky do běžecké vesty. Objemy, uzávěry, kompatibilita s batohem, čištění a zima.',
    intro='<p><strong>Hydrovak</strong> je měkký vak na vodu s hadičkou a náustkem, který se vkládá do batohu. Pijete za pochodu nebo za jízdy, aniž byste zastavovali a vyndávali láhev. Proto ho mají rádi cyklisti, turisté, skialpinisté i běžci. Menší příbuzný je soft flask, měkká láhev s ventilem, která se nosí v kapsách běžecké vesty a během pití se zmenšuje. Do kategorie patří i velké vaky na vodu do kempu.</p>'
          '<p>Sporteka ukazuje nabídky českých obchodů na hydrovaky značek '
          + B(('deuter', 'Deuter'), ('salomon', 'Salomon'), ('merco', 'Merco')) +
          ', Hydrapak, CamelBak, Sea to Summit, Silva, MFH nebo Mil-Tec. Najdete tu vaky od jednoho do tří litrů, soft flasky, vojenské vaky do pouzder MOLLE i náhradní hadičky. Hydrovak patří mezi <a href="/lahve-a-termosky/">láhve a termosky</a>, ale nejvíc se používá s <a href="/cyklisticke-batohy/">cyklistickými batohy</a> a <a href="/bezecke-vesty-a-batohy/">běžeckými vestami</a>.</p>',
    guide='<h2>Jak hydrovak funguje</h2>'
          '<p>Vak z pružného plastu má plnicí otvor, vývod dole a na něj nasazenou hadičku. Na konci hadičky je náustek s ventilem. Když skousnete a nasajete, voda teče. Když náustek pustíte, ventil se zavře. Většina náustků má navíc uzavírací páčku, aby vak v batohu nepouštěl vodu, když na něj něco zatlačí. Vak se vkládá do zvláštní kapsy u zad a hadička vede otvorem v batohu přes ramenní popruh dopředu.</p>'
          '<h2>Objem podle aktivity</h2>'
          + T(['Objem', 'Typické použití', 'Kam se vejde'], [
              ['0,25–0,75 l (soft flask)', 'běh, trail, závody', 'kapsy na ramenou vesty'],
              ['1–1,5 l', 'trail, kratší vyjížďky na kole', 'běžecké vesty, malé batohy'],
              ['2 l', 'kolo, celodenní výlety', 'cyklistické a menší turistické batohy'],
              ['3 l', 'dlouhé túry, horko, málo vody na trase', 'turistické batohy s velkou kapsou'],
              ['5 l a víc', 'kemp, zásoba vody na vaření', 'stojí nebo visí v táboře']]) +
          '<p>Deuter nabízí vaky Streamer v objemech 1,5, 2 a 3 litry. Velký vak není nutné plnit celý, ale prázdný prostor v něm šplouchá. U tří litrů počítejte s tím, že plný vak váží přes tři kila a tlačí do zad. Na kole je proto rozumné vozit tolik, kolik do další studny nebo obchodu opravdu vypijete.</p>'
          '<h2>Plnicí otvor a uzávěr</h2>'
          '<p>Dva hlavní typy jsou šroubovací víčko a posuvný uzávěr přes celou šířku vaku. Šroubovací víčko je jednoduché, ale do užšího otvoru se hůř dostane ruka s kartáčem a kostky ledu. Posuvný uzávěr, který mají například vaky Deuter Streamer, otevře vak po celé šířce. Vak se pak dá snadno naplnit, vymýt i vysušit. Druhou generaci Streamer II podle prodejců vyrábí pro Deuter firma HydraPak a vak jde obrátit naruby.</p>'
          '<p>Na hadičce se vyplatí rychlospojka. Hadičku odpojíte a vak vytáhnete z batohu, aniž byste ji museli provlékat zpátky. Spojky různých značek do sebe ale nemusí pasovat, takže náhradní díly kupujte ke konkrétnímu modelu.</p>'
          '<h2>Kompatibilita s batohem</h2>'
          '<p>Většina turistických, cyklistických a běžeckých batohů má kapsu na hydrovak, háček nebo suchý zip k zavěšení a otvor pro hadičku. Před nákupem porovnejte rozměry vaku s kapsou, hlavně u tří litrů. Široký vak v úzké kapse se nedá dobře naplnit a vytahuje se těžko. Vojenské vaky mají často vlastní obal s úchyty MOLLE a připínají se na vestu nebo batoh zvenku. Kdo nemá batoh s kapsou, může vak vložit do batohu zvlášť, ale hadičku pak musí vést pod víkem nebo zipem.</p>'
          '<h2>Soft flask do běžecké vesty</h2>'
          '<p>Soft flask je měkká láhev z TPU s ventilem v uzávěru. Salomon u modelu Soft Flask 500 ml uvádí, že se během pití stlačuje, takže voda v kapse nešplouchá. Ventil se otevře skousnutím. Stejný model se prodává s hrdlem 42 mm a 28 mm, užší hrdlo se hůř plní a myje. Soft flasky mají výhodu, že vidíte, kolik vody zbývá, a že se doplňují rychleji než vak v zadní kapse vesty.</p>'
          '<h2>Čištění</h2>'
          '<p>Hydrovak je teplé a vlhké prostředí, ve kterém se rychle množí plíseň a bakterie, hlavně po iontových nápojích. Po každém použití ho vypláchněte a nechte vyschnout. CamelBak radí používat čisticí tablety nebo roztok jedlé sody, roztokem propláchnout i hadičku a vak vydrhnout kartáčem. Pak ho rozložit a nechat vyschnout. Pokud vak nemůžete hned vysušit, výrobce doporučuje dát ho do mrazáku.</p>'
          '<ol><li>Vylijte zbytek vody a vak propláchněte teplou vodou.</li>'
          '<li>Nalijte roztok s tabletou nebo sodou a nechte ho působit podle návodu.</li>'
          '<li>Zvedněte vak nad hlavu a stiskněte náustek, aby roztok protekl hadičkou.</li>'
          '<li>Vydrhněte vak a hadičku kartáči, náustek vyjměte a omyjte zvlášť.</li>'
          '<li>Vše opláchněte čistou vodou a nechte schnout rozevřené, vak třeba na ramínku.</li></ol>'
          '<p>Myčku používejte jen tehdy, když to výrobce u konkrétního vaku uvádí. Na čištění se prodávají sady kartáčů a tablet. Zápach nového plastu obvykle zmizí po několika vypláchnutích.</p>'
          '<h2>Na kole, na běh a v kempu</h2>'
          '<p>Na horském kole je hydrovak častější než láhev v košíku. V terénu se láhev špatně vytahuje a na celoodpružených rámech na ni někdy nezbývá místo. Malé objemy, kolem jednoho a půl litru, se prodávají i do ledvinek, jako je Evoc Hip Pack Hydration Bladder. Váha je tak nízko na bocích a záda se tolik nepotí. Na silnici a gravelu stačí obvykle láhve a hydrovak se bere jen na dlouhé vyjížďky v horku.</p>'
          '<p>Při běhu se hydrovak v zadní kapse vesty ozývá šploucháním, pokud v něm zůstane vzduch. Po naplnění ho proto obraťte otvorem nahoru a vzduch vymačkejte. Na kratší tréninky běžci volí dva soft flasky vpředu, na ultra závody kombinaci flasků a vaku. Před závodem se podívejte, jaké vybavení pořadatel předepisuje, některé závody určují minimální objem vody.</p>'
          '<p>V kempu se hodí velký skládací vak s kohoutkem, například Pack Tap od Sea to Summit. Naplníte ho u pramene nebo v umývárně, pověsíte na strom a máte vodu na vaření i mytí nádobí. Prázdný se srolovaný vejde do kapsy batohu. Na delší pobyt ve stanu ušetří několik cest pro vodu.</p>'
          '<p>Na skialpinismu a zimních túrách sledujte, jak rychle voda v hadičce zamrzá. Některé batohy mají kapsu na hydrovak blíž k zádům a hadičku vedou pod ramenním popruhem, aby ji hřálo tělo. Na lyžích je ale často jednodušší termoska s čajem, kterou otevřete při přestávce. Hydrovak se v zimě vyplatí spíš na kratší a rychlé výstupy, kdy se nechcete zastavovat.</p>'
          '<p>Kolik pít, záleží na teplotě, zátěži a člověku. Hydrovak pomáhá hlavně tím, že se dá pít často po malých doušcích. Snadno se ale přehlédne, kolik vody zbývá. Při plánování trasy si proto ověřte, kde se dá doplnit, a průhledný vak občas zkontrolujte.</p>'
          '<h2>První použití a náhradní díly</h2>'
          '<p>Nový vak před prvním použitím vymyjte teplou vodou, propláchněte hadičku a nechte ho vyschnout. Pachuť plastu zmizí rychleji, když do vaku dáte vodu s trochou sody nebo citronové šťávy a necháte ji chvíli stát. Pak vše důkladně opláchněte. Náustek je nejvíc namáhaná část a časem se prokousne. Vyplatí se mít náhradní náustek a uzavírací ventil, které stojí málo a vak s nimi vydrží další sezóny. Hadička se dá vyměnit celá, pokud je uvnitř zabarvená a nejde vyčistit.</p>'
          '<p>Vojenské vaky a vaky ve vlastním obalu s úchyty MOLLE prodávají značky jako MFH, Mil-Tec nebo Viper. Obal chrání vak před propíchnutím a dá se připnout na nosný systém nebo na batoh zvenku. Hodí se i pro airsoft, myslivost a dlouhé pochody. Náhradní vaky do takových obalů nemusí pasovat od jiné značky, proto si ověřte rozměry. Kdo vak nosí venku, dá přednost pevnějšímu materiálu a krytu na náustek, aby se do něj nedostala špína.</p>'
          '<p>Kdo hydrovak teprve vybírá, ať si předem ověří, zda jeho batoh má kapsu na vak. Pokud ne, lze koupit batoh rovnou s vakem v balení.</p>'
          '<h2>Hydrovak v zimě</h2>'
          '<p>Na mrazu zamrzne nejdřív voda v hadičce a v náustku. Po napití proto vyfoukněte vodu z hadičky zpět do vaku. Pomůže i zateplená hadička a izolační návlek na náustek. Hadičku veďte pod bundou nebo pod popruhem blíž k tělu. Na skialpy a zimní túry je často praktičtější termoska v batohu, protože horký čaj v ní vydrží teplý déle.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte objem, typ uzávěru, délku a průměr hadičky, náustek s uzavíracím ventilem, rychlospojku a rozměry vaku. Zjistěte, jestli jsou k dostání náhradní náustky. U soft flasků sledujte hrdlo a to, do které vesty pasují. Kromě vaku se hodí i obyčejné <a href="/cyklo-lahve-a-drzaky/">cyklolahve s držákem</a>, jako záloha na delší túry. Tam, kde chybí čistý zdroj, pomůže <a href="/filtry-na-vodu/">filtr na vodu</a>, který se dá na některé vaky našroubovat.</p>',
    faq=[
        ('Jaký objem hydrovaku zvolit?', 'Na běh 1–1,5 litru, na kolo kolem 2 litrů, na dlouhé túry v horku 3 litry. Plný třílitrový vak je ale těžký.'),
        ('Pasuje hydrovak do každého batohu?', 'Ne. Batoh potřebuje kapsu, závěs a otvor pro hadičku. Porovnejte rozměry vaku s kapsou, hlavně u tří litrů.'),
        ('Jak vyčistit hydrovak?', 'Vypláchněte ho, použijte čisticí tablety nebo roztok sody, vydrhněte vak i hadičku kartáčem a nechte vše rozložené vyschnout.'),
        ('Proč hydrovak zapáchá?', 'Zbytky vody nebo sladkých nápojů v něm zplesniví. Po každém použití ho vypláchněte a vysušte, případně uložte do mrazáku.'),
        ('Můžu do hydrovaku dát iontový nápoj?', 'Ano, ale vak pak hned vymyjte. Cukr a sůl podporují růst plísní v hadičce i v náustku.'),
        ('Jak zabránit zamrznutí hadičky?', 'Po napití vyfoukněte vodu zpět do vaku, použijte zateplenou hadičku a veďte ji blíž k tělu.'),
        ('Co je soft flask?', 'Měkká láhev s ventilem do kapes běžecké vesty. Během pití se stlačuje a nešplouchá.'),
        ('Jsou rychlospojky různých značek kompatibilní?', 'Často ne. Náhradní hadičky a náustky kupujte ke konkrétnímu modelu vaku.'),
        ('Dá se hydrovak mýt v myčce?', 'Jen pokud to výrobce u daného modelu uvádí. Jinak ruční mytí a sušení.'),
        ('Kde koupit hydrovak?', 'Sporteka u každého vaku a soft flasku zobrazí nabídky českých e-shopů. Koupíte ho v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ termosky-na-jidlo
NEW['termosky-na-jidlo'] = dict(long=True,
    title='Termosky na jídlo a termoobědáře',
    desc='Termosky na jídlo pro děti, do práce i na túry: objemy, jak dlouho drží teplo podle výrobců, předehřátí, lžíce a mytí. Nabídky e-shopů.',
    intro='<p><strong>Termoska na jídlo</strong> je nerezová nádoba s dvojitou stěnou a vakuem mezi nimi. Na rozdíl od termosky na pití má široké hrdlo, takže do ní dáte polévku, guláš, kaši nebo těstoviny a jíte přímo z ní. Teplé jídlo udrží teplé několik hodin, studené zase chladné. Používají ji děti ve škole, lidé v práci bez kuchyňky, turisté, rybáři i lyžaři, kteří nechtějí na horách platit za každý oběd.</p>'
          '<p>Na Sportece jsou nabídky českých obchodů na termosky na jídlo značek Thermos, Zopa, Esbit, Nils Camp, Laken, Highlander, Primus nebo '
          + B(('stanley', 'Stanley')) +
          '. Vybírat můžete mezi malými dětskými modely, klasickými termoskami kolem půl litru, velkými jídlonosiči i kombinovanými termoskami na jídlo i pití. Kategorie patří k <a href="/lahve-a-termosky/">lahvím a termoskám</a> a doplňuje <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>',
    guide='<h2>Jak termoska na jídlo funguje</h2>'
          '<p>Mezi vnitřní a vnější nerezovou stěnou je vakuum. To brání přenosu tepla, takže jídlo chladne jen pomalu, hlavně přes víčko. Proto mají kvalitní termosky silné izolované víko a těsnění. Čím větší objem a čím víc jídla v nádobě je, tím déle si drží teplotu. Poloprázdná termoska chladne rychleji než plná.</p>'
          '<h2>Jak dlouho drží teplo</h2>'
          '<p>Výrobci udávají, kolik hodin zůstane jídlo teplé a studené. Thermos u dětské termosky FUNtainer o objemu 290 ml uvádí přibližně 5 hodin teplé a 7 hodin studené. U modelu Stainless King o objemu 470 ml uvádí zhruba 9 hodin teplé a 14 hodin studené. Údaje platí pro předehřátou nádobu, naplněnou horkým jídlem a zavřenou celou dobu. Každé otevření a malé množství jídla dobu zkracují. Porovnávejte proto hodnoty u konkrétního modelu a berte je jako orientační.</p>'
          + T(['Objem', 'Pro koho', 'Poznámka'], [
              ['250–350 ml', 'děti do školky a školy', 'malé hrdlo, lehká, často se lžící'],
              ['400–550 ml', 'oběd do práce, svačina na túru', 'nejběžnější velikost pro dospělé'],
              ['600–800 ml', 'velký oběd, dva menší chody', 'často se šálkem a skládací lžící'],
              ['1 l a víc', 'pro dva a víc lidí, rybaření, chata', 'těžší, hodí se i na polévku pro rodinu']]) +
          '<h2>Předehřátí</h2>'
          '<p>Nejdůležitější krok, který většina lidí vynechá. Thermos radí naplnit nádobu vroucí vodou zhruba ze tří čtvrtin, nechat ji pět minut stát, vylít a teprve pak dát jídlo. Studená nerezová stěna by jinak odebrala teplo jídlu hned na začátku. Pro studená jídla platí opak: vypláchněte termosku ledovou vodou. Jídlo dávejte do termosky co nejteplejší, ideálně přímo z hrnce, ne vlažné.</p>'
          '<p>Termoska na jídlo nepatří do mikrovlnné trouby. Thermos upozorňuje, že nerez v mikrovlnce jiskří a poškodí nádobu i troubu. Jídlo ohřejte v hrnci nebo v mikrovlnce v jiné nádobě a do termosky ho přelijte.</p>'
          '<h2>Na co se dívat při výběru</h2>'
          '<ul><li><strong>Šířka hrdla:</strong> čím širší, tím snáz se jí přímo z nádoby a tím snáz se myje.</li>'
          '<li><strong>Víčko a těsnění:</strong> mělo by jít rozebrat, aby se dalo umýt i pod těsněním.</li>'
          '<li><strong>Lžíce:</strong> některé modely mají skládací lžíci uloženou ve víčku nebo v pouzdru.</li>'
          '<li><strong>Šálek nebo miska:</strong> víčko, které slouží jako miska, se hodí pro dva lidi nebo na polévku.</li>'
          '<li><strong>Vnitřní nádoby:</strong> větší jídlonosiče mají několik misek nad sebou, například na polévku a hlavní jídlo.</li>'
          '<li><strong>Povrch:</strong> matný lak nebo silikonový obal lépe drží v ruce a méně se škrábe.</li></ul>'
          '<h2>Pro děti</h2>'
          '<p>Dětské termosky mají menší objem a víčko, které dítě zvládne otevřít samo. Vyzkoušejte to doma, než termosku pošlete do školy. Některé děti nedokážou povolit pevně utažené víčko. Dejte do ní jídlo, které dítě opravdu sní, a připravte ho ráno horké. Teplotu hotového jídla před podáním ověřte, předehřátá termoska drží teplo dobře a polévka může být ještě po několika hodinách velmi horká.</p>'
          '<h2>Na túru, lyže a ryby</h2>'
          '<p>Na horách oceníte robustní termosku s pevným víkem, kterou lze nosit v batohu bez obav. Lyžaři mají rádi polévku nebo čaj v kombinované termosce, rybáři a myslivci velký jídlonosič na celý den venku. Kdo jde na několikadenní túru, obvykle termosku nebere, protože jídlo se vaří večer na vařiči. Pro takové výpravy se hodí spíš <a href="/outdoorova-strava/">outdoorová strava</a>, kterou zalijete horkou vodou. Na nápoje jsou určené <a href="/termohrnky/">termohrnky</a> a klasické termosky na pití.</p>'
          '<h2>Co do termosky dát</h2>'
          '<p>Nejlépe se v termosce drží jídla s tekutinou: polévky, guláš, chilli, rizoto, kaše nebo těstoviny s omáčkou. Tekutina drží teplo a jídlo se neslepí. Rýže a těstoviny bez omáčky během několika hodin změknou a vychladnou rychleji. Smažená a křupavá jídla v uzavřené nádobě zvlhnou, ta do termosky nepatří. Na studené jídlo se hodí jogurt s ovocem, salát nebo studená polévka.</p>'
          '<p>Termosku naplňte skoro celou, ale pod víčkem nechte kousek volného místa, aby se dala dobře zavřít a těsnění nebylo od jídla. Hutná jídla před naplněním promíchejte s trochou vývaru nebo horké vody. Když se horké jídlo uzavře a postupně chladne, vznikne uvnitř mírný podtlak. Víčko pak může jít ztuha otevřít, pomůže krátce ho povolit a znovu dotáhnout hned po naplnění.</p>'
          '<p>Na víkendovou chatu nebo na ryby se vyplatí uvařit větší množství jídla a rozdělit ho do dvou termosek. Jedna se otevře k obědu, druhá večer. Zavřená druhá termoska tak drží teplotu déle, než kdyby se jedna velká nádoba otvírala celý den.</p>'
          '<h2>Termoska, nebo obědový box?</h2>'
          '<p>Plastový nebo nerezový obědový box bez izolace je lehčí a levnější, ale jídlo v něm do oběda vystydne. Hodí se tam, kde je mikrovlnka nebo kde jíte studenou svačinu. Termoska na jídlo dává smysl všude, kde se ohřát nedá: na stavbě, ve škole bez výdejny, na sjezdovce, u vody nebo na výletě. Některé termosky jsou kombinované a zvládnou jídlo i pití. Thermos má třeba řadu Mountain se šálkem na víčku, k níž se prodávají i náhradní šálky. Velké jídlonosiče s několika nádobkami zase pojmou polévku i hlavní chod najednou.</p>'
          '<p>Kdo nosí termosku každý den do práce, ocení model, který se snadno myje a nemá mnoho dílů. Pro výlety je lepší robustní tvar s víčkem, které vydrží pád do sněhu nebo na kameny. Děti potřebují víčko, které otevřou samy, a lžíci, kterou neztratí. Lyžaři chtějí termosku, kterou otevřou i v rukavicích. Než si vyberete, promyslete, kde a jak ji budete používat nejčastěji.</p>'
          '<p>Důležité je i těsnění. Termoska, ze které při naklonění vytéká polévka, se do batohu ani do školní tašky nehodí. Výrobci obvykle uvádějí, zda je víčko vodotěsné. U levnějších modelů si to ověřte doma s vodou, než do termosky poprvé nalijete polévku.</p>'
          '<h2>Hmotnost a balení</h2>'
          '<p>Nerezová termoska není lehká. Prázdná půllitrová nádoba váží několik set gramů a s jídlem se blíží kilu. Na celodenní výlet to nevadí, do běžeckého batohu se ale nehodí. V batohu ji dávejte do střední části blízko zad a víčkem nahoru, aby případný únik nevytekl na ostatní věci. Pouzdro nebo neoprénový obal chrání lak před oděrem a ztlumí nárazy, kterým se vakuum nemusí líbit.</p>'
          '<h2>Bezpečnost jídla</h2>'
          '<p>Termoska teplo neudrží věčně. Jídlo, které se během dne ochladí na vlažnou teplotu, už nenechávejte stát další hodiny a nejezte ho druhý den. Mléčné kaše a jídla s vejci jsou citlivější než polévka. Do termosky nedávejte jídlo, které už předtím dlouho stálo na lince. Pokud chcete jídlo jen chladné, například salát nebo ovoce, může vedle termosky posloužit i <a href="/chladici-tasky/">chladicí taška</a>.</p>'
          '<h2>Mytí a péče</h2>'
          '<p>Termosku umyjte co nejdřív po jídle, zaschlé zbytky se z hrdla a těsnění dostávají těžko. Těsnění vyjměte a umyjte zvlášť, pod ním se drží zbytky jídla a zápach. Thermos u některých modelů povoluje myčku v horním koši, jinde doporučuje ruční mytí. Řiďte se návodem ke konkrétnímu modelu. Nerezovou nádobu nenechávejte namočenou celou noc a nepoužívejte drátěnku, která poškrábe povrch. Zápach po polévce pomůže odstranit roztok jedlé sody s teplou vodou.</p>'
          '<p>Termosku po umytí nechte vyschnout otevřenou. Zavřená vlhká nádoba začne páchnout. Pokud termoska přestane držet teplo a vnější stěna se po nalití horkého jídla zahřívá, vakuum se nejspíš porušilo, obvykle po pádu nebo nárazu. Taková nádoba už izolovat nebude.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte objem, deklarovanou dobu udržení tepla a chladu, šířku hrdla, příslušenství, hmotnost a návod k mytí. Pozor na položky, které jsou jen náhradním šálkem nebo víčkem k termosce, a na termosky na pití s úzkým hrdlem. Kdo na výlet potřebuje i horký nápoj, přidá k termosce na jídlo klasickou termosku z kategorie <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>',
    faq=[
        ('Jak dlouho udrží termoska jídlo teplé?', 'Záleží na modelu a objemu. Thermos uvádí u dětské termosky 290 ml zhruba 5 hodin, u modelu Stainless King 470 ml asi 9 hodin.'),
        ('Proč se termoska předehřívá?', 'Studená nerezová stěna by jídlu odebrala teplo hned na začátku. Vroucí voda na pět minut tento pokles odstraní.'),
        ('Můžu termosku na jídlo dát do mikrovlnky?', 'Ne. Nerez v mikrovlnné troubě jiskří a poškodí nádobu i troubu. Jídlo ohřejte jinde a přelijte ho.'),
        ('Jakou velikost termosky vybrat pro dítě?', 'Pro školku a školu obvykle 250–350 ml. Vyzkoušejte, zda dítě víčko samo otevře.'),
        ('Dá se termoska mýt v myčce?', 'Některé modely ano, obvykle v horním koši. Jiné výrobce doporučuje mýt ručně. Řiďte se návodem.'),
        ('Proč termoska přestala hřát?', 'Nejspíš se po pádu porušilo vakuum mezi stěnami. Poznáte to tak, že se vnější stěna po nalití horkého jídla zahřívá.'),
        ('Můžu do termosky dát studené jídlo?', 'Ano. Termoska udrží jídlo chladné, předem ji vypláchněte studenou vodou.'),
        ('Jak odstranit zápach z termosky?', 'Umyjte zvlášť těsnění a nádobu vypláchněte roztokem jedlé sody s teplou vodou. Pak ji nechte vyschnout otevřenou.'),
        ('Jaký je rozdíl mezi termoskou na jídlo a na pití?', 'Termoska na jídlo má široké hrdlo, ze kterého se dá jíst lžící. Termoska na pití má úzké hrdlo a uzávěr na nalévání.'),
        ('Kde koupit termosku na jídlo?', 'Sporteka u každé termosky zobrazí nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])
