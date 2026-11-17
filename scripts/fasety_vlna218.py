"""sporteka.cz — facet landing texts wave 218 (gender facets of transitional jackets, quilted jackets and hiking backpacks):
panska-podzimni-bunda, detska-podzimni-bunda, damska-prosivana-bunda, detsky-turisticky-batoh, damsky-turisticky-batoh.
Assortment described from the live catalogue copy (brands and model names as they appear in product names).
Sources checked: EN 14682:2014 cords and drawstrings on children's clothing (no cords in hood/neck area up to 7 years / 134 cm;
productip.com, SGS, BSI), MA-1 developed for the US Air Force in the 1950s with an orange lining for signalling and M-65 field jacket
introduced 1965 replacing the M-1951 (Wikipedia, Alpha Industries), sewn-through vs box-baffle construction (OutdoorGearLab buying advice),
Deuter fits SL / regular / EL with back lengths ~42 / 46 / 50 cm and kids' packs from two years (deuter.com advice pages), Deuter Fox
VariQuick back-length adjustment (deuter.com, REI), Osprey torso measurement C7 to iliac crest (osprey.com size & fit), Osprey Kyte as the
women's counterpart of Kestrel and Tempest of Talon (REI, retailer listings), Osprey Daylite Jr. age range (osprey.com),
backpack load around a tenth of a child's body weight as a common guideline (Cleveland Clinic, Healthline; stated as a guideline only).
No prices, counts, stock claims, no medical promises."""
from texty_vlna1a import T

NEW = {}

# ------------------------------------------------------------------ panska-podzimni-bunda
NEW['panska-podzimni-bunda'] = dict(
    title='Pánská podzimní bunda: softshell, větrovka, zateplená',
    desc='Pánské podzimní bundy: softshell, větrovka, lehce zateplená, bomber i polní bunda. Jak vybrat typ, materiál, střih a velikost na přechodné období.',
    intro='<p><strong>Pánská podzimní bunda</strong> má těžkou práci. V září stačí, když zastaví vítr, v listopadu už musí hřát, odolat dešti a vejít se pod ni teplá mikina. '
          'Proto se pod jedním názvem skrývá několik dost odlišných typů: softshell, lehká větrovka, nepromokavá bunda s membránou, tence zateplená bunda nebo hybrid, ale i městský bomber a polní bunda ve vojenském stylu. '
          'Na této stránce jsou pánské modely z kategorie <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> a jejich nabídky z českých obchodů. '
          'Průvodce vysvětluje, jak se jednotlivé typy chovají ve větru a v dešti, podle čeho číst parametry, jak vybrat pánský střih a velikost a jak o bundu pečovat, aby vydržela několik sezon. '
          'Pokud už víte, že chcete pružný softshell, pokračujte rovnou na stránku <a href="/softshellova-bunda-panska/">pánská softshellová bunda</a>. Na mrazivé dny jsou tu <a href="/panska-zimni-bunda/">pánské zimní bundy</a>.</p>',
    guide='<h2>Jaké typy pánských podzimních bund existují</h2>'
          '<p>Název podzimní bunda neříká nic o konstrukci. Rozhoduje, jestli bunda stojí na pružném materiálu, na membráně, nebo na tenké výplni. Každý typ se hodí na jinou část podzimu a na jiný způsob pohybu.</p>'
          + T(['Typ', 'Co umí', 'Slabina'], [
              ['softshell', 'pruží, dobře dýchá, zastaví většinu větru, krátkou přeháňku vydrží', 'v dlouhém dešti promokne, sám o sobě moc nehřeje'],
              ['větrovka', 'velmi lehká, sbalí se do kapsy, chrání před větrem', 'proti dešti a chladu nestačí'],
              ['bunda s membránou', 'drží déšť i vítr, šustí, mívá podlepené švy', 'při rychlé chůzi se pod ní člověk zapotí víc'],
              ['lehce zateplená bunda', 'tenká syntetická nebo péřová výplň, hřeje i na chladné ráno', 'většinou jen odpuzuje vodu, nepromokavá není'],
              ['hybridní bunda', 'zateplený trup a pružné boky nebo rukávy', 'v dešti a na zastávce v mrazu nestačí'],
              ['bomber a polní bunda', 'městský vzhled, odolná látka, často odepínací vložka', 'na túru je těžší a méně prodyšná']]) +
          '<p>Kdo potřebuje jednu bundu na všechno, většinou skončí u lehce zateplené bundy s odolným vrchním materiálem, nebo u nepromokavé bundy, pod kterou si podle počasí oblékne mikinu. '
          'Kdo se hodně hýbe, na kole, při běhu nebo na túře, vystačí si se softshellem a v batohu nosí tenkou <a href="/nepromokave-bundy/">nepromokavou bundu</a> pro případ deště.</p>'
          '<h2>Podzim po měsících: jak skládat vrstvy</h2>'
          '<p>Září bývá teplé přes den a chladné večer. Na procházku nebo cestu do práce stačí větrovka nebo tenký softshell přes tričko. V říjnu přibývá deště a větru, takže se vyplatí bunda, která drží vodu, a pod ní tenká <a href="/fleecove-mikiny/">fleecová mikina</a>. '
          'V listopadu teploty klesají k nule a i podzimní bunda pak potřebuje teplou vrstvu. Buď zvolíte zateplený model, nebo kombinaci nepromokavé skořepiny a <a href="/panska-funkcni-mikina/">funkční mikiny</a>. Velmi praktická je i <a href="/panske-vesty/">pánská vesta</a>, která zahřeje trup a nesvazuje ruce.</p>'
          '<p>Vrstvení má jednu výhodu: jednotlivé kusy se dají odložit. Zateplená bunda se v teplém odpoledni nedá nijak ztenčit, zatímco ze skořepiny a mikiny sundáte tu vrstvu, která právě přebývá.</p>'
          '<h2>Parametry, které čtěte v popisu</h2>'
          '<ul><li><strong>Vodní sloupec</strong> se udává v milimetrech a říká, jaký tlak vody látka vydrží, než propustí kapku. Vyšší číslo znamená spolehlivější ochranu v dlouhém dešti.</li>'
          '<li><strong>Prodyšnost</strong> se uvádí v gramech vodní páry na metr čtvereční za 24 hodin. Čím víc, tím snáz pot uniká ven.</li>'
          '<li><strong>Podlepené švy</strong> jsou nutné, pokud má bunda opravdu nepromokat. Jinak voda proteče dírkami po jehle.</li>'
          '<li><strong>Vodoodpudivá úprava</strong> na povrchu látky způsobí, že voda stéká v kapkách. Časem slábne a dá se obnovit.</li>'
          '<li><strong>Typ výplně</strong> u zateplených modelů: syntetika hřeje i vlhká, peří je lehčí, ale mokro mu nesvědčí.</li></ul>'
          '<p>Pokud obchod parametry neuvádí, berte bundu spíš jako odolnou proti větru a krátké přeháňce. Slova jako voděodolná nebo water resistant obvykle znamenají jen povrchovou úpravu, ne membránu.</p>'
          '<h2>Pánský střih a velikost</h2>'
          '<p>Pánské bundy počítají se širšími rameny, delšími rukávy a rovnějším trupem. Sportovní modely bývají střižené těsněji, aby pod nimi nebyl zbytečný vzduch, městské a polní bundy volněji. '
          'Velikost zkoušejte s tím, co pod bundu budete nosit. Kdo plánuje v listopadu mikinu, musí ji mít na sobě i při zkoušení. Předpažte, zvedněte ruce nad hlavu a zkuste se předklonit: rukáv by neměl vyjet nad zápěstí a záda by se neměla odhalit.</p>'
          '<p>Kapuce má jít stáhnout tak, aby při otočení hlavy neomezovala výhled. Kdo jezdí na kole nebo na koloběžce, ocení prodloužená záda. Pro cyklisty jsou ale vhodnější přímo <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>, které mají střih do předklonu.</p>'
          '<h2>Bunda na túru a do hor</h2>'
          '<p>Na podzimní túře se střídá výstup, kdy je člověku horko, s vrcholem, kde fouká a teplota je o několik stupňů nižší než v údolí. Turistická bunda proto potřebuje odvětrání. Nejpraktičtější jsou zipy v podpaží, kterými se pustí pára ven bez rozepínání celé bundy. '
          'Kapsy mají být umístěné výš, aby šly otevřít i s utaženým bederním pásem batohu. Kapuce má mít kšilt, který drží déšť mimo obličej, a stahování vzadu, aby se otáčela spolu s hlavou. '
          'Pod bundu si na túru vezměte funkční tričko místo bavlněného, které nasákne potem a na větru studí. K bundě se hodí <a href="/panske-outdoorove-kalhoty/">pánské outdoorové kalhoty</a>, které vydrží vítr a lehký déšť a nebrání v kroku.</p>'
          '<h2>Bomber a polní bunda: vojenské vzory ve městě</h2>'
          '<p>Mezi podzimními bundami najdete i dva klasické střihy, které vznikly pro armádu. Bomber MA-1 byl vyvinut pro americké letectvo v padesátých letech minulého století jako lehčí letecká bunda. Typická je pro něj oranžová podšívka, která měla po obrácení bundy naruby pomoci záchranářům sestřeleného pilota najít. '
          'Polní bunda M-65 dostala jméno podle roku 1965, kdy ji americká armáda zavedla jako náhradu staršího vzoru M-1951. Má čtyři velké kapsy na přední straně, stojáček se schovanou kapucí a často odepínací zateplovací vložku.</p>'
          '<p>V nabídce se tyto střihy objevují pod jmény jako MA-1 nebo M65 od výrobců vojenského a volnočasového oblečení. Na podzim se nosí dobře, ve městě vydrží hodně. Na túru se ale hodí méně, protože bývají těžší a méně prodyšné než sportovní bundy.</p>'
          '<h2>Značky, které v nabídce uvidíte</h2>'
          '<p>Turistické a outdoorové pánské bundy nabízí řada značek. Často uvidíte <a href="/znacka/regatta/">Regatta</a>, Trespass a Peak Mountain, ze střední Evropy <a href="/znacka/northfinder/">Northfinder</a>, Hannah a Kilpi, ze severských značek <a href="/znacka/haglofs/">Haglöfs</a> a Helly Hansen. '
          'Na horské sporty se zaměřují Dynafit, Salewa a La Sportiva, k nim přibývají The North Face, Columbia a Craft. Sportovní tréninkové bundy mají v nabídce hlavně Nike, Adidas, Puma a Under Armour. '
          'Mitchell & Ness a podobné značky dodávají bundy s logy týmů z NBA, NHL nebo MLB, které jsou spíš módním kouskem než oblečením do terénu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Softshell do deště.</strong> Pružný materiál vydrží přeháňku, při celodenním dešti ale promokne. Na deštivé dny potřebujete membránu.</li>'
          '<li><strong>Příliš teplá bunda.</strong> Kdo chodí rychle nebo jezdí na kole, se v zateplené bundě potí a pak mu je zima. Lepší je tenčí bunda a mikina pod ni.</li>'
          '<li><strong>Velikost bez mikiny.</strong> Bunda, která sedí jen na tričko, bude v listopadu s mikinou pod ní těsná.</li>'
          '<li><strong>Zapomenutá kapuce.</strong> Bez kapuce musíte v dešti nosit čepici nebo deštník. U městské bundy to nevadí, u turistické ano.</li></ul>'
          '<h2>Péče o podzimní bundu</h2>'
          '<p>Nejvíc bundě ublíží změkčovač aviváže a horká voda. Membránové a softshellové bundy perte na nízkou teplotu v prostředku určeném pro funkční oblečení, s vypnutým odstřeďováním nebo jen na nízké otáčky, a se zapnutými zipy. '
          'Když voda přestane po povrchu stékat v kapkách a látka se začne nasávat, obnovte vodoodpudivou úpravu přípravky z kategorie <a href="/impregnace/">impregnace</a>. Zateplené bundy sušte rozložené, péřové ideálně v sušičce na nízkou teplotu. Na léto bundu uložte čistou a suchou na ramínko, ne zmačkanou ve skříni.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Nejdřív si ujasněte typ, potom hledejte konkrétní parametry a teprve nakonec barvu. U stejného modelu se nabídky často liší jen odstínem nebo velikostí, kterou obchod právě má. Sporteka sdružuje nabídky českých e-shopů na jednom místě, nákup dokončíte v obchodě, který si vyberete. '
          'Dámské modely najdete na stránce <a href="/jarni-a-podzimni-bundy-damske/">dámské jarní a podzimní bundy</a>, dětské pod odkazem <a href="/detska-podzimni-bunda/">dětská podzimní bunda</a>. Kdo chce pod bundu hlavně teplo, může se podívat na <a href="/panska-perova-bunda/">pánské péřové bundy</a> nebo na kategorii <a href="/prosivane-bundy/">prošívané bundy</a>.</p>',
    faq=[
        ('Jakou pánskou bundu na podzim vybrat?', 'Na začátek podzimu stačí softshell nebo větrovka. Na deštivý říjen a listopad je lepší bunda s membránou a mikinou pod ní, nebo lehce zateplená bunda. Rozhoduje, jak moc se v ní budete hýbat.'),
        ('Je softshell nepromokavý?', 'Většinou ne. Softshell má vodoodpudivou úpravu a krátkou přeháňku vydrží, v dlouhém dešti ale promokne. Výjimkou jsou modely s membránou, které to mají uvedené v popisu.'),
        ('Co znamená vodní sloupec u bundy?', 'Udává v milimetrech, jaký tlak vody látka vydrží, než začne propouštět. Vyšší číslo znamená spolehlivější ochranu. Pro nepromokavost jsou ale stejně důležité podlepené švy.'),
        ('Jaký je rozdíl mezi podzimní a zimní bundou?', 'Podzimní bunda je lehčí a má méně výplně, nebo žádnou. Spoléhá na vrstvy pod ní. Zimní bunda je silně zateplená a hřeje i bez mikiny, na podzim je v ní ale často horko.'),
        ('Co je hybridní bunda?', 'Bunda, která kombinuje zateplené části, obvykle na trupu, s pružným a prodyšným materiálem na bocích nebo rukávech. Hodí se na pohyb v chladu, kdy klasická zateplená bunda přehřívá.'),
        ('Jak vybrat velikost pánské bundy?', 'Zkoušejte ji s vrstvou, kterou pod ní budete nosit. Při předpažení nemá rukáv vyjet nad zápěstí a při předklonu se nemají odhalit záda. Řiďte se obvodem hrudníku v tabulce obchodu.'),
        ('Hodí se bomber na túru?', 'Spíš ne. Bomber a polní bundy bývají těžší a méně prodyšné, jsou určené hlavně do města. Na túru je lepší softshell nebo lehká bunda s membránou.'),
        ('Kdy vznikla bunda M-65?', 'Polní bunda M-65 nese jméno podle roku 1965, kdy ji zavedla americká armáda. Nahradila starší vzor M-1951. Dnes ji vyrábí řada značek v civilní verzi.'),
        ('Jak prát podzimní bundu s membránou?', 'Na nízkou teplotu v prostředku na funkční oblečení, bez aviváže a se zapnutými zipy. Když voda přestane stékat po povrchu, obnovte vodoodpudivou úpravu impregnací.'),
        ('Kde porovnat nabídky pánských podzimních bund?', 'Na této stránce vidíte nabídky českých obchodů vedle sebe. Nákup dokončíte v e-shopu, kde ještě ověříte parametry, velikost a dostupnou barvu.'),
    ])

