"""sporteka.cz — facet landing texts wave 116: damska-funkcni-mikina, ccm-hokejky, sportovni-podprsenka-nike, plavky-adidas.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ damska-funkcni-mikina
NEW['damska-funkcni-mikina'] = dict(
    title='Dámská funkční mikina: střih, vrstva a výběr podle sportu',
    desc='Dámská funkční mikina má užší ramena, delší rukávy a kratší tělo. Jak vybrat velikost, tloušťku a zip pro běh, túru i lyže a porovnat obchody.',
    intro='<p>Dámská funkční mikina vypadá na ramínku podobně jako pánská, ale na těle se chová jinak. Má užší ramena, delší rukáv vzhledem k šířce, tvarovaný pas a boky, na které nemá žádný zbytečný přebytek látky. Kdo si vezme pánský kus o číslo menší, často narazí na krátký trup nebo na rukáv, který nesedí v loktech. '
          'Na této stránce jsou mikiny z kategorie <a href="/funkcni-mikiny/">funkční mikiny</a> určené ženám, od lehkých běžeckých vrstev přes tréninkové kousky až po teplejší mikiny na hory. Průvodce vysvětluje, v čem je ženský střih jiný, jak zvolit tloušťku podle činnosti, kdy sáhnout po zipu až k bradě a kdy raději po kulatém výstřihu, a jak mikinu vrstvit se <a href="/sportovni-podprsenky/">sportovní podprsenkou</a> a <a href="/leginy/">legínami</a>. Zajímavá bude i volba mezi syntetikou a <a href="/merino-mikiny/">merinem</a>.</p>',
    guide='<h2>V čem je ženský střih opravdu jiný</h2>'
          '<p>Rozdíl mezi dámskou a pánskou funkční mikinou se neomezuje na barvy. Ženská postava má v průměru užší ramena a výraznější proporce v pase a na bocích, a proto výrobci mění samotnou konstrukci kusu. U těsněji střižených funkčních vrstev je to dobře znát: pánská mikina se na menší ženě sbírá v podpaží, visí v pase a rukáv přesahuje přes zápěstí.</p>'
          + T(['Část mikiny', 'Dámská úprava', 'Co z toho máte'], [
              ['Ramena a průramky', 'užší sedlo, vyšší průramek', 'volnější paže, žádné padání ramene'],
              ['Pas a boky', 'mírně tvarovaný střih', 'látka nezkrabatí na břiše a nebrání při předklonu'],
              ['Délka těla', 'delší záda, často zaoblený lem', 'záda zůstanou kryta při běhu a v předklonu'],
              ['Rukávy', 'v poměru k šířce delší, někdy s otvory na palce', 'ruce zůstávají v teple i při zvednutých pažích'],
              ['Výstřih a zip', 'nižší límec nebo stojáček s měkkým lemem', 'neškrtí a nedře krk'],
              ['Velikosti', 'písmenné XS–XL nebo číselné evropské', 'jemnější odstupňování než u unisex řad']]) +
          '<p>Rozdíl se projeví při pohybu paží. Když zvednete ruce nad hlavu, špatně střižená mikina se vytáhne nad pas a odhalí záda, kde se rychle prochladne. Dámský střih bývá delší vzadu právě proto. V nabídce stojí za pozornost modely označené jako <em>women</em>, <em>lady</em> nebo prostě dámské, ale ověřte vždy i skutečné rozměry v tabulce.</p>'
          '<h2>Mikina jako střední vrstva, nebo samostatný kus</h2>'
          '<p>Funkční mikina se v systému oblékání používá dvojím způsobem. Při chladném počasí je středním článkem mezi spodním tričkem a vnější bundou. Při mírném počasí je sama vrchní vrstvou, na běh, procházku se psem nebo na trénink venku. Podle toho se liší tloušťka a střih.</p>'
          '<ul><li><strong>Střední vrstva:</strong> lehce přiléhavá, s elastickou látkou a rýhovanou nebo mřížkovou strukturou uvnitř, která drží teplo. Vedle ní se musí vejít nepromokavá bunda, proto nechtějte volný střih.</li>'
          '<li><strong>Samostatná vrstva:</strong> o něco volnější, s kapsami na zip a lépe odolným povrchem proti oděru batohu.</li>'
          '<li><strong>Zahřívací vrstva na zastávky:</strong> hustší materiál nebo fleece, který lehce zabalíte do batohu.</li></ul>'
          '<p>Pokud spíš hledáte teplý kus s měkkou vnitřní stranou, projděte <a href="/fleecove-mikiny/">fleecové mikiny</a>. Obecný přehled všech druhů najdete v kategorii <a href="/mikiny/">mikiny</a>. Tato stránka zůstává u kusů, které především odvádějí pot a nepřekážejí v pohybu.</p>'
          '<h2>Tloušťka podle činnosti</h2>'
          + T(['Činnost', 'Vhodná mikina', 'Na co dát pozor'], [
              ['Svižný běh', 'tenká, přiléhavá, rychleschnoucí', 'zip do půlky hrudi pro větrání, reflexní prvky'],
              ['Fitness a trénink v hale', 'lehká, pružná, bez objemných kapes', 'netlačící švy v podpaží, jemný límec'],
              ['Procházky a lehká turistika', 'střední gramáž s měkkým vnitřkem', 'kapsy na zip, prodyšný záda'],
              ['Běžky a zimní sporty', 'hřejivá s větrnější přední částí', 'delší záda, ochrana krku'],
              ['Jóga a zahřátí před cvičením', 'hladká, měkká, nepříliš těsná', 'plochý zip nebo bez zipu'],
              ['Cestování', 'univerzální střední tloušťka', 'málo se mačká, rychle schne po vyprání']]) +
          '<p>Pravidlo je prosté: čím je činnost intenzivnější, tím tenčí mikinu potřebujete. Při klusu v chladu se tělo rozehřeje po několika minutách a hutná mikina je pak zbytečná. Při pomalé chůzi nebo stání na kopci naopak potřebujete izolaci, protože nevytváříte dost vlastního tepla. Proto se vyplatí na delší výlet nést tenkou i hřejivější verzi a podle tempa střídat.</p>'
          '<h2>Zip, kapuce, límec a kapsy</h2>'
          '<p>Detaily rozhodují o pohodlí víc, než se zdá. Mikina s dlouhým zipem je univerzální, protože se dá otevřít při stoupání a zavřít na rozcestí. Krátký zip u krku šetří váhu a jeho absence omezuje místa, kde může foukat. Kulatý výstřih je nejlehčí a nejjednodušší, ale chybí mu možnost větrání.</p>'
          '<ul><li><strong>Celý zip:</strong> nejuniverzálnější, snadno se svléká. Dobré je zakončení brady měkkým lemem.</li>'
          '<li><strong>Půlzip:</strong> méně prostupný větru, lehčí a oblíbený u běžců.</li>'
          '<li><strong>Stojáček:</strong> chrání krk bez šály. Pozor na tuhý lem, který se může dřít o bradu.</li>'
          '<li><strong>Kapuce:</strong> hodí se do města, na túru brání větru, ale při nošení batohu tlačí na krku.</li>'
          '<li><strong>Kapsy na zip:</strong> uchrání klíče nebo telefon před vypadnutím, kapsy bez zipu při běhu nic neudrží.</li>'
          '<li><strong>Otvory na palce:</strong> prodlouží rukáv přes hřbet ruky a nahradí tenkou rukavici.</li></ul>'
          '<h2>Syntetika, merino a směsi</h2>'
          '<p>Většina funkčních mikin je z polyesteru nebo jeho směsi s elastanem. Polyester schne rychle, nemačká se a snese časté praní. Odpovědí na zápach u syntetiky bývá antibakteriální úprava, která však slábne praním. Merino a směsi s vlnou drží teplo i vlhké, nezapáchají a příjemně hřejí, ale rychle schnou o něco méně a při neopatrném praní se srazí. Ke komplexním informacím se vraťte v přehledu <a href="/merino-mikiny/">merino mikin a svetrů</a>.</p>'
          '<p>Pro ženy, které se v chladu rychle potí a vzápětí zmrznou, je materiál důležitější než tloušťka. Hladký polyester odvede pot k povrchu a vrchní vrstva ho vypustí ven. Bavlna ve směsi pot nasákne a drží ho u těla. Proto se do funkční vrstvy bavlně vyhněte, pokud neplánujete jen procházku.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Velikosti dámských mikin kolísají mezi značkami více než u trik. Švédská a norská výroba bývá střižena štíhleji, britské outdoorové řady volněji, sportovní lifestylové značky často s přesahem v ramenou. Proto se vyplatí vzít do ruky metr a změřit obvod hrudi pod paží, pasu a boků, pak porovnat s tabulkou konkrétního výrobce. Ke každé nabídce na Sportece ověřte, zda velikost sedí na váš obvod, a ne jen na označení S nebo M.</p>'
          '<ol><li>Změřte obvod hrudníku v nejširším místě a pasu v nejužším bodě.</li>'
          '<li>Podívejte se do tabulky u produktu a vyberte velikost podle většího rozměru.</li>'
          '<li>Pokud plánujete pod mikinou nosit tlustší spodní vrstvu, přidejte půl velikosti.</li>'
          '<li>Zkontrolujte délku rukávů: mají končit těsně za zápěstní kostí.</li>'
          '<li>Při pochybnostech vezměte dvě velikosti a vraťte tu, která při předklonu odkryje záda.</li></ol>'
          '<h2>Co nosit pod mikinou a pod ní</h2>'
          '<p>Pod mikinou je nejlepší hladké funkční triko s krátkým nebo dlouhým rukávem a sportovní podprsenka s dostatečnou oporou. Pokud mikinu nosíte při běhu, přijdou na řadu <a href="/tilka/">tílka</a> nebo tričko, které se neřasí pod popruhy. Zespodu se hodí <a href="/leginy/">legíny</a> nebo kalhoty s elastickou texturou, které nebrání kroku. Při zimní aktivitě pomůže <a href="/termopradlo/">termoprádlo</a>, které rozšiřuje rozsah teplot mikiny bez přidání objemu.</p>'
          '<p>Při kombinování dbejte na jednotnost barev. Černá a šedá vyhovují každému doplňku, výrazné odstíny jsou praktické pro viditelnost při večerním běhu. Světlé barvy odhalí oděr nebo skvrny od zeminy, tmavé je skryjí, ale v šeru splývají s okolím. Proto se vyplatí zvolit mikinu se světlými reflexními detaily.</p>'
          '<h2>Značky, které v dámských mikinách najdete</h2>'
          '<p>Nabídka na Sportece zahrnuje široké spektrum. Outdoorové a trekové mikiny nabízejí značky ' + B(('dare2b', 'Dare2b'), ('hannah', 'Hannah'), ('kilpi', 'Kilpi'), ('northfinder', 'Northfinder'), ('whistler', 'Whistler')) + '. Pro běh a trénink sáhněte po ' + B(('adidas', 'Adidas'), ('under-armour', 'Under Armour'), ('on', 'On'), ('4f', '4F')) + '. Pro běžky a zimní pohyb se vyplatí rozhlédnout po ' + B(('swix', 'Swix'), ('kari-traa', 'Kari Traa')) + ', které se zaměřují přímo na ženy a sezonní vrstvení. Značky mají různé zaměření, proto vždy čtěte popis materiálu a doporučené použití.</p>'
          '<h2>Péče, aby mikina vydržela</h2>'
          '<p>Funkční mikinu perte podle štítku, obvykle na nižší teplotu a bez aviváže, která zalepuje vlákna a snižuje odvod vlhkosti. Zapněte zip, aby neškrábal ostatní kusy, a otočte mikinu naruby, aby se vnitřní struktura zbytečně netřela. Sušte ji volně na ramínku mimo přímý zdroj tepla. Pokud po praní stále zapáchá, nechte ji přes noc namočit v roztoku studené vody a octa nebo použijte prací prostředek pro sportovní textil.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každé mikiny porovnejte nabídky obchodů, ověřte dostupnost své velikosti a podívejte se na materiál i střih v popisu. Pokud váháte mezi dvěma kusy, rozhodne obvykle použití: pro svižný pohyb tenčí, pro pomalejší aktivity hřejivější. Dalšími ženskými řadami jsou i <a href="/damske-plavky/">dámské plavky</a> pro bazén nebo <a href="/bezecka-obuv/">běžecká obuv</a>, kterou se vyplatí sladit s oblečením ještě před sezonou.</p>',
    faq=[
        ('Čím se dámská funkční mikina liší od pánské?', 'Má užší ramena, tvarovanější pas, delší záda a v poměru k šířce delší rukávy. Pánský kus ženě obvykle visí v pase a v podpaží se sbírá. Dámský střih omezuje zbytečnou látku a při zvednutých pažích lépe kryje záda.'),
        ('Můžu si koupit unisex nebo pánskou mikinu?', 'Ano, pokud vám sedí ramena i délka rukávů. Menší ženy se často cítí lépe v dámském střihu, vyšší nebo širší postavy bývají spokojené i v unisex řadách. Při rozhodování se řiďte skutečnými rozměry v tabulce, ne jen označením.'),
        ('Jak poznám, že mikina odvádí pot?', 'Hledejte popis syntetických vláken, polyesteru nebo směsi s elastanem a zmínku o odvodu vlhkosti. Rozhoduje i struktura vnitřní strany. Bavlněná mikina pot nasaje a zůstane studená, funkční ho přenese k povrchu, kde schne.'),
        ('Jak tlustou mikinu na běh zvolit?', 'Na běh vybírejte tenkou a přiléhavou, která se dá snadno svléknout a uložit k pasu. Rozběhaná se zahřejete dřív, než čekáte, proto příliš hutná vrstva nevyhovuje. Při chladném počasí je lepší přidat jednu vrstvu pod mikinu než volit masivní kus.'),
        ('Je lepší celý zip, nebo půlzip?', 'Celý zip je univerzální a umožňuje větrání i snadné svlékání. Půlzip je lehčí, menší a lépe drží teplo kolem krku. Na běh a rychlé aktivity stačí půlzip, na turistiku nebo promenádu se víc hodí celý zip.'),
        ('Dá se funkční mikina prát v pračce?', 'Ano, na nižší teplotu a bez aviváže. Zapněte zip, otočte mikinu naruby a nepoužívejte sušičku s vysokou teplotou. Aviváž zalepuje vlákna, takže mikina přestane odvádět pot. Sušte ji na ramínku.'),
        ('Zapáchá syntetická mikina víc než merino?', 'Syntetika zachytává pachy rychleji, protože bakterie se na vláknech snadno množí. Pomůže antibakteriální úprava, pravidelné praní a vyvětrání po použití. Merino je v tomto ohledu klidnější, ale schne pomaleji a vyžaduje jemnější péči.'),
        ('Mám volit mikinu s kapucí, nebo bez?', 'Kapuce se hodí do města a na procházky, kde chrání před větrem. Při sportu a nošení batohu tlačí na krk a zadní část hlavy. Na běh a trénink proto upřednostněte stojáček nebo prostý výstřih.'),
        ('Co si obléct pod funkční mikinu?', 'Nejlépe hladké funkční triko nebo termoprádlo z jemného materiálu a sportovní podprsenku s oporou odpovídající aktivitě. Bavlna pot drží u těla. Při mrazu přidejte spodní vrstvu z merina, v mírném počasí stačí tenké tričko.'),
        ('Jakou velikost vybrat, když jsem mezi dvěma?', 'Pokud mikinu nosíte jako samostatnou vrstvu, zvolte menší. Pokud ji plánujete oblékat přes další vrstvu, vezměte větší. Vždy porovnejte obvod hrudníku s tabulkou výrobce a zkontrolujte, zda rukáv nekončí příliš nad zápěstím.'),
    ])

# ------------------------------------------------------------------ ccm-hokejky
NEW['ccm-hokejky'] = dict(
    title='CCM hokejky: Ribcor, Jetspeed, Tacks a Vizion',
    desc='Hokejky CCM pro děti, juniory i dospělé: řady Ribcor, Jetspeed, Tacks a Vizion, délka, flex, zahnutí čepele a rozdíly proti Bauer. Srovnání obchodů.',
    intro='<p>CCM patří mezi tři největší jména světového hokejového vybavení a hokejky tvoří jeho nejviditelnější část. V nabídce Sporteky najdete hole z řad Ribcor, Jetspeed, Tacks a Vizion, v délkách od miniatur pro nejmenší po seniorské modely, v pravé i levé verzi a s několika zahnutími čepele. '
          'Rozdíly mezi řadami nespočívají jen v barvě. Liší se konstrukcí, váhou, odezvou a tím, pro koho jsou určeny. Průvodce níže vysvětluje, jak se orientovat v označeních typu SR, INT, JR a YTH, jak vybrat flex a délku, co znamenají čísla P28, P29 nebo P92 a kdy se vyplatí alternativa od konkurence. Základ celé kategorie najdete v přehledu <a href="/hokejky/">hokejky</a>, ke srovnání se hodí <a href="/bauer-hokejky/">hokejky Bauer</a> a <a href="/hokejka-warrior/">Warrior</a>.</p>',
    guide='<h2>Jak číst označení CCM hokejek</h2>'
          '<p>Název hole obsahuje hned několik údajů. Za jménem řady následuje velikostní třída, tuhost a zahnutí čepele. Pokud si je přečtete správně, vyhnete se zakoupení špatné hole a nemusíte ji vracet.</p>'
          + T(['Zkratka', 'Význam', 'Pro koho'], [
              ['SR (Senior)', 'dospělá velikost, dlouhá násada', 'dospělí a dorostenci, kteří dosáhnou na dospělou délku'],
              ['INT (Intermediate)', 'střední velikost mezi juniorem a seniorem', 'starší dorost a menší dospělí'],
              ['JR (Junior)', 'hole pro dorost a starší děti', 'přibližně školní věk druhého stupně'],
              ['YTH (Youth)', 'dětská velikost', 'mladší děti od začátků bruslení'],
              ['Mini', 'nejkratší verze, často zábavně barevná', 'nejmenší děti a suvenýry'],
              ['L / R nebo P / Levá / Pravá', 'strana, na které držíte dolní ruku', 'podle toho, jak držíte hůl']]) +
          '<p>Čísla jako 85, 75 nebo 55 u názvu značí flex, tedy tuhost. Označení P28, P29 nebo P92 vyjadřuje zahnutí čepele, tedy její tvar a sklon. Pokud nevíte, jakou čepel držíte, zeptejte se trenéra nebo se podívejte na značení na hokejce, kterou už používáte.</p>'
          '<h2>Jednotlivé řady CCM</h2>'
          '<p>Značka rozděluje hole do řad podle toho, jak se hraje. Přesné popisy a parametry proměňuje s každou sezonou, proto jsou zde jen obecná vodítka. Přesné údaje vždy ověřte u konkrétního modelu.</p>'
          '<ul><li><strong>Ribcor Trigger:</strong> řada se zaměřením na střelbu a dynamický odpal. Najdete ji ve více cenových třídách a od dětských po seniorské velikosti.</li>'
          '<li><strong>Jetspeed:</strong> hůl pro hráče, kteří chtějí rychlý spoušť a lehkou konstrukci. K dispozici je i dámská verze FTW pro středně pokročilé.</li>'
          '<li><strong>Tacks:</strong> řada pro hráče, kteří kladou důraz na cit a práci s pukem. V nabídce se objevují varianty AS-V, AS-570 a XF.</li>'
          '<li><strong>Vizion:</strong> modely pro začínající a pokročilé hráče, mimo jiné i juniorské a dětské verze.</li>'
          '<li><strong>Ultimate a Secret Minis:</strong> dětské a zábavní hole, vhodné pro první kroky na ledě nebo na ulici.</li></ul>'
          '<p>Při vyhledávání v nabídce se držte celých názvů řad, protože stejné číslo flexu se u různých modelů může chovat odlišně. Dvě hole se stejným číslem nemusí být stejně pevné, pokud mají jinou konstrukci nebo materiál.</p>'
          '<h2>Délka hole podle výšky a stylu hry</h2>'
          '<p>Při správné délce hole se hráč v základním postoji může s pukem pohodlně pohybovat a zároveň vidí, kam míří. Základní pravidlo: hůl postavená na špičku čepele má končit mezi bradou a nosem hráče bez bruslí. S bruslemi se délka posouvá o výšku nože a boty.</p>'
          + T(['Styl hry', 'Doporučená délka', 'Co to přináší'], [
              ['Obránce, silová hra', 'o něco delší', 'delší dosah při obraně a silnější úder'],
              ['Útočník, práce s pukem', 'o něco kratší', 'lepší kontrola a rychlejší manipulace'],
              ['Univerzální hráč', 'ke rtům nebo bradě', 'kompromis mezi dosahem a citem'],
              ['Dětský hráč', 'ke rtům, ne výš', 'netahá hůl v nepřirozeném úhlu'],
              ['Při růstu', 'raději delší a seříznout', 'hůl vydrží další sezonu']]) +
          '<p>U kompozitových holí lze násadu zkrátit pilkou, ale nelze ji prodloužit jinak než nástavcem. Proto se při pochybnostech vybírá delší verze. U dětí se vyplatí kupovat hole s moderní délkou raději o něco kratší, aby se naučily správné držení a nehrbily se. Pokud potřebujete prodloužení nebo novou čepel, najdete je v kategorii <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>.</p>'
          '<h2>Flex: kolik tuhosti unesete</h2>'
          '<p>Flex vyjadřuje, kolik síly je potřeba k prohnutí hole. Obecné pravidlo říká, že hráč by měl zvolit hodnotu zhruba poloviční oproti své tělesné hmotnosti v kilogramech, u dětí se tato hodnota vyjadřuje v nižších číslech. Ve skutečnosti rozhoduje i technika. Pokud při střelbě hůl neprohnete, je příliš tuhá a vaše střela ztrácí sílu. Je-li naopak příliš měkká, ztrácíte přesnost a cítíte nepřesnou odezvu.</p>'
          '<ul><li><strong>Nižší flex:</strong> pro lehčí hráče a děti, hůl se snáze prohýbá.</li>'
          '<li><strong>Střední flex:</strong> většina rekreačních dospělých a dorostenců.</li>'
          '<li><strong>Vyšší flex:</strong> těžší a silnější hráči s dobrou střeleckou technikou.</li>'
          '<li><strong>Zkrácená hůl:</strong> po seříznutí se tuhost zvyšuje, proto si u dlouhé hole klidně vezměte nižší hodnotu.</li></ul>'
          '<h2>Zahnutí čepele a strana</h2>'
          '<p>Zahnutí určuje, jak puk leží na čepeli a jak se vám přihrává i střílí. Označení jako P28, P29 nebo P92 odkazují na konkrétní tvary čepele, které se liší sklonem, otevřeností a místem, kde je čepel nejvíce zahnutá. Přesný tvar se mezi modely a sezonami mění, proto ověřte popis konkrétní hole. Pokud začínáte, držte se zahnutí, na které jste zvyklí, a změnu zkoušejte až po delším hraní.</p>'
          '<p>Strana hole se určuje podle toho, která ruka je dole na násadě. Levý hráč drží hůl dolní levou rukou, pravý pravou. Děti by měly vyzkoušet obě varianty a vybrat tu, v níž se jim nejpřirozeněji střílí. Špatná strana není vada, ale vede k trvalému nepohodlí. Pokud si nejste jistí, požádejte trenéra o rychlý test.</p>'
          '<h2>Dětské a juniorské hole CCM</h2>'
          '<p>Pro děti jsou důležité nízká váha a vhodná délka. Příliš dlouhá hůl vede k hrbení a špatnému bruslení. Při koupi se řiďte velikostními řadami YTH, JR a INT a hledejte také poznámku o hmotnosti hole. Pro nejmladší hráče existují i minihole, které slouží jako suvenýr nebo trénink doma. Pokud shánite pomůcku pro dítě, prohlédněte si i výběr <a href="/detska-hokejka/">dětská hokejka</a> a zvažte doplnění o <a href="/hokejove-pasky-a-doplnky/">hokejové pásky</a>.</p>'
          '<p>Je dobré počítat s tím, že děti rostou rychle a hole se obnovují častěji než u dospělých. Proto se vyplatí vybírat střední kategorii s poctivou konstrukcí a ne nejdražší model. Pro soutěžní juniory má smysl zvážit lehčí kompozit, který jim pomůže s rychlostí střely.</p>'
          '<h2>CCM v porovnání s Bauer, Warrior a Winnwell</h2>'
          '<p>Hlavními konkurenty jsou ' + B(('bauer', 'Bauer'), ('warrior', 'Warrior'), ('sherwood', 'Sherwood'), ('winnwell', 'Winnwell'), ('fischer', 'Fischer')) + '. Všichni nabízejí kompozitové hole různých tříd, liší se hlavně konstrukcí, zahnutími a reakcí hole při střelbě. Winnwell je často volbou pro začátečníky a rekreační hráče, Fischer je znám především ze světa pozemního hokeje a florbalu. Pro hráče je nejlepší rada jednoduchá: vyzkoušet několik holí a vybrat tu, která sedí v rukou. Pokud porovnáváte, začněte u <a href="/bauer-hokejky/">hokejek Bauer</a> a <a href="/hokejka-warrior/">hokejek Warrior</a>.</p>'
          '<h2>Co ještě k hokejce patří</h2>'
          '<p>Pro hru je kromě hole důležité i vybavení pod ní. Správně seříznuté a omotané ruce, tedy <a href="/hokejove-pasky-a-doplnky/">páska a doplňky</a>, ovlivňují cit. Pro ochranu hráče sehrají roli <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>, pro bruslení pak <a href="/hokejove-brusle/">hokejové brusle</a>. Na přepravu jsou praktické <a href="/hokejove-tasky/">hokejové tašky</a>. Celkový obor popisuje kategorie <a href="/hokej/">hokej</a>.</p>'
          '<h2>Jak nakupovat hokejky CCM na Sportece</h2>'
          '<p>Při srovnání nabídek zkontrolujte u každé hole několik údajů. Přesný název řady, flex, délku, stranu, zahnutí a stav skladu v obchodě. Stejný model se vyskytuje v mnoha variantách a drobný rozdíl v označení odpovídá jinému tvaru čepele. Použité nebo letité modely z dřívější sezony se mohou lišit materiálem i parametry, proto čtěte popis a nenechte se zmást podobným názvem. Zlatá, černá nebo bílá barva sice neovlivní hru, ale pomáhá poznat hůl v šatně, k čemuž se hodí i výběr <a href="/zlata-hokejka/">zlatá hokejka</a>.</p>'
          '<h2>Péče o hůl</h2>'
          '<p>Kompozitová hůl nemá ráda údery o tvrdý povrch, zvlášť v místě přechodu mezi násadou a čepelí. Po zápase hůl otřete a neodkládejte ji v mokré tašce. Hrany čepele se při hře obrušují, proto páska chrání před opotřebením. Hůl neskladujte v autě za horka nebo v mrazu, kompozitové vlákno může změnit vlastnosti. Před sezonou překontrolujte, zda nemá praskliny, a při jakékoli pochybnosti hůl vyměňte, protože rozlomená hůl při střele může způsobit zranění.</p>',
    faq=[
        ('Co znamená označení SR, INT, JR a YTH u hokejky CCM?', 'SR je senior, tedy dospělá velikost, INT je střední velikost mezi juniorem a seniorem, JR je juniorská hůl pro dorost a YTH je dětská verze. Velikost vyjadřuje délku a obvykle i tuhost. Nejmenší hole označené Mini slouží hlavně pro nejmladší děti.'),
        ('Jak dlouhou hokejku vybrat?', 'Hůl postavená na špičku čepele má bez bruslí končit zhruba mezi nosem a bradou. Obránci volí o něco delší, útočníci kratší. Hůl lze u kompozitu zkrátit, ale ne prodloužit, proto při nejistotě vyberte delší.'),
        ('Který flex je pro mě správný?', 'Orientačně přibližně polovina tělesné hmotnosti v kilogramech, u dětí se hodnoty drží výrazně níž. Pokud hůl při střelbě neprohnete, je tuhá. Pokud je příliš měkká, ztrácíte přesnost. Správný flex vám při střelbě dovolí cítit prohnutí bez snahy o sílu.'),
        ('Jak poznám, jestli mám levou, nebo pravou hokejku?', 'Podle toho, která ruka je při držení dole na násadě. Levý hráč drží hůl levou rukou dole, pravý pravou. Děti by měly zkusit obě varianty a vybrat tu, ve které jim střelba a přihrávka jdou přirozeněji. Trenér s tím rád poradí.'),
        ('Čím se liší řady Ribcor, Jetspeed a Tacks?', 'Jde o rozdílné konstrukce a zaměření podle hráče. Ribcor je řada orientovaná na střelbu, Jetspeed na rychlou odezvu a lehkost, Tacks na cit a práci s pukem. Přesné vlastnosti se mění s každou sezonou, proto čtěte popis konkrétního modelu.'),
        ('Je CCM lepší než Bauer?', 'Nejde o jednoznačné pořadí. Obě značky nabízejí kompozitové hole ve všech třídách. Rozhoduje to, jak vám konkrétní model sedí v rukou, jaké zahnutí používáte a jaký je jeho flex. Vyzkoušejte aspoň dvě hole a vyberte tu, která sedí.'),
        ('Kolik mám počítat s životností kompozitové hole?', 'Záleží na intenzitě hry a na tom, jak často hůl naráží o led nebo mantinel. U pravidelných hráčů se může výměna hole opakovat několikrát za sezonu. Rekreační hráč vystačí s jednou holí déle. Pokud se objeví prasklina, hůl vyměňte.'),
        ('Dají se hole CCM seříznout?', 'Ano, kompozitové hole lze zkrátit pilkou nebo řezačkou. Tuhost se po zkrácení zvyšuje, proto si u delší hole klidně vezměte nižší flex. Prodloužit hůl jde jen použitím nástavce nebo koupí delšího modelu.'),
        ('Hodí se CCM hokejka i na florbal nebo pozemní hokej?', 'Ne. Hokejky na led mají jinou délku, tvar čepele a konstrukci než florbalové hole nebo hole na pozemní hokej. Při nákupu zkontrolujte název kategorie a doporučené použití, protože stejně vypadající hole se používají ve zcela jiném sportu.'),
        ('Jakou hůl koupit dítěti, které teprve začíná?', 'Lehkou, krátkou a nepříliš tuhou dětskou nebo juniorskou verzi odpovídající výšce. Vyhněte se příliš dlouhým holím, které nutí k hrbení. Nejdražší model nemá smysl, dítě z hole brzy vyroste. Zkontrolujte stranu a zahnutí čepele.'),
    ])

# ------------------------------------------------------------------ sportovni-podprsenka-nike
NEW['sportovni-podprsenka-nike'] = dict(
    title='Sportovní podprsenka Nike: Indy, Swoosh, Pro a Dri-FIT',
    desc='Sportovní podprsenky Nike: rozdíl mezi řadami Indy, Swoosh a Pro, míra podpory, velikosti i dívčí modely. Jak vybrat a porovnat nabídky obchodů.',
    intro='<p>Sportovní podprsenky Nike se v nabídce dělí především podle míry podpory a podle sportu, pro který vznikly. Řada Indy míří na lehčí aktivity a jógu, Swoosh nabízí střední oporu pro trénink a běh a Pro používají ženy, které chtějí střih těsně přiléhající k tělu. K tomu přibývají modely z materiálu Dri-FIT, odvádějícího pot, a dívčí varianty pro mladé sportovkyně. '
          'Na této stránce najdete podprsenky Nike z kategorie <a href="/sportovni-podprsenky/">sportovní podprsenky</a>. Průvodce vysvětluje, co znamenají názvy řad, jak číst označení podpory, kdy zvolit vycpávky a kdy raději bez nich, jak se liší velikosti od značek s košíčky a jak se Nike staví vedle <a href="/sportovni-podprsenka-under-armour/">Under Armour</a> nebo <a href="/sportovni-podprsenka-calvin-klein/">Calvin Klein</a>.</p>',
    guide='<h2>Jak číst řady Nike</h2>'
          '<p>Nike dává modelům krátká jména, která naznačují účel. Skutečné parametry vždy čtěte v popisu u konkrétního produktu, protože střih i podpora se mohou měnit mezi sezonami. Následující přehled slouží jako obecné vodítko k řadám, které v nabídce najdete.</p>'
          + T(['Řada', 'Obvyklé zaměření', 'Pro jaké sporty'], [
              ['Indy', 'nízká podpora, měkký střih', 'jóga, pilates, protahování, chůze'],
              ['Swoosh', 'střední podpora, často s lehkými vycpávkami', 'fitness, tanec, lehčí běh'],
              ['Pro', 'přiléhavý střih, často s košíčky, střední podpora', 'trénink, posilovna, cvičení v hale'],
              ['Dri-FIT 365', 'technický materiál, každodenní nošení', 'cvičení i běžný den'],
              ['Sportswear', 'volnočasový vzhled, měkký top', 'město, procházky, odpočinek'],
              ['Girls / dětské', 'menší velikosti, jednodušší střih', 'školní tělocvik, gymnastika, kroužky']]) +
          '<p>Podprsenky v nabídce se liší i barvou: Nike nabízí klasické černé a bílé kusy, ale také červené, růžové, zelené nebo vínové. Pro každodenní trénink je černá praktická, protože skryje pot a otěr, bílá působí svěže, ale rychleji ukáže skvrny. Pro barevné varianty se vyplatí pročíst <a href="/bila-sportovni-podprsenka/">bílou sportovní podprsenku</a>, kde se vyskytují i modely jiných značek.</p>'
          '<h2>Míra podpory a skutečný sport</h2>'
          '<p>Základní pravidlo zní: čím větší náraz, tím pevnější podpora. Nízká podpora vyhovuje klidným aktivitám, střední cvičení s občasným skákáním, vysoká pak běhu a skokům. Nike označuje u řady Pro a Indy často střední nebo nízkou podporu přímo v názvu, například ve formulaci Medium-Support, a stejné označení hledejte i v popisu obchodu. Pokud potřebujete podprsenku na pravidelný běh, ověřte, zda je skutečně určena pro vyšší nárazy, a nespoléhejte se jen na název řady.</p>'
          '<ul><li><strong>Jóga a pilates:</strong> měkký střih bez kostic, často s tenkými ramínky nebo zkříženými zády.</li>'
          '<li><strong>Posilovna:</strong> širší ramínka a pevný spodní lem, aby podprsenka při zdvihání nevyjížděla.</li>'
          '<li><strong>Běh:</strong> kompresní nebo zapouzdřený střih s pevnou oporou, bez volného prostoru po stranách.</li>'
          '<li><strong>Tanec a skupinové lekce:</strong> střední podpora s lehkou vycpávkou pro rozhýbané pohyby.</li>'
          '<li><strong>Každodenní nošení:</strong> měkký top bez zipů a bez švů, který nedře.</li></ul>'
          '<p>Při pochybnostech zkuste jednoduchý test: ve zkušebně se několikrát vyskočte a pohybujte pažemi. Podprsenka by měla držet bez zařezávání a nesmí se posouvat po těle. Na internetu vám stejný test nahradí podrobné čtení popisu a velikostní tabulky.</p>'
          '<h2>Vycpávky, košíčky a pevné kousky</h2>'
          '<p>Modely Nike s označením padded mají vyjímatelné nebo zabudované vycpávky. Zajišťují krytí, tvar a nenápadnost pod světlým tričkem. Vyjímatelné vložky se vám při praní občas posunou, proto je před sušením vyndejte a po vyschnutí vraťte. Modely bez vycpávek jsou lehčí a rychleji schnou, což ocení hlavně běžkyně v létě. Rozhodněte se podle toho, co od podprsenky čekáte, ne podle módy.</p>'
          '<h2>Velikosti u Nike: písmena, ne košíčky</h2>'
          '<p>Většina podprsenek Nike se dodává v písmenných velikostech XS až XL, nikoli v kombinaci obvod a košíček. To je pohodlné pro menší a střední poprsí, ale ženy s plnějším tvarem mohou narazit na hranici. Takovým ženám se vyplatí vybírat modely s vyšší oporou nebo porovnat s řadami, které velikost uvádějí číselně. Měřte obvod pod prsy i v nejširším místě hrudi a porovnejte s tabulkou na stránce obchodu.</p>'
          + T(['Kontrola', 'Jak má podprsenka sedět'], [
              ['Spodní lem', 'leží rovně, netlačí a nesjíždí nahoru'],
              ['Ramínka', 'přiléhají, ale neřežou, nemají se sesouvat z ramen'],
              ['Střed mezi prsy', 'přiléhá ke hrudní kosti nebo je jen lehce nad ní'],
              ['Záda', 'stejně těsná jako vpředu, nevyskakuje při předklonu'],
              ['Dýchání', 'plný nádech nesmí být omezený']]) +
          '<p>Pokud jste mezi dvěma velikostmi, vyberte menší u měkkých modelů z pružné pleteniny a větší u modelů s pevnými vycpávkami. Přesnější radu najdete vždy v popisu produktu.</p>'
          '<h2>Materiály a péče</h2>'
          '<p>Technická pletenina Dri-FIT slouží k odvodu potu, tedy aby látka zůstala sušší než bavlna. Většinou jde o směs polyesteru a elastanu, někdy s příměsí jiných vláken. Perte ji ve vlažné vodě, nejlépe v ochranném pytlíku, bez aviváže. Aviváž zalepuje vlákna a snižuje pružnost, takže podprsenka brzy ztratí oporu. Sušte ji na vzduchu, ne na radiátoru a ne v sušičce. Pokud má podprsenka vyjímatelné vložky, vyndejte je a nechte vyschnout samostatně.</p>'
          '<p>Pro delší životnost střídejte dva nebo tři kusy při pravidelném tréninku. Pružná vlákna si potřebují po zátěži odpočinout a podprsenka nošená denně ztrácí oporu rychleji. Pokud se vám zdá, že lem sjíždí, je čas na výměnu.</p>'
          '<h2>Dívčí podprsenky Nike</h2>'
          '<p>Dívčí modely se označují Girls nebo dětské a zahrnují například asymetrické střihy a lehké topy. Jejich cílem je pohodlí při tělocviku, gymnastice, tanci a míčových hrách. Zpravidla nejsou určeny pro intenzivní vysokou zátěž, takže při pravidelném sportu u starších dívek je dobré sledovat popis podpory. Při výběru velikosti u dívek raději počítejte s tím, že rostou, ale přílišná volnost nepomáhá. Pružný pás by měl držet bez stlačení hrudníku.</p>'
          '<h2>Nike v porovnání s dalšími značkami</h2>'
          '<p>Nike se zaměřuje na univerzální sportovní střihy s výraznou logem na lemu. Podobnou nabídku mají ' + B(('under-armour', 'Under Armour'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('reebok', 'Reebok')) + '. Specializovanější podprsenky s numerickými velikostmi nabízejí značky orientované na vysokou podporu, kde obvod a košíček určují přesnější tvar. Nike je tedy vhodné pro většinu tréninků, jógu, posilovnu a každodenní nošení. Pro nejintenzivnější běh a vyšší velikosti hledejte pevné střihy s jasně uvedenou podporou.</p>'
          '<h2>Jak podprsenku zvolit podle fází cvičení</h2>'
          '<p>Mnoho žen potřebuje podprsenku do více situací, a proto se vyplatí mít dva typy. Měkký top s nízkou oporou použijete na protažení, procházku nebo doma při práci. Pevnější model si nechte na běh, skupinové lekce a cvičení se skoky. Pokud máte jen jeden kus, vyberte střední podporu a při intenzivnějším sportu zkontrolujte, jak se chová při poskoku. Před tréninkem v zimě je příjemné zvolit podprsenku z hladkého materiálu, který nedře o termoprádlo, a v létě model s větraným zády.</p>'
          '<p>Důležitá je i trvanlivost švů. Ploché nebo bezešvé spoje nedřou pod pažemi a pod prsy, zatímco hrubé švy se po několika hodinách tréninku mohou projevit otlaky. Při čtení popisu proto sledujte zmínku o bezešvém provedení a o šířce spodního lemu, který má ležet rovně a neotáčet se.</p>'
          '<h2>Co nosit společně</h2>'
          '<p>Podprsenku doplňte <a href="/leginy/">legínami</a> s vysokým pasem a <a href="/tilka/">tílkem</a>, které nebude tlačit na ramínka. Při chladnějším počasí přidejte lehkou <a href="/funkcni-mikiny/">funkční mikinu</a>, kterou lze snadno rozepnout. Pokud potřebujete běžné spodní vrstvy, prohlédněte si <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>. Při plavání nebo vodních aktivitách se hodí <a href="/damske-plavky/">dámské plavky</a> s oporou.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každé podprsenky porovnejte nabídky několika obchodů, ověřte skladovost své velikosti a přečtěte si uvedenou míru podpory. Pozor na kombinaci stejného názvu a odlišné barvy, protože některé barevné varianty mohou být v obchodě dostupné jen v určitých velikostech. Pokud hledáte podprsenku bez vycpávek nebo naopak s nimi, použijte slova padded a non padded v popisu. Při pochybnostech si vyberte model s jasnějším popisem podpory a využijte možnosti vrácení zboží u obchodu.</p>',
    faq=[
        ('Jaký je rozdíl mezi řadami Indy, Swoosh a Pro?', 'Indy je řada s nízkou podporou pro klidné aktivity, Swoosh nabízí střední podporu pro fitness a trénink a Pro je těsněji střižená řada. Přesné parametry se mohou měnit, proto vždy čtěte popis u konkrétního modelu a míru podpory.'),
        ('Hodí se podprsenka Nike na běh?', 'Záleží na modelu. Měkké kousky z řady Indy jsou určené pro nízký náraz. Na běh vybírejte model s označením pevné nebo vysoké podpory, případně kompresní střih. Podprsenka by se při zkoušce neměla pohybovat nahoru a dolů.'),
        ('Jak vybrat správnou velikost?', 'Změřte obvod pod prsy a v nejširším místě hrudi a porovnejte s tabulkou obchodu. Nike používá hlavně písmenné velikosti od XS po XL. Při nejistotě volte menší u pružných měkkých topů a větší u modelů s pevnými vycpávkami.'),
        ('Mají podprsenky Nike vyjímatelné vložky?', 'Některé ano. Modely s označením padded mají vložky, které lze často vyndat. Před praním je vyjměte a po vyschnutí vraťte, aby se nezkroutily. Modely bez vycpávek jsou lehčí a rychleji schnou.'),
        ('Dají se podprsenky Nike prát v pračce?', 'Obvykle ano, ve vlažné vodě a nejlépe v ochranném pytlíku. Nepoužívejte aviváž, která zalepuje vlákna a snižuje pružnost, a nedávejte je do sušičky. Podprsenku sušte volně na vzduchu mimo radiátor.'),
        ('Jak dlouho vydrží sportovní podprsenka?', 'Při pravidelném tréninku zhruba jednu až dvě sezony. Poznáte to podle ochablého lemu, povolených ramínek a ztráty opory. Střídejte dva nebo tři kusy, pružná vlákna se pak mezi cvičeními stihnou zregenerovat.'),
        ('Prodávají se podprsenky Nike i pro dívky?', 'Ano. Dívčí a dětské modely mají menší velikosti a jednodušší střih. Jsou určené pro tělocvik, gymnastiku a lehké sporty. U starších dívek při intenzivním sportu raději sledujte popis podpory.'),
        ('Je lepší černá, nebo bílá?', 'Černá skryje pot i otěr a hodí se pod světlejší oblečení jako spodní vrstva. Bílá je svěží, ale rychleji ukáže skvrny a viditelně prosvítá pod tmavým tričkem. Pro každodenní trénink bývá praktičtější tmavá varianta.'),
        ('Co znamená Dri-FIT?', 'Jde o označení technické pleteniny Nike, která odvádí pot od těla k povrchu látky, kde schne. Nejde o ochranu před zápachem ani o nepromokavost. Praní bez aviváže pomáhá zachovat vlastnosti materiálu.'),
        ('Kam se podprsenka hodí v rámci celého outfitu?', 'Nosí se pod tílkem nebo tričkem, případně jako samostatný top při cvičení a v létě. Kombinujte ji s legínami, tílkem a lehkou funkční mikinou. Pro chladné počasí je dobrá spodní vrstva z termoprádla.'),
    ])

# ------------------------------------------------------------------ plavky-adidas
NEW['plavky-adidas'] = dict(
    title='Plavky Adidas: bazén, pláž, kraťasy a jednodílné',
    desc='Plavky Adidas pro ženy, muže i děti: jednodílné, bikiny, kraťasy a jammery. Rozdíly mezi Performance a Originals, velikosti, chlór a porovnání obchodů.',
    intro='<p>Adidas nabízí plavky pro bazén i pláž a drží se dvou hlavních směrů. Řada Performance míří na plavce a aktivní vodní sporty, řada Originals sází na volnočasový vzhled s třemi pruhy. Najdete tu jednodílné dámské plavky, bikiny, chlapecké a pánské kraťasy, jammery i dětské plavky s motivy z filmů. '
          'Tento průvodce vysvětluje, jak se Performance liší od Originals, proč se u pánských kraťasů uvádí délka v palcích, kdy zvolit těsné jammery a kdy volnější šortky a jak vybrat velikost pro děti. K základní nabídce se vraťte přes <a href="/plavky/">plavky</a>, podle pohlaví se orientujte v <a href="/damske-plavky/">dámských</a>, <a href="/panske-plavky/">pánských</a> a <a href="/detske-plavky/">dětských plavkách</a>.</p>',
    guide='<h2>Performance a Originals: dvě tváře Adidasu</h2>'
          '<p>Rozdíl mezi řadami se projeví v účelu. Performance je zaměřená na funkci, tedy na plavání, trénink a aktivní zábavu u vody. Originals vychází z volnočasového stylu značky, takže barvy, vzory a tvary jsou módnější. Plavky z obou řad lze nosit u bazénu i na pláži, ale s různými očekáváními.</p>'
          + T(['Vlastnost', 'Performance', 'Originals'], [
              ['Účel', 'plavání, trénink, aktivní hra ve vodě', 'pláž, dovolená, módní vzhled'],
              ['Střih', 'přiléhavější, pevné uchycení', 'volnější nebo módní tvary'],
              ['Materiál', 'důraz na odolnost a rychlé schnutí', 'pohodlí a vzhled'],
              ['Logo a vzory', 'tři pruhy, jednoduché barvy', 'výraznější grafika, retro prvky'],
              ['Vhodnost k chlóru', 'obecně lepší volba pro časté plavání', 'spíše občasné koupání']]) +
          '<p>Pokud plavete pravidelně, sáhněte po řadě Performance a hledejte popis odolnosti vůči chlóru. U Originals se soustřeďte na pohodlí a vzhled. Plavky z lifestylové řady mohou při intenzivním bazénovém tréninku vydržet kratší dobu, protože chlór pružná vlákna postupně rozkládá.</p>'
          '<h2>Pánské plavky Adidas: šortky, boxerky, jammery</h2>'
          '<p>Pánská nabídka se dělí podle délky a těsnosti. U kraťasů uvádí Adidas často délku v palcích, například 5IN nebo 8IN, a to je velmi praktické vodítko. Číslo označuje délku nohavice od rozkroku, takže vyšší hodnota znamená delší šortky. Kratší střih omezuje tření a hodí se k plavání, delší se používá na pláži a ve vodním sportu, kde potřebujete krytí.</p>'
          '<ul><li><strong>Krátké plavecké šortky (kolem 5 palců):</strong> pohodlné pro bazén, lehké a nebrání kroku.</li>'
          '<li><strong>Delší šortky (kolem 8 palců):</strong> pro pláž, paddleboard a oblečení, které se hodí i na procházku.</li>'
          '<li><strong>Plavky typu trunk:</strong> těsnější střih nad kolena, kompromis mezi pohodlím a hydrodynamikou.</li>'
          '<li><strong>Jammer:</strong> přiléhavý střih po kolena, určený pro trénink a závodní plavání.</li>'
          '<li><strong>Vzorované kraťasy:</strong> módní varianty s potiskem, určené spíš pro dovolenou.</li></ul>'
          '<p>Pokud pravidelně plavete, vyplatí se jammer, protože nepoutá vodu a nebrání tempu. Pokud plavky nosíte při dovolené, ocenění zaslouží šortky s vnitřní podšívkou, které nevyžadují druhé spodní prádlo. Další varianty najdete v přehledu <a href="/panske-plavky/">pánských plavek</a>.</p>'
          '<h2>Dámské plavky Adidas: jednodílné a dvoudílné</h2>'
          '<p>U žen se nabídka dělí na jednodílné plavky, bikiny a samostatné díly. Jednodílné sportovní modely s širšími ramínky a vyšším zády jsou praktické pro bazén, protože při plavání drží a nepohybují se. Bikiny se hodí k pláži, odpočinku a lehčím vodním hrám. Samostatné díly, například vrchní díl bez kostic, umožňují sladit velikost horní a dolní části.</p>'
          + T(['Typ', 'Hodí se na', 'Na co dát pozor'], [
              ['Jednodílné s širšími ramínky', 'pravidelné plavání, aquaaerobik', 'pevné ramínko, které nesklouzává'],
              ['Jednodílné módní', 'dovolená, pláž, večerní koupání', 'střih, který drží při pohybu'],
              ['Bikiny se zavazováním', 'sluneční koupání, odpočinek', 'uvolnění při plavání'],
              ['Vrchní díl s vycpávkami', 'pláž, jemná opora', 'vyjímatelné vložky, schnutí'],
              ['Plavkové kalhotky', 'kombinace dílů', 'výška v bocích, přiléhavost']]) +
          '<p>Při výběru dámských plavek dbejte na střed zad a ramínka, kde se plavky nejvíc namáhají. Při pravidelném plavání zvolte bezpečný střih se zkříženými zády, který nevypadne při obratu. V nabídce najdete i sportovní podprsenky pro koupání, které opticky připomínají plavkový top, ale nejsou vždy určeny pro dlouhé pobývání ve vodě. Podrobnější přehled je v kategorii <a href="/damske-plavky/">dámské plavky</a>.</p>'
          '<h2>Dětské a chlapecké plavky Adidas</h2>'
          '<p>Dětské plavky patří k nejčastějším položkám značky. Chlapci mají plavecké šortky nebo kraťasy, dívky jednodílné nebo dvoudílné plavky. U mladších dětí jsou oblíbené motivy z filmů a komiksů, například Disney a Spider-Man. U starších dětí, které plavou v oddílech, se vyplatí vybrat řadu Performance s pevnějším materiálem a střihem.</p>'
          '<ul><li><strong>Velikost podle výšky:</strong> u dětských plavek se většinou uvádí výška v centimetrech, ne věk. Změřte dítě a porovnejte s tabulkou.</li>'
          '<li><strong>Pružnost:</strong> příliš těsné plavky vadí při pohybu, příliš volné se plní vodou a sjíždějí.</li>'
          '<li><strong>Zapínání:</strong> šortky se šňůrkou nebo gumou, které dítě zvládne samo.</li>'
          '<li><strong>Rychlé schnutí:</strong> pro dovolenou je výhodné vzít dvoje plavky na střídání.</li></ul>'
          '<p>Rodiče by měli počítat s tím, že děti rostou rychle a plavky vydrží jen jednu až dvě sezony. Barevné motivy se po čase vyperou, proto nekupujte příliš velké. Přehled dalších značek najdete v kategorii <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h2>Chlór, slunce a sůl: co plavky ničí</h2>'
          '<p>Chlór v bazénu rozkládá elastická vlákna, takže plavky ztrácejí tvar a stávají se průsvitnými. Slaná voda a slunce vyblednou barvy, ale elastan poškozují méně. Proto se plavky pro časté plavání vyrábějí z materiálů označených jako odolné chlóru. Aby vydržely déle, po plavání je opláchněte čistou vodou a nenechávejte je mokré v tašce.</p>'
          '<ol><li>Po koupání opláchněte plavky ve sladké vodě.</li>'
          '<li>Nemačkejte je silou, jen je jemně vymačkejte.</li>'
          '<li>Sušte ve stínu na vzduchu, ne na radiátoru ani na přímém slunci.</li>'
          '<li>Neperte je s aviváží, na jemném programu nebo ručně.</li>'
          '<li>Neseďte v mokrých plavkách na drsném povrchu, vlákno se snadno trhá.</li></ol>'
          '<h2>Adidas v porovnání s dalšími značkami</h2>'
          '<p>V nabídce Sporteky najdete i jiné značky plavek: ' + B(('speedo', 'Speedo'), ('arena', 'Arena'), ('roxy', 'Roxy'), ('nike', 'Nike'), ('calvin-klein', 'Calvin Klein')) + '. Speedo a Arena jsou tradičně spojeny s plaveckým sportem, Roxy se zaměřuje na surf a plážový styl, Nike a Adidas drží most mezi sportem a módou. Pokud budete plavat často a na vyšší úrovni, prohlédněte si <a href="/speedo-plavky/">plavky Speedo</a> a <a href="/arena-plavky/">plavky Arena</a>. Pro pláž a volný čas je Adidas pohodlnou alternativou, stejně jako <a href="/plavky-nike/">plavky Nike</a>.</p>'
          '<h2>Velikosti a střih u plavek Adidas</h2>'
          '<p>Plavky se musí na těle držet pevněji než běžné oblečení, protože ve vodě se materiál rozpíná a látka se nemá nasávat. Proto vybírejte velikost podle obvodu, ne podle toho, jakou velikost nosíte v tričkách. Ženy měří obvod hrudníku, pasu a boků, muži pas a boky, u dětí rozhoduje výška. Mezi dvěma velikostmi se vyplatí zvolit menší u plavek z pružné pleteniny a větší u šortek se šňůrkou.</p>'
          '<p>Zkoušejte také pohyb: předkloňte se, zvedněte ruce a udělejte dřep. Plavky by neměly sjíždět, tlačit v rozkroku ani ukazovat podšívku. U kraťasů zkontrolujte, zda gumička v pase nedře a zda nohavice nebrání kroku. Na dlouhý den u vody se hodí kapsa na zip, do které schováte klíč.</p>'
          '<h2>Doplňky k plavání</h2>'
          '<p>K plavkám patří i drobnosti, které zlepšují komfort. Při plavání v bazénu se hodí <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plavecké čepice</a>, které chrání vlasy před chlórem. Začátečníkům pomůžou <a href="/plavecke-pomucky/">plavecké pomůcky</a>. Pro zábavu doma se hodí <a href="/bazeny/">bazény</a> a další doplňky. Při přípravě na dovolenou nezapomeňte na druhé plavky na střídání.</p>'
          '<h2>Jak nakupovat plavky Adidas na Sportece</h2>'
          '<p>Při výběru začněte účelem: bazén, pláž, nebo sport. Pak určete pohlaví, velikost a střih, poté porovnejte nabídky obchodů. Hůře dostupné velikosti a barvy se v obchodech střídají, proto mějte připraveno více variant. U plavek se oplatí číst velikostní tabulku, protože označení S, M a L se mezi řadami liší. Při pochybnostech zkontrolujte popis materiálu a doporučené použití u konkrétního kusu. Plavky se z hygienických důvodů často nevracejí, ověřte si podmínky obchodu předem.</p>',
    faq=[
        ('Jaký je rozdíl mezi řadami Performance a Originals?', 'Performance míří na plavání a aktivní vodní sporty, takže důraz je na pevnost, střih a odolnost. Originals vychází z volnočasového stylu, nabízí módnější střihy a vzory pro pláž a dovolenou. Pro pravidelný bazén je praktičtější Performance.'),
        ('Co znamená označení 5IN nebo 8IN u kraťasů?', 'Jde o délku nohavice v palcích od rozkroku. Menší číslo znamená kratší šortky, které méně překážejí při plavání. Větší číslo znamená delší střih, který hodí na pláž nebo paddleboard a nabízí větší krytí.'),
        ('Hodí se plavky Adidas na pravidelné plavání?', 'Ano, zejména modely z řady Performance, které jsou určeny pro bazén. Hledejte popis odolnosti vůči chlóru a přiléhavý střih. Módní kusy z řady Originals jsou spíš pro pláž a občasné koupání.'),
        ('Jak vybrat velikost dětských plavek?', 'Změřte výšku dítěte a porovnejte s tabulkou obchodu, protože dětské velikosti se většinou uvádějí v centimetrech. Příliš těsné plavky vadí při pohybu, příliš volné se plní vodou. Volte raději přiléhavější střih bez zbytečné rezervy.'),
        ('Jak dlouho vydrží plavky při chlorované vodě?', 'Záleží na četnosti plavání a péči. Při pravidelném tréninku vydrží jednu až dvě sezony, při občasném koupání déle. Pomáhá oplachování po každém plavání a sušení ve stínu. Chlór postupně ničí elastická vlákna.'),
        ('Co je jammer?', 'Jammer je přiléhavé pánské plavky po kolena, které snižují odpor vody. Používají se k tréninku a závodění. Pro rekreační plavání jsou pohodlnější trunky nebo krátké šortky, protože mají volnější střih.'),
        ('Dají se plavky prát v pračce?', 'Lepší je ruční praní v čisté vodě. Pokud štítek pračku povoluje, použijte jemný program a ochranný pytlík. Nepoužívejte aviváž, bělidlo ani sušičku. Plavky sušte ve stínu mimo přímý zdroj tepla.'),
        ('Mají dámské jednodílné plavky Adidas vycpávky?', 'Některé modely ano, vždy záleží na konkrétním kusu. Vyjímatelné vložky lze vyndat při praní. Pokud potřebujete větší oporu, hledejte popis, který tuto vlastnost výslovně uvádí, a porovnejte střih ramínek.'),
        ('Mohu na pláž nosit i plavky z řady Performance?', 'Samozřejmě. Plavky Performance jsou pevnější a pohodlně drží, takže se hodí i pro aktivní hry u vody. Jsou jen méně módní než kusy z řady Originals, ale pro dovolenou je pohodlí často důležitější než vzhled.'),
        ('Do kdy se vyplatí kupovat plavky?', 'Nabídka je největší na jaře, před sezonou. Vybraná velikost a barva se pak postupně rozprodává. Pokud potřebujete konkrétní model, nakupujte dříve. Po sezoně se zboží z minulých kolekcí častěji objevuje ve slevě, ale s menším výběrem.'),
    ])
