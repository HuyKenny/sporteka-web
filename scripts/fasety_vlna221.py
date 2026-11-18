"""sporteka.cz — facet landing texts wave 221 (kids' and Reima overalls, women's thermal leggings):
detska-kombineza, reima-kombineza, damske-termo-leginy.
Assortment described from the live catalogue copy (brands and model names as they appear in product names and shop descriptions).
Sources checked: Reima founded 1944 in Kankaanpää (Finland) from repurposed army material, Reimatec collection launched in the 1990s,
Lassie brand acquired together with Tutta in the 1990s, adult clothing dropped in 2004 and focus on kids 0–12 (company.reima.com, reima.com
our story); Reimatec fabric and taped seams waterproof above the 1 300 mm standard threshold, water can still get in at ankles, wrists and
neck, zips are not waterproof (help.reima.com); Reima sizes based on body measurements, size number = height in cm (reima.com size charts);
Gotland, Lappi and Puhuri sold as Reimatec overalls (retailer listings), Kurikka described as Reimatec in shop descriptions; Didriksons
founded 1913 in Sweden and its Extend size lengthens sleeves and legs by about one size by unpicking marked seams (support.didriksons.com);
Devold of Norway since 1853 (devold.com); EN 14682:2014 cords and drawstrings on children's clothing incl. skiwear (BSI) and no cords in
hood/neck area for small children (as checked for wave 218); Kari Traa founded 2002 by the Olympic moguls champion (karitraa.com);
Helly Hansen LIFA polypropylene base layer launched in the 1970s (Helly Hansen heritage); Klimatex founded 2007 with roots in
polypropylene functional wear of the 1970s (mediaguru.cz); merino fibre roughly 15–24 microns vs coarser wool, itch linked to thick
fibres (Woolmark, Icebreaker).
Deliberately left out (not verified): a single water-column figure for all Reimatec products, which Reima models other than Gotland,
Lappi, Puhuri and Kurikka are Reimatec, the Reima model name Trondheim (truncated in the catalogue), origin of the Sensor brand,
the mechanism of Loap Grow System, specific merino gram weights per model.
No prices, counts, stock claims, no medical promises."""
from texty_vlna1a import T

NEW = {}

