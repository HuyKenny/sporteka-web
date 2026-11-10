"""sporteka.cz — texts of wave 1, part B: clothing and swimwear (3. 11. 2026). Same rules as texty_vlna1a.py."""
from texty_vlna1a import T

NEW = {}

NEW['sportovni-obleceni'] = dict(
    title='Sportovní oblečení – porovnání cen v e-shopech | Sporteka',
    desc='Sportovní oblečení pánské, dámské i dětské: trička, mikiny, kalhoty, legíny, bundy a termoprádlo. Porovnejte ceny a velikosti u českých obchodů.',
    intro='<p><strong>Sportovní oblečení</strong> má za úkol odvádět pot, nebránit pohybu a ochránit vás před počasím. Podle sportu a sezóny se skládá z několika vrstev: spodní prádlo a <a href="/sportovni-tricka/">trička</a>, '
          'střední vrstva jako <a href="/mikiny/">mikina</a> nebo fleece a vnější <a href="/sportovni-bundy/">bunda</a>. Na běh, do posilovny i na turistiku se vyplatí funkční materiály, na volný čas stačí bavlněné směsi.</p>'
          '<p>Na Sportece porovnáte ceny oblečení z českých obchodů a uvidíte, které velikosti jsou skladem. Výběr zúžíte podle pohlaví, značky, velikosti a ceny. '
          'Hledáte-li konkrétní kus, otevřete <a href="/leginy/">legíny</a>, <a href="/sportovni-kalhoty/">kalhoty</a>, <a href="/sportovni-kratasy/">kraťasy</a> nebo <a href="/termopradlo/">termoprádlo</a>.</p>',
    guide='<h2>Jak vybrat sportovní oblečení</h2>'
          '<p>Oblečení vybírejte podle aktivity, intenzity a počasí. Pro stejný sport potřebujete v létě něco jiného než v zimě, a kdo se potí rychle, ocení jiné materiály než ten, kdo chodí pomalu. '
          'Dobré sportovní oblečení poznáte podle toho, že si ho při pohybu nevšimnete.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Polyester:</strong> rychle schne, odvádí pot a drží tvar. Nejčastější materiál funkčního oblečení. Může déle držet pach.</li>'
          '<li><strong>Polyamid (nylon):</strong> odolný a příjemný na dotek, používá se u legín, kraťasů a bund.</li>'
          '<li><strong>Elastan:</strong> přidává pružnost, bývá v poměru několika procent.</li>'
          '<li><strong>Merino:</strong> přírodní vlna, která hřeje i vlhká a méně zapáchá. Je dražší a citlivější na praní.</li>'
          '<li><strong>Bavlna:</strong> příjemná na každý den, ale nasákne potem a pomalu schne, na intenzivní sport se nehodí.</li></ul>'
          '<h3>Vrstvení</h3>'
          '<p>V chladnu se osvědčuje systém tří vrstev. První vrstva (<a href="/termopradlo/">termoprádlo</a>) odvádí pot od těla, druhá (<a href="/fleecove-mikiny/">fleece</a>, mikina) hřeje a třetí (bunda) chrání před větrem a deštěm. '
          'Na jaře a na podzim stačí často jen dvě. Vrstvy mají být volnější, aby mezi nimi mohl cirkulovat vzduch.</p>'
          '<h3>Střih a velikost</h3>'
          '<p>Sportovní střih bývá přiléhavější, než jste zvyklí z civilních věcí. Pro běh a fitness je dobrý přiléhavý střih, který nešmouhá a neřeže. Na turistiku a volný čas sedí volnější. '
          'Velikost vybírejte podle tabulky výrobce a míry hrudníku, pasu a boků, ne jen podle písmene. Značky se liší, někdy i o celou velikost.</p>'
          + T(['Aktivita', 'Na co se zaměřit'], [['Běh', 'lehký prodyšný materiál, reflexní prvky, kapsy'], ['Fitness a posilovna', 'pružnost, přiléhavý střih, odvod potu'], ['Turistika', 'rychle schnoucí vrstvy, bunda proti větru a dešti'], ['Zima a lyže', 'termoprádlo, zateplená vrstva, membránová bunda']]) +
          '<h3>Péče o oblečení</h3>'
          '<p>Funkční oblečení perte na 30 až 40 °C, bez aviváže (zhoršuje odvod potu) a nesušte v sušičce na vysokou teplotu. Pokud nepříjemný pach nezmizí, pomůže namáčení v roztoku s octem nebo speciální prací prostředek. '
          'Mikiny a legíny perte naruby, snížíte žmolkování a odření potisku.</p>'
          '<h3>Srovnání cen</h3>'
          '<p>Sportovní oblečení se často slevuje o sezónu dřív. V cenách se liší nejen obchody, ale i velikosti a barevné varianty téhož kusu. Proto u každého produktu vidíte nabídky obchodů vedle sebe i s dostupností velikostí.</p>',
    faq=[('Z čeho má být sportovní oblečení?', 'Na intenzivní sport z polyesteru nebo polyamidu s trochou elastanu. Rychle schnou a odvádějí pot. Bavlna se hodí spíš na volný čas.'),
         ('Jak prát sportovní oblečení?', 'Na 30 až 40 °C, bez aviváže a naruby. Nesušte na topení ani v sušičce na vysokou teplotu, materiál se poškodí.'),
         ('Co znamená vrstvení oblečení?', 'Několik tenčích vrstev místo jedné tlusté: termoprádlo odvádí pot, střední vrstva hřeje a vnější chrání před větrem a deštěm. Vrstvy se dají přidávat a ubírat.'),
         ('Jak poznám správnou velikost sportovního oblečení?', 'Změřte hrudník, pas a boky a porovnejte s tabulkou výrobce. Sportovní střih bývá přiléhavější a značky se liší, proto se neřiďte jen písmenem.'),
         ('Hodí se bavlněné tričko na sport?', 'Na krátké a lehké cvičení ano, na delší nebo intenzivnější sport ne. Bavlna nasákne potem, pomalu schne a může dřít.'),
         ('Kdy se sportovní oblečení nejvíc slevuje?', 'Zimní kusy se výrazně slevňují na konci zimy, letní koncem léta. Slevy se často týkají minulých kolekcí, takže hledejte hlavně velikosti a barvy, které zůstaly skladem.')],
)

