"""sporteka.cz — wave 19e (4. 11. 2026): long texts (>= 1650 words) for cyklisticke-bundy-a-vesty, holinky, aminokyseliny-bcaa, kempingove-doplnky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklisticke-bundy-a-vesty
NEW['cyklisticke-bundy-a-vesty'] = dict(long=True,
    title='Cyklistické bundy a vesty: výběr podle počasí',
    desc='Cyklistické bundy, větrovky, vesty a pláštěnky pro silnici, MTB i město. Jak vybrat střih, membránu, větrání a velikost a porovnat nabídky obchodů.',
    intro='<p>Na kole se počasí chová jinak než při chůzi. Jedete-li třicet kilometrů v hodině, vítr proti hrudi ochladí tělo víc než teplota vzduchu, a po sjezdu z kopce se zpocená záda promění v mokrý obklad. '
          'Cyklistická bunda nebo vesta proto řeší dvě věci zároveň: zastaví proud vzduchu a odvede vlhkost zevnitř ven. Dobrý kus se v kapse dresu srolovaný ztratí a na kopci se dá během pár vteřin sundat.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u bund a vest značek jako Rockbros, Silvini, Siroko, Northwave nebo Craft. '
          'Do kompletního oblečení patří také <a href="/cyklisticke-dresy/">cyklistické dresy</a>, <a href="/cyklisticke-navleky/">návleky</a>, <a href="/cyklisticke-rukavice/">rukavice</a> a <a href="/cyklisticke-kratasy-a-kalhoty/">kalhoty</a>. '
          'Následující průvodce vysvětluje rozdíl mezi typy, materiály, střihem i péčí.</p>',
    guide='<h2>Bunda, vesta nebo pláštěnka: co se k čemu hodí</h2>'
          '<p>Než začnete porovnávat značky, ujasněte si, proti čemu se chcete bránit. Vítr, chladné ráno, studený déšť a hustý liják jsou čtyři různé problémy a každý z nich řeší jiný kus oděvu. '
          'Jeden univerzální kabát neexistuje: ten, který vydrží celodenní déšť, bývá nepříjemně horký, a ten, který dobře dýchá, propustí první průtrž.</p>'
          + T(['Typ oděvu', 'Hlavní úkol', 'Typická situace'], [
              ['Větrovka', 'zastaví proud vzduchu, váží velmi málo', 'sjezdy, chladné ráno, přechodné období'],
              ['Vesta', 'chrání trup, ruce zůstávají volné', 'jarní a podzimní vyjížďky, intenzivní tempo'],
              ['Softshellová bunda', 'větruodolná a mírně vodoodpudivá, pružná', 'chladné dny bez trvalého deště'],
              ['Nepromokavá bunda s membránou', 'drží vodu venku, vlhkost pouští ven', 'delší déšť, dojíždění do práce'],
              ['Zateplená bunda', 'izoluje a brání větru', 'zimní jízda při nízkých teplotách'],
              ['Pláštěnka', 'rychlá bariéra proti dešti', 'záloha v zadní kapse, městská jízda']]) +
          '<p>Pokud zatím neznáte obecné rozdíly mezi látkami, podívejte se i na kategorie <a href="/vetrovky/">větrovky</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/nepromokave-bundy/">nepromokavé bundy</a>. '
          'Cyklistické kousky se od nich liší střihem a detaily, které zmíníme níže, ale materiálová logika je stejná.</p>'
          '<h2>Větrovka: lehká ochrana před větrem</h2>'
          '<p>Tenká větrovka je nejuniverzálnější vrstva do batohu nebo kapsy. Její úkol není hřát, ale zastavit vítr, který jinak proniká dresem jako sítem. Většina modelů používá hustě tkaný syntetický materiál, často s úpravou proti slabému dešti. '
          'Zadní záda bývají tvarovaná do špičky, aby při předklonu kryla bedra, a zip jde zvednout do výšky brady. Mnoho kousků má na zádech perforaci nebo síťovinu, která pomáhá odvádět páru, protože úplně neprodyšný materiál by uvnitř vytvořil sauna efekt.</p>'
          '<p>Při výběru sledujte hlavně sbalitelnost. Dobrá větrovka se vejde do dlaně a nevadí v zadní kapse dresu. Pak ji vozíte vždy a nemusíte pak před vyjížďkou rozhodovat, zda se vám bude hodit.</p>'
          '<h2>Vesta: když stačí chránit jen trup</h2>'
          '<p>Vesta je oblíbená u silničářů a gravelistů, protože chrání ten díl těla, který je při jízdě proti větru nejvíc vystavený, a nenarušuje volnost paží. Jednoduchá větrovková vesta má vpředu větruodolný panel a vzadu prodyšnou síťku, takže pára uniká. '
          'Ruce se tak nepřehřívají a při tempu se dá vesta rozepnout bez zastavení. Zdatnější modely se vejdou do kapsy dresu a v kopci se sundají jednou rukou.</p>'
          '<p>Variantou jsou zateplené vesty s lehkou výplní nebo fleecovým zadním dílem. Hodí se na podzimní odpoledne, kdy ráno mrzlo a odpoledne svítí slunce. Pokud jezdíte po městě, hledejte reflexní prvky a delší záda, která překryjí sedlo a zabrání mokrému pruhu na kalhotách.</p>'
          '<h2>Nepromokavé bundy: membrána a švy</h2>'
          '<p>U bund proti dešti rozhoduje to, jak výrobce spojí látku a membránu. Dvouvrstvé a třívrstvé konstrukce se liší tím, kde je membrána chráněna před otěrem. Švy musí být zalepené, jinak voda proteče právě tudy. '
          'Vodní sloupec se uvádí v milimetrech a vyjadřuje odolnost proti tlaku vody, prodyšnost se udává v gramech vodní páry za den. Čísla jednotlivých výrobců ale nejdou vždy přesně porovnat, protože se měří odlišnými metodami, a proto se hodí spíš jako hrubý orientační údaj.</p>'
          '<p>Nepromokavý oděv nikdy neodvede úplně všechno. Při intenzivním tempu se pod ním zpotíte a zvlhnete zevnitř. Pomáhá větrání pod pažemi, výklopná záda a možnost otevřít zip. Pokud hledáte kompromis, vybírejte lehkou membránu s vyšší prodyšností a počítejte s tím, že při bouři budete mokří i zevnitř.</p>'
          '<h2>Střih: proč cyklistická bunda nevypadá jako turistická</h2>'
          '<p>Rozdíl se pozná hned v nastavení těla. Rukávy jsou delší, aby v předklonu nepodjížděly k loktům, záda se táhnou níž, přední díl je kratší, aby se nesbíral na břiše, a límec bývá nízký, aby neškrtil při pohledu dopředu. '
          'Bunda, která při stání vypadá divně, na kole sedí přesně. Opačně to platí pro volný turistický střih: nad řídítky se nafoukne a vlaje.</p>'
          + T(['Detail střihu', 'Proč na něm záleží'], [
              ['Prodloužená záda', 'kryjí bedra a spodní část zad v předklonu'],
              ['Delší rukávy s manžetou', 'zakrývají zápěstí mezi rukavicí a rukávem'],
              ['Zadní kapsy', 'unesou lahev, mapu nebo svačinu bez batohu'],
              ['Reflexní prvky', 'zlepšují viditelnost za šera a v dešti'],
              ['Zip s krytkou', 'netlačí do brady a brání pronikání vody'],
              ['Větrací otvory', 'umožňují snížit teplotu bez svlékání']]) +
          '<h2>Velikost a vrstvení</h2>'
          '<p>Cyklistická bunda má sedět přiléhavěji než městská. Příliš volná plácá a zvyšuje odpor vzduchu, příliš těsná omezuje dýchání a pohyb ramen. '
          'Vyzkoušejte ji v předklonu, jako byste drželi řídítka: rukávy mají sahat ke kloubům prstů, záda krýt kříž a zip nesmí tlačit. Pamatujte, že pod bundou bude funkční vrstva, případně <a href="/funkcni-tricka/">funkční tričko</a>, <a href="/merino-tricka/">merino triko</a> nebo <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<p>Klasické pravidlo tří vrstev platí i na kole. První vrstva odvádí pot, druhá izoluje a třetí chrání před větrem a deštěm. Díky tomu můžete podle teploty měnit jednotlivé díly, aniž byste museli kupovat ten nejtlustší kus. '
          'V zimě se vyplatí zateplená vesta nebo bunda s fleecovým zadním dílem, kdežto v létě stačí lehká větrovka v kapse.</p>'
          '<h2>Podle sportu: silnice, MTB, gravel a město</h2>'
          '<h3>Silniční kolo</h3>'
          '<p>Rychlé tempo a aerodynamická poloha vyžadují přiléhavý střih, zadní prodlouženou část a minimum látky. Hodí se lehká větrovka nebo vesta, kterou lze sbalit do zadní kapsy dresu. U delších výjezdů se počítá s nepromokavou vrstvou jako rezervou.</p>'
          '<h3>Horské kolo</h3>'
          '<p>V terénu je důležitější odolnost proti ostružiní a otěru a také větrání při výstupech. MTB bundy mívají zpevněná ramena, větší pohybový prostor a kapuci kompatibilní s přilbou. Kapuce se přitom má dát zafixovat, aby při jízdě nevlála. K ochraně těla se hodí i <a href="/cyklo-chranice/">cyklistické chrániče</a>.</p>'
          '<h3>Gravel a dlouhé výlety</h3>'
          '<p>Gravelisté potřebují obojí: prodyšnost pro rychlé úseky a spolehlivou ochranu na dlouhé dny. Dobře se osvědčí lehká nepromokavá bunda s větracími otvory, ke které se v kapse najde ještě tenká vesta.</p>'
          '<h3>Město a dojíždění</h3>'
          '<p>Při dojíždění do práce počítejte s tím, že na vás budou lidé koukat i mimo kolo. Bundy s decentním střihem, zakrytými reflexními prvky a delšími zády vypadají normálně v kanceláři a na kole splní svou funkci. Pro městskou jízdu je dobré mít k dispozici svítící prvky a <a href="/cyklo-svetla/">světla na kolo</a>.</p>'
          '<h2>Viditelnost a bezpečnost</h2>'
          '<p>Za šera pomáhají světlé a reflexní materiály, ale nenahradí světla. Nejlépe fungují reflexní plochy na pohybujících se částech těla, tedy na ramenou, loktech a lýtkách. Silné reflexní pásky na zádech jsou dobře vidět zezadu, ale zboku jen málo. '
          'Světlé barvy, jako žlutá nebo oranžová, zlepšují orientaci řidičů ve dne. Černé a tmavé modely vypadají elegantně, ale za šera je potřebujete doplnit odrazkami.</p>'
          '<h2>Co s bundou v kapse: sbalitelnost a doplňky</h2>'
          '<p>Při výběru počítejte s tím, kam bunda půjde, když zrovna nesvítí vítr. Lehčí modely mají sáček nebo kapsu, do které se dají sbalit, těžší kusy se hodí spíš do brašny nebo na řidítka. Pro vození většího množství vrstev se hodí <a href="/cyklo-tasky-a-nosice/">cyklistické brašny a nosiče</a>. '
          'K ochraně hlavy, očí a rukou nezapomeňte na <a href="/cyklisticke-helmy/">přilbu</a>, <a href="/cyklisticke-bryle/">brýle</a> a rukavice. Do chladu přibývá i <a href="/cyklisticke-ponozky/">ponožka</a>, <a href="/cyklisticka-obuv/">obuv</a> a návlek na boty.</p>'
          '<h2>Péče o cyklistické bundy</h2>'
          '<p>Pot, bláto a sunscreen zanášejí póry membrány, takže se časem snižuje její prodyšnost. Perte podle štítku, ideálně s jemným prostředkem bez aviváže, která vodoodpudivou úpravu zalepí. Teplo, například krátké vysušení v sušičce při nízké teplotě, impregnaci často oživí, ale použijte ho jen tehdy, když to štítek výrobce povoluje; žehlení membrány raději vynechte. '
          'Až voda přestane vytvářet kapky, obnovte úpravu sprejem nebo prostředkem do pračky. Zip občas opláchněte a lehce namažte voskem. Bundu skladujte suchou a nezmačkanou, jinak se vytvářejí trvalé záhyby, ve kterých materiál rychleji stárne.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul>'
          '<li>Koupě nepromokavé bundy bez větrání. Po hodině jízdy se zpotíte i bez deště.</li>'
          '<li>Příliš velká velikost „aby se tam vešlo víc vrstev“. Pak bunda plácá a nafukuje se větrem.</li>'
          '<li>Ignorování délky zad. Krátká záda znamenají studená bedra a mokrý pruh po dešti.</li>'
          '<li>Výběr tmavé barvy bez reflexních prvků na silnici.</li>'
          '<li>Praní s aviváží, které poškodí membránu i vodoodpudivou povrchovou úpravu.</li>'
          '<li>Očekávání, že jedna bunda zvládne zimu i léto. Praktičtější je kombinovat tenkou vrstvu s teplejší.</li>'
          '</ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Každý produkt má stránku s nabídkami obchodů. Porovnáte dostupnost velikostí, dopravu a možnosti vrácení zboží. Při řešení, zda objednat dvě velikosti a jednu vrátit, se nejdřív podívejte na tabulku výrobce a přeměřte hrudník i délku paže. '
          'Značky se liší střihem: <strong>Silvini</strong> a <strong>Craft</strong> bývají přiléhavější, <strong>Rockbros</strong> často univerzálnější, kdežto <strong>Kilpi</strong> a <strong>Rockrider</strong> myslí na turisty a rekreační jezdce. Novinky a slevy se obměňují, takže stojí za to jednou za čas zkontrolovat i kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a hlavní rozcestník <a href="/cyklistika/">cyklistika</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi cyklistickou větrovkou a nepromokavou bundou?',
         'Větrovka zastaví proud vzduchu a bývá velmi lehká, ale déšť propustí nebo ho odolá jen krátce. Nepromokavá bunda má membránu a zalepené švy, takže drží vodu venku, je však těžší, dražší na výrobu a při tempu méně prodyšná. Na jarní a podzimní vyjížďky bývá praktická větrovka, na delší déšť nepromokavá vrstva.'),
        ('Je lepší vesta, nebo bunda?',
         'Vesta chrání trup a nechává ruce volné, takže se hodí pro mírně chladné dny a rychlé tempo. Bunda s rukávy kryje i paže a hodí se při nižší teplotě nebo větru. Hodně jezdců vozí vestu v kapse a rukávy doplňují návleky, které lze během jízdy sundat.'),
        ('Jak poznám, že mi cyklistická bunda sedí?',
         'Zaujměte předklon, jako byste drželi řídítka. Rukávy mají sahat ke kloubům prstů, záda mají zakrývat kříž a zip nesmí škrtit krk ani tlačit na břicho. Pod bundou se musí vejít funkční vrstva, ale látka se nemá nafukovat větrem.'),
        ('Dá se nepromokavá bunda prát?',
         'Ano, a je to dokonce žádoucí. Pot a nečistoty ucpávají membránu, a tím snižují prodyšnost. Perte jemným prostředkem bez aviváže podle štítku. Po vyprání se vodoodpudivá úprava často obnoví teplem, a když přestanou vznikat kapky, použijte impregnační prostředek.'),
        ('Co znamená vodní sloupec u bund?',
         'Je to údaj o tlaku vody, který látka vydrží, než začne propouštět, udávaný v milimetrech. Vyšší číslo značí větší odolnost, ale výrobci měří různě, takže jde spíš o hrubé vodítko. Důležitější než samotné číslo je kvalita zalepených švů a zipů.'),
        ('Jak se oblékat na kolo, když je zima?',
         'Funguje systém tří vrstev: funkční spodní prádlo, izolační střední vrstva a větruodolná vnější vrstva. Prsty, uši a chodidla chladnou první, takže se vyplatí rukavice, čepice pod helmu a návleky na boty. Raději začněte s mírným pocitem chladu, protože po pár minutách jízdy se tělo zahřeje.'),
        ('Proč mají cyklistické bundy delší záda?',
         'V předklonu se standardní bunda vyhrne a odhalí bedra. Delší záda zakryjí spodní část zad, brání chladu a při dešti zastaví stříkající vodu od zadního kola. Z toho důvodu se cyklistické kousky při stání tváří zvláštně, ale na kole sedí.'),
        ('Hodí se cyklistická bunda i na běh nebo turistiku?',
         'Lehká větrovka bez těžké izolace poslouží i při běhu, jen mívá střih přizpůsobený předklonu a kapsy na zádech nemusí vyhovovat. Při turistice si všímejte, že přiléhavý střih omezí oblékání dalších vrstev. Pro univerzální použití je pohodlnější klasická outdoorová bunda.'),
        ('Na co si dát pozor při koupi bundy do deště na kolo?',
         'Sledujte zalepené švy, kvalitu zipu a možnost větrání pod pažemi nebo na zádech. Kapuce musí jít zafixovat, aby nevlála, a pod helmu se má vejít. Pamatujte, že žádná membrána neodvede všechen pot při intenzivní jízdě, takže vždy počítejte s určitým zvlhnutím zevnitř.'),
        ('Jak velkou bundu mám objednat?',
         'Změřte obvod hrudníku, pasu a délku paže a porovnejte s tabulkou výrobce, protože střih se liší značku od značky. Pokud váháte mezi dvěma velikostmi, zkuste menší s lepším sedem v předklonu, ale jen pokud ji lze pohodlně zapnout. Zkontrolujte u obchodu podmínky vrácení.'),
    ])

# ------------------------------------------------------------------ holinky
NEW['holinky'] = dict(long=True,
    title='Holínky: dětské, dámské a pánské, jak vybrat',
    desc='Gumové a neoprenové holínky pro děti, ženy i muže. Jak zvolit velikost, výšku, podšívku a podrážku a kde porovnat nabídky českých obchodů.',
    intro='<p>Holínka je nejjednodušší způsob, jak mít suché nohy v blátě, trávě nebo na rybářském břehu. Základ je nepropustný materiál, který se dá opláchnout hadicí, a podrážka s dezénem, který se v louži nesklouzne. '
          'Rozdíly mezi jednotlivými páry jsou ale větší, než se zdá: odlišně se chovají lehké gumové boty pro školku, vysoké neoprenové boty pro rybáře i módní modely na festival.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů u holínek značek Viking, Mikado, Delphin, Crocs, Regatta, Reima nebo Helly Hansen. Pro přechodné počasí se hodí také <a href="/nepromokave-bundy/">nepromokavé bundy</a>, <a href="/plastenky/">pláštěnky</a> a <a href="/kombinezy/">kombinézy</a>, pro dlouhé procházky <a href="/trekova-obuv/">trekové boty</a>. '
          'Průvodce níže popisuje materiály, velikosti, podšívky a péči o boty.</p>',
    guide='<h2>Z čeho se holínky vyrábějí</h2>'
          '<p>Klasická holínka je z přírodní nebo syntetické pryže, která se vulkanizuje do jednoho dílu. Díky tomu nemá švy, kterými by mohla vniknout voda. Lehčí modely se vyrábějí z PVC nebo z pěnových polymerů, které mají menší hmotnost, ale na mrazu tvrdnou. '
          'Neoprenové holínky mají textilní podšívku z pěnové gumy, která izoluje a drží nohu v teple, a hodí se do chladna a na vodu. Gumové boty bez podšívky jsou rychle k vysušení, ale v zimě studí.</p>'
          + T(['Materiál', 'Výhoda', 'Omezení'], [
              ['Přírodní kaučuk', 'pružný, odolný, příjemný na dotek', 'těžší, na UV záření časem praská'],
              ['PVC', 'nízká hmotnost, snadná údržba', 'za mrazu tvrdne a může praskat'],
              ['Neopren', 'izoluje a drží teplo', 'pomalu schne, hůř se čistí uvnitř'],
              ['Pěnové polymery', 'velmi lehké, pohodlné', 'rychleji se obrušují a méně chrání proti propíchnutí'],
              ['Textilní podšívka', 'příjemné na nohu a pohlcuje pot', 'musí se po použití vysušit']]) +
          '<h2>Výška svršku: kotníkové, střední a vysoké</h2>'
          '<p>Výška rozhoduje o tom, jak hluboko můžete stát ve vodě. Kotníkové modely jsou praktické v lehkém dešti a v městských kalužích, střední holínky ke lýtku se hodí do zahrady a na louku, vysoké boty po kolena zvládnou rybářský břeh nebo bahnitý les. '
          'Příliš vysoká holínka se při chůzi otírá o lýtko, příliš nízká nechá vodu vniknout přes okraj. Při volbě se zeptejte, kolik času strávíte přímo ve vodě a jak vysoká je tráva nebo sníh.</p>'
          '<h2>Velikost: jak sedí holínky</h2>'
          '<p>Holínky nemají šněrování ani zip, a proto nesmějí být příliš velké. Nohu drží jen pata a výška svršku. Když je velikost větší, pata se zvedá, prsty narážejí do špičky a chůze se mění v klouzání. U dospělých se doporučuje zkoušet je s ponožkou, kterou budete nosit. '
          'U modelů s podšívkou počítejte s tím, že boty budou o něco těsnější než gumový základ. Neopren se časem lehce ustálí a přizpůsobí tvaru nohy.</p>'
          '<p>Měřicí tabulka výrobce je vždy lepší než odhad podle běžné obuvi, protože každá firma používá jiné kopyto. Širší lýtko vyžaduje model s rozšířenou holení, jinak se holínka nasazuje s námahou. Objevují se i varianty se stahovacími šňůrkami nebo přezkami v horní části, které přizpůsobí obvod.</p>'
          '<h2>Dětské holínky</h2>'
          '<p>Děti rostou rychle a holínky jsou jeden z mála kusů obuvi, které je rozumné kupovat s malou rezervou. Mezera 1 až 1,5 cm před palcem stačí, víc je na škodu, protože dítě klopýtá. Dobré dětské modely jsou lehké, protože dětská noha nemá sílu zvedat těžké boty. '
          'Hledejte široký otvor s ouškami pro snadné obouvání, protože samostatné oblékání vyžaduje trénink. Reflexní prvky pomáhají za šera cestou ze školky, kdežto vyjímatelná vložka usnadní sušení. Značky jako Reima, Viking, Crocs nebo Coqui mají velkou nabídku dětských barev a motivů.</p>'
          '<p>K dešti dětem poslouží pláštěnka nebo nepromokavá kombinéza, ke které holínky dobře sedí. Zimní modely s teplou podšívkou nahrazují zimní obuv jen při krátkém pobytu venku. Při delší chůzi po sněhu je lepší <a href="/snezky/">sněhule</a>.</p>'
          '<h2>Dámské a pánské holínky</h2>'
          '<p>Dámské modely mají užší patu a štíhlejší lýtko, často se nabízejí v módních vzorech a barvách a hodí se do města, na festival nebo na procházku se psem. Pánské holínky mají širší kopyto a většinou robustnější podrážku. '
          'Pracovní holínky se specializují: někdy mají ocelovou špičku a stélku proti propíchnutí, což se hodí na stavbu a ve stájích. Pro zahradu, práci s dobytkem nebo lov je důležitá odolnost materiálu proti oděru a chemikáliím. Ve stájích se kromě <a href="/jezdecka-obuv/">jezdecké obuvi</a> používají i hrubší gumové boty.</p>'
          '<h2>Podrážka a dezén</h2>'
          '<p>Podrážka určuje, jestli se při chůzi po blátě udržíte na nohou. Hluboký hrubý dezén dobře drží v blátě a trávě, ale na hladké dlažbě je méně stabilní. Hladší podrážka je lepší na rybářské lodi a v domě, kde nechcete zanášet nečistoty. '
          'Samočisticí dezén vyplivne bláto, aby se nehromadilo pod nohou. U lodí a sklouzávajících povrchů hledejte jemnější vzor s širokým kontaktem. Na ledu a ve sněhu žádná běžná holínka nemá dobrý záběr, a proto zvažte <a href="/nesmeky/">nesmeky</a>.</p>'
          '<h2>Teplo a podšívky</h2>'
          '<p>Nepromokavá guma je zároveň nepropustná pro páru, takže noha se v ní potí. Textilní podšívka tento vlhký pocit zmírní. Pro chladné dny se hodí fleecová nebo neoprenová vložka, která zatepluje, a zároveň tlumí šum při chůzi. '
          'Silné ponožky z <a href="/merino-ponozky/">merina</a> nebo <a href="/sportovni-ponozky/">sportovní ponožky</a> pomáhají odvádět vlhkost. Bavlněné ponožky se nehodí, protože vlhkost drží a nohy rychle zchladnou.</p>'
          '<h2>Pro koho jsou které holínky</h2>'
          + T(['Využití', 'Doporučený typ', 'Na co se dívat'], [
              ['Školka a hřiště', 'lehké dětské, střední výška', 'ouška, reflexní prvky, vyjímatelná vložka'],
              ['Zahrada a procházky', 'střední výška, hrubší dezén', 'pohodlná pata, lehká váha'],
              ['Rybaření a voda', 'vysoké, často neoprenové', 'výška, izolace, protiskluzová podrážka'],
              ['Stáj a práce se zvířaty', 'robustní, chemicky odolná guma', 'oděruvzdornost, snadné čištění'],
              ['Festival a město', 'módní nižší modely', 'pohodlí při dlouhé chůzi, stabilní podrážka'],
              ['Les a lov', 'vyšší, tlumené, často s podšívkou', 'tišší podrážka, teplo, odolnost proti trnům']]) +
          '<p>Rybáři se zajímají o varianty s bezpečností při brodění. K nim patří i <a href="/rybarske-obleceni/">rybářské oblečení</a> a <a href="/obuv-do-vody/">obuv do vody</a>. Myslivci hledají tišší obuv, kterou doplní <a href="/lovecke-obleceni/">lovecké oblečení</a>. Pro brodění v hlubší vodě ale holínky nestačí a nahradí je prsačky nebo brodicí boty.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po použití holínky opláchněte vodou a nechte vyschnout v pokojové teplotě, ne u radiátoru ani na přímém slunci. Vysoké teplo materiál zkřehne a vznikají drobné praskliny. Vnitřek se vysušuje sám, ale u textilní podšívky pomůže vložit pár zmačkaných novin. '
          'Přírodní kaučuk občas ošetřete přípravkem na gumu, který zpomaluje stárnutí a odstraňuje bělavý povlak. Ten vzniká vypocením přísad a je neškodný. Skladujte je na stojánku nebo ve stoje, aby se svršek nezlomil, a mimo přímé slunce.</p>'
          '<p>Drobnou trhlinu opravíte záplatou na gumu nebo lepidlem určeným pro daný materiál, ale při větší prasklině se vyplatí koupit nové boty. Mokré nohy při chůzi chladnou rychle, a proto s proděravělými holínkami raději nevyrážejte na delší cestu.</p>'
          '<h2>Jak holínky obouvat a nosit</h2>'
          '<p>Při obouvání přidržte svršek u horního okraje a nohu zasuňte rovně, ne šikmo, aby se nezkroutila pata. Pomáhá obouvací klínek nebo opření o zeď. Na kamenech a mokré půdě choďte pomalu, protože mokrá guma na kamenech klouže víc než suchá. '
          'Kalhoty do nízkých holínek nezasouvejte, nohavice nechte přes okraj, aby voda nestékala dovnitř. Do vysokých holínek se kalhoty naopak zasunout dají. Pro dlouhé stání se vyplatí vložit měkkou stélku, která izoluje od studené země a odlehčí chodidlu.</p>'
          '<h2>Holínky a životní prostředí</h2>'
          '<p>Pryž a PVC se špatně recyklují, proto se vyplatí kupovat holínky na delší dobu a opravovat je. Dětské boty, které dítě vyroste, se dají předat mladšímu sourozenci nebo dál. Pokud necháváte holínky v autě, chraňte je před horkem. Opotřebované boty odevzdejte do sběrného dvora, protože v běžném odpadu končí jako objemný materiál bez dalšího užití.</p>'
          '<h2>Časté chyby</h2>'
          '<ul>'
          '<li>Koupě o dvě čísla větších holínek. Noha se v nich pohybuje a otlačuje.</li>'
          '<li>Sušení na topení, po kterém guma praská.</li>'
          '<li>Nošení bez ponožek nebo v bavlněných ponožkách, které vlhnou.</li>'
          '<li>Výběr nízkého modelu pro brodění přes strouhu.</li>'
          '<li>Očekávání, že holínky vydrží celodenní pochod. Nejsou přizpůsobené dlouhé chůzi do kopce.</li>'
          '<li>Zapomenutí na teplo: neizolované holínky v mrazu studí i při tlusté ponožce.</li>'
          '</ul>'
          '<h2>Nákup na Sportece</h2>'
          '<p>Každý model má stránku, kde obchody ukazují dostupné velikosti a dopravu. Díky tomu vidíte, zda je určitá velikost k mání. U dětských holínek se vyplatí koupit před sezónou, kdy bývají vyprodané barvy. Podle potřeby můžete rozšířit výběr o <a href="/zimni-obuv/">zimní obuv</a>, <a href="/pantofle-a-zabky/">pantofle a žabky</a> pro volnější dny a <a href="/outdoor/">outdoorové vybavení</a>.</p>',
    faq=[
        ('Jakou velikost holínek koupit?',
         'Nejlepší je změřit chodidlo a porovnat s tabulkou výrobce, protože střih se liší. Dospělí zkouší holínky v ponožce, kterou budou nosit, a hledají mezeru zhruba do jednoho centimetru před prsty. Příliš velké holínky se na patě zvedají a nohu vyčerpají.'),
        ('Jaký je rozdíl mezi gumovými a neoprenovými holínkami?',
         'Gumové jsou lehké, snadno se čistí a hodí se do tepla i mírné zimy. Neoprenové mají izolační podšívku z pěnové gumy, drží teplo a hodí se do chladu, na rybaření nebo do blátivého lesa. Neopren je ale těžší a hůře schne uvnitř.'),
        ('Proč se v holínkách potí nohy?',
         'Pryž a PVC jsou nepropustné pro vodu i vodní páru, takže pot nemá kam uniknout. Pomáhá textilní podšívka a ponožky z materiálů, které odvádějí vlhkost, například z vlny nebo syntetiky. Po použití je vhodné holínky vyvětrat a nechat uschnout.'),
        ('Jak sušit holínky?',
         'Při pokojové teplotě a v dobře větraném prostoru. Vyhněte se radiátoru a přímému slunci, protože guma zkřehne a praská. Mokrou vložku vyndejte, do vlhkých míst vložte zmačkaný papír, který nasaje vlhkost.'),
        ('Co je to bílý povlak na gumových holínkách?',
         'Jde o výpotek přísad z přírodního kaučuku. Je neškodný a nepoškozuje materiál, ale vypadá neesteticky. Setřete ho vlhkým hadříkem nebo ošetřete přípravkem na gumu, který také zpomalí stárnutí materiálu.'),
        ('Hodí se holínky na turistiku?',
         'Na krátkou procházku po blátě ano, na dlouhé túry ne. Nemají vyztuženou podešev ani pevnou oporu kotníku, a tak jsou pohodlnější trekové boty s membránou. Holínky se hodí tam, kde je potřeba stát v mokru.'),
        ('Jak vybrat dětské holínky?',
         'Zvolte lehký model s dostatečně širokým otvorem, který dítě zvládne samo obout. Rezerva před palcem by měla být kolem jednoho a půl centimetru. Reflexní prvky a vyjímatelná stélka zlepší bezpečnost a údržbu, na zimu se hodí podšívka.'),
        ('Dají se holínky opravit?',
         'Menší trhlinu lze zalepit záplatou nebo lepidlem určeným na daný materiál. Dobře to funguje u tenkých prasklin v horní části. Pokud je poškozená podešev, spojení svršku s podrážkou nebo praskliny na ohybu, je rozumnější koupit nový pár.'),
        ('Jsou holínky vhodné na zimu?',
         'Pouze s izolační podšívkou a silnou ponožkou. Obyčejná guma v mrazu studí a na ledu klouže. Pro delší pobyt venku v mrazu je lepší zimní obuv nebo sněhule, případně doplněná nesmeky.'),
        ('Čím se liší pracovní holínky od běžných?',
         'Mívají zesílenou špičku, někdy ocelovou, a stélku proti propíchnutí, hrubší podrážku a chemicky odolnější materiál. Hodí se na stavbu, do stáje nebo do chovu. Pro běžnou zahradu a hřiště stačí lehčí provedení bez výztuh.'),
    ])

# ------------------------------------------------------------------ aminokyseliny-bcaa
NEW['aminokyseliny-bcaa'] = dict(long=True,
    title='Aminokyseliny a BCAA: přehled a jak vybrat',
    desc='Aminokyseliny, BCAA, EAA a glutamin v prášku, kapslích i tabletách. Co je v nich, jak číst složení a kde porovnat nabídky českých obchodů.',
    intro='<p>Aminokyseliny jsou stavební jednotky bílkovin a doplňky stravy s nimi se prodávají v různých formách: prášek k rozpuštění, kapsle, tablety i hotové nápoje. '
          'Nejčastěji se setkáte s označením BCAA, tedy směsí tří větvených aminokyselin leucinu, isoleucinu a valinu, dále s EAA, která obsahují všechny esenciální aminokyseliny, a s jednotlivými látkami, třeba glutaminem nebo argininem.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů u produktů značek GymBeam, Extrifit, Amix, BioTech USA, Nutrend, Scitec Nutrition a dalších. Vedle toho najdete <a href="/proteiny/">proteiny</a>, <a href="/kreatin/">kreatin</a>, <a href="/predtreninkove-boostery/">předtréninkové boostery</a> a <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>. '
          'Text níže nabízí obecné informace o složení a výběru. Nejde o zdravotní radu, a proto se při jakýchkoli pochybnostech obraťte na lékaře nebo kvalifikovaného odborníka na výživu.</p>',
    guide='<h2>Co jsou aminokyseliny</h2>'
          '<p>Lidské tělo skládá bílkoviny z dvaceti aminokyselin. Část z nich si umí vytvořit samo, jiné je nutné přijímat potravou a označují se jako esenciální. Strava, která obsahuje dostatek bílkovin, tedy maso, ryby, vejce, mléčné výrobky či luštěniny, aminokyseliny běžně dodává. '
          'Doplňky jsou prostě jiný způsob, jak je přijmout: prášek se rozmíchá v lahvi a pije se během dne, kapsle se zapíjejí. Zda je potřebujete, závisí na jídelníčku a cílech a je to dobré probrat s odborníkem.</p>'
          + T(['Typ produktu', 'Co obsahuje', 'Poznámka'], [
              ['BCAA', 'leucin, isoleucin a valin v určitém poměru', 'poměr se uvádí třeba jako 2:1:1'],
              ['EAA', 'všech devět esenciálních aminokyselin', 'úplnější složení než BCAA'],
              ['Glutamin', 'jedna jediná aminokyselina', 'bývá samostatně nebo ve směsích'],
              ['Arginin a citrulin', 'jednotlivé látky často v boosterech', 'viz <a href="/predtreninkove-boostery/">předtréninkové boostery</a>'],
              ['Hydrolyzovaná bílkovina', 'krátké řetězce aminokyselin', 'blíže <a href="/proteiny/">proteinům</a>'],
              ['Kapsle a tablety', 'koncentrovaná dávka bez chuti', 'pohodlné na cesty, menší obsah v kuse']]) +
          '<h2>BCAA: poměr a složení</h2>'
          '<p>Zkratka BCAA je z anglického „branched-chain amino acids“. Na etiketě se objevuje poměr leucinu k isoleucinu a valinu, nejčastěji 2:1:1, ale existují i 4:1:1, 8:1:1 a další. Čím větší první číslo, tím víc leucinu v poměru k ostatním. '
          'Poměr sám o sobě neříká, který produkt je lepší, jen popisuje složení. Důležitější je množství každé látky v jedné dávce, které výrobce povinně uvádí v tabulce. Ve výrobku může být i další přídavek: vitaminy, elektrolyty, sladidla, aromata a barviva.</p>'
          '<p>Praktický postup: otevřete nutriční tabulku a spočítejte, kolik gramů každé aminokyseliny získáte z jedné dávky. Pak vydělte cenu zvolenou dávkou. Tak pochopíte, že dvoukilový balíček s nízkou dávkou nemusí být výhodnější než menší s koncentrovanou. Samotný údaj „velký počet porcí“ nic nevypovídá, pokud je porce malá.</p>'
          '<h2>EAA a rozdíl oproti BCAA</h2>'
          '<p>EAA je zkratka pro esenciální aminokyseliny. Kromě tří větvených obsahují i lysin, methionin, fenylalanin, threonin, tryptofan a histidin. Výrobci proto tvrdí, že jde o úplnější doplněk. '
          'Ve skutečnosti záleží na tom, co už jíte: když máte v jídelníčku dost plnohodnotných bílkovin, rozdíl mezi BCAA a EAA nemusí být významný. Spotřebitele zajímá hlavně to, co přesně se v balení nachází a jak chutná. Odborná diskuse o přínosu těchto doplňků probíhá a o jejich užití se vyplatí poradit s lékařem nebo dietologem.</p>'
          '<h2>Forma: prášek, kapsle, tablety, nápoj</h2>'
          '<h3>Prášek</h3>'
          '<p>Nejčastější a nejvýhodnější forma pro vyšší dávky. Rozmíchá se v shakeru s vodou. Aminokyseliny mají přirozeně hořkou chuť, proto výrobci přidávají aromata a sladidla a nabízejí desítky příchutí od citronu po ovoce. Neochucené varianty jsou levnější a bez sladidel, ale vyžadují odolné chuťové buňky. Prášek se hodí k pití během tréninku nebo během dne.</p>'
          '<h3>Kapsle a tablety</h3>'
          '<p>Pohodlné, bez chuti, ideální na cesty. Jedna dávka však bývá rozdělena do několika kusů, protože v jedné kapsli se vejde jen omezené množství. Pokud potřebujete větší množství, je prášek praktičtější. Při čtení etiket sledujte, kolik tablet tvoří jednu porci.</p>'
          '<h3>Hotové nápoje a šťávy</h3>'
          '<p>Hodí se, když nechcete nic míchat. Bývají dražší za dávku a krátce trvanlivé po otevření. Podobně fungují <a href="/iontove-napoje/">iontové nápoje</a>, které obsahují minerály a sacharidy.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<ul>'
          '<li><strong>Velikost porce a počet porcí.</strong> Porce určuje, kolik látky skutečně získáte, ne hmotnost balení.</li>'
          '<li><strong>Obsah v jedné porci.</strong> Součet leucinu, isoleucinu a valinu by měl odpovídat uvedenému celku.</li>'
          '<li><strong>Doplňky ve složení.</strong> Kofein, vitaminy, sladidla nebo barviva se mohou hodit či ne podle toho, jak je snášíte.</li>'
          '<li><strong>Alergeny.</strong> Lecitin, sója nebo mléčné složky mohou být přítomné i v nebílkovinném produktu.</li>'
          '<li><strong>Upozornění výrobce.</strong> Najdete tam doporučenou denní dávku a upozornění pro těhotné, kojící nebo osoby s onemocněním.</li>'
          '</ul>'
          '<h2>Pro koho tyto doplňky nejsou</h2>'
          '<p>Doplňky stravy nenahrazují pestrou stravu. Nejsou určeny dětem, těhotným a kojícím ženám ani lidem s některými onemocněními, zejména ledvin a jater, ani těm, kdo užívají léky. '
          'Před zahájením užívání je rozumné domluvit se s lékařem. Ani jeden produkt nemůže zaručit konkrétní výsledek, a proto nehledejte zázraky: zlepšení tréninku vychází hlavně ze spánku, jídla, tréninkového plánu a pravidelnosti.</p>'
          '<h2>Jak se aminokyseliny doplňují v praxi</h2>'
          '<p>Rekreační sportovci s vyváženým jídelníčkem většinou doplňky nepotřebují. Ti, kdo trénují více denně nebo mají omezený jídelníček, například vegetariáni, někdy sahají po směsích aminokyselin. '
          'Čas užití bývá otázkou zvyku: někdo pije během tréninku, jiný po něm, další přes den. Nejde o přesnou vědu, a proto hodnoťte zejména praktičnost. Lahev nápoje s příchutí zpříjemní trénink, a pokud vám chuť nevyhovuje, existují i neochucené možnosti. Dávku vždy dodržujte podle návodu výrobce a nepřekračujte ji.</p>'
          '<p>Pomůže i pitný režim. Zdroje tekutin najdete v kategoriích <a href="/lahve-a-termosky/">láhve a termosky</a> a <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>. Mezi další oblasti patří <a href="/kolagen-a-klouby/">kolagen a klouby</a>, <a href="/spalovace-tuku/">spalovače tuků</a> nebo <a href="/ostatni-doplnky-stravy/">ostatní doplňky</a>.</p>'
          '<h2>Značky a rozdíly mezi nimi</h2>'
          '<p>V katalogu se nejčastěji objevují GymBeam, Extrifit, Amix, BioTech USA, Prom-In, Nutrend, Scitec Nutrition a ATP Nutrition. Liší se příchutěmi, velikostí balení, složením a doplňky. '
          'Některé firmy nabízejí jen základní směs, jiné rozšiřují sortiment o kombinace s vitaminy a elektrolyty. Neexistuje obecně nejlepší značka, a proto hodnoťte nutriční tabulku, ne marketingový slogan. Přitom si ověřte, že produkt je určen k prodeji v Česku a má česky psanou etiketu s povinnými údaji.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Prášek skladujte suchý, uzavřený a mimo slunce a vlhko, aby nechytal hrudky. Po otevření spotřebujte v době, kterou uvádí výrobce, a vždy používejte suchou odměrku. Hotový nápoj z prášku vypijte rychle, protože při pokojové teplotě se v něm množí mikroorganismy. '
          'Kapsle a tablety nenechávejte v autě v létě. Dodržujte datum minimální trvanlivosti na obalu.</p>'
          '<h2>Glutamin, arginin a další samostatné aminokyseliny</h2>'
          '<p>Vedle směsí se prodávají i jednotlivé aminokyseliny. Glutamin je v prášku bez chuti a rozpouští se ve vodě, arginin a citrulin se nejčastěji objevují ve složení boosterů, taurin a karnitin pak ve funkčních nápojích. Každá látka má v obchodě vlastní popis a výrobce uvádí návod k použití. '
          'Co která z nich v těle dělá, vysvětluje odborná literatura, nikoli prodejní text, proto se při zájmu obracejte na lékaře nebo dietologa. Jednotlivé aminokyseliny si nekombinujte bez rady a hlídejte součet dávek ze všech doplňků, které užíváte.</p>'
          '<h2>Porovnání ceny za porci</h2>'
          '<p>Nejpřesnější způsob srovnání je spočítat cenu za jednu dávku. Vezměte velikost porce v gramech, počet porcí v balení a cenu v obchodě. Teprve pak se ukáže, zda levnější velké balení není ve skutečnosti dražší na dávku než menší koncentrovaný produkt. '
          'Do výpočtu patří i sladidla a plniva, protože čistý obsah aminokyselin v porci bývá menší než hmotnost lžičky prášku. Sportek ukazuje nabídky více obchodů u jednoho produktu a doporučuje srovnávat i dopravu a podmínky vrácení.</p>'
          '<h2>Příchutě a chuťové zkušenosti</h2>'
          '<p>Ovocné příchutě, jako citron, pomeranč nebo jahoda, jsou nejčastější a nejlépe maskují hořkost. Kolové a ledové čaje nabízejí méně sladkou alternativu. Pokud se vám chuť nelíbí, nechte si prášek rozmíchat s větším množstvím vody, nebo zvolte neochucenou variantu a použijte ji do ovocného nápoje. První balení raději kupujte menší, abyste zjistili, jestli vám příchuť sedí.</p>'
          '<h2>Doplněk neznamená náhradu</h2>'
          '<p>Základem sportovní výživy zůstává strava, spánek a pitný režim. Aminokyselinové doplňky mohou být praktickou pomůckou, ale nikdy jedinou součástí plánu. Pokud trénujete pravidelně a máte konkrétní cíl, domluvte se s trenérem nebo dietologem a plán přizpůsobte svým potřebám.</p>'
          '<h2>Časté omyly</h2>'
          '<ul>'
          '<li>Domněnka, že čím víc, tím lépe. Větší dávka nezaručuje větší účinek a překračování doporučeného množství není vhodné.</li>'
          '<li>Porovnávání jen podle ceny za balení místo za dávku.</li>'
          '<li>Zaměňování BCAA za kompletní protein. BCAA obsahují jen tři aminokyseliny.</li>'
          '<li>Spoléhání na doplněk místo na plnohodnotný jídelníček.</li>'
          '<li>Přehlížení alergenů a přídatných látek v ochuceném prášku.</li>'
          '</ul>'
          '<h2>Jak nakupovat přes Sportek</h2>'
          '<p>U každého produktu vidíte nabídky obchodů vedle sebe, včetně dostupnosti a dopravy. Porovnejte složení a velikost porce a až poté cenu. '
          'Pro přehled okolních kategorií se vraťte na <a href="/fitness/">fitness</a> nebo se podívejte na <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>, <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>.</p>',
    faq=[
        ('Co to jsou BCAA?',
         'BCAA je zkratka pro větvené aminokyseliny: leucin, isoleucin a valin. Prodávají se jako prášek, kapsle nebo tablety, nejčastěji v poměru 2:1:1. Jsou součástí běžných bílkovin v potravě, doplněk je jen koncentrovanou formou těchto tří látek.'),
        ('Jaký je rozdíl mezi BCAA a EAA?',
         'BCAA obsahují jen tři větvené aminokyseliny, EAA zahrnují všech devět esenciálních, tedy i lysin, methionin, threonin a další. EAA jsou tedy úplnější složení. Který produkt vám vyhovuje, záleží na jídelníčku, a proto se vyplatí konzultovat výběr s odborníkem.'),
        ('Co znamená poměr 2:1:1 u BCAA?',
         'Udává poměr leucinu k isoleucinu a valinu. Při poměru 2:1:1 připadají na dva díly leucinu po jednom dílu zbylých dvou aminokyselin. Jiné poměry, například 4:1:1 nebo 8:1:1, mají více leucinu. Poměr jen popisuje složení a neříká, který výrobek je lepší.'),
        ('Je lepší prášek, nebo kapsle?',
         'Prášek se hodí pro vyšší dávky a bývá výhodnější na porci, ale vyžaduje shaker a může mít výraznou chuť. Kapsle a tablety jsou praktické na cesty a bez chuti, ale jedna dávka se skládá z několika kusů. Vyberte podle toho, co zvládnete pravidelně užívat.'),
        ('Proč je prášek s aminokyselinami hořký?',
         'Volné aminokyseliny mají přirozeně hořkou chuť, zejména leucin. Proto výrobci přidávají aromata a sladidla. Neochucené varianty hořkost zachovávají, což může vadit při pití čistého roztoku, ale nemusí obsahovat sladidla.'),
        ('Potřebuji aminokyseliny, když jím dost bílkovin?',
         'Pokud jídelníček obsahuje dostatek plnohodnotných bílkovin, doplňky aminokyselin nemusí přinášet výrazný rozdíl. Zda je potřebujete, záleží na stravě, množství tréninku a zdravotním stavu. Nejlepší je poradit se s lékařem nebo dietologem.'),
        ('Kdy se aminokyseliny užívají?',
         'Doba užití je věcí zvyku a doporučení výrobce. Někdo je pije během tréninku, jiný po něm nebo přes den. Důležitější než přesná hodina je dodržet dávku uvedenou na obalu a nepřekračovat ji.'),
        ('Pro koho nejsou doplňky aminokyselin vhodné?',
         'Nejsou určeny dětem, těhotným a kojícím ženám, lidem s onemocněním ledvin nebo jater a těm, kdo užívají léky, pokud to neschválí lékař. Doplňky stravy nenahrazují pestrou stravu a mohou způsobit nežádoucí reakce u citlivých osob.'),
        ('Jak poznám kvalitní produkt?',
         'Sledujte úplnou nutriční tabulku s obsahem jednotlivých aminokyselin na porci, seznam složek a alergenů, datum trvanlivosti a české označení výrobce nebo distributora. Marketingové sliby na přední straně nahrazovat tabulku nemohou. Porovnávejte cenu za porci, ne za balení.'),
        ('Jak skladovat prášek?',
         'Na suchém, chladném místě mimo slunce, v uzavřeném obalu a s čistou suchou odměrkou. Vlhko způsobí hrudky a zkracuje trvanlivost. Hotový nápoj vypijte brzy, protože se v roztoku množí mikroorganismy.'),
    ])

# ------------------------------------------------------------------ kempingove-doplnky
NEW['kempingove-doplnky'] = dict(long=True,
    title='Kempingové doplňky: lampy, nádoby i pomůcky',
    desc='Kempingové doplňky pro stan, auto i karavan: osvětlení, voda, ochrana před hmyzem, podlážky a elektřina. Jak vybrat a kde porovnat nabídky obchodů.',
    intro='<p>Kemping se skládá z velkých věcí, jako je stan nebo spacák, a z desítky drobností, bez kterých je noc nepříjemná. Lampa, která svítí do stanu, kanystr s vodou, prodlužovací kabel, ventilátor, podložka pod stan nebo moskytiéra rozhodují o tom, jestli dovolená proběhne klidně, nebo ztratí půl dne hledáním. '
          'Doplňky se hodí všem, od víkendových stanařů po rodiny s karavanem.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u kempingových doplňků značek Quechua, Cattara, Nils, Naturehike, Eurotrail, Skandika, Yate nebo King Camp. Pokud skládáte celou výbavu, mrkněte i na <a href="/stany/">stany</a>, <a href="/spaci-pytle/">spací pytle</a>, <a href="/karimatky-a-matrace/">karimatky</a>, <a href="/kempingovy-nabytek/">kempingový nábytek</a> a <a href="/kempingove-nadobi/">nádobí</a>. '
          'Průvodce dále popisuje, co do kempu skutečně potřebujete a podle čeho vybírat.</p>',
    guide='<h2>Co patří mezi kempingové doplňky</h2>'
          '<p>Kategorie shromažďuje věci, které nespadají do stanu, spacího vybavení ani vaření, ale bez kterých se nedá žít; patří sem i lehké skládací stolky a piknikové deky pro zázemí u stanu. Tvoří ji osvětlení, zásobování vodou, ochrana proti hmyzu a vlhku, drobné nářadí, úložné pomůcky a zázemí na pozemku. '
          'Rozdělení pomáhá nepřehlédnout drobnosti při balení a vyhnout se nákupu duplicit.</p>'
          + T(['Skupina', 'Typické předměty', 'K čemu slouží'], [
              ['Osvětlení', 'lucerny, čelovky, svítilny, solární světla', 'orientace po setmění, světlo ve stanu'],
              ['Voda', 'kanystry, vaky, sprchy, skládací umyvadla', 'zásoba pitné a užitkové vody'],
              ['Ochrana', 'moskytiéry, odpuzovače, plachty, podlážky', 'proti hmyzu, dešti a vlhku od země'],
              ['Úklid a pořádek', 'pytle, kbelíky, věšáky, organizéry', 'pořádek v předsíni a v autě'],
              ['Energie', 'prodlužovací kabely, rozdvojky, powerbanky', 'napájení a nabíjení v kempu'],
              ['Drobné nářadí', 'kladívko, lano, provázek, sada na opravu', 'ukotvení, opravy, úpravy zázemí']]) +
          '<h2>Osvětlení: lucerna, čelovka, solární světla</h2>'
          '<p>Po setmění je světlo základ. Lucerna rozsvítí stan a stůl a svítí do všech stran, čelovka se hodí na cesty a při práci rukama a drobná solární světla vyznačí lanka a kolíky. Napájení bývá z akumulátoru nabíjeného přes USB, z baterií, nebo ze solárního panelu. '
          'U lucerny hlídejte možnost ztlumení, protože prudké bílé světlo ve stanu oslňuje a láká hmyz. Teplejší barva světla je příjemnější pro oči. Podrobněji se čelovkám věnuje kategorie <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</p>'
          '<p>Přes den nezapomeňte lucernu nabít. Pokud jedete na více dnů bez elektřiny, vezměte <a href="/powerbanky-a-nabijeni/">powerbanku</a> nebo solární panel, protože lampy s vestavěným akumulátorem se vybijí bez varování.</p>'
          '<h2>Voda: přeprava, mytí a sprchování</h2>'
          '<p>Většina kempů má pitnou vodu, ale kohoutek bývá daleko od stanu. Skládací vak nebo kanystr s kohoutkem šetří chození a skládací kbelík nebo umyvadlo se hodí na mytí nádobí. Při výběru nádoby se ptejte na materiál bez zápachu a na uzávěr, který neprotéká. '
          'Kanystr by měl mít madlo a stabilní podstavu, protože plný váží hodně. Sluneční sprcha je černý vak, který na slunci ohřeje vodu, a v létě poslouží dobře. Na čištění vody se používají filtry a tablety, které ale nemají nahradit vodu určenou k pití z kempu. Pro nápoje i chlazení se hodí <a href="/lahve-a-termosky/">láhve a termosky</a> a <a href="/chladici-boxy/">chladicí boxy</a>.</p>'
          '<h2>Ochrana před hmyzem a vlhkem</h2>'
          '<p>V letní noci rozhoduje moskytiéra o klidném spánku. Stany mají obvykle vlastní síťku ve dveřích, ale samostatné moskytiéry se věší u lehátek a hamaků. K odpuzování se používají spreje, spirály a lampy; výrobci dávají návod, jak je používat. Hledejte ty určené pro venkovní prostor. '
          'Víc najdete v kategorii <a href="/hygiena-a-repelenty/">hygiena a repelenty</a> a také u <a href="/hamaky/">hamaků</a>.</p>'
          '<p>Studená a vlhká zem je druhý nepřítel. Podlážka pod stan chrání dno před oděrem a vlhkem, ale musí být o něco menší než půdorys, jinak shromažďuje dešťovou vodu pod stanem. Nepromokavá plachta se hodí jako zástěna před vchodem, ale i jako pokrývka na nářadí. Další zázemí poskytují <a href="/pristresky-a-party-stany/">přístřešky a párty stany</a> a <a href="/stanove-doplnky/">stanové doplňky</a>.</p>'
          '<h2>Pořádek a úložné pomůcky</h2>'
          '<p>Malé věci se v kempu ztrácejí, a proto pomáhají síťové kapsy, závěsné organizéry a pytle s popisky. Vodotěsný vak chrání oblečení a elektroniku, kdežto skládací koš na špinavé prádlo oddělí mokré a čisté věci. '
          'Věšáky na provázku se hodí ke sušení ručníků, ale přetížené lanko se může uvolnit. Ve stanu pomáhá lanko s háčky pod stropem, na které se zavěsí lucerna nebo malé věci. Pro velký náklad jsou užitečné <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h2>Elektřina v kempu</h2>'
          '<p>Kempy s přípojkou používají modrý CEE konektor. Potřebujete prodlužovací kabel s odpovídajícím průřezem a ochranou proti vlhkosti, ideálně s hrubě odlitou zásuvkou, která drží i v dešti. Kabel nenechávejte stočený při velkém odběru, protože se přehřívá. '
          'Elektrické zařízení udržujte mimo kaluže a nenechávejte zásuvky na zemi bez krytí. Pokud máte pochybnosti o zapojení, poraďte se s obsluhou kempu. Nabíjení menších zařízení zvládne <a href="/powerbanky-a-nabijeni/">powerbanka</a>, ale zásobník stačí jen na krátkou dobu.</p>'
          '<h2>Drobné nářadí a opravy</h2>'
          '<p>Do batohu patří sada na opravy: plátno s lepidlem na stan, nit a jehla, náhradní kolíky, páska a lanko. Kladívko nebo gumová palička usnadní zatloukání <a href="/stanove-kolky/">stanových kolíků</a>, zejména na tvrdé zemi. '
          'Dobrý multifunkční nůž je užitečný ve všem od krájení po opravu, a proto se na něj podívejte v <a href="/outdoorove-noze-a-multitoola/">kategorii nožů a multitoolů</a>. Drobné vybavení pro zdraví najdete v <a href="/prvni-pomoc/">první pomoci</a>.</p>'
          '<h2>Podle typu kempování</h2>'
          + T(['Styl', 'Co nezapomenout', 'Na co se zaměřit'], [
              ['Víkend se stanem u auta', 'lucerna, kanystr, podlážka, kladívko', 'jednoduchost a rychlé balení'],
              ['Rodinný kemp', 'více světel, zástěna, organizéry, repelent', 'pořádek a ochrana dětí před hmyzem'],
              ['Karavan nebo obytný vůz', 'prodlužovací kabel, klíny, hadice na vodu', 'napájení a stabilita'],
              ['Lehký pěší tábor', 'čelovka, malá lucerna, vak na vodu', 'hmotnost a objem'],
              ['Festival', 'čelovka, zámek na stan, zátky do uší', 'rychlé postavení a bezpečnost'],
              ['Rybářský tábor', 'světla, plachta, chladicí box', 'zázemí na břehu a počasí']]) +
          '<p>Pro rybáře jsou tu <a href="/rybarske-stany/">rybářské stany</a> a <a href="/rybarske-tasky/">tašky</a>. Pro vaření jsou připraveny kategorie <a href="/vareni-v-prirode/">vaření v přírodě</a> a <a href="/varice-a-kartuse/">vařiče a kartuše</a>. Vše dohromady najdete v rozcestníku <a href="/kemping/">kemping</a>.</p>'
          '<h2>Materiály a údržba</h2>'
          '<p>Doplňky z PVC a polyesteru se čistí vlažnou vodou a jemným mýdlem. Před uskladněním je důležité je úplně vysušit, jinak se tvoří plísně. Kovové části, třeba karabiny a háčky, otřete od soli a písku. '
          'Hadice, kanystry a vaky na vodu jednou za čas vymyjte roztokem jedlé sody a vyvětrejte, aby neměly zápach. Baterie ve svítilnách vyndejte, pokud je delší dobu nepoužijete, protože mohou vytéct a poškodit kontakty. Lampy a světla skladujte v suchu.</p>'
          '<h2>Zázemí před stanem</h2>'
          '<p>Většinu času v kempu strávíte před stanem, a proto stojí za to zázemí promyslet. Rohožka nebo koberec ze síťoviny zadrží písek a trávu, aby se nenosily dovnitř, a pomáhá i stojánek na boty. Plachta natažená na dvou tyčích vytvoří stín nebo zastřešení při dešti. '
          'Lanko s kolíky spojí přístřešek a stan a zajistí ho proti větru. Zkontrolujte, že lana neblokují průchod, protože v šeru se o ně snadno zakopne, a proto se hodí reflexní nebo světlé nitě.</p>'
          '<h2>Odpad a čistota v kempu</h2>'
          '<p>Pytle na odpad a malý kbelík s víkem zabrání zápachu a lákání zvířat. Odpad patří do kontejnerů v kempu, v přírodě se odnáší zpět. Nádobí se myje mimo vodní toky a mýdlo se volí šetrné k prostředí. '
          'Skládací umyvadlo a houbička zaberou málo místa. Papírové ubrousky nahradí látkové utěrky, které se dají vyprat a znovu použít.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul>'
          '<li>Nákup velké lucerny bez ztlumení. Ve stanu oslňuje a přitahuje hmyz.</li>'
          '<li>Zapomenutí na nabíjení před cestou a absence záložního světla.</li>'
          '<li>Podlážka větší než půdorys stanu, pod kterou se zachytává dešťová voda.</li>'
          '<li>Příliš tenký prodlužovací kabel ve styku s vlhkem.</li>'
          '<li>Pořizování samostatných věcí tam, kde by stačil kus nářadí s více funkcemi.</li>'
          '<li>Nedostatečné zajištění vaku nebo kanystru s vodou na šikmé zemi.</li>'
          '</ul>'
          '<h2>Jak nakupovat přes Sportek</h2>'
          '<p>Každý produkt má stránku s nabídkami obchodů, kde vidíte dostupnost a dopravu. Před nákupem si zkontrolujte rozměry a hmotnost, protože v kempu se počítá každý litr zavazadlového prostoru. Značky jako Quechua a Naturehike cílí spíš na turistiku a lehké vybavení, zatímco Cattara, Eurotrail, Skandika a Yate nabízejí robustnější a rodinné řešení. '
          'Doplňky se hodí vybírat po částech: nejprve to, co chybí, a až pak věci navíc. Podobné doplňky najdete také v kategoriích <a href="/outdoor-doplnky/">outdoorové doplňky</a> a <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</p>',
    faq=[
        ('Co si vzít do kempu kromě stanu a spacáku?',
         'Světlo, tedy lucernu a čelovku, zásobu vody v kanystru nebo vaku, podlážku pod stan, moskytiéru nebo repelent, základní nářadí, lékárničku a organizéry na drobnosti. Pokud jedete do kempu s elektřinou, přibude prodlužovací kabel a rozdvojka.'),
        ('Jakou lucernu do stanu vybrat?',
         'Takovou, která umí ztlumit světlo a má teplejší odstín, aby neoslňovala. Sledujte způsob napájení: nabíjecí akumulátor je praktický, ale bez nabíjecího zdroje se vybije. U lucerny s háčkem ji zavěsíte pod strop stanu.'),
        ('Je podlážka pod stan nutná?',
         'Není povinná, ale chrání dno stanu před otěrem a vlhkostí od země a prodlužuje jeho životnost. Musí být o něco menší než půdorys stanu, jinak po ní stéká dešťová voda pod stan. Dává se pod dno, ne dovnitř.'),
        ('Jak uchovat pitnou vodu v kempu?',
         'Používejte čisté kanystry nebo vaky určené pro potraviny, které uzavřete a skladujte ve stínu. Nádoby pravidelně myjte a vyvětrejte. Voda ze zdrojů, u kterých si nejste jistí, se musí upravit filtrem nebo převařit.'),
        ('Čím se brání hmyzu ve stanu?',
         'Základem je zavřená síťka ve dveřích a vypnuté světlo při otevírání vchodu. Pomáhají repelenty na kůži, spirály a lampy určené pro venkovní prostor. Moskytiéry se věší nad lehátka a hamaky a při pobytu u vody se vyplatí.'),
        ('Jaký prodlužovací kabel použít v kempu?',
         'Takový, který je určený pro venkovní použití, má dostatečný průřez vodičů a krytí proti vlhku. Kabel před použitím úplně rozvinout, aby se při zátěži nepřehříval, a nevést ho kalužemi. V případě nejistoty se zeptejte provozovatele kempu.'),
        ('Jak vyčistit kanystr nebo vak na vodu?',
         'Vymyjte ho teplou vodou s jedlou sodou nebo prostředkem určeným pro nádoby na potraviny, dobře vypláchněte a nechte vyschnout s otevřeným uzávěrem. Při uskladnění ho nezavírejte, aby uvnitř nevznikal zápach.'),
        ('Co všechno se hodí do opravárenské sady?',
         'Samolepicí záplaty na stanovinu, lepidlo, nit a jehla, náhradní kolíky a šňůry, izolační páska a lanko. Záplata a páska vás zachrání, když vítr roztrhne plachtu. Sadu uložte do suchého vaku.'),
        ('Jak ušetřit místo při balení doplňků?',
         'Používejte skládací nádoby, lucerny s kompaktními rozměry a víceúčelové nářadí. Drobnosti seskupte do organizérů podle kategorií a těžké věci umístěte dolů a blíž k zádům. Hodnotit se vyplatí i hmotnost, ne jen rozměr.'),
        ('Co potřebuji pro kempování v karavanu?',
         'Prodlužovací kabel s CEE koncovkou, rozdvojku, hadici na vodu, klíny pod kola a stabilizační podložky. Rovnoměrné zatížení a bezpečné připojení k elektřině jsou základ. Kromě doplňků ověřte u provozovatele kempu typ přípojky.'),
    ])
