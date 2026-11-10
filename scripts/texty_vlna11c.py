"""sporteka.cz — wave 11c (4. 11. 2026): long texts for sandaly, kosile, fleecove-mikiny. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ sandaly
NEW['sandaly'] = dict(long=True,
    title='Sportovní sandály – trekové, vodní, dámské | Sporteka',
    desc='Sportovní a trekové sandály dámské, pánské i dětské. Jak vybrat podrážku, uchycení a velikost, a porovnání cen z českých obchodů.',
    intro='<p><strong>Sportovní sandály</strong> jsou letní obuv postavená na delší chůzi, brodění potoků a cestování, kde běžný pantofel brzy selže. Mají pevnější podrážku, pásky držící patu i přední část chodidla a materiály, které po namočení nenasáknou jako kůže nebo textil.</p>'
          '<p>Na Sportece vedle sebe uvidíte nabídku <strong>dámských, pánských i dětských sandálů</strong> z českých obchodů a snadno zjistíte, kde je vaše velikost skladem. Níže najdete průvodce typy, podrážkami, uchycením a péčí, aby sandály vydržely víc než jednu sezonu.</p>'
          '<p>Pro náročnější terén se podívejte také na <a href="/trekova-obuv/">trekové boty</a> a pro chvíle u vody na <a href="/obuv-do-vody/">boty do vody</a>.</p>',
    guide='<h2>Jak vybrat sportovní sandály</h2>'
          '<p>Nejdřív si odpovězte, na co budou sandály sloužit. Na celodenní túru potřebujete něco jiného než na pláž nebo na procházku po městě. Kdo chce jedny sandály na všechno, skončí obvykle u kompromisu, který nic nedělá dokonale, a proto se vyplatí přesněji pojmenovat hlavní použití.</p>'
          '<h3>Typy sportovních sandálů</h3>'
          + T(['Typ', 'Hlavní přednost', 'Hodí se na'], [
              ['Trekové', 'protiskluzová podrážka s hlubším vzorkem, nastavitelné pásky', 'túry v suchém terénu, via ferraty nejsou vhodné'],
              ['Vodní', 'rychlé schnutí, měkká guma přilnavá na mokrém kameni', 'brodění, řeky, kajak, paddleboard'],
              ['Městské sportovní', 'lehká pěnová mezipodešev a pohodlná stélka', 'cestování, dovolená, každodenní nošení'],
              ['Barefoot', 'tenká ohebná podrážka bez převýšení paty', 'chůze blízká chůzi naboso'],
              ['Dětské', 'uzavřená špička, suchý zip', 'hřiště, výlety, školka']]) +
          '<h3>Uchycení paty a pásky</h3>'
          '<p>Nejdůležitější rozdíl mezi sportovním a módním sandálem je zajištění paty. Když pata sjíždí dopředu, prsty narážejí do špičky a po hodině chůze se objeví otlaky. Dobré modely mají pásek přes nárt, pásek kolem paty a třetí bod uchycení u kotníku, všechny nastavitelné na suchý zip nebo přezku.</p>'
          '<ul><li><strong>Suchý zip:</strong> rychlé nastavení i mokrýma rukama, časem ale ztrácí přilnavost zanesený pískem.</li>'
          '<li><strong>Přezky a rychloupínací spony:</strong> pevně drží a nezanášejí se, trochu hůř se v pohybu dotahují.</li>'
          '<li><strong>Elastické a šněrovací systémy:</strong> pohodlné na delší dobu, hodí se spíš do klidnějšího terénu.</li></ul>'
          '<h3>Podrážka, tlumení a protiskluz</h3>'
          '<p>Guma s výraznějším vzorkem drží na mokré hlíně a kamenech, tenká hladká podrážka se na kluzkém povrchu chová jako brusle. Tlumení zajišťuje pěna ve střední vrstvě; měkčí je příjemná na dlouhém chození po rovině, tužší podrážka lépe chrání při došlapu na kameny a kořeny. Ohebnost zkontrolujte rukou: sandál by se měl ohnout v místě, kde se ohýbají prsty, ne uprostřed klenby.</p>'
          '<h3>Velikost a sezení</h3>'
          '<p>Chodidlo při teple otéká, takže sandály zkoušejte odpoledne nebo po procházce. Prsty mají mít před sebou malou rezervu a po stranách nesmí přesahovat přes podešev. Širší chodidlo vyžaduje model s nastavitelnými pásky, úzká pata zase vyžaduje pásek, který se dá pevně utáhnout.</p>'
          '<ol><li>Postavte se na sandály a zatlačte patou dozadu, pata nemá vyjet z formy stélky.</li>'
          '<li>Projděte se po místnosti a sledujte, zda pásky netlačí na kotníky.</li>'
          '<li>Zkuste i chůzi ze schodů, kde se nejlépe ukáže posun chodidla.</li></ol>'
          '<h3>Materiály</h3>'
          '<p>Pásky se vyrábějí z polyesteru, nylonu, někdy z kůže. Syntetika schne rychle a nezapáchá tolik jako kůže, kožené modely naopak lépe tvarují chodidlo a vydrží déle s údržbou. Stélky bývají z pěny EVA nebo korku, korková stélka se časem přizpůsobí tvaru nohy, ale vodu snáší hůř než syntetika.</p>'
          '<h3>Sandály, pantofle a boty do vody</h3>'
          '<p>Nezaměňujte sandály s <a href="/pantofle-a-zabky/">pantoflemi a žabkami</a>, které chodidlo nezajišťují a na túru se nehodí. Pokud voda tvoří většinu výletu, zvažte <a href="/obuv-do-vody/">boty do vody</a> s uzavřenou špičkou, a pokud chcete nejpřirozenější došlap, prohlédněte si <a href="/barefoot-obuv/">barefoot boty</a>.</p>'
          '<h3>Sandály na cestování a dovolenou</h3>'
          '<p>Na výlety, kde se střídá město, pláž a lehká stezka, se hodí lehký model, který se dá zabalit do batohu a schne přes noc. Sandály si před odjezdem rozchoďte doma, protože nová obuv na dovolené bývá častou příčinou puchýřů. Do vlhkého prostředí vybírejte materiály bez houbovité absorpce a stélku, kterou lze vyjmout a usušit zvlášť.</p>'
          '<h3>Ponožky v sandálech</h3>'
          '<p>Ponožka v sandálu není jen módní přešlap. Tenká bezešvá ponožka chrání před otlaky a na chladnější ráno přidá pár stupňů pohodlí. Vybírejte materiál, který schne, například syntetický nebo vlnu merino, a podívejte se na nabídku <a href="/sportovni-ponozky/">sportovních ponožek</a>.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou sandály značek {B(("keen", "Keen"), ("teva", "Teva"), ("crocs", "Crocs"), ("skechers", "Skechers"), ("geox", "Geox"), ("columbia", "Columbia"), ("adidas", "Adidas"), ("rieker", "Rieker"), ("biomecanics", "Biomecanics"), ("camper", "Camper"))}. Každá značka má trochu jiný střih, a tak stejné číslo nemusí sedět všude stejně.</p>'
          '<h3>Péče a údržba</h3>'
          '<ul><li>Po koupání nebo brodění sandály opláchněte čistou vodou, písek a bahno brousí pásky i stélku.</li>'
          '<li>Sušte je ve stínu, přímé slunce a radiátor deformují pěnu i lepené spoje.</li>'
          '<li>Stélku občas vyjměte a omyjte mýdlovou vodou, zabráníte zápachu.</li>'
          '<li>Suchý zip vyčistěte kartáčkem od chlupů a písku.</li>'
          '<li>Kožené části ošetřete vhodným impregnačním prostředkem, jakmile zesvětlají nebo ztuhnou.</li></ul>'
          '<h3>Jak sandály vybírat podle sezóny</h3>'
          '<p>Hlavní sezóna je od konce jara do začátku podzimu. Na jaře a na podzim se obvykle prodávají zbytky sezónních kolekcí, v létě je výběr velikostí nejširší. Pokud potřebujete specifickou velikost nebo širší střih, vyplatí se hledat dřív, než se rozprodají střední čísla.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Sandály bez pásku kolem paty na delší túru, kde noha neustále klouže.</li>'
          '<li>Zkoušení brzy ráno, kdy je chodidlo nejmenší.</li>'
          '<li>Hladká pěnová podrážka na kluzký mokrý kámen.</li>'
          '<li>Příliš velká velikost, ve které se noha při sestupu sune dopředu.</li>'
          '<li>Úplně nové sandály na první velký výlet bez rozchození.</li></ul>'
          '<h3>Dětské sandály</h3>'
          '<p>Děti rostou rychle, ale příliš velká obuv zvyšuje riziko zakopnutí. Hledejte uzavřenou špičku, která chrání prsty při běhání, pásky na suchý zip a rezervu zhruba na půl velikosti. Kontrolujte prsty každé dva až tři měsíce, nohy rostou hlavně v létě. Pokud potřebujete zakoupit několik kusů, nabízí Sporteka přehled cen napříč obchody.</p>',
    faq=[('Jaké sandály vybrat na turistiku?', 'Trekové modely s protiskluzovou podrážkou, uchycením paty a nastavitelnými pásky přes nárt a kotník. Na delší túry zvažte raději uzavřenou botu.'),
         ('Jaký je rozdíl mezi sportovními sandály a pantoflemi?', 'Sportovní sandály drží chodidlo pásky kolem paty a nártu, mají pevnější podrážku a snesou delší chůzi. Pantofle jsou jen nasunuté a slouží na krátké vzdálenosti.'),
         ('Mohu v sandálech chodit do vody?', 'Vodní a trekové modely ano, mají rychle schnoucí materiály a přilnavou podrážku. Městské sandály s nasákavou pěnou nebo kůží ve vodě rychle ztratí tvar.'),
         ('Co jsou barefoot sandály?', 'Sandály s tenkou a ohebnou podrážkou bez převýšení paty. Chodidlo se v nich pohybuje blíž přirozené chůzi, ale chybí tlumení, takže na tvrdých površích jsou náročnější.'),
         ('Jak poznám správnou velikost?', 'Prsty mají mít malou rezervu před sebou a nesmí přesahovat po stranách. Pata zůstává v lůžku stélky a pásky se dají utáhnout bez tlaku. Zkoušejte odpoledne, když chodidlo trochu otéká.'),
         ('Hodí se sandály pro děti na každodenní nošení?', 'Ano, pokud mají uzavřenou špičku, pevné uchycení a měkkou stélku. Na sport a delší chůzi jsou lepší než pantofle, protože nohu zajistí lépe.'),
         ('Je lepší textilní, nebo kožený pásek?', 'Textil a syntetika rychle schnou a méně páchnou, kůže se lépe přizpůsobí chodidlu a při údržbě vydrží déle. Do vody je vhodnější syntetika.'),
         ('Jak vyčistit zapáchající sandály?', 'Vyjměte stélku, omyjte vše vlažnou vodou s jemným mýdlem a nechte uschnout ve stínu. Zápachu pomáhá nosit sandály střídavě a nenechávat je mokré v batohu.'),
         ('Mohu sandály nosit i s ponožkami?', 'Ano, tenká bezešvá ponožka chrání před otlaky a v chladnějším počasí zahřeje. Vyberte materiál, který rychle schne a nepáchne.')],
)

# ------------------------------------------------------------------ kosile
NEW['kosile'] = dict(long=True,
    title='Outdoorové a turistické košile | Sporteka',
    desc='Turistické košile pánské i dámské: rychleschnoucí, s UV ochranou i taktické. Průvodce výběrem a ceny z českých obchodů pohromadě.',
    intro='<p><strong>Outdoorová košile</strong> chrání ramena a paže před sluncem, odvádí pot a dá se rozepnout, když je horko. Na rozdíl od běžné kancelářské košile bývá z rychle schnoucí tkaniny, má větrací záložky a rukávy, které se dají vyhrnout a zajistit patkou.</p>'
          '<p>Sporteka porovnává <strong>pánské i dámské turistické a pracovní košile</strong> z českých obchodů, takže uvidíte nabídku značek, velikostí a barev na jednom místě. Níže najdete průvodce materiály, střihy, funkcemi a péčí, ať si vyberete košili, která se hodí na túru, cestování, rybaření nebo pro práci v terénu.</p>'
          '<p>Pod košili se v chladu hodí <a href="/funkcni-tricka/">funkční trička</a>, a když je horko, je lehčí variantou <a href="/polokosile/">polokošile</a>.</p>',
    guide='<h2>Jak vybrat turistickou a outdoorovou košili</h2>'
          '<p>Košile je v outdooru nejvíc ceněná v horku a na slunci. Dlouhý rukáv chrání před spálením, límec brání zátylek a zapnutá knoflíková lišta se dá během několika vteřin otevřít. Vybírejte podle materiálu, střihu a doplňkových funkcí, ne podle vzhledu na ramínku.</p>'
          '<h3>Materiály a jejich vlastnosti</h3>'
          + T(['Materiál', 'Výhody', 'Nevýhody'], [
              ['Polyester', 'rychle schne, lehký, odolný', 'může zapáchat při dlouhém nošení bez praní'],
              ['Nylon', 'pevný, odolný proti otěru, dobře schne', 'méně příjemný na omak než bavlna'],
              ['Bavlna', 'příjemná a prodyšná na suchu', 'po zmoknutí schne pomalu a chladí'],
              ['Merino', 'nezapáchá, hřeje i vlhké', 'jemnější vlákno, méně odolné proti oděru'],
              ['Směsi', 'kombinují pevnost a komfort', 'vlastnosti závisejí na poměru vláken']]) +
          '<h3>Funkce, které se vyplatí</h3>'
          '<ul><li><strong>Větrací záložky na zádech:</strong> pomáhají proudění vzduchu mezi lopatkami.</li>'
          '<li><strong>Patky na rukávech:</strong> vyhrnutý rukáv drží, aniž by klouzal na loket.</li>'
          '<li><strong>Kapsy na hrudi:</strong> s knoflíkem nebo zipem se do nich vejde mapa, brýle nebo telefon.</li>'
          '<li><strong>Zvedací límec:</strong> přikryje zátylek při práci na slunci.</li>'
          '<li><strong>UV filtr:</strong> látka s označením UPF sníží množství záření, které projde na kůži.</li>'
          '<li><strong>Úprava proti hmyzu:</strong> hodí se v některých oblastech, ale časem se praním oslabuje.</li></ul>'
          '<h3>Střih, velikost a délka</h3>'
          '<p>Outdoorové košile se střihají s větší volností v ramenou a pod paží, aby nebránily pohybu. Zkontrolujte délku zad, protože při předklonu nebo sezení v kajaku nesmí vylézat z kalhot. Rukáv vyzkoušejte se zvednutými pažemi, správná košile se nestáhne k lokti.</p>'
          '<p>Pokud jste mezi dvěma velikostmi, vezměte volnější, protože pod košili často přijde ještě tričko nebo lehká vrstva. Dámské střihy jsou užší v pase a mají obvykle kratší rukávy, pánské jsou rovnější. Při tělesné stavbě mimo standard hledejte modely s delším nebo širším střihem.</p>'
          '<h3>Kdy volit košili místo trička</h3>'
          '<p>Na slunečné túry v horách, výlety do teplých zemí nebo plavbu na vodě poskytne košile ochranu bez nutnosti mazat se krémem po celém těle. Při intenzivním běhu nebo kolech se spíš hodí <a href="/funkcni-tricka/">funkční triko</a>, které těsněji přiléhá a nemá knoflíky. Pro vrstvení v chladu poslouží <a href="/termopradlo/">termoprádlo</a> pod košilí.</p>'
          '<h3>Taktické a pracovní košile</h3>'
          '<p>Ve výběru jsou také taktické a pracovní košile se zesílenými lokty, více kapsami a často i maskovacím vzorem. Hodí se pro airsoft, lov, práci v lese a všude tam, kde se látka obírá o větve. Sledujte hlavně odolnost proti otěru, polohu kapes (nesmí překážet popruhům batohu) a hmotnost látky, protože silná tkanina v horku zbytečně hřeje.</p>'
          '<h3>Košile na cestování</h3>'
          '<p>Při zavazadle do letadla ocení cestovatel košili, kterou lze prát v umyvadle a do rána se usuší. Nemačkavé syntetické tkaniny vypadají slušně i po cestě v batohu, merino snese několik dní bez praní. Kombinace košile a <a href="/outdoorove-kalhoty/">outdoorových kalhot</a> pokryje většinu cestovatelských situací.</p>'
          '<h3>Vrstvení a doplňky</h3>'
          '<p>Košile funguje jako střední vrstva pod lehkou <a href="/softshellove-bundy/">softshellovou bundou</a> nebo jako samostatná horní vrstva v teple. Na hlavu se vám může hodit <a href="/cepice-a-celenky/">kšiltovka nebo klobouk</a>, na krk <a href="/nakrcniky-a-satky/">nákrčník</a> pro ochranu před sluncem.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce uvidíte {B(("fjallraven", "Fjällräven"), ("celio", "Celio"), ("nike", "Nike"), ("adidas", "Adidas"), ("gap", "Gap"), ("tommy-hilfiger", "Tommy Hilfiger"), ("calvin-klein", "Calvin Klein"), ("guess", "Guess"), ("armani-exchange", "Armani Exchange"))}. U módních značek sledujte popis materiálu a určení modelu.</p>'
          '<h3>Praní a údržba</h3>'
          '<ul><li>Perte při teplotě uvedené na štítku a vyhněte se aviváži, která zalepí vlákna a snižuje odvod potu.</li>'
          '<li>Funkční tkaniny nesušte v sušičce na vysoký stupeň, mohou ztratit tvar nebo UV úpravu.</li>'
          '<li>Merino perte šetrným programem s prostředkem na vlnu.</li>'
          '<li>Vyvěste a vytvarujte rukávy, ušetříte žehlení.</li>'
          '<li>Impregnaci proti hmyzu a vodě je třeba po pár praních obnovit.</li></ul>'
          '<h3>Barvy a viditelnost</h3>'
          '<p>Světlé barvy odrážejí slunce a v horku jsou chladnější, ale je na nich vidět pot a špína. Tmavé tóny skrývají nečistoty, hřejí však víc. Do přírody se hodí tlumené odstíny, které neplaší zvěř, na horský provoz zase výraznější barva pro lepší viditelnost.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Bavlněná košile na vícedenní túru v dešti, která dlouho schne.</li>'
          '<li>Příliš těsný střih, který se po zvednutí rukou vytahuje z kalhot.</li>'
          '<li>Zapomenutá ochrana zátylku a krku na slunci.</li>'
          '<li>Silná pracovní látka v teple, ve které se tělo přehřívá.</li>'
          '<li>Praní s aviváží a následná ztráta funkčních vlastností.</li></ul>',
    faq=[('Jaká košile se hodí na turistiku?', 'Lehká rychle schnoucí košile z polyesteru, nylonu nebo směsi, s větracími záložkami, patkami na rukávech a případně UV ochranou. Barvu volte podle slunce a okolí.'),
         ('Je bavlněná košile vhodná na túru?', 'Na krátký suchý výlet ano, příjemně se nosí. Při dešti nebo velké potivosti schne pomalu a chladí, proto je na delší túry vhodnější syntetika nebo merino.'),
         ('Co znamená označení UPF?', 'UPF udává, kolik ultrafialového záření látka propustí ke kůži. Vyšší číslo znamená lepší ochranu, platí to ale jen pro zakrytá místa, hlavu a ruce je třeba chránit zvlášť.'),
         ('Jak mám prát outdoorovou košili?', 'Šetrně podle štítku, bez aviváže a bez žehlení. Sušte volně ve stínu, aby se nepoškodila funkční úprava.'),
         ('Jsou dámské košile jinak střižené?', 'Ano, bývají užší v pase a mají kratší rukávy. Pánský střih je rovnější a delší, proto může ženám s menší postavou připadat příliš velký.'),
         ('Jaká velikost je správná?', 'Podle tabulky výrobce a obvodu hrudníku, s malou rezervou na vrstvu pod košilí. Při předklonu a zvednutých pažích se nemá nikde stahovat.'),
         ('Čím se liší taktická košile od turistické?', 'Taktická má zesílené lokty, víc kapes a odolnější látku, určená je pro lov, airsoft nebo práci v terénu. Turistická je lehčí, prodyšnější a míří na pohodlí při chůzi.'),
         ('Hodí se košile i na cestování?', 'Ano, nemačkavý syntetický materiál se pere v umyvadle a rychle schne. Merino zvládne několik dní nošení bez praní a nezapáchá.'),
         ('Chrání košile před klíšťaty a hmyzem?', 'Dlouhý rukáv a zapnutý límec omezují přístup hmyzu, úprava proti hmyzu pomáhá, ale časem slábne. Po návratu z přírody se vždy prohlédněte, na úpravu se nespoléhejte.')],
)

# ------------------------------------------------------------------ fleecove-mikiny
NEW['fleecove-mikiny'] = dict(long=True,
    title='Fleecové mikiny – pánské, dámské, dětské | Sporteka',
    desc='Fleecové mikiny na zip i přes hlavu, pánské, dámské a dětské. Průvodce gramáží, vrstvením a péčí a ceny z českých obchodů pohromadě.',
    intro='<p><strong>Fleecová mikina</strong> je jedním z nejpraktičtějších kousků outdoorové výbavy. Vlákna ze syntetické příze zadržují teplo ve vzduchových kapsách, takže mikina hřeje při nízké hmotnosti, odvádí vlhkost a po zmoknutí rychle schne.</p>'
          '<p>Na Sportece porovnáte <strong>pánské, dámské i dětské fleecové mikiny</strong> z českých obchodů a vyberete podle velikosti, barvy, značky a gramáže. Průvodce níže vysvětluje, jak se liší typy fleece, jak mikinu vrstvit a jak o ni pečovat, aby vydržela mnoho let a nepelichala.</p>'
          '<p>Další možnosti najdete v nadřazené kategorii <a href="/mikiny/">mikiny</a>, mezi <a href="/funkcni-mikiny/">funkčními mikinami</a> nebo mezi <a href="/merino-mikiny/">merino mikinami a svetry</a>.</p>',
    guide='<h2>Jak vybrat fleecovou mikinu</h2>'
          '<p>U fleece rozhoduje tloušťka materiálu, střih a typ zapínání. Lehká mikina se hodí do pohybu a pod bundu, silná na odpočinek a chladné dny. Vyplatí se vědět, k čemu ji budete nosit nejčastěji, protože jedna univerzální mikina většinou nezahřeje v mrazu a nepřehřeje při chůzi do kopce.</p>'
          '<h3>Gramáž a tloušťka</h3>'
          + T(['Gramáž', 'Charakter', 'Použití'], [
              ['do 150 g/m²', 'lehká, tenká, dobře dýchá', 'aktivní pohyb, jaro, podzim, pod bundu'],
              ['kolem 200 g/m²', 'střední, nejuniverzálnější', 'túry, běžné nošení, cestování'],
              ['300 g/m² a více', 'tlustá, měkká a objemná', 'zima, kemp, odpočinek, zimní sporty při klidu']]) +
          '<p>Gramáž uvádějí obchody různě pečlivě, proto ji berte jako orientační. U módních značek také pozor, že „fleece“ v názvu (například Club Fleece) často znamená počesanou bavlnu, která hřeje jinak a po zmoknutí schne pomaleji než polyesterový outdoorový fleece. Důležitější bývá způsob zpracování: hladký fleece lépe dýchá, plyšový je měkčí a teplejší, mřížkový (grid) je lehký a odvádí vlhkost.</p>'
          '<h3>Typy střihu a zapínání</h3>'
          '<ul><li><strong>Celý zip:</strong> nejlépe se větrá, rychle se obléká a svléká přes jiné vrstvy.</li>'
          '<li><strong>Půl zip:</strong> menší hmotnost, méně dírek pro vítr, hodí se na sportovní použití.</li>'
          '<li><strong>S kapucí:</strong> přidá ochranu hlavy a krku, ale pod bundou s kapucí je nepraktická.</li>'
          '<li><strong>Bez kapuce se stojáčkem:</strong> lépe sedí pod bundou a nehromadí látku za krkem.</li>'
          '<li><strong>Dětské modely:</strong> měkké, odolné, s kapsami a často s reflexními prvky.</li></ul>'
          '<h3>Fleece jako střední vrstva</h3>'
          '<p>Při vrstvení funguje fleece uprostřed. Základ tvoří <a href="/termopradlo/">termoprádlo</a> nebo <a href="/funkcni-tricka/">funkční triko</a>, přes něj mikina a navrch větruodolná či nepromokavá bunda, například <a href="/softshellove-bundy/">softshellová</a> nebo z kategorie <a href="/nepromokave-bundy/">nepromokavé bundy</a>. Samotný fleece totiž proud vzduchu propouští, a proto bez svrchní vrstvy v silném větru ztrácí účinnost.</p>'
          '<h3>Ve srovnání s jinými materiály</h3>'
          + T(['Materiál', 'Teplo', 'Hmotnost', 'Poznámka'], [
              ['Fleece', 'dobré, drží i vlhký', 'nízká', 'rychle schne, propouští vítr'],
              ['Merino', 'dobré, nezapáchá', 'střední', 'jemnější a citlivější na údržbu'],
              ['Bavlněná mikina', 'střední', 'vyšší', 'po zmoknutí studí a dlouho schne'],
              ['Softshell', 'střední, odolná větru', 'střední', 'méně dýchá, často s membránou']]) +
          '<h3>Velikost a střih</h3>'
          '<p>Fleece se při nošení málo přizpůsobuje, takže volte takovou velikost, ve které se pohodlně zvednou ruce nad hlavu. Příliš těsná mikina stlačí vzduch ve vrstvách pod sebou a přestane hřát. Příliš velká zase nabírá vítr a pod bundou hromadí látku. Pozor na délku rukávů, manžeta se má dotýkat zápěstí i při předpažení.</p>'
          '<h3>Pro koho a na co</h3>'
          '<ul><li><strong>Turistika a trek:</strong> lehká až střední gramáž, štíhlejší střih, celý zip.</li>'
          '<li><strong>Lyže a běžky:</strong> tenká mikina s vysokým límcem pod lyžařskou bundu.</li>'
          '<li><strong>Kemp a cestování:</strong> tlustší, měkká, dobře stlačitelná v batohu.</li>'
          '<li><strong>Děti:</strong> praktická, snadno vyprat a rychle usychá po hrách venku.</li>'
          '<li><strong>Každodenní nošení:</strong> klasický střih, který zapadne i do města.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("nike", "Nike"), ("regatta", "Regatta"), ("columbia", "Columbia"), ("trespass", "Trespass"), ("under-armour", "Under Armour"), ("helly-hansen", "Helly Hansen"), ("rossignol", "Rossignol"), ("slam", "Slam"), ("dare2b", "Dare2b"), ("adidas", "Adidas"), ("viking", "Viking"), ("leone-1947", "Leone 1947"))}. Britské značky bývají silné v dětských a turistických modelech, sportovní značky v tréninkových střizích.</p>'
          '<h3>Praní a péče</h3>'
          '<ul><li>Perte při nízké teplotě a bez aviváže, která pokrývá vlákna a zhoršuje odvod vlhkosti.</li>'
          '<li>Zapněte zip, aby nepoškrábal ostatní prádlo a nezachytával látku.</li>'
          '<li>Nesušte na topení ani v sušičce na vysoký stupeň, syntetická vlákna se deformují a tvrdnou.</li>'
          '<li>Nežehlete a nepoužívejte bělidlo.</li>'
          '<li>Pokud fleece pelichá, pomůže kartáč na oblečení nebo holicí strojek na žmolky použitý jemně.</li></ul>'
          '<h3>Ekologie a mikroplasty</h3>'
          '<p>Fleece se vyrábí z polyesteru, často z recyklovaných PET lahví, a při praní uvolňuje drobná vlákna. Dopad snížíte praním v ochranném sáčku, nižšími otáčkami a menší frekvencí praní. Kvalitnější mikina vydrží déle než levná, které pelichá už po několika cyklech.</p>'
          '<h3>Sezónnost nákupu</h3>'
          '<p>Nejširší nabídku velikostí a barev najdete na začátku podzimu, výprodeje obvykle přicházejí po zimě. Pokud potřebujete běžnou černou nebo šedou mikinu, bývá skladem prakticky vždy, výraznější barvy a dětské velikosti se rozprodávají rychleji.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Fleece bez svrchní vrstvy ve větru, i když by měla být zima.</li>'
          '<li>Příliš těsná mikina, která stlačí vrstvy pod sebou.</li>'
          '<li>Nejtlustší model na aktivní pohyb, ve kterém se přehříváte.</li>'
          '<li>Praní s aviváží a následná ztráta hebkosti.</li>'
          '<li>Zbytečně dlouhý střih, který se zasekává v popruzích batohu.</li></ul>',
    faq=[('Jaká fleecová mikina se hodí na túru?', 'Lehká až střední gramáž na celý zip, aby se dobře větrala. Měla by se vejít pod bundu a po zmoknutí rychle uschnout.'),
         ('Hřeje fleece, i když je mokrý?', 'Ano, syntetická vlákna nasávají minimum vody, teplo drží i při vlhku a mikina rychle schne. Na rozdíl od bavlny nestudí.'),
         ('Co znamená gramáž fleece?', 'Hmotnost jednoho metru čtverečního látky v gramech. Vyšší číslo značí tlustší a teplejší materiál, ale také těžší a objemnější mikinu.'),
         ('Potřebuji bundu přes fleecovou mikinu?', 'Ve větru nebo v dešti ano. Fleece teplo zadržuje, ale proud vzduchu a déšť propouští, proto se doplňuje větruodolnou nebo nepromokavou svrchní vrstvou.'),
         ('Jak mám fleecovou mikinu prát?', 'Při nízké teplotě, bez aviváže a se zapnutým zipem. Sušte volně, nikdy na topení, protože teplo vlákna zdeformuje.'),
         ('Proč mi fleece pelichá?', 'Povrchová vlákna se třou o jiné oblečení a v pračce. Pomáhá pračka v ochranném pytlíku, nízké otáčky a kvalitnější materiál, žmolky odstraníte strojkem.'),
         ('Jaká je dětská fleecová mikina nejlepší?', 'Měkká, odolná a na celý zip, aby se dítě oblékalo samo. Velikost vybírejte s malou rezervou, příliš velká mikina překáží při hrách.'),
         ('Liší se fleece od funkční mikiny?', 'Fleece je konkrétní materiál s plyšovým povrchem. Funkční mikina může být z různých úpletů, často tenčích a elastičtějších, a míří na sportovní pohyb.'),
         ('Hodí se fleecová mikina do města?', 'Ano, v klasickém střihu a tlumené barvě vypadá nenápadně. Na formální příležitosti se nehodí, ale pro každodenní nošení je pohodlná a lehká.')],
)


# ------------------------------------------------------------------ extensions
NEW['sandaly']['intro'] += ('<p>Při srovnání nabídky dávejte pozor i na určení modelu, protože označení „sportovní“ používají obchody pro velmi různé typy obuvi, od terénních po lehké plážové.</p>')
NEW['sandaly']['guide'] += (
    '<h3>Jak sandály poznat podle konstrukce</h3>'
    '<p>Otočte sandál podešví vzhůru a prohlédněte, jak jsou pásky připevněny. Prošité nebo zalisované konce drží déle než jen nalepené. U trekových modelů se podešev často zvedá kolem špičky, aby chránila palec před kopnutím do kamene. Zkontrolujte také, zda je okraj stélky hladký, protože ostrá hrana při potu rychle způsobí otlak.</p>'
    '<h3>Jak vybrat podle terénu</h3>'
    + T(['Terén', 'Doporučená konstrukce', 'Na co se zaměřit'], [
        ['Zpevněné cesty a města', 'lehká pěnová podešev', 'pohodlná stélka a prodyšné pásky'],
        ['Lesní a polní stezky', 'středně hluboký vzorek, zesílená špička', 'držení paty při sestupu'],
        ['Řeky a pobřeží', 'měkká přilnavá guma, rychle schnoucí pásky', 'protiskluz na mokrém kameni'],
        ['Cestování po městech', 'univerzální sportovní model', 'nízká hmotnost, snadné balení'],
        ['Domácí a zahradní nošení', 'měkká pěna a anatomická stélka', 'pohodlí při dlouhém stání']]) +
    '<h3>Zdravotní hlediska</h3>'
    '<p>Při problémech s klenbou, patní ostruhou nebo plochou nohou hledejte anatomickou stélku s oporou klenby a širší patu. Univerzální rada neexistuje, protože každé chodidlo reaguje jinak, a proto má smysl modely střídat a sledovat, kdy noha začíná bolet. U zdravotních potíží se poraďte s ortopedem nebo podiatrem, sandály sami nic nevyřeší.</p>'
    '<h3>Jak dlouho sandály vydrží</h3>'
    '<p>Životnost závisí hlavně na podešvi a lepených spojích. Když se guma začne drolit nebo odlepuje od pěny, další chůze přestává být bezpečná. Pásky se pomalu protahují, takže po sezóně nemusí držet patu tak pevně jako nové. Včasná výměna ušetří puchýře a v horách i pád na klouzavém kameni.</p>')

NEW['kosile']['intro'] += ('<p>U každé nabídky porovnejte materiál, střih a velikostní tabulku, ať vybraná košile odpovídá tomu, k čemu ji budete nosit: na túru, na cesty, nebo do města.</p>')
NEW['kosile']['guide'] += (
    '<h3>Jak poznat kvalitní zpracování</h3>'
    '<p>Podívejte se na švy, které by měly být rovné, hustě prošité a v místech namáhání zesílené. Knoflíky mají být přišité pevně, ideálně s podšívkou nebo odolným stehem. Dobrá outdoorová košile má límec, který drží tvar po praní, a zadní díl delší než přední, aby při předklonu nevyjížděl z kalhot.</p>'
    '<h3>Srovnání podle ročního období</h3>'
    + T(['Období', 'Vhodná košile', 'Tip'], [
        ['Léto', 'lehký nylon nebo polyester, světlá barva', 'vyhrnuté rukávy a otevřené větrací záložky'],
        ['Jaro a podzim', 'střední gramáž, směsi vláken', 'volnější střih pro lehkou vrstvu pod'],
        ['Zima', 'těžší flanelová nebo pracovní látka', 'jako mezivrstva pod bundou, ne jako svrchní'],
        ['Tropy a vlhko', 'rychle schnoucí syntetika s větráním', 'dlouhý rukáv chrání před sluncem i hmyzem']]) +
    '<h3>Košile pro rybáře, lovce a práci venku</h3>'
    '<p>Rybářské košile mají často velké kapsy na drobnosti a rychle schnou po postříkání. Lovecké bývají tlumených barev a tišší látky, které nešustí. Pracovní zase vydrží otěr o větve a nářadí. U všech tří skupin je důležitá pevnost látky v místech loktů a ramen, kde se obléká popruh batohu nebo pušky.</p>'
    '<h3>Jak se s košilí chovat v praxi</h3>'
    '<ul><li>V horku košili rozepněte, ale ramena a paže nechte zakryté, kůže se nespálí a pot se odpaří.</li>'
    '<li>Při chladném větru košili zapněte a vztyčte límec, ochrání krk.</li>'
    '<li>U vody a při dešti nezapomeňte, že syntetika schne rychleji než kombinované tkaniny.</li>'
    '<li>V batohu ji rolujte, nikoli skládejte, aby se netvořily ostré záhyby.</li></ul>'
    '<h3>Ochrana před sluncem v praxi</h3>'
    '<p>I látka s UV filtrem nechrání obličej a ruce, proto je dobré doplnit ji kloboukem a krémem na odkryté části. Světlé a tenké tkaniny propouštějí víc záření než husté tmavé. Ochrana klesá po opakovaném praní a u mokré látky, což je dobré mít na paměti při dlouhém pobytu u vody.</p>')

NEW['fleecove-mikiny']['intro'] += ('<p>Pomůže vám také vědět, že označení „fleece“ pokrývá materiály od tenkých sportovních po tlusté plyšové, proto se vyplatí sledovat gramáž a popis povrchu.</p>')
NEW['fleecove-mikiny']['guide'] += (
    '<h3>Druhy fleece a jejich povrchy</h3>'
    + T(['Druh', 'Povrch', 'Vlastnosti'], [
        ['Mikrofleece', 'jemný, hladký', 'lehký, ideální pod bundu'],
        ['Plyšový fleece', 'hustý, huňatý', 'velmi hřejivý a měkký, objemnější'],
        ['Grid fleece', 'mřížkový vzor uvnitř', 'dobře odvádí vlhkost a rychle schne'],
        ['Sherpa', 'kudrnatá imitace vlny', 'teplý, spíše na volný čas'],
        ['Fleece s větruodolnou vrstvou', 'hladký s membránou', 'brání větru, ale hůř dýchá']]) +
    '<h3>Jak mikinu zabalit a převážet</h3>'
    '<p>Fleece se dobře stlačí, a tak se pohodlně vejde do batohu jako záloha pro večer nebo pro vrchol kopce. Neskládejte ji natěsno na dlouhou dobu, vlákna se mohou zhuštit a ztratit prodyšnost. Pokud ji nosíte v batohu, uložte ji do svrchní části, ať je po ruce, když se ochladí.</p>'
    '<h3>Doplňky pro zimu</h3>'
    '<p>Při vyšších horách přidejte k mikině i <a href="/cepice-a-celenky/">čepici</a>, <a href="/sportovni-rukavice/">rukavice</a> a <a href="/nakrcniky-a-satky/">nákrčník</a>, protože odkryté hlava a ruce rychle chladnou. Pod mikinu je vhodné <a href="/termopradlo/">termoprádlo</a>, které odvádí pot a hřeje zespodu. Pro vícedenní túry doplňte výbavu o <a href="/turisticke-batohy/">turistický batoh</a> a o lehké <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>.</p>'
    '<h3>Jak vybrat podle pohlaví a věku</h3>'
    '<ul><li><strong>Pánské:</strong> rovnější střih, delší rukávy, větší ramena.</li>'
    '<li><strong>Dámské:</strong> užší pas, kratší rukávy, často tvarovaný střih v bocích.</li>'
    '<li><strong>Dětské:</strong> volnější střih, který nebrání hře, a pevné zipy s tahátkem.</li>'
    '<li><strong>Unisex:</strong> neutrální střih, na který se dobře navrství další oblečení.</li></ul>')


# ------------------------------------------------------------------ extensions 2
NEW['sandaly']['guide'] += (
    '<h3>Jak sandály sladit s dalším vybavením</h3>'
    '<p>Do kempu nebo na vícedenní cestu bývají sandály druhou obuví vedle <a href="/trekova-obuv/">trekových bot</a>. Večer v nich odpočinou chodidla po celodenním tlaku pevné boty a v mokré stanové předsíňce nahradí pantofle. Jejich nevýhodou je menší ochrana prstů a kotníku, proto na náročný technický terén stále patří uzavřená obuv.</p>'
    '<h3>Co zkontrolovat před koupí online</h3>'
    '<ul><li>Zda výrobce uvádí délku stélky v centimetrech, ne jen číslo velikosti.</li>'
    '<li>Zda je v popisu zmíněna podešev s protiskluzovou úpravou.</li>'
    '<li>Jak se nastavují pásky a zda je lze stáhnout i u širší nohy.</li>'
    '<li>Jaké jsou podmínky vrácení, protože sandály je nutné zkusit na vlastním chodidle.</li>'
    '<li>Zda jsou na skladě sousední velikosti, když váháte mezi dvěma čísly.</li></ul>')
NEW['kosile']['guide'] += (
    '<h3>Jak se košile chová při různých aktivitách</h3>'
    '<p>Při chůzi do kopce se tělo zahřívá a nejdůležitější je odvod vlhkosti a možnost rychle rozepnout. Při sezení v lodi nebo v autě záleží spíš na tom, aby látka nezachytávala popruhy a nehřála na zádech. Při práci s nářadím se oceňuje pevnost a při focení nebo pozorování přírody tichá, nešustící látka tlumené barvy.</p>'
    '<h3>Co zkontrolovat před koupí online</h3>'
    '<ul><li>Složení materiálu a to, zda jde o funkční nebo módní model.</li>'
    '<li>Rozměrovou tabulku a obvod hrudníku, ne jen označení S až XXL.</li>'
    '<li>Délku rukávu a zad, u vyšších postav zvlášť.</li>'
    '<li>Podmínky vrácení zboží, abyste mohli velikost bez rizika vyměnit.</li>'
    '<li>Barvu na více fotografiích, protože světlé a pastelové odstíny se na displeji liší.</li></ul>'
    '<h3>Jak košili vybrat pro děti a mladé</h3>'
    '<p>Pro děti hledejte odolnou, snadno pratelnou látku a střih, který jim při hře neomezuje ruce. Rychle rostou, takže se vyplatí volnější velikost s možností vyhrnout rukáv. Pro teenagery je rozhodující i vzhled, proto je dobré košili vybírat společně.</p>')
NEW['kosile']['faq'].append(('Do kdy se vyplatí košili vyměnit nebo vrátit?', 'Podle podmínek obchodu, obvykle je na vrácení zboží zákonná lhůta čtrnácti dnů při nákupu na dálku. Košili vyzkoušejte doma a neodstřihávejte štítky, dokud si nejste jistí velikostí.'))
NEW['fleecove-mikiny']['guide'] += (
    '<h3>Jak se fleece vyrábí a proč na tom záleží</h3>'
    '<p>Fleece vzniká z polyesterových vláken, která se po upletení kartáčují, aby vytvořila huňatý povrch. Čím hustší a rovnoměrnější kartáčování, tím lépe látka drží teplo a tím pomaleji pelichá. Kvalitu poznáte prsty: dobrý fleece je hebký, nevypadává z něj chmýří a po protažení se vrátí do tvaru. Levnější varianty bývají řidší a rychleji žmolkovatější.</p>'
    '<h3>Fleece pro aktivní sport</h3>'
    '<p>Při běhu na lyžích, rychlé chůzi do kopce nebo na kole se tělo zahřívá a mikina nesmí hřát příliš. Hledejte tenký, strečový nebo mřížkový fleece s větracími detaily, třeba zipem pod paží, který rychle vypustí vzduch. Naopak při pozorování zvěře, fotografování nebo čekání u ohně se hodí hustší a tlustší materiál.</p>'
    '<h3>Co zkontrolovat před koupí online</h3>'
    '<ul><li>Zda obchod uvádí gramáž nebo alespoň popis „lehká“, „střední“ a „zimní“.</li>'
    '<li>Zda je zip celý a zda má krytku nebo zarážku pod bradou.</li>'
    '<li>Zda jsou kapsy na zip, protože otevřené kapsy ztrácejí drobnosti.</li>'
    '<li>Jak je zpracovaná manžeta a spodní lem, zda je elastická nebo stahovatelná.</li>'
    '<li>Zda jsou skladem dostupné sousední velikosti, když váháte mezi dvěma.</li></ul>'
    '<h3>Jak mikinu uskladnit</h3>'
    '<p>Před uložením mikinu vyperte a nechte úplně vyschnout. Skladujte ji volně, ideálně pověšenou na ramínku nebo složenou v suchém prostoru. Při dlouhodobém uložení netlačte vrstvy pod těžké věci, vlákna se jinak zploští. Před další sezónou ji nechte vyvětrat, případný zápach z uložení se rychle ztratí.</p>')
NEW['fleecove-mikiny']['faq'].append(('Dá se fleecová mikina nosit celý rok?', 'V létě ve večerních horách nebo na chladnější vodě ano, v mrazu ji doplňte vrstvami. Lehká mikina funguje na jaro a podzim, v zimě slouží jako střední vrstva.'))
NEW['sandaly']['faq'].append(('Hodí se sandály na kolo?', 'Na krátké městské jízdy ano, na delší trasy je lepší uzavřená obuv. Při šlapání na pedálech sandál chrání prsty hůř a hrozí uvolnění paty.'))


# ------------------------------------------------------------------ extensions 3
NEW['fleecove-mikiny']['guide'] += (
    '<h3>Fleece při dětských výletech a hrách</h3>'
    '<p>Děti se při hře venku střídavě potí a ochlazují, a právě proto se fleece osvědčil: vlhkost odvádí od těla a po prvním dešti nebo pádu do trávy schne za pár hodin. Do batůžku se vejde složená do malého balíčku, takže ji rodič vytáhne, jakmile se setmí. Při výběru dbejte na zip s krytkou pod bradou, aby nedrhl, a na kapsy, ve kterých dítě udrží kapesník nebo klíč.</p>'
    '<h3>Jak poznat, že mikina dosloužila</h3>'
    '<p>Fleece neztrácí funkci náhle. Typickým znamením je zplihlý, slepený povrch, který už nezadržuje vzduch, a mikina pak hřeje znatelně hůř než dřív. Druhým signálem jsou prodřené lokty nebo manžety a rozpadající se zip. Zip lze často nechat vyměnit u krejčího, což je levnější než kupovat novou mikinu a hodí se u kvalitnějších kusů.</p>'
    '<h3>Fleece a pocení během dne</h3>'
    '<p>Pokud při chůzi cítíte, že se potíte, rozepněte zip dříve, než se mikina promočí zevnitř. Vlhká vrstva pod bundou se při zastavení rychle ochladí a tělo ztrácí teplo. Lepší je zastavit, mikinu sundat a po zchladnutí ji obléct zpět, než nosit mokrou po celý výlet.</p>')
NEW['sandaly']['guide'] += (
    '<h3>Sandály a hygiena chodidel</h3>'
    '<p>V otevřené obuvi se na chodidlo dostává víc prachu a bakterií, proto se vyplatí nohy po výletě umýt a dobře vysušit mezi prsty. Při pocení pomáhá střídání dvou párů a pravidelné praní stélky. Kdo má sklon k plísním nebo ztvrdlé kůži, měl by sandály používat jen osobně a po vlhkém dni je nechat řádně vyschnout.</p>'
    '<h3>Kdy sandály nepoužít</h3>'
    '<p>Na kamenité zásypy, ledovcové přechody, v prostředí s ostrými předměty nebo při práci s těžkým nářadím jsou sandály nevhodné. Chybí jim ochrana prstů a kotníku. V chladném počasí je lepší uzavřená obuv, protože odkryté chodidlo rychle prochladne.</p>')
NEW['kosile']['guide'] += (
    '<h3>Košile a hmyz v praxi</h3>'
    '<p>V létě v lese a u vody se hodí dlouhý rukáv, zapnutý límec a nohavice zasunuté do ponožek. Světlá barva usnadňuje nalezení klíštěte na látce. Po návratu košili vyklepejte a vyperte, než ji pověsíte do skříně, protože drobný hmyz zůstane na textilu i několik hodin.</p>'
    '<h3>Jak košili sladit s kalhotami</h3>'
    '<p>Zastrčená košile drží záda v teple a chrání bedra, volně nošená se lépe větrá. Při těžkém batohu s bederním pásem nechte košili venku, jinak se pod pásem mačká a tvoří otlaky. Kalhoty s boční kapsou doplní hrudní kapsy košile a rozloží drobné věci tak, aby se k nim dalo dosáhnout i s batohem na zádech.</p>')