NEW['mikiny'] = dict(
    title='Mikiny – porovnání cen pánských a dámských | Sporteka',
    desc='Mikiny pánské, dámské a dětské: s kapucí, na zip, fleecové i funkční. Porovnejte ceny a velikosti skladem v českých sportovních obchodech.',
    intro='<p><strong>Mikina</strong> je střední vrstva pro sport i volný čas. Na běh nebo fitness se hodí lehká funkční mikina, která odvádí pot, na chladné dny a výlety zase <a href="/fleecove-mikiny/">fleecová mikina</a>. '
          'Bavlněné mikiny jsou příjemné na každý den, ale delší sport se v nich špatně nosí.</p>'
          '<p>Na Sportece najdete mikiny z českých obchodů s cenou, slevou a velikostmi skladem. Vybírat můžete podle značky, velikosti a střihu: s kapucí, na zip, přes hlavu nebo s límcem. '
          'Hledáte-li něco přímo na trénink, podívejte se na <a href="/funkcni-mikiny/">funkční mikiny</a>, doplnit je můžete <a href="/teplaky/">teplákovou soupravou</a>.</p>',
    guide='<h2>Jak vybrat mikinu</h2>'
          '<p>Mikinu vybírejte podle toho, jak ji budete nosit. Na sport rozhoduje materiál a odvod potu, na volný čas střih a pohodlí. Pokud chcete obojí, vezměte směs bavlny a polyesteru.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Bavlna:</strong> měkká a příjemná na dotek, ale nasákne potem a pomalu schne.</li>'
          '<li><strong>Směs bavlny a polyesteru:</strong> drží tvar, méně se mačká a rychleji schne. Častá volba pro každý den.</li>'
          '<li><strong>Polyester a funkční materiály:</strong> odvádí pot a schne rychle, hodí se na běh a trénink.</li>'
          '<li><strong>Fleece:</strong> lehký a hřejivý, vhodný na chladné dny a pod bundu.</li></ul>'
          '<h3>Střih a provedení</h3>'
          '<p>Mikina přes hlavu s kapucí je klasika, na zip se lépe svléká při pohybu a hodí se do tepla. Oversize střih je volný a módní, ale při sportu překáží. Pokud mikinu nosíte pod bundu, vezměte přiléhavější. '
          'Kapsa na zip se hodí na klíče a telefon, manžety a lem z pružné pleteniny drží teplo a tvar.</p>'
          '<h3>Velikost</h3>'
          '<p>U mikin se střihy liší: některé jsou klasické, jiné rozšířené nebo zkrácené. Podívejte se na tabulku s šířkou a délkou, nejen na písmeno. U bavlny počítejte s tím, že se po praní může mírně srazit. '
          'Dětské mikiny kupujte raději s malou rezervou, ale ne příliš velké, aby překážely při hře.</p>'
          + T(['Využití', 'Doporučení'], [['Běh a fitness', 'funkční materiál, přiléhavý střih'], ['Chladné dny a výlety', 'fleece nebo zateplená mikina'], ['Volný čas a škola', 'bavlněná směs, kapuce, kapsa'], ['Pod bundu', 'tenčí přiléhavá mikina']]) +
          '<h3>Praní a péče</h3>'
          '<p>Mikiny perte naruby na 30 až 40 °C, abyste zachovali potisk a omezili žmolky. Žmolky vznikají třením, odstraníte je žmolkovačem nebo jemným holicím strojkem pro textil. Zip před praním zapněte, aby nepoškodil látku. '
          'Sušte volně, nejlépe na ramínku nebo pověšené, ne přímo na topení.</p>'
          '<h3>Srovnání cen</h3>'
          '<p>Mikiny známých značek se v obchodech slevují v různou dobu. Na Sportece vidíte u jednoho modelu nabídky více obchodů a velikosti skladem, takže poznáte, kde se vyplatí koupit.</p>',
    faq=[('Jak se zbavit žmolků na mikině?', 'Žmolkovačem nebo jemným holicím strojkem na textil. Předcházet jim můžete praním naruby při 30 °C a sušením bez sušičky.'),
         ('Jak prát mikinu, aby nebyla sražená?', 'Perte ji naruby na 30 až 40 °C, bez horké vody a bez prudkého ždímání. Bavlna se může mírně srazit, proto sušte volně.'),
         ('Jaká mikina je vhodná na sport?', 'Funkční z polyesteru nebo směsi, která odvádí pot a rychle schne. Bavlněná mikina je příjemná, ale při intenzivním pohybu nasákne.'),
         ('Jaký je rozdíl mezi mikinou a fleecem?', 'Fleece je lehčí, hřeje i vlhký a rychle schne, mikina bývá z hustší pleteniny a je spíš na každý den. Na výlety se hodí fleece.'),
         ('Jak poznám správnou velikost mikiny?', 'Porovnejte šířku a délku z tabulky s mikinou, která vám sedí. Střihy se liší, takže nespoléhejte jen na písmeno velikosti.'),
         ('Kdy se mikiny nejvíc slevují?', 'Nejvíc na konci zimy a koncem léta. Slevy se týkají hlavně minulých barev a kolekcí, proto hledejte hlavně velikosti, které zůstaly skladem.')],
)

