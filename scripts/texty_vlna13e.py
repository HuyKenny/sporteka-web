"""sporteka.cz — wave 13e (4. 11. 2026): long texts (>= 1650 words) for funkcni-tricka, tilka, rybarske-pruty, sportovni-tasky.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ funkcni-tricka
NEW['funkcni-tricka'] = dict(long=True,
    title='Funkční trička: běh, kolo, fitness, hory | Sporteka',
    desc='Funkční trička pro muže, ženy i děti. Průvodce materiály, střihem, vrstvením a péčí a porovnání nabídek českých e-shopů na jednom místě.',
    intro='<p><strong>Funkční tričko</strong> je oblečení, které se stará o to, co se děje mezi kůží a okolním vzduchem. Odvádí vlhkost z povrchu těla, rychle schne a při pohybu nepřilne k zádům jako mokrá bavlna. Právě proto je základní součástí výbavy běžců, cyklistů, turistů i lidí, kteří chodí cvičit pod střechu.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů u triček z polyesteru, polyamidu, směsí s elastanem i vlny. Pro příbuzné kusy se podívejte na <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/merino-tricka/">merino trička</a> nebo <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>. Níže najdete pomůcku, jak vybrat správný materiál, střih a velikost, včetně rad pro děti, péči i okamžik, kdy je čas tričko vyměnit.</p>',
    guide='<h2>Co dělá tričko funkčním</h2>'
          '<p>Funkční tričko nevyniká tím, že by mělo nějaký tajný přídavek, ale tím, že jeho vlákna nenasáknou vodu. Syntetické vlákno vlhkost nepohltí, ale rozvede ji po povrchu látky, kde se rychle odpaří. Bavlna naopak vodu zadrží uvnitř vlákna, ztěžkne a po zastavení chladí. Při chůzi po rovině je rozdíl malý, při běhu, jízdě na kole nebo výstupu do kopce je znát velmi rychle.</p>'
          '<p>Druhou vlastností je tvar. Funkční trička se šijí s ohledem na pohyb: rukávy bývají vykrojené tak, aby se při předpažení nezvedal lem, záda jsou delší než přední část a švy jsou mimo místa, kde se tkanina tře o popruhy batohu. Proto se funkční tričko v obchodě často zdá nezvykle hladké a lehké, a přitom ve sportu funguje lépe než na pohled hezčí běžné triko.</p>'
          '<h2>Materiály a jejich chování</h2>'
          + T(['Materiál', 'Silné stránky', 'Slabší stránky'], [
              ['Polyester', 'schne nejrychleji, lehký, drží barvu i tvar', 'více se v něm drží pach'],
              ['Polyamid (nylon)', 'hladký na dotek, odolný proti oděru', 'schne o něco pomaleji než polyester'],
              ['Elastan ve směsi', 'pružnost a přiléhavost, nemačká se', 'v samotné podobě nevhodný, tvoří jen malou část'],
              ['Merino vlna', 'zvládne širší rozsah teplot a pachu se drží méně', 'pomaleji schne, citlivější na hrubé praní'],
              ['Viskóza z bambusu nebo eukalyptu', 'měkká a hebká na kůži', 'méně odolná při opakovaném zatížení']]) +
          '<p>Většina triček na trhu je směs. Na štítku zkontrolujte, zda převažuje polyester nebo polyamid, a zda je přidáno pár procent elastanu. Pokud je v nabídce tričko z přírodní vlny, přejděte do kategorie <a href="/merino-tricka/">merino trička</a>, kde se vlna podrobně porovnává. Pro nošení pod bundou na zimu pak slouží <a href="/termopradlo/">termoprádlo</a>, které je tenčí a přiléhavější než klasické funkční triko.</p>'
          '<h2>Výběr podle sportu</h2>'
          '<h3>Běh a atletika</h3>'
          '<p>Běžecké tričko je lehké, s plochými švy a často s vzdušnými síťovanými zónami na zádech a pod podpažím. Délka rukávu se řídí sezónou. V létě stačí krátký, na jaře a na podzim se hodí dlouhý rukáv, který se dá vyhrnout. Za šera hledejte reflexní prvky na zádech a na hrudi. Pro nízké teploty doplňte tričko o <a href="/funkcni-mikiny/">funkční mikinu</a> nebo lehkou vestu a v dešti o <a href="/nepromokave-bundy/">nepromokavou bundu</a>. Při běhu v terénu se hodí <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, takže vybírejte tričko bez tlustých švů na ramenou.</p>'
          '<h3>Cyklistika</h3>'
          '<p>Cyklistický dres má delší záda, kapsy na zádech a často zip na hrudi pro větrání. Pokud nechcete investovat do speciálního dresu, vystačí si rekreační cyklista s přiléhavým funkčním tričkem, jen je dobré vybrat takové bez objemných švů v místě popruhů batohu. Odborné kusy najdete v kategoriích <a href="/cyklisticke-dresy/">cyklistické dresy</a> a <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>'
          '<h3>Fitness a posilovna</h3>'
          '<p>V hale není důležitý vítr, ale vedro. Vyberte materiál, který se po zpocení nelepí k tělu, a volnější střih tam, kde potřebujete hluboké dřepy a tahy. Při cvičení na zemi se hodí tričko, které při předklonu nesjede přes hlavu. Aktivity v hale doplníte kategoriemi <a href="/fitness/">fitness</a> a <a href="/funkcni-trenink/">funkční trénink</a>.</p>'
          '<h3>Turistika a outdoor</h3>'
          '<p>Při chůzi s batohem si dejte pozor na tření popruhů o ramena. Tenká látka se může na zádech otírat, proto je rozumné zvolit tričko s hladším povrchem a ploššími švy. V horách přibalte vždy alespoň jednu vrstvu navíc, protože propocené tričko po zastavení chladí. Související kategorie jsou <a href="/outdoor/">outdoor</a> a <a href="/trekova-obuv/">trekové boty</a>.</p>'
          '<h3>Zimní sporty a běžky</h3>'
          '<p>V zimě slouží funkční tričko jako první vrstva pod fleece nebo softshell. Na běžkách se hodí tenčí, přiléhavé a prodyšné, aby se při intenzivní práci pot rychle odvedl. Tepelný komfort pak zajišťují vrstvy navrch. Související kategorie najdete u <a href="/bezecke-lyzovani/">běžeckého lyžování</a> a <a href="/lyzarske-termopradlo/">lyžařského termoprádla</a>.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Stejná velikost M se u různých značek liší, proto vždy porovnejte tabulku výrobce s vlastními rozměry. Měřte obvod hrudníku a délku trupu a porovnejte je s hodnotami v tabulce. Na sport volte přiléhavější střih, který se přes tělo neshrnuje. Na volný čas stačí volnější. Pokud jste na hraně mezi dvěma velikostmi, vyberte menší u elastických materiálů a větší u pevných.</p>'
          + T(['Střih', 'Popis', 'Pro koho'], [
              ['Přiléhavý (slim, fitted)', 'těsně obepíná tělo, minimální záhyby', 'běh, kolo, první vrstva v zimě'],
              ['Regular', 'mírný odstup od těla, volný pohyb', 'fitness, turistika, týmové sporty'],
              ['Volný (relaxed, oversized)', 'viditelně širší, měkký spád', 'volný čas, jóga, posilovna'],
              ['Dámský střih', 'užší v pase, kratší v rukávu, tvarovaný průramek', 'ženy všech sportů'],
              ['Dětský střih', 'jednodušší, měkké švy, někdy delší záda', 'školní tělocvik, kroužky, výlety']]) +
          '<h2>Pachové a UV úpravy</h2>'
          '<p>Polyester se po delším používání může stát pachově zatíženým. Výrobci proto přidávají antibakteriální úpravy, často na bázi stříbra nebo zinku. Ty zpomalují množení bakterií, ale nenahradí praní. U UV triček je rozdíl v hustotě pletiva: čím hustší látka, tím méně slunečního záření projde. Pro děti u vody a pro delší pobyt na slunci se používají lycra trička, kterým se věnuje kategorie <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>.</p>'
          '<h2>Jak o funkční tričko pečovat</h2>'
          '<p>Funkční materiál se dá poškodit nevhodným praním. Perte na 30 až 40 °C v pračce nebo ručně, ideálně naruby. Nepoužívejte aviváž, protože se usazuje na vláknech a zhoršuje odvod potu. Chlorové bělidlo nahrazuje ocet nebo sportovní prací přípravek. Sušte na šňůře, nikoli na topení, a nežehlete, protože teplo zdeformuje vlákno a poškodí potisk.</p>'
          '<ul><li>Sportovní tričko po použití nenechávejte v tašce přes noc, bakterie se množí ve vlhku.</li>'
          '<li>Perte odděleně od oblečení s suchým zipem, který vlákno natahuje.</li>'
          '<li>Nepoužívejte sušičku na vysokou teplotu, hlavně u triček s potiskem.</li>'
          '<li>Při žmolkování pomůže odžmolkovač, ale po čase je vhodné tričko vyměnit.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Bavlněné tričko na běh.</strong> Na kratší procházku nevadí, při delším pohybu však klade zbytečný odpor.</li>'
          '<li><strong>Příliš velká velikost.</strong> Volné tričko se nepřilepí na kůži a vlhkost se z těla neodvádí.</li>'
          '<li><strong>Vícevrstvé oblečení bez základu.</strong> Fleece nebo bunda přes bavlněné triko vlhkost uzavře.</li>'
          '<li><strong>Zapomenutá sezóna.</strong> V zimě se vyplatí tenčí tričko a teplé vrstvy, v létě vzdušné tričko a světlé barvy.</li>'
          '<li><strong>Nezkontrolované švy.</strong> Vadí hlavně u dlouhých tras s batohem.</li></ul>'
          '<h2>Značky a jejich zaměření</h2>'
          '<p>V kategorii najdete tisíce kusů od značek jako ' + B(('nike', 'Nike'), ('mizuno', 'Mizuno'), ('adidas', 'Adidas'), ('progress', 'Progress'), ('under-armour', 'Under Armour'), ('craft', 'Craft'), ('klimatex', 'Klimatex'), ('puma', 'Puma'), ('swix', 'Swix'), ('columbia', 'Columbia'), ('dynafit', 'Dynafit'), ('kilpi', 'Kilpi'), ('compressport', 'Compressport')) + '. Nike, Adidas, Puma a Mizuno obvykle nabízejí sportovní střih na běh a trénink. Craft a Swix míří na severské sporty, běžky a vytrvalost. Dynafit a Columbia pracují s horským terénem, Kilpi a Progress nabízejí širší nabídku pro turistiku a rekreační sporty.</p>'
          '<h2>Pro koho jaké tričko</h2>'
          '<p>Začínající běžec ocení jedno univerzální tričko s krátkým rukávem a jedno s dlouhým. Rodina s dětmi se vyplatí zásobit se několika jednoduchými kusy, protože děti trička rychle ničí a vyrůstají z nich. Turista s batohem hledá pevnější materiál a hladké švy, cyklista tričko s delšími zády. Kdo cvičí v hale, nepotřebuje nejlehčí materiál, ale takový, který snese opakované praní. Senioři ocení měkké pletivo bez tlačících štítků a trochu volnější střih.</p>'
          '<h2>Jak kombinovat vrstvy</h2>'
          '<p>Funkční tričko funguje jako první vrstva. Na chladné dny přidejte <a href="/funkcni-mikiny/">funkční mikinu</a> nebo <a href="/fleecove-mikiny/">fleecovou mikinu</a>, pro vítr <a href="/vetrovky/">větrovku</a> a pro déšť <a href="/nepromokave-bundy/">nepromokavou bundu</a>. Dole se hodí <a href="/sportovni-kratasy/">sportovní kraťasy</a> nebo <a href="/leginy/">legíny</a>. Pro vyšší podporu u žen patří pod tričko <a href="/sportovni-podprsenky/">sportovní podprsenka</a>. Ruce a hlavu zahřejete <a href="/cepice-a-celenky/">čepicí</a>, krk <a href="/nakrcniky-a-satky/">nákrčníkem</a>.</p>'
          '<h2>Trička pro děti a mládež</h2>'
          '<p>Dětské funkční tričko řeší jiné problémy než dospělé. Děti se hýbou nárazově, rychle se zahřejí a stejně rychle zchladnou, takže se vyplatí tričko, které schne za pár desítek minut. Hodí se měkké švy bez štítků v zádech, protože děti si na škrábavý štítek stěžují dřív, než by jim vadilo zpocení. Při výběru pro školní tělocvik, kroužky nebo tábory počítejte s tím, že tričko bude často v praní, a vybírejte odolnější pletivo s potiskem, který se neodlupuje. Rezerva na růst by měla být malá, aby nebránila pohybu a odvodu potu.</p>'
          '<h2>Barvy, potisk a viditelnost</h2>'
          '<p>Světlé barvy odrážejí slunce a v horku působí příjemněji, tmavé skryjí pot a skvrny. Výrazné neonové odstíny a reflexní potisky zlepšují viditelnost pro řidiče, proto je ocení běžci a cyklisté, kteří vyráží za šera. Samotný potisk může snížit prodyšnost, hlavně pokud pokrývá velkou plochu hrudi. Při horkém počasí proto upřednostněte tričko s menším potiskem nebo takové, kde je grafika součástí tkaniny.</p>'
          '<h2>Kdy tričko vyměnit</h2>'
          '<p>Funkční tričko nevydrží věčně. Pokud se látka zjevně ztenčila, na zádech se objevují průsvity, elastan povolil nebo se po praní stále drží pach, odvod potu už nebude takový jako dřív. Také odlupující se potisk a roztřepené švy jsou signálem k výměně. Pro pravidelně sportujícího člověka je praktické mít několik kusů a střídat je, takže se každé tričko opotřebuje pomaleji.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Stejné tričko se v různých obchodech liší dostupnými velikostmi, barvami a dopravou. Na Sportece vidíte nabídky vedle sebe a můžete vybírat podle toho, co potřebujete. Před nákupem zkontrolujte složení, střih a tabulku velikostí, podívejte se na pravidla vrácení zboží a při koupi dvou kusů vyberte jeden světlý a jeden tmavý, aby se po praní nemíchaly. Slevy se objevují na konci sezóny, kdy se vyprodávají kolekce, takže se vyplatí sledovat starší modely.</p>',
    faq=[('Čím se funkční tričko liší od bavlněného?', 'Funkční tričko odvádí pot z povrchu pokožky a rychle schne, zatímco bavlna vlhkost nasákne a po zastavení chladí. Při klidné chůzi je rozdíl malý, při intenzivním pohybu nebo v chladu je výrazný.'),
         ('Je lepší polyester, nebo merino?', 'Polyester schne rychleji, lépe snáší časté praní a hodí se na intenzivní sport. Merino se dobře nosí v širším rozsahu teplot a méně zapáchá, ale schne pomaleji. Rozhodněte podle sportu a toho, jak často perete.'),
         ('Proč funkční tričko zapáchá?', 'Polyester dobře váže mastné látky z potu a bakterie se v něm množí. Pomáhá praní hned po použití, sportovní prací prostředek bez aviváže a v případě zatuhlého pachu namočení v octové lázni.'),
         ('Jakou velikost funkčního trička zvolit?', 'Řiďte se tabulkou výrobce a vlastním obvodem hrudníku. Na sport vybírejte přiléhavý střih, který se neshrnuje. Mezi dvěma velikostmi je u elastických látek vhodnější menší, u pevných větší.'),
         ('Hodí se funkční tričko na zimu?', 'Ano, jako první vrstva pod fleece nebo bundu. Na samotné zimní oblečení nestačí, ale spolu s teplou střední vrstvou a vnější ochranou je vhodné. Na velký mráz se používá spíše termoprádlo nebo merino.'),
         ('Smím funkční tričko sušit v sušičce?', 'Nízká teplota většinou nevadí, ale vysoká poškodí elastan a potisk. Bezpečnější je sušení na šňůře při pokojové teplotě. Vždy se řiďte pokyny na štítku.'),
         ('Jaká jsou nejlepší trička na běh?', 'Taková, která jsou lehká, mají ploché švy a vzdušné zóny. V létě krátký rukáv, na jaře a na podzim dlouhý. Za šera hledejte reflexní prvky. Konkrétní model je třeba vybrat podle střihu, který vám sedí.'),
         ('Mohu funkční trička používat i každý den?', 'Ano, je to praktické pro lidi, kteří hodně chodí nebo pracují venku. Syntetické materiály ale hůře dýchají v klidu, proto pro kancelář bývá příjemnější směs s bavlnou nebo viskózou.'),
         ('Jaká jsou trička pro děti?', 'Dětská funkční trička mají měkké švy, často delší záda a odolné pletivo. Při výběru dbejte na pohodlí a rezervu na růst, ale příliš velké tričko se nepřilepí a odvod potu zhorší.'),
         ('Jak poznám kvalitní funkční tričko?', 'Podle rovnoměrného pletiva, plochých švů, pevného lemu a čitelného štítku se složením. Dobré tričko se po praní nevytahuje, nežmolkuje a zachovává tvar i po několika desítkách pracích cyklů.')],
)

# ------------------------------------------------------------------ tilka
NEW['tilka'] = dict(long=True,
    title='Tílka a topy: sportovní, dámská, pánská | Sporteka',
    desc='Sportovní tílka a topy na fitness, běh, kolo i léto. Průvodce střihy, materiály a velikostí, porovnání nabídek českých obchodů na jednom místě.',
    intro='<p><strong>Tílko</strong> je nejvzdušnější vrstva horního dílu oblečení. Nechává ramena a paže volné, takže se hodí do horka, k vodě, do posilovny i na tréninkový běh. Pro ženy existují topy s vyšším nebo nižším krytím, pro muže tílka s hlubokým průramkem nebo klasické sportovní střihy.</p>'
          '<p>Na Sportece porovnáte tílka od značek Adidas, Nike, Joma, Under Armour a dalších. Pro chladnější dny se podívejte na <a href="/sportovni-tricka/">sportovní trička</a> nebo <a href="/funkcni-tricka/">funkční trička</a>. Níže najdete, jak vybrat materiál, střih a velikost i jak předejít tření a otěrům při delším pohybu a jak tílko využít i mimo sport, například na dovolené, u vody nebo pod košilí či lehkým svetrem.</p>',
    guide='<h2>K čemu se tílka nosí</h2>'
          '<p>Tílko není jen letní oblečení. Ve sportu má konkrétní úkol: uvolňuje horní část těla a umožňuje chlazení v místech, kde se nejvíc potíme. Lidé, kteří posilují, ocení volné rameno, které nebrání pohybu. Běžci zase tílko oceňují v teplých dnech, kdy je každé zbytečné množství látky na škodu. Mimo sport slouží jako vrstva pod košili, mikinu či lehkou bundu.</p>'
          '<p>V týmových sportech slouží jako dresy, například u basketbalu nebo atletiky. V kategorii <a href="/dresy/">dresy</a> najdete týmová oblečení, zde se soustředíme na tílka pro volný trénink a běžné nošení.</p>'
          '<h2>Střihy a typy tílek</h2>'
          + T(['Typ', 'Charakteristika', 'Typické použití'], [
              ['Klasické tílko', 'úzká ramínka, rovný střih', 'léto, volný čas, běh v teple'],
              ['Pánské posilovací tílko', 'hluboký průramek, volný střih', 'posilovna, crossfit'],
              ['Dresové tílko', 'široký průramek, delší střih, často potisk', 'basketbal, atletika, týmové hry'],
              ['Crop top', 'zkrácená délka nad pasem', 'fitness, jóga, léto'],
              ['Sportovní top', 'tvarovaný střih, často s vestavěnou podporou', 'běh, tanec, aerobik'],
              ['Tílko s integrovanou podprsenkou', 'vnitřní elastická vrstva', 'cvičení bez další vrstvy'],
              ['Dětské tílko', 'měkké švy, jednoduchý střih', 'léto, tábory, sportovní kroužky']]) +
          '<p>Pro ženy, které potřebují víc podpory, platí, že top s vestavěnou podprsenkou je jen kompromis. Pro intenzivní pohyb je vhodnější samostatná <a href="/sportovni-podprsenky/">sportovní podprsenka</a> s tílkem navrch. Pro běžné cvičení a jógu ale často stačí top s lehkou podporou.</p>'
          '<h2>Materiály</h2>'
          '<ul><li><strong>Polyester</strong> je nejrozšířenější. Schne rychle, je lehký a barevně stálý.</li>'
          '<li><strong>Polyamid</strong> je hladký a odolnější proti oděru, často v dámských topech.</li>'
          '<li><strong>Elastan</strong> dodává pružnost a držení tvaru, v malém podílu je prakticky ve všech topech.</li>'
          '<li><strong>Bavlna</strong> je příjemná na dotek a vhodná na volný čas. Při intenzivním potu ale nasákne.</li>'
          '<li><strong>Merino</strong> funguje v širokém rozsahu teplot a méně zapáchá. Tílka z merina ocení hlavně turisté. Více viz <a href="/merino/">merino</a>.</li>'
          '<li><strong>Viskóza a modal</strong> jsou měkké a splývavé, hodí se na jógu a volný čas.</li></ul>'
          '<h2>Výběr podle sportu</h2>'
          '<h3>Běh</h3>'
          '<p>Při běhu rozhoduje odvod potu a absence tření. Hledejte lehký materiál, ploché švy u podpaží a střih, který se nesbalí na hrudi. Pro vyšší teploty jsou nejvhodnější světlé barvy a síťované zóny. Ranní nebo večerní běh vyžaduje reflexní prvky. Doporučujeme kombinaci s <a href="/sportovni-kratasy/">kraťasy</a> nebo <a href="/leginy/">legínami</a> a vhodnou <a href="/bezecka-obuv/">běžeckou obuví</a>.</p>'
          '<h3>Posilovna a fitness</h3>'
          '<p>Při zvedání je potřeba volný pohyb v ramenou a lopatkách. Pánské posilovací tílko má hluboké průramky a volný střih, dámský top je přiléhavější, aby se při předklonu neposouval. Při cvičení s činkami zkontrolujte, zda tílko nebrání pohybu ruky a nesjíždí při tahu. Vybavení pro trénink najdete také v kategoriích <a href="/fitness/">fitness</a> a <a href="/cinky-a-kotouce/">činky a kotouče</a>.</p>'
          '<h3>Jóga a pilates</h3>'
          '<p>Tady se hodí měkký, pružný materiál s delšími zády, který se při předklonech neposune. Přiléhavý střih zabrání, aby se látka přehodila přes hlavu při pozicích hlavou dolů. Tílko je vhodné kombinovat s legínami a podložkou z kategorie <a href="/joga-a-podlozky/">jóga a podložky</a>.</p>'
          '<h3>Kolo a turistika</h3>'
          '<p>Na kole je důležité, aby tílko nezvedalo vítr v zádech. Přiléhavý střih a delší zadní část chrání záda před větrem. U turistiky s batohem dejte pozor na ramínka, která mohou pod popruhy tlačit. Tam je lepší širší ramínko nebo klasické tričko. Na slunci myslete na ochranu ramen krémem nebo lehkou vrstvou navíc.</p>'
          '<h3>Týmové sporty a basketbal</h3>'
          '<p>Basketbalové tílko bývá širší a delší, aby nesvazovalo pohyb. U atletiky se používá nízký střih a lehký materiál. Spoluhráči často volí stejné barvy, proto se vyplatí zkontrolovat dostupnost stejné velikosti a barvy ve více kusech. Související vybavení najdete v kategoriích <a href="/basketbal/">basketbal</a> a <a href="/micove-sporty/">míčové sporty</a>.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Při výběru tílka sledujte obvod hrudníku, pasu a délku trupu. Tílko by mělo sedět pevně, ale nesmí škrtit. U elastických materiálů je rozumné volit menší velikost, protože látka povolí, u pevných bavlněných větší. Dámské střihy bývají užší v pase, pánské širší v ramenou, u unisex střihu zkontrolujte odpovídající tabulku. Při nákupu pro děti zvolte rezervu na růst, ale ne příliš velkou, protože tílko by mělo zůstat na ramenou.</p>'
          '<h2>Jak o tílko pečovat</h2>'
          '<p>Syntetické materiály perte na 30 až 40 °C, nejlépe naruby a v ochranném pytlíku. Vyhněte se aviváži, která ucpává póry a zhoršuje odvod potu. Elastické topy se nesmějí sušit na topení, protože se poškodí pružnost. Bavlněné tílko vydrží vyšší teplotu, ale srazí se. Potisky chraňte tím, že tílko perete naruby a neždímáte vysokými otáčkami.</p>'
          '<ul><li>Tílko po sportu nenechávejte v tašce, ve vlhku zapáchá.</li>'
          '<li>Světlé a tmavé kusy perte zvlášť.</li>'
          '<li>Při škrábání štítku jej opatrně odstřihněte.</li>'
          '<li>Skladujte vyvěšené nebo složené, ne zmuchlané.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Bavlněné tílko na intenzivní trénink.</strong> Nasákne a ztěžkne.</li>'
          '<li><strong>Příliš těsný top na dlouhé cvičení.</strong> Může omezovat dýchání.</li>'
          '<li><strong>Příliš hluboký průramek na běh.</strong> Způsobuje tření o bok.</li>'
          '<li><strong>Zanedbaná ochrana před sluncem.</strong> Odhalená ramena se rychle spálí.</li>'
          '<li><strong>Tmavá barva na slunci.</strong> Nasákne víc tepla než světlá.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr tílek a topů mají ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('joma', 'Joma'), ('gap', 'Gap'), ('trespass', 'Trespass'), ('under-armour', 'Under Armour'), ('puma', 'Puma'), ('gymbeam', 'GymBeam'), ('asics', 'Asics'), ('craft', 'Craft'), ('4f', '4F'), ('loap', 'Loap'), ('icebreaker', 'Icebreaker')) + '. Adidas, Nike a Puma nabízejí sportovní střihy na trénink. Joma a Asics se zaměřují na týmové a běžecké sporty, GymBeam na posilovnu a Icebreaker na merino. Gap a Guess mají spíš módní charakter, proto je u nich třeba zkontrolovat použitelnost pro sport.</p>'
          '<h2>Pro koho jaké tílko</h2>'
          '<p>Začátečník v posilovně vystačí s volným bavlněným nebo polyesterovým tílkem. Běžec potřebuje lehký, přiléhavý kus bez švů. Žena na jógu ocení měkký top s vyšším pasem. Dítě ve sportovním kroužku potřebuje odolné a příjemné tílko, které se bude snadno prát. Na dovolenou si vyberte vzdušnou směs s viskózou, která se nemačká.</p>'
          '<h2>Jak kombinovat</h2>'
          '<p>Tílko lze kombinovat s mnoha dalšími kusy. Navrch se hodí <a href="/mikiny/">mikina</a> nebo <a href="/teplaky/">tepláky</a>, dole <a href="/sportovni-sukne-a-saty/">sportovní sukně</a>. Při chladu přidejte <a href="/funkcni-mikiny/">funkční mikinu</a> nebo <a href="/sportovni-bundy-jaro-podzim/">sportovní bundu</a>. Spodní prádlo najdete v kategorii <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>.</p>'
          '<h2>Sezóna, počasí a ochrana těla</h2>'
          '<p>Tílko je typicky letní kus, ale s vhodnými vrstvami ho lze nosit i mimo léto. Na jaře a na podzim funguje jako spodní vrstva pod tenkou bundu: rozepnete bundu, když se zahřejete, a pod ní zůstane vzdušná látka. V zimě se hodí v tělocvičně nebo při běhu na pásu, kde je teplo. Venku v chladu je vhodnější dlouhý rukáv. Při pobytu na slunci nezapomeňte, že tílko odkrývá ramena a horní část zad, což jsou místa, která se nejsnáz spálí. Použijte opalovací krém, případně přes tílko přehoďte lehkou košili nebo UV tričko z kategorie <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>.</p>'
          '<h2>Tření, otěry a pot</h2>'
          '<p>Nejčastější problém u tílek je tření v podpaží a na hrudi, kde se při opakovaném pohybu látka otírá o kůži. Pomáhá hladký materiál, ploché nebo bezešvé spoje a správná velikost: příliš volné tílko se sune, příliš těsné škrtí. Při dlouhém běhu muži často řeší tření bradavek, proto se vyplatí zvolit hladký materiál bez hrubých švů nebo použít ochrannou náplast. Ženy by měly kontrolovat okraje topu v oblasti podpaží a pod prsy, kde lem nesmí řezat ani tlačit. U dlouhé aktivity je dobré mít po ruce suché tílko na převlečení.</p>'
          '<h2>Tílko jako běžné oblečení</h2>'
          '<p>Mimo sport se tílka nosí na dovolenou, k vodě a jako spodní vrstva pod košili nebo lehký svetr. Hodí se jednoduché barvy, které se kombinují s kraťasy i sukní. Pokud tílko slouží také jako běžné oblečení, zvažte směs s bavlnou nebo viskózou, která je příjemnější při pomalejším pohybu a méně se leskne než čistý polyester. Kategorie <a href="/sportovni-tricka/">sportovní trička</a> pak doplní nabídku pro situace, kdy chcete přikrýt ramena.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Sporteka zobrazuje nabídky různých obchodů vedle sebe. Před nákupem zkontrolujte dostupné velikosti a barvy, protože stejné tílko se v různých obchodech může lišit. Zvažte, zda potřebujete spíše vzdušné tílko na léto, nebo pevnější kus na trénink. Při nákupu více kusů zvolte kombinaci barev, která se hodí k ostatnímu oblečení. Slevy bývají na konci léta, kdy se vyprodávají letní kolekce, a u starších barevných variant.</p>',
    faq=[('Jaké tílko na běh?', 'Lehké, z rychleschnoucího polyesteru či polyamidu, s plochými švy a bez zbytečných ozdob. V horku zvolte světlou barvu a síťované zóny pro větrání, večer reflexní prvky.'),
         ('Jaké tílko do posilovny?', 'Volný střih s hlubším průramkem, který nebrání pohybu v ramenou. Materiál by měl odvádět pot, ale snést časté praní. Ženám často vyhovuje top s větší přiléhavostí, aby se nesunul.'),
         ('Čím se liší top od tílka?', 'Top bývá kratší a přiléhavější, často s podporou prsou. Tílko je delší, volnější a má jen ramínka. V praxi se oba pojmy prolínají, proto zkontrolujte popis a střih.'),
         ('Je crop top vhodný na sport?', 'Ano, pro fitness, jógu a lehký trénink. Pro intenzivní běh nebo skákání je třeba dostatečná podpora, kterou zajistí samostatná sportovní podprsenka.'),
         ('Dá se tílko nosit na kolo?', 'Dá, pokud nemáte problém s ramínky pod popruhy batohu. Na delší jízdy je ale vhodnější cyklistický dres, který má delší záda a kapsy.'),
         ('Jak velké tílko vybrat?', 'Řiďte se tabulkou výrobce a svými rozměry. Elastické materiály povolí, proto je vhodnější menší velikost, u bavlny volte jistěji větší. Mezi unisex a dámským střihem rozhoduje pohodlí v ramenou.'),
         ('Jak prát sportovní tílko?', 'Na 30 až 40 °C, naruby, bez aviváže a bez sušení na topení. Elastan a potisk jsou citlivé na teplo. Při zápachu pomůže sportovní prací prostředek nebo namočení v octovém roztoku.'),
         ('Je merino tílko vhodné do léta?', 'Tenké merino se nosí i v teple, protože pomáhá regulovat teplotu a méně zapáchá. Schne ale pomaleji než polyester, takže na intenzivní běh v horku je vhodnější syntetika.'),
         ('Hodí se tílko pro děti?', 'Ano, v létě a na sportovních kroužcích. Zvolte měkké švy, odolný materiál a rezervu na růst. Při pobytu na slunci nezapomeňte na ochranu ramen, protože tílko je odkrývá.'),
         ('Proč tílko při pohybu sjíždí?', 'Většinou je příliš velké nebo má úzká ramínka a krátká záda. Vyberte menší velikost, širší ramínka nebo delší zadní část. U elastických materiálů pomáhá střih s vyšším průramkem.')],
)

# ------------------------------------------------------------------ rybarske-pruty
NEW['rybarske-pruty'] = dict(long=True,
    title='Rybářské pruty: přívlač, kapr, feeder, muška | Sporteka',
    desc='Rybářské pruty na přívlač, kapry, feeder, muškaření i moře. Průvodce délkou, akcí a hmotností nástrahy a porovnání obchodů na jednom místě.',
    intro='<p><strong>Rybářský prut</strong> rozhoduje o tom, jak daleko dohodíte, jak citlivě zaregistrujete záběr a jak pohodlně zdoláte rybu. Prut se vybírá podle způsobu lovu, ne podle délky ani barvy. Jiný se hodí na kapra, jiný na dravce a jiný na jemný lov bílé ryby.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů u prutů značek Daiwa, Mikado, Westin, Shimano, Favorite či Delphin. K prutu patří <a href="/rybarske-navijaky/">navijáky</a>, <a href="/vlasce-a-snury/">vlasce a šňůry</a>, <a href="/nastrahy-a-navnady/">nástrahy a návnady</a> a <a href="/rybarske-tasky/">rybářské tašky</a>. Nadřazenou stránkou je <a href="/rybareni/">rybaření</a>. Najdete tu rady pro začátečníky i pokročilé rybáře, od čtení označení na prutu přes výběr první sestavy až po bezpečnou přepravu a péči o vybavení po lovu.</p>',
    guide='<h2>Z čeho se prut skládá</h2>'
          '<p>Prut tvoří blank, tedy trubice z uhlíkového vlákna, skelného vlákna nebo jejich směsi, a doplňují ho očka, rukojeť a sedlo pro naviják. Karbon je lehký a citlivý, ale křehčí při nárazu. Sklolaminát je těžší a odolnější, proto se používá u pevných prutů na těžké nástrahy. Velmi často se materiály kombinují, aby prut byl dostatečně tuhý a přitom odpouštěl chyby.</p>'
          '<p>Očka vedou vlasec nebo šňůru podél prutu. Měla by být pevně přilepená, bez prasklin a s vložkou, která snáší otěr. Rukojeť bývá z korku nebo pěny EVA. Korek je příjemný na dotek, pěna odolnější vůči vlhku a špíně. Sedlo pro naviják má pevný šroubový nebo kolíkový zámek, který naviják drží při tahu ryby.</p>'
          '<h2>Typy prutů podle způsobu lovu</h2>'
          + T(['Typ', 'Použití', 'Typické vlastnosti'], [
              ['Přívlačový', 'dravci na umělé nástrahy', 'kratší, rychlá akce, rozsah hmotnosti nástrahy'],
              ['Kaprový', 'kapři a velké bílé ryby', 'delší, dálkové nahazování, testní křivka v librách'],
              ['Feederový', 'lov na krmítko', 'výměnné špičky, střední délka'],
              ['Match a bolognese', 'jemný lov bílé ryby na splávek', 'dlouhý, lehký, citlivá špička'],
              ['Muškařský', 'lov na umělé mušky', 'označení třídy šňůry, dlouhý a pružný'],
              ['Mořský', 'rybaření na moři a ze člunu', 'odolný, silné očka, tužší akce'],
              ['Teleskopický', 'cestování a rekreace', 'skládací, kompaktní'],
              ['Dětský', 'začátečníci', 'krátký, lehký, tolerantní']]) +
          '<p>Správný výběr závisí na vodě a rybě, kterou chcete lovit. Rychlá řeka vyžaduje jiný prut než klidný rybník. Ke každému typu patří odpovídající naviják a vlasec, jinak se prut nebude chovat tak, jak má.</p>'
          '<h2>Délka prutu</h2>'
          '<p>Delší prut dohodí dál, lépe tlumí výpady ryby a umožní vést návazec nad překážkami. Kratší prut je obratnější v úzkých místech, v křoví nebo z lodi. Přívlačové pruty bývají kratší, kaprové delší, feederové střední. Při delší délce roste hmotnost a vyšší nároky na ruku, proto vybírejte vyváženě. U dělených prutů záleží i na transportní délce, která se hodí do auta nebo na batoh.</p>'
          '<h2>Akce prutu</h2>'
          '<p>Akce udává, jak se prut ohýbá při zatížení. U rychlé akce se ohýbá hlavně špička, prut je citlivý a přesný. U pomalé akce se ohýbá celá délka, odpouští chyby a hodí se pro rybu, která by se jinak snadno vytrhla. Střední akce je kompromis. Pro začátečníka je často vhodnější pomalejší nebo střední akce, protože toleruje chyby při zdolávání.</p>'
          '<h2>Hmotnost nástrahy a testní křivka</h2>'
          '<p>Přívlačové pruty se označují rozsahem hmotnosti nástrahy, který prut bezpečně unese. Je-li nástraha příliš lehká, prut ji nedohodí; je-li příliš těžká, hrozí přetížení a poškození prutu. Kaprové pruty se označují testní křivkou v librách, která udává sílu prutu při určitém ohybu. Vždy se držte údajů výrobce a dbejte, aby odpovídaly navijáku, vlasci a ulovené rybě.</p>'
          '<h2>Výběr podle vody a ryby</h2>'
          '<h3>Přívlač na dravce</h3>'
          '<p>Lov štiky, okouna nebo candáta se opírá o aktivní vedení umělé nástrahy. Hodí se kratší prut s rychlou akcí a citlivou špičkou, často v kombinaci s braidem. Okounům stačí lehčí prut, štikám silnější. Vybírejte podle velikosti nástrahy a prostředí. Související kategorie: <a href="/nastrahy-a-navnady/">nástrahy a návnady</a> a <a href="/vlasce-a-snury/">vlasce a šňůry</a>.</p>'
          '<h3>Kapr a velké ryby</h3>'
          '<p>Kaprové pruty jsou delší a tužší, aby zvládly dálkové hody a silné výpady. Pro lov z břehu jsou nejběžnější modely kolem tří a půl metru. Pokud lovíte ve volné vodě, vybírejte podle překážek a dostřelu. Navíjejte na naviják s pevnou brzdou a dostatečnou kapacitou vlasce.</p>'
          '<h3>Feeder a bílá ryba</h3>'
          '<p>Feeder je vhodný pro lov na řece i rybníku. Prut má sadu výměnných špiček, které se volí podle zátěže krmítka a proudu. Slabší špička je citlivější, silnější odolnější vůči větru a proudu. Match a bolognese pruty jsou delší a lehčí, určené pro jemný lov na splávek.</p>'
          '<h3>Muškaření</h3>'
          '<p>Muškařský prut se označuje třídou, která odpovídá hmotnosti šňůry. Třída musí sedět s navijákem a šňůrou. Pro pstruhy v potoce se používá nižší třída, pro větší řeky a lov na dálku vyšší. Příslušné vybavení najdete v kategorii <a href="/muskareni/">muškaření</a>.</p>'
          '<h3>Moře a těžký lov</h3>'
          '<p>Mořské pruty jsou odolné, s pevnými očky a často tužší akcí. Při rybaření z lodi se používají kratší, při lovu z břehu delší modely. Součástí výbavy jsou odolné navijáky, silné šňůry a vybavení do slané vody, které se po lovu musí opláchnout.</p>'
          '<h2>Prut a naviják jako pár</h2>'
          '<p>Prut s navijákem musí ladit, jinak se výkon sníží. Příliš těžký naviják vychýlí vyvážení, příliš lehký zase nezvládne zatížení. Při skládání výbavy zkuste prut s navijákem podržet v místě rukojeti: měl by zůstat v rovnováze. Velikost navijáku se uvádí číslem a orientačně se řídí délkou prutu a typem lovu. Víc k výběru najdete v kategorii <a href="/rybarske-navijaky/">rybářské navijáky</a>.</p>'
          '<h2>Péče o prut</h2>'
          '<p>Po výpravě prut otřete vlhkým hadříkem, osušte a zkontrolujte očka. Po rybaření v moři opláchněte sladkou vodou. Skladujte v pouzdře nebo tubusu, mimo přímé slunce a vlhko. Při přepravě držte špičku v ochranném obalu, protože se snadno zlomí. Nikdy prut neopírejte špičkou o zeď a při skládání dbejte na rovné spojení dílů.</p>'
          '<ul><li>Spojení dílů občas promažte voskem, aby nehrozilo zadření.</li>'
          '<li>Očka kontrolujte nehtem, abyste odhalili prasklinu dřív než vlasec.</li>'
          '<li>Prut na dlouho neskladujte zatížený nebo ohnutý.</li>'
          '<li>Neodkládejte prut v autě na slunci, lepidla a pryskyřice mohou změknout.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Prut na všechno.</strong> Žádný prut nezvládne dobře kapra i štiku; začátečník ať zvolí kompromisní prut pro jeden způsob lovu.</li>'
          '<li><strong>Zanedbaná hmotnost nástrahy.</strong> Přetížený nebo nevyužitý prut se chová špatně.</li>'
          '<li><strong>Příliš dlouhý prut do úzkých míst.</strong> Zamotá se v křoví a brání v obratnosti.</li>'
          '<li><strong>Špatný naviják.</strong> Nesoulad vede k nepříjemnému vyvážení.</li>'
          '<li><strong>Příliš tvrdý prut pro začátečníka.</strong> Trhá lehčí návazce a zhoršuje pocit ze záběru.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky jako ' + B(('daiwa', 'Daiwa'), ('mikado', 'Mikado'), ('westin', 'Westin'), ('caperlan', 'Caperlan'), ('favorite', 'Favorite'), ('delphin', 'Delphin'), ('shimano', 'Shimano'), ('sema', 'Sema'), ('mivardi', 'Mivardi'), ('dam', 'DAM'), ('penn', 'Penn'), ('fox', 'Fox'), ('savage-gear', 'Savage Gear'), ('black-cat', 'Black Cat')) + '. Westin a Savage Gear míří hlavně na přívlač, Mikado, Daiwa a Shimano pokrývají široký rozsah od začátečníků po zkušené. Delphin a Mivardi jsou silné u kapraření a feederu, Black Cat se specializuje na sumce a Penn na mořský rybolov.</p>'
          '<h2>Pro koho jaký prut</h2>'
          '<p>Začátečník potřebuje univerzální prut střední délky s tolerantní akcí a k tomu základní naviják. Dítě ocení krátký a lehký model. Přívlačáři se vyplatí mít dvě sestavy, lehkou na okouny a silnější na štiky. Kapraři využijí dvojici stejných prutů pro lov z břehu. Cestovatel vezme dělený nebo teleskopický prut, který zabere málo místa.</p>'
          '<h2>Související vybavení</h2>'
          '<p>K prutu patří řada doplňků. Do tašky na výpravu se hodí <a href="/rybarske-tasky/">rybářské tašky</a>, pro ležení a spaní <a href="/rybarske-spacaky/">rybářské spacáky</a>, pro lov z vody <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>. Další vybavení najdete v kategoriích <a href="/rybarske-doplnky/">rybářské doplňky</a> a <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>'
          '<h2>Jak číst označení na prutu</h2>'
          '<p>Na spodním dílu prutu najdete vytištěné údaje, které shrnují jeho určení. Obvykle jde o délku v metrech nebo stopách, rozmezí hmotnosti nástrahy v gramech nebo uncích a u kaprových prutů testní křivku v librách. U přívlačových prutů často stojí i doporučený rozsah vlasce či šňůry. Pokud se čísla pohybují těsně u hranice, prut pracuje nejlépe uprostřed rozsahu, kdy se ohýbá přirozeně. Pokud kupujete přes internet, ověřte, zda je uvedená délka skutečná, nebo transportní, protože u dělených prutů se liší.</p>'
          '<h2>První sestava pro začátečníka</h2>'
          '<p>Kdo začíná, nepotřebuje několik prutů najednou. Rozumná výchozí sestava se skládá z jednoho univerzálního prutu střední délky, navijáku odpovídající velikosti, monofilního vlasce a základní sady háčků, splávků a zátěží. S tím lze chytat v rybníce, na pomalé řece i v lomu. Teprve po prvních sezónách se ukáže, kterým směrem se rybaření ubírá, a podle toho se doplňuje výbava. Vyhnete se tak nákupu prutu, který nebudete používat.</p>'
          '<h2>Přeprava a dělení</h2>'
          '<p>Dělené pruty se skládají ze dvou až čtyř dílů a zabírají v autě i na kole méně místa. Čím více dílů, tím kratší transportní délka, ale také víc spojů, které mohou ovlivnit pružnost. Kvalitní spoj je pevný, bez vůle a po sestavení vytváří souvislou křivku. Pro cestování vlakem nebo letadlem se hodí cestovní pruty s více díly, pro běžný lov z auta stačí dvoudílný model. Transportní pouzdro nebo tubus chrání před zlomením, zvlášť špičky, a udrží pruty pohromadě.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Sporteka zobrazuje nabídky různých obchodů pohromadě. Před nákupem zkontrolujte délku, počet dílů, hmotnost nástrahy a transportní délku. U stejného modelu se mohou lišit dostupné délky, proto porovnejte detail. Pokud nakupujete jako začátečník, vybírejte spíše ověřené modely s jasnými parametry. Prut není potřeba měnit každý rok, vyplatí se kvalitní kus, který vydrží několik sezón.</p>',
    faq=[('Jaký prut na přívlač?', 'Kratší prut s rychlou akcí a rozsahem hmotnosti nástrahy, který odpovídá vašim nástrahám. Pro okouna lehčí, pro štiku silnější. K prutu zvolte naviják a splétanou šňůru.'),
         ('Co znamená akce prutu?', 'Popisuje, jak se prut ohýbá. Rychlá akce se ohýbá hlavně ve špičce a je citlivější, pomalá se ohýbá po celé délce a odpouští chyby.'),
         ('Co je testní křivka?', 'Údaj v librách u kaprových prutů, který popisuje sílu prutu při ohybu. Pomáhá určit, jakou zátěž a vzdálenost prut zvládne.'),
         ('Jak dlouhý prut vybrat?', 'Záleží na vodě a způsobu lovu. Delší prut dohodí dál, kratší je obratnější v úzkých místech a při lovu z lodi. Přívlač bývá kratší, kapr delší.'),
         ('Hodí se teleskopický prut?', 'Pro cestování a rekreační rybaření ano. Při náročném lovu bývají dělené pruty spolehlivější, protože lépe přenášejí sílu a jsou citlivější.'),
         ('Jaký prut pro začátečníka?', 'Univerzální, střední délky, s tolerantní akcí a čitelnými parametry. Nemusí být nejdražší, ale měl by mít kvalitní očka a pevné spoje.'),
         ('Jaký naviják k prutu?', 'Takový, který prut vyváží a odpovídá jeho délce a třídě. Příliš těžký naviják vychýlí rovnováhu, příliš lehký nezvládne zatížení. Velikost navijáku výrobce často uvádí.'),
         ('Jak pečovat o prut?', 'Po lovu otřít a osušit, zkontrolovat očka, po moři opláchnout. Skladovat v pouzdře mimo slunce a vlhko, špičku chránit proti zlomení.'),
         ('Jaký prut na feeder?', 'Střední délky, s výměnnými špičkami podle zátěže krmítka. Slabší špička pro klidnou vodu, silnější pro proud a vítr.'),
         ('Co je třída u muškařského prutu?', 'Číslo, které odpovídá hmotnosti šňůry. Prut, šňůra a naviják musí mít stejnou třídu, jinak se hod zhorší a vybavení nepracuje správně.')],
)

# ------------------------------------------------------------------ sportovni-tasky
NEW['sportovni-tasky'] = dict(long=True,
    title='Sportovní tašky a ledvinky: fitness, cesty | Sporteka',
    desc='Sportovní tašky, duffel bagy, ledvinky a vaky na trénink, cesty a výlety. Průvodce objemem, materiálem a nošením, ceny českých e-shopů.',
    intro='<p><strong>Sportovní taška</strong> musí odnést vybavení a při tom se pohodlně nosit. Do posilovny potřebujete jinou než na víkend u vody nebo na cestu autobusem. Rozhoduje objem, materiál, uspořádání kapes a způsob nošení: přes rameno, v ruce, na zádech nebo kolem pasu.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K taškám patří <a href="/tasky-pres-rameno/">tašky přes rameno a dokladovky</a>, <a href="/batohy/">batohy</a>, <a href="/turisticke-batohy/">turistické batohy</a>, <a href="/mestske-batohy/">městské batohy</a> a <a href="/skolni-batohy/">školní batohy</a>. Níže najdete, jak vybrat typ, objem, materiál a organizaci obsahu, aby se vám s taškou dobře cestovalo, ať ji berete do posilovny, na vodu nebo na víkend, a aby vám v ní věci vydržely v pořádku.</p>',
    guide='<h2>Co všechno sem patří</h2>'
          '<p>Kategorie sdružuje několik odlišných typů. Fitness tašky jsou prostorné a mají oddělené kapsy na boty a vlhké věci. Duffel bagy jsou válcové, odolné a vhodné na víkendové cesty. Ledvinky nosí doklady, klíče a telefon při běhu, kole nebo procházce. Vodotěsné vaky chrání obsah před vodou při pádlování. Tašky přes rameno se hodí jako městský doplněk, a spadají do podkategorie <a href="/tasky-pres-rameno/">tašky přes rameno a dokladovky</a>.</p>'
          '<p>Hranice mezi typy nejsou ostré. Duffel bag se nosí přes rameno i na zádech, malá taška se stává ledvinkou a obráceně. Vybírejte proto podle toho, co potřebujete odnést a jak dlouho ji ponesete. Pokud trasa vyžaduje nosit tašku déle než deset minut, bývá pohodlnější batoh.</p>'
          '<h2>Typy tašek a jejich použití</h2>'
          + T(['Typ', 'Typický objem', 'Použití'], [
              ['Fitness taška', 'menší až střední', 'posilovna, plavání, sportovní kroužek'],
              ['Duffel bag', 'střední až velký', 'víkendové cesty, týmové výjezdy'],
              ['Ledvinka', 'jednotky litrů', 'běh, kolo, procházky, festival'],
              ['Taška přes rameno', 'malý objem', 'město, doklady, drobnosti'],
              ['Vodotěsný vak', 'střední', 'kajak, paddleboard, déšť'],
              ['Cestovní taška na kolečkách', 'velký', 'dovolená, letiště'],
              ['Taška na boty', 'malý', 'oddělení špinavé obuvi']]) +
          '<p>Specializované tašky, například hokejové nebo lyžařské vaky, mají vlastní kategorie: <a href="/hokejove-tasky/">hokejové tašky</a> a <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>. Pro golfisty najdete <a href="/golfove-tasky-a-voziky/">golfové tašky a vozíky</a> a pro cyklisty <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>'
          '<h2>Jak zvolit objem</h2>'
          '<p>Objem se udává v litrech a je orientační. Na jeden trénink stačí menší taška, do které se vejdou boty, oblečení na převlečení a ručník. Na víkendovou cestu potřebujete střední duffel, na dovolenou nebo delší pobyt velký. Příliš velká taška se zbytečně plní a je těžká, příliš malá nutí nacpat věci a namáhá zipy. Praktické je zvolit objem podle nejčastějšího použití a pro výjimečné cesty vypůjčit nebo koupit samostatnou.</p>'
          + T(['Situace', 'Doporučený rozsah'], [
              ['Trénink v posilovně', 'zhruba 20 až 40 litrů'],
              ['Víkend mimo domov', 'zhruba 40 až 70 litrů'],
              ['Delší cesta či dovolená', 'zhruba 70 litrů a více'],
              ['Běh a krátké procházky', 'ledvinka několik litrů'],
              ['Doklady a telefon ve městě', 'malá dokladovka']]) +
          '<h2>Materiály a konstrukce</h2>'
          '<ul><li><strong>Nylon a polyester</strong> jsou nejběžnější. Jsou lehké a odolné proti oděru, často s impregnací.</li>'
          '<li><strong>PVC a plachtovina</strong> jsou těžší, ale vodotěsné, hodí se na vodní sporty.</li>'
          '<li><strong>Kůže a koženka</strong> vypadají elegantně, ale váží víc a vyžadují péči.</li>'
          '<li><strong>Bavlněné plátno</strong> je pohodlné a měkké, ale nasákne vodou.</li>'
          '<li><strong>Recyklované materiály</strong> se objevují u mnoha značek, vlastnosti jsou podobné běžným syntetikám.</li></ul>'
          '<p>Kromě materiálu rozhoduje kvalita zipů, švů a popruhů. Zipy by měly mít silné zuby a pohodlné tahací očko. Popruhy musí být přišité na zesíleném podkladu, nikoli jen přes látku. Dno bývá zesílené, aby taška nenasákla od podlahy. U vodotěsných vaků se kontrolují svařené švy a rolovací uzávěr, který se několikrát přehne.</p>'
          '<h2>Způsoby nošení</h2>'
          '<h3>V ruce a přes rameno</h3>'
          '<p>Většina fitness tašek má dvě krátká ucha a jeden nastavitelný popruh přes rameno. Popruh by měl být široký a s polstrováním, aby se při zátěži nezařezával. Při delším nošení střídejte strany, abyste nezatěžovali jedno rameno.</p>'
          '<h3>Na zádech</h3>'
          '<p>Některé duffel bagy mají odnímatelné popruhy a dají se nosit jako batoh. Tento způsob je pohodlnější při delší chůzi a při nosení těžších věcí. Pokud uvažujete o pravidelném nošení na zádech, zvažte spíše <a href="/batohy/">batoh</a>, který má lepší rozložení váhy.</p>'
          '<h3>Kolem pasu a přes hruď</h3>'
          '<p>Ledvinka drží drobnosti blízko těla. Při běhu se musí nastavit tak, aby neskákala. Pro delší túry se vyplatí ledvinka s širokým pásem a více kapsami. Přes hruď se nosí malé tašky a dokladovky, které jsou rychle přístupné.</p>'
          '<h2>Výběr podle sportu a aktivity</h2>'
          '<h3>Posilovna a trénink</h3>'
          '<p>Hledejte tašku s větrací kapsou na boty a samostatnou kapsou na vlhké věci. Dobře se hodí taška s širokým otevřením, protože v ní snadno najdete věci. Při cvičení s vlastním vybavením, například gumami nebo kotouči, ocení pevné dno. Vybavení pro cvičení najdete v kategorii <a href="/fitness/">fitness</a>.</p>'
          '<h3>Plavání a vodní sporty</h3>'
          '<p>Po bazénu se hodí taška s větratelnou kapsou na mokré plavky a lehká síťovina. Pro vodní sporty je lepší vodotěsný vak, který ochrání telefon, klíče a oblečení. K plavání patří <a href="/plavky/">plavky</a>, <a href="/plavecke-pomucky/">plavecké pomůcky</a> a <a href="/plavecke-bryle/">plavecké brýle</a>.</p>'
          '<h3>Kolo a běh</h3>'
          '<p>Ledvinka nebo malá taška přes rameno je pohodlná na krátké vyjížďky. Pro delší cesty se hodí <a href="/cyklo-tasky-a-nosice/">cyklo tašky</a>. Při běhu vybírejte lehké ledvinky s pevným pásem, případně <a href="/bezecke-opasky/">běžecké opasky</a>, které se při pohybu neposouvají.</p>'
          '<h3>Týmové sporty</h3>'
          '<p>Hokejisté potřebují velký prostor pro chrániče, týmové tašky mají pevné dno a velké přihrádky. Fotbalisté vystačí s menší taškou a samostatnou kapsou na kopačky. Související vybavení najdete v kategoriích <a href="/hokej/">hokej</a> a <a href="/fotbal/">fotbal</a>.</p>'
          '<h3>Cesty a víkendy</h3>'
          '<p>Duffel bag je skvělý, protože se přizpůsobí tvaru obsahu a snadno se vejde do kufru nebo na polici. Pro cesty s přestupem je výhodnější taška na kolečkách. Při letecké dopravě zkontrolujte limity rozměrů příručního zavazadla u dopravce.</p>'
          '<h2>Vybavení uvnitř tašky</h2>'
          '<p>Uvnitř tašky se vyplatí používat malé organizéry a sáčky. Mokré oblečení dejte do vodotěsného sáčku, boty do samostatné tašky, drobnosti do síťované kapsy. Doplňky jako <a href="/lahve-a-termosky/">láhve a termosky</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a> mají svůj prostor a nezaberou místo hlavní přihrádce.</p>'
          '<h2>Péče o tašku</h2>'
          '<p>Po tréninku tašku vyvětrejte a vysušte, vlhké věci nenechávejte uvnitř. Čistěte vlhkým hadříkem a jemným mýdlem, silné čisticí prostředky mohou poškodit impregnaci. Zipy občas očistěte kartáčkem a lehce promažte. Při nasáknutí vodou tašku nechte vyschnout při pokojové teplotě, nikoli u topení, a po vyschnutí případně znovu impregnujte. Skladujte volně, ne přeplněnou, aby se nedeformovala.</p>'
          '<ul><li>Neprat v pračce, pokud to výrobce výslovně nepovoluje.</li>'
          '<li>Boty vkládejte do samostatné kapsy nebo sáčku.</li>'
          '<li>Popruhy nenechávejte přetížené delší dobu.</li>'
          '<li>Při poškození zipu zkuste výměnu jezdce dříve než reklamaci celé tašky.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Příliš velká taška.</strong> Naplní se zbytečnostmi a je těžká.</li>'
          '<li><strong>Tenké popruhy.</strong> Zařezávají se do ramene a rychle povolí.</li>'
          '<li><strong>Zanedbaná kapsa na boty.</strong> Špinavá obuv znečistí zbytek.</li>'
          '<li><strong>Nevodotěsný materiál na vodu.</strong> Obsah nasákne a zničí se elektronika.</li>'
          '<li><strong>Ledvinka na těžké věci.</strong> Táhne dolů a obtěžuje v pase.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr mají značky ' + B(('fjallraven', 'Fjällräven'), ('rothco', 'Rothco'), ('hms', 'HMS'), ('deuter', 'Deuter'), ('adidas', 'Adidas'), ('nike', 'Nike'), ('the-north-face', 'The North Face'), ('merco', 'Merco'), ('sea-to-summit', 'Sea to Summit'), ('rains', 'Rains'), ('helikon-tex', 'Helikon-Tex®'), ('osprey', 'Osprey'), ('tatonka', 'Tatonka'), ('eastpak', 'Eastpak')) + '. Adidas, Nike a Puma nabízejí tašky pro sport, Deuter, Osprey a The North Face jsou silné v outdoorovém prostředí. Sea to Summit a Rains se soustředí na vodotěsné materiály, Fjällräven, Eastpak a Helikon-Tex nabízejí odolné kusy pro každodenní nošení i výpravy.</p>'
          '<h2>Pro koho jaká taška</h2>'
          '<p>Rekreační sportovec do posilovny vystačí s taškou střední velikosti a boční kapsou na boty. Rodina s dětmi ocení větší duffel, do kterého se vejdou věci pro více lidí. Cestovatel hledá odolný materiál a pohodlné popruhy. Běžec a cyklista vezmou lehkou ledvinku. Vodní sportovec potřebuje vodotěsný vak. Student si vybere kombinaci tašky přes rameno a menšího batohu.</p>'
          '<h2>Organizace obsahu</h2>'
          '<p>I velká taška se rychle změní v nepořádek, pokud do ní věci jen házíte. Praktický je systém tří zón: dole těžké a odolné věci, uprostřed oblečení a nahoře to, co potřebujete rychle, například klíče nebo láhev. Vnější kapsy se hodí na doklady a drobnosti, vnitřní zipová kapsa na cennosti. Kompresní sáčky šetří místo u oblečení a síťované pouzdro uchová nabíječky a kabely pohromadě. Při pravidelném tréninku se vyplatí mít v tašce stálou základní sadu, aby bylo před cestou méně balení.</p>'
          '<h2>Bezpečnost a viditelnost</h2>'
          '<p>Pokud tašku nosíte při běhu nebo jízdě na kole za šera, zvolte kus s reflexními prvky nebo si je přidejte. Ledvinka by měla sedět pevně a nehoupat se, protože houpající se váha zhoršuje rovnováhu. Ve městě je rozumné nosit cennosti na straně k tělu a zipy otáčet dovnitř, aby byly hůře dostupné. U tašek s uzamykatelnými zipy lze použít malý visací zámek, což oceníte při šatnových skříňkách a na cestách.</p>'
          '<h2>Taška jako příruční zavazadlo</h2>'
          '<p>Pokud tašku chcete použít při letu, zkontrolujte maximální rozměry příručního zavazadla u dopravce a pravidla pro kapaliny. Měkká duffel taška se snadněji vejde do úzkého prostoru nad sedadlem než pevný kufr. Vyplatí se, když má jmenovku nebo označení, protože tašky stejné barvy a velikosti se snadno zaměňují.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Sporteka zobrazuje nabídky obchodů vedle sebe. Před nákupem zkontrolujte rozměry, objem, materiál a způsob nošení. U stejné tašky se mohou lišit barevné varianty a dostupnost. Pokud kupujete na delší cesty, ověřte kvalitu zipů a popruhů. Slevy bývají po sezóně, například po zimě u lyžařských vaků nebo po létě u plážových tašek.</p>',
    faq=[('Jakou tašku do posilovny?', 'Střední velikosti, zhruba tak, aby se vešly boty, oblečení a ručník. Hodí se oddělená kapsa na boty, odolný materiál a pohodlný popruh přes rameno.'),
         ('Co je duffel bag?', 'Válcová prostorná taška bez pevné konstrukce. Přizpůsobí se obsahu, je odolná a vhodná na víkendové cesty i týmové výjezdy.'),
         ('K čemu je vodotěsný vak?', 'Chrání věci před vodou při pádlování, na lodi, na kole nebo za deště. Obvykle má svařené švy a rolovací uzávěr.'),
         ('Jak velká taška na víkend?', 'Pro víkend obvykle stačí střední duffel. Pokud berete objemné věci, například spacák, zvolte větší. Kontrolujte i omezení rozměrů při cestování letadlem.'),
         ('Jak se liší ledvinka od dokladovky?', 'Ledvinka se nosí kolem pasu a je určená pro pohyb. Dokladovka je menší taška přes rameno nebo hruď, vhodná pro město a krátké cesty.'),
         ('Jak čistit sportovní tašku?', 'Vlhkým hadříkem a jemným mýdlem, vyvětrat a nechat vyschnout při pokojové teplotě. Pračka jen pokud výrobce výslovně povoluje, jinak hrozí poškození impregnace a konstrukce.'),
         ('Jaká taška na plavání?', 'S větratelnou kapsou na mokré plavky a materiálem, který nenasákne. Hodí se síťované přihrádky a vodotěsná kapsa pro telefon.'),
         ('Je lepší taška, nebo batoh?', 'Taška je praktická na krátké vzdálenosti a snadný přístup. Na delší chůzi je pohodlnější batoh, protože rozloží váhu na obě ramena a záda.'),
         ('Jak poznám kvalitní zipy?', 'Mají silné zuby, hladce jedou a jezdec drží pevně. Ověřte, zda zip nekončí těsně u švu, protože právě tam se nejčastěji trhá látka.'),
         ('Hodí se sportovní taška i pro děti?', 'Ano, na trénink, tábory i školní tělocvik. Vybírejte lehčí kus s měkkými popruhy a menším objemem, který dítě unese bez zatížení zad.')],
)
