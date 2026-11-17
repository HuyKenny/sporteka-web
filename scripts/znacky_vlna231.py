"""sporteka.cz — brand page texts wave 231: fischer, garmin, birkenstock, tamaris, ugg, specialized.
General facts only, no prices or counts; assortment taken from the live catalogue (17. 11. 2026).

Sources (checked 17. 11. 2026):
- Fischer: en.wikipedia.org/wiki/Fischer_(company); austria-forum.org (Fischer Sports, 1924, Ried im Innkreis, family-owned);
  Fischer Vacuum fit (inthesnow.com, suburbanskiandbike.com/pages/fischer-vacuum-process); IFP plates / Turnamic compatibility
  (evo.com, snowleader.com); bike helmets "Fischer Die Fahrradmarke" = MTS Group, Rülzheim (helmet manual, mediamarkt.at).
- Garmin: en.wikipedia.org/wiki/Garmin (1989, Gary Burrell + Min Kao, Olathe since 1996); Garmin timeline (Forerunner 201, 2003);
  Tacx acquisition 2019 (garmin.com newsroom, SEC 10-Q).
- Birkenstock: birkenstock-group.com (tradition since 1774, Langen-Bergheim); en.wikipedia.org/wiki/Birkenstock (1963 footbed
  sandal sold as Madrid, L Catterton 2021, IPO 2023); birkenstock.com FAQ regular vs narrow width; Birko-Flor and EVA descriptions.
- Tamaris: wortmann-group.com/en/group/history (Wortmann KG, Detmold, Horst Wortmann 1967; Tamaris active capsule 2021;
  Caprice, Marco Tozzi, Jana); tamaris.com product pages (Touch-it footbed, removable footbed, Comfort fit width).
- UGG: en.wikipedia.org/wiki/UGG_(brand) and /Ugg_boots (Brian Smith, 1978, Deckers 1995, generic term in Australia/NZ).
- Specialized: en.wikipedia.org/wiki/Specialized_Bicycle_Components, /Specialized_Stumpjumper (1974 Mike Sinyard, Stumpjumper 1981,
  Morgan Hill); specialized.com Body Geometry (Roger Minkow); ANGi sensor (bikeradar.com); SWAT (specialized.com); S-Sizing
  (theproscloset.com, support.specialized.com).
Left out (not verified): exact launch years of Arizona/Boston, Garmin Edge launch year, Roval ownership details, who makes
the Fischer-branded apparel, official UGG half-size rule."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ fischer
NEW['fischer'] = dict(
    title='Fischer: lyže, běžky, lyžařské boty a hokejky',
    desc='Fischer v katalogu: sjezdové lyže The Curv a RC4, běžky Twin Skin a Speedmax, boty na běžky, lyžáky Vacuum a hokejky RC One. Jak vybrat a srovnat nabídky.',
    intro='<p>Když lidé hledají Fischer, obvykle myslí rakouského výrobce lyží z Riedu im Innkreis. Pod stejným jménem se ale prodávají i výrobky jiných firem: německé cyklistické přilby, a dokonce montážní pěny a kotvy pro stavebníky. '
          'Tato stránka se soustředí na Fischer Sports, tedy na sjezdové a <a href="/bezecke-lyze/">běžecké lyže</a>, boty na běžky, lyžařské boty, hole a hokejové vybavení. '
          'Sporteka.cz u každého produktu ukazuje nabídky českých e-shopů vedle sebe, takže hned vidíte, kde je konkrétní délka lyží nebo číslo boty skladem. Nakupujete pak přímo v obchodě, který si zvolíte. '
          'Níže najdete stručnou historii značky, přehled řad, rady k délkám a velikostem a postup, jak porovnat nabídky na stejný model z různých sezón.</p>',
    guide='<h2>Rodinná firma z Horních Rakous</h2>'
          '<p>Firmu založil v roce 1924 Josef Fischer v hornorakouském městě Ried im Innkreis. Začínal jako kolář a truhlář, vyráběl vozíky a sáně a brzy k nim přidal dřevěné lyže. Po druhé světové válce do podniku nastoupil jeho syn Josef Fischer mladší a výroba se postupně zmechanizovala. Fischer Sports je dodnes rodinná firma se sídlem v Riedu. Kromě sjezdových lyží je silný hlavně v běžeckém lyžování a vyrábí také hokejky, brusle a další hokejové vybavení.</p>'
          '<p>Jméno Fischer ovšem nosí víc nesouvisejících značek. Městské cyklistické přilby Fischer Urban a Urban Plus, které v katalogu také najdete, pocházejí od německé společnosti MTS Group, která pod názvem Fischer prodává kola a cyklistické doplňky. Montážní pěny, úhelníky a háky zase vyrábí německý výrobce upevňovací techniky fischer. Nic z toho s lyžemi z Riedu nesouvisí, proto u neznámého produktu vždy zkontrolujte, o jakého výrobce jde.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější skupinou jsou <a href="/lyzarske-boty/">lyžařské boty</a>, následují běžky a <a href="/bezecke-boty/">boty na běžecké lyžování</a>. Velký podíl mají <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyze-komplety/">komplety lyží s vázáním</a> a <a href="/detske-lyze/">dětské lyže</a>. Obchody pod značkou vedou i lyžařské bundy a kalhoty, softshelly, mikiny a <a href="/lyzarske-hole/">lyžařské hole</a>. Hokejová část zahrnuje <a href="/hokejky/">hokejky</a>, <a href="/hokejove-tasky/">hokejové tašky</a>, čepele a brankářské vybavení. Menší skupiny tvoří <a href="/skialpove-boty/">skialpové boty</a>, vázání na běžky a vosky.</p>'
          + T(['Řada', 'Typ', 'Pro koho'], [
              ['The Curv', 'sjezdové lyže na upravené sjezdovky', 'rekreační a pokročilí lyžaři'],
              ['RC4', 'závodně laděné sjezdové lyže i lyžařské boty', 'technicky zdatní lyžaři, mládež v závodních oddílech'],
              ['Ranger, Transalp', 'freeride a skialpinismus, lyže i boty', 'terén mimo sjezdovky, výstupy'],
              ['Twin Skin, Crown', 'klasické běžky se stoupacími pásky nebo šupinami', 'rekreační běžkaři bez mazání'],
              ['Speedmax, Carbonlite, Aerolite', 'závodní a sportovní běžky na klasiku i bruslení', 'výkonnostní běžkaři'],
              ['RC One, W-series', 'kompozitové a dřevěné hokejky', 'hráči od dětí po dospělé']]) +
          '<h2>Běžky: šupiny, pásky, nebo vosk</h2>'
          '<p>Na klasiku potřebujete pod vázáním odrazovou zónu, která lyži při odrazu zabrzdí. Řada Crown má v této zóně vyfrézované šupiny, které fungují bez mazání a hodí se hlavně na méně ideální sníh kolem nuly. Twin Skin má místo šupin dva pásy umělé nebo mohérové kožešiny. Ty drží lépe a jsou tišší, jen je potřeba je občas vyčistit a ošetřit sprejem. Klasické lyže bez šupin a pásků se mažou stoupacím voskem podle teploty a jsou určené zkušenějším běžkařům. Na bruslení slouží kratší a tužší lyže řady Skate, které odrazovou zónu nemají.</p>'
          '<p>U běžek nevybírejte jen podle výšky. Rozhodující je tuhost lyže vzhledem k vaší hmotnosti, proto mají modely v názvu označení soft, medium nebo stiff a výrobce u každé délky uvádí rozsah váhy lyžaře. Pokud jste na hranici dvou kategorií, pro rekreační běh je vhodnější měkčí varianta, protože odraz pak funguje spolehlivěji.</p>'
          '<h2>Vázání a boty na běžky</h2>'
          '<p>Většina současných běžek Fischer má desku IFP, na kterou se nasouvá vázání Turnamic nebo rekreační Control Step-In. Tato vázání přijímají boty s podrážkou NNN, Prolink i Turnamic, takže starší boty s NNN obvykle použijete dál. Starší systém SNS Profil kompatibilní není. Boty na klasiku jsou měkčí a ohebné ve špičce, boty na bruslení mají pevnou manžetu kolem kotníku. Kombinované boty zvládnou obojí, ale v žádné technice nejsou nejlepší. Při zkoušení počítejte se silnější ponožkou a necháte si v botě zhruba prst místa před palcem.</p>'
          '<h2>Sjezdové lyže a lyžařské boty</h2>'
          '<p>Délku sjezdovek volte podle úrovně a stylu. Začátečníkovi stačí lyže zhruba po bradu, pokročilý lyžař na sjezdovce obvykle volí délku mezi nosem a čelem. Krátký poloměr oblouku znamená svižné krátké oblouky, delší poloměr klid ve vyšší rychlosti. Většina lyží se prodává jako komplet s vázáním, což usnadňuje nákup, protože vázání je k lyži napevno přizpůsobené.</p>'
          '<p>U lyžařských bot vám název napoví většinu parametrů. Číslo za názvem řady je index tuhosti, například 85 je měkčí bota pro rekreační jízdu a 130 tvrdá bota pro silného a zkušeného lyžaře. Zkratky LV, MV a HV označují šířku kopyta, tedy úzké, střední a široké. GW znamená podrážku GripWalk, která se lépe chodí, ale potřebuje kompatibilní vázání. Vacuum označuje skelet, který autorizovaný prodejce nahřeje a vytvaruje podle vaší nohy. Velikost se uvádí v mondopointu, tedy v centimetrech délky chodidla.</p>'
          '<ol><li>Změřte délku chodidla ve stoje a podle ní najděte mondopoint.</li>'
          '<li>Podle šířky nohy vyberte LV, MV nebo HV.</li>'
          '<li>Tuhost volte spíš nižší, pokud jezdíte pár dní v sezóně.</li>'
          '<li>Ověřte, že vázání podporuje podrážku boty, hlavně u GripWalk.</li></ol>'
          '<h2>Hokejky</h2>'
          '<p>Hokejky Fischer se dělí podle velikosti na SR, INT, JR a YTH. Kromě toho se liší flexem, tedy číslem udávajícím tuhost, a zahnutím čepele. Pro dítě volte nižší flex, jinak hokejku neprohne a střela bude slabá. Grip znamená pogumovaný povrch žerdi, který drží v rukavici. Pokud hokejku zkracujete, flex se zvýší. Podrobnější přehled je na stránce <a href="/fischer-hokejka/">hokejky Fischer</a>.</p>'
          '<h2>Oblečení a doplňky pod jménem Fischer</h2>'
          '<p>Obchody pod značkou Fischer nabízejí také <a href="/lyzarske-bundy/">lyžařské bundy</a> a kalhoty, softshellové a přechodové bundy, mikiny a čepice. U bund se v názvu často objevuje údaj o vodním sloupci membrány, například 20.000. Čím vyšší číslo, tím déle membrána odolá mokrému sněhu a dešti. Pro běžné lyžování v Alpách stačí střední hodnota, vyšší oceníte při jízdě v mokrém sněhu nebo mimo sjezdovky. Mezi doplňky patří vaky na lyže a boty, které se hodí na cestu autem i letadlem, a vosky na běžky i sjezdovky.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš tvrdé lyžařské boty pro rekreačního lyžaře. Noha je neovládne a jízda bolí.</li>'
          '<li>Běžky vybrané jen podle výšky bez ohledu na váhu. Odraz pak neklouže nebo nedrží.</li>'
          '<li>Lyžařské boty o číslo větší „na ponožky“. Bota se v ní hýbe a lyže reagují pozdě.</li>'
          '<li>Nové vázání na běžky bez kontroly podrážky staré boty.</li>'
          '<li>Dětská výbava na dvě sezóny dopředu. Příliš dlouhé lyže a velké boty dítěti učení zkomplikují.</li></ul>'
          '<p>U dětí se vyplatí zvážit bazar nebo půjčovnu na celou sezónu, protože noha roste rychle. Pokud kupujete nové, sledujte hlavně dětské komplety lyží s vázáním, kde je výběr délek nejširší.</p>'
          '<h2>Péče o lyže a boty</h2>'
          '<ul><li>Skluznici sjezdovek i běžek pravidelně voskujte, suchá skluznice zpomaluje a rychleji se poškodí.</li>'
          '<li>Stoupací pásky Twin Skin čistěte speciálním čističem, nikdy je nemažte skluzným voskem.</li>'
          '<li>Lyžařské boty sušte s vyjmutou vložkou při pokojové teplotě, ne na radiátoru.</li>'
          '<li>Přes léto nechte přezky lyžáků lehce zapnuté, aby skelet držel tvar.</li>'
          '<li>Hrany po sezóně nechte nabrousit a lyže uskladněte v suchu.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Fischer každou sezónu mění grafiku a občas i konstrukci, ale stejný model se v obchodech prodává několik let vedle sebe. Proto u každé nabídky zkontrolujte rok kolekce, délku, typ vázání a u bot šířku kopyta. Starší ročník bývá levnější a jízdní vlastnosti mívá podobné. Na běžky se vyplatí koukat už na podzim, než se rozeberou běžné délky. Další výběr najdete na stránkách <a href="/fischer-lyze/">lyže Fischer</a>, <a href="/bezky-fischer/">běžky Fischer</a> a <a href="/boty-na-bezky-fischer/">boty na běžky Fischer</a>. Pro srovnání stojí za pohled i lyže značek '
          + B(('rossignol', 'Rossignol'), ('head', 'Head'), ('salomon', 'Salomon')) +
          ', u hokeje '
          + B(('bauer', 'Bauer'), ('ccm', 'CCM')) + '.</p>',
    faq=[
        ('Odkud pochází značka Fischer?',
         'Lyžařský Fischer je rakouská rodinná firma, kterou v roce 1924 založil Josef Fischer v Riedu im Innkreis v Horních Rakousích. Sídlí tam dodnes.'),
        ('Je cyklistická přilba Fischer od stejné firmy jako lyže?',
         'Ne. Přilby Fischer Urban a Urban Plus prodává německá společnost MTS Group pod svou cyklistickou značkou Fischer. S rakouským výrobcem lyží nesouvisí.'),
        ('Jaký je rozdíl mezi běžkami Twin Skin a Crown?',
         'Twin Skin má pod vázáním pásy kožešiny, které dobře drží a jsou tiché. Crown má šupiny vyfrézované do skluznice. Obojí funguje bez stoupacího vosku.'),
        ('Jakou délku běžek Fischer zvolit?',
         'Hlavní je hmotnost, ne výška. Výrobce u každé délky a tuhosti uvádí rozsah váhy lyžaře, podle něj vybírejte. Délka pak vychází z výšky a stylu.'),
        ('Pasují moje staré boty NNN do vázání Turnamic?',
         'Ano, vázání Turnamic a Control Step-In na deskách IFP přijímají podrážky NNN, Prolink i Turnamic. Boty se systémem SNS Profil do nich nepasují.'),
        ('Co znamenají zkratky MV, HV a GW u lyžáků Fischer?',
         'MV a HV jsou střední a široké kopyto, LV úzké. GW je podrážka GripWalk, se kterou se lépe chodí, ale vázání ji musí podporovat.'),
        ('Co je technologie Vacuum?',
         'Skelet lyžařské boty z materiálu, který prodejce nahřeje a pomocí tlaku vytvaruje podle nohy. Úprava se dělá u autorizovaného prodejce.'),
        ('Jak vybrat hokejku Fischer pro dítě?',
         'Podle velikosti YTH nebo JR a s nízkým flexem, aby ji dítě dokázalo prohnout. Délka má po postavení na brusle sahat zhruba k bradě.'),
        ('Kdy jsou lyže Fischer nejlevnější?',
         'Obvykle na konci zimy a na jaře, kdy obchody doprodávají ročník. Starší kolekce mívá stejné jízdní vlastnosti a liší se hlavně grafikou.'),
        ('Prodává sporteka.cz lyže Fischer přímo?',
         'Ne. Sporteka porovnává nabídky českých e-shopů a odkazuje na ně. Objednávku, montáž vázání i případnou reklamaci řešíte s obchodem.'),
    ],
)

# ------------------------------------------------------------------ garmin
NEW['garmin'] = dict(
    title='Garmin: sportovní hodinky, cyklopočítače a radary',
    desc='Garmin v katalogu: hodinky Forerunner, Fenix, Venu a Instinct, cyklopočítače Edge, radary Varia, golfové Approach i sonary. Jak vybrat a srovnat nabídky.',
    intro='<p>Garmin je americký výrobce navigací, který se v posledních dvaceti letech stal jedním z hlavních jmen ve sportovní elektronice. Lidé u nás hledají hlavně <a href="/sportovni-hodinky/">sportovní hodinky</a> s GPS, ale firma vyrábí i cyklopočítače, zadní radary na kolo, golfové hodinky, potápěčské počítače, satelitní komunikátory a rybářské sonary. '
          'Sporteka.cz u každého modelu sbírá nabídky českých obchodů, takže porovnáte, kde je hodinky v požadované velikosti pouzdra a barvě skutečně možné koupit. Objednávka pak proběhne v e-shopu, který si vyberete. Elektronika se navíc často liší jen drobností v názvu, například velikostí pouzdra, typem displeje nebo safírovým sklem, a právě to rozhoduje o ceně i o tom, zda vám hodinky budou vyhovovat. '
          'Níže najdete přehled řad hodinek a cyklopočítačů, vysvětlení rozdílů mezi verzemi a rady, na co si dát pozor, když stejný model prodává více obchodů.</p>',
    guide='<h2>Od navigací k hodinkám</h2>'
          '<p>Firmu založili v roce 1989 Gary Burrell a Min Kao, zpočátku pod názvem ProNav. Název Garmin vznikl spojením jejich křestních jmen. Prvními výrobky byly navigační přístroje pro letectví, lodě a později auta. Od roku 1996 sídlí americká centrála v Olathe ve státě Kansas, právně je společnost od roku 2010 registrovaná ve švýcarském Schaffhausenu.</p>'
          '<p>Do sportu Garmin vstoupil v roce 2003 modelem Forerunner 201, který firma uvádí jako první GPS trenažér na zápěstí. Od té doby se řada Forerunner stala synonymem běžeckých hodinek. V roce 2019 Garmin koupil nizozemskou firmu Tacx, výrobce cyklistických trenažérů, a jeho chytré trenažéry se dnes prodávají pod oběma jmény.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Největší skupinou jsou sportovní a <a href="/chytre-hodinky/">chytré hodinky</a>. Druhou velkou oblastí je cyklistika: <a href="/cyklo-computery/">cyklopočítače</a> Edge, držáky, snímače rychlosti a kadence, hrudní pásy, radary a <a href="/cyklo-svetla/">cyklistická světla</a> Varia. Golfisté najdou hodinky a dálkoměry Approach mezi <a href="/golfove-doplnky/">golfovými doplňky</a>, rybáři sonary a mapové plottery Striker a Echomap v kategorii <a href="/rybarske-lode-a-elektronika/">rybářská elektronika</a>. Menší zastoupení mají potápěčské počítače Descent, satelitní komunikátory inReach, trenažéry Tacx a chytrá váha Index.</p>'
          + T(['Řada', 'Zaměření', 'Pro koho'], [
              ['Forerunner', 'běžecké a triatlonové hodinky', 'od začínajících běžců po závodníky'],
              ['Fenix, Enduro', 'odolné multisportovní hodinky s mapami', 'hory, ultra, outdoor'],
              ['Instinct', 'robustní hodinky, často se solárním dobíjením', 'outdoor, práce venku'],
              ['Venu, Vivoactive', 'chytré hodinky s fitness funkcemi', 'každodenní nošení, posilovna'],
              ['Edge', 'cyklopočítače s GPS a navigací', 'silnice, gravel, MTB'],
              ['Varia', 'zadní radary a světla na kolo', 'jízda v provozu'],
              ['Approach', 'golfové hodinky a dálkoměry', 'golfisté'],
              ['Descent', 'potápěčské počítače', 'potápěči']]) +
          '<h2>Jak vybrat hodinky</h2>'
          '<p>Nejdřív si ujasněte, k čemu je chcete. Pro běh a občasné kolo stačí levnější Forerunner, který měří tempo, vzdálenost a tep ze zápěstí. Vyšší modely Forerunner přidávají mapy, měření síly běhu a delší výdrž. Fenix je těžší a odolnější, má kovové nebo titanové pouzdro, mapy a hodí se na hory a vícedenní akce. Venu a Vivoactive jsou spíš chytré hodinky do města s velkým barevným displejem a sportovními profily. Instinct je jednodušší, ale velmi odolný a u solárních verzí vydrží dlouho bez nabíječky.</p>'
          '<p>Rozhodující je také displej. AMOLED je jasný a barevný, ale baterii vybíjí rychleji, zvlášť když je trvale zapnutý. Transflektivní displej je na slunci dobře čitelný a hodinky s ním vydrží déle. Velikost pouzdra, například 42, 47 nebo 51 mm, ovlivní pohodlí i kapacitu baterie. Na útlé zápěstí vybírejte menší pouzdro, větší sedí lépe na široké ruce a vydrží déle.</p>'
          '<ol><li>Vyberte řadu podle sportu a toho, jak často hodinky nosíte.</li>'
          '<li>Rozhodněte se mezi AMOLED a úspornějším displejem.</li>'
          '<li>Zvolte velikost pouzdra podle zápěstí.</li>'
          '<li>Ověřte doplňky v názvu: Pro, Sapphire, Solar, Music nebo inReach.</li></ol>'
          '<h2>Co znamenají přídomky v názvu</h2>'
          '<p>Stejná řada se prodává v několika verzích a právě v nich se nabídky obchodů nejčastěji liší. Sapphire označuje safírové sklíčko, které je odolnější proti poškrábání. Solar má solární dobíjení, které prodlouží výdrž. Music umí ukládat hudbu a přehrávat ji do sluchátek bez telefonu. inReach u nejvyšších modelů Fenix znamená satelitní komunikaci a možnost odeslat zprávu i mimo signál mobilní sítě. Pro na konci názvu obvykle přidává svítilnu, rozšířené mapy nebo jiné prémiové funkce. Číslo generace odlišuje novější model od staršího, například Fenix 8 a Fenix 9.</p>'
          '<h2>Cyklopočítače a radary</h2>'
          '<p>Edge se liší velikostí displeje, výdrží a mapami. Menší modely ukazují hlavně data, větší zvládnou navigaci po trase s mapou a odbočkami. Verze s přídomkem bundle obsahují v balení i snímače, například hrudní pás nebo snímač rychlosti a kadence. Zadní radar Varia se montuje na sedlovku a upozorňuje na auta, která se blíží zezadu. Varování se zobrazí na cyklopočítači, na hodinkách nebo v telefonu. Radar ale nenahrazuje pozornost a ohleduplnou jízdu. Na <a href="/cyklo-riditka/">řídítka</a> se počítač připevní držákem, který bývá v balení, předsazené držáky se prodávají zvlášť mezi <a href="/cyklo-prislusenstvi/">cyklo příslušenstvím</a>.</p>'
          '<h2>Výdrž baterie v praxi</h2>'
          '<p>Údaje o výdrži uvádí výrobce zvlášť pro režim hodinek a pro záznam aktivity s GPS. Skutečná výdrž závisí na tom, jak často používáte GPS, zda máte zapnutý displej trvale, posloucháte hudbu nebo měříte tep a saturaci i v noci. Multipásmový příjem GPS je přesnější mezi budovami a v lese, ale spotřebuje víc energie. Pokud plánujete vícedenní akci bez nabíjení, vybírejte model s delší výdrží, solární verzi nebo si přibalte <a href="/powerbanky-a-nabijeni/">powerbanku</a>.</p>'
          '<h2>Snímače a kompatibilita</h2>'
          '<p>Hodinky a cyklopočítače Garmin komunikují se snímači přes ANT+ a Bluetooth. Ke stejným hodinkám tak připojíte hrudní pás, snímač kadence, wattmetr nebo chytrý trenažér. Hrudní pás měří tep přesněji než optický snímač na zápěstí, hlavně při intervalech a v zimě. Data se ukládají do aplikace Garmin Connect, odkud je můžete posílat i do dalších tréninkových služeb. Ověřte, že váš telefon aplikaci podporuje, zejména u starších zařízení.</p>'
          '<h2>Golf, voda a rybaření</h2>'
          '<p>Golfové hodinky Approach ukazují vzdálenost na green a k překážkám na mapách hřišť. Dálkoměry a monitory odpalu doplňují trénink na driving range. Řada Descent je určená potápěčům a funguje jako potápěčský počítač. Pro rybáře nabízí Garmin sonary Striker, které ukazují dno, hloubku a ryby pod lodí, a kombinované plottery Echomap s mapou. U sonarů sledujte, zda je v balení sonda a jaký typ zobrazení podporuje.</p>'
          '<h2>Trenažéry Tacx a dětské hodinky</h2>'
          '<p>Chytré trenažéry Tacx promění silniční kolo v domácí trenažér. Modely s přímým převodem se nasazují místo zadního kola, takže odpadá opotřebení pláště a jízda je tišší. Trenažér sám nastavuje odpor podle tréninkového programu nebo virtuální trasy a spojí se s hodinkami, cyklopočítačem i aplikacemi v počítači. Před nákupem ověřte, zda trenažér pasuje k typu osy a počtu převodů vašeho kola. V katalogu jsou také dětské chytré hodinky Bounce. Jejich hlavní funkce stojí na mobilním připojení, proto si před koupí zjistěte, zda příslušná služba funguje v Česku.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě nejvyššího modelu kvůli funkcím, které nikdy nepoužijete.</li>'
          '<li>Velké pouzdro na útlé zápěstí. Hodinky se pak hýbou a optické měření tepu je méně přesné.</li>'
          '<li>Záměna generací, například staršího modelu za novější, protože vypadají podobně.</li>'
          '<li>Cyklopočítač bez snímačů, když chcete měřit kadenci nebo tep.</li></ul>'
          '<h2>Měření zdraví není lékařské vyšetření</h2>'
          '<p>Hodinky Garmin měří tep, spánek, úroveň stresu nebo saturaci kyslíkem. Tato čísla slouží jako orientace pro trénink a nejsou lékařskou diagnózou. Hodinky nejsou zdravotnický prostředek. Pokud máte zdravotní potíže nebo vám měření ukazuje neobvyklé hodnoty, obraťte se na lékaře.</p>'
          '<h2>Péče a provoz</h2>'
          '<ul><li>Po plavání v chlorované nebo slané vodě opláchněte hodinky čistou vodou.</li>'
          '<li>Silikonový řemínek občas umyjte mýdlem, pot a krém zanechávají usazeniny.</li>'
          '<li>Aktualizujte software přes aplikaci Garmin Connect, opravy přicházejí často.</li>'
          '<li>Nabíjejte originálním kabelem, kontakty udržujte suché a čisté.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>U elektroniky se vyplatí kontrolovat celé označení modelu, nejen řadu. Jeden obchod může nabízet Fenix 8 AMOLED ve velikosti 47 mm, jiný stejnou cenovou hladinu se solární verzí 51 mm. Ověřte i barvu pouzdra a řemínku a to, zda jde o českou distribuci s českým menu. Novou generaci obvykle doprovází pokles ceny té předchozí, proto se vyplatí porovnat obě. Srovnání nabízejí také hodinky Polar, Suunto a Coros. Pro triatlonisty je užitečná kategorie <a href="/triatlon/">triatlon</a>, pro domácí trénink <a href="/kardio-trenazery/">kardio trenažéry</a>.</p>',
    faq=[
        ('Odkud pochází Garmin?',
         'Firmu založili v roce 1989 v Kansasu Gary Burrell a Min Kao. Americká centrála je v Olathe, právně je společnost registrovaná ve Švýcarsku.'),
        ('Jaký je rozdíl mezi Garmin Forerunner a Fenix?',
         'Forerunner je lehčí, zaměřený na běh a trénink. Fenix je odolnější multisportovní model s kovovým pouzdrem, mapami a delší výdrží na hory.'),
        ('Které hodinky Garmin jsou vhodné pro začátečníka?',
         'Nižší modely Forerunner, například řada 55 až 170, měří tempo, vzdálenost a tep a nabízejí tréninkové plány. Pro začátek běhu stačí.'),
        ('Co znamená AMOLED u hodinek Garmin?',
         'Barevný a velmi jasný displej. Je dobře čitelný, ale spotřebuje víc energie, zvlášť pokud ho necháte trvale zapnutý.'),
        ('Co je Garmin Varia?',
         'Řada světel a zadních radarů na kolo. Radar upozorní na vozidla blížící se zezadu, varování se zobrazí na cyklopočítači nebo hodinkách.'),
        ('Co obsahuje balení Edge bundle?',
         'Kromě cyklopočítače i snímače, obvykle hrudní pás a snímač rychlosti nebo kadence. Přesný obsah se liší podle modelu, ověřte ho v popisu.'),
        ('Jsou hodinky Garmin vodotěsné?',
         'Většina sportovních modelů vydrží plavání, ale odolnost se liší. Údaj v ATM nebo metrech najdete u konkrétního modelu, potápění zvládá řada Descent.'),
        ('Je měření tepu a spánku na Garminu lékařsky přesné?',
         'Ne. Jde o orientační údaje pro trénink, hodinky nejsou zdravotnický prostředek. Při zdravotních potížích se poraďte s lékařem.'),
        ('Kdy zlevňují hodinky Garmin?',
         'Typicky po uvedení nové generace a při velkých výprodejích. Starší generace pak často nabízí většinu funkcí za nižší cenu a dál dostává aktualizace softwaru.'),
        ('Prodává sporteka.cz hodinky Garmin?',
         'Ne. Sporteka ukazuje nabídky českých obchodů na jednom místě, nákup, záruku i servis řešíte s vybraným e-shopem.'),
    ],
)

# ------------------------------------------------------------------ birkenstock
NEW['birkenstock'] = dict(
    title='Birkenstock: pantofle Arizona, Boston, sandály Gizeh',
    desc='Birkenstock v katalogu: pantofle Arizona a Madrid, nazouváky Boston, sandály Gizeh a Milano, modely z EVA i dětské. Šířky, velikosti a péče o korek.',
    intro='<p>Birkenstock je německá značka obuvi, kterou poznáte podle tvarovaného korkového stélku a výrazných přezek. Pantofle, které kdysi nosili hlavně lékaři, zdravotní sestry a lidé hledající pohodlí, se během posledních let staly běžnou součástí městského šatníku. Nejhledanější jsou pantofle Arizona se dvěma pásky, uzavřené nazouváky Boston a žabky Gizeh. Nabídka ale zahrnuje i sandály pro děti, lehké modely z EVA, pracovní obuv Super Birki a v posledních letech i tenisky. '
          'Na této stránce sporteka.cz porovnává nabídky českých e-shopů, aby bylo vidět, kde je konkrétní model ve vaší velikosti a šířce skladem. Objednáte pak přímo v obchodě. Pozor na rozdíly: stejný model se vyrábí v několika materiálech a ve dvou šířkách, takže dvě nabídky se stejným názvem nemusí znamenat stejnou botu. '
          'Pod úvodem najdete stručnou historii, vysvětlení rozdílu mezi šířkou regular a narrow, rady k materiálům a péči a tipy, jak srovnat nabídky na stejný model.</p>',
    guide='<h2>Ševcovská tradice od roku 1774</h2>'
          '<p>Rodina Birkenstocků odvozuje svou tradici od Johanna Adama Birkenstocka, který je v roce 1774 zapsán v církevních záznamech hesenské vesnice Langen-Bergheim jako švec. Skutečný základ dnešní značky však vznikl až ve dvacátém století, kdy se rodina zaměřila na tvarované vložky do bot. V roce 1963 uvedl Karl Birkenstock na trh první sandál s hlubokým a pružným stélkem, který se od roku 1979 prodává pod názvem Madrid. Z něj se postupně vyvinuly modely Arizona, Boston, Gizeh nebo Milano.</p>'
          '<p>Od roku 2021 má ve firmě většinový podíl investiční společnost L Catterton, v roce 2023 vstoupila skupina Birkenstock na newyorskou burzu. Výroba se i nadále soustředí hlavně v Německu.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Zdaleka největší skupinou jsou <a href="/pantofle-a-zabky/">pantofle a žabky</a>, kam obchody řadí Arizonu, Madrid, Gizeh i nazouváky Boston. Následují <a href="/tenisky/">tenisky</a>, i když pod tímto označením obchody často nabízejí i sandály. Skutečnými teniskami jsou například modely Bend Low. Další velkou skupinou jsou <a href="/sandaly/">sandály</a> s páskem za patou, jako Milano nebo dětský Mogami. Malou část tvoří holinky, ponožky a obuv do bazénu z EVA. Přehledy najdete i na stránkách <a href="/birkenstock-pantofle/">pantofle Birkenstock</a> a <a href="/birkenstock-sandaly/">sandály Birkenstock</a>.</p>'
          + T(['Model', 'Typ', 'K čemu'], [
              ['Arizona', 'pantofle se dvěma nastavitelnými pásky', 'léto, domov, město'],
              ['Madrid', 'pantofle s jedním páskem', 'nejjednodušší původní tvar'],
              ['Boston', 'uzavřený nazouvák, verze s kožešinou Shearling', 'přechodné období, domov'],
              ['Gizeh', 'žabky s páskem mezi prsty', 'léto, k vodě v provedení EVA'],
              ['Milano, Mogami', 'sandály s páskem za patou', 'delší chůze, děti'],
              ['Super Birki', 'pracovní nazouvák z polyuretanu', 'kuchyně, nemocnice, dílna']]) +
          '<h2>Stélka: korek, latex a semiš</h2>'
          '<p>Typický stélek Birkenstock je z přírodního korku a latexu, zespodu doplněný jutou a shora potažený semišem. Je tvarovaný s vyvýšením pod podélnou klenbou, příčnou klenbou a hlubokým lůžkem pro patu. Při nošení se korek postupně přizpůsobí tvaru chodidla. První dva až tři týdny proto mohou být nové pantofle tvrdé a je rozumné je nosit postupně. Varianty se změkčeným stélkem mají pod semišem navíc vrstvu pěny a jsou pohodlnější hned od začátku.</p>'
          '<p>Stélek není zdravotní pomůcka a nenahradí vložky na míru. Lidé s ortopedickými potížemi, cukrovkou nebo bolestmi nohou by se měli o vhodné obuvi poradit s lékařem nebo ortopedem.</p>'
          '<h2>Materiály svršku</h2>'
          '<p>Birko-Flor je syntetický materiál, který používá jen Birkenstock. Je odolný, dobře se čistí a drží tvar. Birkibuc vypadá jako nubuk, ale je to také syntetika. Přírodní kůže a semiš jsou příjemnější a časem se tvarují, ale potřebují víc péče. Modely z EVA jsou z jednoho kusu lehké pěny, nebojí se vody a hodí se k bazénu nebo na pláž. Vegan verze jsou vyrobené bez materiálů živočišného původu.</p>'
          '<h2>Šířka regular, nebo narrow</h2>'
          '<p>Většina modelů se vyrábí ve dvou šířkách. Regular je určená pro normální až širší nohu, narrow pro užší nohu. Na stélku je šířka vyznačená symbolem chodidla: u narrow je plný, u regular jen obrys. Délka je u obou šířek stejná, proto při nevhodném pocitu nejdřív zkuste druhou šířku a teprve potom jiné číslo.</p>'
          '<ol><li>Změřte chodidlo ve stoje, nejlépe odpoledne.</li>'
          '<li>K délce připočtěte asi centimetr, prsty nemají dosahovat na okraj stélku.</li>'
          '<li>Pata má sedět v lůžku, ne přesahovat přes okraj.</li>'
          '<li>Při úzké noze hledejte v názvu narrow nebo úzký střih.</li></ol>'
          '<p>Velikost se uvádí v evropských číslech. Půlčísla se běžně nevyrábějí, proto pokud jste mezi dvěma velikostmi, zkuste u pantoflí spíš větší číslo, aby prsty měly místo.</p>'
          '<h2>Boston a modely na chladnější dny</h2>'
          '<p>Uzavřený nazouvák Boston kryje prsty a hodí se na podzim, na jaře i jako domácí obuv. Verze Shearling má stélek potažený ovčí vlnou nebo umělou kožešinou a je teplejší. Boston ze semiše nebo nubuku vypadá elegantněji, ale bojí se vody a soli. V katalogu jsou i vyšší modely, holinky a zimní boty, které tvoří jen malou část nabídky. Boston se kupuje spíš přesně na délku, protože uzavřená špička nedovolí prstům přesahovat.</p>'
          '<h2>Tenisky a pracovní obuv</h2>'
          '<p>Tenisky Bend Low mají plochou podrážku a vyjímatelnou stélku a nosí se jako běžná městská obuv. Neočekávejte od nich korkový stélek jako u pantoflí. Super Birki je uzavřený nazouvák z polyuretanu s vyjímatelnou stélkou, který se používá v kuchyních, nemocnicích a laboratořích. Snadno se omývá a podrážka je protiskluzová. Před nákupem do práce ověřte, zda splňuje požadavky vašeho zaměstnavatele na pracovní obuv.</p>'
          '<h2>Dětské Birkenstocky</h2>'
          '<p>Dětské modely mají stejný tvarovaný stélek, jen menší. U malých dětí jsou praktičtější sandály s páskem za patou, například Milano nebo Mogami, protože pantofle Arizona z nohy snadno spadnou. Velikost kontrolujte každou sezónu. Prsty nesmějí přesahovat přes okraj stélku a pata má sedět v lůžku. Pro dětskou letní obuv nabízí víc možností i kategorie <a href="/detske-sportovni-sandaly/">dětské sandály</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Volba menšího čísla, aby pantofle „neplandaly“. Prsty pak tlačí na okraj korku a ten se rychle opotřebuje.</li>'
          '<li>Koupě korkových pantoflí k bazénu místo modelu z EVA.</li>'
          '<li>Sušení mokrého stélku u topení.</li>'
          '<li>Záměna šířky narrow a regular, když se dvě nabídky liší jen kódem.</li></ul>'
          '<h2>Nákup online bez zkoušení</h2>'
          '<p>Pantofle Birkenstock se nejčastěji kupují bez vyzkoušení, a proto se vyplatí připravit si údaje předem. Pokud už nějaké Birkenstocky máte, podívejte se na stélek: najdete tam číslo velikosti a symbol šířky. Stejné číslo a šířka obvykle sednou i u jiného modelu se stejným stélkem. U modelů s měkčím stélkem, u tenisek a u Bostonu se pocit může lišit. Ověřte také, zda obchod umožňuje výměnu velikosti a kdo platí dopravu při vrácení. Pantofle při zkoušení noste jen doma na čisté podlaze, aby se daly vrátit.</p>'
          '<h2>Kdy se nabídka mění</h2>'
          '<p>Letní barvy a materiály přicházejí na jaře a během léta se rychle rozebírají běžné velikosti. Podzimní kolekce přináší Boston, verze s kožešinou a tmavší barvy. Klasické modely jako Arizona v černé nebo hnědé barvě se prodávají celoročně a jejich cena se mění méně než u sezónních barev. Kdo nespěchá, může sledovat cenu konkrétní varianty a nakoupit mimo hlavní sezónu, typicky na podzim u letních modelů a na jaře u Bostonu s kožešinou.</p>'
          '<h2>Péče o korek a kůži</h2>'
          '<ul><li>Okraj korku po čase ztratí lesk a začne se drolit. Ošetřete ho prostředkem na korek, který výrobce i obchody nabízejí.</li>'
          '<li>Nenechávejte pantofle na slunci za oknem auta ani u topení, korek se může zkroutit.</li>'
          '<li>Semišový stélek otřete vlhkým hadříkem a nechte volně vyschnout.</li>'
          '<li>Kožený svršek ošetřete krémem, semiš kartáčem a <a href="/impregnace/">impregnací</a>.</li>'
          '<li>Modely z EVA stačí umýt vlažnou vodou s mýdlem.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>Stejné jméno modelu skrývá různé materiály, barvy a šířky. Arizona z Birko-Floru, ze semiše, z nubuku a z EVA jsou čtyři odlišné produkty s jinou cenou i životností. U každé nabídky proto ověřte materiál svršku, šířku, typ stélku a velikost. Letní modely bývají nejdražší od dubna do července, nazouváky Boston se kupují hlavně na podzim. Podobné pantofle a sandály najdete i u značek '
          + B(('rieker', 'Rieker'), ('geox', 'Geox'), ('crocs', 'Crocs')) +
          '. Další výběr nabízejí <a href="/damske-pantofle/">dámské pantofle</a>, <a href="/panske-pantofle/">pánské pantofle</a> a <a href="/domaci-pantofle/">domácí pantofle</a>.</p>',
    faq=[
        ('Odkud pochází značka Birkenstock?',
         'Z Německa. Rodina se hlásí k ševcovské tradici od roku 1774, první sandál s tvarovaným stélkem uvedl Karl Birkenstock v roce 1963.'),
        ('Jaký je rozdíl mezi šířkou regular a narrow?',
         'Regular je pro normální a širší nohu, narrow pro užší. Délka je stejná. Na stélku poznáte narrow podle plného symbolu chodidla.'),
        ('Jakou velikost Birkenstock zvolit, když jsem mezi čísly?',
         'Půlčísla se běžně nevyrábějí. U pantoflí obvykle sedne spíš větší číslo, aby prsty nedosahovaly na okraj stélku.'),
        ('Proč jsou nové pantofle Birkenstock tvrdé?',
         'Korkový stélek se teprve tvaruje podle chodidla, obvykle dva až tři týdny. Pokud chcete pohodlí hned, hledejte variantu se změkčeným stélkem.'),
        ('Co je Birko-Flor?',
         'Syntetický materiál svršku, který používá jen Birkenstock. Je odolný a snadno se čistí, ale nepřizpůsobí se noze jako přírodní kůže.'),
        ('Můžu pantofle Birkenstock nosit do vody?',
         'Korkové modely ne, voda stélku škodí. Na pláž a k bazénu jsou určené modely z EVA, které jsou lehké a nevadí jim mokro.'),
        ('Jsou Birkenstocky zdravotní obuv?',
         'Ne. Tvarovaný stélek je pohodlný, ale nejde o zdravotní pomůcku. S ortopedickými potížemi se poraďte s lékařem nebo ortopedem.'),
        ('Jak ošetřit korek u Birkenstocků?',
         'Když okraj korku ztratí lesk, natřete ho prostředkem na korek. Pantofle nesušte u topení a nenechávejte je na přímém slunci.'),
        ('Má Birkenstock i dětské modely?',
         'Ano, například Arizona, Milano nebo Mogami v dětských velikostech. Sandály s páskem za patou drží na noze lépe než pantofle, proto se pro menší děti hodí víc. Velikost kontrolujte na začátku každé sezóny, noha roste rychle.'),
        ('Prodává sporteka.cz boty Birkenstock?',
         'Ne. Sporteka porovnává nabídky českých e-shopů, nákup, výměnu velikosti i vrácení řešíte přímo s vybraným obchodem. Před objednávkou si u něj ověřte podmínky dopravy a vrácení zboží.'),
    ],
)

# ------------------------------------------------------------------ tamaris
NEW['tamaris'] = dict(
    title='Tamaris: dámské tenisky, sandály, kotníkové a zimní boty',
    desc='Tamaris v katalogu: dámské tenisky, kotníkové a zimní boty, sandály, nazouváky i trekové boty s Gore-Tex. Velikosti, šířky a jak srovnat nabídky obchodů.',
    intro='<p>Tamaris je německá značka dámské obuvi, kterou v Česku najdete v mnoha obchodních centrech i e-shopech. Prodává tenisky, kotníkové boty, sandály, nazouváky, zimní boty a v posledních sezónách i lehké trekové boty. Většina kolekce je určená na každý den do města a do práce, ne na sport. Kolekce se obměňuje každou sezónu a sleduje módní trendy, proto se stejný tvar boty často objevuje v několika barvách a materiálech a zároveň rychle mizí z nabídky. Velkou výhodou je číselný kód modelu, podle kterého dohledáte stejnou botu u různých prodejců. '
          'Sporteka.cz zařadila značku do srovnání, protože se u ní často vyplatí porovnat nabídky: stejný model prodává více obchodů v různých barvách a s rozdílnou dostupností velikostí. U každého páru vidíte, kde je vaše číslo skladem, a objednáváte přímo v obchodě. '
          'Níže najdete původ značky, přehled sortimentu, vysvětlení číselného označení modelů a rady k velikostem a péči.</p>',
    guide='<h2>Z Detmoldu do celé Evropy</h2>'
          '<p>Tamaris patří do skupiny Wortmann, kterou v roce 1967 založil Horst Wortmann v severoněmeckém Detmoldu. Firma je dodnes rodinná, od roku 2016 ji operativně vede synovec zakladatele Jens Beining. Do stejné skupiny patří i značky Marco Tozzi, Caprice a Jana, které mají podobný styl a často se prodávají ve stejných obchodech. Tamaris je z nich nejznámější a má vlastní síť prodejen po Evropě.</p>'
          '<p>Skupina boty navrhuje a vývoj řídí z Německa, výroba však probíhá v závodech mimo Německo. Konkrétní zemi výroby najdete na štítku nebo v popisu produktu. V roce 2021 přidala značka kolekci Tamaris active zaměřenou na outdoor, odtud pocházejí trekové boty s membránou, které jsou v katalogu.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější skupinou jsou <a href="/tenisky/">tenisky</a>, kam obchody řadí nejen sportovní tenisky, ale i polobotky a kotníkové boty. Druhou velkou skupinou jsou <a href="/sandaly/">sandály</a> s plochou podrážkou, na klínku i na podpatku. Následují nazouváky a <a href="/pantofle-a-zabky/">pantofle</a>, <a href="/zimni-obuv/">zimní obuv</a> se zateplením a menší řada <a href="/trekova-obuv/">trekových bot</a> s membránou Gore-Tex. Dámské modely tvoří prakticky celý sortiment.</p>'
          + T(['Typ obuvi', 'Typické provedení', 'Kdy nosit'], [
              ['Tenisky', 'kůže, semiš nebo textil, často vyšší podrážka', 'město, práce, volný čas'],
              ['Kotníkové boty', 'kožené, na zip, s podpatkem i bez', 'podzim a jaro'],
              ['Sandály', 'ploché, na klínku nebo na podpatku', 'léto, společenské příležitosti'],
              ['Nazouváky a pantofle', 'kůže, textil, profilovaný stélek', 'léto, krátké pochůzky'],
              ['Zimní boty a sněhule', 'zateplení, protiskluzová podrážka', 'mráz a sníh ve městě'],
              ['Trekové boty active', 'nízké i kotníkové, Gore-Tex', 'vycházky a lehká turistika']]) +
          '<h2>Jak číst označení modelů</h2>'
          '<p>Tamaris pojmenovává většinu bot číselným kódem, například 1-23760-41. Prostřední pětimístné číslo určuje model, poslední dvojčíslí sezónu a za ním obchody často uvádějí kód barvy. Díky tomu dohledáte stejnou botu v různých e-shopech, i když každý obchod uvádí jiný název. Hledáte-li konkrétní pár, který jste viděli v prodejně, opište si kód z krabice nebo ze stélky.</p>'
          '<h2>Velikosti a šířka</h2>'
          '<p>Tamaris používá evropská čísla a půlčísla se u něj běžně nevyrábějí. Podle zkušeností obchodníků boty odpovídají obvyklé velikosti. Pokud jste přesně mezi dvěma čísly, zvolte spíš větší, zvlášť u zimních bot, kam si oblékáte silnější ponožku. Kolekce Comfort má pohodlnější šířku a vyjímatelnou stélku, takže do ní lze vložit vlastní vložku. Některé modely mají stélku Touch-it z paměťové pěny, která se přizpůsobí chodidlu.</p>'
          '<ol><li>Změřte chodidlo odpoledne, kdy je noha nejvíc rozšířená.</li>'
          '<li>K délce chodidla připočtěte asi centimetr a podle tabulky obchodu vyberte číslo.</li>'
          '<li>U kotníkových bot na podpatku vyzkoušejte chůzi do schodů, pata nemá vyklouzávat.</li>'
          '<li>Pokud nosíte vlastní vložky, hledejte model s vyjímatelnou stélkou.</li></ol>'
          '<p>Profilovaná stélka zvyšuje pohodlí, ale není zdravotní pomůckou. Pokud máte ortopedické potíže, poraďte se s lékařem, jaký typ obuvi nebo vložek je pro vás vhodný.</p>'
          '<h2>Výběr podle příležitosti</h2>'
          + T(['Příležitost', 'Co hledat', 'Na co si dát pozor'], [
              ['Kancelář', 'kožené polobotky, kotníkové boty s nízkým podpatkem', 'pohodlí při celodenním nošení'],
              ['Město a nákupy', 'tenisky, ploché sandály, mokasíny', 'tlumení a protiskluzová podrážka'],
              ['Svatba a večer', 'sandály a lodičky na podpatku', 'výška a šířka podpatku'],
              ['Zima ve městě', 'zateplené kotníkové boty a sněhule', 'vzorek podrážky a voděodolnost'],
              ['Výlet do přírody', 'nízké trekové boty s membránou', 'opora kotníku a pevnost podešve']]) +
          '<p>Tamaris se hodí ženám, které chtějí módní obuv na každý den a nehledají specializovanou sportovní botu. Kolekce sleduje aktuální trendy, takže se barvy a tvary každou sezónu mění. Pokud vám některý model sedí, vyplatí se koupit ho, dokud je v nabídce, nebo si poznamenat jeho kód a hledat ho u dalších obchodů.</p>'
          '<h2>Sandály a nazouváky na léto</h2>'
          '<p>Letní kolekce zahrnuje ploché sandály, modely na klínku a sandály na podpatku k šatům. Na celodenní chůzi po městě jsou nejpohodlnější ploché sandály nebo nízký klínek s páskem kolem kotníku, který drží nohu na místě. Podpatek nad pět centimetrů nosí většina lidí jen na kratší dobu. Kožená stélka lépe saje pot než syntetická, ale potřebuje víc péče. Nazouváky bez pásku za patou se hodí na krátké pochůzky, na delší chůzi noha v obuvi klouže. Další letní výběr najdete v kategorii <a href="/damske-sportovni-sandaly/">dámské sandály</a>.</p>'
          '<h2>Tenisky a kotníkové boty</h2>'
          '<p>Tenisky Tamaris jsou módní obuv do města, často na vyšší podrážce nebo platformě a s koženým či semišovým svrškem. Na běh nebo sport v hale nejsou určené. Kotníkové boty na zip tvoří velkou část podzimní kolekce. Zip na boku usnadní obouvání, ale má se zapínat bez tahání, jinak je bota příliš úzká v nártu. Podpatek volte podle toho, kolik chodíte: blokový podpatek je stabilnější než úzký.</p>'
          '<h2>Materiály a veganské modely</h2>'
          '<p>Část bot je z přírodní kůže a semiše, část ze syntetiky nebo textilu. Kůže lépe dýchá, časem se tvaruje podle nohy a při dobré péči vydrží déle. Syntetika je lehčí, levnější a snadno se čistí, ale v teple se v ní noha víc potí. Značka nabízí i veganské modely bez živočišných materiálů, které v roce 2022 získaly ocenění PETA Vegan Fashion Award. Materiál svršku, podšívky a stélky vždy uvádí popis produktu.</p>'
          '<h2>Zimní boty a sněhule</h2>'
          '<p>Zimní modely mají zateplení z umělé kožešiny nebo vlny a podrážku s hlubším vzorkem. Do města na sníh a rozbředlou sůl stačí, na dlouhé zimní výlety do hor ale nejsou stavěné. Pokud chcete jistotu v mokru, hledejte v popisu membránu nebo označení vodoodolné. Více inspirace najdete na stránkách <a href="/damske-zimni-boty/">dámské zimní boty</a> a <a href="/damske-snehule/">dámské sněhule</a>.</p>'
          '<h2>Trekové boty Tamaris active</h2>'
          '<p>Trekové boty s Gore-Tex jsou lehčí a měkčí než klasické turistické boty. Hodí se na procházky do přírody, výlety po značených cestách a cestování. Pro náročné horské túry s těžkým batohem vyberte raději obuv specializovaného výrobce s pevnější podešví. Srovnání nabízí kategorie <a href="/damske-trekove-boty/">dámské trekové boty</a>.</p>'
          '<h2>Sourozenecké značky</h2>'
          '<p>Kdo má rád Tamaris, často sáhne i po dalších značkách skupiny Wortmann. Jde hlavně o Marco Tozzi, Caprice a Jana. Caprice vznikla v roce 1990 v Pirmasensu a od začátku se zaměřuje na pohodlné dámské boty ve více šířkách, což ocení ženy, kterým běžná šířka nesedí. Ve vícebrandových obchodech najdete tyto značky vedle sebe. Velikosti se mezi nimi mohou mírně lišit, proto i u nich kontrolujte tabulku konkrétního obchodu.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Výběr podle názvu obchodu místo kódu modelu. Stejná bota se pak koupí dráž.</li>'
          '<li>Zimní boty přesně na délku, když do nich nosíte silné ponožky.</li>'
          '<li>Vysoká platforma na dlouhé procházky po dlažbě.</li>'
          '<li>Semišové boty bez impregnace do mokrého počasí.</li></ul>'
          '<h2>Péče</h2>'
          '<ul><li>Hladkou kůži čistěte vlhkým hadříkem a ošetřujte krémem v odpovídající barvě.</li>'
          '<li>Semiš a nubuk kartáčujte za sucha a chraňte <a href="/impregnace/">impregnací</a>.</li>'
          '<li>Sůl ze zimních bot otřete hned po příchodu domů, jinak na kůži zůstanou mapy.</li>'
          '<li>Mokré boty sušte vycpané papírem při pokojové teplotě.</li>'
          '<li>Textilní tenisky perte jen tehdy, když to štítek dovoluje.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>Díky číselnému kódu můžete snadno porovnat stejný model v různých obchodech. Ověřte, že sedí i kód barvy a materiál, protože stejné číslo modelu se vyrábí v kůži i v syntetice. Kolekce se mění každou sezónu, starší modely proto rychle zlevňují, zvlášť na konci léta a po Vánocích. Podobný styl a pohodlí nabízejí značky '
          + B(('rieker', 'Rieker'), ('ecco', 'Ecco'), ('geox', 'Geox'), ('skechers', 'Skechers')) +
          '. Další výběr najdete mezi <a href="/damske-tenisky/">dámskými teniskami</a> a <a href="/damske-pantofle/">dámskými pantoflemi</a>.</p>',
    faq=[
        ('Odkud pochází značka Tamaris?',
         'Z Německa. Patří do rodinné skupiny Wortmann z Detmoldu, kterou v roce 1967 založil Horst Wortmann. Do skupiny patří i Marco Tozzi a Caprice.'),
        ('Kde se boty Tamaris vyrábějí?',
         'Návrh a vývoj řídí skupina Wortmann z Německa, samotná výroba probíhá v zahraničí. Zemi výroby konkrétního páru uvádí štítek nebo popis produktu.'),
        ('Jak padnou boty Tamaris?',
         'Obvykle odpovídají běžné evropské velikosti. Půlčísla se nevyrábějí, mezi dvěma čísly se doporučuje spíš větší, hlavně u zimních bot.'),
        ('Má Tamaris i boty pro širší nohu?',
         'Kolekce Comfort má pohodlnější šířku a vyjímatelnou stélku. Konkrétní šířku ověřte v popisu modelu.'),
        ('Co znamená číslo jako 1-23760-41?',
         'Prostřední číslo je kód modelu, poslední dvojčíslí sezóna. Podle kódu najdete stejný model v různých obchodech.'),
        ('Jsou trekové boty Tamaris vhodné do hor?',
         'Hodí se na vycházky a lehkou turistiku po cestách. Na náročné túry s těžkým batohem zvolte pevnější obuv specializovaného výrobce.'),
        ('Mají boty Tamaris vyjímatelnou stélku?',
         'Některé ano, hlavně modely Comfort. Do nich lze vložit vlastní vložky, u ostatních je stélka často pevně vlepená.'),
        ('Má Tamaris pánskou obuv?',
         'Prakticky ne, jde o značku dámské obuvi. Pánské boty v podobném stylu nabízejí například Rieker nebo Geox.'),
        ('Kdy bývá Tamaris ve slevě?',
         'Při obměně kolekce, tedy na konci léta a po zimní sezóně. Starší barvy a modely zlevňují nejrychleji.'),
        ('Prodává sporteka.cz boty Tamaris?',
         'Ne. Sporteka shromažďuje nabídky českých e-shopů, objednávka, výměna velikosti i vrácení probíhá u vybraného obchodu.'),
    ],
)

# ------------------------------------------------------------------ ugg
NEW['ugg'] = dict(
    title='UGG: boty z ovčí kůže, sněhule Classic a pantofle',
    desc='UGG boty v katalogu: Classic Mini a Ultra Mini, Bailey Bow, pantofle Tasman a Disquette, tenisky Lowmel i sandály. Velikosti, péče o semiš a srovnání.',
    intro='<p>UGG je americká značka, kterou proslavily boty z ovčí kůže s vlnou uvnitř. V Česku lidé hledají hlavně „ugg boty“, tedy klasické nízké a kotníkové modely Classic, ale nabídka je širší: pantofle Tasman a Disquette, tenisky Lowmel, sandály Goldenstar, holinky, ponožky a pletené čepice. '
          'Sporteka.cz u každého produktu zobrazuje nabídky českých obchodů vedle sebe, takže porovnáte barvy, materiály a dostupné velikosti. Nakupujete pak přímo v e-shopu, který si vyberete. U oblíbených modelů se vyplatí sledovat více obchodů, protože běžné velikosti se v zimě rychle vyprodávají. '
          'Na stránce najdete stručnou historii značky, přehled hlavních modelů, rady k velikostem, které jsou u ovčí kůže specifické, a návod, jak o boty pečovat, aby vydržely víc než jednu zimu. Dozvíte se také, které modely zvládnou mokrý sníh a které patří spíš do suchého mrazu nebo domů.</p>',
    guide='<h2>Australská bota, americká značka</h2>'
          '<p>Boty z ovčí kůže nosili na australském venkově a mezi surfaři už dávno předtím, než vznikla značka. Slovo ugg je v Austrálii a na Novém Zélandu obecné označení tohoto typu bot. Značku UGG založil v roce 1978 v jižní Kalifornii australský surfař Brian Smith, který boty z domova začal prodávat americkým surfařům. V roce 1995 firmu koupila americká společnost Deckers, která vlastní ochrannou známku UGG ve více než stovce zemí. Mimo Austrálii a Nový Zéland proto název UGG označuje výrobky jedné firmy.</p>'
          '<p>Na počátku tisíciletí se boty Classic staly módním hitem a z plážového doplňku se proměnily ve zimní obuv do města. Dnes UGG vyrábí obuv pro ženy, muže i děti a k ovčí kůži přidal i syntetické materiály a membrány.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Největší skupinou jsou kotníkové boty a <a href="/tenisky/">tenisky</a>, kam obchody řadí kromě tenisek Lowmel i nízké modely Classic. Hodně jsou zastoupené <a href="/pantofle-a-zabky/">pantofle a nazouváky</a>, <a href="/zimni-obuv/">zimní obuv</a> a sněhule, letní <a href="/sandaly/">sandály</a> a <a href="/holinky/">holinky</a>. Doplňky tvoří <a href="/sportovni-ponozky/">ponožky</a>, <a href="/cepice-a-celenky/">čepice</a> a rukavice. Většina nabídky je dámská, pánské a dětské modely tvoří menší část.</p>'
          + T(['Model', 'Typ', 'Na co'], [
              ['Classic Ultra Mini, Mini, Short', 'nízké až polovysoké boty z ovčí kůže', 'suchá zima, město'],
              ['Classic Micro, Platform', 'nižší nebo na vyšší podrážce', 'módní styl, suché počasí'],
              ['Bailey Bow', 'Classic s mašlí na patě', 'zima ve městě'],
              ['Tasman, Tazz, Disquette', 'nazouváky a pantofle s vlnou', 'domov, krátké cesty ven'],
              ['Lowmel, Neumel', 'tenisky a kotníkové boty', 'přechodné období'],
              ['Goldenstar, Goldenglow', 'sandály s lehkou podrážkou', 'léto'],
              ['Adirondack, voděodolné modely', 'zimní boty s protiskluzovou podrážkou', 'sníh, mokro']]) +
          '<h2>Ovčí kůže a jak se chová</h2>'
          '<p>Klasické boty UGG jsou z ovčí kůže, u které zůstává vlna na vnitřní straně. Vlna dobře hřeje, odvádí vlhkost a v teple se v ní noha tolik nepotí, proto se boty tradičně nosí bez ponožek nebo s tenkou ponožkou. Venkovní strana je semiš, který vlhkost nesnáší. Klasické modely Classic proto nejsou do deště ani do rozbředlého sněhu se solí. Do mokrého počasí jsou určené řady s ošetřeným semišem, s membránou nebo holinky.</p>'
          '<h2>Velikosti: proč mají sedět těsněji</h2>'
          '<p>Vlna uvnitř boty se během prvních dní nošení slehne a bota se trochu povolí. Nové boty z ovčí kůže proto mají sedět spíš těsněji, ale prsty nesmějí narážet do špičky. Pokud jsou volné hned při zkoušení, budou časem ještě volnější a pata začne vyklouzávat. Řada klasických modelů se vyrábí jen v celých číslech. Kdo je mezi dvěma velikostmi, u Classic obvykle volí menší, u tenisek a bot bez vlny spíš svou běžnou velikost.</p>'
          '<ol><li>Změřte chodidlo a porovnejte ho s tabulkou u konkrétního obchodu.</li>'
          '<li>U Classic počítejte s tím, že se vlna slehne.</li>'
          '<li>Pokud chcete nosit silné ponožky, menší velikost nevolte.</li>'
          '<li>U pantoflí Tasman a Disquette má pata sedět na stélce, ne přesahovat.</li></ol>'
          '<h2>Péče o semiš a vlnu</h2>'
          '<ul><li>Před prvním nošením ošetřete boty <a href="/impregnace/">impregnací</a> na semiš a obnovujte ji každých pár měsíců.</li>'
          '<li>Mokré boty sušte volně při pokojové teplotě, nikdy na topení nebo fénem.</li>'
          '<li>Skvrny čistěte čističem na ovčí kůži a měkkou houbou, celé boty nenamáčejte.</li>'
          '<li>Po vyschnutí semiš lehce pročešte kartáčem, vlas se tak narovná.</li>'
          '<li>Sůl otřete co nejdříve, na semiši zanechává bílé mapy.</li>'
          '<li>Na léto uložte boty vycpané papírem v látkovém sáčku.</li></ul>'
          '<h2>Voděodolné modely a holinky</h2>'
          '<p>Kdo chce vzhled UGG i do mokrého počasí, má několik možností. Zimní boty s protiskluzovou podrážkou a vodoodolným svrškem, například z řady Adirondack, zvládnou sníh i rozbředlou břečku. <a href="/damske-holinky/">Holinky</a> z gumy s vlněnou vložkou jsou určené do deště. U semišových bot s ošetřením proti vodě počítejte s tím, že odolají krátké přeháňce, ale ne celodennímu chození v mokru.</p>'
          '<h2>Tenisky, sandály a celoroční nabídka</h2>'
          '<p>Tenisky Lowmel a kotníkové boty Neumel kombinují semiš, textil a lehkou podrážku. Vnitřek bývá částečně vystlaný vlnou nebo textilem, takže jsou příjemné na podzim a na jaře. Letní sandály Goldenstar a Goldenglow mají měkkou, lehkou podrážku a nastavitelné pásky. Ponožky s příměsí vlny a pletené čepice jsou vhodným doplňkem, pokud hledáte dárek bez nutnosti trefit velikost bot.</p>'
          '<h2>Pánské a dětské boty</h2>'
          '<p>Pánská nabídka zahrnuje hlavně Classic Ultra Mini, nazouváky Tasman a kotníkové boty Neumel. Dětské boty se prodávají ve velikostech pro batolata, malé i větší děti. U dětí dávejte přednost modelům s pevnější podrážkou do venku a pravidelně kontrolujte velikost, protože vlna se slehne a noha roste. Pro aktivní zimní hry na sněhu jsou vhodnější klasické dětské sněhule s membránou.</p>'
          '<h2>Který model do jakého počasí</h2>'
          + T(['Počasí', 'Vhodný typ', 'Poznámka'], [
              ['Suchý mráz', 'Classic Mini, Short, Bailey Bow', 'nejteplejší varianta, semiš ošetřete impregnací'],
              ['Mokrý sníh a sůl', 'voděodolné zimní boty, Adirondack', 'hledejte protiskluzovou podrážku'],
              ['Déšť', 'holinky s vlněnou vložkou', 'semišové boty nechte doma'],
              ['Podzim a jaro', 'Lowmel, Neumel, Tasman', 'lehčí podrážka, méně vlny'],
              ['Léto', 'sandály Goldenstar a Goldenglow', 'měkká lehká podrážka']]) +
          '<p>Klasické boty z ovčí kůže mají měkkou podrážku z lehkého materiálu. Na ledu a ujetém sněhu kloužou víc než zimní boty s hlubokým vzorkem. Kdo chodí do práce pěšky po neudržovaných chodnících nebo do kopce, ocení modely s výraznějším dezénem. Na dlouhé zimní procházky do přírody jsou vhodnější specializované zimní boty s membránou a oporou kotníku.</p>'
          '<h2>Pantofle a domácí obuv</h2>'
          '<p>Nazouváky Tasman, pantofle Disquette nebo Scuff mají vlnu uvnitř a pevnější podrážku, takže v nich můžete i na krátkou cestu ven. Jako domácí obuv jsou teplejší než běžné bačkory a vlna v nich méně zapáchá. Více možností najdete mezi <a href="/domaci-pantofle/">domácími pantoflemi</a>.</p>'
          '<h2>Jak poznat kvalitní kus</h2>'
          '<p>Originální boty Classic mají vlnu přirozeně spojenou s kůží, ne nalepenou zvlášť. Vlna je hustá a po stisknutí se vrací. Podrážka je pružná a pevně spojená se svrškem. Na patě je štítek s logem a uvnitř etiketa s velikostí a kódem modelu. Nejjistější cestou je nákup u zavedeného obchodu s jasnými podmínkami vrácení. Podezřele nízká cena u neznámého prodejce, chybějící kontakty nebo nejasná adresa firmy jsou důvodem k opatrnosti. Sporteka zobrazuje nabídky českých e-shopů, ale podmínky prodeje si vždy ověřte přímo u obchodu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě o číslo větších Classic kvůli silné ponožce. Bota po slehnutí vlny plandá.</li>'
          '<li>Nošení semišových bot v rozbředlém sněhu se solí.</li>'
          '<li>Sušení mokrých bot na radiátoru, semiš ztvrdne a popraská.</li>'
          '<li>Nákup výrazně pod obvyklou cenou na neznámém webu, kde hrozí padělek.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>Modely Classic mají mnoho variant, které se v obchodech snadno zamění: Ultra Mini je nejnižší, Mini sahá nad kotník, Short do poloviny lýtka. K tomu přistupují verze na platformě nebo s mašlí. Porovnávejte proto přesný název, barvu a materiál a sledujte, zda nejde o dámskou, pánskou nebo dětskou řadu. Před zimou se nejrychleji vyprodávají běžné velikosti v černé a kaštanové barvě, slevy přicházejí po Vánocích. Hledáte-li zimní boty, podívejte se i na stránku <a href="/ugg-zimni-boty/">zimní boty UGG</a> a kategorie <a href="/damske-snehule/">dámské sněhule</a> nebo <a href="/detske-zimni-boty/">dětské zimní boty</a>. Pro srovnání stojí za pohled zimní boty značek '
          + B(('columbia', 'Columbia'), ('timberland', 'Timberland'), ('keen', 'Keen')) + '.</p>',
    faq=[
        ('Odkud pochází značka UGG?',
         'Boty z ovčí kůže pocházejí z Austrálie, značku UGG ale založil v roce 1978 v Kalifornii australský surfař Brian Smith. Od roku 1995 patří firmě Deckers.'),
        ('Proč se v Austrálii prodávají „ugg boty“ i od jiných výrobců?',
         'V Austrálii a na Novém Zélandu je ugg obecné slovo pro boty z ovčí kůže. Mimo tyto země je UGG chráněná značka firmy Deckers.'),
        ('Jakou velikost UGG bot zvolit?',
         'Klasické boty z ovčí kůže mají zpočátku sedět těsněji, protože se vlna slehne. Mezi dvěma čísly se u Classic obvykle volí menší velikost.'),
        ('Nosí se boty UGG s ponožkami?',
         'Vlna uvnitř hřeje a odvádí vlhkost, proto se tradičně nosí naboso nebo s tenkou ponožkou. Se silnou ponožkou vyberte běžnou velikost.'),
        ('Můžu boty UGG nosit do deště a sněhu?',
         'Klasické semišové modely do mokra nejsou. Pomůže impregnace, ale do rozbředlého sněhu vyberte voděodolné modely nebo holinky.'),
        ('Jaký je rozdíl mezi Classic Ultra Mini, Mini a Short?',
         'Ultra Mini je nejnižší, těsně nad kotník. Mini je o něco vyšší, Short sahá zhruba do poloviny lýtka.'),
        ('Jak vyčistit boty UGG?',
         'Skvrny čistěte čističem na ovčí kůži a houbou, celou botu nenamáčejte. Sušte volně při pokojové teplotě, nikdy na topení.'),
        ('Má UGG i pánské a dětské boty?',
         'Ano, například Classic Ultra Mini, Tasman nebo Neumel pro muže a dětské verze Classic. Většina nabídky je ale dámská.'),
        ('Kdy jsou boty UGG levnější?',
         'Obvykle po Vánocích a na konci zimy. Před sezónou se běžné velikosti v oblíbených barvách rychle vyprodají, proto je dobré sledovat cenu konkrétní varianty s předstihem.'),
        ('Prodává sporteka.cz boty UGG?',
         'Ne. Sporteka porovnává nabídky českých obchodů. Pravost, záruku a vrácení řešíte s e-shopem, ve kterém nakoupíte.'),
    ],
)

# ------------------------------------------------------------------ specialized
NEW['specialized'] = dict(
    title='Specialized: kola, elektrokola Turbo, helmy a doplňky',
    desc='Specialized v katalogu: horská kola Rockhopper a Epic, elektrokola Turbo Levo a Vado, gravel Diverge, helmy, tretry a doplňky. Jak vybrat a porovnat.',
    intro='<p>Specialized je americký výrobce jízdních kol z Kalifornie, který stál u zrodu sériově vyráběných horských kol. V katalogu najdete horská kola od hardtailu Rockhopper po celoodpružené Epic a Stumpjumper, elektrokola Turbo Levo a Turbo Vado, gravely Diverge a krosová kola Sirrus X. '
          'Velkou část nabídky tvoří příslušenství: helmy, tretry, sedla, pláště, pumpy, košíky na láhve a rukavice. '
          'Sporteka.cz u každého produktu ukazuje nabídky českých obchodů, takže porovnáte dostupnost velikosti rámu, barvy i modelového roku. Kolo nebo doplněk pak koupíte přímo u prodejce, kterého si vyberete. U kol se vyplatí počítat i se službami obchodu, tedy se seřízením, první prohlídkou a dostupností servisu v okolí. '
          'Níže najdete historii značky, přehled modelových řad, vysvětlení velikostí rámů a rady k péči a srovnávání nabídek.</p>',
    guide='<h2>Od dovozu dílů k prvnímu sériovému horskému kolu</h2>'
          '<p>Firmu založil v roce 1974 Mike Sinyard. Začínal dovozem italských cyklistických dílů, které rozvážel prodejnám, a brzy přidal vlastní pláště a komponenty. V roce 1981 uvedl Specialized na trh Stumpjumper, který bývá označován za první sériově vyráběné horské kolo. Jeden z prvních kusů je dnes ve sbírkách Smithsonova institutu ve Washingtonu. Od osmdesátých let sídlí firma v kalifornském Morgan Hill.</p>'
          '<p>Specialized dlouhodobě pracuje s ergonomií. Program Body Geometry začal spoluprací s odborníkem na ergonomii Rogerem Minkowem na sedlech s výřezem, který snižuje tlak v citlivé oblasti. Dnes se stejný přístup uplatňuje u tretr, rukavic a řídítek. Označení BG proto v katalogu najdete u rukavic i sedel.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější skupinou je <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>, kam obchody řadí tretry, sedla, pláště, kabely a servisní sady. Následují <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/horska-kola/">horská kola</a> a <a href="/horska-elektrokola/">horská elektrokola</a>. Zastoupené jsou také <a href="/celoodpruzena-horska-kola/">celoodpružená kola</a>, <a href="/trekingova-elektrokola/">trekingová elektrokola</a>, gravely, krosová kola, košíky a brašny, <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>, světla a rukavice. Menší část tvoří dresy, kraťasy, láhve a zapletená kola Roval.</p>'
          + T(['Řada', 'Typ kola', 'Na co'], [
              ['Rockhopper', 'hliníkový hardtail', 'začátek na horském kole, lesní cesty'],
              ['Chisel, Epic HT', 'lehké hardtaily', 'cross country, závody'],
              ['Epic, Stumpjumper, Enduro', 'celoodpružená horská kola', 'od XC po náročné sjezdy'],
              ['Turbo Levo, Levo SL', 'horská elektrokola', 'trail a enduro s motorem'],
              ['Turbo Vado, Vado SL, Tero', 'trekingová a městská elektrokola', 'dojíždění, výlety, šotolina'],
              ['Diverge, Crux', 'gravel kola', 'šotolina, silnice, bikepacking'],
              ['Sirrus X', 'krosová a fitness kola', 'město, cyklostezky']]) +
          '<h2>Elektrokola Turbo</h2>'
          '<p>Všechna elektrokola Specialized nesou v názvu slovo Turbo. Levo je celoodpružené horské elektrokolo, verze SL je lehčí, s menším motorem a baterií, takže se chová víc jako klasické kolo. Vado je trekingové elektrokolo s blatníky, nosičem a světly pro dojíždění. Vado SL je jeho lehčí obdoba. Tero je určené pro kombinaci silnice, polních cest a lehkého terénu. Při výběru porovnejte kapacitu baterie ve watthodinách, typ motoru, váhu kola a výbavu. Označení EQ obvykle znamená plně vybavenou verzi s blatníky, nosičem a světly. Step-through je rám s nízkým nástupem.</p>'
          '<h2>Velikosti rámů</h2>'
          '<p>U novějších horských kol jako Stumpjumper nebo Turbo Levo používá Specialized značení S1 až S6 místo klasického S, M a L. Mezi velikostmi se mění hlavně délka rámu, tedy reach, zatímco výška sedlové trubky roste jen mírně. Výběr se proto řídí víc tím, jak dlouhý posed chcete, než samotnou výškou. Cross country kola a hardtaily jako Rockhopper nebo Chisel se dál prodávají ve velikostech XS až XL.</p>'
          '<ol><li>Najděte v tabulce výrobce velikost podle své výšky.</li>'
          '<li>Jste-li mezi dvěma velikostmi, menší rám je hravější, větší stabilnější.</li>'
          '<li>U S-Sizing porovnejte reach se svým současným kolem.</li>'
          '<li>Kolo si pokud možno vyzkoušejte u prodejce.</li></ol>'
          '<h2>Helmy a tretry</h2>'
          '<p>Helmy Specialized pokrývají všechny styly: Align II a Chamonix na běžné ježdění, Search a Ambush do terénu, Prevail a Evade na silnici. Verze s označením Mips mají vnitřní vrstvu, která při šikmém nárazu umožňuje mírný posun. Řada novějších helem je připravená na senzor ANGi, který spolu s aplikací Specialized po nárazu spustí odpočet a pokud ho nezrušíte, pošle vaší kontaktní osobě polohu. Velikost helmy volte podle obvodu hlavy změřeného nad obočím. Další výběr je mezi <a href="/mtb-a-integralni-helmy/">helmami na MTB</a> a <a href="/silnicni-cyklohelmy/">silničními helmami</a>.</p>'
          '<p>Tretry Torch jsou silniční, Recon je určený pro gravel a horská kola, Remix je volnočasová obuv k plochým pedálům. Specialized tradičně vyrábí tretry s tužší podešví a vnitřní tvarovanou stélkou. Při výběru ověřte, zda tretry odpovídají vašemu typu nášlapných pedálů.</p>'
          '<h2>Sedla a rukavice Body Geometry</h2>'
          '<p>Sedla Specialized se vyrábějí v několika šířkách, protože každý má jinou vzdálenost sedacích kostí. Prodejci značky ji umějí změřit na jednoduché podložce. Sedla Power a Romin mají výřez uprostřed, který snižuje tlak na měkké tkáně. Rukavice BG mají v dlani gelové nebo pěnové polštářky, které rozkládají tlak na řídítkách. Sedlo ani rukavice ale nejsou zdravotní pomůckou. Pokud vás při jízdě opakovaně brní ruce nebo bolí v sedle, zkontrolujte posed na kole a při přetrvávajících potížích se poraďte s lékařem. Dámské varianty mají v názvu zkratku WMN.</p>'
          '<h2>Gravel a krosová kola</h2>'
          '<p>Diverge je gravel kolo s pohodlnější geometrií a místem pro široké pláště, některé verze mají v hlavové trubce odpružení Future Shock. Crux je lehčí a sportovnější, vhodný na rychlou jízdu po šotolině. Sirrus X má rovná řídítka a hodí se do města i na cyklostezky, verze s vyšším číslem mají lepší komponenty. Kdo váhá mezi gravelem a krosovým kolem, měl by zvážit, zda chce beránky a jízdu na delší vzdálenosti, nebo vzpřímený posed.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Elektrokolo s největší baterií, i když jezdíte krátké trasy. Kolo je pak zbytečně těžké.</li>'
          '<li>Velikost rámu podle kamaráda místo podle tabulky a vlastní výšky.</li>'
          '<li>Celoodpružené kolo na asfalt a cyklostezky, kde stačí hardtail nebo krosové kolo.</li>'
          '<li>Helma bez zkoušky obvodu hlavy, která pak na hlavě klouže.</li></ul>'
          '<h2>Na co se zeptat při koupi elektrokola</h2>'
          '<p>Elektrokolo je dražší nákup a vyplatí se znát podmínky prodejce dřív, než zaplatíte. Zeptejte se, kdo zajistí seřízení a první servisní prohlídku, jak dlouhá je záruka na baterii a motor a zda se dá baterie později vyměnit za větší. U modelů s nabíjecím portem v rámu ověřte, zda je v balení nabíječka a jak dlouho trvá nabití. Zjistěte také, zda prodejce umí aktualizovat software motoru a diagnostiku, protože ta vyžaduje servisní nástroje značky. Pokud kolo převážíte na autě, hlídejte nosnost nosiče, elektrokola jsou výrazně těžší než klasická. Před první delší vyjížďkou si vyzkoušejte jednotlivé režimy podpory a odhadněte, kolik baterie spotřebujete do kopce. Dojezd uváděný výrobcem platí pro ideální podmínky, v zimě, s těžkým nákladem nebo v prudkém stoupání bude kratší. U nižších teplot nechte baterii před nabíjením ohřát v místnosti.</p>'
          '<h2>Drobné doplňky</h2>'
          '<p>SWAT je systém pro uložení nářadí, duše a pumpičky přímo na kole, například v rámu nebo pod košíkem. Košíky Zee Cage se nasazují z boku, což usnadňuje vytažení láhve na malých rámech. Pláště Specialized se liší směsí a ochranou proti průrazu, Butcher je do terénu, All Condition na silnici za každého počasí.</p>'
          '<h2>Péče o kolo</h2>'
          '<ul><li>Po jízdě v blátě kolo opláchněte slabým proudem vody, ne tlakovou myčkou do ložisek.</li>'
          '<li>Řetěz pravidelně čistěte a mažte, u elektrokol se opotřebuje rychleji.</li>'
          '<li>Baterii elektrokola skladujte v suchu při pokojové teplotě, přes zimu nabitou zhruba napůl.</li>'
          '<li>Tlak v pláštích a odpružení kontrolujte před každou delší vyjížďkou.</li>'
          '<li>Utahujte šrouby momentovým klíčem, hlavně u karbonových dílů.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>Specialized prodává jeden model v několika úrovních výbavy, typicky Sport, Comp, Expert, Pro a S-Works. Liší se materiálem rámu, komponenty a odpružením, takže dvě kola stejného jména mohou být zcela jinak vybavená. Porovnávejte proto přesný název, modelový rok, velikost rámu a barvu. Starší ročníky se doprodávají na podzim a v zimě, kdy přichází nová kolekce. Pro srovnání stojí za pohled kola značek '
          + B(('scott', 'Scott')) +
          ', Trek nebo Cube a další výběr v kategorii <a href="/gravel-kola/">gravel kola</a>.</p>',
    faq=[
        ('Odkud pochází Specialized?',
         'Z Kalifornie. Firmu založil v roce 1974 Mike Sinyard, dnes sídlí v Morgan Hill. V roce 1981 uvedla na trh horské kolo Stumpjumper.'),
        ('Co znamená Turbo v názvu kola Specialized?',
         'Turbo nesou všechna elektrokola značky: Levo do terénu, Vado na dojíždění a výlety, Tero na kombinaci silnice a lehkého terénu.'),
        ('Jaký je rozdíl mezi Turbo Levo a Levo SL?',
         'SL je lehčí verze s menším motorem a baterií. Jezdí se na něm víc jako na klasickém kole, plná verze nabídne větší pomoc a dojezd.'),
        ('Co znamenají velikosti S1 až S6?',
         'Systém S-Sizing u novějších horských kol. Mezi velikostmi se mění hlavně délka rámu, výška sedlové trubky jen mírně.'),
        ('Jaký je rozdíl mezi Comp, Expert a S-Works?',
         'Jde o úrovně výbavy. Comp je dostupnější, Expert a Pro mají lepší komponenty a S-Works je nejvyšší řada, obvykle s karbonovým rámem.'),
        ('Co je senzor ANGi?',
         'Malý senzor na helmu, který s aplikací Specialized pozná náraz. Spustí odpočet, a pokud ho nezrušíte, pošle kontaktní osobě vaši polohu.'),
        ('Co znamená EQ u elektrokola Vado?',
         'Plně vybavenou verzi pro každodenní provoz, obvykle s blatníky, nosičem a světly. Výbavu vždy ověřte v popisu modelu.'),
        ('Které rukavice Specialized zvolit?',
         'Řada BG Dual Gel a Sport Gel má gelové polštářky do dlaně, Trail je do terénu. LF znamená dlouhé prsty, WMN dámský střih.'),
        ('Kdy jsou kola Specialized levnější?',
         'Obvykle na podzim a v zimě, kdy obchody doprodávají modelový rok před příchodem nové kolekce. Starší ročník mívá stejný rám a liší se hlavně barvou nebo některými komponenty, proto se vyplatí porovnat obě verze.'),
        ('Prodává sporteka.cz kola Specialized?',
         'Ne. Sporteka porovnává nabídky českých obchodů, nákup, seřízení kola a servis zajišťuje prodejce, u kterého nakoupíte. U kol a elektrokol se proto vyplatí vybírat i podle dostupnosti servisu v okolí.'),
    ],
)