NEW['leginy'] = dict(
    title='Legíny – porovnání cen sportovních a zateplených | Sporteka',
    desc='Sportovní legíny dámské: kompresní, zateplené, push up i s vysokým pasem. Porovnejte ceny, slevy a velikosti skladem u českých obchodů.',
    intro='<p><strong>Legíny</strong> se nosí na běh, do posilovny, na jógu i každý den. Sportovní legíny jsou pružné, drží tvar a odvádějí pot, civilní bývají měkčí a hodí se k tunikám a svetrům. '
          'Na zimu existují zateplené modely, na výkon kompresní a na cvičení legíny s vysokým pasem, který drží a nerolluje se.</p>'
          '<p>Na Sportece najdete legíny z českých obchodů s porovnáním ceny a dostupnosti velikostí. Zúžíte je podle značky, velikosti a ceny. Součástí outfitu mohou být i <a href="/sportovni-podprsenky/">sportovní podprsenky</a> '
          'nebo <a href="/sportovni-tricka/">funkční trička</a>, a pro volnější styl <a href="/sportovni-kratasy/">kraťasy</a>.</p>',
    guide='<h2>Jak vybrat legíny</h2>'
          '<p>Legíny vybírejte podle toho, co v nich budete dělat. Na intenzivní cvičení potřebujete pevnou, neprůsvitnou látku a vysoký pas, na běh lehčí materiál s kapsou, na zimu zateplení.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Polyamid s elastanem:</strong> hladké, pružné, rychle schnou. Nejčastější materiál sportovních legín.</li>'
          '<li><strong>Polyester s elastanem:</strong> lehčí, dobře odvádí pot, bývá matný.</li>'
          '<li><strong>Bavlna s elastanem:</strong> měkká a příjemná na každý den, hůř schne a při cvičení může klouzat.</li>'
          '<li><strong>Zateplený (brushed) materiál:</strong> vnitřek je našpendlený a hřeje, hodí se na běh v chladu.</li></ul>'
          '<h3>Pas a střih</h3>'
          '<p>Vysoký pas drží břicho a při cvičení se nesrolovává. Nižší pas je volnější. Dobře padnoucí legíny nesmí klouzat a v pase nesmí škrtit. Šev v rozkroku, plochý šev a zesílené místo v kolenou zvyšují pohodlí. '
          'Kapsa na telefon na boku nebo v pasu se hodí na běh.</p>'
          '<h3>Délka</h3>'
          '<p>Dlouhé legíny jsou univerzální, 7/8 a 3/4 jsou lehčí na léto a nezachytí se o boty, kraťasové (biker) se hodí na cvičení a do tepla. Při výběru počítejte s tím, že u vyšších postav bývá potřeba delší střih.</p>'
          '<h3>Kompresní a push up</h3>'
          '<p>Kompresní legíny jemně stahují svaly a mají stabilizovat při pohybu. Efekt na výkon je individuální, hodí se spíš pro komfort. Push up legíny mají šev nebo střih, který tvaruje, ale nejsou určeny pro intenzivní běh. '
          'Těhotenské legíny mají vyšší pás nebo pružný pás přes břicho.</p>'
          '<h3>Test průsvitnosti</h3>'
          '<p>Před koupí si legíny natáhněte a zkontrolujte, zda se při předklonu nebo dřepu látka nerozevírá a neprosvítá. Světlé barvy jsou obvykle průsvitnější než černé. Recenze a popis výrobce se na to často zaměřují.</p>'
          + T(['Využití', 'Vhodné legíny'], [['Běh v teple', '7/8 nebo 3/4, lehký polyamid, kapsa'], ['Běh v zimě', 'zateplený materiál, dlouhé nohavice'], ['Posilovna a jóga', 'vysoký pas, neprůsvitná látka'], ['Každodenní nošení', 'bavlna s elastanem, měkký pas']]) +
          '<h3>Praní</h3>'
          '<p>Legíny perte na 30 až 40 °C, bez aviváže a naruby, aby se materiál netřel. Nesušte na topení a v sušičce na nejvyšší teplotu, elastan se poškodí a legíny ztratí tvar.</p>',
    faq=[('Jak nosit legíny?', 'Sportovní legíny na trénink s funkčním tričkem nebo top. Civilní se hodí k dlouhému svetru, tunice nebo mikině. K šatům a sukni vyber jemnější a tmavší.'),
         ('Jaké legíny na běhání?', 'Přiléhavé z polyamidu s elastanem, v zimě zateplené. Hodí se kapsa na telefon a plochý šev, který neotlačuje.'),
         ('Co jsou kompresní legíny?', 'Legíny, které jemně stahují svaly. Mají pomoci s komfortem a stabilitou při pohybu. Vliv na výkon je individuální.'),
         ('Jak poznám, že legíny nebudou průsvitné?', 'Natáhněte látku proti světlu, zkuste dřep a předklon před zrcadlem. Tmavé barvy a hustší pletenina prosvítají méně.'),
         ('Jak prát legíny?', 'Naruby na 30 až 40 °C bez aviváže. Sušte volně, ne na topení, jinak se poškodí elastan.'),
         ('Jaké legíny na zimu?', 'Zateplené s hladkým vnějškem a měkkým pleteným vnitřkem, v kombinaci s termoprádlem při velkém mrazu. Dlouhé nohavice chrání lýtka.')],
)

