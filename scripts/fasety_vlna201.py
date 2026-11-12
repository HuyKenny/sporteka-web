"""sporteka.cz — facet landing texts wave 201: fjallraven-mikina, icebreaker-ponozky, under-armour-rukavice, lotto-tenisky.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ fjallraven-mikina
NEW['fjallraven-mikina'] = dict(
    title='Fjällräven mikina: bavlna, fleece a výběr řady',
    desc='Fjällräven mikiny od městských bavlněných Logo a Vardag po turistické fleecové Abisko. Rozdíly řad, velikosti M a W, vrstvení a porovnání obchodů.',
    intro='<p>Fjällräven je švédská outdoorová značka, která vznikla v roce 1960 a vžila se hlavně díky batohům a pevným turistickým kalhotám. Mikiny jsou u ní dvě odlišná zboží pod jedním logem. První skupinu tvoří bavlněné kousky do města, druhou technické fleecové vrstvy určené na stezku. '
          'Na této stránce je porovnáte vedle sebe a hned uvidíte, které řady jsou volnočasové a které patří do batohu na túru. Průvodce vysvětluje názvy modelů, rozdíl mezi označením pánský a dámský, vrstvení s bundou i péči, aby vás nezklamalo srážení nebo příliš tenký fleece. '
          'Širší nabídku najdete v kategorii <a href="/mikiny/">mikiny</a>, o značce samotné <a href="/znacka/fjallraven/">Fjällräven</a>.</p>',
    guide='<h2>Dva světy pod jednou liškou</h2>'
          '<p>Název Fjällräven znamená ve švédštině polární liška a právě její silueta zdobí hrudník většiny mikin. Značka vychází z výpravní tradice, takže i městská mikina bývá střižená prakticky a bez zbytečných ozdob. Aby se v nabídce dalo vyznat, pomůže rozdělení podle účelu. Přesné vlastnosti vždy ověřte v popisu u konkrétního obchodu, protože se materiály jednotlivých sezón mohou lišit.</p>'
          + T(['Řada podle názvu', 'Typ mikiny', 'Hodí se'], [
              ['Logo Hoodie, Logo Sweater', 'bavlněná, jednoduchý střih, výrazné logo', 'město, škola, víkend'],
              ['1960 Logo Badge Sweater', 'bavlněná bez kapuce, nášivka v retro stylu', 'každý den, ke džínám'],
              ['Vardag, Classic', 'bavlněná nebo tepláková, uvolněný střih', 'doma, výlety autem, kavárna'],
              ['Abisko Lite, Abisko Trail, Abisko Day', 'sportovní a trekingová, lehčí materiál', 'pěší túry, běžná chůze v horách'],
              ['Abisko Grid Fleece, Polar Fleece, Stina, Pine', 'fleece různé hustoty, často s kapucí', 'střední vrstva, chladné ráno u stanu'],
              ['High Coast Wind Hoodie', 'tenká vrstva proti větru', 'lehká ochrana v batohu'],
              ['Expedition Lätt, Pack Down', 'zateplený kousek blížící se bundě', 'zima a mezisezóna, viz bundy']]) +
          '<p>Poslední dvě řádky už hranici mikiny překračují. Pokud hledáte spíš zateplenou bundu, otevřete landing <a href="/fjallraven-bunda/">Fjällräven bunda</a>, protože tam jsou i podobné kousky s kapucí.</p>'
          '<h2>Bavlněné mikiny: jak se nosí a drží tvar</h2>'
          '<p>Bavlněné řady Logo, Vardag a 1960 mají střih, který na první pohled nevypadá sportovně. Hodí se do města, na pracovní den bez obleku nebo na dovolenou, kde ocení měkkost a nenápadný vzhled. Bavlna je příjemná na dotek, ale po vyprání se může mírně srazit a nasákne potem. Proto ji nevybírejte na běh ani na rychlý výstup do kopce, kde se z ní stane těžká a studená vrstva.</p>'
          '<ul><li><strong>Kapuce:</strong> kousky s kapucí vyberte, pokud je nosíte venku, bez kapuce jsou čistší pod bundu.</li>'
          '<li><strong>Zip a výstřih:</strong> klasický svetr přes hlavu je teplejší u krku, na zip se rychleji větrá.</li>'
          '<li><strong>Barva:</strong> tmavé odstíny snesou víc praní, světlé béžové a šedé vynikají ve městě, ale zachytí skvrny.</li>'
          '<li><strong>Žebrování:</strong> pevné manžety a lem drží mikinu na místě, když pod ní nosíte batoh.</li></ul>'
          '<h2>Fleecové mikiny řady Abisko a spol.</h2>'
          '<p>Na stezku se víc hodí fleece, který při nízké hmotnosti drží teplo a po zvlhčení rychle schne. Řady Abisko Lite a Abisko Trail slouží jako střední vrstva pod bundu, tlustší typy Polar Fleece nebo Grid Fleece jsou určené do chladnějšího počasí. Grid struktura, tedy vzor se zdvojenými kanálky na vnitřní straně, zlepšuje prodyšnost, ale přesný popis technologie hledejte vždy u konkrétního produktu. Jakmile potřebujete vlhkost odvést z celého pohybu, doplňte fleece spodní vrstvou z <a href="/merino-pradlo/">merino prádla</a>.</p>'
          '<p>Při výběru fleece sledujte hlavně tloušťku. Lehká varianta se vejde do dna batohu a vystačí na aktivní chůzi. Hustší typ je lepší, když se zastavujete na vrcholech nebo spíte pod širákem. Ucelený přehled všech druhů je v kategorii <a href="/fleecove-mikiny/">fleecové mikiny</a>, pro sportovní použití pak v kategorii <a href="/funkcni-mikiny/">funkční mikiny</a>.</p>'
          '<h2>Pánské, dámské a velikosti</h2>'
          '<p>V názvech modelů se označuje pohlaví. Písmeno W za názvem, například Hoodie W, znamená dámský střih, M nebo slovo pánská se uvádí u mužských kousků. Dámské střihy mají užší ramena a kratší délku těla, pánské jsou rovnější. Unisex označení se u značky objevuje jen výjimečně, takže se řiďte tabulkou výrobce a naměřenými rozměry, ne zvyklostí z jiné značky.</p>'
          + T(['Kde měřit', 'Jak', 'Co s výsledkem'], [
              ['Hrudník', 'v nejširším místě pod paždím', 'porovnejte s obvodem hrudníku v tabulce'],
              ['Délka rukávu', 'od ramenního švu po zápěstí', 'důležité u fleecu s dlouhými manžetami'],
              ['Délka těla', 'od krku po dolní lem', 'pod bundu stačí kratší, ven delší'],
              ['Ramena', 'od ramene k rameni po zádech', 'rozhoduje u těsnějších střihů'],
              ['Vrstvy pod mikinou', 'zahrňte tričko nebo merino', 'u fleecu raději o jednu velikost volněji']]) +
          '<h2>Jak mikinu vrstvit</h2>'
          '<p>Ve třech vrstvách funguje bavlněná mikina jen jako městská střední. V horách obvykle začíná spodní vrstvou z merina nebo syntetiky, na ni se oblékne fleece a navrch bunda proti větru a dešti. Aby fleece nezamrzal, zapínejte ho jen tehdy, když je opravdu zima, a při stoupání ho svlékněte dřív, než začnete mít mokrá záda. Pro zimu se vyplatí vedle mikiny pohlídat i <a href="/zimni-bundy/">zimní bundy</a> a <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>Oproti sportovním značkám působí Fjällräven střídměji, s důrazem na dlouhou životnost a výpravní design. Mikiny značek <a href="/the-north-face-mikina/">The North Face</a> a <a href="/columbia-mikina/">Columbia</a> jsou technické a barevnější, <a href="/nike-mikina/">Nike</a> a <a href="/adidas-mikina/">Adidas</a> cílí na sport a streetwear a bývají sportovně přiléhavé. Když vám jde především o outdoor styl bez velkého loga, Fjällräven se vyplatí vyzkoušet.</p>'
          '<h2>Péče, aby mikina vydržela</h2>'
          '<ol><li>Přečtěte štítek a dodržujte teplotu praní, bavlna se tepelně namáhá víc než syntetika.</li>'
          '<li>Fleece perte naruby, bez aviváže, která zalepí vlákna a ubere teplo.</li>'
          '<li>Před praním zapněte zip a kapsy, aby nepoškodily jemný materiál.</li>'
          '<li>Sušte volně na tyči, ne na topení, a fleece nežehlete.</li>'
          '<li>Skvrny z lesa ošetřete hned, dokud nezaschnou, a nepoužívejte bělicí prostředky.</li></ol>'
          '<h2>Co dalšího si ke Fjällräven vybrat</h2>'
          '<p>Značka funguje jako ucelená výbava. K mikině se hodí batoh z landingu <a href="/fjallraven-batoh/">Fjällräven batoh</a>, čepice z <a href="/fjallraven-cepice/">Fjällräven čepice</a> nebo pevné <a href="/fjallraven-kalhoty/">kalhoty</a> a <a href="/fjallraven-tricko/">trička</a>. Když si vyberete jednu barevnou paletu, vyjde z toho kompletní outfit, který lze nosit na túru i do města.</p>',
    faq=[
        ('Jsou mikiny Fjällräven vhodné i do města?', 'Ano, bavlněné řady Logo, Vardag a 1960 Logo Badge Sweater jsou navržené právě pro každodenní nošení. Mají jednoduchý střih a odolný materiál. Technické fleecové řady Abisko jsou do města spíše praktické než elegantní a hodí se na podzim a zimu.'),
        ('Co znamená písmeno W v názvu modelu?', 'W je zkratka anglického women a označuje dámský střih. Pánské kousky mívají v názvu M nebo označení pánská. Pokud se pohlaví v názvu nevyskytuje, zkontrolujte popis u obchodu a velikostní tabulku výrobce.'),
        ('Srazí se bavlněná mikina po praní?', 'Bavlna se při prvním praní může mírně srazit, zvlášť při vysoké teplotě a v sušičce. Dodržujte teplotu uvedenou na štítku a sušte volně. Směsové materiály s polyesterem drží tvar lépe.'),
        ('Kterou řadu zvolit na pěší túru?', 'Na túru vyberte fleecové mikiny řady Abisko Lite nebo Abisko Trail, které jsou lehčí a rychle schnou. V chladném počasí se hodí hustší Polar Fleece. Bavlněné Logo mikiny nechte na město, při pocení ztěžknou.'),
        ('Je High Coast Wind Hoodie opravdu mikina?', 'Je to tenká vrstva proti větru, takže má blíž k lehké bundě s kapucí. Hodí se do batohu jako rychlá ochrana, ale hřeje méně než fleece. Hledáte-li teplo, zvolte fleece nebo zateplenou variantu.'),
        ('Jaká velikost sedí, když jsem mezi dvěma?', 'U bavlněných mikin, které se můžou srazit, volte spíše větší velikost. U fleecu určeného jako střední vrstva také, aby se pod něj vešlo tričko nebo merino. U těsného městského střihu naopak sáhněte po menší.'),
        ('Dá se Fjällräven mikina nosit pod bundu?', 'Ano, tenký fleece a kousky bez kapuce jsou na to ideální. Silná mikina s velkou kapucí pod bundou tlačí na krk a omezuje pohyb. Ověřte si, že zip bundy se dopne bez odporu.'),
        ('Jak poznám originální kus?', 'Kupujte u prověřených obchodů, které porovnáváme na této stránce. Zkontrolujte švy, kvalitu nášivky s liškou a štítek s údaji o materiálu. Nezvykle nízká cena u nového kusu je důvod k opatrnosti.'),
        ('Kdy se Fjällräven slevuje?', 'Slevy se nejčastěji objevují při výprodeji sezónních barev a při změně kolekce, tedy na jaře a na konci zimy. Základní barvy modelů jako Logo Hoodie se objevují trvale. Porovnejte nabídky obchodů a sledujte skladovost velikostí.'),
        ('Jak vyprat fleecovou mikinu?', 'Perte ji naruby na šetrný program, bez aviváže a bez bělidla. Po vyprání ji sušte volně v pokojové teplotě. Aviváž zalepí vlákna a ubere fleecu schopnost hřát a odvádět vlhkost.'),
    ],
)

# ------------------------------------------------------------------ icebreaker-ponozky
NEW['icebreaker-ponozky'] = dict(
    title='Icebreaker ponožky: merino na túru, lyže a běh',
    desc='Icebreaker ponožky z merina: řady Hike+, Ski+, Run+ a Lifestyle, tloušťky od ultralight po heavy, délky Micro až OTC. Jak vybrat a porovnat nabídky.',
    intro='<p>Icebreaker je novozélandská značka, která se od poloviny devadesátých let soustředí na merino vlnu. Ponožky jsou u ní rozdělené podle sportu a v názvu každého modelu najdete řadu, tloušťku a délku, třeba Hike+ Light Crew nebo Ski+ Medium OTC. Hned se tak dá poznat, zda je to ponožka do lehké boty, na celodenní túru, nebo do lyžáků. '
          'Tato stránka shrnuje, co jednotlivá označení znamenají, jak zvolit tloušťku podle počasí a kam patří které délky. Obecný výběr je v kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a>, přehled všech vlněných kousků v kategorii <a href="/merino-ponozky/">merino ponožky</a> a o značce najdete víc na stránce <a href="/znacka/icebreaker/">Icebreaker</a>.</p>',
    guide='<h2>Jak číst názvy modelů Icebreaker</h2>'
          '<p>Značka používá jednotné pojmenování, které funguje jako zkratka pro určení. První slovo za ponožkou říká, pro jaký sport je určená, další tloušťku tkaniny a poslední střih. Díky tomu si můžete porovnat různé obchody a nenakoupit omylem ponožku na lyže, když potřebujete běžeckou. Údaj Mens a Wmns označuje pánský a dámský střih, Kids dětský.</p>'
          + T(['Část názvu', 'Příklady', 'Význam'], [
              ['Řada', 'Hike+, Ski+, Run+, Lifestyle, Multisport', 'určený sport a konstrukce ponožky'],
              ['Tloušťka', 'Ultralight, Light, Medium, Heavy', 'tloušťka a tepelný komfort od nejtenčí po nejteplejší'],
              ['Délka', 'Micro, Mini, Crew, Mid Calf, OTC', 'od nízké ponožky po podkolenku'],
              ['Liner', 'Hike+ Liner Crew', 'tenká vnitřní ponožka pod silnější'],
              ['Contour', 'Ski+ Mountain Contour', 'lyžařské provedení s tvarováním'],
              ['Sada 2 ks', 'Hike+ Light Crew (sada 2 ks)', 'dva páry v balení, praktické na zásobu']]) +
          '<p>Zkratka Mer v názvu, například u řady Mer Run+, znamená merino. Jde o stejný materiál, jen v kratším pojmenování.</p>'
          '<h2>Proč merino a kdy nestačí</h2>'
          '<p>Merino hřeje i vlhké, pomaleji zapáchá než syntetika a na kůži bývá příjemnější než hrubší vlna. Čisté merino by se ale rychle prodřelo, proto bývá v ponožkách smíchané se syntetickými vlákny pro pevnost a s elastanem pro pružnost. Přesné složení najdete na štítku produktu. Na dlouhý běh v horku se někdy vyplatí syntetika, která schne rychleji, ale pro většinu dnů v horách, na lyžích i při běžné chůzi je merino spolehlivá volba.</p>'
          '<h2>Řady podle sportu</h2>'
          '<h3>Hike+: pěší turistika</h3>'
          '<p>Turistická řada je nejširší. Lehké Light Crew se hodí do nízkých botek a na letní trasy, Medium Crew a Mid Calf do vysokých turistických bot na celodenní výlety, Heavy do chladu a na zimní treky. Dlouhá Mid Calf ponožka chrání lýtko před trním a otěrem horního okraje boty. K ponožce patří i <a href="/turisticke-batohy/">turistický batoh</a>, ale nezapomeňte, že víc záleží na botě než na ponožce. Ve špatně sedící obuvi neporadí ani nejlepší vlna.</p>'
          '<h3>Ski+: lyže a snowboard</h3>'
          '<p>Lyžařské ponožky jsou dlouhé OTC, tedy nad lýtko, aby se nezkrucovaly a nedřely o horní okraj lyžáku. Tloušťka Light a Ultralight se hodí do dobře padnoucích přilnavých bot a na jarní lyžování, Medium je univerzální volba. Dobře sedící lyžák žádnou silnou ponožku nepotřebuje, protože tlustá vrstva zvyšuje tlak na chodidlo a zhoršuje prokrvení. Další varianty jsou v kategorii <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a pro děti ve výběru <a href="/detske-lyzarske-ponozky/">dětské lyžařské ponožky</a>.</p>'
          '<h3>Run+ a Multisport: běh a lehké sporty</h3>'
          '<p>Ultralight ponožky Run+ jsou tenké a ve střihu Micro nebo Mini nepřečnívají z běžecké boty. Řada Multisport se hodí na kolo, fitness nebo rychlou chůzi. Pro silniční a trailové běhání si vedle ponožek prohlédněte <a href="/bezecka-obuv/">běžeckou obuv</a>, aby se tloušťka ponožky shodovala s tvarem boty. Na kolo se hodí i speciální <a href="/cyklisticke-ponozky/">cyklistické ponožky</a>.</p>'
          '<h3>Lifestyle: do města a kanceláře</h3>'
          '<p>Lifestyle ponožky jsou jednodušší, tenčí a vzorované nebo jednobarevné. Hodí se k teniskám, polobotkám i do kanceláře, kde potřebujete příjemné suché nohy celý den. Pokud chcete vlněné ponožky do tenisek, podívejte se i na <a href="/tenisky/">tenisky</a>.</p>'
          '<h2>Jak zvolit tloušťku podle počasí</h2>'
          + T(['Situace', 'Tloušťka', 'Poznámka'], [
              ['Léto, krátký výlet nebo běh', 'Ultralight, Light', 'nízký střih, vzdušná konstrukce'],
              ['Jaro a podzim, celodenní túra', 'Light až Medium', 'Crew nebo Mid Calf podle boty'],
              ['Zima, mráz, dlouhé zastávky', 'Medium až Heavy', 'zkontrolujte, zda se vejde do boty'],
              ['Lyžování při pohybu', 'Light až Medium', 'OTC, bez záhybů v lyžáku'],
              ['Kancelář a město', 'Light', 'Lifestyle řada'],
              ['Pod silnější ponožku', 'Liner', 'omezuje otěry při dlouhé chůzi']]) +
          '<p>Platí obecné pravidlo, že tlustší ponožka nemusí být teplejší. Když zaplní bota příliš těsně, zhorší oběh krve a chodidlo zmrzne dřív. Zimní boty proto zkoušejte s ponožkami, které budete nosit.</p>'
          '<h2>Velikosti a střih pro muže, ženy a děti</h2>'
          '<p>Velikosti se uvádějí v rozmezích, například M pro několik sousedních čísel obuvi. Pokud se pohybujete na hranici, vyberte větší velikost u tenčích ponožek a menší u hustých. Ženské střihy Wmns jsou užší a v klenbě upravené, pánské Mens delší. Dětské Kids ponožky jsou menší v obvodu, ale noha dětí rychle roste, takže se vyplatí vybrat s malou rezervou. Pro nejmenší vlněné modely poslouží <a href="/detske-merino-ponozky/">dětské merino ponožky</a>, pro dospělé existují přehledy <a href="/merino-ponozky-damske/">dámských</a> a <a href="/merino-ponozky-panske/">pánských</a> merino ponožek.</p>'
          '<h2>Srovnání s jinými vlněnými značkami</h2>'
          '<p>Z podobně zaměřených značek jsou v nabídce <a href="/smartwool-ponozky/">Smartwool</a> a <a href="/lasting-merino-ponozky/">Lasting</a>. Smartwool je americký konkurent s podobnými řadami pro túru a lyže, Lasting je česká značka s širokým sortimentem vlněných a bavlněných ponožek. Pro porovnání se sportovním mainstreamem, třeba <a href="/nike-ponozky/">Nike ponožkami</a>, platí, že merino se hodí na hory a delší pohyb, syntetika zase na krátký trénink.</p>'
          '<h2>Jak o ponožky pečovat</h2>'
          '<ol><li>Perte je na teplotu uvedenou na štítku, obvykle třicet až čtyřicet stupňů.</li>'
          '<li>Nepoužívejte aviváž, zalepuje vlákna a snižuje odvod vlhkosti.</li>'
          '<li>Obracejte je naruby, aby se povrch vlákna neotíral o buben pračky.</li>'
          '<li>Sušte volně, ne na radiátoru, jinak merino ztvrdne.</li>'
          '<li>Při prvních dírkách je zašijte dřív, než se rozšíří.</li></ol>'
          '<p>Pokud jedete na vícedenní túru, stačí vzít dva páry a střídat je. Vlna se vyvětrá a druhý den je znovu použitelná.</p>',
    faq=[
        ('Co znamená Hike+, Ski+ a Run+ u Icebreaker ponožek?', 'Jsou to řady určené pro konkrétní sport: Hike+ pro turistiku, Ski+ pro lyžování a snowboarding, Run+ pro běh. Rozdíl je ve střihu, tvarování a zesílených místech. Pro lehké vycházky stačí řada Lifestyle.'),
        ('Jaká tloušťka je nejlepší na celodenní túru?', 'Pro většinu počasí funguje Light nebo Medium. V létě sáhněte po Light, v chladu po Medium nebo Heavy. Rozhoduje také bota, v těsné zimní botě se tlustá ponožka nemusí vejít.'),
        ('Čím se liší Crew, Mid Calf a OTC?', 'Crew sahá těsně nad kotník, Mid Calf do poloviny lýtka, OTC je podkolenka určená do lyžařských bot. Mini a Micro jsou nízké a hodí se do nízké obuvi.'),
        ('Pálí merino na kůži?', 'Jemné merino vlákno pálí méně než běžná hrubší vlna, přesto citlivá pokožka může reagovat. Pokud si nejste jisti, začněte tenkou ponožkou a vyzkoušejte ji několik hodin. Pomůže i vyprání před prvním nošením.'),
        ('Dají se Ski+ ponožky nosit i mimo lyže?', 'Ano, v zimě jsou vhodné do zimních bot, na sníh i na dlouhé procházky. Dlouhá OTC délka ale nezapadá do nízké obuvi. Pro ni zvolte Crew nebo nižší.'),
        ('Jak poznám správnou velikost?', 'Podívejte se do tabulky u produktu a porovnejte ji s číslem obuvi. Je-li noha mezi dvěma velikostmi, u tenké ponožky vezměte větší, u husté menší. Dětské velikosti kupujte s malou rezervou.'),
        ('Je lepší merino, nebo syntetická ponožka?', 'Merino hřeje i vlhké a méně zapáchá, syntetika rychleji schne a bývá odolnější. Na vícedenní túru a lyže se většinou hodí merino, na krátký intenzivní běh stačí syntetika. Mnoho ponožek obsahuje směs obou vláken.'),
        ('Jak dlouho ponožky vydrží?', 'Záleží na zátěži, obuvi a péči. Nejvíc se opotřebují místa pod patou a prsty. Pomáhá střídání dvou párů, správná velikost obuvi a praní na šetrný program.'),
        ('Proč se někde prodává sada 2 ks?', 'Dva páry stejného typu v jednom balení se hodí na střídání při delší cestě. Porovnejte cenu za pár v nabídkách obchodů, protože se sady a kusové ponožky mohou lišit. Dávejte pozor, zda dostanete stejný odstín.'),
        ('Mají Icebreaker i dětské ponožky?', 'Ano, v nabídce jsou modely označené Kids, například pro lyže a turistiku. Dětská noha roste rychle, takže se vyplatí kontrolovat velikost každou sezónu. Více vlněných variant najdete mezi dětskými merino ponožkami.'),
    ],
)

# ------------------------------------------------------------------ under-armour-rukavice
NEW['under-armour-rukavice'] = dict(
    title='Under Armour rukavice: Storm, Halftime a trénink',
    desc='Under Armour rukavice: zimní Storm Insulated a Liner, běžecké Storm Run, tréninkové a na posilování. Jak vybrat velikost a typ podle sportu a počasí.',
    intro='<p>Americká značka Under Armour vznikla v roce 1996 jako výrobce funkčního prádla a rukavice jsou u ní přirozené rozšíření. Sortiment je užší než u specializovaných výrobců, ale pokrývá tři hlavní situace: chladné dny a běh v řadě Storm, vrstvu do mírného podzimu pod názvem Halftime a tréninkové rukavice do posilovny. '
          'Na této stránce uvidíte jednotlivé modely vedle sebe a průvodce vysvětlí, jak se liší Storm Liner od Storm Insulated, kdy zvolit tenkou vrstvu místo zateplené a jak správně vybrat velikost. Obě skupiny zahrnují pánské, dámské i chlapecké střihy, takže si vyberete i pro děti. Širší přehled najdete v kategorii <a href="/sportovni-rukavice/">rukavice</a> a o značce na stránce <a href="/znacka/under-armour/">Under Armour</a>.</p>',
    guide='<h2>Řady Under Armour rukavic podle názvu</h2>'
          '<p>Názvy modelů prozrazují účel víc než popis v obchodě. Slovo Storm označuje zimní a větrné počasí, Run a Liner tenčí konstrukci, Insulated zateplené provedení. Přesné materiály a vlastnosti si vždy ověřte v popisu produktu, protože se u jednotlivých sezón mohou změnit.</p>'
          + T(['Model podle názvu', 'Na co míří', 'Hodí se'], [
              ['Storm Liner', 'tenká vrstva do chladu', 'běh, kolo, ranní cesta, pod silnější rukavici'],
              ['Storm Run, Storm Run Liner', 'sportovní, lehká a pružná', 'zimní běhání, rychlá chůze'],
              ['Storm Insulated', 'zateplená rukavice', 'chladné dny, zimní procházky, dojíždění'],
              ['Halftime', 'měkká prakticky nošená rukavice', 'podzim, jaro, každodenní nošení'],
              ['Training Glove, Weightlifting', 'ochrana dlaně při cvičení', 'posilovna, kalistenika, činky'],
              ['Drive Cart Mitt', 'golfový palčák proti zimě', 'golf za chladného počasí'],
              ['Storm pro chlapce', 'dětský střih', 'škola, sáňkování, zimní hry']]) +
          '<p>Značka vyrábí rukavice ve střídmém barevném provedení, hlavně černé, šedé a občas modré. Černá se nejlépe kombinuje a dlouho vypadá čistě, světle šedá rychleji zachytí špínu z řidítek nebo lana.</p>'
          '<h2>Storm Liner a Storm Insulated: tenká, nebo teplá</h2>'
          '<p>Nejčastější otázka u značky zní, kterou z rukavic Storm zvolit. Liner je tenká a pružná, hodí se v ranním chladu, při pohybu a pod další vrstvu. Insulated má zateplení, zahřeje i na zastávce a při pomalejší chůzi. Pokud se při pohybu rychle zahřejete, zvolte tenkou rukavici, ve které se nezapotíte. Kdo má ruce stále studené, potřebuje zateplenou variantu. Výhodou Liner modelů je i to, že se vejdou do kapsy bundy.</p>'
          '<p>Označení Storm odkazuje na úpravu proti vodě, ale rukavice nejsou ponořitelné ani nepromokavé jako lyžařské. V trvalém dešti nebo ve sněhu na svahu si raději vezměte rukavici z kategorie <a href="/lyzarske-rukavice/">lyžařské rukavice</a>, která má nepropustnou membránu, vyztuženou dlaň a dlouhou manžetu.</p>'
          '<h2>Běh v rukavicích</h2>'
          '<p>Při běhu se ruce zahřívají hůř než nohy, protože tělo posílá krev hlavně do trupu a velkých svalů. Zimní běžec proto ocení pružnou rukavici, která nepřekáží při držení klíčů nebo telefonu. Volte co nejtenčí, ale dostatečně těsnou, aby nešustila a nepohybovala se na prstech. Pokud při běhu nosíte i čepici a vrstvu na tělo, podívejte se na <a href="/under-armour-mikina/">mikiny Under Armour</a> nebo na <a href="/bezecke-boty-under-armour/">běžecké boty Under Armour</a>, abyste sladili výbavu.</p>'
          '<ul><li><strong>Dotykové špičky:</strong> ověřte v popisu, zda jsou prsty uzpůsobené ovládání displeje.</li>'
          '<li><strong>Manžeta:</strong> kratší manžeta zapadne pod rukáv, delší pokryje zápěstí.</li>'
          '<li><strong>Reflexní prvky:</strong> hodí se pro běh za šera.</li>'
          '<li><strong>Prodyšnost:</strong> příliš teplá rukavice vede k potu a rychlému zchladnutí.</li></ul>'
          '<h2>Tréninkové a posilovací rukavice</h2>'
          '<p>Rukavice Training a Weightlifting chrání dlaň před otlaky a zlepšují úchop činek, kettlebellu nebo hrazdy. Mají zesílenou dlaň a obvykle volné prsty, aby zůstal cit. Neslouží proti zimě. Dobře padnoucí rukavice nemá volné místo ve špičkách prstů a nesvírá zápěstí. Pro co největší cit vybírejte rukavici s tenkou, ale pevnou dlaní, která se při úchopu nepřesouvá. Další vybavení do posilovny najdete v kategorii <a href="/treninkova-obuv/">tréninková obuv</a> a v landingu <a href="/under-armour-teplaky/">Under Armour tepláky</a>.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Vyberte velikost podle obvodu dlaně, který změříte kolem kloubů prstů bez palce, a podle délky ruky od zápěstí po špičku nejdelšího prstu. Naměřené hodnoty porovnejte s tabulkou výrobce. Pánské, dámské a dětské střihy se liší šířkou dlaně i délkou prstů. Dámské modely jsou užší, dětské mají kratší prsty a často pevnou manžetu proti sněhu.</p>'
          + T(['Zkouška', 'Správně', 'Špatně'], [
              ['Špičky prstů', 'lehká rezerva, prsty se dotýkají konců', 'prázdný prostor nebo tlak na nehty'],
              ['Sevření pěsti', 'látka nepovoluje a netlačí na klouby', 'rukavice se napíná nebo sjíždí'],
              ['Zápěstí', 'manžeta obepíná bez škrcení', 'šustí, drží se jen rukou'],
              ['Palec', 'volně se opře o ukazovák', 'šev tlačí do základu palce'],
              ['S druhou vrstvou', 'tenká rukavice se vejde pod teplou', 'obě společně svírají ruce']]) +
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>Oproti <a href="/nike-rukavice/">Nike rukavicím</a> a <a href="/adidas-rukavice/">Adidas rukavicím</a>, které jsou si v sortimentu blízké, působí Under Armour technicky s důrazem na přiléhavý střih a trénink. Specializované kousky do sněhu a na běžky nabízejí značky jako <a href="/swix-rukavice/">Swix</a>, <a href="/silvini-rukavice/">Silvini</a> nebo <a href="/rukavice-dynafit/">Dynafit</a>, pro nejmenší pak <a href="/reima-rukavice/">Reima</a>. Rozdělení rukavic podle pohlaví najdete také v landingech <a href="/panske-rukavice/">pánské rukavice</a>, <a href="/damske-rukavice/">dámské rukavice</a> a <a href="/detske-rukavice/">dětské rukavice</a>.</p>'
          '<h2>Péče o rukavice</h2>'
          '<ol><li>Přečtěte štítek, rukavice s úpravou proti vodě nepatří do sušičky.</li>'
          '<li>Perte je na šetrný program nebo ručně, bez aviváže.</li>'
          '<li>Po vyprání je tvarujte a nechte schnout při pokojové teplotě.</li>'
          '<li>Vlhké rukavice nikdy nesušte na radiátoru, deformuje se materiál.</li>'
          '<li>Sportovní rukavice vyvětrejte po každém použití, aby nezapáchaly.</li></ol>'
          '<h2>Kdy kupovat a co dělat s jedním kusem</h2>'
          '<p>Zimní řady se nejlevněji kupují na jaře a koncem zimy, tréninkové rukavice se slevují celoročně. Když ztratíte jednu rukavici, nejsnáze ji nahradíte stejným modelem, a proto se vyplatí pamatovat si název, například Storm Liner nebo Halftime. Porovnejte nabídky obchodů a ověřte, zda je ve vašem čísle skladem. U zimních modelů myslete také na to, že se populární velikosti vyprodají dřív než nejmenší a největší, proto s nákupem příliš nečekejte.</p>',
    faq=[
        ('Čím se liší Storm Liner a Storm Insulated?', 'Liner je tenká, pružná vrstva do chladnějšího počasí a pod další rukavici. Insulated je zateplený a hřeje i při pomalém pohybu nebo stání. Volte podle teploty a podle toho, jak moc se při pohybu zahřejete.'),
        ('Jsou rukavice Storm nepromokavé?', 'Úprava Storm odpuzuje vodu a vítr, ale rukavice nejsou určené do trvalého deště nebo na sjezdovku. Pro mokrý sníh vyberte lyžařskou rukavici s membránou. Ověřte popis u každého modelu.'),
        ('Lze v nich ovládat mobil?', 'Některé modely mají dotykové špičky, jiné ne. Údaj hledejte v popisu konkrétního produktu. Pokud jej nenajdete, počítejte s tím, že rukavici sundáte.'),
        ('Jakou řadu zvolit na zimní běh?', 'Nejlepší je tenká, pružná rukavice jako Storm Run nebo Storm Liner. Příliš teplá způsobí pot a následné zchladnutí rukou. Při velkém mrazu nasaďte přes ni palčák.'),
        ('Hodí se Halftime pro každodenní nošení?', 'Ano, jde o praktickou rukavici do mírného počasí na podzim a na jaře. Vydrží běžné nošení, ale neočekávejte zimní izolaci. Do mrazu zvolte Storm Insulated.'),
        ('Jak vybrat velikost?', 'Změřte obvod dlaně kolem kloubů a délku ruky a porovnejte s tabulkou výrobce. Rukavice má sedět těsně, ale bez tlaku. Mezi dvěma velikostmi vezměte menší u tenkých rukavic a větší u zateplených.'),
        ('Jsou pánské a dámské střihy opravdu jiné?', 'Dámské jsou užší v dlani a mají kratší prsty. Muž s menší rukou může být spokojený s dámským modelem a naopak. Řiďte se naměřenými rozměry, ne označením.'),
        ('Mají Under Armour dětské rukavice?', 'V nabídce se objevují chlapecké modely Storm. Pro nejmenší děti jsou praktičtější palčáky, které hřejí víc a snáz se oblékají. U dětí kupujte s malou rezervou a kontrolujte velikost každou sezónu.'),
        ('Jak perou tréninkové rukavice?', 'Na šetrný program nebo ručně, bez aviváže a sušení v sušičce. Kožené nebo syntetické dlaně po vyprání tvarujte a nechte volně vyschnout. Pravidelné vyvětrání zabrání zápachu.'),
        ('Hodí se tyto rukavice na lyže?', 'Na lehké běžecké lyžování ano, zvlášť tenčí modely. Na sjezdové lyžování raději zvolte specializované lyžařské rukavice s nepromokavou membránou a vyztuženou dlaní, které najdete ve zvláštní kategorii.'),
    ],
)

# ------------------------------------------------------------------ lotto-tenisky
NEW['lotto-tenisky'] = dict(
    title='Lotto tenisky: modely AMF, střih a výběr velikosti',
    desc='Lotto tenisky pro dámy, pány a děti: řady Astra, Kibra, Sirius, Spacelite a další. Střih, velikosti, materiály, péče a porovnání nabídek českých obchodů.',
    intro='<p>Lotto je italská sportovní značka, kterou v roce 1973 založila rodina z městečka Montebelluna, známého výrobou obuvi. Světově se proslavila fotbalem a tenisem, ale v českých obchodech ji nejčastěji najdete jako pohodlné volnočasové tenisky v bílé, černé a modré barvě. '
          'Na této stránce porovnáte řady jako Astra, Kibra, Sirius, Spacelite nebo Antares a průvodce vysvětlí, jak se liší dámské, pánské a dětské provedení, jak vybrat velikost a jak tenisky udržet bílé. Součástí jsou i tipy na dětskou obuv do školy a na tělocvik, protože právě tam se Lotto prodává nejčastěji. Širší přehled najdete v kategorii <a href="/tenisky/">tenisky</a> a o značce na stránce <a href="/znacka/lotto/">Lotto</a>.</p>',
    guide='<h2>Jak se v modelech Lotto vyznat</h2>'
          '<p>Značka pojmenovává tenisky krátkými jmény a zkratkami za nimi. Zkratka AMF se objevuje u většiny kousků, zbytek názvu označuje řadu, generaci a barevnost. Přesné parametry konkrétního páru najdete v popisu u obchodu, my se zaměřujeme na rozdělení podle použití.</p>'
          + T(['Označení', 'Příklady', 'Typ obuvi'], [
              ['Dámské městské', 'Astra, Venus, Antares, Court 73, Lava', 'nízké tenisky na každý den'],
              ['Pánské městské', 'Kibra, Sirius 95, Slam, Altair, SK-B 360', 'volnočasové a vycházkové boty'],
              ['Retro', 'Trainer 2000, Court 73, 1973', 'klasická silueta inspirovaná starší sportovní obuví'],
              ['Pohodlné s pěnovou podešví', 'Lunar, Love Ride', 'delší chůze, práce vstoje'],
              ['Dětské s suchým zipem', 'Arriba, Oasi, Spacelite', 'školka a škola, snadné obouvání'],
              ['Dětské sportovní', 'Whizzer, Kobalto, Run 80, Boston', 'hřiště, tělocvik, volný čas']]) +
          '<p>Lotto je dnes především značkou městské a dětské obuvi. Pokud hledáte kopačky, otevřete landing <a href="/kopacky-lotto/">kopačky Lotto</a>, kde je historická vazba značky na fotbal zachycena v nabídce.</p>'
          '<h2>Dámské Lotto tenisky</h2>'
          '<p>Dámské řady jsou nenápadné, ve světlých barvách, s tenčí podrážkou a hladkým svrškem. Hodí se k džínám, sukním i šatům a na každodenní dojíždění. Modely typu Astra nebo Venus mají klasický tvar, Antares a Lava jsou lehčí a snadno se kombinují. Pro těžší procházky vybírejte páry s měkkou stélkou a dostatečným uchycením paty. Pokud hledáte přehled ve více značkách, vyplatí se landing <a href="/damske-tenisky/">dámské tenisky</a>.</p>'
          '<h2>Pánské Lotto tenisky</h2>'
          '<p>Pánské Sirius 95, Kibra, Slam a SK-B 360 sázejí na čisté linie, bílou nebo tmavou barvu a pohodlnou podrážku. Jsou vhodné do kanceláře s volnějším dress codem, na výlety a do městského provozu. Do sportu je nepoužívejte, nemají stabilitu ani tlumení běžecké obuvi. Když chcete na běhání lehčí bota, podívejte se do kategorie <a href="/bezecka-obuv/">běžecké boty</a>.</p>'
          '<h2>Dětské Lotto boty</h2>'
          '<p>Značka je u dětí oblíbená kvůli praktickému zapínání na suchý zip a široké špičce, která nechává prstům prostor. Modely Arriba, Oasi a Spacelite jsou určené k celodennímu nošení. Děti rostou rychle, proto kupujte s rezervou asi centimetr a velikost kontrolujte každé tři až čtyři měsíce. Větší děti ocení sportovnější Whizzer, Kobalto nebo Run 80 do tělocviku. Do sálu platí, že podešev nesmí zanechávat stopy. Pro lehkou sportovní obuv zkuste i <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Změřte chodidlo večer, kdy je největší, a k délce přičtěte rezervu. Při koupi na dálku porovnejte hodnotu v centimetrech s tabulkou na stránce obchodu. Pokud jsou ve vaší velikosti recenze, které upozorňují na menší nebo větší střih, přihlédněte k nim. U dětí zkontrolujte vnitřní délku stélky a nechte prsty prostor.</p>'
          + T(['Test', 'Co sledovat'], [
              ['Pata', 'drží bez zvedání, netlačí na achilovku'],
              ['Prsty', 'mají prostor, neposouvají se dopředu'],
              ['Šířka', 'střed chodidla nevyboulí svršek'],
              ['Podrážka', 'nezahýbá se vedle klenby, neklouže'],
              ['Jazyk', 'nedře o nárt a nesjíždí na stranu']]) +
          '<h2>Materiály a barvy</h2>'
          '<p>Svršky bývají z textilu, syntetické kůže nebo jejich kombinace. Textil je lehčí a prodyšnější, ale rychleji se zašpiní, syntetická kůže se otře vlhkým hadříkem, ovšem v teple méně dýchá. Bílé tenisky vypadají svěže, a proto jsou nejčastější, ale vyžadují čištění. Černé a tmavě modré skryjí špínu a snášejí delší sezónu. Při výběru barvy myslete na to, co k nim budete nosit.</p>'
          '<h2>Jak udržet tenisky čisté</h2>'
          '<ol><li>Po použití otřete povrch vlhkým hadříkem, dokud špína nezaschne.</li>'
          '<li>Vyjměte tkaničky a vložky a vyperte je zvlášť.</li>'
          '<li>Podrážku očistěte kartáčem a jemným mýdlem.</li>'
          '<li>Sušte při pokojové teplotě, vycpané papírem, ne na topení.</li>'
          '<li>Nepoužívejte bělidla, která žloutnou na gumě.</li></ol>'
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>Oproti <a href="/nike-tenisky/">Nike teniskám</a>, <a href="/adidas-tenisky/">Adidas teniskám</a> a <a href="/puma-tenisky/">Puma teniskám</a> jsou Lotto jednodušší a nenápadnější, bez výrazných technologií. Skechers sázejí na měkké vložky, Lotto na čistý design a snadné nošení. Pro lehčí dětskou a dámskou volnočasovou obuv jde o rozumnou volbu bez módního loga, kterou lze snadno kombinovat s ostatním oblečením.</p>'
          '<p>Při srovnávání zvažte, zda obchod uvádí vnitřní délku stélky, zda je pár skladem ve vaší velikosti a zda platí vrácení do několika dnů. Rozdíl v ceně bývá u stejného modelu daný hlavně dostupností velikostí.</p>',
    faq=[
        ('Co znamená zkratka AMF v názvu Lotto bot?', 'Objevuje se v názvu většiny modelů a patří k označení řady. Přesný význam výrobce neuvádí v běžných popisech obchodů. Důležité je sledovat název modelu, generaci a velikost.'),
        ('Jsou Lotto tenisky vhodné na sport?', 'Většina modelů je určená na každodenní nošení, ne na výkonnostní sport. Pro běh volte běžeckou obuv a pro tělocvik halovou obuv s nešpinící podrážkou. Lotto kopačky jsou v samostatné nabídce.'),
        ('Jak sedí Lotto, spíš větší, nebo menší?', 'Střih bývá klasický, ale u každého modelu se může lišit. Řiďte se délkou stélky v centimetrech a recenzemi. U dětí vezměte rezervu asi centimetr.'),
        ('Které řady jsou pro dívky a ženy?', 'Dámské jsou například Astra, Venus, Antares, Court 73 a Lava. Dívčí varianty mívají názvy jako Oasi nebo Arriba. Pro obě skupiny se hodí světlé barvy a lehká podrážka.'),
        ('Mají dětské Lotto boty suchý zip?', 'Mnohé modely ano, například Arriba, Oasi a Spacelite. Je to praktické pro školku a školu. U starších dětí se vyskytují i šněrovací varianty.'),
        ('Jak vyčistit bílé tenisky?', 'Povrch otřete vlhkým hadříkem, podrážku vyčistěte kartáčem a jemným mýdlem. Tkaničky vyperte zvlášť. Nepoužívejte agresivní bělidla a nesušte na topení.'),
        ('Jsou vhodné na dlouhé chození po městě?', 'Modely s pěnovou podrážkou, například Lunar nebo Love Ride, jsou na delší chůzi pohodlnější než tenké retro tenisky. Při celodenním nošení vybírejte měkkou vložku a pevnou patu.'),
        ('Pro koho jsou pánské Sirius a Kibra?', 'Pro muže hledající nenápadné volnočasové boty do města, do kanceláře s volnějším dress codem a na výlety. Neslouží jako běžecká obuv.'),
        ('Dá se Lotto prát v pračce?', 'Většina výrobců to nedoporučuje, protože se může zdeformovat lepidlo i svršek. Čistěte ručně. Pokud štítek pračku povoluje, použijte šetrný program v ochranném pytlíku a bez ždímání.'),
        ('Kdy se Lotto tenisky slevují?', 'Slevy se objevují při změně kolekce a na konci sezóny, zejména u barev, které se přestávají vyrábět. U oblíbených velikostí se skladové zásoby rychle vyprodají. Porovnejte nabídky obchodů a sledujte dostupnost velikostí.'),
    ],
)

# ------------------------------------------------------------------ doplnění sekcí (rozšíření hloubky)
NEW['fjallraven-mikina']['guide'] += (
    '<h2>Kterou mikinu na jaké roční období</h2>'
    + T(['Období a situace', 'Rozumná volba', 'Doplněk'], [
        ['Jaro a podzim ve městě', 'bavlněná Logo nebo Vardag', 'tenká bunda proti větru'],
        ['Podzimní túra', 'lehký fleece typu Abisko Lite', 'nepromokavá bunda v batohu'],
        ['Zima v nížinách', 'hustší fleece pod zimní bundu', 'merino spodní vrstva'],
        ['Letní večery v horách', 'tenká mikina nebo větrná vrstva', 'čepice a rukavice při změně počasí'],
        ['Kempování', 'fleece s kapucí na večer', 'suché ponožky na spaní']]) +
    '<p>Z tabulky je vidět, že jedna mikina nepokryje všechno. Pokud pořizujete jen jeden kus, vybírejte podle toho, kde ho budete nosit nejčastěji. Městská bavlna prakticky nikdy nenahradí fleece na hřebeni a naopak, i když se oba kousky tváří podobně.</p>'
    '<h2>Barvy a jejich praktický význam</h2>'
    '<p>Fjällräven nabízí zemité odstíny, jako je tmavě zelená Deep Forest nebo Patina Green, i výrazné kousky, například Flame Orange. Zemité barvy splývají s krajinou a dobře skrývají zašpinění od lesa a ohně. Oranžová a modrá je zase vidět v mlze a ve sněhu, což přijde vhod při dlouhé túře, kde se skupina rozdělí. Světlé barvy, béžová nebo šedá, vypadají ve městě elegantně, ale rychleji se špiní. Nabídka barev se mění s každou sezónou, a pokud vás zaujala konkrétní, nenechávejte rozhodnutí na konec.</p>'
    '<h2>Kapuce, zip a kapsy v praxi</h2>'
    '<p>Kapuce se u fleecových mikin hodí hlavně ve stanu a při pauze na větru, na chůzi pod bundou překáží. Zip dlouhý do poloviny těla umožní odvětrat po stoupání, krátký zip u krku je lehčí a méně se otírá. U kapes sledujte, zda jsou přístupné i s batohem na zádech, protože bederní pás většinu kapes zakryje. Kapsa na hrudi je praktická na mapu nebo telefon, rukavice se vejdou do bočních kapes.</p>'
)
NEW['fjallraven-mikina']['faq'] += [
    ('Hodí se mikina Fjällräven jako dárek?', 'Ano, bavlněné Logo Hoodie nebo 1960 Logo Badge Sweater jsou nenápadné a lze je nosit v každé situaci. U velikosti raději volte volnější střih nebo si předem ověřte, jakou velikost obdarovaný nosí. Barvu vybírejte neutrální.'),
]

NEW['icebreaker-ponozky']['intro'] = NEW['icebreaker-ponozky']['intro'].replace('Hned se tak dá poznat,', 'Díky tomu se dá snadno poznat,')
NEW['icebreaker-ponozky']['guide'] += (
    '<h2>Sladění ponožky a boty</h2>'
    + T(['Obuv', 'Rozumná délka', 'Tloušťka'], [
        ['Nízká běžecká bota', 'Micro nebo Mini', 'Ultralight'],
        ['Tenisky a polobotky', 'Mini nebo Crew', 'Light'],
        ['Turistická nízká obuv', 'Crew', 'Light až Medium'],
        ['Vysoká trekingová bota', 'Mid Calf', 'Medium až Heavy'],
        ['Lyžařské boty a snowboard', 'OTC', 'Light až Medium'],
        ['Zimní holínky nebo kozačky', 'Mid Calf nebo OTC', 'Medium až Heavy']]) +
    '<p>Délka ponožky se řídí okrajem boty. Pokud lem ponožky končí přesně na okraji boty, tlačí na kůži a způsobuje otlaky. Proto se do vysoké boty vybírá Mid Calf, aby okraj ponožky končil nad botou, zatímco nízký střih Micro by se v ní sjížděl dolů.</p>'
    '<h2>Prevence puchýřů na túře</h2>'
    '<p>Puchýř vzniká třením a vlhkem, ne jen novou botou. Merino pomáhá tím, že vlhkost odvádí a nehromadí se u kůže. Přesto na dlouhou túru dodržte několik zásad:</p>'
    '<ul><li>Ponožky vždy zkoušejte s botou, kterou ponesete na trase.</li>'
    '<li>Zkontrolujte, že uvnitř nejsou záhyby, zvlášť na špičce a patě.</li>'
    '<li>Při pauze boty rozvažte a ponožky vyvětrejte, v druhé ponožce je chodidlo na chvíli sušší.</li>'
    '<li>Na první horké místo reagujte hned a zastavte se dřív, než se z červené skvrny stane puchýř.</li>'
    '<li>Na vícedenní výlet zabalte aspoň jeden pár navíc.</li></ul>'
    '<h2>Dvouvrstvý systém s Liner ponožkou</h2>'
    '<p>Liner je tenká vnitřní ponožka, která se obléká pod silnější. Tření se přesune mezi ponožky, ne mezi ponožku a kůži, takže je méně odřenin na patách a prstech. Vyzkoušejte ji, pokud se vám i v dobře padnoucích botách tvoří puchýře, a chcete si před delší trasou ověřit komfort. Dvojitá vrstva ale vyžaduje o něco prostornější botu, proto se do těsné obuvi nehodí.</p>'
)
NEW['icebreaker-ponozky']['faq'] += [
    ('Je vhodné nosit vlněnou ponožku v létě?', 'Ano, tenké Ultralight a Light modely jsou prodyšné a nepřehřívají. Vlna navíc tlumí zápach při celodenním nošení. Pro teplé dny volte nízký střih a vzdušné pletení.'),
]

NEW['under-armour-rukavice']['intro'] = NEW['under-armour-rukavice']['intro'].replace('Na této stránce uvidíte', 'Na této stránce hned uvidíte')
NEW['under-armour-rukavice']['guide'] += (
    '<h2>Jakou rukavici vybrat podle počasí</h2>'
    + T(['Počasí', 'Volba', 'Proč'], [
        ['Mírný chlad, ráno a večer', 'Halftime nebo Storm Liner', 'hřeje, ale nepřehřívá při pohybu'],
        ['Chlad s větrem', 'Storm Run', 'tenčí vrstva a těsný střih proti proudění'],
        ['Mráz a stání na místě', 'Storm Insulated', 'zateplení drží teplo bez pohybu'],
        ['Mokrý sníh', 'lyžařská rukavice s membránou', 'běžná sportovní rukavice navlhne'],
        ['Posilovna a hrazda', 'Training nebo Weightlifting', 'ochrana dlaně, žádné zateplení'],
        ['Golf v zimě', 'Drive Cart Mitt', 'palčák na ruku mezi údery']]) +
    '<p>Rukavice samy o sobě nezachrání zmrzlé ruce, pokud je tělo podchlazené. Oblékněte se proto kompletně, včetně čepice a vrstvy na trupu. Z oblečení značky se k rukavicím hodí třeba <a href="/ksiltovka-under-armour/">kšiltovka Under Armour</a> nebo <a href="/under-armour-ponozky/">ponožky Under Armour</a>.</p>'
    '<h2>Golf a další aktivity s palčáky</h2>'
    '<p>Golfové rukavice a palčáky, jako je Drive Cart Mitt, se používají mezi údery. Hráč si je nasadí, když čeká u vozíku, a při úderu sundá. Zateplená konstrukce brání tomu, aby ruce vychladly na delším kole. Pro jiné sporty, třeba pro rybářskou nebo zahradní práci v chladu, jsou praktické tenké rukavice Liner, které nebrání jemné práci prstů.</p>'
    '<h2>Dětské rukavice a ztráta kusu</h2>'
    '<p>Děti rukavice často ztrácejí. Pomůže pevná gumička nebo klip, který spojí obě rukavice v rukávu. Chlapecké modely Storm jsou menší v obvodu dlaně a mají delší manžetu, aby sníh nezapadal pod rukáv. Pro školu a hřiště si vybírejte tmavou barvu, která se nezašpiní. Pokud děti sáňkují, hodí se palčák, nikoli prstová rukavice. Na zimní hry s mokrým sněhem počítejte s náhradním párem, který čeká v tašce suchý.</p>'
)
NEW['under-armour-rukavice']['faq'] += [
    ('Jak poznám, že je rukavice opotřebovaná?', 'Podívejte se na dlaň a špičky prstů. Pokud se látka protřela nebo se odlepuje zesílení, ztrácí rukavice úchop i izolaci. Povolené švy a ztvrdlý materiál po praní jsou dalším znamením.'),
]

NEW['lotto-tenisky']['guide'] += (
    '<h2>Značka v kostce</h2>'
    '<p>Lotto vzniklo v roce 1973 v oblasti Montebelluna v severní Itálii, kde sídlí velká část evropské výroby sportovní obuvi. Počátky značky jsou spojené s fotbalem a tenisem, proto se v názvech modelů objevují čísla jako 73 a 1973, která odkazují na rok založení. Dnes ji spojujeme hlavně s dostupnou obuví na každý den, nikoli s technicky náročným sportem.</p>'
    '<h2>Podrážka, tlumení a pohodlí</h2>'
    '<p>Tenisky se liší tím, jak je podešev tlustá a z jakého materiálu. Tenká gumová podrážka retro modelů je lehká a stabilní, ale tlumí málo, takže při celodenní chůzi po dlažbě pocítíte tvrdý povrch. Pěnová mezipodešev u modelů typu Lunar nebo Love Ride pohodlněji pružinuje a hodí se pro práci vstoje. Po několika stech kilometrech se pěna sesedne a tlumení slábne, což je přirozené. Když tenisky začnou být tvrdé, vyměňte je, nebo aspoň vložky. Tlumení nejvíc poznáte po dni strávenému na nohou: pokud večer bolí paty a klenba, bota už pravděpodobně dosloužila.</p>'
    '<h2>Dětská velikost a rychlý růst</h2>'
    + T(['Období', 'Jak často kontrolovat', 'Na co dát pozor'], [
        ['Batolata a předškoláci', 'zhruba každé tři měsíce', 'prsty se v botě nesmí opírat o špičku'],
        ['Mladší školáci', 'každou sezónu', 'suchý zip má pevně držet patu'],
        ['Starší školáci', 'dvakrát ročně', 'střed chodidla se nemá bortit'],
        ['Dospívající', 'při pocitu tlaku', 'šířka přední části chodidla']]) +
    '<p>Dětskou botu zkoušejte s ponožkou, kterou dítě nosí. Nechte je stát, ne sedět, protože ve stoje se chodidlo prodlouží. Zmáčkněte špičku, a pokud nahmatáte prsty těsně u okraje, bota je malá. Starší tenisky po sourozenci nepřejímejte u dětí, které mají problémy s chodidlem, protože vyšlapaná stélka formuje nohu jinak.</p>'
    '<h2>Tenisky do školy a do tělocvičny</h2>'
    '<p>Na přezutí ve škole se hodí bílá podrážka, která nezanechává stopy, a suchý zip, který zvládnou i malé děti. Do tělocvičny vyberte lehkou sálovou obuv s ohebnou podešví, ne klasické městské tenisky s tvrdou gumou. Některé školy žádají světlou podrážku, proto se před koupí zeptejte, co vyžaduje vaše škola.</p>'
    '<h2>Kombinace a nošení v roce</h2>'
    '<p>Světlé textilní modely se hodí na jaro a léto k lehkým kalhotám a kraťasům. V chladnějších měsících sáhněte po tmavých syntetických kouscích, které snesou vlhkost. Na deštivé dny nosit bílý textil nemá smysl, špinavá voda se do něj vsákne. Lotto tenisky se dobře kombinují s mikinou nebo s bundou, a pokud chcete celý sportovní outfit, najdete vybavení od <a href="/sportovni-obuv/">sportovní obuvi</a> po oblečení v jednotném stylu.</p>'
)
NEW['lotto-tenisky']['faq'] += [
    ('Jak dlouho tenisky Lotto vydrží?', 'Záleží na nošení a materiálu. Při každodenním používání se nejdřív sesedne pěna a opotřebuje podrážka. Střídání dvou párů a sušení při pokojové teplotě životnost výrazně prodlouží.'),
    ('Dají se Lotto nosit celoročně?', 'V jarních, letních a podzimních měsících ano. V zimě tenisky nehřejí a při mokru nechrání, proto zvolte zimní obuv. Pro mrazy se hodí i vlněné ponožky.'),
]
