"""sporteka.cz — brand texts wave 204: under-armour, regatta, celio, merrell.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ under-armour
NEW['under-armour'] = dict(
    title='Under Armour: trička, kraťasy, boty a mikiny ve srovnání',
    desc='Under Armour v katalogu Sporteky: trička, kraťasy, mikiny, legíny, tenisky a běžecké boty. Jak vybrat střih, velikost a kdy sledovat slevy.',
    intro='<p>Sortiment značky Under Armour v katalogu Sporteky stojí na tréninkovém oblečení. Největší skupinu tvoří <a href="/sportovni-tricka/">trička a tílka</a>, hned za nimi jdou tenisky, trailové boty, <a href="/sportovni-kratasy/">kraťasy</a> a mikiny. Zboží je určené převážně mužům, ale dámská a dětská část je také rozsáhlá, a to včetně legín, kalhot a čepic. '
          'V názvech produktů se opakují zkratky jako HG, UA nebo Armour Comp, podle kterých poznáte přiléhavé a volnější střihy. Tato stránka vysvětluje, jak v takové nabídce vybírat: čím se liší přiléhavé tričko od volného, kdy sáhnout po fleecové mikině, jak zvolit velikost a na co si dát pozor při koupi obuvi. Sporteka sama nic neprodává, jen porovnává nabídky obchodů a ukazuje, kde je právě vaše velikost skladem, takže se hned vidí i rozdíl v dopravě a v podmínkách vrácení.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Under Armour je v nabídce hlavně textilní značka s tréninkovým zaměřením. Převažují kousky určené na posilovnu, běh, fotbal a běžné nošení po sportu. Obuv tu je také, ale slouží spíše jako doplněk k oblečení: volnočasové tenisky, trailové a silniční běžecké boty a několik sandálů či pantoflí na šatnu. Přehled hlavních kategorií, ve kterých značku najdete, ukazuje tabulka.</p>'
          + T(['Kategorie', 'Typický kousek', 'Pro koho se nejčastěji hodí'], [
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'přiléhavé tričko s krátkým rukávem, tílko, tričko s logem', 'trénink, běh, každodenní nošení'],
              ['<a href="/funkcni-tricka/">Funkční trička</a>', 'tričko z lehké syntetiky odvádějící pot', 'vytrvalostní sporty, léto'],
              ['<a href="/sportovni-kratasy/">Kraťasy</a>', 'tréninkové šortky a lehké tkané kraťasy', 'posilovna, běh, fotbal, léto'],
              ['<a href="/mikiny/">Mikiny</a> a <a href="/fleecove-mikiny/">fleecové mikiny</a>', 'mikina na zip, mikina přes hlavu, fleece', 'rozcvička, chladnější dny, volný čas'],
              ['<a href="/teplaky/">Tepláky</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>', 'zúžené tepláky, tkané kalhoty', 'cesta na trénink, regenerace'],
              ['<a href="/leginy/">Legíny</a>', 'dlouhé a tříčtvrteční legíny', 'ženy i muži pod kraťasy, běh, fitness'],
              ['<a href="/cepice-a-celenky/">Čepice a kšiltovky</a>', 'kšiltovka, čelenka, zimní čepice', 'běh, každodenní nošení'],
              ['<a href="/tenisky/">Tenisky</a>, <a href="/trailove-boty/">trailové</a> a <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>', 'městské tenisky a běžecká obuv', 'běh a běžný provoz']]) +
          '<p>Z toho plyne praktická rada: pokud hledáte kompletní tréninkový outfit od jedné značky, najdete tu tričko, kraťasy, mikinu i čepici, a barevně k sobě ladí. Pokud potřebujete specializovanou obuv na horský terén nebo maraton, srovnejte nabídku s <a href="/znacka/salomon/">Salomonem</a>, <a href="/znacka/asics/">Asicsem</a> nebo <a href="/znacka/hoka/">Hokou</a>, které se na boty soustředí víc.</p>'
          '<h2>Pro koho je zboží určené</h2>'
          '<p>Největší část nabídky míří na muže, dámské oblečení je ale také silně zastoupené a dětská nabídka zahrnuje trička, kraťasy a tepláky. Unisex kousky jsou nejčastěji čepice, ponožky a doplňky. Při vyhledávání proto použijte filtr na pohlaví, jinak se vám smíchají střihy, které sedí úplně jinak. Dámské legíny a podprsenky mají jiný průběh švů než pánské komprese a dětské velikosti se často označují podle věku nebo výšky, ne podle písmen.</p>'
          '<p>Za zmínku stojí také barvy. Zdaleka nejčastější je černá, s velkým odstupem následují bílá, šedá a modrá. Chcete-li kousek, který se kombinuje s čímkoli, je černá bezpečná volba. Výraznější barvy jako zelená, růžová nebo červená bývají v sortimentu zastoupeny méně, takže se vyplatí sledovat dostupnost velikostí.</p>'
          '<h2>Přiléhavé a volné střihy: jak je rozeznat</h2>'
          '<p>Značka je známá tím, že nabízí vedle volnějších triček i těsně přiléhavé kompresní střihy. V názvech produktů poznáte kompresní řadu podle zkratky HG nebo slov jako Armour Comp, volnější denní a tréninkové kousky nesou označení jako Tech, Sportstyle či Left Chest. Rozdíl pocítíte hlavně při pohybu: komprese drží tělo, nemotá se a nevlaje, ale je znát na hrudi a pažích. Volný střih dýchá a nevadí, když se oblečení nepohodlně drží na těle.</p>'
          + T(['Typ střihu', 'Jak poznat v názvu', 'Kdy se hodí', 'Na co si dát pozor'], [
              ['Přiléhavý, kompresní', 'HG, Armour Comp, Legging', 'trénink s vysokou intenzitou, vrstvení pod mikinu', 'zvolte přesnou velikost, ne o číslo víc'],
              ['Střední, sportovní', 'Tech, Tech Graphic', 'běh, fitness, každodenní nošení', 'kontrolujte délku rukávu'],
              ['Volný, volnočasový', 'Sportstyle, Left Chest, Wordmark', 'město, kancelář bez sakáčku, cestování', 'bývá méně technický, ale pohodlný'],
              ['Tkané kraťasy a kalhoty', 'Woven, Wdmk', 'chladné rozcvičení, volný čas', 'zvolte podle pasu, ne podle trička']]) +
          '<p>Chcete-li si ověřit, jak tyto střihy vypadají na konkrétních kategoriích, projděte si <a href="/under-armour-leginy/">legíny Under Armour</a> a <a href="/sportovni-podprsenka-under-armour/">sportovní podprsenky Under Armour</a>, kde se kompresní střih projevuje nejvíc.</p>'
          '<h2>Trička a funkční vrstva</h2>'
          '<p>Trička jsou v tomto sortimentu nejpočetnější, takže výběr vyžaduje systém. Nejprve rozhodněte, zda jde o tréninkové tričko, nebo o volnočasové. Tréninkové z umělých vláken odvádí pot od kůže, rychle schne a nepřijímá pach tak snadno jako bavlna. Volnočasová verze s potiskem se hodí spíš do města. Oba typy najdete v kategoriích <a href="/sportovni-tricka/">trička a tílka</a> a <a href="/funkcni-tricka/">funkční trička</a>; liší se hlavně tím, že druhá skupina je výslovně označená jako technická.</p>'
          '<ul><li><strong>Délka:</strong> kompresní trička bývají delší, aby zůstala zasunutá při předklonu.</li>'
          '<li><strong>Rukáv:</strong> krátký se nosí v létě, dlouhý jako druhá vrstva pod mikinu.</li>'
          '<li><strong>Krk:</strong> kulatý výstřih je univerzální, výstřih do V se vyplatí pod košili nebo při vrstvení.</li>'
          '<li><strong>Švy:</strong> ploché švy omezují otěr při dlouhém pohybu, ale u kraťasů záleží na vnitřním prádle víc.</li></ul>'
          '<p>Při praní nepoužívejte aviváž, protože zalepí vlákna a zhoršuje odvod potu. Pere se obvykle při nižší teplotě a nejlépe naruby; potisky tak vydrží déle. Přesný postup je vždy na štítku konkrétního kousku.</p>'
          '<h2>Kraťasy, tepláky a legíny</h2>'
          '<p>V kategorii <a href="/sportovni-kratasy/">kraťasů</a> najdete lehké tkané šortky a pružnější tréninkové modely. Tkané jsou volnější, rychle schnou a hodí se k běhu i k posilovně, kde nepřekáží. Elastické s vnitřním pasem se lépe drží při skocích a sprintu. Pozor na délku nohavice: kolem kolen jsou bermudy, nad koleny klasické tréninkové kraťasy. Pokud chcete krátkou nohavici a pevnou oporu, hledejte vnitřní spodní vrstvu.</p>'
          '<p>Tepláky se dělí podle zúžení nohavic. Úzké se zakončením u kotníku se nehodí na běh ve větru a dobře vypadají s teniskami, kdežto rovné nohavice dávají víc prostoru pro prkenné svaly. Legíny pak slouží ženám jako základ tréninku, ale muži je používají pod kraťasy při chladnějším počasí. Při výběru legín se zaměřte na pas: široký pás drží při dřepech a nesjíždí, úzký může stahovat. V nabídce navíc najdete označení High Rise u kalhot, což znamená vyšší pas.</p>'
          '<h2>Mikiny a fleece: vrstva na chladnější dny</h2>'
          '<p>Mikiny a <a href="/fleecove-mikiny/">fleecové mikiny</a> zaujímají významný podíl sortimentu. Klasická mikina s kapucí se hodí na rozcvičení a do města, fleece je lehčí a hřeje při menší váze, ale neposkytuje ochranu před větrem. Pro větší ochranu zvolte softshell nebo bundu a mikinu používejte jako střední vrstvu. Na zip se mikina snáze snímá při zahřátí, přes hlavu drží lépe teplo.</p>'
          '<h2>Obuv a velikosti</h2>'
          '<p>Z obuvi převažují <a href="/tenisky/">tenisky a volnočasové boty</a> a překvapivě početné jsou <a href="/trailove-boty/">trailové běžecké boty</a>; silniční běžecké boty a sandály tvoří menší část. Pro běh po asfaltu zvolte <a href="/silnicni-bezecke-boty/">silniční modely</a> s tlumením, na lesní cesty a kamenitý podklad trail s výraznějším vzorkem podešve. Podrobnější průvodce srovnává <a href="/bezecke-boty-under-armour/">běžecké boty Under Armour</a> a rovněž <a href="/kopacky-under-armour/">kopačky Under Armour</a>.</p>'
          '<p>Velikosti se v online obchodech liší podle trhu. Americké označení bývá číselně jiné než evropské, proto vždy porovnejte údaj v centimetrech vnitřní stélky s délkou vlastního chodidla. Oblečení označené S, M, L nebo XL se řídí mezinárodním systémem, ale přiléhavý střih sedí jinak než volný, takže stejná velikost může působit odlišně. U tričkového střihu s kompresí volte svou obvyklou velikost, u volného zvažte o stupeň menší, pokud nechcete volně plandající tvar.</p>'
          '<h2>Jak vybírat mezi konkurenty</h2>'
          '<p>Under Armour soupeří hlavně s <a href="/znacka/nike/">Nike</a>, <a href="/znacka/adidas/">Adidasem</a> a <a href="/znacka/puma/">Pumou</a>. Hlavní rozdíl je v poměru: u Under Armour dominuje tréninkové oblečení a menší část nabídky tvoří obuv, u velkých konkurentů je obuv a lifestylový sortiment rozsáhlejší. Pokud hledáte kompresní a přiléhavý střih na posilovnu, patří Under Armour do užšího výběru. Pokud chcete nejširší výběr fotbalové a basketbalové obuvi, porovnejte značky vedle sebe.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Perte oblečení naruby a bez aviváže, aby potisky a technická vlákna vydržely.</li>'
          '<li>Sušte na vzduchu nebo při nízké teplotě; vysoké teplo poškozuje elastická vlákna.</li>'
          '<li>Boty po tréninku vyndejte ze stélky a nechte oschnout při pokojové teplotě, ne na topení.</li>'
          '<li>Střídejte dva páry běžecké obuvi, každý má čas se zregenerovat.</li>'
          '<li>Komprese s ztrátou pružnosti vyměňte, přestane plnit svůj účel.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Sezónní zboží se zlevňuje na konci sezóny: letní trička a kraťasy na podzim, mikiny a fleece na jaře. Dobrým signálem jsou menší množství velikostí u starších barev. Základní černé a šedé kousky se zlevňují méně často, ale bývají dostupné ve větším výběru velikostí. Sporteka porovnává nabídky obchodů, takže uvidíte, kdo má stejný model levněji, a můžete si sledovat vývoj ceny. Jen pozor na rozdíl mezi opravdovou slevou a nižším prodejem starší kolekce, kde chybí rozměry.</p>'
          '<p>Pro srovnání s dalšími tréninkovými značkami použijte stránky <a href="/znacka/nike/">Nike</a> a <a href="/znacka/puma/">Puma</a>. Pokud hledáte jen konkrétní kategorii bez ohledu na značku, projděte <a href="/leginy/">legíny</a> a <a href="/teplaky/">tepláky</a>.</p>',
    faq=[
        ('Co Under Armour v katalogu Sporteky nejčastěji nabízí?',
         'Nejčastější jsou trička a tílka, kraťasy, mikiny, fleecové mikiny a tepláky, k tomu tenisky a trailové běžecké boty. Značka se v katalogu prezentuje jako tréninková, takže obuv je doplněk k oblečení.'),
        ('Čemu odpovídá označení HG nebo Armour Comp v názvu?',
         'Podle názvů produktů jde o řadu přiléhavého, kompresního střihu. Takové tričko nebo legíny drží u těla, proto volte přesnou velikost a nehledejte volné pohodlí.'),
        ('Jak vybrat velikost trička Under Armour?',
         'U přiléhavé řady vezměte svou obvyklou velikost, u volné nebo volnočasové zvažte o stupeň menší, pokud nechcete volný tvar. Před koupí vždy porovnejte tabulku velikostí konkrétního obchodu.'),
        ('Je Under Armour vhodné i pro ženy a děti?',
         'Ano, v katalogu je velká dámská část včetně legín, kalhot a triček a menší dětská nabídka. Použijte filtr podle pohlaví, protože střihy se liší.'),
        ('Jsou boty Under Armour vhodné do terénu?',
         'V nabídce jsou trailové běžecké boty, které mají agresivnější podešev pro lesní cesty a kamení. Na asfalt zvolte silniční modely s tlumením.'),
        ('Jak prát funkční trička, aby vydržela?',
         'Perte je naruby na nižší teplotu, bez aviváže a bez sušení v horkém vzduchu. Aviváž zalepí vlákna a zhorší odvod potu, teplo poškodí elastické materiály.'),
        ('Čím se Under Armour liší od Nike nebo Adidasu?',
         'V katalogu převažuje tréninkové oblečení a kompresní střihy, zatímco velké konkurenční značky mají širší obuv a lifestylovou nabídku. Obě skupiny stojí za porovnání.'),
        ('Kdy se vyplatí čekat na slevu?',
         'Nejlépe na konci sezóny: letní kousky na podzim, mikiny a fleece na jaře. Základní černé modely se zlevňují méně, ale bývají skladem ve více velikostech.'),
        ('Prodává Sporteka zboží Under Armour přímo?',
         'Ne, Sporteka nic neprodává. Porovnává nabídky obchodů a po kliknutí vás přesměruje na stránku prodejce, kde dokončíte objednávku.'),
    ])

# ------------------------------------------------------------------ regatta
NEW['regatta'] = dict(
    title='Regatta: outdoorové bundy, kalhoty a boty ve srovnání',
    desc='Regatta v katalogu Sporteky: jarní, zimní a nepromokavé bundy, softshell, fleece, kalhoty a trekové boty. Jak vybrat vrstvy a kdy hledat slevy.',
    intro='<p>Regatta je v katalogu Sporteky outdoorová značka, kde zdaleka vedou bundy. Největší skupinu tvoří <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, následují <a href="/zimni-bundy/">zimní a péřové</a>, <a href="/nepromokave-bundy/">nepromokavé</a> a <a href="/softshellove-bundy/">softshellové</a> modely. K nim přibývají fleecové mikiny, outdoorové kalhoty a trekové boty včetně dětských. '
          'Názvy modelů jako Clumber, Dalent, Pack It nebo Highton ukazují, že značka staví na funkčních kouscích na výlety, procházky a běžný provoz v chladnějším počasí. Průvodce níže popisuje, jak z takové nabídky poskládat celý outdoorový outfit od jedné značky, jak rozeznat nepromokavou bundu od odolné proti větru, co od kalhot a bot čekat a jak hledat slevy. Sporteka sama nic neprodává, jen ukazuje, kde je vaše velikost a jaké jsou podmínky vrácení.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Regatta pokrývá hlavně vrchní vrstvy a obuv pro pohyb venku. Přehled kategorií ukazuje, jak se sortiment skládá, a hodí se jako mapa pro rychlou orientaci.</p>'
          + T(['Kategorie', 'Co v ní najdete', 'Kdy se hodí'], [
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehké bundy, hybridní a prošívané modely', 'přechodná období, běžná chůze'],
              ['<a href="/zimni-bundy/">Zimní a péřové bundy</a>', 'zateplené a prošívané bundy s kapucí', 'mráz, město i krátké výlety'],
              ['<a href="/nepromokave-bundy/">Nepromokavé bundy</a>', 'pláštěnkové a membránové modely, skládací bundy', 'déšť, výlet, cestování'],
              ['<a href="/softshellove-bundy/">Softshellové bundy</a>', 'pružné bundy odolné větru', 'aktivní pohyb za svěžího počasí'],
              ['<a href="/fleecove-mikiny/">Fleecové mikiny</a>', 'mikiny na zip, lehké vrstvy', 'střední vrstva pod bundu'],
              ['<a href="/outdoorove-kalhoty/">Outdoorové kalhoty</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>', 'turistické kalhoty, odolné a lehké', 'túry, procházky'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'nízké a polovysoké boty, dětské modely', 'túry, každodenní nošení venku'],
              ['<a href="/sportovni-vesty/">Vesty</a>, <a href="/sportovni-tricka/">trička</a>, <a href="/sportovni-kratasy/">kraťasy</a>', 'doplňkové vrstvy a letní oblečení', 'léto, vrstvení']]) +
          '<p>Takto vidět sortiment je užitečné: Regatta je volba pro člověka, který chce během jednoho nákupu vybavit celý outdoorový outfit od vrchní vrstvy po boty. Pro specializované horolezecké nebo extrémní vybavení srovnejte nabídku také s <a href="/znacka/the-north-face/">The North Face</a> nebo <a href="/znacka/columbia/">Columbií</a>.</p>'
          '<h2>Pro koho je zboží určené</h2>'
          '<p>Pánská nabídka je mírně větší, ale dámská část je téměř stejně široká a dětská zahrnuje nepromokavé bundy, kalhoty a turistické boty. Dětské oblečení do deště a na výlety je tu důležitou skupinou, protože děti rostou a potřebují často měnit velikosti. Při výběru dětské bundy volte vždy o číslo větší a rukávy lze zahnout. Unisex kousky jsou vzácnější, takže pohlavní filtr se vyplatí.</p>'
          '<p>Barevně nabízí značka víc než černou: spolu s ní se hojně objevuje modrá, zelená, šedá a hnědá, a také béžová a růžová. Díky tomu lze snadno sladit bundu s kalhotami, ale u dětského oblečení se vyplatí zvolit výraznou barvu, která je viditelná v mlze a lese.</p>'
          '<h2>Jak číst názvy bund</h2>'
          '<p>V popisech se opakují stejná slova a mají praktický význam. Zde je malý slovníček, který pomáhá rozlišit, co která bunda skutečně zvládne.</p>'
          + T(['Slovo v názvu', 'Co obvykle znamená', 'Na co si dát pozor'], [
              ['Nepromokavá', 'zvenčí odpuzuje vodu, často s kapucí', 'dlouhý déšť vyžaduje utěsněné švy a regulovatelnou kapuci'],
              ['Zateplená, prošívaná', 'výplň drží teplo', 'je objemnější, na chůzi do kopce se může přehřívat'],
              ['Hybridní', 'kombinace materiálů na trupu a rukávech', 'hodí se na střídavé počasí a pohyb'],
              ['Softshell', 'pružný materiál odolný větru a lehké vlhkosti', 'není určen na vytrvalý liják'],
              ['Pack It', 'skládací model, který lze sbalit do malého rozměru', 'ideální do batohu jako záložní vrstva'],
              ['Fleece', 'měkká a lehká izolační vrstva', 'neutralizuje chlad, ale nezastaví vítr']]) +
          '<p>Důležité je si uvědomit, že nepromokavá bunda a zateplená bunda se doplňují. Bunda proti dešti poskytuje vnější štít, zatímco izolační vrstva uvnitř hřeje. Pokud máte jen jednu bundu, bývá nejpraktičtější hybridní nebo softshell na jaro a podzim.</p>'
          '<h2>Vrstvení: jak poskládat outfit</h2>'
          '<ol><li><strong>Spodní vrstva:</strong> tričko nebo termoprádlo, které odvádí vlhkost od kůže. Pro chladné dny zvolte dlouhý rukáv.</li>'
          '<li><strong>Střední vrstva:</strong> <a href="/fleecove-mikiny/">fleecová mikina</a> nebo vesta. Hřeje a dýchá, takže při chůzi neudělá z těla sauna.</li>'
          '<li><strong>Vnější vrstva:</strong> bunda podle počasí: <a href="/nepromokave-bundy/">nepromokavá</a> na déšť, <a href="/softshellove-bundy/">softshell</a> na vítr, <a href="/zimni-bundy/">zimní</a> na mráz.</li>'
          '<li><strong>Doplňky:</strong> <a href="/cepice-a-celenky/">čepice</a>, rukavice a dobré ponožky, které řeší většinu chladu.</li></ol>'
          '<p>Takovým systémem můžete vyrazit s jednou základní bundou a obměňovat podle počasí. V létě pak stačí jen lehká nepromokavá vrstva v batohu a tričko.</p>'
          '<h2>Kalhoty a obuv</h2>'
          '<p>Turistické kalhoty v nabídce mají často označení voděodolné nebo odolné a jejich velkou výhodou je pružnost při chůzi. Pro delší túry vyberte střih s pohodlným zdvihem a kapsami se zipem, pro město stačí volnější typ. Vyplatí se zkontrolovat, jestli nohavice nejde odepnout, takže se z kalhot dá vytvořit kraťasy, což oceníte na dlouhé trase s proměnlivým počasím.</p>'
          '<p>Z obuvi nabízí Regatta v kategorii <a href="/trekova-obuv/">trekových bot</a> nízké i vyšší modely včetně dětských nepromokavých. Nízká treková obuv se hodí na pohodlné cesty a každodenní chůzi, vyšší nad kotník lépe drží nohu v nerovném terénu a chrání před kamením. Pro náročné horské túry se zaměřte na pevnější podešev a pozorně zkontrolujte, jestli je bota prodyšná. Pokud hledáte specializovanější obuv, porovnejte ji s <a href="/znacka/merrell/">Merrell</a> nebo <a href="/znacka/hi-tec/">Hi-Tec</a>.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Oblečení používá mezinárodní velikosti od S do XXL a dětské podle výšky nebo věku. U bund počítejte s tím, že pod ně chcete vrstvu: pokud se chystáte nosit pod nimi fleece, volte svou obvyklou velikost, ne menší. U kalhot ověřte obvod pasu a délku nohavice, u dětských s rezervou na růst. Obuv se vždy porovnává s délkou chodidla a s ponožkami, ve kterých na túru půjdete. Ráno bývá noha menší než večer, takže zkoušejte spíše po odpoledni.</p>'
          '<h2>Jak se Regatta liší od konkurence</h2>'
          '<p>V katalogu je Regatta značkou, která nabízí rozsáhlý výběr bund pro každodenní outdoor, a to v širokém spektru typů od lehkých skládacích po zateplené. V porovnání s <a href="/znacka/salomon/">Salomonem</a> nebo Columbií je tu méně specializované horské obuvi, ale více celých sad oblečení. To z ní dělá vhodnou volbu pro rodiny, výletníky a každého, kdo potřebuje kvalitní vrstvy na běžné počasí a nechce se zabývat technickými detaily.</p>'
          '<h2>Výlety s dětmi a rodinný nákup</h2>'
          '<p>Rodiny s dětmi tvoří důležitou část zákazníků, kteří outdoorové oblečení kupují. Děti se při hře venku rychle zašpiní, zmoknou a vyrostou z věcí za jednu sezónu, proto se vyplatí hledat praktické kousky a nehonit se za módou. Nepromokavá bunda s kapucí a kalhoty, které snesou kolena v blátě, jsou základ. Pod ně patří fleecová mikina a v zimě zateplená vrstva. Boty vybírejte s rezervou, ale ne tak velkou, aby se noha v botě klouzala; při sestupu by prsty neměly narážet. Starší sourozenecké kousky se hodí do další zimy, pokud je materiál nepoškozený a zip funguje.</p>'
          '<h2>Každodenní nošení a cestování</h2>'
          '<p>Většina lidí outdoorové bundy nenosí jen na hory, ale hlavně na cestu do práce, venčení psa a na víkendové procházky. Pro takové použití není nutná nejextrémnější výbava; důležité je pohodlí, kapsy na zip a kapuce, která se nevlní ve větru. Skládací bundu uložíte do tašky a vytáhnete při první kapce. Při cestování letadlem se hodí zateplená vesta, kterou přes den nosíte na sobě a v letadle ji zmačkáte jako polštář. Barvu volte podle toho, zda chcete bundu k večernímu oblečení, nebo k hrubšímu venkovnímu použití.</p>'
          '<h2>Na co se zeptat před koupí</h2>'
          '<ul><li>Je bunda určena pro déšť, nebo jen pro vítr? Odpověď najdete v popisu materiálu.</li>'
          '<li>Má kapuce stahování a kšilt, který chrání obličej?</li>'
          '<li>Jsou kapsy na zip a dost hluboké pro rukavice a telefon?</li>'
          '<li>Lze rukávy upravit na zápěstí, aby dovnitř netekla voda?</li>'
          '<li>Pro jakou vrstvu pod bundou je střih počítán, tenkou, nebo silný fleece?</li></ul>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Nepromokavé bundy perte speciálním prostředkem, ne běžným práškem; zanechává usazeniny, které narušují odpuzování vody.</li>'
          '<li>Zip a suchý zip před praním zavřete, aby nepoškodily látku.</li>'
          '<li>Softshell a fleece sušte při nízké teplotě nebo na vzduchu.</li>'
          '<li>Boty po túře vyčistěte kartáčem, vyndejte stélky a nechte oschnout mimo zdroj tepla.</li>'
          '<li>Zateplené bundy skladujte volně a nestlačené, výplň si tak zachová objem.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní bundy se zlevňují po vánočním období a na jaře, jarní a nepromokavé bundy na konci léta. Další příležitost jsou starší barvy a velikosti, které obchod chce uvolnit. Při srovnání berte v úvahu, zda sleva platí na všechny velikosti, nebo jen na krajní. Sporteka ukazuje obchody vedle sebe, takže poznáte, kdo má stejný model za příznivých podmínek a kdo nabízí rychlejší dopravu.</p>'
          '<p>Chcete-li srovnat konkurenci, otevřete stránky <a href="/znacka/columbia/">Columbia</a>, <a href="/znacka/the-north-face/">The North Face</a> nebo <a href="/znacka/hannah/">Hannah</a>.</p>',
    faq=[
        ('Co Regatta v katalogu Sporteky nabízí nejvíc?',
         'Nejvíc jsou zastoupeny jarní a podzimní bundy, následují zimní, nepromokavé a softshellové bundy, fleecové mikiny, kalhoty a trekové boty.'),
        ('Jak poznám bundu, která opravdu vydrží déšť?',
         'Hledejte v názvu slovo nepromokavá, kapuci a po čtení popisu zkontrolujte, zda jsou švy utěsněné. Softshell odolává větru a lehké vlhkosti, ale na vytrvalý liják nestačí.'),
        ('K čemu je skládací bunda typu Pack It?',
         'Je to záložní vrstva, která se sbalí do malého rozměru a vejde se do batohu. Hodí se na výlet, na cestu i jako pojistka před náhlým deštěm.'),
        ('Jaká velikost bundy je správná, když nosím pod ní fleece?',
         'Zvolte svou obvyklou velikost, ne menší, aby zůstal prostor pro střední vrstvu. Zkontrolujte délku rukávů a pohyblivost v ramenou při zvednutých pažích.'),
        ('Je Regatta vhodná i pro děti?',
         'Ano, v katalogu najdete dětské nepromokavé bundy, kalhoty a turistické boty. U dětí volte o číslo větší, rukávy a nohavice lze podehnout.'),
        ('Čím se zateplená bunda liší od softshellu?',
         'Zateplená má výplň, která hřeje i při stání, softshell je tenčí, pružný a chrání hlavně před větrem. Softshell se lépe hodí na pohyb, zateplená na mráz.'),
        ('Jak pečovat o nepromokavé oblečení?',
         'Perte je speciálním prostředkem, ne běžným práškem, a nepoužívejte aviváž. Zip zavřete a sušte při nízké teplotě, aby se zachovala impregnace.'),
        ('Jak vybrat trekové boty Regatta?',
         'Nízké boty se hodí na pohodlné cesty a běžné nošení, polovysoké nad kotník do nerovného terénu. Vždy zkoušejte s ponožkami, ve kterých půjdete, a odpoledne.'),
        ('Kdy čekat na slevy u zimních bund?',
         'Nejčastěji po vánočním období a na jaře. Sledujte rozsah velikostí, protože u slevy zůstávají často jen krajní rozměry.'),
    ])

# ------------------------------------------------------------------ celio
NEW['celio'] = dict(
    title='Celio: pánské kalhoty, košile a bermudy ve srovnání obchodů',
    desc='Celio v katalogu Sporteky: pánské kalhoty, košile, bermudy, trička, bundy a mikiny. Jak vybrat střih a velikost a kdy hledat slevy mezi obchody.',
    intro='<p>Celio je v katalogu Sporteky téměř výhradně pánská značka. Největší část nabídky tvoří <a href="/sportovni-kalhoty/">kalhoty</a>, hned za nimi jsou <a href="/kosile/">košile</a>, <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, <a href="/sportovni-tricka/">trička</a> a <a href="/mikiny/">mikiny</a>. K nim se řadí bermudy, polokošile, ponožky a čepice. '
          'Názvy modelů jako Todaniel, Pomur, Cosmart nebo Bochino naznačují, že jde o městskou a volnočasovou módu pro muže, ne o technické horské vybavení. Stránka vysvětluje, jak vybrat kalhoty podle střihu a velikosti, jak sladit barvy, kdy zvolit bermudy a jak přistupovat k péči a slevám. Sporteka sama nic neprodává, jen porovnává obchody a ukazuje, kde je vaše velikost skladem, což je u kalhot s dvojí velikostí zvlášť užitečné.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Celio patří k volnočasovým značkám, které se na Sportece objevují díky sportovnějšímu stylu a pohodlnému střihu. Převážně jde o oblečení pro každý den, do práce s uvolněným dress codem a na cestování. Tabulka ukazuje hlavní kategorie a jejich využití.</p>'
          + T(['Kategorie', 'Typický kousek', 'Kdy se hodí'], [
              ['<a href="/sportovni-kalhoty/">Kalhoty</a>', 'chinos, volnočasové a lehké kalhoty v mnoha barvách', 'práce, město, cestování'],
              ['<a href="/kosile/">Košile</a>', 'lehké košile s dlouhým i krátkým rukávem', 'léto, kancelář, večer'],
              ['<a href="/polokosile/">Polokošile</a>', 'polokošile s límečkem', 'teplé dny, uvolněný dress code'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'bavlněná trička, jednobarevná i potištěná', 'každodenní nošení'],
              ['<a href="/sportovni-kratasy/">Kraťasy</a> a bermudy', 'bermudy v letních barvách', 'léto, dovolená'],
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehké bundy, někdy s kapucí', 'přechodná období'],
              ['<a href="/mikiny/">Mikiny</a> a <a href="/teplaky/">tepláky</a>', 'mikiny a pohodlné kalhoty', 'doma, cesta, volný čas'],
              ['<a href="/zimni-bundy/">Zimní bundy</a>, <a href="/sportovni-vesty/">vesty</a>', 'zateplené bundy a vesty', 'chladné dny']]) +
          '<p>Z přehledu je zřejmé, že Celio je vhodné pro muže, kteří hledají kombinace do běžného života, nikoli sportovní trénink. Pokud potřebujete tréninkové kousky, projděte raději <a href="/znacka/nike/">Nike</a> nebo <a href="/znacka/adidas/">Adidas</a>.</p>'
          '<h2>Pro koho je zboží určené</h2>'
          '<p>Značka v katalogu cílí prakticky na muže. Dámských, unisex a dětských položek je jen zanedbatelný počet, takže filtr podle pohlaví nemá velký význam. Pokud hledáte dámský nebo dětský sortiment, zvolte jiné značky z přehledu, například <a href="/znacka/regatta/">Regatta</a> nebo <a href="/znacka/under-armour/">Under Armour</a>. U Celia se soustřeďte na rozlišení střihů a barev.</p>'
          '<p>Barvy jsou tu typicky světlé a přírodní. Nejvíc je bílé, hned za ní černá, modrá a šedá, k tomu zelená, hnědá a béžová. Světlé odstíny kalhot a bermud patří do jarního a letního šatníku, tmavší jsou praktičtější na podzim a zimu. Vzhledem k tomu, že mnoho kousků nese v názvu barvu jako světle modrá, světle zelená nebo khaki, snadno poskládáte letní outfit.</p>'
          '<h2>Jak vybrat kalhoty</h2>'
          '<p>Kalhoty jsou největší kategorie, proto zde vyplatí systém. První otázka zní, na co je budete nosit. Do kanceláře s uvolněným stylem se hodí střih podobný chinos, na víkend pohodlnější a volnější, na cesty pružný materiál s příměsí elastanu.</p>'
          + T(['Typ kalhot', 'Jak poznat', 'Vhodné pro', 'Poznámka'], [
              ['Úzký střih', 'popis slim nebo zúžené', 'štíhlejší postavu, městský styl', 'zkontrolujte pohodlí v sedě'],
              ['Rovný střih', 'popis regular či straight', 'většinu postav', 'univerzální volba'],
              ['Volnočasové s pasem do gumy', 'pas s kšandou či gumou', 'cestování, pohodlí', 'méně formální vzhled'],
              ['Lehké letní', 'světlé barvy, tenký materiál', 'léto, dovolená', 'může prosvítat u bílé']]) +
          '<p>V nabídce se u některých kalhot objevuje v názvu číselné označení velikosti, například hodnota se čtyřmi číslicemi, a u jiných jen písmena. Proto před nákupem vždy otevřete tabulku velikostí konkrétního obchodu a porovnejte obvod pasu a délku nohavice se svým oblíbeným kouskem. Nejjistější je změřit stávající pohodlné kalhoty vleže na stole.</p>'
          '<h2>Bermudy a kraťasy</h2>'
          '<p>V kategorii <a href="/sportovni-kratasy/">kraťasů</a> se u Celia objevují hlavně bermudy v pastelových a přírodních barvách. Je to volnočasová alternativa ke kalhotám, která se hodí na dovolenou, na zahradu i do města. Délka sahá obvykle k okraji kolene. Při výběru zkontrolujte pas: gumový s tkanicí je pohodlný, klasický s knoflíkem vypadá upraveněji. Kapsy by měly být hluboké, aby z nich nevypadl telefon při sezení.</p>'
          '<h2>Košile a polokošile</h2>'
          '<p>Druhou největší skupinou jsou <a href="/kosile/">košile</a>. V kategorii jsou pod názvem turistické a outdoorové košile, ale u Celia jde převážně o běžné volnočasové modely. Lehká bavlněná nebo lněná košile s krátkým rukávem je ideální na léto, s dlouhým rukávem ji lze nosit rozepnutou přes tričko. Při výběru sledujte materiál: bavlna dobře dýchá, ale mačká se, příměs syntetiky zlepší tvarovou stálost. Polokošile s límečkem se nosí mezi trikem a košilí a dobře sedí k bermudám i k chinos.</p>'
          '<h2>Bundy, mikiny a vesty</h2>'
          '<p>V chladnějším období nabízí značka lehké <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, mikiny a menší počet <a href="/zimni-bundy/">zimních bund</a>. Jsou určené spíše pro městské použití než pro vysokohorský pohyb, takže při plánu delší túry zvolte technické oblečení jiné značky. Mikiny se hodí jako střední vrstva, vesta ocení ten, komu se při pohybu přehřívají paže. Pokud se pohybujete mezi interiérem a ulicí, praktická je bunda s kapucí, kterou lze rychle stáhnout.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Velikosti oblečení se označují písmeny S až XXL a u kalhot v mnoha případech číselně. Francouzské a evropské značky mívají užší střih než americké, proto pokud se pohybujete mezi dvěma velikostmi, zvažte větší. U trička a košile sledujte šířku ramen, u kalhot obvod pasu a délku nohavice. Po vyprání bavlna mírně sbíhá, takže nechte malou rezervu.</p>'
          '<h2>Jak se Celio liší od sportovních značek</h2>'
          '<p>Na rozdíl od značek jako <a href="/znacka/adidas/">Adidas</a>, <a href="/znacka/puma/">Puma</a> nebo <a href="/znacka/regatta/">Regatta</a> nemá Celio v katalogu technický ani tréninkový profil. Jde o módnější a každodenní vrstvu: kalhoty, košile a bermudy k městskému životu. Pokud hledáte oblečení, které nevypadá jako sportovní výbava a přesto je pohodlné, stojí za porovnání.</p>'
          '<h2>Jak sestavit městský outfit</h2>'
          '<p>Základ šatníku tvoří dvoje kalhoty v neutrálních barvách, například béžové a tmavě modré, a k nim několik triček a jedna košile. Světlé kalhoty kombinujte s tmavším vrškem, tmavé s bílou nebo světle modrou košilí. Khaki a zelená tvoří přirozený pár s hnědou obuví a černá se hodí k čemukoli. Pokud nosíte mikinu, zvolte jednobarevnou a ladící s kalhotami. Příliš mnoho vzorů najednou působí nepřehledně, takže potisk nechte jen na jednom kousku. Takto poskládané kousky snadno obměníte podle ročního období a z několika položek vytvoříte desítky kombinací.</p>'
          '<h2>Do kanceláře s uvolněným dress codem</h2>'
          '<p>V prostředí, kde se nevyžaduje oblek, se dobře uplatní rovné kalhoty z jemnějšího materiálu, košile nebo polokošile a čisté tenisky. Důležitý je detail: vyžehlená košile a nepomačkané kalhoty vypadají upraveně i bez saka. Sportovní materiály s pružností umožňují sedět celý den bez nepohodlí, ale lesklé syntetické tkaniny se do kanceláře moc nehodí. Pokud po práci míříte rovnou na procházku nebo do restaurace, přidejte lehkou bundu nebo vestu. Mikinu si ponechte na domácí pohodlí, do prostředí s klienty se obvykle nehodí.</p>'
          '<h2>Dovolená a cestování</h2>'
          '<p>Lehké bermudy, bavlněné nebo lněné košile a několik triček tvoří základ cestovního kufru do teplých krajů. Světlé barvy odrážejí slunce, ale snadno se špiní, takže je vhodné vzít i tmavší kousky. Na večer přibalte tenčí bundu nebo mikinu, protože u moře či v horách se po západu slunce ochladí. Kalhoty s pružným materiálem se v kufru nemačkají a pohodlně se v nich cestuje několik hodin. Vyplatí se oblečení vybírat tak, aby se dalo kombinovat mezi sebou a stačilo méně kusů.</p>'
          '<h2>Na co se zeptat před koupí</h2>'
          '<ul><li>Jaké je složení materiálu a obsahuje elastan pro pohodlí v sedě?</li>'
          '<li>Jaký je střih, úzký, rovný, nebo volný, a odpovídá vašemu oblíbenému páru?</li>'
          '<li>Je barva ve skutečnosti stejná jako na fotografii, jak píší recenze?</li>'
          '<li>Lze zboží vrátit, pokud střih nesedí, a kdo platí zpáteční dopravu?</li></ul>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Světlé kalhoty perte zvlášť od tmavých, aby se nezašedily.</li>'
          '<li>Košile vyndejte z pračky hned po odstředění a pověste na ramínko, vyžehlení pak zabere méně času.</li>'
          '<li>Bavlněné kousky perte na doporučenou teplotu, vysoká teplota je smrští.</li>'
          '<li>Bermudy a kalhoty vyklepejte z kapes, aby se nepoškodily švy.</li>'
          '<li>Světlé odstíny ošetřete skvrny co nejdříve, než zaschnou.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Letní kousky, tedy bermudy, košile s krátkým rukávem a trička, se zlevňují koncem srpna a v září. Jarní a podzimní bundy najdete levněji v zimě a na začátku jara. Základní jednobarevné kalhoty bývají skladem celý rok, ale konkrétní kombinace velikosti dostupná jen v některých obchodech, takže stojí za to srovnávat. Sporteka umožňuje porovnat obchody vedle sebe a vidět, kde je vaše velikost a jaká je doprava.</p>'
          '<p>Další inspiraci najdete u značek <a href="/znacka/puma/">Puma</a> a <a href="/znacka/regatta/">Regatta</a> nebo v kategoriích <a href="/polokosile/">polokošile</a> a <a href="/teplaky/">tepláky</a>.</p>',
    faq=[
        ('Co Celio v katalogu Sporteky nabízí?',
         'Hlavně pánské kalhoty, košile, jarní a podzimní bundy, trička, mikiny, bermudy a polokošile. Jde o volnočasový a městský sortiment.'),
        ('Má Celio dámské nebo dětské oblečení?',
         'V katalogu je dámských, dětských i unisex položek jen malý počet. Značka je prakticky pánská, proto pro ženy a děti hledejte jiné značky.'),
        ('Jak poznat správnou velikost kalhot?',
         'Změřte stávající pohodlné kalhoty vleže a porovnejte obvod pasu a délku nohavice s tabulkou obchodu. U kalhot s číselnou velikostí v názvu vždy ověřte, co hodnoty znamenají.'),
        ('Hodí se kalhoty a košile Celio na túru?',
         'Ne, jde o městský a volnočasový sortiment. Na túry zvolte technické oblečení z outdoorových kategorií, například nepromokavé bundy nebo turistické kalhoty.'),
        ('Jaké barvy jsou v nabídce nejčastější?',
         'Nejvíc je bílé, černé, modré a šedé, doplňují je zelená, hnědá a béžová. Světlé odstíny se hodí na léto, tmavší na podzim a zimu.'),
        ('Jak vybrat bermudy?',
         'Zkontrolujte délku k okraji kolene, typ pasu a hloubku kapes. Gumový pas je pohodlný, klasický vypadá upraveněji.'),
        ('Mačkají se bavlněné košile víc než směsové?',
         'Ano, čistá bavlna a len se mačkají víc, ale lépe dýchají. Směs s umělým vláknem drží tvar a méně se mačká, ale hůře odvádí pot.'),
        ('Kdy se vyplatí čekat na slevu?',
         'Letní oblečení se zlevňuje koncem léta, jarní bundy v zimě. Základní kalhoty jsou skladem často celý rok, ale ne vždy ve všech velikostech.'),
        ('Prodává Sporteka oblečení Celio přímo?',
         'Ne, Sporteka porovnává nabídky obchodů a po kliknutí vás přesměruje k prodejci. Tam také dokončíte objednávku a řešíte vrácení.'),
    ])

# ------------------------------------------------------------------ merrell
NEW['merrell'] = dict(
    title='Merrell: trekové, trailové a barefoot boty ve srovnání',
    desc='Merrell v katalogu Sporteky: tenisky, trekové a trailové boty, barefoot, sandály a zimní obuv. Jak vybrat model, velikost a kdy sledovat slevy.',
    intro='<p>Merrell je v katalogu Sporteky obuvnická značka a skoro všechno, co pod ní najdete, jsou boty. Největší skupinu tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, hned za nimi jsou <a href="/trekova-obuv/">trekové boty</a>, <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> a <a href="/trailove-boty/">trailové běžecké boty</a>. Menší část tvoří silniční běžecká obuv, sandály, barefoot a zimní modely. '
          'V názvech modelů se opakují řady Moab, Speed Strike, Accentor, Vapor Glove nebo Agility Peak a označení WP a GTX, která ukazují na nepromokavou úpravu. Stránka vysvětluje, jak mezi nimi vybírat: podle terénu, podle výšky boty, podle vodotěsnosti, jak zkoušet velikost a jak o boty pečovat. Sporteka sama nic neprodává, jen porovnává obchody a ukazuje, kde je vaše číslo skladem.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Merrell je typická outdoorová a trailová značka, která v nabídce pokrývá celé spektrum pěší obuvi od lehkých teniskových modelů po vysoké boty na túry. Přehled kategorií usnadní orientaci.</p>'
          + T(['Kategorie', 'Typický model', 'Kdy se hodí'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'nízké boty a lehké outdoorové modely', 'město, výlety, každodenní chůze'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'nízké a polovysoké outdoorové boty', 'túry po cestách, delší chůze'],
              ['<a href="/vysoke-trekove-boty/">Vysoké trekové boty</a>', 'boty nad kotník', 'nerovný terén, těžší batoh'],
              ['<a href="/trailove-boty/">Trailové běžecké boty</a>', 'běžecké boty s výrazným vzorkem', 'běh v lese a horách'],
              ['<a href="/silnicni-bezecke-boty/">Silniční běžecké boty</a>', 'boty na asfalt a zpevněné cesty', 'běh ve městě'],
              ['<a href="/barefoot-obuv/">Barefoot boty</a>', 'ploché, ohebné modely (řada Glove)', 'přirozený došlap, krátké trasy'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'otevřená letní obuv', 'léto, voda, procházky'],
              ['<a href="/zimni-obuv/">Zimní boty</a>', 'zateplené modely Thermo', 'sníh a chlad']]) +
          '<p>Menší část nabídky tvoří <a href="/termopradlo/">funkční prádlo</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a vodní sporty, jako <a href="/kajaky-a-cluny/">kajaky a čluny</a>. Tyto kategorie jsou méně časté a stojí za samostatné prohlédnutí, pokud k botám hledáte doplňky.</p>'
          '<h2>Pro koho je zboží určené</h2>'
          '<p>Pánské boty převažují, dámských je ale také hodně a dětské tvoří jen malou část nabídky. Hledáte-li obuv pro dítě, najdete modelů málo, takže pro mladší děti srovnejte i jiné značky. U dospělých dává filtr smysl, protože dámské modely mají užší patu a nižší objem, zatímco pánské jsou širší. Velká skupina bot se prodává jako unisex v pánském rozsahu velikostí; ženy s větší nohou je mohou zvažovat, ale sedět musí v prstech i v patě.</p>'
          '<p>Barevně dominuje černá, následovaná hnědou, šedou, zelenou a béžovou. Zemité odstíny se hodí do terénu a nejsou náchylné na špínu. Chcete-li výraznější barvu pro lepší viditelnost, hledejte ji spíš u trailových modelů.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Značka používá v názvech zkratky a názvy řad. Jejich význam se opakuje, takže se vyplatí znát je při srovnání v obchodech.</p>'
          + T(['Označení', 'Co naznačuje', 'Na co se zaměřit'], [
              ['WP', 'vodotěsná úprava', 'pro déšť a mokrou trávu, méně prodyšná'],
              ['GTX', 'membrána Gore-Tex v modelu', 'vodotěsná a prodyšná, hodí se na celoroční použití'],
              ['Mid', 'polovysoká bota', 'chrání kotník, vhodná na nerovné cesty'],
              ['Ltr', 'kožený vrch', 'odolný, vyžaduje ošetření'],
              ['Thermo', 'zateplený model', 'zimní obuv, pozor na přehřátí na jaře'],
              ['Glove', 'barefoot řada', 'minimální podrážka, nutná adaptace'],
              ['Moab, Speed Strike, Accentor', 'řady turistických modelů', 'liší se tuhostí a prodyšností']]) +
          '<p>Pro srovnání těchto označení si otevřete jednotlivé kategorie; popis konkrétního obchodu vždy upřesní materiál a membránu.</p>'
          '<h2>Nízká, polovysoká, nebo vysoká bota</h2>'
          '<p>Nejčastější otázka u trekové obuvi zní, jak vysokou botu zvolit. Nízká bota je lehká, prodyšná a nabízí volný pohyb kotníku, takže se hodí na cesty, výlety a delší chůzi s lehkým batohem. Polovysoká drží kotník víc a chrání před kamením a vlhkou trávou. Vysoké modely z kategorie <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> se vyplatí při těžším zatížení a v náročném terénu. Rozhodněte se podle typu cest, ne podle módy.</p>'
          '<ul><li><strong>Zpevněné cesty a lesní stezky:</strong> nízká bota je dost, kotník netrpí.</li>'
          '<li><strong>Kameny, kořeny a mokrý podklad:</strong> polovysoká bota s lepší oporou.</li>'
          '<li><strong>Těžký batoh a dlouhé túry:</strong> vyšší a tužší model.</li>'
          '<li><strong>Zimní chůze:</strong> zateplená obuv se silnějším vzorkem podešve.</li></ul>'
          '<h2>Vodotěsnost: kdy ji potřebujete</h2>'
          '<p>Membrána drží vodu venku, ale zároveň zpomaluje odvod vlhkosti z nohy. V létě na suchých cestách je prodyšný model pohodlnější, vodotěsná bota se hodí na podzim, na jaře a do proměnlivého počasí. Nejdůležitější pravidlo: vodotěsná bota nepomůže, pokud se voda dostane přes horní okraj, takže při brodění stejně zmokne. Pro letní túry a běh volte nemembránové modely, pro celoroční nošení membránové.</p>'
          '<h2>Trailové a silniční běžecké boty</h2>'
          '<p>Z <a href="/trailove-boty/">trailových bot</a> je v nabídce značné množství. Mají výraznější vzorek podešve a pevnější špičku, aby chránily prsty před kameny. Na zpevněný asfalt je tento vzorek zbytečný a rychleji se obrušuje, takže pro běh ve městě zvolte <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>. Pokud často přecházíte z lesa na silnici, trailová bota s menším vzorkem je kompromis. O volbě běžecké obuvi podrobněji pojednává <a href="/trailove-boty/">stránka trailových bot</a>.</p>'
          '<h2>Barefoot obuv: pro koho a jak začít</h2>'
          '<p>Barefoot modely, které v názvech nesou slovo Glove, mají tenkou ohebnou podrážku a minimální převýšení paty. Dovolují noze pohybovat se přirozeněji, ale svaly chodidla a lýtka si na to musí zvyknout. Začněte krátkými trasami a postupně přidávejte vzdálenost. Barefoot obuv není vhodná na dlouhé túry s těžkým batohem, kde potřebujete tlumení. Podrobnější přehled najdete v kategorii <a href="/barefoot-obuv/">barefoot boty</a>.</p>'
          '<h2>Velikost a zkoušení</h2>'
          '<p>Boty zkoušejte odpoledne, kdy je noha největší, a v ponožkách, které na túru nosíte. Mezi špičkou a prsty by měla zůstat rezerva zhruba na šířku palce, aby prsty při sestupu nenarážely. Pata nesmí vyskakovat a boty nemají tlačit v nártu. Merrell má podle zkušeností kupujících spíše běžnou šířku; pokud máte široký nárt, zvažte modely s širší špičkou nebo barefoot řadu. Při koupi přes internet si vždy ověřte možnost výměny velikosti.</p>'
          '<h2>Jak se Merrell liší od konkurence</h2>'
          '<p>V katalogu je Merrell čistě obuvní značkou se silným zaměřením na pěší outdoor. Srovnání nabízí <a href="/znacka/salomon/">Salomon</a> s rychlejším, technickým stylem, <a href="/znacka/la-sportiva/">La Sportiva</a> s horským zaměřením a <a href="/znacka/regatta/">Regatta</a>, která staví víc na oblečení a cenově dostupnější obuvi. Pro rodiny a pohodlné túry je Merrell logická volba, pro technickou horolezeckou obuv hledejte jinde.</p>'
          '<h2>Výběr podle ročního období</h2>'
          '<p>Na jaře a na podzim jsou nejpraktičtější polovysoké vodotěsné modely, protože počasí se mění a podklad bývá mokrý. V létě dává smysl lehká prodyšná bota nebo sandál, v nichž se noha tolik nepřehřívá. V zimě potřebujete zateplenou obuv se silnějším vzorkem podešve a vyšším vrškem, aby sníh nenapadal dovnitř. Pro celoroční nošení zvolte univerzální polovysokou botu s membránou a v létě ji doplňte druhým, lehčím párem. Dvě sady bot vydrží déle než jedna, protože mají čas vyschnout.</p>'
          '<h2>Ponožky a stélky: malé věci, velký rozdíl</h2>'
          '<p>Dobrá bota ztratí půlku pohodlí, pokud se do ní obuje bavlněná ponožka. Bavlna nasákne potem, zůstane mokrá a způsobuje puchýře, proto na túru zvolte <a href="/sportovni-ponozky/">sportovní ponožky</a> z vlny nebo syntetiky. Na delší trasy se hodí vyšší ponožka, která chrání nad hranou boty. Také stélku můžete vyměnit za anatomickou, pokud máte vysoký nebo plochý nárt. Při zkoušení boty vždy použijte stejnou ponožku jako na túře, jinak vám velikost vyjde jinak. Rezervní pár ponožek do batohu zabere málo místa a v mokru udělá velký rozdíl.</p>'
          '<h2>Chůze s dětmi a pohodlná obuv na každý den</h2>'
          '<p>Mnoho kupujících hledá obuv, která se dá nosit celý den a vyrazit v ní i na krátký výlet. Lehká nízká treková bota nebo teniska z kategorie <a href="/tenisky/">tenisky a volnočasové boty</a> je takovým kompromisem. Dobře drží nohu, má protiskluzovou podešev a nevypadá příliš technicky. Pozor na příliš měkké podrážky, které se při dlouhé chůzi rychle ušlapou, a na úzké špičky, jež tlačí na prsty.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Po túře vyčistěte kartáčem, vyndejte stélky a nechte oschnout mimo topení.</li>'
          '<li>Kožený vrch ošetřete impregnací nebo vosky podle pokynů výrobce.</li>'
          '<li>Membránové boty perte jen jemně, bez agresivních prostředků, které narušují membránu.</li>'
          '<li>Střídejte páry, aby měla podešev čas se zregenerovat.</li>'
          '<li>Opotřebované vložky vyměňte, prodlouží to život boty.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní obuv se zlevňuje na jaře, letní a běžecké modely na podzim. Starší řady po uvedení nové generace, například nová verze téhož modelu, bývají levnější, i když se liší jen detaily. Pozor na velikosti: u slev bývají skladem krajní čísla. Sporteka porovnává obchody vedle sebe, takže uvidíte, kdo má vaši velikost a za jakých podmínek ji pošle či vymění.</p>'
          '<p>Pokud hledáte srovnání, otevřete <a href="/znacka/salomon/">Salomon</a> a <a href="/znacka/hi-tec/">Hi-Tec</a> nebo kategorii <a href="/tenisky/">tenisky</a> a <a href="/sandaly/">sandály</a>.</p>',
    faq=[
        ('Co Merrell v katalogu Sporteky nabízí?',
         'Hlavně obuv: tenisky, trekové a vysoké trekové boty, trailové a silniční běžecké boty, barefoot, sandály a zimní modely. Menší část tvoří funkční prádlo a ponožky.'),
        ('Co znamená WP nebo GTX v názvu boty?',
         'WP označuje vodotěsnou úpravu, GTX membránu Gore-Tex. Obě pomáhají proti vodě, ale zhoršují prodyšnost, takže se hodí hlavně na chladnější a vlhčí období.'),
        ('Jaký je rozdíl mezi nízkou a polovysokou trekovou botou?',
         'Nízká je lehčí a prodyšnější, polovysoká lépe drží kotník a chrání před kamením a vlhkem. Vysoké boty se vyplatí při těžším batohu a v náročném terénu.'),
        ('Je barefoot obuv Merrell vhodná na túry?',
         'Na krátké a lehké trasy ano, ale potřebuje adaptaci chodidla. Na dlouhé túry s těžkým batohem je lepší klasická treková bota s tlumením.'),
        ('Mám zvolit trailovou, nebo silniční běžeckou botu?',
         'Na lesní cesty a kamení trailovou s výrazným vzorkem, na asfalt silniční s tlumením. Trailový vzorek se na tvrdém povrchu rychle obrušuje.'),
        ('Jak vybrat správnou velikost?',
         'Zkoušejte odpoledne v ponožkách, které na túru nosíte, a nechte před špičkou rezervu zhruba na šířku palce. Pata nemá vyskakovat a nárt netlačit.'),
        ('Jsou boty Merrell i pro děti a ženy?',
         'Dámských modelů je v katalogu hodně, dětských jen málo. Dámské boty mají obvykle užší patu a nižší objem než pánské.'),
        ('Jak pečovat o vodotěsné boty?',
         'Po použití je vyčistěte, vyndejte stélky a nechte oschnout mimo zdroj tepla. Perte je jemně bez agresivních prostředků, aby se nepoškodila membrána.'),
        ('Kdy čekat na slevu na zimní nebo letní obuv?',
         'Zimní modely se zlevňují na jaře, letní a běžecké na podzim. U slev bývají skladem hlavně krajní velikosti.'),
    ])
