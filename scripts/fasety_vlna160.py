"""sporteka.cz — facet landing texts wave 160: rieker-sandaly, damska-softshellova-bunda, panske-bezecke-boty, head-lyze.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ rieker-sandaly
NEW['rieker-sandaly'] = dict(
    title='Rieker sandály: pohodlná letní obuv na každý den',
    desc='Rieker sandály s měkkou stélkou a nastavitelným zapínáním. Jak vybrat velikost, kůži či syntetiku a čím se liší od Keen a Teva. Porovnejte nabídku obchodů.',
    intro='<p>Rieker je značka, kterou většina lidí zná jako pohodlnou městskou obuv na celý den, ne jako technický outdoor. Sandály Rieker proto patří do jiné poloviny kategorie <a href="/sandaly/">sportovních sandálů</a>: nejde o brodění potoků, ale o dlouhé dny na nohou na dovolené, ve městě, v práci nebo na zahradě. '
          'Typický pár má měkkou stélku, pružnou lehkou podrážku, kožené nebo syntetické pásky a zapínání na přezku či suchý zip. Většinu nabídky tvoří dámské střihy, vedle nich se objevují i pánské modely. '
          'Tato stránka vysvětluje, co od sandálů Rieker čekat, jak zvolit velikost a šířku, kdy sáhnout po kůži a kdy po syntetice, jak je udržovat a v čem se liší od značek jako Keen nebo Teva. Aktuální nabídku obchodů a dostupné velikosti najdete u konkrétních párů níže.</p>',
    guide='<h2>Pro koho jsou sandály Rieker</h2>'
          '<p>Značka staví na komfortu, ne na výkonu. To je důležité říct hned na začátku, protože slovo „sportovní“ v názvu kategorie svádí k očekávání trekové podrážky a ochranné špičky. U Riekeru je těžištěm lehká obuv pro lidi, kteří stráví hodně času chůzí po rovném povrchu: dovolená v historickém městě, procházky po promenádě, práce ve stoje, cesta do kanceláře v horkých dnech. '
          'Hodí se i pro ty, kdo mají citlivá chodidla, protože měkká stélka a pružná podešev jsou základem celého sortimentu.</p>'
          '<p>Naopak do hor, na kamenité stezky nebo do vody jsou vhodnější specializované značky. Najdete je v samostatných výběrech <a href="/sandaly-keen/">sandály Keen</a> a <a href="/teva-sandaly/">sandály Teva</a>. Kdo hledá oboje, kupuje obvykle dva páry: jeden městský a jeden terénní.</p>'
          + T(['Situace', 'Hodí se Rieker?', 'Poznámka'], [
              ['Městská procházka, dovolená u moře', 'ano', 'měkká stélka a nízká hmotnost jsou hlavní přednost'],
              ['Práce ve stoje, kancelář v létě', 'ano', 'elegantnější vzhled než u typických outdoorových sandálů'],
              ['Zahrada, chata, nákup', 'ano', 'snadno se obouvají, zapínání rychle nastavíte'],
              ['Celodenní túra v kamenitém terénu', 'spíš ne', 'chybí ochrana špičky a agresivní vzorek podrážky'],
              ['Brodění, vodní sporty', 'ne', 'kůže a měkké pěny po namočení ztrácejí tvar'],
              ['Dlouhý let a cestování s handicapem', 'ano', 'v lehkých, rozepnutelných sandálech otoky nohou tolik netlačí']]) +
          '<h2>Co obvykle sandály Rieker nabízejí</h2>'
          '<p>Sortiment je široký, ale několik prvků se opakuje. Podešev bývá lehká a pružná, často s lehkým klínkem nebo mírným převýšením paty, které chodidlo drží v přirozeném úhlu a odlehčuje Achillově šlaše. Svršek se skládá z několika pásků, někdy kombinovaných s perforací nebo pleteninou. Zapínání je na suchý zip, přezku nebo gumový pásek přes patu. Stélka bývá vystlaná měkčím materiálem a tvarovaná podle klenby.</p>'
          '<p>V nabídce se vyskytují také sandály bez pásku přes patu, tedy v podstatě pantofle s pásky přes nárt. Ty jsou pohodlné pro krátké použití, ale na delší chůzi je lepší pata uchycená. Když pata sjíždí dopředu, prsty se tlačí do přední části a po hodině chůze se objeví otlaky.</p>'
          '<ul><li><strong>Dva až tři body uchycení:</strong> nárt, patní pásek a případně kotník drží chodidlo i při delším pochodu.</li>'
          '<li><strong>Lehká podešev s klínkem:</strong> pohodlná na rovině, na kluzkém mokrém dlažebním kameni ale může klouzat.</li>'
          '<li><strong>Měkká stélka:</strong> příjemná od první minuty, časem se vlivem váhy tlačí do tvaru chodidla.</li>'
          '<li><strong>Syntetika a kůže:</strong> syntetika snáší vodu, kůže lépe dýchá a přizpůsobí se nohám.</li></ul>'
          '<h2>Kůže, nebo syntetika</h2>'
          '<p>V nabídce vedle sebe uvidíte kožené a syntetické páry a rozhodnutí se vyplatí promyslet. Kůže se po pár dnech nošení přizpůsobí tvaru nohy, dobře odvádí vlhkost a neutvrzuje pach tak rychle jako některé plasty. Nevýhodou je, že nesnáší opakované promočení: zaschne zkroucená, ztvrdne a může popraskat. Syntetika neboli textilní a plastové materiály jsou lehčí, rychleji schnou a snadno se otírají, ale prodyšnost bývá slabší a v horku se noha potí.</p>'
          + T(['Vlastnost', 'Kůže', 'Syntetika'], [
              ['Prodyšnost', 'dobrá', 'nižší, závisí na perforaci'],
              ['Přizpůsobení noze', 'po rozchození sedí lépe', 'drží tvar od začátku'],
              ['Odolnost proti vodě', 'omezená, nesušit na topení', 'snáší déšť i oplach'],
              ['Údržba', 'impregnace a krém', 'otření vlhkým hadříkem'],
              ['Hmotnost', 'o trochu vyšší', 'obvykle nižší'],
              ['Vzhled po sezóně', 'může patinovat', 'drží barvu, ale může se odírat']]) +
          '<p>Pro dovolenou u vody a výlety do města vybírejte syntetiku, na dlouhé dny ve městě a do kanceláře kůži. Dva páry na střídání vydrží déle než jeden nošený denně.</p>'
          '<h2>Velikost, šířka a vnitřní stélka</h2>'
          '<p>Sandály Rieker se u většiny modelů vyrábějí v evropských velikostech a vyplatí se řídit údajem o délce stélky v centimetrech, pokud ho obchod uvádí. Změřte chodidlo na konci dne, kdy je největší, a přidejte přibližně půl centimetru až centimetr. U sandálů je rezerva menší než u zavřených bot, protože prsty mohou lehce vyčnívat, ale špička nesmí sahat přes okraj stélky.</p>'
          '<p>Zvláštní pozornost si zaslouží šířka. Pokud máte širší nárt nebo vystouplou kost u palce, vybírejte páry se třemi nastavitelnými pásky nebo s pružnou pletenou částí. Pevný syntetický pásek bez možnosti úpravy tlačí a po celodenním nošení bolí. Pokud nosíte vložky nebo ortopedické stélky, vybírejte model s vyjímatelnou stélkou, aby se vložky vešly bez zvýšení nártu.</p>'
          '<ol><li>Změřte chodidlo večer a zaznamenejte délku v centimetrech.</li>'
          '<li>Porovnejte ji s údajem o stélce u konkrétního páru, ne jen s označením čísla.</li>'
          '<li>U přezek zvolte pár, u kterého zůstane po zapnutí ještě rezerva v obou směrech.</li>'
          '<li>Při prvním nošení zkuste nejprve hodinu chůze po bytě nebo po zahradě.</li>'
          '<li>Když se objeví tlak, vraťte pár dříve, než se podešev znečistí venkem.</li></ol>'
          '<h2>Rieker a další značky sandálů</h2>'
          '<p>V kategorii je vedle Riekeru velký výběr značek a hodí se vědět, v čem se liší. <a href="/sandaly-keen/">Keen</a> a <a href="/teva-sandaly/">Teva</a> vsázejí na výrazný vzorek podrážky, stabilnější konstrukci a terénní použití. <a href="/sandaly-crocs/">Crocs</a> jsou lehké a snadno omyvatelné, nejblíže pantoflím. <a href="/birkenstock-sandaly/">Birkenstock</a> a <a href="/geox-sandaly/">Geox</a> se zaměřují na ortopedicky tvarované stélky a prodyšnost.</p>'
          '<p>Rieker je mezi nimi kompromis pro každodenní nošení: lehčí a elegantnější než terénní sandály, výraznější v designu než plážová obuv. Pokud kupujete sandály pro děti, otevřete rovnou <a href="/detske-sportovni-sandaly/">dětské sportovní sandály</a>, protože pro ně platí jiná pravidla uchycení, a pro ženy hledající širší srovnání je určená stránka <a href="/damske-sportovni-sandaly/">dámské sportovní sandály</a>.</p>'
          '<h2>Péče, aby vydržely víc než jedno léto</h2>'
          '<p>Většina sandálů se nezničí chůzí, ale špatným uložením a čištěním. Kůži čistěte vlhkým hadříkem, nikdy ji nenamáčejte do vody a nesušte na radiátoru ani na slunci. Po zaschnutí ji ošetřete krémem nebo impregnací, aby nepraskala. Syntetické pásky stačí otřít vlažnou vodou s malým množstvím mýdla. Suchý zip pravidelně vyčistěte kartáčkem od písku a vlasů, jinak přestane držet. Stélku občas vyndejte a nechte vyvětrat, čímž omezíte zápach.</p>'
          '<p>Na konci sezóny uložte sandály na suchém a tmavém místě, ne v igelitu. Pokud se podešev odlepuje, zajděte k obuvníkovi hned, dokud je poškození malé; později se oprava prodražuje a někdy už nejde provést.</p>'
          '<h2>Jak sandály kombinovat</h2>'
          '<p>Díky střídmému designu se sandály Rieker nosí k lněným kalhotám, džínovým šortkám, šatům i k lehkým sukním. Tmavé a béžové odstíny se snadno kombinují s většinou letního šatníku, bílé a světlé pásky působí svěže, ale jsou náročnější na čištění. Barevné kombinace, například modrá se šedou, oživí jednobarevný outfit. Do kanceláře s přísnějším dress codem vybírejte pár bez výrazných přezek a s uzavřenější patou.</p>'
          '<h2>Kdy kupovat a na co si dát pozor v nabídce</h2>'
          '<p>Sandály se nejčastěji prodávají na jaře a v létě, nejširší výběr velikostí mívají obchody na začátku sezóny. Na konci léta se zboží vyprodává a vybrat lze už jen málo čísel. Kdo hledá konkrétní velikost, měl by objednávat dřív. U označení modelu, třeba čísla v názvu, hledejte stejné číslo napříč obchody, protože jedna a ta samá podešev se prodává pod více popisy a barvami.</p>'
          '<p>Při srovnání dávejte pozor na název barvy. Stejný model se v jednom obchodě jmenuje bílý a v jiném krémový, a pokud barvu hledáte přesně, rozhodnou o ní fotografie. Pokud potřebujete sandály na výlet a do vody, poohlédněte se i v kategorii <a href="/obuv-do-vody/">obuv do vody</a>; pokud hledáte zavřenou obuv na chladnější dny, pomůže <a href="/sportovni-obuv/">sportovní obuv</a>.</p>',
    faq=[
        ('Jsou sandály Rieker vhodné na dlouhé chození?',
         'Na městské procházky a dovolenou ano, jsou lehké a mají měkkou stélku. Na celodenní túru v terénu ale chybí ochrana špičky i agresivní vzorek podrážky, tam patří trekové sandály.'),
        ('Jak poznám správnou velikost sandálů Rieker?',
         'Změřte chodidlo večer, přidejte přibližně půl až jeden centimetr a porovnejte s délkou stélky u konkrétního páru. Označení čísla není u všech modelů stejné, proto se řiďte centimetry, pokud je obchod uvádí.'),
        ('Mají Rieker sandály užší, nebo širší střih?',
         'Střih se liší podle modelu. U pásků na suchý zip nebo přezky si šířku nastavíte, u pevných syntetických pásků ne. Pokud máte široký nárt, zvolte pár s více nastavitelnými body.'),
        ('Dají se Rieker sandály nosit k ortopedickým vložkám?',
         'Pokud mají vyjímatelnou stélku, ano. Vyjměte originální vložku a nahraďte ji svou, aby se nezvýšil nárt. U modelů se stélkou zalepenou je to složité a pár se může stát těsným.'),
        ('Kůže, nebo syntetika: co je lepší do horka?',
         'Kůže lépe dýchá a přizpůsobí se noze, takže se hodí na dlouhé dny ve městě. Syntetika je lehčí, rychle schne a snese déšť, ale v parnu se v ní noha více potí.'),
        ('Jak vyčistit kožené sandály?',
         'Otřete je vlhkým hadříkem, nenamáčejte je a nesušte na topení. Po zaschnutí použijte krém nebo impregnaci. Znečištěný suchý zip vykartáčujte, jinak přestane držet.'),
        ('Čím se Rieker liší od Keen a Teva?',
         'Rieker staví na lehkosti a vzhledu pro každodenní nošení, Keen a Teva na terénní podrážce, ochraně špičky a pevném uchycení. Pokud chodíte převážně po městě, stačí Rieker; do přírody vezměte terénní značku.'),
        ('Dají se sandály Rieker nosit s ponožkami?',
         'Dají, hlavně v chladnějších dnech na jaře a na podzim. Zvolte tenké ponožky bez švů, které nevytvoří vyvýšeninu pod páskem. Zapínání pak nastavte o malý kousek volněji.'),
        ('Kdy je nejlepší doba na nákup letních sandálů?',
         'Největší výběr velikostí bývá na začátku sezóny, výprodeje přicházejí na konci léta, ale často už jen v méně obvyklých velikostech. Kdo chce konkrétní barvu a číslo, nakupuje dřív.'),
        ('Je lepší pár s pásky přes patu, nebo bez nich?',
         'Pro delší chůzi je lepší pata uchycená, protože chodidlo neujíždí dopředu a prsty netlačí do špičky. Pantofle bez zadního pásku jsou pohodlné jen na krátké využití, třeba na terasu nebo do bazénu.')])

# ------------------------------------------------------------------ damska-softshellova-bunda
NEW['damska-softshellova-bunda'] = dict(
    title='Dámská softshellová bunda: střih, vrstvení a výběr',
    desc='Dámská softshellová bunda s přiléhavým střihem a tvarovaným pasem. Jak vybrat velikost a zateplení pro túry, běh i město a porovnat nabídky obchodů.',
    intro='<p>Dámská softshellová bunda je nejčastější vrstva žen na podzim a na jaře: dost pružná na pohyb, dost hustá na vítr a dost úzká, aby se pod ní vešel fleece nebo funkční triko. '
          'Od pánské verze se liší nejen barvami. Ženský střih počítá s užšími rameny, kratšími rukávy, o něco delším tělem a tvarováním v pase i bocích, takže se v ní chodí líp než v unisex bundě o dvě čísla menší. '
          'Na této stránce najdete dámské modely z kategorie <a href="/softshellove-bundy/">softshellové bundy</a> od turistických i městských značek. Průvodce rozebírá střih, velikosti, zateplení, kapuce, kapsy a použití pro túry, běžky, kolo i každodenní nošení. Nabízíme také odkazy na příbuzné výběry, aby se nabídka dala rychle zúžit.</p>',
    guide='<h2>Čím se dámský softshell liší od pánského</h2>'
          '<p>Rozdíl je především v konstrukci, ne v tkanině. Materiál bývá stejný: pružný polyester nebo polyamid s elastanem, někdy s větrnou membránou, vnitřní strana hladká nebo česaná. Střih se ale liší v několika bodech, které se při chůzi poznají okamžitě.</p>'
          + T(['Část bundy', 'Dámský střih', 'Co to znamená v praxi'], [
              ['Ramena a průramky', 'užší, nasazené blíže ke krku', 'nesjíždějí ze štíhlých ramen a netlačí v podpaží'],
              ['Rukávy', 'kratší, užší v předloktí', 'nepřebývají přes zápěstí, rukavice se vejdou pod manžetu'],
              ['Pas a boky', 'zúžený pas, volnější okolo boků', 'bunda sedí tvarovaně, ale nepřitahuje se u sedu'],
              ['Délka těla', 'často o něco delší vzadu', 'kryje bedra při předklonu nebo při jízdě na kole'],
              ['Hrudník', 'prostor odpovídající ženské postavě', 'zip se nepruží a nesjíždí do strany'],
              ['Kapuce', 'menší nebo odnímatelná', 'nezakrývá výhled a lépe padne přes helmu či čepici']]) +
          '<p>Pokud vás zajímá opačná varianta, najdete ji ve výběru <a href="/softshellova-bunda-panska/">pánská softshellová bunda</a>. Pro dívky, které ještě rostou, je určena kategorie <a href="/detska-softshellova-bunda/">dětská softshellová bunda</a> s rezervou v rukávech a v těle.</p>'
          '<h2>Velikost a zkouška na těle</h2>'
          '<p>Ženské velikosti se v obchodech zapisují dvěma způsoby: písmeny od XS po XL, někdy po XXL, nebo číselnou řadou, která začíná kolem 34 a pokračuje po dvou. Mezi značkami se přepočty liší, a proto se vyplatí změřit hrudník, pas a boky a porovnat je s tabulkou u konkrétního kusu. Při pochybnostech hledejte v popisu údaj o délce bundy a rukávu, ten často rozhodne víc než samotné písmeno.</p>'
          '<ul><li><strong>Přiléhavost:</strong> softshell má sedět blíže tělu než péřovka. Pod ním má zůstat místo na jedno tenké a jedno střední vrstvení, ne na objemný svetr.</li>'
          '<li><strong>Zvednutí rukou:</strong> předpažte a zvedněte ruce nad hlavu; dolní okraj bundy se nemá vyhrnout nad pas.</li>'
          '<li><strong>Rukávy:</strong> po natažení paží má manžeta končit na zápěstí, ne nad ním.</li>'
          '<li><strong>Prsa a ramena:</strong> zip je zapnutý bez tahu, rameno nepřečnívá.</li>'
          '<li><strong>Sezení:</strong> v sedu se bunda nesmí zařezávat do boků a zip nemá dráždit bradu.</li></ul>'
          '<h2>Zateplení, membrána a větruodolnost</h2>'
          '<p>U dámských softshellů se nabídka dělí na tři skupiny. Lehká bunda bez membrány je prodyšná a hodí se na rychlý pohyb. Bunda s větrnou membránou chrání lépe, ale hůř odvádí pot, takže se v ní vyplatí větrat zipy. Zateplený softshell s česaným vnitřkem nahrazuje fleece a je vhodný na chladnější dny kolem bodu mrazu. Nepokoušejte se jediným kusem pokrýt všechna počasí: jeden z extrémů vždy zklame.</p>'
          + T(['Typ dámského softshellu', 'Hodí se na', 'Nehodí se na'], [
              ['Lehký bez membrány', 'rychlou chůzi, běh, jaro a podzim', 'silný vítr a trvalý déšť'],
              ['S větrnou membránou', 'vyšší hory, kolo, běžky', 'intenzivní pohyb v teple'],
              ['Zateplený česaný', 'chladné dny, město, pomalejší túry', 'vysoký tep, horké dny'],
              ['Hybridní s odlišnými panely', 'dlouhé túry s batohem', 'ležérní městské nošení'],
              ['S odnímatelnou kapucí', 'proměnlivé počasí', 'vítr bez pevně sedící kapuce']]) +
          '<p>Voděodolná povrchová úprava zadrží jen krátký déšť a mokrý sníh. Při několikahodinovém lijáku bunda nasákne, proto do batohu patří i lehká <a href="/nepromokave-bundy/">nepromokavá bunda</a>. Naopak když je chladno bez deště, může softshell nahradit těžší bundy a kombinovat se s teplou vrstvou z kategorie <a href="/zimni-bundy/">zimní a péřové bundy</a>.</p>'
          '<h2>Na co se použití liší</h2>'
          '<p>Stejný softshell se jinak chová na túře, při běhu a ve městě. Proto zvažte, kde budete bundu nosit nejčastěji.</p>'
          '<ul><li><strong>Turistika:</strong> kapuce přes čepici, kapsa na zip na mapu nebo telefon, ventilační otvory pod pažemi, popruh batohu nesmí tlačit na zip.</li>'
          '<li><strong>Běžecké lyžování:</strong> bunda bez objemných švů na ramenou, s pružnými manžetami a zadní kapsou nebo prodlouženým zadním dílem. V nabídce se objevují modely značek zaměřených na běžky, například Swix.</li>'
          '<li><strong>Cyklistika a gravel:</strong> zadní díl delší, aby kryl bedra při předklonu, reflexní prvky a kapsy dostupné i s číslem na řídítkách.</li>'
          '<li><strong>Běh:</strong> lehká tenká tkanina s prodyšnými panely, kapuce bez šňůrek, pevný zip bez zadrhávání.</li>'
          '<li><strong>Město:</strong> decentní barva, hladký povrch a rovný střih, který se dobře nosí s šálou.</li></ul>'
          '<h2>Vrstvení pod softshell na celý rok</h2>'
          '<p>Softshell je střední až vnější vrstva a skutečně funguje v kombinaci. Zdola funkční triko nebo tenké merino, nad ním podle teploty tenký fleece, a teprve pak bunda. Při chůzi vzhůru stačí triko a softshell, protože tělo vyrábí teplo. Na rozhledně nebo na přestávce si přes ni přehoďte péřovou vestu nebo bundu, aby vás neuchladil pot. Chladnější dny se řeší přidáním tenké vrstvy, ne koupí těsnější velikosti, protože tlačící bunda omezuje pohyb a stlačuje izolační vzduch.</p>'
          '<p>Příjemným doplňkem jsou lehké rukavice a čepice či čelenka. Hrdlo při větru chrání tubulární šátek, který se nosí i jako čelenka. Kapuce bez pevného stažení se při větru nafoukne, proto vyzkoušejte šňůrku nebo gumu v obličejové části.</p>'
          '<h2>Menší a vyšší postavy, těhotenství a tvarování</h2>'
          '<p>U menších žen bývá potíž s délkou rukávů a těla: bunda ve velikosti S je stále příliš dlouhá, a tak se vyplatí hledat modely s údajem o délce rukávu a případně manžety s možností zúžení. Vyšší ženy naopak hledají delší zadní díl a delší rukáv a mnohdy musejí zvolit pánský střih nebo větší velikost. V těhotenství se hodí volnější softshell o číslo větší a s pružným materiálem nebo s možností rozepnutí zdola, přičemž bundu nezapínejte tak, aby tlačila na břicho.</p>'
          '<h2>Značky v dámské nabídce</h2>'
          '<p>V nabídce jsou domácí i zahraniční značky outdoorového oblečení: ' + B(('kilpi', 'Kilpi'), ('husky', 'Husky'), ('loap', 'Loap'), ('alpine-pro', 'Alpine Pro'), ('hannah', 'Hannah'), ('northfinder', 'Northfinder'), ('regatta', 'Regatta'), ('trespass', 'Trespass'), ('columbia', 'Columbia')) + '. '
          'České a slovenské značky stavějí na poměru ceny a výbavy a nabízejí široké barevné řady. Ze zahraničních vybírají ženy často ' + B(('haglofs', 'Haglöfs'), ('dynafit', 'Dynafit'), ('siroko', 'Siroko')) + ', které se orientují na náročnější sport a vyšší cenovou hladinu.</p>'
          '<p>Kdo vybírá podle značky, může pokračovat ve výběrech <a href="/softshellova-bunda-kilpi/">softshellová bunda Kilpi</a> a <a href="/alpine-pro-softshellova-bunda/">Alpine Pro softshellová bunda</a>. Každá značka má trochu jiný střih, a proto se vyplatí zkontrolovat tabulku velikostí zvlášť.</p>'
          '<h2>Barva a údržba</h2>'
          '<p>Světlé odstíny, například béžová, mentolová nebo růžová, jsou ve městě osvěžující, ale rychle se špiní od batohu a zipů. Tmavá modrá a černá jsou praktičtější a snáze se kombinují. Do hor se hodí sytá barva, díky níž vás v případě nehody snáz objeví záchranáři i parta na stezce. Při praní dodržujte pokyny na štítku: obvykle jde o třicet stupňů, bez aviváže a bez sušení v bubnu. Aviváž ucpává póry tkaniny a ničí voděodolnou impregnaci, kterou je po několika praních vhodné obnovit sprejem nebo pracím přípravkem.</p>'
          '<p>Před uložením bundu vyvětrejte, zapněte zip a pověste na ramínko, nikoli sbalenou v batohu. Při dlouhém skladování ji nenechávejte v plastovém sáčku, kde by se držela vlhkost.</p>'
          '<h2>Jak nakupovat v nabídce obchodů</h2>'
          '<p>Stejný model se v obchodech prodává pod trochu jiným názvem a barvou, proto sledujte číselný kód v názvu. Pozor na střih označený jako unisex nebo pánský, který se v dámské kategorii občas objeví. Při srovnání pomáhá údaj o hmotnosti a složení tkaniny, který bývá v popisu. Sezónní dopředné nákupy se vyplatí na konci zimy a na jaře, kdy se rozprodávají zateplené kusy. Pokud hledáte spíš lehčí vrstvu na teplejší dny, zvažte také <a href="/sportovni-bundy-jaro-podzim/">sportovní bundy na jaro a podzim</a> a pro kombinaci pod bundu <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>',
    faq=[
        ('Jakou velikost dámské softshellové bundy zvolit?',
         'Změřte hrudník, pas a boky a porovnejte s tabulkou konkrétní značky, protože písmena nejsou jednotná. Bunda má sedět blíže tělu a pod ní má zůstat místo na tenké a střední vrstvení.'),
        ('Je dámský softshell opravdu jiný než pánský?',
         'Ano, hlavně střihem. Rukávy jsou kratší, ramena užší, pas zúžený a boky volnější. Tkanina bývá stejná, ale bunda sedí v místech, kde má pánská volný prostor.'),
        ('Zadrží softshell déšť?',
         'Jen krátký déšť nebo mokrý sníh, protože povrch je impregnovaný, ale nenarušený membránou. Při dlouhém lijáku nasákne, proto do batohu patří i nepromokavá vrstva.'),
        ('Co si obléknout pod softshellovou bundu?',
         'Funkční triko a tenký fleece nebo merino vrstvu. Bavlna se potí a drží vlhkost, takže v chladnu zebe. Při mrazu přidejte teplejší střední vrstvu, ale bunda nesmí být těsná.'),
        ('Kdy zvolit softshell se zateplením a kdy bez?',
         'Zateplený česaný vnitřek se hodí kolem nuly a při pomalém pohybu, lehký bez zateplení na rychlou chůzi, běh a jarní dny. Při vyšším tepu se zateplený model snadno přehřívá.'),
        ('Jak softshell vyprat?',
         'Obvykle na třicet stupňů, bez aviváže a bez bubnové sušičky. Zapněte zipy a vyčistěte suchý zip. Po několika praních obnovte impregnaci sprejem nebo prostředkem do pračky.'),
        ('Hodí se softshell na běžky?',
         'Ano, zvlášť lehčí s větrnou membránou nebo s odnímatelnými rukávy. Důležité jsou pružné manžety, žádné objemné švy na ramenou a prodyšnost. Při rychlé jízdě se přehřátí hlavně na zádech.'),
        ('Je lepší mít kapuci, nebo bez ní?',
         'Kapuce se hodí do hor a při větru. Do města a při běhu někomu překáží, proto pomůže odnímatelná. Zkuste, zda se dá přetáhnout přes čepici nebo helmu a nezakrývá výhled.'),
        ('Můžu nosit softshell celoročně?',
         'V mírných měsících ano, v zimě jen jako střední nebo vnější vrstvu spolu s teplým doplňkem. V létě se v ní zapaří, a tak si do batohu zabalte lehkou větrovku.'),
        ('Kolik kapes by měla dámská softshellová bunda mít?',
         'Nejpraktičtější jsou dvě boční kapsy na zip a jedna na hrudi na telefon nebo karty. Kapsy bez zipu se hodí jen do města, na túře v nich snadno ztratíte klíče.')])

# ------------------------------------------------------------------ panske-bezecke-boty
NEW['panske-bezecke-boty'] = dict(
    title='Pánské běžecké boty: velikost, tlumení a výběr podle běhu',
    desc='Pánské běžecké boty pro silnici, trail i závody. Rozdíly oproti dámským, šířka a velikost, tlumení podle váhy a tempa a značky. Porovnejte nabídky obchodů.',
    intro='<p>Pánské běžecké boty se od dámských neliší jen barvou. Staví se na širší kopyto, vyšší objem nártu a větší rozsah velikostí a počítají s tím, že průměrný běžec je těžší. To mění požadavky na tlumení, stabilitu i trvanlivost podešve. '
          'Na této stránce jsou boty z kategorie <a href="/bezecka-obuv/">běžecká obuv</a> určené mužům: silniční tréninkové, tempové a závodní modely, trailové s hrubým vzorkem i lehké boty na každodenní kilometry. '
          'Průvodce vysvětluje, jak vybrat velikost podle délky a šířky chodidla, jakou tvrdost pěny zvolit podle hmotnosti a tempa, kdy se vyplatí kupovat dva páry a které značky co nabízejí. Pokud hledáte užší střih, přejděte na <a href="/bezecke-boty-damske/">dámské běžecké boty</a>.</p>',
    guide='<h2>V čem se muž v botě liší od ženy</h2>'
          '<p>Rozdíl není jen v číslech. Mužské chodidlo je v průměru delší, širší v přední části a širší v patě, nárt bývá vyšší a kotník silnější. Výrobci proto pro pánské modely používají jiné kopyto a lehce odlišnou geometrii. Dámská verze téhož modelu bývá užší v patě i ve středu a v menších velikostech, často s měkčí pěnou, protože ženy bývají lehčí.</p>'
          + T(['Oblast', 'Pánský model', 'Důsledek při výběru'], [
              ['Kopyto', 'širší přední část a pata', 'vyšší komfort pro silnější nohu, ale u úzkého chodidla sjíždí pata'],
              ['Rozsah velikostí', 'zhruba od 40 do 49 i víc', 'velká čísla mají v obchodech menší výběr'],
              ['Mezipodešev', 'tužší nebo hustší pěna pro vyšší hmotnost', 'méně se propadá, ale působí tvrději'],
              ['Nárt a jazyk', 'vyšší prostor', 'šněrování je volnější, stačí lehčí tah'],
              ['Barvy', 'výrazné tmavé a neonové odstíny', 'vzhled neovlivní běžeckou vlastnost'],
              ['Unisex označení', 'často se prodává stejný pár jako pánský', 'ženy z něj mívají o 1,5 až 2 čísla menší velikost']]) +
          '<p>Unisex značení u některých značek znamená, že stejná bota se prodává v pánské a dámské řadě s odlišným číslováním. Při přepočtu hledejte tabulku výrobce a vždy porovnejte délku stélky v centimetrech, ne jen číslo.</p>'
          '<h2>Jak vybrat velikost a šířku</h2>'
          '<p>Při běhu se chodidlo prodlužuje a nárt otéká, takže bota musí mít před palcem rezervu zhruba šířky palce, tedy asi centimetr až centimetr a půl. Měřte odpoledne po zátěži. Špička má být tak široká, aby se prsty mohly rozevřít, jinak vznikají puchýře a černé nehty. Pata drží pevně, ale nesmí tlačit na Achillovu šlachu.</p>'
          '<ul><li><strong>Délka:</strong> nechte si před palcem jedno prstové místo a zkontrolujte, zda se při sestupu prsty nezarazí o špičku.</li>'
          '<li><strong>Šířka:</strong> u modelů s označením wide nebo široké kopyto zkoušejte první, pokud vás tlačí malíček nebo zevnitř palec.</li>'
          '<li><strong>Pata:</strong> při sjezdu z kopce nesmí vyklouznout, pomůže tužší pata nebo zapnutí patního oka na tkaničce.</li>'
          '<li><strong>Nárt:</strong> tlak od tkaniček řešte vynecháním oka, ne uvolněním pod nárt.</li>'
          '<li><strong>Zimní a dlouhé běhy:</strong> ponožky silnější nebo zateplené vyžadují o půl čísla víc.</li></ul>'
          '<h2>Tlumení podle hmotnosti a tempa</h2>'
          '<p>Hmotnost běžce ovlivňuje, jak se pěna stlačuje. Těžší muž stlačuje stejnou pěnu hlouběji než lehký, proto se pro vyšší váhu hodí širší základna a hustší nebo vyšší mezipodešev. Naopak lehký, rychlý běžec ocení tenčí a pružnější pěnu s hmotností pod průměrem, protože vyšší bota by mu bránila v rychlém odrazu. Rozhodnutí vždy odvozujte od typické jednotky, ne od jediné závodní chvíle.</p>'
          + T(['Typ běžce', 'Doporučený směr', 'Čeho se vyvarovat'], [
              ['Začátečník do osmdesáti kilogramů', 'neutrální tréninková bota se středním tlumením', 'příliš lehkých závodních bot'],
              ['Těžší běžec', 'vysoké tlumení a široká stopa', 'úzkých minimalistických bot na dlouhé trasy'],
              ['Rychlý tréninkový běžec', 'lehčí tempová bota s pružnou pěnou', 'měkkých bot, které ubírají odraz'],
              ['Běžec s propadáním kotníku', 'stabilní model s pevnější vnitřní stranou', 'vysokých měkkých modelů bez stabilizace'],
              ['Terénní běžec', 'trailová bota s vyšším vzorkem a ochranou špičky', 'silničních bot na mokrých kořenech']]) +
          '<h2>Silnice, nebo trail</h2>'
          '<p>Kdo běhá převážně po asfaltu, vybírá z <a href="/silnicni-bezecke-boty/">silničních běžeckých bot</a>, jejichž podešev je hladká a odolná proti otěru. Kdo vyrazí do lesa, potřebuje <a href="/trailove-boty/">trailové boty</a> s vyšším vzorkem a pevnější špičkou. Trailové modely se v sortimentu pánských bot objevují od značek jako Salomon, Merrell, La Sportiva, Dynafit nebo Craft. Hybridní boty se hodí pro kombinované trasy po zpevněných cestách a poli.</p>'
          '<p>Mezi trailovými botami rozhoduje ještě konstrukce. Bota pro suchý terén má méně membrán a dýchá, bota s membránou GORE-TEX zadrží vodu a sníh, ale v teple přehřívá. Zimní běžec ji ocení, letní ne.</p>'
          '<h2>Značky v pánské nabídce</h2>'
          '<p>Nabídka je široká a každá značka má jiný střih a filozofii. ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('asics', 'Asics'), ('new-balance', 'New Balance'), ('puma', 'Puma'), ('mizuno', 'Mizuno'), ('under-armour', 'Under Armour')) + ' pokrývají silniční tréninkové a závodní modely, ' + B(('salomon', 'Salomon'), ('merrell', 'Merrell')) + ' patří mezi nejviditelnější v terénu a ' + B(('on', 'On'), ('skechers', 'Skechers'), ('joma', 'Joma')) + ' nabízejí lehčí nebo cenově dostupnější řady.</p>'
          '<p>Chcete-li si značku vybrat, použijte přehledy <a href="/nike-bezecke-boty/">Nike běžecké boty</a>, <a href="/adidas-bezecke-boty/">Adidas běžecké boty</a>, <a href="/bezecke-boty-asics/">Asics</a>, <a href="/bezecke-boty-hoka/">Hoka</a>, <a href="/new-balance-bezecke-boty/">New Balance</a> nebo <a href="/salomon-bezecke-boty/">Salomon</a>. Každá značka má v kopytě jiný obrys: Nike bývá užší, Asics a New Balance širší v přední části a Hoka rozměrnější v celkovém objemu.</p>'
          '<h2>Kolik párů a jak často měnit</h2>'
          '<p>Pěna v mezipodešvi ztrácí pružnost dřív než podešev vypadá opotřebovaně. Jako orientace slouží několik set kilometrů, u těžších běžců méně, u lehkých více. Praktické znamení je únava lýtek a bolest holení po kratším běhu, která dříve nebyla. Zkušení běžci střídají dva páry: jeden měkčí na dlouhé a jeden pevnější na kratší rychlé tréninky. Střídání prodlužuje životnost obou párů a snižuje riziko přetížení, protože noha je opakovaně zatěžována lehce odlišně.</p>'
          '<p>Starou obuv nevyhazujte hned po opotřebení: na procházky, zahradu nebo vodní hrátky se ještě hodí. Nosit závodní boty v tréninku je nehospodárné, protože pěna rychle slábne.</p>'
          '<h2>Ponožky a další doplňky</h2>'
          '<p>Správná bota se doplňuje ponožkami bez švů, nejlépe z umělého vlákna nebo merina; bavlna v bocích drží vlhkost a vede k puchýřům. Vyberte si ponožky z kategorie <a href="/sportovni-ponozky/">sportovní ponožky</a>. Pro delší trasy s vodou a jídlem se hodí <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a> a pro sledování tempa <a href="/sportovni-hodinky/">sportovní hodinky</a>. Při výprodejích sledujte přehled <a href="/bezecke-boty-vyprodej/">běžecké boty výprodej</a>, protože starší generace téhož modelu bývají prakticky stejné.</p>'
          '<h2>Došlap, stabilita a jak ho poznat doma</h2>'
          '<p>Mnoho mužů má pocit, že potřebuje stabilní botu, přestože pro to nemá důvod. Jednoduchý test: postavte se bosí na suchý podklad, namočte chodidlo a otiskněte ho na papír nebo asfalt. Úzký otisk s výrazným obloukem naznačuje vyšší klenbu a sklon k supinaci, široký plný otisk plochou nohu a sklon k pronaci. Test je jen orientační, ale pomůže při diskusi v obchodě a při srovnání s tím, jak se opotřebovává stará obuv. Pokud je podešev sjetá hlavně na vnější hraně paty, jde o typický supinační běh; sjetí uvnitř signalizuje pronaci.</p>'
          '<h2>Závodní a tempové boty</h2>'
          '<p>Na závody a rychlé tréninky se nabízejí lehčí a pružnější modely, často s tuhou vložkou nebo deskou ve středu podešve. Zvyšují efektivitu odrazu, ale vyžadují silnější lýtka a lepší techniku a rychle ztrácejí pružnost. Pro začátečníka nebo pro denní tréninky jsou zbytečné a stojí víc než tréninkové boty. Praktické pravidlo zní, že závodní bota patří na závod a na jeden nebo dva kontrolní tréninky před ním, aby si na ni chodidlo zvyklo.</p>'
          '<h2>Zima, déšť a špatné počasí</h2>'
          '<p>V chladu zvažte botu s hustším svrškem, který nepropustí sníh, a podešev s hlubším vzorkem. Membránové modely drží vodu venku, ale v hlubokém mokrém sněhu nakonec nasáknou i tak, a po vběhnutí do kaluže pomáhá spíš rychle schnoucí síťovina. Při mrazu dbejte na přilnavost gumy: tvrdá guma na ledu klouže, měkčí lépe drží. Večerní běhy ve tmě vyžadují reflexní prvky na botě nebo na oblečení.</p>'
          '<h2>Jak nakupovat v nabídce obchodů</h2>'
          '<p>Stejný model bývá pod různými názvy: obchod napíše celé jméno, jiný jen číslo generace, třetí přidá barvu. Hledejte proto kód modelu nebo název s číslem. U dvou generací téhož modelu rozhoduje drobnost, například tvar horní části nebo přísada v pěně. Starší generace bývá levnější a téměř shodná, ale pokud ji nezvolíte kvůli výprodeji, ověřte rok vydání.</p>',
    faq=[
        ('Jaký je rozdíl mezi pánskými a dámskými běžeckými botami?',
         'Pánské mají širší kopyto, vyšší objem a větší velikostní rozsah, často i pevnější pěnu pro vyšší hmotnost. Dámské jsou užší v patě a střední části. Unisex bota se prodává v obou řadách s jiným číslováním.'),
        ('Jakou velikost běžeckých bot zvolit?',
         'Obvykle o půl až jedno číslo větší než běžná obuv. Před palcem nechte přibližně palec rezervy a zkoušejte odpoledne, když je chodidlo největší. Pata ale musí držet bez sjíždění.'),
        ('Jak poznám, že mám boty příliš těsné?',
         'Prsty se při došlapu zarážejí do špičky, tlačí nárt nebo malíček a po delším běhu bolí nehty. Nepomůže uvolnit tkaničky, protože v botě chybí prostor, správné řešení je vyšší velikost nebo širší model.'),
        ('Potřebuji stabilní běžeckou obuv?',
         'Jen pokud se vám kotník při došlapu výrazně propadá dovnitř a bolí vnitřní strana kolena nebo holeň. Většina rekreačních běžců vystačí s neutrální botou se středním tlumením.'),
        ('Jak často vyměňovat běžecké boty?',
         'Podle kilometrů, nikoli podle vzhledu. Orientačně po několika stovkách kilometrů, dříve u těžšího běžce a při tvrdém povrchu. Když se vrací bolest lýtek nebo kloubů, pěna už nepruží.'),
        ('Mohu v silničních botách běhat po lese?',
         'Po suchých udusaných cestách ano, ale v bahně a na kořenech klouže. Pro les s kopci vyberte trailovou botu s vyšším vzorkem a ochranou špičky, případně hybridní model.'),
        ('Jaké boty vybrat těžšímu běžci?',
         'Tlumenou botu se širší základnou a hustší pěnou. Úzké lehké závodní boty se těžšímu běžci rychle propadnou. Stejně důležité jsou pomalejší tempo a dostatek odpočinku mezi tréninky.'),
        ('Má smysl kupovat starší generaci modelu?',
         'Ano, když nechcete platit za drobné úpravy. Starší verze bývá téměř shodná a levnější. Zkontrolujte jen, zda je dostupná vaše velikost a zda pěna nestárne po delším skladování.'),
        ('Čím se liší běžecká bota od běžné sportovní obuvi?',
         'Má pružnější mezipodešev a určitý sklon podešve (drop), lehčí konstrukci a prodyšný svršek pro opakovaný odval. Běžné tenisky tlumí méně a rychleji se rozpadají při pravidelném běhání.'),
        ('Je lepší kupovat běžecké boty ve výprodeji?',
         'Ano, hlavně u předchozí generace modelu. Velikosti se ale rozprodávají postupně a vzácnější čísla mizí první. Kdo ví, co sedí, nakoupí hned.')])

# ------------------------------------------------------------------ head-lyze
NEW['head-lyze'] = dict(
    title='Head lyže: řady, délka a vázání pro každou úroveň',
    desc='Head lyže od závodních WC Rebels po rekreační Supershape, Joy a Discovery. Jak vybrat řadu, délku a vázání. Porovnejte nabídky českých obchodů.',
    intro='<p>Head je rakouský výrobce, který ve sjezdovém lyžování stojí na dvou pilířích: závodních lyžích a širokém sortimentu pro rekreační jezdce od dětí po zkušené dospělé. Proto se v nabídce vedle sebe objeví lyže z řady WC Rebels určené pro slalom a obří slalom, carvingové lyže Supershape, dámské řady Joy a univerzální Discovery. '
          'Většina kusů se prodává s vázáním, takže netřeba skládat sadu zvlášť. Stránka ukazuje, jak se jednotlivé řady rozlišují, jak z označení vyčíst úroveň a poloměr oblouku, jak vybrat délku a vázání a v čem se Head liší od <a href="/rossignol-lyze/">Rossignol</a> či <a href="/fischer-lyze/">Fischer</a>. '
          'Základní kategorie <a href="/sjezdove-lyze/">sjezdové lyže</a> vysvětluje obecné pojmy; tady se soustředíme na to, co je pro Head specifické.</p>',
    guide='<h2>Jak číst řady Head v nabídce</h2>'
          '<p>Názvy modelů vypadají na první pohled nesrozumitelně, ale mají logiku. Jméno řady říká, pro koho lyže je, číslo či přívlastek udává šířku nebo úroveň a za plusem následuje vázání, které je součástí nabídky. U závodních kusů se objevuje označení WC Rebels a písmena SL, GS nebo SLR, která odkazují na slalom, obří slalom a jejich závodně-rekreační verze. Dámské řady nesou jméno Joy.</p>'
          + T(['Řada v nabídce', 'Zaměření', 'Pro koho'], [
              ['WC Rebels (e-Race, e-SL, e-GS)', 'závodní konstrukce na tvrdou trať', 'zkušení a závodní lyžaři, trenéři, silní jezdci'],
              ['Supershape', 'dynamické carvingové lyže pro rychlé oblouky', 'pokročilí lyžaři na upravených sjezdovkách'],
              ['Shape', 'sportovní carving s vyšší stabilitou', 'středně pokročilí až pokročilí na sjezdovce'],
              ['Discovery', 'univerzální lyže pro rekreační použití', 'většina dospělých, kteří jezdí na dovolené a o víkendech'],
              ['Joy (Real Joy, Easy Joy, Super Joy, e-Power Joy)', 'dámské lyže, lehčí konstrukce', 'ženy a dívky od začátečnic po zkušené jezdkyně'],
              ['Monster, Supershape Team, Paw Patrol', 'dětské a juniorské lyže', 'děti podle hmotnosti a úrovně']]) +
          '<p>Přívlastek AM, Pro nebo Sport za jménem modelu odlišuje úroveň a šířku pod botou. Čím užší lyže, tím rychlejší přechod z hrany na hranu a čím širší, tím větší stabilita v rozbředlém sněhu. Přesné hodnoty vždy ověřte v technických údajích konkrétního kusu, protože se liší podle sezóny.</p>'
          '<h2>Délka a poloměr oblouku</h2>'
          '<p>Délka lyží se odvíjí od výšky, hmotnosti a úrovně. Začátečník volí kratší, protože se lépe otáčí a odpouští chyby, rychlý jezdec delší pro stabilitu. Závodní WC Rebels se vyrábějí v délkách odpovídajících disciplíně, a kdo je kupuje, často nevolí podle výšky, ale podle trenérova doporučení. Při pochybnostech zvolte kratší variantu, pokud jezdíte spíš pomalu, a delší, pokud preferujete rychlost a dlouhé oblouky.</p>'
          '<ul><li><strong>Kratší rádius:</strong> ostré a rychlé zatáčky, lyže se točí snadno, vhodné pro úzké sjezdovky a plynulé oblouky.</li>'
          '<li><strong>Delší rádius:</strong> stabilní při vyšší rychlosti a v rozbité trati, vyžaduje větší prostor na zatáčení.</li>'
          '<li><strong>Tuhost:</strong> tužší lyže vyžaduje větší sílu a lepší techniku, měkčí se snáze ohýbá, ale v rychlosti klepe.</li>'
          '<li><strong>Šířka pod botou:</strong> do 80 mm pro sjezdovku, nad 90 mm už pro sníh mimo upravené trasy.</li></ul>'
          '<h2>Vázání: co znamená číslo a označení GW</h2>'
          '<p>V názvech se objevuje výraz jako PR 11 GW, PRD 12 GW nebo FF 14 GW. Číslo udává nejvyšší nastavitelnou hodnotu uvolnění vázání a Označení GW znamená, že vázání je kompatibilní s botami s protiskluzovou podrážkou GripWalk. Pokud máte starší boty s hladkou podrážkou, ověřte, zda se s vázáním potkají; většina vázání s označením GW pracuje i se staršími botami podle normy, ale výslovně to zkontrolujte u výrobce.</p>'
          + T(['Označení u vázání', 'Co obvykle znamená', 'Pro koho'], [
              ['JRS 4.5', 'junior, nižší hodnota uvolnění', 'malé děti a lehké juniory'],
              ['JRS 7.5', 'junior, vyšší hodnota', 'starší děti, dívky, lehčí mladiství'],
              ['PR 11 GW', 'nastavení do 11, GripWalk', 'rekreační dospělí a středně pokročilí'],
              ['SX 10 GW, JOY 9 GW, JOY 11 GW', 'vázání laděná k dámským lyžím', 'ženy a lehčí jezdci'],
              ['PRD 12 GW', 'vyšší hodnota uvolnění', 'těžší, rychlejší nebo agresivní lyžaři'],
              ['FF 14 GW', 'nejvyšší hodnota z uvedených', 'závodní a velmi silní lyžaři']]) +
          '<p>Hodnotu uvolnění nenastavujte sami. Správné nastavení vychází z hmotnosti, výšky, věku a úrovně lyžaře a mělo by ho provést servis. Kdo chce vázání doplnit nebo vyměnit zvlášť, najde výběr v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>.</p>'
          '<h2>Pánské, dámské a dětské Head</h2>'
          '<p>Dámské řady Joy bývají lehčí, měkčí a se střihem upraveným na nižší hmotnost a jinak posazené těžiště. Díky tomu se stejná délka jezdí snadněji než unisex lyže. Existují i prémiové modely se zesílenou konstrukcí pro zkušené jezdkyně. Vybíráte-li lyže pro ženu, začněte stránkou <a href="/damske-sjezdove-lyze/">dámské sjezdové lyže</a>, a pro porovnání pánských modelů poslouží <a href="/sjezdove-lyze-panske/">pánské sjezdové lyže</a>.</p>'
          '<p>Děti rostou rychle, proto se kupují s rezervou a často se využívají víc sezón. Dětské lyže Head vybírejte podle výšky dítěte a jeho úrovně, nikoli podle věku. Obvykle sahají od brady po nos, začátečníkovi spíš kratší. Dětské lyže s vázáním najdete v kategorii <a href="/detske-lyze/">dětské lyže</a> a podrobněji ve výběru <a href="/detske-sjezdove-lyze/">dětské sjezdové lyže</a>. Pokud se vybírá lyže s motivem Paw Patrol, je to především hra pro nejmenší; pro dítě, které se začne učit, funguje stejně dobře jako jednobarevná.</p>'
          '<h2>Komplet, nebo samostatné lyže</h2>'
          '<p>Většina kusů Head se prodává jako komplet s vázáním, protože výrobce ladí lyži a vázání do celku. Výhodou je cena, jistota kompatibility a jedna montáž. Samostatně se vyplatí kupovat jen tehdy, pokud už máte kvalitní vázání nebo chcete jiný typ upevnění. Souhrnné nabídky najdete v kategorii <a href="/lyze-komplety/">lyže s vázáním (komplety)</a>. K lyžím patří <a href="/lyzarske-boty/">lyžařské boty</a>, které se vybírají nejdřív, protože od nich se odvíjí nastavení vázání, a nezapomínejte na <a href="/lyzarske-helmy/">helmu</a>, hole a brýle.</p>'
          '<h2>Head a ostatní značky</h2>'
          '<p>Na trhu jsou stabilně přítomné i další velké značky. <a href="/rossignol-lyze/">Rossignol</a> a <a href="/fischer-lyze/">Fischer</a> nabízejí také široký sortiment od rekreačních po závodní modely, <a href="/salomon-lyze/">Salomon</a> je známý univerzálními lyžemi pro široké spektrum jezdců a <a href="/sjezdove-lyze-atomic/">Atomic</a> má široké řady od rekreačních po sportovní modely. Head se v tomto srovnání prosazuje hlavně závodní tradicí a vazbou na dynamický carving. Který model vám sedne, rozhodne mnohem víc úroveň a styl než samotný název značky. Kdo hledá českou značku, může se podívat na <a href="/lyze-sulov/">lyže Šulov</a>.</p>'
          '<h2>Tři typické scénáře výběru</h2>'
          '<p>Rodinný lyžař, který jezdí jeden týden v roce na upravených svazích, potřebuje lyže, které odpustí chyby, tedy univerzální řadu Discovery v kratší délce a komplet s vázáním do nižších hodnot. Víkendový pokročilý jezdec, který sjíždí celé dny a rád ukrojí hranu, ocení Supershape nebo Shape, protože drží stopu a reagují hned. Závodník nebo trenér volí WC Rebels a nepřemýšlí o pohodlí, ale o přesnosti v ledové trati.</p>'
          '<p>Rozdíl je i v péči: rekreační lyže stačí brousit jednou za sezónu, závodní vyžadují častější servis a vosk podle teploty a typu sněhu. Počítejte s tím při rozhodování, protože vyšší řady mají vyšší provozní nároky.</p>'
          '<h2>Chyby, kterých se lidé při nákupu dopouštějí</h2>'
          '<ul><li><strong>Přeceňování úrovně:</strong> lyže pro závodníka se pro rekreačního jezdce stává tuhým nepřítelem, který ho unaví už dopoledne.</li>'
          '<li><strong>Koupě lyží před botami:</strong> vázání se seřizuje podle délky botové podrážky, proto bota je prvním krokem.</li>'
          '<li><strong>Příliš dlouhé lyže pro začátečníka:</strong> hůř se řídí a bojí se na nich zatáčet.</li>'
          '<li><strong>Ignorování stáří vázání:</strong> u starších kusů z druhé ruky ověřte u servisu, zda je lze bezpečně nastavit.</li>'
          '<li><strong>Vynechání servisu:</strong> nové lyže bývají v obchodě jen rychle namazané a před prvním dnem je dobré je nechat prohlédnout.</li></ul>'
          '<h2>Péče o lyže a kdy kupovat</h2>'
          '<p>Skluznice vyžaduje pravidelné mazání a hrany pravidelné broušení. Před sezónou nechte lyže prohlédnout v servisu, kde zkontrolují hrany a zda se skluznice nedeformovala. Po sezóně lyže očistěte, namažte vrstvou vosku na uskladnění a uložte na suchém a chladném místě, nikoli u topení. Vázání nevystavujte vysokému napětí a při přepravě chraňte před pádem. Nákup se vyplatí na konci zimy a v létě, kdy se vyprodává předchozí kolekce, v předvánoční sezóně je výběr velikostí nejširší, ale zboží je dražší.</p>'
          '<p>Při srovnávání nabídky používejte kód nebo celý název modelu včetně délky a vázání. Totéž jméno se v obchodech objevuje s různými vázáními, ale pod jinou cenou.</p>',
    faq=[
        ('Pro koho jsou lyže Head z řady WC Rebels?',
         'Pro zkušené a závodní lyžaře, kteří jezdí rychle na upravené trati. Konstrukce je tuhá a vyžaduje správnou techniku. Rekreační lyžař si lépe poradí s řadou Supershape nebo Discovery.'),
        ('Jak vybrat délku Head lyží?',
         'Podle výšky, hmotnosti a úrovně. Začátečník volí kratší lyže zhruba k bradě až k nosu, pokročilý delší. Závodní modely se vybírají podle disciplíny, nejlépe po poradě s trenérem nebo servisem.'),
        ('Co znamená označení GW u vázání?',
         'Že vázání pracuje s botami se zakřivenou protiskluzovou podrážkou GripWalk. Boty s touto podrážkou se pohodlněji chodí mimo lyže. Starší hladké boty ověřte u výrobce, jestli jsou kompatibilní.'),
        ('Co znamená číslo u vázání, například PR 11?',
         'Maximální hodnotu uvolnění, tedy sílu, při které se bota uvolní. Hodnotu správně nastavuje servis podle hmotnosti, výšky, věku a úrovně lyžaře. Sami ji neměňte.'),
        ('Jsou dámské lyže Head Joy jen jinak vybarvené?',
         'Ne, jsou lehčí a stavěné na nižší hmotnost a jiné rozložení těžiště. Díky tomu se lépe ohýbají a zatáčejí s menší silou. Silnější nebo vyšší ženy mohou zvolit i unisex model.'),
        ('Jak poznám, že dětská lyže sedí?',
         'Dítěti sahá obvykle od brady po nos, začátečníkovi spíš kratší. Rozhoduje hmotnost a úroveň, ne věk. Vázání nastavuje servis podle hmotnosti a bot dítěte.'),
        ('Mám kupovat lyže s vázáním, nebo bez něj?',
         'Většinou komplet, protože je přizpůsobený lyži a výhodnější. Samostatně lyže vybírejte, jen pokud máte vázání, které chcete přemontovat, nebo požadujete konkrétní typ.'),
        ('Hodí se Discovery pro začátečníka?',
         'Ano, pokud zvolíte kratší délku a jízdu na upravených sjezdovkách. Univerzální řady odpustí chyby a hodí se i na pozdější pokrok. Čistě závodní lyže pro začátek nejsou vhodné.'),
        ('Kdy je nejlepší doba na nákup lyží?',
         'Širší výběr velikostí bývá na podzim, ale vyšší ceny. Na konci zimy a v létě se vyprodává minulá sezóna a ceny klesají, ale nemusí zbýt vaše délka. Kdo ví, co hledá, nakupuje v létě.'),
        ('Jak často nechat lyže seřídit a naostřit?',
         'Před každou sezónou prohlídka servisem a pak podle používání. Při časté jízdě na tvrdém sněhu se hrany otupí rychle. Mazání skluznice se vyplatí před velkými výlety a před uskladněním.')])