# ------------------------------------------------------------------ detska-podzimni-bunda
NEW['detska-podzimni-bunda'] = dict(
    title='Dětská podzimní bunda: softshell, do deště, zateplená',
    desc='Dětské podzimní bundy do školky, školy i na výlety: softshell, nepromokavé, lehce zateplené. Velikost podle výšky, bezpečnost a péče.',
    intro='<p><strong>Dětská podzimní bunda</strong> to má těžší než bunda pro dospělého. Prolézá s dítětem křoví, válí se v listí, klouže po mokré skluzavce a za rok je většinou malá. '
          'Musí přitom chránit před větrem a deštěm, nepřehřívat při běhání a dát se snadno vyprat. '
          'Na této stránce jsou dětské modely z kategorie <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> s nabídkami z českých obchodů: softshellové bundy, nepromokavé bundy do deště, lehce zateplené a prošívané bundy i sportovní bundy na trénink. '
          'Průvodce radí, jak vybrat typ podle věku a podle toho, kde dítě bundu nosí, jak určit velikost podle výšky, na co si dát pozor kvůli bezpečnosti a jak bundu udržet v dobré kondici. '
          'Pokud chcete rovnou pružný softshell, pokračujte na stránku <a href="/detska-softshellova-bunda/">dětská softshellová bunda</a>. Na mrazy jsou určené <a href="/detska-zimni-bunda/">dětské zimní bundy</a>.</p>',
    guide='<h2>Jaký typ bundy na co</h2>'
          '<p>Dítě se v bundě pohybuje jinak než dospělý. Neustále se zahřívá a zase chladne, sedá si na zem a strká ruce do louží. Proto je dobré vybírat typ podle toho, kde bude bundu nosit nejčastěji.</p>'
          + T(['Kde dítě bundu nosí', 'Vhodný typ', 'Na co se dívat'], [
              ['školka, pískoviště, les', 'nepromokavá bunda nebo softshell s membránou', 'odolný materiál, kapuce, zesílené lokty'],
              ['cesta do školy', 'lehce zateplená bunda nebo softshell', 'reflexní prvky, kapsy na zip'],
              ['výlet s rodiči', 'softshell a v batohu bunda do deště', 'nízká hmotnost, sbalitelnost'],
              ['trénink a hřiště', 'sportovní bunda nebo větrovka', 'volnost v ramenou, prodyšnost'],
              ['studený listopadový den', 'zateplená nebo prošívaná bunda', 'délka přes bedra, manžety, které nepouští vítr']]) +
          '<p>Pro nejmenší děti, které tráví hodně času na zemi, se na podzim osvědčují nepromokavé soupravy, tedy bunda s kalhotami s laclem. Kalhoty najdete také v kategorii <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>. Školáci, kteří se do bláta tolik nedostanou, vystačí s bundou a běžnými kalhotami.</p>'
          '<h2>Softshell, membrána, nebo zateplení?</h2>'
          '<p>Dětský softshell je pružný a prodyšný, zvenku má vodoodpudivou úpravu a uvnitř často tenký fleece. Dítě v něm může běhat bez pocení a krátký déšť mu nevadí. Na celodenní pobyt venku v mokru ale nestačí, protože se při delším kontaktu s vodou, například při sezení na mokré lavičce, začne nasávat. '
          'Bunda s membránou a podlepenými švy drží vodu spolehlivě, šustí a méně pruží. Lehce zateplená bunda s tenkou syntetickou výplní je dobrá na chladná rána a na děti, které se tolik nehýbou, například v kočárku nebo na sedačce kola.</p>'
          '<p>Na většinu podzimu se dá použít kombinace: lehčí bunda a pod ní mikina nebo <a href="/detske-vesty/">dětská vesta</a>. Když se oteplí, vrstva zmizí v batohu. V chladu pomůže tenké <a href="/detske-termopradlo/">dětské termoprádlo</a>, které odvádí pot a dítě se v něm méně podchladí.</p>'
          '<h2>Velikost podle výšky</h2>'
          '<p>Dětské oblečení se nejčastěji značí výškou dítěte v centimetrech, například 110, 116 nebo 128. Některé značky používají věk v letech, třeba 5–6 Y, a obchody pak přidávají převodní tabulku. Spolehlivější je výška, protože děti stejného věku se mohou lišit o celé číslo. '
          'Dítě změřte bez bot a vyberte velikost, která odpovídá aktuální výšce nebo je o číslo větší. Větší rezerva se nevyplácí: dlouhé rukávy padají přes dlaně, bunda se shrnuje a víc do ní fouká. Řada výrobců dětských bund proto přidává do rukávů manžety, které se dají vyhrnout nebo stáhnout suchým zipem.</p>'
          '<p>Při zkoušení nechte dítě zvednout ruce nad hlavu a dřepnout si. Bunda má zakrývat bedra i v podřepu a rukáv má zůstat na zápěstí.</p>'
          '<h2>Bezpečnost: šňůrky, kapuce, reflexní prvky</h2>'
          '<p>U dětského oblečení se sleduje, zda šňůrky a tkanice nemohou dítě ohrozit zachycením. Evropská norma EN 14682 pro dětské oblečení do věku 7 let, tedy pro děti do výšky 134 cm, nepovoluje šňůrky v oblasti kapuce a krku. U starších dětí omezuje jejich délku a volné konce. '
          'Při výběru proto dávejte přednost kapucím, které se stahují pružnou páskou nebo suchým zipem, a staženým lemům se šňůrkou uvnitř. Odnímatelná kapuce na patentky se při zachycení uvolní, což je u malých dětí výhoda.</p>'
          '<p>Na podzim se brzy stmívá. Reflexní proužky na rukávech a zádech zvýší viditelnost dítěte pro řidiče, a pokud bunda žádné nemá, doplňte ji reflexní páskou nebo <a href="/reflexni-vesty/">reflexní vestou</a>. Světlé a výrazné barvy pomáhají také ve dne, třeba v lese nebo v davu.</p>'
          '<h2>Jak poznat, jestli je dítěti teplo, nebo zima</h2>'
          '<p>Malé děti často neumějí říct, že je jim zima, nebo si toho nevšimnou, dokud si hrají. Ruce bývají chladné skoro vždy a o celkovém teple moc neřeknou. Spolehlivější je sáhnout dítěti za krk nebo na záda pod bundou. Když je kůže teplá a suchá, je to v pořádku. Zpocená záda znamenají, že je dítě oblečené příliš, a studená, že potřebuje další vrstvu. '
          'Častější chybou je přehřátí. Dítě, které běhá v zateplené bundě, se zpotí a ve chvíli, kdy se zastaví, rychle prochladne. Proto je lepší obléct tenčí vrstvy a jednu nosit v batohu.</p>'
          '<h2>Na kolo a na koloběžku</h2>'
          '<p>Při jízdě na kole nebo koloběžce fouká víc než při chůzi a ruce i krk prochládají rychleji. Hodí se bunda s delšími zády, která se při předklonu nevyhrne, a s manžetami, jež nepustí vítr do rukávů. '
          'Kapuci nedávejte pod přilbu, přilba by pak neseděla tak, jak má. Pokud je chladno, patří pod přilbu tenká čepice nebo kukla, kapuce zůstane volně vzadu nebo ji odepněte.</p>'
          '<h2>Detaily, které rozhodují v praxi</h2>'
          '<ul><li><strong>Zip s krytem u brady</strong> neštípe pod krkem a mladší dítě si ho zapne samo.</li>'
          '<li><strong>Zesílené lokty a spodní lem</strong> vydrží lezení po prolézačkách.</li>'
          '<li><strong>Poutko na pověšení</strong> uvnitř u krku se ve školce i ve škole hodí víc, než by se zdálo.</li>'
          '<li><strong>Místo na jmenovku</strong> pomůže, když stejnou bundu má půl třídy.</li>'
          '<li><strong>Kapsy na zip</strong> nevysypou klíče ani kapesníky při kotrmelci.</li></ul>'
          '<h2>Jedna bunda, nebo dvě?</h2>'
          '<p>Hodně rodin řeší podzim dvěma bundami. Jedna odolná a nepromokavá slouží do školky, do lesa a na dny, kdy se počítá s blátem. Druhá, čistší a lehčí, se nosí na cestu do školy, na návštěvu nebo do města. '
          'Bunda na hraní pak nemusí vypadat dobře a bunda do města nemusí vydržet louže. Pokud vám jedna bunda stačit má, volte spíš tu odolnější a k ní tenkou mikinu, kterou lze pod ni přidat nebo ji sundat. '
          'V přechodném období mezi létem a podzimem dobře poslouží i samotná vesta přes mikinu, která nechá ruce volné a nepřehřívá.</p>'
          '<h2>Zkouška před první sezonou</h2>'
          '<p>Novou bundu je dobré nechat dítě vyzkoušet doma ještě před prvním chladným dnem. Ověříte, jestli si ji samo zapne, jestli mu kapuce nepadá do očí a jestli rukávy nejsou krátké s mikinou pod nimi. Když něco nesedí, je ještě čas bundu vyměnit za jinou velikost.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Dětské outdoorové bundy patří k hlavním řadám finské značky <a href="/znacka/reima/">Reima</a>, od <a href="/znacka/kilpi/">Kilpi</a>, Peak Mountain, Trespass a Regatta uvidíte modely pro malé i starší děti. '
          'Dále se v nabídce objevují Columbia, Didriksons, <a href="/znacka/loap/">Loap</a>, Hannah a Alpine Pro. Sportovní tréninkové bundy, často jako součást týmového oblečení, mají Nike, Adidas, Puma, Errea a Hummel. Módní kousky, třeba riflové bundy, dodávají Gap, Guess nebo Tommy Hilfiger.</p>'
          '<h2>Péče a předávání dál</h2>'
          '<p>Dětskou bundu budete prát častěji než svou. Perte ji podle štítku, obvykle na 30 až 40 °C, s prostředkem na funkční textil a bez aviváže, která ucpává membránu a ruší vodoodpudivou úpravu. Hrubé bláto nechte zaschnout a vykartáčujte, než bundu dáte do pračky. '
          'Po několika praních se povrch přestane chovat vodoodpudivě. Pomůže prací nebo sprejová <a href="/impregnace/">impregnace</a>. Kvalitní dětská bunda často vydrží víc dětí než jedno, a pokud ji po sezoně vyperete a uložíte suchou, poslouží i mladšímu sourozenci.</p>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Nejdřív zvolte typ podle toho, kde ho dítě bude nosit, potom hledejte velikost podle výšky a zkontrolujte bezpečnost kapuce. Sporteka ukazuje nabídky českých obchodů na jednom místě, objednávku dokončíte v e-shopu. '
          'K bundě se na podzim hodí <a href="/detske-trekove-boty/">dětské trekové boty</a> nebo <a href="/detske-holinky/">dětské holinky</a> do bláta a tenké <a href="/detske-rukavice/">dětské rukavice</a>. Pro dospělé se podívejte na <a href="/panska-podzimni-bunda/">pánské podzimní bundy</a> a <a href="/jarni-a-podzimni-bundy-damske/">dámské jarní a podzimní bundy</a>.</p>',
    faq=[
        ('Jakou podzimní bundu do školky?', 'Do školky se hodí bunda, která vydrží mokro a lezení po zemi: nepromokavá bunda nebo softshell s membránou, ideálně s kapucí bez šňůrek a s reflexními prvky. Pro nejmenší jsou praktické nepromokavé soupravy.'),
        ('Je dětský softshell nepromokavý?', 'Většinou ne. Krátký déšť vydrží díky vodoodpudivé úpravě, ale při delším dešti nebo sezení v mokru se nasákne. Na deštivé dny je spolehlivější bunda s membránou a podlepenými švy.'),
        ('Jak vybrat velikost dětské bundy?', 'Změřte výšku dítěte bez bot a vyberte velikost podle výšky, případně o číslo větší. Příliš velká bunda padá přes ruce a fouká do ní. Při zkoušení nechte dítě zvednout ruce a dřepnout si.'),
        ('Proč dětské bundy nemají šňůrky v kapuci?', 'Evropská norma EN 14682 je u dětského oblečení do 7 let a výšky 134 cm v oblasti kapuce a krku nepovoluje, protože by se mohly zachytit. Kapuce se proto stahují pružnou páskou nebo suchým zipem.'),
        ('Má být podzimní bunda pro dítě zateplená?', 'Na začátek podzimu ne, dítě se v ní při běhání zpotí. Lepší je lehčí bunda a pod ní mikina nebo vesta. Zateplená bunda se hodí na studené listopadové dny a na děti, které se moc nehýbou.'),
        ('Co pod dětskou podzimní bundu?', 'Funkční tričko nebo tenké termoprádlo, přes ně mikinu nebo fleece a navrch bundu. Vrstvy se dají odložit, když se oteplí nebo když dítě začne běhat.'),
        ('Jak prát dětskou bundu s membránou?', 'Podle štítku, obvykle na 30 až 40 °C s prostředkem na funkční textil a bez aviváže. Zaschlé bláto nejdřív vykartáčujte. Když voda přestane stékat po povrchu, bundu impregnujte.'),
        ('Proč jsou na dětských bundách reflexní prvky?', 'Na podzim se brzy stmívá a reflexní proužky výrazně zvýší viditelnost dítěte ve světle reflektorů. Pokud je bunda nemá, pomůže reflexní páska nebo vesta.'),
        ('Které značky dělají dětské podzimní bundy?', 'V nabídce jsou například Reima, Kilpi, Peak Mountain, Trespass, Regatta, Columbia, Didriksons, Loap, Hannah a Alpine Pro. Sportovní bundy mají Nike, Adidas, Puma nebo Hummel.'),
        ('Kde porovnat nabídky dětských podzimních bund?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Objednávku dokončíte v e-shopu, kde ověříte velikostní tabulku a dostupnou barvu.'),
    ])

