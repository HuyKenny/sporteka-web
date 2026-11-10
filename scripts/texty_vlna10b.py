"""sporteka.cz — wave 10b (3. 11. 2026): next big categories without a text. General true facts only, no prices.
Brands from the live catalogue; short entries (intro >= 50, guide >= 220 words)."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['cyklo-dily'] = dict(short=True,
    title='Cyklistické díly a pláště – kola, brzdy, pohon | Sporteka',
    desc='Díly na kolo: pláště a duše, brzdy, pohon, řídítka, sedla, pedály a blatníky. Porovnejte ceny z českých obchodů a vyberte díl, který na vaše kolo sedne.',
    intro='<p><strong>Díly na kolo</strong> vybíráte hlavně podle kompatibility. Velikost kola, průměr řídítek, typ brzd, počet převodů nebo uchycení sedlovky určují, co vám na kolo sedne. Špatně zvolený díl znamená vracení a zbytečné starosti, proto je u každého dílu důležité ověřit rozměry.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Přehled podle skupin: <a href="/plaste-a-duse/">pláště a duše</a>, <a href="/cyklo-brzdy/">brzdy</a>, <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklo-riditka/">řídítka a představce</a>, <a href="/sedla-a-gripy/">sedla a gripy</a>, <a href="/cyklo-pedaly/">pedály</a>, <a href="/cyklo-blatniky/">blatníky</a>, <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a> a <a href="/cyklo-kola-a-rafky/">kola a ráfky</a>.</p>',
    guide='<h2>Jak vybrat správný díl na kolo</h2>'
          '<p>Před nákupem si zapište rozměry svého kola a stávajícího dílu. Většina dílů má normy a standardy a ne všechny se dají kombinovat, proto se vyplatí zkontrolovat popis u každého produktu.</p>'
          '<h3>Co zkontrolovat podle dílu</h3>'
          + T(['Díl', 'Na co dát pozor'], [['Plášť a duše', 'průměr kola (např. 26, 27,5, 29) a šířka pláště, typ ventilku'], ['Brzdy a kotouče', 'typ brzdy (kotoučová, ráfková), velikost a uchycení kotouče'], ['Pohon', 'počet rychlostí a kompatibilita kazety, řetězu a přehazovačky'], ['Řídítka a představec', 'průměr upnutí 31,8 mm nebo jiný, délka a výška'], ['Sedlovka a sedlo', 'průměr sedlovky a kolejničky sedla'], ['Pedály', 'závit pedálu a typ: plošinové, nášlapné']]) +
          '<h3>Kvalita a údržba</h3>'
          '<p>Díly, které jsou namáhané, jako pláště, brzdové destičky, řetěz a kazeta, se opotřebují a vyměňují pravidelně. Včas vyměněný řetěz prodlužuje životnost kazety a převodníků.</p>'
          '<h3>Nářadí a montáž</h3>'
          '<p>Základní díly jako pláště, gripy a pedály zvládnete vyměnit sami, brzdy a pohon vyžadují zkušenost. Pokud si nejste jisti, nechte montáž na servisu, špatně seřízené brzdy jsou nebezpečné.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("shimano", "Shimano"), ("kenda", "Kenda"), ("maxxis", "Maxxis"), ("ergon", "Ergon"), ("force", "Force"), ("rockbros", "RockBros"), ("ritchey", "Ritchey"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Nákup dílu bez kontroly rozměrů a norem.</li><li>Výměna řetězu bez kontroly opotřebení kazety.</li><li>Příliš úzký plášť pro terén nebo příliš široký pro rám.</li></ul>',
    faq=[('Jak poznám správný plášť na kolo?', 'Na boku pláště je uveden rozměr, například 29 × 2,2. Vybírejte stejný průměr a šířku podle možností rámu a ráfku.'),
         ('Jaké brzdy mám na kole?', 'Podle toho, zda jsou na kole kotouče, nebo ráfkové čelisti. Liší se i uchycení, takže ověřte typ.'),
         ('Kdy měnit řetěz?', 'Když je prodloužený o více než zhruba 0,5 až 0,75 %, což zjistíte měřidlem opotřebení. Včasná výměna šetří kazetu.'),
         ('Jak vybrat řídítka?', 'Podle průměru upnutí, šířky a tvaru, který odpovídá typu kola a stylu jízdy.'),
         ('Mohu díly měnit sám?', 'Základní díly ano. Brzdy a pohon je lepší svěřit servisu, pokud nemáte zkušenosti.'),
         ('Co jsou plošinové pedály?', 'Široké pedály bez nášlapů, určené pro běžnou obuv, oblíbené v terénu i ve městě.')],
)

NEW['cyklo-prislusenstvi'] = dict(short=True,
    title='Cyklo příslušenství – helmy, brýle, zvonky | Sporteka',
    desc='Příslušenství na kolo: cyklistické brýle, chrániče, zvonky a zrcátka, lahve a držáky, světla a doplňky. Porovnejte ceny z českých obchodů.',
    intro='<p><strong>Cyklistické příslušenství</strong> zlepšuje bezpečnost i komfort jízdy. Základem jsou světla, zvonek a helma, dál se přidávají brýle, lahve, tašky a chrániče. Správný výběr záleží na tom, jestli jezdíte po městě, silnici nebo v terénu.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Rychlé přehledy: <a href="/cyklisticke-bryle/">cyklistické brýle</a>, <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>, <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a>, <a href="/cyklo-chranice/">chrániče</a> a <a href="/cyklo-tasky-a-nosice/">brašny a nosiče</a>. Oblečení najdete v <a href="/cyklisticke-obleceni/">cyklistickém oblečení</a>.</p>',
    guide='<h2>Jak vybrat příslušenství na kolo</h2>'
          '<p>Nejdřív bezpečnost, potom pohodlí. Světla vpředu a vzadu a reflexní prvky patří na kolo při jakékoli jízdě za šera. Helma je u dětí a v terénu nezbytností a doporučuje se všem.</p>'
          '<h3>Co k čemu</h3>'
          + T(['Příslušenství', 'K čemu je'], [['Světla', 'viditelnost za šera, nejlépe přední a zadní'], ['Zvonek', 'upozornění chodců a ostatních cyklistů'], ['Helma', 'ochrana hlavy při pádu'], ['Brýle', 'ochrana očí před prachem, hmyzem a sluncem'], ['Chrániče', 'ochrana kolen, loktů a zad v terénu'], ['Láhev a držák', 'pití při jízdě'], ['Brašny a nosiče', 'přeprava věcí bez batohu']]) +
          '<h3>Brýle na kolo</h3>'
          '<p>Cyklistické brýle chrání před prachem a hmyzem a existují s výměnnými nebo fotochromatickými zorníky. Dbejte na UV ochranu a pevné držení na hlavě.</p>'
          '<h3>Chrániče a helmy</h3>'
          '<p>Při downhillu a enduru se používají pevné helmy a chrániče, které přenášejí náraz. Dětské modely mají nastavitelný pásek a vybírají se podle obvodu hlavy.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("shimano", "Shimano"), ("force", "Force"), ("specialized", "Specialized"), ("author", "Author"), ("ritchey", "Ritchey"), ("max1", "Max1"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Jízda za šera bez světel.</li><li>Helma, která je příliš volná nebo nasazená na zátylku.</li><li>Pití z lahve na kole bez držáku, který ji pevně drží.</li></ul>',
    faq=[('Co potřebuji na kolo povinně?', 'Světla vpředu a vzadu při jízdě za šera, odrazky a zvonek. Pro děti do 18 let platí povinnost helmy.'),
         ('Jak vybrat cyklistickou helmu?', 'Podle obvodu hlavy, typu jízdy a ventilace. Helma musí sedět pevně a nesmí se hýbat.'),
         ('Hodí se cyklistické brýle i do města?', 'Ano, chrání před prachem a hmyzem a snižují únavu očí ve slunci.'),
         ('Jak vybrat držák na láhev?', 'Podle uchycení na rámu a velikosti lahve. Držák má láhev pevně držet i na nerovné cestě.'),
         ('K čemu jsou chrániče?', 'Chrání kolena, lokty a záda při pádu v terénu, hlavně u enduro a downhill jízdy.')],
)

NEW['kolobezky-a-brusle'] = dict(short=True,
    title='Koloběžky, brusle a skateboardy | Sporteka',
    desc='Koloběžky, kolečkové brusle, inline brusle a skateboardy včetně chráničů a helem. Porovnejte ceny z českých obchodů a vyberte velikost pro děti i dospělé.',
    intro='<p><strong>Koloběžky, brusle a skateboardy</strong> jsou nejpopulárnější sporty pro děti i dospělé, které zvládnete začít bez dlouhé přípravy. Každý sport vyžaduje jiné dovednosti: koloběžka je nejjednodušší a stabilní, brusle potřebují cvik a skateboard rovnováhu. U všeho platí, že helma a chrániče jsou základ.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů: <a href="/kolobezky/">koloběžky</a>, <a href="/inline-brusle/">inline brusle</a>, <a href="/skateboardy/">skateboardy a longboardy</a> a <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>',
    guide='<h2>Jak vybrat koloběžku, brusle nebo skateboard</h2>'
          '<p>Rozhodněte, co chcete dělat a kdo bude jezdit. Pro nejmenší je nejbezpečnější třikolka nebo malá koloběžka, pro teenagery a dospělé se hodí městská, freestylová nebo elektrická koloběžka.</p>'
          '<h3>Co vybrat podle věku a cíle</h3>'
          + T(['Aktivita', 'Co hledat'], [['Malé děti', 'lehká koloběžka se širokým stupínkem, nastavitelné řídítko'], ['Městská jízda', 'větší kola, odpružení, skládací konstrukce'], ['Triky a park', 'pevná konstrukce, malá kola, odolné řídítko'], ['Rekreační bruslení', 'inline brusle s ložisky ABEC a pohodlnou botou'], ['Skateboard', 'deska podle stylu: street, cruiser nebo longboard']]) +
          '<h3>Velikost bruslí a dětské brusle</h3>'
          '<p>Dětské brusle mají nastavitelnou velikost a rostou s nohou. Dospělé brusle mají pevnou velikost, vybírejte podle chodidla a při zkoušení si vezměte ponožky, ve kterých budete bruslit.</p>'
          '<h3>Bezpečnost</h3>'
          '<p>Helma, chrániče zápěstí, loktů a kolen patří k základní výbavě. Hlavně začátečníci a děti se bez nich nevyhnou odřeninám. Chrániče musí sedět pevně, aby se nesesouvaly.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("micro", "Micro"), ("powerslide", "Powerslide"), ("tempish", "Tempish"), ("raven", "Raven"), ("nils", "Nils"), ("core", "Core"), ("bauer", "Bauer"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Jízda bez helmy a chráničů.</li><li>Příliš velká koloběžka nebo brusle pro dítě na vyrůstání.</li><li>Zanedbaná ložiska a kolečka, která zhoršují jízdu.</li></ul>',
    faq=[('Jaká koloběžka pro dítě?', 'Lehká se širokým stupínkem a nastavitelným řídítkem, ve velikosti podle výšky dítěte.'),
         ('Jak vybrat inline brusle?', 'Podle velikosti chodidla, ložisek a typu bruslení. Rekreační brusle mají měkčí botu s dobrou podporou kotníku.'),
         ('Co je longboard?', 'Delší skateboard určený na svezení a cestování, pohodlnější než krátká deska.'),
         ('Jaké chrániče kupovat?', 'Na zápěstí, lokty a kolena a pevnou helmu. Musí sedět pevně a odpovídat velikosti.'),
         ('Jak často kontrolovat kolečka?', 'Před sezónou a pravidelně během ní, opotřebená kolečka měňte a ložiska čistěte.')],
)

NEW['nastrahy-a-navnady'] = dict(short=True,
    title='Rybářské nástrahy a návnady – wobblery, boilies',
    desc='Rybářské nástrahy a návnady: gumové nástrahy, wobblery, třpytky, boilies a návnady na kapra. Porovnejte ceny z českých obchodů a vyberte podle ryby.',
    intro='<p><strong>Rybářské nástrahy a návnady</strong> určují, jakou rybu chytíte. Dravce lákají umělé nástrahy a kapry a cejny návnady a boilies. Nástrahy imitují kořist a hrají si s pohybem, barvou a rychlostí vedení, návnady lákají vůní a chutí.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K nástrahám patří <a href="/rybarske-pruty/">pruty</a>, <a href="/rybarske-navijaky/">navijáky</a> a <a href="/vlasce-a-snury/">vlasce</a>, uložit je pomohou <a href="/rybarske-tasky/">tašky a krabičky</a>. Přehled najdete také v <a href="/rybareni/">rybaření</a>.</p>',
    guide='<h2>Jak vybrat nástrahy a návnady</h2>'
          '<p>Vybírejte podle druhu ryby, způsobu lovu a vody. Čirá voda a slunečný den vyžadují přirozené barvy, kalná voda a šero zase výrazné odstíny.</p>'
          '<h3>Nástrahy na dravce</h3>'
          '<ul><li><strong>Gumové nástrahy (shady, twistry):</strong> na štiku, candáta a okouna, vedou se na jigové hlavičce.</li>'
          '<li><strong>Wobblery:</strong> tvrdé plovoucí a potápivé nástrahy imitující rybku.</li>'
          '<li><strong>Třpytky a rotačky:</strong> kovové, které se otáčejí nebo kmitají, vhodné pro pstruhy a okouny.</li>'
          '<li><strong>Jigy a hlavičky:</strong> olověné hlavičky pro gumové nástrahy.</li></ul>'
          '<h3>Návnady na kapra a bílou rybu</h3>'
          '<ul><li><strong>Boilies:</strong> kuličky z těsta, základ kaprařiny.</li>'
          '<li><strong>Pelety a partikly:</strong> menší návnady pro krmení a method feeder.</li>'
          '<li><strong>Boostery a esence:</strong> zvýrazňují vůni a chuť.</li>'
          '<li><strong>Obalovací pasty:</strong> používají se na krmení i obalování.</li></ul>'
          '<h3>Barva a velikost</h3>'
          '<p>Velikost nástrahy by měla odpovídat kořisti v dané vodě. Vyplatí se mít v krabičce více odstínů a velikostí a podle podmínek měnit.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("rapala", "Rapala"), ("westin", "Westin"), ("savage-gear", "Savage Gear"), ("illex", "Illex"), ("mikado", "Mikado"), ("jet-fish", "Jet Fish"), ("mikbaits", "Mikbaits"), ("nikl", "Nikl"), ("caperlan", "Caperlan"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velká nástraha na malé ryby.</li><li>Špatná rychlost vedení, která nástrahu zbavuje života.</li><li>Zanedbaná ostrost háčků, které po pár záběrech tupí.</li></ul>',
    faq=[('Jaké nástrahy na štiku?', 'Gumové ryby na jigové hlavičce, větší wobblery a třpytky. Velikost volte podle vody a sezóny.'),
         ('Co jsou boilies?', 'Kuličky z těsta, hlavní návnada na kapra. Mají různé chutě a velikosti.'),
         ('Jak vybrat barvu nástrahy?', 'Ve čisté vodě přirozené odstíny, v kalné nebo za šera výrazné. Mějte v krabičce víc variant.'),
         ('Co je jigová hlavička?', 'Olověná hlavička s háčkem, na kterou se nasazuje gumová nástraha.'),
         ('Co jsou boostery?', 'Tekuté přípravky, které zvyšují vůni a chuť boilies a návnad.')],
)

NEW['merino-tricka'] = dict(short=True,
    title='Merino trička a tílka – pánská, dámská, dětská | Sporteka',
    desc='Merino trička a tílka pánská, dámská a dětská: lehká na léto, střední na celý rok i s dlouhým rukávem. Porovnejte ceny z českých obchodů a vyberte gramáž.',
    intro='<p><strong>Merino triko</strong> je oblíbená první vrstva pro sport i cestování. Hřeje v chladu, v teple chladí a po dnech nošení nezapáchá. Proto ho vyhledávají běžci, turisté i ti, kdo chtějí lehké triko do batohu.</p>'
          '<p>Na Sportece porovnáte <strong>merino trička</strong> z českých obchodů, můžete filtrovat podle velikosti, barvy a značky. Další merino oblečení najdete v kategorii <a href="/merino/">merino oblečení</a>, spodní prádlo v <a href="/merino-pradlo/">merino prádle</a> a doplňky v <a href="/merino-doplnky/">merino doplňcích</a>.</p>',
    guide='<h2>Jak vybrat merino triko</h2>'
          '<p>Rozhodněte, k čemu ho budete používat. Pro léto a běh se hodí lehká gramáž, pro celoroční turistiku střední, pro zimu a hory těžší. Rukáv a střih určují, jak se triko hodí pod další vrstvy.</p>'
          '<h3>Gramáž a sezóna</h3>'
          + T(['Gramáž', 'Použití'], [['do 150 g/m²', 'léto, běh a lehká turistika'], ['150–200 g/m²', 'celoroční triko na túry a každodenní nošení'], ['nad 200 g/m²', 'zimní první vrstva a hory']]) +
          '<h3>Střih a délka rukávu</h3>'
          '<p>Přiléhavý střih funguje nejlépe jako první vrstva, protože merino musí být blízko pokožce. Krátký rukáv se hodí v teple, dlouhý chrání před sluncem a chladem. Tílka využijete na horké dny a pod lehké oblečení.</p>'
          '<h3>Směsi a odolnost</h3>'
          '<p>Čisté merino je jemné, ale méně odolné. Směsi s polyesterem nebo nylonem jsou pevnější a rychleji schnou. Vybírejte podle toho, jak často a jak intenzivně triko nosíte.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("icebreaker", "Icebreaker"), ("sensor", "Sensor"), ("lasting", "Lasting"), ("smartwool", "Smartwool"), ("helly-hansen", "Helly Hansen"), ("devold", "Devold"), ("progress", "Progress"), ("viking", "Viking"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Perte šetrně a na nízké teplotě, bez aviváže a sušte volně. Větrání mezi nošením prodlužuje čas do praní.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš volný střih, který se nedotýká pokožky.</li><li>Praní na vysokou teplotu, po kterém merino zhrbí.</li><li>Těžká gramáž na intenzivní běh v teple.</li></ul>',
    faq=[('Jaké merino triko vybrat na túru?', 'Střední gramáž kolem 150–200 g/m², přiléhavé, s krátkým nebo dlouhým rukávem podle počasí.'),
         ('Zapáchá merino triko?', 'Méně než syntetika. Vlna zadržuje pach méně a triko jde nosit několik dní.'),
         ('Jak prát merino triko?', 'Šetrně na nízkou teplotu bez aviváže a sušit volně.'),
         ('Hodí se merino i na běh?', 'Ano, lehká gramáž funguje v teple i v chladu, ale pomaleji schne než syntetika.'),
         ('Čisté merino, nebo směs?', 'Čisté je jemnější, směs je odolnější a rychleji schne. Záleží na použití.')],
)

NEW['zimni-bundy'] = dict(short=True,
    title='Zimní a péřové bundy – pánské, dámské, dětské | Sporteka',
    desc='Zimní, péřové a zateplené bundy pánské, dámské a dětské: městské i outdoorové. Porovnejte ceny z českých obchodů a vyberte bundu podle teploty.',
    intro='<p><strong>Zimní bunda</strong> musí především hřát, ale zároveň odolávat větru a vlhku a nepřehřívat při pohybu. Rozhoduje výplň, tedy peří nebo syntetika, střih a použití: městská bunda se liší od outdoorové.</p>'
          '<p>Na Sportece najdete <strong>zimní bundy pánské, dámské i dětské</strong> z českých obchodů, porovnáte ceny a vyberete podle velikosti, barvy a značky. Pro lyžování hledejte <a href="/lyzarske-bundy/">lyžařské bundy</a>, pro přechodové období <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> a pro deštivé dny <a href="/nepromokave-bundy/">nepromokavé bundy</a>.</p>',
    guide='<h2>Jak vybrat zimní bundu</h2>'
          '<p>Vybírejte podle teploty, ve které ji budete nosit, a podle aktivity. Čím víc se hýbete, tím lehčí zateplení stačí, při stání v mrazu potřebujete silnou izolaci.</p>'
          '<h3>Výplň bundy</h3>'
          '<ul><li><strong>Péřová:</strong> nejlehčí a nejteplejší vzhledem k váze, ale citlivá na vlhko.</li>'
          '<li><strong>Syntetická (PrimaLoft apod.):</strong> hřeje i vlhká a rychle schne, je těžší.</li>'
          '<li><strong>Prošívaná:</strong> městský vzhled, zpravidla lehčí zateplení.</li>'
          '<li><strong>Hybridní:</strong> kombinace izolace a pružných vložek pro pohyb.</li></ul>'
          '<h3>Střih a délka</h3>'
          '<p>Delší bunda zakryje stehna a drží teplo při stání, kratší se hodí k pohybu. Kapuce, manžety a stahování v pase zvyšují těsnost.</p>'
          '<h3>Vodoodpudivost</h3>'
          '<p>Většina zimních bund má vodoodpudivou úpravu, která zvládne sníh a lehký déšť. Na vytrvalý déšť potřebujete membránu. Péřové bundy bez ochrany pohlcují vlhkost.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("regatta", "Regatta"), ("trespass", "Trespass"), ("columbia", "Columbia"), ("the-north-face", "The North Face"), ("dare2b", "Dare2b"), ("fjallraven", "Fjällräven"), ("adidas", "Adidas"), ("champion", "Champion"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Péřovou bundu perte s přípravkem na péří a sušte s tenisovými míčky, aby se peří nezlepilo. Syntetickou perte podle štítku.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těsná bunda, která nepustí vrstvu pod ní.</li><li>Péřová bunda do vlhka bez ochrany.</li><li>Kupování podle vzhledu bez ohledu na teplotu.</li></ul>',
    faq=[('Jaká zimní bunda je nejteplejší?', 'Péřová s vyšší gramáží výplně a kapucí. Pro vlhko je lepší syntetická.'),
         ('Péřová, nebo syntetická bunda?', 'Péřová je lehčí a hřeje víc vzhledem k váze, syntetická lépe snáší vlhko.'),
         ('Jak vybrat velikost?', 'Podle tabulky výrobce a s rezervou na svetr nebo fleece pod bundou.'),
         ('Jak prát péřovou bundu?', 'S přípravkem na péří, šetrně a sušit s míčky, aby se peří nezlepilo.'),
         ('Hodí se zimní bunda na lyže?', 'Na lyže je lepší lyžařská bunda s membránou a sněhovou manžetou, městská péřovka stačí na procházky.')],
)

NEW['cyklisticke-obleceni'] = dict(short=True,
    title='Cyklistické oblečení – dresy, kraťasy, bundy | Sporteka',
    desc='Cyklistické oblečení: dresy, kraťasy a kalhoty, rukavice, bundy, ponožky a návleky. Porovnejte ceny z českých obchodů a vyberte velikost a vrstvy.',
    intro='<p><strong>Cyklistické oblečení</strong> je navržené tak, aby se na kole dobře sedělo, odvádělo pot a chránilo před větrem a deštěm. Dres má kapsy na zádech a delší záda, kalhoty se šámem zvyšují komfort a rukavice tlumí otřesy a chrání při pádu.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů a vybíráte podle velikosti, barvy a značky: <a href="/cyklisticke-dresy/">dresy</a>, <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy a kalhoty</a>, <a href="/cyklisticke-rukavice/">rukavice</a>, <a href="/cyklisticke-bundy-a-vesty/">bundy a vesty</a>, <a href="/cyklisticke-ponozky/">ponožky</a> a <a href="/cyklisticke-navleky/">návleky</a>.</p>',
    guide='<h2>Jak vybrat cyklistické oblečení</h2>'
          '<p>Základem je vrstvení a materiál. Syntetika odvádí pot, merino hřeje a nezapáchá. Správně sedící oblečení je přiléhavé, ale nebrání v pohybu a nemá švy tam, kde se dotýká sedla.</p>'
          '<h3>Co obléct podle počasí</h3>'
          + T(['Počasí', 'Doporučené oblečení'], [['teplo nad 20 °C', 'lehký dres, kraťasy, rukavice, ponožky'], ['jaro a podzim', 'dres s dlouhým rukávem, návleky, tenká větrovka'], ['chladno do 10 °C', 'termo dres, dlouhé kalhoty, rukavice, návleky na boty'], ['déšť', 'nepromokavá bunda, blatníky, návleky']]) +
          '<h3>Šám a kalhoty</h3>'
          '<p>Šám je vložka v kalhotách, která tlumí tlak v sedle. Kalhoty se šámem se nosí bez spodního prádla. Pro dlouhé výlety vybírejte kvalitnější šám a dobře padnoucí velikost.</p>'
          '<h3>Rukavice a ponožky</h3>'
          '<p>Rukavice chrání dlaně a tlumí otřesy. Ponožky mají být vyšší, vzdušné a bez švů, aby netlačily.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("silvini", "Silvini"), ("rockbros", "RockBros"), ("haven", "Haven"), ("kilpi", "Kilpi"), ("etape", "Etape"), ("siroko", "Siroko"), ("r2", "R2"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Volné oblečení, které vlaje a zpomaluje.</li><li>Šámové kalhoty nošené se spodním prádlem.</li><li>Bavlněné tričko na delší výlet, které nasákne potem.</li></ul>',
    faq=[('Co si obléct na kolo?', 'Dres a kalhoty ze syntetiky nebo merina, v chladu s vrstvou navíc a v dešti s nepromokavou bundou.'),
         ('K čemu je šám?', 'Vložka v kalhotách, která tlumí tlak a snižuje tření v sedle.'),
         ('Nosí se pod šámové kalhoty prádlo?', 'Ne, šám je určen pro nošení přímo na pokožce.'),
         ('Jak vybrat cyklistický dres?', 'Podle velikosti, materiálu a kapes na zádech. Přiléhavý střih omezuje vlání.'),
         ('Hodí se bavlna na kolo?', 'Na krátké jízdy ano, na delší trasy je lepší syntetika nebo merino.')],
)

NEW['sportovni-bryle'] = dict(short=True,
    title='Sportovní a sluneční brýle – polarizační | Sporteka',
    desc='Sportovní a sluneční brýle pánské, dámské a dětské: polarizační, fotochromatické, na kolo, běh a turistiku. Porovnejte ceny z českých obchodů.',
    intro='<p><strong>Sportovní sluneční brýle</strong> chrání oči před sluncem, větrem, prachem i hmyzem. Rozhoduje kategorie filtru, tvar rámu a materiál čoček. Při běhu a jízdě na kole musí brýle pevně držet a nezamlžovat, při turistice a ve vysokých horách potřebují silný filtr a ochranu po stranách.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Pro zimní sporty hledejte <a href="/lyzarske-bryle/">lyžařské brýle</a>, pro kolo <a href="/cyklisticke-bryle/">cyklistické brýle</a> a pro vodu <a href="/plavecke-bryle/">plavecké brýle</a>.</p>',
    guide='<h2>Jak vybrat sportovní brýle</h2>'
          '<p>Vybírejte podle sportu a světelných podmínek. Pro slunečný den potřebujete tmavší filtr, pro proměnlivé počasí fotochromatické čočky, které se přizpůsobí světlu.</p>'
          '<h3>Kategorie filtru</h3>'
          + T(['Kategorie', 'Použití'], [['0–1', 'šero, zataženo, večer'], ['2', 'proměnlivé počasí'], ['3', 'slunečný den, běžné použití'], ['4', 'vysoké hory, ledovec, extrémní slunce']]) +
          '<h3>Čočky</h3>'
          '<ul><li><strong>Polarizační:</strong> omezují odlesky od vody a silnice.</li>'
          '<li><strong>Fotochromatické:</strong> mění propustnost podle světla.</li>'
          '<li><strong>Zrcadlové:</strong> odráží část světla a lépe snášejí ostré slunce.</li></ul>'
          '<h3>Rám a střih</h3>'
          '<p>Brýle mají pevně sedět na nose a spáncích a při pohybu nesklouzávat. Sportovní rámy bývají z odolného lehkého plastu s pogumovanými částmi. Dětské brýle mají menší střih a UV ochranu 400.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("oakley", "Oakley"), ("alpina", "Alpina"), ("uvex", "Uvex"), ("relax", "Relax"), ("rockbros", "RockBros"), ("r2", "R2"), ("laceto", "Laceto"), ("o-neill", "O\'Neill"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Brýle bez UV ochrany, které rozšíří zornici a škodí oku.</li><li>Příliš tmavé čočky při jízdě tunelem nebo lesem.</li><li>Rám, který tlačí na spánky a při delším nošení bolí.</li></ul>',
    faq=[('Jaké brýle vybrat na běhání?', 'Lehké, pevně držící a odvětrané, s UV ochranou a tmavším filtrem pro slunečný den.'),
         ('Co jsou polarizační čočky?', 'Čočky, které omezují odlesky od hladin a silnic a zlepšují kontrast.'),
         ('Jaká je kategorie filtru 3?', 'Kategorie pro slunečný den, běžně užívaná na pláži, při sportu a turistice.'),
         ('Hodí se fotochromatické brýle?', 'Ano, v proměnlivém počasí, protože se přizpůsobí světlu.'),
         ('Jak vybrat dětské sluneční brýle?', 'S UV 400, měkkým rámem a pevným uchycením, které děti nesnáší hned shodí.')],
)

NEW['cinky-a-kotouce'] = dict(short=True,
    title='Činky a kotouče – jednoručky, kettlebelly, sady | Sporteka',
    desc='Činky, jednoručky, nakládací sady, kotouče a kettlebelly pro domácí posilování. Porovnejte ceny z českých obchodů a vyberte hmotnost a materiál.',
    intro='<p><strong>Činky a kotouče</strong> jsou základ domácího posilování. Pevné jednoručky se hodí na rychlý start, nakládací činky umožňují přidávat zátěž a kotouče s tyčí vytvoří silovou sadu. Správná hmotnost je taková, při které zvládnete techniku správně a poslední opakování už je náročné.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Další pomůcky najdete v kategoriích <a href="/kettlebelly/">kettlebelly</a>, <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>',
    guide='<h2>Jak vybrat činky a kotouče</h2>'
          '<p>Vybírejte podle cíle: posilování, tvarování těla nebo síla. Začátečníkům stačí sada jednoručních činek s mírnou zátěží, zkušenější ocení nakládací systém s kotouči.</p>'
          '<h3>Typy činek</h3>'
          '<ul><li><strong>Pevné jednoručky:</strong> fixní hmotnost, rychle k použití, často šestihranné, aby se neodkutálely.</li>'
          '<li><strong>Nakládací činky:</strong> tyč s kotouči, hmotnost si upravíte podle potřeby.</li>'
          '<li><strong>Dlouhé tyče a kotouče:</strong> základ pro bench press, dřepy a mrtvý tah.</li>'
          '<li><strong>Kettlebelly:</strong> koule s držadlem, pro dynamické cvičení.</li></ul>'
          '<h3>Materiál</h3>'
          '<p>Ocelové a litinové kotouče jsou tradiční a odolné, pogumované chrání podlahu a snižují hluk, vinylové a plastové se hodí pro lehké zátěže. Zkontrolujte průměr otvoru kotouče a tyče, aby si odpovídaly.</p>'
          '<h3>Jak zvolit hmotnost</h3>'
          '<p>Začněte s lehčí zátěží a správnou technikou, hmotnost zvyšujte postupně. Pro malé svalové skupiny, jako ramena a paže, je potřeba menší hmotnost než pro nohy a záda.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("hms", "HMS"), ("insportline", "inSPORTline"), ("sedco", "Sedco"), ("gorilla-sports", "Gorilla Sports"), ("gymbeam", "GymBeam"), ("hop-sport", "Hop-Sport"), ("fitforce", "Fitforce"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těžká zátěž na začátku, která vede ke špatné technice.</li><li>Nákup kotoučů, které nepasují na tyč.</li><li>Cvičení bez podložky na hladké podlaze.</li></ul>',
    faq=[('Jak těžké činky vybrat?', 'Takové, abyste zvládli správnou techniku. Pro začátek zvolte lehčí a postupně přidávejte.'),
         ('Pevné, nebo nakládací činky?', 'Pevné jsou rychlé a pohodlné, nakládací umožňují upravit hmotnost a bývají výhodnější v dlouhodobém použití.'),
         ('Jak poznám správný průměr kotouče?', 'Zkontrolujte průměr tyče a otvor kotouče, nejběžnější jsou 25–30 mm a 50 mm.'),
         ('Hodí se kettlebell pro začátečníka?', 'Ano, ale vyžaduje správnou techniku, začněte s lehčím modelem a poraďte se s trenérem.'),
         ('Jak chránit podlahu?', 'Podložkou nebo pogumovanými kotouči a činkami.')],
)

NEW['fitness-pomucky'] = dict(short=True,
    title='Fitness pomůcky – gumy, švihadla, podložky | Sporteka',
    desc='Fitness pomůcky pro cvičení doma: posilovací gumy, švihadla, balanční podložky, závěsné trenažéry a další. Porovnejte ceny z českých obchodů.',
    intro='<p><strong>Fitness pomůcky</strong> umožňují cvičit doma bez velkých strojů. Posilovací gumy, švihadla, balanční podložky a závěsné trenažéry zaberou málo místa a posílí celé tělo. Jsou ideální pro začátečníky i jako doplněk k činkám.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Najdete tu <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/svihadla/">švihadla</a> a <a href="/balancni-pomucky/">balanční pomůcky</a>, k nim <a href="/cinky-a-kotouce/">činky</a> a <a href="/joga-a-podlozky/">jógové podložky</a>.</p>',
    guide='<h2>Jak vybrat fitness pomůcky</h2>'
          '<p>Vyberte podle cíle: posílení, kondice, mobilita nebo rehabilitace. Pomůcky se liší odporem a obtížností, proto je lepší začít s lehčím odporem a přidávat.</p>'
          '<h3>Co k čemu</h3>'
          + T(['Pomůcka', 'Využití'], [['Posilovací guma', 'odpor pro ramena, nohy, hýždě a záda, jednoduché přenášení'], ['Švihadlo', 'kondice a koordinace, cvičení kdekoli'], ['Balanční podložka', 'stabilita a posílení hlubokého svalstva'], ['Závěsný trenažér', 'cvičení s vlastní vahou na dveřích nebo stropě'], ['Masážní válec', 'regenerace svalů a fascií']]) +
          '<h3>Odpor gum</h3>'
          '<p>Gumy se dělí podle odporu, často barvou. Lehčí slouží k zahřátí a rehabilitaci, silnější k posilování větších svalů. Kvalitní guma se neroztrhne a nesmekne.</p>'
          '<h3>Bezpečnost a péče</h3>'
          '<p>Před každým cvičením zkontrolujte, že se pomůcka nepoškodila. Gumy skladujte mimo slunce a vlhkost, aby neztratily pružnost.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("merco", "Merco"), ("hms", "HMS"), ("insportline", "inSPORTline"), ("gymbeam", "GymBeam"), ("sedco", "Sedco"), ("sportago", "Sportago"), ("viking", "Viking"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš silná guma na začátku, která vede k špatné technice.</li><li>Cvičení bez zahřátí.</li><li>Nesprávně upevněný závěsný trenažér.</li></ul>',
    faq=[('Jaké pomůcky na cvičení doma?', 'Posilovací gumy, činky, jógová podložka a švihadlo, tedy lehké věci, které zaberou málo místa.'),
         ('Jak vybrat posilovací gumu?', 'Podle odporu. Začněte lehčí a přecházejte na silnější podle pokroku.'),
         ('K čemu je balanční podložka?', 'Zlepšuje stabilitu a posiluje hluboké svaly trupu a nohou.'),
         ('Hodí se švihadlo pro začátečníky?', 'Ano, ale začněte krátkými intervaly a zvolte správnou délku podle výšky.'),
         ('Jak se starat o gumy?', 'Skladovat mimo slunce a vlhko a pravidelně kontrolovat trhliny.')],
)

NEW['rybarske-pruty'] = dict(short=True,
    title='Rybářské pruty – přívlačové, kaprové, feeder | Sporteka',
    desc='Rybářské pruty: přívlačové, kaprové, feederové, muškařské a dětské. Porovnejte ceny z českých obchodů a vyberte délku, akci a hmotnost nástrahy.',
    intro='<p><strong>Rybářský prut</strong> je základ výbavy a jeho parametry určují, jak daleko dohodíte, jak citlivě zaznamenáte záběr a jakou rybu zvládnete zdolat. Prut se vybírá podle způsobu lovu, ne podle délky a ceny. Jiný se hodí na přívlač, jiný na kapra a jiný na feeder.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K prutům patří <a href="/rybarske-navijaky/">navijáky</a>, <a href="/vlasce-a-snury/">vlasce</a> a <a href="/nastrahy-a-navnady/">nástrahy</a>. Hlavní stránkou je <a href="/rybareni/">rybaření</a>.</p>',
    guide='<h2>Jak vybrat rybářský prut</h2>'
          '<p>Nejdřív určete způsob lovu a rybu. Podle toho vyberte délku, akci a hmotnost nástrahy, kterou prut unese. Prut musí ladit s navijákem a vlascem.</p>'
          '<h3>Typy prutů</h3>'
          + T(['Typ', 'Použití'], [['Přívlačový', 'lov dravců na umělé nástrahy, kratší a rychlejší'], ['Kaprový', 'delší, s testní křivkou v librách, na dlouhé nahazování'], ['Feederový', 'lov na krmítko, s výměnnými špičkami'], ['Muškařský', 'lov na umělé mušky, lehký, podle třídy šňůry'], ['Teleskopický', 'skládací, praktický na cestování']]) +
          '<h3>Akce a hmotnost</h3>'
          '<p>Akce udává, jak se prut ohýbá: rychlá akce je citlivější a přesnější, pomalá odpouští chyby. Hmotnost nástrahy označuje, jaký rozsah prut bezpečně unese. Vždy se držte údajů výrobce.</p>'
          '<h3>Délka a dělení</h3>'
          '<p>Delší prut dohodí dál a lépe zvládne dlouhý souboj, kratší je obratnější v úzkých místech. Vícedílné pruty se snadněji převážejí.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("daiwa", "Daiwa"), ("shimano", "Shimano"), ("mikado", "Mikado"), ("westin", "Westin"), ("favorite", "Favorite"), ("delphin", "Delphin"), ("sema", "Sema"), ("fox", "Fox"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po výletě prut očistěte a osušte, zkontrolujte očka a skladujte v pouzdře. Při přepravě chraňte špičku před zlomením.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Prut s nesprávnou hmotností nástrahy, který se přetíží nebo nepracuje.</li><li>Příliš dlouhý prut do úzkých míst.</li><li>Zanedbaná očka, která poškrábou vlasec.</li></ul>',
    faq=[('Jaký prut na přívlač?', 'Kratší rychlý prut s hmotností nástrahy podle ryby a vody, spojený s malým navijákem a splétanou šňůrou.'),
         ('Co znamená akce prutu?', 'Způsob, jakým se prut ohýbá. Rychlá akce je citlivější, pomalá odpouští chyby.'),
         ('Co je testní křivka?', 'Údaj v librách u kaprových prutů, který popisuje sílu prutu a vhodné zatížení.'),
         ('Jak dlouhý prut vybrat?', 'Podle způsobu lovu a vody. Delší pro dálkové hody, kratší pro obratnost.'),
         ('Hodí se teleskopický prut?', 'Ano, na cestování a rekreační lov, výkonnostní lov vyžaduje spíš dělené modely.')],
)

NEW['zimni-obuv'] = dict(short=True,
    title='Zimní boty a sněhule – pánské, dámské, dětské | Sporteka',
    desc='Zimní boty a sněhule pánské, dámské a dětské: nepromokavé, zateplené, s membránou i městské. Porovnejte ceny z českých obchodů a vyberte velikost.',
    intro='<p><strong>Zimní boty</strong> mají udržet nohy v teple a suchu a zároveň držet na kluzkém povrchu. Rozhoduje materiál, podešev, zateplení a vodotěsnost. Městská zimní bota se liší od sněhule do hlubokého sněhu i od outdoorové trekové.</p>'
          '<p>Na Sportece najdete <strong>zimní boty pánské, dámské i dětské</strong> z českých obchodů, porovnáte ceny a vyberete podle velikosti. K teplým nohám patří <a href="/sportovni-ponozky/">ponožky</a> a <a href="/merino-ponozky/">merino ponožky</a>, k celému zimnímu outfitu <a href="/zimni-bundy/">zimní bunda</a>.</p>',
    guide='<h2>Jak vybrat zimní boty</h2>'
          '<p>Rozhodněte, kde je budete nosit. Do města stačí lehčí zateplená bota s dobrým vzorkem, do sněhu sněhule nebo bota s vysokou lýtkovou částí.</p>'
          '<h3>Typy zimní obuvi</h3>'
          '<ul><li><strong>Městské zateplené boty:</strong> lehké, s vodoodolnou úpravou, na procházky.</li>'
          '<li><strong>Boty s membránou:</strong> vodotěsné a prodyšné, na deštivé a sněhové dny.</li>'
          '<li><strong>Sněhule:</strong> vysoké, teplé a vodotěsné, do hlubokého sněhu.</li>'
          '<li><strong>Dětské zimní boty:</strong> s rychlým zapínáním a zateplením, často s reflexními prvky.</li></ul>'
          '<h3>Podešev a protiskluz</h3>'
          '<p>Hluboký vzorek zlepšuje přilnavost na sněhu, měkká pryž drží lépe na ledu. Zkontrolujte, že podrážka neztvrdne při mrazu.</p>'
          '<h3>Velikost a zateplení</h3>'
          '<p>Zimní bota má mít rezervu pro silnější ponožku a vzduch kolem prstů, který zlepšuje izolaci. Příliš těsná bota zhoršuje prokrvení a nohy mrznou rychleji.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("geox", "Geox"), ("loap", "Loap"), ("skechers", "Skechers"), ("o-neill", "O\'Neill"), ("moon-boot", "Moon Boot"), ("reima", "Reima"), ("alpine-pro", "Alpine Pro"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Boty po nošení vysušte při pokojové teplotě, nikoli na radiátoru. Impregnaci obnovte sprejem a odstraňte sůl, která poškozuje kůži.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těsná bota, ve které nohy mrznou.</li><li>Sušení na radiátoru, které poškodí materiál.</li><li>Městská bota s hladkou podešví na led.</li></ul>',
    faq=[('Jaké zimní boty vybrat?', 'Podle prostředí: do města zateplené s dobrým vzorkem, do sněhu sněhule nebo boty s membránou.'),
         ('Jaká velikost zimních bot?', 'S rezervou na silnější ponožku a s prostorem pro prsty, zhruba o půl velikosti větší.'),
         ('Co je membrána v botě?', 'Vrstva, která propouští páru ven a zadržuje vodu, díky ní zůstává noha suchá.'),
         ('Jak sušit zimní boty?', 'Při pokojové teplotě, s vytaženou vložkou, ne na radiátoru.'),
         ('Jaké zimní boty pro děti?', 'Teplé, nepromokavé s rychlým zapínáním a pevnou podrážkou, v takové velikosti, která nestlačí prsty.')],
)

NEW['lahve-a-termosky'] = dict(short=True,
    title='Láhve a termosky – sportovní, dětské, termolahve | Sporteka',
    desc='Sportovní láhve, termosky, hydrovaky a šejkry: tritan, nerez, dětské i turistické. Porovnejte ceny z českých obchodů a vyberte objem a materiál.',
    intro='<p><strong>Láhev na pití</strong> je nejjednodušší způsob, jak mít při sportu a na výletě po ruce vodu. Termoska a termoláhev udrží nápoj teplý nebo studený hodiny, hydrovak se hodí na kolo a trek. Při výběru rozhodují materiál, objem, zavírání a to, zda vyhovuje dětem nebo dospělým.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Pro kolo najdete <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a>, pro trek <a href="/turisticke-batohy/">turistické batohy</a>, na cesty <a href="/vareni-v-prirode/">vaření v přírodě</a>.</p>',
    guide='<h2>Jak vybrat láhev nebo termosku</h2>'
          '<p>Nejdřív zvolte použití: sport, turistika, kancelář nebo dítě. Podle toho vyberte materiál a objem. Pro každodenní použití je praktická lehká láhev, na výlet termoska.</p>'
          '<h3>Materiály</h3>'
          '<ul><li><strong>Tritan a plast bez BPA:</strong> lehký a nerozbitný, vhodný na sport.</li>'
          '<li><strong>Nerez:</strong> odolný a bez zápachu, dobrý pro termosky a láhve na turistiku.</li>'
          '<li><strong>Hliník:</strong> lehký, často s vnitřní úpravou.</li>'
          '<li><strong>Sklo:</strong> bez zápachu, ale těžší a křehké.</li></ul>'
          '<h3>Objem podle použití</h3>'
          + T(['Použití', 'Objem'], [['Běh a kolo', '500–750 ml'], ['Turistika', '750 ml – 1 l'], ['Celodenní túra', '1–2 l nebo hydrovak'], ['Děti do školy', '300–500 ml'], ['Termoska na výlet', '350–750 ml']]) +
          '<h3>Termo a zavírání</h3>'
          '<p>Termolahve s dvojitou stěnou udrží nápoj teplý nebo studený hodiny. Sportovní uzávěr s pítkem se hodí při běhu, šroubovací pro turistiku a dětské brčko pro školky.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("laken", "Laken"), ("thermos", "Thermos"), ("camelbak", "CamelBak"), ("nalgene", "Nalgene"), ("primus", "Primus"), ("force", "Force"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Láhve perte pravidelně a nechte je vyschnout otevřené. Termosky nenechávejte dlouho s čajem nebo džusem, nerez může pachnout.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těsná zátka, která zhoršuje mytí.</li><li>Termoska s mlékem nebo sladkým nápojem nevymytá do druhého dne.</li><li>Láhev bez držáku při jízdě na kole.</li></ul>',
    faq=[('Jaká láhev na sport?', 'Lehká z tritanu nebo hliníku s uzávěrem, který se dá otevřít jednou rukou.'),
         ('Jak dlouho termoska drží teplo?', 'Podle modelu několik hodin, kvalitní nerezové termosky drží teplo i celý den. Údaj najdete u každého produktu.'),
         ('Co je tritan?', 'Plast bez BPA, odolný, lehký a dobře se myje, často se používá u sportovních lahví.'),
         ('Jak vybrat termosku pro dítě?', 'S bezpečným uzávěrem, bez ostrých hran a s objemem podle věku.'),
         ('Jak pečovat o termosku?', 'Po použití vymýt a nechat uschnout otevřenou, aby nezapáchala.')],
)

NEW['sportovni-tasky'] = dict(short=True,
    title='Sportovní tašky a ledvinky – fitness, cestovní | Sporteka',
    desc='Sportovní tašky, ledvinky, duffel bagy a vodotěsné vaky: na trénink, cesty i kolo. Porovnejte ceny z českých obchodů a vyberte objem a materiál.',
    intro='<p><strong>Sportovní taška</strong> musí uchovat vybavení v pořádku a pohodlně se nosit. Do posilovny vybíráte jinou než na cesty nebo na vodu: trénink potřebuje oddělené kapsy na boty a vlhké věci, cesty pevné a prostorné duffel bagy a voda vodotěsné vaky.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K taškám patří <a href="/batohy/">batohy</a>, <a href="/tasky-pres-rameno/">tašky přes rameno</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    guide='<h2>Jak vybrat sportovní tašku</h2>'
          '<p>Vyberte podle použití a objemu. Taška má pohodlná ucha, pevný popruh přes rameno a materiál, který snese vlhko a oděr.</p>'
          '<h3>Typy tašek</h3>'
          + T(['Typ', 'Použití'], [['Fitness taška', 'trénink, oddělená kapsa na boty a vlhké věci'], ['Duffel bag', 'cesty a víkendy, prostorný a odolný'], ['Ledvinka', 'drobnosti při běhu, kole a procházkách'], ['Vodotěsný vak', 'voda, kajak, paddleboard a deštivé počasí'], ['Taška přes rameno', 'doklady a drobnosti v městském stylu']]) +
          '<h3>Objem</h3>'
          '<p>Na jeden trénink stačí 20–40 l, na víkend 40–70 l a na dlouhou cestu 70 l a více. Příliš velká taška se naplní zbytečnou váhou.</p>'
          '<h3>Materiály a odolnost</h3>'
          '<p>Silný nylon nebo polyester snese oděr a vlhko, vodotěsné modely mají svařené švy a rolovací uzávěr. Zkontrolujte zipy, popruhy a spodní dno.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("fjallraven", "Fjällräven"), ("deuter", "Deuter"), ("adidas", "Adidas"), ("nike", "Nike"), ("the-north-face", "The North Face"), ("hms", "HMS"), ("merco", "Merco"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po tréninku taška vyvětrejte a vysušte, vlhké věci nenechávejte uvnitř. Čistěte vlhkým hadrem a skladujte volně.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velká taška, která se zbytečně zatíží.</li><li>Špatná ucha, která se při zatížení trhají.</li><li>Vlhké věci zavřené v tašce bez větrání.</li></ul>',
    faq=[('Jakou tašku vybrat do posilovny?', 'Taška 30–40 l s oddělenou kapsou na boty, pevnými uchy a odolným materiálem.'),
         ('Co je duffel bag?', 'Válcová prostorná taška bez pevné konstrukce, praktická na cesty a sport.'),
         ('K čemu je vodotěsný vak?', 'Ochrání věci před vodou na kajaku, paddleboardu nebo za deště.'),
         ('Jak se starat o sportovní tašku?', 'Po tréninku vyvětrat a osušit, čistit vlhkým hadrem a skladovat suchou.'),
         ('Hodí se ledvinka na běh?', 'Ano, lehká a pevná ledvinka udrží telefon a klíče bez houpání.')],
)
