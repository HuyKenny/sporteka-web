"""sporteka.cz — wave 26c (16. 11. 2026): long texts for vyhrivane-obleceni, kluzaky-na-snih.
General true facts only, no prices or exact runtimes. Brands linked only if present in znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ vyhrivane-obleceni
NEW['vyhrivane-obleceni'] = dict(long=True,
    title='Vyhřívané rukavice, ponožky a vložky: jak vybrat',
    desc='Vyhřívané rukavice, ponožky, vložky do bot, vesty a ohřívače rukou. Baterie, stupně ohřevu, praní a bezpečnost. Porovnejte nabídky českých obchodů.',
    intro='<p>Vyhřívané oblečení má v sobě tenké topné vlákno nebo fólii, kterou napájí malá nabíjecí baterie. Nejde tedy o „hřejivé“ materiály, které teplo jen zadržují, ale o výrobek, který teplo vyrábí. Hodí se pro lidi, kterým rychle mrznou prsty, a na dlouhé stání v mrazu, lyžování, hokej, rybaření, jízdu na motorce nebo večerní procházky se psem.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů: vyhřívané rukavice a palčáky, ponožky, vložky do bot, vesty, bundy, nákrčníky, vyhřívané tašky a také ohřívače rukou, a to bateriové i opakovaně použitelné gelové. Nic zde neprodáváme, u vybraného kousku kliknete do obchodu a nakoupíte přímo tam. V nabídce najdete například značky Lenz, W-tec, Glovii a Oxford a ve větším počtu také ' + B(('regatta', 'Regatta'), ('insportline', 'Insportline'), ('trespass', 'Trespass'), ('kilpi', 'Kilpi'), ('viking', 'Viking'), ('bauer', 'Bauer')) + '.</p>'
          '<p>Běžné zimní vybavení najdete v jiných kategoriích: <a href="/lyzarske-rukavice/">lyžařské rukavice</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, <a href="/termopradlo/">termoprádlo</a> a <a href="/zimni-obuv/">zimní obuv</a>. Vyhřívání je přídavek k dobré vrstvě, nenahrazuje ji. Celkový přehled zimních kategorií je v sekci <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    guide='<h2>Jak vyhřívané oblečení funguje</h2>'
          '<p>V látce nebo v textilní vložce vedou tenké vodivé nitě, uhlíková vlákna nebo fólie. Průchodem proudu se zahřívají – podobně jako elektrická přikrývka, jen v malém. Napájí je Li-ion baterie schovaná v kapse, v manžetě nebo v zadní části ponožky. Kapacita se udává v mAh a napětí většinou odpovídá nabíjení přes USB. Zapíná se tlačítkem na baterii nebo na oblečení, případně bezdrátovým ovladačem či aplikací v telefonu.</p>'
          '<p>Teplo se rozptyluje do okolí, takže vyhřívání nejlépe funguje tam, kde je dobrá izolace. Tenká rukavice bude na větru hřát hůř než dobře utěsněná zimní. Právě proto se vyhřívané modely dělají nejčastěji jako zimní rukavice s membránou a zateplením.</p>'
          '<h2>Co všechno se dá koupit</h2>'
          + T(['Typ', 'Kam se teplo dostává', 'Na co dát pozor'], [
              ['Rukavice a palčáky', 'prsty a hřbet ruky, někdy i dlaň', 'umístění topných prvků, výška manžety, velikost, baterie v manžetě'],
              ['Ponožky', 'prsty a nárt, případně celé chodidlo', 'tloušťka vůči botě, praní, pružnost kolem baterie'],
              ['Vložky do bot', 'chodidlo od špičky po patu', 'bezdrátové ovládání, kapacita, přizpůsobení velikosti'],
              ['Vesty a bundy', 'záda, hrudník, někdy i ramena a kapsa', 'počet topných zón, umístění baterie, střih, zateplení'],
              ['Nákrčníky a čepice', 'krk a obličej', 'pohodlí, praní'],
              ['Vyhřívané tašky', 'obsah tašky a záda', 'baterie a kapacita, zateplení'],
              ['Bateriové ohřívače rukou', 'dlaň a kapsa', 'dobíjení, hmotnost, teplota povrchu'],
              ['Gelové ohřívače rukou', 'dlaň a kapsa po zahřátí', 'opakované použití, doba chladnutí'],
              ['Vyhřívané gripy a vyhřívání obuvi', 'ruce na řídítkách, chodidla ve výbavě', 'záleží na konkrétním použití']]) +
          '<h2>Vyhřívané rukavice a palčáky</h2>'
          '<p>Tady je výběr nejširší a rozdíl dělá hlavně umístění topných prvků. Nejlépe je vyhřívat prsty a hřbet ruky, protože právě prsty mrznou nejdřív. Dlaň je u některých modelů vynechána kvůli úchopu a pohodlí. Palčáky drží teplo lépe než prstové rukavice, protože se prsty navzájem zahřívají, zato se v nich hůř manipuluje s věcmi. Pro lyžaře bývá volba jasná: vyhřívaný palčák s dlouhou manžetou, kterou lze zasunout pod rukáv i přetáhnout přes něj. Rybáři nebo fotografovi se víc hodí prstová rukavice s tenčí dlaní, ve které zvládne stisknout spoušť nebo uvázat návazec.</p>'
          '<p>Vždy dbejte na velikost. Příliš těsná rukavice stlačí izolaci a zhorší prokrvení prstů, takže budou zábst i s vyhříváním. Prsty se v rukavici musí lehce hýbat a nemají tlačit na špičku. Baterie bývá v manžetě, kde ji nahmatáte i v rukavici; ověřte si ale, zda tlačítko zvládnete stisknout i prsty v rukavici.</p>'
          '<h2>Vyhřívané ponožky a vložky do bot</h2>'
          '<p>Nohy bývají na mrazu největším problémem. Obuv je těsná, chodidlo je daleko od srdce a od země do něj táhne chlad. Výhodou vyhřívaných ponožek je, že hřejí přímo u kůže. Bývají ale silnější než běžné ponožky, takže boty zkoušejte právě s nimi, aby prsty měly dost místa. Vložky se naopak dají přendávat z boty do boty a nemusí se prát, v botě ale nesmějí zabírat tolik místa, aby chodidlo tlačily nahoru.</p>'
          '<p>U vložek sledujte, zda se dají přistřihnout na velikost a zda jsou topné prvky chráněné. U bot s těsným střihem (běžecké lyžáky, brusle) zkoušejte hlavně pohodlí. Příliš silná vyhřívaná ponožka může zmenšit prostor pro prsty a pak se prokrvení zhorší. Boty by měly sedět s ponožkou, kterou chcete nosit. Základ tepelného pohodlí nohou ale dál tvoří <a href="/lyzarske-ponozky/">kvalitní ponožky</a> a <a href="/zimni-obuv/">obuv</a> s dobrou izolací; vyhřívání je jen podpora.</p>'
          '<h2>Vesty, bundy a doplňky</h2>'
          '<p>Vyhřívaná vesta hřeje trup, tedy místo, odkud se teplo rozvádí do celého těla. Je to výhodný způsob, jak zahřát celé tělo – s trupem se ohřejí i ruce a nohy. Na rozdíl od rukavic se vesta hodí pod bundu jako střední vrstva. V nabídce jsou dámské i pánské střihy, často s několika topnými zónami (záda, hrudník, někdy ramena). Dobrá vesta nemá topné plochy v místech, kterými se opíráte nebo na která doléhá batoh.</p>'
          '<p>Vyhřívané bundy kombinují zateplení s topnými zónami a bývají dražší. Smysl dávají pro dlouhé stání venku, třeba u hokejových zápasů, na rybách nebo při práci na zahradě. Pro aktivní sport, kdy se tělo ohřeje samo, je vrstvení často praktičtější. Doplňky jako nákrčník nebo vyhřívaná taška mají užší využití, motorkářům a cyklistům se ale nákrčník osvědčí.</p>'
          '<h2>Baterie a nabíjení</h2>'
          '<p>Většina oblečení používá lithium-iontovou baterii s kapacitou udávanou v mAh a nabíjením přes USB. Vyšší kapacita znamená delší provoz, ale také větší a těžší baterii. Výdrž závisí na zvoleném stupni a kapacitě baterie; údaje výrobce se obvykle vztahují k nejnižšímu stupni. Na nejvyšším stupni počítejte s mnohem kratší dobou. Pro celodenní výlet proto zvažte náhradní baterii nebo powerbanku, pokud ji výrobce povoluje.</p>'
          '<ul><li>Nabíjejte originálním nebo doporučeným zdrojem a kabelem, ne levnou nabíječkou neznámého původu.</li>'
          '<li>Baterii nenabíjejte bez dozoru a nenechávejte ji nabíjet přes noc na hořlavém podkladu.</li>'
          '<li>Při mrazu baterie ztrácí kapacitu. Před výletem ji mějte nabitou, a pokud to jde, noste ji blíž u těla.</li>'
          '<li>Poškozenou, nabobtnanou nebo promáčklou baterii nepoužívejte.</li>'
          '<li>Při delším skladování nenechávejte baterii úplně vybitou a uložte ji v suchu a chladu.</li></ul>'
          '<p>Při cestování letadlem platí pro lithiové baterie zvláštní pravidla. Ověřte si je u letecké společnosti ještě před odletem, zejména zda baterie patří do příručního zavazadla.</p>'
          '<h2>Stupně ohřevu a ovládání</h2>'
          '<p>Většina výrobků nabízí dva až čtyři stupně, často označené barvou kontrolky. Nejnižší stupeň stačí na mírný mráz a dlouhé stání, střední na pohyb s přestávkami a nejvyšší pro krátké zahřátí. Praktické je, když si výrobek pamatuje poslední zvolenou úroveň a dá se ovládat i v rukavici. Bezdrátový ovladač a aplikace jsou příjemné, ale přidávají další baterii, kterou je třeba nabíjet. U vložek a ponožek je ovladač často nutností, protože tlačítko je schované v botě.</p>'
          '<h2>Péče, praní a bezpečnost</h2>'
          '<p>Před praním vždy vyjměte baterii a zkontrolujte návod. Mnohé kusy se perou jen ručně nebo v šetrném programu při nízké teplotě, bez aviváže a bez sušičky. Nikdy nežehlete přes topné prvky. Pokud oblečení při použití nepříjemně hřeje na jednom místě, přestaňte ho používat. Děti by vyhřívané oblečení neměly používat bez dozoru. Lidé s kožním onemocněním nebo sníženým vnímáním tepla by si měli před použitím ověřit u lékaře, zda jim vyhřívání nevadí. Nespěte ve vyhřívaném oblečení a nenoste ho mokré.</p>'
          '<h2>Ohřívače rukou: bateriové a gelové</h2>'
          '<p>Ohřívače rukou jsou levnější a jednodušší způsob, jak zahřát prsty. Bateriové mají vestavěný akumulátor, nabíjejí se přes USB a hřejí na několik úrovní teploty. Některé fungují zároveň jako powerbanka. Jejich výhodou je rychlé zahřátí a možnost regulace. Gelové ohřívače obsahují roztok, který po zmáčknutí kovového plíšku zkrystalizuje a uvolní teplo. Po zahřátí ve vroucí vodě se vrátí do původního stavu a lze je použít znovu. Neobsahují baterii, takže se hodí i do mrazivých podmínek, ale zahřejí jen na omezenou dobu a není u nich žádná regulace.</p>'
          '<p>V nabídce se vyskytují také jednorázové ohřívače, které se po vybalení zahřejí oxidací na vzduchu a po použití se vyhazují. Hodí se jako nouzová rezerva v kapse bundy nebo v rukavici a hřejí po dobu, kterou uvádí výrobce. Všechny ohřívače dávejte do kapsy nebo rukavice, ne přímo na holou kůži, aby nedošlo k popálení, hlavně u dětí a při vyšších stupních.</p>'
          '<h2>Pro koho je vyhřívané oblečení</h2>'
          '<ul><li><strong>Lidé, kterým rychle mrznou prsty:</strong> rukavice nebo palčáky s vyhříváním prstů a vložky do bot.</li>'
          '<li><strong>Lyžaři a snowboardisté:</strong> palčáky a vložky do bot, přídavek k <a href="/lyzarske-rukavice/">lyžařským rukavicím</a> a <a href="/lyzarske-obleceni/">lyžařskému oblečení</a>. Vyhřívání je doplněk k dobře padnoucí obuvi.</li>'
          '<li><strong>Rybáři, myslivci a fotografové:</strong> dlouhé stání na místě, kde se tělo samo nezahřeje.</li>'
          '<li><strong>Motorkáři a cyklisté:</strong> vesta a rukavice, k tomu vyhřívané gripy na řídítka, pokud je motorka podporuje.</li>'
          '<li><strong>Diváci venkovních sportů:</strong> vesta, ohřívače rukou a vložky do bot.</li>'
          '<li><strong>Rodiče malých dětí:</strong> spíš ohřívače rukou do kapsy než vyhřívané oblečení pro dítě.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupě podle největší kapacity baterie bez ohledu na hmotnost a umístění.</li>'
          '<li>Příliš těsná velikost, která stlačí izolaci a zhorší prokrvení.</li>'
          '<li>Očekávání, že vyhřívání nahradí zimní vrstvu. Bez izolace teplo uniká.</li>'
          '<li>Zapomenuté nabití před cestou nebo chybějící náhradní baterie.</li>'
          '<li>Praní s baterií uvnitř, případně v sušičce.</li>'
          '<li>Nákup z neznámého zdroje bez uvedené kapacity, bezpečnostních údajů a záruky.</li></ul>'
          '<h2>Jak číst parametry v nabídce</h2>'
          + T(['Údaj', 'Co znamená'], [
              ['Kapacita (mAh)', 'množství energie v baterii, vyšší hodnota znamená delší provoz a větší baterii'],
              ['Napětí a nabíjení', 'většina modelů se nabíjí přes USB, údaj najdete v popisu'],
              ['Počet stupňů ohřevu', 'obvykle dva až čtyři; čím víc, tím jemnější nastavení'],
              ['Počet topných zón', 'kolik částí těla je vyhřívaných, u vest záda, hrudník nebo ramena'],
              ['Doba provozu', 'výdrž závisí na stupni vyhřívání a kapacitě baterie; údaje výrobce bývají pro nejnižší stupeň'],
              ['Praní', 'zda se baterie vyjímá a jakou teplotu snese textilie'],
              ['Ovládání', 'tlačítko, bezdrátový ovladač nebo aplikace'],
              ['Velikost a střih', 'u rukavic obvod dlaně, u ponožek a vložek velikost boty, u vest a bund střih']]) +
          '<h2>Kde porovnat a jak nakupovat</h2>'
          '<p>Sporteka porovnává nabídky českých e-shopů a objednávku vždy uzavřete přímo v obchodě. Před koupí si zjistěte podmínky vrácení zboží, záruku na baterii a dostupnost náhradní baterie nebo nabíječky. U oblečení, které se těžko zkouší, hledejte velikostní tabulku a recenze od lidí s podobnou postavou. Zvažte také, jak často budete vyhřívání používat. Pokud jen občas vyrážíte na delší zimní akce, může stačit kvalitní termoprádlo, zateplené rukavice a ohřívače rukou v kapse.</p>'
          '<h2>Jak vyhřívání zapojit do vrstvení</h2>'
          '<p>Vyhřívání funguje nejlépe jako součást promyšleného vrstvení. Na kůži patří <a href="/termopradlo/">termoprádlo</a>, které odvádí vlhkost. Přes něj přijde teplá střední vrstva a navrch větruodolná bunda nebo <a href="/lyzarske-kombinezy/">kombinéza</a>. Vyhřívaná vesta slouží jako střední vrstva, bunda ji chrání před větrem a zadržuje teplo. U rukou je to podobné: tenká podvlékací rukavice, vyhřívaná rukavice navrch. Nohy chrání dobře padnoucí vlněná ponožka a boty s odpovídající izolací. Přidáte-li vyhřívání do těsných bot, riskujete horší prokrvení a efekt bude opačný.</p>'
          '<p>Důležitá je i vlhkost. Mokrá rukavice nebo ponožka hřeje špatně a zbytečně vybíjí baterii. Jakmile se začnete potit, vypněte topení nebo vrstvu sundejte, dřív než se zpotíte víc. Mokré oblečení nechte před dalším použitím oschnout, nejlépe při pokojové teplotě, ne na topení.</p>'
          '<p>Nakonec zvažte i hmotnost a objem baterie. U rukavic sledujte, zda baterie v manžetě netlačí na zápěstí a zda se vejde pod rukáv. U ponožek a vložek se baterie nosí na lýtku nebo se připíná na botu a při chůzi nesmí tlačit. Krátký test doma, ještě před prvním výletem, ukáže, zda vám sedí.</p>',
    faq=[
        ('Jak dlouho vyhřívané oblečení vydrží na jedno nabití?',
         'Výdrž závisí na stupni vyhřívání a kapacitě baterie; údaje výrobce bývají pro nejnižší stupeň. Na nejvyšším stupni počítejte s podstatně kratší dobou a v mrazu s tím, že baterie ztrácí část kapacity. Na celodenní akci se hodí náhradní baterie.'),
        ('Dá se vyhřívané oblečení prát?',
         'Většinou ano, ale vždy po vyjmutí baterie a podle návodu. Obvykle se doporučuje šetrné nebo ruční praní při nízké teplotě, bez aviváže a bez sušičky. Nežehlete přes topné prvky.'),
        ('Mohu vyhřívané oblečení vzít do letadla?',
         'Baterie jsou lithiové, a proto pro ně platí zvláštní pravidla. Ověřte podmínky letecké společnosti pro lithiové baterie před odletem, hlavně zda je můžete vzít do příručního zavazadla.'),
        ('Je lepší vyhřívaná vesta, nebo rukavice?',
         'Záleží na tom, co vám mrzne. Vesta ohřívá trup a teplo se rozvádí tělem, takže pomůže i rukám a nohám. Pokud vám ale chladnou hlavně prsty, bývají přímější volbou vyhřívané rukavice nebo palčáky. Kombinace obojího je nejdražší, ale nejpohodlnější.'),
        ('Jak vybrat velikost vyhřívaných rukavic a ponožek?',
         'Řiďte se tabulkou výrobce. Rukavice nesmí být těsné, protože stlačená izolace hřeje hůř a zhorší se prokrvení. U ponožek a vložek zvažte, jestli se do boty vejdou spolu s další ponožkou, a vyberte velikost podle boty.'),
        ('Jsou bateriové ohřívače rukou lepší než gelové?',
         'Bateriové se dají regulovat a rychle zahřejí, ale vyžadují nabíjení. Gelové nemají baterii a po zahřátí ve vodě je můžete používat opakovaně, regulovat je však nelze a hřejí omezenou dobu. Pro nouzovou rezervu v kapse jsou praktické oba druhy.'),
        ('Je vyhřívané oblečení vhodné pro děti?',
         'Dětské modely existují, děti by je ale měly používat jen pod dohledem dospělého. Děti hůř poznají, že jim je příliš horko, a baterie nepatří do jejich rukou. Pro menší děti je často lepší zateplené oblečení a ohřívače rukou do kapsy.'),
    ])

# ------------------------------------------------------------------ kluzaky-na-snih
NEW['kluzaky-na-snih'] = dict(long=True,
    title='Kluzáky na sníh: plastové, talíře, Snow Rocket',
    desc='Kluzáky na sníh pro děti i dospělé: plastové, talíře, Snow Rocket, nafukovací i dvoumístné. Jak vybrat velikost a bezpečně. Porovnejte nabídky obchodů.',
    intro='<p>Kluzák na sníh je nejjednodušší způsob, jak si užít zasněžený kopec. Je lehký, bez ocelových částí a dá se vzít pod paží nebo za provaz. Děti na něm zvládnou první jízdu i bez zkušeností a dospělí ocení, že se nemusí tahat s těžkými klasickými saněmi a kluzák se vejde do kufru. Sporteka porovnává nabídky českých e-shopů u plastových kluzáků, talířů, raket typu Snow Rocket, nafukovacích kluzáků i dvoumístných modelů.</p>'
          '<p>V nabídce uvidíte známé značky jako Sulov, Stiga a Prosperplast, zahraniční dodavatele jako KHW a Spartan a další. Sporteka sama nic neprodává: ukáže vám, kde kluzák na sníh aktuálně nabízejí, a nakoupíte přímo v obchodě. Vedle kluzáků nabízí kategorie <a href="/sane-a-boby/">sáně a boby</a> také klasické saně a boby; zimní vybavení pro celou rodinu shrnuje sekce <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<p>Na svah patří i vhodné oblečení. Podívejte se na <a href="/lyzarske-obleceni/">lyžařské oblečení</a> a <a href="/lyzarske-kombinezy/">kombinézy</a>, <a href="/lyzarske-rukavice/">rukavice</a> a pro děti také <a href="/lyzarske-helmy/">helmu</a>.</p>',
    guide='<h2>Jaké kluzáky existují</h2>'
          '<p>Slovem kluzák se označuje několik odlišných tvarů. Liší se způsobem sezení, ovladatelností a tím, jak se na nich brzdí. Před koupí si ujasněte, kdo bude jezdit a na jakém svahu.</p>'
          + T(['Typ', 'Popis', 'Hodí se pro'], [
              ['Plastový kluzák (lopata, korýtko)', 'tvarovaná miska se zvýšeným předkem, často s provazem nebo úchyty', 'malé děti a krátké svahy'],
              ['Sněžná raketa (Snow Rocket)', 'delší aerodynamický tvar s opěrkou a madly, sedí se i leží', 'větší děti a mladiství, rychlejší jízda'],
              ['Talíř', 'kulatá plocha s úchyty, točí se při jízdě', 'zábava na mírném svahu, i více dětí'],
              ['Nafukovací kluzák', 'nafukovací tubus nebo kruh, měkký, v hlubokém sněhu se nezaboří', 'větší rychlost na prašanu, pohodlí'],
              ['Dvoumístný kluzák', 'delší tělo pro dospělého s dítětem nebo dvě děti', 'rodiče s malými dětmi'],
              ['Kluzák s řízením nebo brzdou', 'madla, brzdová rukojeť nebo řízení', 'děti, které se učí zatáčet a zastavovat']]) +
          '<h2>Plastový kluzák: nejjednodušší volba</h2>'
          '<p>Nejběžnější kluzák je z jednoho kusu plastu s mírně zvednutým předkem. Je odolný, nepromokne a snadno se čistí. Většinou má provaz nebo madlo vpředu, aby se dal vytáhnout do kopce. Menší kluzák pro dítě předškolního věku stačí na mírný svah, větší už unese i dospělého. Při výběru sledujte nosnost, rozměr sedací plochy a také to, zda má úchyty pro ruce. Bez nich se dítě drží okraje, a to je při rychlejší jízdě méně jisté.</p>'
          '<p>Pozor na materiál. Plast v mrazu křehne a tenký hlubokotažený kluzák může při nárazu na kámen prasknout. Kvalitní model je z polyethylenu určeného do mrazu, bez ostrých hran. Na mrazu, třeba pod minus deset stupňů, ho nikdy neohýbejte a nešlapejte na něj. Dobře si prohlédněte spodek: hladký a rovný lépe klouže a nezachytává se.</p>'
          '<h2>Sněžná raketa: tvar, rychlost a ovládání</h2>'
          '<p>Kluzáky ve tvaru rakety, jako je Stiga Snow Rocket, jsou delší a užší. Dítě se na nich opře o opěrku zad, nohy dá dopředu a drží se madel. Jezdí se rychleji než na plastové lopatě, protože tvar lépe klouže a těžiště je nízko. Zatáčí se nakláněním těla, případně pomocí nohou. Hodí se pro starší děti, které se už spolehlivě udrží a umějí zastavit. Raketa je vhodnější na delší a pomalu klesající svahy než na krátký strmý kopeček, kde by dítě kvůli vysoké rychlosti nestihlo zabrzdit.</p>'
          '<p>Ve výběru najdete různé délky, například 80 nebo 110 cm. Delší model má větší sedací plochu a pojme i vyšší dítě, kratší je lehčí a tolik se nerozjede. Řiďte se výškou a hmotností dítěte podle údajů výrobce.</p>'
          '<h2>Talíř a nafukovací kluzáky</h2>'
          '<p>Talíř je kulatý plastový kruh, na kterém se sedí nebo klečí. Nemá určený směr jízdy, takže se při jízdě otáčí. Děti to baví, rodiče už méně, protože talíř nejde řídit. Hodí se na mírný svah s dlouhým výběhem, kde nic nehrozí. Nikdy nejezděte tam, kde by se talíř mohl rozjet do stromů, plotu nebo silnice.</p>'
          '<p>Nafukovací kluzáky jsou z pevného nafukovacího materiálu, který je měkčí a při nárazu odpruží. Hodí se pro hlubší sníh a větší rychlosti, musí se ale nafouknout pumpičkou a po propíchnutí opravit. Vezměte s sebou záplatu, pokud jezdíte po drsnějším povrchu, a před jízdou zkontrolujte tlak. Zajímavou variantou jsou kluzáky pro dva, často s úchyty pro obě osoby.</p>'
          '<h2>Jednomístný, nebo dvoumístný</h2>'
          '<p>Dvoumístný kluzák je praktický, když jezdíte s malým dítětem, které by samotné nezvládlo ovládat ani zastavit. Dospělý sedí vzadu, drží dítě před sebou a může brzdit nohama. Dvoumístný model je ale delší a hůř se nosí i táhne do kopce. Pro větší děti jsou lepší dva jednomístné kluzáky, protože každé jede samo a svým tempem. Dbejte na celkovou nosnost, která platí pro všechny sedící dohromady.</p>'
          '<h2>Velikost, věk a nosnost</h2>'
          '<p>Kluzák musí odpovídat výšce a hmotnosti jezdce. Výrobce obvykle uvádí věkové rozmezí a maximální zatížení. Příliš velký kluzák na malém dítěti se těžko ovládá, na příliš malém zase jezdec nesedí stabilně. Pro nejmenší děti je vhodnější kluzák s opěrkou a pásem, nebo jízda s dospělým. Menší děti by nikdy neměly jezdit samy bez dozoru.</p>'
          '<h2>Brzdy, madla a provaz</h2>'
          '<p>Základní kluzák se brzdí jen nohama, jinak ho zpomaluje pouze tření o sníh. Pro děti se hodí model s madly, která se dají pevně držet, a s ruční brzdou. Kdo kupuje rychlejší model, měl by hledat skutečné brzdy, nebo aspoň tvar, který jde zastavit zabořením pat. Provaz vpředu by měl být dost dlouhý, aby se dal držet i dětskou rukou, ale ne tak dlouhý, aby se okolo něj mohly motat nohy. Ověřte, jak pevně je ke kluzáku připevněný, a nikdy si ho neovazujte kolem zápěstí.</p>'
          '<h2>Bezpečnost na svahu</h2>'
          '<ul><li>Jezděte jen na bezpečném svahu s dostatečným výběhem a bez překážek, jako jsou stromy, ploty, kameny, potoky nebo terénní hrany.</li>'
          '<li>Nikdy nejezděte směrem k silnici, parkovišti nebo vodní ploše. Mezi koncem svahu a nebezpečím musí být rozumná vzdálenost.</li>'
          '<li>Pro děti je rozumná helma, například <a href="/lyzarske-helmy/">lyžařská helma</a>. Chrání hlavu při pádu nebo srážce.</li>'
          '<li>Nejezděte po tmě a v mlze, kdy se špatně odhaduje terén.</li>'
          '<li>Nejezděte v davu. Dávejte pozor na ostatní, dohodněte se, kudy se jezdí dolů a kudy se chodí nahoru.</li>'
          '<li>Dospělý dohlíží na děti a stoupá bokem svahu, ne uprostřed dráhy.</li>'
          '<li>Dítě ke kluzáku nikdy nepřivazujte a kluzák s dítětem nikdy netahejte za autem, čtyřkolkou ani skútrem.</li>'
          '<li>Ledový svah, kde se kluzák nedá ovládat, je pro děti nevhodný. Na tvrdém sněhu je rychlost mnohem větší.</li></ul>'
          '<h2>Oblečení a výbava pro kluzákování</h2>'
          '<p>Na kluzáku se sedí, takže kalhoty a bunda musí být nepromokavé. Dítě v obyčejných džínách bude brzy mokré a promrzlé. Hodí se zateplené nepromokavé kalhoty, <a href="/lyzarske-kombinezy/">kombinéza</a>, teplá bunda a dlouhé zateplené rukavice, které se dají utáhnout u zápěstí. Obuv musí mít protiskluzovou podrážku a vyšší svršek, aby se dovnitř nedostal sníh. Pod oblečení patří <a href="/termopradlo/">termoprádlo</a> a <a href="/lyzarske-ponozky/">teplé ponožky</a>. Na zábly ruce a nohy pomohou i <a href="/vyhrivane-obleceni/">vyhřívané doplňky</a> nebo ohřívače rukou do kapsy.</p>'
          '<p>Při cestě do kopce s kluzákem na provaze pomohou <a href="/nesmeky/">nesmeky</a>, hlavně na zledovatělých cestách ke svahu. Pomůže i malý batoh s čajem a náhradními rukavicemi.</p>'
          '<h2>Uskladnění a péče</h2>'
          '<p>Po sezoně kluzák očistěte od bláta a soli, osušte a uložte na suchém místě mimo přímé slunce, protože UV záření plast postupně vysušuje. Nepokládejte na něj těžké věci, jinak se zdeformuje. Nafukovací kluzák vyfoukněte, osušte a složte bez ostrých záhybů. Pokud je kluzák prasklý nebo má ostré hrany, vyřaďte ho, aby se dítě neporanilo. Uvolněný provaz nebo poškozená madla opravte dřív, než na něm dítě znovu pojede.</p>'
          '<h2>Jak vybrat podle věku a svahu</h2>'
          + T(['Situace', 'Doporučení'], [
              ['Batole a předškolní děti', 'menší plastový kluzák s madly nebo jízda s dospělým na mírném svahu'],
              ['Školní děti', 'větší plastový kluzák, talíř nebo raketa s opěrkou'],
              ['Rodič s dítětem', 'dvoumístný kluzák nebo jízda dospělého s dítětem na jednom kluzáku, respektujte nosnost'],
              ['Mladiství a dospělí', 'delší model nebo nafukovací kluzák, vhodný je delší svah s výběhem'],
              ['Mírný, krátký kopec', 'plastová lopata, talíř'],
              ['Delší pozvolný svah', 'raketa nebo nafukovací kluzák'],
              ['Sníh je mokrý a těžký', 'kluzák s hladkým spodkem, těžší sníh brzdí'],
              ['Tvrdý či zledovatělý svah', 'nejezdit nebo volit pomalejší kluzák, hrozí velká rychlost']]) +
          '<h2>Na co si dát pozor při koupi</h2>'
          '<ul><li>Údaj o nosnosti a doporučeném věku.</li>'
          '<li>Tloušťka plastu a tvar okrajů, aby nebyly ostré.</li>'
          '<li>Pevné úchyty a provaz, které se po zatažení neutrhnou.</li>'
          '<li>Zda je kluzák určený do mrazu, a nejde jen o plastovou hračku.</li>'
          '<li>Rozměry kluzáku vzhledem k autu. Dlouhou raketu do kufru nesložíte.</li>'
          '<li>Hmotnost – dítě ho bude do kopce nosit nebo táhnout mnohokrát.</li></ul>'
          '<h2>Kde porovnat a nakoupit</h2>'
          '<p>Sporteka porovnává nabídky českých e-shopů a kluzák kupujete přímo v obchodě, který vyberete. Před objednáním si ověřte rozměr, nosnost a dostupnost. Sezona kluzáků je krátká, a když napadne dost sněhu, oblíbené modely se v obchodech rychle vyprodají. U nafukovacích kluzáků zjistěte, zda je v balení pumpička a záplata. U větších kusů zkontrolujte poštovné, protože doručení rozměrného zboží bývá dražší.</p>'
          '<h2>Kluzák, boby, nebo klasické saně</h2>'
          '<p>Klasické dřevěné saně s kovovými lyžinami jsou stabilní, vydrží dlouho a dá se na nich vézt i náklad, ale jsou těžké a při nehodě tvrdší. Boby s řízením se ovládají lépe a hodí se pro delší sjezdy, jsou ale rychlé a potřebují vhodný svah. Plastové kluzáky jsou nejlehčí, dají se pohodlně přenášet a v autě zaberou méně místa. Nejsou však tak dobře ovladatelné a svah by měl být mírnější. Pro rodinné odpoledne na nedalekém kopci bývá lehký kluzák nejlepší volbou, na delší výlety v horách se spíš hodí klasické saně nebo boby. Více variant najdete v kategorii <a href="/sane-a-boby/">sáně a boby</a>.</p>'
          '<p>Pokud dítě začíná, vybírejte nejdřív jednoduchý kluzák. Postupně pak zjistíte, zda vás baví rychlejší jízda, a můžete přejít na raketu nebo bob. Vždy ale platí, že vhodný svah, správné oblečení a dohled dospělého jsou důležitější než parametry kluzáku.</p>',
    faq=[
        ('Od kolika let může dítě jezdit na kluzáku?',
         'Záleží na typu a údajích výrobce. Nejmenší děti by měly jezdit jen s dospělým a na mírném svahu, samostatně až když se spolehlivě udrží a umí zastavit. Vždy dodržujte věkové rozmezí a nosnost uvedené u výrobku.'),
        ('Jaký kluzák vybrat pro malé dítě?',
         'Menší plastový kluzák s madly nebo opěrkou, případně jízdu dítěte s dospělým na dvoumístném kluzáku. Svah má být mírný, bez překážek a s dlouhým výběhem.'),
        ('Je plastový kluzák bezpečný v mrazu?',
         'Kvalitní kluzák z plastu určeného do mrazu vydrží, ale tenký nebo levný plast může při nárazu praskat. Před jízdou zkontrolujte, zda nemá trhliny a ostré hrany, a na mrazu jej neohýbejte.'),
        ('Čím se liší Snow Rocket od obyčejného kluzáku?',
         'Raketa je delší a užší, s opěrkou a madly, takže se v ní sedí nebo leží a jede se rychleji. Obyčejný plastový kluzák je kratší a pomalejší, vhodný spíš pro menší děti a kratší svah.'),
        ('Potřebuje dítě na kluzáku helmu?',
         'Helma je pro děti rozumná, protože při pádu nebo srážce chrání hlavu. Lyžařská helma na svah patří při jízdě na kluzáku stejně jako na saních.'),
        ('Lze na jednom kluzáku jet dvě děti nebo dospělý s dítětem?',
         'Jen pokud to výrobce povoluje. Řiďte se uvedenou nosností pro všechny jezdce dohromady. Jednomístný kluzák pro dva nepřetěžujte, protože se hůř ovládá.'),
        ('Kde je bezpečné jezdit na kluzáku?',
         'Na svahu bez stromů, plotů, kamenů a vody, s dostatečným výběhem a bez provozu. Nikdy ne směrem k silnici, parkovišti nebo potoku. Je dobré svah předem projít a děti nechat jezdit pod dohledem dospělého.'),
    ])
