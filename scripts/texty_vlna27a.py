"""sporteka.cz — wave 27a (16. 11. 2026): long texts for elektrolyty, multivitaminy, l-karnitin, probiotika.
General true facts only, health claims only in the wording of authorised EU claims (Reg. 432/2012), no prices, no dosing advice.
L-carnitine and probiotics have no authorised claim — said plainly. Brands with an indexed page (znacky.json): gymbeam, insportline;
other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ elektrolyty
NEW['elektrolyty'] = dict(long=True,
    title='Elektrolyty a solné tablety: prášky, šumivky, kapsle',
    desc='Elektrolyty v prášku, šumivých tabletách, kapslích i kapkách. Kolik sodíku na porci, rozdíl proti iontovému nápoji a nabídky českých obchodů.',
    intro='<p>Elektrolyty jsou minerální látky, které v tělních tekutinách nesou elektrický náboj: především sodík, draslík, chlorid, hořčík a vápník. S potem z těla odcházejí spolu s vodou a ze všech nejvíc sodíku. Kdo trénuje dlouho, v teple nebo se prostě hodně potí, proto k vodě často přidává i soli. Doplňky v této kategorii se od klasických iontových nápojů liší hlavně tím, že cukru obsahují málo nebo vůbec, a soustředí se na samotné minerály.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů, objednávku ale dokončíte přímo v obchodě, který si vyberete. Najdete tu prášky k rozmíchání, šumivé tablety, solné kapsle, koncentrované kapky i hotové tekuté nápoje. Zastoupené jsou značky ATP Nutrition, Pulse Performance, Nutrend, Enervit, Isostar, Sponser, OlaOla, Flow Nutrition, Science in Sport, Elete nebo Extrifit. Nadřazenou kategorií jsou <a href="/iontove-napoje/">iontové nápoje</a>, souvisejí s ní také <a href="/horcik/">hořčík</a> a <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>.</p>',
    guide='<h2>Které minerály patří mezi elektrolyty</h2>'
          '<p>Hlavním minerálem potu je sodík, v menší míře člověk ztrácí draslík, chlorid, hořčík a vápník. Množství sodíku v potu se mezi lidmi výrazně liší. Někomu po tréninku zůstanou na tričku nebo na kšiltovce bílé solné mapy, jiný je nemá skoro nikdy. Proto neexistuje jedno množství elektrolytů, které by sedělo všem, a výrobky se mezi sebou obsahem sodíku liší i několikanásobně.</p>'
          '<p>U jednotlivých minerálů schválila Evropská unie tato zdravotní tvrzení: draslík přispívá k normální činnosti svalů, k normální činnosti nervové soustavy a k udržení normálního krevního tlaku. Hořčík přispívá k elektrolytické rovnováze a k normální činnosti svalů. Vápník také přispívá k normální činnosti svalů. Pro sodík přidávaný do výrobku žádné zdravotní tvrzení schválené není, i když ho tělo potem ztrácí nejvíc. Evropský úřad pro bezpečnost potravin sice uznal, že sodík přispívá k normální činnosti svalů, Evropská komise ale toto tvrzení neschválila. Podle ní by spotřebitele mátlo, protože sodíku má většina lidí v jídelníčku spíš nadbytek. Jediné schválené tvrzení spojené se sodíkem se týká naopak sníženého příjmu sodíku a udržení normálního krevního tlaku. Výrobce smí tvrzení použít jen tehdy, když výrobek daný minerál obsahuje ve významném množství.</p>'
          '<h2>Roztoky sacharidů a elektrolytů: dvě tvrzení s podmínkami</h2>'
          '<p>Pro nápoje, které spojují sacharidy se sodíkem, existují dvě schválená tvrzení. Roztoky sacharidů a elektrolytů přispívají k udržení vytrvalostního výkonu během dlouhodobého vytrvalostního cvičení. A roztoky sacharidů a elektrolytů zlepšují vstřebávání vody během fyzického cvičení. Výrobek je ale smí uvést jen při splnění přesných podmínek. Hotový nápoj musí obsahovat 80 až 350 kcal na litr ze sacharidů. Nejméně 75 % energie musí pocházet ze sacharidů s vysokým glykemickým účinkem, například z glukózy, jejích polymerů nebo sacharózy. Sodíku musí být 20 až 50 mmol na litr, tedy zhruba 460 až 1150 mg, a osmolalita musí být 200 až 330 mOsm na kilogram vody.</p>'
          '<p>Elektrolyty bez cukru tyto podmínky z principu nesplní, protože jim chybí sacharidy. Pokud na takovém výrobku vidíte slib lepšího výkonu, schválené tvrzení to není. Přípravky se sacharidy hledejte spíš v kategorii <a href="/iontove-napoje/">iontové nápoje</a>; zde převažují směsi minerálů s minimem cukru, i když několik nápojů s maltodextrinem se najde i tady.</p>'
          '<h2>Formy elektrolytů v nabídce</h2>'
          + T(['Forma', 'Jak se používá', 'Na co se dívat'], [
              ['Prášek', 'rozmíchá se ve vodě podle odměrky', 'sodík na porci, cukr nebo sladidla'],
              ['Šumivé tablety', 'tableta se rozpustí ve sklenici nebo v lahvi', 'počet tablet v tubě, sodík ze šumivé složky'],
              ['Solné kapsle (salt caps)', 'polykají se a zapíjejí vodou', 'množství sodíku na jednu kapsli'],
              ['Tablety k polykání', 'podobně jako kapsle, bez rozpouštění', 'kolik tablet tvoří jednu porci'],
              ['Koncentrované kapky', 'přidávají se po kapkách do vody', 'obsah na kapku a na mililitr'],
              ['Hotový nápoj', 'tekutina připravená k pití', 'objem, obsah cukru, konzervanty'],
              ['Elektrolyty s kofeinem', 'minerály spolu s kofeinem', 'množství kofeinu na porci']]) +
          '<h2>Elektrolyty, nebo iontový nápoj?</h2>'
          '<p>Hranice mezi oběma skupinami není ostrá a obchody je často řadí dohromady. Iontový nápoj obvykle obsahuje sacharidy, tedy energii, a k tomu sodík. Elektrolyty bez cukru dodávají jen minerály a hodí se tam, kde energii nepotřebujete nebo ji berete z gelů a tyčinek. Při hodinovém tréninku v posilovně většině lidí obvykle stačí obyčejná voda. Při několikahodinovém běhu, cyklistické vyjížďce nebo na túře se může hodit spojení energie a solí.</p>'
          '<p>Podle koncentrace rozpuštěných látek se nápoje dělí na hypotonické, izotonické a hypertonické. Izotonický nápoj má podobnou koncentraci jako krevní plazma, hypotonický má nižší koncentraci a hypertonický vyšší, typicky kvůli vyššímu podílu sacharidů. Tonicitu ale ovlivníte sami. Stejný prášek rozmíchaný v menším množství vody bude koncentrovanější, než výrobce počítal.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<ul><li><strong>Sodík v miligramech na porci:</strong> nejdůležitější údaj. Některé obaly uvádějí v tabulce sůl, ne sodík; sodík tvoří zhruba 40 % hmotnosti soli.</li>'
          '<li><strong>Další minerály:</strong> draslík, hořčík, vápník a chlorid v miligramech a v procentech referenční hodnoty příjmu.</li>'
          '<li><strong>Porce a počet porcí:</strong> u prášku hmotnost balení dělená odměrkou, u šumivek počet tablet v tubě.</li>'
          '<li><strong>Cukr a sladidla:</strong> varianty bez cukru bývají slazené sukralózou, acesulfamem K nebo steviolglykosidy.</li>'
          '<li><strong>Kofein a další přísady:</strong> vitamíny skupiny B, taurin, aroma, barviva.</li>'
          '<li><strong>Forma minerálu:</strong> citráty se ve vodě rozpouštějí dobře, oxid hořečnatý hůř a může zanechat usazeninu.</li></ul>'
          '<h2>Proč se o elektrolytech mluví i v zimě</h2>'
          '<p>Pot není jen letní záležitost. V lednu, kdy se mnoho lidí vrací k pravidelnému cvičení s novoročním předsevzetím, se trénuje hlavně uvnitř: na spinningu, na běžeckém pásu, v posilovně nebo ve sportovní hale. Kdo jezdí doma na trenažéru bez ventilátoru, se zpotí víc, než by čekal, protože chybí proudění vzduchu, které pot odvádí. Na horách se zase člověk při skialpinismu nebo na běžkách zpotí pod několika vrstvami oblečení a ani si toho nevšimne.</p>'
          '<p>Vytápěné byty a kanceláře mají suchý vzduch a v chladu navíc obvykle pociťujeme menší žízeň. Základem zůstává pravidelné pití vody během dne. Elektrolyty dávají smysl hlavně po delším nebo intenzivním tréninku, kdy se výrazně zpotíte. Na běžný den v kanceláři je nepotřebujete.</p>'
          '<h2>Kdy dát pozor</h2>'
          '<p>Sodíku má běžný jídelníček spíš nadbytek, protože sůl je v pečivu, uzeninách, sýrech i hotových jídlech. Elektrolyty proto nepatří k nápojům, které by se měly pít celý den místo vody. Lidé s vysokým krevním tlakem, s onemocněním srdce nebo ledvin a ti, kdo drží dietu s omezením soli, by se měli o užívání poradit s lékařem. U některých léků na tlak a srdce je navíc potřeba hlídat příjem draslíku. Totéž platí pro těhotné a kojící ženy a pro děti. Velikost porce a jejich počet za den stanoví etiketa výrobku, nepřekračujte je.</p>'
          '<p>Opačným problémem je hyponatrémie, tedy příliš nízká hladina sodíku v krvi. Při velmi dlouhém výkonu, například při maratonu nebo ultramaratonu, k ní může vést pití velkého množství čisté vody nad rámec ztrát potem. Hlavní prevencí je nepít víc, než kolik potem ztrácíte. Sodík v nápoji nebo solné kapsle nadměrné pití nevyváží. Pít „do zásoby“ proto není řešení; rozumnější je pít podle žízně a podle plánu, který máte vyzkoušený z tréninku.</p>'
          '<h2>Solné kapsle na závody</h2>'
          '<p>Kapsle jako Enervit Salt Caps, Nutrend Salt Caps nebo Extrifit Electrolyte Salt Caps si oblíbili běžci, cyklisté a triatlonisté. Nemění chuť toho, co pijete, a vejdou se do kapsy dresu nebo do běžecké vesty. Nevýhodou je, že každou kapsli musíte zapít a hůř se rozkládá příjem soli v čase. Žádný nový přípravek nezkoušejte poprvé na závodě; trávení při výkonu reaguje na neznámé věci citlivě.</p>'
          '<h2>Prášek, šumivka, nebo kapky</h2>'
          '<p>Prášek vychází na jednu porci obvykle nejlépe a jeho množství si upravíte. Velké dózy, třeba 900 g, se hodí pro ty, kdo trénují často, sáčky na vyzkoušení chutí. Šumivé tablety se snadno nosí a rozpustí se přímo v lahvi; šumivá složka bývá na bázi hydrogenuhličitanu a často sama přidává sodík. Kapky typu Elete jsou koncentrát, který se přidává do vody nebo jiného nápoje, a jedno balení vystačí na mnoho litrů. Hotové nápoje jsou pohodlné, jen s nimi vozíte hlavně vodu.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Porovnávání soli a sodíku bez přepočtu.</li>'
          '<li>Pití elektrolytů po celý den místo obyčejné vody.</li>'
          '<li>První vyzkoušení nového přípravku až na závodě.</li>'
          '<li>Přehlédnutý kofein ve složení u večerního tréninku.</li>'
          '<li>Souběh s dalším doplňkem hořčíku, takže ho přijmete víc, než jste chtěli.</li>'
          '<li>Míchání hustšího nápoje, než uvádí výrobce, ve snaze „přidat“.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky několika českých obchodů vedle sebe, včetně dopravy a dostupnosti, a objednávku pak dokončíte přímo v e-shopu. U elektrolytů vybírejte nejdřív podle obsahu sodíku na porci a podle formy, která vám sedí při tréninku, a teprve potom podle příchuti. Šumivé tablety držte v dobře zavřené tubě, protože vlhko je znehodnotí, a prášek nabírejte vždy suchou odměrkou. Pro vytrvalostní výkony se podívejte i na <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a na <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi elektrolyty a iontovým nápojem?', 'Iontový nápoj obvykle obsahuje sacharidy a k nim sodík, takže dodává i energii. Elektrolyty bez cukru dodávají jen minerály. Obchody obě skupiny často řadí dohromady, proto rozhoduje složení na etiketě.'),
        ('Kdy dává smysl pít elektrolyty?', 'Hlavně při delším nebo intenzivním výkonu, při kterém se výrazně potíte, například při dlouhém běhu, na kole nebo při skialpinismu. Při krátkém tréninku většině lidí stačí voda.'),
        ('Proč je důležitý hlavně sodík?', 'Sodíku obsahuje pot nejvíc ze všech minerálů. Tvrzení o sodíku a činnosti svalů ale EU neschválila, protože by odporovalo doporučení jíst soli méně. Schválená tvrzení mají například draslík a hořčík.'),
        ('Jak přepočítám sůl na sodík?', 'Sodík tvoří zhruba 40 % hmotnosti soli. Pokud etiketa uvádí sůl, vynásobte údaj 0,4 a dostanete přibližné množství sodíku.'),
        ('Jsou solné kapsle lepší než prášek?', 'Kapsle nemění chuť pití a dobře se nosí na závodech, prášek se snáz dávkuje a obvykle vychází na porci lépe. Volba záleží na tom, jak a kde je chcete užívat.'),
        ('Mohu elektrolyty pít místo vody celý den?', 'Nedoporučuje se to. Běžný jídelníček obsahuje sodíku dost, elektrolyty patří hlavně k delšímu výkonu. Množství porcí za den určuje etiketa výrobku.'),
        ('Pro koho elektrolyty nejsou vhodné bez porady s lékařem?', 'Pro lidi s vysokým krevním tlakem, s onemocněním srdce nebo ledvin, pro ty, kdo drží dietu s omezením soli nebo užívají léky, a také pro těhotné, kojící ženy a děti.'),
        ('Proč řešit pití i v zimě?', 'V chladu obvykle pociťujeme menší žízeň a vytápěné místnosti mají suchý vzduch. Při tréninku v hale, na trenažéru nebo pod vrstvami oblečení na horách se přitom člověk dokáže výrazně zpotit.'),
    ])

# ------------------------------------------------------------------ multivitaminy
NEW['multivitaminy'] = dict(long=True,
    title='Multivitamíny: pro ženy, muže i děti, tablety a želé',
    desc='Multivitamíny v tabletách, kapslích, želé i tekuté formě. Jak číst % RHP a formy minerálů, čím se liší řady pro ženy a muže a nabídky českých obchodů.',
    intro='<p>Multivitamín spojuje v jedné tabletě nebo kapsli více vitamínů a obvykle i minerálů. Lidé po něm sahají, když si nejsou jistí, že jim jídelníček všechno pokryje, nebo když nechtějí kupovat pět samostatných doplňků. Mezi výrobky jsou ale velké rozdíly v počtu látek, v jejich množství i ve formách, které výrobce zvolil. Dvě krabičky se stejným nápisem tak mohou mít velmi odlišné složení a výběr se vyplatí udělat podle tabulky na obalu, ne podle názvu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů, nákup pak proběhne přímo v e-shopu, který si zvolíte. V kategorii jsou multivitamíny pro muže, ženy, těhotné, děti i seniory, a to v tabletách, kapslích, želé, šumivých tabletách i v tekuté liposomální formě. Nabízejí je značky jako ' + B(('gymbeam', 'GymBeam')) + ', ATP Nutrition, Weider, BioTech USA, Applied Nutrition, Viridian, GreenFood Nutrition, Advance Nutraceutics, MedPharma, Terezia nebo ' + B(('insportline', 'Insportline')) + '. Samostatné látky najdete v nadřazené kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a> a dále v kategoriích <a href="/vitamin-d/">vitamín D</a>, <a href="/zinek/">zinek</a> a <a href="/horcik/">hořčík</a>.</p>',
    guide='<h2>Co je multivitamín a co od něj čekat</h2>'
          '<p>Multivitamín je doplněk stravy, tedy potravina, která má běžný jídelníček doplnit, ne nahradit. Zelenina, ovoce, luštěniny a celozrnné výrobky dodávají kromě vitamínů i vlákninu a další látky, které v tabletě nejsou. Pro multivitamín jako celek žádné zdravotní tvrzení neexistuje. Schválená tvrzení se vždy vztahují ke konkrétní složce a výrobce je smí použít jen tehdy, když jí výrobek obsahuje dostatek.</p>'
          '<p>Několik příkladů z unijního seznamu: vitamín C, vitamín B6, vitamín B12, kyselina listová, železo a hořčík přispívají ke snížení míry únavy a vyčerpání. Jód přispívá k normální tvorbě hormonů štítné žlázy a k normální činnosti štítné žlázy. Selen přispívá k ochraně buněk před oxidativním stresem. Kyselina listová přispívá k růstu mateřských tkání během těhotenství. Jde o popis role, kterou látka v těle hraje, nikoli o slib, že se po multivitamínu budete cítit jinak.</p>'
          '<h2>Jak číst tabulku složení</h2>'
          '<p>U každé látky najdete množství v miligramech nebo mikrogramech a procento referenční hodnoty příjmu, zkráceně RHP, anglicky NRV. Referenční hodnota je orientační údaj pro průměrného dospělého, ne osobní doporučení. Sto procent u vitamínu neznamená, že je přípravek kvalitnější, a tisíc procent už není výhoda, jen vysoké množství.</p>'
          '<ul><li><strong>Počet složek:</strong> 20 nebo 30 látek zní dobře, rozhoduje ale, kolik každé z nich porce obsahuje. Hořčíku a vápníku bývá v multivitamínech málo, protože by se potřebné množství do jedné tablety nevešlo.</li>'
          '<li><strong>Velikost porce:</strong> některé přípravky se užívají jednou denně, jiné po dvou až třech kapslích. Balení 90 kapslí pak nemusí vydržet 90 dní.</li>'
          '<li><strong>Formy minerálů:</strong> cheláty a citráty, nebo levnější oxidy a uhličitany.</li>'
          '<li><strong>Formy vitamínů:</strong> kyselina listová, nebo methylfolát; kyanokobalamin, nebo methylkobalamin; retinol, nebo beta-karoten.</li>'
          '<li><strong>Železo a jód:</strong> ne každý multivitamín je obsahuje a ne každý člověk je potřebuje.</li>'
          '<li><strong>Pomocné látky:</strong> cukr, sladidla, barviva, želatina nebo rostlinný obal kapsle.</li></ul>'
          '<h2>Formy multivitamínů</h2>'
          + T(['Forma', 'Výhoda', 'Na co si dát pozor'], [
              ['Tablety', 'nejvíc látek v jednom kusu, dlouhá trvanlivost', 'bývají velké, obsahují pojiva'],
              ['Kapsle', 'neutrální chuť, želatinové i rostlinné', 'na porci jich často potřebujete víc'],
              ['Želé a gumoví medvídci', 'dobrá chuť, oblíbené u dětí', 'cukr nebo sladidla, méně minerálů'],
              ['Šumivé tablety', 'rozpustí se ve vodě', 'šumivá složka obvykle přidává sodík'],
              ['Tekuté a liposomální', 'pro ty, kdo nechtějí polykat', 'po otevření dodržet uchování podle etikety'],
              ['Prášek k rozmíchání', 'přidá se do nápoje nebo šejku', 'porce podle odměrky, příchutě a sladidla'],
              ['Instantní nápoje a hroznový cukr s vitamíny', 'spíš osvěžení než plnohodnotný multivitamín', 'kolik obsahují cukru']]) +
          '<h2>Pro ženy, pro muže, pro seniory: rozdíl, nebo marketing?</h2>'
          '<p>Část rozdílů je skutečná. Řady pro ženy v plodném věku mívají železo a kyselinu listovou, protože ženy železo ztrácejí menstruací. Přípravky pro muže a pro seniory železo často vynechávají nebo ho obsahují méně. Řady pro seniory zase mívají více vitamínu D a B12, protože vstřebávání B12 z potravy s věkem slábne. Jinde je rozdíl hlavně v barvě krabičky, takže před nákupem porovnejte samotnou tabulku složení.</p>'
          '<p>Těhotenské multivitamíny, například Trime Pregnancy Essentials nebo Viridian Pregnancy Formula, stavějí na kyselině listové a jódu. Vitamín A ve formě retinolu v nich výrobci obvykle omezují nebo ho nahrazují beta-karotenem, protože vysoké dávky retinolu jsou v těhotenství rizikové. Výběr doplňku v těhotenství a při kojení ale patří k lékaři nebo lékárníkovi, ne k náhodnému nákupu.</p>'
          '<h2>Dětské multivitamíny</h2>'
          '<p>Pro děti jsou určeny gumové bonbony, želatinky jako Terezia Rakytníček, Penco Junior, Vitar Kids nebo Viridikid od Viridianu. Obsah látek je přizpůsobený věku, proto dětem nedávejte přípravek pro dospělé a u každého výrobku zkontrolujte, od kolika let je určen. Želé ukládejte mimo dosah dětí, protože vypadá jako sladkost a dítě ho může sníst víc najednou. Zvlášť nebezpečné je u malých dětí předávkování železem. Pokud si nejste jistí, poraďte se s pediatrem.</p>'
          '<p>V kategorii se mohou objevit i multivitamíny pro psy a kočky, například z řady MOVit PET. Jsou určené zvířatům, ne lidem, a obráceně zvířatům nedávejte přípravky pro lidi.</p>'
          '<h2>Cheláty, methylfolát a další „lepší“ formy</h2>'
          '<p>Prémiové řady, například GreenFood Multi VitaMin Chelate nebo různé „Premium Chelate“ kapsle, zdůrazňují chelátové minerály a aktivní formy vitamínů. Chelát znamená minerál navázaný na aminokyselinu, nejčastěji glycin, a výrobci ho uvádějí jako šetrnější k žaludku. Methylfolát je forma folátu, kterou tělo nemusí přeměňovat, a vyhledávají ji lidé, kteří chtějí přeměnu kyseliny listové obejít. Methylkobalamin je jedna z forem vitamínu B12, které tělo přímo využívá, kyanokobalamin je stabilnější forma, kterou si tělo přemění. Rozdíly ve vstřebávání mezi formami existují, u zdravého člověka se ale často přeceňují. Důležitější je, kolik látky porce obsahuje.</p>'
          '<h2>Kolik je moc: pozor na souběh doplňků</h2>'
          '<p>Vitamíny rozpustné v tucích, tedy A, D, E a K, se v těle ukládají a při dlouhodobém nadbytku se mohou hromadit. Riziko obvykle nevzniká z jednoho přípravku, ale ze souběhu: multivitamín, samostatný vitamín D, zinek, směs na imunitu a k tomu obohacený proteinový nápoj. Sečtěte si proto, kolik které látky dostáváte ze všech výrobků dohromady. Kuřáci by se měli vyhnout přípravkům s vysokým obsahem beta-karotenu.</p>'
          '<p>Vitamín K může ovlivnit účinek léků na ředění krve a vápník, železo nebo hořčík mohou snížit vstřebávání některých antibiotik a léků na štítnou žlázu. Těhotné a kojící ženy, rodiče malých dětí, lidé s chronickým onemocněním a ti, kdo užívají léky, by se proto měli o multivitamínu poradit s lékařem nebo lékárníkem. Kolik tablet denně, určuje etiketa.</p>'
          '<h2>Proč se o multivitamínech mluví v lednu</h2>'
          '<p>S novým rokem si mnoho lidí předsevezme víc cvičit a méně jíst. Redukční jídelníček s menšími porcemi ale znamená i menší přísun vitamínů a minerálů, zvlášť když z něj člověk vyřadí celé skupiny potravin. V zimě navíc jíme méně čerstvé sezonní zeleniny a víc času trávíme uvnitř. Multivitamín může v takové situaci posloužit jako pojistka, rozumnější je ale nejdřív upravit jídelníček tak, aby zůstal pestrý i v dietě. Vitamín D, který se v zimě řeší nejčastěji, najdete samostatně v kategorii <a href="/vitamin-d/">vitamín D</a>.</p>'
          '<h2>Multivitamín a sport</h2>'
          '<p>Sportovní řady, například ATP Vitality Multivitamin, Weider Multivitamin Complete nebo Applied Nutrition Multi-Vitamin Complex, se od běžných liší obvykle vyšším obsahem vitamínů skupiny B, víc hořčíku nebo přidanými extrakty. Vyšší výdej energie ale většinou znamená i víc jídla a s ním víc vitamínů. Speciální sportovní multivitamín tedy nepotřebuje každý, kdo chodí do posilovny. Když trénujete hodně a jíte jednotvárně, poslouží jako pojistka. K němu si můžete přidat <a href="/omega-3/">omega-3</a> nebo <a href="/proteiny/">protein</a>, pokud vám v jídelníčku chybějí.</p>'
          '<h2>Vegani a vegetariáni</h2>'
          '<p>Veganské multivitamíny, jako BioTech USA Vegan Multivitamin nebo rostlinné kapsle Masmusculo, mají obal kapsle z celulózy a vitamín D3 z lišejníků nebo D2. Pro vegany je klíčový vitamín B12, který se v rostlinné stravě přirozeně prakticky nevyskytuje. Zkontrolujte jeho obsah a také to, zda přípravek obsahuje jód a zinek.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr podle počtu složek místo podle jejich množství.</li>'
          '<li>Souběžné užívání multivitamínu a několika samostatných doplňků se stejnými látkami.</li>'
          '<li>Dětské želé uložené tam, kde na něj dítě dosáhne.</li>'
          '<li>Přehlédnutí, že na jednu porci připadají dvě nebo tři kapsle.</li>'
          '<li>Výběr řady pro ženy nebo muže jen podle obalu, bez kontroly železa a jódu.</li></ul>'
          '<h2>Skladování a nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky více českých obchodů a můžete porovnat velikost balení, dopravu i dostupnost; objednávku pak dokončíte v e-shopu. Multivitamíny skladujte v suchu, v uzavřeném obalu a mimo koupelnu, protože vlhko jim škodí, zejména šumivým tabletám a želé. Tekuté formy po otevření uchovávejte tak, jak říká etiketa, často v chladničce. U větších balení si spočítejte, zda je stihnete spotřebovat před datem minimální trvanlivosti.</p>',
    faq=[
        ('Potřebuju multivitamín, když jím pestře?', 'Při pestré a dostatečné stravě ho většina zdravých dospělých nepotřebuje. Může posloužit jako pojistka při jednotvárném jídelníčku nebo redukční dietě. Kdo si není jistý, ať se poradí s lékařem nebo lékárníkem.'),
        ('Co znamená procento RHP na obalu?', 'Je to procento referenční hodnoty příjmu, orientačního údaje pro průměrného dospělého. Vyšší procento neznamená lepší přípravek, jen vyšší množství dané látky.'),
        ('Liší se multivitamín pro ženy a pro muže?', 'Často ano: řady pro ženy mívají víc železa a kyseliny listové, řady pro muže železo obsahují méně nebo vůbec. U některých výrobků je ale rozdíl hlavně v obalu, proto porovnejte tabulku složení.'),
        ('Jsou chelátové multivitamíny lepší?', 'Výrobci je uvádějí jako šetrnější k žaludku. Rozdíl ve vstřebávání oproti levnějším formám se u zdravého člověka často přeceňuje; důležitější je množství látky na porci.'),
        ('Mohu dávat dětem multivitamín pro dospělé?', 'Ne. Dětské přípravky mají obsah přizpůsobený věku. Dodržte věk a množství, které uvádí výrobce, a želé ukládejte mimo dosah dětí.'),
        ('Mohu kombinovat multivitamín s dalšími doplňky?', 'Ano, ale sečtěte si, kolik které látky přijímáte ze všech přípravků. Vitamíny A, D, E a K se v těle ukládají. Při užívání léků se poraďte s lékařem nebo lékárníkem.'),
        ('Je gumový multivitamín stejně dobrý jako tableta?', 'Želé chutná a hodí se pro ty, kdo nepolykají tablety, ale obvykle obsahuje cukr nebo sladidla a méně minerálů. Porovnejte tabulku složení s tabletou.'),
        ('Proč se multivitamíny kupují hlavně v zimě a v lednu?', 'Na začátku roku mnoho lidí drží redukční dietu a v zimě jí méně čerstvé sezonní zeleniny. Multivitamín pak slouží jako pojistka, ale pestrý jídelníček nenahradí.'),
    ])

# ------------------------------------------------------------------ l-karnitin
NEW['l-karnitin'] = dict(long=True,
    title='L-karnitin: tekutý, kapsle, tartrát, Carnipure a shoty',
    desc='L-karnitin tekutý, v kapslích, tabletách i shotech. Formy, přepočet na porci a co o něm víme bez přikrášlení, a porovnat nabídky českých obchodů.',
    intro='<p>L-karnitin je látka, kterou si lidské tělo vyrábí samo z aminokyselin lysinu a methioninu, převážně v játrech a ledvinách. Z jídla ho nejvíc dodává červené maso, méně mléčné výrobky. Ve fitness světě patří k nejznámějším doplňkům a často se prodává jako spalovač tuků. Tady je ale potřeba říct na rovinu: pro L-karnitin Evropská unie neschválila žádné zdravotní tvrzení, tedy ani o hubnutí, ani o výkonu nebo regeneraci.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů, nakoupíte pak přímo v e-shopu, který si vyberete. V kategorii jsou tekuté koncentráty, ampule a shoty, kapsle, tablety, hotové nápoje i kombinace se zeleným čajem, kofeinem nebo chromem. Vyrábějí je například ' + B(('gymbeam', 'GymBeam')) + ', Nutrend, QNT, Trec Nutrition, Extrifit, Mammut Nutrition, Best Body Nutrition, Reflex Nutrition, ActivLab, OstroVit nebo MaxxWin. Nadřazenou kategorií jsou <a href="/spalovace-tuku/">spalovače tuků</a>, příbuzné jsou <a href="/aminokyseliny-bcaa/">aminokyseliny a BCAA</a> a <a href="/proteiny/">proteiny</a>.</p>',
    guide='<h2>Co L-karnitin v těle dělá</h2>'
          '<p>Většina karnitinu je v těle uložena ve svalech, kosterních i srdečním. V buňkách slouží jako přenašeč, který dopravuje mastné kyseliny s dlouhým řetězcem do mitochondrií, kde se z nich uvolňuje energie. Právě z této role vznikla představa, že víc karnitinu znamená rychlejší spalování tuku. Zdravé tělo si ho ale vytvoří dost a jeho množství ve svalech se doplňkem zvyšuje jen obtížně. Výsledky studií jsou nejednotné, a pokud nějaký rozdíl ukazují, bývá malý. Spolehlivý doklad, že by doplněk u zdravého člověka hubnutí zrychlil, chybí.</p>'
          '<h2>Žádné schválené tvrzení: co to znamená</h2>'
          '<p>Evropský úřad pro bezpečnost potravin posuzoval řadu žádostí o tvrzení pro L-karnitin, mimo jiné o přispění k normálnímu metabolismu tuků, rychlejší regeneraci svalů po zátěži nebo zvýšení vytrvalosti. U žádného z nich úřad nepovažoval souvislost mezi příjmem L-karnitinu a slibovaným účinkem za prokázanou, a Evropská komise proto žádné z nich neschválila. Výrobce proto nesmí na obalu tvrdit, že L-karnitin spaluje tuk nebo pomáhá hubnout. Pokud takovou větu u výrobku vidíte, jde o marketing, ne o ověřený fakt.</p>'
          '<p>Kombinované přípravky mohou schválené tvrzení nést, týká se ale jiné složky. Typickým příkladem je chrom, který přispívá k udržení normální hladiny glukózy v krvi. Toto tvrzení ale patří chromu, ne L-karnitinu, a výrobce ho smí použít jen tehdy, když porce obsahuje chromu dostatečné množství.</p>'
          '<h2>Formy L-karnitinu</h2>'
          + T(['Forma', 'Co to je', 'Poznámka'], [
              ['L-karnitin (báze), tekutý', 'čistý L-karnitin rozpuštěný ve vodě', 'lahve a shoty, se sladidly a konzervanty'],
              ['L-karnitin tartrát (LCLT)', 'sůl L-karnitinu s kyselinou vinnou', 'kapsle a tablety; L-karnitin tvoří asi dvě třetiny hmotnosti'],
              ['Acetyl-L-karnitin (ALCAR)', 'karnitin s navázanou acetylovou skupinou', 'samostatná forma, obvykle v kapslích'],
              ['Carnipure', 'ochranná známka suroviny L-karnitinu', 'označuje původ suroviny, nejde o jinou látku'],
              ['Shoty a ampule', 'menší balení tekutého koncentrátu', 'praktické do tašky, víc obalového materiálu'],
              ['Hotový nápoj', 'L-karnitin ve vodě s příchutí, někdy sycený', 'některé varianty obsahují kofein'],
              ['Kombinace', 'se zeleným čajem, kofeinem, CLA, chromem nebo taurinem', 'zkontrolujte množství každé složky']]) +
          '<h2>Čísla na lahvích: 3000, 70 000, 220 000</h2>'
          '<p>Tekuté karnitiny mívají v názvu velká čísla. Jednou jde o množství L-karnitinu v miligramech v jedné porci, jindy o celkové množství v celé lahvi, a z názvu se to vždy nepozná. Rozhoduje tabulka na obalu: kolik mililitrů tvoří porci, kolik L-karnitinu v ní je a kolik porcí lahev vydá. Jen tak porovnáte lahve s různým objemem i různou koncentrací. U kapslí a tablet sledujte, zda výrobce uvádí hmotnost tartrátu, nebo čistého L-karnitinu, protože čistého karnitinu je v tartrátu méně, než říká hmotnost soli.</p>'
          '<h2>Tekutý, nebo kapsle?</h2>'
          '<p>Tekutá forma se rychle odměří a vypije, obsahuje ale sladidla, aroma a konzervanty a po otevření se často uchovává v chladničce; řiďte se pokynem na etiketě. Kapsle a tablety jsou bez chuti, dobře se skladují a hodí se na cesty, jen jich na porci bývá víc. Shoty a ampule, třeba Nutrend Carnitine 3000 Shot nebo shoty od QNT a ActivLabu, se snadno nosí v tašce na trénink. Hotové nápoje typu Nutrend Carnitine Activity Drink obsahují L-karnitin rozpuštěný ve vodě s příchutí a některé varianty i kofein.</p>'
          '<h2>Kombinace s kofeinem a rostlinnými extrakty</h2>'
          '<p>Hodně výrobků v kategorii není čistý L-karnitin. MaxxWin L-Carnitine Guarana Taurine, OstroVit CLA + Green Tea + L-Carnitine nebo OstroVit Slim Care s glukomannanem spojují karnitin s dalšími látkami. U kofeinu, guarany a extraktu ze zeleného čaje sledujte celkové množství kofeinu na porci a připočtěte k němu kávu nebo energetické nápoje, které pijete. Přípravky s kofeinem nejsou vhodné pro děti, těhotné a kojící ženy. Kombinace jsou pohodlné, jen nad jednotlivými složkami máte menší kontrolu.</p>'
          '<h2>Kdy dát pozor</h2>'
          '<p>U zdravých dospělých bývá L-karnitin obvykle dobře snášen. Vyšší množství ale může způsobit zažívací potíže, nevolnost a u některých lidí nepříjemný rybí pach potu, dechu nebo moči. Část karnitinu přeměňují střevní bakterie na látku TMAO, jejíž souvislost se zdravím srdce a cév se zkoumá. Těhotné a kojící ženy, děti, lidé s onemocněním ledvin, srdce nebo štítné žlázy a ti, kdo užívají léky, například na ředění krve, by se měli poradit s lékařem nebo lékárníkem. Kolik užít, stanoví etiketa, a toto množství nepřekračujte.</p>'
          '<h2>Lednová předsevzetí a reálná očekávání</h2>'
          '<p>Na začátku roku se o L-karnitin zajímá víc lidí, protože k novoročním předsevzetím často patří hubnutí. Tuk ale ubývá tehdy, když tělo dlouhodobě vydá víc energie, než přijme, a doplněk na tomto principu nic nemění. Nenahradí jídelníček s dostatkem bílkovin, pravidelný pohyb ani spánek. Kdo se rozhodne L-karnitin vyzkoušet, měl by vědět, že kupuje doplněk bez schváleného tvrzení. Pro hubnutí obvykle víc udělá pravidelný trénink a kvalitní jídlo, například z kategorie <a href="/fit-potraviny/">fit potraviny</a>.</p>'
          '<h2>Vegani a vegetariáni</h2>'
          '<p>Protože hlavním zdrojem karnitinu v jídle je maso, přijímají vegetariáni a vegani z potravy méně karnitinu. Tělo si ho ale vyrábí samo, a proto se L-karnitin neřadí mezi esenciální živiny. U doplňku je pro vegany důležité, zda kapsle není želatinová a zda je výrobek bez živočišných složek. V nabídce jsou i veganské tablety a rostlinné kapsle, například Vitobest L-karnitin 500 nebo Fit Sport Nutrition Karnitin Taurin ve vege kapslích.</p>'
          '<h2>Jak číst složení</h2>'
          '<ul><li><strong>Množství L-karnitinu na porci:</strong> v miligramech, u tartrátu ideálně přepočtené na čistý L-karnitin.</li>'
          '<li><strong>Velikost porce:</strong> mililitry u tekutých forem, počet kapslí nebo tablet u pevných.</li>'
          '<li><strong>Forma:</strong> báze, tartrát, acetyl-L-karnitin; u surovin s ochrannou známkou její název.</li>'
          '<li><strong>Další složky:</strong> kofein, guarana, zelený čaj, chrom, CLA, taurin, vitamíny skupiny B.</li>'
          '<li><strong>Sladidla a konzervanty:</strong> hlavně u tekutých forem a nápojů.</li>'
          '<li><strong>Datum minimální trvanlivosti:</strong> v nabídce se objevují i výprodeje se zkrácenou trvanlivostí nebo zboží po datu minimální trvanlivosti, což bývá uvedeno přímo v názvu.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Očekávání, že L-karnitin sám o sobě zhubne tuk.</li>'
          '<li>Srovnávání lahví podle čísla v názvu bez přepočtu na porci.</li>'
          '<li>Přehlédnutý kofein v kombinovaném přípravku.</li>'
          '<li>Zaměňování hmotnosti tartrátu s obsahem čistého karnitinu.</li>'
          '<li>Nákup velké lahve, kterou po otevření nestihnete včas spotřebovat.</li></ul>'
          '<h2>L-karnitin v jídle</h2>'
          '<p>Nejvíc karnitinu obsahuje hovězí a jehněčí maso, méně vepřové, drůbež a ryby, ještě méně mléko a mléčné výrobky. Rostlinné potraviny ho mají jen nepatrně. Kdo jí maso několikrát týdně, přijímá z jídla řádově víc karnitinu než vegan, a k tomu si tělo dalšího vytvoří samo. I proto u zdravého člověka s běžnou stravou nedostatek karnitinu nehrozí.</p>'
          '<h2>Kvalita a soutěžní sport</h2>'
          '<p>V doplňcích se používá L-forma karnitinu, tedy ta, kterou tělo samo vytváří; na obalu ji poznáte podle předpony L-. L-karnitin nepatří mezi látky zakázané Světovou antidopingovou agenturou. U doplňků stravy ale obecně hrozí, že nekvalitní výrobek obsahuje nečistoty nebo nepřiznané látky. Soutěžící sportovci by proto měli sáhnout po výrobcích s uvedenou šarží a nezávislým testováním, rekreačním sportovcům postačí známá značka s jasným složením.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Nabídky několika českých obchodů najdete na kartě produktu vedle sebe, i s dopravou a dostupností; objednávka pak proběhne přímo v e-shopu. U L-karnitinu porovnávejte nejprve obsah na porci a počet porcí v balení, teprve potom příchuť a formu. Pokud vás zajímají spíš doplňky s doloženým účinkem, projděte si kategorii <a href="/spalovace-tuku/">spalovače tuků</a> s vědomím, že ani tam nejde o zázraky, a zaměřte se na příjem bílkovin a kategorii <a href="/proteiny/">proteiny</a>.</p>',
    faq=[
        ('Spaluje L-karnitin tuk?', 'Pro L-karnitin není v EU schválené žádné zdravotní tvrzení, ani o hubnutí. Spolehlivý doklad, že by doplněk u zdravého člověka hubnutí zrychlil, chybí. Tuk ubývá, když tělo dlouhodobě vydá víc energie, než přijme.'),
        ('Co je L-karnitin tartrát?', 'Je to sůl L-karnitinu s kyselinou vinnou, která se používá v kapslích a tabletách. Čistý L-karnitin tvoří zhruba dvě třetiny její hmotnosti, proto sledujte, co přesně etiketa uvádí.'),
        ('Co znamená Carnipure?', 'Carnipure je ochranná známka suroviny L-karnitinu. Označuje původ a kvalitu suroviny, nejde o jinou nebo silnější látku.'),
        ('Co znamenají čísla jako 70 000 nebo 3000 v názvu?', 'Někdy jde o množství L-karnitinu v miligramech v jedné porci, jindy o celkové množství v lahvi. Rozhodující je tabulka na obalu: velikost porce, obsah karnitinu v ní a počet porcí.'),
        ('Je lepší tekutý L-karnitin, nebo kapsle?', 'Tekutý se rychle odměří, ale obsahuje sladidla a konzervanty a po otevření se často uchovává v chladu. Kapsle jsou bez chuti a vydrží déle. Porovnávejte obsah na porci.'),
        ('Má L-karnitin nežádoucí účinky?', 'Vyšší množství může způsobit zažívací potíže a u některých lidí rybí pach potu nebo moči. Těhotné, kojící ženy, děti, lidé s onemocněním ledvin, srdce nebo štítné žlázy a ti, kdo užívají léky, by se měli poradit s lékařem nebo lékárníkem.'),
        ('Potřebují vegani L-karnitin doplňovat?', 'Vegani přijímají z potravy méně karnitinu, tělo si ho ale vyrábí samo a neřadí se mezi esenciální živiny. Zda je doplněk na místě, posoudí lékař nebo nutriční terapeut.'),
        ('Proč mají některé karnitiny v názvu kofein nebo guaranu?', 'Jde o kombinované přípravky. Kofein v nich není kvůli karnitinu, ale jako další složka. Sečtěte si celkový příjem kofeinu včetně kávy; pro děti, těhotné a kojící ženy nejsou vhodné.'),
    ])

# ------------------------------------------------------------------ probiotika
NEW['probiotika'] = dict(long=True,
    title='Probiotika: kmeny, CFU, kapsle, kapky a skladování',
    desc='Probiotika v kapslích, sáčcích, kapkách i pro děti. Jak číst kmeny a CFU, jak je skladovat a co jsou prebiotika, a porovnat nabídky českých obchodů.',
    intro='<p>Probiotika jsou doplňky stravy s živými mikroorganismy, nejčastěji s bakteriemi mléčného kvašení a bifidobakteriemi, méně často s kvasinkami. Prodávají se v kapslích, sáčcích, kapkách i cucavých tabletách a liší se tím, jaké kmeny obsahují a v jakém množství. Než začnete vybírat, je dobré vědět jednu věc: slovo „probiotikum“ není v Evropské unii schváleným zdravotním tvrzením a pro probiotické kultury v doplňcích stravy žádné tvrzení schválené není.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů, nákup provedete přímo v obchodě, který si zvolíte. V kategorii najdete přípravky značek ' + B(('gymbeam', 'GymBeam')) + ', Optibac, MOVit Energy, Viridian, GreenFood Nutrition, Webber Naturals, Terezia, Vitar, Blendea nebo Puhdistamo, samostatné kmeny i směsi s prebiotiky a vitamíny. Nadřazenou kategorií jsou <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>, příbuzné jsou <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a> a <a href="/vitamin-d/">vitamín D</a>.</p>',
    guide='<h2>Co říkají pravidla EU</h2>'
          '<p>Evropská komise považuje slovo probiotikum na obalu potraviny za nepřímé zdravotní tvrzení, protože naznačuje přínos pro zdraví. Evropský úřad pro bezpečnost potravin posoudil stovky žádostí o tvrzení pro konkrétní bakteriální kmeny a s výjimkou kultur v jogurtu žádnou nepodpořil, nejčastěji kvůli nedostatečně popsanému kmeni nebo slabým důkazům. Jednotlivé členské státy přistupují k samotnému označení různě, proto se s ním na trhu setkáte. Pro vás z toho plyne, že sliby o lepším trávení nebo silnější imunitě u probiotických kultur nejsou ověřené tvrzení.</p>'
          '<p>Jediné schválené tvrzení spojené s živými kulturami se týká jogurtu. Živé kultury v jogurtu nebo zakysaném mléčném výrobku zlepšují trávení laktózy obsažené ve výrobku u osob, které mají potíže s trávením laktózy. Platí ale jen pro jogurt nebo zakysaný mléčný výrobek s kulturami Lactobacillus delbrueckii subsp. bulgaricus a Streptococcus thermophilus v předepsaném množství, ne pro kapsle. Má-li probiotický doplněk na obalu tvrzení, vztahuje se k přidanému vitamínu nebo minerálu, například k vitamínu D nebo C.</p>'
          '<h2>Jak číst název kmene</h2>'
          '<p>Pořádně označený přípravek uvádí rod, druh a kód kmene, například Lacticaseibacillus rhamnosus GG nebo Bifidobacterium animalis subsp. lactis BB-12. Výsledky studií u jednoho kmene nelze automaticky přenášet na jiný kmen téhož druhu. Když obal uvádí jen „laktobacily“ nebo druh bez kódu kmene, víte o obsahu méně. V roce 2020 navíc vědci rozdělili rod Lactobacillus do 25 rodů. Stejná bakterie proto může na starším obalu figurovat jako Lactobacillus rhamnosus a na novějším jako Lacticaseibacillus rhamnosus; jde o tutéž bakterii s novým jménem.</p>'
          + T(['Skupina', 'Příklady na obalech', 'Poznámka'], [
              ['Laktobacily (dnes několik rodů)', 'L. rhamnosus, L. plantarum, L. acidophilus, L. gasseri, L. reuteri', 'nejčastější složka kapslí i kapek'],
              ['Bifidobakterie', 'B. lactis, B. longum, B. breve, B. bifidum', 'často ve směsi s laktobacily'],
              ['Sporotvorné bakterie', 'Bacillus coagulans, například surovina LactoSpore', 'spory snášejí teplo a kyselé prostředí lépe'],
              ['Kvasinky', 'Saccharomyces boulardii', 'nejde o bakterii, antibiotika na ni nepůsobí'],
              ['Streptokoky', 'Streptococcus thermophilus, S. salivarius', 'S. salivarius bývá v cucavých tabletách'],
              ['Synbiotika', 'kultury spolu s prebiotiky, třeba inulinem', 'označení směsi, ne zvláštní druh bakterie']]) +
          '<h2>CFU: co číslo na obalu znamená</h2>'
          '<p>CFU, z anglického colony forming units, udává počet živých mikroorganismů schopných se množit. Na obalech se uvádí v miliardách, třeba 5, 10 nebo 80 miliard na porci. Podstatné je, k jakému okamžiku číslo platí: zda v den výroby, nebo do konce minimální trvanlivosti. Počet živých buněk během skladování klesá, takže údaj platný do konce trvanlivosti má pro kupujícího větší hodnotu. Vyšší číslo samo o sobě neznamená lepší přípravek, protože u různých kmenů se zkoumala různá množství. U směsí sledujte, zda výrobce uvádí množství jednotlivých kmenů, nebo jen jejich součet.</p>'
          '<h2>Formy v nabídce</h2>'
          '<p>Nejčastější jsou kapsle, u nichž výrobci někdy uvádějí obal odolný vůči žaludeční kyselině. Sáčky s práškem, například od Optibacu nebo Maxivita Kids, se rozmíchají ve vodě nebo v jídle, které není horké. Pro kojence a malé děti se prodávají olejové kapky, třeba Terezia baby kapky nebo Blendea Kids s vitamínem D3. Cucavé tablety, jako Zdravý zoubek od MOVit Energy, jsou určené pro děti. Větší balení prášku, například Vegan Gut Blend, míří na ty, kdo si je přidávají do nápojů. Najdete i kombinace s hlívou ústřičnou, vlákninou, trávicími enzymy nebo vitamíny.</p>'
          '<p>V nabídce se objevují také přípravky pro psy a kočky, například Vitar Veterinae nebo MOVit PET. Jsou určené zvířatům, takže si při nákupu všimněte, komu je výrobek určen.</p>'
          '<h2>Skladování: lednice, nebo skříňka</h2>'
          '<p>Živé kultury jsou citlivé na teplo, vlhkost a kyslík. Některé výrobky vyžadují uchování v chladničce, jiné jsou díky lyofilizaci a balení v blistrech nebo lahvičce s vysoušedlem stabilní i při pokojové teplotě. Vždy platí pokyn na obalu. V zimě hlídejte umístění: polička nad radiátorem nebo kuchyňská linka vedle trouby je pro probiotika to nejhorší místo. Lahvičku po každém otevření pořádně zavřete a nenechávejte ji v koupelně. Pokud výrobek vyžaduje chlazení, zjistěte si před objednávkou, jak ho obchod přepravuje.</p>'
          '<h2>Prebiotika a synbiotika</h2>'
          '<p>Prebiotika jsou látky, které člověk sám nestráví a které slouží jako potrava některým střevním bakteriím. Typicky jde o inulin, fruktooligosacharidy (FOS) a galaktooligosacharidy (GOS). Synbiotikum spojuje probiotické kultury s prebiotikem; příkladem jsou GymBeam Synbio Complex nebo Viridian Synerbio. Inulin a další vláknina mohou zpočátku způsobit nadýmání. V jídle se tyto vlákniny přirozeně vyskytují v cibuli, česneku, pórku, čekance, chřestu nebo banánech.</p>'
          '<h2>Probiotika a antibiotika</h2>'
          '<p>Mnoho lidí kupuje probiotika během léčby antibiotiky nebo po ní. Antibiotika ničí i bakterie z doplňku, proto se bakteriální probiotika obvykle užívají s časovým odstupem od léku. Kvasinku Saccharomyces boulardii antibiotika proti bakteriím nezasáhnou, léky proti kvasinkovým infekcím ale ano. O vhodnosti, načasování a výběru přípravku se ale poraďte s lékařem nebo lékárníkem, který zná i konkrétní lék, jenž užíváte.</p>'
          '<h2>Probiotika s vitamíny, hlívou a vlákninou</h2>'
          '<p>Část výrobků v kategorii jsou kombinace: Vitar Probiotika s vlákninou a vitamíny C a D, VemoHerb Probiotic 8+ Immuno nebo Terezia Hlíva + lactobacily. Pokud takový přípravek nese zdravotní tvrzení, pochází od vitamínu. Vitamín D i vitamín C přispívají k normální funkci imunitního systému, jsou-li v přípravku v dostatečném množství. Pro hlívu ústřičnou ani pro probiotické kultury schválené tvrzení neexistuje. U kombinací si sečtěte vitamíny ze všech doplňků, které užíváte, ať je nepřijímáte dvakrát.</p>'
          '<h2>Kdy probiotika užívat</h2>'
          '<p>Výrobci se liší v tom, zda doporučují užívat přípravek s jídlem, nebo nalačno, a to podle kmene a technologie kapsle. Proto se řiďte pokynem na konkrétním obalu. Kapsli nebo sáček nezapíjejte horkým čajem a prášek nemíchejte do horkého jídla, protože teplo živé kultury ničí. Pro většinu přípravků je důležitější pravidelnost než přesná hodina.</p>'
          '<h2>Fermentované potraviny</h2>'
          '<p>Živé kultury obsahují také jogurty, kefír, acidofilní mléko, kysané zelí, kimči nebo kombucha. Pasterizované výrobky, například sterilované zelí ve sklenici, živé kultury většinou nemají, protože je zahřátí zničí. Fermentované potraviny nejsou totéž co přípravek s definovaným kmenem a počtem CFU, jako součást pestré stravy jsou ale dobrou volbou.</p>'
          '<h2>Pro koho opatrně</h2>'
          '<p>Zdraví dospělí probiotika obvykle snášejí dobře, na začátku se může objevit nadýmání. Lidé s oslabenou imunitou, vážně nemocní, pacienti se zavedeným centrálním žilním katétrem, těhotné a kojící ženy a ti, kdo užívají léky, by se měli předem poradit s lékařem. U novorozenců, zvlášť předčasně narozených, rozhoduje vždy pediatr. Dětem dávejte jen přípravky určené pro jejich věk, v množství, které uvádí výrobce. Dlouhodobé nebo závažné zažívací potíže patří k lékaři, ne do nákupního košíku.</p>'
          '<h2>Alergeny a veganské varianty</h2>'
          '<p>Některé kmeny se pěstují na živných půdách s mlékem a kapsle mohou obsahovat stopy mléka nebo laktózu jako plnivo. Kdo nesnáší mléčnou bílkovinu nebo jí vegansky, ať hledá označení „vegan“ a seznam alergenů. Obal kapsle bývá želatinový i rostlinný z celulózy. U kapek zkontrolujte, v jakém oleji jsou kultury rozptýlené.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr jen podle nejvyššího čísla CFU.</li>'
          '<li>Přehlédnutí, zda CFU platí v den výroby, nebo do konce trvanlivosti.</li>'
          '<li>Skladování v teple, na slunci nebo v koupelně.</li>'
          '<li>Nákup přípravku bez uvedeného kmene, když vás zajímá konkrétní kmen.</li>'
          '<li>Očekávání, že doplněk vyřeší dlouhodobé zažívací potíže bez návštěvy lékaře.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky více českých obchodů vedle sebe, včetně dopravy a dostupnosti, a objednávku pak dokončíte přímo v e-shopu. U probiotik porovnávejte nejprve kmeny a množství CFU na porci, pak počet porcí v balení a způsob skladování. Zkontrolujte i datum minimální trvanlivosti, protože u živých kultur je zvlášť důležité. Pokud vás zajímají vitamíny, které se do probiotických směsí často přidávají, podívejte se do kategorií <a href="/vitamin-d/">vitamín D</a> a <a href="/vitamin-c/">vitamín C</a>.</p>',
    faq=[
        ('Má probiotikum schválené zdravotní tvrzení?', 'Ne. Slovo probiotikum není v EU schváleným zdravotním tvrzením a pro probiotické kultury v doplňcích žádné tvrzení schválené není. Pokud má výrobek tvrzení, týká se přidaného vitamínu nebo minerálu.'),
        ('Co znamená CFU?', 'Počet živých mikroorganismů schopných se množit, uváděný obvykle v miliardách na porci. Důležité je, zda číslo platí v den výroby, nebo do konce minimální trvanlivosti.'),
        ('Je lepší probiotikum s vyšším počtem CFU?', 'Ne automaticky. U různých kmenů se zkoumala různá množství. Porovnávejte kmeny, množství na porci a to, k jakému datu výrobce počet garantuje.'),
        ('Musí se probiotika skladovat v lednici?', 'Záleží na výrobku. Některá chlazení vyžadují, jiná jsou stabilní při pokojové teplotě. Vždy platí pokyn na obalu; nikdy je nenechávejte u radiátoru nebo v koupelně.'),
        ('Proč mají laktobacily na obalech nová jména?', 'V roce 2020 byl rod Lactobacillus rozdělen do 25 rodů. Lactobacillus rhamnosus se tak dnes jmenuje Lacticaseibacillus rhamnosus, jde ale o tutéž bakterii.'),
        ('Mohu užívat probiotika s antibiotiky?', 'Bakteriální probiotika se obvykle užívají s časovým odstupem, protože je antibiotika ničí; kvasinku Saccharomyces boulardii nezasáhnou. Načasování a výběr proberte s lékařem nebo lékárníkem.'),
        ('Jaký je rozdíl mezi probiotiky a prebiotiky?', 'Probiotika obsahují živé mikroorganismy, prebiotika jsou nestravitelné látky jako inulin nebo FOS, které slouží jako potrava některým střevním bakteriím. Jejich kombinace se nazývá synbiotikum.'),
        ('Mohu dát probiotika dětem?', 'Jen přípravky určené pro daný věk a v množství, které uvádí výrobce. U kojenců a předčasně narozených dětí rozhoduje vždy pediatr.'),
    ])
