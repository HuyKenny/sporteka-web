"""sporteka.cz — wave 24a (5. 11. 2026): long texts for pop-up-a-plazove-stany, hry-na-zahradu, hokejove-suveniry-a-karty, discgolf.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ pop-up-a-plazove-stany
NEW['pop-up-a-plazove-stany'] = dict(long=True,
    title='Pop-up a plážové stany: velikost, UV filtr, větrná stabilita',
    desc='Samorozkládací pop-up stany a plážové přístřešky. Jak vybrat velikost, UV ochranu, kotvení a skládání, a porovnat nabídky českých obchodů.',
    intro='<p>Samorozkládací stan se po vyndání z obalu sám narovná a během několika vteřin stojí. Právě tahle rychlost z něj dělá oblíbenou pomůcku na pláž, na festival, na koupaliště i na dětské hřiště, kde se neplatí skládat tyče a napínat šňůry. Sporteka porovnává nabídky českých obchodů u plážových stínítek, kompaktních pop-up stanů na přespání, převlékacích a sprchových kabinek i dílů, jako jsou náhradní tyče a kolíky.</p>'
          '<p>V nabídce jsou značky ' + B(('nils', 'Nils'), ('nils-camp', 'NILS Camp'), ('springos', 'Springos'), ('quechua', 'Quechua'), ('spokey', 'Spokey'), ('loap', 'Loap'), ('skandika', 'Skandika'), ('mfh', 'Mfh'), ('high-peak', 'High Peak'), ('insportline', 'Insportline')) +
          '. Pokud hledáte klasické tyčové konstrukce, pokračujte do kategorií <a href="/stany/">stany</a>, <a href="/turisticke-stany/">turistické stany</a> nebo <a href="/rodinne-stany/">rodinné stany</a>.</p>',
    guide='<h2>Jak pop-up stan funguje</h2>'
          '<p>Základem je pružný obruč z ocelového drátu nebo skelného vlákna, ovinutý látkou. Po uvolnění popruhu se obruč vlastní pružností rozevře do původního tvaru a stan se napne. Dva nebo tři zkřížené oblouky vytvoří kopuli, jeden ohnutý oblouk vytvoří klasický plážový polostan se zadní stěnou. Balení je opačný postup: obruč se přeloží do několika smyček a stan se zkroutí do plochého disku. Chvíli trvá, než si na to ruka zvykne, ale potom se skládání dá zvládnout bez návodu.</p>'
          '<p>Tahle konstrukce je ovšem kompromis. Obruč nemá takovou pevnost jako hliníkové tyče, takže pop-up stan hůř snáší silný vítr a těžké mokro. Pro stálý tábor na týden v horách se nehodí, pro denní výlet k vodě nebo víkend na festivalu je to ideální řešení.</p>'
          '<h2>Typy stanů v kategorii</h2>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Plážový stan', 'nízká, napínaná zadní stěna, otevřená přední strana', 'pláž, koupaliště, piknik s dětmi'],
              ['Samorozkládací stan na přespání', 'kompaktní kopule pro 2 až 3 osoby, někdy se zatemněním', 'festivaly, jednorázové noci, dětské přespání na zahradě'],
              ['Zatemňovací varianta', 'tmavá vnitřní vrstva proti světlu', 'ranní spaní na festivalu, kojenci a malé děti'],
              ['Převlékací a sprchový stan', 'vysoký, úzký, uzavřený', 'pláž, kemp, zahrada, závody'],
              ['Rodinný plážový stan', 'větší půdorys, stínění ze tří stran', 'rodina s dětmi na celý den'],
              ['Stan na sportovní akce', 'lehký přístřešek bez podlahy', 'trenér a rozhodčí u hřiště, týmový přístřešek'],
              ['Náhradní díly', 'tyče, kolíky, taška', 'oprava poškozeného stanu']]) +
          '<h2>Velikost podle počtu lidí a vybavení</h2>'
          '<p>Rozměry výrobci uvádějí jako délku, šířku a výšku v centimetrech a souhrnně jako počet osob. Číslovka na štítku je obvykle ale optimistická: dva dospělí a dvě tašky se do stanu pro dvě osoby vejdou jen při úzkém uložení. Počítejte s rezervou o jednu osobu více, než kolik lidí chcete ubytovat nebo zastínit.</p>'
          '<ul><li><strong>Jedna osoba nebo dítě:</strong> stačí menší stínítko, do kterého se vejde lehátko nebo dětský koberec.</li>'
          '<li><strong>Pár nebo rodina se dvěma malými dětmi:</strong> volte plážový stan s hloubkou alespoň okolo 120 cm a přední vstup, ze kterého vidíte na vodu.</li>'
          '<li><strong>Čtyři a více osob:</strong> větší kopule nebo model se stíněním ze tří stran, ale pozor na váhu a velikost obalu.</li>'
          '<li><strong>Přespání:</strong> počítejte s délkou aspoň o 20 až 30 cm víc, než je tělesná výška nejvyššího spáče, a se zbytkem prostoru pro zavazadla.</li></ul>'
          '<p>Důležitý je i rozměr po složení. Pop-up stan má typicky tvar disku, jehož průměr odpovídá přibližně polovině rozevřené šířky. Vejde se tedy do kufru, ale na kolo nebo do batohu ho s sebou nevezmete.</p>'
          '<h2>UV ochrana a stínění</h2>'
          '<p>Plážový stan chrání před přímým sluncem, ale ne před odraženým světlem od vody a písku. UV filtr se označuje jako UPF nebo UV faktor a výrobce ho uvádí v popisu. Čím tmavší a hustší je látka, tím lépe filtruje záření. Stříbrný povlak odráží záření zpět, kdežto tmavá látka ho pohlcuje a ohřívá se. Světlé barvy se méně zahřívají, ale propouštějí víc záření.</p>'
          '<p>V horkých dnech pomůže, když stan umožňuje průvan. Síťová okénka nebo možnost odepnout zadní stěnu zlepší větrání, jinak se ve stanu hromadí horký vzduch. Čtěte také, zda je zadní stěna pevně přišitá, nebo zda se dá zvednout. Pro děti je vhodné stínění spolu s krémem a pokrývkou hlavy, stan samotný jim ochranu nezajistí.</p>'
          '<h2>Vítr a kotvení</h2>'
          '<p>Největší nepřítel pop-up stanu je vítr. Plochá plocha stěny funguje jako plachta a lehký stan se může převrátit i s dítětem uvnitř. Proto se vyplatí zakotvit ho vždy, ne jen když začne foukat.</p>'
          '<ul><li><strong>Kolíky:</strong> v písku drží špatně. Použijte delší nebo spirálové, nebo je zakopejte šikmo a obložte kameny. Podrobnosti najdete v kategorii <a href="/stanove-kolky/">stanové kolíky a kotvení</a>.</li>'
          '<li><strong>Písek v kapsách:</strong> některé plážové stany mají na spodním okraji lem, který se dá zasypat pískem.</li>'
          '<li><strong>Otočení zády:</strong> zadní stěnu natočte proti převládajícímu větru, otevřená strana ať směřuje po větru.</li>'
          '<li><strong>Zátěž uvnitř:</strong> batoh, chladicí box nebo taška vody drží stan při zemi.</li>'
          '<li><strong>Rozumný odchod:</strong> při silných nárazech nebo bouřce stan sbalte, protože tenké drátěné obruče se při přetížení lámou.</li></ul>'
          '<h2>Materiál, švy a voděodolnost</h2>'
          '<p>Většina pop-up stanů je z polyesteru nebo nylonu s povrchovou úpravou. Plážové modely nejsou stavěné na déšť, takže jejich voděodolnost bývá nízká a švy nemusí být přelepené. Stany na přespání mívají vyšší voděodolnost a dno z pevnější vrstvy, ale přesto nenahrazují klasický turistický stan při dlouhém dešti. Údaj vodního sloupce porovnávejte jen mezi stany podobné kategorie, a hlavně sledujte, zda jsou švy přelepené.</p>'
          '<p>Pozor na rozdíl mezi stanem s podlážkou a bez. Plážový stan bývá bez podlahy, takže pod ním rozložíte deku nebo lehátko. Stan na spaní naopak potřebuje podlahu, a pokud ji nemá, doplňte ji <a href="/stanove-doplnky/">podlážkou nebo plachtou</a>.</p>'
          '<h2>Skládání a balení</h2>'
          '<p>Nejčastější stížnost se týká balení, ne stavění. Postup je prostý, ale vyžaduje cvik: stan postavte na bok, uchopte dva protilehlé body obruče a tlačte je k sobě, přitom stan přetáčejte, až vznikne trojitá smyčka. Poté ho stáhněte popruhem nebo vložte do obalu. Ukázku si před koupí vyhledejte v návodu výrobce a zkuste si to jednou doma, ne ve větru na pláži.</p>'
          '<ul><li>Nikdy nesvírejte obruč v ruce proti ohybu, zlomí se.</li>'
          '<li>Při balení stan nepokládejte na ostrý kámen, a zbavte ho písku.</li>'
          '<li>Při prvním rozložení doma si ověřte, zda sedí všechny popruhy a kolíky.</li>'
          '<li>Skládání v týmu je snazší: jeden drží obruč, druhý stahuje popruh.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Po pláži vždy stan omyjte čistou vodou, protože sůl a písek poškozují látku a zipy. Nechte ho úplně vyschnout v rozloženém stavu, jinak se na látce objeví plíseň a zápach. Zipy občas natřete silikonovým mazivem a z kapes vytřepejte písek. Uložte ho volně, ne pod těžkými předměty, a mimo přímé slunce, které poškozuje impregnaci i barvy.</p>'
          '<p>Opravy drobných dírek zvládne samolepicí záplata. Při zlomení obruče je oprava komplikovanější: u některých modelů se dají koupit náhradní tyče, ale u levnějších se stan obvykle vyměňuje celý. Další opravárenské doplňky najdete v kategorii <a href="/stanove-doplnky/">plachty, podlážky a opravy stanů</a>.</p>'
          '<h2>Pop-up stan na přespání: co čekat</h2>'
          '<p>Samorozkládací stan pro víkend vypadá lákavě, ale má svá omezení. Většinou má jednu vrstvu látky, takže vlhkost se sráží na vnitřní stěně a ve stanu je ráno vlhko. Prostor bývá nízký, takže se nedá vstát. Zatemňovací vrstva sice zadrží světlo, ale zhorší větrání. Proto se na pop-up stan spoléhejte tam, kde chcete rychlost a pohodlí, ne extrémní podmínky. Pokud plánujete trek nebo vícedenní pobyt v přírodě, přečtěte si raději o <a href="/turisticke-stany/">turistických a trekových stanech</a>, a pokud pojedete s dětmi, porovnejte i <a href="/detske-stany/">dětské stany</a>.</p>'
          '<p>K přespání se hodí <a href="/karimatky-a-matrace/">karimatka nebo matrace</a> a <a href="/spaci-pytle/">spací pytel</a>, protože tenký povrch stanu od země téměř neizoluje. Na festival se vyplatí lampička nebo <a href="/celovky-a-svitilny/">čelovka</a>, protože stany bývají blízko sebe a snadno se v noci splete vstup.</p>'
          '<h2>Převlékací a sprchové kabiny</h2>'
          '<p>Vysoké kabinky mají v kategorii vlastní místo. Jsou to úzké válce nebo hranoly, které se v jednom pohybu rozloží a poskytnou soukromí pro převlečení, sprchu s kempingovým zásobníkem nebo záchod. Dobře se hodí na pláže bez zázemí, na závodní akce a na zahradu. Hledejte nepropustnou látku, aby neprosvítala, a možnost zatížit dno. U modelů se zipem do podlahy pamatujte, že písek se do zipu rád dostane a pokazí ho.</p>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Dovolená u moře s dětmi:</strong> větší plážový stan s UV filtrem a výrazným lemem na zakotvení pískem.</li>'
          '<li><strong>Koupaliště a jednodenní výlet:</strong> lehký stan, který se vejde do kufru a dá se rychle postavit i složit.</li>'
          '<li><strong>Festival:</strong> zatemňovací pop-up s dvěma vchody a dobrým větráním.</li>'
          '<li><strong>Sportovní akce:</strong> menší přístřešek bez podlahy, který se dá umístit u hřiště.</li>'
          '<li><strong>Zahradní přespání dětí:</strong> prostorná kopule, ke které se hodí <a href="/detske-spacaky/">dětské spacáky</a>.</li>'
          '<li><strong>Rybář:</strong> robustnější stan, spíš z kategorie <a href="/rybarske-stany/">rybářské stany a bivaky</a>.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Většinu nabídky tvoří plážové stany značek Nils, NILS Camp a Springos. Quechua je zastoupená známými stany 2 Seconds, které jsou dostupné v různých velikostech a se zatemněním. Spokey, Loap, Skandika, High Peak a Insportline nabízejí menší stínítka a rodinné modely. Objeví se tu i stan Mfh Quick Up Monodom, převlékací a sprchové kabinky nebo stan na plážovou házenou. Do kategorie patří také tyče a díly. Jiné stany, například <a href="/pristresky-a-party-stany/">přístřešky a párty stany</a> nebo <a href="/strechni-stany/">střešní stany</a>, najdete ve svých kategoriích.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Spoléhání na uvedenou kapacitu bez ohledu na vybavení a prostor pro pohyb.</li>'
          '<li>Koupě bez kolíků a bez představy, jak stan zajistit v písku.</li>'
          '<li>Očekávání, že plážový stan vydrží déšť nebo silnou bouřku.</li>'
          '<li>Nepočítání s tím, že tmavá látka a špatné větrání vytvoří uvnitř horko.</li>'
          '<li>Zkoušení balení až na pláži, kde fouká.</li>'
          '<li>Skladování nevysušeného stanu v obalu.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Plážové stany jsou sezónní zboží, takže nabídka a dostupnost velikostí a barev se mění. U každého produktu vidíte, které obchody ho mají, a můžete porovnat varianty. Sledujte popis rozměrů, UV faktoru, váhy a zda je v ceně taška a kolíky. Skladové zásoby jsou nejširší na jaře, ke konci léta se rozprodávají poslední barvy, což je dobrá příležitost pro ty, kdo nepotřebují konkrétní odstín.</p>',
    faq=[
        ('Jak rychle se pop-up stan postaví?', 'Obvykle během několika vteřin: stačí uvolnit popruh a stan se sám rozevře. Pak ho zakotvíte kolíky. Zdlouhavější je balení, které chce trochu cviku.'),
        ('Vydrží plážový stan vítr?', 'Jen mírný, protože ploché stěny fungují jako plachta. Zakotvěte ho kolíky nebo písečnými kapsami, otočte zády k větru a zatěžte uvnitř. Při silném větru ho radši sbalte.'),
        ('Chrání plážový stan před UV zářením?', 'Částečně. Látka s UV filtrem snižuje záření, ale odražené světlo od vody a písku se dostane dovnitř. Pro děti proto nezapomeňte na krém a pokrývku hlavy.'),
        ('Dá se v pop-up stanu spát?', 'Ano, v modelech určených na přespání, které mají podlahu a vstup se zipem. Pro nepříznivé počasí a delší pobyty jsou ale vhodnější klasické turistické stany.'),
        ('Jak vybrat velikost stanu?', 'Počet osob na štítku berte jako maximum a počítejte s jednou osobou navíc. Důležitá je i výška, délka a zavazadla. Zohledněte také rozměr po složení, aby se vešel do kufru.'),
        ('Jak stan složit zpátky do obalu?', 'Postavte ho na bok, stlačte dva protilehlé body obruče k sobě a stan přetáčejte, až vznikne trojitá smyčka. Přetížení proti ohybu obruč láme, takže nenásilně.'),
        ('Jak pop-up stan čistit?', 'Omyjte ho čistou vodou, ideálně hadicí, a nechte rozložený úplně vyschnout. Sůl a písek poškozují látku i zipy. Nepoužívejte agresivní chemii a stan neperte v pračce.'),
        ('Je zatemňovací stan lepší?', 'Na ranní spaní a pro malé děti ano, protože zadrží světlo. Teplota uvnitř ale závisí hlavně na větrání a provedení, proto v popisu hledejte síťová okénka nebo údaj výrobce; ve velkém vedru bez průvanu se bude zahřívat každý stan.'),
        ('K čemu je převlékací stan?', 'Poskytuje soukromí při převlékání nebo sprše, na pláži, v kempu i na závodech. Je úzký a vysoký, rychle se staví a hodí se i na zahradu. Při větru ho zatěžte u dna.'),
        ('Kde koupit náhradní tyče nebo kolíky?', 'U některých značek se prodávají samostatně, v kategorii najdete vybrané díly. Kolíky univerzálního typu najdete také v kategorii stanové kolíky a kotvení. U levnějších modelů se ale často vyplatí vyměnit celý stan.'),
    ],
)

# ------------------------------------------------------------------ hry-na-zahradu
NEW['hry-na-zahradu'] = dict(long=True,
    title='Hry na zahradu a pláž: kroket, pétanque, boccia, soft tenis',
    desc='Kroket, pétanque, boccia, soft tenis a další hry na zahradu a pláž. Jak vybrat sadu podle věku, povrchu a počtu hráčů a porovnat nabídky obchodů.',
    intro='<p>Zahradní hry mají jednu výhodu: nepotřebují hřiště ani zvláštní kondici a baví děti, rodiče i prarodiče najednou. Stačí kus trávníku, písek nebo udusaná cesta. Sporteka porovnává nabídky českých obchodů u krocketu, pétanque a koulené, boccie, soft tenisu, dětských her na venkovní odpoledne a drobného příslušenství, například náhradních koulí. Ať už plánujete nedělní odpoledne na chalupě, rodinnou dovolenou u vody nebo oslavu s dětmi na dvorku, najdete tu hru, která vyžaduje minimum přípravy.</p>'
          '<p>V kategorii jsou značky ' + B(('lucio-londero', 'Lucio Londero'), ('geologic', 'Geologic'), ('master', 'Master'), ('koodza', 'Koodza'), ('decathlon', 'Decathlon'), ('londero', 'Londero'), ('sedco', 'Sedco'), ('obut', 'Obut'), ('kensis', 'Kensis'), ('mondo', 'Mondo')) +
          '. Podobné nápady najdete také v kategoriích <a href="/volny-cas/">hry a volný čas</a>, <a href="/sipky/">šipky</a>, <a href="/discgolf/">discgolf a frisbee</a> a <a href="/trampoliny/">trampolíny</a>.</p>',
    guide='<h2>Jaké hry v kategorii najdete</h2>'
          '<p>Nabídka je užší než u běžných sportů, ale každá hra se hodí jinak. Něco vyžaduje rovný trávník, jiné se dá hrát na pláži, na štěrku nebo v kempu. Při výběru se proto ptejte, kde se bude hrát a kolik lidí se zúčastní.</p>'
          + T(['Hra', 'Povrch', 'Hráči', 'Charakter'], [
              ['Kroket', 'trávník, rovná plocha', '2 až 6', 'tichá strategie, vhodná pro všechny věkové skupiny'],
              ['Pétanque a koulená', 'písek, štěrk, udusaná zem', '2 až 6', 'hod kovovou nebo plastovou koulí k cílové kuličce'],
              ['Boccia', 'rovný pevný povrch', '2 až 4', 'podobná pétanque, vhodná i pro hráče s omezením pohybu'],
              ['Soft tenis', 'zahrada, pláž, ulice', '2', 'měkké míčky a lehké rakety bez sítě'],
              ['Gabaky a hry na chytání', 'zahrada, pláž', '2 až 4', 'rychlé, hlučné, pro děti'],
              ['Fotbalový kroket', 'trávník', '2 až 4', 'mix krocketu a fotbalu pro děti']]) +
          '<h2>Kroket: dřevo, kov a plast</h2>'
          '<p>Kroket je nejobsáhlejší hra v kategorii. Základní sada obsahuje dřevěné nebo plastové koule, kladívka, branky a dva kolíky. Pro malé hráče existují lehčí plastové sady s krátkými kladívky, pro dospělé klasické modely s dlouhou násadou a těžšími koulemi. Kvalitní sady ocení ti, kdo hrají pravidelně: tvrdé dřevo odolá dopadům a kovová branka vydrží víc sezón. Hodí se i vozík nebo stojan, který udržuje díly pohromadě.</p>'
          '<ul><li><strong>Počet hráčů:</strong> sady pro čtyři a šest hráčů se liší počtem koulí a kladívek. Nákup pro šest se vyplatí, pokud hrajete s širší rodinou.</li>'
          '<li><strong>Průměr koulí:</strong> náhradní koule se prodávají v rozměrech, třeba 90 mm. Před nákupem změřte stávající.</li>'
          '<li><strong>Branky:</strong> robustní kovové vydrží i na tvrdém povrchu, tenké plastové se zlomí na kameni.</li>'
          '<li><strong>Úložný vozík:</strong> chrání před ztrátou kousků a usnadňuje přepravu na chalupu nebo do kempu.</li></ul>'
          '<h2>Pétanque a koulená: materiál a váha koulí</h2>'
          '<p>Pétanque je hra, která stojí na rovnováze vhozu a přesnosti. Zájemce o vážný sport hledá kovové koule s předepsanou hmotností a rýhováním, rekreační hráč sáhne po plastové nebo lehčí sadě, kterou unese i dítě. Sada obvykle obsahuje tři, čtyři, šest nebo osm koulí a malou kuličku zvanou jack nebo prasátko, která slouží jako cíl. U některých značek, třeba Obut, je pétanque dlouhá tradice, jiné nabízejí cenově nenáročné rekreační sady.</p>'
          '<ul><li><strong>Kovové koule:</strong> těžší, přesnější, vhodné na štěrk a hlínu, hlasitější při dopadu.</li>'
          '<li><strong>Plastové koule:</strong> lehké, tiché, skvělé na pláž, ale nepřesné ve větru.</li>'
          '<li><strong>Měkké koule:</strong> určené pro nejmenší nebo na hru v bytě a na terase, nepoškozují dlažbu.</li>'
          '<li><strong>Kruh na pétanque:</strong> skládací kruh vymezí hrací pole a pomáhá s měřením vzdálenosti.</li>'
          '<li><strong>Měřicí pásmo:</strong> při těsném výsledku se hodí, protože rozhodnout okem často nejde.</li></ul>'
          '<h2>Boccia a podobné hry</h2>'
          '<p>Boccia vychází z podobných pravidel, ale hraje se většinou na pevném rovném povrchu. Výhodou jsou měkké koule, které se snadno uchopí a nezpůsobují zranění. Hodí se pro děti, seniory a skupiny, kde jsou rozdíly ve fyzické zdatnosti, protože v ní rozhoduje cit, ne síla. Modely s dvanácti koulemi dvou barev pojmou dvě družstva. Pro dlouhodobé hraní zvolte povrchovou úpravu, která odolá oděru.</p>'
          '<h2>Soft tenis a míčové hry bez sítě</h2>'
          '<p>Soft tenis se hraje lehkými raketami a měkkými míčky, které se při dopadu nemrští tak daleko. Hodí se na zahradu, pláž nebo do úzké ulice, protože se míček nedostane k sousedům. Sady většinou obsahují dvě rakety a jeden až tři míčky. Náhradní míčky se dají koupit samostatně, což se vyplatí, protože se ztrácejí v křoví. Pokud děti vyrostou ze soft tenisu, přejdou na skutečné <a href="/tenisove-rakety/">tenisové rakety</a> nebo <a href="/badminton/">badminton</a>.</p>'
          '<h2>Výběr podle věku</h2>'
          '<ul><li><strong>Děti do pěti let:</strong> měkké a lehké hry bez ostrých hran, nejlépe z plastu nebo látky. Ty nejmenší baví hlavně házení a chytání.</li>'
          '<li><strong>Školní věk:</strong> kroket s kratšími kladívky, soft tenis, fotbalový kroket a boccia. Hra už má pravidla, ale pořád má být kratší.</li>'
          '<li><strong>Teenageři:</strong> pétanque a vyšší úrovně krocketu, kde se hraje o přesnost a taktiku.</li>'
          '<li><strong>Dospělí a senioři:</strong> kvalitní kovové koule a dřevěný kroket, pro seniory boccia.</li>'
          '<li><strong>Smíšené skupiny:</strong> hry bez nutnosti síly, kde mají šanci všichni, třeba kroket nebo boccia.</li></ul>'
          '<h2>Povrch a prostor</h2>'
          '<p>Trávník by měl být posekaný a rovný, jinak koule uvíznou a kroket ztratí smysl. Na štěrku se výborně hraje pétanque, ale kroket tam ničí kladívka. Na pláži se hodí lehké plastové sady a míčky, ale kovové koule se zabořují. Před nákupem si proto promyslete, kde hra skončí většinu času. Pokud sdílíte hřiště s jinými, například ve společné zahradě nebo kempu, počítejte s rozměry kroketového hřiště, které je obvykle větší než dvacet metrů na deset.</p>'
          '<h2>Bezpečnost a pravidla fair play</h2>'
          '<p>Kladívka a těžké koule patří mezi nejčastější příčiny drobných zranění. Dětem proto vysvětlete základní pravidla: nikdo nestojí před hrajícím, kladívko se nezvedá nad kolena a koule se neházejí směrem k lidem. Při hře s kovovými koulemi je dobré mít pevnější boty. Pro hlučnější kolektivy se hodí jasné domluvené časy hry, aby hra nerušila sousedy. Hry se hrají nejlépe, když se obě strany předem domluví na pravidlech, jinak vznikají spory o to, zda koule v poli ještě platí.</p>'
          '<h2>Péče, uložení a náhradní díly</h2>'
          '<p>Dřevěné díly krocketu po sezóně otřete a nechte oschnout, nikdy je neskladujte venku. Kovové koule pétanque po dešti osušte, aby nerezavěly, a plastové omyjte vodou. Soft tenisové míčky se časem deformují a ztrácejí pružnost, takže se hodí zásoba. Mnohé díly se prodávají jednotlivě: náhradní koule krocketu, jack k pétanque nebo míčky. U kvalitních sad se vyplatí koupit náhradu, než kupovat celou sadu znovu. Dlouhodobé uložení v původním vozíku nebo pouzdru chrání před ztrátou.</p>'
          '<h2>Co dalšího si vzít na zahradu a pláž</h2>'
          '<p>K odpolednu na zahradě patří <a href="/hamaky/">hamaka</a> na odpočinek, <a href="/nafukovaci-hracky/">nafukovací hračky</a> pro děti a <a href="/lahve-a-termosky/">láhve a termosky</a> s pitím. Na pláži se hodí <a href="/plazove-doplnky/">plážové doplňky</a> a ochrana před sluncem, třeba <a href="/pop-up-a-plazove-stany/">pop-up plážový stan</a>. Pro sportovnější odpoledne se doporučuje <a href="/badminton/">badminton</a>, <a href="/volejbal/">volejbal</a> nebo <a href="/trampoliny/">trampolína</a>. Rodinný výlet do kempu doplní <a href="/kemping/">kempingové vybavení</a>.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Největší část nabídky tvoří krocket a pétanque. Značka Lucio Londero nabízí krocketové sady pro čtyři i šest hráčů a náhradní koule, Geologic a Master jsou zastoupeny hlavně pétanque, Koodza a Decathlon rekreačními sadami, Sedco soft tenisem, kroketem a koulenou. Obut je známý kovovými koulemi. Dále tu najdete boccii Handilife, hru Gabaky, fotbalový kroket BS Toys, míčky Mondo a dětské sady Kensis. Kategorie obsahuje i drobnosti typu skládací kruh na pétanque nebo sada jackových kuliček. Pro míčové sporty s hřištěm vyberte raději <a href="/micove-sporty/">míčové sporty</a>.</p>'
          '<h2>Jak hru rozjet na oslavě nebo na chalupě</h2>'
          '<p>Při větší společnosti se osvědčí rozdělení do družstev a krátký turnaj. Kroket se dá hrát na několik kol a vítěz postupuje, pétanque funguje jako vyřazovací soutěž, kde se zápasy hrají do předem dohodnutého počtu bodů. Dětem pomůže, když mají vlastní menší hřiště s kratší dráhou, aby nečekaly dlouho na řadu. Stolek s pitím, stín a dostatek prostoru kolem hřiště jsou stejně důležité jako sada samotná. Před začátkem prohlédněte trávník, odstraňte kameny a větve a vyznačte hrací plochu provazem nebo kolíky.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě těžkých kovových koulí pro malé děti.</li>'
          '<li>Výběr plastové sady na štěrk nebo do větru.</li>'
          '<li>Nezjištění počtu hráčů, takže kroket pro čtyři nestačí na šest.</li>'
          '<li>Skladování dřevěné sady venku v dešti.</li>'
          '<li>Nepočítání s rozměrem hřiště a překážkami, jako jsou záhony.</li>'
          '<li>Zapomenutí na náhradní míčky nebo jack.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>U každého produktu vidíte nabídky obchodů a můžete porovnat, co sada skutečně obsahuje. Čtěte popis počtu koulí, jejich průměru a materiálu a zda je součástí vozík nebo pouzdro. Zahradní hry jsou výrazně sezónní, a proto na konci léta bývá snazší najít sadu ve slevě. Nabídka je užší než u běžných sportů, takže u oblíbených sad může být dostupnost proměnlivá.</p>',
    faq=[
        ('Jakou hru vybrat pro rodinu s dětmi?', 'Kroket nebo boccia, protože v nich rozhoduje cit a každý má šanci. Pro malé děti jsou vhodné lehké plastové sady a měkké koule bez ostrých hran.'),
        ('Jaký je rozdíl mezi pétanque a koulenou?', 'Pravidla jsou stejná, protože jde o tutéž hru: házíte koule co nejblíž k malé cílové kuličce. Rozdíl je hlavně v kvalitě sady, soutěžní kovové koule jsou přesnější a dražší než levné rekreační.'),
        ('Na jakém povrchu se hraje pétanque?', 'Nejlépe na štěrku, udusané hlíně nebo tvrdém písku. Na trávníku se koule špatně kutálejí a na měkkém písku se zabořují, proto se tam hodí lehčí plastové sady.'),
        ('Kolik hráčů potřebuje kroket?', 'Základní sady jsou pro čtyři, větší pro šest hráčů. Menší počet hráčů hrát může tak, že každý používá dvě koule, což ale prodlužuje hru.'),
        ('Dají se koupit náhradní koule?', 'Ano, náhradní koule krocketu se prodávají v rozměrech jako 90 mm a v jednotlivých barvách. Před nákupem změřte průměr stávajících koulí, aby sedly.'),
        ('Je kroket vhodný pro malé děti?', 'Ano, v lehčí verzi s krátkými kladívky a plastovými koulemi. Dohlédněte na bezpečný odstup, protože kladívko může při neopatrném zamáchnutí zranit.'),
        ('Čím se liší boccia od pétanque?', 'Boccia se hraje většinou na rovném pevném povrchu a s měkčími koulemi, takže je klidnější a bezpečnější. Pétanque má tvrdší koule a hraje se na štěrku nebo hlíně.'),
        ('Jak pečovat o dřevěný kroket?', 'Po hře ho otřete, nechte oschnout a uložte v suchu. Na dřevě se nesmí držet vlhkost, aby nenabobtnalo a neprasklo. Kovové části občas ošetřete a zkontrolujte.'),
        ('Co je Gabaky?', 'Je to zahradní hra s házením, kterou nabídka označuje jako hru pro děti. Hodí se na trávník a pláž a pravidla se u různých sad mohou lišit, proto si před nákupem přečtěte popis konkrétního produktu, kde je obsah sady a doporučený věk.'),
        ('Mohu hry použít na pláži?', 'Ano, vyberte lehké plastové sady a měkké míčky. Kovové koule se v písku zabořují a kroket vyžaduje rovný pevný povrch, takže na pláži moc nefunguje.'),
    ],
)

# ------------------------------------------------------------------ hokejove-suveniry-a-karty
NEW['hokejove-suveniry-a-karty'] = dict(long=True,
    title='Hokejové karty a suvenýry: Upper Deck, obaly, minipucky',
    desc='Hokejové sběratelské karty NHL, obaly a alba, minipucky, figurky a fanouškovské suvenýry. Jak vybrat balíčky, ochranu karet a porovnat obchody.',
    intro='<p>Hokejové karty a fanouškovské suvenýry spojuje to, že nejsou výstroj, ale radost ze hry a sbírání. Sběratel hledá nový ročník s oblíbeným hráčem, fanoušek dárek s logem týmu a rodič malý minipuk pro dítě. Sporteka porovnává nabídky českých obchodů u balíčků a boxů karet NHL, ochranných obalů, alb a toploaderů, figurek, přívěšků a mini hokejových sad. Výběr je určen sběratelům i fanouškům, kteří hledají dárek nebo si chtějí doplnit sbírku.</p>'
          '<p>Zastoupené značky jsou ' + B(('upper-deck', 'Upper Deck'), ('ultra-pro', 'Ultra PRO'), ('inglasco', 'Inglasco'), ('mcfarlane', 'McFarlane'), ('fansarena', 'FansArena'), ('strida-sport', 'Střída Sport'), ('ccm', 'CCM'), ('bauer', 'Bauer')) +
          '. K hokejovému světu patří i <a href="/hokej/">hokej</a>, <a href="/hokejove-dresy-a-obleceni/">dresy</a>, <a href="/hokejove-puky-a-branky/">puky a branky</a> a <a href="/hokejky/">hokejky</a>.</p>',
    guide='<h2>Co všechno kategorie obsahuje</h2>'
          '<p>Zboží se dá rozdělit na tři světy, které se překrývají jen částečně: sběratelské karty, ochrana a uložení karet, fanouškovské předměty. Každý má jiné nároky a jiného kupce.</p>'
          + T(['Skupina', 'Příklady', 'Pro koho'], [
              ['Hobby boxy a balíčky karet', 'ročníkové edice NHL od Upper Deck', 'sběratelé a otevírači balíčků'],
              ['Ochrana karet', 'měkké obaly, toploadery, folie do alba', 'každý sběratel'],
              ['Alba a krabičky', 'alba na karty, krabice na stovky karet', 'uspořádání sbírky'],
              ['Minipucky a přívěšky', 'klubové a reprezentační přívěšky, fanouškovské pucky', 'dárky a fanoušci'],
              ['Figurky', 'hokejisté v poloze akce, Igráček', 'sběratelé, děti, dárek'],
              ['Mini hokejové sady', 'branky, puk a hokejky v malém', 'pokojová hra a dětský pokoj'],
              ['Kuchyňské a kancelářské suvenýry', 'hrnky s logem NHL klubu', 'dárek a fanoušek']]) +
          '<h2>Sběratelské karty: balíček, hobby box a ročník</h2>'
          '<p>Karty NHL se prodávají v balíčcích, ve větších hobby boxech a v kolekcích zaměřených na konkrétní téma. Hobby box obsahuje několik balíčků, ve kterých jsou základní karty a jedna nebo více zvláštních, například s podpisem nebo kusem dresu. Co přesně uvnitř je, vždy určuje výrobce a nelze to předem zaručit. Při koupi jde tedy o hru náhody, a to i u dražších produktů.</p>'
          '<p>Ročník se označuje roky sezóny, například 2024-25 nebo 2025-26. Série vycházejí postupně, začínají obvykle Series 1, pak Series 2 a doplňkové edice, jako Allure, SP, SPx, Artifacts, Parkhurst nebo MVP. Každá edice má vlastní design, rozsah karet a zaměření. Sběratelé volí podle toho, co sbírají: všechny hráče týmu, jednoho hráče, nováčky nebo kompletní set ročníku.</p>'
          '<ul><li><strong>Balíček:</strong> menší nákup na zkoušku nebo dárek.</li>'
          '<li><strong>Hobby box:</strong> pro sběratele, kteří chtějí větší šanci na speciální karty a rádi otvírají.</li>'
          '<li><strong>Kolekce a setové edice:</strong> zaměřené na hráče nebo tým, třeba kolekce Connora Bedarda nebo edice k výročí klubů.</li>'
          '<li><strong>Doplnění sbírky:</strong> při hledání konkrétních karet často pomůže výměna nebo nákup jednotlivých kusů u specializovaných prodejců.</li></ul>'
          '<h2>Značky karet a doplňků</h2>'
          '<p>Většinu karet vydává Upper Deck, licenční partner NHL. Doplňky na ochranu karet vyrábí převážně Ultra PRO, což je široce používaná značka obalů, toploaderů a alb. Suvenýry NHL klubů nabízí Inglasco, figurky McFarlane a minipucky či přívěšky české značky Střída Sport a FansArena. V nabídce se objeví i drobné mini hokejové sady CCM a Bauer.</p>'
          '<h2>Ochrana karet: obaly, toploadery, folie</h2>'
          '<p>Karta je křehká. Ohnutý roh, otisk prstu nebo škrábnutí sníží její sběratelskou hodnotu i radost z ní, a proto je ochrana stejně důležitá jako samotná karta. Nejlevnější úroveň ochrany jsou měkké obaly, takzvané soft sleeves, do kterých se karta zasune. Pevnější ochranu poskytují toploadery, tvrdé plastové kapsy, které karta neohnou. Pro kartu s kusem dresu nebo silnější materiálem se prodávají toploadery s vyšším číslem tloušťky, například 120 nebo 180 pt.</p>'
          '<ul><li><strong>Měkké obaly (sleeves):</strong> základ pro každou kartu, které se dají vložit do alba nebo krabice.</li>'
          '<li><strong>Toploader:</strong> pevný obal na cennější kus, volte tloušťku podle karty. Označení pt udává tloušťku materiálu v tisícinách palce.</li>'
          '<li><strong>Folie do alba:</strong> listy s kapsami, nejčastěji po devíti kartách, které se vkládají do kroužkového alba.</li>'
          '<li><strong>Opakovaně uzavíratelné sáčky:</strong> chrání před prachem při přepravě a výměně.</li>'
          '<li><strong>Krabičky na sto a více karet:</strong> vhodné pro opakované karty a doplňování sbírky.</li></ul>'
          '<p>Přesný postup: kartu nejdříve vložte do měkkého obalu a poté do toploaderu. Tím zabráníte škrábancům o plast. Udržujte karty mimo přímé slunce, vlhkost a extrémní teploty.</p>'
          '<h2>Alba a uspořádání sbírky</h2>'
          '<p>Sbírka karet roste rychle a bez systému se v ní nedá vyznat. Album je nejlepší způsob, jak mít přehled a zároveň karty ukázat. Stránky s devíti kapsami nabízejí nejběžnější formát, ale pro silnější karty existují i jiné. Ukládejte je tak, aby se nehromadily jedna na druhé, a při zasouvání buďte opatrní, aby nevznikaly rohy. Klasické a pevné krabičky se hodí pro duplicity a sady, které neotevíráte.</p>'
          '<ul><li>Řaďte podle týmu, hráče nebo ročníku, podle toho, co sbíráte.</li>'
          '<li>Cennější karty držte v toploaderech v samostatné krabici.</li>'
          '<li>Album stavte do svislé polohy, ne naležato, aby se stránky neprohýbaly.</li>'
          '<li>Seznam sbírky si vedete v tabulce nebo aplikaci, aby se karty nekupovaly dvakrát.</li></ul>'
          '<h2>Minipucky, přívěšky a figurky</h2>'
          '<p>Minipuk je zmenšená kopie hokejového puku, často s logem klubu, hráče nebo turnaje. Výborně poslouží jako přívěsek na klíče, dekorace nebo malý dárek. V nabídce jsou přívěšky českého lva a mistrovství světa, hráčské přívěšky a licencované fanouškovské pucky NHL. Figurky McFarlane znázorňují hráče v typickém postoji, mají podstavec a bývají určené sběratelům. Drobné díly nejsou vhodné pro děti mladší, než uvádí výrobce, a hrozí jejich spolknutí, proto sledujte upozornění na věk na obalu.</p>'
          '<h2>Mini hokejové sady a domácí hra</h2>'
          '<p>Mini hokejová sada obsahuje branky, puk a malé hokejky pro hru na stole, koberci nebo v dětském pokoji. Zahrnuje obvykle kluby NHL, takže dítě si vybere oblíbený tým. Výhodou je, že hra nevyžaduje led a nenapáchá škody. Pokud dítě začíná s hokejem skutečně, hodí se spíš <a href="/hokejove-puky-a-branky/">puky, branky a tréninkové pomůcky</a> a <a href="/hokejky/">dětské hokejky</a>.</p>'
          '<h2>Dárek pro hokejového fanouška</h2>'
          '<p>Hokejový dárek má největší úspěch, když zasáhne správný tým a správnou generaci. Zjistěte, který klub nebo hráče obdarovaný sleduje, a podle toho vyberte hrnek, přívěšek nebo balíček karet. Pro sběratele je ideální doplněk k jeho sbírce, třeba album nebo toploadery. Dětem nejvíc udělá radost figurka nebo mini sada. Pro dospělého fanouška, který hraje, zvolte praktický dárek z kategorie <a href="/hokejove-pasky-a-doplnky/">hokejové pásky a doplňky</a> nebo <a href="/hokejove-tasky/">hokejová taška</a>.</p>'
          '<h2>Sezóna, výročí a reprezentace</h2>'
          '<p>Nabídka se mění s hokejovým kalendářem. Na začátku sezóny přicházejí nové série karet, během play-off a po mistrovství světa roste zájem o přívěšky a figurky reprezentantů. Výroční edice klubů a zvláštní kolekce vycházejí v omezeném množství, takže se rychleji vyprodají. Pokud hledáte konkrétní edici, sledujte dostupnost u více obchodů najednou.</p>'
          '<h2>Jak nakupovat karty rozumně</h2>'
          '<ul><li>Stanovte si rozpočet předem, protože otvírání balíčků může svádět k dalším nákupům.</li>'
          '<li>Ověřte sezónu a edici, aby nedošlo k záměně s podobným produktem.</li>'
          '<li>Sledujte, zda jde o hobby balíček, nebo jiný formát, protože obsah se liší.</li>'
          '<li>Počítejte s ochranou karet, jinak se hodnota snižuje.</li>'
          '<li>Karty berte jako zábavu. Hodnota se může měnit a nic nezaručuje.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Přibližně polovinu nabídky tvoří Upper Deck: hobby boxy a balíčky edic MVP, Allure, SP, SPx, Parkhurst, Artifacts, Series 1 i centenniálních edic klubů jako Detroit Red Wings nebo New York Rangers. Ultra PRO doplňuje obaly, toploadery, folie a alba. Inglasco nabízí hrnky, fanouškovské pucky a autogramiádní blistry klubů. McFarlane přidává figurky hráčů reprezentace Kanady a Igráček přináší figurku fanynky z MS. Najdete tu také minipucky, přívěšky na klíče a mini hokejové sady klubů NHL. Pokud sbíráte jiné věci, mrkněte i do kategorií <a href="/volny-cas/">hry a volný čas</a> a <a href="/dresy/">dresy</a>.</p>'
          '<h2>Jak začít sbírat hokejové karty</h2>'
          '<p>Nejprve si ujasněte, co chcete sbírat. Může to být oblíbený tým, jeden hráč, nováčci, reprezentace nebo kompletní set z jednoho ročníku. Bez cíle se sbírka rozpadá do nahodilých kusů. Pak si pořiďte základní ochranu, tedy měkké obaly, pár toploaderů a album, a teprve potom kupujte karty. Mnoho sběratelů začíná jedním nebo dvěma balíčky, zjišťuje, co je baví, a až potom přechází na hobby boxy. Dobře funguje i výměna s dalšími sběrateli, protože duplicity v jedné sbírce bývají chybějícím kouskem v jiné.</p>'
          '<p>Důležité je také seznámit se s pojmy. Základní karta je běžná karta setu, vložená karta je vzácnější a obvykle se týká zvláštní série. Nováček neboli rookie je karta hráče z jeho první sezóny. Autogramová karta nese podpis hráče a karta s kusem dresu obsahuje malý kousek materiálu. Přesný význam pojmů se může u jednotlivých edic mírně lišit, proto si přečtěte popis produktu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Dotyky holou rukou na plochu karty, vyplatí se držet za okraje.</li>'
          '<li>Zasunutí karty rovnou do tvrdého toploaderu, aniž je v měkkém obalu.</li>'
          '<li>Nákup edice bez ověření sezóny.</li>'
          '<li>Skladování karet na slunci nebo ve vlhku.</li>'
          '<li>Očekávání, že každý balíček obsahuje vzácnou kartu.</li>'
          '<li>Nákup dětských figurek bez ohledu na doporučený věk.</li></ul>',
    faq=[
        ('Co je hobby box hokejových karet?', 'Je to větší balení se několika balíčky karet, určené sběratelům. Obvykle může obsahovat speciální karty, přesné složení ale určuje výrobce a předem se nedá zaručit.'),
        ('Co znamenají ročníky jako 2025-26?', 'Označují hokejovou sezónu, ke které se karty vztahují. Série a edice v rámci ročníku vycházejí postupně a liší se designem, rozsahem karet i zaměřením.'),
        ('Čím se liší toploader od měkkého obalu?', 'Měkký obal je tenký plastový rukáv, který chrání před prachem a škrábanci. Toploader je pevná plastová kapsa, která kartu neohne. Nejlepší ochranu dává kombinace obou.'),
        ('Co znamená označení 120 pt nebo 180 pt?', 'Jde o tloušťku karty, pro kterou je toploader určen, v tisícinách palce. Silnější karty, třeba s kusem dresu, potřebují vyšší číslo, jinak se do obalu nevejdou.'),
        ('Jak uložit sbírku karet?', 'Do alba s kapsami po devíti kartách nebo do krabiček, v suchu a mimo slunce. Cennější kusy držte v toploaderech a album skladujte ve svislé poloze.'),
        ('Jsou hokejové karty dobrá investice?', 'Ne, nemůžeme to zaručit. Hodnota karet se mění a závisí na zájmu sběratelů. Berte je jako koníčka, ne jako jistý způsob zhodnocení peněz.'),
        ('Kdo vydává karty NHL?', 'V nabídce převládá Upper Deck, který vydává edice jako Series 1, MVP, Allure, SP, SPx, Artifacts a Parkhurst. Ochranné obaly dodává hlavně Ultra PRO.'),
        ('Jaký dárek zvolit pro hokejového fanouška?', 'Záleží na jeho koníčku: sběratel ocení balíčky a ochranu karet, dítě figurku nebo mini sadu, dospělý hrnek, přívěšek nebo minipuk oblíbeného klubu.'),
        ('Jsou minipucky bezpečné pro děti?', 'Jsou to drobné předměty, takže se řiďte věkovým upozorněním výrobce. Pro nejmenší děti nejsou vhodné, hrozí spolknutí. Starším dětem a dospělým slouží jako přívěšek nebo dekorace.'),
        ('K čemu je mini hokejová sada?', 'Slouží k hraní na stole, koberci nebo v pokoji. Obsahuje malé branky, puk a hokejky, často v barvách klubu NHL. Pro skutečný trénink na ledě se nehodí.'),
    ],
)

# ------------------------------------------------------------------ discgolf
NEW['discgolf'] = dict(long=True,
    title='Discgolf a frisbee: disky, koše, startovní sady',
    desc='Discgolfové disky, koše, startovní sady, frisbee a oblečení s discgolfovým motivem. Jak vybrat podle zkušeností a síly hodu a porovnat nabídky obchodů.',
    intro='<p>Discgolf se hraje podobně jako golf, jen místo míčku a holí se používá létající disk a místo jamek kovový koš s řetězy. Cílem je dostat disk do koše na co nejméně hodů. Sport je dostupný: základní disky stojí málo a hřiště v parcích jsou zpravidla volně přístupná. Vedle toho kategorie zahrnuje klasické frisbee, bumerangy a kruhy, které se hodí na pláž a zahradu. Sporteka porovnává nabídky českých obchodů a zahrnuje startovní sady, jednotlivé disky, přenosné koše i oblečení.</p>'
          '<p>Najdete tu značky ' + B(('eleven', 'Eleven'), ('aerobie', 'Aerobie'), ('kensis', 'Kensis'), ('latitude-64', 'LATITUDE 64°'), ('merco', 'Merco'), ('eurodisc', 'Eurodisc'), ('schildkrot', 'Schildkröt'), ('westside-discs', 'Westside Discs'), ('discmania', 'Discmania')) +
          '. Související kategorie: <a href="/golf/">golf</a>, <a href="/hry-na-zahradu/">hry na zahradu</a>, <a href="/volny-cas/">hry a volný čas</a> a <a href="/lukostrelba/">lukostřelba</a>.</p>',
    guide='<h2>Jak se discgolf hraje</h2>'
          '<p>Hřiště je tvořeno drahami, na každé je odhaz a koš. Hráč odhodí disk z tee, další hod provádí z místa, kde disk přistál, a pokračuje, dokud nedojde ke koši. Počítají se hody a vyhrává ten, kdo jich potřebuje nejméně. Překážkou jsou stromy, vodní plochy a převýšení, jako v golfu. Hraje se v parcích a lesích a v Česku je řada veřejných hřišť, jejichž seznam najdete na webech hráčských komunit.</p>'
          '<p>Základní pravidla jsou jednoduchá, takže začít se dá během jedné hodiny. Důležité je ale dodržovat etiketu: před hodem se přesvědčte, že nikdo není v dráze, a respektujte ostatní návštěvníky parku.</p>'
          '<h2>Druhy disků</h2>'
          '<p>Discgolfové disky se od klasického frisbee liší tvarem hrany a rozložením váhy. Dělí se podle účelu: putter pro krátký a přesný hod, midrange pro střední vzdálenost, fairway driver a distance driver pro dlouhé hody. Čím je disk rychlejší, tím má ostřejší hranu a vyžaduje větší sílu a techniku.</p>'
          + T(['Typ disku', 'Použití', 'Pro koho'], [
              ['Putter', 'krátké a přesné hody, zakončení u koše', 'všichni, zejména začátečníci'],
              ['Midrange', 'střední vzdálenost, stabilní let', 'začátečníci i pokročilí'],
              ['Fairway driver', 'delší hody s dobrou kontrolou', 'hráči s již vyvinutou technikou'],
              ['Distance driver', 'maximální vzdálenost', 'silní a zkušení hráči'],
              ['Startovní sada', '2 až 3 disky různých typů', 'úplní začátečníci'],
              ['Mini a dětská sada', 'lehké disky a malý koš', 'děti a zahrada']]) +
          '<h2>Čísla letu</h2>'
          '<p>Většina disků nese čtyři čísla, tzv. flight numbers: rychlost, klouzavost, stabilitu při prvním letu a odchylku na konci. Na rychlost se pozor: vyšší číslo neznamená lepší disk, ale disk, který potřebuje víc síly. Začátečník s pomalejším hodem dosáhne větší vzdálenosti s disky o nízké rychlosti, protože ty nepotřebují velkou rotaci. Čísla slouží k orientaci a mezi výrobci se mohou mírně lišit, takže je berte jako přibližný průvodce.</p>'
          '<h2>Plast a váha disku</h2>'
          '<p>Disk se vyrábí v různých plastech. Základní plasty jsou levnější a rychleji se otřepou, prémiové vydrží déle a jejich let se mění pomaleji. Některé plasty jsou měkčí a lépe drží v ruce, jiné tvrdší a odolnější. Značky mají vlastní označení plastů, třeba Opto, BioGold nebo Exo, ale princip je stejný. Hmotnost disku se uvádí v gramech a pohybuje se v určitém rozmezí. Lehčí disk je vhodnější pro děti a slabší hod, těžší stabilnější ve větru. Při nákupu přes internet sledujte, zda je uvedena konkrétní hmotnost nebo rozmezí, protože barva a hmotnost se u některých obchodů vybírají náhodně.</p>'
          '<h2>Startovní sada pro začátečníka</h2>'
          '<p>Na začátek stačí tři disky: putter, midrange a driver s nižší rychlostí. Hotové sady od značek jako Latitude 64°, Artis, Merco nebo Discmania jsou správnou volbou, protože obsahují vyvážený výběr. Rozhodně nemusíte kupovat velké množství disků. Hrát s několika se naučíte víc než s tuctem. Časem poznáte, co vám sedí, a doplníte disky podle technického stylu.</p>'
          '<ul><li>Začněte putterem, protože pro krátké hody i zakončení je nejdůležitější.</li>'
          '<li>Midrange je univerzální a odpouští chyby.</li>'
          '<li>Driver kupujte až po prvních hrách, kdy víte, jakou sílu máte.</li>'
          '<li>Vybírejte spíš lehčí disky v nižším rozsahu hmotnosti.</li></ul>'
          '<h2>Koše a trénink doma</h2>'
          '<p>Přenosný koš si můžete postavit na zahradě a trénovat přesnost. Modely pro začátečníky, například od Artis, Merco nebo Sandever, mají řetězy, které zachytí disk, a koš, do kterého spadne. Na zahradě pamatujte na bezpečnou vzdálenost a směr hodu, protože disk má ostrou hranu a letí rychle. Trénink putting se dá provádět i ve vnitřních prostorách s měkkými disky. Koše bývají rozkládací, takže se vejdou do kufru.</p>'
          '<h2>Frisbee, kruhy a bumerangy</h2>'
          '<p>Klasické frisbee, aerodynamické kruhy a bumerangy mají jiný tvar než discgolfový disk. Jsou větší, nadnášejí lépe a hodí se na hru ve dvou nebo v kolektivu na pláži či louce. Aerobie je známá kruhy Sprint, Pro, Superdisc a bumerangem Orbiter, Schildkröt nabízí měkké a neoprenové modely a Kensis a Eurodisc barevné talíře pro děti. Svítící a LED varianty prodlouží zábavu do večera. Pro děti zvolte měkké materiály, které neublíží při chycení. Dospělí ocení tuhý plastový talíř s přesným letem.</p>'
          '<ul><li><strong>Měkké frisbee:</strong> pro děti a začátečníky, bezpečné.</li>'
          '<li><strong>Tvrdý talíř:</strong> přesný let, vhodný pro dospělé.</li>'
          '<li><strong>Kruh:</strong> dlouhý dolet, hodí se na pláž a louku.</li>'
          '<li><strong>Bumerang:</strong> vyžaduje trochu cviku, ale vrací se.</li>'
          '<li><strong>Svítící varianty:</strong> večerní hra, kempování.</li></ul>'
          '<h2>Technika hodu</h2>'
          '<p>Nejběžnější hod je zadní (backhand), při kterém se disk drží palcem nahoře a prsty pod okrajem. Tělo se otáčí a disk se pouští v úrovni pasu s dostatečnou rotací. Hlavní zásada je, aby disk letěl plochý a rotoval, jinak se kymácí. Druhým základním hodem je forehand, kterým se disk vrhá bočním pohybem zápěstí. Začátečníci by se měli soustředit na čistý a plynulý pohyb, ne na sílu. Při rozcvičce se prohřejte rameno a zápěstí, protože agresivní hody bez přípravy způsobují přetížení.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Hraje se venku a často v lese, takže se hodí pohodlná sportovní obuv, funkční oblečení a v zimě teplejší vrstvy. V kategorii najdete i oblečení značky Eleven s discgolfovými motivy: trička, kalhoty a ponožky. Důležité je i příslušenství: marker neboli malý disk, kterým označíte místo dopadu, ručník na utření disků, taška nebo batoh na disky a podložka. Pro výběr oblečení pokračujte do kategorií <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> nebo <a href="/trekova-obuv/">trekovou obuv</a>. Disky se dají nést i v <a href="/batohy/">batohu</a> a <a href="/sportovni-tasky/">sportovní tašce</a>.</p>'
          '<h2>Péče o disky</h2>'
          '<ul><li>Po hře disk otřete od bláta a trávy, případně opláchněte vlažnou vodou.</li>'
          '<li>Neskladujte ho na slunci nebo v horkém autě, plast se deformuje.</li>'
          '<li>Vyvarujte se hodů do kamenů a asfaltu, hrana se zničí.</li>'
          '<li>Opotřebovaný disk se nevyhazuje: lze ho použít pro trénink nebo pro jiný typ letu.</li>'
          '<li>Nezapomínejte, že každý disk po čase změní let, i když to vypadá stejně.</li></ul>'
          '<h2>Disky pro různou sílu hodu</h2>'
          '<p>Slabší nebo mladší hráč dosáhne větší vzdálenosti s lehčím diskem s nízkou rychlostí než s těžkým driverem. Silnější hráč naopak potřebuje stabilnější disk, který se při velké rotaci nepřevrací. Proto se doporučuje začínat s disky, které letí předvídatelně rovně, a až poté zkoušet disky s výraznou křivkou. Vítr změní let každého disku, a tak se vyplatí mít v tašce několik variant pro různé podmínky.</p>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Úplný začátečník:</strong> startovní sada s putterem, midrangem a nízkorychlostním driverem.</li>'
          '<li><strong>Děti:</strong> měkké a lehké disky nebo zahradní mini discgolf set s košem.</li>'
          '<li><strong>Pokročilý hráč:</strong> specializované disky od Latitude 64°, Westside Discs nebo Discmania podle stylu.</li>'
          '<li><strong>Rodinný výlet:</strong> frisbee nebo kruh a měkký disk na pláž.</li>'
          '<li><strong>Dárek:</strong> sada disků nebo oblečení s discgolfovým motivem.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Největší část tvoří oblečení Eleven s motivem discgolfu a disky Latitude 64° (putter Pure, midrange Pearl a Fuse, fairway River). Aerobie nabízí kruhy a bumerangy, Westside Discs a Discmania další discgolfové disky, Artis a Merco sady disků a koše. Kensis, Schildkröt, Eurodisc, Nerf a Olaian doplňují volnočasové létající talíře a kruhy. Najdete tu i markery a zahradní discgolfové sady pro děti. Pokud vás zajímá trénink přesnosti, podívejte se také na <a href="/sipky/">šipky</a> nebo <a href="/lukostrelba/">lukostřelbu</a>.</p>'
          '<h2>Kde hrát a jak se připravit na první kolo</h2>'
          '<p>První hru si zkuste na jednoduché dráze s krátkými vzdálenostmi, kde se učíte spíš cit pro disk než sílu. Vezměte si vodu, malý ručník, marker a pár disků. Před hrou si prostudujte plánek hřiště: u každé dráhy bývá uvedena délka a doporučený postup. Většina hráčů je vstřícná a radí začátečníkům, takže se nebojte zeptat. Pamatujte na úklid, nic nenechávejte v přírodě a respektujte pravidla parku, třeba časová omezení a ochranu zvěře.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Nákup rychlého driveru pro začátečníka, který ho neumí vrhnout.</li>'
          '<li>Příliš velký počet disků na začátku.</li>'
          '<li>Záměna klasického frisbee s discgolfovým diskem, které se liší hranou a letem.</li>'
          '<li>Házení v místech, kde mohou projít lidé nebo psi.</li>'
          '<li>Skladování disků v horku.</li>'
          '<li>Ignorování hmotnosti, která u dětí a slabších hráčů rozhoduje.</li></ul>',
    faq=[
        ('Co je discgolf?', 'Je to sport podobný golfu, kde se házejí létající disky do kovového koše s řetězy. Vyhrává hráč, který potřebuje nejméně hodů. Hraje se v parcích a lesích.'),
        ('Čím se liší discgolfový disk od frisbee?', 'Má ostřejší hranu, užší tvar a váhu rozloženou na okraji, takže letí rychleji a přesněji. Klasické frisbee je větší a nadnáší lépe, hodí se na pláž a hru ve dvou.'),
        ('Jaké disky koupit na začátek?', 'Putter, midrange a nízkorychlostní driver, nejlépe v hotové startovní sadě. Pro začátek jsou vhodné spíše lehčí disky, protože se lépe ovládají.'),
        ('Co znamenají čísla na disku?', 'Čtyři čísla popisují rychlost, klouzavost, stabilitu a odchylku na konci letu. Slouží k orientaci a mezi výrobci se mohou mírně lišit, nejde o míru kvality disku.'),
        ('Potřebuji koš na trénink doma?', 'Není nutný, ale pomáhá s přesností, zvlášť s hody z blízka. Můžete začít i s jednoduchým košem pro začátečníky nebo zahradní sadou, a hrát pak na veřejném hřišti.'),
        ('Jaký plast disku vybrat?', 'Základní plasty jsou levnější a rychleji se opotřebují, prémiové vydrží déle. Začátečníkovi stačí levnější, protože disky stejně často padají do trávy a do křoví.'),
        ('Mohou discgolf hrát děti?', 'Ano, s lehkými a měkkými disky a menším košem. Dohlédněte na bezpečnou vzdálenost ostatních a směr hodu, protože i lehký disk může při dopadu zranit.'),
        ('Jak disky ošetřovat?', 'Po hře je otřete nebo opláchněte, neskladujte je v horku a nehazujte do kamenů. Plast se při horku může deformovat a změní se tím let.'),
        ('K čemu je marker?', 'Je to malý disk, kterým označíte místo, kde váš disk přistál. Hodí se při hře ve skupině, aby se místo nezaměnilo, a při měření vzdálenosti ke koši.'),
        ('Hodí se frisbee do vody nebo na pláž?', 'Ano, měkké a neoprenové modely jsou vhodné na pláž i do vody. Svítící a LED varianty prodlouží hru do večera, tvrdý plastový talíř je lepší pro přesný let.'),
    ],
)
