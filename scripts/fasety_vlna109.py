"""sporteka.cz — facet landing texts wave 109: adidas-bezecke-boty, termopradlo-panske, arena-plavky, decathlon-plavky.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ adidas-bezecke-boty
NEW['adidas-bezecke-boty'] = dict(
    title='Adidas běžecké boty: řady, střihy a výběr podle běhu',
    desc='Adidas běžecké boty od vstupních Duramo a Runfalcon po tlumené Supernova, lehké Adizero a trailové Terrex. Jak vybrat řadu, velikost a porovnat obchody.',
    intro='<p>Adidas patří k nejširším nabídkám v běžecké obuvi: od jednoduchých bot na první kilometry přes měkké modely na dlouhé pomalé běhy až po lehké tempové a trailové kousky. Právě šíře sortimentu je zároveň největší záludnost, protože názvy řad jako Duramo, Runfalcon, Supernova nebo Adizero napovídají určení jen tomu, kdo je zná. '
          'Tato stránka třídí boty značky z kategorie <a href="/bezecka-obuv/">běžecké boty</a> a vysvětluje, co která řada nabízí, jak se liší pánské, dámské a dětské provedení, kdy sáhnout po trailovém Terrexu a jak se Adidas srovná s konkurencí. Pokud víte, kde poběžíte, zúžíte výběr rovnou na <a href="/silnicni-bezecke-boty/">silniční</a> nebo <a href="/trailove-boty/">trailové boty</a>. Jiné značky najdete u <a href="/nike-bezecke-boty/">Nike</a>, <a href="/bezecke-boty-asics/">Asics</a> a <a href="/new-balance-bezecke-boty/">New Balance</a>.</p>',
    guide='<h2>Jak je sortiment Adidas v běžecké obuvi uspořádaný</h2>'
          '<p>Značka nemá jednu univerzální běžeckou botu, ale několik řad s jasně odlišným posláním. Stejný princip platí u většiny velkých výrobců, jen u Adidas je těch řad víc a jejich názvy se v nabídce obchodů opakují v mnoha barevných verzích. Nejpraktičtější je proto orientovat se podle jména řady a podle toho, k čemu bota slouží. Tabulka shrnuje řady, které se v nabídce objevují nejčastěji.</p>'
          + T(['Řada', 'Zaměření', 'Pro koho je'], [
              ['Duramo', 'vstupní tréninková bota, odolná a nenáročná', 'začátečníci a rekreační běžci s pár výběhy týdně'],
              ['Runfalcon', 'jednoduchá lehká bota pro běžný pohyb', 'první běžecké boty, škola, rekreační sport'],
              ['Galaxy', 'základní pohodlná bota na kratší vzdálenosti', 'občasný běh, svižná chůze, fitness'],
              ['Supernova', 'tlumený trenér na delší kilometry', 'pravidelní běžci, kterým záleží na komfortu'],
              ['Adistar', 'měkčí, výrazněji tlumená bota', 'delší pomalé běhy a vyšší běžci'],
              ['Adizero', 'lehčí, živější tempové a závodní modely', 'rychlé tréninky, závody, zkušenější běžci'],
              ['Ultraboost a Pureboost', 'měkký komfortní odraz s pěnou Boost', 'běh i každodenní nošení'],
              ['Terrex', 'outdoorová řada s přilnavou podrážkou', 'stezky, kopce a smíšený terén']]) +
          '<p>Dobrá zpráva je, že mezi řadami rozhoduje spíš styl běhání než úroveň. Člověk, který běhá dvakrát týdně po parku, nepotřebuje závodní Adizero a zbytečně by zaplatil za vlastnosti, které nevyužije. Opačně zkušený běžec s tempovými tréninky brzy zjistí, že vstupní Duramo mu nabídne méně živosti než lehký trenér. Začněte tím, kolik a jak rychle běháte, a teprve potom vybírejte barvu.</p>'
          '<h2>Vstupní řady: Duramo, Runfalcon a Galaxy</h2>'
          '<p>Tyto boty jsou nejčastější volbou prvního páru. Mají měkký, nenáročný svršek, rozumně tlumenou podrážku a konstrukci, která odpouští drobné chyby v technice. Hodí se na rovné cesty, do parku nebo na pásy ve fitku, kde ocení hlavně pohodlí. Neočekávejte od nich špičkovou odezvu ani nízkou hmotnost, ale pro první měsíce jsou rozumným základem. Pokud začnete běhat častěji a bota se vám zdá mdlá, je čas přejít na tlumenější nebo živější řadu. Právě u těchto modelů se často objevují i dětské a juniorské verze, kterým se věnuje další kapitola.</p>'
          '<h2>Tlumené tréninkové boty: Supernova a Adistar</h2>'
          '<p>Supernova je řada pro ty, kdo běhají pravidelně a chtějí botu, která zvládne většinu tréninků. Tlumení má střední až vyšší, rozměr podešve je stabilní a bota dobře drží tvar i po stovkách kilometrů. Adistar jde směrem měkčího a výrazněji tlumeného běhu, což oceníte po dlouhém pomalém běhu na tvrdém asfaltu. U obou řad se v nabídce setkáte s označením pánských i dámských modelů a také s variantami pro vyšší stabilitu nebo pohodlnější komfort. Nezapomeňte, že měkčí bota není automaticky lepší. Příliš velké propadání pěny může u někoho znamenat nejistý došlap, zatímco jiný se v ní cítí jako na oblaku. Rozhodne zkouška na vlastní noze.</p>'
          '<h2>Lehké a tempové boty: Adizero</h2>'
          '<p>Řada Adizero míří na rychlejší běh. Boty jsou lehčí, mají živější pěnu a často i pevnější konstrukci, která pomáhá odrazu. Vhodné jsou na intervaly, tempové úseky a závody od pěti kilometrů výš. Na každodenní pomalé běhání se používají hůř, protože mají menší tolerance k únavě chodidla a opotřebovávají se rychleji. Pro většinu amatérů je rozumnější mít jeden tlumený trenér na běžný trénink a Adizero si nechat na ty dny, kdy opravdu zrychlujete. Takto se obě boty střídají a každá vydrží déle.</p>'
          '<h2>Komfortní řady Ultraboost a Pureboost</h2>'
          '<p>Boty s označením Boost vznikly jako komfortní běžecké modely, ale časem se staly oblíbenou obuví na každodenní nošení. V běžecké kategorii se s nimi setkáte hlavně v tlumené a měkké podobě. Hodí se pro běžce, kteří upřednostňují pohodlí před nízkou hmotností, a také pro ty, kteří chtějí jednu botu na běh i na cesty do práce. Jejich nevýhodou bývá vyšší hmotnost a menší přímost kontaktu s podložím. Pokud hledáte hravý a svižný pocit, podívejte se spíše do řady Adizero.</p>'
          '<h2>Trailový Terrex a boty do terénu</h2>'
          '<p>Terrex je outdoorová divize Adidas a její běžecké modely jsou určeny pro stezky, lesní cesty a kopcovitý terén. Mají hrubší vzorek podrážky, pevnější špičku a svršek, který lépe snáší otěr o kámen a kořeny. U některých modelů se objevuje i membrána Gore-Tex, tedy nepromokavá vrstva, kterou ocení běžci v chladném a mokrém počasí. Pro suché léto je lepší bota bez membrány, protože je prodyšnější a rychleji schne. Na asfalt trailová bota nepatří, vzorek se rychle sjíždí a došlap je tvrdší. Více o výběru v terénu najdete v kategorii <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<h2>Velikosti a střih: na co dát pozor</h2>'
          '<p>Adidas používá evropské velikosti doplněné o britské a americké ekvivalenty a u většiny běžeckých modelů je poloviční velikost běžná. Při výběru se držte délky vložky v centimetrech, kterou prodejci obvykle uvádějí. Změřte si chodidlo odpoledne, kdy je největší, a přidejte asi centimetr rezervy pro prsty. Při běhu se noha prodlužuje a při dlouhém klesání se posouvá dopředu. Šířka je u značky většinou standardní, takže uživatelé s opravdu širokou nohou si musejí dávat pozor na úzký střih špičky, zejména u závodních modelů.</p>'
          '<ul><li><strong>Zkoušejte s běžeckou ponožkou</strong>, ne s tenkou bavlněnou.</li><li><strong>Zkontrolujte patu:</strong> nesmí se při došlapu zvedat ani odírat Achillovu šlachu.</li><li><strong>Prsty musejí mít prostor</strong> a nesmí narážet do špičky při sbíhání ze svahu.</li><li><strong>Při online nákupu</strong> si ověřte lhůtu pro vrácení a výměnu velikosti.</li></ul>'
          '<h2>Pánské, dámské a dětské běžecké boty</h2>'
          '<p>Dámské modely mají obvykle užší patu a o něco užší střih než pánské, často i měkčí tlumení vzhledem k nižší hmotnosti uživatelky. To ale neznamená, že je žena musí vždy volit. Pokud sedí pánská bota lépe, je správná. Dětské a juniorské modely, například z řady Runfalcon, se vyrábějí v menších velikostech s jednodušší konstrukcí a často suchým zipem nebo gumičkou místo tkaniček. U dětí se vyplatí kupovat botu s dostatečnou rezervou, ale ne větší než dvě čísla, aby noha neklouzala. Dětskému sortimentu se věnuje stránka <a href="/detske-bezecke-boty/">dětské běžecké boty</a> a ženský výběr najdete u <a href="/bezecke-boty-damske/">dámských běžeckých bot</a>.</p>'
          '<h2>Jak se Adidas srovnává s jinými značkami</h2>'
          '<p>Každý výrobce staví boty na vlastním kopytu, tedy na tvaru formy, a to je hlavní důvod, proč jedna značka sedí a jiná tlačí. Z toho plyne, že není objektivně nejlepší značka, ale jen ta, která sedí vaší noze. U značek jako ' + B(('nike', 'Nike'), ('asics', 'Asics'), ('new-balance', 'New Balance'), ('hoka', 'Hoka'), ('on', 'On'), ('mizuno', 'Mizuno')) + ' najdete obdobné rozdělení na vstupní, tréninkové a závodní modely, jen s jinými názvy a jinými proporcemi. Srovnávat se vyplatí hlavně podle typu boty, ne podle loga. Přehledy jednotlivých značek jsou na stránkách <a href="/nike-bezecke-boty/">Nike</a>, <a href="/bezecke-boty-hoka/">Hoka</a>, <a href="/salomon-bezecke-boty/">Salomon</a> a <a href="/mizuno-bezecke-boty/">Mizuno</a>.</p>'
          '<h2>Péče o boty a výměna po kilometrech</h2>'
          '<p>Běžecké boty se nepárují s pračkou. Po použití je vyndejte, vysušte při pokojové teplotě a nedávejte je na radiátor, protože horko poškozuje pěnu a lepené spoje. Zabláceně boty opláchněte vlažnou vodou a kartáčkem. Pěna v podešvi postupně ztrácí pružnost a po několika stovkách kilometrů je třeba bota vyměnit, i když svršek vypadá dobře. Pokud po běhu cítíte nové bolesti kolen nebo holení, je to častý signál, že tlumení dosloužilo. Střídání dvou párů boty prodlužuje životnost obou a dává pěně čas na zotavení.</p>',
    faq=[
        ('Jaká řada Adidas je nejlepší pro začátečníka?',
         'Pro první běžecké boty se nejčastěji vybírají vstupní řady Duramo nebo Runfalcon. Jsou pohodlné, odolné a nestojí tolik jako závodní modely. Až po několika měsících pravidelného běhání má smysl uvažovat o tlumenější řadě Supernova.'),
        ('Čím se liší Supernova od Adizero?',
         'Supernova je tlumený trenér na pravidelné kilometry a pomalejší tempo. Adizero je lehčí a živější a hodí se na rychlé tréninky nebo závody. Většina běžců má větší užitek z Supernovy a Adizero používá jen občas.'),
        ('Jsou boty Adidas větší, nebo menší než u jiných značek?',
         'Velikosti se mezi modely drobně liší, proto se spoléhejte na délku vložky v centimetrech, ne jen na číslo. Změřte chodidlo odpoledne a přidejte rezervu pro prsty. U úzkého střihu špičky může mít širší noha pocit těsnosti.'),
        ('Hodí se boty Terrex i na asfalt?',
         'Dají se použít krátce, například cestou na stezku, ale na delší běh po silnici nejsou ideální. Hrubý vzorek se rychle sjíždí a podrážka je tužší. Na asfalt je lepší silniční model s hladší podešví.'),
        ('Potřebuji botu s membránou Gore-Tex?',
         'Membrána pomáhá v dešti, bahně a chladu, kdy chrání před promáčením. V horku a při běhu v suchu naopak snižuje prodyšnost a nohy se v ní více potí. Pro většinu letního běhání je lepší lehká bota bez membrány.'),
        ('Mohou běžecké boty Ultraboost nahradit trailové?',
         'Ne, jsou určeny hlavně pro komfortní běh po zpevněném povrchu a každodenní nošení. Nemají přilnavou podrážku ani ochranu špičky, kterou potřebujete v kamenitém terénu. Pro lesní stezky vyberte trailový model.'),
        ('Kdy je potřeba měnit běžecké boty?',
         'Přesné číslo neexistuje, závisí na hmotnosti běžce, povrchu a typu pěny. Signálem je ztráta odrazu, nerovnoměrně sjetá podrážka nebo nové bolesti kloubů po běhu. Pokud běháte často, střídejte dva páry, vydrží déle.'),
        ('Jak vybrat dětské běžecké boty Adidas?',
         'Vybírejte lehkou botu s pevnou patou, ohebnou podrážkou a dostatečným prostorem na prsty. Dítě by mělo mít před špičkou asi centimetr rezervy. Při rychlém růstu kontrolujte velikost každé dva až tři měsíce.'),
        ('Je lepší koupit pánský, nebo dámský model?',
         'Rozhodne to tvar nohy, ne označení. Dámský model má obvykle užší patu a měkčí tlumení, pánský širší obrys. Zkuste obě verze a vyberte tu, ve které noha po stranách netlačí a pata drží.'),
        ('Jak prát běžecké boty Adidas?',
         'Do pračky je nedávejte, horká voda a odstřeďování poškozují pěnu i lepidlo. Stačí vlažná voda, jemný kartáček a sušení při pokojové teplotě. Vložku vyndejte a usušte zvlášť, aby se v botě nezdržoval zápach.'),
    ])

# ------------------------------------------------------------------ termopradlo-panske
NEW['termopradlo-panske'] = dict(
    title='Termoprádlo pánské: střih, vrstvení a výběr materiálu',
    desc='Pánské termoprádlo: trička, spodky a sety. Jak vybrat střih, tloušťku a materiál od syntetiky po merino pro běh, lyže, túry i každodenní zimu.',
    intro='<p>Pánské termoprádlo se liší od dámského a dětského hlavně střihem, který počítá se širšími rameny, delším trupem a nohavicemi sedícími na dlouhé nohy. Správně zvolené sedí těsně, ale nestahuje, nevytváří záhyby pod bundou a odvádí pot od kůže. Špatně zvolené, třeba příliš volné nebo ze špatného materiálu, může způsobit rychlejší ochlazení než žádné prádlo. '
          'Tato stránka třídí funkční spodní vrstvy pro muže z kategorie <a href="/termopradlo/">termoprádlo</a> a vysvětluje, jak vybrat tričko, spodky nebo celý set, jak se liší tloušťky, kdy sáhnout po merinu a čím se liší prádlo na běžky, sjezdovku nebo túru. Podobné výběry máte u <a href="/termopradlo-damske/">dámského</a> a <a href="/detske-termopradlo/">dětského termoprádla</a> a na stránce <a href="/lyzarske-termopradlo/">lyžařského prádla</a>.</p>',
    guide='<h2>Co je na pánském termoprádle jiné</h2>'
          '<p>Rozdíl mezi pánským a dámským termoprádlem není kosmetický. Pánské modely mají delší trup a rukávy, širší záda a prsní část, jednotný střih v pase a u spodků často praktický poklopec. Vyrábějí se v klasických velikostech S až XXL a u značek zaměřených na sport i v delších nebo užších variantách. Při nákupu je užitečné měřit obvod hrudníku, pasu a délku vnitřní strany nohy a porovnat je s tabulkou výrobce, protože každá značka počítá s jiným tvarem těla.</p>'
          + T(['Kus oblečení', 'Pánská specifika', 'Na co se zaměřit'], [
              ['Triko s dlouhým rukávem', 'delší trup, širší ramena', 'zakrývá bedra při předklonu na kole nebo lyžích'],
              ['Triko s krátkým rukávem', 'volnější proti pohybu paží', 'vhodné pod košili nebo do tepla'],
              ['Spodky dlouhé', 'delší nohavice a pas, často poklopec', 'nesmí se vrásnit pod kalhotami'],
              ['Boxerky a slipy', 'bezešvé nebo s plochými švy', 'užitečné pod funkční kalhoty'],
              ['Set (triko a spodky)', 'sladěná tloušťka a velikosti', 'jistota stejné kvality obou částí'],
              ['Rolák a zip', 'vyšší límec chrání krk', 'dobrý do mrazu a větru']]) +
          '<p>Většina mužů nakupuje termoprádlo jen podle velikosti trička, což je nejčastější chyba. Pas a délka nohavic mohou být jiné než u běžných kalhot, hlavně u vyšších postav. Nohavice, které končí nad kotníkem, pustí chlad pod ponožku a vytvoří studený pruh na kůži.</p>'
          '<h2>Syntetika, merino nebo směs</h2>'
          '<p>Základní materiálová rozhodnutí se u mužů neliší, ale praxe ano. Muži se obvykle více potí při stejné intenzitě pohybu a mají hustší ochlupení, které s drsnějším materiálem vytváří tření. Syntetické pleteniny z polyesteru nebo polypropylenu schnou rychle a přežijí časté praní, proto se hodí pro běh, kolo a běžky. Merino vlna je příjemnější při dlouhém nošení, nepáchne tak rychle a zahřeje i vlhká. Hodí se na túry, cestování nebo práci venku, kdy se prádlo nemění několik dní. Směsi spojují oba světy a bývají nejpraktičtějším kompromisem. Více o vlně najdete v kategorii <a href="/merino/">merino oblečení</a>.</p>'
          '<h2>Tloušťka a použití</h2>'
          '<p>Silnější prádlo není automaticky teplejší, protože záleží i na tom, jak se pohybujete. Při intenzivní činnosti vyrábí tělo teplo samo a příliš silná spodní vrstva způsobí přehřátí, pot a následné prochladnutí. Naopak při sedavé činnosti, jako je rybaření, pozorování zvěře nebo čekání na vleku, tělo teplo nevyrábí a silnější vrstva je nutná. Pro orientaci poslouží přehled aktivit.</p>'
          + T(['Aktivita', 'Vhodná tloušťka', 'Poznámka'], [
              ['Běh a kolo za chladna', 'tenká, těsná', 'důležitá je prodyšnost a rychlé schnutí'],
              ['Běžky', 'tenká až střední', 'při výstupu se hodně potíte'],
              ['Sjezdové lyžování', 'střední', 'dobře funguje s merinem nebo směsí'],
              ['Túra a skialp', 'střední, merino nebo směs', 'zvolte i náhradní triko'],
              ['Stání a čekání venku', 'silná', 'myslete na ponožky a čepici'],
              ['Každodenní zima', 'tenká až střední', 'pod oblek nebo džíny stačí lehká vrstva']]) +
          '<p>Pokud váháte, kupte spíš středně silnou verzi. Přehřátí lze řešit rozepnutím zipu nebo svlečením vrchní vrstvy, ale nedostatek izolace se za pochodu opravuje hůř. K běhu a běžkám se vyplatí mít samostatně tenčí kus.</p>'
          '<h2>Jak sedí a proč záleží na těsnosti</h2>'
          '<p>Termoprádlo musí těsně přiléhat k pokožce, jinak nemůže odvádět vlhkost. Prádlo s rezervou nasákne potem a chladí. Po obléknutí by nemělo nikde tahat, ani stlačovat. Při předklonu, zvednutí paží a dřepu zkontrolujte, zda se triko nevyhrne a spodky nesjíždějí. Bezešvé pleteniny jsou příjemné pro dlouhou aktivitu, ale vyžadují přesnou velikost, protože tvar neodpouští. Pro vyšší nebo širší postavy hledejte značky s větším rozsahem velikostí.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Najdete zde sportovní specialisty jako ' + B(('craft', 'Craft'), ('swix', 'Swix'), ('sensor', 'Sensor'), ('devold', 'Devold'), ('brubeck', 'Brubeck')) + ', outdoorové značky ' + B(('viking', 'Viking'), ('the-north-face', 'The North Face'), ('husky', 'Husky'), ('alpine-pro', 'Alpine Pro'), ('kilpi', 'Kilpi')) + ' i české a slovenské ' + B(('klimatex', 'Klimatex'), ('progress', 'Progress')) + '. Jednotlivé firmy se liší tím, jak tvoří střih, jaké pleteniny používají a pro jaký sport své prádlo primárně navrhují. Skandinávské značky obvykle sázejí na dobře padnoucí lehké prádlo pro běžecké lyžování a merino, kdežto outdoorové firmy staví na odolnosti a univerzálnosti. Rozdíly poznáte nejlépe podle popisu určení, ne podle loga.</p>'
          '<h2>Vrstvení: kde termoprádlo začíná</h2>'
          '<p>Termoprádlo je jen první vrstva. Druhou tvoří izolační prvek, třeba fleece nebo lehká péřová mikina, a třetí chrání před větrem a vlhkostí. U pánské garderoby se často přehlíží jednoduchý fakt: prádlo musí zasahovat do všech vrstev, ne jen pod bundu. Při větru a mrazu se vyplatí vrchní vrstva s vyšším límcem a rukávy, které přesahují zápěstí. Mezi další vrstvy zařaďte <a href="/funkcni-mikiny/">funkční mikiny</a> nebo lehká <a href="/funkcni-tricka/">funkční trička</a> pro teplejší dny.</p>'
          '<h2>Dlouhý rukáv, rolák, zip nebo krátký rukáv</h2>'
          '<p>Základní trička se liší výškou límce a délkou rukávu. Kulatý výstřih je nejuniverzálnější a nevadí pod košilí. Rolák nebo stojáček chrání krk před větrem a hodí se na běžky, jízdu na kole a stání na vleku. Zip u krku se hodí při změně intenzity, protože výstřih během stoupání rozepnete a na sjezdu zavřete. Krátký rukáv najde uplatnění při rychlé chůzi za mírného chladu nebo pod volnější košili a také v teplých interiérech. Volte podle toho, co potřebujete chránit a kde se budete nejčastěji pohybovat.</p>'
          '<h2>Typické chyby při nákupu</h2>'
          '<ul><li><strong>Příliš volná velikost:</strong> prádlo bez kontaktu s kůží neodvádí pot a chladí.</li><li><strong>Bavlna jako spodní vrstva:</strong> při pohybu nasákne a po zastavení chladí. Ponožky řešte zvlášť, například u <a href="/lyzarske-ponozky/">lyžařských ponožek</a>.</li><li><strong>Příliš tlusté prádlo na pohyb:</strong> vede k pocení a následnému prochladnutí.</li><li><strong>Aviváž při praní:</strong> ucpává vlákna a snižuje funkčnost.</li><li><strong>Špatná délka nohavic:</strong> u vysokých mužů vzniká odkrytý pruh nad kotníkem.</li></ul>'
          '<p>Většinu těchto chyb lze odstranit tím, že si prádlo před prvním použitím vyzkoušíte doma při pohybu. Dřep, předklon a zvednutí paží ukážou, kde prádlo tahá, vyhrnuje se nebo odhaluje kůži. Sezónní nákup naplánujte ještě před prvními mrazy, kdy je výběr velikostí i tlouštěk nejširší.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Funkční materiály nemají rády aviváž, protože ucpává vlákna a zhoršuje odvod vlhkosti. Perte je podle štítku, obvykle při nízké teplotě, a nesušte na radiátoru. Merino perte šetrným pracím prostředkem určeným pro vlnu. Syntetika někdy drží zápach, proto ji neponechávejte zmačkanou ve sportovní tašce několik dní. Pravidelným praním a vzdušným sušením prodloužíte životnost o celé sezony.</p>'
          '<h2>Spodky pro každý den a pro sport</h2>'
          '<p>Muži často řeší, jestli kupovat zvlášť spodky a zvlášť triko. Praktické je mít dvě základní vrstvy ve stejné tloušťce a barvě, ale doplnit je o tenčí kus na intenzivní pohyb. Pokud chodíte po městě, stačí jedna sada středně silného prádla pod běžné kalhoty. Pro sportovce se vyplatí tři kusy: tenké na rychlý pohyb, střední na univerzální použití a silné na dny, kdy stojíte nebo sedíte. Při cestování stačí dvě trička a jedny spodky z merina, protože se dají vyvětrat a večer vyprat v umyvadle.</p>',
    faq=[
        ('Jakou velikost termoprádla pro muže zvolit?',
         'Řiďte se tabulkou výrobce a vlastními mírami: obvod hrudníku, pasu a délka vnitřní strany nohy. Prádlo má přiléhat k tělu bez stahování. Pokud jste mezi velikostmi, u syntetiky zvolte menší, u silnějšího merina spíš větší.'),
        ('Je lepší merino, nebo syntetika?',
         'Merino lépe zahřeje, dlouho nepáchne a je příjemné na kůži, ale schne pomaleji a méně vydrží. Syntetika schne rychle a snese časté praní. Na intenzivní sport sáhněte po syntetice, na túry a cesty po merinu nebo směsi.'),
        ('Jak silné termoprádlo vybrat?',
         'Podle aktivity: tenké na běh a kolo, střední na lyže a túry a silné na sezení či stání venku. Pokud váháte, vezměte střední. Přehřátí lze snadno vyřešit rozepnutím nebo svlečením vrstvy.'),
        ('Musí být termoprádlo těsné?',
         'Ano, funguje jen tehdy, když se dotýká kůže a odvádí vlhkost dál. Volné prádlo nasákne potem a nepřenáší ho k další vrstvě. Při pohybu se ale nemá nikde zařezávat.'),
        ('Dá se nosit termoprádlo každý den ve městě?',
         'Ano, při chladném počasí je praktické jako spodní vrstva pod oblek nebo džíny. Stačí tenčí až střední tloušťka. V kancelářích a vytápěných prostorech se nevolí příliš silné modely, abyste se nepřehřívali.'),
        ('Vyplatí se kupovat set, nebo samostatné kusy?',
         'Set zaručuje stejnou kvalitu a tloušťku obou částí. Samostatné kusy se hodí, když potřebujete na horní polovinu jiný materiál nebo tloušťku než na nohy. Pro začátek je set jednodušší.'),
        ('Čím se liší termoprádlo na běžky a na sjezdovku?',
         'Prádlo na běžky je lehčí a prodyšnější, protože se při pohybu hodně zahřejete. Na sjezdovce se víc stojí na vleku a vyplatí se silnější a teplejší vrstva. Více u kategorie <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>.'),
        ('Proč mi termoprádlo páchne i po vyprání?',
         'Syntetická vlákna zachycují zápach, pokud se perou při příliš nízké teplotě nebo s aviváží. Zkuste jemný prací prostředek bez aviváže, delší máchání a sušení na vzduchu. U trvale zapáchajících kusů pomáhá přechod na merino.'),
        ('Je termoprádlo vhodné i pod pracovní oděv?',
         'Ano, na stavbě, v lese nebo při práci venku funguje jako spodní vrstva stejně jako při sportu. Zvolte odolné kusy s plochými švy, ať nedrhnou pod opaskem a postrojem. Při fyzické práci platí tenčí varianta.'),
        ('Co si vzít pod termoprádlo?',
         'Obvykle nic, má se dotýkat přímo kůže. Ke spodním partiím můžete zvolit bezešvé boxerky nebo slipy pro větší komfort. Bavlněné spodní prádlo pod ním nasákne a zmaří efekt vrstvy.'),
    ])

# ------------------------------------------------------------------ arena-plavky
NEW['arena-plavky'] = dict(
    title='Arena plavky: bazénové a závodní plavky pro každého',
    desc='Arena plavky pro bazén i závodní plavání: dámské jednodílné a bikiny, pánské jammery a boxerky, dětské modely. Jak vybrat střih, velikost a péči.',
    intro='<p>Arena je značka, která se soustředí na plavání, a od většiny módních plavkových značek se liší tím, že plavky navrhuje především pro vodu a trénink. V nabídce proto uvidíte jednodílné modely s pevnými zády, pánské jammery a přiléhavé šortky, ale i bikiny a plážové boxerky pro odpočinek u vody. '
          'Tato stránka třídí plavky značky z kategorie <a href="/plavky/">plavky</a>, vysvětluje, jak se liší střihy zad a nohavic, co znamená označení Pro Back, Cross Back nebo Jammer a jak vybrat velikost, aby plavky vydržely v chlorované vodě. Najdete také tipy na dětské a juniorské plavky a porovnání s dalšími značkami, například <a href="/speedo-plavky/">Speedo</a>, <a href="/plavky-nike/">Nike</a> a <a href="/plavky-adidas/">Adidas</a>.</p>',
    guide='<h2>V čem je Arena jiná než módní plavková značka</h2>'
          '<p>Plavecká značka řeší jiné věci než módní. Rozhoduje hydrodynamika, pevnost švů, odolnost materiálu proti chloru a to, aby plavky držely při obrátkách a odrazu od stěny. Vzory a barvy jsou důležité, ale až na druhém místě. Proto mají plavky Arena obvykle plochý střih, pevná ramínka a materiály určené pro častý pobyt v bazénu. Pro dovolenou u moře jsou stejně použitelné, ale pro běžné opalování mohou působit sportovněji, než kdo čeká.</p>'
          '<h2>Dámské plavky: jednodílné, Cross Back a bikiny</h2>'
          '<p>Nejčastěji se mezi dámskými plavkami Arena objevují jednodílné modely se zády, které se u plavání osvědčily. Název prozrazuje tvar zad a to, jak pevně plavky drží na ramenou. Při nákupu proto věnujte pozornost střihu zad víc než barvě.</p>'
          + T(['Střih', 'Jak vypadá', 'Pro koho je'], [
              ['Pro Back', 'užší ramínka vedoucí k zádům, tvarovaný výstřih', 'plavky na trénink, kde záleží na volnosti ramen'],
              ['Cross Back / Xcriss', 'ramínka se v zádech kříží', 'pevné držení a nesklouzávání při aktivním plavání'],
              ['Open Back / U Back', 'otevřená záda s širším výstřihem', 'rekreační plavání a pohodlí v ramenou'],
              ['Wing Back', 'široká ramínka s křídlovým střihem', 'větší opora v horní části a tvarovací efekt'],
              ['Dvoudílné a bikiny', 'horní díl a kalhotky, často bandeau nebo trojúhelník', 'odpočinek u vody a lehké plavání'],
              ['Shapewear', 'tvarovací střih s pevnějším tkaním', 'pro ty, kdo preferují stažení a zpevnění']]) +
          '<p>Zkoušejte plavky v předklonu a při zvednutí paží. Jednodílné modely s vyšším vzadu střihem drží i při obrátkách a skocích. Pokud plavete jen občas, ocení se pohodlnější otevřená záda. Při tréninku několikrát týdně vyberte Cross Back nebo Pro Back, které se během pohybu nepohnou.</p>'
          '<h2>Pánské plavky: jammer, slipy a šortky</h2>'
          '<p>U pánských modelů je nejdůležitější délka nohavice. Jammer sahá po kolena a nabízí nejvíce hydrodynamiky i opory svalů. Slipy jsou nejlehčí, ale méně pohodlné pro někoho, kdo je nenosí. Plavecké šortky (swim short) a boxerky jsou volnější a lépe se hodí na pláž nebo do aquaparku. Uprostřed leží krátký a střední jammer, například s označením Mid Jammer, který kombinuje sportovní střih s pohodlím. Pro pravidelné plavání se hodí slipy a jammery, protože se při obrátkách nevlní, zatímco volné šortky odpor zvyšují.</p>'
          '<h2>Závodní plavky a technologie přiléhavosti</h2>'
          '<p>Mezi nabídkou se objevují i závodní modely s označením Powerskin Carbon, tedy plavky s velmi přiléhavým, tuhým materiálem určeným pro závody. Takové plavky se obléknou obtížně, mohou trvat několik minut a trvanlivost je kratší než u tréninkových modelů. Nevhodné jsou na každodenní plavání. Pro závodní plavce platí i pravidla federací pro povolené střihy, takže před nákupem si zkontrolujte, zda vybraný typ odpovídá soutěži, do které půjdete. Pro zbytek lidí postačí trénink v odolném tréninkovém modelu, který je příjemný a stálý.</p>'
          '<h2>Dětské a juniorské plavky Arena</h2>'
          '<p>Chlapecké modely bývají k dispozici jako jammery, slipy a šortky, dívčí jako jednodílné plavky nebo dvoudílné sety. Pro děti, které chodí na kroužek plavání, volte pevný materiál a bezpečné držení ramínek. U nejmenších ocení rodiče jednoduché oblékání. Dětské plavky se rychle stávají malými, proto kupujte podle aktuální míry a ne o dvě čísla větší, protože ve vodě by se plavky nafoukly a bránily pohybu. Další výběr je v kategoriích <a href="/detske-plavky/">dětské plavky</a>, <a href="/damske-plavky/">dámské plavky</a> a <a href="/panske-plavky/">pánské plavky</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Velikosti plavek Arena se uvádějí v číselném evropském systému nebo v klasických S až XL, proto vždy ověřte, jaké značení u konkrétního modelu platí. Plavky mají být těsné, ale nezařezávat. Před koupí změřte obvod hrudníku, pasu a boků a porovnejte s tabulkou výrobce. Protože plavecké materiály po namočení povolí o chlup, kupujte raději menší, pokud se vám v obchodě zdá modelová velikost pohodlná. Pro děti zvolte plavky, které nezanechávají stopy v kůži po nošení.</p>'
          '<h2>Péče o plavky v chlorované vodě</h2>'
          '<p>Chlor je největším nepřítelem elastických vláken. Po každém plavání plavky vypláchněte ve sladké vodě, nikdy je nenechávejte zabalené mokré v tašce a nesušte na slunci ani na topení. Perte ručně, bez aviváže a bez ždímání, jen je jemně stlačte v ručníku. Při pravidelném tréninku střídejte dva páry plavek, aby se vlákna mezi použitím zotavila. Slunce vyblednou barvy, proto plavky sušte ve stínu. Tím prodloužíte životnost o mnoho měsíců.</p>'
          '<h2>Jak plavky zkoušet a na co si dát pozor</h2>'
          '<p>Plavky zkoušejte vždy přes spodní prádlo, jak je zvykem v obchodě, ale pamatujte, že voda mění objem látky. Zkontrolujte tři místa: ramínka nesmí řezat do ramen, nohavice nesmí vytvářet vroubek na stehnech a zadní část nesmí být příliš vysoká nebo naopak nízká. Při předklonu a dřepu se jednodílné plavky nesmí přetáčet v pase. U dvoudílných modelů drží horní díl obvod pod prsy, nikoliv ramínka. Pokud se při zvednutí paží plavky posunují, jsou příliš velké, pokud brání nadechnutí, jsou příliš malé. Pořiďte raději dva kusy základních barev než jeden módní vzor, který se po několika týdnech chlorování ztratí.</p>'
          '<h2>Plavky pro různé typy postavy</h2>'
          '<p>Sportovní střih bývá tolerantní k různým tvarům, ale pár pravidel pomůže. Při širších ramenou se osvědčují zkřížená záda, která rozkládají tah ramínek. Při výraznějších bocích je lepší vyšší střih nohavic s pevnějším lemem, který se nezařezává. Vyšší postavy sáhnou po delším trupu, aby se plavky nestahovaly ramínky nahoru. Menším postavám sedí kratší trup a užší ramínka. U mužů závisí volba na obvodu stehen: jammer s pružným lemem drží, aniž by se zařezával, ale příliš krátký střih se při obrátkách zvedá. Pomůže i vyzkoušení plavek ve dvou velikostech vedle sebe.</p>'
          '<h2>Kdy je Arena dobrou volbou</h2>'
          '<ul><li><strong>Plavete alespoň jednou týdně</strong> a potřebujete plavky, které vydrží chlor.</li><li><strong>Dítě chodí na plavecký kroužek</strong> a potřebuje pevný střih, který se nesesouvá.</li><li><strong>Hledáte sportovní vzhled</strong> bez módních doplňků a volánků.</li><li><strong>Chcete jednu značku</strong> na bazén, moře i aquapark.</li></ul>'
          '<p>Pokud naopak míříte jen na pláž a hledáte hlavně vzory a ozdoby, vybírejte spíše z módních kolekcí. Sportovní střih nemusí každému sedět do formálnějšího prostředí hotelu.</p>'
          '<h2>Doplňky k plavání</h2>'
          '<p>K plavkám patří i další vybavení. Vyberte si <a href="/plavecke-bryle/">plavecké brýle</a> podle tvaru obličeje, <a href="/plavecke-cepice/">plavecké čepice</a> z latexu, silikonu nebo látky a <a href="/plavecke-pomucky/">plavecké pomůcky</a> pro nácvik techniky. Každý z doplňků má vlastní kritéria, ale všechny spojuje to, že se vyplatí zkoušet je v kombinaci s plavkami, aby spolu sedělo celé vybavení.</p>'
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>V kategorii najdete také značky ' + B(('speedo', 'Speedo'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('litex', 'Litex'), ('roxy', 'Roxy')) + '. Každá volí jiné proporce střihů a jiný poměr mezi sportovním a módním přístupem. Arena i Speedo staví své plavky na plaveckých potřebách, kdežto Roxy sází na plážový styl. Na srovnání použijte stránky <a href="/speedo-plavky/">Speedo plavky</a>, <a href="/plavky-nike/">Nike plavky</a>, <a href="/litex-plavky/">Litex plavky</a> a <a href="/decathlon-plavky/">Decathlon plavky</a>.</p>',
    faq=[
        ('Jaké plavky Arena vybrat do bazénu?',
         'Pro pravidelné plavání se hodí jednodílné plavky s pevnými zády, třeba Cross Back nebo Pro Back, a pánské jammery nebo slipy. Tyto střihy se nevlní a drží při obrátkách. Odolnost vůči chloru je dána materiálem.'),
        ('Co znamená Pro Back a Cross Back?',
         'Označují tvar zad jednodílných plavek. Pro Back má užší ramínka vedoucí do zad, Cross Back má ramínka zkřížená. Obojí drží při aktivním plavání, Cross Back o něco pevněji.'),
        ('Čím se jammer liší od slipů a šortek?',
         'Jammer sahá po kolena a nabízí oporu svalů a minimální odpor. Slipy jsou nejlehčí a nejméně omezují pohyb. Šortky jsou volnější a hodí se na pláž, ale ve vodě brzdí.'),
        ('Dají se závodní plavky nosit na trénink?',
         'Nedoporučuje se to. Jsou velmi těsné, obtížně se oblékají a jejich životnost bývá kratší. Na trénink je vhodnější odolný tréninkový model, závodní si nechte na soutěž.'),
        ('Jak velikost plavek Arena vybrat?',
         'Změřte hrudník, pas a boky a porovnejte tabulku výrobce. Plavky mají přiléhat bez zařezávání. Pokud jste mezi velikostmi, u tréninkového střihu zvolte menší, protože se ve vodě mírně povolí.'),
        ('Mohu v plavkách Arena plavat i v moři?',
         'Ano, jsou použitelné i u moře a v aquaparku. Pro pláž sice možná ocení volnější střih, ale sportovní plavky fungují bez problémů. Po moři je stejně vždy opláchněte sladkou vodou.'),
        ('Jak pečovat o plavky po chlorované vodě?',
         'Po plavání je vypláchněte sladkou vodou, jemně vymačkejte a sušte ve stínu. Nepouštějte je do pračky ani nepoužívejte aviváž. Střídání dvou kusů prodlužuje životnost elastických vláken.'),
        ('Vybírám plavky pro dítě, na co dát pozor?',
         'Důležitá je správná velikost a pevný materiál, který drží ramínka. Příliš velké plavky se ve vodě nafouknou. U kroužku plavání zvolte jednodílné dívčí nebo jammer a slipy pro chlapce.'),
        ('Proč plavky Arena po čase ztrácejí tvar?',
         'Příčinou bývá chlor, horká voda a sluneční světlo, které rozkládají elastická vlákna. Pomáhá důkladné vypláchnutí a sušení mimo přímé slunce. Při pravidelném tréninku se vyplatí mít dva páry.'),
        ('Dají se plavky Arena kombinovat s dalším plaveckým vybavením?',
         'Ano, k plavkám se běžně pořizují plavecké brýle, čepice a pomůcky na nácvik techniky. Při výběru zkoušejte vše společně, aby brýle nepřekážely čepici a ramínka plavek netlačila pod řemínkem.'),
    ])

# ------------------------------------------------------------------ decathlon-plavky
NEW['decathlon-plavky'] = dict(
    title='Decathlon plavky: sportovní plavky pro celou rodinu',
    desc='Decathlon plavky: dámské díly a jednodílné, pánské kraťasy a jammery, dívčí a chlapecké, surfové i těhotenské. Jak kombinovat díly a vybrat velikost.',
    intro='<p>Decathlon je obchodní řetězec s vlastními sportovními značkami a jeho plavky slouží hlavně jako praktický základ pro celou rodinu, od prvního brouzdání dětí až po pravidelné plavání dospělých. V nabídce najdete jednodílné modely, dámské plavky prodávané po dílech, pánské kraťasy a boxerky, dětské a dívčí plavky i speciální kousky na surf nebo pro těhotné. '
          'Tato stránka třídí plavky z kategorie <a href="/plavky/">plavky</a> od tohoto prodejce a pomáhá orientovat se v tom, jak si poskládat horní a spodní díl, jak vybrat střih na plavání a surfování a na co se zaměřit u dětských kousků. K dispozici je také srovnání s dalšími značkami, například <a href="/arena-plavky/">Arena</a>, <a href="/speedo-plavky/">Speedo</a> nebo <a href="/litex-plavky/">Litex</a>.</p>',
    guide='<h2>Co typicky nabízí Decathlon mezi plavkami</h2>'
          '<p>Sortiment prodejce je postavený na tom, že plavky mají fungovat, snášet sport a nebýt módním doplňkem na jednu sezonu. Velká část dámských plavek se prodává po dílech, takže si horní a spodní díl poskládáte podle sebe. U pánských a dětských je nabídka rozdělená na plavecké kraťasy, boxerky, jammery a slipy. Jednotlivé typy modelů se v katalogu často opakují v různých vzorech a velikostech a názvy jsou ženská nebo dívčí jména, například Nora nebo Sofy, což je pro Decathlon typické.</p>'
          + T(['Typ plavek', 'Jak vypadá', 'Kdy se hodí'], [
              ['Jednodílné dámské', 'pevná záda, vyšší výstřih nebo otevřená záda', 'bazén, aquaaerobik, surf'],
              ['Horní a spodní díl zvlášť', 'bandeau, trojúhelník, sportovní top, kalhotky s různou výškou', 'dovolená, plavání a kombinování velikostí'],
              ['Pánské kraťasy a boxerky', 'volnější střih s podšívkou nebo sítí', 'pláž, aquapark, rekreační plavání'],
              ['Jammer a slipy', 'přiléhavé, odolné vůči chlóru', 'pravidelné plavání v bazénu'],
              ['Dívčí a chlapecké', 'jednodílné, dvoudílné, šortky, jammery', 'kroužek plavání, dovolená, škola v přírodě'],
              ['Surfové díly a lycra', 'pevné uchycení, vázání, delší střih', 'surf, paddleboard, vodní sporty'],
              ['Těhotenské', 'jednodílné s prostorem pro břicho', 'plavání a odpočinek v těhotenství']]) +
          '<p>Díky systému po dílech není nutné ladit celé plavky podle jedné velikosti. Žena s odlišným obvodem hrudníku a boků si snadno koupí horní díl v jedné a kalhotky v jiné velikosti. Prodejce tím odpovídá na největší problém, který u hotových dvoudílných plavek vzniká.</p>'
          '<h2>Jak kombinovat horní a spodní díl</h2>'
          '<p>Začněte horním dílem, protože ten je citlivější na tvar těla. Bandeau je bez ramínek a hodí se k opalování, sportovní top s pevnými ramínky je lepší do vody. Trojúhelníkové kousky se vážou a nastavují, což je praktické při změně velikosti, ale při plavání drží hůř. U kalhotek je důležitá výška pasu. Vyšší pas lépe sedí u surfu a je pohodlnější při pohybu. Klasické kalhotky jsou pohodlnější při opalování. Pamatujte, že u kombinovaných dílů musejí být odstíny a materiály v téže šarži, protože i mírné rozdíly se na slunci projeví.</p>'
          '<h2>Surfové plavky: pevné uchycení a pohyb</h2>'
          '<p>Některé modely jsou označené jako surfové, tedy určené k pohybu ve vlnách. Mají pevnější vázání, spodní díly s vyšším pasem a přiléhavý střih, který nesklouzne. Hodí se i na paddleboard a jiné vodní sporty, při kterých se tělo hodně pohybuje. Jejich výhodou je, že při pádu do vody nezmizí nic z místa. Pro běžné koupání jsou praktické, ale mohou být méně vzdušné než lehčí plážové plavky. Vybírejte podle toho, jak často se při vodních sportech vyvracíte.</p>'
          '<h2>Plavecké kraťasy a jammery pro muže</h2>'
          '<p>Pánské plavecké kraťasy jsou volnější, rychle schnou a mají podšívku nebo síťku. Na pláž a do aquaparku jsou nejpohodlnější. Pro pravidelné plavání v bazénu se osvědčily jammery, které sahají po kolena a nezpůsobují odpor. Slipy jsou nejlehčí, ale zvykají si na ně jen někteří. Zkuste si vybrat podle toho, kde plavete nejčastěji, a ne podle toho, co je právě ve výprodeji.</p>'
          '<h2>Dívčí a chlapecké plavky</h2>'
          '<p>Dětské plavky musejí hlavně pohodlně sedět a snadno se oblékat. Dívkám se hodí jednodílné plavky s pevnými zády pro plavání a dvoudílné, které se dobře oblékají při pobytu na pláži. Chlapci nosí kraťasy nebo slipy, na plavecký kroužek se vyplatí jammery nebo plavky s pevným střihem. Pro nejmenší jsou k dispozici i modely s volánky nebo roztomilým potiskem, ale vždy zkontrolujte, aby švy nedrhly. Volte přesnou velikost podle výšky a vyhněte se příliš velkým, které se ve vodě nafouknou. Rodiče mohou doplnit kategorií <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h2>Těhotenské plavky a plavání v těhotenství</h2>'
          '<p>Mezi nabídkou najdete i jednodílné těhotenské plavky s prostorem pro rostoucí břicho a pevným držením hrudníku. Plavání je pro mnoho těhotných pohodlnou aktivitou, protože voda nese váhu těla. Při výběru dbejte na pružný, ale nestahující materiál a ramínka, která se dají upravit. Pokud plánujete plavat až do konce těhotenství, vyberte model s prodlouženým trupem. Případné zdravotní otázky nejlépe probere ošetřující lékař.</p>'
          '<h2>Materiály a odolnost proti chloru</h2>'
          '<p>Chlorovaná voda zkracuje život elastických vláken. Pro časté plavání v bazénu se proto vyplatí plavky z polyesteru nebo z materiálů označených jako odolné chlóru. Na pláž stačí běžný mix polyamidu a elastanu, který je měkčí a příjemnější. Zjistěte si složení na štítku nebo v popisu produktu a podle něj vyberte. Světlé barvy často vyžadují podšívku, aby nebyly průsvitné.</p>'
          '<h2>Plavky na dovolenou, do bazénu a do aquaparku</h2>'
          '<p>Rodiny často kupují plavky na jednu sezonu a očekávají, že budou fungovat všude. V praxi se vyplatí rozlišit tři prostředí. Na dovolenou u moře pracujte s pohodlím a rychlým schnutím, protože se plavky nosí celý den. V bazénu je důležitější odolnost vůči chloru a pevný střih. V aquaparku se jede na skluzavkách po tvrdém povrchu, proto zvolte plavky bez ozdob, kovových doplňků a tvrdých prvků, které by se mohly zachytit nebo způsobit poranění. Pro děti pamatujte i na UV ochranu, například na lycra triko s dlouhým rukávem, které chrání před spálením lépe než krém samotný.</p>'
          '<h2>Na co se zaměřit při výběru online</h2>'
          '<p>Při nákupu na dálku se dívejte na tři údaje. Prvním je popis střihu: zda jde o jednodílné plavky, horní díl, spodní díl nebo kraťasy, protože názvy často liší jen jedním slovem. Druhým je složení materiálu, které rozhoduje o odolnosti vůči chloru a pohodlí. Třetím je tabulka velikostí s mírami v centimetrech, ne jen označení S nebo M. U dílů prodávaných zvlášť si ověřte, že druhý díl máte ve stejném vzoru a odstínu. Zkontrolujte také podmínky vrácení, protože hygienické zboží si někteří prodejci vracet nenechají, pokud je štítek odstraněn. Plavky proto zkoušejte doma jen přes spodní prádlo a štítek ponechte.</p>'
          '<h2>Praktická péče o plavky</h2>'
          '<p>Po koupání plavky vypláchněte sladkou vodou, vymačkejte je bez ždímání a sušte ve stínu. Nenechávejte je zabalené v mokrém ručníku, protože se rychle objeví zápach a plíseň. Pro péči nepoužívejte aviváž ani horkou vodu. Pokud plavky nosíte denně na dovolené, střídejte dva kusy, aby jeden mohl schnout. Barvy zachová i opláchnutí po pobytu v moři, kde sůl a slunce urychlují vyblednutí. Tak zůstanou plavky použitelné i další sezonu.</p>'
          '<h2>Srovnání s dalšími značkami</h2>'
          '<p>Decathlon je spíš široký praktický sortiment než specializovaná plavecká značka. Pokud potřebujete plavky přímo pro závodní trénink, mrkněte na ' + B(('arena', 'Arena'), ('speedo', 'Speedo')) + '. Pro módnější a plážové varianty se podívejte na ' + B(('roxy', 'Roxy'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('litex', 'Litex')) + '. Další přehledy jsou na stránkách <a href="/plavky-nike/">Nike plavky</a>, <a href="/plavky-adidas/">Adidas plavky</a>, <a href="/calvin-klein-plavky/">Calvin Klein plavky</a> a <a href="/roxy-plavky/">Roxy plavky</a>.</p>'
          '<h2>Jak si vybrat podle kategorie</h2>'
          '<p>Pokud víte, pro koho plavky hledáte, využijte rychlé zkratky: <a href="/damske-plavky/">dámské plavky</a>, <a href="/panske-plavky/">pánské plavky</a> a <a href="/detske-plavky/">dětské plavky</a>. Každá z nich nabízí odlišné střihy a doplňuje nabídku prodejce o další značky.</p>',
    faq=[
        ('Jsou plavky Decathlon vhodné do bazénu?',
         'Ano, vybírejte jednodílné dámské plavky s pevnými zády a pánské jammery nebo slipy z materiálu odolného chlóru. Volné kraťasy a dvoudílné kousky na opalování se do bazénu hodí méně.'),
        ('Mohu si koupit horní a spodní díl v jiné velikosti?',
         'Ano, dámské plavky se prodávají po dílech právě proto, aby šlo kombinovat velikosti. Sledujte, aby byl odstín a vzor stejný, a zkuste si díly vždy v kombinaci.'),
        ('Co jsou surfové plavky a kdy je potřebuji?',
         'Jsou to plavky s pevnějším uchycením a vyšším pasem, které při pohybu ve vodě nesklouznou. Hodí se na surf, paddleboard nebo jiné vodní sporty. Na běžné koupání stačí lehčí plážový střih.'),
        ('Jak vybrat dětské plavky podle velikosti?',
         'Měřte výšku a obvod hrudníku dítěte a porovnejte s tabulkou. Plavky mají přiléhat, ale neškrtit. Příliš velké se ve vodě nafouknou a mohou bránit pohybu.'),
        ('Jaké plavky zvolit pro kroužek plavání?',
         'Pro dívky jednodílné s pevnými zády a pro chlapce jammery nebo slipy. Důležité je, aby švy nedrhly a materiál zvládal chlor. Barvy nejsou tak důležité jako střih.'),
        ('Je v nabídce něco pro těhotné?',
         'Ano, jednodílné těhotenské plavky s prostorem pro břicho a pružným, ale pevným materiálem. Zvolte model s nastavitelnými ramínky a delším trupem. Plavání v těhotenství je dobré probrat s lékařem.'),
        ('Čím se liší pánské kraťasy a jammery?',
         'Kraťasy jsou volnější a pohodlné na pláž. Jammer sahá po kolena, přiléhá a snižuje odpor ve vodě, takže se hodí do bazénu. Slipy jsou nejlehčí, ale méně pohodlné pro každého.'),
        ('Jak dlouho plavky vydrží?',
         'Záleží na četnosti plavání a péči. Chlor a slunce zkracují život vláken. Pomáhá opláchnutí sladkou vodou po každém použití, sušení ve stínu a střídání dvou kusů.'),
        ('Jak vybrat velikost dámských plavek?',
         'Změřte obvod hrudníku, pasu a boků a řiďte se tabulkou. U dílů vyberte horní a spodní zvlášť. Plavky mají přiléhat bez zařezávání, ve vodě se mírně povolí.'),
        ('Jaká značka je lepší pro závodní plavání?',
         'Pro závodní trénink se spíše hodí specializované plavecké značky, například Arena nebo Speedo. Decathlon je vhodný jako praktická rodinná volba pro rekreační plavání a dovolenou.'),
    ])