NEW['sportovni-kalhoty'] = dict(
    title='Sportovní kalhoty – porovnání cen v e-shopech | Sporteka',
    desc='Sportovní kalhoty pánské i dámské: outdoorové, lyžařské, tepláky a funkční. Porovnejte ceny a velikosti skladem u českých e-shopů.',
    intro='<p><strong>Sportovní kalhoty</strong> jsou rozcestník pro tepláky, outdoorové kalhoty, lyžařské kalhoty a funkční modely na běh a trénink. Pro stejný sport jsou v létě vhodné lehké rychleschnoucí kalhoty, '
          'v zimě zateplené nebo membránové. <a href="/outdoorove-kalhoty/">Outdoorové kalhoty</a> vydrží větší zátěž, <a href="/teplaky/">tepláky</a> jsou pohodlné na každý den.</p>'
          '<p>Sporteka porovnává kalhoty z českých obchodů. Vidíte ceny, slevy a velikosti skladem, vybírat lze podle pohlaví, značky a ceny. Na zimu se podívejte i na <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>',
    guide='<h2>Jak vybrat sportovní kalhoty</h2>'
          '<p>Kalhoty vybírejte podle aktivity, počasí a toho, kolik pohybu vyžadují. Pro turistiku jsou důležité odolnost a rychlé schnutí, pro běh lehkost, pro lyže izolace a vodotěsnost.</p>'
          '<h3>Typy sportovních kalhot</h3>'
          '<ul><li><strong>Outdoorové kalhoty:</strong> z odolného rychleschnoucího materiálu, často s odepínacími nohavicemi nebo UV ochranou.</li>'
          '<li><strong>Tepláky:</strong> pohodlné, z bavlny nebo směsi, na volný čas a trénink.</li>'
          '<li><strong>Běžecké a tréninkové kalhoty:</strong> lehké, pružné, s elastickým pasem a zipem na kotníku.</li>'
          '<li><strong>Lyžařské kalhoty:</strong> zateplené, voděodolné nebo s membránou, se sněhovou manžetou.</li>'
          '<li><strong>Softshellové kalhoty:</strong> chrání před větrem a lehkým deštěm, jsou pružné.</li></ul>'
          '<h3>Materiál</h3>'
          '<p>Polyamid a polyester s elastanem jsou lehké a schnou rychle, softshell hřeje a odolává větru. Membrána (například GORE-TEX) je vodotěsná, ale hůř větrá, takže se hodí na dlouhé deštivé výlety a lyže. '
          'U běžných kalhot rozhoduje hlavně pohodlí a pružnost.</p>'
          '<h3>Střih a velikost</h3>'
          '<p>Rovný střih je univerzální, zúžený (tapered) se hodí k botám a na sport, volnější pro každodenní nošení. Velikost odvozujte od pasu a délky nohavic, ne jen od písmene. '
          'Pokud pasujete do dvou velikostí, vyberte při sportu spíš menší, při volném čase větší. Dětské kalhoty kupujte s malou rezervou v délce.</p>'
          + T(['Aktivita', 'Vhodné kalhoty'], [['Turistika v létě', 'lehké rychleschnoucí outdoorové'], ['Turistika na podzim', 'softshell, voděodolný materiál'], ['Běh a trénink', 'pružné, lehké, se zipem na kotníku'], ['Lyže a snowboard', 'zateplené s membránou a sněhovou manžetou']]) +
          '<h3>Praktické detaily</h3>'
          '<p>Kapsy na zip uloží klíče a telefon, nastavitelný pas a pásek zajistí dobrou polohu, zesílení v kolenou a zadku prodlouží životnost. Reflexní prvky se hodí při běhu za šera.</p>'
          '<h3>Praní</h3>'
          '<p>Většinu kalhot perte na 30 až 40 °C bez aviváže. Impregnaci outdoorových a lyžařských kalhot po čase obnovte speciálním přípravkem, jinak přestanou odpuzovat vodu.</p>',
    faq=[('Jaké kalhoty na turistiku?', 'Lehké rychleschnoucí outdoorové kalhoty z polyamidu s elastanem. Na chladnější dny softshell, na deštivé trasy přibalte nepromokavé kalhoty.'),
         ('Jaký je rozdíl mezi softshellem a membránou?', 'Softshell chrání před větrem a lehkým deštěm a je pružný. Membrána je vodotěsná, ale hůř větrá, takže je lepší na silný déšť a sníh.'),
         ('Jak vybrat velikost sportovních kalhot?', 'Změřte pas a délku nohavic a porovnejte s tabulkou výrobce. Střihy se liší, proto se řiďte rozměry, ne jen písmenem.'),
         ('Jak obnovit impregnaci kalhot?', 'Po vyprání naneste impregnační sprej nebo přípravek do pračky podle návodu. Impregnace na outdoorových kalhotách časem slábne.'),
         ('Jsou tepláky sportovní kalhoty?', 'Ano, ale jsou určené hlavně pro pohodlí a lehčí trénink. Na výkon nebo outdoor je lepší funkční materiál.'),
         ('Jaké kalhoty na zimní sporty?', 'Zateplené lyžařské kalhoty s membránou a sněhovou manžetou, případně softshellové na lehčí aktivity. Pod ně termoprádlo.')],
)

