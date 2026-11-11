"""sporteka.cz — facet landing texts wave 171: adidas-kratasy, detske-lyzarske-kalhoty, under-armour-ponozky, detske-teplaky.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ adidas-kratasy
NEW['adidas-kratasy'] = dict(
    title='Adidas kraťasy: řady, střihy a výběr podle sportu',
    desc='Adidas kraťasy na fotbal, běh, trénink i každý den. Jak se liší řady Squadra, Entrada, Own the Run a Essentials, jak vybrat velikost a délku.',
    intro='<p>Adidas šije kraťasy pro několik zcela odlišných situací a z názvu řady se dá poznat, na co jsou určené. Řady Squadra, Entrada a Tiro vznikly pro fotbalové tréninky a zápasy, Own the Run pro běh, Essentials a 3-Stripes pro volný čas a lehké cvičení. '
          'Na této stránce jsou kraťasy značky z kategorie <a href="/sportovni-kratasy/">sportovní kraťasy</a>, pánské, dámské i dětské, tkané i pletené. Průvodce vysvětluje, jak se čtou názvy modelů, čím se liší tkaná látka od žerzeje, kdy se vyplatí vnitřní slipy nebo dvouvrstvý střih, jak vybrat délku nohavice a proč dámské vysoké pasy sedí jinak než týmové šortky. '
          'Najdete zde i srovnání s dalšími značkami a odkazy na výběry podle pohlaví, takže si zúžíte nabídku rychleji než při procházení jednotlivých e-shopů.</p>',
    guide='<h2>Jak se v nabídce Adidas orientovat podle názvů řad</h2>'
          '<p>Katalog značky působí na první pohled chaoticky, protože jeden střih se prodává pod desítkami kódů. Pomůže znát několik opakujících se slov, která naznačují určení. Název řady je spolehlivější vodítko než barva nebo cena, protože říká, pro koho a pro jaký pohyb byl střih navržen.</p>'
          + T(['Řada nebo označení', 'Zaměření', 'Pro koho se hodí'], [
              ['Squadra, Entrada, Tiro', 'týmový fotbal a tréninkové šortky', 'kluby, školní týmy, hráči na trénink'],
              ['Own the Run', 'běh, lehká tkaná látka a kapsa', 'běžci na silnici a na dráze'],
              ['Essentials, 3-Stripes', 'volný čas, mírná aktivita', 'každodenní nošení, lehké cvičení, léto'],
              ['Chelsea', 'volnější tkaný střih po kolena', 'pohodlí v teple, procházky, dovolená'],
              ['Biker, High Waisted', 'přiléhavé dámské šortky ve vysokém pasu', 'fitness, jóga, pilates, podklad pod sukni'],
              ['Reversible, 2 in 1', 'oboustranné nebo dvouvrstvé šortky', 'trénink s vnitřními slipy, týmové barvy'],
              ['Referee', 'rozhodcovské šortky', 'rozhodčí, trenéři a všichni, kdo chtějí neutrální černý střih']]) +
          '<p>Značka používá také zkratky jako W pro dámské nebo K a Kid pro dětské modely. V takto zkrácených názvech se skrývá i velikostní řada, a proto před nákupem ověřte, zda nejde o jinou skupinu, než hledáte. Dámský model v pánském obchodě i naopak je v nabídce bez úpravy filtru častější, než byste čekali.</p>'
          '<h2>Fotbalové kraťasy: Squadra, Entrada a Tiro</h2>'
          '<p>Týmové řady slouží na tréninku i v zápase. Jsou z lehkého polyesteru, mají pružný pas se šňůrkou a boční otvory, které nebrání kopacímu pohybu. Squadra a Entrada bývají nejjednodušší a nejlépe dostupné pro celé týmy, protože se dají objednat ve stejné barvě pro všechny hráče. Tiro je střih o něco moderněji laděný a v nabídce se objevuje i ve dvouvrstvé verzi, kde vnější šortka překrývá přiléhavou vnitřní vrstvu.</p>'
          '<p>Chcete-li kraťasy do zápasu, hledejte jednolité barvy a odstín shodný s dresy. K tomu se hodí <a href="/dresy/">dresy</a> a dlouhé ponožky nebo štulpny. Na trénink si vystačíte s jakoukoli barvou. Pro brankáře nabízí značka vypodložené brankářské modely, ty ale slouží hlavně na hřiště s tvrdým povrchem, kde chrání před odřením boků a kolen.</p>'
          '<ul><li><strong>Délka:</strong> fotbalové šortky končí nad kolenem, aby nepřekážely při kopu.</li>'
          '<li><strong>Pas:</strong> pružná guma se šňůrkou drží bez ohledu na pohyb, na zápas ji ale pevně uvažte.</li>'
          '<li><strong>Kapsy:</strong> bývají malé nebo chybí, hráč na hřišti totiž nic nenosí.</li>'
          '<li><strong>Prodyšnost:</strong> děrované panely nebo síťka po stranách pomáhají odvádět teplo.</li></ul>'
          '<h2>Běžecké šortky a lehký trénink</h2>'
          '<p>Běžecké modely jsou lehčí a kratší než týmové. Mívají vnitřní slipy, které nahrazují spodní prádlo a zabraňují vzájemnému tření, a malou kapsu na klíč nebo gel. Řada Own the Run patří ke klasice: tenká tkaná látka, nízká hmotnost a střih, který se při kroku nepodtahuje. Na delší tratě má smysl prohlédnout švy v rozkroku, protože každý hrubší šev se po desítkách kilometrů projeví otlakem.</p>'
          '<p>Pokud kombinujete běh a posilování, zvolte model s pružnou látkou, který při dřepu neprosvítá. Vyzkoušejte ho předklonem před zrcadlem nebo se dřepem přímo doma. Kdo chce pod volné šortky přiléhavou vrstvu, najde ji ve výběru <a href="/leginy/">legíny</a>.</p>'
          '<h2>Volnočasové Essentials a 3-Stripes</h2>'
          '<p>Nejširší část sortimentu tvoří bavlněné a směsové šortky se třemi pruhy po straně. Pletenina je měkká a pohodlná, ale při pocení ztěžkne a pomalu schne, takže na intenzivní sport se nehodí. Tkané modely z polyesteru jsou lehčí, rychleji schnou a lépe snášejí déšť i bazén. Pletená varianta se nosí k trikům a mikinám, a pokud k ní pasuje <a href="/mikiny/">mikina</a>, vznikne pohodlný jarní outfit na procházku.</p>'
          '<p>Volnočasové šortky mívají běžné kapsy, někdy zipové, a širší střih po stehnech. Velikost proto nevybírejte podle nejtěsnějšího kusu, který jste kdy měli, ale podle pasu a tvaru boků. V případě pochybností raději sáhněte po větší velikosti, protože šňůrka uvnitř pasu vyrovná rozdíl, kdežto příliš malé kraťasy sundáte zpět na obchod.</p>'
          '<h2>Dámské modely: vysoký pas a přiléhavé střihy</h2>'
          '<p>U dámských řad dominuje vysoký pas a přiléhavý střih po stehna. Šortky označené jako Biker nebo Short Legging se nosí na fitness, jógu a pilates, protože nikde nepřekáží a po celý trénink drží polohu. Důležitá je neprůhlednost: hustější pletení nebo dvojitý pas zabrání prosvítání při hlubokém dřepu. Kdo se v těsných šortkách necítí dobře, najde značka volnější tkané kraťasy s pružným pasem, s volnějším střihem.</p>'
          '<p>Při výběru velikosti sledujte obvod pasu a boků v tabulce Adidas, ne jen písmeno. Vysoký pas navíc sedí jinak podle délky trupu: kratší trup má pas pod žebry, delší pas drží blíž pupku. Další srovnání najdete ve výběru <a href="/damske-kratasy/">dámské kraťasy</a>, u pánských modelů pak v kategorii <a href="/panske-kratasy/">pánské kraťasy</a>.</p>'
          '<h2>Dětské Adidas kraťasy</h2>'
          '<p>Dětské šortky, třeba Train Essentials nebo dětské Tiro, mají stejné střihy jako dospělé, jen v menších velikostech. Rostou ale rychleji než dítě, proto sáhněte po nastavitelném pasu se šňůrkou. Dítě na fotbal potřebuje lehkou látku a šortky, které nepřekáží při běhu. Pro školní tělocvik stačí jednoduchá pletenina. Velikosti se označují výškou dítěte v centimetrech a vyplatí se dát přednost větší, pokud je dítě na hranici dvou čísel.</p>'
          '<h2>Srovnání s dalšími značkami</h2>'
          '<p>Adidas má podobnou nabídku jako konkurence, ale liší se důrazem. Ve fotbalovém odvětví patří ke dvěma největším hráčům a týmové řady jsou nejdostupnější. Střih bývá u mnoha modelů o něco užší než u značky Nike, jejíž kusy porovnáte ve výběru <a href="/nike-kratasy/">Nike kraťasy</a>, ale to se u jednotlivých modelů mění. Ti, kdo chtějí jiný styl, mohou zkusit <a href="/under-armour-kratasy/">Under Armour kraťasy</a>, které jsou častěji přiléhavé a kompresní, nebo <a href="/kratasy-puma/">Puma kraťasy</a>. Svou značku si můžete prohlédnout i na stránce <a href="/znacka/adidas/">Adidas</a>.</p>'
          + T(['Kritérium', 'Týmové řady', 'Běžecké', 'Volnočasové'], [
              ['Materiál', 'lehký polyester', 'tenký tkaný polyester', 'pletenina nebo tkanina'],
              ['Vnitřní slipy', 'jen u některých modelů', 'často ano', 'obvykle ne'],
              ['Kapsy', 'malé nebo žádné', 'malá kapsa na klíč', 'běžné i zipové'],
              ['Schnutí', 'rychlé', 'velmi rychlé', 'pomalejší u bavlny']]) +
          '<h2>Kdy kraťasy neslouží</h2>'
          '<p>Žádné šortky nejsou univerzální. Na kolo potřebujete vycpanou vložku, kterou volnočasový model nemá, a na plavání rychleschnoucí materiál bez vnitřních slipů z bavlny. Při delším běhu v dešti se tkaná látka přilepí k nohám méně než pletenina. Na zimní trénink v chladu patří spíš dlouhé kalhoty, třeba z výběru <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, nebo přiléhavá vrstva pod šortkami.</p>'
          '<h2>Velikost, praní a údržba</h2>'
          '<p>Měřte pas v nejužším místě a boky v nejširším, pak je porovnejte s tabulkou. Pokud jste mezi dvěma velikostmi, vezměte větší u pletených a volnočasových kusů, a menší u týmových s pružným pasem. Tištěné logo nebo pruhy perte naruby při nízké teplotě a nesušte v sušičce na vysoký stupeň, protože se začnou odlepovat. Aviváž zhoršuje odvod potu u technických látek, proto se jí raději vyhněte.</p>'
          '<p>Kupujete-li větší počet kusů pro tým nebo třídu, hledejte shodnou řadu, ne jen shodnou barvu. Stejný odstín se u různých látek mírně liší a při společném fotografování to vynikne. Cenové rozdíly mezi obchody jsou u kraťasů značky velké a porovnání několika prodejců se hodí hlavně u starších řad, kde se zbytky velikostí vyprodávají.</p>',
    faq=[
        ('Jak poznám, jestli jsou Adidas kraťasy na fotbal nebo na běh?', 'Podle názvu řady. Squadra, Entrada a Tiro jsou týmové a tréninkové, Own the Run je běžecká řada. Běžecké bývají lehčí, kratší a s vnitřními slipy, fotbalové mají volnější nohavice a jednoduchý pas.'),
        ('Mají Adidas kraťasy vnitřní slipy?', 'Záleží na modelu. Běžecké a některé dvouvrstvé tréninkové šortky je mají, týmové a volnočasové obvykle ne. Informaci najdete v popisu u e-shopu, často zkratkou nebo slovy 2 in 1 či s vnitřními slipy.'),
        ('Jsou Adidas kraťasy spíš větší, nebo menší?', 'Střih se liší podle řady. Týmové a volnočasové bývají spíš volnější, dámské přiléhavé šortky ve vysokém pasu sedí těsně. Spolehlivě pomůže jen tabulka obvodu pasu a boků na stránce konkrétního modelu.'),
        ('Co znamenají tři pruhy na kraťasech?', 'Tři pruhy jsou charakteristický prvek značky a objevují se na šortkách, tričkách i teplácích. Funkci nemají, jde o designové označení. Podle nich často poznáte volnočasové řady 3-Stripes a Essentials.'),
        ('Hodí se Adidas kraťasy do posilovny?', 'Ano, pokud zvolíte model z pružné látky, který se při dřepu nepřetahuje a neprosvítá. U žen se osvědčují přiléhavé šortky ve vysokém pasu, u mužů tkané kraťasy po kolena nebo tréninkové šortky.'),
        ('Jak vybrat dětské Adidas kraťasy?', 'Podle výšky dítěte v centimetrech a s rezervou na růst. Důležitý je pas se šňůrkou, který se dá upravit. Na fotbal zvolte lehkou tréninkovou řadu, do školy a na hraní stačí jednoduchá pletenina.'),
        ('Jak prát sportovní kraťasy, aby vydržely?', 'Perte naruby při nízké teplotě, bez aviváže a bez sušičky. Tištěné logo a pruhy snesou méně než samotná látka. Na potní zápach pomůže prací prostředek na sport, ne vyšší teplota.'),
        ('Mohu kraťasy použít na jiný sport, než pro který jsou určené?', 'Do jisté míry ano. Fotbalové šortky jsou dobré na běh a trénink, volnočasové bavlněné se na intenzivní sport nehodí, protože nasáknou potem a pomalu schnou. Cyklistika a plavání potřebují speciální střih.'),
        ('Čím se Adidas kraťasy liší od Nike a Under Armour?', 'Adidas má nejširší týmovou a fotbalovou nabídku, Nike podobný rozsah s jiným střihem a Under Armour častěji přiléhavé a kompresní modely. Rozdíly se mění podle řady, proto porovnávejte konkrétní kusy, ne značky obecně.'),
    ])

# ------------------------------------------------------------------ detske-lyzarske-kalhoty
NEW['detske-lyzarske-kalhoty'] = dict(
    title='Dětské lyžařské kalhoty: velikost, lacl, výběr podle věku',
    desc='Dětské lyžařské kalhoty pro kluky a holky: jak vybrat velikost podle výšky, kdy zvolit lacl, jaká izolace a kolena vydrží celou sezonu.',
    intro='<p>Dítě na sněhu padá, klečí, sedí a válí se v závějích, takže zimní kalhoty musí zvládnout mnohem víc než kalhoty dospělého lyžaře. Rozhoduje odolnost kolen a zadečku, nepromokavost švů, pohodlný pas a nohavice, které se nenatahují na botu. '
          'Na této stránce jsou dětské modely z kategorie <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>, od lehkých kalhot pro školu v přírodě po zateplené kusy s laclem pro nejmenší. Průvodce vysvětluje, jak vybrat velikost podle výšky a růstu, kdy dává smysl lacl a kdy klasický pas, jak poznat kvalitní zpevnění a membránu a jak dítě oblékat pod kalhoty. '
          'Zmiňujeme i rostoucí systémy, které prodlouží životnost o jednu sezonu, a ukazujeme, kde ušetřit a kde ne.</p>',
    guide='<h2>Čím se dětské lyžařské kalhoty liší od dospělých</h2>'
          '<p>Nejde jen o zmenšený střih. Děti mají jiné proporce: relativně delší trup, kratší nohy a výraznější břicho, takže kalhoty s pasem u kyčlí se u nich neustále svlékají. Proto jsou dětské modely nasazené výš, často s elastickými šle nebo s laclem a s pružnou vložkou v pase. Nohavice bývají kratší a opatřené sněhovou manžetou, která se přitahuje na botu a nedovolí sněhu vniknout dovnitř.</p>'
          '<p>Druhý rozdíl je zátěž. Dítě tráví na sjezdovce mnoho času v klidu: při čekání na vlek, při stavění sněhuláka, při sáňkování. Kalhoty se proto zahřívají méně než u vytrvalého lyžaře a potřebují lehkou izolaci i při slabších mrazech. Při intenzivní jízdě naopak dítě rychle přehřívá, a tak se vyplatí prodyšnější materiál s odvětráním.</p>'
          '<h2>Velikost podle výšky a růstu</h2>'
          '<p>Dětské velikosti se označují výškou dítěte v centimetrech, například 110, 122, 134 nebo 146, případně věkem. Věk je ale jen hrubý údaj, protože děti stejného věku se liší o desítky centimetrů. Změřte dítě bez bot u zdi a vyberte velikost nejblíž nahoru. Pamatujte, že pod kalhoty přijdou ještě termo spodky, takže těsný střih zkoušejte s nimi.</p>'
          + T(['Výška dítěte', 'Orientační věk', 'Na co se zaměřit'], [
              ['do 98 cm', 'asi 2–3 roky', 'lacl nebo kalhoty s šlemi, snadné zapínání, pevné kolena'],
              ['104–116 cm', 'asi 4–6 let', 'lacl nebo vysoký pas, sněhová manžeta, odolný zadeček'],
              ['122–134 cm', 'asi 7–9 let', 'pohodlný pas s nastavením, první pokusy o samostatné oblékání'],
              ['140–152 cm', 'asi 10–12 let', 'střih blízký dospělým, odvětrání, volnější kolena'],
              ['158 cm a více', 'od 13 let', 'dospělé nebo juniorské velikosti, kontrola délky nohavic']]) +
          '<p>Chcete-li kalhoty využít dvě sezony, vezměte o číslo větší a spolehněte se na nastavitelný pas. Dvě čísla navíc už působí neohrabaně, látka se hromadí v kolenou a dítě se v nich špatně hýbe. Nohavice se dají podvinout nebo přitáhnout, ale pas a rozkrok musí sedět.</p>'
          '<h2>Lacl, nebo klasický pas</h2>'
          '<p>Lacl se hodí pro nejmenší a pro začátečníky. Přikrývá záda, takže mezi bundou a kalhotami nevzniká mezera, kudy by se dostal sníh, a kalhoty se nesvlékají. Nevýhodou je složitější odskok na toaletu a menší vzdušnost pod bundou. Dětské lacle mají proto často zip na boku nebo praktické zapínání. Klasický pas je pohodlnější pro větší děti, které už chtějí vypadat jako dospělí, a pro ty, co se samy oblékají.</p>'
          + T(['Konstrukce', 'Výhody', 'Nevýhody'], [
              ['Lacl s šlemi', 'bez mezer na zádech, drží na místě, hřeje trup', 'složitější toaleta, vyšší hmotnost'],
              ['Klasický pas s gumou', 'snadné oblékání, větší prodyšnost', 'může se svlékat, mezera mezi bundou a kalhotami'],
              ['Rostoucí systém', 'pas a nohavice se prodlužují na další rok', 'složitější střih, o něco vyšší hmotnost'],
              ['Kalhoty se šlemi na zip', 'dají se sundat, zachovají pas bez lacle', 'menší kryt zad při pádu']]) +
          '<h2>Izolace, membrána a vodotěsnost</h2>'
          '<p>Většina dětských kalhot má syntetickou izolaci v rozsahu od lehké po silnější. Na sjezdovku v běžných zimních dnech stačí střední hrubost; do větších mrazů nebo pro děti, které dlouho čekají, sáhněte po silnější vrstvě. Při jarním lyžování se naopak vyplatí tenčí, třeba bez izolace, spolu s vrstvením spodního prádla. Údaj o vodním sloupci v milimetrech říká, jakému tlaku vody látka vzdoruje, ale u dětí hraje větší roli kvalita švů a zpevnění než samotné číslo.</p>'
          '<p>Švy v kolenou, na zadečku a po vnitřní straně nohavic by měly být zalepené nebo překryté. Děti klečí v mokrém sněhu a každý neprůvanný šev se okamžitě projeví promoknutím. Ptejte se na výztuhu dolní hrany nohavice, která ochraňuje před poškozením hranami lyží, zvlášť u dětí, které se ještě učí jezdit a občas si kříží lyže.</p>'
          '<h2>Co musí mít kvalitní dětské kalhoty</h2>'
          '<ul><li><strong>Zpevněná kolena a zadeček:</strong> silnější látka v místech nejčastějšího kontaktu se sněhem.</li>'
          '<li><strong>Sněhová manžeta:</strong> pružná, s gumou nebo silikonovým prvkem, který zabrání sjíždění.</li>'
          '<li><strong>Nastavitelný pas nebo šle:</strong> pružina uvnitř, případně knoflíky, které dovolí upravit obvod.</li>'
          '<li><strong>Zipové kapsy:</strong> aspoň jedna kapsa, kam se vejde skipas nebo kapesník, nejlépe na zip.</li>'
          '<li><strong>Reflexní prvky:</strong> na sjezdovce se hodí viditelnost, hlavně pro dítě v davu.</li>'
          '<li><strong>Odvětrávací zipy:</strong> u větších dětí, které při jízdě zahřívají.</li></ul>'
          '<h2>Jak dítě oblékat pod kalhoty</h2>'
          '<p>Bavlna je na sněhu špatná volba, protože nasákne potem a ochladí nohy. Pod kalhoty patří funkční termoprádlo nebo merino, které odvádí vlhkost. Výběr najdete v kategorii <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>. Přes ně jedna tenká vrstva, třeba legíny nebo tenký fleece, a pak kalhoty. Nepřidávejte další silné vrstvy, protože kalhoty tím ztratí izolační efekt a dítě se bude potit a ochlazovat.</p>'
          '<p>K souboru patří také <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-rukavice/">rukavice</a> a ponožky speciálně určené pro lyže, které najdete ve výběru <a href="/lyzarske-ponozky/">lyžařské ponožky</a>. Kdo hledá celek v jednom kuse, zvolí <a href="/lyzarske-kombinezy/">lyžařskou kombinézu</a>, která pro nejmenší bývá praktičtější než dva kusy. Nezapomeňte na <a href="/lyzarske-helmy/">lyžařskou helmu</a>, která se nosí i při nácviku.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nabídka je široká a sahá od českých a evropských po severské a velké outdoorové značky. ' + B(('kilpi', 'Kilpi'), ('loap', 'Loap'), ('cmp', 'Cmp'), ('dare2b', 'Dare2b')) + ' nabízejí cenově přístupné modely pro každodenní lyžování, kde se hodí barevné vzory a snadná údržba. '
          + B(('reima', 'Reima'), ('didriksons', 'Didriksons')) + ' jsou severské značky se zaměřením na dětské zimní oblečení a na odolnost v mokru; Reima má přitom i rostoucí modely. '
          + B(('helly-hansen', 'Helly Hansen'), ('rossignol', 'Rossignol')) + ' pocházejí ze světa lyžování a nabízejí sportovnější střihy pro děti, které už jezdí pravidelně. Značky ' + B(('protest', 'Protest'), ('ziener', 'Ziener')) + ' doplňují nabídku o další střihy a barvy.</p>'
          '<h2>Kalhoty pro kluky a pro holky</h2>'
          '<p>Rozdíl je především ve střihu a barvách. Dívčí modely mají často užší boky a jemnější odstíny, chlapecké o něco širší střih. Funkčně jsou stejné a mladší děti je můžou sdílet. U větších dívek se vyplatí zvolit dámské nebo juniorské velikosti, protože dětské střihy už nemusí vyhovovat rostoucí postavě. Podívejte se i na <a href="/damske-lyzarske-kalhoty/">dámské lyžařské kalhoty</a> a <a href="/panske-lyzarske-kalhoty/">pánské lyžařské kalhoty</a>, pokud je dítě na hranici.</p>'
          '<h2>Kolik kalhot dítě potřebuje</h2>'
          '<p>Na týdenní pobyt na horách se vyplatí mít dvoje kalhoty, aby jedny mohly po dni na sněhu v klidu uschnout. Druhý pár může být starší nebo půjčený od sourozence. Pro rodinu, která jezdí jednou za rok, dává smysl půjčit si nebo koupit použité kusy v dobrém stavu, ale zkontrolujte zip, švy a sněhovou manžetu, protože právě ty se s věkem rozpadají jako první.</p>'
          '<h2>Běžecké lyžování a sáňkování</h2>'
          '<p>Pro běžky se hodí tenčí, pružnější kalhoty s lepší prodyšností, protože dítě při pohybu vyrábí hodně tepla. Zateplené lacle jsou na to příliš těžké. Na sáňkování a hru ve sněhu naopak oceníte zvýšenou odolnost zadečku a silnější izolaci, protože dítě sedí a leží na místě. Kdo si koupí jedny kalhoty na všechno, měl by zvolit střední izolaci a lehké odvětrání, a mrazivé dny řešit vrstvením.</p>'
          '<h2>Péče, sušení a další sourozenec</h2>'
          '<p>Perte podle štítku při nižší teplotě, bez aviváže, která ucpává membránu. Vodoodpudivou úpravu občas obnovte impregnací určenou pro membránové oblečení. Mokré kalhoty po lyžování rozvěste, aby uvnitř nezůstala vlhkost. Dobře udržované kalhoty od kvalitnějších značek přejdou na mladšího sourozence, proto se vyplatí neřešit jen cenu, ale i to, jak dlouho vydrží.</p>',
    faq=[
        ('Jakou velikost dětských lyžařských kalhot vybrat?', 'Podle výšky dítěte v centimetrech, ne podle věku. Změřte dítě bez bot a vyberte nejbližší vyšší velikost. Přidáním jednoho čísla získáte rezervu na růst, další číslo už snižuje pohodlí.'),
        ('Je pro malé dítě lepší lacl, nebo kalhoty s pasem?', 'Pro nejmenší bývá lepší lacl, protože drží na místě a chrání záda před sněhem. Větší děti, které se samy oblékají a chodí na toaletu, ocení klasické kalhoty s nastavitelným pasem.'),
        ('Kolik vrstev oblečení patří pod lyžařské kalhoty?', 'Obvykle stačí funkční termoprádlo a jedna tenká vrstva navíc. Bavlnu raději vynechejte. Příliš mnoho vrstev stlačí izolaci a dítě se zbytečně potí, takže mu je potom zima.'),
        ('Jaký vodní sloupec mají mít dětské lyžařské kalhoty?', 'Pro běžné lyžování stačí střední hodnota, důležitější než číslo jsou zalepené švy a zpevněná kolena. Dítě klečí a sedí ve sněhu, proto na kvalitě provedení záleží víc než na maximální hodnotě.'),
        ('Co jsou rostoucí lyžařské kalhoty?', 'Mají prodlužitelné nohavice nebo nastavitelný pas, takže dítěti vydrží o sezonu déle. Rozšíření se řeší záhyby v látce a umožní růst zhruba o jednu velikost. Zvýšená cena se tak rozloží na dvě zimy.'),
        ('Dají se dětské lyžařské kalhoty použít na sáňkování a hry ve sněhu?', 'Ano, patří to k jejich běžnému používání. Hodí se zvlášť modely se zesíleným zadečkem a koleny. Na delší pobyt venku vybírejte kalhoty se silnější izolací a po návratu je dobře usušte.'),
        ('Jak vyprat dětské lyžařské kalhoty s membránou?', 'Při teplotě podle štítku, bez aviváže a s prostředkem určeným na funkční oblečení. Po vyschnutí se vyplatí obnovit impregnaci. Aviváž a silné prášky snižují odvod vlhkosti a vodoodpudivost.'),
        ('Mohou kalhoty po starším sourozenci vydržet další dítě?', 'Ano, pokud jsou zdravé šev, zip a zpevnění. Zkontrolujte kolena, zadeček a sněhovou manžetu, případně obnovte impregnaci. Kvalitnější modely s odolnou látkou obvykle vydrží i několik sezon.'),
        ('Jak poznám, že dítě v kalhotách nepromokne?', 'Podívejte se na štítek s vodním sloupcem, zalepené švy a zpevněná místa v kolenou. Po prvním dnu zkontrolujte, zda je pod látkou sucho. Mokré kolena ukazují na slabé švy nebo vybledlou impregnaci.'),
    ])

# ------------------------------------------------------------------ under-armour-ponozky
NEW['under-armour-ponozky'] = dict(
    title='Under Armour ponožky: řady, délky a balení po třech',
    desc='Under Armour ponožky: jak se liší Performance Tech a Performance Cotton, co znamenají zkratky NS, QTR a Crew, jak vybrat velikost a délku.',
    intro='<p>Ponožky Under Armour se prodávají hlavně v balení po třech, často v jednotných barvách černé, bílé nebo v mixu. Důležité je ale poznat, co se skrývá za zkratkami v názvech: NS znamená nízké ponožky do tenisek bez viditelného lemu, QTR čtvrtinovou délku těsně nad kotník, Crew posádkovou délku do půli lýtka. '
          'Tato stránka shrnuje ponožky značky z kategorie <a href="/sportovni-ponozky/">sportovní ponožky</a> a pomáhá je dát do souvislostí s vaším sportem. Vysvětlujeme rozdíl mezi řadou Performance Tech a Performance Cotton, ukazujeme, jak velikostní rozpětí funguje u balení pro více lidí, a radíme, kdy je vhodnější bavlněná směs a kdy syntetika. '
          'Najdete tu i srovnání s dalšími značkami a odkazy na příbuzné výběry podle pohlaví.</p>',
    guide='<h2>Jak číst názvy ponožek Under Armour</h2>'
          '<p>Katalog značky je pro nováčka zdánlivě nepřehledný, protože se v něm opakuje několik slov. Když je znáte, vyberete rychle správný kus. Název se skládá z řady, počtu párů, délky a barvy, tedy například Performance Tech 3PK QTR, tedy balení tří párů čtvrtinové délky z řady Tech.</p>'
          + T(['Označení', 'Význam', 'Použití'], [
              ['NS, No Show', 'ponožka do tenisky bez viditelného lemu', 'kondiční boty, fitness, létě do plátěných bot'],
              ['Low', 'nízká, těsně nad botou', 'běh po silnici, trénink, tenis'],
              ['QTR', 'čtvrtinová, těsně nad kotník', 'univerzální každodenní sport'],
              ['Crew', 'posádková, do půli lýtka', 'trénink, studené dny, hlubší boty'],
              ['Mid-Crew', 'mezi QTR a Crew', 'kompromis pro vyšší boty a chladnější dny'],
              ['3PK, 6PK', 'balení po 3 nebo 6 párech', 'výhodnější pro pravidelné používání'],
              ['Ultimate', 'varianta se zpevněním', 'delší tréninky, větší namáhání']]) +
          '<p>Zkratky nejsou přísně jednotné. Různé modely nemusí mít přesně stejnou výšku lemu, proto vždy ověřte, jak vysoko kraj sahá.</p>'
          '<h2>Performance Tech a Performance Cotton</h2>'
          '<p>Dvě nejčastější řady se liší materiálem. Performance Tech je syntetický materiál, který při pocení nenasákne tolik jako bavlna a rychleji schne. Hodí se na běh, kondiční tréninky i delší dny v botách. Performance Cotton obsahuje větší podíl bavlny, je měkčí na dotek a při nižší zátěži pohodlnější, ale při dlouhé námaze pomaleji schne. Přesné složení najdete na štítku: u obou řad jde obvykle o směs s elastanem a polyamidem.</p>'
          + T(['Vlastnost', 'Performance Tech', 'Performance Cotton'], [
              ['Odvod potu', 'rychlejší, vlákno málo saje', 'pomalejší, bavlna drží vlhkost'],
              ['Měkkost', 'hladší, technická', 'měkčí, jemnější'],
              ['Schnutí', 'rychlé', 'pomalejší'],
              ['Nejlepší použití', 'běh, intenzivní trénink, dlouhý den', 'škola, kancelář, lehké cvičení, volný čas']]) +
          '<p>Pokud trénujete většinou v klidnějším tempu, nebo potřebujete ponožky na celý den do práce, bude vám bavlněná směs pohodlnější. Pro vytrvalejší pohyb, kdy se noha potí, volte syntetiku. Detailnější přehled materiálů najdete v kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a>, merino variantu v části <a href="/merino-ponozky/">merino ponožky</a>.</p>'
          '<h2>Délka ponožky podle boty a sportu</h2>'
          '<p>Délka se vybírá podle obuvi, ne podle sportu. Nízkou ponožku do vysoké boty nosit nechcete, protože se bota otírá o kůži a vytváří otlaky. Do nízkých tenisek zase nepatří posádková délka, která vystupuje nad kotník.</p>'
          '<ul><li><strong>Běh po silnici:</strong> Low nebo QTR podle toho, jak vysoko sahá bota; hlavní je bezpečný lem na patě.</li>'
          '<li><strong>Posilovna:</strong> NS nebo Low pro kondiční boty, Crew pro zvedání s holeněmi chráněnými před tyčí při mrtvém tahu.</li>'
          '<li><strong>Fotbal a míčové sporty:</strong> Crew pod štulpny nebo jako samostatná vrstva pod chrániče.</li>'
          '<li><strong>Každodenní nošení:</strong> NS do plátěnek a tenisek, QTR a Crew do kotníkových bot.</li>'
          '<li><strong>Studený den:</strong> Crew nebo Mid-Crew, které kryjí kotník a Achillovu šlachu.</li></ul>'
          '<h2>Velikost a balení po třech</h2>'
          '<p>Velikost bývá označena rozpětím, například M odpovídá několika číslům bot v jedné skupině. To je praktické, ale znamená, že u okrajových čísel je ponožka na hraně. Pokud nosíte číslo na horní hranici rozpětí, vezměte vyšší velikost, aby špička netlačila. Při vyšší velikosti se zase může tvořit záhyb pod chodidlem, proto vyzkoušejte jeden pár před objednáním většího počtu.</p>'
          '<p>Balení po třech nebo šesti párech se hodí, protože se ponožky rychle opotřebovávají a pár se vždy ztratí. Výhodou je jednotná barva a stejné vlastnosti, nevýhodou omezený výběr: mix barev v jednom balení nemusí odpovídat vašemu oblečení. Při koupi pro rodinu je dobré do kategorie zasáhnout dětskými variantami, které značka rovněž nabízí v bílé a v mixu.</p>'
          '<h2>Pro koho se které ponožky hodí</h2>'
          '<p>Unisex označení se objevuje u většiny modelů a znamená, že střih nemá pohlavní variantu, jen rozsah velikostí. Dámské varianty, například řada Breathe Lite, bývají tenčí a nižší, určené do nízkých bot. Pánské jsou častěji vyšší s pevnějším lemem. Dětské balení najdete s bílou nebo mixem barev, kde dominují školní tělocvik a trénink.</p>'
          '<p>Do tenisek na každodenní nošení vybírejte tenké nízké ponožky, do posilovny pevnější s mírným polstrováním. Pro hodně potící se nohu zvolte syntetický materiál a vyhněte se příliš silnému frote, v němž se teplo drží. Výběr podle pohlaví najdete v odkazech <a href="/damske-sportovni-ponozky/">dámské sportovní ponožky</a> a <a href="/panske-sportovni-ponozky/">pánské sportovní ponožky</a>.</p>'
          '<h2>Srovnání s dalšími značkami</h2>'
          '<p>Nabídka Under Armour je užší než u největších značek, ale soustředí se na jednoduché a praktické balení. V porovnání s <a href="/nike-ponozky/">Nike ponožkami</a> jde o podobné délky a řady, Nike má širší výběr barev a motivů. <a href="/adidas-ponozky/">Adidas ponožky</a> přidávají týmové štulpny a podkolenky, které Under Armour tolik nenabízí, a <a href="/puma-ponozky/">Puma ponožky</a> sázejí na jednoduché střihy a nízké ceny. Pokud chcete zjistit širší nabídku značky, otevřete stránku <a href="/znacka/under-armour/">Under Armour</a>.</p>'
          '<h2>Kdy zvolit které balení</h2>'
          '<p>Pro běžce a sportovce, kteří trénují několikrát týdně, se vyplatí šestikusové balení v jedné barvě, protože ponožky snadno spárujete po praní. Kdo ponožky nosí hlavně do školy nebo do práce, vystačí si s třípárovým mixem a bavlněnou směsí. Zvláštní skupinu tvoří nízké ponožky bez viditelného lemu, které se do nízké boty hodí nejlépe v létě. Protože každá sada používá jiný střih paty a lemu, kupujte při opakované objednávce stejný název modelu, abyste dostali stejné pohodlí.</p>'
          '<h2>Chyby, kterým se při nákupu vyhnout</h2>'
          '<ul><li><strong>Špatná délka k botě:</strong> nízká ponožka ve vyšší botě se sjíždí a otírá kotník.</li>'
          '<li><strong>Příliš malá velikost:</strong> sevřená špička způsobuje tlak na nehty a otlaky.</li>'
          '<li><strong>Bavlna na dlouhý běh:</strong> nasákne potem a po hodině začne třít.</li>'
          '<li><strong>Míchání starých a nových párů:</strong> rozdílné opotřebení způsobí nerovnoměrné tlačení.</li>'
          '<li><strong>Přehnaná tloušťka:</strong> silná ponožka v těsné botě zmenší prostor a stlačí chodidlo.</li></ul>'
          '<p>Chcete-li vyzkoušet jiný materiál, podívejte se na <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> pro lehké a vzdušné střihy nebo na <a href="/lyzarske-ponozky/">lyžařské ponožky</a> pro zimu.</p>'
          '<h2>Ponožky podle ročního období</h2>'
          '<p>V létě se hodí nízké syntetické ponožky, které odvádějí pot a nezahřívají. Na jaro a podzim stačí střední tloušťka v délce QTR nebo Crew, v zimě přidejte vyšší lem, který kryje kotník před chladem. Pro lyžování ani pro dlouhou zimní túru ale běžná sportovní ponožka nestačí, tam sáhněte po speciálních kusech. Na celoroční trénink v hale si vystačíte s jednou řadou, jen střídejte tloušťku podle teploty v tělocvičně.</p>'
          '<h2>Komfort uvnitř boty</h2>'
          '<p>Ponožka je prvním místem, kde se projeví nesprávná velikost boty. Pokud vás bota tlačí, zkuste nejdřív tenčí ponožku, ne hned větší botu. Naopak velká bota se vyrovnává silnější ponožkou jen omezeně a dlouhodobě vede k otlakům. Zkoušejte proto boty vždy v ponožkách, ve kterých budete sportovat, a ne v tenkých nízkých, které jsou součástí obchodního zkoušení.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Perte ponožky naruby při nižší teplotě, bez aviváže a bez sušičky na vysoký stupeň, která poškozuje elastan. Nejdřív rozdělte barvy: bílé a světlé nemají přijít do styku s tmavými. Pokud ponožka po čase ztratí pružnost lemu nebo se prodře pata, jde o konec její životnosti, protože další nošení způsobuje otlaky. U rychle se opotřebovaných míst, jako je pata a špička, pomáhá střídání párů.</p>'
          '<p>Pro prevenci zápachu stačí pravidelné praní a večerní vyvětrání. Ponožky nenechávejte dlouho vlhké v tašce, protože se v nich rychle množí bakterie. Kdo si kupuje větší balení, může pár označit podle dne a střídat je rovnoměrně, aby se opotřebovávaly stejně.</p>',
    faq=[
        ('Co znamená NS, QTR a Crew u ponožek Under Armour?', 'NS je ponožka do tenisky bez viditelného lemu, QTR čtvrtinová délka nad kotník a Crew posádková délka do půli lýtka. Zkratku vždy porovnejte s botou, do které ponožku obujete.'),
        ('Jaký je rozdíl mezi Performance Tech a Performance Cotton?', 'Tech je syntetický a rychleji schne, Cotton obsahuje víc bavlny a je měkčí. Na intenzivní sport a delší tréninky volte Tech, na škola, práci a lehké cvičení stačí Cotton.'),
        ('Jak velikost ponožek vybrat, když jsem na hranici dvou čísel?', 'Raději zvolte větší velikost, aby špička netlačila. Pokud se po obutí tvoří záhyb, zkuste další balení. Ponožky bývají pružné a rozpětí velikostí je hodně široké, takže nejlepší je zkouška na jednom páru.'),
        ('Hodí se ponožky Under Armour na běh?', 'Ano, nejlépe řada Performance Tech v nízké nebo čtvrtinové délce. Syntetika rychle odvádí pot a drží tvar. Na dlouhé tratě sledujte hladké švy a zpevnění v místě paty a špičky.'),
        ('Jsou ponožky Under Armour unisex?', 'Většina modelů je označena jako unisex a liší se jen rozsahem velikostí. Dámské varianty, například řada Breathe Lite, bývají tenčí a nižší. Dětské balení se prodává zvlášť.'),
        ('Proč se ponožky prodávají po třech párech?', 'Protože se rychle opotřebovávají a ztrácejí. Balení nabízí jednotnou barvu a vlastnosti, takže si pár vždy dohledáte. Nevýhodou je omezený výběr a nutnost zvolit stejnou velikost pro všechny tři kusy.'),
        ('Mohu ponožky Under Armour nosit do běžných bot?', 'Ano, nízké a čtvrtinové modely dobře fungují do tenisek a plátěnek. Bavlněná směs je pro každodenní nošení pohodlnější. Do vysokých kotníkových bot vybírejte Crew délku, aby bota neodírala.'),
        ('Jak prát sportovní ponožky, aby vydržely?', 'Naruby, při nižší teplotě, bez aviváže a bez vysokého sušení. Aviváž ucpává vlákno a zhoršuje odvod potu, vysoké teplo poškozuje elastan. Tmavé a světlé kusy perte zvlášť.'),
        ('Kdy ponožky vyměnit?', 'Když se prodře pata nebo špička, ztratí lem pružnost nebo se zhroutí polstrování. Takové ponožky způsobují otlaky a puchýře. U intenzivního sportu je dobré mít několik párů a střídat je.'),
    ])

# ------------------------------------------------------------------ detske-teplaky
NEW['detske-teplaky'] = dict(
    title='Dětské tepláky: velikosti, střihy a výběr podle věku',
    desc='Dětské tepláky pro kluky i holky: jak vybrat velikost podle výšky, jaký materiál vydrží kolena, kdy zvolit manžety a které značky jsou v nabídce.',
    intro='<p>Dětské tepláky se nosí ve škole, na hřišti, na kroužku i doma, a proto musí vydržet víc než dospělé. Rozhodují kolena, pas, který se nesvléká, délka nohavic a to, jestli je materiál příjemný na pokožce. Rostoucí dítě navíc vyroste z kusu dřív, než se obnosí, takže má smysl vybírat s rezervou a dívat se na střih. '
          'Na této stránce jsou tepláky z kategorie <a href="/teplaky/">tepláky</a> pro děti, od nejmenších s jemným fleecem po sportovní kousky pro mladé fotbalisty. Průvodce vysvětluje dětské velikosti, rozdíl mezi manžetou a rovnou nohavicí, výběr materiálu podle ročního období a to, jak koupit chlapecké a dívčí tepláky, které nebudou lemovat zem. '
          'Dozvíte se také, které značky se v nabídce objevují a co lze od jednotlivých očekávat.</p>',
    guide='<h2>Co dětské tepláky odlišuje od dospělých</h2>'
          '<p>Dětské tělo má jiné proporce. Trup je relativně delší, nohy kratší a břicho výraznější, takže dospělý střih zmenšený o pár čísel sedí špatně. Dobře zpracované dětské tepláky mají proto vyšší pas s širokou gumou, tvarované nohavice a prostor v rozkroku. Také šňůrka musí fungovat jinak: u malých dětí je bezpečnější bez dlouhých konců, které se zachytí o hrazdu nebo kolo.</p>'
          '<p>Druhý rozdíl je zátěž. Dítě klečí na zemi, sedí na lavici, šplhá a padá, proto se tepláky ošoupou v kolenou a na zadečku mnohem dříve než u dospělého. Odolnější model má dvojitou látku v kolenou nebo hustší pletení a pevné švy. U levnějších kusů zvedněte látku proti světlu: když prosvítá, brzy se prodře.</p>'
          '<h2>Velikosti podle výšky a věku</h2>'
          '<p>Dětské oblečení se označuje buď výškou v centimetrech (například 128), nebo věkem (7–8 let, někdy zkráceně 7Y). Výška je spolehlivější, protože děti stejného věku se liší o hlavu. U některých amerických značek najdete označení S, M, L nebo věk v letech, která je potřeba před nákupem přepočítat podle tabulky konkrétního prodejce.</p>'
          + T(['Výška', 'Zhruba věk', 'Tipy při výběru'], [
              ['80–92 cm', '1–2 roky', 'měkká pletenina, široká guma bez šňůrky, dobré manžety'],
              ['98–110 cm', '3–5 let', 'zpevněná kolena, pas s pružinou, snadné oblékání'],
              ['116–128 cm', '6–8 let', 'odolný materiál, kapsy, první sportovní střihy'],
              ['134–146 cm', '9–11 let', 'více sportovní střihy, slabší nebo silnější gramáž podle sportu'],
              ['152–170 cm', '12 let a více', 'přechod k dospělým střihům, ověřte délku nohavic']]) +
          '<p>Při koupi s rezervou vyberte o číslo vyšší a spolehněte se na manžety, které nohavice zkrátí. Rovná nohavice bez manžety je citlivější na délku: příliš dlouhá se zašlapává a špiní, příliš krátká se zvedá nad kotník. Vyplatí se vždy porovnat rozměry z tabulky s tepláky, které dítě nosí a které mu dobře padnou.</p>'
          '<h2>Manžety, rovná nohavice a jogger</h2>'
          '<p>Nejčastějším střihem je jogger se zúženou nohavicí a manžetou u kotníku. Drží u nohy, hodí se do tenisek a nezachycuje se při běhu. Rovná nohavice se nosí spíš ve škole a doma, hodí se pro malé děti, protože se dobře obléká přes plenu nebo boty. Široké sportovní tepláky se zipem u kotníku používají mladí fotbalisté při tréninku, kdy se kalhoty natahují přes kopačky.</p>'
          + T(['Střih', 'Výhody', 'Nevýhody'], [
              ['Jogger s manžetou', 'drží u kotníku, nezachycuje se, vypadá sportovně', 'dítě s tlustšími lýtky může cítit tlak'],
              ['Rovná nohavice', 'snadné oblékání, volnost pro děti', 'může zametat zem, když je moc dlouhá'],
              ['Se zipem u kotníku', 'jde přes kopačky nebo boty', 'zip se může zasekávat o oblečení'],
              ['Rozšířená (bootcut)', 'dívčí módní střih', 'méně praktická na sport']]) +
          '<h2>Materiál podle sezóny a použití</h2>'
          '<p>Většina dětských tepláků je z bavlněné směsi s polyesterem. Bavlna je měkká, příjemná na kůži a dobře pere, ale po zmoknutí a v potu těžkne. Polyester přidává odolnost a rychleji schne. Elastan zajišťuje pružnost. Hustší pletenina s nepočesanou vnitřní stranou je vhodná pro jaro a podzim, počesaná s fleecem hřeje v zimě. Pro dítě, které se hodně potí, jsou sportovní syntetické tepláky komfortnější.</p>'
          '<ul><li><strong>Jaro a léto:</strong> tenčí pletenina nebo tkaný materiál, pohodlný na večerní hru venku.</li>'
          '<li><strong>Podzim:</strong> střední gramáž, počesaný vnitřek, manžety proti studenému vzduchu.</li>'
          '<li><strong>Zima:</strong> silnější fleece, případně vrstvení s termoprádlem pod tepláky.</li>'
          '<li><strong>Tělocvik:</strong> pružné, bez tvrdých švů a šňůrek, které by překážely.</li>'
          '<li><strong>Trénink:</strong> sportovní syntetika s pružným pasem a zipy u kotníku.</li></ul>'
          '<p>Při citlivé kůži vybírejte měkkou bavlnu bez drsných nášivek na vnitřní straně a štítky odstřihněte. Nové tepláky vyperte před prvním nošením. Pokud dítě trpí atopickým ekzémem, vyhněte se silně barvené a tištěné látce a zkuste jemný kus bez potisku.</p>'
          '<h2>Chlapecké a dívčí tepláky</h2>'
          '<p>Rozdíl je především ve střihu a barvách. Chlapecké modely mívají širší boky a volnější nohavice, dívčí užší pas a více barevných odstínů. U mladších dětí je funkčně nerozlišujete a tepláky bez rodového označení se dají sdílet mezi sourozenci. U starších dívek se objevuje módnější střih bootcut a vysoký pas. Výběr podle skupiny je v nabídce označen jako chlapecké a dívčí; pro teenagery zvažte dospělé střihy z výběru <a href="/damske-teplaky/">dámské tepláky</a> a <a href="/panske-teplaky/">pánské tepláky</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V dětském oddílu uvidíte sportovní, módní i americké značky. ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('kappa', 'Kappa')) + ' vycházejí ze sportovní tradice a nabízejí jednoduché střihy se značkovým logem, často v soupravách. '
          + B(('gap', 'Gap')) + ' je v nabídce mimořádně zastoupena a sází na klasické barvy a měkkou pleteninu s logem. '
          + B(('4f', '4F'), ('lotto', 'Lotto')) + ' přidávají evropský sportovní styl a '
          + B(('tommy-hilfiger', 'Tommy Hilfiger'), ('guess', 'Guess')) + ' módnější kousky pro volný čas. Pokud hledáte konkrétní značku, projděte stránky <a href="/nike-teplaky/">Nike tepláky</a>, <a href="/adidas-teplaky/">Adidas tepláky</a>, <a href="/under-armour-teplaky/">Under Armour tepláky</a> nebo <a href="/teplaky-puma/">Puma tepláky</a>.</p>'
          '<h2>Soupravy a kombinace</h2>'
          '<p>Pro děti jsou praktické soupravy, protože se kalhoty i mikina hodí k sobě a rodič nemusí kombinovat. Souprava se hodí do školy i na hřiště, ale po vyprání jedné části se může barva lišit od druhé, proto raději perte obě společně. Chcete-li kombinovat samostatně, zvolte jednobarevné tepláky a k nim <a href="/mikiny/">mikinu</a> s potiskem. Pro aktivnější děti se vyplatí mít dva kusy, aby se při praní daly střídat. Více variant najdete v kategorii <a href="/soupravy/">soupravy</a>.</p>'
          '<h2>Jak dětské tepláky vydrží déle</h2>'
          '<p>Perte je naruby při nízké teplotě a bez aviváže, která zhoršuje savost a ničí elastan. Skvrny od trávy a hlíny nejprve namočte a pak vyperte; nešetřete na pracím prostředku určeném pro barevné prádlo. Vyvarujte se sušičky na vysoký stupeň, při které se látka smršťuje a pas ztrácí pružnost. Dětské kolena lze zpevnit nažehlovací záplatou, pokud tepláky stojí za zachování. Opravené kusy předávejte mladšímu sourozenci, ale nejdřív zkontrolujte pas a šňůrky, aby byly bezpečné.</p>'
          '<h2>Škola, tělocvik a družina</h2>'
          '<p>Do školy se hodí tmavší odstíny, na kterých tolik nevynikne špína, a pevná guma, která zvládne několik hodin sezení a běhání o přestávkách. Pro tělocvik mějte po ruce druhé tepláky, protože ty školní se při hře na zemi rychle zašpiní a vlhké z potu by dítě nemělo nosit zpátky domů. Do družiny a na hřiště funguje jednoduchá pletenina, která se dá vyprat po každém použití bez obav o logo. Pojmenujte kusy fixou na štítku, ať se neztratí v šatně.</p>'
          '<h2>Kdy tepláky doplnit termoprádlem</h2>'
          '<p>Při mrazu stačí pod tepláky obléknout tenké funkční spodky, které odvádějí vlhkost a nevytvářejí další objem v kolenou. Bavlněné spodní kalhoty nasáknou potem a ochladí dítě stejně jako mokrá látka. Tepláky samy nejsou voděodolné, takže na zimní hrátky ve sněhu patří spíš kalhoty s membránou, třeba z výběru <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>. Tepláky se na sníh používají jen na krátkou chvíli a po návratu je dobře usušte.</p>'
          '<h2>Na co si dát pozor při nákupu</h2>'
          '<p>Při koupi online pečlivě porovnejte výšku dítěte s tabulkou prodejce a pamatujte, že dětské označení Y u amerických značek značí roky věku, nikoli velikost. Kontrolujte složení: čistá bavlna se může po praní smrštit, směs s elastanem drží tvar lépe. Prověřte také, zda je v nabídce uvedena zimní varianta s fleecem, protože to bývá zjevné jen z popisu. Výsledek nákupu je lepší, když dítěti tepláky vyzkoušíte přes jeho běžné spodky nebo legíny, které nosí pod nimi, jako ve výběru <a href="/detske-leginy/">dětské legíny</a>.</p>',
    faq=[
        ('Jak vybrat velikost dětských tepláků?', 'Podle výšky dítěte v centimetrech, ne podle věku. Změřte dítě bez bot, porovnejte s tabulkou prodejce a vezměte o číslo větší, pokud chcete rezervu na růst. Manžety nohavice zkrátí.'),
        ('Jsou lepší tepláky s manžetou, nebo s rovnou nohavicí?', 'Manžeta lépe drží a nezachycuje se, hodí se do sportu a k teniskám. Rovná nohavice se lépe obléká a vyhovuje menším dětem. Při volbě záleží na věku dítěte a použití.'),
        ('Z jakého materiálu vybírat dětské tepláky?', 'Na každý den dobře funguje bavlna s polyesterem a trochou elastanu. Na sport zvolte syntetiku, v zimě počesanou pleteninu s fleecem. U citlivé kůže se vyplatí měkká bavlna bez drsných nášivek.'),
        ('Čím se liší chlapecké a dívčí tepláky?', 'Hlavně střihem a barvami. Chlapecké mívají širší boky a volnější nohavice, dívčí užší pas a více odstínů. Pro mladší děti jsou funkčně stejné a dají se sdílet mezi sourozenci.'),
        ('Jak poznat odolné dětské tepláky?', 'Podle hustoty látky a zpevnění v kolenou. Zvedněte látku proti světlu: když prosvítá, rychle se prodře. Dobré jsou dvojité švy, zpevněná kolena a pevná guma v pase.'),
        ('Mohou mít malé děti tepláky se šňůrkou?', 'Pro nejmenší je bezpečnější bez dlouhých konců, které se zachytí o hrazdu nebo kolo. U starších dětí stačí šňůrka zastrčená v pase nebo jen pevná guma bez šňůrky.'),
        ('Jak prát dětské tepláky, aby nepovolil pas?', 'Naruby při nízké teplotě, bez aviváže a bez sušičky na vysoký stupeň. Vysoké teplo poškodí elastan v gumě a tepláky se smrští. Skvrny od trávy nejdřív namočte a pak vyperte.'),
        ('Má smysl kupovat soupravu, nebo samostatné tepláky?', 'Souprava je praktická, když chcete jednotný vzhled bez kombinování. Samostatné tepláky umožní měnit mikiny a lépe se střídají při praní. Souprava se po praní může mírně lišit barevně.'),
        ('Jaké značky mají dětské tepláky v nabídce?', 'Sportovní jako Adidas, Nike, Puma, Under Armour a Kappa, módnější Tommy Hilfiger a Guess, a také Gap, 4F nebo Lotto. Střihy a barvy se liší, proto porovnávejte konkrétní kusy.'),
    ])
