"""sporteka.cz — wave 28b (16. 11. 2026): long texts for softshellove-kalhoty, jednodilne-plavky, dvoudilne-plavky, kompresni-ponozky.
General true facts only, no prices, no product counts. Softshell: membrane vs. non-membrane, water column only for membrane fabrics.
Compression: sport compression is not a medical device, medical stockings belong to a doctor and pharmacy; no health promises.
Brands linked only if present in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ softshellove-kalhoty
NEW['softshellove-kalhoty'] = dict(long=True,
    title='Softshellové kalhoty: pánské, dámské i dětské',
    desc='Softshellové kalhoty pánské, dámské i dětské, s membránou i bez, zateplené fleecem. Jak vybrat podle počasí a jak prát; nabídky českých e-shopů.',
    intro='<p><strong>Softshellové kalhoty</strong> jsou z pružné tkaniny, která zastaví vítr, odpudí slabý déšť a sníh a přitom dobře odvádí teplo a vlhkost z těla. Stojí mezi lehkými turistickými kalhotami a nepromokavými kalhotami s membránou: nepromoknou do první přeháňky, ale ani se v nich člověk nezapaří při stoupání. Proto je mají rádi turisté, skialpinisté, běžkaři i rodiče malých dětí, pro které jsou dětské softshellové kalhoty základem oblečení do školky od podzimu do jara.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů a nakoupíte přímo v e-shopu, který si zvolíte. V katalogu najdete pánské, dámské i dětské modely značek ' + B(('dynafit', 'Dynafit'), ('husky', 'Husky'), ('regatta', 'Regatta'), ('northfinder', 'Northfinder')) + ', Salewa, Trimm a u dětí například Lewro nebo Etape. Nadřazenou kategorií jsou <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, ke kalhotám se hodí <a href="/softshellove-bundy/">softshellové bundy</a>.</p>',
    guide='<h2>Co je softshell</h2>'
          '<p>Softshell je tkaná látka s příměsí elastanu, takže se natahuje a nepřekáží při vysokém kroku. Na povrchu je hustě tkaná a ošetřená vodoodpudivou úpravou, zkráceně DWR, po které voda steče v kapkách. Rubová strana bývá hladká u letních modelů, nebo počesaná do jemného fleecu u zimních. Část softshellů je dvouvrstvá, další třívrstvá s membránou uprostřed. Společné mají to, že jsou měkčí, tišší a pružnější než nepromokavé kalhoty, kterým se říká hardshell.</p>'
          '<p>Důležité je vědět, co softshell neumí. Vodoodpudivá úprava zvládne sníh, mrholení a krátkou přeháňku, při dlouhém dešti ale látka postupně nasákne. Na celodenní déšť patří nepromokavé kalhoty s membránou a podlepenými švy, případně pláštěnka. Softshell je oblečení na pohyb v proměnlivém počasí, ne na sezení v lijáku.</p>'
          '<h2>S membránou, nebo bez</h2>'
          + T(['Druh', 'Vlastnosti', 'Kdy se hodí'], [
              ['Bez membrány', 'nejlépe dýchá, vítr částečně zbrzdí, rychle schne', 'turistika a skialp při stoupání, běžky, aktivní pohyb'],
              ['S větruodolnou membránou', 'vítr nepropustí, dýchá o něco méně', 'hřebeny, vítr, zima při mírnějším tempu'],
              ['S membránou a vodním sloupcem', 'vydrží delší déšť, pořád pružná', 'proměnlivé počasí, děti na hřišti'],
              ['Zateplený fleecem', 'hřeje, často s membránou', 'zima, procházky, školka, práce venku'],
              ['Lehký letní softshell', 'tenký, bez zateplení', 'jaro, léto na horách, lezení']]) +
          '<p>Membrána je tenká fólie uvnitř látky, která propustí vodní páru zevnitř, ale ne vodu zvenku. Teprve u membránových softshellů dává smysl údaj o <strong>vodním sloupci</strong> v milimetrech, například 5000 nebo 10 000 mm. Říká, jak vysoký sloupec vody látka v laboratoři vydrží, než propustí kapky. Prodyšnost se uvádí v gramech vodní páry na metr čtvereční za den. U softshellu bez membrány vodní sloupec neuvádějte za rozhodující parametr; tam rozhoduje hustota tkaniny a kvalita úpravy DWR. Švy softshellových kalhot obvykle podlepené nejsou, takže i membránový model není nepromokavý v pravém slova smyslu.</p>'
          '<h2>Zateplené, nebo letní</h2>'
          '<p>Zateplené softshellové kalhoty mají na rubu počesaný fleece nebo mřížkovou strukturu, která drží teplý vzduch u těla. Nosí se na zimní procházky, na sáňkování, k práci venku nebo na pomalejší turistiku. Při rychlém stoupání do kopce ale mohou být až příliš teplé. Letní a celoroční softshell je tenký, lehký a nezateplený, hodí se na túry, lezení a ferraty od jara do podzimu. V zimě ho skialpinisté a běžkaři nosí s tenkým <a href="/termopradlo/">termoprádlem</a> pod ním, protože při výstupu se hřeje pohybem.</p>'
          '<h2>Dětské softshellové kalhoty</h2>'
          '<p>Dětské softshellové kalhoty jsou v Česku jedním z nejčastějších kusů oblečení do školky. Dítě v nich proleze hřiště, sedne si na mokrou lavičku a sjede skluzavku, a kalhoty vydrží. Na co se dívat:</p>'
          '<ul><li><strong>Zateplení:</strong> fleecová podšívka na podzim a zimu, tenká varianta na jaro a teplejší dny.</li>'
          '<li><strong>Zesílená kolena a sedací část:</strong> právě tam se kalhoty nejdřív prodřou.</li>'
          '<li><strong>Nastavitelný pas:</strong> knoflíková guma uvnitř pasu nebo odepínací kšandy, aby kalhoty vydržely víc než jednu sezónu.</li>'
          '<li><strong>Gumička pod chodidlo:</strong> drží nohavici v botě a nepustí sníh dovnitř.</li>'
          '<li><strong>Reflexní prvky:</strong> v listopadu a v prosinci se z venku vrací za šera.</li>'
          '<li><strong>Velikost podle výšky:</strong> značí se v centimetrech, například 104, 116 nebo 128; rezerva jedné velikosti stačí.</li></ul>'
          '<p>Do mokrého sněhu a na celodenní lyžování jsou lepší lyžařské kalhoty nebo oteplovačky s vyšším vodním sloupcem a podlepenými švy. Softshell se po hodině válení ve sněhu může na kolenou a na zadku provlhnout. Dětské lyžařské modely najdete v kategorii <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>'
          '<h2>Střih a detaily</h2>'
          '<ul><li><strong>Předtvarovaná kolena</strong> kopírují pokrčenou nohu, takže kalhoty netáhnou při výstupu.</li>'
          '<li><strong>Klínek v rozkroku</strong> přidá volnost při vysokém kroku a dřepu.</li>'
          '<li><strong>Zipy na nohavicích</strong> umožní rozšířit lem přes skialpové nebo lyžařské boty.</li>'
          '<li><strong>Zesílení na vnitřní straně lemu</strong> chrání látku před mačkami a hranami lyží.</li>'
          '<li><strong>Větrací zipy</strong> na stehnech pustí ven přebytečné teplo.</li>'
          '<li><strong>Kapsy na zip</strong> udrží mobil a klíče při pádu i v sedačce lanovky.</li>'
          '<li><strong>Integrovaný pásek nebo poutka</strong> podle toho, zda nosíte vlastní opasek nebo sedák.</li></ul>'
          '<p>Skialpové modely Dynafitu jsou přiléhavé a lehké, s dlouhými zipy na nohavicích. Turistické kalhoty Northfinderu, Husky nebo Regatty mají volnější střih a víc kapes. Při výběru si ujasněte, zda dáváte přednost nízké hmotnosti, nebo pohodlí a kapsám.</p>'
          '<h2>Pánské a dámské střihy</h2>'
          '<p>Dámské softshellové kalhoty mají užší pas a víc místa v bocích, často také vyšší pas vzadu. Pánské jsou rovnější a delší v nohavici. Řada výrobců nabízí délkové varianty short, regular a long, což ocení vysocí i drobnější lidé. Kalhoty mají v pase sedět pevně i bez pásku a při dřepu nesmí táhnout v rozkroku ani v kolenou. Nohavice by měla dosednout na botu, ale ne se pod ní shrnovat do záhybů, které se prodřou.</p>'
          '<h2>Softshell, hardshell, nebo lehké turistické kalhoty</h2>'
          '<p>Lehké turistické kalhoty z tenkého polyamidu jsou nejvzdušnější a nejrychleji schnou, proti větru a chladu ale skoro nechrání. Hodí se na léto a teplé dny. Hardshell, tedy nepromokavé kalhoty s membránou a podlepenými švy, vydrží liják i vichřici, je ale šustivý, méně pružný a při stoupání se v něm zapaříte. Softshell stojí uprostřed. Kdo chodí na hory v jedněch kalhotách od jara do podzimu, sáhne nejčastěji právě po něm a nepromokavé kalhoty nosí sbalené v batohu pro případ dlouhého deště.</p>'
          '<h2>Zimní běh a práce venku</h2>'
          '<p>Při zimním běhu ve větru a mrazu chrání softshellové kalhoty stehna a kolena, která v legínách rychle prochladnou. Běžecké modely jsou přiléhavé, s reflexními prvky a krátkým zipem u kotníku. Pro práci venku, na zahradě nebo na stavbě se hodí volnější střih s pevnějšími koleny a kapsami na nářadí. Pracovní softshell bývá těžší a odolnější, zato méně prodyšný.</p>'
          '<h2>Kde se softshellové kalhoty uplatní</h2>'
          '<p>Na <a href="/skialpinismus/">skialpinismus</a> jsou ideální, protože při výstupu se člověk zpotí a při sjezdu fouká; softshell zvládne obojí. Běžkaři ocení pružnost a malou hmotnost. Turisté je nosí od podzimu do jara v kombinaci s <a href="/vysoke-trekove-boty/">vysokými trekovými botami</a>. Myslivci, rybáři, zahradníci a lidé pracující venku je mají rádi pro odolnost a tichost. Na sjezdovku se hodí jen v suchém a mírném počasí; jinak jsou lepší lyžařské kalhoty s izolací.</p>'
          '<h2>Softshellové kalhoty pro myslivce a rybáře</h2>'
          '<p>Myslivci a rybáři potřebují kalhoty, které při pohybu nešustí a nevyplaší zvěř ani ryby. Softshell je v tom proti nepromokavým kalhotám s tvrdou membránou výrazně tišší. Modely pro ně mívají maskovací nebo olivové barvy, zesílená kolena na klečení a hluboké kapsy. Na dlouhé sezení na posedu v mrazu se pod ně obléká teplé spodní prádlo.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Softshell perte na teplotu podle štítku, obvykle 30 °C, se zapnutými zipy a suchými zipy a naruby. Použijte prací prostředek na technické oblečení nebo tekutý prostředek bez aviváže. Aviváž a práškové prostředky zanášejí membránu i vlákna a vodoodpudivá úprava pak přestane fungovat. Pokud to štítek dovoluje, krátké sušení v sušičce na nízkou teplotu úpravu DWR částečně obnoví. Když voda přestane po látce stékat a místo toho se do ní vpije, je čas na impregnaci. Prostředky na praní i obnovu najdete v kategorii <a href="/impregnace/">impregnace</a>.</p>'
          '<p>Zateplené kalhoty s fleecem uvnitř se mohou časem žmolkovat, hlavně na stehnech. Pomáhá praní naruby a oddělení od věcí se suchými zipy. Dětské kalhoty od bláta nechte nejdřív uschnout a hrubou špínu vykartáčujte, teprve pak je dejte prát.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Očekávání, že softshell vydrží celodenní déšť.</li>'
          '<li>Zateplený model na rychlou túru nebo skialp, ve kterém se člověk upotí.</li>'
          '<li>Porovnávání vodního sloupce u kalhot, které membránu nemají.</li>'
          '<li>Praní s aviváží, po kterém přestane fungovat vodoodpudivá úprava.</li>'
          '<li>Dětské kalhoty o dvě velikosti větší, ve kterých dítě zakopává.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe a hned zjistíte, kde je vaše délka a velikost skladem. Objednávku pak dokončíte v e-shopu. U dětských kalhot se vyplatí hlídat konec sezóny, kdy obchody vyprodávají starší barvy. Další možnosti pro zimu najdete v kategoriích <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>.</p>',
    faq=[
        ('Jsou softshellové kalhoty nepromokavé?', 'Ne úplně. Vodoodpudivá úprava zvládne sníh, mrholení a krátkou přeháňku, při dlouhém dešti látka nasákne. Na celodenní déšť patří nepromokavé kalhoty s membránou a podlepenými švy.'),
        ('Jaký je rozdíl mezi softshellem s membránou a bez ní?', 'Softshell bez membrány lépe dýchá a hodí se na aktivní pohyb. Membrána zastaví vítr a vydrží víc vody, ale dýchá o něco méně.'),
        ('Co znamená vodní sloupec u softshellu?', 'Jak vysoký sloupec vody látka vydrží, než propustí kapky. Má smysl jen u membránových softshellů; u ostatních rozhoduje hustota tkaniny a úprava DWR.'),
        ('Jakou velikost dětských softshellových kalhot vybrat?', 'Podle výšky dítěte v centimetrech, s rezervou nejvýš jedné velikosti. Nastavitelný pas a kšandy pomohou, aby kalhoty vydržely déle.'),
        ('Hodí se softshellové kalhoty na lyže?', 'Na skialpinismus a běžky ano. Na sjezdovku jen v suchém a mírném počasí; jinak jsou lepší lyžařské kalhoty s izolací a membránou.'),
        ('Jak prát softshellové kalhoty?', 'Na 30 °C, naruby, se zapnutými zipy, prostředkem na technické oblečení a bez aviváže. Když voda přestane stékat, obnovte impregnaci.'),
        ('Jaký je rozdíl mezi softshellem a hardshellem?', 'Softshell je pružný, dobře dýchá a odolá větru a slabému dešti. Hardshell má membránu a podlepené švy, vydrží liják, ale je méně pružný a méně prodyšný.'),
        ('Jsou zateplené softshellové kalhoty vhodné na túry?', 'Na pomalejší zimní procházky ano. Při rychlém stoupání se v nich člověk zpotí, proto je lepší nezateplený softshell s termoprádlem.'),
    ])

# ------------------------------------------------------------------ jednodilne-plavky
NEW['jednodilne-plavky'] = dict(long=True,
    title='Jednodílné plavky: dámské, sportovní i zeštíhlující',
    desc='Jednodílné plavky dámské: sportovní do bazénu, zeštíhlující, s košíčky i s nohavičkou. Materiály odolné chloru, velikost a péče, nabídky e-shopů.',
    intro='<p><strong>Jednodílné plavky</strong> drží na těle při plavání, skocích do vody i hraní s dětmi a nic se v nich neposune. Proto je volí ženy, které v bazénu opravdu plavou, ale i ty, které chtějí zakrýt břicho nebo se na pláži prostě cítí jistěji. Nabídka je široká: tenké sportovní plavky z materiálu odolného chloru, plážové modely s košíčky, zeštíhlující plavky se stahovacími panely, plavky s nohavičkou nebo s volnou sukénkou.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů, nakoupíte pak přímo v e-shopu. Najdete tu jednodílné plavky značek ' + B(('speedo', 'Speedo'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('calvin-klein', 'Calvin Klein'), ('litex', 'Litex')) + ', Arena, Chantelle, Triumph, Roxy nebo Nebbia. Kategorie patří pod <a href="/damske-plavky/">dámské plavky</a>, další druhy najdete v kategorii <a href="/plavky/">plavky</a>.</p>',
    guide='<h2>Sportovní, nebo plážové</h2>'
          '<p>Nejdůležitější rozhodnutí je, k čemu plavky budou. Sportovní plavky do bazénu jsou tenké, přiléhavé a mají zády střih, který uvolní lopatky. Plážové plavky víc řeší vzhled, tvar prsou a postavy, mají košíčky, ozdoby a pestré vzory. Jedny i druhé se dají použít na dovolené, ale plážové plavky z běžného materiálu se v chlorované vodě bazénu rychle opotřebují.</p>'
          + T(['Typ', 'Typické znaky', 'Pro koho'], [
              ['Sportovní', 'tenký pružný materiál, otevřená záda, bez košíčků', 'pravidelné plavání, kondiční bazén, aquafitness'],
              ['Plážové', 'košíčky, výraznější střih a vzory', 'dovolená, koupaliště, odpočinek'],
              ['Zeštíhlující', 'stahovací panely na bříšku, řasení, tmavší barvy', 'kdo chce opticky zpevnit postavu'],
              ['S kosticemi a košíčky', 'velikost podle podprsenky, pevná opora', 'větší prsa, plnější postavy'],
              ['S nohavičkou', 'krátká nohavice kryje horní část stehen', 'plavání, vodní sporty, kdo nechce vysoký výřez'],
              ['Se sukénkou', 'volná sukně přes spodní díl', 'odpočinek u vody, větší krytí']]) +
          '<h2>Materiál a chlor</h2>'
          '<p>Většina plavek je z polyamidu s elastanem, který se v obchodech často označuje jako lycra. Materiál je příjemný a velmi pružný, chlor ale elastan postupně rozkládá. Plavky se pak vytahají, ztratí barvu a v sedu začnou prosvítat. Kdo plave několikrát týdně, ušetří si zklamání s plavkami z polyesteru nebo PBT, které výrobci označují jako odolné chloru. Speedo je prodává pod názvem Endurance, Arena pod označením MaxLife. Jsou o něco méně pružné a na první dotek tužší, zato v bazénu vydrží výrazně déle.</p>'
          '<p>U plážových plavek hraje roli podšívka. Dobrá podšívka zabrání průsvitnosti světlých barev a zlepší tvar. Některé modely deklarují také UV ochranu tkaniny, která chrání kůži pod plavkami. Kůži mimo plavky ale musíte chránit krémem, případně UV tričkem s dlouhým rukávem, jaké najdete v kategorii <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>.</p>'
          '<h2>Střih zad a ramínek</h2>'
          '<ul><li><strong>Racerback (zápasnický střih):</strong> ramínka se spojují mezi lopatkami a nic nepadá z ramen. Nejčastější u sportovních plavek.</li>'
          '<li><strong>Křížená ramínka (X-back):</strong> dobře drží, víc odhalují záda.</li>'
          '<li><strong>Tenká ramínka a otevřená záda:</strong> plážový styl, při plavání mohou sklouzávat.</li>'
          '<li><strong>Nastavitelná ramínka:</strong> umožní doladit délku trupu, hodí se vysokým ženám.</li>'
          '<li><strong>Bez ramínek:</strong> na opalování; do vody je jistější model se snímatelnými ramínky.</li>'
          '<li><strong>Asymetrický střih přes jedno rameno:</strong> módní varianta k odpočinku.</li></ul>'
          '<h2>Zeštíhlující plavky</h2>'
          '<p>Zeštíhlující nebo stahovací plavky mají v přední části vrstvu pevnější pružné síťoviny, které se říká power mesh. Ta mírně stáhne bříško a vyhladí tvar. Pomáhá také řasení na boku nebo vpředu, které rozbije linii, tmavší barvy, svislé vzory a výstřih do V, který opticky prodlouží horní část těla. Vyšší výřez na nohou zase prodlouží nohy. Je fér říct, že plavky postavu nezmění. Upraví ji opticky a jemně ji zpevní, a pokud jsou příliš malé, naopak zařezávají a vytvářejí záhyby. Vybírejte proto velikost, ve které se cítíte pohodlně, ne o číslo menší.</p>'
          '<h2>Plavky s košíčky a kosticemi</h2>'
          '<p>Ženy s většími prsy ocení plavky, které se velikostí řídí jako podprsenka, tedy obvodem pod prsy a velikostí košíčku, například 80D. Takové modely mají Chantelle, Triumph nebo Litex. Kostice drží tvar, tvarované košíčky skryjí obrys bradavek a široká ramínka rozloží váhu. Pro plavání v bazénu bývají méně pohodlné než sportovní střih, protože kostice se při záběru otlačují. Měkké vyjímatelné vycpávky jsou kompromis, při praní je ale vyndejte, aby se nezkroutily.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Evropské velikosti se uvádějí čísly 36, 38, 40 a dále, sportovní značky často také písmeny nebo vlastní tabulkou. Rozhoduje obvod hrudníku, pasu a boků a u jednodílných plavek také délka trupu. Pokud plavky táhnou v rozkroku a ramínka zařezávají, máte delší trup a potřebujete větší velikost nebo model s nastavitelnými ramínky. Některé značky nabízejí varianty pro delší trup. Plavky ve vodě trochu povolí, sportovní by proto měly v suchu sedět těsně. Plážové plavky naopak nesmí na suchu nikde škrtit.</p>'
          '<p>Plavky zkoušejte přes spodní prádlo a s hygienickou páskou, kterou bývají opatřené. Řada obchodů přijímá vrácení jen tehdy, když páska zůstane neporušená.</p>'
          '<h2>Plavky pro těhotné a po porodu</h2>'
          '<p>Pro těhotenství se prodávají plavky s pružným bříškem a podpůrnou podprsenkou, které rostou s postavou. Po porodu se hodí plavky s pevnějším bříškem nebo tankiny, které se dají snadno vyhrnout. Plavání v těhotenství je obvykle vhodné, o jeho rozsahu se ale poraďte s lékařem.</p>'
          '<h2>Závodní plavky</h2>'
          '<p>Závodnice používají speciální plavky s nohavičkou ke kolenům, které jsou velmi těsné a oblékají se i několik minut. Plavky pro oficiální soutěže musí splňovat pravidla Světové plavecké federace World Aquatics a mít její schválení. Na běžný trénink se nehodí, protože jsou drahé, choulostivé a nepohodlné. Na tréninky si vyberte plavky odolné chloru a k nim <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plaveckou čepici</a>.</p>'
          '<h2>Plavky na aquafitness a cvičení ve vodě</h2>'
          '<p>Na aquaerobik a cvičení ve vodě se hodí sportovní plavky se širšími ramínky a vyšším výstřihem, které při poskocích nic neodhalí. Plavky s krátkou nohavičkou zabrání tomu, aby se spodní díl při kopech vyhrnoval. Lekce probíhají v chlorované vodě často několikrát týdně, takže i tady vydrží déle materiál odolný chloru. Kdo cvičí ve vodě kvůli kloubům nebo po úrazu, ocení plavky, které se snadno oblékají i svlékají.</p>'
          '<h2>Jednodílné plavky pro zralejší postavu</h2>'
          '<p>S věkem obvykle přichází potřeba víc opory a krytí. Vhodné jsou plavky se širšími ramínky, s měkkými košíčky nebo vnitřní podprsenkou a s pevnější přední částí. Vyšší záda zakryjí lopatky, nižší výřez na nohou zase horní část stehen. Modely se sukénkou nebo s nohavičkou nabídnou krytí ještě větší. Praktické jsou plavky bez složitého zavazování, protože ve stísněné kabince se s uzlíky manipuluje špatně.</p>'
          '<h2>Barvy a vzory</h2>'
          '<p>Tmavé odstíny jako černá, tmavě modrá nebo vínová postavu opticky zmenší, světlé a zářivé ji zvětší. Velké vzory přitáhnou pozornost, drobné ji rozptýlí. Tmavší spodní část a světlejší horní díl posunou pohled k obličeji. Světlé plavky bez podšívky mohou ve vodě prosvítat, proto u bílé a pastelových barev kontrolujte, zda podšívka kryje celou přední část. Na slunci a v chloru plavky časem blednou, proto je sušte vždy ve stínu.</p>'
          '<h2>Kolikery plavky mít</h2>'
          '<p>Kdo chodí plavat pravidelně, vystačí si se dvěma sportovními plavkami, které se střídají a mezi tréninky stihnou úplně uschnout. Vlhké plavky zavřené v tašce do druhého dne rychleji stárnou a začnou zapáchat. Na dovolenou se hodí jedny plavky na koupání a druhé na opalování, aby se nemusely oblékat mokré. Stejný model v jiné barvě je pohodlná volba, protože už víte, že vám sedí.</p>'
          '<h2>Plavky pro těhotné a kojící maminky</h2>'
          '<p>Kojící maminky ocení jednodílné plavky s odepínacími ramínky nebo s výstřihem, který se dá snadno odhrnout. Při plavání s miminkem v kurzu se hodí střih, který drží i při zvedání dítěte nad vodu, a materiál bez hrubých ozdob, o které by se malé ručičky mohly odřít.</p>'
          '<h2>Péče o plavky</h2>'
          '<ul><li>Po bazénu i moři plavky hned vypláchněte ve studené čisté vodě, chlor a sůl materiál poškozují.</li>'
          '<li>Perte ručně ve vlažné vodě s jemným prostředkem, bez ždímání a kroucení.</li>'
          '<li>Sušte naplocho ve stínu, ne na slunci, na radiátoru ani na rozpáleném kamení.</li>'
          '<li>Neseďte v plavkách na drsných okrajích bazénu, látka se rychle žmolkuje.</li>'
          '<li>Opalovací krémy a oleje mohou zanechat žluté skvrny, nechte je vsáknout před oblečením plavek.</li>'
          '<li>Při plavání několikrát týdně střídejte dvoje plavky, elastan si odpočine.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Plážové plavky na pravidelné plavání v chlorované vodě.</li>'
          '<li>Zeštíhlující plavky o číslo menší, které zařezávají.</li>'
          '<li>Přehlédnutí délky trupu u vysokých žen.</li>'
          '<li>Plavky s kosticemi na intenzivní plavání.</li>'
          '<li>Sušení na slunci a na radiátoru.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu porovnáte nabídky více obchodů a podíváte se, kde je vaše velikost skladem; objednávku dokončíte v e-shopu. Zkontrolujte i podmínky vrácení, které se u plavek kvůli hygieně liší. Pokud dáváte přednost dvoudílnému střihu, prohlédněte si <a href="/dvoudilne-plavky/">dvoudílné plavky a bikiny</a>, pro děti jsou určeny <a href="/detske-plavky/">dětské plavky</a> a na pláž se hodí <a href="/plazove-doplnky/">plážové doplňky</a>.</p>',
    faq=[
        ('Jaké jednodílné plavky vybrat do bazénu?', 'Sportovní plavky z materiálu odolného chloru, například z polyesteru nebo PBT, se zády ve střihu racerback. Vydrží pravidelné plavání výrazně déle než plavky z polyamidu s elastanem.'),
        ('Fungují zeštíhlující plavky?', 'Postavu nezmění, ale stahovací panely, řasení a tmavší barvy ji opticky zpevní. Zvolte velikost, ve které nikde nezařezávají.'),
        ('Proč se plavky v bazénu vytahají?', 'Chlor postupně rozkládá elastan. Pomáhá okamžité vypláchnutí ve studené vodě a plavky z materiálu odolného chloru.'),
        ('Jak poznám správnou velikost jednodílných plavek?', 'Podle obvodu hrudníku, pasu a boků v tabulce výrobce. Když plavky táhnou v rozkroku a ramínka zařezávají, máte delší trup a potřebujete větší velikost.'),
        ('Mají plavky s košíčky smysl pro větší prsa?', 'Ano. Modely s velikostí podle podprsenky, kosticemi a širokými ramínky dávají oporu. Na intenzivní plavání jsou ale méně pohodlné.'),
        ('Mohu plavky vrátit, když nesedí?', 'Záleží na obchodě. Plavky se zkoušejí přes prádlo a s hygienickou páskou; řada obchodů přijímá vrácení jen s neporušenou páskou.'),
        ('Jsou plavky s nohavičkou vhodné na plavání?', 'Ano. Krátká nohavička kryje horní část stehen, spodní díl se nevyhrnuje a hodí se na plavání, aquafitness i vodní sporty.'),
        ('Které barvy plavek opticky zeštíhlí?', 'Tmavé odstíny jako černá, tmavě modrá nebo vínová, svislé vzory a řasení. Světlé barvy a velké vzory postavu opticky zvětší.'),
        ('Jak plavky sušit?', 'Naplocho ve stínu, bez ždímání. Slunce, radiátor ani rozpálené kamení plavkám neprospívají.'),
    ])

# ------------------------------------------------------------------ dvoudilne-plavky
NEW['dvoudilne-plavky'] = dict(long=True,
    title='Bikiny a dvoudílné plavky: tankiny i pro plnoštíhlé',
    desc='Bikiny a dvoudílné plavky dámské: push-up, bandeau, vysoký pas, tankiny i pro plnoštíhlé. Samostatné díly a velikosti, nabídky českých e-shopů.',
    intro='<p><strong>Bikiny</strong> a další <strong>dvoudílné plavky</strong> mají jednu velkou výhodu: horní a spodní díl si často můžete vybrat zvlášť, každý ve své velikosti. To ocení ženy, jejichž prsa a boky neodpovídají stejnému číslu v tabulce. Mezi dvoudílnými plavkami jsou drobné trojúhelníkové bikiny na opalování, push-up a balconette s kosticemi, sportovní modely na plážový volejbal i tankiny, jejichž delší horní díl zakryje celé bříško.</p>'
          '<p>Na Sportece najdete nabídky českých e-shopů a objednávku dokončíte v obchodě, který si vyberete. Jsou tu plavky ' + B(('speedo', 'Speedo'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('calvin-klein', 'Calvin Klein'), ('litex', 'Litex')) + ', Roxy, Chantelle, Triumph, Arena nebo Nebbia, kompletní soupravy i samostatné vršky a spodky. Nadřazenou kategorií jsou <a href="/damske-plavky/">dámské plavky</a>, celistvý střih nabízejí <a href="/jednodilne-plavky/">jednodílné plavky</a>.</p>',
    guide='<h2>Horní díly: jaký tvar zvolit</h2>'
          '<p>Horní díl rozhoduje o tom, jak plavky drží a jak budou vypadat. Pro malá prsa a opalování se hodí jiný tvar než pro větší prsa nebo skákání do vln.</p>'
          + T(['Horní díl', 'Jak drží', 'Komu sedí'], [
              ['Trojúhelník', 'zavazování za krkem a na zádech, bez kostic', 'menší prsa, opalování'],
              ['Bandeau', 'pruh bez ramínek, často se silikonovým lemem', 'menší prsa, opalování bez pruhů'],
              ['Push-up', 'vycpávky zdvihnou prsa a přidají objem', 'menší a střední prsa'],
              ['Balconette a s kosticemi', 'tvarované košíčky, velikost podle podprsenky', 'střední a větší prsa'],
              ['Sportovní top', 'široký lem, racerback, bez zavazování', 'plavání, volejbal, surf'],
              ['Tankiny', 'delší top až k pasu nebo bokům', 'kdo chce zakrýt bříško']]) +
          '<p>Trojúhelník se zavazováním je nejuniverzálnější, protože si utažením nastavíte velikost i tvar. Při skoku do vody nebo v příboji ale mohou uzlíky povolit. Bandeau bez ramínek je skvělé na opalování, ve vodě se bez silikonového lemu nebo snímatelných ramínek rádo posouvá. Pro větší prsa jsou nejjistější díly s kosticemi a velikostí podle podprsenky, které mají například Chantelle a Triumph.</p>'
          '<h2>Spodní díly</h2>'
          '<ul><li><strong>Klasické kalhotky</strong> se středním krytím vzadu, nejběžnější volba.</li>'
          '<li><strong>Brazilky</strong> mají vzadu menší střih, oblíbené na opalování.</li>'
          '<li><strong>Vysoký pas</strong> sahá k pupíku nebo nad něj, zakryje bříško a dobře drží.</li>'
          '<li><strong>Se zavazováním na bocích</strong> se dá upravit obvod, ale uzly mohou povolit.</li>'
          '<li><strong>Šortky a boxerky</strong> kryjí horní část stehen a hodí se na aktivní pohyb.</li>'
          '<li><strong>S řasením</strong> vzadu nebo na bocích, které opticky zvětšuje a tvaruje.</li></ul>'
          '<h2>Tankiny</h2>'
          '<p>Tankiny je dvoudílná plavka, jejíž horní díl připomíná tílko a sahá k pasu nebo přes boky. Spojuje krytí jednodílných plavek s praktičností dvoudílných: na toaletu se nemusíte celá svlékat a horní díl i spodek si koupíte každý v jiné velikosti. Tankiny volí ženy, které nechtějí ukazovat bříško nebo jizvu, maminky, které si hrají s dětmi ve vodě, i starší ženy, kterým klasické bikiny nevyhovují. Horní díl bývá volný, s řasením nebo s vnitřní podprsenkou, a kombinuje se s klasickými kalhotkami, s vysokým pasem nebo se šortkami.</p>'
          '<h2>Samostatné díly</h2>'
          '<p>Mnoho značek prodává vršky a spodky zvlášť v rámci jedné kolekce. Nejvíc to ocení ženy s větším hrudníkem a užšími boky nebo naopak. Při nákupu hlídejte, aby oba díly pocházely ze stejné kolekce a měly stejné označení barvy. I u stejné barvy se odstín mezi kolekcemi nebo sezónami může lišit. Pokud kupujete díly v různých obchodech, porovnejte kód produktu, ne jen název barvy.</p>'
          '<h2>Bikiny pro plnoštíhlé</h2>'
          '<p>Plnoštíhlé ženy dnes najdou dvoudílné plavky ve větších velikostech u řady značek. Pomáhají tyto prvky:</p>'
          '<ul><li><strong>Horní díl s kosticemi a širokými ramínky</strong>, které rozloží váhu prsou a nezařezávají.</li>'
          '<li><strong>Spodní díl s vysokým pasem</strong>, který zakryje bříško a v pase drží bez rolování.</li>'
          '<li><strong>Tankiny</strong> pro maximální krytí a pohodlí.</li>'
          '<li><strong>Řasení a tmavé barvy</strong>, které opticky zeštíhlí.</li>'
          '<li><strong>Nastavitelné zapínání vzadu</strong> s háčky jako u podprsenky místo zavazování.</li></ul>'
          '<p>Rozhodující je správná velikost. Příliš malé plavky zařezávají a vytvářejí záhyby, které by žádná barva nezakryla. Velikost horního dílu proto berte podle změřeného obvodu pod prsy a košíčku, ne podle velikosti oblečení.</p>'
          '<h2>Jak změřit velikost</h2>'
          '<p>Pro horní díl s kosticemi změřte obvod těsně pod prsy a obvod přes nejširší místo prsou. Z rozdílu obou čísel určuje tabulka výrobce velikost košíčku. Trojúhelníky a sportovní topy se prodávají v písmenných velikostech XS až XL. Pro spodní díl změřte obvod boků v nejširším místě. Plavky by měly sedět těsně, ale bez zařezávání, protože ve vodě trochu povolí. Pokud jste mezi dvěma velikostmi a spodek se zavazuje, zvolte menší; pevný spodek si vezměte raději větší.</p>'
          '<h2>Sportovní dvoudílné plavky</h2>'
          '<p>Na plážový volejbal, surfování, paddleboard nebo kondiční plavání potřebujete plavky, které při prudkém pohybu nesklouznou. Sportovní dvoudílné plavky Nike, Adidas nebo Speedo mají top se širokým lemem a ramínky ve tvaru racerback, žádné uzlíky a spodní díl s pevnou gumou. Surfařské značky jako Roxy nabízejí i modely s delším rukávem. K vodním sportům se hodí další vybavení z kategorií <a href="/paddleboardy/">paddleboardy</a> a <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>, plážový volejbal najdete v kategorii <a href="/volejbal/">volejbal</a>.</p>'
          '<h2>Materiály a podšívka</h2>'
          '<p>Většina bikin je z polyamidu s elastanem, příjemného a pružného materiálu, který dobře drží tvar. Kvalitní plavky mají podšívku v celém horním díle i ve spodku, která zabrání průsvitnosti světlých barev. Některé kolekce používají recyklované vlákno z rybářských sítí a dalšího plastového odpadu. Na chlorované bazény se plážové bikiny hodí jen občas; elastan v nich chlor postupně rozkládá.</p>'
          '<h2>Vysoký pas a retro střihy</h2>'
          '<p>Spodní díly s vysokým pasem se vrátily se stylem padesátých let a dnes patří k nejoblíbenějším. Sahají k pupíku nebo nad něj, takže zakryjí bříško i jizvu po císařském řezu a v pase se nerolují. S krátkým topem nebo bandeau tvoří střih, který sluší štíhlým i plnějším postavám. Na sport se hodí vysoký pas s pevnou gumou, na opalování spíš měkčí varianta s řasením.</p>'
          '<h2>Bikiny na dovolenou k moři</h2>'
          '<p>K moři se vyplatí vzít aspoň dvoje plavky, aby jedny mohly uschnout. Slaná voda a písek plavkám dávají víc zabrat než sladká voda v jezeře; písek se usazuje v podšívce a dře o látku. Po každém koupání proto plavky opláchněte ve sprše nebo v umyvadle. Pokud plánujete šnorchlování, paddleboard nebo hraní ve vlnách, přibalte i sportovnější díl, který se neuvolní. Na celodenní pobyt na slunci se hodí také tričko s UV ochranou.</p>'
          '<h2>Dvoudílné plavky pro dospívající dívky</h2>'
          '<p>Dívky v pubertě často přecházejí z dětských plavek na bikiny. Vhodné jsou modely, které dobře drží: top se širšími ramínky nebo sportovní střih a spodní díl s pevnou gumou bez zavazování na bocích. Velikosti se řídí výškou postavy v centimetrech nebo písmenným značením XS a S. Pokud dívka plave ve škole nebo v oddílu, je praktičtější sportovní jednodílný střih. Další modely najdete v kategorii <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h2>Barvy a kombinování dílů</h2>'
          '<p>Dvoudílné plavky dávají víc prostoru pro hru s barvami. Tmavý spodek a světlejší nebo vzorovaný vršek přesune pozornost nahoru, opačná kombinace dolů. Jednobarevné kalhotky se dají kombinovat s několika různými vršky, a z jedněch plavek tak vzniknou troje. Řasení a zavazování na bocích opticky zúží boky, široký lem vysokého pasu zpevní bříško. Kovové kroužky a ozdoby vypadají dobře na fotkách, na slunci se ale umějí pořádně rozpálit.</p>'
          '<h2>Bikiny se zavazováním, nebo se sponou</h2>'
          '<p>Zavazování za krkem a na zádech umožní přesné doladění, uzlík na krku ale při celodenním nošení může tlačit. Spona nebo háčky vzadu drží pevněji a zapínají se rychleji. Na pláž s dětmi nebo na hraní ve vodě se hodí spíš spona, na opalování a fotky zavazování.</p>'
          '<h2>Jak o bikiny pečovat</h2>'
          '<p>Hned po koupání v moři nebo bazénu je opláchněte ve studené vodě a vymačkejte jemně v ručníku, ne kroucením. Perte ručně s jemným prostředkem, nikdy ne s bělidlem. Sušte ve stínu, protože slunce bledí barvy a unavuje elastan. Vycpávky push-up vršků před praním vyjměte a sušte zvlášť, aby se nezkroutily. Kovové ozdoby a kroužky po moři pořádně opláchněte, jinak mohou zanechat stopy rzi.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr horního dílu podle velikosti oblečení místo změřeného obvodu.</li>'
          '<li>Bandeau bez opory na skákání do vln.</li>'
          '<li>Díly z různých kolekcí, které se barevně neshodují.</li>'
          '<li>Plavky o číslo menší, které zařezávají v pase i na zádech.</li>'
          '<li>Zavazovací bikiny na aktivní sport.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe, takže zjistíte, kde mají právě vaši kombinaci velikostí. Samotný nákup proběhne v e-shopu. Před objednávkou si přečtěte podmínky vrácení, u plavek bývají kvůli hygieně přísnější. Na pláž se hodí také <a href="/plazove-doplnky/">plážové doplňky</a> a stín z kategorie <a href="/pop-up-a-plazove-stany/">pop-up a plážové stany</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi bikinami a tankiny?', 'Bikiny mají krátký horní díl, který kryje jen prsa. Tankiny mají delší horní díl ve tvaru tílka až k pasu nebo bokům a zakryje bříško.'),
        ('Mohu koupit horní a spodní díl v jiné velikosti?', 'Ano, pokud značka prodává díly samostatně. Hlídejte, aby oba pocházely ze stejné kolekce a měly stejné označení barvy.'),
        ('Jaké bikiny jsou vhodné pro plnoštíhlé?', 'Horní díl s kosticemi a širokými ramínky, spodní díl s vysokým pasem nebo tankiny. Rozhoduje správně změřená velikost.'),
        ('Jak změřit velikost horního dílu?', 'Změřte obvod pod prsy a přes nejširší místo prsou. Velikost košíčku pak určíte z tabulky výrobce.'),
        ('Jsou bikiny vhodné na sport?', 'Na sport volte sportovní dvoudílné plavky se širokým lemem, racerbackem a bez uzlíků. Zavazovací bikiny se při skocích a vlnách mohou povolit.'),
        ('Co je bandeau?', 'Horní díl ve tvaru pruhu bez ramínek. Hodí se na opalování bez pruhů, ve vodě je jistější se silikonovým lemem nebo snímatelnými ramínky.'),
        ('Jaké plavky si vzít na dovolenou k moři?', 'Aspoň dvoje, aby jedny mohly uschnout, a ideálně jeden sportovnější díl na vlny a vodní sporty. Po koupání je oplachujte ve sladké vodě.'),
        ('Co je push-up u plavek?', 'Horní díl s vycpávkami, které prsa zdvihnou a opticky zvětší. Vycpávky bývají vyjímatelné a před praním je vyndejte.'),
        ('Mohu bikiny nosit do bazénu?', 'Občas ano, chlor ale elastan rozkládá. Na pravidelné plavání jsou lepší plavky z materiálu odolného chloru.'),
    ])

# ------------------------------------------------------------------ kompresni-ponozky
NEW['kompresni-ponozky'] = dict(long=True,
    title='Kompresní podkolenky a ponožky na běh i sport',
    desc='Kompresní podkolenky, ponožky a návleky na lýtka pro běh a sport. Jak vybrat velikost, čím se liší od zdravotních punčoch; nabídky českých e-shopů.',
    intro='<p><strong>Kompresní podkolenky</strong> a ponožky tlačí na nohu víc než běžné ponožky. U sportovních modelů je tlak obvykle odstupňovaný: nejsilnější u kotníku a směrem nahoru slábne. Nosí je běžci, triatlonisté, cyklisté nebo lyžaři, kterým pevné obepnutí lýtka vyhovuje při výkonu i po něm. Patří sem i návleky na lýtka bez chodidla, které se kombinují s vlastními ponožkami.</p>'
          '<p>Hned na začátku je dobré říct jednu věc: sportovní kompresní ponožky nejsou zdravotnický prostředek a nenahrazují zdravotní kompresní punčochy, které určuje lékař. Sporteka porovnává nabídky českých obchodů a nakoupíte přímo v e-shopu. V nabídce jsou výrobky značek Compressport, CEP, Collm, Eleven, Haven, Klimatex nebo McDavid. Nadřazenou kategorií jsou <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>',
    guide='<h2>Jak komprese funguje</h2>'
          '<p>Kompresní úplet je pletený s vysokým podílem elastanu a po natažení na nohu na ni vyvíjí tlak. Ten se udává v milimetrech rtuťového sloupce, zkráceně mmHg, stejně jako krevní tlak. U odstupňované komprese je tlak největší v oblasti kotníku a ke kolenu postupně klesá. Některé sportovní výrobky uvádějí tlak přesně, jiné jen popisně jako lehkou nebo střední kompresi. Tlak také závisí na tom, jak velikost odpovídá vaší noze: příliš malá ponožka tlačí víc, příliš velká skoro vůbec.</p>'
          '<h2>Sportovní, nebo zdravotní komprese</h2>'
          + T(['', 'Sportovní kompresní ponožky', 'Zdravotní kompresní punčochy'], [
              ['Účel', 'pocit opory při sportu a po něm', 'léčba a prevence žilních onemocnění'],
              ['Kdo o nich rozhoduje', 'sportovec sám', 'lékař, který určí kompresní třídu'],
              ['Kde se kupují', 'sportovní obchody a e-shopy', 'lékárna, zdravotnické potřeby, často na předpis'],
              ['Velikost', 'podle obvodu lýtka a velikosti boty', 'podle přesně změřených obvodů a délek'],
              ['Označení tlaku', 'nejednotné, někdy chybí', 'kompresní třída podle normy']]) +
          '<p>Zdravotní kompresní punčochy se dělí do kompresních tříd. Často se používá německý standard RAL, podle kterého první třída odpovídá zhruba 18 až 21 mmHg a druhá 23 až 32 mmHg; vyšší třídy jsou ještě silnější. Předepisuje je lékař při křečových žilách, otocích, po operacích nebo při léčbě trombózy a měří je odborník v lékárně či prodejně zdravotnických potřeb. Pokud máte potíže s žilami, otoky nebo bolesti nohou, sportovní ponožky z e-shopu nejsou řešení a patří to k lékaři.</p>'
          '<h2>Ponožky, podkolenky, nebo návleky</h2>'
          '<ul><li><strong>Kompresní podkolenky</strong> sahají pod koleno a stlačují chodidlo, kotník i celé lýtko. Nejčastější volba běžců a triatlonistů.</li>'
          '<li><strong>Návleky na lýtka</strong> (calf sleeves) nemají chodidlo. Nosí se s vlastními běžeckými ponožkami, rychle se svlékají a hodí se v létě.</li>'
          '<li><strong>Kompresní ponožky</strong> končí nad kotníkem. Obepínají klenbu a kotník, lýtko nechávají volné.</li>'
          '<li><strong>Kompresní stehenní návleky a kalhoty</strong> se nosí méně a patří spíš k oblečení, například mezi <a href="/leginy/">legíny</a>.</li></ul>'
          '<p>Návleky mají výhodu v tom, že si ponožky vyberete samostatně podle bot a počasí, třeba z <a href="/merino-ponozky/">merino ponožek</a>. Podkolenky zase obepínají nohu bez přechodu a nic se neposune.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>U kompresního oblečení rozhoduje míra víc než u čehokoli jiného. Výrobci vycházejí obvykle z obvodu lýtka v nejširším místě, někdy také z obvodu nad kotníkem a z velikosti boty. Měřte ráno, kdy jsou nohy nejméně oteklé, vestoje a krejčovským metrem bez utahování. Pokud jste na hranici dvou velikostí, rozhodne obvykle obvod lýtka; při velmi silných lýtkách existují u některých značek široké varianty.</p>'
          '<p>Správně padnoucí podkolenka nesmí dělat záhyby, horní lem nesmí zařezávat do kůže pod kolenem a pata musí sedět na patě. Záhyb nebo zarolovaný lem vytvoří úzký pruh s vysokým tlakem, který je nepříjemný a v krajním případě škodí. Bolest, mravenčení, bledé nebo namodralé prsty jsou signál k okamžitému sundání.</p>'
          '<h2>Kdy je sportovci nosí</h2>'
          '<p>Běžci je obouvají na dlouhé tratě, do terénu i na silnici, triatlonisté pod neopren nebo až na kolo a běh. Lyžaři mají vlastní kategorii kompresních <a href="/lyzarske-ponozky/">lyžařských ponožek</a>. Nosí se i po výkonu, na cestu z maratonu domů nebo při dlouhém sezení v autě. Mnoho lidí uvádí, že se v nich nohy cítí lépe nebo že lýtko při běhu méně „kmitá“. Výzkumy vlivu na samotný výkon jsou ale nejednoznačné a výrazné zrychlení od kompresních ponožek čekat nelze. Berte je jako oblečení, které vám buď vyhovuje, nebo ne.</p>'
          '<p>Na dlouhé lety se kompresní podkolenky také doporučují. Pokud ale máte rizikové faktory trombózy, například prodělanou trombózu, nedávnou operaci, těhotenství nebo hormonální léčbu, poraďte se před cestou s lékařem. Určí, zda a jakou kompresi potřebujete.</p>'
          '<h2>Komprese na cestách a v práci</h2>'
          '<p>Lidé, kteří celý den stojí nebo sedí, třeba prodavači, kadeřnice, řidiči nebo programátoři, sahají po kompresních podkolenkách často proto, že jim nohy večer připadají méně těžké. Pro tyto účely se prodávají i nenápadné podkolenky do kancelářských bot v černé, šedé nebo tělové barvě. Pokud vám ale nohy otékají pravidelně nebo se objevují viditelné žíly, nečekejte, že pomůže sportovní ponožka, a nechte se vyšetřit.</p>'
          '<h2>Komprese pro cyklisty a lyžaře</h2>'
          '<p>Cyklisté nosí kompresní podkolenky hlavně na dlouhé vyjížďky, kde ocení tenký materiál a lem, který se při šlapání neshrnuje. U lyžařů jsou tenké kompresní podkolenky běžné, protože vysoká lyžařská bota tlačí na holeň a hladká ponožka bez záhybů je v ní pohodlnější. Lyžařské modely mívají zesílenou holeň a v botě nesmí být zmuchlané.</p>'
          '<h2>Dámské a pánské velikosti</h2>'
          '<p>Většina sportovních kompresních ponožek je unisex a velikost se řídí obvodem lýtka. Některé značky ale mají dámské řady s užší patou a kratší podkolenkou, protože ženské lýtko bývá kratší. Pokud vám podkolenka sahá až přes koleno, potřebujete kratší střih; horní lem patří zhruba dva prsty pod podkolenní jamku.</p>'
          '<h2>Komprese a regenerace po závodě</h2>'
          '<p>Po maratonu, dlouhém trailu nebo triatlonu si mnoho sportovců obleče kompresní podkolenky na cestu domů a na zbytek dne. Někomu je pevné obepnutí příjemné, zázračnou regeneraci ale nečekejte. Víc udělá dostatek tekutin, jídlo, spánek a lehké protažení. Pokud po závodě cítíte v lýtku ostrou bolest nebo vidíte otok jen na jedné noze, nehledejte řešení v ponožkách a vyhledejte lékaře.</p>'
          '<h2>Kdy kompresi nenosit bez rady lékaře</h2>'
          '<p>Komprese není vhodná pro každého. Lidé s onemocněním tepen dolních končetin, s pokročilou cukrovkou a poruchou citlivosti nohou, se srdečním selháním, s kožními záněty nebo otevřenými ranami na noze by ji měli nosit jen se souhlasem lékaře. Totéž platí pro otoky nejasného původu. Sportovní kompresní ponožky se zdravotní pomůckou nestávají ani tehdy, když mají v popisu vysoký tlak.</p>'
          '<h2>Materiály a provedení</h2>'
          '<p>Kompresní úplet je převážně z polyamidu a elastanu, někdy s příměsí polypropylenu nebo merino vlny pro lepší odvod potu a teplo v zimě. Chodidlo bývá zesílené v patě a ve špičce, některé modely mají anatomický tvar pro levou a pravou nohu. Ploché švy u prstů zabrání otlakům. Na běh se hodí tenčí ponožky, které se vejdou do bot bez přidávání velikosti; zimní modely jsou silnější. Barevné a reflexní podkolenky jsou za šera lépe vidět. Pokud běháte v lehkých silničních botách, vyzkoušejte, zda vám s kompresní ponožkou nebudou těsné; obuv najdete v kategorii <a href="/bezecka-obuv/">běžecká obuv</a>.</p>'
          '<h2>Jak kompresní ponožky obléknout</h2>'
          '<p>Kompresní podkolenku nenatahujte jako obyčejnou ponožku, protože ji nedostanete přes patu. Strčte ruku dovnitř, chyťte patu a obraťte horní část ponožky naruby až k patě. Nasuňte chodidlo, usaďte patu a pak postupně roviňte úplet nahoru po lýtku. Nakonec rukama rozprostřete látku tak, aby nikde nebyly záhyby. Gumové rukavice na mytí nádobí pomohou s úchopem a ochrání úplet před nehty.</p>'
          '<h2>Praní a životnost</h2>'
          '<p>Kompresní ponožky perte po každém nošení, protože pot a kožní maz unavují elastan. Obvykle stačí 30 až 40 °C podle štítku, bez aviváže, a sušit volně na vzduchu, ne na topení ani v sušičce. Teplo vlákna poškozuje a komprese pak slábne. I při dobré péči úplet časem povolí, a pokud se ponožky natahují snadněji než na začátku, tlak už je menší. Při každodenním nošení proto počítejte s výměnou po několika měsících, při občasném běhání vydrží déle.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr velikosti podle čísla boty bez změření lýtka.</li>'
          '<li>Nošení sportovních ponožek místo zdravotních punčoch, které má určit lékař.</li>'
          '<li>Zarolovaný horní lem nebo záhyby na lýtku.</li>'
          '<li>Sušení na topení, které zkracuje životnost.</li>'
          '<li>Očekávání výrazného zrychlení na závodě.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe a zjistíte, kde je skladem velikost podle obvodu vašeho lýtka; objednávku pak dokončíte v e-shopu. Tabulky velikostí se mezi značkami liší, proto si je otevřete u každého modelu zvlášť. Další vybavení pro běh najdete v kategorii <a href="/beh/">běh</a>, na podporu kloubů slouží <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> a <a href="/tejpy/">tejpy</a>.</p>',
    faq=[
        ('Jsou sportovní kompresní ponožky totéž co zdravotní punčochy?', 'Ne. Sportovní ponožky jsou oblečení. Zdravotní kompresní punčochy jsou zdravotnický prostředek, kompresní třídu určuje lékař a měří se v lékárně nebo prodejně zdravotnických potřeb.'),
        ('Jak vybrat velikost kompresních podkolenek?', 'Ráno vestoje změřte obvod lýtka v nejširším místě, případně nad kotníkem, a porovnejte ho s tabulkou výrobce. Velikost boty sama nestačí.'),
        ('Co znamená mmHg?', 'Milimetry rtuťového sloupce, jednotka tlaku. U kompresních výrobků udává, jak silně úplet tlačí na nohu, obvykle v oblasti kotníku.'),
        ('Zlepší kompresní ponožky výkon při běhu?', 'Výzkumy jsou nejednoznačné a výrazné zlepšení výkonu čekat nelze. Mnoho běžců je nosí, protože jim pevné obepnutí lýtka vyhovuje.'),
        ('Jaký je rozdíl mezi podkolenkami a návleky na lýtka?', 'Podkolenky obepínají chodidlo i lýtko. Návleky nemají chodidlo a nosí se s vlastními ponožkami, takže se rychleji svlékají.'),
        ('Kdo by neměl nosit kompresi bez porady s lékařem?', 'Lidé s onemocněním tepen dolních končetin, s pokročilou cukrovkou a poruchou citlivosti, se srdečním selháním, kožními záněty nebo otoky nejasného původu.'),
        ('Kdy kompresní ponožky vyměnit?', 'Když se natahují snadněji než na začátku a lem nedrží. Při každodenním nošení to bývá po několika měsících, při občasném sportu déle.'),
        ('Mohu v kompresních podkolenkách spát?', 'Sportovní kompresní ponožky se na noc obvykle nenosí, vleže komprese potřeba není. Pokud vám ji předepsal lékař, řiďte se jeho pokynem.'),
        ('Jak kompresní ponožky prát?', 'Po každém nošení na 30 až 40 °C podle štítku, bez aviváže, a sušit volně na vzduchu. Teplo topení a sušičky kompresi oslabuje.'),
    ])
