"""sporteka.cz — facet landing texts wave 114: elektrokola-crussis, panske-vesty, damske-boty-do-vody, speedo-plavky.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ elektrokola-crussis
NEW['elektrokola-crussis'] = dict(
    title='Elektrokola Crussis: modelové řady, baterie a velikosti',
    desc='Elektrokola Crussis v nabídce českých obchodů: hardtaily a celoodpružené e-bike, dámské rámy, kapacity baterií a rady k velikosti rámu a kol.',
    intro='<p>Crussis je česká značka, která v nabídce srovnávače vystupuje hlavně s horskými elektrokoly. Najdete tu pevné rámy i celoodpružené stroje, dámské provedení rámu a modely označené ročníkem, u nichž se v názvu objevuje kapacita baterie ve watthodinách i údaj o středovém motoru. '
          'Tato stránka je užší výběr z kategorie <a href="/elektrokola/">elektrokola</a>: pomáhá se zorientovat v tom, jak číst názvy modelů, čím se liší hardtail od celoodpruženého kola a jakou velikost rámu zvolit. Dozvíte se také, co si ověřit u baterie, jak plánovat dojezd v kopcovitém terénu a proč se vyplatí porovnat stejný model u více prodejců. Pokud hledáte něco jiného než horské kolo, projděte si sousední výběr <a href="/panska-elektrokola/">pánská elektrokola</a> nebo <a href="/elektrokola-vyprodej/">výprodej elektrokol</a>.</p>',
    guide='<h2>Co z Crussis najdete a jak číst názvy modelů</h2>'
          '<p>Značka staví horská elektrokola, která pokrývají cestu od pohodlných jezdeckých strojů po sportovnější celoodpružené modely. V katalogu se opakují pojmenování jako e-Atland, e-Largo, e-Hard, e-Fionna, e-Guera, e-Full a ONE-Full. Číslo za jménem, třeba 10.11 nebo 9.11, odpovídá výbavě a ročníku. Za ním bývá uvedena kapacita baterie, velikost kol v palcích a v závorce nebo za pomlčkou velikost rámu. U novějších ročníků se u vybraných modelů uvádí i typ středového motoru.</p>'
          + T(['Část názvu', 'Co znamená', 'Na co se zaměřit'], [
              ['e-Hard, e-Atland, e-Largo', 'kola s pevným rámem, tedy hardtail', 'jednodušší údržba, přímý přenos síly, vhodné na lesní cesty a dojíždění do kopců'],
              ['e-Full, ONE-Full', 'celoodpružené modely s tlumičem vzadu', 'komfort na kořenech a kamení, ale větší hmotnost a více míst k seřízení'],
              ['Dámská verze (e-Guera)', 'rám s nižším průvlakem', 'snazší nasedání, ale ověřte nosnost a velikost rámu'],
              ['Číslo s Wh (např. 715Wh)', 'kapacita baterie', 'čím vyšší, tím delší dojezd i větší hmotnost'],
              ['27,5" nebo 29"', 'průměr kol', 'menší kolo je hravější, větší překonává terén plynuleji'],
              ['Ročník (model 2026)', 'generace kola', 'u starších ročníků porovnejte výbavu a záruku']]) +
          '<p>Všechna čísla v názvu berte jako vodítko. Úplný seznam komponent, tedy značku brzd, převodníku a vidlice, najdete vždy na stránce prodejce nebo u výrobce, protože se mezi ročníky mění.</p>'
          '<h2>Hardtail, nebo celoodpružené kolo</h2>'
          '<p>Hardtail má odpruženou jen přední vidlici a zadní stavba je pevná. Je lehčí, levněji se udržuje a při šlapání do kopce se necuká. Pro většinu jezdců, kteří jezdí po lesních a polních cestách, je to rozumná volba. Celoodpružené kolo drží stopu na nerovném povrchu, lépe chrání záda a dlouhé sjezdy jsou pohodlnější. Platíte za to hmotností, složitější konstrukcí a vyššími nároky na údržbu čepů a tlumiče.</p>'
          '<ul><li><strong>Dojíždění a rodinné výlety:</strong> hardtail s nižším rámem a širšími plášti.</li>'
          '<li><strong>Lesní a kopcovité trasy:</strong> hardtail s kvalitní vidlicí, případně lehčí celoodpružené kolo.</li>'
          '<li><strong>Technické stezky a delší sjezdy:</strong> celoodpružený model s dostatečným zdvihem.</li>'
          '<li><strong>Vyšší hmotnost jezdce nebo náklad:</strong> zkontrolujte maximální nosnost celého kola, ne jen rámu.</li></ul>'
          '<h2>Baterie, motor a skutečný dojezd</h2>'
          '<p>Kapacita ve watthodinách říká, kolik energie baterie pojme. Dojezd z ní ale určují vaše podmínky: hmotnost jezdce, převýšení, vítr, tlak v pneumatikách i zvolená úroveň podpory. V rovině dojedete mnohem dál než v kopcích a při jízdě s nejvyšší podporou se baterie vyčerpá výrazně rychleji. Proto se u horských tras řiďte spíš převýšením než kilometry.</p>'
          '<p>Středový motor, který se u novějších kol Crussis uvádí v názvu modelu, sedí v oblasti kliky. Těžiště zůstává nízko a rovnoměrně rozložené, kolo se chová přirozeně a snadno se vede. Při koupi si ověřte, zda je baterie vyjímatelná, jak dlouho se nabíjí a zda lze koupit náhradní nabíječku a baterii. U elektrokola to rozhoduje o životnosti celého stroje.</p>'
          + T(['Situace', 'Dopad na dojezd', 'Co dělat'], [
              ['Strmé a dlouhé stoupání', 'vysoká spotřeba', 'využívejte nižší převod a střední podporu'],
              ['Zima a chlad', 'baterie dočasně ztrácí kapacitu', 'nechte ji před jízdou v teple'],
              ['Nízký tlak v pneumatikách', 'větší odpor', 'kontrolujte tlak před každou delší jízdou'],
              ['Těžký náklad nebo batoh', 'vyšší zátěž motoru', 'rozložte váhu, nepřetěžujte zadní nosič'],
              ['Rovina s mírnou podporou', 'nejlepší dojezd', 'volte nejnižší stupeň podpory']]) +
          '<h2>Jak zvolit velikost rámu a kol</h2>'
          '<p>Velikost rámu se u horských kol uvádí v palcích, u Crussis ji najdete v názvu produktu, například 17", 19" nebo 21". Orientačně platí, že menším postavám vyhovuje rám kolem šestnácti až sedmnácti palců, střední výšce osmnáct až devatenáct a vysokým jezdcům dvacet a víc. Rozhodující je ale délka nohou a pohodlný dosah na řídítka. Výrobce k tomu vždy uvádí tabulku podle výšky postavy, kterou si před koupí ověřte.</p>'
          '<p>Velikost kol 27,5" se vyplatí pro menší jezdce a hravější ovládání, 29" pro vyšší postavy a plynulejší přejíždění nerovností. Na rámech pro nižší postavu se často vyskytují menší kola, protože vyšší by narážela na nohy. Pokud jste na hranici dvou velikostí, vyzkoušejte obě, nebo zvolte menší rám a prodlužte představec či sedlovku.</p>'
          '<h2>Dámské rámy a kolo pro menší postavu</h2>'
          '<p>Dámský model, v nabídce například e-Guera, má obvykle nižší průvlak a někdy jinak tvarované sedlo i řídítka. Nasedání je pohodlnější, zvlášť s plně naloženým batohem nebo ve svahu. Při výběru nehledejte jen označení pro ženy, ale hlavně dostupné velikosti rámu a jejich nosnost. Pokud jste vyšší, jsou pro vás stejně vhodné i modely bez označení. Z kategorií stojí za zhlédnutí také <a href="/damska-elektrokola/">dámská elektrokola</a> a <a href="/detska-elektrokola/">dětská elektrokola</a>, kde najdete menší rámy.</p>'
          '<h2>Co si u Crussis ověřit před koupí</h2>'
          '<ol><li>Přesný ročník a výbavu: dva modely se stejným jménem mohou mít jiné komponenty.</li>'
          '<li>Kapacitu baterie a to, zda se dá vyjmout a nabíjet i mimo kolo.</li>'
          '<li>Velikost rámu a velikost kol, nejlépe podle tabulky výrobce.</li>'
          '<li>Dopravu a stav: některé obchody posílají kolo složené, jiné smontované, a je třeba domluvit seřízení.</li>'
          '<li>Záruku na rám, motor a baterii zvlášť, protože se často liší.</li>'
          '<li>Možnosti servisu: někdo ze značkových dealerů nebo vlastní servis ve vašem okolí.</li></ol>'
          '<h2>Příslušenství a doprovodné vybavení</h2>'
          '<p>Hodí se helma, světla, zámek a brašna. U elektrokola doporučujeme kvalitní zámek, protože hodnota kola láká zloděje. Dobré světlo na řídítkách pomáhá i při večerním návratu z lesa. Z doplňků se vyplatí projít <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/cyklo-svetla/">světla na kolo</a>, <a href="/cyklo-zamky/">zámky na kolo</a> a <a href="/cyklo-tasky-a-nosice/">brašny, nosiče a košíky</a>. Pro opravy na trase se hodí <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Crussis nabízí i některé doplňky, například světla, láhve a držáky na láhev, které se k jejich kolům hodí barevně.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejný model může mít u různých prodejců jinou dodací lhůtu i jinou cenu, protože se liší balení a servis. Sledujte, zda je kolo skladem, jaká je velikost rámu a jak je popsaná baterie. Pokud chcete kolo s nižší podporou a jiným typem využití, projděte kategorii <a href="/horska-elektrokola/">horská elektrokola</a>, kde najdete i jiné značky, a pro delší cesty se podívejte na <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>. Sklopné nebo kompaktní kolo pro vlak řeší kategorie <a href="/skladaci-elektrokola/">skládací elektrokola</a>.</p>'
          '<h2>Péče a bezpečné používání</h2>'
          '<p>Po jízdě v blátě omyjte kolo mírným proudem vody, ne tlakovou myčkou a ne přímo do motoru či baterie. Řetěz promažte, brzdové destičky kontrolujte častěji než u běžného kola, protože vyšší hmotnost a rychlost je opotřebovávají rychleji. Baterii ukládejte částečně nabitou, v suchu a při pokojové teplotě, a nenechávejte ji dlouho zcela vybitou. Před první jízdou vyzkoušejte brzdy a nastavení podpory na rovině. Pravidelný servis motoru a brzd si předem domluvte u prodejce.</p>',
    faq=[
        ('Jaké elektrokola Crussis jsou v nabídce?', 'Hlavně horská elektrokola: hardtaily s pevným rámem i celoodpružené modely, k tomu dámské provedení a modely označené ročníkem. U každého zjistíte kapacitu baterie, velikost kol a rámu. Konkrétní nabídka se u obchodů mění, proto ji ověřte aktuálně na stránce produktu.'),
        ('Hodí se Crussis na dojíždění do práce?', 'Ano, zejména hardtail s vyjímatelnou baterií, pokud máte kopcovitou trasu. Horské kolo ale bývá těžší než městské, takže počítejte s komfortem v terénu na úkor lehkosti. Pro čistě rovinaté dojíždění je pohodlnější městský nebo trekingový model.'),
        ('Je lepší hardtail, nebo celoodpružené kolo?', 'Hardtail se hodí pro lesní cesty, kopce a pravidelné výlety, protože je lehčí a jednodušší na údržbu. Celoodpružené kolo vyberte, pokud jezdíte po nerovných a technických stezkách, kde zadní tlumič výrazně přidá na komfortu a kontrole.'),
        ('Jak velkou baterii zvolit?', 'Záleží na terénu a délce jízd. Pro krátké okruhy v mírném terénu postačí menší kapacita, na delší horské výlety s velkým převýšením zvolte větší. Číslo ve Wh je jen kapacita, skutečný dojezd ovlivňují váha, vítr, tlak v plášti i stupeň podpory.'),
        ('Jak poznám správnou velikost rámu?', 'Podívejte se do tabulky výrobce, kde je velikost přiřazena k výšce postavy. Orientačně platí, že nižší jezdci volí menší rám v rozmezí šestnácti až sedmnácti palců, střední výška osmnáct až devatenáct a vyšší dvacet a víc. Rozhodne také délka nohou a pohodlný dosah na řídítka.'),
        ('Čím se liší 27,5" a 29" kola?', 'Menší kola jsou hravější a lépe se vedou v zatáčkách, hodí se pro nižší postavy. Větší kola plynuleji přejíždějí kořeny a kameny, proto je volí vyšší jezdci a ti, kdo preferují stabilitu při vyšší rychlosti.'),
        ('Můžu s elektrokolem jezdit bez podpory?', 'Ano, kolo funguje jako běžné, ale je těžší, takže bez pomoci motoru se jede hůř, hlavně do kopce. Motor se zapíná jen při šlapání. Pro delší úseky bez podpory si zvolte lehčí převod a šetřete baterii.'),
        ('Jak dlouho se nabíjí baterie?', 'Doba nabíjení závisí na kapacitě baterie a výkonu nabíječky, obvykle jde o několik hodin. Přesný údaj uvádí výrobce. Baterii je lepší nabíjet při pokojové teplotě a nenechávat ji zapojenou donekonečna.'),
        ('Na co si dát pozor při online nákupu kola?', 'Ověřte velikost rámu, ročník a výbavu, způsob dodání a rozsah záruky na motor i baterii. Zjistěte, zda je kolo smontované, nebo zasláno částečně rozložené, a kde proběhne první seřízení. Srovnejte to u více prodejců a berte v úvahu nejen cenu, ale i servis.'),
        ('Potřebuji na elektrokolo helmu nebo pojištění?', 'Helma se doporučuje vždy, protože se jezdí rychleji než na běžném kole. Pro děti ji ukládá zákon a dospělým ji lze jen doporučit. Pokud motor podporuje jen do 25 km/h a má omezený výkon, jezdí se s kolem jako s jízdním kolem, u silnějších strojů se ale pravidla liší, proto kategorii ověřte u prodejce.'),
    ])

# ------------------------------------------------------------------ panske-vesty
NEW['panske-vesty'] = dict(
    title='Pánské vesty: střih, materiál a vrstvení pro každou sezónu',
    desc='Pánské vesty pro město, turistiku, běh i kolo: jak vybrat velikost, materiál a střih, kdy vesta nahradí bundu a jak ji vrstvit. Srovnání nabídek.',
    intro='<p>Pánská vesta je vrstva, která zahřeje trup, ale nechá volné ruce. Hodí se v zimě pod bundu, na jaře a na podzim samostatně a v horách při chůzi, kdy rukávy přehřívají. Oproti dámským a dětským modelům se pánská řada liší delším tělem, širšími rameny a rovnějším střihem v pase, který ponechává dost místa pro vrstvu pod ní. '
          'Tato stránka vybírá z kategorie <a href="/sportovni-vesty/">vesty</a> modely určené mužům, od lehkých prošívaných přes softshellové a fleecové až po běžecké a cyklistické. V průvodci najdete rady pro velikost, srovnání materiálů, vrstvení a doporučení podle sportu. Pokud hledáte jiný střih, vyzkoušejte <a href="/damske-vesty/">dámské vesty</a> nebo <a href="/detske-vesty/">dětské vesty</a>.</p>',
    guide='<h2>V čem se pánská vesta liší</h2>'
          '<p>Pánské modely se šijí na širší ramena a delší trup. Pas bývá rovnější a boky nejsou výrazně tvarované, protože vesta nesedí na křivkách, ale slouží jako volnější vrstva. Délka sahá obvykle k pasu nebo o něco níž, aby kryla spodní část zad. Rozhodující je rozměr přes prsa a délka zad, ne jen označení M nebo L. Mezi značkami se velikosti liší: britský střih bývá štíhlejší než severský, lyžařské značky mají prostornější vesty na vrstvení.</p>'
          + T(['Prvek', 'Pánská úprava', 'Co si ověřit'], [
              ['Ramena', 'širší prostřih podpaží', 'volná paže při předpažení, vesta nesmí škrtit'],
              ['Délka', 'delší záda, někdy delší vzadu než vpředu', 'pokrytí bederní oblasti na kole a při předklonu'],
              ['Pas a boky', 'rovnější střih', 'prostor pro vrstvu, ale vesta nemá viset'],
              ['Kapsy', 'větší na zip, někdy vnitřní na telefon', 'dostupnost při batohu a bederním pásu'],
              ['Límec', 'stojáček nebo kapuce', 'ochrana krku vs. volnost v batohu']]) +
          '<p>Při koupi zvažte, co budete mít pod vestou. Tenké triko vyžaduje přiléhavější střih, mikina nebo fleece zase o číslo větší velikost. Pokud kolísáte mezi dvěma velikostmi, volte větší u vesty na vrstvení a menší u sportovní, kde se hodí přiléhavost.</p>'
          '<h2>Typy vest podle materiálu</h2>'
          '<p>Materiál určuje, v jakém počasí vesta pomůže. Prošívaná se syntetickou izolací hřeje i při mírném zvlhnutí, péřová je nejlehčí na teplo, ale neodpouští vlhkost. Softshell odráží vítr, fleece je prodyšný a příjemný při pohybu. Pro ty, kdo hledají univerzální jednu vestu na celou sezonu, je dobrou volbou softshell nebo hybridní vesta s izolovanou hrudí a pružnými zády.</p>'
          + T(['Typ', 'Hodí se pro', 'Slabina'], [
              ['Prošívaná', 'město, výlety, vrstva pod bundu', 'prošívání může propouštět vítr'],
              ['Péřová', 'chladné suché dny, skladnost', 'ztrácí teplo při promoknutí'],
              ['Softshell', 'turistika, kolo, jaro a podzim', 'méně izolace než prošívaná'],
              ['Fleece', 'pobyt venku, chůze, vrstva pod bundu', 'propouští vítr'],
              ['Běžecká a trailová', 'běh, rychlá turistika', 'minimum tepla, jen pro pohyb'],
              ['Pracovní a reflexní', 'dílna, doprava, viditelnost', 'netepluje, některé jsou jen bezpečnostní']]) +
          '<p>V nabídce srovnávače najdete pánské vesty značek jako ' + B(('regatta', 'Regatta'), ('columbia', 'Columbia'), ('helly-hansen', 'Helly Hansen'), ('haglofs', 'Haglöfs'), ('loap', 'Loap'), ('kilpi', 'Kilpi'), ('hannah', 'Hannah'), ('husky', 'Husky'), ('northfinder', 'Northfinder'), ('swix', 'Swix'), ('4f', '4F')) + '. Liší se zaměřením: některé jsou orientované na turistiku, jiné na běžecké lyžování nebo městský styl.</p>'
          '<h2>Jak vestu vrstvit</h2>'
          '<p>Vrstvení má tři úrovně: spodní prádlo odvádí pot, střední vrstva hřeje a svrchní chrání před větrem a deštěm. Vesta patří do střední vrstvy nebo ji lze nosit jako svrchní, pokud je z větruodolného materiálu. Hřeje kmen, ale nechává volné paže, takže zabrání přehřátí v rukávech a zároveň drží teplo tam, kde je ho nejvíc zapotřebí.</p>'
          '<ul><li><strong>Chladné ráno:</strong> funkční triko s dlouhým rukávem, vesta a bunda přes ni, vestu při zahřátí sundáte a uložíte.</li>'
          '<li><strong>Stání nebo chůze v zimě:</strong> vesta pod zimní bundou zahřeje jádro těla.</li>'
          '<li><strong>Pohyb ve větru:</strong> softshellová vesta s dlouhým rukávem pod ní nahradí těžší bundu.</li>'
          '<li><strong>Kancelář a město:</strong> tenká prošívaná vesta přes košili nebo mikinu.</li></ul>'
          '<p>K vestě se hodí <a href="/mikiny/">mikiny</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/vetrovky/">větrovky</a>, které vrstvu doplní, když se ochladí.</p>'
          '<h2>Vesta podle sportu</h2>'
          '<p>Na túru volte lehkou, prodyšnou vestu s kapsami, do kterých dosáhnete i s batohem. Pro běh stačí tenká vesta s vyšším límcem a zadní kapsou, příp. odnímatelná. Na kolo zvolte větruvzdorný přední díl a prodyšná záda, ideálně delší vzadu. Pro běžecké lyžování se osvědčily přiléhavé větruvzdorné vesty, které nebrání pohybu paží. Podle toho se hodí také <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a> či <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>. Pokud hledáte vesty s větším počtem kapes, pomůže kategorie <a href="/sportovni-bundy/">sportovní bundy a vesty</a>.</p>'
          '<h2>Velikost a střih krok za krokem</h2>'
          '<ol><li>Změřte obvod hrudníku v nejširším místě, ve stoje, pod pažemi.</li>'
          '<li>Změřte délku od krčního obratle k pasu, abyste věděli, jak dlouhou vestu potřebujete.</li>'
          '<li>Porovnejte čísla s tabulkou konkrétní značky, ne s tabulkou jiné.</li>'
          '<li>Přemýšlejte, jakou vrstvu pod vestou budete nosit, a podle toho případně přidejte číslo.</li>'
          '<li>U online nákupu zkontrolujte vrácení zboží, abyste mohli velikost vyměnit.</li></ol>'
          '<h2>Vesta jako součást oblečení do hor a do města</h2>'
          '<p>V horách se vesta uplatní při výstupu, kdy se tělo zahřívá a rukávy by zbytečně přidávaly teplo. Na vrcholu a při odpočinku přes ni natáhnete bundu a zabráníte prochladnutí. Důležité je, aby vesta nešla při sundání batohu do cesty: límec by neměl tlačit na krk a popruhy batohu nesmějí třít o zip. V zimě, při pomalé chůzi nebo při stání na zastávce, hřeje prošívaná vesta pod kabátem nebo zimní bundou kmen, kde je teplo nejdůležitější, a nezvětšuje objem rukávů.</p>'
          '<p>V městském provozu je vesta nenápadnější než bunda a lépe se kombinuje. Tenká prošívaná pasuje přes košili, softshell přes tričko nebo mikinu, fleece přes tričko a k džínám. Při výběru do kanceláře zvolte jednobarevnou, bez velkých log a s tichým zipem. Pokud ji chcete nosit i v autě, vybírejte měkký materiál, který se nemačká a nešustí.</p>'
          '<h2>Na co se dívat u zipů, kapes a límce</h2>'
          '<ul><li><strong>Zip:</strong> dvoucestný zip umožní sednout si, aniž by vesta zvedala spodní okraj, a krytý zip zadrží vítr.</li>'
          '<li><strong>Kapsy:</strong> boční kapsy na zip ochrání telefon, vnitřní kapsa se hodí na peněženku nebo klíče.</li>'
          '<li><strong>Límec:</strong> vyšší stojáček chrání krk a bývá z měkké podšívky, aby netřel.</li>'
          '<li><strong>Spodní lem:</strong> stahovací šňůrka nebo guma zabraňuje profukování.</li>'
          '<li><strong>Průramky:</strong> lemování nebo pružná páska zajistí, že vesta neodstává od těla.</li></ul>'
          '<p>Tyto drobnosti rozhodují, zda se vesta bude nosit denně, nebo jen výjimečně. Jednoduchý zip, který se nezasekává, a kapsy, do kterých dosáhnete bez shýbání, ocení ten, kdo ji bere na každodenní cesty.</p>'
          '<h2>Barva a viditelnost</h2>'
          '<p>Černá a tmavě modrá se hodí do města a ke všemu, ale ve tmě se ztrácejí. Pro kolo a běh po setmění zvolte reflexní prvky nebo výraznou žlutou či oranžovou. Světlé barvy ukazují špínu, zvlášť na manžetě a u kapsy. Pracovní vesty mívají reflexní pruhy, které slouží bezpečnosti, ne zahřátí.</p>'
          '<h2>Péče o vestu</h2>'
          '<p>Prošívané a péřové vesty perte na šetrný program s přípravkem na péřové oděvy a sušte s tenisovými míčky, aby se výplň rozptýlila. Softshell perte při nízké teplotě bez aviváže, která zalepí póry. Fleece nesuší u zdroje tepla, protože se deformuje. Po dlouhém používání obnovte impregnaci voděodolné úpravy. Pokud vestu často balíte, skladujte ji volně, ne stlačenou celé měsíce.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejná vesta se objevuje u více obchodů s různou cenou, dodáním a dostupností velikostí. Sledujte, zda je skladem vaše velikost a jak se zboží vrací. Pozor na dětské a dámské modely: v kategorii Vesty jsou i ony, takže hledejte označení pánská. Pro doplnění stylu se podívejte i na <a href="/zimni-bundy/">zimní bundy</a> a <a href="/nepromokave-bundy/">nepromokavé bundy</a>.</p>',
    faq=[
        ('Jakou velikost pánské vesty zvolit?', 'Řiďte se obvodem hrudníku a tabulkou konkrétní značky. Pokud vestu nosíte přes mikinu nebo fleece, vezměte o číslo větší. Pro sportovní užití je lepší přiléhavější střih, který nebrání pohybu a nepřekáží pod bundou.'),
        ('Je lepší prošívaná, nebo softshellová vesta?', 'Prošívaná lépe hřeje při stání a pomalém pohybu, softshell je pružnější, odolá větru a hodí se při pohybu. Pro každodenní nošení v chladnu zvolte prošívanou, pro turistiku a kolo softshell.'),
        ('Dá se vesta nosit místo bundy?', 'Na jaře, na podzim nebo při intenzivním pohybu ano, zvlášť pokud máte pod ní vrstvu s dlouhým rukávem. V zimě a v dešti ale vesta samotná nestačí a patří pod bundu nebo spolu s nepromokavou vrstvou.'),
        ('Čím se pánská vesta liší od dámské?', 'Je delší v trupu, širší v ramenou a rovnější v pase. Dámská je kratší a víc tvarovaná k bokům. Štíhlejší muži si někdy vyberou dámský střih, ale měřte vždy podle tabulky.'),
        ('Jak vestu vrstvit?', 'Spodní vrstva odvádí pot, vesta hřeje střed těla a svrchní bunda chrání před deštěm. Vestu můžete při zahřátí sundat bez toho, abyste museli rozepínat bundu. U větru zvolte větruvzdorný materiál.'),
        ('Hodí se vesta na kolo?', 'Ano, pokud je větruvzdorná vpředu a prodyšná vzadu. Delší záda chrání bedra při předklonu a reflexní prvky pomáhají za šera. Kapsy na zip uloží telefon nebo klíče.'),
        ('Jak se pere péřová vesta?', 'Na šetrný program s přípravkem na péřové oděvy, při nízké teplotě, a po vyprání se suší s tenisovými míčky nebo plastovými kuličkami, aby se péří nezlepilo. Neperte ji často, jen když je opravdu špinavá.'),
        ('Jakou barvu zvolit?', 'Pro univerzální nošení černou nebo tmavě modrou. Pro viditelnost při běhu, na kole nebo při práci v dopravě volte žlutou, oranžovou nebo vestu s reflexními pruhy. Světlé barvy se rychle špiní.'),
        ('Jak poznám, že je vesta dost teplá?', 'Podívejte se na materiál a výplň: péří a syntetická izolace hřejí víc než fleece nebo tenký softshell. Údaj o gramáži najdete jen u některých značek. Nejlépe se orientujte podle popisu určení, třeba zimní, jarní nebo sportovní.'),
        ('Mohu vestu dát do sušičky?', 'Syntetické prošívané vesty obvykle ano na nízkou teplotu, ale vždy čtěte štítek. Softshell a fleece raději nechte oschnout volně, vysoká teplota poškozuje membránu i vlákna. Péřové vesty se v sušičce suší s míčky.'),
    ])

# ------------------------------------------------------------------ damske-boty-do-vody
NEW['damske-boty-do-vody'] = dict(
    title='Dámské boty do vody: velikost, podrážka a materiál',
    desc='Dámské boty do vody do moře, k jezeru i na paddleboard: jak vybrat velikost, neopren nebo síťku, podrážku a péči. Porovnejte nabídky obchodů.',
    intro='<p>Dámské boty do vody se vyrábějí na užší nohu s užší patou a nižším nártem, než mívají pánské a unisex modely. To se projeví hlavně při chůzi po kamenech nebo při plavání: příliš volná bota sklouzává z paty a vyplavuje ji voda, příliš těsná tlačí na prsty. '
          'Na této stránce jsou boty z kategorie <a href="/obuv-do-vody/">boty do vody</a> určené ženám, od neoprenových přes sítové po otevřené sandály do vody a plavecké ponožky. Průvodce vysvětluje, jak vybrat velikost, jakou podrážku zvolit pro kamenité dno, kdy se vyplatí neopren a co dělat po koupání. Pro muže a děti se podívejte na <a href="/panske-boty-do-vody/">pánské boty do vody</a> a <a href="/detske-boty-do-vody/">dětské boty do vody</a>.</p>',
    guide='<h2>Čím se dámské boty do vody liší</h2>'
          '<p>Ženská noha je v průměru užší, má užší patu a často vyšší klenbu při stejné délce. Dámské modely proto mívají užší střih, menší objem v pateční části a pružnější tkaninu, která obepne nárt. Vybrat správnou velikost je zásadní hlavně u neoprenu, kde je potřeba, aby bota přiléhala, ale netlačila na nehty. V nabídce najdete menší velikosti od EU 35 až po větší, takže zvolíte podle skutečné délky chodidla.</p>'
          + T(['Část boty', 'Dámská úprava', 'Proč na tom záleží'], [
              ['Pata', 'užší, hlubší', 'bota nesklouzává při chůzi ve vodě'],
              ['Nárt', 'nižší, pružný materiál', 'obepne nohu, bez tlaku na šlachy'],
              ['Špička', 'užší, ale s prostorem pro prsty', 'chrání nehty při nárazu na kámen'],
              ['Podešev', 'tenčí a ohebnější', 'lepší cit pro povrch, nižší hmotnost'],
              ['Barvy', 'širší paleta včetně fialové a růžové', 'jde o vzhled, ne o výkon']]) +
          '<p>Rozdíl není jen kosmetický, ale ani zásadní: pokud vám vyhovuje unisex nebo pánský model, můžete ho klidně vzít. Při výběru podle dámského střihu však častěji najdete pevné sedění v patě, což ve vodě rozhoduje.</p>'
          '<h2>Neopren, síťka, ponožka nebo sandál</h2>'
          '<p>Materiál určuje, k čemu se bota hodí. Neopren zahřeje a pevně obepne, síťka propouští vodu a rychle schne, ponožka je tenká a skladná, sandál prodyšný a pohodlný na pláž. Nejčastěji se v nabídce objevuje neopren, ale vybírejte podle toho, kam jedete.</p>'
          + T(['Typ', 'Hodí se na', 'Na co dát pozor'], [
              ['Neoprenová bota', 'chladná voda, paddleboard, kajak, potápění', 'těžší vysušení, nutná správná velikost'],
              ['Síťová bota', 'brodění, treky u vody, potoky', 'méně tepla, písek se do sítě dostane'],
              ['Plavecká ponožka', 'pláž, bazén, lehké kamínky', 'tenká podrážka, málo ochrany'],
              ['Sandál do vody', 'horké dny, rodinné koupání', 'méně pevný při prudším proudu'],
              ['Neopren s tvrdou podešví', 'skalnaté pobřeží, ostré dno', 'méně ohebná, pro dlouhou chůzi těžší']]) +
          '<p>V nabídce srovnávače najdete dámské boty do vody značek ' + B(('speedo', 'Speedo'), ('springos', 'Springos'), ('seac', 'Seac'), ('aqua-speed', 'Aqua Speed'), ('aquos', 'Aquos'), ('alba', 'Alba'), ('insportline', 'inSPORTline')) + '. Speedo se zaměřuje na plavání a vodní sporty, Seac na potápění a Aqua Speed na plavecké doplňky, ostatní značky nabízejí spíš rodinné modely na dovolenou.</p>'
          '<h2>Jak zvolit velikost a nezvolit špatně</h2>'
          '<p>U neoprenových bot platí zásada, že mají přiléhat jako ponožka, ale prsty nesmí zatínat o špičku. Změřte chodidlo večer, kdy je nejširší, a porovnejte s tabulkou. Při velikosti na hranici volte spíš větší, protože ve vodě se noha mírně zmenší a do boty se vejde ještě tenká neoprenová ponožka. V obchodech se objevují označení typu EU 38 nebo velikosti S až L, které se u různých značek liší, proto se vždy řiďte centimetry.</p>'
          '<ol><li>Změřte délku chodidla od paty po nejdelší prst.</li>'
          '<li>Přidejte půl centimetru rezervy na prsty.</li>'
          '<li>Vyberte velikost v tabulce výrobce.</li>'
          '<li>Pokud plánujete tlustší ponožku nebo delší procházky, zvolte o číslo víc.</li>'
          '<li>Po prvním nasazení zkontrolujte, zda pata nesklouzává a zda nic netlačí na kotník.</li></ol>'
          '<h2>Podrážka a přilnavost</h2>'
          '<p>Podrážka je pro bezpečnost rozhodující. Na kamenitém dně potřebujete protiskluzový vzorek a dostatečnou tloušťku, která tlumí tlak ostrých hran. U rodinných dovolených stačí pružná pryž s drobným vzorem, na brodění v řece vyberte pevnější, hrubší vzorek. Tenká podešev pomáhá cítit povrch, ale chrání méně. Boty s ochranou prstů zlepšují bezpečnost při nárazu do skály.</p>'
          '<h2>Kam a na co boty použít</h2>'
          '<ul><li><strong>Moře a skalnatá pláž:</strong> pevnější podešev, uzavřená špička, ideálně neopren s tvrdší podrážkou.</li>'
          '<li><strong>Jezero a písčité dno:</strong> lehká síťka, sandál nebo ponožka.</li>'
          '<li><strong>Paddleboard a kajak:</strong> neopren, který zahřeje nohy a dobře sedí ve stoje.</li>'
          '<li><strong>Brodění a treky u vody:</strong> síťová bota se stabilní podešví, která schne za pochodu.</li>'
          '<li><strong>Bazén a aquapark:</strong> tenké ponožky nebo sandály proti uklouznutí na mokrých dlaždicích.</li></ul>'
          '<p>K výbavě se hodí <a href="/plavky/">plavky</a>, <a href="/neopreny/">neopreny</a>, <a href="/paddleboardy/">paddleboardy</a> a další zboží z kategorie <a href="/vodni-sporty/">vodní sporty</a>. Pro letní chůzi mimo vodu zvažte <a href="/sandaly/">sandály</a> nebo <a href="/pantofle-a-zabky/">pantofle a žabky</a>. Doplňky na pláž najdete v kategorii <a href="/plazove-doplnky/">plážové doplňky</a>.</p>'
          '<h2>Boty do vody a chlad: kdy hřejí a kdy ne</h2>'
          '<p>Neopren hřeje tím, že zadrží tenkou vrstvu vody u kůže, kterou tělo ohřeje. Proto musí bota dobře přiléhat, jinak se voda vyměňuje a zahřátí se neprojeví. U dívek a žen, které rychleji mrznou na chodidlech, je to často hlavní důvod, proč boty do vody vůbec berou. V teplém moři neopren naopak nohy přehřívá, proto se v létě vyplatí lehká síťka nebo tenká ponožka. Na jarní paddleboard a na horské jezero zvolte neopren, který kryje i kotník, aby se studená voda nedostala dovnitř.</p>'
          '<h2>Dámské boty do vody pro dovolenou s rodinou</h2>'
          '<p>Při rodinné dovolené se boty hodí zejména u moře s kamenitým vstupem, v aquaparku nebo na pláži s kamínky, kde se bosky chodí špatně. Praktické jsou modely, které se rychle nazouvají a nemají složité zapínání, protože s dětmi na ruce není čas na tkaničky. Zvolte lehčí podešev, která ve vodě nepřitahuje písek, a barvu, která nevyblednou na slunci. Pokud děláte víc aktivit, jedny sítové boty zvládnou brodění, pláž i krátkou procházku.</p>'
          '<h2>Typické chyby při výběru</h2>'
          '<ul><li><strong>Příliš velká bota:</strong> voda ji vyplavuje a pata sklouzává, takže nohu nechrání, ale zatěžuje.</li>'
          '<li><strong>Příliš tenká podešev:</strong> na ostrých kamenech pomůže jen málo, přestože je pohodlná.</li>'
          '<li><strong>Špatný materiál pro teplotu:</strong> neopren v horkém počasí a síťka ve studené vodě jsou nepohodlné.</li>'
          '<li><strong>Zapomenutá ponožka:</strong> bez ponožky se mohou objevit puchýře, hlavně u hrubší podešve a při delší chůzi.</li>'
          '<li><strong>Uložení vlhkých bot:</strong> zápach a plíseň se vytvoří i za jediný den, proto boty vždy vysušte.</li></ul>'
          '<p>Pro koupání s dětmi a v mělkém moři stačí jednoduchá varianta. Pro paddleboard a brodění vyberte pevnější model s kvalitním uchycením na patě.</p>'
          '<h2>Péče po koupání</h2>'
          '<p>Po použití v moři boty opláchněte sladkou vodou, aby sůl nezanechala skvrny a nepoškodila neopren. Sušte je ve stínu, ne na přímém slunci ani na topení, kde se materiál zkřehne. Ve vlhkých botách nikdy neodkládejte do zavřeného pytle, jinak se objeví zápach. Při delším užívání je občas vyperte rukou v teplé vodě s jemným mýdlem. Neopren neždímejte a nezkrucujte, ztrácí tvar.</p>'
          '<h2>Jak číst nabídky obchodů</h2>'
          '<p>Při porovnání ověřujte materiál a typ boty, velikost v centimetrech a to, zda je boty pro ženy, nebo unisex. Stejné modely se v obchodech prodávají v různých barvách, ale mohou se lišit dostupnými velikostmi. Pokud hodláte boty použít i při delší chůzi, zkontrolujte podešev na fotografii, protože u levnějších modelů bývá tenká.</p>',
    faq=[
        ('Čím se dámské boty do vody liší od pánských?', 'Mají užší střih, užší patu a nižší nárt, aby bota dobře držela na užší noze. Pánské modely jsou širší a objemnější. Pokud máte širší nohu, vyberte unisex nebo pánský model, jinak dámský střih pohodlněji obepne nohu.'),
        ('Jakou velikost vybrat?', 'Změřte chodidlo od paty po nejdelší prst a porovnejte s tabulkou výrobce. U neoprenu volte přiléhavou velikost, u síťových bot a sandálů nechte půl centimetru rezervy. Pokud jste na hranici, vezměte spíš větší.'),
        ('Je lepší neopren, nebo síťka?', 'Neopren hřeje a pevně obepíná, hodí se do chladnější vody a na vodní sporty. Síťka je lehčí a rychleji schne, proto se hodí na brodění a teplé dny. Pro dovolenou u moře stačí obě varianty, zvolte podle teploty vody.'),
        ('Můžu v botách do vody plavat?', 'Ano, jsou na to určené, ale plavání s nimi je pomalejší, protože zvyšují odpor. Pro rekreační plavání jsou vhodné, pro sportovní se hodí tenčí plavecké ponožky. Zvolte pevné přiléhání, aby nesklouzly z paty.'),
        ('Hodí se do moře s ježky?', 'Chrání před ostrými kameny, škeblemi i před nešťastným došlápnutím na ježka, ale jen částečně. Pevnější podešev a vyšší špička zlepšují ochranu. Žádná bota ale nenahradí opatrnost, proto ježky stále obcházejte.'),
        ('Jak boty vyčistit a vysušit?', 'Po koupání v moři opláchněte sladkou vodou, vyperte jemným mýdlem a sušte ve stínu. Nedávejte je na topení ani na přímé slunce, kde se neopren zkřehne. Před uložením nechte úplně vyschnout.'),
        ('Proč mi boty zapáchají?', 'Za zápach může vlhkost a bakterie. Pomůže pravidelné vypláchnutí, důkladné vysušení a občasné vyprání v teplé vodě. Neukládejte je vlhké do zavřeného pytle. Pokud zápach zůstává, použijte jemný dezinfekční prostředek určený pro neopren.'),
        ('Dají se použít jako obuv do bazénu?', 'Ano, tenké ponožky nebo sandály pomáhají proti uklouznutí na mokrých dlaždicích. Pokud ale bazén vyžaduje čistou obuv, ověřte si pravidla provozovatele. Silná neoprenová bota není pro bazén nutná.'),
        ('Jaké boty zvolit na paddleboard?', 'Neoprenovou botu s ohebnou podrážkou, která dobře drží na desce a zahřeje při studené vodě. Přesná velikost je důležitá, aby se noha nepohybovala. Pro teplé dny postačí síťová bota nebo ponožka, když je voda příjemná.'),
        ('Mohu boty použít i na procházku?', 'Krátkou chůzi po pláži nebo pobřeží zvládnou, ale delší procházky po asfaltu nejsou pro tenkou podrážku ideální. Pro delší pěší túry použijte turistickou obuv a boty do vody si nechte jen na vodu.'),
    ])

# ------------------------------------------------------------------ speedo-plavky
NEW['speedo-plavky'] = dict(
    title='Speedo plavky: sortiment, střihy a výběr podle plavání',
    desc='Speedo plavky pro dámy, pány i děti: sportovní kostýmy, jammery, aquashorty a plážové kraťasy. Střihy, velikosti D a péče o chlór. Srovnání obchodů.',
    intro='<p>Speedo je britská značka s australskými kořeny, která se od začátku zaměřuje na plavání. V nabídce srovnávače najdete sportovní jednodílné kostýmy pro dámy, jammery a aquashorty pro muže, závodní startovní obleky i plážové kraťasy a modely pro děti. Rozdíl oproti módním plavkám je v materiálu a střihu: sportovní Speedo se šije pro pravidelný pohyb ve vodě a snáší chlór lépe než běžné pláže. '
          'Tato stránka vybírá z kategorie <a href="/plavky/">plavky</a> jen produkty této značky. Průvodce ukazuje, jak poznat jednotlivé střihy, jak číst velikosti typu D a rozměry v palcích, co rozhoduje při volbě pro bazén nebo moře a jak plavky ošetřovat. Hledáte-li jinou značku, srovnejte i <a href="/arena-plavky/">plavky Arena</a>, <a href="/plavky-nike/">plavky Nike</a> a <a href="/plavky-adidas/">plavky Adidas</a>.</p>',
    guide='<h2>Co Speedo nabízí a jak se střihy liší</h2>'
          '<p>V sortimentu se opakují tři skupiny: tréninkové a závodní plavky, plážové a volnočasové modely a dětské kolekce. Dámské plavky mají podobu jednodílných kostýmů s různým zády, například racerback, thinstrap nebo leaderback, a také modelů s vyšším krytím, jako je modest. Pánské najdete jako jammery, aquashorty, slipy a kraťasy. Závodní startovní obleky patří do zvláštní skupiny pro soutěžní plavce.</p>'
          + T(['Střih', 'Pro koho', 'Charakteristika'], [
              ['Jednodílný kostým s úzkými ramínky (thinstrap)', 'rekreační a trénující plavkyně', 'lehký, volnější záda, snadno se obléká'],
              ['Racerback / leaderback', 'pravidelné plavání', 'záda tvaru písmene Y, ramínka se nesesouvají při tempu'],
              ['Modest (dlouhé nebo kryté)', 'ty, kdo preferují vyšší krytí', 'delší nohavice nebo rukávy, odolné materiály'],
              ['Aquashort', 'muži, tréninky i kondiční plavání', 'kratší nohavice, přiléhavý, pružný'],
              ['Jammer', 'sportovní plavci', 'nohavice po kolena, nižší odpor ve vodě'],
              ['Slip (brief)', 'závodní a rychlostní plavání', 'minimum látky, nutná jistota střihu'],
              ['Plážové kraťasy (watershort)', 'dovolená a volný čas', 'volnější střih, rychleschnoucí, často se vzory']]) +
          '<p>Rozhodněte se, jak často budete plavky nosit v chlorované vodě. Pro pravidelný trénink volte sportovní střihy z materiálu odolného chlóru, pro dovolenou stačí pláž. Střih také ovlivní pohodlí při plavání: pevné záda drží ramínka, širší nohavice šustí a zpomalují.</p>'
          '<h2>Materiály a odolnost proti chlóru</h2>'
          '<p>Většina sportovních plavek značky je z polyesterových nebo elastanových směsí, které lépe odolávají chlóru než čisté polyamidové materiály. Odolnost se v nabídce často značí v názvu řady, například Endurance nebo Eco Endurance+ u trvanlivějších modelů. Při častém plavání je tato volba rozumná, protože běžné plavky z chlóru rychle zešednou a ztratí pružnost. Modely s přídavkem recyklovaného materiálu se v názvu označují jako Eco.</p>'
          '<ul><li><strong>Polyesterová směs:</strong> vhodná pro bazén, drží barvu i tvar.</li>'
          '<li><strong>Polyamid a elastan:</strong> měkčí na dotek, pohodlný pro pláž.</li>'
          '<li><strong>Zesílené švy:</strong> důležité u plavek, které se často natahují.</li>'
          '<li><strong>Podšívka:</strong> u světlých barev zajišťuje neprůhlednost.</li>'
          '<li><strong>Rychlé schnutí:</strong> praktické u kraťasů a plážových modelů.</li></ul>'
          '<h2>Jak číst velikosti</h2>'
          '<p>Speedo u dámských a dětských plavek často používá označení D a číslo, například D2, D3 nebo D4, které odpovídají velikostem v britském pojetí. U pánských kraťasů a jammerů se používá číslo v centimetrech nebo palcích. U plážových šortek se uvádí délka nohavice v palcích, třeba 16" nebo 20". Vždy se proto řiďte tabulkou konkrétní značky, ne pocitem z jiného výrobce.</p>'
          + T(['Označení', 'Kde se objevuje', 'Co udělat'], [
              ['D2, D3, D4 …', 'dámské a dětské kostýmy', 'změřte hrudník a boky a vyberte v tabulce'],
              ['Velikost pasu v cm', 'pánské jammery a aquashorty', 'změřte pas, zvolte rovnou, ne o číslo větší'],
              ['Délka v palcích (16", 20")', 'plážové šortky', 'vyberte podle toho, jak dlouhé nohavice chcete'],
              ['Roky nebo výška', 'dětské modely', 'ověřte výšku, ne jen věk, děti rostou nerovnoměrně'],
              ['XS–XL', 'plážové modely a trička', 'ověřte tabulku, nesedí vždy jako ostatní značky']]) +
          '<p>Při pochybnostech zvolte menší velikost u sportovních kostýmů, které se po namočení lehce natáhnou, a větší u plážových šortek. Nejlepší cesta je vzít si metr a porovnat míry s tabulkou prodejce.</p>'
          '<h2>Plavky pro ženy</h2>'
          '<p>Dámské plavky Speedo najdete v kategorii <a href="/damske-plavky/">dámské plavky</a>. Pro pravidelný trénink se osvědčují jednodílné kostýmy s vyztuženými ramínky a zády tvaru Y, které nesklouzávají při tempu. Pro lehčí použití se hodí thinstrap, pro vyšší krytí modest. Při výběru barvy zvažte, že tmavé a jednobarevné plavky lépe odolávají chlóru, zatímco světlé vzory rychle blednou.</p>'
          '<h2>Plavky pro muže</h2>'
          '<p>V kategorii <a href="/panske-plavky/">pánské plavky</a> najdete jammery, aquashorty a kraťasy. Aquashort a jammer volte pro trénink, protože neplandá a nezpomaluje. Plážové watershorty jsou volnější a hodí se spíš k vodě na dovolené. Slipy zvolte spíš pro závodní plavání než pro rodinný bazén. Pozor na to, že plavky s vyšším obsahem elastanu po letech ztrácejí tvar.</p>'
          '<h2>Plavky pro děti</h2>'
          '<p>Dětské Speedo najdete v kategorii <a href="/detske-plavky/">dětské plavky</a>. U dívek jde o jednodílné i dvoudílné modely, u chlapců o kraťasy do vody nebo závodní jammery. Při výběru sledujte výšku dítěte a nechte rezervu na růst, ale plavky nesmí viset, jinak se ve vodě zvedají. Pro malé děti se hodí snadné oblékání a měkké švy bez štítků.</p>'
          '<h2>Startovní obleky a trénink</h2>'
          '<p>Závodní obleky se šijí z velmi pevného materiálu a jejich oblékání trvá déle než u běžných plavek. Hodí se jen pro soutěže, ne pro každodenní plavání, protože jsou méně pohodlné a jejich životnost je omezená. Pro trénink zvolte běžný sportovní kostým nebo jammer. Pro plavce jsou užitečné i <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-cepice/">plavecké čepice</a> a <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>'
          '<h2>Speedo pro bazén, moře a otevřenou vodu</h2>'
          '<p>V bazénu rozhoduje odolnost proti chlóru a přiléhavost: plavky nesmí plandat ani se při odrazu od stěny posouvat. V moři a na dovolené vítězí pohodlí, rychlé schnutí a odolnost vůči soli a slunci, takže se vyplatí plážové šortky nebo kostým s příjemnějším materiálem. V otevřené vodě a při triatlonu se hodí pevné plavky s pevnými švy, které při delším plavání nedřou. Stejný model nemusí být ideální pro všechny tři prostředí, proto si předem ujasněte, kde ho budete nosit nejčastěji.</p>'
          '<h2>Jak Speedo srovnat s jinými značkami</h2>'
          '<p>Speedo je v kategorii plavky jednou z nejznámějších značek zaměřených na plavání. Podobně sportovně se profiluje i Arena, kdežto <a href="/znacka/nike/">Nike</a> a <a href="/znacka/adidas/">Adidas</a> kombinují plavecký střih se sportovním designem. Rozdíly se nejvíc projeví na střihu a velikostech: u jedné značky sedí kostým volněji, u jiné je užší v ramenou. Pokud už máte ověřenou značku, zůstaňte u ní, jinak porovnejte tabulky velikostí a materiál. Při výběru se řiďte tím, na co budete plavky používat, a ne jen znalostí značky.</p>'
          '<h2>Jak plavky zkoušet a poznat správný střih</h2>'
          '<p>Správně sedící sportovní plavky přiléhají k tělu bez záhybů, nikde netlačí a při předklonu či zvednutí paží nesklouzávají. Ramínka mají zůstat na ramenou i při tempu, nohavice se nesmějí vhoupat ani zařezávat do stehen. Pokud je nezkoušíte osobně, ověřte výrobcovu tabulku a podívejte se na délku střihu u konkrétního modelu. Po prvním namočení se elastické materiály lehce uvolní, takže mírná těsnost v suchém stavu je v pořádku. Naopak záhyby na zádech nebo mezera u hrudi signalizují, že je velikost příliš velká.</p>'
          '<h2>Péče, aby plavky vydržely</h2>'
          '<p>Po plavání plavky opláchněte sladkou vodou, aby chlór a sůl nepoškozovaly vlákna. Perte je ručně nebo na šetrný program bez aviváže a nikdy je nesušte na topení ani v sušičce. Nemačkejte je a nekruťte. Plavky střídejte, pokud plavete často, aby se elastan mohl zotavit. Zapomenuté mokré plavky v tašce plesniví, takže je hned po plavání vyndejte.</p>'
          '<h2>Jak porovnat nabídky Speedo</h2>'
          '<p>Stejný model se v obchodech liší dostupnými velikostmi a barvami. Ověřte, zda jde o aktuální kolekci, nebo starší kus, a kolik velikostí zbývá. Pozor na zaměnitelná jména, třeba Endurance, Eco Endurance+ nebo Medalist: každé označuje trochu jiný materiál a střih. K doplnění letní výbavy se hodí také <a href="/plazove-doplnky/">plážové doplňky</a> a <a href="/vodni-sporty/">vodní sporty</a>.</p>',
    faq=[
        ('Čím se Speedo liší od běžných plavek?', 'Je to značka zaměřená na plavání, takže sportovní modely mají střih pro pohyb ve vodě a materiály odolnější chlóru. Běžné módní plavky jsou určené spíš na pláž a rychleji zešednou nebo ztratí tvar při pravidelném bazénu.'),
        ('Jaké střihy Speedo nabízí?', 'Dámy najdou jednodílné kostýmy, například racerback, thinstrap nebo modest, páni jammery, aquashorty, slipy a kraťasy. Děti mají kostýmy i kraťasy. K tomu přibývají plážové modely a závodní startovní obleky.'),
        ('Co znamená označení D2, D3, D4?', 'Jde o velikosti používané u dámských a dětských plavek, které odpovídají britskému označení. Číslo je potřeba vyhledat v tabulce konkrétního modelu, protože se mezi řadami může lišit. Změřte hrudník a boky a porovnejte s tabulkou.'),
        ('Jak vybrat velikost pánských jammerů?', 'Změřte pas a porovnejte s tabulkou výrobce. Jammer by měl přiléhat, ale nesmí tlačit nebo se zařezávat. Pokud jste na hranici, zvolte spíš menší velikost, protože se po namočení trochu uvolní.'),
        ('Co je aquashort?', 'Je to přiléhavé pánské plavky s kratšími nohavicemi než jammer. Hodí se pro trénink, kondiční plavání i aquaerobik. Díky přiléhavému střihu klade menší odpor než volné kraťasy.'),
        ('Jak dlouho Speedo plavky vydrží?', 'Při pravidelném používání v bazénu vydrží sportovní plavky obvykle několik měsíců až rok, záleží na četnosti a péči. Střídejte páry, oplachujte je po plavání a nesušte na topení, tím trvanlivost výrazně prodloužíte.'),
        ('Jak perou plavky Speedo?', 'Po koupání opláchněte sladkou vodou, ručně vyperte v chladné vodě s jemným mýdlem a nechte oschnout ve stínu. Nepoužívejte aviváž, bělidlo ani sušičku, ničí elastan. Plavky nežmoulejte, jen opatrně vymačkejte.'),
        ('Hodí se Speedo i na pláž?', 'Ano, pro pláž a vodní zábavu jsou ideální plážové šortky nebo kostýmy se vzory. Sportovní kostým je také použitelný, ale má méně módní střih. Pro delší pobyt na slunci zvažte i model s vyšším krytím.'),
        ('Co jsou startovní obleky Speedo?', 'Je to závodní plavecký oblek z pevného, málo propustného materiálu, určený pro soutěže. Oblékání trvá déle, oblek je méně pohodlný a rychleji se opotřebuje. Pro trénink a rekreační plavání se nehodí.'),
        ('Jaké plavky zvolit pro dítě?', 'Dívkám se hodí jednodílné nebo dvoudílné kostýmy, chlapcům kraťasy nebo jammer. Vybírejte podle výšky dítěte a nechte menší rezervu na růst. U malých dětí sledujte měkké švy, snadné oblékání a pevné gumy.'),
    ])