# ------------------------------------------------------------------ detska-kombineza
NEW['detska-kombineza'] = dict(
    title='Dětská kombinéza: zimní, softshellová i do deště',
    desc='Dětské kombinézy na zimu, do bláta i do vody: zimní overal, softshell, nepromokavá souprava a neopren. Jak vybrat velikost, materiál a detaily.',
    intro='<p><strong>Dětská kombinéza</strong> je pro malé děti nejpraktičtější kus oblečení ven. Nikde nevyjede tričko, sníh se nedostane za záda a rodič obléká jen jednu věc místo bundy a kalhot. '
          'Pod tímto názvem se ale prodávají dost odlišné věci: zateplený zimní overal s membránou, lehčí softshellová kombinéza na jaro a podzim, tenká nepromokavá souprava do deště a kaluží, flísový overal pod svrchní vrstvu i neoprenová nebo plavková kombinéza k vodě. '
          'Na této stránce jsou dětské modely z kategorie <a href="/kombinezy/">kombinézy</a> s nabídkami českých obchodů. Průvodce vysvětluje, jak vybrat typ podle ročního období a věku, jak určit velikost podle výšky dítěte, co znamenají údaje o nepromokavosti a které detaily rozhodují v každodenním provozu. '
          'Kombinézy finské značky Reima mají vlastní stránku <a href="/reima-kombineza/">Reima kombinéza</a>.</p>',
    guide='<h2>Typy dětských kombinéz</h2>'
          '<p>Kombinéza je jen střih. To, k čemu se hodí, určuje materiál a výplň. Než začnete srovnávat značky, ujasněte si, do jakého počasí ji dítě bude nosit.</p>'
          + T(['Typ', 'Kdy se hodí', 'Na co dát pozor'], [
              ['zimní zateplený overal', 'sníh, mráz, sáňkování, dlouhé pobyty venku', 'výplň a membrána, zesílení na kolenou a sedu'],
              ['softshellová kombinéza', 'jaro a podzim, vítr, vlhko, školka', 'sama nehřeje, v dlouhém dešti promokne'],
              ['nepromokavá souprava do deště', 'kaluže, bláto, pískoviště po dešti', 'nezateplená, pod ni patří teplá vrstva'],
              ['flísový nebo vlněný overal', 'mezivrstva pod svrchní kombinézu, kočárek', 'neodolá vodě ani větru'],
              ['neoprenová a plavková kombinéza', 'koupání, moře, kurz plavání, ochrana před sluncem', 'velikost těsně na tělo, ne volně']]) +
          '<p>Většina rodin si vystačí se dvěma kusy: zimní kombinézou na období sněhu a mrazu a lehčí nepromokavou nebo softshellovou na zbytek roku. Flísový overal se vyplatí hlavně u nejmenších dětí, které ještě nechodí a v kočárku nebo v nosítku se málo hýbou.</p>'
          '<h2>Velikost podle výšky dítěte</h2>'
          '<p>Dětské velikosti se v Evropě obvykle značí výškou postavy v centimetrech: 80, 86, 92, 98, 104 a tak dál po šesti centimetrech. Číslo na štítku tedy odpovídá dítěti, které je zhruba tak vysoké. '
          'Před nákupem dítě změřte bez bot a porovnejte výšku s tabulkou výrobce, ne s věkem. Dvě tříleté děti se mohou lišit o celou velikost.</p>'
          '<p>Zimní kombinéza se kupuje s malou rezervou, protože pod ní bude termoprádlo a mikina a dítě během sezony vyroste. Příliš velký overal je ale nepraktický: rozkrok visí u kolen, rukávy přes dlaně a do nohavic se dostává sníh. Rozumná rezerva je jedna velikost, ne dvě. '
          'Některé značky to řeší prodlužováním. Didriksons u části modelů označuje systém Extend size: po vypárání označeného švu se rukávy a nohavice prodlouží zhruba o jednu velikost. Loap zase prodává modely s názvem Grow System, které popisuje jako rostoucí.</p>'
          '<h2>Nepromokavost, prodyšnost a švy</h2>'
          '<p>U zimních a nepromokavých kombinéz se uvádí <strong>vodní sloupec</strong> v milimetrech. Udává, jaký tlak vody látka vydrží, než propustí vlhkost. Dítě, které sedí v mokrém sněhu nebo klečí v kaluži, tlačí na látku mnohem víc než déšť, proto u dětského oblečení dává smysl vyšší hodnota. '
          'Druhý údaj je prodyšnost, tedy kolik vodní páry projde látkou ven. Děti se při hře zapotí rychleji, než by rodič čekal, a vlhké oblečení pak na saních nebo na lavičce studí.</p>'
          '<p>Stejně důležité jsou <strong>podlepené švy</strong>. Bez nich voda proteče dírkami po jehle, i když je samotná látka nepromokavá. Pozor na rozdíl mezi slovy nepromokavý a voděodolný: druhé obvykle znamená jen povrchovou úpravu, která vydrží krátkou přeháňku. Ani ta nejlepší kombinéza ale nezabrání tomu, aby voda zatekla u zápěstí, kotníků nebo krku, když dítě sedí v kaluži.</p>'
          '<h2>Výplň a teplo</h2>'
          '<p>Zimní overaly mají většinou syntetickou výplň. Hřeje i ve vlhku, snese časté praní a rychle schne. Péřové kombinézy existují také, například retro model Nuptse od <a href="/znacka/the-north-face/">The North Face</a> pro nejmenší. Peří je lehké a velmi teplé, ale mokro mu nesvědčí a praní je složitější. '
          'Pro chodící děti, které válí sudy ve sněhu, je syntetika praktičtější. Peří dává smysl spíš v kočárku a při mrazivých procházkách.</p>'
          '<p>Hřejivost overalu výrobci popisují různě: gramáží výplně, teplotním rozsahem nebo slovy jako lehce zateplená. Teplotní údaje berte orientačně. Dítě, které běhá, potřebuje méně než dítě, které sedí v kočárku. Teplo přidává hlavně správné vrstvení pod kombinézou.</p>'
          '<h2>Co pod kombinézu</h2>'
          '<p>První vrstva má odvádět pot. Hodí se <a href="/detske-termopradlo/">dětské termoprádlo</a> ze syntetiky nebo z merina, bavlna zůstane mokrá a dítě v ní prochladne. Druhá vrstva je tenká mikina, flís nebo vlněný overal, podle mrazu. Svrchní kombinéza pak chrání před větrem, sněhem a vlhkem. '
          'Ruce a nohy jsou místa, kde děti prochladnou nejdřív. K overalu patří nepromokavé <a href="/detske-rukavice/">dětské rukavice</a> s dlouhou manžetou a teplé <a href="/detske-zimni-boty/">dětské zimní boty</a>, přes které jde nohavice se sněhovým návlekem.</p>'
          '<h2>Detaily, které rozhodují v praxi</h2>'
          '<ul><li><strong>Zip</strong> přes celou délku až ke kotníku usnadní oblékání. Dva jezdce nebo zip v obou nohavicích ocení rodiče batolat.</li>'
          '<li><strong>Sněhové návleky</strong> uvnitř nohavic a gumička nebo poutko pod botu drží nohavici na místě.</li>'
          '<li><strong>Zesílený materiál</strong> na kolenou, sedu a spodku nohavic vydrží klouzání, lezení po prolézačkách i štěrk.</li>'
          '<li><strong>Odepínací kapuce</strong> se při zachycení za větev nebo skluzavku uvolní. Kapuce ani krk by u malých dětí neměly mít šňůrky.</li>'
          '<li><strong>Reflexní prvky</strong> pomohou v zimě, kdy se brzy stmívá a děti chodí ze školky za tmy.</li>'
          '<li><strong>Poutko na jméno</strong> nebo štítek uvnitř se hodí do školky, kde visí na věšácích stejné modely.</li></ul>'
          '<p>Norma EN 14682 řeší šňůrky a stahovací tkanice na dětském oblečení včetně lyžařského. Pro menší děti zakazuje šňůrky v oblasti kapuce a krku, protože se mohou zachytit na prolézačce. Při nákupu z neznámého zdroje je dobré to zkontrolovat sami.</p>'
          '<h2>Kombinéza, nebo bunda a kalhoty</h2>'
          '<p>Jednodílný overal je nejlepší pro děti zhruba do předškolního věku. Nic nevyjede, sníh se nedostane k zádům a dítě se obléká jedním pohybem. Starší děti ho ale na záchodě ve školce nebo ve škole svlékají špatně a začnou chtít dvoudílnou soupravu. '
          'Pak přichází na řadu <a href="/detska-zimni-bunda/">dětská zimní bunda</a> s <a href="/detske-lyzarske-kalhoty/">dětskými lyžařskými kalhotami</a> s laclem. Dvoudílná souprava se snáz kombinuje, kalhoty se dají obléct i k jiné bundě a při rychlém růstu stačí vyměnit jen jeden kus. '
          'Na hory se pro malé lyžaře prodávají i jednodílné <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a>, které mají sněhové návleky střižené přes lyžák.</p>'
          '<h2>Kombinéza do deště a k vodě</h2>'
          '<p>Nezateplená nepromokavá souprava je nejlevnější způsob, jak nechat dítě skákat v kalužích. Bývá z pogumované nebo PU látky, která vodu nepropustí, ale ani nedýchá. Hodí se na krátké hraní venku, ne na dlouhou túru. Pod ni oblékněte mikinu podle teploty a doplňte ji <a href="/detske-holinky/">dětskými holínkami</a>. '
          'V nabídce jsou i soupravy, kde jsou bunda a kalhoty s laclem prodávány jako komplet, například Trespass Kinley.</p>'
          '<p>K vodě se prodávají neoprenové kombinézy a plavkové overaly s UV ochranou. Neopren drží dítě v teple při delším koupání v chladnější vodě, plavkový overal chrání kůži před sluncem. Obojí musí sedět těsně, volný neopren nahřívá vodu jen špatně. Další modely najdete v kategorii <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíc dětských kombinéz v katalogu nese značka <a href="/znacka/reima/">Reima</a>, od zimních overalů s membránou přes softshellové modely až po kojenecké a plavkové overaly. Švédská <a href="/znacka/didriksons/">Didriksons</a> nabízí zimní overaly jako Bjärven. '
          'Dále tu jsou kombinézy Trespass, Columbia, Dare2b, Regatta, Hummel, Alpine Pro, Loap, Lewro, Pidilidi, Zigzag nebo Color Kids a dětská kolekce LEGO kidswear. Norský Devold má vlněný overal Polar Baby, který slouží jako teplá mezivrstva.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Kombinézu s membránou perte podle štítku, obvykle na nízkou teplotu, s tekutým pracím prostředkem a bez aviváže, která ucpává póry membrány. Zipy i suché zipy před praním zapněte, jinak mohou látku zachytit a poškodit. '
          'Když voda přestane po povrchu stékat v kapkách, obnovte impregnaci sprejem nebo prostředkem do pračky. Sušte volně, ne na topení. Zimní overal ukládejte suchý a čistý, aby přežil do další sezony nebo k mladšímu sourozenci.</p>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Nejdřív zvolte typ a velikost podle výšky, potom porovnávejte konkrétní modely. Stejný overal se v obchodech často liší barvou a dostupnými velikostmi, proto si v nabídce ověřte, zda e-shop má právě tu vaši. '
          'Na <a href="/sane-a-boby/">sáňky a boby</a> i na první lyžování se hodí zimní overal s vyšším vodním sloupcem, do školky spíš praktický model se zesílenými koleny. Na sjezdovku k overalu patří i <a href="/detske-lyzarske-helmy/">dětská lyžařská helma</a>.</p>',
    faq=[
        ('Jakou velikost dětské kombinézy vybrat?', 'Podle výšky dítěte v centimetrech, ne podle věku. Změřte dítě bez bot a zvolte velikost, která výšku pokrývá s malou rezervou na vrstvy a růst. Víc než jednu velikost navíc nedoporučujeme.'),
        ('Je lepší kombinéza, nebo bunda a kalhoty?', 'Pro malé děti zhruba do předškolního věku je praktičtější kombinéza, protože nic nevyjede a sníh se nedostane za záda. Starší děti často chtějí dvoudílnou soupravu, kterou snáz svléknou samy.'),
        ('Co znamená vodní sloupec u kombinézy?', 'Je to údaj v milimetrech, který říká, jaký tlak vody látka vydrží. Čím vyšší číslo, tím déle dítě vydrží sedět v mokrém sněhu. Důležité jsou i podlepené švy.'),
        ('Co obléct dítěti pod zimní kombinézu?', 'Termoprádlo ze syntetiky nebo z merina, nad něj podle mrazu mikinu nebo flís. Bavlněné tričko zůstane po zapocení mokré a dítě v něm prochladne.'),
        ('Je softshellová kombinéza vhodná na zimu?', 'Jen na mírné dny kolem nuly a se silnější vrstvou pod ní. Softshell chrání před větrem a vlhkem, ale sám moc nehřeje a v mokrém sněhu nakonec promokne.'),
        ('Proč by kapuce neměla mít šňůrky?', 'Šňůrky u krku a v kapuci se mohou zachytit na skluzavce nebo prolézačce. Norma EN 14682 je u oblečení pro menší děti v této oblasti nepřipouští.'),
        ('Co je rostoucí kombinéza?', 'Model, u kterého se dají prodloužit rukávy a nohavice. Didriksons to u části oděvů řeší vypáráním označeného švu, které přidá zhruba jednu velikost.'),
        ('Jak prát kombinézu s membránou?', 'Na nízkou teplotu podle štítku, tekutým prostředkem a bez aviváže. Zapněte zipy, sušte volně a po několika praních obnovte impregnaci.'),
        ('Hodí se zimní kombinéza na lyže?', 'Na první pokusy na sněhu ano. Pro pravidelné lyžování je lepší lyžařská kombinéza nebo souprava, které mají sněhové návleky střižené přes lyžařskou botu.'),
        ('Kde porovnat ceny dětských kombinéz?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Nákup dokončíte v e-shopu, kde si ověřte dostupnou velikost, barvu a podmínky vrácení.'),
    ])

