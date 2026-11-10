"""sporteka.cz — wave 1, extension: longer intro + extra guide sections (brands from the live catalogue on 3. 11. 2026, common mistakes,
who it is for, when to buy). texty-export.py appends EXTRA[slug]['intro'] / ['guide'] to the entries of texty_vlna1a/b/c.py."""


def B(*pairs):
    """'<a href="/znacka/adidas/">Adidas</a>, …' from (slug, name) pairs."""
    return ', '.join(f'<a href="/znacka/{s}/">{n}</a>' for s, n in pairs)


EXTRA = {}

EXTRA['sportovni-obuv'] = dict(
    intro='<p>Při výběru nezapomeňte, že stejná velikost značky Nike nebo Adidas nemusí sedět stejně jako u jiného výrobce. Proto u každého páru ověřujte velikostní tabulku a sledujte, ve kterých obchodech jsou vaše čísla ještě skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr sportovní obuvi mají v nabídce značky {B(("adidas", "Adidas"), ("skechers", "Skechers"), ("nike", "Nike"), ("puma", "Puma"), ("converse", "Converse"), ("geox", "Geox"), ("new-balance", "New Balance"), ("asics", "Asics"))}. '
          'Každá má trochu jiný střih: Asics a New Balance bývají širší v přední části, Nike spíš užší, Skechers měkké a pohodlné na denní chůzi. Střih je důležitější než logo na jazyku.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Koupě bot jen podle designu, bez ohledu na určení. Módní tenisky nenahradí běžeckou obuv.</li>'
          '<li>Zkoušení ráno. Odpoledne a večer je chodidlo větší a bota, která ráno seděla, začne tlačit.</li>'
          '<li>Příliš těsná obuv. Prsty se musí mírně hýbat, jinak vznikají puchýře a otlaky.</li>'
          '<li>Ignorování šířky. Pokud vás bota tlačí na bocích, nepomůže větší číslo, ale širší střih.</li>'
          '<li>Nošení stejných bot každý den. Střídání dvou párů prodlužuje životnost a nohám uleví.</li></ul>'
          '<h3>Pánské, dámské a dětské boty</h3>'
          '<p>Dámské modely bývají užší v patě a středu chodidla a lehčí, pánské širší. Unisex modely se prodávají v obou velikostních řadách, převod mezi nimi uvádí výrobce. '
          'Dětské boty kupujte s rezervou asi 1 cm, ale ne větší, jinak dítě klopýtá. Dětské chodidlo roste rychle, proto se vyplatí kontrolovat velikost každé tři až čtyři měsíce.</p>'
          '<h3>Kdy se vyplatí koupit</h3>'
          '<p>Slevy se objevují na konci sezóny a při obměně kolekce. Zimní obuv bývá levnější na jaře, letní na podzim. Velikosti, které se rozprodávají poslední, jsou obvykle nejčastější a nejméně obvyklé, takže při slevě se rozhoduje rychle.</p>',
)

EXTRA['tenisky'] = dict(
    intro='<p>Nejčastěji hledané značky jsou Adidas, Nike, Puma, Converse a Skechers, k nim patří také New Balance, Geox a Vans. Mezi vyhledávanými klasikami je například Adidas Stan Smith. U každého modelu najdete srovnání obchodů, takže poznáte, kde je nejnižší cena i kde je vaše velikost skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr tenisek mají značky {B(("adidas", "Adidas"), ("skechers", "Skechers"), ("nike", "Nike"), ("puma", "Puma"), ("converse", "Converse"), ("new-balance", "New Balance"), ("geox", "Geox"), ("vans", "Vans"))}. '
          'Skechers jsou známé měkkou podešví na denní chůzi, Converse a Vans plochou podrážkou ve stylu klasických plátěnek, New Balance a Nike širokou škálou od retro po odpružené modely.</p>'
          '<h3>Dámské, pánské a dětské tenisky</h3>'
          '<p>U dámských tenisek se častěji setkáte s lehčí konstrukcí a pestřejšími barvami, pánské jsou širší. Platformové a retro modely se nosí i ke sportovním šatům. '
          'Dětské tenisky vybírejte lehké a s dobrým držením paty, na zavazování nebo suchý zip podle věku. Nejmenším se hodí suchý zip, školákům tkaničky.</p>'
          '<h3>Jak tenisky nosit</h3>'
          '<p>Bílé a světlé tenisky se hodí k džínám, šatům i oblekovým kalhotám a jsou nejuniverzálnější. Výrazné barvy a vzory se hodí ke střídmějšímu oblečení. '
          'Pokud tenisky nosíte celý den, zvolte lehký model s pružnější podrážkou. Při dešti dávejte přednost kůži nebo syntetice, textil nasákne.</p>'
          '<h3>Časté chyby při koupi</h3>'
          '<ul><li>Příliš těsná obuv jen proto, že dobře vypadá. Do měsíce ji přestanete nosit.</li>'
          '<li>Koupě nejnovějšího modelu za plnou cenu, i když stejná bota z minulé sezóny stojí podstatně míň.</li>'
          '<li>Očekávání, že tenisky vydrží běh nebo turistiku. Na to jsou určené jiné kategorie.</li></ul>',
)

