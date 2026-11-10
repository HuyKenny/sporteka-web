"""sporteka.cz — wave 15c (4. 11. 2026): long texts (>= 1650 words) for outdoorove-kalhoty, inline-brusle, cyklo-tasky-a-nosice, salova-obuv.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ outdoorove-kalhoty
NEW['outdoorove-kalhoty'] = dict(long=True,
    title='Outdoorové kalhoty: turistické, odepínací, zimní | Sporteka',
    desc='Outdoorové kalhoty pánské, dámské i dětské: materiál, střih, sezóna a péče. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Outdoorové kalhoty</strong> mají zvládnout víc než běžné džíny: ohýbají se s vámi při stoupání, odolají otěru o kameny a po přeháňce rychle uschnou. Jedny kalhoty ale nezvládnou všechno. Lehký letní model by vás v únorovém větru podržel jen chvíli a zateplené softshelly se v červenci stanou zbytečnou zátěží.</p>'
          '<p>Na Sportece porovnáte <strong>turistické, odepínací, softshellové i zateplené kalhoty</strong> pro muže, ženy a děti z českých obchodů. K tomu se hodí <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a>, <a href="/trekova-obuv/">trekové boty</a> a <a href="/turisticke-batohy/">turistické batohy</a>. Pod tímto textem najdete postup, jak vybrat správný materiál, střih a velikost.</p>',
    guide='<h2>Jak vybrat outdoorové kalhoty podle použití</h2>'
          '<p>Než začnete porovnávat modely, položte si tři otázky: v jakém počasí je budete nosit, jak dlouho v nich budete venku a kolik toho budete nést. Krátká procházka k rozhledně klade jiné nároky než týdenní přechod hor s plným batohem. Čím delší a náročnější akce, tím víc se vyplatí pevnější materiál, vyztužená místa a promyšlené kapsy.</p>'
          + T(['Situace', 'Na co dbát', 'Typ kalhot'], [
              ['Letní túry a výlety', 'lehkost, prodyšnost, rychlé schnutí', 'tenké kalhoty z polyamidu, odepínací modely'],
              ['Jaro a podzim', 'vítr, rosa, chladná rána', 'softshellové nebo pevnější strečové kalhoty'],
              ['Zima mimo sjezdovku', 'teplo a ochrana před sněhem', 'zateplené kalhoty nebo vrstvení s termoprádlem'],
              ['Deštivé dny', 'nepromokavost, větrání', 'membránové kalhoty, případně lehké přes kalhoty'],
              ['Kempování a běžné nošení', 'odolnost, kapsy, pohodlí vsedě', 'kalhoty z pevné směsi s pružným pasem']]) +
          '<h2>Typy outdoorových kalhot</h2>'
          '<ul><li><strong>Lehké letní kalhoty</strong> jsou z tenkého a pružného materiálu, který odvádí pot a rychle schne. Hodí se do tepla, na hřebenovky i na cesty, kde potřebujete zabalit co nejméně věcí.</li>'
          '<li><strong>Odepínací kalhoty</strong> mají nohavice na zip a během pár vteřin z nich uděláte kraťasy. Praktické jsou při ranních i poledních teplotách, ale zipy někomu v dolní části nohavice překážejí. Kdo kraťasy preferuje, najde je v kategorii <a href="/sportovni-kratasy/">sportovní kraťasy</a>.</li>'
          '<li><strong>Softshellové kalhoty</strong> stojí mezi tenkým materiálem a membránou: brání větru, odpuzují drobný déšť a zůstávají pružné. Jsou to nejuniverzálnější kalhoty pro přechodová období.</li>'
          '<li><strong>Membránové kalhoty</strong> jsou určené na vytrvalý déšť. Drží vodu venku, ale při námaze se pod nimi pocení projeví, proto se často nosí jako záložní vrstva v batohu.</li>'
          '<li><strong>Zateplené kalhoty</strong> mají podšívku nebo izolační vrstvu. Využijete je při statické činnosti v chladu, třeba na pozorování zvěře nebo při rybaření, viz <a href="/rybareni/">rybaření</a>.</li>'
          '<li><strong>Trekové kalhoty pro náročné podmínky</strong> mají vyztužená kolena a zadnici a pevnější tkaninu. Používají se na vícedenní túry v kamenitém terénu i při práci v přírodě.</li></ul>'
          '<h2>Materiál: co znamenají zkratky na štítku</h2>'
          '<p>Většina outdoorových kalhot je z polyamidu (nylonu) nebo polyesteru, často s příměsí elastanu pro pružnost. Syntetika nenasákne vodou tolik jako bavlna a rychle schne. Bavlněné nebo bavlněné směsné kalhoty jsou příjemné na dotek a odolné, ale po zmoknutí schnou dlouho a studí. Pro celodenní túru v proměnlivém počasí proto bývá lepší syntetika.</p>'
          '<p>Důležitá je také gramáž a hustota tkaniny. Hustě tkaná látka lépe odolává otěru a větru, řidší dýchá. Hladký povrch rychleji stéká vodou, hrubší je odolnější vůči zachycení o větve. Výrobci často přidávají povrchovou úpravu proti vodě, která je ale jen vodoodpudivá, ne vodotěsná. Při delším dešti prosákne, což je u kalhot normální.</p>'
          '<h3>Pružnost a střih</h3>'
          '<p>Elastan v tkanině dává kalhotám čtyřcestný strečový účinek. Díky němu se nohavice neprotahují a v kolenou se nepřetahují. Podívejte se i na střih: předtvarovaná kolena, klínek v rozkroku nebo gusset usnadňují široký krok a lezení přes překážky. Pro pohyb ve skále se hodí volnější střih, pro běžnou chůzi i přiléhavější.</p>'
          '<h2>Na co se dívat při porovnání detailů</h2>'
          '<ul><li><strong>Kapsy na zip:</strong> mobil, klíče nebo doklady v otevřené kapse snadno vypadnou při sedání nebo kroku přes překážku.</li>'
          '<li><strong>Pas:</strong> kombinace gumy vzadu a pásku vpředu sedí pod popruhy batohu bez tlaku. Příliš silný pásek může pod bederním popruhem třít.</li>'
          '<li><strong>Zip a poklopec:</strong> kovový je odolnější, plastový lehčí. Důležité je, aby nepřetahoval látku.</li>'
          '<li><strong>Zesílená místa:</strong> kolena, zadnice a spodní okraj nohavic vydrží víc otěru.</li>'
          '<li><strong>Zakončení nohavic:</strong> stahovací šňůrka nebo poutko pod botu brání vlezení sněhu a bláta.</li>'
          '<li><strong>Větrání:</strong> zipy na stehnech v některých modelech slouží jako větrací otvory při zahřátí.</li></ul>'
          '<h2>Velikost a délka nohavice</h2>'
          '<p>Vyberte si podle obvodu pasu, boků a vnitřní délky nohy, ne jen podle písmen S, M a L. Každý výrobce má vlastní tabulku a ta se mezi značkami liší. Zkoušejte kalhoty v ohnutém dřepu, při kroku na vyšší schod a s oblečenými podvlékačkami, pokud je plánujete nosit v zimě. Pas se nesmí přetáčet a v koleni nesmějí kalhoty napínat.</p>'
          '<p>Délka nohavice se vyplatí u vyšších a menších postav. Některé značky nabízejí krátké, normální a dlouhé délky, jindy se nohavice zkracuje. Dobré kalhoty mají přes botu nechat malou rezervu, aby při sestupu netahaly. Dětské kalhoty kupujte s rezervou na růst, ale pas musí držet bez neustálého zvedání.</p>'
          '<h2>Pánské, dámské a dětské kalhoty</h2>'
          '<p>Dámské střihy mají jiné proporce pasu a boků, často kratší vnitřní délku a užší stehna. Pánské střihy jsou rovnější. Unisex modely jsou méně běžné, ale existují zejména u pracovních typů. U dětí hledejte kalhoty s vyztuženými koleny, protože právě ta se na výletech otírají nejvíc. Pro menší výletníky se hodí také odepínací kalhoty, které se rychle přizpůsobí, když se dopoledne ochladí.</p>'
          '<h2>Jak kalhoty vrstvit a s čím je kombinovat</h2>'
          '<p>Outdoorové kalhoty tvoří střední vrstvu na nohou. V chladu pod ně patří <a href="/termopradlo/">termoprádlo</a> nebo <a href="/merino-pradlo/">merino prádlo</a>, které odvádí pot od těla. Nad nimi se při dešti nosí membránové přehoz kalhoty. K celkové výbavě patří <a href="/trekove-hole/">trekové hole</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a podle sezóny i <a href="/sportovni-rukavice/">rukavice</a>. V zimních horách přijdou vhod i <a href="/nesmeky/">nesmeky</a> a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('fjallraven', 'Fjällräven'), ('viking', 'Viking'), ('regatta', 'Regatta'), ('northfinder', 'Northfinder'), ('dare2b', 'Dare2b'), ('dynafit', 'Dynafit'), ('loap', 'Loap'), ('alpine-pro', 'Alpine Pro'), ('columbia', 'Columbia'), ('haglofs', 'Haglöfs'), ('kilpi', 'Kilpi'), ('trespass', 'Trespass'), ('hannah', 'Hannah'), ('lundhags', 'Lundhags')) + '. Každá má jiný střih a jinou filozofii. Některé se zaměřují na lehké horské kalhoty, jiné na pevné pracovně-turistické, další na široké rodinné řady. Střih proto zkoumejte u konkrétního kusu a nespoléhejte jen na zkušenost se značkou.</p>'
          '<h2>Péče o outdoorové kalhoty</h2>'
          '<p>Perte kalhoty podle štítku, obvykle na 30 až 40 °C, zapnuté na zip a bez aviváže. Aviváž ucpává póry materiálu a zhoršuje odvádění vlhkosti i odpuzování vody. Nepoužívejte bělidla. Sušte volně rozložené mimo přímé slunce a radiátor. Zvlhlé kalhoty uložené v batohu rozvěste, jakmile dorazíte do tábora.</p>'
          '<p>Povrchovou úpravu proti vodě obnovíte speciálním přípravkem, který se nanáší v pračce nebo sprejem. Ten funguje, pouze pokud je látka čistá, proto se impregnuje po praní. Drobné trhlinky zalepte záplatou dřív, než se roztrhnou. Při skladování na sezónu dbejte, aby byly kalhoty suché, jinak mohou zapáchat a zplesnivět.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupit bavlněné kalhoty na vícedenní túru v dešti a pak se divit, že nechtějí schnout.</li>'
          '<li>Zvolit příliš těsný střih, který v kroku napíná látku a na batohu tře.</li>'
          '<li>Podcenit zipy na kapsách a nechat si mobil v otevřené kapse.</li>'
          '<li>Spoléhat na odepínací nohavice, i když vám zip při chůzi překáží.</li>'
          '<li>Nosit zateplené kalhoty při intenzivním výstupu a skončit zpocený.</li>'
          '<li>Zapomenout, že vodoodpudivá úprava není totéž co nepromokavé kalhoty.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého modelu najdete nabídky několika obchodů vedle sebe, takže snadno uvidíte, kde je právě vaše velikost skladem. Filtrujte podle pohlaví, značky a barvy a čtěte materiálové složení v popisu. Pokud hledáte výbavu na celé tělo, pokračujte do <a href="/outdoor/">outdoor</a> nebo <a href="/sportovni-obleceni/">sportovního oblečení</a> a pro horské akce se podívejte i na <a href="/horolezectvi/">horolezectví</a>.</p>',
    faq=[('Jaké kalhoty na turistiku vybrat?', 'Pro letní túry lehké, pružné a rychleschnoucí z polyamidu s elastanem. Na jaro a podzim softshell, v zimě zateplené nebo vrstvení s termoprádlem. Dbejte na střih v kolenou a zipové kapsy.'),
         ('K čemu slouží odepínací kalhoty?', 'Nohavice se odepnou na zip a kalhoty se promění v kraťasy. Hodí se při změnách teploty během dne, ale zipy u některých lidí v nohavici překážejí.'),
         ('Jsou outdoorové kalhoty nepromokavé?', 'Většina je jen vodoodpudivá. Drobný déšť zvládnou, dlouhý déšť prosákne. Na vytrvalé počasí potřebujete membránové kalhoty, které se obvykle nosí v batohu jako záloha.'),
         ('Mohu outdoorové kalhoty nosit i do města?', 'Ano. Pevný materiál a kapsy se hodí i v běžném provozu, a protože rychle schnou, nevadí ani náhlý déšť. Vybírejte klidnější barvy a méně technické detaily.'),
         ('Jak vybrat správnou velikost?', 'Podle pasu, boků a vnitřní délky nohy dle tabulky výrobce. Vyzkoušejte dřep a široký krok. Pokud je kalhoty napnou nebo spadne pas, zkuste jinou velikost nebo střih.'),
         ('Jak prát outdoorové kalhoty?', 'Na 30 až 40 °C, zapnuté na zip a bez aviváže, která zhoršuje odvádění vlhkosti. Sušte volně, mimo radiátor a přímé slunce. Impregnaci pak obnovte speciálním přípravkem.'),
         ('Jaký je rozdíl mezi softshellem a membránou?', 'Softshell je pružný a dýchá, brání větru a drobnému dešti. Membrána je vodotěsná, ale méně prodyšná a obvykle méně pružná. Pro námahu je lepší softshell, na déšť membrána.'),
         ('Hodí se bavlněné kalhoty na túru?', 'Na krátké výlety za sucha ano, na delší túry a proměnlivé počasí ne. Bavlna nasákne, dlouho schne a v chladu studí.'),
         ('Co pod kalhoty v zimě?', 'Funkční nebo merino spodní prádlo, které odvádí pot. Bavlněné spodky se potí a zůstávají mokré. Vrstvení je v zimě účinnější než jedna silná vrstva.'),
         ('Jaké outdoorové kalhoty pro děti?', 'Pružné, s vyztuženými koleny a gumou v pase. Mělo by jít o materiál, který rychle schne a snese špínu. Raději nepřehánějte velikost, aby děti neklopýtaly o nohavice.'),
         ('Kde najdu další oblečení k outdoorovým kalhotám?', 'V kategoriích sportovní bundy, softshellové bundy, funkční trička, sportovní ponožky a trekové boty. Na horách přibude výbava jako trekové hole a batohy.')],
)

# ------------------------------------------------------------------ inline-brusle
NEW['inline-brusle'] = dict(long=True,
    title='Inline brusle: dětské, dámské, pánské | Sporteka',
    desc='Inline brusle pro děti, dámy i pány: velikost, kolečka, ložiska, brzda a chrániče. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Inline brusle</strong> jsou jeden z nejdostupnějších způsobů, jak si zasportovat na asfaltu: stačí hladká cyklostezka, pár chráničů a trocha trpělivosti. Rozdíl mezi levnými dětskými bruslemi a fitness bruslemi s kvalitními ložisky je ale velký, a to nejen v rychlosti. Liší se pohodlím, stabilitou i tím, jak dlouho vám brusle vydrží.</p>'
          '<p>Na Sportece najdete <strong>dětské, dámské i pánské inline brusle</strong> z českých obchodů a nabídky porovnáte u každého páru. K bruslím patří <a href="/chranice-a-helmy/">chrániče a helmy</a>, hodí se i <a href="/rekreacni-brusle/">rekreační brusle</a>, <a href="/kolobezky-a-brusle/">koloběžky a brusle</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>. Níže vysvětlíme, co všechno ve výběru rozhoduje.</p>',
    guide='<h2>Jak vybrat inline brusle podle toho, kde a jak budete jezdit</h2>'
          '<p>První otázka zní: na co brusle chcete? Rekreační jízda po cyklostezce, pravidelné fitness, dlouhé vzdálenosti nebo sjezd z kopce kladou různé nároky na tvar boty, velikost koleček a tuhost rámu. Většina lidí ale potřebuje obecně použitelné fitness nebo rekreační brusle, které jim dovolí jezdit v různých podmínkách, i když nejsou určené pro náročný terén.</p>'
          + T(['Využití', 'Kolečka a rám', 'Bota'], [
              ['Rekreace a začátečníci', 'menší kolečka, kratší rám, větší stabilita', 'měkčí bota, pohodlí, pevná pata'],
              ['Fitness a delší jízdy', 'střední až větší kolečka, delší rám', 'pevná bota s dobrým držením kotníku'],
              ['Dlouhé vzdálenosti a rychlost', 'největší kolečka, delší rám, kvalitní ložiska', 'tuhá bota s přesným sedem'],
              ['Děti', 'menší kolečka a nastavitelná velikost', 'snadné zapínání, pevný kotník'],
              ['Městské triky a skate', 'tvrdší malá kolečka, rámy pro skluzy', 'zesílená bota, odolný materiál']]) +
          '<h2>Konstrukce brusle: z čeho se skládá</h2>'
          '<p>Inline brusle se skládají z boty, rámu, koleček, ložisek a brzdy. Každá část ovlivňuje jízdu jinak a správná kombinace dá zábavu, špatná zbytečně unaví nohy.</p>'
          '<ul><li><strong>Bota (skořepina a vnitřní botička):</strong> měkká bota se příjemně nosí, ale drží kotník méně. Tvrdá skořepina dobře přenáší sílu, což ocení pokročilejší jezdec. Vnitřní botička bývá vyjímatelná, takže ji lze vyprat.</li>'
          '<li><strong>Zapínání:</strong> tkaničky drží rovnoměrně, přezky se zapínají rychle, kombinace tkaniček s přezkou nebo páskem nad kotníkem drží nejlépe. U dětí je praktické rychlé a bezpečné zapínání.</li>'
          '<li><strong>Rám:</strong> hliníkový je pevný a přesný, plastový lehčí a tlumivější. Delší rám je stabilnější a rychlejší, kratší obratnější.</li>'
          '<li><strong>Kolečka:</strong> větší jedou rychleji a lépe překonávají nerovnosti, menší zrychlují svižněji a bruslí se na nich obratněji.</li>'
          '<li><strong>Ložiska:</strong> určují, jak lehce se kolečka točí. Číslo na ložisku udává přesnost výroby, ale praktický rozdíl pozná zejména pravidelný jezdec.</li>'
          '<li><strong>Brzda:</strong> klasická patní brzda je pro začátečníka nejjednodušší. Pokročilí ji někdy odmontují a brzdí technikou.</li></ul>'
          '<h2>Velikost koleček a tvrdost</h2>'
          '<p>Průměr koleček se udává v milimetrech. Kolečka okolo 80 mm jsou častá na rekreačních a fitness bruslích, větší se hodí na delší trasy a rychlejší jízdu. Menší průměr dává lepší kontrolu a jde většinou o dětské nebo triková modely. Rozhodující je i tvrdost, která se udává na stupnici A. Měkčí kolečko drží na hrubém asfaltu a tlumí vibrace, tvrdší jede rychleji na hladkém povrchu a déle vydrží.</p>'
          '<p>Kolečka se při jízdě obrušují nerovnoměrně, zejména ta, která jsou u brzdy nebo na vnější straně. Proto se otáčejí: přehazují se mezi pozicemi, aby se opotřebovala rovnoměrně. Zvlášť důležité je to u rychlých a dlouhých jízd.</p>'
          '<h2>Velikost brusle a dětské nastavitelné modely</h2>'
          '<p>Velikost brusle se řídí délkou chodidla a výrobcovou tabulkou. Brusle sedí jako sportovní bota: pata pevně, prsty bez ohnutí, ale s drobnou rezervou. Zkoušejte je v tenké sportovní ponožce a procházejte se v nich. Pokud paty při předklonu pohybují nebo tlačí zevnitř, zkuste jinou velikost nebo jiný střih.</p>'
          '<p>Dětské brusle bývají nastavitelné o čtyři až pět velikostí. Ušetří výdaje při růstu, ale rozhodující je, aby i při nejmenším nastavení bota držela. Příliš velká nastavitelná bota s klopýtajícím dítětem nepomůže. Při nastavování se kontroluje, že se nepovolil žádný šroub a že kolečka nebrzdí.</p>'
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p>Dámské brusle bývají užší v patě a mají nižší kotník, pánské širší a objemnější. Unisex modely nabízejí společné velikosti. Děti by měly nosit brusle odpovídající jejich velikosti a hmotnosti: příliš měkké brusle neposkytnou oporu, příliš tuhé mohou odrazovat. Kdo začíná, může zvážit i <a href="/rekreacni-brusle/">rekreační brusle</a> nebo klasické <a href="/brusle/">brusle</a> na led.</p>'
          '<h2>Chrániče a výbava, bez které nejezděte</h2>'
          '<p>Nejčastější zranění začátečníků jsou zápěstí, lokty, kolena a hlava. Chrániče zápěstí, loktů a kolen spolu s přilbou přitom výrazně snižují riziko i závažnost většiny z nich. Zvolte helmu odpovídající velikosti hlavy, která sedí pevně a nekývá se. Chrániče musejí těsně držet, ale nesmějí tlačit na klouby. Celý přehled je v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<p>Přilba na inline brusle může být stejná jako pro <a href="/skateboardy/">skateboard</a> nebo <a href="/kolobezky/">koloběžky</a>. Na cyklostezce, kde se potkáváte s cyklisty, ocení rodiče také <a href="/cyklisticke-helmy/">cyklistické helmy</a>, pokud splňují použití. Nezapomeňte na pohodlné <a href="/sportovni-ponozky/">sportovní ponožky</a> bez švů, které snižují riziko puchýřů.</p>'
          '<h2>Jak začít: základy bezpečné jízdy</h2>'
          '<ol><li>Obujte se doma a zvykněte si na stání na trávě nebo na koberci, na kterém brusle nikam nejezdí.</li>'
          '<li>Naučte se základní postoj: kolena ohnutá, váha mírně dopředu, ruce před tělem.</li>'
          '<li>Trénujte pád směrem dopředu na chrániče a zvedání po pádu.</li>'
          '<li>Pak zvládněte brzdění patní brzdou, nejlépe na rovině.</li>'
          '<li>Vyberte hladké místo bez provozu a bez schodů.</li></ol>'
          '<p>První lekci si vyplatí odbýt s někým zkušeným nebo na kurzu, protože základní technika se ve dvou lidech učí rychleji než samostatně.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejčastěji najdete ' + B(('raven', 'Raven'), ('powerslide', 'Powerslide'), ('fila', 'Fila'), ('roces', 'Roces'), ('k2', 'K2'), ('bauer', 'Bauer'), ('tempish', 'Tempish'), ('nils', 'Nils'), ('rollerblade', 'Rollerblade'), ('nils-extreme', 'Nils Extreme'), ('arcore', 'Arcore'), ('attabo', 'Attabo'), ('sfr', 'SFR')) + '. Liší se zaměřením od dětských a rekreačních modelů po sportovní fitness brusle. Rozdíl nepoznáte podle názvu značky, ale podle konkrétní konstrukce a velikosti.</p>'
          '<h2>Údržba inline bruslí</h2>'
          '<ul><li>Po jízdě v mokru brusle vytřete a nechte vyschnout. Voda zrychluje korozi ložisek.</li>'
          '<li>Pravidelně kontrolujte šrouby koleček a rámu a dotahujte je.</li>'
          '<li>Kolečka otáčejte, když začnou nerovnoměrně ubývat.</li>'
          '<li>Vyměňte patní brzdu, když se stírá k základně.</li>'
          '<li>Ložiska čistěte a mažte podle návodu výrobce. Zanesená ložiska brzdí.</li>'
          '<li>Vnitřní botičku vyjměte a vyvětrejte nebo vyperte podle štítku.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit brusle příliš velké „na růst“ a výsledkem je neustálé klopýtání.</li>'
          '<li>Podcenit chrániče a přilbu a jezdit bez nich.</li>'
          '<li>Vybrat brusle jen podle vzhledu, bez ohledu na sed boty.</li>'
          '<li>Zapomenout, že plastové dětské brusle s rychlou přezkou se hodí na krátkou rekreaci, ne na trénink.</li>'
          '<li>Zanedbat údržbu a po zimě nasadit zrezivělá ložiska.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého páru vidíte nabídky několika obchodů a dostupné velikosti. Použijte filtry podle značky a velikosti. Pro celé spektrum bruslí a podobných sportů si projděte <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>, <a href="/volny-cas/">volný čas</a> a podle potřeby <a href="/hokejove-brusle/">hokejové brusle</a> nebo <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a>.</p>',
    faq=[('Jaké inline brusle vybrat pro začátečníka?', 'Rekreační nebo fitness model s pohodlnou botou, pevným kotníkem, patní brzdou a středně velkými kolečky. Důležitější než značka je správná velikost a sed, a také chrániče.'),
         ('Jak poznám správnou velikost brusle?', 'Změřte chodidlo a porovnejte s tabulkou výrobce. Prsty by měly mít mírnou rezervu, pata sedí pevně a kotník se nehýbe. Zkoušejte v ponožkách, ve kterých budete jezdit.'),
         ('Dají se dětské brusle nastavit s růstem nohy?', 'Nastavitelné dětské brusle vydrží několik velikostí. Důležité je, aby bota i v nejmenším nastavení držela a šrouby byly pevně dotažené.'),
         ('Jaká kolečka jsou nejlepší?', 'Záleží na použití. Větší a tvrdší jedou rychleji na hladkém povrchu, menší a měkčí jsou stabilnější a lépe drží na hrubém asfaltu. Pro rekreaci stačí střední rozměr.'),
         ('K čemu slouží ložiska a jak se pečuje?', 'Umožňují lehké otáčení koleček. Po mokré jízdě je osušte, čistěte podle návodu a občas promažte. Zanesená nebo zrezivělá ložiska brzdí a vrzají.'),
         ('Musím mít chrániče a helmu?', 'Doporučují se vždy, zejména začátečníkům. Chrání zápěstí, lokty, kolena a hlavu, které při pádu nejvíc riskují. Pro děti jsou základní výbavou.'),
         ('Jak dlouho vydrží kolečka?', 'Záleží na povrchu, hmotnosti jezdce a stylu jízdy. Poznáte to podle opotřebení a zešikmení. Pravidelné otáčení pozic koleček životnost prodlužuje.'),
         ('Mohu bruslit po silnici?', 'Pro bezpečnost je vhodnější cyklostezka, hladký chodník nebo uzavřené plochy. Ve společném provozu platí pravidla pro chodce a je třeba dbát předpisů daného místa.'),
         ('Jak brzdit na inline bruslích?', 'Nejjednodušší je patní brzda: jednu nohu natáhněte dopředu, špičku zvedněte a tlačte patou na brzdu. Pokročilejší používají jiné techniky, které se učí v kurzu.'),
         ('Jak brusle uložit přes zimu?', 'Vyčistěte je, osušte a uložte na suchém místě mimo mráz a přímé slunce. Vnitřní botičku vyjměte a vyvětrejte. Před sezónou zkontrolujte šrouby a ložiska.'),
         ('Kde najdu další bruslařské vybavení?', 'V kategoriích rekreační brusle, kolobežky a brusle, chrániče a helmy, skateboardy a hokejové brusle. Pro zimní led se hodí krasobruslařské a hokejové modely.')],
)

# ------------------------------------------------------------------ cyklo-tasky-a-nosice
NEW['cyklo-tasky-a-nosice'] = dict(long=True,
    title='Cyklo brašny, nosiče a košíky: průvodce výběrem | Sporteka',
    desc='Brašny na nosič, tašky na rám a řídítka, košíky a nosiče na kolo: kapacita, uchycení, voděodolnost. Nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Cyklo brašny, nosiče a košíky</strong> mění kolo z jednoduchého dopravního prostředku na nákladní nebo cestovní. Správný systém uloží věci tak, aby kolo bylo stabilní, nic nedrnčelo a po cestě se k obsahu snadno dostanete. Špatně zvolená brašna nebo nosič, které se kývou na nerovnostech, naopak jízdu zhorší.</p>'
          '<p>Na Sportece porovnáte <strong>brašny na nosič, tašky na rám a řídítka, košíky a nosiče</strong> z českých obchodů. K cestování se hodí <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>, <a href="/cyklo-blatniky/">blatníky</a>, <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zamky/">zámky</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Dole vysvětlíme, jak vybrat systém podle trasy i kola.</p>',
    guide='<h2>Jak vybrat uložení na kolo podle způsobu jízdy</h2>'
          '<p>Nejprve určete, co budete vozit a jak daleko. Do práce stačí batoh nebo jedna boční brašna, na víkend vyrazíte s dvojicí brašen a malou taškou na řídítka, na vícedenní cestu potřebujete kompletní systém s nosičem vpředu i vzadu. Čím víc nákladu, tím důležitější je rozložení hmotnosti a pevnost uchycení.</p>'
          + T(['Situace', 'Nejlepší volba', 'Na co dbát'], [
              ['Dojíždění do práce', 'jedna nebo dvě boční brašny na zadní nosič', 'rychlé uchycení, voděodolnost, reflexní prvky'],
              ['Nákupy ve městě', 'košík, brašna na nosič', 'objem a tvar pro tašky, stabilita při odstavení'],
              ['Půldenní a celodenní výlet', 'taška na rám nebo sedlová brašna', 'těsné zapnutí, nerozhoupe se při jízdě'],
              ['Vícedenní cesta', 'brašny na přední i zadní nosič plus taška na řídítka', 'rovnoměrné rozložení, vodotěsnost, pevný nosič'],
              ['Horské kolo a bikepacking', 'tašky na rám, řídítka a pod sedlo', 'uchycení bez nosiče, pevné řemínky, odolnost']]) +
          '<h2>Typy brašen a tašek</h2>'
          '<ul><li><strong>Brašny na zadní nosič</strong> mají největší kapacitu a tvoří základ cestovního vybavení. Jsou dostupné jako jednotlivé nebo párové.</li>'
          '<li><strong>Brašny na přední nosič</strong> jsou menší, vyvažují náklad vzadu a zlepšují stabilitu. Mění ale řízení, takže se je vyplatí vyzkoušet na kratší trase.</li>'
          '<li><strong>Tašky na rám</strong> využívají prostor mezi nohama. Drží pevné a nízké těžiště, ale omezují místo pro láhev a při zvedání nohy mohou překážet.</li>'
          '<li><strong>Tašky na řídítka</strong> nesou lehké a často používané věci: doklady, svačinu, mobil. Příliš těžký náklad vpředu zhoršuje řízení.</li>'
          '<li><strong>Podsedlové brašny</strong> jsou kompaktní a vhodné na nářadí a vložku. Nejsou určené pro těžké věci, protože zadní část kola by se rozkmitávala.</li>'
          '<li><strong>Košíky</strong> na řídítka nebo nosič jsou praktické pro městské jízdy, nákupy a psí kamarády, pokud je to přípustné.</li>'
          '<li><strong>Ledvinky a malé tašky</strong> doplňují cyklistický styl o věci na dosah ruky. Viz též <a href="/sportovni-tasky/">sportovní tašky</a>.</li></ul>'
          '<h2>Nosiče: zadní, přední a kompatibilita</h2>'
          '<p>Nosič musí sedět na rám, vidlici a kola. Zadní nosič se obvykle šroubuje do ok nad osou kola a do ok na sedlových trubkách. Kola bez ok, třeba některé silniční, gravel nebo celoodpružené modely, potřebují speciální uchycení, například na sedlovku nebo osu. Průměr kola (například 26, 27,5 nebo 28 palců) určuje velikost nosiče, takže si před nákupem ověřte, pro jaké kolo je určený.</p>'
          '<p>Kromě uchycení se řeší nosnost, kterou výrobce uvádí v popisu. Překročení této nosnosti není jen otázka životnosti: rozhoupaný a přetížený nosič ohrožuje bezpečnost. U karbonových rámů a elektrokol platí přísnější omezení, takže si ověřte doporučení výrobce kola. Při pochybnostech konzultujte servis. Montážní podložky a šrouby dotáhněte a po několika kilometrech znovu zkontrolujte.</p>'
          '<h3>Zadní nosič a pata</h3>'
          '<p>Brašny musí být na nosiči posazené tak, aby se při šlapání nedotýkaly paty. U kratších kol nebo velkých brašen se doporučuje posunout brašnu dozadu nebo zvolit užší typ. Ověřte také, že se nosič nedotýká blatníku a světel. Pro cestu s nosičem se hodí <a href="/cyklo-blatniky/">blatníky</a> a <a href="/cyklo-svetla/">světla</a> s dostatečným prostorem.</p>'
          '<h2>Uchycení brašen a rychlé systémy</h2>'
          '<p>Brašna drží na nosiči pomocí háčků nebo klipů, které se zahákou za trubky. Rychloupínací systémy se snadno sundávají a hodí se pro dojíždění, protože brašnu snadno vezmete s sebou. Pevnější systémy s přítlačnými háčky nebo pásky jsou stabilnější na nerovném povrchu. Zkontrolujte, že spodní zajištění brzdí kývání a že brašna na nosiči nedrnčí.</p>'
          '<h2>Voděodolnost a materiál</h2>'
          '<p>Brašny jsou z plachtoviny, nylonu nebo pogumovaných tkanin. Vodotěsné modely mívají svařované švy a roll-top zavírání, které se několikrát přehne a zapne. Voděodolné uzavírají zipem a po dlouhém dešti mohou prosáknout. Pokud potřebujete suchou elektroniku nebo spacák, vyplatí se vložit věci do vodotěsného pytle. Světlá a reflexní místa zvyšují viditelnost za šera. Pro viditelnost za šera ale reflexní prvky nestačí, doplňte je kvalitními <a href="/cyklo-svetla/">světly</a>.</p>'
          '<h2>Jak správně rozložit náklad</h2>'
          '<ol><li>Těžké věci dejte nízko a blízko osy kola.</li>'
          '<li>Rozdělte váhu mezi levou a pravou stranu, aby se kolo nenaklánělo.</li>'
          '<li>Lehké a objemné předměty (spacák, oblečení) patří nahoru nebo dozadu.</li>'
          '<li>Často používané věci uložte tam, kde na ně dosáhnete bez zastavení.</li>'
          '<li>Při vícedenní cestě zkuste zátěž před odjezdem a upravte ji.</li></ol>'
          '<p>Po naložení kolo vyzkoušejte při pomalé jízdě a při brzdění. Nedoporučuje se vozit těžké věci vysoko na zadním nosiči a také ne nést těžký batoh na zádech, když máte k dispozici nosič.</p>'
          '<h2>Batohy a alternativy</h2>'
          '<p>Kdo nechce montovat nosič, může použít <a href="/batohy/">batoh</a>, <a href="/mestske-batohy/">městský batoh</a> nebo <a href="/bezecke-vesty-a-batohy/">běžecký batoh</a>. Pro kratší výlety je to praktické. Při delších trasách však záda hřeje a unavuje. Přepravu nákladu odlehčí také brašny a <a href="/cyklo-sedacky-a-voziky/">dětské sedačky a vozíky</a>, pokud vozíte děti.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('rockbros', 'Rockbros'), ('topeak', 'Topeak'), ('deuter', 'Deuter'), ('m-wave', 'M-Wave'), ('ortlieb', 'Ortlieb'), ('basil', 'Basil'), ('force', 'Force'), ('acepac', 'Acepac'), ('fjallraven', 'Fjällräven'), ('max1', 'Max1'), ('author', 'Author'), ('west-biking', 'West Biking'), ('elops', 'Elops'), ('wozinsky', 'Wozinsky')) + '. Některé jsou zaměřené na cestovní brašny, jiné na městský styl, další na kompaktní tašky a doplňky. Porovnávejte parametry, ne jméno.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Po dešti brašnu vyndejte z nosiče, vysušte a uložte rozevřenou, aby se uvnitř nevytvořila plíseň.</li>'
          '<li>Špínu vytřete vlhkým hadrem, bez agresivních čisticích prostředků.</li>'
          '<li>Zipy občas očistěte a promažte vhodným prostředkem. Roll-top uzávěry zbavte písku.</li>'
          '<li>Šrouby nosiče a uchycení kontrolujte před každou delší jízdou.</li>'
          '<li>Při skladování nenechávejte brašny stlačené pod těžkými věcmi.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupit nosič bez ověření, zda sedí na rám, ok a velikost kol.</li>'
          '<li>Přetěžovat nosič nad nosnost, kterou výrobce uvádí.</li>'
          '<li>Zvolit brašnu bez vodotěsného zavírání pro deštivé cesty.</li>'
          '<li>Naložit těžký náklad vysoko a dozadu, kde zhoršuje stabilitu.</li>'
          '<li>Příliš velká taška na řídítka, která zakrývá světlo a brání řízení.</li>'
          '<li>Zapomenout na viditelnost: reflexní prvky a světla jsou základ.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého produktu uvidíte nabídky více obchodů a podle potřeby si zvolíte barvu, velikost nebo systém uchycení. Dále se podívejte na <a href="/cyklistika/">cyklistiku</a>, <a href="/jizdni-kola/">jízdní kola</a>, <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>, <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a> a <a href="/cyklo-udrzba/">údržbu</a>.</p>',
    faq=[('Jakou brašnu na nosič vybrat?', 'Podle délky cest a množství nákladu. Do města stačí jedna menší brašna s rychlým uchycením, na vícedenní cesty párové vodotěsné brašny. Ověřte, zda uchycení sedí na trubky vašeho nosiče.'),
         ('Jak poznám, jestli nosič sedí na moje kolo?', 'Zkontrolujte oka na rámu a vidlici, průměr kol a nosnost. Bez ok se používají nosiče upevněné na sedlovku nebo osu. U karbonových rámů a elektrokol dodržujte doporučení výrobce.'),
         ('Jaká je maximální nosnost nosiče?', 'Udává ji výrobce v popisu produktu i na samotném nosiči. Nepřekračujte ji, protože přetížení zhoršuje stabilitu a může nosič poškodit.'),
         ('Jsou cyklistické brašny vodotěsné?', 'Záleží na modelu. Vodotěsné mají svařované švy a roll-top zavírání, voděodolné jen odolávají dešti a po delším vystavení mohou propustit vodu. Citlivé věci vložte do vodotěsného pytle.'),
         ('Kam dát těžké věci?', 'Nízko a blízko osy kola, rovnoměrně na obě strany. Lehké a objemné věci patří nahoru a dozadu. Tak je kolo stabilnější a lépe se řídí.'),
         ('K čemu je taška na rám?', 'Využívá prostor mezi nohama a nese věci s nízkým těžištěm. Hodí se pro nářadí, svačinu a drobnosti, ale může překážet při šlapání nebo omezit místo pro láhev.'),
         ('Je lepší batoh, nebo brašna?', 'Na delší cesty brašny, protože odlehčí záda a zlepší pohodlí. Batoh je praktický na krátké vyjížďky a pro ty, kdo nechtějí montovat nosič.'),
         ('Jak často kontrolovat šrouby nosiče?', 'Před každou delší cestou a po prvních kilometrech po montáži. Šrouby se vibracemi mohou uvolnit a je dobré je prohlédnout.'),
         ('Mohu brašny používat na elektrokole?', 'Ano, ale sledujte nosnost nosiče a doporučení výrobce kola. Elektrokolo je těžší a rychlejší, takže bezpečné uchycení je ještě důležitější.'),
         ('Jak brašny čistit a skladovat?', 'Vlhkým hadrem a jemným mýdlem, po dešti osušit a uložit rozevřené. Zipy a roll-top zbavte písku a nenechávejte brašny stlačené nebo vlhké.'),
         ('Co ještě patří k výbavě na delší cestu?', 'Světla, zámek, pumpa a nářadí, blatníky a láhev s držákem. Vše najdete v kategoriích cyklo příslušenství, světla, zámky, pumpy a nářadí a blatníky.')],
)

# ------------------------------------------------------------------ salova-obuv
NEW['salova-obuv'] = dict(long=True,
    title='Sálová obuv: futsal, florbal, volejbal, házená | Sporteka',
    desc='Sálová obuv pro futsal, florbal, volejbal, házenou i badminton: podrážka, tlumení, velikost a péče. Průvodce výběrem a nabídky obchodů vedle sebe.',
    intro='<p><strong>Sálová obuv</strong> je vyrobená pro hladké povrchy hal a tělocvičen, kde potřebujete přilnavost, rychlé zastavení a bezpečné změny směru. Obyčejné tenisky nebo běžecké boty jsou na takový povrch často příliš klouzavé, zatímco boty s tmavou gumou mohou na světlé podlaze zanechávat stopy. Rozhoduje proto nejen značka, ale hlavně podrážka a styl hry.</p>'
          '<p>Na Sportece najdete <strong>sálové boty pro děti i dospělé</strong> na futsal a halový fotbal, florbal, volejbal, házenou, badminton i školní tělocvik. Související kategorie: <a href="/treninkova-obuv/">tréninková obuv</a>, <a href="/basketbalova-obuv/">basketbalová obuv</a>, <a href="/tenisova-obuv/">tenisová obuv</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>. Níže najdete postup, jak vybrat správný pár.</p>',
    guide='<h2>Jak vybrat sálovou obuv podle sportu</h2>'
          '<p>Různé halové sporty kladou na obuv odlišné nároky. Florbalista potřebuje nízký profil a stabilitu při rychlém běhu, volejbalista tlumení při doskoku, házenkář pevný sed a přilnavost při výskocích a obratech. Při výběru tedy začněte tím, co budete hrát nejčastěji, a teprve pak řešte barvu a design.</p>'
          + T(['Sport', 'Důležité vlastnosti', 'Na co dbát'], [
              ['Futsal a halový fotbal', 'plochá podrážka bez kolíků, pevný sed, odolné svrchní partie', 'dobrý grip na hale, odolnost proti otěru při kontaktu s míčem'],
              ['Florbal', 'nízká váha, přilnavá podrážka, ochrana boků', 'pevný sed paty, rychlé zastavení'],
              ['Volejbal', 'tlumení v přední části a patě, stabilita při doskoku', 'dobré držení kotníku, flexibilita špičky'],
              ['Házená', 'přilnavost, pevný sed a boční opora', 'robustní svršek, odolnost proti otěru'],
              ['Badminton a squash', 'lehká bota, přesné ovládání, boční stabilita', 'tenká podrážka, dobrý grip na hladkém povrchu'],
              ['Školní tělocvik a rekreace', 'univerzální podrážka, pohodlí, snadné obouvání', 'světlá podrážka, vhodná pro haly']]) +
          '<h2>Co dělá sálovou obuv jinou než běžnou</h2>'
          '<p>Nejvýznamnější rozdíl je v podrážce. Sálová obuv má většinou nízký a plochý profil z přírodní nebo syntetické gumy, která v hale dobře drží a přitom nepodkluzuje. Vzorek bývá hladký nebo jemně strukturovaný, protože hluboké vroubky pro venkovní terén by v hale zbytečně zachytávaly. Boty na venek mají tvrdší a hlubší podešev a halový povrch ničí.</p>'
          '<p>Druhým rozdílem je konstrukce svršku. Boční zesílení v oblasti palce a malíku zvyšuje stabilitu při bočním pohybu. Prodyšná tkanina chladí, vyztužené partie chrání proti otěru, který vzniká při smyku po podlaze. Výplň a tlumení pod patou a přední částí chodidla ulevuje kloubům při doskocích.</p>'
          '<h2>Podrážka: přilnavost, barva a pravidla haly</h2>'
          '<p>Světlá nebo průsvitná guma nezanechává na podlaze šmouhy a většina hal ji vyžaduje. Černá a tmavá guma může po sobě nechat stopy, takže si před koupí ověřte pravidla vaší haly nebo školy. Přilnavost se mění s čistotou podrážky: prach z podlahy ji zhoršuje, proto se podrážka občas otře vlhkým hadříkem. U sálových bot je normální, že na novém páru je podrážka ze začátku trochu kluzká, dokud se nezaběhne.</p>'
          '<h3>Tlumení a stabilita</h3>'
          '<p>Při výskocích a doskocích působí na klouby velká zátěž. Tlumení v patě a v přední části chodidla ji snižuje. Stabilita znamená, že bota drží chodidlo při rychlém pohybu do strany. Měkká bota je pohodlná, ale méně drží, tvrdší lépe vede. Nejlepší je zvážit styl hry: někdo potřebuje maximální obratnost, jiný ochranu kotníku.</p>'
          '<h2>Nízká, střední a vysoká bota</h2>'
          '<ul><li><strong>Nízká bota</strong> je lehká a nechává kotník volný. Hodí se pro florbal, badminton a hráče, kteří potřebují obratnost.</li>'
          '<li><strong>Střední bota</strong> trochu zpevňuje kotník a je kompromis mezi svobodou a oporou.</li>'
          '<li><strong>Vysoká bota</strong> pevně drží kotník. Používá se zejména v basketbalu, viz <a href="/basketbalova-obuv/">basketbalová obuv</a>, a u hráčů s citlivými kotníky.</li></ul>'
          '<p>Vysoký svršek ale zranění kotníku zcela nezabrání. Dobrý pocit z pevné boty by neměl nahradit protahování a posilování. Při opakovaných zraněních se poraďte s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Velikost a zkoušení</h2>'
          '<p>Zkoušejte boty odpoledne, kdy je noha mírně oteklá, a v ponožkách, které použijete při hře. Prsty by neměly narážet na špičku při zastavení, ale pata má sedět pevně. Dobře si vyzkoušejte krok do strany, krátký výskok a rychlé zastavení. Pokud pata prokluzuje nebo se na bocích objeví tlak, zkuste jinou velikost nebo širší střih.</p>'
          '<p>Dětské boty kupujte s rezervou asi centimetr, ale ne víc, aby se v botě dítě nehouplalo. Chodidlo roste rychle, proto kontrolujte velikost každé tři až čtyři měsíce. Na tělocvik se hodí lehká bota se suchým zipem nebo šněrováním, kterou se dítě naučí obouvat samo.</p>'
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p>Dámské boty bývají užší v patě a středu chodidla, pánské širší. Rozdíly mezi značkami jsou velké, takže se vyplatí řídit se tabulkou a zkoušet. Děti potřebují lehké a pevné boty, které se snadno obouvají a mají světlou podrážku. Pokud děti hrají i venku, pořiďte jim samostatné boty na hřiště, třeba z <a href="/sportovni-obuv/">sportovní obuvi</a> nebo <a href="/tenisky/">tenisek</a>.</p>'
          '<h2>Sálová obuv a další sporty</h2>'
          '<ul><li>Fanoušci míčových her najdou další vybavení v kategoriích <a href="/florbal/">florbal</a>, <a href="/volejbal/">volejbal</a>, <a href="/hazena/">házená</a> a <a href="/badminton/">badminton</a>.</li>'
          '<li>Na squash se vyplatí podívat do kategorie <a href="/squash/">squash</a>, kde jsou i další doplňky.</li>'
          '<li>Pro jiné povrchy slouží <a href="/kopacky/">kopačky</a> na trávu a umělý povrch.</li>'
          '<li>Na cvičení a posilování se hodí <a href="/treninkova-obuv/">tréninková obuv</a>.</li>'
          '<li>K doplnění patří <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('adidas', 'Adidas'), ('asics', 'Asics'), ('mizuno', 'Mizuno'), ('puma', 'Puma'), ('nike', 'Nike'), ('joma', 'Joma'), ('salming', 'Salming'), ('kensis', 'Kensis'), ('kempa', 'Kempa'), ('umbro', 'Umbro'), ('kanso', 'Kanso'), ('lotto', 'Lotto'), ('victor', 'Victor'), ('hummel', 'Hummel')) + '. Některé jsou specialisté na jednotlivé sporty, třeba na volejbal, házenou nebo badminton, jiné nabízejí univerzální modely. Střih a tlumení se mezi nimi liší, proto sledujte parametry konkrétního páru.</p>'
          '<h2>Péče o sálovou obuv</h2>'
          '<ul><li>Používejte ji jen v hale. Venkovní povrch zničí podrážku a zhorší přilnavost.</li>'
          '<li>Po tréninku boty vyvětrejte, vyndejte stélky a nechte je vyschnout při pokojové teplotě, ne na radiátoru.</li>'
          '<li>Podrážku občas otřete vlhkým hadříkem, aby neztratila přilnavost.</li>'
          '<li>Střídejte dva páry, pokud hrajete často. Obuv se tak lépe osuší a déle vydrží.</li>'
          '<li>Textilní svršek lze čistit jemným roztokem a měkkým kartáčem, v pračce jen pokud to dovoluje výrobce.</li>'
          '<li>Při opotřebení podrážky nebo ztrátě tlumení boty vyměňte, aby se nezvyšovalo riziko zranění.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Hrát v běžných běžeckých botách, které nedrží při bočním pohybu.</li>'
          '<li>Koupit tmavou podrážku do haly, kde je zakázaná.</li>'
          '<li>Zvolit příliš velkou velikost, ve které noha při zastavení klouže.</li>'
          '<li>Nosit sálové boty venku a zničit tak přilnavost.</li>'
          '<li>Podcenit tlumení u volejbalu, kde se často skáče.</li>'
          '<li>Jedny boty na všechno, i když se hraje několik sportů s různými nároky.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého páru najdete nabídky několika obchodů a velikosti skladem. Vyberte sport, značku a velikost a poté porovnejte. Další sportovní obuv najdete v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>, <a href="/micove-sporty/">míčové sporty</a> a <a href="/bezecka-obuv/">běžecká obuv</a>.</p>',
    faq=[('Čím se liší sálová obuv od běžecké?', 'Má plochou a přilnavou podrážku určenou pro hladký povrch a boční stabilitu při rychlých změnách směru. Běžecká bota je navržená pro dopředný pohyb a v hale může při bočním pohybu klouzat.'),
         ('Jakou sálovou obuv na florbal?', 'Lehkou a nízkou botu s přilnavou podrážkou a pevným sedem paty. Dbejte na boční stabilitu a zesílení v oblasti prstů, kde bota nejvíc trpí smykem.'),
         ('Co je důležité u volejbalové obuvi?', 'Tlumení při doskocích, pevné držení chodidla a flexibilní špička. Boty by měly dobře chránit klouby a umožnit rychlý pohyb do stran.'),
         ('Proč musí být podrážka světlá?', 'Světlá nebo průsvitná guma nezanechává na podlaze stopy a většina hal ji vyžaduje. Ověřte pravidla vaší haly nebo školy před nákupem.'),
         ('Mohu sálovou obuv nosit venku?', 'Nedoporučuje se. Venkovní povrch podrážku opotřebuje a zašpiní, takže v hale hůř drží. Pro hřiště používejte samostatnou obuv.'),
         ('Jak poznám správnou velikost?', 'Zkoušejte odpoledne v ponožkách, ve kterých budete hrát. Prsty nesmí narážet na špičku při zastavení a pata musí držet. Pomůže i krok do strany a krátký výskok.'),
         ('Je lepší nízká, nebo vysoká sálová bota?', 'Nízká je lehčí a svobodnější, vysoká více drží kotník. Záleží na sportu a zkušenostech. Při opakovaných problémech s kotníky se poraďte s lékařem nebo fyzioterapeutem.'),
         ('Jak často sálovou obuv měnit?', 'Když se podrážka opotřebuje do hladka, ztratí se tlumení nebo se svršek rozpadá. Při pravidelném tréninku to může být po několika měsících až letech, podle intenzity.'),
         ('Jak pečovat o podrážku?', 'Používejte boty jen v hale, občas podrážku otřete vlhkým hadříkem a boty nechte vyschnout při pokojové teplotě. Prach a špína přilnavost zhoršují.'),
         ('Jakou obuv pro děti na tělocvik?', 'Lehkou, s pevným sedem a světlou podrážkou, nejlépe se zapínáním, které si dítě zvládne samo. Velikost kupujte s rezervou asi centimetr a pravidelně kontrolujte.'),
         ('Kde najdu další vybavení na halové sporty?', 'V kategoriích florbal, volejbal, házená, badminton, squash a míčové sporty. Obuv doplní sportovní ponožky, bandáže a ortézy.')],
)


# ------------------------------------------------------------------ extensions (more guide sections, longer intros)
_SHOP = '<h2>Jak nakupovat na Sportece</h2>'


def _ext(slug, intro_add, guide_add):
    d = NEW[slug]
    d['intro'] = d['intro'].replace('</p>', ' ' + intro_add + '</p>', 1)
    d['guide'] = d['guide'].replace(_SHOP, guide_add + _SHOP, 1)


_ext('outdoorove-kalhoty',
     'Pomůžeme vám s tím, co dělat při výběru: od střihu přes sezónu až po velikost.',
     '<h2>Kalhoty na různé typy túr</h2>'
     '<p>Jednodenní výlet z auta zvládnou i lehčí kalhoty s několika kapsami. Na hřebenovku s plným batohem se hodí pevnější látka, která nepřichytává o skály a snese tření popruhů. Při vícedenní výpravě oceníte kalhoty, které rychle schnou po praní v potoce a netřou v rozkroku. V lese s hustým podrostem pomáhají hladké povrchy, na kterých se nezachytávají větvičky a trny. V horách s proměnlivým počasím se vyplatí vzít kalhoty s větrací funkcí a k nim lehké nepromokavé přes kalhoty.</p>'
     '<h2>Kalhoty do hor v zimě a na sněžnice</h2>'
     '<p>Zimní túra bez lyží je statičtější než sjezdovka. Při chůzi se tělo zahřívá, při zastávkách ztrácí teplo rychle. Proto se zimní outdoorové kalhoty obvykle kombinují s termoprádlem a podle potřeby se přidává nepromokavá vrstva. Vyšší zimní boty a <a href="/snezky/">sněžnice</a> vyžadují, aby se spodní okraj nohavic dal stáhnout nebo zasunout, a gamaše zabrání sněhu v prosypání do bot. Pro lyžování je vhodnější specializovaná kategorie lyžařských kalhot.</p>'
     '<h2>Barva, vzhled a praktické detaily</h2>'
     '<p>Zemité a tmavé tóny se hodí do přírody i do města a skryjí drobné skvrny. Světlé barvy jsou v létě chladnější, ale rychle se zašpiní. Reflexní prvky pomáhají při šerosvitu, třeba když se vracíte po setmění. Klasické detaily, jako poutko na karabinu, kapsa na mapu nebo odpružený pásek, jsou drobnosti, které při dlouhém dni ocení hlavně ti, kdo chodí často.</p>'
     '<h2>Kdy kalhoty vyměnit</h2>'
     '<p>Vyměňte je, když se protrhnou na místech, kde se trhlina nedá spravit, když se pružnost ztratí a kalhoty se vytahují, nebo když se látka rozpadá při praní. Menší trhlinky se dají zašít nebo zalepit záplatou. Když kalhoty přestanou odpuzovat vodu, často stačí nová impregnace, ne nový kus.</p>')

_ext('inline-brusle',
     'Pomůžeme vám vybrat správnou velikost, kolečka i ochranu pro bezpečnou jízdu.',
     '<h2>Vybavení pro dospělé, děti a rodiny</h2>'
     '<p>Rodiny často kupují brusle pro několik lidí najednou. Dospělý začátečník potřebuje pohodlné fitness brusle s dobrou oporou, dítě zase nastavitelný model, který se přizpůsobí růstu. Starší děti už tíhnou k modelům s lepším rámem a většími kolečky. Před nákupem zvažte, kde budete jezdit: pokud máte poblíž rovnou cyklostezku, vystačí si většina rodin s rekreačními bruslemi. V městských podmínkách s hrubým povrchem se hodí měkčí kolečka.</p>'
     '<h2>Terén a povrch</h2>'
     '<p>Brusle se nejlépe jezdí na hladkém, čistém asfaltu. Hrubý povrch, štěrk, listí a mokrá vozovka jsou nebezpečné, protože kolečko se zastaví na malém kamínku a jezdec letí dopředu. Dlažební kostky a obrubníky jsou problém pro většinu modelů. Při jízdě v blízkosti cyklistů a chodců dodržujte pravidla slušné jízdy: pozor na zatáčky, dostatečný odstup a včasné brzdění.</p>'
     '<h2>Brusle pro pokročilé a speciální styly</h2>'
     '<p>Kdo zvládá základy, může přejít k rychlostní jízdě na delších trasách, k jízdě městem se slalomem, k trikům nebo k agresivním stylům na rampách. Každá disciplína má vlastní konstrukci: rychlostní brusle mají dlouhý rám a velká kolečka, slalomové krátký rám a hladká kolečka, agresivní zpevněnou botu a rámy pro skluzy. Přechod na specializované brusle se vyplatí, až když vám stávající model začne jízdu omezovat.</p>'
     '<h2>Jak prodloužit život bruslí</h2>'
     '<p>Pravidelné otáčení koleček, čistá a promazaná ložiska a dotažené šrouby jsou základ. Brzdu vyměňte včas, jinak se začne stírat plastová konzola a ztratíte brzdný účinek. Po každé jízdě v mokru brusle osušte a při delším skladování je uložte v suchu. Boty vystavené slunci nebo mrazu vlivem teplotních výkyvů křehnou, takže je neskladujte v autě.</p>')

_ext('cyklo-tasky-a-nosice',
     'Nejdřív si ujasněte, kolik věcí skutečně potřebujete vozit, a teprve podle toho volte brašny a nosič.',
     '<h2>Kapacita: kolik litrů vlastně potřebujete</h2>'
     '<p>Kapacita brašen se udává v litrech. Pro dojíždění do práce vystačíte orientačně s 10 až 20 litry, tedy s malou brašnou, do které se vejde notebook, svačina a náhradní oblečení. Pro víkendový výlet s přespáním se počítá s párem brašen o celkové kapacitě zhruba 30 až 40 litrů, na vícedenní cesty se spacákem a stanem je potřeba kombinace zadních, předních a rámových brašen. Neplatí, že větší je vždycky lepší: nedoplněná brašna se při jízdě sesouvá a věci uvnitř drnčí. Vyberte velikost, kterou běžně zaplníte, a zbytek řešte upínacími pásky.</p>'
     '<h2>Bikepacking bez nosičů</h2>'
     '<p>Bikepacking je styl cestování s taškami připevněnými přímo na rám, řídítka a pod sedlo. Hodí se pro horská a gravel kola, která často nemají oka pro nosič. Výhodou je nízká hmotnost, úzký profil a lepší chování v technickém terénu. Nevýhodou je menší kapacita a nutnost pečlivě balit. Uchycení se děje pomocí řemínků s přezkami, proto je nutné pravidelně kontrolovat, zda se nepovolily a nebrousí o rám nebo kabely.</p>'
     '<h2>Městské kolo, košík a každodenní praktičnost</h2>'
     '<p>Ve městě rozhoduje pohodlí a rychlost. Košík na nosič nebo řídítka pojme nákup a malé zavazadlo, ale nezapomínejte na stabilitu: těžká taška vpředu stáčí řízení. Brašny s rychlým uchycením se po příjezdu snadno sundají, takže je nemusíte nechávat u zamčeného kola. Pro ochranu před krádeží kolo zamykejte spolehlivým <a href="/cyklo-zamky/">zámkem</a> a cennosti berte s sebou.</p>'
     '<h2>Kola s elektropohonem a dětské sedačky</h2>'
     '<p>Elektrokolo má vyšší hmotnost a zrychlení, takže nosič musí být dostatečně pevný a dobře ukotvený. Ověřte si, že brašny nezasahují do baterie a motoru a nekryjí světlo. Pokud vozíte dítě v sedačce, počítejte s tím, že nosnost nosiče se může sdílet. Informace najdete v popisech výrobců a v kategorii <a href="/elektrokola/">elektrokola</a>, případně <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>.</p>')

_ext('salova-obuv',
     'Pomůžeme vám zvolit správný model podle sportu, podrážky i velikosti.',
     '<h2>Jak často hrajete a jak náročně</h2>'
     '<p>Rekreační hráč, který chodí do haly jednou týdně, potřebuje spolehlivý univerzální model, který drží a nepodkluzuje. Pravidelný hráč v lize ocení lehčí a specializovanější obuv s lepším tlumením a stabilitou. Čím častěji hrajete, tím rychleji se opotřebuje podrážka a zhoršuje tlumení, takže se vyplatí zvážit dva páry ke střídání. U dětí rozhoduje spíš pohodlí a velikost než technické detaily.</p>'
     '<h2>Prevence zranění a rozcvičení</h2>'
     '<p>Obuv je jen jednou částí prevence zranění. Důležitá je i správná rozcvička, posilování kotníků a stabilizační cviky a dostatečná regenerace. Při bolestech kloubů, opakovaných vyvrtnutích nebo potížích s chodidly se vyplatí konzultace s lékařem nebo fyzioterapeutem, který doporučí vhodné vložky nebo ortézy. Obecné informace jsou jen orientační a nenahradí odborné vyšetření.</p>'
     '<h2>Stélky a vložky</h2>'
     '<p>Výrobce obvykle dodává základní stélku. Pokud potřebujete lepší tlumení nebo oporu klenby, lze ji vyměnit za vlastní vložku. Při výměně dbejte na to, aby bota po vložení vložky stále dobře seděla a nezmenšil se prostor pro prsty. Vložky a další doplňky najdete v kategorii <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
     '<h2>Sálová obuv a školní potřeby</h2>'
     '<p>Pro školní tělocvik platí jednoduché pravidlo: světlá podrážka, pevné zapínání a pohodlí. Škola často požaduje samostatný pár pro halu, aby se nezanášel venkovní špinou. Značení jména na jazyku nebo patě pomáhá proti záměně v šatně. Ke sportovní výbavě patří i <a href="/sportovni-tasky/">sportovní taška</a>, kam boty zabalíte do samostatné kapsy, aby neušpinily ostatní věci.</p>')

_ext('inline-brusle',
     '',
     '<h2>Jak se zvedat po pádu a jak padat</h2>'
     '<p>Pád patří k učení. Nejbezpečnější je padat dopředu na chrániče kolen a zápěstí, ne dozadu na ruce nebo hlavu. Při ztrátě rovnováhy snižte těžiště, pokrčte kolena a vezměte váhu dopředu. Po pádu se postavte na kolena, nasaďte jednu brusli na zem a odrazem druhé se zvedněte. Procvičte si to na měkkém povrchu, aby to bylo automatické, až to budete potřebovat. Děti se učí rychleji, když se pád jako hra procvičí s dohledem dospělého.</p>'
     '<h2>Bruslení jako doplněk jiných sportů</h2>'
     '<p>Inline brusle trénují rovnováhu, vytrvalost a sílu nohou, proto je oblíbené využívají i hokejisté, lyžaři nebo běžci. Pro letní přípravu se hodí také <a href="/hokejove-brusle/">hokejové brusle</a> či <a href="/bezecke-lyzovani/">běžecké lyžování</a> na kolečkách. Pro jiný typ pohybu najdete v nabídce <a href="/kolobezky/">koloběžky</a> a <a href="/skateboardy/">skateboardy</a>.</p>')

_ext('cyklo-tasky-a-nosice',
     '',
     '<h2>Bezpečnost na silnici s nákladem</h2>'
     '<p>Naložené kolo se chová jinak než prázdné. Brzdná dráha se prodlužuje, kolo se hůř vyvažuje a v zatáčkách je potřeba snížit rychlost. Nejdůležitější je zachovat viditelnost: zadní světlo nesmí být zakryté brašnou, reflexní prvky na brašnách pomáhají za šera. Dobrý je i zvonek a zrcátko, viz <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>. Před delší cestou zkuste pár kilometrů s plným nákladem, abyste zjistili, co drnčí nebo překáží.</p>'
     '<h2>Co sbalit na jednodenní a vícedenní cestu</h2>'
     '<p>Na výlet stačí náhradní duše, pumpa, základní nářadí, bunda proti dešti a dost pití. Na vícedenní cestu přibývá oblečení na převlečení, hygiena, jídlo a případně přístřeší. Vše dělte do menších vodotěsných pytlů, abyste se k věcem snadno dostali a mokro nezasáhlo zbytek. Užitečné jsou <a href="/plaste-a-duse/">pláště a duše</a> i <a href="/cyklo-pumpy-a-naradi/">nářadí</a>.</p>')

_ext('salova-obuv',
     '',
     '<h2>Jak poznat, že boty přestávají stačit</h2>'
     '<p>Varovné signály jsou hladká podrážka, která už nedrží, propadlá stélka, trhliny ve svršku a bolest chodidel nebo kolen po tréninku, která dříve nebyla. Boty ztrácejí tlumení postupně, takže si toho člověk nemusí hned všimnout. Pokud hrajete pravidelně, srovnejte starý pár s novým: rozdíl v pružnosti bývá zřetelný. Včasná výměna je levnější než dlouhá pauza kvůli zranění.</p>'
     '<h2>Jak sladit boty s dalším vybavením</h2>'
     '<p>Správné ponožky předcházejí puchýřům: vybírejte bezešvé a prodyšné, které odvádějí pot. U sportů s častými skoky může pomoci <a href="/bandaze-a-ortezy/">bandáž nebo ortéza</a>, vždy po konzultaci s odborníkem. Do haly se hodí lehké oblečení, které se nepřilepí na tělo a nebrání pohybu, například <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/sportovni-tricka/">sportovní trička</a>.</p>')
