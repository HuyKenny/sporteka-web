"""sporteka.cz — texts of the winter subcategories, part 2 (3. 11. 2026): wax, bags, ski sets, children's skis, bindings, clothing,
skates, sleds, poles, socks, accessories. General true facts only, no prices, no superlatives, no invented statistics.
Search phrases come from Marketing Miner (cs, 11/2026). Brands come from the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['lyzarske-vosky'] = dict(short=True,
    title='Lyžařské vosky – vosk na lyže a snowboard | Sporteka',
    desc='Vosky na sjezdové, běžecké lyže a snowboardy: tuhé, sprejové i tekuté, odstraňovače a základní vosky. Porovnejte ceny v českých obchodech.',
    intro='<p><strong>Lyžařský vosk</strong> zlepšuje klouzavost a chrání skluznici před vysycháním. Pravidelné voskování prodlužuje životnost lyží i snowboardu a usnadňuje jízdu, hlavně na pomalejším sněhu.</p>'
          '<p>Na Sportece najdete vosky českých obchodů. K údržbě patří také <a href="/lyzarske-vaky-a-tasky/">vaky a tašky</a> na přepravu a <a href="/lyzarske-doplnky/">další doplňky</a>.</p>',
    guide='<h2>Jak vybrat vosk na lyže</h2>'
          '<p>Výběr závisí na tom, co voskujete: sjezdové a běžecké lyže mají jiné nároky než snowboard. Každý vosk má teplotní rozsah a způsob aplikace, který udává výrobce na obalu, proto se vždy řiďte jeho tabulkou.</p>'
          '<h3>Druhy vosků</h3>'
          '<ul><li><strong>Tuhé vosky:</strong> nanášejí se žehličkou, vsáknou se do skluznice a vydrží déle.</li>'
          '<li><strong>Sprejové a tekuté:</strong> rychlá aplikace v terénu, ideální pro doplnění během dne.</li>'
          '<li><strong>Základní vosky:</strong> připravují nově broušenou nebo suchou skluznici na hlavní vosk.</li>'
          '<li><strong>Odstraňovače a čističe:</strong> odstraňují starý vosk a nečistoty před novým nanášením.</li></ul>'
          '<h3>Sjezdové lyže a snowboard</h3>'
          '<p>Skluznice se voskuje horkým způsobem žehličkou, vosk se nechá vychladnout a odstraní se přebytek škrabkou. Poté se přebrousí kartáčem. Před sezónou jednou, během sezóny podle používání.</p>'
          '<h3>Běžecké lyže</h3>'
          '<p>Klasické běžky potřebují zároveň skluzný vosk a stoupací vosk (nebo tulení pás či šupiny). Skate lyže voskujete pouze na klouzavost. Teplota a vlhkost sněhu rozhodují o tom, jaký vosk použít.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou vosky značek {B(("swix", "Swix"), ("star-ski-wax", "Star Ski Wax"), ("holmenkol", "Holmenkol"), ("toko", "Toko"), ("vauhti", "Vauhti"), ("druchema", "Druchema"), ("vola", "Vola"))}.</p>'
          '<h3>Co k voskování potřebujete</h3>'
          '<p>Kromě vosku se hodí žehlička na lyže, plastová škrabka, kartáč a čistič. Při práci s horkým voskem větrejte a dávejte pozor na teplotu žehličky.</p>',
    faq=[('Jaký vosk na sjezdové lyže?', 'Univerzální nebo podle teploty sněhu. Vždy se řiďte údaji na obalu.'),
         ('Jak často voskovat lyže?', 'Před sezónou a pak podle používání. Suchá skluznice bývá matná a pomalejší.'),
         ('Čím se liší tuhý vosk od spreje?', 'Tuhý se nanáší žehličkou a vydrží déle. Sprej je rychlý na doplnění a nenahradí důkladné voskování.'),
         ('Je vosk stejný pro lyže a snowboard?', 'Obecně ano pro sjezdové lyže i snowboard, ale u běžek se používají zvláštní vosky podle stylu.'),
         ('Co je základní vosk?', 'Vosk pro novou nebo vysušenou skluznici, který připraví povrch na hlavní voskování.')],
)

NEW['lyzarske-vaky-a-tasky'] = dict(short=True,
    title='Vaky a tašky na lyže a lyžařské boty | Sporteka',
    desc='Vaky na lyže, tašky na lyžařské boty a obaly na snowboard. Porovnejte ceny v českých obchodech a vyberte velikost podle délky lyží.',
    intro='<p><strong>Vak na lyže</strong> a taška na boty chrání výbavu při cestě na hory a usnadňují přenášení. Vybírejte podle délky lyží, počtu párů a toho, jestli potřebujete kolečka.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K přepravě se hodí také <a href="/lyzarske-doplnky/">další lyžařské doplňky</a> a <a href="/lyzarske-vosky/">vosky</a> na péči o lyže.</p>',
    guide='<h2>Jak vybrat vak nebo tašku</h2>'
          '<p>Nejdřív změřte délku lyží a přidejte rezervu 5–10 cm. Vak musí pojmout celé lyže včetně hůlek a případných doplňků. Pokud jezdíte víc lidí, hodí se vaky na dva i více párů.</p>'
          '<h3>Typy vaků a tašek</h3>'
          '<ul><li><strong>Vak na lyže:</strong> chrání lyže před poškozením a špínou, existují jednoduché obaly i polstrované.</li>'
          '<li><strong>Taška na lyžařské boty:</strong> oddělí boty od ostatního vybavení a pojme přilbu nebo rukavice.</li>'
          '<li><strong>Vak na snowboard:</strong> přizpůsobený šířce a délce desky, často s kapsou pro vázání.</li>'
          '<li><strong>Kombinovaný vak:</strong> pojme lyže i boty a hodí se na krátké cesty.</li></ul>'
          '<h3>Přeprava letadlem a autem</h3>'
          '<p>Při letu je lepší vak s pevným polstrováním nebo kolečky. V autě stačí lehčí obal, který chrání proti poškrábání.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou vaky a tašky značek {B(("rossignol", "Rossignol"), ("dynafit", "Dynafit"), ("merco", "Merco"), ("accezzi", "Accezzi"), ("arcore", "Arcore"), ("head", "Head"), ("x2", "X2"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po cestě vak vyvětrejte a vysušte, aby uvnitř nevznikla plíseň. Lyže nikdy neskladujte dlouhodobě v obalu mokré.</p>',
    faq=[('Jak velký vak na lyže koupit?', 'O 5–10 cm delší než lyže. Změřte lyže včetně špiček.'),
         ('Hodí se vak na více párů lyží?', 'Ano, pokud jedete s rodinou. Dvojitý vak je pohodlnější než dva samostatné.'),
         ('Co patří do tašky na lyžařské boty?', 'Boty, rukavice, helma a brýle. Boty by měly být suché.'),
         ('Mohu v letadle převážet lyže ve vaku?', 'Ano, doporučuje se vak s pevným polstrováním nebo kufr. Pravidla ověřte u letecké společnosti.'),
         ('Jak se starat o vak na lyže?', 'Vyvětrejte, vysušte a uložte rozložený. Nenechávejte v něm vlhké vybavení.')],
)

NEW['lyze-komplety'] = dict(short=True,
    title='Lyže s vázáním – komplety na sjezdovku | Sporteka',
    desc='Sjezdové lyže s vázáním pro dospělé a děti. Porovnejte ceny, délky a značky v českých obchodech a vyberte lyže podle výšky a úrovně.',
    intro='<p><strong>Lyže s vázáním</strong> jsou nejjednodušší cesta k vlastnímu vybavení. Lyže a vázání od výrobce spolu ladí a vy se vyhnete hledání kompatibility. Hodí se rekreačním jezdcům i začátečníkům.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K lyžím potřebujete <a href="/lyzarske-boty/">boty</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-helmy/">helmu</a>.</p>',
    guide='<h2>Jak vybrat lyže s vázáním</h2>'
          '<p>Nejdřív zvolte délku podle výšky a schopností, potom typ lyží. U kompletů je vázání už namontované, ale vždy je třeba seřídit ho podle bot, váhy a výšky v servisu. Seřízení je z hlediska bezpečnosti důležité.</p>'
          '<h3>Délka lyží</h3>'
          + T(['Úroveň', 'Orientační délka'], [['začátečník', 'od brady po nos'], ['pokročilý', 'od nosu po čelo'], ['expert, rychlá jízda', 'po čelo nebo výše']]) +
          '<h3>Typ lyží</h3>'
          '<ul><li><strong>Carvingové:</strong> užší, snadno se otáčejí na hranách, vhodné pro upravené sjezdovky.</li>'
          '<li><strong>Allmountain:</strong> univerzální, zvládnou sjezdovku i neupravený sníh.</li>'
          '<li><strong>Freeride:</strong> širší, pro prašan a terén mimo sjezdovku.</li></ul>'
          '<h3>Pánské, dámské a dětské</h3>'
          '<p>Dámské lyže bývají lehčí a měkčí, dětské kratší a flexibilnější. Rozhodující je výška a váha, ne označení pohlaví.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Najdete lyže značek {B(("rossignol", "Rossignol"), ("elan", "Elan"), ("head", "Head"), ("atomic", "Atomic"), ("fischer", "Fischer"), ("salomon", "Salomon"), ("wedze", "Wedze"))}.</p>'
          '<h3>Servis</h3>'
          '<p>Před sezónou nechte lyže navoskovat, zkontrolovat hrany a seřídit vázání. Bez toho může být vázání nastavené jinak, než odpovídá vašim botám.</p>',
    faq=[('Jaké lyže s vázáním vybrat?', 'Podle výšky, váhy a úrovně. Pro rekreační jízdu se hodí carvingové nebo allmountain lyže.'),
         ('Jak dlouhé lyže koupit?', 'Začátečník vybírá lyže od brady po nos, pokročilý až po čelo.'),
         ('Musí se vázání nechat seřídit?', 'Ano, vždy podle botu, váhy a výšky. Seřízení dělá servis.'),
         ('Co jsou carvingové lyže?', 'Užší lyže, které se dobře otáčejí na hraně a hodí se na sjezdovky.'),
         ('Kupovat komplet, nebo samostatně?', 'Komplet je jednodušší a méně rizikový. Samostatný výběr dává větší volnost pro zkušené.')],
)

NEW['detske-lyze'] = dict(short=True,
    title='Dětské lyže – sjezdové lyže pro děti | Sporteka',
    desc='Dětské sjezdové lyže a komplety s vázáním pro nejmenší i školáky. Porovnejte ceny a délky v českých obchodech a vyberte lyže podle výšky dítěte.',
    intro='<p><strong>Dětské lyže</strong> jsou kratší, lehčí a měkčí než dospělé. Vybírejte podle výšky dítěte, ne podle toho, jestli „vyroste“. Lyže, které jsou příliš dlouhé, se špatně ovládají a dítě rychle odradí.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Pro dítě pořiďte také <a href="/lyzarske-boty/">boty</a>, <a href="/lyzarske-helmy/">helmu</a> a <a href="/lyzarske-bryle/">brýle</a>.</p>',
    guide='<h2>Jak vybrat dětské lyže</h2>'
          '<p>Základem je výška dítěte. Lyže mají sahat zhruba k bradě nebo po nos podle zkušeností a váhy dítěte. Tvar a pružnost lyží by měly dítěti usnadnit zatáčení, ne ho bránit.</p>'
          '<h3>Délka podle výšky</h3>'
          + T(['Výška dítěte', 'Orientační délka lyží'], [['do 100 cm', '70–90 cm'], ['100–120 cm', '90–110 cm'], ['120–140 cm', '110–130 cm'], ['140–160 cm', '130–150 cm']]) +
          '<h3>Vázání a boty</h3>'
          '<p>Dětské vázání se seřizuje podle váhy a velikosti boty. Boty musí sedět, protože jsou pro dítě důležitější než samotné lyže. Nekupujte boty o víc než půl čísla větší.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou lyže značek {B(("rossignol", "Rossignol"), ("fischer", "Fischer"), ("blizzard", "Blizzard"), ("atomic", "Atomic"), ("sulov", "Sulov"), ("head", "Head"), ("elan", "Elan"))}.</p>'
          '<h3>Koupit, nebo půjčit</h3>'
          '<p>Děti rychle rostou, proto se vyplatí zvážit půjčení nebo koupě použitých lyží. Nové lyže dávají smysl, pokud dítě jezdí pravidelně nebo je máte pro více sourozenců.</p>'
          '<h3>Servis</h3>'
          '<p>Před sezónou zkontrolujte vázání a hrany, u mladších dětí také upevnění bot. Pravidelná kontrola je levnější než nehoda.</p>',
    faq=[('Jak dlouhé lyže pro dítě?', 'Podle výšky: od hrudi po bradu u nejmenších, po nos u zkušenějších.'),
         ('Má smysl koupit lyže na vyrůstání?', 'Ne. Příliš dlouhé lyže se hůř ovládají. Raději zvolte správnou délku nebo půjčení.'),
         ('Jak seřídit vázání pro dítě?', 'Podle váhy a velikosti boty, nejlépe v servisu.'),
         ('Mám koupit komplet?', 'Pro rekreační lyžování ano, protože lyže s vázáním spolu ladí.'),
         ('Jak často měnit dětské lyže?', 'Obvykle po jedné až dvou sezónách, podle růstu dítěte.')],
)

NEW['lyzarske-vazani'] = dict(short=True,
    title='Lyžařské vázání – sjezdové vázání | Sporteka',
    desc='Sjezdová lyžařská vázání pro dospělé a děti. Porovnejte ceny a značky v českých obchodech a vyberte vázání podle bot, váhy a šířky lyží.',
    intro='<p><strong>Lyžařské vázání</strong> drží botu na lyži a při pádu se uvolní, aby chránilo kotník a koleno. Rozhoduje o bezpečnosti, proto nestačí vybrat jen podle ceny. Vázání se nastavuje podle váhy, výšky, schopností a bot.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K vázání patří <a href="/sjezdove-lyze/">lyže</a> a <a href="/lyzarske-boty/">boty</a>.</p>',
    guide='<h2>Jak vybrat lyžařské vázání</h2>'
          '<p>Začněte lyží. Vázání musí odpovídat šířce lyže a její montážní desce nebo systému. Potom zkontrolujte botu: alpské boty se řídí normou ISO 5355, pro boty s úpravou GripWalk platí jiná norma a ne každé vázání s nimi pracuje.</p>'
          '<h3>Hodnota DIN</h3>'
          '<p>Hodnota DIN říká, jak silným tlakem se vázání uvolní. Správnou hodnotu určuje váha, výška, věk a úroveň lyžaře. Nastavení patří do servisu, protože špatná hodnota je nebezpečná v obou směrech.</p>'
          '<h3>Brzdy a šířka</h3>'
          '<p>Brzda vázání musí odpovídat šířce lyže pod nohou. Příliš úzká brzda se nemůže otevřít, příliš široká se táhne po sněhu. Šířka brzdy se uvádí v milimetrech u každého modelu.</p>'
          '<h3>Pro koho</h3>'
          '<ul><li><strong>Rekreační:</strong> nižší hodnoty DIN, lehčí konstrukce.</li>'
          '<li><strong>Pokročilí a závodní:</strong> vyšší hodnoty a tužší vázání.</li>'
          '<li><strong>Dětská:</strong> nastavitelná na rostoucí botu a nižší sílu.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce najdete vázání značek {B(("dynafit", "Dynafit"), ("ride", "Ride"), ("nitro", "Nitro"), ("salomon", "Salomon"), ("k2", "K2"), ("stockli", "Stöckli"), ("hagan", "Hagan"))}. Část nabídky tvoří vázání jiných disciplín, proto ověřte popis výrobce.</p>',
    faq=[('Jak vybrat lyžařské vázání?', 'Podle šířky lyží, normy boty a váhy a schopností lyžaře.'),
         ('Co je hodnota DIN?', 'Je to síla, při které se vázání uvolní. Nastavuje se podle váhy a úrovně lyžaře.'),
         ('Mohu si vázání nastavit sám?', 'Doporučuje se servis. Špatné nastavení může být nebezpečné.'),
         ('Hodí se každé vázání na každou botu?', 'Ne. Záleží na normě boty (alpská, GripWalk). Ověřte kompatibilitu.'),
         ('Jak často kontrolovat vázání?', 'Před každou sezónou, u dětí častěji kvůli růstu.')],
)

NEW['lyzarske-kombinezy'] = dict(short=True,
    title='Lyžařské kombinézy – dětské i dospělé | Sporteka',
    desc='Lyžařské a zimní kombinézy pro děti a dospělé. Porovnejte ceny a velikosti v českých obchodech a vyberte oteplování i membránu podle věku.',
    intro='<p><strong>Lyžařská kombinéza</strong> je pohodlné řešení pro děti i dospělé, protože chrání celé tělo a nedovolí sněhu dostat se pod bundu. U nejmenších dětí bývá praktičtější než kalhoty s bundou.</p>'
          '<p>Na Sportece porovnáte ceny českých obchodů. Pokud preferujete dvoudílné oblečení, vyberte si <a href="/lyzarske-bundy/">bundy</a> a <a href="/lyzarske-kalhoty/">kalhoty</a>.</p>',
    guide='<h2>Jak vybrat lyžařskou kombinézu</h2>'
          '<p>Nejdůležitější je střih a materiál. Kombinéza musí mít dost prostoru pro pohyb, ale nesmí být tak volná, aby v ní dítě nebo dospělý ztratilo teplo. Dětské modely mívají zesílená kolena a manžety na nohavicích.</p>'
          '<h3>Velikost</h3>'
          '<p>Dětské kombinézy se vybírají podle výšky dítěte a bývá výhodné vybrat rezervu 2–4 cm. Nastavitelné rukávy a nohavice prodlouží životnost. U dospělých ověřte délku nohavic a rozpětí v rozkroku.</p>'
          '<h3>Zateplení a voděodolnost</h3>'
          '<ul><li><strong>Zateplení:</strong> syntetická výplň drží teplo i vlhká, peří je lehčí, ale citlivější na vodu.</li>'
          '<li><strong>Vodní sloupec:</strong> pro rekreační lyžování stačí zhruba 5 000–10 000 mm, při dlouhém dešti nebo mokrém sněhu výš.</li>'
          '<li><strong>Prodyšnost:</strong> bez ní se dítě potí, což zvyšuje riziko prochladnutí.</li></ul>'
          '<h3>Co si vzít pod kombinézu</h3>'
          '<p>Základem je <a href="/lyzarske-termopradlo/">termoprádlo</a> a fleece nebo svetr podle teploty. Bavlněné tričko u kůže nahraďte syntetikou nebo merino vlnou.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou kombinézy značek {B(("didriksons", "Didriksons"), ("helly-hansen", "Helly Hansen"), ("2117-of-sweden", "2117 of Sweden"), ("slope", "Slope"), ("whistler", "Whistler"), ("kilpi", "Kilpi"), ("scott", "Scott"))}.</p>',
    faq=[('Jakou kombinézu vybrat pro dítě?', 'Podle výšky, s nastavitelnými rukávy a nohavicemi a vodním sloupcem alespoň 5 000 mm.'),
         ('Je lepší kombinéza, nebo bunda s kalhotami?', 'Pro nejmenší je praktičtější kombinéza. Větší děti a dospělí často preferují dvoudílné oblečení.'),
         ('Jaký vodní sloupec stačí?', 'Pro běžné lyžování 5 000–10 000 mm, při mokrém sněhu raději víc.'),
         ('Co pod kombinézu?', 'Termoprádlo a fleece. Vyhněte se bavlně, která drží vlhkost.'),
         ('Kdy koupit kombinézu?', 'Výběr velikostí bývá nejširší na podzim, ceny se mění v průběhu sezóny.')],
)

NEW['lyzarske-termopradlo'] = dict(short=True,
    title='Termoprádlo – funkční prádlo na lyže | Sporteka',
    desc='Termoprádlo pánské, dámské a dětské: merino i syntetika, trička, spodky a sety. Porovnejte ceny v českých obchodech a vyberte vrstvu pod lyžařskou bundu.',
    intro='<p><strong>Termoprádlo</strong> je základní vrstva, která odvádí pot od těla a udržuje teplo. Pod lyžařské oblečení patří těsně přiléhající, ne volné, a z materiálu, který nedrží vlhkost.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Vrchní vrstvu vyberte mezi <a href="/lyzarske-bundy/">bundami</a>, <a href="/lyzarske-kalhoty/">kalhotami</a> a <a href="/lyzarske-ponozky/">ponožkami</a>.</p>',
    guide='<h2>Jak vybrat termoprádlo</h2>'
          '<p>Nejdůležitější je materiál a přiléhavost. Termoprádlo funguje, jen když leží u kůže. Příliš volné nepřenáší vlhkost, příliš těsné omezuje pohyb. Při výběru velikosti si změřte hrudník a pas podle tabulky výrobce.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Merino:</strong> přírodní vlna, ohřívá i vlhká a méně zapáchá, je ale dražší a citlivější na praní.</li>'
          '<li><strong>Syntetika:</strong> rychle schne, je odolná a levnější, hodí se při vysoké intenzitě.</li>'
          '<li><strong>Směs:</strong> kombinuje výhody obou, nejčastější volba rekreačních lyžařů.</li></ul>'
          '<h3>Typ a tloušťka</h3>'
          '<p>Tričko s dlouhým rukávem a spodky tvoří základ, v zimě doplněte ponožky a čelenku. Tloušťku volte podle teploty a intenzity: tenké pro aktivní jízdu, tlustší při mrazu a stání ve frontě.</p>'
          '<h3>Pro děti a dospělé</h3>'
          '<p>Dětské termoprádlo bývá měkčí a bez švů v místech, kde by dráždily. Kupujte spíš přiléhavé velikosti, ne větší na vyrůstání, protože volné prádlo nehřeje.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Najdete zde značky {B(("wedze", "Wedze"), ("siroko", "Siroko"), ("northfinder", "Northfinder"), ("lemon-explore", "Lemon Explore"), ("swedemount", "Swedemount"), ("ulvang", "Ulvang"), ("viking", "Viking"))}.</p>'
          '<h3>Praní</h3>'
          '<p>Perte podle štítku, bez aviváže, která zhoršuje odvod potu. Merino často vyžaduje jemný program.</p>',
    faq=[('Jaké termoprádlo vybrat na lyže?', 'Přiléhavé z merina nebo syntetiky. Bavlna pod lyžařské oblečení nepatří.'),
         ('Merino, nebo syntetika?', 'Merino méně zapáchá a hřeje i vlhké. Syntetika rychleji schne a je levnější.'),
         ('Jak poznám správnou velikost?', 'Podle tabulky výrobce. Prádlo má sedět u kůže, ale nesmí tlačit.'),
         ('Smí se termoprádlo prát s aviváží?', 'Ne, avivážní přípravky zhoršují odvod potu.'),
         ('Kolik vrstev oblékat při lyžování?', 'Zpravidla tři: termoprádlo, izolační vrstvu a lyžařskou bundu.')],
)

NEW['lyzarske-cepice-a-nakrcniky'] = dict(short=True,
    title='Lyžařské čepice a nákrčníky | Sporteka',
    desc='Čepice pod helmu, nákrčníky, čelenky a kukly na lyže. Porovnejte ceny a materiály v českých obchodech a vyberte hlavu a krk do mrazu.',
    intro='<p><strong>Čepice a nákrčníky</strong> chrání hlavu, uši a krk před větrem. Pod lyžařskou helmu patří tenká čepice nebo čelenka, na vrcholech a v mrazu pomůže nákrčník nebo kukla.</p>'
          '<p>Na Sportece najdete nabídku českých obchodů. K hlavě patří také <a href="/lyzarske-helmy/">helma</a> a <a href="/lyzarske-bryle/">brýle</a>.</p>',
    guide='<h2>Jak vybrat čepici a nákrčník</h2>'
          '<p>Vybírejte podle použití. Pod helmu potřebujete tenkou, těsnou čepici nebo čelenku, která se nemačká a nepřekáží v uších. Mimo helmu se hodí tlustší čepice z vlny nebo fleecu.</p>'
          '<h3>Typy</h3>'
          '<ul><li><strong>Čepice:</strong> pletená nebo fleecová, pod helmu raději tenká.</li>'
          '<li><strong>Nákrčník (multifunkční šátek):</strong> chrání krk a při větru i spodní část obličeje.</li>'
          '<li><strong>Čelenka:</strong> zakrývá uši a nepřehřívá hlavu, hodí se pod helmu a při aktivní jízdě.</li>'
          '<li><strong>Kukla:</strong> krytí hlavy, krku a obličeje v silném mrazu.</li></ul>'
          '<h3>Materiál</h3>'
          '<p>Merino vlna hřeje i vlhká a méně zapáchá, syntetika rychle schne a je levnější, fleece je měkký a hřejivý. Vyhněte se bavlně, která absorbuje vlhkost a rychle chladne.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou značky {B(("wedze", "Wedze"), ("lemon-explore", "Lemon Explore"), ("rossignol", "Rossignol"), ("the-north-face", "The North Face"), ("mess", "Mess"), ("siroko", "Siroko"), ("sulov", "Sulov"))}.</p>'
          '<h3>Pro děti</h3>'
          '<p>Dětské čepice by měly mít měkký lem bez švů a zakrývat uši. Pro nejmenší se hodí zavazování pod bradou, aby čepice nespadla.</p>',
    faq=[('Jaká čepice pod lyžařskou helmu?', 'Tenká, těsná a z materiálu, který neodvádí vlhkost. Čelenka nebo tenká čepice z merina.'),
         ('K čemu je nákrčník na lyže?', 'Chrání krk před větrem a dá se stáhnout přes obličej.'),
         ('Co je lepší, čepice, nebo čelenka?', 'Čelenka při aktivní jízdě, čepice při mrazu a pauzách.'),
         ('Jakou velikost vybrat?', 'Podle obvodu hlavy, těsně, ale bez tlaku.'),
         ('Proč se vyhnout bavlně?', 'Bavlna drží vlhkost a rychle prochladne.')],
)

NEW['krasobruslarske-brusle'] = dict(short=True,
    title='Krasobruslařské brusle – brusle na krasobruslení | Sporteka',
    desc='Krasobruslařské brusle pro dívky a ženy, začátečnice i pokročilé. Porovnejte ceny a velikosti v českých obchodech a vyberte brusle s kvalitním nožem.',
    intro='<p><strong>Krasobruslařské brusle</strong> mají na rozdíl od hokejových delší nůž se zoubky na špičce, pomocí kterých se dělají piruety a skoky. Výběr závisí na úrovni, četnosti bruslení a velikosti chodidla.</p>'
          '<p>Na Sportece porovnáte ceny českých obchodů. Podívejte se také na <a href="/rekreacni-brusle/">rekreační brusle</a> a <a href="/hokejove-brusle/">hokejové brusle</a>.</p>',
    guide='<h2>Jak vybrat krasobruslařské brusle</h2>'
          '<p>Začátečníci často volí brusle s měkčí botou, která poskytuje pohodlí, pokročilí s tužší botou pro skoky a piruety. Bota musí sedět pevně v patě a nesmí tlačit na prsty. Podle velikosti chodidla a obuvi se liší označení, proto se řiďte tabulkou výrobce.</p>'
          '<h3>Velikost</h3>'
          '<p>Krasobrusle se zpravidla kupují přesně na velikost chodidla, ne o číslo větší. Zkoušejte je v tenké ponožce a po zavázání zkuste dřep, abyste ověřili podporu kotníku.</p>'
          '<h3>Nůž</h3>'
          '<p>Nůž je často samostatnou součástí a vyměňuje se při opotřebení. Pro začátečníky stačí pevně namontovaný nůž, zkušenější jezdci ocení výměnné modely. Nůž je nutné pravidelně brousit, nejlépe u odborníka.</p>'
          '<h3>Pro začátečníky a pokročilé</h3>'
          '<ul><li><strong>Rekreační:</strong> měkčí bota, pohodlnější sevření a nižší cena.</li>'
          '<li><strong>Pokročilé a závodní:</strong> tužší bota, přesný nůž a vyšší odolnost.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou značky {B(("winnwell", "Winnwell"), ("attabo", "Attabo"), ("jackson", "Jackson"), ("kubisport", "Kubisport"), ("smj", "SMJ"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po bruslení nůž osušte a nasaďte ochranné kryty. Skladujte v textilním obalu, ne v plastu, kde kondenzuje vlhkost.</p>',
    faq=[('Jaké krasobrusle vybrat pro začátečnici?', 'S měkčí botou a pevným nožem, v přesné velikosti.'),
         ('Jaká velikost krasobrusle?', 'Přesně podle chodidla, ne o číslo větší. Zkoušejte s tenkou ponožkou.'),
         ('Čím se liší krasobrusle od hokejových?', 'Mají delší nůž se zoubky na špičce a vyšší botu.'),
         ('Jak často brousit nůž?', 'Podle používání, obvykle po několika desítkách hodin na ledě.'),
         ('Hodí se krasobrusle na rekreační bruslení?', 'Ano, pokud vám vyhovuje vyšší bota a styl jízdy.')],
)

NEW['rekreacni-brusle'] = dict(short=True,
    title='Brusle na led – rekreační lední brusle | Sporteka',
    desc='Lední brusle pro děti, ženy i muže na kluziště a rybník. Porovnejte ceny a velikosti v českých obchodech a vyberte pohodlné brusle pro rekreační bruslení.',
    intro='<p><strong>Rekreační lední brusle</strong> jsou určené na kluziště, rybník nebo zimní stadion. Vybírejte podle velikosti chodidla, pohodlí a typu zapínání. Pro děti se hodí brusle s nastavitelnou velikostí.</p>'
          '<p>Na Sportece najdete nabídku českých obchodů. Hokej a krasobruslení mají vlastní kategorie: <a href="/hokejove-brusle/">hokejové brusle</a> a <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a>.</p>',
    guide='<h2>Jak vybrat lední brusle</h2>'
          '<p>Brusle musí sedět v patě a pevně držet kotník. Příliš volné způsobují otlaky a nejistotu na ledě, příliš těsné tlačí a studí. Zkoušejte je v tenké ponožce a projděte se po místnosti, ve které je půda rovná.</p>'
          '<h3>Velikost a růst dítěte</h3>'
          '<p>Dětské brusle s nastavitelnou velikostí vydrží několik sezón. Velikost se přepíná po jednom čísle a zajišťuje se šrouby nebo zámkem. Před sezónou si velikost nechte ověřit.</p>'
          '<h3>Zapínání</h3>'
          '<ul><li><strong>Šněrování:</strong> nejpřesnější a nejpevnější, vyžaduje trochu času.</li>'
          '<li><strong>Přezky:</strong> rychlé a pohodlné, vhodné pro děti.</li>'
          '<li><strong>Kombinace:</strong> přezky na špičce a šněrování nahoře dávají oporu kotníku.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou lední brusle značek {B(("fila", "Fila"), ("bauer", "Bauer"), ("arcore", "Arcore"), ("tempish", "Tempish"), ("roces", "Roces"), ("k2", "K2"), ("oxelo", "Oxelo"))}.</p>'
          '<h3>Brusle na ledě a venku</h3>'
          '<p>Lední brusle nejsou určené na chůzi po tvrdém povrchu, protože se poškodí nůž. Na kluzišti a ledě chrání nůž ochranné krytky, po cestě je navlékněte.</p>'
          '<h3>Péče</h3>'
          '<p>Nůž osušte po každém bruslení a občas nechte nabrousit. Mokré brusle nevkládejte do uzavřené tašky, aby nerezaly.</p>',
    faq=[('Jaké brusle vybrat pro rekreační bruslení?', 'Pohodlné, přesně padnoucí, s oporou kotníku a vhodným zapínáním.'),
         ('Jaká velikost brusle pro dítě?', 'Podle chodidla, s nastavitelnou velikostí na růst. Zkontrolujte, že pata sedí pevně.'),
         ('Jak často brousit brusle?', 'Podle používání, obvykle po několika desítkách hodin nebo když se ztrácí hrana.'),
         ('Mohu v bruslích chodit po tvrdém?', 'Jen s krytkou na noži. Jinak nůž ztupí a poškodí se.'),
         ('Jak sušit lední brusle?', 'Nůž osušit a boty nechat vyvětrat, nezavírat do vlhké tašky.')],
)

NEW['sane-a-boby'] = dict(short=True,
    title='Sáně a boby – zimní zábava pro děti | Sporteka',
    desc='Dřevěné a plastové sáně, boby, kluzáky a kovové sáňky pro děti. Porovnejte ceny a velikosti v českých obchodech a vyberte bezpečný sáňkařský set.',
    intro='<p><strong>Sáně, boby a kluzáky</strong> patří k zimě pro celou rodinu. Dřevěné sáně vydrží roky a hodí se pro několik dětí, plastové jsou lehké a levné, boby se řídí a umí rychlejší jízdu.</p>'
          '<p>Na Sportece najdete nabídku českých obchodů. Pro zimní pobyt pořiďte také <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-helmy/">helmu</a> a <a href="/lyzarske-obleceni/">teplé oblečení</a>.</p>',
    guide='<h2>Jak vybrat sáně nebo bob</h2>'
          '<p>Základem je věk a počet dětí. Malé děti potřebují sáně s opěrkou a šňůrou, větší děti a dospělí hledají řiditelné boby nebo kluzáky pro rychlý sjezd. Zvažte také svah: kopce plné stromů vyžadují brzdu a řízení.</p>'
          '<h3>Typy</h3>'
          '<ul><li><strong>Dřevěné sáně:</strong> pevné, vhodné na sáňkařské dráhy a pro více dětí.</li>'
          '<li><strong>Plastové sáně a kluzáky:</strong> lehké, odolné proti vlhku, snadno se přenáší.</li>'
          '<li><strong>Boby:</strong> většinou s řízením a brzdou, pro vyšší rychlost a delší svahy.</li>'
          '<li><strong>Kovové sáně:</strong> pevná konstrukce s opěradlem, někdy pro dvě osoby.</li></ul>'
          '<h3>Bezpečnost</h3>'
          '<p>Na saních nejezděte přes silnice, v blízkosti vody nebo mezi stromy. Pro děti je dobré nosit helmu, rukavice a pevné boty. Šňůra by měla být dost dlouhá pro tažení, ale ne tak dlouhá, aby se dítě zamotalo.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou sáně a boby značek {B(("sulov", "Sulov"), ("plastkon", "Plastkon"), ("merco", "Merco"), ("gizmo-riders", "Gizmo Riders"))}.</p>'
          '<h3>Uložení</h3>'
          '<p>Po zimě sáně osušte a uložte v suchu. Dřevěné chraňte před vlhkem, aby nepraskaly, kovové ošetřete proti korozi.</p>',
    faq=[('Jaké sáně koupit pro malé dítě?', 'Dřevěné nebo plastové s opěrkou a šňůrou, v bezpečné velikosti.'),
         ('Jaký je rozdíl mezi bobem a saněmi?', 'Bob se řídí a má brzdu, sáně se ovládají tělem a šňůrou.'),
         ('Hodí se plastové sáně na kopec?', 'Ano, jsou lehké a rychlé, ale hůř se řídí než boby.'),
         ('Potřebuje dítě helmu na sáňkování?', 'Pro bezpečnost je vhodná, hlavně u rychlejších svahů.'),
         ('Jak sáně skladovat?', 'Osušené, v suchu a mimo mráz, dřevo chránit před vlhkem.')],
)