# ------------------------------------------------------------------ damska-prosivana-bunda
NEW['damska-prosivana-bunda'] = dict(
    title='Dámská prošívaná bunda: lehká, zimní, krátká i dlouhá',
    desc='Dámské prošívané bundy s péřovou nebo syntetickou výplní: lehké přechodové, zimní, krátké i dlouhé. Jak vybrat výplň, délku, velikost a jak je prát.',
    intro='<p><strong>Dámská prošívaná bunda</strong> se pozná podle vodorovných komor, které drží výplň na místě. Komory mohou být úzké jako u lehké bundy, kterou sbalíte do kapsy, nebo široké a nafouklé jako u zimního modelu do mrazu. '
          'Pod jedním názvem se tedy skrývají kousky na přechodné období i na zimu, krátké bundy do pasu i dlouhé kabáty pod kolena. Liší se výplní, konstrukcí prošití, délkou a tím, jestli mají kapuci. '
          'Na této stránce jsou dámské modely z kategorie <a href="/prosivane-bundy/">prošívané bundy</a> s nabídkami z českých obchodů. '
          'Průvodce vysvětluje rozdíl mezi péřovou a syntetickou výplní, proč na prošití záleží, jak vybrat délku a velikost a jak bundu prát, aby neztratila objem. '
          'Hledáte-li čistě péřový model, podívejte se také na stránku <a href="/perova-bunda-damska/">dámská péřová bunda</a>.</p>',
    guide='<h2>Proč je bunda prošitá</h2>'
          '<p>Výplň potřebuje držet na svém místě. Kdyby byla mezi vrchní látkou a podšívkou volně, po pár týdnech nošení by se sesypala dolů a v ramenou by zůstala jen prázdná látka. Prošití rozdělí bundu na komory, z nichž každá drží svůj díl výplně. '
          'Šířka komor ovlivňuje vzhled i teplo. Úzké komory dávají bundě plochý, elegantní tvar, bunda je tenká a hodí se pod kabát nebo na přechodné období. Široké komory pojmou víc výplně a bunda hřeje víc, působí ale objemněji.</p>'
          '<h2>Prošití skrz, nebo komory s přepážkou</h2>'
          '<p>Nejjednodušší konstrukce sešívá vrchní látku přímo s podšívkou. Je lehká a levnější na výrobu, jenže v místě švu žádná výplň není a látka je tam jen dvojitá. Švy pak fungují jako chladné pruhy, kudy uniká teplo a fouká vítr. '
          'U teplejších modelů se proto používají komory s přepážkou. Mezi vrchní látku a podšívku je všitý pruh látky, který komory odděluje, a výplň má prostor i v místě švu. Bunda je teplejší, ale těžší a dražší na výrobu. Na přechodné období a do města stačí prošití skrz, do mrazu a na dlouhé stání venku je lepší přepážka.</p>'
          '<h2>Péřová, nebo syntetická výplň</h2>'
          + T(['Výplň', 'Výhody', 'Nevýhody'], [
              ['péří a prachové peří', 'nejlepší poměr tepla a hmotnosti, dobře se sbalí, vydrží mnoho let', 've vlhku ztrácí objem, praní a sušení vyžaduje péči'],
              ['syntetická výplň', 'hřeje i vlhká, rychle schne, snadno se pere', 'při stejném teple je těžší a objemnější, časem se slehne'],
              ['vatelín a polyesterové rouno', 'jednoduchá a levná výplň módních bund', 'méně tepla na gram, horší sbalitelnost'],
              ['kombinace', 'peří na trupu, syntetika na ramenou a rukávech', 'menší výběr modelů']]) +
          '<p>U péřových bund obchody uvádějí poměr prachového peří k peří, například 80/20 nebo 90/10, a někdy plnivost, tedy schopnost peří vrátit se do původního objemu. Vyšší číslo znamená víc tepla na gram. U syntetiky se uvádí gramáž výplně na metr čtvereční. '
          'Pokud bundu nosíte hlavně ve městě a často ji vezmete do deště, syntetika je praktičtější. Kdo chce nejvíc tepla a nejmenší objem, sáhne po peří. Podrobnosti o péřových modelech najdete v kategorii <a href="/perove-bundy/">péřové bundy</a>.</p>'
          '<h2>Délka a střih</h2>'
          '<ul><li><strong>Krátká bunda do pasu</strong> je lehká a nepřekáží v autě, na kole ani s batohem. Hodí se na přechodné období a ke sportovnějšímu oblečení.</li>'
          '<li><strong>Bunda přes boky</strong> je nejuniverzálnější délka. Zakryje bedra a ještě nebrání v pohybu.</li>'
          '<li><strong>Dlouhá bunda nebo kabát</strong> pod zadek či ke kolenům hřeje na celé tělo a je ideální na čekání na zastávce. Na kole nebo při delší chůzi do kopce ale svazuje. Dlouhé zimní modely najdete také v kategorii <a href="/kabaty-a-parky/">kabáty a parky</a> a na stránce <a href="/damsky-kabat/">dámský kabát</a>.</li></ul>'
          '<p>Dámský střih bývá v pase zúžený, některé modely mají stahovací pásek nebo šňůrku. Oversize střihy jsou naopak volnější a pod ně se vejde silný svetr. Prošívaná vesta, pro kterou je stránka <a href="/damske-vesty/">dámské vesty</a>, je praktickou alternativou na přechodné období.</p>'
          '<h2>Lehká přechodová, nebo zimní</h2>'
          '<p>Lehké prošívané bundy mají tenkou výplň a úzké komory. Hřejí na jaře a na podzim, v zimě poslouží jako mezivrstva pod nepromokavou bundu nebo kabát. Hodně z nich se sbalí do vlastní kapsy nebo do přiloženého pytlíku a na výlet je můžete nosit v batohu. '
          'Zimní prošívané bundy mají víc výplně, širší komory, často kapuci s lemem a manžety, které nepouští vítr do rukávů. Kdo hledá teplou zimní bundu jiné konstrukce, najde ji na stránce <a href="/damska-zimni-bunda/">dámská zimní bunda</a>. Na přechodné období jsou tu i <a href="/jarni-a-podzimni-bundy-damske/">dámské jarní a podzimní bundy</a>.</p>'
          '<h2>Prošívaná bunda a déšť</h2>'
          '<p>Prošívaná bunda většinou není nepromokavá. Každý šev znamená řadu dírek po jehle, kterými voda proteče dovnitř, a vrchní látka mívá jen vodoodpudivou úpravu. Lehký déšť nebo sníh vydrží, delší déšť ne. '
          'Do deště se proto prošívaná bunda nosí pod nepromokavou vrstvu, nebo se vybírá model se svařovanými komorami bez prošití. Pro deštivé dny je vhodnější <a href="/damska-nepromokava-bunda/">dámská nepromokavá bunda</a>, pod kterou lehká prošívaná bunda funguje jako teplá vrstva.</p>'
          '<h2>Kapuce, límec a další detaily</h2>'
          '<p>Kapuce je u prošívané bundy znát víc, než se zdá. Zateplená kapuce s pružným lemem kolem obličeje zastoupí v mírném počasí čepici, odepínací kapuce zase umožní nosit bundu ve městě s šálou. Vysoký stojáček chrání krk, a když má uvnitř u brady měkký úplet, nedře. '
          'Praktické jsou kapsy podšité fleecem, ve kterých se zahřejí ruce, a vnitřní kapsa na telefon, kde baterie v mrazu vydrží déle. U dlouhých modelů oceníte dvoucestný zip, který se dá rozepnout zespodu při sedání nebo při jízdě v autě.</p>'
          '<h2>Původ peří</h2>'
          '<p>Kdo kupuje péřovou prošívanou bundu, může sledovat certifikaci RDS, tedy Responsible Down Standard. Ta má zaručit, že peří nepochází z ptáků škubaných zaživa ani z nuceného výkrmu. Údaj o certifikaci najdete na štítku nebo v popisu produktu. '
          'Syntetické výplně tuto otázku neřeší, některé značky do nich ale přidávají recyklovaný polyester. Pokud vám záleží na původu materiálu, hledejte konkrétní údaj v popisu, obecná slova o udržitelnosti bez certifikace mnoho neříkají.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Prošívaná bunda má sedět volně, ale ne plandat. Výplň potřebuje prostor, aby mohla nadýchnout. Když je bunda těsná, výplň se stlačí a hřeje méně. Zkoušejte ji se svetrem nebo mikinou, kterou pod ní budete nosit. '
          'Rukávy mají zakrývat zápěstí i při natažení rukou dopředu. U dlouhých modelů vyzkoušejte, jestli se v nich dá pohodlně sednout, rozparek vzadu nebo dvoucestný zip tomu hodně pomáhá.</p>'
          '<h2>Do města i na výlet</h2>'
          '<p>Městské prošívané bundy mají hladkou lesklou nebo matnou látku, zúžený pas a často kožešinový lem kapuce. Sportovní modely jsou lehčí, mají pružné boky a dají se sbalit. Kdo bundu bere i na hory, ocení odolnější vrchní látku a manžety, které se vejdou pod rukavice.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Dámské prošívané bundy v nabídce nejčastěji dodávají <a href="/znacka/regatta/">Regatta</a>, <a href="/znacka/trespass/">Trespass</a> a <a href="/znacka/dare2b/">Dare2b</a>. Dále se objevují Siroko, Lotto, Willard, Superdry s modelem Fuji, Champion, Trimm, Northfinder, The North Face, Helly Hansen nebo Columbia. Módnější střihy mají Guess, Gap, DKNY nebo EA7 Emporio Armani.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Syntetickou prošívanou bundu vyperete v pračce na nízkou teplotu s běžným jemným prostředkem bez aviváže. Péřovou bundu perte v prostředku určeném na peří, na šetrný program a s mírným odstřeďováním. '
          'Péří je po praní slepené do hrudek a potřebuje se rozbít. Nejlépe se suší v sušičce na nízkou teplotu s několika tenisovými míčky, které výplň během sušení rozmělní. Sušení na vzduchu trvá i několik dní a bundu je potřeba často protřepat, jinak peří může zatuchnout. '
          'Na léto bundu ukládejte volně na ramínku nebo ve velkém prodyšném vaku, ne dlouhodobě stlačenou v kompresním obalu.</p>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Nejprve si vyberte výplň a délku, potom kapuci a barvu. U stejného modelu se nabídky často liší jen odstínem. Sporteka ukazuje nabídky českých e-shopů pohromadě, nákup dokončíte v obchodě, který si zvolíte. '
          'Pod lehkou prošívanou bundu se na výlet hodí <a href="/damska-funkcni-mikina/">dámská funkční mikina</a>, pro sportovnější použití pak <a href="/damska-softshellova-bunda/">dámská softshellová bunda</a>.</p>',
    faq=[
        ('Hřeje prošívaná bunda v zimě?', 'Záleží na výplni a šířce komor. Lehké prošívané bundy jsou na přechodné období, zimní modely mají víc výplně a širší komory. V mrazu hřejí lépe modely s přepážkami mezi komorami.'),
        ('Je prošívaná bunda nepromokavá?', 'Většinou ne. Švy mají dírky po jehle a vrchní látka bývá jen vodoodpudivá. Lehký déšť vydrží, do delšího deště ji noste pod nepromokavou bundou.'),
        ('Péří, nebo syntetika?', 'Péří dá nejvíc tepla při nejnižší hmotnosti a dobře se sbalí, ve vlhku ale ztrácí objem. Syntetika hřeje i vlhká, rychle schne a snadno se pere, při stejném teple je těžší.'),
        ('Co znamená 80/20 u péřové bundy?', 'Poměr prachového peří a peří. Prachové peří je jemnější a hřeje víc, proto vyšší podíl, třeba 90/10, znamená teplejší výplň při stejné hmotnosti.'),
        ('Jaký je rozdíl mezi prošitím skrz a komorami s přepážkou?', 'Při prošití skrz je vrchní látka sešitá přímo s podšívkou a ve švu není výplň, takže tam uniká teplo. Komory s přepážkou mají výplň i v místě švu a hřejí lépe.'),
        ('Jakou velikost prošívané bundy vybrat?', 'Takovou, která sedí volně se svetrem pod ní. V těsné bundě se výplň stlačí a hřeje méně. Rukávy mají zakrývat zápěstí i při natažení rukou.'),
        ('Jak prát dámskou péřovou bundu?', 'V prostředku na peří, šetrným programem na nízkou teplotu a s mírným odstřeďováním. Sušte v sušičce na nízkou teplotu s tenisovými míčky, které rozbijí hrudky peří.'),
        ('Je lepší krátká, nebo dlouhá prošívaná bunda?', 'Krátká je pohodlnější na kolo, do auta a s batohem. Dlouhá hřeje víc, hodí se na čekání venku a do mrazu, ale svazuje při chůzi do kopce.'),
        ('Dá se prošívaná bunda nosit pod jinou bundu?', 'Lehké modely ano. Pod nepromokavou bundou fungují jako teplá vrstva a celek pak drží déšť i chlad. Silné zimní bundy jsou na to příliš objemné.'),
        ('Kde porovnat nabídky dámských prošívaných bund?', 'Na této stránce vidíte nabídky českých obchodů vedle sebe. Nákup dokončíte v e-shopu, kde ověříte výplň, velikost a dostupnou barvu.'),
    ])