EXTRA['bezecka-obuv'] = dict(
    intro='<p>Při výběru pomůže i značka: v nabídce najdete Adidas, Asics, Nike, Mizuno, Skechers i La Sportiva, Merrell nebo New Balance. Každá má jiný střih a jiné odpružení, takže dobré zkušenosti s jednou nemusí platit u druhé. Porovnání obchodů vám ukáže, kde je skladem váš model a velikost.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr běžecké obuvi mají {B(("adidas", "Adidas"), ("asics", "Asics"), ("nike", "Nike"), ("mizuno", "Mizuno"), ("skechers", "Skechers"), ("puma", "Puma"), ("la-sportiva", "La Sportiva"), ("merrell", "Merrell"))}. '
          'Asics a Mizuno jsou tradičně spojené s odpružením a stabilitou, La Sportiva a Merrell s terénním během, Nike a Adidas mají širokou řadu od tréninkových po závodní modely.</p>'
          '<h3>Kde se začátečníci nejčastěji spletou</h3>'
          '<ul><li>Příliš těsné boty ve snaze mít „dobrý cit“. Při delším běhu noha otéká a prsty tlačí.</li>'
          '<li>Boty bez odpružení na dlouhé tratě. Měkčí mezipodešev zmírní nárazy na klouby.</li>'
          '<li>Závodní lehké boty na každodenní tréninky. Rychle se opotřebují a víc zatěžují nohy.</li>'
          '<li>Výběr podle barvy. Střih a odpružení rozhodují o pohodlí, ne vzhled.</li></ul>'
          '<h3>Pánské, dámské a dětské boty</h3>'
          '<p>Dámské běžecké boty mají užší patu a často měkčí odpružení, pánské jsou širší. Děti si vystačí s lehkou tréninkovou obuví bez speciálních technologií, hlavně aby jim seděla a měla pružnou podrážku. '
          'Rostoucí chodidlo kontrolujte po čtyřech až šesti měsících.</p>'
          '<h3>Kdy se vyplatí koupit</h3>'
          '<p>Modely minulé sezóny se slevují a liší se většinou barvou a drobnými úpravami. Vyplatí se, když znáte svůj střih a velikost. Pokud boty kupujete poprvé, zkuste je nejdřív v obchodě a pak hledejte nejlepší cenu.</p>',
)

EXTRA['trailove-boty'] = dict(
    intro='<p>Výběr trailové obuvi je užší než u silničních modelů. V nabídce najdete Adidas, Nike, Asics, Skechers, La Sportiva nebo Merrell. Pokud běháte jen občas na lesních cestách, stačí univerzální bota. Na náročnější terén a hory hledejte modely s výztuží a hlubším vzorkem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr trailové obuvi mají {B(("adidas", "Adidas"), ("nike", "Nike"), ("asics", "Asics"), ("skechers", "Skechers"), ("la-sportiva", "La Sportiva"), ("puma", "Puma"), ("merrell", "Merrell"), ("new-balance", "New Balance"))}. '
          'La Sportiva a Merrell jsou spojované s horským terénem, Asics a Nike mají univerzálnější modely pro lesní běh. Střih se liší, proto vždy porovnejte tabulku velikostí.</p>'
          '<h3>Pánské, dámské a dětské trailové boty</h3>'
          '<p>Dámské trailové boty mají užší patu a středovou část a bývají lehčí. Pokud vám sedí unisex nebo pánský střih, nemusíte kupovat dámskou verzi jen kvůli označení. '
          'Pro děti existují lehké terénní boty s hrubším vzorkem, ale na rekreační běhání v lese postačí běžné běžecké boty s dobrým držením paty.</p>'
          '<h3>Jak poznat dobrou trailovou botu</h3>'
          '<ul><li>Pata drží pevně a nevyklouzává ani v prudkém klesání.</li>'
          '<li>Špička je zpevněná a chrání prsty před kameny.</li>'
          '<li>Podrážka drží na mokrém kameni i bahně, ne jen na suchu.</li>'
          '<li>Jazyk je připevněný k bokům, aby se nesunul a nenapadal do něj písek.</li>'
          '<li>Tkaničky se dají schovat do kapsy nebo mají rychloupínací systém.</li></ul>'
          '<h3>Příslušenství k terénnímu běhu</h3>'
          '<p>V terénu se hodí návleky proti kamínkům (gamaše), běžecká vesta s vodou a čelovka na večerní trasy. Doplňky najdete v kategorii <a href="/bezecka-obuv/">běžeckých bot</a> a <a href="/sportovni-obleceni/">sportovního oblečení</a>. '
          'Při delším běhu mějte u sebe vodu a základní vybavení.</p>'
          '<h3>Kdy vyměnit trailové boty</h3>'
          '<p>Trailová bota vydrží přibližně stejně jako silniční, obvykle 600 až 800 km, na tvrdém povrchu méně. Znamením je sjeté hrbolky, ztvrdlá mezipodešev a ztráta přilnavosti na mokru.</p>',
)

