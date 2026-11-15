"""sporteka.cz — wave 26b (16. 11. 2026): long texts for fit-potraviny, posilovaci-veze, zatezove-vesty, gymnasticke-mice.
General true facts only, no prices. Brands linked only where they exist in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ fit-potraviny
NEW['fit-potraviny'] = dict(long=True,
    title='Fit potraviny a arašídová másla: jak číst složení',
    desc='Arašídová másla, proteinové kaše a palačinky, pudinky, sirupy bez cukru a rýžové chlebíčky. Na co se dívat na obalu a kde porovnat nabídky obchodů.',
    intro='<p>Fit potraviny jsou běžné snídaně, svačiny a pomazánky v úpravě, která vyhovuje sportovně založeným lidem: s vyšším podílem bílkovin, bez přidaného cukru nebo s kratším složením. Sporteka tu porovnává nabídky českých obchodů u arašídových a ořechových másel, proteinových palačinek a kaší, proteinových pudinků, sirupů bez cukru a rýžových chlebíčků. Prodává vždy obchod, u kterého se rozhodnete nakoupit; my ukazujeme, kdo co nabízí.</p>'
          '<p>Sortiment je široký a zdaleka ne všechno, co nese slovo „fit“, se od klasických potravin liší. Rozdíly prozradí tabulka nutričních hodnot a seznam složek, a proto se jim podrobně věnuje text pod výpisem. V nabídce se objevují značky jako ' + B(('gymbeam', 'GymBeam')) + ' i čeští výrobci jako Nutrend, Lifelike, Mixit nebo Lyofood.</p>'
          '<p>Jde o potraviny, které doplňují běžný jídelníček, a proto tu najdete jen to, co se hodí jako součást pestré stravy. Doplňky v podobě prášků a tyčinek najdete v souvisejících kategoriích <a href="/proteiny/">proteiny</a>, <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a> a v nadřazené <a href="/sportovni-vyziva/">sportovní výživě</a>.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Potraviny v této kategorii mají jedno společné: nahrazují obvyklou podobu něčeho známého. Místo klasické sladké snídaně proteinová kaše, místo čokoládové pomazánky ořechové máslo, místo džemu nebo medu sirup bez cukru, místo sladkého pečiva rýžový chlebíček. Hranice mezi nimi a sportovní výživou je neostrá. Prášek na kaši nebo palačinky se podobá proteinu, ale má jiné složení a míchá se do jídla, nikoli do šejkru.</p>'
          + T(['Skupina', 'Co to je', 'Na co se dívat'], [
              ['Arašídová a ořechová másla', 'rozemleté arašídy, mandle, kešu nebo lískové ořechy, někdy s přísadami', 'podíl ořechů, přidaná sůl, cukr a palmový olej'],
              ['Proteinové kaše', 'ovesná, rýžová nebo jiná kaše v prášku nebo instantní směs', 'bílkovina na porci, bezlepkovost, obsah cukru'],
              ['Proteinové palačinky a vafle', 'směs na přípravu, do které se přidá voda nebo mléko', 'složení směsi, alergeny, doporučená porce'],
              ['Proteinové pudinky', 'prášek na vaření nebo hotový chlazený dezert', 'sladidla, bílkovina, způsob přípravy'],
              ['Sirupy bez cukru', 'sladké sirupy k polévání palačinek, do kaší a nápojů', 'druh sladidel, aroma, barviva'],
              ['Rýžové chlebíčky', 'lisovaná nafouklá rýže nebo jiné obilí', 'sůl, příchuť, velikost balení']]) +
          '<h2>Arašídová a ořechová másla</h2>'
          '<p>Arašídové máslo je nejznámější pomazánka ze světa fitness. Základem jsou pražené arašídy, které se melou, dokud nevznikne hladká, případně jemně zrnitá hmota. Podle struktury se dělí na krémové a křupavé (crunchy) s kousky arašídů. Kromě nich se prodávají másla z mandlí, kešu, lískových oříšků nebo kombinace několika druhů. Botanicky patří arašídy mezi luštěniny, v obchodě se ale řadí k ořechům a skladují se stejně jako ony.</p>'
          '<p>Nejdůležitější je složení. Nejjednodušší máslo obsahuje jen arašídy, někdy špetku soli. Levnější a sladší varianty přidávají cukr, rostlinné tuky nebo palmový olej, který brání odlučování oleje. U másla bez stabilizátoru se olej při skladování odděluje a drží se na povrchu; před použitím stačí máslo promíchat. Je to normální a neznamená to, že je zkažené. Proteinová másla mají v receptuře navíc bílkovinný koncentrát, takže jsou hustší a obsahují víc bílkovin na porci; jejich složení ale bývá delší.</p>'
          '<p>Ořechová másla jsou energeticky vydatná, protože ořechy obsahují hodně tuku. Porce se obvykle uvádí kolem 20–30 g, tedy přibližně jedna až dvě lžíce. Při porovnávání proto čtěte hodnoty na 100 g i na porci a odhadněte, kolik másla skutečně sníte. Hodí se jako součást pestré stravy, třeba na toast, do kaše nebo do smoothie.</p>'
          '<p>Důležité upozornění: arašídy i ořechy patří mezi hlavní alergeny. Na obalu hledejte tučně vyznačené složky a větu o možných stopách. Pokud někdo v domácnosti alergii má, nestačí se spolehnout na to, že máslo je z jiného druhu ořechu, protože zpracování často probíhá na společné lince.</p>'
          '<h2>Proteinové kaše a palačinky</h2>'
          '<p>Proteinová kaše je obvykle instantní směs ovesných nebo rýžových vloček s přidaným mléčným, sójovým nebo rostlinným proteinem. Zalije se horkou vodou nebo mlékem a za pár minut je hotová. Palačinkové směsi fungují podobně, jen se z nich smaží palačinky nebo pečou vafle ve vaflovači. Na rozdíl od klasických směsí mají vyšší podíl bílkovin a často kratší nebo odlišné složení.</p>'
          '<p>Při srovnání hledejte údaje, které se dají porovnat. Výrobci někdy uvádějí bílkovinu na 100 g prášku, jindy na hotovou porci po rozmíchání s mlékem. Dvě kaše tak mohou vypadat stejně, i když u jedné je hodnota počítaná s mlékem a u druhé jen s práškem. Přepočtěte si, kolik gramů prášku tvoří jednu porci, a porovnávejte bílkovinu na tuto porci. Mezi příchutěmi se liší i obsah cukru, takže se vyplatí otevřít tabulku u konkrétní příchutě, ne jen u té, kterou obchod ukazuje jako první.</p>'
          '<p>Ovesné vločky často obsahují stopy lepku, protože se oves při pěstování a zpracování mísí s pšenicí. Bezlepkové kaše musí být na obalu výslovně označené, ideálně přeškrtnutým klasem. Rýžové kaše jsou bezlepkové přirozeně. Při alergii na mléko hledejte rostlinné bílkoviny, například z hrachu nebo rýže, a kontrolujte, zda směs neobsahuje i syrovátku.</p>'
          '<h2>Proteinové pudinky</h2>'
          '<p>Proteinový pudink se prodává buď jako prášek, který se rozmíchá v mléce a zahřeje do zhoustnutí, nebo jako hotový chlazený dezert v kelímku. Z prášku si pudink připravíte doma a dá se použít i jako náplň do dortů nebo přimíchat do jogurtu. Chlazené pudinky se musí převážet v chladu a mají krátkou trvanlivost, proto je e-shopy nabízejí jen výjimečně a častější jsou trvanlivé pudinky v prášku.</p>'
          '<p>Vždy si zjistěte, čím je pudink dochucený a oslazený. Mnohé proteinové pudinky obsahují náhradní sladidla místo cukru, takže jsou sladké bez dalších kalorií z cukru. Pokud vám sladidla nevyhovují, vybírejte kratší složení nebo ochucení kakaem a vanilkou. Při domácí přípravě prášek ve studeném mléce důkladně rozmíchejte, jinak se tvoří hrudky.</p>'
          '<h2>Sirupy bez cukru a jak jsou oslazené</h2>'
          '<p>Sirupy bez cukru se používají k polití palačinek, do kaší, jogurtů nebo do nápojů. Chuť javorového sirupu, karamelu, čokolády nebo vanilky jim místo cukru dodávají aromata a sladidla. Hustotu zajišťují zahušťovadla, například gumy nebo vláknina.</p>'
          '<p>Nejčastější sladidla v těchto produktech jsou sukralóza, steviol glykosidy (výtažek ze stévie), acesulfam K, aspartam, cyklamát nebo cukerné alkoholy, jako je erythritol, xylitol nebo maltitol. Všechna smějí být v EU použita jen po schválení a v seznamu složek se uvádějí jako „sladidlo“ s názvem nebo číslem E. Chuť se liší: někdo cítí u stévie hořkou dochuť, jiný u sukralózy nic. Cukerné alkoholy ve větším množství mohou působit projímavě, a proto na obalu bývá upozornění. V praxi se proto vyplatí vybrat si jeden sirup, vyzkoušet ho v malém balení a teprve potom kupovat větší.</p>'
          '<p>Označení „bez cukru“ neznamená, že sirup nemá žádnou energii. Cukerné alkoholy a zahušťovadla nějakou energii mají. Přesné údaje najdete v řádku energie a sacharidů na 100 g.</p>'
          '<h2>Rýžové chlebíčky</h2>'
          '<p>Rýžový chlebíček vzniká tak, že se rýže ve formě zahřeje a nafoukne; výsledkem je lehký křupavý kruh. Dobře se přenáší, vydrží několik týdnů a podle příchuti si můžete vybrat sladkou, nebo slanou verzi. Základní varianta obsahuje rýži a případně sůl, ochucené varianty mají čokoládovou polevu, jogurtový povlak nebo koření.</p>'
          '<p>Hmotnost jednoho kusu se liší, často jde o 6–10 g. Nutriční hodnoty se proto vztahují na porci o dvou nebo třech chlebíčcích. Slané verze obsahují víc soli, a pokud je mažete arašídovým máslem, celkové množství soli ještě vzroste. Chlebíčky s polevou jsou spíš sladkost než základ svačiny.</p>'
          '<h2>Jak číst štítek, aby srovnání dávalo smysl</h2>'
          '<p>Základem je nutriční tabulka. Ve všech kategoriích platí podobné pořadí kroků:</p>'
          '<ol><li><b>Velikost porce.</b> Jeden výrobce uvádí 30 g, jiný 50 g. Čísla na porci se proto nedají přímo porovnat.</li>'
          '<li><b>Bílkoviny.</b> Hledejte množství na porci i na 100 g a všímejte si, z čeho pocházejí (mléko, vejce, rostliny).</li>'
          '<li><b>Cukry.</b> V řádku „z toho cukry“ jsou přirozené cukry z mléka nebo ovoce i přidané. Přidaný cukr se pozná podle seznamu složek.</li>'
          '<li><b>Seznam složek.</b> Složky jsou seřazené sestupně podle množství. Pokud je cukr nebo palmový olej hned za arašídy, vyšší podíl ořechů nečekejte.</li>'
          '<li><b>Alergeny.</b> Vyznačují se tučně. Pozor také na upozornění „může obsahovat stopy“.</li>'
          '<li><b>Trvanlivost a skladování.</b> Po otevření většinou stačí chladnější tmavé místo, másla bez konzervantů je vhodné spotřebovat během několika týdnů až měsíců.</li></ol>'
          '<p>Při porovnání nabídek v tabulce nad výpisem hledejte vždy cenu za kilogram, ne jen za balení. Tak snadno srovnáte i dvě různě velká balení téhož másla. Sporteka nabídky jen porovnává, objednáváte přímo v obchodě, který vás osloví nejvíc.</p>'
          '<h2>Jak je zařadit do jídelníčku</h2>'
          '<p>Potraviny z této kategorie nenahrazují běžné jídlo a nejsou ani zázrakem. Jsou to hotové polotovary, které šetří čas při přípravě snídaně nebo svačiny a hodí se k pestré stravě, ve které převládá čerstvá zelenina, ovoce, maso, ryby, luštěniny a celozrnné přílohy. Neslibují hubnutí ani svalový přírůstek. Pokud řešíte konkrétní jídelníček s ohledem na zdravotní stav, proberte ho s dietologem nebo lékařem.</p>'
          '<p>Praktická pravidla: vybírejte potraviny, které vám chutnají, protože jen ty vás u pravidelného stravování udrží dlouhodobě. Kupujte nejdřív malé balení, než se rozhodnete pro pětikilovou verzi. Hlídejte, jak velké porce skutečně jíte. A příchutě střídejte, aby se vám snídaně neomrzela.</p>'
          '<p>Chcete-li bílkoviny doplnit nápojem z prášku, podívejte se na <a href="/proteiny/">proteiny</a>. K rychlé svačině mezi jídly se hodí <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>. Přehled celého sortimentu najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>',
    faq=[
        ('Z čeho se vyrábí arašídové máslo?', 'Základem jsou pražené arašídy rozemleté na pastu. Kvalitnější másla obsahují jen arašídy, případně špetku soli. Levnější přidávají cukr, rostlinné tuky nebo palmový olej, aby se olej neodlučoval.'),
        ('Proč se na másle odlučuje olej?', 'Pokud máslo neobsahuje stabilizátor, olej se časem usadí na povrchu. Stačí ho promíchat a máslo je v pořádku. V chladnější místnosti nebo při skladování dnem vzhůru se olej odlučuje méně.'),
        ('Je arašídové máslo vhodné pro alergiky?', 'Ne. Arašídy i ořechy jsou závažné alergeny. Na obalu hledejte vyznačené složky a upozornění na možné stopy. Při alergii se vyhněte i máslům z jiných druhů ořechů, pokud výrobce nezaručí oddělenou výrobu.'),
        ('Jak poznat dobrou proteinovou kaši?', 'Porovnejte bílkovinu na porci (při stejném způsobu přípravy), cukr a délku složení. Pokud potřebujete bezlepkovou kaši, musí to obal výslovně uvádět.'),
        ('Mají proteinové palačinky nižší energetickou hodnotu než běžné?', 'Nemusí. Vyšší podíl bílkovin neznamená nižší energii. Záleží na složení směsi a na tom, co do těsta přidáte. Proto se dívejte na hodnoty na porci.'),
        ('Jaká sladidla jsou v sirupech bez cukru?', 'Nejčastěji sukralóza, steviol glykosidy, acesulfam K, aspartam nebo cukerné alkoholy jako erythritol. Seznam složek je uvádí jako „sladidlo“ s názvem. Chuť je individuální, proto zkuste nejdřív malé balení.'),
        ('Jak dlouho vydrží otevřené balení?', 'Řiďte se pokyny na obalu. Másla a sirupy se obvykle skladují v chladu a suchu a po otevření se spotřebují během několika týdnů až měsíců. Prášky na vlhku tvrdnou, proto balení zavřete hned po použití.'),
        ('Jsou rýžové chlebíčky bezlepkové?', 'Rýže je bezlepková přirozeně, ale chlebíček může obsahovat jiné složky nebo stopy lepku z výroby. Hledejte přeškrtnutý klas a informace o výrobě.')])

# ------------------------------------------------------------------ posilovaci-veze
NEW['posilovaci-veze'] = dict(long=True,
    title='Posilovací věže a multistanice: jak vybrat a umístit',
    desc='Posilovací věže, multistanice a domácí fitness stroje. Zátěž, rozměry, nastavení a bezpečnost; porovnání nabídek českých obchodů.',
    intro='<p>Posilovací věž je pevný rám, na kterém se dá cvičit hned několik cviků bez dalšího vybavení: shyby, kliky na bradlech a zvedání nohou, někdy i dipy a šikmé kliky. Zabere málo místa, a proto je oblíbená v bytech, garážích a malých domácích posilovnách. Multistanice jde dál a přidává kladkový systém s odporem, nejčastěji ve formě závaží nebo tyče s kotouči. Sporteka porovnává nabídky českých obchodů a kupujete přímo v obchodě, který vám vyhovuje.</p>'
          '<p>Nabízejí se věže od značek ' + B(('hms', 'HMS'), ('insportline', 'Insportline')) + ' a také od dalších výrobců, například Master, Vifito, Finnlo nebo Hammer. Další vybavení pro cvičení s vlastní vahou najdete v kategorii <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</p>'
          '<p>Při výběru zvažte, co chcete cvičit, kolik máte místa a kolik váží cvičenec. Níže najdete přehled typů, parametrů a pravidel bezpečného používání.</p>',
    guide='<h2>Věž, multistanice, nebo klec?</h2>'
          '<p>V obchodech se názvy často zaměňují, konstrukce se ale opravdu liší. Když rozdíly znáte, snáz se zorientujete už při prvním výběru.</p>'
          + T(['Typ', 'Co obsahuje', 'Hodí se pro'], [
              ['Posilovací věž (power tower)', 'rám se hrazdou, bradly na dipy a opěrkou zad pro zvedání nohou', 'cvičení s vlastní vahou, kalisteniku, domácí tréninkový koutek'],
              ['Multistanice s kladkami', 'věž nebo rám s lany, kladkami a závažím nebo tyčí', 'celotělové posilování na jednom místě'],
              ['Multistanice s deskami', 'místo skládaného závaží se na tyč nasazují kotouče', 'ti, kdo už mají kotouče a potřebují zvyšovat zátěž jemněji'],
              ['Silová klec (power rack)', 'čtyři sloupky s pojistkami pro činky', 'těžké dřepy, benchpress a mrtvý tah'],
              ['Rohová věž', 'rám postavený do rohu místnosti, často s lanovým systémem', 'malé prostory']]) +
          '<p>Silová klec a posilovací stroje jsou samostatné kategorie. Pokud plánujete cvičit s velkými činkami, prohlédněte si <a href="/posilovaci-stroje/">posilovací stroje</a> a <a href="/cinky-a-kotouce/">činky a kotouče</a>. Pro cvičení s vlastní vahou stačí věž nebo samostatná <a href="/hrazdy-a-bradla/">hrazda a bradla</a>.</p>'
          '<h2>Věž na cvičení s vlastní vahou</h2>'
          '<p>Klasická posilovací věž stojí na zemi, takže se nemusí připevňovat ke zdi ani ke stropu. Rám tvoří ocelové profily a podpírá ho široká základna. Nahoře je hrazda, někdy s několika úchopy (široký, úzký, neutrální). Dole jsou dvě madla nebo bradla pro dipy a kliky a polstrovaná zádová opěrka s podpěrami loktů pro zvedání nohou nebo kolen k tělu.</p>'
          '<p>Na jedné věži můžete cvičit shyby, vzpory, kliky, zvedání nohou, australské shyby na nízké hrazdě a kombinace s gumami nebo závažím. Cviků je méně než na stroji s kladkami, pro základní sílu to ale stačí. Obtížnost můžete dál zvýšit zátěžovou vestou nebo odporovou gumou. O vestách píšeme v kategorii <a href="/zatezove-vesty/">zátěžové vesty</a>.</p>'
          '<h2>Multistanice a odpor</h2>'
          '<p>Multistanice nahrazuje několik strojů v posilovně. Pomocí kladek a lan se tah ze závaží přenáší na madla, takže se cvičí stahování k hrudi, veslování, tlaky, bicepsové zdvihy, tricepsové stahy a podobné cviky. Odpor může mít dvě podoby.</p>'
          '<ul><li><b>Skládané závaží (weight stack).</b> Sloupec desek, ve kterém se kolíkem nastaví požadovaná hmotnost. Nastavení je rychlé a bezpečné, ale zátěž roste po krocích, často po pěti nebo deseti kilogramech.</li>'
          '<li><b>Deskové (plate loaded) systémy.</b> Na tyč se nasazují kotouče. Zátěž se mění po malých krocích, potřebujete ale vlastní kotouče a při každé změně je musíte přenášet.</li></ul>'
          '<p>Pokud kupujete multistanici poprvé, vyberte takovou, která vám bude stačit. Lehčí sada závaží začátečníkům vyhovuje, rychle ji ale přerostou. Vyplatí se proto zjistit, zda jde závaží dokoupit, případně vyměnit za těžší.</p>'
          '<h2>Nosnost, rozměry a stabilita</h2>'
          '<p>Maximální nosnost uvádí výrobce v kilogramech. Berte ji jako hranici, ne jako cíl. Při dynamických cvicích, jako jsou shyby se švihem (kipping) nebo zvedání nohou, působí na rám větší síla, než odpovídá samotné hmotnosti těla. Pokud se vaše hmotnost blíží limitu, vyberte odolnější model. Zvlášť se uvádí nosnost závaží nebo tyče, u multistanice velmi důležitá.</p>'
          '<p>Rozměry zjistěte před objednávkou. Sestavená věž měří na výšku zhruba dva metry i víc, takže se musí vejít pod strop. Měřte nejen výšku místnosti, ale i prostor nad hrazdou, protože při shybu se hlava dostává nad úchop. Kolem věže nechte volný prostor na každé straně aspoň jeden metr. U multistanice počítejte s tím, že lana a madla potřebují prostor i do šířky.</p>'
          '<p>Stabilitu zvyšuje široká základna, protiskluzové nožky a zátěž ve spodní části. Spoje by měly být svařené nebo stažené pevnými šrouby. Po prvním použití a znovu po několika týdnech dotáhněte matice, protože se vibracemi povolují. Pokud se rám při shybu viditelně chvěje, je špatně sestavený nebo příliš lehký.</p>'
          '<h2>Nastavitelnost a ergonomie</h2>'
          '<p>Dobrá věž se dá přizpůsobit výšce cvičence. Bradla a opěrka by měla mít několik poloh, aby při vzporu zůstával loket pod ramenem. Madla na hrazdě by měla mít protiskluzový povrch a pěnový potah, který nedře dlaně. Multistanice by měla mít polohovatelné sedadlo a opěrku zad a přesunutelné kladky, jinak se dráha pohybu nastavuje nepohodlně.</p>'
          '<p>Zkontrolujte také lana a jejich uchycení: podívejte se, zda výrobce uvádí nosnost kladek a zda lze lano později vyměnit. U kladek se vyplatí podívat se na ložiska, díky nimž je chod plynulý a tichý.</p>'
          '<h2>Bezpečnost a údržba</h2>'
          '<ul><li>Před každým cvičením se podívejte, zda nejsou povolené šrouby a zda se rám nehýbá.</li>'
          '<li>Při dipech a shybech zvolte prostor bez předmětů, na které byste mohli spadnout.</li>'
          '<li>Pro těžší cviky mějte spolucvičence nebo použijte pojistky, kde to konstrukce umožňuje.</li>'
          '<li>Postavte věž na rovnou a pevnou podlahu. Na koberci se rám může naklánět, pod nožky se vyplatí podložka.</li>'
          '<li>Lana a kladky občas zkontrolujte, roztřepená nebo poškozená lana vyměňte.</li>'
          '<li>Dbejte na pravidelnou rozcvičku a techniku. Nepřeceňujte své síly, zvláště po delší pauze.</li></ul>'
          '<p>Pokud máte zdravotní omezení, poraďte se před zahájením tréninku s lékařem nebo trenérem. Údržba spočívá v utírání potu z potahů, občasném promazání pohyblivých částí a kontrole spojů.</p>'
          '<h2>Pořadí cvičení a týdenní plán</h2>'
          '<p>Věž i multistanici nejlépe využijete, když máte jednoduchý plán. Začátečník může cvičit dvakrát až třikrát týdně celé tělo: nejdřív tahové cviky (shyby nebo stahování k hrudi), pak tlakové (kliky, dipy, tlaky), nakonec trup a nohy. Mezi tréninky nechte aspoň jeden den volna, aby se svaly a šlachy zotavily. Pokud zvládáte plný počet opakování ve všech sériích bez zhoršení techniky, přidejte zátěž nebo opakování, ne obojí najednou.</p>'
          '<p>U věže se obtížnost mění úhlem těla a rozsahem pohybu. Kliky na zvýšených madlech jsou lehčí než kliky s nohama výš, shyby s gumou pod koleny jsou lehčí než shyby bez ní. Bez dalšího vybavení tak zvládnete postup od úplných začátků až k pokročilým cvikům. U multistanice se postupuje po stupních závaží; jednotlivé cviky si zapisujte, jinak pokrok z týdne na týden špatně uhlídáte.</p>'
          '<h2>Co v nabídce porovnávat kromě parametrů</h2>'
          '<p>Při srovnání pomůže jednoduchý seznam. Zkontrolujte nosnost uživatele a zátěže, rozměry v sestaveném stavu, počet úchopů na hrazdě, polstrování madel, nastavitelnost a obsah balení včetně nářadí. U multistanic zjistěte, zda je v ceně sedadlo, kladky, lana a madla, nebo se dokupují zvlášť. Čtěte popis montáže: některé rámy přicházejí částečně smontované a stavba je rychlá, jiné se skládají z desítek dílů. Zjistěte také, kdo těžký balík doveze a zda obchod zajistí odvoz zpět, kdyby zboží dorazilo poškozené.</p>'
          '<h2>Kam věž postavit</h2>'
          '<p>Nejvhodnější je garáž, sklep, pokoj s pevnou podlahou nebo balkon pod střechou. V bytě pod věž dejte gumovou podložku, která chrání podlahu a tlumí vibrace i hluk při seskoku. Dávejte pozor na výšku stropu a lustr, protože při shybu se hlava zvedá výš než při stoji. Rozebírání a skládání rámu je pracné, takže místo vyberte s rozmyslem – stěhovat ho často nebudete chtít.</p>'
          '<h2>Jak se rozhodnout</h2>'
          '<p>Rozhodujte podle cíle. Pokud chcete jen shyby, kliky a cviky na břicho, stačí věž. Pokud chcete také kladkové cviky a nemáte kotouče ani činky, hledejte multistanici se závažím. Potřebujete-li těžké dřepy a tlaky, sáhněte po kleci a <a href="/posilovaci-lavice/">posilovací lavici</a>. Menší doplňky, například gumy, najdete v kategorii <a href="/funkcni-trenink/">funkční trénink</a>.</p>'
          '<p>Při porovnání nabídek nehleďte jen na cenu. Zjistěte dobu dodání, možnost vrácení zboží poškozeného při přepravě (rám může vážit desítky kilogramů), dostupnost náhradních dílů a záruku. Sporteka ukazuje nabídky českých obchodů a objednáváte přímo v obchodě. Sestavení trvá obvykle několik hodin, proto počítejte s pomocníkem a se sadou klíčů.</p>',
    faq=[
        ('Jaký je rozdíl mezi posilovací věží a multistanicí?', 'Věž slouží ke cvičení s vlastní vahou: shyby, dipy, zvedání nohou. Multistanice má kladky a závaží nebo tyč s kotouči a umožňuje klasické posilovací cviky s odporem.'),
        ('Unese věž dospělého muže o hmotnosti kolem 100 kg?', 'Záleží na modelu. Řiďte se maximální nosností uvedenou výrobcem a nechte si rezervu, zvlášť pokud budete cvičit dynamické cviky nebo přidáte zátěžovou vestu.'),
        ('Kolik místa potřebuje posilovací věž?', 'Pro základnu zhruba metr na metr a kolem ní aspoň metr volného místa. Důležitá je výška místnosti: věž bývá přes dva metry a nad hrazdou musíte mít prostor na shyb.'),
        ('Je lepší skládané závaží, nebo kotouče?', 'Závaží se mění rychle a bezpečně, ale po krocích. Kotouče dávají jemnější přírůstky, ale vyžadují vlastní kotouče a více manipulace. Začátečníkovi obvykle vyhovuje závaží.'),
        ('Dá se věž připevnit ke zdi?', 'Samostatná věž se ke zdi nepřipevňuje, stojí na vlastní základně. Hrazdy a rámy určené k montáži na zeď jsou jiný typ výrobku; u nich dbejte na materiál zdi a vhodné hmoždinky.'),
        ('Co se dá na věži cvičit?', 'Shyby, kliky na bradlech, dipy, zvedání nohou nebo kolen a variace s gumovým odporem. Multistanice přidává stahování, veslování, tlaky a bicepsové a tricepsové cviky.'),
        ('Jak věž sestavit sám?', 'Vyhraďte si několik hodin a pomocníka, protože díly jsou těžké. Šrouby nejdřív utahujte lehce, až po složení celého rámu je dotáhněte pevně, a po týdnu je zkontrolujte znovu.')])

# ------------------------------------------------------------------ zatezove-vesty
NEW['zatezove-vesty'] = dict(long=True,
    title='Zátěžové vesty: kolik kg zvolit a na co dávat pozor',
    desc='Zátěžové vesty pro běh, kalisteniku a trénink s vlastní vahou. Jak vybrat hmotnost, střih a materiál a porovnat nabídky českých obchodů.',
    intro='<p>Zátěžová vesta je přiléhavý kus oblečení se zátěží rozloženou na hrudi a zádech. Přidává odpor při klasických cvicích, aniž byste museli držet činky nebo nosit batoh. Hodí se na shyby, kliky, dřepy, chůzi do schodů, běh a kalisteniku. Sporteka porovnává nabídky českých obchodů a vestu si objednáte přímo v obchodě, který vás osloví.</p>'
          '<p>Nejvíc vest prodávají značky ' + B(('hms', 'HMS'), ('merco', 'Merco'), ('gymbeam', 'GymBeam'), ('insportline', 'Insportline')) + ', dále se objevují Sportago, Tunturi, Virtufit nebo DBX Bushido. Vesty se liší hmotností, tím, zda je zátěž pevná, nebo odnímatelná, i střihem.</p>'
          '<p>Vybírejte podle toho, co s vestou budete dělat. K ostatním pomůckám pro trénink s vlastní vahou se dostanete v kategorii <a href="/funkcni-trenink/">funkční trénink</a>.</p>',
    guide='<h2>K čemu zátěžová vesta slouží</h2>'
          '<p>Princip je jednoduchý: tělo váží pořád stejně, takže zátěž při cvicích s vlastní vahou po čase přestane stačit. Vesta přidá kilogramy, takže stejný shyb, klik nebo výpad je těžší. Zátěž je u těla, nerozkývá se jako činka, a dá se použít při pohybech, které by s činkami v rukou nešly, například při shybech nebo na bradlech.</p>'
          '<p>Hodí se k těmto činnostem:</p>'
          '<ul><li><b>Kalistenika a shyby.</b> Přidaná hmotnost u shybů, dipů a kliků.</li>'
          '<li><b>Dřepy, výpady a chůze do schodů.</b> Zátěž pomáhá zvyšovat odpor bez činek v rukou.</li>'
          '<li><b>Chůze a pochod s vestou.</b> Lehká zátěž přidá intenzitu při obyčejné procházce.</li>'
          '<li><b>Funkční trénink a cvičení v přírodě.</b> Vesta se nosí pod batohem nebo bez něj.</li>'
          '<li><b>Hasičská a vojenská příprava, soutěže.</b> Vesty se vyrábějí v různých hmotnostech.</li></ul>'
          '<p>Začátečníkům často víc vyhovuje cvičení s oporou hrazdy nebo věže. K tomu se hodí <a href="/hrazdy-a-bradla/">hrazdy a bradla</a> nebo <a href="/posilovaci-veze/">posilovací věže</a>.</p>'
          '<h2>Pevná, nebo nastavitelná zátěž</h2>'
          '<p>Základní rozdělení vest je podle toho, jak se zátěž mění.</p>'
          + T(['Typ', 'Jak funguje', 'Výhody a omezení'], [
              ['Pevná zátěž', 'zátěž je zašitá a nelze ji vyndat', 'jednodušší, často levnější; hmotnost nelze měnit'],
              ['Nastavitelná zátěž', 'kapsy na pytlíky s pískem nebo kovové destičky, které se vyndávají', 'dá se zvyšovat po malých krocích, hodí se na dlouhodobou progresi'],
              ['Vesta se zátěží z kovových plátů', 'tenké destičky v kapsách po celé vestě', 'slušně přiléhá, rozložení je pravidelné'],
              ['Vesta ve stylu plate carrier', 'taktická nosná vesta, do které se vkládají desky', 'vhodné pro vojenské a taktické použití'],
              ['Pásek a manžety', 'zátěž na pas, na kotníky nebo zápěstí', 'doplněk, ne náhrada vesty']]) +
          '<p>Nastavitelná vesta stojí obvykle víc, ale vyplatí se, pokud chcete zvyšovat odpor postupně. Pevná zátěž je jednodušší a pro krátké cvičení stačí. Zjistěte u konkrétního produktu, jaká zátěž je v balení, po kolika kilogramech se dá měnit a zda se dají dokoupit další pytlíky nebo destičky.</p>'
          '<h2>Jakou hmotnost zvolit</h2>'
          '<p>Hmotnost se uvádí v kilogramech a v nabídce jsou vesty zhruba od několika kilogramů po dvacet i více. Obecné pravidlo je začít nízko. Zátěž, která vypadá zanedbatelně, při desítkách opakování zatěžuje klouby, páteř a šlachy víc, než by člověk čekal.</p>'
          '<p>Za rozumné se obvykle považuje začít s malým zlomkem tělesné hmotnosti a přidávat po malých krocích, jen pokud se technika cviků nezhoršuje. U běhu a skoků buďte opatrní dvojnásob, protože síla dopadu se násobí. Při chůzi je tolerance větší než při běhu. Rozhodně nezačínejte těžkou vestou a mějte na paměti, že s únavou se technika zhoršuje.</p>'
          '<p>Nastavitelná vesta umožňuje postup po kilogramu nebo dvou. Pokud kupujete pevnou, je lepší zvolit nižší hmotnost a časem dokoupit těžší vestu než hned sáhnout po příliš těžké.</p>'
          '<h2>Střih, velikost a pohodlí</h2>'
          '<p>Vesta se musí držet u těla. Pokud se pohybuje, zátěž naráží do hrudníku a dráždí kůži. Dobrý střih má upravitelné popruhy v pase a na ramenou, aby ji šlo nastavit přesně. Zátěž má být rozložena mezi předek a záda stejnoměrně, jinak se tělo naklání. Ramenní část by neměla tlačit, jinak omezuje pohyb při shybech.</p>'
          '<p>Dávejte pozor na velikost. Některé vesty jsou unisex a jedna velikost sedí širokému rozsahu postav. Jiné se prodávají v několika velikostech. Pokud si velikostí nejste jistí, změřte si obvod hrudníku a pasu a porovnejte ho s tabulkou výrobce. Dámské modely mívají užší střih, kratší délku a vykrojená ramena.</p>'
          '<p>Při cvičení v teple bývá problémem pot. Hledejte prodyšný materiál na zádech a vnitřní podšívku, která se dá vyprat nebo setřít. Kožené nebo silné nylonové vesty jsou odolné, ale hůře větrají.</p>'
          '<h2>Materiál a zpracování</h2>'
          '<p>Nejčastěji se používá nylon nebo polyester v silnější tkanině, která odolá odírání. Zátěž tvoří železný nebo ocelový granulát, písek nebo kovové destičky, někdy ve vodotěsných pytlících. U vest s pískem se vyplatí kapsy, které se dobře zapínají suchým zipem nebo zipem, aby se pytlíky nevysypaly. Švy by měly být zdvojené, zejména na ramenou, kde působí největší tah.</p>'
          '<p>Kovové součásti, například přezky a zipy, by neměly rezavět. Pokud vestu necháváte venku, hlídejte, aby zátěž nenavlhla. Praní se řídí návodem, většinou se sundá zátěž a pere se jen textilní obal.</p>'
          '<h2>Bezpečnost a postupné zvyšování zátěže</h2>'
          '<ul><li>Začněte s krátkými tréninky a nízkou hmotností a sledujte, jak na zatížení reagují záda, kolena a kotníky.</li>'
          '<li>Hmotnost zvyšujte po malých krocích a jen tehdy, když technika zůstává čistá.</li>'
          '<li>Vestu nepoužívejte při každém cvičení. Střídejte dny se zátěží a bez ní, aby se tělo zotavilo.</li>'
          '<li>Při běhu a skocích počítejte se zvýšeným nárazem. Je rozumné začít chůzí.</li>'
          '<li>Dlouhé nošení těžké vesty může zatěžovat páteř. Pokud cítíte bolest, vestu odložte.</li>'
          '<li>Při potížích s páteří, srdcem, tlakem nebo klouby se předem poraďte s lékařem.</li></ul>'
          '<p>Děti a dospívající by bez odborného vedení těžké vesty používat neměli. Pro základní cvičení stačí vlastní váha a nízká zátěž.</p>'
          '<h2>Příklad postupného zvyšování zátěže</h2>'
          '<p>Předpokládejme cvičence, který zvládá dvacet kliků a deset shybů. Vestu s nízkou hmotností si nasadí nejdřív na chůzi nebo na pomalé dřepy a po týdnu přidá kliky. Pokud všechny série dokáže odcvičit stejně čistě jako bez vesty, přidá další zátěž u nastavitelného modelu, nebo přejde na těžší kus u pevné vesty. Do cviků, kde záleží na rychlosti a skocích, například skoky na bednu, vestu zařazuje až nakonec a s nejnižší zátěží. Takové zvyšování může trvat týdny až měsíce, a to je normální.</p>'
          '<p>Tělo si na zátěž zvyká postupně. Šlachy a vazy se přizpůsobují pomaleji než svaly, takže pocit síly může předbíhat skutečnou připravenost. Proto se vyplatí zapisovat si zátěž, počet opakování a to, jak se druhý den cítíte. Bolest v kloubech je signál ke snížení zátěže, ne k tvrdohlavému pokračování.</p>'
          '<h2>Vesta, nebo batoh či činky</h2>'
          '<p>Někdo začíná s batohem naplněným knihami nebo lahvemi s vodou. Je to levné, ale zátěž se v batohu posouvá a tlačí na ramena. Vesta rozkládá hmotnost rovnoměrně a lépe drží. Činky v rukou zase zatěžují úchop a omezují pohyb při shybech. Vesta je tedy praktická hlavně tam, kde potřebujete mít ruce volné. Pro cviky, které vyžadují přesně odměřenou zátěž v rukou, jsou lepší <a href="/kettlebelly/">kettlebelly</a> nebo činky.</p>'
          '<h2>Na co si dát pozor při koupi</h2>'
          '<p>U inzerované hmotnosti ověřte, zda zahrnuje jen zátěž, nebo i vestu samotnou. Zjistěte, jestli je zátěž rozložena symetricky a zda se pytlíky nepřesouvají. Prohlédněte fotografie švů a popruhů, u nastavitelných modelů se ptejte na velikost jednoho dílku zátěže. Některé obchody uvádějí rozsah obvodu hrudníku, pro který je vesta navržena. A všímejte si zápachu nového materiálu: silný chemický pach u levnějších vest po vyvětrání obvykle zmizí, ale je dobré to mít na paměti.</p>'
          '<p>Pokud vestu kupujete jako dárek, raději zvolte nastavitelnou, protože správnou hmotnost obdarovaný ještě nezná. Vyšší pořizovací cenu nastavitelné vesty časem obvykle vyrovná delší využití.</p>'
          '<p>Před každým tréninkem se krátce rozcvičte: zakružte rameny, kyčlemi a kotníky a udělejte několik lehkých sérií bez vesty. Tělo se tak připraví na zátěž a pohyby budou jistější.</p>'
          '<h2>Co dalšího se k vestě hodí</h2>'
          '<p>Při cvičení s vestou se vyplatí vhodná podložka, protože při kleku a výpadech tlačí kolena. Podložky najdete v kategorii <a href="/joga-a-podlozky/">jóga a podložky</a>. Pokud trénujete s hrazdou nebo bradly, projděte si i <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>. Při silovém tréninku vestu dobře doplní <a href="/kettlebelly/">kettlebelly</a> nebo <a href="/cinky-a-kotouce/">činky a kotouče</a>.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů; hmotnost zátěže, možnost jejího nastavení, materiál a záruku si ale před koupí ověřte přímo u obchodu. U vesty s fixní zátěží je vhodné spočítat, jestli hmotnost, kterou berete, odpovídá vašemu tréninku i za měsíc nebo dva.</p>',
    faq=[
        ('Jakou hmotnost zátěžové vesty zvolit na začátek?', 'Raději nižší, tedy jen malý zlomek tělesné hmotnosti. Zátěž zvyšujte postupně a jen tehdy, když si udržíte správnou techniku. Nastavitelná vesta usnadňuje malé kroky.'),
        ('Je lepší pevná, nebo nastavitelná vesta?', 'Pro dlouhodobý trénink nastavitelná, protože zátěž můžete zvyšovat po kilogramech. Pevná je jednodušší a stačí na krátké nebo příležitostné použití.'),
        ('Dá se s vestou běhat?', 'Ano, ale opatrně. Zátěž násobí náraz při dopadu na klouby, proto začněte chůzí a krátkými úseky. Vesta musí dobře přiléhat k tělu, aby se nehoupala.'),
        ('Pro koho jsou zátěžové vesty vhodné?', 'Pro cvičence, kteří zvládají základní cviky s vlastní vahou a chtějí je ztížit. Pro úplné začátečníky a děti se nehodí. Při zdravotních potížích se poraďte s lékařem.'),
        ('Jak vestu vyprat?', 'Podle návodu. Většinou se vyndá zátěž a pere se jen textilní obal na nižší teplotu bez aviváže. Zátěž s pískem ani kovy do pračky nepatří.'),
        ('Kolik by měla vesta vážit vzhledem k mé váze?', 'Pevné procento nelze říct. Záleží na zkušenostech, cviku a zdravotním stavu. Vyjděte z toho, že cvik musí zůstat technicky čistý a že zátěž zvyšujete po malých krocích.'),
        ('Hodí se zátěžová vesta pro ženy?', 'Ano. Existují vesty s užším střihem nebo s upravitelnými popruhy, které sednou i drobnější postavě. Při výběru porovnejte obvod hrudníku a pasu s tabulkou výrobce.')])

# ------------------------------------------------------------------ gymnasticke-mice
NEW['gymnasticke-mice'] = dict(long=True,
    title='Gymnastické míče: velikost podle výšky a typy',
    desc='Gymnastické míče, overbally, balanční a sedací míče. Jak vybrat velikost 55, 65 nebo 75 cm, materiál a nosnost; porovnání nabídek českých obchodů.',
    intro='<p>Gymnastický míč je nafukovací kulatá pomůcka, na které se cvičí a sedí a která se využívá i při rehabilitaci. V obchodech se mu říká také fitball nebo gymball a nejčastěji se prodává ve velikostech kolem 55, 65 a 75 cm. Sporteka porovnává nabídky českých obchodů, koupit pak můžete přímo v tom, který vás osloví.</p>'
          '<p>V kategorii najdete gymnastické míče, malé overbally na pilates, balanční půlkoule i sedací míče s nožkami nebo s rukojetí. Vyrábějí je například značky ' + B(('hms', 'HMS'), ('merco', 'Merco'), ('gymbeam', 'GymBeam')) + ' a také Lifefit, Sedco, Ledragomma, Spokey nebo Kubisport.</p>'
          '<p>Pro další pomůcky ke cvičení se podívejte na <a href="/fitness-pomucky/">fitness pomůcky</a>, <a href="/balancni-pomucky/">balanční pomůcky</a> a <a href="/pilates-pomucky/">pilates pomůcky</a>.</p>',
    guide='<h2>Jaké typy míčů existují</h2>'
          '<p>Pod označením „gymnastický míč“ se skrývá několik různých pomůcek. Liší se průměrem, tvarem i využitím.</p>'
          + T(['Typ', 'Popis', 'Hodí se pro'], [
              ['Gymnastický míč (fitball, gymball)', 'velký nafukovací míč o průměru zhruba 45–85 cm', 'cvičení trupu, protahování, sezení, rehabilitace'],
              ['Overball', 'malý míč o průměru zhruba 20–30 cm, nafouknutý jen částečně', 'pilates, posilování vnitřních svalů stehen a břicha, cvičení pro seniory'],
              ['Balanční půlkoule', 'půlkulová pomůcka s plochou základnou, někdy s popruhy', 'balanční cvičení, dřepy, kliky'],
              ['Sedací míč', 'míč s kroužkem na základně, s nožkami nebo s rukojetí', 'sezení u stolu, děti, rovnováha při sezení'],
              ['Míč s rukojeťmi (hopsadlo)', 'míč s úchytem pro skákání', 'hra a cvičení dětí'],
              ['Masážní míč', 'malý tuhý míč s výstupky', 'automasáž, ne gymnastický míč v užším smyslu']]) +
          '<p>Nejdřív si ujasněte, co s míčem chcete dělat. Velký fitball se hodí pro celé tělo, overball pro jemnou práci s hlubokými svaly a pilates, balanční půlkule pro trénink rovnováhy. Mnoho lidí má míč doma hlavně na sezení – pak rozhoduje velikost a stabilita.</p>'
          '<h2>Velikost podle výšky těla</h2>'
          '<p>Nejčastější chybou je koupit míč nevhodné velikosti. Pro cvičení platí, že při sezení na míči mají být kolena zhruba v pravém úhlu, případně o něco níže než kyčle. Výrobci běžně uvádějí tuto orientační tabulku.</p>'
          + T(['Průměr míče', 'Výška postavy', 'Poznámka'], [
              ['45 cm', 'děti a velmi drobní dospělí', 'také pro rehabilitaci a malé děti'],
              ['55 cm', 'zhruba 150–165 cm', 'nejmenší běžná dospělá velikost'],
              ['65 cm', 'zhruba 165–175 cm', 'nejčastější volba'],
              ['75 cm', 'zhruba 175–190 cm', 'vyšší postavy'],
              ['85 cm', 'nad 190 cm', 'pro velmi vysoké postavy a sezení u vysokého stolu']]) +
          '<p>Hodnoty jsou orientační. Pokud jste mezi dvěma velikostmi, počítejte s tím, že tvrději nafouknutý míč je o něco vyšší. Pokud na míči cvičíte hlavně břicho a záda, drobné odchylky nevadí. Pro dlouhé sezení se řiďte výškou stolu a židle a zvolte velikost, která jim odpovídá.</p>'
          '<h2>Materiál a bezpečnost: anti-burst</h2>'
          '<p>Míče se vyrábějí z PVC, někdy s příměsí jiných materiálů. Kvalitnější PVC je silnější a hladší. Důležité je označení „anti-burst“, česky zhruba „odolný proti prasknutí“. Takový míč při propíchnutí nepraskne, ale vzduch z něj uniká pomalu, takže cvičenec stihne zareagovat. Označení není zárukou, že se míč nepropíchne, jde o vlastnost konstrukce. U míčů, na kterých budete cvičit celou vahou těla, hledejte tuto informaci i hodnotu nosnosti.</p>'
          '<p>Nosnost bývá uvedena v kilogramech a liší se podle velikosti a kvality. Pokud ji výrobce neuvádí, zvolte raději jiný míč. Povrch má být mírně hrubý nebo protiskluzový, aby se na něm neklouzalo. Hladký lesklý míč po zpocení klouže. Zkontrolujte, zda je materiál bez ftalátů, zejména pokud bude míč používat dítě.</p>'
          '<h2>Příslušenství v balení</h2>'
          '<p>Většina míčů se prodává vyfouknutá. Součástí balení bývá pumpa, někdy jen pumpička s malou kapacitou, a zátky ventilu. Elektrická nebo dvojčinná ruční pumpa ušetří čas. Míč nafukujte postupně a nechte ho pár hodin ustát, protože se materiál natahuje a míč trochu povolí. Pak ho podle návodu dofoukejte na požadovaný průměr.</p>'
          '<p>Některé sady obsahují také plakát s cviky, stojan na míče nebo gumové expandery. Stojan se hodí do ordinací a škol, doma stačí míč uložit tam, kde nejsou ostré kovové předměty.</p>'
          '<h2>Jak cvičit a k čemu míč slouží</h2>'
          '<p>Na nestabilním povrchu míče musí tělo neustále vyrovnávat polohu, a zapojuje tak svaly trupu i hluboké stabilizační svaly. Typické cviky jsou:</p>'
          '<ul><li>zvedání trupu, plank na míči a variace s nohama na míči,</li>'
          '<li>mostík s nohama nebo zády na míči,</li>'
          '<li>dřep s míčem u zdi,</li>'
          '<li>protažení zad a boků v poloze na míči,</li>'
          '<li>kliky s nohama na míči,</li>'
          '<li>pilates cviky s overballem mezi koleny.</li></ul>'
          '<p>Míč se používá i při rehabilitaci, při cvičení v těhotenství a při cvičení dětí. Máte-li zdravotní potíže nebo jste těhotná, poraďte se před zahájením cvičení s lékařem nebo fyzioterapeutem. Začátečníci by měli cvičit u zdi nebo s oporou a postupně přidávat obtížnost.</p>'
          '<h2>Sezení na míči</h2>'
          '<p>Někomu slouží míč místo židle, aby se i vsedě víc hýbal. Sedět se na něm dá i několik hodin, praktičtější je ale střídat ho s běžnou židlí. Dlouhé sezení na nestabilním povrchu unavuje a nenahrazuje pravidelný pohyb. Při práci používejte míč s protiskluzovým kroužkem a nohama pevně na zemi, aby se neodkutálel. Sedací míč s nožkami je stabilnější a hodí se pro děti.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Nenechávejte míč na slunci ani u radiátoru, vzduch uvnitř se roztahuje a materiál stárne.</li>'
          '<li>Čistěte vlhkým hadříkem a jemným mýdlem, bez rozpouštědel.</li>'
          '<li>Před cvičením zkontrolujte tlak a povrch, hledejte prasklinky a odřeniny.</li>'
          '<li>Nepoužívejte míč venku na drsné zemi ani na ostrých předmětech.</li>'
          '<li>Při delším skladování ho nechte částečně vyfouknutý a uložený mimo ostré předměty.</li></ul>'
          '<h2>Jak začít s prvním cvičením na míči</h2>'
          '<p>Posaďte se doprostřed míče, chodidla dejte na šířku boků a záda držte vzpřímeně. Zkuste pomalu přenášet váhu ze strany na stranu a naklánět pánev dopředu a dozadu. Po několika minutách zkuste zvednout jednu nohu. Až se budete na míči cítit stabilně, přidejte zvedání paží nebo malé výpady. Teprve potom přejděte k cvikům na zemi, kde je míč pod zády nebo pod nohama. Pomalý nácvik vás chrání před pádem a učí tělo hledat rovnováhu.</p>'
          '<p>Při cvičení myslete na dýchání a nezadržujte dech. Pohyb má vycházet z vás, ne z míče: pokud se zbytečně kymácíte, snižte obtížnost, například rozšiřte stoj nebo se opřete o zeď. Po cvičení si na míč nesedejte zpocení, protože vlhký povrch klouže.</p>'
          '<h2>Overball a balanční půlkoule podrobněji</h2>'
          '<p>Overball je malý míč, který se nafukuje jen napůl, aby zůstal měkký a stlačitelný. Používá se mezi koleny, pod pánví nebo za zády při pilates a při jemném posilování. Je tichý, lehký a vejde se do tašky. Balanční půlkoule má ploché dno a oblou horní stranu, takže se na ní dá stát, klečet nebo se o ni opírat při klikách. Lze ji obrátit a cvičit na rovné straně. Výběr závisí na tom, zda potřebujete nestabilní povrch pro nohy, nebo pomůcku pro jemné cvičení.</p>'
          '<h2>Míče pro děti a seniory</h2>'
          '<p>Pro děti se používají menší míče a sedací míče s nožkami nebo s rukojetí, díky nimž míč neujíždí. Děti cvičí hravou formou, například houpání, odkopávání nebo cvičení při sezení u stolu. Dohled dospělého je samozřejmost. Pro seniory se hodí overball a menší míč na cvičení vsedě na židli, kde opora brání pádu. Cvičení by mělo být pomalé a pohyby malé. Při potížích s rovnováhou nebo kostmi se poraďte s lékařem či fyzioterapeutem.</p>'
          '<h2>Chyby při výběru</h2>'
          '<p>Nejčastěji lidé kupují míč podle barvy a ceny a přehlédnou průměr. Další chybou je příliš velký míč na sezení, na kterém pak nedosáhnete nohama na zem. Jiní naopak koupí příliš malý míč a při cvičení se jim kolena zvedají výš než kyčle. Nepodceňujte ani pumpu: nedostatečně nafouknutý míč se hůř ovládá. Pokud si nejste jistí, zeptejte se obchodu na tabulku velikostí nebo zvolte velikost podle tabulky výšek uvedené výše a doma ji vyzkoušejte vsedě.</p>'
          '<h2>Co dalšího se hodí</h2>'
          '<p>K míči patří podložka, protože při cvičení na zemi tlačí tvrdá podlaha. Najdete ji v kategorii <a href="/joga-a-podlozky/">jóga a podložky</a>. Gumové expandery a další doplňky najdete mezi <a href="/fitness-pomucky/">fitness pomůckami</a>, pro nácvik rovnováhy slouží <a href="/balancni-pomucky/">balanční pomůcky</a>. Pro jemné posilování těla si prohlédněte <a href="/pilates-pomucky/">pilates pomůcky</a>.</p>'
          '<p>Nabídky nesrovnávejte jen podle ceny. Všímejte si průměru, nosnosti, označení anti-burst, dodané pumpy a podmínek vrácení. Sporteka porovnává nabídky českých obchodů a objednáváte přímo v obchodě. Míče se dodávají vyfouknuté, proto počítejte s časem na první nafouknutí.</p>',
    faq=[
        ('Jakou velikost gymnastického míče zvolit?', 'Podle výšky postavy. Obvykle 55 cm pro výšku zhruba 150–165 cm, 65 cm pro 165–175 cm a 75 cm pro 175–190 cm. Při sezení mají být kolena přibližně v pravém úhlu.'),
        ('Co znamená anti-burst?', 'Míč je konstruován tak, aby při propíchnutí nepraskl a vzduch z něj unikal pomalu. Cvičenec tak má čas sednout nebo vstát. Nejde o záruku, že se míč neprořízne.'),
        ('Jaký je rozdíl mezi fitballem a overballem?', 'Fitball je velký míč na sezení a cvičení celého těla. Overball je malý, jen částečně nafouknutý míč na jemné posilování a pilates.'),
        ('Dá se na míči sedět místo židle?', 'Střídavě ano, ale dlouhé sezení na nestabilním povrchu unavuje. Používejte stabilní míč s protiskluzovým povrchem a střídejte ho s běžnou židlí.'),
        ('Jak míč správně nafouknout?', 'Nafukujte postupně a nechte míč několik hodin ustát, protože se materiál natahuje. Pak dohustěte na průměr podle návodu. Lehce stlačený míč je pro cvičení pohodlnější než pevný.'),
        ('Jakou nosnost má mít míč?', 'Řiďte se údajem výrobce a nechte si rezervu. Dynamické cviky, například skákání, míč zatěžují víc než sezení. Nosnost je důležitější než barva nebo značka.'),
        ('Mohou míč používat děti?', 'Ano, ale vhodná je menší velikost a dohled dospělého. Hledejte míč bez ftalátů a se stabilizovanou základnou nebo s nožkami.')])
