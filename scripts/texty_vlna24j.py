"""sporteka.cz — wave 24j (5. 11. 2026): long texts for damska-kola, strechni-stany, krasobruslarske-brusle, celoodpruzena-horska-kola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ damska-kola
NEW['damska-kola'] = dict(long=True,
    title='Dámská kola: městská a trekingová, výběr rámu',
    desc='Dámská kola s nízkým průlezem: městská, cruiser a trekingová. Jak vybrat velikost rámu, počet převodů, kola a výbavu a porovnat nabídky obchodů.',
    intro='<p>Dámské kolo se pozná podle nízkého průlezu nebo zcela otevřeného rámu, přes který se dá přehodit noha bez zvedání do výšky. Hodí se každému, kdo na kolo často nasedá a sesedá, vozí nákup, jezdí v šatech nebo se zkrátka nechce při zastavení na křižovatce zamotat. Sporteka porovnává nabídky českých obchodů u městských, cruiserových a trekingových modelů, takže vidíte, jaké velikosti rámu a kol jsou právě k mání.</p>'
          '<p>V kategorii převažují značky ' + B(('storm', 'Storm'), ('davi', 'Davi'), ('canellini', 'Canellini'), ('author', 'Author')) +
          '. Pokud hledáte sportovnější jízdu, projděte <a href="/krosova-kola/">krosová kola</a> a <a href="/trekingova-kola/">trekingová kola</a>, na dojíždění pak <a href="/mestska-kola/">městská kola</a>, a pro snazší kopce <a href="/damska-elektrokola/">dámská elektrokola</a>.</p>',
    guide='<h2>Co dámský rám přináší a co ne</h2>'
          '<p>Základní myšlenka je stará: rám s nízkým nebo zakřiveným horním trubkou umožňuje nasednout bez velkého zvedání nohy. Vznikl v době, kdy ženy nosily dlouhé sukně, ale užitek má dodnes. Senioři, rodiče s dětskou sedačkou, lidé po úrazu kolene i vozící těžký náklad si na nízký průlez zvyknou velmi rychle. Za pohodlí se platí menší tuhostí rámu, protože chybí horní trubka, která konstrukci vyztužuje. U rekreační jízdy po rovině to nevadí, při prudkém šlapání ze sedla nebo s těžkým nákladem se ale rám může lehce kroutit.</p>'
          '<p>Důležité je také neplést si dámský rám s dámskou geometrií. Označení dámské často znamená jen nízký průlez, zatímco délka rámu, rozteč řídítek a tvar sedla se mezi modely liší. Mnoho žen jezdí bez problémů na unisex nebo pánských kolech, hlavně sportovnějších, a zkouška v obchodě řekne víc než štítek.</p>'
          '<h2>Typy dámských kol v nabídce</h2>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Městské kolo', 'vzpřímená poloha, blatníky, kryt řetězu, často nosič', 'každodenní dojíždění, nákup, krátké trasy'],
              ['Cruiser a retro', 'široká řídítka, pohodlné sedlo, často jedna rychlost', 'pomalá jízda po rovině, promenáda, styl'],
              ['Trekingové kolo', 'robustní rám, více převodů, 28" kola', 'výlety po silnici i lesních cestách'],
              ['Krosové kolo', 'lehčí, sportovnější poloha, odpružená vidlice', 'rychlejší jízda, smíšený povrch'],
              ['Kolo s košíkem', 'přední nebo zadní košík, nosič', 'nákup, drobné zavazadlo']]) +
          '<p>Mnoho nabídky tvoří městská kola s ocelovým rámem, jedním nebo třemi převody a košíkem. Jsou jednoduchá, nenáročná na údržbu a dobře se k nim pořizují náhradní díly. Trekingové a krosové modely mají víc převodů a lepší brzdy, proto jsou vhodnější do kopců a na delší trasy.</p>'
          '<h2>Velikost rámu a kol</h2>'
          '<p>Rám se u dámských kol udává v palcích nebo v centimetrech, například 17", 18" nebo 19". Základní orientace podle výšky postavy je u každého výrobce trochu jiná, takže hledejte tabulku přímo u modelu. Rozhodující je ale vnitřní délka nohy. Při stání nad rámem by měl být zbytek volného místa a při sezení na sedle byste se měla špičkou nebo podešví dotknout země podle toho, jak jistě se cítíte.</p>'
          '<ul><li><strong>Kola 26":</strong> menší, hravější, vhodná pro nižší postavy a starší typy městských kol.</li>'
          '<li><strong>Kola 28":</strong> nejběžnější u městských a trekingových modelů, lépe se valí a překonávají nerovnosti.</li>'
          '<li><strong>Mezi velikostmi:</strong> vyberte menší rám a vyšší sedlovku, než abyste dosahovala na pedály špičkou ve střední poloze.</li></ul>'
          '<p>Správná výška sedla pomáhá kloubům. Při dolní poloze pedálu má být koleno mírně pokrčené, ne úplně natažené. Stačí povolit rychloupínák nebo šroub sedlovky a posunout sedlo o centimetr nahoru či dolů.</p>'
          '<h2>Převody: jedna rychlost, tři, nebo více</h2>'
          '<p>Jednorychlostní kolo je lehké, jednoduché a skoro nepotřebuje údržbu. Hodí se tam, kde je terén rovný. Tříprevodové zadní náboje, běžné u městských kol, ukryjí převody uvnitř náboje, takže se nezanášejí blátem a dají se přeřadit i ve stoje. Trekingová a krosová kola mají vnější přehazovačku a víc kol na kazetě, což pomáhá v kopcích, ale vyžaduje občasné seřízení lanka.</p>'
          '<p>Při výběru si představte nejtěžší úsek své trasy. Pokud se v něm vyskytuje delší kopec, vyplatí se víc převodů nebo elektropohon. Rovinaté okolí s krátkými vzdálenostmi si vystačí s jednoduchým řešením.</p>'
          '<h2>Brzdy, sedlo a řídítka</h2>'
          '<p>Torpédová nožní brzda funguje bez lanka a je vidět u jednorychlostních městských kol. Je odolná, ale v dlouhém kopci se zahřívá. Ráfkové brzdy V-brake vyžadují čistý ráfek, hydraulické kotoučové brzdy mají nejsilnější záběr za mokra, jsou ale dražší na opravu. Pro nákup po městě stačí cokoli, co je správně seřízené.</p>'
          '<p>Sedlo musí odpovídat šířce sedacích kostí a poloze těla. Ve vzpřímené poloze se širší a měkčí sedlo osvědčí, při sportovnější jízdě je lepší užší a tužší. Řídítka s vyšším zdvihem šetří záda a zápěstí, naopak úzká rovná řídítka zlepší ovladatelnost při rychlejší jízdě.</p>'
          '<h2>Výbava, která dává smysl</h2>'
          '<ul><li><strong>Blatníky a kryt řetězu:</strong> chrání oblečení před špínou, dobře je doplnit samostatné <a href="/cyklo-blatniky/">blatníky</a>, pokud je kolo nemá.</li>'
          '<li><strong>Nosič a košík:</strong> pro nákup a běžný náklad se hodí zadní nosič nebo <a href="/cyklo-tasky-a-nosice/">brašny, nosiče a košíky</a>.</li>'
          '<li><strong>Světla:</strong> přední a zadní osvětlení je při jízdě za šera nezbytné, vybírejte z <a href="/cyklo-svetla/">světel na kolo</a>.</li>'
          '<li><strong>Zámek:</strong> kvalitní <a href="/cyklo-zamky/">zámek na kolo</a> je rozumná investice, hlavně pokud kolo stojí venku.</li>'
          '<li><strong>Helma:</strong> pro každodenní jízdu zvolte <a href="/mestske-cyklohelmy/">městskou helmu</a> nebo obecnější <a href="/cyklisticke-helmy/">cyklistické helmy</a>.</li>'
          '<li><strong>Zvonek a zrcátko:</strong> drobnosti z kategorie <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a> zvyšují bezpečnost v provozu.</li></ul>'
          '<h2>Materiál rámu a hmotnost</h2>'
          '<p>Ocelový rám je odolný, snadno se opravuje a dobře tlumí nerovnosti, váží ale víc. Hliníkový rám je lehčí, nekoroduje a lépe se hodí do kopců a pro ty, kdo kolo nosí do schodů. U dámských kol s košíkem a třemi převody se oba materiály běžně potkávají. Podívejte se také, zda je rám lakovaný proti korozi na místech, kde se hromadí voda, tedy kolem hlavy řízení a pod sedlem.</p>'
          '<h2>Péče a údržba, aby kolo vydrželo</h2>'
          '<ul><li><strong>Tlak v pneumatikách:</strong> kontrolujte ho pravidelně, nedofouknuté pláště zvyšují odpor a snáz se probodnou. K tomu pomůže <a href="/cyklo-pumpy-a-naradi/">pumpa a nářadí</a>.</li>'
          '<li><strong>Řetěz:</strong> stačí ho občas otřít a promazat, ne zasypat olejem. Pomůžou <a href="/cyklo-udrzba/">mazadla a čističe</a>.</li>'
          '<li><strong>Brzdy a lanka:</strong> pokud brzdy začnou drhnout nebo se páky mačkají až k řídítkům, jde o seřízení, které zvládne servis během chvíle.</li>'
          '<li><strong>Uložení:</strong> v zimě kolo uložte do sucha, nejlépe pod střechu, aby neměla rez šanci.</li></ul>'
          '<h2>Poloha na kole a pohodlí na delší trase</h2>'
          '<p>Vzpřímená poloha, typická pro městské a cruiserové modely, odlehčuje zápěstí a krční páteř, ale zvyšuje odpor vzduchu a zatěžuje sedací kosti. Na trase delší než půl hodiny se proto vyplatí sedlo odpovídající šířce kostí a řídítka, která nejsou ani příliš vysoko, ani příliš daleko. Trekingové a krosové modely mají předklon mírnější než silniční kola a umožňují střídat polohu rukou, což pomáhá proti pálení v dlaních. Rukavice s gelovou vložkou z kategorie <a href="/cyklisticke-rukavice/">cyklistické rukavice</a> tlumí vibrace, které řídítky putují do zápěstí.</p>'
          '<p>Pokud se zvedá kolenní bolest, zkontrolujte nejprve výšku sedla a vzdálenost sedla od řídítek. Příliš nízké sedlo zatěžuje přední stranu kolena, příliš vysoké nutí kyčel kolébat se ze strany na stranu. Posun sedla dopředu nebo dozadu po kolejničkách mění úhel nohy a zpravidla stačí několik milimetrů.</p>'
          '<h2>Oblečení a doplňky na každodenní jízdu</h2>'
          '<p>V městském provozu nemusíte nosit speciální dres, ale rozumné je vyhnout se volným nohavicím, které se zachytí do řetězu. Pomůže sponka na kalhoty nebo kryt řetězu, který jsou u dámských kol běžné. Za deště se osvědčí pláštěnka s větráním a blatníky, v zimě tenké rukavice a čepice pod helmu. Kategorie <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> nabízí příjemnější materiály pro delší výlety, kde bavlněné tričko rychle nasákne potem.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<p>Nejčastější chybou je velikost vybraná podle obrázku, ne podle postavy. Druhou je hledání nejlevnějšího modelu bez zvážení, kam s ním pojedete. Kolo určené na krátké cesty po rovině nebude příjemné na trase s kopcem. Třetí chybou je koupit kolo bez blatníků pro každodenní používání a zjistit až při první dešťové jízdě, že oblečení nese stopu po celé zadní straně. Čtvrtá je nezkusit sedlo a řídítka, i když je lze snadno vyměnit.</p>'
          '<h2>Pro koho je dámské kolo vhodné</h2>'
          '<p>Hodí se pro každodenní jízdu na práci, ke škole nebo na nákup, ale také jako rodinné kolo, na které nasedá víc lidí různé postavy. Nízký průlez ocení lidé s omezenou pohyblivostí kyčlí a kolen, i těhotné ženy nebo rodiče s dětskou sedačkou. Dětské kolo hledejte v kategorii <a href="/detska-kola/">dětská kola</a>, pro sportovní jízdu <a href="/horska-kola/">horská kola</a>, a pokud plánujete skládání do auta nebo do vlaku, <a href="/skladaci-kola/">skládací kola</a>.</p>'
          '<h2>Jak nakupovat u srovnávače</h2>'
          '<p>Sporteka ukazuje nabídky různých obchodů vedle sebe. U každého modelu zkontrolujte velikost rámu a kol, počet převodů, barvu a to, zda je kolo dodáváno smontované, nebo v krabici k dokončení. Obchody se liší doručením a možností osobního odběru. Pokud kolo nezkusíte před koupí, vyberte prodejce s jasnými podmínkami vrácení a nechte si kolo před první jízdou zkontrolovat v servisu.</p>',
    faq=[('Jaký je rozdíl mezi dámským a pánským kolem?', 'Hlavně v rámu. Dámský má nízký nebo otevřený průlez pro snadné nasedání, pánský má rovnou horní trubku, která rám zpevňuje. U sportovních kol se rozdíl stírá a mnoho žen jezdí na unisex rámech.'),
         ('Jaká velikost rámu je pro mě správná?', 'Vyjděte z výšky postavy a vnitřní délky nohy a porovnejte je s tabulkou výrobce u modelu. Ve stoji nad rámem má zbýt volné místo a při jízdě musíte mít pohodlně pokrčené koleno v nejnižší poloze pedálu.'),
         ('Jsou lepší kola 26", nebo 28"?', 'Kola 28" se lépe valí a překonávají nerovnosti, takže jsou nejčastější u městských a trekingových kol. Menší 26" se hodí pro nižší postavu a hravější jízdu. Rozhodněte podle výšky a typu tras.'),
         ('Kolik převodů potřebuji do města?', 'Na rovině stačí jedna rychlost nebo tři převody v náboji. Pokud trasa vede do kopce nebo jezdíte i mimo město, hodí se víc převodů s přehazovačkou. Ještě snazší jízdu nabídne elektrokolo.'),
         ('Hodí se dámské kolo i na delší výlety?', 'Trekingové a krosové dámské modely na to jsou stavěné, mají víc převodů a pevnější brzdy. Městské kolo s jednou rychlostí se naopak hodí spíš na krátké trasy po rovině.'),
         ('Je ocelový rám lepší než hliníkový?', 'Ocel je odolná a dobře tlumí nerovnosti, ale je těžší a při poškození laku rezne. Hliník je lehčí a nekoroduje. Pro městské používání jsou oba materiály v pořádku, rozdíl se projeví při nošení kola do schodů.'),
         ('Jaké příslušenství si dokoupit jako první?', 'Světla, zámek a helmu, tedy věci, které řeší bezpečnost a krádež. Dále blatníky a nosič, pokud je kolo nemá. Zvonek je podle pravidel provozu na kole také potřeba.'),
         ('Jak často kolo servisovat?', 'Stačí jednou za rok kontrola brzd, lanek, ložisek a kol, při větším počtu kilometrů i častěji. Mezi servisy sledujte tlak v plášti, čistotu a promazání řetězu a stav brzdových destiček.'),
         ('Dá se na dámské kolo namontovat dětská sedačka?', 'U většiny městských a trekingových modelů ano, nízký rám to naopak usnadňuje. Před koupí ale zkontrolujte, zda výrobce sedačku povoluje a jaký typ upevnění rám umožňuje. Nabídku najdete v kategorii dětské sedačky a vozíky za kolo.'),
         ('Co dělat, když si nejsem jistá velikostí?', 'Vyberte raději menší rám a upravte výšku sedla a řídítek, než abyste jezdila na příliš velkém kole. Pokud to jde, vyzkoušejte kolo v obchodě, případně si ověřte možnost vrácení zboží.')])

# ------------------------------------------------------------------ strechni-stany
NEW['strechni-stany'] = dict(long=True,
    title='Střešní stany, autostany a předstany: výběr',
    desc='Střešní stany, autostany a předstany k autu. Jak vybrat typ, nosnost střechy, velikost a příslušenství a porovnat nabídky v českých obchodech.',
    intro='<p>Stan, který se rozloží na střeše auta, ušetří čas, sníží vlhkost od země a umožní spát na místech, kde by klasický stan nešel postavit. Kategorie ale pojímá šířeji, než je název: kromě střešních stanů, které čeští prodejci často nazývají autostany, zde najdete také předstany k dodávkám a množství dílů, jako jsou prostěradla, matrace, obaly nebo žebříky. Sporteka porovnává nabídku českých obchodů a pomáhá vybrat správné řešení pro vaše auto.</p>'
          '<p>V nabídce jsou značky ' + B(('quechua', 'Quechua'), ('viking', 'Viking'), ('sovnaran', 'Sovnaran'), ('king-camp', 'King Camp'), ('arb', 'ARB'), ('cattara', 'Cattara')) +
          '. Další stany najdete v kategoriích <a href="/stany/">stany</a>, <a href="/turisticke-stany/">turistické stany</a>, <a href="/rodinne-stany/">rodinné stany</a> a <a href="/pristresky-a-party-stany/">přístřešky a party stany</a>.</p>',
    guide='<h2>Čím se liší střešní stan, autostan a předstan</h2>'
          '<p>Slova se v praxi míchají, a proto se vyplatí rozlišovat, co se kupuje. Střešní stan se montuje na střešní nosiče a rozkládá se nad autem, spí se v něm jako v pevné posteli. V českých obchodech se pro střešní stan běžně používá i označení autostan, proto na něj narazíte v nabídce pod oběma názvy. Střešní stany se dělí na skládací, skořepinové a nafukovací. Předstan je malý samostatný přístavek ke karavanu nebo dodávce, který zajišťuje zázemí před vchodem.</p>'
          + T(['Typ', 'Princip', 'Výhoda', 'Co je třeba vědět'], [
              ['Střešní stan', 'montáž na střešní nosič, rozkládá se nahoru nebo do strany', 'rychlé postavení, spaní nad zemí', 'zvyšuje spotřebu a výšku auta, potřebuje nosiče s dostatečnou nosností'],
              ['Skládací střešní stan (autostan)', 'plachta v kufru nebo obalu, po rozložení vznikne větší lůžko', 'prostorný, cenově dostupnější', 'rozložení a sbalení trvá déle než u skořepiny'],
              ['Nafukovací střešní stan', 'nosnou konstrukci tvoří vzduchové trubky', 'postavení bez skládání tyčí', 'nutná pumpa a opravná sada'],
              ['Předstan, přístřešek', 'doplněk k dodávce nebo karavanu', 'zázemí před vchodem', 'nesedí na každé auto'],
              ['Díly a doplňky', 'prostěradla, obaly, žebříky, montážní sady', 'oprava, rozšíření, výměna', 'díly musí odpovídat modelu stanu']]) +
          '<p>V nabídce najdete střešní stany různých značek, nafukovací modely a množství dílů k nim, například žebříky, matrace a prostěradla. Pokud hledáte konkrétní díl, zkontrolujte, k jakému modelu se hodí, protože dílce sedí vždy jen na určitou řadu.</p>'
          '<h2>Co musí unést střecha vašeho auta</h2>'
          '<p>Při výběru střešního stanu je klíčový údaj ve voze: maximální zatížení střechy, které uvádí výrobce auta v návodu. Dynamická nosnost, tedy limit při jízdě, bývá výrazně nižší než statická při stání, kdy se ve stanu spí. Stan, nosiče a případně žebřík se do dynamického limitu započítávají všechny. Nosiče musí vyhovovat i tomu, že stan váží desítky kilogramů a na střeše pak působí při brzdění a zatáčení.</p>'
          '<ul><li><strong>Zkontrolujte nosnost střechy</strong> a nosičů a porovnejte ji s hmotností stanu podle výrobce.</li>'
          '<li><strong>Rozložení váhy:</strong> těžiště stanu držte nad nosnou částí, ne na kraji střechy.</li>'
          '<li><strong>Dotahování:</strong> před vyjetím a po prvních kilometrech zkontrolujte šrouby a upevnění.</li>'
          '<li><strong>Výška:</strong> pamatujte na podjezdy, parkovací domy a větve, protože auto je se stanem výrazně vyšší.</li></ul>'
          '<p>Na střešní nosiče se montuje i další příslušenství, například <a href="/cyklo-nosice-na-auto/">nosiče kol na auto</a> nebo box. Jejich hmotnost se k hmotnosti stanu připočítává a nesmí přesáhnout nosnost střechy.</p>'
          '<h2>Tvrdá skořepina, nebo skládací stan</h2>'
          '<p>Střešní stany se dělí na dva základní typy. Skládací mají plachtu uloženou v pevném kufru nebo v měkkém obalu a po rozložení vytvoří stan podobný velkému loži. Jsou prostorné a levnější na výrobu. Skořepinové stany se otevřou jako schránka a stanový prostor je u nich nižší, ale postavení i sbalení je velmi rychlé, což ocení ti, kdo spí na různých místech jednu noc. Skořepina bývá aerodynamičtější, takže méně zvyšuje spotřebu paliva.</p>'
          '<p>Jak se stan rozkládá, to ovlivní i provoz. Plachtu je potřeba sbalit suchou, protože vlhkost způsobuje plísně. Pokud jste ve vlhku museli stan sbalit mokrý, doma ho znovu rozložte a vysušte.</p>'
          '<h2>Autostan: na co se při výběru dívat</h2>'
          '<p>Autostany jsou určeny lidem, kteří chtějí spát nad zemí a mít lůžko rozložené během několika minut. Důležité je, jak velké lůžko stan nabízí, kolik váží a jak se vejde na střechu. Střešní stan nelze používat bez nosičů, takže nejdřív zkontrolujte, zda je auto unese. Na zemi pak potřebujete rovné místo pro žebřík.</p>'
          '<ul><li><strong>Konstrukce:</strong> skládací rám z hliníku, pevná skořepina nebo nafukovací trubky, které se staví rychleji.</li>'
          '<li><strong>Odolnost vody:</strong> vodní sloupec se uvádí v milimetrech, rozhoduje i kvalita švů a dna.</li>'
          '<li><strong>Větrání:</strong> okna a větrací otvory brání kondenzaci, která je hlavní příčinou mokrého stanu.</li>'
          '<li><strong>Zatemnění:</strong> zatemňovací potah omezuje světlo, takže se ráno spí déle. Údaj výrobce o ohřevu vnitřku na slunci si ověřte.</li></ul>'
          '<h2>Nafukovací konstrukce</h2>'
          '<p>Nafukovací autostan nepotřebuje skládací tyče. Po rozbalení se do trubek napumpuje vzduch a stan stojí. Je rychlý na postavení a není problém ho postavit samotný. Nevýhodou je riziko úniku vzduchu z trubky nebo ventilu, proto mějte po ruce pumpu a opravnou záplatu. Při vyšších teplotách se vzduch roztahuje, takže tlak je dobré zkontrolovat, aby trubky nepraskly.</p>'
          '<h2>Příslušenství a díly</h2>'
          '<p>Velká část kategorie jsou doplňky: prostěradlo na podlahu, obal na matraci, přístřešek nebo obal na celý stan. Při koupi dílů se vždy řiďte označením modelu, například stejný název řady a počet osob. Spacích doplňků se týká i naše nabídka <a href="/karimatky-a-matrace/">karimatek a matrací</a> a <a href="/perove-spacaky/">péřových spacáků</a> a <a href="/dekove-spacaky/">dekových spacáků</a>, zázemí pak <a href="/kempingovy-nabytek/">kempingový nábytek</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li><strong>Vysušení:</strong> stan nikdy neskladujte vlhký, plesnivá plachta se nedá spolehlivě vyčistit.</li>'
          '<li><strong>Čištění:</strong> používejte vlažnou vodu a jemný kartáč, agresivní chemie poškozuje impregnaci a švy.</li>'
          '<li><strong>Zipy:</strong> zbavte je písku a občas ošetřete vhodným mazivem.</li>'
          '<li><strong>Uložení:</strong> v suchu, bez tlaku na tyče, mimo mráz a přímé slunce.</li>'
          '<li><strong>Kontrola před sezónou:</strong> rozložte stan na zahradě a ověřte švy a zipy dřív, než pojedete.</li></ul>'
          '<h2>Pro koho se střešní stan hodí</h2>'
          '<p>Nejvíc ocení střešní stan cestovatelé, kteří spí každou noc jinde, a lidé, kteří potřebují postavit stan rychle za špatného počasí nebo na nerovném terénu. Pro delší pobyt na jednom místě je výhodnější <a href="/rodinne-stany/">rodinný stan</a>. Pokud chcete spíše lehkou turistiku a pěší přesuny, hodí se spíš <a href="/turisticke-stany/">turistický stan</a>, případně <a href="/expedicni-stany/">expediční stan</a> do náročných podmínek.</p>'
          '<h2>Montáž, rozložení a spaní ve stanu</h2>'
          '<p>Montáž střešního stanu se obvykle dělá ve dvou lidech, protože stan váží tolik, že ho jeden člověk těžko zvedne na střechu. Stan se přichytí k nosičům svorkami nebo šrouby a po upevnění se zkontroluje, zda nic nehýbe. Při rozkládání se vychází z toho, že auto stojí na rovném místě, protože naklonění o pár stupňů se ve spánku znatelně projeví. Žebřík se nastaví tak, aby stál stabilně na zemi, a při výstupu se drží obě ruce na příčkách.</p>'
          '<p>Uvnitř je matrace pevně zabudovaná, takže ložní prádlo je běžný spacák nebo peřina. Přidanou izolaci proti chladu zajistí podložka pod matraci nebo deka, protože vzduch pod stanem je v noci studený. Ráno se zvlhlá plachta při balení otře, ideálně na slunci. Při bouři nebo silném větru je bezpečnější stan sbalit, protože střešní plachta funguje jako plachta lodi a namáhá nosiče.</p>'
          '<h2>Auto a zázemí kolem stanu</h2>'
          '<p>Kdo spí na střeše, potřebuje ještě místo na vaření, sezení a skladování věcí. K tomu slouží <a href="/kempingovy-nabytek/">kempingový nábytek</a>, skládací stolek a židle, a <a href="/kempingove-nadobi/">kempingové nádobí</a> s vařičem. Přístřešek z kategorie <a href="/pristresky-a-party-stany/">přístřešky a party stany</a> poskytne stín nebo ochranu před deštěm bez nutnosti vylézat. Obecně platí, že čím víc věcí vozíte, tím důležitější je dodržet limit zatížení střechy a vozit těžké zavazadla uvnitř auta, ne nad ním.</p>'
          '<h2>Časté chyby</h2>'
          '<p>Častá chyba je přehlédnutí limitu střechy a spoléhání na to, že nosiče jsou silnější než střecha. Další je nákup dílů bez kontroly modelu, protože prostěradlo a obal se u podobně pojmenovaných stanů liší velikostí. Poměrně časté je i podcenění větrání, které vede k mokrým stěnám i při suchém počasí. A nakonec: stan není určen k jízdě s rozloženou plachtou nebo v silném větru.</p>'
          '<h2>Jak nakupovat na srovnávači</h2>'
          '<p>Sporteka seřadí nabídky několika obchodů vedle sebe. U každého produktu zkontrolujte typ, jestli jde o samotný stan, nebo jen doplněk, a rozměry po složení. Zpráva o dodání a vrácení zboží je důležitá hlavně u rozměrného zboží, které se po otevření obtížně posílá zpět.</p>',
    faq=[('Je střešní stan vhodný pro každé auto?', 'Ne. Záleží na nosnosti střechy a nosičů uvedené výrobcem auta, na rozměrech a hmotnosti stanu. Dynamický limit při jízdě bývá nižší než statický při spaní, proto je nutné ověřit oba údaje v návodu auta.'),
         ('Jaký je rozdíl mezi střešním stanem a autostanem?', 'Žádný zásadní, v českých obchodech jde o dva názvy téhož typu: stan se montuje na střešní nosiče a spí se v něm nad zemí. Odlišit je třeba spíš provedení, tedy skládací, skořepinový nebo nafukovací stan, a dále předstan, který se používá u dodávek a karavanů.'),
         ('Zvyšuje střešní stan spotřebu?', 'Ano, zvyšuje odpor vzduchu, a tím spotřebu paliva. Aerodynamičtější skořepinové modely ji zvyšují méně než skládací, přesnou hodnotu ale uvádí jen měření pro konkrétní kombinaci auta a stanu.'),
         ('Jak sbalit stan, když je mokrý?', 'Při nutnosti sbalit mokrý stan ho po příjezdu domů znovu rozložte a vysušte. Vlhká plachta bez větrání plesniví a ztrácí impregnaci.'),
         ('Co znamená nafukovací autostan?', 'Konstrukci tvoří vzduchové trubky místo tyčí. Stan se postaví napumpováním, což je rychlejší a jednodušší než skládání tyčí, vyžaduje ale pumpu a opravnou sadu.'),
         ('Mohu koupit pouze prostěradlo nebo obal na matraci?', 'Ano, v kategorii jsou i samostatné díly. Vybírejte podle označení modelu stanu a počtu osob, protože rozměry se mezi řadami liší.'),
         ('Hodí se střešní stan na zimu?', 'Záleží na modelu. Většina je určena pro tří až čtyři sezóny, v chladu ale vyžaduje dobrý spacák a izolaci matrace od podlahy. Informaci o sezónnosti hledejte u konkrétního stanu.'),
         ('Jak často kontrolovat upevnění střešního stanu?', 'Před každou jízdou a znovu po prvních kilometrech, kdy se spoje mohou usadit. Šrouby a svorky nosičů dotahujte podle návodu výrobce.'),
         ('Kde sehnat další vybavení na kempování?', 'Spacáky, matrace, nábytek a nádobí najdete v kategoriích kempingového vybavení. Pro menší zázemí poslouží přístřešky a party stany.'),
         ('Na co si dát pozor při převozu stanu v autě?', 'Střešní stan se vozí na střešních nosičích, proto před jízdou zkontrolujte dotažení šroubů a svorek a po prvních kilometrech je dotáhněte znovu. Stan musí být zavřený a zajištěný zipy či přezkami, aby ho za jízdy nepoškodil vítr. Před uložením ho vždy vysušte, aby se nešířila plíseň. Rozměrné díly, například žebřík, obaly nebo matraci, vozte uvnitř auta a upevněte popruhem, aby se při brzdění neposouvaly a nepoškodily lak či interiér vozu.'),
         ('Mohu v autě spát bez stanu?', 'Obecně ano, pokud to dovolují místní pravidla a bezpečnost parkoviště. Pohodlí závisí na matraci a větrání. Stan přidává prostor a oddělení od auta.')])

# ------------------------------------------------------------------ krasobruslarske-brusle
NEW['krasobruslarske-brusle'] = dict(long=True,
    title='Krasobruslařské brusle: velikost, bota a nůž',
    desc='Krasobruslařské brusle pro dívky a ženy. Jak vybrat velikost, tuhost boty a nůž, jak o brusle pečovat a porovnat nabídky českých obchodů.',
    intro='<p>Krasobruslařská bruslařská bota je jiná než hokejová: je vyšší, pevnější kolem kotníku a nůž má na špičce zoubky, které slouží při skocích a piruetách. Správné brusle rozhodují o tom, zda se dítě na ledě bude bavit, nebo se bude trápit bolavými kotníky. Sporteka porovnává nabídky českých obchodů u dívčích i dámských krasobruslí, od jednoduchých rekreačních párů po modely se samostatným nožem a širší nebo užší botou.</p>'
          '<p>V nabídce jsou značky ' + B(('winnwell', 'Winnwell'), ('attabo', 'Attabo'), ('jackson', 'Jackson'), ('kubisport', 'Kubisport'), ('smj', 'SMJ'), ('roces', 'Roces')) +
          '. K běžnému bruslení se hodí také <a href="/rekreacni-brusle/">rekreační brusle</a>, pro hokej <a href="/hokejove-brusle/">hokejové brusle</a> a obecně <a href="/brusle/">zimní brusle</a>.</p>',
    guide='<h2>Jak je krasobruslařská bota postavená</h2>'
          '<p>Krasobrusle jsou přesně nastavené na přenos váhy z nohy na nůž. Bota sahá vysoko nad kotník, aby držela nohu při doskocích. Podpatek je zvýšený, špička je užší než u hokejky a nůž je delší než bota, takže zpředu i zezadu přesahuje. Kolem kotníku bývá použita vrstva tvrdé hmoty, kůže nebo její náhrady. Čím tužší bota, tím větší podpora, ale také tím menší pohodlí pro začátečníka.</p>'
          + T(['Úroveň', 'Typ boty', 'Nůž', 'Pro koho'], [
              ['Rekreační', 'měkčí, často z umělých materiálů', 'pevně přinýtovaný', 'volné bruslení, začátečnice a děti'],
              ['Kluby a kurzy', 'středně tuhá, kožená nebo kombinovaná', 'pevně namontovaný, kvalitnější ocel', 'pravidelný trénink, základní skoky'],
              ['Pokročilé', 'tužší, tepelně tvarovatelná', 'samostatný nůž podle disciplíny', 'jezdkyně s doskoky a piruetami'],
              ['Dívčí a dětské', 'menší velikosti, obvykle jednodušší', 'pevný', 'první sezóny a rostoucí děti']]) +
          '<p>V kategorii je mnoho dětských modelů Winnwell Figure, které jsou označené velikostmi Y pro nejmenší děti a dále číselnými velikostmi. Jde o jednoduché pevné brusle určené pro začátečníky. Značky Jackson a Attabo nabízejí i dámské modely a širší nebo užší varianty boty.</p>'
          '<h2>Velikost: nejdůležitější rozhodnutí</h2>'
          '<p>Krasobrusle se kupují přesně nebo jen o půl čísla větší, ne s velkou rezervou jako dětské boty. Při příliš volné botě se noha uvnitř posouvá a vznikají puchýře, při příliš malé se prsty ohýbají a bolí. U rostoucích dětí je lákavé koupit o dvě čísla víc, výsledkem je ale špatná kontrola nad nožem a rychlé ztráty zájmu. Rozumné je nejvýš půl čísla navíc a tenká ponožka, případně bazarové nebo půjčené brusle na první sezónu.</p>'
          '<ul><li><strong>Měření:</strong> změřte délku chodidla na rovném papíře a porovnejte s tabulkou výrobce, protože označení se liší (EU, UK, US).</li>'
          '<li><strong>Zkouška:</strong> v zavázané botě musí pata sedět pevně a prsty se mají lehce dotýkat špičky.</li>'
          '<li><strong>Šířka:</strong> některé modely mají širší variantu, to jsou pak označeny například široké (wide).</li>'
          '<li><strong>Ponožky:</strong> tenké, bez švů, ne silné zimní, ty boty ucpávají a tlačí.</li></ul>'
          '<h2>Tuhost boty a podpora kotníku</h2>'
          '<p>Základní pravidlo zní: boty tužší než technika jezdce dělají víc škody než užitku. Kotník musí být podpořen, ale ne ztuhlý. Pro děti do prvních skoků stačí měkčí bota, která se dá ohnout v hlezně, jakmile se začnou dělat dvojité skoky, přichází na řadu tužší boty. Jak zjistit, zda je bota příliš měkká: kotník se při pohybu dovnitř zřetelně sklápí. Pokud je naopak příliš tvrdá, noha nemůže v kolenou pracovat a bruslařka se nemůže správně pokrčit.</p>'
          '<h2>Nůž: co je důležité</h2>'
          '<p>Na noži záleží stejně jako na botě. Krasobruslařský nůž má zoubky pouze na špičce a zabodávají se do ledu při skocích. Spodní hrana je mírně vypouklá a má dvě hrany s drážkou mezi nimi, což umožňuje zatáčky na hraně. Nůž se u kvalitnějších modelů prodává zvlášť a jeho velikost se vybírá podle délky chodidla a úrovně jezdce.</p>'
          '<ul><li><strong>Pevný nůž:</strong> nůž je pevně přinýtovaný a nedá se vyměnit, bruslařka se na něj naučí základy.</li>'
          '<li><strong>Výměnný nůž:</strong> při opotřebení se vymění samotný nůž, bota zůstane.</li>'
          '<li><strong>Brusná hrana:</strong> musí být ostrá a rovná, jinak brusle klouže nebo se zasekává.</li>'
          '<li><strong>Chránič nože:</strong> tvrdé kryty se používají jen při chůzi mimo led. Na led se chrániče sundávají.</li></ul>'
          '<h2>Broušení a péče o nůž</h2>'
          '<p>Krasobruslařský nůž brousí odborník. Nejde o hokejové broušení, které je jednodušší, krasobruslařský výbrus má správně vedenou drážku a tvar. Brusle se brousí podle četnosti: při bruslení několikrát týdně i několikrát za sezónu, rekreační jezdci méně. Pokud brusle klouže nebo naopak neprokluzuje, je čas na broušení. Dobrý výbrus se pozná podle toho, že hrana drží, když se bruslařka opírá o vnitřní nebo vnější hranu.</p>'
          '<h2>Po bruslení: sušení a skladování</h2>'
          '<ul><li><strong>Utřít nůž:</strong> po sundání bot utřete nůž do sucha, protože vlhkost na kovu způsobí rez.</li>'
          '<li><strong>Chránič na přepravu:</strong> v tašce používejte měkké chrániče, které absorbují zbytky vody.</li>'
          '<li><strong>Vysušit botu:</strong> vyndejte vložku a nechte vyschnout při pokojové teplotě, mimo topení.</li>'
          '<li><strong>Tvrdé kryty:</strong> používejte jen při chůzi, ne při uložení, kde zadržují vlhkost.</li>'
          '<li><strong>Tkaničky:</strong> vyměňte, když se začnou trhat, protože na zavázání boty závisí podpora kotníku.</li></ul>'
          '<h2>Jak správně zavázat brusle</h2>'
          '<p>Krasobrusle se zavazují různě podle úseku. Špička a nárt mají sevření pevné, ale ne ucpávající, kotník má být vázán pevněji, aby držel patu na místě. Háčky nahoře se zavazují volněji, aby mohlo koleno pracovat. Po zavázání proveďte několik dřepů a ověřte, že pata nezvedá a prsty se neotírají. Pokud tlačí nárt, uvolněte jej a zkuste jiný způsob utažení.</p>'
          '<h2>Co dalšího se hodí</h2>'
          '<p>Při prvních bruslích je dobré mít rukavice, teplé oblečení z pružných materiálů a případně chránič na zadek a zápěstí. V obchodech najdete také <a href="/inline-brusle/">inline brusle</a> pro trénink mimo led, <a href="/kolobezky-a-brusle/">koloběžky a brusle</a> pro celoroční pohyb a <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a> pro pohodlí na ledě. Pro bruslení na ledu jsou dobré i <a href="/leginy/">legíny</a> z pružného materiálu.</p>'
          '<h2>První týdny na ledě a nejčastější potíže</h2>'
          '<p>Nové brusle je dobré rozchodit doma několikaminutovým chozením v botách s chrániči nože, aby se materiál přizpůsobil noze. Na ledě se v prvních hodinách objevuje únava lýtek a chodidel, protože svaly pracují jinak než při chůzi. Pokud bota tlačí na jednom místě, zpravidla pomůže změna zavázání, tenčí ponožka nebo odborné vytvarování boty v obchodě. Pokud bolest trvá, vezměte brusle zpět a porovnejte velikost, protože chyba bývá právě tam.</p>'
          '<p>Další častá potíž je, že kotník padá dovnitř. Neznamená to nutně slabé brusle, často jde o slabý kotník dítěte, který se posílí cvičením a časem. Dobrý trenér pozná, zda stačí cvičení, nebo je potřeba tužší bota. Správně sedící brusle jsou z velké části otázkou kontroly a rady, ne jen nákupu.</p>'
          '<h2>Led, hala a oblečení pro bruslení</h2>'
          '<p>Na zimním stadionu bývá chladno, takže se vyplatí vrstvit: elastické legíny nebo punčochové kalhoty, tenká mikina a rukavice, které chrání ruce při pádu. Volné části oděvu, šály a dlouhé vlasy je dobré sepnout, aby nepřekážely. Mnoho jezdkyň nosí krasobruslařské sukně a šaty, ty ale nejsou nutné pro začátky. Pro pohodlný pohyb ve volném bruslení jsou důležitější pružné materiály, které se nezadrhávají o nůž.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<p>Častá chyba je koupit hokejové brusle místo krasobruslí a naopak. Hokejová brusle se liší konstrukcí, nůž nemá zoubky a má jiný profil, než jaký potřebuje krasobruslení. Druhá je volba příliš velké velikosti, aby dítě brusle nosilo víc sezón. Třetí je zbytečně drahá a tvrdá bota pro začátečnici, která pak nemůže ohýbat kotník. A čtvrtá je zanedbání broušení, kvůli kterému dítě padá a ztrácí chuť na led.</p>'
          '<h2>Jak vybrat podle věku a úrovně</h2>'
          '<p>Nejmenší děti potřebují lehkou botu s dobrou oporou kotníku a jednoduchým zavazováním. Teenageři na kroužku se pohybují mezi měkčí a středně tuhou botou, podle toho, jak rychle se učí skoky. Dospělé začátečnice mohou volit širší pohodlnější modely, pokud je bruslení rekreační. Pro soutěžní jezdkyně je potřeba konzultovat trenéra a odborný obchod, protože výběr boty a nože ovlivňuje techniku.</p>'
          '<h2>Jak nakupovat na srovnávači</h2>'
          '<p>Sporteka ukazuje nabídky různých obchodů vedle sebe, takže snadno uvidíte, kde je vaše velikost skladem. Ověřte označení velikosti, tedy EU, UK nebo US, a zda jde o dětský nebo dámský střih. Zkontrolujte také, zda brusle jsou nabroušené při dodání, protože kvalitní broušení je nutné před prvním použitím. Před koupí nejistých rozměrů si raději ověřte podmínky vrácení.</p>',
    faq=[('Čím se liší krasobrusle od hokejových bruslí?', 'Krasobrusle mají vyšší a pevnější botu, delší nůž se zoubky na špičce a zvýšenou patu. Hokejové brusle mají kratší nůž bez zoubků a jsou stavěné na rychlé zatáčky a zrychlení.'),
         ('Jakou velikost zvolit pro dítě?', 'Přesnou nebo maximálně o půl až jedno číslo větší, s tenkou ponožkou. Velká rezerva způsobí, že se noha v botě posouvá a nůž nelze dobře ovládat.'),
         ('Jak poznám, že je bota příliš měkká?', 'Kotník se při zatížení sklápí dovnitř nebo ven a bota nedrží tvar. U začátečníků se to vyskytuje u nejlevnějších modelů, ale také u rostoucích dětí, které technikou přerostly svoje brusle.'),
         ('Kdy brousit nůž?', 'Když brusle klouže bez záběru, zasekává se nebo nedrží hranu. Při pravidelném tréninku jednou za několik týdnů, při rekreačním bruslení méně často. Brousit by měl odborník, který zná krasobruslařský výbrus.'),
         ('Můžu chodit v bruslích po zemi?', 'Jen s tvrdými chrániči nože, které nůž chrání před poškozením, a nikdy ne po betonu nebo štěrku bez nich. Po ledu pak chrániče sundejte, protože zadržují vodu a způsobují rez.'),
         ('Jak sušit brusle po tréninku?', 'Nůž utřete do sucha, vložte měkký chránič na přepravu a doma vyndejte a vysušte vložku. Boty sušte při pokojové teplotě, ne na topení, které poškozuje kůži a lepidla.'),
         ('Hodí se krasobrusle i pro dospělé?', 'Ano, ženy i muži s nimi mohou bruslit rekreačně nebo trénovat jednoduché prvky. Pro dospělé s širším chodidlem existují široké varianty modelů. Důležité je správné broušení a opora kotníku.'),
         ('Mohu koupit brusle bez nože?', 'U kvalitnějších modelů se bota a nůž prodávají zvlášť. Nůž se musí vybrat podle velikosti a úrovně a správně namontovat. Pro začátečníky je jednodušší model s pevným nožem.'),
         ('Jak často děti vyrůstají z bruslí?', 'Záleží na růstu, často po jedné až dvou sezónách. Dobré brusle lze po zhodnocení prodat nebo předat mladšímu sourozenci, pokud jsou bota i nůž v dobrém stavu.'),
         ('Jak připravit nové brusle před první jízdou?', 'Zkontrolujte, zda jsou nabroušené a nůž je pevně přichycený. Ponožky zvolte tenké a dlouhé, tkaničky zavažte pevněji u kotníku a volněji nahoře. Doma si v nich na koberci projděte několik minut s nasazenými chrániči, aby se bota přizpůsobila noze. První bruslení nepřehánějte, protože nohy a lýtka potřebují čas na přivyknutí. Po každém tréninku brusle vysušte a zkontrolujte tkaničky, háčky i upevnění nože, aby se drobná závada neprojevila až na ledě. Pokud se bota při chůzi pohybuje, zavázání upravte, dokud pata nesedí pevně.'),
         ('Kde sehnat brusle na jiný sport?', 'Pro hokej jsou hokejové brusle, pro rekreaci kategorie rekreační brusle, pro celoroční jízdu inline brusle.')])

# ------------------------------------------------------------------ celoodpruzena-horska-kola
NEW['celoodpruzena-horska-kola'] = dict(long=True,
    title='Celoodpružená horská kola: zdvih, rám, výběr',
    desc='Celoodpružená horská kola (full): XC, trail a all-mountain. Jak vybrat zdvih, velikost rámu, tlumič a komponenty a porovnat nabídky českých obchodů.',
    intro='<p>Celoodpružené horské kolo, zvané také full, má pružinu vpředu na vidlici i vzadu na zadní stavbě. Díky tomu lépe drží stopu na kořenech a kamenech, tlumí údery a umožňuje rychleji projet drsný terén. Za to platí vyšší hmotností, složitější konstrukcí a pravidelným servisem. Sporteka porovnává nabídky českých obchodů a pomáhá zorientovat se v kategoriích od lehkých cross-country strojů po výkonná kola na stezky a bikeparky. Při výběru je potřeba zvážit terén, hmotnost i nároky na údržbu.</p>'
          '<p>V kategorii jsou značky ' + B(('specialized', 'Specialized'), ('rockrider', 'Rockrider'), ('trek', 'Trek'), ('4ever', '4ever'), ('kellys', 'Kellys'), ('scott', 'Scott')) +
          '. Pro srovnání zkuste i <a href="/horska-kola/">horská kola</a> obecně, <a href="/horska-elektrokola/">horská elektrokola</a> nebo <a href="/gravel-kola/">gravel kola</a> pro rychlejší nenáročný terén.</p>',
    guide='<h2>Co dělá celoodpružené kolo jiným</h2>'
          '<p>Na pevném kole, kterému se říká hardtail, tlumí nárazy pouze vidlice, a zbytek přenáší rám a jezdec. U celoodpruženého kola pracuje zadní kolo na kinematice, která při nárazu ustoupí a vrátí se zpět. Kolo tak lépe přilne k povrchu, zadní kolo neodskakuje a jezdec je méně unavený. Při šlapání do kopce se ale část energie může ztrácet pohupováním, což výrobci řeší geometrií, lockouty nebo tlumiči s přepínačem.</p>'
          + T(['Kategorie', 'Zdvih', 'Zaměření', 'Povaha jízdy'], [
              ['Cross-country (XC)', 'zhruba 100–120 mm', 'rychlost, závody, maratony', 'lehké, účinné do kopce'],
              ['Trail', 'zhruba 120–150 mm', 'všestranná jízda stezkami', 'vyvážené do kopce i z kopce'],
              ['All-mountain a enduro', 'zhruba 150–170 mm', 'strmé a technické sjezdy', 'těžší, stabilnější, hodí se pro vlek nebo kopec'],
              ['Downhill, bikepark', 'více než 180 mm', 'sjezd, skoky, dráhy', 'jen z kopce, těžké a odolné']]) +
          '<p>Hodnoty jsou orientační a každý výrobce má vlastní označení. Z nabídky: Specialized Epic je typický cross-country stroj, Trek Top Fuel patří do podobné kategorie, Trek Fuel EX a Rockrider Feel spadají k trailu a all-mountainu. Označení typu pomůže, ale rozhodující je, kam budete jezdit.</p>'
          '<h2>Kolik zdvihu potřebujete</h2>'
          '<p>Větší zdvih neznamená lepší kolo. Delší zdvih je těžší, pomalejší do kopce a méně přesný při rychlé jízdě po hladkém povrchu. Menší zdvih je naopak rychlejší, ale ve strmém kamenitém terénu nemusí vyhovět. Podle místních tras si představte nejčastější terén: lesní cesty a pagorky vyžadují méně, technické stezky a skály více.</p>'
          '<ul><li><strong>Většinou lesní cesty a kopce:</strong> kratší zdvih, nižší hmotnost.</li>'
          '<li><strong>Mix stezek a technických úseků:</strong> střední zdvih, který zvládne obojí.</li>'
          '<li><strong>Prudké sjezdy a skoky:</strong> delší zdvih a odolnější rám.</li></ul>'
          '<h2>Rám: materiál a velikost</h2>'
          '<p>Rám bývá z hliníku nebo karbonu. Hliník je odolnější vůči nárazům, snáze se opravuje a stojí méně. Karbon je lehčí a tužší, ale citlivější na poškození a dražší. Velikost se označuje písmeny S až XL a odpovídá výšce postavy podle tabulky výrobce. Rozhodují délka horní trubky (reach) a rozvor, které ovlivňují stabilitu a ovladatelnost. Delší rám je stabilnější při rychlosti, kratší hravější.</p>'
          '<p>Mezi velikostmi se rozhoduje podle toho, zda dáváte přednost jistotě při sjezdu (větší rám), nebo ovladatelnosti (menší). U celoodpruženého kola je také důležitá výška sedla. Teleskopická sedlovka, kterou lze za jízdy snížit, je u trailových kol výhodou.</p>'
          '<h2>Velikost kol: 29", 27,5" a smíšené</h2>'
          '<p>Velká kola 29" se lépe valí a překonávají překážky, hodí se pro rychlé stezky a vyšší jezdce. Menší 27,5" jsou obratnější a lépe vyhovují nižším postavám a hravému stylu. Někteří výrobci kombinují velké přední a menší zadní kolo, což se označuje jako mullet a dává větší prostor zadnímu kolu při hravé jízdě. Menší velikosti rámu nejsou vždy s 29" koly, proto se na to zeptejte při výběru.</p>'
          '<h2>Odpružení: vidlice a tlumič</h2>'
          '<p>Vidlice a tlumič se nastavují podle váhy jezdce. Správné nastavení se projeví v tom, že odpružení pracuje při nárazech a nepropadá se při šlapání. Základem je tlak vzduchu a pak odskok, který určuje rychlost návratu. Většina tlumičů má i přepínač, který odpružení uzamkne do kopce. Podrobněji se těmto dílům věnují <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>.</p>'
          '<ul><li><strong>Sag:</strong> procento zdvihu, které se prohne pod váhou jezdce při sezení, nastavuje se při koupi nebo v servisu.</li>'
          '<li><strong>Odskok:</strong> příliš rychlý odskok kolo vymrští, příliš pomalý ho nechá zaseknout v nárazech.</li>'
          '<li><strong>Zámek:</strong> pomáhá do kopce a na silnici, před sjezdem se musí odemknout.</li></ul>'
          '<h2>Brzdy, převody a ostatní komponenty</h2>'
          '<p>Hydraulické kotoučové brzdy jsou u celoodpružených kol standardem. U sjezdovějších modelů se používají větší kotouče a čtyřpístkové třmeny pro větší brzdný výkon. Převody jsou nejčastěji jednopřevodníkové s širokou kazetou, což zjednodušuje řazení a snižuje hmotnost. Kvalitu komponentů poznáte podle řady, ale na většinu jízd stačí střední třída. Více o této části kola se dočtete v kategoriích <a href="/cyklo-brzdy/">brzdy</a>, <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklo-pedaly/">pedály</a> a <a href="/cyklo-riditka/">řídítka</a>.</p>'
          '<h2>Povinná výbava a ochrana</h2>'
          '<p>Na horském kole patří k základu helma a rukavice. Pro technické stezky a sjezdy je rozumné zvolit helmu s delším krytím týlu z kategorie <a href="/mtb-a-integralni-helmy/">MTB a integrální helmy</a> a <a href="/cyklo-chranice/">chrániče</a> kolen a loktů. Dále se hodí <a href="/cyklisticke-rukavice/">rukavice</a>, <a href="/cyklisticka-obuv/">cyklistická obuv</a>, <a href="/cyklisticke-ponozky/">ponožky</a> a lahev nebo batoh na pití. Pro základní opravy nechybí pumpa a multiklíč z kategorie <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Údržba, kterou nelze přeskočit</h2>'
          '<p>Celoodpružené kolo má víc ložisek a pohyblivých dílů, a proto vyžaduje častější péči než pevné. Zadní kyvná vidlice se uchycuje na čepech a ložiskách, která při bahně a prachu rychle trpí. Po každé jízdě v terénu kolo opláchněte a promažte řetěz. Čištění a mazání usnadní <a href="/cyklo-udrzba/">mazadla a čističe</a>.</p>'
          '<ul><li><strong>Vidlice a tlumič:</strong> servis podle návodu výrobce, obvykle po určitém počtu hodin jízdy.</li>'
          '<li><strong>Ložiska zadní stavby:</strong> kontrolujte vůli, při vůli nebo skřípání jedete do servisu.</li>'
          '<li><strong>Řetěz a kazeta:</strong> opotřebený řetěz poškozuje zbytek pohonu, takže ho včas vyměňte.</li>'
          '<li><strong>Brzdové destičky:</strong> měnit při opotřebení, nikdy nejezdit až na kov.</li>'
          '<li><strong>Utahovací momenty:</strong> u karbonových dílů dodržujte předepsané hodnoty a momentový klíč.</li></ul>'
          '<h2>Pro koho se full hodí a kdy stačí hardtail</h2>'
          '<p>Celoodpružené kolo vyhoví tomu, kdo jezdí často po kořenitých nebo kamenitých stezkách a chce mít větší komfort a kontrolu. Pro lesní cesty, nízké kopce nebo kolo na dojíždění je výhodnější lehčí a levnější pevné <a href="/horska-kola/">horské kolo</a>. Pro delší výlety po silnici se hodí <a href="/trekingova-kola/">trekingová</a> nebo <a href="/silnicni-kola/">silniční</a> kola a pro nenáročné výjezdy <a href="/krosova-kola/">krosová kola</a>. Pokud chcete podporu motoru v kopcích, najdete ji v kategorii <a href="/horska-elektrokola/">horská elektrokola</a>.</p>'
          '<h2>Jak se kolo chová na stezce</h2>'
          '<p>Na kamenech a kořenech zadní stavba ustupuje a drží kolo na zemi, takže má zadní kolo trakci i při šlapání v členitém terénu. V ostrých zatáčkách se oceňuje stabilita a v rychlých sjezdech menší únava rukou a zápěstí. Na hladkém povrchu a v kopci se ale může kolo houpat, hlavně pokud je tlumič příliš měkký. Proto je důležitá správná poloha na kole: v kopci sedět vpředu na sedle s tělem vysunutým dopředu, aby se nezvedalo přední kolo, ve sjezdu stát na pedálech s pokrčenými koleny a lokty.</p>'
          '<p>Kdo přechází z pevného kola, potřebuje pár výletů, než si zvykne na jiné vnímání terénu. Odpružení odpouští chyby ve stopě, ale nahrazuje techniku jen částečně. Krátký kurz techniky jízdy nebo jízda s zkušenějším kamarádem pomůže víc než dražší komponenty.</p>'
          '<h2>Přeprava a skladování</h2>'
          '<p>Celoodpružené kolo je těžší a hůř se zavěšuje na standardní držáky, proto před koupí zkontrolujte, zda ho unese váš <a href="/cyklo-nosice-na-auto/">nosič kol na auto</a>. Některé nosiče nejsou určeny pro kola s rámem bez horní trubky nebo s extrémně širokými plášti. Při skladování v bytě se vyplatí držák na zeď, který odlehčí zadní stavbě. Odpružení je dobré uložit lehce roztlačené, ne propadlé, a po zimě zkontrolovat tlak ve vidlici a tlumiči.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<p>Nejčastější chybou je koupit kolo s příliš velkým zdvihem pro místní trasy, takže je těžké a pomalé. Druhou je nastavení odpružení ponechané ve výchozím stavu bez ohledu na váhu jezdce. Třetí je koupě velikosti podle vzhledu, ne podle tabulky a zkoušky. Čtvrtou je zanedbání servisu a pětou podcenění ochrany hlavy a těla.</p>'
          '<h2>Jak nakupovat na srovnávači</h2>'
          '<p>Sporteka seřazuje nabídky různých obchodů a ukazuje dostupné velikosti. U každého modelu zkontrolujte ročník, velikost rámu a kol, typ rámu a výbavu, protože stejný název může mít několik úrovní komponentů. Poznamenejte si, zda se kolo dodává smontované, nebo zčásti rozložené, a jaké jsou podmínky vrácení u velkého zboží.</p>',
    faq=[('Čím se liší celoodpružené kolo od hardtailu?', 'Celoodpružené kolo má pružinu i vzadu, takže lépe tlumí nárazy a drží stopu v terénu. Je ale těžší, složitější a vyžaduje víc servisu. Hardtail je lehčí, jednodušší a levnější.'),
         ('Jaký zdvih je pro mě vhodný?', 'Pro rychlé cross-country trasy zhruba 100 až 120 mm, pro univerzální stezky 120 až 150 mm a pro náročné sjezdy více. Rozhodněte podle nejčastějšího terénu, ne podle maxima.'),
         ('Jsou lepší kola 29", nebo 27,5"?', 'Větší 29" se lépe valí a překonávají překážky, menší 27,5" jsou hravější a lépe vyhoví nižším postavám. Některá kola kombinují obojí.'),
         ('Je karbonový rám lepší než hliníkový?', 'Je lehčí a tužší, ale dražší a citlivější na nárazy a špatné utažení. Hliník je odolný a levnější. Pro většinu jezdců stačí kvalitní hliník.'),
         ('Jak nastavit tlak ve vidlici a tlumiči?', 'Podle váhy jezdce a doporučení výrobce, přičemž se sleduje sag, tedy propad odpružení při sezení. Nastavení vám při koupi ukáže servis nebo obchod.'),
         ('Kdy servisovat odpružení?', 'Podle návodu výrobce, obvykle po určitém počtu hodin jízdy, u těžkého terénu a bahna častěji. Zanedbaný servis zkracuje životnost těsnění a ložisek.'),
         ('Hodí se celoodpružené kolo na silnici?', 'Příliš ne, zbytečně se pohupuje a je těžší. Na asfalt a lehký terén se hodí trekingová, gravel nebo silniční kola. Zámek odpružení problém zmírní, ale neodstraní.'),
         ('Jakou ochranu při jízdě na fullu používat?', 'Helmu a rukavice vždy, při technických stezkách a sjezdech navíc chrániče kolen a loktů a případně integrální helmu. Pro lehčí terén stačí otevřená MTB helma.'),
         ('Mohu jet s plným odpružením do kopce?', 'Ano, moderní kola mají zámek nebo přepínač tlumiče a geometrii, která pomáhá. Je ale těžší než pevné kolo, takže bude náročnější, zvlášť na delších stoupáních.'),
         ('Jak si vybrat mezi novým a bazarovým fullem?', 'Bazarové kolo bývá levnější, ale odpružení má opotřebované těsnění, ložiska zadní stavby a případně vůli v čepech. Před koupí zkontrolujte rám na praskliny kolem svarů a spojů, funkci vidlice a tlumiče, stav pohonu a servisní historii. U nového kola máte záruku a aktuální geometrii. Záleží, zda vám stačí starší model s kvalitnější výbavou, nebo je lepší novější konstrukce. Nezapomeňte započítat i servis odpružení, výměnu opotřebovaného řetězu a brzdových destiček, které mohou na bazarovém kole přijít brzy po koupi.'),
         ('Kde sehnat elektrické horské kolo?', 'V kategorii horská elektrokola. Elektropohon pomáhá v kopcích, ale zvyšuje hmotnost a cenu kola.')])
