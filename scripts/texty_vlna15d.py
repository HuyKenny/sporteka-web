"""sporteka.cz — wave 15d (4. 11. 2026): long texts (>= 1650 words) for merino-pradlo, sportovni-sukne-a-saty, rybarske-navijaky, sedla-a-gripy.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ merino-pradlo
NEW['merino-pradlo'] = dict(long=True,
    title='Merino spodní prádlo a legíny: výběr, péče | Sporteka',
    desc='Merino spodní prádlo, legíny a spodní vrstvy pro muže, ženy i děti: gramáž, střih, velikost a praní. Průvodce a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Merino prádlo</strong> je spodní vrstva, kterou si lidé obvykle koupí jednou a pak se k ní vracejí. Jemná vlna z ovcí merino se na kůži nekousá tak jako obyčejná vlna, drží teplo i ve chvíli, kdy se trochu zpotíte, a po delším nošení nezačne nepříjemně zapáchat. Proto se hodí na hory, na kolo, na dlouhé túry a stejně dobře i do studené kanceláře.</p>'
          '<p>Na Sportece najdete <strong>merino legíny, spodky, dlouhé spodní vrstvy a komplety</strong> pánské, dámské i dětské z českých obchodů a nabídky porovnáte vedle sebe. Hledáte-li horní díl, podívejte se do kategorie <a href="/merino-tricka/">merino trička a tílka</a>, na teplo pro nohy do <a href="/merino-ponozky/">merino ponožek</a> a na celou skupinu do rozcestníku <a href="/merino/">merino oblečení</a>. Dole najdete i průvodce gramáží, střihem a praním.</p>',
    guide='<h2>Co je merino a proč se hodí jako spodní vrstva</h2>'
          '<p>Merino vlákno je výrazně tenčí než vlákno běžné vlny. Díky tomu se při dotyku ohýbá a nepíchá, takže ho většina lidí snese přímo na kůži. Vlněné vlákno má navíc vlastnost, kterou umělá vlákna napodobují jen částečně: pohlcuje vodní páru z těla dovnitř svého jádra a navenek zůstává relativně suché. Tělo se proto při námaze méně ochlazuje a prádlo nepůsobí vlhce tak brzy.</p>'
          '<p>Další výhodou je pomalejší vznik zápachu. Vlna nesbírá pach tak ochotně jako polyester, takže zvládne několik dnů v řadě bez praní, což ocení hlavně lidé na vícedenních trasách. Nevýhodou je menší pevnost proti syntetice. Čisté merino se v místech tření a při hrubém zacházení otírá dřív, proto výrobci často přidávají nylon nebo elastan.</p>'
          '<h2>Jaké druhy merino prádla najdete v nabídce</h2>'
          '<ul><li><strong>Dlouhé spodní kalhoty</strong> sahají od pasu až ke kotníkům a pod kalhoty vytvoří hřejivou vrstvu bez objemu.</li>'
          '<li><strong>Legíny</strong> mají přiléhavější střih a lépe se nosí samostatně, například při běhu v chladu nebo jako domácí oblečení.</li>'
          '<li><strong>Boxerky, slipy a kalhotky</strong> z merina se nosí celoročně a hodí se i v létě na kolo.</li>'
          '<li><strong>Dlouhé spodní vrstvy s rukávem</strong> a <strong>komplety</strong> spojují horní díl a kalhoty v jednom stylu, takže se barvy i gramáž shodují.</li>'
          '<li><strong>Dětské merino prádlo</strong> pomáhá hlavně u dětí, které mnoho času tráví venku, protože je hřeje i při pohybu a nevadí jim na pokožce.</li>'
          '<li><strong>Podprsenky a sportovní topy</strong> z vlny se hledají mezi <a href="/sportovni-podprsenky/">sportovními podprsenkami</a>, protože tam se řeší podpora a nosit ji pod merino triko je běžná kombinace.</li></ul>'
          '<h2>Gramáž: jak teplé prádlo zvolit</h2>'
          '<p>Gramáž udává hmotnost materiálu na čtvereční metr. Čím vyšší číslo, tím silnější a teplejší úplet. Nejde o přesnou vědu, protože dvě značky se stejnou gramáží mohou hřát odlišně, ale k orientaci to stačí.</p>'
          + T(['Vrstva', 'Charakter', 'Kdy ji zvolit'], [
              ['Lehká', 'tenká, rychle schne, na těle skoro nevnímáte', 'podzim, jaro, běh, kolo, pobyt v teplých domech'],
              ['Střední', 'univerzální volba, hřeje a stále dýchá', 'zimní túry, běžky, celodenní pobyt venku'],
              ['Těžká', 'silná a hřejivá, hůř se prostřídává', 'mráz, zimní spaní, statické činnosti jako rybaření nebo pozorování']]) +
          '<p>Pokud kupujete jedno prádlo na všechno, sáhněte po střední gramáži. Na aktivity s vysokou intenzitou, kde se zpotíte hned, je lepší lehká vrstva a teplo dodat dalším oblečením. Při statickém pobytu venku se naopak vyplatí silnější vrstva, protože tělo teplo nevyrábí a prádlo ho jen drží.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Spodní vrstva musí přiléhat, jinak neplní svou funkci. Mezi kůží a látkou nesmí vznikat volný prostor, v němž se zadržuje studený vzduch a ve kterém se pot nemá kam vsáknout. Zároveň by nemělo nic škrtit, stahovat nebo tlačit ve švech. Zkoušejte prádlo v pohybu: dřep, předklon a zvednutí nohy. Pás nemá sjíždět ani zařezávat se.</p>'
          '<p>Nové prádlo bývá po prvním praní o něco měkčí a přilne k tělu víc. Pokud váháte mezi dvěma velikostmi, zkontrolujte tabulku výrobce a délku nohavic. U vyšších lidí je častým problémem příliš krátká nohavice, která se při sedu vyhrnuje nad kotník.</p>'
          '<h3>Pánské, dámské a dětské modely</h3>'
          '<p>Dámské střihy bývají užší v pase a širší v bocích, pánské mají v rozkroku zpravidla jiné řešení, a proto se vyplatí držet se označení. U dětí řešte hlavně růst. Kalhoty s pružným pasem nebo pletenou manžetou vydrží déle, protože se dají zrolovat. Oblečení pro nejmenší by mělo mít hladké, ploché švy.</p>'
          '<h2>Značky, které najdete na Sportece</h2>'
          f'<p>V nabídce merino prádla dominují značky {B(("icebreaker", "Icebreaker"), ("sensor", "Sensor"), ("smartwool", "Smartwool"), ("lasting", "Lasting"), ("viking", "Viking"), ("husky", "Husky"))}. Dále ve výběru najdete {B(("devold", "Devold"), ("helly-hansen", "Helly Hansen"), ("kari-traa", "Kari Traa"), ("simond", "Simond"), ("klimatex", "Klimatex"))}. Každá se trochu liší střihem, množstvím příměsi a způsobem zpracování švů, takže stejná velikost nemusí padnout stejně. Spolehlivý způsob, jak se vyhnout vracení, je porovnat rozměry v tabulce s vlastním pasem a délkou vnitřní strany nohy.</p>'
          '<h2>Kombinace s dalšími vrstvami</h2>'
          '<p>Merino prádlo je základ třívrstvého systému. Nad něj přijde izolační vrstva, například fleece nebo lehká péřovka, a nakonec ochrana proti větru a vodě. Pokud celý systém navazuje, nemusí být spodní vrstva extrémně silná. Na zimní sporty se vyplatí zkontrolovat i speciální nabídku v kategorii <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a> a na univerzální funkční vrstvy v rozcestníku <a href="/termopradlo/">termoprádlo</a>. Pro vrchní díl je k dispozici i <a href="/merino-mikiny/">merino mikiny</a> a drobnosti včetně čepic či nákrčníků v <a href="/merino-doplnky/">merino doplňcích</a>.</p>'
          '<h2>Pro koho je merino prádlo vhodné</h2>'
          '<ul><li><strong>Turisté a trekaři</strong> na delších trasách, kde se nedá prát každý večer.</li>'
          '<li><strong>Lyžaři a běžkaři</strong>, kteří se v kopci zahřejí a pak v lanovce nebo sjezdu rychle chladnou, viz <a href="/bezecke-lyzovani/">běžecké lyžování</a> nebo <a href="/skialpinismus/">skialpinismus</a>.</li>'
          '<li><strong>Cyklisté</strong> na dlouhé jízdy v proměnlivém počasí.</li>'
          '<li><strong>Lidé s citlivou pokožkou</strong>, kterým obyčejná vlna vadí. Zkuste lehčí gramáž a prádlo si v obchodě osaháte.</li>'
          '<li><strong>Rodiče dětí</strong>, které tráví zimu na sněhu a na hřišti.</li>'
          '<li><strong>Zaměstnanci v chladných provozech</strong> a všichni, kdo hledají teplo bez objemu pod oblek či pracovní kalhoty.</li></ul>'
          '<h2>Péče o merino prádlo krok za krokem</h2>'
          '<p>Správná péče zdvojnásobí životnost, nesprávná ji zkrátí na pár sezón. Řiďte se vždy štítkem, ale několik zásad platí téměř univerzálně.</p>'
          '<ol><li>Perte na šetrný program, většinou do 30 °C, s jemným prostředkem určeným na vlnu nebo funkční textil.</li>'
          '<li>Nepoužívejte aviváž. Zalepí vlákna a omezí odvod vlhkosti.</li>'
          '<li>Neždímejte vysokými otáčkami a neždímejte ručním kroucením.</li>'
          '<li>Sušte rozložené na vzduchu, mimo přímý zdroj tepla. Sušička nebo radiátor mohou vlnu srazit.</li>'
          '<li>Před nošením po delší době zkontrolujte, zda nejsou v prádle moli. Do skříně patří čisté a suché prádlo, ne zpocené z výletu.</li>'
          '<li>Drobnou dírku zašijte hned, dokud se nezvětší.</li></ol>'
          '<h2>Časté chyby při nákupu a nošení</h2>'
          '<ul><li>Příliš volná velikost, ve které prádlo nepracuje jako vrstva.</li>'
          '<li>Bavlněné triko nebo spodní prádlo pod merinem: bavlna nasákne potem a vlna už nic nezachrání.</li>'
          '<li>Nošení těžké gramáže při intenzivním pohybu, kdy se tělo přehřívá.</li>'
          '<li>Praní s drsným oblečením a zipy, které vlákna škrábou.</li>'
          '<li>Sušení na topení, po němž se prádlo zkrátí.</li>'
          '<li>Očekávání, že směsové prádlo bude stejně hebké jako čisté merino.</li></ul>'
          '<h2>Merino prádlo podle sportu a činnosti</h2>'
          + T(['Činnost', 'Doporučený přístup', 'Poznámka'], [
              ['Zimní túra', 'střední gramáž, dlouhé kalhoty, k tomu <a href="/trekova-obuv/">trekové boty</a>', 'v batohu mějte suchou náhradní vrstvu na večer'],
              ['Běh v chladu', 'lehké legíny nebo přiléhavé spodky', 'nad nimi stačí tenká větrovka'],
              ['Spaní ve stanu nebo chatě', 'střední až těžká gramáž', 'doplní <a href="/spaci-pytle/">spacák</a> a vložku, viz <a href="/vlozky-do-spacaku/">vložky do spacáků</a>'],
              ['Kolo na podzim', 'lehká vrstva pod cyklistické kalhoty', 'dbejte na bezešvou plochu v místě sedla'],
              ['Každodenní nošení', 'lehké legíny pod sukni nebo kalhoty', 'dobře funguje i u sedavé práce v chladném prostoru']]) +
          '<h2>Jak poznat kvalitní zpracování</h2>'
          '<p>Hned po rozbalení zkontrolujte švy. Ploché švy nebo šití bez výstupků se nezařezávají a při dlouhém nošení netlačí. Úplet by měl být rovnoměrný, bez řídkých míst a bez viditelných zátrhů. Pas má držet tvar, ale nemá se zařezávat, a gumička uvnitř by neměla škrábat. Zkuste prádlo lehce natáhnout. Pokud se po chvíli vrátí do původního tvaru, je pružnost v pořádku. Kontrolujte i značku s uvedením složení, protože vám prozradí, kolik merina v prádle skutečně je.</p>'
          '<h2>Balení na cesty a skladování</h2>'
          '<p>Merino je skvělé do batohu, protože zabírá málo místa a nemusí se prát každý den. Na cestách ho po dni nošení pověste ven na vzduch, nejlépe do stínu, a ráno bývá opět svěží. Na delší dobu prádlo ukládejte vyprané, suché a složené, ne zavěšené, aby se úplet nevytahoval. Do skříně patří přírodní repelent proti molům, například cedrové dřevo, a pravidelná kontrola. Pokud potřebujete lehčí tašku, najdete vhodné zavazadlo mezi <a href="/turisticke-batohy/">turistickými batohy</a> nebo v kategorii <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>, kde si porovnáte i syntetické alternativy.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>V seznamu můžete filtrovat podle velikosti, značky a barvy. U každého produktu vidíte nabídky z více obchodů, takže snadno porovnáte, kdo má vaši velikost skladem a jak vypadá doprava. Před objednávkou si ověřte materiálové složení, protože se označení „merino“ používá pro čisté i smíšené materiály. Prádlo si koupíte nejlépe na konci sezóny, kdy se obchody zbavují zásob, ale velikosti už někdy chybí. Pokud potřebujete konkrétní kus, objednejte včas.</p>',
    faq=[
        ('Hodí se merino spodní prádlo i do léta?', 'Ano, lehká gramáž dobře funguje i v teple, například na kolo nebo do hor, protože vlna odvádí vlhkost a nezačíná tak rychle zapáchat. Letní prádlo volte z tenkého úpletu.'),
        ('Kolikrát se může merino prádlo nosit bez praní?', 'Obecně vydrží déle než syntetika, protože pomaleji zachycuje pach. Po jednom až dvou dnech stačí vyvětrat. Po větším zpocení nebo po dlouhém nošení ale praní patří.'),
        ('Jaký je rozdíl mezi merino legíny a spodními kalhotami?', 'Legíny jsou přiléhavější a hodí se i samostatně, spodní kalhoty jsou určené především jako vrstva pod další oblečení. Liší se střihem pasu, délkou a často i gramáží.'),
        ('Pere se merino prádlo v pračce?', 'Většina modelů ano, ale na šetrný program s nízkou teplotou, s jemným prostředkem a bez aviváže. Přesný postup uvádí štítek.'),
        ('Proč se merino prádlo srazí?', 'Vlna reaguje na teplo, tření a prudké ždímání. Při horké vodě, sušičce nebo agresivním programu se vlákna zhustí a oblečení se zmenší.'),
        ('Je merino vhodné pro děti?', 'Často ano, protože hřeje i při pohybu a bývá měkké. U velmi citlivé pokožky je dobré začít lehčí gramáží a prádlo před prvním nošením vyprat.'),
        ('Kousá merino prádlo?', 'Kvalitní jemné merino by kousat nemělo, ale citlivost je individuální. Pomáhá lehčí gramáž, hladký úplet a ploché švy. Pokud pokožka reaguje, zkuste jinou značku nebo směs.'),
        ('Jakou velikost zvolit, když jsem mezi dvěma?', 'Spodní vrstva má přiléhat, proto obvykle sáhněte po menší velikosti. U vyšších osob dejte přednost delšímu střihu. Vždy porovnejte rozměry v tabulce výrobce.'),
        ('Je merino náročné na údržbu?', 'Není, ale nesnáší jen hrubé zacházení. Pokud ho perete šetrně a sušíte na vzduchu, zachová tvar i měkkost řadu let.'),
        ('Jak poznat směsové merino od čistého?', 'Složení najdete na štítku a v popisu produktu. Směsi s nylonem nebo elastanem jsou odolnější, elastičtější a rychleji schnou, čisté merino bývá měkčí, ale lépe se nosí šetrně.'),
    ])

# ------------------------------------------------------------------ sportovni-sukne-a-saty
NEW['sportovni-sukne-a-saty'] = dict(long=True,
    title='Sportovní sukně a šaty na tenis, golf, fitness | Sporteka',
    desc='Sportovní sukně, sukně se šortkami a sportovní šaty pro tenis, golf, badminton i volný čas: střih, délka, materiál a velikost. Porovnání obchodů.',
    intro='<p><strong>Sportovní sukně a šaty</strong> spojují volnost pohybu s ženským střihem. Bývají lehké, pružné a uvnitř často doplněné krátkými šortkami, takže se v nich dá bez obav běhat, skákat i dřepovat. Hodí se na kurt, na golfové hřiště, na lekci tance i na výlet, kdy nechcete oblékat těsné legíny.</p>'
          '<p>Na Sportece porovnáte <strong>sportovní sukně, sukně se šortkami a sportovní šaty</strong> z nabídky českých e-shopů a uvidíte nabídky vedle sebe. K sukni se dobře hodí <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/tilka/">tílka</a> nebo <a href="/sportovni-podprsenky/">sportovní podprsenky</a>. Pokud hledáte jiné řešení pro dolní díl, zkuste <a href="/leginy/">legíny</a> či <a href="/sportovni-kratasy/">sportovní kraťasy</a>. Pod přehledem najdete průvodce délkou, střihem a materiálem.</p>',
    guide='<h2>Proč zvolit sportovní sukni místo kraťasů nebo legín</h2>'
          '<p>Sukně se nosí kvůli pohodlí, vzhledu i praktičnosti. Nohy se v ní nezahřívají tak jako v dlouhých legínách, vzduch pod sukní proudí a pohyb nic nestahuje. Ve většině raketových sportů jde navíc o zvyk a řada hráček má sukni ráda kvůli volnosti kroku. Pokud vám vadí, že by se mohla zvednout, hledejte model s integrovanými šortkami.</p>'
          '<p>Sportovní šaty fungují podobně, jen nahrazují dva kusy oblečení jedním. Na hřišti se tím zjednoduší balení a vzhled je sladěný. Pro každodenní nošení se hodí lehké pružné šaty z funkčního úpletu, které se nemačkají.</p>'
          '<h2>Typy sportovních sukní a šatů</h2>'
          '<ul><li><strong>Sukně se šortkami</strong> mají vnitřní kalhotky nebo kraťasy, často s kapsou na míček. Jsou nejuniverzálnější volbou.</li>'
          '<li><strong>Skorty</strong> vypadají jako sukně, ale vpředu je přeložená látka, pod ní krátké kalhotky. Jsou praktické na golf.</li>'
          '<li><strong>Plisované sukně</strong> mají klasický sportovní vzhled a při pohybu příjemně vlají.</li>'
          '<li><strong>Rovné pružné sukně</strong> sedí těsněji a hodí se na fitness, do města i pod bundu.</li>'
          '<li><strong>Tenisové šaty</strong> mají často zabudovanou podprsenku nebo širší ramínka a bývají střižené s ohledem na pohyb paží.</li>'
          '<li><strong>Volnočasové sportovní šaty</strong> jsou delší, volnější a hodí se na pláž nebo do města.</li>'
          '<li><strong>Dětské sukně a šaty</strong> pro dívky ke sportu, tanci i škole. Mívají pevnější švy a pružný pas.</li></ul>'
          '<h2>Délka a střih podle sportu</h2>'
          + T(['Sport', 'Obvyklá délka', 'Na co dbát'], [
              ['Tenis, padel, badminton', 'krátká až střední', 'integrované šortky, kapsy na míčky, pružný pas, viz <a href="/tenis/">tenis</a> a <a href="/padel/">padel</a>'],
              ['Golf', 'střední, často skort', 'pohodlný krok, kapsa na míček, ochrana před sluncem, více v <a href="/golf/">golfu</a>'],
              ['Fitness a jóga', 'těsnější střih nebo legíny pod sukní', 'sukně se nesmí při předklonu zvedat'],
              ['Tanec a gymnastika', 'krátká, pružná', 'volnost bokem, sladění s <a href="/tanecni-obleceni/">tanečním oblečením</a>'],
              ['Volný čas a výlety', 'delší, volnější', 'rychleschnoucí materiál, kapsy, případně vrstvení']]) +
          '<p>Délka není jen estetická. Krátká sukně dává volnost kroku, ale vyžaduje kvalitní integrované šortky. Delší sukně lépe chrání před sluncem, ale může se zamotat do nohou při prudkém pohybu. Zkuste se předklonit, dřepnout a zvednout nohu, abyste zjistili, jak se sukně chová.</p>'
          '<h2>Materiál a funkční vlastnosti</h2>'
          '<p>Většina sportovních sukní je z polyesteru, polyamidu a elastanu. Polyester rychle schne a nemačká se, polyamid je měkčí na dotyk a elastan zajišťuje pružnost. Bavlněné směsi jsou příjemné ve městě, ale při větší námaze nasáknou potem a pomalu schnou. Pokud sportujete venku, hledejte označení jako rychleschnoucí, prodyšná nebo s UV ochranou. Reálnou ochranu před sluncem prověřte v popisu výrobce.</p>'
          '<p>Důležité jsou také švy a pas. Plochý pas se nezařezává při předklonu a elastický lem brání sjíždění při pohybu. Vnitřní šortky by neměly být přehnaně těsné, nemají se vyhrnovat a lem na stehně nesmí tlačit.</p>'
          '<h2>Velikost a zkoušení</h2>'
          '<p>Sportovní sukně sedí na pase a boku, takže se řiďte oběma rozměry. Při dvou velikostech zvolte tu, v níž se pohodlně posadíte do dřepu. Příliš těsná sukně se vyhrnuje, příliš volná sjíždí. U šatů se vyplatí zkontrolovat i délku trupu a šířku ramínek. Pokud nosíte pod šaty sportovní podprsenku, ověřte, aby nebyla vidět v rukávech a výstřihu. Velikostní tabulky se u různých značek liší, takže vždy porovnejte rozměry v centimetrech.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Nabídka obsahuje značky {B(("loap", "Loap"), ("litex", "Litex"), ("gap", "Gap"), ("woox", "Woox"), ("hannah", "Hannah"), ("alpine-pro", "Alpine Pro"), ("lotto", "Lotto"), ("evona", "Evona"))}. Najdete také {B(("silvini", "Silvini"), ("4f", "4F"), ("northfinder", "Northfinder"), ("adidas", "Adidas"), ("kilpi", "Kilpi"), ("willard", "Willard"))}. Některé značky se zaměřují hlavně na sport a outdoor, jiné nabízejí volnější oblečení do města, takže před nákupem sledujte popis. Sportovně laděné kousky bývají určené pro pohyb a mají lepší pružnost než čistě módní model.</p>'
          '<h2>Co se hodí k sukni</h2>'
          '<p>K sukni zvolte střih, který nehromadí látku v pase. Přiléhavé <a href="/funkcni-tricka/">funkční tričko</a> nebo tílko vytvoří vyvážený vzhled, na chladnější den přidejte <a href="/mikiny/">mikinu</a>. K tenisu patří <a href="/tenisova-obuv/">tenisová obuv</a> a <a href="/tenisove-rakety/">tenisové rakety</a>, na golf <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a>. Při běhu v sukni myslete na vhodné <a href="/bezecka-obuv/">běžecké boty</a>. V létě se vyplatí chránit kůži před sluncem a vybrat <a href="/lycra-a-uv-tricka/">UV trička</a>.</p>'
          '<h2>Pro koho je sportovní sukně vhodná</h2>'
          '<ul><li><strong>Hráčky raketových sportů</strong>, které chtějí volný krok a praktické kapsy.</li>'
          '<li><strong>Golfistky</strong>, pro které je důležité pohodlí při švihu.</li>'
          '<li><strong>Tanečnice a gymnastky</strong>, hlavně v tréninku a při vystoupeních.</li>'
          '<li><strong>Děvčata ve škole nebo kroužku</strong>, kde se hodí pevná sukně s šortkami.</li>'
          '<li><strong>Ženy, které nechtějí těsné legíny</strong>, ale chtějí pohodlí pro chůzi či výlet.</li>'
          '<li><strong>Cestovatelky</strong>, protože sukně i šaty z funkčního úpletu zabírají v batohu minimum místa.</li></ul>'
          '<h2>Péče o sportovní sukně a šaty</h2>'
          '<p>Funkční materiály perte na šetrný program, nejlépe obrácené naruby, s jemným prostředkem. Aviváž zalepuje vlákna a snižuje odvod vlhkosti. Plisování vydrží déle, pokud sukni po praní pověsíte a zbytečně nežmoulíte. Neždímejte vysokými otáčkami, nesušte na radiátoru ani v sušičce, pokud to štítek nedovolí. Pozor na zipy a suchý zip, které při praní zachytí jemnou látku. Skvrny od trávy nebo hlíny ošetřete dřív, než zaschnou, a nepoužívejte bělidlo.</p>'
          '<h2>Integrované šortky: na co se zaměřit</h2>'
          '<p>Vnitřní kalhotky rozhodují o pohodlí víc než samotná sukně. Měly by přiléhat na stehnech, ale nesmí je stahovat, a lem se nemá vyhrnovat. Kratší nohavička se při kroku do strany může vyhrnout, delší chrání před třením stehen. Zkontrolujte, zda je materiál uvnitř hladký a švy ploché, protože právě tam vzniká otlak při opakovaném pohybu. Některé šortky mají silikonový proužek, který brání sjíždění, jiné jen pružný lem. Pokud vám silikonový proužek vadí, hledejte model s pružným lemem.</p>'
          '<p>Ve většině sukní jsou šortky našité napevno, takže je nejde vyměnit. Když vám vyhovují jiné kalhotky, vybírejte sukni bez nich a kombinujte s kraťasy nebo spodním dílem podle vlastního výběru, třeba z <a href="/sportovni-spodni-pradlo/">sportovního spodního prádla</a>.</p>'
          '<h2>Sezóna a vrstvení</h2>'
          '<p>Sukně se nemusí nosit jen v létě. Na jaře a na podzim ji lze kombinovat s legínami nebo s dlouhými ponožkami a ve větru ji doplní lehká větrovka. Na kurtu se přes zahřívací tričko obléká mikina, kterou si hráčka při zahřátí sundá. Při zimním pobytu venku se sukně ke sportu příliš nehodí, ale pod ni lze obléknout teplé spodní vrstvy. V létě se vyplatí volit světlé barvy, které se méně zahřívají, a kombinovat je s pokrývkou hlavy a opalovacím krémem.</p>'
          '<h3>Barvy a vzory</h3>'
          '<p>Bílá je na sportovišti klasika, ale na ní se projeví každá skvrna. Tmavé a středně sytě zbarvené kusy zakryjí drobné nečistoty a lépe se hodí na výlety. Vzory a pruhy zdůrazňují linii, a proto je před nákupem posuďte na fotografiích z více úhlů. Pokud potřebujete více kusů v souladu, zvolte jednu barevnou paletu a kombinujte s jednoduchými doplňky.</p>'
          '<h2>Sukně a šaty pro děti a dorost</h2>'
          '<p>Dívky potřebují oblečení, které vydrží běhání, kolo i cvičení v tělocvičně. Zkontrolujte, zda je pas pružný a nešije se do těla, a ověřte, že šortky uvnitř nesjíždějí. Nižší dítě ocení kratší sukni, která se nezachytí o kolena při skákání. Raději volte jednodušší střih bez mnoha ozdob, které se při praní trhají. Pokud dcera roste, vyplatí se model s pružným pasem a mírně delším lemem, který snese přizpůsobení o jednu velikost. Další vybavení pro mladé hráčky najdete v kategoriích <a href="/badminton/">badminton</a> a <a href="/stolni-tenis/">stolní tenis</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě pouze podle vzhledu, bez zkoušky pohybu.</li>'
          '<li>Zapomenutí na integrované šortky, a tím vznik nepohodlí při skoku.</li>'
          '<li>Příliš těsný pas, který v pohybu škrtí.</li>'
          '<li>Nevhodný materiál na horké dny, například silná bavlněná směs.</li>'
          '<li>Podcenění délky u dětí. Sukně do kolen může při běhu překážet.</li>'
          '<li>Neověřená velikost, protože se značky liší.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>V seznamu filtrujte podle velikosti, barvy a značky. U každého modelu vidíte nabídky z různých obchodů, takže snadno porovnáte dostupnost velikostí i způsob dopravy. Čtěte popis materiálu a údaje o délce, protože se právě ony liší nejvíc. Velikosti oblíbených barev se vyprodávají rychle, takže pokud máte jasno, nenechávejte objednávku na poslední chvíli. Více oblečení pro stejný účel najdete v hlavní kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi sukní se šortkami a skortem?', 'Sukně se šortkami je klasická sukně, pod níž jsou našité krátké kalhotky. Skort vpředu vypadá jako sukně, ale přední látka je přeložená přes šortky. Obě řešení chrání před nechtěným odhalením.'),
        ('Jakou délku sukně zvolit na tenis?', 'Většinou se nosí krátká nebo střední délka, která nebrání kroku. Důležitější než délka bývá kvalita šortek uvnitř a kapsa na míček.'),
        ('Hodí se sportovní sukně na golf?', 'Ano, na golfu se nosí často ve formě skortu. Hledejte pohodlný pas, volný krok a materiál, který nepřekáží při švihu.'),
        ('Dá se sukně nosit na běhání?', 'Ano, pokud má dobré integrované šortky a pružný pas. Pro delší běh ověřte, zda se nestírají stehna a lem nesjíždí.'),
        ('Mají sportovní sukně kapsy?', 'Mnohé modely mají kapsu v integrovaných šortkách nebo na boku. Na tenis se hodí kapsa na míček, na výlet kapsa na klíče nebo telefon.'),
        ('Z jakého materiálu je nejlepší sportovní sukně?', 'Pro pohyb jsou vhodné polyester, polyamid a elastan, protože rychle schnou a pružně sedí. Bavlněné směsi se hodí spíše pro volný čas.'),
        ('Jak vybrat velikost sukně a šatů?', 'Změřte pas, boky a případně délku trupu a porovnejte hodnoty s tabulkou výrobce. Pokud váháte, zvolte velikost, ve které bezpečně zvládnete dřep a předklon.'),
        ('Jak prát sportovní sukni?', 'Na šetrný program, naruby, s jemným prostředkem a bez aviváže. Suší se na vzduchu, mimo přímé teplo, aby se pružnost i plisování zachovaly.'),
        ('Jsou sukně a šaty vhodné i pro děti?', 'Ano, pro dívky se hodí na sport, tanec i školní aktivity. Vybírejte pevné švy, pružný pas a šortky uvnitř, aby se dítě mohlo volně pohybovat.'),
        ('Čím nahradit sukni, když se mi nelíbí?', 'Alternativou jsou kraťasy nebo legíny, které nabízejí jiný pocit z pohybu. Dobrou volbou jsou i lehké sportovní kalhoty, najdete je v odpovídajících kategoriích.'),
    ])

# ------------------------------------------------------------------ rybarske-navijaky
NEW['rybarske-navijaky'] = dict(long=True,
    title='Rybářské navijáky: přívlač, feeder, kapr, moře | Sporteka',
    desc='Rybářské navijáky: typy, velikost, brzda, převod a cívka. Průvodce výběrem pro přívlač, feeder, kapry i moře a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Rybářský naviják</strong> je mechanický střed celé soupravy. Ukládá vlasec, ovládá brzdu při zdolávání ryby a rozhoduje o tom, jak plynule se bude s náčiním pracovat. Špatně zvolený naviják pokazí i nejlepší prut, naopak vyvážená souprava dělá z dlouhého dne na vodě příjemný zážitek.</p>'
          '<p>Na Sportece porovnáte <strong>navijáky na přívlač, feeder, kapry, muškaření i moře</strong> z českých obchodů a nabídky uvidíte vedle sebe. K navijáku patří vhodný <a href="/rybarske-pruty/">rybářský prut</a>, kvalitní <a href="/vlasce-a-snury/">vlasec nebo šňůra</a> a správné <a href="/nastrahy-a-navnady/">nástrahy a návnady</a>. Pod seznamem najdete průvodce velikostí, převodem, brzdou i péčí, aby nákup seděl ke stylu lovu. Vyplatí se také zamyslet nad tím, kde nejčastěji chytáte, protože rybník, řeka a moře kladou na mechanismus odlišné nároky.</p>',
    guide='<h2>Hlavní typy navijáků</h2>'
          '<p>Při výběru nejdřív rozhodněte, jaký systém potřebujete. Každý typ má jiný způsob odvíjení vlasce a hodí se na jinou techniku rybolovu.</p>'
          + T(['Typ', 'Princip', 'Typické využití'], [
              ['Naviják s pevnou cívkou', 'cívka stojí, vlasec se odvíjí přes okraj, rotor jej navíjí', 'přívlač, feeder, položená, plavaná, univerzální rybolov'],
              ['Multiplikátor', 'otočná cívka na ose, vlasec se odvíjí otáčením cívky', 'těžká přívlač, mořský rybolov, vláčení'],
              ['Naviják s volnoběhem', 'pevná cívka s přepínačem, který uvolní vlasec bez brzdy', 'kapraření a lov dravců na živou rybku'],
              ['Muškařský naviják', 'jednoduchý ruční mechanismus uložený na patce prutu', 'muškaření, viz <a href="/muskareni/">muškaření</a>'],
              ['Naviják s volnou cívkou (centrpin)', 'volně se otáčející cívka bez převodu', 'plavaná na řekách, přesné vedení vlasce']]) +
          '<p>Nejrozšířenější je naviják s pevnou cívkou, protože zvládne širokou škálu technik a odpouští chyby při náhozu. Multiplikátor vyžaduje cvik, ale odměnou je přesnější vedení a větší síla při zdolávání těžkých ryb.</p>'
          '<h2>Velikost navijáku a vyvážení k prutu</h2>'
          '<p>Velikost se označuje číselnou řadou, třeba od malých po velké. Malé číslo patří lehkým navijákům na jemný rybolov, vysoké číslo robustním navijákům na těžké ryby a dlouhé náhozy. Rozhodující je kapacita cívky, tedy kolik vlasce se vejde, a poměr hmotnosti k prutu. Pokud je naviják příliš těžký, souprava se při držení naklání dopředu a unavuje zápěstí, pokud příliš lehký, nezvládne zatížení a špatně se vyvažuje.</p>'
          '<p>Praktická zkouška: nasaďte naviják na prut a držte jej v místě rukojeti. Souprava by měla v ruce ležet téměř vodorovně a nemá se překlápět. Pak zkontrolujte, zda průvlečky na prutu odpovídají průměru vlasce, který chcete použít. Pro výběr správného páru si přečtěte tipy v kategorii <a href="/rybarske-pruty/">rybářské pruty</a>.</p>'
          '<h2>Technika rybolovu a doporučený naviják</h2>'
          '<h3>Přívlač</h3>'
          '<p>Při přívlači se hodí lehčí a rychlý naviják s plynulou brzdou. Pletená šňůra dobře přenáší záběr, ale potřebuje cívku bez ostrých hran. Menší velikosti stačí na okouna, střední na štiku a candáta, větší na těžší nástrahy. Rychlejší převod urychlí navíjení při vedení nástrahy u hladiny, pomalejší dává větší sílu.</p>'
          '<h3>Feeder a položená</h3>'
          '<p>Při feederu se opakují náhozy na stejné místo, takže je důležitá spolehlivá brzda a rovnoměrné ukládání vlasce. Správně naplněná mělká cívka na dlouhé nahazování zlepší přesnost i délku náhozu. Hodí se model střední velikosti s dostatečnou kapacitou, který dobře unese zátěž krmítka.</p>'
          '<h3>Kapraření</h3>'
          '<p>Při kaprařském rybolovu ležící prut hlídá nástrahu hodiny. Naviják s volnoběhem (baitrunner) umožní kaprovi odtáhnout vlasec bez odporu, aniž by prut spadl z podložek. Zvolte velký objem cívky a robustní převody. K dispozici je i řada doplňků a oblečení mezi <a href="/rybarske-doplnky/">rybářskými doplňky</a> a v kategorii <a href="/bivaky-a-kresla/">bivaky a křesla</a>.</p>'
          '<h3>Moře a těžký rybolov</h3>'
          '<p>Slaná voda je agresivní, takže se u mořských navijáků sleduje odolnost proti korozi a těsnění. Používají se často multiplikátory nebo velké navijáky s pevnou cívkou, které unesou zátěž a silnou šňůru. Po rybaření je nutné navijáky důkladně opláchnout sladkou vodou a dobře vysušit.</p>'
          '<h3>Muškaření</h3>'
          '<p>Muškařský naviják je konstrukčně jednodušší. Slouží hlavně k uložení šňůry a k brzdění větších ryb. Kupujte jej společně s prutem a šňůrou, protože musí odpovídat třídě soupravy. Celý výběr je ve skupině <a href="/muskareni/">muškaření</a>.</p>'
          '<h2>Brzda: jak funguje a proč na ní záleží</h2>'
          '<p>Brzda omezuje sílu, kterou ryba může táhnout, a chrání vlasec před přetržením. Čelní brzda je u cívky, takže se nastavuje jednoduše a bývá plynulejší, zadní brzda je za navijákem a hodí se spíš na rychlé úpravy za boje. Kvalitní brzda se rozbíhá hladce, bez cukání, protože právě trhaný záběr způsobí utržení.</p>'
          '<p>Nastavte ji tak, aby ryba při záběru odtáhla vlasec, ale nepřetrhla jej. Obvykle se nastavuje na zlomek pevnosti vlasce. Po každém rybolovu brzdu povolte, aby se podložky nezatuhly a nemusely deformovat. Hodnoty uvedené u navijáku berte jako horní hranici, nikoli jako pracovní nastavení.</p>'
          '<h2>Převodový poměr a rychlost navíjení</h2>'
          '<p>Převod udává, kolikrát se rotor otočí při jednom otočení kličky. Vyšší převod navíjí rychleji a hodí se na rychlé vedení nástrah a na zvedání vlasce při hlubší vodě. Nižší převod dává větší sílu a pomáhá při tažení těžších nástrah nebo odporu proudu. Údaj o délce vlasce navinuté za jednu otáčku je ještě praktičtější než samotný poměr.</p>'
          '<h2>Konstrukce: co vás v obchodě zaujme</h2>'
          '<ul><li><strong>Kuličková ložiska</strong> zvyšují plynulost chodu, ale počet sám nic nezaručuje. Rozhoduje kvalita.</li>'
          '<li><strong>Materiál těla</strong> bývá z kompozitu, hliníku nebo grafitu. Kompozit je lehký a odolný proti korozi, hliník tužší.</li>'
          '<li><strong>Cívka</strong> by měla být vyvážená a mít odolný povrch, který chrání před poškrábáním pletené šňůry.</li>'
          '<li><strong>Navíječ vlasce</strong> zajišťuje rovnoměrné ukládání a snižuje vznik uzlů.</li>'
          '<li><strong>Klička</strong> musí mít pevné uložení a pohodlnou rukojeť. Některé modely umožňují přehození na pravou nebo levou ruku.</li>'
          '<li><strong>Protizpětná pojistka</strong> brání kličce v otáčení zpět, aby se naviják nedostal do vůle.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Na Sportece najdete navijáky značek {B(("daiwa", "Daiwa"), ("mikado", "Mikado"), ("shimano", "Shimano"), ("delphin", "Delphin"), ("penn", "Penn"), ("westin", "Westin"), ("okuma", "Okuma"), ("dam", "DAM"))}. Další nabídka zahrnuje {B(("giants-fishing", "Giants Fishing"), ("tica", "Tica"), ("fox-rage", "Fox rage"), ("ms-range", "MS Range"), ("iron-claw", "Iron Claw"))}. Výběr se liší zaměřením. Některé značky jsou orientované na přívlač a lehký rybolov, jiné na kapraření nebo moře, takže se řiďte typem soupravy, nikoli jménem výrobce.</p>'
          '<h2>Cívka a vlasec</h2>'
          '<p>Cívka musí odpovídat vlasci, jaký chcete použít. Na mělké cívky se hodí tenký vlasec nebo šňůra, na hluboké silnější a delší. Pletená šňůra potřebuje při navinutí lehký tah a podložení, aby neprokluzovala po holé cívce. Vlasec navinutý příliš těsně se stáčí, příliš volně se vzpříčí. Cívka by měla být naplněná téměř po okraj, jinak se nához zkrátí, protože vlasec se odvíjí přes okraj cívky s větším třením. Hodí se mít druhou cívku s jiným vlascem, abyste mohli změnit techniku. Širší výběr materiálů je v kategorii <a href="/vlasce-a-snury/">vlasce a šňůry</a>.</p>'
          '<h2>Péče a údržba navijáku</h2>'
          '<ol><li>Po rybaření naviják opláchněte čistou vodou, zvláště po slané.</li>'
          '<li>Osušte jej měkkým hadrem a nechte uschnout rozložený.</li>'
          '<li>Uvolněte brzdu, aby se podložky nestlačily.</li>'
          '<li>Kapku oleje nanášejte na klíčová místa, jako jsou osa kličky nebo navíječ, přebytek otřete.</li>'
          '<li>Nepoužívejte tlakovou vodu, protože by mohla vnikat do ložisek.</li>'
          '<li>Před sezónou zkontrolujte vůli, plynulost chodu i stav vlasce.</li></ol>'
          '<h2>Pravá nebo levá klička a ergonomie</h2>'
          '<p>Většina navijáků umožňuje přehodit kličku na druhou stranu, takže nemusíte kupovat zvláštní provedení. Praváci obvykle drží prut pravou rukou a navíjejí levou, ale pevného pravidla není. Rozhodněte se podle toho, co vám je přirozené, a případně otestujte oba způsoby. Pozornost věnujte také rukojeti. Měkčí a delší hlavice drží lépe v mokré ruce a při dlouhém zdolávání netlačí do dlaně. Při chladném počasí oceníte kličku, kterou lze uchopit i v rukavici. Zkontrolujte, zda se klička po přehození pevně zajistí a nemá vůli.</p>'
          '<h2>Navijáky pro děti a rodinný rybolov</h2>'
          '<p>Děti potřebují naviják lehký, jednoduchý a odpouštějící chyby. Uzavřená cívka nebo menší model s pevnou cívkou se zvládá snadněji než multiplikátor. Nastavte brzdu spíše volněji a nechte dítě zvyknout si na pocit z ryby. Velmi důležité je vybrat naviják, který se hezky točí a nezadrhává, protože zábava u vody stojí na úspěchu. Dětský prut s kratší délkou dobře kopíruje velikost malé postavy, a proto vybírejte společně v kategorii <a href="/rybarske-pruty/">rybářské pruty</a>. K rodinnému rybaření se hodí i <a href="/rybarske-stany/">rybářské stany</a>, pohodlné křeslo a vhodné oblečení do deště.</p>'
          '<h2>Kdy a jak nakupovat</h2>'
          '<p>Nejvíc zájmu bývá na jaře před začátkem sezóny, kdy se rozprodávají i oblíbené velikosti. Po sezóně se objevují slevy a rozprodeje starších modelů, často beze změny v konstrukci. Pokud nejste na spěchu, porovnejte více obchodů, sledujte popis a čtěte hodnocení. Při koupi dražšího navijáku ověřte, zda jsou k dostání náhradní cívky a díly, protože dostupnost servisu prodlužuje životnost.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš velký naviják na lehký prut, který pak nevyvážíte.</li>'
          '<li>Koupě podle počtu ložisek místo podle kvality chodu.</li>'
          '<li>Podcenění brzdy, a tedy přetrhávání vlasce.</li>'
          '<li>Nevhodná kapacita cívky pro vzdálenost náhozu.</li>'
          '<li>Použití pletené šňůry bez podložení na hladké cívce.</li>'
          '<li>Zapomenutí na péči po rybaření ve slané vodě.</li></ul>'
          '<h2>Pro koho jsou které navijáky</h2>'
          '<p>Začátečníci nejlépe poslouží univerzální naviják s pevnou cívkou střední velikosti, který se dá využít na přívlač, položenou i feeder. Zkušení kaprařští rybáři ocení naviják s volnoběhem a velkou kapacitou, přívlačáři lehký a plynulý model s kvalitní brzdou. Mořští rybáři sáhnou po robustních kusech odolných proti korozi, děti po jednoduchých lehkých navijácích, které se snadno ovládají. Více o doplňcích na vodu najdete v kategoriích <a href="/rybarske-tasky/">rybářské tašky</a> a <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>V seznamu filtrujte podle značky a ceny a u každého navijáku porovnejte nabídky obchodů. Čtěte údaje o velikosti, převodu, kapacitě cívky a hmotnosti. Pokud skládáte soupravu, sjednoťte údaje z prutu, vlasce a navijáku. Nezapomeňte na náhradní cívku. Více o tématu najdete v rozcestníku <a href="/rybareni/">rybaření</a> a v sousední kategorii <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>.</p>',
    faq=[
        ('Jaký naviják koupit pro začátečníka?', 'Nejvhodnější je univerzální naviják s pevnou cívkou střední velikosti. Hodí se na přívlač, položenou i feeder a odpouští chyby při náhozu.'),
        ('Jak poznat správnou velikost navijáku?', 'Zvolte ji podle prutu a vlasce. Naviják by měl prut vyvážit a mít dost místa pro potřebnou délku šňůry. Pomůže doporučení výrobce prutu.'),
        ('K čemu je volnoběh u navijáku?', 'Volnoběh, často nazývaný baitrunner, umožní rybě odtáhnout vlasec bez odporu brzdy. Používá se hlavně při kaprařském rybolovu a lovu na živou rybku.'),
        ('Čím se liší čelní a zadní brzda?', 'Čelní brzda je na cívce a bývá plynulejší a přesnější. Zadní brzda je na těle navijáku a lépe se upravuje při zdolávání, ale bývá méně citlivá.'),
        ('Jaký převod vybrat?', 'Pro rychlé vedení nástrah vyšší převod, pro těžké nástrahy a tah proti proudu nižší. Důležitá je i délka vlasce navinutá za jednu otáčku.'),
        ('Hodí se multiplikátor pro začátečníky?', 'Obvykle ne. Vyžaduje cvik při náhozu, jinak vznikají paruky vlasce. Jeho přednosti ocení až zkušenější rybáři při těžké přívlači nebo na moři.'),
        ('Jak se starat o naviják po rybaření?', 'Opláchněte jej čistou vodou, osušte, povolte brzdu a občas lehce promažte. Po mořském rybolovu je oplach zvlášť důležitý.'),
        ('Dá se použít stejný naviják pro více technik?', 'Částečně ano. Univerzální střední model zvládne přívlač i feeder, ale na kapraření nebo moře je lepší specializovaná konstrukce.'),
        ('Jak navinout šňůru na cívku?', 'Navíjejte ji s mírným rovnoměrným tahem a cívku naplňte téměř po okraj. U pletené šňůry použijte podložku, aby neprokluzovala.'),
        ('Kdy vyměnit vlasec na navijáku?', 'Při poškrábání, ztrátě pevnosti nebo po delším používání. Zkontrolujte jej vždy před sezónou, protože sluneční záření a otěr jej oslabují.'),
    ])

# ------------------------------------------------------------------ sedla-a-gripy
NEW['sedla-a-gripy'] = dict(long=True,
    title='Sedla, gripy a potahy na kolo: jak vybrat | Sporteka',
    desc='Cyklistická sedla, gripy, omotávky a potahy: šířka, tvar, materiál a rozměry pro horská, silniční i městská kola. Průvodce a nabídky obchodů vedle sebe.',
    intro='<p><strong>Sedlo a gripy</strong> jsou dvě místa, kterými se jezdec dotýká kola nejčastěji, a proto rozhodují o pohodlí víc než většina drahých dílů. Špatně zvolené sedlo způsobí dřevěnění, tlak a bolest, nevhodné gripy zase brnění rukou a otlaky. Dobrá zpráva je, že obě součásti jsou levné na výměnu a efekt poznáte obvykle hned po první delší jízdě.</p>'
          '<p>Na Sportece porovnáte <strong>cyklistická sedla, gripy, omotávky řídítek a potahy</strong> z českých obchodů a nabídky uvidíte vedle sebe. Související díly najdete v kategoriích <a href="/cyklo-riditka/">řídítka</a>, <a href="/cyklo-pedaly/">pedály</a> a <a href="/cyklo-brzdy/">brzdy</a>. Pod seznamem je průvodce šířkou sedla, tvarem, uchycením a rozměry gripů, aby se vám nestalo, že díl nepasuje ke kolu.</p>',
    guide='<h2>Jak vybrat cyklistické sedlo</h2>'
          '<p>Sedlo je osobní věc a žádné není dobré pro všechny. Nejdůležitějším parametrem je šířka, která se řídí vzdáleností sedacích kostí, nikoli měkkostí. Příliš úzké sedlo opře váhu o měkké tkáně, příliš široké otírá vnitřní stranu stehen. Mnoho obchodů nabízí měření na speciální podložce a řada výrobců uvádí doporučení podle postoje na kole.</p>'
          '<h3>Sedlo podle posedu a typu kola</h3>'
          + T(['Typ jízdy', 'Posed', 'Sedlo'], [
              ['Silniční a gravel', 'předklon, dlouhé jízdy', 'užší a delší tvar, často s výřezem, viz <a href="/silnicni-kola/">silniční kola</a> a <a href="/gravel-kola/">gravel kola</a>'],
              ['Horská kola', 'proměnlivý posed, sjezdy a stoupání', 'střední šířka, odolný potah, zesílené boky, viz <a href="/horska-kola/">horská kola</a>'],
              ['Treking a město', 'vzpřímený posed', 'širší a měkčí sedlo, často s pružinami, viz <a href="/trekingova-kola/">trekingová kola</a> a <a href="/mestska-kola/">městská kola</a>'],
              ['Elektrokola', 'vzpřímený až sportovní', 'pohodlné sedlo s dobrým rozložením tlaku, více v <a href="/elektrokola/">elektrokolech</a>'],
              ['Děti a dorost', 'malý rozměr, krátké jízdy', 'užší sedlo odpovídající velikosti kola, viz <a href="/detska-kola/">dětská kola</a>']]) +
          '<p>Čím víc se jezdec předklání, tím užší a tužší sedlo zpravidla vyhovuje, protože se váha přesouvá dopředu a na ruce. Čím vzpřímenější posed, tím širší a měkčí podložku potřebujete. Rozhodně neplatí, že nejměkčí sedlo je nejpohodlnější. Příliš měkká pěna se po čase promáčkne a tlak se soustředí do míst, kde to bolí.</p>'
          '<h2>Tvar, výřez a vycpávka</h2>'
          '<p>Výřez nebo prohlubeň uprostřed sedla snižují tlak na střed těla, což pomáhá při delších jízdách. Rovný profil umožňuje měnit polohu dopředu a dozadu, zatímco zakřivený drží jezdce na místě. Měkká pěna nebo gel se hodí na krátké vyjížďky, tužší pěna drží tvar a přináší stabilitu při dlouhé jízdě. Gel se často prodává jako synonymum pohodlí, ale nemusí platit vždy. Pokud vám nevyhovuje, vyzkoušejte sedlo s tenčí pěnovou vrstvou a lepším tvarem.</p>'
          '<h3>Materiál potahu a rámu</h3>'
          '<p>Potah bývá z umělé kůže, mikrovlákna nebo pravé kůže. Umělé materiály se špatně nasákají, snáze se čistí a hodí se do deště. Kůže se přizpůsobí tělu, ale vyžaduje péči. Ližiny, tedy rámeček pod sedlem, jsou z oceli, titanu nebo karbonu. Ocel je levná a odolná, lehčí materiály snižují hmotnost a tlumí vibrace, ale zvyšují cenu. Zkontrolujte i tvar ližin, aby pasovaly do vaší sedlovky.</p>'
          '<h2>Správné nastavení sedla</h2>'
          '<p>I nejlepší sedlo bolí, pokud je špatně nastavené. Výška se upravuje tak, aby se noha v nejnižším bodě otáčení téměř natáhla, ale pánev se na sedle nekývala ze strany na stranu. Vodorovný náklon je výchozí poloha, pak se dá jemně upravovat. Posun dozadu a dopředu ovlivňuje polohu kolene nad pedálem. Po změně nastavte vždy jen jednu věc najednou a ověřte ji během delší jízdy.</p>'
          '<h2>Gripy a omotávky: jak vybrat</h2>'
          '<p>Gripy ovlivňují přenos vibrací, kontrolu kola a komfort rukou. Měkčí gripy tlumí nárazy, tužší dávají přímější pocit. Tloušťka musí odpovídat velikosti dlaně. Jezdci s malou rukou se hodí tenčí gripy, s větší rukou silnější. Hodí se i tvar, například ergonomická opora dlaně, která rozloží tlak a zmírní brnění prstů.</p>'
          '<h3>Typy gripů</h3>'
          '<ul><li><strong>Klasické gripy</strong> se nasouvají na řídítka a drží třením nebo lepidlem.</li>'
          '<li><strong>Lock-on gripy</strong> mají jednu nebo dvě svorky a nepootáčejí se. Na horských kolech se používají nejčastěji.</li>'
          '<li><strong>Ergonomické gripy</strong> mají rozšíření pro dlaň a hodí se pro dlouhé jízdy.</li>'
          '<li><strong>Pěnové gripy</strong> jsou lehké a měkké, hodí se pro závodní využití.</li>'
          '<li><strong>Kožené a korkové omotávky</strong> patří na silniční a gravel řídítka a tlumí vibrace.</li>'
          '<li><strong>Dětské gripy</strong> jsou užší a kratší, aby je malá ruka obepnula.</li></ul>'
          '<h3>Rozměry a kompatibilita</h3>'
          '<p>U horských a městských kol se obvykle používají řídítka s průměrem 22,2 mm, ale délka gripu a způsob uchycení se liší. Řídítka s řadicí nebo brzdovou páčkou potřebují gripy správné délky, aby se tam obě páky vešly. Silniční řídítka mají jiný průměr a obvykle se obalují omotávkou, ne gripy. Před koupí si změřte průměr a volnou délku řídítek, případně ověřte standard v popisu. Více informací najdete v kategorii <a href="/cyklo-riditka/">řídítka</a>.</p>'
          '<h2>Omotávka řídítek na silničním kole</h2>'
          '<p>Omotávka se navíjí od konce řídítek směrem ke středu, přes brzdové páky a zpět. Důležité je rovnoměrné napětí a překrytí, aby výsledek vypadal čistě a držel. Konce se zajišťují lepicí páskou a záslepkou. Pro lepší tlumení lze použít tlustší omotávku nebo ji doplnit gelovou podložkou. Pokud je omotávka mokrá, zvolte rychleschnoucí a protiskluzovou variantu. Při práci se vyplatí trpělivost, a pokud se výsledek nepovede, omotávku můžete odmotat a začít znovu.</p>'
          '<h2>Potahy na sedlo a další doplňky</h2>'
          '<p>Potah chrání sedlo před deštěm a nečistotou. Lehký nepromokavý potah se vejde do kapsy a stačí ho navléct při parkování na ulici. Gelové potahy přidávají vrstvu měkkého materiálu, ale nenahradí sedlo, které k tělu nesedí. Na zimu se hodí potah z neoprenu nebo jiného termoizolačního materiálu. Do výbavy dále patří <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>, kterými sedlo a řídítka upravíte, a <a href="/cyklo-udrzba/">cyklo údržba</a> pro čištění.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii najdete značky {B(("ergon", "Ergon"), ("odi", "ODI"), ("rockbros", "Rockbros"), ("force", "Force"), ("max1", "Max1"), ("lizard-skins", "Lizard Skins"), ("author", "Author"), ("prologo", "Prologo"))}. Dále je zastoupena {B(("reverse", "Reverse"), ("hms", "HMS"), ("velo", "Velo"), ("haven", "Haven"))}. Některé značky se zaměřují na ergonomii a jsou doporučované pro dlouhé jízdy, jiné na lehké závodní sedla nebo na jednoduché městské modely. Před koupí si přečtěte popis, protože právě tam najdete šířku, hmotnost a doporučené využití.</p>'
          '<h2>Sedla pro ženy a muže</h2>'
          '<p>Ženská sedla bývají většinou širší v zadní části a mají výraznější výřez, protože se u žen v průměru liší šířka pánve. Přesto neplatí, že každá žena potřebuje dámské sedlo. Rozhodují sedací kosti a styl jízdy, ne označení. Pokud vám sedí unisex tvar, není důvod měnit. Při zkoušení sedla dopřejte tělu čas, protože první jízdy mohou být nezvyklé a skutečný dojem získáte až po několika desítkách kilometrů. Pokud se tlak objevuje stále na stejném místě, zkuste jinou šířku nebo tvar výřezu.</p>'
          '<h2>Tlumení vibrací a komfort na dlouhých trasách</h2>'
          '<p>Komfort nevytváří jen sedlo. Vibrace z vozovky procházejí také sedlovkou, rámem a řidítky. Pružnější sedlovka nebo širší plášť v nižším tlaku mohou pomoci víc než měkčí pěna. U gripů a omotávek se vyplatí hledat tlumicí vrstvu v dlani, například pěnu, gel nebo korek. Dlouhé jízdy zvládnete lépe, pokud střídáte polohu rukou na řidítkách a uvolníte paže. Pomoc nabídne vhodné oblečení s vložkou, rukavice s polstrováním a pravidelné krátké přestávky, při nichž si protáhnete záda a dlaně.</p>'
          '<h2>Montáž krok za krokem</h2>'
          '<ol><li>Před výměnou si poznamenejte stávající výšku a náklon sedla, například značkou fixou na sedlovce.</li>'
          '<li>Uvolněte svorku sedlovky a vyjměte staré sedlo, uložte si šrouby a podložky.</li>'
          '<li>Nové sedlo uchyťte do svorky se stejným náklonem a ližiny upněte uprostřed jejich rozsahu.</li>'
          '<li>Šrouby utahujte postupně a rovnoměrně, nejlépe momentovým klíčem podle údajů výrobce.</li>'
          '<li>Gripy z řídítek stáhněte, očistěte a nové nasuňte. Lock-on gripy upevněte a svorku pevně dotáhněte, ale nepřetahujte.</li>'
          '<li>Zkuste krátkou jízdu a zkontrolujte, zda se nic neposouvá, a upravte polohu podle pocitu.</li></ol>'
          '<p>Na montáž si připravte základní nářadí, které najdete v kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Pokud si nejste jistí s karbonovými díly, svěřte práci servisu.</p>'
          '<h2>Pro koho se které díly hodí</h2>'
          '<p>Příležitostní jezdci ocení širší sedlo s rozumnou výplní a měkčí gripy. Sportovně orientovaní cyklisté budou hledat užší tvar, odolný potah a lehké gripy s dobrou kontrolou. Cestovatelé s kolem s brašnami by měli upřednostnit trvanlivost a pohodlí na dlouhých etapách. Dojíždějící do práce se hodí potah proti dešti a gripy, které nekloužou v rukavicích. Rodiče malých jezdců zvolí nižší sedlo vhodné k velikosti kola a pevné měkké gripy. Zájemci o příslušenství si prohlédnou i <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a> a <a href="/cyklistika/">cyklistiku</a> jako celek.</p>'
          '<h2>Kdy sedlo nebo gripy vyměnit</h2>'
          '<ul><li>Po nárazu nebo pádu, kdy je sedlo prasklé nebo ližiny ohnuté.</li>'
          '<li>Pokud pěna ztvrdla nebo se promáčkla.</li>'
          '<li>Pokud gripy kloužou, jsou ošoupané nebo se protáčejí.</li>'
          '<li>Při opakovaném brnění rukou nebo bolesti v rozkroku, která nesouvisí s nastavením.</li>'
          '<li>Po změně stylu jízdy, například z města na delší trasy nebo ze silnice na gravel.</li>'
          '</ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Výběr nejměkčího sedla v domnění, že bude pohodlné.</li>'
          '<li>Ignorování šířky sedacích kostí.</li>'
          '<li>Zapomenutí na rozměr ližin a sedlovky.</li>'
          '<li>Gripy příliš tenké nebo příliš silné pro velikost ruky.</li>'
          '<li>Vyřešení bolesti rukou pouze gripy, aniž byste zkontrolovali polohu páček a výšku řídítek.</li>'
          '<li>Utažení šroubů silou. Karbonové ližiny a hliníkové komponenty snadno praskají, proto použijte momentový klíč.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Filtrujte podle značky a typu a u každého dílu porovnejte nabídky obchodů. U sedel sledujte šířku, délku a hmotnost, u gripů průměr, délku a systém uchycení. Pokud chcete vyměnit víc dílů, prohlédněte si širší nabídku v kategorii <a href="/cyklo-dily/">cyklo díly</a> a k outfitu pro jízdu <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a> s vložkou, které s vhodným sedlem tvoří pohodlnou dvojici. Pro lepší kontrolu nad řidítky vyzkoušejte <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>.</p>',
    faq=[
        ('Jak změřit šířku sedlových kostí?', 'Nejjednodušší je sednout si na kus kartonu nebo pěny a změřit vzdálenost otisků. Řada obchodů nabízí i měřicí podložku. Výsledek porovnejte s doporučením výrobce sedla.'),
        ('Je lepší měkké, nebo tvrdé sedlo?', 'Neplatí, že měkčí je pohodlnější. Příliš měkká pěna se promáčkne a tlak se soustředí na citlivá místa. Střední tuhost s dobrým tvarem bývá spolehlivější.'),
        ('Jak vybrat gripy na horské kolo?', 'Zvolte lock-on gripy s průměrem odpovídajícím vaší ruce. Tlumení a tvar volte podle délky jízdy, na delší trasy se hodí ergonomické gripy.'),
        ('Co jsou lock-on gripy?', 'Jde o gripy s upínací svorkou, která je pevně drží na řidítkách. Nepřetáčejí se a nemusí se lepit, takže se snáze montují i vyměňují.'),
        ('Mám gripy nebo omotávku na silniční kolo?', 'Silniční řídítka mají jiný tvar i průměr, proto se na ně obvykle navíjí omotávka. Gripy jsou určené pro rovná řídítka u horských, městských a trekingových kol.'),
        ('Jak poznat, že je sedlo špatné?', 'Typickými příznaky jsou dřevěnění, tlak v rozkroku nebo otlaky na stehnech. Než sedlo vyměníte, ověřte nastavení výšky a náklonu, které bývá častou příčinou.'),
        ('Pasují sedla na všechny sedlovky?', 'Většina sedel používá standardní ližiny, ale tvar a průměr se mohou lišit. U karbonových či zvláštních ližin zkontrolujte kompatibilitu se svorkou sedlovky.'),
        ('Jak vyčistit sedlo a gripy?', 'Stačí vlažná voda s jemným mýdlem a měkký hadr. Neutírejte je ostrými čisticími prostředky, které poškozují povrch a zkracují životnost.'),
        ('Pomůže gelové sedlo při dlouhých jízdách?', 'Ne vždy. Gel přidává měkkost, ale bez správného tvaru a šířky pohodlí nezajistí. Na dlouhé trasy bývá důležitější tvar a nastavení.'),
        ('Jak často vyměňovat gripy?', 'Když se ošoupou, tvrdnou nebo kloužou. U aktivních jezdců je to obvykle po několika sezónách, u příležitostných později. Špatné gripy zhoršují kontrolu kola.'),
    ])
