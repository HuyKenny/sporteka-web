"""sporteka.cz — wave 22a (4. 11. 2026): long texts (>= 1650 words) for cyklisticka-obuv, lycra-a-uv-tricka, proteinove-tycinky-a-snacky, lyzarske-vaky-a-tasky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklisticka-obuv
NEW['cyklisticka-obuv'] = dict(long=True,
    title='Cyklistické tretry a boty: silnice, MTB, gravel, zima',
    desc='Cyklistické tretry a boty pro silnici, MTB, gravel i zimu. Jak vybrat podrážku, kufry, zapínání a velikost a porovnat nabídky obchodů.',
    intro='<p>Cyklistická obuv je jediná část výbavy, která přenáší sílu z nohou přímo na pedály, a proto její výběr rozhoduje o pohodlí i efektivitě jízdy. Tuhá podrážka nezmačkává chodidlo při tlaku, kufr drží nohu v ose a pořádné zapínání zabrání otlakům. Sporteka porovnává nabídky českých obchodů u silničních, horských, gravelových, zimních i volnočasových modelů a u příbuzných kousků, jako jsou návleky nebo chrániče na boty. U každé nabídky najdete údaje o kufru a pedálech podle popisu obchodu.</p>'
          '<p>V nabídce převažují značky ' + B(('lake', 'Lake'), ('force', 'Force'), ('sidi', 'Sidi'), ('giro', 'Giro'), ('northwave', 'Northwave'), ('shimano', 'Shimano'), ('fizik', 'Fizik'), ('catlike', 'Catlike')) +
          '. K botám se hodí <a href="/cyklo-pedaly/">pedály</a>, <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> a <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>',
    guide='<h2>Jaké druhy cyklistické obuvi existují</h2>'
          '<p>Základní dělení vychází z typu kola a z toho, jak často z něj sesedáte. Silniční bota je lehká a téměř bez profilu, horská má hrubší podešev a prostor pro kufr, gravelová leží mezi nimi. Další skupinu tvoří boty na ploché pedály, zimní modely a tenisky s mírně tužší podrážkou pro městskou jízdu.</p>'
          + T(['Typ', 'Podrážka a kufr', 'Hodí se pro'], [
              ['Silniční tretry', 'velmi tuhá, často karbon, tříšroubový kufr', 'závodní a výkonnostní jízda na asfaltu'],
              ['MTB tretry', 'tuhá s hrubým běhounem, dvoušroubový kufr', 'terén, kde se chodí a tlačí kolo'],
              ['Gravelové boty', 'střední tuhost, zapuštěný kufr, chůze v blátě', 'dlouhé vyjížďky po štěrku i silnici'],
              ['Boty na ploché pedály', 'lepivá guma, měkčí podešev', 'enduro, downhill, dirt, freeride'],
              ['Zimní cyklistické boty', 'izolace, membrána, vyšší svršek', 'jízda pod bodem mrazu a v dešti'],
              ['Městské a trekingové boty', 'mírně tuhá podešev, vzhled tenisky', 'dojíždění, výlety s častými zastávkami']]) +
          '<p>Chcete-li si typ obuvi ověřit, začněte u pedálů, které na kole máte nebo plánujete koupit. Bota a pedál tvoří pár a dohromady musí fungovat. Pokud ještě nevíte, zda zvolit nášlapné, nebo ploché pedály, přečtěte si text v kategorii <a href="/cyklo-pedaly/">cyklistické pedály</a>.</p>'
          '<h2>Kufry a systémy pedálů</h2>'
          '<p>Kufr je kovová nebo plastová destička, která se přišroubuje na spodek boty a zacvakne do pedálu. Dvoušroubový systém, často označovaný jako SPD, je zapuštěný do podešve, takže se v něm dá snadno chodit. Tříšroubový systém na silničních botách má větší plochu pro přenos síly, ale kufr z podrážky vyčnívá a na dlažbě se chodí nejistě.</p>'
          '<ul><li><strong>Kompatibilita:</strong> kufr musí odpovídat pedálu. Dvoušroubový kufr nezacvakne do silničního pedálu a naopak.</li>'
          '<li><strong>Poloha kufru:</strong> správné seřízení určuje, zda se vám budou bolet kolena a chodidla. Kufr se posunuje po dlouhém otvoru v podrážce a vyplatí se jej doladit po prvních vyjížďkách.</li>'
          '<li><strong>Opotřebení:</strong> plastové kufry se otloukají, zvlášť pokud se v nich často chodí. Včas je vyměňte, jinak hrozí nečekané vypnutí z pedálu.</li>'
          '<li><strong>Kryty kufrů:</strong> silniční boty často mají gumové ochrany, které chrání kufr i podlahu v kavárně.</li></ul>'
          '<h2>Podrážka a tuhost</h2>'
          '<p>Tuhost podrážky se udává různými stupnicemi podle výrobce a nelze je přesně porovnávat mezi značkami. Obecně platí, že karbonová podrážka je tužší a lehčí než nylonová, ale také hůř odpouští při dlouhé chůzi. Nylon, kompozit nebo sklolaminát jsou pružnější, levnější na výrobu a pro rekreační jízdu často pohodlnější.</p>'
          '<p>Příliš tuhá obuv na turistiku nebo pro začátečníky není výhoda. Pokud jezdíte hlavně po okolí a občas se zastavíte na kávu, ocení vaše chodidla střední tuhost a profilovanou podešev. Výkonnostní cyklisté naopak profitují z karbonu, protože se tlak rozloží na větší plochu a nedeformuje chodidlo.</p>'
          '<h2>Zapínání: tkaničky, přezky, BOA a suchý zip</h2>'
          '<p>Způsob zapínání ovlivňuje tvar boty při šlapání i komfort na dlouhých trasách. Moderní tretry kombinují několik systémů a u dražších modelů se používá kolečkový mechanismus s ocelovým lankem, který se otáčí po milimetrech. Tradiční tkaničky jsou lehké, levné a dobře se dotahují, ale při jízdě je nepřitáhnete.</p>'
          + T(['Zapínání', 'Výhoda', 'Nevýhoda'], [
              ['Tkaničky', 'jemné nastavení, nízká hmotnost', 'nedotáhnete za jízdy, mohou se zachytit o řetěz'],
              ['Suchý zip', 'rychlé a levné, snadná obsluha', 'časem ztrácí přilnavost, hůř drží u vysokého tlaku'],
              ['Kolečko (BOA a podobné)', 'plynulé dotahování i za jízdy', 'při poruše bývá nutná výměna celého dílu'],
              ['Ráčnové přezky', 'pevné stažení, snadná výměna', 'vytváří tlakové body, hmotnost']]) +
          '<p>U silničních bot je běžné kombinovat dvě kolečka nebo kolečko s přezkou, u gravelových přibývá suchý zip pro přesné dotažení přes nárt. U širšího chodidla se hodí zapínání, které rozloží tlak po celé délce nártu.</p>'
          '<h2>Velikost, šířka a vložky</h2>'
          '<p>Cyklistické boty mají přesnější střih než běžné tenisky. Noha musí být v botě opřená v patě a prsty mají mít jen malou rezervu, aby se při dlouhé jízdě nezatlačily dopředu. Velikostní tabulky se u různých značek liší, proto vždy porovnejte délku stélky v centimetrech s délkou svého chodidla. Italské značky jako Sidi a Fizik bývají užší, španělské a některé americké pohodlnější v šířce.</p>'
          '<p>Pro široké chodidlo existují modely ve verzi wide a někteří výrobci nabízejí výměnné vložky různé tloušťky. Ortopedické vložky se dají použít, pokud je bota dostatečně hluboká a stélka vyjímatelná. Poraďte se s odborníkem, pokud máte plochonoží nebo bolesti kolen. Dobře sedící bota je totiž základ prevence přetížení při dlouhých trasách.</p>'
          '<h2>Zimní a nepříznivé počasí</h2>'
          '<p>Chodidla jsou na kole nejvíc vystavená chladu, protože se nepohybují tak jako u běhu a proudí kolem nich vzduch. Zimní boty mají izolační vrstvu, často membránu a vyšší manžetu, která zabrání vniknutí vody od kotníku. Výrobci Lake nebo Northwave mají zimní řady známé robustním provedením, jiné značky nabízejí lehčí varianty pro podzim a jaro.</p>'
          '<p>Pokud nechcete kupovat speciální zimní model, použijte neoprenové <a href="/cyklisticke-navleky/">cyklistické návleky</a> na boty a teplé ponožky. Návleky jsou levnější a lépe se hodí pro proměnlivé počasí, ale nevytvoří tak dokonalou bariéru jako izolovaná obuv. V kategorii narazíte také na ochranné přezůvky, které se natahují přes celou botu a chrání před deštěm a větrem.</p>'
          '<h2>Výběr podle stylu jízdy</h2>'
          '<ul><li><strong>Začátečník na silnici:</strong> střední tuhost, suchý zip nebo kolečko, dvoušroubový kufr pro snadnější chůzi a nenáročné pedály.</li>'
          '<li><strong>Závodník:</strong> karbonová podrážka, nízká hmotnost a přesné dotažení. Vyplatí se zkusit víc značek, protože střih je u každé jiný.</li>'
          '<li><strong>Gravel a bikepacking:</strong> chůzeschopná podešev, odolný svršek a prostor na silnější ponožku. Při tlačení kola do kopce oceníte gumový běhoun.</li>'
          '<li><strong>Enduro a downhill:</strong> ploché pedály, měkčí lepivá guma a vyztužená špička proti nárazům o kameny.</li>'
          '<li><strong>Dojíždění do práce:</strong> boty vypadající jako tenisky, které bez problémů obujete v kanceláři.</li></ul>'
          '<h2>Co všechno ještě v kategorii najdete</h2>'
          '<p>Kategorie pokrývá víc než jen silniční tretry: od lehkých závodních bot přes MTB a gravel až po zimní a městské modely. Obuv pro jiné sporty, například <a href="/kopacky/">kopačky</a>, <a href="/bezecka-obuv/">běžeckou obuv</a> nebo <a href="/atletika/">atletické vybavení</a>, hledejte v jejich vlastních kategoriích. Při výběru bot na kolo se orientujte podle značky, typu kufru a pedálu, se kterým se má bota párovat.</p>'
          '<p>Další zboží, které se vejde k botám, jsou chrániče a návleky, sušicí vložky, náhradní kufry a šrouby. Starší kolekce a poslední kusy se prodávají za výhodné ceny, často jen v jedné velikosti, takže se před koupí ujistěte, že vám sedí.</p>'
          '<h2>Péče o cyklistickou obuv</h2>'
          '<ul><li>Po jízdě v dešti boty vyjměte z tašky, vyndejte stélky a nechte je schnout při pokojové teplotě. Nikdy je nesušte na radiátoru ani v blízkosti ohně.</li>'
          '<li>Svršek čistěte vlhkým hadříkem a jemným mýdlem, protože agresivní prostředky poškozují lepené spoje.</li>'
          '<li>Kufry zbavte bláta a jednou za čas je promažte tenkou vrstvou maziva, aby zacvakávání nevrzalo.</li>'
          '<li>Zkontrolujte šroubky kufru a jejich utažení, zvlášť před delší vyjížďkou.</li>'
          '<li>Uložte boty v suchu, mimo přímé slunce, s vloženými novinami, aby si udržely tvar.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Největší chybou je koupit botu bez ohledu na pedály. Dále lidé volí příliš malou velikost, protože chtějí „přiléhavý“ pocit, a po hodině jízdy trpí. Častá je i záměna silničních a horských kufrů nebo pořízení extrémně tuhé karbonové obuvi pro příležitostnou rekreační jízdu.</p>'
          '<p>Rozhodněte se nejdřív podle povrchu a pedálů a až potom podle vzhledu. Pomůže také kompletní výbava: <a href="/cyklisticke-helmy/">helma</a>, <a href="/cyklisticke-rukavice/">rukavice</a> a <a href="/cyklisticke-bryle/">brýle</a>. Kdo cvičí i doma, ocení <a href="/cyklo-udrzba/">údržbové přípravky</a> a pro delší cesty <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka sleduje nabídky českých obchodů a ukazuje, kde je právě dostupná vaše velikost. U bot je to klíčové, protože mnoho kusů se prodává jen v několika velikostech. Porovnávejte stejný model u více prodejců, sledujte dopravu a podmínky vrácení. U obuvi je totiž vrácení běžné a ověřená politika vrácení ušetří starosti, když bota nesedne.</p>',
    faq=[
        ('Jaký je rozdíl mezi silničními a horskými tretry?', 'Silniční tretry mají velmi tuhou podrážku a tříšroubový kufr, který vyčnívá z podešve, takže se v nich špatně chodí. Horské tretry mají dvoušroubový kufr zapuštěný v podrážce a hrubší běhoun, což je praktičtější v terénu a při tlačení kola.'),
        ('Pasují silniční tretry na horské pedály?', 'Ne, systémy se liší počtem šroubů a tvarem kufru. Některé gravelové a MTB boty mají jen dvoušroubový otvor, silniční mají tři šrouby. Před koupí zjistěte, jaký pedál máte.'),
        ('Jak poznám správnou velikost cyklistické boty?', 'Změřte chodidlo a porovnejte délku s velikostní tabulkou značky. Pata má v botě pevně sedět, prsty mají mít malou rezervu. Boty se mezi značkami liší, proto vybírejte podle centimetrů, ne podle čísla.'),
        ('Potřebuji karbonovou podrážku?', 'Pro rekreační jízdu ne. Karbon je lehký a tuhý, ale méně pohodlný při chůzi. Střední tuhost z nylonu nebo kompozitu bude pro většinu cyklistů dostačující.'),
        ('Jak dlouho vydrží kufry na botách?', 'Záleží na tom, jak často po nich chodíte. Plastové kufry se otloukají a časem nedrží stabilně v pedálu. Kontrolujte je pravidelně a vyměňte, pokud je zacvakávání nejisté.'),
        ('Dají se v zimě použít běžné cyklistické boty?', 'Ano, ale s teplými ponožkami a neoprenovými návleky. Pro dlouhé jízdy pod bodem mrazu je lepší izolovaný model s membránou a vyšším svrškem.'),
        ('Jaké zapínání je nejlepší?', 'Záleží na preferencích. Kolečko umožňuje jemné dotahování i za jízdy, suchý zip je jednoduchý a tkaničky lehké. Mnoho bot kombinuje více systémů, aby se tlak rozložil rovnoměrně.'),
        ('Mohu na boty používat ortopedické vložky?', 'Často ano, pokud má bota vyjímatelnou stélku a dost hloubky. Při potížích s kolenem nebo nohou se poraďte s odborníkem. Vložka mění objem boty, takže ji vyzkoušejte při zkoušení velikosti.'),
        ('Jak čistit cyklistické boty?', 'Svršek omyjte vlhkým hadříkem a jemným mýdlem, vyndejte stélky a nechte boty vyschnout při pokojové teplotě. Z kufrů odstraňte bláto a občas je lehce namažte.'),
        ('Podle čeho poznám pravou cyklistickou obuv?', 'Slovo „tretry“ se používá i pro obuv jiných sportů. Cyklistickou obuv poznáte podle zmínky o pedálech, kufrech nebo jízdě na kole v názvu a podle tuhé podrážky s otvory pro kufr.'),
        ('Kolik párů ponožek k botám potřebuji?', 'Stačí dva až tři páry tenkých funkčních ponožek, které střídáte. Bavlna se prosákne potem a způsobuje otlaky, proto zvolte syntetiku nebo merino.'),
        ('Je lepší koupit výprodejový kus?', 'Může to být výhodné, pokud znáte svou velikost a model. U obuvi si ověřte možnost vrácení, protože výprodejové boty často zbývají jen v několika velikostech.'),
    ],
)

# ------------------------------------------------------------------ lycra-a-uv-tricka
NEW['lycra-a-uv-tricka'] = dict(long=True,
    title='Lycra a UV trička do vody: rashguardy pro děti i dospělé',
    desc='Lycrová a UV trička do vody: rashguardy na surf, šnorchlování, potápění i pláž. Jak vybrat střih, rukáv, UV faktor a velikost.',
    intro='<p>Lycrové triko, nazývané také rashguard, je tenká přiléhavá vrstva z elastického materiálu, která chrání kůži před sluncem, otěrem prkna a neoprenu i před podrážděním z medúz. Nosí se na surfu, paddleboardu, při šnorchlování, potápění i prostě na pláži, kde děti vydrží ve vodě hodiny. Sporteka porovnává nabídky českých obchodů a v kategorii najdete pánské, dámské i dětské modely s krátkým a dlouhým rukávem. Přehled je rozdělený tak, abyste rychle našli správný střih i velikost.</p>'
          '<p>Zastoupené jsou značky ' + B(('o-neill', "O'Neill"), ('aqualung', 'Aqualung'), ('scubapro', 'Scubapro'), ('camaro', 'Camaro'), ('quiksilver', 'Quiksilver'), ('rip-curl', 'Rip Curl'), ('speedo', 'Speedo'), ('mares', 'Mares')) +
          '. K tématu se hodí <a href="/plavky/">plavky</a>, <a href="/neopreny/">neopreny</a> a <a href="/plazove-doplnky/">plážové doplňky</a>.</p>',
    guide='<h2>Co je lycra a UV triko a proč ho nosit</h2>'
          '<p>Základem je směs polyesteru nebo nylonu s elastanem, která drží tvar a rychle schne. Plošně přiléhá k tělu, nezvedá se ve vlnách a nedrhne tam, kde se při pádání na prkno otírá hrudník nebo břicho. U modelů s UV ochranou je tkanina hustá a má certifikovaný nebo deklarovaný ochranný faktor, který snižuje množství UV záření procházejícího k pokožce.</p>'
          '<p>Světlo se odráží od hladiny, takže se spálíte i při zatažené obloze. Tričko z lycry vás nezbaví nutnosti používat krém na odkrytých místech, ale výrazně zmenší plochu těla, kterou musíte natřít. Dětem pomáhá hlavně tím, že nemusíte krém každou chvíli obnovovat na zádech a ramenou.</p>'
          '<h2>Typy triček v nabídce</h2>'
          + T(['Typ', 'Charakter', 'Pro koho'], [
              ['Rashguard s krátkým rukávem', 'lehký, přiléhavý, letní', 'pláž, šnorchl, paddleboard v teple'],
              ['Rashguard s dlouhým rukávem', 'chrání ruce, předloktí a otěr o prkno', 'surf, SUP, potápění, děti'],
              ['Tričko s UV ochranou ve volnějším střihu', 'pohodlné, méně přiléhavé', 'rodinná dovolená, vodní hrátky'],
              ['Lycra pro potápění', 'pod neopren a pod vestu', 'potápěči, kajak, jachting'],
              ['Rashguard pro bojové sporty', 'kompresní střih, odolné švy', 'BJJ, MMA, grappling, trénink v tělocvičně'],
              ['Dětské plavecké tričko', 'jednoduchý střih, zip nebo rozevírací zadní díl', 'batolata a školáci u vody']]) +
          '<p>Slovo „lycra“ je mezi výrobci rozšířené, ale zahrnuje i tričko do tělocvičny. Hledáte-li oblečení do vody, hlídejte, aby popis uváděl ochranu před sluncem nebo vodní využití. Pro trénink v tělocvičně nebo chladnější počasí se podívejte i do kategorií <a href="/funkcni-tricka/">funkční trička</a>, <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a> a <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<h2>Střih a rukáv</h2>'
          '<p>Správný střih přiléhá, aniž by tlačil. Příliš volné tričko se ve vodě nafoukne, zvedá se a odkryje záda. Příliš těsné omezuje dýchání a pohyb ramen. U dospělých platí, že rukávy mají končit u zápěstí a spodní lem se nemá zdvihat při předklonu.</p>'
          '<ul><li><strong>Krátký rukáv:</strong> vhodnější do horka a pro plavání, protože necháte volné paže. Předloktí a část paží ale zůstanou nechráněné.</li>'
          '<li><strong>Dlouhý rukáv:</strong> základ pro surf a děti, které stráví ve vodě i na slunci hodiny.</li>'
          '<li><strong>Stojáček a zip:</strong> chrání krk a dá se rozepnout při větších teplotách. U surfu bývá zip na zádech, který neodírá hruď.</li>'
          '<li><strong>Palcové poutko:</strong> udrží rukáv na místě při pádlování a zabrání vyhrnutí.</li></ul>'
          '<h2>Materiál, UV faktor a odolnost</h2>'
          '<p>Hustota úpletu určuje, kolik záření projde skrz. Světlé a řídké tkaniny propouštějí víc než tmavé a hustě pletené. Mnoho výrobců uvádí hodnotu UPF, což je ochranný faktor oblečení. Obecně platí, že čím vyšší, tím větší ochrana, ale hodnota se časem snižuje opotřebením a vytahaností materiálu.</p>'
          '<p>Chlor, slaná voda a opalovací krém poškozují elastan. Po každém použití tričko opláchněte čistou vodou a nechte schnout ve stínu, ne na slunci a ne na radiátoru. Hrubé švy na prkně se opotřebují rychleji, proto vybírejte modely s plochými švy, které při otěru neřežou.</p>'
          '<h2>Výběr podle aktivity</h2>'
          '<h3>Surf a paddleboard</h3>'
          '<p>Při surfování jde především o ochranu před otěrem a sluncem. Tričko s dlouhým rukávem a plochými švy si poradí s vodou i voskem na prkně. Pro paddleboard je důležitá volnost ramen, protože celé pádlování probíhá s rukama nad hlavou. Prkna najdete v kategorii <a href="/paddleboardy/">paddleboardy</a>.</p>'
          '<h3>Šnorchlování a potápění</h3>'
          '<p>U šnorchlování se leží na hladině a záda jsou ozářená bez přestávky. Lycra je proto nezbytná i v teplé vodě. Potápěči ji nosí pod neoprenem, aby se jim snáze oblékal, a také samostatně při krátkém ponoru v teplém moři. Pro další vybavení se podívejte do kategorie <a href="/snorchlovani/">šnorchlování</a> a k plavání na <a href="/plavecke-bryle/">plavecké brýle</a> či <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>'
          '<h3>Děti na pláži</h3>'
          '<p>Dětská pokožka je na sluneční záření citlivější a děti se v mělké vodě drží celé hodiny. Vyberte tričko s dlouhým rukávem, krátkou zipovou lištou nebo rozevíracím zadním dílem, které se snadno oblékne i na mokré tělo. Uvítáte také kombinezony a komplety v kategorii <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h3>Bojové sporty a fitness</h3>'
          '<p>Kategorie obsahuje i kompresní trička pro bojové sporty a trénink. Mají odolnější švy, protože přežijí tahání za rukáv a tření o žíněnku. Do vody nejsou primárně určena, ale pro zápas v tělocvičně se výborně hodí.</p>'
          '<h2>Velikost a vyzkoušení</h2>'
          '<p>Rashguardy mají střih bližší než běžná trička, proto sledujte tabulku výrobce a změřte hrudník, délku trupu a rukávu. Surfové značky mají vlastní velikostní tabulky, které se liší od běžných velikostí. Dětem nekupujte větší velikost než o jednu, protože volné tričko se ve vodě nafukuje a chrání hůř.</p>'
          '<p>Při váhání mezi dvěma velikostmi zvolte menší u dospělých, pokud chcete maximální ochranu a komfort ve vodě. U dětí je lepší střední varianta, která se dá pohodlně obléct i po koupání.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie je přirozeně směsí. Největší část tvoří klasické rashguardy značek jako O\'Neill, Quiksilver nebo Rip Curl, které se vyrábějí pro surfaře a rodiny u moře. Druhá velká skupina patří potápěčským značkám Aqualung, Scubapro a Mares, jejichž lycry jsou střižené pod neopren a vestu. Dále tu jsou sportovní značky Nike a Speedo, dětské kolekce značek Reima nebo Gap a pár specialit, například zateplená lycrová čepice pod přilbu nebo kompresní trička pro bojové sporty.</p>'
          '<p>Barva i design souvisí s ochranou. Tmavé tkaniny pohlcují víc záření, ale i víc tepla, světlé jsou chladnější a na lodi či v moři zároveň viditelnější. Neonové barvy dětem pomáhají, aby je dospělí neztratili z dohledu v davu na pláži.</p>'
          '<h2>Vrstvení a doplňky</h2>'
          '<p>Lycrové triko se často nosí jako spodní vrstva. Pod neoprenem se zmenší tření a obléknete se rychleji. Samotné tričko v lehkém větru po výstupu z vody ochladí, proto mějte po ruce suchou mikinu nebo osušku. U lodí a SUPů přidejte vestu z kategorie <a href="/plovaci-vesty/">plovací vesty</a> a pro děti hlídejte také protiskluzovou ochranu chodidel, například <a href="/obuv-do-vody/">obuv do vody</a>.</p>'
          '<p>Do batohu na výlet k vodě zabalte náhradní suché tričko, voděodolný sáček a ručník. Pokud jedete na delší dovolenou, vezměte aspoň dva kusy, aby se jeden mohl sušit, zatímco druhý používáte. Tričko se vejde do malého prostoru, jen pamatujte, že ochrana závisí na stavu materiálu a mokrá tkanina mívá nižší UPF než suchá.</p>'
          '<h2>Jak poznáte kvalitní kus</h2>'
          '<ul><li>Švy jsou ploché nebo lepené a nezanechávají otlaky na hrudníku ani v podpaží.</li>'
          '<li>Látka se po natažení vrací do tvaru a není prosvítavá.</li>'
          '<li>Výstřih a zip nedrhnou o krk, případně jsou zakryté měkkým lemem.</li>'
          '<li>Popis uvádí složení, doporučenou péči a u UV modelů hodnotu ochranného faktoru.</li>'
          '<li>Velikostní tabulka je konkrétní a nejde jen o označení S, M, L bez rozměrů.</li></ul>'
          '<h2>Pro koho se tričko hodí a pro koho ne</h2>'
          '<ul><li>Pro rodiny s dětmi, které tráví u vody celé dny.</li>'
          '<li>Pro každého, kdo se rychle spálí nebo nechce používat krém na celém těle.</li>'
          '<li>Pro surfaře, paddleboardisty a šnorchlaře, kteří chtějí chránit kůži před otěrem.</li>'
          '<li>Pro lidi, kterým vadí podráždění od medúz nebo mořských vší.</li></ul>'
          '<p>Nahradit nemusí nutně všechny ostatní vrstvy. Pokud plavete v chladné vodě, potřebujete spíš <a href="/neopreny/">neopren</a> a při dlouhém pobytu na lodi nebo plavbě po jezeře doplňte <a href="/cepice-a-celenky/">čepici</a> a brýle.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po koupání tričko opláchněte a nenechte ho zabalené mokré. Neždímejte ho a nekrouťte, protože elastické vlákno ztrácí tvar. Pere se při nízké teplotě, bez aviváže, která zalepuje strukturu a zhoršuje odvod vlhkosti. Sušte ve stínu na ramínku a po sezóně uložte suché a čisté.</p>'
          '<h2>Časté chyby</h2>'
          '<p>Nejčastější chybou je koupit tričko příliš volné, které se ve vodě nadouvá. Další omyl je spoléhat na to, že tričko nahradí krém na obličej a ruce. Také se často přehlíží nutnost pravidelně kontrolovat, zda tkanina není prosvítavá a vytahaná. Když tričko při natažení prosvítá, ochrana klesá.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu, zobrazujeme dostupné velikosti a jednotlivé varianty. Sledujte, zda je tričko určené pro muže, ženy nebo děti, protože střihy se liší. Podle potřeby doplňte i <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/panske-plavky/">pánské plavky</a> nebo <a href="/damske-plavky/">dámské plavky</a>.</p>',
    faq=[
        ('Co je rashguard a k čemu slouží?', 'Je to přiléhavé tričko z elastického materiálu, které chrání pokožku před sluncem, otěrem prkna a neoprenu a před podrážděním od medúz. Rychle schne a ve vodě drží tvar.'),
        ('Je UV tričko dostatečná ochrana před sluncem?', 'Chrání plochy, které zakrývá, ale odkryté části těla je nutné ošetřit krémem. Ochrana také závisí na hustotě tkaniny a jejím opotřebení.'),
        ('Jaký rukáv zvolit?', 'Krátký rukáv je vhodný do horka a pro plavání, dlouhý chrání ruce při surfování, paddleboardingu a u dětí. Pokud trávíte hodiny ve vodě, je dlouhý rukáv praktičtější.'),
        ('Má tričko do vody sedět přiléhavě?', 'Ano. Volné tričko se ve vodě nafoukne a zvedá, takže ztrácí ochranu. Střih má přiléhat, ale nesmí omezovat dýchání ani pohyb ramen.'),
        ('Jak vybrat velikost dětského rashguardu?', 'Podle výšky a obvodu hrudníku v tabulce výrobce. Příliš velké tričko neochrání, takže nekupujte o dvě velikosti větší. Zvolte střih, který se snadno obléká i na mokré tělo.'),
        ('Lze lycru nosit pod neoprenem?', 'Ano, usnadňuje oblékání a snižuje otěr neoprenu o kůži. V teplé vodě ji lze nosit samostatně. Pro chladnější vodu použijte neopren dostatečné tloušťky.'),
        ('Jak prát lycrové triko?', 'Opláchněte po každém koupání, pak perte při nízké teplotě bez aviváže a sušte ve stínu. Slaná i chlorovaná voda poškozuje elastan, proto čistá voda hned po použití prodlužuje životnost.'),
        ('Jsou v kategorii i trička na bojové sporty?', 'Ano, najdete tu kompresní rashguardy pro tréninky v tělocvičně. Mají odolné švy a hodí se na žíněnku. Pro vodu vybírejte modely s popisem plavání nebo surfu.'),
        ('Proč se tričko časem vytahuje?', 'Elastické vlákno ztrácí pružnost vlivem chloru, slané vody, tepla a opalovacího krému. Neschnoucí tričko zabalené v tašce stárne rychleji. Péče o ně zpomalí úbytek ochrany.'),
        ('Hodí se UV tričko i pro dospělé do města?', 'Může, hlavně při pobytu na slunci při sportu nebo cestování. Pro každodenní nošení je ale praktičtější lehké funkční tričko s dlouhým rukávem, které dýchá.'),
        ('Lze lycru použít i do bazénu?', 'Ano, chlor ji ale opotřebovává rychleji, proto ji vždy po plavání vypláchněte. Pro pravidelný trénink v bazénu zvažte plavky určené do chloru.'),
    ],
)

# ------------------------------------------------------------------ proteinove-tycinky-a-snacky
NEW['proteinove-tycinky-a-snacky'] = dict(long=True,
    title='Proteinové tyčinky a snacky: přehled, složení a výběr',
    desc='Proteinové tyčinky, flapjacky, sušenky a slané snacky pro sport. Jak číst složení, porovnat velikost balení a vybrat podle chuti a alergií.',
    intro='<p>Proteinové tyčinky a snacky jsou praktická svačina do tašky, kanceláře i na výlet. Kategorie je pestřejší, než by název napovídal: kromě klasických tyčinek se zde objevují měkké sušenky, ovesné flapjacky, křupavé fazolky, oříškové směsi, chipsy a malé balíčky na cestu. Sporteka porovnává nabídky českých obchodů v jednom přehledu, takže snadno uvidíte, kde je vaše oblíbená příchuť skladem a jak velká jsou balení. Každý výrobek má vlastní složení, proto stojí za to chvíli číst etiketu.</p>'
          '<p>Nejčastější značky jsou ' + B(('gymbeam', 'GymBeam'), ('nutrend', 'Nutrend'), ('amix', 'Amix'), ('mixit', 'Mixit'), ('myprotein', 'MyProtein'), ('enervit', 'Enervit'), ('applied-nutrition', 'Applied Nutrition'), ('powerlogy', 'Powerlogy')) +
          '. Podobné doplňky najdete také v kategoriích <a href="/proteiny/">proteiny</a>, <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>',
    guide='<h2>Z čeho se proteinová tyčinka skládá</h2>'
          '<p>Základem je zdroj bílkovin, nejčastěji mléčný protein, kasein, sójový nebo hrachový izolát, případně směs. K němu se přidávají sacharidy, tuky a pojidla, která dávají tyčince konzistenci. Výrobci používají sirupy, rostlinné oleje, kakao, ořechy, ovesné vločky nebo sušené ovoce. Složení se liší natolik, že dvě tyčinky s podobným názvem mohou mít zcela jiné nutriční profily.</p>'
          '<p>Základní pravidlo čtení etikety: seznam složek je řazený podle množství, takže první položky tvoří nejvíc výrobku. U tyčinky ocení pozorný čtenář také typ sladidla, přítomnost polyolů a zdroj tuku. Tabulka nutričních hodnot ukazuje obsah bílkovin, sacharidů, cukrů, tuků a vlákniny na 100 g i na jednu porci, proto porovnávejte vždy stejné jednotky.</p>'
          '<h2>Druhy výrobků v kategorii</h2>'
          + T(['Druh', 'Typická textura', 'Hodí se'], [
              ['Proteinová tyčinka', 'žvýkací nebo křupavá, často v polevě', 'svačina do tašky, po tréninku'],
              ['Měkká proteinová sušenka', 'větší, sušenková, někdy plněná', 'k čaji nebo kávě, jako sladká odměna'],
              ['Flapjack', 'ovesný, hutný, bez dalších bílkovin nebo s nimi', 'výlety, delší vycházky, snídaně na cestě'],
              ['Wafer a křupavé plátky', 'vrstvené oplatky s krémem', 'pro ty, kdo preferují lehčí chuť'],
              ['Slané snacky', 'křupavé fazolky, hrášek, tyčinky, chipsy', 'alternativa ke sladkému'],
              ['Ořechové a ovocné směsi', 'celé suroviny bez polevy', 'tašky, cestování, turistika']]) +
          '<p>Pokud hledáte rychlý zdroj energie hlavně na vytrvalostní výkon, podívejte se do <a href="/energeticke-gely-a-tycinky/">energetických tyčinek a gelů</a>. Bílkovinný prášek na shake najdete v <a href="/proteiny/">proteinech</a>, doplňky k tréninku v <a href="/predtreninkove-boostery/">předtréninkových boosterech</a> a v <a href="/gainery/">gainerech</a>.</p>'
          '<h2>Jak číst nutriční tabulku</h2>'
          '<ul><li><strong>Bílkoviny na porci:</strong> uvedené množství se týká celé tyčinky, nikoli 100 g. Porovnávejte tedy obojí a všímejte si velikosti balení.</li>'
          '<li><strong>Sacharidy a cukry:</strong> část cukrů může pocházet z ovoce nebo mléka. Sladidla a sirupy najdete v seznamu složek.</li>'
          '<li><strong>Tuky:</strong> nasycené tuky z kokosového či palmového oleje jsou běžné, protože drží polevu a tvar.</li>'
          '<li><strong>Vláknina:</strong> ovesné vločky, ořechy nebo inulin zvyšují sytost, někomu mohou způsobit nadýmání.</li>'
          '<li><strong>Sladidla typu polyoly:</strong> u citlivých jedinců mohou při větším množství působit na trávení.</li></ul>'
          '<p>Obecně jde o doplněk stravy nebo potravinu určenou pro sportovce a aktivní lidi, nikoli o náhradu pestrého jídelníčku. Informace v tomto textu mají obecný charakter a nenahrazují radu lékaře či výživového poradce, zejména pokud máte zdravotní omezení.</p>'
          '<h2>Kdy tyčinka dává smysl</h2>'
          '<p>Tyčinka je pohodlná, když nemáte po ruce plnohodnotné jídlo. V tašce vydrží několik týdnů, nepotřebuje chlazení a nic neteče. Hodí se do kanceláře na odpolední svačinu, na výlet do hor, na cestu autem nebo před tréninkem, když chcete něco malého a nekomplikovaného. Při dlouhé turistice je užitečné mít kromě sladkého i slané a nevázat se na jedinou chuť.</p>'
          '<p>Nejde o kouzelný produkt. Pokud jíte pravidelně a pestře, tyčinka je především pohodlí a chuť. Vyvarujte se ji jíst místo hlavního jídla jen proto, že je to rychlé, a nezapomínejte na pitný režim, který najdete v kategorii <a href="/iontove-napoje/">iontové nápoje</a> a <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>'
          '<h2>Výběr podle chuti, textury a omezení</h2>'
          '<p>Chuť je u tyčinek rozhodující. Některé jsou křupavé s polevou, jiné měkké s karamelovým jádrem, další hutné a ovesné. Při nákupu nového druhu zvolte nejdřív menší balení nebo variantu mix, abyste zjistili, co vám chutná. Výrobci často nabízejí sady různých příchutí, ve kterých najdete čokoládu, arašídy, kokos, ovoce i slané varianty.</p>'
          '<ul><li><strong>Bez lepku:</strong> tyčinky s ovsem, rýží nebo ořechy bývají označené, ale vždy ověřte symbol na obalu, protože sdílená výroba je častá.</li>'
          '<li><strong>Bez laktózy a veganské:</strong> používají rostlinný protein, nejčastěji hrachový nebo sójový. Alergici mají sledovat upozornění na obalu.</li>'
          '<li><strong>Bez přidaného cukru:</strong> nahrazují cukr sladidly, často polyoly, u nichž dbejte na množství.</li>'
          '<li><strong>Alergeny:</strong> ořechy, arašídy, sója a mléko jsou častou složkou. Při alergii si pročtěte celé složení.</li></ul>'
          '<h2>Značky v nabídce a jejich zaměření</h2>'
          '<p>GymBeam a Nutrend patří k nejširším nabídkám v kategorii, prodávají tyčinky, sušenky, flapjacky i slané snacky v několika příchutích. Amix, Mixit a MyProtein cílí na sportovce a fitness komunitu, Enervit a Decathlon nabízejí praktické balení na trénink a výlety. Z menších značek najdete Powerlogy, Oshee, Bombus nebo Topnatur, které se zaměřují na tyčinky z ořechů, ovoce a ovsa. Značky se liší velikostí tyčinek a množstvím bílkovin, proto porovnávejte cenovou nabídku vždy na stejnou porci.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Většina tyčinek má dlouhou trvanlivost a skladuje se při pokojové teplotě. V horku se může poleva rozpustit a v mrazu ztvrdnout, proto je nenechávejte v autě přes léto. Po otevření balíčku ho spotřebujte hned, nebo uložte v uzavřené krabičce. Pokud nabízí obchod výprodej, zkontrolujte datum minimální trvanlivosti na obalu a nenakupujte na zásobu víc, než stihnete sníst.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Hodnocení tyčinky podle nápisu „protein“ na obalu bez čtení tabulky.</li>'
          '<li>Porovnávání ceny balení bez přepočtu na jednu tyčinku nebo na 100 g.</li>'
          '<li>Ignorování alergenů a sladidel u citlivých osob.</li>'
          '<li>Koupě velkého balení neznámé příchuti, která pak zbyde ve skříni.</li>'
          '<li>Spoléhání na tyčinku místo skutečného jídla.</li></ul>'
          '<h2>Tyčinka podle situace</h2>'
          + T(['Situace', 'Na co dbát', 'Typ výrobku'], [
              ['Před tréninkem', 'nic těžkého, malá porce, menší množství tuku', 'lehká tyčinka, ovesný flapjack'],
              ['Po tréninku', 'chuť, pohodlí a možnost zapít', 'proteinová tyčinka nebo sušenka'],
              ['Dlouhá túra', 'odolnost proti horku a rozdrcení', 'flapjack, ořechová směs, slané snacky'],
              ['Kancelář a škola', 'tichý a nekapavý obal, nenápadná chuť', 'tyčinka s polevou nebo křupavé fazolky'],
              ['Cestování', 'trvanlivost a balení po kusech', 'multipack, malé snacky, krabička']]) +
          '<p>U dlouhých túr kombinujte tyčinky s běžným jídlem. Hory a cesty mají vlastní kategorie: <a href="/outdoorova-strava/">outdoorová strava</a>, <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/kemping/">kemping</a>. Aktivním lidem v nabídce chybí snadno snězitelné jídlo, a tak tyčinky velmi dobře doplní svačinový balíček, který držíte po ruce.</p>'
          '<h2>Pozor na marketing na obalu</h2>'
          '<p>Slova „fit“, „lehká“ nebo „bez cukru“ nejsou právně všechno vypovídající. Výrobek může mít málo cukru, ale hodně tuku, a naopak. Sledujte celkovou energetickou hodnotu a také velikost porce. Dvě tyčinky o hmotnosti 35 g a 80 g nelze přímo srovnávat podle obsahu bílkovin na kus. Pomáhá přepočítat hodnoty na 100 g nebo se podívat na procento bílkovin v celkové hmotnosti.</p>'
          '<p>Obal často vyzdvihuje to, co se hodí do reklamy, například příchuť, a skrývá detaily jako sladidla. Pokud nakupujete pravidelně, vyplatí se jednou věnovat pár minut čtení složení a pak se držet jen několika osvědčených druhů. Aktuální dostupnost a nabídky vidíte přímo na Sportece.</p>'
          '<h2>Tyčinka a běžný jídelníček</h2>'
          '<p>Pro většinu lidí je plnohodnotná strava základ a tyčinky jsou doplněk. Bílkoviny můžete získat i z vajec, luštěnin, mléčných výrobků, ryb, masa nebo tofu. Výhodou tyčinky je pohodlnost a stálá chuť. Nevýhodou obvykle vyšší cena za jednu porci než u běžných potravin a často přidaná sladidla. Rozhodněte se podle toho, co vám vyhovuje, a pokud řešíte konkrétní potřeby, například redukci hmotnosti nebo specifickou dietu, obraťte se na odborníka. Informace zde mají pouze obecný charakter.</p>'
          '<h2>Tipy pro nákup do zásoby</h2>'
          '<ul><li>Vyzkoušejte nejdřív malé balení nebo mix příchutí.</li>'
          '<li>Při koupi krabice zkontrolujte datum minimální trvanlivosti.</li>'
          '<li>Sledujte, zda se prodává po kusech nebo po vícekusových baleních.</li>'
          '<li>Porovnejte dopravu a minimální hodnotu objednávky u více obchodů.</li>'
          '<li>Sbírejte oblíbené příchutě a značky do vlastního seznamu, abyste nemuseli stále hledat.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka sbírá nabídky českých obchodů a ukazuje, kde je stejný výrobek dostupný. Porovnávejte nejen cenu za balení, ale také počet kusů v krabici a velikost jedné porce. Sledujte datum spotřeby u slev a pro doplnění nákupu se podívejte do kategorie <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>, <a href="/outdoorova-strava/">outdoorová strava</a> nebo <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>.</p>',
    faq=[
        ('Jsou proteinové tyčinky zdravé?', 'Záleží na složení. Mohou být praktickým zdrojem bílkovin, ale často obsahují také cukry, tuky a sladidla. Čtěte etiketu a berte tyčinky jako doplněk stravy, ne jako náhradu plnohodnotného jídla. V případě pochybností se poraďte s lékařem.'),
        ('Kolik bílkovin má mít dobrá tyčinka?', 'Obsah se liší, běžně se pohybuje od několika gramů po desítky gramů na kus. Vždy porovnávejte hodnoty na porci i na 100 g a sledujte hmotnost celé tyčinky.'),
        ('Jaký je rozdíl mezi proteinovou a energetickou tyčinkou?', 'Proteinová klade důraz na bílkoviny, energetická na rychle dostupné sacharidy pro výkon. Pokud potřebujete zdroj energie při dlouhé aktivitě, hledejte v kategorii energetických tyčinek a gelů.'),
        ('Mohou tyčinky obsahovat alergeny?', 'Ano, často obsahují mléko, sóju, ořechy, arašídy nebo lepek. Alergeny jsou zvýrazněné v seznamu složek. Při alergii čtěte celé složení a upozornění na možné stopy.'),
        ('Co jsou polyoly a proč jsou v tyčinkách?', 'Jsou to sladidla, která dodávají sladkost s nižším podílem cukru. Ve větším množství mohou u citlivých osob dráždit trávení, proto nejezte víc tyčinek najednou a sledujte tabulku složek.'),
        ('Je flapjack proteinová tyčinka?', 'Ne vždy. Klasický flapjack je ovesná tyčinka s tuky a sirupem, ale existují i verze obohacené bílkovinou. Údaje najdete v tabulce na obalu.'),
        ('Kdy se hodí slané snacky místo sladkých tyčinek?', 'Když máte dost sladkého nebo hledáte křupavou alternativu. Sušené fazolky, hrášek nebo ořechy se hodí na cestu a výlet. Mají jiné složení než tyčinky, proto čtěte tabulku.'),
        ('Jak dlouho vydrží tyčinka po otevření?', 'Doporučuje se sníst ji hned. Pokud zbude, uložte ji v uzavřené krabičce při pokojové teplotě. Dodržujte pokyny na obalu a datum minimální trvanlivosti.'),
        ('Mohou tyčinky jíst děti?', 'Obecně jsou určené spíš aktivním dospělým. Pro děti vybírejte jednoduché potraviny a před zařazením sportovní výživy se poraďte s pediatrem.'),
        ('Jak nepřeplatit?', 'Porovnejte cenu na jednu tyčinku a na 100 g mezi obchody, sledujte akce na krabice a zkoušejte nové příchutě v malém balení. Sporteka vám ukáže nabídky vedle sebe.'),
        ('Dají se tyčinky vzít do letadla?', 'Pevné tyčinky a sušenky obvykle ano, ale pravidla se liší podle letiště a země. Tekuté a pastovité výrobky mohou podléhat omezením. Ověřte si podmínky u letecké společnosti.'),
        ('Kde najdu veganské varianty?', 'Hledejte v popisu hrachový nebo sójový protein a označení vegan. Mléčný protein zde nebývá. Ujistěte se i o lepku a ořeších, pokud je potřebujete vyloučit.'),
    ],
)

# ------------------------------------------------------------------ lyzarske-vaky-a-tasky
NEW['lyzarske-vaky-a-tasky'] = dict(long=True,
    title='Vaky a tašky na lyže, boty a snowboard: jak vybrat',
    desc='Vaky na lyže, tašky na lyžařské boty a helmu, obaly na snowboard a skialpové batohy. Jak vybrat délku, polstrování a typ přepravy.',
    intro='<p>Dobrý vak na lyže chrání výbavu při cestě na svah, usnadňuje přenášení a drží pohromadě všechny kusy, které by se jinak rozsypaly po autě. Kategorie zahrnuje jednoduché obaly, polstrované vaky na jeden či dva páry, tašky na lyžařské boty a přilbu, obaly na snowboard, kolečkové kufry, ale také skialpové a skimo batohy. Sporteka porovnává nabídky českých obchodů, takže uvidíte, kde je váš rozměr aktuálně skladem. Texty níže vám pomohou vybrat délku, polstrování i způsob přepravy.</p>'
          '<p>V nabídce najdete značky ' + B(('rossignol', 'Rossignol'), ('dynafit', 'Dynafit'), ('head', 'Head'), ('merco', 'Merco'), ('accezzi', 'Accezzi'), ('arcore', 'Arcore'), ('fischer', 'Fischer'), ('blizzard', 'Blizzard')) +
          '. K přepravě se hodí také <a href="/lyzarske-doplnky/">lyžařské doplňky</a>, <a href="/lyzarske-boty/">lyžařské boty</a> a <a href="/sjezdove-lyze/">sjezdové lyže</a>.</p>',
    guide='<h2>Co všechno kategorie obsahuje</h2>'
          '<p>Přestože je název zaměřený na lyže, nabídka je širší. Základem jsou obaly na sjezdové a běžecké lyže, tašky na boty a přilby a vaky na snowboard. K tomu přibývají specializované kousky: obal na kolečkové lyže, malé pouzdro na biatlonovou zbraň, taška na holínky nebo skialpové batohy s držákem lyží a lavinovým vybavením.</p>'
          + T(['Typ', 'Co pojme', 'Hodí se pro'], [
              ['Jednoduchý obal na lyže', 'jeden pár lyží, někdy hole', 'krátká cesta autem, skladování'],
              ['Polstrovaný vak', 'lyže s vázáním, případně hole', 'cesta autobusem, vlakem, letadlem'],
              ['Dvojitý nebo víceúčelový vak', 'dva páry lyží nebo lyže s hůlkami', 'rodina, společná cesta'],
              ['Taška na boty a přilbu', 'boty, helma, rukavice, brýle', 'přenos k lanovce, hotel, auto'],
              ['Vak s kolečky', 'lyže i další vybavení, vyšší hmotnost', 'letiště, delší přesuny'],
              ['Obal na snowboard', 'prkno a vázání, někdy boty', 'snowboardisté, přeprava v autě'],
              ['Skialpový batoh', 'zimní vrstvy, lavinové vybavení, lyže na zádech', 'skialpinismus a skimo']]) +
          '<p>Skialpinistům jsou určené samostatné kategorie jako <a href="/skialpinismus/">skialpinismus</a>, <a href="/skialpove-lyze/">skialpové lyže</a>, <a href="/skialpove-boty/">skialpové boty</a> a <a href="/skialpove-pasy/">skialpové pásy</a>. Snowboardisté najdou obaly a další vybavení v kategorii <a href="/snowboarding/">snowboarding</a>.</p>'
          '<h2>Jak zvolit délku</h2>'
          '<p>Základní pravidlo zní: vak musí být o pár centimetrů delší než lyže. Rezervu 5 až 10 cm doporučuje většina výrobců, protože špičky a patky vyžadují prostor a zip nemá být napnutý. Nejdřív změřte lyže, ne vak. U vaků s nastavitelnou délkou si ověřte rozsah od minima po maximum.</p>'
          '<ul><li><strong>Dětské lyže:</strong> vak v kratší velikosti se lépe nosí a nezachytává o zem. Pokud dítě rychle roste, vyplatí se model s nastavitelnou délkou.</li>'
          '<li><strong>Carvingové a all-mountain lyže:</strong> většinou stačí standardní délka vaku. Ověřte šířku, protože velmi široké freeride lyže potřebují prostornější obal.</li>'
          '<li><strong>Běžecké lyže:</strong> jsou dlouhé a štíhlé. Existují speciální obaly na několik párů včetně holí.</li>'
          '<li><strong>Víc párů:</strong> dvojitý vak je pohodlnější, ale těžší. Zvažte, kdo ho ponese.</li></ul>'
          '<h2>Polstrování a materiál</h2>'
          '<p>Při cestě autem postačí tenký obal z polyesteru. Pokud lyže převážíte vlakem, v letadle nebo na střeše, hledejte polstrování, zesílené dno a pevné konce. Odolný materiál, například nylon s vyšší hustotou tkaniny, snese tření o schody a podlahu. Voděodolná vrstva je výhodou, ale nepočítejte s tím, že ochrání před silným deštěm.</p>'
          '<p>Kvalitní zip s krytem a přeponky na konci vaku zabrání rozbalení při manipulaci. Pro pohodlné nošení vybírejte modely s vyztuženým popruhem přes rameno a s ramenním polstrováním. Pokud nosíte lyže dlouho, ocení se držadlo uprostřed a kapsa na hůlky, vosk nebo lyžařský pas.</p>'
          '<h2>Taška na lyžařské boty</h2>'
          '<p>Lyžařské boty jsou těžké a nepohodlné na přenášení. Dobrá taška má vyztužené dno, aby si boty zachovaly tvar, a oddělené kapsy na přilbu, rukavice a brýle. Vlhké boty po jízdě vždy vyndejte a vysušte, protože taška s větracími otvory jen omezí zápach, ale boty samotné neusuší. Další popis najdete v kategorii <a href="/lyzarske-helmy/">lyžařské helmy</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a> a <a href="/lyzarske-rukavice/">lyžařské rukavice</a>.</p>'
          '<p>Chcete-li si zajistit pohodlné přenášení, volte tašku s batohovými popruhy. Pro zimní dovolenou je praktická také kombinace tašky na boty a vaku na lyže, protože jednou rukou nesete lyže a druhou boty. Některé modely tvoří sadu.</p>'
          '<h2>Přeprava letadlem, vlakem a autem</h2>'
          '<ul><li><strong>Letadlo:</strong> obvykle je nutné mít lyže v obalu, ale pravidla o rozměrech a hmotnosti se mezi aerolinkami liší. Informace si ověřte u dopravce a zvažte pevné polstrování nebo kufr.</li>'
          '<li><strong>Vlak a autobus:</strong> ocení se pevné popruhy a vyztužené konce, protože vybavení se při manipulaci opírá o stěny.</li>'
          '<li><strong>Auto:</strong> stačí lehký obal, který chrání proti poškrábání a vlhkosti. Na střechu přiložte nosič a obal dobře zajistěte.</li>'
          '<li><strong>Střešní box:</strong> lyže se do něj dávají bez obalu nebo s tenkým chráničem. Zkontrolujte rozměry boxu.</li></ul>'
          '<p>K přepravě v autě se hodí také <a href="/cyklo-nosice-na-auto/">nosiče na auto</a> a pro krátké cesty <a href="/sportovni-tasky/">sportovní tašky</a>. Pokud lyžujete pravidelně, vaky pro starší lyže můžete použít i na uložení přes léto.</p>'
          '<h2>Skialpové a freeridové batohy</h2>'
          '<p>Skialpový batoh má boční nebo diagonální uchycení lyží, kapsu na lavinový set a snadný přístup k vrstvám. Zadní část bývá vyztužená, aby batoh nepřenášel tlak lopaty a sondy do zad. Skimo modely jsou lehčí a štíhlé, protože se jezdí rychle a s minimem vybavení. Dynafit, Kilpi nebo Arcore nabízejí různé objemy podle délky túry a množství vrstev. Další batohy najdete v kategoriích <a href="/batohy/">batohy</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<p>Při výběru objemu počítejte s oblečením navíc, jídlem, pitím, lyžařskými pásy a bezpečnostní výbavou. Zkontrolujte přezky na hrudním a bederním pásu, který musí držet batoh těsně u těla při sjezdu. Prázdné místo v batohu nenechávejte volné, protože se náklad při pohybu přesouvá.</p>'
          '<h2>Obaly na snowboard a další speciality</h2>'
          '<p>Obal na snowboard je užší než lyžařský a často má kapsu pro vázání nebo boty. Kvalitní obaly mají polstrovanou špičku a patku. Pro delší cestu zvolte větší vak, který pojme i helmu a oblečení. Specializované obaly pro kolečkové lyže, biatlonové zbraně nebo boty do lodí a kajaků najdete vyhledáváním podle názvu přímo v této kategorii.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Po cestě vak vyndejte, rozepněte a nechte vyschnout. Zabalené mokré lyže rychle způsobují plíseň a rez na hranách.</li>'
          '<li>Lyže před uložením očistěte a ošetřete voskem z kategorie <a href="/lyzarske-vosky/">lyžařské vosky</a>.</li>'
          '<li>Zip občas ošetřete tukem nebo voskem, aby se neseká.</li>'
          '<li>Skladujte v suchu, mimo přímé slunce.</li>'
          '<li>Zkontrolujte švy a popruhy před každou sezónou.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je koupit vak příliš krátký, který se nedá zapnout nebo se špičky lyží opírají o zip. Další chybou je podcenit polstrování pro let a koupit nejlevnější tenký obal. Lidé také opomíjejí váhu prázdného vaku s kolečky nebo dvojitého vaku, který se při přenášení projeví. Zbytečné je také kupovat tašku na boty, do které se boty a helma společně nevejdou.</p>'
          '<h2>Výběr podle typu lyžaře</h2>'
          + T(['Typ lyžaře', 'Doporučení', 'Na co si dát pozor'], [
              ['Rekreační rodina', 'dvojitý vak a jedna velká taška na boty', 'celková hmotnost, kdo co ponese'],
              ['Dítě a junior', 'kratší vak, případně nastavitelná délka', 'zip, který zvládne dětská ruka'],
              ['Častý cestovatel letadlem', 'polstrovaný vak nebo pevný kufr', 'podmínky dopravce a zámek'],
              ['Skialpinista', 'skialpový nebo skimo batoh s držákem lyží', 'objem, pás, přístup k lavinovému setu'],
              ['Běžkař a biatlonista', 'dlouhý štíhlý obal, případně pouzdro na zbraň', 'délka lyží a hůlek'],
              ['Snowboardista', 'obal na prkno s kapsou pro vázání', 'šířka a polstrovaná špička']]) +
          '<h2>Co zabalit do vaku a co ne</h2>'
          '<p>Ve vaku mají být lyže s vázáním a hůlky, nic těžkého a ostrého. Lyže přenášejte s hranami proti sobě nebo s ochranou hran, aby se při pohybu nepoškrábaly. Pokud je vak měkký, nevkládejte do něj ostré předměty ani těžké boty, protože by tlačily na lyže. Boty patří do vlastní tašky a přilba do kapsy nebo měkké látky.</p>'
          '<p>V létě je dobré do vaku přidat sáčky s vysoušedlem nebo slabou vrstvu papíru, který pohlcuje vlhkost. Neukládejte tam vlhké oblečení a potraviny. Pokud vak používáte také na cesty, vyjměte všechny drobnosti, aby se při schovávání nedeformoval zip a švy.</p>'
          '<h2>Značky a rozdíly mezi nimi</h2>'
          '<p>Rossignol, Head, Fischer a Blizzard jsou výrobci lyží a mají vlastní řady vaků i tašek, které ladí s kolekcí. Dynafit se zaměřuje na skialpinismus a nabízí lehké batohy a obaly. Merco, Accezzi, Arcore, X2 a Artis jsou typické pro širší, cenově dostupnější nabídku, kde najdete základní obaly, tašky na boty i sady. Wedze a Simond patří Decathlonu a míří na rekreační lyžaře a horolezce. Každá značka používá jiný střih a materiál, a proto se vyplatí porovnat rozměry a popis, ne jen název.</p>'
          '<h2>Jak poznat kvalitní vak</h2>'
          '<ul><li>Zip běží hladce a je krytý chlopní proti vodě.</li>'
          '<li>Švy jsou dvojité, zejména u popruhů a rukojetí.</li>'
          '<li>Polstrování je rovnoměrné a nezkroutí se po stlačení.</li>'
          '<li>Popruh přes rameno se dá upravit a nedře.</li>'
          '<li>Obal je dostatečně široký, aby lyže zapadly bez násilného tlačení.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu a ukazujeme různé délky. Mimo sezónu bývají vaky a tašky k dostání výhodněji, na začátku zimy se nejžádanější velikosti vyprodávají rychle. Při nákupu doplňte <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-obleceni/">lyžařské oblečení</a> a <a href="/lyzarske-ponozky/">ponožky</a>, aby výbava byla kompletní.</p>',
    faq=[
        ('Jak dlouhý vak na lyže potřebuji?', 'O 5 až 10 cm delší než lyže. Změřte lyže od špičky po patku a porovnejte s údaji výrobce. U nastavitelných vaků ověřte minimální a maximální délku.'),
        ('Kdy se vyplatí polstrovaný vak?', 'Při přepravě letadlem, vlakem, autobusem nebo při dlouhé cestě, kde se s vybavením manipuluje. Pro krátkou cestu autem stačí jednoduchý obal.'),
        ('Co všechno se vejde do tašky na lyžařské boty?', 'Boty, přilba, rukavice, brýle a drobnosti. Boty by měly být po jízdě vyndané z tašky a vysušené. Vyberte tašku s vyztuženým dnem a oddělenými kapsami.'),
        ('Mohu v letadle převážet lyže ve vaku?', 'Obvykle ano, ale podmínky se u dopravců liší. Zjistěte limity hmotnosti a rozměrů a zvažte vak s polstrováním nebo pevný kufr.'),
        ('Lze do jednoho vaku dát dva páry lyží?', 'Ano, existují dvojité vaky. Jsou pohodlné pro rodinu, ale těžší. Vždy zkontrolujte celkovou šířku a to, zda se do obalu zmenší oba páry včetně hůlek.'),
        ('Co je skimo batoh?', 'Lehký a štíhlý batoh pro skialpinismus a rychlé túry. Má držák na lyže, prostor na vrstvy a lavinové vybavení. Dobře sedí na zádech i při pohybu.'),
        ('Jak vybrat obal na snowboard?', 'Podle délky prkna a šířky vázání. Obal má mít polstrovanou špičku a patku, případně kapsu na boty. Pro cestu letadlem zvolte větší model s polstrováním.'),
        ('Jak vak sušit a skladovat?', 'Po použití vyndejte lyže, rozepněte vak a nechte ho vyschnout. Skladujte v suchu a mimo slunce. Zip občas ošetřete tukem nebo voskem.'),
        ('Hodí se vak s kolečky?', 'Při cestách po letišti nebo nádraží ano, kolečka ulehčí tahání. Počítejte ale s vyšší hmotností prázdného vaku a nutností snést ho po schodech.'),
        ('Mohu lyže uložit přes léto ve vaku?', 'Ano, ale suché a očištěné, s ošetřenými hranami a skluznicí. Vak ukládejte na chladném suchém místě, aby nevznikla plíseň.'),
        ('Proč je v kategorii i taška na helmu nebo holínky?', 'Kategorie sdružuje přepravní obaly pro zimní a outdoorové vybavení. Některé obchody sem řadí i příbuzné tašky, proto se podívejte na popis a rozměry.'),
    ],
)
