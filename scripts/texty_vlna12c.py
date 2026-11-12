"""sporteka.cz — wave 12c (4. 11. 2026): long texts for bezecka-obuv, sportovni-kalhoty, trailove-boty, zimni-sporty. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bezecka-obuv
NEW['bezecka-obuv'] = dict(long=True,
    title='Běžecké boty: silniční, trailové i závodní | Sporteka',
    desc='Běžecké boty pro silnici, trail i závody. Poradíme s odpružením, dropem, velikostí a výměnou a porovnáme nabídku českých obchodů.',
    intro='<p><strong>Běžecké boty</strong> jsou jediný kus výbavy, na kterém opravdu záleží od prvního kilometru. Špatně zvolený pár se projeví puchýři, bolavými lýtky nebo kolenem, zatímco dobře sedící bota se při běhu skoro neozývá. Výběr přitom nestojí na značce, ale na kombinaci povrchu, tréninkového plánu, vaší váhy a tvaru chodidla.</p>'
          '<p>Na Sportece najdete celou nabídku v jedné kategorii a dvě větve: <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> na asfalt a zpevněné cesty a <a href="/trailove-boty/">trailové boty</a> do lesa a hor. Průvodce níže vysvětluje, jak boty rozlišit, jak poznat správnou velikost, kdy dává smysl druhý pár a jak často běžecké boty měnit. Doplňuje ho přehled doplňků, které k běhu patří, od ponožek po hodinky.</p>',
    guide='<h2>Jak se v běžeckých botách vyznat</h2>'
          '<p>Běžecká bota je kompromis mezi třemi vlastnostmi: tlumením, stabilitou a hmotností. Měkká a vysoká bota působí pohodlněji, ale je těžší a méně živá. Lehká závodní bota je rychlá, ale odpouští méně chyb. Nejlepší pár proto není ten nejlehčí ani nejměkčí, nýbrž ten, který odpovídá vaší typické tréninkové jednotce.</p>'
          '<h3>Typy běžecké obuvi</h3>'
          + T(['Typ boty', 'Čím se vyznačuje', 'Pro koho'], [
              ['Tréninková neutrální', 'střední až měkké tlumení, pohodlná špička, odolná podrážka', 'většina rekreačních běžců a každodenní kilometry'],
              ['Stabilní (podporující)', 'pevnější vnitřní strana mezipodešve, širší stopa', 'běžci, kterým se kotník při došlapu výrazně propadá dovnitř'],
              ['Závodní a tempová', 'nízká hmotnost, pružná pěna, často vložená deska', 'rychlé tréninky a soutěže'],
              ['Maximálně tlumená', 'vysoká pěnová mezipodešev, široká základna', 'dlouhé pomalé běhy, těžší běžci, regenerace'],
              ['Minimalistická a barefoot', 'tenká podešev, široká špička, nízký nebo nulový drop', 'zkušení běžci, kteří chtějí trénovat techniku postupně'],
              ['Trailová', 'hrubý vzorek, ochrana špičky, tužší konstrukce', 'lesy, kopce, kamenité cesty a bahno']]) +
          '<p>Kdo si není jistý, začne neutrální tréninkovou botou. Je to nejuniverzálnější volba a podle ní se dobře pozná, jestli vám něco chybí. Stabilní model zkoušejte až ve chvíli, kdy po běhu opakovaně bolí vnitřní strana kolena nebo holeň.</p>'
          '<h3>Silnice, nebo terén</h3>'
          '<p>Hlavní rozcestí vede mezi asfaltem a lesem. Na tvrdém povrchu je důležité tlumení a hladká, odolná guma, v terénu přilnavost a ochrana chodidla. Na přehledné stránce <a href="/silnicni-bezecke-boty/">silničních běžeckých bot</a> proto uvidíte modely s plynulým odvalem, zatímco v <a href="/trailove-boty/">trailových botách</a> najdete zubatější podrážky a zesílenou špičku. Pokud běháte stejně často po parku i po cestě v lese, vybírejte hybridní model s mělkým vzorkem. Čistě silniční bota na mokrém kořeni klouže a čistě trailová se na chodníku rychle sjíždí.</p>'
          '<h2>Parametry, které rozhodují</h2>'
          '<h3>Drop, tlumení a hmotnost</h3>'
          '<p>Drop je výškový rozdíl mezi patou a špičkou. Vyšší drop odlehčuje lýtka a Achillovu šlachu, nižší nutí chodidlo pracovat víc. Přechod mezi extrémy dělejte postupně a první týdny běhejte jen krátké úseky. Tlumení určuje druh a množství pěny v mezipodešvi. Moderní lehké pěny jsou pružné a oproti starším typům ztrácejí tvar pomaleji, ale bývají méně stabilní, takže na nerovném povrchu nebo při větší hmotnosti běžce může být lepší pevnější pěna. Hmotnost hraje roli hlavně u závodní obuvi, při běžném tréninku je důležitější komfort.</p>'
          '<h3>Svršek, jazyk a zadní část</h3>'
          '<p>Většina běžeckých bot má svršek z lehké sítoviny, která odvádí teplo a rychle schne. Dobře sedí, když se nesmotá v jazyku a nevytváří tlakové body nad nártem. Zadní část by měla držet patu bez trhání kůže na Achillovce. U bot do chladna se můžete setkat s hustší pleteninou nebo membránou, ale v letních měsících stačí prodyšný svršek. Šněrování se dá přizpůsobit: u širšího nártu vynechejte jedno očko, při klouzání paty použijte další oko pro tzv. běžeckou smyčku.</p>'
          '<h3>Pronace a stabilita</h3>'
          '<p>Pronace popisuje, jak se noha po došlapu naklání dovnitř. Mírná pronace je přirozená a většinu běžců nijak neomezuje. Pomoc stabilnější boty má smysl, když si všimnete výrazně sešlapané vnitřní hrany podrážky nebo vás bolí kolena. Rozbor došlapu na pásu nabízejí specializované běžecké obchody a ušetří spoustu zkoušení naslepo.</p>'
          '<h2>Velikost a zkoušení</h2>'
          '<p>Běžecká bota je záměrně o něco větší než běžná obuv. Před špičkou by měl zůstat prostor zhruba na šířku palce, protože při běhu noha mírně klouže dopředu a po půl hodině otéká. Šířka je stejně důležitá jako délka: pokud je špička úzká, tlačí malíček a roste riziko puchýře. U některých značek existují široké verze, jiné mají prostornou špičku už v základním provedení.</p>'
          '<ul><li>Zkoušejte odpoledne nebo večer, kdy je noha největší.</li>'
          '<li>Obujte si ponožky, v nichž budete běhat, ne tenké ponožky z obchodu.</li>'
          '<li>Zkuste zašněrovat boty pevně a udělat několik drobných kroků i seběhnout schody.</li>'
          '<li>Pata nesmí vyklouzávat, ale ani tlačit na kost.</li>'
          '<li>Při nákupu na internetu si ověřte vratnou lhůtu a vyzkoušejte boty doma na čistém koberci.</li></ul>'
          '<p>Velikostní tabulky se mezi značkami liší, proto neodvozujte číslo jen od svého posledního páru. Změřte chodidlo a porovnejte údaj v centimetrech s tabulkou výrobce. Pro děti platí stejná pravidla, jen s kratším intervalem výměny, protože nohy rostou.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete zástupce všech cenových úrovní. Tradiční specialisté na silnici jsou ' + B(('asics', 'Asics'), ('mizuno', 'Mizuno'), ('brooks', 'Brooks'), ('saucony', 'Saucony'), ('hoka', 'Hoka'), ('on', 'On')) + '. Velcí sportovní výrobci jako ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('new-balance', 'New Balance'), ('puma', 'Puma')) + ' nabízejí široký rozsah od základních po závodní modely. Do terénu míří spíš ' + B(('salomon', 'Salomon'), ('la-sportiva', 'La Sportiva'), ('inov-8', 'Inov 8'), ('dynafit', 'Dynafit'), ('altra', 'Altra')) + '. Zkušenost s jednou značkou nemusí platit pro další, protože střih a tvar kopyta se liší, takže je lepší sledovat konkrétní model než logo.</p>'
          '<h2>Střídání, životnost a péče</h2>'
          '<h3>Kdy boty vyměnit</h3>'
          '<p>Životnost běžecké boty se počítá v kilometrech, ale vyčíst ji z ní nejde přesně. Závisí na vaší hmotnosti, povrchu a stylu běhu. Za vyřazení hovoří zploštělá nebo ztvrdlá mezipodešev, asymetricky sjetá podrážka a nová bolest, která se dřív neozývala. Podešev si občas prohlédněte zespodu a zkuste boty ohnout rukou: pokud se nepoddají tam, kde dřív pružily, nebo jsou naopak ochablé, je čas na nový pár.</p>'
          '<p>Střídání dvou párů dává pěně čas se vrátit do tvaru a snižuje jednostranné přetížení. Rozumná kombinace je tréninková bota na běžné kilometry a rychlejší lehčí model na intervaly. Kdo běhá terénem, přidá <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<h3>Čištění a sušení</h3>'
          '<p>Z bot vyjměte vložky a nechte je zvlášť oschnout při pokojové teplotě. Mokré boty vycpejte novinovým papírem, který nasaje vlhkost. Nikdy je nedávejte na topení, do sušičky ani na slunce, protože se lepidlo a pěna deformují. Blátivé boty opláchněte vlažnou vodou a kartáčem, pračka a vyšší teplota jim nesvědčí.</p>'
          '<h2>Co k běhu patří vedle bot</h2>'
          '<p>Správná obuv funguje nejlépe ve spojení s dalšími kusy. <a href="/sportovni-ponozky/">Sportovní ponožky</a> bez švů a z funkčního materiálu omezují otlaky, <a href="/leginy/">legíny</a> a <a href="/sportovni-kratasy/">kraťasy</a> nezpůsobují odření a <a href="/funkcni-tricka/">funkční trička</a> odvádějí pot. Na delší tratě se hodí <a href="/bezecke-vesty-a-batohy/">běžecká vesta</a> nebo <a href="/bezecke-opasky/">běžecký opasek</a> na klíče, telefon a gely. Tréninkový plán a čas měří <a href="/sportovni-hodinky/">sportovní hodinky</a>. Celkový přehled najdete v kategorii <a href="/beh/">běh</a>.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li><strong>Moc malá velikost:</strong> prsty narážejí do špičky při sbíhání a nehty černají.</li>'
          '<li><strong>Výběr podle vzhledu:</strong> pěkná bota může mít úplně jiný tvar kopyta než ten váš.</li>'
          '<li><strong>Jeden pár na všechno:</strong> asfalt, trail i rychlý trénink spolu nejdou dobře.</li>'
          '<li><strong>Prudká změna dropu:</strong> lýtka a Achillovka potřebují čas na přizpůsobení.</li>'
          '<li><strong>Ignorování bolesti:</strong> nová bolest po výměně obuvi je signál, ne cena za zlepšení.</li></ul>'
          '<h3>Pro koho jaká bota</h3>'
          '<p>Začátečník dostane největší užitek z měkčí neutrální boty se širší špičkou. Pokročilý běžec ocení lehčí pár na tempo a druhý na objem. Těžší běžec by měl hledat větší tlumení a odolnější podrážku. Žena s úzkým kotníkem může využít dámský střih, který má užší patu a mírně jiný tvar nártu. U dětí upřednostněte pevnou a ohebnou botu s dostatečným prostorem pro růst, ne extrémní odpružení. Na Sportece porovnáte nabídky českých obchodů a podle skladových velikostí zjistíte, kde si můžete boty ještě vyzkoušet.</p>',
    faq=[
        ('Jak poznám správnou velikost běžeckých bot?', 'Změřte si chodidlo odpoledne a počítejte s rezervou zhruba šířky palce před špičkou. Pata musí držet bez vyklouzávání a špička nesmí tlačit do stran. Číslo na jedné značce se nemusí shodovat s jinou, proto se řiďte tabulkou výrobce v centimetrech.'),
        ('Mohu běhat v obyčejných teniskách?', 'Pro občasný lehký pohyb ano, ale na pravidelný běh jsou vhodnější běžecké boty. Mají odpružení, stabilnější konstrukci a lehčí svršek, které zvyšují komfort při opakovaném došlapu. Módní tenisky tlumí méně a rychleji se unaví.'),
        ('Co je drop a jaký zvolit?', 'Drop je rozdíl výšky paty a špičky. Vyšší drop zatěžuje méně lýtka a Achillovu šlachu, nižší nutí chodidlo víc pracovat. Pokud jste zvyklí na určitou hodnotu, měňte ji postupně a nové boty zpočátku používejte jen na kratší běhy.'),
        ('Jak často mám běžecké boty měnit?', 'Nejde o pevný počet kilometrů. Sledujte zploštělou mezipodešev, nerovnoměrně sjetou podrážku a bolest, která dřív nebyla. Lehčí běžec na hladkém povrchu vydrží s botami déle než těžší běžec v terénu.'),
        ('Je lepší měkká, nebo tvrdší bota?', 'Měkká bota se hodí na dlouhé pomalé běhy a pro těžší běžce, tvrdší a pružnější na rychlejší tempa. Univerzální řešení neexistuje, proto mnoho běžců střídá dva páry s odlišným chováním.'),
        ('Potřebuji stabilní boty, když se mi propadá kotník?', 'Mírná pronace je normální a většina běžců s ní vyjde bez potíží. Stabilní model zkuste, když vás opakovaně bolí kolena nebo holeně, případně když je vnitřní strana podrážky výrazně sešlapaná. Pomůže i rozbor došlapu v specializovaném obchodě.'),
        ('Čím se liší silniční a trailové boty?', 'Silniční mají hladší podrážku a více tlumení, trailové hrubší vzorek, pevnější špičku a lepší přilnavost. Na asfaltu se trailová guma rychleji sjíždí a boty působí tvrději, v bahně naopak silniční bota klouže.'),
        ('Jak běžecké boty správně vyprat a usušit?', 'Preferujte ruční čištění vlažnou vodou a kartáčem. Vložky vyndejte, boty vycpěte papírem a sušte při pokojové teplotě. Pračka, topení a přímé slunce poškozují lepené spoje i pěnu v mezipodešvi.'),
        ('Je dobré mít dva páry najednou?', 'Ano, pokud běháte víckrát týdně. Pěna se mezi tréninky vrací do tvaru a každý pár zatěžuje nohu trochu jinak, což snižuje riziko přetížení. Druhý pár může být lehčí na rychlejší tréninky nebo trailový na terén.'),
        ('Jak vybrat boty pro dítě?', 'Dětská bota má být pevná, ohebná a o něco prostornější, aby noha mohla růst. Extrémní tlumení nepotřebuje. Velikost kontrolujte pravidelně a vezměte v úvahu, že děti vyrostou rychleji než dospělí vyřadí boty.')])

# ------------------------------------------------------------------ trailove-boty
NEW['trailove-boty'] = dict(long=True,
    title='Trailové běžecké boty: výběr do terénu | Sporteka',
    desc='Trailové běžecké boty do lesa, hor i bahna. Vzorek podrážky, ochrana špičky, membrána a velikost. Porovnejte nabídku českých obchodů.',
    intro='<p><strong>Trailové boty</strong> jsou určené pro běh mimo asfalt: po lesních pěšinách, loukách, kamenitých svazích i horských hřebenech. Pod nohou se střídá hlína, bahno, kořeny, kameny a někdy sníh, takže od obuvi čekáte hlavně přilnavost, ochranu chodidla a stabilitu při sbíhání. Pohodlí na hladké cestě je až druhé v pořadí.</p>'
          '<p>Na Sportece najdete trailové modely vedle <a href="/silnicni-bezecke-boty/">silničních běžeckých bot</a> v rámci kategorie <a href="/bezecka-obuv/">běžecké boty</a>. Níže vysvětlíme, jak číst vzorek podrážky, kdy se hodí membrána, jak volit podle tratě a sezóny, na co dát pozor u velikosti a jak boty chránit. Přidáme i doporučení k výbavě, která s trailem souvisí, od ponožek po běžeckou vestu.</p>',
    guide='<h2>Co dělá trailovou botu trailovou</h2>'
          '<p>Na první pohled se trailová bota liší hrubší podešví, ale rozdíly jdou hlouběji. Svršek bývá odolnější proti otěru, špička je zpevněná gumovým prvkem a mezipodešev je často nižší a stabilnější než u silničních bot, aby noha na nerovném povrchu nelétala. Trail je také specifický tím, že boty nesmí být jen přilnavé, ale musí držet nohu v pevné poloze při bočních výchylkách.</p>'
          '<h3>Vzorek a směs podrážky</h3>'
          + T(['Podmínky', 'Vhodný vzorek', 'Poznámka'], [
              ['Bahno, mokrá tráva, rozbředlý sníh', 'hluboké, daleko od sebe položené hrbolky', 'čistí se samy, na tvrdém povrchu se rychle sjíždějí'],
              ['Suché lesní a polní cesty', 'střední vzorek s kombinací hran', 'nejuniverzálnější volba pro většinu běžců'],
              ['Skála a kameny', 'nižší, hustší vzorek s lepivou směsí', 'důležitá je přilnavost na mokrém kameni'],
              ['Udusané cesty a mix s asfaltem', 'mělký vzorek, spojitější kontakt', 'hodí se i na přesuny mezi trasami'],
              ['Zimní trasy', 'agresivní vzorek, případně ochrana proti sněhu', 'doplnit protiskluzovými návleky']]) +
          '<p>Důležitá je i směs gumy. Měkčí lépe lepí na mokrých kamenech, tvrdší vydrží déle na štěrku a dlouhých přesunech. Výrobci někdy kombinují oboje v různých zónách podrážky.</p>'
          '<h3>Ochrana chodidla a tuhost</h3>'
          '<p>Zpevněná špička chrání prsty před kameny a kořeny. Mezi mezipodešví a podrážkou se někdy skrývá ochranná deska (rock plate), která brání bolesti od ostrých hran. Za cenu menší citlivosti nabízí jistotu při delších trasách. V lehkých botách do měkkého terénu se s ní nesetkáte. Pokud vyrážíte na kamenité hřebeny a nesete batoh, je rozumné vybrat tužší model, na lesní okruhy stačí ohebnější.</p>'
          '<h3>Svršek, jazyk a šněrování</h3>'
          '<p>Trailový svršek musí vydržet otěr o větve i kamení, a přitom propouštět teplo. Husté sítoviny s vrstvou ochranného povlaku odolávají lépe než tenké siloniny. Jazyk připevněný po stranách (tzv. kapsový) brání vnikání drobných kamínků. Pevné šněrování se rychle nestahuje a zadní část s výztuhou drží patu. U sbíhání platí, že pata musí zůstat na místě, jinak se prsty zarážejí do špičky.</p>'
          '<h2>Výběr podle trasy a sezóny</h2>'
          '<p>Ten nejlepší model neexistuje, ale existuje nejlepší model pro konkrétní trasu. Rozhodněte, jestli běháte převážně po lesních cestách, nebo po náročných horských stezkách, a podle toho zvolte vzorek a tuhost.</p>'
          '<h3>Lesní okruhy a přírodní parky</h3>'
          '<p>Pro rekreační běh po zpevněných lesních cestách se hodí lehčí boty se středním vzorkem a mírným tlumením. Dobře se v nich přechází i na krátké úseky asfaltu a nejsou příliš tvrdé.</p>'
          '<h3>Hory, kameny a dlouhé tratě</h3>'
          '<p>Pro horské běhy vybírejte pevnější konstrukci s ochranou špičky, lepivou směsí a stabilním zadním dílem. Při dlouhých trasách ocení běžec víc tlumení i prostornější špičku, protože noha během hodin otéká. Součástí výbavy bývá <a href="/bezecke-vesty-a-batohy/">běžecká vesta</a> s vodou a lehkou bundou, kterou doplní <a href="/bezecke-opasky/">běžecký opasek</a> na drobnosti.</p>'
          '<h3>Zima, sníh a ledové úseky</h3>'
          '<p>Ve sněhu se osvědčují boty s hlubokým vzorkem a těsnějším svrškem. Na tvrdý led samy nestačí a pomohou speciální <a href="/nesmeky/">nesmeky</a> přes podrážku. Zateplené modely a vrstva nepromokavé tkaniny pomáhají udržet teplo, ale také hůř odvádějí vlhkost.</p>'
          '<h2>Membrána, nebo prodyšnost</h2>'
          '<p>Membrána zastaví vodu zvenku, ale zároveň omezuje odvod potu. Jakmile se voda dostane přes okraj boty, uvnitř zůstane a boty schnou dlouho. Na jaře, na podzim a v chladném počasí je rozumná volba, na horké letní dny a trasy s brody se hodí prodyšný model bez membrány, který rychle odvádí vodu i teplo. Pomůže tenká ponožka z merina nebo syntetiky; <a href="/merino-ponozky/">merino ponožky</a> udrží teplo i mokré a nepáchnou tak rychle.</p>'
          '<h2>Velikost a sezení</h2>'
          '<p>V terénu je správná velikost důležitější než v běžné obuvi. Při sbíhání prsty tlačí dopředu, proto počítejte s větší rezervou před špičkou, zvláště na dlouhé tratě. Pata musí sedět pevně, protože případné vyklouzávání způsobuje puchýře a nejistotu na nerovném povrchu. V obchodě zkuste seběhnout schody nebo šikmou plochu a zkontrolujte, že se prsty nedotýkají přední části.</p>'
          '<ul><li>Zkoušejte s ponožkami, které budete na trailu používat.</li>'
          '<li>Počítejte s tím, že na delších trasách noha mírně nateče.</li>'
          '<li>Zkontrolujte šířku v nártu a v přední části, protože úzká špička způsobuje otlaky.</li>'
          '<li>U zimních modelů připočtěte prostor pro silnější ponožku.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Specializace na trail mají ' + B(('salomon', 'Salomon'), ('la-sportiva', 'La Sportiva'), ('inov-8', 'Inov 8'), ('dynafit', 'Dynafit'), ('salewa', 'Salewa')) + '. Do kategorie zasahují také běžecké značky jako ' + B(('hoka', 'Hoka'), ('altra', 'Altra'), ('on', 'On'), ('saucony', 'Saucony'), ('brooks', 'Brooks'), ('asics', 'Asics')) + ', jejichž trailové modely se liší hlavně mírou tlumení a tvarem špičky. Z outdoorové strany se objevují ' + B(('merrell', 'Merrell'), ('columbia', 'Columbia'), ('aku', 'Aku')) + '. Rozdíly jsou v odvalu, šířce kopyta a poměru tlumení, a proto se vyplatí porovnat konkrétní modely, ne jen značky.</p>'
          '<h2>Péče o trailové boty</h2>'
          '<p>Po běhu boty vyklepejte, vyndejte vložky a z podrážky odstraňte kameny i hlínu. Bláto nechte zaschnout a pak ho setřete kartáčem, protože mokré bláto roztírá zbytečně. Svršek omyjte vlažnou vodou, sušte při pokojové teplotě s vycpáním z papíru. Topení, kamna a prudké slunce poškozují lepení i membránu. Impregnace svršku se hodí u bot bez membrány, jinde může zhoršit prodyšnost. Pokud běháte víckrát týdně, střídejte dva páry.</p>'
          '<h3>Související výbava a prolinkování</h3>'
          '<p>Trail vyžaduje i další vybavení. <a href="/trekove-hole/">Trekové hole</a> pomohou na dlouhých stoupáních, <a href="/celovky-a-svitilny/">čelovky</a> na zimní a večerní tratě a <a href="/sportovni-hodinky/">sportovní hodinky</a> s navigací na neznámé stezky. Pro chladnější dny se hodí <a href="/vetrovky/">větrovky</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a> bez švů. Pro spojení s chůzí přejděte do kategorie <a href="/trekova-obuv/">trekové obuvi</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li><strong>Boty bez rezervy:</strong> sbíhání ze stráně stlačí prsty ke špičce.</li>'
          '<li><strong>Membrána do léta:</strong> noha se potí a boty po brodu schnou hodiny.</li>'
          '<li><strong>Trailovka na asfalt:</strong> rychle se sjíždí a běh je tvrdší.</li>'
          '<li><strong>Zanedbané šněrování:</strong> uvolněná pata způsobí puchýře a nejistotu.</li>'
          '<li><strong>Přeceňování ochrany:</strong> příliš tuhá bota v lehkém terénu zbytečně omezuje cit.</li></ul>'
          '<p>Na Sportece porovnáte trailové boty z českých obchodů a podle skladových velikostí poznáte, kde je seženete. Před koupí si ujasněte typ tratě, počasí a vzdálenost a podle toho zúžte filtry.</p>',
    faq=[
        ('Můžu trailové boty používat na silnici?', 'Ano, ale jen občas. Trailová podrážka je hrubší a na tvrdém povrchu se rychleji sjíždí a působí tužším dojmem. Pro pravidelný běh po asfaltu je pohodlnější silniční model.'),
        ('Jak hluboký vzorek podrážky zvolit?', 'Do bahna a mokré trávy se hodí hluboké hrbolky, na běžné lesní cesty střední vzorek. Na kamenité a suché trasy stačí nižší a hustší vzorek s lepivou směsí. Nejuniverzálnější je střední hloubka.'),
        ('Potřebuji trailové boty s membránou?', 'Membrána se hodí na chladnější a deštivé dny. V létě a při častých brodech je lepší prodyšný model, který rychle schne. Pokud se voda dostane přes okraj, membrána ji uvnitř zadrží.'),
        ('Má trailová bota mít větší velikost než silniční?', 'Často ano, aspoň o půl čísla navíc nebo větší prostor před špičkou. Při sbíhání noha klouže dopředu a na dlouhých tratích otéká. Pata ale musí zůstat pevně usazená.'),
        ('Co je ochranná deska v podrážce?', 'Je to tenká vrstva mezi mezipodešví a podrážkou, která brání tlaku od ostrých kamenů. Zvyšuje jistotu na tvrdém terénu, ale mírně snižuje cit a ohebnost. Na lehčí trasy ji nepotřebujete.'),
        ('Jak vyčistit blátivé boty?', 'Nechte bláto zaschnout, setřete ho kartáčem a svršek omyjte vlažnou vodou. Vložky vyndejte a boty sušte při pokojové teplotě. Topení a pračka poškozují lepené spoje.'),
        ('Hodí se trailové boty na zimu?', 'Ve sněhu a blátě ano, hluboký vzorek dobře drží. Na ledu samotné boty nestačí a doplňují se nesmeky. Při mrazu vezměte teplejší ponožky a zvolte těsnější svršek.'),
        ('Jak poznám, že boty sedí na trail?', 'Pata nevyklouzává, prsty se při sbíhání nedotýkají špičky a v nártu nic netlačí. Zkuste v obchodě seběhnout schody nebo šikmou plochu. Dobrý test je také stoupání s uvolněným a zatíženým šněrováním.'),
        ('Jak často trailové boty vyměnit?', 'Podle opotřebení vzorku, ochrany špičky a ztvrdlé mezipodešve. Kamenitý terén opotřebuje boty rychleji než lesní cesty. Pokud noha začne po běhu bolet jinak než dřív, je čas na kontrolu.'),
        ('Lze trailové boty použít na turistiku?', 'Na lehké cesty ano, jsou lehké a prodyšné. Na těžší batoh a nerovné hřebeny je lepší pevnější trekový model s tužším podrážkovým dílem.')])

# ------------------------------------------------------------------ sportovni-kalhoty
NEW['sportovni-kalhoty'] = dict(long=True,
    title='Sportovní kalhoty: tepláky, outdoor, lyže | Sporteka',
    desc='Sportovní kalhoty do přírody, na trénink i na zimu. Materiály, střihy a velikosti. Porovnejte kalhoty z českých obchodů na jednom místě.',
    intro='<p><strong>Sportovní kalhoty</strong> pokrývají širokou škálu od domácích tepláků po lyžařské kalhoty s membránou. Společné mají jediné: mají zvládnout pohyb a počasí, na které jsou určené. Proto se vybírají podle činnosti, ne podle módního střihu, a už vůbec ne jen podle písmene na štítku.</p>'
          '<p>Na Sportece najdete jednotlivé větve pohromadě: <a href="/teplaky/">tepláky</a> na trénink a volný čas, <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> na túry a cestování a <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a> na svah. V textu níže rozebíráme materiály, střihy, velikosti a praktické detaily, které se při nákupu snadno přehlédnou. Také poradíme, jak kalhoty vrstvit a udržovat.</p>',
    guide='<h2>Jak vybírat sportovní kalhoty</h2>'
          '<p>Nejdřív si odpovězte na tři otázky: co v nich budete dělat, v jakém počasí a jak intenzivně se budete hýbat. Kalhoty na pomalou procházku mají jiné nároky než kalhoty na běh nebo celodenní túru. Teprve pak vybírejte materiál, střih a drobnosti jako kapsy.</p>'
          '<h3>Přehled typů</h3>'
          + T(['Typ kalhot', 'Hlavní přednost', 'Typické použití'], [
              ['Tepláky', 'měkkost, pohodlí, volný střih', 'trénink, domov, volný čas'],
              ['Outdoorové kalhoty', 'odolnost, rychlé schnutí, kapsy', 'túry, kempování, cestování'],
              ['Softshellové kalhoty', 'ochrana před větrem a lehkým deštěm, pružnost', 'podzimní a jarní túry, lezení'],
              ['Běžecké a tréninkové kalhoty', 'nízká hmotnost, pružnost, zip na kotníku', 'běh, fitness, týmový sport'],
              ['Lyžařské a snowboardové kalhoty', 'izolace, voděodolnost, sněhová manžeta', 'sjezdovka, freeride, snowpark'],
              ['Legíny a elastické kalhoty', 'přiléhavost, volnost pohybu', 'jóga, fitness, vrstvení pod kalhoty']]) +
          '<p>Hranice mezi jednotlivými typy nejsou ostré. Některé outdoorové kalhoty fungují i na běh po horách a podobně se jako tepláky nosí i elastické modely z funkčních materiálů.</p>'
          '<h3>Materiál a jeho chování</h3>'
          '<p>Polyamid a polyester s příměsí elastanu jsou lehké, pružné a rychle schnou. Bavlna je příjemná na dotek, ale po zpocení nebo promáčení se suší pomalu a ochlazuje. Pro volný čas je v pořádku, na aktivní pohyb v chladu raději volte syntetické nebo směsové materiály. Softshell vrstvou odolá větru, ale není úplně nepromokavý. Membrána vodu zastaví, ale jde na úkor prodyšnosti, proto je vhodná na déšť a mokrý sníh, ne na vysoké tempo.</p>'
          '<p>Gramáž tkaniny určuje, jak odolné a hřejivé kalhoty jsou. Tenké se skládají do batohu a hodí se do tepla, silnější drží teplo, ale hůř se suší. Zesílení na kolenou a v sedu prodlužují životnost a pomáhají u lezení nebo při práci na zahradě.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Základní volbou je střih: rovný je univerzální, zúžený (tapered) lépe vypadá s botami a je praktický při pohybu, volnější pohodlněji obepíná při sezení a nošení vrstev. Zvláštním případem jsou kalhoty s předtvarovanými koleny, které při dřepu a výstupu nestahují.</p>'
          '<ul><li>Velikost nehledejte jen podle písmene, porovnejte obvod pasu a délku nohavice s tabulkou výrobce.</li>'
          '<li>Pokud se nevejdete do jedné velikosti, řiďte se materiálem: u elastických úpletů zvolte spíš menší, u pevných tkanin raději větší.</li>'
          '<li>Dámské střihy mají jiné proporce boků a pasu, nejde jen o barvy.</li>'
          '<li>U dětí počítejte s malou rezervou v délce, ale nekupujte o dvě čísla větší, překážejí při pohybu.</li>'
          '<li>Nastavitelný pas, pásek a pružné lemování pomáhají doladit sedění.</li></ul>'
          '<h2>Praktické detaily, které stojí za pozornost</h2>'
          '<p>Kapsy na zip zabrání ztrátě klíčů a telefonu při pohybu. Odepínací nohavice přeměňují dlouhé kalhoty na kraťasy a šetří místo v batohu. Zip na kotníku usnadňuje přezutí bot a větrání, elastické manžety drží kalhoty na místě v botě. Reflexní prvky ocení běžci za šera. Větrací zipy na stehnech pomáhají u svahu a při výstupech. UV filtr v tkanině je užitečný v horách a při dlouhém pobytu na slunci.</p>'
          '<h3>Zimní kalhoty a sněhová manžeta</h3>'
          '<p>Lyžařské kalhoty mají sněhovou manžetu, která brání vniknutí sněhu do bot, zesílení na vnitřní straně nohavic proti ostřím lyží a izolaci podle teploty. Podrobné rady najdete v rozcestníku <a href="/zimni-sporty/">zimních sportů</a> a v kategorii <a href="/lyzarske-obleceni/">lyžařského a snowboardového oblečení</a>. Pod kalhoty patří <a href="/lyzarske-termopradlo/">termoprádlo</a> nebo <a href="/termopradlo/">funkční prádlo</a>, které odvádí pot od těla.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Outdoorová a horská stránka je zastoupena značkami ' + B(('fjallraven', 'Fjällräven'), ('haglofs', 'Haglöfs'), ('regatta', 'Regatta'), ('kilpi', 'Kilpi'), ('husky', 'Husky'), ('hannah', 'Hannah'), ('viking', 'Viking'), ('trespass', 'Trespass')) + '. Sportovní a tréninkové kalhoty nabízejí ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('champion', 'Champion'), ('4f', '4F')) + '. Zimní modely najdete například u značky ' + B(('rossignol', 'Rossignol')) + '. Každý výrobce má jiný střih, proto před nákupem porovnejte rozměry, ne jen označení velikosti.</p>'
          '<h2>Vrstvení a doplnění outfitu</h2>'
          '<p>Kalhoty jsou součástí systému vrstev. V chladu můžete pod ně obléknout <a href="/leginy/">legíny</a> nebo termoprádlo, na jaře a na podzim se uplatní lehčí kalhoty s větrovkou nebo <a href="/softshellove-bundy/">softshellovou bundou</a>. Na túru vybírejte i vhodné <a href="/trekova-obuv/">trekové boty</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>, aby kalhoty netřely o kotník. Pro horké dny zvažte <a href="/sportovni-kratasy/">sportovní kraťasy</a> nebo <a href="/outdoorove-kalhoty/">odepínací outdoorové kalhoty</a>. Širší výběr oblečení je v <a href="/sportovni-obleceni/">sportovním oblečení</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Většinu kalhot perte na 30 až 40 °C, bez aviváže a s menším množstvím prášku. Aviváž zanáší vlákna, zhoršuje savost funkčních materiálů a ruší vodoodpudivou úpravu. Zapněte zipy, aby se nezachytily. Kalhoty s membránou perte speciálním prostředkem a po vyprání občas krátce prohřejte v sušičce na nízký stupeň, pokud to štítek povoluje. Impregnaci je třeba obnovovat, jakmile voda přestane ze svrchní vrstvy odtékat v kapkách. Při skladování nechte kalhoty větrat a nesušte je na topení.</p>'
          '<h3>Jak kalhoty otestovat před koupí</h3>'
          '<p>Zkuste dřep, hluboký výpad a zvednutí kolena k hrudi. Kalhoty by se neměly stahovat v rozkroku ani v pase, nohavice by neměly vyjíždět nad kotník. Zkontrolujte, zda kapsy nepřekážejí a zda se zipy dobře ovládají. Pokud kupujete přes internet, využijte možnost vrácení a vyzkoušejte kalhoty doma s botami, které s nimi budete nosit.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li><strong>Bavlna na aktivní pohyb:</strong> po zpocení se hůř suší a ochlazuje.</li>'
          '<li><strong>Příliš těsná velikost:</strong> pohyb omezuje a namáhá švy.</li>'
          '<li><strong>Membrána na každý den:</strong> v teple se pod ní pot hromadí.</li>'
          '<li><strong>Zapomenutá impregnace:</strong> tkanina nasákne a kalhoty ztratí výhodu.</li>'
          '<li><strong>Ignorování délky:</strong> příliš dlouhé nohavice se otírají o boty a rozpadají.</li></ul>'
          '<p>Na Sportece porovnáte kalhoty z českých obchodů podle pohlaví, značky a skladových velikostí a vybere si jak ten, kdo hledá obyčejné tepláky, tak ten, kdo chystá výbavu na horskou túru nebo zimní svah.</p>',
    faq=[
        ('Jaké kalhoty zvolit na turistiku?', 'Lehké outdoorové kalhoty z rychleschnoucího materiálu s elastanem, ideálně s kapsami na zip a zesílením v kolenou. V chladu se hodí softshell, na deštivé výlety kalhoty s membránou nebo vodoodpudivou úpravou.'),
        ('Mohu používat tepláky na sport?', 'Na lehký trénink a volný čas ano. Na intenzivní pohyb nebo chlad jsou lepší funkční tréninkové či outdoorové kalhoty, které odvádějí pot a rychleji schnou. Bavlněné tepláky nasáknou a ochlazují.'),
        ('Jak poznat, že lyžařské kalhoty jsou dostatečně teplé?', 'Podívejte se na izolaci a na to, zda lze pod ně obléknout termoprádlo. Důležitá je i sněhová manžeta a voděodolnost. Vlastní pocit se liší, takže při chladnějším počasí vrstvěte pod kalhoty.'),
        ('Co znamená softshell u kalhot?', 'Jde o pružnou tkaninu, která odolává větru a lehkému dešti, ale není zcela vodotěsná. Je prodyšnější než membrána a dobře se pohybuje, proto se hodí na jarní a podzimní túry.'),
        ('Podle čeho určit správnou velikost?', 'Měřte obvod pasu, boků a délku vnitřní strany nohy, a pak porovnejte s tabulkou výrobce. Označení S, M, L bývá mezi značkami proměnlivé. Při váhání se řiďte materiálem: u elastických úpletů zvolte spíš menší, u pevných tkanin raději větší.'),
        ('Jak prát kalhoty s membránou?', 'Použijte speciální prací prostředek, jemný cyklus a nižší teplotu bez aviváže. Následně můžete impregnaci obnovit sprejem nebo přídavkem do pračky. Aviváž ničí funkci membrány.'),
        ('Hodí se kalhoty s odepínacími nohavicemi?', 'Ano, na túry a cesty s proměnlivým počasím. Ušetří místo v batohu a umožní rychlou změnu mezi dlouhými kalhotami a kraťasy. Švy a zipy bývají mírně citlivější, proto je ošetřujte.'),
        ('Čím se liší pánské a dámské střihy?', 'Dámské kalhoty mají užší pas, širší boky a jiné proporce nohavic. Pánské bývají rovnější a s delším rozkrokem. Použití opačného střihu nemusí fungovat ani při správném čísle.'),
        ('Je lepší tkanina s elastanem?', 'Pro pohyb ano. Elastan zlepšuje volnost při dřepech, výpadech i lezení a omezuje tlak na švy. U pracovních nebo velmi odolných kalhot může být podíl menší, aby se zachovala trvanlivost.'),
        ('Jak dlouho vydrží impregnace?', 'Závisí na používání a praní. Jakmile voda přestane tvořit kapky a vsakuje se do tkaniny, je čas impregnaci obnovit speciálním přípravkem. Kalhoty tak znovu odpuzují vodu a lépe dýchají.')])

# ------------------------------------------------------------------ zimni-sporty
NEW['zimni-sporty'] = dict(long=True,
    title='Zimní sporty: lyže, snowboard, oblečení | Sporteka',
    desc='Vybavení na zimní sporty: lyže, snowboardy, boty, helmy, brýle a oblečení. Poradíme s výběrem a porovnáme nabídku českých obchodů.',
    intro='<p><strong>Zimní sporty</strong> stojí a padají na výbavě, která zvládne mráz, vlhko i pády. Sjezdovka, běžecká stopa a skialpový výstup mají odlišné nároky na obuv, oblečení i bezpečnost, a proto se vyplatí nejdřív rozhodnout, čemu se budete věnovat. Teprve pak se hodí vybírat konkrétní lyže, boty nebo bundu.</p>'
          '<p>Na Sportece najdete <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/snowboarding/">snowboarding</a>, <a href="/bezecke-lyzovani/">běžecké lyžování</a>, <a href="/skialpinismus/">skialpinismus</a>, <a href="/lyzarske-obleceni/">lyžařské oblečení</a> i drobné doplňky z českých obchodů. Průvodce níže projde výbavu pro jednotlivé sporty, pomůže s velikostmi a vrstvením a upozorní na chyby, které při nákupu vznikají nejčastěji.</p>',
    guide='<h2>Jak se vybavit na zimní sezónu</h2>'
          '<p>Zimní výbava je drahá hlavně tehdy, když se kupuje bez plánu. Pomáhá pořadí: nejdřív boty, helma a oblečení, potom doplňky a až nakonec lyže nebo snowboard. Prkna a lyže si můžete na začátku půjčit, ale boty vás drží dlouhé hodiny, a proto je dobré mít vlastní.</p>'
          '<h3>Co kam patří</h3>'
          + T(['Sport', 'Základní výbava', 'Kde hledat'], [
              ['Sjezdové lyžování', 'lyže s vázáním, boty, hole, helma, brýle', '<a href="/sjezdove-lyze/">lyže</a>, <a href="/lyzarske-boty/">boty</a>, <a href="/lyzarske-hole/">hole</a>'],
              ['Snowboarding', 'prkno s vázáním, boty, helma, brýle, chrániče', '<a href="/snowboardy/">snowboardy</a>, <a href="/snowboardove-boty/">boty</a>, <a href="/snowboardova-vazani/">vázání</a>'],
              ['Běžecké lyžování', 'lyže, boty, vázání, hole, vosky', '<a href="/bezecke-lyze/">lyže</a>, <a href="/bezecke-boty/">boty</a>, <a href="/lyzarske-vosky/">vosky</a>'],
              ['Skialpinismus', 'lehké lyže, pásy, boty s režimem chůze, lavinová výbava', '<a href="/skialpove-lyze/">lyže</a>, <a href="/skialpove-pasy/">pásy</a>, <a href="/skialpove-boty/">boty</a>'],
              ['Sněžnice a procházky', 'sněžnice, hole, teplá obuv', '<a href="/snezky/">sněžnice</a>, <a href="/zimni-obuv/">zimní obuv</a>'],
              ['Bruslení a sáňkování', 'brusle nebo sáně, helma, rukavice', '<a href="/brusle/">brusle</a>, <a href="/sane-a-boby/">sáně a boby</a>']]) +
          '<p>Rozhodnutí o druhu sportu určuje všechno ostatní. Kdo chce jen jezdit na sjezdovce několik dní v roce, vystačí s půjčenými lyžemi a vlastní helmou. Kdo míří na dlouhé běžecké trasy nebo do kopců, potřebuje specifickou obuv i vázání.</p>'
          '<h2>Lyže a snowboard</h2>'
          '<h3>Délka, rádius a určení</h3>'
          '<p>Sjezdové lyže se vybírají podle úrovně, váhy a oblíbeného terénu. Kratší a užší lyže se snáz zatáčejí a odpouštějí chyby, delší a širší jsou stabilnější při vysoké rychlosti a v hlubším sněhu. Rádius udává, jak ostře lyže zatáčejí. Pro začátečníky jsou lepší měkčí lyže s tolerantním charakterem, závodní modely se hodí zkušeným lyžařům. Důležité je i vázání, které musí odpovídat botám a nastavení by měl provést servis. Čtěte více v kategoriích <a href="/lyze-komplety/">lyžařské komplety</a> a <a href="/detske-lyze/">dětské lyže</a>.</p>'
          '<p>Snowboardy se dělí na univerzální, freestylové a freerideové. Univerzální prkno je nejlepším základem a lze na něm zvládnout sjezdovku i park. U vázání dbejte na vhodnou velikost k botám, protože špatně sedící vázání způsobuje únavu a ztrátu kontroly. Pro začátek zvažte i <a href="/snowboardove-sety/">snowboardové sety</a>, které mají sladěné části.</p>'
          '<h3>Hole a údržba</h3>'
          '<p>Správná délka lyžařské hole je taková, aby se při držení za madlo svíral loket zhruba v pravém úhlu, když je hrot u země. Kvalitní madlo s poutkem drží i v rukavici. Skluznici lyží a snowboardu je třeba pravidelně <a href="/lyzarske-vosky/">mazat</a> a hrany brousit. Po sezóně lyže uložte suché a mírně namazané, ať skluznice nevysychá.</p>'
          '<h2>Obuv, helma a brýle</h2>'
          '<p>Boty jsou nejdůležitější součást výbavy. Lyžařská bota přenáší pohyb nohy na lyži, a proto musí sedět pevně, ale bez bolestivých tlaků. Zkoušejte ji s lyžařskou ponožkou a stůjte v mírném předklonu. Ve stoji se prsty dotýkají špičky a v předklonu se od ní lehce odtáhnou, pata přitom drží. Pokud noha vyklouzává, je bota velká, pokud ji brní, je těsná. Najdete je v kategoriích <a href="/lyzarske-boty/">lyžařských bot</a> a <a href="/snowboardove-boty/">snowboardových bot</a>.</p>'
          '<p><a href="/lyzarske-helmy/">Lyžařské helmy</a> chrání při pádu a srážce a jsou dnes samozřejmostí, pro děti často i povinnou. Velikost se určuje podle obvodu hlavy, helma musí sedět pevně bez tlaku a řemínek by se měl dát zapnout bez vůle. <a href="/lyzarske-bryle/">Lyžařské brýle</a> musí dobře těsnit kolem nosu, nezamlžovat se a mít vhodnou kategorii skla podle světla. Na jasné slunce se hodí tmavší, do mlhy a za šera světlejší. Přes brýle s helmou se nemá objevit mezera na čele.</p>'
          '<h2>Vrstvení oblečení</h2>'
          '<p>Zima je o udržení tepla a odvodu potu. Funguje stejný systém vrstev jako v horách: spodní, střední a svrchní vrstva. Každá plní jinou funkci a chybějící článek se obvykle projeví nepříjemnou zimou nebo mokrem.</p>'
          + T(['Vrstva', 'Úkol', 'Co zvolit'], [
              ['Spodní', 'odvod potu, přiléhavost', '<a href="/lyzarske-termopradlo/">termoprádlo</a>, <a href="/merino-pradlo/">merino prádlo</a>'],
              ['Střední', 'izolace, udržení tepla', '<a href="/fleecove-mikiny/">fleece</a>, lehká izolace'],
              ['Svrchní', 'ochrana před větrem a sněhem', '<a href="/lyzarske-bundy/">bundy</a>, <a href="/lyzarske-kalhoty/">kalhoty</a>, <a href="/lyzarske-kombinezy/">kombinézy</a>'],
              ['Doplňky', 'ruce, hlava, krk, nohy', '<a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, <a href="/lyzarske-ponozky/">ponožky</a>']]) +
          '<p>Bavlna se na zimní aktivity nehodí, protože po zpocení nasákne a odebírá teplo. U bund a kalhot sledujte voděodolnost a prodyšnost: pro suchý mráz stačí lehčí vrstva, pro mokrý sníh potřebujete membránu a proklížené švy. Větrací zipy pomáhají při výstupech. Děti se oblékají o vrstvu více než dospělí na stejný den a často kontrolujte, jestli nejsou zpocené.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Lyže, boty a vázání nabízejí ' + B(('rossignol', 'Rossignol'), ('head', 'Head'), ('atomic', 'Atomic'), ('fischer', 'Fischer'), ('salomon', 'Salomon'), ('k2', 'K2'), ('dynafit', 'Dynafit')) + '. Helmy a brýle jsou doménou značek ' + B(('alpina', 'Alpina'), ('uvex', 'Uvex'), ('scott', 'Scott')) + '. Oblečení najdete u značek ' + B(('helly-hansen', 'Helly Hansen'), ('kilpi', 'Kilpi'), ('dare2b', 'Dare2b'), ('viking', 'Viking'), ('trespass', 'Trespass'), ('protest', 'Protest'), ('o-neill', "O'Neill")) + ' a vosky a servisní materiál u značky ' + B(('swix', 'Swix')) + '. Každá má silnější stránku, a proto je lepší hledat podle konkrétní potřeby než podle loga.</p>'
          '<h2>Bezpečnost mimo sjezdovku</h2>'
          '<p>Kdo opouští upravené trasy, potřebuje lavinovou výbavu, znalost terénu a lavinovou prevenci. Základem je lavinový vyhledávač, sonda a lopata a také umět je rychle použít. Informace o stavu sněhu a bezpečnostní kurz jsou stejně důležité jako vybavení. Na sjezdovce pomáhají <a href="/snowboardove-chranice/">chrániče</a> zad, zápěstí a kolen, hlavně u začátečníků a dětí. V terénu patří k výstupu také <a href="/trekove-hole/">trekové hole</a> a <a href="/celovky-a-svitilny/">čelovka</a> při návratu za šera.</p>'
          '<h3>Kdy nakupovat</h3>'
          '<p>Nabídka zimní výbavy se mění během sezóny. Na začátku jsou nejlépe skladem velikosti, v průběhu zimy a po ní se rozprodávají modely z minulé sezóny, které mívají stejné parametry. Boty a helmy se vyplatí zkoušet vždy, lyže a oblečení lze častěji zvolit podle parametrů. Na Sportece porovnáte nabídky obchodů a uvidíte, co je skladem.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li><strong>Boty o číslo menší:</strong> kvůli lepšímu držení, bolest pak výlet zkazí.</li>'
          '<li><strong>Příliš dlouhé lyže pro začátečníka:</strong> hůř se ovládají a víc unavují.</li>'
          '<li><strong>Bunda bez membrány v mokru:</strong> rychle promokne a uniká teplo.</li>'
          '<li><strong>Bavlněné spodní prádlo:</strong> po zpocení způsobí zimu.</li>'
          '<li><strong>Vynechání servisu:</strong> neseřízené vázání a tupé hrany zvyšují riziko pádu.</li></ul>'
          '<p>Zimní sezóna se nejlépe užívá, když výbava odpovídá úrovni a počasí. Začněte základem a doplňujte podle zkušenosti. Pokud váháte mezi dvěma kusy, upřednostněte ten, který ovlivňuje bezpečnost a pohodlí.</p>',
    faq=[
        ('Co koupit jako první na zimní sporty?', 'Nejdřív boty, helmu a základní oblečení včetně spodní vrstvy a rukavic. Lyže nebo snowboard lze zpočátku půjčit v půjčovně, ale bota musí sedět jako vlastní.'),
        ('Jak velké lyže vybrat?', 'Délka se odvíjí od výšky, váhy, úrovně a stylu jízdy. Začátečníci volí kratší a měkčí lyže, které odpouštějí chyby, zkušení delší a tužší. Při pochybnostech se poraďte v servisu.'),
        ('Má cenu kupovat lyžařské brýle s výměnným sklem?', 'Pokud lyžujete za různého světla, ano. Světlejší sklo se hodí do mlhy a za šera, tmavší na slunce. Jedny brýle se skly pro podmínky ušetří hodně improvizace.'),
        ('Jak poznám, že lyžařské boty sedí?', 'Ve stoji se prsty dotýkají špičky a v mírném předklonu se od ní lehce odtáhnou, přitom pata nevyklouzává. Boty nesmí bolet ani brnět. Zkoušejte je s lyžařskou ponožkou a nechte je několik minut zapnuté.'),
        ('Jak vybrat helmu pro dítě?', 'Změřte obvod hlavy a vyberte helmu, která sedí pevně bez tlaku. Řemínek zapněte tak, aby nebyl uvolněný. Po silném nárazu helmu vyměňte, i když vypadá celá.'),
        ('Jak se oblékat na lyže?', 'Pod bundu a kalhoty oblékněte funkční prádlo a střední izolační vrstvu. Bavlnu vynechte. Vrstev je lepší mít víc a podle teploty je ubírat, než jet v jedné silné.'),
        ('Čím se liší běžecké lyže od sjezdových?', 'Běžecké lyže jsou užší, lehčí a boty mají volnou patu. Používají se na upravených stopách nebo v terénu. Sjezdové jsou širší a zaměřené na jízdu z kopce s pevnou patou.'),
        ('Co potřebuji na skialpinismus?', 'Lehké lyže s vázáním umožňujícím zvednutí paty, stoupací pásy, boty s režimem chůze a lavinovou výbavu. Důležité je také školení a znalost terénu.'),
        ('Kdy se vyplatí nakupovat zimní výbavu?', 'Nejlépe skladem jsou velikosti na začátku sezóny, výhodnější nákup přinášejí modely z minulé sezóny. U bot a helem raději zkoušejte, lyže a oblečení lze vybírat podle parametrů.'),
        ('Jak pečovat o lyže po sezóně?', 'Očistěte skluznici, zkontrolujte hrany a naneste vrstvu vosku jako ochranu. Lyže uložte na suchém a chladnějším místě bez přímého tepla. Před další sezónou nechte seřídit vázání.')])


# ------------------------------------------------------------------ extensions (appended sections)
NEW['bezecka-obuv']['guide'] += (
    '<h3>Jak si zavést plán výměny bot</h3>'
    '<p>Praktický způsob, jak nepřekvapit nohy, je poznamenat si datum koupě a počet běžeckých týdnů. Hodinky i aplikace umějí kilometry u jednotlivých párů sčítat, takže máte přehled bez počítání. Nový pár si pořiďte ještě dříve, než starý úplně dosloužíte, a několik týdnů je střídejte. Přechod je plynulejší a noha si zvykne na odlišné tlumení postupně.</p>'
    '<p>Při změně značky nebo typu boty začněte kratším během a sledujte, jak reagují lýtka, kolena a chodidlo. Pokud se po několika bězích objeví nová bolest, nepokračujte násilím a zvažte jiný model.</p>')
NEW['bezecka-obuv']['faq'] += [
    ('Jaký je rozdíl mezi pánskými a dámskými běžeckými botami?', 'Dámské modely mívají užší patu, mírně odlišný tvar nártu a často měkčí tlumení, protože běžkyně bývají lehčí. Neznamená to ale, že je musí nosit jen ženy. Rozhoduje tvar chodidla, ne označení.')]

NEW['trailove-boty']['guide'] += (
    '<h2>Technika běhu v terénu a vliv na výběr obuvi</h2>'
    '<p>Terénní běh se liší od běhu po silnici kratším krokem, vyšší frekvencí a častými změnami směru. Boty proto musí fungovat jako stabilní platforma pro chodidlo a kotník. Při stoupání se noha opírá o přední část boty, při sbíhání naopak brzdí patou a špičkou, takže potřebuje pevnou patu i ochrannou špičku. Rozdíl pocítíte hlavně na dlouhém klesání, kde špatně sedící bota rychle odhalí všechny nedostatky.</p>'
    '<p>Stabilitu zvyšuje širší základna a nižší profil podešve. Vysoká měkká mezipodešev je pohodlná na rovině, ale na nerovném kameni se noha může nepříjemně naklonit. Pokud máte slabší kotníky, zvolte nižší a tužší konstrukci a posilujte nohy mimo trénink. Naopak na dlouhé ultratratě ocení běžci tlumení, které šetří svaly i klouby po mnoha hodinách.</p>'
    '<h3>Jak otestovat trailové boty před sezónou</h3>'
    '<p>Před první delší akcí je vhodné boty rozběhat. Udělejte několik kratších výběhů s různým povrchem a zkontrolujte, zda nevznikají místa tlaku nebo odření. Vyzkoušejte sběh strmé pěšiny, aby se ukázalo, jestli prsty nenarážejí do špičky, a stoupání, kde se pozná držení paty. Při větší trase s sebou vezměte lehké náhradní ponožky a při delších trasách si prohlédněte stav šněrování a vzorku.</p>'
    '<h3>Vliv ponožek, vložek a šněrování</h3>'
    '<p>Ponožky mění sezení boty víc, než by se zdálo. Tenká ponožka dává větší prostor, silnější ho ubírá. Funkční vlákno snižuje riziko otlaků a rychle schne. Původní vložka bývá základní a u běžců s netypickým klenutím ji lze nahradit tvarovanou vložkou, pokud se vejde. Šněrování lze upravit podle potřeby: při tlaku na nárt vynechte oko, při klouzání paty použijte dvojitý uzel nebo další oko. Správně zafixovaná pata je nejlepším preventivním opatřením proti puchýřům.</p>')
NEW['trailove-boty']['faq'] += [
    ('Jak předejít puchýřům v trailových botách?', 'Vyberte správnou velikost, funkční ponožky bez švů a boty před delší akcí rozběhejte. Pata nesmí klouzat a špička nesmí tlačit. Na mokrých trasách mějte náhradní ponožky a při prvním pocitu tření problém ošetřete.'),
    ('Jsou trailové boty vhodné pro začátečníky?', 'Ano, pokud běháte v lese a po nerovných cestách. Začátečníkovi se hodí středně tlumený model se středním vzorkem a prostornější špičkou. Extrémně lehké a tuhé modely nechte až na později.')]

NEW['sportovni-kalhoty']['intro'] = NEW['sportovni-kalhoty']['intro'].replace('Proto se vybírají podle činnosti', 'Proto se vybírají nejdřív podle činnosti a počasí')
NEW['sportovni-kalhoty']['intro'] += '<p>Vybírat můžete také podle sezóny, pohlaví a značky, a hlavně podle toho, v jaké velikosti jsou kalhoty právě skladem.</p>'
NEW['sportovni-kalhoty']['guide'] += (
    '<h2>Kalhoty podle sportu a ročního období</h2>'
    '<h3>Jaro a léto</h3>'
    '<p>V teplých měsících se hodí tenké kalhoty z rychleschnoucí tkaniny, které odvádějí vlhkost a chrání před sluncem a kopřivami; proti klíšťatům pomáhá kryt kotníků a repelent. Větrání zajistí síťované kapsy nebo zipy na stehnech. Tepláky z lehčích pletenin zvládnou večerní trénink venku, ale na celodenní výlet raději zvolte outdoorový model. Při pobytu u vody uvítáte materiály, které po promočení nepřilnou k tělu.</p>'
    '<h3>Podzim a zima mimo svah</h3>'
    '<p>Pro chladnější období jsou praktické zateplené nebo softshellové kalhoty, případně obyčejné outdoorové kalhoty s termoprádlem pod nimi. Zimní procházky se obejdou bez těžké izolace, protože při pohybu tělo samo hřeje. Při stání na místě, třeba u výhledů nebo při focení, ale vrstva izolace chybí. Dobře fungují kalhoty s větrnou membránou na přední straně a pružným materiálem vzadu.</p>'
    '<h3>Trénink, gym a týmové sporty</h3>'
    '<p>V hale a v posilovně se uplatní elastické kalhoty s nízkou hmotností a odvodem potu. U týmových sportů je výhodou zip na kotníku, aby šly kalhoty rychle sundat přes boty. Děti na školní tělocvik nebo kroužky potřebují hlavně pohodlí, odolná kolena a pevný pas, který nepadá. Pokud ráno trénujete za tmy, vyberte model s reflexními prvky.</p>'
    '<h3>Cestování a každodenní nošení</h3>'
    '<p>Lehké outdoorové kalhoty se uplatní i na cesty. Dobře se perou, rychle schnou a nemačkají se. Několik kapes na zip pomůže uschovat doklady a drobnosti. Sportovně střižené kalhoty vypadají dostatečně decentně i do města a kombinují se s teniskami nebo lehkou obuví.</p>')
NEW['sportovni-kalhoty']['faq'] += [
    ('Jak poznám kvalitní zpracování kalhot?', 'Podívejte se na švy, zipy a kapsy. Švy by měly být rovné, bez volných nití, zipy by měly běhat plynule a zesílená místa nesmí být jen přišitá. Pomáhá i štítek s informacemi o materiálu a údržbě.')]

NEW['zimni-sporty']['intro'] = NEW['zimni-sporty']['intro'].replace('Teprve pak se hodí', 'Teprve potom má smysl')
NEW['zimni-sporty']['intro'] += '<p>Výběr zúžíte podle sportu, značky, velikosti nebo délky lyží a skladové dostupnosti jednotlivých obchodů.</p>'
NEW['zimni-sporty']['guide'] += (
    '<h2>Zimní sporty pro děti a rodiny</h2>'
    '<p>Dětská výbava se řídí jinými pravidly než dospělá. Děti rostou, takže nekupujte drahé vybavení do zásoby a raději využijte půjčovny a bazary na lyže a snowboardy. Naopak helma, rukavice a teplé oblečení by měly mít vlastní, protože na nich závisí bezpečí a zábava. Malé děti rychle prochladnou a navíc se hůř vyjadřují, proto kontrolujte prsty, nos a tváře a často dělejte přestávky na čaj a odpočinek.</p>'
    '<p>Dětské lyžařské boty by měly být měkčí a snáz se zapínat. Lyže pro začátečníky jsou krátké, měkké a odpouštějí chyby. Pokud plánujete bruslení na ledu nebo sáňkování, hodí se helma a pevné rukavice, protože pády bývají zdánlivě nevinné, ale mohou skončit úrazem hlavy. Na sáňky a boby se vyplatí vybrat bezpečný sklon a prostor bez překážek. Kdo plánuje s dětmi celý týden na horách, může si předem projít i <a href="https://kakapo.cz/lyzovani/">nabídky lyžařských pobytů</a> a vybrat ubytování blízko sjezdovky a školky.</p>'
    '<h2>Péče o zimní výbavu</h2>'
    '<p>Po každém dni na sněhu nechte boty a rukavice vyschnout při pokojové teplotě, nikoli na topení. Vyndejte vložky z lyžařských bot a povolte přezky, aby se tvar nedeformoval. Bundy a kalhoty s membránou perte speciálním prostředkem a občas obnovte impregnaci. Hrany lyží a snowboardu po sezóně očistěte a zbavte rzi, skluznici naneste vosk. Vázání před dalším ježděním nechte zkontrolovat v servisu, protože nastavení závisí na váze, výšce a stylu jízdy.</p>'
    '<h3>Doprava a skladování</h3>'
    '<p>Lyže se převážejí ve vaku nebo v držáku na střeše a boty v samostatné tašce, aby se nedeformovaly a nenavlhly. Přehledné <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a> chrání výbavu před poškozením. Po sezóně vybavení rozložte a nechte odvětrat. Skladujte ho na suchém místě bez přímého tepla a před dalším ježděním zkontrolujte vázání, hrany a zip na oblečení.</p>')
NEW['zimni-sporty']['faq'] += [
    ('Mám si koupit lyžařský komplet, nebo samostatné kusy?', 'Komplet je jednodušší a výhodnější pro začátečníky nebo děti, protože lyže a vázání jsou už sladěné. Zkušení lyžaři si častěji skládají samostatné kusy podle potřeby. Boty ale nejlépe kupujte zvlášť.'),
    ('Čím se liší lyžařská a snowboardová bunda?', 'Snowboardové bundy bývají volnější a delší, protože při jízdě i sezení na sněhu potřebují krýt boky. Lyžařské jsou střiženější. Funkce, tedy voděodolnost a izolace, jsou u obou podobné.')]

NEW['sportovni-kalhoty']['guide'] += (
    '<h3>Kalhoty pro děti a dorost</h3>'
    '<p>Dětské sportovní kalhoty musí hlavně vydržet. Zesílená kolena prodlouží životnost při hraní venku, pružný pas s tkaničkou zabrání padání a lemování nohavic se dá po čase upravit. U zimních kalhot hledejte regulovatelné ramínky nebo možnost zkrátit nohavici, aby kalhoty vydržely i druhou sezónu. Děti se mnoho pohybují, proto dávejte přednost měkkým materiálům bez drsných švů a nenechte je v kalhotách, které se po zpocení lepí na kůži.</p>'
    '<p>Při dospívání se mění proporce, takže velikost kontrolujte před každou sezónou znovu. Mladší sourozenci mohou kalhoty po starších dědit, pokud jsou švy a zipy v pořádku.</p>')
