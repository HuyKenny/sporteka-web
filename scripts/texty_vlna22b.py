"""sporteka.cz — wave 22b (4. 11. 2026): long texts (>= 1650 words) for nafukovaci-hracky, svihadla, kettlebelly, vybaveni-pro-kone.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ nafukovaci-hracky
NEW['nafukovaci-hracky'] = dict(long=True,
    title='Nafukovací hračky, lehátka a matrace do vody a na kemp',
    desc='Nafukovací kruhy, lehátka, ostrůvky a matrace do vody i do stanu. Jak vybrat velikost, materiál a pumpu a porovnat nabídky českých obchodů.',
    intro='<p>Pod názvem nafukovací hračky a lehátka se na Sportece skrývá pestrá směs. Najdete tu klasické kruhy, ostrůvky a zvířátka do bazénu, plovací lehátka na jezero, nafukovací křesla a také nafukovací matrace pro spaní v lese nebo na návštěvě u příbuzných. Společné mají jedno: drží tvar díky vzduchu, takže se do auta vejdou složené a po sezoně zabírají v komoře minimum místa.</p>'
          '<p>Nabídky českých obchodů tu porovnáváme u značek jako '
          + B(('bestway', 'Bestway'), ('intex', 'Intex'), ('acra-sport', 'ACRA Sport'), ('sea-to-summit', 'Sea to Summit'), ('sun-club', 'Sun Club'), ('avenli', 'Avenli'), ('skandika', 'Skandika'), ('quechua', 'Quechua')) +
          '. Na léto se hodí také <a href="/bazeny/">bazény</a>, <a href="/plavecke-pomucky/">plavecké pomůcky</a> a <a href="/plazove-doplnky/">plážové doplňky</a>, na spaní pod stanem <a href="/karimatky-a-matrace/">karimatky a matrace</a>.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Sortiment se rozpadá do dvou světů, které se potkávají jen kvůli stejnému materiálu. První je voda: dětské kruhy s motivem, velké ostrůvky pro několik lidí, lehátka s držákem na nápoj, hračky ve tvaru žraloka nebo labutě. Druhý je souš: samonafukovací a nafukovací matrace, vzduchové polštářky a lehká křesla do kempu. Než začnete porovnávat nabídky, rozhodněte, co skutečně hledáte, protože parametry se liší.</p>'
          + T(['Typ', 'Typické použití', 'Na co dát pozor'], [
              ['Plavecký kruh', 'děti v bazénu, brouzdaliště', 'velikost otvoru, věkové označení, bezpečné ventilky'],
              ['Plovací lehátko', 'odpočinek na hladině jezera nebo bazénu', 'nosnost, opěrka hlavy, odolnost proti slunci'],
              ['Velký ostrůvek a hrací zvíře', 'party v bazénu, hry', 'rozměr, počet komor, držadla'],
              ['Nafukovací křeslo a lehátko 2v1', 'zahrada, pláž, břeh vody', 'stabilita, rozměr po nafouknutí'],
              ['Nafukovací matrace pro dva', 'návštěva, chata, přistýlka', 'výška, vestavěná pumpa, materiál povrchu'],
              ['Samonafukovací a turistická matrace', 'stan, trek, kemp', 'izolace, hmotnost, rozměr po sbalení']]) +
          '<p>Toto členění pomáhá i při vyhledávání na Sportece. Zadáte-li název značky, rychle odfiltrujete nabídky, které s vaším účelem nesouvisí. Samonafukovací matrace od značek typu Robens nebo Sea to Summit patří spíš do outdooru, zatímco zvířátka a kruhy jsou doménou zábavních značek.</p>'
          '<h2>Hračky a lehátka do vody</h2>'
          '<h3>Kruhy a dětské pomůcky</h3>'
          '<p>Plavecký kruh je pro nejmenší oblíbený, ale nenahrazuje dohled dospělého ani plovací vestu. Je to hračka, ne záchranný prostředek. Dítě z něj může při neopatrném pohybu vyklouznout, proto vybírejte takový, který u pasu nebo mezi nohama drží. U miminek se hodí kruhy se sedátkem a bezpečnostním pásem. Starší děti už zvládnou jednoduchý kruh nebo rukávky, viz <a href="/plavecke-pomucky/">plavecké pomůcky</a>. Kdo hledá skutečnou jistotu na vodě, ať se podívá do kategorie <a href="/plovaci-vesty/">plovací vesty</a>.</p>'
          '<h3>Lehátka, ostrůvky a velké modely</h3>'
          '<p>Plovací lehátka mají velkou plochu, často s opěrkou hlavy nebo držákem na pití. Hodí se do bazénu a na klidnou hladinu rybníka, ne na moře s vlnami a proudem. Vítr dokáže lehké nafukovadlo odnést od břehu rychleji, než by člověk čekal. Když se chystáte na přírodní vodu, zvolte model s lanem nebo držadly a zůstávejte s ním jen v dosahu břehu.</p>'
          '<p>Velké ostrůvky pro čtyři a více lidí tvoří komory, které mají vlastní ventil. Dvě nebo tři komory znamenají, že při případném úniku vzduchu zůstane plocha alespoň částečně nadnášet. Pokud děti hrají hry s přeskakováním, vyhledejte tvrdší materiál a vyšší nosnost.</p>'
          '<h3>Zvířátka a hračky pro nejmenší</h3>'
          '<p>Hračky do bazénu ve tvaru žraloka, labutě nebo jednorožce jsou u dětí hit. Ve skutečnosti ale slouží především jako záminka k hraní, takže u nich sledujte spíš bezpečnost než technické parametry: hladký šev, žádné ostré hrany, ventil, který se dá zavřít jednou rukou, a pevné držadlo. Menší hračky ze slabší fólie vydrží jednu sezonu, silnější vinyl s vrstvou textilu vydrží déle.</p>'
          '<h2>Nafukovací matrace a lehátka pro spaní</h2>'
          '<p>Druhá polovina kategorie patří spaní. Nafukovací matrace pro dva s vestavěnou nebo pístovou pumpou se hodí pro návštěvu, chatu nebo cestu s větším autem. Mají vyšší profil, jsou měkké a obvykle potažené jemným povrchem, který se nesmekne. Pro trek a turistiku jsou určené úzké a lehké modely s izolací proti chladu země.</p>'
          '<p>U matrace počítejte s tím, že komfort se neodvíjí jen od výšky. Rozhoduje tvar komor, vnitřní konstrukce a to, jak dobře matrace drží vzduch přes noc. Dobrá turistická matrace je kompromis mezi hmotností, rozměrem po sbalení a izolací. Samonafukovací matrace obsahuje pěnu, která po otevření ventilku nasaje vzduch, a proto je při doplnění dechem příjemně pevná. Další informace najdete v kategorii <a href="/karimatky-a-matrace/">karimatky a matrace</a> a u zázemí kempu v kategoriích <a href="/kemping/">kemping</a>, <a href="/spaci-pytle/">spací pytle</a> a <a href="/vlozky-do-spacaku/">vložky do spacáků</a>.</p>'
          '<h2>Materiál a konstrukce</h2>'
          '<p>Většina levnějších kusů je z PVC, přesněji z vinylu s různou tloušťkou. Je lehce svařitelný, odolává vodě a dobře se čistí. Nevýhodou je křehkost za mrazu a citlivost na ostré předměty. Hračky určené do slunce by měly být odolné proti UV záření, jinak materiál časem tvrdne a praská ve švech. Turistické matrace se vyrábějí z polyesteru nebo nylonu s potahem z TPU, který je lehčí a při skládání méně namáhaný. Povrch bývá pogumovaný nebo vlnitý, aby člověk neklouzal.</p>'
          '<p>Cenu výrobku ovlivňuje i počet vrstev a způsob sváření. Plochy spojené vysokofrekvenčním svařováním drží lépe než lepené. Pokud na etiketě vidíte údaj o tloušťce materiálu, porovnávejte ho s konkurenčními kusy. Vyšší číslo zpravidla znamená odolnější výrobek, ale i vyšší hmotnost.</p>'
          '<h2>Jak nafukovat a čím</h2>'
          + T(['Způsob', 'Výhody', 'Nevýhody'], [
              ['Ústy', 'nic navíc nepotřebujete', 'únavné u velkých kusů, vlhkost uvnitř'],
              ['Ruční nebo nožní pumpa', 'levná, lehká, spolehlivá', 'u velkých ostrůvků zabere čas'],
              ['Elektrická pumpa na 12 V nebo na síť', 'rychlé nafouknutí, často i vyfouknutí', 'potřeba zdroj, hluk'],
              ['Pytel na nafukování pro matrace', 'šetří dech a vlhkost', 'jen pro vybrané modely']]) +
          '<p>Pumpa s několika nástavci se hodí na ventilky různých typů. Ventil typu Boston, typické pro bazénové kusy, má jiný průměr než ventil u karimatek. Zkontrolujte, jestli nástavce u pumpy vyhovují těm, které má vaše hračka.</p>'
          '<h2>Bezpečnost u vody</h2>'
          '<p>Nafukovací pomůcka dítě nechrání před utonutím. Při každém použití je potřeba být u dětí na dosah ruky a při koupání v přírodě znát hloubku i proudění. Označení věku na obalu platí a nemá se obcházet. Pro větší vodní plochy se hodí plovací vesta odpovídající hmotnosti dítěte; lano slouží jen k připoutání lehátka ke břehu, před utonutím dítě nechrání. Jinak se doporučuje držet se jen do míst, kde dítě dosáhne na dno.</p>'
          '<p>Při použití na slunci myslete také na ochranu kůže. Plavky s UV faktorem, tričko a čepice zmenší riziko spálení, viz <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> a <a href="/detske-plavky/">dětské plavky</a>. Pro cestu na pláž se hodí i <a href="/pop-up-a-plazove-stany/">pop-up a plážové stany</a>, ve kterých je stín.</p>'
          '<h2>Péče, čištění a skladování</h2>'
          '<p>Po koupání ve slané nebo chlorované vodě hračku opláchněte sladkou vodou, jinak se materiál časem naruší. Úplně vysušte, než ji složíte, vlhkost vede k plísním a zápachu. Skladujte na suchém místě bez ostrých předmětů a mimo dosah slunce a zdrojů tepla. Neukládejte natlakované hračky v autě za horka, protože vzduch uvnitř se rozpíná a může protrhnout šev.</p>'
          '<p>Díra se nejčastěji hledá ponořením nafouknutého kusu do vody a pozorováním bublinek, případně potřením mýdlovou pěnou. Záplata ze soupravy na lepení zpravidla funguje, pokud je povrch čistý a suchý. Většina záplat vyžaduje několik hodin tuhnutí.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš velký ostrůvek do malého bazénu, který se pak nevejde ani do vody, ani do auta.</li>'
          '<li>Matrace pro dva vybraná jen podle rozměru, bez ohledu na nosnost a výšku.</li>'
          '<li>Nafukování turistické matrace ústy při zimních výpravách, kdy vlhkost uvnitř mrzne.</li>'
          '<li>Podcenění obalu a ventilů, přestože právě tam bývá nejčastější únik vzduchu.</li>'
          '<li>Zapomenutá pumpa nebo záplata ve výbavě.</li></ul>'
          '<h2>Kdo si co vybere</h2>'
          '<p>Rodina s malými dětmi ocení kruhy se sedátkem, malé hračky a menší matraci do dětského koutku. Parta kamarádů na rybníku si užije velký ostrůvek, zatímco pár u jezera zvolí plovací lehátko. Vodáci a paddleboarďáci se podívají do <a href="/vodni-sporty/">vodních sportů</a>, <a href="/paddleboardy/">paddleboardů</a> a <a href="/kajaky-a-cluny/">kajaků a člunů</a>. Chataři a lidé, kteří přijímají hosty, vyberou dvojmatraci, kemperi lehkou turistickou karimatku nebo <a href="/hamaky/">hamak</a> či <a href="/stany/">stan</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka sleduje nabídky českých obchodů a pomůže vám ověřit, kde je kus skladem. U každé položky se vyplatí přečíst rozměr po nafouknutí, materiál, nosnost a to, zda je pumpa součástí balení. Začněte značkou, kterou znáte, a pak ji porovnejte s dalšími. U dětských kusů se dívejte na věkové označení a certifikace uvedené výrobcem.</p>',
    faq=[
        ('Nahradí nafukovací kruh plovací vestu?', 'Ne. Kruh je hračka a dítě z něj může vyklouznout. Plovací vesta má tvar, který drží tělo při hladině. Při koupání malých dětí je nutný stálý dohled dospělého.'),
        ('Jak poznám, že mi hračka nebo matrace pomalu uniká vzduch?', 'Po nafouknutí nechte kus několik hodin ležet a zkontrolujte, zda zůstal pevný. Pokud změkl, ponořte ho do vody nebo potřete mýdlovou vodou. Bublinky ukážou místo úniku.'),
        ('Dá se nafukovací hračka opravit?', 'Menší dírku většinou vyspravíte záplatou z opravné soupravy. Povrch musí být čistý a suchý a lepidlo potřebuje čas, než zatuhne. Poškozený šev nebo větší trhlina se opravuje hůř.'),
        ('Jak dlouho vydrží nafukovací hračka?', 'Záleží na tloušťce materiálu, intenzitě používání a péči. Slabší fólie obvykle vydrží jednu sezonu, silnější vinyl s potahem déle. Správné skladování a umytí po koupání životnost výrazně prodlouží.'),
        ('Můžu nafukovací lehátko použít na moři?', 'Spíš ne. Vítr a proudy unášejí lehké nafukovadlo od břehu. Na otevřené vodě je bezpečnější zůstat v dosahu pláže, mít kus připoután lanem a znát podmínky na místě.'),
        ('Jaká pumpa se k nafukovacím hračkám hodí?', 'Pro malé kusy stačí ruční, u velkých ostrůvků a matrací pro dva se vyplatí elektrická nebo pístová. Důležité je, aby měla nástavce odpovídající ventilům.'),
        ('Proč se matrace ráno sama vyfoukla?', 'Nejčastější příčinou je neuzavřený ventil, drobná trhlina nebo pokles teploty, který stlačí vzduch uvnitř. Zkontrolujte ventil, doplňte vzduch a případně použijte test s mýdlovou vodou.'),
        ('Jak čistit nafukovací hračku?', 'Opláchněte čistou vodou, případně jemným mýdlovým roztokem, a nechte úplně vyschnout. Nepoužívejte agresivní chemii ani abrazivní houbičky, mohly by poškodit povrch.'),
        ('Jaký je rozdíl mezi nafukovací a samonafukovací matrací?', 'Nafukovací matrace plníte vzduchem celou. Samonafukovací obsahuje pěnu, která po otevření ventilku nasaje část vzduchu sama. Dofouknutí je pak rychlé a izolace bývá lepší.'),
        ('Mohu hračky nechat přes zimu venku?', 'Nedoporučuje se. Mráz zkřehčí PVC a UV záření poškodí povrch. Vyperte, vysušte, lehce poprášete mastkem a uložte složené na suché místo.'),
        ('Pro jak staré děti jsou nafukovací kruhy?', 'Věk určuje výrobce na obalu. Pro nejmenší jsou kruhy se sedátkem a opěrkou, pro větší děti jednoduché kruhy. Označení věku se vyplatí dodržet.'),
    ])

# ------------------------------------------------------------------ svihadla
NEW['svihadla'] = dict(long=True,
    title='Švihadla: rychlostní, zátěžová, kožená i s počítadlem',
    desc='Švihadla na box, crossfit, kondici i děti: rychlostní, zátěžová, kožená a digitální. Jak vybrat délku, materiál a značku a porovnat nabídky.',
    intro='<p>Švihadlo je nenápadná pomůcka, která umí víc, než by člověk čekal. Rozproudí krev, zlepší koordinaci, zahřeje před tréninkem a vejde se do kapsy. Na Sportece v kategorii najdete jednoduché dětské modely, kožená švihadla s dřevěnými ručkami, rychlostní kabely pro crossfit, zátěžové verze, švihadla s počítadlem i bezdrátové digitální kousky.</p>'
          '<p>Porovnáváme nabídky českých obchodů u značek jako '
          + B(('merco', 'Merco'), ('sedco', 'Sedco'), ('fitforce', 'Fitforce'), ('sportago', 'Sportago'), ('hms', 'HMS'), ('lifefit', 'Lifefit'), ('domyos', 'Domyos'), ('gymbeam', 'GymBeam')) +
          '. K tréninku se hodí také <a href="/fitness-pomucky/">fitness pomůcky</a>, <a href="/boxovaci-pytle/">boxovací pytle</a> a <a href="/funkcni-trenink/">funkční trénink</a>.</p>',
    guide='<h2>Druhy švihadel a k čemu slouží</h2>'
          '<p>Nejlepší švihadlo neexistuje, existuje jen takové, které sedí na váš účel. Na pomalém skákání pro radost stačí cokoli, ale při intervalech a technických trikách rozdíl pocítíte po pár minutách. Základní rozdělení vychází z materiálu lanka a konstrukce rukojetí.</p>'
          + T(['Typ', 'Charakter', 'Vhodné pro'], [
              ['Dětské a gymnastické', 'lehké, často z plastu nebo bavlny, barevné', 'děti, školní tělocvik, rytmická gymnastika'],
              ['Kožené', 'těžší, příjemný rytmus, dřevěné ručky', 'box, bojové sporty, rozcvička'],
              ['Rychlostní kabel', 'tenké ocelové lanko v obalu, kuličková ložiska', 'crossfit, double-unders, intervaly'],
              ['Zátěžové', 'těžší lanko nebo zatížené rukojeti', 'silová kondice, ramena, předloktí'],
              ['S počítadlem', 'displej v ručce, počítá skoky', 'motivace, měření výkonu'],
              ['Bezdrátové digitální', 'bez lana, počítadlo v ručkách', 'cvičení v malém prostoru, byt']]) +
          '<p>Velkou skupinu tvoří univerzální lanka z PVC, která se dají zkracovat a stačí na pravidelné cvičení. Kdo chce zlepšovat techniku, měl by si časem pořídit kvalitnější rychlostní kabel, který se otáčí plynule a nezamotává.</p>'
          '<h2>Jak vybrat správnou délku</h2>'
          '<p>Délka je klíčový parametr. Příliš dlouhé lano se plete, příliš krátké nutí přitahovat kolena a zvedat ramena. Orientační postup je jednoduchý: postavte se na střed lanka a zvedněte ručky ke svému tělu. Při správné délce dosáhnou rukojeti zhruba do úrovně podpaží, u rychlostních kabelů o něco níž. Děti potřebují kratší lano než dospělí, proto výrobci uvádějí velikosti číslem nebo výškovým rozmezím.</p>'
          '<p>Většina modelů se dá seříznout nebo seřídit kolíčkem. Zkracujte opatrně a vždy po malých kouscích, protože prodloužit se lano už nedá. Pokud švihadlo sdílí více lidí, hodí se model s plynulým nastavením délky.</p>'
          '<h2>Materiál lana a rukojetí</h2>'
          '<h3>Lano</h3>'
          '<p>PVC je levné a odolné, ale při dopadu na tvrdý povrch se opotřebovává. Bavlněné nebo hrubé provazy mají příjemný rytmus, jsou však náchylné na vlhkost. Kožené lanko je těžší a drží tvar, hodí se do tělocvičny a na dřevěnou nebo gumovou podlahu. Ocelové lanko v plastovém plášti rotuje rychle a hodí se do tréninku s vyšším tempem.</p>'
          '<h3>Rukojeti</h3>'
          '<p>Dřevěné ručky dobře sedí, ale mohou při pocení klouzat. Plastové jsou lehké a levné. Hliníkové a pogumované drží i při vlhkých dlaních, ale mohou být těžší. U rychlostních modelů hrají hlavní roli ložiska: uložení má zajistit, aby se lano točilo, i když ruka nehybně drží rukojeť. Pokud lano skřípe, ložisko je opotřebené nebo znečištěné.</p>'
          '<h2>Podle sportu</h2>'
          '<p>Boxeři a bojovníci využívají švihadlo jako součást rozcvičky i tréninku nožní práce. Zpravidla preferují kožené nebo střední PVC modely, které dávají rytmus, ne rychlost. Více se dozvíte v <a href="/bojove-sporty/">bojových sportech</a> a u <a href="/boxerske-rukavice/">boxerských rukavic</a>.</p>'
          '<p>Crossfit vyžaduje rychlost. Dvojité přeskoky, takzvané double-unders, potřebují tenký kabel s plynulým otáčením. Funkční trénink často střídá skákání s činkami, viz <a href="/kettlebelly/">kettlebelly</a> a <a href="/cinky-a-kotouce/">činky a kotouče</a>. Fotbalisté, basketbalisté a další hráči míčových her skáčou pro lepší reaktivitu a odraz, viz <a href="/micove-sporty/">míčové sporty</a>. Gymnastky a děti ocení barevné lehké modely nebo stuhu, viz <a href="/tanec-a-gymnastika/">tanec a gymnastika</a> a <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>'
          '<h2>Kde skákat</h2>'
          '<p>Povrch ovlivňuje jak výdrž lana, tak zdraví kloubů. Beton a asfalt jsou nejhorší volba: tvrdé a brusné. Dřevěná podlaha nebo pružná tělocvičná podložka je výrazně šetrnější. Doma pomůže gumová podložka a vhodná <a href="/treninkova-obuv/">tréninková obuv</a>, která tlumí dopad. Kdo skáče v bytě, měl by dbát na sousedy pod sebou a zvolit tišší lanka.</p>'
          '<h2>Technika, kterou zvládne každý</h2>'
          '<p>Základ je jednoduchý: lokty u těla, otáčení z předloktí a zápěstí, malý odraz. Ramena nezvedejte, pohled směřujte před sebe. Pro začátek stačí krátké série, třeba třicet vteřin skákání a stejně dlouhá pauza. Postupně prodlužujte aktivní část. Jakmile zvládnete základní skok, přidejte střídání nohou, boxerský krok nebo přeskok s křížením rukou. Technické prvky se nejlépe učí na lehčím a rychlejším lanku.</p>'
          '<p>Švihadlo může být součástí zahřátí před během, viz <a href="/beh/">běh</a>, nebo doplňkem kardio tréninku vedle <a href="/kardio-trenazery/">kardio trenažérů</a>. Kdo má problémy s kolenními klouby, kotníky nebo zády, měl by se před zahájením pravidelného skákání poradit s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Švihadlo s počítadlem a digitální modely</h2>'
          '<p>Počítadlo skoků v ručce je užitečné, pokud chcete sledovat pokrok nebo držet cíl. Mechanická verze počítá otáčky, digitální může zobrazovat čas i odhad kalorií. Údaje berte jako orientační, protože výrobci počítají odlišně. Bezdrátová švihadla bez lana se hodí tam, kde není místo, například v malém bytě. Technika skákání je však jiná, takže je neberte jako náhradu klasických.</p>'
          '<p>U modelů s baterií se podívejte, zda se dá vyměnit. U rychlostních kabelů s displejem je dobré, aby se lano dalo nahradit.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Po tréninku lano otřete suchým hadříkem, zvlášť pokud cvičíte venku.</li>'
          '<li>Kožené modely občas ošetřete vhodným přípravkem, aby nepraskaly.</li>'
          '<li>Rychlostní kabely skladujte volně svinuté, bez ostrých zlomů.</li>'
          '<li>Ložiska občas očistěte a nechte oschnout, olejujte jen podle pokynů výrobce.</li>'
          '<li>Opotřebovaný plášť nebo uvolněné koncovky včas vyměňte, aby nehrozilo prasknutí při skoku.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<p>Nejčastější chybou je špatná délka. Druhá je skákání na tvrdém povrchu v nevhodné obuvi. Třetí chyba spočívá v nadměrném tempu hned na začátku, což vede k bolestem lýtek a achillových šlach. Čtvrtá je kupování nejtěžšího švihadla, protože zátěž mění rytmus a není pro každého. Začátečník by měl mít lehké univerzální lano, které později doplní specializovaným kusem.</p>'
          '<h2>Pro koho které švihadlo</h2>'
          '<p>Děti a školáky potěší barevná lehká lanka. Začátečníci vyberou univerzální PVC se střední délkou. Pokročilí zvolí rychlostní lano s ložisky. Bojovníci sáhnou po kožených modelech, silově orientovaní po zátěžových. Pokud potřebujete sestavit kompletní domácí tréninkový koutek, přidejte <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/joga-a-podlozky/">podložku</a> a <a href="/hrazdy-a-bradla/">hrazdu</a>.</p>'
          '<h2>Nákup na Sportece</h2>'
          '<p>Při srovnání nabídek se řiďte délkou, materiálem lanka, typem ložisek a váhou. U značek jako Domyos nebo Sedco pomůže zkontrolovat velikostní tabulku. Sledujte také, zda je nabídka skladem a v jakém obchodě. Díky přehledu uvidíte, ve kterém e-shopu najdete právě to, co potřebujete.</p>',
    faq=[
        ('Jak dlouhé švihadlo potřebuji?', 'Postavte se na střed lanka a zvedněte ručky. Rukojeti by měly sahat zhruba do podpaží. Rychlostní kabely bývají o něco kratší. Děti potřebují menší velikosti.'),
        ('Je lepší lanko kožené, PVC, nebo ocelové?', 'Kožené má rytmus a hodí se na box, PVC je univerzální a odolné, ocelové lanko v plášti je nejrychlejší. Výběr se řídí účelem a povrchem, na kterém skáčete.'),
        ('Na jakém povrchu se skáče nejlépe?', 'Nejšetrnější je pružná podložka nebo dřevěná podlaha. Beton a asfalt jsou tvrdé a zničí lano i klouby. Pomůže také obuv s tlumením.'),
        ('Dá se švihadlo zkrátit?', 'U většiny modelů ano, odříznutím nebo seřízením u rukojeti. Zkracujte opatrně po malých částech, prodloužit už lano nelze.'),
        ('K čemu je lano s ložisky?', 'Ložisko umožňuje, aby se lano otáčelo nezávisle na ruce. Zlepšuje plynulost při rychlém skákání a zabraňuje zamotání. Je vhodné pro pokročilé a crossfit.'),
        ('Je zátěžové švihadlo vhodné pro začátečníky?', 'Spíš ne. Mění rytmus a zatěžuje ramena i předloktí. Začněte s lehkým, naučte se techniku a těžší model přidejte později.'),
        ('Jak často můžu skákat?', 'Záleží na kondici a cíli. Začátečníci začínají krátkými sériemi několikrát týdně a pomalu je prodlužují. Při potížích s klouby se poraďte s lékařem.'),
        ('Počítá počítadlo správně?', 'Pro orientaci ano, ale není měřicí přístroj. Údaje o kaloriích jsou odhad. Pro sledování pokroku postačí srovnání vlastních výsledků v čase.'),
        ('Jak pečovat o kožené švihadlo?', 'Po tréninku otřete a nenechávejte vlhké. Občas ošetřete přípravkem na kůži. Skladujte na suchém místě mimo radiátor.'),
        ('Hodí se švihadlo pro děti?', 'Ano, rozvíjí koordinaci a rytmus. Vyberte lehký model s přiměřenou délkou a skákání provádějte na rovném, pružném povrchu.'),
        ('Můžu skákat doma v bytě?', 'Ano, pokud máte dost prostoru a pružnou podložku. Počítejte s hlukem dopadu a vybírejte měkčí lano, které nešlehá o strop ani o nábytek.'),
    ])

# ------------------------------------------------------------------ kettlebelly
NEW['kettlebelly'] = dict(long=True,
    title='Kettlebelly: ocelové, vinylové i nastavitelné činky',
    desc='Kettlebelly od lehkých po těžké: litinové, poplastované, vinylové i nastavitelné. Jak vybrat hmotnost, tvar madla a začít cvičit s kettlebellem.',
    intro='<p>Kettlebell neboli činka s kuličkou a madlem je jedno z nejuniverzálnějších závaží pro domácí cvičení. Těžiště leží mimo ruku, takže se s ním dají provádět švihy, přenášení, tahy i turecké vstávání. Na Sportece najdete litinové a ocelové kusy, poplastované a vinylové modely, měkké kettlebelly pro začátečníky i nastavitelné verze, které se plní pískem nebo doplňují kotouči.</p>'
          '<p>Nabídky českých obchodů srovnáváme u značek jako '
          + B(('hms', 'HMS'), ('sedco', 'Sedco'), ('gorilla-sports', 'Gorilla Sports'), ('domyos', 'Domyos'), ('sharp-shape', 'Sharp Shape'), ('actiget', 'Actiget'), ('sportago', 'Sportago'), ('lifefit', 'Lifefit')) +
          '. K základní výbavě patří také <a href="/cinky-a-kotouce/">činky a kotouče</a>, <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>',
    guide='<h2>Z čeho se kettlebelly vyrábějí</h2>'
          '<p>Materiál ovlivňuje cenu, hlučnost i trvanlivost. Kettlebelly se na první pohled podobají, ale jejich chování se při dopadu a při chytání liší.</p>'
          + T(['Typ', 'Vlastnosti', 'Hodí se pro'], [
              ['Litinový holý', 'klasický, tvrdý, hrubý povrch', 'zkušené, silový a ruský styl'],
              ['Poplastovaný nebo pogumovaný', 'chrání podlahu, tišší', 'domácí použití, byt'],
              ['Vinylový plněný pískem', 'měkčí povrch, nižší hmotnosti', 'začátečníci, rodinné cvičení'],
              ['Měkký kettlebell', 'textilní nebo pěnový obal, bezpečný pro dopady', 'přenášení, cviky na zemi, děti a senioři'],
              ['Nastavitelný', 'regulace hmotnosti kotouči nebo pískem', 'malý prostor, postupné zvyšování'],
              ['Kettlebell s funkcí činky 3v1', 'rozložitelný, podpěra na kliky', 'domácí komplexní cvičení']]) +
          '<p>Soutěžní ocelové modely mají stejný rozměr bez ohledu na hmotnost, a to je výhoda: když se zvýší váha, neroste velikost. U litinových, vinylových a pískem plněných modelů roste objem s hmotností, což mění úchop i způsob cvičení.</p>'
          '<h2>Jak vybrat hmotnost</h2>'
          '<p>Správná hmotnost závisí na tom, co s činkou budete dělat. Švihy a tahy používají sílu celého těla a snesou vyšší zátěž. Tlaky nad hlavu, shyby a turecké vstávání zatěžují menší svalové skupiny a vyžadují lehčí kus. Začátečníci by měli vybírat opatrně, aby udrželi techniku. Příliš těžká činka vede k nesprávnému pohybu a bolestem zad.</p>'
          '<p>Obecně platí, že ženy a úplní začátečníci začínají lehčími kusy a časem přidávají. Muži s tréninkovou zkušeností si mohou vybrat těžší. Praktický postup je pořídit dva kettlebelly: lehčí na techniku a těžší na švihy. Zkušení si pak přidají třetí. Nastavitelný model nahradí více kusů, ale je objemnější a méně příjemný při dopadu.</p>'
          '<h2>Madlo, rám a váha</h2>'
          '<p>Kvalitní kettlebell má hladké a širší madlo, ve kterém projdou dvě ruce při dvouručním švihu. Povrch rukojeti by neměl být ani příliš hrubý, ani lakovaný do lesku, protože s křídou se drží špatně. Zkontrolujte, zda je přechod mezi madlem a tělem plynulý a bez ostrých hran. Dno má být ploché a stabilní, aby se činka dala bezpečně odložit.</p>'
          '<p>Pokud je v popisu uvedena hmotnost v librách, převeďte si ji. Jedna libra odpovídá asi 0,45 kg, a proto se hodnoty v kilogramech a librách mírně liší. Nezapomeňte, že kettlebelly se prodávají i v neokrouhlých hmotnostech.</p>'
          '<h2>Základní cviky</h2>'
          '<h3>Švih</h3>'
          '<p>Základní a nejoblíbenější cvik. Činka se pohybuje z prostoru mezi nohama do výše hrudníku a pohyb vychází z kyčlí, ne z rukou. Rovná záda, pevný střed těla a plynulé přenášení váhy jsou nutností. Švih trénuje zadní řetězec a kondici.</p>'
          '<h3>Goblet dřep</h3>'
          '<p>Kettlebell se drží u hrudi za rohy madla. Je to ideální cvik pro učení správné techniky dřepu. Zátěž vpředu pomáhá udržet rovná záda a hluboký dřep.</p>'
          '<h3>Turecké vstávání</h3>'
          '<p>Složitý cvik, který rozvíjí stabilitu ramene i celého těla. Začíná se bez zátěže nebo s lehkou činkou. Správné provedení je důležitější než hmotnost.</p>'
          '<h3>Další variace</h3>'
          '<p>Tlaky nad hlavu, přitahování k tělu, nosení v ruce a mrtvý tah s kettlebellem doplňují sestavu. Pro celkovou kondici můžete cviky zřetězit do intervalového tréninku, viz <a href="/funkcni-trenink/">funkční trénink</a>. Pro zahřátí se hodí <a href="/svihadla/">švihadla</a> a <a href="/joga-a-podlozky/">podložka</a>.</p>'
          '<h2>Kde cvičit</h2>'
          '<p>Na tvrdé dlažbě se kettlebell při pádu poškodí, a hlavně poškodí podlahu. Pod činku patří gumová podložka nebo pogumovaná podlaha. V bytě je výhodné zvolit poplastovaný model. Venku na trávě se vyplatí rovný pevný povrch, na kterém neklouzáte. Cvičební obuv s pevnou podrážkou zlepšuje stabilitu, viz <a href="/treninkova-obuv/">tréninková obuv</a> a <a href="/barefoot-obuv/">barefoot obuv</a>.</p>'
          '<h2>Jak kettlebell zapadá do domácí posilovny</h2>'
          '<p>Kettlebell je dobrý základ minimalistické posilovny. K dispozici je celotělový trénink s jednou nebo dvěma činkami. Doplňte jej o <a href="/hrazdy-a-bradla/">hrazdu</a>, <a href="/posilovaci-gumy/">gumy</a> a <a href="/balancni-pomucky/">balanční pomůcky</a>. Pokud chcete větší flexibilitu, přidejte klasické <a href="/cinky-a-kotouce/">jednoručky</a> nebo <a href="/posilovaci-stroje/">posilovací stroj</a>. Pro regeneraci jsou užitečné <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>'
          '<h2>Bezpečnost a technika</h2>'
          '<p>Pohyb začíná z kyčlí a nohou, ne ze zad. Neohýbejte páteř, nezvedejte činku rukama a nedržte dech. Před zahájením si ověřte, že máte kolem sebe dost místa a že madlo není klouzavé. Pro začátek je vhodné cvičení s trenérem nebo podle kvalitního videa. Pokud máte potíže se zády, rameny nebo srdcem, konzultujte trénink s lékařem či fyzioterapeutem.</p>'
          '<h2>Péče o kettlebell</h2>'
          '<ul><li>Litinové kusy otřete od potu a vlhkosti, aby nerezly.</li>'
          '<li>Při rzi použijte jemnou drátěnku a naolejujte tenkou vrstvou oleje.</li>'
          '<li>Poplastované kettlebelly neskladujte na slunci ani u topení.</li>'
          '<li>U nastavitelných modelů občas zkontrolujte uzávěry.</li>'
          '<li>Neodkládejte činku na schody, snadno se rozbije dlaždice i kettlebell.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější je výběr příliš těžké činky. Další je nákup nejlevnějšího kusu s hrubým švem, který poškozuje ruce. Chyba je i koupě pouze jednoho kettlebellu a následné zjištění, že na vybrané cviky nestačí. Neúplná je také představa, že nastavitelný kus vždy nahradí pevný: má jiný tvar a vyvážení.</p>'
          '<h2>Pro koho je kettlebell</h2>'
          '<p>Hodí se začátečníkům, kteří chtějí jednoduchou pomůcku na celé tělo, i pokročilým, kteří upravují trénink pro kondici a sílu. Měkké kettlebelly ocení rodiny a senioři. Sportovci z míčových her, běžci a cyklisté oceňují posílení zadního řetězce a stability. Pro doplnění viz <a href="/beh/">běh</a>, <a href="/cyklistika/">cyklistika</a> a <a href="/micove-sporty/">míčové sporty</a>.</p>'
          '<h2>Nákup na Sportece</h2>'
          '<p>Porovnejte materiál, hmotnost a typ madla u více obchodů. Zkontrolujte, zda je nabídka skladem, a u nastavitelných modelů, co je součástí balení. Díky přehledu uvidíte více variant značek na jednom místě a vyberete tu, která odpovídá vašemu účelu.</p>',
    faq=[
        ('Jakou hmotnost kettlebellu mám začít?', 'Začněte lehčím kusem, na kterém udržíte správnou techniku. Příliš těžká činka vede k chybám. Až budete jistí, přidejte těžší kus.'),
        ('Je lepší jeden nastavitelný kettlebell, nebo více pevných?', 'Nastavitelný šetří místo, ale bývá objemnější a jinak vyvážený. Pevné kusy mají stabilní tvar a komfortnější držení. Záleží na prostoru a stylu cvičení.'),
        ('Čím se liší litinový a poplastovaný kettlebell?', 'Litina je tvrdá a odolná, poplastovaný model je tišší a šetrnější k podlaze. U obou drží velikost nezávisle na změně hmotnosti, pokud jde o plné kusy.'),
        ('Jaký cvik je nejlepší pro začátek?', 'Goblet dřep a švih. Dřep učí držení těla, švih rozvíjí práci kyčlí. Oba cviky začněte s lehkou činkou.'),
        ('Dá se s kettlebellem cvičit v bytě?', 'Ano, na gumové podložce a s poplastovaným nebo měkkým kusem. Dejte pozor na strop, nábytek a sousedy pod vámi.'),
        ('Jak čistit rez z kettlebellu?', 'Rez odstraňte jemnou drátěnkou nebo brusným papírem, poté otřete a naolejujte. Nasucho skladujte, aby se nevracela.'),
        ('Jsou měkké kettlebelly bezpečnější?', 'Pro dopady a cviky na zemi ano, protože mají měkký povrch. Pro těžké švihy mají méně příjemný tvar a nižší hmotnosti.'),
        ('Mohu s kettlebellem cvičit denně?', 'Záleží na zátěži a regeneraci. Začátečníkům stačí několik tréninků týdně s odpočinkem. Při bolesti se poraďte s lékařem.'),
        ('Co znamená zkratka lbs v popisu?', 'Je to libra, anglická jednotka hmotnosti. Jedna libra odpovídá asi 0,45 kg, takže 20 lbs je přibližně devět kilogramů.'),
        ('Kolik kettlebellů stačí na domácí cvičení?', 'Pro začátek jeden až dva kusy různé hmotnosti. Pak podle pokroku přibudou další. Pestrost zajišťují i jiné pomůcky, jako gumy nebo hrazda.'),
    ])

# ------------------------------------------------------------------ vybaveni-pro-kone
NEW['vybaveni-pro-kone'] = dict(long=True,
    title='Vybavení pro koně: deky, ohlávky, péče, krmné doplňky',
    desc='Vybavení pro koně a poníky: deky, ohlávky, udidla, čabraky, kartáče, kopytní mast, lizy a doplňky. Jak vybrat velikost a porovnat nabídky obchodů.',
    intro='<p>Kůň je velké zvíře s požadavky, které se mění s ročním obdobím, tréninkem i věkem. Proto je kategorie vybavení pro koně tak široká. Najdete tu deky do výběhu a do stáje, ohlávky a uzdečky, udidla a otěže, čabraky, kartáče a šampony, kopytní masti, solné lizy, doplňkové krmivo i drobné doplňky pro jezdce na vyjížďky.</p>'
          '<p>Na Sportece porovnáváme nabídky českých obchodů u značek jako '
          + B(('fouganza', 'Fouganza'), ('start', 'Start'), ('waldhausen', 'Waldhausen'), ('topvet', 'Topvet'), ('galop-wear', 'Galop Wear'), ('horseware-ireland', 'Horseware Ireland'), ('kerbl', 'Kerbl'), ('vetoquinol', 'Vetoquinol')) +
          '. Pro jezdce se hodí také <a href="/jezdectvi/">jezdectví</a>, <a href="/jezdecke-helmy/">jezdecké helmy</a>, <a href="/jezdecka-obuv/">jezdecká obuv</a> a <a href="/jezdecke-doplnky/">jezdecké doplňky</a>.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Kategorie sdružuje vše, co se týká koně samotného, od ochrany přes ošetřování až po výživu. Vybavení jezdce, například helma, boty a kalhoty, najdete v sousedních kategoriích. Tady se zaměřujeme na zvíře a stáj.</p>'
          + T(['Skupina', 'Příklady', 'Na co myslet'], [
              ['Deky', 'výběhové, stájové, odpotní, letní', 'velikost, gramáž, nepromokavost'],
              ['Ohlávky a vedení', 'ohlávky, vodítka, uzdečky, otěže', 'materiál, nastavitelnost, bezpečnost'],
              ['Udidla a doplňky', 'udidla, gumové kroužky, ochrana', 'typ, šířka, údržba'],
              ['Čabraky a sedlové podložky', 'čabraky, gely, podložky', 'tvar, rozměr, prodyšnost'],
              ['Ošetřování', 'kartáče, hřebelce, šampony, kondicionéry', 'typ srsti, citlivá kůže'],
              ['Kopyta a nohy', 'mast na kopyta, šlachovky, bandáže', 'pravidelná kontrola, správná velikost'],
              ['Krmení a doplňky', 'solné lizy, doplňkové krmivo', 'složení, poradit se s veterinářem']]) +
          '<h2>Deky: jak vybrat správnou velikost</h2>'
          '<p>Deka se vybírá podle délky koně od hrudníku po kořen ocasu, nikoli podle jeho výšky v kohoutku. Změřte pásmem vzdálenost od středu hrudníku po zadní hranu hýždí a výsledek porovnejte s tabulkou výrobce. Velikost se udává v centimetrech nebo ve stopách, takže pozor na převod. Příliš velká deka sjíždí a může způsobit odřeniny nebo zamotání, příliš malá tlačí v kohoutku a omezuje pohyb.</p>'
          '<h3>Typy dek</h3>'
          '<p>Výběhová deka je nepromokavá a zpravidla odolná proti roztržení. Její teplo určuje gramáž výplně, od nuly pro deštivé letní dny po stovky gramů pro mrazy. Stájová deka je prodyšnější a lehčí, určená do boxu. Odpotní deka odvádí vlhkost po práci, takže kůň neprochladne. Letní deka chrání před hmyzem a prachem. Pro koně s dlouhou nebo oholenou srstí volíme jiný druh než pro ty s hustou zimní srstí.</p>'
          '<p>Při výběru sledujte popruhy, zapínání a skladbu švů. Křížové popruhy pod břichem zlepšují držení, ale musí se správně nastavit. Kvalitní model vydrží při pohybu na místě a nemění polohu. Pravidelně kontrolujte pod dekou kůži, zda není odřená nebo mokrá.</p>'
          '<h2>Ohlávky, uzdečky a otěže</h2>'
          '<p>Ohlávka slouží k vedení koně ze stáje, při ošetřování a převozu. Nejčastěji je z nylonu nebo kůže. Nylon je levný a snadno se čistí, kůže je příjemná na dotek a při správné péči dlouho vydrží, jen ji je třeba čas od času ošetřit a nenechat vysychat. Bezpečnost při vyvázání koně zajišťují k tomu určené ohlávky a uvazovací pomůcky, ne slabé místo v materiálu. Správná velikost sedí tak, aby se pod nosním řemínkem vešly dva prsty.</p>'
          '<p>Uzdečka je součást vybavení pro práci pod sedlem. Obsahuje nánosník, podbradník, lícnice a otěže. Kombinace s udidlem nebo bez něj závisí na výcviku koně a jezdcově ruce. Udidla se liší materiálem a tvarem, proto je dobré se poradit s trenérem nebo zkušeným jezdcem. Gumové kroužky u udidla chrání koutky tlamy, ale i ty se opotřebovávají.</p>'
          '<h2>Čabraky a podložky pod sedlo</h2>'
          '<p>Čabrak chrání hřbet před třením a sedlo před potem. Nemá nahradit správně sedící sedlo. Bavlněné čabraky dobře nasávají pot, funkční z umělých materiálů schnou rychleji. Gelové nebo pěnové podložky pomáhají rozložit tlak, ale špatně padnoucí sedlo nezachrání. Pravidelně čabrak perte, protože zbytky potu a prachu dráždí kůži.</p>'
          '<h2>Péče o srst, kůži a kopyta</h2>'
          '<p>Základní sada na hřebelcování obsahuje hřebelec, tvrdý kartáč, měkký kartáč, kopytní škrabku a hřeben na hřívu. Šampony a kondicionéry slouží pro mytí a lesk srsti, ale nepoužívejte je příliš často, aby se kůže nevysušovala. Pro citlivé koně vybírejte jemné přípravky bez agresivních parfémů. Pro skladování praktické tašky pomáhají udržet pořádek.</p>'
          '<p>Kopyta vyžadují každodenní kontrolu. Vyčistěte je škrabkou a zkontrolujte podkovu, zápach či trhliny. Mast na kopyta se používá podle potřeby, zvlášť v obdobích sucha nebo nadměrné vlhkosti, ale nenahrazuje práci kováře. Veterinářem doporučený postup je nejlepší reakcí na jakoukoli změnu stavu kopyt.</p>'
          '<h2>Ochrana nohou: šlachovky a bandáže</h2>'
          '<p>Šlachovky a bandáže chrání šlachy a klouby při práci. Musí správně sedět, nesmí být příliš utažené ani příliš volné. Po tréninku se mají sundat a vyčistit, protože zachycený písek a pot dráždí kůži. Zda je pro vašeho koně vhodná určitá ochrana, určí trenér nebo veterinář, protože se liší podle disciplíny, terénu a stavby končetin.</p>'
          '<h2>Krmné doplňky a lizy</h2>'
          '<p>Solný liz je jednoduchý doplněk, který kůň využívá podle potřeby. Existují lizy přírodní, minerální nebo ochucené. Doplňková krmiva obsahují vitaminy, minerály, bylinky nebo další látky. Doplňky nenahrazují krmnou dávku a nelze od nich čekat zdravotní účinky: jaké doplňky kůň potřebuje, rozhoduje dávka stravy, věk a zátěž. Před zařazením jakéhokoli přípravku do krmné dávky se poraďte s veterinářem nebo odborníkem na výživu koní. Kvalitní seno a voda zůstávají základem.</p>'
          '<h2>Podle ročního období</h2>'
          '<ul><li>Jaro: kartáče na línání, lehká deka a příprava na venkovní sezonu.</li>'
          '<li>Léto: letní deka, ochrana před hmyzem, přístup ke stínu a vodě.</li>'
          '<li>Podzim: výběhová deka s lehčí výplní, kontrola nepromokavosti.</li>'
          '<li>Zima: silnější deky, ochrana kopyt před blátem a ledem, čištění po každém výběhu.</li></ul>'
          '<h2>Pro koho které vybavení</h2>'
          '<p>Začínající majitelé vystačí se základní ohlávkou, vodítkem, hřebelcem a kopytní škrabkou. Rekreační jezdci doplní uzdečku, čabrak a ochranu nohou. Sportovní jezdci řeší specializované vybavení pro disciplínu. Majitelé starších koní kladou větší důraz na teplo, deky a ošetřování. Pro děti a poníky se vyplatí vybavení odpovídající menší velikosti. Pokud potřebujete vybavení pro sebe, podívejte se na <a href="/jezdecke-obleceni/">jezdecké oblečení</a>, <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a> a <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<p>Nejčastější chybou je zakoupení deky podle výšky koně, ne délky. Další je zanedbání pravidelné kontroly pod dekou. Dále se objevuje použití příliš těsné ohlávky, špatná velikost šlachovek a výběr přípravků jen podle ceny a obalu. Konečně doplňková krmiva se nemají podávat bez konzultace, aby nedošlo k překrmení.</p>'
          '<h2>Nákup na Sportece</h2>'
          '<p>Při porovnání nabídek se zaměřte na velikost, materiál, gramáž a značku. Zkontrolujte, zda je položka skladem a jaké jsou podmínky vrácení u vybraného obchodu. U přípravků a doplňků si přečtěte složení a návod výrobce. Značky jako Fouganza, Waldhausen nebo Horseware Ireland najdete přehledně na jednom místě a vyberete nabídku, která vyhovuje vašemu koni i rozpočtu.</p>',
    faq=[
        ('Jak změřit koně na deku?', 'Změřte pásmem vzdálenost od středu hrudníku po zadní hranu hýždí. Hodnotu porovnejte s tabulkou výrobce. Výška v kohoutku k výběru nestačí.'),
        ('Jakou gramáž deky zvolit?', 'Záleží na počasí, srsti a tom, zda kůň přespává venku. Nulová gramáž slouží jako nepromokavá vrstva, vyšší gramáže hřejí. Sledujte, zda se kůň nepotí ani netřese.'),
        ('Jak poznám správnou velikost ohlávky?', 'Ohlávka má sedět tak, aby pod nosním řemínkem prošly dva prsty a nezatínala. Příliš volná se zachytí, příliš těsná tlačí.'),
        ('Jak často čistit kopyta?', 'Ideálně před i po jízdě a po výběhu. Kontrola odhalí kameny, bahno a změny v kopytě. S dlouhodobými problémy se obraťte na kováře nebo veterináře.'),
        ('K čemu je solný liz?', 'Je to doplněk, který si kůň podle potřeby olizuje. Nenahrazuje vyváženou krmnou dávku. Dávkování a výběr konzultujte s veterinářem.'),
        ('Mám pod dekou kontrolovat kůži?', 'Ano, pravidelně. Sledujte odřeniny, vlhkost a známky pocení. Deku podle potřeby sundejte a nechte srst vyschnout.'),
        ('Jak často prát čabrak?', 'Dle intenzity používání, ideálně po každém několikátém použití. Zbytky potu a prachu dráždí kůži a snižují komfort.'),
        ('Potřebuje můj kůň šlachovky?', 'Záleží na disciplíně, terénu a stavbě končetin. Rozhodnutí je lepší probrat s trenérem nebo veterinářem, špatné použití může škodit.'),
        ('Jaký je rozdíl mezi výběhovou a stájovou dekou?', 'Výběhová je odolná a nepromokavá, stájová lehčí a prodyšná. Obě slouží k odlišnému prostředí a nejsou vždy zaměnitelné.'),
        ('Jak vybrat šampon pro koně?', 'Podle typu srsti a kůže. Pro citlivé koně volte jemné přípravky bez agresivních parfémů a po mytí důkladně opláchněte.'),
    ])


# ------------------------------------------------------------------ doplnění (rozšíření sekcí)
NEW['nafukovaci-hracky']['guide'] += (
    '<h2>Praktické rady na cesty a na pláž</h2>'
    '<p>Před odjezdem hračku nafoukněte doma na zkoušku, ať víte, že ventil těsní a nic neuniká. Na pláži nafukujte až na místě, protože plně nafouknutý ostrůvek se do kufru nevejde a ve vyhřátém autě se vzduch roztahuje. Pro přepravu skládejte kus od protilehlého konce k ventilu, aby vzduch vycházel celou plochou. S sebou berte i krátké lano nebo kotvu, pokud chcete vodní lehátko připoutat u břehu.</p>')
NEW['svihadla']['intro'] += '<p>Vybírejte podle cíle: zahřátí, kondice, box, crossfit nebo hra s dětmi.</p>'
NEW['svihadla']['guide'] += (
    '<h2>Jednoduchý plán pro začátečníka</h2>'
    '<p>První týden zkuste skákat třikrát, vždy jen pár minut v krátkých sériích s pauzou na zklidnění dechu. Soustřeďte se na rovnou postavu, lehké došlapy na přední část chodidla a rytmus, který si udržíte bez předklánění. Ve druhém týdnu série prodlužte a zařaďte jednoduchou obměnu, třeba skok z nohy na nohu. Ve třetím týdnu přidejte střídání tempa, například půl minuty rychle a půl minuty pomalu. Pokud se objeví bolest v lýtkách nebo nártech, zkraťte sérii a nechte nohám čas na zotavení.</p>'
    '<h2>Švihadlo v kruhovém tréninku</h2>'
    '<p>Skákání dobře doplňuje silové stanice. Můžete ho střídat s kliky, výpady, dřepy nebo cviky s kettlebellem a krátkými pauzami složit kruh, který zabere čtvrt hodiny. Pro zahřátí se hodí i kratší blok před posilováním, protože zvedne tep a připraví kotníky a lýtka. Po skončení zařaďte protažení lýtek, stehen a ramen. Kdo trénuje venku, měl by počítat s tím, že vítr lano zpomaluje a mokrá tráva zhoršuje oporu.</p>'
    '<h2>Cestování a skladnost</h2>'
    '<p>Hlavní výhodou švihadla je, že zabírá méně místa než jakákoli jiná pomůcka. Lanko se dá svinout do kapsy batohu nebo sportovní tašky, viz <a href="/sportovni-tasky/">sportovní tašky</a>. Při cestování ocení zejména ti, kdo hledají rychlý trénink v hotelu nebo na služební cestě. Zvolte pak lehký model s rukojeťmi, které se nezkroutí, a kus lana s náhradními koncovkami.</p>')
NEW['kettlebelly']['intro'] += '<p>Vybírejte podle hmotnosti, materiálu a toho, kde a jak budete cvičit.</p>'
NEW['kettlebelly']['guide'] += (
    '<h2>Ukázkový tréninkový týden</h2>'
    '<p>Začátečník může cvičit třikrát týdně po dvaceti až třiceti minutách. První den se zaměřte na goblet dřepy, kliky a přitahování, druhý den na švihy a výpady, třetí den na turecké vstávání a nošení v ruce. Mezi sériemi odpočívejte tak dlouho, abyste nezačali ztrácet techniku. Po několika týdnech přidejte sérii, zkraťte pauzy nebo zvyšte hmotnost, nikdy ne všechno najednou. Jeden den volna mezi tréninky pomáhá regeneraci a snižuje riziko přetížení zad i zápěstí.</p>'
    '<h2>Úchop, magnézium a mozoly</h2>'
    '<p>Při opakovaných švizích se může na dlaních objevit mozol, zejména pokud je madlo hrubé. Pomůže pravidelné ošetření kůže, krátké nehty a případně rukavice nebo křída pro lepší držení. Zápěstí by mělo zůstat rovné a madlo leží uvnitř dlaně šikmo, ne v prstech. Pokud cítíte bolest v loktech nebo zápěstích, snižte zátěž a přeneste pozornost na techniku. U vlhkých dlaní pomáhá suchý ručník poblíž činky.</p>'
    '<h2>Uložení a přeprava</h2>'
    '<p>Kettlebell patří do stojanu nebo na rovnou podlahu, ne na polici nad hlavou. Při přenášení v autě jej zajistěte proti převrácení, nejlépe v kufru mezi pevnými předměty. Těžší kusy držte oběma rukama v dřepu, ne předklonem. Pro více činek se vyplatí stojan nebo police v nízké výšce, aby se zvedání nestalo rizikem. Pokud bydlíte v paneláku, nepokládejte kettlebell na křehkou podlahu a pod stojan dejte pogumovanou desku.</p>'
    '<h2>Kombinace s dalšími pomůckami</h2>'
    '<p>Kettlebell se skvěle doplňuje se <a href="/svihadla/">švihadlem</a> pro kondici, s <a href="/joga-a-pilates/">jógou a pilates</a> pro mobilitu a s <a href="/gymnasticke-pomucky/">gymnastickými pomůckami</a> pro stabilitu trupu. Pro regeneraci po tréninku se hodí <a href="/masazni-pomucky/">masážní pomůcky</a> a <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> pro ochranu zápěstí.</p>')
NEW['vybaveni-pro-kone']['intro'] += '<p>Tabulky a rady níže pomáhají s výběrem podle koně, sezony a způsobu práce.</p>'
NEW['vybaveni-pro-kone']['guide'] += (
    '<h2>Základní výbava do stáje a na vyjížďku</h2>'
    '<p>Pokud kůň teprve přichází do nové stáje, pořiďte nejdřív ohlávku, vodítko, hřebelec, kartáče, kopytní škrabku a deku odpovídající ročnímu období. K tomu přidejte vlastní kyblík na vodu a krmítko, aby nebylo třeba půjčovat. Pro vyjížďky se hodí uzdečka, čabrak, vhodné sedlo a lehká taška na drobnosti. Do výbavy patří také lékárnička pro koně, kterou doporučí veterinář a která obsahuje obvazový materiál a dezinfekci.</p>'
    '<h2>Kontrola vybavení před použitím</h2>'
    '<p>Před každým použitím zkontrolujte popruhy, přezky a švy. Kůže by neměla být popraskaná, nylon roztřepený a kov zrezivělý. Nezapomeňte na zapínání dek, které se při hře koní často trhá. Poškozený kus raději vyřaďte, než abyste riskovali zranění zvířete nebo vlastní. Pravidelné čištění a ošetření kůže prodlouží životnost uzdečky a otěží a uvolněné šrouby je třeba dotáhnout.</p>'
    '<h2>Mytí a sušení dek</h2>'
    '<p>Deky se perou podle návodu výrobce, často ve velké pračce nebo ve specializované prádelně. Nepromokavé vrstvy a nepromokavé impregnace časem slábnou, takže je lze obnovit přípravkem na impregnaci. Před uložením deku úplně vysušte, jinak vzniká plíseň a zápach. Přes léto ji skladujte v prodyšném obalu na suchém a tmavém místě.</p>'
    '<h2>Doprava a výcvik</h2>'
    '<p>Při převozu koně se používají chrániče, přepravní deka a pevná ohlávka. Pokud jezdíte na závody nebo vyjížďky, myslete na příslušenství pro dopravu. Více o vlastním výcviku a oblečení pro jezdce najdete v kategoriích <a href="/jezdectvi/">jezdectví</a> a <a href="/jezdecke-obleceni/">jezdecké oblečení</a>.</p>')

# ------------------------------------------------------------------ doplnění 2
NEW['svihadla']['intro'] += '<p>Přehled pomáhá najít lano pro začátečníka i pokročilého.</p>'
NEW['svihadla']['guide'] += (
    '<h2>Švihadlo a děti</h2>'
    '<p>Pro děti je skákání přirozená hra a zároveň trénink rytmu. Malým dětem stačí lehké lano s měkkými rukojeťmi a kratší délkou. Školáci mohou skákat ve dvojicích, přes dlouhé lano nebo po jednom. Dohlédněte na rovný povrch bez překážek a vhodnou obuv. Společné skákání se dá změnit v soutěž o nejdelší sérii nebo nejrychlejší střídání nohou, což děti motivuje bez nutnosti číst návody. Starší děti si mohou zkusit základní triky a postupně přejít na rychlejší model.</p>'
    '<h2>Kdy lano vyměnit</h2>'
    '<p>Pokud se plášť rozedře až k jádru, lanko zůstává zkroucené nebo ručky vůbec neotáčí lano, je čas na výměnu. U rychlostních kabelů lze často vyměnit jen samotné lanko. Kožená a bavlněná lana se opotřebují nerovnoměrně, takže si jich všimnete podle hrbolů a rozstřapených konců. Nenechávejte použité lano s praskajícím jádrem, protože může při skoku vymrštit zlomek kabelu.</p>'
    '<h2>Na co se zaměřit při porovnání cen a nabídek</h2>'
    '<p>Dva podobné produkty se někdy liší jen drobnostmi: délkou dodaného lana, přibalenými náhradními koncovkami nebo kvalitou ložisek. Zjistěte, zda je součástí balení pouzdro a návod. Prohlédněte si fotografii rukojeti, protože tvar vám řekne, jak dobře padne do dlaně. Značku nechte být jedním z kritérií, nikoli jediným.</p>')
NEW['kettlebelly']['guide'] += (
    '<h2>Kettlebell a běžné bolesti zad</h2>'
    '<p>Mnoho lidí sahá po kettlebellu, aby si posílili záda, ale technika pohybu je klíčová. Švih, při kterém se zaoblí záda, přetěžuje bederní páteř a může ublížit. Pokud už máte potíže se zády, proberte trénink nejdříve s fyzioterapeutem. Za bezpečné se považuje začít se cviky, které učí správný předklon v kyčlích (hip hinge) bez zátěže, a teprve potom přidat činku. Zrcadlo nebo záznam na telefonu pomohou odhalit chyby, které sami nevnímáte.</p>'
    '<h2>Kettlebell pro seniory a po delší pauze</h2>'
    '<p>Kdo se vrací ke cvičení po delší pauze nebo začíná v pozdějším věku, ocení měkké modely a nižší hmotnosti. Jednoduché cviky, jako goblet dřep nebo přenášení činky při chůzi, rozvíjejí sílu a stabilitu bez složitých pohybů. Důležitá je pomalost, kontrola dechu a dostatek času na odpočinek. Před zahájením pravidelného cvičení je vhodné zvážit lékařskou kontrolu, zvláště pokud užíváte léky nebo máte kardiologické potíže.</p>'
    '<h2>Jak číst popis produktu</h2>'
    '<p>V popisu hledejte hmotnost, materiál, rozměr dna a průměr madla. U poplastovaných modelů zkontrolujte, zda plast nepraská ani neloupe. U nastavitelných kusů ověřte rozsah hmotnosti a způsob zajištění. Pokud popis chybí, porovnejte jej s jiným obchodem. Rozdíl v hmotnosti několika set gramů je běžný a nemá vliv na výsledek tréninku.</p>')
NEW['vybaveni-pro-kone']['guide'] += (
    '<h2>Ošetření kůže a srsti v různých obdobích</h2>'
    '<p>V období línání pomáhá pravidelné hřebelcování, které odstraňuje uvolněnou srst a podporuje prokrvení kůže. V zimě se srst nechává delší a hřebelcujte jemněji, aby kůň neztrácel přirozenou izolaci. Po jízdě v potu ho osušte nebo přikryjte odpotní dekou, než se zcela zklidní. V létě chraňte kůži před hmyzem a slunečním zářením, zejména u koní s růžovou kůží kolem nozder a očí. Pokud se objeví změna srsti, parazité nebo kožní problémy, kontaktujte veterináře.</p>'
    '<h2>Poníci a malí jezdci</h2>'
    '<p>Pro poníky platí stejná pravidla jako pro koně, jen rozměry jsou menší. Deka, uzdečka i ohlávka musí odpovídat velikosti, jinak vybavení nesedí a zvíře obtěžuje. Děti často rostou rychleji než poník, a proto se hodí nastavitelné popruhy a výbava, která vydrží několik sezon. Pro děti je důležité, aby jim vybavení nebránilo v pohybu a bylo bezpečné. Dohled zkušeného dospělého je při práci s koněm na prvním místě.</p>'
    '<h2>Kde vybavení skladovat</h2>'
    '<p>Deky, čabraky a kožené součásti skladujte v suché skříni nebo boxu a chraňte je před hlodavci. Nenechávejte kůži u radiátoru, vysychá a praská. Kartáče a hřebelce vyplachujte a sušte, nebo je odkládejte na polici čepelí nahoru. Takto zůstane výbava použitelná déle a stáj je přehlednější.</p>')
