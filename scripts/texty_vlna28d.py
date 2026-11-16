"""sporteka.cz — wave 28d (16. 11. 2026): long texts for nafukovaci-matrace, samonafukovaci-karimatky, kempingove-zidle, kempingove-stoly.
General true facts only, no prices, no product counts. R-value explained via ASTM F3340. Brands linked only where they exist in
src/texts/znacky.json (husky, regatta); other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ nafukovaci-matrace
NEW['nafukovaci-matrace'] = dict(long=True,
    title='Nafukovací matrace a lehátka: do stanu, na chatu i k vodě',
    desc='Nafukovací matrace pro hosty i do stanu, nafukovací lehátka k bazénu a izolované matrace na túry. Jak vybrat rozměr, pumpu a ventil.',
    intro='<p>Nafukovací matrace řeší dvě úplně odlišné situace. Jednou jde o přistýlku pro návštěvu nebo o pohodlné spaní v rodinném stanu, podruhé o lehátko, na kterém se v létě houpete na hladině bazénu. Do kategorie navíc patří i lehké izolované matrace pro turisty, které se sbalí do velikosti láhve. Každý z těchto typů se vybírá podle jiných parametrů, a proto se vyplatí nejdřív vědět, k čemu matraci chcete.</p>'
          '<p>Na Sportece najdete nabídky českých obchodů k jednotlivým výrobkům na jednom místě; koupi pak uzavřete přímo v e-shopu. V nabídce jsou velkoobjemové matrace Intex a Bestway, kempingové postele Coleman, matrace High Peak a izolované modely Sea to Summit. Nadřazenou kategorií jsou <a href="/karimatky-a-matrace/">karimatky a matrace</a>, k vodě se hodí i <a href="/nafukovaci-hracky/">nafukovací hračky</a>.</p>',
    guide='<h2>Tři druhy nafukovacích matrací</h2>'
          '<p>Pod jedním názvem se v obchodech skrývají tři skupiny výrobků, které mají společný jen vzduch uvnitř. Velké matrace pro hosty a do stanu jsou vysoké, široké a těžké, protože jsou z vinylu nebo zesíleného PVC. Lehátka do vody jsou tenká, lehká a stavěná na hladinu, ne na spaní. Turistické matrace jsou úzké, z lehké tkaniny s vrstvou TPU a často mají uvnitř izolaci, aby od země netáhla zima.</p>'
          + T(['Typ', 'K čemu slouží', 'Čím se liší'], [
              ['Matrace pro hosty a na chatu', 'přistýlka doma, spaní na chatě', 'výška až kolem půl metru, často vestavěná elektrická pumpa'],
              ['Kempingová matrace do stanu', 'rodinné stany, karavan, kemp', 'nižší profil, odolnější spodní strana, ruční nebo nožní pumpa'],
              ['Nafukovací lehátko k vodě', 'bazén, klidná voda u břehu', 'tenké komory, polštářek, někdy průhledné okénko nebo síťka'],
              ['Izolovaná turistická matrace', 'stan na túře, bivak', 'nízká hmotnost, malý objem, udávaná R-hodnota']]) +
          '<h2>Matrace pro hosty a do stanu</h2>'
          '<p>U matrace, na které má někdo spát celou noc, rozhoduje vnitřní konstrukce. Levné modely mají jednoduché podélné komory a při pohybu se vlní. Lepší matrace spojují horní a spodní stěnu desítkami svislých přepážek nebo vláken, takže je povrch rovnější a matrace se tolik nehoupe. Výrobci tuto technologii nazývají různě, třeba Fiber-Tech u Intexu nebo Tritech u Bestwaye, princip je ale podobný.</p>'
          '<p>Vysoké matrace se lépe opouštějí, což ocení starší hosté, a sedí se na nich skoro jako na posteli. Do stanu ale vysoký model nepatří: zabírá místo, kolem něj se špatně chodí a uvnitř je víc vzduchu, který v noci chladne. Pro stan proto volte matraci nižší a s pevnější spodní stranou, která snese drobné kamínky pod podlahou stanu.</p>'
          '<p>Rozměry se u velkých matrací často uvádějí podle amerických postelí: twin pro jednoho, full nebo queen pro dva. Vždy se ale dívejte na skutečné centimetry v popisu a porovnejte je s podlahou stanu nebo s místem v pokoji. Matrace pro dva s jedinou komorou přenáší každý pohyb na druhého spáče; dvě samostatné jednolůžkové matrace vedle sebe tento problém nemají.</p>'
          '<h2>Pumpa a ventil</h2>'
          '<p>Vestavěná elektrická pumpa na 230 V je nejpohodlnější řešení pro byt a chatu: matrace se nafoukne během pár minut a stejnou pumpou se často i vyfoukne. Ve stanu bez elektřiny ale nepomůže, tam se hodí nožní pumpa, ruční pístová pumpa nebo malá pumpa na baterie či do zásuvky v autě. Před koupí zkontrolujte, zda je pumpa v balení, nebo se kupuje zvlášť, a jestli její nástavce pasují do ventilu.</p>'
          '<p>Ventily se liší rychlostí i spolehlivostí. Dvoudílný ventil se šroubovací zátkou umožňuje rychle vypustit vzduch a zároveň brání úniku při nafukování. U lehátek se setkáte s jednoduchými zátkami, které se zatlačí do hrdla. Ať je ventil jakýkoli, nechte ho po vyfouknutí otevřený a matraci srolujte směrem k němu, vzduch pak odejde snáz.</p>'
          '<h2>Proč matrace v noci „splaskne“, i když nepouští</h2>'
          '<p>Nová matrace z vinylu se při prvních nocích roztahuje a materiál povolí, takže ji bude potřeba dofouknout. Výrobci proto doporučují matraci před prvním použitím nafouknout a nechat ji tak několik hodin. Druhým důvodem je teplota. Vzduch, kterým matraci večer nafouknete, v chladné noci zmenší objem a matrace působí měkčí. To není závada; ráno po ohřátí se tvar zase vrátí. Teprve když matrace měkne i při stálé teplotě, hledejte díru, nejlépe s mýdlovou vodou, ve které unikající vzduch udělá bublinky.</p>'
          '<p>Většina velkých matrací má v balení záplaty. Lepí se na čistý a suchý povrch a lepidlo musí před dalším nafouknutím zatuhnout. Pro opravy na cestách se vyplatí mít v autě malou opravnou sadu, protože záplata, která leží doma v šuplíku, vám na kempu nepomůže.</p>'
          '<h2>Zima od země: proč na velké matraci mrznete</h2>'
          '<p>Velká matrace bez izolace je v chladné noci vlastně studený polštář vzduchu. Vzduch uvnitř cirkuluje a odvádí teplo od těla k zemi. V létě to nevadí, na jaře a na podzim už ano. Pomůže položit na matraci deku nebo tenkou karimatku a teprve na ni <a href="/spaci-pytle/">spací pytel</a>. Na túry, kde se spí v chladu, patří spíš izolovaná matrace s uvedenou R-hodnotou.</p>'
          '<h2>Izolované matrace a R-hodnota</h2>'
          '<p>Turistické matrace Sea to Summit, High Peak a dalších výrobců mají uvnitř syntetické vlákno nebo reflexní fólii, které zpomalují únik tepla. Míru izolace udává R-hodnota, tedy tepelný odpor. Čím vyšší číslo, tím méně tepla matrace pustí k zemi. Od roku 2020 velcí výrobci měří R-hodnotu jednotnou metodou podle normy ASTM F3340, takže čísla různých značek se dají porovnat. U starších nebo neznačkových výrobků může být hodnota změřená jinak, proto jí věřte méně.</p>'
          '<p>Orientačně platí, že matrace s R-hodnotou do 2 se hodí na teplé letní noci, kolem 2 až 4 na jaro, léto a podzim, a pro spaní v mrazu nebo na sněhu se volí hodnoty nad 5,5. R-hodnoty dvou podložek se sčítají, takže tenká pěnová karimatka pod nafukovací matrací zlepší izolaci a zároveň chrání matraci před propíchnutím.</p>'
          '<h2>Nafukovací lehátko k vodě</h2>'
          '<p>Lehátka se liší tvarem a pohodlím: klasické pruhované s polštářkem, křesla s opěradlem a držákem na nápoj, kruhy s průhledným dnem nebo síťová lehátka, při kterých je část těla ve vodě a v horku příjemně chladí. Pro pobyt na hladině je důležitý také materiál. Silnější PVC lépe odolává ostrým hranám u bazénu, tenké lehátko se rychleji prodře o beton.</p>'
          '<p>Nafukovací lehátko není záchranný prostředek a nikoho neudrží nad vodou, když z něj sklouzne. Na volné vodě se s ním nevzdalujte od břehu, protože vítr foukající od pevniny dokáže lehátko odnést rychleji, než se zdá. Děti na lehátku nikdy nenechávejte bez dozoru a neplavce k němu přidejte <a href="/plovaci-vesty/">plovací vestu</a>. Lehátko po koupání opláchněte od chloru nebo soli, nechte uschnout ve stínu a teprve pak ho sbalte.</p>'
          '<h2>Kempingové postele a matrace s rámem</h2>'
          '<p>Na pomezí matrace a nábytku stojí kempingová lehátka a postele se skládacím rámem. Některé modely spojují rám přímo s nafukovací matrací, jiné jsou jen napnutá látka na kovových nohách, na kterou se karimatka položí. Lehátko zvedne spáče nad studenou a vlhkou zem, hodí se do velkých stanů, na chatu a pro lidi, kterým se špatně vstává z podlahy. Počítejte ale s vyšší hmotností a tím, že pod napnutou látkou proudí vzduch, takže v chladu je potřeba izolace i zespodu.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Vysoká matrace pro hosty koupená do malého stanu.</li>'
          '<li>Spoléhání na vestavěnou pumpu tam, kde není zásuvka.</li>'
          '<li>Reklamace „díry“, která je ve skutečnosti jen ochladlý vzduch nebo roztažený nový materiál.</li>'
          '<li>Spaní na neizolované matraci v chladné noci bez deky nebo karimatky.</li>'
          '<li>Porovnávání R-hodnot, z nichž jedna není měřená podle ASTM F3340.</li>'
          '<li>Skladování vlhké matrace, která pak zapáchá a plesniví.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Matraci před uložením otřete, vysušte a srolujte volně, bez ostrých přehybů. Skladujte ji v suchu, mimo přímé slunce a mimo dosah myší, které vinyl rády okusují. Zimu v nevytápěné garáži snáší PVC hůř, protože v mrazu křehne; pokud můžete, uložte ji doma. Lehátka nepouštějte na rozpálenou dlažbu bez dozoru, horko zvětšuje tlak uvnitř.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Karta produktu ukáže nabídky několika obchodů vedle sebe, a když najdete tu správnou, objednávka proběhne v daném e-shopu. U matrací hledejte nejdřív rozměr a výšku, potom typ pumpy a nakonec vzhled. Do stanu pro více lidí se podívejte i na <a href="/rodinne-stany/">rodinné stany</a>, k pohodlnému spaní venku na <a href="/samonafukovaci-karimatky/">samonafukovací karimatky</a> a pro odpočinek u stanu na <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</p>',
    faq=[
        ('Proč je nafukovací matrace ráno měkčí?', 'Nejčastěji kvůli teplotě. Vzduch v matraci se v chladné noci smrští a matrace změkne, ráno se opět zpevní. Nová matrace se navíc při prvních použitích roztahuje, proto ji výrobci doporučují nejprve nafouknout na několik hodin a pak dofouknout.'),
        ('Jak najdu díru v matraci?', 'Matraci nafoukněte a potírejte podezřelá místa mýdlovou vodou. Kde vzduch uniká, vytvoří se bublinky. Místo osušte, očistěte a přelepte záplatou podle návodu výrobce.'),
        ('Je nafukovací matrace vhodná do stanu?', 'Ano, ale volte nižší model s odolnou spodní stranou. Velký objem vzduchu v chladné noci odvádí teplo, proto pod spací pytel přidejte deku nebo karimatku. Na túry jsou lepší lehké izolované matrace s udanou R-hodnotou.'),
        ('Co znamená R-hodnota?', 'Tepelný odpor podložky: čím vyšší, tím lépe izoluje od studené země. Velcí výrobci ji od roku 2020 měří podle normy ASTM F3340, takže se dají porovnávat. R-hodnoty dvou podložek položených na sobě se sčítají.'),
        ('Jakou pumpu potřebuju?', 'Doma a na chatě je nejpohodlnější vestavěná elektrická pumpa. Ve stanu bez elektřiny použijte nožní nebo ruční pumpu, případně malou pumpu na baterie. Zkontrolujte, zda nástavec pasuje do ventilu matrace.'),
        ('Je nafukovací lehátko bezpečné pro děti?', 'Lehátko není záchranný prostředek. Děti na něm nechávejte jen pod dohledem, neplavce vybavte plovací vestou a na volné vodě se nevzdalujte od břehu, protože vítr může lehátko odnést.'),
        ('Jak matraci skladovat přes zimu?', 'Čistou a suchou ji volně srolujte a uložte v suchu a teple, mimo slunce a hlodavce. V mrazu PVC křehne, proto je lepší místo doma než v nevytápěné garáži.'),
    ])

# ------------------------------------------------------------------ samonafukovaci-karimatky
NEW['samonafukovaci-karimatky'] = dict(long=True,
    title='Samonafukovací karimatky: R-hodnota, tloušťka, ventily',
    desc='Samonafukovací i nafukovací karimatky do stanu a na túry. Jak vybrat podle R-hodnoty, tloušťky, hmotnosti a ventilu a jak karimatku skladovat.',
    intro='<p>Samonafukovací karimatka spojuje pěnu a vzduch. Uvnitř obalu je pružná pěna s otevřenými buňkami, a když otevřete ventil, pěna se roztáhne a nasaje vzduch sama. Stačí pak pár výdechů na doladění tuhosti. Oproti pěnové karimatce je pohodlnější a lépe izoluje, oproti čistě nafukovací karimatce je odolnější a nespí se na ní jako na balonku. Vedle samonafukovacích modelů tu najdete i lehké nafukovací karimatky, které se sbalí do menšího objemu.</p>'
          '<p>Sporteka zobrazuje nabídky českých e-shopů vedle sebe a vy pak nakoupíte v obchodě, který vám vyhovuje. Zastoupené jsou značky ' + B(('husky', 'Husky'), ('regatta', 'Regatta')) + ', Yate, Easy Camp, Nomad, Sulov, High Peak nebo Sea to Summit. Celou skupinu najdete v kategorii <a href="/karimatky-a-matrace/">karimatky a matrace</a>, k ní patří <a href="/spaci-pytle/">spací pytle</a> a <a href="/turisticke-stany/">turistické stany</a>.</p>',
    guide='<h2>Jak samonafukovací karimatka funguje</h2>'
          '<p>Pěna uvnitř karimatky je stlačená, dokud je ventil zavřený a karimatka srolovaná. Po rozbalení a otevření ventilu se buňky pěny rozpínají a nasávají vzduch. Za pár minut je karimatka z velké části plná, při prvním použití nebo po dlouhém skladování v rolce to ale může trvat déle. Pak se ventil zavře, případně se karimatka dofoukne několika výdechy nebo pumpovacím vakem, a je hotovo.</p>'
          '<p>Pěna zároveň plní roli izolace. Brání tomu, aby vzduch uvnitř volně proudil a odváděl teplo k zemi, a proto samonafukovací karimatka izoluje lépe než stejně tlustá nafukovací komora bez výplně. Má ale i nevýhodu: pěna něco váží a ve sbaleném stavu zabírá místo.</p>'
          '<h2>Samonafukovací, nebo nafukovací karimatka?</h2>'
          + T(['Vlastnost', 'Samonafukovací karimatka', 'Nafukovací karimatka'], [
              ['Plnění', 'pěna nasaje vzduch, doladí se pár výdechy', 'nafouknutí ústy, pumpovacím vakem nebo pumpičkou'],
              ['Hmotnost a objem', 'těžší a objemnější', 'lehčí, sbalí se do menšího vaku'],
              ['Tloušťka', 'obvykle 2,5 až 10 cm', 'často 5 až 10 cm i víc'],
              ['Při propíchnutí', 'pěna dál trochu izoluje a tlumí', 'bez vzduchu spíte prakticky na zemi'],
              ['Typické použití', 'kemp, stan u auta, turistika s menšími nároky na váhu', 'dálkové túry, cyklovýlety, bivak']]) +
          '<p>Kdo jezdí stanovat autem nebo nese batoh jen na víkend, obvykle sáhne po samonafukovací karimatce. Kdo počítá každý gram na vícedenní túře, zvolí nafukovací karimatku s izolační výplní. Pro děti a do rodinného stanu se hodí širší samonafukovací modely, protože snesou hrubší zacházení.</p>'
          '<h2>R-hodnota podle normy ASTM F3340</h2>'
          '<p>Nejdůležitějším údajem pro spaní v chladu je R-hodnota, tedy tepelný odpor karimatky. Velcí výrobci outdoorového vybavení se v roce 2020 shodli na jednotné zkušební metodě podle normy ASTM F3340, a od té doby lze R-hodnoty různých značek srovnávat. Pokud výrobce normu neuvádí, berte číslo jako orientační.</p>'
          '<ul><li><strong>R do 2:</strong> letní noci, chaty, spaní pod střechou.</li>'
          '<li><strong>R 2 až 4:</strong> jaro, léto a podzim v běžném terénu.</li>'
          '<li><strong>R 4 až 5,5:</strong> chladné noci, hory, začátek zimy.</li>'
          '<li><strong>R nad 5,5:</strong> mráz a spaní na sněhu.</li></ul>'
          '<p>Hodnoty se sčítají, takže tenká pěnová podložka pod samonafukovací karimatkou zvýší izolaci a navíc chrání spodní stranu. Lidé, kterým je v noci rychle zima, by měli volit vyšší hodnotu, než naznačuje roční období. Nezapomeňte, že na pohodlí má vliv i <a href="/spaci-pytle/">spacák</a> a tloušťka oblečení, karimatka je jen jedna část systému.</p>'
          '<h2>Tloušťka, šířka a tvar</h2>'
          '<p>Tenké samonafukovací karimatky kolem 2,5 až 3 cm jsou lehké a malé, na tvrdé zemi ale ucítíte kořen i kámen a boční spáč na nich narazí kyčlí do země. Karimatky kolem 5 cm jsou kompromisem pro většinu turistů. Tloušťky 7,5 až 10 cm už se blíží matraci a dávají smysl hlavně při kempování u auta, kde nevadí hmotnost.</p>'
          '<p>Běžná šířka je kolem 50 až 55 cm, širší modely mají 65 cm a víc a hodí se pro neklidné spáče. Mumiový tvar se zúženým koncem ušetří gramy a vejde se lépe do úzkého stanu, obdélníková karimatka nabízí víc místa pro nohy. Některé modely, například dvojité karimatky Easy Camp nebo Yate, mají po stranách patentky nebo spony, kterými se dají spojit dvě karimatky k sobě.</p>'
          '<h2>Ventily a nafukování</h2>'
          '<p>Klasický šroubovací ventil je jednoduchý a spolehlivý. Novější modely mají ploché ventily se dvěma režimy: jedním se vzduch dovnitř pouští a ven neuniká, druhým se vypustí naráz. Sea to Summit a další výrobci používají ventily, ve kterých se při nafukování nedá vzduch nechtěně ztratit. Na nafukovací karimatky se vyplatí pumpovací vak, protože vlhkost z dechu se uvnitř komory sráží a v mrazu může vytvořit led. Některé vaky zároveň slouží jako nepromokavý obal.</p>'
          '<h2>Hmotnost a sbalený rozměr</h2>'
          '<p>Rozdíl mezi modely je velký. Lehké samonafukovací karimatky na túry váží kolem půl kilogramu až kilogramu, tlusté kempingové i přes dva kilogramy. Nafukovací karimatky s izolací se umí dostat pod půl kilogramu a sbalí se do velikosti litrové láhve. Údaje v popisu uvádějte vždy do poměru s R-hodnotou a tloušťkou: nejlehčí karimatka nemá smysl, když na ní budete v noci mrznout.</p>'
          '<h2>Materiál a odolnost</h2>'
          '<p>Horní strana bývá z polyesteru nebo nylonu s jemnou strukturou, aby po ní nesjížděl spací pytel. Spodní strana je obvykle silnější a odolnější vůči oděru. Hustota tkaniny se udává v denierech, například 30D nebo 75D, a vyšší číslo znamená silnější vlákno. Lehká tkanina se sbalí do menšího objemu, ale snáz se propíchne. Opravná sada se záplatami bývá součástí balení a na cestu ji vždy přibalte.</p>'
          '<h2>Skladování: proč karimatku nenechávat srolovanou</h2>'
          '<p>Většina výrobců doporučuje skladovat samonafukovací karimatku doma rozbalenou a s otevřeným ventilem, například za skříní nebo pod postelí. Pěna, která je měsíce stlačená v rolce, ztrácí pružnost a karimatka se pak sama nafukuje pomaleji a hůř. Otevřený ventil zároveň dovolí vyschnout vlhkosti, která se dovnitř dostala z dechu.</p>'
          '<p>Po výletě karimatku otřete vlhkým hadříkem a nechte uschnout. Při balení ji nejprve srolujte s otevřeným ventilem od opačného konce, zavřete ventil a pak ji srolujte podruhé, už pevněji. Takto se vejde do obalu, který se při prvním pokusu zdá vždycky malý.</p>'
          '<h2>Pro boční spáče a pro děti</h2>'
          '<p>Kdo spí na boku, opírá se o karimatku hlavně ramenem a kyčlí, tedy malou plochou. Tenká karimatka se pod nimi promáčkne až k zemi, proto by boční spáč měl volit aspoň kolem 5 cm a raději širší model. Spáči na zádech vystačí s tenčí karimatkou, protože se jejich váha rozloží do větší plochy.</p>'
          '<p>Pro děti se prodávají kratší karimatky, které ušetří místo ve stanu i v batohu. Malé dítě ale ztrácí teplo rychleji než dospělý, takže R-hodnotu nepodceňujte ani u dětského modelu. Samonafukovací karimatka je pro děti obvykle vhodnější než nafukovací, protože ji nepropíchne pastelka ani kamínek ve stanu a při úniku vzduchu dál trochu izoluje.</p>'
          '<h2>Polštář a podložka pod karimatku</h2>'
          '<p>K pohodlnému spaní patří i polštář. Nafukovací kempingové polštáře se sbalí do velikosti pěsti, některé karimatky mají polštář přímo vestavěný v horní části. Pod karimatku je dobré dát tenkou pěnovou podložku nebo podlážku stanu: chrání spodní tkaninu před jehličím a kamínky a přidá trochu izolace navíc.</p>'
          '<h2>Zima a spaní na sněhu</h2>'
          '<p>V zimě ztrácí tělo teplo do země mnohem rychleji než do vzduchu, a to i v nejlepším péřovém spacáku. Na sněhu se proto spí na kombinaci dvou podložek: dole pěnová karimatka, která se nemůže prasknout, nahoře samonafukovací nebo izolovaná nafukovací. Jejich R-hodnoty se sčítají a když jedna selže, druhá vás aspoň trochu ochrání. Ventil v mrazu otevírejte opatrně a karimatku ráno nefoukejte dechem, aby uvnitř nevznikl led.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Volba podle tloušťky bez ohledu na R-hodnotu.</li>'
          '<li>Dlouhodobé skladování v pevné rolce se zavřeným ventilem.</li>'
          '<li>Nafukování nafukovací karimatky v mrazu ústy místo pumpovacím vakem.</li>'
          '<li>Úzká karimatka pro spáče, který se v noci často otáčí.</li>'
          '<li>Výlet bez opravné sady.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě karimatky vidíte, který obchod ji má skladem a za jakých podmínek, a objednávku pak dokončíte u něj. Rozhodujte se nejprve podle R-hodnoty a období, ve kterém chcete spát venku, pak podle tloušťky a hmotnosti a až nakonec podle barvy. Pro kempování u auta se podívejte i na <a href="/nafukovaci-matrace/">nafukovací matrace</a> a pro chladné noci na <a href="/vlozky-do-spacaku/">vložky do spacáku</a>.</p>',
    faq=[
        ('Jak se samonafukovací karimatka nafoukne?', 'Rozbalte ji a otevřete ventil. Pěna uvnitř se roztáhne a nasaje vzduch, což trvá několik minut, při prvním použití i déle. Potom ji podle potřeby dofoukněte několika výdechy nebo pumpovacím vakem a ventil zavřete.'),
        ('Jaká R-hodnota stačí na stanování v létě?', 'Na teplé letní noci obvykle stačí R-hodnota kolem 2. Pro jaro a podzim volte 2 až 4, na mráz a sníh nad 5. Pokud je vám v noci snadno zima, vezměte vyšší hodnotu.'),
        ('Je lepší samonafukovací, nebo nafukovací karimatka?', 'Samonafukovací je odolnější a při propíchnutí ještě trochu izoluje, ale je těžší a objemnější. Nafukovací karimatka je lehčí a menší, takže se hodí na dlouhé túry. Volba záleží hlavně na tom, jak daleko vybavení ponesete.'),
        ('Jak skladovat samonafukovací karimatku?', 'Doma rozbalenou a s otevřeným ventilem. Pěna stlačená měsíce v rolce ztrácí pružnost a karimatka se pak hůř sama nafukuje. Otevřený ventil umožní vyschnout vlhkosti uvnitř.'),
        ('Proč karimatku nefoukat ústy v mrazu?', 'Dech obsahuje vlhkost, která se uvnitř komory sráží a v mrazu může zmrznout. Pumpovací vak nebo ruční pumpička tento problém nemají a vlhkost uvnitř zůstává menší.'),
        ('Co znamená ASTM F3340?', 'Je to norma, podle které velcí výrobci od roku 2020 měří R-hodnotu karimatek jednotným způsobem. Díky ní lze porovnávat čísla různých značek. U hodnot bez uvedené normy buďte opatrnější.'),
        ('Dají se dvě karimatky spojit?', 'Některé modely mají po stranách patentky, spony nebo pásky, kterými se dají spojit k sobě. Prodávají se také dvojité samonafukovací karimatky pro dva spáče, které se hodí do rodinného stanu.'),
    ])

# ------------------------------------------------------------------ kempingove-zidle
NEW['kempingove-zidle'] = dict(long=True,
    title='Kempingová židle a křeslo: skládací, lehké i odolné',
    desc='Kempingové židle, skládací křesla, režisérské židle i lehká křesílka do batohu. Jak vybrat podle nosnosti, hmotnosti a sbaleného rozměru.',
    intro='<p>Kempingová židle je jedna z věcí, které na první výpravě chybějí nejvíc. Sezení na pařezu nebo na chladivé zemi přestane bavit po pár minutách, zatímco v pohodlném skládacím křesle vydržíte u ohně celý večer. Nabídka sahá od jednoduchých skládacích stoliček přes klasická kempingová křesla s područkami až po polohovací lehátka a ultralehká křesílka, která se sbalí do batohu. Rozhoduje hlavně nosnost, hmotnost a rozměr po složení, teprve potom barva a doplňky. Kdo jezdí autem, může si dovolit pohodlné polstrované křeslo, kdo nese všechno na zádech, ocení každých sto gramů dole.</p>'
          '<p>Na Sportece vidíte, co ke konkrétní židli nabízejí české e-shopy, a nákup uzavřete u toho, jehož nabídka vám vyhovuje. V kategorii najdete židle Outwell, Coleman, King Camp, Nils Camp, Eurotrail, High Peak nebo ' + B(('husky', 'Husky')) + '. Patří do skupiny <a href="/kempingovy-nabytek/">kempingový nábytek</a>, ke které se hodí i <a href="/kempingove-stoly/">kempingové stoly</a> a <a href="/piknikove-deky/">piknikové deky</a>.</p>',
    guide='<h2>Typy kempingových židlí</h2>'
          '<p>Než začnete srovnávat značky, ujasněte si, kam židli povezete. Jiná se hodí do kufru auta, jiná na záda na třídenní přechod hor. Podle konstrukce se dělí na několik základních skupin.</p>'
          + T(['Typ', 'Výhody', 'Na co si dát pozor'], [
              ['Skládací křeslo s područkami', 'pohodlné sezení, držák na pití, rychlé složení do obalu', 'sbalené měří kolem metru, váží kolem 3 až 5 kg'],
              ['Režisérská židle', 'pevný sed, vyšší sezení, často boční stolek', 'složí se naplocho, ale do batohu se nevejde'],
              ['Polohovací křeslo a lehátko', 'opěradlo v několika polohách, opěrka nohou', 'vyšší hmotnost, delší složení'],
              ['Ultralehké křesílko', 'pod kilogram, sbalí se do malého vaku', 'nízký sed, menší nosnost, na měkkém terénu se boří'],
              ['Stolička a trojnožka', 'minimální rozměr, rybaření, festivaly', 'bez opěradla, na delší sezení nepohodlná']]) +
          '<h2>Nosnost: nejdůležitější číslo</h2>'
          '<p>Výrobci uvádějí maximální nosnost, nejčastěji mezi 100 a 150 kg, robustní modely i víc. Číslo platí pro klidné sezení na rovném podkladu. Když se do židle prudce sesunete, houpete se na zadních nohách nebo stojí na svahu, působí na konstrukci mnohem větší síla. Proto si nechte rezervu a pro těžšího člověka volte židli s nosností výrazně nad jeho hmotností. U levných modelů se nejčastěji lámou nýty a spoje v kloubech, ne samotné trubky.</p>'
          '<h2>Hmotnost a sbalený rozměr</h2>'
          '<p>U kempování autem na hmotnosti skoro nezáleží, zato rozhoduje, kolik židlí se vejde do kufru vedle stanu a chladicího boxu. Klasická skládací křesla se sbalí do dlouhého válcovitého obalu, režisérské židle a polohovací křesla se složí naplocho. Na cyklovýlety a túry se hodí ultralehká křesílka s hliníkovou kostrou spojenou gumovým lankem, podobně jako tyčky stanu. Sbalí se do vaku velikosti termosky a váží obvykle pod kilogram. Sedí se v nich ale nízko a vstávání je pro starší lidi méně pohodlné.</p>'
          '<h2>Materiál rámu a potahu</h2>'
          '<p>Ocelový rám je pevný a levnější, ale těžší a při poškození povrchové úpravy může rezavět. Hliníkový rám je lehčí a nekoroduje tolik, na stejnou nosnost však musí mít silnější profil. Potah bývá z polyesteru, často s označením 600D, kde vyšší číslo znamená silnější vlákno. Některá křesla mají vatované polstrování, které v chladném večeru hřeje, jiná síťované panely, které v létě větrají. Prodyšná síťovina se hodí k vodě, polstrování k podzimnímu ohni.</p>'
          '<h2>Pohodlí a výbava</h2>'
          '<ul><li><strong>Výška sedu:</strong> vyšší židle se snáz opouští a hodí se ke kempingovému stolu, nízké se hodí k ohni a na pláž.</li>'
          '<li><strong>Područky:</strong> pevné područky pomohou při vstávání, látkové jsou lehčí.</li>'
          '<li><strong>Opěradlo:</strong> vysoké opěradlo podepře hlavu, polohovací umožní odpočinek v pololehu.</li>'
          '<li><strong>Držák na nápoj a kapsy:</strong> praktické drobnosti, které na kempu oceníte.</li>'
          '<li><strong>Boční stolek:</strong> typický u režisérských židlí, na hrnek nebo knihu.</li>'
          '<li><strong>Patky nohou:</strong> širší patky se tolik nebořívají do měkké trávy a písku.</li></ul>'
          '<h2>Kempingové křeslo, nebo skládací židle ke stolu?</h2>'
          '<p>Hluboké kempingové křeslo je ideální k odpočinku, ale u stolu se v něm jí nepohodlně, protože sedíte nízko a zakloněni. Pokud na kempu plánujete společné jídlo, vyplatí se mít aspoň pár vyšších židlí s rovným sedem, třeba režisérských, nebo stůl s lavicemi. Kempingová křesla pak doplníte na večerní posezení. Pro rodiny s dětmi existují i dětské kempingové židličky, které jsou nižší a lehčí, takže si je dítě samo přenese.</p>'
          '<h2>Rybaření, festivaly a pláž</h2>'
          '<p>Rybáři používají speciální křesla se stavitelnými nohama, která se dají vyrovnat na nerovném břehu, a ta najdete u <a href="/rybarske-doplnky/">rybářských doplňků</a>. Na festivaly se hodí lehké skládací stoličky, které se snadno nosí, a na pláž nízká křesílka s krátkými nohami, která se v písku nepřevrhnou. Stejná pravidla platí i pro koncerty pod širým nebem: méně kil znamená, že židli nenecháte doma.</p>'
          '<h2>Židle pro seniory a pro bolavá záda</h2>'
          '<p>Starším lidem a těm, kdo mají potíže se zády nebo s koleny, se z nízkého a hlubokého křesla vstává špatně. Pro ně je lepší vyšší sed, pevné područky, o které se dá opřít, a opěradlo, které podepře bedra. Režisérské židle a některá polohovací křesla tyto požadavky splňují. Před koupí se podívejte na výšku sedu v popisu a porovnejte ji s židlí, na které člověk doma sedí rád.</p>'
          '<h2>U ohně opatrně</h2>'
          '<p>Polyester a nylon jsou syntetické látky, které od jiskry snadno propálí díru a v plameni se taví. Židle proto nestavte těsně k ohništi a nesušte na nich mokré oblečení nad ohněm. Hliníkové a ocelové trubky se na slunci i u ohně zahřejí, s čímž počítejte, když si sedá dítě v kraťasech. Vlněná deka přes opěradlo je u večerního ohně praktičtější než polstrování, které jiskra propálí.</p>'
          '<h2>Kolik židlí a jak je převézt</h2>'
          '<p>Při plánování výletu počítejte jednu židli na každého člena výpravy a ideálně jednu navíc pro návštěvu od sousedního stanu. Válcovité obaly klasických křesel se nejlépe skládají do kufru nastojato nebo podél stěny, režisérské židle naplocho pod ostatní věci. Pokud jedete s nosičem na střeše, vejdou se ploché židle do střešního boxu vedle stanu. Na kolo se hodí jen ultralehká křesílka, která připnete k nosiči nebo dáte do brašny.</p>'
          '<h2>Dětské kempingové židličky</h2>'
          '<p>Dětské modely mají nižší sed a menší nosnost a často veselé barvy nebo potisky, aby si dítě svou židli samo našlo. Vybírejte takovou, kterou dítě samo rozloží a složí bez rizika přiskřípnutí prstů v kloubech. Na nosnost nedávejte dospělé, i když se zdá, že židle vypadá pevně. Jakmile dítě vyroste, poslouží dětská židlička ještě jako podnožka nebo odkládací stolek.</p>'
          '<h2>Co hledat v popisu výrobku</h2>'
          '<ul><li><strong>Maximální nosnost</strong> a zda ji výrobce uvádí pro statické sezení.</li>'
          '<li><strong>Výška sedu a šířka sedáku</strong> v centimetrech, ne jen celkové rozměry.</li>'
          '<li><strong>Hmotnost</strong> a rozměr po složení, včetně obalu.</li>'
          '<li><strong>Materiál rámu</strong> a průměr trubek; silnější profil znamená tužší židli.</li>'
          '<li><strong>Typ látky</strong> a zda je potah snímatelný a pratelný.</li>'
          '<li><strong>Počet poloh opěradla</strong> u polohovacích křesel a způsob aretace.</li></ul>'
          '<p>Pokud popis některý z těchto údajů neuvádí, podívejte se na stránky výrobce nebo do návodu. Dvě židle stejného vzhledu se mohou nosností lišit o desítky kilogramů. Užitečné bývají i recenze zákazníků v e-shopech, které často prozradí, jak se židle chová po první sezoně, jestli látka nepraská u švů a zda obal po čase nepovolí.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Židli po výletě očistěte od písku a hlíny, zejména v kloubech, kde písek drhne a urychluje opotřebení. Mokrou nikdy neschovávejte do obalu, nechte ji nejprve proschnout. Na slunci látka časem bledne a slábne, proto židli nenechávejte venku celé léto. Pokud vrže, pomůže kapka silikonového spreje do kloubů. Před sezónou zkontrolujte nýty a švy; povolený nýt je předzvěstí zlomeniny.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr podle hmotnosti bez ohledu na nosnost.</li>'
          '<li>Nákup nízkých křesel k vysokému stolu.</li>'
          '<li>Ultralehké křesílko pro staršího člověka, kterému se z něj špatně vstává.</li>'
          '<li>Úzké nohy bez patek na písečnou pláž.</li>'
          '<li>Složení mokré židle do obalu a její zapomenutí do příští sezony.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka seřadí nabídky obchodů k vybrané židli, takže je můžete porovnat i s dopravou; objednávku pak dokončíte v e-shopu. Rozhodujte se nejprve podle nosnosti a způsobu dopravy, potom podle pohodlí a výbavy. K posezení se hodí <a href="/kempingove-stoly/">kempingový stůl</a>, na nápoje <a href="/chladici-boxy/">chladicí box</a> a na večerní světlo <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</p>',
    faq=[
        ('Jakou nosnost by měla mít kempingová židle?', 'Běžně se uvádí 100 až 150 kg, robustní modely snesou víc. Údaj platí pro klidné sezení na rovném podkladu, proto si nechte rezervu nad vlastní hmotností.'),
        ('Kolik váží kempingová židle?', 'Klasická skládací křesla váží obvykle kolem 3 až 5 kg, polohovací křesla víc. Ultralehká křesílka na túry se dostanou pod kilogram, sedí se v nich ale níž.'),
        ('Je lepší ocelový, nebo hliníkový rám?', 'Ocel je pevná a levnější, ale těžší a při poškození laku může rezavět. Hliník je lehčí a odolnější vůči korozi. Pro kempování autem stačí ocel, na cesty pěšky a na kole volte hliník.'),
        ('Jaká židle se hodí ke kempingovému stolu?', 'Vyšší židle s rovným sedem, například režisérská. V hlubokém kempingovém křesle se u stolu jí nepohodlně, protože sedíte nízko a zakloněni.'),
        ('Co dělat, když židle vrže?', 'Očistěte klouby od písku a hlíny a nastříkejte do nich trochu silikonového spreje. Zkontrolujte také nýty, protože vrzání může znamenat povolený spoj.'),
        ('Jak kempingovou židli skladovat?', 'Čistou a suchou ve vlastním obalu, v suchu a mimo přímé slunce. Mokrá látka v obalu plesniví a ocelový rám může korodovat.'),
        ('Je kempingová židle vhodná i na zahradu?', 'Ano, na občasné posezení určitě. Na celé léto venku ale není stavěná, protože látka na slunci bledne a slábne. Po použití ji uklízejte pod střechu.'),
        ('Jakou židli vzít na pláž?', 'Nízké křeslo s krátkými nohami nebo širokými patkami, které se v písku nebořívá a nepřevrhne. Prodyšná síťovina se hodí do horka a rychle uschne.'),
    ])

# ------------------------------------------------------------------ kempingove-stoly
NEW['kempingove-stoly'] = dict(long=True,
    title='Kempingový stůl: skládací, rolovací a stoly s lavicemi',
    desc='Kempingové stoly kufříkové, s rolovací deskou, s lavicemi i malé stolky do batohu. Jak vybrat rozměr, materiál desky a výšku nohou.',
    intro='<p>Kempingový stůl promění louku u stanu v jídelnu, kuchyň i místo na karty. Bez něj se vaří na zemi, talíře se převracejí v trávě a nádobí končí od písku. V nabídce jsou skládací stoly do kufru auta, stoly s rolovací deskou, které se sbalí do úzkého vaku, kempingové sety se dvěma lavicemi i malé stolky, které unese i cyklista. Liší se rozměrem, hmotností, materiálem desky a tím, jak dobře stojí na nerovném terénu. Než začnete vybírat, spočítejte, kolik lidí bude u stolu jíst a kolik místa zbývá v kufru auta po naložení stanu a spacáků.</p>'
          '<p>Sporteka vedle sebe ukazuje nabídky českých obchodů k jednotlivým stolům a nákup provedete přímo u vybraného e-shopu. Najdete tu stoly Coleman, Outwell, Highlander, Crossroad, Redcliffs nebo Travellife. Spadají do kategorie <a href="/kempingovy-nabytek/">kempingový nábytek</a>, k nim patří <a href="/kempingove-zidle/">kempingové židle</a> a k vaření <a href="/vareni-v-prirode/">vaření v přírodě</a>.</p>',
    guide='<h2>Typy kempingových stolů</h2>'
          '<p>Konstrukce stolu určuje, jak velký bude po složení a jak rychle ho postavíte. Pro kempování autem se hodí jiný typ než pro výlet na kole.</p>'
          + T(['Typ', 'Jak se skládá', 'Pro koho'], [
              ['Kufříkový stůl', 'deska se přeloží napůl, nohy se schovají dovnitř, nese se za držadlo', 'kempování autem, zahrada, trhy'],
              ['Stůl s rolovací deskou', 'lamely desky se srolují, rám se složí do vaku', 'kempování autem i karavan, menší sbalený objem'],
              ['Set stůl a dvě lavice', 'lavice se zaklapnou do desky stolu', 'rodiny, chaty, festivalový stánek'],
              ['Malý stolek do batohu', 'hliníkové lamely a tyčky na gumovém lanku', 'cyklovýlety, túry, vařič u stanu'],
              ['Kuchyňský kempingový stůl', 'rám s policemi, závětřím a místem pro vařič', 'delší pobyty, vaření pro více lidí']]) +
          '<h2>Rozměr desky a počet strávníků</h2>'
          '<p>Na jídlo pro dva stačí menší stůl, pro čtyřčlennou rodinu potřebujete desku zhruba o délce od 80 do 120 cm, aby se vedle talířů vešel i hrnec a láhev. Šest a více lidí se pohodlně usadí kolem stolu dlouhého 150 cm a víc, případně kolem dvou menších stolů postavených vedle sebe. Při výběru si změřte i místo v předsíni stanu, pokud chcete jíst pod střechou.</p>'
          '<h2>Výška a stavitelné nohy</h2>'
          '<p>Většina stolů má výšku podobnou domácímu stolu, tedy kolem 70 cm, a hodí se ke kempingovým židlím s vyšším sedem. Nízké stoly kolem 40 až 50 cm jsou určené k nízkým křesílkům a k pikniku. Stoly se stavitelnými nohama umí obojí: jednou slouží jako jídelní stůl, podruhé jako nízký stolek u ohně. Na nerovném terénu se hodí nohy s jemným nastavením nebo vyrovnávacími patkami, protože kempy s dokonale rovnou trávou jsou výjimka.</p>'
          '<h2>Materiál desky</h2>'
          '<ul><li><strong>Hliník:</strong> lehký, odolný vůči vodě i horkému hrnci, nejčastější u rolovacích stolů.</li>'
          '<li><strong>MDF nebo dřevotříska s povrchovou úpravou:</strong> pevné a levnější, ale citlivé na dlouhodobou vlhkost a na odřené hrany, kterými nasákne voda.</li>'
          '<li><strong>Plast (HDPE):</strong> pevná deska s vylisovanými žebry, snadno se myje, typická u kufříkových stolů.</li>'
          '<li><strong>Bambus a dřevěné lamely:</strong> pěkný vzhled, vyžadují péči a sušení.</li>'
          '<li><strong>Textilní deska:</strong> u nejlehčích stolků, unese jen hrnek a talíř.</li></ul>'
          '<p>Horký hrnec nebo pánev rovnou z vařiče nepokládejte na plastovou ani textilní desku, i když vypadá odolně. Na hliníkovém stole je méně riskantní, podložka ale neuškodí ani tam.</p>'
          '<h2>Nosnost a stabilita</h2>'
          '<p>Výrobci uvádějí nosnost desky, často v desítkách kilogramů. U malých stolků bývá nižší, protože jsou postavené na lehkost. Nosnost ale neznamená, že stůl unese člověka, který se o něj opře celou vahou při vstávání. Stabilitu zvyšují křížové vzpěry mezi nohama a široké patky. Stůl s rolovací deskou bývá na pohled jemnější, při rovnoměrném zatížení ale drží dobře; kufříkové stoly jsou tužší v kroucení.</p>'
          '<h2>Sbalený rozměr a hmotnost</h2>'
          '<p>Kufříkový stůl se složí naplocho a v kufru zabere plochu velkého kufru, rolovací stůl se vejde do úzkého vaku, který zastrčíte vedle zavazadel. Malé stolky s tyčkami na gumovém lanku se sbalí do velikosti láhve a váží kolem kilogramu nebo méně. Sety se dvěma lavicemi jsou nejtěžší, ale vyřeší sezení pro čtyři až šest lidí najednou a nemusíte k nim vozit židle.</p>'
          '<h2>Kempingová kuchyně</h2>'
          '<p>Kdo stanuje déle, ocení kuchyňský stůl s policemi, závětřím kolem vařiče a háčky na nádobí. Vařič na něm stojí ve vhodné výšce, potraviny jsou z dosahu mravenců a vše má své místo. Pro vaření potřebujete samozřejmě i <a href="/varice-a-kartuse/">vařič a kartuše</a> a <a href="/kempingove-nadobi/">kempingové nádobí</a>. Vařič vždy stavte na nehořlavý povrch a dál od stěny stanu.</p>'
          '<h2>Jak postavit stůl, aby se neviklal</h2>'
          '<p>Nejdřív vyberte co nejrovnější místo a odstraňte pod nohama větší kameny a šišky. Pak stůl postavte, zatlačte rukou na každý roh a sledujte, která noha se zvedá. U stavitelných nohou ji prodlužte nebo zkraťte, u pevných pomůže plochý kámen nebo kousek prkénka pod patkou. Na měkké trávě a v písku se nohy postupně boří, takže podložení širšími destičkami ušetří ranní rovnání. Když po rovnání všechny čtyři nohy pevně stojí, deska se nehoupe ani při krájení chleba.</p>'
          '<h2>Vítr a slunečník</h2>'
          '<p>Lehký hliníkový stolek odnese silný poryv větru snáz, než by člověk čekal, zvlášť když je na něm prázdný plastový ubrus. Na kempu u moře nebo na horské louce proto stůl na noc složte, nebo ho aspoň zatižte. Pokud chcete na stole slunečník, potřebujete model s otvorem v desce a pevný stojan; samotný stolek slunečník ve větru neudrží. Stín bezpečněji zajistí přístřešek ukotvený kolíky.</p>'
          '<h2>Stůl k obytnému autu a do karavanu</h2>'
          '<p>Majitelé obytných aut a karavanů řeší hlavně místo v úložném prostoru. Hodí se jim stoly, které se složí naplocho a vejdou se do štěrbiny za sedačkou nebo do garáže vozu, případně rolovací stoly v úzkém vaku. Ocení i nohy, které se dají vyrovnat, protože obytné auto často parkuje na mírném svahu. Kdo cestuje se psem nebo s dětmi, ocení omyvatelnou desku bez spár, ve kterých se drží drobky.</p>'
          '<h2>Na zahradu, trhy a akce</h2>'
          '<p>Kempingový stůl nemusí čekat v garáži jen na dovolenou. Kufříkový stůl poslouží jako odkládací plocha při zahradní oslavě, jako prodejní pult na bleším trhu nebo jako stůl na grilování. Stoly s plastovou deskou vydrží i občasné postříkání omáčkou a snadno se umyjí hadicí. Pro opakované stavění a skládání je ale dobré zkontrolovat, jak pevné jsou zámky nohou, protože na nich závisí bezpečnost všeho, co na stole leží.</p>'
          '<h2>Lehké stolky na túry a na kolo</h2>'
          '<p>Kdo nosí vybavení na zádech nebo veze v brašnách na kole, sáhne po malém stolku s deskou z hliníkových lamel nebo z napnuté látky. Takový stolek unese vařič, hrnek a talíř a ušetří vám vaření na kolenou nebo na pařezu. Je ale nízký, takže se k němu sedí na karimatce nebo na ultralehkém křesílku. Při výběru porovnávejte hmotnost, rozměr desky a to, zda se nohy dají zapíchnout i do měkkého terénu. Stolek s nohama na gumovém lanku se složí za pár vteřin a po cestě nenechává v batohu žádné volné díly, které by se mohly ztratit v trávě.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Desku po jídle otřete a stůl sbalte suchý. Zbytky jídla přitahují vosy a mravence a v uzavřeném obalu plesniví. Písek z kloubů a z lamel rolovací desky vyklepejte, jinak drhne a rámy se dřív opotřebují. Dřevěné a MDF desky skladujte v suchu a nenechávejte je přes noc v dešti. Hliníkový stůl snese víc, ale i jemu prospěje, když ho po sezoně umyjete a vysušíte.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Malý stolek koupený pro celou rodinu.</li>'
          '<li>Vysoký stůl k nízkým křesílkům, u kterého se jí s talířem na kolenou.</li>'
          '<li>Horký hrnec na plastové nebo textilní desce.</li>'
          '<li>MDF deska nechaná přes noc v dešti.</li>'
          '<li>Stůl bez stavitelných nohou na svažitém pozemku.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>U každého stolu vidíte nabídky více e-shopů a podmínky dopravy, takže snadno porovnáte, kde je stůl skladem; objednávka pak proběhne v obchodě. Rozhodujte se nejprve podle počtu lidí a způsobu přepravy, pak podle materiálu desky. Na nápoje a potraviny se podívejte na <a href="/chladici-boxy/">chladicí boxy</a>, na stín na <a href="/pristresky-a-party-stany/">přístřešky a party stany</a>.</p>',
    faq=[
        ('Jak velký kempingový stůl potřebuju pro rodinu?', 'Pro čtyři osoby se hodí deska zhruba od 80 do 120 cm, aby se vedle talířů vešel i hrnec. Pro šest a víc lidí volte stůl kolem 150 cm nebo dva menší stoly vedle sebe.'),
        ('Jaký je rozdíl mezi kufříkovým a rolovacím stolem?', 'Kufříkový stůl se složí naplocho a nese se za držadlo, je tužší, ale zabere víc místa. Rolovací deska se srolovaná vejde do úzkého vaku, který se snáz uloží do auta.'),
        ('Jaký materiál desky je nejodolnější?', 'Hliník je lehký a dobře snáší vodu i teplo. Plast se snadno myje. MDF je pevná, ale citlivá na dlouhodobou vlhkost. Horké nádobí raději pokládejte na podložku.'),
        ('K čemu jsou stavitelné nohy?', 'Umožňují vyrovnat stůl na nerovném terénu a u některých modelů změnit výšku z jídelní na nízkou ke křesílkům nebo k ohni.'),
        ('Unese kempingový stůl vařič?', 'Většina stolů ano, vařič ale stavte na nehořlavý povrch a stůl postavte stranou od stanu. Pro delší pobyty se vyplatí kuchyňský stůl se závětřím.'),
        ('Je lepší stůl s lavicemi, nebo samostatné židle?', 'Set s lavicemi vyřeší sezení pro více lidí najednou a sbalí se dohromady. Samostatné židle jsou pohodlnější a hodí se i k odpočinku mimo stůl.'),
        ('Jak zabránit tomu, aby se stůl viklal?', 'Postavte ho na co nejrovnější místo, odstraňte kameny pod nohama a vyrovnejte nohy, pokud jsou stavitelné. Na měkkém terénu podložte patky širšími destičkami, aby se nebořily.'),
        ('Jak stůl po kempování uložit?', 'Očistěte ho od jídla a písku, nechte uschnout a sbalte do obalu. Dřevěné a MDF desky skladujte v suchu, aby nenasákly a nekroutily se.'),
    ])
