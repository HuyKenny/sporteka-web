"""sporteka.cz — brand page texts wave 227: napapijri, bushman, unuo, baagl, stanley, ea7-emporio-armani.
General facts only, no prices or counts; assortment taken from the live catalogue (17. 11. 2026)."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ napapijri
NEW['napapijri'] = dict(
    title='Napapijri: bundy Skidoo, mikiny, trička a čepice',
    desc='Napapijri v katalogu: bundy Skidoo a Rainforest, zimní a péřové bundy, mikiny, polokošile, tenisky i čepice. Jak vybrat střih a srovnat nabídky obchodů.',
    intro='<p>Napapijri je italská značka, kterou v Česku lidé hledají hlavně kvůli bundám. Typický je anorak Skidoo s norskou vlajkou na rukávu, ale sortiment je mnohem širší: přechodové a zimní bundy, mikiny, trička s potiskem, polokošile, čepice z vlněné směsi, tenisky, žabky a koupací šortky. '
          'Velká část kolekce je pánská, dámské a dětské modely tvoří menší podíl. '
          'Na této stránce sporteka.cz sbírá nabídky českých e-shopů, které značku prodávají, a řadí je vedle sebe, abyste viděli, kde je konkrétní model a velikost dostupná. Samotná objednávka pak proběhne přímo v obchodě, který si vyberete. '
          'Níže najdete průvodce řadami bund, rady k velikostem a péči o technické materiály a odpovědi na otázky, které se kolem této značky opakují nejčastěji.</p>',
    guide='<h2>Odkud Napapijri pochází</h2>'
          '<p>Značku založila v roce 1987 podnikatelka Giuliana Rosset v italském údolí Aosta, tedy v alpském regionu na hranici s Francií a Švýcarskem. Název je odvozený z finského slova napapiiri, které znamená polární kruh. Prvním výrobkem nebyla bunda, ale cestovní taška Bering z voskovaného plátna. Proslavil ji však až lehký anorak Skidoo s norskou vlajkou, který se z hor rychle přesunul do měst a dodnes je nejznámějším kusem kolekce.</p>'
          '<p>Od roku 2004 patří Napapijri do skupiny VF Corporation, pod kterou spadají také '
          + B(('the-north-face', 'The North Face'), ('timberland', 'Timberland'), ('vans', 'Vans')) +
          '. Sídlo firmy se mezitím přesunulo do švýcarského Stabia. V posledních sezónách značka spolupracuje s britskou návrhářkou Martine Rose; kusy s jejím jménem v názvu se objevují i v katalogu.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější skupinou jsou <a href="/tenisky/">tenisky</a>, následují <a href="/mikiny/">mikiny</a> a <a href="/sportovni-tricka/">trička</a> s krátkým i dlouhým rukávem. Silně jsou zastoupené <a href="/polokosile/">polokošile</a> a <a href="/sportovni-bundy-jaro-podzim/">přechodové bundy</a>, kam obchody řadí lehké bundy, anoraky i přechodové verze bund Rainforest. Do chladného počasí jsou určené <a href="/zimni-bundy/">zimní bundy</a>, například prošívané a péřové modely, a v menší míře i <a href="/lyzarske-bundy/">lyžařské bundy</a>. Doplňky tvoří <a href="/cepice-a-celenky/">čepice</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/pantofle-a-zabky/">žabky a pantofle</a>, koupací šortky a menší <a href="/mestske-batohy/">městské batohy</a>.</p>'
          + T(['Řada nebo typ', 'Charakter', 'Na co se hodí'], [
              ['Skidoo', 'anorak přes hlavu s kapucí a klokaní kapsou', 'vítr, přeháňky, město i výlet'],
              ['Rainforest', 'lehké i zimní bundy s kapucí, verze Winter se zateplením', 'jaro, podzim, u verze Winter i zima'],
              ['Prošívané a péřové bundy', 'zateplení s prošitými komorami', 'zima ve městě, delší pobyt venku'],
              ['Mikiny a fleece', 'bavlna nebo fleece, s kapucí i bez', 'vrstva pod bundu, volný čas'],
              ['Polokošile a trička', 'bavlněný úplet s logem', 'léto, kancelář s volnějším dress codem'],
              ['Čepice a doplňky', 'pletené čepice, kšiltovky, šály', 'do chladného a větrného počasí']]) +
          '<h2>Skidoo: jak poznat správný anorak</h2>'
          '<p>Skidoo se obléká přes hlavu. Má krátký zip u krku, velkou přední kapsu, kapuci a stahovací šňůrky v pase. Kromě lehké verze bez zateplení se během let objevily i varianty s podšívkou nebo výplní a lyžařská bunda Skidoo 2.0, proto u každého kusu čtěte popis materiálu. U bund Rainforest prozradí zateplenou verzi doplněk Winter v názvu. Před nákupem si ujasněte, zda chcete hlavně vrstvu proti větru a dešti na přechodné období, nebo kus, který nahradí zimní bundu.</p>'
          '<p>Lehký anorak nemá zateplení, proto se pod něj v zimě vejde mikina nebo fleece. Pokud plánujete takové vrstvení, zvolte o číslo větší velikost nebo model se volnějším střihem. U zateplených verzí to naopak nedělejte, protože by bunda na těle visela a v pase do ní táhlo.</p>'
          '<h2>Velikosti a střih</h2>'
          '<p>Italská konfekce bývá u některých modelů užší v ramenou a kratší v rukávech, než jsou zvyklí zákazníci severských nebo amerických značek. Proto se vyplatí otevřít tabulku velikostí u konkrétní nabídky a porovnat obvod hrudníku a délku rukávu se svou oblíbenou bundou. U polokošil a triček se střihy liší podle řady: některé jsou rovné, jiné vypasované nebo naopak oversize. V názvu se to často neuvádí, proto čtěte popis a fotky na postavě.</p>'
          '<ol><li>Změřte obvod hrudníku přes tričko, ne přes svetr.</li>'
          '<li>U bund ověřte délku rukávu od švu na rameni po zápěstí.</li>'
          '<li>U anoraku přes hlavu počítejte s tím, že se hůř obléká, když je příliš těsný.</li>'
          '<li>U dámských modelů hledejte označení dámská, protože unisex střih je obvykle podle pánských měr.</li></ol>'
          '<h2>Zimní a péřové bundy</h2>'
          '<p>Do mrazu jsou v nabídce prošívané bundy s umělou výplní i péřové modely, mezi nimi například řada s názvem A-Molveno nebo zateplená bunda Arnil. Rozdíl je praktický: péří je lehčí a lépe hřeje při stejné tloušťce, ale po namočení ztrácí objem. Syntetická výplň snáší vlhko lépe a je méně náročná na praní. Podrobněji o rozdílech píšeme v kategoriích <a href="/perove-bundy/">péřové bundy</a> a <a href="/panska-zimni-bunda/">pánská zimní bunda</a>. Na hory obchody nabízejí i lyžařské bundy, například model Skidoo 2.0; před nákupem si v popisu ověřte zateplení a sněhový pás.</p>'
          '<h2>Mikiny, trička a polokošile</h2>'
          '<p>Mikiny tvoří druhou největší skupinu. Vybírat lze mezi modely s kapucí a bez ní, celopropínacími a přetahovacími a mezi bavlněným úpletem a fleecem. Fleecová mikina Equipe nebo podobné modely zahřejí i pod lehkou bundou a rychle schnou. Trička jsou převážně bavlněná, s malým nebo velkým logem a v klidných barvách, takže se snadno kombinují. Polokošile se hodí do léta i do práce, kde nemusíte nosit košili; více porovnání najdete v přehledu <a href="/panske-polokosile/">pánské polokošile</a>.</p>'
          '<h2>Obuv a letní doplňky</h2>'
          '<p>Velkou část nabídky tvoří tenisky do města a v menší míře i <a href="/trekova-obuv/">treková obuv</a>. Nejde o specializované boty do hor, ale o pohodlnou obuv na každý den s výraznějším designem. K moři a k bazénu se nabízejí žabky a koupací šortky, například řada Haldane. U obuvi platí totéž co u oblečení: velikosti se mohou mezi modely lišit, proto ověřte délku stélky v centimetrech.</p>'
          '<h2>Batohy a tašky</h2>'
          '<p>Značka začínala cestovní taškou, a tak není divu, že do kolekce stále patří batohy a tašky. V katalogu jich je méně než oblečení, převažují městské batohy na notebook a menší tašky přes rameno. Hodí se do školy, do práce nebo na víkendový výlet. U batohu sledujte objem v litrech, polstrování zad a to, zda má oddělenou kapsu na počítač. Na delší túru s těžkým nákladem raději vyberte <a href="/turisticke-batohy/">turistický batoh</a> s bederním pásem.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Názvy produktů u Napapijri často začínají písmenem a pomlčkou, například A-Ega, A-Glane nebo F-Vispa. Při hledání stejného modelu v jiných obchodech zadávejte celý název včetně písmene, jinak vám vyhledávání nabídne příbuzné kusy. Některé e-shopy uvádějí jen obecný název bunda nebo mikina, proto se vyplatí porovnat fotky a kód produktu. Stejný model se navíc často prodává v mnoha barvách, mezi kterými se může lišit cena i dostupnost velikostí.</p>'
          '<h2>Pro koho se Napapijri hodí</h2>'
          '<p>Značka vyhovuje lidem, kteří chtějí oblečení použitelné ve městě i na nenáročném výletě a mají rádi výraznější design s logem. Anorak Skidoo oceníte při jízdě na kole po městě, na procházce v dešti nebo na festivalu. Pro vysokohorskou turistiku, skialpinismus nebo dlouhé treky ale hledejte specializované vybavení s membránou a pevnějšími švy. Napapijri je spíše volnočasová značka s outdoorovými kořeny než výbava pro expedice.</p>'
          '<h2>Péče o technické materiály</h2>'
          '<ul><li>Bundy perte podle štítku, obvykle na nízkou teplotu a bez aviváže, která zhoršuje odpudivost vody.</li>'
          '<li>Před praním zapněte zipy a suché zipy, aby nepoškodily látku.</li>'
          '<li>Vodoodpudivou úpravu lze po čase obnovit impregnací ve spreji nebo do pračky.</li>'
          '<li>Péřové bundy suště v sušičce s tenisovými míčky, aby se péří znovu rozprostřelo.</li>'
          '<li>Bavlněná trička a mikiny perte naruby, potisk tak vydrží déle.</li></ul>'
          '<h2>Konkurence a srovnání</h2>'
          '<p>Napapijri stojí na pomezí outdooru a městské módy. Kdo potřebuje bundu do náročného terénu s membránou, najde specializovanější výběr u značek '
          + B(('the-north-face', 'The North Face'), ('columbia', 'Columbia'), ('helly-hansen', 'Helly Hansen')) +
          '. Kdo chce hlavně výrazný kus do města, který zvládne i výlet, je u Napapijri správně. Podobnou volnočasovou linii nabízí také '
          + B(('tommy-hilfiger', 'Tommy Hilfiger'), ('timberland', 'Timberland')) +
          '. Rozhodující bývá střih a konkrétní model, nikoli samotné logo.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Přechodové bundy a anoraky se nejvíc prodávají na jaře a na podzim, zimní modely od října do prosince. Výprodeje přicházejí po skončení sezóny, tedy u zimních bund v lednu a únoru a u letních triček a polokošil koncem léta. Starší barevné varianty Skidoo se často zlevňují, když přichází nová kolekce. Sledujte vývoj ceny u konkrétního produktu a zapněte si hlídání, pokud čekáte na svou velikost.</p>',
    faq=[
        ('Odkud pochází značka Napapijri?',
         'Vznikla v roce 1987 v italském údolí Aosta. Založila ji Giuliana Rosset a od roku 2004 patří do skupiny VF Corporation. Dnes sídlí ve švýcarském Stabiu.'),
        ('Co znamená název Napapijri?',
         'Vychází z finského slova napapiiri, tedy polární kruh. Odkaz na sever připomíná i norská vlajka, kterou nosí anoraky Skidoo.'),
        ('Které bundy Napapijri jsou nejznámější?',
         'Anorak Skidoo s norskou vlajkou, který se obléká přes hlavu, a bundy Rainforest. Obě řady existují v lehkém i zateplenějším provedení, u Rainforest poznáte zimní verzi podle slova Winter.'),
        ('Hřeje anorak Skidoo i v zimě?',
         'Základní lehká verze nemá zateplení a v zimě potřebuje pod sebe mikinu nebo fleece. Pro mrazy hledejte model s výplní nebo rovnou zimní či péřovou bundu.'),
        ('Jak padnou velikosti Napapijri?',
         'U některých modelů jsou užší ramena a kratší rukávy. Vždy porovnejte tabulku u konkrétní nabídky se svou bundou a u anoraku přes hlavu nevolte příliš těsnou velikost.'),
        ('Najdu u Napapijri i dámské a dětské oblečení?',
         'Ano, ale v menším výběru. Většina nabídky je pánská, dámské modely jsou mezi bundami, mikinami a tričky. U unisex kusů počítejte s pánskými mírami.'),
        ('Jsou boty Napapijri vhodné na turistiku?',
         'Jde hlavně o tenisky a obuv do města. Pro lehké výlety stačí, do hor s batohem raději vyberte specializovanou trekovou obuv s pevnou podešví.'),
        ('Jak prát bundu Napapijri?',
         'Podle štítku, obvykle na nízkou teplotu, se zapnutými zipy a bez aviváže. Odpudivost vody po čase obnoví impregnace, péřové bundy dosušte v sušičce s míčky.'),
        ('Kdy bývají bundy Napapijri levnější?',
         'Zimní modely obvykle zlevňují v lednu a únoru, přechodové bundy po jarní a podzimní sezóně. Starší barvy zlevňují s příchodem nové kolekce.'),
        ('Prodává sporteka.cz zboží Napapijri?',
         'Ne. Sporteka srovnává nabídky českých obchodů, ukáže dostupné velikosti a odkáže vás na e-shop, kde nákup dokončíte za jeho podmínek dopravy a vrácení.'),
    ],
)

# ------------------------------------------------------------------ bushman
NEW['bushman'] = dict(
    title='Bushman: české outdoorové a volnočasové oblečení',
    desc='Bushman v katalogu: trička, košile, polokošile, kalhoty, mikiny, bundy, šaty a tašky z přírodních materiálů. Jak vybrat velikost a srovnat obchody.',
    intro='<p>Bushman je česká značka oblečení na cesty a do přírody, která se drží zemitých barev a materiálů jako bavlna, len nebo vlna. V nabídce převažují pánská a dámská trička, dále košile, polokošile, kalhoty, mikiny, přechodové a zimní bundy, vesty, šaty a sukně. K tomu patří tašky přes rameno, městské batohy a drobné doplňky. '
          'Typické jsou jednoslovné názvy modelů psané velkými písmeny, například NAKO, DALVIK nebo FJORD, a široká škála khaki, hnědých, vínových a tmavě zelených odstínů. '
          'Sporteka zde přehledně staví vedle sebe nabídky e-shopů, které Bushman prodávají, abyste mohli porovnat dostupnost barev a velikostí. Zboží si pak objednáte u obchodu, který vám vyhovuje. '
          'Následující průvodce popisuje historii značky, jednotlivé skupiny oblečení a to, na co si dát pozor u velikostí a praní přírodních materiálů.</p>',
    guide='<h2>Historie značky Bushman</h2>'
          '<p>Bushman vznikl v roce 1997. Jeho zakladatel Jindřich Melichar podle vlastních slov tehdy hodně cestoval a chybělo mu oblečení, které by bylo pohodlné a vydrželo dlouhé putování. Z vlastních zkušeností a postřehů lidí potkaných na cestách sestavil první kolekci. Název si firma vypůjčila z australské angličtiny, kde označuje svobodomyslného člověka žijícího v buši. Anglické jméno v devadesátých letech pomohlo překonat nedůvěru k domácím značkám, dnes je ale Bushman vnímaný jako česká firma.</p>'
          '<p>Značka si prošla i složitým obdobím. Neúspěšná expanze do Spojených států ji oslabila, firmu pak stabilizoval investiční fond a od roku 2019 ji vede nový management. Provozuje síť vlastních prodejen v Česku a na Slovensku a působí také v dalších evropských zemích. Výrobce každý rok připravuje dvě kolekce, jednu pro teplé a jednu pro chladné období, a jejich základ tvoří osvědčené modely, které se jen upravují.</p>'
          '<h2>Co Bushman v katalogu nabízí</h2>'
          '<p>Největší skupinou jsou <a href="/sportovni-tricka/">trička</a>, pánská i dámská, s krátkým i dlouhým rukávem. Následují <a href="/kosile/">košile</a> s typickým cestovatelským střihem, <a href="/mikiny/">mikiny</a>, <a href="/sportovni-kalhoty/">kalhoty</a> a <a href="/sportovni-bundy-jaro-podzim/">přechodové bundy</a>. Menší zastoupení mají <a href="/polokosile/">polokošile</a>, <a href="/zimni-bundy/">zimní bundy</a>, <a href="/sportovni-vesty/">vesty</a>, <a href="/sportovni-kratasy/">kraťasy</a> a dámské <a href="/sportovni-sukne-a-saty/">šaty a sukně</a>. Z doplňků se nabízejí <a href="/tasky-pres-rameno/">tašky přes rameno</a>, <a href="/mestske-batohy/">městské batohy</a> a drobnosti v kategorii <a href="/outdoor-doplnky/">outdoorové doplňky</a>.</p>'
          + T(['Skupina', 'Typický materiál', 'Kdy se hodí'], [
              ['Trička a polokošile', 'bavlna, směsi s lnem nebo bambusem', 'léto, cestování, volný čas'],
              ['Košile', 'bavlna, len, flanel', 'výlety i běžné nošení do města'],
              ['Kalhoty a kraťasy', 'pevná bavlna, směsi s elastanem', 'chůze, cestování, práce venku'],
              ['Mikiny a vesty', 'bavlněný úplet, zateplení', 'přechodné období, vrstva pod bundu'],
              ['Bundy', 'bavlna s úpravou, syntetické zateplení', 'jaro, podzim, zima ve městě'],
              ['Tašky a batohy', 'plátno, kůže, odolné tkaniny', 'každodenní nošení a cestování']]) +
          '<h2>Přírodní materiály a co z nich plyne</h2>'
          '<p>Bushman staví kolekce převážně na přírodních vláknech: bavlně, vlně, lnu, bambusu a kůži. Výhodou je příjemný omak, dobrá prodyšnost a to, že se materiál na konci životnosti snáze recykluje. Má to ale i praktické důsledky. Bavlna nasákne vodu a schne pomaleji než syntetika, takže tričko z ní není ideální na rychlý výstup do kopce, kde se hodně potíte. Len se mačká, což k jeho vzhledu patří. Vlna hřeje i ve vlhku, ale potřebuje šetrné praní.</p>'
          '<p>Pro sportovní výkon proto Bushman není první volbou. Na běh nebo náročnou túru se hodí spíše <a href="/funkcni-tricka/">funkční trička</a> ze syntetiky nebo merina. Bushman se uplatní na cestách, při procházkách, v kempu, na chatě i ve městě, kde chcete vypadat upraveně a zároveň se pohybovat pohodlně.</p>'
          '<h2>Kalhoty: střih, kapsy a délka</h2>'
          '<p>Kalhoty jsou pro značku klíčové. V katalogu se objevují například pánské modely NAKO a SALVE nebo dámské KISTA. Bývají z pevné bavlněné tkaniny, často s příměsí elastanu pro volnější pohyb v kolenou. Před nákupem zkontrolujte tři věci: obvod pasu, délku nohavice a typ střihu. Rovný střih se hodí na cestování, užší na nošení do města. Kapsy na zip ocení každý, kdo nosí doklady na výletech.</p>'
          '<ul><li>Změřte obvod pasu v místě, kde kalhoty skutečně nosíte.</li>'
          '<li>Délku nohavice porovnejte s kalhotami, které vám sedí, měřeno po vnitřním švu.</li>'
          '<li>U bavlny počítejte s mírným srážením po prvním praní, pokud výrobce neuvádí jinak.</li>'
          '<li>Na túry v horku jsou příjemnější lehčí modely nebo kraťasy.</li></ul>'
          '<h2>Bundy a vesty do chladnějšího počasí</h2>'
          '<p>Přechodové bundy, například pánské JENS a HENDRIK nebo dámské MALIKKA a ANDREA, mají obvykle klasický střih s kapsami a límcem. Nejde o technické bundy s membránou do bouřky, ale o oblečení na běžné jarní a podzimní dny. Pro zimu jsou v nabídce zateplené modely, například FJORD, a vesty jako ARNO, které zahřejí trup a nechají volné paže. Pokud čekáte silný déšť, kombinujte je s <a href="/nepromokave-bundy/">nepromokavou bundou</a> nebo pláštěnkou.</p>'
          '<h2>Jak sedí velikosti</h2>'
          '<p>Bushman šije pánské i dámské střihy zvlášť, takže unisex kusy tvoří jen malou část nabídky. Pánská trička a košile bývají střižená spíše rovně, dámské modely jsou vypasovanější. U košil se vyplatí zkontrolovat šířku přes ramena a délku rukávu, u triček délku zad. Výrobce na svých stránkách zveřejňuje průvodce velikostmi; v obchodech najdete tabulku u každého modelu. Při objednávce dvou velikostí na zkoušku si předem ověřte podmínky vrácení u vybraného e-shopu.</p>'
          '<h2>Dámská kolekce</h2>'
          '<p>Dámská část nabídky není jen zmenšenou verzí pánské. Najdete v ní šaty, například KATLA nebo RUNA, sukně, košile s ženským střihem, jako je LILLE, a trička MIA, SABINE nebo NARSA. Šaty z bavlny nebo viskózy se hodí na léto ve městě i na dovolenou, kde chcete jeden kus na den i na večer. Dámské mikiny AKIA nebo YLVA zase poslouží jako vrstva na chladnější večery u vody nebo v horách. Velikosti dámských modelů se řídí vlastní tabulkou, proto neodvozujte číslo od pánských kusů.</p>'
          '<h2>Tašky a batohy na cesty</h2>'
          '<p>Doplňky tvoří menší, ale zajímavou část nabídky. Tašky přes rameno se hodí na doklady, telefon a peněženku při cestování, městské batohy na každodenní nošení do práce. Některé jsou z plátna, jiné s koženými detaily. Na výlet do hor s větším nákladem se ale hodí spíše specializovaný <a href="/turisticke-batohy/">turistický batoh</a> s nosným systémem a bederním pásem.</p>'
          '<h2>Jak sbalit oblečení na cestu</h2>'
          '<p>Filozofie značky stojí na tom, že jedno oblečení zvládne více situací. Na týdenní cestu proto obvykle stačí dvoje kalhoty, z nichž jedny mohou být kraťasy, tři až čtyři trička, jedna košile s dlouhým rukávem proti slunci a komárům, mikina nebo vesta a lehká bunda. Když se barvy navzájem hodí, vytvoříte z několika kusů mnoho kombinací. Bavlněná trička se dají přeprat v umyvadle, jen počítejte s tím, že schnou přes noc.</p>'
          '<h2>Polokošile a trička na léto</h2>'
          '<p>Pánská polokošile, například ELISON nebo ITILLEQ, je dobrá volba na cesty do teplých zemí, protože límec chrání krk před sluncem a zároveň působí upraveněji než obyčejné tričko. Trička PRIME II, GUNN nebo WRAY II patří k základům kolekce a vracejí se v nových barvách. U letních kusů sledujte gramáž a složení: lehčí bavlna nebo směs se lnem je v horku příjemnější, silnější úplet zase lépe drží tvar.</p>'
          '<h2>Barvy a kombinování</h2>'
          '<p>Většina kolekce je v tlumených tónech: khaki, hnědá, béžová, tmavě zelená, vínová, tmavě šedá a modrá. Díky tomu se kusy z různých sezón snadno kombinují a na cestách vystačíte s menším počtem věcí. Na fotkách v různých obchodech může stejná barva působit odlišně, proto se vyplatí podívat i na detailní snímek látky.</p>'
          '<h2>Praní a péče</h2>'
          '<ul><li>Bavlnu a len perte naruby na teplotu ze štítku a nesušte v sušičce, pokud to výrobce nepovoluje.</li>'
          '<li>Vlněné kusy perte na vlnový program a suště naplocho.</li>'
          '<li>Kožené tašky a doplňky ošetřujte přípravkem na kůži a chraňte před dlouhým deštěm.</li>'
          '<li>Bundy s úpravou proti vodě obnovte impregnací, jakmile voda přestane perlit.</li></ul>'
          '<h2>Bushman a podobné značky</h2>'
          '<p>Na českém trhu má Bushman blízko ke značkám, které spojují přírodu a město. Technicky zaměřené oblečení najdete u '
          + B(('husky', 'Husky'), ('northfinder', 'Northfinder'), ('alpine-pro', 'Alpine Pro')) +
          ', klasický skandinávský outdoor s důrazem na odolnost u '
          + B(('fjallraven', 'Fjällräven'),) +
          '. Bushman je méně sportovní a více cestovatelský: hodí se tam, kde chcete jedno oblečení na výlet, do kavárny i na cestu letadlem.</p>'
          '<h2>Kdy nakupovat výhodněji</h2>'
          '<p>Letní trička, košile a šaty se nejčastěji zlevňují v druhé polovině léta, zimní bundy a vesty po Vánocích a na konci zimy. Protože značka každou sezónu obměňuje barvy, starší varianty oblíbených modelů se objevují ve výprodejích. U trička nebo kalhot, které se vám osvědčily, se vyplatí sledovat cenu a koupit dvě barvy najednou, když klesne.</p>',
    faq=[
        ('Je Bushman česká značka?',
         'Ano. Vznikla v roce 1997 v Česku a za značkou stojí Bushman company, a. s. Anglický název je inspirovaný australským výrazem pro svobodomyslného člověka z buše.'),
        ('Kdo Bushman založil?',
         'Zakladatelem je Jindřich Melichar, který první kolekci sestavil na základě zkušeností z vlastních cest. Od roku 2019 vede firmu nový management.'),
        ('Z jakých materiálů je oblečení Bushman?',
         'Převážně z přírodních vláken, tedy bavlny, lnu, vlny a bambusu, a doplňky také z kůže. U konkrétního kusu vždy ověřte složení v popisu produktu.'),
        ('Hodí se Bushman na sport?',
         'Spíše ne. Bavlna schne pomalu, proto na běh nebo intenzivní výstup volte funkční trička. Bushman se hodí na cestování, procházky, výlety a běžné nošení.'),
        ('Jak vybrat velikost kalhot Bushman?',
         'Změřte obvod pasu a vnitřní délku nohavice a porovnejte je s tabulkou u modelu. U bavlny počítejte s možným mírným srážením po prvním praní.'),
        ('Jsou bundy Bushman nepromokavé?',
         'Většina přechodových bund je určena na běžné počasí, nikoli na prudký déšť. Do deště je lepší přidat nepromokavou bundu nebo pláštěnku s membránou.'),
        ('Najdu u Bushman i dámské oblečení?',
         'Ano. Nabídka zahrnuje dámská trička, košile, mikiny, kalhoty, bundy, šaty a sukně. Dámské modely mají vlastní vypasovanější střihy.'),
        ('Jak prát lněnou nebo bavlněnou košili?',
         'Naruby, na teplotu podle štítku a bez sušičky, pokud ji výrobce nepovoluje. Len se mačká, žehlete ho ještě mírně vlhký.'),
        ('Kdy bývá Bushman ve slevě?',
         'Letní kolekce obvykle zlevňuje v druhé polovině léta, zimní na konci zimy. Starší barevné varianty se objevují ve výprodejích při příchodu nové sezóny.'),
        ('Mohu Bushman koupit přímo na sporteka.cz?',
         'Ne, sporteka.cz je srovnávač. Ukáže, které české e-shopy model nabízejí, a po kliknutí přejdete do obchodu, kde objednávku dokončíte.'),
    ],
)

# ------------------------------------------------------------------ unuo
NEW['unuo'] = dict(
    title='UNUO: dětské softshellové kalhoty, bundy a čepice',
    desc='UNUO v katalogu: dětské softshellové kalhoty a bundy, oteplovačky, fleece, čepice a nákrčníky. Jak vybrat velikost s rezervou a porovnat nabídky obchodů.',
    intro='<p>UNUO je česká značka funkčního oblečení pro děti, které tráví hodně času venku. Nejčastěji se hledají softshellové kalhoty a bundy, k nim patří zimní bundy, rostoucí oteplovačky, fleecové mikiny, čepice, nákrčníky, rukavice a termoprádlo. Menší část nabídky tvoří dámské softshellové bundy a funkční kalhoty pro rodiče. '
          'Typické jsou veselé potisky a řady s názvy Basic, Street, Sporty nebo Polar, které se liší zateplením a střihem. '
          'Sporteka přináší na jedno místo nabídky českých obchodů s oblečením UNUO, takže snadno zjistíte, kde je skladem potřebná velikost a vzor. Nakupujete pak na e-shopu, který si sami zvolíte. '
          'V průvodci níže vysvětlujeme rozdíly mezi řadami, vrstvení podle počasí a výběr velikosti tak, aby oblečení vydrželo víc než jednu sezónu.</p>',
    guide='<h2>Kdo stojí za značkou UNUO</h2>'
          '<p>Značku založila Petra Plemlová, původně učitelka v mateřské škole. Začínala doma se šicím strojem, nejdřív šila pro vlastní děti a prodávala látky s vlastními potisky. Právě zkušenosti ze školky jí pomohly navrhnout oblečení, které se dětem dobře obléká a vydrží hraní venku. Firma se postupně přestěhovala z Prahy do Tábora a pod jménem Unuodesign dodnes prodává i dětské metráže.</p>'
          '<p>Podle vlastních informací UNUO navrhuje všechny produkty samo a většinu jich šije ve své dílně v Táboře na jihu Čech. Co nedokáže vyrobit doma, zadává ověřeným zahraničním dílnám. Oblečení se prodává i v dalších evropských zemích.</p>'
          '<h2>Co UNUO v katalogu nabízí</h2>'
          '<p>Jádrem sortimentu jsou <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, v naprosté většině softshellové, a <a href="/softshellove-bundy/">softshellové bundy</a>. Druhou velkou skupinou jsou <a href="/cepice-a-celenky/">čepice</a> z fleece, teplákoviny i pleteniny a <a href="/nakrcniky-a-satky/">nákrčníky</a>. Na zimu jsou tu <a href="/zimni-bundy/">zimní bundy</a>, <a href="/kombinezy/">kombinézy</a> a oteplovačky, k vrstvení <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/funkcni-tricka/">funkční trička</a> a <a href="/termopradlo/">termoprádlo</a>. Doplňují je <a href="/sportovni-rukavice/">rukavice</a>, merino trička, <a href="/nepromokave-bundy/">nepromokavé bundy</a>, plavky a dětské batohy.</p>'
          + T(['Řada nebo typ', 'Zateplení', 'Kdy ji obléknout'], [
              ['Softshell bez zateplení (Basic, Street, Sporty)', 'žádné, jen softshell', 'jaro, léto za chladnějších dnů, podzim'],
              ['Softshell s fleecem', 'fleecová podšívka', 'podzim, mírná zima, procházky'],
              ['Softshell s beránkem (Light)', 'hustší beránková podšívka', 'chladné dny a mírný mráz'],
              ['Oteplovačky Polar, Ski', 'zateplené, rostoucí', 'sníh, sáňkování, zima'],
              ['Fleece a termoprádlo', 'vrstva pod bundu', 'celý rok podle počasí'],
              ['Čepice, nákrčníky, rukavice', 'fleece, teplákovina, pletenina', 'vítr a zima']]) +
          '<h2>Softshell: s fleecem, nebo bez?</h2>'
          '<p>Softshell je pružná tkanina, která odolá větru a lehkému dešti a zároveň dobře propouští páru. Pro děti je praktický, protože vydrží klouzání po skluzavce i lezení po stromech. U UNUO se nabízí ve třech hlavních variantách. Model bez zateplení je nejlehčí a hodí se na jaro, léto za chladnějších dnů nebo jako vrchní vrstva přes mikinu. Varianta s fleecem má měkkou podšívku a stačí na většinu podzimních a mírně zimních dnů. Kalhoty s beránkem hřejí nejvíc a zvládnou i chladné ráno ve školce.</p>'
          '<p>Pokud kupujete jen jedny kalhoty na celý rok, většina rodičů sáhne po verzi s fleecem. V létě ale může být teplá a v mrazu už nestačí. Rozumnější bývá kombinace lehkého softshellu a zimních oteplovaček. Více o materiálu najdete v kategorii <a href="/detska-softshellova-bunda/">dětská softshellová bunda</a>.</p>'
          '<h2>Velikosti a rostoucí střih</h2>'
          '<p>Děti rostou rychle, a tak se vyplatí oblečení, které vydrží déle. UNUO u některých zimních oteplovaček, například řad Polar a Ski, uvádí rostoucí provedení, které má prodloužit dobu nošení; jak přesně funguje, popisuje výrobce u konkrétního modelu. U softshellových kalhot se doporučuje vybírat podle aktuální výšky dítěte s malou rezervou, nikoli o dvě čísla větší: příliš dlouhé nohavice se zachytávají a padají do bláta.</p>'
          '<ol><li>Změřte výšku dítěte bez bot a porovnejte ji s tabulkou u modelu.</li>'
          '<li>U kalhot zkontrolujte délku nohavice a to, zda má gumu v pase nebo regulaci.</li>'
          '<li>U bundy počítejte s místem pro mikinu pod ní.</li>'
          '<li>U batolecích modelů ověřte, že se kalhoty vejdou přes plenu.</li></ol>'
          '<h2>Vrstvení podle počasí</h2>'
          '<p>Dítě se při hraní zahřeje a pak rychle prochladne. Proto je lepší obléct několik tenčích vrstev než jednu tlustou. Na tělo patří funkční nebo merino triko, které odvádí pot. Druhou vrstvou je fleecová mikina, vrchní vrstvou softshell nebo zimní bunda. Při sněhu a mokru přidejte oteplovačky a nepromokavé rukavice. Pro nejmenší se v zimě hodí i <a href="/detske-termopradlo/">dětské termoprádlo</a>.</p>'
          '<h2>Čepice, nákrčníky a doplňky</h2>'
          '<p>Čepice tvoří velkou část nabídky: fleecové, z teplákoviny i pletené, často v sadě s nákrčníkem. Nákrčník je pro malé děti bezpečnější než šála, protože se nezachytí na prolézačce. Fleecové modely jsou vhodné na podzim a do větru, pletené s podšívkou do mrazu. Ke kompletní výbavě do školky patří také dětský batoh; srovnání najdete na stránce <a href="/detsky-batoh/">dětský batoh</a>.</p>'
          '<h2>Reflexní prvky a bezpečnost</h2>'
          '<p>Na podzim a v zimě se brzy stmívá a děti se vracejí ze školy nebo z kroužků za šera. Některé bundy a čepice UNUO mají reflexní obrázek, který řidič zahlédne ve světle reflektorů. Při výběru se podívejte, kde přesně reflexní prvek je, a pokud je jen na jedné straně, doplňte ho reflexní páskou nebo přívěskem. U tmavých barev je to obzvlášť důležité. Malé děti ocení i zipy s velkým jezdcem, se kterými si poradí samy v rukavicích.</p>'
          '<h2>Výbava do školky a na výlet</h2>'
          '<p>Rodiče se často ptají, co přesně dítěti pořídit do školky, kde chodí ven za každého počasí. Osvědčený základ vypadá takto:</p>'
          '<ul><li>dvoje softshellové kalhoty, jedny lehké a jedny s fleecem, aby se mohly prát a střídat,</li>'
          '<li>softshellovou bundu a na zimu zateplenou bundu nebo kombinézu,</li>'
          '<li>oteplovačky do sněhu a nepromokavé rukavice,</li>'
          '<li>dvě čepice, tenčí a teplejší, a nákrčník místo šály,</li>'
          '<li>funkční triko a fleecovou mikinu jako mezivrstvu,</li>'
          '<li>náhradní ponožky a spodní prádlo v batůžku.</li></ul>'
          '<p>Na celodenní výlety přidejte nepromokavou bundu nebo pláštěnku a lahev s pitím. Všechno podepište, ve školce se oblečení snadno zamění.</p>'
          '<h2>Merino a termoprádlo</h2>'
          '<p>V nabídce jsou také merino trička a doplňky a dětské termo trika. Merino je jemná vlna, která hřeje i ve vlhku, nekouše a méně zapáchá, takže ho dítě může nosit více dní. Syntetické termoprádlo rychleji schne a je odolnější při praní. Na zimní výlety, lyžování nebo sáňkování je kvalitní spodní vrstva stejně důležitá jako bunda. Další možnosti srovnáváme v kategorii <a href="/merino-tricka/">merino trička</a>.</p>'
          '<h2>Léto a voda</h2>'
          '<p>UNUO nemyslí jen na zimu. V katalogu jsou i dětské plavky a lehké funkční kalhoty, které se hodí na letní tábory a do přírody. Softshell bez zateplení zase poslouží za chladného letního večera nebo v horách, kde se počasí rychle mění.</p>'
          '<h2>Oblečení pro rodiče</h2>'
          '<p>Menší část sortimentu tvoří dámské softshellové bundy a funkční kalhoty. Jsou šité stejným způsobem jako dětské a hodí se rodičům, kteří chodí s dětmi ven za každého počasí. Mají jednoduchý střih a často stejné potisky jako dětská řada.</p>'
          '<h2>Jak poznat kvalitní dětský softshell</h2>'
          '<p>Při porovnávání nabídek se nedívejte jen na vzor. Rozhoduje několik detailů, které se v popisu produktu obvykle dají dohledat. Vodní sloupec udává, jak velkému tlaku vody materiál odolá, a paropropustnost říká, jak dobře odvádí vlhkost od těla. Důležité jsou také podlepené nebo dobře šité švy v sedu a na kolenou, kde dítě nejčastěji klečí v mokré trávě. Gumička nebo poutko pod chodidlo drží nohavici v botě, takže do ní nenapadá sníh. U bundy oceníte kapuci, kterou lze odepnout, a manžety, které nepustí vítr do rukávů.</p>'
          '<h2>Praní softshellu</h2>'
          '<ul><li>Perte na nízkou teplotu a bez aviváže, která ucpává póry membrány.</li>'
          '<li>Před praním zapněte zipy a vyprázdněte kapsy, v dětských kalhotách se najdou kamínky i kaštany.</li>'
          '<li>Nedávejte softshell do sušičky, pokud to štítek nepovoluje.</li>'
          '<li>Když voda přestane perlit, použijte impregnaci určenou pro softshell.</li>'
          '<li>Fleece perte naruby, méně se žmolkuje.</li></ul>'
          '<h2>UNUO a jiné dětské značky</h2>'
          '<p>Na trhu dětského outdooru jsou silné i zahraniční značky, například '
          + B(('reima', 'Reima'), ('kilpi', 'Kilpi'), ('hannah', 'Hannah'), ('alpine-pro', 'Alpine Pro')) +
          '. Reima má propracované zimní kombinézy, Kilpi a Hannah sportovnější střihy. UNUO vyniká hlavně softshelly s veselými vzory a velkou nabídkou čepic a nákrčníků. Výběr záleží na tom, k čemu oblečení potřebujete: do školky, na hory, nebo na celodenní výlety.</p>'
          '<h2>Kdy nakupovat</h2>'
          '<p>Softshellové kalhoty se nejvíc prodávají v září a říjnu, kdy děti nastupují do školky a začíná chladnější počasí. Zimní oteplovačky a bundy mizí nejrychleji před prvním sněhem. Slevy se objevují na konci zimy a při obměně vzorů. Pokud víte, jakou velikost dítě bude potřebovat příští rok, můžete výprodeje využít s předstihem.</p>',
    faq=[
        ('Je UNUO česká značka?',
         'Ano. Založila ji Petra Plemlová a firma sídlí v Táboře. Podle vlastních informací většinu oblečení šije ve své dílně tam, zbytek v ověřených zahraničních dílnách.'),
        ('Jaký je rozdíl mezi softshellem s fleecem a bez zateplení?',
         'Softshell bez zateplení je lehký a hodí se na jaro a teplejší podzim. Verze s fleecovou podšívkou hřeje víc a zvládne chladné podzimní i mírně zimní dny.'),
        ('Stačí softshellové kalhoty i v zimě?',
         'Kalhoty s fleecem nebo beránkem zvládnou mírný mráz při pohybu. Do sněhu a na sáňkování jsou lepší zateplené oteplovačky, které nepromoknou.'),
        ('Jak vybrat velikost oblečení UNUO?',
         'Podle aktuální výšky dítěte s malou rezervou. Kupovat o dvě čísla větší se nevyplácí, dlouhé nohavice se zachytávají a padají do bláta.'),
        ('Co znamenají rostoucí oteplovačky?',
         'Jde o zimní kalhoty navržené tak, aby je dítě mohlo nosit déle než jednu sezónu. Jaké konkrétní řešení model používá, popisuje výrobce u daného produktu.'),
        ('Vejdou se batolecí kalhoty přes plenu?',
         'Batolecí modely bývají střižené volněji v sedu, aby se pod ně plena vešla. Ověřte to v popisu a v tabulce velikostí u konkrétního modelu.'),
        ('Jak prát dětský softshell?',
         'Na nízkou teplotu, bez aviváže a se zapnutými zipy. Do sušičky jen tehdy, když to štítek dovoluje. Odpudivost vody obnoví impregnace pro softshell.'),
        ('Najdu u UNUO i oblečení pro dospělé?',
         'Ano, v menším rozsahu. Jde hlavně o dámské softshellové bundy a funkční kalhoty pro rodiče, které chodí s dětmi ven.'),
        ('Kdy bývá UNUO ve slevě?',
         'Obvykle na konci zimy a při obměně vzorů. Na podzim, kdy poptávka roste, se slevy objevují méně často a oblíbené velikosti rychle mizí.'),
        ('Kde nákup oblečení UNUO dokončím?',
         'V e-shopu, který si na sporteka.cz vyberete. Srovnávač sám nic neprodává, jen ukazuje nabídky obchodů a dostupné velikosti.'),
    ],
)

# ------------------------------------------------------------------ baagl
NEW['baagl'] = dict(
    title='BAAGL: školní batohy, aktovky, gymsacky a láhve',
    desc='BAAGL v katalogu: školní batohy a aktovky, předškolní batůžky, gymsacky, láhve, boxy na svačinu a ledvinky. Jak vybrat batoh pro prvňáka a srovnat obchody.',
    intro='<p>BAAGL je česká značka školních batohů a aktovek, kterou rodiče znají hlavně z období před prvním zářím. V katalogu tvoří naprostou většinu nabídky školní batohy všech velikostí: od předškolních batůžků se zvířátky přes ergonomické aktovky pro prvňáky až po batohy pro starší školáky a studenty. K nim patří vaky na tělocvik, sáčky na přezůvky, tritanové láhve, boxy na svačinu, pláštěnky, ledvinky a batohy na notebook. '
          'Řady se jmenují například Airy, Skate, Core, Dash nebo Cubic a vedle nich jsou licenční kolekce s motivy Harry Potter, Minecraft, Batman nebo Kuromi. '
          'Na sporteka.cz vidíte nabídky e-shopů s výrobky BAAGL pohromadě, takže snadno porovnáte, kde je skladem konkrétní vzor. Kupujete pak v obchodě, který si vyberete. '
          'Průvodce níže vysvětluje, jak vybrat batoh podle věku a výšky dítěte, jak ho správně seřídit a co sledovat u doplňků.</p>',
    guide='<h2>Kdo stojí za značkou BAAGL</h2>'
          '<p>Značku založili v roce 2016 dva otcové, Petr a Martin, kteří sháněli aktovky pro své budoucí prvňáčky. Chtěli spojit funkční a zdravotně nezávadnou tašku s designem, který se dětem líbí. BAAGL dnes provozuje česká společnost Presco Group, a. s., která vlastní i ochranné známky značky. Při vývoji ergonomických modelů spolupracuje s fyzioterapeutkou a v týmu má vlastní návrháře.</p>'
          '<p>Výrobce uvádí, že řada produktů obsahuje recyklovaný materiál z PET lahví a že část sortimentu nese certifikaci GRS. Platí ale jen pro výrobky, které mají označení GRS přímo u sebe. Funkčnost a zdravotní nezávadnost výrobků, které přicházejí do styku s jídlem, podle výrobce ověřují nezávislé laboratoře.</p>'
          '<h2>Co BAAGL v katalogu nabízí</h2>'
          '<p>Jádrem nabídky jsou <a href="/skolni-batohy/">školní batohy</a>, do kterých obchody řadí i většinu doplňků se stejným motivem. Samostatné srovnání batohů najdete na stránce <a href="/baagl-batoh/">BAAGL batoh</a>. Menší část nabídky tvoří <a href="/turisticke-batohy/">turistické batohy</a> pro výlety, <a href="/lahve-a-termosky/">láhve</a>, <a href="/sportovni-tasky/">sportovní tašky</a>, <a href="/tasky-pres-rameno/">tašky přes rameno</a> a dětské <a href="/plastenky/">pláštěnky</a>. Pro starší studenty jsou určeny <a href="/batohy-na-notebook/">batohy na notebook</a> a <a href="/ledvinky/">ledvinky</a>.</p>'
          + T(['Typ výrobku', 'Pro koho', 'Na co se dívat'], [
              ['Předškolní batůžek (např. Buddy)', 'děti ve školce', 'nízká hmotnost, malý objem, hrudní popruh'],
              ['Aktovka pro prvňáka', '1. a 2. třída', 'pevná záda, tvarovaný zádový panel, reflexe'],
              ['Měkký školní batoh', 'od 2. nebo 3. třídy', 'objem, nastavitelné popruhy, přihrádky'],
              ['Studentský batoh', 'druhý stupeň a střední škola', 'kapsa na notebook, odolný materiál'],
              ['Gymsack a sáček na obuv', 'všechny věkové skupiny', 'pevná šňůra, praní'],
              ['Láhev a box na svačinu', 'školka i škola', 'materiál, těsnost, mytí']]) +
          '<h2>Aktovka, nebo školní batoh?</h2>'
          '<p>Slova se často zaměňují, ale v obchodech mají odlišný význam. Aktovka je pevná taška s tuhými zády, která drží tvar i bez náplně a chrání sešity. Hodí se pro prvňáky a mladší školáky, protože pevná záda rozloží hmotnost po zádech a dítě nenosí knihy v hromádce na dně. Školní batoh je měkčí, lehčí a má větší objem, proto ho volí starší děti, které nosí více věcí a samy si je skládají. Obchody ale oba typy často řadí pod společný název školní batoh, proto v popisu hledejte, zda má model pevnou konstrukci a tvarovaná záda.</p>'
          '<h2>Jak vybrat batoh pro prvňáka</h2>'
          '<p>Při výběru první aktovky se rodiče nejvíc soustředí na motiv, ale rozhodují jiné vlastnosti. Prázdná aktovka by měla být co nejlehčí, protože do ní přibudou učebnice, penál a svačina. Zádový panel má kopírovat tvar zad a mít polstrování, které odvádí pot. Ramenní popruhy musejí být široké a nastavitelné, aby se aktovka dala seřídit podle toho, jak dítě roste.</p>'
          '<ol><li>Vyzkoušejte aktovku s dítětem nebo porovnejte její rozměry s jeho výškou.</li>'
          '<li>Horní okraj by neměl přesahovat ramena, spodní by měl končit nad pasem.</li>'
          '<li>Zkontrolujte hrudní popruh, který drží ramenní popruhy na místě.</li>'
          '<li>Reflexní prvky by měly být vpředu i na bocích, protože děti chodí do školy i za šera.</li>'
          '<li>Ověřte, zda se aktovka vejde do skříňky nebo na háček ve třídě.</li></ol>'
          '<p>Plná aktovka by neměla vážit víc, než dítě pohodlně unese. Obvykle se uvádí orientační hranice kolem desetiny hmotnosti dítěte. Pomáhá i pravidlo, že se do tašky nosí jen věci na daný den.</p>'
          '<h2>Správné seřízení batohu</h2>'
          '<p>I nejlepší batoh bude dítě bolet, když je špatně nastavený. Oba ramenní popruhy se nosí vždy současně, nikdy jen přes jedno rameno. Batoh má těsně přiléhat k zádům, bez mezery, kterou by se taška houpala. Hrudní popruh zapněte ve výšce hrudníku, ne pod krkem. Těžké učebnice dávejte nejblíž k zádům, lehčí věci dopředu. Seřízení zkontrolujte vždy na začátku pololetí, protože děti rostou nerovnoměrně.</p>'
          '<h2>Předškolní batůžky</h2>'
          '<p>Pro děti ve školce jsou určené malé batůžky, například řada Buddy se zvířátky nebo předškolní batohy s pohádkovými motivy. Mají malý objem, do kterého se vejde svačina, láhev a náhradní oblečení, a nízkou hmotnost, aby je dítě neslo samo. Hrudní popruh zabrání tomu, aby popruhy sklouzávaly z úzkých ramen. Ke školkovému batůžku se hodí předškolní sáček na přezůvky a pláštěnka, kterou dítě nosí s sebou na vycházky. Batůžek vybírejte podle výšky dítěte, ne podle toho, kolik se do něj vejde.</p>'
          '<h2>Bezpečnost na cestě do školy</h2>'
          '<p>Děti chodí do školy v zimních měsících za tmy a za šera. Reflexní prvky na aktovce proto nejsou ozdobou, ale důležitou součástí výbavy. Výrobce uvádí, že je používá u svých batohů; při výběru se podívejte, zda jsou na čelní straně i na bocích, aby dítě bylo vidět i při přecházení silnice. Tmavé aktovky doplňte reflexní páskou nebo přívěskem. Zapínání hrudního popruhu by mělo být jednoduché, aby ho dítě zvládlo samo i v rukavicích; některé řady mají magnetické přezky Fidlock.</p>'
          '<h2>Batohy pro starší děti a studenty</h2>'
          '<p>Na druhém stupni se mění požadavky. Děti chtějí batoh, který nevypadá dětsky, a potřebují místo pro tablet nebo notebook. Pro tuto věkovou skupinu jsou vhodné modely s jednodušším designem, oddělenou polstrovanou kapsou a odolným materiálem. U studentských batohů sledujte objem v litrech a to, zda kapsa na notebook sedí na velikost vašeho počítače. Pro dospívající, kteří nosí batoh i mimo školu, může být alternativou běžný <a href="/mestske-batohy/">městský batoh</a>.</p>'
          '<h2>Licenční kolekce</h2>'
          '<p>Značná část nabídky nese motivy z filmů, her a seriálů: Harry Potter, Minecraft, Fortnite, Batman, Hello Kitty nebo Kuromi. Pro dítě je motiv často rozhodující, pro rodiče je důležité vědět, že licenční model má stejnou konstrukci jako řada, ze které vychází. Před nákupem si proto ověřte, k jaké řadě motiv patří, a porovnejte parametry se základní verzí. Licenční motivy bývají oblíbené a v sezóně rychle mizí ze skladu.</p>'
          '<h2>Doplňky se stejným motivem</h2>'
          '<p>K aktovce se obvykle kupuje vak na tělocvik, sáček na přezůvky, penál, láhev a box na svačinu. BAAGL je nabízí ve stejných vzorech, takže sada ladí. Tritanové láhve jsou lehké a nerozbijí se, verze s brčkem ocení menší děti. Boxy na svačinu mají často přihrádky, které oddělí ovoce od pečiva. Gymsack čili vak se šňůrkami se hodí na tělocvik i na kroužky. Některé obchody prodávají výhodné školní sety, kde je aktovka, penál a vak dohromady.</p>'
          '<h2>Ledvinky a batohy na notebook</h2>'
          '<p>Kromě školních tašek nabízí BAAGL i věci pro dospívající a dospělé. Ledvinky se nosí kolem pasu nebo přes rameno a hodí se na telefon, klíče a peněženku při výletech a na koncerty. Batohy na notebook mají polstrovanou kapsu a jednodušší vzhled, takže je mohou nosit studenti i rodiče do práce. U ledvinky zkontrolujte délku popruhu a kvalitu přezky, u batohu na notebook velikost kapsy v palcích.</p>'
          '<h2>Péče a praní</h2>'
          '<ul><li>Batoh vyprázdněte a vysypte drobky aspoň jednou týdně.</li>'
          '<li>Skvrny čistěte vlhkým hadříkem a jemným mýdlem, pevné aktovky nedávejte do pračky.</li>'
          '<li>Gymsacky a sáčky na přezůvky obvykle snesou praní v pračce, ověřte štítek.</li>'
          '<li>Láhve a boxy na svačinu myjte ručně, pokud výrobce neuvádí, že snesou myčku.</li>'
          '<li>Zipy občas očistěte od písku, prodloužíte tím jejich životnost.</li></ul>'
          '<h2>BAAGL a další značky</h2>'
          '<p>Na českém trhu školních batohů má BAAGL silné postavení, ale vedle něj se prodávají i outdoorové značky s dětskými batohy, například '
          + B(('deuter', 'Deuter'), ('husky', 'Husky'), ('loap', 'Loap')) +
          '. Ty se hodí spíše na výlety než do školy. Pokud hledáte batůžek pro malé dítě do školky nebo na procházky, porovnejte nabídku v kategorii <a href="/detsky-batoh/">dětský batoh</a>.</p>'
          '<h2>Kdy nakupovat</h2>'
          '<p>Hlavní sezóna školních batohů začíná už na jaře, kdy rodiče budoucích prvňáků začínají vybírat, a vrcholí v srpnu. Nejoblíbenější motivy bývají koncem léta vyprodané. Pokud chcete konkrétní vzor, nakupte s předstihem. Výprodeje starších kolekcí přicházejí na podzim a v zimě, což je vhodná doba pro náhradní batoh nebo doplňky.</p>',
    faq=[
        ('Je BAAGL česká značka?',
         'Ano. Značku založili v roce 2016 dva otcové budoucích prvňáků a dnes ji provozuje česká společnost Presco Group, a. s.'),
        ('Jaký je rozdíl mezi aktovkou a školním batohem?',
         'Aktovka má pevná záda a drží tvar, proto se hodí pro prvňáky. Školní batoh je měkčí, lehčí a prostornější a volí ho spíše starší děti.'),
        ('Jakou aktovku BAAGL vybrat pro prvňáka?',
         'Lehkou, s tvarovaným zádovým panelem, širokými nastavitelnými popruhy, hrudním popruhem a reflexními prvky. Horní okraj nemá přesahovat ramena dítěte.'),
        ('Kolik by měla vážit plná školní taška?',
         'Orientačně se uvádí zhruba desetina hmotnosti dítěte. Pomáhá nosit jen věci na daný den a těžké učebnice ukládat nejblíž k zádům.'),
        ('Jak správně seřídit školní batoh?',
         'Oba popruhy přes ramena, batoh těsně u zad a hrudní popruh ve výšce hrudníku. Seřízení zkontrolujte na začátku každého pololetí.'),
        ('Mají licenční motivy stejnou kvalitu jako běžné řady?',
         'Licenční modely vycházejí z konkrétních řad značky. Před nákupem si ověřte, ke které řadě motiv patří, a porovnejte parametry se základní verzí.'),
        ('Jsou výrobky BAAGL z recyklovaných materiálů?',
         'Výrobce uvádí, že řada produktů obsahuje recyklovaný materiál z PET lahví. Certifikace GRS ale platí jen pro výrobky, které ji mají přímo uvedenou.'),
        ('Lze školní batoh prát v pračce?',
         'Pevné aktovky do pračky nepatří, čistěte je vlhkým hadříkem. Gymsacky a sáčky na přezůvky obvykle praní snesou, rozhoduje štítek.'),
        ('Kdy koupit školní batoh, aby byl výběr největší?',
         'Na jaře a začátkem léta. V srpnu bývají oblíbené motivy vyprodané. Starší kolekce se zlevňují na podzim a v zimě.'),
        ('Kde batoh BAAGL nakonec koupím?',
         'V jednom z českých e-shopů, které sporteka.cz porovnává. Srovnávač ukáže dostupnost a cenu u obchodů a objednávka proběhne přímo u vybraného prodejce.'),
    ],
)

# ------------------------------------------------------------------ stanley
NEW['stanley'] = dict(
    title='Stanley: termosky, termohrnky Quencher a láhve',
    desc='Stanley v katalogu: termosky Classic, termohrnky Quencher a Transit, láhve IceFlow, jídelní termosky i kempingové nádobí. Jak vybrat objem a porovnat ceny.',
    intro='<p>Stanley je americká značka termosek, kterou mnoho lidí pozná podle zeleného kladívkového laku na klasické láhvi. V katalogu převažují termohrnky a cestovní hrnky, mezi nimi velmi oblíbený Quencher s uchem a brčkem, dále termosky řady Classic Legendary, láhve na vodu IceFlow, jídelní termosky se lžící, placatky, korbely a kempingové nádobí. '
          'Většina výrobků je z nerezové oceli s dvojitou stěnou a vakuovou izolací, která drží nápoje teplé nebo studené mnoho hodin. '
          'Sporteka shromažďuje nabídky českých e-shopů se zbožím Stanley a umožňuje porovnat je podle barvy a objemu. Objednávku pak dokončíte v obchodě, na který z přehledu přejdete. '
          'Níže vysvětlujeme rozdíly mezi řadami, výběr objemu podle použití a péči, díky které termoska vydrží roky.</p>',
    guide='<h2>Historie značky Stanley</h2>'
          '<p>Za značkou stojí vynálezce William Stanley Jr., který v roce 1913 přišel s celoocelovou vakuovou láhví. Při práci s transformátory zjistil, že díky svařovací technice může skleněnou vložku tehdejších termosek nahradit ocelí. Láhev se tak přestala rozbíjet a stala se oblíbeným vybavením dělníků, vojáků i rybářů. Typická zelená barva s kladívkovým povrchem se stala poznávacím znamením.</p>'
          '<p>Dnes značku vlastní společnost Pacific Market International se sídlem v Seattlu. Pozor na záměnu: výrobce nářadí Stanley Black &amp; Decker je samostatná firma, která používá stejné jméno. Proto se v katalogu pod značkou Stanley může výjimečně objevit i nůž nebo nářadí, které s termoskami nesouvisí. Největší rozmach v posledních letech přinesl hrnek Quencher, uvedený v roce 2016, který se díky sociálním sítím stal módním doplňkem.</p>'
          '<h2>Co Stanley v katalogu nabízí</h2>'
          '<p>Nejvíc zboží obchody řadí do kategorie <a href="/vareni-v-prirode/">vaření v přírodě</a>, kam spadají termohrnky Quencher, Transit, Café-To-Go nebo Stay Hot. Druhou velkou skupinou jsou <a href="/lahve-a-termosky/">láhve a termosky</a>, tedy klasické termosky Legendary Classic, láhve IceFlow a Wellspring a jídelní termosky. Samostatně můžete porovnat <a href="/termohrnky/">termohrnky</a>. Menší zastoupení mají <a href="/outdoor-doplnky/">outdoorové doplňky</a>, například placatky, korbely na pivo a obědové boxy, <a href="/kempingove-nadobi/">kempingové nádobí</a> a <a href="/chladici-boxy/">chladicí boxy</a>.</p>'
          + T(['Řada', 'Typ', 'Typické použití'], [
              ['Classic Legendary', 'klasická termoska s víčkem-hrnkem', 'túry, ryby, práce venku'],
              ['Quencher', 'velký termohrnek s uchem a brčkem', 'kancelář, auto, celodenní pití'],
              ['IceFlow, Wellspring', 'láhev na vodu s brčkem nebo poutkem', 'sport, posilovna, škola'],
              ['Transit, Café-To-Go, AeroLight', 'cestovní hrnek na kávu', 'cesta do práce, auto, vlak'],
              ['Adventure', 'hrnky, korbely, jídelní termosky', 'kemp, chata, výlety'],
              ['Jídelní termosky', 'široké hrdlo, lžíce nebo spork', 'teplý oběd v práci a na túře']]) +
          '<h2>Termoska, termohrnek, nebo láhev?</h2>'
          '<p>Výběr začíná otázkou, co budete pít a kde. Klasická termoska Legendary Classic má těsný uzávěr a víčko, které slouží jako hrnek. Je určená na čaj nebo kávu na celý den venku a do batohu ji můžete položit naležato. Termohrnek je pohodlnější na pití za chůze nebo v autě, ale u většiny modelů se nedoporučuje přenášet ho v batohu s rizikem vylití. Láhev na vodu typu IceFlow se hodí hlavně na studené nápoje a sport, protože má brčko nebo širší otvor pro rychlé pití.</p>'
          '<p>Quencher patří mezi termohrnky, ale je výrazně větší než běžný hrnek na kávu. Ucho a zúžené dno, které se vejde do držáku v autě, z něj dělají praktický kus na celodenní pití vody s ledem. Na horké nápoje a cestování v batohu se ale nehodí: výrobce víčko s brčkem popisuje jako odolné proti rozlití, nikoli jako zcela těsné.</p>'
          '<h2>Jak vybrat objem</h2>'
          '<ul><li>Malé hrnky a placatky do půl litru stačí na jeden šálek kávy nebo krátkou cestu.</li>'
          '<li>Láhve a termosky kolem tří čtvrtě litru až litru jsou univerzální volbou na celodenní výlet pro jednoho.</li>'
          '<li>Termosky přes litr, například velká Legendary Classic, se hodí pro dva a více lidí nebo na rybaření a práci venku.</li>'
          '<li>Jídelní termosky okolo půl litru pojmou porci polévky nebo teplého oběda.</li></ul>'
          '<p>Platí, že větší objem drží teplotu déle, protože velké množství tekutiny chladne pomaleji. Výrobce u každého modelu uvádí, kolik hodin udrží nápoj teplý a kolik studený; při porovnání sledujte i to, zda údaj platí pro plnou nádobu.</p>'
          '<h2>Na čem závisí, jak dlouho termoska hřeje</h2>'
          '<p>Vakuová izolace funguje nejlépe, když termosku před naplněním předehřejete horkou vodou, kterou pak vylijete. Studené nápoje zase udržíte déle, když nádobu nejdřív vychladíte ledovou vodou. Plná termoska hřeje déle než poloprázdná, protože v ní je méně vzduchu. Každé otevření znamená ztrátu tepla, proto si na túře nalévejte větší dávky najednou. Pokud termoska náhle přestane hřát a zvenku je teplá, je pravděpodobně poškozené vakuum.</p>'
          '<h2>Hrnky na kávu: Transit, Café-To-Go a AeroLight</h2>'
          '<p>Kdo pije kávu cestou do práce, sáhne spíše po menším cestovním hrnku než po velké termosce. Řady Transit, Café-To-Go nebo AeroLight mají objem od jednoho šálku po větší porci, víčko s otvorem na pití a tvar, který se vejde do držáku v autě. Některé modely mají víčko, které se dá úplně uzavřít, jiné jen zakrýt. Pokud hrnek nosíte v tašce, vybírejte uzavíratelný model. Před nákupem porovnejte i hmotnost prázdného hrnku, protože se mezi řadami liší.</p>'
          '<h2>Láhve IceFlow a Wellspring na sport</h2>'
          '<p>Řada IceFlow je určená hlavně na studenou vodu. Láhve mají brčko, které se odklápí, nebo široký otvor pro rychlé pití, a pevné poutko pro přenášení. Hodí se do posilovny, na kolo, do školy i do kanceláře. Láhve Wellspring mají podobné určení. Na rozdíl od klasické termosky se z nich pije přímo, bez nalévání do víčka. Pokud chcete láhev vozit na kole, ověřte, zda její průměr pasuje do <a href="/cyklo-lahve-a-drzaky/">košíku na láhev</a>; velké objemy se do běžného košíku obvykle nevejdou. Pokud do ní dáváte led, počítejte s tím, že zabere část objemu, a láhev plňte jen tak, aby šla dobře zavřít.</p>'
          '<h2>Jak číst objem v názvech</h2>'
          '<p>E-shopy uvádějí objem různě: v mililitrech, v litrech nebo v amerických uncích, které se objevují u originálních názvů. Hodnota 40 oz odpovídá zhruba 1,2 litru, 30 oz přibližně 0,9 litru a 20 oz asi 0,6 litru. Některé obchody objem zkracují v názvu na číslo bez jednotky, například 470 nebo 700, což znamená mililitry. Před porovnáním si proto ověřte, že srovnáváte stejnou velikost.</p>'
          '<h2>Jídelní termosky a kempování</h2>'
          '<p>Jídelní termosky mají široké hrdlo, aby se z nich dalo jíst lžící, a některé jsou balené se sporkem, kombinací lžíce a vidličky. Hodí se na teplý oběd v práci, ve škole i na horách. Do kempu se hodí také řada Adventure s hrnky, korbely a nádobím. Pro vaření na výletě budete kromě nádoby potřebovat i <a href="/varice-a-kartuse/">vařič a kartuše</a>; přehled vybavení najdete v kategorii <a href="/kemping/">kemping</a>.</p>'
          '<h2>Péče a mytí</h2>'
          '<ul><li>Po použití termosku vypláchněte a nechte otevřenou vyschnout, zabráníte zápachu.</li>'
          '<li>Usazeniny od kávy a čaje odstraní roztok jedlé sody nebo speciální čisticí tablety.</li>'
          '<li>Do myčky dávejte jen díly, u kterých to výrobce výslovně dovoluje.</li>'
          '<li>Těsnění občas vyjměte a umyjte zvlášť, pod ním se drží nečistoty.</li>'
          '<li>Termosku nenechávejte v mrazu s vodou, led by mohl poškodit uzávěr.</li></ul>'
          '<h2>Barvy a varianty</h2>'
          '<p>Kromě klasické zelené se termosky a hrnky Stanley vyrábějí v mnoha barvách, a zejména u Quencheru se pravidelně objevují nové odstíny a limitované edice. Stejný model se proto v e-shopech nabízí v desítkách variant. Pokud jde hlavně o funkci, porovnejte cenu všech barev, protože méně žádané odstíny bývají levnější.</p>'
          '<h2>Stanley jako dárek</h2>'
          '<p>Termosky a hrnky patří k oblíbeným dárkům, protože je využije téměř každý. Pro chataře a milovníky <a href="/rybareni/">rybaření</a> je typickou volbou klasická zelená Legendary Classic, pro řidiče a lidi, kteří pracují v kanceláři, Quencher nebo hrnek Transit, pro sportovce láhev IceFlow. Při výběru barvy se vyplatí zjistit, jakou má obdarovaný rád, protože u řady Quencher se nabízí mnoho odstínů.</p>'
          '<h2>Pozor na napodobeniny</h2>'
          '<p>Oblíbenost Quencheru vedla k tomu, že se na internetu objevují kopie s podobným tvarem. U neověřených prodejců s nápadně nízkou cenou buďte opatrní. Originál nese logo Stanley a v popisu výrobce bývá uvedeno, z jaké oceli je nádoba vyrobená. Na sportece porovnáváme nabídky zavedených českých obchodů, ale u každé nabídky si zkontrolujte, kdo je prodejce a jaké jsou podmínky reklamace.</p>'
          '<h2>Kdy nakupovat</h2>'
          '<p>Termosky se nejvíc prodávají na podzim a v zimě a jako dárek před Vánoci, láhve na vodu a hrnky s ledem v létě. Slevy přicházejí při výprodejích po svátcích a při uvolňování starších barev. Pokud sháníte konkrétní odstín, sledujte jeho dostupnost delší dobu, protože některé limitované barvy se rychle vyprodají.</p>',
    faq=[
        ('Odkud pochází značka Stanley?',
         'Z USA. William Stanley Jr. v roce 1913 vynalezl celoocelovou vakuovou láhev. Dnes značku vlastní společnost Pacific Market International ze Seattlu.'),
        ('Souvisí termosky Stanley s nářadím Stanley?',
         'Ne. Výrobce nářadí Stanley Black & Decker je samostatná firma. Proto se pod stejným jménem v katalogu výjimečně objeví i nůž nebo nářadí.'),
        ('Co je Stanley Quencher?',
         'Velký termohrnek s uchem, víčkem a brčkem, uvedený v roce 2016. Hodí se na celodenní pití vody s ledem v kanceláři nebo v autě.'),
        ('Je Quencher vhodný do batohu?',
         'Spíše ne. Výrobce víčko popisuje jako odolné proti rozlití, ne jako zcela těsné. Do batohu je lepší klasická termoska nebo láhev s uzavíratelným víčkem.'),
        ('Jaký objem termosky zvolit na celodenní výlet?',
         'Pro jednoho obvykle stačí tři čtvrtě litru až litr. Na rybaření, práci venku nebo pro dva a více lidí se hodí větší termoska přes litr.'),
        ('Jak dlouho termoska Stanley udrží teplotu?',
         'Záleží na modelu a objemu, údaj uvádí výrobce u každé řady. Teplotu udržíte déle, když termosku předehřejete a naplníte až po okraj.'),
        ('Lze termosky Stanley mýt v myčce?',
         'Jen díly, u kterých to výrobce výslovně uvádí. Ostatní myjte ručně, usazeniny odstraní roztok jedlé sody nebo čisticí tablety.'),
        ('Proč moje termoska přestala hřát?',
         'Pokud je při plnění horkým nápojem zvenku teplá, je pravděpodobně poškozené vakuum, často po pádu. Takovou termosku už nejde opravit.'),
        ('K čemu slouží jídelní termoska?',
         'Na teplé jídlo, například polévku nebo těstoviny. Má široké hrdlo a některé modely se prodávají se sporkem, tedy lžící s vidličkou v jednom.'),
        ('Prodává sporteka.cz výrobky Stanley?',
         'Ne. Sporteka ukazuje nabídky českých obchodů vedle sebe a nákup proběhne u prodejce, kterého si vyberete. Zkontrolujte jeho podmínky reklamace.'),
    ],
)

# ------------------------------------------------------------------ ea7-emporio-armani
NEW['ea7-emporio-armani'] = dict(
    title='EA7 Emporio Armani: tepláky, mikiny, bundy a trička',
    desc='EA7 Emporio Armani v katalogu: teplákové soupravy, mikiny, trička, bundy, lyžařské oblečení, plavky i tenisky. Jak vybrat střih a srovnat nabídky obchodů.',
    intro='<p>EA7 je sportovní linie italského módního domu Armani. V katalogu sporteky se u ní nejčastěji objevují tepláky a teplákové soupravy, mikiny a trička, ale nabídka je široká: přechodové a zimní bundy včetně péřových, lyžařské bundy a kalhoty, legíny, sportovní podprsenky, koupací šortky, pantofle, čepice a tenisky. '
          'Pánská a dámská kolekce jsou zastoupeny zhruba vyrovnaně, menší část tvoří dětské modely. Typické je výrazné logo EA7 a střídmé barvy, především černá, bílá a tmavě modrá. '
          'Sporteka.cz sbírá nabídky e-shopů, které EA7 prodávají, a dává je vedle sebe, abyste viděli rozdíly v ceně a dostupnosti velikostí. Zboží si objednáte v obchodě, který vám nejvíc vyhovuje. '
          'Průvodce níže vysvětluje, jak se EA7 liší od ostatních linií Armani, jak vybrat velikost a co sledovat u jednotlivých skupin oblečení.</p>',
    guide='<h2>Co je EA7</h2>'
          '<p>Linie EA7 vznikla v roce 2004 z nápadu Giorgia Armaniho jako sportovní větev značky Emporio Armani. Měla mít výraznou sportovní identitu, která ji odliší od módních kolekcí, a spojit technické materiály s typickým čistým designem Armani. Logo spojuje iniciály EA s číslicí 7, kterou výrobce popisuje jako symbol energie a soutěživosti.</p>'
          '<p>EA7 je od roku 2012 oficiálním dodavatelem oblečení pro italskou reprezentaci na olympijských a paralympijských hrách. Je také titulárním sponzorem basketbalového klubu Olimpia Milano, který patří do světa Armani. Kolekce pokrývají tenis a padel, lyžování, golf, běh, fitness a jógu. Vedle EA7 existují i další linie skupiny, například módnější '
          + B(('armani-exchange', 'Armani Exchange')) +
          ', proto u konkrétního kusu sledujte, ke které linii patří.</p>'
          '<h2>Co EA7 v katalogu nabízí</h2>'
          '<p>Největší skupinou jsou <a href="/teplaky/">tepláky</a>, mezi nimiž převažují celé soupravy; srovnání najdete také v kategorii <a href="/teplakove-soupravy/">teplákové soupravy</a>. Následují <a href="/mikiny/">mikiny</a> s kapucí i bez a <a href="/sportovni-tricka/">trička</a>. Silné zastoupení mají <a href="/sportovni-bundy-jaro-podzim/">přechodové bundy</a> a <a href="/zimni-bundy/">zimní bundy</a>, k nim <a href="/lyzarske-bundy/">lyžařské bundy</a> a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>. Do letní sezóny patří <a href="/plavky/">plavky</a> a <a href="/pantofle-a-zabky/">pantofle</a>, do posilovny <a href="/leginy/">legíny</a> a <a href="/sportovni-podprsenky/">sportovní podprsenky</a>. Doplňují je <a href="/cepice-a-celenky/">čepice</a>, kšiltovky, ponožky a <a href="/tenisky/">tenisky</a>.</p>'
          + T(['Skupina', 'Typický materiál', 'K čemu'], [
              ['Teplákové soupravy', 'bavlna, směsi s elastanem, polyester', 'volný čas, cestování, trénink'],
              ['Mikiny', 'bavlněný úplet, technické směsi', 'vrstva pod bundu, běžné nošení'],
              ['Trička a funkční trička', 'bavlna, modal, rychleschnoucí syntetika', 'běžné nošení i trénink'],
              ['Bundy a péřové bundy', 'polyamid, péří nebo syntetická výplň', 'město, přechodné období, zima'],
              ['Lyžařské oblečení', 'technické tkaniny se zateplením', 'sjezdovka, zimní dovolená'],
              ['Plavky a pantofle', 'polyester, pryž', 'moře, bazén, wellness']]) +
          '<h2>Teplákové soupravy</h2>'
          '<p>Souprava je pro EA7 nejtypičtějším produktem. Prodává se jako celek mikiny a kalhot ve stejné barvě, často s výrazným logem na hrudi nebo na stehně. Bavlněné soupravy jsou příjemné na nošení doma, na cestování nebo do města. Modely ze syntetiky nebo se směsí s elastanem jsou lehčí, méně se mačkají a hodí se na trénink. Před nákupem zkontrolujte, zda se souprava prodává jako celek, nebo zda jsou mikina a kalhoty samostatné položky, u kterých si můžete vybrat různé velikosti.</p>'
          '<p>Pokud nosíte horní a dolní díl v jiné velikosti, je samostatný nákup výhodnější. Porovnání dalších značek najdete na stránkách <a href="/panske-teplaky/">pánské tepláky</a> a <a href="/damske-teplaky/">dámské tepláky</a>.</p>'
          '<h2>Jak sedí velikosti EA7</h2>'
          '<p>Italské střihy bývají užší než americké. Mikiny a trička EA7 jsou často střižené k tělu, tepláky mají zúžené nohavice s manžetou. Pokud preferujete volnější styl, zvažte o číslo větší velikost nebo hledejte modely s označením oversize, které se objevují hlavně v dámské kolekci. U dětských modelů se velikost obvykle uvádí podle věku nebo výšky.</p>'
          '<ol><li>Změřte obvod hrudníku a pasu a porovnejte je s tabulkou u nabídky.</li>'
          '<li>U kalhot ověřte délku nohavice, protože zúžený střih s manžetou je citlivý na výšku postavy.</li>'
          '<li>U bund počítejte s mikinou pod nimi.</li>'
          '<li>Při nákupu na zkoušku si předem přečtěte podmínky vrácení u vybraného obchodu.</li></ol>'
          '<h2>Bundy a lyžařské oblečení</h2>'
          '<p>Přechodové bundy jsou převážně lehké, s kapucí a zipem, vhodné do města a na cestování. Zimní nabídka zahrnuje prošívané a péřové bundy. Lyžařské bundy a kalhoty jsou určené na sjezdovku; u konkrétního modelu si v popisu ověřte zateplení, sněhový pás a kapsu na skipas. Linie EA7 se lyžování věnuje dlouhodobě a k jejím vyslancům patří i italská sjezdařka Sofia Goggia. Pro rekreační lyžaře je lyžařská bunda EA7 kombinací funkce a módního vzhledu; kdo jezdí hodně mimo sjezdovky, porovná ji s technicky zaměřenými značkami.</p>'
          '<h2>Péřové a prošívané bundy</h2>'
          '<p>Do zimy nabízí EA7 prošívané a péřové bundy pro dospělé i děti a také péřové vesty. Péřová výplň je lehká a dobře hřeje, ale po namočení ztrácí objem; syntetická výplň je odolnější vůči vlhku. U péřových bund se v popisu uvádí poměr prachového a drobného peří, vyšší podíl prachového peří znamená lepší izolaci při nižší hmotnosti. Více o výběru najdete v kategorii <a href="/perove-bundy/">péřové bundy</a>.</p>'
          '<h2>Trička a funkční oblečení na trénink</h2>'
          '<p>Trička jsou z bavlny, ze směsi s modalem nebo z rychleschnoucí syntetiky. Bavlněná trička patří spíše do města, na trénink jsou vhodnější <a href="/funkcni-tricka/">funkční trička</a>, která odvádějí pot. V dámské kolekci najdete legíny a sportovní podprsenky pro fitness a jógu. Při výběru legín sledujte výšku pasu a to, zda materiál při předklonu neprosvítá.</p>'
          '<h2>Dámská kolekce</h2>'
          '<p>Dámská část sortimentu je stejně rozsáhlá jako pánská. Kromě souprav a mikin v ní najdete oversize trička, legíny, sportovní podprsenky, vesty a bundy s vypasovaným střihem. Dámské teplákové soupravy bývají z bavlny s příměsí elastanu, takže lépe drží tvar. Barevná paleta je pestřejší než u pánských modelů a objevují se v ní i pastelové a růžové tóny. Velikosti se řídí vlastní tabulkou, která se od pánské liší.</p>'
          '<h2>Dětská kolekce</h2>'
          '<p>Menší část nabídky tvoří oblečení pro chlapce a dívky: tepláky, mikiny, trička a bundy podobné modelům pro dospělé. Velikost se uvádí podle věku nebo výšky. Děti rostou rychle, proto zvažte, zda se vyplatí dražší značkový kus, nebo raději vybrat jednodušší model. U teplákových souprav pro děti oceníte manžety, které nohavice drží na místě.</p>'
          '<h2>Tenisky a obuv</h2>'
          '<p>Obuv EA7 zahrnuje hlavně tenisky do města s logem na boku a pantofle k vodě. Tenisky jsou určené na běžné nošení, nikoli na běh nebo halové sporty, pro které se hodí specializovaná <a href="/bezecka-obuv/">běžecká obuv</a>. Velikosti se uvádějí v evropských číslech, ale mohou se mezi modely lišit, proto porovnávejte délku stélky v centimetrech.</p>'
          '<h2>Letní kolekce</h2>'
          '<p>Na léto EA7 nabízí koupací šortky, pantofle a žabky s logem a lehká trička. Koupací šortky mají často vnitřní síťku a rychleschnoucí materiál. Pantofle se hodí k bazénu i do wellness, ale na delší chůzi nejsou určené. Výběr dalších plavek najdete v kategorii <a href="/panske-plavky/">pánské plavky</a>.</p>'
          '<h2>EA7 a jiné sportovní značky</h2>'
          '<p>EA7 se pohybuje mezi sportovními a módními značkami. Na trénink a výkon se často srovnává se značkami '
          + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('under-armour', 'Under Armour'), ('puma', 'Puma')) +
          ', ve volnočasovém oblečení s logem spíše s '
          + B(('lacoste', 'Lacoste'), ('tommy-hilfiger', 'Tommy Hilfiger'), ('calvin-klein', 'Calvin Klein'), ('guess', 'Guess')) +
          '. Rozhodující bývá střih a materiál, výraznější logo je u EA7 součástí stylu.</p>'
          '<h2>Jak rozpoznat linii a vyhnout se padělkům</h2>'
          '<p>Pod jménem Armani se prodává několik linií a v e-shopech se někdy zaměňují. Oblečení EA7 nese logo EA7 a v názvu obvykle i spojení EA7 Emporio Armani. Kvůli oblibě značky se na trhu objevují napodobeniny, proto nakupujte u zavedených prodejců. Nápadně nízká cena, chybějící visačky nebo nekvalitní šití loga jsou varovné signály. Sporteka zobrazuje nabídky českých obchodů, u každé si ale zkontrolujte, kdo je prodejcem.</p>'
          '<h2>Péče o oblečení</h2>'
          '<ul><li>Bavlněné soupravy perte naruby a na nízkou teplotu, potisk a logo vydrží déle.</li>'
          '<li>Funkční trička a legíny perte bez aviváže, která zhoršuje odvod potu.</li>'
          '<li>Péřové bundy perte se speciálním pracím prostředkem a suště v sušičce s míčky.</li>'
          '<li>Lyžařské oblečení po sezóně vyperte a obnovte impregnaci.</li></ul>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Teplákové soupravy a mikiny se prodávají celoročně, ale nejvíc zlevňují při výprodejích po Vánocích a na konci léta. Bundy a lyžařské oblečení klesají na konci zimy, plavky a pantofle po létě. Starší barevné varianty se objevují ve slevách při příchodu nové kolekce. U oblíbených modelů v černé barvě bývají slevy menší, protože se prodávají nejlépe.</p>',
    faq=[
        ('Co je EA7 Emporio Armani?',
         'Sportovní linie Emporio Armani, která vznikla v roce 2004 z nápadu Giorgia Armaniho. Spojuje sportovní oblečení s designem typickým pro Armani.'),
        ('Co znamená sedmička v logu EA7?',
         'Podle výrobce je číslice 7 symbolem energie, výjimečnosti a soutěživého ducha. Písmena EA odkazují na Emporio Armani.'),
        ('Jaký je rozdíl mezi EA7 a Armani Exchange?',
         'EA7 je sportovní linie zaměřená na trénink, lyžování a sportovní volný čas. Armani Exchange je módnější městská linie skupiny Armani.'),
        ('Jak padnou velikosti EA7?',
         'Střihy bývají užší, mikiny a trička k tělu a tepláky se zúženými nohavicemi. Kdo chce volnější styl, často volí o číslo větší velikost.'),
        ('Prodávají se teplákové soupravy EA7 jako celek?',
         'Často ano, ale některé obchody nabízejí mikinu a kalhoty samostatně. Pokud nosíte díly v různých velikostech, je samostatný nákup praktičtější.'),
        ('Hodí se EA7 i na sport?',
         'Ano. Kolekce zahrnuje funkční trička, legíny, sportovní podprsenky a lyžařské oblečení. Bavlněné soupravy se hodí spíše na volný čas.'),
        ('Má EA7 lyžařské oblečení?',
         'Ano, nabídka zahrnuje lyžařské bundy a kalhoty se zateplením. Hodí se rekreačním lyžařům, kteří chtějí funkční oblečení s výrazným designem.'),
        ('Najdu EA7 i pro děti?',
         'Ano, ale v menším výběru než pro dospělé. Jde hlavně o tepláky, mikiny, trička a bundy, velikost se obvykle uvádí podle věku nebo výšky.'),
        ('Kdy bývá EA7 ve slevě?',
         'Nejčastěji po Vánocích, na konci léta a při obměně kolekce. Bundy zlevňují na konci zimy, plavky po létě.'),
        ('Prodává sporteka.cz oblečení EA7?',
         'Ne. Sporteka zobrazuje nabídky českých obchodů, aby šly porovnat. Objednávku i dopravu řešíte přímo v e-shopu, který si vyberete.'),
    ],
)
