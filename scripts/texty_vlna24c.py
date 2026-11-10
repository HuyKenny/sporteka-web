"""sporteka.cz — wave 24c (5. 11. 2026): long texts for mestska-elektrokola, rybarske-doplnky, mestska-kola, gainery.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ mestska-elektrokola
NEW['mestska-elektrokola'] = dict(long=True,
    title='Městská elektrokola: motor, baterie, rám a výbava',
    desc='Městská elektrokola na dojíždění: jak vybrat motor, baterii, rám, brzdy a výbavu, na co si dát pozor a jak o kolo pečovat. Porovnání obchodů.',
    intro='<p>Městské elektrokolo má nahradit auto nebo MHD na trasách, které jsou na obyčejné kolo trochu dlouhé nebo kopcovité. Jezdí se na něm v běžném oblečení, s kabelou na nosiči a bez pocení u cíle. Kategorie spojuje pohodlné modely se vzpřímeným sezením, blatníky, světly a často i nízkým nástupem, ale také lehčí „ebiky“ ve stylu městského kola a několik moderních kousků s řemenovým pohonem. Sporteka porovnává nabídky českých obchodů a u každého modelu zobrazí údaje o motoru, kapacitě baterie, velikosti kol a výbavě.</p>'
          '<p>V kategorii najdete například značky ' + B(('dyu', 'DYU'), ('hitway', 'Hitway'), ('samebike', 'Samebike'), ('ttgo', 'Ttgo'), ('moma-bikes', 'Moma Bikes'), ('urlife', 'Urlife'), ('devron', 'Devron'), ('elops', 'Elops'), ('jobobike', 'Jobobike')) +
          '. Pro delší výlety se hodí <a href="/trekingova-elektrokola/">trekingová elektrokola</a>, pro ženy <a href="/damska-elektrokola/">dámská elektrokola</a> a pro těsné byty <a href="/skladaci-elektrokola/">skládací elektrokola</a>.</p>',
    guide='<h2>Co dělá elektrokolo městským</h2>'
          '<p>Městské elektrokolo se od horského či silničního liší hlavně tím, že je postavené na každodenní praktičnost. Rám dovoluje nastoupit bez zvedání nohy přes příčku, řídítka jsou zvednutá nebo zahnutá k jezdci a sedlo je širší a měkčí. Výbava bývá hotová už z výroby: blatníky, světla, stojánek, zvonek a nosič. Pneumatiky mají hladší vzorek, který se v dešti i na dlažbě chová předvídatelně a méně hučí na asfaltu.</p>'
          '<p>V praxi se v kategorii potkáte se třemi proudy. Prvním jsou klasicky vyhlížející kola s motorem v zadním náboji a baterií v rámu, druhým lehčí „ebiky“ na dojíždění s tenkými pneumatikami a třetím modely s úzkým rámem a řemenem místo řetězu. Rozdíly jsou v hmotnosti, ceně údržby i v tom, jak se kolo chová do kopce.</p>'
          '<h2>Motor: kde sedí a jak jezdí</h2>'
          '<p>Motor v předním kole je nejjednodušší a nejlevnější řešení, ale přilnavost je horší při rozjezdu do kopce nebo na mokru, protože přední kolo odlehčuje. Zadní motor tlačí kolo přirozeněji a je v městských kolech nejčastější. Středový motor u pedálů pracuje s převody kola, proto dobře šplhá do kopců a rozkládá váhu k těžišti. Ke kolům s řemenem a nábojovou převodovkou se střed hodí jako bezúdržbová kombinace, bývá ale dražší.</p>'
          + T(['Poloha motoru', 'Jak se projevuje', 'Hodí se'], [
              ['Přední náboj', 'kolo je tahané, při prokluzu ztrácí přilnavost', 'rovinaté trasy, suchý povrch'],
              ['Zadní náboj', 'přirozený tlak jako při šlapání, snadná oprava kola', 'běžné dojíždění, mírné kopce'],
              ['Střed rámu', 'využívá převody, nižší těžiště', 'kopcovité trasy, častá zátěž nákupem'],
              ['Libovolná poloha se snímačem momentu', 'asistence reaguje na sílu šlapání', 'kdo chce plynulou, tichou jízdu']]) +
          '<p>Snímač točivého momentu měří, jak silně šlapete, a podle toho dávkuje pomoc. Jízda je plynulejší než u jednoduchého snímače otáček, který pomoc spustí po několika otočkách kliky. U městské jízdy ocení rozdíl hlavně ti, kdo se rozjíždějí na křižovatkách.</p>'
          '<h2>Baterie, nabíjení a dojezd</h2>'
          '<p>Baterie se popisuje napětím ve voltech a kapacitou v ampérhodinách, případně ve wattových hodinách. Kapacita ve Wh vznikne vynásobením obou čísel, takže baterie 36 V s 13 Ah odpovídá přibližně 470 Wh. Právě údaj ve Wh je nejspolehlivější pro porovnání dvou modelů. Skutečný dojezd ovlivňuje váha jezdce a nákladu, vítr, teplota, tlak v pneumatikách, počet rozjezdů i zvolený stupeň asistence. Výrobcovy hodnoty proto berte jako rozmezí.</p>'
          '<ul><li><strong>Vyjímatelná baterie</strong> se nabíjí v bytě nebo kanceláři, takže kolo nemusíte tahat po schodech.</li>'
          '<li><strong>Baterie ukrytá v rámu</strong> vypadá nenápadněji a chrání se před poškozením, ale u některých kol se snímá hůř.</li>'
          '<li><strong>Baterie na nosiči</strong> se lépe vyměňuje a bývá dostupnější, zvyšuje ale těžiště vzadu.</li>'
          '<li><strong>Nabíječka</strong> má odpovídat modelu, ne jen konektoru. Cizí nabíječka může baterii poškodit.</li></ul>'
          '<p>Další tipy k úložišti, výměně článků a náhradním bateriím najdete v kategorii <a href="/ebike-baterie/">baterie pro elektrokola</a>.</p>'
          '<h2>Rám, velikost kol a nástup</h2>'
          '<p>U městských modelů se setkáte s koly o průměru 26, 27,5 a 28 palců, případně s lehčími 700C. Větší kola lépe přejedou obrubníky a díry, menší jsou obratnější a snižují těžiště. Nízký nástup je pohodlný pro všechny, nejen pro ženy, ale rám bývá o něco méně tuhý. Klasický rám s horní trubkou nese větší zátěž, takže se hodí těžším jezdcům a na nákup s nosičem.</p>'
          '<p>Velikost rámu se volí podle výšky postavy a délky nohou. Elektrokolo je těžké, proto je dobré ho před koupí aspoň rozhýbat a zkusit nasednout. Při sezení na sedle má špička nohy dosáhnout na zem a kolena mají být při šlapání mírně pokrčená. Výškově stavitelná řídítka a představec pomohou doladit sezení po koupi.</p>'
          '<h2>Brzdy, převody a pohon</h2>'
          '<p>Elektrokolo je těžší a rychlejší než běžné kolo, takže brzdy hrají větší roli. Kotoučové brzdy brzdí stejně i za deště a odolají delšímu klesání, ráfkové brzdy jsou jednodušší na údržbu. Hydraulické kotouče mají jemnější ovládání než mechanické, ale hůř se seřizují bez zkušenosti.</p>'
          '<ul><li><strong>Přehazovačka a kazeta</strong> (například Shimano na 7 rychlostí) je rozšířená, lehká a dobře opravitelná.</li>'
          '<li><strong>Nábojová převodovka</strong> je chráněná a řadí se i ve stoji, ocení ji lidé, kteří nechtějí řešit mazání řetězu.</li>'
          '<li><strong>Řemenový pohon</strong> je čistý a tichý, nevyžaduje mazání, ale vyžaduje speciální rám a při poruše se těžko nahrazuje.</li></ul>'
          '<h2>Hmotnost a každodenní manipulace</h2>'
          '<p>Městské elektrokolo je těžší než běžné, a to nejen kvůli baterii. Silnější rám a nosič přidávají další kilogramy. Než ho vyberete, zvažte, kam budete kolo ukládat. Pokud bydlíte v panelovém domě bez výtahu nebo kolo nosíte do sklepa, vyplatí se lehčí model a baterie, kterou lze snímat. Zvládnout musíte také zvedání na nosič auta, pro které existují speciální <a href="/cyklo-nosice-na-auto/">nosiče kol na auto</a> s nájezdovou lištou.</p>'
          '<h2>Výbava, která se hodí ve městě</h2>'
          '<ul><li><strong>Světla napájená z baterie</strong> svítí vždy, nemusíte řešit baterie ani dynamo. Další modely najdete v kategorii <a href="/cyklo-svetla/">světla na kolo</a>.</li>'
          '<li><strong>Blatníky a kryt řetězu</strong> udrží oblečení čisté. Případné náhradní kusy jsou v kategorii <a href="/cyklo-blatniky/">blatníky</a>.</li>'
          '<li><strong>Nosič a tašky</strong> se hodí na každodenní věci. Skladba tašek a košíků je v kategorii <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>.</li>'
          '<li><strong>Stojánek</strong> musí unést hmotnost elektrokola, kontrolujte ho před nákupem.</li>'
          '<li><strong>Odpružená sedlovka</strong> zjemní rázy na dlažbě.</li></ul>'
          '<h2>Pravidla a legislativa</h2>'
          '<p>Podle českých předpisů se jako jízdní kolo posuzuje elektrokolo, jehož motor má jmenovitý výkon do 250 W a pomáhá jen při šlapání do 25 km/h. Pro takové kolo není nutné řidičské oprávnění, registrace ani pojištění odpovědnosti. Modely s tlačítkem „plyn“ nebo s motorem nad tuto hranici jsou jiná kategorie vozidel a při koupi je vždy třeba ověřit, zda se na ně nevztahují další povinnosti. Informace v textu mají obecný charakter, vždy se řiďte aktuální legislativou.</p>'
          '<h2>Péče a údržba městského elektrokola</h2>'
          '<ul><li>Tlak v pneumatikách kontrolujte každé dva týdny, pomůže dojezdu i bezpečnosti. K tomu slouží <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</li>'
          '<li>Řetěz čistěte a mažte podle provozu, u kol s řemenem sledujte napnutí.</li>'
          '<li>Baterii skladujte v suchu při pokojové teplotě. Před dlouhou přestávkou ji nenechávejte vybitou ani plně nabitou. Doporučení výrobce ale vždy stojí na prvním místě.</li>'
          '<li>Kolo neomývejte tlakovou vodou, vniká do ložisek a konektorů.</li>'
          '<li>Brzdové destičky a plášť měňte včas, těžší kolo je opotřebovává rychleji. Vhodné postupy najdete v kategorii <a href="/cyklo-udrzba/">údržba kol</a>.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Porovnávání jen podle voltů a ampérhodin bez přepočtu na Wh.</li>'
          '<li>Podcenění hmotnosti kola, které se hůř nosí než jezdí.</li>'
          '<li>Koupě bez dostupného servisu. Pokud je baterie nebo motor specifický, hledejte, kdo ho opraví.</li>'
          '<li>Zapomenutý zámek. Elektrokolo je lákavý cíl, viz <a href="/cyklo-zamky/">zámky na kola</a>.</li>'
          '<li>Jízda bez helmy. Rychlost 25 km/h je na městské komunikaci vysoká, vyberte z <a href="/cyklisticke-helmy/">cyklistických helem</a>.</li></ul>'
          '<h2>Pro koho se městské elektrokolo hodí</h2>'
          '<p>Hodí se dojíždějícím do práce na trase mezi pěti a dvaceti kilometry, rodičům vozícím děti do školky, seniorům, kteří chtějí zůstat v pohybu, i lidem z kopcovitých měst. Pokud plánujete spíš víkendové výlety po cyklostezkách, projděte si nejdřív <a href="/trekingova-elektrokola/">trekingová elektrokola</a>. Pokud jezdíte po lesních cestách, hledejte v kategorii <a href="/horska-elektrokola/">horská elektrokola</a>. Široký přehled celé nabídky najdete v kategorii <a href="/elektrokola/">elektrokola</a> a mezi obyčejnými koly v oddíle <a href="/jizdni-kola/">jízdní kola</a>.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Nabídku tvoří od jednoduchých levnějších modelů s 36V baterií po kola s řemenem, snímačem točivého momentu a vyšším výkonem. Najdete tu městská kola Elops, Specialized a řadu menších značek, které prodávají především přes e-shopy. U některých modelů se opakují stejné rámy s různým označením, proto při porovnání sledujte baterii, motor a brzdy, nikoli jen název.</p>',
    faq=[('Jak se liší městské elektrokolo od trekingového?', 'Městské je určené na krátké denní trasy po rovině a po dlažbě, má vzpřímenější sezení a často nízký nástup. Trekingové snese delší cesty, nosí víc zavazadel a má větší baterii i širší převodový rozsah.'),
         ('Jakou kapacitu baterie zvolit na dojíždění?', 'Počítejte s tím, že na jedné cestě v kopcovitém městě spotřebujete víc než po rovině. Pro denní dojíždění do pár kilometrů stačí menší baterie, pro trasu tam a zpět bez dobíjení volte kapacitu s rezervou. Rozhodující je údaj ve Wh.'),
         ('Musím mít na městské elektrokolo registraci nebo pojištění?', 'Pokud motor má jmenovitý výkon do 250 W a pomáhá pouze při šlapání do 25 km/h, považuje se elektrokolo za jízdní kolo a registraci ani povinné ručení nepotřebujete. Model s plynem nebo vyšším výkonem je jiné vozidlo.'),
         ('Jak daleko dojedu na jedno nabití?', 'Záleží na kapacitě baterie, váze jezdce, terénu, počasí a stupni asistence. Výrobce uvádí rozmezí a v praxi je spodní hranice reálnější. Kratší dojezd je v zimě, při větru a v kopcích.'),
         ('Je lepší zadní nebo středový motor?', 'Zadní motor je jednodušší a pro městské dojíždění obvykle stačí. Středový motor dává přirozenější vedení kola a lépe zvládá strmé kopce, protože využívá převody. Rozdíl pocítíte hlavně při rozjezdech a v prudkém stoupání.'),
         ('Jak často se musí nabíjet baterie?', 'Podle počtu ujetých kilometrů. Praktické je dobíjet ji po jízdě, nemusíte ji vybíjet do nuly. Pokud kolo nepoužíváte, zkontrolujte její stav alespoň jednou za několik týdnů a nabijte ji podle pokynů výrobce.'),
         ('Mohu s elektrokolem jezdit v dešti?', 'Ano, kola jsou na déšť stavěná. Vyhněte se hlubokým kalužím a nemyjte kolo tlakovou vodou. Po mokré jízdě osušte konektory a baterii nechte před nabíjením zaschnout.'),
         ('Čím se liší řemenový pohon od řetězu?', 'Řemen nevyžaduje mazání, nešpiní kalhoty a je tichý. Potřebuje ale speciální rám s dělitelným zadním trojúhelníkem nebo oddělenou vidličkou a jeho výměna je dražší. Řetěz je levnější a snadněji dostupný.'),
         ('Jak zabezpečit elektrokolo proti krádeži?', 'Použijte kvalitní zámek, který připoutá rám a kolo k pevnému bodu. Baterii snímejte, pokud ji lze vyjmout, a kolo neparkujte celou noc na ulici. Pomůže také označení rámu a záznam sériového čísla.'),
         ('Kolik váží městské elektrokolo a zvládnu ho do schodů?', 'Obvykle několik desítek kilogramů s baterií, přesněji v popisu konkrétního modelu. Pokud kolo musíte nosit po schodech, vybírejte lehký rám a snímací baterii nebo si předem ověřte, kde ho budete odkládat.'),
         ('Kdy je dobré koupit elektrokolo?', 'Nejlepší výběr bývá na jaře, ale slevy se objevují i na podzim. Sporteka ukazuje aktuální nabídky v obchodech, takže sledujte skladovost své velikosti, ta se mění rychle.')],
)

# ------------------------------------------------------------------ mestska-kola
NEW['mestska-kola'] = dict(long=True,
    title='Městská kola: rám, převody, velikost a výbava',
    desc='Městská kola na každodenní jízdu: jak vybrat rám, velikost, převody, brzdy a výbavu, co sledovat u dámských a pánských modelů a jak kolo udržovat.',
    intro='<p>Městské kolo je stroj na každodenní cesty: do práce, na trh, za kamarády nebo do parku. Nejde o rychlost a nízkou hmotnost, ale o pohodlí, spolehlivost a to, že na něm můžete jet v běžném oblečení. Typické městské kolo má vzpřímenou polohu, široké sedlo, blatníky, nosič a světla. Kategorie na Sportece zahrnuje klasicky stylizované modely s ocelovým i hliníkovým rámem, dámské verze s nízkým nástupem, retro kola s košíkem i moderní kousky s nábojovou převodovkou.</p>'
          '<p>Z nabídky vynikají značky ' + B(('davi', 'Davi'), ('author', 'Author'), ('storm', 'Storm'), ('canellini', 'Canellini'), ('elops', 'Elops'), ('f-lli-schiano', 'F.lli Schiano'), ('dhs', 'Dhs'), ('leader-fox', 'Leader Fox'), ('kellys', 'Kellys')) +
          '. Pokud hledáte spíš delší výlety, podívejte se na <a href="/trekingova-kola/">trekingová kola</a>, pro ženy je tu <a href="/damska-kola/">kategorie dámských kol</a> a pro tenčí pneumatiky <a href="/krosova-kola/">krosová kola</a>.</p>',
    guide='<h2>Co řadíme mezi městská kola</h2>'
          '<p>Hranice mezi městským, trekingovým a krosovým kolem je plynulá. Městské kolo je nejvíc zaměřené na krátké trasy po rovině a špatně se hodí na dlouhé výlety s kopci. Má pohodlnou polohu, větší důraz na ochranu oblečení a výbavu hotovou z výroby. Naopak vyšší hmotnost, širší pneumatiky a nižší počet převodů jsou cena za tuto praktičnost.</p>'
          + T(['Typ městského kola', 'Charakteristika', 'Hodí se'], [
              ['Klasické holandské', 'vzpřímené sezení, nízký nástup, často nábojové převody', 'každodenní jízda, pohodlí, sukně'],
              ['Retro a vintage', 'ocelový rám, košík, oblé tvary', 'procházky, kavárny, styl'],
              ['Městský hybrid', 'lehčí hliník, užší pneumatiky, přehazovačka', 'rychlejší dojíždění'],
              ['Fixie a singlespeed', 'jeden převod, minimum dílů', 'plochá města, kdo chce jednoduchost'],
              ['Pánské s horní trubkou', 'tužší rám, větší nosnost', 'těžší nákup, vyšší jezdci']]) +
          '<h2>Rám: materiál, tvar a nástup</h2>'
          '<p>Ocelový rám je pružný, snese záběry a dá se v servisu opravit, ale je těžší a při poškození laku může rezavět. Hliník je lehčí, nekoroduje a hodí se na dojíždění po schodech, je ale tužší, takže přenáší víc otřesů. Rámy se liší i tvarem: <strong>nízký nástup</strong> je pohodlný pro všechny a usnadňuje zastavování na křižovatce, <strong>horní trubka</strong> dodává tuhost. Dámské modely mívají nižší rám a často zakrytý řetěz.</p>'
          '<h2>Velikost kola a rámu</h2>'
          '<p>Rám se označuje v palcích nebo v centimetrech a kola mívají průměr 26, 27,5 nebo 28 palců. Čím vyšší jezdec, tím větší rám. Orientační rozmezí uvádí většina výrobců, například jako výšku postavy od–do, a v nabídce Sporteky se objevují právě takové údaje. Pokud jste mezi dvěma velikostmi, upřednostněte menší rám s delším představcem, je lépe ovladatelný než příliš velký.</p>'
          '<ul><li><strong>Výška sedla</strong> nastavte tak, aby noha při spodní poloze pedálu byla mírně pokrčená.</li>'
          '<li><strong>Poloha řídítek</strong> pomůže odlehčit zádům. Sklopná řídítka se hodí do menších bytů.</li>'
          '<li><strong>Kola 26"</strong> jsou obratnější, <strong>28"</strong> lépe přejedou nerovnosti a drží rychlost.</li></ul>'
          '<h2>Převody a pohon</h2>'
          '<p>Mezi městskými koly najdete jednu rychlost, tři, sedm i více. Jednorychlostní kolo je lehké a nenáročné, ale v kopci vás rychle unaví. Nábojové převody (obvykle 3 až 8 rychlostí) jsou skryté v zadním náboji, řadí se i při stání a nemusíte řešit seřízení přehazovačky. Přehazovačka se šesti nebo sedmi kolečky má lepší účinnost a stačí na většinu měst. Zadní kazeta a řetěz jsou spotřební díly, které se dají snadno vyměnit.</p>'
          '<p>Pokud bydlíte v kopcovitém městě, volte víc převodů a menší největší rozdíl mezi převody. Jedete-li po rovině, nepotřebujete víc než tři. Další komponenty, jako jsou kliky, pedály a řetězy, nabízí kategorie <a href="/cyklo-pohon/">pohon a převody</a>.</p>'
          '<h2>Brzdy</h2>'
          '<ul><li><strong>Ráfkové V-brzdy</strong> jsou jednoduché a dobře seřiditelné, za deště brzdí slaběji.</li>'
          '<li><strong>Pedálová torpédová brzda</strong> se aktivuje šlápnutím pozpátku, hodí se u retro kol, kde ji často doplňuje ruční brzda na přední kolo.</li>'
          '<li><strong>Bubnové a kotoučové brzdy</strong> zvládají déšť lépe, bubnové jsou chráněné a málo údržbové.</li></ul>'
          '<p>Brzdy se opotřebovávají a vyžadují občasnou kontrolu. Viz <a href="/cyklo-brzdy/">brzdy na kola</a>.</p>'
          '<h2>Výbava, která šetří nervy</h2>'
          '<p>Nejpraktičtější městské kolo má vše v základu. Blatníky chrání oděv před špínou, kryt řetězu před olejem, nosič a košík ocení každý, kdo vozí nákup. Stojánek a zvonek jsou samozřejmost, světla doplňte kvalitním modelem z kategorie <a href="/cyklo-svetla/">světla na kolo</a>. Silnější <a href="/cyklo-zamky/">zámek</a> je ve městě povinná součást vybavení, nejlépe U-zámek v kombinaci s kabelem pro druhé kolo.</p>'
          '<ul><li>Zadní nosič obvykle unese několik desítek kilogramů, přesný údaj najdete u každého modelu.</li>'
          '<li>Dynamo v náboji je spolehlivé, ale mírně brzdí, LED světla s akumulátorem jsou lehčí a hodí se k doplnění.</li>'
          '<li>Pro nákup se hodí sady tašek z <a href="/cyklo-tasky-a-nosice/">tašek a nosičů</a>.</li></ul>'
          '<h2>Pro koho se které městské kolo hodí</h2>'
          '<ul><li><strong>Dojíždějící do práce:</strong> hliníkový rám, 7 rychlostí a pevné blatníky.</li>'
          '<li><strong>Senior nebo jezdec s citlivými zády:</strong> nízký nástup, široké sedlo a vzpřímená poloha.</li>'
          '<li><strong>Student:</strong> lehčí kolo se zámkem a světly, které nevadí, když se trochu ošoupe.</li>'
          '<li><strong>Retro nadšenec:</strong> ocelový rám, košík a klasické zvonky.</li>'
          '<li><strong>Ten, kdo jezdí do kopců:</strong> zvažte raději <a href="/mestska-elektrokola/">městské elektrokolo</a> nebo <a href="/skladaci-kola/">skládací kolo</a> pro přenos vlakem.</li></ul>'
          '<h2>Péče a údržba</h2>'
          '<p>Základ je pravidelné nafukování plášťů, mazání řetězu a kontrola brzd. Pneumatiky ztrácejí tlak i bez jízdy, proto je dobré měřit ho jednou za dva týdny. Řetěz očistěte hadrem a promažte lehkým olejem, přebytek otřete. Ocelové rámy chraňte před rzí, drobné odřeniny lakem zatřete. O pumpách a nářadí viz <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>, o dalších postupech <a href="/cyklo-udrzba/">údržba kol</a>.</p>'
          '<ul><li>Jednou ročně nechte zkontrolovat ložiska, drátky a brzdy v servisu.</li>'
          '<li>Kolo skladujte v suchu, ideálně pod střechou.</li>'
          '<li>Po dešti kolo osušte, hlavně řetěz a brzdy.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš velký rám, který nutí k nepohodlné poloze.</li>'
          '<li>Výběr jen podle barvy bez ohledu na brzdy a převody.</li>'
          '<li>Nepodcenit hmotnost, pokud kolo nosíte po schodech.</li>'
          '<li>Levný zámek, který se dá přeříznout během minuty.</li>'
          '<li>Opomenutí helmy a světel, viz <a href="/mestske-cyklohelmy/">městské cyklohelmy</a>.</li></ul>'
          '<h2>Pneumatiky a pohodlí na dlažbě</h2>'
          '<p>Šířka pláště rozhoduje o komfortu víc než odpružení, které městská kola většinou nemají. Širší plášť s nižším tlakem pohltí kostky a nerovnosti, užší jede lehčeji po asfaltu. Hladký vzorek vyhovuje městu, jemný vzorek s reflexním bokem přidává viditelnost za tmy. Pokud jezdíte po štěrkových cestách a v parku, zvolte plášť s mírně hrubším profilem. Ráfky a pláště najdete v kategorii <a href="/cyklo-kola-a-rafky/">kola a ráfky</a>. Pláště s ochrannou vložkou jsou těžší, ale lépe odolávají střepům a trnům, takže zastavujete méně často kvůli defektu.</p>'
          '<h2>Dámská a pánská městská kola</h2>'
          '<p>Rozdíl je především v rámu. Dámská varianta má nízký průchod, pánská horní trubku. Jinak jde o stejné kolo, sedlo se obvykle liší šířkou, protože ženy mívají širší sedací kosti. Nízký rám ocení každý, kdo často zastavuje, vozí nákup nebo jezdí v dlouhém kabátě, a proto ho mnoho mužů volí také. Další modely s nízkým rámem a různými barvami najdete v <a href="/damska-kola/">dámských kolech</a>.</p>'
          '<h2>Bezpečnost a viditelnost</h2>'
          '<p>Ve městě se největší nebezpečí skrývá v křižovatkách a při výjezdech z parkovacích míst. Světla zapínejte i za šera, reflexní prvky pomáhají i přes den. Zvonek a zpětné zrcátko zvyšují přehled. Pokud jezdíte do práce, mějte po ruce náhradní duši a malé nářadí, protože defekt je nejčastější porucha. Zvonky a zrcátka najdete v kategorii <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>.</p>'
          '<h2>Kdy kolo koupit a jak ho převzít</h2>'
          '<p>Nejširší výběr velikostí bývá na začátku jara, zatímco koncem léta se často objevují poslední kusy modelů předchozí sezony. Při srovnání nabídek sledujte, zda je v obchodě skladem vaše velikost, a ověřte dopravu i způsob předání: část kol se prodává částečně smontovaná a před jízdou je nutné dotáhnout řídítka, pedály a seřídit brzdy. Pokud si nejste jistí, nechte kolo zkontrolovat v servisu.</p>'
          '<h2>Zabezpečení a pojištění kola</h2>'
          '<p>Kolo ve městě je nejčastěji ohroženo krádeží. Zamykejte vždy rám a alespoň jedno kolo k pevnému objektu, ideálně na viditelném a osvětleném místě. Dva různé zámky, například U-zámek a řetěz, zvyšují odolnost, protože vyžadují různé nástroje. Ceduli s číslem rámu a fotografii kola uschovejte pro případ ztráty a zvažte i pojištění domácnosti, které může kolo zahrnovat. Přehled zámků najdete v kategorii <a href="/cyklo-zamky/">zámky na kola</a>.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Z hlediska počtu produktů převládá značka Davi s dámskými i pánskými modely v různých velikostech rámu, následují Author, Storm, Canellini, Elops a F.lli Schiano. Objevují se tu i modely Orbea, Btwin a Kellys. Některá kola se v nabídce opakují v několika velikostech, proto při srovnání sledujte údaj o výšce postavy a počtu převodů.</p>',
    faq=[('Jaké městské kolo vybrat pro každodenní dojíždění?', 'Rozhodují trasa a výbava. Na rovině vystačíte s několika převody, v kopcích volte víc rychlostí. Důležité jsou blatníky, světla, nosič a spolehlivé brzdy, které zvládnou i déšť.'),
         ('Jakou velikost městského kola si mám vybrat?', 'Podle výšky postavy a délky nohou. Výrobce většinou uvádí rozmezí v centimetrech pro každou velikost rámu. Při sezení na sedle byste měli dosáhnout aspoň špičkami na zem a při šlapání mít koleno mírně pokrčené.'),
         ('Je lepší nábojová převodovka, nebo přehazovačka?', 'Nábojová převodovka je chráněná, řadí se i na místě a nevyžaduje seřizování, ale bývá těžší. Přehazovačka je lehčí, má více rychlostí a lépe se opravuje. Pro město bez velkých kopců je nábojová volba pohodlná.'),
         ('Jaký materiál rámu je lepší?', 'Ocel je pružná a opravitelná, hliník lehčí a bez koroze. Pro každodenní nošení po schodech zvolte hliník, pro pohodlí a klasický vzhled ocel. Důležitější než materiál bývá kvalita svarů a výbava.'),
         ('Hodí se městské kolo i na výlety?', 'Na krátké okružní výlety po rovině ano. Na delší trasy a kopce je lepší trekingové kolo, které má lehčí rám, širší převodový rozsah a pohodlnější geometrii pro několik hodin v sedle.'),
         ('Co znamená nízký nástup a komu se hodí?', 'Nízký nástup je rám bez horní trubky, takže přes něj nemusíte přehazovat nohu. Hodí se seniorům, lidem v sukni nebo s nákupem a také každému, kdo často zastavuje a nasedá, třeba ve městě.'),
         ('Potřebuji na městské kolo světla?', 'Ano, za snížené viditelnosti musí mít kolo přední bílé a zadní červené světlo. Dále se vyžadují odrazky a funkční brzdy. Světla si můžete koupit samostatně a snímat je při parkování.'),
         ('Jak zabezpečit městské kolo před krádeží?', 'Použijte pevný zámek, který zajistí rám a zadní kolo k pevnému objektu. Nenechávejte kolo přes noc na ulici, pokud to jde. Pomáhá také zapsat sériové číslo rámu a pořídit fotky pro policii.'),
         ('Jak často kolo servisovat?', 'Základní kontrolu proveďte před každou sezonou a po větších ujetých vzdálenostech. Pokud kolo používáte denně, nechte jednou ročně přezkoušet brzdy, ložiska a výplet kol v servisu a průběžně doplňujte tlak v pneumatikách.'),
         ('Mohu si na městské kolo namontovat dětskou sedačku?', 'Mnoho kol to umožňuje, ale ověřte nosnost nosiče a rámu u výrobce. Pro sedačku na rám nebo nosič potřebujete správný typ upevnění a nákupem se vybírá zvláštní výbava. Zvažte i dětskou helmu.')],
)

# ------------------------------------------------------------------ rybarske-doplnky
NEW['rybarske-doplnky'] = dict(long=True,
    title='Rybářské doplňky: rod pody, křesla a stolky',
    desc='Rod pody, kaprová křesla, stolky a lůžka pro rybáře. Jak vybrat stojan na pruty, nosnost, materiál a výbavu na dlouhé zasedání u vody.',
    intro='<p>Kdo rybaří delší dobu, rychle zjistí, že samotný prut a naviják nestačí. Na břehu se potřebuje pohodlně sedět, odložit nástrahy, uložit pruty tak, aby se nepoškodily, a hlídat záběr bez držení prutu v ruce. Kategorie rybářské doplňky na Sportece se proto soustředí hlavně na výbavu k lovu na dlouhé zasedání, především kaprařskou: rod pody a stojany na pruty, rybářská křesla a židle, stolky u bivaku a kaprová lůžka. Každý produkt porovnáme napříč obchody a uvedeme rozměry, nosnost nebo počet prutů.</p>'
          '<p>V nabídce převažují značky ' + B(('mikado', 'Mikado'), ('delphin', 'Delphin'), ('zfish', 'Zfish'), ('giants-fishing', 'Giants Fishing'), ('prologic', 'Prologic'), ('mivardi', 'Mivardi'), ('sonik', 'Sonik'), ('trakker-products', 'Trakker'), ('fox', 'Fox')) +
          '. K výbavě na břeh patří <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/rybarske-navijaky/">navijáky</a>, <a href="/rybarske-tasky/">tašky a pouzdra</a> a <a href="/rybarske-stany/">rybářské stany</a>.</p>',
    guide='<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Název „doplňky“ je široký, ale v praxi tu převládá nábytek a stojany pro delší zasedání. Velkou část nabídky tvoří <strong>rod pody</strong>, tedy skládací stojany na dva až čtyři pruty se zabudovanými hlavicemi. Dále tu najdete kaprová křesla s nastavitelnými nohami, rybářské židle, stolky ke stanu a kaprové postele, které se po složení vejdou do auta. Drobné potřeby jako nástrahy, háčky a náčiní hledejte v kategoriích <a href="/nastrahy-a-navnady/">nástrahy a návnady</a> a <a href="/vlasce-a-snury/">vlasce a šňůry</a>.</p>'
          + T(['Doplněk', 'K čemu slouží', 'Na co dát pozor'], [
              ['Rod pod', 'stojan na 2 až 4 pruty se signalizací záběru', 'stabilita na měkkém břehu, výška, šířka'],
              ['Přenosný stojan na loď', 'upevnění prutů na čluně nebo lodi', 'ukotvení, tvar bočnice'],
              ['Křeslo', 'pohodlné sezení několik hodin', 'nastavitelné nohy, nosnost, opěrka'],
              ['Židle', 'lehčí a levnější alternativa', 'váha, stabilita, polstrování'],
              ['Stolek', 'odkládání nástrah, jídla, nářadí', 'rozměr, výška, skládání'],
              ['Lůžko', 'spaní na břehu, často s nastavitelným sklonem', 'rozměr, nosnost, váha při přenosu']]) +
          '<h2>Rod pod: jak funguje a jak vybrat</h2>'
          '<p>Rod pod je kovová konstrukce, která stojí na třech nebo čtyřech nohách a drží pruty ve vodorovné nebo mírně skloněné poloze. Na jeho přední části sedí hlavice s rýhou pro prut, vzadu opěra pro rukojeť. Mnoho modelů má už v sadě signalizátory záběru, které zapípají nebo se rozsvítí, když ryba zabere. Pro začátečníka se hodí kompletní sada, pokročilí kapraři dávají přednost samostatnému podu bez signalizátorů a vybaví jej dle potřeby.</p>'
          '<ul><li><strong>Počet prutů:</strong> dva až tři jsou běžné. Čtyři se vyplatí, pokud místní předpisy dovolují víc prutů, ale pod je pak širší a těžší.</li>'
          '<li><strong>Šířka a výška:</strong> nastavitelné nohy dorovnávají nerovný břeh. Prut má držet při zasekávání bezpečně a ne se uvolňovat.</li>'
          '<li><strong>Materiál:</strong> nerez je odolný proti korozi, hliník lehčí a vhodný pro vzdálenější pěší cesty. Plastové součásti se často lámou na mrazu.</li>'
          '<li><strong>Kompatibilita:</strong> závity pro signalizátory a hlavice mívají standardní rozteč, přesto ověřte popis.</li>'
          '<li><strong>Přenos:</strong> pod ve vlastní tašce je lepší než volné kusy, které se rozpadnou v kufru.</li></ul>'
          '<h2>Rybářské křeslo a židle</h2>'
          '<p>Rybář sedí u vody i desítky hodin, takže na kvalitě křesla záleží. Kaprová křesla mají kovový rám, polstrovaný sedák, opěradlo a nastavitelné nohy, které se vyrovnají po nerovné půdě. Mívají i područky a někdy kapsy na drobnosti. Nízké židle bez opěrky se hodí pro krátké výjezdy a přívlač, kde se rybář pohybuje. Někdy jde o hybrid mezi sedačkou a lehátkem, který se po sklopení opěradla změní v krátké lehátko.</p>'
          '<ul><li><strong>Nosnost:</strong> porovnávejte údaj výrobce s vlastní hmotností a hmotností batohu na sedáku.</li>'
          '<li><strong>Nohy:</strong> teleskopické nohy musí mít pevné zámky, jinak se pod váhou zasunou. Nohy s širokými patkami nezapadají do bahna.</li>'
          '<li><strong>Čalounění:</strong> nenasákavé tkaniny rychle schnou a snášejí rosu. Silnější polstrování pohodlí zlepší, ale zvýší váhu a objem.</li>'
          '<li><strong>Opěradlo:</strong> nastavitelné opěradlo se hodí na dlouhé zasedání, vzpřímené na krátkou jízdu.</li>'
          '<li><strong>Skládání:</strong> kompaktní křeslo se vejde do kufru, ale širší a robustní obsadí celý prostor.</li></ul>'
          '<p>Další křesla a bivaková lehátka jsou v kategorii <a href="/bivaky-a-kresla/">bivaky a křesla</a>, kempingový nábytek obecně v <a href="/kempingovy-nabytek/">kempingovém nábytku</a>.</p>'
          '<h2>Stolky u bivaku</h2>'
          '<p>Stolek u rybářského bivaku drží krabičky s nástrahami, vařič, jídlo, svítilnu, mobil i nářadí. Praktický je model s nastavitelnými nohami, protože půda u vody je nerovná. Hodí se protiskluzová deska a boční kapsy. Skládací stolek je malý a lehký, větší pojme víc věcí, ale vyžaduje pevný podklad. Při používání v bivaku sledujte rozměr stolku, aby se ještě vešel mezi postel a vchod.</p>'
          '<h2>Lůžko a bivakový komfort</h2>'
          '<p>Kaprová postel je skládací lůžko s tuhým rámem a nastavitelnými nohami. Chrání před vlhkem a studenou zemí, srovnává nerovnosti a po dlouhých nocích šetří záda. Modely s více nohama nesou větší zátěž, ale zabírají víc místa a váží víc. K lůžku se hodí <a href="/rybarske-spacaky/">rybářský spacák</a> a přikrývka, spolu s ním tvoří kompletní spaní u vody. Pro ochranu před deštěm slouží <a href="/rybarske-stany/">rybářské stany</a> a bivaky.</p>'
          '<h2>Signalizátory, hlavice a drobné součásti</h2>'
          '<p>Signalizátor záběru reaguje na pohyb vlasce a upozorní zvukem nebo světlem. Elektronické modely se nastavují na citlivost a hlasitost, což se hodí v noci i za větru. Hlavice na stojanu určují, jak prut leží: otevřené s rýhou jsou rychlé na zakládání, zavřené s pojistkou drží i při silném záběru. Při koupi zkontrolujte, zda máte volné závity a zda hlavice odpovídá průměru prutu. Praktické doplňky jsou nohy s patkami na měkkou zem, popruh na nošení a pouzdro, aby pod nepoškrábal ostatní výbavu.</p>'
          '<h2>Jak pod postavit u vody</h2>'
          '<ul><li>Zvolte rovné místo, kde stojan nezapadne do bahna. Pokud břeh klesá, nastavte nohy tak, aby byl pod vodorovně.</li><li>Zapíchněte nebo zajistěte přední nohy, aby se konstrukce při záběru nepohnula.</li><li>Prut položte s uvolněnou brzdou nebo zapnutým volnoběhem navijáku, podle toho, jak lovíte, viz <a href="/rybarske-navijaky/">navijáky</a>.</li><li>Signalizátor nastavte tak, aby ho bylo slyšet z křesla, ale nerušil okolní rybáře.</li><li>Při změně počasí kontrolujte stabilitu, vítr a podmáčená půda mohou stojan nakloněním uvolnit.</li></ul>'
          '<h2>Ohleduplnost u vody a bezpečnost</h2>'
          '<p>Dlouhé zasedání u vody se vyplatí plánovat. Dodržujte revírový řád, který určuje počet prutů, dobu lovu a způsob nocování. Odnášejte odpadky, nenechávejte u vody vlasec ani nástrahy, ohrožují zvířata. V noci používejte čelovku, aby nikdo nezakopl o vaše vybavení, a při bouřce přerušte lov, odložte pruty a pody a odejděte od vody do úkrytu, ne pod osamělý strom. Základní lékárničku i repelent proti hmyzu najdete v <a href="/prvni-pomoc/">první pomoci</a> a v kategorii <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>.</p>'
          '<h2>Jak vybrat podle způsobu rybaření</h2>'
          '<ul><li><strong>Kapraři na delší zasedání:</strong> pod, křeslo s opěradlem, stolek a lůžko jsou základ komfortu.</li>'
          '<li><strong>Rybář na jednodenní výlet:</strong> lehká židle, skládací stolek a stojan na dva pruty, které se vejdou do jedné tašky.</li>'
          '<li><strong>Rybáři z lodi:</strong> stojan na bok lodi, ukotvení a menší sedátko. Plavidla a elektroniku najdete v kategorii <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>.</li>'
          '<li><strong>Rybaření s dětmi:</strong> stabilní židle a stolek, který se nepřevrhne, a jednoduchý stojan, který zvládne i malý rybář.</li></ul>'
          '<h2>Materiály a odolnost</h2>'
          '<p>Rybářské doplňky se používají venku, v rose a vlhku, proto zvažujte, z čeho jsou. Hliník je lehký a nerezaví, ocel je pevnější, ale potřebuje povrchovou úpravu proti korozi. Nerez je nejodolnější, ale nejdražší a těžší. Tkaniny s polyesterovou nebo nylonovou nití odolají plísním a snadno se otírají. Plastové spoje a šrouby jsou častým místem poruchy, proto je dobré zkontrolovat, zda jsou náhradní díly dostupné.</p>'
          '<h2>Péče o doplňky po sezoně</h2>'
          '<ul><li>Po každém výletu stojan a křeslo opláchněte čistou vodou, hlavně pokud jste lovili u slané nebo bahnité vody, a nechte je vysušit.</li>'
          '<li>Závity a kloubové spoje lehce naolejujte, aby se neseklo.</li>'
          '<li>Látky nikdy nesušte na topení ani na přímém slunci, pro delší životnost je skladujte v suchu a mimo přímé slunce.</li>'
          '<li>Před sezonou zkontrolujte šrouby, matice a pojistky.</li>'
          '<li>Stojan skladujte v pouzdru, aby se nepoškodily hlavice a závity.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš malý rod pod pro počet prutů, který chcete používat.</li>'
          '<li>Koupě křesla bez ověření nosnosti.</li>'
          '<li>Nedostatečné nohy na měkké půdě, kde se rám propadá.</li>'
          '<li>Opomenutí hmotnosti při pěším dojezdu k vodě.</li>'
          '<li>Nepočítání s rozměry v kufru auta.</li></ul>'
          '<h2>Jak sladit doplňky do jedné sestavy</h2>'
          '<p>Nejlepší komfort vznikne, když se vybavení dá snadno převážet a vejde se do jednoho auta nebo vozíku. Vybírejte stejné značky nebo série, protože nohy, šrouby a popruhy spolu často ladí. Složený rozměr pod, křesla, stolku a lůžka sečtěte a porovnejte s kufrem. Při pěším přístupu se vyplatí jednodušší sestava s lehkým křeslem a malým stolkem, při přijíždění autem až k vodě naopak širší a pohodlnější vybavení.</p>'
          '<h2>Co dalšího se hodí k rybářské výbavě</h2>'
          '<p>K rybaření patří také osvětlení, termoska, oblečení do vlhka a ochrana před sluncem. Tipy najdete v kategoriích <a href="/rybarske-obleceni/">rybářské oblečení</a>, <a href="/celovky-a-svitilny/">čelovky a svítilny</a> a <a href="/lahve-a-termosky/">lahve a termosky</a>. Pro širší přehled vstupte do hlavní kategorie <a href="/rybareni/">rybaření</a>. Pokud rybaříte i mimo vodu, podívejte se do oddílu <a href="/lov-a-priroda/">lov a příroda</a>.</p>',
    faq=[('K čemu slouží rod pod?', 'Rod pod je stojan, který drží pruty na břehu a umožňuje sledovat záběr bez držení prutu v ruce. Obsahuje opěrky a hlavice pro pruty a často i signalizátory záběru. Je určený pro kapraře a lov na delší zasedání.'),
         ('Kolik prutů má rod pod unést?', 'Nejčastěji dva až tři. Čtyři pruty vyžadují širší a robustnější pod. Zjistěte také, kolik prutů je na vaší vodě povoleno, protože rybářský řád se liší revír od revíru.'),
         ('Jaký materiál stojanu je nejlepší?', 'Nerez je odolná proti korozi a velmi pevná, hliník je lehký a hodí se pro dlouhé přesuny. Ocel vyžaduje dobrou povrchovou úpravu. Nejdůležitější je pevné spojení nohou a stabilita při zasekávání.'),
         ('Čím se liší kaprové křeslo od obyčejné židle?', 'Kaprové křeslo má robustní rám, polstrování, často opěradlo a nastavitelné nohy, které vyrovnají nerovný břeh. Obyčejná židle je lehčí a jednodušší, hodí se na kratší výlety a nesnese tolik zátěže.'),
         ('Na co se dívat u rybářského stolku?', 'Rozměr, výšku, nosnost a stabilitu na měkkém povrchu. Praktické jsou nastavitelné nohy a protiskluzová deska. Zkontrolujte také, zda se stolek vejde do vašeho bivaku a do kufru auta.'),
         ('Hodí se kaprová postel i na krátké výjezdy?', 'Obvykle ne, protože je objemnější a těžší než křeslo. Pro jednodenní lov stačí židle. Postel se vyplatí na vícedenní zasedání, kdy chcete kvalitně spát a chránit záda před chladem země.'),
         ('Jak o rybářské doplňky pečovat?', 'Po použití je opláchněte čistou vodou, osušte a uložte na suchém místě. Závity a klouby jednou za čas naolejujte. Látky chraňte před přímým sluncem a plísní. Před sezonou zkontrolujte šrouby a matice.'),
         ('Jak velký rod pod vybrat do auta?', 'Podívejte se na složený rozměr a hmotnost sady, včetně tašky. Menší pody jsou lehké, ale mají užší rozteč. Pokud vozíte více vybavení, zvolte kompaktní model, který se rozloží na kratší díly.'),
         ('Lze rod pod použít i na lodi?', 'Standardní pod na lodi nestojí stabilně. Pro loď existují speciální stojany, které se ukotvují k bokům nebo k podlaze. Při koupi sledujte typ ukotvení a rozměr lodi, aby držák seděl bezpečně.'),
         ('Potřebuji signalizátory záběru hned při nákupu?', 'Ne, mnoho podů se prodává bez nich a signalizátory se přikoupí podle potřeby. Začátečníkovi se hodí hotová sada, protože zjednoduší výběr a sladí závity i hlavice.')],
)

# ------------------------------------------------------------------ gainery
NEW['gainery'] = dict(long=True,
    title='Gainery: sacharidy a bílkoviny, složení, výběr',
    desc='Gainery a sacharido-proteinové směsi: jak číst složení, porovnat podíl bílkovin a sacharidů, vybrat velikost balení a příchuť. Přehled nabídek.',
    intro='<p>Gainer je práškový doplněk stravy, který kombinuje sacharidy, bílkoviny a někdy i tuky či další složky v jednom balení. Cílem je pohodlně doplnit energii lidem, kteří mají vysoký výdej nebo mají potíže s příjmem jídla. Obvykle se rozmíchá ve vodě nebo mléce a pije jako shake. Kategorie obsahuje klasické sacharido-proteinové směsi, hustší „mass gain“ s vyšším podílem sacharidů i jednodušší varianty ve formě smoothie nebo jednotlivých sáčků. Informace jsou obecné a nenahrazují radu lékaře nebo výživového poradce.</p>'
          '<p>Nejčastěji nabídku tvoří značky ' + B(('nutrend', 'Nutrend'), ('vitobest', 'Vitobest'), ('pvl', 'PVL'), ('myprotein', 'MyProtein'), ('extrifit', 'Extrifit'), ('nutriversum', 'Nutriversum'), ('muscleclinic', 'MuscleClinic'), ('weider', 'Weider')) +
          '. Související výběr je v kategoriích <a href="/proteiny/">proteiny</a>, <a href="/kreatin/">kreatin</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny a BCAA</a> a <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>',
    guide='<h2>Co gainer je a z čeho se skládá</h2>'
          '<p>Základem je sacharidová složka, nejčastěji maltodextrin, dextróza, rýžový škrob, ovesné vločky nebo směs více zdrojů. K ní se přidává bílkovinná část, obvykle syrovátka, kasein, sójový nebo hrachový protein. Někteří výrobci doplňují tuky (například MCT), vlákninu, vitaminy a minerály, případně kreatin nebo trávicí enzymy. Poměr složek se liší: některé směsi jsou hlavně sacharidové s nízkým podílem bílkovin, jiné vyváženější. Údaje proto vždy porovnávejte na porci i na 100 g.</p>'
          + T(['Typ produktu', 'Charakteristika', 'Hodí se'], [
              ['Klasický gainer', 'hodně sacharidů, střední podíl bílkovin', 'kdo hledá pohodlný zdroj energie v shaku'],
              ['Vyvážený sacharido-proteinový mix', 'víc bílkovin, méně jednoduchých cukrů', 'kdo preferuje vyšší podíl bílkovin'],
              ['Mass gain s tuky a vlákninou', 'hustší, větší energetická hodnota na porci', 'velmi aktivní lidé s vysokým výdejem'],
              ['Smoothie a vícesložkové směsi', 'chuť podobná ovoci, často s ovesnými vločkami', 'kdo preferuje jemnější chuť'],
              ['Sáčky a malé balení', 'jednotlivé porce na cesty', 'výlety, ochutnávka nové příchutě'],
              ['Veganské varianty', 'hrachový nebo rýžový protein', 'rostlinná strava, alergie na mléko']]) +
          '<h2>Pro koho je gainer určený</h2>'
          '<p>Gainer je pohodlný doplněk pro lidi, kteří jsou velmi aktivní, rychle spalují a těžko dosáhnou potřebné energie z klasického jídla. Hodí se také při špatné chuti k jídlu, při časové vytíženosti nebo při práci s vyšším výdejem. Nejde o doplněk pro každého: kdo nemá nedostatek energie, nepotřebuje přidávat další kalorie. Zdravotní stav, těhotenství, onemocnění ledvin nebo cukrovka jsou důvody, proč se předem poradit s lékařem.</p>'
          '<h2>Jak číst složení a nutriční údaje</h2>'
          '<ul><li><strong>Velikost porce:</strong> výrobci uvádějí porci v gramech a doporučené množství tekutiny. Porovnávejte stejnou velikost porce.</li>'
          '<li><strong>Energie:</strong> hodnota v kJ a kcal na porci a na 100 g ukazuje, jak hutný produkt je.</li>'
          '<li><strong>Bílkoviny a sacharidy:</strong> sledujte poměr a to, z jakých zdrojů pocházejí. Maltodextrin má rychlé vstřebávání, ovesné vločky pomalejší.</li>'
          '<li><strong>Cukry:</strong> část pochází z mléka nebo ovoce, část z přidaných sladidel.</li>'
          '<li><strong>Alergeny:</strong> mléko, sója, lepek a ořechy jsou běžné. Alergici čtou celou etiketu.</li>'
          '<li><strong>Sladidla a aromata:</strong> citlivý žaludek může reagovat na některé náhražky cukru.</li></ul>'
          '<h2>Jak gainer připravit</h2>'
          '<p>Většina směsí se míchá v šejkru s vodou nebo mlékem. Mléko směs zahustí a zvýší energetickou hodnotu, voda je lehčí a rychleji se pije. Pro hladký nápoj nejdřív nalijte tekutinu a až pak přidejte prášek. Pokud shake zahušťuje, zkuste víc tekutiny nebo mixér. Do mixéru můžete přidat banán, ovesné vločky nebo ořechové máslo, ale tím se změní energetická hodnota, proto na to myslete. Připravenou směs vypijte brzy, protože se nehodí k dlouhému skladování.</p>'
          '<h2>Kdy a kolik gainera pít</h2>'
          '<p>Výrobce na obalu uvádí doporučenou porci a počet porcí denně. Držte se jí a nezvyšujte dávku bez rady odborníka. Jedna porce často obsahuje velké množství energie, proto začněte menším množstvím a sledujte, jak vám vyhovuje. Mnoho lidí pije gainer mezi jídly nebo po tréninku, aby nezatěžovali žaludek těsně před výkonem. Gainer nemá nahrazovat běžné jídlo, ale doplnit ho. Pitný režim hlídejte i s dalšími nápoji, například <a href="/iontove-napoje/">iontovými nápoji</a>.</p>'
          '<h2>Velikost balení a porce</h2>'
          '<p>V nabídce najdete menší balení stovek gramů, kilogramová a několikakilogramová balení. Menší balení se hodí na vyzkoušení chuti a snášenlivosti, větší vychází na porci výhodněji, ale vyžaduje, aby produkt vydržel spotřebovat do data minimální trvanlivosti. Zkontrolujte, kolik porcí balení obsahuje a jak velká je porce, ne jen hmotnost. Dvě směsi se stejnou hmotností mohou obsahovat velmi odlišný počet porcí.</p>'
          '<h2>Příchutě a rozpustnost</h2>'
          '<p>Vanilka, čokoláda, jahoda a banán jsou nejčastější. Sladká chuť gaineru bývá výraznější než u čistého proteinu, protože obsahuje víc sacharidů. Pokud vám sladké nesedí, zkuste neutrální příchuť nebo menší porci. Rozpustnost se liší: směsi s ovesnými vločkami nebo vlákninou mohou být hustší a hůř se míchají. Při koupi novou příchuť raději zkuste v malém balení.</p>'
          '<h2>Gainer, protein a jídlo</h2>'
          '<p>Gainer nenahrazuje běžnou stravu, ani čistý protein. Kdo potřebuje hlavně bílkoviny a méně sacharidů, zvolí <a href="/proteiny/">proteinový prášek</a>. Kdo potřebuje rychlou energii při vytrvalostním výkonu, najde vhodnější zdroje v <a href="/energeticke-gely-a-tycinky/">energetických gelech a tyčinkách</a>. Gainer je volba pro ty, kdo potřebují obě složky najednou v tekuté a pohodlné formě. Pokud preferujete lehkou svačinu, podívejte se i na <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>.</p>'
          '<h2>Sacharidy v gaineru: jaké druhy existují</h2>'
          '<p>Typ sacharidu ovlivňuje, jak se směs chová v žaludku. Maltodextrin a dextróza se rychle rozpouštějí a vstřebávají, proto jsou běžné v klasických směsích. Rýžový škrob nebo ovesné vločky se tráví pomaleji a směs je sytější. Vlákninu některé směsi přidávají kvůli hustotě a pocitu sytosti, citlivému trávení ale může způsobit nadýmání. Pokud se vám po mléčném shaku zvedá žaludek, zkuste směs s menším podílem laktózy.</p>'
          '<h2>Bílkoviny v gaineru: syrovátka, kasein a rostlinné zdroje</h2>'
          '<p>Syrovátková bílkovina je mléčná a dobře rozpustná, kasein se rozpouští hustěji a tvoří gel. Mnoho gainerů obsahuje jejich směs. Rostlinné směsi používají hrachový, rýžový nebo sójový protein a často je kombinují, aby se doplnily jednotlivé aminokyseliny. V seznamu složek je zdroj bílkovin vždy uveden, a to podle pořadí množství. Podrobnější přehled najdete v textu o <a href="/proteiny/">proteinech</a> a o <a href="/aminokyseliny-bcaa/">aminokyselinách</a>.</p>'
          '<h2>Domácí alternativa a rozdíl oproti jídlu</h2>'
          '<p>Podobný nápoj lze namíchat doma z mléka, ovesných vloček, banánu a ořechového másla. Domácí varianta má známé složení a jemnější chuť, vyžaduje ale mixér a čas. Gainer v prášku vyhrává tím, že se dá připravit kdekoli v šejkru a v tašce zabere málo místa. Ani jedno řešení nenahrazuje pestrou stravu s dostatkem zeleniny, ovoce a kvalitních zdrojů bílkovin, spíše ji doplňují.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<ul><li>Prášek skladujte v suchu, v dobře uzavřeném obalu a mimo přímé slunce.</li>'
          '<li>Po otevření pevně uzavřete víko, vlhkost způsobuje hrudky.</li>'
          '<li>Odměrku nenechávejte v prášku, mohou do něj vnikat bakterie.</li>'
          '<li>Dbejte na datum minimální trvanlivosti na obalu.</li>'
          '<li>Připravený shake nenechávejte v teple, vypijte ho hned nebo ho uložte do chladu.</li></ul>'
          '<h2>Časté chyby při výběru a užívání</h2>'
          '<ul><li>Výběr jen podle ceny za kilogram bez kontroly podílu bílkovin a porce.</li>'
          '<li>Nahrazování plnohodnotných jídel gainerem.</li>'
          '<li>Příliš velká první porce, která zatíží trávení.</li>'
          '<li>Ignorování alergenů a pokynů na obalu.</li>'
          '<li>Kupování velkého balení bez vyzkoušení chuti.</li>'
          '<li>Očekávání zázraku bez tréninku a pestrého jídelníčku.</li></ul>'
          '<h2>Údržba a čistota šejkru</h2>'
          '<p>Šejkr a odměrku po použití opláchněte teplou vodou, jinak mléčná směs zakysá a začne zapáchat. Víčko i těsnění pravidelně rozeberte a vyčistěte, aby se pod nimi neusazovaly zbytky. Spoustu práce ušetří šejkr s kovovou kuličkou nebo sítkem, které rozbijí hrudky. Lahve vhodné k přípravě shaků najdete v kategorii <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení má Nutrend s několika variantami Mass Gain, následují Vitobest (například Monster Gainer), PVL, MyProtein a Extrifit. Dále se objevují Nutriversum, MuscleClinic, Weider, Kevin Levrone, Rule ONE a Megabol. Najdete tu i produkty Decathlon a menší zahraniční značky jako OstroVit nebo Reflex Nutrition. Značky se liší chutí, složením a velikostí balení, takže srovnávejte konkrétní etikety.</p>'
          '<h2>Další doplňky k tréninku</h2>'
          '<p>Další produkty pro aktivní lidi najdete v kategoriích <a href="/predtreninkove-boostery/">předtréninkové boostery</a>, <a href="/spalovace-tuku/">spalovače tuku</a>, <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a> a <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>. Pro základní vybavení k cvičení se podívejte na <a href="/fitness/">fitness</a> a <a href="/lahve-a-termosky/">lahve a termosky</a>, které se hodí k přípravě shaků. Doplňky stravy nejsou náhradou pestré stravy a u zdravotních potíží se vždy poraďte s lékařem.</p>',
    faq=[('Co je gainer a k čemu slouží?', 'Gainer je prášek, který obsahuje sacharidy a bílkoviny a slouží jako pohodlný doplněk energie. Hodí se lidem s vysokým výdejem nebo s malou chutí k jídlu. Neslouží jako náhrada běžné stravy.'),
         ('Čím se gainer liší od proteinu?', 'Protein obsahuje hlavně bílkoviny a málo sacharidů, gainer přidává větší podíl sacharidů a má vyšší energetickou hodnotu. Volba závisí na tom, zda potřebujete hlavně bílkoviny, nebo celkovou energii.'),
         ('Jak se gainer připravuje?', 'Většinou se míchá v šejkru nebo mixéru s vodou či mlékem. Nejdřív nalijte tekutinu, pak přidejte prášek. Mléko směs zahustí a zvýší energii, voda je lehčí. Dodržujte porci na obalu.'),
         ('Kdy gainer pít?', 'Mnoho lidí ho pije mezi jídly nebo po tréninku. Těsně před výkonem může zatížit žaludek. Doporučené množství a dobu užití najdete na obalu, případně se poraďte s výživovým poradcem.'),
         ('Je gainer vhodný pro každého?', 'Ne. Kdo nepotřebuje navíc energii, gainer nepotřebuje. Při onemocnění ledvin, cukrovce, těhotenství nebo jiných zdravotních omezeních se předem poraďte s lékařem. Informace v textu jsou obecné.'),
         ('Jak číst údaje o gaineru na obalu?', 'Sledujte velikost porce, energii, podíl bílkovin a sacharidů, cukrů a alergeny. Porovnávejte hodnoty na porci i na 100 g, protože porce se mezi výrobci liší.'),
         ('Jaké balení gaineru zvolit?', 'Pro první pokus menší balení, abyste ověřili chuť a snášenlivost. Pokud vám vyhovuje, přejděte na větší, které vychází výhodněji. Kontrolujte datum minimální trvanlivosti.'),
         ('Existují veganské gainery?', 'Ano, používají hrachový, sójový nebo rýžový protein a rostlinné sacharidy, například ovesné vločky. Při alergiích čtěte celé složení, protože sdílená výroba je běžná.'),
         ('Jak gainer skladovat?', 'V suchu, v dobře zavřeném obalu a mimo přímé slunce. Odměrku nenechávejte v prášku a po otevření spotřebujte do doby uvedené výrobcem. Hotový shake vypijte hned.'),
         ('Jak poznat, že je gainer kvalitně namíchaný?', 'Porovnejte pořadí složek na etiketě, uvedený zdroj bílkovin a údaj o porci. Čím jasněji výrobce popisuje složení a alergeny, tím snáze produkt posoudíte. Na marketingové slogany na přední straně obalu nespoléhejte.'),
         ('Pomůže gainer sám bez tréninku?', 'Gainer dodá energii a bílkoviny, ale výsledek závisí na celkovém jídelníčku, pohybu a spánku. Doplněk stravy nenahradí pestrou stravu a při zdravotních otázkách je potřeba poradit se s lékařem nebo výživovým poradcem.'),
         ('Může gainer způsobit zažívací potíže?', 'U citlivých lidí ano, zvlášť při větší porci nebo při intoleranci laktózy. Začněte menší dávkou, vyzkoušejte variantu bez laktózy a při potížích užívání přerušte a poraďte se s lékařem.')],
)