NEW['sportovni-kratasy'] = dict(
    title='Sportovní kraťasy – porovnání cen v e-shopech | Sporteka',
    desc='Sportovní kraťasy pánské a dámské na běh, fitness i volný čas. Porovnejte ceny a velikosti skladem v českých obchodech.',
    intro='<p><strong>Sportovní kraťasy</strong> se nosí na běh, do posilovny, na fotbal i na každý den. Běžecké jsou lehké a mají vnitřní slipy, fitness kraťasy bývají pevnější a volnější, '
          'basketbalové delší a prostornější. Dobré kraťasy neomezují pohyb, nešmouhají a nedřou.</p>'
          '<p>Ve Sportece uvidíte ceny kraťasů z českých obchodů a skladové velikosti. Vybírat můžete podle značky, velikosti a ceny. Pokud potřebujete kompletní outfit, podívejte se i na <a href="/sportovni-tricka/">trička</a> '
          'nebo <a href="/sportovni-obleceni/">sportovní oblečení</a> celkově, dámské varianty najdete mezi <a href="/leginy/">legínami</a>.</p>',
    guide='<h2>Jak vybrat sportovní kraťasy</h2>'
          '<p>Kraťasy vybírejte podle aktivity: běh má jiné nároky než posilování nebo míčové sporty. Společné je, že by neměly omezovat pohyb a měly rychle schnout.</p>'
          '<h3>Typy</h3>'
          '<ul><li><strong>Běžecké kraťasy:</strong> velmi lehké, často s vnitřními slipy, boční rozparky a kapsa na klíče nebo gel.</li>'
          '<li><strong>Fitness a trénink:</strong> pevnější a pružnější materiál, vyšší pas, někdy 2v1 s přiléhavými kraťasy uvnitř.</li>'
          '<li><strong>Míčové sporty:</strong> delší a volnější, například basketbalové nebo fotbalové, často z lesklého polyesteru.</li>'
          '<li><strong>Volný čas:</strong> bavlněné nebo směsové kraťasy, bez vnitřních slipů, s kapsami.</li></ul>'
          '<h3>Materiál a délka</h3>'
          '<p>Polyester rychle schne a odvádí pot, elastan přidává pružnost. Bavlna je příjemná, ale při potu těžkne. Krátké kraťasy (nad kolena) se hodí na rychlý běh, delší na fitness a míčové sporty. '
          'Zkrácená délka chrání před otlaky a poskytuje větší volnost.</p>'
          '<h3>Střih a velikost</h3>'
          '<p>Kraťasy musí držet v pase bez škrcení, nesmí se roztáčet a nohavice se nemají zvedat při kroku. Zkoušejte je v pohybu: dřep, výpad. U dámských modelů je důležité, aby pas nerolloval a nohavice nepodjížděly. '
          'Velikost vybírejte podle pasu a boků, ne jen podle písmene.</p>'
          + T(['Aktivita', 'Vhodné kraťasy'], [['Rychlý běh', 'lehké, krátké, s vnitřními slipy'], ['Posilovna', 'pružné, vyšší pas, 2v1'], ['Fotbal, basketbal', 'delší, volnější, rychleschnoucí'], ['Volný čas', 'bavlněné směsi, kapsy']]) +
          '<h3>Praní</h3>'
          '<p>Perte na 30 až 40 °C bez aviváže, aby si látka zachovala schopnost odvádět pot. Sušte volně. Tenký materiál se může při tření o zip zadrhnout, proto zip zapněte nebo perte v pytlíku.</p>',
    faq=[('Jaké kraťasy na běhání?', 'Lehké s vnitřními slipy, rychleschnoucí, s kapsou na klíče nebo gel. Důležité je, aby nedřely a nesjížděly.'),
         ('Co jsou kraťasy 2v1?', 'Dvě vrstvy v jednom: volný vnější kraťas a přiléhavý vnitřní. Hodí se na fitness a na běh, protože zabraňují otěru.'),
         ('Jak vybrat velikost kraťasů?', 'Změřte pas a boky a porovnejte s tabulkou výrobce. Zkuste dřep a výpad, abyste viděli, jestli nesjíždějí.'),
         ('Mohu v bavlněných kraťasech sportovat?', 'Na lehké cvičení ano, na intenzivní sport ne. Bavlna nasákne potem, těžkne a dře.'),
         ('Jak prát sportovní kraťasy?', 'Na 30 až 40 °C bez aviváže, aby si materiál zachoval odvod potu. Sušte volně.'),
         ('Jaká délka kraťasů je nejlepší?', 'Záleží na sportu. Na rychlý běh krátké, na fitness a míčové sporty delší pro větší pohodlí a volnost pohybu.')],
)

