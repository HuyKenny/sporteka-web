"""sporteka.cz — facet landing texts wave 187: reima-cepice, lacoste-teplaky, puma-leginy, columbia-vesta.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ reima-cepice
NEW['reima-cepice'] = dict(
    title='Reima čepice: dětské zimní čepice, kšiltovky a beanie',
    desc='Reima čepice pro děti: zimní čepice, přechodové beanie, kšiltovky a oboustranné klobouky. Jak zvolit obvod hlavy, podšívku a sezónu a porovnat obchody.',
    intro='<p>Reima je finská značka dětského oblečení a v nabídce <a href="/cepice-a-celenky/">čepic, kšiltovek a čelenek</a> je skoro výhradně dětskou záležitostí. Najdete tu zimní čepice s podšívkou, tenčí přechodové modely na jaro a podzim, kšiltovky na slunce i oboustranné klobouky, které se hodí do školky a na hřiště. '
          'Tato stránka porovnává nabídky obchodů u celé řady Reima a vysvětluje, v čem se jednotlivé typy liší, jak poznat správný obvod hlavy u rostoucího dítěte a proč se vyplatí kupovat čepici před sezónou, ne uprostřed mrazů. '
          'Průvodce dále ukazuje, na co se dívat u uší, zapínání pod bradou a podšívky, jak čepici prát a čím se Reima liší od sportovních značek jako <a href="/cepice-nike/">Nike</a> nebo <a href="/adidas-cepice/">Adidas</a>.</p>',
    guide='<h2>Reima v kategorii čepic: pro koho je určena</h2>'
          '<p>Reima je finská firma, která se soustředí na oblečení pro děti od miminek po školáky a na venkovní hraní v nepříznivém počasí. Čepice tu proto nejsou módním doplňkem v prvé řadě, ale součástí celé vrstvy: stejné názvy modelů se opakují u kombinéz, bund a rukavic, takže si dítě lze obléknout do sladěné sady. Na této stránce proto nehledejte dospělé velikosti. Pokud potřebujete čepici pro sebe, projděte spíš <a href="/znacka/reima/">všechny produkty značky</a> pro přehled velikostí nebo širší nabídku v hlavní kategorii.</p>'
          '<p>Z názvů nabídek je vidět, že se prodávají čtyři základní druhy: zimní čepice, lehčí čepice na přechodné období, kšiltovky a oboustranné klobouky. Každý z nich řeší jiný problém, a tak jejich výběr závisí hlavně na teplotě, větru a na tom, jak dlouho dítě venku zůstane.</p>'
          + T(['Typ', 'Kdy se nosí', 'Na co se zaměřit'], [
              ['Zimní čepice s podšívkou', 'mráz, sníh, sáňkování, lyžování', 'zakrytí uší, měkká podšívka, zapínání pod bradou u malých dětí'],
              ['Přechodová čepice (jaro, podzim)', 'chladné ráno, vítr, déšť', 'tenčí pletení nebo úplet, lehká podšívka, aby se dítě nepotilo'],
              ['Beanie bez podšívky', 'školka, škola, krátké cesty', 'měkký materiál, šev, který netlačí na čele'],
              ['Kšiltovka', 'léto, výlety, sluneční dny', 'kšilt zakrývající oči, nastavitelný pásek, prodyšnost'],
              ['Oboustranný klobouk', 'léto, hřiště, voda a písek', 'široká krempa, snadné praní, dvě barevné strany'],
              ['Čepice pod helmu', 'lyže, bobová dráha, kolo', 'tenký střih, který netlačí pod pásky helmy']]) +
          '<p>Když si nejste jistí, začněte podle ročního období. Zima znamená podšívku a zakryté uši, jaro a podzim lehkou čepici, léto kšiltovku nebo klobouk. Dalším krokem je velikost.</p>'
          '<h2>Jak změřit hlavu dítěte a nespoléhat jen na věk</h2>'
          '<p>Dětské čepice se u většiny značek označují podle obvodu hlavy v centimetrech, nikoli podle věku, protože hlavy stejně starých dětí se liší. Změřte krejčovským metrem obvod kolem čela, těsně nad obočím a ušima, kde čepice sedí. Pokud nemáte metr, použijte tkaničku a pak ji přiložte k pravítku. Výsledek porovnejte s tabulkou v nabídce a raději volte nejbližší vyšší rozmezí.</p>'
          + T(['Věk (orientačně)', 'Obvod hlavy', 'Poznámka'], [
              ['Batole, 1–2 roky', 'zhruba 46–49 cm', 'hlava roste rychle, měřte před každou sezónou'],
              ['Předškolák, 3–4 roky', 'zhruba 48–51 cm', 'beanie i klobouk se dají doladit širším pletením'],
              ['Mladší školák, 5–7 let', 'zhruba 50–53 cm', 'zimní čepice s manžetou pak lze nosit dva roky'],
              ['Starší školák, 8–10 let', 'zhruba 52–55 cm', 'už se hodí i velikosti pro dospělé s menším obvodem'],
              ['Dospívající', 'zhruba 54–57 cm', 'mnoho dětských modelů už nestačí']]) +
          '<p>Hodnoty jsou jen orientační a individuální rozdíly bývají velké. Důležitější než číslo je dojem při nasazení: čepice se nesmí zařezávat do čela a zároveň nesmí vyklouznout při záklonu hlavy. Malé děti potřebují zavazování nebo pružnou pásku, která drží pod bradou. Starším dětem stačí přiléhavé pletení, které samo drží na hlavě.</p>'
          '<h2>Teplo, podšívka a vítr</h2>'
          '<p>Rozhodující vlastností zimní čepice není tloušťka vlny, ale to, zda chrání uši a zadní část hlavy a zároveň neprofukuje. Podšívka z fleecového nebo jemného úpletu zadrží vzduch u hlavy. Vnější vrstva z pleteniny sama o sobě vítr propouští, proto u nejmrazivějších dnů hledejte čepice s větruodolnou vložkou nebo dvouvrstvé provedení. Při chůzi do školky stačí jedna vrstva, při dlouhém pobytu na svahu dvě.</p>'
          '<ul><li><strong>Zakryté uši:</strong> přes uši musí být látka dvojitá, jinak mrznou jako první.</li>'
          '<li><strong>Vlna, nebo syntetika:</strong> vlna hřeje i vlhká a nepáchne, syntetika rychleji schne a snadněji se pere.</li>'
          '<li><strong>Měkký šev:</strong> citlivé děti odmítají čepici, která škrábe na čele; vyzkoušejte ji na zápěstí i na čele.</li>'
          '<li><strong>Zapínání:</strong> pásek nebo tkanička pod bradou zabrání ztrátě na lanovce i při běhání.</li>'
          '<li><strong>Reflexní prvek:</strong> zlepšuje viditelnost při ranních cestách v tmavých měsících.</li></ul>'
          '<p>Pod helmu volte tenkou verzi bez bambule. Pro ukrytí krku se hodí <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a> nebo samostatné <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>, rukavice najdete v kategorii <a href="/lyzarske-rukavice/">lyžařské rukavice</a>.</p>'
          '<h2>Kšiltovky a klobouky pro léto</h2>'
          '<p>V nabídce Reima se objevují i kšiltovky a oboustranné klobouky, které dětem poslouží jako ochrana před sluncem. Kšilt nebo krempa zastíní oči a čelo, kde se kůže spálí nejdřív. Oboustranný klobouk se dá navléknout lícem i rubem, takže dítě má dvě barvy v jedné a rodič snadno poznat špinavou stranu. Kšiltovka s nastavitelným páskem vydrží víc let, pokud ji dítě nevyroste hned.</p>'
          '<p>Při výběru sledujte prodyšnost a hmotnost: lehká látka se rychle suší a nepřehřívá, těžká bavlna je příjemná, ale v horku se potí. Klobouk s tkaničkou pod bradou se hodí k vodě, zatímco kšiltovka na hřiště. Pro slunné dny nezapomeňte, že čepice nenahradí krém na obličej.</p>'
          '<h2>Jak porovnat nabídky stejné čepice</h2>'
          '<p>Stejný model se prodává v mnoha barvách a velikostech a každý obchod má skladem něco jiného. Před objednávkou proto zkontrolujte tři věci: obvod hlavy, ročník kolekce a rozdíl v doručení. Barva se může lišit i u položek s totožným názvem. V seznamu nabídek vidíte všechny obchody, takže poznáte, kde je ještě dostupná velikost, kterou potřebujete.</p>'
          '<p>Pokud vybíráte dárek, zvažte kombinaci čepice a rukavic stejného modelu. Při rostoucí hlavě je praktické kupovat v říjnu nebo listopadu, kdy je skladem nejširší výběr velikostí. Slevové akce na zimní čepice bývají na jaře, ale pak už chybí nejobvyklejší čísla.</p>'
          '<h2>Péče o dětské čepice</h2>'
          '<ol><li>Přečtěte si štítek: vlněné čepice většinou snesou jemné praní na nízké teplotě.</li>'
          '<li>Perte je v sáčku na prádlo, aby se nezachytily o zip nebo suchý zip.</li>'
          '<li>Nesušte je na radiátoru ani v sušičce, mohou se srazit a deformovat.</li>'
          '<li>Sušte je rozložené naplocho a před uložením úplně vyschlé.</li>'
          '<li>Mokrou čepici po hře vždy vyměňte za suchou, jinak dítěti rychle prochladne hlava.</li></ol>'
          '<h2>Reima, nebo sportovní značky?</h2>'
          '<p>Sportovní značky jako <a href="/cepice-nike/">Nike</a>, <a href="/puma-cepice/">Puma</a> nebo <a href="/the-north-face-cepice/">The North Face</a> cílí hlavně na dospělé a teenagery a nabízejí vzor s logem. Reima se naopak zaměřuje na malé děti a funkční vrstvu do chladného a vlhkého počasí. Pokud hledáte fanouškovskou kšiltovku, podívejte se na <a href="/new-era-ksiltovka/">kšiltovky New Era</a>. Pokud potřebujete dětskou zimní čepici s podšívkou a zapínáním, je Reima logická první volba.</p>',
    faq=[
        ('Pro jaký věk jsou čepice Reima?', 'Nabídka je zaměřená na děti od batolat po školáky. Přesný věk není rozhodující, počítá se obvod hlavy v centimetrech. Při koupi si ověřte rozmezí uvedené u konkrétního modelu a raději vybírejte nejbližší vyšší velikost, protože dětská hlava rychle roste.'),
        ('Jak změřit obvod hlavy dítěte?', 'Obtočte krejčovský metr kolem čela těsně nad obočím a ušima, tedy tam, kde čepice sedí. Metr nesmí škrtit ani viset. Pokud dítě nevydrží klidně stát, použijte tkaničku a změřte ji pravítkem. Údaj porovnejte s tabulkou výrobce.'),
        ('Je zimní čepice s podšívkou lepší než jednovrstvá?', 'Pro mráz a vítr ano, protože podšívka zadrží vzduch a chrání uši. Při krátké cestě do školky v mírném chladu stačí jednovrstvá beanie. Dítě, které se hodně pohybuje, se ve dvouvrstvé čepici může zpotit, proto ji lze střídat podle teploty.'),
        ('Má čepice sedět pevně, nebo volněji?', 'Přiléhavě, ale bez tlaku na čelo. Měla by zakrývat uši a při zakloněné hlavě neslézt. Příliš volná čepice sklouzává do očí, příliš těsná nechává otisk a dítě ji odmítne nosit.'),
        ('Čím se liší kšiltovka od oboustranného klobouku?', 'Kšiltovka chrání jen přední část obličeje, zato je lehká a snadno se přizpůsobí páskem. Klobouk má krempu dokola, takže stíní i uši a krk, a bývá oboustranný. Na výlety do slunce se lépe hodí klobouk, na hřiště kšiltovka.'),
        ('Jak čepici prát, aby se nesrazila?', 'Dodržujte pokyny na štítku. Obecně pomáhá nízká teplota, jemný prostředek, sáček na prádlo a žádné ždímání. Sušte ji naplocho při pokojové teplotě. Radiátor ani sušička čepici nesvědčí, vlna se může srazit.'),
        ('Kdy je nejlepší čas na nákup zimní čepice?', 'Na začátku podzimu, kdy mají obchody skladem nejširší řadu velikostí a barev. Slevy přicházejí až v zimě a na jaře, ale tehdy často chybí obvyklé velikosti. U dětí, které rostou, se vyplatí koupit přesně na sezónu.'),
        ('Hodí se Reima čepice i pro dospělé?', 'Většina nabídky je dětská a velikosti končí u starších školáků. Dospělí s menším obvodem hlavy mohou některé modely nosit, ale odpovídající střih najdete spíš u značek, které dospělé velikosti vyrábějí přímo. Zkontrolujte rozmezí obvodu hlavy.'),
        ('Dá se čepice nosit pod helmu?', 'Ano, pokud je tenká a bez bambule nebo širokého lemu. Silné pletení netěsní pod pásky a tlačí. Při lyžování je dobré čepici vyzkoušet přímo s helmou, aby se dítě necítilo stísněně a helma seděla správně.'),
        ('Proč se stejný model prodává v různých barvách a cenách?', 'Obchody mají různé zásoby a barvy se rozprodávají nerovnoměrně. Starší kolekce se často nabízí levněji než čerstvé. Konkrétní rozdíl poznáte v přehledu nabídek u daného modelu, kde si vedle sebe porovnáte dostupné velikosti.'),
    ])

# ------------------------------------------------------------------ lacoste-teplaky
NEW['lacoste-teplaky'] = dict(
    title='Lacoste tepláky: pánské, dámské a dětské s bavlnou',
    desc='Lacoste tepláky a teplákové šortky: pánské, dámské i dětské, většinou s bavlnou a vyšitým krokodýlem. Jak vybrat střih, velikost a porovnat obchody.',
    intro='<p>Lacoste vzniklo kolem tenisty Reného Lacosta a dodnes si drží sportovní eleganci, takže jeho tepláky vypadají jinak než funkční kalhoty na trénink. Většinou jde o bavlněné nebo bavlnou směsované kousky s vyšitým krokodýlem, jednoduchým střihem a decentními barvami. '
          'Stránka sbírá nabídky <a href="/teplaky/">tepláků</a> této značky: pánské, dámské i dětské, dlouhé kalhoty, teplákové šortky, kompletní soupravy a několik kolekcí spojených s tenisovými turnaji. '
          'Průvodce vysvětluje, jak se Lacoste liší od sportovnějších značek, jak vybrat střih a velikost, co dělá bavlněná teplákovina dobře i špatně, jak ji prát a kdy se hodí šortky místo dlouhých kalhot.</p>',
    guide='<h2>Co dělá Lacoste tepláky jiné</h2>'
          '<p>Značka Lacoste je spojená s tenisem a s polo košilemi. Její tepláky z toho vycházejí: nejsou stavěné na maximální odvod potu ani na kompresi, ale na každodenní nošení a elegantní vzhled. Typický kus má jednobarevnou plochu, malé vyšité logo, pevný pas a manžety, které drží tvar. Logo je obvykle drobné, takže teplákovina působí nenápadně a lze ji kombinovat s košilí, polo tričkem nebo mikinou. Pokud hledáte výrazné velké logo, hodí se spíš výběr <a href="/nike-teplaky/">Nike</a> nebo <a href="/adidas-teplaky/">Adidas</a>.</p>'
          '<p>Značka nabízí především teplákovinu na volný čas a lifestyle. V nabídce ale najdete i modely z kolekcí spojených s turnajem Roland-Garros a s tenistou Daniilem Medvěděvem. Tyto kusy bývají sportovněji laděné, ale pořád jsou určené pro městské nošení víc než pro intenzivní trénink.</p>'
          + T(['Druh', 'Pro koho a kdy', 'Na co se dívat'], [
              ['Dlouhé tepláky pánské', 'město, doma, cestování, tenisový klub', 'střih nohavic, manžeta nebo rovný konec, podíl bavlny'],
              ['Dlouhé tepláky dámské', 'volný čas, cesty, pohodlí do kanceláře bez dresscodu', 'výška pasu, délka nohavic, hustota bavlny'],
              ['Teplákové šortky', 'léto, dovolená, domácí cvičení', 'délka nad kolena, kapsy se zipem nebo bez'],
              ['Teplákový set (bunda a kalhoty)', 'cesty, sportovní vstup, volný čas', 'zda se dají nosit i samostatně'],
              ['Dětské tepláky', 'škola, kroužky, výlety', 'odolná kolena, pružný pas, růst dítěte']]) +
          '<h2>Bavlněná teplákovina: výhody a omezení</h2>'
          '<p>Většina nabídek označuje kalhoty jako bavlněné nebo s bavlnou. Bavlna je měkká na dotek, příjemná v chladu i v teplu a dobře drží tvar střihu. Její slabinou je pot: nasákne a pomalu schne, takže se v ní při dlouhém cvičení pozdě ochlazujete. Proto Lacoste tepláky volte na chůzi, cesty a odpočinek, na běh a posilování spíš syntetické kalhoty z kategorie <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>'
          '<ul><li><strong>Vyšší podíl bavlny:</strong> měkčí, hřejivější a lépe vypadá, ale víc se mačká a pomaleji schne.</li>'
          '<li><strong>Příměs elastanu nebo polyesteru:</strong> kus drží tvar a méně se vytahuje na kolenou.</li>'
          '<li><strong>Zvenku hladký, uvnitř počesaný:</strong> počesání hřeje, hladký úplet se hodí do teplejšího počasí.</li>'
          '<li><strong>Vyšívané logo:</strong> trvanlivější než nažehlené, nepraská ani se nelepí při praní.</li></ul>'
          '<p>Při srovnání dvou nabídek proto kontrolujte složení materiálu, ne jen fotografii. Dvojice kalhot vypadající stejně může mít jinou gramáž a podíl bavlny.</p>'
          '<h2>Střih, velikost a délka</h2>'
          '<p>Lacoste šije tepláky ve dvou hlavních variantách: klasický zúžený střih s manžetou u kotníku a rovnější kalhoty bez manžety. Manžeta se hodí ke sportovní obuvi, rovný konec spíš k tenisce nebo mokasínu. Značka má vlastní velikostní označení, které se u některých kousků liší od běžných S až XL. Vždy proto použijte tabulku v konkrétní nabídce nebo změřte vlastní kalhoty, které vám sedí, a porovnejte pas, rozkrok a délku nohavice.</p>'
          + T(['Míra', 'Jak ji změřit', 'Proč je důležitá'], [
              ['Obvod pasu', 'měřit nenatažený pas naplocho a vynásobit dvěma', 'pružný pas se přizpůsobí, ale příliš velký sjíždí'],
              ['Rozkrok', 'od rozkroku po spodní okraj nohavice', 'rozhoduje o délce a o poloze manžety'],
              ['Šířka stehna', 'napříč nohavicí těsně pod rozkrokem', 'určuje, zda je střih úzký nebo volný'],
              ['Výška pasu', 'od pasu po rozkrok', 'ovlivní, kde kalhoty sedí na břiše']]) +
          '<p>Při pochybnostech zvolte větší velikost a pas upravte šňůrkou. Bavlněná teplákovina se po prvním praní může mírně srazit, nejvíc na délku. Dámské modely mívají nižší pas a užší stehno než pánské, a proto štíhlejší muži a vyšší ženy občas sáhnou po opačné řadě. Rozdíly mezi pohlavími najdete také na stránkách <a href="/panske-teplaky/">pánské tepláky</a> a <a href="/damske-teplaky/">dámské tepláky</a>.</p>'
          '<h2>Teplákové šortky a soupravy</h2>'
          '<p>Vedle dlouhých kalhot se v nabídce hodně objevují teplákové šortky pánské i dámské. Jsou ideální na léto, na dovolenou a na doma, protože zachovají pohodlí teplákoviny bez zbytečného tepla. Měří obvykle po kolena nebo kousek nad ně, takže se nehodí k posilování, kde by se zadrhávaly. K šortkám se nosí polo tričko, tílko nebo trička z kategorie <a href="/sportovni-tricka/">sportovní trička</a>.</p>'
          '<p>Teplákový set spojuje kalhoty s mikinou nebo bundou. Nosí se jako souprava na cesty, ale rozdělené kousky se kombinují i samostatně. Při výběru zkontrolujte, zda se barvy po praní neliší, protože dvě samostatné části se mohou lišit odstínem. Podobné soupravy hledejte i v kategorii <a href="/mikiny/">mikiny</a>, kam patří horní díl.</p>'
          '<h2>Lacoste a ostatní značky tepláků</h2>'
          '<p>Rozdíl oproti sportovním značkám je v zaměření. <a href="/nike-teplaky/">Nike</a> a <a href="/adidas-teplaky/">Adidas</a> staví na výkonnostních řadách a velkých logách. <a href="/champion-teplaky/">Champion</a> nabízí klasickou americkou teplákovinu s výrazným písmem, <a href="/teplaky-tommy-hilfiger/">Tommy Hilfiger</a> preppy styl s vlajkou. Lacoste je z nich nejblíž ke klubovému tenisu: jemné logo, bavlna a čisté barvy. Pokud hledáte praktické kalhoty na intenzivní pohyb, vyberte sportovní značku, pokud elegantní teplákovinu do města, Lacoste dává smysl.</p>'
          '<h2>Jak tepláky kombinovat</h2>'
          '<ul><li><strong>S tenisky:</strong> bílé nebo světlé tenisky tvoří nejjednodušší základ, viz <a href="/tenisky/">tenisky</a>.</li>'
          '<li><strong>S mikinou:</strong> jednobarevnou mikinou stejné barvy vznikne dojem soupravy i bez setu.</li>'
          '<li><strong>S polo tričkem:</strong> střídmá varianta do města, kde tepláky nevypadají domácky.</li>'
          '<li><strong>S bundou:</strong> v zimě přidejte lehkou <a href="/sportovni-bundy/">sportovní bundu</a> a pod ni termoprádlo.</li></ul>'
          '<h2>Péče o bavlněnou teplákovinu</h2>'
          '<p>Perte tepláky obrácené na rubovou stranu na 30 stupňů, aby vyšité logo a počesaná plocha neztratily vzhled. Aviváž a ždímání vysokými otáčkami zkracují životnost, zejména u počesané vnitřní vrstvy. Sušte je rozložené nebo v sušičce na nízkou teplotu a nikdy neotáčejte vlhké kalhoty v radiátoru. Zip na kapse zapněte před praním, aby se nezachytil o ostatní prádlo. Drobné žmolky se dají odstranit strojkem.</p>'
          '<p>Při nákupu v obchodech se vyplatí ověřit, zda jde o autorizovaného prodejce, protože značkové oblečení bývá často napodobováno. Originál poznáte podle kvalitního šití, přesně vyšitého loga a štítku s údaji o složení.</p>',
    faq=[
        ('Jsou Lacoste tepláky vhodné na sport?', 'Spíš na volný čas. Většina kousků je z bavlny nebo bavlnou směsované, která pot nasaje a pomalu schne. Na chůzi, cesty a lehké cvičení stačí, na běh a intenzivní trénink se hodí spíše syntetické sportovní kalhoty. Některé modely z tenisových kolekcí jsou sportovnější.'),
        ('Jak velké jsou Lacoste tepláky oproti běžným velikostem?', 'Značka používá vlastní označení, které se u některých kousků neshoduje s klasickým S až XL. Spolehněte se na tabulku v konkrétní nabídce a porovnejte míry s kalhotami, které vám sedí. Při pochybnostech vyberte větší velikost, pas lze upravit šňůrkou.'),
        ('Srazí se bavlněné tepláky po praní?', 'Mírně ano, nejčastěji na délku. Perte je na 30 stupňů a sušte volně. Pokud je kupujete s malou rezervou, počítejte s tím, že první praní může kalhoty o něco zkrátit. Vyšší podíl elastanu nebo polyesteru srážení omezuje.'),
        ('Čím se liší pánské a dámské tepláky Lacoste?', 'Dámské mají obvykle užší stehno a o něco nižší pas, pánské jsou rovnější a delší. Rozdíl nemusí být zásadní, proto se u unisex střihů dá volit podle míry. Dětské jsou samostatná řada a mají pružný pas a odolnější kolena.'),
        ('Kdy zvolit teplákové šortky místo kalhot?', 'V létě, na dovolené a při cvičení doma. Šortky z teplákoviny jsou pohodlné a lehčí než dlouhé kalhoty. V chladu a při delších procházkách se víc hodí dlouhé tepláky s manžetou, protože chrání lýtka.'),
        ('Jak poznám originální Lacoste tepláky?', 'Zaměřte se na vyšité logo s pravidelnými stehy, štítek se složením a kvalitní šití u švů. Nejjistější cestou je nakupovat u známých obchodů. Příliš nízká cena u čerstvé kolekce je varovný signál, ověřte si prodejce.'),
        ('Dá se Lacoste teplákový set nosit po částech?', 'Ano, většina souprav se skládá z mikiny nebo bundy a kalhot, které lze kombinovat samostatně. Po praní se může odstín obou dílů mírně lišit, proto soupravu perte a sušte společně. Samostatné kousky se pak nosí s ostatním oblečením.'),
        ('Jak dlouho vydrží tepláky z bavlny?', 'Při šetrném praní několik sezón. Namáhaná jsou kolena, manžety a pas. Nešetrné praní s aviváží a vysokými otáčkami zkracuje životnost počesané vrstvy. Drobné žmolky nejsou vada materiálu a dají se sundat strojkem.'),
        ('Do čeho tepláky obléci, aby nevypadaly domácky?', 'Kombinujte je s čistými tenisky, jednobarevným polo tričkem nebo lehkou bundou. Vybírejte tmavé nebo neutrální barvy, hladký povrch a manžetu, která drží tvar. Zmačkané a vytahané kolena působí domácky nejvíc, proto kalhoty včas vyžehlete nebo vyměňte.'),
    ])

# ------------------------------------------------------------------ puma-leginy
NEW['puma-leginy'] = dict(
    title='Puma legíny: Essentials, Strong, běžecké i dívčí',
    desc='Puma legíny: Essentials s logem, tréninkové řady Strong a Evostripe, běžecké 7/8 i dívčí a dětské. Jak vybrat délku, pas a materiál a porovnat obchody.',
    intro='<p>Puma je německá sportovní značka a její <a href="/leginy/">legíny</a> pokrývají celé spektrum od bavlněných modelů na každý den po tréninkové řady na posilovnu a běh. Mezi nabídkami se opakují názvy jako Essentials, Strong, Evostripe, Favorite nebo Run Velocity a najdete tu i dívčí, dětské a několik pánských běžeckých kousků. '
          'Tato stránka ukazuje, v čem se jednotlivé řady liší, jak číst označení délky 7/8, 3/4 a capri, kdy zvolit bavlnu a kdy syntetiku a jak legíny sedí ve srovnání s modely Nike, Adidas a Under Armour. '
          'Dozvíte se také, jak vybrat dívčí velikost, jak legíny prát a jak ověřit neprůsvitnost při dřepu.</p>',
    guide='<h2>Řady Puma legín podle účelu</h2>'
          '<p>Puma neprodává jeden typ legín. Názvy v nabídce prozrazují účel, ačkoli přesné parametry se u jednotlivých modelů liší, a proto je vždy čtěte v popisu obchodu. Základní orientace vypadá takto:</p>'
          + T(['Řada podle názvu', 'Pro co je určená', 'Co čekat'], [
              ['Essentials / ESS (No. 1 Logo)', 'každý den, volný čas, lehký pohyb', 'měkčí materiál, často s podílem bavlny, výrazné logo'],
              ['Strong, Evostripe, Train', 'posilovna, funkční trénink, cross', 'pevnější úplet, vysoký pas, neprůsvitnost při dřepu'],
              ['Run Velocity, Dreamrun, Lightspeed', 'běh', 'lehčí syntetika, delší střih, někdy reflexní prvky'],
              ['Favorite, All Day', 'trénink i denní nošení', 'univerzální střih, pohodlný pas'],
              ['Shapeluxe, Seamless', 'jóga, pilates, fitness', 'bezešvé pletení, tvarování a pružnost'],
              ['Dívčí a dětské', 'škola, kroužky, tanec, hřiště', 'bavlnou směsované materiály, pružný pas']]) +
          '<p>Pokud si nejste jistí, začněte podle činnosti. Na chůzi a běžný den stačí Essentials, na běh si vyberte lehčí a delší běžecký střih, na posilovnu pevný úplet s vysokým pasem. Obecné rozdělení legín podle použití najdete v kategorii <a href="/leginy/">legíny</a>, takže zde se soustředíme na rozdíly mezi řadami Puma.</p>'
          '<h2>Délka: dlouhé, 7/8, 3/4 a capri</h2>'
          '<p>Značka nabízí legíny v několika délkách a označení se opakuje v názvech modelů. 7/8 končí nad kotníkem, takže se nezachytává o botu a nehrnou se u kotníku. 3/4 a capri jsou o něco kratší a hodí se na teplo. Krátké legíny s označením short leggings nebo Power Tape shorts sahají zhruba nad kolena a nosí se při cvičení, kdy delší nohavice vadí. Dlouhé legíny jsou nejuniverzálnější do chladu.</p>'
          '<ul><li><strong>7/8:</strong> nejpopulárnější délka pro studio, běh i den, kotník zůstává volný.</li>'
          '<li><strong>3/4 a capri:</strong> léto, jóga, tanec; pozor, aby se nesvíjely u kolen.</li>'
          '<li><strong>Short leggings:</strong> horké dny, posilovna, pod sukni a šaty jako vrstva proti odření.</li>'
          '<li><strong>Dlouhé:</strong> chlad a delší trénink; zkontrolujte, zda nejsou příliš dlouhé a nesvírají kotník.</li></ul>'
          '<p>Délka se odvíjí od výšky postavy. Pokud máte delší nohy, hledejte označení Tall nebo vyzkoušejte dlouhé legíny, které 7/8 prodlouží ke kotníku.</p>'
          '<h2>Vysoký pas, materiál a neprůsvitnost</h2>'
          '<p>V nabídce Puma převládají vysoký pas (High Waist, HW) a pas se širokým lemem. Taková konstrukce legíny drží na místě při pohybu a nezařezává se do boků. Pro jógu a pilates je důležitý bezešvý úplet, který netře, na posilování zase pevnější materiál, který se při hlubokém dřepu nezprůsvitní. Zkoušku si můžete udělat doma: legíny natáhněte přes dlaň a pokud skrz ně prosvítá kůže, při dřepu bude prosvítat také.</p>'
          + T(['Materiál', 'Výhoda', 'Slabina'], [
              ['Bavlna s elastanem', 'příjemná na dotek, dobře se nosí celý den', 'pot nasákne, pomalu schne'],
              ['Polyester s elastanem', 'lehký, rychle schne, drží barvu', 'povrch bývá sušší a matnější'],
              ['Polyamid s elastanem', 'hladký, pevný, jemný na kůži', 'bývá dražší, citlivý na vysokou teplotu při sušení'],
              ['Úplet s technologií odvodu potu', 'vhodný na intenzivní trénink', 'název technologie se liší, sledujte popis nabídky']]) +
          '<p>Výrobce zpravidla uvádí složení na štítku, ale konkrétní technologie pojmenovává různě. Nespoléhejte se jen na název řady, ale přečtěte si popis nabídky.</p>'
          '<h2>Velikosti, střih a dívčí legíny</h2>'
          '<p>Puma legíny sedí spíš sportovně a těsněji, ale pružnost se liší podle materiálu. Bavlnou směsované jsou volnější, technické přiléhavější. Mezi velikostmi se rozhodněte podle obvodu boků a pasu v tabulce, nikoli podle obvyklé konfekční velikosti. Dámské i pánské kousky se mohou lišit délkou i střihem v rozkroku. Pánské běžecké legíny z nabídky mají delší střih a bývají určené pro běh v chladu nebo pod šortky.</p>'
          '<p>Dívčí legíny jsou samostatná řada s označením G nebo Girls. Velikosti se udávají podle výšky dítěte, například 110, 128 nebo 152. Dítě roste, proto je lepší koupit s malou rezervou, nikoli o dvě velikosti víc, aby legíny nesjížděly. U dětí se osvědčuje měkký pas bez tlačících švů a bavlnou směsované materiály, které nedráždí. Další výběr najdete na stránce <a href="/detske-leginy/">dětské legíny</a>.</p>'
          '<h2>Puma, nebo jiná značka?</h2>'
          '<p>Značky mají trochu jiný přístup. <a href="/nike-leginy/">Nike</a> sází na vlastní technické úplety a výrazné tréninkové řady, <a href="/adidas-leginy/">Adidas</a> na pruhy a sportovní střih, <a href="/under-armour-leginy/">Under Armour</a> na kompresi a pevné přilnutí. Puma bývá přístupnější a zaměřená na stylové kolekce Essentials s logem přes stehno. V nabídce se objevují i spolupráce se závodem HYROX, který cílí na fitness závodníky. Pro základní trénink stačí kterákoli z těchto značek, rozhodnout by měl střih a materiál.</p>'
          '<h2>Barvy a kombinace</h2>'
          '<p>Černé legíny jsou nejpraktičtější, protože nezvýrazňují pot a hodí se k jakémukoli vrchu. Najdete je také ve speciálním výběru <a href="/cerne-leginy/">černé legíny</a> a <a href="/damske-leginy/">dámské legíny</a>. Fialová, červená a hnědá jsou výraznější a lépe viditelné při běhu za šera. K legínám se hodí delší triko nebo <a href="/mikiny/">mikina</a> a podprsenka z kategorie <a href="/sportovni-podprsenky/">sportovní podprsenky</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<ol><li>Perte legíny na 30 stupňů, nejlépe v sáčku na prádlo a obrácené naruby.</li>'
          '<li>Nepoužívejte aviváž, zanáší vlákna a snižuje odvod vlhkosti.</li>'
          '<li>Neperte je s oblečením se zipy a suchým zipem, které poškrábou povrch.</li>'
          '<li>Sušte je volně, nikoli na radiátoru ani v horké sušičce, pružnost se jinak ztrácí.</li>'
          '<li>Vyměňte legíny, jakmile se materiál na kolenou a v rozkroku prosvítá nebo se zhoršuje pružnost.</li></ol>',
    faq=[
        ('Která řada Puma legín je nejlepší na běh?', 'Hledejte lehké syntetické modely s označením běžecké, například řady Run Velocity nebo Dreamrun. Důležitá je pevnost pasu, rychlé schnutí a případně reflexní prvky nebo kapsa. Bavlnou směsované Essentials se hodí spíš na chůzi a volný čas než na pravidelný běh.'),
        ('Co znamená označení 7/8 u legín?', 'Legíny sahají zhruba nad kotník, tedy zhruba sedm osmin délky nohy. Nezachytávají se o boty a odkryjí kotník. Jsou oblíbené na cvičení i běžné nošení, protože sedí na většině postav a nemusí se zkracovat.'),
        ('Jak poznám, že legíny neprosvítají?', 'Natáhněte látku přes dlaň a prohlédněte ji pod světlem. Pokud prosvítá kůže, při dřepu prosvítat bude. Silnější úplet a tmavé barvy jsou méně rizikové. U tréninkových řad s vysokým pasem bývá neprůsvitnost jedním z hlavních požadavků.'),
        ('Jakou velikost dívčích legín koupit?', 'Řiďte se výškou dítěte uvedenou v tabulce, například 128 nebo 152. Kupujte s malou rezervou, nejvýše o jednu velikost víc. Příliš velké legíny sjíždějí a ztrácejí tvar. Při růstu pomůže pružný pas, který se přizpůsobí.'),
        ('Jsou Puma legíny z bavlny dobré na cvičení?', 'Na lehké cvičení a domácí jógu ano, na intenzivní trénink ne. Bavlna se při pocení nasákne a pomalu schne. Při vyšším zatížení vybírejte syntetický úplet s elastanem, který pot odvádí.'),
        ('Jak legíny prát, aby vydržely?', 'Perte je na 30 stupňů v sáčku na prádlo, bez aviváže, obrácené na rubovou stranu a bez zipů v bubnu. Sušte je volně. Horká sušička a radiátor poškozují elastan a legíny se vytahují a ztrácejí tvar.'),
        ('Hodí se Puma legíny i pro muže?', 'V nabídce jsou i pánské běžecké legíny a tréninkové kousky. Delší střih a odlišný rozkrok jsou stavěné na mužskou postavu. Pokud vám sedí dámský model, nic nebrání jeho nošení, ale střih v rozkroku bývá jiný.'),
        ('Kdy zvolit short leggings místo dlouhých?', 'Při horkém počasí, na posilovně a pod šaty nebo sukni jako ochrana proti odření stehen. Krátký střih je pohodlný na kolo i na tanec. V chladu a při běhu venku v zimě se hodí dlouhé nebo 7/8 legíny.'),
        ('Čím se Puma liší od Nike nebo Adidas?', 'Všechny tři značky mají sportovní i volnočasové řady. Puma bývá výraznější logem a cenově přístupnější, Nike nabízí více technických úpletů, Adidas pruhy a klasický sportovní střih. Rozhodovat by měl střih, materiál a velikost, ne jen značka.'),
        ('Jak dlouho legíny vydrží?', 'Při pravidelném nošení a šetrném praní jednu až dvě sezóny intenzivního používání, déle při občasném. Konec životnosti poznáte podle průsvitnosti, vytahaných kolen a ztráty pružnosti pasu. Ty se po vyprání už nevrátí.'),
    ])

# ------------------------------------------------------------------ columbia-vesta
NEW['columbia-vesta'] = dict(
    title='Columbia vesta: péřové, zateplené a softshellové',
    desc='Columbia vesty: zateplené Powder Lite, péřové Lake 22, softshell Ascender a hybridní Powder Pass. Jak zvolit izolaci, střih a velikost a porovnat obchody.',
    intro='<p>Columbia je americká outdoorová značka a její vesty patří k nejvyhledávanějším v <a href="/sportovni-vesty/">kategorii vest</a>. Najdete tu zateplené prošívané vesty na každý den, péřové modely s označením Down, hybridní kusy, kde je izolace jen na hrudi, a lehké softshelly na vítr. '
          'Stránka vysvětluje, jak rozlišit izolaci a konstrukci podle názvu, jak se vesta nosí ve vrstvách, jak vybrat velikost a střih pro ženy, muže i děti a čím se Columbia liší od The North Face nebo 4F. Průvodce uvádí i péči o péřová a syntetická plnění a ukazuje, jak číst nabídky obchodů.</p>',
    guide='<h2>Co Columbia ve vestách nabízí</h2>'
          '<p>Columbia šije outdoorové oblečení pro turistiku, lyžování a běžný život ve chladných měsících. Vesty jsou u značky jedním z nejpraktičtějších kusů, protože se nosí buď samostatně na teplejší dny, nebo pod bundou jako středová vrstva. V nabídkách se vyskytují názvy jako Powder Lite, Powder Pass, Lake 22, Puffect, Heavenly, Copper Crest nebo Ascender. Konkrétní vlastnosti nabízí popis modelu, ale podle názvu a typu zboží poznáte hlavní směr.</p>'
          + T(['Typ vesty', 'Pro koho a kdy', 'Na co se dívat'], [
              ['Zateplená prošívaná (Powder Lite, Puffect, Copper Crest)', 'podzim, jaro, město, procházky', 'syntetická izolace, která hřeje i při navlhnutí'],
              ['Péřová (Lake 22 Down)', 'chladné dny, zima ve vrstvách', 'péřové plnění, citlivost na vlhko, nízká hmotnost'],
              ['Hybridní (Powder Pass Hybrid, Juniper Peak Hybrid)', 'pohyb v chladu, aktivní turistika', 'izolace na trupu, pružnější materiál po stranách'],
              ['Softshellová (Ascender, Tall Heights)', 'vítr, mírný déšť, turistika na jaře a na podzim', 'větruvzdornost a pružnost, méně tepla'],
              ['Half zip a fleecové (Basin Trail, Hike, Timber Crest)', 'chladné ráno, vrstva pod bundu', 'prodyšnost, propustnost větru'],
              ['Dětské (Pike Lake, Arctic Blast)', 'škola, výlety, hřiště', 'růst dítěte, reflexní prvky, snadné praní']]) +
          '<p>Rozhodující je tedy otázka, jak studeně bude a jak hodně se budete pohybovat. Prošívaná vesta chrání při stání a chůzi, fleece a softshell lépe snášejí běh a kolo, protože prodyšnost převažuje nad izolací.</p>'
          '<h2>Péřová, nebo syntetická izolace</h2>'
          '<p>Péřová izolace je lehčí a po sbalení menší, ale po navlhnutí ztrácí schopnost hřát. Syntetická je těžší, ale i vlhká izoluje a snáz se perou. V nabídce Columbia se objevují názvy s označením Down i údaji o fill power, například 650 Fill Power. Čím vyšší fill power, tím víc tepla na gram, ale číslo samo nic neříká o odolnosti proti vlhku. Pokud jedete v lese za mlhy nebo při sněžení, syntetika je praktičtější. Pro suchý mráz a sbalení do batohu zvolte péří.</p>'
          '<ul><li><strong>Hybridní konstrukce:</strong> izolace jen na hrudi a zádech, pohyblivé části z elastického materiálu, hodí se na turistiku.</li>'
          '<li><strong>Odrazivé a tepelné vložky:</strong> značka je používá u některých řad, ale popis modelu ověřte přímo v nabídce.</li>'
          '<li><strong>Dlouhé prošívání (Puffect Long):</strong> prodloužené záda a boky chrání před průvanem.</li>'
          '<li><strong>Kapuce:</strong> většina vest ji nemá, takže ji nahradí čepice nebo šála.</li></ul>'
          '<p>Další vesty podle účelu najdete také na stránkách <a href="/damske-vesty/">dámské vesty</a>, <a href="/panske-vesty/">pánské vesty</a> a <a href="/detske-vesty/">dětské vesty</a>.</p>'
          '<h2>Jak vesta sedí a jak ji vrstvit</h2>'
          '<p>Vesta se nosí přes triko, košili nebo tenkou mikinu a pod bundu. Nemá být přiléhavá jako funkční vrstva, ale musí sedět v ramenou. Pokud je příliš volná, studený vzduch vniká dovnitř. Příliš těsná tlačí a omezuje pohyb paží. Při zapnutém zipu byste měli volně zvednout ruce nad hlavu a vesta by se neměla vyhrnout nad pas. Dámské střihy bývají kratší a užší v pase, pánské delší a širší v ramenou.</p>'
          + T(['Vrstva', 'Příklad', 'Úloha'], [
              ['Základní', 'funkční triko, termoprádlo', 'odvod potu od těla'],
              ['Střední', 'vesta, fleece, tenká mikina', 'zadržení tepla'],
              ['Vnější', 'nepromokavá bunda, softshell', 'ochrana před větrem a deštěm']]) +
          '<p>Pokud kombinujete vestu s bundou, vybírejte tenčí kus, aby se pod ním nesvíral loket. Do větru je dobrý <a href="/softshellove-bundy/">softshell</a>, na déšť <a href="/nepromokave-bundy/">nepromokavá bunda</a> a pro kombinaci se zimou <a href="/zimni-bundy/">zimní bunda</a>. Pod vestu v mrazu patří <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<h2>Velikost a střih pro ženy, muže a děti</h2>'
          '<p>Ženské i mužské modely se vyrábějí ve velikostech XS až XXL, ve vybraných řadách i ve velikostech Plus, a dětské podle věku nebo výšky. Značka v anglických a francouzských popisech používá výrazy Women, Femme, Men a Youth, takže při hledání se nemusíte řídit jen českým označením. Měřte hrudník, ne pas, protože vesta musí sedět v horní části těla. Podle tabulky v nabídce porovnejte obvod hrudníku a délku zad.</p>'
          '<p>U dětí počítejte s růstem a koupě o jednu velikost větší je rozumná, jenže příliš velká vesta se vyhrnuje a netěsní. Dětské modely mívají měkčí zip a bezpečné zapínání. Zkontrolujte kapsy: děti si do nich ukládají rukavice a klíče, takže kapsy se zipem přijdou vhod.</p>'
          '<h2>Columbia ve srovnání s jinými značkami</h2>'
          '<p>Columbia je pro mnoho lidí první outdoorovou volbou s dobrým poměrem funkčnosti a vzhledu. Vedle ní stojí <a href="/the-north-face-vesta/">The North Face</a> s výraznějším sportovním stylem, <a href="/vesta-4f/">4F</a> s lehčími a levnějšími kusy a <a href="/kilpi-vesta/">Kilpi</a> jako český výrobce s jednoduššími vestami. Výběr nerozhodne značka sama, ale typ izolace, střih a pasování na tělo.</p>'
          '<h2>Péče a skladování</h2>'
          '<ol><li>Péřové vesty perte na šetrný program s prostředkem určeným pro peří a dosušte je s tenisovými míčky v sušičce na nízké teplotě, aby se peří nezhroutilo.</li>'
          '<li>Syntetické vesty snesou běžné praní na 30 stupňů a sušení naplocho.</li>'
          '<li>Softshell perte bez aviváže, která poškozuje voděodolnou úpravu, a po sezóně ji obnovte impregnací.</li>'
          '<li>Vesty skladujte volně, ne stlačené v sáčku, jinak plnění ztrácí objem.</li>'
          '<li>Zipy občas očistěte a vypláchněte, aby nevázly.</li></ol>',
    faq=[
        ('Co znamená Down v názvu vesty Columbia?', 'Označuje péřové plnění. Peří je lehké a výborně hřeje při malém objemu, ale po navlhnutí ztrácí tepelnou izolaci. Hodí se do suchého mrazu a do batohu. Pro vlhké počasí je praktičtější syntetická izolace, která hřeje i mokrá.'),
        ('Čím se liší zateplená a softshellová vesta?', 'Zateplená má prošívanou izolaci a chrání před chladem při stání a chůzi. Softshell odráží vítr a lehký déšť, je pružný a prodyšný, ale hřeje méně. Na jarní turistiku a kolo je lepší softshell, na zimní procházku zateplená.'),
        ('Jak vybrat velikost vesty?', 'Změřte obvod hrudníku a porovnejte ho s tabulkou v nabídce. Vesta musí sedět v ramenou a po zapnutí zipu se nemá vyhrnout, když zvednete ruce. Pokud ji chcete nosit přes mikinu, zvolte o něco volnější velikost, ale ne tak velkou, aby nefoukalo.'),
        ('Hodí se vesta Columbia na lyže?', 'Jako střední vrstva ano, pod lyžařskou bundou nebo samostatně při teplejším dni. Na svah potřebujete především vnější vrstvu, která odolá sněhu a větru. Vesty ze sekce <a href="/lyzarske-bundy/">lyžařských bund</a> jsou určené spíš pro samotný sport, zatímco Columbia vesta chrání trup při pohybu v chladu.'),
        ('Jak prát péřovou vestu?', 'Použijte jemný program na 30 stupňů a prostředek na peří. Vestu dobře vypláchněte, vysušte při nízké teplotě a do bubnu přidejte tenisové míčky, které peří rozbijí. Nepoužívejte aviváž. Pokud výrobce praní nepovoluje, svěřte ji čistírně.'),
        ('Jsou dětské vesty Columbia teplé?', 'Jsou vhodné jako vrstva na jaro, podzim a do školy, při mrazu je doplňte mikinou a bundou. Dětem se osvědčují modely s bezpečným zipem a kapsami. Velikost volte s malou rezervou, nikoli o dvě čísla víc, aby se vesta nevyhrnovala.'),
        ('Má vesta nahradit bundu?', 'Ne, vesta chrání trup, ale ne paže. V mrazu a v dešti potřebujete rukávy, takže vesta slouží jako vrstva pod bundu nebo na teplejší dny. Při pohybu je ale často příjemnější než bunda, protože se v rukávech nepotíte.'),
        ('Kdy se vyplatí nakupovat vesty?', 'Nejširší výběr velikostí je na začátku podzimu. Slevy přicházejí na konci zimy a na jaře, ale některé velikosti a barvy se rozprodávají nejdřív. Pokud znáte konkrétní model, porovnejte více obchodů a sledujte dostupnost.'),
        ('Co znamená fill power u péřových vest?', 'Údaj vyjadřuje, jak velký objem zabere unce peří, a tedy kolik tepla zachytí na gram. Vyšší číslo znamená lehčí vestu při stejném teple. Nehodnotí odolnost proti vlhku ani šití, takže samotné číslo nestačí a srovnávejte i hmotnost a konstrukci.'),
        ('Jak poznat, že vesta nebude příliš těsná?', 'Zapněte zip, zvedněte ruce nad hlavu a předkloňte se. Vesta se nesmí vyhrnovat ani tlačit v podpaží. Pod ní můžete mít triko nebo tenkou mikinu. Pokud ji chcete vrstvit s bundou, zvolte tenčí typ, aby se pod bundou neskládala.'),
    ])

# ------------------------------------------------------------------ doplňky (delší průvodce)
NEW['reima-cepice']['guide'] += (
    '<h2>Kdy dítě čepici nechce nosit</h2>'
    '<p>Odpor k čepici má většinou konkrétní příčinu. Nejčastěji škrábe vlna na čele, tlačí šev nad uchem, zakrývá oči nebo je v bytě příliš teplá. Pomůže nechat dítě vybrat si barvu a vzor, protože čepici, kterou si samo zvolilo, nosí ochotněji. Zkuste ji také zkoušet doma, ne až u dveří, kdy spěcháte. Menším dětem se osvědčují čepice s měkkým lemem a zavazováním, které se dá povolit, zatímco školáci ocení tenkou beanii, jež se vejde do kapsy.</p>'
    '<p>Při cestě do školky a ze školky počítejte s tím, že dítě se pohybuje a potí. Mokrá čepice pak chladí, a proto má smysl nosit v batůžku druhou, suchou. Po návratu domů nechte čepici vyschnout na vzduchu, ne na topení.</p>'
    '<h2>Jak čepici sladit s ostatními doplňky</h2>'
    '<p>Čepice, nákrčník a rukavice se v zimě nosí jako sada. Sjednocení barev dětem usnadní oblékání a rodičům hledání ztracených kousků. Když kupujete celou sadu, držte se jedné kolekce, protože odstíny stejné barvy se mezi ročníky liší. Menší doplňky, například <a href="/merino-doplnky/">merino doplňky</a>, přidají tenkou vrstvu pod čepici. Pokud dítě vyrazí na delší pobyt venku, nákrčník zakrývá krk a bradu a čepice nemusí být tak hluboká.</p>')

NEW['lacoste-teplaky']['intro'] = NEW['lacoste-teplaky']['intro'].replace('Průvodce vysvětluje,', 'Najdete tu ověřené rady k výběru i kombinování. Průvodce vysvětluje,')
NEW['lacoste-teplaky']['guide'] += (
    '<h2>Kdy se vyplatí kupovat značkové tepláky</h2>'
    '<p>Tepláky za vyšší cenu mají smysl, pokud je budete nosit často a dlouho. Kvalitní bavlněná pletenina vydrží víc sezón a drží tvar i po opakovaném praní, zatímco levnější kalhoty se brzy vytáhnou na kolenou. Ptejte se proto, kolikrát týdně je obléknete. Pokud každý den, rozdíl v životnosti se vyplatí. Pokud jen na doma a občas, stačí jednodušší kousek.</p>'
    '<p>Prodejci mění kolekce dvakrát ročně a starší barvy se rozprodávají. Neutrální odstíny, jako černá, šedá a námořnická modrá, se stahují rychleji než výrazné. Chcete-li konkrétní barvu a velikost, kupujte včas a ověřte, zda ji obchod opravdu drží skladem.</p>'
    '<h2>Tepláky do práce a na cesty</h2>'
    '<p>V uvolněných kancelářích a při práci z domova se hodí tmavé tepláky bez výrazného loga, s úzkou manžetou a hladkým povrchem. Na cesty letadlem jsou praktické díky měkkému pasu a kapsám se zipem, do kterých se vejdou doklady. Delší cestu snáší lépe materiál s příměsí elastanu, který se na kolenou nevytahuje. K tomu přidejte lehkou mikinu, jelikož v letadle bývá chladno, a pohodlné boty, třeba z kategorie <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
    '<p>Dětské tepláky Lacoste jsou méně obvyklé a hodí se spíš na slavnostnější příležitosti než na hřiště. Pro každodenní hraní vybírejte odolnější materiál a pár velikostí navíc, protože děti rostou a koleno bývá první, co se prodře. Podrobněji se tomu věnuje stránka <a href="/detske-teplaky/">dětské tepláky</a>.</p>')

NEW['puma-leginy']['guide'] += (
    '<h2>Jak otestovat legíny při zkoušení</h2>'
    '<p>Doma si legíny vyzkoušejte při pohybech, které budete při cvičení dělat. Udělejte hluboký dřep, zvedněte nohu do výšky pasu, předkloňte se a zatočte tělem. Pas se nesmí sunout dolů ani se zařezávat do břicha. Švy nesmí tlačit na stehnech a v rozkroku. Sedněte si na chvíli a zkontrolujte, zda se nezačnou krčit na kolenou. Příliš těsné legíny naopak omezují krevní oběh a po půl hodině je chcete sundat.</p>'
    '<p>Pokud kupujete na dálku, nechte si v obchodě možnost vrácení a legíny po rozbalení nevypírejte, dokud nejste rozhodnutí. Použité kousky obchody většinou nepřijímají. Většina značek také nabízí tabulku, která vychází z obvodu pasu a boků, proto změřte obojí a vyberte větší hodnotu.</p>'
    '<h2>Legíny na jednotlivé sporty</h2>'
    '<ul><li><strong>Běh:</strong> lehčí úplet, kapsa na klíče nebo telefon, v chladu delší střih; v létě krátké nebo 3/4.</li>'
    '<li><strong>Posilovna:</strong> pevný materiál, vysoký pas, který nesjede při dřepu, a neprůsvitnost.</li>'
    '<li><strong>Jóga a pilates:</strong> měkký a pružný úplet, bezešvé provedení, široký pas, který netlačí.</li>'
    '<li><strong>Tanec a gymnastika:</strong> hladký pevný materiál, který se nezachycuje o podlahu a nesvírá.</li>'
    '<li><strong>Každodenní nošení:</strong> bavlnou směsované legíny s logem Essentials, kombinace s tunikou nebo dlouhým svetrem.</li>'
    '<li><strong>Cyklistika:</strong> bez vnitřních švů v rozkroku, jinak třou; pro delší jízdy jsou lepší cyklistické kalhoty s vložkou.</li></ul>'
    '<h2>Časté chyby při výběru</h2>'
    '<p>Nejčastější chybou je koupit legíny jen podle fotografie. Barva vypadá na monitoru jinak než ve skutečnosti a materiál nepoznáte bez složení. Další chyba je nesprávná velikost: příliš malé se prosvítají a zařezávají, příliš velké sjíždějí. Poslední je nošení stejných legín na všechno. Cvičební kousky se rychle opotřebují, pokud je nosíte i na cesty, a bavlněné Essentials se nehodí na intenzivní běh. Rozdělte si tedy legíny na dva páry, tréninkové a volnočasové.</p>')

NEW['columbia-vesta']['intro'] = NEW['columbia-vesta']['intro'].replace('Průvodce uvádí i péči', 'Dozvíte se i rozdíly mezi dámskými, pánskými a dětskými řadami. Průvodce uvádí i péči')
NEW['columbia-vesta']['guide'] += (
    '<h2>Vesta podle ročního období</h2>'
    '<p>Na jaře a na podzim se osvědčuje lehká prošívaná nebo softshellová vesta, protože ráno bývá chladno a odpoledne teplo. Můžete ji snadno sundat a sbalit do batohu. V zimě patří vesta pod bundu, kde zahřeje jádro těla, a při mírných mrazech ji nosíte s mikinou samostatně. V létě se hodí tenká vesta na horské túry, kde teplota na hřebeni prudce klesá. Dlouhé modely sahající pod pas ocení ti, kdo hodně sedí nebo jezdí na kole, protože chrání spodní část zad.</p>'
    '<h2>Praktické detaily, které vyberou</h2>'
    '<ul><li><strong>Kapsy se zipem:</strong> v pohybu neztratíte klíče a telefon, kapsy na rukou zahřejí prsty.</li>'
    '<li><strong>Zip s krytkou u brady:</strong> chrání obličej před studeným kovem a zabrání dření.</li>'
    '<li><strong>Stahování lemu:</strong> šňůrka na spodním okraji zabrání průvanu.</li>'
    '<li><strong>Vnitřní kapsa:</strong> na doklady nebo na sbalení vesty do sebe, pokud ji model nabízí.</li>'
    '<li><strong>Reflexní prvky:</strong> uvítáte je při dopravě a chůzi za šera.</li></ul>'
    '<p>Pokud hledáte výraznější barvu pro lepší viditelnost, existuje i samostatný výběr <a href="/zlute-vesty/">žluté vesty</a>. Pro běžný každodenní styl a skladnost je ale nejuniverzálnější černá, hnědá nebo námořnická modrá, protože se dobře kombinují s džínami i s turistickými kalhotami.</p>'
    '<h2>Kdy vesta nestačí</h2>'
    '<p>Při dlouhém stání v mrazu, při silném větru a v deštivém počasí potřebujete rukávy a vnější nepromokavou vrstvu. Vesta zahřeje jádro, ale ruce a ramena zůstanou odkryté. Při dlouhém sezení venku, třeba na tribuně, proto zvolte raději bundu nebo přidejte vrstvu pod vestu. Vesta také nechrání před promočením. Péřová pak po zvlhnutí přestane hřát, takže při dešti zvolte syntetický model nebo přidejte plášť.</p>')
