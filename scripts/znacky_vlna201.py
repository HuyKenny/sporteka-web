"""sporteka.cz — brand texts wave 201: adidas, nike, skechers, puma.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ adidas
NEW['adidas'] = dict(
    title='Adidas: tenisky, kopačky a oblečení ve srovnání obchodů',
    desc='Adidas v katalogu Sporteky: tenisky, trailové boty, kopačky, trička a tepláky. Jak vybrat řadu, velikost a kdy hledat slevy mezi obchody.',
    intro='<p>Adidas je v katalogu Sporteky jednou z nejširších značek: vedle obuvi tu najdete oblečení, doplňky a fotbalovou výbavu pro dospělé i děti. Zdaleka nejvíc nabídky tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, hned za nimi se řadí trailová a turistická obuv, <a href="/kopacky/">kopačky</a> a basketbalové modely. '
          'Textilní část pokrývají trička, kraťasy, <a href="/teplaky/">tepláky</a> a <a href="/mikiny/">mikiny</a>. Na této stránce vysvětlujeme, jak se v tak velké nabídce zorientovat: podle koho obuv koupit, jak poznat řady kopaček, kdy dává smysl značková turistická bota a jak sledovat slevy. Sporteka sama nic neprodává, ceny a dostupnost jednotlivých velikostí porovnává napříč obchody, takže vždy uvidíte, u kterého prodejce je vaše číslo skladem a za jakých podmínek se dá zboží vrátit.</p>',
    guide='<h2>Co Adidas v katalogu nabízí</h2>'
          '<p>Skladba sortimentu značky je dobře čitelná z kategorií. Většinu tvoří obuv, takže kdo hledá značku Adidas, nejčastěji hledá boty. Textil a doplňky jsou menší, ale pestré část nabídky a jejich výběr stojí za samostatný pohled.</p>'
          + T(['Skupina', 'Kategorie značky', 'Typický zájemce'], [
              ['Každodenní obuv', '<a href="/tenisky/">tenisky a volnočasové boty</a>', 'město, škola, práce, cestování'],
              ['Outdoor', '<a href="/trailove-boty/">trailové boty</a> a turistická obuv', 'běh v terénu, výlety, chůze po stezkách'],
              ['Fotbal', '<a href="/kopacky/">kopačky</a>, <a href="/dresy/">dresy</a>, chrániče, míče', 'tréninky, zápasy, týmové vybavení'],
              ['Hala a kurt', '<a href="/salova-obuv/">sálová obuv</a>, <a href="/tenisova-obuv/">tenisová obuv</a>, <a href="/basketbal/">basketbal</a>', 'florbal, házená, volejbal, tenis, basketbal'],
              ['Oblečení', '<a href="/sportovni-tricka/">trička</a>, <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/teplaky/">tepláky</a>, <a href="/mikiny/">mikiny</a>', 'trénink i volný čas']]) +
          '<p>V katalogu jsou zastoupeny všechny hlavní skupiny kupujících. Dámské a pánské zboží má podobně velký podíl, dětské modely tvoří výrazný třetí díl a unisex kousky jsou spíš výjimkou. Pro rychlé zúžení proto využijte filtr „Pro koho“ a až poté vybírejte barvu a velikost. Z barev dominuje černá, hned po ní bílá; modrá, šedá a béžová už jsou vzácnější.</p>'
          '<h2>Tenisky a volnočasové boty</h2>'
          '<p>Nejpočetnější kategorie je pro Adidas zároveň nejméně sportovní. Najdete tu klasické nízké modely, kožené i textilní, ale i kousky s tenisovým původem, jako je řada Grand Court. Jejich silueta je jednoduchá, podešev nízká a vzhled univerzální. Hodí se do města a do kanceláře s neformálním dress codem, na delší chůzi je však lepší mít pružnější a měkčí podrážku.</p>'
          '<ul><li><strong>Kůže nebo syntetika:</strong> kůže se postupně vytvaruje podle nohy, syntetický svršek se lépe čistí a méně nasákne.</li>'
          '<li><strong>Podešev:</strong> tenká gumová drží dobře na hladkém povrchu, tlustší tlumí nárazy při celodenní chůzi.</li>'
          '<li><strong>Bílé provedení:</strong> vypadá čistě, ale na prvním výletě se zašpiní. Počítejte s údržbou nebo sáhněte po tmavší barvě.</li>'
          '<li><strong>Šněrování nebo suchý zip:</strong> u dětí šetří ráno čas, u dospělých je šněrování přesnější.</li></ul>'
          '<p>Chcete-li si rychle projít jen tuto kategorii, použijte přímo stránku <a href="/tenisky/">tenisky</a> a zúžte nabídku na značku Adidas.</p>'
          '<h2>Kopačky: jak číst názvy řad</h2>'
          '<p>Kopačky patří mezi největší skupiny a v názvech se opakují jména řad. V katalogu se setkáte s modely F50, Predator a Copa; ve vzorku zboží figurují i verze League, Club nebo Pure. Přesnou charakteristiku každé řady uvádí výrobce na produktové kartě. Pro výběr si zapamatujte tři praktické věci.</p>'
          '<ol><li><strong>Povrch.</strong> Zkratka FG/MG značí pevný a mírně měkký přírodní trávník, AG umělou trávu s nízkými kolíky. Na umělou trávu s hustým povrchem patří kopačky přímo určené pro umělý trávník, ne kolíkované.</li>'
          '<li><strong>Úroveň.</strong> Označení jako League nebo Club míří na amatérskou hru a tréninky, vyšší řady jsou lehčí a dražší. Pro začínajícího hráče nebo dítě je vyšší řada zbytečná.</li>'
          '<li><strong>Svršek.</strong> Textilní nebo syntetické materiály jsou lehké a nepromokavé, kůže je měkčí a tvaruje se. Pro dětský růst záleží víc na správné velikosti než na materiálu.</li></ol>'
          '<p>Podrobnější průvodce zvolenou značkou najdete na stránce <a href="/kopacky-adidas/">kopačky Adidas</a>, obecné rady k výběru v kategorii <a href="/kopacky/">kopačky</a>. Sálové boty pro halový fotbal jsou jiný produkt: mají plochou podešev bez kolíků a patří do kategorie <a href="/salova-obuv/">sálová obuv</a>. Jednoduše je rozeznáte tak, že na dně nemají žádné výstupky.</p>'
          '<h2>Běh, trail a turistika</h2>'
          '<p>Trailová kategorie je u Adidasu překvapivě velká, protože se do ní řadí i boty z outdoorové linie Terrex, tedy turistická obuv s membránou nebo bez ní. Rozdíl mezi trailovým během a turistikou je v tom, co od obuvi chcete. Pro běh potřebujete lehkou botu s hrubším vzorkem podešve a bezpečným uchycením paty; pro chůzi s batohem tužší podešev a oporu kotníku.</p>'
          + T(['Požadavek', 'Trailová běžecká bota', 'Turistická bota'], [
              ['Hmotnost', 'nízká, bota se při kroku nemá vlát', 'vyšší, kvůli stabilitě'],
              ['Podešev', 'vzorek s kolíky pro držení v bahně a na kamenech', 'tužší, odolnější proti odření'],
              ['Vodotěsnost', 'obvykle volitelná, častěji prodyšná síť', 'membrána chrání v dešti a ve sněhu'],
              ['Použití', 'rychlý pohyb po stezkách', 'celodenní trasy, zátěž v batohu']]) +
          '<p>Pokud označení u modelu obsahuje GORE-TEX nebo jinou membránu, počítejte s nižší prodyšností. V létě a při rychlém běhu raději vybírejte síťovanou verzi, na podzim a v zimě naopak membránu. Pro běžce na silnici je lepší otevřít stránku <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> a pro společné srovnání stránku <a href="/adidas-bezecke-boty/">běžecké boty Adidas</a>. Pro delší výlety slouží výběr <a href="/adidas-trekove-boty/">trekové boty Adidas</a>.</p>'
          '<h2>Oblečení: trička, mikiny, tepláky</h2>'
          '<p>Textil značky je v katalogu postavený na základních kouscích. Typické jsou trička s velkým logem, mikiny na zip typu French Terry, tepláky s jednoduchým střihem a kraťasy na trénink. Sportovní trička z umělého vlákna odvádějí pot rychleji než bavlněná, naopak čistě bavlněné kousky jsou příjemnější do města, ale po mokré aktivitě schnou pomalu.</p>'
          '<p>U tepláků a mikin sledujte střih: úzký (slim) vypadá elegantněji, volnější je pohodlný na doma a při tréninku. Značka používá obvykle označení velikostí S až XL, u dětí číselně podle výšky. Pokud váháte mezi dvěma velikostmi, otevřete tabulku v obchodě a přeměřte konkrétní kus. Další informace najdete v kategoriích <a href="/teplaky/">tepláky</a>, <a href="/mikiny/">mikiny</a> a <a href="/sportovni-kratasy/">kraťasy</a>.</p>'
          '<h2>Pro koho vybírat: dámské, pánské, dětské</h2>'
          '<p>Nabídka je rozdělená téměř rovnoměrně mezi dámy a pány, ale děti tvoří významnou část. Pro děti platí zvláštní pravidla. Dětská noha roste rychle, takže se vyplatí koupit botu s rezervou na prsty, ne o celé číslo větší. Při převodu mezi označeními velikostí hledejte u každé boty délku vložky v centimetrech; ta je spolehlivější než číslo.</p>'
          '<ul><li><strong>Dámské modely:</strong> bývají užší v oblasti paty a mají mírně odlišné tvarování podešve.</li>'
          '<li><strong>Pánské modely:</strong> jsou širší a v prstech prostornější.</li>'
          '<li><strong>Dětské modely:</strong> mají měkčí zakončení kolem kotníku a častěji suchý zip nebo gumové tkaničky.</li>'
          '<li><strong>Junior velikosti:</strong> často sedí i drobnějším ženám, což může být levnější cesta, pokud je produkt k dispozici.</li></ul>'
          '<h2>Jak sedí velikosti a jak o boty pečovat</h2>'
          '<p>Obuv Adidas sedí obvykle věrně číslu, ale mezi řadami se střih mění. Širší nohy dávají přednost modelům s jednoduchým svrškem, štíhlé kousky bývají vhodné na sprint a kopačky. Vždy se řiďte měřením vložky, ne tím, co máte doma ve skříni. Boty zkoušejte odpoledne, kdy je chodidlo největší.</p>'
          '<p>Péče se liší podle materiálu. Kůži po každém namočení nechte schnout při pokojové teplotě, nikdy na topení. Textilní boty se čistí kartáčem s mýdlovou vodou; pračka zkracuje životnost lepidla. Kopačky po zápase očistěte od hlíny a vyndejte vložku, aby vyschla. Zimní dres nebo mikinu vyperte naruby a bez aviváže, která zhoršuje odvod potu u funkčních materiálů.</p>'
          '<h2>Značka a konkurence</h2>'
          '<p>Při výběru mezi velkými značkami se často rozhoduje podle střihu a dostupnosti. Pro srovnání otevřete stránky <a href="/znacka/nike/">Nike</a>, <a href="/znacka/puma/">Puma</a> a <a href="/znacka/skechers/">Skechers</a>. U Adidasu vynikne šíře fotbalového vybavení, od kopaček po chrániče a míče, a turistická obuv s označením Terrex. Skechers je v katalogu zaměřený hlavně na pohodlnou vycházkovou obuv, Nike a Puma mají vedle bot silné zastoupení kopaček a oblečení.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Sporteka porovnává obchody, takže uvidíte, kdo má stejný kus výhodněji. Největší rozdíly bývají u starších kolekcí a u barev, které už výrobce nezařazuje do nové řady. Pomáhá několik pravidel.</p>'
          '<ul><li>Sledujte konec sezóny: zimní mikiny a bundy jsou nejlevnější na jaře, letní kraťasy a sandály na podzim.</li>'
          '<li>Hledejte předchozí generaci kopaček. Rozdíl oproti nové je pro většinu hráčů minimální.</li>'
          '<li>Porovnávejte i dopravu a možnost vrácení; rozdíl v poštovném někdy převáží cenovou výhodu.</li>'
          '<li>Při nákupu více kusů zkontrolujte, zda se nabídky obchodů při změně velikosti nemění.</li>'
          '<li>Zboží s poslední velikostí bývá výhodnější, ale jen pokud sedí; nekupujte jen kvůli slevě.</li></ul>'
          '<p>Pokud se chystáte vybavit celý tým, podívejte se také na plavky a rukavice: najdete je na stránkách <a href="/plavky-adidas/">plavky Adidas</a> a <a href="/brankarske-rukavice-adidas/">brankářské rukavice Adidas</a>.</p>',
    faq=[
        ('Jaké zboží Adidas na Sporteka převažuje?', 'Největší část tvoří tenisky a volnočasová obuv, za nimi trailové a turistické boty, kopačky a basketbalové modely. Z oblečení jsou nejvíc zastoupená trička, kraťasy, tepláky a mikiny. Poměr se mění podle sezóny a dostupnosti v obchodech.'),
        ('Jak poznám, že kopačky Adidas sedí na můj povrch?', 'Podívejte se na zkratku v názvu. FG značí pevný přírodní trávník, MG měkčí, AG umělou trávu. Pro hustý umělý povrch hledejte obuv označenou jako kopačky na umělý trávník a pro halu zvolte sálovou obuv bez kolíků.'),
        ('Je lepší koupit vyšší řadu kopaček, nebo League či Club?', 'Pro tréninky, amatérskou hru a děti stačí řady League a Club. Vyšší řady jsou lehčí a z jemnějších materiálů, ale rozdíl pocítí hlavně pokročilí hráči. Důležitější než řada je správná velikost a typ povrchu.'),
        ('Čím se liší trailové běžecké boty od turistických?', 'Trailová bota je lehčí, flexibilnější a míří na rychlý pohyb po stezkách. Turistická bota je tužší, stabilnější a chrání kotník i chodidlo při zátěži v batohu. Pokud chodíte s těžším batohem, zvolte turistickou, na běh trailovou.'),
        ('Sedí obuv Adidas větší, nebo menší?', 'Obvykle sedí podle čísla, ale rozdíly jsou mezi řadami. Spolehlivější než číslo je délka vložky v centimetrech, kterou uvádí výrobce nebo obchod. Boty zkoušejte odpoledne a s ponožkou, kterou budete nosit.'),
        ('Jak vyčistit bílé tenisky, aby nezežloutly?', 'Použijte kartáč, vlažnou vodu a jemné mýdlo a boty nechte schnout při pokojové teplotě. Pračka a topení poškozují lepení i materiál. Šněrovadla vyperte zvlášť a vložky vyndejte, aby uschly.'),
        ('Kdy bývají sportovní věci Adidas nejvýhodnější?', 'Nejlepší příležitosti jsou na konci sezóny a při výprodeji starších kolekcí. Zimní oblečení bývá levnější na jaře, letní na podzim. Na Sporteka stačí porovnat obchody podle konkrétní velikosti.'),
        ('Najdu tu dětské věci značky?', 'Ano, dětské zboží tvoří významnou část nabídky, od kopaček přes tenisky až po tepláky a trička. U dětí sledujte délku vložky a kupujte s malou rezervou, protože příliš velká bota vede ke klopýtání.'),
        ('Prodává Sporteka zboží sama?', 'Ne. Sporteka je srovnávač: ukazuje nabídky obchodů a po kliknutí vás přesměruje k prodejci. Objednávku, platbu a vrácení zboží vyřizujete přímo s obchodem.'),
    ],
)

# ------------------------------------------------------------------ nike
NEW['nike'] = dict(
    title='Nike: boty, kopačky a sportovní oblečení k porovnání',
    desc='Nike v katalogu Sporteky: tenisky, běžecké a basketbalové boty, kopačky, mikiny a dresy. Průvodce řadami, velikostmi a hledáním slev.',
    intro='<p>Značka Nike má v katalogu Sporteky největší váhu u obuvi, především u <a href="/tenisky/">tenisek a volnočasových bot</a>, ale znatelně zastoupené jsou i <a href="/basketbal/">basketbalové modely</a>, <a href="/kopacky/">kopačky</a>, <a href="/trailove-boty/">trailové boty</a> a tréninková obuv. '
          'Textil tvoří trička, dresy, <a href="/mikiny/">mikiny</a>, fleecové mikiny, bundy a kraťasy. Mezi kupujícími převažují pánská a dámská nabídka, dětské kousky jsou menší, ale stabilní skupina. V textu rozebíráme, jak se orientovat v názvech řad, čím se liší běžecké boty od tréninkových, na co si dát pozor u kopaček a pantoflí a kdy se vyplatí čekat na slevu. Sporteka neprodává sama, jen porovnává obchody, takže uvidíte, kde je dostupná právě vaše velikost, barva a jak výhodné jsou podmínky dopravy.</p>',
    guide='<h2>Z čeho se sortiment Nike skládá</h2>'
          '<p>Při pohledu na kategorie je patrné, že Nike je především obuvnická značka. Každá další kategorie je řádově menší než tenisky, přesto dohromady dávají kompletní výbavu od hlavy k patě. Nejlépe to ukazuje přehled hlavních skupin.</p>'
          + T(['Oblast', 'Kde ji najdete', 'Kdy dává smysl'], [
              ['Městské boty', '<a href="/tenisky/">tenisky</a>, pantofle, žabky', 'každodenní nošení, cestování, bazén'],
              ['Běh', '<a href="/nike-bezecke-boty/">běžecké boty Nike</a>, <a href="/trailove-boty/">trail</a>', 'pravidelný trénink na silnici nebo v lese'],
              ['Míčové sporty', '<a href="/kopacky-nike/">kopačky</a>, <a href="/basketbalove-boty-nike/">basketbalová obuv</a>', 'fotbal, basket, halové sporty'],
              ['Fitness', '<a href="/treninkova-obuv/">tréninková obuv</a>, <a href="/sportovni-kratasy/">kraťasy</a>', 'posilovna, skupinové lekce'],
              ['Oblečení', '<a href="/sportovni-tricka/">trička</a>, <a href="/mikiny/">mikiny</a>, <a href="/fleecove-mikiny/">fleece</a>, <a href="/sportovni-bundy-jaro-podzim/">bundy</a>', 'trénink i volný čas, přechodné období']]) +
          '<p>Kategorie <a href="/kosile/">turistické a outdoorové košile</a> je u Nike překvapivě početná, takže při hledání lehkého oblečení na výlet zkontrolujte, zda kus opravdu patří do této skupiny. Běžné sportovní textilie jsou v kategorii <a href="/sportovni-tricka/">sportovní trička</a>. Barevně nabídka stojí na černé a bílé, dále se objevuje šedá, modrá a červená; zajímavé barvy jako růžová nebo žlutá bývají sezónní.</p>'
          '<h2>Tenisky, pantofle a každodenní boty</h2>'
          '<p>Většina nabídky směřuje do běžného života. Jde o nízké kožené a syntetické tenisky, například z řady Court Vision, a o lehké modely Air Max. Zvlášť oblíbené jsou také pantofle a žabky Victori One. Do vody nebo na pláž zvolte právě je, protože se rychle osuší a netlačí.</p>'
          '<ul><li><strong>Court Vision:</strong> tenisový střih, jednoduchý svršek, snadno se kombinuje s džíny i tepláky.</li>'
          '<li><strong>Air Max:</strong> název řady se objevuje u tréninkových i městských modelů, přesný účel určuje popis a kategorie.</li>'
          '<li><strong>Victori One:</strong> pantofle na bazén, do sprch a po tréninku; nejsou určeny na dlouhou chůzi.</li>'
          '<li><strong>Junior velikosti:</strong> dětské modely mívají zpevněnou špici a pevnější zadní část.</li></ul>'
          '<p>Při srovnávání rozlišujte kategorii <a href="/tenisky/">tenisky</a> a <a href="/treninkova-obuv/">tréninkovou obuv</a>. Druhá má stabilnější podešev a lépe drží patu při bočních pohybech, první je určená do města a na cesty.</p>'
          '<h2>Běžecké boty: silnice, trail, vybavení</h2>'
          '<p>Značka nabízí běžecké boty pro různé typy chodidla. Pro výběr si ujasněte, kde budete běhat, jak často a s jakou váhou. Pravidelný běžec na silnici potřebuje obuv s tlumením pod patou, trailový běžec s vyšším zakončením vzorku. Názvy jako Run Defy, Structure nebo Juniper Trail ve vzorku zboží ukazují, že řady mají různé určení; popis modelu vždy napoví, zda je určen na silnici, nebo do lesa.</p>'
          '<ol><li>Změřte si chodidlo odpoledne a ponechte před prsty zhruba šířku palce.</li>'
          '<li>Vyzkoušejte botu s ponožkou, v které poběžíte, nejlépe i s vložkou, kterou používáte.</li>'
          '<li>Vyměňte boty po delší době běhání, jakmile mezipodešev ztratí pružnost.</li>'
          '<li>Pokud kolísáte mezi dvěma velikostmi, vezměte delší a víc přitáhněte tkaničky.</li></ol>'
          '<p>Základní seznam modelů pro silnici najdete na stránce <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, stejný výběr zúžený jen na značku je na stránce <a href="/nike-bezecke-boty/">běžecké boty Nike</a>. Terénní modely hledejte v kategorii <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<h2>Basketbal a halové sporty</h2>'
          '<p>V sortimentu basketbalu najdete obuv s vysokým i nízkým střihem. Vyšší kotník stabilizuje při doskoku, nízký střih je lehčí a rychlejší. Hráči, kteří si často vyvrtnou kotník, by měli sáhnout po vyšším střihu s pevnou patou. Rozhodující je také podešev: na dřevěné palubovce potřebujete jemnější vzorek, venku na betonu pevnější a odolnější gumu. Za to, že se obě venkovní podložky rychle sjíždějí, platíte kratší životností.</p>'
          '<p>Značkové modely, například Precision, mají určení naznačené už v názvu. Jednotlivé typy porovnáte na stránce <a href="/basketbalove-boty-nike/">basketbalové boty Nike</a> a obecné rady najdete v kategorii <a href="/basketbal/">basketbal</a>. Pro halový fotbal, florbal nebo házenou patří do košíku <a href="/salova-obuv/">sálová obuv</a>.</p>'
          '<h2>Kopačky Nike</h2>'
          '<p>Kopačky jsou jedním z nejvíc rozeznatelných produktů značky. V katalogu se objevují řady Mercurial a Phantom a modely s označeními Academy nebo Vapor. Zkratky v názvu určují povrch: FG pro pevný trávník, MG pro smíšený, a podobně. Academy je přístupnější řada pro amatéry, vyšší řady slouží náročnějším hráčům.</p>'
          '<ul><li>Nízký střih (Low) podporuje pohyblivost, ale nechrání kotník.</li>'
          '<li>Dětské kopačky vybírejte hlavně podle délky chodidla; příliš velké zhoršují cit pro míč.</li>'
          '<li>Pro trénink na umělé trávě je vhodnější obuv určená právě na ni než klasické kolíky.</li>'
          '<li>Světlé nebo výrazné barvy, například růžová, se hodí, pokud chcete boty snadno poznat v šatně.</li></ul>'
          '<p>Podrobnější přehled je v kategorii <a href="/kopacky/">kopačky</a>, výběr značky najdete na stránce <a href="/kopacky-nike/">kopačky Nike</a> a barevnou variantu na stránce <a href="/ruzove-kopacky-nike/">růžové kopačky Nike</a>.</p>'
          '<h2>Oblečení: mikiny, tepláky, leginy, dresy</h2>'
          '<p>V textilu převládají základní kousky pro trénink i volný čas. Mikina Club patří k nejčastějším jménům a doplňují ji fleecové varianty a bundy do přechodného počasí. Pro fotbal a běh jsou k dispozici kalhoty s technickým materiálem. Rozdíl mezi bavlněnou a funkční mikinou poznáte po zátěži: bavlna nasákne a schne pomalu, funkční vlákno pot odvádí.</p>'
          '<p>Chcete-li si prohlédnout konkrétní skupiny, otevřete stránky <a href="/nike-mikina/">mikiny Nike</a>, <a href="/nike-teplaky/">tepláky Nike</a>, <a href="/nike-kratasy/">kraťasy Nike</a>, <a href="/nike-leginy/">leginy Nike</a> a <a href="/nike-dresy/">dresy Nike</a>. Sportovní podprsenky najdete na stránce <a href="/sportovni-podprsenka-nike/">sportovní podprsenky Nike</a>.</p>'
          '<h2>Pro koho: pánské, dámské, dětské</h2>'
          '<p>Pánská nabídka je největší, dámská ji následuje a děti tvoří menší, ale stále široký díl. Rozdělení je důležité nejen kvůli střihu, ale i kvůli barvám a materiálům. Dámské modely bývají lehčí a v pase užší, pánské mají prostornější kapsy a delší střih. U dětí sledujte nejen velikost, ale i způsob zapínání: suchý zip a pružné tkaničky ušetří ráno čas, klasické tkaničky se lépe nastaví na úzkou nohu.</p>'
          '<p>Juniorské velikosti obuvi jsou vhodné i pro štíhlejší ženy s malou nohou, ale jen tehdy, pokud nepotřebujete konkrétní dámský střih. U oblečení se juniorské číslování řídí výškou, proto před nákupem dospívajícího změřte, kolik skutečně měří, a porovnejte s tabulkou v obchodě. Na stránce <a href="/znacka/puma/">Puma</a> a <a href="/znacka/adidas/">Adidas</a> najdete podobné rozdělení, což se hodí při srovnání střihu.</p>'
          '<h2>Velikosti a střih</h2>'
          '<p>Nike sedí u obuvi spíš užším střihem, a proto širší nohy mohou potřebovat o půl čísla víc. Mezi řadami jsou ale velké rozdíly, takže se opírejte o délku vložky uvedenou v popisu. U oblečení sedí trička a mikiny sportovně, na tělo; pokud preferujete volný střih, volte o velikost větší. Dětské oblečení se označuje podle výšky, proto stačí změřit dítě a porovnat s tabulkou obchodu.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Boty po sportu vyvětrejte, vyndejte vložku a nechte schnout mimo topení.</li>'
          '<li>Bílé a světlé tenisky čistěte jemným kartáčem a mýdlem, ne agresivními přípravky.</li>'
          '<li>Funkční oblečení perte bez aviváže, která zhoršuje odvod vlhkosti.</li>'
          '<li>Mikiny a tepláky perte naruby, potisk a logo vydrží déle.</li>'
          '<li>Běžecké boty střídejte aspoň dva páry; mezipodešev se tak stihne obnovit.</li></ul>'
          '<h2>Jak se Nike liší od ostatních</h2>'
          '<p>V katalogu hraje Nike silně v kategoriích basketbal a běh, kde má širokou škálu určení. Značky <a href="/znacka/adidas/">Adidas</a> a <a href="/znacka/puma/">Puma</a> nabízejí podobný rozsah, Adidas se silnějším zastoupením fotbalového vybavení a turistické obuvi. <a href="/znacka/skechers/">Skechers</a> sází na měkkou a pohodlnou obuv. Správná volba záleží spíš na střihu nohy než na logu, proto zkoušejte nebo si projděte tabulky.</p>'
          '<h2>Slevy bez překvapení</h2>'
          '<p>Nejvýhodnější bývají předchozí kolekce a barvy, které už se do nových řad nezařazují. Sezónní zboží, jako pantofle a žabky, je nejlevnější na podzim, mikiny a bundy zjara. Při porovnání berte v úvahu také poštovné a podmínky vrácení. Pokud kupujete rychle rostoucí dítě, vyplatí se zboží s mírnou slevou a jistou velikostí víc než nejlevnější kus, který nesedí.</p>',
    faq=[
        ('Jaký sortiment Nike je na Sporteka nejobsáhlejší?', 'Největší část tvoří tenisky a volnočasová obuv, následují trailové boty, basketbal, kopačky a trička. Dále jsou zastoupené dresy, mikiny, fleecové mikiny a bundy. Skladba se mění podle skladů obchodů.'),
        ('Jak vybrat běžeckou botu Nike?', 'Rozhodněte se, kde poběžíte: silnice vyžaduje tlumení, les pevnější vzorek podešve. Zkoušejte odpoledne, počítejte s mírnou rezervou před prsty a vyberte botu, která drží patu. Podrobnosti najdete v popisu konkrétního modelu.'),
        ('Co znamenají zkratky FG, MG a AG u kopaček?', 'FG je určeno na pevný přírodní trávník, MG na smíšený povrch a AG na umělou trávu. Pokud hrajete na různých podkladech, hledejte víceúčelový model a ověřte, co uvádí výrobce.'),
        ('Sedí Nike větší, nebo menší?', 'U obuvi spíš užší, takže někomu pomůže půl čísla navíc. Spolehlivější než číslo je délka vložky v centimetrech. U dětí kupujte jen s malou rezervou.'),
        ('Jsou pantofle Victori One vhodné na delší chůzi?', 'Ne, jsou určeny na bazén, sprchy a po tréninku. Při dlouhé chůzi chybí fixace paty a chodidlo se unavuje. Na celodenní pohyb zvolte tenisky.'),
        ('Čím se liší tréninková obuv od tenisek?', 'Tréninková obuv má stabilnější a plošší podešev, lépe drží chodidlo při bočním pohybu a zvedání závaží. Tenisky jsou pohodlnější do města a na krátké vzdálenosti.'),
        ('Jak čistit světlé tenisky?', 'Kartáčem a vlažnou vodou s jemným mýdlem, bez pračky a bez sušení na topení. Tkaničky vyperte zvlášť a vložky nechte uschnout samostatně, aby bota nezapáchala.'),
        ('Kdy čekat na slevu?', 'Nejčastěji při změně sezóny a při obměně kolekce. Mikiny a bundy jsou levnější na jaře, letní obuv na podzim. Na Sporteka porovnejte obchody v konkrétní velikosti.'),
        ('Mohu na Sporteka přímo nakoupit?', 'Ne, Sporteka obchody pouze porovnává. Po kliknutí se dostanete k prodejci, u kterého dokončíte objednávku, platbu a případné vrácení zboží.'),
        ('Jak poznám, zda jde o pánský, dámský nebo dětský model?', 'Podle označení v názvu produktu a ve filtru Pro koho. Dámské modely bývají užší v oblasti paty, pánské širší. U dětských kousků kontrolujte tabulku velikostí obchodu, protože se řídí délkou chodidla nebo výškou.'),
    ],
)

# ------------------------------------------------------------------ skechers
NEW['skechers'] = dict(
    title='Skechers: pohodlná obuv pro ženy, muže a děti',
    desc='Skechers v katalogu Sporteky: vycházkové tenisky, zimní boty, sandály a tréninková obuv. Jak vybrat velikost, řadu a porovnat obchody.',
    intro='<p>Skechers je v katalogu Sporteky téměř výhradně obuvnická značka a drtivá většina nabídky patří do kategorie <a href="/tenisky/">tenisky a volnočasové boty</a>. Spíš než o výkon jde o každodenní pohodlí: měkké vycházkové modely, zimní boty, sandály, dětská obuv a pracovní kousky. '
          'Nejvíc zboží míří na ženy, těsně za nimi jsou muži a velký díl tvoří děti. Menší kategorie, jako <a href="/trailove-boty/">trailové boty</a>, <a href="/treninkova-obuv/">tréninková obuv</a> a <a href="/sandaly/">sandály</a>, doplňují sortiment pro aktivní využití. Průvodce vysvětluje, jak z názvů poznat účel boty, jak se rozhodnout mezi zimními a přechodnými modely, jak vybírat dětské boty a kdy sledovat slevy. Sporteka sama neprodává a pouze porovnává nabídky obchodů.</p>',
    guide='<h2>Jak je sortiment Skechers v katalogu složený</h2>'
          '<p>Pohled na kategorie ukazuje jasné těžiště. Skechers se prodává především jako značka pohodlných bot do města, do práce a na každodenní nošení. Sportovní části sortimentu jsou menší, ale zajímavé.</p>'
          + T(['Skupina', 'Kategorie', 'Co od ní čekat'], [
              ['Každodenní obuv', '<a href="/tenisky/">tenisky a volnočasové boty</a>', 'lehké, měkké modely na denní nošení'],
              ['Zima', '<a href="/zimni-obuv/">zimní boty a sněhule</a>', 'zateplené a vyšší boty do chladu'],
              ['Léto', '<a href="/sandaly/">sportovní sandály</a>', 'otevřené modely s popruhy na dovolenou a procházky'],
              ['Aktivní využití', '<a href="/treninkova-obuv/">tréninková obuv</a>, <a href="/trailove-boty/">trailové boty</a>, <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>', 'rekreační pohyb, chůze, lehčí běh'],
              ['Turistika', '<a href="/trekova-obuv/">trekové boty</a>', 'lehčí procházky a výlety'],
              ['Ostatní', 'kopačky, tenisová obuv', 'malé zastoupení, ověřte popis modelu']]) +
          '<p>V seznamu kategorií si všimnete i položek jako sáně nebo kajaky. U značky typu Skechers jde pravděpodobně o chybné či okrajové zařazení nabídky obchodů, proto se při hledání vždy řiďte popisem produktu, ne jen názvem kategorie. Pokud chcete skutečné sáně nebo vodní sporty, otevřete raději kategorie <a href="/sane-a-boby/">sáně a boby</a> a <a href="/kajaky-a-cluny/">kajaky a čluny</a> bez filtru značky.</p>'
          '<h2>Volnočasové tenisky: co ukazují názvy</h2>'
          '<p>V názvech se opakují jména jako Uno, Bobs, Flex Advantage, D’Lux Walker nebo Reggae Slim. Každé označuje jinou řadu a přesný popis najdete u konkrétního modelu v obchodě. V praxi se ale dají odvodit rozdíly: některé modely mají tvar městských bot do ulice, jiné se podobají lehčím vycházkovým botám pro delší chůzi. Všimněte si také slova slip-in v některých názvech, které obvykle naznačuje nazouvání bez ohýbání a bez zavazování; detail si u konkrétního kusu vždy ověřte.</p>'
          '<ul><li><strong>Měkkost podešve:</strong> pro celodenní chůzi po tvrdém povrchu je důležitější než vzhled.</li>'
          '<li><strong>Hmotnost:</strong> těžší boty unavují nohu při dlouhém dni, lehké se hodí na cestování.</li>'
          '<li><strong>Šířka:</strong> široká noha oceňuje měkký svršek, který se po pár dnech tvaruje.</li>'
          '<li><strong>Vložka:</strong> vyndávací vložku lze nahradit ortopedickou, pokud ji potřebujete.</li>'
          '<li><strong>Čištění:</strong> textilní svršek lze kartáčovat, hladká syntetika stačí otřít.</li></ul>'
          '<p>Pro rychlé srovnání s jinými značkami si otevřete kategorii <a href="/tenisky/">tenisky</a> a zúžení podle značek <a href="/znacka/adidas/">Adidas</a>, <a href="/znacka/nike/">Nike</a> a <a href="/znacka/puma/">Puma</a>. Zatímco tyto značky mají sportovnější charakter, Skechers cílí hlavně na komfort při chůzi a stání.</p>'
          '<h2>Zimní boty a sněhule</h2>'
          '<p>Zimní obuv je druhý největší tahák značky v praxi: ve vzorku zboží se objevují modely s označením zateplená obuv, voděodolné varianty a kousky s límcem. Vybírejte podle prostředí. Do města s mírnými mrazy stačí zateplená bota s dobrým vzorkem, do sněhu a rozmoklého terénu hledejte voděodolné provedení, vyšší svršek a podešev, která na ledu neklouže.</p>'
          '<ol><li>Zkoušejte boty s tlustší ponožkou, kterou budete v zimě nosit.</li>'
          '<li>Dbejte na prostor pro prsty: příliš těsná zimní bota chladne, protože zastavuje proudění krve.</li>'
          '<li>Ověřte, zda se na botě dá zapnout zip nebo šněrování bez vyzouvání, pokud ji budete často nazouvat.</li>'
          '<li>Po použití vyndejte vložku a boty sušte při pokojové teplotě.</li></ol>'
          '<p>Další modely jsou v kategorii <a href="/zimni-obuv/">zimní boty a sněhule</a>. Mají-li být boty i do hor, porovnejte je s tradičními outdoorovými značkami v kategorii <a href="/trekova-obuv/">trekové boty</a>, protože městská zimní obuv není určena na náročný terén.</p>'
          '<h2>Sandály a letní obuv</h2>'
          '<p>V létě se hodí sportovní sandály, které mají fixaci na paty a bocích. Rozdíl proti pantoflím je v bezpečnosti: sandál drží nohu při delší chůzi, pantofle spadnou. Dětské sandály vybírejte s pevnou špicí, protože děti často nohou kopou do překážek. Při dovolené u moře zvolte materiály, které snesou vodu, tedy ne klasickou kůži. Ve vzorku zboží najdete jak dámské, tak dívčí modely s barevnými popruhy, ať jde o dovolenou nebo školní prázdniny.</p>'
          '<p>Přehled je v kategorii <a href="/sandaly/">sportovní sandály</a>; pokud chcete turistický střih, zkuste hledat v kategoriích <a href="/trekova-obuv/">trekové boty</a> nebo <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<h2>Tréninková, trailová a běžecká obuv</h2>'
          '<p>Menší část nabídky míří na aktivní pohyb. Tréninková obuv je stabilnější a hodí se na skupinové lekce nebo lehčí posilování. Trailové boty mají hrubší vzorek podešve a pevnější špici pro nerovný terén. Silniční běžecká obuv je určena pro asfalt a mírný běh. Pokud plánujete pravidelný vytrvalostní běh, porovnejte nabídku s vyhrazenými běžeckými značkami, protože Skechers v katalogu cílí hlavně na rekreační využití.</p>'
          + T(['Aktivita', 'Vhodná kategorie', 'Na co si dát pozor'], [
              ['Chůze do práce', '<a href="/tenisky/">tenisky</a>', 'měkká podešev, dobrá fixace paty'],
              ['Lehký fitness trénink', '<a href="/treninkova-obuv/">tréninková obuv</a>', 'stabilita při bočním pohybu'],
              ['Výlet po stezce', '<a href="/trailove-boty/">trailové boty</a>', 'vzorek podešve, odolnost svršku'],
              ['Běh po silnici', '<a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>', 'tlumení a hmotnost'],
              ['Tenis', '<a href="/tenisova-obuv/">tenisová obuv</a>', 'boční opora a odolná podešev']]) +
          '<h2>Pro koho vybírat: dámské, pánské, dětské</h2>'
          '<p>Katalog je v tomto směru netypický: na rozdíl od jiných značek tvoří největší díl dámské modely, hned za nimi pánské, přičemž dětská obuv je podstatná část. Unisex kusy se prakticky nevyskytují, takže pokud hledáte botu pro oba, porovnejte stejné řady v dámské i pánské verzi.</p>'
          '<ul><li><strong>Ženy:</strong> převažují vycházkové tenisky, slip-on boty, zimní obuv a sandály.</li>'
          '<li><strong>Muži:</strong> nabídka zahrnuje sportovní tenisky, pracovní modely a boty do chladu.</li>'
          '<li><strong>Děti:</strong> dívčí obuv často s barevnými detaily, ale hledejte i neutrální kousky, které vydrží do dalšího roku.</li>'
          '<li><strong>Pracovní obuv:</strong> modely označené jako pracovní míří do prostředí se stáním a chůzí na tvrdém podkladu; ověřte, zda splňují bezpečnostní požadavky vašeho zaměstnavatele.</li></ul>'
          '<h2>Velikosti a střih</h2>'
          '<p>Obuv Skechers bývá voluminóznější než sportovní značky a méně těsná kolem nohy. Díky tomu je vhodná pro širší chodidlo a pro ty, kdo nechtějí pevné sevření. Naopak, pokud máte štíhlou nohu, může být bota v oblasti paty volnější, proto pomůže silnější ponožka nebo uvolnění tkaniček na míru. Zkoušejte odpoledne a vždy při výběru porovnejte délku vložky s vaším chodidlem v centimetrech.</p>'
          '<p>U dětí volte botu asi o palec delší než chodidlo a každé tři až čtyři měsíce velikost překontrolujte. Zvlášť pozorně sledujte zimní boty, kde se přidává ještě silnější ponožka.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Měkký svršek čistěte vlažnou vodou a jemným mýdlem, bez agresivní chemie.</li>'
          '<li>Boty nesušte na topení; guma se deformuje a lepení slábne.</li>'
          '<li>Vložky občas vyndejte a nechte uschnout, aby neprosakovaly pachem.</li>'
          '<li>Zimní boty impregnujte na začátku sezóny a po každém větším provlhnutí.</li>'
          '<li>Střídejte dva páry, pokud boty nosíte každý den; vydrží déle a noha si odpočine.</li></ul>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>U obuvi tohoto typu se výrazné rozdíly mezi obchody objevují hlavně u starších barev a řad, které výrobce nahrazuje novými. Zimní boty bývají výhodnější na jaře, sandály na konci léta. Při porovnání nabídek se vyplatí zkontrolovat i dostupnost přesné velikosti, protože slevy se často týkají jen několika čísel. Dalším trikem je porovnat dámskou, pánskou a juniorskou verzi stejné řady: menší dospělé velikosti jsou někdy k mání v dětské řadě.</p>'
          '<p>Mezi značkami vychází Skechers jako volba pro toho, kdo chodí hodně pěšky a chce měkkou obuv bez nutnosti ji dlouho rozšlapávat. Sportovně laděný kupující najde širší výběr u značek Adidas, Nike a Puma. Nakonec si udělejte krátký kontrolní seznam: určení, velikost podle vložky, materiál a zpětná cesta, pokud bota nesedí. Se Skechers se nejčastěji kupuje pohodlí, takže jakmile vás bota tlačí, nečekejte, že se rozchodí.</p>',
    faq=[
        ('Jaký sortiment Skechers v katalogu převažuje?', 'Naprostá většina patří do kategorie tenisek a volnočasových bot. Dále následují trailové boty, tréninková obuv, sandály a zimní obuv. Oblečení je zastoupeno minimálně, takže značka se u nás hledá hlavně pro boty.'),
        ('Je Skechers vhodný na běhání?', 'Katalog obsahuje silniční i trailové běžecké boty, ale většina nabídky je zaměřená na chůzi a každodenní nošení. Pro pravidelný vytrvalostní trénink porovnejte popis modelu a určení, případně se podívejte i na jiné značky.'),
        ('Co znamená označení slip-in v názvu boty?', 'Obvykle jde o model, který se nazouvá bez ohýbání a zavazování. Přesný způsob a konstrukci si ověřte v popisu konkrétního kusu, protože výrobce používá označení pro více řad.'),
        ('Jak vybrat zimní boty Skechers?', 'Podle prostředí: do města stačí zateplená bota s dobrým vzorkem, do sněhu hledejte voděodolné provedení a vyšší svršek. Zkoušejte s tlustší ponožkou a nechte prostor pro prsty.'),
        ('Jsou boty příliš široké na štíhlou nohu?', 'Mohou být, zejména v oblasti paty. Pomůže zapnout šněrování pevněji, silnější ponožka nebo užší model. Proto je dobré ověřit možnost vrácení u konkrétního obchodu.'),
        ('Jak velkou dětskou botu koupit?', 'Zhruba o palec delší než chodidlo, ne víc. Vložku změřte v centimetrech a kontrolujte ji každé tři až čtyři měsíce, protože děti rostou nerovnoměrně.'),
        ('Proč jsou mezi kategoriemi značky sáně nebo kajaky?', 'Jde pravděpodobně o okrajové či chybné zařazení nabídky obchodů. Při výběru se proto řiďte popisem produktu a ne jen názvem kategorie.'),
        ('Mohu boty prát v pračce?', 'Spíše ne. Pračka a sušení na topení zkracují životnost lepení a deformují materiál. Lepší je ruční čištění kartáčem a vlažnou vodou.'),
        ('Kdy zvolit sandály a kdy pantofle?', 'Sandály se hodí na delší chůzi, protože drží patu. Pantofle patří k vodě, na bazén a krátké cesty. Dětem kupujte raději sandály s pevnou špicí.'),
        ('Hodí se boty na celodenní stání nebo práci?', 'Mnoho modelů je zaměřeno na pohodlí při chůzi a stání, ale požadavky na pracovní obuv se liší. Ověřte, zda váš zaměstnavatel vyžaduje bezpečnostní prvky, a zkontrolujte popis modelu.'),
        ('Jak dlouho vydrží zimní boty?', 'Záleží na používání a péči. Impregnujte je na začátku sezóny, sušte při pokojové teplotě a střídejte dva páry, pokud je nosíte denně. Mokrá bota na topení se deformuje.'),
    ],
)

# ------------------------------------------------------------------ puma
NEW['puma'] = dict(
    title='Puma: tenisky, kopačky a oblečení k porovnání obchodů',
    desc='Puma v katalogu Sporteky: tenisky, kopačky King a Future, běžecké boty, mikiny a tepláky. Jak vybírat řadu, velikost a kdy čekat na slevu.',
    intro='<p>Puma tvoří v katalogu Sporteky samostatný a pestrý blok: od <a href="/tenisky/">tenisek a volnočasových bot</a> přes <a href="/kopacky/">kopačky</a> a běžecké boty až po sportovní textil. Podíl pánského, dámského a dětského zboží je vyrovnanější než u řady jiných značek, takže si vybere skoro každý člen rodiny. '
          'Na této stránce rozebíráme, jak se orientovat v názvech řad kopaček King a Future, čím se liší modely pro běh a jak vybírat <a href="/mikiny/">mikiny</a>, <a href="/teplaky/">tepláky</a> a trička Essentials. Dozvíte se také, jak pracovat s velikostmi, jak o věci pečovat a kdy se vyplatí čekat na slevu. Sporteka sama zboží neprodává, jen porovnává nabídky obchodů podle velikosti a dostupnosti.</p>',
    guide='<h2>Z čeho se nabídka Puma skládá</h2>'
          '<p>Obuv je v katalogu zastoupena většinou, ale u Pumy je podíl textilu a kopaček vyšší než u některých podobných značek. Přehled hlavních skupin ukazuje, kde se značka v nabídce opravdu pohybuje.</p>'
          + T(['Skupina', 'Kategorie', 'Poznámka'], [
              ['Městská obuv', '<a href="/tenisky/">tenisky a volnočasové boty</a>', 'nejpočetnější část, retro i moderní tvary'],
              ['Fotbal', '<a href="/kopacky-puma/">kopačky</a>, <a href="/dresy/">dresy</a>', 'řady King a Future, dětské i dospělé'],
              ['Běh', '<a href="/bezecke-boty-puma/">běžecké boty Puma</a>, <a href="/silnicni-bezecke-boty/">silnice</a>, <a href="/trailove-boty/">trail</a>', 'tréninkové i terénní modely'],
              ['Basketbal', '<a href="/basketbal/">basketbalová obuv</a>', 'menší, ale samostatná skupina'],
              ['Oblečení', '<a href="/sportovni-tricka/">trička</a>, <a href="/mikiny/">mikiny</a>, <a href="/teplaky-puma/">tepláky</a>, <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/sportovni-bundy-jaro-podzim/">bundy</a>', 'řada Essentials a tréninkové kousky']]) +
          '<p>V barevnosti vede černá, hned za ní bílá. Zbytek palety doplňují modrá, šedá a růžová. Jednobarevné černé nebo bílé kusy se nejsnáze kombinují a nejdéle vypadají aktuálně; výrazné barvy se obvykle prodávají v nižší sérii a rychleji mizí ze skladu.</p>'
          '<h2>Tenisky a retro modely</h2>'
          '<p>Nejpočetnější kategorie mixuje klasické nízké tenisky s novějšími modely. Ve vzorku zboží se objevují například Speedcat OG, Softride Enzo nebo tenisky s polstrovaným límcem. Rozdíl mezi retro a běžeckým stylem je v podešvi: retro boty mívají tenčí a pevnější, běžecké měkčí a prohnutou. Pokud je budete nosit celý den po městě, zvolte měkčí variantu, pokud je berete k outfitu na pár hodin, rozhoduje design.</p>'
          '<ul><li><strong>Nízký střih:</strong> univerzální pro džíny i sukně, nechrání kotník.</li>'
          '<li><strong>Polstrovaný límec:</strong> pohodlnější kolem kotníku, ale zahřívá v létě.</li>'
          '<li><strong>Semišový svršek:</strong> vypadá dobře, ale špatně snáší vodu; chraňte jej impregnací.</li>'
          '<li><strong>Dětské verze:</strong> často se suchým zipem, tkaničky vyžadují ruční zručnost.</li></ul>'
          '<h2>Kopačky Puma: King, Future a další</h2>'
          '<p>Kopačky tvoří druhou největší skupinu značky a názvy řad se opakují. Nejčastější jsou King a Future, doplněné koncovkami Play, Match nebo Pro. Přesná charakteristika každé řady je na produktové kartě výrobce, ale k výběru pomůže orientační logika: Play bývá nejjednodušší varianta pro tréninky a děti, Match střední úroveň, Pro míří na pokročilé hráče. Označení FG/AG ukazuje, že se model hodí na přírodní i umělou trávu s krátkými kolíky.</p>'
          '<ol><li>Rozhodněte se, na jakém povrchu budete hrát nejčastěji.</li>'
          '<li>Vyberte úroveň podle hry: pro trénink a děti stačí nižší řada, závodní hráči oceňují lehčí materiály.</li>'
          '<li>Zkontrolujte šířku: některé modely jsou užší, jiné se po rozehrání rozšíří.</li>'
          '<li>Ověřte, zda jde o dospělou nebo dětskou verzi; u dětí je často mělčí zakončení.</li></ol>'
          '<p>Kopačky lze porovnat přímo na stránce <a href="/kopacky-puma/">kopačky Puma</a>, obecný průvodce je v kategorii <a href="/kopacky/">kopačky</a>. Sálovou obuv, například modely Solarstrike, najdete v kategorii <a href="/salova-obuv/">sálová obuv</a>.</p>'
          '<h2>Běžecké boty</h2>'
          '<p>Na silnici i v terénu je dostupná řada modelů pro různé typy běžců. Název Electrify Nitro ve vzorku zboží napovídá, že jde o běžeckou obuv s jiným určením než městské tenisky. Při výběru se řiďte třemi otázkami: jak často běháte, jak dlouhé tratě a jaký povrch. Pro začátečníka je rozumnější bota s měkčím tlumením, zkušený běžec ocení lehčí a pružnější kousek.</p>'
          + T(['Typ běhu', 'Vhodná obuv', 'Poznámka'], [
              ['Krátké tratě na silnici', 'lehká běžecká bota', 'pružná podešev, nižší hmotnost'],
              ['Delší tréninky', 'bota s více tlumením', 'kontrolujte opotřebení mezipodešve'],
              ['Les a polní cesty', '<a href="/trailove-boty/">trailové boty</a>', 'hrubší vzorek, pevnější špice'],
              ['Rekreační běh', 'univerzální silniční model', 'zvolte pohodlí před rychlostí']]) +
          '<p>Přehled běžeckých modelů značky je na stránce <a href="/bezecke-boty-puma/">běžecké boty Puma</a>, kategorie jsou dostupné na stránkách <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> a <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<h2>Oblečení: Essentials, tréninkové kousky a bundy</h2>'
          '<p>V textilu převládají základní řady. Název Essentials se objevuje u triček, mikin, tepláků i bund a označuje jednodušší, každodenní kousky. Mezi tréninkovými položkami najdete tričko Velocity pro běh, dámské legíny nebo funkční dresy. Rozdíl poznáte po zátěži: bavlněné kousky jsou příjemné do města, funkční materiály lépe odvádějí pot při sportu.</p>'
          '<ul><li><strong>Mikiny:</strong> s kapucí nebo bez, hladký úplet je vhodný do tepla, česaný zevnitř do chladu.</li>'
          '<li><strong>Tepláky:</strong> manžety zužují nohavici, rovný střih je volnější; <a href="/teplaky-puma/">výběr tepláků Puma</a> usnadní porovnání.</li>'
          '<li><strong>Trička:</strong> volte podle aktivity: bavlna do města, funkční vlákno na trénink.</li>'
          '<li><strong>Bundy:</strong> prošívané a větrovky do přechodného počasí; porovnejte je v kategorii <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>.</li></ul>'
          '<h2>Basketbal, dresy a týmové oblečení</h2>'
          '<p>Basketbalová obuv je menší část nabídky, ale má jasné určení: vyšší opora, tlumení při doskoku a podešev na parketu nebo na venkovním hřišti. Vyberte podle povrchu, na kterém hrajete nejčastěji, a podle toho, zda se vám lépe hraje v nízkém, nebo ve vyšším střihu. Více rad je v kategorii <a href="/basketbal/">basketbal</a>.</p>'
          '<p>Dresy slouží týmům i fanouškům. Pro hru hledejte lehký prodyšný materiál, pro nošení do města stačí pohodlnější střih. Při objednávce pro celý tým porovnejte, zda obchod nabízí stejný model ve více velikostech a barvách; dohledat později chybějící velikost bývá obtížné. Stránka <a href="/dresy/">dresy</a> shromažďuje nabídku všech značek na jednom místě.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kopačky podle vzhledu: povrch a úroveň rozhodují víc než barva.</li>'
          '<li>Retro tenisky na celodenní chůzi: tenká podešev unavuje chodidlo.</li>'
          '<li>Běžecká bota jako každodenní: tlumení se opotřebuje dřív, než byste čekali.</li>'
          '<li>Velikost mikiny podle starého kusu: střihy se mění mezi řadami.</li>'
          '<li>Nákup jen podle slevy: boty, které tlačí, se nerozchodí.</li></ul>'
          '<h2>Pro koho vybírat</h2>'
          '<p>Nabídka je rozdělena zhruba mezi muže, ženy a děti, s převahou pánského zboží. Dětské modely tvoří významnou část díky kopačkám a tenisek. Unisex zboží je spíše vzácné, ale u triček a čepic na něj narazíte. Při výběru pro děti se řiďte výškou i délkou chodidla, protože značková označení bývají odlišná od českých velikostí.</p>'
          '<p>Chcete-li srovnat střih s jinými značkami, projděte si stránky <a href="/znacka/adidas/">Adidas</a>, <a href="/znacka/nike/">Nike</a> a <a href="/znacka/skechers/">Skechers</a>. Puma si vybere ten, kdo chce střední cestu mezi sportovním a módním vzhledem.</p>'
          '<h2>Velikosti, střih a péče</h2>'
          '<p>Obuv Puma sedí obvykle podle čísla, ale u kopaček nebo úzkých nízkých tenisek dává smysl vyzkoušet o půl čísla víc. Základem je délka vložky v centimetrech. U oblečení sedí trička sportovně, mikiny spíše volněji. Zimní kousky zkoušejte s vrstvou pod nimi.</p>'
          '<ul><li>Kopačky po zápase očistěte kartáčem a nechte vyschnout bez topení.</li>'
          '<li>Semišové tenisky impregnujte a čistěte suchým kartáčkem.</li>'
          '<li>Funkční textil perte bez aviváže, aby neztratil schopnost odvádět vlhkost.</li>'
          '<li>Potištěné kousky perte naruby a nesušte v horkém sušiči.</li>'
          '<li>Běžecké boty používejte jen na běh; v nich chodit celý den zkracuje životnost tlumení.</li></ul>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Nejlepší příležitosti přicházejí při výměně kolekcí a na konci sezóny. Kopačky předchozích řad jsou pro většinu hráčů dostatečné a bývají výhodnější. Mikiny a bundy zlevní na jaře, letní tričko a kraťasy na podzim. Při porovnání obchodů si všímejte rozdílu v dopravě a v možnosti vrácení, protože u obuvi se velikost často mění. Pokud sbíráte více kusů najednou, může se vyplatit koupit je u jednoho prodejce.</p>',
    faq=[
        ('Co v katalogu značky Puma převažuje?', 'Největší skupinou jsou tenisky a volnočasové boty, následují kopačky, trička, trailové boty, mikiny a kraťasy. Menší skupiny tvoří basketbal, silniční běžecké boty, tepláky a bundy.'),
        ('Čím se liší kopačky King a Future?', 'Jde o dvě různé řady s různým střihem i určením. Přesné parametry uvádí výrobce na kartě konkrétního modelu. Při výběru sledujte hlavně povrch, úroveň označenou koncovkou a velikost.'),
        ('Co znamená FG/AG u kopaček?', 'Označuje, že model je určen pro pevný přírodní trávník a umělou trávu s kratšími kolíky. Pro halu nebo tvrdý umělý povrch hledejte sálovou obuv nebo model pro umělý trávník.'),
        ('Je Puma vhodná pro děti?', 'Ano, dětské zboží tvoří silnou část sortimentu, od kopaček přes tenisky po trička a mikiny. U bot kupujte jen s malou rezervou a kontrolujte velikost každé tři až čtyři měsíce.'),
        ('Jak vybrat běžeckou botu Puma?', 'Podle povrchu, délky tratí a frekvence. Pro silnici zvolte lehčí model s tlumením, do lesa trailovou botu. Zkoušejte odpoledne a ponechte před prsty malou rezervu.'),
        ('Jak čistit semišové tenisky?', 'Suchým kartáčkem po směru vlákna, případně gumou na semiš. Nenamáčejte je a před nošením v dešti použijte impregnaci. Pračka semiš poškodí.'),
        ('Sedí mikiny Essentials volně?', 'Obvykle spíše volněji a pohodlně na doma i do města. Pokud preferujete přiléhavý střih, zvolte o velikost menší a ověřte tabulku obchodu.'),
        ('Kdy je dobrý čas na nákup?', 'Při změně sezóny a při obměně kolekce. Zimní kousky zlevní na jaře, letní na podzim. Na Sporteka stačí porovnat obchody ve vaší velikosti a podle podmínek dopravy.'),
        ('Prodáváte zboží přímo?', 'Ne, Sporteka je srovnávač. Po kliknutí se dostanete k prodejci, u něhož dokončíte objednávku a vyřídíte případné vrácení zboží.'),
        ('Jak dlouho vydrží běžecké boty?', 'Životnost záleží na váze, povrchu a frekvenci tréninku. Jakmile mezipodešev ztratí pružnost nebo podešev vyhladí, boty vyměňte. Střídání dvou párů jim prodlouží život a noze uleví.'),
        ('Jak vybrat velikost mikiny nebo trička?', 'Změřte hrudník a porovnejte jej s tabulkou obchodu. Sportovní trička sedí těsněji, mikiny volněji. Pokud váháte mezi dvěma velikostmi, zvolte větší, pokud chcete volný střih, nebo menší pro přiléhavý.'),
        ('Hodí se kopačky Puma i na umělou trávu?', 'Modely označené FG/AG ano, pokud je kolíky nejsou příliš dlouhé. Pro hustý umělý povrch hledejte obuv určenou přímo na umělý trávník a ověřte popis výrobce.'),
    ],
)
