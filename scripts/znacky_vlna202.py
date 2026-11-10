"""sporteka.cz — brand page texts wave 202: converse, geox, new-balance, asics.
Only generally known facts, derived from catalogue categories and product names. No prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ converse
NEW['converse'] = dict(
    title='Converse: tenisky Chuck Taylor, trička a mikiny',
    desc='Converse v katalogu sporteky: plátěné i kožené tenisky Chuck Taylor All Star, dámské, dětské a pánské modely, trička, mikiny a batohy. Průvodce výběrem.',
    intro='<p>Converse je v katalogu sporteky téměř celý o obuvi. Naprostou většinu nabídky tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, hlavně kotníkové a nízké modely z řady Chuck Taylor All Star, a kolem nich stojí menší výběr oblečení. Najdete tu trička s hvězdou, mikiny, tepláky, čepice, městské batohy, pár basketbalových bot a zimní modely. Nabídka míří především na ženy a dívky, velkou část tvoří dětské velikosti a mužské i unisex kousky doplňují zbytek. Stránka vám pomůže zorientovat se v tom, čím se liší plátěná a kožená verze, kdy dává smysl platforma nebo zesílená podrážka, jak velikosti vycházejí v praxi a jak sledovat slevy, aby se vám cenové srovnání z více obchodů skutečně vyplatilo. Texty vycházejí z toho, co v katalogu skutečně je, nikoli z historie značky.</p>',
    guide='<h2>Co Converse v katalogu nabízí</h2>'
          '<p>Značka je v nabídce sporteky nejvíc vidět jako výrobce jednoho rozpoznatelného střihu. Ten se opakuje v desítkách barev, materiálů a výšek kotníku, a proto je obuvi mnohonásobně víc než čehokoli jiného. Oblečení tvoří menšinu a drží se stejného vizuálního stylu: logo s hvězdou, výšivka nebo velký potisk na hrudi. Když tedy hledáte Converse, nejde o sportovní značku ve smyslu technických bot na výkon, ale o značku, která patří do každodenního šatníku a do street stylu.</p>'
          + T(['Skupina zboží', 'Co v ní najdete', 'Pro koho je nejčastěji'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'plátěné i kožené kotníkové a nízké tenisky, modely s plošnou podrážkou, dětské capáčky', 'ženy, děti, muži'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'bavlněná trička s logem, výšivkou a potiskem hvězdy', 'unisex, dámské'],
              ['<a href="/basketbalova-obuv/">Basketbalové boty</a>', 'vysoké boty s podporou kotníku pro hru i pro nošení', 'muži a dospívající'],
              ['<a href="/mikiny/">Mikiny</a> a <a href="/fleecove-mikiny/">fleecové mikiny</a>', 'mikiny s kapucí a bez ní, mikiny s výšivkou', 'unisex'],
              ['<a href="/teplaky/">Tepláky</a>', 'volné bavlněné tepláky k mikině', 'unisex, dámské'],
              ['<a href="/cepice-a-celenky/">Čepice a kšiltovky</a>', 'kšiltovky a zimní čepice s logem', 'všichni'],
              ['<a href="/mestske-batohy/">Městské batohy</a>', 'školní a každodenní batohy', 'děti, studenti'],
              ['<a href="/zimni-obuv/">Zimní boty</a>', 'kotníkové boty s vodoodolnou úpravou a hrubší podešví', 'ženy, děti']]) +
          '<h2>Pro koho Converse vybírat: pohlaví a děti</h2>'
          '<p>Podle filtru pro koho jsou nejpočetnější dámské modely, hned za nimi dětské a teprve potom pánské. Je to logické: ženám slouží nízké a kotníkové tenisky jako běžná městská obuv a děti se do nich obouvají do školy i na hřiště. Muži kupují hlavně klasický kotníkový střih a trička. Unisex označení se objevuje u triček a mikin, kde pohlaví nerozhoduje, a občas i u bot ve společné velikostní řadě.</p>'
          '<p>U dětí věnujte pozornost dvěma různým skupinám. Malé capáčky pro batolata mají měkkou podrážku a bývají na suchý zip nebo gumičku, takže se obouvají samy. Školní velikosti už napodobují dospělé tenisky a mají šněrování. Pokud vybíráte pro rostoucí nohu, počítejte s malou rezervou na délku, ale ne s plnou velikostí navíc: u plátěné boty bez pevné pěty by se noha při velkém prostoru ohýbala na špatném místě.</p>'
          '<h2>Plátno, kůže nebo platforma</h2>'
          '<p>Základní rozhodnutí u Converse je materiál a podrážka. Plátno je lehké, prodyšné a dobře se pere, ale při dešti rychle promokne. Kůže vydrží víc, hůře se špiní a lépe odolává vodě, na druhou stranu bývá tužší a na rozchození potřebuje několik dnů. Modely s označením lift mají vyšší platformu, která opticky prodlouží nohu, ale je těžší a při dlouhé chůzi méně pohodlná. Varianta s lugged heel má zesílenou strukturovanou podrážku s větším záběrem a hodí se do horšího počasí.</p>'
          + T(['Typ', 'Výhoda', 'Na co si dát pozor'], [
              ['Plátěný nízký model', 'lehký, vzdušný, na léto a do města', 'nechrání před vodou a nemá žádnou podporu kotníku'],
              ['Plátěný kotníkový model', 'klasický vzhled, trochu stability', 'v horku se v něm hodně potí'],
              ['Kožený model', 'odolnost, snadná údržba, delší životnost', 'delší rozchození, vyšší hmotnost'],
              ['Model s platformou (lift)', 'výraznější silueta', 'těžší a méně ohebný při dlouhé chůzi'],
              ['Model s lugged heel nebo vodoodolný', 'záběr a ochrana v mokru', 'o něco robustnější vzhled, vyšší váha']]) +
          '<p>Chcete-li jedny boty na celý rok, zvolte kožený nebo vodoodolný model v tmavé barvě. Na léto a na cestování vyhraje plátno v neutrální barvě. Pokud chcete nejvíc srovnatelných nabídek, sledujte základní bílé a černé verze, protože jejich cenové rozdíly mezi obchody jsou na srovnávači nejlépe vidět.</p>'
          '<h2>Jak vybírat barvu</h2>'
          '<p>Katalog zobrazuje nejčastěji černé a bílé tenisky, pak růžové, modré, béžové a šedé. Černá se nejlépe maskuje a vydrží nejdéle v městském provozu. Bílá vypadá čistě jen první týdny, pak je potřeba ji pravidelně čistit. Růžová a pastelové odstíny jsou velmi populární u dívek a mladých žen a obvykle patří k sezonním kolekcím, takže se po vyprodání neobjeví. Pokud nevíte, vyberte béžovou nebo šedou: ladí k džínám i k teplákům a nemusíte je tolik prát.</p>'
          '<h2>Velikosti a střih</h2>'
          '<p>Converse se obecně vnímají jako boty se širším a plošším střihem v přední části. Velikosti se často shodují s běžnou městskou obuví nebo vycházejí o půl čísla větší, takže při objednávce z internetu je nejjistější změřit chodidlo a porovnat ho s tabulkou obchodu. U dětských bot se ve vedlejším sloupci uvádí délka vložky v centimetrech, což je přesnější než číslo. V obchodech uvádějí často i EU a US velikost najednou, a proto zkontrolujte, kterou právě čtete. U triček s označením US 2XS nebo 2XL jde o americké označení a střih bývá volnější než evropský.</p>'
          '<ul><li><strong>Změřte chodidlo večer</strong>, kdy je mírně otočené, a přidejte malou rezervu na prsty.</li>'
          '<li><strong>Při mezivelikosti</strong> volte větší číslo, pokud nosíte silnější ponožky.</li>'
          '<li><strong>Vložku si vytáhněte</strong> a přiložte k ní nohu, zjistíte tak skutečný prostor.</li>'
          '<li><strong>Široká noha</strong> se v plátěném modelu cítí lépe než v kožené verzi.</li></ul>'
          '<h2>Oblečení Converse: co k botám přidat</h2>'
          '<p>Trička s hvězdou, mikiny a tepláky jsou jednoduché kousky, které sladíte s botami. Bavlněné materiály se perou na třicet až čtyřicet stupňů a vydrží při obracení naruby, což ochrání potisk a výšivku. Mikiny z <a href="/mikiny/">kategorie mikin</a> jsou praktické na chladnější večery, ve fleecové variantě pak <a href="/fleecove-mikiny/">fleecové mikiny</a> hřejí víc a lépe drží teplo. Čepice a kšiltovky z <a href="/cepice-a-celenky/">čepic a kšiltovek</a> zakončí celé oblečení jednoduchým logem. Pro školáky je praktický batoh z kategorie <a href="/mestske-batohy/">městských batohů</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Plátěné tenisky nepatří do pračky na vysoké teploty, protože lepidlo podrážky může povolit. Nejšetrnější je kartáč, mýdlová voda a pomalé schnutí na vzduchu mimo topení. Kožené modely stačí otřít vlhkým hadříkem a občas ošetřit krémem. Před deštěm pomůže impregnace, která sníží nasákavost bez změny vzhledu. Podrážka se opotřebí nejdřív na patě, takže pravidelně otáčejte páry a nenoste jedny boty každý den. Dětské boty z kvalitní kůže přenášejí často mezi sourozenci, pokud se udržují sušené a čisté.</p>'
          '<h2>Jak Converse porovnat s konkurencí</h2>'
          '<p>Nejbližší alternativou bývají nízké tenisky od značek jako <a href="/znacka/vans/">Vans</a>, <a href="/znacka/superga/">Superga</a> nebo <a href="/znacka/adidas/">Adidas</a>. Converse se obvykle pozná podle vyšší špičky a výrazné gumové ochrany před špičkou. Vans mají často vyztuženou stélku a lepší tlumení, zatímco Superga je plošší a bližší klasickým plátěnkám. Pokud nehledáte sportovní výkon, ale styl a snadnou kombinaci, bude Converse nejvíc srovnatelný s těmito značkami. Pro běh a trénink platí opačně, že se do nich raději neinvestuje, protože podrážka nemá odpružení.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Tenisky Converse se nejčastěji zlevňují mimo sezonu, tedy zimní boty na jaře a letní plátno na podzim. Největší výběr přináší období výprodejů po Vánocích a při letním úklidu skladů. Sledujte také starší barevné verze: stejný střih v méně žádané barvě vyjde výhodněji než aktuální novinka. Nezaměňujte slevu s cenou, kterou obchod porovnává s vlastní dřívější cenou. Praktickou metodou je otevřít produkt ve srovnávači, vybrat více obchodů a porovnat konečnou cenu včetně dopravy. Základní modely se obvykle vrací do skladu, proto počkejte, pokud vám nehoří termín.</p>'
          '<h2>Rychlý rozcestník</h2>'
          '<p>Chcete-li zúžit nabídku, začněte u <a href="/tenisky/">tenisek</a>, použijte filtr pro koho a barvu. Pro hru a ve městě zkuste i <a href="/basketbalova-obuv/">basketbalové boty</a>, pro chladné měsíce se podívejte na <a href="/zimni-obuv/">zimní obuv</a> a na <a href="/pantofle-a-zabky/">pantofle a žabky</a> na bazén. Podobnou volnočasovou nabídku mají i značky ' + B(('vans', 'Vans'), ('superga', 'Superga'), ('skechers', 'Skechers')) + '.</p>',
    faq=[
        ('Jsou Converse vhodné na sport?', 'Plátěné tenisky Converse jsou určené hlavně pro městské nošení a volný čas. Pro běh nebo trénink v hale mají slabé tlumení a malou oporu, proto použijte specializovanou obuv. Výjimkou jsou basketbalové modely, které jsou k dispozici v kategorii basketbalových bot.'),
        ('Jak poznám správnou velikost Converse?', 'Změřte chodidlo v centimetrech a porovnejte ho s tabulkou konkrétního obchodu. Converse bývají o půl čísla větší nebo se shodují s běžnou obuví, ale střih se podle řady liší. U dětí se vyplatí dívat se na délku vložky a nechat malou rezervu.'),
        ('Co je lepší, plátěné nebo kožené tenisky?', 'Plátno je lehčí a vzdušnější, což se hodí na léto. Kůže lépe odolává vodě a špíně a vydrží déle, ale je těžší a potřebuje rozchodit. Na celoroční nošení volte kůži, na teplé měsíce plátno.'),
        ('Dají se Converse prát v pračce?', 'Plátěné modely se někdy perou ve slabém programu bez ždímání, ale lepidlo podrážky to snáší hůř. Bezpečnější je kartáč a mýdlová voda. Kožené tenisky nedávejte do pračky vůbec a otírejte je vlhkým hadříkem.'),
        ('Čím se liší nízké a kotníkové tenisky?', 'Kotníkové tenisky podepřou kotník a vypadají klasicky, ale hůř se větrají. Nízké jsou vzdušnější, snadněji se obouvají a lépe se hodí k šortkám a sukním. Výběr je především otázka stylu, protože podpora kotníku je u plátna omezená.'),
        ('Jsou pro děti vhodné Converse?', 'Ano, nabídka dětských modelů je velká, od capáčků pro nejmenší až po školní tenisky. Hledejte model s pevnější patou, který drží nohu, a dbejte na dostatečný prostor pro prsty. Pro zimu zvolte zimní model, plátno nehřeje.'),
        ('Kdy nakupovat Converse levněji?', 'Zlevňují se hlavně mimo sezonu a při výprodejích po svátcích. Dobře se hledají i starší barvy základních střihů. Porovnejte konečnou cenu v několika obchodech včetně dopravy, ne jen uvedenou slevu.'),
        ('Jak dlouho Converse vydrží?', 'Záleží na materiálu a na tom, jak často je nosíte. Kožený model při střídání párů vydrží několik sezon, plátno se ošoupe dřív, zejména u paty a na špičce. Dlouhodobě pomáhá čištění a sušení při pokojové teplotě.'),
        ('Mají Converse kromě bot i oblečení?', 'Ano, v katalogu jsou trička, mikiny, tepláky, čepice a batohy. Oblečení nese stejný styl s logem a hvězdou a hodí se jako doplněk k obuvi. Většinou jde o volnější unisex střihy, u kterých zkontrolujte tabulku velikostí.'),
        ('Mohu v Converse chodit v zimě?', 'Klasické plátěné modely na mráz nestačí. V katalogu jsou zimní a vodoodolné boty s hrubší podešví, které vydrží sníh a mokro. Pro suchý chladný den si vezměte silnější ponožky a kožený model.'),
    ])

# ------------------------------------------------------------------ geox
NEW['geox'] = dict(
    title='Geox: dětské a dámské boty, sandály a zimní obuv',
    desc='Geox na sporteka.cz: dětské tenisky, pánská a dámská volnočasová obuv, sandály i zimní boty. Jak vybrat řadu, velikost a kdy hledat slevy.',
    intro='<p>Geox je v nabídce sporteky přede vším obuv, a to takové, která se nosí celý den. Většinu katalogu tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, na druhém místě jsou <a href="/sandaly/">sportovní sandály</a> a za nimi zimní boty, barefoot modely, pantofle, trekové boty a holínky. Z oblečení se objevují jen jarní a podzimní bundy, kabáty a čepice, z doplňků sedla na jezdecký sport. Nejpočetnější je dětská řada, podle ní dámská a pánská. Stránka vysvětluje, jak v nabídce rozlišit označení modelů podle prvního písmene, co si vybrat pro školáka a co pro dospělého, jak vybírat sezonní obuv a podle čeho porovnávat ceny mezi obchody. Obsah vychází z názvů produktů v katalogu a z obecných zásad výběru, ne z historie značky.</p>',
    guide='<h2>Co Geox v katalogu nabízí</h2>'
          '<p>Geox patří k značkám, které se soustředí na pohodlí při běžném nošení, takže ve sporteka katalogu nenajdete technické závodní boty. Typický produkt je kotníková nebo nízká volnočasová obuv do města, škola a na procházku. Sandály a zimní obuv doplňují sezonu a menší kategorie ukazují, že značka sahá i k dalším oborům, jako jsou jezdecké doplňky nebo bundy.</p>'
          + T(['Skupina zboží', 'Co v ní najdete', 'Pro koho'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'nízké a kotníkové boty na denní nošení, školní obuv, chlapecké a dívčí modely', 'děti, muži, ženy'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'sandály na suchý zip, na léto a do vody', 'děti, ženy'],
              ['<a href="/zimni-obuv/">Zimní boty a sněhule</a>', 'teplé a vodoodolné boty se zateplením', 'děti, dospělí'],
              ['<a href="/barefoot-obuv/">Barefoot boty</a>', 'tenké ohebné boty s širokou špičkou', 'děti, dospělí'],
              ['<a href="/pantofle-a-zabky/">Pantofle a žabky</a>', 'domácí a plážová obuv', 'všichni'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'pevnější obuv do terénu', 'dospělí'],
              ['<a href="/holinky/">Holínky</a>', 'gumová obuv do deště', 'děti'],
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehčí bundy na přechodná období', 'děti, dospělí']]) +
          '<h2>Jak číst názvy modelů</h2>'
          '<p>V názvech produktů Geox se opakuje systém, který pomáhá při třídění. První písmeno za značkou ukazuje určení: U znamená pánskou obuv, D dámskou a J dětskou, tedy juniorskou. Za ním následuje název řady, například Spherica, Flextride, Foot-Run, Flexyper, Granito nebo Nebula, a někdy dovětek jako WR či WPF, který bývá označením vodoodolné nebo zateplené verze. Přesný význam zkratek ověřte v popisu u konkrétního obchodu, protože se mohou lišit podle sezony. Když se naučíte číst název, snadno poznáte, zda se díváte na školní botu, nebo na pánskou obuv na každý den.</p>'
          '<h2>Děti: největší část nabídky</h2>'
          '<p>Podle filtru pro koho tvoří dětské modely zhruba největší skupinu, a to nejen kvůli školním botám. Děti rostou rychle, takže se obuv mění několikrát za rok a pro každou sezonu je potřeba jiný model. Chlapecké a dívčí označení u Geox je většinou věcí barev a vzhledu, střih bývá podobný. Pro školní věk jsou nejpraktičtější modely na suchý zip nebo gumové tkaničky, protože se obouvají samy a v šatně nezabírají čas. Starší děti sahají spíš po šněrovacích sportovních teniskách, kde je důležité vybírat s dostatečným místem na prsty.</p>'
          '<ul><li><strong>Podrážka:</strong> měla by se ohýbat pod prsty, ale ne uprostřed chodidla.</li>'
          '<li><strong>Pata:</strong> pevná patní část chrání ještě vyvíjející se kotník.</li>'
          '<li><strong>Rezerva:</strong> asi centimetr před špičkou, nikdy větší; příliš velká bota způsobuje zakopávání.</li>'
          '<li><strong>Vodoodolná verze:</strong> pro podzim a jaro, kdy se děti nevyhýbají kalužím.</li>'
          '<li><strong>Sezonní výměna:</strong> v září a v březnu přezkoušejte velikost celého šatníku najednou.</li></ul>'
          '<h2>Dámská a pánská volnočasová obuv</h2>'
          '<p>U dospělých se Geox používá hlavně jako obuv do města, do kanceláře s neformálním dress codem a na cesty. Dámské modely s označením D a pánské s označením U mají podobné spojení měkké stélky, lehké podrážky a decentního designu. Kotníková obuv, v katalogu označovaná jako kotníková, se hodí na podzim a na jaro, kdežto nízké boty se nosí od léta do pozdního podzimu. Protože se jedná o obuv na chůzi, rozhodují pohodlí, lehkost a prostor v přední části boty.</p>'
          + T(['Situace', 'Jaký typ zvolit', 'Na co si dát pozor'], [
              ['Každodenní chůze po městě', 'nízká nebo kotníková volnočasová obuv', 'dostatečně široká špička, měkká stélka'],
              ['Léto, dovolená', '<a href="/sandaly/">sandály</a>', 'pevný pásek přes patu a upínací suchý zip'],
              ['Deštivý podzim', 'vodoodolná verze s označením WR nebo podobným', 'ověřte popis konkrétního obchodu'],
              ['Zima', '<a href="/zimni-obuv/">zimní boty</a>', 'podrážka s hlubším vzorem proti smyku'],
              ['Lehčí túry', '<a href="/trekova-obuv/">trekové boty</a>', 'tužší podrážka a ochrana špičky'],
              ['Doma a po bazénu', '<a href="/pantofle-a-zabky/">pantofle a žabky</a>', 'protiskluzová podrážka']]) +
          '<h2>Sandály, zimní obuv a barefoot</h2>'
          '<p>Sandály jsou po teniskách druhou největší skupinou, což odpovídá tomu, že děti je nosí od prvních teplých dnů do září. Dobrý sandál má uzavřenou špičku nebo alespoň zesílený okraj, fixaci kolem paty a nastavitelné popruhy. Zimní obuv zahrnuje kotníkové boty se zateplením a vodoodolnou úpravou. Při výběru dbejte na to, aby dovnitř mohla pronikat jen minimální vlhkost a aby se dala boty rychle sundat a vysušit. Barefoot modely jsou naproti tomu tenké a ohebné a patří do kategorie, kterou je lepší zavádět postupně, protože chodidlo si na ně musí zvyknout.</p>'
          '<p>Z doplňků stojí za zmínku sedla, gripy a potahy v kategorii <a href="/sedla-a-gripy/">sedel a gripů</a> a oblečení pro bojové sporty v kategorii <a href="/obleceni-bojove-sporty/">kimon a oblečení</a>. Jde o menší sortiment než obuv, ale může se hodit při hledání doplňků. Pro přechodné období pomůže <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bunda</a> nebo <a href="/kabaty-a-parky/">kabát a parka</a>.</p>'
          '<h2>Velikost, šířka a střih</h2>'
          '<p>Geox bývá obecně vnímán jako obuv s vyšší stavbou a s prostorem v prstech, proto vyhovuje i nohám s širším nártem. Přesto ověřte u konkrétního obchodu, jak je velikost definována. Dětské velikosti jsou uvedené podle EU číslování, u dospělých se vyplatí ověřit délku vložky v centimetrech. Při koupi na dálku si noha na vložku položte, změřte vzdálenost od paty ke špičce nejdelšího prstu a přičtěte menší rezervu. Ponožky zkoušejte stejné, jaké budete nosit.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Většina volnočasové obuvi vydrží nejdéle, když ji střídáte a necháte po dni schnout. Vlhké boty nepokládejte na radiátor, protože se materiál zdeformuje a podrážka může povolit. Čištění zvládne kartáč a vlažná voda, u semišových částí speciální pryž. Při impregnaci vybírejte přípravek podle materiálu a nanášejte ho na čisté boty. Ve škole nechávají děti boty často v šatně, tak zkontrolujte, zda se nezačínají odlepovat okraje podešve, a včas kupte novou velikost.</p>'
          '<h2>Jak Geox porovnat s ostatními</h2>'
          '<p>V kategorii dětské a pohodlné obuvi je přirozeným srovnáním značka <a href="/znacka/ecco/">Ecco</a> a pro sportovnější pojetí také <a href="/znacka/skechers/">Skechers</a>. Zatímco Skechers sází na výraznou měkkost a pestrost, Geox působí střídměji a klidněji, často v tmavých tónech. V oblasti sandálů a trekové obuvi se hodí porovnat i <a href="/znacka/keen/">Keen</a> a <a href="/znacka/lowa/">Lowa</a>, které míří spíš na venkovní použití. Pro výkon a trénink ale Geox ve srovnávači nehledejte, v tom ho předčí specializované značky.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Dětská obuv se nejvýhodněji kupuje v období výprodejů, hlavně letní sandály po prázdninách a zimní boty na jaře. Pokud znáte velikost, na které jste právě, můžete koupit o číslo větší pro další sezonu, ale jen u bot, které děti zvládnou dlouho nosit. Sledujte starší barevné verze, které bývají zlevněné, a modely bez sezonního označení, které se vracejí. Při porovnání obchodů nehodnoťte pouze procentuální slevu, ale konečnou cenu včetně dopravy a možnosti vrácení, což je u dětské obuvi důležité kvůli výměně velikostí.</p>'
          '<h2>Rychlý rozcestník</h2>'
          '<p>Nejrychlejší cesta vede přes <a href="/tenisky/">tenisky a volnočasové boty</a>, kde použijete filtr pro koho a barvu. Pro léto vyberte <a href="/sandaly/">sandály</a>, pro déšť <a href="/holinky/">holínky</a> a pro zimu <a href="/zimni-obuv/">zimní boty</a>. Další pohodlné obuvi se věnují také značky ' + B(('ecco', 'Ecco'), ('skechers', 'Skechers'), ('keen', 'Keen')) + '.</p>',
    faq=[
        ('Co znamená písmeno U, D nebo J v názvu Geox?', 'Označuje určení obuvi. U bývá pánská, D dámská a J dětská, tedy junior. Při hledání tak snadno poznáte, kterou skupinu právě prohlížíte. Přesné značení si ale ověřte u konkrétního obchodu.'),
        ('Je Geox vhodný pro děti do školy?', 'Ano, velká část nabídky jsou dětské tenisky a volnočasové boty na každodenní nošení. Hledejte modely na suchý zip nebo gumové tkaničky, pevnější patu a ohebnou podrážku. Na podzim se hodí vodoodolná verze.'),
        ('Jak vybrat správnou velikost dětské obuvi?', 'Změřte délku chodidla a přidejte asi centimetr rezervy před prsty. Větší rezerva vede k zakopávání a špatnému držení nohy. Kontrolujte velikost každé tři až čtyři měsíce, protože děti rostou rychle.'),
        ('Jsou Geox boty vodotěsné?', 'Některé modely nesou označení vodoodolné, například WR nebo WPF, ale ne všechny. Vodoodolná úprava zvládne déšť a kaluže, ne ponoření. Vždy si přečtěte popis u konkrétního obchodu.'),
        ('Hodí se Geox na dlouhé chození?', 'Volnočasová řada je určena na denní nošení a procházky po městě. Pro vícedenní túry zvolte trekové boty, které mají tužší podrážku. U vzdálenějších tras je vhodné boty nejprve rozchodit.'),
        ('Kdy začít kupovat zimní obuv pro děti?', 'Nejlepší výběr bývá na podzim, kdy jsou skladem všechny velikosti. Pozdější nákup přináší slevy, ale hrozí, že vaše velikost bude vyprodaná. Zkoušejte s tlustší ponožkou, ve které boty nosíte.'),
        ('Jak čistit volnočasovou obuv Geox?', 'Odstraňte hrubou špínu kartáčem a otřete obuv vlhkým hadříkem s trochou jemného čisticího prostředku. Sušte při pokojové teplotě, nikdy na topení. Semišové části ošetřete speciální pryží.'),
        ('Jsou v nabídce také barefoot boty?', 'Ano, kategorie barefoot bot je zastoupena, ale menším počtem modelů. Jsou tenké a ohebné, mají širokou špičku a hodí se pro zvyk na chůzi s minimálním tlumením. Zavádějte je postupně a ne na celý den.'),
        ('Dělá Geox také oblečení?', 'V katalogu jsou lehčí jarní a podzimní bundy, kabáty, parky a čepice. Obuv ale tvoří drtivou většinu nabídky. Oblečení se vyplatí kupovat podle tabulky velikostí daného obchodu.'),
        ('Jak ušetřit při nákupu Geox?', 'Porovnejte konečnou cenu v několika obchodech a počkejte na sezonní výprodeje. U dětských bot se vyplatí kupovat starší barevné verze, které bývají zlevněné. Zohledněte dopravu a podmínky vrácení.'),
    ])

# ------------------------------------------------------------------ new-balance
NEW['new-balance'] = dict(
    title='New Balance: tenisky, běžecké a trailové boty',
    desc='New Balance na sporteka.cz: volnočasové tenisky, silniční a trailové běžecké boty, kopačky a oblečení. Jak vybrat řadu a velikost a porovnat obchody.',
    intro='<p>New Balance je v katalogu sporteky rozdělená na dvě poloviny, které se prolínají. První je obrovská nabídka volnočasových <a href="/tenisky/">tenisek</a> s číselnými názvy jako 574, 997 nebo 520, druhou jsou skutečné sportovní boty: <a href="/trailove-boty/">trailové</a> a <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, <a href="/kopacky/">kopačky</a> a <a href="/treninkova-obuv/">tréninková obuv</a>. K nim přibývají trička, mikiny, tepláky, soupravy a ponožky. Nejvíc zboží je dámského a pánského, dětské a unisex modely jsou menšina. Stránka vysvětluje, jak se orientovat v číslech a písmenech v názvech, čím se liší běžecký model od volnočasového, jak vybrat velikost a barvu a kdy hledat slevy. Vše vychází z názvů produktů, které v katalogu najdete, ne z firemní historie.</p>',
    guide='<h2>Co New Balance v katalogu nabízí</h2>'
          '<p>Většina nabídky patří volnočasové obuvi, ale na rozdíl od jiných značek tu najdete i pořádný sportovní sortiment. Největší sportovní skupinu tvoří trailové boty a za nimi silniční běžecké modely. Značka tedy slouží jak lidem, kteří chtějí pohodlné tenisky na každý den, tak běžcům a hráčům malé kopané.</p>'
          + T(['Skupina zboží', 'Co v ní najdete', 'Pro koho'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'městské modely s číselnými názvy, retro i moderní střihy', 'ženy, muži, děti'],
              ['<a href="/trailove-boty/">Trailové běžecké boty</a>', 'boty do terénu s hrubým vzorem podrážky', 'běžci v terénu'],
              ['<a href="/silnicni-bezecke-boty/">Silniční běžecké boty</a>', 'modely na asfalt a stezky', 'běžci'],
              ['<a href="/kopacky/">Kopačky</a>', 'kopačky na trávu i umělý povrch', 'fotbalisté'],
              ['<a href="/treninkova-obuv/">Fitness a tréninková obuv</a>', 'stabilnější boty do posilovny', 'cvičenci'],
              ['<a href="/mikiny/">Mikiny</a>, <a href="/teplaky/">tepláky</a>, <a href="/soupravy/">soupravy</a>', 'oblečení do volného času', 'ženy, muži'],
              ['<a href="/sportovni-ponozky/">Sportovní ponožky</a>', 'ponožky do běžecké i městské obuvi', 'všichni'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'tričko na sport i na denní nošení', 'všichni']]) +
          '<h2>Jak číst názvy modelů</h2>'
          '<p>New Balance používá u mnoha bot kódy místo slovních názvů. Písmeno na začátku obvykle odlišuje skupinu: M míří na muže, W na ženy a U označuje unisex. Číselná část označuje řadu, například 574, 997, 520 nebo 480. U běžeckých bot se přidává pojmenování podstatné pro vybavení, jako Fresh Foam, a verze s písmenem V a číslem, třeba V8 nebo V9. To je aktuální generace modelu: vyšší číslo znamená novější verzi, přičemž starší verze bývá často levnější. Dovětek GTX u běžecké obuvi ukazuje vodoodolnější verzi.</p>'
          '<h2>Volnočasové tenisky: pro koho a jak vybrat</h2>'
          '<p>Podle filtru pro koho tvoří největší skupinu dámské modely, pak pánské a dětské. Ženy sahají hlavně po světlých a pastelových barvách, muži po šedé, černé a bílé. Většina těchto bot má měkčí stélku, nízkou až střední podrážku a kombinaci semiše a sítě. Jsou určené na chůzi po městě, na dojíždění a na cesty, ne na pravidelný běh. Pokud hledáte tenisky do každodenního života, rozhodujte podle tvaru špičky, barvy a toho, jak vám sedí v oblasti nártu.</p>'
          '<ul><li><strong>Retro střih:</strong> užší siluetě a tenčí podešev, lépe ladí k džínám.</li>'
          '<li><strong>Chunky střih:</strong> silnější podrážka, výraznější vzhled, pohodlnější tlumení.</li>'
          '<li><strong>Semiš a síť:</strong> vzdušné, ale citlivé na vodu a špínu.</li>'
          '<li><strong>Kůže:</strong> lépe odolává počasí, delší životnost.</li>'
          '<li><strong>Barva:</strong> šedá a béžová se hodí ke všemu a nejméně se špiní.</li></ul>'
          '<h2>Běžecké boty: silnice a trail</h2>'
          '<p>Pro běh vyberte nejdřív povrch. Silniční boty mají hladší podrážku, lehčí konstrukci a více tlumení, protože tvrdý povrch zatěžuje klouby. Trailové boty mají hrubý vzor, pevnější špičku a silnější materiál svršku, který snese kameny a kořeny. V nabídce New Balance převažuje trail nad silnicí, takže si dá práci zvolit mezi terénním modelem a univerzálnějším. Pro začátečníka na asfaltu je lepší silniční bota s dostatečným tlumením, pro smíšený terén trailová s mírnějším vzorem.</p>'
          + T(['Kritérium', 'Silniční běh', 'Trailový běh'], [
              ['Podrážka', 'hladší, tlumení', 'hrubý vzor, záběr v blátě'],
              ['Svršek', 'lehká prodyšná síť', 'pevnější, odolný proti oděru'],
              ['Špička', 'standardní', 'zesílená proti nárazům'],
              ['Váha', 'nižší', 'o něco vyšší'],
              ['Vhodné pro', 'chodníky, stezky, běžecký pás', 'lesy, kopce, kamenitý terén']]) +
          '<p>Při výběru počítejte s tím, že noha při běhu otéká, takže běžecká obuv by měla být o půl až celé číslo větší než městská. Zkoušejte ji odpoledne a s běžeckými ponožkami z kategorie <a href="/sportovni-ponozky/">sportovních ponožek</a>. V cenovém srovnání jsou k dispozici i konkrétní stránky <a href="/new-balance-bezecke-boty/">běžeckých bot New Balance</a>, kde je výběr už zúžený.</p>'
          '<h2>Kopačky a tréninková obuv</h2>'
          '<p>Kopačky New Balance tvoří menší část nabídky a jsou dostupné na samostatné stránce <a href="/new-balance-kopacky/">kopaček New Balance</a>. Před nákupem rozhodněte, na jakém povrchu hrajete: trávník vyžaduje kolíky, umělá tráva nebo tvrdý povrch má jiný vzor. Hráči s užší nohou ocení těsnější střih, širší noha potřebuje o něco větší velikost. V kategorii <a href="/treninkova-obuv/">fitness a tréninkové obuvi</a> najdete stabilnější boty do posilovny, které mají plošší a tvrdší podrážku než běžecké modely.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Oblečení tvoří menší část, ale je dobře použitelné: <a href="/mikiny/">mikiny</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/teplaky/">tepláky</a> a soupravy do volného času. Soupravy se vyplatí, pokud chcete stejný odstín nahoře i dole. Trička vybírejte podle materiálu: bavlna je příjemná do města, syntetika rychleji schne a hodí se na sport. Kategorie <a href="/kosile/">košil</a> přináší outdoorové a turistické kousky pro chladnější dny.</p>'
          '<h2>Velikost a šířka</h2>'
          '<p>New Balance bývá u zákazníků známý tím, že u řady modelů nabízí více šířek a že střih je spíš prostornější v přední části. V katalogu se ale šířka u každého obchodu neuvádí, proto čtěte popis. Velikosti uvádějí obchody v EU, UK nebo US a pro jistotu je vhodné ověřit délku vložky. Při nákupu přes internet se držte pravidla, že zvolíte známou velikost z předchozí obuvi stejné skupiny a v případě pochybností kupujte u obchodu s bezplatným vrácením.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Semiš ošetřete kartáčem a speciální pryží, síťovinu otřete vlhkým hadříkem a boty sušte při pokojové teplotě. Běžecké boty nepoužívejte na každodenní chůzi, protože se tlumení vyčerpá rychleji než svršek. Zpravidla se vyplatí mít zvlášť boty na běh a zvlášť do města. Pokud běháte pravidelně, střídejte dva páry, aby mezitím pěna zregenerovala. Podrážku zkontrolujte po několika stovkách kilometrů, zda se nevytrácí vzor a zda nejsou boční stěny deformované.</p>'
          '<h2>Jak New Balance porovnat s ostatními</h2>'
          '<p>V běžecké oblasti je nejbližší konkurencí <a href="/znacka/asics/">Asics</a>, <a href="/znacka/brooks/">Brooks</a>, <a href="/znacka/saucony/">Saucony</a>, <a href="/znacka/hoka/">Hoka</a> a <a href="/znacka/salomon/">Salomon</a> v terénu. Ve volném času se porovnává s <a href="/znacka/nike/">Nike</a>, <a href="/znacka/adidas/">Adidas</a> a <a href="/znacka/puma/">Pumou</a>. New Balance působí klidněji a nenápadněji, v retro střizích vyniká a nabízí široký výběr šedých a béžových odstínů, což potvrzuje i přehled barev v katalogu.</p>'
          '<h2>Jak sestavit výběr krok za krokem</h2>'
          '<p>Nejdřív si ujasněte, k čemu boty potřebujete: pokud k chůzi, jděte do volnočasových tenisek, pokud k běhu, určete povrch. Potom zvolte barvu, protože šedá, černá a bílá patří k nejčastějším a nabízejí nejvíc obchodů ke srovnání. Teprve nakonec řešte konkrétní řadu a generaci. Pokud kupujete pro někoho jiného, vyberte neutrální barvu a obchod s jednoduchou výměnou velikosti. U sportovních modelů ověřte, zda je v popisu uvedeno určení pro muže, ženy nebo unisex, a zda souhlasí s vaší nohou. Dětské modely vybírejte s rezervou na délku a kontrolujte je každých několik měsíců.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Slevy se objevují u starších verzí modelů, když vyjde nová generace. Například verze V8 zlevní, jakmile se prodává V9. Běžecké boty je dobré kupovat v zimě a koncem léta, volnočasové modely při výprodejích po svátcích. Sledujte také barvy, které se už nevyrábějí. Ve srovnávači ověřte nejen cenu, ale i dostupnost velikosti, protože slevové páry často zbývají jen v extrémních velikostech.</p>'
          '<h2>Rychlý rozcestník</h2>'
          '<p>Chcete-li začít od běhu, otevřete <a href="/new-balance-bezecke-boty/">běžecké boty New Balance</a> a vyberte mezi silnicí a trailem. Pro volný čas použijte <a href="/tenisky/">tenisky</a> s filtrem pro koho a barvu. Další značky s podobným zaměřením jsou ' + B(('asics', 'Asics'), ('brooks', 'Brooks'), ('saucony', 'Saucony'), ('hoka', 'Hoka')) + '.</p>',
    faq=[
        ('Co znamenají čísla v názvech New Balance, třeba 574 nebo 997?', 'Jde o označení řady volnočasových bot, ne o velikost. Za číslem často následuje písmeno M, W nebo U, které ukazuje určení pro muže, ženy nebo unisex. Obdobně V8 či V9 u běžeckých bot znamená generaci modelu.'),
        ('Jsou volnočasové New Balance vhodné na běh?', 'Ne, městské modely nemají takové tlumení jako běžecká obuv. Na pravidelný běh zvolte kategorii silničních nebo trailových bot. Volnočasové se hodí na chůzi a na denní nošení.'),
        ('Jak poznám rozdíl mezi silniční a trailovou botou?', 'Trailová bota má výrazně hrubší vzor podrážky, zesílenou špičku a odolnější svršek. Silniční je hladší, lehčí a má lepší tlumení pro tvrdý povrch. Pro smíšené trasy zvolte trail s mírnějším vzorem.'),
        ('Je lepší koupit starší generaci modelu?', 'Často ano, hlavně když vyjde novější verze s vyšším číslem. Starší verze bývá zlevněná, a pokud vám původní střih vyhovoval, nemusíte hned přecházet. Zkontrolujte, zda je skladem vaše velikost.'),
        ('Kolik čísel větší vybírat běžeckou obuv?', 'Obvykle o půl až celé číslo větší než městskou, protože se noha při běhu zvětšuje. Zkoušejte odpoledne a v běžeckých ponožkách. Před špičkou by měl zůstat prostor na šířku palce.'),
        ('Nabízí New Balance i kopačky?', 'Ano, v katalogu je samostatná skupina kopaček. Před nákupem určete povrch, na kterém hrajete, protože kolíky a podrážka se liší. Na stránce kopaček New Balance je výběr zúžený.'),
        ('Jak čistit semišové tenisky?', 'Použijte měkký kartáč a speciální pryž na semiš, vodě se vyhněte. Na síťovinu stačí vlhký hadřík. Boty sušte při pokojové teplotě a nikdy na radiátoru.'),
        ('Jsou v nabídce dětské modely?', 'Ano, dětská nabídka je menší než dámská a pánská, ale zahrnuje volnočasové boty i sportovní obuv. U dětí dbejte na rezervu před špičkou a kontrolujte velikost pravidelně.'),
        ('Má New Balance také oblečení?', 'V katalogu jsou mikiny, fleecové mikiny, tepláky, soupravy, trička, tílka, košile a ponožky. Je to doplněk k obuvi a vyplatí se při hledání jednotného vzhledu. Střih ověřte v tabulce velikostí obchodu.'),
        ('Kdy se New Balance nejvíc zlevňuje?', 'Nejčastěji při výprodejích po svátcích a při příchodu nové generace modelu. Sledujte také starší barevné verze a ověřte dostupnost velikosti. Porovnávejte konečnou cenu včetně dopravy.'),
    ])

# ------------------------------------------------------------------ asics
NEW['asics'] = dict(
    title='Asics: běžecké, tenisové a sálové boty',
    desc='Asics na sporteka.cz: trailové a silniční běžecké boty, tenisová, sálová a volejbalová obuv, legíny a kraťasy. Jak vybrat model a porovnat obchody.',
    intro='<p>Asics je v katalogu sporteky pestřejší než většina obuvních značek, protože pokrývá víc sportů najednou. Největší skupinu tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, ale hned za nimi stojí <a href="/trailove-boty/">trailové</a> a <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, <a href="/salova-obuv/">sálová obuv</a>, <a href="/tenisova-obuv/">tenisová obuv</a> a obuv pro <a href="/padel/">padel</a> a <a href="/volejbal/">volejbal</a>. Z oblečení jsou k dispozici <a href="/leginy/">legíny</a>, <a href="/sportovni-kratasy/">kraťasy</a>, tílka a ponožky. Nabídka je skoro vyrovnaně dámská a pánská, dětských modelů je výrazně méně. Stránka vysvětluje, jak se orientovat mezi jednotlivými sporty, jak rozlišit řady jako Gel-Kayano nebo Gel-Resolution podle názvu a kdy hledat slevy. Vše vychází z produktů v katalogu a z obecně známých zásad výběru.</p>',
    guide='<h2>Co Asics v katalogu nabízí</h2>'
          '<p>Asics je ve sporteka nabídce značka obuvi pro konkrétní sporty. Vedle běhu tu najdete halové sporty, tenis a raketové sporty, což je u obuvního výrobce výjimečná šíře. Pokud tedy hledáte specializovanou obuv, začněte u sportu, nikoli u značky. Teprve pak porovnávejte modely uvnitř kategorie.</p>'
          + T(['Skupina zboží', 'Co v ní najdete', 'Pro koho'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'městské modely odvozené z běžeckých střihů', 'ženy, muži'],
              ['<a href="/trailove-boty/">Trailové běžecké boty</a>', 'terénní boty, například řady Trabuco a Gel-Sonoma', 'běžci'],
              ['<a href="/silnicni-bezecke-boty/">Silniční běžecké boty</a>', 'modely jako Gel-Kayano, GT-20 nebo Gel-Excite', 'běžci'],
              ['<a href="/salova-obuv/">Sálová a halová obuv</a>', 'obuv pro házenou, florbal a další halové sporty', 'hráči'],
              ['<a href="/tenisova-obuv/">Tenisová obuv</a>', 'boty na antuku i na všechny povrchy', 'tenisté'],
              ['<a href="/volejbal/">Volejbal</a> a <a href="/padel/">padel</a>', 'volejbalové boty a obuv na padel', 'hráči'],
              ['<a href="/leginy/">Legíny</a> a <a href="/sportovni-kratasy/">kraťasy</a>', 'běžecké a tréninkové oblečení', 'ženy, muži'],
              ['<a href="/sportovni-ponozky/">Ponožky</a> a <a href="/tilka/">tílka</a>', 'doplňky k běhu a tréninku', 'všichni']]) +
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Asics pojmenovává mnoho bot s předponou Gel a názvem řady, například Gel-Kayano, Gel-Resolution, Gel-Dedicate nebo Gel-Challenger. Tenisové řady mají v názvu často typ povrchu: Resolution se objevuje u modelů na antuku, Dedicate u modelů na všechny povrchy. U běžeckých bot jsou kódy jako GT-20, kde číslo odpovídá generaci. Volejbalové boty bývají označené Sky Elite nebo Beyond, házenkářské Gel Task. Když si zapamatujete, že název řady souvisí se sportem, snadno zúžíte výběr.</p>'
          '<h2>Běžecké boty: silnice a trail</h2>'
          '<p>V běhu rozhoduje povrch, hmotnost nohy a to, kolik opory potřebujete. Silniční boty s dostatečným tlumením zvolte na chodníky, asfaltové cesty a běžecký pás. Trailové boty mají agresivnější vzor, odolnější svršek a pevnou špičku. V nabídce Asics je trailových bot překvapivě mnoho, což zvyšuje šanci najít správnou velikost i barvu. Stabilnější řady ocení běžci, kterým se noha při došlapu zalamuje dovnitř, neutrální modely vyberou ti, kdo mají nohu vyváženou. Pokud si nejste jistí, nechte si v prodejně ukázat běh na pásu nebo požádejte o rozbor došlapu.</p>'
          + T(['Typ běžce', 'Co hledat', 'Příklad v nabídce'], [
              ['Začátečník na asfaltu', 'tlumení a stabilita', 'silniční modely s tlumicí podešví'],
              ['Pronace dovnitř', 'oporu uvnitř klenby', 'řada GT'],
              ['Neutrální došlap, delší trasy', 'měkké tlumení', 'řada Gel-Kayano nebo Gel-Excite'],
              ['Les a kopce', 'hrubý vzor a pevná špička', 'Trabuco, Gel-Sonoma'],
              ['Smíšené trasy', 'mírnější vzor', 'univerzální trailové modely']]) +
          '<p>Pro rychlý přehled slouží i stránka <a href="/bezecke-boty-asics/">běžecké boty Asics</a>, kde je výběr zúžený na běžeckou obuv. Při koupi počítejte s tím, že noha při běhu otéká, proto vybírejte o půl až celé číslo větší než městské boty.</p>'
          '<h2>Tenis a padel</h2>'
          '<p>V tenisové obuvi se rozlišuje podle povrchu. Antuka vyžaduje obuv, která drží a umožňuje kontrolované klouzání, tvrdý povrch klade důraz na odolnost podrážky a boční stabilitu. Modely na všechny povrchy představují kompromis, hodí se rekreačním hráčům, kteří střídají kurty. V kategorii <a href="/tenisova-obuv/">tenisové obuvi</a> najdete oboje a dámské i pánské velikosti. Padel má vlastní kategorii <a href="/padel/">padel</a>, protože povrch s pískem a skleněné stěny vyžadují jiný vzor podrážky než tenis.</p>'
          '<ul><li><strong>Antuka:</strong> vzor ve tvaru rybí kosti, který se nezanáší.</li>'
          '<li><strong>Tvrdý povrch:</strong> odolná podešev a podpora boků.</li>'
          '<li><strong>Všechny povrchy:</strong> univerzální vzor, ale kompromis ve všem.</li>'
          '<li><strong>Padel:</strong> zesílené boční části a záběr v písku.</li>'
          '<li><strong>Šířka:</strong> hráči s širší nohou volí model s prostornější špičkou.</li></ul>'
          '<h2>Sálová obuv, házená a volejbal</h2>'
          '<p>V hale se hraje na parketách nebo na speciální podlaze, proto sálová obuv nesmí zanechávat stopy a musí dobře držet. Podrážka je obvykle z hladké nebo jemně strukturované pryže, kterou je vhodné čistit před zápasem. Při výběru zvažujte, jaký sport hrajete: házená vyžaduje stabilitu a ochranu kotníku, volejbal vertikální odraz a tlumení dopadu, florbal nízký profil. V kategorii <a href="/salova-obuv/">sálové obuvi</a> jsou tyto modely společně, ve <a href="/volejbal/">volejbalu</a> najdete užší výběr.</p>'
          '<h2>Oblečení: legíny, kraťasy, tílka</h2>'
          '<p>Běžecké legíny a kraťasy z řady Core mají střih na pohyb a rychle schnou. Legíny se hodí na chladnější dny a do posilovny, kraťasy na rychlejší běh nebo do hor v létě. Sportovní tílka nabízí maximální vzdušnost, doplněná ponožkami z <a href="/sportovni-ponozky/">kategorie ponožek</a> zajistí pohodlí při dlouhém tréninku. Při výběru legín sledujte, zda je pás dostatečně široký a nesklouzává, a zkoušejte je při dřepu, aby látka nebyla průsvitná.</p>'
          '<h2>Pro koho: pohlaví a děti</h2>'
          '<p>Nabídka je vyrovnaná mezi dámskými a pánskými modely, což je u značky se sportovním zaměřením poměrně vzácné. Dětské velikosti jsou omezené a jde hlavně o sálovou a tenisovou obuv, takže mladí hráči mají k dispozici jen vybrané modely. Pokud vybíráte pro dospívajícího, který už má dospělou nohu, zvažujte dospělou velikost a unisex střih.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Asics bývá vnímán jako značka s konzervativním, spíše užším střihem v oblasti paty a středu chodidla. Šířka přední části se liší podle modelu, proto se vyplatí zkontrolovat popis. Změřte chodidlo, přidejte rezervu na prsty a při pochybnostech zvolte větší číslo. Tenisové a sálové boty mají sedět těsněji než běžecké, ale nesmí tlačit na prsty při brzdění.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Sportovní obuv sušte při pokojové teplotě a nikdy v pračce. Po zápasu vyndejte vložky, ať boty vyschnou. U halové obuvi čistěte podrážku vlhkým hadříkem, aby se neztrácel záběr. Běžecké boty vydrží zhruba do okamžiku, kdy pěna ztratí odezvu a vzor je opotřebený. Střídání dvou párů prodlužuje životnost obou, protože pěna má čas se vrátit do tvaru.</p>'
          '<h2>Jak Asics porovnat s konkurencí</h2>'
          '<p>V běhu se Asics srovnává s <a href="/znacka/new-balance/">New Balance</a>, <a href="/znacka/brooks/">Brooks</a>, <a href="/znacka/saucony/">Saucony</a>, <a href="/znacka/hoka/">Hoka</a> a <a href="/znacka/mizuno/">Mizuno</a>. Ve volejbalu a v hale je přirozeným soupeřem <a href="/znacka/mizuno/">Mizuno</a>, v tenisu <a href="/znacka/adidas/">Adidas</a> a <a href="/znacka/nike/">Nike</a>. Asics se v nabídce odlišuje právě šíří: jedna značka pokryje běh, tenis, volejbal i padel.</p>'
          '<h2>Jak sestavit výběr podle sportu</h2>'
          '<p>Postupujte od sportu k obuvi. Nejdřív zvolte kategorii, například trail, antuku nebo halu, pak pohlaví a velikost a teprve potom barvu a konkrétní řadu. U běžeckých bot ověřte generaci modelu v názvu, protože starší verze bývá výhodnější. U tenisu a haly dbejte na to, aby bota patřila na povrch, na kterém opravdu hrajete, a ne jen k podobnému sportu. Oblečení vybírejte až po obuvi, protože legíny a kraťasy z kategorií legín a kraťasů lze snadno sladit s jakoukoli barvou bot. Pokud kupujete pro dospívajícího, vyberte pevnější model s rezervou a ověřte možnost výměny.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Slevy se objevují hlavně u starších generací běžeckých bot, když vychází nový ročník. Halová a tenisová obuv bývá zlevněná po skončení sezony, tedy na jaře a v létě. Ve srovnávači porovnávejte konečnou cenu a dostupnost velikosti, protože slevové modely zůstávají často jen v extrémních velikostech. Pokud potřebujete boty na konkrétní turnaj, nečekejte na slevu, ale vyberte si předem a ověřte možnost vrácení.</p>'
          '<h2>Rychlý rozcestník</h2>'
          '<p>Chcete-li začít u běhu, otevřete <a href="/bezecke-boty-asics/">běžecké boty Asics</a> nebo <a href="/silnicni-bezecke-boty/">silniční</a> a <a href="/trailove-boty/">trailové boty</a>. Pro tenis a padel použijte <a href="/tenisova-obuv/">tenisovou obuv</a> a <a href="/padel/">padel</a>. Podobné sportovní zaměření mají i značky ' + B(('mizuno', 'Mizuno'), ('brooks', 'Brooks'), ('saucony', 'Saucony'), ('new-balance', 'New Balance')) + '.</p>',
    faq=[
        ('Co znamená Gel v názvech bot Asics?', 'Gel je součást názvu mnoha řad, například Gel-Kayano nebo Gel-Resolution. Přesný popis technologie najdete u konkrétního obchodu. Pro výběr je důležitější část za ním, která naznačuje sport a určení.'),
        ('Jak vybrat tenisovou obuv podle povrchu?', 'Na antuku zvolte model určený pro antuku, který nezanáší vzor. Na tvrdé kurty hledejte odolnou podešev a boční stabilitu. Modely na všechny povrchy jsou kompromisem pro rekreační hráče.'),
        ('Jaký je rozdíl mezi silniční a trailovou běžeckou botou?', 'Trailová bota má hrubší vzor, zesílenou špičku a odolnější svršek pro terén. Silniční je hladší a lehčí s tlumením pro tvrdý povrch. Na smíšené trasy volte trail s mírnějším vzorem.'),
        ('Hodí se Asics i na volejbal a házenou?', 'Ano, v katalogu najdete sálovou obuv, volejbalové boty a házenkářské modely. Dívejte se na stabilitu, tlumení a hladkou podrážku, která nezanechává stopy na podlaze.'),
        ('Pro koho je řada GT?', 'Řada s označením GT se v katalogu objevuje u silničních bot a obvykle míří na běžce, kteří potřebují stabilnější došlap. Před koupí je vhodné nechat si ověřit způsob došlapu a přečíst si popis obchodu.'),
        ('Jak velkou velikost vybírat pro běh?', 'Obvykle o půl až celé číslo větší než městskou obuv, protože noha při běhu otéká. Zkoušejte odpoledne a ve sportovních ponožkách. Před špičkou má zůstat prostor.'),
        ('Má Asics také oblečení?', 'Ano, najdete legíny, kraťasy, tílka, kšiltovky a ponožky. Oblečení doplňuje obuv a hodí se na běh i trénink. Zkontrolujte tabulku velikostí a materiál podle ročního období.'),
        ('Jak čistit sálovou obuv?', 'Podrážku otřete vlhkým hadříkem, aby se neztrácel záběr, a nenoste ji venku. Po zápase vyndejte vložky a nechte boty vyschnout při pokojové teplotě. Nikdy je nesušte na topení.'),
        ('Jsou v nabídce dětské velikosti?', 'Ano, ale v menším počtu než dámské a pánské modely. Jde hlavně o halovou a tenisovou obuv. Dospívající s dospělou nohou mohou zvolit unisex nebo pánskou velikost.'),
        ('Kdy se nejvíc vyplatí hledat slevu?', 'U běžecké obuvi při příchodu nové generace modelu, u halové a tenisové po sezoně. Porovnejte konečnou cenu včetně dopravy a ověřte dostupnost své velikosti.'),
    ])
