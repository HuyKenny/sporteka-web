"""Guides wave 5e (2026-11-19): jak-vybrat-bezecke-boty, jak-vybrat-tenisovou-raketu, jak-vybrat-badmintonovou-raketu,
velikosti-fotbalovych-micu.

Sources used for the facts:
- Running shoes: ASICS "Ensuring the correct fit for running shoes" (half to a full thumb's width in front of the toes,
  try on in the late afternoon / evening, with the socks you run in); Kuru Footwear fit guide (about a thumb's width,
  feet swell during the day and during runs); Healthline "How a running shoe should fit"; Foundation Podiatry
  "Running shoes" (drop = height difference between rearfoot and forefoot in mm, 0 to about 12 mm, a sudden change
  from high to low drop matters more than the drop itself, replacement about 400-600 km, possibly up to 800 km);
  ASICS "How often do you need to replace running shoes" and retailer guides (300-500 miles = about 500-800 km,
  surface and body weight change it, wear signs are the real signal).
- Tennis: ITF Rules of Tennis, Appendix II (frame max 73.7 cm / 29.0 in long and 31.7 cm / 12.5 in wide, hitting
  surface max 39.4 x 29.2 cm, no energy source in the racket); Britannica (29 in limit for pro play 1979, for all
  play 2000); tenniscompanion.org, Tennis Warehouse and Wilson (head size categories differ by brand: midsize about
  85-97 sq in, midplus about 98-105, oversize from about 105-107; smaller head = control, larger = power and
  forgiveness); typical unstrung weight 255-340 g (no ITF weight rule); grip L0-L5 = 4 in to 4 5/8 in, L2-L3 most
  common for adults, measure from the middle crease of the palm to the tip of the ring finger (tennisexpress.com,
  tennisracquets.com, utrsports.net); junior racquet charts (centralsports.co.uk, tenniscompanion.org: 19/21/23/25/26 in,
  height matters more than age, head just above the floor when held at the side, 27 in adult standard, juniors
  mostly 4 in / L0 grip, 26 in step before adult size).
- Badminton: BWF Laws of Badminton, Law 4.1 (frame max 680 mm long, 230 mm wide); Yonex weight classes as reproduced
  by retailers (2U 90-94.9 g, 3U 85-89.9 g, 4U 80-84.9 g, 5U 75-79.9 g, lower number = heavier) and grip G4/G5/G6
  (higher number = thinner, G4 and G5 most common, a grip can be built up with an overgrip but not reduced); balance
  point measured in mm from the end of the handle, about < 285 mm head light, 285-295 even, > 295 head heavy
  (thresholds differ between sources, some put head heavy over 300 mm), stringing raises and a grip lowers the
  balance point; beginner tension about 20-22 lbs, advanced 26 lbs and more (Central Sports, Badminton HQ,
  Smash UK, Stiga buying guides).
- Footballs: IFAB Laws of the Game, Law 2 as published by The FA (size 5: 68-70 cm, 410-450 g at the start of the
  match, pressure 0.6-1.1 atm at sea level); Nike soccer ball sizing chart (size 3: 58.5-61 cm, size 4: 63.5-66 cm);
  Decathlon product pages (size 4 350-390 g, size 3 weight 290-335 g, so given as a range only); Czech tournament
  rules Pohár mládeže 2025/26 (U8: size 3, U12: size 4, 290-390 g, 63-66 cm); FC Hradec Králové methodology (size 3,
  or a lightweight size 4); FA Futsal Law 2 and older FIFA Futsal Laws (62-64 cm, 400-440 g, first rebound 50-65 cm
  when dropped from 2 m); FIFA "Quality marks explained" and "FIFA Quality Programme for Footballs" (FIFA Quality Pro,
  FIFA Quality, FIFA Basic which replaced IMS; tests for weight, circumference, roundness, rebound, water absorption,
  pressure loss, shape and size retention; balls in international FIFA/confederation matches must bear a mark).
Left out because not verified or sources disagree: the 1/8 inch per balance point in tennis, exact mm values of
tennis and badminton grips, whether Yonex U classes are strung or unstrung weight, an official FAČR table of ball
sizes by category, exact size 3 weight from the Laws, exact FIFA test thresholds, a fixed replacement mileage for
trail shoes, cushioning stack heights.
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- jak-vybrat-bezecke-boty
RUN_TYPES = T(['Typ boty', 'Povrch', 'Podrážka', 'Pro koho'], [
    ['Silniční', 'Asfalt, chodník, dráha, pás', 'Hladší, plošší, s hustším vzorkem', 'Většina městských běžců'],
    ['Trailová', 'Lesní cesty, kořeny, kamení, bláto', 'Hluboké výstupky, tužší a odolnější materiál', 'Běh v terénu a v horách'],
    ['Hybridní (road to trail)', 'Šotolina, parkové a polní cesty', 'Nižší výstupky, které nevadí ani na asfaltu', 'Kdo střídá město a lehký terén'],
    ['Závodní', 'Asfalt, dráha', 'Lehká, často s tuhou deskou v mezipodešvi', 'Rychlé tréninky a závody'],
])

GUIDES['jak-vybrat-bezecke-boty'] = dict(
    name='Jak vybrat běžecké boty',
    h1='Jak vybrat běžecké boty: povrch, tlumení, drop a správná velikost',
    seo_title='Jak vybrat běžecké boty: povrch, tlumení a velikost',
    seo_desc='Silniční, nebo trailové? Kolik tlumení a jaký drop? Jak poznat správnou velikost a kdy boty vyměnit. Praktický návod k výběru běžeckých bot krok za krokem.',
    intro_html=(
        '<p><strong>Jak vybrat běžecké boty?</strong> Začněte povrchem, po kterém poběžíte. Na asfalt a chodníky patří silniční boty, do lesa a hor trailové s hlubším vzorkem. '
        'Pak zvolte míru tlumení podle toho, kolik a jak dlouho běháte, a podívejte se na drop, tedy rozdíl výšky pod patou a pod špičkou. '
        'Nakonec rozhoduje padnoutí: před nejdelším prstem má zůstat zhruba půl až celá šířka palce volného místa a pata nesmí v botě klouzat. '
        'Boty zkoušejte odpoledne a v ponožkách, ve kterých běháte.</p>'
        '<p>V článku projdeme typy bot podle povrchu, tlumení, drop, rozdíl mezi neutrální a stabilní obuví, výběr velikosti a to, kdy je čas na nový pár. '
        'Na konci najdete nejčastější chyby, které při nákupu vídáme. Sporteka sama nic neprodává, jen srovnává nabídky českých e-shopů, takže pod jednotlivými částmi uvidíte konkrétní boty k porovnání.</p>'
    ),
    sections=[
        dict(h2='Krok 1: Kde budete běhat',
             html=(
                 '<p>Povrch rozhoduje o podrážce víc než cokoli jiného. Bota stavěná na asfalt má hladší, plošší podešev, která se po tvrdém podkladu dobře odvaluje a pomaleji se ojíždí. '
                 'V blátě nebo na mokrých kořenech ale klouže. Trailová bota má naopak výrazné výstupky, které se zakousnou do měkkého terénu, jenže na asfaltu se rychleji obrušují a působí hrbolatě.</p>'
                 + RUN_TYPES +
                 '<p>Kdo běhá převážně po městě a jen občas zajede do parku, vystačí se silniční botou. Pokud polovinu tras tvoří lesní cesty a šotolina, zvažte hybridní model. '
                 'Pro skutečný terén s kamením, kořeny a strmými seběhy si pořiďte trailovky. Mnoho běžců má časem dva páry a střídá je podle trasy.</p>'
                 '<p>Nabídku bot na tvrdý povrch najdete v kategorii <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, celé spektrum včetně závodních modelů v kategorii <a href="/bezecka-obuv/">běžecké boty</a>.</p>'
             ), cat='silnicni-bezecke-boty', n=4),
        dict(h2='Trailové boty: na co se dívat navíc',
             html=(
                 '<p>U běhu v terénu sledujte několik věcí, které na silnici nehrají roli:</p>'
                 '<ul><li><strong>Hloubka a tvar výstupků.</strong> Hlubší a řidčeji rozmístěné výstupky se lépe čistí od bláta a drží v měkkém terénu. Nižší a hustší vzorek sedí na suché, tvrdé lesní cesty.</li>'
                 '<li><strong>Gumová směs.</strong> Lepivější směs drží na mokré skále, tvrdší vydrží déle. Výrobci často uvádějí vlastní značení podrážky, například Vibram nebo Contagrip.</li>'
                 '<li><strong>Ochrana prstů a chodidla.</strong> Zesílená špička chrání před kopnutím do kamene. Některé modely mají v mezipodešvi tenkou ochrannou destičku proti ostrým kamenům.</li>'
                 '<li><strong>Membrána.</strong> Verze s membránou (často označená GTX) se hodí do zimy, mokré trávy a na krátké loužičky. V létě se v ní noha víc potí a když voda nateče shora, pomaleji schne.</li>'
                 '<li><strong>Pevnost svršku a fixace paty.</strong> Při seběhu noha nesmí jezdit dopředu. Pevnější pata a dobře nastavitelné šněrování tomu brání.</li></ul>'
                 '<p>Trailové boty bývají o něco těžší a tužší než silniční. Na první výběhy volte spíš kratší trasu, než si nohy na jiný pocit zvyknou. '
                 'Modely do terénu porovnáte v kategorii <a href="/trailove-boty/">trailové běžecké boty</a>, na delší výběhy se hodí i <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>.</p>'
             ), cat='trailove-boty', n=4),
        dict(h2='Krok 2: Kolik tlumení potřebujete',
             html=(
                 '<p>Tlumení zajišťuje mezipodešev z pěny. Výrobci ji dělají v různé tloušťce a tvrdosti a každý ji pojmenovává po svém. Pro orientaci stačí tři skupiny:</p>'
                 '<ol><li><strong>Minimální tlumení.</strong> Tenká podrážka, výrazný kontakt se zemí. Hodí se pro zkušené běžce, na krátké tréninky, rovinky a posilování chodidla. Sem patří i barefoot obuv.</li>'
                 '<li><strong>Střední tlumení.</strong> Univerzální volba na denní běhání a tempové tréninky. Bota je pružná, ale cit pro povrch zůstává.</li>'
                 '<li><strong>Maximální tlumení.</strong> Vysoká a měkká mezipodešev na dlouhé běhy a regenerační kilometry. Mezi známé příklady patří modely značky <a href="/znacka/hoka/">Hoka</a>.</li></ol>'
                 '<p>Víc pěny neznamená automaticky lepší botu. Vysoká a měkká podrážka působí na krátkém běhu příjemně, ale na nerovném terénu je méně stabilní a někomu nevyhovuje pocit „plavání“. '
                 'Začátečníkům, kteří běhají po asfaltu, obvykle sedí střední až vyšší tlumení. Rozhodující je, jak se vám v botě běží, ne číslo v popisu.</p>'
                 '<p>Pokud teprve začínáte, přečtěte si i článek <a href="/bezecka-abeceda/">běžecká abeceda</a>. Lepší technika kroku pomůže v jakékoli botě.</p>'
             )),
        dict(h2='Krok 3: Drop a co znamená v praxi',
             html=(
                 '<p><strong>Drop</strong> je rozdíl mezi výškou podrážky pod patou a pod přední částí chodidla, uvádí se v milimetrech. Běžně se pohybuje od 0 mm, kdy je pata ve stejné výšce jako špička, do zhruba 12 mm. '
                 'Vyšší drop znamená, že pata je výš. Takové boty bývají pohodlné pro běžce, kteří dopadají na patu, a méně zatěžují lýtka a Achillovu šlachu. Nižší drop podporuje dopad na střed chodidla a víc zapojuje lýtka.</p>'
                 '<ul><li><strong>8–12 mm:</strong> klasické tréninkové boty, nejběžnější volba.</li>'
                 '<li><strong>4–8 mm:</strong> přechodová skupina, častá u trailových bot.</li>'
                 '<li><strong>0–4 mm:</strong> nízký až nulový drop, typický pro minimalistické modely a některé značky, jako je Altra.</li></ul>'
                 '<p>Důležitější než konkrétní číslo je změna. Podologové upozorňují, že náhlý přechod z vysokého dropu na nízký zatíží lýtka a šlachy víc, než na co jsou zvyklé. '
                 'Když chcete drop snížit, střídejte zpočátku nový pár se starým a prodlužujte vzdálenost postupně, třeba několik týdnů. '
                 'Pokud střídáte více párů najednou, volte je s podobným dropem, aby se tělo nemuselo přizpůsobovat při každém výběhu.</p>'
             )),
        dict(h2='Krok 4: Neutrální, nebo stabilní bota',
             html=(
                 '<p>Při každém kroku se chodidlo po dopadu přirozeně stáčí lehce dovnitř. Tomu pohybu se říká pronace a do určité míry tlumí náraz. '
                 'Neutrální boty pohybu chodidla nijak nebrání. Stabilní (podpůrné) boty mají na vnitřní straně tužší pěnu, zvýšený okraj nebo vodicí prvky, které nadměrné stáčení omezují.</p>'
                 '<p>Jak poznat, co potřebujete:</p>'
                 '<ol><li>Podívejte se na podrážku starých bot. Výrazně ojetá vnitřní hrana pod palcem může naznačovat větší pronaci.</li>'
                 '<li>Nechte si natočit běh na páse zezadu. Mnoho specializovaných prodejen to nabízí zdarma.</li>'
                 '<li>Zkuste obě varianty. Když se vám ve stabilní botě běží příjemněji a nic netlačí, je to dobré znamení. Když ji vnímáte jako tvrdou a nepřirozenou, vraťte se k neutrální.</li></ol>'
                 '<p>Většině běžců vyhovuje neutrální bota. Podrobně celé téma vysvětluje průvodce <a href="/pronace-a-supinace/">pronace a supinace</a>. '
                 'Botu nekupujte jako léčbu bolesti. Opakovaná bolest kolen, holení nebo chodidel patří k lékaři nebo fyzioterapeutovi, ne do prodejny obuvi.</p>'
             ), cat='bezecka-obuv', n=4),
        dict(h2='Krok 5: Velikost a padnoutí',
             html=(
                 '<p>Většina běžců, kteří si stěžují na černé nehty a otlaky, má boty příliš malé. Běžecká bota se nevybírá „na těsno“ jako společenská obuv. Při zkoušení postupujte takto:</p>'
                 '<ol><li><strong>Zkoušejte odpoledne nebo večer.</strong> Chodidla během dne a při běhu mírně otékají.</li>'
                 '<li><strong>Vezměte si běžecké ponožky.</strong> Tlustá bavlněná ponožka změní velikost víc, než by se zdálo.</li>'
                 '<li><strong>Změřte délku chodidla.</strong> Postavte se patou ke zdi na papír, označte nejdelší prst a změřte vzdálenost v centimetrech. Měřte obě nohy, rozhoduje ta delší.</li>'
                 '<li><strong>Nechte místo vpředu.</strong> ASICS doporučuje mezi prsty a špičkou boty půl až celou šířku palce. V praxi to bývá kolem jednoho centimetru.</li>'
                 '<li><strong>Zkontrolujte šířku.</strong> Malíček ani kloub palce nesmí narážet do bočnice. Některé modely se vyrábějí v široké verzi.</li>'
                 '<li><strong>Zkuste chůzi z kopce nebo seskok.</strong> Prsty nesmí narazit do špičky a pata nesmí klouzat nahoru a dolů.</li></ol>'
                 '<p>Velikosti se mezi značkami liší, a to i o půl čísla. Proto nekupujte naslepo podle EU velikosti z jiného výrobce. Porovnejte délku chodidla v centimetrech s tabulkou dané značky. '
                 'Převody mezi EU, UK a US čísly a postup měření najdete v článku <a href="/tabulka-velikosti/">tabulka velikostí</a>. Vhodné ponožky vyberete v kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>'
             ), cat='sportovni-ponozky', n=4),
        dict(h2='Dámské, pánské a dětské boty',
             html=(
                 '<p>Dámské verze běžeckých bot nejsou jen pánské boty v jiné barvě. Obvykle mají užší patu a jinou šířku v přední části a začínají menšími velikostmi. '
                 'Když má žena širší chodidlo, může jí lépe sedět pánský model, a naopak muž s úzkou nohou si může vybrat dámskou verzi. Rozhoduje tvar, ne nápis. '
                 'Výběr porovnáte třeba v nabídce <a href="/damske-silnicni-bezecke-boty/">dámských silničních běžeckých bot</a>.</p>'
                 '<p>U dětí noha rychle roste, takže je dobré délku chodidla přeměřit každých pár měsíců. Dětská bota má mít vpředu rezervu, ale nesmí být o dvě čísla větší, aby v ní dítě nezakopávalo. '
                 'Modely pro malé běžce najdete v nabídce <a href="/detske-bezecke-boty/">dětských běžeckých bot</a>.</p>'
             )),
        dict(h2='Kdy boty vyměnit',
             html=(
                 '<p>Mezipodešev se během kilometrů postupně stlačuje a ztrácí pružnost, i když svršek vypadá jako nový. Běžně uváděná životnost je přibližně 500 až 800 km. '
                 'Lehčí běžec na rovném asfaltu se dostane k horní hranici, těžší běžec v terénu spíš k dolní. Kilometry berte jako vodítko, skutečný stav poznáte podle příznaků:</p>'
                 '<ul><li>podrážka je v místě dopadu ojetá až na pěnu nebo vzorek zmizel,</li>'
                 '<li>mezipodešev má hluboké vrásky a po stlačení palcem nepruží,</li>'
                 '<li>bota položená na stole se naklání na jednu stranu,</li>'
                 '<li>pata uvnitř je prodřená a noha v ní ztrácí oporu,</li>'
                 '<li>po běhu cítíte únavu nebo tlak tam, kde jste dřív nic nevnímali.</li></ul>'
                 '<p>Životnost prodloužíte, když boty používáte jen na běh, ne na celodenní nošení. Pomáhá i střídání dvou párů, aby pěna mezi tréninky stihla vyschnout a vrátit se do tvaru. '
                 'Mokré boty sušte volně při pokojové teplotě s vycpávkou z novin, ne na topení. Tkaničky a vložky pro výměnu najdete v kategorii <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>'
             ), cat='doplnky-k-obuvi', n=4),
        dict(h2='Nejčastější chyby při výběru',
             html=(
                 '<ol><li><strong>Výběr podle barvy nebo podle toho, co nosí kamarád.</strong> Každá noha je jiná a model, který jinému sedí, vám může tlačit.</li>'
                 '<li><strong>Příliš malá velikost.</strong> Bota má na noze sedět pevně v patě a nártu, ale prsty potřebují prostor.</li>'
                 '<li><strong>Trailovky na asfalt.</strong> Výstupky se na tvrdém povrchu rychle sjedou a bota nepůsobí plynule.</li>'
                 '<li><strong>Závodní karbonová bota na každodenní trénink.</strong> Je lehká a rychlá, ale méně odolná a pro začátečníka zbytečně specifická.</li>'
                 '<li><strong>Prudká změna dropu nebo tlumení.</strong> Na nový typ bot si zvykejte postupně.</li>'
                 '<li><strong>Běhání v ojetých botách.</strong> Bota vypadá dobře, ale pěna už netlumí.</li>'
                 '<li><strong>Nákup bez porovnání.</strong> Stejný model se u různých obchodů liší cenou i dostupností velikostí, proto se vyplatí nabídky srovnat.</li></ol>'
                 '<p>Pokud plánujete běhat i v chladu a tmě, podívejte se na článek <a href="/zaciname-behat-v-zime/">začínáme běhat v zimě</a>. '
                 'Konkrétní modely známých značek najdete na stránkách <a href="/bezecke-boty-asics/">běžecké boty Asics</a> nebo <a href="/salomon-bezecke-boty/">běžecké boty Salomon</a>.</p>'
             ), cat='bezecka-obuv', n=4),
    ],
    faq=[
        ('Jak poznám, že mám správnou velikost běžeckých bot?',
         '<p>Před nejdelším prstem zůstane přibližně půl až celá šířka palce, pata při chůzi neklouže a nic netlačí do stran. Zkoušejte je odpoledne a v běžeckých ponožkách, kdy je noha mírně oteklá jako při běhu.</p>'),
        ('Mají být běžecké boty o číslo větší?',
         '<p>Ne vždy o celé číslo, ale většinou o něco delší než vaše vycházková obuv. Rozhoduje délka chodidla v centimetrech plus zhruba centimetr rezervy, porovnaná s tabulkou konkrétní značky.</p>'),
        ('Jaký je rozdíl mezi silničními a trailovými botami?',
         '<p>Silniční mají hladší a lehčí podrážku pro asfalt a chodníky. Trailové mají hlubší výstupky, odolnější svršek a často zesílenou špičku pro lesní cesty, kořeny a kamení.</p>'),
        ('Co je drop u běžeckých bot?',
         '<p>Rozdíl výšky podrážky pod patou a pod špičkou v milimetrech. Běžně bývá 0 až 12 mm. Při přechodu na nižší drop postupujte pozvolna, aby si lýtka a šlachy zvykly.</p>'),
        ('Potřebuji stabilní boty?',
         '<p>Většině běžců vyhovují neutrální boty. Stabilní model může pomoct lidem s výraznější pronací, kterým v něm běh připadá pohodlnější. Bolest při běhu ale řešte s lékařem nebo fyzioterapeutem.</p>'),
        ('Kolik kilometrů vydrží běžecké boty?',
         '<p>Obvykle se uvádí 500 až 800 km. Záleží na hmotnosti běžce, povrchu a modelu. Spolehlivější je sledovat ojetí podrážky, zvrásnění pěny a to, jak se vám v botách běží.</p>'),
        ('Mohu v běžeckých botách chodit i do fitka?',
         '<p>Na kardio stroje ano. Na dřepy a zvedání činek se vysoká měkká podrážka nehodí, protože je na ní noha méně stabilní. Na silový trénink je vhodnější tréninková obuv s plochou podešví.</p>'),
        ('Vyplatí se boty s membránou?',
         '<p>Do zimy, rosy a bláta ano. V létě se v nich noha víc potí, a když voda nateče přes horní okraj, schnou pomaleji. Na běžné běhání v suchu stačí prodyšný síťovaný svršek.</p>'),
        ('Jak dlouho trvá, než si boty zaběhnu?',
         '<p>Dobře padnoucí běžecká bota by měla být pohodlná od začátku. První výběhy dejte kratší, abyste ověřili, že nic netlačí. Bota, která v obchodě tlačí, se většinou „nerozchodí“.</p>'),
    ],
    cats=['bezecka-obuv', 'silnicni-bezecke-boty', 'trailove-boty'],
    updated='2026-11-19',
)

# ---------------------------------------------------------------- jak-vybrat-tenisovou-raketu
TEN_HEAD = T(['Velikost hlavy', 'Přibližně (sq in)', 'Co nabízí', 'Pro koho'], [
    ['Midsize', '85–97', 'Kontrola, přesnost, menší sweet spot', 'Pokročilí hráči s plným švihem'],
    ['Midplus', '98–105', 'Kompromis mezi silou a kontrolou', 'Většina rekreačních hráčů'],
    ['Oversize', 'od cca 105–107', 'Síla zadarmo, velká tolerance chyb', 'Začátečníci, hráči s kratším švihem'],
])

TEN_GRIP = T(['Evropské značení', 'Americké značení (palce)', 'Obvykle pro'], [
    ['L0 (0)', '4', 'Děti, juniorské rakety'],
    ['L1 (1)', '4 1/8', 'Menší dlaně, juniorské a dámské rakety'],
    ['L2 (2)', '4 1/4', 'Častá velikost u žen i mužů'],
    ['L3 (3)', '4 3/8', 'Častá velikost u mužů'],
    ['L4 (4)', '4 1/2', 'Větší dlaně'],
    ['L5 (5)', '4 5/8', 'Velké dlaně'],
])

TEN_JUNIOR = T(['Délka rakety', 'Orientační věk', 'Poznámka'], [
    ['19" (cca 48 cm)', 'do 4 let', 'První seznámení s tenisem, pěnové míčky'],
    ['21" (cca 53 cm)', '4–6 let', 'Měkčí míče pro malé hřiště'],
    ['23" (cca 58 cm)', '6–8 let', 'Často první raketa na kurt'],
    ['25" (cca 64 cm)', '8–10 let', 'Přechod na větší hřiště'],
    ['26" (cca 66 cm)', '10–12 let', 'Poslední krok před dospělou raketou'],
    ['27" (cca 69 cm)', 'od 12 let a dospělí', 'Standardní délka dospělých raket'],
])

GUIDES['jak-vybrat-tenisovou-raketu'] = dict(
    name='Jak vybrat tenisovou raketu',
    h1='Jak vybrat tenisovou raketu: velikost hlavy, váha, vyvážení a grip',
    seo_title='Jak vybrat tenisovou raketu: hlava, váha a grip',
    seo_desc='Velikost hlavy, hmotnost, vyvážení, vzor výpletu a správný grip. Jak změřit velikost gripu a jakou délku rakety zvolit pro dítě podle věku a výšky.',
    intro_html=(
        '<p><strong>Jak vybrat tenisovou raketu?</strong> Začátečník a rekreační hráč obvykle nejlépe pochodí s raketou s větší hlavou (zhruba 100 až 110 čtverečních palců) a s hmotností kolem 260 až 290 g bez výpletu. '
        'Taková raketa odpustí nepřesný zásah a nevyžaduje velký švih. Pokročilí hráči volí menší hlavu a těžší rám kvůli kontrole. '
        'Velikost gripu změříte pravítkem od střední rýhy v dlani ke špičce prsteníčku. U dětí se délka rakety vybírá podle výšky, ne jen podle věku.</p>'
        '<p>V článku projdeme všechny parametry, které výrobci uvádějí: velikost hlavy, hmotnost, vyvážení, tuhost rámu, vzor výpletu a grip. '
        'Přidáme tabulku dětských délek a postup, jak raketu otestovat. Sporteka nic neprodává, jen porovnává nabídky českých obchodů. Pod částmi článku proto uvidíte rakety a tenisovou obuv k porovnání.</p>'
    ),
    sections=[
        dict(h2='Velikost hlavy: síla, nebo kontrola',
             html=(
                 '<p>Velikost hlavy znamená plochu výpletu. Výrobci ji uvádějí ve čtverečních palcích (sq in), někdy i v cm². Hranice mezi kategoriemi se u jednotlivých značek trochu liší, orientačně platí:</p>'
                 + TEN_HEAD +
                 '<p>Větší hlava má větší „sweet spot“, tedy místo, kde míček odskočí rychle a raketa se v ruce nechvěje. Výplet se víc prohne a vrátí míčku víc energie. '
                 'Menší hlava je přesnější a lépe se s ní mění směr úderu, ale nepřesný zásah víc potrestá. Nejvíc rozšířené jsou rakety se 100 sq in, které sedí široké skupině hráčů.</p>'
                 '<p>Pravidla ITF omezují celkovou délku rámu na 73,7 cm (29 palců) a šířku na 31,7 cm. Hrací plocha výpletu smí měřit nejvýš 39,4 × 29,2 cm. '
                 'Do těchto mezí se vejdou všechny rakety, které běžně koupíte. Nabídku dospělých i juniorských raket najdete v kategorii <a href="/tenisove-rakety/">tenisové rakety</a>.</p>'
             ), cat='tenisove-rakety', n=4),
        dict(h2='Hmotnost: proč lehčí neznamená vždy lepší',
             html=(
                 '<p>Hmotnost se obvykle uvádí bez výpletu (unstrung). Výplet, omotávka a tlumítko přidají zhruba několik desítek gramů. Pravidla hmotnost neomezují, běžné rakety pro dospělé váží přibližně 255 až 340 g.</p>'
                 '<ul><li><strong>Do 270 g:</strong> lehké rakety pro začátečníky, juniory přecházející na plnou délku a hráče s pomalejším švihem.</li>'
                 '<li><strong>270–300 g:</strong> nejširší skupina pro rekreační a mírně pokročilé hráče.</li>'
                 '<li><strong>Nad 300 g:</strong> těžší rámy pro hráče s rychlým a plným švihem, kteří chtějí stabilitu a kontrolu.</li></ul>'
                 '<p>Lehká raketa se snadno ovládá, ale při zásahu tvrdého míče se víc kroutí a do ruky přenáší víc otřesů. Těžší raketa je stabilnější a míček „protlačí“ sama, jen s ní musíte umět zrychlit. '
                 'Když zvolíte příliš těžký rám, na konci zápasu budete pozdě na úder. Při příliš lehkém rámu zase budete mít nutkání švihat víc z ruky a zápěstí.</p>'
                 '<p>Hráči, kteří mají potíže s loktem nebo ramenem, by měli raketu vybírat spíš s trenérem a zdravotní potíže řešit s lékařem nebo fyzioterapeutem. Žádná raketa sama bolest neodstraní.</p>'
             )),
        dict(h2='Vyvážení a tuhost rámu',
             html=(
                 '<p><strong>Vyvážení (balance)</strong> říká, kde leží těžiště rakety. Měří se od konce rukojeti a uvádí se v milimetrech nebo v bodech. '
                 'Raketa může být vyvážená do hlavy (head heavy), vyrovnaná (even) nebo do rukojeti (head light).</p>'
                 '<ul><li><strong>Do hlavy:</strong> typické pro lehčí rakety. Hlava při švihu přidá sílu, raketa ale reaguje pomaleji u sítě.</li>'
                 '<li><strong>Vyrovnané:</strong> univerzální volba.</li>'
                 '<li><strong>Do rukojeti:</strong> typické pro těžší rakety. Dobře se s nimi manévruje a rychle reagují při volejích.</li></ul>'
                 '<p>Lehká a do hlavy vyvážená raketa a těžká raketa vyvážená do rukojeti se mohou v ruce chovat podobně. Proto parametry nehodnoťte odděleně. Vyvážení se změní i omotávkou, výpletem nebo olůvkem.</p>'
                 '<p><strong>Tuhost (stiffness)</strong> se uvádí jako číslo RA, obvykle v rozmezí od nízkých šedesátek po sedmdesátky. Tužší rám vrací víc energie a míček letí rychleji, ale do ruky přenáší víc otřesů. '
                 'Pružnější rám je komfortnější a dává lepší cit, zato vyžaduje rychlejší švih. Začátečníkům obvykle vyhovuje střední tuhost.</p>'
             )),
        dict(h2='Vzor výpletu: 16×19, nebo 18×20',
             html=(
                 '<p>Vzor výpletu udává počet podélných a příčných strun. U dospělých raket jsou nejčastější dva:</p>'
                 '<ul><li><strong>16×19 (otevřený vzor):</strong> struny mají mezi sebou víc místa, víc se pohybují a pomáhají míčku dát rotaci. Výplet se ale rychleji opotřebuje.</li>'
                 '<li><strong>18×20 (hustý vzor):</strong> kontrolovanější a plošší let míčku, delší životnost výpletu, menší „dar“ síly i rotace zadarmo.</li></ul>'
                 '<p>Rekreačnímu hráči obvykle vyhovuje otevřený vzor. Hustý vzor ocení hlavně hráči, kteří sami generují rychlost a trhají struny.</p>'
                 '<p>Stejně důležitý jako vzor je samotný výplet a jeho napětí. Většina raket se prodává už vypletená z výroby. Pokud hrajete pravidelně, nechte si raketu přeplést ve sportovní prodejně nebo tenisovém klubu podle napětí doporučeného na rámu. '
                 'Nižší napětí znamená víc síly a komfortu, vyšší víc kontroly. Výplet ztrácí napětí i ve skříni, proto se po delší pauze vyplatí přeplétání.</p>'
             )),
        dict(h2='Jak změřit velikost gripu',
             html=(
                 '<p>Grip je obvod rukojeti. V Evropě se značí L0 až L5 (nebo jen 0 až 5), v USA v palcích. Obě značení si odpovídají takto:</p>'
                 + TEN_GRIP +
                 '<p>Postup měření:</p>'
                 '<ol><li>Natáhněte hrací ruku dlaní nahoru a prsty u sebe.</li>'
                 '<li>Najděte střední ze tří vodorovných rýh v dlani.</li>'
                 '<li>Pravítkem změřte vzdálenost od této rýhy ke špičce prsteníčku.</li>'
                 '<li>Naměřenou hodnotu v palcích (nebo převedenou z cm) porovnejte s tabulkou. Například kolem 4 1/4 palce (asi 10,8 cm) odpovídá L2.</li></ol>'
                 '<p>Kontrola v obchodě: držte raketu běžným úchopem a zkuste mezi konečky prstů a dlaň vložit ukazováček druhé ruky. Když se tam vejde jen tak tak, grip sedí. '
                 'Když mezera chybí, je rukojeť příliš tenká. Když zbývá místo, je příliš tlustá.</p>'
                 '<p>Pokud váháte mezi dvěma velikostmi, vezměte menší. Rukojeť zesílíte vrchní omotávkou (overgrip) zhruba o polovinu velikosti, ale zmenšit ji nejde. '
                 'Příliš tlustý grip ztěžuje změnu úchopu a práci zápěstím, příliš tenký se v ruce stáčí a vede k přílišnému svírání.</p>'
             )),
        dict(h2='Dětská raketa: délka podle věku a výšky',
             html=(
                 '<p>Dětské rakety se značí délkou v palcích. Věkové tabulky se mezi výrobci liší o jednu velikost, proto berte věk jen jako výchozí bod:</p>'
                 + TEN_JUNIOR +
                 '<p>Rozhodující zkouška: dítě stojí rovně, raketu drží za rukojeť volně podél těla. Hlava rakety má být těsně nad zemí a nedotýkat se jí. '
                 'Když se raketa opírá o podlahu, je dlouhá. Když končí vysoko nad zemí, je krátká. Vysoké sedmileté dítě tak může potřebovat 23", menší devítileté naopak ještě 23".</p>'
                 '<p>Juniorské rakety mají obvykle jediný, malý grip L0. Neberte dítěti raketu „na růst“. Příliš dlouhá a těžká raketa vede ke špatné technice a dítě s ní hraje pozdě. '
                 'Krok na 26" a pak na 27" dávejte, až když dítě kratší raketu jasně zvládá. Juniorské modely najdete v kategorii <a href="/tenisove-rakety/">tenisové rakety</a> a vybavení pro tenis obecně v kategorii <a href="/tenis/">tenis</a>.</p>'
             ), cat='tenis', n=4),
        dict(h2='Jak vybrat podle úrovně hráče',
             html=(
                 '<ol><li><strong>Úplný začátečník a příležitostný hráč:</strong> hlava 100–110 sq in, hmotnost kolem 260–285 g, vyvážení do hlavy nebo vyrovnané, otevřený vzor výpletu. Rakety z hliníku jsou levné, ale tvrdě přenášejí otřesy; grafitový nebo kompozitní rám je pro pravidelné hraní příjemnější.</li>'
                 '<li><strong>Rekreační hráč, který hraje každý týden:</strong> hlava kolem 100 sq in, hmotnost 285–300 g, vyrovnané vyvážení. Do této skupiny patří tzv. „game improvement“ i lehčí verze populárních modelů.</li>'
                 '<li><strong>Pokročilý a soutěžní hráč:</strong> hlava 95–100 sq in, hmotnost od 300 g výš, vyvážení do rukojeti, výběr vzoru výpletu podle herního stylu.</li></ol>'
                 '<p>Mnoho výrobců prodává jednu řadu ve více hmotnostech. Například u značky <a href="/znacka/head/">Head</a> nebo Wilson najdete stejný model ve verzi „L“ (lite) a v plné hmotnosti. '
                 'Pokud se vám líbí určitá řada, ale plná verze je těžká, zkuste lehčí variantu. Kdo hraje i na antuce v hale, potřebuje vedle rakety vhodnou obuv, tu porovnáte v kategorii <a href="/tenisova-obuv/">tenisová obuv</a>.</p>'
             ), cat='tenisova-obuv', n=4),
        dict(h2='Jak raketu vyzkoušet a čemu se vyhnout',
             html=(
                 '<p>Nejlepší způsob je zahrát si. Mnoho tenisových klubů a specializovaných prodejen půjčuje testovací rakety. Při testu si všímejte:</p>'
                 '<ul><li>jestli se vám raketa na konci hodiny nezdá těžká,</li>'
                 '<li>jak se chová při volejích u sítě a na servisu,</li>'
                 '<li>jestli necítíte nepříjemné chvění v lokti nebo zápěstí,</li>'
                 '<li>kam létají míče při nepřesném zásahu.</li></ul>'
                 '<p>Časté chyby:</p>'
                 '<ol><li><strong>Kopírování rakety profesionála.</strong> Těžká raketa s malou hlavou je stavěná pro hráče, kteří trénují denně.</li>'
                 '<li><strong>Příliš velký grip.</strong> Vzniká, když se velikost odhaduje „podle oka“. Menší grip jde vždy zesílit.</li>'
                 '<li><strong>Dětská raketa na růst.</strong> Dítě s ní hraje hůř a ztrácí chuť.</li>'
                 '<li><strong>Starý výplet.</strong> Ani dobrá raketa nehraje dobře s výpletem, který ztratil napětí.</li>'
                 '<li><strong>Výběr jen podle ceny.</strong> Stejný model se u různých obchodů liší cenou, ale i rokem výroby a dostupností gripů. Porovnejte nabídky a hlídejte si, jakou velikost gripu kupujete.</li></ol>'
             )),
    ],
    faq=[
        ('Jakou tenisovou raketu pro začátečníka?',
         '<p>Lehčí raketu (zhruba 260–285 g bez výpletu) s větší hlavou kolem 100–110 sq in a otevřeným vzorem výpletu 16×19. Odpustí nepřesný zásah a nevyžaduje rychlý švih.</p>'),
        ('Jak změřím velikost gripu?',
         '<p>Pravítkem od střední rýhy v dlani ke špičce prsteníčku. Délku v palcích porovnejte s tabulkou: 4 1/8 = L1, 4 1/4 = L2, 4 3/8 = L3. Při váhání zvolte menší grip a zesilte ho omotávkou.</p>'),
        ('Jaký grip mají dětské rakety?',
         '<p>Většina juniorských raket se vyrábí v jediné malé velikosti, obvykle L0 (4 palce). Větší gripy se objevují až u raket pro dospělé.</p>'),
        ('Jakou délku rakety pro dítě?',
         '<p>Orientačně 19" do 4 let, 21" pro 4–6 let, 23" pro 6–8 let, 25" pro 8–10 let a 26" pro 10–12 let. Ověřte to výškou: raketa držená podél těla má končit těsně nad zemí.</p>'),
        ('Je lepší lehká, nebo těžká raketa?',
         '<p>Lehká se snadno ovládá, ale je méně stabilní a přenáší víc otřesů. Těžká je stabilní a přesná, jenže vyžaduje rychlý a dobře načasovaný švih. Volte nejtěžší raketu, kterou zvládnete ovládat celý zápas.</p>'),
        ('Co znamená 16×19 a 18×20?',
         '<p>Počet podélných a příčných strun. Otevřený vzor 16×19 pomáhá rotaci a dodá víc síly, hustý 18×20 dává víc kontroly a výplet déle vydrží.</p>'),
        ('Jak často přeplétat raketu?',
         '<p>Častým pravidlem je přeplétat tolikrát ročně, kolikrát týdně hrajete. Výplet ztrácí napětí i bez hraní, proto se po zimní pauze vyplatí nový výplet.</p>'),
        ('Je hliníková raketa vhodná?',
         '<p>Pro první seznámení s tenisem nebo pro děti na pár her ano. Pro pravidelné hraní je příjemnější grafitový nebo kompozitní rám, který méně přenáší otřesy do ruky.</p>'),
        ('Jaká je maximální délka tenisové rakety?',
         '<p>Pravidla ITF povolují nejvýš 73,7 cm (29 palců). Běžné rakety pro dospělé mají 27 palců, tedy přibližně 68,6 cm. Prodloužené modely bývají o půl až jeden palec delší.</p>'),
    ],
    cats=['tenisove-rakety', 'tenis', 'tenisova-obuv'],
    updated='2026-11-19',
)

# ---------------------------------------------------------------- jak-vybrat-badmintonovou-raketu
BAD_WEIGHT = T(['Značení', 'Hmotnost', 'Charakter'], [
    ['2U', '90–94,9 g', 'Těžší, stabilní, pro silné hráče'],
    ['3U', '85–89,9 g', 'Výkonné rakety pro dvouhru a útočnou hru'],
    ['4U', '80–84,9 g', 'Nejuniverzálnější, rychlé a snadno ovladatelné'],
    ['5U', '75–79,9 g', 'Velmi lehké, rychlé v obraně a u sítě'],
])

BAD_BAL = T(['Vyvážení', 'Bod rovnováhy (orientačně)', 'Hodí se na'], [
    ['Do hlavy (head heavy)', 'nad cca 295 mm', 'Smeče a útok ze zadní části kurtu, dvouhra'],
    ['Vyrovnané (even)', 'cca 285–295 mm', 'Univerzální hru, začátečníky i pokročilé'],
    ['Do rukojeti (head light)', 'pod cca 285 mm', 'Rychlou obranu, hru u sítě, čtyřhru'],
])

GUIDES['jak-vybrat-badmintonovou-raketu'] = dict(
    name='Jak vybrat badmintonovou raketu',
    h1='Jak vybrat badmintonovou raketu: hmotnost, vyvážení, tvrdost a výplet',
    seo_title='Jak vybrat badmintonovou raketu: váha, balanc a tvrdost',
    seo_desc='Co znamená 3U, 4U a G5 na raketě? Jak zvolit vyvážení, tvrdost násady a napětí výpletu podle úrovně a stylu hry. Návod pro začátečníky i pokročilé.',
    intro_html=(
        '<p><strong>Jak vybrat badmintonovou raketu?</strong> Pro většinu začátečníků a rekreačních hráčů je dobrá volba raketa s hmotností 4U (80–84,9 g), vyrovnaným vyvážením nebo mírně do rukojeti, '
        'pružnou násadou a výpletem s nižším napětím kolem 20–22 liber. Taková raketa je snadno ovladatelná, odpustí chyby a nebolí z ní zápěstí. '
        'Těžší rakety vyvážené do hlavy a s tuhou násadou se hodí pro pokročilé útočné hráče, kteří umí rychle švihnout.</p>'
        '<p>V článku vysvětlíme, co znamenají kódy jako 3U nebo G5, jak vyvážení a tvrdost ovlivní hru, jak zvolit výplet a čím se liší levné sady pro rekreaci od raket na trénink v oddíle. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů. Pod jednotlivými částmi proto najdete rakety a vybavení na badminton k porovnání.</p>'
    ),
    sections=[
        dict(h2='Rekreační sada, nebo „opravdová“ raketa',
             html=(
                 '<p>Na trhu jsou dva rozdílné světy. <strong>Rekreační sady</strong> se dvěma až čtyřmi raketami, košíčky a někdy i sítí jsou určené na zahradu, pláž a dovolenou. '
                 'Rakety bývají ocelové nebo hliníkové, těžší a s volnějším výpletem. Na občasné odpalování to stačí a sada vydrží hrubší zacházení.</p>'
                 '<p><strong>Rakety pro halový badminton</strong> mají rám z grafitu (uhlíkových vláken), váží zhruba 75 až 95 g a dají se přesně vyplést. '
                 'Pokud chodíte hrát do haly pravidelně, i třeba jen jednou týdně, vyplatí se vlastní grafitová raketa. Rozdíl ve hře je velký: lehká raketa umožní rychlé reakce, které s těžkou ocelovou nezvládnete.</p>'
                 '<p>Pravidla BWF povolují rám nejvýš 680 mm dlouhý a 230 mm široký. Běžné rakety pro dospělé mají kolem 665 až 675 mm. '
                 'Kompletní nabídku raket, košíčků i sítí najdete v kategorii <a href="/badminton/">badminton</a>, výběr z obchodu Decathlon na stránce <a href="/decathlon-badminton/">badminton Decathlon</a>.</p>'
             ), cat='badminton', n=4),
        dict(h2='Hmotnost: co znamená 3U, 4U a 5U',
             html=(
                 '<p>Japonská značka Yonex zavedla značení hmotnosti písmenem U a číslem. Čím vyšší číslo, tím lehčí raketa. Systém dnes používá i řada dalších výrobců:</p>'
                 + BAD_WEIGHT +
                 '<p>Yonex uvádí i 1U (95–99,9 g) a některé značky nabízejí ještě lehčí 6U. U většiny hráčů se ale výběr točí kolem 3U a 4U. Kód bývá vytištěný na krčku rakety nebo na násadě, často spolu s gripem, například „4U G5“.</p>'
                 '<p>Lehčí raketa se rychleji dostane do úderu, méně unavuje zápěstí a rameno a hodí se pro obranu a hru u sítě. Těžší raketa je stabilnější a míček, tedy košíček, s ní letí dál a rychleji při plném švihu, '
                 'ale vyžaduje sílu a dobrou techniku. Začátečník nejčastěji sáhne po 4U. Hráč dvouhry s dobrou technikou může zkusit 3U.</p>'
                 '<p>Rozdíl pěti gramů zní zanedbatelně, ale u nástroje vážícího kolem 85 g je to výrazná změna. Hmotnost navíc vždy posuzujte spolu s vyvážením.</p>'
             )),
        dict(h2='Grip: G4, G5 a G6',
             html=(
                 '<p>Velikost rukojeti se u Yonexu a dalších značek značí písmenem G a číslem. <strong>Čím vyšší číslo, tím tenčí rukojeť.</strong> Nejčastěji se prodávají G4 a G5, G6 je ještě tenčí. '
                 'Jiní výrobci mají vlastní systémy, proto při porovnávání čtěte popis konkrétního modelu.</p>'
                 '<p>V badmintonu se raketa drží volněji než v tenise a úchop se během výměny často mění. Tenčí rukojeť to usnadňuje a umožní víc práce prsty. '
                 'Proto řada hráčů volí tenčí grip a podle potřeby ho zesílí. Vrchní omotávka (overgrip) obvod zvětší, opačně to ale nejde.</p>'
                 '<p>Omotávky se dělají ze syntetického materiálu, nebo z froté, které lépe saje pot. Měňte je, jakmile kloužou nebo jsou ošoupané. Nová omotávka stojí málo a hodně změní pocit z rakety.</p>'
             )),
        dict(h2='Vyvážení (balanc): útok, nebo obrana',
             html=(
                 '<p>Vyvážení udává, kde leží těžiště rakety. Měří se v milimetrech od konce rukojeti. Výrobci a prodejci používají trochu odlišné hranice, orientačně platí:</p>'
                 + BAD_BAL +
                 '<p><strong>Raketa vyvážená do hlavy</strong> má těžiště blíž k výpletu. Při smeči funguje jako kladivo a košíček dostane víc rychlosti. Na rychlé výměny u sítě a v obraně je ale pomalejší a víc unavuje zápěstí.</p>'
                 '<p><strong>Raketa vyvážená do rukojeti</strong> je v ruce svižná, lehce se s ní přechází z forhendu do bekhendu a rychle reaguje na prudké údery soupeře. Typická je pro čtyřhru, kde hráč u sítě rozhoduje o výměně v desetinách sekundy.</p>'
                 '<p><strong>Vyrovnaná raketa</strong> je kompromis a pro začátečníka nejbezpečnější volba. Vyvážení se mírně mění i výpletem, který těžiště posune k hlavě, a omotávkou, která ho posune k rukojeti.</p>'
             ), cat='badminton', n=4),
        dict(h2='Tvrdost násady (flex)',
             html=(
                 '<p>Násada (shaft) je tenká trubka mezi rukojetí a hlavou. Při švihu se ohýbá a v okamžiku zásahu se vrací. Výrobci ji popisují jako pružnou (flexible), střední (medium), tuhou (stiff) a extra tuhou.</p>'
                 '<ul><li><strong>Pružná násada</strong> pomáhá hráčům s pomalejším švihem. Ohne se a „vystřelí“ košíček i při menší síle. Je komfortnější a odpouští nepřesné načasování.</li>'
                 '<li><strong>Střední násada</strong> je univerzální a hodí se pro rekreační i mírně pokročilé hráče.</li>'
                 '<li><strong>Tuhá násada</strong> reaguje přesněji a rychleji, ale potřebuje rychlý švih a správnou techniku. Bez nich je raketa „mrtvá“ a ruka se víc unaví.</li></ul>'
                 '<p>Tvrdost hodnoťte podle rychlosti vlastního švihu, ne podle toho, co hrají reprezentanti. Pokud si nejste jisti, zvolte pružnější verzi. Hráč, který raketu přerostl, to brzy pozná a další koupě bude jasnější.</p>'
             )),
        dict(h2='Výplet a napětí',
             html=(
                 '<p>Napětí výpletu se v badmintonu udává v librách (lbs). Rakety z výroby bývají vypletené na nižší napětí, levnější modely často už v továrně. Lepší rakety se prodávají i bez výpletu a hráč si nechá vyplést vlastní.</p>'
                 '<ul><li><strong>Kolem 20–22 lbs:</strong> doporučované pro začátečníky. Výplet je pružnější, má větší „trampolínový“ efekt a košíček doletí i při menší síle.</li>'
                 '<li><strong>Kolem 23–25 lbs:</strong> běžné pro rekreační a mírně pokročilé hráče.</li>'
                 '<li><strong>26 lbs a víc:</strong> pokročilí hráči s rychlým švihem, kteří chtějí přesnost.</li></ul>'
                 '<p>Vyšší napětí neznamená automaticky silnější úder. Když hráč nezvládne trefit střed výpletu dostatečnou rychlostí, tvrdý výplet košíček spíš „zabrzdí“. Navíc se při vysokém napětí struny rychleji trhají.</p>'
                 '<p>Každá raketa má na rámu nebo v popisu maximální doporučené napětí. Nepřekračujte ho, hrozí prasknutí rámu a zánik záruky. '
                 'Tenčí struny (kolem 0,65 mm) dávají víc citu a zvuku, silnější (kolem 0,70 mm) vydrží déle. Kdo struny trhá často, zvolí silnější.</p>'
             )),
        dict(h2='Výběr krok za krokem podle úrovně',
             html=(
                 '<ol><li><strong>Rekreace na zahradě a na dovolené:</strong> sada se dvěma až čtyřmi raketami a košíčky. Ocel nebo hliník vydrží, výkon nerozhoduje.</li>'
                 '<li><strong>Začátečník v hale:</strong> grafitová raketa 4U, vyrovnané vyvážení nebo do rukojeti, pružná násada, výplet 20–22 lbs, grip G5 s možností omotávky.</li>'
                 '<li><strong>Pravidelný rekreační hráč:</strong> 4U, případně 3U, střední násada, vyvážení podle stylu hry, výplet 22–25 lbs.</li>'
                 '<li><strong>Útočný hráč dvouhry:</strong> 3U, vyvážení do hlavy, tužší násada, vyšší napětí.</li>'
                 '<li><strong>Hráč čtyřhry hrající hodně u sítě:</strong> 4U nebo 5U, vyvážení do rukojeti, střední až tuhá násada.</li></ol>'
                 '<p>U velkých značek, jako je Yonex, mají řady rakety ve více verzích. Zjednodušeně Play a Game jsou levnější a odpouštějící, Tour a Pro náročnější. Při porovnávání proto čtěte celý název modelu. '
                 'Na hru v hale nezapomeňte na obuv se světlou podrážkou, která na palubovce drží a nešpiní ji. Vybírat můžete v kategorii <a href="/salova-obuv/">sálová a halová obuv</a>.</p>'
             ), cat='salova-obuv', n=4),
        dict(h2='Nejčastější chyby a péče o raketu',
             html=(
                 '<ol><li><strong>Příliš těžká a tuhá raketa na začátek.</strong> Bolí z ní zápěstí a hráč se nenaučí správný švih.</li>'
                 '<li><strong>Výplet na maximum.</strong> Začátečník s tvrdým výpletem hraje kratší údery a častěji trhá struny.</li>'
                 '<li><strong>Příliš tlustý grip.</strong> Brání rychlé změně úchopu. Tenčí rukojeť zesílíte omotávkou.</li>'
                 '<li><strong>Raketa v horkém autě.</strong> Vysoká teplota škodí výpletu i rámu. Rakety přenášejte v obalu nebo tašce na rakety.</li>'
                 '<li><strong>Srážky rakety s partnerem ve čtyřhře.</strong> Grafitový rám je pevný v ohybu, ale náraz hranou na hranu ho snadno zlomí.</li></ol>'
                 '<p>Pro squash a další raketové hry platí odlišná pravidla i parametry. Jejich vybavení najdete v kategorii <a href="/squash/">squash</a>, další raketové a míčové sporty v kategorii <a href="/micove-sporty/">míčové a raketové sporty</a>.</p>'
             )),
    ],
    faq=[
        ('Co znamená 4U G5 na badmintonové raketě?',
         '<p>4U je hmotnostní třída 80–84,9 g podle systému značky Yonex. G5 označuje velikost rukojeti, vyšší číslo znamená tenčí grip. Raketa 4U G5 je tedy středně lehká s tenčí rukojetí.</p>'),
        ('Jakou badmintonovou raketu pro začátečníka?',
         '<p>Grafitovou raketu 4U s vyrovnaným vyvážením nebo mírně do rukojeti, pružnou násadou a výpletem kolem 20–22 lbs. Je snadno ovladatelná a nepřetěžuje zápěstí.</p>'),
        ('Je lepší raketa vyvážená do hlavy, nebo do rukojeti?',
         '<p>Do hlavy pro útočné hráče, kteří hodně smečují. Do rukojeti pro rychlou obranu a hru u sítě, typicky ve čtyřhře. Vyrovnaná raketa je univerzální kompromis.</p>'),
        ('Jaké napětí výpletu zvolit?',
         '<p>Začátečník kolem 20–22 lbs, rekreační hráč kolem 23–25 lbs, pokročilý od 26 lbs výš. Nikdy nepřekračujte maximální napětí uvedené na rámu rakety.</p>'),
        ('Jakou tvrdost násady potřebuji?',
         '<p>Čím pomalejší švih, tím pružnější násadu. Tuhá násada se vyplatí jen hráčům s rychlým a technicky správným švihem, jinak působí tvrdě a košíček nedoletí.</p>'),
        ('Jaký grip vybrat, G4, nebo G5?',
         '<p>G5 je tenčí a umožní rychlejší změnu úchopu. Když vám přijde moc tenký, zesílíte ho omotávkou. Silnější G4 ocení hráči s velkou dlaní.</p>'),
        ('Kolik váží badmintonová raketa?',
         '<p>Grafitové rakety pro halový badminton zhruba 75 až 95 g. Rekreační ocelové a hliníkové rakety ze sad bývají výrazně těžší.</p>'),
        ('Jaká je maximální délka badmintonové rakety?',
         '<p>Podle pravidel BWF smí celý rám měřit na délku maximálně 680 mm a na šířku 230 mm. Běžně prodávané rakety bývají dlouhé zhruba 665 až 675 mm.</p>'),
        ('Vyplatí se raketa z rekreační sady pro hraní v hale?',
         '<p>Na první vyzkoušení ano. Pokud ale chcete hrát pravidelně, těžká ocelová raketa vás bude brzdit. Lehká grafitová raketa umožní rychlejší údery a lepší techniku.</p>'),
    ],
    cats=['badminton', 'salova-obuv'],
    updated='2026-11-19',
)

# ---------------------------------------------------------------- velikosti-fotbalovych-micu
BALL_SIZES = T(['Velikost', 'Obvod', 'Hmotnost', 'Orientačně pro'], [
    ['č. 3', '58,5–61 cm', 'přibližně 300–340 g podle výrobce', 'Děti do 8 let, přípravky'],
    ['č. 4', '63,5–66 cm', 'přibližně 350–390 g (odlehčené méně)', 'Děti zhruba 8–12 let, mladší žáci'],
    ['č. 5', '68–70 cm', '410–450 g (pravidla IFAB)', 'Od zhruba 12–13 let a dospělí'],
    ['Futsal č. 4', '62–64 cm', '400–440 g', 'Futsal a sálová kopaná'],
])

GUIDES['velikosti-fotbalovych-micu'] = dict(
    name='Velikosti fotbalových míčů',
    h1='Velikosti fotbalových míčů: který míč pro jaký věk',
    seo_title='Velikosti fotbalových míčů: který míč pro jaký věk',
    seo_desc='Míč č. 3, 4, nebo 5? Obvod a hmotnost podle pravidel, který míč pro jaký věk, futsalový míč, materiály, značky FIFA Quality a jak míč nafukovat a skladovat.',
    intro_html=(
        '<p><strong>Jakou velikost fotbalového míče vybrat?</strong> Dospělí a mládež zhruba od 12–13 let hrají s míčem velikosti 5, který má podle pravidel obvod 68–70 cm a hmotnost 410–450 g. '
        'Děti zhruba mezi 8 a 12 lety používají menší a lehčí míč velikosti 4 (obvod asi 63,5–66 cm). Nejmenší děti do 8 let hrají s míčem velikosti 3. '
        'Na futsal se používá speciální míč velikosti 4 s menším odskokem. Věkové hranice se mezi soutěžemi liší, proto se u dětí v oddíle vždy zeptejte trenéra.</p>'
        '<p>V článku najdete tabulku velikostí, rozdíly mezi tréninkovým a zápasovým míčem, futsalovým a halovým míčem, vysvětlení značek FIFA Quality a návod, jak míč správně nafukovat. '
        'Sporteka nic neprodává, jen srovnává nabídky českých obchodů. Pod částmi článku proto uvidíte míče a kopačky k porovnání.</p>'
    ),
    sections=[
        dict(h2='Tabulka velikostí fotbalových míčů',
             html=(
                 '<p>Rozměry dospělého míče stanoví pravidlo 2 Pravidel fotbalu, která vydává IFAB. Menší velikosti pravidla přímo nepopisují, jejich obvod a hmotnost určují výrobci a soutěžní řády mládeže. '
                 'Proto se údaje u různých značek mírně liší.</p>'
                 + BALL_SIZES +
                 '<p>Velikost je téměř vždy vytištěná přímo na míči, obvykle jako „Size 5“ nebo číslo vedle loga. V popisu produktu ji e-shopy uvádějí jako „vel. 5“ nebo „č. 5“. '
                 'Nabídku všech velikostí porovnáte v kategorii <a href="/fotbalove-mice/">fotbalové míče</a>.</p>'
             ), cat='fotbalove-mice', n=4),
        dict(h2='Který míč pro jaký věk',
             html=(
                 '<p>Menší a lehčí míč dětem umožní správnou techniku přihrávky i střely a nebolí při hlavičkování ani při zásahu do těla. Orientační dělení, které používá většina výrobců:</p>'
                 '<ul><li><strong>Velikost 3:</strong> předškoláci a děti zhruba do 8 let. Například v soutěžích kategorie U8 se v Česku hraje běžně s míčem č. 3.</li>'
                 '<li><strong>Velikost 4:</strong> děti zhruba od 8 do 12 let. Pro mladší z nich se vyrábějí i odlehčené „light“ verze, které jsou velikostí 4, ale hmotností blíž menšímu míči. '
                 'Propozice pro kategorii U12 uvádějí například míč č. 4 s obvodem 63–66 cm a hmotností 290–390 g.</li>'
                 '<li><strong>Velikost 5:</strong> starší žáci, dorost a dospělí, obvykle od 12–13 let.</li></ul>'
                 '<p>Věkové tabulky se u výrobců liší, a někde se dokonce posouvají o několik let. Rozhodující je, s jakým míčem hraje oddíl a soutěž, kam dítě chodí. '
                 'Některé kluby po dětech chtějí vlastní míč na trénink. Metodiky klubů často uvádějí velikost 3, případně odlehčenou čtyřku. Než míč koupíte, zeptejte se trenéra.</p>'
                 '<p>Pro hraní na zahradě s malými dětmi stačí jakýkoli menší a měkčí míč. Na kopání do branky na zahradě se hodí i <a href="/fotbalove-branky/">fotbalové branky</a> menších rozměrů.</p>'
             ), cat='fotbalove-branky', n=4),
        dict(h2='Futsalový a halový míč',
             html=(
                 '<p>Futsal se hraje s vlastním míčem. Má velikost 4 s obvodem 62–64 cm, ale hmotnost 400–440 g, tedy skoro jako dospělý míč na velký fotbal. '
                 'Uvnitř má hustší výplň nebo speciální duši, která snižuje odskok. Podle pravidel futsalu musí míč puštěný z výšky 2 m při prvním odrazu vyskočit do výšky 50 až 65 cm.</p>'
                 '<p>Nízký odskok drží míč u země, takže se s ním lépe kombinuje na malém prostoru a tvrdé palubovce. Běžný fotbalový míč by v hale skákal nekontrolovatelně.</p>'
                 '<ul><li><strong>Futsalový míč:</strong> pro oficiální futsal a sálovou kopanou podle pravidel FIFA.</li>'
                 '<li><strong>Halový míč (indoor):</strong> obvykle velikost 4 nebo 5 s plstěným nebo měkkým povrchem pro tělocvičny. Nešpiní stěny a je tišší.</li>'
                 '<li><strong>Míč na umělou trávu a beton:</strong> má odolnější povrch, který se tolik neodírá.</li></ul>'
                 '<p>Na hru v hale potřebujete i správnou obuv s nešpinivou podrážkou. Porovnejte ji v kategorii <a href="/salova-obuv/">sálová a halová obuv</a>.</p>'
             ), cat='salova-obuv', n=4),
        dict(h2='Zápasový, tréninkový a rekreační míč',
             html=(
                 '<p>Stejná velikost neznamená stejný míč. Výrobci prodávají několik úrovní, které se liší konstrukcí, materiálem i životností:</p>'
                 '<ol><li><strong>Zápasový (match) míč</strong> má nejpřesnější tvar, stálou hmotnost a jemný povrch, který dobře reaguje na nohu. Bývá dražší a na drsném povrchu se rychleji opotřebí.</li>'
                 '<li><strong>Tréninkový míč</strong> je odolnější a snese denní kopání na umělé trávě i škvaře. Hraje se s ním trochu „tvrději“.</li>'
                 '<li><strong>Rekreační míč</strong> na zahradu a hřiště je levný, často z PVC, a nevadí mu ani asfalt.</li></ol>'
                 '<p>Oficiální míče soutěží, například české ligy nebo Ligy mistrů, se prodávají v zápasové verzi i v levnějších replikách se stejným designem. '
                 'Replika je obvykle tréninkový nebo rekreační míč, nikoli totéž co zápasový kus. Rozdíl poznáte podle názvu modelu a podle certifikace FIFA.</p>'
             )),
        dict(h2='Co znamenají značky FIFA Quality Pro, FIFA Quality a FIFA Basic',
             html=(
                 '<p>FIFA provozuje program kvality fotbalových míčů. Nezávislá laboratoř míč testuje a výrobce pak smí použít jednu ze tří značek:</p>'
                 '<ul><li><strong>FIFA Quality Pro:</strong> nejvyšší úroveň. Nejpřísnější testy přesnosti, výkonu a odolnosti, určené pro profesionální zápasy.</li>'
                 '<li><strong>FIFA Quality:</strong> důraz na odolnost a bezpečnost, vhodné i pro soutěžní fotbal.</li>'
                 '<li><strong>FIFA Basic:</strong> základní úroveň, která ověřuje základní výkon, přesnost, bezpečnost a odolnost. Nahradila dřívější značku IMS (International Match Standard).</li></ul>'
                 '<p>Testuje se hmotnost, obvod, kulatost, odskok, nasákavost vodou, ztráta tlaku a zachování tvaru a velikosti po opakovaných nárazech. '
                 'Podle pravidel musí míče v mezinárodních zápasech pořádaných FIFA nebo konfederacemi nést některou z těchto značek.</p>'
                 '<p>Pro rekreační hru certifikát nepotřebujete. Pro oddílový trénink a zápasy je značka užitečná jistota, že míč má stálý tvar a neztrácí rychle vzduch. Míče v oficiálních soutěžích mládeže vybírá pořadatel.</p>'
             ), cat='fotbalove-mice', n=4),
        dict(h2='Materiál a konstrukce: šitý, nebo lepený',
             html=(
                 '<p><strong>Povrch</strong> se vyrábí nejčastěji z polyuretanu (PU) nebo z PVC. Polyuretan je měkčí a lépe reaguje na nohu, proto se používá u zápasových a lepších tréninkových míčů. '
                 'PVC je tvrdší, levnější a odolnější vůči odření, typicky u rekreačních míčů.</p>'
                 '<p><strong>Spojení panelů</strong> existuje ve třech hlavních variantách:</p>'
                 '<ul><li><strong>ručně šitý</strong> míč s pevnými a odolnými švy,</li>'
                 '<li><strong>strojově šitý</strong> míč, levnější a vhodný na rekreaci,</li>'
                 '<li><strong>tepelně lepený (thermobonded)</strong> míč bez švů s velmi stálým tvarem a nižší nasákavostí, typický pro moderní zápasové míče.</li></ul>'
                 '<p><strong>Duše</strong> bývá z butylu nebo z latexu. Butylová duše drží vzduch déle a hodí se na trénink. Latexová dává měkčí pocit z kopu, ale vzduch z ní uniká rychleji, takže se míč musí dofukovat častěji.</p>'
             )),
        dict(h2='Jak míč nafukovat, kontrolovat a skladovat',
             html=(
                 '<ol><li><strong>Zjistěte doporučený tlak.</strong> Bývá vytištěný u ventilku. Pravidla povolují pro dospělý míč 0,6 až 1,1 atmosféry na úrovni moře, výrobce ale udává užší rozmezí pro konkrétní model.</li>'
                 '<li><strong>Navlhčete jehlu.</strong> Kapka vody nebo glycerinu ochrání ventilek. Jehlu zasouvejte rovně a pomalu.</li>'
                 '<li><strong>Měřte tlak manometrem.</strong> Zkouška zmáčknutím palcem je nepřesná. Přefouknutý míč je tvrdý a hůř se kontroluje, podfouknutý se rychleji deformuje.</li>'
                 '<li><strong>Míč po tréninku očistěte a osušte.</strong> Bláto a voda zkracují životnost povrchu a švů.</li>'
                 '<li><strong>Skladujte ho v suchu a pokojové teplotě.</strong> Mráz a horko v autě míči škodí. Na delší skladování vypusťte trochu vzduchu.</li>'
                 '<li><strong>Nesedejte si na míč.</strong> Deformuje se tím a ztrácí kulatý tvar.</li></ol>'
                 '<p>Zápasové míče se nehodí na beton a asfalt, povrch se brzy odře. Na takové hřiště si vezměte tréninkový nebo rekreační míč.</p>'
                 '<p>Míč zkontrolujte vždy před sezónou. Vypouklý panel, odlepený šev nebo „vajíčkový“ tvar po kopnutí znamenají, že duše nebo kostra jsou poškozené a míč už nepoletí rovně. '
                 'Když míč ztrácí vzduch rychleji než dřív, zkuste ventilek namočit do vody s jarem. Bublinky prozradí, jestli vzduch uniká ventilkem, nebo jinde. Prasklou duši už většinou nespravíte a vyplatí se nový míč.</p>'
             )),
        dict(h2='Jak vybrat míč krok za krokem',
             html=(
                 '<ol><li><strong>Určete velikost</strong> podle věku hráče a podle toho, s čím hraje jeho oddíl.</li>'
                 '<li><strong>Zvolte povrch</strong>, na kterém se bude hrát: tráva, umělá tráva, hala, nebo asfalt.</li>'
                 '<li><strong>Rozhodněte úroveň:</strong> zápas, trénink, nebo rekreace.</li>'
                 '<li><strong>U soutěžního fotbalu</strong> hledejte značku FIFA Quality nebo FIFA Quality Pro, případně požadavek ligy na konkrétní model.</li>'
                 '<li><strong>Porovnejte nabídky.</strong> Stejný míč se u různých obchodů liší cenou i dostupností velikostí.</li></ol>'
                 '<p>K míči se hodí i vhodná obuv. Pro velké hřiště vybírejte <a href="/kopacky/">kopačky</a> s podrážkou podle povrchu, pro děti nabídka <a href="/detske-kopacky/">dětské kopačky</a>. '
                 'Na chránění holení slouží <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a> a další vybavení najdete v kategorii <a href="/fotbal/">fotbal</a>.</p>'
             ), cat='kopacky', n=4),
    ],
    faq=[
        ('Jakou velikost míče má dospělý fotbal?',
         '<p>Velikost 5. Podle pravidla 2 Pravidel fotbalu má obvod 68–70 cm a na začátku utkání váží 410–450 g.</p>'),
        ('Jaký míč pro dítě 6 let?',
         '<p>Nejčastěji velikost 3, která je menší a lehčí. Některé kluby používají u mladších dětí i odlehčenou velikost 4. Ověřte si to u trenéra.</p>'),
        ('Jaký míč pro dítě 10 let?',
         '<p>Obvykle velikost 4. Pokud hraje v oddíle, ptejte se trenéra na konkrétní typ, některé soutěže předepisují odlehčenou verzi.</p>'),
        ('Od kolika let se hraje s míčem č. 5?',
         '<p>Zpravidla od 12 až 13 let, kdy děti přecházejí na větší hřiště. Přesná hranice se liší podle soutěže a výrobce.</p>'),
        ('Jaký je rozdíl mezi futsalovým a fotbalovým míčem?',
         '<p>Futsalový míč je menší (velikost 4, obvod 62–64 cm), ale poměrně těžký a má výrazně nižší odskok. Puštěný z 2 m vyskočí jen 50–65 cm, takže se drží u země.</p>'),
        ('Co znamená FIFA Quality Pro?',
         '<p>Nejvyšší certifikace v programu kvality FIFA. Míč prošel nejpřísnějšími testy hmotnosti, obvodu, kulatosti, odskoku, nasákavosti a ztráty tlaku. Nižší úrovně jsou FIFA Quality a FIFA Basic.</p>'),
        ('Jak poznám velikost míče?',
         '<p>Velikost bývá vytištěná přímo na míči, obvykle jako Size 3, 4 nebo 5. Pokud chybí, změřte obvod krejčovským metrem a porovnejte s tabulkou.</p>'),
        ('Na jaký tlak nafouknout fotbalový míč?',
         '<p>Podle údaje výrobce, který je vytištěný u ventilku. Pravidla povolují pro dospělý míč 0,6–1,1 atmosféry. Tlak měřte manometrem a jehlu před zasunutím navlhčete.</p>'),
        ('Je lepší šitý, nebo lepený míč?',
         '<p>Tepelně lepený míč má stálejší tvar a méně nasákne vodou, proto se používá u zápasových modelů. Šitý míč je odolný a hodí se na trénink. Pro rekreaci stačí strojově šitý.</p>'),
    ],
    cats=['fotbalove-mice', 'fotbal', 'kopacky'],
    updated='2026-11-19',
)