NEW['sportovni-tricka'] = dict(
    title='Sportovní trička – porovnání cen funkčních triček | Sporteka',
    desc='Sportovní a funkční trička pánská i dámská na běh, fitness a turistiku. Porovnejte ceny a velikosti skladem u českých e-shopů.',
    intro='<p><strong>Sportovní trička</strong> odvádějí pot od těla, rychle schnou a při pohybu nedřou. Nejčastěji se šijí z polyesteru, někdy z merina, a hodí se na běh, fitness i turistiku. '
          'Bavlněná trička jsou příjemná na každý den, ale na sport se příliš nehodí. Podle střihu najdete krátký a dlouhý rukáv i <a href="/tilka/">tílka</a> a <a href="/polokosile/">polokošile</a>.</p>'
          '<p>Na Sportece porovnáte ceny triček z českých obchodů a uvidíte, které velikosti jsou skladem. Hledáte-li funkční materiál, otevřete <a href="/funkcni-tricka/">funkční trička</a>. Teplejší varianty najdete mezi <a href="/termopradlo/">termoprádlem</a>.</p>',
    guide='<h2>Jak vybrat sportovní tričko</h2>'
          '<p>Tričko vybírejte podle sportu, počasí a intenzity. Na běh v létě potřebujete lehký prodyšný materiál, na turistiku s batohem plochý šev, který neotlačuje, a v zimě tričko jako spodní vrstvu.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Polyester:</strong> schne za pár minut a nenasákne potem. Nejčastější volba pro sportovní trička.</li>'
          '<li><strong>Merino:</strong> přírodní vlna, která méně zapáchá a hřeje i vlhká, hodí se na vícedenní túry. Je dražší a hůře snáší praní.</li>'
          '<li><strong>Směsi:</strong> kombinují komfort bavlny s odvodem potu polyesteru, vhodné na lehčí trénink.</li>'
          '<li><strong>Bavlna:</strong> příjemná v klidu, ale při potu nasákne a těžkne.</li></ul>'
          '<h3>Střih a švy</h3>'
          '<p>Přiléhavý střih při sportu nešmouhá a lépe odvádí pot, volnější je pohodlnější na každý den. U běhu a turistiky hledejte ploché nebo bezešvé spoje, aby neotíraly pod popruhy batohu. '
          'Reflexní prvky se hodí při běhu za šera a UV ochrana na vysokohorskou turistiku.</p>'
          '<h3>Velikost</h3>'
          '<p>Porovnejte tabulku výrobce s měrami hrudníku a délky. Sportovní střih bývá přiléhavější, než jste zvyklí z civilních triček. Dámské modely mají užší střih a jiné prostřihy. '
          'Pokud se vám zdá, že váháte mezi dvěma velikostmi, na sport volte spíš menší.</p>'
          + T(['Sport', 'Doporučené tričko'], [['Běh v létě', 'lehký polyester, krátký rukáv'], ['Fitness', 'přiléhavý střih, rychlé schnutí'], ['Turistika', 'rychleschnoucí nebo merino, plochý šev'], ['Zima', 'dlouhý rukáv jako spodní vrstva']]) +
          '<h3>Péče a pach</h3>'
          '<p>Funkční trička perte na 30 až 40 °C bez aviváže, která zalepuje vlákna a zhoršuje odvod potu. Pokud tričko drží pach, zkuste namáčení s octem nebo speciální prací prostředek na sportovní textil. Sušte volně, ne na topení.</p>',
    faq=[('Z čeho má být sportovní tričko?', 'Na sport z polyesteru, který rychle schne a odvádí pot. Na dlouhé túry se hodí i merino. Bavlna je pro volný čas.'),
         ('Jak odstranit pach z funkčního trička?', 'Namočte tričko do roztoku vody s octem nebo použijte prací prostředek na sportovní textil. Perte bez aviváže.'),
         ('Jaký je rozdíl mezi funkčním a bavlněným tričkem?', 'Funkční tričko odvádí pot a rychle schne. Bavlněné nasákne potem a zůstává vlhké, takže se hodí hlavně na každodenní nošení.'),
         ('Jak vybrat velikost sportovního trička?', 'Změřte hrudník a porovnejte s tabulkou výrobce. Sportovní střih bývá přiléhavý, při váhání vyberte menší.'),
         ('Je merino tričko lepší než polyester?', 'Merino méně zapáchá a hřeje i vlhké, ale je dražší a citlivější na praní. Polyester rychleji schne a je odolnější.'),
         ('Proč neperu funkční trička s aviváží?', 'Aviváž zalepí vlákna a trička pak hůř odvádějí pot. Pachy se navíc drží déle.')],
)

