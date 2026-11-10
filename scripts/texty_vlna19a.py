"""sporteka.cz — wave 19a (4. 11. 2026): long texts (>= 1650 words) for neopreny, sportovni-spodni-pradlo, pilates-pomucky, cyklo-zamky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ neopreny
NEW['neopreny'] = dict(long=True,
    title='Neopreny: pěnové obleky, tloušťka a velikost',
    desc='Neoprenové obleky, boty, rukavice a vesty pro surf, paddleboard, potápění i plavání. Jak vybrat tloušťku, střih a velikost a porovnat obchody.',
    intro='<p>Neopren je pěnová pryž s uzavřenými buňkami plynu, která izoluje tělo od chladné vody a zároveň se na něm dobře přizpůsobí tvaru. '
          'Díky němu se dá na paddleboardu, surfu, kajaku nebo při plavání v jezeře zůstat venku i tehdy, kdy by se bez obleku nedalo vydržet déle než pár minut. '
          'Výběr ale není jen o tloušťce: záleží na střihu, švech, zapínání a hlavně na přesné velikosti, protože oblek, který nepřiléhá, vodu nezachytí.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u obleků, bot, rukavic i čepic od značek O\'Neill, Hiko, Aqualung, ION nebo Roxy. '
          'Podle sportu se hodí i <a href="/paddleboardy/">paddleboardy</a>, <a href="/kajaky-a-cluny/">kajaky a čluny</a>, <a href="/snorchlovani/">šnorchlování</a> a <a href="/plavky/">plavky</a>. '
          'Níže najdete přehled typů, rozdíly mezi tloušťkami a praktické rady pro velikost a péči.</p>',
    guide='<h2>Jak neopren funguje</h2>'
          '<p>Materiál obsahuje drobné bublinky plynu, které špatně vedou teplo. Do obleku proniká tenká vrstva vody, tělo ji ohřeje a vrstva pak funguje jako další izolace. '
          'Proto musí oblek sedět těsně, ale nesmí stahovat dech. Pokud je příliš volný, voda uvnitř neustále proudí a tělo se ochlazuje. '
          'Suchý oblek se oproti tomu vodě bez zbytku brání a patří do jiné kategorie vybavení. Neopreny na Sportece jsou převážně mokré obleky, doplněné botami, rukavicemi, kapucemi a vestami.</p>'
          '<h2>Typy neoprenů</h2>'
          + T(['Typ', 'Co kryje', 'Typické použití'], [
              ['Dlouhý oblek (fullsuit)', 'celé tělo včetně paží a nohou', 'chladnější voda, surf, plavání, potápění'],
              ['Krátký oblek (shorty)', 'trup, krátké rukávy a nohavice', 'teplejší voda, léto, paddleboard'],
              ['Spring suit', 'dlouhé rukávy a krátké nohavice nebo naopak', 'přechodné období'],
              ['Neoprenové kalhoty a farmer john', 'nohy a trup bez rukávů', 'kajak, rybaření, vodní lyže, volnost paží'],
              ['Vesta, top a bunda', 'jen horní část těla', 'doplněk, ochrana proti větru'],
              ['Boty, rukavice, čepice', 'končetiny a hlava', 'studená voda, kameny, výdrž']]) +
          '<h2>Tloušťka a teplota vody</h2>'
          '<p>Tloušťka se udává v milimetrech a často ve dvou nebo třech číslech, například 3/2. První hodnota platí pro trup, druhá pro končetiny, kde je pohyblivost důležitější. '
          'Tloušťku volte podle teploty vody, ročního období a doby, kterou ve vodě strávíte; konkrétní teplotní rozmezí uvádí výrobce u každého modelu. Při plavání produkuje tělo více tepla než při stání na surfu, takže stejný oblek působí různě.</p>'
          + T(['Tloušťka', 'Charakter', 'Hodí se do'], [
              ['do 2 mm', 'velmi pohodlný, tenký', 'teplé vody, léto, ochrana před sluncem a otěrem'],
              ['3/2 mm', 'univerzální volba', 'jaro a podzim, vodní sporty v mírné vodě'],
              ['4/3 mm', 'tepleji, méně pružný', 'chladné vody, delší pobyt, zima s dalšími doplňky'],
              ['5 mm a víc', 'velmi teplý a tuhý', 'velmi studená voda, často s kapucí']]) +
          '<p>Tabulka je orientační a každý výrobce přidává vlastní doporučení pro rozsah teplot. Citlivější lidé a děti se ochlazují rychleji, proto volí tepleji. Pokud jste na vodě jen krátce a hlavně se hýbete, vystačí tenčí oblek.</p>'
          '<h2>Střih, švy a zapínání</h2>'
          '<h3>Zip na zádech nebo na hrudi</h3>'
          '<p>Zip na zádech se nejlépe obléká, ale nechává místo, kudy proniká voda. Hrudní zip bývá těsnější a teplejší, oblékání je však náročnější. Zapínání bez zipu je pružnější, ale vyžaduje cvik. Na zip se hodí lehký sprej na zip, ostatní mazání nepoužívejte.</p>'
          '<h3>Švy</h3>'
          '<p>Ploché švy jsou levnější a pohodlné ve vlažné vodě. Lepené a slepené švy zabraňují průniku vody dovnitř a patří do chladnějších podmínek. Vnější přelepení zvyšuje odolnost, ale oblek ztuhne. Před nákupem zkontrolujte, zda jsou švy v namáhaných místech, zejména v podpaží a v rozkroku, pevně přilepené.</p>'
          '<h3>Vnitřní podšívka</h3>'
          '<p>Hladká nebo plyšová podšívka přidává teplo a rychle schne. Oblek bez podšívky se hůř obléká, ale lépe odvádí vodu a hodí se k plavání. Podšívka se při opakovaném nošení otírá, proto ji perte jen jemně.</p>'
          '<h2>Velikost a pohodlí</h2>'
          '<p>Neoprenové velikosti se liší výškou i obvody, takže stačí překročit hranici v jedné míře a oblek už nesedí. Vezměte metr, změřte výšku, hrudník, pas a boky a porovnejte hodnoty s tabulkou výrobce. Mezi dvěma velikostmi se rozhodněte podle sportu: pro plavání bývá lepší menší, pro paddleboard a kajak mírně volnější v ramenou. '
          'Oblek se po několika použitích mírně přizpůsobí, ale nikdy se výrazně nenatáhne. Při zkoušce musí obepínat celé tělo bez záhybů v tříslech a v podpaží a v ramenou nesmí táhnout.</p>'
          '<p>Dětské neopreny se vybírají s menší rezervou, než se dá čekat. Dítě rychle roste, ale příliš velký oblek nehřeje a zvyšuje nebezpečí prochladnutí. Vyplatí se proto zkoušet po sezóně nebo používat dětské modely s nastavitelnými nohavicemi, pokud je výrobce nabízí.</p>'
          '<h2>Výběr podle sportu</h2>'
          '<ul><li><strong>Surfování a bodyboard:</strong> pružný oblek s lepenými švy, tloušťka podle moře, často s kapucí a botami.</li>'
          '<li><strong>Paddleboard a kajak:</strong> důraz na volnost paží, hodí se farmer john nebo shorty s vestou, protože do vody padáte jen příležitostně. Základ vodní výbavy najdete v kategorii <a href="/vodni-sporty/">vodní sporty</a>.</li>'
          '<li><strong>Plavání v otevřené vodě a triatlon:</strong> speciální plavecké obleky mají tenčí a pružnější materiál na ramenou a hladký povrch. Souvisí s tím kategorie <a href="/triatlon/">triatlon</a>, <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plavecké čepice</a>.</li>'
          '<li><strong>Šnorchlování a potápění:</strong> tlustší materiál pro delší pobyt, doplněný o masku a ploutve ze skupiny <a href="/snorchlovani/">šnorchlování</a>.</li>'
          '<li><strong>Rybaření a lodě:</strong> neoprenové kalhoty a boty chrání před chladem při brodění.</li></ul>'
          '<h2>Neoprenové boty, rukavice a doplňky</h2>'
          '<p>Nohy a ruce se ve vodě ochlazují nejdřív, proto chladnější sezóna vyžaduje i tyto díly. Boty mají tenkou podrážku pro letní kameny nebo silnější s vyztuženou špičkou. Zip na boku usnadní oblékání, ale tvoří slabé místo. '
          'Rukavice bývají dvou nebo pětiprsté, tenké přidají cit, silnější teplo. Neoprenová kapuce nebo čepice zadržuje teplo hlavy, kterou tělo ztrácí rychleji než zbytek. '
          'Pokud chcete jen ochranu před sluncem a otěrem bez zateplení, stačí <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mezi neopreny mají ' + B(("o-neill", "O'Neill"), ("hiko", "Hiko"), ("decathlon", "Decathlon"), ("agama", "Agama"), ("aqualung", "Aqualung"), ("nrs", "NRS"), ("palm", "Palm"), ("ion", "ION")) +
          '. Další nabídku mají ' + B(("elements-gear", "Elements Gear"), ("roxy", "Roxy"), ("kaiwai", "Kaiwai"), ("splash-about", "Splash About")) + '. '
          'Surfové značky kladou důraz na pružnost, potápěčské na odolnost a rybářské na praktické kapsy a kalhoty. Dětské obleky najdete například u značky Splash About. Porovnejte střih a materiál u konkrétního modelu a nespoléhejte jen na jméno výrobce.</p>'
          '<h2>Péče o neopren</h2>'
          '<p>Po každém použití oblek opláchněte čistou vlažnou vodou, aby z materiálu zmizela sůl, písek a chlór. Suší se ve stínu, nejlépe převrácený na rubovou stranu, na tlustém ramínku nebo přehozený přes tyč. Přímé slunce a radiátor materiál rychle zkřehnou. '
          'Neoprenový oblek nikdy nežehlete, nesušte v sušičce a nepoužívejte běžný prací prášek s bělidlem. Na praní stačí speciální přípravek nebo jemný šampon a ruční praní.</p>'
          '<p>Uskladněte ho zavěšený nebo volně rozložený, aby se nevytvořily záhyby. Poškozené místo se dá často opravit speciálním lepidlem na neopren, pokud trhlina není na zipu nebo v namáhaném švu.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš volný oblek, který se plní vodou. Raději volte menší, když máte pochybnost o velikosti.</li>'
          '<li>Příliš tlustý materiál pro letní vodu, v němž se přehřejete a hůř pohybujete.</li>'
          '<li>Ignorování zipu a švů. Levný oblek s plochými švy se hodí do vlažné vody, ne do jarního jezera.</li>'
          '<li>Koupě jen podle designu bez ohledu na sport, pro který oblek slouží.</li>'
          '<li>Nepoužití ponožek či bot. Bez nich vám v chladné vodě zmrznou nohy dřív než zbytek těla.</li></ul>'
          '<h2>Kdy kupovat</h2>'
          '<p>Nabídka je nejširší na jaře, ceny se ale hýbou nejvíc po sezóně, když obchody uvolňují sklady. Pokud znáte velikost, sledujte starší kolekce, které se funkčně příliš nemění. Na Sportece vidíte vedle sebe nabídky několika obchodů a rychle poznáte, kde se oblek vyskytuje v hledané velikosti. '
          'Ke krátkému pobytu v teplé vodě může stačit tenčí kus a doplnění o <a href="/plavky/">plavky</a>, <a href="/detske-plavky/">dětské plavky</a> nebo <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>',
    faq=[
        ('Jak poznám správnou velikost neoprenu?', 'Změřte výšku, hrudník, pas a boky a srovnejte hodnoty s tabulkou výrobce. Oblek má obepínat tělo bez záhybů, v podpaží netáhnout a nesmí bránit dýchání.'),
        ('Jaká tloušťka se hodí na paddleboard?', 'Na jaro a podzim obvykle stačí tloušťka kolem 3 mm, v létě i tenčí, případně jen vesta nebo shorty. Při pádech do chladné vody je lepší oblek tlustší a s dlouhými nohavicemi.'),
        ('Je lepší dlouhý, nebo krátký neopren?', 'Dlouhý oblek hřeje celé tělo a hodí se do chladnější vody. Krátký je pohodlnější v létě a nechává více volnosti, ale nohy zůstávají odkryté.'),
        ('Dá se neopren používat i při plavání?', 'Ano, ale pro delší plavání jsou vhodnější specializované plavecké modely s tenčím a pružnějším materiálem na ramenou. Klasický surfový oblek bývá tužší a plavec se v něm rychleji unaví.'),
        ('Má se neopren nosit s plavkami pod ním?', 'Většina lidí pod oblek obléká plavky, aby se oblek snadno nasazoval a nedřel. Pro chladné podmínky se někdy přidává tenká lycra nebo termo vrstva.'),
        ('Jak neopren správně sušit a prát?', 'Opláchněte ho čistou vodou, otočte na rubovou stranu a sušte ve stínu. Nesuší se na slunci ani na topení, nežehlí se a nepere se v pračce s prostředky na bělení.'),
        ('Co dělat, když neopren zapáchá?', 'Namočte ho do vlažné vody se speciálním přípravkem na neopren nebo jemným šamponem a pak důkladně vypláchněte. Pach je obvykle znamení, že oblek zůstal vlhký zabalený.'),
        ('Jak poznám, že je oblek poškozený?', 'Podívejte se na švy v podpaží a v rozkroku, na zip a na místa s popraskaným povrchem. Drobné trhliny lze přelepit lepidlem na neopren, větší poškození raději řešit výměnou.'),
        ('Hodí se neopren i pro děti?', 'Ano, děti se ve vodě ochlazují rychleji než dospělí. Dětský oblek musí sedět těsně, ale nesmí tlačit, a při delším pobytu ve vodě je potřeba dohled dospělého.'),
        ('Musím kupovat boty a rukavice zvlášť?', 'V teplé vodě stačí oblek samotný. V chladnější sezóně se ochlazují nejdřív ruce a nohy, proto se boty a rukavice vyplatí přidat, zvlášť při delším pobytu ve vodě.'),
    ])

# ------------------------------------------------------------------ sportovni-spodni-pradlo
NEW['sportovni-spodni-pradlo'] = dict(long=True,
    title='Sportovní spodní prádlo: boxerky, kalhotky, trenýrky',
    desc='Sportovní spodní prádlo pánské, dámské i dětské. Jak vybrat materiál, střih a velikost pro běh, kolo, fitness i outdoor a porovnat obchody.',
    intro='<p>Spodní prádlo je první vrstva, která se dotýká kůže, a při pohybu rozhoduje o tom, zda budete myslet na sport, nebo na tření a vlhkost. '
          'Sportovní modely se od běžného bavlněného prádla liší materiálem, který odvádí pot, střihem, který se při pohybu neposouvá, a švy, které nedřou. '
          'Hodí se při běhu, jízdě na kole, ve fitku, na horách i při dlouhém dni v práci, kdy chcete suchou a pohodlnou kůži.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u boxerek, trenýrek, kalhotek, spodních triček a sad od značek Viking, Klimatex, Craft, Smartwool, Kari Traa nebo Icebreaker. '
          'K tématu se vážou také <a href="/termopradlo/">termoprádlo</a>, <a href="/sportovni-podprsenky/">sportovní podprsenky</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>. '
          'Níže najdete přehled materiálů, střihů a zásad péče.</p>',
    guide='<h2>Co dělá prádlo sportovním</h2>'
          '<p>Základem je materiál, který pot nasává co nejméně a rychle ho pouští do vrstvy nad sebou. Kůže zůstane suchá, takže se tolik neochlazuje a méně dře. '
          'Další znaky jsou pružnost ve čtyřech směrech, ploché nebo bezešvé spoje, nízký pas, který netlačí, a v mnoha modelech zpevněné nebo větrané partie. '
          'Naproti tomu čistá bavlna nasákne potem, těžkne a pomalu schne, takže se k dlouhému pohybu příliš nehodí.</p>'
          '<h2>Materiály</h2>'
          + T(['Materiál', 'Vlastnosti', 'Vhodné pro'], [
              ['Polyester', 'rychle schne, málo nasákne', 'běh, kolo, fitness, horké dny'],
              ['Polyamid (nylon)', 'hladký, pevný, příjemný na dotek', 'bezešvé střihy, přiléhavé modely'],
              ['Elastan (lycra)', 'dodává pružnost', 'v příměsi u většiny sportovních kusů'],
              ['Merino vlna', 'hřeje i vlhká, méně zapáchá', 'outdoor, chladno, vícedenní túry'],
              ['Viskóza a bambus', 'měkké, jemné na kůži', 'každodenní nošení, nižší zátěž'],
              ['Bavlna se syntetikou', 'komfort a přijatelná sušivost', 'volnější aktivity']]) +
          '<p>Syntetické vlákno často obsahuje přísadu proti zápachu, ale účinek nikdy nenahradí pravidelné praní. Vlna je přírodní vláknina a lehčí merino modely vydrží i horké dny. U citlivé pokožky a alergií jsou důležité hladké švy, štítky mimo kůži a materiál, který nedráždí; některé lidi dráždí vlna, jiné určité syntetické směsi.</p>'
          '<h2>Pánské spodní prádlo</h2>'
          '<h3>Boxerky a trenýrky</h3>'
          '<p>Přiléhavé boxerky s delší nohavicí zabraňují tření stehen a drží tvar při běhu i jízdě na kole. Volnější trenýrky nabízejí větší ventilaci, ale při intenzivním pohybu se mohou vyhrnovat. Při výběru zkontrolujte pas, aby neřezal, a vnitřní švy, které se při pohybu pohybují po kůži.</p>'
          '<h3>Slipy a sportovní spodky</h3>'
          '<p>Slipy jsou nejlehčí, ale vlhnou rychleji a při delší aktivitě nedávají stehnům ochranu. Hodí se pod těsné kalhoty, plavky a na kratší trénink. Pánské modely se zpevněnou přední částí zvyšují komfort při jízdě na kole a při běhu v členitém terénu.</p>'
          '<h2>Dámské spodní prádlo</h2>'
          '<p>Dámské kalhotky se dělají v různých délkách střihu: klasické, brazilské, střih bokové a vysoké. Bezešvé kusy se hodí pod těsné legíny, vysoký pas drží tvar a nevyhrnuje se při předklonu. Pod cyklistické kraťasy s vložkou se spodní prádlo nenosí, jinak vložka nefunguje správně a švy odírají. '
          'K horní části patří <a href="/sportovni-podprsenky/">sportovní podprsenky</a> a pod funkční oblečení také <a href="/leginy/">legíny</a> či <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>'
          '<h2>Spodní trička a doplňky</h2>'
          '<p>Spodní tričko tvoří vrstvu mezi kůží a bundou. Pro letní horké dny stačí tenké tílko z polyesteru, v zimě se přidává <a href="/termopradlo/">termoprádlo</a> z jemné vlny nebo syntetiky. Kdo hledá přírodní variantu, najde ji v kategoriích <a href="/merino-pradlo/">merino prádlo</a> a <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>. '
          'Nezapomeňte na ponožky: <a href="/merino-ponozky/">merino ponožky</a> udrží chodidlo v suchu, a tím brání vzniku puchýřů.</p>'
          '<h2>Výběr podle sportu</h2>'
          + T(['Sport', 'Na co dbát', 'Typický kus'], [
              ['Běh', 'bezešvé švy, lehká tkanina, žádné štítky', 'boxerky nebo kalhotky z polyamidu'],
              ['Kolo', 'ochrana před třením, kraťasy s vložkou nad spodním prádlem se nenosí', 'bezešvé kusy bez silných švů'],
              ['Fitness a crossfit', 'držení tvaru při dřepech a výpadech', 'přiléhavé, pružné a neprůhledné'],
              ['Turistika a outdoor', 'merino nebo rychleschnoucí syntetika, málo zápachu', 'lehké merino boxerky, spodní prádlo na vícedenní túry'],
              ['Plavání', 'pro bazén sportovní plavky, ne spodní prádlo', 'plavky z kategorie <a href="/plavky/">plavky</a>'],
              ['Zimní sporty', 'teplá vrstva bez nadměrné objemnosti', 'vlněné nebo hřejivé syntetické spodky']]) +
          '<h2>Střih a velikost</h2>'
          '<p>Velikost spodního prádla se řídí obvodem boků a pasu. Změřte se před zrcadlem a porovnejte s tabulkou výrobce, protože konfekční čísla se u různých značek liší. Příliš těsné prádlo se zařezává a omezuje krevní oběh, volné se při pohybu pohybuje a tře. '
          'Správně sedící kus se nehýbe, žádný okraj nevytváří viditelný otlak a pas zůstává na místě i po delším pohybu. Zvlášť pozor na délku nohavic u mužských boxerek: musí končit pod hranicí tření stehen, ale nesmí se podsouvat vzhůru.</p>'
          '<h2>Prádlo pro děti</h2>'
          '<p>Děti potřebují měkký materiál bez drsných štítků a bez tlačících gumiček. Pro školní tělocvik a sportovní kroužky stačí pohodlné bavlněné nebo bavlněno-syntetické prádlo, při dlouhých pobytech venku je lepší syntetika či merino. Dětské prádlo se rychle vyměňuje, protože děti rostou, a proto se vyplatí kupovat rovnou více kusů.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("viking", "Viking"), ("klimatex", "Klimatex"), ("craft", "Craft"), ("smartwool", "Smartwool"), ("trespass", "Trespass"), ("adidas", "Adidas"), ("sensor", "Sensor"), ("puma", "Puma")) +
          '. Další nabídku mají ' + B(("kari-traa", "Kari Traa"), ("speedo", "Speedo"), ("icebreaker", "Icebreaker"), ("atlantic", "Atlantic"), ("nike", "Nike"), ("saxx", "Saxx")) + '. '
          'Outdoorové značky sázejí na vlnu a funkční vlákna, sportovní na bezešvé technologie a módní řady na barevnost. Hodnoťte střih a složení u konkrétního kusu, ne jen název výrobce.</p>'
          '<h2>Péče o sportovní prádlo</h2>'
          '<p>Perte ho podle štítku, obvykle na šetrný cyklus a nižší teplotě. Aviváž ucpává mikropóry funkčních vláken a zhoršuje odvod potu, proto ji vynechte. Bělidlo poškozuje elastan. Sušte volně, bez sušičky a mimo topení, protože vysoká teplota zničí pružnost. '
          'Vlněné kusy perte jen jemným prostředkem určeným na vlnu a sušte vleže, aby se nenatáhly. Praní provádějte brzy po tréninku, protože zaschlý pot zhoršuje zápach.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nošení bavlny na dlouhý nebo intenzivní trénink. Nasákne a při chladu ochlazuje.</li>'
          '<li>Volba velikosti „pro jistotu“ větší. Volné prádlo se pohybuje a tře.</li>'
          '<li>Kombinace silných švů a těsných kalhot, které vytváří otlaky.</li>'
          '<li>Aviváž a vysoká teplota při praní, které zničí funkci materiálu.</li>'
          '<li>Opakované nošení bez výměny, i když pot z vláken nevymizel.</li></ul>'
          '<h2>Kdy kupovat a jak porovnávat</h2>'
          '<p>Spodní prádlo se prodává po sadách i jednotlivě. Sady bývají výhodnější, ale ověřte, zda všechny kusy odpovídají vaší velikosti a způsobu použití. Prádlo se opotřebuje dříve než svrchní oblečení, takže se vyplatí obnovovat ho po pár sezónách. '
          'Na Sportece vidíte nabídky obchodů vedle sebe a můžete porovnat dostupné velikosti. Pokud skládáte celou sadu, podívejte se i na <a href="/funkcni-tricka/">funkční trička</a>, <a href="/sportovni-tricka/">sportovní trička</a> a <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>',
    faq=[
        ('Čím se sportovní spodní prádlo liší od běžného?', 'Odvádí pot, rychle schne, přiléhá a nemá silné švy. Běžná bavlna se při pohybu nasákne a pomalu schne, takže kůže zůstává vlhká.'),
        ('Je pro běh lepší boxerka, nebo slip?', 'Pro delší běh se většinou vyplatí přiléhavé boxerky, protože chrání stehna před třením. Slip je lehčí a vhodný na kratší trénink pod volnější oblečení.'),
        ('Hodí se merino i na sport v létě?', 'Ano, lehké merino dobře reguluje teplotu a méně zapáchá, takže se hodí i na horské túry za tepla. Na intenzivní běh se někdy hodí spíše syntetika, která schne rychleji.'),
        ('Proč se nemá používat aviváž?', 'Aviváž zanáší strukturu funkčních vláken a zhoršuje odvod potu. Tkanina pak nasává vlhkost a zápach se drží déle.'),
        ('Mám nosit spodní prádlo pod cyklistické kraťasy?', 'Obvykle ne. Cyklistické kraťasy mají vlastní vložku, která se nosí přímo na kůži, a další vrstva by vytvářela švy a tření.'),
        ('Jak se vybírá velikost?', 'Změřte obvod pasu a boků a porovnejte s tabulkou výrobce. Prádlo má přiléhat bez zařezávání a nemá se při pohybu posouvat.'),
        ('Dá se sportovní prádlo sušit v sušičce?', 'Raději ne. Vysoká teplota poškozuje elastan a zkracuje životnost pružnosti, proto je lepší sušit volně na vzduchu mimo zdroj tepla.'),
        ('Jak poznám bezešvé prádlo?', 'Bezešvé kusy se pletou v jednom celku a nemají silné boční švy. Na dotek jsou hladší a při pohybu méně dřou, ale mívají omezený počet velikostí.'),
        ('Je spodní prádlo vhodné i pro děti?', 'Ano, děti ocení měkký materiál bez štítků a gumiček, které tlačí. Při dlouhém pobytu venku se hodí funkční syntetika nebo lehké merino.'),
        ('Kdy prádlo vyměnit?', 'Když ztratí pružnost, poklesne mu pas nebo začne dřít. Intenzivně nošené kusy vydrží zhruba několik sezón, při správné péči déle.'),
    ])

# ------------------------------------------------------------------ pilates-pomucky
NEW['pilates-pomucky'] = dict(long=True,
    title='Pilates pomůcky: míče, kruhy, gumy a podložky',
    desc='Pilates pomůcky pro cvičení doma i ve studiu: overbally, kruhy, gumy, válce a podložky. Jak vybrat velikost a materiál a porovnat obchody.',
    intro='<p>Pilates je cvičení zaměřené na střed těla, kontrolu pohybu a správné dýchání. Pomůcky nejsou nutné, ale přidávají odpor, nestabilitu nebo oporu a pomáhají cvičit přesněji. '
          'Jednoduchá podložka, malý míč a guma stačí na celou řadu cviků doma a každý další kus rozšiřuje možnosti: kruh posiluje vnitřní a vnější stehna a paže, válec uvolňuje svaly a míč zapojuje hluboké svaly trupu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek HMS, Merco, Insportline, Ledragomma, Lifefit, GymBeam nebo Domyos. '
          'Základ vybavení doplníte kategoriemi <a href="/joga-a-podlozky/">jóga a podložky</a>, <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>. '
          'Níže najdete přehled typů, výběr podle cílů a rady, jak pomůcky používat bezpečně.</p>',
    guide='<h2>Co do pilates patří</h2>'
          '<p>Pomůcky jsou odvozeny z klasických cviků na podložce i z přístrojů používaných ve studiích. Doma se využívají malé a lehké kusy, které se vejdou do skříně. Studiové přístroje, jako je reformer, jsou rozměrné a pro běžné cvičení doma nejsou nutné. '
          'Menší pomůcky nabízejí podobný efekt: odpor, nestabilitu nebo zvýšenou oporu. Pomůcku vybírejte podle cvičebního cíle, ne podle toho, co je zrovna v akci.</p>'
          + T(['Pomůcka', 'K čemu slouží', 'Pro koho'], [
              ['Podložka', 'tlumí podlahu, chrání páteř a kostrč', 'všichni, základní výbava'],
              ['Overball (malý míč)', 'opora pod zády, aktivace středu těla', 'začátečníci i pokročilí'],
              ['Pilates kruh', 'odpor pro paže a nohy', 'cvičení horních i dolních končetin'],
              ['Odporová guma', 'jemný až střední odpor', 'rehabilitační cvičení, doplněk silového tréninku'],
              ['Válec (foam roller)', 'automasáž a uvolnění', 'po tréninku nebo při ztuhlosti'],
              ['Balanční podložka a půlkoule', 'nestabilní povrch', 'rovnováha, koordinace'],
              ['Velký gymnastický míč', 'sed, cviky na trup', 'posilování středu těla a práce s dechem']]) +
          '<h2>Podložka</h2>'
          '<p>Pilates se cvičí často vleže na zádech, takže podložka musí stačit na to, aby neprotlačila kostrč a páteř. Doporučuje se tloušťka výrazně větší než u jógové podložky, protože v józe se spíše stojí. '
          'Materiál se vybírá mezi pěnou NBR, TPE a přírodním kaučukem. NBR je měkká a levnější, TPE dobře odolává otěru a přírodní kaučuk drží i při potu, ale bývá těžší. Ověřte také protiskluzovou povrchovou úpravu. '
          'Pro cvičení na tvrdé podlaze je delší podložka výhodnější než krátká, aby se při převalování nikdy nedostal kus těla mimo ni.</p>'
          '<h2>Overball a gymnastické míče</h2>'
          '<p>Malý míč s průměrem zhruba čtvrt metru se vkládá mezi kolena, pod pánev nebo za záda a cvičení tak zapojuje hluboké svaly. Nafukuje se jen na střední tvrdost, aby zůstal pružný. '
          'Velký gymnastický míč se vybírá podle výšky postavy: při sezení mají být kolena přibližně v pravém úhlu. Příliš malý míč vytváří špatné držení těla a příliš velký znemožňuje dosáhnout na podlahu. Před použitím zkontrolujte, zda míč nepropouští vzduch, a nepoužívejte ho u ostrých předmětů.</p>'
          '<h2>Pilates kruh</h2>'
          '<p>Pružný kruh o průměru zhruba třiceti centimetrů se tiskne dlaněmi, stehny nebo kotníky. Přidává odpor, ale i zpětnou vazbu: když tlačíte proti němu, cítíte, které svaly pracují. '
          'Kruh má měkké madlo a pevný kovový nebo skleněný nosník. Příliš tuhý model je vhodný jen pro pokročilé, začátečníkům stačí měkčí odpor. Při výběru zkontrolujte pevnost spojů a výplň madel, která nemá klouzat v dlani.</p>'
          '<h2>Odporové gumy a pásky</h2>'
          '<p>Gumy se prodávají v několika stupních odporu a často v sadách. Dělí se na ploché pásky, uzavřené smyčky a gumy s madly. Pásky jsou univerzální a vhodné i pro rehabilitaci, smyčky se navlékají kolem kolen a kotníků, gumy s madly se hodí na paže a záda. '
          'Barva odpovídá odporu, ale stupnice se u výrobců liší, takže nepřecházejte mezi značkami naslepo. Gumu před cvičením zkontrolujte, protože prasklina se při napnutí může změnit v trhlinu. Další možnosti najdete v kategorii <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
          '<h2>Válce a automasáž</h2>'
          '<p>Pěnový válec uvolňuje svaly po tréninku a před cvičením zlepšuje pohyblivost. Hladký je jemnější, strukturovaný zasahuje hlouběji. Mírný tlak je v pořádku, ostrá bolest ne. Válec se nepřejíždí přes kloub, ale přes svaly. U zranění, bolestí páteře nebo zdravotních potíží se vyplatí poradit se s lékařem nebo fyzioterapeutem. '
          'K podobnému účelu slouží i míčky na trigger pointy a masážní hůlky.</p>'
          '<h2>Balanční pomůcky</h2>'
          '<p>Nestabilní povrch vyžaduje práci hlubokých stabilizačních svalů. Balanční půlkoule, podložky a kotouče se používají při stoji, dřepech i při cvičení v kleku. Začněte na stabilní podlaze a teprve s jistotou přejděte na nestabilní povrch. '
          'Na Sportece najdete rozšířenou nabídku také v kategorii <a href="/balancni-pomucky/">balanční pomůcky</a>.</p>'
          '<h2>Výběr podle cíle</h2>'
          '<ul><li><strong>Začátek bez zkušeností:</strong> podložka, malý míč a lehká guma. Cvičení najdete ve videích nebo v lekcích u lektora.</li>'
          '<li><strong>Posílení středu těla:</strong> overball, velký míč a podložka s dostatečnou tloušťkou.</li>'
          '<li><strong>Tvarování a odpor:</strong> pilates kruh a gumy různých odporů.</li>'
          '<li><strong>Uvolnění a regenerace:</strong> pěnový válec, masážní míček a měkká podložka. Doplňte o <a href="/jogove-pomucky/">jógové pomůcky</a>.</li>'
          '<li><strong>Cvičení v těhotenství či po úrazu:</strong> vždy po domluvě s lékařem nebo fyzioterapeutem, s omezeným výběrem pomůcek.</li></ul>'
          '<h2>Pilates a návaznost na další cvičení</h2>'
          '<p>Pilates se dobře kombinuje s jógou, během a silovým tréninkem. Díky pilates zlepšíte kontrolu pohybu a držení těla, což pomáhá i v jiných sportech. Pokud se chcete věnovat i jiným aktivitám, prohlédněte si kategorie <a href="/joga-a-pilates/">jóga a pilates</a>, <a href="/fitness/">fitness</a> a <a href="/funkcni-trenink/">funkční trénink</a>. '
          'Pro pohodlí při cvičení se hodí <a href="/leginy/">legíny</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>, ideálně protiskluzové.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku pilates pomůcek mají ' + B(("hms", "HMS"), ("merco", "Merco"), ("insportline", "Insportline"), ("ledragomma", "Ledragomma"), ("lifefit", "Lifefit"), ("sedco", "Sedco"), ("gymbeam", "GymBeam"), ("domyos", "Domyos")) +
          '. Další značky jsou ' + B(("fitforce", "Fitforce"), ("spokey", "Spokey"), ("neolymp", "Neolymp"), ("kubisport", "Kubisport"), ("bodhi", "Bodhi"), ("sportago", "Sportago")) + '. '
          'Ledragomma se soustředí na gymnastické míče, HMS a Merco nabízejí široké sady a Bodhi se věnuje spíše józe. Porovnávejte rozměry a materiál u konkrétního kusu.</p>'
          '<h2>Bezpečnost a péče</h2>'
          '<p>Nejdůležitější je technika, ne rychlost. Pomůcky používejte na rovném a nekluzkém povrchu, míče nafukujte podle návodu a gumy kontrolujte na praskliny. '
          'Podložku čistěte vlhkým hadříkem s jemným mýdlem a sušte ve stínu. Míč uskladněte mimo slunce a ostré předměty. Při bolesti, závratích nebo zdravotních potížích cvičení přerušte a poraďte se s odborníkem.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš tenká podložka, která netlumí tlak na páteř a kostrč.</li>'
          '<li>Velký míč bez ohledu na výšku těla.</li>'
          '<li>Příliš silný odpor od začátku, který vede ke špatné technice.</li>'
          '<li>Nákup velké sady, z níž se nakonec používají jen dva kusy.</li>'
          '<li>Vynechání rozcvičky a protažení.</li></ul>'
          '<p>Při nákupu porovnávejte rozměry, hmotnost a recenze a vyberte si to, co skutečně použijete. Na Sportece uvidíte nabídky obchodů vedle sebe a můžete rychle zjistit, kde se pomůcka vyskytuje v hledaném provedení.</p>',
    faq=[
        ('Jaké pilates pomůcky jsou nejlepší pro začátečníky?', 'Základem je dostatečně silná podložka, malý overball a lehká guma. Další kusy dokupujte podle toho, co ve cvičení opravdu potřebujete.'),
        ('Jak silná má být pilates podložka?', 'Silnější než jógová, aby tlumila tlak na páteř a kostrč při cvičení vleže. Měkký materiál, který se nepropadá, a protiskluzový povrch jsou důležitější než značka.'),
        ('Jakou velikost míče vybrat?', 'Malý míč má obvykle okolo 25 cm. U velkého gymnastického míče se řiďte výškou postavy, aby při sezení kolena svírala přibližně pravý úhel.'),
        ('K čemu je pilates kruh?', 'Pružný kruh přidává odpor při tlaku dlaněmi nebo stehny a pomáhá aktivovat svaly paží, ramen a vnitřních stehen. Hodí se i na cvičení středu těla.'),
        ('Je lepší guma s madly, nebo plochý pásek?', 'Guma s madly se hodí pro cviky na paže a záda, plochý pásek je univerzální a vhodný i pro rehabilitaci. Smyčky se používají hlavně na nohy a hýždě.'),
        ('Může se pilates cvičit i bez pomůcek?', 'Ano, klasické cviky na podložce nepotřebují nic dalšího. Pomůcky přidávají odpor nebo nestabilitu a zpestřují cvičení.'),
        ('Je pěnový válec vhodný pro každého?', 'Obecně se hodí k uvolnění svalů, ale při bolesti páteře, zranění nebo zdravotních problémech je lepší poradit se s lékařem nebo fyzioterapeutem.'),
        ('Jak poznám, že je guma opotřebovaná?', 'Objeví se drobné praskliny, ztráta pružnosti nebo lepivý povrch. Opotřebovanou gumu vyměňte, protože se při napnutí může přetrhnout.'),
        ('Jak pomůcky čistit?', 'Otřete je vlhkým hadříkem s jemným mýdlem a nechte uschnout mimo přímé slunce. Agresivní chemie může poškodit povrch a guma pak ztvrdne.'),
        ('Hodí se pilates pomůcky pro děti?', 'Míče a podložky se používají i při hrách a pohybových aktivitách dětí, ale vždy pod dohledem dospělých. Pro dlouhodobější cvičení doporučujeme lektora s dětskou praxí.'),
    ])

# ------------------------------------------------------------------ cyklo-zamky
NEW['cyklo-zamky'] = dict(long=True,
    title='Zámky na kolo: U-zámky, řetězy a skládací',
    desc='Zámky na kolo: U-zámky, řetězové, skládací, lankové a zámky na kola i elektrokola. Jak vybrat délku, odolnost a upevnění a porovnat obchody.',
    intro='<p>Žádný zámek není nezničitelný, ale dobrý zámek zlodějům prodlouží práci a odradí je od cesty nejmenšího odporu. Většina krádeží využívá situaci, kdy je kolo připevněno slabým lankem nebo kdy zámek není správně použit. '
          'Správný zámek se vybírá podle toho, kde kolo zamykáte, jak dlouho tam zůstává a jak vzácné je. Do města na celý den se hodí těžký U-zámek nebo masivní řetěz, na krátké zastávky u obchodu lehčí model.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Rockbros, Axa, Kryptonite, Abus, Master Lock, Force, Hiplok nebo Author. '
          'K tématu patří <a href="/jizdni-kola/">jízdní kola</a>, <a href="/elektrokola/">elektrokola</a>, <a href="/cyklo-svetla/">světla</a> a <a href="/cyklisticke-helmy/">helmy</a>. '
          'Níže najdete přehled typů zámků, zásady zamykání a výběr podle prostředí.</p>',
    guide='<h2>Typy zámků</h2>'
          + T(['Typ', 'Výhody', 'Nevýhody'], [
              ['U-zámek (třmen)', 'tuhý, pevný, dobrý poměr ochrany a váhy', 'omezená délka, nutné správně upevnit na rámu'],
              ['Řetězový zámek', 'flexibilní, lze obtočit různé objekty', 'těžký, vysoká ochrana je těžká'],
              ['Skládací zámek', 'kompaktní, pohodlný transport', 'více kloubů, menší ochrana než plný třmen'],
              ['Lankový zámek', 'lehký, snadný', 'nejnižší ochrana, jen na krátké zastavení'],
              ['Zámek na zadní kolo (rámový)', 'rychlé zajištění, nemusí se nic vázat', 'kolo se neposune, ale lze odnést'],
              ['Alarmový a chytrý zámek', 'hlasité upozornění, někdy i lokalizace', 'cena i závislost na baterii']]) +
          '<p>Žádný z typů nevyhrává ve všech ohledech. Pevnost se odvíjí od průměru kovu a kvality zámku, flexibilita od konstrukce a váha od materiálu. Praktické je kombinovat dva různé typy zámků, protože zloděj potřebuje jiný nástroj na každý z nich.</p>'
          '<h2>Co rozhoduje o odolnosti</h2>'
          '<p>Důležitý je průměr třmenu nebo článku řetězu, tvrdost kalené oceli a konstrukce uzávěru. Slabým místem bývá zámek samotný, nikoli kov kolem. Značky obvykle uvádějí hodnocení odolnosti ve stupnici, ale ta se mezi výrobci liší, proto ji berte jen jako orientační a nespoléhejte na slib bezpečnosti. '
          'Důležité jsou také vložka, ochrana proti vrtání a pouzdro, které chrání zámek před nečistotami a vodou.</p>'
          '<h3>Vložka a klíč</h3>'
          '<p>Většina zámků se otevírá klíčem. Kvalitní vložka je odolná proti vyvrtání a proti páčení. Dodávané klíče bývají kódovány a značkové zámky je nabízejí i s registrací pro náhradu. Zámky na kód jsou pohodlné, ale kombinace se dá odpozorovat, takže ji nikdy nenechávejte na ukázkové hodnotě. Při zimních teplotách se vložka někdy zasekává, pomáhá speciální mazivo.</p>'
          '<h3>Délka a velikost</h3>'
          '<p>Velký třmen se snadněji připojí k pevnému předmětu, ale vyplňuje volný prostor a zloději pak mají lepší místo pro páčení. Menší třmen se hodí ke kolu zamčenému na stojan. Naopak řetěz nabídne větší dosah, ale váží víc. Zvažte, zda potřebujete zamknout i kola a rám, nebo jen rám a zadní kolo.</p>'
          '<h2>Jak správně zamykat</h2>'
          '<ul><li>Vždy provlečte zámek rámem a připevněte k pevnému předmětu, ne jen ke kolu.</li>'
          '<li>Zámek držte nad zemí. Při pokládce na zem je snazší ho rozbít.</li>'
          '<li>Využijte co nejmenší volný prostor, aby se do něj nevešly nástroje.</li>'
          '<li>Zamykejte zadní kolo i rám. Vyjímatelná kola zajistěte zvlášť, nebo je vezměte s sebou.</li>'
          '<li>Pevný stojan nebo pevný sloup, který nelze rozebrat ani přeřezat, je nutné. Nezamykejte ke stromečku nebo k lehkému plotu.</li>'
          '<li>Pomocí druhého zámku zajistěte přední kolo, jestli je vyjímatelné.</li></ul>'
          '<h2>Výběr podle prostředí</h2>'
          + T(['Situace', 'Doporučení', 'Poznámka'], [
              ['Krátká zastávka u obchodu', 'lehčí skládací nebo lankový zámek', 'jen na dohled'],
              ['Celodenní parkování ve městě', 'masivní U-zámek nebo řetěz', 'vždy k pevnému stojanu'],
              ['Noc venku, sídliště', 'kombinace dvou zámků, nejlépe třmen a řetěz', 'raději do sklepa nebo kolárny'],
              ['Elektrokolo a drahé kolo', 'nejtěžší zámek a doplňkový zámek', 'baterii při parkování vyjměte'],
              ['Cestování a kempování', 'lehčí zámek s alarmem a dohled', 'ne nechávat kolo bez dozoru'],
              ['Dětské kolo', 'lanko nebo skládací zámek', 'dítě se zámkem naučit zacházet']]) +
          '<h2>Elektrokola a drahá kola</h2>'
          '<p>Elektrokola jsou těžká a lákavá, takže vyžadují vyšší úroveň zabezpečení. Zámek bývá dražší než u klasického kola, a přesto stojí za to, protože hodnota kola je mnohonásobně vyšší. '
          'Vyjmutelnou baterii i displej berte s sebou. Zvažte také možnost lokátoru GPS ukrytého v rámu. <a href="/elektrokola/">Elektrokolo</a> zamykejte vždy za rám k pevnému předmětu; <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a> sundejte spolu s baterií, pokud to konstrukce dovoluje.</p>'
          '<h2>Skladování a doprava zámku</h2>'
          '<p>Zámek se dá nosit v držáku na rámu, v brašně, v batohu nebo kolem sedlové trubky. Těžké zámky snadno zahltí batoh, takže pomáhá speciální držák s rychlým uvolněním. Řetěz s textilním návlekem nepoškrábe lak. Vyberte způsob, který nebudete nechávat doma, protože zámek, který u sebe nemáte, nechrání nic. '
          'Pro nosiče použijte <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>, pro dopravu na auto <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>, kde se kolo zamyká přímo k nosiči.</p>'
          '<h2>Další zabezpečení</h2>'
          '<p>Zámek je jen jedna vrstva. Označení rámu gravírováním nebo registrací usnadní vrácení při nálezu. '
          'Na rizikovějších místech parkujte na osvětleném místě s kamerami a v blízkosti lidí. Odnímatelné součásti, jako jsou <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-computery/">cyklopočítače</a> a rychloupínáky, se vyplatí vzít s sebou.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(("rockbros", "Rockbros"), ("axa", "Axa"), ("kryptonite", "Kryptonite"), ("abus", "Abus"), ("master-lock", "Master Lock"), ("force", "Force"), ("hiplok", "Hiplok"), ("author", "Author")) +
          '. Další jsou ' + B(("onguard", "Onguard"), ("max1", "Max1"), ("m-wave", "M-Wave"), ("sekura", "Sekura"), ("stahlex", "Stahlex"), ("nexelo", "Nexelo")) + '. '
          'Kryptonite, Abus a Hiplok se soustředí na bezpečnostní modely pro město, Axa a Onguard na praktické zámky na rám a Force a Author nabízejí cenově přívětivější řešení. Při porovnání se dívejte na konstrukci, ne na značku.</p>'
          '<h2>Údržba zámku</h2>'
          '<p>Vložku občas ošetřete speciálním olejem na zámky, aby se klíč neseknul, a třmen otřete suchým hadříkem. Zamrzlý zámek nelijte horkou vodou, ale ohřejte teplým vzduchem nebo rukama. Chraňte ho před pískem a bahnem. '
          'Zkontrolujte, zda se na kovu neobjevila koroze a zda se uzávěr zavírá bez odporu. Ztracený klíč vám výrobce často vymění po registraci, proto si uchovejte registrační kartu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Zamykání jen kola, ne rámu. Zloděj kolo odšroubuje a rám odnese.</li>'
          '<li>Lehký zámek na celý den na rizikovém místě.</li>'
          '<li>Zámek položený na zemi, který se dá snadno rozbít.</li>'
          '<li>Pevný bod, který se dá snadno rozebrat nebo přeřezat.</li>'
          '<li>Nechané světlo, počítač nebo baterie na zaparkovaném kole.</li></ul>'
          '<p>Na Sportece vidíte nabídky obchodů vedle sebe a při porovnání se můžete soustředit na rozměry, hmotnost a typ zamykání. Pro úplné vybavení se podívejte na <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a> a <a href="/cyklistika/">cyklistiku</a>.</p>',
    faq=[
        ('Jaký zámek je nejlepší na kolo?', 'Nejlepší je ten, který odpovídá místu a době parkování. Pro celodenní městský provoz se hodí masivní U-zámek nebo silný řetěz, pro krátkou zastávku stačí lehčí skládací zámek.'),
        ('Je U-zámek bezpečnější než řetěz?', 'Záleží na konkrétním modelu. U-zámek bývá při stejné hmotnosti tužší, řetěz je flexibilnější a umožní zamknout složitější objekty. Kvalita ocele a zámku rozhoduje víc než typ.'),
        ('Je lankový zámek dostatečný?', 'Lanko je nejslabší varianta a hodí se jen na velmi krátké zastavení v klidném prostředí. Pro dlouhé parkování volte tvrdší zámek.'),
        ('Má smysl používat dva zámky?', 'Ano, zloděj pak potřebuje dva různé nástroje a více času. Dobrá kombinace je třmen na rám a zadní kolo a doplňkový zámek nebo lanko na přední kolo.'),
        ('Kam kolo zamykat?', 'K pevnému stojanu nebo sloupu, který nelze rozebrat ani přeřezat. Zámek provlečte rámem a pokud možno i zadním kolem.'),
        ('Jak chránit elektrokolo?', 'Používejte nejtěžší zámek, doplňkový zámek na kolo a vyjímejte baterii i displej. Kolo parkujte na viditelném a osvětleném místě nebo v uzamčené místnosti.'),
        ('Jaký zámek vybrat pro dětské kolo?', 'Pro dětské kolo obvykle stačí lehký skládací nebo lankový zámek. Důležité je, aby ho dítě zvládlo samo zamknout a odemknout.'),
        ('Jak přenášet těžký zámek?', 'Pomůže držák na rám, brašna na nosič nebo opasek. Tak se nemusí nosit v batohu a zůstane po ruce, když ho potřebujete.'),
        ('Co dělat, když zámek zamrzne?', 'Zahřejte ho teplým vzduchem nebo v dlaních a použijte speciální rozmrazovač na zámky. Nepoužívejte horkou vodu, která později zamrzne znovu.'),
        ('Pomáhá registrace a gravírování rámu?', 'Zlodějům neubrání, ale pomáhá s vrácením nalezeného kola. Uložte si sériové číslo rámu, fotografie a doklad o koupi, které se hodí při hlášení policii.'),
    ])

# ------------------------------------------------------------------ extensions (extra guide sections)
NEW['neopreny']['guide'] += (
    '<h2>Jak neopren obléknout a svléknout</h2>'
    '<p>Oblek se nasazuje pomalu, od chodidel a nohou vzhůru, a nikdy se netahá za látku silou, protože by se mohly utrhnout švy. Nehty si zastřihněte a sundejte prsteny. Vlhký nebo lehce namočený oblek se oblékne snáz, zatímco suchý na kůži drhne. '
    'Někdo si na chodidla a ruce navlékne igelitový sáček, po kterém materiál hladce sklouzne. Při svlékání se oblek stahuje z ramen a obrací naruby, podobně jako se svléká ponožka.</p>'
    '<h2>Kdy zvolit jiný typ ochrany</h2>'
    '<p>Pokud se chystáte jen na krátké koupání v mírně vlažné vodě, oblek nepotřebujete. Pro sluneční záření a otěr stačí lycra, při chladném větru nad hladinou pomůže vodoodolná bunda. Neopren se nehodí do horkých dní mimo vodu, protože v něm tělo rychle přehřeje. '
    'Při dlouhém pobytu v chladné vodě mějte po ruce suché oblečení a teplý nápoj. Prochladnutí se projevuje třesem, nejistými pohyby a ztrátou citu v prstech, a v takové chvíli je správné vodu opustit.</p>')

NEW['sportovni-spodni-pradlo']['guide'] += (
    '<h2>Sezónní rozdíly</h2>'
    '<p>V létě je cílem odvést pot a nechat kůži dýchat, proto se hodí lehké, vzdušné a světlé materiály. V zimě naopak záleží na tom, aby spodní vrstva zůstala u těla a nebyla příliš objemná, aby se nad ní vešla další vrstva. '
    'Nejčastější chybou je zimní prádlo, které je příliš tlusté a po prvním potu vychladne. Při přechodném počasí se osvědčila lehká vlna nebo jemná syntetika, která zvládne rozdíl mezi chladným ránem a teplým polednem.</p>'
    '<h2>Na co si dát pozor u levných kusů</h2>'
    '<p>Levné sady často mívají zdrsněné švy, štítky vyšité přímo do prádla a gumu v pase, která po několika pracích ztratí pružnost. Zkuste si ohmatat vnitřní stranu a zkontrolovat, zda se štítek dá odstřihnout. '
    'Pokud plánujete spodní prádlo používat při sportu pravidelně, vyplatí se investovat do kvalitnějších kusů, protože se tolik nepohybují a lépe vydrží praní. Výhodné jsou i sady po třech nebo pěti kusech, které umožní střídat prádlo bez čekání na vyprání.</p>'
    '<h2>Zápach a hygiena</h2>'
    '<p>Zápach vzniká činností bakterií na potu, který ulpívá ve vláknech. Syntetika ho zadržuje víc než vlna, ale oba materiály se dají vyčistit pravidelným praním. Nenechávejte vlhké prádlo zabalené v tašce, ale po tréninku ho rozprostřete. '
    'Pokud zápach zůstává i po vyprání, pomůže namočení ve vodě s malým množstvím octa nebo speciálním sportovním prostředkem. Prádlo vyměňujte po každém sportovním výkonu, i když se zdá být suché.</p>'
    '<h2>Prádlo pro aktivní denní nošení</h2>'
    '<p>Mnoho lidí nosí sportovní prádlo celý den, například při práci vstoje, v dlouhých cestách nebo při pobytu venku. Pomáhá udržet kůži v suchu a snižuje tření, které při pohybu vzniká. Hodí se i pro lidi s citlivou pokožkou, pokud zvolí hladký materiál bez silných švů. '
    'U dlouhých cest autem nebo letadlem oceníte prodyšný střih, který nepřidává další vlhkost.</p>')

NEW['pilates-pomucky']['guide'] += (
    '<h2>Jak často a jak dlouho cvičit</h2>'
    '<p>Pilates nevyžaduje dlouhé hodiny. Pravidelná krátká sezení, například dvacet až třicet minut několikrát týdně, mají větší smysl než jednorázový maraton. Začněte základními cviky na podložce a pomůcky přidávejte, až zvládnete správné držení těla a dýchání. '
    'Každý cvik provádějte pomalu a soustředěně, protože kvalita pohybu je důležitější než počet opakování. Pokud nemáte jistotu v technice, vyplatí se několik lekcí s certifikovaným lektorem, protože chyby se obtížně opravují bez zpětné vazby.</p>'
    '<h2>Příklady jednoduchých cviků</h2>'
    '<ul><li><strong>Most s míčem mezi koleny:</strong> leh na zádech, míč mezi koleny, zvedání pánve po jednotlivých obratlích.</li>'
    '<li><strong>Stovka s kruhem:</strong> kruh v rukou a drobné pohyby paží při klidném dýchání.</li>'
    '<li><strong>Boční leh s gumou:</strong> smyčka kolem kolen a zvedání horní nohy.</li>'
    '<li><strong>Roll-up s pomocí pásku:</strong> kontrolované posazování a pokládání páteře.</li>'
    '<li><strong>Uvolnění zad na válci:</strong> pomalé pojíždění po horní části zad s oporou rukou za hlavou.</li></ul>'
    '<p>Jde pouze o obecnou inspiraci. Přesné provedení najdete u lektora, v knize nebo v ověřeném video kurzu.</p>'
    '<h2>Kde cvičit a kolik místa potřebujete</h2>'
    '<p>Stačí volná plocha o velikosti podložky a prostor na natažení paží a nohou. Podlaha má být rovná a nekluzká, ideálně bez koberce s dlouhým vlasem. Před cvičením zkontrolujte, že v okolí nejsou ostré rohy nábytku. '
    'Pomůcky se dají uskladnit do krabice pod postel nebo do skříně, protože většina z nich je lehká a skladná. Pokud nemáte doma místo, vyberte skládací nebo nafukovací kusy.</p>')

NEW['cyklo-zamky']['guide'] += (
    '<h2>Zámek na zadní kolo a rámové zámky</h2>'
    '<p>Rámový zámek se připevňuje k zadní vidlici a po zavření zablokuje kolo, takže se s kolem nedá odjet. Je rychlý a hodí se na krátké zastávky, například u obchodu. Nezabrání ale tomu, aby někdo kolo odnesl, proto se často kombinuje s řetězem nebo lankem, které prochází rámem a pevným objektem. '
    'Existují modely, které jdou na rám připojit dalším lankem nebo řetězem a tvoří tak univerzální řešení pro město.</p>'
    '<h2>Alarmové a chytré zámky</h2>'
    '<p>Alarmový zámek při dotyku nebo nárazu spustí hlasitou sirénu. Pomáhá odradit zloděje a upozornit okolí, ale nenahrazuje pevnost samotného zámku. Chytré zámky se spojují s telefonem a umožňují odemykání bez klíče, někdy i sledování polohy. '
    'Předpokladem je pravidelné nabíjení nebo výměna baterií, jinak se v nejméně vhodnou chvíli nemusí odemknout. Pro klasickou jízdu do práce často stačí pevný mechanický zámek bez elektroniky.</p>'
    '<h2>Doprava zámku a ochrana laku</h2>'
    '<p>Kovový třmen i řetěz mohou při přepravě poškrábat rám a přerušit lak. Hodí se textilní nebo gumový návlek, který se nasazuje přes řetěz, a pryžová ochrana na třmen. '
    'Těžký zámek bývá lepší nosit v držáku nebo brašně připevněné na nosiči, protože zadní kapsa batohu zatěžuje záda. Pokud máte zámek v batohu, mějte jej uložený tak, aby se klíč nedal ztratit.</p>'
    '<h2>Doma, ve sklepě a v bytovém domě</h2>'
    '<p>I zamčený sklep nebo kolárna je cílem krádeží, proto se i tam vyplatí kolo zamknout k pevnému stojanu. Zvažte kotvu přišroubovanou do zdi nebo podlahy, ke které se zámek připojí. '
    'V bytě je dobré kolo uložit tak, aby ho nebylo vidět z okna nebo z chodby. Pro ochranu před zlodějem využijte pojistku nebo pojištění domácnosti, které může krádež kola zahrnovat. Podmínky se u pojišťoven liší, proto je vždy ověřte přímo ve smlouvě.</p>')

NEW['sportovni-spodni-pradlo']['guide'] += (
    '<h2>Jak poznat kvalitní zpracování</h2>'
    '<p>Při nákupu si prohlédněte lem nohavic a pasu: silikonový proužek nebo široká guma drží prádlo na místě a neřeže. Zkontrolujte rozkrokový díl, který by měl mít plochý šev, a materiál v místech nejvyššího tření. '
    'Rovnoměrné prošití bez uvolněných nití signalizuje pečlivou výrobu. Dobrý kus po natažení rychle vrací tvar a po vyprání se nevytahuje do pytlovitých kolen nebo boků. Pokud štítek nepíše složení, zbystřete, protože u sportovního prádla je procento elastanu důležitá informace.</p>'
    '<h2>Prádlo na cesty a do batohu</h2>'
    '<p>Na vícedenní výlety se hodí lehké kusy, které zabírají málo místa a po vyprání v umyvadle rychle schnou. Dva až tři páry na střídání stačí i na týden, pokud je večer vyperete a rozložíte. '
    'Merino prádlo vydrží nošení déle bez zápachu, což ocení ti, kdo cestují nalehko. Syntetické kusy jsou lehčí a schnou rychleji, ale nejsou tak odolné vůči pachu. Podle délky cesty vybírejte kombinaci obou.</p>')

NEW['pilates-pomucky']['guide'] += (
    '<h2>Kolik utratit a co nekupovat</h2>'
    '<p>Pro začátek stačí základní sada a nemá smysl hned pořizovat všechny typy pomůcek. Z drahých přístrojů a velkých sestav nejprve vyzkoušejte jen to, co skutečně použijete: podložku, malý míč a gumové pásy obvykle pokryjí první měsíce. Důležitější než počet pomůcek je pravidelnost a správné provedení. '
    'Rozhodnutí o dalších kusech si nechte, dokud nezjistíte, které cviky vás baví. Pokud cvičíte ve skupině nebo ve studiu, zjistěte u lektora, jaké pomůcky se při hodinách používají, a pořiďte si stejné.</p>'
    '<h2>Pilates a cvičení v práci či na cestách</h2>'
    '<p>Malé pomůcky, jako je guma, masážní míček nebo skládací kruh, se vejdou do tašky a umožní krátké cvičení i mimo domov. Na služební cestě nebo na dovolené stačí ručník místo podložky a gumová smyčka k posílení. '
    'Pravidelné drobné protažení během dne pomáhá proti ztuhlosti od dlouhého sezení. Jde o obecnou radu, a pokud máte potíže se zády nebo klouby, poraďte se s lékařem či fyzioterapeutem.</p>')

NEW['cyklo-zamky']['guide'] += (
    '<h2>Pojištění a záznam o kole</h2>'
    '<p>Některé pojistky domácnosti kryjí krádež kola jen při splnění podmínek, například při použití schváleného zámku nebo pouze v uzamčeném prostoru. Podmínky se liší, proto je vždy ověřte ve smlouvě a u pojišťovny. '
    'Uložte si fotografie kola ze všech stran, sériové číslo rámu a detailní snímky nezaměnitelných prvků. Při krádeži urychlí hlášení policii a usnadní případné vrácení.</p>'
    '<h2>Zámek a zimní podmínky</h2>'
    '<p>V mrazu a v soli ze silnic zámky trpí. Vložka může zamrznout, třmen zkorodovat a mechanismus ztuhnout. Po zimě proto zámek očistěte, promažte vložku speciálním olejem a zkontrolujte, zda se klíč otáčí lehce. '
    'Pokud kolo používáte celoročně, vybírejte zámek s krytkou vložky a lakovanou nebo plastem potaženou ocelí, která lépe odolává vlhku.</p>')
