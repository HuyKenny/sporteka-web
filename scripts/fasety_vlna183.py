"""sporteka.cz — facet landing texts wave 183: panske-holinky, sportovni-boty-adidas, tricko-puma, columbia-batoh."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ panske-holinky
NEW['panske-holinky'] = dict(
    title='Pánské holínky: velikosti, výška a podšívka',
    desc='Pánské holínky na zahradu, do lesa i na práci. Jak vybrat výšku, vložku a velikost pro široké lýtko, kdy sáhnout po neoprenu a kde porovnat nabídky.',
    intro='<p>Pánské holínky jsou stavěné na širší chodidlo, vyšší lýtko a těžší krok, než jaké mají dámské nebo dětské modely. '
          'Rozdíl poznáte hlavně na obvodu holeně: muž s osmačtyřicítkou v botě potřebuje jiný průřez než žena s osmatřicítkou, a proto se u pánských řad objevují i modely se zúžením nebo stahovací šňůrkou. '
          'Tato stránka třídí nabídku z kategorie <a href="/holinky/">holínky</a> pro muže: od jednoduchých PVC bot na dvůr přes myslivecké a farmářské modely s neoprenem až po nízké kotníkové varianty na dojíždění. '
          'Průvodce vysvětluje, jak se liší materiály, proč záleží na výšce lýtka, jak poznat holínku vhodnou do zimy a co udělat, aby se v ní nohy nepotily. Obchody srovnáváte podle skladových velikostí.</p>',
    guide='<h2>Čím se pánská holínka liší</h2>'
          '<p>Pánská řada se nedělá jen zvětšením dámské. Kopyto bývá širší v přednoří, špička je vyšší a podrážka silnější, protože musí unést větší hmotnost. Šachta, tedy část kolem lýtka, má vyšší obvod a často i větší výšku. '
          'Pro člověka, který stojí celý den ve stáji nebo na stavbě, to znamená méně otlaků a menší tlak na lýtkový sval. Kdo má naopak štíhlou nohu, hledá modely s textilním stahováním nebo s měkkým neoprenem, který se přizpůsobí.</p>'
          + T(['Typ holínky', 'Typické použití', 'Na co si dát pozor'], [
              ['Nízká PVC, kotníková', 'dvůr, mytí auta, krátká cesta', 'neochrání před hlubokou blátivou vodou'],
              ['Klasická středně vysoká', 'zahrada, stáj, lesní cesty', 'sledujte obvod šachty v lýtku'],
              ['Vysoká přes koleno', 'rybaření, mělké potoky, rozbahněný terén', 'těžší, hůř se v nich chodí do kopce'],
              ['Neoprenová, zateplená', 'myslivost, zimní práce venku', 'v teple se přehřívá, potřebuje větrání'],
              ['Pracovní s ochranou špičky', 'stavba, zemědělství, průmysl', 'ověřte označení a účel použití u každého kusu'],
              ['Kožená nebo hybridní', 'dlouhé trasy, kombinace lesa a města', 'vyžaduje impregnaci a sušení']]) +
          '<h2>Jak vybrat velikost a lýtko</h2>'
          '<p>Holínka nemá tkaničky, takže nohu drží jen tvar kopyta. Příliš velká bota znamená otlaky a ztrátu stability při chůzi po svahu, příliš malá bolestivě tlačí do palce. '
          'Počítejte s tím, že do zimní holínky chcete tlustou ponožku. Pro orientaci změřte chodidlo večer, kdy je nejširší, a přidejte k délce rezervu zhruba na šířku prstu. Tabulku výrobce vždy přečtěte pozorně, protože velikosti se u evropských a francouzských značek liší.</p>'
          '<ul><li><strong>Obvod lýtka:</strong> změřte nejširší místo, porovnejte s údajem u šachty a nechte aspoň malou vůli.</li>'
          '<li><strong>Výška šachty:</strong> jde-li o práci v blátě, volte vyšší; na lesní stezky a krátké chození stačí střední.</li>'
          '<li><strong>Nastavitelný popruh nebo šněrování:</strong> pomáhá u modelů, které mají širší horní okraj, aby se dovnitř nehrnula voda.</li>'
          '<li><strong>Vložka:</strong> vyjímatelná vložka se dá vyměnit a vysušit; dobrou vložku lze dokoupit zvlášť.</li></ul>'
          '<h2>Materiál: PVC, kaučuk a neopren</h2>'
          '<p>Pevné lité PVC je nejlevnější způsob, jak mít vodotěsnou botu, a pro běžné zahradnické použití bohatě stačí. Nevýhodou je, že tvrdne v mrazu a může popraskat v ohybu. '
          'Přírodní kaučuk je pružnější a lépe sedí na noze, hodí se pro delší chození, ale je dražší na výrobu a musí se chránit před sluncem. Neopren, tedy pěnová pryž, funguje jako izolace a v zimě nahrazuje ponožky navíc. '
          'Nevýhodou je, že pot z nohou uvnitř neodchází, proto jsou neoprenové modely často zip nebo šněrovací, a po použití se mají vysušit. Prodejci označují zateplené kusy slovy „hřejivé“, „zateplené“ nebo „winter“.</p>'
          '<h2>Značky, které v nabídce najdete</h2>'
          '<p>Nabídka je pestrá. ' + B(('solognac', 'Solognac'), ('aigle', 'Aigle'), ('rouchette', 'Rouchette'), ('cerva', 'Cerva'), ('aquos', 'Aquos'), ('dunlop', 'Dunlop')) +
          ' tvoří jádro skutečných gumových holínek, každá s jiným zaměřením. Aigle a Rouchette mířili původně na lov a venkov, Solognac vychází z myslivecké řady obchodu Decathlon, Cerva je česká firma zaměřená i na pracovní obuv. '
          'Vedle toho se mezi pánskými výsledky objevují i boty s podobným účelem, jako ' + B(('timberland', 'Timberland'), ('palladium', 'Palladium'), ('ugg', 'Ugg'), ('skechers', 'Skechers'), ('cmp', 'Cmp'), ('trespass', 'Trespass')) +
          ': nejde o gumové holínky, ale o voděodolné kotníkové boty, které zvládnou mokrou ulici. Rozdíl poznáte podle popisu produktu. Pokud chcete opravdu vodotěsnou botu, hledejte slova jako gumová, PVC nebo kaučuk; membránová bota není nepromokavá přes okraj.</p>'
          '<h2>Holínka do zimy</h2>'
          '<p>V mrazu se nejvíc projeví tuhost materiálu. Neoprenová nebo podšitá holínka drží teplo, ale pozor na těsný kus, protože stlačená ponožka izoluje hůř. Raději volte o číslo větší velikost a přidejte ponožku z vlny nebo syntetiky. '
          'Při chůzi po sněhu potřebujete hluboký vzorek podrážky, který se nezanáší. Mokré ponožky pak vyměňte hned po příchodu; u zimní holínky je to základ. Pro dlouhé chození zimní krajinou se vyplatí vedle holínek zvážit i <a href="/zimni-obuv/">zimní boty a sněhule</a>.</p>'
          '<h2>Kde se holínky hodí a kde ne</h2>'
          '<p>Na zahradě, ve stáji, při práci s vodou a v mokrém lese je holínka ideální. Na dlouhý výlet je naopak nepohodlná: nemá oporu pro kotník, pata se uvnitř pohybuje a chodidlo nedýchá. '
          'Kdo plánuje delší túru v mokru, přijde si lépe na <a href="/trekova-obuv/">trekové boty</a>, a ten, kdo brodí potok, najde lehčí řešení mezi botami do vody v kategorii <a href="/obuv-do-vody/">boty do vody</a>. '
          'Širší přehled najdete v hlavní kategorii <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Péče, aby vydržely</h2>'
          '<p>Po použití holínku opláchněte vlažnou vodou, očistěte od bláta a nechte vyschnout na vzduchu, nikoli u topení ani na přímém slunci. Teplo způsobuje praskání a barevnost mizí. Vložky vyndejte, aby uvnitř nezůstala vlhkost a zápach. '
          'Gumu občas ošetřete přípravkem na kaučuk, který zachová pružnost a vrací lesk. Uskladňujte je ve stoje nebo zavěšené, aby šachta neměla zlomy; ohyb za dlouhou dobu vede k puklinám. Drobný průsak lze zalepit speciální záplatou, ale u šachty a švu je lepší nepokoušet se.</p>'
          '<h2>Holínky podle povolání a koníčku</h2>'
          '<p>Zahrádkář chce lehkou a levnou botu, kterou po práci odloží před dveře; rozhodují snadné nazouvání a čištění. Chovatel a farmář stojí na betonu a ve hnoji, takže potřebuje silnější podrážku proti prokluzu a hladký povrch bez drážek, kde se nic nezachytí. '
          'Myslivec a lesník hledá tichý krok, tlumené barvy a zateplení na dlouhé čekání, proto sahá po zelených a hnědých neoprenových modelech. Rybář oceňuje vysoké stehenní provedení, které zvládne brodění. Cyklista nebo pěší na dlouhé dojíždění by zvolil raději nízkou kotníkovou verzi. '
          'Každá z těchto rolí tlačí na jinou vlastnost, a proto nemá smysl hledat jednu nejlepší holínku pro všechno.</p>'
          + T(['Kdo ji nosí', 'Co je nejdůležitější', 'Kterou variantu zvážit'], [
              ['Zahrádkář', 'lehkost, snadné nazutí', 'střední PVC bez podšívky'],
              ['Chovatel, farmář', 'protiskluz, odolnost vůči chemii', 'pracovní holínka s hladkou podrážkou'],
              ['Myslivec, lesník', 'teplo, tichost, kamufláž', 'neopren v zelené nebo hnědé'],
              ['Rybář', 'výška, voděodolnost', 'vysoká holínka nebo brodicí obuv'],
              ['Dojíždějící po městě', 'vzhled, lehkost', 'nízká kotníková bota']]) +
          '<h2>Rychlý kontrolní seznam před koupí</h2>'
          '<ul><li>Zjistěte, zda jde o skutečnou gumovou holínku, nebo o voděodolnou kotníkovou botu.</li>'
          '<li>Změřte chodidlo a lýtko a porovnejte je s tabulkou výrobce, ne s dojmem z jiné značky.</li>'
          '<li>Rozhodněte, zda potřebujete podšívku; pro letní provoz bývá zbytečná, v zimě naopak nepostradatelná.</li>'
          '<li>Podívejte se na vzorek podrážky: hluboké drážky drží v blátě, hladší se čistí snadněji.</li>'
          '<li>Prověřte, zda je ve vybrané velikosti nabídka u více obchodů, a porovnejte rozdíly v dopravě.</li></ul>'
          '<p>Při koupi na dálku nezapomeňte na možnost vrácení. Holínky vyzkoušejte doma na čistém povrchu a ponechte je bez znečištění, abyste případně mohli výměnu bez potíží uplatnit.</p>'
          '<h2>Navazující výběry</h2>'
          '<p>Pokud nakupujete pro rodinu, podívejte se na <a href="/damske-holinky/">dámské holínky</a> a <a href="/detske-holinky/">dětské holínky</a>, kde bývají jiné velikosti a výška. '
          'Barevné a vzorované modely znáte z výběrů <a href="/coqui-holinky/">Coqui holínky</a> a <a href="/crocs-holinky/">Crocs holínky</a>, na delší chození do lesa pak míří <a href="/holinky-viking/">holínky Viking</a>. Pro děti ze severské řady je tu i <a href="/reima-holinky/">holínky Reima</a>.</p>',
    faq=[
        ('Jak poznám správnou velikost pánské holínky?', 'Změřte délku chodidla večer a přidejte rezervu zhruba na šířku prstu. Do zimní holínky počítejte s tlustší ponožkou. Pohodlná bota drží patu a prsty se v ní ještě mírně pohnou. Tabulky se u různých značek liší, takže se řiďte údaji u konkrétního kusu.'),
        ('Co dělat, když mám silné lýtko?', 'Hledejte holínky s širokou šachtou, nastavitelným popruhem nebo elastickým vložením. Změřte obvod lýtka v nejširším místě a porovnejte s údajem výrobce. Neoprenové modely mají měkčí stěnu, která se lépe přizpůsobí, ale zeptejte se i na to, jak se snadno nazouvají.'),
        ('Jaká výška holínky je nejuniverzálnější?', 'Pro zahradu a lesní cesty obvykle stačí střední výška pod kolenem. Vysoké holínky se hodí do hlubokého bláta a při brodění, jsou ale těžší. Nízké kotníkové varianty se vyplatí na krátké cesty a do auta, vodu přes okraj ale nezastaví.'),
        ('Čím se liší PVC, kaučuk a neopren?', 'PVC je tvrdší a nejjednodušší, v mrazu tuhne. Kaučuk je pružnější a sedí příjemněji, ale vyžaduje péči. Neopren je pěnová pryž, která izoluje a hodí se do zimy, ale hůře odvádí pot. Podle použití tedy volíte mezi cenou, pohodlím a teplem.'),
        ('Jsou pánské holínky vhodné i na delší chození?', 'Na krátké trasy ano, na celodenní túru nikoli. Chybí jim opora kotníku a noha v nich nedýchá. Pro delší trasy v mokru je lepší trekový model s membránou, holínka je vhodná tam, kde potřebujete mít nohy suché ve vodě a bahně.'),
        ('Jak zabránit potu v holínkách?', 'Používejte ponožky z vlny nebo syntetiky, které odvádějí vlhkost, a ne bavlnu. Po použití holínky vyvětrejte a vyndejte vložku. U neoprenových modelů zvažte vložku s ventilací nebo druhý pár na střídání. Pot se nahromadí hlavně při dlouhém nošení.'),
        ('Dají se holínky nosit v zimě?', 'Ano, pokud jsou zateplené nebo máte dostatečně teplou ponožku a volnější velikost. Nezateplená PVC holínka v mrazu tvrdne a nohy rychle chladnou. Pro zimu vybírejte modely označené jako hřejivé nebo winter a vzorek, který se nezanáší sněhem.'),
        ('Jak holínky správně čistit a sušit?', 'Opláchněte je vodou, ručně očistěte kartáčem a nechte vyschnout při pokojové teplotě. Nikdy je nesušte na topení, protože guma tvrdne a praská. Vložky vyndejte zvlášť. Občasné ošetření přípravkem na kaučuk prodlužuje životnost a drží materiál pružný.'),
        ('Jsou v nabídce i pracovní holínky?', 'Ano, najdete modely určené pro farmářskou a lesní práci, často s ochranou špičky a protiskluzovou podrážkou. U pracovního použití si ověřte označení v popisu produktu a pro které prostředí je bota určena. Běžná zahradní holínka takovou ochranu nenabízí.'),
        ('Kde porovnám pánské holínky z více obchodů?', 'Přímo tady. U každého modelu vidíte nabídky obchodů, jejich skladovou dostupnost a aktuální cenu, takže rychle poznáte, kde mají vaši velikost. Výběr zúžíte filtrem podle značky nebo velikosti a odkaz vás odvede do e-shopu.'),
    ])

# ------------------------------------------------------------------ sportovni-boty-adidas
NEW['sportovni-boty-adidas'] = dict(
    title='Sportovní boty Adidas: kopačky, běh, Terrex a tenisky',
    desc='Sportovní boty Adidas od kopaček F50 a Predator přes běžecké Duramo po outdoorové Terrex a pantofle Adilette. Jak se orientovat v řadách a velikostech.',
    intro='<p>Adidas nedělá jednu botu, ale několik oddělených světů pod společným logem tří pruhů. Fotbalisté znají kopačky řad F50, Predator a Copa, běžci řadu Duramo a Response, turisté outdoorové boty Terrex, hráči tenisu a sálových sportů modely Grand Court nebo Ligra a široká veřejnost pohodlné tenisky a pantofle Adilette. '
          'Na této stránce jsou sportovní boty značky z kategorie <a href="/sportovni-obuv/">sportovní obuv</a> řazené tak, abyste mezi nimi snadno našli ten typ, který skutečně potřebujete. '
          'Průvodce vysvětluje, jak se podle názvu modelu pozná zaměření boty, čím se liší povrchové kategorie u kopaček, jak sedí obuv značky a kdy dává smysl srovnat Adidas s konkurencí. Dole najdete i odpovědi na časté dotazy k velikostem a péči.</p>',
    guide='<h2>Jak číst názvy modelů Adidas</h2>'
          '<p>Největší překážkou je množství názvů. Značka je ale poměrně přehledná, když víte, kam patří které slovo. Název modelu většinou naznačuje sport, a to dřív, než otevřete popis. '
          'Za názvem často stojí úroveň: u kopaček označení Club, League a Pro, u běžeckých bot číslování generací. Pokud tedy vidíte rok, ročník nebo dvojku za modelem, jde o novější verzi stejné řady, zatímco starší verze bývají dostupné za nižší nabídku.</p>'
          + T(['Název v nabídce', 'Zaměření', 'Pro koho'], [
              ['F50, Predator, Copa', 'kopačky na různé povrchy', 'hráče fotbalu od dětí po dospělé'],
              ['Duramo, Response, Ultrabounce', 'běžecké a tréninkové boty', 'rekreační běh, fitness, každodenní pohyb'],
              ['Terrex', 'outdoor, turistika, trail', 'výlety v horách, výlety v kamenitém terénu'],
              ['Grand Court, Advantage, Breakbase', 'volnočasové tenisky', 'město, škola, každodenní nošení'],
              ['Ligra, Predator Club In Sala, Speedcourt', 'sálová a halová obuv', 'tělocvična, futsal, házená a volejbal'],
              ['Adilette, Adissage', 'pantofle a žabky', 'bazén, šatna, po tréninku'],
              ['Tensaur, Rapid Court J, K a C v názvu', 'dětské a juniorské modely', 'děti, kde rozhoduje růst a cena']]) +
          '<p>Písmena na konci názvu mívají vlastní význam. J značí juniory, K nebo Kids děti a C nejmenší velikosti, W ženy. U outdoorových bot označení GTX nebo Gore-Tex říká, že bota má membránu, a zkratky Mid nebo High vyšší kotník. '
          'Jde o obecnou konvenci obuvi, takže si ji můžete ověřit i u jiných značek.</p>'
          '<h2>Kopačky Adidas a povrch</h2>'
          '<p>Kopačky tvoří velkou část nabídky a nejčastěji se na nich chybuje v povrchu. Zkratky FG, MG a SG patří k trávě: FG je firm ground, pevný povrch s kolíky, MG multi ground, univerzální pro různé povrchy, SG soft ground, měkký terén s vyměnitelnými kolíky. '
          'Označení TF a Turf míří na umělou trávu s nízkými nopky, IN nebo Indoor na halu. Špatná volba nebolí hned, ale na tvrdém povrchu se pevné kolíky bolestivě zatíží a na hale se kopačka rychle ničí. Podrobnosti najdete v kategorii <a href="/kopacky/">kopačky</a> a pro halu v <a href="/salova-obuv/">sálové a halové obuvi</a>.</p>'
          '<p>Řady F50, Predator a Copa se liší charakterem. F50 stavěla značka na rychlost a lehkost, Predator na kontrolu míče a Copa na klasickém střihu s kůží nebo kožením povrchem pro pohodlí. Řada League je střední třída pro pravidelné hráče, Club cílí na začátečníky a děti, a vyšší modely mají lehčí a dražší materiály. Pro dítě, které rychle roste, se rozhodně nevyplácí sahat po nejdražším kuse.</p>'
          '<h2>Běžecké a tréninkové boty</h2>'
          '<p>Modely jako Duramo, Response nebo Ultrabounce slouží rekreačnímu běhu a cvičení, nikoli závodnímu výkonu. Mají pěnový střed, který tlumí dopad, a vzorek podrážky pro silnici. Pro pravidelné běhání zvolte botu s větší rezervou ve špičce, protože noha při běhu otéká. '
          'Rozdíly mezi typy bot, tedy neutrální, stabilní nebo trailové, probírá kategorie <a href="/bezecka-obuv/">běžecké boty</a>. Pro posilovnu raději sáhněte po <a href="/treninkova-obuv/">fitness a tréninkové obuvi</a> s pevnější podrážkou.</p>'
          '<h2>Terrex: outdoor a turistika</h2>'
          '<p>Terrex je outdoorová řada Adidas. Z názvů v nabídce poznáte nízké boty do lehčího terénu, kotníkové modely a varianty s membránou Gore-Tex nebo označením Climaproof. Hodí se na jednodenní výlety, procházky v horách a rychlé přechody, kde nepotřebujete těžkou trekovou botu. '
          'Pro náročnější trasy s těžkým batohem a vysokými kopci raději srovnejte i klasické <a href="/trekova-obuv/">trekové boty</a>. Při výběru membrány pamatujte, že dýchá hůře než bota bez membrány, takže v létě je nepohodlnější než lehčí síťovina.</p>'
          '<h2>Volný čas, tenis a pantofle</h2>'
          '<p>Grand Court, Advantage a Breakbase jsou jednoduché, nenápadné tenisky, které vzhledem navazují na tenisovou klasiku. Nejsou určené pro sport, ale hodí se na každodenní nošení. Pokud chcete skutečné tenisové boty s oporou pro boční pohyb, hledejte v kategorii <a href="/tenisova-obuv/">tenisová obuv</a>. '
          'Pantofle Adilette a Adissage se nosí u bazénu, v šatně a po tréninku. Podrobněji je rozebírá kategorie <a href="/pantofle-a-zabky/">pantofle a žabky</a>; pro volný čas pak <a href="/tenisky/">tenisky a volnočasové boty</a>.</p>'
          '<h2>Jak sedí boty Adidas</h2>'
          '<p>Značka vyrábí velikosti podle evropského systému a většina modelů sedí standardně. Přesto se liší střih: sálovky bývají přiléhavější, kopačky úzké a turistické modely širší. Pokud váháte mezi dvěma čísly, měřte chodidlo a podívejte se na délku vložky v centimetrech. '
          'Nechte rezervu pro prsty, u dětí zhruba půl až celé číslo, a pro přezkoušení použijte stejné ponožky, v jakých budete boty nosit. U kopaček je rezerva menší, protože hráč chce těsný kontakt s míčem.</p>'
          '<h2>Adidas a konkurence</h2>'
          '<p>Chcete-li porovnat výběr, otevřete <a href="/nike-sportovni-boty/">sportovní boty Nike</a> a <a href="/sportovni-boty-puma/">sportovní boty Puma</a>. Všechny tři značky mají podobné řady od kopaček po tenisky, rozdíly jsou ve střihu a detailech. '
          'Adidas bývá oblíbený u fotbalistů a v outdoorové řadě, Nike u basketbalu a běhu, Puma u sportovního stylu. Neznamená to, že jedna značka je lepší, jen že každá má jiné silné segmenty.</p>'
          '<h2>Pro koho a v jakém pohlaví</h2>'
          '<p>Stejné modely bývají dostupné ve více provedeních. Pro ženy si otevřete <a href="/damska-sportovni-obuv/">dámskou sportovní obuv</a>, pro muže <a href="/panska-sportovni-obuv/">pánskou sportovní obuv</a> a pro děti <a href="/detska-sportovni-obuv/">dětskou sportovní obuv</a>. '
          'Dámské modely mívají užší patu a lehčí konstrukci, dětské jsou odolné v místech, kde se bota nejvíc opotřebuje, hlavně na špičce.</p>'
          '<h2>Sálová obuv a dětské modely</h2>'
          '<p>Na hale rozhoduje podrážka. Světlá nebo gumová bez barvení nesmí na parketech zanechávat stopy a musí dobře držet při náhlých změnách směru. Proto se sálovky Adidas od kopaček liší plochou podrážkou a měkčím svrškem, který nepoškodí míč ani podlahu. '
          'Dětem vybírejte boty podle druhu pohybu: na tělocvik stačí lehké tenisky, na kroužek fotbalu kopačky Club, na školní halu sálovou botu. Příliš specializovaný kus se při jiném použití rychle zničí. Pro mladší děti oceníte suchý zip, protože vázání tkaniček před hodinou tělocviku zdržuje a bota se při špatně zavázané tkaničce uvolní.</p>'
          '<h2>Jak se rozhodnout mezi typy</h2>'
          '<p>Pomůže vyřazovací postup. Nejdřív určete sport nebo prostředí, potom povrch a nakonec pohodlí a vzhled. Teprve poté se dívejte na konkrétní model a barvu.</p>'
          '<ol><li>Chodím převážně po asfaltu, nebo po hlíně, trávě a kamenech?</li>'
          '<li>Potřebuji botu na jeden sport, nebo na všechno dohromady?</li>'
          '<li>Bude bota v mokru? Pak zvažte membránu nebo hrubší podrážku.</li>'
          '<li>Jak dlouho v ní budu stát nebo chodit v kuse? Čím déle, tím víc se vyplatí odpružení.</li>'
          '<li>Do jaké míry záleží na vzhledu? Pokud hlavně na něm, zvolte volnočasový model a nenechte se zlákat sportovním označením.</li></ol>'
          '<h2>Co se týká obchodů a dostupnosti</h2>'
          '<p>Adidas prodává velké množství obchodů, ale jednotlivé velikosti jsou skladem různě. Populární kombinace velikosti a barvy zmizí nejdřív, proto se vyplatí vybrat si náhradní variantu. U sezónních modelů, jako jsou kopačky před začátkem sezóny, bývá nabídka nejširší na jaře a na podzim. '
          'Při srovnání sledujte i dopravu a možnost vrácení, protože boty je nutné vyzkoušet, a ne všechny obchody je přijmou zpět bez problémů.</p>'
          '<h2>Péče o boty</h2>'
          '<p>Boty po použití vyvětrejte, vložky vyndejte a nesušte je na topení. Špínu setřete vlhkým hadříkem, textilní svršek lze kartáčovat jemným mýdlem. Kopačky po zápase očistěte od trávy a bláta, aby kolíky nebyly zalepené. '
          'Pantofle z pěnového materiálu omyjte vodou a nechte oschnout; netřeba je vystavovat dlouhému přímému slunci. Správně ošetřená bota vydrží více sezón.</p>',
    faq=[
        ('Jak poznám, jestli je model Adidas běžecký, nebo jen volnočasový?', 'Podívejte se na název a popis. Duramo, Response nebo Ultrabounce míří na běh a cvičení, Grand Court, Advantage a Breakbase na každodenní nošení. Běžecké boty mají pěnový střed, volnočasové jsou jednodušší. Při nejistotě ověřte zaměření v popisu produktu.'),
        ('Co znamenají zkratky FG, MG, SG a TF u kopaček Adidas?', 'FG je pevná tráva, MG univerzální povrch, SG měkká tráva s výměnnými kolíky a TF umělý trávník s malými nopky. IN neboli Indoor je pro halu. Povrch zvolte podle hřiště, kde hrajete nejčastěji. Univerzální kopačky MG kombinují více povrchů, ale nejsou ideální na žádném.'),
        ('Je Adidas Terrex vhodný na hory?', 'Pro jednodenní výlety a lehký terén ano. Nízké modely se hodí na stezky, kotníkové na hrubší cesty. Při těžkém batohu a delších trasách zvažte i klasické trekové boty. Membrána Gore-Tex pomáhá v mokru, v horku ale hůře dýchá.'),
        ('Sedí Adidas větší, nebo menší než jiné značky?', 'Většinou sedí v běžné evropské velikosti, ale střihy se liší podle typu. Kopačky bývají užší, turistické boty širší. Nejjistější je změřit chodidlo a porovnat délku vložky v centimetrech. Při váhání volte raději delší vložku než příliš těsnou.'),
        ('Jakou velikost vybrat dítěti?', 'Dítěti nechte rezervu zhruba půl až celé číslo, aby mělo prostor pro růst, ale ne příliš velké, jinak bota klouže. U kopaček je vhodnější těsnější sedlo. Velikost kontrolujte alespoň každého půl roku, děti rostou nerovnoměrně a malá bota se nepozná včas.'),
        ('Mohu nosit kopačky mimo hřiště?', 'Nedoporučuje se. Kolíky a podrážka jsou stavěné na trávu a na tvrdém povrchu se rychle ničí nebo skřípou. Pro město je lepší tenisky. Výjimkou jsou halové a sálové modely s plochou podrážkou, které se dají použít v tělocvičně.'),
        ('Čím se liší pánské, dámské a dětské provedení téhož modelu?', 'Liší se střih i barevnost. Dámský model bývá užší v patě a lehčí, dětský odolnější a často s upevněním na suchý zip. Svršek a podrážka jsou obvykle podobné. Pokud se vám pánský střih pohodlně nosí, nemusíte hledat výhradně dámskou verzi.'),
        ('Jak čistit bílé tenisky Adidas?', 'Vlhkým hadříkem s jemným mýdlem, zvlášť okraj podrážky a svršek. Vložky a tkaničky vyperte zvlášť. Nepoužívejte bělidlo, které žloutne materiál. Nechte je uschnout na vzduchu a mimo přímé slunce či topení, aby se nezdeformovaly.'),
        ('Dá se Adidas porovnat s Nike a Pumou?', 'Ano, všechny tři značky mají podobné řady od kopaček po tenisky. Rozdíly jsou ve střihu a detailech, proto se vyplatí boty vyzkoušet nebo porovnat odkazy na velikostní tabulky. Samotná značka není zárukou pohodlí, rozhoduje tvar vaší nohy.'),
        ('Kdy se u bot Adidas nejvíc slevuje?', 'Nejčastěji se slevují starší ročníky a barevné varianty při příchodu nové kolekce, tedy po sezóně. U kopaček a běžeckých bot je dobré sledovat ročník modelu. Sleva sama o sobě neříká, zda je cena dobrá, porovnejte ji s ostatními obchody na této stránce.'),
    ])

# ------------------------------------------------------------------ tricko-puma
NEW['tricko-puma'] = dict(
    title='Tričko Puma: Essentials, běžecká a fotbalová trika',
    desc='Tričko Puma pro muže, ženy i děti: bavlněné Essentials, běžecká trika Velocity, fotbalové dresy Liga a polo Ferrari. Střihy, velikosti a praní.',
    intro='<p>Tričko Puma může být bavlněné triko s logem na každý den, lehké běžecké tričko, fotbalový dres týmu nebo polokošile v motorsportovém stylu. Na první pohled se podobají, ale každé je šité na jiný účel. '
          'V nabídce kategorie <a href="/sportovni-tricka/">trička a tílka</a> proto najdete řady Essentials, Better Essentials, Velocity, teamGOAL a Liga, grafické modely i dětské verze s označením Youth nebo Junior. '
          'Stránka pomáhá orientovat se v tom, který typ zvolit, jak poznáte střih regular, relaxed nebo boxy, kdy vybrat bavlnu a kdy syntetiku, jaké velikosti sedí na dámském a pánském střihu a jak tričko s potiskem prát, aby logo vydrželo. Obchody pak porovnáte podle skladovosti velikostí.</p>',
    guide='<h2>Řady triček Puma podle názvu</h2>'
          '<p>Značka používá krátké názvy řad, které se opakují napříč pohlavím i věkem. Když je znáte, rozhodnete se o účelu dřív než při čtení popisu. Pomůže následující přehled, který shrnuje, co je pod jakým označením k nalezení.</p>'
          + T(['Označení v názvu', 'Typické použití', 'Materiál a střih'], [
              ['Essentials, ESS, Better Essentials', 'denní nošení, lehký trénink', 'převážně bavlněné nebo bavlna s příměsí, rovný střih'],
              ['Velocity, Run, Cloudspun v názvu, Train', 'běh, fitness, cvičení', 'lehké syntetické pleteniny, odvádění potu'],
              ['teamGOAL, Liga, Individualcup', 'fotbal, týmové dresy', 'polyester, dresové trička, jednotné barvy'],
              ['Graphic, Boxy, Relaxed, Stacked', 'streetový styl', 'volnější střih s potiskem'],
              ['Polo, Piqué', 'každodenní oblečení, golf, motorsport', 'polokošile s límečkem'],
              ['Youth, Junior', 'děti a dorost', 'menší střih, stejné řady jako dospělí']]) +
          '<p>Označení Ferrari u polo triček odkazuje na spolupráci Puma s motorsportem. Tato trička se nosí hlavně jako volnočasové oblečení, ale střih polokošile je praktický i v kanceláři. Podrobnosti o límečkových modelech najdete v kategorii <a href="/polokosile/">polokošile</a>.</p>'
          '<h2>Bavlněné triko, nebo sportovní materiál</h2>'
          '<p>Bavlna je měkká a příjemná na kůži, ale nasákne potem a pomalu schne. Na procházku, do kanceláře nebo na lehké cvičení je skvělá. Při běhu, ve fitku nebo v horkém dni ji vystřídá syntetika, která vlhkost převádí na povrch a rychle schne. '
          'Puma zařazuje takové materiály do řad, které mají v názvu běh nebo trénink. Pokud neznáte použitý materiál, zkontrolujte složení v popisu: čistá bavlna znamená nižší odvod potu, polyester nebo elastan větší rychlost schnutí. Podrobnější průvodce je v kategorii <a href="/funkcni-tricka/">funkční trička</a>.</p>'
          '<h2>Střih: regular, relaxed a boxy</h2>'
          '<p>U značky se často setkáte s popisem střihu. Regular je klasický, přiléhavě rovný střih. Relaxed je volnější v rameni a hrudi, boxy navíc kratší a širší, takže tričko tvoří čtvercový tvar. Slim se přimyká k tělu. '
          'Rozdíl je důležitý zejména pro vyšší lidi, kteří mohou volit delší regular, a pro ty, kdo chtějí nosit tričko přes pas, kde se hodí boxy. Pokud váháte, přepočítejte hrudník a porovnejte jej s tabulkou. U volného střihu můžete zvolit menší velikost, aby tričko nepůsobilo příliš široce.</p>'
          '<h2>Pánská, dámská a dětská trička</h2>'
          '<p>Dámský střih je užší v rameni a v pase a často o něco delší. U pánského je rameno širší a rukáv volnější. Dívky i ženy ocení i verze s delším rukávem nebo tričko do pasu. Pro ženy je vhodné prohlédnout si <a href="/funkcni-tricka-damska/">dámská funkční trička</a>, pro muže pak běžný výběr <a href="/panska-tricka/">pánských triček</a>. '
          'U dětí volte velikost podle výšky a nechte malou rezervu; značka označuje juniory a Youth, které sedí podle věkové tabulky výrobce.</p>'
          '<h2>Fotbalová trika a týmové dresy</h2>'
          '<p>Řady teamGOAL, Liga a Individualcup patří k týmovým dresům a trikům na trénink. Jsou z lehkého polyesteru a vyrábějí se v jednotných barvách, aby klub mohl sehnat stejné kusy pro všechny hráče. '
          'Pro kluky bývají k dispozici ve velikostech juniorských. Pokud je kupujete pro tým, ověřte, zda lze získat stejné barvy v potřebném počtu velikostí, protože barva se může lišit mezi šaržemi. Na trénink stačí základní model, na zápas oceníte větší prodyšnost a potisky čísel.</p>'
          '<h2>Pro koho je tričko Puma</h2>'
          '<p>Puma cílí na sportovně laděné publikum, které chce, aby oblečení vypadalo sportovně i mimo hřiště. Trička Essentials s malým logem na hrudi se hodí k džínám i k teplákovým kalhotám. Grafická trička jsou výraznější a ke každodennímu nošení vyžadují jednodušší doplňky. '
          'Pokud preferujete minimalistický vzhled, zvolte jednobarevné tričko s logem na hrudi. Pokud vás zajímá hlavně funkce, nechte logo stranou a zaměřte se na materiál.</p>'
          '<h2>Porovnání s jinými značkami</h2>'
          '<p>Podobné nabídky mají i konkurenti: <a href="/adidas-tricko/">trička Adidas</a>, <a href="/nike-tricko/">trička Nike</a>, <a href="/under-armour-tricko/">trička Under Armour</a>, <a href="/kappa-tricko/">trička Kappa</a> a <a href="/fila-tricko/">trička Fila</a>. '
          'Rozdíly spočívají v střihu a barevnosti, základní princip je stejný. Při výběru tedy nehledejte „nejlepší značku“, ale nejlepší střih a materiál. U sportovního použití je pro vás nejlepší materiál, který odvádí pot, u volného času má větší význam pohodlí.</p>'
          '<h2>Praní, aby potisk vydržel</h2>'
          '<ul><li><strong>Naruby:</strong> trička s potiskem perte obrácená na rubovou stranu, abyste omezili otěr loga.</li>'
          '<li><strong>Teplota:</strong> bavlna snese vyšší teplotu, syntetika raději třicet až čtyřicet stupňů; vždy se řiďte štítkem.</li>'
          '<li><strong>Bez aviváže:</strong> u funkčních materiálů aviváž zhoršuje odvod potu.</li>'
          '<li><strong>Sušení:</strong> na vzduchu; sušička může zmenšit bavlnu a poškodit potisk.</li>'
          '<li><strong>Žehlení:</strong> potisk žehlete jen z rubu, nebo vůbec.</li></ul>'
          '<p>Světlá trička perte zvlášť, abyste předešli zešednutí. Při pravidelném praní se tričko po čase přirozeně smrští nebo vypere, proto je dobré při nákupu zvolit lehce volnější velikost, pokud nechcete střih těsný.</p>'
          '<h2>Tričko podle ročního období</h2>'
          '<p>V létě se vyplatí lehká, prodyšná pletenina a světlejší barvy, které méně hřejí na slunci. Tričko s krátkým rukávem často nosíte i pod mikinu nebo bundu v chladnějších měsících, proto se hodí mít několik základních kusů. '
          'Z přechodného období je praktické triko s dlouhým rukávem, které Puma nabízí v řadě Essentials: nahradí svetr a snadno se kombinuje. V zimě slouží funkční tričko jako první vrstva pod teplejší oblečení, ale musí sedět přiléhavě, jinak pot neodvádí. '
          'Bavlněné tričko přímo na kůži při zimním sportu nepoužívejte, protože zvlhne a ochlazuje tělo.</p>'
          + T(['Období', 'Vhodný typ', 'Proč'], [
              ['Léto, horko', 'lehká syntetická pletenina, světlé barvy', 'rychle schne, méně se zahřívá'],
              ['Jaro, podzim', 'bavlněné Essentials, dlouhý rukáv', 'kombinuje se s mikinou a bundou'],
              ['Zima', 'přiléhavé funkční tričko jako spodní vrstva', 'odvádí pot, nechladí'],
              ['Celoročně v hale', 'lehký polyester', 'rychlé schnutí, žádné zatížení']]) +
          '<h2>Jak kombinovat tričko s logem</h2>'
          '<p>Značkové tričko s velkým logem je výrazné, takže k němu volte klidné spodní díly: tmavé džíny, tepláky nebo šortky bez dalšího potisku. Malé logo na hrudi je univerzální a vejde se k čemukoli. '
          'Barevné modely se hodí k neutrální černé, šedé nebo bílé. Pokud nosíte tričko přes kalhoty, vybírejte boxy nebo relaxed střih. Pro sportovní vzhled od hlavy k patě stačí sladit barvu trička s obuví, například s bílými teniskami.</p>'
          '<h2>Na co se dívat u kvality</h2>'
          '<ul><li><strong>Šití:</strong> rovné švy bez uvolněných nití, zejména kolem límce a rukávů.</li>'
          '<li><strong>Límec:</strong> kvalitní žebrovaný lem se nevytahuje a drží tvar i po opakovaném praní.</li>'
          '<li><strong>Gramáž a hustota:</strong> příliš tenká bavlna prosvítá, příliš tlustá hřeje; u popisu hledejte údaj o materiálu.</li>'
          '<li><strong>Potisk:</strong> pryžový nebo nažehlovaný potisk drží déle než lehký tisk, ale u levnějších kusů se může odlupovat.</li>'
          '<li><strong>Štítek:</strong> měkký štítek nebo potisk uvnitř omezuje dráždění pokožky při sportu.</li></ul>'
          '<p>Pokud bude tričko nošeno pod batohem nebo s popruhem, vyhněte se kusům s hrubými švy na ramenou, které by se mohly otírat. Dlouhodobě nejlépe vyjdete s tím, že si pořídíte několik základních kousků a doplníte je jedním výraznějším.</p>'
          '<h2>Další výběry</h2>'
          '<p>Pokud hledáte variantu bez rukávů, podívejte se na <a href="/tilka/">tílka a topy</a>. Pro dlouhodobé nošení mohou být zajímavé také <a href="/the-north-face-tricko/">trička The North Face</a>, <a href="/lacoste-tricko/">trička Lacoste</a> nebo <a href="/tricko-vans/">trička Vans</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi řadou Essentials a Velocity?', 'Essentials je základní volnočasová řada s rovným střihem a často bavlněným materiálem, vhodná pro každodenní nošení. Velocity a podobné běžecké řady používají lehčí syntetické pleteniny, které odvádějí pot, a hodí se na běh nebo trénink. Určuje to zejména materiál.'),
        ('Co znamená regular fit, relaxed a boxy?', 'Regular je klasický střih, relaxed je volnější v rameni a hrudi, boxy je kratší a širší, takže tvoří čtvercový obrys. Pokud chcete přiléhavé tričko, zvolte regular nebo slim, na volný styl relaxed či boxy. Označení najdete v popisu produktu.'),
        ('Jak vybrat velikost trička Puma?', 'Změřte obvod hrudníku a porovnejte jej s tabulkou výrobce. U volného střihu můžete zvolit menší velikost, u přiléhavého držte přesnou. Dámské a pánské tabulky se liší, proto se nenechte zmást stejným písmenem S, M nebo L.'),
        ('Hodí se bavlněné tričko na běh?', 'Na krátký lehký běh stačí, ale při delším nebo intenzivním výkonu nasákne potem a začne dřít. Pro běh a fitness je praktičtější syntetika, která pot odvádí a rychle schne. Bavlna se hodí do každodenního života a na odpočinek.'),
        ('Jak prát tričko s potiskem?', 'Perte ho obrácené na rubovou stranu při teplotě podle štítku, bez aviváže a bez sušičky. Potisk žehlete jen z rubu. Šetrné praní prodlouží životnost loga a udrží barvy čisté. Světlé a tmavé kusy perte zvlášť.'),
        ('Lze koupit i fotbalová trika pro dětský tým?', 'Ano, řady teamGOAL a Liga mají juniorské velikosti a jednotné barvy. U týmové objednávky zkontrolujte, zda je v obchodě dost kusů stejné barvy a velikosti. Barva se může u různých šarží mírně lišit, proto kupujte najednou.'),
        ('Co jsou trička Ferrari od Puma?', 'Jde o polo trička a trička inspirovaná motorsportem ve spolupráci s tímto týmem. Nosí se hlavně jako volnočasové oblečení, mají často nášivky nebo logo na hrudi. Pro sportovní účely nejsou určena, spíše pro styl.'),
        ('Může tričko Puma sedět jinak než Adidas nebo Nike?', 'Ano, střihy se mezi značkami liší, i když se označují stejnou velikostí. Nejjistější je porovnat míry v tabulce konkrétního produktu s vlastním obvodem hrudníku. Pokud se mezi velikostmi nemůžete rozhodnout, volte podle preferovaného střihu, ne jen podle písmene.'),
        ('Jak poznám dámské a dětské trička v nabídce?', 'V názvu bývá slovo Dámské, W, Wn, Youth nebo Junior. Dámský střih je užší v rameni a pase, dětský se řídí výškou dítěte. Pokud název nic neříká, ověřte v popisu, pro koho je model určen.'),
        ('Kdy nakupovat trička Puma levněji?', 'Slevy se objevují především při výprodeji sezónních kolekcí, na konci léta a v zimě. Starší grafiky a barvy se slevují častěji než základní černé a bílé kusy. Ceny porovnejte přímo tady, protože se mezi obchody mohou výrazně lišit.'),
    ])

# ------------------------------------------------------------------ columbia-batoh
NEW['columbia-batoh'] = dict(
    title='Columbia batoh: Trail Traveler, Atlas Explorer, Convey',
    desc='Columbia batoh na výlet, do města i na cesty: modely Trail Traveler, Atlas Explorer, Convey Rolltop a skládací Lightweight Packable. Objemy a výběr.',
    intro='<p>Columbia je americká outdoorová značka, která se věnuje hlavně oblečení do hor, a její batohy tomu odpovídají: jsou praktické, jednoduché a míří na každodenní výlet spíš než na expedici. '
          'V nabídce kategorie <a href="/batohy/">batohy</a> najdete modely Trail Traveler a Atlas Explorer v objemu kolem osmadvaceti litrů, menší Trek, Tandem Trail a Zigzag, městské Buxton a Street Transit, rolltop Convey a skládací Lightweight Packable. '
          'Stránka vysvětluje, jak se jednotlivé řady liší, jaký objem se hodí na který účel, kdy má smysl rolltop a kdy klasický zip, jak batoh nastavit na záda a čím Columbia vyniká a čím naopak ne ve srovnání se značkami s technickými nosnými systémy. Obchody pak porovnáte podle barvy a skladovosti.</p>',
    guide='<h2>Co od batohu Columbia čekat</h2>'
          '<p>Značka je známá hlavně oblečením, a proto jsou její batohy stavěné jako doplněk výletní výbavy, ne jako technický nosič. Většina modelů nemá složitý nosný rám ani nastavitelná záda. '
          'Jde o jednoduché batohy do dvaceti pěti až třiceti litrů s polstrovanými zády, ramenními popruhy, někdy hrudním popruhem a kapsou na lahev. To úplně stačí na půlden i celodenní procházku s lehčí zátěží. '
          'Pokud ale plánujete víc dní s těžkým nákladem, hledejte u specializovaných značek s nosným systémem, například v kategorii <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          + T(['Název modelu', 'Objem v názvu', 'Použití'], [
              ['Trail Traveler II, Atlas Explorer', 'kolem 28 l', 'celodenní výlet, cesty, univerzál'],
              ['Convey III Rolltop', 'kolem 27 l', 'městský a cestovní batoh s rolovacím zavíráním'],
              ['Buxton, Echo Mountain', 'kolem 25 l', 'město, škola, lehký výlet'],
              ['Zigzag, Lightweight Packable II', 'kolem 21–22 l', 'denní batoh, skládací záložní kus do zavazadla'],
              ['Trek, Tandem Trail', 'kolem 16–18 l', 'krátká procházka, dětský a malý výlet'],
              ['Landroamer, Flawless', 'podle provedení, Flawless kolem 30 l a víc', 'cestovní a turistické použití'],
              ['Street Transit', 'městský', 'dojíždění do práce']]) +
          '<p>Přesný objem a rozměry si vždy ověřte v popisu konkrétního kusu: stejný název se může objevit ve více objemech a barvách. Údaj v litrech je jen orientační a hodnotu ovlivňuje i způsob měření.</p>'
          '<h2>Jaký objem zvolit</h2>'
          '<p>Pro krátké procházky a děti stačí šestnáct až osmnáct litrů. Obsahuje svačinu, láhev, pláštěnku a mikinu. Pro celodenní výlet v horách a běžné dojíždění je rozumné dvacet pět až osmadvacet litrů, kam se vejde i náhradní oblečení. '
          'Nad třicet litrů se dostanete s cestovními modely, které stačí na víkendovou cestu nebo letecké příruční zavazadlo; limit rozměrů si ale ověřte u dopravce. '
          'Příliš velký batoh se zaplní zbytečně a váha tlačí na ramena, takže raději volte menší objem s pevnými zády.</p>'
          '<h2>Rolltop a skládací batoh</h2>'
          '<p>Rolltop znamená zavírání rolováním horního okraje místo zipu. Výhodou je lepší odolnost proti dešti, protože vodu neprovede zip, a možnost přizpůsobit objem podle nákladu. Nevýhodou je pomalejší přístup k věcem a nutnost správně zavinout. '
          'Skládací modely Lightweight Packable se složí do kapsy a vejdou se do kufru nebo většího batohu. Jsou ideální jako záložní batoh na výlet z hotelu, ne jako denní nosič těžké zátěže, protože nemají tuhá záda ani výztuž. '
          'Pokud chcete vybírat podle stylu, podívejte se na <a href="/mestske-batohy/">městské a sportovní batohy</a>.</p>'
          '<h2>Městský, školní a cestovní provoz</h2>'
          '<p>Modely Buxton, Zigzag a Street Transit patří spíš do města a ke každodennímu dojíždění. Mají jednodušší tvar, dostatek kapes a často přihrádku na laptop. Pokud je vybíráte jako školní batoh, zkontrolujte vyztužení zad a polstrování ramenních popruhů. '
          'Přehled pro školáky najdete v kategorii <a href="/skolni-batohy/">školní a studentské batohy</a>. Pro cestu je praktický model s dobrým přístupem do hlavní komory a vnější kapsou na doklady; Landroamer a Flawless jsou označené jako cestovní nebo turistické.</p>'
          '<h2>Co sbalit do batohu na jednodenní výlet</h2>'
          '<p>Do batohu o objemu kolem dvaceti pěti litrů se vejde všechno potřebné na celý den. Základem je voda, svačina, lehká pláštěnka nebo bunda, náhradní vrstva a malá lékárnička. Přidejte mapu nebo nabitý telefon, čelovku na podzim a opalovací krém v létě. '
          'Těžké věci patří dovnitř blízko zad, lehké nahoru a do bočních kapes. Mokrý a špinavý oděv oddělte do sáčku, aby nezvlhl zbytek obsahu. Proti dešti vezměte lehkou pláštěnku, protože odolnost látky proti dlouhému dešti bývá omezená.</p>'
          + T(['Situace', 'Doporučený objem', 'Poznámka'], [
              ['Procházka s dítětem', '16–18 l', 'lehký batoh, hlavně svačina a pití'],
              ['Půlden v lese a v kopcích', '20–25 l', 'vrstva navíc a pláštěnka'],
              ['Celý den na túře', '25–30 l', 'jídlo, pití, bunda, lékárnička'],
              ['Víkend v penzionu', '30 l a víc', 'oblečení na dva dny, hygiena'],
              ['Dojíždění do práce', '20–27 l', 'notebook, oběd, boty na převlečení']]) +
          '<h2>Batoh pro děti a mladé</h2>'
          '<p>Menší modely Trek, Tandem Trail a Zigzag jsou po rozměrech vhodné i pro starší děti a mladé, které začínají s výlety. Důležité je, aby popruhy nesklouzávaly a aby batoh nevisel pod pasem. Dítě by nemělo nosit víc než desetinu své hmotnosti. '
          'Pro nejmenší děti jsou lepší skutečné dětské modely, které najdete mezi <a href="/detsky-batoh/">dětskými batohy</a>. Dospívající s výškou dospělého nosí klidně dvaceti až pětadvacetilitrový batoh a rychle ho přenese do běžného života.</p>'
          '<h2>Na co si dát pozor při koupi</h2>'
          '<ul><li><strong>Označení a objem:</strong> stejný název má více objemů; hledejte údaj v litrech přímo v popisu.</li>'
          '<li><strong>Typ zavírání:</strong> zip pro rychlý přístup, rolltop pro lepší odolnost vůči dešti.</li>'
          '<li><strong>Polstrování:</strong> záda a ramenní popruhy by měly být vystlané a v místech tření pevné.</li>'
          '<li><strong>Kapsy:</strong> boční na lahev, přední na drobnosti a případně vnitřní na notebook.</li>'
          '<li><strong>Hmotnost prázdného batohu:</strong> lehký batoh ušetří zátěž, ale může být méně odolný.</li></ul>'
          '<p>Nespoléhejte na to, že každý model Columbia je odolný vůči dešti. Voděodolná látka vydrží přeháňku, ale dlouhý déšť a ponor ne. Pro jistotu si do batohu dejte důležité věci do sáčku nebo použijte pláštěnku na batoh.</p>'
          '<h2>Jak nastavit batoh na záda</h2>'
          '<ol><li>Uvolněte popruhy a naložte nejtěžší věci blízko zad.</li>'
          '<li>Nasaďte batoh a zatáhněte ramenní popruhy tak, aby přiléhal k zádům a netlačil pod ramenem.</li>'
          '<li>Pokud je k dispozici hrudní popruh, zapněte ho ve výšce klíčních kostí.</li>'
          '<li>Bederní pás, je-li přítomen, dotáhněte na kyčle; nese část váhy a odlehčí ramenům.</li>'
          '<li>Po prvních kilometrech zkontrolujte popruhy a případně je doladěte.</li></ol>'
          '<p>Menší modely do osmnácti litrů obvykle bederní pás nemají, a proto je nezatěžujte víc než lehce. Rozhoduje i rozložení: těžké věci nahoru a blízko zad, měkké a objemné dolů.</p>'
          '<h2>Columbia ve srovnání s dalšími značkami</h2>'
          '<p>Značka Columbia je cenově dostupnější alternativou k technickým batohům a hodí se pro rekreační použití. Naproti tomu Osprey a Deuter vynikají nosnými systémy a dlouholetou specializací, takže na náročné trasy sáhněte spíš po jejich nabídce. '
          'Porovnat můžete <a href="/osprey-batoh/">batohy Osprey</a>, <a href="/deuter-batohy/">batohy Deuter</a> a <a href="/the-north-face-batoh/">batohy The North Face</a>, které míří na podobného zákazníka. '
          'Z životního stylu je blíž <a href="/fjallraven-batoh/">Fjällräven</a>, ze sportovních značek <a href="/nike-batoh/">Nike</a> a <a href="/adidas-batoh/">Adidas</a>. Pro konkrétní skupinu můžete také použít <a href="/damsky-batoh/">dámské batohy</a>, <a href="/pansky-batoh/">pánské batohy</a> a <a href="/detsky-batoh/">dětské batohy</a>.</p>'
          '<h2>Barvy a praktičnost</h2>'
          '<p>Nabídka zahrnuje černou, šedou, tmavě modrou, ale i růžovou, zelenou, žlutou, oranžovou nebo vínovou. Tmavé odstíny skryjí otěr a špínu a hodí se do města. Světlé a výrazné barvy jsou v terénu a v šeru lépe vidět, což ocení rodiče dětí na výletě. '
          'Barva nemá vliv na nosnost; rozhoduje jen střih a objem. Pokud kupujete batoh jako dárek, je jednobarevný model bezpečnější volbou než výrazný.</p>'
          '<h2>Péče o batoh</h2>'
          '<p>Po výletě batoh vyprázdněte, vytřepejte drobky a písek a otřete vlhkým hadříkem. Skvrny odstraňte jemným mýdlem a kartáčkem. V pračce se batoh ničí, protože poškozuje výztuže a lepené spoje. '
          'Před uložením jej nechte uschnout rozevřený a mimo přímé slunce. Zipy občas očistěte od písku. U rolltop modelů zkontrolujte okraj, aby nebyl zalomený nebo zalepený.</p>'
          '<h2>Jak hledat v nabídce</h2>'
          '<p>Při srovnání se podívejte nejen na objem, ale i na hmotnost, počet komor a zda jsou záda polstrovaná. Stejný název může být dostupný v různých barvách a ceny se v obchodech liší, proto využijte porovnání nabídek přímo na této stránce.</p>',
    faq=[
        ('Je batoh Columbia vhodný na turistiku?', 'Pro jednodenní a půldenní výlety ano. Modely Trail Traveler a Atlas Explorer mají kolem osmadvaceti litrů, polstrovaná záda a kapsy na lahev. Na vícedenní treky s těžkou zátěží raději zvolte batoh se specializovaným nosným systémem a nastavitelnou délkou zad.'),
        ('Jaký objem batohu Columbia je nejuniverzálnější?', 'Pro město i výlety se osvědčuje dvacet pět až osmadvacet litrů. Pojme laptop nebo oblečení na převlečení a stále se dobře nosí. Menší šestnáct až osmnáct litrů je ideální na procházku, větší cestovní modely pojmou víkendový výlet.'),
        ('Co znamená Rolltop u modelu Convey?', 'Horní okraj se zavírá rolováním a zacvaknutím, ne zipem. Lépe odolává dešti a objem lze mírně upravit. Přístup k obsahu je ale pomalejší a je nutné správně zavinout okraj. Pokud potřebujete rychlý přístup, vyberte raději klasický zip.'),
        ('K čemu je skládací batoh Lightweight Packable?', 'Složí se do malé kapsy a vejde se do kufru nebo většího batohu. Hodí se jako záložní batoh na výlet z hotelu nebo na nákup. Nemá tuhá záda ani výztuž, takže nevhodný na těžkou zátěž nebo celodenní nošení.'),
        ('Dá se batoh Columbia použít jako školní?', 'Ano, městské modely Buxton, Zigzag nebo Street Transit se hodí pro starší žáky a studenty. Zkontrolujte polstrování zad a ramenních popruhů a zda se vejdou učebnice. Pro mladší děti zvolte menší model a hlídejte, aby plný batoh nebyl příliš těžký.'),
        ('Jak batoh Columbia vyčistit?', 'Vlhkým hadříkem a jemným mýdlem, drobné nečistoty kartáčkem. Pračce se vyhněte, ničí výztuže a spoje. Před uložením nechte vyschnout rozevřený a mimo přímé slunce. Zipy očistěte od písku, aby neváznuly.'),
        ('Vejde se batoh Columbia jako příruční zavazadlo do letadla?', 'Záleží na rozměrech batohu a limitech konkrétního dopravce. Menší modely do zhruba dvaceti pěti litrů se obvykle vejdou pod sedadlo, větší cestovní modely nemusí. Změřte batoh naplněný a ověřte limity dopravce před odletem.'),
        ('Čím se Columbia liší od Osprey nebo Deuter?', 'Columbia je především oděvní značka a batohy jsou jednodušší, vhodné pro rekreační výlety. Osprey a Deuter se specializují na batohy s nosnými systémy, nastavitelnými zády a ventilací pro náročné trasy. Pro běžné denní použití je rozdíl menší než při vícedenním treku.'),
        ('Je batoh Columbia dostupný i v dámských barvách?', 'Ano, nabídka obsahuje růžovou, zelenou, žlutou, oranžovou nebo vínovou a další odstíny. Střih je většinou unisex, takže jde hlavně o barvu. Pro skutečný dámský střih s užšími popruhy se podívejte do kategorie dámské batohy.'),
        ('Kde porovnám ceny batohů Columbia?', 'Na této stránce vidíte nabídky více obchodů pro každý model, včetně barvy a dostupnosti. Můžete je porovnat a kliknout do e-shopu, který vám vyhovuje. Ceny i skladové zásoby se průběžně mění, takže před koupí ověřte aktuální stav.'),
    ])
