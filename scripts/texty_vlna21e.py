"""sporteka.cz — wave 21e (4. 11. 2026): long texts (>= 1650 words) for outdoorova-strava, lyze-komplety, plavecke-cepice, horska-kola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ outdoorova-strava
NEW['outdoorova-strava'] = dict(long=True,
    title='Outdoorová a lyofilizovaná strava na túry a kemp',
    desc='Lyofilizovaná jídla, hotové sáčky, sušené ovoce a dezerty na túry. Jak vybrat podle délky výpravy, váhy, vaření a porovnat nabídky obchodů.',
    intro='''<p>Jídlo v batohu rozhoduje o tom, jestli vás večer na horské chatě nebo v bivaku čeká příjemný odpočinek, nebo promrzlé louskání studených konzerv. Outdoorová strava vznikla pro situace, kdy je každý gram na zádech znát, vařič je jediný spotřebič a dřez nahrazuje hrnek s vodou. Dobré jídlo na cestu je lehké, vydrží měsíce v obalu a z pytlíku se promění v teplou porci po pár minutách.</p>
<p>V této kategorii najdete lyofilizovaná jídla, hotové sterilované porce, polévky, kaše, dezerty i sušené ovoce od značek LYOfood, Expres menu, Adventure menu, Firepot, Voyager nebo Food Force. Pohodlně si porovnáte nabídky českých obchodů a vybereme vám i doplňky z kategorií <a href="/vareni-v-prirode/">vaření v přírodě</a>, <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/lahve-a-termosky/">láhve a termosky</a>. Níže je přehled druhů jídel, rady pro plánování zásob a tipy, jak je připravit.</p>''',
    guide='''<h2>Jaké druhy outdoorové stravy existují</h2>
<p>Pod pojmem outdoorová strava se skrývá několik technologií, které se liší hmotností, přípravou a trvanlivostí. Než začnete vybírat konkrétní chuť, rozhodněte se, jakou formu budete na trase nosit. Rozdíl je znát už na váze zabaleného jídla na čtyři dny.</p>'''
          + T(['Typ jídla', 'Jak vypadá', 'Příprava', 'Hodí se na'], [
              ['Lyofilizované hlavní jídlo', 'suchá lehká směs v sáčku', 'zalít horkou vodou a počkat', 'vícedenní treky, kde záleží na váze'],
              ['Sterilovaná hotová jídla', 'plná porce v sáčku nebo konzervě', 'ohřát ve vodě nebo jíst studené', 'kemp u auta, kánoe, základní tábor'],
              ['Sušené polévky a kaše', 'prášek nebo granulát', 'rozmíchat ve vodě', 'rychlá snídaně nebo teplá večeře'],
              ['Lyofilizované ovoce', 'křupavé kousky nebo plátky', 'bez přípravy', 'svačina, přísada do kaše, čaje a müsli'],
              ['Dezerty a sladké porce', 'mousse, crumble, pudink', 'zalít vodou nebo zamíchat', 'zpestření večera po náročném dni']]) +
          '''<p>Lyofilizace znamená sušení zmrazeného jídla ve vakuu. Voda z potraviny přejde rovnou z ledu do páry, takže se zachovává tvar a struktura kousků a zároveň zmizí většina váhy. Proto je lyofilizované jídlo suché, lehké a velmi dlouho trvanlivé, pokud je obal nepoškozený. Hotové sterilované porce naproti tomu obsahují vodu a váží víc, zato se obejdou bez vaření a hodí se tam, kde zátěž nehraje roli.</p>
<h2>Značky a jejich styl</h2>
<p>Největší část nabídky tvoří české a slovenské značky. '''
          f'{B(("lyofood", "LYOfood"), ("expres-menu", "Expres menu"), ("adventure-menu", "Adventure menu"), ("adventure-food", "Adventure Food"), ("voyager", "Voyager"), ("firepot", "Firepot"), ("food-force", "Food Force"), ("tactical-foodpack", "Tactical Foodpack"), ("trek-n-eat", "Trek n Eat"))}. '
          '''Každá se zaměřuje na trochu jiné publikum: některé nabízejí široké menu lyofilizovaných jídel ve velikostech pro jednoho, jiné hotové sáčky určené pro kempování, a další jídla v armádním stylu pro dlouhé akce. Ovoce k mlsání a do kaší najdete mimo jiné u značek GymBeam, Wolfberry nebo Allnature. Zajímavé je porovnat gramáž a počet porcí, protože údaj „2 porce“ u jedné značky může odpovídat jedné velké večeři u jiné.</p>
<h2>Jak plánovat zásoby na výpravu</h2>
<h3>Spočítejte dny a jídla</h3>
<p>Základ je jednoduchý: napište si, kolik snídaní, večeří a svačin potřebujete, a přidejte jednu rezervní porci na případné zdržení. Počítejte s tím, že při pohybu v horách a v chladu bývá chuť k jídlu větší než doma. Raději mějte o něco víc lehké svačiny, třeba ovoce, tyčinky nebo oříšky, než zbytečně těžké konzervy.</p>
<h3>Rozložení během dne</h3>
<ul><li><strong>Snídaně:</strong> kaše, müsli s lyofilizovaným ovocem nebo teplá polévka, která zahřeje po noci ve stanu.</li>
<li><strong>Svačina za pochodu:</strong> věci, které nevyžadují vařič: ovoce, ořechy, tyčinky a gely, které najdete v kategorii <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>.</li>
<li><strong>Večeře:</strong> hlavní jídlo s rýží, těstovinami nebo bramborami, ideálně teplé a výrazněji dochucené.</li>
<li><strong>Pití:</strong> čaj, kakao nebo iontový nápoj z oddílu <a href="/iontove-napoje/">iontové nápoje</a>.</li></ul>
<h2>Jak se jídlo připravuje</h2>
<p>Pytlík otevřete, případně vyndejte sáček s pohlcovačem kyslíku, který se nejí. Dovnitř nalijte horkou vodu podle údaje na obalu, promíchejte, uzavřete a nechte stát. Většina jídel potřebuje několik minut, hustší porce s rýží nebo těstovinami trvají déle. Pokud pytlík zabalíte do bundy nebo čepice, jídlo zůstane teplé déle a lépe se rozpustí. Voda by měla být skutečně horká, ne jen vlažná, jinak zůstanou kousky tvrdé.</p>
<p>Příprava přímo v pytlíku šetří nádobí a mytí. Přesto se hodí mít lžíci s dlouhou rukojetí, aby se dosáhlo až na dno. Odpadky z obalů odneste s sebou, prázdný sáček váží minimum. K čisticím a vařicím potřebám se hodí <a href="/kempingove-nadobi/">kempingové nádobí a příbory</a> a vařič z kategorie <a href="/kemping/">kemping</a>.</p>
<h3>Kolik vody a kolik paliva</h3>
<p>Každé jídlo uvádí množství vody a vařič je potřeba počítat dopředu. Čím víc teplých jídel a čajů, tím víc paliva a delší sestup k potoku pro vodu. Na výpravách, kde je voda vzácná, se hodí jídla, která se dají jíst i s menším množstvím tekutiny, nebo ovoce a svačiny bez vaření. V zimě počítejte s tím, že tání sněhu spotřebuje mnohem víc plynu než ohřev vody z potoka.</p>
<h2>Výběr podle typu výpravy</h2>
<ul><li><strong>Jednodenní túra:</strong> stačí svačiny, sušené ovoce a sendvič, teplé jídlo se většinou nevyplatí.</li>
<li><strong>Víkend na chatě nebo v kempu:</strong> hotová jídla v sáčku a polévky, kde váha nehraje velkou roli a jde hlavně o pohodlí.</li>
<li><strong>Vícedenní trek bez doplňování:</strong> lyofilizovaná jídla s nejlepším poměrem váhy a velikosti porce, doplněná ovocem a lehkými svačinami.</li>
<li><strong>Zimní výstup a skialp:</strong> něco teplého, tučnějšího a rychle připraveného, a k tomu termoska z oddílu <a href="/lahve-a-termosky/">láhve a termosky</a>.</li>
<li><strong>Kajak a kánoe:</strong> lyofilizované porce se vejdou do vodotěsného pytle a bez problémů přežijí vlhko, pokud je obal celý.</li>
<li><strong>Rodinné kempování:</strong> hotové porce, kaše a dezerty, které děti znají a které se připraví bez složitého vaření.</li></ul>
<h2>Na co se dívat na obalu</h2>
<p>Než jídlo vložíte do košíku, projděte si údaje na stránce produktu. Nejdůležitější je gramáž porce a počet porcí, protože hmotnost celého balení sama o sobě moc neříká. Podívejte se na seznam složek a na upozornění na alergeny, zvlášť u jídel s ořechy, mlékem, lepkem nebo sójou. Pro vegetariány a vegany existují samostatné varianty, které bývají označené na obalu. Nezapomeňte na datum minimální trvanlivosti, které u lyofilizovaných jídel bývá dlouhé, ale u sterilovaných porcí kratší.</p>
<h3>Chuť a koření</h3>
<p>V terénu chutná jídlo jinak než doma. Výška, únava a chlad otupují chuť, takže výraznější a slanější jídla zpravidla vyhovují víc než jemné. Do batohu se vyplatí přibalit malé sáčky se solí, kořením nebo ostrou omáčkou. Před velkou výpravou si jednotlivé druhy vyzkoušejte doma a zjistěte, jaká jídla vám chutnají a nezpůsobují trávicí potíže.</p>
<h2>Lyofilizované ovoce a dezerty</h2>
<p>Křupavé lyofilizované ovoce je nejuniverzálnější část nabídky. Jahody, maliny, višně, mango nebo brusinky se jedí přímo ze sáčku, přidávají do kaše, rozmíchají v čaji nebo drtí na jogurt po návratu domů. Kousky jsou lehké, ale objemné, proto se do batohu vejdou hůř, než byste čekali. Dezerty typu mousse nebo crumble se připravují stejně jako hlavní jídla a večer ve stanu dokážou potěšit víc než další těstoviny. Pokud ovoce kupujete jen na mlsání, sledujte, zda je bez přidaného cukru, a porovnejte gramáž balení, protože ta je u ovoce často jen několik desítek gramů.</p>
<h2>Skupiny, děti a společné vaření</h2>
<p>Při výpravě ve více lidech se vyplatí vybrat stejná jídla a připravovat je společně z jednoho kotlíku nebo postupně v pytlících. Děti jedí raději známé chutě, takže zkuste kaše, těstoviny nebo sladké porce, které už ochutnaly doma. Pro dospívající s velkým apetitem počítejte větší porce a přidejte svačiny. Ve skupině je také praktické rozdělit nošení jídla podle dnů, aby každý nesl stejnou váhu a zásoby se neztratily s jedním batohem.</p>
<h2>Skladování a balení</h2>
<p>Nepoškozený obal lyofilizovaného jídla chrání obsah před vlhkostí a kyslíkem. Skladujte ho na suchém a chladnějším místě, mimo přímé slunce a ostré předměty. V batohu pytlíky snadno zmáčknete, proto je zabalte tak, aby nebyly na dně pod stanem nebo vařičem. Z bezpečnostních důvodů nevyhazujte nesnědené zbytky do přírody, odneste je zpátky.</p>
<p>Pokud je nutné ušetřit objem, vyndejte jídla z krabiček a přebalte je do jednoho pevného pytle. Odpadá tím vzduch a pytlíky se lépe skládají. Rozdělte je podle dnů do menších sáčků s popiskem, v noci pak nemusíte hledat správný obsah. Vhodný objem batohu a systém zavazadla najdete v kategoriích <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/spaci-pytle/">spací pytle</a>.</p>
<h2>Časté chyby při nákupu a přípravě</h2>
<ul><li>Zásoba jen z jedné chuti, která omrzí po třetím dni.</li>
<li>Příliš málo vody na ohřev, takže jídlo zůstane částečně tvrdé.</li>
<li>Nezkoušení nových jídel před cestou a následné trávicí potíže.</li>
<li>Přebalení obsahu do nekvalitního sáčku, který propustí vlhkost.</li>
<li>Opomenutí paliva do vařiče, když počítáte jen potraviny.</li>
<li>Pouze lyofilizovaná jídla bez svačin, které se jedí za chůze.</li></ul>
<h2>Doplňky k jídlu na cestu</h2>
<p>Kromě jídla samotného se vyplatí pomyslet na menší věci. K přípravě stačí kvalitní lžíce, hrnek a ohřívač vody; podrobnosti najdete v rubrice <a href="/vareni-v-prirode/">vaření v přírodě</a>. Na pití se hodí skládací láhev nebo vak, k tomu filtr nebo tablety na úpravu vody. V sekci <a href="/sportovni-vyziva/">sportovní výživa</a> najdete tyčinky a nápoje, které doplňují teplá jídla při dlouhých etapách.</p>''',
    faq=[
        ('Jaký je rozdíl mezi lyofilizovaným a sterilovaným jídlem?', 'Lyofilizované jídlo je zmrazené a vysušené ve vakuu, takže je velmi lehké a stačí je zalít vodou. Sterilované je tepelně ošetřené v obalu, obsahuje vodu, je těžší, ale jí se rovnou.'),
        ('Jak dlouho vydrží lyofilizovaná jídla?', 'Při nepoškozeném obalu a skladování v suchu a chladu bývá trvanlivost dlouhá. Přesné datum je vždy uvedeno na obalu a řídí se jím i skladování.'),
        ('Musím mít vařič, abych jídlo připravil?', 'Většina lyofilizovaných jídel potřebuje horkou vodu, takže vařič nebo termoska se hodí. Ovoce, svačiny a sterilované porce jíst můžete i bez ohřevu.'),
        ('Kolik porcí na osobu a den mám plánovat?', 'Záleží na výdeji energie, počasí a výšce. Obvykle snídaně, večeře a několik svačin, ale gramáž porcí se mezi značkami liší, proto si porovnejte údaje na stránce produktu.'),
        ('Je porce označená „2 porce“ pro dva lidi?', 'Ne vždy. Výrobci počítají porci různě a hladový turista po celém dni zvládne i jednu celou. Řiďte se gramáží a vlastním apetitem, ne jen označením.'),
        ('Dají se jídla připravit i studenou vodou?', 'Některá ano, ale trvá to mnohem déle a výsledek bývá méně chutný. Pokud chcete vynechat vaření, zvolte ovoce, kaše určené pro studenou přípravu nebo hotové porce.'),
        ('Jsou v nabídce jídla pro vegetariány a bezlepkovou stravu?', 'Ano, najdete vegetariánské a veganské varianty a občas i jídla bez lepku. Složení a alergeny vždy zkontrolujte přímo u produktu, protože se u výrobců mění.'),
        ('Co dělat s prázdnými obaly po jídle?', 'Obaly zabalte a odneste s sebou do odpadkového koše. Po vyjedení váží minimum a zanechání odpadu v přírodě je nepřípustné.'),
        ('Hodí se tato jídla i do nouzové zásoby doma?', 'Díky dlouhé trvanlivosti a nízké váze se hodí do auta, na chatu nebo jako rezerva pro výpadek proudu. Zkontrolujte si ale datum trvanlivosti a občas zásobu obměňte.'),
        ('Proč jsou některá jídla dražší než jiná?', 'Cenu ovlivňuje technologie, množství masa a kvalita surovin, velikost porce i značka. Proto porovnávejte cenu za gramáž a za porci, nejen za balení.'),
    ],
)

# ------------------------------------------------------------------ lyze-komplety
NEW['lyze-komplety'] = dict(long=True,
    title='Lyže s vázáním: komplety pro dospělé i děti',
    desc='Sjezdové lyže s namontovaným vázáním pro dospělé, dámy i děti. Jak vybrat délku, rádius, šířku a typ vázání a porovnat nabídky obchodů.',
    intro='''<p>Komplet znamená, že lyže a vázání už patří k sobě a nemusíte zjišťovat, které vázání sedne na kterou lyži. U většiny modelů je vázání namontované na integrované liště nebo na speciální desce od výrobce, takže zbývá jen seřízení podle bot a váhy lyžaře. Pro začátečníky, rodiny s dětmi i rekreační jezdce, kteří lyžují několik dní v sezóně, jde o nejpřímější cestu k vlastnímu vybavení.</p>
<p>Ve Sportece porovnáte nabídky českých obchodů u lyží značek Rossignol, Elan, Head, Atomic, Fischer, Salomon, Wedze, Nordica nebo Dynastar, včetně dámských a juniorských modelů. K lyžím patří <a href="/lyzarske-boty/">lyžařské boty</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-helmy/">helma</a>. Níže vysvětlíme, jak číst technické údaje, jak zvolit délku a šířku a na co nezapomenout při nákupu a servisu.</p>''',
    guide='''<h2>Co je v kompletu a co v něm není</h2>
<p>Lyže s vázáním tvoří jedno zboží, které se prodává společně. V popisu uvidíte zápis typu „lyže + vázání“, například model lyže a za plusem označení vázání, často s doplňkem GW. Zkratka GW říká, že vázání zvládne i boty s podrážkou GripWalk, tedy se zaoblenou protiskluzovou patou, v které se líp chodí. Hole, boty ani helma součástí kompletu nebývají, výjimkou jsou některé nejlevnější dětské sady.</p>
<p>Výhoda kompletu je v tom, že výrobce lyže a vázání odladil. Lyže mívají speciální montážní plochu, která umožňuje posouvat vázání a pomáhá tlumit vibrace. U volného vázání, které se koupí zvlášť, je třeba dbát na kompatibilitu a nechat montáž udělat v servisu. Najdete je v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>.</p>
<h2>Druhy lyží podle terénu</h2>'''
          + T(['Typ', 'Šířka pod nohou', 'Chování', 'Pro koho'], [
              ['Carvingové', 'užší, zhruba do 80 mm', 'rychlé přenášení z hrany na hranu', 'začátečníci a jezdci na upravených sjezdovkách'],
              ['Sportovní carving', 'úzké, pevná konstrukce', 'přesnost a stabilita ve vyšší rychlosti', 'pokročilí, kteří chtějí tlačit na hrany'],
              ['Allmountain', 'střední šířka', 'univerzální na sjezdovku i mimo ni', 'rekreační lyžaři s různým terénem'],
              ['Freeride', 'široké, často nad 100 mm', 'nosnost v hlubokém sněhu', 'zkušení jezdci mimo sjezdovku'],
              ['Dětské a juniorské', 'užší, měkčí', 'odpouštějící, lehce ovladatelné', 'děti od prvních oblouků po závodní kluby']]) +
          '''<p>Pro většinu lidí je rozumný výběr mezi carvingem a allmountainem. Užší lyže snáz zatáčí, širší lépe plují v neupraveném sněhu, ale na tvrdé podložce vyžadují víc práce. Pokud jezdíte hlavně na sjezdovce s občasným výletem do hlubokého sněhu, stačí allmountain střední šířky.</p>
<h2>Jak zvolit délku lyží</h2>
<p>Délka se odvíjí od výšky, váhy, úrovně a stylu. Začátečník volí kratší lyže, které se snáze otáčejí, pokročilý delší pro vyšší stabilitu. Obecně platí, že dámské a juniorské lyže jsou o něco kratší než pánské a že se lyže vyrábějí v délkách po pěti centimetrech a doporučení se mezi výrobci mírně liší.</p>'''
          + T(['Úroveň', 'Orientační délka vůči postavě', 'Poznámka'], [
              ['Začátečník', 'od brady po nos', 'lépe se otáčí a odpouští chyby'],
              ['Rekreační pokročilý', 'od nosu po čelo', 'nejčastější volba pro sjezdovku'],
              ['Sportovní jezdec', 'po čelo nebo výše', 'stabilita ve vyšší rychlosti'],
              ['Dítě', 'zhruba po bradu až nos', 'kratší, aby si dítě lyže ovládlo samo']]) +
          '''<p>Při váhání mezi dvěma délkami vezměte v úvahu váhu a odvahu. Těžší lidé a rychlejší jezdci mohou jít do delší lyže, lehčí a ti, kdo jezdí opatrně, do kratší. Výrobce často uvádí doporučený rozsah váhy nebo výšky v popisu modelu.</p>
<h2>Parametry, které vás zajímají</h2>
<h3>Rádius</h3>
<p>Rádius udává, jak velký oblouk lyže sama vyřeže. Menší číslo znamená těsnější oblouky, větší delší a klidnější. Pro začátečníky a rekreační jezdce se hodí střední až menší rádius, delší oblouky patří rychlým a zkušeným lyžařům.</p>
<h3>Rocker, camber a konstrukce</h3>
<p>Camber je klasický prohnutý profil pod botou, který zajišťuje přilnavost na hranách. Rocker je zdvižená špička a někdy i pata, která pomáhá v hlubokém sněhu a usnadňuje zatáčení. Hybridní profily kombinují obě vlastnosti. Jádro lyže bývá dřevěné nebo kombinované, vrstvy kovu zpevňují lyži a zlepšují stabilitu, ale zvyšují hmotnost.</p>
<h3>Vázání v kompletu</h3>
<p>Vázání se přizpůsobuje bootě a váze lyžaře. Důležitá je nastavitelná hodnota uvolnění, kterou má seřídit servis podle váhy, výšky, věku a stylu jízdy. Dětská vázání mají měkčí rozsah a často jednoduchý systém pro nastavení délky boty. Dospělé modely se liší maximální hodnotou, kterou zvládnou, a pokročilí lyžaři by měli hledat vázání s vyšším rozsahem než začátečníci.</p>
<h2>Dámské, pánské a dětské komplety</h2>
<p>Dámské lyže bývají lehčí a měkčí, často s posunutým montážním bodem tak, aby se zohlednilo rozložení váhy. Pánské jsou pevnější a odolnější. Rozhodující je ale hlavně váha, výška a styl, takže silnější žena může zvolit pánský model a naopak. Dětské komplety jsou nejjednodušší: kratší lyže s vázáním s jednodušším seřízením a barevným designem, který děti motivuje. U rostoucích dětí nekupujte lyže o moc větší, protože se s nimi hůř jezdí a děti ztratí motivaci. Pokud se vám nedaří vybrat, podívejte se i do kategorie <a href="/detske-lyze/">dětské lyže</a>.</p>
<h2>Značky v nabídce</h2>
<p>Širokou nabídku komplet lyží tvoří '''
          f'{B(("rossignol", "Rossignol"), ("elan", "Elan"), ("head", "Head"), ("atomic", "Atomic"), ("fischer", "Fischer"), ("salomon", "Salomon"), ("wedze", "Wedze"), ("nordica", "Nordica"), ("dynastar", "Dynastar"), ("k2", "K2"))}. '
          '''Najdete tu ale také kusy od Völklu, Kästle nebo Dynafit. Rossignol a Elan mají velký počet lyží a vázání od jednoho výrobce, Head a Atomic zase nabízejí řady odstupňované podle úrovně jezdce. Wedze je obchodní značka řetězce Decathlon a míří na začátečníky i rekreační jezdce. Při porovnávání se zaměřte na typ lyže, ne jen na značku, protože i stejný výrobce má několik řad pro zcela odlišné lyžaře.</p>
<h2>Výběr podle úrovně a stylu jízdy</h2>
<ul><li><strong>První dny na sněhu:</strong> kratší carvingové lyže s měkčím flexem a jednoduchým vázáním, které odpouští chyby.</li>
<li><strong>Rodinný rekreační jezdec:</strong> allmountain střední šířky, univerzální lyže, která zvládne i zasněženou trať.</li>
<li><strong>Sportovní jízda na hranách:</strong> pevnější carving s kovovou vrstvou a vázáním s vyšším rozsahem.</li>
<li><strong>Prašan a volný terén:</strong> širší freeridové lyže, často s rockerem; hledejte je i v kategorii <a href="/sjezdove-lyze/">sjezdové lyže</a>.</li>
<li><strong>Výlety na skialpech:</strong> klasický komplet nestačí, mrkněte na <a href="/skialpove-lyze/">skialpové lyže</a>, které mají lehčí konstrukci a jiné vázání.</li></ul>
<h2>Boty a vázání musí spolupracovat</h2>
<p>Nejčastější technická chyba při koupi kompletu je ta, že boty a vázání nemají kompatibilní podrážky. Klasické alpské boty a boty s podrážkou GripWalk potřebují vázání, které to dovoluje. Pokud vázání nese označení GW, zvládne obě varianty, ale ověřte to vždy u konkrétního modelu. Seřízení vázání na botu dělá servis a měl by ho provést před první jízdou, bez ohledu na to, zda je komplet nový, nebo bazarový. Přehled bot najdete v kategorii <a href="/lyzarske-boty/">lyžařské boty</a>.</p>
<h2>Péče a servis</h2>
<p>Po sezóně lyže očistěte, osušte, promažte hrany a uložte s vrstvou ochranného vosku na skluznici. Před další sezónou nechte seřídit vázání, zkontrolovat stav hran a naostřit je. Pravidelné mazání zlepšuje kluznost a prodlužuje život skluznice. Doma můžete lyže ošetřit sami, ale nastavení vázání je z bezpečnostních důvodů záležitost autorizovaného servisu. Prostředky najdete v oddílu <a href="/lyzarske-vosky/">vosky a mazání</a>. Na přepravu se hodí <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže</a>.</p>
<h2>Jak číst popis modelu v obchodě</h2>
<p>Název kompletu bývá zkratkový a skrývá víc údajů, než se zdá. Za jménem lyže následuje často číslo, které označuje šířku pod nohou nebo řadu, potom typ vázání a doplňky jako GW nebo označení pro děti. Tytéž lyže se někdy prodávají s různými vázáními, takže dvě nabídky s podobným názvem mohou mít jinou výbavu. Při porovnávání proto kontrolujte celý zápis, ne jen jméno lyže. Pozor také na ročník: starší model z minulé sezóny bývá technicky stejný, ale liší se grafikou, a hodí se, pokud vám nevadí výprodejový design. Důležité je zkontrolovat i dostupnost konkrétní délky, protože nejčastěji se vyprodávají právě střední velikosti.</p>
<h2>Vybavení a bezpečnost dětí</h2>
<p>U dětí stojí za zvážení pravidelná výměna lyží, protože rostou rychleji než se opotřebuje výbava. Nejpraktičtější je koupit kvalitní sadu a po sezóně ji prodat dál, případně využít půjčovnu. K dětskému kompletu patří vždy helma, páteřní chránič doporučený na svazích a rukavice s pevným zápěstím. Vázání musí být seřízené podle váhy, ne podle přání dítěte, a malé děti ještě nepotřebují vyšší nastavení. Podívejte se i na <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, které rodinnou výbavu doplní.</p>
<h2>Časté chyby při nákupu</h2>
<ul><li>Příliš dlouhé lyže „pro růst“, které začátečníka zbytečně unaví.</li>
<li>Koupě kompletu bez ověření, zda sedí na vaše boty.</li>
<li>Přehlédnutí, že vázání potřebuje seřízení servisem před první jízdou.</li>
<li>Volba široké freeridové lyže na sjezdovku, na které se hůř ovládá.</li>
<li>Nákup podle designu bez ohledu na úroveň jezdce.</li>
<li>Zapomenutí na další výbavu: helmu, hole a ochranu zad u dětí.</li></ul>
<h2>Co komplet nezahrnuje</h2>
<p>Komplet řeší lyže a vázání, někdy i hole. Další výbavu je potřeba doplnit zvlášť: <a href="/lyzarske-helmy/">lyžařskou helmu</a>, <a href="/lyzarske-bryle/">brýle</a> a <a href="/lyzarske-rukavice/">rukavice</a>. Oblečení řešte po vrstvách, od <a href="/lyzarske-termopradlo/">termoprádla</a> po <a href="/lyzarske-bundy/">lyžařskou bundu</a>, a více najdete v kategorii <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>
<h2>Kdy nakupovat a co s sebou</h2>
<p>Nabídka velikostí je nejširší na podzim, před sezónou, kdežto po Vánocích zbývají jen vybrané délky. Pokud si nejste jistí, vyplatí se vyzkoušet lyže v půjčovně a pak teprve koupit. K novému kompletu doplňte <a href="/lyzarske-helmy/">helmu</a>, <a href="/lyzarske-bryle/">brýle</a>, <a href="/lyzarske-rukavice/">rukavice</a> a vhodné <a href="/lyzarske-ponozky/">ponožky</a>. Oblečení najdete v kategorii <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>''',
    faq=[
        ('Co je výhodnější: komplet, nebo lyže a vázání zvlášť?', 'Komplet je jednodušší a výrobce lyže a vázání odladil. Zvlášť se koupí, když chcete konkrétní vázání nebo máte speciální požadavky.'),
        ('Musím nechat vázání seřídit i u nového kompletu?', 'Ano. Vázání se nastavuje podle váhy, výšky, úrovně a bot, proto by to měl před první jízdou udělat servis.'),
        ('Co znamená GW v názvu vázání?', 'Označuje vázání kompatibilní s botami s podrážkou GripWalk. Takové vázání zvládne obvykle i klasické alpské boty, ale ověřte to u konkrétního modelu.'),
        ('Jak dlouhé lyže mám zvolit?', 'Podle výšky, váhy a úrovně. Začátečníci volí kratší, od brady po nos, pokročilí delší, po čelo. Pomůže tabulka výrobce.'),
        ('Jaký je rozdíl mezi carvingem a allmountainem?', 'Carving je užší a vyniká na upravených sjezdovkách. Allmountain je širší a univerzálnější, zvládne i neupravený sníh.'),
        ('Hodí se komplet pro začínající dítě?', 'Ano, hlavně pro děti, které lyžují pravidelně. Vyberte kratší lyže s měkčím flexem a ověřte, že vázání jde nastavit na délku boty.'),
        ('Kolik let vydrží lyže?', 'Při pravidelné péči slouží lyže mnoho sezón. Vázání má omezenou životnost a starší kusy někteří servisy odmítají seřizovat.'),
        ('Jak lyže uložit přes léto?', 'Očistěte je, osušte, naneste ochranný vosk a uložte na suchém a chladném místě ve vaku, nejlépe svázané a ne opřené natrvalo v jedné poloze.'),
        ('Dají se lyže z kompletu používat na skialpy?', 'Klasické sjezdové komplety nejsou pro skialpové túry určené. Pro stoupání potřebujete jiné vázání, lehčí lyže a pásy.'),
        ('Jak poznat dámské a pánské lyže?', 'Dámské jsou obvykle lehčí a měkčí, často s jiným rozložením hmotnosti. Rozhoduje ale váha a styl jízdy, ne pohlaví.'),
    ],
)

# ------------------------------------------------------------------ plavecke-cepice
NEW['plavecke-cepice'] = dict(long=True,
    title='Plavecké čepice: silikonové, textilní, dětské',
    desc='Plavecké čepice silikonové, latexové i textilní, na dlouhé vlasy, závodní a dětské. Jak zvolit materiál a velikost a porovnat nabídky obchodů.',
    intro='''<p>Plavecká čepice se v bazénu často vyžaduje a z dobrého důvodu: drží vlasy mimo obličej, chrání je před chlorovanou vodou a snižuje odpor těla při plavání. Pro rekreační plavce je to praktická pomůcka, pro trénující plavce a závodníky samozřejmá součást výbavy. Čepice se liší materiálem, tvarem i velikostí, a právě podle toho se rozhoduje, jak dlouho vydrží a jak pohodlně sedí.</p>
<p>Na Sportece najdete čepice značek Aqua Speed, Speedo, Arena, Zoggs, Nike, Finis, Mad Wave nebo Effea a mnoho dalších, od jednoduchých dětských po závodní modely. Porovnáte nabídky českých obchodů a snadno doplníte výbavu o <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-pomucky/">plavecké pomůcky</a> a <a href="/plavky/">plavky</a>. V textu níže jsou rady pro volbu materiálu, velikosti a péči.</p>''',
    guide='''<h2>Materiály plaveckých čepic</h2>
<p>Materiál určuje, jak čepice sedí, jak se chová ve vodě a jak dlouho vydrží. Nejčastější jsou silikon, latex a textil, každý má své přednosti i nevýhody a hodí se pro jiný druh plavání.</p>'''
          + T(['Materiál', 'Vlastnosti', 'Nevýhody', 'Vhodné pro'], [
              ['Silikon', 'pružný, odolný, nepropouští vodu, dlouhá životnost', 'může tahat vlasy při nasazování', 'trénink, pravidelné plavání, plavci s alergií na latex'],
              ['Latex', 'tenký, velmi lehký, těsně přiléhá', 'rychleji se trhá, u citlivých osob dráždí kůži', 'závody a krátké tréninky'],
              ['Textil (nylon, lycra)', 'měkký, příjemný, nešustí', 'propouští vodu, vlasy zůstanou mokré', 'rekreační plavání a aquaaerobik'],
              ['Textil se silikonovým povrchem', 'komfort textilu s částečnou ochranou', 'ne tak těsný jako čistý silikon', 'děti a ti, kdo silikon nesnášejí'],
              ['Neoprenové a speciální', 'tepelná izolace', 'tlustší a méně pružné', 'plavání ve studené otevřené vodě']]) +
          '''<p>Silikon je dnes nejrozšířenější volba a zároveň nejuniverzálnější. Latex nemusí vyhovovat lidem s citlivostí na tento materiál, takže pro rodinu a děti bývá bezpečnější silikon nebo textil. Pokud plavete hlavně pro radost a nepotřebujete, aby vlasy zůstaly zcela suché, stačí textilní čepice. Pro triatlon a plavání v otevřené vodě vybírejte čepici zářivé barvy, aby vás ostatní lépe viděli.</p>
<h2>Čepice podle vlasů a velikosti hlavy</h2>
<h3>Krátké vlasy</h3>
<p>Při krátkých vlasech postačí standardní velikost, která těsně sedí a nesvírá spánky. U silikonu je důležité, aby čepice při nasazování nesjížděla do čela. Pro děti existují menší velikosti, často označené jako junior nebo kids.</p>
<h3>Dlouhé a husté vlasy</h3>
<p>Dlouhé vlasy se nejlépe skládají do uzlu nebo drdolu, aby čepice nebyla vypouklá na jedné straně. Na trhu jsou speciální modely na dlouhé vlasy, které jsou objemnější a mají prodloužený zadní díl. Hledejte označení jako „long hair“ nebo „volume“. Při nasazování držte čepici za okraje a nenatahujte ji prudce, aby nepraskla.</p>
<h3>Velká hlava a vlasy s copánky</h3>
<p>Pokud máte velkou hlavu nebo hustší účes, zvolte větší velikost nebo elastický textil. Příliš těsná čepice tlačí do čela a způsobuje bolest hlavy. Příliš velká se naopak vlní a ve vodě sjíždí. Pomůže vždy zkusit vybrat podle obvodu hlavy, který výrobci uvádějí v tabulce.</p>
<h2>Typy čepic podle použití</h2>
<ul><li><strong>Rekreační čepice:</strong> pohodlná a odolná, často s potiskem nebo barevným vzorem, určená k častému plavání v bazénu.</li>
<li><strong>Závodní a startovací:</strong> tvarované, vyšší a těsnější, minimalizují odpor a drží přesně na hlavě. Najdete je například u značek Speedo, Arena a Zoggs.</li>
<li><strong>Dětské s motivy:</strong> barevné čepice s postavičkami, které děti motivují. Hledejte měkký silikon bez ostrých švů.</li>
<li><strong>S kapsami na uši:</strong> mají tvarované kapsy, které chrání uši před vodou, a hodí se pro plavce s citlivýma ušima.</li>
<li><strong>Na dlouhé vlasy:</strong> větší objem a prodloužený zadní díl.</li>
<li><strong>Čepice pro plavání v otevřené vodě:</strong> výrazné barvy, někdy silnější materiál, který udrží teplo. Pro studenou vodu se hodí i neopren.</li></ul>
<h2>Tvar, švy a střih</h2>
<p>Dvě čepice ze stejného materiálu mohou sedět úplně odlišně podle střihu. Ploché modely jsou nejjednodušší a nejlevnější na výrobu, ale na hlavě mohou tvořit záhyb. Tvarované modely mají předpřipravenou křivku hlavy, takže přiléhají hladce a lépe drží při skoku z bloku nebo při obrátce. Dobrá čepice má plynulý okraj bez ostrého švu, který by tlačil na čelo nebo za ucho. Některé modely mají zesílený hřeben nebo matnou texturu proti klouzání brýlí. Pokud si nejste jistí, začněte klasickým silikonovým střihem v tabulkové velikosti a zjistěte, zda vám vyhovuje.</p>
<h2>Barvy, potisk a týmové čepice</h2>
<p>Barevné vzory nejsou jen ozdoba. Plavecké kluby často používají jednotné barvy, aby trenér poznal své svěřence, a v otevřené vodě pomáhá výrazná čepice při orientaci a bezpečnosti. Potisk na silikonu se časem otírá, zejména pokud čepici nasazujete s ostrými nehty nebo ji skladujete ve společné tašce s ostrými předměty. U dětských čepic s postavičkami dbejte na kvalitní tisk, který se nezačne loupat. Pro plavecký oddíl nebo školní kurz se vyplatí vybírat čepice stejné barvy a velikosti, aby se děti nemusely dohadovat o svých kusech.</p>
<h2>První čepice pro začátečníky</h2>
<p>Kdo se k plavání teprve vrací, nemusí hned kupovat nejdražší model. Rozumný start je jednoduchá silikonová čepice střední velikosti, která snese i mnoho návštěv bazénu. Vyzkoušejte, jestli vám nevadí tlak na čele a jestli drží i při zvýšeném tempu. Až zjistíte, že plavete pravidelně, zvolte tvarovaný nebo závodní model. U plavců s vlasy po ramena je dobré hned pořídit větší velikost, protože s drdolem se těsnější čepice nasazuje špatně.</p>
<h2>Zvláštní situace</h2>
<h3>Citlivá pokožka a alergie</h3>
<p>Latex může u některých lidí vyvolat podráždění, proto lidé s alergií nebo s citlivou dětskou pokožkou volí silikon nebo textil. Při nové čepici nejdřív zkuste kratší plavání a sledujte reakci pokožky. Po plavání čepici sundejte a hlavu opláchněte, protože dlouhé nošení mokré čepice po plavání ztrácí smysl a může dráždit. U velmi citlivých lidí pomůže pod čepici vložit tenkou textilní čepičku.</p>
<h3>Plavání ve studené vodě</h3>
<p>V chladných nádržích a jezerech je hlava jedinou nekrytou částí těla a chlad se tam projevuje nejvíc, a tak se hodí silnější čepice, případně neopren nebo dvojitá čepice. Silikonová čepice sama o sobě moc nehřeje, ale zmenšuje pocit chladu z větru a vodní hladiny. Výrazná barva je v tomto případě téměř povinná. Do studené vody si nikdy nechoďte sami a plavte vždy v dohledu ostatních.</p>
<h3>Plavání s brýlemi a špunty do uší</h3>
<p>Plavci s citlivýma ušima kombinují čepici se špunty. Špunty nasaďte pod čepici, aby je neuvolnil proud vody. Dbejte, aby okraj čepice nepřetlačoval špunt a netlačil na ucho. Doplňky k plavání jako špunty, kolíčky na nos či plovoucí pomůcky najdete v kategorii <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>
<h2>Uskladnění mezi plaváním</h2>
<p>Čepici po opláchnutí osušte a uložte do malého sáčku, který se dodává s některými modely, nebo do větrané kapsy plavecké tašky. Nesvírejte ji silou do kapsy s klíči ani s mokrým ručníkem, aby se neprotrhla. Sáček s mastkem a pár náhradních čepic se vyplatí mít v tašce, pokud plavete pravidelně. Čepice lze po čase vyměnit, jakmile začne praskat, ztrácí pružnost nebo se zbarví.</p>
<h2>Značky v nabídce</h2>
<p>Širokou paletu čepic nabízí '''
          f'{B(("aqua-speed", "Aqua Speed"), ("speedo", "Speedo"), ("arena", "Arena"), ("indigo-sports", "Indigo Sports"), ("merco", "Merco"), ("swimaholic", "Swimaholic"), ("spokey", "Spokey"), ("effea", "Effea"), ("zoggs", "Zoggs"), ("aqua-sphere", "Aqua Sphere"), ("mad-wave", "Mad Wave"), ("nike", "Nike"), ("kubisport", "Kubisport"), ("finis", "Finis"))}. '
          '''Speedo, Arena a Zoggs jsou tradiční plavecké značky se závodními i rekreačními řadami. Aqua Speed, Indigo Sports a Effea nabízejí široký výběr barevných a dětských čepic, Spokey a Merco jsou praktické pro rodiny. Nike a Finis zaměřují nabídku spíše na sportovní plavce. Rozdíly v kvalitě se projeví hlavně na tloušťce materiálu a na šití okrajů, ne na logu.</p>
<h2>Jak čepici nasadit a sundat</h2>
<p>Správné nasazení prodlužuje životnost čepice a chrání vlasy. Nejdřív si vlasy sepněte, pak vložte obě ruce do čepice a roztáhněte ji. Nasaďte ji od čela dozadu a přitáhněte přes týl. Uši by měly zůstat zakryté, pokud nemáte model s kapsami, a okraj má přiléhat bez záhybů. Při sundávání ji nestrhávejte, ale zvedněte okraj a stáhněte dozadu. U silikonu pomůže namočit vlasy předem, protože se čepice snáze nasazuje a netahá chloupky.</p>
<h2>Péče o čepici</h2>
<p>Po každém plavání čepici opláchněte čistou vodou, aby ji chlór neničil, a nechte ji uschnout na vzduchu. Nesušte ji na topení ani na přímém slunci, protože materiál křehne. Latex můžete občas poprášet jemným mastkem, který zabrání slepení. Silikon se nesmí skladovat v těsném svinutí. Nenechávejte čepice dlouho ve vlhké tašce, kde se může objevit zápach. Při správné péči vydrží silikonová čepice déle než latexová, zatímco textilní se postupně vytahuje.</p>
<h2>Čepice v bazénech a pro děti</h2>
<p>Řada bazénů a plaveckých škol čepici vyžaduje, aby se vlasy nedostaly do filtrace. Před návštěvou si ověřte pravidla provozovatele. U dětí je čepice navíc pomůcka při výuce, protože drží vlasy mimo oči a děti se naučí dýchat bez překážek. Pro nejmenší vybírejte měkký silikon s příjemným okrajem, který nestahuje čelo. Plavky pro rodinu najdete v kategoriích <a href="/damske-plavky/">dámské plavky</a>, <a href="/panske-plavky/">pánské plavky</a> a <a href="/detske-plavky/">dětské plavky</a>.</p>
<h2>Čepice a brýle: co k sobě patří</h2>
<p>Brýle se nasazují pod čepici nebo přes ni podle účelu. Při tréninku je praktické přetáhnout řemínek brýlí přes čepici, aby brýle při skoku nesklouzly. Na závodech se řídí zvyk plavce; někteří nosí brýle pod čepicí, protože se pak čepice při strhnutí brýlí nesvlékne. Zvolte brýle, jejichž řemínek se nekříží s okrajem čepice, aby nedocházelo k tlaku na spánky. K vodnímu sportu patří také <a href="/vodni-sporty/">vodní sporty a plavání</a> a pohodlná <a href="/obuv-do-vody/">obuv do vody</a> k bazénu a na pláž.</p>
<h2>Další výbava k bazénu</h2>
<p>K čepici se hodí lehká taška na plavání, osuška z mikrovlákna a láhev z kategorie <a href="/lahve-a-termosky/">láhve a termosky</a>. Pokud trénujete častěji, přibalte i funkční prádlo z oddílu <a href="/termopradlo/">funkční a termo prádlo</a> na cestu domů po venkovním plavání.</p>
<h2>Na co si dát pozor při nákupu</h2>
<ul><li>Alergie na latex u vás nebo u dítěte; pak zvolte silikon nebo textil.</li>
<li>Příliš malá velikost, která tlačí do čela a způsobuje bolest hlavy.</li>
<li>Dětská čepice s ostrými švy nebo s pevným okrajem, který drhne.</li>
<li>Nevhodný tvar pro dlouhé vlasy.</li>
<li>Barva čepice při plavání v otevřené vodě: tmavá čepice je v jezeře hůř vidět.</li>
<li>Nákup tenkého latexu pro každodenní trénink, který rychle praskne.</li></ul>''',
    faq=[
        ('Jaká plavecká čepice je nejlepší: silikonová, latexová, nebo textilní?', 'Záleží na účelu. Silikon je odolný a univerzální, latex lehký a těsný, ale citlivější, textil pohodlný pro rekreační plavání, ale vlasy v něm zůstanou mokré.'),
        ('Je čepice v bazénu povinná?', 'Mnoho bazénů ji vyžaduje, někde stačí vlasy sepnout. Pravidla stanovuje provozovatel, proto si je ověřte před návštěvou.'),
        ('Jak vybrat velikost čepice?', 'Podle obvodu hlavy a množství vlasů. Čepice má sedět těsně, ale netlačit do čela a do spánků. Dětské a juniorské modely jsou menší.'),
        ('Uchrání čepice vlasy před chlórem?', 'Silikonová zabrání většině kontaktu s vodou, latexová také, textilní vlasy nechrání. Po plavání vlasy ještě umyjte čistou vodou.'),
        ('Proč mi čepice trhá vlasy?', 'Obvykle je suchá, příliš těsná, nebo se nasazuje prudce. Navlhčete vlasy, použijte větší velikost a nasazujte pomalu od čela dozadu.'),
        ('Co zvolit pro dlouhé vlasy?', 'Čepici označenou jako long hair nebo volume s větším objemem. Vlasy si předtím svažte do drdolu nebo uzlu na temeni.'),
        ('Jak dlouho čepice vydrží?', 'Záleží na materiálu a péči. Silikonová vydrží nejdéle, latexová se trhá dřív a textilní se vytahuje. Pravidelně ji opláchněte a nesušte na slunci.'),
        ('Mohou čepici nosit děti?', 'Ano, pro děti jsou určeny menší modely z měkkého silikonu nebo textilu. Vyberte takovou, která netlačí do čela a snadno se sundává.'),
        ('Hodí se čepice i do otevřené vody?', 'Ano, volte zářivou barvu pro lepší viditelnost. Do studené vody se hodí silnější materiál nebo neoprenová čepice, případně dvě čepice přes sebe.'),
        ('Dá se čepice prát v pračce?', 'Ne, silikon a latex se perou jen oplachem vodou. Textilní model lze jemně vyprat ručně, ale nesušte ho v sušičce.'),
    ],
)

# ------------------------------------------------------------------ horska-kola
NEW['horska-kola'] = dict(long=True,
    title='Horská kola: hardtaily MTB pro dospělé i dámy',
    desc='Horská kola s přední vidlicí pro les, výlety i závody. Jak vybrat velikost rámu, kola, brzdy, převody a materiál a porovnat nabídky obchodů.',
    intro='''<p>Horské kolo je univerzální stroj pro lesní cesty, polňačky, kamenité stoupání i každodenní dojíždění po rozbité silnici. Díky širším plášťům, odpružené vidlici a nízkým převodům zvládne terén, kde by silniční nebo městské kolo nestačilo. Většina kol v této kategorii má odpruženou jen přední vidlici, tedy tzv. hardtail, a patří k nejlépe vyvážené volbě mezi cenou, váhou a údržbou.</p>
<p>Na Sportece najdete horská kola značek Author, Specialized, Trek, Kellys, Kross, Rockrider, Devron, Kona a dalších. Porovnáte nabídky českých obchodů a vedle toho si prohlédnete <a href="/celoodpruzena-horska-kola/">celoodpružená horská kola</a>, <a href="/horska-elektrokola/">horská elektrokola</a> a <a href="/cyklisticke-helmy/">cyklistické helmy</a>. Níže vysvětlujeme velikost rámu, kola, brzdy, pohon a údržbu.</p>''',
    guide='''<h2>Jaké druhy horských kol existují</h2>
<p>Horská kola se dělí podle toho, jak a kde na nich jezdíte. Rozdíl je především v odpružení, geometrii rámu a váze. Nejčastější jsou hardtaily, tedy kola s přední vidlicí a pevným zadním trojúhelníkem. Pro náročnější terén se hodí celoodpružená kola, pro zimu a sníh fatbiky.</p>'''
          + T(['Typ kola', 'Odpružení', 'Hlavní využití'], [
              ['Hardtail', 'přední vidlice, zadní část pevná', 'lesy, výlety, XC, dojíždění, závody'],
              ['Celoodpružené', 'odpružená vidlice i zadní tlumič', 'technický terén, trailové a enduro jízdy'],
              ['Fatbike', 'extra široké pláště, často bez odpružení', 'sníh, písek, bláto'],
              ['Dámské a juniorské', 'hardtail v menších rámech', 'menší postavy a mladší jezdci'],
              ['Horská elektrokola', 'motor v pohonu, odpružení různé', 'dlouhá stoupání bez únavy']]) +
          '''<p>Hardtail je nejvhodnější pro většinu lidí. Má nižší váhu a méně součástí, které se opotřebují, takže je levnější a snazší na údržbu. Celoodpružené kolo nabídne větší komfort na kamenitých pasážích a pomůže zvládnout sjezdy, ale jeho pořízení i servis jsou náročnější. Fatbiky tvoří zvláštní skupinu, kterou najdete v podkategorii <a href="/fatbiky/">fatbiky</a>.</p>
<h2>Velikost rámu</h2>
<p>Správná velikost rámu je nejdůležitější parametr, který rozhoduje o pohodlí. Příliš velký rám vás natáhne, příliš malý stlačí. Výrobci uvádějí velikost v palcích (například 17", 19") nebo v písmenech S, M, L, XL, a k tomu doporučují rozsah výšky postavy. Při váhání je lepší postupovat podle vnitřní délky nohy a rozměrů rámu, které najdete v tabulce u konkrétního modelu.</p>'''
          + T(['Výška postavy', 'Orientační velikost'], [
              ['do 165 cm', 'S nebo kolem 15 až 16 palců'],
              ['165 až 175 cm', 'M nebo kolem 17 až 18 palců'],
              ['175 až 185 cm', 'L nebo kolem 19 až 20 palců'],
              ['nad 185 cm', 'XL nebo 21 palců a větší']]) +
          '''<p>Hodnoty jsou jen orientační, protože se liší podle výrobce a geometrie rámu. Při koupi přes internet si změřte sebe a porovnejte hodnoty s tabulkou. Zkontrolujte také možnost nastavit výšku sedla a představce, což dokáže drobné rozdíly vyrovnat. Pro menší jezdce hledejte dámské modely s nižší horní trubkou rámu, popřípadě <a href="/damska-kola/">dámská kola</a>.</p>
<h2>Velikost kol: 26, 27,5 a 29 palců</h2>
<p>Dnes převládá 29 palců, které lépe překonávají překážky, mají lepší trakci a udrží rychlost. Velikost 27,5 palce je obratnější, nižší a vhodná pro menší jezdce, kterým u 29" rámů nemusí sedět geometrie. Starší 26" kola se ještě objevují mezi levnějšími modely a dětskými kusy; přehled pro děti najdete v kategoriích <a href="/detska-kola-24-palcu/">dětská kola 24 palců</a> a <a href="/detska-kola/">dětská kola a odrážedla</a>. Na výběru velikosti kol záleží také dostupnost plášťů a dílů, kterých je pro 29" a 27,5" nejvíc.</p>
<h2>Materiál rámu</h2>
<h3>Hliník</h3>
<p>Nejčastější materiál. Rám je lehký, odolný a cenově dostupný, dobře se svařuje a vydrží při běžném používání mnoho sezón. Při nárazu se může deformovat, ale běžné pády snese.</p>
<h3>Karbon</h3>
<p>Karbonové rámy jsou lehčí a tuhé, výrobci je odlaďují pro závodní jízdu. Při poškození ale vyžadují odborné posouzení, protože trhliny nemusí být na první pohled vidět. Hodí se tam, kde záleží na každém gramu.</p>
<h3>Ocel</h3>
<p>Ocel je pružná, snadno opravitelná a oblíbená u nadšenců. Je těžší než hliník a vyžaduje ochranu proti korozi. Mezi horskými koly dnes tvoří menšinu.</p>
<h2>Vidlice, brzdy a pohon</h2>
<h3>Odpružená vidlice</h3>
<p>Vidlice tlumí rázy při jízdě po kořenech a kamenech. Levnější kola mají pružinové provedení, kvalitnější vzduchové s nastavením podle váhy jezdce. Důležitý je zdvih: kratší pro rychlou jízdu v lese, delší pro hrubý terén. Možnosti náhradních dílů a servisu najdete v oddílu <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>.</p>
<h3>Brzdy</h3>
<p>Kotoučové brzdy jsou dnes standard u většiny kol. Na levných kolech s ocelovým rámem a odpruženou vidlicí ale počítejte s nižší kvalitou dílů i brzd; pro skutečný terén se vyplatí hliníkový rám a kvalitnější vidlice. Hydraulické poskytují lepší dávkování a vyžadují menší sílu, mechanické jsou jednodušší na seřízení. Okolí brzdových kotoučů je třeba udržovat čisté a brzdové destičky včas vyměňovat podle <a href="/cyklo-brzdy/">brzdy a brzdové destičky</a>.</p>
<h3>Převody</h3>
<p>Starší nebo levnější kola mívají kombinaci tří předních a sedmi až devíti zadních převodů. Moderní využívají jednu přední převodovku a širokou kazetu vzadu, což zjednodušuje řazení a snižuje počet součástí. Pro začátečníky je důležité, aby se nejlehčí převod dobře točil i do strmého kopce. Pohonné součástky najdete v rubrice <a href="/cyklo-pohon/">pohon</a>.</p>
<h2>Pláště, ráfky a tubeless</h2>
<p>Pláště rozhodují o trakci, valivém odporu i komfortu. Širší plášť s výraznějším vzorkem lépe drží v bahně a na kamenech, užší a hladší je rychlejší na pevném povrchu. Hodně kol dnes přijímá bezdušové pláště, které se plní tmelem a snižují riziko defektu. Podrobnosti o zapletených kolech najdete v kategorii <a href="/cyklo-kola-a-rafky/">zapletená kola, ráfky a náboje</a>. Při výměně vždy zkontrolujte rozměr ráfku a typ ventilku.</p>
<h2>Značky v nabídce</h2>
<p>Největší počet modelů mají '''
          f'{B(("author", "Author"), ("specialized", "Specialized"), ("trek", "Trek"), ("davi", "Davi"), ("rockrider", "Rockrider"), ("kellys", "Kellys"), ("devron", "Devron"), ("kross", "Kross"), ("leader-fox", "Leader Fox"), ("storm", "Storm"), ("4ever", "4ever"), ("afisport", "Afisport"), ("kona", "Kona"), ("olpran", "Olpran"))}. '
          '''České značky Author, Kellys a Devron mají široký sortiment kol od cenově dostupných po sportovní. Specialized a Trek zastupují světové výrobce s výraznou řadou hardtailů i celoodpružených modelů, Rockrider patří do sortimentu sportovního řetězce. Kona se hlásí k trailové jízdě a Kross nabízí dlouhou nabídku modelů pro dospělé i mládež. Vedle sebe tu leží kola v rozdílné výbavě, takže srovnávejte značku, ale hlavně komponenty.</p>
<h2>Výběr podle stylu jízdy</h2>
<ul><li><strong>Víkendové výlety a lesní cesty:</strong> hardtail střední třídy s hydraulickými brzdami a odpruženou vidlicí.</li>
<li><strong>Dojíždění do práce po různých površích:</strong> pevný hliníkový rám s blatníky, světly a nosičem; zvažte i <a href="/krosova-kola/">krosová kola</a> nebo <a href="/trekingova-kola/">trekingová kola</a>.</li>
<li><strong>Sportovní XC a maratony:</strong> lehčí rám, širší převodový rozsah a kvalitní vidlice.</li>
<li><strong>Technické singltreky:</strong> kolo s delším zdvihem vidlice, širšími řídítky a odolnými plášti, nebo celoodpružený model.</li>
<li><strong>Začínající a menší jezdec:</strong> menší velikost rámu a 27,5 palce, případně juniorské kolo.</li>
<li><strong>Silnice i terén:</strong> pokud jezdíte hlavně po zpevněných cestách, zvažte <a href="/gravel-kola/">gravel kola</a>.</li></ul>
<h2>Výbava a příslušenství</h2>
<p>K novému kolu patří helma z oddílu <a href="/cyklisticke-helmy/">cyklistické helmy</a> nebo odolnější <a href="/mtb-a-integralni-helmy/">MTB helma</a>, rukavice a vhodné <a href="/cyklisticka-obuv/">tretry</a>. Na pedálech rozhodnete mezi plošinovými a nášlapnými; vybírat můžete v kategorii <a href="/cyklo-pedaly/">pedály</a>. Praktické jsou <a href="/cyklo-pumpy-a-naradi/">pumpa a nářadí</a>, <a href="/cyklo-zamky/">zámek</a> a <a href="/cyklo-svetla/">světla</a>. Při pádech pomohou <a href="/cyklo-chranice/">chrániče</a>; na pití se hodí láhev v držáku z oddílu <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a>.</p>
<h2>První seřízení a údržba</h2>
<p>I nové kolo vyžaduje po prvních desítkách kilometrů kontrolu. Dotáhněte šrouby, ověřte tlak v plášti, seřiďte brzdy a nastavte vidlici podle váhy. Řetěz pravidelně čistěte a mažte vhodným mazivem, jinak se rychle opotřebuje spolu s kazetou. Po jízdě v bahně kolo opláchněte a osušte, vyhněte se silnému proudu přímo do ložisek. Pomůže vám kategorie <a href="/cyklo-udrzba/">údržba kola</a>. Jednou ročně se vyplatí návštěva servisu, kde vymění opotřebované části a promažou ložiska.</p>
<h2>Dámská, juniorská a rodinná horská kola</h2>
<p>Dámské rámy mívají nižší horní trubku, kratší představec a užší řídítka, díky čemuž pohodlněji sedí menší postavy. Pokud je žena vyšší než 175 cm, často jí vyhovuje i pánský rám. Mladším jezdcům mezi 150 a 165 cm stačí rám velikosti S s koly 27,5 palce. Pro rodiny, které jezdí společně, se vyplatí vybrat kola s podobnou výbavou, aby se výlety nezdržovaly poruchami a všichni měli podobné převody. Při růstu dětí nekupujte předimenzované rámy, protože se na nich hůř zastavuje a jezdci ztratí jistotu. Elektrická varianta v kategorii <a href="/elektrokola/">elektrokola</a> pomůže vyrovnat rozdíly v kondici.</p>
<h2>Časté chyby při výběru</h2>
<ul><li>Příliš velký rám, protože vypadá robustněji.</li>
<li>Volba kola jen podle ceny a počtu převodů, nikoli podle kvality komponentů.</li>
<li>Levná odpružená vidlice, která nahrazuje kvalitní tuhou vidlici a jen přidává váhu.</li>
<li>Přehlédnutí typu brzd a následné potíže s údržbou.</li>
<li>Nákup bez kontroly skutečné výšky postavy proti tabulce výrobce.</li>
<li>Zanedbání prvního seřízení po koupi online.</li></ul>
<h2>Nastavení kola na míru</h2>
<p>Po výběru rámu ještě upravte výšku sedla tak, aby noha při spodní poloze pedálu zůstala mírně pokrčená, a sklon sedla ponechte vodorovný. Šířku řídítek a délku představce zkoušejte podle délky paží a pohodlí zad. Vidlici nastavte podle váhy jezdce včetně batohu a po první delší jízdě ji znovu zkontrolujte. Správně nastavené kolo omezuje bolesti zad, zápěstí a kolen a zvyšuje jistotu v terénu.</p>
<h2>Kdy kupovat a jak zkoušet</h2>
<p>Největší výběr modelů je na jaře, ale právě tehdy se rychle vyprodají oblíbené velikosti. Na konci sezóny a na podzim obchody vyprodávají starší ročníky. Starší model obvykle neznamená špatné kolo, jen se mění barvy nebo drobné součástky. Při osobním odběru nechte kolo nastavit a vyzkoušejte, jak sedí. Pokud nakupujete přes internet, zkontrolujte, zda je kolo smontované, nebo zabalené, a jaká je možnost vrácení. Pro delší stoupání zvažte i <a href="/horska-elektrokola/">horské elektrokolo</a>, které se hodí pro méně trénované nebo ty, kdo se chtějí vydat dál.</p>''',
    faq=[
        ('Jaké horské kolo vybrat na začátek?', 'Hardtail s hliníkovým rámem, kotoučovými brzdami a odpruženou vidlicí je nejuniverzálnější. Klíčová je správná velikost rámu.'),
        ('Jak poznám správnou velikost rámu?', 'Podle výšky postavy, délky nohou a tabulky výrobce. Při stání nad horní trubkou má být mezi trubkou a rozkrokem volný prostor, obvykle několik centimetrů, a sedlo by mělo jít nastavit do správné výšky.'),
        ('Je lepší 27,5, nebo 29 palců?', 'Palce 29 jsou rychlejší a lépe překonávají překážky, 27,5 jsou obratnější a vhodnější pro menší jezdce. Výběr závisí na výšce a stylu jízdy.'),
        ('Je hliníkový rám dostačující?', 'Ano, pro většinu jezdců je hliník nejlepší kompromis mezi váhou, cenou a odolností. Karbon se vyplatí zejména při závodech.'),
        ('Hydraulické, nebo mechanické brzdy?', 'Hydraulické lépe dávkují a potřebují menší sílu, mechanické se snáze seřizují. Pro náročnější terén jsou vhodnější hydraulické.'),
        ('Kdy se vyplatí celoodpružené kolo?', 'Pokud často jezdíte po hrubých kamenech, kořenech a prudkých sjezdech. Pro les a výlety stačí hardtail, který je lehčí a nenáročný na údržbu.'),
        ('Co znamená 1x převody?', 'Jedna přední převodovka a široká kazeta vzadu. Je jednodušší na řazení a údržbu, ale rozsah musí odpovídat vašemu terénu.'),
        ('Jak často mám kolo servisovat?', 'Základní kontrolu zvládnete doma před každou jízdou, důkladný servis jednou ročně. Při intenzivním používání častěji.'),
        ('Mohu na horském kole jezdit po silnici?', 'Ano, ale hrubé pláště a odpružení zvyšují odpor. Pro asfalt můžete použít hladší pláště nebo zamknout vidlici, pokud ji model umožňuje.'),
        ('Hodí se horské kolo pro dámu a juniora?', 'Ano, existují dámské a juniorské rámy s nižší horní trubkou a kratší geometrií. Vybírejte podle výšky postavy, nikoli jen podle barvy.'),
    ],
)