EXTRA['trekova-obuv'] = dict(
    intro='<p>Výběr usnadní i značka: v nabídce najdete Merrell, Regatta, Adidas, La Sportiva, CMP, Columbia, Trespass nebo Salomon. Každá má jiný střih a typické použití. Vybírejte podle trasy a ročního období a porovnejte nabídky obchodů, včetně toho, zda mají vaši velikost skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr trekových bot mají {B(("merrell", "Merrell"), ("regatta", "Regatta"), ("adidas", "Adidas"), ("la-sportiva", "La Sportiva"), ("cmp", "CMP"), ("columbia", "Columbia"), ("trespass", "Trespass"), ("salomon", "Salomon"))}. '
          'Salomon a La Sportiva patří k horským značkám, Merrell nabízí pohodlnější střih na každodenní turistiku, Regatta a Trespass pokrývají cenově dostupnější modely.</p>'
          '<h3>Pánské, dámské a dětské trekové boty</h3>'
          '<p>Dámské boty jsou užší v patě a mívají lehčí konstrukci. Pánské jsou širší a robustnější. Dětské trekové boty musí být lehké, s pružnou podrážkou a dobrým držením kotníku. '
          'Děti rychle rostou, proto počítejte s výměnou každý rok nebo dva.</p>'
          '<h3>Ponožky a vložky</h3>'
          '<p>Správné ponožky jsou polovina pohodlí. Na túry se hodí funkční ponožky z merina nebo syntetiky, které odvádějí vlhkost a nevytvářejí puchýře. Bavlněné ponožky nasáknou potem a drhnou. '
          'Pokud vám původní vložka nevyhovuje, zvažte tvarovanou vložku. Ponožky vždy zkoušejte s botami.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Příliš malé boty. Při klesání prsty naráží na špičku a po několika hodinách bolí.</li>'
          '<li>Nerozchozené boty na dlouhou túru. Před výletem je nosit na kratších trasách.</li>'
          '<li>Výběr jen podle vodotěsnosti. V létě je důležitější prodyšnost.</li>'
          '<li>Ignorování zimní obuvi. Na sníh a led nestačí běžná trekovka bez hrubého vzorku.</li></ul>'
          '<h3>Kdy se vyplatí koupit</h3>'
          '<p>Slevy jsou nejvýraznější na konci sezóny. Letní boty bývají levnější na podzim, zimní na jaře. Při koupi s velkou slevou ověřte velikosti a přijetí vrácení, aby případná chyba nezpůsobila vyšší výdaje.</p>',
)

EXTRA['sportovni-obleceni'] = dict(
    intro='<p>V nabídce najdete Adidas, Nike, Puma, Under Armour, Regatta i další značky. Rozdíly jsou ve střihu, odolnosti a ceně: sportovní značky se zaměřují na funkci, módní více na vzhled. Porovnání obchodů ukáže, kde se konkrétní kus prodává nejlevněji a v jaké velikosti.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr sportovního oblečení mají {B(("adidas", "Adidas"), ("nike", "Nike"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("regatta", "Regatta"), ("champion", "Champion"))}. '
          'Under Armour a Nike se zaměřují na výkonnostní trička a legíny, Regatta na outdoorové a cenově dostupné kusy, Champion a Puma na sportovní styl na každý den.</p>'
          '<h3>Pánské, dámské a dětské oblečení</h3>'
          '<p>Dámské střihy jsou užší v pase a širší v bocích, často s jemnějším materiálem. U dětí se vyplatí kupovat o půl velikosti větší, ale ne víc, aby oblečení nepřekáželo při hře. '
          'Dětské sportovní oblečení má být odolné, snadno se prát a mít pružný pas.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Bavlna na intenzivní sport. Nasákne potem a po pár minutách studí.</li>'
          '<li>Příliš těsná velikost. Při pohybu škrtí a drhne.</li>'
          '<li>Zapomenutá první vrstva. V chladu se vyplatí termoprádlo pod ostatním oblečením.</li>'
          '<li>Praní s aviváží. Funkční vlákna se zalepí a přestanou odvádět pot.</li></ul>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Nejvýraznější slevy bývají na konci sezóny a při obměně kolekce. Zimní kusy jsou nejlevnější na jaře, letní na podzim. Sleduje se hlavně cena minulé kolekce, funkčně totožná s novou.</p>',
)