NEW['teplaky'] = dict(
    title='Tepláky – porovnání cen pánských a dámských | Sporteka',
    desc='Tepláky pánské, dámské a dětské: bavlněné, zateplené, zúžené i baggy. Porovnejte ceny, slevy a velikosti skladem v českých obchodech.',
    intro='<p><strong>Tepláky</strong> jsou pohodlné kalhoty na trénink, výlety i každý den. Najdete klasické zúžené s manžetou, volné baggy a širší straight střihy, bavlněné, směsové i funkční, zateplené na chladné dny. '
          'Jde o jednu z nejčastěji kupovaných částí <a href="/sportovni-kalhoty/">sportovních kalhot</a>.</p>'
          '<p>Na Sportece najdete tepláky z českých obchodů s porovnáním ceny a velikostí skladem. Vybírat můžete podle značky, střihu a ceny. K teplákům se hodí <a href="/mikiny/">mikina</a> '
          'nebo kompletní <a href="/soupravy/">souprava</a>.</p>',
    guide='<h2>Jak vybrat tepláky</h2>'
          '<p>Tepláky vybírejte podle toho, kdy je budete nosit. Na cvičení se hodí pružné a lehké, na doma a do města volnější a měkké, na zimu zateplené.</p>'
          '<h3>Střih</h3>'
          '<ul><li><strong>Zúžené (tapered, jogger):</strong> s manžetou na kotníku, moderní a vhodné ke sportovním botám i na sport.</li>'
          '<li><strong>Rovné (straight):</strong> bez manžety, univerzální, do města i na doma.</li>'
          '<li><strong>Baggy a široké:</strong> volné, módní, pohodlné, ale při sportu mohou překážet.</li>'
          '<li><strong>Přiléhavé a elastické:</strong> pro trénink a běh, často se zipem u kotníku.</li></ul>'
          '<h3>Materiál</h3>'
          '<p>Bavlněné tepláky jsou měkké a příjemné, ale po praní se mohou srazit a při pocení těžknou. Směs bavlny a polyesteru drží tvar a rychleji schne. Funkční polyester odvádí pot a hodí se na trénink. '
          'Zateplené mají uvnitř huňatou vrstvu, fleece nebo froté, a hřejí v chladu. Lehčí plátno nebo tenká pletenina se hodí na léto.</p>'
          '<h3>Pas, kapsy a detaily</h3>'
          '<p>Pružný pas se šňůrkou umožní upravit velikost, vnitřní podšívka drží tvar. Kapsy na zip uloží klíče a telefon a nevypadnou při běhu. Manžety na kotnících drží kalhoty na místě a chrání před chladem. '
          'Zesílená kolena a zadní díl ocení děti i ti, kdo často klečí nebo sedí na zemi.</p>'
          '<h3>Velikost</h3>'
          '<p>Porovnejte tabulku výrobce: obvod pasu a délku vnitřního švu. U volných střihů se vyplatí věnovat pozornost rozkroku a délce, aby se nohavice nepodlézaly pod boty. '
          'Tepláky z bavlny kupujte s malou rezervou, srazí se.</p>'
          + T(['Využití', 'Vhodné tepláky'], [['Trénink a běh', 'pružné, lehké, zúžené, zip u kotníku'], ['Doma a do města', 'rovné nebo baggy z bavlněné směsi'], ['Zima', 'zateplené, s fleecem nebo froté uvnitř'], ['Děti', 'odolnější kolena, pružný pas']]) +
          '<h3>Praní</h3>'
          '<p>Perte na 30 až 40 °C naruby, bez aviváže u funkčních, aby si zachovaly odvod potu. Zateplený vnitřek se nesmí žehlit. Sušte volně, ne na topení.</p>',
    faq=[('Jaké tepláky na sport?', 'Pružné a lehké z polyesteru nebo směsi, s elastickým pasem a ideálně zipem u kotníku. Na zimu zateplené.'),
         ('Jaký střih tepláků zvolit?', 'Zúžený (jogger) se hodí ke sportovním botám a na trénink, rovný je univerzální a baggy volný na každý den.'),
         ('Srazí se bavlněné tepláky?', 'Mohou se při prvním praní mírně srazit, proto je perte na 30 až 40 °C a sušte volně. U bavlny počítejte s malou rezervou.'),
         ('Jak prát tepláky?', 'Naruby na 30 až 40 °C. U funkčních nepoužívejte aviváž. Sušte volně, ne na topení.'),
         ('Jaké tepláky na zimu?', 'Zateplené s fleecem nebo froté uvnitř, případně s manžetou, která drží teplo. Na běh v chladu volte tenčí termo variantu.'),
         ('Jak vybrat velikost tepláků?', 'Podle obvodu pasu a délky vnitřního švu z tabulky výrobce. U volných střihů hlídejte délku, aby se nohavice nepodlézaly pod boty.')],
)

