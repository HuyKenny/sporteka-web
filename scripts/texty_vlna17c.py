"""sporteka.cz — wave 17c (4. 11. 2026): long texts (>= 1650 words) for lyzarske-doplnky, bezecke-lyzovani, florbal, merino-doplnky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-doplnky
NEW['lyzarske-doplnky'] = dict(long=True,
    title='Lyžařské hůlky a doplňky: vosky, vaky, příslušenství',
    desc='Lyžařské hůlky, vosky, mazání, vaky a tašky na lyže a boty. Jak vybrat délku hůlek, vosk podle teploty a obal. Nabídky českých obchodů vedle sebe.',
    intro='<p>Lyže a boty tvoří základ výbavy, jenže o tom, jak se vám bude jezdit a jak dlouho vám vydrží, často rozhodují drobnosti kolem nich. '
          'V kategorii <strong>lyžařské hůlky a doplňky</strong> jsou sjezdové a běžecké hůlky, vosky a produkty na mazání skluznice, tašky a vaky na lyže a boty a další příslušenství, které se při sezóně ukáže jako užitečné. '
          'Najdete tu zboží pro rodinné lyžování i pro závodníky, kteří si servisují lyže před každým startem.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného zboží, takže vidíte, kde je daná délka hůlek nebo balení vosku skladem. '
          'Podrobněji se věnujeme podkategoriím <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-vosky/">vosky a mazání</a> a <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a>. '
          'Na této stránce najdete rady, jak vybírat podle disciplíny, výšky a zvyklostí, a upozornění na chyby, které se opakují každou zimu.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Doplňky se liší podle toho, jestli jezdíte po sjezdovce, po lyžařské stopě, nebo mimo ni. Přehled pomůže určit, co je nezbytné a co jen příjemné.</p>'
          + T(['Doplněk', 'K čemu slouží', 'Pro koho', 'Na co si dát pozor'], [
              ['Sjezdové hůlky', 'rovnováha, rytmus oblouků, pomoc při chůzi a na vleku', 'sjezdaři všech úrovní', 'délka a obsah madla a poutka'],
              ['Běžecké hůlky', 'odraz při klasice i bruslení', 'běžkaři, závodníci', 'delší než sjezdové, tvar košíku a materiál'],
              ['Skialpové hůlky', 'teleskopické, měnitelná délka při stoupání a sjezdu', 'skialpinisté', 'pevný zámek, větší košík do sněhu'],
              ['Vosky a mazání', 'ochrana a zlepšení skluzu skluznice', 'všichni majitelé lyží nebo snowboardu', 'teplota, typ sněhu a styl lyžování'],
              ['Tašky a vaky na lyže', 'přeprava a skladování', 'cestovatelé, skialpinisté, rodiny', 'délka, polstrování a počet párů'],
              ['Tašky na boty', 'přeprava bot a oblečení', 'každý, kdo jezdí autem, lanovkou nebo vlakem', 'větrání, vyztužené dno']]) +
          '<p>Hůlky najdete v samostatné kategorii <a href="/lyzarske-hole/">lyžařské hole</a>, běžecké modely i v podkategorii <a href="/bezecke-lyzovani/">běžeckého lyžování</a>. Skialpinismus má vlastní vybavení v kategorii <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h2>Délka sjezdových hůlek</h2>'
          '<p>Nejčastější způsob měření je jednoduchý. Hůlku obraťte, uchopte pod košíkem a postavte se s ní tak, aby se košík dotýkal země. Paže má v lokti svírat přibližně pravý úhel, předloktí je rovnoběžně s podlahou. '
          'Pokud lokty zůstanou výrazně výše nebo níže, je hůlka příliš krátká či dlouhá. Většina výrobců uvádí délku po pěti centimetrech, takže hledáte nejbližší hodnotu. '
          'Při nejistotě se u rekreačních jezdců zvolí o něco kratší hůlka, protože se s ní lépe manévruje v zatáčkách a na strmějším terénu.</p>'
          '<p>Pro děti platí stejné pravidlo, jen se hůlka musí přizpůsobit rychlému růstu. Nejmenší děti hůlky zpočátku nepotřebují, rovnováhu a vedení oblouků se učí bez nich. Jakmile s nimi začnou, vybírejte pevné hůlky s malým košíkem a měkkým madlem.</p>'
          '<h2>Materiály a konstrukce hůlek</h2>'
          '<ul><li><strong>Hliníkové hůlky</strong> jsou odolné a snášejí pády, často je volí rekreační jezdci a děti.</li>'
          '<li><strong>Uhlíkové a kompozitní hůlky</strong> jsou lehčí a tlumí vibrace, hodí se k závodům a delším túrám. Při nárazu se ale mohou zlomit, protože pružnost snášejí hůř než hliník.</li>'
          '<li><strong>Madlo a poutko</strong> jsou důležité pro pohodlí. Poutko se dává zespodu, dlaň se opírá o něj a držení nevyžaduje křečovité sevření.</li>'
          '<li><strong>Košík</strong> bývá menší na sjezdovku a větší na hlubší sníh nebo skialpy.</li>'
          '<li><strong>Teleskopické hůlky</strong> se prodlužují a zkracují, což oceníte při stoupání, při vedení dítěte nebo když hůlku dáváte do batohu.</li></ul>'
          '<h2>Vosky a mazání skluznice</h2>'
          '<p>Skluznice lyží a snowboardů je z porézního plastu, který se bez údržby suší a ztrácí skluz. Vosk se do ní vsakuje, zlepšuje kluznost a chrání ji proti oxidaci a oděru. Kdo jezdí jen několik dní v roce, vystačí si se servisem před sezónou a krátkým přemazáním cestou. '
          'Pravidelní jezdci mažou lépe po několika dnech provozu. Více o postupech najdete v kategorii <a href="/lyzarske-vosky/">vosky a mazání na lyže a snowboardy</a>.</p>'
          + T(['Typ produktu', 'Použití', 'Poznámka'], [
              ['Horký (žehlicí) vosk', 'základní servis a ochrana skluznice, nanáší se žehličkou', 'vydrží déle než studená varianta, vyžaduje opatrnost s teplotou'],
              ['Sprej a tekutý vosk', 'rychlé přemazání na svahu nebo doma', 'pohodlné, trvanlivost je kratší'],
              ['Stírací a pastové vosky', 'rychlá obnova skluzu bez žehličky', 'vhodné jako doplněk, ne jako náhrada servisu'],
              ['Odmašťovače a čističe', 'odstranění starého vosku a nečistot před mazáním', 'bez čisté skluznice se nový vosk špatně vsákne'],
              ['Stoupací a stopové vosky', 'běžecké lyže, klasická technika', 'řídí se teplotou a vlhkostí sněhu'],
              ['Kartáče a škrabky', 'práce s voskem po vychladnutí', 'kartáče z různých vláken pro různé fáze']]) +
          '<p>Základní postup je u všech stejný: skluznici očistit, vosk rozehřát a rovnoměrně nanést, nechat vychladnout, vosk seškrábnout a zbytky vykartáčovat. Chybou je přehřátý vosk nebo žehlička, která se na jednom místě zastaví, protože skluznici může poškodit. '
          'Fluorované vosky jsou v mnoha zemích kvůli ochraně životního prostředí omezené, proto při výběru čtěte popis produktu a respektujte aktuální pravidla závodů.</p>'
          '<h2>Jak vybrat vosk podle sněhu</h2>'
          '<p>Teplota vzduchu a sněhu ovlivňuje, jak tvrdý vosk potřebujete. Čím je chladněji, tím tvrdší bývá. Mokrý a jarní sníh potřebuje měkčí složení s vyšší odolností proti vodě. Výrobci označují rozsah teplot přímo na balení, který je pro orientaci nejspolehlivější. '
          'Univerzální vosk je dobrý start pro rekreační jezdce, kteří střídají sjezdovky a sněhové podmínky. Závodníci kombinují více vrstev a používají různé pracovní postupy, ale to je specializace, kterou si ověřte u trenéra.</p>'
          '<h2>Tašky a vaky na lyže a boty</h2>'
          '<p>Dobrý obal chrání lyže při přepravě před poškrábáním hran a skluznice a usnadňuje nošení. Podle délky lyží zvolte vak o 5 až 10 centimetrů delší. Dvojitý vak pojme dva páry, což se hodí rodinám nebo závodníkům. '
          'Cestovní modely mají kolečka a polstrování pro přepravu v letadle, skialpové modely jsou užší a lehčí. Přehled najdete v kategorii <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a>.</p>'
          '<p>Taška na boty by měla mít vyztužené dno, aby se do ní dalo boty postavit, a větrací otvory, aby vlhké boty po jízdě vyschly. Praktická je přihrádka na helmu a brýle. '
          'Nezapomeňte, že boty se mají po jízdě vyndat z tašky a sušit odděleně od ostatního vybavení, jinak se v obalu drží vlhko a zápach.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('swix', 'Swix'), ('star-ski-wax', 'Star Ski Wax'), ('holmenkol', 'Holmenkol'), ('toko', 'Toko'), ('vauhti', 'Vauhti'), ('rossignol', 'Rossignol'), ('dynafit', 'Dynafit'), ('head', 'Head')) + '. '
          'Swix, Holmenkol a Toko patří mezi známé výrobce vosků a nářadí na servis. Rossignol a Head nabízejí hůlky a tašky v návaznosti na své lyže, Dynafit je spojen se skialpinismem a Vauhti se zaměřuje na produkty pro běžecké lyžování. '
          'Porovnáním více obchodů zjistíte, který doplněk je skladem právě ve vaší velikosti.</p>'
          '<h2>Další vybavení na svah</h2>'
          '<p>Kdo skládá celou výbavu, ocení odkazy na související kategorie. Základem jsou <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyzarske-boty/">lyžařské boty</a> a <a href="/lyzarske-vazani/">lyžařské vázání</a>. '
          'Hlavu chrání <a href="/lyzarske-helmy/">lyžařské helmy</a>, oči <a href="/lyzarske-bryle/">lyžařské brýle</a>. Teplo zajistí <a href="/lyzarske-rukavice/">rukavice a palčáky</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a> '
          'a <a href="/lyzarske-termopradlo/">termoprádlo</a>. Svrchní vrstvu tvoří <a href="/lyzarske-bundy/">bundy</a> a <a href="/lyzarske-kalhoty/">kalhoty</a>.</p>'
          '<h2>Nejčastější chyby při nákupu doplňků</h2>'
          '<ul><li>Hůlky vybrané podle výšky těla místo podle měření s pokrčenou paží.</li>'
          '<li>Kupování univerzálního vosku do extrémních podmínek, například na velmi studený nebo mokrý sníh.</li>'
          '<li>Použití vosku bez čištění skluznice, při kterém se zbytky špíny zapečou do povrchu.</li>'
          '<li>Příliš krátký vak, ve kterém se lyže nevejdou s vázáním a hůlkami.</li>'
          '<li>Skladování mokrých lyží v obalu, což vede ke korozi hran.</li>'
          '<li>Zanedbání poutka a výměny košíku, který se časem láme.</li></ul>'
          '<h2>Péče o hůlky a výbavu po sezóně</h2>'
          '<p>Po poslední jízdě hůlky osušte a zkontrolujte, zda nejsou ohnuté nebo naštípnuté, protože prasklinu je lepší objevit doma než na sjezdovce. Madla otřete od potu a soli. '
          'Lyže očistěte, zkontrolujte hrany a před uskladněním je silně navoskujte, aby skluznice přes léto nevyschla. Vosk se před další sezónou seškrábne a skluznice se znovu namaže. '
          'Lyže skladujte na suchém místě bez prudkých teplotních změn, v obalu jen pokud jsou zcela suché.</p>'
          '<h2>Doplňky pro cestu a přepravu</h2>'
          '<p>Při cestě na hory autem se lyže vozí na střeše nebo v kufru a obal je pak jediná ochrana proti špíně a solné břečce. Při cestě vlakem nebo skibusem se ocení vak s ramenním popruhem, aby zůstaly volné ruce na hůlky a tašku s botami. '
          'Na letiště patří polstrovaný vak s pevnými zipy, protože přepravní společnosti s lyžemi nezacházejí šetrně. Přibalte i krátký popruh nebo suchý zip na stažení lyží k sobě, ať při nošení nepřekážejí hrany.</p>'
          '<h2>Kdy kupovat</h2>'
          '<p>Hůlky a obaly se prodávají celoročně, ale největší výběr délek je před zimou. Vosky se vyplatí kupovat s předstihem a ve vhodném balení: kdo jezdí jen občas, nepotřebuje velký kus, protože vosk stárne a ztrácí vlastnosti. '
          'U dětí vybírejte hůlky až v době, kdy je potřebují, a zkontrolujte, zda je lze zkrátit.</p>',
    faq=[('Jak změřit délku lyžařských hůlek?', 'Obraťte hůlku, uchopte ji pod košíkem a postavte se tak, aby se košík dotýkal země. Loket má svírat přibližně pravý úhel. Pokud váháte mezi dvěma délkami, rekreační jezdci častěji volí kratší.'),
         ('Jaký je rozdíl mezi sjezdovými a běžeckými hůlkami?', 'Běžecké hůlky jsou výrazně delší, lehčí a mají jiný tvar košíku a poutka, protože slouží k odrazu. Sjezdové jsou kratší a odolnější. Zaměnit je se nedoporučuje.'),
         ('Jak často mazat lyže?', 'Rekreačním jezdcům stačí servis před sezónou a doplnění vosku podle potřeby. Pravidelní jezdci lyže mažou častěji, orientačně po několika dnech provozu. Skluznice, která zbělá a vypadá suše, potřebuje vosk co nejdřív.'),
         ('Můžu mazat lyže doma žehličkou?', 'Ano, ale používejte žehličku určenou pro mazání, která drží stálou teplotu. Vosk se nesmí kouřit a žehlička se nesmí zastavit na jednom místě, protože by popálila skluznici. Dodržujte pokyny uvedené na balení vosku.'),
         ('Co je to fluorovaný vosk a potřebuji ho?', 'Je to vosk s přísadami zlepšujícími odpuzování vody. Používají ho hlavně závodníci. Pro rekreační jezdce není nutný a v některých zemích je jeho prodej či použití omezené z ekologických důvodů.'),
         ('Jaký vosk zvolit na sjezdové lyže?', 'Začněte univerzálním horkým voskem pro daný rozsah teplot. Chladný a suchý sníh vyžaduje tvrdší vosk, mokrý a jarní měkčí. Přesný rozsah uvádí výrobce na obalu.'),
         ('Jak dlouhý vak na lyže potřebuji?', 'O pět až deset centimetrů delší než lyže. Pokud do něj chcete přidat hůlky, vyberte vak s dostatečnou rezervou. Dvojité vaky pojmou dva páry.'),
         ('Hodí se taška na boty i pro snowboardové boty?', 'Ano, pokud je dost prostorná. Snowboardové boty bývají objemnější, proto zvolte tašku s širším vstupem a vyztuženým dnem.'),
         ('Jak sušit lyžařské boty po jízdě?', 'Vyjměte vložky, rozepněte přezky a nechte boty vyschnout při pokojové teplotě. Nesušte je přímo u topení ani na radiátoru, protože teplo může poškodit plasty a pěnu.'),
         ('Mám pro dítě kupovat hůlky?', 'Nejmenší děti ze začátku hůlky nepotřebují. Jakmile zvládají základní oblouky, vybírejte lehké hůlky správné délky a s pevným poutkem. Hůlky na vyrůstání nejsou dobrý nápad.'),
         ('Lze sjezdové hůlky použít na skialpy?', 'Nedoporučuje se. Skialpové hůlky bývají teleskopické, lehčí a mají větší košík do sněhu. Pro stoupání s nimi je pohodlnější přenastavit délku.')],
)

# ------------------------------------------------------------------ bezecke-lyzovani
NEW['bezecke-lyzovani'] = dict(long=True,
    title='Běžecké lyžování: lyže, boty, vázání a hůlky na běžky',
    desc='Běžky pro klasiku i bruslení: lyže, boty, vázání NNN a Prolink, hůlky a oblečení. Jak vybrat délku a typ skluznice a porovnat nabídky obchodů.',
    intro='<p>Běžecké lyžování patří mezi sporty, při kterých se spojí pohyb na čerstvém vzduchu s poměrně nenáročným začátkem. Stačí upravená stopa, vhodná výbava a trocha trpělivosti při prvních kilometrech. '
          'V kategorii <strong>běžecké lyžování</strong> najdete lyže na klasiku, bruslení i kombinované modely, boty, vázání, hůlky a další věci, které se na běžkách hodí: od nákrčníků po vosky.</p>'
          '<p>Nabídky českých obchodů porovnáváme u stejného modelu, takže vidíte, kde je skladem vaše délka lyží nebo velikost bot. Jednotlivé skupiny zboží si prohlédněte v podkategoriích <a href="/bezecke-lyze/">běžecké lyže</a>, '
          '<a href="/bezecke-boty/">boty na běžky</a> a <a href="/bezecke-vazani/">vázání na běžky</a>. Níže vysvětlujeme rozdíl mezi technikami, systémy vázání, výběr délky a to, co je pro začátečníka nutné.</p>',
    guide='<h2>Klasika, bruslení, nebo kombi</h2>'
          '<p>Základní rozhodnutí při koupi běžek je volba techniky. Klasický styl se jezdí ve vyjetých stopách po rovných lyžích, bruslení se jezdí po upravené ploše podobně jako na bruslích. '
          'Každá technika má jinou stavbu lyží, bot i hůlek, takže jedno vybavení se na druhou techniku hodí jen omezeně.</p>'
          + T(['Technika', 'Lyže', 'Boty', 'Hůlky', 'Kde se jezdí'], [
              ['Klasika', 'delší, s prohnutím a stoupací zónou', 'měkčí, pružné v přední části', 'kratší', 'stopa vyfrézovaná rolbou'],
              ['Bruslení', 'kratší a tužší, bez stoupací zóny', 'vyšší, vyztužený kotník', 'delší', 'široká hladká plocha'],
              ['Kombi (combi)', 'kompromis, lehčí na ovládání', 'střední tuhost, univerzální', 'střední délka', 'občasní jezdci, kombinace obou tras'],
              ['Turistické běžky', 'širší, často s šupinami', 'teplejší, vyšší', 'pevné', 'nezpevněné cesty, lesní stezky']]) +
          '<p>Většina začátečníků začíná klasikou, protože je intuitivnější a lze ji jezdit pomalu. Bruslení klade vyšší nároky na rovnováhu a sílu horní poloviny těla, ale po osvojení techniky nabízí vyšší rychlost. '
          'Chcete-li zkoušet obě, zvažte kombinované lyže nebo si jednu techniku nejprve vypůjčte.</p>'
          '<h2>Skluznice a stoupání: vosk, šupiny a skin</h2>'
          '<p>Klasická lyže se musí v místě odrazu zachytit ve sněhu a při skluzu kloužat. Jak to řeší, rozhoduje o údržbě a komfortu.</p>'
          '<ul><li><strong>Voskové lyže</strong> mají hladkou skluznici a do středu se nanáší stoupací vosk podle teploty a typu sněhu. Nabízejí nejlepší výkon, ale vyžadují znalosti a čas.</li>'
          '<li><strong>Bezvoskové lyže se šupinami</strong> mají ve střední části vzor, který zabrání couvání. Nevyžadují mazání odrazové zóny, jízda je méně kluzná a při změnách teplot mohou hlučet.</li>'
          '<li><strong>Skin lyže</strong> mají v zóně odrazu pás z vlákna, podobně jako stoupací pásy skialpů. Nemažou se, zajišťují dobrý záběr v širším rozsahu teplot a hodí se pro rekreační jezdce.</li>'
          '<li><strong>Bruslařské lyže</strong> mají celou skluznici hladkou a ošetřují se jen klouzavým voskem.</li></ul>'
          '<p>Skluznici je třeba čas od času ošetřit. Mazání skluznice popisujeme v kategorii <a href="/lyzarske-vosky/">vosky a mazání na lyže</a>, kde najdete i stopové vosky. Doplňky a nářadí na údržbu shrnuje kategorie <a href="/lyzarske-doplnky/">lyžařské hůlky a doplňky</a>.</p>'
          '<h2>Délka běžeckých lyží</h2>'
          '<p>Orientační pravidlo pro klasiku zní: výška postavy plus zhruba dvacet až třicet centimetrů, pro bruslení výška o deset až patnáct centimetrů menší než postava. Skutečnou hodnotu určuje především hmotnost jezdce, protože lyže mají být pod zátěží správně prohnuté. '
          'Výrobci proto uvádějí tabulku s hmotnostními rozsahy u každého modelu. Pokud je jezdec těžší nebo lehčí než průměr, vyplatí se řídit tabulkou, a ne výškou.</p>'
          + T(['Hodnota', 'Co ovlivňuje'], [
              ['Délka lyže', 'stabilita, rychlost a obratnost'],
              ['Zátěžový rozsah', 'správné prohnutí, schopnost záběru a skluzu'],
              ['Šířka lyže', 'uplatnění na upravené stopě, nebo v hlubším sněhu'],
              ['Typ skluznice', 'údržba a chování při změnách teplot']]) +
          '<h2>Vázání NNN, Prolink a další systémy</h2>'
          '<p>Vázání se vybírá spolu s botami, protože musí zapadnout do jejich podrážky. Dva nejrozšířenější systémy jsou NNN od výrobce Rottefella a Prolink, což je označení systému značky Salomon, které se v praxi prodává jako kompatibilní s NNN. '
          'Přesto před koupí vždy ověřte údaj o kompatibilitě přímo u výrobce, protože se mezi generacemi liší. Starší systém SNS se dnes vyskytuje už jen sporadicky, proto při koupi použitého zboží kontrolujte označení na botě i na vázání.</p>'
          '<p>Mnoho moderních lyží se prodává s montážní lištou (u Rottefelly NIS), do které se vázání NNN dá přišroubovat nebo posunout. Takto se dá nastavit poloha vázání podle těžiště. Kompletní nabídku najdete v kategorii <a href="/bezecke-vazani/">vázání na běžky</a>.</p>'
          '<h2>Boty na běžky</h2>'
          '<p>Správně padnoucí bota rozhoduje o pohodlí víc než samotná lyže. Pro klasiku se hodí boty nižší, s ohebnou podrážkou a volností v přední části. Bruslařské boty mají vyztužený kotník a tužší podrážku, aby se přenesla síla do lyže. '
          'Kombinované boty se vyskytují s vyšší pevností a vyhovují většině rekreačních jezdců. Při měření nezapomeňte na ponožky, které budete nosit. Tenké běžkařské ponožky se liší od silných skialpových nebo trekových, a mohou změnit pocit z velikosti o půl čísla.</p>'
          '<ul><li>Bota by neměla tlačit na prsty, ale pata se nesmí zvedat.</li>'
          '<li>Zkontrolujte, zda je na botě uvedený systém vázání, které máte.</li>'
          '<li>U dětí zvolte velikost jen s malou rezervou pro tenkou ponožku, ne o celou velikost větší.</li></ul>'
          '<p>Podrobné rady a sortiment najdete v kategorii <a href="/bezecke-boty/">boty na běžky</a>. Pro pohodlí vyzkoušejte také <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, případně <a href="/merino-ponozky/">merino ponožky</a>.</p>'
          '<h2>Hůlky, které se na běžky hodí</h2>'
          '<p>Běžecké hůlky jsou delší než sjezdové. Orientačně se pro klasiku počítá hodnota kolem 83 procent výšky postavy, pro bruslení kolem 89 procent. U začátečníků je lepší volit raději kratší, ať se hůlkou neodráží z nepohodlné pozice. '
          'Uhlíkové hůlky jsou lehčí a lépe tlumí vibrace, hliníkové odolnější proti poškození. Poutko se nastavuje tak, aby se dlaň při odrazu opírala o jeho spodní část. '
          'Další informace o hůlkách naleznete v kategorii <a href="/lyzarske-hole/">lyžařské hole</a>.</p>'
          '<h2>Oblečení na běžky</h2>'
          '<p>Při běhu na lyžích člověk vyrábí hodně tepla, takže oblečení musí být lehké a prodyšné. Vyplatí se cibulový systém: spodní vrstva z <a href="/termopradlo/">termoprádla</a> nebo <a href="/merino-pradlo/">merino prádla</a>, '
          'střední z <a href="/funkcni-mikiny/">funkční mikiny</a> a svrchní lehká bunda proti větru. V mrazu pomohou <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/nakrcniky-a-satky/">nákrčník</a> a <a href="/cepice-a-celenky/">čepice nebo čelenka</a>. '
          'Věc, která mnohé překvapí: rukavice na běžky mají být tenčí než sjezdové, jinak se ruce při námaze brzy zpotí.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce kategorie narazíte na značky ' + B(('fischer', 'Fischer'), ('alpina', 'Alpina'), ('rossignol', 'Rossignol'), ('madshus', 'Madshus'), ('salomon', 'Salomon'), ('oneway', 'Oneway'), ('peltonen', 'Peltonen'), ('rottefella', 'Rottefella'), ('atomic', 'Atomic'), ('sporten', 'Sporten'), ('inovik', 'Inovik'), ('skivo', 'Skivo')) + '. '
          'Rottefella je známá především vázáním, Fischer, Rossignol, Madshus, Salomon a Atomic vyrábějí lyže i boty. Alpina a Sporten se objevují mezi výrobci lyží a bot pro rekreační jezdce. '
          'Konkrétní modely se mohou měnit se sezónou, proto vždy ověřte skladovost.</p>'
          '<h2>Pro koho jaké vybavení</h2>'
          '<h3>Začátečníci a rodiny</h3>'
          '<p>Pro první sezóny stačí skin nebo šupinatá lyže na klasiku, pohodlné boty a pevné hůlky. Nemá smysl investovat do závodního modelu, který potřebuje precizní mazání. Dětem pořiďte raději komplet lyží, bot a vázání, kde se nemusí řešit kompatibilita jednotlivých částí.</p>'
          '<h3>Rekreační jezdci</h3>'
          '<p>Ti, kdo vyrážejí pravidelně na víkendy, ocení lepší skluznici, lehčí boty a hůlky z kompozitu. Skin lyže pomohou při změnách počasí a ušetří složité mazání.</p>'
          '<h3>Závodníci a pokročilí</h3>'
          '<p>Pokročilí řeší mazání, lyže podle sněhu a váhy a zvlášť klasické a bruslařské vybavení. U nich se vyplatí servis lyží a výběr podle zátěžových tabulek. Poradí trenér nebo klub.</p>'
          '<h2>Péče o běžky</h2>'
          '<p>Po jízdě lyže osušte, očistěte skluznici od nečistot a zbytků vosku a uložte je na suchém místě. Před sezónou naneste klouzavý vosk, v průběhu zimy ho podle potřeby doplňujte. Šupinaté lyže se čistí kartáčem, skin pásy se chrání před prachem a nedotýkají se mastnými prsty. '
          'Boty po jízdě vyjměte z tašky a sušte při pokojové teplotě, ne u radiátoru. Pro přepravu se hodí <a href="/lyzarske-vaky-a-tasky/">vak na lyže</a>, který chrání lyže před poškrábáním.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Nákup lyží podle výšky bez kontroly zátěžového rozsahu.</li>'
          '<li>Záměna systémů vázání, kdy boty a vázání nepasují k sobě.</li>'
          '<li>Použití bruslařské výbavy pro klasickou stopu a naopak.</li>'
          '<li>Příliš teplé oblečení, ve kterém se jezdec brzy zpotí.</li>'
          '<li>Kupování bot s rezervou velkou jako u zimních bot.</li>'
          '<li>Podcenění údržby skluznice, při které lyže ztrácejí kluznost.</li></ul>'
          '<h2>Doplňková výbava a další sporty</h2>'
          '<p>Kdo běhá na lyžích, často zkouší i skialpy a sjezd. Přehledy najdete v kategoriích <a href="/skialpinismus/">skialpinismus</a>, <a href="/sjezdove-lyze/">sjezdové lyže</a> a <a href="/lyzarske-obleceni/">lyžařské oblečení</a>. '
          'V létě se běžkaři rádi udržují v kondici na kolečkových lyžích nebo při běhu, k čemuž slouží <a href="/bezecka-obuv/">běžecká obuv</a> a hole na nordic walking nebo kolečkové lyže s hůlkami.</p>'
          '<h2>Kdy nakupovat</h2>'
          '<p>Největší výběr velikostí bývá na začátku sezóny, jenže právě tehdy se rozebírají i oblíbené modely. Kdo chce vybírat v klidu, může nakupovat už v létě a na podzim. '
          'U lyží a bot ověřte velikost a systém vázání, u hůlek délku. Z nabídek více obchodů snadno zjistíte, kde se vybrané kombinace dají koupit nejrychleji.</p>',
    faq=[('Jaké běžky koupit pro začátečníka?', 'Většině začátečníků vyhovují lyže na klasiku s šupinatou nebo skin skluznicí, protože se nemusí mazat. K nim patří pohodlné boty odpovídajícího systému a hůlky správné délky.'),
         ('Jak určit délku běžeckých lyží?', 'Pro klasiku orientačně výška postavy plus dvacet až třicet centimetrů, pro bruslení o deset až patnáct méně. Rozhodující je ale zátěžový rozsah uvedený u modelu, který se řídí hmotností jezdce.'),
         ('Jaký je rozdíl mezi klasikou a bruslením?', 'Klasika se jezdí v kolejích přímým krokem, bruslení bočním odrazem na široké ploše. Mají jiné lyže, boty i hůlky, takže se vybavení nedá volně zaměňovat.'),
         ('Co je to NNN a Prolink?', 'Jsou to dva běžné systémy vázání, u kterých bota zapadá do lišty na lyži. Boty a vázání musí být kompatibilní, proto před koupí ověřte označení systému u výrobce.'),
         ('Potřebuji mazat bezvoskové běžky?', 'Stoupací zónu ne, ale skluznici je dobré občas ošetřit klouzavým voskem. Vosk zlepší skluz a chrání plast proti vysychání.'),
         ('Jak dlouhé hůlky na běžky?', 'Pro klasiku zhruba 83 procent výšky postavy, pro bruslení kolem 89 procent. Začátečníci mohou volit o něco kratší. Hůlky na běžky jsou vždy delší než sjezdové.'),
         ('Mohu jezdit na běžkách po nezpevněné stopě?', 'Ano, k tomu se hodí širší turistické běžky nebo šupinaté lyže s pevnější hranou. Úzké závodní lyže jsou určeny pro upravenou stopu.'),
         ('Jak poznám správnou velikost bot na běžky?', 'Palec se nesmí dotýkat špičky, pata nesmí při došlapu vyskakovat. Měřte s ponožkami, které budete nosit na lyžích, a ověřte systém vázání.'),
         ('Co si obléct na běžky?', 'Několik tenkých vrstev: prodyšné spodní prádlo, lehkou mikinu a bundu do větru. Nejčastější chyba je obléci se příliš teple, protože pohyb produkuje hodně tepla.'),
         ('Mohou děti jezdit na běžkách?', 'Ano, běžky jsou pro děti vhodné, jakmile zvládnou chůzi s lyžemi. Existují dětské komplety s vázáním a botami. Vybírejte lyže podle výšky a váhy, ne na vyrůstání.'),
         ('Je lepší kupovat lyže jako komplet?', 'Pro začátečníky ano, protože vázání a boty bývají kompatibilní. Zkušenější jezdci si často skládají výbavu zvlášť podle techniky a svých potřeb.')],
)

# ------------------------------------------------------------------ florbal
NEW['florbal'] = dict(long=True,
    title='Florbal: hole, čepele, míčky, brány a výbava do haly',
    desc='Florbalové hole, čepele, míčky, brány, brankářská výbava a sálová obuv. Jak vybrat délku, flex a čepel a porovnat nabídky českých obchodů.',
    intro='<p>Florbal je rychlá halová hra, kterou lze začít hrát prakticky kdekoli: stačí hůl, míček a pár kamarádů v tělocvičně. Vybavení je ale víc než jen hůl. '
          'V kategorii <strong>florbal</strong> najdete hole pro děti i dospělé, výměnné čepele, míčky, brány, brankářskou výstroj, chrániče, sálovou obuv a oblečení na trénink.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u konkrétního zboží a uvidíte, kde mají vaši délku hole nebo velikost obuvi. Samostatně se věnujeme kategorii <a href="/florbalove-hole/">florbalové hole</a>, '
          'ostatní položky shrnuje tato stránka. Dozvíte se, jak vybrat délku a tuhost hole, jak se liší čepele, na co se zaměřit u dětské výbavy a co brankáři potřebují navíc. Příbuzný obor najdete v kategoriích <a href="/hokej/">hokej</a> a <a href="/pozemni-hokej/">pozemní hokej</a>.</p>',
    guide='<h2>Z čeho se skládá florbalová výbava</h2>'
          '<p>Každý hráč potřebuje alespoň hůl, míček a vhodnou obuv. Pro školní hodiny a rekreační hru to často stačí, soutěžní týmy přidávají další vybavení.</p>'
          + T(['Položka', 'K čemu slouží', 'Pro koho', 'Na co dát pozor'], [
              ['Florbalová hůl', 'vedení míčku, přihrávky a střelba', 'všichni hráči', 'délka, tuhost a zahnutí čepele'],
              ['Výměnná čepel', 'rychlá obměna opotřebované čepele', 'pokročilejší hráči', 'kompatibilita s násadou'],
              ['Míček', 'trénink i zápas', 'všichni', 'liší se tvrdostí a odolností'],
              ['Brána a mantinely', 'domácí a školní trénink', 'kluby, školy, rodiny', 'rozměr, stabilita a skládání'],
              ['Brankářská výstroj', 'ochrana brankáře', 'brankáři', 'helma, chrániče a dres musí sedět'],
              ['Sálová obuv', 'stabilita a přilnavost v hale', 'všichni', 'světlá, neznačící podrážka'],
              ['Chrániče a doplňky', 'ochrana kolen a očí, tkaničky, pásky', 'děti, brankáři, rekreační hráči', 'velikost a pohodlí']]) +
          '<p>Při nákupu postupujte od hole k obuvi a potom k doplňkům. Hůl rozhoduje o pocitu ze hry, obuv o zdraví kloubů a o tom, jestli vás pustí do školní haly. Oblečení najdete v kategoriích <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/funkcni-tricka/">funkční trička</a> a <a href="/funkcni-mikiny/">funkční mikiny</a>.</p>'
          '<h2>Délka florbalové hole</h2>'
          '<p>Postavte se rovně, hůl opřete špičkou o zem vedle sebe. Při klasickém pravidle by měl konec rukojeti sahat zhruba k pupku nebo k pasu. Kratší hůl zlepšuje vedení míčku v těsném prostoru a rychlé změny směru, delší přidává dosah a páku na střelu. '
          'Hráči v obraně volí o něco delší, útočníci kratší, ale hodně záleží na stylu. Děti si často volí hůl po pas, aby jim nepřekážela, a rodiče by neměli kupovat na vyrůstání.</p>'
          + T(['Výška hráče', 'Orientační délka hole', 'Poznámka'], [
              ['do 130 cm', 'asi 70 až 80 cm', 'mladší školáci, krátké hůlky s měkčí čepelí'],
              ['130 až 150 cm', 'asi 80 až 90 cm', 'období rychlého růstu, kontrolujte před každou sezónou'],
              ['150 až 170 cm', 'asi 90 až 100 cm', 'junioři a drobnější dospělí'],
              ['nad 170 cm', 'asi 100 až 105 cm', 'dospělí hráči, volíte podle stylu']]) +
          '<p>Hodnoty jsou jen orientační a výrobci mají vlastní značení. Pokud je mezi dvěma délkami váhání, mnoho trenérů doporučuje zvolit kratší.</p>'
          '<h2>Flex hole</h2>'
          '<p>Flex je číslo na násadě, které popisuje tuhost. Flex se udává jako průhyb v milimetrech, takže nižší číslo znamená tužší hůl a vyšší číslo měkčí, flexibilnější hůl. Běžné hodnoty se pohybují přibližně od dvaceti do třiceti pěti. '
          'Lehčí a mladší hráči, kteří střílejí s menší silou, potřebují hole měkčí, tedy s vyšším číslem, jinak hůl nedokážou prohnout a střela ztrácí rychlost. Silní střelci volí tužší hole s nižším číslem pro přesnější a rychlejší odpich. '
          'Při rozhodování pomáhá i technika: kdo střílí švihem z kolena, potřebuje jiné vlastnosti než hráč, který střílí z místa zápěstím.</p>'
          '<h2>Čepel a její tvar</h2>'
          '<ul><li><strong>Zahnutí čepele</strong> ovlivňuje, jak snadno míček zvednete. Silnější zahnutí je výhodné pro střelce, mělké pro přesné přihrávky a vedení.</li>'
          '<li><strong>Levá a pravá čepel</strong> se určuje podle toho, která ruka je při držení dole. Správnou stranu nejlépe zjistíte vyzkoušením.</li>'
          '<li><strong>Tvrdost čepele</strong> bývá označena jako měkká nebo tvrdá. Měkká čepel má lepší cit na míček, tvrdá vydrží víc a drží tvar.</li>'
          '<li><strong>Výměnné čepele</strong> se nasazují na násadu a snižují náklady na opravu, protože se nemění celá hůl.</li></ul>'
          '<p>Čepel se časem ohýbá a lámou se její hrany. Vyměňte ji, když ztratí tvar nebo má trhliny. Pokud jde o stejnou technologii, funguje to podobně jako u <a href="/hokejove-cepele-a-nasady/">hokejových čepelí a násad</a>, i když konstrukce se nedají zaměňovat.</p>'
          '<h2>Míčky</h2>'
          '<p>Florbalový míček je lehký plastový s množstvím otvorů. Na trénink stačí běžný míček, do zápasů se používají míčky schválené pro soutěže, které se ve stejné řadě chovají stejně. '
          'Míčky se liší tvrdostí a odolností. Při chladné nebo studené hale se mohou chovat jinak, protože plast je tužší a snadněji praská. Opotřebovaný míček s hranami nebo prasklinami raději vyřaďte, protože snadno mění dráhu a může poškodit čepel.</p>'
          '<h2>Sálová obuv</h2>'
          '<p>V hale potřebujete obuv se světlou, neznačící podrážkou a dobrou přilnavostí. Boty s hrubou dezénovou podrážkou nebo ty, které se hodí na běh po lese, se do haly nehodí. Při výběru sledujte tlumení, pevnou patu a pohodlné zapínání. '
          'Více najdete v kategorii <a href="/salova-obuv/">sálová a halová obuv</a>. Pro rozvoj kondice jsou užitečné také <a href="/bezecka-obuv/">běžecké boty</a>, ale na florbal ne.</p>'
          '<h2>Brankářská výbava</h2>'
          '<p>Florbalový brankář hraje v masce, nosí vycpané kalhoty a vestu a chrániče kolen; rukavice jsou nepovinné. Výstroj je lehčí než v ledním hokeji, ale i tak je pro bezpečí důležitá správná velikost. '
          'Maska musí dobře padnout, aby se nehýbala. Dívejte se na kvalitu zapínání a hlavně na zakrytí obličeje. Dětští brankáři potřebují menší velikosti, které se vyrábějí zvlášť, a pomalu rostoucím dětem je lépe kupovat bez velké rezervy. '
          'Při výběru dbejte na to, aby vesta a kalhoty nesvíraly pohyb v dřepu a aby chrániče kolen po došlápnutí nesklouzávaly.</p>'
          '<h2>Chrániče, brýle a doplňky</h2>'
          '<p>Při rekreační hře se obejdete bez chráničů, ale kolenní návleky a chrániče holení pomáhají při pádech na tvrdém povrchu. Pásky na čepel zlepšují cit pro míček a chrání čepel. '
          'Tkaničky, potítka a čelenky se hodí na delší tréninky. Starší děti ocení <a href="/sportovni-ponozky/">sportovní ponožky</a> s polstrováním a vyztužením v místech největšího zatížení.</p>'
          '<h2>Brány a trénink doma</h2>'
          '<p>Domácí branka s mantinely a sadou míčků pomáhá rozvíjet střelbu a vedení. Skládací branky se rychle uklidí a dají se použít i venku. Při nákupu sledujte rozměr, stabilitu a zda jsou součástí sítě. '
          'Pro trénink uvnitř se hodí hladký povrch, venku asfalt nebo tvrdý povrch, který míček nezpomaluje. Kdo trénuje i na ledě, může zvážit <a href="/hokejove-puky-a-branky/">puky, branky a tréninkové pomůcky</a>, ale míčky a pukové vybavení se nemíchají.</p>'
          '<h2>Pravidla hry a vybavení</h2>'
          '<p>Florbal se hraje v pěti hráčích v poli a brankáři, na hřišti s mantinely, takže míček zůstává ve hře i po odrazu od mantinelu. Florbal je v zásadě nekontaktní, hrubá hra se trestá a rozhoduje technika, rychlost a přehled. '
          'Hůl se nesmí při úderu zvedat nad úroveň kolen a hráč nesmí hrát míček úmyslně nohou ani rukou. Proto je dobré, aby začátečník znal alespoň základní pravidla a bezpečnostní zásady. '
          'Hráči si berou do haly také láhev s pitím, viz <a href="/lahve-a-termosky/">láhve a termosky</a>, protože při intenzivní hře se pije často.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('salming', 'Salming'), ('winnwell', 'Winnwell'), ('bauer', 'Bauer'), ('unihoc', 'Unihoc'), ('freez', 'Freez'), ('tempish', 'Tempish'), ('fat-pipe', 'Fat Pipe'), ('blindsave', 'Blindsave'), ('zone', 'Zone'), ('kubisport', 'Kubisport'), ('trix', 'Trix'), ('kensis', 'Kensis')) + '. '
          'Salming, Unihoc, Fat Pipe a Zone jsou typicky spojeny přímo s florbalem. Značky jako Winnwell a Bauer mají širší záběr a jsou známé hlavně z ledního hokeje. '
          'Zboží stejné značky se v obchodech liší dostupností, proto porovnání pomůže najít vaši kombinaci délky, tuhosti a čepele.</p>'
          '<h2>Pro koho jaká výbava</h2>'
          '<h3>Děti a školní hráči</h3>'
          '<p>Stačí lehká hůl správné délky s měkčím flexem, plastový míček a čistá sálová obuv. Na první trénink nic dalšího nepotřebují. Jakmile začnou pravidelně trénovat v klubu, přibude vlastní výbava a rodiče zjistí, co si trenér přeje.</p>'
          '<h3>Rekreační hráči</h3>'
          '<p>Kdo hraje jednou týdně, ušetří, když se vyhne nejlehčím modelům a vyzkouší střední řadu, která vydrží běžné používání a nesnaží se o závodní tuhost.</p>'
          '<h3>Závodní hráči</h3>'
          '<p>Soutěžní hráči si většinou vybírají lehčí hole, vyladěný flex a tvar čepele podle pozice. Mívají více kusů stejného modelu, aby při zlomení hole změna nebyla citelná.</p>'
          '<h2>Péče o hole a míčky</h2>'
          '<p>Hole po tréninku otřete a uložte v suchu mimo přímé slunce a topení. Plast ztrácí pružnost v extrémním teple i v mrazu, proto ji nenechávejte v autě. Čepele kontrolujte, jestli nemají praskliny, a vyměňte je včas. '
          'Míčky se skladují v pytli a vyřazují se, když jsou poškrábané. Obuv, která se používá v hale, nevystavujte venkovnímu bahnu, jinak se podrážka zanese a přestane držet.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš dlouhá hůl pro dítě, která brání práci s míčkem.</li>'
          '<li>Záměna levé a pravé čepele, kterou odhalíte až při zápase.</li>'
          '<li>Příliš tuhá hůl u lehkého hráče, která snižuje sílu střely.</li>'
          '<li>Kupování lehké obuvi s hrubou podrážkou, která neprojde školní halou.</li>'
          '<li>Použití ztvrdlých míčků v zimě, které mohou prasknout.</li>'
          '<li>Podcenění brankářské výstroje u dětí, kde je vhodná velikost základem bezpečí.</li></ul>'
          '<h2>Kdy nakupovat</h2>'
          '<p>Nejvíc zájmu bývá na začátku školního roku a před klubovou sezónou. Rozebrané bývají hlavně dětské délky a pravá čepel. Kdo nakupuje s předstihem, má větší výběr. Mimo sezónu se naopak objevují slevy na starší řady. '
          'Porovnáním více obchodů zjistíte, kde je zboží skladem a jak rychle dorazí.</p>',
    faq=[('Jak dlouhá má být florbalová hůl?', 'Obvykle sahá k pupku nebo k pasu. Kratší hůl dává lepší vedení míčku, delší větší dosah. Pokud váháte, zvolte kratší.'),
         ('Co znamená číslo u florbalové hole?', 'Udává tuhost hole neboli flex. Jde o průhyb v milimetrech, takže nižší hodnota znamená tužší hůl a vyšší měkčí. Děti a lehčí hráči mají vybírat vyšší číslo (měkčí hůl), silní střelci nižší (tužší hůl).'),
         ('Jak poznám levou nebo pravou hůl?', 'Podle toho, jakou rukou držíte hůl níže. Pokud levou, potřebujete levou čepel. Nejjistější je obě strany vyzkoušet na zkoušku v hale.'),
         ('Kdy vyměnit čepel?', 'Když je zdeformovaná, má praskliny nebo při střele ztrácí pružnost. U hole s výměnnou čepelí stačí změnit čepel, násada může zůstat.'),
         ('Jaké boty nosit do haly?', 'Sálovou obuv se světlou, neznačící podrážkou a dobrou přilnavostí. Běžecké boty s hrubým dezénem nebo boty z venku se do haly většinou nehodí.'),
         ('Jaký míček zvolit?', 'Na trénink stačí běžný, do zápasu se používají míčky schválené pro soutěže. Míčky vyměňte, když jsou poškozené nebo ztvrdlé.'),
         ('Co potřebuje florbalový brankář?', 'Helmu s maskou, chrániče, rukavice a pevné oblečení. Podstatná je správná velikost, ať výstroj sedí a nepřekáží.'),
         ('Hodí se florbalová hůl na hokej?', 'Ne. Florbalová hůl je lehká a určená pro míček. Hokejová hůl je pevnější a jiného tvaru a nedá se zaměnit.'),
         ('Co koupit dítěti na první florbal?', 'Lehkou hůl správné délky, míček a sálovou obuv. Chrániče jsou volitelné. Nekupujte hůl na vyrůstání, protože dlouhá hůl zhoršuje techniku.'),
         ('Jak pečovat o florbalové hole?', 'Po hře otřete, uložte v suchu, nevystavujte extrémním teplotám a kontrolujte čepel. Poškozenou čepel včas vyměňte.'),
         ('Potřebuji doma branku?', 'Není nutná, ale pomáhá s tréninkem střelby. Skládací branky se dají uklidit a použít i venku. Při nákupu sledujte rozměr a stabilitu.')],
)

# ------------------------------------------------------------------ merino-doplnky
NEW['merino-doplnky'] = dict(long=True,
    title='Merino čepice, nákrčníky a rukavice: jak vybrat',
    desc='Merino čepice, nákrčníky, čelenky a rukavice z vlny: gramáž, složení, využití na běhání, lyže i treky. Porovnejte nabídky českých obchodů.',
    intro='<p>Hlava, krk a ruce jsou místa, kde se zima projevuje první, a kde na tom, co nosíte, nejvíc záleží. Merino vlna je pro tyto kousky oblíbená, protože hřeje i vlhká, příliš nezapáchá a na kůži je příjemná. '
          'V kategorii <strong>merino čepice, nákrčníky a rukavice</strong> najdete tenké čepice pod helmu, pletené čepice do města, multifunkční šátky, čelenky, rukavice na běhání i hrubší modely na hory.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného zboží, takže vidíte, kde je skladem barva a velikost. Na této stránce vysvětlujeme rozdíl mezi gramážemi a směsmi, '
          'kdy volit čistou vlnu a kdy příměs syntetiky, a jak o doplňky pečovat. Doplňující výbavu najdete v kategorii <a href="/merino/">merino oblečení</a>.</p>',
    guide='<h2>Co kategorie obsahuje</h2>'
          '<p>Merino doplňky se liší tloušťkou, střihem a určením. Stejná vlna se přitom chová jinak v lehkém pleteném nákrčníku a ve vrstvených rukavicích.</p>'
          + T(['Typ', 'Pro koho a kdy', 'Vlastnost', 'Na co dát pozor'], [
              ['Tenká čepice', 'běh, pod helmu, přechodné období', 'lehká, dobře dýchá', 'v silném mrazu nestačí samotná'],
              ['Pletená čepice', 'město, procházky, hory', 'tlustší, hřeje déle', 'může být při námaze příliš teplá'],
              ['Čelenka', 'běh, běžky, kolo', 'chrání uši, nezahřívá temeno', 'bez krytí temene se hodí do mírného chladu'],
              ['Nákrčník a multifunkční šátek', 'kolem krku, přes nos a ústa, jako čepice', 'univerzální, nízká váha', 'nižší těsnost proti větru'],
              ['Kukla a ochrana obličeje', 'extrémní mráz a vítr', 'kryje obličej a krk', 'vyžaduje vhodnou velikost, jinak tlačí'],
              ['Tenké rukavice', 'běh, kolo, vložka pod jiné rukavice', 'citlivé prsty, dobře dýchají', 'nechrání před vodou ani větrem'],
              ['Silnější rukavice a palčáky', 'zimní procházky, hory', 'teplé a měkké', 'nevhodné na techničtější sporty']]) +
          '<p>Podobné zboží z jiných materiálů najdete v kategoriích <a href="/cepice-a-celenky/">čepice, kšiltovky a čelenky</a>, <a href="/nakrcniky-a-satky/">nákrčníky a kukly</a> a <a href="/sportovni-rukavice/">rukavice</a>. Merino vyniká tam, kde se člověk potí a pak zastaví.</p>'
          '<h2>Proč právě merino</h2>'
          '<p>Vlákna merino vlny jsou tenká a jemná, proto nedrbou pokožku jako hrubší vlna. Vlna dokáže pojmout vodní páru, aniž by byla na dotek mokrá, takže při námaze odvádí vlhkost od pokožky. '
          'Při zastavení nevychladne tak rychle jako bavlna, což se hodí při přestávce na vrcholu kopce. Přírodní vlákna také méně zachycují pachy, takže doplněk vydrží několik dní bez praní. '
          'Nevýhodou je vyšší pořizovací cena a menší odolnost proti otěru než u čisté syntetiky, proto se často kombinuje s dalšími vlákny.</p>'
          '<h2>Čistá vlna, nebo směs?</h2>'
          '<ul><li><strong>Čisté merino</strong> je nejjemnější a nejlépe reguluje teplotu. Hodí se na pleť a krk. Je citlivější na mechanické namáhání, proto se u čepic a rukavic používá méně často.</li>'
          '<li><strong>Směs s polyamidem nebo polyesterem</strong> zvyšuje pevnost a tvarovou stálost. Rukavice a čepice s příměsí se méně vytahují.</li>'
          '<li><strong>Elastan nebo lycra</strong> dodá střihu pružnost a pomůže přilnout k hlavě nebo prstům.</li>'
          '<li><strong>Podšívka z fleecu</strong> přidává izolaci, ale snižuje prodyšnost. Hodí se spíš na pomalejší pohyb.</li></ul>'
          '<p>Složení je na štítku uvedeno v procentech. Čím vyšší podíl merina, tím jemnější pocit, ale také vyšší nároky na údržbu.</p>'
          '<h2>Gramáž a síla pleteniny</h2>'
          '<p>Gramáž udává hmotnost materiálu na metr čtvereční. Lehčí materiály, zhruba do dvou set gramů, se hodí na pohyb, kde se těleso zahřeje, silnější patří na pomalejší aktivity a chladné počasí. '
          'Nízká gramáž neznamená horší kvalitu, jen jiné určení. Lehká čepice pod helmu je mnohdy praktičtější než tlustá, která se pod ní nevejde. '
          'Rozhoduje také hustota pleteniny: hustá pletenina lépe chrání před větrem, řidší lépe větrá.</p>'
          '<h2>Čepice a čelenky</h2>'
          '<p>Čepici volte podle sportu. Na běh a rychlé aktivity se hodí tenká, těsně přiléhavá a nenasákavá, která vás nezahřeje příliš. Pro chůzi a odpočinek je lepší hustější pletenina s dvojitou vrstvou. '
          'Na lyžování, kde se čepice nosí pod <a href="/lyzarske-helmy/">lyžařskou helmou</a>, vyberte tenkou a bezešvou, ať netlačí. Přehled lyžařských variant najdete v kategorii <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>. '
          'Čelenka chrání uši a nechává temeno vyvětrat, takže se hodí při intenzivním pohybu, například na <a href="/bezecke-lyzovani/">běžkách</a>, kde je tělo teplé a hlava se rychle přehřívá.</p>'
          '<h2>Nákrčníky a multifunkční šátky</h2>'
          '<p>Nákrčník je nejuniverzálnější kus: dá se nosit kolem krku, přes ústa, jako čelenka nebo jako lehká čepice. Merino varianta je příjemná na kůži a málo zapáchá, což oceníte při vícedenních výletech. '
          'Při větru a mrazu volte delší tubus, který zakryje krk i bradu. Na chladné ráno stačí tenký, do mrazu silnější nebo dvouvrstvý. Nákrčník není náhrada za šálu, ale doplněk, který se vejde do kapsy. '
          'Podrobněji se zabýváme variantami z jiných materiálů v kategorii <a href="/nakrcniky-a-satky/">nákrčníky a kukly</a>.</p>'
          '<h2>Rukavice</h2>'
          '<p>Při výběru rukavic je rozhodující využití. Tenké merino rukavice se hodí pod jiné rukavice, na běh a kolo. Silnější pletené se hodí na procházky, ale nechrání před vlhkem. '
          'V horách, kde hrozí sníh a vítr, se nosí jako vnitřní vrstva pod <a href="/lyzarske-rukavice/">lyžařskými rukavicemi a palčáky</a>. Pro cyklisty jsou k dispozici <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>. '
          'Velikost se měří obvodem dlaně těsně pod prsty. Rukavice mají sedět přiléhavě, ale bez napětí, protože tlak na prsty zhoršuje prokrvení a je v mrazu nepříjemný.</p>'
          + T(['Aktivita', 'Co zvolit', 'Proč'], [
              ['Běh', 'tenká čepice nebo čelenka, tenké rukavice, lehký nákrčník', 'hodně tepla, potřeba prodyšnosti'],
              ['Běžky', 'čelenka nebo tenká čepice, tenké rukavice', 'intenzivní pohyb, vyšší produkce tepla'],
              ['Sjezdové lyžování', 'tenká čepice pod helmu, nákrčník, rukavice jako vnitřní vrstva', 'větší zima při jízdě, přestávky na lanovce'],
              ['Treky a túry', 'střední čepice, nákrčník, silnější rukavice do batohu', 'proměnlivé počasí'],
              ['Město a procházky', 'pletená čepice a nákrčník', 'pohodlí a vzhled']]) +
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('lasting', 'Lasting'), ('kama', 'Kama'), ('smartwool', 'Smartwool'), ('icebreaker', 'Icebreaker'), ('sensor', 'Sensor'), ('mons-royale', 'Mons Royale'), ('husky', 'Husky'), ('buff', 'Buff'), ('eisbar', 'Eisbär'), ('devold', 'Devold'), ('kari-traa', 'Kari Traa'), ('fjallraven', 'Fjällräven'), ('reima', 'Reima'), ('westin', 'Westin')) + '. '
          'Lasting, Kama a Sensor jsou české značky, Smartwool, Icebreaker, Mons Royale a Devold jsou známé především merino oblečením. Buff se proslavil multifunkčními šátky. '
          'Obchody nabízejí různé barvy a velikosti, takže se vyplatí porovnat více nabídek.</p>'
          '<h2>Jak o merino doplňky pečovat</h2>'
          '<p>Merino se pere v mírné teplotě, nejlépe v jemném cyklu nebo ručně, s pracím prostředkem určeným na vlnu. Nepoužívejte aviváž, která zalepuje vlákna a snižuje schopnost odvádět vlhkost. '
          'Neždímejte násilně a nesušte na radiátoru, protože vlna se smrští a změní tvar. Nejlépe se suší rozložená naplocho při pokojové teplotě. '
          'Větrání mezi nošením pomůže víc než časté praní. Případné žmolky lze opatrně sundat hřebenem nebo strojkem na bobky. Při skladování v létě chraňte doplňky před moly v uzavřeném obalu.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Volba příliš silné čepice na intenzivní pohyb, ve které se hlava přehřívá.</li>'
          '<li>Nákup rukavic bez přemýšlení, jestli jsou určeny jako vnitřní, nebo vnější vrstva.</li>'
          '<li>Očekávání, že merino ochrání před větrem a deštěm. Pletená vlna vlhkost nasaje a vítr prochází.</li>'
          '<li>Praní na vysokou teplotu nebo sušení v sušičce.</li>'
          '<li>Nevšímání si složení: čistá vlna rukavic se rychleji opotřebí na dlaních.</li>'
          '<li>Příliš těsné velikosti u nákrčníku nebo čepice, které tlačí a nepříjemně se nosí.</li></ul>'
          '<h2>Jak se hodí do systému vrstvení</h2>'
          '<p>Merino doplňky doplňují vrstvený systém, který začíná spodním prádlem. Pro tělo máte <a href="/merino-tricka/">merino trička</a>, <a href="/merino-pradlo/">merino spodní prádlo a legíny</a>, <a href="/merino-mikiny/">merino mikiny a svetry</a> '
          'a <a href="/merino-ponozky/">merino ponožky</a>. Doplňky pak řeší nejcitlivější místa, kde se chlad dostává nejrychleji. Pro hodně chladné počasí je třeba přidat větruodolnou svrchní vrstvu, třeba z nabídky <a href="/softshellove-bundy/">softshellových bund</a>, a pod ni termo prádlo, viz <a href="/termopradlo/">funkční a termo prádlo</a>.</p>'
          '<h2>Pro koho které doplňky</h2>'
          '<h3>Běžci a sportovci</h3>'
          '<p>Potřebují lehké a tenké kusy, které odvádějí vlhkost. Čelenka a tenké rukavice vydrží v mírném chladu, nákrčník se dá stáhnout dolů, když se oteplí.</p>'
          '<h3>Turisté a horolezci</h3>'
          '<p>Ocení zálohu v batohu: tenkou čepici a rukavice, které zaberou málo místa. Merino se nepotí tak výrazně a po zastavení nevychladne.</p>'
          '<h3>Lyžaři</h3>'
          '<p>Pro sjezd se hodí tenká čepice pod helmu, nákrčník a tenké rukavice jako vnitřní vrstva. Pro běžky převažují čelenky a lehké modely.</p>'
          '<h3>Děti a citlivá pokožka</h3>'
          '<p>Pro děti je merino příjemné, ale ověřte, jestli štítek uvádí možnost praní a jestli se nehodí spíš hladší pletenina. Citlivá pokožka může reagovat na jakékoli vlákno, proto ho nejprve vyzkoušejte krátkou dobu.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Čepice se vybírají podle obvodu hlavy měřeného nad obočím a nad ušima. Dětské velikosti rostou rychle, proto zvolte pružnější pleteninu, která se přizpůsobí. U nákrčníku sledujte délku tubusu a obvod, aby šel přetáhnout přes hlavu, ale netlačil na krku. Při nejistotě zvolte velikost, která po vyprání zůstane přiléhavá.</p>'
          '<h2>Kdy kupovat</h2>'
          '<p>Největší výběr barev a velikostí bývá na podzim, kdy se prodává nová kolekce. V zimě se často rozebírají populární velikosti a barvy. Po sezóně se objevují zbytky řad, na které se dá narazit zvlášť, pokud nehledáte konkrétní barvu. '
          'Přes léto může být doba na koupi vhodná, protože si lze vybírat v klidu. Doplňky z merina vydrží několik sezón, pokud se o ně správně pečuje, a zaplatit za kvalitu se tak vyplatí víc než kupovat každý rok nové.</p>',
    faq=[('Je merino doplněk teplejší než běžný pletený?', 'Záleží na tloušťce a hustotě pleteniny. Merino hřeje i při navlhnutí a lépe odvádí vlhkost, ale silná pletená čepice z jiné vlny může být stejně teplá.'),
         ('Co znamená gramáž u merino čepice?', 'Udává hmotnost materiálu na metr čtvereční. Nižší gramáž je lehčí a prodyšnější, vyšší hřeje víc. Pro aktivní pohyb se hodí nižší, pro klidnější aktivity vyšší.'),
         ('Škrábe merino na pokožce?', 'Jemná merino vlákna obvykle nedráždí. Citlivost je ale individuální a záleží také na zpracování. Doplněk, který se dotýká obličeje, nejdříve zkoušejte krátkodobě.'),
         ('Jak prát merino nákrčník?', 'V mírné teplotě v jemném programu nebo ručně, s pracím prostředkem pro vlnu a bez aviváže. Nesušte v sušičce ani na radiátoru, nejlépe rozložený naplocho.'),
         ('Hodí se merino rukavice na běhání?', 'Ano, tenké merino rukavice dobře dýchají a nezahřívají přes míru. V dešti nebo silném větru ale nestačí a potřebujete rukavice s membránou.'),
         ('Jaký nákrčník vybrat na lyže?', 'Tenký až střední tubus, který se dá stáhnout přes bradu a nos a nepřekáží pod helmou nebo bundou. Při velkém větru volte delší model.'),
         ('Kolik procent merina má mít doplněk?', 'Není jediné správné číslo. Čisté merino je nejjemnější, příměs polyamidu nebo polyesteru zvyšuje odolnost a tvarovou stálost. Rukavice a čepice proto často obsahují část syntetiky.'),
         ('Je merino vhodné pod lyžařskou helmu?', 'Ano, tenká merino čepice nebo čelenka dobře zapadá pod helmu, hřeje a odvádí vlhkost. Čepice nesmí být příliš silná, aby helma dobře seděla.'),
         ('Proč merino nezapáchá?', 'Vlna nasákne vlhkost a pach se tolik neváže jako u syntetiky. Nezapáchá nikdy úplně, ale vydrží déle bez praní a stačí ji vyvětrat.'),
         ('Mohu merino skladovat v létě v obalu?', 'Ano, ale uzavřete ho čistý, protože moli napadají špinavou vlnu. Doplněk nechte před uložením zcela vyschnout.'),
         ('Jak poznat správnou velikost rukavic?', 'Změřte obvod dlaně těsně pod prsty a porovnejte s tabulkou výrobce. Rukavice mají sedět přiléhavě, ale ne tlačit.')],
)
