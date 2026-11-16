"""sporteka.cz — wave 28c (16. 11. 2026): long texts for ledvinky, batohy-na-notebook, termohrnky, piknikove-deky.
General true facts only, no prices, no product counts, no invented heat-retention hours. Notebook sizes in inches explained as display
diagonal; vacuum insulation described in general terms. Brands linked only if present in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ ledvinky
NEW['ledvinky'] = dict(long=True,
    title='Ledvinky: dámské, pánské, běžecké i turistické',
    desc='Ledvinky dámské i pánské, městské, běžecké a turistické s držákem na lahev. Jak vybrat objem, materiál a nošení, a porovnat nabídky e-shopů.',
    intro='<p><strong>Ledvinka</strong> je malá taška na opasku, ve které máte telefon, klíče a peněženku pořád u sebe a ruce volné. Kdysi patřila k turistům v devadesátých letech, dnes se vrátila jako módní doplněk, který se nosí nejen kolem pasu, ale i šikmo přes hrudník nebo přes rameno. Vedle městských modelů existují běžecké ledvinky, které se při pohybu nehoupou, a turistické ledvinky s držáky na lahve, které zvládnou celodenní výlet bez batohu.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů a objednávku dokončíte přímo v obchodě. V katalogu jsou dámské i pánské ledvinky od ' + B(('fjallraven', 'Fjällräven'), ('deuter', 'Deuter'), ('loap', 'Loap'), ('adidas', 'Adidas'), ('tommy-hilfiger', 'Tommy Hilfiger'), ('guess', 'Guess')) + ' nebo Silva. Ledvinky patří do kategorie <a href="/tasky-pres-rameno/">tašky přes rameno</a>; na běh s větší výbavou se hodí také <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>.</p>',
    guide='<h2>Typy ledvinek</h2>'
          '<p>Ledvinky vypadají podobně, ale každý typ je stavěný na něco jiného. Městská ledvinka řeší hlavně vzhled a přehledné kapsy, běžecká stabilitu při pohybu a turistická objem a nosnost.</p>'
          + T(['Typ', 'Typický objem', 'K čemu se hodí'], [
              ['Městská a módní', 'do 2 litrů', 'telefon, peněženka, klíče, nošení přes rameno'],
              ['Běžecká', 'pod 1 litr', 'telefon, gel, klíče; těsně na těle bez houpání'],
              ['Turistická (hip pack)', '2 až 6 litrů i víc', 'svačina, větrovka, mapa, držáky na lahve'],
              ['Cestovní pod oblečení', 'velmi plochá', 'doklady a peníze schované pod tričkem'],
              ['Dětská', 'malá', 'kapesníky, svačina, drobnosti na výlet']]) +
          '<p>Pro město vám obvykle stačí ledvinka, do které se vejde telefon, klíče, karta a malé balení kapesníků. Na celodenní túru bez batohu potřebujete víc místa: na svačinu, lehkou bundu a pití. Běžec naopak chce co nejmenší objem a co nejméně pohybu.</p>'
          '<h2>Dámská ledvinka</h2>'
          '<p>Dámské ledvinky bývají menší a víc dbají na vzhled. Často jsou z koženky, prošívaného nylonu nebo hladké kůže, s kovovými detaily a nastavitelným popruhem, který z ledvinky udělá crossbody kabelku. Značky jako Guess nebo Tommy Hilfiger je nabízejí v barvách svých kolekcí. Hodí se na koncert, do města, na festival nebo na cesty, kde nechcete nosit velkou kabelku. Při výběru zkontrolujte, zda se do ní vejde váš telefon, protože dnešní velké mobily se do nejmenších modelů nevejdou.</p>'
          '<h2>Jak se ledvinka nosí</h2>'
          '<ul><li><strong>Kolem pasu vpředu:</strong> klasika, nejsnazší přístup ke kapsám.</li>'
          '<li><strong>Kolem pasu vzadu:</strong> u turistických ledvinek, kde je váha nejlépe rozložená na bedrech.</li>'
          '<li><strong>Šikmo přes hrudník:</strong> nejčastější městský styl, ledvinka je pod dohledem a nezavazí.</li>'
          '<li><strong>Přes rameno na zádech:</strong> jako malý batůžek, když potřebujete volnost vpředu.</li></ul>'
          '<p>Pro nošení přes hrudník potřebujete delší popruh, než jaký má většina dětských nebo běžeckých modelů. Délku popruhu najdete v popisu produktu, případně si ji odhadněte podle obvodu pasu, který výrobce uvádí.</p>'
          '<h2>Běžecká ledvinka a běžecký opasek</h2>'
          '<p>Při běhu se každá volná věc houpe a tluče do boků. Běžecké ledvinky jsou proto malé, mají pružný pás a pevně přiléhají. Ještě dál jde běžecký opasek, což je pružná trubice kolem pasu s několika otvory, do které se rozloží telefon, klíče a gely. Nic se v něm nehoupe a dá se nosit i pod tričkem. Pokud potřebujete s sebou pití na delší běh, je lepší <a href="/bezecke-vesty-a-batohy/">běžecká vesta</a> s měkkými lahvemi. Opasky a ledvinky pro běžce najdete také v kategorii <a href="/bezecke-opasky/">běžecké opasky</a>. Některé modely značky Silva nebo Deuter mají reflexní prvky, které oceníte za šera.</p>'
          '<h2>Turistická ledvinka místo batohu</h2>'
          '<p>Turistické ledvinky, anglicky hip pack, nesou váhu na bedrech, takže záda zůstávají volná a nepotí se. To ocení každý, kdo jde v létě na celodenní výlet, fotograf, který potřebuje rychlý přístup k objektivu, nebo houbař. Kvalitní turistická ledvinka má široký polstrovaný bederní pás, boční kapsy nebo držáky na lahve a kompresní popruhy. Deuter, Fjällräven nebo Adidas Terrex nabízejí modely s objemem kolem tří až šesti litrů. Pokud se do ledvinky nevejde pláštěnka, svačina a pití, bude pohodlnější malý <a href="/turisticke-batohy/">turistický batoh</a>.</p>'
          '<p>Fjällräven Kånken Hip Pack vychází z oblíbeného batohu Kånken a je ze stejného odolného materiálu Vinylon F. Ulvö Hip Pack od stejné značky je technicky laděný, s větším objemem. U všech turistických ledvinek platí, že plná lahev v bočním držáku zatíží jeden bok. Pokud nosíte dvě lahve, rozložte je na obě strany.</p>'
          '<h2>Materiály</h2>'
          '<ul><li><strong>Nylon a polyester:</strong> lehké, odolné a snadno omyvatelné; nejčastější materiál sportovních ledvinek.</li>'
          '<li><strong>Cordura a podobné tkaniny:</strong> velmi odolné proti oděru, hodí se do terénu.</li>'
          '<li><strong>Vinylon F:</strong> pevná tkanina z vinylalkoholových vláken, kterou používá Fjällräven.</li>'
          '<li><strong>Kůže a koženka:</strong> městský vzhled, kůže stárne s patinou, koženka se může časem loupat.</li>'
          '<li><strong>Recyklované materiály:</strong> polyester z PET lahví, který dnes používá řada značek.</li></ul>'
          '<p>Vodoodolnost je u ledvinek spíš výjimkou. Většina vydrží krátkou přeháňku, ale švy a zip vodu propustí. Do deště proto vložte telefon a doklady do sáčku, případně volte model s vodotěsným zipem a svařovanými švy.</p>'
          '<h2>Na co se dívat při výběru</h2>'
          '<ul><li><strong>Kapsa u těla:</strong> zadní kapsa přiléhající k zádům nebo břichu je nejbezpečnější místo na doklady a peníze.</li>'
          '<li><strong>Karabina na klíče:</strong> klíče se pak nemotají mezi ostatními věcmi.</li>'
          '<li><strong>Zipy:</strong> kvalitní zip s velkými jezdci se dá otevřít i v rukavicích.</li>'
          '<li><strong>Spona:</strong> plastová spona se zacvakne jednou rukou; u městských modelů bývá kovová.</li>'
          '<li><strong>Vnitřní uspořádání:</strong> několik menších kapes zabrání tomu, aby se telefon poškrábal o klíče.</li>'
          '<li><strong>Otvor na sluchátka:</strong> praktický u běžeckých modelů.</li></ul>'
          '<h2>Ledvinka na kolo a na cesty</h2>'
          '<p>Na kole se ledvinka hodí na kratší projížďky do města, nosí se spíš šikmo přes záda než kolem pasu, aby při šlapání nepřekážela. Na delší vyjížďky je lepší taška na rám nebo pod sedlo z kategorie <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>. Na cestách ledvinka nahradí kabelku v letadle i ve městě. V přeplněné tramvaji nebo na turistických místech ji noste vpředu, kde na ni vidíte, a zip mějte otočený k tělu.</p>'
          '<h2>Ledvinka na festival a koncert</h2>'
          '<p>Na festivalu nebo koncertě chcete mít doklady, telefon a peníze pořád u sebe a nehlídat kabelku. Ledvinka nošená vpředu přes hrudník je v davu pod kontrolou a při tanci nepřekáží. Hodí se model se zipem otočeným k tělu a s vnitřní kapsou na kartu. Pokud festival probíhá v dešti nebo v blátě, ocení se tmavá omyvatelná látka a sáček na telefon uvnitř. Na vícedenní akce se vyplatí ledvinka, do které se vejde i malá powerbanka.</p>'
          '<h2>Ledvinka pro pejskaře a fotografy</h2>'
          '<p>Pejskaři nosí v ledvince pamlsky, sáčky na exkrementy, klíče a telefon, takže mají obě ruce volné pro vodítko. Praktická je samostatná přihrádka na pamlsky, kterou lze vyprat, a zásobník na sáčky na vnější straně. Fotografové zase oceňují ledvinky s polstrovanou přihrádkou, do které se vejde menší objektiv nebo kompaktní fotoaparát. Turistické ledvinky s bederním pásem unesou i těžší výbavu, aniž by tížily krk.</p>'
          '<h2>Ledvinky pro děti</h2>'
          '<p>Dětská ledvinka je malá, lehká a má krátký pás. Dítě si do ní na výlet uloží kapesníky, svačinu, oblíbenou hračku nebo kartičku s telefonem na rodiče. Hodí se veselé barvy a reflexní prvek. U nejmenších dětí dbejte na to, aby pás šel snadno rozepnout, a ledvinku nenechávejte na dítěti při spaní ani na prolézačkách, kde by se mohla zachytit.</p>'
          '<h2>Péče</h2>'
          '<p>Nylonové a polyesterové ledvinky otřete vlhkým hadříkem s trochou mýdla, při větším ušpinění je vyperte ručně ve vlažné vodě. Do pračky je dávejte jen tehdy, když to výrobce dovoluje, a vždy v prádelním sáčku se zavřenými zipy. Kožené modely ošetřujte přípravkem na kůži a nenechávejte je zmoklé schnout u topení. Zipy čas od času vyčistěte kartáčkem od písku a prachu, prodloužíte jim život.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Malá městská ledvinka, do které se nevejde velký telefon.</li>'
          '<li>Běžecká ledvinka s volným popruhem, která se při běhu houpe.</li>'
          '<li>Krátký popruh, který nejde nosit přes hrudník.</li>'
          '<li>Turistická ledvinka přeplněná tak, že tlačí na bedra.</li>'
          '<li>Spoléhání na vodoodolnost u modelu bez vodotěsného zipu.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe, včetně barev, které mají skladem; objednávku dokončíte v e-shopu. Porovnejte rozměry a objem v litrech, protože fotky na bílém pozadí velikost nepoznají. Na větší náklad poslouží <a href="/mestske-batohy/">městské batohy</a>, pití s sebou uložíte do lahví z kategorie <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>',
    faq=[
        ('Jak se dnes nosí ledvinka?', 'Kolem pasu vpředu, šikmo přes hrudník nebo přes rameno na zádech. Pro nošení přes hrudník potřebujete delší popruh, ověřte si ho v popisu.'),
        ('Vejde se do ledvinky velký telefon?', 'Do většiny ano, do nejmenších módních modelů ne vždy. Porovnejte vnitřní rozměry ledvinky s rozměry telefonu.'),
        ('Jaký je rozdíl mezi běžeckou ledvinkou a běžeckým opaskem?', 'Ledvinka má jednu kapsu na pásku. Opasek je pružná trubice kolem pasu s několika otvory, věci se rozloží po obvodu a nic se nehoupe.'),
        ('Může turistická ledvinka nahradit batoh?', 'Na krátký nebo letní výlet ano, pokud se do ní vejde svačina, pití a lehká bunda. Na delší túru v proměnlivém počasí je pohodlnější batoh.'),
        ('Jsou ledvinky vodotěsné?', 'Většinou ne. Krátkou přeháňku vydrží, ale zipy a švy vodu propustí. Telefon a doklady v dešti chraňte sáčkem.'),
        ('Jakou ledvinku vybrat pro ženu?', 'Do města menší ledvinku s nastavitelným popruhem, kterou lze nosit jako crossbody. Na sport a výlety platí stejná pravidla jako u pánských modelů.'),
        ('Je ledvinka vhodná na kolo?', 'Na krátké projížďky ano, nejlépe šikmo přes záda. Na delší vyjížďky je pohodlnější taška na rám nebo pod sedlo.'),
        ('Jaký objem ledvinky na túru?', 'Na půldenní výlet s pitím a svačinou kolem tří až šesti litrů. Pokud se dovnitř nevejde ani lehká bunda, bude pohodlnější malý batoh.'),
        ('Jak nosit ledvinku, aby ji nikdo neokradl?', 'Vpředu přes hrudník nebo kolem pasu, se zipem otočeným k tělu. Doklady a peníze uložte do zadní kapsy, která přiléhá k tělu.'),
        ('Jak ledvinku vyčistit?', 'Vlhkým hadříkem s mýdlem, větší špínu ručním praním ve vlažné vodě. Kůži ošetřujte přípravkem na kůži a nesušte ji u topení.'),
    ])

# ------------------------------------------------------------------ batohy-na-notebook
NEW['batohy-na-notebook'] = dict(long=True,
    title='Batohy na notebook 13, 14, 15,6 i 17 palců',
    desc='Batohy na notebook 13, 14, 15,6 i 17 palců: městské, do práce, do školy i na cesty. Jak ověřit, že se notebook vejde, a nabídky českých e-shopů.',
    intro='<p><strong>Batoh na notebook</strong> se od obyčejného batohu liší hlavně polstrovanou přihrádkou, ve které je počítač chráněný před nárazy a odřením. Dobře navržený batoh drží notebook u zad, nad dnem a odděleně od lahve a svačiny. Ve městě ho nosí studenti, lidé, kteří dojíždějí do práce na kole nebo vlakem, i ti, kdo s počítačem cestují letadlem. Podle toho se liší objem, uspořádání kapes i ochrana proti dešti.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů a nakoupíte v obchodě, který si vyberete. Najdete tu batohy ' + B(('fjallraven', 'Fjällräven'), ('the-north-face', 'The North Face')) + ', Caterpillar, XD Design a dalších značek, například Kånken Laptop, Ulvö nebo řadu Base Camp. Nadřazenou kategorií jsou <a href="/mestske-batohy/">městské batohy</a>, další typy najdete v kategorii <a href="/batohy/">batohy</a>.</p>',
    guide='<h2>Palce: co velikost notebooku znamená</h2>'
          '<p>Velikost notebooku v palcích, tedy 13, 14, 15,6, 16 nebo 17, udává úhlopříčku displeje, ne rozměry celého počítače. Jeden palec měří 2,54 cm. Dva notebooky se stejnou úhlopříčkou se mohou lišit šířkou o několik centimetrů, podle toho, jak široký je rámeček kolem displeje a jak silné je tělo. Výrobci batohů proto uvádějí, do jaké velikosti notebooku je přihrádka určená, a ti pečlivější i vnitřní rozměry přihrádky v centimetrech.</p>'
          + T(['Úhlopříčka', 'Typické použití', 'Na co myslet'], [
              ['13 a 14 palců', 'ultrabooky, škola, cestování', 'vejde se do menších městských batohů'],
              ['15,6 a 16 palců', 'nejběžnější pracovní notebooky', 'nejširší výběr batohů'],
              ['17 palců', 'herní a pracovní stanice', 'potřebuje velký batoh, ověřte vnitřní rozměry'],
              ['Tablet', 'do 11 až 13 palců', 'často má v batohu vlastní menší kapsu']]) +
          '<p>Před nákupem si změřte šířku, hloubku a tloušťku svého notebooku a porovnejte je s rozměry přihrádky. U herních notebooků počítejte také s objemnou nabíječkou. Pokud výrobce uvádí jen palce, je lepší přihrádka o stupeň větší než těsně stejná, protože polstrování ubírá místo.</p>'
          '<h2>Jak má vypadat přihrádka na notebook</h2>'
          '<ul><li><strong>Polstrování ze všech stran:</strong> pěna nebo vícevrstvá výplň chrání před nárazem do hrany.</li>'
          '<li><strong>Zvýšené dno:</strong> přihrádka končí několik centimetrů nad dnem batohu, takže když batoh postavíte na zem, notebook nedopadne.</li>'
          '<li><strong>Umístění u zad:</strong> nejtěžší věc nesená blízko těla se nese pohodlněji a je lépe chráněná.</li>'
          '<li><strong>Samostatný přístup:</strong> boční nebo zadní zip umožní vyndat notebook bez vybalování ostatních věcí, ocení to každý na letištní kontrole.</li>'
          '<li><strong>Zapínání přihrádky:</strong> pásek na suchý zip drží menší notebook na místě.</li></ul>'
          '<h2>Objem a uspořádání</h2>'
          '<p>Na každodenní cestu do práce s notebookem, nabíječkou, svačinou a lahví obvykle stačí batoh s objemem kolem 15 až 25 litrů. Kdo nosí ještě oblečení na trénink nebo jezdí na služební cesty, ocení 25 až 35 litrů. Větší batoh ale svádí k přeplnění a těžký batoh zatěžuje ramena. Důležité je i rozvržení: organizér s kapsami na nabíječku, myš, pera a doklady, boční kapsy na lahev a deštník a malá kapsa nahoře na brýle nebo sluchátka. Batoh s jednou velkou komorou je přehledný, ale věci v něm padají na dno.</p>'
          '<h2>Typy batohů na notebook</h2>'
          '<ul><li><strong>Městský batoh se zipem:</strong> nejběžnější tvar, přehledný a s mnoha kapsami. Příkladem jsou batohy z řady Base Camp od The North Face.</li>'
          '<li><strong>Rolovací batoh (rolltop):</strong> horní část se roluje a zapíná sponou. Lépe odolává dešti a objem se dá zvětšit. Takový tvar má například Fjällräven Ulvö Rolltop.</li>'
          '<li><strong>Batoh s klopou:</strong> klasický vzhled, jako Fjällräven Kånken Laptop, který se vyrábí ve verzích pro 13, 15 a 17 palců.</li>'
          '<li><strong>Batoh proti kapsářům:</strong> skryté zipy u zad a pořezu odolná látka; tento styl proslavila XD Design řadou Bobby.</li>'
          '<li><strong>Cestovní batoh:</strong> otevírá se jako kufr, má popruh na kufr a rozměry blízké příručnímu zavazadlu.</li>'
          '<li><strong>Batoh 2 v 1 s taškou:</strong> skrývá popruhy a dá se nést i v ruce jako aktovka.</li></ul>'
          '<h2>Nošení a pohodlí</h2>'
          '<p>Notebook, nabíječka a lahev vody dohromady váží víc, než se zdá, a nosíte je každý den. Polstrované ramenní popruhy by měly být široké a tvarované do písmene S, aby netlačily na krk. Zádový panel s větracími kanálky omezí pocení. Hrudní popruh stabilizuje batoh při chůzi do schodů nebo při jízdě na kole. U těžších batohů pomůže i jednoduchý bederní pásek. Batoh noste na obou ramenou a popruhy utáhněte tak, aby jeho spodní okraj nesahal níž než k bedrům.</p>'
          '<h2>Do deště a na kolo</h2>'
          '<p>Většina městských batohů je z polyesteru nebo nylonu s vodoodpudivou úpravou, která zvládne krátkou cestu v dešti. Zipy a švy ale vodu postupně propustí. Pokud jezdíte na kole za každého počasí, zvolte rolovací batoh z nepromokavé látky se svařovanými švy, nebo mějte s sebou pláštěnku na batoh. Notebook můžete navíc uložit do neoprenového obalu. Pro cyklisty jsou užitečné reflexní prvky a úchyt na blikačku. Pokud nechcete nosit náklad na zádech, podívejte se na tašky z kategorie <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>'
          '<h2>Batoh na notebook do letadla</h2>'
          '<p>Letecké společnosti mají pro osobní zavazadlo pod sedadlem i pro příruční zavazadlo vlastní rozměrové limity, které se liší. Před cestou si je ověřte u konkrétního dopravce a porovnejte s vnějšími rozměry batohu, ne s objemem v litrech. Na letišti oceníte přihrádku na notebook, která se dá otevřít bez vybalování, a popruh na zadní straně batohu, kterým ho navléknete na madlo kufru. Notebook a powerbanku přepravujte v příručním zavazadle, ne v odbaveném.</p>'
          '<h2>USB port a nabíjení</h2>'
          '<p>Některé batohy mají na boku USB port. Jde jen o kabel, který vede z vnější strany batohu dovnitř, kde se připojí powerbanka. Batoh sám o sobě nic nenabíjí a powerbanku si musíte koupit zvlášť, například v kategorii <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a>. Před praním batohu nebo v dešti port zakryjte a powerbanku vyndejte.</p>'
          '<h2>Do školy a na vysokou</h2>'
          '<p>Studenti potřebují batoh, do kterého se vejde notebook i sešity, učebnice a svačina. Pro mladší školáky jsou ale vhodnější aktovky a ergonomické školní batohy s pevnými zády, které najdete v kategorii <a href="/skolni-batohy/">školní batohy</a>. Studentům střední a vysoké školy obvykle vyhoví městský batoh s přihrádkou na notebook, bočními kapsami na lahev a organizérem. Batoh na notebook by u dětí neměl být těžší, než unesou bez předklánění.</p>'
          '<h2>Batoh do práce: jak působí v kanceláři</h2>'
          '<p>Do kanceláře nebo na schůzku se hodí batoh střídmého vzhledu, v černé, šedé nebo tmavě modré barvě, bez výrazných log a visících popruhů. Kožené detaily a pevný tvar mu dodají vzhled aktovky. Batohy 2 v 1 se skrytými popruhy se dají na jednání nést v ruce jako taška. Pro jízdu na kole do práce se ale vyplatí reflexní prvky, které se dají zakrýt nebo jsou nenápadně umístěné.</p>'
          '<h2>Batoh pro grafiky a programátory</h2>'
          '<p>Kdo s sebou nosí výkonný pracovní notebook, k tomu tablet, externí disk, myš a objemnou nabíječku, potřebuje batoh s pevnějším polstrováním a víc menšími přihrádkami. Pro herní a grafické notebooky se sedmnáctipalcovým displejem se vyplatí batoh se samostatně zpevněnou zadní stěnou, který se pod váhou nedeformuje. Kabely a adaptéry se nejlépe drží v samostatném pouzdře, které se celé přendá do jiné tašky.</p>'
          '<h2>Ochrana proti krádeži</h2>'
          '<p>Ve vlaku, tramvaji nebo na letišti je batoh na zádech mimo dohled. Batohy proti kapsářům proto mají hlavní zip u zad, skryté kapsy na doklady a materiál, který odolá říznutí. Některé modely mají zámek na zipy nebo kabel na připevnění k židli. Batoh ale nikdy neochrání úplně, a v přeplněném prostředku je nejbezpečnější sundat ho a držet před sebou. Doklady a peněženku noste raději v kapse u těla.</p>'
          '<h2>Péče</h2>'
          '<p>Batoh vyčistěte vlhkým hadříkem nebo měkkým kartáčkem s trochou mýdla. Pokud je potřeba, perte ho ručně ve vlažné vodě, předtím vyndejte vše z kapes a odepněte pevné výztuhy. Do pračky dávejte batoh jen tehdy, když to dovoluje štítek. Sušte ho otevřený a hlavou dolů, mimo topení. Zipy čistěte od prachu a písku, a pokud zadrhávají, pomůže trocha vosku nebo tuhy.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr jen podle palců bez porovnání rozměrů notebooku a přihrádky.</li>'
          '<li>Přihrádka bez zvýšeného dna, takže notebook dopadne na zem s každým položením batohu.</li>'
          '<li>Batoh, který je zbytečně velký a svádí k přeplnění.</li>'
          '<li>Spoléhání na vodoodpudivou úpravu při jízdě na kole v dešti.</li>'
          '<li>Představa, že USB port v batohu sám nabíjí.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe, takže snadno najdete barvu a velikost, která je skladem. Objednávku pak dokončíte v e-shopu. Pokud nosíte notebook jen občas a jinak potřebujete batoh na výlety, porovnejte i <a href="/turisticke-batohy/">turistické batohy</a>, z nichž některé mají přihrádku na hydrovak vhodnou i pro tenký notebook. Na krátké cesty bez počítače stačí taška z kategorie <a href="/tasky-pres-rameno/">tašky přes rameno</a>.</p>',
    faq=[
        ('Co znamená batoh na notebook 15,6 palce?', 'Přihrádka je určená pro notebook s úhlopříčkou displeje 15,6 palce. Notebooky se stejnou úhlopříčkou se ale liší rozměry, proto porovnejte rozměry přihrádky s vaším počítačem.'),
        ('Vejde se 16palcový notebook do batohu na 15,6 palce?', 'Často ano, protože šestnáctipalcové notebooky mívají užší rámečky. Jistotu dá jen porovnání skutečných rozměrů notebooku s vnitřními rozměry přihrádky.'),
        ('Jaký objem batohu na notebook zvolit?', 'Na každodenní cestu do práce obvykle 15 až 25 litrů, s oblečením na trénink nebo na služební cesty 25 až 35 litrů.'),
        ('Co je zvýšené dno přihrádky?', 'Přihrádka končí několik centimetrů nad dnem batohu, takže notebook při položení batohu na zem nedopadne na podlahu.'),
        ('Nabíjí batoh s USB portem telefon sám?', 'Ne. USB port je jen kabel vedený do batohu, kam musíte připojit vlastní powerbanku.'),
        ('Je batoh na notebook nepromokavý?', 'Většina má jen vodoodpudivou úpravu na krátký déšť. Na kolo za každého počasí volte rolovací batoh z nepromokavé látky nebo pláštěnku na batoh.'),
        ('Kolik litrů má mít batoh na sedmnáctipalcový notebook?', 'Rozhoduje hlavně velikost přihrádky, ne objem. Batohy pro 17 palců mívají kolem 25 litrů a víc; vždy porovnejte vnitřní rozměry přihrádky s notebookem.'),
        ('Jaký batoh na notebook na kolo?', 'Rolovací batoh z nepromokavé látky se svařovanými švy, hrudním popruhem a reflexními prvky. Případně běžný batoh s pláštěnkou a notebookem v neoprenovém obalu.'),
        ('Mohu batoh na notebook vzít do letadla?', 'Obvykle ano, rozměrové limity si ale ověřte u letecké společnosti a porovnejte je s vnějšími rozměry batohu. Notebook a powerbanku nechte v příručním zavazadle.'),
    ])

# ------------------------------------------------------------------ termohrnky
NEW['termohrnky'] = dict(long=True,
    title='Termohrnky na kávu a čaj: Stanley, Thermos a další',
    desc='Termohrnky na kávu a čaj z nerezu s vakuovou izolací, s víčkem proti vylití i brčkem. Jak vybrat objem a víčko, péče, nabídky českých e-shopů.',
    intro='<p><strong>Termohrnek</strong> udrží kávu nebo čaj teplý cestou do práce, na procházce se psem i na sedačce lanovky. Na rozdíl od termosky se z něj pije přímo, bez nalévání do víčka, a je stavěný tak, aby se vešel do ruky i do držáku v autě. Moderní termohrnky jsou většinou z nerezové oceli s dvojitou stěnou a vakuem mezi stěnami, takže drží teplotu nápoje mnohem déle než plastový hrnek. Termohrnek na kávu zároveň nahradí papírové kelímky z kaváren.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů, nákup pak dokončíte přímo v e-shopu. Najdete tu termohrnky Stanley včetně populárního Quencheru, Thermos, Vialli Design, Nils Camp nebo Huron. Nadřazenou kategorií jsou <a href="/lahve-a-termosky/">lahve a termosky</a>, na teplé jídlo venku se hodí výbava z kategorie <a href="/vareni-v-prirode/">vaření v přírodě</a>.</p>',
    guide='<h2>Jak termohrnek funguje</h2>'
          '<p>Teplo uniká třemi způsoby: vedením, prouděním a sáláním. Termohrnek má dvě nerezové stěny a mezi nimi je vzduch odčerpaný na vakuum. Ve vakuu se teplo nemůže šířit vedením ani prouděním, takže se horký nápoj ochlazuje mnohem pomaleji. Nejvíc tepla pak uniká víčkem, které vakuum nemá. Proto se termohrnky liší výdrží hlavně podle konstrukce víčka a podle toho, jak dobře těsní. Totéž funguje opačně: vakuový termohrnek udrží ledovou vodu nebo ledovou kávu dlouho studenou.</p>'
          '<p>Výrobci uvádějí, kolik hodin nápoj zůstane horký nebo studený. Tyto údaje platí pro plný a předehřátý hrnek se zavřeným víčkem. Napůl vypitý hrnek, který otevíráte každých pár minut, chladne rychleji. Pro srovnání jednotlivých modelů jsou ale údaje výrobců užitečné.</p>'
          '<h2>Typy víček</h2>'
          + T(['Víčko', 'Jak funguje', 'Kdy se hodí'], [
              ['Tlačítko proti vylití', 'otevře se stiskem, po puštění se zavře', 'do tašky, do auta, na cesty'],
              ['Posuvné nebo otočné víčko', 'otvor se otevře posunutím', 'do kanceláře, na stůl'],
              ['Víčko s brčkem', 'pije se brčkem, často s otočným krytem', 'studené nápoje, voda během dne'],
              ['Šroubovací uzávěr', 'otevírá se úplně, dobře těsní', 'polévka, delší výlet'],
              ['Víčko s pítkem a klipem', 'pítko se zaklapne', 'turistika, kolo']]) +
          '<p>Pokud termohrnek nosíte v tašce nebo batohu, rozhoduje, zda je skutečně těsný, ne jen „odolný proti polití“. Výrobci to rozlišují: hrnek odolný proti vylití snese převržení na stole, ale v batohu vzhůru nohama může prosakovat. Stanley Quencher s brčkem patří k těm, které se nosí v ruce a do držáku, ne vzhůru nohama v tašce. Hrnky s tlačítkovým uzávěrem typu Thermos nebo Stanley Trigger-Action jsou naopak stavěné na to, aby v tašce netekly.</p>'
          '<h2>Objem</h2>'
          '<ul><li><strong>Kolem 250 až 350 ml:</strong> jedna káva nebo menší čaj na cestu, vejde se do kapsy batohu.</li>'
          '<li><strong>Kolem 400 až 500 ml:</strong> nejuniverzálnější velikost na celé dopoledne.</li>'
          '<li><strong>Kolem 600 ml až 1 litr a víc:</strong> velké hrnky s uchem a brčkem typu Quencher na vodu a studené nápoje během celého dne.</li></ul>'
          '<p>Termohrnek drží teplotu nejlépe, když je plný. Malé množství nápoje ve velkém hrnku vychladne rychleji, protože uvnitř zůstává víc vzduchu. Vybírejte proto objem podle toho, kolik obvykle vypijete.</p>'
          '<h2>Materiál</h2>'
          '<p>Kvalitní termohrnky jsou z nerezové oceli 18/8, označované také jako 304, která nerezaví, je odolná a nepřenáší chuť. Některé modely mají vnitřek s keramickým povlakem, aby káva neměla kovovou pachuť. Venkovní povrch bývá lakovaný nebo práškově lakovaný, což zlepšuje úchop, ale může se poškrábat. Víčka jsou z plastu bez BPA a silikonového těsnění. Plastové nebo skleněné hrnky s dvojitou stěnou bez vakua jen chrání ruku před horkem, teplotu ale drží výrazně kratší dobu.</p>'
          '<h2>Termohrnek do auta</h2>'
          '<p>Kdo pije kávu za volantem, potřebuje hrnek, který se vejde do držáku v autě. Rozhoduje průměr spodní části, proto mají hrnky jako Stanley Quencher spodek zúžený. Víčko by mělo jít otevřít jednou rukou, ideálně tlačítkem, a po napití se samo zavřít. Hrnek s velkým uchem se do některých držáků nevejde. Pokud si nejste jistí, změřte průměr držáku a porovnejte ho s rozměry v popisu.</p>'
          '<h2>Termohrnek na kávu: na co myslet</h2>'
          '<p>Káva s mlékem se v uzavřeném hrnku po několika hodinách kazí rychleji než čaj nebo černá káva, proto ji vypijte během dopoledne a hrnek hned vypláchněte. Kávové usazeniny a mléko se usazují v těsnění víčka a v tlačítkovém mechanismu, kde vytvářejí zápach. Kdo chodí s hrnkem do kavárny, ocení širší hrdlo a výšku, která se vejde pod trysku kávovaru. Některé kavárny nabízejí slevu, pokud si přinesete vlastní hrnek.</p>'
          '<h2>Termohrnek, nebo termoska</h2>'
          '<p>Termohrnek je stavěný na pití přímo z něj během cesty nebo dne. Termoska má větší objem, pevný šroubovací uzávěr a víčko, které slouží jako hrnek. Na celodenní túru v zimě, na běžky nebo na ryby je proto lepší <a href="/lahve-a-termosky/">termoska</a>, ze které se dá nalít víc lidem. Na krátkou procházku, do auta nebo do kanceláře je praktičtější termohrnek. Na teplé jídlo slouží jídelní termoska se širokým hrdlem.</p>'
          '<h2>Termohrnek na hory a do přírody</h2>'
          '<p>Na túru nebo skialp se hodí odolný termohrnek se šroubovacím uzávěrem, který snese pád na kámen. Práškově lakovaný povrch drží i v rukavicích. Na chatu a ke kempu se hodí hrnek s víčkem a uchem, ze kterého se dá pít u ohně. Kempingové hrnky na vaření, které nejsou izolované, ale dají se postavit na vařič, najdete v kategorii <a href="/kempingove-nadobi/">kempingové nádobí</a>. Izolovaný termohrnek na vařič nikdy nedávejte; teplo může poškodit vakuum a lak.</p>'
          '<h2>Jak termohrnek používat</h2>'
          '<ul><li><strong>Předehřátí:</strong> nalijte do hrnku na pár minut horkou vodu, vylijte ji a teprve pak nalijte kávu. Nápoj vydrží teplý déle.</li>'
          '<li><strong>Studené nápoje:</strong> předchlaďte hrnek studenou vodou nebo kostkami ledu.</li>'
          '<li><strong>Bez sycených nápojů:</strong> oxid uhličitý vytváří tlak, který může víčko vystřelit nebo poškodit těsnění.</li>'
          '<li><strong>Do mikrovlnné trouby nepatří:</strong> kov v mikrovlnce jiskří a hrnek ji může poškodit.</li>'
          '<li><strong>Opatrně s horkým nápojem:</strong> horký čaj v dobře izolovaném hrnku zůstane horký dlouho, při prvním doušku se snadno opaříte.</li>'
          '<li><strong>Do mrazáku ne:</strong> roztahující se led může hrnek deformovat.</li></ul>'
          '<h2>Studené nápoje a voda během dne</h2>'
          '<p>Velké termohrnky s uchem a brčkem se používají hlavně na vodu a ledové nápoje. Díky vakuu v nich led vydrží dlouho a hrnek se na stole nerosí, takže nezanechává mokré kroužky na papírech. Kdo chce pít během dne víc vody, ocení, že ji má pořád studenou na dosah. Brčko je ale potřeba pravidelně čistit tenkým kartáčkem, protože se v něm usazuje povlak.</p>'
          '<h2>Dárek a personalizace</h2>'
          '<p>Termohrnek patří k oblíbeným dárkům, protože ho využije skoro každý. Některé obchody nabízejí gravírování jména nebo vzkazu na nerezový povrch, což je odolnější než potisk. Při výběru dárku se zeptejte sami sebe, kde ho obdarovaný bude používat: do auta se hodí hrnek s tlačítkem a zúženým spodkem, do kanceláře velký hrnek s uchem a na hory odolný model se šroubovacím uzávěrem.</p>'
          '<h2>Termohrnek pro děti</h2>'
          '<p>Pro děti se vyrábějí menší termohrnky a termolahvičky s pítkem, které se dají snadno otevřít a nepoleje se z nich oblečení. Do školy a na výlet se hodí na teplý čaj v zimě a na studenou vodu v létě. Dětem nalévejte jen teplý, ne horký nápoj, protože dobře izolovaný hrnek ho dlouho nezchladí.</p>'
          '<h2>Mytí a péče</h2>'
          '<p>Termohrnek po použití vypláchněte a umyjte teplou vodou s prostředkem na nádobí, ideálně kartáčem na lahve. Víčko rozeberte podle návodu a těsnění vyndejte, protože právě pod ním se drží usazeniny. Zda hrnek snese myčku, říká výrobce; u řady modelů smí do myčky jen víčko nebo vnitřní část, vnější lak by mohl utrpět. Kávové usazeniny a zápach odstraní roztok jedlé sody nebo tablety na čištění termosek. Hrnek nechávejte schnout otevřený, aby v něm nezůstala vlhkost. Promáčklý hrnek může mít porušené vakuum, a pokud je na povrchu po nalití horkého nápoje teplý, izolace už nefunguje.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Hrnek s brčkem nebo posuvným víčkem do batohu, kde prosakuje.</li>'
          '<li>Příliš velký hrnek na jednu malou kávu, která v něm rychle vychladne.</li>'
          '<li>Model, který se nevejde do držáku v autě.</li>'
          '<li>Mytí v myčce bez ověření, že to výrobce dovoluje.</li>'
          '<li>Plastový hrnek s dvojitou stěnou bez vakua v očekávání dlouhé výdrže.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe, i s barvami a objemy skladem; objednávku dokončíte v e-shopu. U oblíbených modelů se vyplatí sledovat více obchodů, protože populární barvy se rychle vyprodávají. Na kolo se hodí lahve z kategorie <a href="/cyklo-lahve-a-drzaky/">cyklo lahve a držáky</a>, jídlo na cestu najdete v kategorii <a href="/outdoorova-strava/">outdoorová strava</a>.</p>',
    faq=[
        ('Jak dlouho udrží termohrnek kávu teplou?', 'Záleží na modelu, hlavně na víčku. Výrobci uvádějí výdrž pro plný předehřátý hrnek se zavřeným víčkem. Při častém otevírání nápoj chladne rychleji.'),
        ('Který termohrnek neteče v tašce?', 'Hrnek s těsným uzávěrem, typicky tlačítkovým nebo šroubovacím, který výrobce označuje jako nepropustný. Hrnky s brčkem nebo posuvným víčkem jsou určené k nošení ve svislé poloze.'),
        ('Mohu termohrnek mýt v myčce?', 'Jen pokud to výrobce dovoluje. U mnoha modelů smí do myčky jen víčko, vnější lak by mohl utrpět.'),
        ('Mohu do termohrnku nalít sycený nápoj?', 'Raději ne. Oxid uhličitý vytváří tlak, který může víčko vystřelit nebo poškodit těsnění.'),
        ('Jaký je rozdíl mezi termohrnkem a termoskou?', 'Z termohrnku se pije přímo a nosí se v ruce nebo v autě. Termoska má větší objem, pevný uzávěr a víčko, které slouží jako hrnek.'),
        ('Proč termohrnek zapáchá po kávě?', 'Usazeniny se drží v těsnění a mechanismu víčka. Víčko rozeberte, těsnění vyndejte a hrnek vyčistěte roztokem jedlé sody.'),
        ('Proč je dobré termohrnek předehřát?', 'Studená nerezová stěna odebere nápoji část tepla. Když hrnek na pár minut naplníte horkou vodou a pak ji vylijete, káva vydrží teplá déle.'),
        ('Hodí se termohrnek i na studené nápoje?', 'Ano. Vakuová izolace funguje oběma směry a ledový nápoj udrží studený. Hrnek se navíc na povrchu nerosí.'),
        ('Jak poznám, že termohrnek přestal izolovat?', 'Pokud je povrch po nalití horkého nápoje teplý, vakuum mezi stěnami je porušené, obvykle po pádu nebo promáčknutí.'),
    ])

# ------------------------------------------------------------------ piknikove-deky
NEW['piknikove-deky'] = dict(long=True,
    title='Piknikové deky a koše: nepromokavé deky i sady',
    desc='Piknikové deky s nepromokavým spodkem, plážové deky, proutěné koše s nádobím i chladicí tašky. Jak vybrat velikost a materiál; nabídky e-shopů.',
    intro='<p><strong>Pikniková deka</strong> má na první pohled jednoduchou práci: poskytnout suché a čisté místo na trávě. Dobrá deka toho ale umí víc. Má nepromokavý spodek, takže vlhká tráva neprosákne, měkký vršek, na kterém se dá ležet, a složí se do kompaktního balíčku s uchem. Plážové deky jsou zase lehké, písek z nich snadno opadá a v rozích mají kapsy na kolíky nebo písek, aby je neodnesl vítr. K pikniku patří i koš, často se sadou talířů, příborů a skleniček.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů, objednávku pak dokončíte v obchodě, který si vyberete. Najdete tu piknikové deky, proutěné koše, chladicí piknikové tašky i kompletní sady od značek Calter, Yate, Springos, Naturehike nebo LifeVenture. Nadřazenou kategorií jsou <a href="/kempingove-doplnky/">kempingové doplňky</a>, k pohodlnému sezení se hodí také <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</p>',
    guide='<h2>Druhy piknikových dek</h2>'
          + T(['Typ', 'Materiál', 'Kam se hodí'], [
              ['Klasická pikniková deka', 'vršek z fleece nebo akrylu, nepromokavý spodek', 'park, zahrada, louka'],
              ['Plážová deka', 'lehký nylon nebo polyester, kapsy v rozích', 'pláž, písek, vítr'],
              ['Outdoorová ultralehká deka', 'ripstopový nylon, někdy se zateplením', 'turistika, festival, batoh'],
              ['Vlněná nebo bavlněná deka', 'přírodní materiál bez nepromokavé vrstvy', 'suchá tráva, chata, auto'],
              ['Deka s izolací', 'vrstva pěny nebo vaty', 'chladnější dny, sezení na zemi na jaře a na podzim']]) +
          '<p>Pro běžný piknik v parku nejlépe poslouží klasická deka s nepromokavým spodkem. Na pláž je lepší lehká deka, ze které se písek setřese, a do batohu na túru ultralehká deka, která se sbalí do sáčku. Vlněná deka je příjemná a vypadá krásně, na vlhké trávě ale nasákne.</p>'
          '<h2>Nepromokavý spodek</h2>'
          '<p>Spodní vrstva rozhoduje o tom, zda budete sedět v suchu. Nejčastěji je z PEVA, PE nebo polyesteru s nepromokavou úpravou, některé deky mají spodek z hliníkové fólie, který zároveň odráží teplo. Tráva bývá vlhká i v létě, ráno od rosy a po dešti dlouho, a bez nepromokavé vrstvy prosákne vlhkost k vám. Nepromokavý spodek také chrání deku před blátem a zelenými skvrnami od trávy. Na druhou stranu takovou deku nelze vyprat v pračce na vysokou teplotu a nepromokavá vrstva se při ostrém přeložení může časem lámat.</p>'
          '<h2>Velikost</h2>'
          '<ul><li><strong>Kolem 130 × 150 cm:</strong> pro dva lidi a malou svačinu, vejde se do tašky.</li>'
          '<li><strong>Kolem 150 × 200 cm:</strong> pro pár s dítětem nebo pro dva, kteří si chtějí lehnout.</li>'
          '<li><strong>Kolem 200 × 200 cm a víc:</strong> rodinná deka pro čtyři a víc lidí s jídlem uprostřed.</li></ul>'
          '<p>Při výběru počítejte s tím, že na dece bude kromě lidí i koš, talíře, láhve a hračky. Deka pro dva by měla stačit k tomu, aby si oba mohli lehnout. Pokud často chodíte ve větší skupině, mohou se hodit dvě menší deky místo jedné obrovské, kterou je těžké složit a nést.</p>'
          '<h2>Skládání a přenášení</h2>'
          '<p>Většina piknikových dek se skládá do obdélníku a zapíná páskem na suchý zip s uchem nebo popruhem přes rameno. Některé mají vlastní obal nebo se srolují. Ultralehké outdoorové deky se vejdou do sáčku velikosti láhve. Při výběru se podívejte na rozměry a hmotnost složené deky, pokud ji budete nosit pěšky nebo na kole. Na pláž a ke koupališti se vyplatí deka, která se dá složit a nese se zároveň jako taška.</p>'
          '<h2>Plážové deky</h2>'
          '<p>Na pláži dece škodí dvě věci: písek a vítr. Plážové deky jsou z hladkého a lehkého materiálu, ze kterého písek snadno opadá, a v rozích mají kapsy, které se naplní pískem, nebo očka na kolíky. Takzvané „sand free“ deky mají speciální úpravu nebo síťovinu, kterou písek propadá dolů. Plážová deka rychle schne, když si na ni sednete v mokrých plavkách. Ke koupání se dále hodí <a href="/plazove-doplnky/">plážové doplňky</a> a stínění z kategorie <a href="/pop-up-a-plazove-stany/">pop-up a plážové stany</a>.</p>'
          '<h2>Piknikové koše</h2>'
          '<p>Klasický proutěný koš se dvěma víky vypadá na fotkách krásně a uvnitř skrývá výbavu pro dva nebo čtyři lidi: talíře, příbory, sklenice, ubrousky, prkénko a někdy i otvírák na víno. Proutí je ale těžší a vlhko mu neprospívá. Moderní alternativou jsou textilní piknikové tašky a koše s izolovanou vrstvou, které udrží jídlo a pití chladné. Některé mají vestavěnou chladicí přihrádku, jinde se kombinuje koš s chladicí taškou. Pro delší pobyt v horku je ale jistější skutečný <a href="/chladici-boxy/">chladicí box</a> s chladicími vložkami.</p>'
          '<p>Při výběru koše se dívejte na to, z čeho je nádobí: porcelán a sklo vypadají elegantně, ale jsou těžké a mohou se rozbít, plast a melamin jsou lehké a nerozbitné. Příbory z nerezu vydrží roky. Zkontrolujte, zda je nádobí v koši pevně uchycené, aby o sebe při nesení necinkalo. Další nádobí najdete v kategorii <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>'
          '<h2>Jak naplánovat piknik</h2>'
          '<p>Na jídlo, které se kazí, jako jsou saláty s majonézou, maso, ryby, sýry nebo dezerty se smetanou, platí jednoduché pravidlo: v létě ho nenechávejte dlouho na slunci a vezměte ho v chladicí tašce s chladicími vložkami. Ovoce, zeleninu, pečivo a suché svačiny lze vzít v koši. Pití zabalte do lahví, které nepraskají. Nezapomeňte na pytel na odpadky, vlhčené ubrousky a krém na opalování. Proti komárům a klíšťatům poslouží repelenty z kategorie <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>.</p>'
          '<p>Kdo nechce sedět na zemi, vezme si skládací židle nebo nízký stolek z kategorií <a href="/kempingove-zidle/">kempingové židle</a> a <a href="/kempingove-stoly/">kempingové stoly</a>. Děti se na pikniku nudí rychleji než dospělí, a tak se hodí míč, frisbee nebo hry z kategorie <a href="/hry-na-zahradu/">hry na zahradu</a>.</p>'
          '<h2>Pravidla v parcích a v přírodě</h2>'
          '<p>Před piknikem si zjistěte, zda je v daném parku nebo chráněném území dovoleno sedět na trávě a rozdělávat oheň. Některé městské parky mají vyhrazené plochy, v národních parcích platí přísnější pravidla. Po pikniku vše odneste s sebou, včetně drobných odpadků jako jsou víčka a obaly. Deku pokládejte mimo vyšlapané cestičky a hnízdiště a nehlučte u zvěře.</p>'
          '<h2>Piknik s malými dětmi</h2>'
          '<p>S malými dětmi se vyplatí větší deka s nepromokavým spodkem, protože se na ní bude lézt, přebalovat a rozlévat pití. Světlé deky jsou hezké na fotkách, praktičtější ale bývá vzor, na kterém není vidět každá skvrna. Svačinu dětem dejte do uzavíratelných krabiček a pití do lahví s pítkem. Deku rozložte ve stínu, protože děti se na slunci rychle přehřejí, a v trávě ji nejdřív prohlédněte, zda v ní nejsou střepy nebo vosí hnízdo.</p>'
          '<h2>Piknik na podzim a na jaře</h2>'
          '<p>Piknik se dá udělat i v chladnějších dnech, jen je potřeba počítat se studenou zemí. Deka s izolační vrstvou nebo karimatka pod ní zabrání tomu, aby zem odebírala teplo. Hodí se teplý čaj v termosce, polévka v jídelní termosce a deka navíc přes nohy. Na podzim bývá tráva vlhká skoro celý den, takže nepromokavý spodek je nutnost.</p>'
          '<h2>Péče a čištění</h2>'
          '<ul><li><strong>Po pikniku</strong> deku pořádně vytřepejte, zbavte drobků a jehličí a teprve pak ji složte.</li>'
          '<li><strong>Vlhkou deku</strong> doma rozložte a nechte úplně proschnout, jinak se v záhybech udělá plíseň a zápach.</li>'
          '<li><strong>Praní:</strong> deky s nepromokavým spodkem obvykle snesou jen ruční praní nebo šetrný program na nízkou teplotu; řiďte se štítkem.</li>'
          '<li><strong>Skvrny od trávy a jídla</strong> odstraňte co nejdříve houbičkou s mýdlem.</li>'
          '<li><strong>Proutěný koš</strong> otřete vlhkým hadříkem, nechte vyschnout a skladujte v suchu.</li>'
          '<li><strong>Nádobí</strong> po pikniku hned umyjte, aby v koši nezapáchalo.</li></ul>'
          '<h2>Pikniková deka na cesty a do auta</h2>'
          '<p>Složená pikniková deka se vyplatí mít v kufru auta po celý rok. Hodí se na zastávku u dálnice, k přebalení dítěte na trávě, na koncert pod širým nebem i jako podložka při výměně kola. Na festival se hodí deka, kterou lze snadno vyprat, protože se na ni posadí hodně lidí v různém stavu bot. Při spaní pod širákem nebo ve stanu deka nenahradí karimatku ani spacák, ale poslouží jako další vrstva navíc.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Deka bez nepromokavého spodku na vlhkou trávu.</li>'
          '<li>Rozměr, na kterém si nelehnou ani dva lidé.</li>'
          '<li>Těžký proutěný koš na pěší výlet.</li>'
          '<li>Spoléhání na chladicí přihrádku koše při celodenním horku.</li>'
          '<li>Skládání vlhké deky, ve které se pak udělá plíseň.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky obchodů vedle sebe, takže hned zjistíte, kde je deka v požadované barvě a rozměru skladem; objednávku dokončíte v e-shopu. Porovnejte rozměry rozložené i složené deky a materiál spodní vrstvy. K odpočinku v přírodě se hodí i <a href="/hamaky/">houpací sítě</a>, které se dají pověsit mezi dva stromy hned vedle deky.</p>',
    faq=[
        ('Jak velkou piknikovou deku vybrat?', 'Pro dva lidi stačí kolem 130 × 150 cm, kdo si chce lehnout, ocení 150 × 200 cm. Rodinná deka pro čtyři a víc lidí měří kolem 200 × 200 cm.'),
        ('Proč má pikniková deka nepromokavý spodek?', 'Tráva bývá vlhká od rosy nebo po dešti. Nepromokavá vrstva zabrání tomu, aby vlhkost prosákla k vám, a chrání deku před blátem.'),
        ('Lze piknikovou deku prát v pračce?', 'Záleží na štítku. Deky s nepromokavým spodkem obvykle snesou jen ruční praní nebo šetrný program na nízkou teplotu.'),
        ('Čím se liší plážová deka od piknikové?', 'Plážová deka je lehčí, písek z ní snadno opadá a v rozích má kapsy nebo očka na kolíky proti větru. Rychle schne.'),
        ('Udrží piknikový koš jídlo chladné?', 'Koš s izolovanou přihrádkou na krátkou dobu ano. Při celodenním horku je jistější chladicí box nebo taška s chladicími vložkami.'),
        ('Co by mělo být v piknikovém koši?', 'Talíře, příbory, sklenice nebo hrnky, ubrousky, prkénko a nůž. Hotové sady pro dva nebo čtyři lidi obsahují všechno najednou.'),
        ('Jakou piknikovou deku vzít s malými dětmi?', 'Větší deku s nepromokavým spodkem a vzorem, na kterém nejsou vidět skvrny. Deku pokládejte do stínu a předem prohlédněte trávu.'),
        ('Jak skladovat piknikovou deku?', 'Až úplně suchou a vytřepanou, složenou volně na suchém místě. Vlhká deka v obalu rychle zapáchá a plesniví.'),
    ])
