"""sporteka.cz — wave 15e (4. 11. 2026): long texts (>= 1650 words) for merino-ponozky, lyzarske-helmy, bojove-sporty, horolezectvi.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ merino-ponozky
NEW['merino-ponozky'] = dict(long=True,
    title='Merino ponožky: výběr podle sportu a nabídky | Sporteka',
    desc='Merino ponožky na túry, běh, kolo i lyže: gramáž, výška, střih a velikost. Průvodce výběrem a nabídky českých obchodů vedle sebe na jednom místě.',
    intro='<p><strong>Merino ponožky</strong> patří k věcem, které si lidé po první zimě nebo první vícedenní túře většinou nechtějí vyměnit za nic jiného. Vlna z ovcí merino je jemná, hřeje i trochu zvlhlá a pach se v ní drží méně než v čistě syntetických vláknech. Samotný materiál ale nestačí, rozhoduje také hustota pletení, zesílená místa, výška a podíl pružných vláken.</p>'
          '<p>Na Sportece porovnáte <strong>merino ponožky</strong> z českých obchodů a u každého páru uvidíte nabídky vedle sebe. Pokud hledáte širší výběr, pokračujte do kategorií <a href="/sportovni-ponozky/">sportovní ponožky</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/cyklisticke-ponozky/">cyklistické ponožky</a>. K vlněné výbavě se hodí také <a href="/merino-tricka/">merino trička</a> a <a href="/merino-pradlo/">merino spodní prádlo</a>.</p>',
    guide='<h2>Proč právě merino na nohy</h2>'
          '<p>Noha patří k nejvíc se potícím částem těla, a přitom je uzavřená v botě, kde se vlhkost špatně odvětrává. Vlněné vlákno dokáže pojmout pot, aniž by se na dotek zdálo mokré, a tím snižuje pocit chladu i riziko otlaků. Kadeřavá struktura vlákna navíc zadržuje vzduch, který izoluje. Díky tomu stejná ponožka zvládne chladné ráno i teplejší odpoledne, aniž by se muselo přezouvat.</p>'
          '<p>Čisté merino by se ale rychle prodíralo na patách a špičkách. Proto je téměř každá kvalitní ponožka směsí: vlna dává komfort, nylon nebo polyamid odolnost proti oděru a elastan drží tvar. Podíl jednotlivých složek najdete v popisu a dá se z něj vyčíst určení. Víc vlny znamená měkkost a teplo, víc syntetiky znamená delší životnost při intenzivním používání.</p>'
          '<h2>Gramáž a vrstvení: tenká, střední, silná</h2>'
          '<p>Při pohledu na nabídku narazíte na slova jako lehká, střední nebo expediční. Označení nejsou normovaná, takže si je vykládejte jako vodítko, ne jako přesné číslo. Praktický rozdíl poznáte po obutí: tenká ponožka pohlcuje málo místa, silná zaplní botu a vyžaduje o něco volnější střih.</p>'
          + T(['Typ ponožky', 'Hodí se na', 'Na co dát pozor'], [
              ['Tenká, lehká', 'běh, kolo, letní túry, městské boty', 'dobrá prodyšnost, ale slabší tlumení v těžkých botách'],
              ['Střední', 'celoroční turistika, pracovní boty, zimní procházky', 'univerzální volba pro většinu lidí'],
              ['Silná, froté uvnitř', 'zimní túry, skialpinismus, mrazivé dny', 'zkoušejte v botě, aby nebyla těsná'],
              ['Vysoká podkolenka', 'lyžování, vysoké boty, chladné počasí', 'švy nesmí tlačit na holeni']]) +
          '<h2>Výška ponožky podle boty</h2>'
          '<p>Výška se vybírá podle obuvi a podle toho, kde by mohla bota drhnout. Kotníková ponožka končí pod kotníkovou kostí a hodí se do nízkých bot. Čtvrťová sahá o několik centimetrů výš a chrání kotník před okrajem boty. Polovysoká a podkolenka patří do vysoké obuvi, kde jinak okraj boty tře o holeň.</p>'
          '<ul><li><strong>Neviditelné a nízké</strong> používejte v tenisce nebo městské obuvi, ale u dlouhé chůze mohou při pocení sjíždět pod patu.</li>'
          '<li><strong>Kotníkové a čtvrťové</strong> jsou nejuniverzálnější pro <a href="/nizke-trekove-boty/">nízké trekové boty</a>, <a href="/bezecka-obuv/">běžeckou obuv</a> a trailové boty.</li>'
          '<li><strong>Střední až vysoké</strong> se hodí do <a href="/vysoke-trekove-boty/">vysokých trekových bot</a> a do zimních bot.</li>'
          '<li><strong>Podkolenky</strong> jsou volba pro lyžařské boty, více v oddílu <a href="/lyzarske-ponozky/">lyžařské ponožky</a>.</li></ul>'
          '<h2>Konstrukce, na které záleží</h2>'
          '<p>Podívejte se na detaily, protože právě ony rozhodují o tom, jestli ponožka vydrží celý den. Plochý šev přes prsty zabrání otlaku, který nepříjemně vzniká na hrubém spoji. Zesílená pata a špička vydrží tření při chůzi do kopce. Zónové tlumení pod chodidlem pomáhá při dlouhém dni na tvrdém povrchu. Pružná manžeta drží ponožku na místě, ale neškrtí. Síťovaná část na nártu pomáhá odvětrat teplo při pohybu.</p>'
          '<p>Některé modely mají oddělený pravý a levý kus, jiné jsou symetrické. Rozdělené kusy lépe sedí, ale musíte je rozlišit při nasazení a při praní nesmíte rozdělit pár. Nejdůležitější vlastností však zůstává stejná u všech typů: ponožka má na noze ležet bez záhybů, protože právě záhyb vyrobí puchýř.</p>'
          '<h2>Merino ponožky podle sportu</h2>'
          '<h3>Turistika a trek</h3>'
          '<p>Na túru se hodí střední ponožka s tlumením v oblasti paty a chodidla. Při vícedenním přechodu se vyplatí mít dva páry, jeden na sobě a jeden sušit na batohu. Merino se po vyprání rozložené na vzduchu usuší za pár hodin. Boty a opěrná výbava mají své kategorie: <a href="/trekova-obuv/">trekové boty</a>, <a href="/trekove-hole/">trekové hole</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h3>Běh a trail</h3>'
          '<p>Běžec chce lehkou, přiléhavou ponožku bez objemných švů. U delších tratí se hodí zpevněná pata a odvětrávaný nárt. Pro běh ve vlhku zvažte menší podíl vlny a větší podíl rychleji schnoucího syntetického materiálu. Pro trailové závody a tréninky najdete obuv v <a href="/trailove-boty/">trailových botách</a>.</p>'
          '<h3>Cyklistika</h3>'
          '<p>Na kole chrání ponožka proti tlaku tretry a pomáhá s odvodem potu. Menší výška bývá běžná v létě, delší v chladném počasí, kdy ponožka vyplní prostor mezi nohou a návleky. Jak se k tomu vybavit, ukazuje <a href="/cyklisticka-obuv/">cyklistická obuv</a> a <a href="/cyklisticke-navleky/">cyklistické návleky</a>.</p>'
          '<h3>Zimní sporty</h3>'
          '<p>Lyžařské boty sedí těsně, proto vyberte tenčí ponožku s vyztuženou holení a bez silných švů. Silná ponožka v tuhé botě nehřeje, ale stlačuje cévy a nohy mrznou rychleji. Na běžky a sněžnice se hodí střední vrstva, protože bota je volnější. V kategorii <a href="/zimni-sporty/">zimní sporty</a> najdete i další výbavu.</p>'
          '<h3>Každodenní nošení a práce</h3>'
          '<p>Na dlouhou směnu ve stoje nebo v pracovní obuvi je merino skvělý kompromis. Nohy se nepotí tolik jako v bavlně a ponožka se mezi nošeními dobře vyvětrá, což mnoho lidí oceňuje při cestování. Pro pohodlí v práci ale kupujte hlavně střední gramáž s plochými švy.</p>'
          '<h2>Jak zvolit velikost</h2>'
          '<p>Většina výrobců dělí ponožky do rozmezí, například tři až pět čísel boty v jednom kuse. Pokud jste na hranici mezi dvěma velikostmi, vezměte menší pro tenčí použití a větší pro silnou ponožku. Příliš malá ponožka se napíná, tenčí se na patě a rychle se prodře. Příliš velká se vrásní a tře. Dětské merino volte spíš s krátkým růstovým rozmezím, aby vydrželo celou sezónu.</p>'
          '<h2>Péče, aby merino vydrželo</h2>'
          '<p>Ponožky perte obrácené naruby při teplotě nejvýše 30 až 40 °C, v jemném programu a s tekutým prostředkem bez aviváže. Aviváž pokrývá vlákno filmem a zhoršuje odvod vlhkosti. Vyhněte se bělidlům a sušičce, kde se vlna sráží. Po vyprání je rozložte nebo pověste za špičku, na topení je nesušte. Při prvních použitích merino občas chlupatí, tomu se nevyhnete a po několika vypráních pomine.</p>'
          '<p>Malou dírku zašijte hned, dokud se nezvětšila. Na patách kontrolujte ztenčení a po sezóně nejhorší páry vyřaďte nebo je nechte jen na doma. Střídání několika párů prodlužuje život každému z nich, protože vlna se po nošení potřebuje uvolnit a vyvětrat.</p>'
          '<h2>Pánské, dámské a dětské merino ponožky</h2>'
          '<p>Dámské modely mívají užší střih v patě a nártu, pánské jsou širší a delší. Unisex řady používají rozmezí velikostí a nosí se oběma. Dětské ponožky jsou měkčí, mají méně švů a často výraznější barvy. Pro děti na zimu se hodí vlněná ponožka, která není příliš těsná, aby se dítě neprochladilo, viz také <a href="/zimni-obuv/">zimní boty a sněhule</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete nabídky značek ' + B(('lasting', 'Lasting'), ('smartwool', 'Smartwool'), ('icebreaker', 'Icebreaker'), ('northman', 'Northman'), ('devold', 'Devold'), ('sensor', 'Sensor'), ('mund', 'Mund'), ('drassn', 'Drassn'), ('woox', 'Woox'), ('progress', 'Progress'), ('lundhags', 'Lundhags'), ('dynafit', 'Dynafit')) + '. Různé řady mají jiný střih, takže si u druhého páru všímejte velikostní tabulky konkrétní řady, a ne jen názvu značky.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Kupovat nejtlustší ponožku do každé boty bez zkoušení.</li>'
          '<li>Prát ponožky s aviváží nebo sušit na radiátoru.</li>'
          '<li>Nosit bavlněnou ponožku pod merino a čekat, že bude teplo.</li>'
          '<li>Mít jediný pár a nosit ho den za dnem bez vysušení.</li>'
          '<li>Zvolit nízkou ponožku do vysoké boty, kde okraj škrtí holeň.</li>'
          '<li>Ignorovat špatné sedění v botě a spoléhat na to, že vlna ho vyřeší.</li></ul>'
          '<h2>Na co dalšího nezapomenout</h2>'
          '<p>K ponožkám patří i další vrstvy. Vlněná výbava pokračuje v kategoriích <a href="/merino/">merino oblečení</a>, <a href="/merino-mikiny/">merino mikiny a svetry</a> a <a href="/merino-doplnky/">merino čepice, nákrčníky a rukavice</a>. Pro péči o nohu a boty pomůže i <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého páru se zobrazuje několik nabídek, takže uvidíte, který obchod má vaši velikost a barvu na skladě. Vyberte podle sportu, výšky a gramáže, pak podle značky a střihu. Sady po třech nebo pěti párech dávají smysl, pokud už víte, že vám daný model sedí.</p>',
    faq=[('Čím se merino ponožky liší od běžných bavlněných?', 'Merino odvádí vlhkost od kůže a hřeje, i když je trochu vlhké, kdežto bavlna nasákne a při pocení ochlazuje. Navíc se v ní pach drží méně. Bavlna je naopak levnější a pro krátké suché použití dostačuje.'),
         ('Hřejí merino ponožky i v létě?', 'Tenké letní varianty nepřehřívají, protože vlákno dokáže regulovat teplotu a odvádět pot. Na horké dny volte lehkou gramáž a prodyšnou síťku na nártu. Při velkém horku mohou být vhodnější syntetické ponožky.'),
         ('Jak často je třeba merino ponožky prát?', 'Ponožky perte častěji než triko, protože jsou nejvíc namáhané, ale merino stačí po nošení vyvětrat. Po sportu je perte po jednom použití, na procházku nebo kancelář stačí merino po použití vyvětrat a vyprat po jednom až dvou dnech. Řiďte se pocitem a stavem látky.'),
         ('Musí být ponožka ze 100 % merina?', 'Ne, a často je to dokonce nevýhoda. Čistá vlna se rychle prodírá a ztrácí tvar. Obvykle se přidává polyamid pro odolnost a elastan pro pružnost, takže ponožka drží na noze a vydrží víc sezón.'),
         ('Proč mě merino ponožky svědí?', 'Některým lidem vadí hrubší vlákno. Hledejte označení jemné merino a zkuste tenčí řadu. Pokud svědění přetrvává i u jemných modelů, zvolte směs s větším podílem syntetiky nebo se poraďte s lékařem.'),
         ('Jakou výšku vybrat do trekových bot?', 'Do nízkých bot stačí kotníková nebo čtvrťová, do vysokých polovysoká až podkolenka. Okraj boty by nikdy neměl dosahovat na holou kůži, protože by při chůzi drhl.'),
         ('Kolik párů vzít na vícedenní túru?', 'Většinou dva až tři páry. Jeden máte na sobě, jeden se suší a třetí slouží jako rezerva na spaní nebo mokré počasí. Lehké merino váží málo, takže rezerva batoh nezatíží.'),
         ('Dají se merino ponožky sušit v sušičce?', 'Raději ne. Teplo a mechanické pohyby způsobují srážení a plstnatění. Bezpečnější je rozložit ponožky na stojan nebo je zavěsit na vzduchu mimo přímý zdroj tepla.'),
         ('Proč se mi ponožky na patě tenčí?', 'Pata je při chůzi nejvíc namáhaná a je z velké části vystavená tření o botu. Pomáhá správná velikost boty, zesílená pata a občasné střídání párů. Díra vzniká i při příliš těsné či volné botě.'),
         ('Jaké ponožky pro děti na zimu?', 'Měkké, bez silných švů a střední tloušťky. Dítě nesmí mít botu naplněnou do posledního místa, jinak mu ruce a nohy mrznou rychleji. Raději vybírejte o něco větší velikost boty a vlněnou ponožku.'),
         ('Kde najdu další merino výbavu?', 'V kategoriích merino oblečení, merino trička, merino spodní prádlo, merino mikiny a merino doplňky. Všechny najdete v hlavním přehledu merino výbavy.')],
)

# ------------------------------------------------------------------ lyzarske-helmy
NEW['lyzarske-helmy'] = dict(long=True,
    title='Lyžařské helmy: výběr, velikost a nabídky | Sporteka',
    desc='Lyžařské a snowboardové helmy pro dospělé i děti: konstrukce, velikost, ventilace, MIPS a péče. Průvodce výběrem a nabídky obchodů vedle sebe.',
    intro='<p><strong>Lyžařská helma</strong> je nejdůležitější kus výbavy, který se dá na svahu koupit. Chrání hlavu při pádu i při srážce a na sjezdovkách je dnes samozřejmostí u dětí i dospělých. Dobře vybraná helma sedí pevně, nepřekáží brýlím a nevadí při pohybu. Špatně zvolená velikost znamená, že při nárazu nechrání tak, jak má. Právě proto se vyplatí věnovat výběru čas, zkoušet několik modelů a nespoléhat jen na barvu nebo cenovku.</p>'
          '<p>Na Sportece porovnáte <strong>lyžařské a snowboardové helmy</strong> z českých obchodů a nabídky uvidíte vedle sebe. K helmě patří <a href="/lyzarske-bryle/">lyžařské brýle</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, <a href="/lyzarske-rukavice/">rukavice</a> a <a href="/lyzarske-boty/">boty</a>. Pro začátečníky a děti doporučujeme také <a href="/snowboardove-chranice/">chrániče páteře a boků</a>.</p>',
    guide='<h2>Jak je helma postavená a co dělá</h2>'
          '<p>Helma se skládá ze dvou hlavních vrstev. Vnější skořepina je tvrdší a rozděluje sílu nárazu na větší plochu, vnitřní pěnová vrstva se při nárazu stlačí a pohltí energii. Pak následuje měkká výstelka, která zajišťuje pohodlí a těsné sezení. Rozdíly mezi modely vyplývají z toho, jak jsou obě vrstvy spojené a jak velká část hlavy je pokrytá.</p>'
          '<h3>Typy konstrukce</h3>'
          + T(['Konstrukce', 'Jak funguje', 'Pro koho'], [
              ['In-mold', 'tenká skořepina je slisovaná přímo s pěnou, helma je lehká a dobře větraná', 'většina rekreačních lyžařů a snowboardistů'],
              ['Hard shell', 'samostatná pevná skořepina nalepená na pěnu, odolnější proti drobným poškozením', 'děti, školy, často používané půjčovny'],
              ['Hybrid', 'kombinuje pevný vrch a lehčí spodek s větráním', 'ti, kdo chtějí kompromis mezi váhou a odolností'],
              ['Se systémem rotace', 'vnitřní vrstva se může otáčet vůči skořepině při šikmém nárazu', 'všichni, kdo chtějí dodatečnou ochranu při pádu']]) +
          '<p>Systémy označované jako MIPS a podobné vycházejí z toho, že při šikmém nárazu se hlava může otáčet. Výrobci tvrdí, že jejich vložka snižuje rotační síly přenášené na mozek. Informace o testech najdete v popisu konkrétního modelu a je dobré ji brát jako doplněk ke správné velikosti, ne jako náhradu.</p>'
          '<h2>Velikost a sezení: základ všeho</h2>'
          '<p>Helma musí sedět pevně, ale bez tlaku. Změřte obvod hlavy měkkým metrem těsně nad obočím a ušima a porovnejte s tabulkou výrobce. Pokud jste mezi dvěma velikostmi, zkuste obě. Na hlavě by se helma neměla pohybovat, když zakroutíte hlavou ze strany na stranu, a po zapnutí řemínku se nesmí posunout dozadu ani dopředu.</p>'
          '<ul><li>Okraj helmy má ležet asi dva prsty nad obočím, ne na něm.</li>'
          '<li>Řemínek pod bradou se zapíná tak, aby se dal vsunout jeden prst.</li>'
          '<li>Boční řemínky mají tvořit trojúhelník pod ušima, ne ležet na uších.</li>'
          '<li>Helmu zkoušejte s tenkou kuklou nebo bez čepice, silná čepice mění sezení a helma pak nedrží.</li>'
          '<li>Pokud helma tlačí v jednom místě, zkuste jiný tvar. Některé značky mají užší, jiné kulatější vnitřek.</li></ul>'
          '<h2>Větrání a teplota</h2>'
          '<p>Otvory v helmě pomáhají odvádět teplo a vlhkost. Na jaře, při intenzivní jízdě nebo při pohybu do kopce vyhledejte model s nastavitelným větráním, které se dá zavřít jedním posuvníkem. V mrazu se naopak hodí zavřené otvory a hustší výstelka. Vlhkost se v helmě rychle zachytává, proto se vyplatí vyjímatelná a pratelná výstelka.</p>'
          '<h2>Brýle a helma jako celek</h2>'
          '<p>Brýle by měly těsně doléhat k okraji helmy bez mezery, kterou prochází vítr a zimní vzduch na čelo. Mnoho helem má na zadní straně úchyt, který drží pásek brýlí na místě. Před koupí si ověřte, že brýle a helma pocházejí z kompatibilní řady, nebo je vyzkoušejte spolu. Další tipy najdete v kategorii <a href="/lyzarske-bryle/">lyžařské brýle</a>.</p>'
          '<h2>Podle sportu a stylu jízdy</h2>'
          '<ul><li><strong>Sjezdové lyžování na sjezdovce:</strong> univerzální in-mold helma s větráním a vyjímatelnou výstelkou.</li>'
          '<li><strong>Snowboard a freestyle:</strong> často s odnímatelnými ušními částmi a s možností úchytu na kameru, více v oddílu <a href="/snowboarding/">snowboarding</a>.</li>'
          '<li><strong>Skialpinismus:</strong> lehčí helma, někdy certifikovaná i pro horolezecké použití, viz <a href="/skialpinismus/">skialpinismus</a>.</li>'
          '<li><strong>Freeride a mimo sjezdovku:</strong> pevnější kryt i na zátylku a větší krytí uší.</li>'
          '<li><strong>Běžecké lyžování:</strong> většinou stačí lehká helma s dobrým větráním, informace o vybavení jsou v oddílu <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</li>'
          '<li><strong>Závodní jízda:</strong> pevný kryt s uzavřenými částmi a často i s bradovou ochranou.</li></ul>'
          '<h2>Dětské helmy</h2>'
          '<p>Dětská hlava roste rychle a jen málokterá helma vydrží víc sezón. Nevybírejte ji o dvě velikosti větší, protože by se na hlavě točila. Mnoho dětských modelů má pomocný kolečkový systém, kterým se dá obvod upravit. Při každém začátku sezóny zkontrolujte sezení. Pro nejmenší dětské lyžaře se hodí kombinace helmy, <a href="/detske-lyze/">dětských lyží</a> a <a href="/lyzarske-hole/">lyžařských holí</a>.</p>'
          '<p>Barvy a motivy dětem pomáhají helmu přijmout, ale rozhodující je pohodlí. Pokud dítě helmu sundává, zkontrolujte, jestli netlačí řemínek, nebo jestli není moc teplá.</p>'
          '<h2>Kdy helmu vyměnit</h2>'
          '<p>Po silném nárazu je třeba helmu vyměnit, i když zvenku nevypadá poškozená, protože pěna se mohla stlačit nebo prasknout uvnitř. Totéž platí při viditelných prasklinách, deformaci nebo uvolněné výstelce. Výrobci také doporučují obměnu po několika letech používání, protože materiály stárnou vlivem slunce, potu a teplotních výkyvů. Konkrétní lhůtu najdete v návodu.</p>'
          '<p>Helmu nikdy nepůjčujte po úrazu a nekupujte použitou, pokud nevíte, co se s ní dělo. Poškozená pěna není zvenku poznat a vypadá jako nová.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Povrch otřete vlhkým hadříkem a jemným mýdlem, žádná rozpouštědla ani agresivní čističe.</li>'
          '<li>Výstelku perte ručně, pokud je vyjímatelná, a nechte ji uschnout při pokojové teplotě.</li>'
          '<li>Helmu nenechávejte v zavazadlovém prostoru auta při velkém horku ani mrazu.</li>'
          '<li>Nepřipevňujte samolepky, které obsahují rozpouštědla, mohou poškodit povrch.</li>'
          '<li>Přepravujte ji v obalu nebo v batohu, ne volně mezi tvrdými předměty.</li></ul>'
          '<h2>Kamera, reproduktory a další doplňky</h2>'
          '<p>Některé helmy mají úchyt na akční kameru nebo vestavěná sluchátka. Úchyt na vrchu helmy zvyšuje riziko, že se při pádu zachytí, a proto jej výrobci často navrhují tak, aby se uvolnil. Poslech hudby při jízdě snižuje vnímání okolí, takže při větším provozu na svahu je rozumnější zvuk vypnout.</p>'
          '<h2>Helma v různých podmínkách</h2>'
          '<p>Za mrazu a při větru zavřete větrací otvory a pod helmu přidejte jen tenkou kuklu, aby sezení zůstalo stejné. Za jarního slunce se naopak vyplatí otvory otevřít a vybrat světlejší barvu, která se tolik nezahřívá. Při mlze a sněžení je viditelnost nižší, proto výrazná barva helmy pomáhá ostatním vás zahlédnout. Při jízdě v lese se vyplatí model s dobrým krytím zátylku a uší, protože větve a pády do stromů jsou častější než na upravené sjezdovce.</p>'
          '<h2>Helma při přepravě a na chatě</h2>'
          '<p>Při cestě autem a ve vleku nenechávejte helmu ležet mezi lyžemi a holemi, kde ji může poškodit tlak nebo úder. Po sjezdovce ji nepokládejte na zem před chatou, protože sníh a vlhkost se dostanou do větracích otvorů. Večer ji vyvětrejte a uložte na suché místo, aby výstelka do rána uschla.</p>'
          '<h2>Jak helmu správně nasadit a upravit</h2>'
          '<p>Nasazujte ji rovně, tak aby kryla čelo a spánky, a teprve potom zapněte řemínek. Pokud má helma nastavovací kolečko na zátylku, dotáhněte je, až je sezení pevné, ale pohodlné. Pak zkuste zvednout hlavu a podívat se dolů, helma se nesmí zvednout ani zakrýt zorné pole. Před každou sezónou zkontrolujte přezku, řemínky a výstelku. Oděrky, rozedrané popruhy nebo uvolněná pěna jsou signál k výměně.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Velký výběr nabízejí ' + B(('alpina', 'Alpina'), ('uvex', 'Uvex'), ('relax', 'Relax'), ('smith', 'Smith'), ('rossignol', 'Rossignol'), ('poc', 'Poc'), ('head', 'Head'), ('salomon', 'Salomon'), ('arcore', 'Arcore'), ('briko', 'Briko'), ('k2', 'K2'), ('atomic', 'Atomic'), ('giro', 'Giro'), ('cairn', 'Cairn')) + '. Každá značka má trochu jiný tvar vnitřku, proto helmu nevybírejte jen podle loga, ale podle toho, jak sedí na vaší hlavě.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Kupovat helmu bez zkoušení a spoléhat na odhad velikosti.</li>'
          '<li>Dětem pořizovat helmu s velkou rezervou na růst.</li>'
          '<li>Používat helmu po silném nárazu, protože zvenku nevypadá poškozená.</li>'
          '<li>Nechat řemínek uvolněný, takže při pádu helma sklouzne.</li>'
          '<li>Nosit helmu s příliš silnou čepicí, která posune celý systém.</li>'
          '<li>Vybrat brýle a helmu zvlášť bez ověření, že k sobě sedí.</li></ul>'
          '<h2>Kompletní výbava na svah</h2>'
          '<p>K helmě se kupují další kusy. Kromě brýlí a rukavic přijdou vhod <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-kalhoty/">kalhoty</a>, <a href="/lyzarske-termopradlo/">termoprádlo</a> a <a href="/lyzarske-ponozky/">lyžařské ponožky</a>. Podrobnější přehled najdete v kategorii <a href="/lyzarske-obleceni/">lyžařské oblečení</a> nebo ve skupině <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Při výběru začněte velikostí a sportem. Pak zúžte nabídku podle značky a přidané funkce. U každého kusu vidíte více obchodů, takže poznáte, kde je vaše velikost skladem. Doporučujeme přečíst si popis, protože právě tam výrobci uvádějí informace o certifikaci a o systémech pro snížení rotace.</p>',
    faq=[('Je helma na lyžích povinná?', 'Povinnost se liší podle země, proto si před výjezdem ověřte pravidla místa, kam jedete. Bez ohledu na předpisy ochranu hlavy doporučují všichni, kdo se jízdě na svahu věnují, a u dětí je to samozřejmost.'),
         ('Jak poznám správnou velikost helmy?', 'Změřte obvod hlavy nad obočím a uši a podívejte se do tabulky výrobce. Helma má sedět pevně, nehýbat se při kroucení hlavou a netlačit v žádném místě. Při pochybnostech vyzkoušejte dvě sousední velikosti.'),
         ('Co znamená MIPS?', 'Je to označení systému s vnitřní vrstvou, která se může při šikmém nárazu posunout vůči skořepině. Výrobci tvrdí, že tím snižuje rotační síly působící na hlavu. Podrobnosti hledejte v popisu konkrétního modelu.'),
         ('Jaký je rozdíl mezi in-mold a hard shell?', 'In-mold je lehká konstrukce, kde je skořepina slisovaná s pěnou. Hard shell má samostatnou pevnou skořepinu a bývá odolnější vůči drobnému poškození, ale je o něco těžší.'),
         ('Mohu v lyžařské helmě jezdit na snowboardu?', 'Ano, většina lyžařských helem je určena pro oba sporty. Rozdíl bývá hlavně ve stylu a v doplňcích, například v odnímatelných ušních částech.'),
         ('Jak často měnit helmu?', 'Vždy po silném nárazu a při jakémkoli poškození. Jinak se řiďte pokyny výrobce, který obvykle doporučuje obměnu po několika letech používání, protože materiály stárnou.'),
         ('Mám nosit čepici pod helmou?', 'Jen velmi tenkou, nebo vůbec. Silná čepice mění sezení a helma pak nesedí tak pevně. Raději vybírejte helmu s výstelkou a doplňte tenkou kuklu nebo nákrčník.'),
         ('Jak vybrat helmu pro dítě?', 'Změřte obvod hlavy, vyberte velikost bez velké rezervy a zkontrolujte pevné zapnutí řemínku. Hodí se model s nastavovacím systémem, protože dítě roste, ale nekupujte helmu větší, než je potřeba.'),
         ('Hodí se lyžařská helma i na kolo?', 'Obecně ne. Cyklistické helmy mají jinou konstrukci a certifikaci a lyžařské jsou těžší a hůř větrané. Pro kolo si vyberte model určený pro cyklistiku.'),
         ('Jak čistit lyžařskou helmu?', 'Vlhkým hadříkem a jemným mýdlem, výstelku podle návodu ručně. Nepoužívejte rozpouštědla a nesušte helmu na topení. Skladujte ji na suchém místě mimo přímé slunce.'),
         ('Která helma je vhodná s brýlemi?', 'Taková, která s brýlemi vytváří uzavřený okraj bez mezery na čele. Nejlepší je obě věci vyzkoušet společně nebo vybrat brýle od stejného výrobce jako helmu.')],
)

# ------------------------------------------------------------------ bojove-sporty
NEW['bojove-sporty'] = dict(long=True,
    title='Bojové sporty: rukavice, pytle, chrániče | Sporteka',
    desc='Výbava pro box, MMA, karate, judo a kickbox: rukavice, pytle, chrániče a kimona. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Bojové sporty</strong> mají společné jedno pravidlo: výbava musí sedět a odpovídat disciplíně. Rukavice na box se liší od rukavic na MMA, kimono na judo od kimona na karate a pytel pro začátečníka od pytle pro hodiny údernické techniky. Kdo si vybere podle stylu a velikosti, trénuje pohodlněji a chrání si ruce, kolena i zuby. Dobrá výbava také vydrží déle, a proto se jí vyplatí věnovat pár minut navíc.</p>'
          '<p>Na Sportece najdete <strong>výbavu pro bojové sporty</strong> z českých obchodů a nabídky porovnáte vedle sebe. Hlavní podkategorie jsou <a href="/boxerske-rukavice/">boxerské rukavice</a>, <a href="/boxovaci-pytle/">boxovací pytle a hrušky</a>, <a href="/chranice-bojove-sporty/">chrániče</a> a <a href="/obleceni-bojove-sporty/">kimona a oblečení</a>. K tréninku se hodí také <a href="/fitness/">fitness</a> a <a href="/funkcni-trenink/">funkční trénink</a>.</p>',
    guide='<h2>Která výbava patří ke kterému sportu</h2>'
          '<p>Než začnete nakupovat, ujasněte si, co budete trénovat. Boxer potřebuje jiné rukavice než karatista a trenér v oddílu často řekne, co povinně vyžaduje. Následující tabulka pomůže se základní orientací.</p>'
          + T(['Sport', 'Základ výbavy', 'Doplňky'], [
              ['Box', 'rukavice, bandáže, chránič zubů, skákací lano', 'pytel, hruška, boxerské boty'],
              ['Kickbox a muay thai', 'rukavice, holeně, chránič zubů a rozkroku', 'tlapy, lapy, krátké šortky'],
              ['MMA a grappling', 'rukavice na MMA, rashguard, chránič zubů', 'kimono nebo gi, chrániče kolen'],
              ['Karate a taekwondo', 'kimono nebo dobok, pás, chrániče rukou a nohou', 'chránič zubů, helma, vesta podle soutěže'],
              ['Judo a BJJ', 'kimono, pás, obuv do šaten', 'chrániče prstů, kapa'],
              ['Funkční a kondiční box', 'lehčí rukavice, pytel, švihadlo', 'bandáže, obuv s pevným držením']]) +
          '<h2>Boxerské rukavice: velikost, váha a účel</h2>'
          '<p>Velikost rukavic se označuje v uncích, což je jednotka hmotnosti. Čím větší číslo, tím víc vycpávky a tím lépe chrání ruku i soupeře. Pro trénink s pytlem se běžně volí menší velikosti než pro sparring. V klubu vám zpravidla poradí, co je potřeba, protože pravidla soutěží stanovují minimální váhu v závislosti na váhové kategorii.</p>'
          '<ul><li><strong>Rukavice na pytel</strong> mají tužší výplň a bývají užší, aby šly rychle udeřit.</li>'
          '<li><strong>Sparringové rukavice</strong> jsou měkčí, objemnější a chrání soupeře.</li>'
          '<li><strong>Soutěžní rukavice</strong> splňují pravidla organizace, kde se soutěží.</li>'
          '<li><strong>MMA rukavice</strong> jsou lehké, s otevřenými prsty, aby šlo chytat soupeře.</li>'
          '<li><strong>Dětské rukavice</strong> mají menší střih a lehčí výplň, aby se dítě dobře učilo techniku.</li></ul>'
          '<p>Zapínání na suchý zip je rychlé a hodí se na trénink. Šněrování je tradiční a drží lépe, ale vyžaduje druhou osobu. Materiál může být kůže nebo syntetika. Kůže vydrží déle a časem se přizpůsobí ruce, syntetika bývá lehčí na údržbu. Bližší přehled nabízí kategorie <a href="/boxerske-rukavice/">boxerské rukavice</a>.</p>'
          '<h2>Bandáže a ochrana zápěstí</h2>'
          '<p>Bandáže se omotávají kolem zápěstí a dlaně pod rukavici. Stabilizují zápěstí, rozkládají sílu úderu a pohlcují pot. Existují elastické i neelastické varianty a také vložky s gelem. Správné obtočení si nechte předvést od trenéra, protože příliš těsné bandáže brání prokrvení. Po tréninku je vypraná bandáž suchá a připravená na další použití.</p>'
          '<h2>Boxovací pytle a hrušky</h2>'
          '<p>Pytel musí odpovídat tréninku i prostoru. Těžší pytel snese silnější údery a méně se kývá, lehčí je vhodný pro začátečníky a děti. Jako vodítko slouží pravidlo, že pytel by neměl vážit méně než polovinu hmotnosti cvičence, avšak přesnou hodnotu určuje zkušený trenér. Pytel se plní textilem, pískem nebo se sypkým materiálem, a záleží na tom, jak má být tvrdý.</p>'
          '<ul><li><strong>Závěsný pytel</strong> se zavěšuje na strop, stojan nebo držák a hodí se pro všechny druhy úderů.</li>'
          '<li><strong>Stojanové pytle</strong> se plní vodou nebo pískem a nevyžadují vrtání do stropu, ale zabírají podlahu.</li>'
          '<li><strong>Hrušky</strong> slouží k nácviku rychlosti, rytmu a koordinace, jsou menší a lehké.</li>'
          '<li><strong>Reflexní míče, speed bag a double-end bag</strong> pomáhají rozvíjet reflexy a přesnost.</li>'
          '<li><strong>Dětské pytle</strong> bývají měkčí a lehčí, vhodné pro první tréninky v domácím prostředí.</li></ul>'
          '<p>Při zavěšení myslete na nosnost stropu a použijte vhodné úchyty. Nízký strop nebo křehká zeď jsou častým důvodem, proč se vyplatí stojan. Chodby a byty ve vyšších patrech řešte s ohledem na sousedy, protože údery se šíří konstrukcí budovy. Podrobný výběr najdete v kategorii <a href="/boxovaci-pytle/">boxovací pytle a hrušky</a>.</p>'
          '<h2>Chrániče: co chrání a kdy je povinné</h2>'
          '<p>Chrániče snižují riziko úrazu a jejich nošení bývá u sparringu samozřejmost. Většina oddílů dělá ze zubního chrániče a chrániče rozkroku povinnost. Vybírejte chrániče, které při pohybu nesklouzávají a neomezují dýchání nebo výhled.</p>'
          '<ul><li><strong>Chránič zubů</strong> se dodává univerzální nebo tvarovatelný ve vodě. Pro lepší sedění ho nechte vytvarovat podle návodu.</li>'
          '<li><strong>Chránič rozkroku</strong> je u mužů základ pro jakýkoli kontaktní sport.</li>'
          '<li><strong>Chrániče holení a nártů</strong> se používají při kickboxu, muay thai a taekwondu.</li>'
          '<li><strong>Helma</strong> chrání při sparringu hlavu a obočí, ale nenahrazuje techniku a odpovědný přístup.</li>'
          '<li><strong>Chrániče loktů a kolen</strong> pomáhají při grapplingu a při pádech.</li>'
          '<li><strong>Chránič hrudníku</strong> používají ženy i děti v disciplínách se silným kontaktem.</li></ul>'
          '<p>Další informace jsou v kategorii <a href="/chranice-bojove-sporty/">chrániče</a>. Související ochranu najdete také v oddílech <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> a <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Kimona, doboky a oblečení</h2>'
          '<p>Kimono se vybírá podle sportu. Judogi je tužší a odolné proti tahu, karate gi je lehčí a volnější, kimono na BJJ bývá přiléhavější a má zpevněné části, za které soupeř chytá. Pás označuje stupeň a obvykle si ho pořizujete podle trenéra nebo zkoušek. Velikost se řídí výškou i váhou podle tabulky výrobce. Nové kimono se při prvním praní často srazí, proto kupujte spíše s malou rezervou.</p>'
          '<ul><li><strong>Rashguardy</strong> jsou těsná trička s dlouhým nebo krátkým rukávem pod kimono nebo samostatně.</li>'
          '<li><strong>Šortky na MMA a muay thai</strong> mají široký rozkrok a lehký materiál.</li>'
          '<li><strong>Legíny a kompresní kalhoty</strong> se nosí pod šortky nebo samostatně na grappling.</li>'
          '<li><strong>Boxerská obuv</strong> je lehká, vysoká nad kotník a má tenkou podrážku pro cit v nohou.</li></ul>'
          '<p>K běžnému tréninku stačí i funkční oblečení, viz <a href="/funkcni-tricka/">funkční trička</a> a <a href="/sportovni-kratasy/">sportovní kraťasy</a>. Pro zahřívání se hodí <a href="/svihadla/">švihadla</a>.</p>'
          '<h2>Výbava pro děti</h2>'
          '<p>Děti rostou rychle, takže se vyplatí volit výbavu bez velké rezervy. Důležité je, aby chrániče seděly pevně a neomezovaly pohyb. Dětské rukavice mají menší výplň, ale spolehlivé zapínání. U kimon počítejte s tím, že kalhoty a sako se dají prodloužit pomocí manžet, jenže přehnaná rezerva je na překážku. Pokud si nejste jisti, zeptejte se trenéra, protože pravidla soutěží se mohou lišit podle věku.</p>'
          '<h2>Jak se vyhnout zápachu a opotřebení</h2>'
          '<p>Pot je největší nepřítel rukavic a chráničů. Po tréninku je vyndejte z tašky a nechte je vyvětrat. Sáčky s absorbérem vlhkosti nebo vložky do rukavic zrychlují schnutí. Chrániče a rukavice nikdy nesušte na topení, kůže by popraskala a výplň ztratila tvar. Povrch otírejte jemným prostředkem a čas od času použijte přípravek na kůži. Kimono perte v teplé vodě podle návodu a sušte na vzduchu.</p>'
          '<h2>Jak začít a nepřipravit se o zdraví</h2>'
          '<p>Před prvním tréninkem je rozumné dohodnout se s oddílem, co si vzít, a nenakupovat vše naráz. Nejdřív se pořizuje to, co používáte při každé hodině, tedy rukavice, bandáže a lano. Chrániče se přidávají, jakmile přijde na řadu sparring. Pokud máte zdravotní omezení, poraďte se předem s lékařem. Dobré základy techniky se vyplatí víc než nejdražší vybavení a trenér pozná včas, kdy se začátečník přetěžuje.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce jsou nejčastěji ' + B(('dbx-bushido', 'DBX Bushido'), ('bushido', 'Bushido'), ('hms', 'HMS'), ('venum', 'Venum'), ('acra-sport', 'ACRA Sport'), ('leone-1947', 'Leone 1947'), ('rdx', 'RDX'), ('fairtex', 'Fairtex'), ('insportline', 'Insportline'), ('benlee', 'Benlee'), ('opro', 'Opro'), ('safe-jawz', 'Safe Jawz')) + '. Střihy se u jednotlivých značek liší, takže při opakovaném nákupu se řiďte velikostní tabulkou konkrétní řady.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit příliš lehké rukavice na sparring a ohrozit soupeře i sebe.</li>'
          '<li>Pořídit těžký pytel bez ověření, zda jej strop unese.</li>'
          '<li>Vynechat bandáže, protože rukavice se jeví jako dostatečná ochrana.</li>'
          '<li>Koupit kimono podle módy, ne podle disciplíny.</li>'
          '<li>Nechat vlhkou výbavu zavřenou v tašce a pak se divit, že zapáchá.</li>'
          '<li>Před prvním nákupem se neporadit s trenérem, který zná pravidla oddílu.</li></ul>'
          '<h2>Pro koho je která varianta</h2>'
          '<p>Začátečník domů potřebuje rukavice, bandáže a lano, případně lehčí pytel. Pokročilý přidává chrániče, gumy na odpor a tlapy. Člen oddílu používá to, co trenér požaduje, a doplňuje kvalitu. Rodič dětí vybírá spíš měkké a bezpečné kusy. Pokud chcete jen kondiční trénink bez kontaktu, stačí rukavice a pytel, další ochrana se doplní až při sparringu. Další pohybové aktivity najdete v kategoriích <a href="/funkcni-trenink/">funkční trénink</a>, <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Vyberte nejprve podkategorii, pak zúžte podle sportu, velikosti a značky. U každého kusu uvidíte nabídky více obchodů, takže snadno zjistíte, kde je vaše velikost skladem. Pro bezpečnost nešetřete na ochraně, kterou používáte při kontaktu, a před soutěží si ověřte, jaké předpisy výbava musí splňovat.</p>',
    faq=[('Jaké boxerské rukavice vybrat na začátek?', 'Pro trénink s pytlem a základní práci stačí univerzální rukavice střední velikosti se suchým zipem. Pokud chcete sparring, zeptejte se trenéra na doporučenou váhu, protože se liší podle hmotnosti cvičence a pravidel oddílu.'),
         ('Co znamená označení uncí u rukavic?', 'Unce udávají velikost rukavic a obvykle i množství výplně. Větší číslo znamená víc ochrany pro ruce i partnera. Přesné doporučení závisí na váze cvičence, účelu tréninku a pravidlech oddílu.'),
         ('Potřebuji bandáže pod rukavice?', 'Ano, doporučuje se je používat. Stabilizují zápěstí, snižují tlak na klouby a pohlcují pot. Naučit se je správně omotat vám může ukázat trenér.'),
         ('Jaký pytel zvolit do bytu nebo domu?', 'Stojanový pytel nevyžaduje vrtání do stropu, ale potřebuje plochu na podlaze. Závěsný pytel je tišší na údery, ale musí mít pevný strop nebo nosnou konstrukci. Ověřte nosnost a zohledněte sousedy.'),
         ('Čím naplnit boxovací pytel?', 'Většinou textilem nebo speciální výplní, někdy pískem. Textil je měkčí a lehčí, písek tvrdší a těžší. Pytle se prodávají prázdné i plné, takže pozorně čtěte popis.'),
         ('Je chránič zubů povinný?', 'U sparringu a soutěží ho vyžaduje většina oddílů. Chrání zuby, čelist i jazyk. Dobře sedící chránič se vytvaruje ve vodě podle návodu, aby neklouzal.'),
         ('Jak vybrat velikost kimona?', 'Podle výšky, ne podle váhy, a podle tabulky konkrétního výrobce. Nové kimono se při prvním praní může srazit, takže počítejte s malou rezervou, ale nekupujte moc velké.'),
         ('Čím se liší judogi od karate gi?', 'Judogi je silnější a tužší, protože odolává chytání a tahu. Karate gi je lehčí a volnější, aby neomezovalo kopy a údery. Kimono na BJJ je přiléhavější a má zpevněné části.'),
         ('Jak odstranit zápach z rukavic?', 'Po tréninku je nechte vyvětrat na místě s proudem vzduchu, použijte vložky pohlcující vlhkost a občas povrch otřete jemným prostředkem. Nesušte je na topení, aby kůže nepopraskala.'),
         ('Jakou výbavu potřebuje dítě na první trénink?', 'Většinou stačí pohodlné sportovní oblečení a to, co doporučí trenér. Rukavice, chránič zubů a základní chrániče se kupují později. Ptejte se oddílu, protože pravidla se liší podle sportu.'),
         ('Kde najdu další fitness výbavu?', 'V kategoriích fitness, funkční trénink, fitness pomůcky a posilovací gumy. K bojovým sportům se hodí také lano, kettlebelly nebo gymnastické pomůcky.')],
)

# ------------------------------------------------------------------ horolezectvi
NEW['horolezectvi'] = dict(long=True,
    title='Horolezectví a ferraty: výbava a nabídky | Sporteka',
    desc='Horolezecká výbava a ferraty: lezečky, sedáky, přilby, lana, karabiny a sety. Průvodce výběrem podle stylu lezení a nabídky českých obchodů.',
    intro='<p><strong>Horolezecká výbava</strong> je oblast, kde záleží na bezpečnosti víc než kdekoli jinde v outdooru. Lezečky, sedák, přilba, lano a karabiny se pořizují s ohledem na styl lezení, tedy zda půjdete na umělou stěnu, do skal, na via ferratu, nebo do hor. Špatně zvolený kus může znamenat nepohodlí, v horším případě ohrožení bezpečnosti. Proto se vyplatí číst popisy, ověřovat certifikace a při pochybnostech se zeptat zkušenějších lezců.</p>'
          '<p>Na Sportece najdete <strong>horolezectví a ferraty</strong> z českých obchodů a nabídky porovnáte vedle sebe. Rozcestník vede do podkategorií <a href="/lezecke-boty/">lezečky</a>, <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky, přilby a pomůcky</a> a <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>. K výšlapům se hodí také <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/trekova-obuv/">trekové boty</a>.</p>',
    guide='<h2>Jak se liší jednotlivé styly lezení</h2>'
          '<p>Dříve než se pustíte do nákupu, určete si, co budete provozovat. Výbava pro stěnu je jiná než pro skály nebo pro horu, a ne každý kus se hodí všude.</p>'
          + T(['Styl', 'Co potřebujete', 'Na co dát pozor'], [
              ['Lezení na stěně', 'lezečky, sedák, magnezium a pytlík, jistítko', 'pohodlí lezeček, čistota obuvi, vybavení stěny'],
              ['Sportovní lezení ve skalách', 'lezečky, sedák, lano, expresky, přilba, jistítko', 'délka lana a typ expres sestav'],
              ['Tradiční a vícedélkové lezení', 'sedák, lano, smyčky, friendy a vklíněnce, přilba', 'kompatibilita, zkušenosti a kurz'],
              ['Via ferrata', 'ferratový set, sedák, přilba, rukavice', 'pevné boty, plná certifikace sady'],
              ['Alpské túry a horolezectví', 'sedák, lano, mačky, cepín, přilba, batoh', 'váha výbavy, znalost terénu a počasí']]) +
          '<h2>Lezečky: sedět musí jako ponožka</h2>'
          '<p>Lezecká obuv sedí těsněji než běžná, aby cítila stupy. Cílem není bolest, ale pevné držení bez prostoru mezi nohou a botou. Na začátek volte pohodlnější plochý střih, který nevyžaduje stažené prsty. Zkušenější lezci používají předehnutý tvar, který pomáhá na převisech a malých stupech, ale je náročnější na sezení.</p>'
          '<ul><li><strong>Plochý střih</strong> je vhodný pro začátečníky, na dlouhé cesty a pro celodenní lezení.</li>'
          '<li><strong>Mírně předehnutý</strong> se hodí na kombinaci stěny a skal.</li>'
          '<li><strong>Silně asymetrický</strong> střih je určený pro náročné cesty a bouldering.</li>'
          '<li><strong>Suchý zip, tkaničky nebo pantofle:</strong> suchý zip je rychlý, tkaničky pevné, pantofle skvělé na boulder a stěnu.</li></ul>'
          '<p>Materiál může být kůže nebo syntetika. Kůže se časem roztahuje, syntetika méně, takže při koupi počítejte s tím, jak se bude bota chovat. Podrážka a její hrubost rozhodují o tom, jak boty drží na třecích stupech. Podrobnosti a nabídky jsou v kategorii <a href="/lezecke-boty/">lezečky</a>.</p>'
          '<h2>Sedáky a přilby</h2>'
          '<p>Sedák je spojení lezce s lanem a musí sedět pevně, aby se z něj nedalo vyklouznout. Popruhy kolem pasu a nohou mají být nastavené tak, aby se pod ně vešla dlaň. Při pohybu se nesmí sedák posouvat ani škrtit. Sportovní sedáky jsou lehké, vícedélkové a horské mívají více poutek pro vybavení. Dětské sedáky mají často přidaný hrudní popruh, který zvyšuje stabilitu.</p>'
          '<ul><li><strong>Stěnové sedáky</strong> jsou pohodlné a mají měkké čalounění.</li>'
          '<li><strong>Sportovní sedáky</strong> jsou lehčí a méně vypolstrované.</li>'
          '<li><strong>Horské sedáky</strong> jsou lehké, skladné a často nastavitelné přes zimní oblečení.</li>'
          '<li><strong>Celotělové sedáky</strong> se používají pro děti a pro speciální práce.</li></ul>'
          '<p>Přilba chrání před padajícími kameny a při pádu. Vybírejte takovou, která má certifikaci pro horolezectví, a nasaďte ji pevně s řemínkem pod bradou. Cyklistickou nebo lyžařskou helmu na lezení nepoužívejte, pokud není výslovně určena i pro horolezectví. Každý typ je navržený na jiný náraz. Související kusy najdete v kategoriích <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/cyklisticke-helmy/">cyklistické helmy</a>, ale ty nejsou náhradou za lezeckou přilbu.</p>'
          '<h2>Lana, smyčky a karabiny</h2>'
          '<p>Dynamické lano se při pádu natáhne a pohltí část energie. Statické lano se používá na slaňování, výstup nebo záchranu a nepohlcuje pády. Typ, průměr a délka vycházejí z použití. Tenčí lano je lehčí, ale rychleji se opotřebuje, silnější je odolnější a pohodlnější při jištění.</p>'
          '<ul><li><strong>Jednoduchá lana</strong> se používají na sportovní lezení a stěnu.</li>'
          '<li><strong>Dvojitá a půlená lana</strong> jsou určena pro vícedélkové lezení a alpské cesty.</li>'
          '<li><strong>Karabiny</strong> se liší tvarem, zámkem a nosností, základní jsou zajišťovací a lehké.</li>'
          '<li><strong>Expresky</strong> jsou dvě karabiny spojené poutkem a slouží k jištění ve skále.</li>'
          '<li><strong>Smyčky a popruhy</strong> se používají na stanoviště, slaňování a sebezajištění.</li></ul>'
          '<p>Při výběru věnujte pozornost označení nosnosti a certifikaci. Každý prvek v řetězci musí být určen pro horolezectví a použit v souladu s návodem. Nikdy nekombinujte prvky, jejichž kompatibilitu neznáte. Podrobný výběr najdete v kategorii <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>.</p>'
          '<h2>Jistítka a slaňovací pomůcky</h2>'
          '<p>Jistítko, například tuber nebo model s asistovaným brzděním, slouží k jištění partnera a slaňování. Jistítka s asistovaným brzděním pomáhají zachytit pád, ale nenahrazují techniku a jistič musí lano držet vždy. Osmička je slaňovací pomůcka, k jištění se nehodí. Před koupí si ověřte, které lano a jaký průměr jistítko požaduje, a pokud jistítko poprvé používáte, naučte se s ním pracovat na kurzu nebo s instruktorem. Žádná příručka nenahradí praktické cvičení.</p>'
          '<h2>Ferraty: co si vzít</h2>'
          '<p>Via ferrata je jištěná cesta, kde se člověk zachycuje ocelovým lanem. Základ tvoří ferratový set s tlumičem pádu, sedák a přilba. Rukavice chrání dlaně před drátem a mačkáním. Pevné boty s dobrým držením jsou lepší než měkká obuv. Před výstupem si přečtěte popis cesty a obtížnost, protože ne všechny ferraty jsou vhodné pro začátečníky a děti.</p>'
          '<ul><li>Set s absorbérem energie je nutnost, obyčejné popruhy nestačí.</li>'
          '<li>Při pádu se má absorbér rozvinout, proto se nikdy nesmí svazovat ani zkracovat.</li>'
          '<li>Na jedné sadě nesmí být víc lidí, každý má vlastní.</li>'
          '<li>Pro děti existují speciální sety, které odpovídají hmotnosti dítěte.</li></ul>'
          '<h2>Magnezium, pytlíky a pomůcky</h2>'
          '<p>Magnezium zlepšuje přilnavost prstů při pocení. Existuje v prášku, kuličkách nebo tekuté podobě a ukládá se do pytlíku u pasu nebo do bloku pro boulder. Kartáče na stupy, páska na prsty a péče o ruce jsou další věci, které často chybějí v základní výbavě. Další doplňky sedí v kategoriích <a href="/outdoor-doplnky/">outdoor doplňky</a> a <a href="/prvni-pomoc/">první pomoc</a>.</p>'
          '<h2>Oblečení a doplňky na lezení</h2>'
          '<p>Při lezení se hodí pohyblivé kalhoty, které nebrání zvedání nohou, a trička, která odvádí pot. V horách se vrství. Pro základ použijte <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/nepromokave-bundy/">nepromokavé bundy</a>. Lezení v chladu vyžaduje i <a href="/sportovni-rukavice/">rukavice</a> a <a href="/cepice-a-celenky/">čepici</a>. K nošení výbavy poslouží <a href="/batohy/">batoh</a> s dostatečně pevnými popruhy.</p>'
          '<h2>Péče a životnost výbavy</h2>'
          '<ul><li>Lano chraňte před slunečním zářením, chemikáliemi a ostrými hranami a skladujte ho v obalu.</li>'
          '<li>Karabiny a expresky myjte vlažnou vodou a nechte je uschnout, případně použijte doporučený lubrikant.</li>'
          '<li>Sedák a smyčky perte jen podle návodu a nevystavujte je rozpouštědlům.</li>'
          '<li>Textilní prvky mají omezenou životnost i bez používání, proto kontrolujte datum výroby a pokyny výrobce.</li>'
          '<li>Výbavu, která utrpěla větší pád nebo zátěž, vyřaďte, nebo ji nechte posoudit odborníkem.</li></ul>'
          '<p>Na péči o obuv se podívejte i do kategorie <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
          '<h2>Základní bezpečnostní zásady</h2>'
          '<p>Žádná výbava nenahradí znalosti. Před prvním samostatným lezením absolvujte kurz u zkušeného instruktora a osvojte si zavazování do lana, kontrolu partnera a komunikaci při jištění. Před každým začátkem cesty zkontrolujte uzly, přezky sedáku a zamčení karabin. Při lezení venku sledujte počasí a vždy sdělte blízkým, kam jdete a kdy se vrátíte. Zkušenost s výbavou se nepřenáší jen čtením, takže trénujte pod dohledem.</p>'
          '<h2>Půjčovny a kurzy</h2>'
          '<p>Pokud si nejste jisti, zda vás lezení bude bavit, začněte v půjčovně na stěně nebo na kurzu, kde obvykle vybavení zapůjčí. Teprve po několika návštěvách se vyplatí pořídit vlastní lezečky a sedák, které sednou na míru a jsou hygieničtější než půjčené. Lano a pomůcky na jištění pořizujte až poté, co víte, jak je budete používat.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce kategorie jsou například ' + B(('simond', 'Simond'), ('ocun', 'Ocún'), ('black-diamond', 'Black Diamond'), ('beal', 'Beal'), ('la-sportiva', 'La Sportiva'), ('hms', 'HMS'), ('petzl', 'Petzl'), ('singing-rock', 'Singing Rock'), ('camp', 'Camp'), ('edelrid', 'Edelrid'), ('scarpa', 'Scarpa'), ('edelweiss', 'Edelweiss')) + '. Každá značka se zaměřuje na jiné části výbavy, takže se vyplatí porovnávat konkrétní modely.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Kupovat výbavu bez kurzu a bez zkušeného parťáka.</li>'
          '<li>Příliš těsné lezečky už na začátku, které brání dlouhému tréninku.</li>'
          '<li>Použít sedák nebo smyčku starší, než doporučuje výrobce.</li>'
          '<li>Kombinovat díly, které nejsou určené pro společné použití.</li>'
          '<li>Podcenit přilbu u skal a při ferratách.</li>'
          '<li>Skladovat lano zmuchlané v autě na slunci.</li></ul>'
          '<h2>Pro koho je co</h2>'
          '<p>Začátečník na stěně většinou potřebuje jen lezečky, sedák a magnezium, zbytek si půjčí. Skalní lezec přidá lano, expresky, přilbu a jistítko. Horolezec do vyšších hor doplní výbavu na sníh a led, což už vyžaduje přípravu a kurz. Rodiny s dětmi se mohou věnovat ferratám nebo lanovým parkům s odpovídající výbavou. Pokud se chcete jen pohybovat v terénu, může stačit <a href="/trekove-hole/">trekové hole</a> a pevná obuv.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Vyberte podkategorii a zúžte podle použití a značky. U každého kusu vidíte nabídky obchodů, takže poznáte, kde je skladem vaše velikost. Při nákupu bezpečnostní výbavy čtěte popisy, certifikace a návod. Nejste-li si jisti, poraďte se s instruktorem nebo horolezeckým oddílem.</p>',
    faq=[('Co potřebuji na první lezení na stěně?', 'Většinou stačí lezečky, sedák a magnezium s pytlíkem. Stěna často půjčuje lano a jistítko, ale ptejte se provozovatele. První návštěvu doporučujeme s instruktorem.'),
         ('Jak vybrat správné lezečky?', 'Vyberte střih podle zkušeností. Začátečníkům se hodí plochý a pohodlnější tvar. Bota má dobře držet, ale nemá bolet. Zkoušejte odpoledne a obě nohy, protože se mohou lišit.'),
         ('Jaký je rozdíl mezi dynamickým a statickým lanem?', 'Dynamické lano se při pádu natáhne a pohlcuje energii. Statické se téměř neprotahuje a používá se na slaňování, výstup po laně a záchranu. Při jištění lezce potřebujete dynamické.'),
         ('Jak často měnit lano a sedák?', 'Podle pokynů výrobce, intenzity používání a stavu materiálu. Textilní výbava stárne i bez použití. Poškození, zatuhnutí nebo ztráta pružnosti jsou důvod k vyřazení.'),
         ('Co je to via ferrata?', 'Jištěná cesta s ocelovým lanem a stupy, často kombinovaná s žebříky a mosty. Jistíte se ferratovým setem s tlumičem pádu. Cesty mají různou obtížnost, proto čtěte popis.'),
         ('Je ferratový set nutný?', 'Ano, nejde o místo pro improvizaci. Set s tlumičem energie se při pádu rozvine a zmírní zátěž. Obyčejná smyčka nebo lano ho nenahradí.'),
         ('Mohu na lezení použít cyklistickou helmu?', 'Nedoporučuje se. Lezecké přilby jsou navržené na nárazy shora a mají jinou konstrukci. Používejte přilbu určenou pro horolezectví.'),
         ('Jaké karabiny koupit na začátek?', 'Záleží na použití. Pro sportovní lezení se používají expresky se dvěma karabinami, pro jištění zajišťovací karabiny s pojistkou. Poraďte se s instruktorem a přečtěte si označení nosnosti.'),
         ('Jak pečovat o lezečky?', 'Po lezení je vyvětrejte, nenechávejte je na slunci a v horku. Čistěte podrážku suchým hadříkem a vyhněte se kontaktu s nečistotami před lezením. Obuv se dá předat do opravy podrážky.'),
         ('Jaké oblečení se hodí na lezení?', 'Pohodlné pohyblivé kalhoty a prodyšné tričko. Na skalách přidejte vrstvu proti větru a rukavice, v horách vrstvení podle počasí.'),
         ('Kde najdu další outdoor výbavu?', 'V kategoriích outdoor, outdoor doplňky, turistické batohy, trekové boty a trekové hole. K bezpečí patří také první pomoc.')],
)