EXTRA['mikiny'] = dict(
    intro='<p>V nabídce najdete mikiny značek Nike, Champion, Adidas, Gap, Fanatics nebo Regatta. Volit můžete mezi klasickými, oversize i funkčními střihy. U každého modelu vidíte srovnání obchodů, takže poznáte, kde je cena nejnižší a jaké velikosti jsou skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr mikin mají {B(("nike", "Nike"), ("champion", "Champion"), ("adidas", "Adidas"), ("gap", "Gap"), ("fanatics", "Fanatics"), ("regatta", "Regatta"), ("rossignol", "Rossignol"), ("new-era", "New Era"))}. '
          'Champion a Gap jsou klasika na každý den, Nike a Adidas dělají sportovní i módní střihy, Fanatics a New Era týmové a klubové mikiny, Rossignol a Regatta funkční kousky na výlety.</p>'
          '<h3>Pánské, dámské a dětské mikiny</h3>'
          '<p>Dámské mikiny bývají kratší a užší, často s dekorativními detaily, pánské delší a širší. Dětské mikiny volte s pružnými manžetami a kvalitním zipem. '
          'Ve škole a na hřišti se hodí odolný materiál, který snese časté praní.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Koupě příliš těsné mikiny. Po praní se bavlna mírně srazí a bude tlačit v ramenou.</li>'
          '<li>Oversize na sport. Volný střih se zachytává a překáží.</li>'
          '<li>Ignorování materiálu. Čistá bavlna na delší sport nevyhovuje, naopak čistý polyester je v chladu méně příjemný.</li></ul>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Na podzim se mikiny kupují nejčastěji a ceny jsou nejvyšší. Slevy se objevují na jaře a v létě, kdy se prodávají zbytky kolekce. Při slevě sledujte, zda je ještě skladem vaše velikost.</p>',
)

EXTRA['leginy'] = dict(
    intro='<p>V nabídce najdete legíny značek Adidas, Asics, Under Armour, Puma, Nike, 4F a české Litex či GymBeam. Rozdíly jsou v materiálu, výšce pasu a střihu. Srovnání obchodů u každého kusu ukáže nejnižší cenu a velikosti, které jsou ještě skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr legín mají {B(("adidas", "Adidas"), ("asics", "Asics"), ("under-armour", "Under Armour"), ("puma", "Puma"), ("litex", "Litex"), ("gymbeam", "GymBeam"), ("4f", "4F"), ("nike", "Nike"))}. '
          'Under Armour a Asics se zaměřují na výkonnostní a kompresní modely, Litex a GymBeam na cenově dostupné legíny na cvičení a každý den, Adidas, Nike a Puma na sportovní styl.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Příliš nízký pas při cvičení. Legíny sjíždějí a musíte je stále upravovat.</li>'
          '<li>Světlá barva bez testu průsvitnosti. Při dřepu pak látka prosvítá.</li>'
          '<li>Bavlněné legíny na intenzivní trénink. Nasáknou potem a ztrácejí tvar.</li>'
          '<li>Špatná velikost. Příliš těsné legíny řežou, příliš volné se sbírají a nedrží.</li></ul>'
          '<h3>Legíny pro děti a těhotné</h3>'
          '<p>Dětské legíny mají být z měkké bavlny s elastanem a pružným pasem bez švů, které dřou. Těhotenské legíny mají vyšší pás přes břicho nebo pružný pás, který se přizpůsobí. '
          'U obou skupin se vyplatí vybírat neprůsvitné barvy a delší střih.</p>'
          '<h3>Jak s legínami kombinovat</h3>'
          '<p>Ke cvičení se hodí s přiléhavým topem nebo funkčním tričkem, ve volném čase s dlouhou mikinou nebo tunikou. V zimě pod kalhoty nebo suknici jako spodní vrstva. '
          'Pokud nosíte legíny pod volné šaty, vyberte tmavé neprůsvitné.</p>',
)

EXTRA['sportovni-kalhoty'] = dict(
    intro='<p>V nabídce najdete kalhoty značek Adidas, Puma, Nike, Kilpi, Rossignol, Peak Mountain i Gap či Celio. Vybírat můžete mezi tepláky, outdoorovými kalhotami i lyžařskými modely. Při výběru porovnáte u každého kusu nabídky obchodů, cenu i dostupnost své velikosti.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr sportovních kalhot mají {B(("celio", "Celio"), ("adidas", "Adidas"), ("peak-mountain", "Peak Mountain"), ("rossignol", "Rossignol"), ("kilpi", "Kilpi"), ("puma", "Puma"), ("gap", "Gap"), ("nike", "Nike"))}. '
          'Kilpi, Peak Mountain a Rossignol jsou známé outdoorovými a lyžařskými kalhotami, Adidas, Puma a Nike tepláky a tréninkovými modely, Celio a Gap civilnějším sportovním stylem.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Příliš těsné outdoorové kalhoty. Při dřepu a stoupání do kopce omezují pohyb.</li>'
          '<li>Zapomenutá vodotěsnost při zimních sportech. Prosáknuté kalhoty rychle prochladnou.</li>'
          '<li>Příliš dlouhé nohavice. Zachytávají se o boty a nasávají vodu.</li>'
          '<li>Bavlněné kalhoty na výlety. Po zmoknutí se dlouho suší.</li></ul>'
          '<h3>Pánské, dámské a dětské kalhoty</h3>'
          '<p>Dámské střihy mají užší pas a širší boky, často s elastickým materiálem. Dětské kalhoty by měly mít nastavitelný pas a zesílená kolena, protože při hře a výletech trpí nejvíc. '
          'U dětí počítejte s kalhotami o jednu velikost větší, nohavice lze přehnout a používat další sezónu.</p>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Lyžařské a zimní kalhoty jsou nejlevnější na jaře, letní outdoorové na konci léta. Při slevě ověřte velikost a přijetí vrácení.</p>',
)

