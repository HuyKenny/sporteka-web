"""sporteka.cz — wave 11e (4. 11. 2026): long texts (>= 1500 words) for three categories.
General true facts only, no prices; brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ silnicni-bezecke-boty
NEW['silnicni-bezecke-boty'] = dict(long=True,
    title='Silniční běžecké boty – pánské i dámské, výběr',
    desc='Silniční běžecké boty pánské a dámské: tlumené, neutrální, stabilní i závodní. Průvodce výběrem, velikostí a péčí, porovnání nabídky českých obchodů.',
    intro='<p><strong>Silniční běžecké boty</strong> jsou stavěné pro asfalt, dlažbu, zpevněné cyklostezky a běžecké dráhy. Od trailových modelů se liší hladší podrážkou, měkčí mezipodešví a nižší hmotností. Jejich úkolem je pohltit opakované nárazy a nechat vás běžet bez zbytečné námahy. Pár, který sedí kamarádovi, ale nemusí sedět vám, protože záleží na tvaru chodidla, hmotnosti, tempu a týdenním nájezdu.</p>'
          '<p>Na Sportece porovnáte pánské i dámské modely z českých obchodů a vidíte, kde je vaše velikost skladem. Pro terén se podívejte na <a href="/trailove-boty/">trailové boty</a>, nadřazený přehled najdete v <a href="/bezecka-obuv/">běžecké obuvi</a> a ke každému páru patří kvalitní <a href="/sportovni-ponozky/">sportovní ponožky</a>. Níže rozebíráme typy bot, velikost, drop, tlumení i péči.</p>',
    guide='<h2>Jak si vybrat silniční běžecké boty krok za krokem</h2>'
          '<p>Výběr je jednodušší, když si nejdřív odpovíte na čtyři otázky: kolik kilometrů týdně uběhnete, jakým tempem, na jakém povrchu a zda vás něco bolí. Teprve podle toho se rozhodněte mezi měkkou, stabilní nebo rychlou botou. Vzhled a barva jsou až poslední kritérium, i když u dlouhých tréninků hraje roli i radost z toho, jak boty vypadají.</p>'
          '<h3>Typy silničních bot a komu se hodí</h3>'
          + T(['Typ boty', 'Charakter', 'Pro koho'], [
              ['Maximálně tlumená', 'vysoká podrážka, měkká pěna, vyšší hmotnost', 'dlouhé a pomalé běhy, těžší běžci, regenerace'],
              ['Neutrální univerzální', 'vyvážené tlumení i odraz', 'většina rekreačních běžců a začátečníků'],
              ['Stabilní', 'pevnější boční vedení patní a střední části', 'běžci, kterým se noha stáčí dovnitř'],
              ['Lehká tréninková', 'nižší podešev, pružnější odraz', 'rychlejší tréninky a kratší tratě'],
              ['Závodní', 'minimum hmotnosti, často tuhá vložka', 'závody a intervaly, ne každodenní kilometry'],
              ['S karbonovou deskou', 'tuhá deska a výrazná pěna', 'zkušení běžci, kteří závodí nebo trénují na tempo']]) +
          '<h3>Neutrální, nebo stabilní bota</h3>'
          '<p>Pronace je přirozené propadnutí nohy dovnitř po došlapu a většinou je v pořádku. Stabilní boty mají u klenby pevnější materiál, který pohyb brzdí. Při opakované bolesti kolene či holeně se poraďte s fyzioterapeutem; stabilní boty nejsou lék, jen jedna z možností. Při pochybnostech vám v dobrém běžeckém obchodě nahrají videoanalýzu na pásu. Neutrální bota je pro většinu lidí správná volba a zbytečná korekce může vadit víc než její absence.</p>'
          '<h3>Velikost a zkoušení</h3>'
          '<p>Chodidlo se při běhu roztahuje a večer bývá největší, proto boty měřte odpoledne nebo navečer. Před špičkou potřebujete rezervu zhruba na šířku palce, jinak vám při sbíhání kopců naráží nehty o špičku. Pata má držet bez vyklouzávání a střed boty nesmí tlačit do nártu. Zkoušejte v ponožkách, ve kterých poběžíte, a obě boty zašněrujte. Velikostní tabulky se u značek liší, proto se orientujte spíše podle délky stélky v centimetrech než podle čísla na krabici.</p>'
          '<h3>Drop, tlumení a hmotnost</h3>'
          '<p>Drop je výškový rozdíl mezi patou a špičkou boty. Vyšší hodnota odlehčuje Achillovku a lýtka, nižší vás nutí k plošším došlapům a více zatěžuje chodidlo. Na nižší drop se přecházejte postupně a nejdřív jen na část tréninků. Tlumení určuje měkkost došlapu, ale příliš měkká pěna může být nestabilní a na kratších tratích ztrácíte odraz. Lehčí bota se běží svižněji, těžší nabízí víc ochrany. Mezi těmito póly si zvolte kompromis podle toho, co dělá většinu vašich kilometrů.</p>'
          '<h3>Šířka a tvar špičky</h3>'
          '<p>Běžci s širším předonožím by měli hledat modely označené jako wide, případně značky známé prostornější špičkou. Úzká špička způsobuje otlaky a černé nehty. Nohy se u dlouhých běhů zvětšují, a když vám bota sedí těsně už v obchodě, bude při maratonu nesnesitelná. Naopak příliš prostorná bota nechá nohu klouzat dopředu a vede k puchýřům.</p>'
          '<h2>Co sledovat v konstrukci boty</h2>'
          '<h3>Svršek</h3>'
          '<p>Většina silničních bot používá síťovinu, která dobře odvětrává. V zimě nebo v dešti ocení běžci modely s hustší tkaninou, případně variantu s membránou, kde ale hrozí horší prodyšnost. Švy uvnitř by neměly tlačit, a pokud ano, zkuste ponožku bez švů. Jazyk bývá často integrovaný do svršku, což snižuje tlak v nártu.</p>'
          '<h3>Mezipodešva a podrážka</h3>'
          '<p>Mezipodešva je vrstva pěny, která tlumí a vrací energii. Moderní pěny jsou lehčí a odrazivější než klasické EVA směsi, ale často méně odolné vůči opotřebení. Gumová podrážka chrání pěnu před oděrem, a čím víc gumy na vnější straně paty, tím déle bota vydrží na asfaltu. Hladký vzorek je dobrý na suchu, na mokré dlažbě nebo kolejích si dejte pozor na skluz.</p>'
          '<h3>Pata a opora kotníku</h3>'
          '<p>Pevný patní kryt drží patu na místě. Nízký lem u kotníku sice šetří hmotnost, ale pokud vám pata klouže, zkuste šněrování se zajištěním (runner\'s loop), které patu uzamkne.</p>'
          '<h2>Kolik párů a jak často měnit</h2>'
          '<p>Při běhání dvakrát týdně vám stačí jedna univerzální bota. Kdo běhá čtyřikrát a víckrát, ocení druhý pár s jiným charakterem, například měkčí na pomalé dny a lehčí na tempo. Střídání boty rovnoměrně rozkládá zátěž a pěna mezi tréninky stihne obnovit tvar. Výměna je na místě, když se na podešvi objeví hluboká místa bez gumy, pěna vypadá slisovaná, bota se po běhu cítí tvrdší než dřív, nebo se objevují nové bolesti. Počet kilometrů, po kterých bota dosloužila, se liší podle váhy běžce a povrchu, takže si vedete deník nájezdu a hlídejte hlavně vlastní pocit.</p>'
          '<h2>Silniční, nebo trailové boty</h2>'
          '<p>Silniční boty mají měkčí podrážku a minimum vzorku. Trailové mají agresivní vzorek, pevnější špičku a chrání před kameny a kořeny. Na asfaltu se trailová podrážka rychle opotřebuje a jízda je tvrdá, v bahně naopak silniční bota klouže. Pokud běháte střídavě po lese i po silnici, kupte si pro každý povrch jiný pár nebo zvolte hybridní model s mírnějším vzorkem. Pro lehké terénní běhání po zpevněných cestách se hodí i <a href="/sportovni-obuv/">sportovní obuv</a>, ale na delší tratě je specializovaná bota pohodlnější. Chcete-li ochutnat přirozenější došlap, existuje také <a href="/barefoot-obuv/">barefoot obuv</a>, která vyžaduje postupnou adaptaci.</p>'
          '<h2>Pánské a dámské modely</h2>'
          '<p>Dámské boty bývají na stejném lastu o něco užší v patě a předonoží a mají měkčí vedení kotníku. Neznamená to, že žena nemůže nosit pánskou botu, jen je třeba ověřit, zda není příliš široká. Opačně muž s úzkou nohou může najít pohodlí v dámském modelu. Rozhodující je sedět, ne štítek. Nezapomeňte, že číslování se liší podle výrobce i regionu, a ve velikostní tabulce hledejte délku stélky.</p>'
          '<h2>Příslušenství k běhu</h2>'
          '<p>Správná ponožka zabrání puchýřům víc než dražší bota. Bezešvé ponožky z umělého vlákna nebo merina odvádějí pot, bavlna se namočí a tře. K delším tratím se hodí <a href="/bezecke-opasky/">běžecké opasky</a> nebo <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, k měření tempa <a href="/sportovni-hodinky/">sportovní hodinky</a>. Pro týmové a atletické tréninky navazuje kategorie <a href="/atletika/">atletika</a> a pro přípravu na závody <a href="/triatlon/">triatlon</a>. Základní informace o sportu najdete v kategorii <a href="/beh/">běh</a>.</p>'
          '<h2>Povrch, trasa a počasí v praxi</h2>'
          '<p>Asfalt je tvrdší než dlažba z kostek a ta zase tvrdší než udusaná cesta, takže stejná bota působí na každém povrchu jinak. Kdo běhá převážně po městě, ocení měkčí mezipodešev, kdo střídá park a pěšinu, může zvolit univerzálnější model. Při běhu v dešti sledujte, jak se vzorek chová na mokrých přechodech a kolejích. Za tmy se hodí reflexní prvky na svršku, které zvyšují viditelnost, a doplňkem může být čelovka nebo reflexní vesta. Před delším během zvažte i trasu: stále stejný okruh namáhá tytéž svaly, proto ji občas změňte.</p>'
          '<h2>Péče o boty</h2>'
          '<ul><li>Po běhu vyndejte vložky a povolte šněrování, ať boty rychleji uschnou.</li>'
          '<li>Mokré boty sušte při pokojové teplotě, ne na topení, protože horko poškodí lepené spoje a pěnu.</li>'
          '<li>Nečistotu odstraňte kartáčem a vlažnou vodou, pračce se vyhněte.</li>'
          '<li>Boty nenechávejte v zavazadlovém prostoru auta na slunci.</li>'
          '<li>Silniční boty nepoužívejte na běžné chození celý den, zbytečně se opotřebují.</li></ul>'
          '<h2>Sezónnost a počasí</h2>'
          '<p>V létě vyhledávejte maximálně prodyšný svršek a lehké tlumení. V zimě naopak záleží na přilnavosti na vlhkém povrchu a na tom, zda jsou boty dost široké na silnější ponožku. Při mrazu tuhne pěna a bota působí tvrději, což je normální. Před podzimní sezonou závodů je vhodné nové boty rozběhat alespoň několika kratšími běhy, aby měly čas přizpůsobit se noze.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii najdete nabídku od značek {B(("mizuno", "Mizuno"), ("asics", "Asics"), ("adidas", "Adidas"), ("nike", "Nike"), ("on", "On"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("saucony", "Saucony"), ("hoka", "Hoka"), ("new-balance", "New Balance"), ("salomon", "Salomon"), ("altra", "Altra"), ("skechers", "Skechers"), ("joma", "Joma"))}. Každý výrobce používá vlastní last, takže stejné číslo nemusí sedět stejně. Při změně značky si raději ověřte délku stélky a nekupujte naslepo.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš malá velikost, kvůli které po deseti kilometrech bolí prsty.</li>'
          '<li>Nákup podle vzhledu nebo podle toho, co běhá kamarád.</li>'
          '<li>Závodní lehká bota na každodenní trénink, která se rychle ošoupe.</li>'
          '<li>Běhání ve starých botách s ušlapanou pěnou.</li>'
          '<li>Úplně nový pár na maraton bez předchozího rozběhání.</li>'
          '<li>Opomenutí ponožek a vložek, které rozhodují o pohodlí.</li></ul>'
          '<h2>Jak začít, když jste nový</h2>'
          '<p>Začátečníkovi doporučujeme univerzální neutrální botu s dostatečným tlumením a rezervou ve špičce. Nehoňte se za nejdražšími karbonovými modely, začátečník z nich nic nemá. První týdny střídejte běh s chůzí a pohyb prodlužujte pomalu. Pokud vás něco bolí déle než pár dnů, poraďte se s fyzioterapeutem, ne s prodavačem.</p>',
    faq=[('Jaké silniční běžecké boty zvolit na začátek?', 'Neutrální univerzální pár s dostatečným tlumením, prostornou špičkou a pevnou patou. Důležitější než technologie je, aby vám bota sedla a nikde netlačila.'),
         ('Jaká velikost běžeckých bot je správná?', 'Zhruba o půl až celé číslo větší než běžná obuv, aby před špičkou zbyla rezerva na šířku palce. Měřte navečer, ve správných ponožkách, a sledujte délku stélky.'),
         ('Co znamená drop u běžeckých bot?', 'Je to výškový rozdíl mezi patou a špičkou. Vyšší drop šetří lýtka a Achillovku, nižší povzbuzuje plošší došlap. Při změně dropu přecházejte postupně.'),
         ('Poznám, jestli potřebuji stabilní boty?', 'Orientačně napoví obrus starých bot, ale diagnózu to nenahradí. Analýzu došlapu na pásu nabízejí specializované obchody a při opakované bolesti kolene či holeně se poraďte s fyzioterapeutem.'),
         ('Hodí se karbonové boty pro každého?', 'Ne. Karbonová deska a tuhá pěna jsou stavěné pro rychlejší tempo a závody. Pro pomalé tréninky nebo začátečníky nejsou nutné a bývají méně pohodlné.'),
         ('Mohu v silničních botách běhat v terénu?', 'Po zpevněných lesních cestách ano. V blátě, na kořenech a kamení ale kloužou a nechrání chodidlo, a tam je lepší trailová bota.'),
         ('Jak poznám, že je bota vyběhaná?', 'Pěna je slisovaná a tvrdá, na podešvi chybí guma, pata se kříží nebo začnou bolet klouby a chodidla. Řiďte se pocitem i deníkem najetých kilometrů.'),
         ('Mohu boty prát v pračce?', 'Nedoporučuje se. Bubnování a teplo poškodí lepené spoje i pěnu. Lépe je očistit je kartáčem a vlažnou vodou a nechat doschnout při pokojové teplotě.'),
         ('Mají ženy kupovat dámské modely?', 'Dámské boty sedí většině žen lépe, protože mají užší patu a upravený last. Pokud vám ale pohodlněji sedí pánská varianta, není důvod ji nepoužít.'),
         ('Kdy je nejlepší doba na nákup bot?', 'Kdykoli, kdy je skladem vaše velikost. Starší kolekce jsou častěji zlevněné, a pokud jste s modelem spokojení, vyplatí se je koupit předem a střídat.')],
)

# ------------------------------------------------------------------ kolobezky-a-brusle
NEW['kolobezky-a-brusle'] = dict(long=True,
    title='Koloběžky, brusle a skateboardy – jak vybrat',
    desc='Koloběžky, inline brusle, skateboardy a longboardy pro děti i dospělé. Průvodce velikostí, ložisky, koly a chrániči, porovnání nabídky českých obchodů.',
    intro='<p><strong>Koloběžky, brusle a skateboardy</strong> patří mezi sporty, které zvládne začít skoro každý a kterým stačí kus rovného asfaltu. Každý z nich ale vyžaduje něco jiného. Koloběžka je stabilní a odpouští chyby, inline brusle chtějí čas na zvládnutí rovnováhy a skateboard učí cit pro těžiště. Volba se řídí věkem, výškou, místem jízdy a tím, zda chcete spíš dojíždět, trénovat, nebo dělat triky. Při výběru se vyplatí myslet i na to, kolik místa doma zabere a zda ji unesete do schodů.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů v kategoriích <a href="/kolobezky/">koloběžky</a>, <a href="/inline-brusle/">inline brusle</a>, <a href="/skateboardy/">skateboardy a longboardy</a> a <a href="/chranice-a-helmy/">chrániče a helmy</a>. Pro delší dojíždění existují i <a href="/elektrokolobezky/">elektrokoloběžky</a>. Níže najdete rady, jak vybrat správnou velikost a co nepodcenit.</p>',
    guide='<h2>Jak vybrat podle toho, co chcete jezdit</h2>'
          '<p>Nejdřív si ujasněte účel. Dítě na procházku s rodiči potřebuje něco jiného než teenager do skateparku nebo dospělý, který chce zvládnout cestu do práce. Teprve potom řešte parametry jako velikost kol, hmotnost nebo materiál.</p>'
          + T(['Zájem', 'Co zvolit', 'Na co dát pozor'], [
              ['První kroky nejmenších', 'odrážedlo nebo malá tříkolová koloběžka', 'stabilita, nízký stupínek, lehkost'],
              ['Školák na hřiště', 'dětská koloběžka s nastavitelným řídítkem', 'růst dítěte, brzda, hmotnost'],
              ['Dojíždění po městě', 'koloběžka s většími koly nebo skládací', 'průměr kol, nosnost, brzda'],
              ['Triky a skatepark', 'freestyle koloběžka nebo skateboard', 'pevná konstrukce, malá kola, odolnost'],
              ['Rekreační bruslení', 'inline brusle s měkkou botou', 'podpora kotníku, ložiska, velikost'],
              ['Fitness a rychlá jízda', 'brusle s většími koly a tužším rámem', 'rychlost, sklon zatáčet, zkušenost'],
              ['Svezení po silnici', 'longboard', 'délka desky, tuhost, osy']]) +
          '<h2>Koloběžky</h2>'
          '<h3>Dětské a dospělé modely</h3>'
          '<p>U dětí je klíčová výška řídítek. Má končit zhruba u pasu, aby se dítě nemuselo hrbit ani zvedat ruce. Nastavitelné řídítko vydrží několik sezón a modely s širším stupínkem poskytují větší jistotu. Pro začátečníky jsou dobré trojkolky, které se v zatáčce naklánějí a nepřevrátí se. Starší děti zvládnou dvoukolku s brzdou na zadním kole. Dospělí vybírají podle nosnosti a velikosti kol, přičemž větší kola lépe zvládají nerovnosti.</p>'
          '<h3>Městské, skládací a freestylové</h3>'
          '<p>Městská koloběžka má větší kola s duší nebo plnou pryží, nosnější rám a brzdu. Skládací se vejde do auta či autobusu, ale sklápěcí mechanismus je slabým místem; pravidelně kontrolujte pojistku. Freestylová je malá, tuhá a odolná vůči dopadům, hodí se do skateparku, ale na delší jízdu po městě je nepohodlná. Rozdíl jsou i ložiska a ráfky, které u levných kusů snáze povolí.</p>'
          '<h3>Elektrické koloběžky</h3>'
          '<p>Elektrokoloběžka dojede dál bez námahy, ale je těžší a jejich provoz upravují pravidla pro provoz na silnicích a stezkách. Při koupi sledujte dojezd, nosnost, brzdy, osvětlení a možnost skládání. Provozní předpisy se časem mění, proto je aktuálně ověřte na webu ministerstva dopravy. Nabídku najdete v kategorii <a href="/elektrokolobezky/">elektrokoloběžky</a>.</p>'
          '<h2>Inline brusle</h2>'
          '<h3>Velikost a pohodlí</h3>'
          '<p>Dospělé brusle mají pevnou velikost. Dětské lze často přestavit o několik čísel, aby s nohou rostly. Brusli zkoušejte s ponožkami, ve kterých budete bruslit, a zapněte všechny přezky. Pata nesmí zvedat, prsty mají lehce dosáhnout na špičku. Pokud se při chůzi noha pohybuje, bota je velká. Pohodlí ovlivňuje i tvar boty: měkká sportovní bota je dobrá na rekreaci, vyšší pevná na rychlejší jízdu a kotník podepře lépe.</p>'
          '<h3>Kolečka, ložiska a rám</h3>'
          '<p>Průměr koleček určuje rychlost. Menší kolečka se rychle roztáčejí a obratněji zatáčejí, větší se lépe valí. Tvrdost koleček se udává ve stupních, měkčí kolečka jsou přilnavější a tišší, tvrdší se dlouho nepoškodí a lépe kloužou. Ložiska se označují třídou ABEC, ale vyšší číslo samo o sobě neznamená, že budou lepší, protože hlavně záleží na kvalitě a čistotě. Rám může být plastový nebo hliníkový, hliníkový je tužší a přenáší energii lépe.</p>'
          '<h3>Brzdění a první kroky</h3>'
          '<p>Většina rekreačních bruslí má patní brzdu. Naučte se na rovině klesnout do pozice s pokrčenými koleny a brzdit pomalu, než pojedete z mírného kopce. Začátečník by si měl nejprve zvyknout na stabilitu a nacvičit pád na chrániče. Pro ježdění bez brzdy existují modely do skateparků, ty ale nepatří do provozu.</p>'
          '<h2>Skateboardy a longboardy</h2>'
          '<h3>Rozdíl mezi skateboardem a longboardem</h3>'
          '<p>Skateboard má menší desku s oboustranně prohnutými konci a hodí se k trikům na rampách a v parku. Longboard je delší, nabízí stabilitu a pohodlné svezení, často se používá na dojíždění a carving. Existují i pennyboardy, malé plastové desky vhodné pro děti a krátké trasy. Při koupi se podívejte na šířku desky, tvar a velikost kol.</p>'
          '<h3>Komponenty</h3>'
          + T(['Část', 'Co ovlivňuje', 'Tip'], [
              ['Deska', 'stabilita a ovládání', 'širší pro začátečníky a stabilitu'],
              ['Osy (trucky)', 'zatáčení a stabilita', 'pružnější pro carving, tužší pro triky'],
              ['Kolečka', 'rychlost a přilnavost', 'měkká pro drsný povrch, tvrdá pro park'],
              ['Ložiska', 'plynulost jízdy', 'čistit od prachu a vody'],
              ['Griptape', 'přilnavost chodidla', 'vyměnit, když je ošoupaný']]) +
          '<p>Sestavené desky ušetří starosti začátečníkům, zkušenější jezdci si skládají komponenty sami. U dětí vybírejte menší desku, aby ji udržely pod kontrolou.</p>'
          '<h2>Bezpečnost a chrániče</h2>'
          '<p>Základem je helma, která sedí rovně na hlavě a nesmí se pohybovat, a chrániče zápěstí, loktů a kolen. Zápěstí je u bruslařů nejčastěji zraněná část těla, proto začněte právě jimi. Chrániče vybírejte podle velikosti a musí držet pevně, aby při pádu neujely. Helmy a chrániče najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>. Pro jízdu na kole pak <a href="/cyklisticke-helmy/">cyklistické helmy</a>. Povinnost helmy při jízdě na kole upravuje zákon č. 361/2000 Sb. a týká se osob mladších 18 let; u elektrokoloběžek si aktuální znění ověřte, u klasických koloběžek a bruslí je helma silně doporučená. Přilby po pořádném nárazu vyměňte, i když vypadají v pořádku, protože pěna ztratila schopnost tlumit.</p>'
          '<h2>Jak se začátečník učí</h2>'
          '<p>Nejprve si zvykněte na povrch na rovném prostranství bez provozu, třeba na prázdném parkovišti. Naučte se odrážet oběma nohama, přenášet váhu a zastavit. U skateboardu trénujte nejprve postoj a pomalé zatáčení, triky přijdou později. Na bruslích zvládněte základní postoj, pak jízdu rovně a brzdění. Pomůže kamarád nebo kurz, kde vás naučí padat tak, abyste se nezranili. Čím dřív si osvojíte správný pád, tím méně modřin vás čeká.</p>'
          '<h2>Přeprava, skladování a doprava</h2>'
          '<h3>Jak vybavení bezpečně převážet</h3>'
          '<p>Koloběžku s pevným rámem uložte v autě naležato a zajistěte, aby se nepřevracela. Skládací modely se vejdou do kufru i na zadní sedadlo, ale kontrolujte pojistku sklápění, protože nedotažená se může uvolnit. Brusle převážejte v tašce, ideálně s chrániči na kolečkách, aby neničily zavazadlový prostor. Skateboard noste pod paží kolečky od těla nebo v batohu s upínacími popruhy.</p>'
          '<h3>Skladování mimo sezónu</h3>'
          '<p>Přes zimu vybavení uložte v suchu při pokojové teplotě. Kolečka a ložiska nenechávejte vlhká, dřevěnou desku nikdy nestavte na mokrou podlahu a nenechávejte ji u radiátoru, protože se prohne. U elektrických koloběžek dodržujte pokyny výrobce k uložení baterie. Před novou sezónou provedete celkovou kontrolu: šrouby, brzdu, ložiska a stav chráničů.</p>'
          '<h2>Kde jezdit</h2>'
          '<p>Nejlepší je hladký asfalt bez štěrku, cyklostezky a skateparky. Hrubý povrch zrychluje opotřebení koleček a ztěžuje jízdu, kostky a obrubníky jsou nebezpečné. Nepoužívejte kolečkové sporty ve frekventovaném provozu a ohleduplně se chovejte k chodcům. Na cyklostezkách dodržujte pravidlo jízdy vpravo a předjíždění po ohlášení.</p>'
          '<h2>Údržba a péče</h2>'
          '<ul><li>Před jízdou zkontrolujte dotažení šroubů, os a koleček.</li>'
          '<li>Kolečka bruslí po několika jízdách přehazujte, aby se opotřebovala rovnoměrně.</li>'
          '<li>Ložiska čistěte od prachu a po mokré jízdě osušte, jinak zrezivějí.</li>'
          '<li>U koloběžky sledujte stav brzdy a hustotu pneumatik.</li>'
          '<li>Brusle sušte při pokojové teplotě a vyjměte vložky.</li>'
          '<li>Skateboard po dešti utřete, aby dřevo nebobtnalo a šrouby nerezavěly.</li></ul>'
          '<h2>Jak vybrat pro dítě</h2>'
          '<p>Koupě na vyrůstání se u koloběžek vyplácí díky nastavitelnému řídítku, u bruslí díky přestavitelné velikosti, ale příliš velká obuv nebo deska dítěti ubližuje. Zvolte lehký model, který dítě samo unese a zvládne s ním zahnout. Děti ocení barvu a vzhled, ale rozhoduje funkce. Pokud se dítě na jedné aktivitě nudí, vyzkoušejte jinou. Sporty na kolečkách se navíc dobře doplňují s <a href="/jizdni-kola/">jízdními koly</a> a <a href="/detska-kola/">dětskými koly</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii najdete značky {B(("raven", "Raven"), ("micro", "Micro"), ("powerslide", "Powerslide"), ("tempish", "Tempish"), ("core", "Core"), ("nils", "Nils"), ("met", "MET"), ("bauer", "Bauer"), ("exway", "Exway"), ("fila", "Fila"), ("roces", "Roces"), ("k2", "K2"), ("enuff", "Enuff"))}. Některé se zaměřují na děti, jiné na fitness nebo na elektrickou mobilitu. U každého produktu zkontrolujte parametry, ne jen logo.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Jízda bez helmy a chráničů, zvlášť u začátečníků a dětí.</li>'
          '<li>Příliš velká koloběžka, brusle nebo deska pro dítě.</li>'
          '<li>Nákup nejlevnějšího kusu s plastovými osami, který se brzy rozbije.</li>'
          '<li>Zanedbaná ložiska a opotřebovaná kolečka.</li>'
          '<li>Jízda na hrubém povrchu nebo ve vlhku.</li>'
          '<li>Rychlá jízda z kopce bez zvládnutého brzdění.</li></ul>',
    faq=[('Jaká koloběžka je vhodná pro dítě?', 'Lehká, s nastavitelným řídítkem a širším stupínkem. Řídítka mají končit zhruba u pasu dítěte a brzda musí být dosažitelná i malou rukou.'),
         ('Od kolika let může dítě jezdit na koloběžce?', 'Nejmenší začínají na odrážedle nebo tříkolové koloběžce, obvykle kolem druhého nebo třetího roku. Přesné doporučení uvádí výrobce u konkrétního modelu.'),
         ('Jak vybrat velikost inline bruslí?', 'Podle délky chodidla a velikostní tabulky výrobce. Brusle zkoušejte s ponožkami, ve kterých budete jezdit. Pata nesmí zvedat a prsty se nesmějí tlačit na špičku.'),
         ('Co je to ABEC u ložisek?', 'Je to třída přesnosti ložisek. Vyšší číslo znamená přesnější výrobu, ale na vlastnostech při jízdě záleží i na čistotě a mazání. Pro rekreaci nemusíte kupovat nejvyšší třídu.'),
         ('Jaký je rozdíl mezi skateboardem a longboardem?', 'Skateboard je kratší a slouží ke trikům. Longboard je delší, stabilnější a hodí se na dojíždění a pohodlné svezení po hladkém asfaltu.'),
         ('Které chrániče jsou nejdůležitější?', 'Chrániče zápěstí, protože se při pádu instinktivně opřete rukama. Dále lokty, kolena a helma. Všechny musí sedět pevně a odpovídat velikosti.'),
         ('Jak často otáčet kolečka u bruslí?', 'Přibližně po několika jízdách, podle povrchu a stylu. Kolečka se opotřebují nejvíc na vnitřním okraji, otáčením prodloužíte jejich životnost.'),
         ('Mohu jezdit s elektrokoloběžkou po chodníku?', 'Elektrokoloběžka je podle zákona o silničním provozu malé osobní elektrické vozidlo a jízda po chodníku je zakázána s výjimkami, které stanoví zákon č. 361/2000 Sb. Aktuální znění ověřte u ministerstva dopravy nebo u obce a jezděte ohleduplně.'),
         ('Jak vyčistit ložiska?', 'Vyjměte je z koleček, odstraňte kryt, propláchněte jemným čisticím prostředkem, osušte a lehce namažte. Při nejistotě vyměňte za nová, nejsou drahá.'),
         ('Vyplatí se koupit dětem koloběžku s elektrickým pohonem?', 'Pro děti se většinou nedoporučuje. Rychlost a hmotnost zvyšují riziko úrazu a většina výrobců stanoví minimální věk uživatele.')],
)

# ------------------------------------------------------------------ cyklo-prislusenstvi
NEW['cyklo-prislusenstvi'] = dict(long=True,
    title='Cyklo příslušenství – co na kolo opravdu patří',
    desc='Příslušenství na kolo: brýle, zvonky, zrcátka, lahve, držáky a chrániče. Průvodce výběrem pro město, silnici i terén, porovnání nabídky českých obchodů.',
    intro='<p><strong>Cyklistické příslušenství</strong> mění obyčejnou jízdu v bezpečnější a pohodlnější. Někomu stačí zvonek, světla a lahev na pití, jiný potřebuje brýle, chrániče a držák na telefon. Co skutečně pořídit, záleží na tom, zda jezdíte po městě, po silnici, nebo v terénu, a jak dlouhé trasy zvládáte. Zbytečně pořízená věc leží v šuplíku, chybějící zase kazí výlet. Proto níže rozebíráme, co se vyplatí kupovat jako první a co počká, a také na čem při výběru nešetřit.</p>'
          '<p>Na Sportece najdete <a href="/cyklisticke-bryle/">cyklistické brýle</a>, <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>, <a href="/cyklo-lahve-a-drzaky/">lahve, košíky a držáky telefonu</a> a <a href="/cyklo-chranice/">chrániče pro cyklisty</a>. Související výbavu pokrývají <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zamky/">zámky</a> a <a href="/cyklo-tasky-a-nosice/">brašny a nosiče</a>.</p>',
    guide='<h2>Co na kolo skutečně patří</h2>'
          '<p>Rozlišujte mezi povinnou výbavou a pohodlím. Zákon po cyklistovi vyžaduje, aby bylo jeho kolo za snížené viditelnosti osvětleno, mělo odrazky a funkční brzdy. Zvonek je při jízdě po komunikaci také součást výbavy. Helma je zákonná povinnost pro děti do 18 let a pro ostatní silné doporučení. Aktuální znění ověřte v předpisech, protože se mohou měnit. Vše ostatní je volitelné a vybírá se podle typu jízdy.</p>'
          + T(['Doplněk', 'Hodí se pro', 'Na co si dát pozor'], [
              ['Světla', 'všechny jezdce za šera', 'dosvit, způsob nabíjení, upevnění'],
              ['Zvonek', 'město a stezky', 'hlasitý zvuk, průměr řídítek'],
              ['Zrcátko', 'město, dojíždění', 'stabilní uchycení, velikost plochy'],
              ['Brýle', 'silnice, terén, slunce', 'UV filtr, výměnné zorníky'],
              ['Láhev a držák', 'výlety a tréninky', 'pevné upnutí, objem'],
              ['Držák telefonu', 'navigace', 'bezpečné uchycení, odolnost vůči vibracím'],
              ['Chrániče', 'enduro, downhill, děti', 'velikost, ventilace, pohodlí'],
              ['Blatníky', 'město, deště', 'šířka pláště, upevnění']]) +
          '<h2>Cyklistické brýle</h2>'
          '<h3>Proč je nosit</h3>'
          '<p>Brýle chrání oči před prachem, hmyzem a větrem. Při rychlé jízdě po silnici se do oka dostane i drobný kamínek a v lese větvička. Správné brýle zároveň tlumí oslnění, díky čemuž se méně unavíte.</p>'
          '<h3>Zorníky a jejich barvy</h3>'
          '<p>Tmavé zorníky vyberte do plného slunce, žluté či oranžové zvyšují kontrast v šeru a lese, čiré se hodí do tmy a deště. Fotochromatické se přizpůsobí světlu a nemusíte nosit více zorníků. Hledejte UV ochranu a označení kategorie filtru. Přehled nabízí kategorie <a href="/cyklisticke-bryle/">cyklistické brýle</a>.</p>'
          '<h3>Tvar a uchycení</h3>'
          '<p>Brýle mají sedět těsně, ale netlačit na spánky, a nesmí sjíždět při pohybu hlavy ani zamlžovat. Zkuste je zároveň s helmou, protože zadní konce stran se mohou třít o pásky. Ti, kdo nosí dioptrie, ocení nástavec nebo varianty s dioptrickým rámečkem.</p>'
          '<h2>Zvonky a zrcátka</h2>'
          '<p>Zvonek je nejlevnější způsob, jak upozornit chodce. Vybírejte takový, který vydá čistý a dostatečně hlasitý zvuk a upevníte jej na řídítka tak, abyste na něj dosáhli bez pouštění řidítek. Elektronické a skryté zvonky se montují do konců řídítek. Zrcátko pomáhá ve městě sledovat dění za zády bez otáčení hlavy. Stabilní zrcátko nezkresluje a netřese se, což je u levných variant problém. Zrcátko na helmu nebo brýle je alternativa, ale vyžaduje zvyk. Nabídka se skrývá v kategorii <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>.</p>'
          '<h2>Lahve, košíky a držáky</h2>'
          '<h3>Jak vybrat láhev</h3>'
          '<p>Cyklistická láhev má měkký ventil, který otevřete zuby nebo rukou, a tvar, který pasuje do držáku na rámu. Objem se pohybuje řádově v desetinách litru. Termo lahve udrží nápoj chladný nebo teplý déle, což ocení hlavně léto a zima. Plastové varianty jsou lehčí, ale po čase si zachovávají pach nápojů. Myjte je pravidelně a nechte vyschnout otevřené.</p>'
          '<h3>Držák na láhev</h3>'
          '<p>Držák se montuje na šroubky na rámu. Zkontrolujte, zda je na rámu místo, hlavně u menších velikostí. Materiál držáku může být plastový, hliníkový nebo karbonový. Pevný držák láhev drží i na nerovné cestě, uvolněný ji ztratí. Pro dlouhé trasy použijte dva držáky nebo láhev v zadní kapse dresu.</p>'
          '<h3>Držák telefonu</h3>'
          '<p>Telefon na řídítkách slouží k navigaci a sledování trasy. Zvolte držák s pevným sevřením a zabezpečením proti vibracím, ideálně takový, který telefon obejme z více stran. Při dešti pomůže pouzdro. Zvažte také, že vibrace mohou časem poškodit stabilizaci fotoaparátu v některých telefonech, jak upozorňují někteří výrobci. Pro přehledné navigování vám stačí i <a href="/cyklo-computery/">cyklopočítač</a>. Nabídka je v kategorii <a href="/cyklo-lahve-a-drzaky/">lahve, košíky a držáky telefonu</a>.</p>'
          '<h2>Chrániče pro cyklisty</h2>'
          '<p>Chrániče kolen, loktů, zad a rukavice se používají v bike parcích, na trailech a při enduru. Jejich úkolem je tlumit nárazy při pádu. Vybírejte podle velikosti, protože příliš volný chránič sklouzne přesně v ten okamžik, kdy ho potřebujete. Měkké pěnové varianty jsou lehké a pohodlné, pevné skořepiny chrání lépe, ale hřejí. U dětí volte lehké a odvětrané modely, aby je chtěly nosit. Zvolte také odpovídající helmu: <a href="/mtb-a-integralni-helmy/">MTB a integrální helmy</a>, <a href="/silnicni-cyklohelmy/">silniční helmy</a> nebo <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>. Nabídka pro terén je v kategorii <a href="/cyklo-chranice/">chrániče pro cyklisty</a>.</p>'
          '<h2>Příslušenství podle stylu jízdy</h2>'
          '<h3>Město a dojíždění</h3>'
          '<p>Důležité jsou světla, zvonek, zrcátko, blatníky a spolehlivý zámek. K tomu přibývá nosič s brašnou, aby vás nepálil batoh na zádech. Reflexní prvky a svítivé oblečení v zimě zvyšují šanci, že vás řidič včas uvidí.</p>'
          '<h3>Silnice a trénink</h3>'
          '<p>Silničáři sáhnou po brýlích, lahvi, cyklopočítači a malé podsedlové brašně s duší, montpákami a pumpičkou. Hmotnost se řeší, ale bezpečí je důležitější. Nezapomeňte na <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h3>Terén a bikepark</h3>'
          '<p>V terénu se hodí chrániče, plná helma, pevné rukavice a brýle. Upevnění lahve musí zvládnout otřesy, a proto jsou oblíbené držáky s bočním vstupem. Na výlety pomůže batoh s rezervoárem na vodu.</p>'
          '<h3>Rodinné výlety</h3>'
          '<p>U dětí se hodí zvonek s veselým tvarem, reflexní prvky a helma, kterou si dítě samo vybere, protože pak ji chce nosit. Pro nejmenší jsou k dispozici <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>.</p>'
          '<h2>V jakém pořadí příslušenství pořizovat</h2>'
          '<p>Nejdřív bezpečnost: světla, odrazky, zvonek a helma. Pak věci, které zlepší každou jízdu, tedy láhev s držákem a rukavice. Potom příslušenství podle stylu, například brýle pro silničáře nebo chrániče pro terén. Nakonec doplňky pro komfort, třeba držák telefonu, zrcátko či blatníky. Takto vás nákup nepřetíží a každou novinku opravdu využijete.</p>'
          '<h3>Sezónní doplňky</h3>'
          '<p>Na jaře zkontrolujte, zda se po zimě nezadřely zvonek a upínání držáků. V létě přidejte větší objem na pití a brýle s tmavším zorníkem. Na podzim a v zimě zvyšte důraz na viditelnost, protože se brzy stmívá, a ochraňte ruce a uši. Zimní jízdu usnadní držák lahve s izolací, která brání zamrznutí nápoje.</p>'
          '<h2>Kompatibilita a montáž</h2>'
          '<p>Zvonky, zrcátka a držáky se upínají na řídítka, proto si změřte průměr. Standardně se používá zhruba 22,2 mm u rovných řídítek, silniční řídítka mají odlišný profil. Držák lahve potřebuje na rámu dva závitové otvory, které nemají všechny rámy, jinak použijte upínací varianty. Šrouby dotahujte opatrně, aby nepraskl plast nebo karbon. Při nejistotě vám montáž udělá cykloservis.</p>'
          '<h2>Příslušenství na delší výlety a dovolenou</h2>'
          '<h3>Co si sbalit navíc</h3>'
          '<p>Na vícedenní tůru se kromě základu hodí náhradní světlo nebo powerbanka, lehký zámek, lékárnička a multifunkční nářadí. Do lahve patří voda či iontový nápoj, k ní doplňte malý rezervní objem, pokud jedete krajinou bez obchodů. Brýle uložte do pevného pouzdra, ať se zorníky nepoškrábou v batohu.</p>'
          '<h3>Plánování a orientace</h3>'
          '<p>Při navigaci pomocí telefonu počítejte se spotřebou baterie a mějte záložní mapu offline. Držák telefonu mějte tak, aby displej nebyl na přímém slunci, případně použijte stínítko. Zrcátko u delších tras snižuje únavu krku a zvyšuje přehled o provozu za vámi.</p>'
          '<h3>Rukavice a doplňky pro komfort</h3>'
          '<p>Cyklistické rukavice tlumí vibrace z řídítek, chrání dlaň při pádu a zlepšují úchop v dešti. Gelové vložky ulevují nervům v zápěstí při dlouhých trasách. Pro zimu zvolte delší prsty a větruodolný materiál, pro léto krátké a prodyšné. K tomu přidejte čepici pod helmu, návleky nebo tubus na krk. Každý z těchto kousků váží málo a zabírá minimum místa v kapse dresu, takže se vyplatí mít je pro jistotu s sebou.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Brýle čistěte vodou a měkkou utěrkou, ne papírovým ubrouskem, který zorníky poškrábe.</li>'
          '<li>Lahve myjte po každém výletu a nechte vyschnout otevřené.</li>'
          '<li>Chrániče vyperte podle návodu a nechte uschnout, ať se v nich nemnoží zápach.</li>'
          '<li>Helmu uchovávejte mimo sluneční světlo a chemikálie, které poškozují pěnu.</li>'
          '<li>Zvonek občas zkontrolujte, protože se v zimě může zadřít.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii se objevují značky {B(("shimano", "Shimano"), ("force", "Force"), ("max1", "Max1"), ("specialized", "Specialized"), ("author", "Author"), ("ritchey", "Ritchey"), ("rockbros", "RockBros"), ("craft", "Craft"), ("sram", "SRAM"), ("race-face", "Race Face"), ("kilpi", "Kilpi"))}. Sortiment je široký, od drobných doplňků po technicky náročné součástky. Při srovnání cen se řiďte konkrétními parametry produktu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Jízda za šera bez světel a odrazek.</li>'
          '<li>Helma volná nebo posunutá na zátylek.</li>'
          '<li>Brýle bez UV filtru, které oko zbytečně namáhají.</li>'
          '<li>Držák lahve upevněný jen na jednom šroubku.</li>'
          '<li>Chrániče o číslo větší, které se sesunou.</li>'
          '<li>Kupování příslušenství bez ověření průměru řídítek.</li></ul>',
    faq=[('Co musím mít na kole povinně?', 'Funkční brzdy, odrazky a za snížené viditelnosti světla vpředu i vzadu. Zvonek je běžná součást výbavy a pro děti do 18 let platí povinnost helmy. Aktuální znění ověřte v předpisech.'),
         ('Jaké zorníky vybrat do brýlí?', 'Tmavé do plného slunce, žluté nebo oranžové do šera a lesa, čiré do tmy a deště. Fotochromatické se přizpůsobí světlu a hodí se pro proměnlivé počasí.'),
         ('Jak vybrat držák na láhev?', 'Podle místa na rámu a velikosti láhve. Držák musí láhev pevně držet i při otřesech a mít šroubky vhodné pro váš rám.'),
         ('Hodí se zrcátko na kole?', 'Ve městě ano, protože pomáhá hlídat provoz za zády. Vybírejte stabilní a nezkreslující, a ověřte, že se dá upevnit na vaše řídítka.'),
         ('Jaký průměr řídítek mají kola?', 'Rovná řídítka mívají kolem 22,2 mm, silniční mají odlišný profil. Přesně změřte, než koupíte zvonek, držák nebo zrcátko.'),
         ('Kdy se vyplatí kupovat chrániče?', 'Při enduru, downhillu a jízdě v bikeparku, a také pro děti, které se učí jezdit. V městském provozu stačí helma a rukavice.'),
         ('Mohu telefon při jízdě upevnit na řídítka?', 'Ano, pokud držák pevně drží a zajistí telefon proti vibracím. Na hrubém povrchu je lepší cyklopočítač.'),
         ('Jak vyčistit cyklistickou láhev?', 'Vypláchněte vlažnou vodou s trochou jedlé sody nebo jemného čisticího prostředku, vyčistěte ventil a nechte vyschnout otevřenou.'),
         ('Jak vybrat dětskou helmu?', 'Podle obvodu hlavy a s nastavitelným páskem. Helma musí sedět rovně na čele, nesmí se hýbat a pásek se zapíná pod bradou tak, aby se vešel prst.'),
         ('Musím měnit helmu po pádu?', 'Ano, pokud byl náraz silný. Pěna absorbuje náraz jen jednou a po pádu už nemusí chránit, i když zvenku není poškozená.')],
)
