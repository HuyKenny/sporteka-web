"""Guides wave 5c (2026-11-19): jak-vybrat-spacak, jak-vybrat-stan, jak-vybrat-karimatku, hardshell-vs-softshell.

Demand (CZ / month): jak vybrat spacák 150, jak vybrat stan 80, jak vybrat karimatku 80, hardshell vs softshell 150.

Sources used for the facts:
- Sleeping bag ratings: australianhiker.com.au "ISO 23537-1:2022 sleeping bag temperature rating" (EN 13537 replaced by
  ISO 23537-1; comfort = standard woman sleeping comfortably in a relaxed position; lower limit = standard man sleeping
  8 hours curled up without waking; extreme = survival only for a standard woman, strong cold and risk of hypothermia
  between limit and extreme; standard man 25 y, 1.73 m, 73 kg, standard woman 25 y, 1.60 m, 60 kg; manikin on an
  insulating mat wearing one layer of long underwear; upper limit rarely used commercially); AFNOR / ISO catalogue
  entries for ISO 23537-1:2016 and :2022 (2022 edition covers bags with limit temperature of -20 degC and higher,
  not military or extreme expedition bags); Ferrino "Sleeping bag temperatures".
- Sleeping pads: Sea to Summit "The new ASTM R-values for sleeping mats" (ASTM F3340-18 is the industry test, hot
  plate kept at 35 degC on one side and a cold plate on the other, energy needed to keep the hot plate warm is
  measured, air mats inflated to 0.5 psi, R-values are additive (2 + 3 = 5), warm climates roughly R 0-2, winter or
  at/below 0 degC roughly R 4-6, the standard is voluntary, ratings since 2020 releases, some values went up and some
  down versus old in-house numbers); ASTM newsroom and store page F3340-18; Outside / SectionHiker articles (makers
  incl. Therm-a-Rest started developing the method in 2016; cold plate around 5 degC); REI policy that listed pads carry
  an ASTM F3340-18 rating (via search snippets).
- Tents and membranes: our own guide vodni-sloupec (ISO 811 hydrostatic test, fly vs floor values, RET bands, membrane
  types, 2 / 2.5 / 3-layer laminates) for consistency; general manufacturer conventions (minimum vs packed weight,
  inner-first vs fly-first pitching, footprint slightly smaller than the floor so rain does not collect on it).
Left out because not verified: exact centimetre rule for sleeping-bag length, numbers for how many degrees a liner
adds, exact fill-power test norm, the year the term softshell appeared, any tent water-column minimum stated by a
norm, the R-value at which a pad becomes "winter" according to the standard (the standard sets no seasons).
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- jak-vybrat-spacak
SPACAK_TEPLOTY = T(['Údaj na štítku', 'Co znamená', 'Jak ho používat'], [
    ['Komfort (T comf)', 'Standardní žena spí v uvolněné poloze bez pocitu chladu', 'Hlavní údaj pro ženy a pro každého, kdo snadno zebe'],
    ['Limit (T lim)', 'Standardní muž vydrží 8 hodin spát schoulený, aniž by ho chlad vzbudil', 'Spodní hranice pro muže, kteří spí v teple'],
    ['Extrém (T ext)', 'Hranice přežití, chlad je silný a hrozí podchlazení', 'Nikdy podle něj nevybírejte'],
])

SPACAK_VYPLN = T(['Vlastnost', 'Peří (prachové peří)', 'Syntetické vlákno'], [
    ['Hřejivost vůči hmotnosti', 'Vyšší, spacák je lehčí', 'Nižší, při stejné teplotě je těžší'],
    ['Sbalitelnost', 'Velmi dobrá', 'Horší, zabere víc místa'],
    ['Chování ve vlhku', 'Mokré peří slehne a přestane hřát', 'Hřeje i ve vlhku a rychleji schne'],
    ['Péče', 'Speciální prací prostředek, dlouhé sušení', 'Jednodušší praní i sušení'],
    ['Životnost', 'Při dobré péči mnoho let', 'Vlákno se postupně slehává'],
    ['Kde se hodí', 'Hory, chladné noci, přenášení na zádech', 'Vlhké podmínky, voda, děti, kempování u auta'],
])

GUIDES['jak-vybrat-spacak'] = dict(
    name='Jak vybrat spacák',
    h1='Jak vybrat spacák: teploty, výplň a tvar',
    seo_title='Jak vybrat spacák: teploty, výplň a tvar spacího pytle',
    seo_desc='Jak číst teploty komfort, limit a extrém podle ISO 23537, kdy peří a kdy syntetika, mumie nebo deka, jaká délka a k čemu vložka. Praktický návod.',
    intro_html=(
        '<p><strong>Jak vybrat spacák?</strong> Začněte nejnižší teplotou, při které budete spát, a porovnejte ji s údajem <strong>komfort</strong> na štítku. '
        'Ženy a lidé, kteří snadno zebou, vybírají podle komfortu, muži, kterým bývá teplo, mohou jít až k hodnotě <strong>limit</strong>. Údaj extrém je hranice přežití a pro výběr se nepoužívá. '
        'Pak rozhodněte výplň: peří je lehčí a lépe se sbalí, syntetika snáší vlhko. Tvar mumie hřeje víc, dekový spacák je pohodlnější do kempu. '
        'Délku volte podle výšky postavy, kterou výrobce uvádí, a nezapomeňte na karimatku, bez které nehřeje ani dobrý spacák.</p>'
        '<p>V návodu vysvětlíme, jak se teploty měří, co ovlivňuje skutečné teplo v noci, jak se liší konstrukce komor, jak spacák skladovat a čemu se při nákupu vyhnout. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů, takže pod jednotlivými částmi uvidíte spacáky z naší nabídky.</p>'
    ),
    sections=[
        dict(h2='Teploty na štítku: komfort, limit a extrém',
             html=(
                 '<p>Teplotní údaje spacáků v Evropě vycházejí z normy <strong>EN ISO 23537-1</strong>, která nahradila dřívější normu EN 13537. '
                 'Spacák se měří v laboratoři na vyhřívané figuríně, která leží na izolační podložce a má na sobě jednu vrstvu dlouhého funkčního prádla. Z naměřených hodnot vzniknou tři teploty:</p>'
                 + SPACAK_TEPLOTY +
                 '<p>Norma počítá se „standardním mužem“ (25 let, 173 cm, 73 kg) a „standardní ženou“ (25 let, 160 cm, 60 kg). Ženy obecně zebou dřív, proto se komfort vztahuje k ženě a limit k muži. '
                 'Rozdíl mezi komfortem a limitem bývá několik stupňů. Mezi limitem a extrémem už počítejte se silným chladem a rizikem podchlazení.</p>'
                 '<p>Pozor na spacáky, které uvádějí jen jedno číslo bez odkazu na normu. Může to být komfort, limit i extrém, a výrobce to nemusí říct. Pro srovnání více modelů se držte těch, které mají všechny hodnoty změřené podle ISO 23537.</p>'
             ), cat='spaci-pytle', n=4),
        dict(h2='Proč vám může být zima i ve „správném“ spacáku',
             html=(
                 '<p>Laboratorní teplota předpokládá ideální podmínky. Ve skutečnosti ji posune několik věcí:</p>'
                 '<ul><li><strong>Podložka.</strong> Země odvádí teplo mnohem rychleji než vzduch. Peří pod vámi se slehne vahou těla a skoro neizoluje. Bez karimatky s dostatečnou R-hodnotou budete mrznout i v zimním spacáku.</li>'
                 '<li><strong>Únava a jídlo.</strong> Po celodenním pochodu a bez teplé večeře tělo produkuje méně tepla.</li>'
                 '<li><strong>Vlhkost.</strong> Vlhký vzduch, kondenzace ve stanu nebo propocené oblečení snižují izolaci výplně.</li>'
                 '<li><strong>Vítr a úkryt.</strong> Spaní pod širákem nebo pod tarpem je chladnější než ve stanu.</li>'
                 '<li><strong>Individuální rozdíly.</strong> Věk, hmotnost, kondice i to, jak snadno zebete, se mezi lidmi liší víc, než by se zdálo.</li></ul>'
                 '<p>Proto je rozumné nechat si rezervu a vybírat spacák, jehož komfort leží několik stupňů pod nejnižší teplotou, kterou čekáte. '
                 'V horách se v noci ochlazuje rychleji než v nížině a na jaře nebo na podzim bývá u země přízemní mráz, i když přes den je teplo.</p>'
             )),
        dict(h2='Peří, nebo syntetika',
             html=(
                 '<p>Výplň rozhoduje o hmotnosti, objemu po sbalení a o tom, jak spacák snese vlhko. Srovnání v kostce:</p>'
                 + SPACAK_VYPLN +
                 '<p>U péřových spacáků sledujte dva údaje. <strong>Poměr prachového peří a peří</strong> (například 90/10) říká, kolik je ve výplni lehkého chmýří a kolik tužších per. '
                 '<strong>Plnivost</strong> (fill power) v jednotkách cuin udává, jaký objem zaujme unce peří. Čím vyšší číslo, tím víc vzduchu peří udrží při stejné hmotnosti. '
                 'Vyšší plnivost ale sama nic neříká o teplotě, protože záleží i na tom, kolik peří ve spacáku je. Výrobci, kteří nakupují peří podle standardu RDS (Responsible Down Standard), deklarují, že pochází od zvířat chovaných bez živého škubání.</p>'
                 '<p>Syntetické spacáky jsou plněné dutými polyesterovými vlákny, buď v podobě souvislého rouna, nebo krátkých vloček. Jsou levnější, snesou časté praní a nevadí jim, když se u vody navlhčí. '
                 'Na letní kempování, k vodě a pro děti jsou praktičtější volbou. Péřové modely najdete v kategorii <a href="/perove-spacaky/">péřové spacáky</a>.</p>'
             ), cat='perove-spacaky', n=4),
        dict(h2='Mumie, nebo dekový spacák',
             html=(
                 '<p><strong>Mumie</strong> se zužuje k nohám a má kapuci se stahováním. Uvnitř je málo vzduchu, který musí tělo zahřát, takže při stejné výplni hřeje víc a váží méně. '
                 'Kapuce zabrání úniku tepla kolem hlavy. Na turistiku, do hor a na zimní spaní je to standard.</p>'
                 '<p><strong>Dekový spacák</strong> má obdélníkový tvar, víc místa na nohy a často jde úplně rozepnout na deku. Dva stejné modely s opačným zipem se dají spojit do dvojspacáku. '
                 'Vyhovuje lidem, kteří spí na břiše nebo se v noci často otáčejí, a hodí se ke kempování u auta, na chatu nebo do přívěsu. Hřeje však méně a je objemnější.</p>'
                 '<p>Mezi nimi stojí <strong>poloviční mumie</strong> (anglicky semi-rectangular), která je v nohou širší, ale pořád má kapuci. Je to dobrý kompromis pro ty, kterým je klasická mumie těsná.</p>'
                 '<p>Pro kempování, kde nerozhoduje hmotnost, se podívejte na <a href="/dekove-spacaky/">dekové spacáky</a>. Dětem vybírejte zvlášť <a href="/detske-spacaky/">dětské spacáky</a>, protože v dlouhém spacáku zůstane u nohou studený vzduch.</p>'
             ), cat='dekove-spacaky', n=4),
        dict(h2='Délka, šířka a zip',
             html=(
                 '<p>Výrobci obvykle uvádějí, do jaké výšky postavy je spacák určený, nebo nabízejí stejný model v několika délkách (například regular a long). Řiďte se tímto údajem, ne celkovou délkou spacáku, protože vnější rozměr zahrnuje i kapuci.</p>'
                 '<ul><li><strong>Příliš krátký spacák</strong> tlačí na nohy a ramena, výplň se stlačí a v těch místech zebete.</li>'
                 '<li><strong>Příliš dlouhý spacák</strong> má u nohou prázdný prostor, který musíte zahřát. Dá se do něj vložit oblečení na ráno, ale jinak je to zbytečná hmotnost.</li>'
                 '<li><strong>Šířka v ramenou</strong> rozhoduje u statnějších lidí. Pokud jste široký v ramenou, zkuste si spacák nejdřív lehnout v obchodě.</li></ul>'
                 '<p>Zip bývá vpravo nebo vlevo. Pokud chcete dva spacáky spojit, potřebujete jeden pravý a jeden levý se stejným typem zipu. '
                 'Kvalitní spacák má podél zipu tepelný límec (zateplenou lištu), který brání úniku tepla, a kolem krku stahovací límec. Ženské modely bývají kratší, v bocích širší a mají víc výplně u nohou.</p>'
             )),
        dict(h2='Konstrukce komor a další detaily',
             html=(
                 '<p>Výplň je ve spacáku rozdělena do komor, aby se nepřesouvala. Způsob šití ovlivňuje teplo:</p>'
                 '<ul><li><strong>Prošívaná konstrukce</strong> spojuje vrchní a vnitřní látku přímo švem. Je lehká a levná, ale ve švech je izolace tenká. Hodí se do teplých nocí.</li>'
                 '<li><strong>Komory s přepážkami</strong> (H, trapézové nebo V) oddělují látky pásky textilie. Výplň má kde nadýchnout a teplé místo vznikne i nad švem. Používají je teplejší péřové spacáky.</li>'
                 '<li><strong>Vícevrstvé syntetické rouno</strong> se kladí s přesazenými švy, aby se studené linie překrývaly.</li></ul>'
                 '<p>Další užitečné detaily jsou kapsička na mobil nebo čelovku, dvoucestný zip, kterým jde větrat u nohou, a vrchní látka s vodoodpudivou úpravou proti kondenzátu. '
                 'U zimních spacáků se vyplatí tvarovaný prostor pro nohy, který nestlačuje výplň.</p>'
             )),
        dict(h2='Vložka do spacáku a jak si přidat teplo',
             html=(
                 '<p><strong>Vložka do spacáku</strong> je tenký pytel z bavlny, hedvábí, fleece nebo syntetiky, který se vloží dovnitř. Hlavní smysl má hygienický: chrání vnitřek spacáku před potem a kožním mazem, takže spacák se pere méně často. '
                 'Vložku vyperete po každé cestě, spacák jen jednou za čas. V teplých nocích můžete spát jen ve vložce.</p>'
                 '<p>Výrobci u některých vložek uvádějí, o kolik stupňů spacák oteplí. Tyto údaje se neměří podle normy pro spacáky, takže je berte jako orientační. Fleecové a termovložky přidají znatelně víc než tenká bavlna nebo hedvábí.</p>'
                 '<p>Teplo navíc získáte i jinak:</p>'
                 '<ol><li>Spěte v suchém funkčním prádle, ne v oblečení, ve kterém jste šli.</li>'
                 '<li>Vezměte si čepici a ponožky, hlavně na podzim a v zimě.</li>'
                 '<li>Před spaním se najezte a napijte teplého.</li>'
                 '<li>Pod sebe dejte karimatku s vyšší R-hodnotou nebo dvě karimatky na sebe.</li>'
                 '<li>Ráno spacák větrejte, aby z výplně odešla vlhkost.</li></ol>'
                 '<p>Vložky najdete v kategorii <a href="/vlozky-do-spacaku/">vložky do spacáků</a>, prádlo na spaní pod <a href="/termopradlo/">termoprádlem</a>.</p>'
             ), cat='vlozky-do-spacaku', n=4),
        dict(h2='Hmotnost, sbalení a skladování',
             html=(
                 '<p>Pokud spacák ponesete na zádech, sledujte hmotnost a objem po sbalení. U letních péřových spacáků jde o stovky gramů, zimní modely bývají výrazně těžší. '
                 'Kompresní vak zmenší objem v batohu, ale spacák v něm nenechávejte déle než na cestu.</p>'
                 '<p>Doma skladujte spacák volně: v prodyšném úložném vaku, který bývá v balení, nebo zavěšený ve skříni. Dlouhodobě stlačená výplň ztrácí schopnost nadýchnout se, a tím i hřát. '
                 'Před uskladněním spacák dobře vysušte, vlhký spacák může začít plesnivět.</p>'
                 '<p>Péřový spacák perte jen podle štítku a se speciálním prostředkem na peří. Postup je podobný jako u bundy, který popisujeme v návodu <a href="/jak-prat-perovou-bundu/">jak prát péřovou bundu</a>. Spacák nikdy nežehlete a nedávejte do chemické čistírny, pokud to výrobce výslovně nepovoluje.</p>'
             )),
        dict(h2='Jaký spacák na léto, přechodné období a zimu',
             html=(
                 '<p>Hrubé vodítko podle použití. Konkrétní teploty vždy porovnejte s tím, kam jedete, a nechte si rezervu:</p>'
                 + T(['Použití', 'Na co se dívat', 'Výplň a tvar'], [
                     ['Letní kemp, festival, chata', 'Komfort zhruba nad +10 °C, možnost rozepnout na deku', 'Syntetika, dekový tvar'],
                     ['Jaro a podzim, turistika', 'Komfort kolem 0 až +5 °C podle oblasti', 'Peří i syntetika, mumie'],
                     ['Hory a chladné noci', 'Komfort pod nulou, kapuce a tepelný límec', 'Spíš peří, mumie s komorami'],
                     ['Zimní spaní', 'Komfort hluboko pod nulou, prostor na nohy', 'Peří s přepážkami, zimní karimatka'],
                 ]) +
                 '<p>Vyplatí se mít spíše dva spacáky pro různé sezóny než jeden, který je v létě horký a v zimě nestačí. Letní spacák navíc můžete v chladu použít jako vrchní vrstvu přes teplejší.</p>'
             )),
        dict(h2='Nejčastější chyby a jak porovnat nabídky',
             html=(
                 '<ul><li>Vybírat podle údaje extrém, nebo podle jednoho čísla bez normy.</li>'
                 '<li>Koupit drahý spacák a spát na tenké pěnové podložce v zimě.</li>'
                 '<li>Vzít péřový spacák k vodě bez nepromokavého vaku.</li>'
                 '<li>Skladovat spacák měsíce ve kompresním obalu.</li>'
                 '<li>Ignorovat délku a šířku: příliš těsný spacák hřeje méně.</li></ul>'
                 '<p>Při porovnání nabídek si zapište tři teploty, hmotnost, výplň, délku a stranu zipu. Stejný model se v obchodech prodává pod drobně odlišnými názvy, proto kontrolujte kód nebo variantu délky. '
                 'Na Sporteka porovnáte nabídky českých obchodů v kategorii <a href="/spaci-pytle/">spací pytle</a>. Karimatku k nim pomůže vybrat náš návod <a href="/jak-vybrat-karimatku/">jak vybrat karimatku</a>.</p>'
             ), cat='spaci-pytle', n=4),
    ],
    faq=[
        ('Podle jaké teploty mám vybírat spacák?',
         '<p>Ženy a lidé, kteří snadno zebou, podle teploty komfort. Muži, kterým bývá spíš teplo, mohou vybírat podle limitu. Extrém je hranice přežití a pro výběr se nepoužívá. Nechte si rezervu několika stupňů.</p>'),
        ('Co znamená komfort a limit u spacáku?',
         '<p>Komfort je teplota, při které standardní žena spí v uvolněné poloze bez pocitu chladu. Limit je teplota, při které standardní muž vydrží spát osm hodin schoulený, aniž by ho chlad probudil. Obojí se měří podle EN ISO 23537-1.</p>'),
        ('Je lepší péřový, nebo syntetický spacák?',
         '<p>Péřový je lehčí a lépe se sbalí, ale ve vlhku přestává hřát. Syntetický je těžší a objemnější, zato snáší vlhko, rychleji schne a je levnější. Do hor a na přenášení spíš peří, k vodě a pro děti spíš syntetika.</p>'),
        ('Mumie, nebo dekový spacák?',
         '<p>Mumie hřeje víc při stejné hmotnosti a má kapuci, proto se hodí na turistiku a do chladu. Dekový spacák je prostornější, dá se rozepnout a spojit s druhým, ale je těžší a méně hřeje. Hodí se na kempování u auta a na chatu.</p>'),
        ('Jak dlouhý spacák potřebuji?',
         '<p>Řiďte se výškou postavy, kterou výrobce u modelu uvádí, nebo vyberte správnou délku (regular, long). Příliš krátký spacák stlačuje výplň, příliš dlouhý má u nohou prázdný prostor, který musíte zahřát.</p>'),
        ('K čemu je vložka do spacáku?',
         '<p>Hlavně chrání spacák před potem a nečistotou, takže ho stačí prát méně často. Teplejší vložky z fleece nebo termo materiálů přidají i trochu tepla, údaje výrobců jsou ale jen orientační.</p>'),
        ('Proč mi je ve spacáku zima, i když má nízkou teplotu?',
         '<p>Nejčastěji kvůli slabé karimatce, vlhkosti, únavě nebo hladu. Laboratorní měření počítá s izolační podložkou a suchým prádlem. Pomůže lepší karimatka, suché oblečení, čepice a teplé jídlo před spaním.</p>'),
        ('Jak skladovat spacák?',
         '<p>Volně, v prodyšném úložném vaku nebo zavěšený, suchý a v chladnu. Kompresní obal používejte jen na cestu, dlouhodobé stlačení výplni škodí.</p>'),
        ('Mohu prát péřový spacák v pračce?',
         '<p>Pokud to štítek dovoluje, ano: s prostředkem na peří, na šetrný program a s důkladným mácháním. Pak ho dlouho sušte v sušičce na nízkou teplotu s míčky, aby se peří rozbilo z hrudek.</p>'),
    ],
    cats=['spaci-pytle', 'perove-spacaky', 'dekove-spacaky', 'vlozky-do-spacaku', 'detske-spacaky'],
    updated='2026-11-19')

# ---------------------------------------------------------------- jak-vybrat-stan
STAN_TYPY = T(['Typ stanu', 'Konstrukce', 'Výhody', 'Nevýhody'], [
    ['Kopulový (iglú)', 'Dvě zkřížené tyče', 'Samostatně stojí, rychlá stavba, levný', 'Méně stabilní v silném větru'],
    ['Tunelový', 'Paralelní oblouky, nutné kotvení', 'Hodně prostoru na hmotnost, velké předsíně', 'Bez kolíků nestojí, citlivý na boční vítr'],
    ['Geodetický a polo-geodetický', 'Více tyčí, které se kříží na více místech', 'Stabilní ve větru a pod sněhem', 'Těžší, dražší, složitější stavba'],
    ['Pop-up', 'Pružné obruče, rozloží se samy', 'Postavený za chvíli', 'Neskládá se snadno, slabší ve větru a dešti'],
    ['Nafukovací', 'Vzduchové trubice místo tyčí', 'Rychlá stavba velkých stanů', 'Vyšší hmotnost, nutná pumpa'],
])

GUIDES['jak-vybrat-stan'] = dict(
    name='Jak vybrat stan',
    h1='Jak vybrat stan: počet osob, váha a vodní sloupec',
    seo_title='Jak vybrat stan: počet osob, váha, vodní sloupec a typy stanů',
    seo_desc='Kolik osob, jaký typ konstrukce, vodní sloupec tropika a podlahy, tyče z hliníku nebo sklolaminátu, předsíň a podložka pod stan. Návod krok za krokem.',
    intro_html=(
        '<p><strong>Jak vybrat stan?</strong> Rozhodněte nejdřív, jestli ho ponesete na zádech, nebo vozíte autem. Pro turistiku hledejte lehký dvouplášťový stan s hmotností, kterou unesete, pro kemp u auta stan s větší výškou a předsíní. '
        'Kapacitu berte s rezervou: v udávaném počtu osob se leží těsně vedle sebe, takže pro pohodlí a zavazadla volte stan o jedno místo větší. '
        'Pak zkontrolujte <strong>vodní sloupec</strong> tropika a podlahy, materiál tyčí, počet vchodů a větrání.</p>'
        '<p>Návod projde typy stanů, rozložení a předsíně, materiály, údaje o hmotnosti, stavění i podložku pod stan. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů. U jednotlivých částí najdete stany z naší nabídky.</p>'
    ),
    sections=[
        dict(h2='K čemu stan budete používat',
             html=(
                 '<p>Jeden stan na všechno neexistuje. Než začnete porovnávat, odpovězte si na tyto otázky:</p>'
                 '<ol><li><strong>Ponesu ho?</strong> Na přechod hor nebo dálkovou trasu rozhoduje každé kilo. U auta hmotnost téměř nehraje roli.</li>'
                 '<li><strong>Kolik nás bude a kolik věcí?</strong> Batohy, boty a mokré oblečení potřebují místo v předsíni.</li>'
                 '<li><strong>Kdy a kde?</strong> Letní kemp u řeky, hory na jaře a na podzim, nebo zimní spaní pod sněhem jsou tři různé kategorie.</li>'
                 '<li><strong>Jak často?</strong> Na pár víkendů v roce stačí jednodušší stan. Na pravidelné cesty se vyplatí kvalitnější tyče a látky.</li></ol>'
                 '<p>Podle odpovědí se dostanete k jedné z hlavních skupin: <a href="/turisticke-stany/">turistické stany</a> pro chůzi, <a href="/rodinne-stany/">rodinné stany</a> pro kemp, <a href="/expedicni-stany/">expediční stany</a> do zimy a na vysoké hory, nebo plážové a pop-up stany na den u vody.</p>'
             ), cat='turisticke-stany', n=4),
        dict(h2='Typy stanů podle konstrukce',
             html=(
                 STAN_TYPY +
                 '<p><strong>Kopulový stan</strong> je nejrozšířenější. Stojí i bez kolíků, takže ho můžete přenést na jiné místo, ale v dešti a větru ho stejně vždy ukotvěte. '
                 '<strong>Tunelový stan</strong> nabízí nejvíc prostoru vůči hmotnosti a bývá oblíbený u rodinných modelů s několika ložnicemi. Postavte ho zadní stranou proti větru. '
                 '<strong>Geodetické</strong> konstrukce mají víc průsečíků tyčí, rozkládají zatížení a vydrží i silný vítr nebo sníh, proto se používají u expedičních stanů.</p>'
                 '<p>Existují i ultralehké stany napínané trekovými holemi místo tyčí. Vyžadují zkušenost se stavěním a pečlivé kotvení.</p>'
             )),
        dict(h2='Počet osob a rozložení',
             html=(
                 '<p>Údaj „pro 2 osoby“ znamená, že se na podlahu vejdou dvě karimatky standardní šíře vedle sebe. Na batohy, širší karimatky ani na pohyb už místo nezbývá. Proto platí několik pravidel:</p>'
                 '<ul><li>Dva dospělí s výbavou na delší cestu budou spokojenější ve stanu pro tři.</li>'
                 '<li>Rodina se dvěma dětmi ocení stan pro pět nebo šest osob a samostatné ložnice.</li>'
                 '<li>Solo turista, který hlídá hmotnost, zvládne jednomístný stan, pohodlněji se ale vyspí ve dvoumístném.</li></ul>'
                 '<p>Na rozměrech záleží víc než na čísle. Porovnejte délku a šířku ložnice a výšku v nejvyšším bodě. Vysocí lidé by měli porovnat délku ložnice se svou výškou i s délkou spacáku, aby nohama a hlavou nedrhli o mokré stěny. '
                 'Stany s vchodem z boku a dvěma předsíněmi umožní každému vylézt bez přelézání druhého. Stany s vchodem v čele jsou lehčí, ale méně pohodlné.</p>'
                 '<p>Předsíň (apsida) je prostor mezi ložnicí a tropikem. Uložíte tam batoh a boty a v nouzi i vaříte, vždy ale s otevřeným vchodem a s vědomím rizika požáru a oxidu uhelnatého.</p>'
             ), cat='rodinne-stany', n=4),
        dict(h2='Vodní sloupec tropika a podlahy',
             html=(
                 '<p>Odolnost látky proti vodě se udává ve <strong>vodním sloupci</strong> v milimetrech. Měří se podle normy ISO 811: na látku se zespodu tlačí voda a hodnota je tlak, při kterém voda prosákne. '
                 'U stanů se uvádí zvlášť číslo pro tropiko a pro podlahu. Podlaha mívá vyšší hodnotu, protože na mokrou zem ji tlačí váha těla, kolena a lokty.</p>'
                 '<p>Pro letní kempování stačí tropiko, které vydrží běžný déšť. Na vícedenní cesty, kde nemáte kam utéct, hledejte vyšší hodnoty a hlavně podlepené švy. '
                 'Žádná norma ale pevnou hranici „nepromokavého stanu“ nestanoví, takže samotné číslo nestačí. Stejně důležitá je kvalita švů, napnutí tropika a odstup mezi tropikem a ložnicí.</p>'
                 '<p>Látky tropika bývají ze silikonovaného nylonu nebo polyesteru s polyuretanovým zátěrem. Nylon je pevnější a lehčí, ale za vlhka povolí a tropiko je potřeba dopnout. Polyester se prověšuje méně a lépe snáší slunce. '
                 'Podrobně jednotky a měření vysvětluje průvodce <a href="/vodni-sloupec/">vodní sloupec a prodyšnost</a>.</p>'
             )),
        dict(h2='Dvouplášťový stan, kondenzace a větrání',
             html=(
                 '<p>Většina stanů je <strong>dvouplášťová</strong>: vnitřní ložnice z prodyšné látky a nad ní nepromokavé tropiko. Pára z dechu a těla projde ložnicí a srazí se na tropiku, odkud steče do země. '
                 '<strong>Jednoplášťové</strong> stany jsou lehčí, ale kondenzace se drží přímo na stěně, ke které se ve spaní dotýkáte.</p>'
                 '<p>Kondenzaci nezabrání žádný stan úplně. Za chladné vlhké noci je tropiko zevnitř mokré i u drahých modelů. Pomůže:</p>'
                 '<ol><li>Postavit stan mimo dno údolí a břehy, kde se drží studený vlhký vzduch.</li>'
                 '<li>Nechat otevřené větrací otvory i v dešti, pokud jsou kryté stříškou.</li>'
                 '<li>Nedávat do ložnice mokré oblečení a nevařit uvnitř.</li>'
                 '<li>Dobře vypnout tropiko, aby se nedotýkalo ložnice.</li></ol>'
                 '<p>Moskytiéra ve vchodech a ve větracích otvorech je samozřejmostí, u vody a v létě to oceníte nejvíc.</p>'
             )),
        dict(h2='Tyče: hliník, sklolaminát, nebo vzduch',
             html=(
                 '<p>Tyče nesou celý stan a podle nich se dá dost poznat jeho kvalita.</p>'
                 '<ul><li><strong>Hliníkové tyče</strong> jsou lehké a pevné. Když se ohnou, často se dají narovnat nebo dlahovat opravnou trubičkou. Používají je kvalitnější turistické a expediční stany.</li>'
                 '<li><strong>Sklolaminátové tyče</strong> jsou levnější a těžší. Při zatížení a v mrazu mohou prasknout a štěpit se. Najdete je hlavně u levnějších a rodinných stanů.</li>'
                 '<li><strong>Karbonové tyče</strong> jsou nejlehčí, ale citlivé na nárazy a bodové přetížení.</li>'
                 '<li><strong>Nafukovací trubice</strong> nahrazují tyče u velkých rodinných stanů. Stavba je rychlá, potřebujete ale pumpu.</li></ul>'
                 '<p>Důležité je i to, jak se ložnice na tyče připíná. Háčky a klipy jsou rychlejší než návleky. Stany, které se staví <strong>tropikem napřed</strong> (nebo obojím najednou), mají v dešti výhodu: ložnice zůstane suchá. '
                 'U stanů stavěných <strong>ložnicí napřed</strong> v dešti promokne vnitřek dřív, než přes něj přehodíte tropiko.</p>'
             ), cat='stany', n=4),
        dict(h2='Hmotnost: minimální, nebo balená',
             html=(
                 '<p>Výrobci uvádějí dva údaje. <strong>Minimální hmotnost</strong> zahrnuje jen tropiko, ložnici a tyče. <strong>Balená hmotnost</strong> počítá i kolíky, kotevní šňůry, obaly a případně opravnou sadu. '
                 'Na trase nesete obvykle něco mezi tím, proto porovnávejte vždy stejný údaj. Pokud obchod uvádí jen jedno číslo, ověřte u výrobce, o který jde.</p>'
                 '<p>Pro chůzi platí, že každý kilogram navíc ucítíte, proto porovnejte několik modelů stejné kapacity a podívejte se, o kolik se liší. Ultralehké stany váží méně, robustní expediční více. '
                 'Ve dvou se dá stan rozdělit, jeden nese tropiko a kolíky, druhý ložnici a tyče. U rodinných stanů se hmotnost počítá v desítkách kilogramů a nese je jen auto.</p>'
                 '<p>Lehčí stan obvykle znamená tenčí látky, které vyžadují víc péče. Na rozbité kempy a štěrková místa se hodí silnější podlaha nebo podložka pod stan.</p>'
             )),
        dict(h2='Podložka pod stan a kolíky',
             html=(
                 '<p><strong>Podložka pod stan</strong> (footprint) chrání podlahu před kamínky, kořeny a oděrem a prodlužuje jí život. Výrobci často prodávají podložky střižené přesně na konkrétní model. '
                 'Univerzální plachta by měla být o něco menší než podlaha. Když přečnívá, déšť po ní steče pod stan a voda se tam drží.</p>'
                 '<p>Kolíky v balení bývají univerzální a do tvrdé nebo písčité půdy nestačí. Do kamenitého terénu se hodí tvrdší hliníkové nebo ocelové kolíky, do písku a sněhu široké kolíky nebo sněhové kotvy. '
                 'Náhradní kolíky a podložky najdete v kategoriích <a href="/stanove-kolky/">stanové kolíky</a> a <a href="/stanove-doplnky/">stanové doplňky</a>.</p>'
                 '<p>Kotevní šňůry nepodceňujte. Stan, který stojí jen na kolících v rozích, se ve větru prohýbá a tropiko se dotýká ložnice. Šňůry napněte vždy, když se počasí kazí.</p>'
             ), cat='stanove-doplnky', n=4),
        dict(h2='Péče o stan a nejčastější chyby',
             html=(
                 '<p>Stan po cestě vždy vysušte, i když jste ho balili za sucha. Rosa a kondenzace ve složené látce za pár dní vyrobí plíseň a zápach a zátěr se může začít odlupovat. '
                 'Doma ho rozvěste nebo postavte a nechte uschnout. Skladujte volně složený v suchu, ne natěsno v obalu.</p>'
                 '<p>Časté chyby při výběru a používání:</p>'
                 '<ul><li>Koupit stan přesně pro počet osob a pak se tísnit s batohy uvnitř.</li>'
                 '<li>Neodzkoušet stavbu doma a poprvé ho stavět za tmy v dešti.</li>'
                 '<li>Stavět v prohlubni, kde se při dešti udělá louže.</li>'
                 '<li>Vařit v uzavřené předsíni.</li>'
                 '<li>Nechávat stan dny na přímém slunci, které látky postupně poškozuje.</li></ul>'
                 '<p>Při porovnání nabídek sledujte typ konstrukce, rozměry ložnice, vodní sloupec tropika i podlahy, materiál tyčí a hmotnost. V nabídce Sporteky porovnáte ceny modelů v kategoriích <a href="/stany/">stany</a>, <a href="/turisticke-stany/">turistické stany</a> a <a href="/rodinne-stany/">rodinné stany</a>. '
                 'Ke stanu budete potřebovat i spaní: pomůže návod <a href="/jak-vybrat-spacak/">jak vybrat spacák</a>.</p>'
             )),
    ],
    faq=[
        ('Jak velký stan si mám koupit?',
         '<p>O jedno místo větší, než je počet lidí, pokud chcete mít místo na batohy a pohyb. V udávaném počtu osob leží lidé těsně vedle sebe na standardních karimatkách.</p>'),
        ('Jaký vodní sloupec má mít stan?',
         '<p>Pevnou hranici žádná norma nestanoví. Podlaha by měla mít vyšší hodnotu než tropiko, protože na ni tlačí váha těla. Stejně důležité jako číslo jsou podlepené švy a dobře napnuté tropiko.</p>'),
        ('Jaký je rozdíl mezi kopulovým a tunelovým stanem?',
         '<p>Kopulový stan stojí sám díky zkříženým tyčím a rychle se staví. Tunelový nabízí víc prostoru na hmotnost, ale bez kotvení nestojí a je potřeba ho natočit zádí proti větru.</p>'),
        ('Jsou lepší hliníkové, nebo sklolaminátové tyče?',
         '<p>Hliníkové jsou lehčí, pevnější a dají se opravit. Sklolaminátové jsou levnější a těžší, v mrazu a při přetížení mohou prasknout. Na turistiku vybírejte hliník.</p>'),
        ('Potřebuji podložku pod stan?',
         '<p>Není nutná, ale chrání podlahu před oděrem a propíchnutím a prodlužuje životnost stanu. Měla by být o něco menší než podlaha, aby se na ní nezachytávala dešťová voda.</p>'),
        ('Proč je ve stanu ráno mokro?',
         '<p>Jde o kondenzaci páry z dechu a těla na studeném tropiku. Nejde o zatékání. Pomůže větrání, dobře napnuté tropiko a stavění mimo vlhká místa u vody a na dně údolí.</p>'),
        ('Kolik má vážit turistický stan?',
         '<p>Záleží na kapacitě a konstrukci: ultralehké modely váží nejméně, expediční nejvíc. Rodinné stany nese jen auto. Porovnávejte vždy stejný údaj, minimální nebo balenou hmotnost.</p>'),
        ('Co znamená stavění tropikem napřed?',
         '<p>Nejdřív se postaví nepromokavé tropiko a ložnice se zavěsí pod ně, případně se obě části staví spojené. V dešti tak ložnice zůstane suchá. U stanů stavěných ložnicí napřed se vnitřek může namočit.</p>'),
        ('Jak se starat o stan po výletě?',
         '<p>Vždy ho doma vysušte, i když byl při balení zdánlivě suchý. Skladujte ho volně v suchu. Nečistoty smyjte vlažnou vodou bez agresivních čisticích prostředků a nesušte ho na topení.</p>'),
    ],
    cats=['stany', 'turisticke-stany', 'rodinne-stany', 'expedicni-stany', 'stanove-doplnky'],
    updated='2026-11-19')

# ---------------------------------------------------------------- jak-vybrat-karimatku
KARIMATKA_TYPY = T(['Typ', 'Výhody', 'Nevýhody', 'Pro koho'], [
    ['Pěnová (uzavřené buňky)', 'Nepropíchnete ji, levná, funguje hned', 'Objemná, tvrdší, nižší R-hodnota', 'Krátké výlety, záloha pod nafukovací'],
    ['Samonafukovací', 'Pohodlnější než pěna, dobrá izolace, snadná oprava', 'Těžší a objemnější než nafukovací', 'Kempování, turistika bez hlídání gramů'],
    ['Nafukovací (vzduchová)', 'Nejlehčí a nejmenší po sbalení, vysoký komfort', 'Hrozí propíchnutí, nafukování, šustění', 'Turistika, hory, dálkové trasy'],
    ['Nafukovací matrace', 'Vysoký komfort, rozměr jako postel', 'Velká, těžká, často slabá izolace', 'Kemp u auta, chata, návštěvy'],
])

GUIDES['jak-vybrat-karimatku'] = dict(
    name='Jak vybrat karimatku',
    h1='Jak vybrat karimatku: R-hodnota a typy',
    seo_title='Jak vybrat karimatku: R-hodnota, typy a rozměry',
    seo_desc='Pěnová, samonafukovací, nebo nafukovací karimatka? Co znamená R-hodnota podle ASTM F3340-18, jaká na léto a zimu a jaké rozměry. Návod k výběru.',
    intro_html=(
        '<p><strong>Jak vybrat karimatku?</strong> Nejdůležitější údaj je <strong>R-hodnota</strong>, tedy jak dobře karimatka brání úniku tepla do země. Čím vyšší číslo, tím tepleji. '
        'Do teplého počasí stačí zhruba R 1 až 2, na zimu a mrazy hledejte karimatku s hodnotou kolem 4 až 6 a víc. Porovnávejte jen hodnoty měřené podle normy <strong>ASTM F3340-18</strong>. '
        'Pak vyberte typ: pěnová je nezničitelná, samonafukovací pohodlná a nafukovací nejlehčí. Nakonec zkontrolujte délku, šířku a hmotnost.</p>'
        '<p>V návodu vysvětlíme, jak se R-hodnota měří a sčítá, jak se liší typy karimatek, jaké rozměry dávají smysl a jak karimatku opravit a skladovat. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů. Pod jednotlivými částmi proto uvidíte karimatky a matrace z naší nabídky.</p>'
    ),
    sections=[
        dict(h2='Proč na karimatce záleží víc, než se zdá',
             html=(
                 '<p>Ve spacáku ztrácíte teplo hlavně směrem dolů. Výplň spacáku pod vámi se vahou těla slehne a skoro neizoluje, zatímco studená zem odvádí teplo vedením. '
                 'Proto lidé v dobrém spacáku na tenké podložce mrznou zespodu a ten samý spacák na teplé karimatce stačí. Teplotní údaje spacáků se navíc měří na figuríně ležící na izolační podložce, s karimatkou tedy počítají.</p>'
                 '<p>Karimatka má dva úkoly: izolovat a poskytnout pohodlí. Ne vždy jdou ruku v ruce. Silná nafukovací matrace může být měkká, ale studená, tenká pěnová karimatka je tvrdá, a přesto rozumně izoluje. '
                 'Proto vybírejte podle R-hodnoty, ne podle tloušťky.</p>'
             ), cat='karimatky-a-matrace', n=4),
        dict(h2='Co je R-hodnota a jak se měří',
             html=(
                 '<p>R-hodnota vyjadřuje tepelný odpor: jak moc karimatka brání prostupu tepla. Dlouho si ji výrobci měřili každý po svém a čísla nebyla srovnatelná. '
                 'Proto výrobci karimatek od roku 2016 společně vyvíjeli jednotnou metodu, která vyšla jako norma <strong>ASTM F3340-18</strong>. Karimatky uváděné na trh od roku 2020 ji používají stále častěji.</p>'
                 '<p>Jak test probíhá:</p>'
                 '<ol><li>Karimatka se vloží mezi dvě desky. Spodní studená deska napodobuje zem, horní je vyhřívaná na 35 °C, tedy zhruba teplotu těla.</li>'
                 '<li>Nafukovací karimatky se nafouknou na předepsaný tlak, aby byl výsledek opakovatelný.</li>'
                 '<li>Měří se, kolik energie je potřeba, aby horní deska udržela teplotu. Z ní se vypočítá R-hodnota.</li></ol>'
                 '<p>Norma je dobrovolná. Nápis ASTM nebo „ASTM F3340“ smí nést jen karimatky skutečně měřené touto metodou. Když výrobce uvádí R-hodnotu bez odkazu na normu, může jít o vlastní, nesrovnatelné měření. '
                 'Po přechodu na novou metodu se některým karimatkám hodnota zvýšila a jiným snížila, i když se karimatka sama nezměnila. Starší recenze a katalogy proto berte s rezervou.</p>'
             )),
        dict(h2='Jakou R-hodnotu potřebujete',
             html=(
                 '<p>Norma neurčuje, při jaké teplotě karimatka stačí. Výrobci dávají přibližná doporučení, která se mezi sebou trochu liší. Orientační přehled:</p>'
                 + T(['Použití', 'Orientační R-hodnota', 'Poznámka'], [
                     ['Léto, teplé noci', 'zhruba 1–2', 'Stačí i pěnová nebo lehká nafukovací'],
                     ['Jaro a podzim', 'zhruba 2–4', 'Noci kolem nuly, v horách volte horní hranici'],
                     ['Zima, mráz, sníh', 'zhruba 4–6 a víc', 'Často kombinace dvou karimatek'],
                 ]) +
                 '<p>Vyšší hodnotu volte, pokud snadno zebete, spíte na sněhu nebo zmrzlé zemi, ve větru nebo pod širákem. Ženy obecně potřebují o něco teplejší karimatku. '
                 'V létě vám vyšší R-hodnota obvykle nevadí: přehřát se na karimatce dá jen tehdy, když je země teplejší než vzduch.</p>'
                 '<p>R-hodnoty se sčítají. Pěnová karimatka s R 2 pod nafukovací s R 3 dá dohromady zhruba R 5. Je to levná cesta k zimnímu spaní a zároveň pojistka, kdyby nafukovací karimatka v noci uchází.</p>'
             )),
        dict(h2='Typy karimatek',
             html=(
                 KARIMATKA_TYPY +
                 '<p><strong>Pěnová karimatka</strong> z pěny s uzavřenými buňkami nenasakuje vodu a nemůže prasknout. Bývá rolovací nebo skládací do „harmoniky“. Je ideální jako sedátko, na krátké výlety a jako ochrana pod nafukovací karimatku. '
                 'Některé mají hliníkovou pokovenou vrstvu, která odráží sálavé teplo.</p>'
                 '<p><strong>Samonafukovací karimatka</strong> obsahuje otevřenou pěnu v neprodyšném obalu. Po otevření ventilu se pěna roztáhne a nasaje vzduch, karimatku pak stačí dofouknout. '
                 'Propíchnutá samonafukovací karimatka pořád trochu izoluje díky pěně uvnitř. Výběr najdete v kategorii <a href="/samonafukovaci-karimatky/">samonafukovací karimatky</a>.</p>'
                 '<p><strong>Nafukovací karimatka</strong> je jen vzduchová komora, často s izolačním vláknem nebo odrazivými fóliemi uvnitř, které zvyšují R-hodnotu. Je nejlehčí a po sbalení má velikost láhve. '
                 'Nafukuje se pumpovacím vakem, ruční pumpou nebo ústy. Vlhkost z dechu ale uvnitř kondenzuje a v mrazu může namrzat, proto výrobci doporučují pumpovací vak.</p>'
             ), cat='samonafukovaci-karimatky', n=4),
        dict(h2='Rozměry: délka, šířka a tloušťka',
             html=(
                 '<p>Standardní karimatky bývají dlouhé kolem 180–185 cm a široké kolem 50 cm. Mnoho modelů se vyrábí i v delší a širší verzi. Při výběru myslete na to, jak spíte:</p>'
                 '<ul><li><strong>Na zádech:</strong> stačí běžná šířka, délka podle vaší výšky.</li>'
                 '<li><strong>Na boku:</strong> ocení silnější karimatku, aby se bok a rameno nedotýkaly země.</li>'
                 '<li><strong>Neklidný spánek:</strong> širší karimatka, z které nesjedete ruce ani lokty.</li></ul>'
                 '<p>Existují i zkrácené karimatky do délky stehen. Pod nohy se pak dá batoh nebo lano. Je to úspora pro ty, kdo hlídají gramy, ale v chladu nohy zebou.</p>'
                 '<p>Tvar se liší podobně jako u spacáků: obdélník je pohodlnější a mumiový tvar, zúžený u nohou, šetří hmotnost. Ve dvoumístném stanu zkontrolujte, že se dvě karimatky vedle sebe vejdou na podlahu.</p>'
             )),
        dict(h2='Hmotnost, sbalení a hluk',
             html=(
                 '<p>Pro turistiku jsou hmotnost a objem po sbalení stejně důležité jako R-hodnota. Nafukovací karimatky vycházejí nejlépe, samonafukovací jsou těžší a pěnové nejobjemnější, i když nejsou nejtěžší. '
                 'Pěnovou karimatku obvykle nesete zvenku na batohu.</p>'
                 '<p>Některé nafukovací karimatky s odrazivými fóliemi při pohybu šustí. Pokud spíte s někým, kdo má lehký spánek, přečtěte si zkušenosti uživatelů konkrétního modelu.</p>'
                 '<p>Povrch karimatky ovlivňuje, jak po ní klouže spacák. Hladké nylonové povrchy jsou kluzké, zdrsněné povrchy nebo protiskluzové tečky pomohou, zvlášť pokud stan stojí ve svahu.</p>'
             )),
        dict(h2='Karimatka, nebo nafukovací matrace do kempu',
             html=(
                 '<p>Na kempování u auta sahá řada lidí po <a href="/nafukovaci-matrace/">nafukovacích matracích</a>. Jsou pohodlné a velké jako postel, ale mají velký objem vzduchu, který se v noci ochlazuje. '
                 'Pokud matrace neobsahuje izolační vrstvu, bude vám za chladné noci zima zespodu, ačkoliv leží vysoko nad zemí.</p>'
                 '<p>Jednoduché řešení je položit na matraci deku, pěnovou karimatku nebo spát ve spacáku s teplou spodní částí. Pro chladnější období jsou lepší široké samonafukovací karimatky, které se vyrábějí i ve verzích pro dva.</p>'
             ), cat='nafukovaci-matrace', n=4),
        dict(h2='Péče, oprava a skladování',
             html=(
                 '<ol><li><strong>Před spaním zkontrolujte podklad.</strong> Odstraňte šišky, kamínky a jehličí. Ve stanu pomůže podložka pod stan.</li>'
                 '<li><strong>Nafukujte pumpovacím vakem.</strong> Do karimatky se pak nedostane vlhkost z dechu.</li>'
                 '<li><strong>Při úniku vzduchu</strong> najděte díru ponořením do vody nebo potřením mýdlovou vodou. Místo vysušte a přelepte záplatou z opravné sady, která bývá v balení.</li>'
                 '<li><strong>Doma skladujte samonafukovací karimatku rozbalenou</strong> s otevřeným ventilem, například pod postelí nebo za skříní. Dlouho stlačená pěna ztrácí schopnost se roztáhnout.</li>'
                 '<li><strong>Nafukovací karimatku</strong> uskladněte volně a suchou, ventil nechte otevřený.</li></ol>'
                 '<p>Karimatku nedávejte k ohni a nenechávejte ji na přímém slunci v rozpáleném autě. Teplo může poškodit lepené švy.</p>'
                 '<p>Do batohu na delší cestu přibalte kromě záplat i malou tubu lepidla, pokud ji výrobce k modelu doporučuje. Uniká-li vzduch ventilem, zkontrolujte, zda v něm není písek nebo zbytek trávy, a ventil vyčistěte. '
                 'Pěnovou karimatku stačí otřít vlhkým hadříkem. Samonafukovací i nafukovací karimatku umyjte vlažnou vodou s trochou jemného mýdla, opláchněte a nechte uschnout s otevřeným ventilem, než ji uložíte.</p>'
             )),
        dict(h2='Nejčastější chyby a jak porovnat nabídky',
             html=(
                 '<ul><li>Vybírat podle tloušťky místo podle R-hodnoty.</li>'
                 '<li>Srovnávat R-hodnoty měřené různými metodami.</li>'
                 '<li>Vzít na zimu jen jednu nafukovací karimatku bez pěnové zálohy.</li>'
                 '<li>Foukat do karimatky ústy v mrazu.</li>'
                 '<li>Skladovat samonafukovací karimatku měsíce sbalenou.</li></ul>'
                 '<p>Při porovnání si zapište R-hodnotu s uvedenou normou, typ, rozměry, hmotnost a objem po sbalení. Stejný model mívá více velikostí, proto kontrolujte variantu. '
                 'Nabídky obchodů porovnáte v kategorii <a href="/karimatky-a-matrace/">karimatky a matrace</a>. Ke karimatce se hodí spacák: pomůže náš návod <a href="/jak-vybrat-spacak/">jak vybrat spacák</a>.</p>'
             ), cat='karimatky-a-matrace', n=4),
    ],
    faq=[
        ('Co je R-hodnota karimatky?',
         '<p>Číslo, které vyjadřuje tepelný odpor karimatky, tedy jak brání úniku tepla do země. Čím vyšší, tím tepleji. Srovnatelná jsou čísla měřená podle normy ASTM F3340-18.</p>'),
        ('Jakou R-hodnotu potřebuji na zimu?',
         '<p>Výrobci pro mráz a sníh obvykle doporučují zhruba R 4 až 6 a víc. Pokud snadno zebete, volte vyšší hodnotu. Často se kombinují dvě karimatky, protože R-hodnoty se sčítají.</p>'),
        ('Sčítají se R-hodnoty dvou karimatek?',
         '<p>Ano. Pěnová karimatka s R 2 a nafukovací s R 3 dají zhruba R 5. Pěnová vespod navíc chrání nafukovací před propíchnutím.</p>'),
        ('Je lepší samonafukovací, nebo nafukovací karimatka?',
         '<p>Samonafukovací je odolnější a při propíchnutí pořád trochu izoluje, ale je těžší a objemnější. Nafukovací je nejlehčí a nejmenší po sbalení, zato citlivější na propíchnutí. Na turistiku spíš nafukovací, do kempu samonafukovací.</p>'),
        ('Proč se nemá karimatka nafukovat ústy?',
         '<p>S dechem se dovnitř dostane vlhkost. Ta kondenzuje, v mrazu může namrzat a dlouhodobě škodí izolačním materiálům uvnitř. Výrobci proto doporučují pumpovací vak nebo pumpu.</p>'),
        ('Jak dlouhá má být karimatka?',
         '<p>Aspoň tak dlouhá jako vy, aby hlava i nohy ležely na izolaci. Standard bývá kolem 180–185 cm, vyšší lidé hledají variantu long. Zkrácené karimatky šetří hmotnost, ale v chladu zebou nohy.</p>'),
        ('Stačí na stanování nafukovací matrace?',
         '<p>V létě ano. V chladu matrace bez izolační vrstvy studí, protože vzduch uvnitř se ochlazuje. Pomůže položit na ni deku nebo pěnovou karimatku.</p>'),
        ('Jak opravit propíchnutou karimatku?',
         '<p>Díru najděte ve vodě nebo mýdlovou vodou podle bublinek. Místo očistěte, vysušte a přelepte záplatou z opravné sady. Ventily a švy u větších poškození nechte opravit v servisu.</p>'),
        ('Jakou karimatku vybrat pro děti?',
         '<p>Dětem stačí kratší karimatka, ale R-hodnotu nepodceňujte, protože děti na studené zemi prochladnou rychle. Praktická je samonafukovací nebo pěnová karimatka, kterou dítě samo nepropíchne a snadno ji sbalí.</p>'),
        ('Jak skladovat samonafukovací karimatku?',
         '<p>Rozbalenou a s otevřeným ventilem, aby pěna zůstala roztažená. Sbalená ji nechávejte jen na cestu.</p>'),
    ],
    cats=['karimatky-a-matrace', 'samonafukovaci-karimatky', 'nafukovaci-matrace'],
    updated='2026-11-19')

# ---------------------------------------------------------------- hardshell-vs-softshell
SHELL_SROVNANI = T(['', 'Hardshell', 'Softshell'], [
    ['Ochrana proti dešti', 'Nepromokavý (membrána, podlepené švy)', 'Odolá přeháňce a sněhu, vytrvalý déšť propustí'],
    ['Ochrana proti větru', 'Úplná', 'Vysoká, u modelů s membránou úplná'],
    ['Prodyšnost', 'Omezená, záleží na membráně', 'Vysoká, hodí se k pohybu'],
    ['Pružnost a pohodlí', 'Tužší, šustí', 'Pružný, tichý, příjemný na těle'],
    ['Hmotnost a sbalení', 'Lehké modely se sbalí do malého vaku', 'Bývá těžší a objemnější'],
    ['Typické použití', 'Déšť, hory, vítr na hřebeni', 'Suché i proměnlivé počasí, aktivní pohyb'],
])

GUIDES['hardshell-vs-softshell'] = dict(
    name='Hardshell vs. softshell',
    h1='Hardshell vs. softshell: rozdíly a kdy co nosit',
    seo_title='Hardshell vs. softshell: rozdíly a kdy co nosit',
    seo_desc='Hardshell chrání před deštěm, softshell je prodyšný a pružný. Rozdíly v membráně, vrstvení oblečení a kdy co obléknout na turistiku, skialpy a do města.',
    intro_html=(
        '<p><strong>Hardshell, nebo softshell?</strong> <strong>Hardshell</strong> je nepromokavá a větruodolná bunda s membránou a podlepenými švy. Chrání před vytrvalým deštěm, ale je tužší a méně prodyšná. '
        '<strong>Softshell</strong> je pružný materiál, který zastaví vítr a odolá krátké přeháňce nebo sněžení, ale hlavně dobře odvádí páru při pohybu. '
        'Zjednodušeně: hardshell na déšť a nepohodu, softshell na aktivitu v suchém nebo proměnlivém počasí. Ideální je mít obojí a kombinovat je ve vrstvách.</p>'
        '<p>Návod vysvětlí, jak funguje vrstvení oblečení, čím se materiály liší, jaké hodnoty sledovat a co obléct na konkrétní aktivitu. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů. U jednotlivých částí uvidíte bundy z naší nabídky.</p>'
    ),
    sections=[
        dict(h2='Hardshell a softshell v jedné tabulce',
             html=(
                 SHELL_SROVNANI +
                 '<p>Slovo „shell“ znamená skořápku, tedy vnější vrstvu oblečení. „Hard“ a „soft“ popisují, jak je materiál na omak tvrdý nebo měkký. Hranice ale není ostrá. '
                 'Existují softshelly s membránou, které jsou téměř nepromokavé, i lehké hardshelly z pružných látek. Při výběru proto čtěte parametry, ne jen název.</p>'
             )),
        dict(h2='Vrstvení oblečení: kam která bunda patří',
             html=(
                 '<p>V přírodě se nevyplácí jedna tlustá bunda, ale několik vrstev, které se dají svlékat a oblékat podle tempa a počasí. Klasický systém má tři vrstvy:</p>'
                 '<ol><li><strong>Základní vrstva</strong> leží na kůži a odvádí pot. Funkční triko nebo <a href="/termopradlo/">termoprádlo</a> ze syntetiky či merina, nikdy bavlna, která vlhkost drží.</li>'
                 '<li><strong>Střední vrstva</strong> hřeje. Nejčastěji <a href="/fleecove-mikiny/">fleecová mikina</a>, tenká péřová nebo syntetická bunda.</li>'
                 '<li><strong>Vnější vrstva</strong> chrání před větrem, deštěm a sněhem. Sem patří hardshell.</li></ol>'
                 '<p>Softshell v tomto systému stojí na pomezí střední a vnější vrstvy. Za suchého, chladného a větrného dne ho nosíte navrch místo hardshellu. Když začne pršet, přehodíte přes něj hardshell. '
                 'Tím se softshell stane střední vrstvou. Proto by měl hardshell mít střih, pod který se softshell nebo mikina vejde.</p>'
             ), cat='fleecove-mikiny', n=4),
        dict(h2='Hardshell: nepromokavá skořápka',
             html=(
                 '<p>Hardshell je postavený na <strong>membráně</strong> nebo zátěru, který nepropustí kapky vody, ale propouští vodní páru. Vrchní látka je ošetřená vodoodpudivou úpravou (DWR), na které voda perlí. '
                 'Švy jsou zevnitř podlepené páskou a zipy chráněné krytem nebo zatavené.</p>'
                 '<p>Podle konstrukce se liší váha i odolnost. <strong>Dvouvrstvé</strong> bundy mají volnou podšívku a hodí se do města a na lehkou turistiku. '
                 '<strong>2,5vrstvé</strong> jsou lehké a sbalitelné do malého vaku, vhodné jako „nouzovka“ do batohu. <strong>Třívrstvé</strong> jsou nejodolnější, určené na hory, skialpy a dlouhý pobyt v nepohodě.</p>'
                 '<p>Odolnost proti vodě se udává ve vodním sloupci v milimetrech, prodyšnost v gramech nebo jako RET. Podrobně tyto jednotky rozebírá průvodce <a href="/vodni-sloupec/">vodní sloupec a prodyšnost</a>. '
                 'Pro výběr si zapamatujte, že ani nejlepší membrána nestihne odvést všechen pot při prudkém stoupání. V hardshellu se při výkonu zpotíte, a proto ho na výstup často sundáte.</p>'
                 '<p>Na co se dívat u hardshellu:</p>'
                 '<ul><li>kapuce, která se dá stáhnout a jde přes helmu, pokud lezete nebo jezdíte na skialpech,</li>'
                 '<li>větrací zipy v podpaží (pit zips),</li>'
                 '<li>délka, která zakryje bedra i s batohem,</li>'
                 '<li>kapsy umístěné výš, aby byly přístupné i s bederním pásem.</li></ul>'
                 '<p>Výběr najdete v kategorii <a href="/nepromokave-bundy/">nepromokavé bundy</a>, k nim se hodí <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>.</p>'
             ), cat='nepromokave-bundy', n=4),
        dict(h2='Softshell: pružný, prodyšný a větruodolný',
             html=(
                 '<p>Softshell je obvykle hustě tkaná pružná látka s příměsí elastanu. Zevnitř bývá zdrsněná nebo počesaná, takže trochu hřeje. Povrch má vodoodpudivou úpravu, na které krátký déšť a sníh sklouznou. '
                 'Vítr zastaví hustota tkaniny, u některých modelů i membrána.</p>'
                 '<p>Rozlišují se dvě skupiny:</p>'
                 '<ul><li><strong>Softshell bez membrány</strong> je nejprodyšnější. Hodí se na běžky, skialpy, svižnou turistiku a lezení, tedy tam, kde se hodně potíte.</li>'
                 '<li><strong>Softshell s membránou</strong> je větruodolný a odolá i silnějšímu dešti, ale dýchá méně. Pro běžné nošení do města a na procházky je univerzálnější, při intenzivním pohybu se v něm zahřejete víc.</li></ul>'
                 '<p>Softshell není nepromokavý ani ten s membránou, protože švy obvykle nejsou podlepené. Za vytrvalého deště se dřív nebo později promočí. '
                 'Softshellové bundy porovnáte v kategorii <a href="/softshellove-bundy/">softshellové bundy</a>. Velmi praktické jsou i <a href="/softshellove-kalhoty/">softshellové kalhoty</a> na túry a skialpy.</p>'
             ), cat='softshellove-bundy', n=4),
        dict(h2='Kdy hardshell a kdy softshell: konkrétní situace',
             html=(
                 T(['Situace', 'Co obléct navrch', 'Proč'], [
                     ['Celodenní déšť na horách', 'Hardshell', 'Jen membrána s podlepenými švy udrží vodu venku'],
                     ['Suchý chladný den, svižná túra', 'Softshell', 'Chrání před větrem a nepřehřívá'],
                     ['Výstup na skialpech', 'Softshell, hardshell v batohu', 'Při stoupání se potíte, na sjezd a hřeben přidáte hardshell'],
                     ['Běžky', 'Tenký softshell', 'Vysoký výdej energie, potřebujete odvod páry'],
                     ['Lyžování na sjezdovce', 'Lyžařská bunda nebo hardshell s vrstvami', 'Málo pohybu na lanovce, sníh a vítr'],
                     ['Kolo v proměnlivém počasí', 'Softshell, při dešti tenký hardshell', 'Vítr z jízdy chladí, déšť přijde náhle'],
                     ['Město, každodenní nošení', 'Softshell s membránou nebo lehký hardshell', 'Krátké přesuny, důležité je pohodlí'],
                 ]) +
                 '<p>V praxi zkušení turisté nesou hardshell vždy v batohu, i když vyrazí v softshellu. Na hřebeni se počasí mění rychle a mokrý softshell ve větru vás rychle prochladí.</p>'
                 '<p>Pomůže jednoduché pravidlo: ráno vyrazte lehce oblečení, s pocitem mírného chladu. Po prvních minutách chůze se zahřejete a nemusíte hned zastavovat a svlékat se. '
                 'Na zastávkách a vrcholech naopak hned přidejte vrstvu, dokud jste ještě teplí. Kdo čeká, až mu bude zima, zahřívá se pak dlouho.</p>'
             )),
        dict(h2='Membrána, impregnace a prodyšnost v praxi',
             html=(
                 '<p>Čísla v katalogu ukazují jen část pravdy. Jak se v bundě budete cítit, ovlivňuje i střih, větrací otvory, to, co máte pod ní, a hlavně stav vodoodpudivé úpravy. '
                 'Když DWR zeslábne, vrchní látka nasákne vodou a membrána přestane odvádět páru. Uvnitř je pak vlhko a zdá se, že bunda „teče“, ačkoliv voda zvenku neprošla.</p>'
                 '<p>Jak udržet bundu funkční:</p>'
                 '<ol><li>Perte ji podle štítku, obvykle v prostředku určeném pro funkční oblečení, bez aviváže.</li>'
                 '<li>Po praní ji podle návodu zahřejte v sušičce na nízkou teplotu nebo opatrně vyžehlete přes látku. Teplo u mnoha úprav obnoví vodoodpudivost.</li>'
                 '<li>Když voda přestane perlit, obnovte <a href="/impregnace/">impregnaci</a> sprejem nebo prostředkem do pračky.</li>'
                 '<li>Nepoužívejte běžný prášek s aviváží, který póry zanáší a zhoršuje odpudivost.</li></ol>'
                 '<p>Softshell se pere stejně šetrně. I u něj se vodoodpudivá úprava časem obnovuje.</p>'
             )),
        dict(h2='Jak vybrat velikost a střih',
             html=(
                 '<p>Hardshell kupujte s ohledem na to, co pod ním budete nosit. Zkoušejte ho přes mikinu nebo softshell a zvedněte ruce nad hlavu: rukávy by neměly vyjet nad zápěstí a lem bundy nad bedra. '
                 'Kapuci zkuste zapnout až nahoru, měla by se otáčet s hlavou a nezakrývat výhled.</p>'
                 '<p>Softshell by měl sedět blíž k tělu, aby dobře odváděl páru, ale nesmí omezovat pohyb. Pružné materiály dovolí užší střih. '
                 'Pokud kupujete obojí, vyzkoušejte softshell a hardshell spolu, abyste věděli, že se pod sebe vejdou. Velikosti se mezi značkami liší, proto se vyplatí podívat i do přehledu <a href="/tabulka-velikosti/">tabulka velikostí</a>.</p>'
             )),
        dict(h2='Nejčastější omyly',
             html=(
                 '<ul><li><strong>„Softshell je nepromokavý.“</strong> Odolá přeháňce, ale ne celodennímu dešti.</li>'
                 '<li><strong>„V nepromokavé bundě se nezpotím.“</strong> Při výkonu tvoří tělo víc páry, než membrána stihne odvést.</li>'
                 '<li><strong>„Vyšší vodní sloupec je vždy lepší.“</strong> Odolnější materiály bývají tužší a méně prodyšné. Do města je zbytečný.</li>'
                 '<li><strong>„Hardshell hřeje.“</strong> Sám nehřeje, jen chrání. Teplo dávají vrstvy pod ním.</li>'
                 '<li><strong>„Bunda propouští, je na vyhození.“</strong> Často stačí vyprat a obnovit impregnaci.</li></ul>'
                 '<p>Když váháte, kterou bundu koupit jako první, rozhodněte podle toho, kde nejčastěji chodíte. Do hor a na dlouhé túry patří první hardshell, na aktivní pohyb v suchém počasí softshell. '
                 'Zimní bundu s výplní najdete pod <a href="/zimni-bundy/">zimními bundami</a>, univerzální modely mezi <a href="/sportovni-bundy/">sportovními bundami</a>.</p>'
             ), cat='sportovni-bundy', n=4),
    ],
    faq=[
        ('Jaký je rozdíl mezi hardshellem a softshellem?',
         '<p>Hardshell je nepromokavá bunda s membránou a podlepenými švy, chrání před vytrvalým deštěm. Softshell je pružný a prodyšný, zastaví vítr a krátkou přeháňku, ale vytrvalý déšť propustí.</p>'),
        ('Je softshell nepromokavý?',
         '<p>Ne. Odolá krátkému dešti a sněžení díky hustotě tkaniny a vodoodpudivé úpravě. Ani softshell s membránou nemá obvykle podlepené švy, takže za dlouhého deště promokne.</p>'),
        ('Může hardshell nahradit zimní bundu?',
         '<p>Jen ve vrstvách. Hardshell sám nehřeje, teplo musí dát mikina nebo zateplená bunda pod ním. Výhodou je, že vrstvy můžete měnit podle počasí.</p>'),
        ('Co si vzít na turistiku, hardshell, nebo softshell?',
         '<p>Za suchého počasí softshell na sebe a hardshell do batohu. Na horách se počasí rychle mění a mokrý softshell ve větru studí. Při předpovědi deště jděte rovnou v hardshellu.</p>'),
        ('Proč se v nepromokavé bundě potím?',
         '<p>Membrána odvádí páru jen určitou rychlostí. Při rychlé chůzi do kopce tělo vyprodukuje víc vlhkosti, než stihne odejít. Pomůže zpomalit, otevřít větrací zipy a vyměnit vrstvy pod bundou.</p>'),
        ('Jak poznám dobrý hardshell?',
         '<p>Má membránu s uvedenou hodnotou vodního sloupce a prodyšnosti, podlepené švy, nastavitelnou kapuci a kryté nebo vodotěsné zipy. Na hory se hodí třívrstvé provedení a větrací zipy v podpaží.</p>'),
        ('Softshell s membránou, nebo bez ní?',
         '<p>Bez membrány je prodyšnější a hodí se na intenzivní sporty jako běžky a skialpy. S membránou je větruodolnější a univerzálnější do města a na pomalejší túry, ale při výkonu se v něm více zpotíte.</p>'),
        ('Jak prát hardshell a softshell?',
         '<p>Podle štítku, v prostředku pro funkční oblečení a bez aviváže. Pokud to výrobce dovoluje, bundu po praní zahřejte v sušičce na nízkou teplotu. Když voda přestane perlit, obnovte impregnaci.</p>'),
        ('Potřebuje hardshell i dítě?',
         '<p>Na výlety do hor a do deště ano, stačí ale jednodušší dvouvrstvá nebo 2,5vrstvá bunda. Děti rychle rostou, proto volte střih s rezervou na mikinu pod ní a kontrolujte délku rukávů. Na hraní venku za suchého počasí poslouží softshell.</p>'),
        ('Proč bunda po čase „teče“?',
         '<p>Často jde o vodoodpudivou úpravu, která zeslábla. Vrchní látka nasákne a membrána přestane odvádět páru, uvnitř pak vzniká vlhko. Pomůže vyprání a nová impregnace.</p>'),
    ],
    cats=['nepromokave-bundy', 'softshellove-bundy', 'softshellove-kalhoty', 'nepromokave-kalhoty'],
    updated='2026-11-19')