EXTRA['sportovni-kratasy'] = dict(
    intro='<p>V nabídce najdete kraťasy značek Adidas, Nike, Puma, Under Armour, Speedo i Celio. Vybírat můžete mezi běžeckými, fitness, týmovými a volnočasovými modely. U každého páru uvidíte, který obchod ho nabízí nejlevněji a v jaké velikosti.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr sportovních kraťasů mají {B(("adidas", "Adidas"), ("nike", "Nike"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("celio", "Celio"), ("speedo", "Speedo"), ("haglofs", "Haglöfs"))}. '
          'Nike a Adidas mají širokou řadu od běžeckých po basketbalové, Under Armour se zaměřuje na trénink a kompresi, Speedo na plavecké šortky, Haglöfs na outdoorové.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Kraťasy bez vnitřních slipů na delší běh. Dřou a způsobují otlaky.</li>'
          '<li>Příliš krátké kraťasy při míčových sportech. Při pádech nechrání kolena a nevyhovují pravidlům některých týmů.</li>'
          '<li>Bavlněné kraťasy na trénink. Nasáknou a těžknou.</li>'
          '<li>Příliš volný pas bez šňůrky. Při pohybu sjíždějí.</li></ul>'
          '<h3>Pánské, dámské a dětské kraťasy</h3>'
          '<p>Dámské kraťasy bývají kratší a přiléhavější, často s vyšším pasem. Pánské jsou delší a volnější. Dětské by měly mít pružný pas a odolný materiál, aby vydržely hru na hřišti.</p>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Letní kraťasy jsou nejlevnější na konci léta, často za poloviční cenu. Pokud znáte svou velikost, můžete koupit s předstihem na příští sezónu.</p>',
)

EXTRA['sportovni-tricka'] = dict(
    intro='<p>V nabídce najdete trička značek Adidas, Nike, Puma, Under Armour, Gap i Celio. Rozdíly jsou v materiálu a střihu: sportovní značky nabízejí funkční tkaniny, civilní bavlněné směsi. U každého kusu uvidíte srovnání obchodů, takže poznáte, kde je cena nejnižší a které velikosti jsou skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr triček mají {B(("adidas", "Adidas"), ("nike", "Nike"), ("gap", "Gap"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("celio", "Celio"), ("guess", "Guess"))}. '
          'Nike, Adidas a Under Armour jsou spojené s funkčními a tréninkovými tričky, Puma s týmovým stylem, Gap a Celio s civilním stylem na každý den.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Bavlněné tričko na delší běh nebo túru. Nasákne a studí na zádech.</li>'
          '<li>Příliš volné tričko pod batoh. Sbírá se a drhne.</li>'
          '<li>Zanedbání UV ochrany na horách a u vody. Pokožka se spálí i přes oblečení.</li>'
          '<li>Praní s aviváží. Funkční trička přestávají odvádět pot.</li></ul>'
          '<h3>Pánská, dámská a dětská trička</h3>'
          '<p>Dámská trička mají užší střih a zakulacený lem, pánská jsou rovnější. Dětská trička kupujte z měkkého materiálu bez štítku, který dře. '
          'U sportu a hry se hodí funkční tričko, které rychleji schne než bavlněné.</p>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Letní trička jsou nejlevnější na konci léta, často v balíčcích po více kusech. Základní barvy se vyplatí kupovat s předstihem.</p>',
)

EXTRA['teplaky'] = dict(
    intro='<p>V nabídce najdete tepláky značek Adidas, Puma, Under Armour, Champion, Gap, 4F i Nike. Vybírat můžete mezi klasickými, zúženými i volnými střihy. Vedle sebe uvidíte ceny z více obchodů i to, jaké velikosti jim ještě zbývají.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr tepláků mají {B(("adidas", "Adidas"), ("puma", "Puma"), ("gap", "Gap"), ("under-armour", "Under Armour"), ("champion", "Champion"), ("4f", "4F"), ("nike", "Nike"))}. '
          'Adidas a Puma jsou klasika na každý den i na trénink, Champion a Gap mají měkké bavlněné směsi, Under Armour funkční modely na výkon.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Příliš volné tepláky na sport. Zachytávají se a překáží při pohybu.</li>'
          '<li>Příliš dlouhé nohavice bez manžety. Zamotají se pod boty a nasávají vodu.</li>'
          '<li>Bavlněné tepláky na intenzivní trénink. Po zpocení těžknou.</li>'
          '<li>Neověřená velikost. Střihy se liší, takže stejné písmeno značky A a B neznamená totéž.</li></ul>'
          '<h3>Pánské, dámské a dětské tepláky</h3>'
          '<p>Dámské tepláky mají užší střih a často vyšší pas, pánské jsou rovnější. Dětské by měly mít odolná kolena a pružný pas bez drhnoucích švů. '
          'U dětí počítejte s jednou velikostí navíc, nohavice lze přehnout.</p>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Zateplené tepláky se nejvýrazněji slevují na jaře. Základní modely mívají dlouhodobě stabilní cenu, vyplatí se hlavně sledovat slevy minulých kolekcí.</p>',
)

