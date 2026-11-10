"""sporteka.cz — wave 12a (4. 11. 2026): long texts (>= 1650 words) for sportovni-obuv, tenisky, sportovni-obleceni, sportovni-tricka.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ sportovni-obuv
NEW['sportovni-obuv'] = dict(long=True,
    title='Sportovní obuv: běžecké, trekové, tréninkové boty | Sporteka',
    desc='Sportovní obuv na běh, turistiku, trénink i míčové sporty. Průvodce výběrem podle povrchu a sezóny, porovnání nabídek českých e-shopů na jednom místě.',
    intro='<p><strong>Sportovní obuv</strong> je zastřešující kategorie pro všechno, co se obouvá k pohybu: od lehkých závodních bot přes pevné horské boty až po sálovou obuv na halový sport. Společné mají jen to, že noha v nich musí vydržet opakovanou zátěž, a proto se každý typ konstruuje jinak. Správná volba tedy začíná u činnosti, ne u značky.</p>'
          '<p>Na Sportece najdete jednotlivé větve pohromadě: <a href="/bezecka-obuv/">běžecké boty</a>, <a href="/trekova-obuv/">trekové boty</a>, <a href="/treninkova-obuv/">tréninkovou obuv</a>, <a href="/kopacky/">kopačky</a>, <a href="/zimni-obuv/">zimní boty</a> i každodenní <a href="/tenisky/">tenisky</a>. U každého modelu vidíte nabídky více českých obchodů vedle sebe. Níže je průvodce, který vysvětluje, jak boty dělit, na co se při zkoušení soustředit a jak o ně pečovat.</p>',
    guide='<h2>Jak se v nabídce sportovní obuvi zorientovat</h2>'
          '<p>Z pohledu konstrukce je důležité, jakou práci bota odvádí. Běžecká obuv tlumí opakované nárazy a pomáhá odvalu chodidla, trekové boty chrání před kameny, kořeny a vlhkem, kopačky zajišťují záběr na trávě a sálová obuv drží na parketu bez zanechávání stop. Když vezmete boty z jedné skupiny a použijete je v jiné disciplíně, obvykle to nejprve nepoznáte, ale po delší době se objeví bolest, rychlé opotřebení nebo uklouznutí.</p>'
          '<h3>Přehled hlavních skupin</h3>'
          + T(['Skupina', 'Hlavní vlastnost', 'Pro koho'], [
              ['<a href="/bezecka-obuv/">Běžecké boty</a>', 'odpružená mezipodešev, prodyšný svršek', 'pravidelné běhání po silnici i lesních cestách'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'pevná podrážka, výztuž špičky a paty', 'turistika, hory, delší túry s batohem'],
              ['<a href="/treninkova-obuv/">Fitness a trénink</a>', 'plochá stabilní podrážka', 'posilovna, skupinová cvičení, crossfit'],
              ['<a href="/kopacky/">Kopačky</a>', 'kolíky nebo drobné výstupky na podrážce', 'fotbal na trávě či umělém povrchu'],
              ['<a href="/salova-obuv/">Sálová obuv</a>', 'světlá, protiskluzová podrážka', 'florbal, volejbal, házená, futsal'],
              ['<a href="/tenisova-obuv/">Tenisová obuv</a>', 'zpevněné boky, odolná špička', 'kurty s antukou, tvrdým povrchem i trávou'],
              ['<a href="/barefoot-obuv/">Barefoot boty</a>', 'tenká flexibilní podešev, široká špička', 'chůze a běh s přirozeným došlapem'],
              ['<a href="/zimni-obuv/">Zimní obuv</a>', 'zateplení a podrážka pro sníh a led', 'procházky a práce venku v mrazu']]) +
          '<h3>Běh: silnice, les, hory</h3>'
          '<p>Kdo běhá převážně po asfaltu, sáhne po <a href="/silnicni-bezecke-boty/">silničních běžeckých botách</a> s hladším vzorkem a měkčím odpružením. Běžec, který střídá lesní stezky, kořeny a bláto, ocení <a href="/trailove-boty/">trailové boty</a> s hrubším vzorkem a pevnější špičkou. Rozdíl pocítíte v mokru: silniční podrážka na vlhké hlíně klouže, zatímco trailová na suchém asfaltu zbytečně rychle ztrácí výstupky.</p>'
          '<h3>Turistika: nízké nebo vysoké boty</h3>'
          '<p>Na krátké výlety a udržované cesty stačí <a href="/nizke-trekove-boty/">nízké trekové boty</a>, které jsou lehčí a pohodlnější na chůzi. Pokud nesete těžší batoh, jdete po kamenitém terénu nebo chcete mít kotník stabilnější, patří do výbavy <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>. Výška svršku ale sama kotník před vyvrtnutím neochrání, rozhoduje i tuhost podrážky a šněrování.</p>'
          '<h3>Míčové sporty a povrch</h3>'
          '<p>U kolektivních sportů hraje hlavní roli povrch. Na trávě se používají <a href="/kopacky/">kopačky</a>, v hale <a href="/salova-obuv/">sálová obuv</a>, u košíkové <a href="/basketbalova-obuv/">basketbalové boty</a> s vyšší oporou kotníku a u rakety <a href="/tenisova-obuv/">tenisová obuv</a>. Univerzální bota existuje jen jako kompromis. Pokud hrajete týdně, pořiďte si specializovaný pár, protože rozdíl v přilnavosti i bezpečnosti je znát.</p>'
          '<h3>Léto, voda a zima</h3>'
          '<p>V horku a u vody se hodí <a href="/sandaly/">sportovní sandály</a>, <a href="/pantofle-a-zabky/">pantofle a žabky</a> a <a href="/obuv-do-vody/">boty do vody</a>, které se rychle suší a chrání chodidlo před ostrými kameny. Ve studené části roku nastupují <a href="/zimni-obuv/">zimní boty a sněhule</a>, u práce na zahradě nebo v blátě pak <a href="/holinky/">holínky</a>. Každá z těchto kategorií řeší jiný problém, takže se navzájem nenahrazují.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Největší chyba při online nákupu je spoléhat se na číslo ze staré boty. Střih závisí na kopytu, které výrobce používá, a dva modely téže značky mohou sedět odlišně. Orientační vodítko je délka chodidla měřená večer, kdy je nejširší. Od naměřené hodnoty se přidává rezerva pro prsty a výsledek se porovná s tabulkou konkrétní značky.</p>'
          + T(['Aktivita', 'Doporučená rezerva před prsty', 'Proč'], [
              ['Chůze a volný čas', 'asi 0,5 až 1 cm', 'noha se při došlapu mírně roztáhne'],
              ['Běh', 'asi 1 až 1,5 cm', 'při delším běhu noha otéká a posouvá se vpřed'],
              ['Turistika s klesáním', 'asi 1 až 1,5 cm', 'prsty nesmí narážet do špičky při schodech dolů'],
              ['Kopačky a sálová obuv', 'těsnější, jen malá rezerva', 'potřebujete pevné držení při změnách směru']]) +
          '<p>Při zkoušení si obujte ponožky, které budete používat při sportu. Tenká běžecká ponožka a silná turistická mění objem v botě víc, než čekáte. Zkuste chodit po místnosti, zaklekněte a zkontrolujte, zda pata nepodjíždí. Pokud palec dosahuje na špičku nebo vás tlačí boky, vyberte jiný střih, ne jen větší číslo.</p>'
          '<h2>Materiály a konstrukce</h2>'
          '<ul><li><strong>Síťovina</strong> propouští vzduch a rychle schne, ale méně chrání před vodou a ostrými předměty.</li>'
          '<li><strong>Pletený svršek</strong> obepíná chodidlo jako ponožka a dobře sedí bez švů, které by mohly tlačit.</li>'
          '<li><strong>Kůže</strong> vydrží a pomalu se přizpůsobuje noze, vyžaduje ale ošetření a je těžší.</li>'
          '<li><strong>Membrána</strong> zadrží vodu zvenčí, současně však snižuje prodyšnost, takže se hodí na vlhké a studené počasí.</li>'
          '<li><strong>Pryžová podrážka</strong> s hlubším vzorkem drží na blátě a sněhu, hladká je tišší a lehčí na pevných površích.</li></ul>'
          '<p>Mezipodešev z pěnových materiálů stárne i bez nošení, takže staré nenošené boty nemusí fungovat jako nové. Tuhost podrážky se dá jednoduše otestovat prohnutím: čím je bota určena pro náročnější terén, tím hůř se ohýbá napříč, zatímco přes střed by se kroutit neměla vůbec.</p>'
          '<h2>Značky a jejich střihy</h2>'
          '<p>Největší nabídku obuvi mají značky ' + B(('adidas', 'Adidas'), ('skechers', 'Skechers'), ('nike', 'Nike'), ('puma', 'Puma'), ('converse', 'Converse'), ('geox', 'Geox'), ('new-balance', 'New Balance'), ('asics', 'Asics'), ('vans', 'Vans'), ('merrell', 'Merrell'), ('mizuno', 'Mizuno'), ('crocs', 'Crocs')) + '. Zaměření se liší: Asics a Mizuno jsou známé hlavně běžeckou a halovou obuví, Merrell outdoorovými botami, Converse a Vans se soustředí na plátěné módní boty a Crocs na lehké otevřené pantofle. Při srovnávání modelů tedy hodnoťte, v čem je značka silná, a ne jen jak vypadá.</p>'
          '<h2>Péče o boty a životnost</h2>'
          '<p>Většina sportovní obuvi se nesmí prát v pračce při vysoké teplotě ani sušit na topení. Teplo naruší lepení a deformuje pěnu. Nejlepší postup je odstranit vložky a tkaničky, očistit svršek kartáčem a vlažnou vodou a nechat boty vyschnout při pokojové teplotě, případně s papírem uvnitř. Doplňky jako vložky, tkaničky nebo impregnace najdete v kategorii <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>'
          '<ul><li>Střídejte dva páry, aby měla pěna čas se po zátěži vrátit do tvaru.</li>'
          '<li>Běžecké boty nepoužívejte do práce ani na zahradu, jinak se opotřebují před časem.</li>'
          '<li>Kožené a membránové modely po umytí znovu impregnujte.</li>'
          '<li>Boty skladujte suché a mimo přímé slunce, které zkřehčuje pryž.</li></ul>'
          '<h2>Pro koho jaká obuv</h2>'
          '<p>Začínající běžec vystačí s jedním univerzálním párem a teprve po půl roce má smysl uvažovat o druhém. Rodič dětí potřebuje hlavně rychle měnitelné velikosti a snadné zapínání. Senior ocení stabilní podrážku s dobrým tlumením a měkký svršek bez tlakových míst. Kdo stojí celý den v práci, hodí se mu odpružená obuv s dostatečným prostorem pro prsty. Pro ty, kdo hledají lehkost a pocit blízkosti země, existují <a href="/barefoot-obuv/">barefoot modely</a>, které je však vhodné zavádět postupně, aby si svaly chodidla zvykly.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Stejný model se v různých obchodech liší dostupnými velikostmi, termínem doručení a podmínkami vrácení. Na Sportece proto vidíte nabídky vedle sebe a můžete vybírat podle toho, co vám nejvíc vyhovuje. Při nákupu podle slevy se ujistěte, že jde o vaši šířku a velikost, protože poslední kusy bývají nejméně obvyklé rozměry. Po doručení zkoušejte boty doma na čistém povrchu a vraťte je, pokud se hned nezdají pohodlné. Pohodlí v prvních minutách je nejlepší předpověď komfortu na delší dobu.</p>',
    faq=[('Jaký je hlavní rozdíl mezi běžeckou a trekovou botou?', 'Běžecká bota je lehká, odpružená a pružná v přední části, protože se s ní odráží krok za krokem. Trekové boty mají tužší podrážku a výztuže, které chrání nohu před kameny a stabilizují ji pod batohem, jsou ale těžší a méně pružné.'),
         ('Mohu v tenisce chodit na túry?', 'Na krátké suché cesty ano, ale na kamenitém či mokrém terénu budete postrádat opory a přilnavost. Měkká podrážka se na kamenech rychle prošlape a mokrý svršek se nesuší.'),
         ('Jak často měnit sportovní boty?', 'Záleží na zatížení. Pravidelně běhající člověk mění běžecké boty po několika stech kilometrech, zatímco kožené trekové boty vydrží několik sezón. Pokud boty ztratily odpružení, nerovnoměrně se sjely nebo vás začaly bolet klouby, je čas na výměnu.'),
         ('Je lepší koupit boty ráno, nebo večer?', 'Večer. Chodidlo během dne mírně otéká a největší je po zátěži. Kdo si boty vybere na ranní noze, může zjistit, že odpoledne tlačí.'),
         ('Hodí se barefoot boty pro každého?', 'Ne každý je zvládne hned. Svaly a šlachy chodidla si na tenkou podešev zvykají postupně, proto začněte krátkými procházkami. S bolestí nohou nebo po úrazu se nejprve poraďte s lékařem či fyzioterapeutem.'),
         ('Jak poznám, že mám širokou nohu?', 'Pokud vás boty tlačí na bocích u malíčku a palce, nebo se vám svršek vyboulí, máte pravděpodobně širší chodidlo. Pomůže širší střih nebo model s měkčím materiálem, větší velikost většinou problém nevyřeší.'),
         ('Mohu boty prát v pračce?', 'Řada výrobců to nedoporučuje, protože teplo a bubnování poškozují lepení a pěnu. Bezpečnější je ruční čištění vlažnou vodou a sušení při pokojové teplotě. Vždy se řiďte štítkem v botě.'),
         ('Potřebuji speciální obuv na tělocvičnu?', 'Pokud děláte převážně posilování, vyplatí se plošší a stabilnější podrážka než u běžecké boty. Měkké odpružení u dřepů a mrtvých tahů může vadit, protože pod zátěží se noha víc kývá.'),
         ('Platí velikost napříč značkami?', 'Ne. Číslo bývá obdobné, ale kopyta se liší délkou i šířkou. Proto se řiďte tabulkou konkrétního výrobce a změřte si chodidlo, nespoléhejte jen na velikost staré obuvi.'),
         ('Co dělat, když boty po zkoušení tlačí?', 'Zkuste jiné šněrování, jinou ponožku nebo jiný model. Pokud tlak trvá, vraťte je v zákonné lhůtě. Boty, které tlačí v obchodě, se od rozchození obvykle moc nezlepší.'),
         ('Kdy se hodí sandály místo bot?', 'V horkém počasí, u vody a na lehké procházky. Sportovní sandály mají pevný pásek a podrážku s přilnavostí, takže jsou vhodnější než obyčejné pantofle, na dlouhé túry v kamenitém terénu ale nenahradí uzavřenou botu.')],
)

# ------------------------------------------------------------------ tenisky
NEW['tenisky'] = dict(long=True,
    title='Tenisky a volnočasové boty: průvodce výběrem | Sporteka',
    desc='Tenisky a volnočasové boty pánské, dámské i dětské. Jak vybrat velikost, materiál a styl, plus porovnání nabídek českých e-shopů na jednom místě.',
    intro='<p><strong>Tenisky</strong> jsou nejuniverzálnější obuv současnosti. Nosí se do města, do školy, na výlet i k obleku a díky pohodlné podrážce se hodí na celý den. Přesto nejsou všechny tenisky stejné: liší se střihem, materiálem, tlumením i tím, zda jsou odvozené od běžecké, basketbalové, nebo skateboardové obuvi.</p>'
          '<p>Na Sportece najdete tenisky z českých e-shopů pohromadě a můžete je řadit podle značky, velikosti a nabídky. Pokud hledáte specializovanější typy, otevřete <a href="/sportovni-obuv/">sportovní obuv</a>, <a href="/bezecka-obuv/">běžecké boty</a> nebo <a href="/treninkova-obuv/">tréninkovou obuv</a>. Tento průvodce shrnuje, jaké druhy tenisek existují, jak je vybrat a jak pečovat, aby vydržely.</p>',
    guide='<h2>Druhy tenisek a k čemu jsou</h2>'
          '<p>Pojem tenisky se používá pro širokou škálu nízké obuvi s gumovou podrážkou a šněrováním. Pro orientaci je užitečné rozlišit, odkud se styl vyvinul, protože od toho se odvíjí komfort i způsob nošení.</p>'
          + T(['Druh', 'Čím se vyznačuje', 'Kdy se nosí'], [
              ['Běžecký styl', 'silná pěnová mezipodešev, prodyšná síťovina', 'celodenní chůze, cestování, práce vstoje'],
              ['Retro a klasické', 'plochá nebo mírně profilovaná podrážka, kůže nebo semiš', 'město, kancelář s volnějším dress codem'],
              ['Basketbalový styl', 'vyšší střih, silnější podrážka', 'streetwear, chladnější dny'],
              ['Skate styl', 'plochá vulkanizovaná podešev, zesílená špička', 'každodenní nošení a jízda na prkně'],
              ['Plátěné', 'lehký textil, tenká guma', 'léto, krátké procházky'],
              ['Slip-on', 'bez tkaniček, elastické boky', 'pohodlí a rychlé obouvání']]) +
          '<p>Plochá podrážka je stabilní a nenápadná, ale tlumí méně než pěnová. Kdo nachodí denně velké vzdálenosti, bude spokojenější v modelech s měkčí mezipodešví. Naopak ten, kdo chce klasický vzhled, zvolí tenčí podešev a počítá s tím, že chodidlo při dlouhé chůzi víc pocítí tvrdý povrch.</p>'
          '<h3>Pánské, dámské, dětské a unisex</h3>'
          '<p>Dámské modely mají užší patu a střed chodidla, pánské jsou obecně širší. Unisex tenisky se prodávají v jedné řadě velikostí, ale často se uvádí převodní tabulka. U dětí je důležitá hlavně pevná pata a měkký jazyk, zapínání na suchý zip nebo gumičky usnadní samostatnost. Dětské tenisky kupujte jen s malou rezervou, přibližně centimetr, a velikost pravidelně kontrolujte.</p>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Vyberte si správnou velikost podle délky chodidla, ne podle čísla na jiném páru. Chodidlo změřte večer, k naměřené délce přičtěte rezervu před prsty a porovnejte s tabulkou výrobce. Značky střihají odlišně: <a href="/znacka/new-balance/">New Balance</a> a <a href="/znacka/asics/">Asics</a> nabízejí často více šířek, <a href="/znacka/converse/">Converse</a> a <a href="/znacka/vans/">Vans</a> mají užší plátěné modely, <a href="/znacka/skechers/">Skechers</a> sází na měkké vložky a pohodlí od první chvíle.</p>'
          '<ul><li>Patu by měla bota držet bez zvedání při chůzi.</li>'
          '<li>Prsty se musí mírně rozevřít, ale neposouvat se vpřed.</li>'
          '<li>Střed chodidla má být podepřen, nemá tlačit ani se bortit.</li>'
          '<li>Jazyk a okraj kolem kotníku nesmí škrtit ani dřít.</li></ul>'
          '<h2>Materiály a jejich vlastnosti</h2>'
          '<p>Kůže vydrží a po rozchození se přizpůsobí tvaru nohy. Semiš je měkký a elegantní, ale citlivý na vodu a špínu. Textil a síťovina jsou lehké a prodyšné, hodí se do teplého počasí. Syntetické materiály nenasákají a snadno se čistí, prodyšnost ale bývá nižší. Plátno je tenké a oblíbené u letních modelů, avšak chrání jen málo před vodou a chladem.</p>'
          '<p>Podrážka bývá gumová, pryžová nebo pěnová. Pryž drží na mokru lépe než tvrdé plasty, vulkanizovaná guma poskytuje klasický vzhled a dobrý cit pro zem. Pokud na tenisky spoléháte v zimě, hledejte hlubší vzorek, případně přejděte na <a href="/zimni-obuv/">zimní boty</a>, které mají zateplení a podrážku pro sníh.</p>'
          '<h2>Tenisky podle sezóny</h2>'
          '<ul><li><strong>Jaro a podzim:</strong> kožené a syntetické modely vydrží občasný déšť a chladnější dny.</li>'
          '<li><strong>Léto:</strong> prodyšná síťovina, plátno nebo perforovaná kůže, případně <a href="/sandaly/">sandály</a> a <a href="/pantofle-a-zabky/">pantofle</a> na nejteplejší dny.</li>'
          '<li><strong>Zima:</strong> uzavřený svršek, pevná podrážka a ponožky z vlny nebo merina.</li></ul>'
          '<h2>Tenisky, nebo skutečné sportovní boty?</h2>'
          '<p>Módní tenisky vypadají podobně jako sportovní, ale zpravidla postrádají prvky určené pro zátěž. Pro běhání doporučujeme <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> nebo <a href="/trailove-boty/">trailové modely</a>, na hrubý terén <a href="/trekova-obuv/">trekové boty</a>, do posilovny <a href="/treninkova-obuv/">tréninkovou obuv</a>. Naopak na cestování, do města a na lehké procházky je pohodlná volnočasová bota naprosto dostačující. Pokud hledáte přirozenější došlap, existují také <a href="/barefoot-obuv/">barefoot boty</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce tenisek je od značek ' + B(('adidas', 'Adidas'), ('skechers', 'Skechers'), ('nike', 'Nike'), ('puma', 'Puma'), ('converse', 'Converse'), ('new-balance', 'New Balance'), ('geox', 'Geox'), ('vans', 'Vans'), ('asics', 'Asics'), ('victoria', 'Victoria'), ('palladium', 'Palladium'), ('fila', 'Fila')) + '. Geox se zaměřuje na prodyšné materiály, Victoria na plátěné modely s gumovou špičkou, Palladium na robustnější kotníkové boty, Fila na retro styl. Při srovnání se vyplatí sledovat nejen vzhled, ale i hmotnost a tuhost podrážky.</p>'
          '<h2>Péče o tenisky</h2>'
          '<p>Čistá bota vydrží déle, protože špína drhne materiál a mastnota se vsakuje do vláken. Základní postup je jednoduchý: vyjměte tkaničky a vložky, očistěte hrubou špínu kartáčkem a poté vlhkým hadříkem s jemným mýdlem. Sušte při pokojové teplotě, ne na topení. Semiš čistěte suchým kartáčem a gumou, kůži ošetřete krémem. Pomůcky jako impregnace, nové tkaničky nebo vložky najdete v sekci <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
          '<ul><li>Nenoste jedny tenisky každý den, střídání prodlužuje životnost.</li>'
          '<li>Vlhké boty nesušte u radiátoru, popraskala by pryž a lepení.</li>'
          '<li>Bílé podrážky čistěte hned po znečištění, zaschlé skvrny hůř mizí.</li>'
          '<li>Před deštěm ošetřete kůži nebo semiš impregnací.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>První chybou je koupě podle módy bez zkoušky. Druhou je příliš těsná velikost, protože tenisky se plátěnou či syntetickou vrstvou moc nerozšíří. Třetí je očekávání, že každá bota se hodí na každou činnost. Poslední chybou je zanedbání ponožek: tenká kotníková ponožka s kůží a plátnem dobře funguje, v zimě ale sáhněte po silnější. Pokud nevíte, začněte univerzální neutrální barvou, která se hodí k většině oblečení a dlouho vypadá dobře.</p>'
          '<h2>Jak využít porovnání cen</h2>'
          '<p>Stejný model bývá u více obchodů v odlišných velikostech skladem. Sporteka je vedle sebe ukáže, takže nemusíte procházet každý e-shop zvlášť. Pokud se vám líbí určitá značka, použijte filtr, případně vyhledejte její stránku. Zkuste boty doma, vraťte je při pochybnostech a všímejte si, v jaké době dorazí zásilka.</p>',
    faq=[('Jaké tenisky jsou nejpohodlnější na celý den?', 'Nejpohodlnější bývají modely s měkkou pěnovou mezipodešví, flexibilní špičkou a dobře drženou patou. Důležitější než značka je střih, který sedí vašemu chodidlu, a dostatečný prostor pro prsty.'),
         ('Je lepší kožená, nebo textilní teniska?', 'Kůže déle vydrží a lépe se přizpůsobí noze, textil je lehčí a prodyšnější. Pro léto se hodí textil, pro chladnější období kůže nebo syntetika s hladším povrchem.'),
         ('Mohu v teniskách běhat?', 'Na krátký rozběh ano, na pravidelné běhání ne. Módní tenisky nemají odpružení a konstrukci pro opakované nárazy, takže jsou pro klouby i chodidla méně šetrné než běžecká obuv.'),
         ('Jak vybrat velikost dětských tenisek?', 'Změřte délku chodidla a přidejte asi centimetr rezervy. Větší bota způsobuje klopýtání a otlaky. Velikost kontrolujte každé tři až čtyři měsíce, protože děti rostou rychle.'),
         ('Jak čistit bílé tenisky?', 'Odstraňte tkaničky, očistěte povrch měkkým kartáčkem a vlažnou vodou s jemným mýdlem. Podrážku vyčistěte houbičkou. Nesušte na slunci ani na topení, bílá by mohla zežloutnout.'),
         ('Hodí se tenisky v zimě?', 'Jen v mírných dnech a po suchém terénu. Na sníh a led potřebujete podrážku s hlubším vzorkem a materiál, který nepromokne. Lepší jsou zimní boty nebo vodě odolné modely.'),
         ('Čím se liší unisex tenisky od dámských?', 'Unisex modely mají jednu velikostní řadu a obvykle širší střih. Dámské mají užší patu a středovou část. Podle tvaru chodidla může lépe sedět jedna, nebo druhá varianta.'),
         ('Lze tenisky prát v pračce?', 'Některé textilní modely ano na šetrný program a nízkou teplotu, ale riziko deformace a poškození lepení je vyšší. Kůže a semiš do pračky nepatří. Vždy si přečtěte štítek výrobce.'),
         ('Jak rozchodit nové tenisky?', 'Noste je zpočátku krátce a doma, s ponožkami, které k nim budete používat. Pokud vás tlačí, zkuste jiné šněrování. Příliš těsné boty se výrazně nerozšíří, tak je raději vyměňte.'),
         ('Čím se liší slip-on od šněrovacích?', 'Slip-on se obouvá rychle bez tkaniček a obvykle má elastické boky. Drží hůř než šněrovací bota, takže se hodí na klidnější chůzi, ne na sport nebo delší túru.'),
         ('Jak často tenisky vyměnit?', 'Při denním nošení po několika sezónách. Signálem je prošlápnutá nebo hladká podrážka, ztvrdlá pěna, trhliny v pryži nebo bolest nohou, která dřív nebyla.')],
)

# ------------------------------------------------------------------ sportovni-obleceni
NEW['sportovni-obleceni'] = dict(long=True,
    title='Sportovní oblečení: trička, bundy, kalhoty | Sporteka',
    desc='Sportovní oblečení pro běh, turistiku, fitness i volný čas. Jak vybrat materiál, vrstvy a velikost, plus porovnání nabídek českých e-shopů na jednom místě.',
    intro='<p><strong>Sportovní oblečení</strong> má za úkol udržet tělo v pohodlí při pohybu: odvádět pot, chránit před větrem a deštěm, nebrzdit pohyb a v zimě zadržet teplo. Co je správné pro běžce, nemusí být správné pro turistu, cyklistu nebo návštěvníka posilovny, a proto je dobré začít u činnosti a počasí.</p>'
          '<p>Na Sportece najdete oblečení z českých obchodů pohromadě: <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/sportovni-bundy/">bundy a vesty</a>, <a href="/mikiny/">mikiny</a>, <a href="/sportovni-kalhoty/">kalhoty</a> i <a href="/sportovni-kratasy/">kraťasy</a>. Následující průvodce vysvětluje vrstvení, materiály, velikosti i péči, abyste z nabídky složili výbavu, která se hodí k vašemu sportu a vydrží několik sezón.</p>',
    guide='<h2>Princip tří vrstev</h2>'
          '<p>Oblečení na pohyb venku funguje jako systém. Každá vrstva řeší jiný úkol a spolupracuje se zbytkem. Základní vrstva leží na kůži a odvádí pot, střední vrstva udržuje teplo a vnější vrstva chrání před větrem, deštěm a sněhem. Kdo vrstvení pochopí, vystačí s menším počtem kusů a může oblečení měnit podle počasí.</p>'
          + T(['Vrstva', 'Úkol', 'Co hledat v nabídce'], [
              ['Spodní', 'odvádět pot od kůže', '<a href="/termopradlo/">termo prádlo</a>, <a href="/funkcni-tricka/">funkční trička</a>, <a href="/sportovni-spodni-pradlo/">spodní prádlo</a>'],
              ['Střední', 'držet teplo', '<a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/funkcni-mikiny/">funkční mikiny</a>, lehké vesty'],
              ['Vnější', 'chránit před počasím', '<a href="/vetrovky/">větrovky</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a>, <a href="/zimni-bundy/">zimní bundy</a>']]) +
          '<p>Základním pravidlem je vyhnout se bavlně na kůži při náročnějším pohybu. Bavlna nasákne potem, těžkne a dlouho schne, takže při zastavení rychle chladí. Syntetické vlákno nebo vlna ze stejného důvodu na spodní vrstvě fungují lépe.</p>'
          '<h2>Materiály a co znamenají</h2>'
          '<ul><li><strong>Polyester</strong> je lehký, rychle schne a dobře odvádí vlhkost. Může zadržovat pach, proto se hodí s pravidelným praním.</li>'
          '<li><strong>Polyamid (nylon)</strong> je odolný proti oděru a používá se u bund, kalhot a batohů.</li>'
          '<li><strong>Elastan</strong> dodává pružnost a objevuje se hlavně v <a href="/leginy/">legínách</a> a přiléhavých kouscích.</li>'
          '<li><strong>Merino vlna</strong> hřeje i za vlhka a pomalu pachne, je ale citlivější při praní.</li>'
          '<li><strong>Fleece</strong> izoluje při malé hmotnosti, vítr ale propouští, proto potřebuje vnější vrstvu.</li>'
          '<li><strong>Membrána</strong> zadrží déšť, současně však omezuje odvod vlhkosti, takže se hodí hlavně v nepříznivém počasí.</li></ul>'
          '<h2>Oblečení podle sportu</h2>'
          '<h3>Běh</h3>'
          '<p>Při běhu se tělo zahřívá rychle, proto se obléká o vrstvu méně, než byste si vzali na procházku. Základem je lehké tričko, kraťasy nebo legíny a při chladu větrovka, kterou jde sbalit do kapsy. Reflexní prvky pomáhají při běhání za šera. Kdo trénuje ráno nebo večer, ocení také <a href="/sportovni-rukavice/">rukavice</a> a <a href="/cepice-a-celenky/">čepici nebo čelenku</a>.</p>'
          '<h3>Turistika a outdoor</h3>'
          '<p>Na túru je důležité mít po ruce rezervu na změnu počasí. Do batohu patří nepromokavá bunda, teplejší mikina nebo vesta a náhradní tričko. Kalhoty z rychleschnoucího materiálu, například <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, se hodí na celodenní chůzi. Lehká <a href="/kosile/">outdoorová košile</a> chrání před sluncem a hmyzem, <a href="/nakrcniky-a-satky/">nákrčník</a> slouží jako šátek, čelenka i ochrana krku.</p>'
          '<h3>Fitness a posilovna</h3>'
          '<p>V posilovně se klade důraz na volnost pohybu a odvod potu. Dámám slouží <a href="/sportovni-podprsenky/">sportovní podprsenky</a> s odpovídající oporou a <a href="/leginy/">legíny</a>, mužům tričko a <a href="/sportovni-kratasy/">kraťasy</a> nebo <a href="/teplaky/">tepláky</a>. Šev, který tlačí nebo dře, se při opakování cviku projeví, takže u fitness oblečení zkoušejte pohyb, ne jen stání.</p>'
          '<h3>Týmové sporty a plavání</h3>'
          '<p>Kolektivní sporty používají <a href="/dresy/">dresy</a> a <a href="/soupravy/">soupravy a komplety</a>, které se prodávají i jako fanouškovské zboží. V bazénu a u vody najdete <a href="/plavky/">plavky</a> v dámském, pánském i dětském provedení. Plavky na sport mají odolnější materiál proti chloru, plážové jsou spíš módní.</p>'
          '<h3>Zima a sníh</h3>'
          '<p>Na zimní sporty začněte vrstvením. Pod <a href="/zimni-bundy/">zimní a péřovou bundu</a> patří termo prádlo, případně fleece. <a href="/sportovni-ponozky/">Sportovní ponožky</a> z vlny udrží teplo i při pocení. Pro chladné ráno se hodí <a href="/kabaty-a-parky/">kabáty a parky</a>, které přesahují zadek a chrání při stání nebo pomalé chůzi, a <a href="/kombinezy/">kombinézy a overaly</a> pro děti.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Sportovní oblečení má obvykle anatomický střih a přiléhá víc než běžné. Přiléhavost není tlak: tkanina by měla sedět těsně na těle bez škrcení. Změřte obvod hrudníku, pasu a boků, porovnejte je s tabulkou konkrétní značky a pamatujte, že střihy se liší. Značky z Evropy sedí odlišně od amerických a asijských, takže stejné písmeno nemusí znamenat stejný rozměr.</p>'
          + T(['Typ kousku', 'Jak má sedět', 'Poznámka'], [
              ['Termo prádlo', 'těsně na těle', 'musí se dotýkat kůže, aby odvádělo pot'],
              ['Běžecké tričko', 'přiléhavé, ne těsné', 'švy nesmí dřít v podpaží'],
              ['Mikina', 'volnější', 'prostor pro vrstvu pod ní'],
              ['Bunda', 'volná v ramenou', 'musí jít obléknout přes střední vrstvu'],
              ['Kalhoty', 'pohodlné v pasu a kolenou', 'zkuste dřep nebo zvednutí kolena']]) +
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('new-era', 'New Era'), ('puma', 'Puma'), ('regatta', 'Regatta'), ('under-armour', 'Under Armour'), ('trespass', 'Trespass'), ('speedo', 'Speedo'), ('champion', 'Champion'), ('fjallraven', 'Fjällräven')) + '. Speedo je spojeno s plaveckým oblečením, New Era s čepicemi a kšiltovkami, Regatta, Trespass a Fjällräven s outdoorovým a turistickým oblečením. Při srovnávání se dívejte na materiál a střih, ne jen na jméno.</p>'
          '<h2>Péče o oblečení</h2>'
          '<p>Správné praní prodlužuje životnost funkčních vláken. Používejte šetrný prací prostředek bez aviváže, protože aviváž zanáší vlákna a snižuje schopnost odvádět vlhkost. Membránové bundy občas vyperte a znovu impregnujte, aby voda opět stékala po povrchu. Nepřetěžujte pračku, zapněte zipy a suchý zip, ať se oděv neničí. Sušičku používejte jen tehdy, když to štítek dovoluje.</p>'
          '<ul><li>Merino perte šetrně a sušte položené naplocho.</li>'
          '<li>Péřové bundy se perou speciálním prostředkem a suší s tenisovými míčky v sušičce.</li>'
          '<li>Pachy ze syntetiky lépe odstraní praní hned po použití, než když oblečení leží ve vlhkém koši.</li>'
          '<li>Reflexní a potištěné části nežehlete žehličkou.</li></ul>'
          '<h2>Pro koho které oblečení</h2>'
          '<p>Začátečník potřebuje základ: dvě tři funkční trička, jedny kalhoty nebo legíny, lehkou mikinu a větrovku. Děti ocení odolné a pohodlné kousky, které vydrží prolézání i praní. Fanoušci sportu hledají dresy a týmovou módu, turisté vícevrstvé outdoorové oblečení. Kdo se hýbe celoročně, měl by investovat do kvalitní vnější vrstvy a spodního prádla, protože právě ty rozhodují o komfortu.</p>'
          '<h2>Chytrý nákup</h2>'
          '<p>Oblečení je sezónní zboží, takže slevy přicházejí na konci sezóny, zimní bundy na jaře a plavky na podzim. Sporteka ukazuje nabídky více obchodů vedle sebe a zároveň vidíte dostupné velikosti. Při nákupu na slevu si ujistěte, že ještě zbývá vaše velikost, a porovnejte složení materiálu, protože dvě podobně vypadající trička se mohou lišit kvalitou.</p>',
    faq=[('Proč nenosit bavlnu na sport?', 'Bavlna saje pot a dlouho schne. Mokré tričko chladí a při pauze vás rychle podchladí. Při lehké chůzi nevadí, při náročném pohybu nebo v chladu je lepší syntetika nebo merino.'),
         ('Kolik vrstev na běh v zimě?', 'Obvykle stačí dvě až tři: funkční tričko, případně lehká mikina a větrovka. Tělo se při běhu zahřeje, proto se oblékejte tak, aby vám bylo na začátku mírně chladno.'),
         ('Co je to membrána v bundě?', 'Je to tenká vrstva, která zadržuje kapky vody, ale propouští část vodní páry. Čím lepší odvod páry, tím méně se potíte, ale tím větší bývá zpravidla nárok na péči.'),
         ('Jak vybrat velikost sportovního oblečení?', 'Změřte hrudník, pas a boky a porovnejte je s tabulkou výrobce. U přiléhavých kousků zvažte, zda dáváte přednost těsnějšímu, nebo volnějšímu střihu.'),
         ('Jak často prát funkční oblečení?', 'Po každém náročnějším použití, aby se pot a mastnota nezapekly do vláken. Používejte šetrné prostředky a nepoužívejte aviváž.'),
         ('Je merino lepší než polyester?', 'Merino hřeje i za vlhka a pomalu pachne, ale je dražší a citlivější. Polyester rychleji schne a víc vydrží. Podle sportu se často kombinují obě vlákna.'),
         ('Čím se liší softshell od hardshellu?', 'Softshell je pružnější a prodyšnější, odolá větru a lehkému dešti. Hardshell je plně nepromokavý a méně prodyšný, hodí se na vytrvalý déšť a sníh.'),
         ('Co si vzít na hory za proměnlivého počasí?', 'Vrstvy: funkční tričko, teplou střední vrstvu, nepromokavou bundu, čepici a rukavice. Do batohu přibalte rezervní tričko a ponožky, protože promoknutí a ochlazení bývá největší riziko.'),
         ('Hodí se tepláky na trénink?', 'Na lehký trénink a volný čas ano. Pro náročnější pohyb jsou lepší střihy z technických materiálů, které lépe odvádějí pot a nebrání v pohybu.'),
         ('Jak poznám dobrou sportovní podprsenku?', 'Dobrá podprsenka podpírá bez bolestivého tlaku, nesjíždí a nedře. Zkuste při zkoušení vyskočit a zamávat rukama. Míra opory by měla odpovídat náročnosti sportu.'),
         ('Kdy se vyplatí kupovat zimní bundy se slevou?', 'Na jaře a začátkem léta, kdy obchody uvolňují sklad pro novou kolekci. Rizikem je omezený výběr velikostí, takže se rozhodněte rychle a ověřte střih.')],
)

# ------------------------------------------------------------------ sportovni-tricka
NEW['sportovni-tricka'] = dict(long=True,
    title='Sportovní trička a tílka: jak vybrat | Sporteka',
    desc='Sportovní trička, funkční trička, tílka a polokošile. Průvodce materiálem a střihem pro běh, fitness i turistiku a porovnání nabídek českých e-shopů.',
    intro='<p><strong>Sportovní tričko</strong> je základ každé výbavy, a přesto se v nabídce velmi liší. Jiné tričko patří na maraton, jiné do posilovny, jiné na túru a jiné do města. Rozdíly dělá materiál, střih, švy a schopnost odvádět pot, a právě v nich se skrývá komfort při pohybu.</p>'
          '<p>Na Sportece najdete <a href="/funkcni-tricka/">funkční trička</a>, <a href="/tilka/">tílka a topy</a> i <a href="/polokosile/">polokošile</a> z českých e-shopů. Můžete je třídit podle značky, velikosti a nabídky a porovnávat, ve kterých obchodech je zboží skladem. Průvodce níže vysvětluje materiály, střihy, péči a časté chyby, abyste vybrali tričko, ve kterém se opravdu dobře sportuje.</p>',
    guide='<h2>Z čeho se sportovní trička vyrábějí</h2>'
          '<p>Materiál rozhoduje o tom, jak se tričko chová při potu. Čím rychleji vlhkost odvede a vysuší, tím méně vás chladí a dře. Většina moderních sportovních triček je ze syntetických vláken, ale oblíbené je také merino a bavlna ve směsích.</p>'
          + T(['Materiál', 'Výhody', 'Nevýhody', 'Hodí se na'], [
              ['Polyester', 'rychle schne, lehký, odolný', 'může zadržovat pach', 'běh, fitness, kolo'],
              ['Polyamid', 'hladký, pevný', 'méně prodyšný než polyester', 'náročnější aktivity'],
              ['Merino vlna', 'pomalu pachne, hřeje i mokré', 'jemnější, hůř odolává oděru', 'turistika, vícedenní túry'],
              ['Bavlna', 'příjemná na dotek', 'nasákne a pomalu schne', 'volný čas, lehká chůze'],
              ['Směsi s elastanem', 'pružnost, přiléhavost', 'méně dýchají při vysokém podílu', 'jóga, posilovna, tanec']]) +
          '<p>Na mnoha tričkách najdete označení jako dry, quick dry nebo cool. Jde o marketingová pojmenování technologií výrobce. Skutečnou vlastnost poznáte podle složení na štítku a podle toho, jak se tričko vysuší po první zátěži.</p>'
          '<h2>Střih a švy</h2>'
          '<p>Střih ovlivňuje volnost pohybu a to, zda tričko dře. Přiléhavý střih nepřekáží při běhu a dobře odvádí pot, volnější se hodí na procházky a volný čas. Důležité jsou švy: ploché a málo vystupující švy zabraňují odření, hlavně v podpaží a na ramenou, kde se zatížení opakuje. Také štítky ve výstřihu mohou dráždit, proto je mnoho výrobců tiskne přímo na látku.</p>'
          '<ul><li><strong>Krátký rukáv</strong> je nejuniverzálnější a hodí se do většiny počasí.</li>'
          '<li><strong>Dlouhý rukáv</strong> chrání před sluncem a chladem, na jaro a podzim je praktický a umožňuje bez další vrstvy ráno vyrazit.</li>'
          '<li><strong>Tílko</strong> nechává ramena volná a v horku chladí nejvíc.</li>'
          '<li><strong>Delší zadní díl</strong> chrání záda při předklonu, třeba u kola.</li></ul>'
          '<h2>Druhy triček podle použití</h2>'
          '<h3>Funkční trička</h3>'
          '<p>Kategorie <a href="/funkcni-tricka/">funkčních triček</a> zahrnuje lehké kousky na běh, kolo a turistiku. Měla by sedět přiléhavě, ale bez škrcení, a mít prodyšné panely v místech, kde se nejvíc potíte. Pro delší pobyty v přírodě se vyplatí odolnost vůči pachu a rychlé schnutí, aby tričko vydrželo i několik dní bez praní.</p>'
          '<h3>Tílka a topy</h3>'
          '<p>V sekci <a href="/tilka/">tílka a topy</a> najdete lehké kousky na horké dny, do posilovny nebo k jógě. Tílka mají volné paže, ale pozor na tření ramínek při nošení batohu. Kratší topy se kombinují s vysokým pasem legín nebo kraťasů, delší tílka kryjí boky. Ženy, které potřebují oporu, kombinují top se <a href="/sportovni-podprsenky/">sportovní podprsenkou</a>.</p>'
          '<h3>Polokošile</h3>'
          '<p><a href="/polokosile/">Polokošile</a> mají límeček a knoflíkovou légu, takže se hodí tam, kde je potřeba vypadat upraveně: golf, tenis, klubový trénink nebo cesta do kanceláře. Piké úplet dobře dýchá a nemačká se, funkční varianty z polyesteru rychle schnou. Límeček navíc chrání krk před sluncem.</p>'
          '<h3>Dresy a týmová trička</h3>'
          '<p>Fanouškovské <a href="/dresy/">dresy</a> a týmová trička se prodávají v replice i v hráčské verzi. Replika bývá volnější a vhodná na každodenní nošení, hráčská verze je přiléhavější a lehčí. Pokud dres neslouží ke sportování, nemusíte řešit odvod potu, stačí pohodlí a velikost.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>U triček se řiďte hlavně obvodem hrudníku a délkou trupu. Porovnejte je s tabulkou výrobce, která se mezi značkami liší. Americké střihy bývají prostornější, evropské užší. Pokud váháte mezi dvěma velikostmi, zvolte menší u přiléhavých funkčních modelů a větší u bavlněných, která se mohou srazit.</p>'
          + T(['Situace', 'Doporučení'], [
              ['Běh a rychlé aktivity', 'přiléhavý střih bez volné látky'],
              ['Turistika s batohem', 'střih bez tlaku na ramenou, rychleschnoucí materiál'],
              ['Jóga a fitness', 'pružný materiál, který se při předklonu nezvedá'],
              ['Volný čas', 'volnější střih podle chuti'],
              ['Chladné počasí pod bundou', 'těsnější tričko s dlouhým rukávem']]) +
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídka je od ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('gap', 'Gap'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('4f', '4F'), ('dynafit', 'Dynafit'), ('craft', 'Craft'), ('lotto', 'Lotto'), ('progress', 'Progress')) + '. Dynafit a Craft se zaměřují na výkonnostní oblečení pro vytrvalostní sporty, 4F a Progress na dostupnější sportovní a volnočasové kousky, Gap a Tommy Hilfiger spíše na módní bavlněná trička. Podle účelu proto zvolte správnou skupinu.</p>'
          '<h2>Péče o sportovní trička</h2>'
          '<p>Funkční materiály se perou šetrně. Použijte teplotu podle štítku, bez aviváže a ideálně obrácená naruby, aby se chránil potisk. Aviváž zanáší vlákna a snižuje jejich schopnost odvádět vlhkost. Trička perte po každé větší zátěži, protože pot a bakterie způsobují pach, který se hůř odstraňuje, když zaschne. Sušení v sušičce jen na nízkou teplotu a jen pokud štítek dovoluje.</p>'
          '<ul><li>Merino sušte naplocho, aby se nevytáhlo.</li>'
          '<li>Potištěná trička perte naruby a nežehlete na potisk.</li>'
          '<li>Zápach z polyesteru pomůže odstranit namočení do vody s octem před praním.</li>'
          '<li>Bílá trička perte zvlášť od barevných.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<p>Nejčastější chybou je nošení bavlněného trička na intenzivní sport, kdy se promočí a při zastavení chladí. Další chybou je příliš těsná velikost, která omezuje dýchání a pohyb. Opačně příliš volné tričko se při běhu třepotá a dře. Mnoho lidí opomíjí štítky a švy, které se při dlouhé zátěži projeví odřením. Poslední chybou je praní s aviváží, které funkční tkaninu časem poškodí.</p>'
          '<h2>Jaká trička pro koho</h2>'
          '<p>Začínající sportovec bude spokojený s dvěma třemi polyesterovými tričky a obměnou podle počasí. Pro turisty na vícedenní túry je zajímavé merino. Fanoušci si vyberou dres, kdo hledá úpravnější vzhled, sáhne po polokošili. Děti potřebují především odolná a pohodlná trička, která snesou časté praní. Pro seniory je důležitá jemná látka, která nedráždí kůži, a střih s dostatečnou volností.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Trička se často prodávají ve slevách na konci sezóny. Sporteka porovná nabídky více obchodů, takže uvidíte, kde je vaše velikost skladem. Při koupi se podívejte na složení a popis střihu a po doručení tričko vyzkoušejte při pohybu, ne jen při stání. Pokud sedí, vyplatí se koupit druhý kus pro střídání, protože při pravidelném sportu praní probíhá často.</p>',
    faq=[('Jaké tričko je nejlepší na běh?', 'Lehké přiléhavé tričko z polyesteru nebo směsi s elastanem s plochými švy. Dobře odvádí pot a rychle schne. Při chladnějším počasí zvolte dlouhý rukáv.'),
         ('Je bavlněné tričko vhodné na sport?', 'Na lehkou chůzi nebo volný čas ano, na náročný pohyb ne. Bavlna nasákne potem, těžkne a pomalu schne, takže při zastavení vás ochlazuje.'),
         ('Čím se liší funkční tričko od běžného?', 'Funkční tričko je vyrobeno z vláken, která odvádějí vlhkost od těla a rychle schnou. Má obvykle anatomický střih, ploché švy a někdy prodyšné panely.'),
         ('Jak odstranit pach z funkčního trička?', 'Perte po každém použití a nenechávejte tričko ve vlhkém koši. Pomůže předchozí namočení do vody s octem a vynechání aviváže. Syntetika pach zadržuje víc než merino.'),
         ('Jak poznat správnou velikost trička?', 'Zkontrolujte, že švy ramen sedí na ramenou, rukávy nesvírají paži a tričko dostatečně zakrývá záda při předklonu. U funkčního modelu má tkanina přiléhat, ne škrtit.'),
         ('Kdy zvolit tílko místo trička?', 'V horku, na cvičení a při sportech, kde potřebujete volná ramena. Pokud nosíte batoh, může ramínka tření dráždit, tehdy je lepší tričko s krátkým rukávem.'),
         ('Hodí se merino na léto?', 'Ano, tenké merino dobře reguluje teplotu i v horku a pomalu pachne. Nevýhodou je vyšší citlivost na oděr, proto se nehodí pod těžký batoh.'),
         ('Čím se polokošile liší od trička?', 'Polokošile má límeček a krátkou légu na knoflíky, takže vypadá upraveněji. Funkční varianty z polyesteru se používají třeba na golf a tenis.'),
         ('Může se tričko po praní srazit?', 'Bavlněné a směsové ano, hlavně při vysoké teplotě a sušení v sušičce. Funkční syntetika se obvykle nesráží, ale teplo může poškodit potisk a elastické vlákna.'),
         ('Jak často měnit sportovní trička?', 'Když ztratí tvar, začnou propouštět pot nebo vyblednou či se roztřepí švy. Při pravidelném sportu to bývá po několika sezónách, u kvalitních kousků i později.'),
         ('Je lepší dlouhý rukáv na kolo?', 'V chladnějších dnech ano, na jaře a na podzim zahřeje bez další vrstvy. V létě chrání před sluncem, pokud je materiál lehký a prodyšný.')],
)

# ------------------------------------------------------------------ extensions (extra sections appended to the guides above)
NEW['sportovni-obuv']['guide'] += (
    '<h2>Dětská a juniorská obuv</h2>'
    '<p>U dětí rozhoduje ohebnost přední části a pevné držení paty. Příliš tuhá podrážka brání přirozenému odvalu chodidla, příliš měkká zase nedrží nohu při běhu po hřišti. Šněrování nebo suchý zip musí jít utáhnout samostatně, jinak dítě boty nechává povolené a hrozí zakopnutí. Pro školní tělocvik pořiďte světlou podrážku, která nezanechává stopy, a na hřiště druhý pár určený na venek. Mladší sportovci rostou ve skocích, takže sledujte, jestli se prsty neopírají o špičku.</p>'
    '<h2>Nákup do dlouhodobé zátěže</h2>'
    '<p>Pokud boty používáte denně v práci, třeba ve zdravotnictví, ve skladu nebo v obchodě, hledejte lehkou konstrukci, protiskluzovou podrážku a vložku, kterou lze vyměnit za ortopedickou. U sportovců, kteří trénují několikrát týdně, se vyplácí mít dvě různé boty: jednu na rychlejší tréninky a druhou na pomalé dlouhé jednotky.</p>')

NEW['tenisky']['intro'] += '<p>Na stránce najdete také odkazy na jednotlivé značky, takže si můžete rychle prohlédnout, co která nabízí.</p>'
NEW['tenisky']['guide'] += (
    '<h2>Barvy, kombinace a styl</h2>'
    '<p>Neutrální odstíny jako bílá, černá, šedá a béžová se hodí téměř ke všemu a vizuálně nezestárnou. Výrazné barvy zase oživí jednoduchý outfit, ale bývají méně univerzální. Bílé tenisky působí svěže, vyžadují však častější čištění. Tmavé modely skryjí drobné nečistoty a hodí se do deště nebo na cesty. Kůže v jednobarevném provedení se snadno kombinuje s kalhotami i sukní, zatímco výrazné retro kousky potřebují klidné doplňky.</p>'
    '<h2>Ortopedie, vložky a zdravá chůze</h2>'
    '<p>Pokud máte plochá chodidla nebo používáte ortopedické vložky, vybírejte modely s vyjímatelnou vložkou a dostatečnou výškou svršku. Hluboká pata pomáhá chodidlu zůstat stabilní a širší špička dává prostor pro prsty. Chůze v pevných, ale pružných botách je pro tělo příjemnější než v příliš tvrdých, takže při bolesti kloubů dejte přednost mírnému tlumení. Problémy se zády, koleny nebo chodidly je však nejlepší konzultovat s odborníkem, ne řešit jen botami.</p>'
    '<h2>Cestování a práce vstoje</h2>'
    '<p>Na cesty se hodí lehké tenisky, které se rychle suší a dobře se balí. Pro dlouhé stání v práci zvolte měkčí mezipodešev a přiměřeně pevný opěrný střed. Ověřte si také, zda se bota snadno obouvá a zouvá, pokud často procházíte kontrolou nebo vstupujete do domů, kde se zouvá. Dvojice, kterou nosíte každý den, by měla mít hladší podrážku, aby se pod ní nezachytávaly drobné kamínky, a odolný svršek, který se dá vyčistit.</p>'
    '<h2>Reklamace a vrácení</h2>'
    '<p>Při online nákupu máte zpravidla právo zboží vrátit ve stanovené lhůtě, podmínky ale určuje konkrétní prodejce. Boty zkoušejte doma na čistém povrchu a ponechte originální krabici i štítky. Pokud se po krátké době odlepí podrážka nebo se objeví vada materiálu, uplatněte reklamaci. Opotřebení běžným nošením se však za vadu nepovažuje.</p>')

NEW['sportovni-obleceni']['guide'] += (
    '<h2>Dětské a juniorské oblečení</h2>'
    '<p>Děti rostou rychle a pohybují se jinak než dospělí, takže jim sedí hlavně volnější střih, měkké švy a materiály, které vydrží časté praní. Prakticky se osvědčují kalhoty se zesílenými koleny, bundy s nastavitelnou kapucí a trička z rychleschnoucího materiálu. U menších dětí zvažte zip, který jde otevřít jednou rukou. Oblečení kupujte spíše s malou rezervou ve velikosti, ale ne tak velké, aby překáželo, třeba při lezení nebo jízdě na kole. Pro zimní hry se hodí <a href="/detske-plavky/">dětské plavky</a> na léto a overal na zimu.</p>'
    '<h2>Ženy, muži a unisex</h2>'
    '<p>Dámské střihy zohledňují užší ramena a výraznější boky, pánské jsou rovnější. Unisex kousky bývají volnější a hodí se hlavně na mikiny a trička. Pokud vám střih sedí lépe z opačné řady, není problém ho zvolit, důležité je pohodlí a volnost pohybu. Pro sportovní podprsenky nebo legíny ale platí, že přizpůsobení tvaru těla je zásadní.</p>'
    '<h2>Reflexní prvky a bezpečnost</h2>'
    '<p>Při pohybu za šera pomáhají reflexní pruhy, které odráží světla aut a cyklistů. Nejlépe fungují na pohyblivých částech těla, tedy na rukávech a kotnících, protože pohyb přitahuje pozornost řidičů. Světlé barvy jsou viditelnější než černá, a proto se hodí na večerní běh a jízdu na kole. Kromě oblečení si můžete pořídit reflexní pásek nebo čelovku.</p>'
    '<h2>Sezónní plán nákupu</h2>'
    '<p>Rozumný přístup je kupovat základ celoročně a sezónní kousky při výprodejích. Jaro přináší větrovky a lehké mikiny, léto kraťasy, plavky a tílka, podzim softshelly a fleece, zima péřové bundy a termo prádlo. Když po sezóně necháte věci pořádně vyprat, vysušit a uložit, další rok je vytáhnete v dobrém stavu. Nenavlhlé oblečení uložte do prodyšného obalu, ne do uzavřeného plastu.</p>'
    '<h2>Ekologické a udržitelné volby</h2>'
    '<p>Kvalitní kousky vydrží víc sezón, a proto je dlouhá životnost nejjednodušší cestou ke šetrnějšímu nákupu. Perte při nižších teplotách a pouze když je potřeba. Poškozené zipy a švy se dají opravit, což je často levnější než koupě nového oděvu. Některé značky používají recyklovaný polyester, informace najdete v popisu produktu.</p>')

NEW['sportovni-tricka']['guide'] += (
    '<h2>Trička na jednotlivé sporty</h2>'
    '<p>Pro <strong>vytrvalostní běh</strong> je vhodné tričko s minimem švů a lehkým materiálem, který se při potu nelepí k tělu. Při <strong>jízdě na kole</strong> pomáhá delší záda, kapsy na zádech nebo zip u krku, který umožní větrání. <strong>Posilovna</strong> a <strong>crossfit</strong> kladou důraz na pružnost, protože se tričko nesmí zvedat při zdvihu rukou. Na <strong>turistiku</strong> se nosí rychleschnoucí materiály s ochranou před sluncem a při delších trasách je výhodou pomalé pachnutí. <strong>Týmové sporty</strong> využívají dresy a trička s větracími panely, která se dobře perou a snesou hrubější kontakt.</p>'
    '<h2>Vrstvení s tričkem</h2>'
    '<p>Tričko je nejčastěji spodní vrstva, nad kterou se přidává <a href="/mikiny/">mikina</a> nebo <a href="/sportovni-bundy/">bunda</a>. Pod bundu zvolte tričko s dlouhým rukávem z jemné syntetiky nebo merina, ať odvádí pot od kůže. Pod teplou vrstvu se hodí těsnější střih, který se nesroluje a nevytváří záhyby. V létě naopak tričko slouží jako jediná vrstva, a proto se vyplatí kvalitní a prodyšný materiál.</p>'
    '<h2>Ochrana před sluncem a hmyzem</h2>'
    '<p>Lehké tričko s dlouhým rukávem poskytuje částečnou ochranu před sluncem a hmyzem. Některá trička mají označení ochrany proti UV záření, což je třeba brát jako doplněk, nikoli náhradu opalovacího krému. Světlé barvy odrážejí teplo, tmavé zase lépe skrývají pot. Při turistice po otevřené krajině se osvědčuje tričko s vyšším límcem nebo zipem.</p>'
    '<h2>Kombinace s dalším oblečením</h2>'
    '<p>Trička kombinujte s <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/leginy/">legínami</a> nebo <a href="/sportovni-kalhoty/">sportovními kalhotami</a>. Pro chladnější dny přidejte <a href="/termopradlo/">termo prádlo</a> pod tričko, pro horké zvolte lehké tílko. Při návštěvě posilovny se hodí tričko, které se nepřilepí ke zpoceným zádům, a ručník na krk.</p>'
    '<h2>Barvy, potisky a logo</h2>'
    '<p>Světlé barvy odrážejí teplo, tmavé skrývají skvrny a pot. Potisky a nášivky mohou omezit pružnost a prodyšnost, pokud jsou velké a pogumované. Reflexní prvky jsou užitečné při běhání za šera. U týmových triček a dresů se barvy a loga často mění podle sezóny, takže starší kolekce mívají nižší nabídku velikostí.</p>')

NEW['sportovni-obleceni']['intro'] += '<p>U každé části výbavy najdete také značky a velikosti, které mají obchody právě skladem.</p>'
NEW['sportovni-obleceni']['guide'] += (
    '<h2>Kolik kousků skutečně potřebujete</h2>'
    '<p>Pro pravidelný pohyb stačí menší počet univerzálních věcí, které se dají kombinovat. Tři trička, dvoje kalhoty nebo legíny, jedna mikina a lehká bunda pokryjí většinu běžných situací. Více kusů dává smysl, až když přibudou specializované aktivity, třeba lyžování nebo plavání.</p>')
NEW['sportovni-tricka']['intro'] += '<p>Nechybí ani přehled značek a rady k praní.</p>'
NEW['sportovni-tricka']['guide'] += (
    '<h2>Kolik triček potřebujete</h2>'
    '<p>Při pravidelném sportování stačí čtyři až pět kusů, abyste měli vždy čisté a suché. Dvě lehká trička na horké dny, jedno s dlouhým rukávem a jedno teplejší na vrstvení pokryjí většinu sezóny. Pokud vyrážíte na vícedenní túru, zvolte kus, který se rychle suší přes noc.</p>')
NEW['tenisky']['guide'] += (
    '<h2>Tenisky pro děti a teenagery</h2>'
    '<p>Mladší děti potřebují lehké boty s měkkou špičkou, které snesou běhání po hřišti, a starší si často vyberou podle módy. U obou skupin se vyplatí zkontrolovat, zda je podrážka dostatečně ohebná a pata pevná. Jeden pár do školy a druhý na ven snižuje opotřebení a umožňuje boty střídavě sušit. Drobné kamínky a písek se z vzorku podrážky odstraňují snadno, když je hlubší.</p>'
    '<h2>Tenisky do kanceláře a na každý den</h2>'
    '<p>Kde dress code dovoluje, nahrazují tenisky společenskou obuv. Vhodné jsou jednobarevné, čisté a bez výrazných log. Kožené nebo semišové modely v tmavých tónech působí upraveněji než svítivé běžecké. Před prvním nošením zkontrolujte, zda se podrážka nelepí na mokrou dlažbu a zda jsou boty dostatečně prodyšné na celý pracovní den.</p>')
