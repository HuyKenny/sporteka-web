"""sporteka.cz — facet landing texts wave 166: slunecni-bryle-panske, rossignol-lyze, panska-tricka, helly-hansen-bunda.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ slunecni-bryle-panske
NEW['slunecni-bryle-panske'] = dict(
    title='Sluneční brýle pánské: sport i město, čočky a rámy',
    desc='Pánské sluneční brýle: jak vybrat šířku rámu, kategorii čoček, polarizaci i fotochromatiku pro kolo, běh, řízení a město. Srovnání nabídek obchodů.',
    intro='<p>Pánské sluneční brýle se liší od dámských hlavně šířkou rámu, délkou nožiček a tím, jak sedí na kořeni nosu. Širší obličej potřebuje větší rám s delšími straničkami, jinak brýle tlačí za ušima a po hodině začnou bolet. Tato stránka sbírá sluneční a sportovní brýle určené mužům z <a href="/sportovni-bryle/">kategorie sportovních brýlí</a>, tedy modely od lehkých polarizačních na každodenní nošení po větrné rámy pro kolo, běh a rybaření. '
          'Dozvíte se, jak poznat správnou velikost rámu, kdy se vyplatí polarizace, k čemu slouží fotochromatické čočky a proč se do auta nehodí každé tmavé sklo. Součástí je i srovnání rámových materiálů, rady k péči a přehled značek, které v nabídce najdete. Podle ceny a dostupnosti pak snadno porovnáte obchody u konkrétního modelu.</p>',
    guide='<h2>Jak poznat správnou velikost pánského rámu</h2>'
          '<p>Na vnitřní straně nožičky bývá vyražená trojice čísel, třeba šířka skla, šířka můstku a délka stranice, všechna v milimetrech. Nejdůležitější je celková šířka rámu: měla by být zhruba stejná jako šířka vašeho obličeje v úrovni lícních kostí. Pokud brýle přečnívají za spánky, působí příliš velké a sjíždějí z nosu. Pokud tlačí na spánky, jsou naopak úzké a po delším nošení vyvolají tlakovou bolest hlavy.</p>'
          + T(['Údaj na stranici', 'Co znamená', 'Jak ho ověřit'], [
              ['Šířka skla', 'vodorovný rozměr jedné čočky', 'čím větší, tím větší zorné pole i hmotnost'],
              ['Šířka můstku', 'mezera nad nosem', 'musí obepnout kořen nosu, aby brýle neklouzaly'],
              ['Délka stranice', 'od kloubu k zahnutí za ucho', 'konec má ležet za uchem, ne tlačit na lebku'],
              ['Celkový rozměr', 'souhrn šířky rámu', 'porovnejte s brýlemi, které už vám sedí'],
              ['Zakřivení', 'jak rám obepíná obličej', 'víc zakřivený chrání lépe před bočním světlem a větrem']]) +
          '<p>Nejjednodušší trik na nákup bez zkoušení: vezměte brýle, které vám dlouhodobě sedí, přečtěte z nich tři čísla a hledejte model s hodnotami co nejblíž. Rozdíl dvou tří milimetrů nevadí, větší odchylka už se projeví. U sportovních rámů s vyměnitelnými nosníky a nastavitelnými koncovkami se dá sednutí doladit i bez přesné shody.</p>'
          '<h2>Tvar obličeje a styl rámu</h2>'
          '<p>Nic se nemusí řídit přísně, ale několik zásad pomáhá. Kulatější tvář zeštíhlí hranatější rám nebo klasický tvar s lehce zvednutým horním okrajem. Hranatý, výrazný nebo mohutnější obličej naopak změkčí zaoblené sklo či oválné tvary. Úzký obličej se obejde bez těžkého rámu a dobře snáší lehké drátěné obroučky. Sportovní brýle s jednou prodlouženou čočkou, takzvané maskové, sedí většině mužů, protože obličej víc zakrývají a profil ladí.</p>'
          '<ul><li><strong>Wayfarer a podobné lichoběžníkové tvary:</strong> sedí většině tváří a lze je nosit k obleku i k tričku.</li>'
          '<li><strong>Pilotky:</strong> klasika pro delší obličej, kapkovitá skla chrání i zespodu.</li>'
          '<li><strong>Kulaté a oválné rámy:</strong> zmírní hranaté čelisti, hodí se k retro stylu.</li>'
          '<li><strong>Sportovní obalové brýle:</strong> maximální ochrana před vánkem a bočním světlem, nejlepší na kolo a lyže.</li>'
          '<li><strong>Bezrámové a polorámové:</strong> lehké, ale citlivější na pád, vhodné spíš pro město.</li></ul>'
          '<h2>Kategorie čoček: od 0 do 4</h2>'
          '<p>Brýle se na štítku značí kategorií filtru podle toho, kolik světla projde. Číslo neříká nic o UV ochraně, ta je u kvalitních brýlí stejná v každé kategorii a ověřuje se označením UV 400 nebo CE. Kategorie jen určuje, pro jakou jasnost se čočka hodí.</p>'
          + T(['Kategorie', 'Propustnost světla', 'Kam patří'], [
              ['0 a 1', 'vysoká, velmi světlé sklo', 'zataženo, večer, město bez přímého slunce'],
              ['2', 'střední', 'proměnlivé počasí, jaro a podzim'],
              ['3', 'nižší, nejběžnější sluneční filtr', 'léto, silné slunce, běžná jízda autem'],
              ['4', 'velmi nízká, extrémně tmavé', 'vysoké hory a ledovce, do auta se nehodí']]) +
          '<p>Kategorie 4 patří na horské túry po sněhu, kde se světlo odráží ze všech stran. Při řízení vám ale zhorší rozpoznání světelných signálů a výjezdů z tunelu, proto ji do auta nenoste. Kdo má brýle jen jedny na všechno, nechť sáhne po třetí kategorii, která pokryje většinu letních dnů.</p>'
          '<h2>Polarizační brýle: kdy se vyplatí</h2>'
          '<p>Polarizační filtr potlačuje oslnivý odraz od vodorovných ploch, tedy od vody, mokré silnice nebo kapoty auta. Obraz je klidnější, barvy čistší a oči se méně unaví. Proto jsou polarizační brýle oblíbené u řidičů, rybářů, jachtařů a všech, kdo tráví hodně času u vody. Do lyžařského terénu a při pohledu na displeje je potřeba je vyzkoušet: některé displeje, třeba v autě nebo na kole, se mohou pod polarizací zdát tmavší či se na nich objeví duhový vzor.</p>'
          '<p>Jednoduchý test v obchodě i doma: podívejte se přes čočku na displej mobilu a otáčejte brýlemi. Pokud se obraz zatmí nebo zesvětlí, je filtr polarizační. Značky jako <a href="/znacka/polaroid/">Polaroid</a> jsou na polarizaci postavené, <a href="/znacka/relax/">Relax</a> a <a href="/znacka/r2/">R2</a> ji nabízejí u mnoha sportovních modelů.</p>'
          '<h2>Fotochromatické čočky pro proměnlivé světlo</h2>'
          '<p>Fotochromatická čočka mění odstín podle intenzity UV záření. Na slunci ztmavne, ve stínu a za šera se vyjasní. Hodí se tam, kde během jednoho výletu střídáte les, louku a otevřený hřeben, nebo pro cyklisty vyjíždějící za úsvitu. Nevýhodou je, že tmavnutí trvá několik vteřin a v autě, kde čelní sklo blokuje většinu UV záření, se čočka nezabarví. Nabídka sportovních modelů R2 s označením fotochromatické je rozsáhlá, protože značka tento typ používá napříč sérií.</p>'
          '<h2>Materiály rámu: co unese pot, pád a slunce</h2>'
          + T(['Materiál', 'Výhody', 'Na co si dát pozor'], [
              ['Nylon a polyamid', 'lehký, pružný, snáší nárazy', 'při horku se může rozměrově mírně změnit'],
              ['Acetát', 'bohatá barevnost, kvalitní povrch', 'těžší, může klouzat při potu'],
              ['Kov (titan, ocel)', 'tenký, pevný, elegantní', 'u levnějších slitin hrozí alergie na nikl'],
              ['TR-90 a podobné termoplasty', 'velmi lehké a ohebné', 'mohou pod tlakem prasknout místo ohnutí'],
              ['Gumové koncovky', 'drží brýle při pohybu', 'časem ztvrdnou a ztratí tření']]) +
          '<p>Pro sport jsou nejlepší lehké termoplasty s pryžovými koncovkami, pro každodenní nošení většina mužů volí acetát nebo kov. Pokud vás trápí tlak na nose, pomůže měkčí nosní opěrka nebo model s vyměnitelnými podložkami.</p>'
          '<h2>Sluneční brýle podle činnosti</h2>'
          '<p>Na kole potřebujete obalový tvar, který chrání před větrem a hmyzem, a čočky s vyšší propustností světla v lese. Navazující výběr najdete v kategorii <a href="/cyklisticke-bryle/">cyklistické brýle</a>. Při běhu je důležitá nízká hmotnost a to, aby brýle neposkakovaly: pomůže gumová nosní opěrka a zahnuté koncovky stranic. Na lyže patří spíš kategorie <a href="/lyzarske-bryle/">lyžařské brýle</a> nebo její pánská verze <a href="/lyzarske-bryle-panske/">lyžařské brýle pánské</a>. Plavání a vodní sporty ukryté pod čočkou obecně nezvládnou, ty mají vlastní kategorii <a href="/plavecke-bryle/">plavecké brýle</a>.</p>'
          '<p>Pro řízení doporučujeme polarizovanou kategorii 3 s širšími stranicemi, které nezakrývají výhled do zpětného zrcátka. Pro rybáře je dobrá hnědá nebo jantarová čočka, která zvyšuje kontrast na vodě, zatímco šedá zachovává přirozené barvy. Pro městské procházky stačí cokoli v neutrální šedé nebo zelené.</p>'
          '<h2>Značky v nabídce a čím se liší</h2>'
          f'<p>Sportovní zaměření mají {B(("r2", "R2"), ("relax", "Relax"), ("alpina", "Alpina"), ("siroko", "Siroko"), ("rockbros", "Rockbros"))}. Módní a značkové kousky najdete například od {B(("carrera", "Carrera"), ("guess", "Guess"), ("armani-exchange", "Armani Exchange"), ("marc-jacobs", "Marc Jacobs"))}. Sportovní oděvní značky jako {B(("adidas", "Adidas"), ("meatfly", "Meatfly"))} nabízejí brýle v návaznosti na svůj styl. Hlavní rozdíl je v poměru funkce a vzhledu: u sportovních značek rozhoduje sedění v pohybu, u módních tvar a logo na stranici.</p>'
          '<p>Samostatné výběry máte pro <a href="/oakley-slunecni-bryle/">Oakley sluneční brýle</a>, <a href="/slunecni-bryle-r2/">sluneční brýle R2</a>, <a href="/slunecni-bryle-relax/">sluneční brýle Relax</a>, <a href="/slunecni-bryle-adidas/">sluneční brýle Adidas</a> a <a href="/slunecni-bryle-uvex/">sluneční brýle Uvex</a>.</p>'
          '<h2>Péče, aby sklo vydrželo</h2>'
          '<ol><li>Před čištěním opláchněte brýle vodou, aby zrnka prachu neškrábala sklo.</li>'
          '<li>Použijte kapku jemného mycího prostředku a mikrovláknovou utěrku, nikdy ne tričko ani papírový kapesník.</li>'
          '<li>Neodkládejte je čočkami dolů a na horkém palubním panelu je nenechávejte.</li>'
          '<li>Pro přepravu používejte pouzdro, ať už pevné, nebo textilní, které chrání i před otlaky.</li>'
          '<li>Pokud se uvolní šroubek, dotáhněte jej drobným šroubovákem, ale zbytečně netlačte na plast.</li></ol>'
          '<p>Poškrábaná čočka nejde vyleštit a rozptyluje světlo, takže po výraznějším poškrábání je rozumné koupit nové brýle. Stejně tak vyměňte brýle, jejichž povrch se odlupuje.</p>',
    faq=[
        ('Jakou kategorii čoček zvolit na každodenní nošení?', 'Nejuniverzálnější je kategorie 3, která zvládne většinu letních dnů a běžnou jízdu autem. Pokud brýle nosíte i za mírně zatažené oblohy, stačí kategorie 2, ve městě pak někdy i světlejší filtr.'),
        ('Jsou polarizační brýle lepší než obyčejné?', 'Neznamenají vyšší UV ochranu, ale potlačují oslnění od vody, silnice a lesklých ploch. Hodí se řidičům, rybářům a vodákům. Na displeje a při některých sportech je ale potřeba si je vyzkoušet.'),
        ('Mohu v pánských brýlích řídit auto?', 'Ano, pokud mají kategorii 2 nebo 3 a nezkreslují barvy semaforů. Kategorii 4 do auta nepoužívejte. Pozor také na hodně tmavé fotochromatické čočky, které se za čelním sklem nemusí zbarvit.'),
        ('Jak změřit šířku rámu, když brýle kupuji online?', 'Přečtěte si údaje na vnitřní straně stranice brýlí, které vám sedí, a porovnejte je s tabulkou v popisu produktu. Důležitý je celkový rozměr rámu a šířka můstku, ne jen velikost skla.'),
        ('Co znamená označení UV 400?', 'Čočka zachytí záření až do vlnové délky 400 nanometrů, tedy téměř celé UVA, UVB a UVC. Je to základní podmínka kvalitních slunečních brýlí a nezávisí na tmavosti skla.'),
        ('Jsou fotochromatické čočky vhodné na kolo?', 'Ano, pokud jezdíte v proměnlivém světle, třeba střídavě lesem a otevřenou krajinou. Za chladna reagují pomaleji, takže v zimě mohou zůstat světlejší, než čekáte.'),
        ('Z jakého materiálu je lepší sportovní rám?', 'Nejčastěji z lehkých termoplastů, které snesou pád i ohnutí. Pro každodenní nošení se hodí acetát nebo kov, pro náročný pohyb pak pryžové koncovky a nosní opěrka.'),
        ('Proč brýle sjíždějí z nosu?', 'Nejčastěji kvůli příliš širokému můstku, příliš krátkým stranicím nebo ztvrdlým koncovkám. Pomůže nastavitelná opěrka, jiná velikost rámu nebo výměna pryžových částí.'),
        ('Jak dlouho sluneční brýle vydrží?', 'U kvalitních brýlí roky, pokud se nepoškrábou a nezlomí. Rozhoduje péče a skladování, jen na povrchu čočky se časem může opotřebovat vrstva proti odrazům.'),
        ('Mohu brýle nosit s dioptriemi?', 'Některé sportovní rámy mají vyměnitelný optický klip nebo se dají zasklít dioptrickým sklem v optice. Obvyklé je i použití kontaktních čoček s libovolnými slunečními brýlemi.'),
    ])

# ------------------------------------------------------------------ rossignol-lyze
NEW['rossignol-lyze'] = dict(
    title='Rossignol lyže: řady Hero, Forza, Nova, Arcade a React',
    desc='Rossignol sjezdové lyže: jak se liší řady Hero, Forza, Nova, Arcade a React, jak vybrat délku a vázání a komu se hodí. Srovnání nabídek obchodů.',
    intro='<p>Rossignol je francouzská lyžařská značka s dlouhou závodní tradicí a širokou nabídkou pro rekreační lyžaře. V <a href="/sjezdove-lyze/">kategorii sjezdových lyží</a> se u ní setkáte s několika pojmenovanými řadami, z nichž každá míří na jiný styl jízdy: Hero pro ostré carvingové oblouky, Forza pro univerzální pokročilé, Nova pro ženy, Arcade a Soul pro all-mountain a React a Rossi pro svižné začátečnické a pokročilejší modely. '
          'Na této stránce najdete přehled těchto řad, vysvětlení názvů, doporučení délky a vázání a rady, jak vybrat správný model podle úrovně a terénu. Porovnáte i nabídky obchodů u konkrétních kusů, včetně juniorských lyží a kompletů s vázáním Look Xpress a NX.</p>',
    guide='<h2>Rossignol: značka, která zná závodní svahy</h2>'
          '<p>Značka vznikla ve francouzských Alpách a po generace patří k největším výrobcům lyží na světě. Závodní tradice se promítá do konstrukce i do pojmenování: lyže Hero vycházejí z modelů používaných v závodech a jsou stavěné na přesné, energické oblouky. U rekreačních linií jde o zjednodušení těchto principů na lyže odpouštějící chyby. Pokud hledáte základ pro pochopení všech typů lyží, přečtěte si nejdřív průvodce v kategorii sjezdové lyže; tady se věnujeme tomu, co je specifické právě pro Rossignol.</p>'
          '<h2>Řady Rossignolu a pro koho jsou</h2>'
          + T(['Řada', 'Zaměření', 'Hodí se pro'], [
              ['Hero', 'carvingové a závodně laděné lyže', 'pokročilé a sportovní lyžaře na upravené sjezdovce'],
              ['Forza', 'univerzální carving se stabilitou', 'středně pokročilé až dobré rekreační lyžaře'],
              ['React a Rossi', 'lehčí, přístupné carvingové modely', 'začátečníky a lyžaře, kteří se zlepšují'],
              ['Nova', 'dámské lyže, lehčí a obratnější', 'ženy všech úrovní'],
              ['Arcade a Famous', 'všestranné a dámské všestranné modely', 'lyžaře, kteří jezdí i mimo vyjeté stopy'],
              ['Soul', 'širší all-mountain a freeridové', 'zkušenější lyžaře, kteří vyhledávají prašan'],
              ['Hero Jr', 'juniorské verze řady Hero', 'děti a mladé závodníky']]) +
          '<p>Názvy se v nabídce obchodů doplňují o dodatky. Číslo za názvem, třeba Forza 40 nebo Nova 4, obvykle označuje postavení v řadě: nižší číslo znamená přístupnější lyži, vyšší pak sportovnější. Zkratky jako TI, CA nebo CAM zhruba odkazují na konstrukci a materiály, například použití titanu nebo karbonových vrstev, a čím víc takových označení lyže má, tím sportovnější charakter nabízí. V popisu produktu se vždy ověřte přesné parametry, neboť pojmenování se mezi sezónami mění.</p>'
          '<h2>Hero: sportovní carvingová řada</h2>'
          '<p>Modely s názvem Hero patří k nejznámějším lyžím značky. Jsou stavěné pro oblouk po hraně: poměrně úzké pod vázáním, s výrazným bočním vykrojením a tuhým jádrem, které drží stopu i v rychlosti. Hodí se lyžařům, kteří umějí zatáčet po hranách a chtějí zrychlit. Pro začátečníka jsou obvykle příliš nároční, protože tuhá lyže vyžaduje správnou techniku a při chybě nemilosrdně trestá. Verze s označením MT jsou o něco univerzálnější a lépe se chovají i na rozbitém sněhu než čisté závodní modely. Juniorský Hero Jr dává mladým lyžařům stejnou charakteristiku v menší délce.</p>'
          '<h2>Forza, React a Rossi: pro většinu rekreačních lyžařů</h2>'
          '<p>Pokud na horách trávíte pár týdnů ročně a jezdíte hlavně po upravených trasách, jsou nejpraktičtější právě tyto řady. Forza je stabilní a klidná při vyšších rychlostech, React a Rossi se snáze otáčejí a tolerují menší chyby. Rozdíl zjistíte hlavně v ohybu: měkčí lyže se lépe zatáčí v pomalém tempu, tužší vyžaduje tempo a sílu. Pokud váháte, vezměte tu měkčí, protože s ní uděláte větší pokrok než s lyží, která na vás „nespolupracuje“.</p>'
          '<h2>Nova a Famous: lyže pro ženy</h2>'
          '<p>Dámské lyže jsou lehčí a mají měkčí ohyb, protože průměrná žena je lehčí než muž a vyvine menší sílu na hrany. Také bývá posunutá montážní pozice vázání, aby lyže lépe seděla na těžiště. To neznamená, že muž nesmí jezdit na dámských lyžích, pokud je lehčí, ale rozumné je řídit se hmotností a stylem, ne označením. Samostatný výběr najdete v kategorii <a href="/damske-sjezdove-lyze/">dámské sjezdové lyže</a>. Číslo v názvu Nova kopíruje pozici v řadě: Nova 2 a 3 míří na začátečnice a rekreační jezdkyně, Nova 8 pro lyžařky, které chtějí rychlejší a živější lyži.</p>'
          '<h2>Arcade a Soul: když sjezdovka nestačí</h2>'
          '<p>All-mountain lyže jsou širší pod vázáním, takže lépe plavou v čerstvém sněhu a stabilněji projedou rozbitým svahem. Za to platí menší přesností na tvrdém ledu. Arcade je vhodná jako první univerzální lyže, Soul pak pro zkušenější jezdce, kteří vyrážejí i do neupravených svahů. Pokud lyžujete převážně na upravené sjezdovce, je Forza nebo Hero praktičtější, protože šířka pod vázáním při carvingu zbytečně zpomaluje přehození hran.</p>'
          '<h2>Délka lyží podle výšky, váhy a úrovně</h2>'
          '<p>Pro rekreační carvingové lyže platí jednoduché pravidlo: délka se pohybuje mezi bradou a očima lyžaře. Začátečníci jdou ke spodní hranici, pokročilí a těžší lyžaři výš. Freeridové modely se obvykle volí delší, protože v hlubokém sněhu pomáhají s vztlakem. Pokud se pohybujete mezi dvěma délkami, rozhodněte se podle váhy a stylu: těžší nebo rychlejší lyžař vezme delší, lehčí nebo opatrnější kratší.</p>'
          '<ul><li><strong>Začátečník:</strong> kratší lyže, měkký ohyb, lehké ovládání.</li>'
          '<li><strong>Pokročilý rekreační lyžař:</strong> střední délka, střední tuhost, vyvážená stabilita.</li>'
          '<li><strong>Sportovní lyžař:</strong> delší a tužší modely typu Hero.</li>'
          '<li><strong>Dítě:</strong> délka po bradu až ramena, podle zkušenosti.</li></ul>'
          '<h2>Komplety s vázáním Look a Xpress</h2>'
          '<p>Většina Rossignol lyží v nabídce se prodává jako komplet s vázáním značky Look, které patří do téže skupiny. Označení Xpress a NX odpovídá typu a pokročilosti vázání. Verze Xpress jsou jednodušší, vhodné pro rekreační lyžaře a juniory, NX 12 s označením Konect míří na sportovnější lyže. Součástí bývá deska nebo integrovaný systém, na kterém je vázání přichycené. Neznamená to, že nelze vázání později vyměnit, ale u lyží s integrovanou deskou musíte zvolit kompatibilní model. Samostatnou nabídku najdete v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>, hotové sady pak v <a href="/lyze-komplety/">lyžích s vázáním</a>.</p>'
          '<p>Pamatujte, že vázání se musí nastavit podle hmotnosti, výšky a úrovně lyžaře a vždy ho má seřídit servis. Také ověřte, že délka podrážky boty odpovídá rozsahu vázání, jinak vás vázání při pádu nepustí, nebo se naopak otevře předčasně.</p>'
          '<h2>Juniorské Rossignoly</h2>'
          '<p>U dětí je podstatné, aby lyže odpovídala výšce a měkkosti, kterou zvládne ovládat. Junioři ve věku zhruba od školky po první ročníky dostávají kratší lyže, aby se snadno otáčely. S rostoucí zkušeností přecházejí na delší verze se stejnou charakteristikou. Řada Hero Jr s vázáním Xpress 7 a Kid 4 je tak určená dětem, které už jezdí po hranách a trénují. Jako první lyže je přehnaně sportovní, a začátečník by tak byl lépe na mírnějším modelu. Vybrat můžete v kategorii <a href="/detske-lyze/">dětské lyže</a> nebo ve výběru <a href="/detske-sjezdove-lyze/">dětské sjezdové lyže</a>.</p>'
          '<h2>Rossignol ve srovnání s jinými značkami</h2>'
          '<p>Rossignol je mezi největšími světovými lyžařskými značkami a v sortimentu pokrývá téměř všechny styly. Pokud chcete porovnat, podívejte se na výběry <a href="/head-lyze/">Head lyže</a>, <a href="/fischer-lyze/">Fischer lyže</a>, <a href="/salomon-lyze/">Salomon lyže</a> nebo <a href="/sjezdove-lyze-atomic/">Atomic lyže</a>. Rozdíly jsou spíš v pocitu a konstrukci než v tom, že by jedna značka byla lepší: Head je často považována za sportovnější a tužší, Salomon za příjemnou a přívětivou, Rossignol najdete v nabídce od začátečnických po závodní modely. Rozhoduje nakonec to, jak lyže sedí vám osobně, proto se vyplatí využít testovací dny půjčoven.</p>'
          '<h2>Péče a servis</h2>'
          '<p>Před sezónou nechte lyže zkontrolovat v servisu: zbrousit hrany, opravit skluznici a nastavit vázání. Po každém dni na sněhu je osušte a uložte v suchu. Pokud je skladujete přes léto, nechte je namazané voskem, který skluznici chrání před vysycháním. Doplňky najdete v kategorii <a href="/lyzarske-vosky/">lyžařské vosky</a>, nezbytné jsou i <a href="/lyzarske-boty/">lyžařské boty</a>, které musí odpovídat normě vázání.</p>',
    faq=[
        ('Kterou řadu Rossignol zvolit jako začátečník?', 'Nejvhodnější jsou přístupné a měkčí modely, například z řad React nebo Rossi, u žen Nova s nižším číslem. Sportovní Hero je pro začátek zbytečně tuhé.'),
        ('Co znamená číslo v názvu, například Forza 40?', 'Obvykle udává pozici modelu v řadě: nižší číslo je přístupnější, vyšší sportovnější. Přesné parametry ale ověřte v popisu, protože systém se mezi sezónami mění.'),
        ('Jsou lyže Rossignol vhodné pro děti?', 'Ano, značka má juniorské lyže s vázáním Kid nebo Xpress. Pro nejmenší vybírejte kratší a měkčí model, pro trénující děti řadu Hero Jr.'),
        ('Prodávají se Rossignol lyže s vázáním?', 'Většinou ano, jako komplet s vázáním Look Xpress nebo NX. Pokud vázání nechcete, hledejte modely označené jen jako lyže, ale ověřte kompatibilitu s deskou.'),
        ('Jak dlouhé lyže si vybrat?', 'Pro rekreační carving se délka pohybuje mezi bradou a očima. Začátečník zvolí kratší lyže, těžší nebo sportovnější lyžař delší.'),
        ('Mohu na dámských lyžích Nova jezdit jako muž?', 'Mohou je používat i lehčí muži, protože rozhoduje hmotnost a styl. Dámské modely jsou ale měkčí, takže těžší nebo rychlejší lyžař si vybere raději model pánský.'),
        ('Je Rossignol lepší než Head nebo Atomic?', 'Žádná značka není obecně lepší. Rozdíly jsou v charakteru jízdy a tuhosti, proto je důležité vybírat konkrétní model podle úrovně a terénu.'),
        ('Je lyže Arcade vhodná na sjezdovku?', 'Ano, zvládne ji bez potíží. Je ale širší, takže pro čistý carving na upravených tratích bude mít přesnější vyjetí model Forza nebo Hero.'),
        ('Jak často nechat lyže servisovat?', 'Ideálně před každou sezónou, u aktivních lyžařů i během ní. Hrany se brousí podle opotřebení a vázání má vždy nastavit servis.'),
        ('Pasují k lyžím libovolné boty?', 'Boty musí odpovídat normě vázání, délce podrážky a nastavení pro vaši váhu. Servis vázání seřídí podle konkrétní boty.'),
    ])

# ------------------------------------------------------------------ panska-tricka
NEW['panska-tricka'] = dict(
    title='Pánská trička: střih, materiál a velikost pro sport',
    desc='Pánská trička sportovní i volnočasová: střih, materiál, velikostní tabulky a rozdíly mezi funkčním, bavlněným a merino tričkem. Porovnání obchodů.',
    intro='<p>Pánské tričko se liší od dámského rovnějším bočním švem, širšími rameny a delším tělem, takže mu bývá potřeba jiná velikostní tabulka a jiná představa o sednutí. Na této stránce jsou trička z <a href="/sportovni-tricka/">kategorie triček a tílek</a> určená mužům, od základních bavlněných kusů přes funkční modely na běh a kolo po polokošile a tréninková trička klubů. '
          'Průvodce vysvětluje, jak vybrat správnou velikost podle obvodu hrudníku, jaký střih zvolit pro sport a volný čas a proč stejné označení M nemusí u každé značky znamenat totéž. Najdete tu srovnání materiálů, rady pro praní i seznam značek, které v nabídce převažují, včetně sportovních i módních.</p>',
    guide='<h2>V čem se pánské tričko liší od dámského</h2>'
          '<p>Pánský střih počítá s širšími rameny, rovnějším trupem a ramenními švy posazenými dál od krku. Tělo je delší a straně přibývá prostoru v hrudníku, zatímco pas bývá volnější. Dámské tričko se naopak zužuje v pase a rozšiřuje v bocích. Muž, který si vezme dámský kus, tak často narazí na krátké tělo nebo tlak v podpaží, žena v pánském zase na nízký výstřih a přesah ramen. Označení M, L a XL proto neposuzujte jen podle písmene, ale podle konkrétních rozměrů.</p>'
          + T(['Velikost', 'Obvod hrudníku', 'Orientační typ postavy'], [
              ['S', 'zhruba 88–96 cm', 'štíhlejší, menší postava'],
              ['M', 'zhruba 96–104 cm', 'střední štíhlá postava'],
              ['L', 'zhruba 104–112 cm', 'průměrná až širší postava'],
              ['XL', 'zhruba 112–120 cm', 'širší postava, sportovní hrudník'],
              ['XXL', 'zhruba 120–128 cm', 'velká postava']]) +
          '<p>Hodnoty jsou orientační a výrobci se v nich liší. Nejspolehlivější je změřit si obvod hrudníku v nejširším místě a porovnat ho s tabulkou u daného zboží. U funkčních triček počítejte s tím, že přiléhavý střih znamená volbu své velikosti nebo o číslo větší, u volného naopak nechte prostor navíc.</p>'
          '<h2>Střih: slim, regular, oversized</h2>'
          '<ul><li><strong>Slim a přiléhavý:</strong> sedí těsně na těle, ideální pod bundu, na běh a do posilovny, kde nesmí překážet látka.</li>'
          '<li><strong>Regular:</strong> klasický sportovní střih, který se hodí na každý den a na většinu sportů.</li>'
          '<li><strong>Relaxed a oversized:</strong> volnější, delší, popularita v streetwearu a u značek jako Vans nebo 47 Brand.</li>'
          '<li><strong>Delší zadní díl:</strong> chrání záda při předklonu na kole a při práci, u běžeckých triček je běžný.</li></ul>'
          '<h2>Materiál: bavlna, polyester a merino</h2>'
          + T(['Materiál', 'Hodí se na', 'Slabina'], [
              ['Bavlna', 'volný čas, město, chůze', 'při potu nasákne a těžko schne'],
              ['Polyester', 'běh, fitness, kolo, týmové sporty', 'může zadržovat pach, pokud se dlouho nepere'],
              ['Směs bavlny a polyesteru', 'trénink i každodenní nošení', 'kompromis mezi komfortem a schnutím'],
              ['Merino', 'túry a dlouhé výlety', 'jemnější struktura, vyšší nároky na praní'],
              ['Technické úpletové materiály', 'vysoká intenzita', 'u některých povrchů je cítit zvláštní hladkost']]) +
          '<p>Pokud hledáte přesně technické modely, projděte si <a href="/funkcni-tricka/">funkční trička</a>, pro vlněná vlákna <a href="/merino-tricka/">merino trička</a>. Pro horké dny a pláže pak existují <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>, která chrání před slunečním zářením.</p>'
          '<h2>Pánské tričko podle činnosti</h2>'
          '<p>Na běh vybírejte lehké a hladké materiály s plochými švy. Při delších trasách se vyplatí tričko s reflexními prvky a prodyšnými panely na zádech. Na kolo je lepší delší zadní díl a kapsa na zádech u dresů. V posilovně volíte spíš přiléhavý nebo regular střih, aby látka nepřekážela při cvicích na lavici. Na túry je dobré zvolit tričko, které nepachne po druhém dni, tedy merino nebo kvalitní polyester. Pro každodenní život funguje kombinace bavlny a elastanu, která drží tvar i po opakovaném praní.</p>'
          '<p>Pro tým, trénink a fanoušky existují trička s logy klubů a značek jako <a href="/znacka/lotto/">Lotto</a> nebo <a href="/znacka/puma/">Puma</a>. Pokud dáváte přednost lehčímu a vzdušnějšímu oblečení bez rukávů, podívejte se na <a href="/tilka/">tílka a topy</a>. A když hledáte tričko s límečkem, vyberte z kategorie <a href="/polokosile/">polokošile</a> nebo ze samostatného výběru <a href="/panske-polokosile/">pánské polokošile</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Sportovní základ tvoří {B(("nike", "Nike"), ("adidas", "Adidas"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("lotto", "Lotto"), ("dynafit", "Dynafit"))}. Módní a streetwearové kousky nabízejí {B(("47-brand", "47 Brand"), ("vans", "Vans"), ("tommy-hilfiger", "Tommy Hilfiger"), ("gap", "Gap"), ("celio", "Celio"))}. Outdoorové zaměření má {B(("the-north-face", "The North Face"))}. Rozdíl je především v tom, jak je střih navržen: u sportovních značek na pohyb, u módních na vzhled při stání nebo chůzi.</p>'
          '<p>Samostatné přehledy najdete pro <a href="/nike-tricko/">Nike trička</a>, <a href="/under-armour-tricko/">Under Armour trička</a>, <a href="/adidas-tricko/">Adidas trička</a>, <a href="/tricko-puma/">trička Puma</a> a <a href="/tommy-hilfiger-tricko/">Tommy Hilfiger trička</a>. Pokud vás zajímá styl bez sportovního kontextu, vyzkoušejte <a href="/lacoste-tricko/">Lacoste trička</a> nebo <a href="/tricko-vans/">trička Vans</a>.</p>'
          '<h2>Jak kombinovat pánské tričko</h2>'
          '<p>Základní barvy, tedy bílá, černá, šedá a námořnická modrá, se kombinují s čímkoli. Bílé tričko hezky vypadá s džínami i s tmavými kalhotami, ale na túře je nepraktické. Tmavá trička skrývají pot a skvrny, ovšem v létě hřejí. Výrazné potisky se dobře hodí k jednobarevným kalhotám, jemné proužky oživí jednoduché sako nebo košili. Pokud kombinujete s bundou, nechte spodní okraj trička mírně pod ní, ať se tělo nesplývá s bundou.</p>'
          '<h2>Praní a péče</h2>'
          '<ol><li>Trička perte obrácená na rub, aby se nepoškodil potisk.</li>'
          '<li>Funkční materiály perte bez aviváže, která ucpává póry a zhoršuje odvod potu.</li>'
          '<li>Teplotu volte podle štítku, zpravidla třicet až čtyřicet stupňů.</li>'
          '<li>Vlněná trička perte na jemném programu a sušte vleže.</li>'
          '<li>Neperte zbytečně často: merino a kvalitní syntetika snesou vyvětrání mezi nošením.</li></ol>'
          '<p>Bavlněná trička se při prvním praní mohou smrštit, proto kupujte raději o něco volnější. Funkční kusy sušte ve vzduchu, v sušičce ztrácejí pružnost a povrch.</p>'
          '<h2>Kdy tričko koupit a jak poznat kvalitu</h2>'
          '<p>Kvalitní tričko má rovné švy, pevný lem u krku a netrčící nitky. Látka se po natažení vrací do tvaru, potisk je zřetelný a netrhá se. Zkuste tričko přitáhnout proti světlu: příliš průsvitná látka při potu prosvítá a po praní často řídne. Hlídejte také štítek s vlákninovým složením, protože označení jako „sportovní“ nic nezaručuje. Nejvíc trička levněji nabídnou obchody na konci sezóny, kdy se vyprodávají letní kolekce.</p>',
    faq=[
        ('Jak poznám správnou velikost pánského trička?', 'Změřte obvod hrudníku v nejširším místě a porovnejte ho s tabulkou u konkrétního zboží. Údaje značek se liší, takže písmeno samotné nestačí.'),
        ('Je lepší bavlněné, nebo funkční tričko?', 'Na sport je lepší funkční materiál, který odvádí pot a rychle schne. Na každodenní nošení a lehkou chůzi stačí bavlna nebo směs bavlny a polyesteru.'),
        ('Stojí merino tričko za zvážení?', 'Pro túry a vícedenní cesty ano, protože pomalu pachne a zahřeje i vlhké. Pro krátké tréninky stačí kvalitní polyester.'),
        ('Čím se liší slim a regular střih?', 'Slim přiléhá k tělu a nechává méně volné látky, regular je volnější a pohodlnější na každý den. Oversized je ještě delší a širší, hodí se do streetwearu.'),
        ('Zmenšují se bavlněná trička po praní?', 'Mohou se mírně smrštit, zvlášť při vyšší teplotě a v sušičce. Proto raději kupujte volnější velikost a perte při nižší teplotě.'),
        ('Jaké tričko vybrat do posilovny?', 'Lehké, prodyšné a přiléhavé nebo regular střih z polyesteru nebo směsi s elastanem. Měkké švy zabrání odření při pohybu.'),
        ('Mám volit bílé, nebo tmavé tričko?', 'Tmavé trička skrývají pot, ale v létě hřejí víc. Bílé jsou chladnější a univerzální do města, na túru však zbytečně špiní.'),
        ('Jak vyprat funkční tričko?', 'Při třiceti až čtyřiceti stupních bez aviváže, na rubu a bez sušičky. Aviváž uzavírá vlákna a zhoršuje odvod potu.'),
        ('Lze na tričku poznat kvalitu před koupí?', 'Ano, podle švů, rovnosti úpletu, krční lemovky a vláknového složení na štítku. Tkanina nemá být průsvitná a po natažení se vrací do tvaru.'),
        ('Je pánské tričko vhodné i pro ženu?', 'Může být, pokud oceníte volnější střih. Rozdílný bude tvar ramen a délka těla, takže se vyplatí vyzkoušet nebo řídit se rozměry.'),
    ])

# ------------------------------------------------------------------ helly-hansen-bunda
NEW['helly-hansen-bunda'] = dict(
    title='Helly Hansen bunda: Crew, Dubliner, Loke, Seven J a další',
    desc='Bundy Helly Hansen: norská značka z jachtingu. Řady Crew, Dubliner, Seven J, Loke a Paramount, rozdíly mezi softshellem, nepromokavými a zimními bundami.',
    intro='<p>Helly Hansen je norská značka s dlouhou historií v oblečení pro moře a hory, a to se projevuje i na bundách. V kategorii <a href="/sportovni-bundy/">sportovních bund a vest</a> se setkáte s nepromokavými modely do deště, softshellovými Paramount a Crew, zimními a péřovými kousky i lehkými vestami pro dámy i pány. '
          'Tato stránka vysvětluje, jak se řady Crew, Dubliner, Seven J, Loke, Alpha a Paramount liší, kterou zvolit na déšť, na plachetnici, na turistiku nebo do města a jak správně vybrat velikost. Porovnáte také nabídky obchodů u konkrétních modelů, protože stejný kus bývá v různých e-shopech skladem v jiných velikostech a barvách, a snadno tak najdete obchod, který vám ho pošle hned.</p>',
    guide='<h2>Odkud Helly Hansen přichází</h2>'
          '<p>Značku založil norský kapitán v době, kdy se rybáři a námořníci potřebovali chránit před mokrem a větrem. Z oblečení pro moře se časem stalo i horské a městské, ale základ zůstal: nepromokavost, pevné švy, kapuce, která se dá dotáhnout, a barvy viditelné z dálky. To je důvod, proč jsou bundy Helly Hansen běžné v jachtingu a zároveň na horských stezkách. Když hledáte bundu na déšť a vítr, patří tato značka k přirozeným volbám.</p>'
          '<h2>Přehled řad v nabídce</h2>'
          + T(['Řada', 'Typ bundy', 'Hodí se na'], [
              ['Seven J', 'nepromokavá bunda do deště', 'městský déšť, výlety, cestování'],
              ['Dubliner a Dubliner Insulated', 'nepromokavá, zateplená verze', 'chladný déšť, podzim a zima ve městě'],
              ['Loke a Loke 2.0', 'lehká bunda do deště', 'turistika, kolo, lehké balení'],
              ['Crew a Crew 2.0', 'jachtařská bunda, softshell i midlayer', 'vítr a mokro na vodě, aktivní chůze'],
              ['Paramount', 'softshellové bundy a vesty', 'proměnlivé počasí, chůze, běžný provoz'],
              ['Alpha', 'technická lyžařská nebo horská bunda', 'náročnější hory a zima'],
              ['Alby Puffy, Bossanova, Essence Down', 'péřové a zateplené', 'zima, klid, zastávky v chladu'],
              ['Vesty Crew Ins, Jade, Adore Puffy', 'zateplené vesty', 'vrstvení pod bundu nebo samostatně']]) +
          '<p>Názvy se v obchodech opakují s dodatky jako 2.0 nebo Insulated. Verze 2.0 je obvykle vylepšená generace téhož modelu, Insulated znamená zateplení, vhodné do chladu. Přesný popis materiálu a membrány vždy zkontrolujte v popisu produktu, protože se u jednotlivých sezón liší.</p>'
          '<h2>Nepromokavé bundy: Seven J, Loke, Dubliner</h2>'
          '<p>Nepromokavá bunda má utěsněné švy a vodoodpudivý povrch, který nenechá vodu vniknout dovnitř. Seven J je dobře známý model do deště pro město a výlety, Loke zase jednodušší a lehčí, která se vejde do batohu. Dubliner je delší a robustnější a v zateplené verzi poslouží i za nižších teplot. Rozdíl mezi nimi je v hmotnosti, délce a zateplení. Pro delší túry se řídíte hmotností a balitelností, pro dojíždění delší střih, který chrání i zadní část. Další modely v této skupině najdete v kategorii <a href="/nepromokave-bundy/">nepromokavé a outdoorové bundy</a>.</p>'
          '<h2>Softshellové bundy: Paramount a Crew Softshell</h2>'
          '<p>Softshell je pružný materiál, který zastaví vítr a lehký déšť, ale dobře prodýchá. Paramount je oblíbený na turistiku a podzimní procházky, Crew Softshell pak spojuje námořní střih s větší pohyblivostí. Hodí se při aktivní chůzi, kdy nechcete trpět tím, že se pod nepromokavou membránou pocením zapaříte. Při vytrvalém dešti je ale lepší klasická membrána. Výběr si prohlédněte v kategorii <a href="/softshellove-bundy/">softshellové bundy</a>.</p>'
          '<h2>Zimní, péřové a zateplené bundy</h2>'
          '<p>Péřová bunda hřeje velmi dobře při malé hmotnosti, ale při promočení ztrácí izolaci, proto se kombinuje s vodoodpudivým povrchem. Syntetická izolace, často označovaná jako Lifaloft nebo podobně, hřeje i za vlhka a je odolnější. Zimní modely jako Jade Puffer, Bossanova či Alby Puffy vybírejte podle plánu: do města stačí méně zateplená bunda s kapucí, na vysoké hory pak teplejší. Více o tom v kategorii <a href="/zimni-bundy/">zimní a péřové bundy</a>. Pokud potřebujete lyžařskou bundu, dívejte se na <a href="/helly-hansen-lyzarska-bunda/">Helly Hansen lyžařskou bundu</a>.</p>'
          '<h2>Vesty pro vrstvení</h2>'
          '<p>Vesta chrání trup, ale ruce zůstávají volné. Hodí se při chůzi, kdy se zahřejete rychle, ale nechcete přehřívat paže. Zateplené vesty Helly Hansen bývají buď péřové, nebo s lehkou výplní. V kategorii <a href="/sportovni-vesty/">vesty</a> najdete i další výrobce, pro ženy a muže i unisex střihy. Vestu snadno kombinujete pod nepromokavou bundu: sníží se tím riziko podchlazení, když se po zastávce ochladí.</p>'
          '<h2>Vrstvení a výběr podle počasí</h2>'
          '<ol><li>Spodní vrstva z funkčního materiálu odvádí pot.</li>'
          '<li>Střední vrstva, třeba fleece nebo lehká izolace, drží teplo.</li>'
          '<li>Svrchní vrstva, tedy nepromokavá bunda nebo softshell, chrání před větrem a vodou.</li></ol>'
          '<p>Při dešti ve městě stačí Seven J nebo Dubliner přes mikinu. Na horách přibalte Loke nad izolační vrstvu. Při zimě volte zateplenou bundu nebo kombinaci vesty s nepromokavou vrchní vrstvou. Podrobnější průvodce typy bund obsahuje kategorie sportovní bundy, tady se soustředíme na rozdíly mezi modely značky.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Značky norského původu mívají o něco delší rukávy a prostornější střih než francouzské. Pokud máte pochybnosti, změřte obvod hrudníku a porovnejte ho s tabulkou. U zateplených bund s péřovou výplní nechte místo pro mikinu pod nimi. Námořní střih Crew bývá volnější v ramenou, aby šlo zvedat ruce při práci s lany. U dámských modelů označených W se kratší tělo a užší ramena projevují zvlášť u bund s kapucí.</p>'
          '<h2>Helly Hansen ve srovnání s jinými značkami</h2>'
          '<p>Nabídku můžete porovnat s výběry <a href="/the-north-face-bunda/">The North Face bundy</a>, <a href="/columbia-bunda/">Columbia bundy</a>, <a href="/kilpi-bunda/">Kilpi bundy</a>, <a href="/hannah-bunda/">Hannah bundy</a> nebo <a href="/dynafit-bunda/">Dynafit bundy</a>. Helly Hansen vyniká zkušeností s vodou a větrem, zatímco Dynafit se soustředí na horské a skialpové vybavení, The North Face na široký outdoor a Kilpi nebo Hannah na dostupnější turistické bundy. Dobrým doplňkem je mikina té samé značky: <a href="/mikina-helly-hansen/">mikina Helly Hansen</a> nebo <a href="/zimni-bunda-helly-hansen/">zimní bunda Helly Hansen</a>.</p>'
          '<h2>Péče o membránu a izolaci</h2>'
          '<p>Nepromokavé bundy perte podle štítku s vhodným prostředkem na membrány, ne s aviváží, která zalepí póry. Po praní se povrchová vodoodpudivá úprava obnoví krátkým teplým sušením nebo impregnací. Péřové bundy perte jen speciálním prostředkem a sušte s tenisovými míčky, aby se výplň rozptýlila. Skladujte je volně, nezmačkané v pytli, ať péří nepřijde o objem.</p>',
    faq=[
        ('Která bunda Helly Hansen je nejlepší na déšť?', 'Pro město a výlety jsou běžné Seven J a Dubliner, na turistiku lehčí Loke. Rozhodněte se podle hmotnosti, délky a toho, zda potřebujete zateplení.'),
        ('Čím se liší Crew od Paramountu?', 'Crew vychází z jachtařské tradice a má volnější námořní střih, Paramount je klasický softshell na chůzi a běžné nošení. Obě řady se vyrábějí v několika verzích.'),
        ('Je Helly Hansen vhodný na zimu?', 'Ano, nabízí zateplené a péřové modely, například Bossanova, Alby Puffy nebo Dubliner Insulated. Pro opravdový mráz vybírejte bundu s kapucí a delším střihem.'),
        ('Co znamená označení 2.0?', 'Obvykle vylepšenou generaci téhož modelu s úpravami střihu nebo materiálu. Přesné změny najdete v popisu u konkrétního kusu.'),
        ('Pasuje velikost Helly Hansen jako jiné značky?', 'Střih je spíš prostornější a delší. Pokud nejste jistí, změřte obvod hrudníku a porovnejte ho s tabulkou v popisu.'),
        ('Můžu bundu prát v pračce?', 'Ano, podle štítku a speciálním prostředkem pro membrány, bez aviváže. Péřové modely vyžadují samostatné prostředky a jemné sušení.'),
        ('Jsou softshell bundy nepromokavé?', 'Zastaví vítr a lehký déšť, ale při dlouhém dešti prosáknou. Na vytrvalé mokro vezměte nepromokavou membránovou bundu.'),
        ('Mohu nosit nepromokavou bundu i v zimě?', 'Ano, pokud pod ni vrstvíte fleece nebo zateplenou vestu. Zateplené verze jako Dubliner Insulated ušetří jednu vrstvu.'),
        ('Jak bundu uschovat přes léto?', 'Vyčištěnou a suchou, volně pověšenou na ramínku. Péřové a syntetické zateplení neskladujte stlačené, aby neztratilo objem.'),
        ('Lze koupit i dámské bundy a vesty?', 'Ano, značka vyrábí dámské verze s označením W i unisex modely. U vest a kratších bund pozor na délku těla.'),
    ])


NEW['rossignol-lyze']['guide'] += (
    '<h2>Jak číst nabídku obchodů u Rossignolu</h2>'
    '<p>Stejná lyže se v obchodech objevuje pod různými názvy: někde jen jako model, jinde s přidaným vázáním, délkou a barvou. Při porovnání proto sledujte tři věci. Za prvé délku, protože každý rozměr je samostatný kus a skladem nemusí být ten váš. Za druhé typ vázání, který se může u téhož modelu lišit podle sezóny. Za třetí ročník: starší kolekce bývají úplně funkční a v obchodech se objevují v nižších nabídkách, ale grafika i drobné konstrukční detaily se liší.</p>'
    '<ul><li><strong>Model s vázáním a bez něj:</strong> ověřte, jestli je vázání v nabídce zahrnuto, nebo se kupuje zvlášť.</li>'
    '<li><strong>Označení pohlaví:</strong> dámské, pánské a unisex modely se liší tuhostí a montážní polohou vázání.</li>'
    '<li><strong>Délka v centimetrech:</strong> nabídka zpravidla obsahuje několik rozměrů, vyberte podle tabulky výše.</li>'
    '<li><strong>Barva a grafika:</strong> mění se mezi sezónami, lyže se však chovají stejně.</li></ul>'
    '<h2>Kdy se Rossignol vyplatí a kdy zvážit jinou značku</h2>'
    '<p>Pokud hledáte lyži se sportovním charakterem a zároveň chcete mít možnost zůstat u jedné značky od dětských po dospělé modely, je Rossignol praktický. Rodina může mít lyže stejné firmy v různých úrovních a s podobným pocitem z jízdy. Pro čistě freeridové nebo skialpinistické použití je ale lepší sáhnout po specializovaných kategoriích, například <a href="/skialpove-lyze/">skialpové lyže</a>. Pro běh na lyžích zase existuje samostatná kategorie <a href="/bezecke-lyze/">běžecké lyže</a>. A pokud hledáte lyže z dílny jiného výrobce, který se zaměřuje na carving, porovnejte nabídku s <a href="/lyze-sulov/">lyžemi Šulov</a>.</p>')

NEW['panska-tricka']['guide'] += (
    '<h2>Trička pro konkrétní sporty</h2>'
    '<p>Běžecké tričko má obvykle ploché švy a nízkou hmotnost, aby se nic neotíralo při tisících krocích. Cyklistický dres je delší vzadu a často má na zádech kapsy. Fotbalový a tréninkový dres se prodává v klubových barvách, kde rozhodují prodyšné panely a pevný lem u krku. Na turistiku se hodí tričko s krátkým rukávem a UV ochranou, na vícedenní cesty druhé na převlečení, aby se jedno mohlo sušit. V týmových sportech si hlídejte barvy: stejná značka může mít několik odstínů a při kombinaci s kraťasy se rozdíl projeví.</p>'
    '<ul><li><strong>Běh:</strong> lehké a hladké, s reflexním prvkem na večer.</li>'
    '<li><strong>Kolo:</strong> delší záda, zip u krku pro větrání, kapsy v zadní části.</li>'
    '<li><strong>Posilovna:</strong> měkký materiál, který neřeže u podpaží.</li>'
    '<li><strong>Turistika:</strong> merino nebo rychle schnoucí polyester.</li>'
    '<li><strong>Míčové sporty:</strong> odolný materiál a střih, který nebrání pohybu paží.</li></ul>'
    '<h2>Potisky, loga a barvy</h2>'
    '<p>Potisk se na funkčním tričku dělá jako nažehlený nebo tištěný a časem se může zvrásnit, pokud se pere příliš horkou vodou. Vyšívané logo vydrží déle, ale na kůži může dřít. Barvy se na tričku chovají odlišně: světlé a pastelové jsou chladnější, tmavé lépe skrývají pot a špínu, ale prosvítá jimi méně slunce. Pokud tričko nosíte venku, vybírejte výraznější odstíny pro lepší viditelnost, například při běhu v podvečer. Barevné proužky a bloky se hodí pro kluby a retro styl.</p>'
    '<h2>Tričko pod bundu a do posilovny: tři tipy navíc</h2>'
    '<p>Pod bundu volte přiléhavé a tenké tričko, aby se nedělaly záhyby pod rukávy. Při chůzi ve vrstvách vybírejte takové, které odvádí pot od kůže, nikoli bavlnu, jež zůstane vlhká. Do posilovny nepoužívejte příliš volné modely, protože se mohou zachytit o cvičební stroj. A pokud potřebujete tričko na cestování, vezměte merino nebo rychle schnoucí polyester: přes noc se vypere v umyvadle a ráno je suché.</p>')

NEW['helly-hansen-bunda']['guide'] += (
    '<h2>Dámské a pánské modely</h2>'
    '<p>Značka vyrábí bundy v pánských, dámských i unisex verzích. V nabídce poznáte dámské modely podle označení W nebo slova dámská v názvu. Liší se užšími rameny, kratším tělem a někdy i větším prostorem v bocích. Pro muže se střih rozšiřuje v hrudníku. Pokud mezi velikostmi váháte, vezměte větší, aby pod bundu šla obléct i mikina nebo fleece. Zamyslete se také nad délkou rukávů: u aktivního pohybu by se měly při zvednutí paží nezvedat nad zápěstí.</p>'
    '<h2>Co sledovat u kapuce, zipů a kapes</h2>'
    '<p>U nepromokavé bundy rozhoduje kapuce, kterou lze dotáhnout a která nezakrývá výhled při otáčení hlavy. Zipy mají mít chlopeň nebo utěsnění, aby jimi nezatékala voda. Kapsy se hodí s uzavřením, zejména pokud v nich nosíte telefon nebo klíče. Na turistiku uvítáte větrací zipy v podpaží, které odvedou přebytečné teplo. U zimních bund oceníte manžety s úchytem na palec nebo teplý límec, který chrání krk. Jachtařská bunda Crew má navíc výrazná reflexní místa pro viditelnost na vodě.</p>'
    '<ul><li><strong>Kapuce:</strong> dotahovací, s kšiltem, který neomezuje výhled.</li>'
    '<li><strong>Zipy:</strong> krytý hlavní zip, jednodušší ovládání v rukavicích.</li>'
    '<li><strong>Manžety:</strong> na suchý zip nebo pružné, aby foukal méně vzduchu.</li>'
    '<li><strong>Délka:</strong> delší záda chrání při předklonu a sezení.</li></ul>'
    '<h2>Pro koho je bunda Helly Hansen</h2>'
    '<p>Hodí se všem, kdo chtějí spolehlivou ochranu před deštěm a větrem a nevadí jim zjevně sportovní vzhled. Plachtaři ji ocení pro konstrukci, turisté pro rozumnou hmotnost, dojíždějící pro praktickou délku a kapuci. Menší děti na bundu spíš nepotřebují, jejich oblečení se opotřebuje rychleji, než vyrostou. Dětské lyžařské varianty najdete v samostatných výběrech, například <a href="/detska-lyzarska-bunda/">dětská lyžařská bunda</a>. Pokud hledáte větrovku do batohu, vyzkoušejte kategorii <a href="/vetrovky/">větrovky a šusťákové bundy</a>, pro přechodová období pak <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>.</p>')

NEW['panska-tricka']['guide'] += (
    '<p>Při nákupu více kusů se vyplatí držet se jedné značky a střihu, protože tak snáz zachováte stejné sedění. Základní sada na týden může obsahovat dvě bílé nebo světlé kusy do města, dvě tmavá funkční na sport a jedno merino na túry. Takhle se nemusíte při každém ranním výběru rozmýšlet a trička se pravidelně střídají, takže déle vydrží. Starší kusy s vytahaným límcem nebo roztřepeným lemem dejte raději na práci kolem domu.</p>')
NEW['panska-tricka']['faq'] += [
    ('Kolik triček potřebuji na týdenní cestu?', 'Stačí tři až čtyři kusy z rychle schnoucího materiálu, které se dají vyprat v umyvadle. Merino snese vyvětrání několik dní.'),
    ('Jak dlouho tričko vydrží?', 'Záleží na kvalitě a péči. Dobře vyprané a nepřehřívané tričko vydrží roky, levnější syntetika se po delším používání mnohem dříve ošoupe a vytáhne.')]
NEW['helly-hansen-bunda']['guide'] += (
    '<p>Před koupí také porovnejte, kdo bundu posílá a jak dlouho trvá doručení: u sezónního zboží se vyplatí objednat s předstihem, protože oblíbené velikosti a barvy se vyprodají jako první. Při vrácení zboží zkontrolujte, že štítky zůstanou na bundě, a zkoušejte ji doma jen na čistém povrchu, ať ji neznehodnotíte.</p>')
NEW['helly-hansen-bunda']['faq'] += [
    ('Kdy se bundy Helly Hansen nejčastěji vyprodávají?', 'Zimní kousky se vyprodávají na jaře, nepromokavé na konci léta. Oblíbené velikosti mizí nejdřív, proto se vyplatí sledovat více obchodů.'),
    ('Dá se bunda vrátit po vyzkoušení?', 'Většina obchodů dovoluje vrácení do několika dnů, pokud je zboží nepoškozené a se štítky. Podmínky ověřte vždy u konkrétního prodejce.')]