EXTRA['plavky'] = dict(
    intro='<p>V nabídce najdete plavky značek Speedo, Arena, Adidas, Nike a další. Speedo a Arena se zaměřují na sportovní plavání a závody, ostatní značky nabízejí i plážové modely. U plavek je dostupnost velikostí stejně důležitá jako cena, proto vidíte obojí vedle sebe.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr plavek mají {B(("speedo", "Speedo"), ("arena", "Arena"), ("trendyol", "Trendyol"), ("adidas", "Adidas"), ("litex", "Litex"), ("nike", "Nike"), ("decathlon", "Decathlon"))}. '
          'Speedo a Arena patří mezi značky sportovního plavání, Litex nabízí české cenově dostupné plavky, Adidas a Nike plážové i sportovní.</p>'
          '<h3>Časté chyby při výběru</h3>'
          '<ul><li>Plážové plavky na pravidelné plavání. V chlóru rychle ztratí barvu a elastičnost.</li>'
          '<li>Příliš velká velikost. Mokré plavky se natáhnou a při skoku sjíždějí.</li>'
          '<li>Sušení na slunci nebo topení. Elastan se poškodí a barva vyblednou.</li>'
          '<li>Volné šortky do bazénu. V řadě provozů nejsou povolené.</li></ul>'
          '<h3>Plavky pro menstruaci</h3>'
          '<p>Menstruační plavky mají vestavěnou savou vrstvu a jsou určené pro lehčí dny. Při jejich výběru sledujte popis výrobce, udávaný objem a dobu nošení, a řiďte se pokyny pro praní. '
          'Pokud si nejste jistá, poraďte se s lékařem nebo gynekologem.</p>'
          '<h3>Příslušenství k plavání</h3>'
          '<p>K plavání patří <a href="/plavecke-bryle/">plavecké brýle</a>, čepice a osuška, na pláž <a href="/plazove-doplnky/">plážové doplňky</a>. Plavecké brýle vybírejte podle tvaru obličeje, zkušenosti s plaváním a potřeby UV filtru.</p>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Plavky jsou nejlevnější koncem léta a na podzim. Pokud znáte svou velikost a střih, vyplatí se koupit s předstihem na příští sezónu.</p>',
)

EXTRA['jizdni-kola'] = dict(
    intro='<p>Na Sportece porovnáte nabídky obchodů u kol značek Author, Dino, Davi, Specialized, Kellys nebo Trek. Rozhodující jsou velikost rámu, typ a výbava, ne jen cena. Pokud si nejste jistí, začněte velikostní tabulkou a vyzkoušejte kolo v obchodě.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr kol mají značky {B(("author", "Author"), ("dino", "Dino"), ("davi", "Davi"), ("specialized", "Specialized"), ("engwe", "Engwe"), ("dino-bikes", "Dino Bikes"), ("kellys", "Kellys"), ("trek", "Trek"))}. '
          'Author a Kellys jsou české značky s širokou nabídkou, Specialized a Trek patří mezi světové výrobce, Dino a Davi jsou zaměřené na dětská kola.</p>'
          '<h3>Časté chyby při koupi kola</h3>'
          '<ul><li>Příliš velký nebo malý rám. Způsobuje bolesti zad, krku a zápěstí.</li>'
          '<li>Výběr podle počtu převodů. Kvalita brzd, kol a rámu je důležitější.</li>'
          '<li>Koupě horského kola na asfalt. Široké pláště a odpružení zbytečně zpomalují.</li>'
          '<li>Žádná zkušební jízda. Posez a geometrie rámu se u značek liší.</li>'
          '<li>Opomenutí servisu. Kolo vyžaduje pravidelnou údržbu, jinak rychle stárne.</li></ul>'
          '<h3>Kde kolo koupit a jak ho nastavit</h3>'
          '<p>V kamenném obchodě kolo seřídí a nastaví výšku sedla, na internetu často přijde zabalené a je třeba ho dotáhnout a seřídit. U online koupě počítejte s návštěvou servisu. '
          'Základní nastavení: sedlo ve výšce, kdy má noha při dolní poloze pedálu mírně pokrčené koleno, řídítka podle pohodlí zad.</p>'
          '<h3>Údržba kola</h3>'
          '<p>Pravidelně kontrolujte tlak v pláštích, brzdy a řetěz. Řetěz mažte po každém mytí nebo po jízdě v dešti. Jednou ročně nechte kolo zkontrolovat v servisu, '
          'ušetříte tak výdaje za větší opravy. Součástky najdete v kategorii <a href="/cyklo-dily/">cyklo díly</a>.</p>'
          '<h3>Kdy se vyplatí koupit</h3>'
          '<p>Kola se nejvíc slevují na podzim a v zimě, kdy obchody uvolňují místo nové sezóně. Slevy se týkají hlavně modelů předchozího roku. Na jaře jsou ceny nejvyšší a výběr velikostí nejmenší.</p>',
)