# ------------------------------------------------------------------ reima-kombineza
NEW['reima-kombineza'] = dict(
    title='Reima kombinéza: zimní overal, Reimatec a softshell',
    desc='Kombinézy Reima pro děti: zimní overaly Reimatec, softshellové a flísové modely i plavkové overaly. Jak vybrat řadu, velikost podle výšky a péči.',
    intro='<p><strong>Reima kombinéza</strong> patří v Česku k nejčastěji hledanému dětskému oblečení ven. Finská značka se na děti specializuje desítky let a overaly dělá pro všechny části roku: zimní s membránou Reimatec, softshellové na jaro a podzim, flísové jako mezivrstvu a plavkové k vodě. '
          'Na této stránce jsou kombinézy Reima z kategorie <a href="/kombinezy/">kombinézy</a> s nabídkami českých obchodů. Průvodce shrnuje, co znamená označení Reimatec, jak se orientovat v modelech s finskými a skandinávskými jmény, jak Reima počítá velikosti a jak o overal pečovat, aby vydržel i dalšímu dítěti. V nabídce jsou modely pro kojence v kočárku, batolata i předškoláky. '
          'Srovnání s kombinézami jiných značek najdete na stránce <a href="/detska-kombineza/">dětská kombinéza</a>, ostatní výrobky značky na <a href="/znacka/reima/">stránce Reima</a>.</p>',
    guide='<h2>Kdo je Reima</h2>'
          '<p>Reima vznikla v roce 1944 ve finském Kankaanpää. Podle firemní historie začínala šitím pracovního oblečení z přešitého armádního materiálu. Postupně se zaměřila na odolné látky pro dětské oblečení a v devadesátých letech uvedla kolekci Reimatec. '
          'Ve stejném období spolu s firmou Tutta získala značku Lassie. Od roku 2004 nedělá oblečení pro dospělé a soustředí se jen na děti zhruba do dvanácti let. Overaly tak nejsou zmenšenou verzí dospělé bundy, ale počítají s dětmi, které klečí, kloužou se a válí ve sněhu.</p>'
          '<h2>Co znamená Reimatec</h2>'
          '<p>Reimatec je označení nepromokavých a prodyšných výrobků značky. Podle výrobce jsou nepromokavé jak samotná látka, tak podlepené švy, a materiál přesahuje hranici 1 300 mm vodního sloupce, od které norma pro ochranný oděv mluví o nepromokavém oblečení. '
          'Konkrétní hodnotu vodního sloupce Reima uvádí u jednotlivých výrobků a liší se mezi nimi, proto ji hledejte v popisu konkrétního overalu.</p>'
          '<p>Reima sama upozorňuje na dvě věci. Voda se může dostat dovnitř u kotníků, zápěstí a krku, například když dítě dlouho sedí v kaluži. A většina zipů nepromokavá není, proto má mít dítě v dešti zavřené lišty, které zip kryjí. Nepromokavost tedy neznamená, že dítě po odpoledni v rozbředlém sněhu bude úplně suché.</p>'
          '<h2>Přehled řad v nabídce</h2>'
          '<p>Reima pojmenovává modely po místech a slovech z Finska a Skandinávie. V katalogu se objevují hlavně tyto skupiny:</p>'
          + T(['Skupina', 'Příklady modelů', 'K čemu'], [
              ['zimní overaly s membránou', 'Kurikka, Puhuri, Gotland, Lappi, Toppila, Skaulo', 'mráz, sníh, sáňkování, dlouhé hraní venku'],
              ['další zimní overaly', 'Stavanger, Tromssa, Kipina, Kaunisto, Reitit, Tienoot', 'zimní pobyt venku, liší se střihem a výbavou'],
              ['softshellové overaly', 'Mjosa, Nurmes, Marte Mid, Sevetti', 'jaro, podzim, vítr a vlhko'],
              ['flísové a vlněné overaly', 'Tarhaan, Pirpana', 'mezivrstva, kočárek, chladná rána'],
              ['plavkové a UV overaly', 'Atlentti, Vesihiisi', 'koupání a ochrana před sluncem']]) +
          '<p>Overaly Gotland, Lappi a Puhuri obchody prodávají s označením Reimatec, stejně jako Kurikku. U ostatních modelů ověřte v popisu, zda mají membránu, nebo jen vodoodpudivou úpravu. Část modelů vychází i v edici s motivy Mumínků, například Moomin Puhuri nebo Moomin Mjosa.</p>'
          '<h2>Jak Reima počítá velikosti</h2>'
          '<p>Velikost Reima odpovídá výšce dítěte v centimetrech a výrobce ji odvozuje z tělesných mír. V tabulce na webu značky jsou u každé velikosti uvedené i obvod hrudníku, pasu a délka nohy. U batolat začínají overaly u velikosti 74 nebo 80 a pokračují po šesti centimetrech. '
          'Reima v tabulce připomíná, že děti rostou ve skocích, a proto může mít smysl vzít větší velikost. Overaly se ale nemají kupovat o dvě čísla větší. Dítě v nich zakopává a sněhové návleky pak nesedí na botách.</p>'
          '<p>Při zkoušení posaďte dítě na zem a nechte ho pokrčit kolena a zvednout ruce. Rukávy nemají vyjet nad zápěstí a overal nemá táhnout v rozkroku ani na zádech. Mezi kombinézou a tělem musí zůstat místo pro termoprádlo a mikinu.</p>'
          '<h2>Výbava, kterou u overalů Reima najdete</h2>'
          '<ul><li><strong>Odnímatelná kapuce</strong> se uvolní, když se zachytí za překážku. Kapuce bez šňůrek odpovídá požadavkům na bezpečnost dětského oblečení.</li>'
          '<li><strong>Zesílený materiál</strong> v sedu a na nohavicích od kolen dolů, u Kurikky jej výrobce zmiňuje přímo v popisu.</li>'
          '<li><strong>Sněhové návleky</strong> a poutka pod botu, aby nohavice při klouzání nevyjela nahoru.</li>'
          '<li><strong>Dlouhý zip</strong> přes přední díl a zvýšený límec, který chrání krk před větrem.</li>'
          '<li><strong>Reflexní prvky</strong> pro lepší viditelnost za šera.</li></ul>'
          '<p>Membránové modely mají povrchovou úpravu, na které voda tvoří kapky. Reima ji v popisech některých overalů uvádí pod názvem Bionic-Finish Eco. Taková úprava se praním a otěrem postupně opotřebuje a časem ji je potřeba obnovit.</p>'
          '<h2>Zimní, nebo softshellový overal</h2>'
          '<p>Zimní overal s membránou a výplní je volba na sníh a mráz. Softshell Reima, třeba Mjosa nebo Nurmes, je tenčí a pružnější a hodí se na období, kdy je kolem nuly nebo pár stupňů nad ní. Chrání před větrem a lehkým deštěm a dítě se v něm pohodlně hýbe. '
          'V dlouhém dešti nebo při sezení v mokré trávě ale softshell nakonec propustí vodu. Na mokré podzimní dny proto dávají smysl Reimatec overaly bez silné výplně, pod které oblečete mikinu podle teploty.</p>'
          '<h2>Doplňky od stejné značky</h2>'
          '<p>Reima dělá kompletní výbavu ven, takže se dá sladit barvou i funkcí. Na overal navazují <a href="/reima-cepice/">čepice Reima</a> s ochranou uší, <a href="/reima-rukavice/">rukavice Reima</a> s dlouhou manžetou a <a href="/reima-zimni-boty/">zimní boty Reima</a>. '
          'Starší děti, které už overal nechtějí, přecházejí na dvoudílnou soupravu. Pro ně je tu výběr na stránce <a href="/reima-zimni-bunda/">zimní bunda Reima</a> a obecně <a href="/reima-bunda/">bundy Reima</a>.</p>'
          '<p>Pod zimní overal patří <a href="/detske-termopradlo/">dětské termoprádlo</a>. Membrána odvede páru ven jen tehdy, když ji první vrstva u těla nezadrží jako bavlna. Na jarní kaluže doplňte softshell nebo nepromokavý overal <a href="/detske-holinky/">dětskými holínkami</a>.</p>'
          '<h2>Vrstvy pod overal podle teploty</h2>'
          '<p>Stejný overal může sloužit od podzimu do jara, když se mění to, co je pod ním. Kolem nuly a v suchu stačí pod zimní overal tenké termoprádlo. V mírném mrazu přidejte tenkou flísovou mikinu nebo vlněnou vrstvu. '
          'Ve větším mrazu, a hlavně u dětí v kočárku nebo na saních, které se málo hýbou, je na místě silnější mezivrstva, třeba flísový overal Tarhaan. Naopak dítě, které běhá a staví sněhuláka, se v příliš mnoha vrstvách zpotí a pak rychle vychladne.</p>'
          '<p>Nejjednodušší kontrola je sáhnout dítěti za krk. Když je teplé a suché, je oblečené správně. Když je zpocené, ubírejte. Studené ruce samy o sobě o prochladnutí nevypovídají, ty bývají chladnější skoro vždycky.</p>'
          '<h2>Overal do školky</h2>'
          '<p>Ve školce se overal obléká a svléká několikrát denně, často s pomocí učitelky, která má na starosti celou třídu. Hodí se proto dlouhý zip, který jde snadno zapnout, a poutka na pověšení. '
          'Dovnitř napište jméno dítěte, stejné modely Reima visí v šatně často vedle sebe. Užitečné je mít druhý, lehčí overal na výměnu, protože ten zimní po dopoledni v mokrém sněhu do odpoledne nemusí uschnout.</p>'
          '<h2>Plavkové a kojenecké overaly</h2>'
          '<p>Kromě oblečení na zimu nabízí Reima i overaly k vodě. Atlentti je plavkový overal pro batolata, Vesihiisi plážový overal s UV ochranou. Kojenecké modely jako Tilkkanen nebo flísový Tarhaan slouží do kočárku a jako teplá vrstva. Ostatní dětské plavky najdete v kategorii <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h2>Péče o overal Reima</h2>'
          '<p>Postupujte podle štítku. Obecně platí: zapnout všechny zipy a suché zipy, prát na nízkou teplotu s tekutým prostředkem, bez aviváže a bez bělidla. Membránu nepoškodí běžné praní, ale ucpou ji zbytky aviváže a nečistot. '
          'Overal sušte volně, ne na topení. Když voda přestane stékat po povrchu v kapkách a látka nasakuje, je čas na impregnaci, sprejem nebo přípravkem do pračky. Po zimě uložte overal čistý a suchý. Overaly Reima se často prodávají z druhé ruky a čistý, nepoškozený kus si udrží hodnotu.</p>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Nejdřív si ujasněte, zda chcete zimní overal s membránou, softshell, nebo mezivrstvu. Pak hledejte konkrétní model. Stejný overal mívá v obchodech jiné barvy a jiné dostupné velikosti a někdy se prodává i pod mírně odlišným názvem, třeba overal dětský Kurikka a dětská zimní kombinéza Kurikka. '
          'Před nákupem zkontrolujte číslo velikosti podle výšky dítěte a podmínky vrácení. Nabídky z českých obchodů jsou na této stránce pohromadě.</p>',
    faq=[
        ('Odkud je značka Reima?', 'Z Finska. Firma vznikla v roce 1944 v Kankaanpää a od roku 2004 se věnuje jen dětskému oblečení zhruba do dvanácti let.'),
        ('Co znamená Reimatec?', 'Označení nepromokavých a prodyšných výrobků Reima. Nepromokavá je látka i podlepené švy. Přesnou hodnotu vodního sloupce najdete v popisu konkrétního modelu.'),
        ('Je overal Reimatec úplně nepromokavý?', 'Látka a švy ano, ale voda může zatéct u zápěstí, kotníků a krku a většina zipů není vodotěsná. Při dlouhém sezení v kaluži dítě zevnitř zvlhne.'),
        ('Jakou velikost overalu Reima vybrat?', 'Číslo velikosti odpovídá výšce dítěte v centimetrech. Porovnejte výšku s tabulkou výrobce a počítejte s místem pro termoprádlo a mikinu.'),
        ('Mám vzít overal Reima o číslo větší?', 'Reima připouští větší velikost, protože děti rostou ve skocích. Dvě čísla navíc ale nedávají smysl, overal pak nesedí na botách a dítě v něm zakopává.'),
        ('Který overal Reima je na zimu?', 'Zimní overaly s membránou, například Kurikka, Puhuri, Gotland nebo Lappi. Softshellové modely jako Mjosa jsou na jaro a podzim.'),
        ('Jaký je rozdíl mezi Mjosa a Kurikka?', 'Mjosa je softshellový overal na přechodné období, pružný a bez silné výplně. Kurikka je zimní overal s membránou Reimatec a zesíleným sedem a nohavicemi.'),
        ('Jak prát overal Reima?', 'Se zapnutými zipy na nízkou teplotu, tekutým prostředkem a bez aviváže. Sušte volně a po čase obnovte impregnaci, když voda přestane stékat v kapkách.'),
        ('Má overal Reima odnímatelnou kapuci?', 'Zimní modely ji obvykle mají, kapuce se při zachycení uvolní. U konkrétního modelu to ověřte v popisu výrobku.'),
        ('Kde porovnat ceny kombinéz Reima?', 'Na této stránce jsou nabídky českých obchodů pohromadě. V e-shopu si před nákupem ověřte dostupnou velikost a barvu.'),
    ])

