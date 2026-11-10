"""sporteka.cz — wave 13d (4. 11. 2026): long texts (>= 1650 words) for leginy, sportovni-bryle, cinky-a-kotouce, fitness-pomucky.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ leginy
NEW['leginy'] = dict(long=True,
    title='Legíny sportovní i každodenní: výběr a srovnání | Sporteka',
    desc='Sportovní legíny na běh, cvičení, jógu i zimu. Jak vybrat materiál, pas a délku, jak prát a nakupovat. Nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Legíny</strong> patří mezi kusy oblečení, které se nosí v posilovně, na trati, na podložce i cestou do práce. Právě proto se od sebe výrazně liší: jedny jsou hladké a pevné na dynamický trénink, jiné měkké a vhodné na celý den, další zateplené na chladné ráno. Cena a značka vypovídají o výběru méně než materiál, výška pasu a střih.</p>'
          '<p>Na Sportece najdete legíny z mnoha českých obchodů a u každého kusu porovnáte nabídky a dostupné velikosti. Podle činnosti se vám bude hodit také <a href="/sportovni-podprsenky/">sportovní podprsenka</a>, <a href="/sportovni-tricka/">funkční tričko</a> nebo <a href="/sportovni-ponozky/">ponožky</a>. Tento průvodce vysvětluje, na co se při výběru dívat, jak legíny ošetřovat a kterým chybám se vyhnout.</p>',
    guide='<h2>Jak číst nabídku legín</h2>'
          '<p>Slovo legíny pokrývá velmi široké spektrum. Základní rozdělení je podle účelu: výkonnostní legíny na pohyb, pohodlné na volný čas a zateplené na chladné počasí. Mezi nimi existuje spousta kompromisů, jenže čím víc se kus snaží dělat všechno, tím méně je v jednotlivých disciplínách dobrý. Než začnete porovnávat nabídky obchodů, ujasněte si, v jaké činnosti budete legíny nosit nejčastěji.</p>'
          '<h3>Rychlý přehled podle činnosti</h3>'
          + T(['Činnost', 'Na co dbát', 'Typický střih'], [
              ['Běh v teplém počasí', 'lehká látka, plochý šev, kapsa na telefon', 'dlouhé nebo 7/8, vyšší pas'],
              ['Běh v chladu', 'zateplený vnitřek, těsnější střih u kotníku', 'dlouhé, někdy se zipem u kotníku'],
              ['Posilovna a funkční trénink', 'neprůsvitnost při dřepu, pevný pas', 'vysoký pas, dlouhé nebo 7/8'],
              ['Jóga a pilates', 'měkký materiál, volný pohyb v bocích', 'vysoký pas bez tlačících švů'],
              ['Cyklistika a kolo v teple', 'vložka nebo hladký úplet, který netře', 'těsné krátké nebo 3/4'],
              ['Každodenní nošení', 'příjemný dotek, odolnost proti žmolkování', 'delší střih, měkký pas'],
              ['Turistika a outdoor', 'rychleschnoucí materiál, odolnost proti otěru', 'pevnější úplet, někdy s kapsami']]) +
          '<h2>Materiál a jeho vlastnosti</h2>'
          '<p>Materiál rozhoduje o tom, jak se legíny chovají při potu, praní i opakovaném natahování. Většina sportovních kusů je směs syntetického vlákna a elastanu. Elastan přidává pružnost, základní vlákno určuje dotek, schnutí a trvanlivost.</p>'
          '<ul><li><strong>Polyamid s elastanem</strong> je hladký, pevný a rychle schne. Hodí se na intenzivní pohyb a bývá méně náchylný na žmolkování.</li>'
          '<li><strong>Polyester s elastanem</strong> je lehký, dobře odvádí vlhkost a drží barvu. Povrch bývá matnější a trochu sušší na dotek.</li>'
          '<li><strong>Bavlna s elastanem</strong> je příjemná na každý den, jenže pot nasaje a pomalu schne, takže se do dynamického tréninku moc nehodí.</li>'
          '<li><strong>Merino a směsi s vlnou</strong> hřejí i ve vlhku a méně zapáchají. Hodí se jako spodní vrstva do chladu.</li>'
          '<li><strong>Zateplená pletenina</strong> má počesaný vnitřek, který zadrží teplo u kůže. Na chladné ráno je pohodlná, při vyšší intenzitě ale může přehřívat.</li></ul>'
          '<p>Hustota úpletu se dá posoudit i bez štítku: látka natažená proti světlu nesmí být řídká a po pustění se musí rychle vrátit do původního tvaru. Pokud zůstává vytahaná, legíny se po několika nošeních rozjedou v kolenou a v sedu.</p>'
          '<h2>Pas, švy a střih</h2>'
          '<p>Pas je nejčastější důvod, proč se legíny vracejí. Vysoký pas drží na místě při dřepech, výskocích i běhu a netlačí tak často, jak se čeká, pokud je široký a plochý. Úzká gumička naopak vtlačuje do kůže a při předklonu se zarývá. Pasy s vnitřní kapsičkou na klíč nebo kartu jsou praktické na venkovní běh.</p>'
          '<p>Důležité jsou i švy. Plochý šev se v pohybu méně odírá, kdežto vystouplý šev na vnitřní straně stehen může při delší chůzi či běhu dřít. Rozkrok se středovým švem a bez zesílení bývá slabším místem, protože na něj při pohybu působí největší tah. Kvalitní kusy mají zesílení právě tam nebo střih bez švu.</p>'
          '<h3>Délka nohavic</h3>'
          '<p>Dlouhé legíny jsou nejuniverzálnější a chrání lýtka před chladem i otěrem. Délka 7/8 končí nad kotníkem, nezachytí se o boty a v teple je příjemnější. Variantu 3/4 volí lidé, kteří běhají za vyšších teplot, a krátké biker legíny se nosí při cvičení v hale, kde je teplo. Vyšší postavy by měly zkontrolovat výrobcem uvedenou délku nohavice, protože běžný střih bývá počítaný na průměrnou výšku.</p>'
          '<h2>Kompresní, zateplené a speciální legíny</h2>'
          '<p>Kompresní legíny jsou úpletem navržené tak, aby kolem svalů vytvářely rovnoměrný tlak. Řada lidí je vnímá jako příjemné při dlouhém běhu nebo po tréninku, jenže vliv na výkon je individuální a nelze ho slibovat. Rozhoduje hlavně správná velikost: příliš těsné legíny brzdí pohyb a omezují prokrvení, příliš volné žádný efekt nemají.</p>'
          '<p>Zateplené modely hledejte spíš v <a href="/sportovni-kalhoty/">sportovních kalhotách</a> nebo mezi termoprádlem, pokud jde o skutečný mráz. Pod volné kalhoty se hodí jako spodní vrstva ve spojení s <a href="/termopradlo/">termoprádlem</a>, při lyžování ve spojení s <a href="/lyzarske-termopradlo/">lyžařským termoprádlem</a>. Těhotenské legíny mají vyšší pružný pás přes břicho a místo gumy bývají vybavené pružným pletivem, které se přizpůsobí změně objemu. Dětské legíny se vybírají z měkkého materiálu bez tlačících švů, s rezervou do délky kvůli růstu.</p>'
          '<h2>Test před nošením</h2>'
          '<p>Většina potíží se dá odhalit hned po doručení, pokud legíny vyzkoušíte promyšleně. Před stříháním štítku udělejte následující kroky:</p>'
          '<ol><li>Obujte si je a udělejte hluboký dřep před zrcadlem nebo s telefonem. Látka v sedu a zadku nesmí prosvítat.</li>'
          '<li>Předkloňte se a zdvihněte nohu. Pas nesmí sjet ani se vyhrnout.</li>'
          '<li>Projděte se a zhodnoťte, zda se nohavice v místě kolen nesbírají.</li>'
          '<li>Zkontrolujte švy na vnitřní straně stehen a rozkrok.</li>'
          '<li>Sednout si, zakřížit nohy a zjistit, zda nic netlačí.</li></ol>'
          '<p>Světlé a pastelové odstíny prosvítají víc než černá, tmavomodrá nebo antracit. U světlých barev se proto vyplatí číst v recenzích, jak se látka chová při dřepu.</p>'
          '<h2>Značky a rozdíly mezi nimi</h2>'
          '<p>Nejširší výběr mají v nabídce ' + B(('adidas', 'Adidas'), ('asics', 'Asics'), ('under-armour', 'Under Armour'), ('puma', 'Puma'), ('litex', 'Litex'), ('gymbeam', 'GymBeam'), ('4f', '4F'), ('nike', 'Nike'), ('craft', 'Craft'), ('kari-traa', 'Kari Traa'), ('dynafit', 'Dynafit'), ('domyos', 'Domyos')) + '. '
          'Značky zaměřené na výkon, například Craft, Dynafit nebo Under Armour, se soustředí na úplet, který drží tvar, a na funkční detaily. Kari Traa je spojená se skandinávským prostředím a vlněnými směsmi. Litex a GymBeam nabízejí oděvy pro každodenní cvičení a Adidas, Nike a Puma kombinují sportovní styl s výkonnějšími variantami. Střih se ale liší i mezi kolekcemi jedné značky, proto vždy ověřte velikostní tabulku konkrétního modelu.</p>'
          '<h2>Velikost: jak ji určit</h2>'
          '<p>Legíny jsou pružné, takže se snadno koupí o číslo větší nebo menší, než je vhodné. Podívejte se na tabulku výrobce a porovnejte obvod pasu a boků. Pokud jste mezi dvěma velikostmi, rozhodněte podle činnosti: na intenzivní trénink a kompresní kus zvolte přesnější velikost, na jógu a volný čas pohodlnější. Pokud nakupujete online, zkontrolujte u svého obchodu podmínky vrácení, protože legíny se nejlépe posuzují po obutí.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Legíny perte naruby při teplotě uvedené na štítku, obvykle 30 až 40 °C, a bez aviváže. Aviváž se zachytí na syntetickém vláknu, zhoršuje odvod vlhkosti a časem nasákne pachem. Neperte je spolu s oděvy, které mají suchý zip, háčky nebo drsné zipy, a nesušte na topení ani v sušičce na vysokou teplotu. Elastan teplem křehne a po několika cyklech ztrácí pružnost.</p>'
          '<ul><li>Pokud pot zapáchá, před praním namočte legíny do vlažné vody s trochou octa nebo speciálního přípravku na sportovní textil.</li>'
          '<li>Při žmolkování pomáhá šetrnější program a odstranění žmolků holicím strojkem na textil.</li>'
          '<li>Nepoužívejte bělidlo, vlákna zesvětlí a zkřehnou.</li></ul>'
          '<h2>Co s legínami kombinovat</h2>'
          '<p>Na běh se hodí s lehkým <a href="/funkcni-tricka/">funkčním tričkem</a> a při chladu s <a href="/funkcni-mikiny/">funkční mikinou</a>. Do posilovny je prakticky nosí každý v kombinaci se <a href="/sportovni-podprsenky/">sportovní podprsenkou</a> nebo krátkým topem. Přes legíny se v zimě obléknou volné kalhoty nebo se přidá větrovka a na venkovní trénink <a href="/bezecke-opasky/">běžecký opasek</a> místo kapsy v pasu. Celkový sortiment se otevírá v kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Výběr podle fotky</strong> bez kontroly materiálu. Tentýž střih může být z úplně jiné látky.</li>'
          '<li><strong>Příliš nízký pas</strong> u cvičení. Legíny pak sjíždějí a musíte je poposouvat.</li>'
          '<li><strong>Bavlna na intenzivní trénink</strong>, která pot nasaje a po chvíli se vytahuje.</li>'
          '<li><strong>Podceněná velikost</strong>, kdy látka v dřepu příliš prosvítá.</li>'
          '<li><strong>Sušení na topení</strong>, které zničí elastan.</li></ul>'
          '<h2>Pro koho jaké legíny</h2>'
          '<p>Začínající běžec ocení lehké dlouhé legíny s vyšším pasem a kapsou na telefon. Kdo chodí do posilovny, potřebuje neprůsvitné, pevné a pružné legíny s plochými švy. Pro jógu a pilates volte měkčí materiál s širším pasem. Pokud legíny nosíte celý den v kanceláři, upřednostněte měkkou pleteninu, která se nemačká a nežmolkuje. Dětem vyberte pohodlné barevné kusy a těhotným ženám střih s vysokým pružným pasem, který se přizpůsobí změně objemu.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Stejné legíny prodává často více obchodů, ale liší se dostupnými velikostmi, dobou doručení a poplatky za dopravu. Na Sportece vidíte nabídky vedle sebe a vyberete si podle toho, co vám nejvíc vyhovuje. Při nákupu s časově omezenou slevou si ověřte, zda je skladem právě vaše velikost, protože krajní velikosti se vyprodávají jako první. V případě pochybností vyberte obchod s jednoduchou výměnou.</p>',
    faq=[
        ('Jaké legíny vybrat na běhání?', 'Na běh se hodí přiléhavé legíny z polyamidu nebo polyesteru s elastanem, s plochými švy a vyšším pasem. Praktická je kapsa na telefon nebo klíč. V chladu zvolte zateplený vnitřek a dlouhé nohavice, v teplém počasí lehčí 7/8.'),
        ('Čím se liší sportovní legíny od běžných?', 'Sportovní legíny mají pevnější úplet, odvádějí pot, mají plochý šev a pružný pas, který drží i při dynamickém pohybu. Běžné módní legíny bývají měkčí a z bavlny, takže pro intenzivní trénink nejsou ideální.'),
        ('Jak poznat, že legíny nebudou prosvítat?', 'Natáhněte látku proti světlu a po obutí zkuste hluboký dřep před zrcadlem. Tmavé barvy a hustší pletenina prosvítají méně než světlé. Pokud si nejste jistí, přečtěte si recenze k danému modelu.'),
        ('Jaký pas je nejlepší na cvičení?', 'Většině lidí vyhovuje vysoký a široký pas, který drží v rovnováze při dřepech a předklonech. Měl by být plochý a pružný, aby netlačil. Úzká gumička se při cvičení zarývá do kůže.'),
        ('Pomáhají kompresní legíny k lepšímu výkonu?', 'Kompresní úplet vytváří rovnoměrný tlak kolem svalů, což mnoha lidem vyhovuje při delším běhu nebo po tréninku. Vliv na výkon je ale individuální a nelze ho zaručit. Důležitá je správná velikost.'),
        ('Jak prát legíny, aby vydržely?', 'Perte je naruby při 30 až 40 °C, bez aviváže a bělidla, a sušte volně mimo topení. Elastan teplem křehne a ztrácí pružnost, aviváž zhoršuje odvod vlhkosti.'),
        ('Jakou délku nohavic zvolit?', 'Dlouhé legíny jsou univerzální a hodí se do chladu, 7/8 zůstávají nad kotníkem a jsou příjemné v teple. Kratší 3/4 a biker legíny se nosí v hale a při vyšších teplotách. Vyšší lidé si mají zkontrolovat délku nohavice u konkrétního modelu.'),
        ('Co si obléknout na zimní běh?', 'Nejlépe kombinaci zateplených nebo vlněných legín a funkčního trička s dlouhým rukávem. Při mrazu přidejte termoprádlo a větrovku. Hlavně nepřehřívat, protože se vzniklá vlhkost později ochladí.'),
        ('Jaké legíny nosit v těhotenství?', 'Těhotenské legíny mají vyšší pružný pás, který se přizpůsobí břichu, nebo pás přes břicho. Vyberte měkký materiál bez tlačících švů a raději delší střih. Před větší zátěží se poraďte s lékařem.'),
        ('Jak vybrat legíny pro děti?', 'Dětské legíny by měly být z měkké bavlny s elastanem nebo ze sportovního úpletu, s pružným pasem bez tlačících švů. Počítejte s malou rezervou do délky kvůli růstu, ale ne s příliš velkou, jinak se pod koleny nabírají.'),
    ])

# ------------------------------------------------------------------ sportovni-bryle
NEW['sportovni-bryle'] = dict(long=True,
    title='Sportovní a sluneční brýle: průvodce výběrem | Sporteka',
    desc='Sportovní sluneční brýle na kolo, běh, turistiku, hory i vodu. Kategorie filtrů, typy čoček, rámy, péče a srovnání nabídek českých obchodů.',
    intro='<p><strong>Sportovní brýle</strong> chrání oči před slunečním zářením, větrem, prachem, hmyzem i odlétajícími kamínky. Liší se od módních slunečních brýlí pevnějším sedem na obličeji, odolnějším rámem a čočkami, které zajišťují ostrý kontrast v rychlém pohybu. Při výběru rozhoduje činnost, světelné podmínky a tvar obličeje víc než značka, takže stejný model nemusí sedět každému a vyplatí se číst popis i velikostní údaje.</p>'
          '<p>Na Sportece porovnáte nabídky brýlí z českých obchodů a zúžíte výběr podle značky nebo určení. Pro konkrétní sporty hledejte rovnou <a href="/cyklisticke-bryle/">cyklistické brýle</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a> nebo <a href="/plavecke-bryle/">plavecké brýle</a>. Níže najdete přehled kategorií filtru, typů čoček a materiálů rámu spolu s tipy, jak brýle používat a udržovat.</p>',
    guide='<h2>K čemu sportovní brýle slouží</h2>'
          '<p>Oči jsou na ultrafialové záření a ostré světlo citlivé a po několika hodinách na slunci bez ochrany se objevuje únava, slzení i pálení. Na sněhu, na vodě a v horách je odrazů světla víc než na rovině, a proto tam brýle nejsou doplněk, ale součást výbavy. Při rychlé jízdě na kole nebo při běhu v lese navíc chrání před hmyzem, větvičkami a prachem.</p>'
          '<p>Kvalitní brýle musí kombinovat tři vlastnosti: spolehlivou UV ochranu, vhodnou propustnost světla a pevný, ale lehký rám. Označení UV 400 znamená, že čočky zachytí záření až do vlnové délky 400 nanometrů, což se považuje za standard bezpečných brýlí. Tmavá čočka bez UV filtru je horší než žádná, protože rozšíří zornici a vpustí dovnitř víc záření.</p>'
          '<h2>Kategorie filtru</h2>'
          '<p>Kategorie filtru udává, kolik světla čočka propustí. Čím vyšší číslo, tím tmavší čočka.</p>'
          + T(['Kategorie', 'Propustnost', 'Typické použití'], [
              ['0', 'nejvyšší, téměř čiré', 'noc, zataženo, ochrana před větrem a hmyzem'],
              ['1', 'vysoká', 'šero, podvečer, les a mírné světlo'],
              ['2', 'střední', 'proměnlivé počasí, jaro a podzim'],
              ['3', 'nízká', 'slunečný den, léto, pláž, silnice'],
              ['4', 'nejnižší', 'vysoké hory, ledovec, extrémní sluneční svit']]) +
          '<p>Brýle kategorie 4 nejsou určené k řízení auta, protože propouštějí příliš málo světla a zhoršují rozpoznání signálů. Při jízdě v lese či tunelu naopak zvolte světlejší čočky, aby se nezhoršil kontrast. Pro sportovce, který vyráží za proměnlivého počasí, je praktická výměna čoček v jednom rámu.</p>'
          '<h2>Typy čoček</h2>'
          '<ul><li><strong>Polarizační čočky</strong> potlačují odrazy od vody, mokré silnice a sněhu. Hodí se na vodu, na rybaření a silniční jízdu. Při čtení displejů, například cyklocomputeru, mohou ale způsobit tmavé zóny.</li>'
          '<li><strong>Fotochromatické čočky</strong> samy mění propustnost podle intenzity světla. Vyplatí se, když trasa vede střídavě stínem a sluncem.</li>'
          '<li><strong>Zrcadlové čočky</strong> mají povrchovou vrstvu, která odráží část světla, a snášejí tak silné slunce. Zlepšují komfort, ale musí být odolné proti poškrábání.</li>'
          '<li><strong>Vyměnitelné čočky</strong> se prodávají v sadě, například tmavá, žlutá a čirá. Jsou praktické pro kolaře a běžce, kteří vyrážejí za různých podmínek.</li>'
          '<li><strong>Kontrastní čočky</strong> v žlutých a oranžových odstínech zvýrazňují reliéf terénu při zatažené obloze.</li></ul>'
          '<p>Materiál čoček bývá polykarbonát, který je lehký a odolný proti nárazu, nebo kvalitnější plasty s lepší optikou. Skleněné čočky se ve sportu používají zřídka, protože jsou těžší a při rozbití nebezpečnější. Na čočkách se hodí vrstva proti poškrábání a proti zamlžování, i když ani ta nenahradí správné větrání.</p>'
          '<h2>Rám, sedlo a tvar</h2>'
          '<p>Sportovní rám bývá z lehkého termoplastu, který snese ohýbání. Nosní opěrky a konce branek mají často pogumované plochy, jež při potu drží, místo aby klouzaly. Dobrý sed poznáte tak, že brýle drží, když kývnete hlavou, a netlačí za ušima ani na nose. Příliš široké brýle se při rychlém pohybu třesou, příliš úzké tlačí na spánky.</p>'
          '<p>Tvar a velikost čočky ovlivňuje krytí. Větší, zakřivené čočky chrání proti bočnímu větru a světlu, jenže mohou víc zamlžovat. Rámy bez horní hrany mají širší výhled dolů, což se hodí při jízdě v předklonu. Pokud nosíte přilbu, vyzkoušejte brýle společně s ní, protože branky nesmí kolidovat s popruhy.</p>'
          '<h2>Módní a dětské sluneční brýle</h2>'
          '<p>V nabídce najdete i klasické módní sluneční brýle značkových i menších výrobců. Chrání před sluncem stejně dobře, pokud mají čočky s UV filtrem, ale nejsou stavěné na rychlý pohyb, pot a pády, takže na sport se hodí méně. Dětské sluneční brýle vybírejte s označením UV 400, pružným rámem a pevnou gumičkou nebo ohebnými branky. Levná tmavá čočka bez UV filtru je horší než žádná, protože oko se za tmavým sklem rozšíří a pustí dovnitř více záření.</p>'
          '<h2>Brýle podle sportu</h2>'
          '<h3>Kolo a silnice</h3>'
          '<p>Kolaři potřebují lehké brýle s dobrým větráním a širokým výhledem. V terénu se hodí čirá nebo žlutá čočka do lesa a tmavá na otevřené cesty. Při rychlé jízdě se nevhodný rám třese nebo sjíždí z nosu, proto volte brýle určené přímo pro cyklistiku. Nabídku najdete v kategorii <a href="/cyklisticke-bryle/">cyklistické brýle</a>. K ochraně hlavy patří <a href="/silnicni-cyklohelmy/">silniční cyklohelmy</a> nebo <a href="/mestske-cyklohelmy/">městské helmy</a>.</p>'
          '<h3>Běh a turistika</h3>'
          '<p>Běžec chce brýle co nejlehčí, s pevnými koncovkami a bez odrazů v zorném poli. Turista ocení větší čočky, boční ochranu a kategorii 3. Ve vysokých horách a na ledovci je boční kryt a kategorie 4 nezbytná. K běžeckému vybavení patří také <a href="/cepice-a-celenky/">čepice a čelenky</a> a <a href="/bezecke-opasky/">běžecké opasky</a>.</p>'
          '<h3>Voda, zima a hory</h3>'
          '<p>Na vodě je nejužitečnější polarizace a plovoucí rám nebo pásek, který brýle drží na krku. Pod vodou ale nepoužívejte sluneční brýle, tam patří <a href="/plavecke-bryle/">plavecké brýle</a>. V zimě se na sjezdovce hodí uzavřené <a href="/lyzarske-bryle/">lyžařské brýle</a> s dvojitým sklem proti zamlžení, a pokud nelyžujete, stačí sluneční brýle s boční ochranou. Doplňkem jsou <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a> a <a href="/lyzarske-rukavice/">rukavice</a>.</p>'
          '<h2>Dětské a dioptrické brýle</h2>'
          '<p>Dětské oči propouštějí víc záření než dospělé, proto je u dětí UV filtr o to důležitější. Vybírejte brýle s označením UV 400, měkkým rámem a bezpečným uchycením, například pružným páskem. Příliš tmavé čočky, které se nosí v interiéru, zbytečně rozšiřují zornici.</p>'
          '<p>Pokud nosíte dioptrie, máte tři běžné možnosti: sportovní rám s dioptrickými čočkami od optika, klip, který se nasadí na vlastní brýle, nebo kontaktní čočky pod sportovními brýlemi. Dioptrické vložky vybírejte s ohledem na zakřivení rámu, jinak se zorné pole zkreslí.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší sortiment mají ' + B(('rockbros', 'Rockbros'), ('alpina', 'Alpina'), ('oakley', 'Oakley'), ('relax', 'Relax'), ('o-neill', "O'Neill"), ('laceto', 'Laceto'), ('r2', 'R2'), ('uvex', 'Uvex'), ('polaroid', 'Polaroid'), ('rudy-project', 'Rudy Project'), ('bliz', 'Bliz')) + '. '
          'Alpina, Uvex, Oakley a Rudy Project se zaměřují na výkonnostní brýle pro kolo, běh a zimní sporty. Rockbros nabízí širokou škálu cyklistických modelů a sad s vyměnitelnými čočkami. Relax, R2 a Laceto jsou české a slovenské značky s dostupnějším pojetím a O\'Neill míří na volnočasové a vodní sporty. Polaroid je známý polarizovanými čočkami. U všech si ověřte, že produkt uvádí UV 400 a kategorii filtru.</p>'
          '<h2>Jak brýle vyzkoušet</h2>'
          '<p>Po doručení si brýle nasaďte a projděte několik testů. Nakloňte hlavu dopředu a dozadu, zakývejte a při předklonu zkontrolujte, zda neklouzají po nose. Zkuste je s čepicí nebo přilbou, kterou běžně nosíte. Podívejte se skrz čočky na rovnou čáru, například na okraj dveří. Pokud se čára vlní nebo zkresluje, čočka má horší optickou kvalitu. Vyplatí se také rozhlédnout se do stran a ověřit, že rám nezasahuje do zorného pole a nic nedrhne za ušima.</p>'
          '<h2>Sezóna a denní doba</h2>'
          '<p>Brýle se nehodí jen v létě. Na jaře a na podzim je slunce nízko a oslňuje víc než v poledne, a v zimě ho odráží sníh. Pro stejného sportovce se proto vyplatí mít aspoň dvě sady čoček: tmavou na jasný den a světlejší pro zataženo nebo podvečer. Večerní jízda na kole nebo běh s čirou čočkou zase chrání oči před hmyzem a prachem, aniž by omezovaly vidění.</p>'
          '<h2>Péče o čočky a rám</h2>'
          '<p>Čočky nejprve opláchněte vodou, aby se odplavil prach, a teprve potom je otřete mikrovláknem. Suchá látka s prachem čočku poškrábe. Nepoužívejte běžné čisticí prostředky s alkoholem, pokud je výrobce nedoporučuje, protože mohou poškodit povrchovou vrstvu. Brýle ukládejte do tvrdého pouzdra, ne do kapsy batohu s klíči.</p>'
          '<ul><li>V létě je nenechávejte v zaparkovaném autě, teplo může deformovat rám.</li>'
          '<li>Poškrábané čočky vyměňte, na rozptýleném světle zhoršují kontrast a únava očí roste.</li>'
          '<li>Při zamlžování pomáhá lepší větrání, odstup od obličeje nebo antifog přípravek určený pro brýle.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Brýle bez UV filtru</strong> z náhodného stánku. Pouhé ztmavení ochranu nezaručuje.</li>'
          '<li><strong>Kategorie 4 na běžný den</strong>, kdy se zhorší vnímání okolí.</li>'
          '<li><strong>Příliš velké nebo malé brýle</strong>, které při pohybu sklouzávají nebo tlačí.</li>'
          '<li><strong>Polarizace u displeje</strong>, která zhoršuje čitelnost cyklocomputeru či hodinek.</li>'
          '<li><strong>Zapomenuté pouzdro</strong>, v němž se čočky poškrábou dřív, než je stihnete využít.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U stejných brýlí se nabídky obchodů liší balením, dopravou a tím, zda v ceně jsou náhradní čočky a pouzdro. Na Sportece je vidíte vedle sebe. Při srovnání dbejte na to, zda jde opravdu o stejnou variantu čoček a barvu rámu, protože jeden model se často prodává v několika provedeních s odlišnými vlastnostmi. Při sportu v horách nebo na kole nešetřete na UV ochraně a vyberte spolehlivý rám.</p>',
    faq=[
        ('Jaké sportovní brýle vybrat na běhání?', 'Nejlépe lehké, pevně držící a odvětrané, s UV 400 a kategorií 3 pro slunečný den. Pogumované opěrky zabrání sklouzávání při potu a boční krytí chrání před větrem a prachem.'),
        ('Co znamená kategorie filtru 3?', 'Jde o čočky pro slunečný den, běžné na pláži, při sportu a turistice. Propouštějí malé množství světla, ale pořád dovolují bezpečné vnímání okolí. Pro hory a ledovce se používá tmavší kategorie 4.'),
        ('K čemu jsou polarizační čočky?', 'Potlačují odlesky od vodní hladiny, mokré silnice nebo sněhu, takže zvyšují komfort a kontrast. Při čtení displejů mohou vytvářet tmavé zóny, proto je kolaři s cyklocomputerem zkoušejí předem.'),
        ('Jsou fotochromatické čočky dobrou volbou?', 'Ano, pokud se světelné podmínky během výletu mění, například střídání lesa a otevřené krajiny. Samy se tmaví a světlají, ale reakce není okamžitá, a proto se při rychlé změně světla může projevit zpoždění.'),
        ('Mohou se sportovní brýle zamlžovat?', 'Ano, hlavně při pomalém pohybu a vlhku. Pomáhá rám s větráním, větší odstup čočky od obličeje, vrstva proti zamlžení a v případě potřeby speciální antifog přípravek. Vždy se vyplatí brýle vyzkoušet před delším výletem.'),
        ('Jak vybrat dětské sluneční brýle?', 'Zvolte UV 400, měkký a pružný rám a bezpečné uchycení, například pásek na hlavu. Čočky nemají být příliš tmavé pro běžné použití a rám nesmí tlačit na nos nebo spánky.'),
        ('Mohu používat brýle s dioptriemi při sportu?', 'Ano. Možnosti jsou sportovní rám s dioptrickými čočkami od optika, klip na vlastní brýle nebo kontaktní čočky pod běžným sportovním modelem. Konkrétní řešení vždy konzultujte s očním optikem.'),
        ('Jak čistit čočky, aby se nepoškrábaly?', 'Nejdříve je opláchněte vodou, aby se odplavil prach, a pak je osušte mikrovláknem. Neutírejte je suchou látkou, papírovým kapesníkem ani oblečením. Ukládejte je do pouzdra.'),
        ('Mohu v tmavých sportovních brýlích řídit?', 'Záleží na kategorii. Pro řízení se běžně používají kategorie 0 až 3, kategorie 4 propouští příliš málo světla a je určená do extrémního slunce v horách. U polarizačních čoček zvažte čitelnost displejů a řiďte se pokyny výrobce.'),
        ('Čím se liší sportovní brýle od módních?', 'Mají pevnější a lehčí rám, pogumované opěrky, kvalitní čočky odolné nárazu a často větší krytí nebo vyměnitelné čočky. Móda se zaměřuje na vzhled, sport na sed, odolnost a optiku při pohybu.'),
    ])

# ------------------------------------------------------------------ cinky-a-kotouce
NEW['cinky-a-kotouce'] = dict(long=True,
    title='Činky a kotouče: jednoručky, osy, kettlebelly | Sporteka',
    desc='Činky, kotouče a osy do domácí posilovny. Typy, průměry, materiály, volba hmotnosti, bezpečnost a skladování. Srovnání českých e-shopů.',
    intro='<p><strong>Činky a kotouče</strong> tvoří základ domácí posilovny, protože zátěž se dá zvyšovat postupně a cviků s nimi je prakticky bez konce. Jednoručky se hodí na rychlý start a práci s malými svalovými skupinami, osa s kotouči umožní dřepy, mrtvé tahy i tlaky na lavici a kettlebelly přinášejí dynamické kruhové pohyby. Důležité je vědět, jaký systém koupit, aby se později dal rozšiřovat.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a vyberete si podle značky, typu a hmotnosti. Zvlášť najdete <a href="/kettlebelly/">kettlebelly</a>, k činkám patří také <a href="/posilovaci-stroje/">posilovací stroje</a>, <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a>. V průvodci vysvětlujeme průměry, materiály, hmotnosti i bezpečnost.</p>',
    guide='<h2>Co všechno spadá do kategorie</h2>'
          '<p>Pod hlavičkou činek a kotoučů se skrývá několik odlišných druhů zátěže. Pevné jednoručky mají neměnnou hmotnost. Nakládací činky mají krátkou tyč s pojistkami, na kterou nasazujete kotouče. Dlouhá osa je tyč pro obouruční cviky a kotouče se na ni nasazují z obou stran. Samostatnou skupinu tvoří kettlebelly, s nimiž se cvičí jinak než s klasickou činkou a mají vlastní kategorii.</p>'
          + T(['Typ', 'Výhoda', 'Omezení'], [
              ['Pevné jednoručky', 'okamžitě připravené, žádné nasazování', 'každá hmotnost zabírá místo, je potřeba víc kusů'],
              ['Nakládací jednoručky', 'hmotnost se mění po malých krocích', 'výměna kotoučů zabere čas'],
              ['Dlouhá osa s kotouči', 'dřep, tlak, mrtvý tah a veslování', 'potřebuje stojan nebo lavici a více místa'],
              ['Kettlebell', 'dynamické pohyby, jedna zátěž na celé tělo', 'vyžaduje nácvik techniky'],
              ['Kotouče samostatně', 'rozšíření stávající osy', 'musí odpovídat průměru otvoru']]) +
          '<h2>Průměr osy a otvoru kotouče</h2>'
          '<p>Nejčastější chyba při koupi je nesoulad mezi průměrem tyče a otvorem kotouče. U domácího vybavení se obvykle setkáte se dvěma systémy: užší tyče s menším otvorem a olympijské s tyčí o průměru 50 mm na koncích a stejným otvorem v kotoučích. Olympijský systém je pevnější, snese vyšší zátěž a kotouče se na něj nasazují snadněji, ale tyče i kotouče jsou dražší a těžší. Menší systém je kompaktnější a pro začínající cvičení postačuje. Před koupí vždy ověřte průměr otvoru a délku hrdla tyče, aby se na ni požadovaný počet kotoučů vešel.</p>'
          '<h2>Materiál kotoučů a činek</h2>'
          '<ul><li><strong>Litina</strong> je klasika, odolná a poměrně kompaktní. Neošetřený povrch ale koroduje a při pádu poškodí podlahu.</li>'
          '<li><strong>Pogumované kotouče</strong> mají ocelové jádro v gumě. Tlumí hluk, chrání podlahu a vypadají upraveně. Mohou být o něco objemnější.</li>'
          '<li><strong>Bumper kotouče</strong> jsou silnější a pružnější a hodí se pro zdvihy, které se mohou pouštět z výšky.</li>'
          '<li><strong>Vinylové a plastové</strong> vyplněné cementem nebo pískem se hodí pro lehčí zátěže a začátečníky. Hmotnost je při stejném objemu nižší než u litiny, takže zabírají víc místa.</li>'
          '<li><strong>Neoprenové jednoručky</strong> mají příjemný chyt a hodí se na cvičení v lehčích hmotnostech, například na aerobik nebo rehabilitaci.</li></ul>'
          '<h2>Jak zvolit hmotnost</h2>'
          '<p>Správná hmotnost je taková, se kterou zvládnete plánovaný počet opakování s čistou technikou, přičemž poslední opakování je náročné, ale ne za cenu zhoršení pohybu. Malé svalové skupiny, jako ramena, bicepsy a tricepsy, potřebují výrazně nižší zátěž než nohy, záda nebo hýždě. Začátečník by měl začínat s lehčími činkami, než si osvojí pohyb, a zátěž pak zvyšovat v malých krocích.</p>'
          '<p>Pevné jednoručky mají u začátečníků jednu nevýhodu: za pár týdnů z nich vyrostete a musíte kupovat další pár. Hodí se hlavně tam, kde chybí místo na kotouče a stojan. Nakládací systém s menšími kotouči po půl kilogramu nebo kilogramu dovoluje přidávat zátěž plynule. Pro cviky na nohy se hodí osa, protože ruce by u velké hmotnosti jednoručky neunesly.</p>'
          '<h2>Základní cviky pro domácí cvičení</h2>'
          '<p>S činkami a kotouči se dají procvičit všechny hlavní svalové skupiny. Základem jsou vícekloubové cviky, které zapojují víc svalů najednou a poskytují nejlepší poměr času k efektu:</p>'
          '<ul><li><strong>Dřep</strong> s jednoručkou u hrudi nebo s osou na zádech pro nohy a trup.</li>'
          '<li><strong>Mrtvý tah</strong> pro záda, hýždě a zadní stranu stehen.</li>'
          '<li><strong>Tlaky nad hlavu</strong> pro ramena a tricepsy.</li>'
          '<li><strong>Veslování v předklonu</strong> pro horní záda.</li>'
          '<li><strong>Tlak na lavici</strong> pro prsa, ramena a tricepsy. Potřebuje lavici nebo alespoň stabilní podložku.</li>'
          '<li><strong>Výpady</strong> s jednoručkami pro nohy a rovnováhu.</li></ul>'
          '<p>Techniku si před zvyšováním zátěže vyzkoušejte s prázdnou osou nebo lehkými činkami. Pokud nemáte zkušenosti, nechte si cviky ukázat u trenéra nebo na kvalitních videích, protože chyba v mrtvém tahu nebo dřepu může způsobit bolest zad.</p>'
          '<h2>Co dalšího se hodí k činkám</h2>'
          '<p>Pro rozšíření výbavy se vyplatí lavice, stojan na dřepy a podložka pod osu. Pro cvičení horní části těla jsou praktické <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/svihadla/">švihadla</a> na zahřátí. Po tréninku pomáhá protažení a <a href="/masazni-pomucky/">masážní pomůcky</a>. Podlahu chraňte <a href="/joga-a-podlozky/">podložkou</a> nebo speciální gumovou podlahou. Rukavice z kategorie <a href="/sportovni-rukavice/">sportovní rukavice</a> pomohou proti puchýřům, ale u těžkého tahu se mnoho cvičenců raději drží holou rukou. K tréninku se hodí <a href="/sportovni-tricka/">funkční tričko</a> a <a href="/sportovni-kratasy/">kraťasy</a>.</p>'
          '<h2>Kettlebelly</h2>'
          '<p>Kettlebell je zátěž s držadlem, jejíž těžiště je mimo ruku. Používá se k švihovým pohybům, dřepům i kruhovým pohybům, které rozvíjejí sílu a kondici zároveň. Pro začátek volte lehčí kus a nacvičte techniku, protože chyba ve švihu se projeví na bedrech. Rozdíl mezi litinovými, pogumovanými a nastavitelnými modely uvidíte v samostatné kategorii <a href="/kettlebelly/">kettlebelly</a>.</p>'
          '<h2>Bezpečnost při cvičení s činkami</h2>'
          '<ul><li>Vždy zkontrolujte, že jsou kotouče na ose zajištěné pojistkami a hmotnost je na obou stranách stejná.</li>'
          '<li>Při těžších sériích tlaku a dřepu používejte stojan s bezpečnostními rameny nebo cvičte s jistícím partnerem.</li>'
          '<li>Neházejte kotouče a činky na tvrdou podlahu bez podložky, praskne dlažba a poškodí se kotouč.</li>'
          '<li>Zahřejte se před prvními sériemi, zejména ramena, kyčle a záda.</li>'
          '<li>Nikdy necvičte, pokud cítíte ostrou bolest, a nepřidávejte hmotnost na úkor techniky.</li></ul>'
          '<h2>Kolik místa a jaká podlaha</h2>'
          '<p>Než koupíte osu, změřte místnost. Dlouhá tyč potřebuje v délce zhruba dva metry a po stranách volný prostor na nasazování kotoučů. Strop musí být dost vysoký na tlaky nad hlavu. Pro jednoručky stačí menší kout, ale pro švihové cviky potřebujete volný okruh kolem sebe. Podlaha by měla být pevná a rovná. Pokud bydlíte v bytě, myslete na sousedy pod sebou: pogumované kotouče, silná podložka a pomalé pokládání zátěže snižují hluk i vibrace.</p>'
          '<h2>Postup přidávání zátěže</h2>'
          '<p>Nejjednodušší pravidlo zní, že když zvládnete všechny plánované série s čistou technikou a poslední opakování není na hraně, příště přidáte malou zátěž. Pokud technika při posledních opakováních selhává, zůstaňte na stejné hmotnosti. Změnu zaznamenávejte do zápisníku nebo telefonu, protože bez záznamu se pokrok špatně posuzuje. Kdo má rozvržený trénink na horní a dolní polovinu těla, přidává zátěž u každé skupiny zvlášť.</p>'
          '<h2>Skladování a údržba</h2>'
          '<p>Činky skladujte na stojanu nebo v pevné poličce, aby se neodkutálely a nepadaly. Litinové a ocelové části chraňte před vlhkem, protože rez způsobí zhoršení chytu i vzhledu. Občas je setřete suchou nebo mírně vlhkou látkou a kloubové části osy lehce promažte, pokud to doporučuje výrobce. Závity na nastavitelných činkách udržujte čisté, aby se matice nezasekly.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejširší nabídku mají ' + B(('hms', 'HMS'), ('insportline', 'Insportline'), ('sedco', 'Sedco'), ('gorilla-sports', 'Gorilla Sports'), ('gymbeam', 'GymBeam'), ('hop-sport', 'Hop-sport'), ('domyos', 'Domyos'), ('fitforce', 'Fitforce'), ('merco', 'Merco'), ('lifefit', 'Lifefit'), ('sportago', 'Sportago')) + '. '
          'Insportline je česká a HMS polská značka, obě s velkým rozsahem od jednoduchých jednoruček po olympijské sety. Sedco a Hop-sport nabízejí cenově dostupné kotouče a činky pro domácí cvičení. Gorilla Sports a GymBeam se zaměřují na posilovací vybavení a doplňky a Domyos patří k sortimentu sportovního řetězce. Při srovnání dbejte na deklarovanou hmotnost, průměr otvoru a materiál povrchu.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Nesprávný průměr kotouče</strong>, který na tyč nepasuje.</li>'
          '<li><strong>Příliš těžká zátěž na začátku</strong>, která vede k nesprávné technice.</li>'
          '<li><strong>Pevné činky bez rozšíření</strong>, z nichž po měsíci vyrostete.</li>'
          '<li><strong>Cvičení na hladké podlaze</strong> bez podložky.</li>'
          '<li><strong>Nezkontrolovaná nosnost lavice</strong> vzhledem k celkové hmotnosti na ose.</li></ul>'
          '<h2>Pro koho jaký systém</h2>'
          '<p>Začátečník v bytě ocení sadu nakládacích jednoruček s menšími kotouči, které se vejdou do skříně. Zkušenější cvičenec s prostorem sáhne po olympijské ose, kotoučích a stojanu. Pro rehabilitaci a seniory jsou vhodné lehké neoprenové činky a gumy. Kdo se věnuje funkčnímu tréninku, ocení kettlebelly a nastavitelné jednoručky, které se rychle upravují mezi cviky.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Hmotné vybavení je těžké, a proto porovnávejte nejen cenu, ale i způsob a náklady na dopravu, zejména u kotoučů a os. Obchody se také liší tím, zda zboží prodávají v sadách nebo po kusech. Zkontrolujte, zda cena odpovídá pár nebo jednomu kusu, protože u činek se prodává často jednotlivě. Na Sportece vidíte nabídky vedle sebe a můžete tak zvolit obchod s nejvýhodnější celkovou dodávkou.</p>',
    faq=[
        ('Jaké činky vybrat pro začátečníka?', 'Nejvhodnější jsou nakládací jednoručky s malými kotouči, protože hmotnost zvyšujete v malých krocích. Pokud nemáte místo, postačí i pár lehčích pevných jednoruček. Důležitější než zátěž je správná technika.'),
        ('Čím se liší pevné a nakládací činky?', 'Pevné mají neměnnou hmotnost a jsou připravené ihned. Nakládací mají tyč s pojistkami a kotouče, které přidáváte či ubíráte. Zabírají méně místa a v dlouhodobém použití bývají praktičtější.'),
        ('Jaký průměr osy zvolit?', 'Záleží na tom, jaké kotouče chcete používat. Menší systémy jsou kompaktnější, olympijský s průměrem tyče 50 mm je pevnější a snese větší zátěž. Důležité je, aby průměr otvoru kotouče odpovídal ose.'),
        ('Jak těžké kotouče koupit?', 'Začněte menším počtem lehčích kotoučů, abyste mohli zátěž zvyšovat postupně. Pro nohy a záda potřebujete víc než pro ramena a ruce. Pro jemné přidávání jsou praktické kotouče po půl kilogramu.'),
        ('Jaký materiál kotoučů je nejlepší?', 'Litinové jsou odolné a kompaktní, pogumované tlumí hluk a chrání podlahu. Vinylové a plastové jsou lehčí a levnější pro lehké zátěže, ale objemnější. Rozhodněte podle místa cvičení a rozpočtu.'),
        ('Jak chránit podlahu při cvičení s činkami?', 'Použijte pevnou gumovou podložku, speciální podlahovou desku nebo kotouče s gumovým povrchem. Činky pokládejte, nepouštějte. Na dlažbě nebo parketách se nevyplatí cvičit s volně padajícími kotouči.'),
        ('Je kettlebell vhodný pro začátečníky?', 'Ano, pokud začnete lehčím kusem a naučíte se základní techniku, zejména předklon v kyčli a švih. Špatný švih zatěžuje záda. Hodí se konzultace s trenérem nebo kvalitní instruktážní video.'),
        ('Jak často mám cvičit s činkami?', 'Pro začátek se obvykle doporučují dva až tři tréninky týdně s dnem odpočinku mezi nimi. Po zvládnutí techniky lze frekvenci zvýšit a rozdělit cvičení podle svalových skupin. Dbejte i na spánek a stravu.'),
        ('Jak skladovat činky a kotouče?', 'Na stojanu nebo v pevné polici, aby se nekutálely, v suchu bez vlhka. Kovové části občas otřete, zabrání se tak rzi. Kotouče je dobré skladovat stojatě na kolíku nebo opřené v držáku.'),
        ('Potřebuji k činkám lavici?', 'Není nutná, ale rozšiřuje možnosti cvičení. Na lavici zvládnete tlaky, veslování jednou rukou a další cviky. Zkontrolujte nosnost lavice, aby unesla vás i zátěž.'),
    ])

# ------------------------------------------------------------------ fitness-pomucky
NEW['fitness-pomucky'] = dict(long=True,
    title='Fitness pomůcky: gumy, švihadla, balanční | Sporteka',
    desc='Fitness pomůcky pro domácí cvičení: posilovací gumy, švihadla, balanční pomůcky, válce a podložky. Jak vybrat, cvičit bezpečně a nakupovat.',
    intro='<p><strong>Fitness pomůcky</strong> jsou lehké, skladné a levné způsoby, jak do cvičení doma přidat odpor, koordinaci nebo regeneraci. Posilovací guma nahradí část činek, švihadlo zlepší kondici, balanční podložka zapojí hluboké svaly trupu a masážní válec pomůže po tréninku. Pro začátečníky jsou ideální, protože nevyžadují mnoho místa ani zkušeností, a zkušení je používají jako doplněk k činkám, při cestování nebo na zahřátí před tréninkem.</p>'
          '<p>Na Sportece najdete tři hlavní podkategorie: <a href="/posilovaci-gumy/">posilovací gumy a expandery</a>, <a href="/svihadla/">švihadla</a> a <a href="/balancni-pomucky/">balanční pomůcky</a>. K nim patří také <a href="/cinky-a-kotouce/">činky</a>, <a href="/joga-a-podlozky/">jógové podložky</a> a <a href="/masazni-pomucky/">masážní pomůcky</a>. Průvodce vysvětluje, jak vybrat správný odpor, jak cvičit bezpečně a jak si sestavit smysluplnou sadu.</p>',
    guide='<h2>Co fitness pomůcky umí</h2>'
          '<p>Každá pomůcka řeší jiný problém a žádná nenahradí všechny ostatní. Odporové gumy zvyšují náročnost cviků s vlastní váhou, švihadlo trénuje kondici a koordinaci, balanční pomůcky nutí tělo držet rovnováhu a válce a míčky uvolňují napjaté svaly. Rozumná sada pokryje posilování, kondici i regeneraci a vejde se do jedné krabice.</p>'
          + T(['Pomůcka', 'Co trénuje', 'Hodí se zejména na'], [
              ['<a href="/posilovaci-gumy/">Posilovací guma</a>', 'sílu horní i dolní části těla', 'začátečníky, rehabilitaci, cvičení na cestách'],
              ['<a href="/svihadla/">Švihadlo</a>', 'kondici, koordinaci, odrazy', 'zahřátí, intervaly, box a bojové sporty'],
              ['<a href="/balancni-pomucky/">Balanční podložka a půlkoule</a>', 'stabilitu kotníků a trupu', 'prevenci zranění, rehabilitaci, funkční trénink'],
              ['<a href="/masazni-pomucky/">Masážní válec a míček</a>', 'uvolnění svalů a fascií', 'regeneraci po běhu a posilování'],
              ['<a href="/joga-a-podlozky/">Podložka</a>', 'komfort a ochranu při cvičení na zemi', 'jógu, pilates, cviky na trup']]) +
          '<h2>Posilovací gumy a expandery</h2>'
          '<p>Gumy se vyrábějí v několika podobách. Uzavřené smyčky se navlékají kolem nohou nebo zápěstí a hodí se na cviky na hýždě a ramena. Dlouhé pásy s úchyty se upevňují za dveře a slouží k veslování nebo tlakům. Trubicové expandery s rukojeťmi připomínají kladku, a proto je vyberou ti, kdo chtějí cvičit jako s činkami. Existují i minismyčky z látky, které se při cvičení méně svinují a lépe drží na kůži.</p>'
          '<p>Odpor se obvykle rozlišuje barvou či označením, jenže mezi značkami neexistuje jednotná stupnice. Žlutá guma jedné značky může být těžší než zelená jiné. Při výběru proto sledujte údaje o odporu v popisu a začínejte s lehčím. Nejčastější chyba je koupit rovnou nejsilnější, což vede k nesprávné technice a bolesti kloubů. Praktická je sada několika odporů, protože malé svaly, jako ramena, potřebují menší zátěž než nohy.</p>'
          '<ul><li>Před cvičením zkontrolujte, zda guma nemá drobné trhlinky.</li>'
          '<li>Nenatahujte ji přes dvojnásobek délky, jinak se zbytečně opotřebuje.</li>'
          '<li>Dbejte na pevné ukotvení, aby vám při puštění neprasklo do obličeje.</li>'
          '<li>Latexové gumy nemají používat lidé s alergií na latex. Existují varianty z textilu nebo jiných materiálů.</li></ul>'
          '<h2>Švihadla</h2>'
          '<p>Švihadlo je jednoduchá a efektivní kondiční pomůcka. Na výběr jsou lanová, kabelová, korálková i rychlostní modely. Lehké drátové lanko s ložisky v rukojeti se otáčí rychle a hodí se pro intervaly. Plastové korálkové lanko je pomalejší a poskytuje zpětnou vazbu pro začátečníky. Těžší lana s vahami v rukojeti zapojují ramena a předloktí a se používají na silovější trénink.</p>'
          '<p>Délka lana se nastavuje podle výšky: když se postavíte středem na lano, rukojeti mají sahat zhruba k podpaží. Skákejte na pružném povrchu, ne na betonu, a zvolte obuv s tlumením. Při začátcích pomáhá střídat krátké intervaly skákání s chůzí, protože lýtka a achilovky se potřebují přizpůsobit. Správný skok je nízký a přistává na přední části chodidla.</p>'
          '<h2>Balanční pomůcky</h2>'
          '<p>Balanční podložky, půlkoule a nestabilní disky vytvářejí nerovný povrch a nutí tělo stabilizovat se. Zapojují malé svaly kolem kotníků a kolen a hluboké svalstvo trupu. Používají se při rehabilitaci po výronech, při přípravě na sport a při cvičení pro lepší držení těla. Jsou užitečné i pro běžce a turisty, kteří chtějí posílit kotník.</p>'
          '<p>Začínejte vždy na pevném místě a s oporou, abyste se mohli chytit. Na nestabilním povrchu se nemá cvičit s těžkou zátěží, protože ztráta rovnováhy by mohla končit zraněním. Pokud máte potíže s kloubem nebo po úrazu, nechte si cviky doporučit od fyzioterapeuta. Balanční pomůcky se dělí na nafukovací, pěnové a tvrdé. Nafukovací si upravíte podle pocitu, pěnové jsou jednodušší a levnější a tvrdé disky vydrží nejdéle.</p>'
          '<h2>Regenerace a mobilita</h2>'
          '<p>Po tréninku se vyplatí věnovat pár minut uvolnění. Pěnový válec nebo masážní míček pomáhá uvolnit napjatá místa ve svalech a fascii, hodí se na lýtka, stehna a záda. Tvrdost válce rozhoduje o intenzitě: měkký je vhodný pro začátečníky, tvrdší pro zkušenější. Masážní pomůcky se nikdy nemají valit přímo přes kloub ani bolestivé místo, které je akutně zraněné. Najdete je v kategorii <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>'
          '<h2>Jak si sestavit domácí cvičení</h2>'
          '<p>Základní sada pro začátek obsahuje podložku, dvě až tři gumy různého odporu a švihadlo. To stačí na cvičení celého těla třikrát týdně. Pokud chcete přidat zátěž, přibudou <a href="/cinky-a-kotouce/">činky</a> nebo <a href="/kettlebelly/">kettlebell</a>. Pro cvičení nohou a hýždí se hodí minismyčky, pro horní polovinu těla dlouhá guma s úchyty. Po několika týdnech lze přidat balanční prvky.</p>'
          '<ol><li>Zahřejte se pěti minutami lehkého pohybu, například chůzí nebo švihadlem.</li>'
          '<li>Zvolte šest až osm cviků, které zapojí nohy, záda, hrudník, ramena a trup.</li>'
          '<li>Dělejte dvě až tři série každého cviku s odpočinkem mezi nimi.</li>'
          '<li>Zakončete protažením a krátkým uvolněním válcem.</li></ol>'
          '<h2>Příklad krátkého tréninku</h2>'
          '<p>Pokud nevíte, jak začít, vyzkoušejte jednoduchý okruh na celé tělo. Dřepy s minismyčkou nad koleny, veslování s dlouhou gumou, kliky nebo kliky na kolenou, výpady vzad, prkno na podložce a nakonec dvě minuty švihadla. Každé cvičení dělejte přibližně 30 až 40 sekund, krátce odpočiňte a okruh zopakujte dvakrát až třikrát. Za dvacet až třicet minut zapojíte všechny hlavní svalové skupiny. S postupem času prodlužujte čas nebo přidávejte silnější gumu.</p>'
          '<h2>Rehabilitace a prevence</h2>'
          '<p>Lehké gumy a balanční pomůcky se využívají po zraněních kotníku, kolene nebo ramene, protože dovolují jemně dávkovanou zátěž. Cviky po úrazu ale mají vždy vycházet z doporučení lékaře nebo fyzioterapeuta, který určí rozsah pohybu i odpor. Pomůcky nejsou náhradou za odborné vyšetření. Pro prevenci se vyplatí pravidelně posilovat kotníky, hýždě a svaly kolem lopatek, což ocení běžci i lidé pracující u počítače.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Při cvičení doma se hodí pružné <a href="/leginy/">legíny</a> nebo <a href="/sportovni-kratasy/">kraťasy</a>, prodyšné <a href="/sportovni-tricka/">tričko</a> a pro ženy <a href="/sportovni-podprsenky/">sportovní podprsenka</a>. K protiskluzovému chytu pomohou <a href="/sportovni-rukavice/">sportovní rukavice</a>, na cvičení naboso nebo v ponožkách protiskluzové <a href="/sportovni-ponozky/">sportovní ponožky</a>. Vodu si vezměte do <a href="/lahve-a-termosky/">láhve</a>. Pokud cvičíte venku, přidejte <a href="/sportovni-bryle/">sportovní brýle</a> proti slunci.</p>'
          '<h2>Pro koho které pomůcky</h2>'
          '<ul><li><strong>Začátečník</strong> začne s podložkou a gumami, protože nabízejí bezpečný odpor a snadno se učí.</li>'
          '<li><strong>Běžec a turista</strong> využije válec na regeneraci a balanční podložku na posílení kotníků.</li>'
          '<li><strong>Zkušený cvičenec</strong> přidá závěsný trenažér a těžší gumy jako doplněk k činkám.</li>'
          '<li><strong>Senior</strong> ocení lehké gumy, stabilní podložku a židli pro oporu.</li>'
          '<li><strong>Dítě a rodina</strong> si užijí švihadlo nebo balanční disky jako hru.</li></ul>'
          '<h2>Na co si dát pozor u levných kusů</h2>'
          '<p>Velmi levné gumy a švihadla mohou mít nepřesné značení odporu, slabé švy nebo rukojeti, které se při potu otáčejí. Před koupí si přečtěte recenze a popis materiálu, zkontrolujte, zda je přiložen návod ke cvičení, a u balančních pomůcek ověřte maximální nosnost.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr pomůcek mají ' + B(('merco', 'Merco'), ('hms', 'HMS'), ('insportline', 'Insportline'), ('gymbeam', 'GymBeam'), ('sedco', 'Sedco'), ('viking', 'Viking'), ('sportago', 'Sportago'), ('acra-sport', 'ACRA Sport'), ('power-system', 'Power System'), ('fitforce', 'Fitforce'), ('domyos', 'Domyos'), ('lifefit', 'Lifefit')) + '. '
          'Merco, HMS, Insportline a Sedco nabízejí široký sortiment pro domácí cvičení. GymBeam se zaměřuje na fitness komunitu a doplňky. Viking je známý outdoorovým vybavením a Power System má zaměření na posilování. Podle popisu u konkrétního produktu ověřte odpor, rozměr a materiál.</p>'
          '<h2>Další pomůcky v nabídce</h2>'
          '<p>Kromě gum, švihadel a balančních pomůcek najdete v kategorii i další kusy. Zdvihací pásky a vzpěračský pás pomáhají při těžkých tazích, kolečko na břicho posiluje trup a odporový padák se hodí na sprinty. Power bag nebo vibrační podložka doplní domácí trénink, metové kužele označí hrací plochu. Před koupí si u každého kusu ověřte, k čemu je určený a jaké zátěži odpovídá.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Gumy i látkové pásky skladujte mimo přímé slunce a teplo, protože latex stárne a křehne. Po cvičení je setřete vlhkým hadříkem, případně pudrem proti lepení. Podložky a válce čistěte jemným mýdlem a vlažnou vodou. Švihadlo po použití odložte na háček, aby se lano nezalomilo. Nafukovací pomůcky nepřefukujte na maximum, aby nepraskly.</p>'
          '<h2>Časté chyby při výběru a používání</h2>'
          '<ul><li><strong>Příliš silná guma na začátku</strong>, která nutí ke kompenzačním pohybům.</li>'
          '<li><strong>Cvičení bez zahřátí</strong>, zvláště u skoků a gum na ramena.</li>'
          '<li><strong>Špatně ukotvená guma</strong>, která se může vyšmeknout.</li>'
          '<li><strong>Balanční cvičení bez opory</strong> po úrazu kloubu.</li>'
          '<li><strong>Nesprávně dlouhé švihadlo</strong>, které se zachytává o zem nebo se mrská nad hlavou.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Fitness pomůcky se často prodávají v sadách, jež obsahují gumy několika odporů, popruhy a pouzdro. Při srovnání proto sledujte nejen cenu, ale i obsah balení a poštovné, protože u drobností mívá doprava velký podíl. Stejný produkt může být u jednoho obchodu jednotlivě a u druhého v sadě. Na Sportece se nabídky řadí vedle sebe a snadno poznáte, kde je vybavení výhodné.</p>',
    faq=[
        ('Jaké pomůcky vybrat na cvičení doma?', 'Pro začátek stačí podložka, sada posilovacích gum a švihadlo. Pokryjí posilování, kondici i protažení. Později přidejte činky nebo kettlebell, balanční podložku a masážní válec.'),
        ('Jak vybrat posilovací gumu?', 'Podle odporu a typu cvičení. Začněte lehčí a přecházejte na silnější podle pokroku. Smyčky se hodí na nohy, dlouhé pásy s úchyty na záda a ramena. Odpor se mezi značkami liší, proto čtěte popis.'),
        ('Jak dlouhé švihadlo potřebuji?', 'Když se postavíte středem na lano, rukojeti by měly sahat zhruba k podpaží. Příliš dlouhé lano se zachytává o zem, příliš krátké nutí k velkým skokům. Mnoho modelů lze zkrátit.'),
        ('K čemu je balanční podložka?', 'Trénuje stabilitu kotníků, kolen a trupu a zapojuje hluboké stabilizační svaly. Využívá se při rehabilitaci i přípravě na sport. Začínejte s oporou a na pevném místě.'),
        ('Pomůže pěnový válec po tréninku?', 'Mnoha lidem uleví od pocitu ztuhlosti a pomáhá s uvolněním svalů a fascií. Neměl by se používat přímo na kloub nebo čerstvé zranění. Začněte s měkčím válcem a intenzitu zvyšujte postupně.'),
        ('Jak poznám, že guma je poškozená?', 'Drobné trhlinky, ztráta pružnosti, lepkavý povrch nebo ztenčená místa naznačují stárnutí. Takovou gumu raději vyměňte, protože může prasknout při natažení. Skladujte ji mimo slunce a teplo.'),
        ('Mohu cvičit s gumami, pokud mám alergii na latex?', 'Ano, existují gumy z textilu nebo bezlatexové materiály. U produktu vyhledejte údaj o materiálu a v případě pochybností se poraďte s lékařem.'),
        ('Je švihadlo vhodné pro začátečníky?', 'Ano, když začnete krátkými intervaly a pomalým tempem. Skákejte na pružném povrchu, v obuvi s tlumením a s nízkými skoky. Lýtka a achilovky si potřebují zvyknout.'),
        ('Kolikrát týdně cvičit s pomůckami?', 'Pro začátek dva až tři tréninky týdně s odpočinkem mezi nimi. Se zlepšením se frekvence zvyšuje. Dbejte na zahřátí, techniku a regeneraci a přizpůsobte zátěž svým schopnostem.'),
        ('Mohou děti cvičit s fitness pomůckami?', 'Ano, švihadlo a balanční disky jsou vhodné jako hra a pohyb. Používejte lehčí pomůcky a dohled dospělého, zejména u gum a nafukovacích prvků. Zátěžové cviky s těžkými odpory se pro děti nehodí.'),
    ])
