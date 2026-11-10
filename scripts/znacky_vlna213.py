"""sporteka.cz — brand page texts wave 213: salomon, smartwool, daiwa, mikado.
Only facts derivable from the catalogue and general knowledge; no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ salomon
NEW['salomon'] = dict(
    title='Salomon: boty do terénu, na běh a na lyže',
    desc='Salomon v katalogu: tenisky, trailové a silniční běžecké boty, trekové boty i lyžařská výbava. Jak vybrat řadu, velikost a kdy čekat slevu.',
    intro='<p>Salomon je v našem katalogu především obuvnická značka. Největší část nabídky tvoří tenisky a volnočasové boty, hned za nimi trailové běžecké boty, silniční běžecké modely a nízká i vysoká treková obuv. Menší, ale stálou část tvoří zimní sortiment: lyžařské boty, helmy, brýle, běžky a sjezdové lyže. '
          'Zákazníci jsou převážně muži, výrazně zastoupené jsou i ženy a nechybí dětské a unisex modely. Převažují černé a šedé barvy, doplněné modrou, hnědou a zelenou. Průvodce níže vysvětluje, jak se orientovat v řadách podle názvu modelu, čím se liší trailová bota od silniční, kdy sáhnout po membráně a jak vybrat velikost. Najdete tu i tipy na péči a na sledování slev. Rychlý vstup nabízejí <a href="/znacka/salomon/">souhrn značky</a>, <a href="/trailove-boty/">trailové boty</a> a <a href="/trekova-obuv/">trekové boty</a>.</p>',
    guide='<h2>Co Salomon v katalogu nabízí</h2>'
          '<p>Při pohledu na kategorie je vidět, že značka se v obchodech prodává hlavně jako obuv do přírody a pro pohyb ve městě i mimo něj. Pořadí kategorií pomáhá pochopit, co tu lze čekat v největší šíři.</p>'
          + T(['Kategorie', 'Jak ji číst'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'nejširší výběr; často terénní střih nošený na každý den'],
              ['<a href="/trailove-boty/">Trailové běžecké boty</a>', 'druhá největší skupina, pro lesní a horské běhání'],
              ['<a href="/silnicni-bezecke-boty/">Silniční běžecké boty</a>', 'tlumené boty na asfalt, chodník a běžecký pás'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'nízká turistická obuv na jednodenní výlety'],
              ['<a href="/vysoke-trekove-boty/">Vysoké trekové boty</a>', 'kotníková obuv pro nerovný terén a těžší batoh'],
              ['<a href="/lyzarske-boty/">Lyžařské boty</a>', 'sjezdová obuv, kategorie spíš pro cílené hledání'],
              ['<a href="/lyzarske-helmy/">Lyžařské helmy</a> a <a href="/lyzarske-bryle/">brýle</a>', 'zimní doplňky, které se dobře kombinují s botami'],
              ['<a href="/bezecke-lyzovani/">Běžecké lyžování</a>', 'boty a vybavení na stopu'],
              ['<a href="/outdoor-doplnky/">Outdoorové doplňky</a>', 'běžecké batohy, pásy a drobnosti do terénu']]) +
          '<p>Pokud hledáte konkrétní typ boty, nejrychlejší je jít přes kategorii a teprve poté ji zúžit na značku. Landingy <a href="/salomon-trekove-boty/">Salomon trekové boty</a>, <a href="/salomon-bezecke-boty/">Salomon běžecké boty</a> a <a href="/salomon-lyzarske-boty/">Salomon lyžařské boty</a> už mají výběr připravený.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Katalog obsahuje dlouhé názvy z různých e-shopů, ale několik pravidelností se opakuje. Název modelu obvykle tvoří jméno řady, například X Ultra, XA Pro 3D, Speedcross nebo Aero Glide, a za ním číslo generace či písmenné doplňky. Písmeno W na konci označuje dámskou verzi, J juniorskou. Zkratka GTX ve jménu znamená, že bota má membránu Gore-Tex, tedy ochranu proti vodě. Slovo MID signalizuje vyšší střih nad kotník.</p>'
          '<ul><li><strong>Generace:</strong> číslo ve jménu, třeba V9, ukazuje novější nebo starší verzi stejné řady. Starší generace jsou častým cílem slev.</li>'
          '<li><strong>Dámský a pánský střih:</strong> dámské verze mají užší patu a pro nohu přizpůsobený tvar, ne jen jinou barvu.</li>'
          '<li><strong>Membrána:</strong> modely s GTX se hodí do deště a na podzim, bez ní boty lépe větrají.</li>'
          '<li><strong>Typ použití:</strong> většina obchodů píše do názvu slova jako trailová, turistická nebo běžecká obuv, podle nich filtrujte.</li></ul>'
          '<h2>Trailové boty versus silniční běžecké boty</h2>'
          '<p>Obě skupiny jsou v nabídce silně zastoupené a lidé je zaměňují. Silniční bota je stavěná na pravidelný povrch, takže se soustředí na tlumení a lehkost. Trailová má agresivnější vzorek podešve, pevnější svršek a často ochrannou špičku. Na rozbahněné cestě je proto silniční bota nebezpečně kluzká a na asfaltu zase hrubý vzorek rychleji ubývá.</p>'
          + T(['Vlastnost', 'Trailová bota', 'Silniční bota'], [
              ['Podešev', 'hrubý vzorek s výraznými kolíky', 'hladší, souvislý kontakt s povrchem'],
              ['Svršek', 'odolnější, často s ochranou špičky', 'lehká síťovina s prodyšností'],
              ['Tlumení', 'střední, důležitější je stabilita', 'výraznější, pro dlouhé kilometry na tvrdém'],
              ['Vhodné pro', 'lesní cesty, kameny, blátivé stezky', 'chodník, silnice, pás'],
              ['Orientační nevýhoda', 'na asfaltu se rychleji opotřebí', 'na mokrých kamenech klouže']]) +
          '<p>Chodíte-li na výlety i do práce, můžete zvolit univerzálnější terénní tenisku. Běháte-li ale pravidelně v lese, bude rozdíl znát. Širší pohled na značky v oboru poskytnou stránky <a href="/znacka/hoka/">Hoka</a>, <a href="/znacka/la-sportiva/">La Sportiva</a>, <a href="/znacka/brooks/">Brooks</a> a <a href="/znacka/asics/">Asics</a>. Salomon se od nich v nabídce odlišuje hlavně tím, že stejné jméno najdete jak na běžecké botě, tak na turistické obuvi a lyžařském vybavení, takže jeden výrobce pokryje několik ročních období.</p>'
          '<h2>Treková obuv: nízká nebo vysoká</h2>'
          '<p>Nízká treková bota je lehčí a pohodlnější na zpevněných cestách, vysoká víc podrží kotník a chrání proti kamenům a vlhkosti. Pro jednodenní výlety s malým batohem většině lidí stačí nízký střih. Vysokou botu zvažte, pokud nesete těžší zátěž, chodíte po sutích nebo máte slabší kotníky. Podrobnosti najdete v kategoriích <a href="/trekova-obuv/">trekové boty</a> a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>.</p>'
          '<ul><li><strong>Prodyšnost versus voděodolnost:</strong> membrána chrání před vodou, ale v létě zahřívá. Na horké dny je lepší verze bez ní.</li>'
          '<li><strong>Podrážka:</strong> měkčí guma lépe drží na mokrých skalách, tvrdší déle vydrží na štěrku.</li>'
          '<li><strong>Zavazování:</strong> rychlé systémy šetří čas, klasické tkaničky se snáze opravují.</li>'
          '<li><strong>Zimní varianty:</strong> sněhule a zimní boty najdete v kategorii <a href="/zimni-obuv/">zimní boty a sněhule</a>.</li></ul>'
          '<h2>Velikosti a sedavost</h2>'
          '<p>Salomon je obecně považován za značku s užším a přiléhavým střihem, zejména v oblasti paty a středu nohy. Lidem se širokou nohou může vadit přední část. Dobré je počítat s tím, že běžecká bota má mít před palcem asi šířku palce rezervy, protože noha při běhu nateče a při sestupu klouže dopředu. Turistická obuv se vybírá s ponožkou, kterou na výlet nosíte, a nejlépe odpoledne, kdy je noha větší.</p>'
          '<p>Při nákupu přes internet hledejte délku vložky v centimetrech. Porovnejte ji s vlastním chodidlem změřeným na papíře a přidejte rezervu. Čísla se mohou lišit podle toho, zda obchod uvádí velikost evropskou, britskou nebo americkou, a stejně tak u dámských a pánských modelů. Chystáte-li se bot užívat v zimě, přidejte rezervu na silnější ponožku. Obecný návod k velikostem pomůže ve stránce <a href="/tenisky/">tenisky</a>.</p>'
          '<h2>Muži, ženy, děti</h2>'
          '<p>Podle poměru v katalogu jsou nejvíc zastoupeny pánské modely, s odstupem následují dámské a menší skupinu tvoří dětské a unisex. Pro ženy je proto užitečné použít filtr pohlaví, jinak se výsledky plní pánskými velikostmi. Dětské boty jsou obvykle outdoorové nebo běžecké v juniorské velikostní řadě, například modely značené J. Děti vyrůstají rychle, takže při koupi dejte pozor na rezervu a raději volte starší generaci za nižší cenu.</p>'
          '<h2>Péče a životnost</h2>'
          '<ol><li>Po mokrém výletu vyndejte vložky a boty sušte při pokojové teplotě, ne u topení.</li>'
          '<li>Bláto smývejte vlažnou vodou a měkkým kartáčem, bez agresivních čisticích přípravků.</li>'
          '<li>Boty s membránou občas ošetřete impregnací určenou pro daný materiál, aby voda stékala po povrchu.</li>'
          '<li>Rotujte dva páry, pokud běháte často: střední vrstva podešve potřebuje čas na regeneraci.</li>'
          '<li>Sledujte opotřebení vzorku a boků: když se pěna propadá nebo guma hladí, je čas na výměnu.</li></ol>'
          '<p>Lyžařské boty skladujte uvolněné přezky a v suchu, aby se skořepina nedeformovala. Před sezonou zkontrolujte vložku a přezky. Návod k nákupu lyžařské výbavy je v kategoriích <a href="/lyzarske-boty/">lyžařské boty</a> a <a href="/sjezdove-lyze/">sjezdové lyže</a>.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Nejvýraznější slevy přicházejí, když obchody uvolňují místo pro novou generaci modelu. U běžeckých a trailových bot k tomu dochází po vydání nové verze, u zimní výbavy na konci sezony. Pro nejlepší výsledek porovnejte stejný model napříč obchody, protože skladové zásoby velikostí se liší. Sledujte rozdíl mezi cenou jednotlivých velikostí: nejběžnější čísla bývají vyprodaná dříve, okrajové velikosti zůstávají levnější. Pokud znáte svůj správný model, porovnávač vám ušetří čas při hledání nejnižší nabídky v jednom okamžiku.</p>'
          '<p>Při srovnání dávejte pozor na to, zda jde o stejnou generaci a stejnou barvu. Název s číslem V9 a V8 se může lišit v cenách i v použitých materiálech. Další modely do běžných cest najdete v kategorii <a href="/outdoor-doplnky/">outdoorové doplňky</a> a mezi <a href="/bezecke-lyzovani/">vybavením na běžky</a>.</p>',
    faq=[
        ('Co v katalogu od značky Salomon převažuje?',
         'Největší část tvoří tenisky a volnočasové boty, následují trailové a silniční běžecké boty a treková obuv. K tomu se přidává zimní sortiment a menší skupina outdoorových doplňků.'),
        ('Jak poznám dámskou a juniorskou verzi modelu?',
         'V názvu hledejte písmeno W za jménem řady, které označuje dámský střih, nebo písmeno J pro juniorskou verzi. Obchody také píšou slova dámská, pánská a dětská přímo do titulku.'),
        ('Znamená zkratka GTX opravdu nepromokavou botu?',
         'GTX označuje membránu Gore-Tex, která brání vniknutí vody, a zároveň umožňuje částečný odvod vlhkosti. Pro léto a rychlý běh bývá lepší verze bez membrány, protože lépe větrá.'),
        ('Jaký je rozdíl mezi trailovou a silniční běžeckou botou?',
         'Trailová bota má hrubší vzorek podešve a odolnější svršek pro nerovný terén. Silniční je lehčí, více tlumená a určená na pevný povrch. Na kluzkých stezkách je silniční model riskantní.'),
        ('Hodí se trailová bota i na každodenní nošení?',
         'Ano, mnoho lidí nosí terénní tenisky do města i na výlety. Počítejte ale s tím, že hrubý vzorek na asfaltu rychleji ubývá a podešev může být hlučnější na kachlích.'),
        ('Sedí Salomon spíš úzce, nebo široce?',
         'Podle obecných zkušeností bývá střih spíš přiléhavý v patě a středu nohy. Lidé se širokou nohou si mají zkontrolovat popis modelu a v případě pochybností zvolit větší velikost nebo širší řadu.'),
        ('Mám zvolit vysokou, nebo nízkou trekovou obuv?',
         'Pro jednodenní výlety na zpevněných cestách většinou stačí nízká bota. Vysokou zvolte při těžší zátěži, v suti nebo při slabších kotnících, protože kotník lépe podrží.'),
        ('Kdy bývají zimní produkty od Salomonu levnější?',
         'Typicky v závěru sezony, kdy obchody uvolňují sklad pro novou kolekci. Sledujte lyžařské boty, helmy a brýle od konce zimy a porovnávejte shodný model napříč obchody.'),
        ('Jak dlouho vydrží běžecké boty?',
         'Délka života závisí na váze běžce, povrchu a četnosti běhání. Když se pěna ve střední vrstvě propadá, vzorek je hladký nebo boty tlačí jinak než dřív, je čas na výměnu.'),
        ('Mohu porovnat stejný model v různých obchodech?',
         'Ano, stačí otevřít produkt a porovnat nabídky. Hlídejte shodnou generaci, barvu a velikost, aby bylo srovnání poctivé, a ověřte, že je vaše číslo skladem.'),
    ])

# ------------------------------------------------------------------ smartwool
NEW['smartwool'] = dict(
    title='Smartwool: merino ponožky, trička a spodní prádlo',
    desc='Smartwool v katalogu: merino ponožky, trička, spodní prádlo a doplňky pro hory i každý den. Jak vybrat tlumení, délku a pečovat o merino.',
    intro='<p>Smartwool je v katalogu značka merino vlny. Nejpočetnější jsou merino ponožky, hned za nimi merino trička a tílka, sportovní ponožky, merino spodní prádlo a legíny, mikiny a svetry a menší skupina čepic, nákrčníků a rukavic. '
          'Zastoupení pohlaví je vyrovnané: pánské a dámské modely jsou téměř stejně početné, výrazná je i dětská řada. Barevně vede černá, následují modrá a šedá. '
          'V průvodci vysvětlujeme, jak číst označení tlumení v názvech ponožek, čím se liší model na výlet, běh a lyže, kdy vybrat merino místo syntetiky a jak prát, aby vydrželo. Vstup do nabídky otevřete přes kategorie <a href="/merino-ponozky/">merino ponožky</a>, <a href="/merino-tricka/">merino trička</a> a <a href="/merino-pradlo/">merino spodní prádlo</a>. Rychlé výběry jsou i na stránce <a href="/merino-ponozky-panske/">pánské merino ponožky</a>.</p>',
    guide='<h2>Co Smartwool v katalogu nabízí</h2>'
          '<p>Jméno značky vychází z merino vlny a nabídka tomu odpovídá. Převahu mají ponožky, ale pokrývá se tu i oblečení na tělo. Přehled kategorií ukazuje, kde se vyplatí začít.</p>'
          + T(['Kategorie', 'Pro koho a na co'], [
              ['<a href="/merino-ponozky/">Merino ponožky</a>', 'největší skupina; turistika, běh, každodenní nošení'],
              ['<a href="/merino-tricka/">Merino trička a tílka</a>', 'první vrstva pro pohyb a cestování'],
              ['<a href="/sportovni-ponozky/">Sportovní ponožky</a>', 'ponožky určené na konkrétní aktivitu'],
              ['<a href="/merino-pradlo/">Merino spodní prádlo a legíny</a>', 'teplá základní vrstva pod kalhoty a bundu'],
              ['<a href="/merino-mikiny/">Merino mikiny a svetry</a>', 'střední vrstva do chladna'],
              ['<a href="/merino-doplnky/">Čepice, nákrčníky, rukavice</a>', 'doplňky pro studené dny'],
              ['<a href="/lyzarske-ponozky/">Lyžařské ponožky</a>', 'dlouhé ponožky pod lyžák i snowboardovou botu']]) +
          '<p>Přibývají i produkty mimo čistě merino kategorie, například <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a> a <a href="/sportovni-podprsenky/">podprsenky</a>. V takových případech se vždy podívejte do popisu materiálu.</p>'
          '<h2>Jak číst označení ponožek</h2>'
          '<p>V názvech ponožek se opakují anglická slova, která určují použití i tloušťku. Pomůže, když je znáte, protože e-shopy popisují produkt často jen názvem.</p>'
          + T(['Označení v názvu', 'Co znamená', 'Kdy zvolit'], [
              ['Hike', 'ponožky na turistiku', 'výlety v botách, delší chůze'],
              ['Run', 'běžecké ponožky', 'trénink, kde záleží na střihu a švech'],
              ['Ski, Snowboard', 'zimní ponožky ke sportu', 'dlouhé nad lýtko, tlumení na holeni'],
              ['Everyday', 'každodenní řada, často s potiskem', 'práce, město, volný čas'],
              ['Zero Cushion', 'bez vycpávky', 'těsné boty, lyžařské boty, tenká vrstva'],
              ['Light Cushion', 'lehké tlumení', 'běžné výlety a běh, teplejší počasí'],
              ['Full Cushion', 'plné tlumení', 'chlad, dlouhé túry, citlivá chodidla'],
              ['Targeted Cushion', 'tlumení jen v určených místech', 'kompromis mezi tlumením a pocitem v botě']]) +
          '<p>Délka je druhý údaj: Crew sahá do poloviny lýtka, Mini Crew a Low jsou nižší, OTC znamená přes lýtko. Kompresní ponožky se vyskytují i v nabídce a mají zřetelně těsnější střih, který podporuje chodidlo a lýtko. Dětské modely nesou slovo Kids v názvu.</p>'
          '<h2>Proč merino a kdy raději ne</h2>'
          '<p>Merino vlna je jemné přírodní vlákno, které dobře reguluje teplotu, zahřeje i v mírně vlhkém stavu a pomaleji se v něm tvoří nepříjemný pach. Proto se hodí na vícedenní výlety, na cesty s malým zavazadlem i na každodenní nošení. Nevýhodou je menší odolnost proti otěru než u čistě syntetických materiálů a vyšší nároky na praní. Proto výrobci obvykle přidávají nylon nebo elastan, což zlepšuje tvar a životnost.</p>'
          '<ul><li><strong>Výhody merina:</strong> příjemný dotek, tepelný komfort v chladu i v teple, pomalejší zápach.</li>'
          '<li><strong>Nevýhody:</strong> vlna se prodírá v patách a na špičkách rychleji než syntetika, a schne pomaleji než nylon.</li>'
          '<li><strong>Kdy zvolit syntetiku:</strong> při intenzivním potu v horku, pro opakované praní a pro velmi levné doplňky.</li>'
          '<li><strong>Směs vláken:</strong> kontrolujte složení v popisu; podíl merina a syntetiky určuje, jak se ponožky budou chovat.</li></ul>'
          '<h2>Ponožky podle aktivity</h2>'
          '<p>Na turistiku se obvykle volí ponožky s lehkým nebo středním tlumením, které tlumí nárazy v těžké botě a neruší prsty. Pro běh se hledá kratší střih, přiléhavé klenutí a minimum švů, protože tření přes ponožku končí puchýřem. Na lyže stačí tenká vrstva v lyžařské botě, protože silná ponožka zhoršuje přenos pohybu a může vytvářet tlakové body. Pro každodenní nošení jsou vhodné barevné vzory a nižší střih. Rozdíl mezi nimi je znát hlavně po osmi hodinách chůze.</p>'
          '<p>K ponožkám se hodí vhodné boty. Více v kategoriích <a href="/trekova-obuv/">trekové boty</a>, <a href="/trailove-boty/">trailové boty</a> a <a href="/lyzarske-boty/">lyžařské boty</a>. Vlastní výběry máte také v <a href="/merino-ponozky-damske/">dámských</a> a <a href="/detske-merino-ponozky/">dětských</a> merino ponožkách.</p>'
          '<h2>Merino trička a spodní prádlo</h2>'
          '<p>Merino tričko slouží jako první vrstva: leží přímo na kůži, odvádí vlhkost a chrání před prochladnutím. Na běh s vysokou intenzitou je lepší lehčí gramáž, v zimě naopak hustší pletení nebo dlouhý rukáv. Legíny a spodní prádlo nosíte pod kalhoty, na lyže nebo samostatně pro chladnější běh. Pokud vás zajímají alternativy, srovnejte značky <a href="/znacka/icebreaker/">Icebreaker</a>, <a href="/znacka/devold/">Devold</a> a <a href="/znacka/ortovox/">Ortovox</a>. Smartwool se v nabídce odlišuje tím, že spojuje ponožky a oblečení pod jedním jménem, takže snadno sladíte celý outfit.</p>'
          '<p>Pro střední vrstvu si prohlédněte <a href="/merino-mikiny/">merino mikiny a svetry</a>. Při vrstvení zvolte volnější střih, aby vrstvy držely vzduch mezi sebou, a vlnu nosili pod bundou, která chrání před větrem a deštěm.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Ponožky se prodávají v rozsahu velikostí S, M, L a XL, nikoli po jednom čísle. Rozsah proto vždy zkontrolujte u konkrétního produktu. Při pochybnostech vyberte větší velikost, protože těsná vlna se přirozeně vytahuje, zatímco příliš velké ponožky se krčí v botě. Dětské ponožky se vybírají podle věku nebo čísla bot a mají rezervu na růst. Trička a spodní prádlo sedí obvykle přiléhavě, takže je u nich lepší zvolit svou běžnou velikost, než přidávat.</p>'
          '<h2>Péče o merino</h2>'
          '<ol><li>Perte ve vlažné vodě na šetrný program, nejlépe obrácené na lícovou stranu.</li>'
          '<li>Používejte jemný prací prostředek bez aviváže, která zhoršuje odvod vlhkosti.</li>'
          '<li>Nesušte v bubnu při vysoké teplotě; vlna se může srazit.</li>'
          '<li>Sušte rozložené vodorovně, ne zavěšené za ramínka, aby se materiál nevytahoval.</li>'
          '<li>Vlnu větrejte mezi nošením, často stačí vyvětrat místo praní.</li></ol>'
          '<h2>Kdy se vyplatí sledovat slevy</h2>'
          '<p>Vzorované a sezonní ponožky se po skončení kolekce často prodávají levněji, zejména v barvách, které už se nevyrábějí. Základní jednobarevné kousky bývají stabilnější. Při srovnání ověřte, zda nabídka sedí na stejný střih, délku, tlumení a velikost. Do výběru lze zahrnout i balíčky dvou nebo tří párů. Slevy mají smysl především na kousky, které opravdu vyměníte, ne na barvy jen proto, že jsou zlevněné.</p>',
    faq=[
        ('Co znamená Full Cushion nebo Light Cushion v názvu ponožek?',
         'Jde o míru vycpávky. Zero je bez tlumení, Light má tenčí vrstvu, Full tlumí na celém chodidle a Targeted má vycpávky jen v určených místech. Tloušťku volte podle počasí a těsnosti obuvi.'),
        ('Jak poznám, že jde o dámskou nebo dětskou verzi?',
         'V názvu hledejte slova Women’s nebo dámské a Kids nebo dětské. Střih bývá užší a velikostní rozsah odpovídá menším chodidlům.'),
        ('Jsou merino ponožky vhodné i do léta?',
         'Ano, lehčí tlumení a tenčí vlákno dobře odvádí vlhkost a snižuje pocit horka. Merino reguluje teplotu v obou směrech, takže se v lehké variantě nosí i za tepla.'),
        ('Proč merino méně zapáchá?',
         'Vlněné vlákno pomaleji drží pach než většina syntetických materiálů. Proto se hodí na vícedenní výlety, ale po delším nošení stejně potřebuje vyprat.'),
        ('Mohu merino prádlo prát v pračce?',
         'Většinu kousků ano, ale na šetrný program ve vlažné vodě a bez aviváže. Sušte rozložené a mimo přímé teplo, aby se vlna nesrazila.'),
        ('Jakou velikost ponožek zvolit, když jsem na hranici?',
         'Zvolte spíš větší. Příliš malé ponožky se přetahují a rychleji se prodřou, příliš velké se krčí v botě a vytvářejí tlakové body.'),
        ('Jak dlouho merino ponožky vydrží?',
         'Záleží na intenzitě nošení, obuvi a složení materiálu. Slabší místa jsou paty a špičky. Když se vlákno ztenčí, ponožky už nechrání a patří do výměny.'),
        ('Hodí se Smartwool i na lyže a snowboard?',
         'V nabídce jsou řady pro lyžování i snowboard, které bývají dlouhé a s tlumením v oblasti holeně. Pod lyžařskou botou obvykle stačí tenká vrstva, protože silná zhoršuje přenos pohybu.'),
        ('Kde hledat sladěné merino oblečení?',
         'Prohlédněte si trička, spodní prádlo a mikiny v kategoriích merino a zúžte je na značku. Tak sladíte ponožky, základní vrstvu i doplňky na chladné dny.'),
    ])

# ------------------------------------------------------------------ daiwa
NEW['daiwa'] = dict(
    title='Daiwa: navijáky, pruty a vlasce pro rybáře',
    desc='Daiwa v katalogu: navijáky, rybářské pruty, vlasce a šňůry i doplňky. Jak vybrat velikost navijáku, multiplikátor, délku prutu a kdy čekat slevu.',
    intro='<p>Daiwa je v našem katalogu především rybářská značka. Největší kategorií jsou navijáky, těsně za nimi rybářské pruty a s odstupem vlasce a šňůry, rybářské doplňky, tašky a pouzdra a nástrahy. Zbytek tvoří okrajové položky z jiných sportů, například mikiny, tašky a trenažéry. '
          'Značka tu nemá dělení podle pohlaví, protože jde o vybavení, ne oblečení. V názvech se opakují řady typu Caldia, Legalis, Freams, Prorex, Tatula nebo Ninja a písmenné značky velikostí a převodu. '
          'Průvodce vysvětluje, jak se v těchto označeních vyznat, jak vybrat velikost navijáku podle prutu a návnady, čím se liší klasický naviják od multiplikátoru a jak spárovat prut, naviják a vlasec. Hned na začátek můžete otevřít kategorie <a href="/rybarske-navijaky/">navijáky</a> a <a href="/rybarske-pruty/">rybářské pruty</a> nebo výběr <a href="/navijaky-daiwa/">navijáky Daiwa</a>.</p>',
    guide='<h2>Co Daiwa v katalogu nabízí</h2>'
          '<p>Z kategorií je vidět, že se značka prodává jako výrobce rybářského náčiní. Naviják a prut jsou jádro nabídky, vlasec a doplňky tvoří logické doplnění.</p>'
          + T(['Kategorie', 'K čemu slouží'], [
              ['<a href="/rybarske-navijaky/">Navijáky</a>', 'největší skupina; klasické i multiplikátory'],
              ['<a href="/rybarske-pruty/">Rybářské pruty</a>', 'různé délky a typy pro dravce, mír, moře'],
              ['<a href="/vlasce-a-snury/">Vlasce a šňůry</a>', 'náhradní náplně a pletené šňůry'],
              ['<a href="/rybarske-doplnky/">Rybářské doplňky</a>', 'drobné vybavení, podběráky, nástavce'],
              ['<a href="/rybarske-tasky/">Tašky, pouzdra a krabičky</a>', 'přeprava prutů a drobností'],
              ['<a href="/nastrahy-a-navnady/">Nástrahy a návnady</a>', 'umělé nástrahy na dravce']]) +
          '<p>Několik položek patří i mimo rybolov, například <a href="/sportovni-tasky/">sportovní tašky</a>, <a href="/mikiny/">mikiny</a> a <a href="/kardio-trenazery/">rotopedy</a>. Na ty se nezaměřujeme, protože hlavní hodnotu značky v katalogu tvoří rybolov.</p>'
          '<h2>Jak číst názvy navijáků</h2>'
          '<p>Názvy obsahují jméno řady, rok vydání a řadu zkratek. Rok před jménem, například 23 nebo 24, označuje ročník modelu, takže starší ročníky mohou být levnější. Za jménem se objevuje velikost, třeba 2500 nebo 4000, někdy doplněná písmeny určujícími hloubku cívky nebo převod.</p>'
          + T(['Zkratka', 'Význam'], [
              ['LT', 'označení lehčí konstrukce navijáku; u konkrétního modelu čtěte popis'],
              ['C, XH, H', 'převodový poměr, od nižšího k vyššímu, tedy rychlost navíjení'],
              ['D, S, LD', 'hloubka nebo typ cívky; konkrétní význam určuje model'],
              ['SCW, QD', 'zkratky doplňkových funkcí; hledejte v popisu výrobku'],
              ['Číslo velikosti (2500, 4000)', 'větší číslo znamená větší cívku a nosnost']]) +
          '<p>Zkratky nemusejí mít stejný význam u všech řad, proto se vždy spolehněte na popis konkrétního produktu. Pokud něco nenajdete, porovnejte s technickými údaji u prodejce.</p>'
          '<h2>Klasický naviják, nebo multiplikátor</h2>'
          '<p>Klasický naviják s pevnou cívkou je nejběžnější a nejodpouštějící. Hodí se pro začátečníky, na lehké nástrahy, přívlač i feeder. Multiplikátor má otočnou cívku a navíjí se při hozu jako rotor, je vhodný pro těžší nástrahy a přesné nahazování, ale vyžaduje cvik, protože při špatném nastavení vzniká takzvaná „paruka“ z vlasce. V nabídce Daiwa najdete oboje: například modely Tatula nebo Saltiga jsou multiplikátory, řady Legalis, Freams a Prorex klasické navijáky.</p>'
          '<ul><li><strong>Pro začátek:</strong> klasický naviják střední velikosti, který unese vlasec a nástrahy na běžné vody.</li>'
          '<li><strong>Pro přívlač na dravce:</strong> střední nebo menší velikost s rychlejším převodem, spárovaná s lehkým prutem.</li>'
          '<li><strong>Pro těžké nástrahy a moře:</strong> robustnější model; multiplikátor nebo velký statický naviják.</li>'
          '<li><strong>Pro leváky:</strong> mnoho multiplikátorů se prodává v pravé a levé variantě; zkontrolujte označení.</li></ul>'
          '<p>Doplňující srovnání nabízejí značky <a href="/znacka/shimano/">Shimano</a>, <a href="/znacka/penn/">Penn</a> a <a href="/znacka/abu-garcia/">Abu Garcia</a>. Daiwa se v katalogu vyznačuje tím, že pokrývá široký rozsah od jednodušších řad po prémiové modely. Další hotové porovnání najdete v landingu <a href="/navijaky-shimano/">navijáky Shimano</a> a <a href="/navijaky-penn/">navijáky Penn</a>.</p>'
          '<h2>Vybíráme prut</h2>'
          '<p>Prut musí odpovídat způsobu lovu, nástrahám a návnadám. Rozhoduje délka, hmotnost nahazování a akce, tedy to, v jaké části se prut ohýbá. Krátký prut se hodí k lovu z lodi a z pobřežní vegetace, delší na přesné nahazování na vzdálenost. Hmotnost nahazování určuje rozmezí, ve kterém prut bezpečně vrhá nástrahu, a mělo by odpovídat vašim nástrahám.</p>'
          + T(['Parametr', 'Co říká', 'Na co si dát pozor'], [
              ['Délka', 'dosah hodu a ovladatelnost', 'delší je pohodlnější na vzdálenost, ale hůř se nosí'],
              ['Hmotnost nahazování', 'rozmezí nástrah', 'držte se uprostřed rozmezí, ne na jeho hraně'],
              ['Akce', 'rychlost a ohyb prutu', 'rychlé akce jsou citlivé, pomalé odpouštějí chyby'],
              ['Počet dílů', 'transport', 'více dílů znamená kratší složenou délku'],
              ['Rukojeť', 'komfort a váha', 'u lehkých prutů významná pro vyváženost']]) +
          '<p>Při kombinaci prutu a navijáku dbejte na vyvážení. Příliš těžký naviják na jemném prutu unavuje ruku a snižuje citlivost. Na rozměrnější stránky se podívejte do kategorie <a href="/rybarske-pruty/">rybářské pruty</a>.</p>'
          '<h2>Vlasec, šňůra a jejich spárování</h2>'
          '<p>Monofilní vlasec se natahuje, odpouští chyby a je levný. Pletená šňůra je citlivější, nenatahuje se a snese větší zatížení při menším průměru, ale hůř se uzluje a je viditelnější. Mnoho rybářů proto přidává na konec šňůry průvazec z jiného materiálu. Průměr a nosnost vždy zkontrolujte s ohledem na naviják, který má na cívku určenou kapacitu. Ucelený přehled nabízí kategorie <a href="/vlasce-a-snury/">vlasce a šňůry</a>.</p>'
          '<ol><li>Zvolte prut podle způsobu lovu a nástrah.</li>'
          '<li>K prutu vyberte velikost navijáku, která prut nepřetíží.</li>'
          '<li>Na cívku navíjejte vlasec správné nosnosti a průměru, ne vyšší než doporučená kapacita.</li>'
          '<li>Nástrahy volte podle rozmezí hmotnosti prutu a druhu ryb.</li>'
          '<li>Nastavte brzdu tak, aby povolila dříve, než praskne vlasec.</li></ol>'
          '<h2>Péče a životnost</h2>'
          '<p>Po rybaření, zejména ve slané vodě, naviják opláchněte čerstvou vodou a nechte oschnout. Neponořujte jej do vody celý, pokud to výrobce neuvádí. Brzdu na konci výpravy povolte, aby se nestlačovaly kotouče. Pruty po každé výpravě očistěte, zkontrolujte očka na praskliny a skladujte je v pouzdru. Vlasce nechte před sezonou prohlédnout nebo vyměňte, protože světlo a čas je oslabují. Skladování a přenášení jsou zjednodušené při použití <a href="/rybarske-tasky/">pouzder a tašek</a>.</p>'
          '<h2>Jak sledovat slevy</h2>'
          '<p>Navijáky se po uvedení nového ročníku často zlevňují. Do výběru proto zahrňte starší ročník, který je technicky blízký novějšímu. Prodejci mívají akce před sezonou a při výprodeji skladu. Při porovnání dbejte na to, aby si odpovídaly velikost, převod, ročník a varianta pro leváky. Konkrétní model můžete otevřít a porovnat nabídky obchodů, a ušetřit tak čas při hledání nejlepší nabídky.</p>',
    faq=[
        ('Co znamenají čísla jako 2500 nebo 4000 u navijáku?',
         'Určují velikost cívky a navijáku. Větší číslo znamená větší kapacitu vlasce a vyšší nosnost, ale také vyšší váhu. Na lehký prut stačí menší číslo.'),
        ('Proč jsou v názvu čísla 23 nebo 24?',
         'Většinou označují ročník modelu. Starší ročníky mohou být levnější, přitom se technicky blíží novějším verzím. Ověřte rozdíly v popisu výrobku.'),
        ('Je lepší klasický naviják, nebo multiplikátor?',
         'Klasický je univerzálnější a odpouští chyby. Multiplikátor se hodí pro těžší nástrahy a přesné nahazování, ale vyžaduje cvik. Začátečníkovi doporučujeme klasický model.'),
        ('Jak vybrat velikost navijáku k prutu?',
         'Řiďte se hmotností nahazování prutu, druhem lovu a vlascem. Naviják nesmí prut přetížit ani být příliš malý pro nosnost vlasce.'),
        ('Jaký je rozdíl mezi vlascem a pletenou šňůrou?',
         'Vlasec se natahuje a je odpustnější, šňůra je citlivější a pevnější při stejném průměru. Šňůra se hůř uzluje a bývá viditelnější, proto se často používá s průvazcem.'),
        ('Jak pečovat o naviják po rybaření?',
         'Opláchněte jej čerstvou vodou, nechte oschnout a povolte brzdu. Po slané vodě je to obzvlášť důležité. Skladujte v suchu a před sezonou zkontrolujte chod.'),
        ('Dá se Daiwa použít i pro začátečníky?',
         'Ano, v nabídce jsou jednodušší řady s klasickým navijákem. Důležitější než jméno řady je správná velikost, vyvážení s prutem a nastavení brzdy.'),
        ('Co je nejdůležitější u rybářského prutu?',
         'Délka, hmotnost nahazování a akce. Prut musí odpovídat nástrahám i způsobu lovu. Držte se uprostřed uvedeného rozmezí.'),
        ('Kdy se navijáky zlevňují?',
         'Nejčastěji po uvedení nového ročníku, před sezonou a při výprodeji skladu. Porovnávejte stejnou velikost, převod a variantu pro leváky.'),
    ])

# ------------------------------------------------------------------ mikado
NEW['mikado'] = dict(
    title='Mikado: pruty, navijáky, návnady a rybářské tašky',
    desc='Mikado v katalogu: rybářské pruty, doplňky, navijáky, vlasce, nástrahy, pouzdra a holínky. Jak vybrat kaprařský prut, naviják a výbavu k vodě.',
    intro='<p>Mikado je v katalogu značka rybářského vybavení s velmi širokým záběrem. Nejvíc je tu rybářských prutů, za nimi rybářské doplňky, navijáky, vlasce a šňůry, nástrahy a návnady a tašky, pouzdra a krabičky. Menší skupiny tvoří holínky, bivaky, lehátka a křesla, muškaření a kajaky. '
          'V názvech se objevují kaprařské prut Intro Carp, navijáky řad Sky Dream, Noctis, Bixlite, Trython a Carus a praktické doplňky jako pouzdra na pruty. Barevně vládne zelená, doplněná černou a šedou, protože rybáři obvykle volí maskovací odstíny. '
          'Průvodce vysvětluje, jak z široké nabídky poskládat funkční sadu, jak číst délku a hmotnost prutu, co znamenají zkratky FD u navijáků a jak vybrat pouzdro a holínky. Začít můžete v kategoriích <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/rybarske-doplnky/">rybářské doplňky</a> a <a href="/rybarske-navijaky/">navijáky</a>.</p>',
    guide='<h2>Co Mikado v katalogu nabízí</h2>'
          '<p>Rozsah je podobný malému rybářskému obchodu: kromě základu prut plus naviják se tu najde pouzdro, křeslo, holínky i nástrahy. Díky tomu lze jednou značkou vybavit celou výpravu.</p>'
          + T(['Kategorie', 'Co v ní hledat'], [
              ['<a href="/rybarske-pruty/">Rybářské pruty</a>', 'největší skupina; kaprařské, přívlačové, feederové'],
              ['<a href="/rybarske-doplnky/">Rybářské doplňky</a>', 'široká škála příslušenství k rybolovu'],
              ['<a href="/rybarske-navijaky/">Navijáky</a>', 'řady od základních po vyšší třídy'],
              ['<a href="/vlasce-a-snury/">Vlasce a šňůry</a>', 'náplně na cívky'],
              ['<a href="/nastrahy-a-navnady/">Nástrahy a návnady</a>', 'umělé nástrahy a háčky'],
              ['<a href="/rybarske-tasky/">Tašky, pouzdra a krabičky</a>', 'pouzdra na pruty a organizéry'],
              ['<a href="/holinky/">Holínky</a>', 'obuv k vodě a do bláta'],
              ['<a href="/bivaky-a-kresla/">Bivaky, lehátka a křesla</a>', 'komfort na dlouhé sezení u vody'],
              ['<a href="/muskareni/">Muškaření</a>', 'doplňky pro lov na mušku'],
              ['<a href="/kajaky-a-cluny/">Kajaky a čluny</a>', 'drobnější plavidla']]) +
          '<p>Přehled doplňují několik <a href="/mikiny/">mikin</a> a <a href="/kardio-trenazery/">rotopedů</a>, které do rybolovu nepatří. Jádrem zůstává rybářská výbava.</p>'
          '<h2>Kaprařský prut: délka, libra a díly</h2>'
          '<p>V názvech prutů se opakuje trojice údajů, například 12 ft, 3,6 m a 3 lb. Je to délka ve stopách, délka v metrech a testovací křivka v librách, která vyjadřuje, jak silný prut je. Poslední údaj, třeba 3-dí, říká počet dílů. Pro začátek je nejběžnější prut dlouhý zhruba tři a půl až čtyři metry s křivkou kolem tří liber, ale konkrétní parametry vždy volte podle vody a hmotnosti nástrah.</p>'
          + T(['Údaj v názvu', 'Co určuje', 'Praktický dopad'], [
              ['Délka (ft, m)', 'dosah a ovladatelnost', 'delší hází dál, ale hůř se manipuluje u břehu'],
              ['Test (lb)', 'zatížení a síla prutu', 'vyšší hodnota pro těžší olova a větší ryby'],
              ['Počet dílů', 'složená délka', 'více dílů se snáze převáží'],
              ['Typ prutu', 'kaprařský, přívlačový, feederový', 'každý je stavěn pro jiný způsob lovu']]) +
          '<p>Prut Intro Carp II z názvů je typickým začátečnickým kaprařským prutem. Zvolte ho, pokud chcete jednoduchý a cenově dostupný základ pro lov na stojaté vodě. Zkušenější rybáři si často vybírají podle citlivosti a váhy a srovnávají s jinými výrobci, například <a href="/znacka/daiwa/">Daiwa</a>, <a href="/znacka/korum/">Korum</a> nebo <a href="/znacka/delphin/">Delphin</a>.</p>'
          '<h2>Navijáky a zkratky FD</h2>'
          '<p>V názvech navijáků se objevují jména řad (Sky Dream, Noctis, Bixlite, Trython, Carus, Sensual) a čtyřčíslí, například 3006 nebo 5010, které označuje velikost. Zkratka FD označuje zadní brzdu, tedy systém, který se ovládá otočným kolečkem na konci navijáku. Takové uspořádání se v kaprařském rybolovu hodně využívá, protože umožňuje jemné nastavení při záseku. Zkratka HG označuje vysoký převodový poměr. Někdy se objeví i název s Runner, což je typ s volným chodem pro lov s nastraženou udicí.</p>'
          '<ul><li><strong>Velikost:</strong> menší čísla na lehký prut a menší vodu, vyšší na těžké nástrahy a dálkové hody.</li>'
          '<li><strong>Zadní brzda:</strong> pohodlná pro delší lov, citlivě se nastavuje.</li>'
          '<li><strong>Volný chod (Runner):</strong> hodí se, když necháváte nástrahu ležet a bez dozoru ji chvíli necháte.</li>'
          '<li><strong>Surfcast:</strong> název řady naznačuje použití na pobřeží a při dálkovém lovu.</li></ul>'
          '<p>Další zdroje porovnání jsou <a href="/navijaky-daiwa/">navijáky Daiwa</a>, <a href="/navijaky-shimano/">navijáky Shimano</a> a <a href="/navijaky-fox/">navijáky Fox</a>.</p>'
          '<h2>Pouzdra, tašky a doplňky</h2>'
          '<p>Pouzdra na pruty se v nabídce dělí podle počtu komor, například jednokomorové, čtyřkomorové nebo tříkomorové. Počet komor odpovídá počtu sestavených prutů, které lze uložit, a vnější velikost má odpovídat délce prutů. Zvolte pouzdro delší než nejdelší prut a pevné zipy a zesílené dno. Krabičky a organizéry udržují háčky, olova a drobnosti odděleně, takže na vodě najdete, co potřebujete.</p>'
          + T(['Doplněk', 'Co zvážit'], [
              ['Pouzdro na pruty', 'počet komor, délka, zesílení rohů'],
              ['Taška na vybavení', 'prostor na krabičky, voděodolnost, popruhy'],
              ['Křeslo nebo lehátko', 'nosnost, nastavitelné nohy, váha při přenášení'],
              ['Holínky', 'velikost se silnější ponožkou, výška svršku'],
              ['Krabičky', 'přihrádky, těsnění, odolnost proti vlhku']]) +
          '<p>Kategorie <a href="/rybarske-tasky/">tašky, pouzdra a krabičky</a> a <a href="/bivaky-a-kresla/">bivaky, lehátka a křesla</a> ukazují pohodlí na delší výpravu. Pokud vás zajímá volnější lov bez sedění, podívejte se na <a href="/muskareni/">muškaření</a>.</p>'
          '<h2>Holínky a oblečení k vodě</h2>'
          '<p>Zelené holínky patří k typické výbavě. Důležitá je velikost s rezervou na teplou ponožku, protože v zimě noha v gumové botě mrzne. Podešev by měla mít vzorek, který drží na blátě, a svršek dostatečnou výšku, aby do něj nezatekla voda při brodění. Jsou-li holínky příliš těsné, otlačují lýtko, jsou-li příliš volné, sklouzává pata. Doplňují je mikiny a teplé vrstvy, které můžete porovnat v kategorii <a href="/mikiny/">mikiny</a>.</p>'
          '<h2>Jak poskládat základní sadu</h2>'
          '<ol><li>Rozhodněte se, jakou rybu a na jaké vodě chcete lovit.</li>'
          '<li>Vyberte prut s délkou a testem odpovídajícím nástrahám.</li>'
          '<li>K prutu přiřaďte naviják vhodné velikosti a navinujte vlasec s dostatečnou nosností.</li>'
          '<li>Přidejte pouzdro, krabičky s háčky a olovy a podběrák.</li>'
          '<li>Na závěr doplňte pohodlí: křeslo, holínky a vhodné oblečení.</li></ol>'
          '<h2>Péče a kontrola před sezonou</h2>'
          '<p>Pruty po rybaření otřete a osušte, zejména spoje dílů. Naviják opláchněte, namažte podle návodu a povolte brzdu. Vlasec před sezonou zkontrolujte po celé délce na zdrsnělá místa a v případě pochybností vyměňte. Pouzdra a tašky skladujte suché, aby se nevytvořila plíseň. Holínky nesušte u topení, guma by zkřehla. Drobné opravy, jako výměna očka nebo rukojeti, se vyplatí při starších prutech.</p>'
          '<h2>Kdy sledovat slevy</h2>'
          '<p>Slevy na rybářské vybavení se opakují před sezonou a po ní, kdy obchody uvolňují sklad. Sety prutu a navijáku bývají výhodnější než kusy samostatně, ale ověřte, že se hodí k sobě. Při srovnání dbejte na stejnou délku, test a barvu. Menší doplňky se vyplatí kupovat ve více kusech, pokud je obchod nabízí v sadě.</p>',
    faq=[
        ('Co znamená 12 ft 3,6 m 3 lb v názvu prutu?',
         'Je to délka prutu ve stopách a metrech a testovací křivka v librách. Křivka vyjadřuje sílu prutu a vhodnou zátěž nástrah. Číslo 3-dí udává počet dílů.'),
        ('Jaký kaprařský prut zvolit pro začátek?',
         'Pro stojatou vodu bývá běžný prut kolem tří a půl až čtyř metrů s mírnou testovací křivkou. Konkrétní volbu přizpůsobte vzdálenosti hodu a velikosti ryb.'),
        ('Co znamená zkratka FD u navijáku?',
         'Označuje zadní brzdu ovládanou kolečkem na konci navijáku. Hodí se do lovu, kde potřebujete jemně nastavit odpor při záseku a při tahu ryby.'),
        ('K čemu je označení HG?',
         'Obvykle jde o vyšší převodový poměr. Naviják navine víc vlasce na jednu otáčku kliky, což se hodí pro rychlejší navíjení. Konkrétní hodnotu hledejte v popisu.'),
        ('Co je naviják Runner?',
         'Typ s volným chodem pro lov, při kterém necháte nástrahu ležet a ryba může volně táhnout. Při záseku se chod přepne zpět na normální navíjení.'),
        ('Jak vybrat pouzdro na pruty?',
         'Zvolte počet komor podle počtu prutů a délku větší, než je nejdelší prut ve složeném stavu. Dobré jsou zesílené rohy, pevné zipy a polstrování.'),
        ('Jak vybrat velikost holínek?',
         'Raději s rezervou na teplou ponožku, protože v zimě noha v gumové botě mrzne. Příliš volná bota ale sklouzává z paty, proto ji vyzkoušejte s ponožkou.'),
        ('Dá se u Mikada koupit i vybavení na muškaření?',
         'V katalogu je menší kategorie muškaření. Pro rozsáhlejší výběr se podívejte do dané kategorie a porovnejte značky podle potřeby.'),
        ('Kdy se vyplatí sledovat slevy?',
         'Před sezonou a po jejím konci, kdy obchody uvolňují sklad. Porovnávejte stejné délky, testy a barvy a ověřte, že sety prutu a navijáku k sobě opravdu patří.'),
    ])

# ------------------------------------------------------------------ extra sections
NEW['salomon']['guide'] += (
    '<h2>Zimní sortiment jako doplněk</h2>'
    '<p>Menší část nabídky patří zimě. Lyžařské boty, helmy a brýle se hodí tomu, kdo si chce sladit výbavu u jednoho výrobce, ale při výběru rozhodují vlastní parametry: tvar lýtka, šířka nohy a úroveň lyžování. Helmu zkoušejte s čepicí, kterou nosíte, a brýle ke konkrétní helmě, aby mezi nimi nevznikla mezera na čele. Chcete-li chodit po zasněžených cestách bez lyží, hledejte v kategorii <a href="/zimni-obuv/">zimní boty a sněhule</a> model s teplou vložkou a hrubším vzorkem podešve.</p>'
)

NEW['smartwool']['guide'] += (
    '<h2>Jak sestavit systém tří vrstev</h2>'
    '<p>Merino se nejlépe uplatní, když ho vnímáte jako součást systému. Základní vrstva leží na kůži, střední vrstva drží teplo a vnější chrání před větrem a deštěm. Ponožky pak doplňují systém od nohou. V chladném počasí se vyplatí kombinace tenčího trička, mikiny z vlny a membránové bundy, ve které se můžete v pohybu odepnout a vrstvu odebrat. Do menšího batohu se vejde i náhradní tričko, protože vlna zahřívá i vlhká, ale po zastavení rychle prochladnete.</p>'
    '<ul><li><strong>Při chůzi do kopce:</strong> odepněte vrchní vrstvu dřív, než se zapotíte.</li>'
    '<li><strong>Při zastávce:</strong> hned oblékněte teplejší vrstvu, ať neprochladnete.</li>'
    '<li><strong>Na noc v chatě:</strong> suché merino tričko a ponožky vám zajistí příjemný spánek bez dalšího vybavení.</li></ul>'
    '<h2>Dárky a drobnosti</h2>'
    '<p>Vzorované ponožky a čepice jsou praktický dárek, protože velikostní rozsah je široký a málokdo má merino víc, než potřebuje. Při výběru se zeptejte na délku, kterou dotyčný nosí, a raději volte neutrální barvu. Pro rodiče malých dětí se hodí výběr dětských ponožek, které nejsou příliš tlusté, protože se do dětské boty musí vejít. Pro cestovatele jsou praktické kousky, které se dají prát v umyvadle a rychle schnou.</p>'
    '<h2>Časté chyby při výběru</h2>'
    '<ol><li>Volba příliš silných ponožek do těsné boty: noha se stlačí a hůře prokrvuje.</li>'
    '<li>Nákup podle barvy bez kontroly složení materiálu.</li>'
    '<li>Praní s aviváží, která zhoršuje vlastnosti vlákna.</li>'
    '<li>Sušení na radiátoru, po kterém se vlna zahrubí.</li>'
    '<li>Zapomenutí na velikost u dětských ponožek, které rychle přestanou stačit.</li></ol>'
    '<p>Větší výběr pro celou rodinu najdete v kategoriích <a href="/merino-doplnky/">merino doplňky</a> a <a href="/cepice-a-celenky/">čepice a čelenky</a>.</p>'
)

NEW['daiwa']['guide'] += (
    '<h2>Podle způsobu lovu</h2>'
    '<p>Stejná značka obsahuje vybavení pro několik rybářských stylů. Při přívlači na dravé ryby chodíte po břehu a mnoho hodů provádíte s lehkými nástrahami, proto hledáte lehčí kombinaci s citlivým prutem. Při lovu z lodi nebo na moři se zvyšují nároky na nosnost, odolnost proti soli a velikost cívky. Pro lov na nástrahu u dna je potřeba stabilní prut a naviják s dostatečnou brzdou. Proto před nákupem napište, na jakou rybu a v jakém prostředí chcete lovit, a podle toho kombinaci sestavte.</p>'
    '<ul><li><strong>Přívlač:</strong> menší velikost navijáku, rychlý převod, prut s citlivou špičkou.</li>'
    '<li><strong>Casting s multiplikátorem:</strong> těžší nástrahy, přesné hody, nutnost nastavit brzdu cívky.</li>'
    '<li><strong>Moře:</strong> robustní konstrukce a čistění po každém výjezdu.</li>'
    '<li><strong>Lov z lodi:</strong> kratší prut, který nepřekáží ve vesle a lodním vybavení.</li></ul>'
    '<h2>Nástrahy a doplňky v nabídce</h2>'
    '<p>Menší část nabídky tvoří <a href="/nastrahy-a-navnady/">nástrahy</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>. U nástrah se vyplatí kombinovat několik velikostí a barev, protože ryby reagují na světlo, zákal i roční dobu. Pro začátek stačí pár osvědčených kousků v přirozených barvách a jedna výraznější varianta pro kalnou vodu. Krabičku s háčky a závažími vždy udržujte v suchu, aby kov nekorodoval. Doplňky jako podběrák, metr nebo kleště zkontrolujte před výpravou.</p>'
    '<h2>Časté chyby při výběru</h2>'
    '<ol><li>Příliš velký naviják na lehký prut, který pak přepadá dopředu.</li>'
    '<li>Plná cívka vlasce až po okraj, což vede ke spletení.</li>'
    '<li>Příliš utažená brzda, která nedovolí rybě vybrat vlasec.</li>'
    '<li>Zanedbání čištění po rybaření ve slané vodě.</li></ol>'
)

NEW['mikado']['guide'] += (
    '<h2>Podle typu vody</h2>'
    '<p>Rybář na malé stojaté vodě potřebuje jiné vybavení než ten, kdo loví na velké řece nebo na pobřeží. U menších rybníků stačí kratší prut a menší naviják, protože se nehází daleko a ryby jsou blíž. Na velkých nádržích a při dálkovém lovu se hodí delší prut s vyšším testem a naviják větší velikosti. V proudu rozhoduje stabilita nástrahy a odolnost vlasce proti otěru o kameny. Řada Surfcast naznačuje využití na pobřeží, kde záleží na dálce hodu a silném vlasci.</p>'
    '<ul><li><strong>Malý rybník:</strong> lehčí prut, menší naviják, jemnější vlasec.</li>'
    '<li><strong>Velká nádrž:</strong> delší prut, větší cívka, vyšší nosnost.</li>'
    '<li><strong>Řeka:</strong> odolný vlasec a těžší olova pro držení návnady na místě.</li>'
    '<li><strong>Dlouhé sezení:</strong> pohodlné křeslo nebo lehátko, protože na vodě trávíte hodiny.</li></ul>'
    '<h2>Kajaky, čluny a bivaky</h2>'
    '<p>Menší kategorie <a href="/kajaky-a-cluny/">kajaky a čluny</a> se týká rybářů, kteří se potřebují dostat na místa nedostupná z břehu. U plavidel kontrolujte nosnost a rozměry při převozu a skladování. Bivak a lehátko prodlužují pobyt u vody, ale zvyšují váhu zavazadel. Zvažte, kolik nocí chcete trávit venku a jak daleko od auta se chystáte jít, a podle toho vyberte nejlehčí variantu, která stačí.</p>'
    '<h2>Časté chyby při výběru</h2>'
    '<ol><li>Příliš silný prut pro malou vodu, který ryby nepustí do bojového zápasu.</li>'
    '<li>Pouzdro kratší než složený prut.</li>'
    '<li>Zanedbání zkontrolování očka před sezonou.</li>'
    '<li>Koupě holínek bez rezervy na ponožku.</li></ol>'
)

NEW['smartwool']['faq'] += [
    ('Hodí se merino i pro děti?',
     'Ano, dětské ponožky a spodní vrstvy jsou v nabídce. Vlna zahřeje a neškrábe, pokud je jemná. Při koupi počítejte s rychlým růstem a raději vybírejte tenčí kousky, které se vejdou do dětské boty.'),
    ('Mohu merino nosit pod běžným oblečením každý den?',
     'Samozřejmě. Tenká merino trička a nižší ponožky se nosí do kanceláře i do města. Výhodou je, že se po vyvětrání dají použít opakovaně bez zápachu.'),
    ('Čím se kompresní ponožky liší od běžných?',
     'Mají těsnější střih, který podporuje chodidlo a lýtko. Hodí se na delší běh nebo cestování, ale pro běžné nošení mohou být nepohodlné. Velikost proto zkontrolujte přesněji.'),
]
NEW['daiwa']['faq'] += [
    ('Jak naplnit cívku navijáku?',
     'Navíjejte vlasec s mírným napětím a nechte okraj cívky volný zhruba milimetr až dva. Plná cívka vede ke spletení při hodu, příliš prázdná zkracuje dosah.'),
    ('Mám zvolit levou, nebo pravou ruku u multiplikátoru?',
     'Většinou se klika drží v ruce, kterou netočíte prutem při hodu, ale záleží na zvyku. Obě varianty se prodávají a před koupí ověřte označení, protože výměna bývá složitější.'),
    ('Dají se navijáky použít i ve slané vodě?',
     'Pouze modely, u kterých to výrobce uvádí, například řady určené na moře. Po každém výjezdu naviják opláchněte sladkou vodou a nechte oschnout.'),
]
NEW['mikado']['faq'] += [
    ('Jak poznám, že je vlasec starý?',
     'Ztrácí pružnost, drhne o prsty, na světle bývá matný a tvoří zákruty, které se nevyrovnají. Pak je lepší ho vyměnit, než riskovat přetržení při záseku.'),
    ('Kolik komor má mít pouzdro na pruty?',
     'Tolik, kolik prutů vezete sestavených. Pro začátek jedno- nebo tříkomorové, pro více prutů čtyřkomorové. Délku vybírejte podle nejdelšího prutu.'),
    ('Jaké barvy volit na rybářské vybavení?',
     'Zelené, hnědé a šedé odstíny splynou s břehem a neplaší ryby. Výrazné barvy mají význam u doplňků, které chcete snadno najít, například u krabiček.'),
]
NEW['daiwa']['faq'] += [
    ('Musím mít k navijáku i náhradní cívku?',
     'Není to nutné, ale hodí se. Na druhou cívku navinete jiný vlasec nebo šňůru a podle podmínek ji během několika vteřin vyměníte, aniž byste kupovali další naviják.'),
]