# ------------------------------------------------------------------ damske-termo-leginy
NEW['damske-termo-leginy'] = dict(
    title='Dámské termo legíny: merino, syntetika a zateplené',
    desc='Dámské termo legíny pod lyžařské kalhoty i na zimní běh: merino, syntetika, počesaný úplet a délka 3/4. Jak vybrat materiál, velikost a jak je prát.',
    intro='<p><strong>Dámské termo legíny</strong> jsou nejjednodušší způsob, jak v zimě nemít zimu na nohy. Pod tímto označením se ale prodávají dvě různé věci. Jednou je funkční spodní vrstva, tedy termoprádlo, které se nosí pod lyžařské nebo turistické kalhoty. '
          'Druhou jsou zateplené legíny s počesanou vnitřní stranou, které se nosí samostatně, na zimní běh, procházku se psem nebo do města pod kabát. Na této stránce jsou dámské modely z kategorie <a href="/zateplene-leginy/">zateplené legíny</a> s nabídkami českých obchodů. '
          'Průvodce vysvětluje, jak rozlišit oba typy, kdy vybrat merino a kdy syntetiku, co znamená délka 3/4, jak legíny mají sedět a jak o ně pečovat. Celoroční sportovní modely najdete na stránce <a href="/damske-leginy/">dámské legíny</a>. Pokud hledáte celou sadu s tričkem, pokračujte do kategorie termoprádla.</p>',
    guide='<h2>Spodní vrstva, nebo legíny na ven</h2>'
          '<p>Než začnete porovnávat materiály, rozhodněte se, jestli legíny budou pod kalhotami, nebo navrchu. Podle toho se liší tloušťka, úplet i střih.</p>'
          + T(['Typ', 'Jak se nosí', 'Typické vlastnosti'], [
              ['termo spodky (base layer)', 'pod lyžařské, běžkařské nebo turistické kalhoty', 'tenký úplet těsně na těle, merino nebo syntetika, ploché švy'],
              ['zateplené legíny', 'samostatně na běh, procházku, do města', 'silnější neprůsvitný úplet, počesaná vnitřní strana, kapsy'],
              ['3/4 termo legíny', 'pod lyžařské a skialpové boty', 'končí pod kolenem, v botě se nehrnou']]) +
          '<p>Hranice mezi typy není ostrá. Některé tenčí zateplené legíny se dají nosit i pod kalhoty, silnější merino spodky zase samostatně na skialpy. Pokud ale potřebujete jedny legíny na lyže a druhé na běh, kupujte dvoje. Spodky pod kalhoty mají být tenké, legíny na ven odolné proti oděru a neprůsvitné.</p>'
          '<h2>Merino, nebo syntetika</h2>'
          '<p><strong>Merino</strong> je jemná ovčí vlna. Vlákna mají běžně tloušťku zhruba 15 až 24 mikronů, jsou tedy tenčí než u běžné vlny, a proto merino na kůži obvykle nekouše. Vlna pohlcuje vodní páru, příjemně hřeje i při pomalém pohybu a pomaleji začne zapáchat, takže merino legíny vydrží několik dní na horách bez praní. '
          'Nevýhodou je menší odolnost proti oděru a delší schnutí. Proto se merino často kombinuje s nylonem nebo elastanem, které úplet zpevní a pomohou, aby legíny držely tvar.</p>'
          '<p><strong>Syntetika</strong> (polyester, polypropylen, polyamid) vlhkost nepojme, ale rychle ji odvede k další vrstvě a velmi rychle schne. Hodí se na intenzivní sport, kde se člověk hodně potí, třeba na běžky nebo zimní běh. Bývá levnější a odolnější, ale dřív začne vonět potem. '
          'Polypropylen má u nás dlouhou tradici. Česká značka <a href="/znacka/klimatex/">Klimatex</a>, založená v roce 2007, odvozuje své kořeny od výzkumu polypropylenových vláken pro funkční oblečení ze sedmdesátých let. Na polypropylenu stojí i řada LIFA od Helly Hansen, kterou značka uvedla v sedmdesátých letech.</p>'
          '<p><strong>Bavlna</strong> do termo legín nepatří. Nasákne pot, dlouho schne a na kůži studí. Pozor i na legíny ze směsi s viskózou nebo modalem, které jsou na dotek měkké a příjemné doma, ale při sportu se chovají spíš jako bavlna. '
          'Pro pohyb venku v zimě proto hledejte ve složení merino, polyester, polypropylen nebo polyamid, případně jejich směs s elastanem.</p>'
          '<h2>Tloušťka a gramáž</h2>'
          '<p>U merina výrobci často uvádějí gramáž úpletu v gramech na metr čtvereční. Nižší číslo znamená tenčí a vzdušnější úplet na intenzivní pohyb, vyšší číslo silnější a teplejší úplet na mráz a pomalý pohyb. Syntetické legíny se značí spíš slovy, například light, warm nebo thermo. '
          'Pro lyžování na sjezdovce a běžné zimní túry stačí střední tloušťka, do silného mrazu a na pomalé aktivity, třeba zimní rybaření nebo stání na tribuně, volte silnější. Na skialpy a běžky naopak tenčí, protože při výstupu je horko.</p>'
          '<h2>Zateplené legíny s počesanou stranou</h2>'
          '<p>Legíny s počesaným vnitřkem, v nabídce často popsané jako legíny s chloupkem nebo s fleecem, mají na vnitřní straně jemně vytažená vlákna. Ta drží vzduch u těla a příjemně hřejí. Na zimní běh se hodí modely s reflexními prvky a kapsou na klíče, na procházky a do města spíš neprůsvitné matné legíny s vysokým pasem. '
          'Tyto legíny většinou nejsou nepromokavé. V dešti nebo mokrém sněhu nasáknou, proto se na delší túru v takovém počasí hodí spíš termo spodky a přes ně <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>.</p>'
          '<h2>Délka 3/4 pod lyžáky</h2>'
          '<p>Pod lyžařské a skialpové boty se nosí legíny v délce 3/4, které končí pod kolenem. Důvod je jednoduchý: v lyžáku má být jen jedna vrstva, ponožka. Dlouhé spodky se v botě shrnou do záhybů, tlačí a mohou způsobit otlaky. '
          'Na lyže tedy volte 3/4 legíny a k nim <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, které sahají nad okraj boty. Tříčtvrteční délku v nabídce mají například Salewa Cristallo Warm, Viking Gaja nebo Dare2b In the Zone. Na běžky, kde se nosí nízké boty, jsou naopak praktičtější dlouhé legíny.</p>'
          '<h2>Dámský střih a velikost</h2>'
          '<p>Dámské termo legíny mají užší pas, víc prostoru v bocích a kratší sed než pánské. Spodní vrstva má sedět těsně, ale nesmí škrtit. Pokud mezi legínami a kůží zůstane vzduch, nemohou odvádět vlhkost. Zároveň nemají zařezávat v pase ani pod koleny. '
          'Vysoký pas je praktický pod lyžařské kalhoty, protože se při předklonu nic neodhalí. Ploché švy nebo bezešvé pletení, které nabízí třeba 4F, zabrání odírání pod lyžařskými kalhotami a v botách. Při výběru velikosti vycházejte z obvodu pasu a boků v tabulce výrobce.</p>'
          '<h2>Vrstvení na lyže, běžky a do města</h2>'
          '<p>Na sjezdovce tvoří legíny první vrstvu. Nad ně patří <a href="/damske-lyzarske-kalhoty/">dámské lyžařské kalhoty</a>, zateplené nebo skořepinové. Nahoře se k nim hodí funkční tričko z <a href="/termopradlo-damske/">dámského termoprádla</a> nebo <a href="/merino-triko-damske/">dámské merino triko</a> a <a href="/damska-funkcni-mikina/">dámská funkční mikina</a>. '
          'Na <a href="/bezecke-lyzovani/">běžky</a> stačí tenké spodky a lehké softshellové kalhoty, případně samotné zateplené legíny, pokud nefouká. Do města se zateplené legíny nosí pod delší bundu nebo kabát a k nim teplé boty a <a href="/merino-ponozky-damske/">dámské merino ponožky</a>.</p>'
          '<h2>Kolik párů a jaké</h2>'
          '<p>Na týden na horách stačí většinou dva páry spodní vrstvy. Jeden nosíte, druhý větrá nebo schne po praní. Kdo lyžuje i běhá, vystačí si s jedněmi 3/4 merino legínami pod lyžák a jedněmi dlouhými syntetickými na běžky. '
          'Zateplené legíny na ven se vyplatí mít zvlášť, protože se na nich víc projeví oděr od bot, kola nebo psího vodítka a do lyžařských kalhot by byly zbytečně silné.</p>'
          '<h2>Chyby při výběru</h2>'
          '<ul><li><strong>Příliš volné spodky</strong> neodvádějí pot, protože se nedotýkají kůže. Pod kalhotami se navíc shrnují.</li>'
          '<li><strong>Dlouhé legíny do lyžáku</strong> vytvoří v botě záhyby. Na sjezdovku patří délka 3/4.</li>'
          '<li><strong>Silné legíny na intenzivní sport</strong> znamenají zpocené nohy a pak zimu na vleku nebo při přestávce.</li>'
          '<li><strong>Tenké světlé legíny na ven</strong> mohou být v předklonu průsvitné. U legín na běh a do města proto hledejte v popisu neprůsvitný úplet.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Merino termo legíny tu mají <a href="/znacka/smartwool/">Smartwool</a> (Classic Merino), <a href="/znacka/icebreaker/">Icebreaker</a> (ZoneKnit), <a href="/znacka/sensor/">Sensor</a> (Merino Active, Merino DF, Merino Air), Helly Hansen (LIFA Merino) a <a href="/znacka/kari-traa/">Kari Traa</a>. Norskou značku Kari Traa založila v roce 2002 olympijská vítězka v jízdě v boulích a typické jsou pro ni vzorované vlněné spodky, například řada Rose. '
          'Syntetické a smíšené modely mají Salewa, Viking, Dare2b, 4F, Husky, Odlo, Litex, Willard, Klimatex, Progress, Horsefeathers, Meatfly nebo Lotto. Další merino spodní vrstvy najdete v kategorii <a href="/merino-pradlo/">merino prádlo</a>.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Merino perte na vlněný nebo jemný program, při nízké teplotě a prostředkem na vlnu. Aviváž nepoužívejte, sušte naplocho nebo přes šňůru, ne na topení a ne v sušičce, pokud to štítek výslovně nedovoluje. Merino se díky tomu, že tak rychle nezapáchá, nemusí prát po každém nošení, často stačí vyvětrat. '
          'Syntetické legíny snesou běžné praní, ale ani u nich se aviváž nedoporučuje, protože zhoršuje odvod vlhkosti. Legíny s počesanou stranou perte naruby, chloupek se tak méně žmolkuje.</p>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Nejdřív si ujasněte, zda hledáte spodní vrstvu, nebo legíny na ven, a jakou délku potřebujete. Potom porovnávejte složení (podíl merina a syntetiky), tloušťku a střih. Dvě legíny se stejným názvem termo se mohou lišit materiálem i tloušťkou zásadně. '
          'Stejný model se v obchodech liší barvou a dostupnými velikostmi. Pro lyžaře je souhrnný výběr spodních vrstev v kategorii <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi termo legínami a zateplenými legínami?', 'Termo legíny jako spodní vrstva jsou tenké a nosí se pod kalhoty. Zateplené legíny mají silnější úplet s počesanou vnitřní stranou a nosí se samostatně.'),
        ('Merino, nebo syntetika?', 'Merino hřeje i při pomalém pohybu a pomaleji zapáchá, hodí se na vícedenní pobyt na horách. Syntetika rychleji schne a lépe snáší intenzivní pocení, například na běžkách.'),
        ('Kouše merino?', 'Většinou ne. Merino vlákna jsou jemnější než běžná vlna, takže se na kůži ohýbají a nepíchají. Citlivější kůže může reagovat na hrubší úplety.'),
        ('Proč se pod lyžáky nosí legíny 3/4?', 'Aby v lyžařské botě byla jen ponožka. Dlouhé legíny se v botě shrnou do záhybů a mohou tlačit.'),
        ('Jak mají termo legíny sedět?', 'Těsně na těle, aby mohly odvádět vlhkost, ale nesmí škrtit v pase ani pod koleny. Velikost vybírejte podle obvodu pasu a boků v tabulce výrobce.'),
        ('Jsou zateplené legíny nepromokavé?', 'Většinou ne. V dešti nebo mokrém sněhu nasáknou. Do takového počasí volte termo spodky a přes ně nepromokavé kalhoty.'),
        ('Můžu běhat v termo legínách?', 'Ano, na zimní běh jsou vhodné zateplené legíny se syntetickým úpletem, reflexními prvky a kapsou. Merino spodky se na běh hodí v mrazu a při pomalejším tempu.'),
        ('Jak prát merino legíny?', 'Na vlněný nebo jemný program, při nízké teplotě a prostředkem na vlnu, bez aviváže. Sušte volně, ne na topení. Často stačí jen vyvětrat.'),
        ('Proč termo legíny nepatří do sušičky?', 'Merino se teplem může srazit a syntetický úplet ztratit pružnost. Řiďte se štítkem, některé modely sušičku snesou na nízkou teplotu.'),
        ('Kde porovnat ceny dámských termo legín?', 'Na této stránce jsou nabídky českých obchodů pohromadě. V e-shopu si ověřte složení, délku a dostupnou velikost.'),
    ])
