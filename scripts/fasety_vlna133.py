"""sporteka.cz — facet landing texts wave 133: navijaky-daiwa, alpine-pro-lyzarska-bunda,
jarni-a-podzimni-bundy-damske, decathlon-damske-plavky.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ navijaky-daiwa
NEW['navijaky-daiwa'] = dict(
    title='Navijáky Daiwa: řady, velikosti a výběr podle lovu',
    desc='Navijáky Daiwa pro přívlač, feeder, kapraře i moře. Jak číst označení LT a 2500D-C, jak zvolit velikost a kterou řadu hledat pro svůj styl rybaření.',
    intro='<p>Daiwa je japonská značka, která patří k nejznámějším výrobcům rybářských navijáků na světě, a v nabídce Sportecy ji najdete skoro ve všech kategoriích: od malých navijáků na jemnou přívlač přes univerzální řady až po robustní kousky na moře a těžké ryby. '
          'Názvy modelů ale působí jako šifra. Číslo před jménem označuje rok řady, za ním následuje velikost a písmena jako C, D nebo XH, která říkají, jak je naviják stavěný. '
          'Tato stránka sbírá <a href="/rybarske-navijaky/">navijáky</a> značky Daiwa z českých obchodů. Vysvětlíme, co jednotlivé řady znamenají, jak číst velikosti a převody, pro koho se hodí multiplikátory a co dělat s náhradní cívkou. '
          'Kromě značky samotné ukážeme, jak se Daiwa liší od ostatních výrobců a které doplňky od <a href="/rybarske-pruty/">prutů</a> po šňůry stojí za pozornost.</p>',
    guide='<h2>Jak číst označení navijáků Daiwa</h2>'
          '<p>Na první pohled se zdá, že názvy jako „25 Prorex V LT 3000-CXH“ nemají logiku. Ve skutečnosti se skládají ze čtyř částí, které se pravidelně opakují. Nejdřív rok modelové řady, pak jméno řady, následuje označení konstrukce a nakonec velikost s písmeny pro cívku a převod. Kdo se jednou naučí číst tyto kódy, zorientuje se v nabídce mnohem rychleji než podle fotografií, které u všech navijáků vypadají podobně.</p>'
          + T(['Část názvu', 'Příklad', 'Co zpravidla znamená'], [
              ['Rok řady', '23, 24, 25, 26', 'ročník modelu; starší řady bývají v obchodech vyprodávány a pro praxi jsou často stejně dobré'],
              ['Jméno řady', 'Caldia, Legalis, Prorex, Ballistic, Saltiga', 'zaměření a vybavení; určuje, jestli jde o univerzál, přívlač, jemný lov nebo moře'],
              ['LT', 'Prorex V LT', 'konstrukční koncepce značky, která usiluje o nízkou hmotnost a pevnost; velikost se u ní značí řadou od 1000 výš'],
              ['Velikost', '2500, 3000, 4000, 6000', 'rozměr těla a kapacita cívky; vyšší číslo znamená větší a těžší naviják'],
              ['Písmena za velikostí', 'C, D, S, P, H, XH', 'tvar těla, hloubka cívky a rychlost převodu']]) +
          '<p>Písmena nejsou u všech řad stejná, a proto si vždy ověřte údaje v popisu produktu. Obecně platí, že C označuje kompaktní tělo, tedy menší a lehčí kousek, D hlubší cívku s větší kapacitou, S mělčí cívku pro jemné vlasce a H nebo XH vyšší nebo velmi vysoký převod. Právě převod rozhoduje, kolik vlasce naviják nabere jednou otáčkou kličky.</p>'
          '<h2>Řady Daiwa podle zaměření</h2>'
          '<p>V nabídce se opakují stejné řady v různých velikostech. Rozdíly mezi nimi nejsou jen v ceně, ale především v tom, na co jsou určeny. Následující přehled shrnuje, jak se řady v katalogu obvykle používají. Podrobné parametry si ověřte u konkrétního kusu.</p>'
          + T(['Řada', 'Hlavní využití', 'Kdo ji ocení'], [
              ['Sweepfire, Fuego, Crossfire, Regal', 'univerzální rybaření, přívlač, rybníky a řeky', 'začátečník, který chce spolehlivý naviják bez zbytečných funkcí'],
              ['Caldia, Legalis, Ballistic', 'jemnější a střední přívlač, plynulý chod', 'pokročilý rybář, který ocení kvalitnější brzdu a lehčí váhu'],
              ['Prorex', 'lov dravců na umělé nástrahy', 'přívlačář na štiku, candáta, okouna nebo bolena'],
              ['N’Zon', 'feeder a položená, přesné dálkové náhozy', 'feederista s pravidelnými hody na stejné místo'],
              ['TDR, TDM, Emblem', 'kaprařina, volnoběh a velká kapacita cívky', 'kapřař s ležícími pruty a dlouhým čekáním'],
              ['Saltiga', 'velké ryby a moře', 'rybář na dovolené u moře a vláčení těžkých nástrah'],
              ['Multiplikátory Tatula, SS Air', 'cílená přívlač a těžší nástrahy', 'zkušenější rybář s citem pro nához']]) +
          '<p>Rozdělení vychází ze zaměření, které značka u řad uvádí. Co se hodí na štiku, nemusí být nejlepší pro lov cejnů, a proto vždy začněte otázkou, jakou rybu a jakou nástrahu budete používat. Pro přívlač je nejblíž řada Prorex od značky ' + B(('daiwa', 'Daiwa')) + ', pro dlouhý den feederu se podívejte na modely s velkou cívkou a vyšším převodem.</p>'
          '<h2>Velikost navijáku a délka lovu</h2>'
          '<p>Velikost patří k nejdůležitějším rozhodnutím a chyba se špatně opravuje. Příliš malý naviják nezvládne zatížení a nenabere dost vlasce, příliš velký přetěžuje prut a unavuje zápěstí. Ve světě Daiwy se používá řada čísel od 1000 do 6000 a výš, přičemž střední hodnoty kolem 2500 až 4000 pokrývají nejvíc situací.</p>'
          + T(['Velikost', 'Ryby a nástrahy', 'Typický prut'], [
              ['1000–2000', 'ultralight, okoun, pstruh, malé třpytky', 'lehký prut do několika gramů'],
              ['2500–3000', 'všestranné rybaření, malý a střední dravec', 'prut do čtrnácti až dvaceti gramů'],
              ['4000–5000', 'štika, candát, feeder, těžší nástrahy', 'střední až těžší prut'],
              ['6000 a více', 'dlouhé náhozy, kapr, moře, velká kapacita', 'těžký prut, dlouhý kaprový nebo mořský']]) +
          '<p>Při nákupu na dálku se řiďte kapacitou cívky v popisu a hmotností. Kdo hledá první naviják na všechno, je dobrá volba velikost kolem 3000: pojme dost šňůry a zároveň nepřetěžuje prut. Detailní pravidla vyvážení soupravy najdete v kategorii <a href="/rybarske-navijaky/">navijáky</a> a v nabídce <a href="/rybarske-pruty/">rybářských prutů</a>.</p>'
          '<h2>Převod a rychlost navíjení</h2>'
          '<p>Převod určuje, kolikrát se při otočení kličkou otočí rotor. Vyšší převod, tedy označení H a XH, navíjí rychle a hodí se k nástrahám vedeným u hladiny nebo k rychlému vyhrabání vlasce po hodu. Nižší převod, bez písmene H nebo s označením C u pomalejších modelů, dává větší sílu a je přívětivější u těžkých nástrah, jako jsou gumové rybky s olovem nebo jig. Při chodu proti proudu a dlouhých odhozech je rychlejší převod pohodlnější, protože vlasec nevisí do větru.</p>'
          '<ul><li><strong>Rychlý převod:</strong> kovové třpytky, rychlé woblery, přívlač na čisté vodě.</li>'
          '<li><strong>Středně rychlý převod:</strong> univerzální volba pro začátek, hodí se na většinu nástrah.</li>'
          '<li><strong>Pomalejší převod:</strong> pomalé wobblery, těžší gumy, malé hluboké nástrahy, lov v silném proudu.</li></ul>'
          '<h2>Multiplikátory Daiwa a komu se hodí</h2>'
          '<p>V katalogu je několik multiplikátorů Daiwa. Jejich cívka se otáčí na ose a vlasec se při hodu odvíjí přímo z ní. Dává to větší přesnost a sílu při zdolávání, ale vyžaduje cvik, protože při špatném hodu se vlasec zacuchá, tzv. paruka. Začátečníkům se doporučují nástrahy středního gramu a pozvolné ladění brzdy. Multiplikátory bývají označené pravou nebo levou rukou, a proto zkontrolujte, na které straně chcete kličku mít. Rychlost a výkon dobře využije ten, kdo cíleně loví dravce z loďky nebo od břehu na stejných místech.</p>'
          '<h2>Náhradní cívky, pouzdra a údržba</h2>'
          '<p>Značka Daiwa nabízí k mnoha modelům náhradní cívky. Cívku s jinou kapacitou nebo hloubkou můžete mít připravenou s pleteným vlascem pro přívlač a druhou s monofilem pro jemný lov. Výměna trvá několik sekund, a tak jeden naviják pokryje více technik. Důležité je správně vybrat cívku podle názvu modelu i velikosti, protože cívky mezi řadami nejsou zaměnitelné. V katalogu najdete také ochranná pouzdra, která chrání mechanismus při přepravě v autě nebo v rybářském batohu, viz <a href="/rybarske-tasky/">rybářské tašky</a>. Celkový přehled vybavení najdete v sekci <a href="/rybareni/">rybaření</a>, praktické drobnosti pak mezi <a href="/rybarske-doplnky/">rybářskými doplňky</a> a v <a href="/rybarske-obleceni/">rybářském oblečení</a>.</p>'
          '<p>Po rybaření nechte naviják oschnout, nikdy jej nestříkejte tlakovou vodou a po slané vodě jej opláchněte čistou. Jednou za sezonu lehce promažte kličku a hřídel a zkontrolujte přítlačný šroub brzdy. Pletená šňůra potřebuje při navinování lehké napětí a dobře navinutá cívka drží vlasec rovnoměrně.</p>'
          '<h2>Daiwa v porovnání s dalšími značkami</h2>'
          '<p>Rybáři často srovnávají Daiwu s ' + B(('shimano', 'Shimano')) + ', druhým japonským výrobcem, který nabízí podobné řady. Nehledejte absolutního vítěze: obě značky dělají kvalitní kousky v celé cenové škále a rozdíl bývá ve stylu, ergonomii kličky a detailech v nastavení brzdy. Pro silnější mořský boj a těžké ryby se hledá spíš ' + B(('penn', 'Penn')) + ' známý robustními kousky. Kaprařské navijáky najdete u ' + B(('fox', 'Fox')) + ' a feederové či plavanou výbavu u ' + B(('dam', 'DAM')) + '. Souhrn těchto značek si můžete prohlédnout na stránkách <a href="/navijaky-shimano/">navijáky Shimano</a>, <a href="/navijaky-penn/">navijáky Penn</a>, <a href="/navijaky-fox/">navijáky Fox</a> a <a href="/navijaky-dam/">navijáky DAM</a>.</p>'
          '<h2>Jak rozeznat starší řadu od nové</h2>'
          '<p>Číslo roku na začátku názvu vám pomůže poznat, jak „čerstvý“ model je. U stejné řady se mezi ročníky mění detaily v povrchové úpravě, v bezpečnostních prvcích i v balení, zatímco základní mechanika zůstává. Nejnovější ročník není nutně nejlepší: starší řada může nabízet stejnou práci za nižší cenu. Při porovnávání sledujte, zda jde o stejný model s jinou velikostí, nebo o jinou verzi, a prohlédněte si u každého kusu údaje o kapacitě a hmotnosti.</p>'
          '<h2>Co zkontrolovat před objednávkou</h2>'
          '<ul><li><strong>Přesný název:</strong> řada, velikost i písmena za ní musí odpovídat tomu, co hledáte.</li>'
          '<li><strong>Pravá nebo levá ruka:</strong> u multiplikátorů se klička liší stranou, u pevných cívek se obvykle přehazuje.</li>'
          '<li><strong>Náhradní cívka:</strong> zjistěte, zda je v balení, nebo se prodává zvlášť.</li>'
          '<li><strong>Šňůra a vlasec:</strong> ověřte, jaký průměr vlasce cívka pojme a zda je vhodná i pro pletenou šňůru.</li>'
          '<li><strong>Dostupnost velikosti:</strong> obchody mívají jiný výběr, a proto porovnejte nabídky na jedné stránce.</li></ul>',
    faq=[
        ('Co znamená LT v názvu navijáků Daiwa?', 'Jde o označení konstrukční koncepce, která usiluje o kombinaci nízké hmotnosti a pevnosti. U těchto modelů se velikost značí číslem od 1000 výše a hmotnost bývá nižší než u starších řad. Podrobné údaje si ověřte v popisu konkrétního modelu.'),
        ('Co znamená písmeno C, D, XH nebo S za velikostí?', 'Obvykle C značí kompaktní tělo, D hlubší cívku, S mělčí cívku a H nebo XH vyšší nebo velmi vysoký převod. Písmena se mezi řadami mohou mírně lišit, proto je potřeba číst popis produktu. Převod rozhoduje o rychlosti navíjení.'),
        ('Jaká velikost navijáku Daiwa je nejuniverzálnější?', 'Pro většinu českých vod se osvědčila střední velikost kolem 2500 až 3000. Zvládne okouna i menší štiku a dá se použít s lehkým i středním prutem. Pro těžší nástrahy, feeder nebo kapry sáhněte po velikosti 4000 a více.'),
        ('Je lepší naviják s rychlým, nebo pomalým převodem?', 'Záleží na nástrahách. Rychlý převod se hodí pro třpytky a rychlé woblery, pomalejší pro těžké gumy a silný proud. Pokud nevíte, začněte středně rychlým převodem, který pokryje nejvíc situací.'),
        ('Pro koho jsou multiplikátory Daiwa?', 'Pro rybáře, kteří cíleně loví dravce a chtějí přesnost a sílu při zdolávání. Vyžadují cvik, protože při špatném hodu se vlasec zacuchá. Začátečníkům se doporučují nástrahy střední hmotnosti a pozvolné nastavení brzdy.'),
        ('Dají se k modelům Daiwa koupit náhradní cívky?', 'Ano, pro mnoho modelů jsou nabízeny. Důležité je vybrat cívku přesně podle názvu a velikosti navijáku, protože cívky mezi řadami nejsou zaměnitelné. Druhá cívka umožní střídat typ šňůry nebo vlasce.'),
        ('Můžu s navijákem Daiwa rybařit v moři?', 'Zvolte model určený pro moře, v katalogu například řadu Saltiga. Běžné sladkovodní navijáky nejsou na slanou vodu stavěné a po rybaření je nutné je opláchnout čistou vodou. Mořské kousky mají větší kapacitu a odolnější mechanismus.'),
        ('Jak poznám nový ročník modelu?', 'Podle čísla na začátku názvu, například 25 nebo 26. Znamená rok uvedení řady. Starší ročníky bývají v obchodech vyprodávané a pro běžné rybaření je rozdíl často malý, proto porovnejte nabídky a parametry.'),
        ('Čím se Daiwa liší od Shimana?', 'Obě značky jsou japonské a dělají kvalitní navijáky v celé škále. Rozdíl bývá v ergonomii, vzhledu kličky a v řadách. Neexistuje jednoznačný vítěz, rozhoduje typ rybolovu, pohodlí v ruce a to, co si vyzkoušíte.'),
        ('Jak se starat o naviják, aby vydržel?', 'Po lovu jej nechte oschnout, po slané vodě opláchněte čistou. Jednou za sezonu promažte kličku a hřídel, zkontrolujte brzdu a vlasec navíjejte pod lehkým napětím. Tlakovou vodou jej nestříkejte, aby se nedostala dovnitř.'),
    ],
)

# ------------------------------------------------------------------ alpine-pro-lyzarska-bunda
NEW['alpine-pro-lyzarska-bunda'] = dict(
    title='Alpine Pro lyžařská bunda: modely pro ženy, muže i děti',
    desc='Alpine Pro lyžařská bunda dámská, pánská i dětská. Jak číst názvy modelů, membránu PTX, zateplení, velikosti a vybrat bundu na svah, snowboard i školu.',
    intro='<p>Alpine Pro je česká značka outdoorového a zimního oblečení a její lyžařské bundy patří na našich svazích k nejběžnějším. Důvod je prostý: nabídka pokrývá celou rodinu, tedy dámské, pánské i dětské střihy, a přitom se drží praktických řešení, jako je membrána, kapuce přes helmu nebo sněhová sukně. '
          'Názvy modelů jsou ale vždy vymyšlené jméno, například Olada, Ferera nebo Dearo, a bez vysvětlení z nich není poznat, o jaký typ bundy jde. '
          'Na této stránce najdete lyžařské bundy Alpine Pro z kategorie <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>. Vysvětlíme, co znamená membrána PTX, kdy zvolit péřovou či zateplenou bundu, jak vybrat velikost pro děti podle výšky a čím se Alpine Pro liší od dalších značek. Cílem je, abyste si vybrali kus, který bude na svahu pohodlný.</p>',
    guide='<h2>Sortiment Alpine Pro: ženy, muži a děti</h2>'
          '<p>Z nabídky v katalogu je vidět, že značka má jasně rozdělené střihy. Dámské bundy jsou užší v pase a kratší v rukávech, pánské širší v ramenou a delší v těle. Dětské modely bývají označené číslem velikosti a rozmezím výšky. U většiny modelů je v názvu také jméno, barva a typ membrány, takže se v nabídce lépe orientujete. Dámské a pánské bundy se často nabízejí ve stejných řadách s odlišnými barevnými kombinacemi.</p>'
          + T(['Skupina', 'Co hledat', 'Na co si dát pozor'], [
              ['Dámské', 'užší střih, delší záda, prodloužené rukávy, výrazné barvy', 'u přiléhavého střihu zkontrolujte pohyb v ramenou a prostor na vrstvy'],
              ['Pánské', 'volnější střih, hlubší kapsy, kapuce přes helmu', 'delší rukávy a záda; dlouhé postavy si ověří délku'],
              ['Dětské', 'membrána, reflexní prvky, úchyt pro skipas', 'volte podle výšky dítěte, ne podle věku; rezerva na růst'],
              ['Péřové a prošívané', 'teplo při stání, dojíždění, běžné zimní dny', 'při aktivní jízdě se mohou přehřívat']]) +
          '<p>Chcete-li zvolit bundu podle účelu, začněte otázkou: jezdíte aktivně a rychle, nebo spíš tráví čas na svahu s dětmi? U prvního typu stačí tenčí bunda s membránou a regulací teploty vrstvami. U druhého se vyplatí silnější zateplení a delší střih, který chrání při stání ve frontě.</p>'
          '<h2>Co znamená membrána PTX</h2>'
          '<p>V názvech se opakuje označení „s membránou PTX“. Jde o vlastní membránu značky Alpine Pro, která má bránit pronikání vody a zároveň propouštět vodní páru z těla. Údaje o vodním sloupci a prodyšnosti najdete v popisu konkrétního modelu. Obecně platí, že vyšší vodní sloupec hlídá lépe mokrý sníh a déšť, vyšší prodyšnost se hodí pro aktivní jízdu. Bundy bez uvedené membrány bývají jednodušší, vhodné spíš na suchý a chladný den.</p>'
          '<p>Při srovnávání modelů dávejte pozor na označení „ptx snow“, které se v názvech objevuje u řad určených přímo na sjezdovku. Kromě membrány pomáhá i zatmelení švů a chlopeň přes zip. Kdo jezdí za každého počasí, ocení bundu s přelepenými švy a zipy chráněnými chlopní. Pro suché dny a krátké vyjížďky stačí jednodušší provedení.</p>'
          '<h2>Zateplená, péřová nebo lehká bunda</h2>'
          '<p>V nabídce Alpine Pro najdete bundy různé tloušťky zateplení, včetně prošívaných a péřových kousků, například modely s označením péřová. Rozhodnutí závisí hlavně na tom, jak se při lyžování zahříváte. Pokud jedete plynule a rychle, stačí lehčí zateplení doplněné fleecem. Pokud většinu času stojíte, chodíte s dětmi nebo jezdíte při mrazu, vezměte silnější bundu a pod ni jen tenké termoprádlo.</p>'
          '<ul><li><strong>Péřová bunda:</strong> je velmi teplá při nízké hmotnosti, ale pero nemá rádo mokro, proto je nutná kvalitní vnější tkanina.</li>'
          '<li><strong>Syntetické zateplení:</strong> udrží teplo i při navlhnutí a snáší praní lépe než peří.</li>'
          '<li><strong>Bunda bez zateplení (shell):</strong> chrání před větrem a vodou, teplo se řeší vrstvami pod ní.</li></ul>'
          '<p>Vrstvení pod bundu najdete v kategorii <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>. Pro silné mrazy doplňte i <a href="/lyzarske-rukavice/">lyžařské rukavice</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>.</p>'
          '<h2>Velikosti dětských bund podle výšky</h2>'
          '<p>Děti rostou rychle, proto se dětské lyžařské bundy označují výškou a ne věkem. V katalogu Alpine Pro uvidíte velikosti ve tvaru 116, 128, 140, 152 nebo 164, což odpovídá výšce dítěte v centimetrech. Při výběru změřte dítě bez bot, přidejte jedno číslo na vrstvy a kontrolujte délku rukávů. Bunda by měla pokrýt zadek a při předklonu neodhalit záda.</p>'
          + T(['Výška dítěte', 'Velikost', 'Poznámka'], [
              ['kolem 116 cm', '116', 'malé děti, často s prodlouženým zipem pro snadné oblékání'],
              ['kolem 128 cm', '128', 'školní věk; rukávy lze občas ohrnout pro růst'],
              ['kolem 140 cm', '140', 'střední školní věk, bunda by měla přesahovat pas'],
              ['kolem 152 cm', '152', 'starší děti, často již blízké dámskému nebo pánskému střihu'],
              ['kolem 164 cm', '164', 'dospívající, porovnejte i s nejmenší dámskou nebo pánskou velikostí']]) +
          '<p>Dětské bundy bývají vybaveny reflexními prvky a kapsou na skipas. Pokud dítě roste, vezměte bundu s regulací rukávů, ale nepřehánějte velikost: příliš velká bunda se na svahu zvedá a dítě v ní neudrží teplo ani rovnováhu. Pro celé dětské vybavení si projděte i <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a> a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>'
          '<h2>Detaily, které rozhodují o pohodlí</h2>'
          '<p>Při nákupu bundy prohlédněte konstrukci a nezastavujte se u názvu. Kapuce musí sedět přes helmu a nesmí zakrývat výhled. Sněhová sukně musí jít zapnout, případně se spojit s kalhotami. Větrací zipy pod pažemi pomáhají při jízdě v teplém dni. Manžety s palcovým otvorem drží rukáv na místě a zabrání pronikání sněhu. Zdánlivě drobnosti tvoří rozdíl mezi bundou, kterou na svahu nevnímáte, a bundou, která vás po hodině obtěžuje.</p>'
          '<ul><li><strong>Kapuce:</strong> nastavitelná, kompatibilní s helmou.</li>'
          '<li><strong>Kapsy:</strong> zip s chlopní, vnitřní kapsa na telefon, kapsa na skipas na rukávu.</li>'
          '<li><strong>Sněhová sukně:</strong> přes boky, případně s úchytem na kalhoty.</li>'
          '<li><strong>Zipy:</strong> hlavní zip s chlopní, větrací zipy v podpaží.</li>'
          '<li><strong>Délka:</strong> záda alespoň přes pás, aby při předklonu nefoukalo.</li></ul>'
          '<h2>Pro koho je Alpine Pro vhodná</h2>'
          '<p>Značka cílí na široký okruh lyžařů a snowboardistů, kteří chtějí dobře vybavenou bundu bez extrémních nároků na technické provedení. Hodí se pro rekreační lyžování, rodinné výlety, školu v přírodě i zimní procházky. Profesionální freeriderské nebo skialpové bundy jsou obvykle jiný typ: lehčí, s větším důrazem na prodyšnost a stlačitelnost. Pokud skialpinismu nebo freeridu věnujete většinu času, podívejte se na specializovanější značky, například ' + B(('helly-hansen', 'Helly Hansen'), ('columbia', 'Columbia')) + '.</p>'
          '<h2>Alpine Pro v porovnání s dalšími značkami</h2>'
          '<p>Při výběru lyžařské bundy porovnáváte často několik značek vedle sebe. Alpine Pro je v tomto srovnání spíš všestranná značka s širokou nabídkou pro celou rodinu. Podobné řady nabízejí ' + B(('kilpi', 'Kilpi')) + ' a ' + B(('hannah', 'Hannah')) + ', které jsou také české či středoevropské a konkurují hlavně výběrem barev a střihů. Norský Helly Hansen a americká Columbia jsou známější sportovním zázemím. Všechny tyto značky si můžete projít v samostatných přehledech: <a href="/kilpi-lyzarska-bunda/">Kilpi lyžařská bunda</a>, <a href="/hannah-lyzarska-bunda/">Hannah lyžařská bunda</a>, <a href="/helly-hansen-lyzarska-bunda/">Helly Hansen lyžařská bunda</a> a <a href="/lyzarska-bunda-columbia/">lyžařská bunda Columbia</a>.</p>'
          '<h2>Jak prát a udržovat lyžařskou bundu</h2>'
          '<p>Bunda s membránou se perou šetrně. Zapněte všechny zipy, vyprázdněte kapsy a použijte prací prostředek určený pro funkční oblečení, bez aviváže, která ucpává póry membrány. Teplota vody se řídí štítkem, obvykle do třiceti či čtyřiceti stupňů. Po vyprání je vhodné krátké zahřátí v sušičce nebo žehlení přes tenkou látku, pokud to štítek dovoluje, protože teplo oživí vodoodpudivou úpravu. Skladujte bundu volně pověšenou, nesbalenou v tašce.</p>'
          '<h2>Kdy nakupovat a co ověřit</h2>'
          '<p>Při nákupu lyžařské bundy kontrolujte přesný název modelu, protože některé řady se v různých obchodech objevují s různými barvami a označením. Porovnejte velikost podle tabulky výrobce, zjistěte, zda je zboží skladem ve vaší velikosti, a pokud dítě roste, vyberte modely, které se dají nastavit. Ceny mezi obchody se liší, a proto stránka porovnává nabídky vedle sebe. Pro dokončení výbavy se podívejte i na <a href="/lyzarske-obleceni/">lyžařské oblečení</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/zimni-bundy/">zimní bundy</a> pro běžné nošení ve městě.</p>',
    faq=[
        ('Co znamená membrána PTX u bund Alpine Pro?', 'Je to vlastní membrána značky, která má zadržet vodu zvenčí a pustit ven vodní páru z těla. Konkrétní vodní sloupec a prodyšnost najdete v popisu modelu. Bundy bez označení membrány bývají jednodušší a hodí se spíš pro suchý a chladný den.'),
        ('Jak vybrat velikost dětské lyžařské bundy?', 'Podle výšky dítěte, ne podle věku. Změřte dítě bez bot, přidejte jedno číslo na vrstvy a zkontrolujte délku rukávů a zad. V katalogu se objevují velikosti od 116 do 164, které odpovídají výšce v centimetrech.'),
        ('Je dámská bunda Alpine Pro přiléhavá?', 'Dámské modely mají užší střih v pase a delší záda, často s prodlouženými rukávy. Pokud pod bundu oblékáte silnější vrstvy, vezměte o číslo větší nebo zvolte model s volnějším střihem. Ověřte velikostní tabulku konkrétního kusu.'),
        ('Do jaké zimy se hodí zateplená lyžařská bunda?', 'Rozhoduje zateplení a vaše aktivita. Při jízdě se zahřejete, takže stačí lehčí bunda a vrstvy pod ní. Při stání, s dětmi nebo v silnějším mrazu zvolte teplejší bundu a doplňte ji termoprádlem a rukavicemi.'),
        ('Hodí se bunda Alpine Pro i na snowboard?', 'Ano, lyžařské bundy fungují i na snowboardu. Snowboardisté většinou preferují volnější střih a delší rukávy, protože častěji sedají do sněhu. Zkontrolujte kapsy, sněhovou sukni a odolnost spodní části bundy.'),
        ('Je lepší péřová, nebo syntetická bunda?', 'Péřová je velmi teplá při nízké hmotnosti, ale pero nemá rádo vlhko. Syntetické zateplení drží teplo i navlhlé a snáší praní lépe. Na svah, kde se může sníh i tát, je praktičtější syntetika, na suchý mráz péřová.'),
        ('Jak praním neznehodnotit membránu?', 'Použijte prací prostředek pro funkční oblečení, bez aviváže, a vyperte při teplotě podle štítku. Zapněte zipy a vyprázdněte kapsy. Po vyprání lehce zahřejte, pokud to štítek dovolí, aby se obnovila vodoodpudivá úprava.'),
        ('Čím se Alpine Pro liší od Kilpi nebo Hannah?', 'Všechny tři značky patří ke střednímu okruhu a cílí na rekreační lyžaře. Rozdíl bývá ve střihu, barvách, řadách a dostupných velikostech. Neexistuje obecný vítěz, rozhoduje, co vám sedí a jaké vlastnosti potřebujete.'),
        ('Jak poznám, že bunda sedí i přes helmu?', 'Kapuce musí jít obléct přes helmu a nesmí omezovat výhled do stran. Zkuste ji s helmou na hlavě a pootočte se. Pokud při otočení zůstane kapuce na místě a nezakrývá zorné pole, je velikost vhodná.'),
    ],
)

# ------------------------------------------------------------------ jarni-a-podzimni-bundy-damske
NEW['jarni-a-podzimni-bundy-damske'] = dict(
    title='Jarní a podzimní bundy dámské: střih, materiál, vrstvení',
    desc='Dámské jarní a podzimní bundy: softshell, větrovka, lehce zateplená i nepromokavá. Jak vybrat střih, velikost a materiál podle počasí, pohybu a vrstvení.',
    intro='<p>Dámská bunda na přechodové období se nosí v dubnu i v říjnu, na dojíždění stejně jako na procházce se psem nebo na kole. Právě v tom je problém: musí chránit před větrem a deštěm, nesmí zbytečně hřát a přitom by neměla vypadat jako horolezecký pytel. '
          'Dámský střih navíc znamená víc než jen užší pas. Mění se délka rukávů, šířka ramen, délka v zádech i způsob, jak bunda sedí na bocích. '
          'V této nabídce najdete dámské modely z kategorie <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, od lehkých větrovek přes softshelly až po nepromokavé vrstvy a lehce zateplené kousky. Průvodce vysvětluje, jak se liší typy bund, jak správně zvolit velikost, jak bundu kombinovat s dalšími vrstvami a co sledovat u materiálu a střihu.</p>',
    guide='<h2>Dámský střih: v čem se liší od pánského</h2>'
          '<p>Většina značek staví dámské bundy na užší ramena, kratší záda a vyšší pas. Rukávy bývají kratší a hrudní část tvarovaná. U sportovních bund se mění i poměr mezi hrudí a boky: dámský střih zohledňuje, že boky bývají širší než pas. Rozdíl je nejvíc vidět u bund s vnitřním zapínáním nebo s kapucí. Štíhlé ženy občas ocení i pánský střih ve velikosti S, ale u delších ramen a rukávů může být komfortnější unisex nebo pánský model než dámský.</p>'
          + T(['Část bundy', 'Typická dámská úprava', 'Proč na tom záleží'], [
              ['Ramena', 'užší, nižší nasazení rukávu', 'rukávy nepadají přes rameno a neomezují pohyb paží'],
              ['Pas', 'zúžený nebo se šňůrkou na stažení', 'bunda lépe sedí na těle a méně fouká'],
              ['Délka', 'krátký střih nad boky, nebo delší přes zadek', 'delší model hřeje, kratší se hodí na kolo a do pasu'],
              ['Rukávy', 'o něco kratší, často s elastickou manžetou', 'netlačí na zápěstí a lépe sedí pod rukavicí'],
              ['Kapuce', 'menší, ale s dobrým stažením', 'nepadá přes oči a drží při větru']]) +
          '<p>Dámský střih nemusí být vždy lepší. Pokud máte širší ramena nebo delší trup, vyzkoušejte i pánský střih. Rozhoduje, jak se v bundě cítíte při předpažení a při zvednutí paží nad hlavu.</p>'
          '<h2>Typy bund pro přechodové období</h2>'
          '<p>Vybrat správný typ je důležitější než značka. V nabídce se mísí několik kategorií, které se v praxi chovají odlišně. Obecně tam je větrovka, softshell, lehce zateplená bunda, hardshell s membránou a prošívaná vesta nebo bunda. Základní informace o materiálech najdete v kategorii <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, tady se zaměříme na dámské použití.</p>'
          + T(['Situace', 'Doporučený typ', 'Doplněk'], [
              ['dojíždění do práce, město', 'softshell nebo lehká zateplená bunda s úpravou proti větru', 'šála nebo tenký nákrčník'],
              ['jízda na kole', 'větrovka nebo lehká membránová bunda, delší záda', 'cyklistický dres pod ní'],
              ['běh a svižná chůze', 'lehká větrovka nebo vesta', 'dlouhý rukáv pod ní'],
              ['turistika', 'softshell nebo lehká membrána v batohu', 'fleecová vrstva, pláštěnka'],
              ['procházka, výlet s dětmi', 'prošívaná nebo zateplená bunda s kapucí', 'čepice a rukavice'],
              ['zimní den na hraně přechodu', 'zateplená bunda se šněrováním v pase', 'termoprádlo, šála']]) +
          '<p>Chcete-li pokrýt víc situací jednou bundou, je nejuniverzálnější softshell. Pro déšť si pořiďte lehkou <a href="/nepromokave-bundy/">nepromokavou bundu</a>, kterou nosíte v batohu. Pro studené dny a delší pobyt venku se podívejte na <a href="/zimni-bundy/">zimní bundy</a>.</p>'
          '<h2>Značky v dámské nabídce</h2>'
          '<p>Mezi dámskými bundami najdete široké spektrum značek. Většinou zastoupené jsou ' + B(('trespass', 'Trespass'), ('regatta', 'Regatta'), ('northfinder', 'Northfinder'), ('silvini', 'Silvini')) + ', které nabízejí praktické modely pro každodenní nošení a rekreační turistiku. Výrazněji sportovní zaměření mají ' + B(('dare2b', 'Dare2b'), ('craft', 'Craft'), ('dynafit', 'Dynafit')) + ', zatímco ' + B(('haglofs', 'Haglöfs'), ('fjallraven', 'Fjällräven'), ('the-north-face', 'The North Face'), ('helly-hansen', 'Helly Hansen'), ('columbia', 'Columbia')) + ' cílí na outdoor a hory. Z českých značek jsou v nabídce také ' + B(('hannah', 'Hannah'), ('kilpi', 'Kilpi'), ('loap', 'Loap')) + '. Ke sportovnímu městskému stylu patří i ' + B(('adidas', 'Adidas'), ('nike', 'Nike')) + '.</p>'
          '<p>Značky se liší střihem, velikostmi a barvami, ale ne vždy kvalitou na první pohled. Ověřte vždy materiál, uvedenou odolnost vůči vodě a typ zapínání, ne jen jméno.</p>'
          '<h2>Jak vybrat velikost dámské bundy</h2>'
          '<p>Velikost bundy se neurčuje podle jednoho čísla. Důležité jsou tři míry: obvod hrudníku, obvod pasu a boků a délka rukávu od ramene po zápěstí. Porovnejte je s tabulkou konkrétní značky, protože označení S nebo M se u jednotlivých výrobců liší. Bunda má pojmout tenký svetr nebo funkční triko s dlouhým rukávem, ale nesmí tvořit vak. Pokud jste mezi velikostmi, zvolte větší, když plánujete vrstvení, nebo menší, když chcete přiléhavý sportovní střih.</p>'
          '<ul><li><strong>Zkouška pohybu:</strong> zvedněte ruce nad hlavu a předpažte, bunda nesmí vyjet nad pas.</li>'
          '<li><strong>Rukávy:</strong> po předpažení mají končit na zápěstí, ne uprostřed předloktí.</li>'
          '<li><strong>Délka v zádech:</strong> při předklonu nesmí odhalit spodní záda.</li>'
          '<li><strong>Ramena:</strong> švy sedí na okraji ramene, ne ve vzduchu nebo na paži.</li>'
          '<li><strong>Zapínání:</strong> při zapnutí na zip nesmí táhnout v prsou ani na žebrech.</li></ul>'
          '<h2>Vrstvení pod bundou</h2>'
          '<p>Na jaře a na podzim se teplota během dne výrazně mění. Proto jedna bunda málokdy stačí; fungují vrstvy. Základ tvoří tričko nebo funkční triko s dlouhým rukávem, nad ním tenký svetr nebo <a href="/fleecove-mikiny/">fleecová mikina</a> a nahoře bunda. Při pohybu odepnete nebo sundáte střední vrstvu. Pod bundu nenoste bavlněné tričko při sportu, protože vlhkost nevysychá a ochlazuje. Pokud potřebujete lehkou vrstvu mezi trikem a bundou, najdete ji v <a href="/funkcni-mikiny/">funkčních mikinách</a>.</p>'
          '<h2>Lehce zateplené a prošívané bundy</h2>'
          '<p>Prošívaná bunda s lehkým zateplením je oblíbená hlavně na podzim a v zimním přechodu. Prošití drží izolaci na místě, takže se nehromadí na jednom místě, a bunda se dá často složit do tašky. Dobře funguje ve městě, při zastávkách a při dojíždění. Při svižné chůzi do kopce se ale snadno přehřeje, proto ji doplňte jen tenkou spodní vrstvou. U modelů s kapucí si všimněte, jestli je zateplená i ona, a u modelů se stojáčkem, jestli neškrábe na krku. Pokud chcete přechodovou bundu hlavně na jaro, stačí tenčí zateplení nebo softshell s česanou podšívkou.</p>'
          '<h2>Kolik bund vlastně potřebujete</h2>'
          '<p>Nemusíte mít bundu na každé počasí. Pro většinu žen stačí dvě kombinace. První je pružný softshell nebo lehce zateplená bunda na běžný den, druhá lehká nepromokavá vrstva, která se vejde do kabelky nebo batohu. Třetí, sportovní bunda, přibývá až s konkrétním sportem: běžecká větrovka, cyklistická bunda s delšími zády nebo turistický hardshell. Sportovní model je vždy specializovanější, ale ve městě může působit praktičtěji než módní bunda. Do kombinace se hodí i <a href="/softshellove-bundy/">softshellové bundy</a> a širší výběr <a href="/sportovni-bundy/">sportovních bund</a>.</p>'
          '<h2>Péče a obnova impregnace</h2>'
          '<p>Bunda s vodoodpudivou úpravou nepotřebuje praní po každém nošení, ale po sezoně ji očistěte. Špína a pot zanášejí povrch a snižují prodyšnost i odpudivost vody. Perte ji na šetrný program, bez aviváže, a při sušení ji nechte volně viset. Pokud voda přestane perlit a nasákne do vnější látky, obnovte impregnaci sprejem nebo vložkou do pračky určenou pro funkční oblečení. Fleecové kousky pod bundu perte zvlášť, aby se nezapletly do suchého zipu a nevytvořily žmolky. K bundě se hodí i <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> stejné barevné řady.</p>'
          '<h2>Barvy a viditelnost</h2>'
          '<p>Podzim a časné jaro znamenají často šero a mlhu, proto se vyplatí zvolit bundu se světlejším nebo reflexním prvkem, zvlášť při jízdě na kole nebo běhu. Tmavé barvy jsou praktické ve městě a hůř ukazují špínu, světlé a výrazné lépe fungují v lese a na silnici. Reflexní prvky na zádech a rukávech zlepšují viditelnost bez toho, aby změnily vzhled bundy. Bunda s odnímatelnou kapucí nabízí větší univerzálnost pro město i výlet.</p>'
          '<h2>Co zkontrolovat v popisu produktu</h2>'
          '<p>Při srovnávání modelů dávejte pozor na údaje, které rozhodují o užitné hodnotě. Nezastavujte se u názvu typu bundy: jeden výrobce nazve softshellem lehkou membránu, jiný jen větrovku s úpravou. Kontrolujte složení materiálu, informaci o vodoodpudivé úpravě, přelepených švech a přítomnosti kapuce.</p>'
          '<ul><li><strong>Materiál:</strong> polyester, nylon a elastan; ověřte podíl a typ úpravy proti vodě.</li>'
          '<li><strong>Zateplení:</strong> pokud je uvedeno, zjistěte typ a hustotu; příliš teplá bunda se na jaře přehřívá.</li>'
          '<li><strong>Kapsy:</strong> na zip se hodí pro telefon, otevřené pro ruce.</li>'
          '<li><strong>Stažení:</strong> šňůrka v pasu a v kapuci zlepšují sedění a ochranu před větrem.</li>'
          '<li><strong>Sbalitelnost:</strong> některé větrovky se složí do vlastní kapsy a vejdou se do kabelky.</li></ul>'
          '<p>K bundě lze doplnit i <a href="/sportovni-vesty/">sportovní vesty</a> nebo <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>, pokud potřebujete lehčí vrstvu pro pohyb.</p>',
    faq=[
        ('Jakou bundu zvolit na jaro a podzim?', 'Nejuniverzálnější je softshell, protože dobře chrání před větrem, snese mrholení a je pružný. Pro déšť přibalte lehkou membránovou bundu, pro studené dny zvolte lehce zateplenou. Rozhodují také vaše aktivita a to, kolik se při ní zahřejete.'),
        ('Čím se dámská bunda liší od pánské?', 'Má užší ramena, kratší rukávy a záda, zúžený pas a prostornější boky. Rozdíl se nejvíc projeví u přiléhavých sportovních modelů. Pokud vám pánský střih sedí, můžete jej použít i jako dámský.'),
        ('Jak poznám, že je bunda dost prodyšná?', 'V popisu hledejte údaj o prodyšnosti nebo informaci o membráně. Pro aktivní sport zvolte prodyšnější materiál, třeba softshell nebo lehkou větrovku. Nepromokavé membrány s nízkou prodyšností jsou lepší na déšť než na běh.'),
        ('Jakou velikost bundy vybrat, když jsem mezi dvěma?', 'Pokud chcete bundu nosit přes svetr nebo mikinu, zvolte větší. Pokud chcete přiléhavý sportovní střih nebo na kolo, vyberte menší. Vždy ověřte velikostní tabulku značky a vyzkoušejte předpažení.'),
        ('Je lepší softshell, nebo větrovka?', 'Softshell je pružnější a teplejší, hodí se do chladnějších dnů a pro běžné nošení. Větrovka je lehčí a zabere méně místa, ale méně hřeje a hůře dýchá. Pro běh a kolo je lepší větrovka, pro město a výlet softshell.'),
        ('Jak vrstvit oblečení pod jarní bundu?', 'Základem je funkční nebo tenké bavlněné triko, nad ním tenký svetr nebo fleecová mikina a nahoře bunda. Při pohybu střední vrstvu odepnete. Při sportu se bavlně vyhněte, protože zadržuje vlhkost.'),
        ('Jak bundu prát, aby nepropouštěla vodu?', 'Perte šetrně, podle štítku, bez aviváže, která zanáší vodoodpudivou úpravu. Po vyprání můžete oživit impregnaci teplem nebo impregnačním sprejem určeným pro funkční oblečení. Zavřete všechny zipy.'),
        ('Mám brát bundu s kapucí?', 'Pro město a výlet se kapuce hodí, protože chrání před deštěm a větrem. Odnímatelná kapuce zvyšuje univerzálnost. Zkontrolujte, zda se dá stáhnout a nepadá přes oči.'),
        ('Je lepší tmavá, nebo světlá bunda?', 'Tmavé barvy jsou praktické ve městě a hůř ukazují špínu. Světlé a výrazné jsou lépe vidět v šeru, což oceníte na kole nebo při běhu. Reflexní prvky pomohou i u tmavých bund.'),
    ],
)

# ------------------------------------------------------------------ decathlon-damske-plavky
NEW['decathlon-damske-plavky'] = dict(
    title='Decathlon dámské plavky: surfové díly a kombinace',
    desc='Decathlon dámské plavky po dílech: horní díly, spodní díly na surf, brazilský střih, fulár. Jak vybrat velikost a kombinovat vrch se spodkem.',
    intro='<p>Dámské plavky Decathlon mají jednu zvláštnost, kterou na první pohled nepoznáte: většina nabídky jsou samostatné díly. Horní díl a spodní díl se kupují zvlášť, každý má vlastní velikost a vlastní střih, a vy si tak sestavíte dvoudílné plavky přesně pro svou postavu. '
          'V nabídce převažuje zaměření na surf a aktivní pobyt u vody: spodní díly s vyšším pasem, pevné držení, ale také trojúhelníkové horní díly a brazilské střihy. '
          'Na této stránce najdete plavky Decathlon z kategorie <a href="/damske-plavky/">dámské plavky</a>. Vysvětlíme, jak kombinovat díly, jak vybrat velikost zvlášť pro vrch a spodek, co znamená střih na surf a brazilský střih a čím se liší od klasických plaveckých modelů.</p>',
    guide='<h2>Proč se plavky kupují po dílech</h2>'
          '<p>Většina žen nemá stejnou velikost nahoře a dole. Obvod pod prsy a objem prsou určují horní díl, boky a sed zase spodní díl. Plavky prodávané po dílech tento problém řeší: horní díl vezmete třeba o číslo menší, spodní o číslo větší. Navíc můžete kombinovat barvy a vzory, takže jedny kalhotky se hodí k více vrchním dílům. U jednodílných plavek takovou volnost nemáte a při nesouladu postavy skončíte u kompromisu.</p>'
          '<p>Praktická výhoda se projeví i při poškození nebo opotřebení. Spodní díl se opotřebuje dřív, protože se na něm sedí na písku, na prkně nebo na hraně bazénu. Horní díl pak vydrží další sezonu. Při dokupování kontrolujte, zda se stejná řada prodává v obou dílech a v téže barvě.</p>'
          '<h2>Jak kombinovat horní a spodní díl</h2>'
          '<p>Při sestavování plavek je dobré dodržet několik zásad. Díly by měly být ze stejného nebo podobného materiálu, aby měly podobnou pružnost a schly stejně rychle. Pokud kombinujete vzorovaný a jednobarevný díl, zvolte vzor nahoře a jednobarevný dole, nebo naopak podle toho, co chcete zdůraznit. Dobře fungují také tlumené odstíny jedné barvy.</p>'
          + T(['Kombinace', 'Pro koho', 'Poznámka'], [
              ['trojúhelníkový horní díl + vyšší spodní díl', 'surf, paddleboard, aktivní pláž', 'pevné držení u spodku, horní díl se stavěním šňůrek'],
              ['horní díl s posuvnými trojúhelníky + klasický spodní díl', 'opalování a běžná pláž', 'posuvné trojúhelníky umožní upravit krytí'],
              ['fulárový horní díl + spodní díl s nohavičkami', 'plážové koupání, vodní sporty', 'nohavičky zakryjí víc a drží při pohybu'],
              ['horní díl bez ramínek + brazilský střih', 'opalování, plavba, dovolená', 'méně zakrytí, vhodné pro menší zátěž'],
              ['volánkový spodní díl + jednoduchý horní díl', 'rodinná pláž, koupání', 'volánky zvýrazní boky, nahoře stačí hladký díl']]) +
          '<p>Pokud hledáte plavky na pravidelné plavání v bazénu, najdete vhodnější modely mezi sportovními jednodílnými plavkami v kategorii <a href="/damske-plavky/">dámské plavky</a>. Decathlon v této nabídce dominuje v dvoudílných plavkách na vodu a surf.</p>'
          '<h2>Střih na surf a vyšší pas</h2>'
          '<p>V nabídce se často opakuje formulace „na surf“ a „se zvýšeným pasem“. Plavky na surf jsou navrženy tak, aby se při pohybu na prkně neposouvaly ani neujížděly. Spodní díl má vyšší pas nebo širší lem, který drží na kyčlích, a nohavičky chrání stehna před třením o prkno. Materiál bývá pevnější a hůř se bortí než u čistě módních plavek. Horní díl má často vícenásobné stažení nebo šněrování, které brání posunutí při pádu do vlny.</p>'
          '<ul><li><strong>Vyšší pas:</strong> drží na boku a při pohybu neklouže, zakrývá břicho a stehna.</li>'
          '<li><strong>Nohavičky:</strong> chrání pokožku před třením o prkno nebo písek.</li>'
          '<li><strong>Šněrování nebo posuvné prvky:</strong> umožní doladit sed a krytí.</li>'
          '<li><strong>Pevnější tkanina:</strong> snáší sůl, písek a slunce lépe než tenká módní látka.</li></ul>'
          '<p>Pokud jezdíte na paddleboard, na kajak nebo si vyrážíte na vodní lyže, hodí se stejná konstrukce. Pro delší pobyt na slunci doplňte plavky o <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> a pro aktivní vodní sporty o výbavu v kategorii <a href="/vodni-sporty/">vodní sporty</a>.</p>'
          '<h2>Brazilský střih, volánky a trojúhelníky</h2>'
          '<p>Slovo střih v názvu produktu popisuje, kolik látky spodní díl obsahuje. Brazilský střih má užší zadní část a zakrývá méně, což oceníte při opalování. Klasický střih zakrývá víc, takže je vhodný pro běžnou pláž a koupání. Díl s nohavičkami je nejpraktičtější na vodní sporty. Spodní díl s volánky vizuálně rozšiřuje boky a hodí se tam, kde chcete střih trochu vyvážit.</p>'
          + T(['Střih', 'Zakrytí', 'Hodí se na'], [
              ['brazilský', 'menší', 'opalování, dovolená, lehké koupání'],
              ['klasický', 'střední', 'pláž, rodinné koupání, univerzální použití'],
              ['s nohavičkami', 'větší', 'surf, paddleboard, aktivní sporty'],
              ['s vyšším pasem', 'větší v pase', 'surf, pohodlí, zakrytí břicha'],
              ['s volánky', 'střední', 'plážové koupání, módní dojem']]) +
          '<p>Horní díl trojúhelníkový je nejuniverzálnější a jde nastavit šňůrkami. Horní díl s posuvnými trojúhelníky umožní měnit krytí. Fulárový horní díl bývá ozdobený a hodí se na pláž, kde se řeší vzhled. Při větším objemu prsou hledejte horní díly s širším pásem pod prsy a s ramínky, která nesklouzávají.</p>'
          '<h2>Velikost zvlášť pro horní a spodní díl</h2>'
          '<p>Velikost si změřte dvakrát. Horní díl se řídí obvodem pod prsy a přes prsa, spodní obvodem boků a pasu. U každého dílu porovnejte hodnoty s tabulkou výrobce. Plavky mají sedět pevně, aby se při pohybu ve vodě neposouvaly, ale nesmí zařezávat do kůže. Po namočení se tkanina lehce uvolní.</p>'
          '<ul><li><strong>Horní díl:</strong> pás pod prsy nesmí tlačit ani ujíždět, košíčky nemají vytvářet prázdná místa.</li>'
          '<li><strong>Spodní díl:</strong> lem nesmí zařezávat do boků a při sedu na prkno se nesmí sunout dolů.</li>'
          '<li><strong>Zkouška pohybu:</strong> předkloňte se, zvedněte ruce a zkuste dřep, díly musí zůstat na místě.</li>'
          '<li><strong>Pozor na rozdílné velikosti:</strong> horní a spodní díl nemusí mít stejné označení, proto kontrolujte každý zvlášť.</li></ul>'
          '<h2>Materiál a péče</h2>'
          '<p>Plavky obsahují směs syntetického vlákna a elastanu. Elastan je citlivý na chlór, slunce, olej na opalování i teplo, a proto plavky po koupání opláchněte čistou vodou, vymáchejte je a sušte ve stínu. Nežehlete je a nesušte v sušičce. Na surf a u moře je důležité odstranit písek a sůl, které působí jako brusivo. Plavky nenechávejte mokré v tašce, protože tkanina i barvy rychle trpí.</p>'
          '<p>Pokud plavete v chlorované vodě, počítejte s kratší životností módních plavek. Pro pravidelný trénink jsou vhodnější plavky určené do bazénu, například z nabídky značek ' + B(('speedo', 'Speedo'), ('arena', 'Arena')) + '. Decathlon se v této nabídce soustředí na plavky pro pláž, vodu a surf.</p>'
          '<h2>Decathlon v porovnání s dalšími značkami</h2>'
          '<p>Při výběru plavek se vyplatí porovnat více značek. Decathlon v katalogu zastupuje praktické, sportovně laděné dvoudílné plavky, které se prodávají po dílech. Značka ' + B(('roxy', 'Roxy')) + ' nabízí surfově a plážově laděné modely s módním stylem, ' + B(('calvin-klein', 'Calvin Klein')) + ' městský módní styl. Ostatní značky najdete na samostatných stránkách <a href="/damske-plavky-roxy/">dámské plavky Roxy</a> a <a href="/damske-plavky-calvin-klein/">dámské plavky Calvin Klein</a>. Nabídky se liší střihem, kvalitou materiálu a způsobem prodeje.</p>'
          '<h2>Plavky na plážový den a na aktivní den u vody</h2>'
          '<p>Plážový den a surfování vyžadují jiné plavky, i když vypadají podobně. Na pláž stačí lehčí díly, u nichž hlavně řešíte pohodlí při ležení a opalování. Při aktivním dni, tedy surfování, paddleboardu nebo plavbě na kajaku, potřebujete pevnější spodní díl, vyšší lem a horní díl, který se nesvlékne při pádu. Praktické je mít dvě kombinace: jednu pevnou a jednu pohodlnou. Aktivní kombinaci stačí vyprat a nechat uschnout, plážová vyžaduje opatrnější péči. Nezapomeňte si zabalit i náhradní spodní díl, protože mokré plavky v batohu zahřívají a po několika hodinách nepříjemně chladí.</p>'
          '<h2>Jak vybírat podle postavy</h2>'
          '<p>Při užší postavě a menším objemu prsou stačí trojúhelníkový horní díl s jednoduchým stahováním. Při větším objemu hledejte širší pás a pevnější ramínka. Pokud chcete opticky zvýraznit pas, zvolte vyšší spodní díl s hladkým lemem, pokud chcete vyvážit boky, pomůže volánek nebo vzor u horního dílu. Vždy si nejdříve prohlédněte, jaký zadní střih spodek má, a porovnejte jej s rozměry svého těla.</p>'
          '<h2>Co dalšího se hodí k plavkám</h2>'
          '<p>K plavkám patří i další výbava na vodu a pláž. <a href="/plazove-doplnky/">Plážové doplňky</a> pomohou s pobytem na písku, <a href="/obuv-do-vody/">obuv do vody</a> chrání nohy při vstupu do moře nebo řeky a <a href="/plavecke-bryle/">plavecké brýle</a> použijete při plavání. Pro rodinu si prohlédněte <a href="/detske-plavky/">dětské plavky</a> a <a href="/panske-plavky/">pánské plavky</a>.</p>',
    faq=[
        ('Prodávají se plavky Decathlon po dílech?', 'Ano, v nabídce převažují samostatné horní a spodní díly. Každý díl má vlastní velikost, takže si můžete sestavit plavky podle svých měr. Při nákupu kontrolujte, zda se stejná řada prodává v obou dílech.'),
        ('Mohu kombinovat horní a spodní díl různých velikostí?', 'Ano, to je hlavní výhoda dílů. Horní díl se řídí obvodem pod prsy a objemem, spodní obvodem boků. Velikosti proto vybírejte zvlášť podle tabulky výrobce a nepředpokládejte, že označení musí být shodné.'),
        ('Co znamená střih na surf u plavek?', 'Plavky na surf mají vyšší pas, nohavičky a pevnější držení, aby se při pohybu na prkně neposouvaly a chránily pokožku před třením. Šněrování nebo posuvné prvky umožní doladit sed.'),
        ('Čím se liší brazilský střih od klasického?', 'Brazilský má užší zadní část a zakrývá méně, hodí se na opalování. Klasický střih zakrývá víc a je univerzální na pláž. Pro aktivní sporty zvolte raději spodní díl s nohavičkami nebo vyšším pasem.'),
        ('Hodí se plavky Decathlon do bazénu?', 'Spíš ne pro pravidelný trénink. Módní plavky obsahují elastan citlivý na chlór a rychle ztrácejí tvar. Pro bazén vyberte plavky určené k plavání, které jsou odolnější. Surfové a plážové modely patří k vodě a pláži.'),
        ('Jak vybrat horní díl při větším objemu prsou?', 'Hledejte širší pás pod prsy, pevnější košíčky a ramínka, která nesklouzávají. Posuvné trojúhelníky a šněrování pomohou přizpůsobit tvar. Při výběru velikosti sledujte obvod pod prsy i přes prsa.'),
        ('Jak plavky prát a sušit?', 'Po koupání je opláchněte čistou vodou, vymáchejte a sušte ve stínu. Nesušte v sušičce a nežehlete. Po pobytu na písku odstraňte zbytky písku a soli, které tkaninu poškozují.'),
        ('Co jsou fulárové plavky?', 'Jde o označení pro horní díl s volnějším, často zdobeným střihem a lehkou látkou, který se hodí na pláž, kde se řeší vzhled. Pro aktivní sport zvolte horní díl s pevnějším držením.'),
        ('Jak poznám správnou velikost spodního dílu?', 'Změřte obvod boků a pasu a porovnejte hodnoty s tabulkou výrobce. Spodní díl má sedět pevně, ale nesmí zařezávat. Zkuste dřep a předklon, aby se lem neposouval dolů.'),
    ],
)
