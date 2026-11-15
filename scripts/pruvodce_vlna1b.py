"""sporteka.cz — seasonal guides, wave 1b (16. 11. 2026): winter running and cross-country skiing for beginners.
Facts stay general and true; no prices, no invented statistics, no medical promises."""
from texty_vlna1a import T

GUIDES = {}

GUIDES['zaciname-behat-v-zime'] = dict(
    name='Běh v zimě',
    h1='Začínáme běhat v zimě: boty, oblečení a bezpečnost',
    seo_title='Běh v zimě: boty, oblečení a bezpečnost pro začátečníky',
    seo_desc='Jak začít běhat v zimě: běžecké a trailové boty, nesmeky na led, vrstvení, čelovka a první čtyři týdny. Praktický průvodce a porovnání cen v e-shopech.',
    intro_html=(
        '<p>V lednu se běžecké trasy kolem domů najednou zaplní. Část nových běžců ale po třech týdnech skončí, protože je zima, tma a venku klouže. '
        'Přitom zimní běh není nijak zvlášť náročný. Potřebujete pár správných věcí, rozumný plán a trochu trpělivosti, než si tělo zvykne.</p>'
        '<p>Průvodce je určený těm, kdo s během teprve začínají nebo se vracejí po delší pauze. Projdeme boty, vrstvení, protiskluzové nesmeky, čelovku i první čtyři týdny tréninku. '
        'U každé části najdete odkaz do kategorie, kde na Sportece vidíte nabídky českých e-shopů vedle sebe. Sporteka sama nic neprodává, jen srovnává nabídky obchodů; nakupujete přímo v tom, který vám nabídne nejlepší podmínky.</p>'
        '<p>Kdo se léčí s chronickým onemocněním nebo má potíže se srdcem či klouby, ať se před začátkem poradí s lékařem. Zbytek textu je obecná praxe, ne zdravotní doporučení.</p>'),
    sections=[
        dict(h2='Jak začít: nejdřív boty a plán, ne vybavení za tisíce',
             html=(
                 '<p>Začátečník v zimě potřebuje méně, než si myslí. Zimní bunda s membránou je obvykle zbytečná, protože při běhu se zahřejete rychle a pod nepromokavou vrstvou byste se uvařili. '
                 'Co naopak stojí za to řešit hned: boty s dobrým záběrem, vrstvy, které odvádějí pot, a něco na hlavu a ruce.</p>'
                 '<p>Druhá věc je plán. Běhat třikrát týdně po půl hodině je lepší než jeden dlouhý výběh v neděli, po kterém dva dny chodíte jako o berlích. Zima navíc pomalému tempu přeje. Pokud při běhu zvládnete říct celou větu, běžíte dobře.</p>'
                 '<p>Nákup rozdělte na tři kroky: boty, základní oblečení (vrstvy, čepice, rukavice) a bezpečnost (čelovka, reflexní prvky, případně nesmeky). Zbytek můžete dokoupit později, až zjistíte, co vám opravdu chybí.</p>')),
        dict(h2='Běžecké boty do zimy: silniční, nebo trailové?',
             html=(
                 '<p>Na odklizených chodnících a asfaltu vám bohatě stačí běžná <a href="/silnicni-bezecke-boty/">silniční běžecká obuv</a>. Má měkčí odpružení a lehkou podrážku, jen na sněhu a ledu klouže víc než bota s hrubým vzorkem. '
                 'V mrazu navíc pěna mezipodešve ztuhne a bota působí tvrději. To je normální a po rozběhání se to srovná.</p>'
                 '<p>Jakmile běháte po pěšinách, loukách nebo lesních cestách, kde leží sníh a bláto, sáhněte po <a href="/trailove-boty/">trailových botách</a>. Jejich podrážka má výrazné výstupky, takže se lépe zakousne do rozbředlého sněhu a bahna. '
                 'Pevnější špička chrání prsty před kořeny a kameny schovanými pod sněhem. Trailovky se dají nosit i na silnici, jen se na asfaltu rychleji sjíždějí.</p>'
                 '<h3>Na co se při výběru dívat</h3>'
                 '<ul><li><strong>Velikost:</strong> nechte před špičkou rezervu zhruba půl až celé číslo. V zimě si často obujete silnější ponožku, takže zkoušejte v té, ve které budete běhat.</li>'
                 '<li><strong>Svršek:</strong> vzdušnou síťovinou v mrazu profukuje. Husté pleteniny nebo modely s membránou lépe hřejí a nepropouštějí vodu, hůř ale odvádějí vlhkost.</li>'
                 '<li><strong>Podrážka:</strong> čím hlubší a řidší vzorek, tím lepší záběr na sněhu a v blátě. Na led nepomůže žádný, tam jsou potřeba nesmeky.</li>'
                 '<li><strong>Značka:</strong> na Sportece najdete mimo jiné <a href="/znacka/asics/">Asics</a>, <a href="/znacka/mizuno/">Mizuno</a>, <a href="/znacka/saucony/">Saucony</a>, <a href="/znacka/nike/">Nike</a> nebo <a href="/znacka/la-sportiva/">La Sportiva</a>. Každá má trochu jiný střih, proto si pročtěte velikostní tabulku konkrétního modelu.</li></ul>'
                 '<p>Pokud máte starší boty, které už nemají odpružení, zimní období není dobrá chvíle na jejich dochození. Na zledovatělém a nerovném povrchu navíc sešlapaná podrážka hůř drží.</p>'),
             cat='silnicni-bezecke-boty', n=4),
        dict(h2='Trailové boty na sníh a bláto',
             html=(
                 '<p>Když váháte, jestli se vám trailovky s hrubší podrážkou vyplatí, položte si jednoduchou otázku: kolikrát týdně poběžíte mimo asfalt? Pokud aspoň jednou, vyplatí se. Pokud skoro vůbec, vystačíte si se silničními botami a opatrným krokem.</p>'
                 '<p>Rozdíl poznáte hned na prvním rozmrzlém úseku. Silniční podrážka se v blátě ucpe a klouže, trailová se bláta zbaví a drží stopu. Při klesání po rozbředlém svahu je to rozdíl mezi jistým krokem a nepříjemným uklouznutím.</p>'),
             cat='trailove-boty', n=4),
        dict(h2='Nesmeky na led: malá věc, která chrání kotníky',
             html=(
                 '<p>Náledí je největším zimním nepřítelem běžce. Ani nejlepší bota ho nezvládne, a pokud na trase máte aspoň kousek zledovatělé cesty, stojí za to mít v batůžku nebo v kapse <a href="/nesmeky/">nesmeky</a>. '
                 'Jsou to pružné gumové návleky s kovovými hroty nebo řetízky, které se natáhnou přes podrážku boty. Nasadíte je za pár vteřin a po úseku s ledem zase stáhnete.</p>'
                 '<p>Pro běh vybírejte lehčí modely s krátkými hroty, často jde o takzvané trailové nesmeky. Mohutné horolezecké řetězy s dlouhými hroty jsou na běh těžké a na asfaltu nepříjemné. '
                 'Důležité je, aby seděly na vaši velikost boty. Příliš volné se posouvají, příliš těsné se hůř natahují a trhají. V nabídce Sporteky najdete běžné značky jako Yate, Viking, Salewa nebo Nortec.</p>'
                 '<p>Na suchém asfaltu a na kamenité cestě je raději sundejte. Hroty se na tvrdém povrchu rychle otupí a běh v nich je nepříjemný.</p>'),
             cat='nesmeky', n=4),
        dict(h2='Vrstvení: tři vrstvy a jedno pravidlo',
             html=(
                 '<p>Základní pravidlo běžců zní: na začátku vám má být mírně zima. Pokud se obléknete tak, abyste se cítili příjemně hned ve dveřích, po deseti minutách budete přehřátí a zpocení. A zpocené tělo v mrazu rychle vychládá.</p>'
                 '<h3>Tři vrstvy</h3>'
                 '<ol><li><strong>Spodní vrstva</strong> odvádí pot od kůže. Těsně přiléhající funkční prádlo z polyesteru nebo z merino vlny. Bavlna je v zimě špatná volba, nasákne a studí.</li>'
                 '<li><strong>Střední vrstva</strong> drží teplo. Tenká fleecová nebo pletená mikina, v silnějším mrazu o něco hřejivější. Když je kolem nuly, často ji můžete vynechat.</li>'
                 '<li><strong>Vnější vrstva</strong> chrání před větrem a mokrem. Lehká větrovka nebo tenká bunda, která se dá sundat a uvázat kolem pasu nebo schovat do kapsy.</li></ol>'
                 '<p>Orientačně: při teplotě kolem nuly obvykle stačí dvě vrstvy na trupu, při několika stupních pod nulou přidáte třetí. Nohy se zahřejí samy a zvládnou méně oblečení než trup. Každý to ale vnímá jinak, proto si poznamenávejte, v čem vám bylo dobře.</p>'
                 '<p>Základ tvoří <a href="/termopradlo/">termoprádlo</a>. Viking, Sensor, Craft nebo Klimatex patří mezi značky, které na Sportece snadno najdete v několika nabídkách. Craft má ve srovnávači i <a href="/znacka/craft/">vlastní stránku značky</a>. Hledejte označení pro aktivní sport, ne pro každodenní nošení v kanceláři.</p>'),
             cat='termopradlo', n=4),
        dict(h2='Legíny a kalhoty: těsné běží líp',
             html=(
                 '<p>Na nohy se v zimě nejčastěji nosí dlouhé <a href="/leginy/">sportovní legíny</a>. Přiléhají k tělu, nevlají ve větru a při chůzi do kopce nepřekážejí. Existují tenké pro mírný chlad i zateplené s jemným chlupem uvnitř pro mráz.</p>'
                 '<p>Když je ráno kolem nuly a odpoledne pár stupňů nad ní, bohatě stačí tenké legíny. Při výraznějším mrazu zvažte zateplený model nebo přidejte vrstvu pod ně. Všímejte si zadní kapsy a reflexních prvků na lýtkách – hodí se při večerních výbězích. '
                 'Šev by neměl škrtit v rozkroku, jinak se po čtyřech kilometrech odřete. Vyzkoušejte je proto doma v dřepu a při zvedání kolene.</p>'
                 '<p>Některé legíny mají kapsu na klíče nebo telefon. Telefon v zimě drží baterii hůř, nosit ho při těle je lepší než v zadní kapse běžecké bundy.</p>'),
             cat='leginy', n=4),
        dict(h2='Čepice, čelenky a rukavice',
             html=(
                 '<p>Hlava a ruce jsou místa, kde pocítíte zimu jako první. U <a href="/cepice-a-celenky/">čepic a čelenek</a> se vyplatí tenká a prodyšná varianta. Silná zimní čepice bývá na běh příliš teplá. Při dobrém tempu z hlavy odchází hodně tepla a pod těžkou čepicí se zpotíte.</p>'
                 '<p>Čelenka přes uši je dobrý kompromis, když je kolem nuly. Při vyšším mrazu volte tenkou čepici nebo multifunkční šátek, který lze stáhnout na krk i na nos. Případně zkombinujte oboje.</p>'
                 '<p>U rukou je to podobné. <a href="/sportovni-rukavice/">Rukavice</a> mají být tenké, pružné a dostatečně dlouhé na zápěstí. Silné lyžařské rukavice jsou na běh často zbytečně teplé. V silném mrazu pomůže kombinace: tenká rukavice a přes ni palčáky, které můžete za pochodu stáhnout a strčit do kapsy.</p>'
                 '<p>Při koupi vyzkoušejte, zda v rukavicích ovládnete telefon. Dotykové konečky prstů nefungují u všech modelů spolehlivě.</p>'),
             cat='cepice-a-celenky', n=4),
        dict(h2='Dýchání v mrazu a rozcvička uvnitř',
             html=(
                 '<p>Mrazivý vzduch štípe v krku a v plicích, hlavně při rychlejším tempu. Zdravému člověku obvykle nevadí, jen je nepříjemný. Pomůže tenký nákrčník nebo šátek přes ústa a nos, který vzduch trochu ohřeje. Dýchejte klidně nosem a pusou zároveň a tempo držte takové, abyste zvládli mluvit.</p>'
                 '<p>Rozcvičku udělejte uvnitř, ještě než vyjdete ven. Pět až deset minut stačí. Lehké kroužení kotníků, kolen a boků, výpady, dřepy a chůze po schodech zahřejí svaly dřív, než je zasáhne mráz. Pak vyrazte svižnou chůzí a do běhu přejděte až po pár stech metrech.</p>'
                 '<p>Po výběhu se nezdržujte ve zpocených věcech. Převlečte se do suchého hned, jak se vrátíte, a dejte si něco teplého k pití. Pokud potřebujete nápad na domácí cvičení pro dny, kdy se ven vyrazit nedá, podívejte se na <a href="/kardio-doma/">kardio doma</a> nebo na <a href="/domaci-posilovna/">domácí posilovnu</a>.</p>')),
        dict(h2='Tma ve čtyři odpoledne: čelovka a viditelnost',
             html=(
                 '<p>Od listopadu do února se stmívá brzy. Pokud běháte po práci, pravděpodobně poběžíte potmě. Na osvětlené ulici vám stačí vidět a být viděni, v parku nebo v lese potřebujete vlastní světlo. <a href="/celovky-a-svitilny/">Čelovka</a> nechává ruce volné a svítí tam, kam se díváte.</p>'
                 '<p>Pro běh po chodnících a cestách stačí lehká čelovka se středním výkonem. Do lesa vybírejte jasnější model se širším kuželem světla a rezervou v baterii. Baterie mráz nesnáší, takže si nabíjecí model dobijte těsně před výběhem a náhradní baterie nebo powerbanku držte v teple. '
                 'V nabídce Sporteky potkáte značky jako Petzl, Silva, Ledlenser nebo Nitecore.</p>'
                 '<h3>Viditelnost pro řidiče</h3>'
                 '<ul><li>Noste světlé nebo reflexní barvy. V černých legínách a tmavé mikině vás řidič ve tmě skoro nevidí.</li>'
                 '<li>Reflexní prvky se vyplatí hlavně na místech, která se hýbou, tedy na kotnících a zápěstích, a dále na zádech. Pohyb řidič rozpozná dřív než nehybný bod.</li>'
                 '<li>Blikající světélko vzadu na batohu nebo na pase zvýší bezpečnost, když běžíte po silnici bez chodníku.</li>'
                 '<li>Běhejte proti směru provozu a v zatáčkách se přesuňte tam, kde vás řidič uvidí dřív.</li>'
                 '<li>Pokud posloucháte hudbu přes sluchátka, nechte jedno ucho volné nebo přepněte na režim, který pouští okolní zvuk.</li></ul>'),
             cat='celovky-a-svitilny', n=4),
        dict(h2='První čtyři týdny pro úplného začátečníka',
             html=(
                 '<p>Nejčastější chybou je začít moc rychle a běhat moc dlouho. První čtyři týdny mají za cíl jediné: aby vás běhání bavilo a zvykli si na něj klouby i šlachy. Následující schéma je jen orientační, upravte ho podle toho, jak se cítíte.</p>'
                 + T(['Týden', 'Tréninky', 'Náplň jednoho tréninku'], [
                     ['1', '3× týdně', '5 min svižná chůze, pak 8× (1 min klusu, 2 min chůze), 5 min chůze'],
                     ['2', '3× týdně', '5 min chůze, pak 8× (2 min klusu, 2 min chůze), 5 min chůze'],
                     ['3', '3× týdně', '5 min chůze, pak 6× (3 min klusu, 2 min chůze), 5 min chůze'],
                     ['4', '3× týdně', '5 min chůze, pak 4× (5 min klusu, 2 min chůze), 5 min chůze']]) +
                 '<p>Mezi tréninky nechte aspoň jeden den volna. Na konci čtvrtého týdne byste měli zvládnout pět minut v kuse a další týdny můžete klusové úseky pomalu prodlužovat. '
                 'Tempo držte takové, při kterém ještě zvládnete mluvit. Bolí-li vás kolena, kotníky nebo holeně víc než jen únavou svalů, dejte si pauzu a zvolte jiný druh pohybu. '
                 'Při přetrvávajících potížích se poraďte s lékařem nebo fyzioterapeutem. Pokud chcete s tréninkem spojit i jídelníček, najdete tipy ve <a href="/vyziva-pro-zacatecniky/">výživě pro začátečníky</a>.</p>')),
        dict(h2='Kdy v zimě neběhat',
             html=(
                 '<p>Existují dny, kdy je lepší zůstat uvnitř. Bezpečnost je důležitější než nepřerušená série tréninků.</p>'
                 '<ul><li><strong>Náledí a ledovka.</strong> Pokud je celá trasa zledovatělá a nemáte nesmeky, počkejte. Zlomené zápěstí nebo kotník vás vyřadí na týdny.</li>'
                 '<li><strong>Silný smog.</strong> Při špatné kvalitě ovzduší, kterou hlásí Český hydrometeorologický ústav, přesuňte trénink dovnitř. Aktuální hodnoty najdete na jeho webu nebo v aplikaci.</li>'
                 '<li><strong>Extrémní mráz a vítr.</strong> Při velmi nízkých teplotách a silném větru hrozí omrzliny na nose, uších a prstech. V takové dny zvolte kratší trasu v blízkosti domova nebo cvičení uvnitř.</li>'
                 '<li><strong>Nemoc.</strong> Při horečce nebo bolesti v krku neběhejte a nemoc nejdřív doležte. Po nemoci se vracejte zvolna.</li>'
                 '<li><strong>Tma bez světla.</strong> Bez čelovky nebo na neosvětlených úsecích raději zvolte jinou trasu.</li></ul>'
                 '<p>Pokud v zimě chcete zkusit něco jiného než běh, podívejte se na <a href="/bezky-pro-zacatecniky/">běžky pro začátečníky</a> nebo na <a href="/zimni-radovanky-s-detmi/">zimní radovánky s dětmi</a>.</p>')),
    ],
    faq=[
        ('Je zdravé běhat v mrazu?',
         '<p>Pro zdravého člověka je běh v mrazu obvykle bez problémů, pokud je dobře oblečený a tempo drží rozumné. Dýchání studeného vzduchu může být nepříjemné, pomůže šátek přes ústa. Při srdečních, plicních nebo kloubních potížích se před začátkem poraďte s lékařem.</p>'),
        ('Jaké boty na běh v zimě?',
         '<p>Na odklizené cesty stačí běžná <a href="/silnicni-bezecke-boty/">silniční běžecká obuv</a>. Na sníh, bláto a lesní cesty se hodí <a href="/trailove-boty/">trailové boty</a> s hrubším vzorkem. Na led pomohou <a href="/nesmeky/">nesmeky</a>.</p>'),
        ('Kolik vrstev na běh při nule?',
         '<p>Při teplotě kolem nuly obvykle stačí dvě vrstvy na trupu: funkční triko a lehká mikina nebo větrovka. Na začátku by vám měla být mírně zima, po deseti minutách se zahřejete.</p>'),
        ('Potřebuju na zimní běh čelovku?',
         '<p>Na osvětlených ulicích ne, stačí reflexní prvky. V parku, na pěšinách a v lese ano. <a href="/celovky-a-svitilny/">Čelovka</a> nechává ruce volné a ukazuje terén před vámi.</p>'),
        ('Jak často by měl začátečník běhat?',
         '<p>Třikrát týdně s volným dnem mezi tréninky je dobrý začátek. Střídejte klus s chůzí a délku úseků zvyšujte po týdnech. Důležitější než rychlost je pravidelnost.</p>'),
        ('Mám běhat i při sněhu?',
         '<p>Ano, sníh je zpravidla příjemnější než led. Zpomalte, zkraťte krok a zvolte boty se záběrem. Čerstvý nebo rozbředlý sníh je náročnější na svaly a kotníky, takže počítejte s pomalejším tempem.</p>'),
        ('Kde srovnám ceny zimního běžeckého vybavení?',
         '<p>Na Sportece. Porovnáváme nabídky českých e-shopů a vy nakupujete přímo v obchodě, který vám vyhovuje.</p>'),
    ],
    cats=['beh', 'bezecka-obuv'],
    updated='2026-11-16')


