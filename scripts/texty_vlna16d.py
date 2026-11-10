"""sporteka.cz — wave 16d (4. 11. 2026): long texts (>= 1650 words) for bazeny, merino-mikiny, snorchlovani, joga-a-podlozky.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bazeny
NEW['bazeny'] = dict(long=True,
    title='Bazény a nafukovadla: zahradní i dětské | Sporteka',
    desc='Nadzemní bazény, nafukovací bazénky a vodní hračky od českých obchodů. Jak vybrat velikost, konstrukci, filtraci a čím bazén udržet čistý.',
    intro='<p>Pod hlavičkou <strong>bazénů a nafukovadel</strong> se skrývá všechno od mělkého bazénku pro batole po nadzemní nádrž, do které se vejde celá rodina. Liší se konstrukcí, tvarem, objemem i tím, kolik práce vyžadují po sezoně. Rychlý výběr podle fotky proto často skončí špatně: bazén je buď příliš velký na zahradu, nebo příliš křehký na to, jak ho děti používají.</p>'
          '<p>Na Sportece vidíte nabídky obchodů vedle sebe a můžete porovnat rozměry, typ stěny i příslušenství, které je v balení. Další vodní vybavení najdete v nadřazené skupině <a href="/vodni-sporty/">vodní sporty</a>, ke koupání patří <a href="/plavky/">plavky</a>, <a href="/detske-plavky/">dětské plavky</a> a <a href="/plazove-doplnky/">plážové doplňky</a>. Tahle stránka vás provede výběrem krok za krokem.</p>',
    guide='<h2>Jaké druhy bazénů existují</h2>'
          '<p>Hlavní rozdíl je v tom, jak bazén drží tvar. Od toho se odvíjí odolnost, doba stavby a nároky na místo. Přehled nejběžnějších konstrukcí:</p>'
          + T(['Konstrukce', 'Jak drží tvar', 'Pro koho se hodí'], [
              ['Nafukovací bazének', 'vzduch v horním kruhu nebo ve stěnách', 'malé děti, balkon, terasa, krátké použití'],
              ['Bazén s nafukovacím límcem', 'vzduchový prstenec drží horní okraj, voda zbytek', 'rodiny, které chtějí rychlou stavbu bez nářadí'],
              ['Bazén s ocelovým rámem', 'trubky a spoje pod fólií, voda tlačí na stěnu', 'zahrady s ročním použitím a delší životností'],
              ['Bazén s pevnou stěnou', 'ocelový plech, plast nebo kompozit', 'trvalé umístění, větší objemy, dlouhá sezona'],
              ['Kruhové a oválné bazény', 'rám se stejnými rozpěrami po obvodu', 'plavání, hra ve více lidech'],
              ['Obdélníkové bazény', 'rohové spoje ve vyšším napětí', 'užší pozemky, využití celé délky']]) +
          '<p>Nafukovací varianty jsou nejlevnější na pořízení i skladování, ale nemají dlouhou životnost a nesnášejí ostré předměty. Rámové bazény vydrží roky, vyžadují však rovný podklad a po sezoně pečlivé uložení. Pevné stěny jsou už blíž k trvalé stavbě a hodí se tam, kde bazén nechcete každý rok rozebírat.</p>'
          '<h2>Rozměr a objem: kolik bazénu opravdu potřebujete</h2>'
          '<p>Začněte tím, co na zahradě skutečně zbyde, ne tím, co si přejete. Kromě samotného průměru počítejte s odstupem kolem dokola, aby šlo obejít filtraci, žebřík a kontrolovat stěny. Hloubka rozhoduje o tom, kdo bude bazén používat. Mělké bazénky do cca třiceti centimetrů jsou pro batolata, hloubka kolem stovky centimetrů již slouží plavání a dětem do určitého věku se hodí jen pod dohledem dospělého. Objem vody pak určuje výkon filtrace a spotřebu chemie.</p>'
          '<ul><li><strong>Průměr nebo délka</strong> se v katalozích uvádí u horního okraje. Skutečná plocha dna je menší, protože stěny se mírně svažují.</li>'
          '<li><strong>Výška stěny</strong> se udává pro plný stav. Do bazénu nikdy nenalévejte po okraj, nechte rezervu pro vlnění a vytěsněnou vodu.</li>'
          '<li><strong>Objem</strong> uvádí výrobce při určité hladině. Je to orientační údaj, při menším naplnění klesá.</li>'
          '<li><strong>Nosnost a počet lidí</strong> nejsou normované hodnoty. Berte je jako doporučení a počítejte s tím, že děti často skáčou.</li></ul>'
          '<h2>Příprava podloží</h2>'
          '<p>Většina předčasných poruch začíná pod bazénem. Plocha musí být vodorovná, zbavená kamení, kořenů a ostrých hran. Z trávníku odeberte drn, podklad zhutněte a přidejte vrstvu písku nebo vhodnou podložku. Pod rámové bazény se hodí tvrdší dlaždice nebo desky, které rozloží tlak nohou. Nestavějte bazén pod stromy, protože listí, pyl a trus ptáků zhoršují kvalitu vody. Také se vyhněte místům s podzemním vedením a svahům, kde by se po dešti mohla voda hromadit. Správné umístění vám ušetří víc práce než jakékoli příslušenství.</p>'
          '<h2>Filtrace, čerpadla a údržba vody</h2>'
          '<p>Voda stojící v bazénu bez oběhu se během několika dní zakalí a zezelená. Základ je filtrační zařízení, a to je třeba vybrat podle objemu. Kartušové filtry jsou nejjednodušší, vyměňuje se vložka, písková filtrace čistí lépe a hodí se pro větší nádrže. U drobných bazénků se obejdete bez filtru, ale vodu pak vypouštíte po každém použití.</p>'
          '<ul><li><strong>Výkon čerpadla</strong> by měl za několik hodin protočit celý objem. Menší čerpadlo musí běžet déle, aby protočilo celý objem; podcenění výkonu vede k zakalené vodě.</li>'
          '<li><strong>Chemie</strong> zahrnuje hodnotu pH, dezinfekci a občas přípravek proti řasám. Dávkování řiďte podle návodu a nikdy nemíchejte různé přípravky přímo v nádobě.</li>'
          '<li><strong>Čisticí pomůcky</strong> jako síťka, ruční vysavač nebo automatický robot zkrátí denní údržbu na pár minut. Robotické vysavače bývají u větších bazénů pohodlným řešením.</li>'
          '<li><strong>Krycí plachta</strong> chrání před nečistotami, snižuje odpar a zpomaluje ochlazování vody.</li></ul>'
          '<h2>Vybavení a příslušenství</h2>'
          '<p>K bazénu patří víc, než se zdá. Žebřík nebo schůdky, podlahová a stěnová podložka, plachta, vzduchová pumpa na nafukovací díly, záplatová sada a teploměr. U menších bazénků se vyplatí ohřev na slunci, například tmavá solární plachta, protože zahřátá voda se používá častěji. Pokud pořizujete bazén pro děti, zkontrolujte, zda jde žebřík zajistit nebo odstranit, aby se k vodě nedostaly bez dozoru.</p>'
          '<h2>Pro koho je který typ</h2>'
          '<p>Rodiny s malými dětmi nejčastěji sáhnou po mělkých nafukovacích bazéncích, které se dají vyprázdnit a uschovat. Aktivní plavci a zahrady s dlouhou sezonou by měli zvážit rámový bazén s filtrací, neboť klidně vydrží několik let. Dospívající a skupiny ocení větší průměr a pevnější stěnu. Menší byty a balkony vyřeší bazén o malém objemu, ale zkontrolujte nosnost podlahy, protože voda je těžká: každý litr váží přibližně kilogram.</p>'
          '<h2>Nafukovadla a vodní hračky</h2>'
          '<p>Kategorie zahrnuje i nafukovací kruhy, lehátka, matrace a míče. Při výběru sledujte materiál, počet vzduchových komor a ventily. Víc komor znamená bezpečnější plavidlo: když jedna povolí, ostatní zůstanou nafouknuté. Plavecké pomůcky pro děti najdete ve skupině <a href="/plavecke-pomucky/">plavecké pomůcky</a>, pro kolektivní zábavu se hodí i <a href="/paddleboardy/">paddleboardy</a> a pro slunění <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>. Nafukovadla nejsou záchranné prostředky. Dítě v nich nikdy nenechávejte bez dozoru.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mezi zahradními bazény mají ' + B(('intex', 'Intex'), ('bestway', 'Bestway'), ('marimex', 'Marimex'), ('avenli', 'Avenli')) + '. Jednotlivé řady se liší stěnou, rámem a tím, jaké příslušenství je součástí balení. Číst je třeba popis obsahu balení, ne jen fotku. Pro doplňkové vybavení na koupání se podívejte také do <a href="/plazove-doplnky/">plážových doplňků</a> a <a href="/neopreny/">neoprenů</a> na delší pobyt ve vodě.</p>'
          '<h2>Bezpečnost u bazénu</h2>'
          '<p>Voda je riziková i v mělkém bazénku. Malé dítě se může utopit v pár centimetrech vody. Nikdy ho nenechávejte bez dospělého, který se plně věnuje dohledu, a ne mobilu. Žebřík po koupání sundejte, bazén zakryjte a zvažte oplocení nebo alespoň bránu k zahradě. Čerpadlo napájejte přes proudový chránič (RCD), zapojení svěřte elektrikáři a v dosahu vody nepoužívejte prodlužovací kabely. Chemii skladujte mimo děti a nikdy ji nemíchejte mezi sebou. Jedna nezabezpečená minuta u bazénu nestojí za žádnou úsporu času.</p>'
          '<h2>Uložení po sezoně</h2>'
          '<p>Před zimou bazén vypusťte a vyčistěte. Fólii nechte důkladně oschnout, jinak se tvoří plíseň. Lehce ji poprašte talkem, přeložte bez ostrých záhybů a uložte v suchu a v teple nad bodem mrazu. Rám rozeberte, označte součásti a uložte v kufru či krabici. Filtr i čerpadlo propláchněte a vyprázdněte, protože zbytek vody při mrazu poškodí těleso. Po takovém ošetření bazén bez potíží přečká zimu a další sezonu ho postavíte za hodinu.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit bazén podle průměru bez kontroly volného místa kolem něj.</li>'
          '<li>Podcenit filtraci a pak řešit zelenou vodu.</li>'
          '<li>Stavět na nerovné ploše nebo přímo na kamenitém podkladu.</li>'
          '<li>Nepočítat s potřebou vody: napuštění větších bazénů trvá hodiny a zatíží zahradní kohout.</li>'
          '<li>Spoléhat se na nafukovací kruh jako na bezpečnostní pomůcku.</li>'
          '<li>Zapomenout na uložení: velký rámový bazén se bez místa ve sklepě či garáži stává problémem.</li></ul>',
    faq=[
        ('Jaký bazén je nejlepší pro malé děti?', 'Pro batolata a předškoláky se hodí mělký nafukovací bazének se stěnou, kterou dítě snadno překročí. Voda se dá po koupání vylít a plocha se rychle ohřeje na slunci. Dohled dospělého je nutný při každém použití.'),
        ('Jak velký bazén se vejde na zahradu?', 'Změřte plochu a odečtěte pruh kolem dokola, aby šlo bazén obejít, upravit žebřík a zkontrolovat stěny. K tomu přičtěte místo pro čerpadlo a odtok. Teprve zbytek je vaše použitelná plocha.'),
        ('Je lepší rámový bazén, nebo nafukovací?', 'Rámový bazén vydrží více sezon a lépe snáší zátěž, ale potřebuje delší stavbu a pevný podklad. Nafukovací je rychlejší a levnější na skladování, zato je citlivější na poškození a při větším objemu méně stabilní.'),
        ('Jak často vyměnit vodu v bazénu?', 'Záleží na filtraci a používání. Se správně dimenzovanou filtrací a chemií vydrží voda celou sezonu. U malých bazénků bez filtru ji vypouštíte po každém koupání nebo alespoň každé dva dny.'),
        ('Potřebuji k bazénu filtraci?', 'Pro bazény s větším objemem ano, bez oběhu vody se rychle množí řasy. U mělkých dětských bazénků lze filtraci vynechat, pak ale vodu často měňte a bazén zakrývejte plachtou.'),
        ('Na jaký podklad se bazén staví?', 'Na rovnou, zhutněnou plochu bez kamenů a kořenů. Pomáhá vrstva písku a podložka pod dno. Rámový bazén tlačí nohama do podloží, proto se pod ně dávají desky, které rozloží tlak.'),
        ('Jak ošetřit vodu, aby nebyla zelená?', 'Udržujte funkční filtraci, hlídejte pH a pravidelně dávkujte dezinfekci podle návodu. Plachta po koupání a odstraňování listí zabraňují zanášení. Zelená voda je znamení, že rovnováha chybí.'),
        ('Dá se bazén na zimu nechat venku?', 'Většina zahradních bazénů je určena na sezonu. Vypusťte vodu, vyčistěte a uložte fólii i rám do suchého, nezamrzajícího prostoru. Pevné trvalé nádrže mají vlastní pokyny výrobce k přezimování.'),
        ('Čím se opravuje malý otvor ve fólii?', 'Záplatovou sadou, která se obvykle dodává v balení. Místo se očistí, osuší a přelepí záplatou přes celou dírku. U nafukovacích dílů se únik najde pomocí mýdlové vody, kde se tvoří bublinky.'),
        ('Jsou nafukovací pomůcky bezpečné?', 'Nafukovadla slouží ke hře, ne k záchraně. Dítě se z nich může snadno vyklouznout nebo sjet pod hladinu. Vybírejte modely s více komorami a nikdy nenechávejte děti u vody bez dohledu.'),
    ])

# ------------------------------------------------------------------ merino-mikiny
NEW['merino-mikiny'] = dict(long=True,
    title='Merino mikiny a svetry: výběr, gramáž | Sporteka',
    desc='Merino mikiny, svetry a vrstvy na hory i město. Jak vybrat gramáž, střih a zip, jak merino prát a které značky v nabídce najdete.',
    intro='<p><strong>Merino mikiny a svetry</strong> jsou střední vrstva z vlny merino ovce: hřejí i vlhké, nezapáchají tak rychle jako syntetika a vypadají dost dobře i mimo hory. Na výběr jsou rolláky, pulovry s dlouhým zipem, kapuce, tenké svetry pod košili nebo hrubší pleteniny na zimní túry. Každý typ pracuje jinak a nemá smysl kupovat dva podobné kousky.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů vedle sebe. Základní vrstvu najdete mezi <a href="/merino-tricka/">merino tričky</a> a <a href="/merino-pradlo/">merino prádlem</a>, doplňky v <a href="/merino-ponozky/">merino ponožkách</a> a <a href="/merino-doplnky/">merino doplňcích</a>. Nadřazená skupina <a href="/merino/">merino</a> shrnuje celý sortiment.</p>',
    guide='<h2>Co umí merino ve střední vrstvě</h2>'
          '<p>Vlákna merino ovce jsou jemná a krátká, proto vlna nekouše tolik jako běžná. Vlákno pojme vlhkost, aniž by se na dotek zdálo mokré, a pletenina z něj zadržuje vzduch. Z toho plyne, že svetr hřeje i při potu a po zastavení nevychladne okamžitě. Další výhoda je přirozená odolnost vůči zápachu, takže mikinu na vícedenní túře nemusíte prát po každém dni. Nevýhody existují taky: čisté merino je citlivější na obrušování a háčkování o suché zipy, trhá se snadněji než syntetika a schne pomaleji.</p>'
          '<h2>Typy a kdy se hodí</h2>'
          + T(['Typ', 'Charakter', 'Nejlepší použití'], [
              ['Tenký svetr nebo pulovr', 'jemná pletenina, nižší gramáž', 'pod bundu, do kanceláře, jarní a podzimní dny'],
              ['Mikina s dlouhým zipem', 'snadné větrání při stoupání', 'turistika, běžky, rychlé střídání teploty'],
              ['Rolák nebo s krátkým zipem', 'zakrývá krk a hřeje při pohybu', 'zimní túry, skialpinismus, cesta lanovkou'],
              ['Mikina s kapucí', 'chrání hlavu při vyšší aktivitě', 'městský styl, chladné večery, tábořiště'],
              ['Hrubší pletený svetr', 'silnější vlákno, zřetelná struktura', 'zimní procházky a chaty, ne pro intenzivní výkon'],
              ['Merino s příměsí syntetiky', 'vyšší pevnost a rychlejší schnutí', 'častá zátěž, batoh, horolezectví']]) +
          '<h2>Gramáž a tloušťka</h2>'
          '<p>Gramáž se udává v gramech na metr čtvereční a je důležitým vodítkem. Nižší hodnoty znamenají tenčí a vzdušnější vrstvu na pohyb a mírné počasí, střední jsou univerzální, vyšší patří k pravé zimě nebo k pomalému tempu. Dejte si pozor, že čísla různých výrobců nejsou přesně srovnatelná, protože záleží i na úpletu. Berte to jako orientační rozlišení. Dobrá zkouška: pokud zvolíte vrstvu, ve které je vám lehce chladno na startu, během chůze se zahřejete a nebudete se zpocovat.</p>'
          '<h2>Jak merino vrstvit</h2>'
          '<p>Merino mikina je typická střední vrstva. Zespodu nosíte tričko nebo spodní prádlo, třeba z kategorie <a href="/termopradlo/">termoprádlo</a>, a navrch bundu proti větru či dešti. Při pohybu pomáhá větrat zip a vyhrnuté rukávy. Pokud je velká zima, přidejte další tenkou vrstvu, ne jednu extra tlustou: více vrstev udrží teplo spolehlivěji a umožní lepší regulaci. Při vysoké aktivitě, například při běhu nebo skialpu, stačí lehčí merino, protože tělo vytváří dost tepla. Při stání a pomalém tempu je naopak lepší vyšší gramáž. Alternativou pro náročné zásahy jsou <a href="/fleecove-mikiny/">fleecové mikiny</a> a <a href="/funkcni-mikiny/">funkční mikiny</a>, které lépe snesou otěr.</p>'
          '<h2>Střih, velikost a materiál</h2>'
          '<p>Pro funkci je důležité, aby vrstva k tělu přiléhala, ale nestahovala. Příliš volný svetr vytváří vzduchové kapsy a hůře odvádí vlhkost, příliš těsný omezuje pohyb. Zkontrolujte délku rukávů při zvednutých pažích a zadní délku pod batohem. Sledujte tabulku velikostí od konkrétního výrobce. Škála je mezi značkami odlišná a rozdíl v rozměru bývá znát. Do úvahy přicházejí i příměsi: nylon vyztužuje, elastan dodává pružnost, tencel zjemňuje dotek. Čisté merino je nejměkčí, ale nejméně odolné.</p>'
          '<ul><li><strong>Zip</strong> by měl mít chránič brady, aby neškrábal.</li>'
          '<li><strong>Švy</strong> na ramenou mají být ploché, jinak vás bude tlačit popruh batohu.</li>'
          '<li><strong>Manžety</strong> s palcovou dírkou chrání zápěstí a drží rukáv na místě.</li>'
          '<li><strong>Kapsy</strong> se vyplatí zipové, aby se nic neztratilo při pohybu.</li></ul>'
          '<h2>Pro koho které merino</h2>'
          '<p>Turisté a běžkaři ocení mikinu s dlouhým zipem, která umožní rychle regulovat teplotu. Cestovatelé s malým zavazadlem vezmou jeden svetr, který po večerním nošení vyvětrají, místo tří bavlněných. Lidé ve městě vybírají tenký pulovr pod kabát a rolák do chladných dní. Dětské velikosti jsou, ale výběr je užší; dítě rychle roste, proto vybírejte rozumně. Alergici na vlnu by měli nejdřív zkusit krátkodobé nošení, protože citlivost na vlnu je individuální a jemné merino ji nemusí vyloučit.</p>'
          '<h2>Péče o merino</h2>'
          '<p>Správná péče určuje, jak dlouho vám svetr vydrží. Většina výrobců doporučuje jemné praní, nízkou teplotu a prostředek určený na vlnu. Neprat s běžným pracím práškem s enzymy ani s aviváží, která narušuje vlákno. Svetr po vyprání netočte, jen jemně vymačkejte do ručníku a sušte vleže v plochém tvaru, aby se neprotáhl. Neumisťujte ho na radiátor ani na přímé slunce. Většinu mikin není třeba prát tak často, stačí vyvětrat. Skvrny ošetřete lokálně. Pokud se tvoří žmolky, odstraňte je opatrně hřebenem na pleteniny nebo žmolkovačem, ale nestříhejte je nůžkami do vlákna. Při skladování používejte látkový obal a přidejte levanduli či cedrové dřevo proti moli, před uložením však mikinu vždy vyperte.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V této kategorii zastupuje největší počet nabídek ' + B(('lasting', 'Lasting'), ('icebreaker', 'Icebreaker'), ('smartwool', 'Smartwool'), ('sensor', 'Sensor'), ('kama', 'Kama'), ('progress', 'Progress'), ('ulvang', 'Ulvang'), ('lundhags', 'Lundhags'), ('husky', 'Husky'), ('helly-hansen', 'Helly Hansen'), ('mons-royale', 'Mons Royale')) + '. Rozdíly jsou v kvalitě pleteniny, v tom, zda jde o čisté merino nebo směs, a v zaměření na sport či každodenní nošení. Při porovnání hledejte složení v procentech a gramáž, ne jen název kolekce.</p>'
          '<h2>Co dalšího se hodí k merino mikině</h2>'
          '<p>Na zimu skvěle fungují merino ponožky a čepice, a pokud sháníte výbavu na celé tělo, procházejte <a href="/outdoor/">outdoor</a> a <a href="/mikiny/">mikiny</a> obecně. Pro náročnější podmínky vám pomohou <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> a pro lyžaře <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Kupovat mikinu s vysokou gramáží na pohyb a pak se v ní potit.</li>'
          '<li>Prát merino na vysokou teplotu nebo v sušičce, kde se srazí.</li>'
          '<li>Volit příliš volnou velikost a čekat, že bude odvádět pot.</li>'
          '<li>Nosit čisté merino pod batohem na dlouhé túry bez příměsi, vlákno se obrušuje.</li>'
          '<li>Podceňovat zip a krk: špatně řešený límec vyloučí jinak dobrý svetr.</li>'
          '<li>Ukládat nevyprané: moli lákají zbytky potu a kožního mazu.</li></ul>',
    faq=[
        ('Jaká gramáž merino mikiny je nejuniverzálnější?', 'Střední gramáž zvládne většinu situací od podzimu do jara. Na intenzivní pohyb volte nižší, na pomalé tempo a velkou zimu vyšší. Přesné hodnoty se mezi výrobci liší, takže se řiďte popisem určení.'),
        ('Škrábe merino na kůži?', 'Jemné vlákno merino ovce je oproti běžné vlně výrazně příjemnější, ale citlivost je individuální. Tenčí svetry a spodní vrstvy působí měkčeji. Pokud vlnu nemáte rádi, zkuste nejprve tenčí kus.'),
        ('Dá se merino mikina prát v pračce?', 'Ano, pokud to povoluje štítek. Používejte program na vlnu, nízkou teplotu a jemný prostředek bez enzymů a aviváže. Odstřeďování omezte a sušte vleže, nikoli v sušičce.'),
        ('Jak odstranit žmolky z merino svetru?', 'Jemně je odstraňte hřebenem na pleteniny nebo žmolkovačem. Nestříhejte je nůžkami u vlákna, mohli byste udělat otvor. Žmolky se tvoří hlavně v místech otěru, třeba pod popruhy batohu.'),
        ('Čím se liší merino od syntetického fleecu?', 'Merino hřeje i vlhké a nezapáchá tak rychle, ale hůře snáší otěr a déle schne. Fleece je pevnější a schne rychleji, zato po několika dnech nošení zapáchá. Volba závisí na tom, na co ho budete používat.'),
        ('Je lepší mikina na zip, nebo bez zipu?', 'Zip usnadňuje větrání a hodí se při měnící se zátěži, tedy při chůzi do kopce. Pulovr bez zipu je lehčí a méně objemný, hodí se na klidnější aktivity a městské nošení.'),
        ('Jak velkou velikost vybrat?', 'Svetr má přiléhat, aniž by tlačil. Zkontrolujte délku rukávů a zad při předklonu a řiďte se tabulkou velikostí daného výrobce, protože mezi značkami se rozměry liší.'),
        ('Zničí merino mol?', 'Vlna je pro moly potrava, zejména když je znečištěná potem. Před uložením mikinu vyperte, uložte do uzavřeného obalu a přidejte levanduli či cedr. Pravidelně obsah skříně vyvětrejte.'),
        ('Mohu merino nosit celoročně?', 'Tenčí pleteniny se hodí i na chladnější letní večery, hlavně v horách. Hrubé svetry jsou ale určené pro zimní měsíce. Pro různé sezóny proto bývá praktické mít dvě různé gramáže.'),
        ('Jak dlouho merino mikina vydrží?', 'Při šetrné péči mnoho let. Životnost snižuje hrubé praní, otěr popruhů a skladování bez ochrany před moly. Příměs syntetiky zvyšuje odolnost, ovšem na úkor části přirozených vlastností.'),
    ])

# ------------------------------------------------------------------ snorchlovani
NEW['snorchlovani'] = dict(long=True,
    title='Šnorchlování a potápění: maska, šnorchl, ploutve | Sporteka',
    desc='Masky, šnorchly, ploutve a potápěčská výbava od českých obchodů. Jak vybrat velikost, typ ploutví, ventil a péči o vybavení před cestou k moři.',
    intro='<p>Kategorie <strong>šnorchlování a potápění</strong> pokrývá velmi rozsáhlý sortiment, od jednoduchých dětských sad k moři až po vybavení pro přístrojové potápění. Pro většinu lidí je nejdůležitější trojice maska, šnorchl a ploutve. Když jedna z nich nesedí, dovolená u moře se změní v trápení: netěsní maska, tlačí pata nebo vám stále teče voda do dýchací trubice.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů vedle sebe a vyberete podle velikosti i určení. Další vodní vybavení najdete ve skupině <a href="/vodni-sporty/">vodní sporty</a>, pro delší pobyt ve vodě <a href="/neopreny/">neopreny</a>, na plavání <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-pomucky/">plavecké pomůcky</a>. Tento průvodce vás provede výběrem krok za krokem.</p>',
    guide='<h2>Základní výbava pro šnorchlování</h2>'
          '<p>Šnorchlování je povrchové pozorování podmořského světa. Nepotřebujete certifikaci ani lahev, stačí pár kousků dobře padnoucí výbavy. Zbytek je otázka pohodlí a bezpečnosti.</p>'
          + T(['Kus výbavy', 'K čemu slouží', 'Na co dát pozor při výběru'], [
              ['Maska', 'umožňuje ostře vidět pod vodou', 'těsnění na obličeji, objem, zorné pole, skla'],
              ['Šnorchl', 'dýchání s obličejem pod hladinou', 'ventil nebo sprej, měkký náustek, pohodlná trubice'],
              ['Ploutve', 'pohon s menší námahou', 'velikost, tuhost lopatky, otevřená či celá pata'],
              ['Neopren nebo lycra', 'ochrana před chladem a sluncem', 'tloušťka, střih, velikost'],
              ['Boty a ponožky', 'ochrana nohy v ploutvi a na kamenech', 'podrážka, výška, tloušťka'],
              ['Taška na výbavu', 'přeprava a sušení', 'větrání, velikost, odolnost vůči písku']]) +
          '<h2>Jak vybrat masku</h2>'
          '<p>Maska je nejdůležitější kus, protože musí sedět na obličeji. Platí jednoduchá zkouška: přiložte ji bez pásku k obličeji, lehce se nadechněte nosem a pusťte ji. Pokud drží na místě několik sekund, těsní. Mezi úzkým obličejem a širokým je rozdíl, proto vyzkoušejte víc modelů. Měkká silikonová sukně lépe těsní než tvrdá. Při nošení brýlí hledejte masku s možností vyměnit skla za dioptrická.</p>'
          '<ul><li><strong>Nízký objem</strong> se lépe vyprazdňuje a hodí se pro freediving, vyšší objem nabízí větší zorné pole.</li>'
          '<li><strong>Jednoskelová maska</strong> má široký výhled, dvouskelová umožňuje dioptrie.</li>'
          '<li><strong>Tvrzené sklo</strong> se vyplatí a při rozbití se nerozpadne na ostré střepy.</li>'
          '<li><strong>Barva sukně</strong> ovlivní vnímání: tmavá snižuje odlesky, průhledná propouští více světla.</li></ul>'
          '<h2>Šnorchl: jednoduchý, ventilový, celoobličejová maska</h2>'
          '<p>Nejběžnější je klasická trubice s měkkým náustkem a kolenem. Verze s ventilem na konci brání vniknutí vody při ponoření, ale v hlubším ponoru se hůř vyrovnává tlak. Suchý šnorchl má mechanismus, který trubici při potopení uzavře, a po vynoření ji otevře. Celoobličejové masky pojí masku i šnorchl a umožňují dýchat nosem i ústy. Pozor ale na hluboký ponor, kde nejsou určené, a na špatně padnoucí kusy, protože výdechový vzduch se může hromadit. Měkký náustek šetří čelist, odnímatelný jde vyprat a vyčistit.</p>'
          '<h2>Ploutve a jejich typy</h2>'
          '<p>Rozlišujte krátké a dlouhé ploutve, s uzavřenou a otevřenou patou. Krátké šnorchlovací ploutve se dobře skládají do batohu a méně unavují. Dlouhé jsou efektivnější pro plavání a freediving. Uzavřená pata se obouvá přímo na bosou nohu a hodí se k teplému moři. Otevřená pata se nasazuje na botičku a je univerzálnější pro studenou vodu i potápění s přístrojem. Správná velikost nesmí tlačit, ale ani se motat. Koupě na vyzkoušení na suchu často klame, protože ve vodě noha mírně změní objem.</p>'
          '<h2>Potápění s přístrojem</h2>'
          '<p>Přístrojové potápění už vyžaduje výcvik a kvalifikaci, kterou vám vystaví potápěčská škola. Základ výbavy tvoří regulátor, kompenzátor (vesta), ponorový počítač, ploutve, maska a neopren nebo suchý oblek. V nabídce najdete také přístrojová příslušenství jako svítilny, kompasy, ponorkové hodinky a zavěšení. Značky jako ' + B(('aqualung', 'Aqualung'), ('mares', 'Mares'), ('apeks', 'Apeks'), ('scubapro', 'Scubapro'), ('cressi', 'Cressi'), ('tecline', 'Tecline'), ('shearwater', 'Shearwater')) + ' jsou v kategorii zastoupené vedle běžných šnorchlovacích sad. Životně důležité vybavení jako regulátor nekupujte bez konzultace s instruktorem a pravidelně jej nechávejte servisovat.</p>'
          '<h2>Ochrana těla: neopren a lycra</h2>'
          '<p>I v teplém moři se po delší době ve vodě prochladíte. Slunce navíc pálí záda, když plavete obličejem dolů. Řešením je neopren nebo lehké lycrové tričko. Přečtěte si o nich v kategoriích <a href="/neopreny/">neopreny</a> a <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>. Obuv na kamenitá dna najdete v <a href="/obuv-do-vody/">obuvi do vody</a>, ke slunění pomohou <a href="/plazove-doplnky/">plážové doplňky</a> a ke koupání <a href="/plavky/">plavky</a>.</p>'
          '<h2>Příprava před cestou</h2>'
          '<p>Nová maska má na skle tenkou vrstvu silikonu z výroby, která způsobuje mlžení. Před prvním použitím ji jemně odstraňte, například zubní pastou bez zrnek, a důkladně opláchněte. Na mlžení pomáhá také antifog gel nebo kapka šamponu, který pak opláchnete. Výbavu vyzkoušejte v bazénu nebo mělké vodě před dovolenou, aby se nic nezjistilo až u moře. Pokud cestujete letecky, zkontrolujte rozměry a váhu zavazadla a ploutve složte do kufru jako výplň.</p>'
          '<h2>Pro koho které vybavení</h2>'
          '<p>Rodiny s dětmi zvolí malé sady s měkkým náustkem a menší maskou. Děti rychle rostou, proto stačí levnější kus na pár sezón, ale těsnění musí fungovat. Ti, kdo cestují často, ocení vlastní kvalitní masku a lehké ploutve do příručního zavazadla. Aktivní freediveři potřebují nízkoobjemovou masku, dlouhé ploutve a vhodný neopren. Začínající potápěči by měli před nákupem většího vybavení absolvovat kurz a nechat si poradit.</p>'
          '<h2>Péče o výbavu</h2>'
          '<ul><li>Po každém použití opláchněte vše sladkou vodou, aby sůl nepoškodila materiály.</li>'
          '<li>Sušte ve stínu. Slunce a teplo poškozují silikon a gumu.</li>'
          '<li>Masku neukládejte přitlačenou, silikon se deformuje.</li>'
          '<li>Neopren sušte na plochém ramínku a uložte zavěšený.</li>'
          '<li>Regulátor a ponorové přístroje nechte pravidelně prohlédnout v autorizovaném servisu.</li></ul>'
          '<h2>Bezpečnost při šnorchlování</h2>'
          '<p>Nikdy nešnorchlujte sami. Zjistěte si předem proudy a vlny a držte se blízko pobřeží nebo lodi. Vesta nebo plovoucí bóje s vlajkou usnadní viditelnost a pomůže při únavě. Nehyperventilujte před ponorem, protože zvyšuje riziko ztráty vědomí pod vodou. Neodplouvejte dál, než zvládnete bez námahy doplavat zpět, a nedotýkejte se korálů ani živočichů.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Kupovat masku podle vzhledu a ne podle těsnění.</li>'
          '<li>Volit příliš tuhé ploutve na krátké pobyty, nohy se brzy unaví.</li>'
          '<li>Zapomenout na ochranu před sluncem a chladem.</li>'
          '<li>Použít novou masku bez předchozího odmaštění skla.</li>'
          '<li>Podcenit velikost patního dílu u ploutví.</li>'
          '<li>Pustit se do hlubokých ponorů s vybavením určeným na povrch.</li></ul>',
    faq=[
        ('Jak poznám, že maska dobře těsní?', 'Přiložte ji bez pásku na obličej, lehce vdechněte nosem a pusťte. Pokud zůstane viset několik sekund, těsní. Zkontrolujte také, zda vám nedrhne o nos a nepřekáží ve vousech či vlasech.'),
        ('Proč se mi maska mlží?', 'Nová maska má z výroby silikonovou vrstvu na skle, kterou je třeba odstranit. Později pomáhá antifog gel nebo kapka šamponu. Mlžení snižuje i dostatečné ochlazení skla vodou před nasazením.'),
        ('Jaký šnorchl je pro začátečníka nejlepší?', 'Jednoduchá trubice s měkkým náustkem nebo suchý šnorchl, který uzavře přístup vody při potopení. Podstatné je pohodlí v ústech a snadné vyprázdnění trubice výdechem.'),
        ('Jak vybrat velikost ploutví?', 'Podle obuvi, kterou budete nosit uvnitř. Při uzavřené patě se bere noha naboso, u otevřené s botičkou. Ploutev nesmí tlačit ani se motat. Konkrétní tabulky velikostí se mezi značkami liší.'),
        ('Je lepší otevřená, nebo uzavřená pata?', 'Uzavřená je lehčí a vhodná k teplému moři. Otevřená se nosí s botičkou a hodí se i do chladné vody a na potápění s přístrojem, kde zajišťuje ochranu paty.'),
        ('Mohu šnorchlovat v brýlích?', 'Ne, ale můžete si vybrat masku s dioptrickými skly nebo si nasadit kontaktní čočky. V běžných dioptrických brýlích šnorchlovat nelze. Dioptrická skla se vyměňují do některých modelů masek podle sady.'),
        ('Jak pečovat o šnorchlovací výbavu?', 'Po každém použití opláchněte sladkou vodou, sušte ve stínu a masku ukládejte do pouzdra. Slunce a teplo poškozují silikon, a proto výbavu neponechávejte v rozpáleném autě.'),
        ('Potřebuji neopren i v teplém moři?', 'Není nutný, ale po delším pobytu ve vodě prochladnete. Lehká lycra nebo tenký neopren chrání i proti slunci, medúzám a otěru o kameny.'),
        ('Můžu s šnorchlovací výbavou začít potápět s lahví?', 'Maska a ploutve se hodí, ale přístrojové potápění vyžaduje kurz u instruktora a další výbavu. Regulátor a vestu nekupujte bez konzultace a vždy je nechte servisovat.'),
        ('Jaké vybavení zvolit pro děti?', 'Menší masku s měkkou sukní, krátký šnorchl s lehkým náustkem a ploutve přesné velikosti. Dítě musí být ve vodě pod stálým dohledem dospělého a doplněno plovací vestou.'),
    ])

# ------------------------------------------------------------------ joga-a-podlozky
NEW['joga-a-podlozky'] = dict(long=True,
    title='Jógové podložky: tloušťka, materiál, výběr | Sporteka',
    desc='Jógové a cvičební podložky z PVC, TPE, kaučuku i korku. Jak vybrat tloušťku, protiskluz a rozměr, jak podložku čistit a které značky najdete.',
    intro='<p><strong>Jógová podložka</strong> je základ domácího i studiového cvičení: určuje, jak pevně stojíte v pozicích, jak snášejí klouby tvrdou podlahu a jak pohodlně vás drží při dlouhých sekvencích. Podložky se liší materiálem, tloušťkou, povrchem a hmotností, a rozdíl se pozná hned po prvním cvičení. Příliš měkká podložka rozhazuje rovnováhu, příliš tenká zase tlačí do kolen.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů vedle sebe. Širší výbavu najdete ve skupinách <a href="/joga-a-pilates/">jóga a pilates</a>, <a href="/jogove-pomucky/">jógové pomůcky</a>, <a href="/pilates-pomucky/">pilates pomůcky</a> a <a href="/meditace/">meditace</a>. Níže vás provedeme materiály, rozměry i péčí.</p>',
    guide='<h2>Z čeho se podložky vyrábějí</h2>'
          '<p>Materiál ovlivňuje protiskluz, váhu, životnost i dopad na životní prostředí. Žádný není ideální pro všechny.</p>'
          + T(['Materiál', 'Vlastnosti', 'Pro koho'], [
              ['PVC', 'pevná, odolná, snadno čistitelná, těžší', 'každodenní domácí cvičení, začátečníci'],
              ['TPE', 'lehčí, měkčí, recyklovatelnější než PVC', 'cesty, kombinace s pilates, citlivé klouby'],
              ['Přírodní kaučuk', 'výborný protiskluz, těžší, má typický zápach', 'dynamické styly, pocení rukou'],
              ['Korek', 'přirozeně protiskluzný při vlhku, podle výrobce částečně odolný proti pachům', 'hot jóga, alergici'],
              ['Pěna NBR', 'tlustá, měkká, málo stabilní', 'pilates, cvičení na zemi, rehabilitační pozice'],
              ['Textil a bavlněné koberečky', 'pohodlné, hřejivé, málo protiskluzné', 'doplněk pod relaxační polohy']]) +
          '<h2>Tloušťka a odpružení</h2>'
          '<p>Nejběžnější podložky měří několik milimetrů. Tenčí kusy (cca 1–3 mm) jsou stabilní a skladné, hodí se na cesty a pro ty, kdo potřebují cítit podlahu. Standardní tloušťka kolem 4–6 mm je kompromis mezi oporou a komfortem. Silnější kusy chrání kolena a kyčle, ale ztrácí stabilitu ve stoje a při pozicích na jedné noze. Pokud vás bolí kolena při klečení, zvažte raději druhý menší polštář než extrémně tlustou podložku. Pro pilates, kde ležíte na zádech, se hodí vyšší komfort.</p>'
          '<h2>Rozměr podložky</h2>'
          '<p>Běžná délka bývá kolem 170–185 cm a šířka okolo 60 cm. Vyšší lidé by měli vybrat delší model, aby se vešli bez vyčnívající hlavy či nohou. Širší podložky nabízejí víc prostoru pro rozkročené pozice, ale hůř se nosí. Měřte se na výšku s pažemi nataženými nad hlavou a porovnejte s údajem výrobce.</p>'
          '<h2>Protiskluz a povrch</h2>'
          '<p>Protiskluz je důležitější, než se zdá. Při psí hlavou dolů nebo bojovníkovi se vám ruce a nohy posouvají. Hladký povrch je snadno čistitelný, strukturovaný má lepší záběr. Zkuste podložku vlhkou rukou, než se rozhodnete. U kaučuku nebo korku se protiskluz při potu zlepšuje, zatímco u levného PVC může klesat. Spodní strana by měla držet na podlaze, dřevo a dlažba mají odlišný odpor. Některé podložky mají na povrchu vyznačené linie pro správné zarovnání rukou a nohou, což pomáhá při učení pozic.</p>'
          '<h2>Typy podložek podle cvičení</h2>'
          '<ul><li><strong>Jóga</strong>: tenčí až střední tloušťka, dobrý protiskluz, pevný povrch.</li>'
          '<li><strong>Pilates</strong>: o něco širší a silnější, protože ležíte a kutálíte se po páteři.</li>'
          '<li><strong>Hot jóga</strong>: korek, kaučuk nebo ručník s protiskluzem na podložku.</li>'
          '<li><strong>Cestovní</strong>: tenká a skládací, s nízkou hmotností.</li>'
          '<li><strong>Posilování a stretching</strong>: širší, silnější, aby zvládla činky i dopady.</li>'
          '<li><strong>Podložka pro děti</strong>: kratší, barevná, snadno omyvatelná.</li></ul>'
          '<h2>Co přidat k podložce</h2>'
          '<p>Základní doplňky tvoří blok, popruh, bolster a deka. Blok zkracuje vzdálenost od podlahy, popruh pomáhá v předklonech, bolster podepírá záda a deka zahřeje při relaxaci. K tomu se hodí taška na přenášení a pouzdro. Posilování můžete rozšířit o <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/balancni-pomucky/">balanční pomůcky</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>. Obecný sortiment zahrnuje skupina <a href="/fitness/">fitness</a>. Na protažení po tréninku se hodí i <a href="/pilates-pomucky/">pilates pomůcky</a>. Pro pohodlí během cvičení se hodí také odpovídající sportovní oblečení.</p>'
          '<h2>Jak cvičit na podložce bezpečně</h2>'
          '<p>Podložku položte na rovnou plochu a ověřte, že se neposouvá. Na kluzkém parketu pomůže protiskluzová spodní vrstva. Při přechodu z pozice do pozice dbejte na to, aby se okraj nezvrátil pod nohou. Pokud máte bolesti zad, kolen či jiné zdravotní potíže, poraďte se před cvičením s lékařem nebo kvalifikovaným lektorem. Podložka nemůže opravit špatnou techniku.</p>'
          '<h2>Péče a čištění</h2>'
          '<p>Podložku po cvičení otřete vlhkým hadříkem. Jednou za čas ji umyjte jemným mýdlovým roztokem nebo prostředkem doporučeným výrobcem. Vyhněte se agresivní chemii, alkoholu a silným rozpouštědlům, které poškodí povrch. Sušte ji ve stínu rozloženou nebo rolovanou volně. Přímé slunce a radiátor materiál znehodnocují. Při skladování podložku srolujte povrchem ven, aby se nekroutily okraje. U přírodního kaučuku se po prvním rozbalení může objevit zápach, který časem vyprchá po vyvětrání.</p>'
          '<h2>Pro koho jaká podložka</h2>'
          '<p>Začátečníci uspějí s univerzální podložkou střední tloušťky z PVC nebo TPE. Pokročilí a lidé s propocenými rukama ocení kaučuk nebo korek. Cestovatelé volí tenčí skládací kus. Ti, kdo cvičí často, by měli investovat do kvalitnější podložky, protože lepší materiál drží tvar. Pro rodiny s malými dětmi je praktické mít jednu pevnou, snadno omyvatelnou podložku. U alergiků na latex se vyhýbejte přírodnímu kaučuku a zkontrolujte složení.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce nabídek mají ' + B(('merco', 'Merco'), ('adidas', 'Adidas'), ('hms', 'HMS'), ('sportago', 'Sportago'), ('sharp-shape', 'Sharp Shape'), ('bodhi', 'Bodhi'), ('casall', 'Casall'), ('manduka', 'Manduka'), ('lifefit', 'Lifefit'), ('insportline', 'Insportline'), ('myga', 'Myga'), ('nike', 'Nike'), ('kimjaly', 'Kimjaly'), ('spokey', 'Spokey')) + '. Rozdíly jsou v materiálu, tloušťce a v tom, zda značka cílí na jógové studio, nebo na domácí fitness. Sledujte popis materiálu a rozměry, ne jen barvu.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Vybrat příliš tlustou podložku a ztratit stabilitu ve stoje.</li>'
          '<li>Kupovat podle barvy a ne podle materiálu a protiskluzu.</li>'
          '<li>Zapomenout na délku u vysokých lidí.</li>'
          '<li>Prát podložku v pračce nebo ji čistit agresivní chemií.</li>'
          '<li>Skladovat ji na slunci či u topení.</li>'
          '<li>Čekat, že podložka nahradí správnou techniku.</li></ul>',
    faq=[
        ('Jak tlustá má být jógová podložka?', 'Standardně kolem 4 až 6 milimetrů, což dává oporu i komfort. Tenčí se hodí na cesty a pro stabilitu, silnější chrání klouby při klečení, ale hůře drží rovnováhu.'),
        ('Z jakého materiálu je nejlepší podložka?', 'Záleží na stylu cvičení. PVC je odolná a běžná, TPE lehčí, kaučuk má vynikající protiskluz a korek funguje dobře při pocení. Žádný materiál není nejlepší pro všechny.'),
        ('Jak dlouhá podložka mi stačí?', 'Zhruba 170 až 185 centimetrů je běžná délka. Vyšším lidem sedí delší verze, aby se při ležení vešli celou postavou. Porovnejte svou výšku s údajem výrobce.'),
        ('Proč mi podložka klouže?', 'Možná je povrch nový a ještě nepřilnul, nebo je podložka znečištěná mastnotou. Pomoci může omytí jemným roztokem a vysušení. Při pocení zvažte korek, kaučuk nebo ručník s protiskluzem.'),
        ('Jak podložku čistit?', 'Otřete ji po cvičení vlhkým hadříkem a čas od času omyjte jemným mýdlovým roztokem. Nepoužívejte agresivní chemii ani alkohol a sušte ji ve stínu, ne na slunci či radiátoru.'),
        ('Hodí se jógová podložka na pilates?', 'Pro jednodušší cvičení ano. Pilates ale často vyžaduje silnější vrstvu, protože ležíte a kutálíte se po páteři. Hledejte širší a tlustší model nebo speciální podložku na pilates.'),
        ('Proč podložka z kaučuku zapáchá?', 'Přírodní kaučuk má po výrobě typický zápach, který po několika dnech až týdnech vyvětrání odezní. Rozbalte ji na vzdušném místě a nenechávejte ji v zavřeném obalu.'),
        ('Dá se podložka prát v pračce?', 'Většina výrobců to nedoporučuje, neboť pračka a odstředivka deformují materiál. Omývejte ji ručně podle pokynů výrobce a nechte vyschnout rozloženou.'),
        ('Jak podložku uložit?', 'Srolujte ji povrchem ven, aby se okraje nezvedaly, a uložte na suchém místě bez přímého slunce a tepla. Neskládejte ji ostře, vznikají praskliny.'),
        ('Potřebuji kromě podložky i další pomůcky?', 'Pro začátek stačí podložka. Blok, popruh a bolster pomáhají s flexibilitou a pohodlím. Rozšiřovat vybavení má smysl až tehdy, když zjistíte, co vám při cvičení chybí.'),
    ])


# ------------------------------------------------------------------ extensions (extra sections + FAQ)
def _ext(slug, intro_add, guide_add, faq_add):
    e = NEW[slug]
    e['intro'] = e['intro'].replace('</p>', ' ' + intro_add + '</p>', 1)
    e['guide'] += guide_add
    e['faq'] += faq_add


_ext('bazeny',
     'Počítejte i s tím, že stavba bazénu je jen začátek, protože na údržbu potřebujete pár minut denně.',
     '<h2>Napouštění, ohřev a spotřeba vody</h2>'
     '<p>Větší bazén se napouští hodiny a během toho se hodí kontrolovat, zda stěny rostou rovnoměrně. Pokud se jedna strana zvedá rychleji, bazén je nakloněný a je lepší vodu pustit a podloží upravit hned, ne až po naplnění. Studená voda ze studny nebo řadu bývá chladná, a proto ji na slunci ohřejte. Pomůže tmavá solární plachta nebo solární ohřívač, který využije energii slunce bez elektřiny. Při dlouhé vedrové vlně hlídejte hladinu, protože odpar a stříkání vodu ubírají. Doplňování berte jako součást provozu a zkontrolujte, zda máte po ruce zahradní hadici dostatečné délky.</p>'
     '<h2>Děti a hra u vody</h2>'
     '<p>Pro děti jsou důležité malé věci: schůdky s protiskluzem, měkké hrany a vyšší stěna, přes kterou batole samo nepřelezne. Nafukovací hračky a míče dělají bazén zábavnějším, ale vybírejte takové, které jsou určené pro vodu. Při hře ve větší skupině stanovte pravidla, třeba zákaz skoků do mělké vody a omezení počtu lidí najednou. Starší děti se mohou učit plavat, k čemuž se hodí <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plavecké čepice</a>. Po koupání dětem dopřejte ručník a odpočinek ve stínu, protože sluneční záření u hladiny je intenzivní.</p>'
     '<h2>Co dělat při poruše</h2>'
     '<p>Nejčastější problémy jsou úniky vody, hlučné čerpadlo a zakalená voda. Pokud hladina klesá rychleji, než odpovídá odparu, zkontrolujte spoje hadic, ventily a okraj podložky. Malou dírku v fólii opravíte záplatou, rozsáhlé poškození nebo trhlina u švu znamená výměnu. Hučící čerpadlo bývá zanesené nebo nasává vzduch. Vyčistěte předfiltr a ověřte těsnění. Zakalenou vodu po bouřce nebo velkém zatížení většinou vyřeší proplach filtru a dávka dezinfekce, případně flokulačním přípravkem podle návodu. Pokud potíže přetrvávají, nahlédněte do návodu a zkontrolujte, zda ho výrobce neuvádí jako typickou závadu.</p>'
     '<h2>Jak zvolit podle velikosti rodiny</h2>'
     '<p>Pro dva dospělé a jedno dítě stačí menší kruhový rámový bazén, ve kterém se dá osvěžit, ale neplave se. Pro čtyřčlennou rodinu s předškoláky se hodí větší průměr a hloubka, ve které dítě dosáhne na dno a dospělý se pohodlně posadí. Když má bazén sloužit i ke cvičení či plavání, uvažujte o obdélníkovém tvaru nebo oválu. Při výběru si vždy představte, kolik lidí ho skutečně použije současně, a nikoli kolik se jich tam vejde na fotce katalogu.</p>',
     [('Jak dlouho trvá napuštění bazénu?', 'U větších bazénů několik hodin až přes den, podle objemu a tlaku vody v zahradním kohoutu. Během napouštění kontrolujte, aby stěny rostly rovnoměrně a bazén zůstal vodorovný.'),
      ('Čím bazén ohřát?', 'Nejjednodušší je tmavá solární plachta nebo solární ohřívač. Existuje i tepelné čerpadlo a elektrický ohřev, ty však vyžadují přípravu přívodu a vyšší pořizovací náklady.')])

_ext('merino-mikiny',
     'Tenká pletenina se hodí i do kanceláře a na delší cestu, hrubší zase na zimní chatu, a proto stojí za to vědět, k čemu ji budete nosit.',
     '<h2>Merino na túru, na běžky a do města</h2>'
     '<p>Na túře se merino mikina osvědčí při měnící se zátěži. Při stoupání rozepnete zip a vyhrnete rukávy, na hřebeni zip zavřete a přidáte větrovku. Při běžkování se hodí tenčí vrstva, protože při pohybu vzniká hodně tepla a sníh nenechává ani chvilku zchladnout. Ve městě vystačí svetr pod kabát a kvalitní pulovr vypadá dobře i bez sportovního designu. Cestovatelé ocení, že merino nezačne po jednom dni zapáchat, a mohou tak s sebou vzít méně kousků. Výhodou je i to, že vlna se po vyvětrání obnoví a méně se mačká než bavlna.</p>'
     '<h2>Proč se cena a kvalita liší</h2>'
     '<p>Rozdíly mezi kousky vznikají v kvalitě příze, způsobu pletení a zpracování. Tenčí vlákno bývá měkčí a dražší, hustší pletení je odolnější proti protahování. Příměs syntetického vlákna zvyšuje pevnost, avšak mění chování při nošení. Zkontrolujte původ vlny a zda je výrobce uvádí. Některé značky se věnují etickému chovu ovcí a označují, jak postupují při stříhání. Tyto údaje bývají na webu výrobce nebo na visačce. Neberte slibované vlastnosti za hotovou věc, ale ověřte složení materiálu v popisu.</p>'
     '<h2>Merino pro ženy, muže a děti</h2>'
     '<p>Dámské střihy jsou užší v pase a v ramenou, mužské širší a delší. Unisexové mikiny pokrývají střední velikost a hodí se, pokud vám sedí obě varianty. Dětské merino se hodí tam, kde dítě trpí chladem, třeba při zimních výletech. Pozor ale na růst: zvolte velikost, která dítěti sedí hned, ne příliš velkou, aby vrstva dobře přiléhala. Na stránkách výrobců najdete tabulky velikostí a doporučení pro vrstvení.</p>'
     '<h2>Další oblečení k vrstvení</h2>'
     '<p>Pokud skládáte celý outfit, začněte tričkem z kategorie <a href="/merino-tricka/">merino trička</a>, přidejte mikinu, pak bundu. Pod vrstvu zvolte pohodlné spodní prádlo a ponožky. Na nohy se hodí <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> a při větším chladu <a href="/termopradlo/">termoprádlo</a>. Tento přístup se v horách nazývá „cibulový“ a umožňuje reagovat na změnu počasí bez nutnosti nést objemnou výbavu.</p>',
     [('Hodí se merino mikina na sport s vysokou intenzitou?', 'Tenčí merino se používá při běhu, běžkování nebo skialpu, protože dobře odvádí pot. Pro nejtvrdší zátěž a otěr batohu se hodí směs s příměsí syntetiky, která zvyšuje odolnost.'),
      ('Poznám kvalitu merino svetru na dotek?', 'Částečně. Jemná, hustá pletenina bez drsných vláken a rovné švy jsou dobré znamení. Rozhodující je ale složení a zpracování uvedené v popisu, ne jen první dojem.')])

_ext('snorchlovani',
     'Vybavení k moři přitom nemusí být drahé, jen musí sedět a těsnit.',
     '<h2>Jak se pohybovat ve vodě</h2>'
     '<p>Šnorchlování nezávisí na síle, ale na klidu. Plavte pomalu, pravidelně kopejte z kyčlí a neohýbejte příliš kolena, abyste neztráceli energii. Ruce držte u těla nebo je volně nechte klesat, nepotřebujete je k pohonu. Nadechujte se hluboce a plynule, pokud se do trubice dostane voda, prudce vydechněte a trubici vyprázdníte. Pokud vám v masce vznikne kondenzace nebo voda, zvedněte hlavu nad hladinu, masku upravte a pokračujte. Při první zkoušce začněte na mělkém místě s dobrým výhledem, ať si zvyknete na dýchání pusou.</p>'
     '<h2>Podmínky: moře, jezero, bazén</h2>'
     '<p>Slaná voda nese víc než sladká, proto se v moři snáz drží hladina, ale musíte počítat s vyšší odolností při potápění do hloubky. Sladkovodní jezera mají často horší viditelnost, studenější vodu a chybějící korály, a přesto jsou pro trénink ideální. Bazén je nejlepší místo na vyzkoušení nové masky a naučení dýchání. Před vstupem do moře zjistěte, kde jsou proudy, jaké jsou vlny a kde se pohybují lodě. Při nízké viditelnosti nebo bouřce výlet odložte.</p>'
     '<h2>Podvodní fotografie a doplňky</h2>'
     '<p>Mnoho lidí si chce pořídit záběry. Voděodolná pouzdra na telefony a sportovní kamery zachytí pozorování, ale vyžadují kontrolu těsnění před každým ponorem. Doplňky jako plovoucí úchyt, popruh na zápěstí a bójka s vlajkou zvyšují bezpečnost. Do příruční taštičky přibalte antifog, náhradní pásek na masku a pouzdro na šnorchl. Pokud sháníte ochranné pomůcky, najdete je v <a href="/plazove-doplnky/">plážových doplňcích</a>.</p>'
     '<h2>Přeprava a cestování</h2>'
     '<p>Ploutve a maska zabírají místo, proto zvolte kratší ploutve, pokud cestujete s příručním zavazadlem. Masku uložte do pevného pouzdra, aby se nepřitlačila a nezdeformovala. Šnorchl se vejde do boty nebo do bočních kapes. Neopren nebo lycra váží málo a skládá se. Na kamenité pláže se hodí <a href="/obuv-do-vody/">obuv do vody</a>, pro odpočinek na lehátku zase <a href="/panske-plavky/">pánské plavky</a> nebo <a href="/damske-plavky/">dámské plavky</a> a děti se vejdou do <a href="/detske-plavky/">dětských plavek</a>. Po návratu vše opláchněte, osušte a uložte, aby další sezonu nezapáchalo. Před další cestou zkontrolujte pásek masky, těsnění a ventil šnorchlu, protože guma po delším skladování křehne a zbytečně by vás zradila až u vody. Lehkou lycru a neopren si vezměte vždy, i když počasí vypadá vlídně.</p>',
     [('Je lepší koupit si vlastní výbavu, nebo ji půjčovat?', 'Vlastní maska a šnorchl sedí lépe a jsou hygieničtější. Ploutve se dají půjčit, zejména pokud cestujete s malým zavazadlem. Výběr závisí na tom, jak často do vody chodíte.'),
      ('Kdy je lepší vybrat celoobličejovou masku?', 'Pro pohodlné dýchání a široký výhled při klidném plavání na povrchu. Nehodí se do hloubky ani na freediving, a musí perfektně sedět. Při pochybnostech zvolte klasickou sadu.')])

_ext('joga-a-podlozky',
     'Při výběru se vyplatí myslet na to, kde a jak často budete cvičit, a také kdo další bude podložku používat.',
     '<h2>Podložka podle prostředí</h2>'
     '<p>V bytě s dřevěnou či laminátovou podlahou potřebujete podložku, která neklouže, jinak se ve výpadech posunete. Na koberci se naopak tenčí kus bortí a ztrácí oporu, pomůže pevnější a širší. Ve studiu bývá podložka často k dispozici, přesto si mnoho lidí nosí vlastní z hygienických důvodů. Venku na trávě či pláži ocení cvičenci vodotěsnou, lehce omyvatelnou podložku, kterou pak stačí otřít. Na trávě dbejte na to, aby byl povrch suchý a bez ostrých kamínků, které by podložku porušily.</p>'
     '<h2>Jak podložku používat při různých stylech</h2>'
     '<p>Pomalé styly s dlouhými výdržemi, například restorativní jóga, vyžadují měkčí a teplejší povrch, aby se tělo uvolnilo. Dynamické sekvence typu vinyasa potřebují pevnější a protiskluzovou podložku. Při statickém protahování se dá využít tenčí kus. Pilates zahrnuje pohyby po páteři, k nimž je vhodná silnější vrstva. Pokud kombinujete víc stylů, zvolte střední tloušťku a podle potřeby přidejte složenou deku nebo ručník pod kolena.</p>'
     '<h2>Ekologie a materiály</h2>'
     '<p>Zajímáte-li se o dopad na životní prostředí, sledujte označení výrobce a materiál. TPE bývá označováno jako recyklovatelnější než PVC, přírodní kaučuk a korek pocházejí z obnovitelných zdrojů. Ověřte ale, zda nejde jen o marketing. Z hlediska ekologie je nejlepší podložka ta, která vám vydrží mnoho let. Starou podložku lze využít jako ochrannou podložku pod nářadí, do auta nebo na zahradu, než ji vyhodíte.</p>'
     '<h2>Postup při prvním použití</h2>'
     '<p>Nová podložka bývá z výroby kluzká, protože na povrchu zůstává jemný film. Několikrát ji omyjte jemným roztokem nebo ji prostě používejte, povrch se časem otře. Rozbalte ji několik hodin před cvičením, aby se narovnaly okraje. Při prvním cvičení si zkuste výdrže, ve kterých se hodně pohybujete, a ověřte, že vám nic neklouže. Pokud je podložka stále kluzká, vyzkoušejte protiskluzový ručník, nebo zvažte jiný materiál.</p>'
     '<h2>Podložka pro meditaci a odpočinek</h2>'
     '<p>Pro meditaci v sedě je důležité, aby kolena nezůstala viset ve vzduchu. Pomůže složená deka, meditační polštář nebo blok pod sedací kosti. Silnější podložka lépe tlumí tlak na kotníky, tenká zase poskytuje stabilitu. Více pomůcek najdete v kategorii <a href="/meditace/">meditace</a>. Při relaxační poloze na zádech přikryjte tělo dekou, protože v klidu rychle chladnete. Po jógové sérii se hodí delší protažení, při kterém si dopřejte klid a dostatek času na návrat k normálnímu dechu.</p>'
     '<h2>Jak často podložku měnit</h2>'
     '<p>Při pravidelném cvičení vydrží kvalitní podložka několik let. Znamení k výměně jsou ztracený protiskluz, praskliny na povrchu, prosezené místo, kde vzniká důlek, a trvalé zdeformování. Pokud pozorujete, že vás začíná bolet zápěstí nebo kolena, může být problém v rozměklém materiálu. Při bolesti kloubů se poraďte s lékařem nebo lektorem, podložka je jen jednou z možných příčin. K podložce se hodí i <a href="/fitness-pomucky/">fitness pomůcky</a>, ale ty obvykle pořizujte až poté, co zjistíte, co vám při cvičení skutečně chybí.</p>',
     [('Jak poznám, že je čas koupit novou podložku?', 'Když se ztratí protiskluz, povrch praská, objeví se prosezené důlky nebo se okraje trvale kroutí. Dlouhodobou bolest zápěstí či kolen ale řešte s lékařem nebo lektorem, podložka je jen jednou z možných příčin.'),
      ('Je lepší podložka s vyznačenými liniemi?', 'Linie pomáhají se správným postavením rukou a nohou, takže se hodí začátečníkům. Zkušení cvičenci často dávají přednost čistému povrchu. Je to otázka osobního pohodlí.')])
