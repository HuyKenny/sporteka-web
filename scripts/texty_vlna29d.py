"""sporteka.cz — wave 29d (16. 11. 2026): long texts for boxerky, kalhotky, pennyboardy, basketbalove-kose.
General true facts only, no prices, no product counts. Basketball: rim height 305 cm, inner rim diameter 45 cm and
backboard 180 x 105 cm per FIBA; mini-basketball 260 cm for under-11s per the FIBA mini-basketball rules.
Penny Skateboards: Australian brand founded in 2010 by Ben Mackay; Penny wheels 59 mm / 83A.
Brands with an indexed page (znacky.json): icebreaker, smartwool, sensor, craft, progress, calvin-klein, insportline;
other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ boxerky
NEW['boxerky'] = dict(long=True,
    title='Boxerky a trenky: pánské sportovní, merino i bavlněné',
    desc='Pánské boxerky a trenky na sport i každý den: funkční, merino a bavlněné, s delší nohavičkou i slipy. Materiály, švy, velikost a nabídky obchodů.',
    intro='<p>Boxerky jsou dnes nejběžnějším typem pánského spodního prádla. Přiléhají k tělu, drží na místě a mají krátkou nohavičku, která na rozdíl od slipů kryje i horní část stehen. Na sport se vyplatí jiné boxerky než do kanceláře: funkční z polyesteru nebo polyamidu odvádějí pot a rychle schnou, merino vlna hřeje i ve vlhku a nezačne tak rychle zapáchat, bavlna je příjemná na běžné nošení, ale pot drží. Pod pojmem trenky si někdo představí právě boxerky, jiný volné látkové trenýrky. V kategorii najdete obojí a k tomu slipy, a to v pánských velikostech od běžných po větší. Rozhodnout se můžete podle sportu, podle materiálu i podle toho, jak dlouhou nohavičku máte rádi.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých obchodů a objednávku dokončíte u prodejce. Porovnáte tu boxerky ' + B(('icebreaker', 'Icebreaker'), ('smartwool', 'Smartwool'), ('sensor', 'Sensor'), ('craft', 'Craft'), ('progress', 'Progress')) + ' i oblíbené trenky ' + B(('calvin-klein', 'Calvin Klein')) + '. Nadřazená kategorie je <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>.</p>',
    guide='<h2>Boxerky, trenky a slipy</h2>'
          '<p>Názvy se v češtině používají volně, a tak je dobré vědět, co přesně hledáte. Boxerky jsou úpletové, pružné a přiléhavé, s nohavičkou různé délky. Volné trenýrky se šijí z tkaniny, mají gumu v pase a nohavice volně splývají; nosí se hlavně doma a na spaní, na sport se nehodí, protože se shrnují a odírají. Slipy nemají nohavičku vůbec a končí v tříslech. Pro sport jsou nejpraktičtější přiléhavé boxerky, které nic neshrnou a nikde nedřou.</p>'
          + T(['Střih', 'Jak vypadá', 'Kdy se hodí'], [
              ['krátké boxerky', 'nohavička jen pár centimetrů pod rozkrok', 'každodenní nošení, fitness, pod džíny'],
              ['boxerky s delší nohavičkou', 'nohavička do poloviny stehna', 'běh, kolo, turistika, kde se stehna o sebe třou'],
              ['slipy', 'bez nohavičky, vykrojené u třísel', 'kdo nemá rád látku na stehnech, pod plavky'],
              ['volné trenýrky', 'tkanina, volné nohavice, guma v pase', 'doma, na spaní, pro volnost']]) +
          '<h2>Materiály: syntetika, merino, bavlna</h2>'
          '<h3>Funkční syntetika</h3>'
          '<p>Polyester a polyamid s příměsí elastanu jsou základem většiny sportovních boxerek. Vlákno samo vodu skoro nesaje, takže pot přejde na povrch látky a odpaří se. Boxerky po tréninku rychle schnou, drží tvar a vydrží hodně praní. Nevýhodou je, že syntetika časem začne zapáchat a pach se z ní hůř pere. Výrobci proto přidávají úpravy s ionty stříbra nebo jiné antibakteriální povrchy. Funkční boxerky jsou dobrá volba na posilovnu, běh, kolo a míčové sporty, kde se člověk hodně potí a chce suchý pocit.</p>'
          '<h3>Merino vlna</h3>'
          '<p>Merino je jemná ovčí vlna, která neškrábe a hřeje i ve chvíli, kdy je vlhká. Hlavně ale nezačne zapáchat tak rychle jako syntetika, a proto ji milují turisté, cestovatelé a skialpinisté, kteří spodní prádlo nemají kde vyprat. Čisté merino je méně odolné a pomaleji schne, a tak se do boxerek často přidává polyamid nebo se vlna obtáčí kolem syntetického jádra. Merino boxerky jsou příjemné i v létě, protože vlna reguluje teplotu, jen se jim nesmí dávat vysoká teplota při praní. Další merino oblečení najdete v kategorii <a href="/merino-pradlo/">merino prádlo</a>.</p>'
          '<h3>Bavlna a směsi</h3>'
          '<p>Bavlna je měkká, příjemná na kůži a vhodná na celodenní nošení v klidu. Pot ale nasaje a dlouho drží, takže na sport, kde se člověk zpotí a pak zchladne, není ideální. Většina běžných módních boxerek, třeba známé trenky s logem na gumě, se šije z bavlny s elastanem nebo z mikromodalu, který je na dotek ještě jemnější než bavlna. Na běžné nošení jsou to pohodlné boxerky, na delší výkon je ale doplňte funkčními.</p>'
          + T(['Materiál', 'Výhody', 'Na co si dát pozor'], [
              ['polyester, polyamid', 'rychle schne, odolný, drží tvar', 'časem může zapáchat'],
              ['merino vlna', 'hřeje ve vlhku, pomalu zapáchá, příjemná', 'jemnější, pomaleji schne, šetrné praní'],
              ['bavlna', 'měkká, příjemná na každý den', 'drží pot, na sport se nehodí'],
              ['mikromodal, viskóza', 'velmi jemné na dotek', 'méně odolné vůči tření']]) +
          '<h2>Pas a guma</h2>'
          '<p>Guma v pase rozhoduje o tom, jestli boxerky při běhu nebo dřepu sjíždějí. Sportovní modely mají širší a měkčí gumu, která se neroluje a nezařezává do boků, často je z vnitřní strany potažená látkou. Módní boxerky mívají výraznou gumu s logem, která je vidět nad kalhotami; na trénink je příjemnější hladká guma bez tlustých okrajů. U merino boxerek bývá guma užší a jemnější, aby nezvyšovala objem pod dalšími vrstvami. Kdo nosí batoh s bederním pásem, ocení plochou gumu bez švu vzadu, který by pod pásem tlačil.</p>'
          '<h2>Tvarovaná přední část</h2>'
          '<p>Mnoho sportovních boxerek má vpředu anatomicky tvarovaný díl, kterému výrobci říkají kapsa nebo pouch. Drží vše na místě, nic se nemačká a při běhu nebo na kole se omezí tření. Některé modely mají kapsu ze síťoviny pro lepší větrání, jiné ji kombinují s klasickým rozparkem. Na sport je praktičtější varianta bez rozparku, protože má méně švů a lépe drží tvar.</p>'
          '<h2>Švy a odírání</h2>'
          '<p>Na dlouhém běhu nebo na kole rozhoduje o pohodlí každý šev. Sportovní boxerky mají ploché švy typu flatlock, které neleží jeden na druhém a netlačí do kůže. Nejjemnější jsou bezešvé modely pletené vcelku na kruhovém stroji, kde švy skoro nejsou. Proti odírání vnitřních stran stehen pomáhá delší nohavička, která se neshrnuje, a protiskluzový lem nebo silikonový pruh na konci nohavičky. Pod cyklistické kraťasy s vložkou se spodní prádlo naopak nenosí vůbec, protože vložka je určená na holou kůži a šev boxerek by tlačil.</p>'
          '<h2>Boxerky podle sportu</h2>'
          '<ul><li><strong>Běh:</strong> lehké funkční boxerky s delší nohavičkou a plochými švy, které nedřou ani po desítkách kilometrů.</li>'
          '<li><strong>Posilovna a kondiční trénink:</strong> pružné boxerky, které nepovolí při dřepu a výpadu.</li>'
          '<li><strong>Turistika a cestování:</strong> merino, které vydrží několik dní a večer se dá rychle přeprat.</li>'
          '<li><strong>Zimní sporty:</strong> merino nebo teplejší syntetika jako součást vrstvení, podobně jako <a href="/termopradlo/">termoprádlo</a>.</li>'
          '<li><strong>Míčové sporty:</strong> syntetické boxerky, které rychle schnou mezi tréninkem a zápasem.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Velikost boxerek se určuje podle obvodu pasu, u některých výrobců také podle obvodu boků. Změřte se krejčovským metrem v místě, kde budete mít gumu, a porovnejte číslo s tabulkou konkrétní značky. Sportovní boxerky by měly sedět těsně, ale nesmí škrtit v pase ani v nohavičkách. Příliš volné se při pohybu shrnují a odírají, příliš malé tlačí a zařezávají se. Merino se po prvních praních mírně uvolní, syntetika drží tvar. Pokud jste mezi velikostmi, podívejte se na doporučení výrobce, některé značky střihají úžeji.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Funkční prádlo perte podle štítku, obvykle na 30 až 40 °C, a bez aviváže. Aviváž zanese vlákna a látka pak hůř odvádí pot. Merino perte na vlnu nebo ručně ve vlažné vodě s prostředkem na vlnu a nesušte ho v sušičce, ve které by se mohlo srazit. Boxerky schnou nejlépe rozložené na vzduchu. Když funkční prádlo začne trvale zapáchat, pomůže delší namočení v prostředku na sportovní oblečení, a pokud nepomůže ani to, je čas na nové.</p>'
          '<h2>Boxerky na každý den a značkové trenky</h2>'
          '<p>Vedle čistě sportovního prádla se v kategorii prodávají i módní boxerky známých značek, často v balení po dvou nebo třech kusech. Šijí se hlavně z bavlny s elastanem nebo z mikromodalu a jsou pohodlné do práce, na cesty i na spaní. Na sport se dají použít na krátký a lehčí trénink, třeba na procházku nebo jógu. Na dlouhý běh nebo celodenní túru je ale doplňte funkčními nebo merino boxerkami, které si s potem poradí lépe.</p>'
          '<h2>Kolik párů mít</h2>'
          '<p>Na sport stačí několik párů funkčních boxerek, které se po tréninku vyperou a do druhého dne uschnou. Na vícedenní túru nebo cestu s malým zavazadlem se osvědčuje kombinace dvou až tří merino párů, které se dají nosit déle a večer přeprat. Na každý den pak stačí bavlněné nebo modalové boxerky, které jsou příjemné na dlouhé sezení.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu uvidíte nabídky více obchodů a dostupné velikosti a nákup dokončíte v e-shopu. Nejdřív si vyberte materiál podle toho, na co boxerky budete nosit, potom střih a velikost podle tabulky výrobce. K boxerkám se hodí <a href="/sportovni-ponozky/">sportovní ponožky</a> a pro ženy je tu kategorie <a href="/kalhotky/">sportovní kalhotky</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi boxerkami a trenkami?', 'Boxerky jsou přiléhavé a pružné, s krátkou nohavičkou. Trenky nebo trenýrky jsou volné, z tkaniny a s gumou v pase. V běžné řeči se ale slovem trenky často označují i boxerky.'),
        ('Jaké boxerky na běh?', 'Funkční z polyesteru nebo polyamidu s elastanem, s delší nohavičkou a plochými švy. Rychle schnou, nepřilepí se na tělo a delší nohavička brání odírání vnitřních stran stehen i na dlouhém běhu.'),
        ('Jsou merino boxerky vhodné i v létě?', 'Ano. Tenké merino reguluje teplotu, odvádí vlhkost a nezačne rychle zapáchat, takže je oblíbené i na letní cesty. V horku ale schne pomaleji než syntetika, a tak záleží na tom, co upřednostníte. Hodí se lehčí gramáž látky.'),
        ('Proč nenosit bavlněné boxerky na sport?', 'Bavlna nasaje pot a dlouho ho drží. Mokrá látka studí, těžkne a víc odírá. Na každý den je bavlna příjemná, na sport jsou lepší funkční nebo merino boxerky.'),
        ('Jak vybrat velikost boxerek?', 'Změřte obvod pasu v místě, kde bude guma, a porovnejte ho s tabulkou výrobce. Sportovní boxerky mají sedět těsně, ale neškrtit v pase ani v nohavičkách. Když jste mezi velikostmi, řiďte se doporučením značky.'),
        ('Nosí se boxerky pod cyklistické kraťasy?', 'Pod kraťasy s cyklistickou vložkou ne. Vložka je určená na holou kůži a švy spodního prádla by tlačily a odíraly. Pod volné kraťasy bez vložky se naopak hodí funkční boxerky.'),
        ('Jak prát merino boxerky?', 'Na program pro vlnu nebo ručně ve vlažné vodě s prostředkem na vlnu, bez aviváže. Nesušte je v sušičce, ale volně na vzduchu. Vlna nemusí do pračky po každém nošení, často stačí vyvětrat.'),
    ])

# ------------------------------------------------------------------ kalhotky
NEW['kalhotky'] = dict(long=True,
    title='Kalhotky sportovní a merino: hipster, bikini, bezešvé',
    desc='Dámské sportovní kalhotky z funkčních materiálů a merina: hipster, bikini, bezešvé i boxerkové střihy. Co nosit na běh, jógu a hory a jak je prát.',
    intro='<p>Sportovní kalhotky se od běžného spodního prádla liší hlavně materiálem a zpracováním. Šijí se z funkčních vláken nebo z merino vlny, které odvádějí pot a rychle schnou, a mají ploché švy nebo jsou pletené úplně bez švů. Pod přiléhavými legínami se pak nerýsují, nikde neškrtí a nezačnou dřít ani po hodině běhu. Vybírat můžete z několika střihů, od klasického bikini přes hipster s širším bokem až po dámské boxerky s krátkou nohavičkou. Každý se hodí na trochu jiný sport a jinou postavu, a tak se vyplatí vědět, v čem se liší. Stejně důležitý je materiál: na intenzivní trénink se hodí syntetika, na hory a dlouhé dny venku merino.</p>'
          '<p>Na Sportece vidíte nabídky českých e-shopů pohromadě a objednávku dokončíte přímo u prodejce. Najdete tu kalhotky ' + B(('sensor', 'Sensor'), ('icebreaker', 'Icebreaker'), ('craft', 'Craft'), ('smartwool', 'Smartwool')) + ' a dalších značek, jednotlivě i v balení po více kusech. Nadřazená kategorie je <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>, k nim patří <a href="/sportovni-podprsenky/">sportovní podprsenky</a>.</p>',
    guide='<h2>Střihy sportovních kalhotek</h2>'
          + T(['Střih', 'Jak sedí', 'Na co se hodí'], [
              ['bikini (klasické)', 'středně vysoký pas, užší bok', 'univerzální, běžné nošení i lehký sport'],
              ['hipster', 'nižší pas, širší boční díl přes boky', 'běh, jóga, pod legíny bez zařezávání'],
              ['vysoký pas', 'guma nad pupíkem nebo u něj', 'pod legíny s vysokým pasem, pocit opory'],
              ['brazilky', 'vyšší výkroj na nohou, menší zadní díl', 'kdo nechce látku pod hýžděmi'],
              ['tanga', 'minimum látky vzadu', 'pod velmi přiléhavé oblečení, ne každému sedí při sportu'],
              ['dámské boxerky', 'krátká nohavička', 'běh a turistika, kde se stehna o sebe třou']]) +
          '<p>Nejvíc univerzální je pro sport hipster, protože širší boční díl rozloží tlak gumy a kalhotky nesjíždějí. Dámské boxerky ocení běžkyně a turistky, které trápí odírání vnitřních stran stehen. Tanga a brazilky volí ženy, kterým vadí, když se látka pod legínami shrnuje. Žádný střih není správně pro všechny, rozhoduje postava a pocit.</p>'
          '<h2>Materiály</h2>'
          '<h3>Funkční syntetika</h3>'
          '<p>Polyamid a polyester s elastanem tvoří většinu sportovních kalhotek. Jsou lehké, pružné, rychle schnou a drží tvar i po mnoha praních. Polyamid je na dotek jemnější, polyester bývá odolnější. Na intenzivní trénink, kde se hodně potíte, jsou syntetické kalhotky nejpraktičtější, jen je po tréninku vyperte, protože pach se v nich drží víc než v přírodních vláknech.</p>'
          '<h3>Merino</h3>'
          '<p>Merino kalhotky jsou jemné, neškrábou a mají přirozenou schopnost bránit vzniku zápachu. Hřejí i ve vlhku, takže se hodí na hory, skialpy, běžky a vícedenní túry. Výrobci je obvykle kombinují s polyamidem, který zvyšuje pevnost, a s elastanem, aby kalhotky držely tvar. Čisté merino je méně odolné vůči tření a schne pomaleji než syntetika. Další kousky z vlny najdete v kategorii <a href="/merino-pradlo/">merino prádlo</a>.</p>'
          '<h3>Bavlněný klín</h3>'
          '<p>Mnoho kalhotek má v rozkroku vložený bavlněný díl, i když zbytek je ze syntetiky nebo merina. Bavlna je v tomto místě příjemná a prodyšná. Některé sportovní modely mají klín z téhož funkčního materiálu jako celé kalhotky, aby rychle schly. Pokud máte citlivou pokožku, sledujte složení klínu v popisu produktu.</p>'
          '<h2>Pas a guma</h2>'
          '<p>U sportovních kalhotek se guma často nahrazuje lemem pleteným přímo do materiálu nebo měkkou plochou gumou, která nemá ostré okraje. Pod legínami s vysokým pasem se tak nevytvoří viditelná linka a nic se nezařezává do boků. Klasická úzká guma je levnější a drží spolehlivě, při dlouhém sezení na kole nebo při józe ale může tlačit. Pokud vám kalhotky během běhu rolují nebo sjíždějí, zkuste širší pas nebo střih hipster.</p>'
          '<h2>Dámské boxerky</h2>'
          '<p>Dámské boxerky mají krátkou nohavičku, která kryje horní část stehen. Při běhu, turistice a v létě pod sukní nebo šaty brání tomu, aby se stehna o sebe třela a kůže se podrážděla. Šijí se ze syntetiky i z merina, často bezešvé. Pod úzkými legínami nejsou vidět a pod volnými kraťasy fungují jako pohodlná spodní vrstva. Délka nohavičky se liší od pár centimetrů po polovinu stehna, a tak si vyberte podle toho, kde vás tření nejvíc trápí.</p>'
          '<h2>Bezešvé, nebo s plochými švy</h2>'
          '<p>Bezešvé kalhotky se pletou vcelku do tvaru trubice a mají jen minimum švů, třeba v klínu. Pod legínami a přiléhavými šortkami se nerýsují a nic na nich netlačí. Kalhotky s plochými švy flatlock jsou zase přesnější ve střihu a lépe drží tvar. Na jógu, pilates a tanec, kde jsou legíny tenké a postava je hodně vidět, sahají ženy často po bezešvých modelech. Na běh a turistiku fungují dobře oba typy, pokud kalhotky sedí a nic neřeže.</p>'
          '<h2>Kalhotky podle sportu</h2>'
          '<ul><li><strong>Běh:</strong> lehké syntetické kalhotky nebo dámské boxerky s plochými švy, které se nesvezou a nedřou.</li>'
          '<li><strong>Jóga a pilates:</strong> bezešvé kalhotky s nižším nebo vysokým pasem, které se pod <a href="/leginy/">legínami</a> nerýsují ani v hlubokém předklonu.</li>'
          '<li><strong>Hory a zimní sporty:</strong> merino, případně jako součást vrstvení s termoprádlem.</li>'
          '<li><strong>Posilovna:</strong> pružné kalhotky, které nepovolí při dřepu a nesjíždějí při výpadech.</li>'
          '<li><strong>Kolo:</strong> pod cyklistické kraťasy s vložkou se spodní prádlo nenosí, vložka patří na holou kůži.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Kalhotky se značí písmeny od XS po XL a výrobci k nim uvádějí obvod boků, případně i pasu. Změřte se v nejširším místě boků a porovnejte údaj s tabulkou konkrétní značky, protože velikosti se mezi výrobci liší. Sportovní kalhotky mají sedět těsněji než běžné, aby se nesvezly, guma ale nesmí zařezávat. Bezešvé modely jsou pružnější a často pokrývají dvě velikosti najednou, třeba S/M. Merino se po prvních praních mírně povolí.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Funkční kalhotky perte na nízkou teplotu podle štítku a bez aviváže, která zanáší vlákna. Merino patří na program pro vlnu nebo do ruční koupele s prostředkem na vlnu. Jemné kalhotky perte v síťce, aby se nezachytily o háčky podprsenek nebo zipy. Sušte je na vzduchu, sušička elastan oslabuje a guma pak dřív povolí. Spodní prádlo, které nosíte na trénink, je dobré měnit častěji než běžné, protože pot a tření ho opotřebí rychleji.</p>'
          '<h2>Citlivá pokožka</h2>'
          '<p>Pokud máte citlivou kůži, vybírejte kalhotky s měkkým lemem, bez hrubých štítků a s klínem z bavlny nebo jemného funkčního materiálu. Nové kalhotky před prvním nošením vyperte, odstraníte tak zbytky barviv a úprav z výroby. Pomůže také prací prostředek bez parfemace a vynechání aviváže. Merino lidé s citlivou pokožkou obvykle snášejí dobře, protože jeho vlákno je jemné a neškrábe jako běžná vlna. Při podráždění, které nepřestává, se poraďte s lékařem.</p>'
          '<h2>Na hory a vícedenní túry</h2>'
          '<p>Na túru s batohem se osvědčují dva až tři páry merino kalhotek. Dají se nosit déle než syntetické, večer se přeperou v potoce nebo v umyvadle a přes noc na šňůře nebo na batohu většinou uschnou. Lehké jsou i v balení, takže nezatíží zavazadlo. Na skialpy a běžky je dobré je spojit s merino nebo syntetickým termoprádlem, které odvede pot od těla a nenechá vás při pauze prochladnout.</p>'
          '<h2>Kolik párů mít a kdy je vyměnit</h2>'
          '<p>Na pravidelný trénink se vyplatí mít aspoň tři páry sportovních kalhotek, aby vždy jeden byl čistý a suchý. Na hory a cesty počítejte s merino páry, které se dají nosit déle. Kalhotky je čas vyměnit, když guma povolí a začnou sjíždět, když se látka v klínu ztenčí nebo když syntetika trvale zapáchá i po vyprání. Sportovní prádlo se opotřebovává rychleji než běžné, protože ho zatěžuje pot, tření a častější praní.</p>'
          '<h2>Sady a doplňky</h2>'
          '<p>Někteří výrobci vyrábějí kalhotky a sportovní podprsenky v sadách ze stejného materiálu a barvy. Kdo vrství na hory, kombinuje merino kalhotky s merino tričkem nebo <a href="/termopradlo/">termoprádlem</a>. Na koupání ale sportovní kalhotky nepatří, chlor a slaná voda jim neprospívají a na to jsou určené plavky. Při výběru sady si zkontrolujte, že obě části mají stejnou péči při praní, aby se mohly prát spolu a barva zůstala sladěná. Pro partnera nebo do páru se hodí <a href="/boxerky/">boxerky</a> od stejné značky.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>U každého modelu uvidíte nabídky více obchodů a velikosti skladem, objednávku pak dokončíte u prodejce. Nejdřív si vyberte materiál podle sportu, potom střih a velikost podle tabulky výrobce. Vyplatí se mít doma aspoň dva páry na sport, aby jeden mohl schnout, zatímco druhý nosíte.</p>',
    faq=[
        ('Jaké kalhotky na běh?', 'Lehké funkční kalhotky z polyamidu nebo polyesteru s plochými švy, případně dámské boxerky s krátkou nohavičkou, které brání odírání stehen. Měly by sedět těsně, ale nezařezávat, a rychle schnout, aby po doběhu nestudily.'),
        ('Co je střih hipster?', 'Kalhotky s nižším pasem a širším bočním dílem přes boky. Guma rozloží tlak do větší plochy, takže se pod legínami tolik nerýsují a nesjíždějí.'),
        ('Jsou merino kalhotky vhodné na sport?', 'Ano, hlavně na hory, turistiku a zimní sporty. Merino hřeje i ve vlhku, je jemné na kůži a brání vzniku zápachu, takže se hodí i na vícedenní cesty. Při intenzivním tréninku v teple ale schne pomaleji než syntetika.'),
        ('Proč se kalhotky pod legínami rýsují?', 'Obvykle kvůli silné gumě nebo švům na okrajích nohavic. Pomohou bezešvé kalhotky s lemem pleteným do materiálu nebo střih s širším bočním dílem, případně tanga či brazilky. Rýsování také zvýrazní kalhotky, které jsou příliš malé.'),
        ('Jak vybrat velikost sportovních kalhotek?', 'Změřte obvod boků v nejširším místě a porovnejte ho s tabulkou výrobce, protože velikosti se mezi značkami liší. Bezešvé modely jsou pružnější a často pokrývají dvě velikosti, třeba S/M.'),
        ('Nosí se kalhotky pod cyklistické kraťasy?', 'Ne, pokud mají kraťasy cyklistickou vložku. Ta je určená na holou kůži, spodní prádlo by tlačilo a odíralo.'),
        ('Jak prát sportovní kalhotky?', 'Na nízkou teplotu podle štítku, bez aviváže a ideálně v síťce na prádlo, aby se nezachytily o háčky a zipy. Merino na program pro vlnu s prostředkem na vlnu. Sušte je na vzduchu, ne v sušičce, která oslabuje elastan.'),
    ])

# ------------------------------------------------------------------ pennyboardy
NEW['pennyboardy'] = dict(long=True,
    title='Pennyboard: plastový cruiser 22" a 27" pro děti i dospělé',
    desc='Pennyboardy 22" a 27" z plastu na město i pro děti. Velikost desky, tvrdost kol, ložiska, svítící kola a chrániče. Nabídky českých obchodů.',
    intro='<p>Pennyboard je malý skateboard s deskou z pružného plastu, měkkými koly a lehkými hliníkovými podvozky. Vejde se do batohu, váží málo a po hladkém chodníku nebo cyklostezce jede tiše a plynule. Na rozdíl od klasického skateboardu není stavěný na triky ve skateparku, ale na ježdění po městě, cestu do školy a krátké přesuny. Proto si ho oblíbily děti i dospělí, kteří chtějí jen tak jezdit. Název pochází od australské značky Penny Skateboards a dnes se jím označují všechny malé plastové cruisery bez ohledu na výrobce. Vyrábí se v mnoha barvách, s průhlednými deskami i s motivy, a tak se často kupuje i jako dárek.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a nákup dokončíte u vybraného prodejce. Najdete tu pennyboardy Worker, Sulov, Meteor, Tempish a dalších značek. Nadřazenou kategorií jsou <a href="/skateboardy/">skateboardy</a>. Vybírat můžete podle délky desky, barvy, tvrdosti kol i podle toho, jestli chcete svítící kola.</p>',
    guide='<h2>Odkud se pennyboard vzal</h2>'
          '<p>Značku Penny Skateboards založil v roce 2010 v Austrálii Ben Mackay. Inspirací mu byl malý plastový cruiser, na kterém jezdil jako kluk. Malá deska z plastu s výraznými barvami se rychle rozšířila po celém světě a jméno značky zevšeobecnělo. Když dnes v Česku někdo řekne pennyboard, myslí tím jakýkoli plastový cruiser podobné velikosti, ať ho vyrobila Penny, nebo jiná firma.</p>'
          '<h2>Velikost desky: 22, nebo 27 palců</h2>'
          + T(['Délka', 'Přibližně v cm', 'Pro koho'], [
              ['22"', 'asi 56 cm', 'menší děti, jezdci s menší nohou, kdo chce desku do batohu'],
              ['27"', 'asi 69 cm', 'dospělí, větší děti, delší jízdy, víc stability'],
              ['delší plastové cruisery', '29" a více', 'kdo chce ještě klidnější jízdu, deska už se hůř nosí']]) +
          '<p>Kratší deska je hbitější, lépe se s ní zatáčí a pohodlněji se nosí. Na druhou stranu je citlivější na každý pohyb a ve vyšší rychlosti se může rozkmitat. Delší deska poskytne víc místa pro nohy, takže na ní stojíte v pohodlnějším rozkročení a jízda je klidnější. Většina dospělých proto sáhne po 27", velikost 22" zůstává oblíbená u dětí a u těch, kdo desku hlavně nosí s sebou. Penny u velikosti 27" používá název Nickel.</p>'
          '<h2>Plastová deska</h2>'
          '<p>Deska pennyboardu se lisuje z plastu, který je pružný a neláme se tak snadno jako tenká dřevěná deska. Mírně se prohne pod vahou jezdce, což tlumí otřesy, a vydrží i pád ze schodů nebo náraz do obrubníku. Místo protiskluzového papíru, který se lepí na skateboardy, má povrch vylisovaný vzorek, o který se opírá podrážka. Maximální nosnost uvádí výrobce v popisu produktu a je dobré ji respektovat, zvlášť u levnějších desek. Plast je citlivý na velké horko, a tak desku nenechávejte v létě v rozpáleném autě.</p>'
          '<h2>Kola a tvrdost</h2>'
          '<p>Pennyboardy mají široká a měkká kola z polyuretanu o průměru kolem 59 mm. Tvrdost kol se udává na stupnici Shore A: čím nižší číslo, tím měkčí kolo. Originální kola Penny mají tvrdost 83A, což je běžná hodnota pro cruisery. Měkké kolo spolkne drobné nerovnosti, praskliny v chodníku a kamínky, drží na asfaltu a jízda je tichá. Tvrdší kola klasických skateboardů jedou rychleji po hladkém povrchu skateparku, ale na hrubém asfaltu drnčí a snadno se zaseknou o kamínek. Pro jízdu po městě jsou měkčí kola lepší volbou.</p>'
          '<h2>Svítící kola</h2>'
          '<p>Hlavně dětské pennyboardy mívají kola, která se při jízdě rozsvítí. Většinou nepotřebují baterie, protože si proud vyrobí samy otáčením. Vypadají efektně a večer pomáhají, aby dítě bylo vidět. Za plné osvětlení ale nestačí, a pokud se jezdí za šera, přidejte reflexní prvky na oblečení nebo <a href="/reflexni-vesty/">reflexní vestu</a>.</p>'
          '<h2>Ložiska a co znamená ABEC</h2>'
          '<p>V každém kole jsou dvě ložiska. U skateboardů se často uvádí číslo ABEC, které vyjadřuje přesnost výroby ložiska. Vyšší číslo znamená přesnější výrobu, pro rekreační jízdu po městě ale rozdíl mezi střední a vyšší třídou skoro nepoznáte. Důležitější je, aby ložiska byla čistá a suchá. Voda a písek jim škodí nejvíc: ložisko po jízdě přes kaluže zrezaví a začne drhnout. Kdo jezdí hodně, může ložiska časem vyčistit nebo vyměnit, jsou standardního rozměru jako u ostatních skateboardů.</p>'
          '<h2>Podvozky a nastavení</h2>'
          '<p>Podvozky, kterým se říká trucky, spojují desku s koly. U pennyboardů bývají z hliníku a mají gumové silentbloky, které určují, jak snadno deska zatáčí. Utažením matice na hlavním šroubu se deska zpevní a bude stabilnější v rovné jízdě, povolením se snáz zatáčí. Začátečníkům a dětem se hodí spíš pevnější nastavení. Matici ale neutahujte nadoraz, silentbloky by se zdeformovaly. Čas od času zkontrolujte, že všechny šrouby drží a kola se točí volně.</p>'
          '<h2>Údržba</h2>'
          '<p>Pennyboard nepotřebuje skoro žádnou péči, pár drobností ale prodlouží jeho život. Po jízdě ho otřete od prachu a písku, hlavně kolem kol a ložisek. Když kola přestanou volně dobíhat nebo hlučí, ložiska vyndejte, vyčistěte a namažte, případně vyměňte. Ojetá nebo hranatá kola se dají vyměnit za nová stejného průměru. Pravidelně kontrolujte šrouby, které drží podvozky na desce, protože se otřesy povolují. Desku skladujte v suchu a ne na přímém slunci.</p>'
          '<h2>Pennyboard na cesty</h2>'
          '<p>Díky malé velikosti a nízké hmotnosti se pennyboard dá vzít do tramvaje, do školy nebo na výlet. Velikost 22" se vejde do většího batohu, pro 27" se prodávají držáky a popruhy, se kterými ho nesete přes rameno. Při nošení dávejte pozor na špinavá kola, která umažou oblečení. Ve veřejné dopravě desku držte v ruce, aby se nerozjela.</p>'
          '<h2>Pennyboard pro děti</h2>'
          '<p>Malé plastové desky jsou mezi dětmi velmi oblíbené, protože jsou lehké a barevné. Dítě by na nich ale mělo začínat na rovné a hladké ploše bez provozu, ideálně s dospělým poblíž. Krátká deska je citlivá a z kopce rychle nabere rychlost, a brzdit se na ní dá jen nohou o zem. Povinnou výbavou by měla být přilba a chrániče kolen, loktů a zápěstí, které najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>. Pro menší děti, které ještě nemají dobrou rovnováhu, je bezpečnější začít na <a href="/kolobezky/">koloběžce</a>.</p>'
          '<h2>Jak se na pennyboardu jezdí</h2>'
          '<p>Přední nohu postavte přes přední šrouby desky, zadní nohou se odrážejte od země. Když se rozjedete, dejte zadní nohu na zadní část desky a stůjte bokem ke směru jízdy. Zatáčí se přenesením váhy na špičky nebo na paty. Brzdí se nejčastěji tak, že zadní nohu sundáte a podrážkou se jemně opřete o zem. Pennyboard nemá velký nos ani zadní konec jako skateboard, a tak triky typu ollie jsou těžší. Kdo chce jezdit ve skateparku, vybere si spíš klasický skateboard.</p>'
          '<h2>Kde jezdit a kde ne</h2>'
          '<p>Pennyboard se cítí nejlépe na hladkém asfaltu, cyklostezkách a v parcích. Na dlažbě s širokými spárami a na štěrku se kola zastaví a jezdec může přepadnout dopředu. Do deště ani na mokrý povrch se nehodí, protože plast i kola na mokru kloužou a ložiska trpí. Na chodníku mějte ohled na chodce a jeďte pomalu.</p>'
          '<h2>Pennyboard, nebo koloběžka</h2>'
          '<p>Rodiče často váhají mezi pennyboardem a koloběžkou na cestu do školy. Koloběžka má řídítka a brzdu, takže je pro menší děti a pro jízdu mezi lidmi bezpečnější a snáz se na ní učí. Pennyboard je menší a lehčí, vejde se do batohu a jízda na něm víc rozvíjí rovnováhu, ale chce víc cviku a opatrnosti. Pro starší děti a dospělé, kteří už jezdí jistě, je pennyboard zábavnou alternativou, kterou lze nosit všude s sebou.</p>'
          '<h2>Pennyboard, skateboard, nebo longboard</h2>'
          '<ul><li><strong>Pennyboard:</strong> malý, lehký, na krátké přesuny po městě a pro radost z jízdy.</li>'
          '<li><strong>Skateboard:</strong> dřevěná deska s tvrdšími koly, na triky a skatepark.</li>'
          '<li><strong>Longboard:</strong> dlouhá deska s měkkými koly, stabilní jízda na delší vzdálenosti a z kopce.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě pennyboardu se ukážou nabídky více obchodů vedle sebe, objednávku pak dokončíte u zvoleného prodejce. Vyberte velikost desky podle výšky jezdce a toho, jak ji budete používat, a nezapomeňte na přilbu a chrániče. Kdo chce jezdit i na kolečkách jinak, najde vybavení v kategorii <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>.</p>',
    faq=[
        ('Jakou velikost pennyboardu vybrat?', 'Dospělým a větším dětem se obvykle hodí 27", který je stabilnější a nabídne víc místa pro nohy. Velikost 22" je vhodná pro menší děti a pro ty, kdo desku často nosí v batohu.'),
        ('Od kolika let je pennyboard vhodný?', 'Výrobci obvykle uvádějí doporučený věk a nosnost v popisu produktu. Záleží hlavně na rovnováze a obratnosti dítěte. Na začátku by mělo jezdit na rovné a hladké ploše bez provozu, s přilbou a chrániči a ideálně pod dohledem dospělého.'),
        ('Co znamená tvrdost kol 83A?', 'Je to tvrdost polyuretanu na stupnici Shore A. Nižší číslo znamená měkčí kolo, které lépe tlumí nerovnosti a drží na asfaltu. Hodnota 83A je typická pro cruisery a mají ji i originální kola Penny.'),
        ('Je pennyboard vhodný na triky?', 'Jen omezeně. Krátká plastová deska bez výrazného nosu a zadního konce se hodí hlavně na jízdu po městě a jednoduché manévry. Na ollie, skoky a triky ve skateparku je lepší klasický dřevěný skateboard.'),
        ('Jak se na pennyboardu brzdí?', 'Nejčastěji nohou: zadní nohu sundáte z desky a podrážkou se jemně opřete o zem. Brzdění je dobré nacvičit v pomalé jízdě na rovině dřív, než vyjedete na mírný kopec. Pennyboard brzdu nemá, a tak se prudkým klesáním vyhněte.'),
        ('Potřebují svítící kola baterie?', 'Většinou ne, protože si proud vyrobí otáčením při jízdě. Svítí jen v pohybu a plné osvětlení nenahradí, za šera přidejte reflexní prvky.'),
        ('Můžu s pennyboardem jezdit v dešti?', 'Nedoporučuje se. Kola i deska na mokru kloužou a voda poškozuje ložiska, která pak rezaví a drhnou. Po jízdě přes kaluž desku osušte.'),
    ])

# ------------------------------------------------------------------ basketbalove-kose
NEW['basketbalove-kose'] = dict(long=True,
    title='Basketbalový koš: na zeď, přenosný stojan i mini koš',
    desc='Basketbalové koše na zeď, přenosné stojany s podstavcem na vodu či písek, zabetonované koše i mini koše na dveře. Výška, deska, obroučka a montáž.',
    intro='<p>Basketbalový koš na zahradu nebo do dvora umožní trénovat střelbu kdykoli, bez cesty do haly. Na výběr jsou koše s deskou pro připevnění na zeď nebo garáž, přenosné stojany s podstavcem, který se plní vodou nebo pískem, pevné stojany zabetonované do země a mini koše na dveře pro děti i dospělé fanoušky. Liší se stabilitou, velikostí desky, materiálem i tím, jestli lze nastavit výšku. Na volném hřišti je koš pevně ukotvený, doma záleží na tom, kolik máte místa a jak moc se bude hrát. Než koš objednáte, změřte si plochu a zjistěte, jestli máte pevnou zeď, nebo je lepší samostatný stojan. Myslete i na to, kdo bude hrát: malé děti potřebují koš níž, dospělí plnou výšku.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a nákup dokončíte na webu prodejce. Najdete tu koše Spalding, Wilson, Nils, Spartan, ' + B(('insportline', 'inSPORTline')) + ' nebo My Hood, od dětských stojanů po pevné koše na celoroční hru venku. Další vybavení je v kategorii <a href="/basketbal/">basketbal</a>.</p>',
    guide='<h2>Typy basketbalových košů</h2>'
          + T(['Typ', 'Jak je postavený', 'Kdy se hodí'], [
              ['koš na zeď', 'deska s obroučkou na konzole přišroubované ke zdi', 'garáž, dům, dvůr s pevnou zdí'],
              ['přenosný stojan', 'tyč na podstavci plněném vodou nebo pískem, s kolečky', 'zahrada, příjezdová cesta, když chcete koš přesunout'],
              ['zabetonovaný stojan', 'ocelová tyč ukotvená do betonového základu', 'nejvyšší stabilita, trvalé místo'],
              ['mini koš', 'malá deska a obroučka na dveře nebo zeď', 'děti, pokoj, kancelář, zábava s pěnovým míčem'],
              ['samotná obroučka', 'obroučka se síťkou bez desky', 'výměna na hřišti, montáž na vlastní desku']]) +
          '<h2>Rozměry podle pravidel</h2>'
          '<p>Podle pravidel FIBA je horní okraj obroučky ve výšce 305 cm nad podlahou, tedy deset stop. Vnitřní průměr obroučky je 45 cm a míč velikosti 7 má průměr kolem 24 cm, takže do koše se vejde s rezervou. Oficiální deska na soutěžní basketbal měří 180 × 105 cm. Domácí koše mívají desku menší, obvykle o šířce jednoho metru až něco přes metr, a pro hru na zahradě to stačí. Pro děti do jedenácti let pravidla minibasketbalu FIBA počítají s košem ve výšce 260 cm a s menším míčem. Proto se vyplatí stojan s nastavitelnou výškou, který s dítětem poroste.</p>'
          + T(['Údaj', 'Hodnota', 'Poznámka'], [
              ['výška obroučky', '305 cm', 'pravidla FIBA, horní okraj obroučky'],
              ['vnitřní průměr obroučky', '45 cm', 'pravidla FIBA'],
              ['deska', '180 × 105 cm', 'soutěžní rozměr, domácí desky bývají menší'],
              ['minibasketbal', '260 cm', 'děti do 11 let podle pravidel FIBA pro minibasketbal']]) +
          '<h2>Materiál desky</h2>'
          '<ul><li><strong>Polyetylen (plast):</strong> lehká a odolná deska, typická pro dětské a levnější stojany. Míč se od ní odráží méně živě.</li>'
          '<li><strong>Polykarbonát:</strong> průhledný nebo kouřový plast, velmi odolný proti nárazu a mrazu. Častý u přenosných a zahradních košů.</li>'
          '<li><strong>Akrylát:</strong> průhledný, na pohled podobný sklu a s lepším odrazem než polykarbonát. Je ale křehčí a snáz se poškrábe.</li>'
          '<li><strong>Tvrzené sklo:</strong> nejlepší odraz, stejný jako v hale. Je těžké a používá se u zabetonovaných stojanů a na hřištích.</li></ul>'
          '<p>Pro rodinu, kde se hraje pro radost, stačí polyetylen nebo polykarbonát. Kdo bere basketbal vážně a chce trénovat střelbu s odrazem od desky, ocení akrylát nebo sklo.</p>'
          '<h2>Obroučka a síťka</h2>'
          '<p>Pevná obroučka je jednoduchá a vydrží běžnou hru. Pokud se ale na koši bude smečovat, potřebujete obroučku s pružným uchycením, která po zavěšení povolí a vrátí se zpět. Ta šetří desku i konstrukci. Síťky se prodávají z nylonu, které jsou měkké a tiché, a venkovní řetízkové síťky, které vydrží déšť a slunce, ale jsou hlučné. Síťku lze snadno vyměnit, když se roztrhá.</p>'
          '<h2>Přenosný stojan: voda, nebo písek</h2>'
          '<p>Podstavec přenosného stojanu se plní vodou nebo pískem, aby koš při hře nespadl. Voda se nalije snadno a dá se i vypustit, když koš potřebujete přesunout. Písek je těžší, takže stojan drží pevněji, ale plnění je pracnější a vysypat ho jde těžko. V zimě voda v podstavci zamrzne a může plast roztrhnout, proto ji na zimu vypusťte nebo použijte písek. Výrobci uvádějí, kolik litrů podstavec pojme a čím ho plnit, a těchto údajů se držte. Na stojan se nikdy nezavěšujte, přenosná konstrukce na to není stavěná.</p>'
          '<h2>Koš na zeď a montáž</h2>'
          '<p>Koš na zeď zabere nejméně místa a je stabilní, pokud je zeď dost pevná. Kotví se do zdiva nebo betonu hmoždinkami a šrouby, které odpovídají materiálu zdi; do sádrokartonu nebo zateplené fasády bez pevného podkladu se nemontuje. Spodní hrana desky by měla být od zdi dostatečně daleko, aby hráč pod košem nenarazil do zdi. Konzola s větším vyložením proto pomáhá. Výšku obroučky změřte od země po horní okraj a ověřte vodováhou, že deska visí rovně.</p>'
          '<h2>Zabetonovaný stojan</h2>'
          '<p>Nejpevnější řešení jsou stojany, jejichž tyč se zabetonuje do země nebo přišroubuje k betonovému základu. Mají větší desku, často skleněnou nebo akrylátovou, a některé umožňují měnit výšku obroučky klikou. Hodí se na rodinné hřiště, kde koš zůstane natrvalo. Před montáží zjistěte, kudy vedou podzemní kabely a potrubí, a dodržte rozměry základu, které udává výrobce.</p>'
          '<h2>Koš pro děti</h2>'
          '<p>Děti potřebují koš níž, aby střelba nebyla jen házením míče nahoru. Dětské stojany mají často nastavitelnou tyč, se kterou se obroučka postupně zvedá, a menší a lehčí podstavec. Pro malé hráče se hodí i lehčí míč menší velikosti, kterým trefí koš bez přemáhání. Stojan ale musí být stabilní i tak, protože děti se rády na obroučku zavěšují. Proto ho naplňte podle návodu a pravidelně kontrolujte, jestli se podstavec nenaklání.</p>'
          '<h2>Basketbal 3×3 na dvoře</h2>'
          '<p>Na jeden koš se dá hrát basketbal 3×3, který má vlastní pravidla FIBA a je olympijským sportem. Hraje se na polovině hřiště s jedním košem ve stejné výšce jako klasický basketbal. Pro domácí hru stačí rovná plocha před košem a vyznačená čára, za kterou se střílí. Je to dobrý způsob, jak na zahradě zahrát zápas i s menší partou kamarádů.</p>'
          '<h2>Bezpečnost</h2>'
          '<ul><li>Tyč stojanu a spodní hranu desky můžete obalit polstrováním, které ztlumí náraz při hře pod košem.</li>'
          '<li>Na obroučku přenosného stojanu se nezavěšujte a nedovolte to ani dětem.</li>'
          '<li>Při silném větru stojan zajistěte podle návodu výrobce, velká deska funguje jako plachta.</li>'
          '<li>Po zimě zkontrolujte šrouby, svary a podstavec, jestli nepraskl.</li>'
          '<li>Kolečka přenosného stojanu po přesunu zajistěte, aby se koš při hře nepohyboval.</li></ul>'
          '<h2>Mini koše</h2>'
          '<p>Mini koš na dveře nebo zeď s malým míčem je zábava pro děti v pokoji, ale i pro dospělé v kanceláři nebo v herně. Uchycuje se háky přes dveře nebo šrouby, některé modely mají pružnou obroučku a sadu s pěnovým míčkem, který nic nerozbije. Na trénink skutečné střelby se nehodí, k zábavě a hře o body jsou ale ideální.</p>'
          '<h2>Péče a zima</h2>'
          '<p>Venkovní koš je celý rok na slunci, v dešti a mrazu. Plastové desky a podstavce časem na slunci blednou a křehnou, kovové části mohou korodovat v místech, kde je poškozená barva. Jednou za sezonu proto projděte šrouby a spoje, poškrábaná místa na kovu přetřete a roztrhanou síťku vyměňte. Přenosný stojan je dobré na zimu přesunout do závětří nebo ho při dlouhé nečinnosti sklopit podle návodu. Desku čistěte jen vodou a měkkou houbou, abrazivní prostředky by průhledný plast zmatnily.</p>'
          '<h2>Kam koš umístit</h2>'
          '<p>Plocha pod košem by měla být rovná a pevná, ideálně asfalt, beton nebo zámková dlažba, aby míč dobře skákal. Na trávě se driblovat nedá. Počítejte s volným místem pro střelbu z různých vzdáleností a s tím, že míč občas odskočí do záhonu nebo k sousedům. Koš nestavte pod elektrické vedení a myslete na hluk, který odrazy míče dělají. Desku je dobré natočit tak, aby hráčům při odpolední hře nesvítilo slunce přímo do očí. Pokud koš stojí u příjezdové cesty, nechte kolem něj dost místa, aby se dalo bezpečně zaparkovat i hrát, a hru přerušte, když přijíždí auto.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>U každého koše vidíte nabídky různých e-shopů pohromadě a objednávku pak dokončíte u prodejce, kterého si vyberete. Nejdřív si ujasněte, kde bude koš stát, potom vyberte typ, velikost a materiál desky. K novému koši se hodí <a href="/basketbalove-mice/">basketbalový míč</a> vhodný na venkovní povrch a <a href="/basketbalova-obuv/">basketbalová obuv</a>, další venkovní zábava je v kategorii <a href="/hry-na-zahradu/">hry na zahradu</a>.</p>',
    faq=[
        ('V jaké výšce je basketbalový koš?', 'Podle pravidel FIBA je horní okraj obroučky 305 cm nad zemí, tedy deset stop. Pro děti do jedenácti let počítají pravidla minibasketbalu FIBA s výškou 260 cm. Výšku měřte od země po horní okraj obroučky.'),
        ('Jaký je průměr basketbalové obroučky?', 'Vnitřní průměr obroučky je podle pravidel FIBA 45 cm. Míč velikosti 7 se do ní vejde s rezervou.'),
        ('Čím naplnit podstavec přenosného koše?', 'Vodou nebo pískem podle návodu výrobce. Písek je těžší, nezamrzne a stojan drží pevněji, vodu lze zase snadno vypustit při přesunu. Na zimu vodu vypusťte, aby mráz neroztrhl plastový podstavec.'),
        ('Jaký materiál desky vybrat?', 'Na rodinnou hru stačí polyetylen nebo polykarbonát, který je odolný proti nárazům i mrazu. Akrylát a tvrzené sklo mají lepší odraz od desky, jsou ale těžší a hodí se pro náročnější hráče a pevné stojany.'),
        ('Dá se nastavit výška koše?', 'U mnoha přenosných a zabetonovaných stojanů ano, obvykle posuvnou tyčí nebo klikou. Nastavitelná výška se hodí pro rodiny s dětmi, které začínají níž a postupně přejdou na 305 cm.'),
        ('Můžu na koši smečovat?', 'Jen pokud má koš pevnou konstrukci, ideálně zabetonovanou, a obroučku s pružným uchycením určenou ke smečím. Na přenosný stojan a běžnou obroučku se nezavěšujte, mohl by se převrátit nebo prasknout deska.'),
        ('Jaký míč ke koši na zahradu?', 'Míč určený na venkovní povrch, který vydrží asfalt a beton; halový kožený míč by se venku rychle odřel. Dospělí muži hrají s velikostí 7, ženy se šestkou a menší děti s pětkou.'),
    ])