# ------------------------------------------------------------------ detsky-turisticky-batoh
NEW['detsky-turisticky-batoh'] = dict(
    title='Dětský turistický batoh: podle věku, objemu a zad',
    desc='Dětské turistické batohy pro malé i starší děti: od 7 litrů po trekové s nastavitelnými zády. Jak vybrat objem, velikost, a kolik dítě unese.',
    intro='<p><strong>Dětský turistický batoh</strong> dává dítěti pocit, že na výletě není jen pasažér. Nese si svou svačinu, láhev a bundu, a když batoh dobře sedí, nese ho rádo. '
          'Mezi dětskými batohy jsou malé batůžky pro děti od dvou let, univerzální výletní batohy kolem patnácti až dvaceti litrů i trekové batohy s nastavitelnou délkou zad pro starší děti, které chodí na vícedenní túry. '
          'Na této stránce jsou dětské modely z kategorie <a href="/turisticke-batohy/">turistické batohy</a> s nabídkami z českých obchodů. '
          'Průvodce radí, jak vybrat objem podle věku, jak batoh nastavit, kolik toho dítě rozumně unese a co do něj na výlet zabalit. '
          'Batohy do školy najdete v kategorii <a href="/skolni-batohy/">školní batohy</a>, městské a volnočasové modely na stránce <a href="/detsky-batoh/">dětský batoh</a>.</p>',
    guide='<h2>Jaký objem podle věku</h2>'
          '<p>Menší batoh je pro dítě lepší než velký. Velký batoh láká rodiče, aby do něj přibalili i své věci, a dítě ho pak po hodině odmítne nést. Výrobci uvádějí u dětských batohů doporučený věk nebo výšku, a to je dobré vodítko.</p>'
          + T(['Věk', 'Objem', 'Co dítě nese', 'Příklady z nabídky'], [
              ['2–5 let', 'zhruba 5–10 litrů', 'láhev, svačinu, hračku', 'Deuter Kikki, Deuter Schmusebar, Quechua NH 100 a MH 100 pro 2–5 let'],
              ['5–9 let', 'zhruba 10–18 litrů', 'láhev, svačinu, tenkou bundu', 'Deuter Junior, Osprey Daylite Jr., Husky Jolly a Jikko, Mammut First Zip 16'],
              ['8–12 let', 'zhruba 18–25 litrů', 'k tomu čepici, rukavice, mikinu', 'Deuter Climber 22, Vaude Hidalgo 24+4'],
              ['od 10 let a vícedenní túry', '30–40 litrů', 'oblečení, spacák na chatu', 'Deuter Fox 30 a 40, Quechua MH 500 pro 7–15 let, Osprey Talon Jr']]) +
          '<p>Hranice jsou orientační. Drobné osmileté dítě může potřebovat batoh pro mladší děti, vysoký desetiletý kluk naopak sáhne po menším batohu pro dospělé. U trekových modelů je rozhodující délka zad, ne věk.</p>'
          '<h2>Kolik dítě unese</h2>'
          '<p>Pro dětské batohy se často uvádí orientační pravidlo, že náklad by neměl přesáhnout zhruba desetinu hmotnosti dítěte. Některé zdroje připouštějí víc, jiné u malých dětí doporučují ještě méně. Nejde o přesnou hranici, ale o rozumné vodítko. Dítě, které váží 25 kg, by tak mělo nést kolem dvou a půl kilogramu. '
          'To odpovídá láhvi s vodou, svačině a lehké bundě. Těžší věci, jako jídlo pro celou rodinu, termosku nebo náhradní oblečení pro všechny, nesou rodiče. Pokud dítě začne batoh tahat za popruhy, předklánět se nebo si stěžovat na ramena, je batoh příliš těžký nebo špatně nastavený.</p>'
          '<p>Pokud má dítě problémy se zády nebo jiné zdravotní potíže, poraďte se o vhodné zátěži s dětským lékařem.</p>'
          '<h2>Co má mít dobrý dětský batoh</h2>'
          '<ul><li><strong>Hrudní popruh</strong> spojuje ramenní popruhy a nedovolí jim sklouznout z úzkých dětských ramen. U malých batohů je to nejdůležitější prvek.</li>'
          '<li><strong>Bederní pás</strong> má smysl od objemu kolem dvaceti litrů. U malých batůžků stačí tenký pásek, který jen zabrání houpání.</li>'
          '<li><strong>Odvětraná záda</strong> s tvarovanými polštářky nebo síťkou omezují pocení.</li>'
          '<li><strong>Boční kapsy na láhev</strong>, na které dítě dosáhne bez sundání batohu.</li>'
          '<li><strong>Reflexní prvky</strong> pro návrat z výletu za šera.</li>'
          '<li><strong>Jmenovka a kontaktní údaje</strong> uvnitř víka. Některé dětské batohy mají na štítek přímo připravené místo.</li></ul>'
          '<p>Některé dětské modely mají na přezce hrudního popruhu píšťalku. Hodí se naučit dítě, kdy ji použít, a to jen tehdy, když se ztratí nebo potřebuje pomoc.</p>'
          '<h2>Nastavitelná záda u starších dětí</h2>'
          '<p>Batohy pro vícedenní túry mají systém, kterým se mění výška ramenních popruhů. Například Deuter Fox používá systém VariQuick, díky kterému se dá délka zad nastavit podle toho, jak dítě roste. Batoh tak vydrží několik sezon. '
          'Nastavení je stejné jako u dospělých. Batoh naložte, bederní pás umístěte na horní hranu pánevních kostí, ramenní popruhy mají přiléhat k ramenům bez mezer a hrudní popruh má být zhruba v úrovni podpaží. Pokud popruhy začínají vysoko nad rameny nebo se zarývají do krku, je potřeba upravit délku zad.</p>'
          '<h2>Krosna na dítě není dětský batoh</h2>'
          '<p>Mezi dětskými turistickými batohy se v nabídce objevují také dětská nosítka a krosny, například Deuter Kid Comfort nebo LittleLife Adventurer a Voyager. Ty jsou určené rodičům na nošení dítěte na zádech, nikoli dětem. '
          'Výrobci u nich uvádějí, od jakého věku a do jaké hmotnosti dítěte jsou určené. Dítě by v nich mělo jezdit, až když samo pevně sedí a drží hlavu. Údaje vždy ověřte v popisu konkrétního modelu.</p>'
          '<h2>Co dát do dětského batohu</h2>'
          '<p>Na jednodenní výlet stačí láhev s pitím, svačina, lehká bunda nebo pláštěnka a v chladnějších měsících čepice. Vhodné jsou i malé věci, které dítě baví: lupa, zápisník nebo pastelky. '
          'Na pití se hodí lehké <a href="/lahve-a-termosky/">láhve a termosky</a>, které dítě zvládne otevřít samo. Pro starší děti, které chodí s rodiči do hor, je dobré přibalit i lékárničku a čelovku, pokud se má vracet za šera. Těžší věci nesou dospělí.</p>'
          '<h2>Bezpečnost na výletě</h2>'
          '<p>Batoh v jasné barvě je v lese a v davu dobře vidět. Do víka nebo vnitřní kapsy vložte kartičku se jménem dítěte a telefonním číslem rodičů a naučte dítě, kde ji má. '
          'Domluvte se předem, co dělat, když se ztratíte: zůstat stát na místě, nepouštět se dál po cestě a zavolat nebo pískat. Malé děti by na túře neměly chodit daleko napřed, zvlášť na rozcestích a u srázů. Na delší túry se hodí i tenká pláštěnka přes batoh, protože většina dětských batohů není nepromokavá a náhradní oblečení v mokrém batohu nepomůže.</p>'
          '<h2>Jak dítě nošení batohu nezprotivit</h2>'
          '<p>Dítě nese batoh rádo, když v něm má své věci a když si ho samo vybralo. Nechte ho vybrat barvu a zabalit si svačinu a hračku. První výlety s batohem plánujte krátké, s přestávkami a cílem, který dítě zajímá, třeba rozhlednou nebo potokem. '
          'Když dítě unaví, nevadí, když si batoh na chvíli vezme rodič. Je lepší se k nošení vrátit na příštím výletě, než aby si dítě batoh spojilo s nepříjemným zážitkem.</p>'
          '<h2>Batoh na kolo</h2>'
          '<p>Na výlety na kole jsou určené menší batohy s pevným hrudním popruhem a nízkým profilem, aby nenarážely do přilby. V nabídce se objevuje například Deuter Junior Bike. Batoh na kolo by měl být lehký, protože dítě jeho váhu cítí na rovnováze víc než při chůzi.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejširší výběr dětských turistických batohů má německý <a href="/znacka/deuter/">Deuter</a>, který podle svého webu vyrábí batohy pro děti od dvou let. Dále v nabídce uvidíte <a href="/znacka/osprey/">Osprey</a> s řadami Daylite Jr., Talon Jr a Tempest Jr, českou značku <a href="/znacka/husky/">Husky</a>, Quechua z Decathlonu, Vaude, Mammut, Fjällräven s menšími verzemi Kånkenu, Trollkids, Lundhags a CMP.</p>'
          '<h2>Sourozenci a dědění</h2>'
          '<p>Dětský batoh obvykle vydrží déle, než ho dítě potřebuje. Malý batůžek pro předškoláka může po pár letech převzít mladší sourozenec, zatímco starší dítě přejde na větší model. Proto se vyplatí volit odolný materiál a neutrální barvu, kterou ocení i další dítě. '
          'U trekových batohů s nastavitelnými zády je dědění ještě snazší, protože se dají přizpůsobit menšímu dítěti. Před předáním zkontrolujte přezky, zipy a švy na popruzích, které se opotřebí nejdřív.</p>'
          '<h2>Jak batoh vyzkoušet</h2>'
          '<p>Zkoušejte batoh naložený, protože prázdný sedí jinak. Dejte do něj láhev a bundu a nechte dítě chvíli chodit po bytě, chodit do schodů nebo běhat. Batoh se nemá houpat do stran ani tlačit do zad. '
          'Kupujete-li online, změřte dítě od vystouplého obratle na spodu krku k horní hraně pánevních kostí a porovnejte údaj s tabulkou výrobce. U batohů bez nastavení zad se řiďte doporučeným věkem a výškou.</p>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Nejdřív vyberte objem podle věku a délky výletů, potom zkontrolujte hrudní popruh, bederní pás a odvětrání zad a nakonec barvu. Sporteka sdružuje nabídky českých obchodů na jednom místě, objednávku dokončíte v e-shopu. '
          'K výletu se hodí <a href="/detske-trekove-boty/">dětské trekové boty</a>, na delší túry <a href="/trekove-hole/">trekové hole</a> a na přespání <a href="/detsky-spacak/">dětský spacák</a>. Dospělí najdou batohy na stránkách <a href="/damsky-turisticky-batoh/">dámský turistický batoh</a> a <a href="/pansky-batoh/">pánský batoh</a>.</p>',
    faq=[
        ('Od kolika let dát dítěti turistický batoh?', 'Malý batůžek s lahví a svačinou zvládnou děti zhruba od dvou let. Deuter uvádí dětské batohy pro děti od dvou let. Objem a hmotnost nákladu ale musí odpovídat věku.'),
        ('Jak velký batoh pro dítě na výlet?', 'Pro předškoláky stačí 5–10 litrů, pro mladší školáky 10–18 litrů a pro starší děti 18–25 litrů. Na vícedenní túry jsou určené dětské trekové batohy kolem 30–40 litrů.'),
        ('Kolik smí nést dítě v batohu?', 'Jako orientační pravidlo se často uvádí zhruba desetina hmotnosti dítěte. Při potížích se zády nebo jiných zdravotních obtížích se poraďte s dětským lékařem.'),
        ('Proč má dětský batoh hrudní popruh?', 'Spojuje ramenní popruhy, aby nesklouzávaly z úzkých dětských ramen. Měl by být zhruba v úrovni podpaží a nemá škrtit.'),
        ('Potřebuje dětský batoh bederní pás?', 'U malých batůžků stačí tenký pásek proti houpání. U batohů kolem dvaceti litrů a víc pomůže bederní pás přenést část váhy na boky.'),
        ('Co je VariQuick u Deuter Fox?', 'Systém nastavení délky zad u dětských trekových batohů Deuter Fox. Výšku ramenních popruhů lze měnit, takže batoh roste s dítětem.'),
        ('Jak změřit délku zad u dítěte?', 'Od vystouplého obratle na spodu krku, který se nahmatá při předklonu hlavy, k horní hraně pánevních kostí. Údaj porovnejte s tabulkou výrobce.'),
        ('Je krosna na dítě totéž co dětský batoh?', 'Ne. Krosna nebo nosítko slouží rodiči k nošení dítěte na zádech. Výrobci u nich uvádějí minimální věk a maximální hmotnost dítěte.'),
        ('Co dát dítěti do turistického batohu?', 'Láhev, svačinu, lehkou bundu nebo pláštěnku a v chladu čepici. Těžší věci pro celou rodinu by měli nést dospělí.'),
        ('Kde porovnat nabídky dětských turistických batohů?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Nákup dokončíte v e-shopu, kde ověříte objem, doporučený věk a dostupnou barvu.'),
    ])

