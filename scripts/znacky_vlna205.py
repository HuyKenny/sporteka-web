"""sporteka.cz — brand texts wave 205: rossignol, speedo, trespass, fila.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ rossignol
NEW['rossignol'] = dict(
    title='Rossignol: lyžařské bundy, kalhoty, boty a lyže',
    desc='Rossignol v katalogu Sporteky: lyžařské bundy a kalhoty, rukavice, lyžařské boty, sjezdové lyže, běžky a mikiny. Jak vybrat velikost a kdy čekat na slevu.',
    intro='<p>Rossignol je v katalogu Sporteky především zimní značka. Nejpočetnější skupinou jsou <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>, za nimi následují mikiny, <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/sportovni-rukavice/">rukavice</a> a <a href="/lyzarske-boty/">lyžařské boty</a>. Doplňují je <a href="/sjezdove-lyze/">sjezdové lyže</a>, výbava pro <a href="/bezecke-lyzovani/">běžecké lyžování</a> a mimo sezonu také trailové boty nebo funkční trička s dlouhým rukávem. Pánských a dámských kousků je téměř stejně, přibývají i dětské modely a malá část unisex zboží. Stránka vysvětluje, jak se v takovém sortimentu zorientovat: čím se liší sjezdová bota od běžecké, jak složit bundu s kalhotami do jedné sady, na co se dívat u dětské výbavy a kdy se vyplatí sledovat slevy. Vychází z toho, co obchody skutečně nabízejí, ne z marketingových slibů.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Při pohledu na kategorie je vidět, že Rossignol u nás znamená hlavně sněhovou sezonu. Oblečení do mrazu a na svah tvoří většinu nabídky, tvrdá výbava (boty, lyže) je menší, ale pro lyžaře zásadní část. Letní a přechodový sortiment je v pozadí, přesto tu najdete mikiny, kraťasy nebo boty na běh v terénu. Následující přehled ukazuje, kde se vyplatí začít.</p>'
          + T(['Kategorie', 'Pro koho a k čemu', 'Na co se zaměřit'], [
              ['<a href="/lyzarske-bundy/">Lyžařské bundy</a>', 'dospělí i děti, sjezd a snowboard', 'zateplení, kapuce přes helmu, sněhová zástěra, větrání'],
              ['<a href="/lyzarske-kalhoty/">Lyžařské kalhoty</a>', 'sjezdovka i volnější terén', 'délka nohavic, gamaše, zesílení u bot, kapsy'],
              ['<a href="/sportovni-rukavice/">Rukavice</a>', 'celá rodina', 'prstové nebo palčáky, dlouhý manžet, suchý zip na zápěstí'],
              ['<a href="/lyzarske-boty/">Lyžařské boty</a>', 'sjezd, skate i klasika na běžkách', 'velikost podle chodidla, tuhost, šířka lasty'],
              ['<a href="/sjezdove-lyze/">Sjezdové lyže</a>', 'rekreační i sportovní lyžování', 'délka, poloměr, určení pro začátečníky či pokročilé'],
              ['<a href="/mikiny/">Mikiny</a> a <a href="/fleecove-mikiny/">fleece</a>', 'vrstva pod bundu i na každý den', 'zip, kapuce, pružnost, teplo při pohybu'],
              ['<a href="/cepice-a-celenky/">Čepice a čelenky</a>', 'pod helmu i do města', 'tloušťka, uši, kompatibilita s helmou']]) +
          '<p>Mezi pohlavími je rozdělení vyrovnané, takže ať hledáte pánskou, nebo dámskou bundu, vybírat budete z podobného množství modelů. Dětské kousky tvoří menší, ale zřetelnou část, zejména bundy a rukavice. Z barev vede černá, následuje modrá, dále červená, bílá a šedá. Pokud chcete kus, který na svahu vynikne, sáhněte po červené nebo oranžové, pro univerzální vzhled po černé či šedé.</p>'
          '<h2>Lyžařské boty: sjezd a běžky nejsou totéž</h2>'
          '<p>V nabídce jsou dvě odlišné skupiny. Sjezdové boty mají pevnou skořepinu, přezky a tuhý podpatek, aby přenášely pohyb nohy na hranu lyže. Běžecké boty jsou nízké, lehčí a v oblasti kotníku pohyblivější, protože se při odrazu musí pata zvedat. Podle názvů v katalogu poznáte i dva styly běžeckého lyžování: model označený jako skate je pro bruslení po upravené trati, klasický model pro stopu. Vázání, hole a lyže pak musí odpovídat zvolené technice, proto nemíchejte systémy bez ověření v popisu.</p>'
          '<p>U sjezdových bot rozhoduje hlavně kontakt s chodidlem. Bota nemá tlačit na nárty ani na boky, ale zároveň se v ní nesmí pata zvedat. Zkoušejte ji se stejnou ponožkou, v jaké budete lyžovat, a nechte ji aspoň deset minut zapnutou. Přehled zásad najdete také v průvodci kategorie <a href="/lyzarske-boty/">lyžařské boty</a>. V názvech dámských modelů se objevuje písmeno W a různá čísla, která obvykle souvisejí s tuhostí; označení HV u některých kousků ukazuje na širší střih, ale přesný význam si u každého modelu ověřte v popisu obchodu. Dámské boty bývají v lýtku užší a mívají měkčí flex, což vyhovuje lehčím lyžařkám.</p>'
          '<ul><li><strong>Začátečník:</strong> volte měkčí, pohodlnou botu, která odpouští chyby a nemačká prsty.</li>'
          '<li><strong>Pokročilý rekreační lyžař:</strong> tužší model s přesnějším přenosem, ale stále s komfortním vnitřkem.</li>'
          '<li><strong>Široké chodidlo:</strong> hledejte širší střih, jinak bota tlačí na malíku a po hodině bolí.</li>'
          '<li><strong>Dítě:</strong> bota musí sedět už dnes, ne s rezervou na další sezonu, jinak se noha v botě pohybuje a lyžař ztrácí kontrolu.</li></ul>'
          '<h2>Lyžařská bunda a kalhoty jako jedna sada</h2>'
          '<p>Lyžování je zimní sport v pohybu, proto vrstvy fungují lépe než jedna tlustá bunda. Základem je funkční tričko s dlouhým rukávem, nad ním mikina nebo fleece a navrch membránová bunda. V katalogu najdete všechny tři vrstvy od stejné značky, což usnadňuje barvy i střih. Bunda by měla pokrýt pas a mít sněhovou zástěru, kalhoty zase zesílené kolena a nohavice, které sedí přes lyžařskou botu. Zkontrolujte kapsu na skipas, výdechy v podpaží a to, zda je kapuce dost velká na helmu.</p>'
          + T(['Vrstva', 'Úkol', 'Co hledat'], [
              ['První', 'odvádí pot od kůže', 'funkční triko s dlouhým rukávem, ne bavlna'],
              ['Druhá', 'drží teplo', 'fleecová mikina nebo lehká zateplená bunda'],
              ['Třetí', 'chrání před větrem a mokrem', 'lyžařská bunda a kalhoty s úpravou proti sněhu'],
              ['Doplňky', 'chrání končetiny', 'rukavice, čepice, nákrčník, ponožky']]) +
          '<p>Kalhoty se vyrábějí v několika střizích: štíhlejší sportovní, volnější pro snowboard a softshellové pro aktivní chůzi do kopce. Pokud pojedete do mrazivých oblastí, vyberte zateplenou variantu, pokud lyžujete v jarním slunci, stačí tenčí membrána. Sladit barvu bundy s kalhotami není nutné; kontrastní kombinace je dokonce lépe vidět v mlze a při hledání člena skupiny.</p>'
          '<h2>Rukavice, čepice a drobnosti</h2>'
          '<p>Většinu zimních bolestí způsobují zmrzlé prsty. <a href="/sportovni-rukavice/">Rukavice</a> mají mít dlouhý manžet přes rukáv bundy, zesílenou dlaň a prstíky, které dovolí uchopit hůlku nebo zip. Palčáky drží teplo lépe než prstové, protože se prsty ohřívají navzájem, zato s nimi hůř ovládnete telefon. Dětem se hodí rukavice s upínacím páskem na zápěstí, protože je neztrácejí při pádech. Z <a href="/cepice-a-celenky/">čepic a čelenek</a> sáhněte po tenké čepici, která se vejde pod helmu; objemná se do ní nevejde. Čelenka zase vyhovuje při jarním lyžování a při běžkách, kde se hodně potíte.</p>'
          '<h2>Sjezdové lyže a běžky</h2>'
          '<p>Pro rekreační lyžování rozhoduje délka, určení a přizpůsobení terénu. Kratší lyže se snáz zatáčejí, delší jsou stabilnější v rychlosti, proto začátečník volí spíš kratší model. Lyže v katalogu jsou vedeny samostatně, protože obchody je prodávají s vázáním nebo bez něj; v popisu vždy ověřte, co je součástí. Ke správnému nastavení vázání patří odborný servis, nikoli domácí úprava. Pokud nemáte jistotu, vyzkoušejte si lyže v půjčovně nebo je nechte nastavit v servisu podle váhy a zkušenosti.</p>'
          '<p>V kategorii <a href="/bezecke-lyzovani/">běžecké lyžování</a> se potkají boty, hole a lyže. Pro stopu se hodí klasika s méně tuhou botou, pro upravené tratě bruslení s vyšší botou, která drží kotník. Oblečení na běžky bývá tenčí a prodyšnější než na sjezdovku, protože při pohybu vzniká víc tepla. Právě proto se k běžkám hodí lehká fleecová vrstva a větruodolná vesta místo plné zimní bundy.</p>'
          '<h2>Mimo sezonu: trailové boty a běžné oblečení</h2>'
          '<p>V sortimentu se objevují trailové boty pro muže i ženy a pro děti funkční trička. Na rozdíl od silničních bot mají agresivnější vzorek podrážky a pevnější špičku. Pokud je použijete na dlouhý běh, vybírejte o půl čísla větší, protože noha se při sbíhání roztahuje. Mikiny a kraťasy dobře doplní letní trénink; pro běžné nošení jsou vhodné také <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/sportovni-kratasy/">kraťasy</a>. Stejná značka tak vyřeší celý rok, ovšem zimní část sortimentu je zjevně nejsilnější.</p>'
          '<h2>Jak se Rossignol liší od jiných lyžařských značek</h2>'
          '<p>Nejde o srovnání technologií, ale o to, co značka u nás zastupuje. Rossignol pokrývá od bund po lyže celé zimní vybavení, zatímco jiné značky v katalogu bývají specializovanější. Například '
          + B(('salomon', 'Salomon'), ('atomic', 'Atomic'), ('head', 'Head'), ('fischer', 'Fischer')) +
          ' mají silné zastoupení u bot a lyží, kdežto <a href="/znacka/helly-hansen/">Helly Hansen</a> a <a href="/znacka/columbia/">Columbia</a> se soustředí na oblečení. Chcete-li si kombinovat, nic nebrání vzít botu od jedné značky a bundu od jiné, protože střihy oblečení se řídí obecnou velikostní tabulkou. U bot ale držte jednu a tutéž značku jen tehdy, pokud vám sedí.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Oblečení bývá cíleno na sportovní, mírně přiléhavý střih, který ponechá místo na vrstvu pod bundou. Mezi dvěma velikostmi zvolte větší, pokud pod bundu chcete fleece, a menší, pokud ji nosíte jen na funkční triko. Dětské kousky mívají nastavitelný pas a prodloužitelné rukávy, které sezónu prodlouží. Velikost lyžařské boty se udává v mondopointu, tedy délce chodidla v centimetrech. Změřte chodidlo večer, kdy je největší, a porovnejte s tabulkou obchodu.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li><strong>Praní membrán:</strong> jemným prostředkem bez aviváže, aby se neucpaly póry.</li>'
          '<li><strong>Impregnace:</strong> po několika sezonách obnovte vodoodpudivou vrstvu sprejem nebo prací přísadou.</li>'
          '<li><strong>Boty:</strong> po lyžování vyjměte vložky, nechte vyschnout při pokojové teplotě, ne na topení.</li>'
          '<li><strong>Rukavice:</strong> sušte volně, kožené doplňte vhodným voskem.</li>'
          '<li><strong>Uložení lyží:</strong> v suchu, po sezoně nechte opravit hrany a základnu.</li></ul>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Zimní oblečení se zlevňuje na konci sezóny, tedy na jaře, a znovu při obměně kolekce. Nejširší výběr velikostí bývá na podzim, nejnižší cenu často přinese až březen, ovšem s menší nabídkou barev. Boty a lyže mají sezónní vlnu podobně. Sledujte tedy porovnání obchodů na kartě produktu a nepodléhejte tlaku akčních bannerů. Pokud potřebujete konkrétní velikost, kupujte dřív; pokud vám stačí cokoli rozumného, počkejte na výprodej.</p>',
    faq=[
        ('Co všechno od Rossignolu na Sporteka najdu?', 'Převažují lyžařské a snowboardové bundy, mikiny, lyžařské kalhoty, rukavice a lyžařské boty. Dále jsou tu sjezdové lyže, běžecké lyžování, čepice, kraťasy a trailové boty.'),
        ('Jsou boty Rossignol sjezdové, nebo běžecké?', 'Obojí. Sjezdové boty mají pevnou skořepinu a přezky, běžecké jsou nižší a lehčí. V názvu často poznáte i styl, například klasiku nebo skate.'),
        ('Mám brát lyžařskou bundu větší, nebo menší?', 'Pokud nosíte pod bundou fleece, zvolte velikost, která se nepřitahuje v ramenou. Při nošení jen funkčního trička postačí přiléhavější střih. Vždy zkontrolujte tabulku obchodu.'),
        ('Jak poznám, že je lyžařská bota správná?', 'Špičky se nesmějí dotýkat čela a pata se nesmí zvedat. Po deseti minutách v zapnuté botě nemá nic tlačit. Při bolesti zkuste jiný tvar nebo širší model.'),
        ('Vybírá se dětská lyžařská výbava s rezervou?', 'U oblečení ano, nohavice a rukávy se dají zahnout nebo upravit. U bot a rukavic ne: příliš velká bota zhoršuje kontrolu a snadno způsobí pád.'),
        ('Jsou fleecové mikiny vhodné na lyže?', 'Ano jako střední vrstva pod membránovou bundu. Fleece hřeje při pohybu a nasákne méně než bavlna. Do silného větru ale potřebujete vrchní vrstvu.'),
        ('Kdy se vyplatí kupovat lyžařské oblečení?', 'Nejlepší poměr nabídky a ceny bývá na konci zimní sezóny a při obměně kolekce. Chcete-li konkrétní velikost, dejte přednost nákupu na podzim.'),
        ('Jak se starat o membránovou bundu?', 'Perte ji jemným prostředkem bez aviváže, nejlépe s impregnační přísadou. Po několika sezonách obnovte vodoodpudivou vrstvu a bundu vyvěste na ramínko, nikoli do úzkého místa.'),
        ('Mohu kombinovat boty a lyže různých značek?', 'Ano, pokud vázání odpovídá normě podrážky boty. U běžek je nutné držet systém: klasické a bruslařské vázání se liší. Informace hledejte v popisu produktu.'),
    ],
)

# ------------------------------------------------------------------ speedo
NEW['speedo'] = dict(
    title='Speedo: plavky, plavecké brýle, čepice a ploutve',
    desc='Speedo v katalogu Sporteky: plavky pro ženy, muže a děti, plavecké brýle, čepice, ploutve a pomůcky. Jak vybrat velikost, střih a pečovat o plavky.',
    intro='<p>Speedo je v katalogu Sporteky plavecká značka s širokým záběrem. Největší skupinu tvoří <a href="/plavky/">plavky</a>, hned vedle nich stojí <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-cepice/">plavecké čepice</a>, <a href="/ploutve/">ploutve</a> a <a href="/plavecke-pomucky/">plavecké pomůcky</a> jako desky či packy. Zastoupeny jsou i <a href="/obuv-do-vody/">boty do vody</a>, tašky a dětské pantofle k bazénu. Nabídka se opírá hlavně o ženy, v těsném závěsu jsou muži a velkou část tvoří také děti. Průvodce vysvětluje, čím se liší tréninkové plavky od plážových, jak vybrat brýle podle tvaru obličeje, kdy dětem koupit čepici na dlouhé vlasy a co všechno pomáhá plavkám přežít chlór. Informace vycházejí z nabídky obchodů a z obecných zásad plavání.</p>',
    guide='<h2>Co Speedo v katalogu nabízí</h2>'
          '<p>Sortiment je jednoznačně vodní. Plavky se dělí na dámské, pánské a dětské, vedle toho jsou doplňky potřebné u bazénu. Zajímavou skupinou jsou také <a href="/bazeny/">bazény a nafukovadla</a>, která se v katalogu vyskytují pod značkou, a drobné oblečení jako mikiny nebo kraťasy do vody. Následující tabulka usnadňuje začátek hledání.</p>'
          + T(['Kategorie', 'K čemu slouží', 'Na co se zaměřit'], [
              ['<a href="/damske-plavky/">Dámské plavky</a>', 'trénink, bazén, dovolená', 'střih zad, krytí, odolnost vůči chlóru'],
              ['<a href="/panske-plavky/">Pánské plavky</a>', 'plavání i pláž', 'délka nohavice, šněrování, vnitřní podšívka'],
              ['<a href="/plavecke-bryle/">Plavecké brýle</a>', 'bazén i otevřená voda', 'těsnění, zorný úhel, zrcadlový nebo čirý zorník'],
              ['<a href="/plavecke-cepice/">Plavecké čepice</a>', 'bazény s povinnou čepicí', 'silikon nebo textil, dlouhé vlasy'],
              ['<a href="/ploutve/">Ploutve</a>', 'technika nohou a kondice', 'krátké tréninkové, délka, tuhost'],
              ['<a href="/plavecke-pomucky/">Plavecké pomůcky</a>', 'deska, packy, buoy', 'věk plavce a cíl tréninku'],
              ['<a href="/obuv-do-vody/">Boty do vody</a>', 'bazén, pláž, šatna', 'protiskluz, rychlé schnutí']]) +
          '<p>Převažují černé, modré a vícebarevné kousky, ale najdete i červenou, bílou nebo zelenou. Černá je nejodolnější vůči vybledlým barvám, vícebarevné vzory nesou známky chlóru hůř, ale jsou veselejší. Dětské modely často dekorují postavy a barvy, aby je děti rády nosily.</p>'
          '<h2>Tréninkové plavky vs. plážové</h2>'
          '<p>Rozdíl je v materiálu a střihu. Tréninkové modely jsou z tkaniny, která má v chlóru vydržet víc než běžná elastická. Střih je přiléhavý, aby voda nebrzdila, nohavice nebo ramínka se nezařezávají a pohyb rukou je volný. Plážové a rekreační modely dávají přednost designu, vyšší pasu nebo volnějšímu střihu a časem se v chlórované vodě opotřebují rychleji. Pokud plavete pravidelně, mít dva tréninkové kusy na střídání je praktičtější než jeden výjimečně drahý.</p>'
          '<p>Pánské střihy najdete od plavek s krátkou nohavicí přes aquashorty až po volné kraťasy. Plavecký trénink obvykle vyžaduje přiléhavé střihy, volné kraťasy slouží k pláži a nafukovacímu bazénu. Dámské jednodílné kostýmy mají odlišné zády, od klasických přes ramínka křížená do tvaru X po širší a krycí. Pro začátečnici je dobré vybrat střih s pevnějším záhybem v ramenou, který nesjíždí při obrátce. Další tipy najdete na stránce <a href="/speedo-plavky/">Speedo plavky</a>.</p>'
          '<h2>Jak vybrat plavecké brýle</h2>'
          '<p>Brýle musí především těsnit. Zkouška je jednoduchá: přitlačte zorníky lehce k očím bez pásku a odtáhněte ruku. Pokud se přisají a drží několik vteřin, tvar sedí. Pak nastavte pásek tak, aby se brýle nepohybovaly, ale netlačily na spánky. Zrcadlové zorníky se hodí na slunce a venkovní bazén, čiré nebo světlé v hale, tmavé při silném světle. U antifog úpravy platí, že ji nevytírejte prstem ani utěrkou, jinak se rychle ztratí.</p>'
          '<ul><li><strong>Trénink:</strong> nižší profil, přiléhavé těsnění, menší odpor vody.</li>'
          '<li><strong>Rekreace:</strong> měkké těsnění a širší zorné pole, které snese celodenní nošení.</li>'
          '<li><strong>Děti:</strong> model označený junior, s jemnějším těsněním a menším nosním můstkem.</li>'
          '<li><strong>Otevřená voda:</strong> větší zorníky a viditelnější barva pásku pro záchranáře.</li></ul>'
          '<p>Dětské brýle se v katalogu liší tvarem i velikostí oproti dospělým, proto je nekupujte s rezervou. Příliš velký zorník dítěti prosakuje a plavání mu znechutí. Na zvyknutí se hodí brýle s výrazným designem; pokud dítě nemá rádo vodu v očích, nacvičujte hravě v mělké vodě.</p>'
          '<h2>Plavecké čepice a dlouhé vlasy</h2>'
          '<p>Čepice drží vlasy z obličeje a snižuje odpor vody. Silikonové čepice jsou odolné, snadno se obléknou a nepropouštějí vodu. Textilní jsou měkčí a pohodlnější, ale propouštějí. V katalogu jsou i čepice určené na dlouhé vlasy, mají objemnější tvar a snáz se obléknou. Vlasy sepněte do culíku nebo copu, potom čepici přetáhněte od čela dozadu. Po plavání ji propláchněte sladkou vodou a nechte okapat, před uložením ji nechte uschnout.</p>'
          '<h2>Ploutve a pomůcky pro lepší techniku</h2>'
          '<p>Ploutve nejsou jen pro potápění. Krátké tréninkové ploutve učí plavce správnému kopu a posilují nohy, aniž by příliš zvedaly tempo. Pro děti vybírejte kratší model, aby nepřetížily kotník. Nejdůležitější je pohodlné nasazení patní části, která nesmí škrtit. Mezi pomůckami najdete desku na nácvik kopání, packy na posílení záběru nebo vak na mokré věci. Používejte je cíleně, ne všechny najednou, jinak plavec ztratí cit pro vodu.</p>'
          + T(['Pomůcka', 'Účel', 'Pro koho'], [
              ['Plavecká deska', 'nácvik kopu nohou', 'začátečníci i pokročilí'],
              ['Packy', 'zesílení záběru, korekce techniky', 'pokročilí plavci'],
              ['Krátké ploutve', 'kop a posilování nohou', 'všichni, děti kratší'],
              ['Vak na plavání', 'přeprava mokrých věcí', 'všichni']]) +
          '<h2>Děti a plavání</h2>'
          '<p>Dětský bazénový den potřebuje plavky, brýle, čepici a boty do vody, aby dítě neklouzalo po mokrých dlaždicích. Protiskluzové pantofle jsou praktické i v šatně. Pro nejmenší vybírejte plavky s lehkým pasem a bez zbytečných ozdob, které se zachytí o schod. Děti rostou rychle, proto pečlivě kontrolujte velikost každou sezonu. Plavky, které se při roztažení zdají těsné, se později v chlóru ještě mírně rozšíří, ale stále musí sedět tak, aby neškrtily.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Plavky se vybírají přiléhavě, protože ve vodě tkanina povolí. Pokud váháte mezi dvěma velikostmi, pro plavání je lepší menší, pro odpočinek u vody větší. Měřte hrudník, pas a boky a porovnejte s tabulkou na kartě produktu. Dámské i pánské modely mají vlastní velikostní řadu. U dětí vybírejte podle výšky a obvodu hrudníku.</p>'
          '<h2>Péče o plavky a doplňky</h2>'
          '<ul><li><strong>Po každém koupání:</strong> opláchnout v čisté vodě, aby se vymyl chlór a sůl.</li>'
          '<li><strong>Praní:</strong> ručně, jemným prostředkem, nežmoulat ani nekroutit.</li>'
          '<li><strong>Sušení:</strong> ve stínu, ne na radiátoru ani na přímém slunci.</li>'
          '<li><strong>Brýle:</strong> nedotýkat se zorníků prsty, uložit do pouzdra.</li>'
          '<li><strong>Střídání:</strong> druhý kus plavek se suší, zatímco používáte první, tkanina se rychleji obnoví.</li></ul>'
          '<h2>Jak se Speedo liší od jiných plaveckých značek</h2>'
          '<p>Nejde o technické srovnání. Speedo nabízí široký záběr od dětských brýlí po závodní doplňky, zatímco jiné značky se zaměřují na užší výběr. '
          + B(('arena', 'Arena'), ('zoggs', 'Zoggs'), ('finis', 'Finis'), ('aqua-sphere', 'Aqua Sphere')) +
          ' nabízejí také brýle a trénink, '
          + B(('nike', 'Nike'), ('adidas', 'Adidas')) +
          ' spíš plavky ve sportovním stylu. Kdo hledá plavky na dovolenou, projde i další značky, kdo trénuje, srovná střih a materiál.</p>'
          '<h2>Co sbalit k bazénu</h2>'
          '<p>Kdo chodí plavat pravidelně, ocení pevný seznam věcí. Do tašky patří plavky, brýle, čepice, ručník, přezůvky a lahev s vodou. Mokré věci uložte do samostatné kapsy nebo do vaku, aby nenavlhl zbytek tašky. Po plavání je vyjměte hned, jinak začnou zatuchle zapáchat a plavky ztrácejí pružnost. Děti potřebují navíc náhradní spodní prádlo a něco teplého na převlečení, protože po bazénu rychle vychladnou. Dobrý zvyk je mít tašku vždy hotovou, aby se na trénink nezapomnělo na nic důležitého.</p>'
          '<h2>Pláž, dovolená a otevřená voda</h2>'
          '<p>Na dovolenou nemusíte brát závodní kousky. Pohodlnější je volnější střih, který se nepoškodí při sedání na kámen, a sluneční brýle z kategorie <a href="/sportovni-bryle/">sportovní a sluneční brýle</a>. Sůl a písek plavky ničí stejně jako chlór, takže i po moři je opláchněte sladkou vodou. Při plavání v otevřené vodě pomáhá plavecká čepice v nápadné barvě a brýle s větším zorným polem. Boty do vody ochrání chodidla před ostrými kameny. Pro děti u vody platí, že dohled dospělého je důležitější než jakákoli výbava.</p>'
          '<h2>Jak zvolit výbavu podle cíle</h2>'
          '<p>Pokud chcete jen rekreačně plavat, stačí jedny plavky, pohodlné brýle a čepice. Při tréninku na techniku přidejte desku a krátké ploutve, při kondičním plavání packy. Pro začínající děti zvolte brýle a ploutve až poté, co se naučí dýchat a plavat bez nich; vybavení má pomáhat, nikoli nahrazovat techniku.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Plavky se zlevňují na konci léta a v zimě před novou kolekcí. Brýle a čepice mívají slevy celoročně, protože se jejich design obměňuje pomaleji. Pomůže sledování karty produktu: porovnání obchodů ukáže, kdy cena klesla. Nejširší výběr velikostí bývá na jaře, kdo potřebuje konkrétní střih, nenechá si ho na výprodej.</p>',
    faq=[
        ('Co všechno od Speedo najdu na Sporteka?', 'Hlavně plavky, plavecké brýle, čepice, ploutve a pomůcky. K tomu boty do vody, tašky a dětské kousky. Nabídka zahrnuje ženy, muže i děti.'),
        ('Jak vybrat plavecké brýle?', 'Přitlačte zorníky k očím bez pásku. Když se přisají, tvar sedí. Potom upravte pásek tak, aby nebyl příliš těsný. Zrcadlové zorníky vybírejte na slunce.'),
        ('Čím se liší tréninkové plavky od plážových?', 'Tréninkové jsou přiléhavé a z materiálu odolnějšího vůči chlóru. Plážové dávají přednost designu a pohodlí. Pro pravidelné plavání proto volte první typ.'),
        ('Jak pečovat o plavky, aby vydržely?', 'Po koupání je opláchněte sladkou vodou, perte ručně a sušte ve stínu. Nesušte je na radiátoru a nežmoulejte je. Střídání dvou kusů prodlužuje životnost.'),
        ('Mám dítěti koupit brýle větší na růst?', 'Ne. Příliš velký zorník netěsní a přivádí vodu do očí. Raději kupte juniorskou velikost a po sezoně ji vyměňte.'),
        ('Potřebuji plaveckou čepici i s dlouhými vlasy?', 'Ano, v mnoha bazénech je povinná. Na dlouhé vlasy hledejte model s větším objemem, vlasy sepněte a čepici přetáhněte od čela dozadu.'),
        ('K čemu jsou plavecké ploutve a packy?', 'Ploutve cvičí kop a posilují nohy, packy zesilují záběr. Používejte je cíleně, ne po celou dobu tréninku, aby se nenarušil cit pro vodu.'),
        ('Kdy se plavky nejvíc zlevňují?', 'Nejčastěji na konci léta a před novou kolekcí. Při pozdním nákupu ovšem ubývá velikostí, proto si na konkrétní střih netroufněte čekat.'),
        ('Jsou boty do vody potřeba?', 'U bazénu hlavně pro děti, protože protiskluzová podrážka brání pádům na mokrých dlaždicích. Hodí se také na pláž s kameny a do šatny.'),
    ],
)

# ------------------------------------------------------------------ trespass
NEW['trespass'] = dict(
    title='Trespass: outdoorové bundy, fleece, boty a zimní oblečení',
    desc='Trespass v katalogu Sporteky: jarní, nepromokavé a zimní bundy, fleecové mikiny, trekové a zimní boty i dětské oblečení. Jak vybrat vrstvy a velikost.',
    intro='<p>Trespass je v katalogu Sporteky outdoorová značka pro celou rodinu. Nejpočetnější jsou <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, dále <a href="/nepromokave-bundy/">nepromokavé bundy</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/zimni-bundy/">zimní bundy</a> a <a href="/trekova-obuv/">trekové boty</a>. Doplňují je lyžařské bundy, softshell, kalhoty, kraťasy, tílka a zimní boty. Pánský a dámský sortiment je téměř vyrovnaný, třetinu až čtvrtinu tvoří dětské kousky. Pozoruhodná je převaha hnědých a béžových tónů v kombinaci s černou a modrou. Průvodce vysvětluje, jak z takové nabídky složit funkční vrstvy na výlet, jak vybrat bundu podle počasí, čím se liší softshell od membránové bundy a kdy se vyplatí čekat na slevu. Opírá se o to, co značka v nabídce skutečně má.</p>',
    guide='<h2>Co značka v nabídce zastupuje</h2>'
          '<p>Trespass pokrývá střední třídu turistiky a každodenního oblečení do nepohody. Typickým kouskem je bunda, která skládá do kapsy, fleecová mikina na chladné večery nebo zateplená bunda do města. Hlavní kategorie shrnuje tabulka; u každé se hodí vědět, na co se v popisu soustředit.</p>'
          + T(['Kategorie', 'Pro jaké počasí', 'Na co se dívat'], [
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'chladno, mírný vítr, přeháňky', 'střih, kapuce, skládání do kapsy'],
              ['<a href="/nepromokave-bundy/">Nepromokavé bundy</a>', 'déšť a vytrvalá mokrá zima', 'zalepené švy, vodní sloupec v popisu, větrání'],
              ['<a href="/softshellove-bundy/">Softshellové bundy</a>', 'vítr a aktivní pohyb', 'pružnost, prodyšnost, vodoodpudivost'],
              ['<a href="/zimni-bundy/">Zimní a péřové bundy</a>', 'mráz a pomalá chůze', 'výplň, kapuce, délka, zip s chlopní'],
              ['<a href="/lyzarske-bundy/">Lyžařské bundy</a>', 'sjezdovka, mokrý sníh', 'sněhová zástěra, kapsa na skipas'],
              ['<a href="/fleecove-mikiny/">Fleecové mikiny</a>', 'střední vrstva a chladné večery', 'tloušťka, zip, váha'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'stezky a výlety', 'podešev, výška kotníku, vodotěsnost']]) +
          '<p>Barevně převažuje hnědá, což se u outdoorové značky vidí málokdy. Přináší přírodní, zemitý vzhled, vhodný na každodenní nošení ve městě, a to i bez zvláštního sportovního charakteru. Následuje černá, modrá a šedá, růžová se nejčastěji objevuje u dámských a dětských kousků.</p>'
          '<h2>Vrstvení: jak složit oblečení na výlet</h2>'
          '<p>Základní pravidlo outdoorového oblékání zní: raději tři tenké vrstvy než jedna tlustá. Spodní odvádí pot, střední drží teplo, vrchní chrání před větrem a deštěm. U Trespassu najdete střední i vrchní vrstvu pohromadě, takže je snadné sladit střih a barvu. Při chůzi do kopce vrstvu sundejte dřív, než se zapotíte; pot se v chladu mění v zimu.</p>'
          + T(['Počasí', 'Doporučené složení', 'Poznámka'], [
              ['Chladné jaro a podzim', 'tričko, fleece, lehká bunda do kapsy', 'bunda se vejde do batohu'],
              ['Deštivý den', 'tričko, nepromokavá bunda, nepromokavé kalhoty', 'zkontrolujte větrání v podpaží'],
              ['Větrný, suchý den', 'tričko, softshell', 'dobrý kompromis při aktivním pohybu'],
              ['Mráz', 'termoprádlo, fleece, zateplená bunda', 'čepice a rukavice nezapomínejte'],
              ['Lyžování', 'funkční triko, fleece, lyžařská bunda a kalhoty', 'sněhová zástěra proti sněhu']]) +
          '<p>Základ v podobě funkčního prádla najdete v kategorii <a href="/termopradlo-panske/">pánské termoprádlo</a> a <a href="/termopradlo-damske/">dámské termoprádlo</a>. Bavlněné tričko se hodí jen na krátké a suché výlety, v dešti nasákne a ochlazuje.</p>'
          '<h2>Nepromokavá bunda, softshell, nebo zateplená bunda?</h2>'
          '<p>Nepromokavá bunda chrání proti vytrvalému dešti, ale méně prodýchá, takže při namáhavé chůzi se v ní zahřejete. Softshell je pružný, prodyšný a odolá větru i lehké přeháňce, ale při silném dešti propustí vlhkost. Zateplená bunda je pro nehybný pobyt, procházky ve městě nebo pozdní podzim. Pokud chcete jednu univerzální volbu, pořiďte lehkou nepromokavou bundu a pod ni kombinujte fleecovou mikinu podle teploty.</p>'
          '<ul><li><strong>Skládací bundy (packaway):</strong> v popisu se objevují bundy do kapsy, hodí se do batohu pro případ změny počasí.</li>'
          '<li><strong>Kapuce:</strong> zkuste ji nasadit s čepicí; měla by jít stáhnout a nezakrývat výhled.</li>'
          '<li><strong>Zip a kapsy:</strong> zip s chlopní brání průniku vody, kapsy musí být dostupné i s batohem.</li>'
          '<li><strong>Délka:</strong> delší bunda pokryje bedra a při sezení na kameni zahřeje.</li>'
          '<li><strong>Větrání:</strong> zipy v podpaží ochladí tělo bez svlékání bundy.</li></ul>'
          '<p>Při čtení popisu rozlišujte nepromokavost a vodoodpudivost. První znamená, že se bunda dá použít v dešti, druhá jen potlačuje vsakování vody při krátké přeháňce. Konkrétní hodnoty vždy hledejte v popisu obchodu a nepřebírejte je z názvu.</p>'
          '<h2>Fleecové mikiny jako střední vrstva</h2>'
          '<p>Fleece je lehký, hřejivý a rychle schne. Hodí se pod bundu na výlet, na tábor, k ohni i do města. U <a href="/fleecove-mikiny/">fleecových mikin</a> sledujte zip: celý zip dovoluje větrání, krátký drží krk teplejší. Tenký fleece je vhodný jako střední vrstva, tlustý jako samostatná bunda v jarních dnech. Nezapomeňte, že fleece nechrání před větrem, proto potřebujete vrchní vrstvu. Pro běžné nošení doplňují nabídku také <a href="/mikiny/">mikiny</a> z klasického materiálu.</p>'
          '<h2>Trekové a zimní boty</h2>'
          '<p>V nabídce jsou turistické boty pro muže, ženy i děti. Pro chůzi po stezkách se hodí kotníková bota, která drží kloub při sestupu, pro nenáročné procházky nízká. Dobrá bota má podešev s vzorkem, který nesklouzne po kamení, a špičku, která chrání prsty. Zimní boty a sněhule jsou naopak zateplené a vysoké, často s lemem, který nepustí sníh dovnitř. Při výběru dbejte na to, že přidaná ponožka zvětší objem chodidla, proto bota nesmí být příliš těsná. Podrobnosti najdete v kategoriích <a href="/trekova-obuv/">trekové boty</a> a <a href="/zimni-obuv/">zimní boty a sněhule</a>.</p>'
          '<h2>Děti v přírodě</h2>'
          '<p>Dětská outdoorová výbava je v nabídce výrazná. Děti se hodně pohybují, rychle se zahřejí i prochladnou, a proto potřebují oblečení, které se dá snadno svléci a obléknout. Bundy do kapsy, nepromokavé kombinézy a fleecové vrstvy jsou praktické, protože se dají rychle vyměnit. Sledujte zip, který zvládnou i s rukavicemi, a reflexní prvky pro podzimní soumrak. Dětské boty vybírejte s malou rezervou, ne příliš velké, a zkoušejte je se silnější ponožkou.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Střihy jsou obecně rovné až mírně volnější, aby se pod bundu vešla vrstva. Pokud mezi velikostmi váháte, vezměte větší pro zimní zateplené modely a menší pro letní tenké. Dámské střihy bývají užší v pase a kratší v rukávech. Kupujete-li bundu na dálku, ověřte tabulku obchodu a porovnejte ji s vlastním oblečením, které sedí.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li><strong>Praní:</strong> podle štítku, s jemným prostředkem, bez aviváže u funkčních materiálů.</li>'
          '<li><strong>Impregnace:</strong> po opakovaném praní obnovte vodoodpudivost sprejem nebo prací přísadou.</li>'
          '<li><strong>Fleece:</strong> neprat horkou vodou a nežehlit, vlákna se tvarují.</li>'
          '<li><strong>Boty:</strong> očistit od bláta, vysušit při pokojové teplotě, nikoli na topení.</li>'
          '<li><strong>Skladování:</strong> bundy zavěsit, péřové zateplené nenechávat dlouho stlačené.</li></ul>'
          '<h2>Do hor, na výlet i do města</h2>'
          '<p>Oblečení Trespass se dobře nosí i mimo stezky. Fleecová mikina a lehká bunda do kapsy fungují při cestách vlakem, na chatě i při venčení psa. Pokud kupujete na víkend na horách, sbalte vždy střední a vrchní vrstvu, protože počasí se za den změní. V autě nechávejte náhradní ponožky a čepici, na které se snadno zapomíná. U trekových bot počítejte s rozchozením: první výlet nedělejte na dlouhou trasu, ale na krátkou, aby bota přilnula k noze.</p>'
          '<h2>Dámské, pánské a dětské střihy</h2>'
          '<p>Rovnoměrný poměr pánských a dámských modelů znamená, že ženy nemusí nosit pánské bundy. Dámské střihy jsou užší v pase a ramenou, někdy kratší v délce. Pánské jsou širší a delší, což pomáhá vyšším postavám. Děti vybírejte podle výšky, ne podle věku uvedeného na štítku, protože věk bývá jen orientační. Rodiny ocení, že barvy dětských a dospělých bund se dají sladit, což zrychlí hledání skupiny na stezce.</p>'
          '<h2>Co si zkontrolovat před koupí</h2>'
          '<ul><li><strong>Popis materiálu:</strong> polyester, nylon a fleece mají různé vlastnosti, hledejte údaj o vodoodpudivosti.</li>'
          '<li><strong>Velikostní tabulka:</strong> porovnejte obvod hrudníku s oblečením, které sedí.</li>'
          '<li><strong>Kapuce a límec:</strong> vyzkoušejte je s čepicí a šálou.</li>'
          '<li><strong>Zipy a švy:</strong> spolehlivé zipy a zesílené švy prodlužují životnost.</li>'
          '<li><strong>Vrácení zboží:</strong> ověřte podmínky obchodu pro případ špatné velikosti.</li></ul>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Zimní bundy a boty se zlevňují po vánocích a na jaře, jarní a lehké modely na konci léta. Nepromokavé kousky mají slevy celoročně, protože je lidé kupují před výletem. Chcete-li ušetřit, sledujte porovnání obchodů na kartě produktu a pokud možno si vyberte starší kolekci, která se funkčně téměř neliší.</p>'
          '<h2>Jak se Trespass liší od jiných značek</h2>'
          '<p>Trespass vyniká šíří nabídky pro celou rodinu a pestrostí barev. Podobně široce zaměřené jsou '
          + B(('regatta', 'Regatta'), ('alpine-pro', 'Alpine Pro'), ('hannah', 'Hannah'), ('kilpi', 'Kilpi')) +
          ', o něco technicky zaměřenější bývají '
          + B(('the-north-face', 'The North Face'), ('jack-wolfskin', 'Jack Wolfskin'), ('columbia', 'Columbia')) +
          '. Ke srovnání poslouží kategorie značky a filtr pro koho, takže stejný druh bundy porovnáte přímo.</p>',
    faq=[
        ('Co od Trespass na Sporteka nejčastěji najdu?', 'Převažují jarní a podzimní bundy, nepromokavé bundy, fleecové mikiny, zimní bundy a trekové boty. Doplňují je kalhoty, kraťasy, tílka a zimní boty.'),
        ('Je Trespass jen pro dospělé?', 'Ne. Pánský a dámský sortiment je téměř vyrovnaný a významnou část tvoří dětské kousky, zejména bundy, kombinézy a boty.'),
        ('Čím se liší softshell od nepromokavé bundy?', 'Softshell je pružný, prodyšný a odolný vůči větru, ale při silném dešti vlhne. Nepromokavá bunda se používá v dešti, avšak hůř prodýchá.'),
        ('Jak složit vrstvy na výlet?', 'Spodní vrstva odvádí pot, střední fleece drží teplo a vrchní bunda chrání před větrem a deštěm. Při chůzi do kopce vrstvu sundejte dřív, než se zapotíte.'),
        ('Je fleecová mikina dost teplá do mrazu?', 'Samotná ne. Je skvělou střední vrstvou, ale v mrazu potřebuje zateplenou nebo větruodolnou bundu a pod ní termoprádlo.'),
        ('Jakou velikost bundy vybrat?', 'Pro zateplené modely vezměte volnější velikost, aby se vešla vrstva. U lehkých bund na tričko stačí přiléhavější. Spoléhejte na tabulku obchodu.'),
        ('Jak vybrat dětské boty na výlet?', 'S malou rezervou, nikoli o číslo větší. Zkoušejte s ponožkou, kterou dítě nosí na výletě, a zkontrolujte, zda podešev drží na mokrém povrchu.'),
        ('Jak obnovit vodoodpudivost bundy?', 'Bundu vyperte jemným prostředkem a použijte impregnační sprej nebo přísadu do pračky. Hodí se po několika sezonách nebo po zhoršení vsakování.'),
        ('Kdy kupovat zimní bundu a boty?', 'Nejvýhodněji po vánocích a na jaře. Kdo potřebuje konkrétní velikost nebo barvu, má lepší výběr na podzim.'),
    ],
)

# ------------------------------------------------------------------ fila
NEW['fila'] = dict(
    title='Fila: tenisky, mikiny, trička a inline brusle',
    desc='Fila v katalogu Sporteky: tenisky a volnočasové boty, mikiny, trička, tepláky, ponožky a kolečkové brusle. Jak vybrat velikost, styl a kdy hledat slevy.',
    intro='<p>Fila je v katalogu Sporteky především značka tenisek a volnočasového oblečení. Zdaleka největší skupinu tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, za nimi následují <a href="/mikiny/">mikiny</a>, <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/sportovni-ponozky/">ponožky</a>, <a href="/teplaky/">tepláky</a> a kupodivu také <a href="/inline-brusle/">inline brusle</a>. K tomu přibývají kraťasy, kalhoty, polokošile a lehké bundy. Nabídka cílí hlavně na ženy a muže ve stejném poměru, dětské kousky jsou menší část. Barvou dominuje černá a bílá, což odpovídá klasickým kouskům do města. Stránka pomáhá vybrat správné tenisky, správně zvolit velikost, rozlišit brusle pro děti a dospělé a vědět, kdy sledovat slevy. Neslibuje nic nad rámec toho, co obchody v katalogu nabízejí.</p>',
    guide='<h2>Co Fila v nabídce zastupuje</h2>'
          '<p>Fila je zde hlavně streetová a volnočasová značka. Většinu sortimentu tvoří obuv, podstatně menší část oblečení. Sportovní sekce není hlavní, ale najdete v ní kolečkové brusle, zimní brusle nebo funkční doplňky. Tabulka ukazuje, jak sortiment využít v praxi.</p>'
          + T(['Kategorie', 'K čemu se hodí', 'Na co se zaměřit'], [
              ['<a href="/tenisky/">Tenisky</a>', 'město, škola, cestování', 'podešev, materiál svršku, šířka, styl'],
              ['<a href="/mikiny/">Mikiny</a>', 'každodenní nošení, vrstva', 'kapuce, zip, střih, materiál'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'léto, trénink, město', 'střih, tkanina, potisk'],
              ['<a href="/teplaky/">Tepláky</a>', 'doma, cesta, trénink', 'manžety, pas, zateplení'],
              ['<a href="/sportovni-ponozky/">Ponožky</a>', 'každodenní obuv, sport', 'výška, polstrování, balení více kusů'],
              ['<a href="/inline-brusle/">Inline brusle</a>', 'rekreace a fitness', 'velikost, ložiska, zapínání, brzda'],
              ['<a href="/polokosile/">Polokošile</a>', 'volný styl, práce', 'límec, střih, materiál']]) +
          '<p>Ženských a mužských kousků je přibližně stejně, dětské modely tvoří menší, ale samostatnou část. Unisexových je málo, proto se u obuvi vyplatí zkontrolovat, jestli jde o dámský, nebo pánský střih. Bílé tenisky se hodí k čemukoli a patří k nejuniverzálnějším, černé skrývají špínu, béžové a růžové nabízejí jemnější tón.</p>'
          '<h2>Jak vybrat tenisky</h2>'
          '<p>Většina párů v nabídce je volnočasová. Mají měkčí podešev, pohodlný vnitřek a střih navržený k celodennímu nošení v městském prostředí. Jako běžecké boty se nehodí, protože jim chybí odpružení pro dlouhé vzdálenosti. Výběr proto začněte otázkou, kdy je budete nosit. Do školy a kanceláře dobře poslouží čisté, jednobarevné tenisky, na cesty pohodlné modely s měkkou stélkou, a pokud chcete vyniknout, hledejte výraznější podešev nebo tzv. chunky střih. Další pomoc najdete v průvodci kategorie <a href="/tenisky/">tenisky</a> a <a href="/damska-sportovni-obuv/">dámská sportovní obuv</a>.</p>'
          + T(['Typ podešve', 'Charakter', 'Pro koho'], [
              ['Plochá, tenká', 'klasický retro vzhled', 'město, kombinace s džíny'],
              ['Silnější, platformová', 'výraznější silueta, vyšší vzhled', 'módní kombinace, dámské šaty'],
              ['Odpružená, lehká', 'měkčí došlap', 'celodenní chůze, cestování'],
              ['Vysoká kotníková', 'kotník je podepřený', 'chladnější dny, styl streetwear']]) +
          '<p>U materiálu rozhoduje použití. Kůže a syntetika snesou deštivé počasí a lépe se čistí, textil dýchá a je lehčí, ale rychleji se zašpiní. Bílé tenisky nedoporučujeme do blátivého prostředí; po sezoně je nechte vyčistit, aby bílá nezežloutla. Při chůzi po mokré dlažbě sledujte vzorek podešve, hladká může klouzat.</p>'
          '<h2>Velikosti a střihy tenisek</h2>'
          '<p>Obuv jednotlivých značek vychází z vlastních kopyt, proto je jisté pouze měření chodidla. Změřte délku odpoledne a přidejte rezervu pro prsty, obvykle několik milimetrů. Pokud je noha široká nebo vyšší v nártu, hledejte model s měkčím svrškem a vyšším šněrováním. V nabídce jsou ženské i mužské modely; chcete-li pánský střih pro ženu, zkuste jej s menší velikostí podle tabulky obchodu a ověřte převodník. U dětí kupujte s malou rezervou, dítě by nemělo klopýtat o špičku.</p>'
          '<ul><li><strong>Změřte obě chodidla:</strong> nohy se obvykle liší, řiďte se větší.</li>'
          '<li><strong>Zkoušejte s běžnou ponožkou:</strong> tenká letní a tlustá zimní mění objem.</li>'
          '<li><strong>Zapněte do poloviny:</strong> pata nesmí vyklouznout při kroku.</li>'
          '<li><strong>Projděte se:</strong> bota nemá tlačit na boky ani na malíček.</li></ul>'
          '<h2>Mikiny, tepláky a trička</h2>'
          '<p>Oblečení Fila patří spíš ke každodennímu stylu než k tréninku. <a href="/mikiny/">Mikiny</a> mají často výrazný nápis nebo logo, což je hlavní design. Kapuce zahřeje na procházku, střih bez kapuce se hodí do kanceláře nebo pod bundu. U <a href="/teplaky/">tepláků</a> sledujte manžety: pevnější se lépe nosí s teniskami, volnější jsou pohodlnější doma. Trička a tílka jsou lehčí, bavlna je příjemná, ale u náročného tréninku nedokáže odvádět pot jako syntetika. Pokud plánujete cvičit, hledejte materiál označený jako funkční nebo prodyšný.</p>'
          '<p>Pro kombinace ve stylu sportovní elegance poslouží polokošile, kterou nosíte do práce i k džínám. Černé tepláky a bílá mikina jsou klasický pár, pro odvážnější barvy vyberte béžovou nebo modrou. Sety kusů stejné řady sladí barvu i potisk, což ušetří čas při skládání outfitu.</p>'
          '<h2>Inline brusle pro děti i dospělé</h2>'
          '<p>Kolečkové brusle jsou překvapivě důležitou částí nabídky. Nacházejí se zde modely pro dospělé i dětské s nastavitelnou velikostí, která se mění s rostoucí nohou. Pro začátečníky jsou vhodné brusle s pevným tvarem boty, pohodlným zapínáním a brzdou na patě. Rekreační jezdec ocení modely s většími koly, které se lépe kutálejí po nerovném povrchu. Dětem pořiďte přilbu, chrániče loktů, kolen a zápěstí; brusle bez chráničů nepoužívejte. Další informace najdete v kategorii <a href="/inline-brusle/">inline brusle</a> a ve výběru <a href="/detske-inline-brusle/">dětské inline brusle</a>.</p>'
          + T(['Hledisko', 'Dětské brusle', 'Dospělé brusle'], [
              ['Velikost', 'nastavitelná, roste s nohou', 'pevná, přesná velikost'],
              ['Zapínání', 'přezky a pásek, někdy tkaničky', 'kombinace přezek a tkaniček'],
              ['Kola', 'menší, lehčí', 'větší, plynulejší jízda'],
              ['Chrániče', 'nutné, i s přilbou', 'doporučené vždy']]) +
          '<p>Zimní brusle na led jsou v nabídce také, ale v menším rozsahu. Pokud hledáte právě je, projděte kategorii <a href="/brusle/">zimní brusle</a>, kde se nabízejí různé značky. Fila u nich funguje spíš jako doplněk rekreační nabídky.</p>'
          '<h2>Ponožky a drobnosti</h2>'
          '<p>Ponožky k teniskám jsou často opomíjeným prvkem. Nízké kotníkové se hodí k nízké obuvi, delší sportovní k teplákům a k bruslím. Kupujte vícekusová balení, která vyjdou výhodněji a usnadní střídání. Pro brusle vyberte tenčí, ale pevnou ponožku bez švů, jinak vznikají puchýře. Další drobností je dětská helma pro jízdu na bruslích či kolečkové brusle, která je v nabídce rovněž dostupná.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li><strong>Tenisky:</strong> neperte v pračce, očistěte vlhkým hadříkem a vysušte při pokojové teplotě.</li>'
          '<li><strong>Bílé boty:</strong> čistěte hned po zašpinění, aby se skvrna nezakousla.</li>'
          '<li><strong>Mikiny a tepláky:</strong> perte naruby při nižší teplotě, aby potisk vydržel.</li>'
          '<li><strong>Brusle:</strong> po jízdě je otřete, zkontrolujte ložiska a utáhněte šrouby.</li>'
          '<li><strong>Střídání:</strong> dva páry bot se střídají, takže mají čas vyschnout.</li></ul>'
          '<h2>Jak se Fila liší od jiných značek</h2>'
          '<p>Fila patří k volnočasovým značkám a tato role se odráží v sortimentu: tenisky a mikiny převažují nad tréninkovým vybavením. Podobně zaměřené jsou '
          + B(('puma', 'Puma'), ('reebok', 'Reebok'), ('kappa', 'Kappa'), ('champion', 'Champion')) +
          ', tréninkově zaměřenější bývají '
          + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('under-armour', 'Under Armour')) +
          '. Pro výběr tenisek tedy jde především o vzhled, pohodlí a použití, nikoli o sportovní výkon.</p>'
          '<h2>Jak tenisky kombinovat</h2>'
          '<p>Bílé tenisky ladí s džíny, šaty i kalhotami s úzkou nohavicí a dobře drží celý rok. Černé se hodí do zimy a k tmavému oblečení. Chcete-li zvýraznit barvou, vyberte jeden výrazný prvek, třeba červenou podešev, a zbytek outfitu nechte klidný. K mikině s velkým nápisem se hodí jednoduché tenisky, k hladké mikině naopak obuv s výrazným designem. Platí také pravidlo, že tepláky nosíte nad kotníky, aby tenisky vynikly.</p>'
          '<h2>Pro koho je sortiment vhodný</h2>'
          '<p>Dámská nabídka je o něco větší než pánská, hlavně u tenisek a lehčího oblečení. Muži najdou mikiny, trička a tepláky v jednoduchém střihu. Pro studenty a mladé lidi jsou praktické kusy do školy a na volný čas, pro dospělé tenisky na celodenní chůzi. Děti dostanou brusle, tenisky a mikiny; u dětí se vyplatí kupovat po jednom páru, který zvládne sezónu, ne několik rezerv předem.</p>'
          '<h2>Kontrola kvality před vyzvednutím</h2>'
          '<p>Po doručení zkontrolujte švy, lepení podešve a zip, případně potisk. Tenisky zkoušejte doma na koberci, abyste je mohli případně vrátit nezašpiněné. Zkontrolujte, zda se hodí k oblečení, které chcete nosit, a porovnejte barvu s fotkou v obchodě, protože odstíny se na obrazovce liší. Krabici ani štítky neodstraňujte dřív, než si budete jisti velikostí. Při výměně obchod ocení nepoškozený obal a nenošený kus, což urychlí vyřízení vrácení nebo výměny za jinou velikost.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Tenisky se zlevňují na konci sezóny a při obměně modelů, mikiny a tepláky v zimě a na jaře. Bílé a černé klasiky mívají slevy několikrát ročně, takže je lze pohodlně hlídat. Použijte porovnání obchodů na kartě produktu, a pokud potřebujete konkrétní velikost, nečekejte na poslední výprodej, kdy se řada velikostí rozprodá.</p>',
    faq=[
        ('Co od Fila na Sporteka najdu?', 'Převážně tenisky a volnočasové boty, dále mikiny, trička, ponožky, tepláky, inline brusle, kraťasy, kalhoty a polokošile.'),
        ('Jsou tenisky Fila vhodné na běh?', 'Většina je volnočasová, s měkčí podešví pro celodenní chůzi. Na delší běh si vyberte běžeckou obuv s odpružením, kterou najdete v samostatné kategorii.'),
        ('Jak vybrat velikost tenisek?', 'Změřte chodidlo odpoledne a přidejte rezervu pro prsty. Zkoušejte s ponožkou, kterou běžně nosíte, a ověřte tabulku obchodu.'),
        ('Čím se liší dámské a pánské tenisky?', 'Dámské jsou užší v patě a lehčí, pánské širší. Unisexových je málo, proto vždy zkontrolujte popis a převodní tabulku.'),
        ('Jak vyčistit bílé tenisky?', 'Očistěte je vlhkým hadříkem s jemným prostředkem. Nedávejte je do pračky a sušte při pokojové teplotě, jinak se bílá změní na žlutou.'),
        ('Co je důležité u dětských inline bruslí?', 'Nastavitelná velikost, pevný tvar boty a spolehlivá brzda. Vždy k nim patří přilba a chrániče loktů, kolen a zápěstí.'),
        ('Kdy se vyplatí kupovat mikiny a tepláky?', 'Nejlepší výběr bývá na podzim, slevy přicházejí v zimě a na jaře. Klasické barvy se zlevňují častěji než sezónní.'),
        ('Hodí se tepláky i do města?', 'Ano, černé nebo šedé tepláky s pevnou manžetou se kombinují s mikinou i teniskami. Pro formálnější prostředí zvolte tmavé barvy a čistý střih.'),
        ('Jak se starat o potisk na mikinách?', 'Perte mikiny naruby při nižší teplotě a nesušte je v horké sušičce. Potisk pak déle drží barvu i tvar.'),
    ],
)