NEW['plavky'] = dict(
    title='Plavky – porovnání cen dámské, pánské, dětské | Sporteka',
    desc='Plavky dámské, pánské a dětské na bazén i k moři: jednodílné, dvoudílné, boxerky, slipy. Porovnejte ceny a velikosti skladem v českých obchodech.',
    intro='<p><strong>Plavky</strong> se liší podle toho, kde je používáte. Sportovní plavky na bazén jsou pevnější a odolné proti chloru, plážové jsou měkčí a bohatěji vzorované. '
          'Najdete <a href="/damske-plavky/">dámské plavky</a> jednodílné i dvoudílné, <a href="/panske-plavky/">pánské plavky</a> jako slipy, boxerky a šortky a <a href="/detske-plavky/">dětské plavky</a> včetně UV oblečení.</p>'
          '<p>Na Sportece porovnáte ceny plavek z českých obchodů a uvidíte, které velikosti jsou skladem. Vybírat můžete podle značky, velikosti a ceny. Doplnit je můžete o <a href="/plavecke-bryle/">plavecké brýle</a> '
          'nebo čepici a osušku z kategorie <a href="/plazove-doplnky/">plážové doplňky</a>.</p>',
    guide='<h2>Jak vybrat plavky</h2>'
          '<p>Plavky vybírejte podle toho, jestli budete plavat, nebo se opalovat. Pro pravidelné plavání potřebujete střih, který drží při pohybu a materiál odolný chlóru, na dovolenou stačí pohodlné plážové.</p>'
          '<h3>Plavky na bazén a k moři</h3>'
          '<ul><li><strong>Bazénové:</strong> z polyesteru nebo materiálů odolných chlóru, přiléhavý střih, často bez vypodložení. Vydrží víc plavání.</li>'
          '<li><strong>Plážové:</strong> měkký pružný materiál s elastanem, vzory a vyztužení nebo výplně. V chlóru a na slunci ale rychleji ztrácejí barvu.</li>'
          '<li><strong>Triatlonové a závodní:</strong> těsné, hydrodynamické, rychleschnoucí.</li></ul>'
          '<h3>Dámské plavky</h3>'
          '<p>Jednodílné plavky drží lépe při plavání a jsou praktické pro bazén. Dvoudílné se hodí na opalování a pláž, sportovní verze mají širší ramínka a pevný spodní díl. '
          'Vyztužené košíčky nebo vyjímatelné vložky ocení větší poprsí, ramínka nastavitelná nebo zkřížená na zádech zvyšují jistotu při pohybu. Vysoký pas zdůrazní pas, nižší střih méně ukazuje boky; důležité je hlavně, aby plavka seděla a netlačila.</p>'
          '<h3>Pánské plavky</h3>'
          '<p>Slipy a jammery (těsné delší) jsou vhodné pro závodní plavání, boxerky jsou kompromis a šortky na pláž. V řadě bazénů jsou volné šortky nepovolené, ověřte si pravidla před návštěvou. '
          'Rychle schnoucí podšívka zvyšuje komfort.</p>'
          '<h3>Dětské plavky</h3>'
          '<p>U dětí se vyplatí UV oblečení s dlouhým rukávem a UV faktorem, které chrání na slunci lépe než krém. Plavky kupujte přiléhavé, aby se při hře nenadouvaly, a s malou rezervou kvůli růstu.</p>'
          '<h3>Velikost</h3>'
          '<p>Plavky zkoušejte nejlépe na čistém spodním prádle nebo si v e-shopu ověřte možnost vrácení hygienicky zabalených kusů. Velikost určete podle obvodu hrudníku, pasu a boků a tabulky výrobce. '
          'Správná plavka sedí těsně, ale nikde netlačí a při pohybu nesjíždí.</p>'
          + T(['Využití', 'Vhodné plavky'], [['Pravidelné plavání', 'chlorovzdorné, přiléhavé, jednodílné nebo sportovní'], ['Pláž a opalování', 'plážové, dvoudílné, rychleschnoucí'], ['Děti', 'UV oblečení, přiléhavý střih'], ['Závody', 'těsné hydrodynamické plavky']]) +
          '<h3>Praní a péče</h3>'
          '<p>Po koupání plavky opláchněte ve sladké vodě, aby chlór a mořská sůl nepoškodily vlákna. Perte ručně nebo v pračce na 30 °C bez aviváže, nesušte na slunci a topení, elastan se rozvolní a barva vyběle. '
          'Vytlačit vodu stačí zabalením do ručníku.</p>',
    faq=[('Jaké plavky na plavání?', 'Sportovní plavky z materiálu odolného chlóru, přiléhavé, jednodílné nebo závodní střih. Plážové modely při častém plavání rychleji stárnou.'),
         ('Jak prát plavky?', 'Po koupání je opláchněte sladkou vodou, perte ručně nebo na 30 °C bez aviváže a sušte ve stínu. Nežehlete a nesušte na topení.'),
         ('Jak vybrat plavky podle postavy?', 'Vysoký pas zdůrazní pas, jednodílné plavky s vyztužením drží při pohybu, nastavitelná ramínka pomáhají s větším poprsím. Důležité je, aby plavka nikde netlačila.'),
         ('Jaké pánské plavky do bazénu?', 'Slipy, jammery nebo těsné boxerky. V řadě bazénů jsou volné šortky nepovolené, ověřte si pravidla.'),
         ('Jak vybrat velikost plavek?', 'Podle obvodu hrudníku, pasu a boků z tabulky výrobce. Plavky mají sedět těsně a při pohybu nesjíždět.'),
         ('Co jsou UV plavky pro děti?', 'Plavky nebo trička s UV faktorem, které chrání pokožku před sluncem. Na slunci jsou pohodlnější než opakované mazání krémem.')],
)