EXTRA['elektrokola'] = dict(
    intro='<p>V nabídce najdete elektrokola značek Engwe, Fafrees, Specialized, Samebike, DYU a Hitway. Rozdíly jsou ve výkonu, baterii, hmotnosti a servisu. Porovnání obchodů ukáže, kde je nejnižší cena a které modely jsou skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>V nabídce Sporteky najdete elektrokola značek {B(("engwe", "Engwe"), ("fafrees", "Fafrees"), ("specialized", "Specialized"), ("samebike", "Samebike"), ("dyu", "DYU"), ("hitway", "Hitway"), ("olpran", "Olpran"), ("urlife", "Urlife"))}. '
          'Specialized patří mezi světové výrobce kol, ostatní značky se zaměřují na cenově dostupnější městská a skládací elektrokola. Před koupí ověřte dostupnost servisu a záruku na baterii.</p>'
          '<h3>Časté chyby při koupi elektrokola</h3>'
          '<ul><li>Výběr jen podle ceny. Levný motor a baterie bez servisní sítě mohou způsobit potíže při první poruše.</li>'
          '<li>Podcenění hmotnosti. Těžké kolo se hůř nosí do sklepa i zvedá na nosič.</li>'
          '<li>Příliš malá baterie. Dojezd je v praxi nižší než v katalogu, hlavně v kopcích a v zimě.</li>'
          '<li>Opomenutí zámku. Elektrokolo je častý cíl krádeže, vyplatí se kvalitní zámek a pojištění.</li></ul>'
          '<h3>Péče o baterii</h3>'
          '<p>Baterii nabíjejte při pokojové teplotě a neskladujte ji dlouho zcela vybitou ani plně nabitou. Při delším uskladnění nechte nabití zhruba na polovinu. '
          'V zimě nechte baterii před jízdou ohřát v teple, mráz snižuje dojezd. Používejte originální nabíječku.</p>'
          '<h3>Pro koho je elektrokolo</h3>'
          '<p>Elektrokolo se hodí pro dojíždění do práce, kopcovitý terén, delší výlety, rodiny s dětmi nebo seniory. Zvládnou ho i méně trénovaní jezdci, a protože při šlapání pomáhá, můžete jezdit déle a častěji. '
          'Sportovní jezdci využijí elektrické horské kolo na delší trasy v terénu.</p>'
          '<h3>Kdy se vyplatí koupit</h3>'
          '<p>Slevy jsou nejvýraznější na podzim a v zimě. Elektrokola se u některých obchodů prodávají i na splátky, porovnejte celkovou cenu včetně úroků a poplatků.</p>',
)

EXTRA['cyklistika'] = dict(
    intro='<p>V nabídce najdete vybavení značek Rockbros, Force, Shimano, Silvini, Topeak, Max1, Author a Alpina. Rozhodnutí o značce je až druhé: nejdřív určete, co potřebujete, a pak porovnejte nabídky obchodů a velikosti skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr cyklistického vybavení mají {B(("rockbros", "Rockbros"), ("force", "Force"), ("shimano", "Shimano"), ("silvini", "Silvini"), ("topeak", "Topeak"), ("max1", "Max1"), ("author", "Author"), ("alpina", "Alpina"))}. '
          'Shimano je známý výrobce převodů a brzd, Topeak nabízí nářadí a příslušenství, Force a Max1 cenově dostupné doplňky, Silvini cyklistické oblečení a Alpina helmy a brýle.</p>'
          '<h3>Časté chyby při výběru vybavení</h3>'
          '<ul><li>Šetření na helmě. Chrání nejcennější část těla.</li>'
          '<li>Slabý zámek. Tenké řetízky a lanka se dají rychle přeříznout.</li>'
          '<li>Světla s nízkým výkonem. Za tmy musíte vidět i být viděn.</li>'
          '<li>Opomenutí rukavic a brýlí. Chrání při pádu a před hmyzem a prachem.</li></ul>'
          '<h3>Příslušenství pro rodiny a děti</h3>'
          '<p>Pro děti se vyplatí odrážedla a lehká kola, dětské helmy s nastavitelným řemínkem a reflexní prvky. Nejmenší převezete v sedačce nebo vozíku, viz <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>. '
          'Před jízdou zkontrolujte, zda helma sedí a zda je dítě bezpečně připoutáno.</p>'
          '<h3>Kdy se vyplatí nakupovat</h3>'
          '<p>Cyklistické vybavení se nejvíc slevuje na podzim a v zimě. Základní věci jako světla, zámky a nářadí mají stabilní ceny, u oblečení a helem sledujte slevy minulých kolekcí.</p>',
)


