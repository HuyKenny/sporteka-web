"""sporteka.cz — wave 15b (4. 11. 2026): long texts (>= 1650 words) for soupravy, joga-a-pilates, lyzarske-rukavice, proteiny.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ soupravy
NEW['soupravy'] = dict(long=True,
    title='Sportovní soupravy a komplety | Porovnání nabídek',
    desc='Tepláková souprava, tréninkový komplet, dětská i fitness souprava: materiály, střihy a velikosti. Nabídky českých obchodů vedle sebe na Sportece.',
    intro='<p><strong>Sportovní souprava</strong> spojuje svrchní díl, tedy mikinu, bundu nebo tričko, s kalhotami či kraťasy ve stejném provedení. Výhoda je jasná: barvy, látka i střih k sobě ladí, nemusíte nic kombinovat a oblečení vypadá jednotně na tréninku, v šatně i cestou domů. Cena za komplet bývá navíc výhodnější než nákup dílů zvlášť.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a uvidíte soupravy pro muže, ženy i děti. Pokud skládáte vlastní kombinaci, podívejte se i na <a href="/teplaky/">tepláky</a>, <a href="/mikiny/">mikiny</a>, <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/sportovni-bundy/">sportovní bundy</a>. Níže najdete průvodce typy souprav, materiály, velikostmi a péčí.</p>',
    guide='<h2>Co všechno se skrývá pod pojmem souprava</h2>'
          '<p>Slovo souprava používají obchody pro velmi různé výrobky. Někde je to klasická tepláková souprava na doma, jinde sada s dresem pro oddíl, jinde dvoudílný fitness komplet. Než začnete porovnávat, ujasněte si, k čemu ji budete nosit. Souprava určená na běžný volný čas totiž nemá stejné nároky na materiál ani střih jako souprava, ve které se denně trénuje.</p>'
          + T(['Typ', 'Co obvykle obsahuje', 'Pro koho a kdy'], [
              ['Tepláková souprava', 'mikina nebo bunda se zipem a tepláky', 'volný čas, cestování, zahřátí před výkonem'],
              ['Tréninková souprava', 'lehká bunda a kalhoty z polyesteru', 'týmy, školní tělocvik, venkovní trénink'],
              ['Fitness komplet', 'top nebo podprsenka a legíny či kraťasy', 'posilovna, jóga, skupinová cvičení'],
              ['Běžecký komplet', 'tričko nebo tílko a kraťasy', 'běh a lehká vytrvalost v teple'],
              ['Dětská souprava', 'mikina a kalhoty s pevnějším střihem', 'škola, hřiště, kroužky'],
              ['Zimní souprava', 'zateplená bunda a kalhoty', 'sport a pobyt venku v chladu']]) +
          '<h2>Materiály: bavlna, polyester a směsi</h2>'
          '<p>Materiál rozhoduje o tom, jak se souprava nosí po hodině pohybu. <strong>Bavlna</strong> je měkká a příjemná na kůži, ale nasaje vodu a pomalu schne. Pro klidné nošení a lehké cvičení je v pořádku, na intenzivní trénink se hodí hůř. <strong>Polyester</strong> odvádí vlhkost od těla a rychle schne, proto ho najdete u tréninkových souprav. Může být méně příjemný na dotek a po delší době nošení více drží pach.</p>'
          '<p>Směsové materiály, třeba bavlna s polyesterem a trochou elastanu, hledají kompromis. Jsou pružnější, lépe drží tvar a méně se mačkají. U fitness kompletů se objevuje elastan nebo lycra pro přilnavost a pohyblivost. Údaje o složení najdete na štítku nebo v popisu produktu, nespoléhejte jen na obecné označení „sportovní“.</p>'
          '<h3>Úplet, froté a fleece</h3>'
          '<ul><li><strong>Úplet hladký</strong> je tenčí a hodí se do teplejšího počasí nebo pod bundu.</li>'
          '<li><strong>Froté a počesaná vnitřní strana</strong> hřeje, ale je objemnější a pomaleji schne.</li>'
          '<li><strong>Fleece</strong> je lehký a teplý, najdete ho u zimnějších souprav, příbuzné jsou <a href="/fleecove-mikiny/">fleecové mikiny</a>.</li>'
          '<li><strong>Technické tkaniny</strong> používané u tréninkových souprav mají hladký povrch a odolávají větru.</li></ul>'
          '<h2>Střih a konstrukce, na kterých záleží</h2>'
          '<p>Střih ovlivňuje pohodlí víc než samotný materiál. Volnější střih nechává prostor pro pohyb a vrstvení, přiléhavý střih omezuje poletování látky při běhu nebo cvičení. U tepláků sledujte, zda mají na konci nohavic manžetu, nebo rovný střih. Manžeta drží kalhoty nad kotníkem a hodí se na tréninky venku, rovná nohavice vypadá společensky a pohodlněji se obouvá přes boty.</p>'
          '<ul><li><strong>Zip:</strong> kovový nebo kvalitní plastový zip vydrží víc zapínání. Zip po celé délce dovoluje bundu rychle sundat při zahřátí.</li>'
          '<li><strong>Kapsy:</strong> na zip jsou bezpečnější pro klíče a telefon, otevřené kapsy se hodí do volného času.</li>'
          '<li><strong>Pas:</strong> pevná guma se šňůrkou drží lépe než samotná guma, zvlášť při skocích a sprintech.</li>'
          '<li><strong>Kolena a lokty:</strong> zesílení nebo ohýbaný střih pomáhá hlavně u dětských souprav.</li>'
          '<li><strong>Kapuce:</strong> praktická při chladu, při sportu s míčem ale překáží a při běhu se může zvedat a zasahovat do výhledu.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Souprava má dva díly a každý může sedět jinak. Mnozí lidé potřebují horní díl o číslo jiný než dolní, a proto se vyplatí ověřit, zda obchod dovoluje koupit díly v různých velikostech. Pokud ne, rozhodujte se podle většího problému: kalhoty se dají zkrátit nebo zúžit snáz než bunda v ramenou.</p>'
          + T(['Míra', 'Jak měřit', 'Poznámka'], [
              ['Hrudník', 'v nejširším místě přes prsa a lopatky', 'pro horní díl, u zateplených souprav přidejte rezervu na vrstvu pod ní'],
              ['Pas', 'v nejužším místě trupu', 'u tepláků dobře poslouží pas se šňůrkou'],
              ['Boky', 'v nejširším místě', 'u přiléhavých střihů a legín'],
              ['Délka nohavice', 'od rozkroku ke kotníku', 'u dětí počítejte s růstem, manžeta pomůže'],
              ['Délka rukávu', 'od ramene k zápěstí', 'při zvednuté paži se rukáv nemá vyhrnout']]) +
          '<p>Značky mají různé velikostní tabulky, a stejné označení M proto nemusí znamenat totéž. Podívejte se na tabulku v detailu produktu a porovnejte ji se svým nejlépe sedícím oblečením. Pomůže i recenze jiných kupujících, kteří často píší, zda velikost vychází větší, nebo menší.</p>'
          '<h2>Soupravy podle sportu a činnosti</h2>'
          '<ul><li><strong>Fotbal, házená a florbal:</strong> lehké tréninkové soupravy z polyesteru, k nim <a href="/dresy/">dresy</a> a při chladu mikina. Přehled sportů najdete v kategoriích <a href="/fotbal/">fotbal</a> a <a href="/florbal/">florbal</a>.</li>'
          '<li><strong>Posilovna a cvičení:</strong> přiléhavé komplety s <a href="/leginy/">legínami</a> a <a href="/sportovni-podprsenky/">sportovní podprsenkou</a> nebo topem, viz také <a href="/fitness/">fitness</a>.</li>'
          '<li><strong>Bojové sporty:</strong> speciální komplety a kimona jsou v oddílu <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a>.</li>'
          '<li><strong>Cyklistika:</strong> dres s kalhotami je samostatný sortiment, hledejte v <a href="/cyklisticke-obleceni/">cyklistickém oblečení</a>.</li>'
          '<li><strong>Zimní sporty:</strong> lyžařské komplety a overaly patří do <a href="/lyzarske-obleceni/">lyžařského oblečení</a>, běžná tepláková souprava na svah nestačí.</li>'
          '<li><strong>Plavání a pláž:</strong> pro vodu se používají <a href="/plavky/">plavky</a>, ne souprava s bavlněným oblečením.</li></ul>'
          '<h2>Dětské soupravy</h2>'
          '<p>Děti soupravy nosí denně a v rychlém tempu je rychle zašpiní a odřou, takže se u nich vyplatí robustnost. Hledejte zesílená kolena, kvalitní šití a materiál, který snese časté praní. Příliš hladká látka na kolenou rychle protře, počesaná vnitřní strana se naopak po opakovaném praní může zacuchat. Nastavitelný pas a manžety na nohavicích prodlouží dobu, kdy souprava dítěti padne.</p>'
          '<p>Při koupi dětské velikosti nepřeceňujte „na růst“. Velká souprava překáží při hře a děti v ní vypadají neuspořádaně. Rozumná rezerva je jedna velikost, ne dvě. U menších dětí pomáhá, když se kalhoty zapínají jednoduše a mají měkký pas. Starší děti ocení styl, který se jim líbí, protože soupravu skutečně obléknou.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete mimo jiné ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('peak-mountain', 'Peak Mountain'), ('under-armour', 'Under Armour'), ('new-balance', 'New Balance'), ('joma', 'Joma'), ('helly-hansen', 'Helly Hansen'), ('viking', 'Viking')) + '. Velké sportovní značky mají silné zastoupení u volnočasových a týmových souprav, Joma se prosazuje u kolektivních sportů. Helly Hansen a Viking jsou známé spíše outdoorovými a zimními produkty, proto u nich uvidíte teplejší varianty. Značka sama kvalitu nezaručí, vždy sledujte materiál a zpracování.</p>'
          '<h2>Péče o soupravu</h2>'
          '<p>Správná péče prodlouží život barvám i tvaru. Soupravu perte obrácenou naruby, aby se potisky a vlákna zbytečně neodíraly. Funkční polyester perte bez aviváže, která zalepuje vlákna a snižuje schopnost odvádět vlhkost. Bavlnu stačí prát podle štítku, nejčastěji na 30 až 40 °C. Tmavé barvy perte zvlášť, aby nepouštěly na světlé díly.</p>'
          '<p>Zip před praním zavřete, aby neškrábal ostatní prádlo, a suchá souprava se nemá žehlit přes potisk. Při sušení nepoužívejte horký vzduch, který zmenšuje bavlnu a poškozuje elastické části. Stačí pověsit na ramínko nebo přes šňůru. Pokud na soupravě máte reflexní nebo gumový potisk, řiďte se pokyny na štítku, protože v běžné pračce nemusí vydržet.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit soupravu podle barvy a nezkontrolovat materiál, takže trénink v bavlněných teplácích končí promoklým oblečením.</li>'
          '<li>Spoléhat na označení velikosti bez přečtení tabulky konkrétního výrobce.</li>'
          '<li>Zvolit příliš těsný střih na vrstvení a pak nemít pod ním kam dát tričko.</li>'
          '<li>Pořídit dětskou soupravu o dvě čísla větší, v níž se dítě nemůže pohodlně hýbat.</li>'
          '<li>Prát funkční materiál s aviváží, a ztratit tak jeho schopnost odvádět pot.</li>'
          '<li>Nezkontrolovat, zda je prodáván celý komplet, nebo jen jeden díl.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Použijte filtr podle pohlaví, značky a velikosti. U každé soupravy klikněte na detail a prohlédněte si nabídky obchodů. Rozdíl nemusí být jen v ceně, liší se dostupností velikostí, dopravou a možností vrácení. Ověřte, že obchod prodává komplet, a zjistěte, zda lze velikosti horního a dolního dílu kombinovat. Pokud souprava není skladem, sledujte další obchody a zvažte podobný model.</p>'
          '<p>Chcete-li kompletní sportovní výbavu, doplňte soupravu o <a href="/sportovni-ponozky/">sportovní ponožky</a>, <a href="/sportovni-tasky/">sportovní tašky</a> a vhodnou <a href="/sportovni-obuv/">sportovní obuv</a>. Celý sortiment najdete v kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>',
    faq=[('Co obsahuje sportovní souprava?', 'Obvykle mikinu, bundu nebo tričko a k tomu kalhoty nebo kraťasy ve stejném provedení. Některé sady obsahují i čepici nebo tašku. Přesné složení vždy ověřte v popisu produktu, protože obchody používají slovo souprava i pro jednotlivé díly.'),
         ('Hodí se tepláková souprava na sport?', 'Na lehké cvičení a zahřátí ano. Na intenzivní trénink je lepší polyesterová souprava, která odvádí pot a rychleji schne. Bavlněná souprava se po zpocení lepí na tělo a nepříjemně chladí.'),
         ('Mohu koupit horní a dolní díl v různé velikosti?', 'Záleží na obchodě. Některé nabízejí díly samostatně, jiné jen jako celek. Pokud potřebujete kombinaci velikostí, zkuste vyhledat jednotlivé kusy v kategoriích mikin a tepláků nebo se zeptejte prodejce.'),
         ('Jaký materiál zvolit do posilovny?', 'Pružný materiál s příměsí elastanu nebo polyester, který odvádí vlhkost. Přiléhavý střih se nezachytí o stroje. Bavlna je v pořádku na pomalejší cvičení nebo domácí využití.'),
         ('Jak vybrat dětskou soupravu?', 'Hledejte pevný materiál, zesílená kolena a nastavitelný pas nebo manžety. Velikost volte maximálně o jedno číslo větší. Dítě musí mít v kalhotách volné pohyby při lezení a běhu.'),
         ('Jak soupravu prát?', 'Řiďte se štítkem. Obvykle naruby, na 30 až 40 °C, bez aviváže u funkčních materiálů. Zip zavřete, potisk nežehlete a nesušte při vysoké teplotě.'),
         ('Jak poznat, že velikost odpovídá?', 'Porovnejte vlastní míry s tabulkou výrobce a přečtěte si recenze. Horní díl nemá tlačit v ramenou, kalhoty mají mít dost místa v bocích a zůstat v pase. Stejné označení u dvou značek může znamenat jiný rozměr.'),
         ('Je lepší souprava, nebo samostatné díly?', 'Souprava je pohodlná a vypadá jednotně. Samostatné díly jsou vhodné, pokud máte nestandardní míry nebo chcete střídat barvy. Obojí najdete porovnané na Sportece.'),
         ('Hodí se souprava na zimu?', 'Zimní soupravy se zateplením jsou vhodné na lehký pohyb v chladu. Do lyžařského terénu potřebujete specializovanou výbavu s membránou, najdete ji v lyžařském oblečení. Vrstvení funkčním termoprádlem pomůže u obou řešení.')],
)

# ------------------------------------------------------------------ joga-a-pilates
NEW['joga-a-pilates'] = dict(long=True,
    title='Jóga, pilates a meditace: podložky a pomůcky',
    desc='Podložky, bloky, popruhy, pilates míče a meditační polštáře: jak vybrat podle cvičení a materiálu. Nabídky českých obchodů vedle sebe na Sportece.',
    intro='<p><strong>Jóga, pilates a meditace</strong> vyžadují překvapivě málo vybavení, ale to, co používáte, výrazně ovlivní pohodlí i bezpečí cvičení. Špatná podložka klouže, příliš tenká zatěžuje kolena a nevhodný polštář způsobí, že u meditace vydržíte sedět jen pár minut. Naopak dobře zvolená výbava vás nechá soustředit se na samotné cvičení.</p>'
          '<p>Na Sportece najdete <a href="/joga-a-podlozky/">jógové podložky</a>, <a href="/jogove-pomucky/">jógové bloky, popruhy a bolstery</a>, <a href="/pilates-pomucky/">pilates pomůcky</a> i <a href="/meditace/">meditační polštáře a pomůcky</a>. Nabídky českých obchodů porovnáte vedle sebe a níže najdete průvodce, který vám pomůže vybrat, co k vašemu stylu cvičení opravdu potřebujete.</p>',
    guide='<h2>Co potřebujete na začátek a co můžete přidat později</h2>'
          '<p>Začátečníkovi stačí podložka a pohodlné oblečení. Všechno ostatní je volitelné a hodí se, až zjistíte, co vám při cvičení chybí. Pokud se vám třeba nedaří dosáhnout rukama k zemi, přidáte blok. Pokud potřebujete prohloubit strečink nohou, pomůže popruh. Pilates míče a kruhy se objeví, až budete chtít zapojit hlubší svalstvo.</p>'
          + T(['Pomůcka', 'K čemu slouží', 'Kdy se vyplatí'], [
              ['Podložka', 'tlumení a přilnavost k zemi', 'od prvního cvičení'],
              ['Jógový blok', 'zkrácení vzdálenosti k zemi, opora', 'při omezené pohyblivosti nebo pro přesnější pozice'],
              ['Popruh', 'prodloužení paží při strečinku', 'při předklonech a práci s nohama'],
              ['Bolster', 'podpora při odpočinkových pozicích', 'při regeneraci a pomalé józe'],
              ['Pilates míč', 'nestabilní plocha pro zapojení středu těla', 'při posilování a rehabilitačním cvičení'],
              ['Pilates kruh a gumy', 'odpor pro posilování', 'u pokročilejšího cvičení'],
              ['Meditační polštář', 'pohodlné sezení s rovnými zády', 'při pravidelné meditaci']]) +
          '<h2>Jak vybrat podložku</h2>'
          '<p>Podložka je jádro výbavy a stojí za to jí věnovat nejvíc pozornosti. Rozhodují čtyři vlastnosti: tloušťka, materiál, povrch a rozměr.</p>'
          '<h3>Tloušťka</h3>'
          '<p>Tenká podložka dává lepší kontakt se zemí a stabilitu při stoji a rovnováze. Silnější tlumí kolena, zápěstí a páteř při pozicích na čtyřech nebo vleže. Typická jógová podložka bývá o několik milimetrů silná, pilates podložky se dělají silnější, protože se hodně leží na zádech a boku. Příliš měkká podložka znejistí stoje, proto nepřehánějte tloušťku.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>PVC</strong> je odolné, dobře drží a snadno se čistí. Je těžší a méně ekologické.</li>'
          '<li><strong>TPE</strong> je lehčí, měkčí a recyklovatelné, avšak rychleji se opotřebuje.</li>'
          '<li><strong>Přírodní kaučuk</strong> nabízí výbornou přilnavost, zejména za vlhka. Může mít výraznější vůni a nehodí se pro lidi s alergií na latex.</li>'
          '<li><strong>Korek a bavlna</strong> se kombinují s jiným materiálem a poskytují příjemný povrch na pot.</li>'
          '<li><strong>Pěnové podložky</strong> jsou nejměkčí a hodí se na cvičení na zemi, méně na jógu ve stoji.</li></ul>'
          '<h3>Povrch a rozměr</h3>'
          '<p>Protiskluzový texturovaný povrch je důležitý u dynamických stylů, kde se pohybujete a potíte. Hladká podložka se lépe čistí, ale může klouzat. Standardní délka stačí většině lidí, vyšší cvičenci by měli hledat delší a širší verzi, aby jim při leže nepřečníval krk nebo chodidla. Přidaná taška nebo popruh na nošení se hodí, pokud na cvičení cestujete.</p>'
          '<h2>Jógové pomůcky podrobněji</h2>'
          '<p>Blok bývá z pěny, korku nebo dřeva. Pěnový je lehký a měkčí, korkový a dřevěný jsou stabilnější a těžší. Hodí se pod ruce při polohách ve stoji, pod sedací kosti nebo jako opora při předklonu. Popruh se vybírá podle délky a typu spony: kovová D spona drží pevně, plastová je lehčí. Bolster je podlouhlý polštář pro podporu zad a nohou při pomalejších, regeneračních pozicích. Všechny tyto věci najdete v kategorii <a href="/jogove-pomucky/">jógové bloky, popruhy a bolstery</a>.</p>'
          '<h2>Pilates pomůcky</h2>'
          '<p>Pilates klade důraz na střed těla, kontrolu pohybu a správné dýchání. Pomůcky slouží hlavně k přidání odporu nebo nestability. Malý měkký míč se dává mezi kolena nebo pod záda, velký míč nahrazuje židli nebo lavici. Pilates kruh přidává odpor při tlaku a tahu, gumy se hodí na cvičení pro paže a nohy. Aktuální nabídku najdete v kategorii <a href="/pilates-pomucky/">pilates pomůcky</a>, kde jsou hlavně podložky, míče a kruhy. K posilování se hodí i <a href="/posilovaci-gumy/">posilovací gumy</a>, k masáži fasciální <a href="/masazni-pomucky/">masážní pomůcky</a> a při domácím cvičení také <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>'
          '<h2>Balanční prvky a doplňky</h2>'
          '<p>Pokud chcete trénovat rovnováhu, podívejte se na <a href="/balancni-pomucky/">balanční pomůcky</a>, například podložky a polokoule. K cvičení se hodí i <a href="/fitness-pomucky/">fitness pomůcky</a>, například činky a švihadla. Na protažení po zátěži pomáhá masážní válec, který je v oddílu masážních pomůcek.</p>'
          '<h2>Meditace: polštář, podložka, lavička</h2>'
          '<p>Meditace se obvykle dělá vsedě, a proto je klíčové pohodlí v kyčlích a zádech. Meditační polštář, často plněný pohankovými slupkami nebo kapokem, zvedá pánev nad kolena, takže se páteř přirozeně narovná. Kulatý polštář zvaný zafu se hodí pro sezení se zkříženýma nohama, zabuton je plochá podložka pod něj. Lavička umožňuje klečet a odlehčuje kolena. Pokud sedíte na židli, stačí dobrá opora zad a rovná plocha. Vyberte si podle toho, jak dlouho vydržíte sedět bez bolesti. Všechny varianty jsou v kategorii <a href="/meditace/">meditace</a>.</p>'
          '<h2>Co na sebe a co dalšího se hodí</h2>'
          '<p>Na jógu a pilates se nosí přiléhavé nebo pružné oblečení, které se nehrne při pozicích. Oblíbené jsou <a href="/leginy/">legíny</a>, <a href="/sportovni-podprsenky/">sportovní podprsenky</a> a <a href="/sportovni-tricka/">trička a tílka</a> z elastického materiálu. Na cvičení se chodí naboso, případně v protiskluzových ponožkách. Pro přenášení podložky a pomůcek slouží <a href="/sportovni-tasky/">sportovní tašky</a>. Po cvičení pomůže láhev z kategorie <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>'
          '<h2>Podle stylu cvičení</h2>'
          + T(['Styl', 'Doporučená výbava', 'Poznámka'], [
              ['Klidná hatha jóga', 'střední podložka, blok, popruh', 'stabilita je důležitější než měkkost'],
              ['Dynamická jóga (vinyasa)', 'protiskluzová podložka s dobrou přilnavostí', 'pot zhoršuje klouzání na hladkém povrchu'],
              ['Regenerační jóga', 'bolster, deka, blok', 'záleží na pohodlné opoře těla'],
              ['Pilates na podložce', 'silnější podložka, míč, kruh', 'tlumení pro páteř a lopatky'],
              ['Meditace', 'polštář, lavička nebo židle', 'pohodlí ve vsedě rozhoduje o délce praxe'],
              ['Cvičení doma s dětmi', 'větší podložka, pěnová varianta', 'ocení se snadné čištění']]) +
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce jsou například ' + B(('merco', 'Merco'), ('hms', 'HMS'), ('sportago', 'Sportago'), ('insportline', 'Insportline'), ('lifefit', 'Lifefit'), ('bodhi', 'Bodhi'), ('manduka', 'Manduka'), ('myga', 'Myga'), ('casall', 'Casall'), ('adidas', 'Adidas')) + '. Merco, HMS, Sportago, Insportline a Lifefit nabízejí širokou škálu cenově dostupných podložek i pomůcek. Bodhi, Manduka a Myga se zaměřují přímo na jógu a často používají kvalitnější materiály. Casall je skandinávská značka s důrazem na funkci a vzhled. Značka sama nic nezaručuje, sledujte materiál, tloušťku a hodnocení kupujících.</p>'
          '<h2>Péče o podložku a pomůcky</h2>'
          '<p>Podložku po cvičení otřete vlhkým hadříkem s jemným mýdlem nebo speciálním čisticím sprejem. Nepoužívejte agresivní čističe a alkohol, které povrch vysušují. Nechte ji dobře vyschnout a pak ji srolujte povrchem ven, aby se nekroutily okraje. Nenechávejte ji dlouho na přímém slunci ani v horkém autě, kde se materiál deformuje. Podložka z přírodního kaučuku se může časem mírně měnit barvu, což je normální.</p>'
          '<p>Pěnové bloky otřete a nechte oschnout, korkové stačí otřít vlhkým hadrem. Popruhy a povlaky na polštářích se perou podle štítku. Polštáře s pohankou nikdy neperte celé, vyjměte náplň a perte jen povlak.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupit příliš tlustou měkkou podložku a pak se divit, že ve stoji nestabilní.</li>'
          '<li>Ušetřit na přilnavosti, což se vymstí hlavně při dynamické józe.</li>'
          '<li>Zvolit krátkou podložku pro vysokou postavu.</li>'
          '<li>Pořídit velkou sadu pomůcek najednou, aniž byste znali svůj styl.</li>'
          '<li>Zapomenout na alergii na latex u kaučukových materiálů.</li>'
          '<li>Meditovat bez opory a pak se vzdát, protože bolí záda.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Vyberte podkategorii a zúžte nabídku podle značky. U každé položky najdete nabídky několika obchodů. Porovnávejte nejen cenu, ale i rozměry, tloušťku a materiál, protože podobně vypadající podložky se mohou výrazně lišit. Dobré je také zkontrolovat dopravu, protože objemné zboží se někdy vyplatí vyzvednout osobně. Při pochybnostech si přečtěte popis a recenze.</p>',
    faq=[('Jaká podložka na jógu je nejlepší pro začátečníka?', 'Taková, která dobře drží a není příliš měkká. Obecně se osvědčuje střední tloušťka s protiskluzovým povrchem. Začátečník potřebuje hlavně stabilitu při základních pozicích ve stoji.'),
         ('Jaký je rozdíl mezi jógovou a pilates podložkou?', 'Pilates podložka bývá silnější, protože se při cvičení hodně leží na zádech a boku. Jógová je tenčí a přilnavější, aby se na ní dalo bezpečně stát. Pro univerzální využití se hodí střední tloušťka.'),
         ('K čemu slouží jógový blok?', 'Zkracuje vzdálenost k zemi, takže se dostanete do pozice bez přetěžování. Může sloužit jako opora pod ruce, pod sedací kosti nebo mezi kolena. Neznamená, že cvičíte špatně, ale že cvičíte pohodlněji.'),
         ('Potřebuji speciální vybavení na pilates?', 'Pro začátek stačí podložka. Míč, kruh nebo gumy přidejte, až budete chtít cvičení zpestřit nebo zvýšit odpor.'),
         ('Jak podložku čistit?', 'Otřete ji vlhkým hadříkem s jemným mýdlem, nechte vyschnout a srolujte. Vyhněte se alkoholu a agresivním čističům, které poškozují povrch.'),
         ('Jaký materiál podložky vybrat?', 'PVC je odolné a cenově dostupné, TPE lehčí a měkčí, přírodní kaučuk nabízí vynikající přilnavost. Při alergii na latex kaučuk nevolte.'),
         ('Jak vybrat meditační polštář?', 'Zvolte takový, který zvedne pánev nad kolena a umožní rovná záda. Plnění z pohankových slupek se přizpůsobí tvaru těla, kapok je lehčí. Vyzkoušejte, jak dlouho na něm vydržíte sedět.'),
         ('Hodí se podložka i na cvičení na koberci?', 'Ano, podložka zlepší přilnavost a poskytne oporu. Na hladké podlaze pomůže protiskluzová vrstva pod ní. Zkontrolujte, zda se podložka nesesouvá.'),
         ('Kolik pomůcek si koupit?', 'Začněte podložkou a jednou pomůckou podle potřeby, například blokem. Další přidejte až po několika týdnech, kdy zjistíte, co vám při cvičení chybí.'),
         ('Jak skladovat podložku?', 'Srolovanou nebo složenou na suchém místě bez přímého slunce a horka. Nepokládejte na ni těžké předměty, které by ji trvale zdeformovaly.')],
)

# ------------------------------------------------------------------ lyzarske-rukavice
NEW['lyzarske-rukavice'] = dict(long=True,
    title='Lyžařské rukavice a palčáky: výběr | Sporteka',
    desc='Lyžařské a snowboardové rukavice a palčáky pro muže, ženy i děti: membrána, izolace, velikost a péče. Nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Lyžařské rukavice</strong> mají jediný úkol, který je ale náročný: udržet ruce v teple a suchu při pohybu ve sněhu, větru a mrazu. Ruce patří k částem těla, které mrznou jako první, protože jsou hodně vystavené větru a chladu a kůže na nich má málo izolace. Nevhodné rukavice proto dokážou zkazit celý den na svahu.</p>'
          '<p>Na Sportece porovnáte <strong>lyžařské rukavice a palčáky</strong> pánské, dámské i dětské z nabídek českých obchodů. Další výbavu najdete v kategoriích <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/lyzarske-doplnky/">lyžařské doplňky</a>. Průvodce níže shrnuje, na co se při výběru dívat.</p>',
    guide='<h2>Prstové rukavice, nebo palčáky</h2>'
          '<p>První rozhodnutí je mezi prsty a palčáky. Prstové rukavice dávají lepší cit, snadno se s nimi uchopí hůl, zip i telefon. Palčáky mají prsty pohromadě, takže se navzájem ohřívají a jsou při stejné izolaci teplejší. Tato volba není otázkou módy, ale vašeho typu rukou a způsobu lyžování.</p>'
          + T(['Typ', 'Výhody', 'Nevýhody', 'Hodí se pro'], [
              ['Prstové rukavice', 'cit, úchop, obratnost', 'chladnější při stejné izolaci', 'aktivní lyžaře, snowboardisty, práci se zipy'],
              ['Palčáky', 'teplejší, jednoduché', 'horší úchop drobností', 'mrazivé dny, lidi s chladnýma rukama, malé děti'],
              ['3v1 rukavice', 'vnější shell a vnitřní fleecová rukavice', 'objemnější', 'proměnlivé počasí a celou sezónu'],
              ['Tenké rukavice', 'lehké, na ohřátí a teplejší dny', 'nejsou do silného mrazu', 'jarní lyžování, vrstvení pod silnější rukavice'],
              ['Rukavice na běžky', 'prodyšné, lehké', 'méně izolace', 'běžecké lyžování, viz <a href="/bezecke-lyzovani/">běžecké lyžování</a>']]) +
          '<h2>Konstrukce: vrstvy, které dělají rukavici funkční</h2>'
          '<p>Kvalitní lyžařská rukavice je několikavrstvá. Vnější materiál chrání proti větru a oděru, uprostřed bývá membrána, pak izolace a uvnitř podšívka. Všechny části spolu musejí fungovat, jinak se rukavice buď prohřeje a zapotí ruku, nebo naopak promokne.</p>'
          '<h3>Vnější materiál</h3>'
          '<p>Nylon a polyester jsou lehké a vodoodpudivé, kůže je odolná a dobře drží, ale potřebuje impregnaci a pomalu schne. Dlaň často bývá z kůže nebo syntetické kůže, která zlepšuje úchop hole a odolává otěru při pádech. Zesílení na zápěstí a mezi prsty zvyšuje životnost místa, které se opotřebuje nejdřív.</p>'
          '<h3>Membrána a voděodolnost</h3>'
          '<p>Membrána zabraňuje průniku vody, ale pustí ven vodní páru z potu. Vodoodpudivá úprava povrchu jen zpomaluje promoknutí, nenahrazuje membránu. U rukavic hledejte uvedenou vodní odolnost nebo zmínku o membráně. U vysokého zápěstí hlídejte, aby voda nevtekla dovnitř. Sníh se do rukavice dostane nejčastěji přes manžetu.</p>'
          '<h3>Izolace a podšívka</h3>'
          '<p>Izolace zadržuje vzduch a tím hřeje. Syntetická výplň se hodí do vlhka, protože zůstává funkční i při zvlhnutí, peří je lehčí a teplejší, ale při namočení ztrácí účinek. Vnitřní podšívka z fleecu nebo vlny je příjemná na dotek a odvádí pot. Příliš silná izolace v těsné rukavici ale naopak chladí, protože stlačuje vzduch.</p>'
          '<h2>Délka manžety a zapínání</h2>'
          '<ul><li><strong>Dlouhá manžeta</strong> se natahuje přes rukáv bundy a zabraňuje vniknutí sněhu. Hodí se pro hlubší sníh a snowboard.</li>'
          '<li><strong>Krátká manžeta</strong> se schová pod rukáv. Je pohodlná, ale méně chrání před sněhem.</li>'
          '<li><strong>Stahovací šňůrka nebo suchý zip</strong> dotáhne zápěstí a drží rukavici na ruce.</li>'
          '<li><strong>Poutko nebo karabinka</strong> usnadní spárování rukavic a zavěšení na batoh.</li>'
          '<li><strong>Šňůrka s popruhem</strong> brání ztrátě rukavice při svlékání, což oceníte u dětí.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Správná velikost je klíčová: příliš těsná rukavice stlačuje ruku a tím zhoršuje prokrvení, příliš volná nehřeje a zhoršuje úchop. Změřte obvod dlaně v nejširším místě pod prsty bez palce a porovnejte s tabulkou výrobce. Konečky prstů se mají lehce dotýkat konce rukavice, ale nesmějí se tlačit.</p>'
          + T(['Obvod dlaně', 'Orientační velikost', 'Poznámka'], [
              ['do cca 18 cm', 'XS nebo dětské', 'u dětí řiďte se výškou i věkem'],
              ['cca 18–20 cm', 'S', 'užší ruka'],
              ['cca 20–22 cm', 'M', 'běžná dámská nebo štíhlá pánská ruka'],
              ['cca 22–24 cm', 'L', 'běžná pánská ruka'],
              ['nad 24 cm', 'XL a větší', 'širší ruka, delší prsty']]) +
          '<p>Značky mají různé střihy a tabulky, proto se v detailu produktu podívejte na pokyny konkrétního výrobce. Při koupi zkuste sevřít pěst a uchopit hůl nebo předmět podobné tloušťky. Švy nesmějí tlačit na prsty a palec se nesmí kroutit.</p>'
          '<h2>Rukavice pro děti</h2>'
          '<p>Dětské ruce chladnou rychleji a nezvládají jemné zapínání, takže se vyplatí volit jednoduché typy. Palčáky jsou obvykle nejlepší volba, protože jsou teplé a snadno se oblékají. Pomůže široká manžeta, kterou lze navléknout přes rukáv, a stahování suchým zipem. Šňůrka mezi rukavicemi zabrání ztrátě. Pokud dítě lyžuje celý den, vezměte druhý pár na výměnu. Mokrá rukavice hřeje výrazně hůř, proto mějte po ruce suché.</p>'
          '<p>K dětské výbavě patří také <a href="/detske-lyze/">dětské lyže</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/lyzarske-bryle/">lyžařské brýle</a>. Pro hry ve sněhu se hodí i <a href="/sane-a-boby/">sáně a boby</a>.</p>'
          '<h2>Rukavice podle sportu</h2>'
          '<ul><li><strong>Sjezdové lyžování:</strong> teplé a odolné rukavice s vyztuženou dlaní, k nim <a href="/lyzarske-hole/">lyžařské hole</a>.</li>'
          '<li><strong>Snowboarding:</strong> rukavice s dlouhou manžetou a zesílenou dlaní, často s ochranou zápěstí, doplňují <a href="/snowboardove-chranice/">snowboardové chrániče</a>.</li>'
          '<li><strong>Skialpinismus:</strong> lehčí prodyšné rukavice, protože při stoupání se zapotíte, více v kategorii <a href="/skialpinismus/">skialpinismus</a>.</li>'
          '<li><strong>Běžky:</strong> tenčí rukavice s dobrým úchopem hole.</li>'
          '<li><strong>Zimní turistika:</strong> univerzální rukavice, případně palčáky na zahřátí, vedle <a href="/trekove-hole/">trekových holí</a>.</li>'
          '<li><strong>Jiné sporty:</strong> pro běh nebo kolo se hodí tenčí <a href="/sportovni-rukavice/">sportovní rukavice</a> nebo <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>.</li></ul>'
          '<h2>Vrstvení a doplňky</h2>'
          '<p>Ruce se dají zahřát i vrstvením. Tenká vnitřní rukavice z merina nebo syntetiky pod silnější vnější zlepšuje izolaci a umožňuje na chvíli sundat tlustou rukavici bez ztráty tepla. K tomu patří zahřívací sáčky, které se vkládají dovnitř při velkých mrazech. Dobře izolovaná výbava celého těla pomáhá rukám: kompletní oblečení najdete v <a href="/lyzarske-obleceni/">lyžařském oblečení</a>, včetně <a href="/lyzarske-bundy/">bund</a> a <a href="/lyzarske-kalhoty/">kalhot</a>. Teplo drží i <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete ' + B(('viking', 'Viking'), ('rossignol', 'Rossignol'), ('ziener', 'Ziener'), ('hestra', 'Hestra'), ('reusch', 'Reusch'), ('leki', 'Leki'), ('reima', 'Reima'), ('relax', 'Relax'), ('level', 'Level'), ('roeckl', 'Roeckl')) + '. Viking a Rossignol mají největší nabídku, Hestra a Reusch jsou známé specializací na rukavice, Leki spojuje rukavice s hůlkami. Reima a Viking nabízejí široký výběr dětských modelů. Značka sama o kvalitě nerozhoduje, sledujte materiál a popis.</p>'
          '<h2>Péče o rukavice</h2>'
          '<p>Mokré rukavice vysušte při pokojové teplotě na větraném místě. Nesušte je na topení, kamnech ani v sušičce, protože teplo poškozuje membránu, lepidlo a kůži. Vnitřní podšívku vyndejte, pokud to konstrukce dovolí, a nechte ji vyschnout zvlášť. Kožené rukavice po vyschnutí ošetřete voskem nebo krémem. Textilní perte podle štítku a impregnaci obnovujte sprejem, protože se po několika prání vytrácí.</p>'
          '<p>Na konci sezóny rukavice vyčistěte a uložte suché na tmavém místě. Vlhké rukavice v zavřené tašce plesniví a zapáchají. Pokud rukavice spojuje popruh, zkontrolujte šití, aby při pádu neprasklo.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit rukavice těsně, aby „dobře seděly“, a tím omezit prokrvení.</li>'
          '<li>Spoléhat na tenkou rukavici ve velkém mrazu a doufat, že se ruka zahřeje pohybem.</li>'
          '<li>Zaměňovat vodoodpudivou úpravu za membránu.</li>'
          '<li>Sušit rukavice na topení.</li>'
          '<li>Nevzít dětem náhradní pár.</li>'
          '<li>Zapomenout na dlouhou manžetu při jízdě v hlubokém sněhu.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Filtrujte podle pohlaví, značky a velikosti. U modelu otevřete detail a porovnejte obchody, dostupnost velikostí a dopravu. Dbejte na popis materiálu a typ rukavice, protože podobné produkty se mohou lišit teplem i odolností. Pokud jste nejistí s velikostí, vyberte obchod s možností vrácení zboží.</p>',
    faq=[('Palčáky, nebo prstové rukavice na lyže?', 'Palčáky jsou teplejší, protože se prsty ohřívají navzájem. Prstové rukavice dávají lepší cit a úchop. Pro mrazivé dny a děti volte palčáky, pro aktivní jízdu a manipulaci se zipy prstové.'),
         ('Jak vybrat velikost lyžařských rukavic?', 'Změřte obvod dlaně pod prsty a porovnejte s tabulkou výrobce. Prsty mají lehce sahat ke konci rukavice, bez tlaku. Značky se liší střihem, proto vždy čtěte pokyny u konkrétního modelu.'),
         ('Jsou lyžařské rukavice nepromokavé?', 'Většina kvalitních modelů má membránu nebo vodoodolnou úpravu. Skutečnou odolnost poznáte podle popisu. Dlouhý pobyt ve vlhkém sněhu ověří i velmi dobrou rukavici, proto se vyplatí mít náhradní.'),
         ('Co jsou rukavice 3v1?', 'Skládají se z vnější nepromokavé rukavice a vyjímatelné vnitřní rukavice z fleecu nebo jiné izolace. Dají se nosit společně, nebo každá zvlášť podle počasí.'),
         ('Jak sušit lyžařské rukavice?', 'Při pokojové teplotě na větraném místě, vnitřní vrstvu vyjměte. Přímé teplo z topení nebo sušičky poškozuje membránu, lepidlo i kůži.'),
         ('Jaké rukavice pro děti?', 'Nejčastěji palčáky s dlouhou manžetou, stahováním a šňůrkou proti ztrátě. Zkontrolujte, zda se dobře oblékají, a vezměte druhý pár na výměnu.'),
         ('Proč mi i v dobrých rukavicích mrznou ruce?', 'Příčinou bývá příliš těsná rukavice, vlhkost uvnitř nebo nedostatečné oblečení těla. Pomůže větší velikost, vnitřní tenká rukavice a teplejší vrstva na paže. Při přetrvávajících potížích se poraďte s lékařem.'),
         ('Hodí se lyžařské rukavice i na snowboard?', 'Ano, snowboardisté ale často preferují delší manžetu a zesílenou dlaň, protože se hodně dotýkají sněhu. Označení rukavic bývá společné pro lyže i snowboard.'),
         ('Jak často rukavice impregnovat?', 'Podle používání a materiálu, obvykle jednou za sezónu nebo když voda přestane stékat po povrchu. Kůži ošetřujte voskem, textil sprejem určeným pro daný materiál.'),
         ('Mohu použít lyžařské rukavice i na běžky?', 'Pro běžky jsou lepší tenčí a prodyšnější rukavice, protože při námaze se ruka více zahřívá. V mrazu můžete použít tlustší, ale zvažte ztrátu citu při práci s holemi.')],
)

# ------------------------------------------------------------------ proteiny
NEW['proteiny'] = dict(long=True,
    title='Proteiny: syrovátkový, kaseinový, rostlinný',
    desc='Proteinové prášky: syrovátkový koncentrát a izolát, kasein i rostlinný protein. Jak číst etiketu a porovnat nabídky českých obchodů na Sportece.',
    intro='<p><strong>Protein</strong> je doplněk stravy v podobě prášku, který usnadňuje pokrýt denní příjem bílkovin, pokud ho nezvládáte z běžného jídla. Rozmíchá se ve vodě nebo mléce, přidá do kaše, smoothie nebo palačinek. Není to žádný zázračný prostředek, jen praktická potravina, kterou si lidé vybírají podle chuti, složení a pohodlí.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů s proteiny různých typů a příchutí. Vedle proteinů najdete i <a href="/kreatin/">kreatin</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny</a>, <a href="/gainery/">gainery</a> a <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>. Níže najdete průvodce typy, etiketou a nákupem. Jde o obecné informace, ne o zdravotní doporučení.</p>',
    guide='<h2>Co protein je a co není</h2>'
          '<p>Proteinový prášek je potravina vyrobená z mléčných, vaječných nebo rostlinných zdrojů, ze kterých se oddělí bílkovina a vysuší se. Nenahrazuje běžnou stravu a nic neslibuje samo o sobě. Je to jen pohodlný způsob, jak přijmout bílkoviny, když nemáte čas vařit nebo když vám při stravování chybí zdroj. Před nákupem ověřte, zda vám vyhovuje skladba jídelníčku. Individuální potřebu bílkovin vám pomůže určit lékař nebo výživový poradce, zvlášť pokud máte zdravotní omezení nebo problémy s ledvinami.</p>'
          '<h2>Druhy proteinu</h2>'
          + T(['Typ', 'Vstřebávání', 'Charakteristika', 'Pro koho'], [
              ['Syrovátkový koncentrát (WPC)', 'rychlé', 'nejrozšířenější, obsahuje trochu laktózy a tuku', 'běžné použití, začátečníci'],
              ['Syrovátkový izolát (WPI)', 'rychlé', 'vyšší podíl bílkovin, méně laktózy', 'citlivější na laktózu'],
              ['Syrovátkový hydrolyzát', 'velmi rychlé', 'předtrávený, specifická chuť', 'zájemci o rychle stravitelnou formu'],
              ['Kasein', 'pomalé', 'houstne, tvoří krémovou konzistenci', 'večerní porce nebo jako náhrada jídla'],
              ['Vaječný protein', 'střední', 'bez mléka', 'lidé bez tolerance mléka'],
              ['Hrachový, rýžový, sójový', 'různé', 'rostlinné, často směsi', 'vegani a lidé s intolerancí mléka'],
              ['Vícesložkové směsi', 'kombinované', 'mix rychlých i pomalých bílkovin', 'univerzální použití přes den']]) +
          '<h3>Syrovátka</h3>'
          '<p>Syrovátka vzniká při výrobě sýrů. Je nejoblíbenější, dobře se míchá a nabízí mnoho příchutí. Koncentrát je cenově dostupnější a obsahuje i trochu sacharidů a tuku. Izolát prošel další filtrací a má vyšší podíl bílkovin. Hydrolyzát je předtrávený a bývá nejdražší. Zda je rozdíl pro vás znatelný, záleží na toleranci a chuti. Při nesnášenlivosti laktózy zkuste izolát, při alergii na mléčnou bílkovinu mléčné proteiny vůbec nevolte.</p>'
          '<h3>Kasein</h3>'
          '<p>Kasein se trávi pomaleji a po rozmíchání houstne, takže se hodí do pudinků nebo jako krémová večerní porce. Jeho chuť i struktura se liší od syrovátky. Pro mnoho lidí je to otázka pohodlí a pocitu sytosti, ne hlavní rozdíl v účinku.</p>'
          '<h3>Rostlinné proteiny</h3>'
          '<p>Hrachový, rýžový, sójový, konopný nebo dýňový protein jsou volbou pro vegany a lidi, kteří nesnášejí mléko. Jednotlivé rostlinné zdroje mají odlišné složení aminokyselin, proto se často kombinují, například hrách s rýží. Chuť bývá výraznější a textura hrubší, což se dá zmírnit mixováním s ovocem nebo kakaem. Sója je alergen a někteří lidé se jí vyhýbají.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<p>Rozdíly mezi produkty se skrývají v detailech. Cena za balení neříká nic, pokud neznáte množství bílkovin, které za ně dostanete.</p>'
          '<ul><li><strong>Obsah bílkovin ve 100 g:</strong> udává podíl čisté bílkoviny v prášku. Čím vyšší, tím méně doplňků a sacharidů.</li>'
          '<li><strong>Velikost porce:</strong> porovnávejte cenu za porci nebo za gram bílkovin, ne za kilogram prášku.</li>'
          '<li><strong>Složení:</strong> krátký seznam je snazší pochopit. Sledujte sladidla, ztužující látky a aromata.</li>'
          '<li><strong>Alergeny:</strong> mléko, sója, vejce nebo lepek musí být zvýrazněny.</li>'
          '<li><strong>Sacharidy a tuky:</strong> důležité při hlídání energetického příjmu.</li>'
          '<li><strong>Trvanlivost a původ:</strong> kontrolujte datum minimální trvanlivosti a informace o výrobci.</li>'
          '<li><strong>Testy a certifikace:</strong> soutěžní sportovci ocení ověření, že výrobek neobsahuje zakázané látky.</li></ul>'
          '<h2>Příchuť, rozpustnost a konzistence</h2>'
          '<p>Chuť rozhoduje o tom, zda protein skutečně budete pít. Příchutě jako čokoláda, vanilka, jahoda nebo karamel patří k nejoblíbenějším. Neochucený protein je univerzální do jídla, ale samotný může připomínat mléko. Rozpustnost se liší: syrovátka se rozmíchá snadno, rostlinné směsi a kasein potřebují šejkr nebo mixér. Šejkr se hodí z kategorie <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>'
          '<h2>Jak protein používat</h2>'
          '<p>Nejběžnější je po tréninku nebo jako doplněk snídaně a svačiny. Dá se přimíchat do ovesné kaše, jogurtu, palačinek nebo pečení. Dodržujte dávkování výrobce a nevytvářejte si z prášku hlavní zdroj výživy. Při citlivém trávení začněte menší porcí. Pokud trpíte onemocněním ledvin nebo jinými zdravotními potížemi, poraďte se předem s lékařem. Těhotné a kojící ženy a děti by měly doplňky stravy konzultovat s odborníkem.</p>'
          '<h2>Protein podle cíle a typu sportovce</h2>'
          + T(['Situace', 'Co obvykle bývá praktické', 'Co zvážit'], [
              ['Začátečník v posilovně', 'syrovátkový koncentrát v oblíbené příchuti', 'nejdřív zhodnotit jídelníček, ne kupovat vše najednou'],
              ['Vegan nebo vegetarián', 'rostlinná směs z hrachu a rýže', 'sledovat složení a alergeny'],
              ['Nesnášenlivost laktózy', 'izolát nebo rostlinný protein', 'číst etiketu, stopy mléka mohou zůstat'],
              ['Běžec nebo cyklista', 'menší porce po výkonu, doplněná sacharidy', 'proteinů navíc není potřeba nadměrně'],
              ['Hubnutí a snížení energie', 'proteinový nápoj s nízkým obsahem cukru', 'neslouží jako náhrada všech jídel'],
              ['Cestování a práce', 'jednotlivé sáčky nebo tyčinky', 'srovnat složení se sladkostmi']]) +
          '<h2>Protein v tyčinkách, nápojích a dalších formách</h2>'
          '<p>Kromě prášku se prodávají hotové proteinové nápoje, pudinky a <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>. Jsou praktické na cesty, jenže mívají vyšší cenu za gram bílkovin a různé množství cukru. Pro nabité tréninkové dny stojí za zvážení i <a href="/gainery/">gainery</a>, tedy směsi bílkovin a sacharidů, které jsou však energeticky bohatší. Při vytrvalostním sportu doplňují bílkoviny <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a <a href="/iontove-napoje/">iontové nápoje</a>.</p>'
          '<h2>Další sportovní výživa</h2>'
          '<ul><li><a href="/kreatin/">Kreatin</a> se nejčastěji užívá v silových sportech.</li>'
          '<li><a href="/aminokyseliny-bcaa/">Aminokyseliny a BCAA</a> jsou stavební látky bílkovin.</li>'
          '<li><a href="/predtreninkove-boostery/">Předtréninkové boostery</a> obvykle obsahují kofein, takže je zvažte dle své citlivosti.</li>'
          '<li><a href="/vitaminy-a-mineraly/">Vitamíny, minerály a omega-3</a> doplňují jídelníček.</li>'
          '<li><a href="/kolagen-a-klouby/">Kolagen a kloubní výživa</a> je samostatná skupina.</li>'
          '<li><a href="/spalovace-tuku/">Spalovače tuků</a> se používají jen jako doplněk režimu.</li>'
          '<li>Přehled všeho najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a> a <a href="/ostatni-doplnky-stravy/">další doplňky stravy</a>.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr mají ' + B(('gymbeam', 'GymBeam'), ('myprotein', 'MyProtein'), ('extrifit', 'Extrifit'), ('amix', 'Amix'), ('biotech-usa', 'BioTech USA'), ('nutrend', 'Nutrend'), ('scitec-nutrition', 'Scitec Nutrition'), ('weider', 'Weider'), ('muscleclinic', 'MuscleClinic')) + '. GymBeam a MyProtein nabízejí široký sortiment proteinů, Extrifit, Nutrend a Amix jsou známé z českého a slovenského trhu, BioTech USA a Scitec Nutrition mají širokou paletu příchutí. Značka je jen jedním z vodítek, rozhodujte podle složení, podílu bílkovin a vlastní chuti.</p>'
          '<h2>Skladování a bezpečné používání</h2>'
          '<p>Protein skladujte v suchu a chladu, otevřené balení pevně uzavřete. Vlhkost způsobuje hrudky a zhoršuje trvanlivost. Odměrku nenechávejte uvnitř a nezanášejte do prášku mokré lžíce. Po rozmíchání nápoj vypijte brzy, protože nevhodně skladovaný zkysne. Sáčky chraňte před teplem a slunečním světlem. Při jakémkoli podezření na zkaženost produkt nepoužívejte. Uchovávejte mimo dosah dětí.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Porovnávat jen cenu za balení bez ohledu na podíl bílkovin a velikost porce.</li>'
          '<li>Koupit velké balení neznámé příchutě a pak ho nedopít.</li>'
          '<li>Ignorovat alergeny a intoleranci, například při mléčné bílkovině.</li>'
          '<li>Považovat protein za náhradu jídla nebo za nutnost.</li>'
          '<li>Kupovat několik doplňků najednou a nevědět, co vám vyhovuje.</li>'
          '<li>Věřit reklamním slibům místo složení na etiketě.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Vyberte typ proteinu a značku, otevřete detail a porovnejte obchody. Všímejte si gramáže balení, příchutě a dopravy. Pro férové srovnání si spočítejte cenu za 100 g bílkoviny, ne za kilogram prášku, protože podíl bílkovin se mezi produkty liší. Kontrolujte i datum minimální trvanlivosti a dostupnost vámi vybrané příchutě. Pokud zkoušíte novou značku, začněte menším balením.</p>',
    faq=[('Který protein je nejlepší pro začátek?', 'Syrovátkový koncentrát v příchuti, která vám chutná. Je cenově dostupný a dobře se rozmíchává. Při nesnášenlivosti laktózy zvolte izolát nebo rostlinnou směs.'),
         ('Kolik bílkovin denně potřebuji?', 'Potřeba závisí na hmotnosti, aktivitě a zdravotním stavu. Konkrétní množství vám určí lékař nebo výživový poradce. Prášek slouží jako doplněk jídla, ne jeho náhrada.'),
         ('Jaký protein vybrat pro vegany?', 'Rostlinný protein z hrachu, rýže, sóji nebo jejich směsi. Kombinace více zdrojů dává pestřejší složení aminokyselin. Zkontrolujte alergeny a sladidla.'),
         ('Kdy protein užívat?', 'Nejčastěji po tréninku nebo kdykoli během dne, kdy chybí bílkoviny v jídle. Kasein lidé často volí na večer. Rozhodující je pravidelnost a celkový denní příjem.'),
         ('Čím se liší koncentrát od izolátu?', 'Izolát prošel další filtrací, takže má vyšší podíl bílkovin a méně laktózy a tuku. Koncentrát je obvykle levnější a chuťově plnější.'),
         ('Jak porovnat ceny proteinů?', 'Vypočtěte cenu za 100 g bílkovin: vydělte cenu množstvím prášku a vynásobte podílem bílkovin ve 100 g. Cena za balení samotná nic neříká.'),
         ('Je protein vhodný i pro ženy a starší lidi?', 'Jde o potravinu, kterou mohou používat dospělí různého věku. Při zdravotních potížích, těhotenství, kojení nebo chronickém onemocnění se předem poraďte s lékařem.'),
         ('Jak protein rozmíchat bez hrudek?', 'Nejdřív nalijte tekutinu a pak přidejte prášek, nebo použijte šejkr s kuličkou či sítkem. Rostlinné proteiny a kasein se lépe rozmíchají v mixéru.'),
         ('Jak dlouho vydrží otevřené balení?', 'Při suchém a chladném skladování obvykle do data minimální trvanlivosti uvedeného výrobcem. Balení vždy pevně zavírejte a nenechávejte v něm mokrou odměrku.'),
         ('Mohu protein používat při hubnutí?', 'Je to potravina s vysokým podílem bílkovin, která může pomoci sestavit jídelníček. Nenahrazuje pestrou stravu a není zázračný. Při redukční dietě vyhledejte radu výživového specialisty.')],
)

# ------------------------------------------------------------------ doplňky k již napsaným textům (délka)
NEW['soupravy']['intro'] += ('<p>Při výběru myslete také na sezónu: léto vyžaduje lehkou prodyšnou látku, podzim a jaro něco pružného na vrstvení, zima pak zateplení nebo funkční spodní vrstvu.</p>')
NEW['soupravy']['guide'] = NEW['soupravy']['guide'].replace('<h2>Jak na Sportece porovnat nabídky</h2>',
    '<h2>Sezónní výběr souprav</h2>'
    '<p>Souprava na léto má být lehká, rychleschnoucí a s větracími prvky, třeba síťovinou na zádech nebo perforací pod pažemi. Přechodové období vyžaduje kompromis: lehkou bundu se zipem, kterou lze sundat, a kalhoty z materiálu, který chrání před vánkem. V zimě se souprava používá jako vrchní vrstva na lehký pohyb nebo jako teplá domácí varianta. Jakmile mrzne, přidejte pod ni <a href="/termopradlo/">funkční termoprádlo</a>, které odvádí pot a drží teplo u těla.</p>'
    '<h2>Barvy, potisky a design</h2>'
    '<p>Barva není jen otázka vzhledu. Světlé odstíny odrážejí slunce a jsou vidět za šera, tmavé lépe skryjí skvrny a pot. Reflexní prvky pomáhají při večerním běhání a cestování po městě. Potisky a nášivky vydrží různě dlouho, proto sledujte pokyny k praní. Týmové soupravy se často pořizují společně pro celý oddíl, a proto se vyplatí zjistit, zda lze doobjednat stejný model, když přibude nový člen.</p>'
    '<h2>Kdy souprava nestačí</h2>'
    '<p>Souprava je skvělá pro běžný pohyb, jenže pro specializované sporty je potřeba cílená výbava. Při běhu se hodí <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/sportovni-tricka/">trička a tílka</a> s funkčním materiálem, při turistice <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, v dešti <a href="/nepromokave-bundy/">nepromokavé bundy</a>. Soupravu proto vnímejte jako univerzální základ, ne jako náhradu všeho.</p>'
    '<h2>Jak na Sportece porovnat nabídky</h2>')

NEW['joga-a-pilates']['intro'] += ('<p>Ať už se rozhodujete mezi podložkou, kterou vezmete do studia, nebo pomůckami na domácí cvičení, pomůže vám přehled materiálů, tlouštěk a typů cvičení níže.</p>')
NEW['joga-a-pilates']['guide'] = NEW['joga-a-pilates']['guide'].replace('<h2>Jak na Sportece porovnat nabídky</h2>',
    '<h2>Cvičení doma, ve studiu nebo venku</h2>'
    '<p>Doma potřebujete podložku, která se snadno skladuje a čistí. Do studia se hodí lehká podložka s popruhem na nošení, protože ji vozíte s sebou. Studia často půjčují podložky, ale vlastní je hygieničtější a vždy sedí stejně. Pro cvičení venku na trávě zvolte silnější a odolnější podložku z materiálu, který snese vlhko a nerovný povrch. Na pláži či terase pomůže ručník přes podložku, aby se neklouzala potem.</p>'
    '<h2>Cvičení s omezenou pohyblivostí</h2>'
    '<p>Pokud nemáte ohebnost, nic se neděje. Právě pro tyto případy jsou určeny bloky a popruhy, které zkracují vzdálenost k zemi a umožňují pozici prodloužit postupně. Měkčí podložka nebo přeložená deka pod kolena pomůže u citlivých kloubů. Při zdravotních potížích, po úrazu nebo v těhotenství se před zahájením cvičení poraďte s lékařem či fyzioterapeutem, protože výběr pomůcek neřeší individuální omezení.</p>'
    '<h2>Hygiena a sdílení</h2>'
    '<p>Podložku sdílenou s jinými lidmi pravidelně dezinfikujte jemným prostředkem. Cvičíte-li naboso, po delší době podložku jednou za čas důkladněji očistěte a nechte vyvětrat. Textilní povlaky na polštářích perte podle štítku. Čistá výbava se lépe používá a vydrží déle.</p>'
    '<h2>Jak na Sportece porovnat nabídky</h2>')

NEW['lyzarske-rukavice']['guide'] = NEW['lyzarske-rukavice']['guide'].replace('<h2>Jak na Sportece porovnat nabídky</h2>',
    '<h2>Teplota, počasí a intenzita pohybu</h2>'
    '<p>Rukavice vybírejte podle toho, kolik tepla vaše ruce vyrobí. Dynamický sjezd a práce s holemi ruce zahřeje, zatímco vleky, kabinky a pauzy je rychle ochladí. Při větru se teplota na pokožce snižuje, proto i mírný mráz může být nepříjemný. V jarních podmínkách s sluncem a mokrým sněhem stačí tenčí rukavice, ovšem se spolehlivou vodoodolností. Při silných mrazech sáhněte po palčácích nebo rukavicích s tlustší izolací a vezměte náhradní.</p>'
    '<h2>Dotykové displeje, zipy a drobnosti</h2>'
    '<p>Některé rukavice mají na prstech vodivou plošku pro ovládání telefonu, takže je nemusíte sundávat. Ocení se i kapsička na skipas nebo zip na ohřívač rukou. Čím více detailů, tím víc se ale zvyšuje cena i objem. Zvažte, zda tyto funkce skutečně využijete, nebo se spokojíte s dobrým základem.</p>'
    '<h2>Ochrana při pádu</h2>'
    '<p>Snowboardisté se při pádu často opírají o ruce, a proto se k rukavicím přidávají chrániče zápěstí. Zesílená dlaň zmírňuje otěr, vyztužení palce chrání před přetížením. Při lyžování s holemi zkontrolujte, zda je v dlani dostatečná vrstva, aby poutko nedřelo. Rukavice nenahrazují chrániče, pokud jde o riziko zranění, a nabídku chráničů najdete ve <a href="/snowboarding/">snowboardingu</a>.</p>'
    '<h2>Jak na Sportece porovnat nabídky</h2>')

NEW['proteiny']['intro'] += ('<p>Výběr usnadní pochopení rozdílů mezi druhy proteinu, podílu bílkovin a velikosti porce, což se na první pohled z obalu nepozná.</p>')
NEW['proteiny']['guide'] = NEW['proteiny']['guide'].replace('<h2>Jak na Sportece porovnat nabídky</h2>',
    '<h2>Velikost balení a cena za porci</h2>'
    '<p>Proteiny se prodávají od malých vzorků po několikakilogramová balení. Malé balení se hodí na vyzkoušení příchutě a konzistence, velké je ekonomičtější, pokud už víte, co vám chutná. Jakmile se balení otevře, trvanlivost se zkracuje při špatném skladování. Zvažte, jak rychle prášek spotřebujete, a nekupujte větší množství, než vyčerpáte před koncem trvanlivosti.</p>'
    '<h2>Sladidla, aromata a citlivý žaludek</h2>'
    '<p>Ochucené proteiny často obsahují sladidla a aromata, která mohou některým lidem nevyhovovat. Pokud trávíte hůře, zkuste neochucenou variantu nebo jednodušší složení. Některé produkty mají přidané enzymy nebo další látky, které nejsou pro každého vhodné. Čtěte etiketu a začínejte menší porcí, abyste poznali, jak organismus reaguje.</p>'
    '<h2>Recepty a použití v kuchyni</h2>'
    '<p>Protein se neuplatní jen v šejkru. Přimíchat ho můžete do ovesné kaše, tvarohu, palačinek, domácích tyčinek nebo smoothie. Při pečení se mění chuť i struktura, a proto se začíná s malým množstvím. Neochucený prášek se hodí i do slaných jídel, ochucený se naopak využije do sladkých dezertů. Horká tekutina může způsobit srážení, proto při míchání do teplých jídel dávejte pozor.</p>'
    '<h2>Jak na Sportece porovnat nabídky</h2>')

NEW['lyzarske-rukavice']['guide'] = NEW['lyzarske-rukavice']['guide'].replace('<h2>Jak na Sportece porovnat nabídky</h2>',
    '<h2>Kdy rukavice vyměnit</h2>'
    '<p>Rukavice se opotřebují postupně. Za vyměnění stojí, když dlaň prodřela povrchovou vrstvu, švy se rozpářou nebo izolace slehla do hrudek a už nehřeje. Znamení je i to, že voda začíná prosakovat i po impregnaci. Na starých rukavicích se dá ještě zkusit ošetření, ale nenahradí poškozenou membránu. Pořiďte raději nový pár dřív, než vám zima zkazí lyžování.</p>'
    '<h2>Jak na Sportece porovnat nabídky</h2>')
NEW['proteiny']['guide'] = NEW['proteiny']['guide'].replace('<h2>Jak na Sportece porovnat nabídky</h2>',
    '<h2>Proteiny a pitný režim</h2>'
    '<p>Protein se rozmíchává s tekutinou a samotný nápoj nenahradí pravidelné pití vody během dne. Při vyšším příjmu bílkovin dbejte na dostatek tekutin. Při zdravotním omezení, třeba u onemocnění ledvin, se o vhodném množství bílkovin a tekutin poraďte s lékařem. Ke každému dni patří i pestrá strava s ovocem, zeleninou a celozrnnými přílohami, ke kterým prášek nic nepřidává.</p>'
    '<h2>Jak na Sportece porovnat nabídky</h2>')

NEW['lyzarske-rukavice']['intro'] += ('<p>Při výběru sledujte hlavně materiál membrány, tvar prstů, délku manžety a to, zda rukavice zvládnou pád na zledovatělý svah bez odření dlaně.</p>')