GUIDES['bezky-pro-zacatecniky'] = dict(
    name='Běžky pro začátečníky',
    h1='Běžky pro začátečníky: klasika, nebo bruslení a co koupit',
    seo_title='Běžky pro začátečníky: klasika, bruslení a co koupit',
    seo_desc='Běžky pro začátečníky: klasika, nebo bruslení, výběr lyží, bot a vázání NNN, SNS a Prolink, hole, vosky a tipy na první výlet. Srovnání nabídek e-shopů.',
    intro_html=(
        '<p>Běžky jsou jedním z nejpřístupnějších zimních sportů. Nepotřebujete vlek ani permanentku, stačí upravená stopa a pár hodin času. Zapojí se při nich celé tělo a v zimní krajině, kam byste se pěšky jinak moc nevypravili, zažijete klid i pohyb.</p>'
        '<p>Začátky ale bývají trochu zmatené. V obchodech uvidíte lyže s různými povrchy, boty se zkratkami různých systémů a vázání, které se k botám nemusí hodit. '
        'Tento průvodce vám pomůže se zorientovat: rozdíl mezi klasikou a bruslením, jak vybrat délku lyží, které boty zapadnou do kterého vázání, a co si vzít na první výlet. '
        'Sporteka vedle sebe ukazuje nabídky českých e-shopů, sama nic neprodává a nakupujete přímo v obchodě.</p>'
        '<p>Pokud nemáte pohybové zkušenosti nebo se léčíte, před prvním výletem se poraďte s lékařem. Jinak stačí začít pomalu a první den se nepřetěžovat.</p>'),
    sections=[
        dict(h2='Klasika, nebo bruslení?',
             html=(
                 '<p>Na běžkách se používají dva základní styly. <strong>Klasika</strong> je klouzání v prolisovaných stopách s rovnoběžně vedenými lyžemi. <strong>Bruslení</strong> (volná technika) se jezdí na upravené široké ploše a lyžař se odráží z hrany lyže podobně jako bruslař na ledě. Vybavení se pro oba styly liší, proto se před nákupem nejdřív rozhodněte, kterým chcete jezdit.</p>'
                 + T(['', 'Klasika', 'Bruslení'], [
                     ['Terén', 'Stopy prolisované v upraveném sněhu, ale i neupravené cesty', 'Široká, tvrdě upravená plocha bez stopy'],
                     ['Technika', 'Střídavý krok, lyže vedle sebe', 'Odraz z hrany, lyže ve tvaru V'],
                     ['Lyže', 'Delší, s oblastí záběru (vosk, šupiny nebo pás)', 'Kratší, bez záběru, celá kluzná plocha'],
                     ['Hole', 'Kratší, zhruba do podpaží', 'Delší, zhruba k bradě nebo k ústům'],
                     ['Boty', 'Měkčí a nižší, volnější kotník', 'Vyšší, pevné a zpevněné kolem kotníku'],
                     ['Náročnost pro začátečníka', 'Snazší první kroky, navazuje na přirozenou chůzi', 'Potřebuje cit pro rovnováhu a více energie']]) +
                 '<p>Pro většinu začátečníků je lepší začít <strong>klasikou</strong>. Jezdí se snadněji, stopy jsou skoro vždy po ruce a vybavení promine víc chyb. Bruslení přidejte později, až budete mít jistotu na lyžích. '
                 'Existují i kombinované (combi) lyže, hole a boty, které s jistými kompromisy zvládnou obojí. Pro začátek jsou použitelné, ale pro konkrétní styl budou vždy o něco horší než specializované.</p>'
                 '<p>Pokud chcete jezdit hlavně pohodově po neupravených cestách, v lese nebo po loukách, existují také <em>turistické</em> běžky, širší a stabilnější. Dál se ale věnujeme klasice na upravených tratích.</p>')),
        dict(h2='Šupiny, mohérový pás, nebo vosk?',
             html=(
                 '<p>U klasických lyží je hlavní otázkou, čím lyže drží při odrazu. Část lyže zhruba pod chodidlem se jmenuje oblast záběru a podle jejího řešení se rozlišují tři hlavní typy.</p>'
                 '<ul><li><strong>Voskové lyže</strong> mají hladkou plochu a záběr vytvoří vosk, který se na střed lyže natře podle teploty a typu sněhu. Dávají nejlepší záběr a skluz, ale vyžadují trochu znalostí a práce.</li>'
                 '<li><strong>Šupinové lyže (bezvosk)</strong> mají do kluznice vyfrézované šupiny. Drží dobře bez mazání, jsou nejjednodušší, ale při určitých teplotách jsou méně příjemné a trochu hlučné.</li>'
                 '<li><strong>Lyže s mohérovým (nebo syntetickým) pásem</strong> mají v kluznici vložený pruh s chloupky, které zajišťují záběr. Technicky jde o bezvoskové lyže, které bývají tišší a kloužou lépe než šupiny.</li></ul>'
                 '<p>Pro začátečníka, který nechce řešit mazání, je nejpraktičtější šupinová nebo pásová lyže. Pro ty, kdo chtějí jezdit víc a lépe, se vosky brzy vyplatí. Čím dřív se naučíte základy mazání, tím víc si jízdu užijete.</p>')),
        dict(h2='Běžecké lyže: délka, tvrdost a výběr',
             html=(
                 '<p>Při koupi vás čekají dvě čísla: délka a tvrdost (nebo ohyb). U dospělého jsou obecná pravidla jednoduchá. Klasické lyže bývají o několik centimetrů delší než výška těla, lyže na bruslení o něco kratší. Přesné rozmezí ale určuje výrobce, proto se <strong>řiďte jeho tabulkou podle hmotnosti</strong> – o tom, jak se lyže prohne, rozhoduje hmotnost, ne výška.</p>'
                 '<p>Proč hmotnost? Klasická lyže musí být tak tvrdá, aby při klidném stání ležela na sněhu oběma konci a střed (oblast záběru) se nedotýkal, a při odrazu se prohnula a střed dosedl. Když je lyže moc tvrdá, nezabere. Když je moc měkká, drhne i při skluzu. Proto výrobci u každého modelu udávají doporučenou hmotnost uživatele.</p>'
                 '<p>Při výběru <a href="/bezecke-lyze/">běžeckých lyží</a> narazíte na značky jako Fischer, Madshus, <a href="/znacka/rossignol/">Rossignol</a>, Peltonen nebo Acra. Sety lyží s už namontovaným vázáním jsou pro začátečníka pohodlné. Pokud kupujete lyže a vázání zvlášť, počítejte s montáží v servisu, kde vám vázání namontují a seřídí.</p>'
                 '<p>Na první sezonu se vyplatí střední třída. Nejlevnější lyže bývají těžké a nemají kvalitní kluznici, vrcholové závodní modely jsou pro začátek zbytečně náročné a citlivé na mazání.</p>'),
             cat='bezecke-lyze', n=4),
        dict(h2='Kompatibilita bot a vázání: NNN, SNS, Prolink, Turnamic',
             html=(
                 '<p>Tady se při nákupu chybuje nejčastěji. Boty a vázání musí být ze stejného systému, jinak boty do vázání nezapadnou. Zkratky, se kterými se setkáte:</p>'
                 + T(['Systém', 'Co to je', 'Poznámka'], [
                     ['NNN', 'New Nordic Norm, systém firmy Rottefella', 'Dnes nejrozšířenější, dvě lišty na podrážce boty'],
                     ['Prolink', 'Systém Salomon', 'Boty a vázání Prolink jsou kompatibilní s NNN'],
                     ['Turnamic', 'Systém Fischer', 'Boty i vázání jsou kompatibilní s NNN'],
                     ['SNS', 'Starší standard Salomon', 'Jedna střední lišta, s NNN nejde kombinovat; v obchodech ubývá']]) +
                 '<p>Praktický závěr: pokud kupujete nové vybavení, vybírejte NNN, Prolink nebo Turnamic. Boty z jednoho z nich zapadnou do vázání kteréhokoli dalšího. SNS je starší systém. Pokud koupíte použité lyže s vázáním SNS, hledejte i boty SNS.</p>'
                 '<p>Vázání a boty se navíc dělí podle stylu na klasické, bruslařské a kombinované. I to při výběru zohledněte, protože bruslařské boty jsou vyšší a pevnější v kotníku a vázání se k nim vybírá podle stylu. Zeptejte se v obchodě, nebo si před objednáním přečtěte popis a porovnejte označení na botě a na vázání.</p>'),
             cat='bezecke-vazani', n=4),
        dict(h2='Běžecké boty: pohodlí je důležitější než značka',
             html=(
                 '<p><a href="/bezecke-boty/">Běžecké boty</a> jsou lehčí a měkčí než sjezdové. Na klasiku bývají nižší, aby šel kotník ohýbat. Boty na bruslení jsou vyšší a mají pevnější opěrku kolem kotníku. Kombinované modely jsou kompromis a pro první rok jsou rozumnou volbou.</p>'
                 '<p>Zkoušejte je v ponožkách, ve kterých budete jezdit, a to tenčích než na túru. Příliš silné ponožky zhorší prokrvení a nohy vám budou mrznout. Bota má sedět pevně v patě, prsty nesmí narážet do špičky. Po obutí se v nich projděte a ohněte špičku jako při odrazu.</p>'
                 '<p>Na Sportece najdete modely od <a href="/znacka/alpina/">Alpiny</a>, <a href="/znacka/salomon/">Salomonu</a>, <a href="/znacka/rossignol/">Rossignolu</a>, Fischeru nebo Madshusu. Velikosti se mezi značkami liší, proto si doma změřte chodidlo a porovnejte délku s tabulkou výrobce.</p>'),
             cat='bezecke-boty', n=4),
        dict(h2='Hole: délka podle stylu',
             html=(
                 '<p>Hole pro běžky jsou lehčí a delší než sjezdové. Pro klasiku se délka vybírá zhruba po podpaží, pro bruslení až k bradě nebo k ústům. Orientační pravidlo je jednoduché: klasické hole jsou o něco kratší, protože se jimi odráží blíž u těla, bruslařské delší, aby šlo do odrazu přenést váhu těla.</p>'
                 '<p>Při výběru se podívejte na úchop a poutko. Poutko má být pohodlné a pevné, ale nemá škrtit. Rukojeť z korku nebo z plastu je příjemná i v mrazu. <a href="/lyzarske-hole/">Lyžařské hole</a> s označením na běžky najdete od značek jako Leki, Komperdell, Swix, <a href="/znacka/rossignol/">Rossignol</a> nebo Salomon. Pozor: sjezdové hole mají jiné talířky a nehodí se do prolisovaných stop.</p>'
                 '<p>Hole z karbonu jsou lehčí a dražší, hliníkové pevnější a levnější. Pro začátek je hliník naprosto v pořádku.</p>'),
             cat='lyzarske-hole', n=4),
        dict(h2='Oblečení na běžky: méně, než čekáte',
             html=(
                 '<p>Na běžkách se zahřejete rychle. Základem je proto <a href="/termopradlo/">termoprádlo</a> na kůži, které odvádí pot, a lehká větruodolná vrstva. Silná zimní bunda je zbytečná, jen se v ní zpotíte.</p>'
                 '<p>Oblékejte se na cibuli. Zpočátku, hlavně při čekání na parkovišti, je zima, po deseti minutách jízdy teplo. V batohu se vyplatí mít lehkou mikinu nebo tenkou bundu, kterou si obléknete při zastávce nebo odpočinku. Na nohy stačí elastické běžecké kalhoty nebo lehčí softshell, ne džíny. Z doplňků myslete na tenké rukavice, čepici nebo čelenku a na brýle proti slunci a sněhu.</p>'
                 '<p>Podívejte se také na <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a> a <a href="/lyzarske-rukavice/">lyžařské rukavice</a>. Rukavice na běžky by měly být tenčí než sjezdové, aby se v nich ruce nepřehřívaly.</p>'),
             cat='termopradlo', n=4),
        dict(h2='Vosky: kdy a jaké',
             html=(
                 '<p>Vosky jsou dvojího druhu. <strong>Kluzný vosk</strong> se nanáší na kluznou část lyže, tedy na špičku a patu, a zrychluje skluz. <strong>Stoupací vosk</strong> (záběrový) se nanáší do oblasti pod nohou a zajišťuje záběr při odrazu. U bruslení se maže celá kluznice kluzným voskem.</p>'
                 '<p>Na začátek vám stačí jeden nebo dva stoupací vosky podle teploty a typu sněhu; teplotní rozmezí je uvedené na obalu. Čerstvý sníh a nízké teploty vyžadují jiný vosk než mokrý sníh kolem nuly. '
                 'Mazání není nic složitého, chce to ale praxi. Pokud lyže drhnou nebo naopak nedrží, bývá příčinou nejčastěji špatně zvolený vosk pro dané podmínky.</p>'
                 '<p>Značky jako Swix, Toko, Holmenkol nebo Vauhti nabízejí kompletní řady vosků. <a href="/lyzarske-vosky/">Lyžařské vosky</a> si kupujte podle teplotní tabulky na obalu a zeptejte se v obchodě, co se hodí v místech, kam jedete. '
                 'K mazání potřebujete ještě korek a škrabku, často jsou součástí startovacích sad.</p>'),
             cat='lyzarske-vosky', n=4),
        dict(h2='Kam vyrazit a jak najít upravené stopy',
             html=(
                 '<p>Pro začátek se držte upravených stop. Najdete je v horách i v nižších polohách, často u větších středisek a v oblastech, kde je tradice běžkování. Stopy upravují obce, střediska nebo spolky a jejich stav se mění s počasím.</p>'
                 '<p>Před výletem si ověřte aktuální stav tratí. Informace bývají na webech středisek a obcí, ve speciálních mapách a aplikacích o běžkařských trasách a někdy na webových kamerách. Údaje starší než den berte s rezervou. '
                 'Sněhová pokrývka se mění a po oblevě může být trasa zledovatělá. Do neznámého terénu a na hřebeny bez upravených stop nevyrážejte bez zkušeností a navigace.</p>'
                 '<p>Pro první pokusy je ideální krátký rovinatý okruh, třeba kolem pěti kilometrů. Dlouhá stoupání a prudká klesání nechte na později.</p>')),
        dict(h2='První výlet: praktické tipy',
             html=(
                 '<ol><li><strong>Vyberte krátký a plochý okruh.</strong> První den vám stačí čtyři až pět kilometrů. Únava přichází rychleji, než čekáte.</li>'
                 '<li><strong>Zkuste si výbavu doma.</strong> Boty do vázání zacvakněte a vyzkoušejte, jak se uvolňují. Hole nastavte na délku.</li>'
                 '<li><strong>Začněte bez stop.</strong> Na rovné ploše si zkuste kluzný krok, přenášení váhy a zastavení. Teprve potom vjeďte do stopy.</li>'
                 '<li><strong>Naučte se zastavit a spadnout.</strong> Pád do strany na bok je lepší než dozadu. Na klesání jeďte pomalu v mírném pluhu nebo si lyže sundejte.</li>'
                 '<li><strong>Vezměte si pití a svačinu.</strong> Termosku s teplým čajem ocení každý a po výletu se vám bude hodit něco k jídlu.</li>'
                 '<li><strong>Dávejte pozor na stopu.</strong> Pěší do klasické stopy nepatří a lyžař zase nepatří na pěší cestu. Rychlejším běžkařům včas uhněte.</li>'
                 '<li><strong>Řekněte, kam jedete.</strong> Před delším výletem někomu řekněte, kudy pojedete a kdy se vrátíte, a vezměte si nabitý telefon.</li></ol>'
                 '<p>A hlavně nespěchejte. První den si zvykáte na lyže, o tempo nejde. Další dny pak budete mít v nohou víc a lépe poznáte, jaké vybavení vám vyhovuje. '
                 'Pokud vyrážíte s dětmi, podívejte se na <a href="/zimni-radovanky-s-detmi/">zimní radovánky s dětmi</a>, a pokud chcete cvičit i mimo sníh, najdete nápady v <a href="/kardio-doma/">kardiu doma</a>.</p>')),
    ],
    faq=[
        ('Klasika, nebo bruslení pro začátečníka?',
         '<p>Většině začátečníků se lépe začíná klasikou. Jezdí se ve stopě, je to snazší na rovnováhu a vybavení promine víc chyb. Bruslení přidejte později, až budete mít jistotu.</p>'),
        ('Jak dlouhé běžky si mám koupit?',
         '<p>Obecně jsou klasické lyže o několik centimetrů delší než výška těla a bruslařské o něco kratší. Přesnou délku a tvrdost určuje hmotnost, proto se řiďte tabulkou výrobce podle hmotnosti.</p>'),
        ('Jaké boty se hodí k jakému vázání?',
         '<p>Boty a vázání musí být ze stejného systému. NNN, Prolink a Turnamic jsou vzájemně kompatibilní. SNS je starší standard a s NNN se nekombinuje.</p>'),
        ('Potřebuji vosk, nebo stačí šupiny?',
         '<p>Pro začátek stačí lyže se šupinami nebo s pásem, které nemusíte mazat. Vosk se vyplatí, jakmile budete jezdit častěji a budete chtít lepší záběr i skluz.</p>'),
        ('Jak dlouhé hole k běžkám?',
         '<p>Na klasiku zhruba po podpaží, na bruslení po bradu nebo ústa. Výrobci uvádějí délky v tabulkách podle výšky postavy.</p>'),
        ('Co si obléct na běžky?',
         '<p>Termoprádlo na kůži, lehkou větruodolnou vrstvu a tenké rukavice. Při pohybu se zahřejete rychle, proto noste vrstvy, které jde snadno sundat a uložit do batohu.</p>'),
        ('Kde nakoupit běžky a srovnat ceny?',
         '<p>Sporteka porovnává nabídky českých e-shopů u lyží, bot, vázání, holí i vosků. Nakupujete přímo v obchodě, který vám vyhovuje.</p>'),
    ],
    cats=['bezecke-lyzovani', 'zimni-sporty'],
    updated='2026-11-16')
