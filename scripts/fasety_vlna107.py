"""sporteka.cz — facet landing texts wave 107: detske-boty-do-vody, dakine-batohy, barefoot-boty-damske, cerna-mikina.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detske-boty-do-vody
NEW['detske-boty-do-vody'] = dict(
    title='Dětské boty do vody: velikost, typy a výběr podle věku',
    desc='Dětské boty do vody na moře, jezero i aquapark: neopren, síť nebo ponožky. Jak změřit nohu, vybrat suchý zip a pár, který dítěti nesklouzne.',
    intro='<p>Dětská noha ve vodě řeší jiné problémy než dospělá: je citlivější na ostré dno, rychleji se ochladí a dítě se u vody pohybuje bez ohledu na to, kam šlape. Dobrá obuv do vody proto musí hlavně držet na noze, mít protiskluzovou podrážku a jít snadno obout a zout mokrýma rukama. '
          'Na této stránce jsou dětské modely z kategorie <a href="/obuv-do-vody/">boty do vody</a>, od měkkých ponožek pro batolata přes sítové boty na suchý zip po neoprenové boty pro starší děti. Průvodce vysvětluje, jak změřit chodidlo, kolik místa nechat na růst, čím se liší typy podle věku a jak boty po koupání ošetřit. Dospělé a odrostlé děti najdou nabídku v <a href="/panske-boty-do-vody/">pánských</a> a <a href="/damske-boty-do-vody/">dámských botách do vody</a>.</p>',
    guide='<h2>Proč dítě potřebuje boty do vody</h2>'
          '<p>Na dovolené u moře se děti většinu dne pohybují po kamenitém dně, rozpáleném písku, mokrých schodech a molech. Malé chodidlo má jemnější kůži než dospělé, takže se rychleji odře, popálí i pořeže o střep nebo lasturu. Obuv do vody tyto situace zmírňuje a přidává jistotu při první chůzi po kluzkých kamenech. Hodí se také v bazénu a aquaparku, kde je podlaha mokrá a hladká, a na koupalištích s trávou a štěrkem.</p>'
          '<p>Důležité je nečekat od bot víc, než umějí. Chrání proti otěrům, drobným říznutím a horkému povrchu, ale neudělají z dítěte plavce a nenahradí dozor. Děti v nich také nesmí chodit hlouběji, než jim dosáhnou na dno, a pomůcky na plavání zůstávají samostatnou kapitolou, kterou najdete v kategorii <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>'
          '<h2>Typy dětských bot do vody</h2>'
          + T(['Typ', 'Konstrukce', 'Hodí se pro'], [
              ['Plavecká ponožka', 'tenký elastický textil nebo neopren s gumovými puntíky', 'batolata, bazén, písečná pláž'],
              ['Sítová bota na suchý zip', 'prodyšná síťka, pryžová podrážka, upínací pásek', 'předškoláky a školáky, kamenité pobřeží, brodění'],
              ['Neoprenová bota', 'pružný neopren, lepená podrážka, někdy boční zip', 'chladnější vodu, kajak, paddleboard, delší pobyt ve vodě'],
              ['Sandálový typ', 'pásky, otevřená špička nebo pěnová podrážka', 'horký den, rodinná koupaliště, krátké brouzdání'],
              ['Pěnová nazouvací bota', 'lehká pěna, otvory, pásek přes patu', 'rychlé obutí, loď, bazén, hřiště s vodou']]) +
          '<p>Pro nejmenší dávejte přednost měkkým modelům, které se nesmekají z nohy a mají zakulacenou špičku. Starším dětem, které lezou po skalách nebo brodí potok, se víc hodí pevnější podrážka. Ponožky se v mělké vodě a na pláži obejdou bez pásků, ale na ostré dno nestačí a na mokrém molu mohou klouzat, pokud nemají gumové prvky.</p>'
          '<h2>Jak změřit nohu a vybrat velikost</h2>'
          '<p>Děti rostou rychle a obuv do vody se obvykle kupuje na jednu až dvě sezony. Příliš velká bota se ale na noze převrací a nabírá vodu, příliš malá tlačí a otírá. Správný postup je změřit nohu na papíře: dítě se postaví, obkreslete chodidlo svisle vedenou tužkou a změřte vzdálenost od paty k nejdelšímu prstu. Ke zjištěné délce se přičítá rezerva, kterou výrobci uvádějí v tabulce.</p>'
          + T(['Délka chodidla', 'Vnitřní délka boty', 'Orientační velikost EU'], [
              ['14 cm', 'asi 15 cm', 'kolem 22–23'],
              ['16 cm', 'asi 17 cm', 'kolem 25–26'],
              ['18 cm', 'asi 19 cm', 'kolem 28–29'],
              ['20 cm', 'asi 21 cm', 'kolem 31–32'],
              ['22 cm', 'asi 23 cm', 'kolem 34–35']]) +
          '<p>Tabulka je jen orientační, protože značky mají různé kopyto. Většina výrobců uvádí délku vložky v centimetrech, a pokud ji najdete v popisu, řiďte se jí před číslem na štítku. U neoprenových bot nechávejte rezervu jen kolem půl centimetru, protože se při kontaktu s vodou o něco povolí. U sítových bot a sandálů může být rezerva o něco větší, ale jen taková, aby se špička při chůzi neohýbala před palcem.</p>'
          '<h2>Zapínání: suchý zip, guma nebo zip</h2>'
          '<p>Boty, které dítě samo nezvládne obout, vydrží u vody jen pár minut. Proto pomáhá, když má bota široké otevření, poutko na patě a jedno rychlé zapínání.</p>'
          '<ul><li><strong>Suchý zip:</strong> nejrychlejší a nejoblíbenější. Hodí se pro děti od školky, jen je třeba po koupání vyčistit zip od písku a chlupů.</li>'
          '<li><strong>Elastická šňůrka s pojistkou:</strong> bota se sama přizpůsobí, drží i při běhu a nemá žádné části, které by se mohly zacvaknout o jiné dítě.</li>'
          '<li><strong>Zip na boku:</strong> typický pro neopren, snadno se utáhne, ale písek v zubech vyžaduje důkladné vypláchnutí.</li>'
          '<li><strong>Nazouvací bez zapínání:</strong> pro batolata, kde stačí, aby bota nevyklouzla; pokud sjíždí, vyberte model s pásky přes patu.</li></ul>'
          '<h2>Co vybrat podle věku</h2>'
          '<h3>Batolata a děti do tří let</h3>'
          '<p>Nejlepší jsou měkké ponožky nebo lehké pěnové boty s širokým otvorem. Dítě jim nemusí rozumět, takže bota musí držet bez doladění. Hlídejte, aby podrážka nebyla příliš tuhá a prsty měly místo. Nejmenší děti také rychle ztrácejí teplo, a pokud se koupou delší dobu, pomůže tenký neopren.</p>'
          '<h3>Předškoláci a mladší školáci</h3>'
          '<p>V tomto věku se děti pohybují nejvíc a boty zažívají nejtvrdší zacházení. Hodí se sítové boty na suchý zip s přesahující špičkou, která chrání prsty při kopání do kamenů. Zajímavá je také pryžová podrážka s hlubším vzorem, na kamenech i na lodním molu drží lépe než hladký povrch.</p>'
          '<h3>Starší děti a mladiství</h3>'
          '<p>Ve věku, kdy dítě začne provozovat vodní sporty, přichází ke slovu neopren. Delší pobyt ve vodě chladí nohy i v létě a nízká neoprenová bota je rychle ohřeje. Pro kajak a paddleboard je užitečná podrážka s dobrou přilnavostí a vyztužená špička. Kdo chodí s rodiči do skal a kaňonů, ocení spíš pevnou sítovou botu. Víc o vodních aktivitách najdete v kategorii <a href="/vodni-sporty/">vodní sporty</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Dětské boty do vody mají v nabídce značky ' + B(('reima', 'Reima'), ('konges-sl-jd', 'Konges Sløjd'), ('loap', 'Loap'), ('aquos', 'Aquos'), ('aqua-sphere', 'Aqua Sphere'), ('aquastic', 'Aquastic'), ('aqualung', 'Aqualung'), ('mares', 'Mares')) + '. Rozdíly vycházejí hlavně z původu: Reima a Konges Sløjd jsou značky dětského oblečení a obuvi, takže se soustředí na barvy, pohodlné střihy a snadné obouvání, zatímco Aqua Sphere, Aqualung a Mares vycházejí z plavání a potápění a bývají praktičtější, technicky orientované. Loap a Aquos pokrývají cenově dostupnější a rodinné modely. Dále se objevují například ' + B(('crocs', 'Crocs'), ('adidas', 'Adidas'), ('trespass', 'Trespass'), ('decathlon', 'Decathlon')) + '.</p>'
          '<h2>Na co dát pozor při nákupu</h2>'
          '<ul><li><strong>Podrážka:</strong> hledejte vzorek, který se nepoloží do plochy po jednom kroku, a ohebný materiál, který dítěti nebrání v chůzi.</li>'
          '<li><strong>Odvod vody:</strong> otvory v podrážce nebo síťka nad ní vytlačí vodu a zkrátí dobu schnutí.</li>'
          '<li><strong>Švy uvnitř:</strong> u neoprenu zkontrolujte, zda hrubý šev netlačí na prsty nebo patu.</li>'
          '<li><strong>Barva:</strong> výrazná barva usnadní nalézt botu na břehu a pomůže při hlídání dítěte ve skupině.</li>'
          '<li><strong>UV ochrana:</strong> sluneční záření vyblednou i degradují tenké materiály, takže boty po koupání nedržte na přímém slunci.</li></ul>'
          '<h2>Péče po koupání</h2>'
          '<p>Slaná voda a chlorovaná voda materiály vysušují a boty mohou po týdnu zapáchat. Po každém koupání je vypláchněte pod čistou vodou, vyndejte vložky a nechte je uschnout ve stínu s dostatkem vzduchu. Neoprenové boty obraťte naruby, aby uschla i vnitřní strana, a nesušte je na topení ani na autě za sklem, protože se lepené spoje uvolní. Aby se předešlo plísním na nohou, ať děti nenosí mokré boty po vodě delší dobu a po koupání dostanou suché ponožky a suchou obuv z kategorie <a href="/sandaly/">sandály</a>.</p>'
          '<h2>Ostatní vybavení pro děti u vody</h2>'
          '<p>Boty jsou jen část výbavy. K bezpečné dovolené patří i <a href="/detske-plavky/">dětské plavky</a>, UV oblečení z kategorie <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>, plavecká čepice a doplňky z nabídky <a href="/plazove-doplnky/">plážových doplňků</a>. Pro delší pobyt ve vodě se vyplatí vybrat i <a href="/plavecke-bryle/">plavecké brýle</a> a pro plavání s dlouhými vlasy <a href="/plavecke-cepice/">plavecké čepice</a>.</p>',
    faq=[
        ('Od jakého věku mají děti nosit boty do vody?', 'Pevný věk neexistuje. Batolata, která chodí po kamenité pláži nebo mokré podlaze, mohou nosit měkké ponožky už od první samostatné chůze. Rozhoduje prostředí: u písčité pláže stačí bosé nohy, u kamenů a mol je bota užitečná.'),
        ('Kolik místa nechat na růst?', 'U sítových bot a sandálů asi centimetr před nejdelším prstem, u neoprenu jen půl centimetru, protože se materiál v kontaktu s vodou povolí. Větší rezerva způsobuje, že bota klouže a dítě se o ni zachytává.'),
        ('Jak poznám správnou velikost bez zkoušení?', 'Změřte chodidlo na papíře, přidejte rezervu a porovnejte výsledek s délkou vložky, kterou uvádí výrobce. Číslo na štítku se mezi značkami liší, centimetry jsou spolehlivější.'),
        ('Hodí se neoprenové boty i v létě?', 'Ano, pokud se dítě koupe v chladnější vodě nebo je v ní dlouho, například u jezera, při kajaku nebo na paddleboardu. Na rozpálené pláži a u bazénu stačí lehčí sítová bota nebo ponožka.'),
        ('Jak dlouho boty schnou?', 'Sítové boty a ponožky usychají během několika hodin, neopren trvá déle, zejména uvnitř. Pomáhá vyndat vložky, otočit boty naruby a dát je do stínu s průvanem.'),
        ('Mohu dítěti místo bot do vody dát obyčejné pantofle?', 'Na krátké brouzdání ano, ale gumové pantofle sjíždějí z nohy a v hloubce plavou. Boty do vody mají pásek kolem paty nebo uzavřenou špičku a lépe drží na kluzkých kamenech.'),
        ('Jak vyčistím boty od písku?', 'Nejprve je nechte zaschnout, písek se pak sám vydrolí. Zbytek vypláchněte vlažnou vodou, u suchého zipu pomůže starý kartáček. Zip na neoprenu vypláchněte a zasucho promažte, jen pokud výrobce doporučuje.'),
        ('Proč dětem boty zapáchají?', 'Zápach vzniká z vlhkosti a potu v uzavřeném prostředí. Pomůže vypláchnout boty po každém koupání, vysušit je v průvanu a občas použít jemné mýdlo. Zápach nesmí být důvodem k praní v pračce, tou se poškodí lepení.'),
        ('Mohu boty z mořské vody používat i v bazénu?', 'Ano, ale oplachujte je nejen proti soli, také proti chlóru. V některých plaveckých areálech se nesmí chodit v uličních botách, plavecká obuv a ponožky bývají povoleny, proto se řiďte řádem areálu.'),
        ('Kdy dítě z bot do vody vyroste?', 'Typicky za jednu až dvě sezony. Pokud se noha mezi dvěma koupáními zvětší natolik, že je prst u špičky, boty vyřaďte nebo je předejte mladšímu sourozenci, jen se přesvědčte, že nejsou deformované.'),
    ],
)

# ------------------------------------------------------------------ dakine-batohy
NEW['dakine-batohy'] = dict(
    title='Dakine batohy: modely, objemy a komu se hodí',
    desc='Dakine batohy: městské Campus a 365, školní Grom, snowboardové a cestovní modely. Který objem a styl vybrat a čím se Dakine liší od jiných značek.',
    intro='<p>Dakine je značka, která vyrostla ze surfu a snowboardingu a do městských batohů přenesla praktické přístupy z hor a pláží: dobře dostupné kapsy, odolné materiály a jednoduchý, zřetelně sportovní vzhled. Její batohy se hodí do školy, na dojíždění, na výlety i na cesty. '
          'Na této stránce jsou modely z kategorie <a href="/batohy/">batohy</a>, mezi nimi Campus, 365, Mission, Method, June nebo dětská řada Grom, a také sportovní a cestovní tašky. Průvodce vysvětluje, v čem se jednotlivé řady liší, jaký objem zvolit pro školu, město a víkend, co obnášejí kapsy na notebook a jak Dakine vychází ve srovnání s jinými značkami. Další výběry jsou <a href="/mestske-batohy/">městské</a>, <a href="/skolni-batohy/">školní</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    guide='<h2>Co je pro batohy Dakine typické</h2>'
          '<p>Dakine vznikla v prostředí surfařů a snowboardistů a podle toho její batohy vypadají. Mají zpravidla jednoduchý tvar, pevné záda a množství praktických kapes, které se využijí při přesunu mezi lyžařským svahem, pláží a městem. Materiály jsou odolné vůči otěru a vlhkosti a zipy bývají dimenzované na každodenní zátěž. Vzhled je sportovní, ale ne agresivní, takže se hodí na univerzitu, do kanceláře i do školy.</p>'
          '<p>V nabídce nenajdete jen klasické batohy. Značka má také cestovní tašky Duffle, crossbody tašky, vaky na mokré věci i doplňky a oblečení, které s batohy sdílejí vzhled. Pro tuto stránku je důležité, že hlavní část tvoří městské, školní a sportovní modely, a proto jim věnujeme nejvíc prostoru.</p>'
          '<h2>Řady v nabídce a komu se hodí</h2>'
          + T(['Řada', 'Charakter', 'Hodí se hlavně'], [
              ['Campus', 'velký městský batoh s organizérem, v různých objemech', 'univerzita, škola, dojíždění, víkendová cesta'],
              ['365 Pack', 'jednodušší městský batoh bez zbytečností', 'denní nošení, kancelář, kolo'],
              ['Mission', 'sportovní batoh s pevným tvarem a hlavní komorou', 'město, trénink, lehčí výlet'],
              ['Method', 'tvarem upravený batoh s horním přístupem', 'skatepark, město, škola'],
              ['Grom', 'dětská řada v menším objemu', 'školáci, mladší děti, první batoh'],
              ['June a Wednesday', 'městské batohy s ženskějšími barvami a stylem', 'škola, univerzita, dojíždění'],
              ['EQ Duffle', 'cestovní taška s tvarovaným dnem', 'trénink, sport, krátká cesta'],
              ['Heli Pro a Poacher', 'snowboardové a skialpové batohy', 'freeride, skialp, svah']]) +
          '<p>Seznam modelů se v obchodech mění podle sezony a barev, ale názvy řad se drží několik let a v popisu najdete jejich objem v litrech. Dobré je při srovnání ceny hledat stejný objem i barvu, protože se rozdíly mezi obchody projevují právě tam.</p>'
          '<h2>Objem: kolik litrů pro koho</h2>'
          '<p>Dakine označuje objem přímo v názvu, například Campus 25L nebo Mission 25L. Číslo vyjadřuje součet hlavní komory a kapes, takže skutečně použitelný prostor je o něco menší. Při výběru vyjděte z toho, co nosíte každý den, ne z toho, co by se do batohu mohlo vejít jednou za rok.</p>'
          + T(['Objem', 'Použití', 'Co se vejde'], [
              ['13–18 l', 'mladší děti, malé výlety, ženy bez notebooku', 'svačina, lahev, přezůvky, tenká bunda'],
              ['20–25 l', 'škola, dojíždění, kancelář', 'sešity nebo notebook, oběd, mikina, lahev'],
              ['28–33 l', 'univerzita, trénink, víkend', 'notebook, boty na sport, oblečení na převlečení'],
              ['35 l a víc', 'cestovní taška, sport, víkend', 'sportovní výbava, oblečení na dva až tři dny']]) +
          '<p>Pokud nosíte notebook a sešity, dávejte přednost modelu s pevnou zadní stěnou. Měkké záda se ohýbají podle obsahu a při neopatrném zacházení se displej může zatlačit. Větší batoh nepřidává nosnost, jen vábí k přebalování.</p>'
          '<h2>Kapsy, notebook a organizace</h2>'
          '<p>U Dakine se opakuje stejný přístup: hlavní komora pojme objemnější věci, přední kapsa obsahuje organizér s přihrádkami na tužky, klíče a telefon, a zadní část má polstrovanou kapsu na notebook. Přihlédněte k těmto prvkům:</p>'
          '<ul><li><strong>Velikost notebooku:</strong> ověřte úhlopříčku v popisu, 15palcová kapsa nepojme větší stroj.</li>'
          '<li><strong>Fleecem vystlaná kapsa:</strong> na brýle a telefon, kde by se jinak poškrábal displej.</li>'
          '<li><strong>Boční kapsy:</strong> pro lahev nebo deštník, nejlépe s elastickým okrajem.</li>'
          '<li><strong>Hrudní popruh:</strong> hodí se při jízdě na kole a při delší chůzi; některé modely ho nemají.</li>'
          '<li><strong>Kapsa na hodnoty:</strong> menší kapsa u zad, kam se vejde peněženka a doklady.</li></ul>'
          '<h2>Městský, školní a cestovní provoz</h2>'
          '<p>Pro město vybírejte středně velký batoh s pevnými zády a organizérem. Čisté linie značky se hodí do kanceláře i ke sportovnímu oblečení, ale pokud potřebujete formálnější vzhled, vyberte tmavou jednobarevnou variantu. Ve škole platí zásada, že plný batoh nesmí přetěžovat záda. Pro mladší děti proto stačí řada Grom, u starších žáků a studentů se hodí Campus nebo Mission. Další modely jsou v kategoriích <a href="/skolni-batohy/">školní batohy</a> a <a href="/mestske-batohy/">městské batohy</a>.</p>'
          '<p>Pro cestování mají smysl hlavně cestovní tašky Duffle, které se dají zavěsit na rameno nebo nést jako batoh. Jsou pohodlné pro sport a krátké pobyty, ale pro treky jsou nevhodné, protože jim chybí bederní pás. K nim se hodí i další <a href="/sportovni-tasky/">sportovní tašky</a>.</p>'
          '<h2>Snowboard, lyže a hory</h2>'
          '<p>Značka Dakine se k horám vrací při každé příležitosti. Snowboardové a skialpové modely mají jiný tvar a kapsy než městské batohy: držáky na desku nebo lyže, kapsu na bezpečnostní vybavení a polstrování zad. Pro jízdu mimo vyznačené sjezdovky je ale důležitější správné vybavení a znalost terénu než batoh, a proto se řiďte doporučením horských služeb a nespoléhejte se na jediný prvek. Víc o výběru navazující výbavy najdete v kategoriích <a href="/snowboarding/">snowboarding</a> a <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>.</p>'
          '<h2>Dakine ve srovnání s jinými značkami</h2>'
          '<p>Jestliže váháte mezi Dakine a jinou značkou, rozhoduje účel. Outdoorové firmy se zaměřují na nosné systémy pro několikadenní túry, zatímco Dakine vyniká ve všedním provozu. Pro dlouhou túru se podívejte na stránky <a href="/osprey-batoh/">Osprey</a>, <a href="/deuter-batohy/">Deuter</a> nebo <a href="/the-north-face-batoh/">The North Face</a>. Domácí alternativou v městské a školní třídě jsou <a href="/vuch-batoh/">Vuch</a>, <a href="/batoh-husky/">Husky</a>, <a href="/baagl-batoh/">Baagl</a> a <a href="/oxybag-batoh/">Oxybag</a>. Univerzální výběry podle pohlaví jsou <a href="/pansky-batoh/">pánský batoh</a> a <a href="/damsky-batoh/">dámský batoh</a>.</p>'
          '<h2>Barva a vzhled</h2>'
          '<p>Většina modelů je k dispozici v černé, šedé, tmavě modré a v sezonních barvách. Černá se nejlépe kombinuje a skrývá drobné otěry, ale hůř se v ní hledají věci uvnitř. Světlejší vnitřní podšívka vám pomůže najít klíče. Pokud hledáte nejuniverzálnější variantu, najdete ji v kategorii <a href="/cerny-batoh/">černý batoh</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Batoh vyprázdněte a vytřepejte, drobné skvrny odstraňte vlhkým hadříkem a jemným mýdlem. Pračka poškozuje pěnové vyztužení a potahy, ruční praní ve vlažné vodě je šetrnější. Nechte jej uschnout na vzduchu mimo přímé slunce a vyvarujte se topení. Zipy čistěte kartáčkem a zatížené uzávěry mírně promažte vhodným prostředkem. Při pečlivém zacházení vydrží batoh od značky několik let provozu.</p>'
          '<h2>Pět otázek před koupí</h2>'
          '<ol><li>Co v batohu skutečně nosím každý den a kolik to váží?</li>'
          '<li>Potřebuji kapsu na notebook, a pokud ano, jak velký?</li>'
          '<li>Pojedu s ním na kole nebo ve městě v dešti, takže se hodí pláštěnka nebo voděodolný materiál?</li>'
          '<li>Budu ho nosit celý den, nebo jen dojíždět, takže záleží na polstrování a hrudním popruhu?</li>'
          '<li>Hodí se mi barva, nebo hledám tmavou, kterou nepoznám po roce nošení?</li></ol>'
          '<p>Odpovědi obvykle zúží výběr na jednu nebo dvě řady. Teprve potom se vyplatí porovnávat obchody, protože stejný model v různých barvách se prodává za odlišné ceny a nemusí být všude ve všech provedeních. Ověřte také, zda jde o aktuální kolekci, nebo o starší sezónní edici, která mívá méně barev a může být zajímavější z hlediska ceny.</p>'
          '<h2>Praktické doplňky k batohu</h2>'
          '<p>Ke každodennímu nošení se hodí vodotěsný vak na mokré věci, organizér na kabely a pouzdro na notebook, které přidává ochranu při pádu. Pro kolo je užitečná reflexní pláštěnka přes batoh a při jízdě za tmy přívěsné světlo upevněné na popruhu. Pokud batoh nosíte i na sport, vezměte do něj samostatný sáček na boty, aby se špína nedostala k notebooku a sešitům. Hrudní popruh pomáhá při chůzi se zátěží a drží batoh blíž k tělu.</p>',
    faq=[
        ('Jaký objem Dakine batohu zvolit do školy?', 'Pro základní školu stačí kolem patnácti až dvaceti litrů, pro střední a vysokou školu dvacet pět až třicet tři litrů. Při volbě sledujte formát sešitů a velikost notebooku, ne jen číslo v názvu.'),
        ('Co znamená označení typu 21L nebo 25L?', 'Je to celkový objem v litrech včetně kapes. Skutečně využitelný prostor hlavní komory je o něco menší, protože část objemu zabírá organizér a polstrování.'),
        ('Vejde se do batohu Dakine notebook?', 'Většina městských modelů má vystlanou kapsu na notebook, ale rozměry se liší podle řady. Zkontrolujte úhlopříčku v popisu a nezapomeňte na pouzdro, které přidá několik milimetrů.'),
        ('Jak se liší Campus od 365?', 'Campus je rozsáhlejší, má víc kapes, organizér a nabízí víc velikostí. Řada 365 je jednodušší a lehčí, hodí se na každodenní nošení bez velkých nároků na organizaci.'),
        ('Je řada Grom jen pro děti?', 'Je určena menším uživatelům a menší ramena i záda ji lépe ponesou. Dospělý, který potřebuje malý lehký batoh, ji používat může, ale popruhy jsou kratší.'),
        ('Hodí se Dakine na turistiku?', 'Na krátký výlet ano, ale městské modely nemají bederní pás ani nosný rám. Na několikahodinovou túru s plnou zátěží vyberte turistický batoh z kategorie turistické batohy.'),
        ('Jak poznám, že batoh sedí?', 'Naložte ho několika kilogramy a ověřte, zda popruhy přiléhají k ramenům, záda se opírají o celou plochu a hrudní popruh nestlačuje hrudník. Batoh nesmí při chůzi klouzat ani se houpat.'),
        ('Mohu batoh prát v pračce?', 'Výrobci obvykle doporučují ruční praní ve vlažné vodě s jemným mýdlem. Pračka a sušička mohou poškodit pěnu v zádech a potah, proto je vynechte.'),
        ('Liší se dámské a pánské modely?', 'Jedná se hlavně o barvy a styl, někdy o užší popruhy. U městských batohů je rozdíl menší než u turistických, kde je střih nosného systému zásadní.'),
        ('Kde najdu srovnání cen jednoho modelu?', 'U každého modelu ukazujeme nabídky z více obchodů vedle sebe. Při srovnání dbejte na stejnou barvu a objem, protože se mohou lišit sezónní edice a nabídka velikostí.'),
    ],
)

# ------------------------------------------------------------------ barefoot-boty-damske
NEW['barefoot-boty-damske'] = dict(
    title='Barefoot boty dámské: střih, velikost a výběr',
    desc='Dámské barefoot boty: užší pata, široká špička, nulový drop. Jak změřit nohu, přejít z podpatků a vybrat tenisky, balerínky či zimní boty.',
    intro='<p>Dámská noha má obvykle užší patu a středonoží než pánská a zároveň se v klasické ženské obuvi dlouho tlačí do zúžené špičky a zvednuté paty. Dámské barefoot boty se proto liší od pánských nejen velikostmi, ale i kopytem: paty bývají užší, špička přesto zůstává široká, aby se prsty mohly roztáhnout. '
          'Na této stránce jsou modely z kategorie <a href="/barefoot-obuv/">barefoot boty</a> určené ženám, od městských teniskách přes balerínky a kotníkové boty po sandály a zimní obuv. Průvodce vysvětluje, jak změřit chodidlo, jak přejít z podpatků a jak zvolit boty do kanceláře, na procházky a do zimy. Pánskou nabídku najdete v kategorii <a href="/barefoot-boty-panske/">barefoot boty pánské</a>.</p>',
    guide='<h2>Čím jsou dámské barefoot boty jiné</h2>'
          '<p>Základní vlastnosti barefoot obuvi, tedy široká špička, nulový rozdíl mezi patou a špičkou a ohebná podešev, jsou pro obě pohlaví stejné. U dámských modelů se k nim přidávají úpravy kopyta. Ženské chodidlo je v poměru k délce obvykle užší, zvlášť v patě, a proto se u mužských nebo unisex bot často stává, že pata vyklouzává. Dámské kopyto proto drží patu pevněji, ale špičku necháte dostatečně prostornou.</p>'
          + T(['Vlastnost', 'Dámský model', 'Na co si dát pozor'], [
              ['Špička', 'široká, zaoblená, prostor pro roztažení prstů', 'úzká špička „barefoot stylu“ není skutečný barefoot'],
              ['Pata', 'užší, s fixací proti vyklouznutí', 'u širší nohy zkuste unisex nebo pánský střih'],
              ['Drop', 'nulový, pata a špička ve stejné výšce', 'v popisu hledejte hodnotu v milimetrech'],
              ['Podešev', 'tenká a ohebná, často se vzorkem', 'tenčí podešev víc cítí povrch, silnější chrání před chladem'],
              ['Vzhled', 'balerínky, tenisky, polobotky, sandály', 'širší špička vypadá jinak než klasická štíhlá bota']]) +
          '<p>Označení dámské je vodítko, ne pevná hranice. Žena s širokým chodidlem může být spokojenější v pánském nebo unisex modelu, a naopak štíhlý muž ocení dámskou patu. Rozhodují změřené rozměry, ne štítek.</p>'
          '<h2>Přechod z podpatků a úzkých bot</h2>'
          '<p>Většina žen nosí část života boty se zvýšenou patou nebo úzkou špičkou. Lýtkové svaly a Achillova šlacha se tomu přizpůsobily a při chůzi bez paty se mohou ozvat. Přechod proto musí být postupný a nejde o soutěž, kdo ho zvládne rychleji.</p>'
          '<ul><li>V prvních týdnech noste barefoot boty jen na procházky a do kanceláře, ne na dlouhé túry.</li>'
          '<li>Střídejte je se starou obuví a zvyšujte podíl podle pocitu v lýtkách a chodidlech.</li>'
          '<li>Bolest v lýtkách je signál ke zpomalení, bolest v kloubu je důvod přestat a poradit se.</li>'
          '<li>Procvičujte chodidlo: zvedání prstů, stoj na jedné noze a chůzi po špičkách i po patách.</li>'
          '<li>Při diagnostikovaném problému s chodidlem, kolenem nebo páteří se předem poraďte s ortopedem či fyzioterapeutem.</li></ul>'
          '<p>Pokud jste do té doby nosily vyšší podpatky, vybírejte spíš boty s o něco silnější podešví a mírně měkkou vložkou. Ohebnější a tenčí podešve si nechte na později. Obecný postup přechodu najdete v textu kategorie <a href="/barefoot-obuv/">barefoot boty</a>.</p>'
          '<h2>Práce s vložkami a ponožkami</h2>'
          '<p>Většina barefoot bot má vyjímatelnou vložku, takže si můžete upravit vnitřní prostor. Pokud potřebujete trochu víc místa, vložku vyndejte, ale počítejte s tím, že se změní i výška nohy v botě. Ponožky vybírejte s širokou špičkou, tedy ne sevřené klasické, nebo prstové. Tenký kousek bavlny nebo merina odvádí vlhkost a zabraňuje otěru. Silná ponožka mění cit pro povrch, takže ji nechte na zimu. Při potížích s otlaky pomáhá zkontrolovat, zda je bota dostatečně široká a nezužuje špičku.</p>'
          '<h2>Barefoot pro různé typy nohy</h2>'
          '<p>Úzké chodidlo potřebuje pevnější patu a pásek přes nárt, aby se noha v botě nepohybovala. Širší chodidlo oceňuje měkkou kůži nebo pružný textil, který se přizpůsobí. U vysokého nártu zvolte boty s pružnou jazykovou částí a tkaničkami až dolů. Pokud se vám prsty vyklánějí přes hranu, jde o signál, že potřebujete ještě širší špičku, než jakou nabízí běžné barefoot kopyto. Doplňující rady k výběru obuvi najdete také v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Jak změřit nohu a vybrat velikost</h2>'
          '<p>Barefoot výrobci obvykle uvádějí délku vložky v centimetrech, což je přesnější než číslo na štítku. Změřte si chodidlo večer, kdy je největší, na papíře: postavte se na list, obkreslete nohu svisle vedenou tužkou a změřte vzdálenost od paty k nejdelšímu prstu. Pak přidejte rezervu.</p>'
          + T(['Typ obuvi', 'Rezerva za nejdelším prstem', 'Poznámka'], [
              ['Tenisky a polobotky', 'asi 0,5–1 cm', 'prsty se nesmí opírat o špičku při sestupu'],
              ['Balerínky a nazouvací', 'asi 0,5 cm', 'pata musí zůstat na místě i bez zapínání'],
              ['Sandály s pásky', 'asi 0,5 cm', 'prsty nesmějí přesahovat okraj'],
              ['Zimní boty a kotníčky', 'asi 1–1,5 cm', 'místo na silnější ponožku']]) +
          '<p>Většina barefoot značek nabízí velikostní tabulku podle délky vložky a pokud jsou vaše rozměry mezi dvěma čísly, zvolte větší. Zaměřte se i na šířku: noha musí ležet celou plochou na vložce a okraj nesmí tlačit do prstu. Při online nákupu porovnejte rozměry u více obchodů.</p>'
          '<h2>Typy dámských barefoot bot podle situace</h2>'
          '<h3>Město a kancelář</h3>'
          '<p>Balerínky, polobotky a kožené nazouvací boty v neutrální barvě se hodí do práce i k šatům. Hledejte materiál, který drží tvar a nemá příliš tvrdý okraj, aby se pata neodírala. Stylové modely stále mají širokou špičku, ale linie je upravená tak, aby vypadaly elegantněji než sportovní.</p>'
          '<h3>Tenisky a každodenní nošení</h3>'
          '<p>Nejuniverzálnější volba. Textilní nebo kožená tenisky s tenkou podešví jsou pohodlné na procházky a nákupy. K dalším typům obuvi v nabídce patří <a href="/tenisky/">tenisky</a>, jejichž klasické modely mohou mít zvýšenou patu a užší špičku.</p>'
          '<h3>Léto a sandály</h3>'
          '<p>Otevřené sandály s pásky dovolují prstům maximální volnost. Pásek přes nárt a kolem paty musí držet nohu, aby sandál nesjížděl. Další modely najdete v kategorii <a href="/sandaly/">sandály</a>.</p>'
          '<h3>Zima</h3>'
          '<p>Chlad se do tenké podešve dostává snadněji než u klasické obuvi, a proto se zimní barefoot boty vyrábějí s teplou podšívkou, membránou a mírně silnější podešví. K tomu se hodí vlněné ponožky, které nestlačují prsty. Širší nabídku zimních modelů najdete v kategorii <a href="/zimni-obuv/">zimní obuv</a>.</p>'
          '<h3>Trail, běh a turistika</h3>'
          '<p>Pro lehké trasy existují modely s výraznějším vzorkem a pevnější špičkou. Pokud přecházíte na barefoot běh, začněte krátkými úseky. Doplňkové typy obuvi najdete v <a href="/bezecka-obuv/">běžeckých</a> a <a href="/trekova-obuv/">trekových botách</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V dámských barefoot botách se objevují značky ' + B(('merrell', 'Merrell'), ('vivobarefoot', 'Vivobarefoot'), ('xero-shoes', 'Xero Shoes'), ('be-lenka', 'Be Lenka'), ('leguano', 'Leguano'), ('pegres', 'Pegres'), ('vibram', 'Vibram')) + '. Merrell je outdoorová značka s řadou minimalistické obuvi, Vivobarefoot a Xero Shoes se zaměřují přímo na barefoot, Leguano patří k oblíbeným lehkým modelům do domu a na zahradu a Vibram je známý podrážkami a prstovými botami. Ostatní značky, například ' + B(('aylla', 'Aylla'), ('angles', 'Angles'), ('zazoo', 'Zazoo'), ('blusun', 'Blusun'), ('muris', 'Muris')) + ', nabízejí městské a lehké modely. Střih a šířka se liší podle výrobce, proto je rozumné porovnat velikostní tabulky.</p>'
          '<h2>Na co dát pozor při nákupu</h2>'
          '<ul><li><strong>Označení barefoot:</strong> slovo v názvu nestačí, ověřte drop, šířku špičky a ohebnost.</li>'
          '<li><strong>Vložka:</strong> vyjímatelná vložka umožní zvolit ortopedickou vložku nebo vlastní variantu.</li>'
          '<li><strong>Materiál:</strong> kůže se přizpůsobí noze, textil je lehčí a lépe dýchá, syntetika se hodí na vodu.</li>'
          '<li><strong>Zapínání:</strong> tkaničky, suchý zip nebo guma musí patu držet, ne ji jen obejmout.</li>'
          '<li><strong>Vzorek podešve:</strong> na dlažbě i v lese pomáhá, ale hluboký vzorek tlumí cítění povrchu.</li></ul>'
          '<h2>Péče o barefoot boty</h2>'
          '<p>Kožené modely otírejte vlhkým hadříkem a pravidelně ošetřujte přípravkem proti vodě. Textilní tenisky lze většinou prát na šetrném programu, ale nesušte je u topení. Zachovávejte tenkou podešev: ostré kameny, hřebíky a střepy ji snadno poškodí, takže ji občas zkontrolujte. Po delším provozu se boty vždy vysuší a vyvětrají, aby neměly zápach.</p>',
    faq=[
        ('Jsou dámské barefoot boty jiné než pánské?', 'Ano, mají užší kopyto zejména v patě a o něco kratší velikostní řadu. Principy jsou ale stejné: široká špička, nulový drop a ohebná podešev.'),
        ('Mohu rovnou nosit barefoot boty celý den?', 'Neradí se to. Svaly chodidla a lýtek potřebují čas, takže začněte hodinou denně a čas zvyšujte podle pocitů. U dlouhodobých obtíží se předem poraďte s fyzioterapeutem.'),
        ('Jak změřím velikost pro online nákup?', 'Obkreslete chodidlo na papír, změřte délku k nejdelšímu prstu a přidejte rezervu podle typu obuvi. Porovnejte výsledek s délkou vložky v tabulce výrobce, protože čísla na štítcích se liší.'),
        ('Jaká rezerva je ideální?', 'U tenisek asi půl až jeden centimetr, u zimních bot víc, aby se vešla ponožka. Prsty se nesmějí při chůzi dolů opírat o špičku.'),
        ('Lze v barefoot botách do kanceláře?', 'Ano, existují kožené polobotky a balerínky, které vypadají společensky. Jejich špička je ale širší než u klasické obuvi, což je při zvyku zřejmé.'),
        ('Jsou vhodné do zimy?', 'Zimní modely s teplou podšívkou a membránou ano. Tenká podešev propouští chlad, proto se hodí vlněné ponožky a při dlouhém pobytu venku silnější nebo zateplená podešev.'),
        ('Hodí se při problémech s chodidlem?', 'Barefoot obuv není léčba. Při plochonoží, bolesti paty nebo kolene se nejdřív poraďte s odborníkem, který posoudí, zda a jak přecházet.'),
        ('Mohu v barefoot botách běhat?', 'Ano, ale po několika týdnech chůze a s krátkými úseky. Dopad na střed chodidla a vyšší frekvence kroků jsou jiné než v odpružené obuvi, takže se přizpůsobuje i technika.'),
        ('Jak dlouho trvá, než si na barefoot zvyknu?', 'Je to individuální, obvykle několik týdnů až měsíců. Rychleji si zvyknou ženy, které nosily plochou obuv, déle ty z podpatků. Řiďte se pocitem v lýtkách a chodidlech a nepřidávejte čas, dokud se neztratí únava z předchozího dne.'),
        ('Mohu do barefoot bot vložit ortopedické vložky?', 'Lze, pokud je v botě vyjímatelná vložka a místo po jejím vyndání. Vložka však zvedá nohu a omezuje cit pro povrch, takže se vyplatí záležitost nejdřív probrat s ortopedem, který ji předepsal.'),
        ('Jak barefoot boty čistit?', 'Kůži otírejte vlhkým hadříkem a ošetřujte impregnací, textil perte šetrně. Nesušte u topení ani na přímém slunci, aby se nedeformoval materiál a neuvolnilo lepení.'),
    ],
)

# ------------------------------------------------------------------ cerna-mikina
NEW['cerna-mikina'] = dict(
    title='Černá mikina: střih, materiál a kombinace',
    desc='Černá mikina na zip, s kapucí i fleecová: čím se liší materiály a střihy, jak udržet černou a jak ji kombinovat. Průvodce výběrem pro každý den.',
    intro='<p>Černá mikina je nejméně náročný kus oblečení: nevadí jí drobné skvrny, hodí se ke všemu a stejně dobře funguje v posilovně, na horách i ve městě. Za černou barvou se ale skrývá velký rozdíl v materiálu, střihu a použití. Bavlněná kapucová mikina se chová jinak než tenká funkční nebo fleecová, a také jinak stárne. '
          'Na této stránce jsou černé modely z kategorie <a href="/mikiny/">mikiny</a>, od klasických přes hlavu po zipy, od značek jako Champion, Puma, Adidas nebo Nike až po outdoorové a lyžařské. Průvodce vysvětluje, na co si u černé barvy dát pozor, jak ji praním udržet sytou, jak ji kombinovat a kdy je lepší zvolit jiný materiál. Navazující výběry jsou <a href="/panska-mikina/">pánská mikina</a>, <a href="/nike-mikina/">Nike mikina</a> a <a href="/gap-mikina/">Gap mikina</a>.</p>',
    guide='<h2>Proč je černá mikina tak oblíbená</h2>'
          '<p>Černá je neutrální, prakticky se nedá s ničím pokazit a vypadá upraveně i po delším nošení. Skvrny od jídla nebo mastné šmouhy jsou na ní méně vidět než na světlé. Hodí se jako základní vrstva ke džínům a kalhotám, pod bundu i pod kabát a stejně funguje pro muže, ženy i děti. Ve sportovním provozu navíc nevadí žádné nevyhnutelné otěry od batohu nebo od cyklistických rukavic.</p>'
          '<p>Černá ale má i nevýhody, které je dobré znát předem. Zachytává prach, chlupy a vlákna z jiných látek. Při opakovaném praní se vybledne do šeda a na slunci se rychleji zahřívá než světlá. Ve tmě je zcela neviditelná, což je důležité pro běžce a cyklisty. Tyto věci se dají vyřešit, jen je třeba s nimi počítat při výběru a péči.</p>'
          '<h2>Materiál rozhoduje víc než barva</h2>'
          + T(['Materiál', 'Chování', 'Hodí se na'], [
              ['Bavlna', 'měkká, příjemná, nasákne potem a pomalu schne', 'město, volný čas, doma'],
              ['Bavlna s polyesterem', 'drží tvar, méně se sráží, rychleji schne', 'každodenní nošení, lehký trénink'],
              ['Funkční polyester', 'odvádí pot a rychle schne, lehčí', 'běh, fitness, kolo'],
              ['Fleece', 'teplý a lehký, nenasákne', 'chladné dny, túry, střední vrstva'],
              ['Merino a směsi', 'hřeje i při vlhku, méně zapáchá', 'treky, lyžování, cestování']]) +
          '<p>Barva černá zakrývá strukturu látky, takže rozdíly poznáte spíš hmatem než očima. Zkuste mikinu promnout: hustá česaná bavlna je měkká zevnitř, lehká směs je hladká a tvarově stálá. Pro sport vybírejte materiál podle intenzity. Jemné modely v kategorii <a href="/funkcni-mikiny/">funkční mikiny</a> odvádějí pot, <a href="/fleecove-mikiny/">fleecové mikiny</a> zahřejí, ale nedýchají jako tenký polyester, a <a href="/merino-mikiny/">merino mikiny</a> drží teplo i při vlhku.</p>'
          '<h2>Střihy a typy</h2>'
          '<ul><li><strong>Mikina s kapucí:</strong> klasika, kapuce chrání před větrem a deštěm a hodí se do chladnějších dnů. Přes batoh může tlačit.</li>'
          '<li><strong>Mikina na zip:</strong> umožňuje rychle větrat a svléknout se bez zničení vlasů, vhodná pro sport s proměnlivou intenzitou.</li>'
          '<li><strong>Crewneck, bez kapuce:</strong> čistší vzhled, snadno se vrství pod bundu nebo oblek.</li>'
          '<li><strong>Půlzip nebo stojáček:</strong> chrání krk, často ve fleecovém nebo funkčním provedení na běh a skialp.</li>'
          '<li><strong>Oversize:</strong> volný střih pro město, rukávy pak nesmí zakrývat ruce.</li>'
          '<li><strong>Fanouškovská:</strong> mikiny týmů a lig s logem na hrudi, hlavně z kategorie sportovních dresů.</li></ul>'
          '<p>Při zkoušení zvedněte ruce nad hlavu. Spodní lem se nesmí vyhrnout nad pas a rukávy zůstanou na zápěstí. Přiléhavější střih je vhodný pro sport, volnější pro vrstvení a kombinaci s tričkem navíc.</p>'
          '<h2>Jak udržet černou syté</h2>'
          '<p>Černá mikina vyblednout nemusí, pokud se s ní zachází správně. Hlavními nepřáteli jsou teplo, agresivní prací prášek a tření.</p>'
          '<ol><li>Perte naruby, aby se vnější strana méně otírala o ostatní kusy.</li>'
          '<li>Použijte nižší teplotu, nejlépe třicet stupňů, a prostředek určený pro tmavé prádlo.</li>'
          '<li>Nepřidávejte aviváž k funkčním tkaninám, protože zalepuje vlákna a snižuje odvod potu.</li>'
          '<li>Nesušte v sušičce na plný výkon, vyberte šetrný program nebo rozvěste na vzduchu mimo přímé slunce.</li>'
          '<li>Chlupy a vlákna odstraníte lepicím válečkem nebo vlhkou rukavicí, ne škrábáním.</li></ol>'
          '<p>Pokud už mikina zešedla, existují přípravky na obnovení černé barvy. Funkční syntetické materiály se barví obtížněji než bavlna, takže u nich raději předcházejte bledení šetrnou péčí.</p>'
          '<h2>Viditelnost a bezpečnost</h2>'
          '<p>Černá je za šera a ve tmě téměř neviditelná. Pro běžce, cyklisty a chodce na silnicích proto hledejte modely s reflexními prvky na rukávech, zádech nebo kapuci, nebo přidejte reflexní vestu či pásky z kategorie <a href="/funkcni-tricka/">funkční trika</a> a ostatní oblečení. Platí to zejména pro běžecké a cyklistické mikiny na podzim a v zimě.</p>'
          '<h2>Značky a jejich přístup</h2>'
          '<p>V černých mikinách se objevují hlavně sportovní značky ' + B(('champion', 'Champion'), ('puma', 'Puma'), ('adidas', 'Adidas'), ('nike', 'Nike'), ('under-armour', 'Under Armour'), ('fila', 'Fila'), ('kappa', 'Kappa'), ('jordan', 'Jordan')) + ', které nabízejí klasické střihy s logem a pohodlnou bavlnou. Outdoorové a horské modely vyrábějí ' + B(('fjallraven', 'Fjällräven'), ('helly-hansen', 'Helly Hansen'), ('columbia', 'Columbia'), ('dynafit', 'Dynafit'), ('rossignol', 'Rossignol'), ('regatta', 'Regatta'), ('dare2b', 'Dare2b'), ('viking', 'Viking'), ('kilpi', 'Kilpi'), ('alpine-pro', 'Alpine Pro')) + ', a to často z fleecu nebo funkčního materiálu. Fanouškovské mikiny najdete u ' + B(('fanatics', 'Fanatics'), ('mitchell-ness', 'Mitchell & Ness'), ('outerstuff', 'Outerstuff')) + ' a módní variace u značek ' + B(('gap', 'Gap'), ('tommy-hilfiger', 'Tommy Hilfiger')) + '.</p>'
          '<h2>Jak černou mikinu kombinovat</h2>'
          '<p>Černá se hodí k čemukoli, ale některé kombinace vypadají lépe. Pro sportovní styl ji doplňte tmavými teplákovými kalhotami z kategorie <a href="/teplaky/">tepláky</a> a bílými teniskami. Pro město se hodí džíny, tmavý kabát a čistá obuv. Světlé tričko pod mikinou rozjasní kombinaci, a pokud chcete celý outfit v černé, dodejte kontrast strukturou materiálu, například hladkou bundou nebo žebrovanými kalhotami.</p>'
          '<p>V zimě tvoří černá mikina střední vrstvu pod lyžařskou nebo zimní bundu. Pozor na tlustou kapuci pod bundou: pokud se nevejde pod límec, zvolte model bez kapuce nebo s lehkým stojáčkem. Zimní bundy najdete v kategorii <a href="/zimni-bundy/">zimní bundy</a>.</p>'
          '<h2>Černá mikina pro děti, ženy a muže</h2>'
          '<p>Dětské černé mikiny se hodí do školy, na sport i na hřiště, protože skrývají špínu. Zde je důležitější pevné šití a snadné zapínání než barva: zip s ochranou brady a kapuce bez dlouhých šňůrek, které se mohou zachytit na hřišti. Ženské střihy bývají kratší a užší v ramenou, pánské delší a širší. Mnoho lidí sahá po unisex nebo oversize modelu, a pak záleží hlavně na délce rukávů. Rozdíly detailněji rozebírají stránky <a href="/panska-mikina/">pánská mikina</a> a <a href="/damska-funkcni-mikina/">dámská funkční mikina</a>.</p>'
          '<h2>Sezónní použití</h2>'
          '<p>Na jaře a na podzim stačí lehká bavlněná mikina s kapucí, v zimě funguje jako střední vrstva mezi termoprádlem a bundou. V létě se hodí tenká bez kapuce na chladnější večery u vody. Při lyžování volte funkční mikinu s krátkým zipem, která neomezuje pohyb a dobře odvádí pot. Černý fleece se hodí na túry za chladna, ale při pohybu v mírném počasí se v něm snadno zapaříte. Další variantu představuje lehčí černé tričko z kategorie <a href="/sportovni-tricka/">sportovní trička</a> pod mikinou, které se dá po zahřátí snadno svléknout.</p>'
          '<h2>Jak poznat kvalitní mikinu</h2>'
          '<p>Dobrá mikina má husté, rovnoměrné pletivo bez světlých proužků proti světlu, pevné lemy, které se po natažení vrátí do tvaru, a švy bez přečnívajících nití. Kapuce má být dvouvrstvá, aby držela tvar, a zip jednosměrný s kovovým nebo silným plastovým jezdcem. U potištěných modelů zkontrolujte, zda potisk není nalepený jako tuhá fólie, která praská. Rubová strana prozradí, zda jde o česanou bavlnu, nebo o hladký polyester.</p>'
          '<h2>Na co dát pozor při nákupu</h2>'
          '<ul><li><strong>Gramáž a hustota:</strong> tenká mikina hřeje málo, příliš tlustá se špatně vrství.</li>'
          '<li><strong>Švy a lem:</strong> pevné lemy na rukávech a dole drží tvar, měkké se rychle vytahají.</li>'
          '<li><strong>Potisk:</strong> potištěné logo se při praní může popraskat, výšivka vydrží déle.</li>'
          '<li><strong>Odstín černé:</strong> některé modely mají spíše grafitový nebo antracitový odstín, což prozradí fotografie na denním světle.</li>'
          '<li><strong>Velikostní tabulka:</strong> střihy značek se liší, zvlášť u oversize a přiléhavých modelů.</li></ul>',
    faq=[
        ('Jaká černá mikina se hodí do každodenního nošení?', 'Nejuniverzálnější je bavlněná nebo směsová mikina s kapucí či bez ní, v klasickém střihu. Je příjemná, snadno se kombinuje a drží tvar i po opakovaném praní.'),
        ('Jak zabránit vyblednutí černé mikiny?', 'Perte ji naruby při nízké teplotě s prostředkem na tmavé prádlo, nepoužívejte aviváž a nesušte v silné sušičce ani na přímém slunci. Šetrná péče zachová sytost barvy mnohem déle.'),
        ('Proč se na černé mikině drží chlupy?', 'Černá látka je dobře vidí a statická elektřina z polyesteru je přitahuje. Pomáhá lepicí váleček, vlhká rukavice nebo praní s kouskem nové látky, který nitky zachytí.'),
        ('Je černá mikina vhodná na běhání?', 'Ano, pokud je funkční a má reflexní prvky. Černá je ve tmě špatně vidět, proto přidejte reflexní vestu nebo vybírejte model s reflexními pruhy.'),
        ('Zahřívá se černá mikina na slunci víc?', 'Ano, tmavé látky pohlcují víc záření než světlé. Při letním sportování na slunci je lepší tenká funkční a světlejší vrstva, v zimě naopak černá zahřeje o něco víc.'),
        ('Jak vybrat mikinu na zip nebo přes hlavu?', 'Zip se hodí pro sport s proměnlivou intenzitou a pro vrstvení, protože ji snadno otevřete. Mikina přes hlavu je jednodušší, bez zipu pod bundou netlačí a bývá o něco teplejší.'),
        ('Je fleecová mikina lepší než bavlněná?', 'Pro chlad a pohyb venku ano: fleece je lehčí, nenasákne a rychle schne. Do města a pro pohodlí doma je příjemnější bavlna.'),
        ('Dá se zešedlá černá mikina obnovit?', 'U bavlny pomohou barvy na textil nebo speciální přípravek, u funkčních materiálů je výsledek horší. Lepší je předcházet bledení.'),
        ('Jakou velikost vybrat, když jsem mezi dvěma?', 'U přiléhavého sportovního střihu vezměte větší, aby se vešla vrstva pod mikinou. U oversize střihu naopak menší, jinak bude rukáv delší a ramena spadlá. Ověřte rozměry v tabulce výrobce, obvykle obvod hrudi a délku těla.'),
        ('Co znamená oversize střih?', 'Je to záměrně volnější střih s delším tělem a širšími rameny, nošený ve městě. Pokud ho nechcete, zvolte klasický nebo přiléhavý střih a velikost podle velikostní tabulky.'),
        ('Mohu černou mikinu nosit do kanceláře?', 'Ano, pokud je bez výrazného potisku a z hustšího materiálu, například crewneck v jednobarevném provedení. Pod sako se hodí tenká mikina bez kapuce.'),
    ],
)