# ------------------------------------------------------------------ damsky-turisticky-batoh
NEW['damsky-turisticky-batoh'] = dict(
    title='Dámský turistický batoh: kratší záda, užší popruhy',
    desc='Dámské turistické batohy s kratšími zády, užšími popruhy a tvarovaným bederním pásem. Jak změřit délku zad, vybrat objem a batoh nastavit.',
    intro='<p><strong>Dámský turistický batoh</strong> není jen zmenšený nebo jinak obarvený pánský model. Liší se nosný systém: záda bývají kratší, ramenní popruhy užší a víc prohnuté a bederní pás je tvarovaný tak, aby seděl na pánvi, která bývá u žen širší. '
          'Na dlouhé túře se ten rozdíl pozná na ramenou i na bocích. '
          'Na této stránce jsou dámské modely z kategorie <a href="/turisticke-batohy/">turistické batohy</a> s nabídkami z českých obchodů, od lehkých batohů na jednodenní výlet až po velké batohy na vícedenní trek. '
          'Průvodce vysvětluje, jak se dámský střih batohu liší, jak změřit délku zad, jaký objem zvolit podle délky túry a jak batoh správně nastavit. '
          'Městské dámské batohy najdete na stránce <a href="/damsky-batoh/">dámský batoh</a>, batohy pro děti pod odkazem <a href="/detsky-turisticky-batoh/">dětský turistický batoh</a>.</p>',
    guide='<h2>V čem je dámský batoh jiný</h2>'
          '<p>Výrobci staví dámské batohy na průměrných proporcích ženského těla. Ženy mívají v poměru k výšce kratší trup, užší ramena a širší boky. Batoh s pánskými zády pak u nich sedí tak, že bederní pás je moc nízko nebo ramenní popruhy začínají nad rameny a tlačí do krku.</p>'
          + T(['Část nosného systému', 'Dámská úprava', 'Co to přinese'], [
              ['délka zad', 'kratší, nebo s nastavením v nižším rozsahu', 'váha sedí na bocích, ne na ramenou'],
              ['ramenní popruhy', 'užší, víc prohnuté do tvaru S, kratší', 'netlačí na hrudník a nesjíždějí z ramen'],
              ['hrudní popruh', 'posuvný ve větším rozsahu', 'dá se umístit nad hrudník'],
              ['bederní pás', 'kuželovitě tvarovaný, kratší', 'obepne boky a nepřitlačí se do pasu'],
              ['hmotnost a objem', 'často o něco menší a lehčí', 'snadnější nesení na dlouhé túře']]) +
          '<p>Německý Deuter označuje dámské batohy zkratkou SL, Slim Line. Podle jeho tabulky počítá střih SL s délkou zad kolem 42 cm a postavou zhruba 160 až 175 cm, běžný střih s délkou zad kolem 46 cm a prodloužený EL s délkou kolem 50 cm. Deuter zároveň uvádí, že střih SL může sednout i štíhlým mužům s kratšími zády.</p>'
          '<h2>Jak změřit délku zad</h2>'
          '<p>Rozhoduje délka trupu, ne výška postavy. Dvě stejně vysoké ženy mohou mít různě dlouhá záda. Měří se od sedmého krčního obratle, který nahmatáte jako vystouplou kost na spodu krku, když skloníte bradu k hrudi, k horní hraně pánevních kostí. Tuto rovinu najdete, když dáte ruce v bok a palci sjedete dozadu k páteři. '
          'Měření je lepší udělat ve dvou, s krejčovským metrem vedeným podél páteře. Výsledek porovnejte s tabulkou výrobce. Osprey u svých batohů uvádí velikosti podle délky trupu, Deuter rozlišuje střihy SL, běžný a EL. Bederní pás se vybírá podle obvodu boků v úrovni pánevních kostí, nikoli podle obvodu pasu.</p>'
          '<h2>Jaký objem na jakou túru</h2>'
          + T(['Typ túry', 'Objem', 'Co se vejde'], [
              ['půldenní výlet, běh do kopce', '10–20 litrů', 'voda, svačina, větrovka'],
              ['celodenní túra', '20–30 litrů', 'k tomu teplá vrstva, nepromokavá bunda, lékárnička'],
              ['túra s přespáním na chatě', '30–40 litrů', 'náhradní oblečení, hygiena, spacák do chaty'],
              ['vícedenní trek se stanem', '45–65 litrů a víc', 'stan, spacák, karimatka, vařič, jídlo']]) +
          '<p>Batoh volte podle nejčastější túry, ne podle výjimky. Pokud chodíte hlavně na jednodenní výlety, poslouží vám dvacetilitrový batoh lépe než čtyřicetilitrový, který bude poloprázdný a bude se houpat.</p>'
          '<h2>Nastavení batohu krok za krokem</h2>'
          '<ol><li>Naložte do batohu zhruba tolik, kolik ponesete, aspoň několik kilogramů. Prázdný batoh se nastavit nedá.</li>'
          '<li>Povolte všechny popruhy, nasaďte batoh a utáhněte bederní pás tak, aby jeho střed ležel na horní hraně pánevních kostí.</li>'
          '<li>Dotáhněte ramenní popruhy, až přilnou k ramenům. Nemají nést hlavní váhu, ta má zůstat na bocích.</li>'
          '<li>Stáhněte stabilizační popruhy nad rameny, pokud je batoh má, aby se horní část batohu přitáhla k zádům.</li>'
          '<li>Hrudní popruh zapněte nad hrudníkem a utáhněte jen lehce, aby nebránil dýchání.</li></ol>'
          '<p>Správně nastavený batoh se při chůzi nehoupe, ramenní popruhy nezařezávají a pod bederním pásem necítíte tlak na jednom místě. U batohů s nastavitelnými zády posuňte ramenní popruhy, pokud začínají příliš vysoko nebo příliš nízko nad rameny.</p>'
          '<h2>Dámské řady známých značek</h2>'
          '<p>V nabídce najdete dámské batohy u většiny turistických značek a často je poznáte už podle názvu. <a href="/znacka/deuter/">Deuter</a> přidává zkratku SL, třeba Trail 28 SL, Guide 22 SL, Trans Alpine 28 SL nebo Aircontact Core 45+10 SL. '
          '<a href="/znacka/osprey/">Osprey</a> má samostatné dámské řady: Kyte je ženský protějšek řady Kestrel a Tempest dámská obdoba Talonu. V nabídce jsou dále modely Sirrus, Renn nebo Ariel. '
          '<a href="/znacka/mammut/">Mammut</a> označuje dámské verze slovem Women, například Lithium Women, a <a href="/znacka/salewa/">Salewa</a> slovem Women nebo zkratkou Ws, třeba Alp Trainer nebo Alp Mate. Ferrino používá slovo Lady, třeba Agile Lady nebo Transalp 50 Lady, <a href="/znacka/fjallraven/">Fjällräven</a> písmeno W, jako u Keb 72 W. '
          'Dámské modely dále mají Millet, Lowe Alpine, Gregory, Tatonka, Vaude, Loap a Hannah.</p>'
          '<h2>Odvětrání zad: síťka, nebo polštářky</h2>'
          '<p>Turistické batohy používají dva základní typy zad. První má napnutou síťku, která drží batoh několik centimetrů od těla, a vzduch tak proudí podél celých zad. V létě a při výstupu do kopce se pod ní potíte méně. Těžiště je ale o něco dál od těla a batoh se hůř nakládá, protože vnitřní prostor je prohnutý. '
          'Druhý typ má tvarované polštářky s kanálky mezi nimi. Batoh přiléhá blíž k zádům, je stabilnější v náročném terénu a na lezeckých úsecích, odvětrání je ale slabší. Deuter například označuje síťová záda názvem Aircomfort a záda s polštářky Aircontact.</p>'
          '<h2>Kapsy a pití</h2>'
          '<p>Na túře se hodí mít drobnosti po ruce. Kapsy na bederním pásu pojmou telefon, tyčinku nebo opalovací krém, které pak nemusíte hledat v batohu. Boční kapsy na láhev by měly jít použít bez sundání batohu. '
          'Kdo pije průběžně, ocení přihrádku na hydratační vak s otvorem pro hadičku. Pružná přední kapsa slouží na mokrou pláštěnku nebo bundu, kterou chcete mít oddělenou od suchých věcí.</p>'
          '<h2>Kdy zvolit pánský nebo unisex batoh</h2>'
          '<p>Dámský střih není povinnost. Ženy s dlouhým trupem nebo širokými rameny často lépe využijí běžný nebo unisex batoh. Naopak muži s krátkými zády nebo úzkými rameny mohou být spokojenější s dámským modelem. Rozhoduje délka zad, obvod boků a to, jak batoh sedí, ne označení. '
          'Dobrou volbou bývají i batohy s nastavitelnými zády, které se dají doladit v širším rozsahu. Při nákupu online si proto vždy zjistěte rozsah délky zad v popisu výrobce.</p>'
          '<h2>Výbava, která se s batohem hodí</h2>'
          '<p>Batoh je jen část výbavy. K pohodlné túře patří i <a href="/damske-trekove-boty/">dámské trekové boty</a>, <a href="/damske-outdoorove-kalhoty/">dámské outdoorové kalhoty</a> a pro výstupy a sestupy <a href="/trekove-hole/">trekové hole</a>, které část zátěže přenesou do rukou. '
          'V batohu by neměla chybět <a href="/damska-nepromokava-bunda/">dámská nepromokavá bunda</a> a láhev z kategorie <a href="/lahve-a-termosky/">láhve a termosky</a>. Pokud batoh nemá vlastní pláštěnku, vyplatí se ji dokoupit, protože většina batohů není nepromokavá.</p>'
          '<h2>Hmotnost prázdného batohu</h2>'
          '<p>Na dlouhé túře se počítá každé kilo. Batohy stejného objemu se mohou lišit hmotností prázdného batohu o stovky gramů podle materiálu, rámu a výbavy. Lehký batoh se ale vyplatí jen tehdy, když nesete lehký náklad. '
          'U velkých batohů na vícedenní trek je pevný rám a dobře polstrovaný bederní pás důležitější než ušetřená váha, protože právě ony přenesou zátěž z ramen na boky. Údaj o hmotnosti najdete v popisu produktu.</p>'
          '<h2>Péče o batoh</h2>'
          '<p>Po túře batoh vyprázdněte, vytřepte drobky a nechte ho vyschnout otevřený. Pot ze zad a popruhů vymyjte vlažnou vodou s trochou jemného mýdla a houbou, batohy obvykle nepatří do pračky. Uložte ho na suchém místě, ne ve sklepě, kde může zplesnivět.</p>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Nejdřív si změřte délku zad a zvolte objem, potom porovnávejte konkrétní modely. U batohů s velikostmi XS/S a M/L si v nabídce ověřte, jakou velikost obchod nabízí. Sporteka sdružuje nabídky českých e-shopů na jednom místě. '
          'Přehled podle značek najdete na stránkách <a href="/deuter-batohy/">batohy Deuter</a>, <a href="/osprey-batoh/">batohy Osprey</a> a <a href="/fjallraven-batoh/">batohy Fjällräven</a>.</p>',
    faq=[
        ('Čím se liší dámský turistický batoh od pánského?', 'Má kratší záda, užší a víc prohnuté ramenní popruhy, posuvnější hrudní popruh a kuželovitě tvarovaný bederní pás. Lépe tak sedí na postavě s kratším trupem a širšími boky.'),
        ('Co znamená SL u batohů Deuter?', 'Slim Line, tedy dámský střih. Deuter u něj uvádí délku zad kolem 42 cm, užší ramena a kratší trup. Podle výrobce může vyhovovat i štíhlým mužům s kratšími zády.'),
        ('Jak změřit délku zad pro batoh?', 'Od sedmého krčního obratle, vystouplé kosti na spodu krku, k horní hraně pánevních kostí. Nejlépe ve dvou, metrem vedeným podél páteře. Údaj porovnejte s tabulkou výrobce.'),
        ('Jaký objem dámského batohu na jednodenní túru?', 'Většině žen stačí 20–30 litrů. Vejde se voda, jídlo, teplá vrstva, nepromokavá bunda a lékárnička. Na kratší výlety stačí i batoh do 20 litrů.'),
        ('Jaký batoh na túru s přespáním?', 'Na chatu stačí 30–40 litrů, na vícedenní trek se stanem a spacákem 45 litrů a víc. U velkých batohů je ještě důležitější správná délka zad a kvalitní bederní pás.'),
        ('Je Osprey Kyte dámský batoh?', 'Ano, Kyte je dámský protějšek řady Kestrel. Podobně Tempest je dámská obdoba řady Talon. Osprey je nabízí v několika objemech a velikostech.'),
        ('Může žena nosit pánský batoh?', 'Ano, pokud jí sedí. Ženám s delším trupem nebo širšími rameny často lépe vyhoví běžný nebo unisex batoh. Rozhoduje délka zad a obvod boků, ne označení.'),
        ('Kde má být bederní pás?', 'Jeho střed má ležet na horní hraně pánevních kostí. Bederní pás nese hlavní část váhy, ramenní popruhy batoh jen přidržují u těla.'),
        ('Proč batoh tlačí na ramena?', 'Nejčastěji je bederní pás povolený nebo moc nízko, případně má batoh špatnou délku zad. Utáhněte pás na bocích a zkontrolujte, kde začínají ramenní popruhy.'),
        ('Kde porovnat nabídky dámských turistických batohů?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Nákup dokončíte v e-shopu, kde ověříte velikost zad, objem a dostupnou barvu.'),
    ])