# --- second pass: shortest guides get one more concrete section each ---
EXTRA['sportovni-kratasy']['guide'] += ('<h3>Kraťasy podle sportu</h3>'
    '<p>Cyklistické kraťasy s vložkou najdete mezi <a href="/cyklisticke-obleceni/">cyklistickým oblečením</a>, plavecké šortky mezi <a href="/plavky/">plavkami</a>. Pro běh vybírejte kraťasy bez objemných švů na vnitřní straně stehen, '
    'pro posilování pevnější materiál, který se při dřepu neprotahuje. Co dát do kapes: klíče a kartu do kapsy na zip, telefon do zadní nebo bederní kapsy, jinak se při běhu pohybuje a dře.</p>'
    '<p>Pokud kraťasy zkoušíte doma, udělejte dřep, výpad a několik kroků po schodech. U dobrých kraťasů se nohavice při pohybu nezvedá a pas neklouže.</p>')
EXTRA['sportovni-tricka']['guide'] += ('<h3>Dlouhý rukáv, tílka a polokošile</h3>'
    '<p>Tričko s dlouhým rukávem je vhodné na chladnější dny a jako spodní vrstva, <a href="/tilka/">tílka</a> na horké dny a posilování, <a href="/polokosile/">polokošile</a> na golf, tenis a volný čas. '
    'Při běhu za slunečných dnů pomáhá tričko s UV ochranou nebo světlé barvy, které odrážejí teplo.</p>'
    '<p>Na vícedenní túru je praktické merino, které se nemusí prát po každé etapě. Na krátký trénink stačí lehký polyester, který se usuší přes noc.</p>')
EXTRA['sportovni-kalhoty']['guide'] += ('<h3>Jak otestovat kalhoty před koupí</h3>'
    '<p>Udělejte hluboký dřep, výpad a zvedněte koleno k hrudi. Kalhoty se nesmí napínat v rozkroku, pas nesmí sjíždět a nohavice se nesmí zachytávat o boty. U outdoorových kalhot zkontrolujte, '
    'zda kapsy na zip jdou otevřít s rukavicemi a zda je pás nastavitelný. Pro lyžařské kalhoty zkuste je přes termoprádlo a lyžařské boty.</p>')
EXTRA['teplaky']['intro'] += '<p>Tepláky se dají kombinovat s <a href="/mikiny/">mikinou</a> do kompletní soupravy nebo nosit samostatně s tričkem.</p>'
EXTRA['teplaky']['guide'] += ('<h3>Souprava, nebo samostatné tepláky</h3>'
    '<p>Kompletní <a href="/soupravy/">souprava</a> se stejnou barvou a látkou působí jednotně a hodí se do posilovny i na cestování. Samostatné tepláky lépe zkombinujete s různými mikinami a tričky a při praní vydrží déle, '
    'protože se nemusí prát stejně často jako mikina. Pokud kupujete soupravu, ověřte, že jednotlivé díly lze zakoupit i samostatně.</p>')
EXTRA['cyklistika']['intro'] += '<p>Pro začátečníky se vyplatí začít helmou, světly a zámkem a teprve potom řešit speciální oblečení a doplňky.</p>'
EXTRA['cyklistika']['guide'] += ('<h3>Jak začít s cyklistikou</h3>'
    '<p>Nejdřív vyberte kolo podle terénu, který budete jezdit, pak helmu, světla a zámek. Oblečení nechte na později: na krátké jízdy stačí běžné sportovní, na delší pak kalhoty s vložkou a dres. '
    'Začněte kratšími trasami a postupně přidávejte. Pokud hledáte společnost, v řadě měst existují cyklistické skupiny pro začátečníky.</p>')
EXTRA['mikiny']['guide'] += ('<h3>Mikina pod bundu, nebo samostatně</h3>'
    '<p>Pod zimní bundu se hodí tenká přiléhavá mikina nebo fleece, která nenabírá objem. Samostatně nosíte tlustší a volnější. Při sportu v chladu zkombinujte tričko, tenkou mikinu a vnější vrstvu proti větru, '
    'mikinu snadno sundáte a uložíte do batohu.</p>')
EXTRA['bezecka-obuv']['guide'] += ('<h3>Jak si boty vyzkoušet</h3>'
    '<p>Zkoušejte je s ponožkami, ve kterých poběžíte, odpoledne, na obou nohách. Projděte se po obchodě, popoběhněte a zkontrolujte, zda pata vyklouzává a špička nenarážá. '
    'Pokud kupujete na internetu, vyzkoušejte je doma na koberci a zachovejte krabici, aby šlo boty případně vrátit.</p>')
EXTRA['trailove-boty']['guide'] += ('<h3>Trailové boty a ponožky</h3>'
    '<p>Na terén jsou vhodné ponožky z merina nebo syntetiky, které se nerolují a odvádějí pot. U delších běhů pomáhají tenké bezešvé modely a ponožky s ochranou paty a špičky. '
    'Bavlněné ponožky nasáknou a způsobují puchýře, proto je v terénu raději nepoužívejte.</p>')
