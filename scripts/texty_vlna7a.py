"""sporteka.cz — texts of the winter subcategories, part 1 (3. 11. 2026): snowboard, cross-country, ski touring, wax.
General true facts only, no prices, no superlatives, no invented statistics. Search phrases come from Marketing Miner (cs, 11/2026).
Brands come from the live catalogue. Short entries (short=True): lower length thresholds in texty-export.py."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['snowboardy'] = dict(short=True,
    title='Snowboardy – prkna pro začátečníky i pokročilé | Sporteka',
    desc='Snowboardy pánské, dámské a dětské, sety s vázáním a splitboardy. Porovnejte ceny, délky a značky v českých obchodech a vyberte prkno podle váhy.',
    intro='<p><strong>Snowboard</strong> vybíráte podle váhy, výšky a stylu jízdy. Na Sportece najdete <a href="/snowboardy/">pánské, dámské i dětské snowboardy</a> od českých obchodů na jednom místě. '
          'Prkna lze řadit podle ceny nebo slevy a filtrovat podle délky, typu použití a značky.</p>'
          '<p>K desce patří <a href="/snowboardove-boty/">boty</a>, <a href="/snowboardova-vazani/">vázání</a> a <a href="/snowboardove-chranice/">chrániče</a>. Kdo začíná, často sáhne po kompletní sadě, kterou prodejci nabízejí jako set s vázáním.</p>',
    guide='<h2>Jak vybrat snowboard</h2>'
          '<p>Prkno musí sedět na vaši váhu a umět to, co od něj chcete. Příliš dlouhý snowboard se hůř otáčí, příliš krátký je nestabilní v rychlosti. Výrobci vždy uvádějí rozsah hmotnosti, ve kterém deska funguje nejlépe, proto se řiďte jím a ne jen výškou.</p>'
          '<h3>Délka podle hmotnosti</h3>'
          + T(['Hmotnost jezdce', 'Orientační délka'], [['do 50 kg', '135–145 cm'], ['50–65 kg', '145–152 cm'], ['65–80 kg', '152–158 cm'], ['80–95 kg', '158–164 cm'], ['nad 95 kg', '162 cm a více']]) +
          '<h3>Profil a tvar desky</h3>'
          '<ul><li><strong>Camber:</strong> klasický prohnutý profil, stabilní a přesný na hranách.</li>'
          '<li><strong>Rocker:</strong> prohnutí do opačného směru, deska odpouští chyby a lépe plave v prašanu.</li>'
          '<li><strong>Hybrid:</strong> kombinace obou, vhodná pro většinu rekreačních jezdců.</li>'
          '<li><strong>Twin:</strong> symetrická deska pro parky a jízdu oběma směry, <strong>directional</strong> je určený pro jízdu vpřed a freeride.</li></ul>'
          '<h3>Široká deska</h3>'
          '<p>Jezdci s velkou botou, zhruba od velikosti 45, potřebují širší desku, aby jim špičky a paty nezasahovaly do sněhu. Označuje se jako wide a v nabídce ji najdete ve filtru typu použití.</p>'
          '<h3>Děti a dospívající</h3>'
          '<p>Dětské desky jsou kratší, měkčí a lehčí. Vybírejte podle výšky dítěte a nekupujte „na vyrůstání“, protože příliš dlouhé prkno dítě znechutí. Pomůže také set, ve kterém jsou vázání už namontovaná.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Najdete zde {B(("raven", "Raven"), ("gravity", "Gravity"), ("ride", "Ride"), ("nitro", "Nitro"), ("head", "Head"), ("hatchey", "Hatchey"))} a další.</p>'
          '<h3>Splitboard</h3>'
          '<p>Splitboard je prkno, které se dá rozdělit na dvě lyže s tulením pásem na stoupání a po vrcholu se spojí zpět. Je určený pro túry mimo sjezdovky a vyžaduje znalost terénu i lavinové vybavení.</p>',
    faq=[('Jak dlouhý snowboard si vybrat?', 'Podle hmotnosti a stylu jízdy. Pro většinu jezdců sahá deska od brady po nos, přesný rozsah udává výrobce u každého modelu.'),
         ('Jaký snowboard je vhodný pro začátečníka?', 'Spíše měkčí deska s rockerem nebo hybridním profilem, která odpouští chyby a snadněji se otáčí.'),
         ('Co je snowboard set?', 'Je to prkno prodávané společně s vázáním. Kupující ušetří čas s kontrolou kompatibility.'),
         ('Jaký je rozdíl mezi twin a directional?', 'Twin je symetrický a jede se oběma směry stejně, directional má jasný předek a hodí se na rychlou jízdu a freeride.'),
         ('Jak poznám, že potřebuju širokou desku?', 'Když jsou špičky nebo paty boty zřetelně přes hranu desky, zhruba od velikosti 45 se vyplatí wide model.'),
         ('Mohu koupit dětský snowboard s větším předstihem?', 'Krátkodobě ano, ale deska by měla odpovídat výšce dítěte už teď. Příliš dlouhá deska se špatně ovládá.')],
)

NEW['snowboardove-boty'] = dict(short=True,
    title='Snowboardové boty – boty na snowboard | Sporteka',
    desc='Boty na snowboard pánské, dámské a dětské. Boa, rychlošněrování i klasické šněrování. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Snowboardové boty</strong> jsou měkčí než lyžařské a dovolují pohyb kotníku, takže správná velikost a pevnost rozhodují o pohodlí celého dne. '
          'Na Sportece porovnáte nabídku českých obchodů, filtrujte podle velikosti, způsobu zapínání a značky.</p>'
          '<p>Boty vybírejte společně s <a href="/snowboardova-vazani/">vázáním</a> a <a href="/snowboardy/">snowboardem</a>. Nejdřív zjistěte velikost podle chodidla a pak ji sladíte s vázáním.</p>',
    guide='<h2>Jak vybrat boty na snowboard</h2>'
          '<p>Bota musí držet patu na místě a nesmí tlačit na prsty. Pokud pata při předklonu stoupá, bota je velká, pokud se prsty dotýkají špičky stále, je malá. V botě se nemá pohybovat noha, ale prsty mají mít mírný prostor.</p>'
          '<h3>Způsob zapínání</h3>'
          '<ul><li><strong>Klasické šněrování:</strong> nejjednodušší a nejlevnější řešení, ale po cestě na lanovku se obtížněji dotahuje v rukavicích.</li>'
          '<li><strong>Rychlošněrování:</strong> jedním tahem dotáhnete celou botu, dobré pro denní jízdu.</li>'
          '<li><strong>Boa:</strong> kolečko se stahovacím lankem umožňuje jemně doladit utažení a dá se použít i v rukavicích.</li></ul>'
          '<h3>Tuhost</h3>'
          '<p>Měkké boty se hodí do parku a pro začátečníky, protože dovolují hravost a nezatěžují kotník. Středně tuhé jsou univerzální volbou pro všechny styly. Tužší boty vyberou freeridoví a rychlí jezdci, kteří potřebují přesnější přenos síly na hranu.</p>'
          '<h3>Velikost a vázání</h3>'
          '<p>Velikost snowboardových bot se často uvádí v mondopointech nebo v EU a US. Při výběru vázání si ověřte, že maximální velikost vázání odpovídá vaší botě, jinak se nedá správně utáhnout.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Vybírat můžete například z bot značek {B(("vans", "Vans"), ("northwave", "Northwave"), ("dreamscape", "Dreamscape"), ("burton", "Burton"), ("ride", "Ride"), ("nitro", "Nitro"), ("raven", "Raven"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po jízdě vyndejte vložky, boty osušte při pokojové teplotě mimo radiátor a nenechávejte je na topení. Vysušená vložka drží tvar a bota vydrží déle.</p>',
    faq=[('Jaké boty na snowboard vybrat?', 'Podle velikosti chodidla, stylu jízdy a pohodlí zapínání. Začátečníci volí měkčí až středně tuhé boty.'),
         ('Co je Boa v botách na snowboard?', 'Je to systém s kolečkem a lankem, který boty rovnoměrně utáhne a dá se ovládat i v rukavicích.'),
         ('Mám koupit boty o číslo větší?', 'Ne. Příliš volná bota způsobuje otlaky a špatně přenáší pohyb na hranu.'),
         ('Hodí se na snowboard obyčejné zimní boty?', 'Ne, nejsou dost pevné a vázání na ně nedrží. Použijte speciální snowboardové boty.'),
         ('Jak poznat správnou velikost bot na snowboard?', 'Stoupněte do boty, předkloňte se a zkontrolujte, že pata zůstává na místě a prsty se jen lehce dotýkají špičky.')],
)

NEW['snowboardova-vazani'] = dict(short=True,
    title='Snowboardové vázání – vázání na snowboard | Sporteka',
    desc='Vázání na snowboard klasická i rychloupínací, dětská a pro splitboardy. Porovnejte ceny a velikosti v českých obchodech a vyberte podle bot a desky.',
    intro='<p><strong>Snowboardové vázání</strong> spojuje botu s deskou a rozhoduje o ovládání, pohodlí i bezpečí. Vybírejte podle velikosti boty, tuhosti a typu zapínání a hlavně podle upevnění na desku.</p>'
          '<p>Na Sportece porovnáte vázání českých obchodů. Hledejte také <a href="/snowboardy/">desky</a> a <a href="/snowboardove-boty/">boty</a>, aby vše ladilo.</p>',
    guide='<h2>Jak vybrat vázání na snowboard</h2>'
          '<p>Nejdřív zkontrolujte velikost: vázání se dělí do tabulky S, M, L a XL podle velikosti boty. Bota musí v lůžku pevně sedět, špička ani pata nesmí přesahovat zbytečně daleko přes okraj.</p>'
          '<h3>Typy zapínání</h3>'
          '<ul><li><strong>Klasické s pásky (strap-in):</strong> nejrozšířenější řešení, dobře se dá doladit.</li>'
          '<li><strong>Rychloupínací (Flow, step-in):</strong> botu nasadíte zezadu nebo do zámku, což šetří čas na svahu.</li></ul>'
          '<h3>Tuhost</h3>'
          '<p>Měkčí vázání dovolí hravou jízdu a hodí se začátečníkům, střední je univerzální a tužší vázání vybírají freeridoví jezdci a ti, kdo jezdí rychle.</p>'
          '<h3>Montáž na desku</h3>'
          '<p>Většina desek má děrování 4×4 nebo 2×4. Značka Burton používá vlastní systém Channel, proto před koupí zkontrolujte, jestli vázání sedí na vaši desku. Úhly a vzdálenost si nastavte podle postoje a ověřte je při první jízdě.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou vázání značek {B(("nitro", "Nitro"), ("head", "Head"), ("union", "Union"), ("bataleon", "Bataleon"), ("dreamscape", "Dreamscape"), ("burton", "Burton"), ("nidecker", "Nidecker"))}.</p>'
          '<h3>Dětská vázání</h3>'
          '<p>Dětská vázání jsou měkčí a nastavitelná, aby pasovala na rostoucí nohu. Zkontrolujte, že se dají dotáhnout i v rukavicích a že má dítě dost místa v botě.</p>',
    faq=[('Jak vybrat vázání na snowboard?', 'Podle velikosti boty, tuhosti a typu zapínání a podle toho, jestli sedí na děrování vaší desky.'),
         ('Jak nastavit vázání na snowboard?', 'Nastavte šířku postoje zhruba na šířku ramen a úhly podle pohodlí. U nastavení pomůže servis nebo návod výrobce.'),
         ('Co je rychloupínací vázání na snowboard?', 'Je to systém, který nemá klasické pásky. Do vázání se vstoupí zezadu nebo se bota zacvakne do zámku.'),
         ('Sedí každé vázání na každou desku?', 'Ne. Většina desek má děrování 4×4 nebo 2×4, Burton používá systém Channel, proto vždy zkontrolujte kompatibilitu.'),
         ('Jaká velikost vázání pasuje k mé botě?', 'Podle tabulky výrobce. Velikost boty se přiřazuje k S, M, L nebo XL.')],
)

NEW['snowboardove-chranice'] = dict(short=True,
    title='Snowboardové chrániče – zápěstí, záda, kolena | Sporteka',
    desc='Chrániče na snowboard: zápěstí, záda, kolena a kostrč. Porovnejte ceny a velikosti v českých obchodech a vyberte ochranu podle stylu jízdy.',
    intro='<p><strong>Chrániče na snowboard</strong> chrání nejčastěji zraňované části těla: zápěstí, kostrč, kolena a záda. Začátečníci padají víc, takže ochranu ocení hlavně v prvních dnech.</p>'
          '<p>Na Sportece porovnáte ceny v českých obchodech. K desce přidejte <a href="/lyzarske-helmy/">helmu</a> a <a href="/lyzarske-rukavice/">rukavice</a>.</p>',
    guide='<h2>Jak vybrat chrániče na snowboard</h2>'
          '<p>Chránič musí sedět těsně a nesmí se při pohybu posouvat. Příliš volný nechrání, příliš těsný omezuje oběh a vadí v lanovce. Vybírejte podle obvodu pasu, hrudníku nebo zápěstí a řiďte se tabulkou výrobce.</p>'
          '<h3>Typy chráničů</h3>'
          '<ul><li><strong>Chrániče zápěstí:</strong> nejčastější volba, chrání proti zlomenině při pádu na ruce.</li>'
          '<li><strong>Chránič páteře:</strong> vesta nebo záda s tvrdou nebo pěnovou vrstvou.</li>'
          '<li><strong>Kalhotky s ochranou:</strong> chrání kostrč a kyčle, hodí se začátečníkům a v parku.</li>'
          '<li><strong>Chrániče kolen:</strong> pomáhají hlavně při práci s hranou a při klečení.</li></ul>'
          '<h3>Měkké a tvrdé</h3>'
          '<p>Měkké pěnové chrániče se pohodlně nosí pod oblečením. Tvrdé skořepiny nabízejí vyšší odolnost proti nárazu, ale zabírají víc místa. Pro rekreační jízdu stačí pěnová ochrana, pro park a freeride ocení někteří jezdci tvrdší.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Najdete zde chrániče značek {B(("dreamscape", "Dreamscape"), ("scott", "Scott"), ("qunature", "Qunature"), ("salomon", "Salomon"), ("poc", "POC"), ("cairn", "Cairn"), ("atomic", "Atomic"))}.</p>'
          '<h3>Kdy nosit</h3>'
          '<p>Doporučuje se při prvním lyžování nebo snowboardingu, v parku a při jízdě v neznámém terénu. Chrániče neřeší pád z velké výšky, ale snižují následky běžných pádů.</p>',
    faq=[('Jaké chrániče na snowboard vybrat?', 'Pro začátečníka chrániče zápěstí a kalhotky s ochranou kostrče. Pro park a freeride přidejte chránič páteře.'),
         ('Jak poznám správnou velikost chrániče?', 'Změřte obvod pasu, hrudníku nebo zápěstí podle tabulky výrobce. Chránič musí sedět těsně a nehýbat se.'),
         ('Hodí se chrániče na zápěstí do lyžařských rukavic?', 'Ano, nosí se pod rukavicemi nebo jsou součástí rukavic. Zkontrolujte, že jdou rukavice dobře zapnout.'),
         ('Chrání chránič zad při pádu?', 'Snižuje následky běžných pádů a nárazů. Nenahradí opatrnou jízdu ani helmu.'),
         ('Mám nosit chrániče, i když umím jezdit?', 'V parku a při rychlé jízdě se vyplatí. Na běžném svahu je to osobní rozhodnutí.')],
)

NEW['bezecke-boty'] = dict(short=True,
    title='Běžecké boty na lyže – klasika, skate, kombi | Sporteka',
    desc='Boty na běžky pro klasiku, bruslení i kombi. NNN, SNS a Prolink, pánské, dámské a dětské. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Boty na běžky</strong> se liší podle stylu: klasika, bruslení (skate) nebo kombi. Každý typ má jiné podrážky a výšku nártu, proto si vyberte podle toho, jak jezdíte, a hlavně podle vázání na lyžích.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. K botám patří <a href="/bezecke-lyze/">běžecké lyže</a>, <a href="/bezecke-vazani/">vázání</a> a hole. Nejdřív zjistěte systém, který mají vaše vázání.</p>',
    guide='<h2>Jak vybrat boty na běžky</h2>'
          '<p>Bota musí odpovídat systému vázání na lyžích: NNN, SNS nebo Prolink. Informaci najdete u vázání nebo na lyžích, v případě pochybností se zeptejte prodejce. Špatný systém se do vázání nezacvakne.</p>'
          '<h3>Styl jízdy</h3>'
          '<ul><li><strong>Klasika:</strong> nižší, pružná bota, která se dobře ohýbá v nártu.</li>'
          '<li><strong>Skate (bruslení):</strong> vyšší a tužší bota s oporou kotníku.</li>'
          '<li><strong>Kombi:</strong> kompromis pro oba styly, vhodné pro rekreační jezdce a začátečníky.</li></ul>'
          '<h3>Zateplení a velikost</h3>'
          '<p>Při jízdě se nohy zahřívají, ale při pomalé jízdě nebo delší pauze ocení teplejší bota. Vyberte velikost s malou rezervou pro tenkou běžeckou ponožku a při zkoušce stoupněte, pata nesmí zvedat.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou boty značek {B(("alpina", "Alpina"), ("rossignol", "Rossignol"), ("madshus", "Madshus"), ("fischer", "Fischer"), ("salomon", "Salomon"), ("inovik", "Inovik"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po jízdě boty osušte při pokojové teplotě, vyndejte vložky a očistěte mechanismus u špičky. Zamrzlý sníh ve vázání nebo v botě by mohl zabránit zacvaknutí.</p>',
    faq=[('Jaké boty na běžky vybrat?', 'Podle stylu jízdy a systému vázání. Rekreační jezdci často volí kombi.'),
         ('Jaký je rozdíl mezi NNN a SNS?', 'Jsou to dva různé systémy vázání. Bota musí odpovídat systému na lyžích.'),
         ('Co je Prolink?', 'Je to další systém vázání s vlastním označením. Boty i vázání musí mít stejné označení, proto kompatibilitu ověřte u prodejce nebo výrobce.'),
         ('Jsou běžecké boty na klasiku a skate stejné?', 'Ne. Skate bota je vyšší a tužší, klasická nižší a pružnější. Kombi boty se snaží spojit obojí.'),
         ('Jakou velikost bot na běžky zvolit?', 'Stejnou nebo o půl čísla větší, s malou rezervou pro tenkou ponožku.')],
)

NEW['bezecke-vazani'] = dict(short=True,
    title='Vázání na běžky – NNN, SNS, Prolink | Sporteka',
    desc='Vázání na běžecké lyže systémů NNN, SNS a Prolink. Porovnejte ceny v českých obchodech a vyberte vázání podle bot a stylu jízdy.',
    intro='<p><strong>Vázání na běžky</strong> musí odpovídat systému bot. Nejčastěji se setkáte s NNN, SNS a Prolink, a když si vyberete špatně, bota se nezacvakne. Vyberte si podle stylu jízdy a bot a pak podle lyží.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Hledejte také <a href="/bezecke-boty/">běžecké boty</a> a <a href="/bezecke-lyze/">lyže</a>.</p>',
    guide='<h2>Jak vybrat vázání na běžky</h2>'
          '<p>Nejdřív zkontrolujte boty. Na patce nebo špičce je označení NNN, SNS nebo Prolink. Vázání stejného systému se dá nasadit do každé lyže určené pro daný systém. Pokud boty znáte, hledáte jen vázání.</p>'
          '<h3>Systémy vázání</h3>'
          '<ul><li><strong>NNN:</strong> systém výrobce Rottefella, rozšířený na rekreačních lyžích.</li>'
          '<li><strong>SNS:</strong> systém Salomon.</li>'
          '<li><strong>Prolink:</strong> systém s vlastním označením, u kterého vždy ověřte kompatibilitu bot a vázání u výrobce.</li>'
          '<li><strong>NIS:</strong> montážní deska na lyžích, do které se vázání NNN přišroubuje nebo posune.</li></ul>'
          '<h3>Klasika, skate, kombi</h3>'
          '<p>Vázání pro klasiku je pružnější a dovolí zdvihnout patu, pro skate bývá tužší a robustnější. Při výběru kombi si ověřte, že vázání vyhovuje oběma stylům.</p>'
          '<h3>Montáž</h3>'
          '<p>Vázání se montuje ve specializovaném servisu nebo podle návodu. Pokud lyže montáž neumožňují (nemají NIS desku), je nutné vyvrtat otvory, což je lepší nechat servisu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce najdete vázání značek {B(("rottefella", "Rottefella"), ("salomon", "Salomon"), ("fischer", "Fischer"), ("kastle", "Kästle"))} a další.</p>',
    faq=[('Jaké vázání na běžky vybrat?', 'Takové, které odpovídá systému vašich bot: NNN, SNS nebo Prolink.'),
         ('Jaký je rozdíl mezi NNN a SNS?', 'Jde o dva různé systémy vázání. Každé vázání funguje jen s botami stejného systému.'),
         ('Co je NIS deska?', 'Je to montážní lišta na lyži, do které se vázání NNN snadno připevní a posune.'),
         ('Mohu si vázání namontovat sám?', 'Při desce NIS ano, jinak je lepší nechat to servisu, aby otvory seděly přesně.'),
         ('Mění se vázání podle klasiky a skate?', 'Ano. Vázání pro klasiku je pružnější, pro skate pevnější. Kombi je kompromis.')],
)

NEW['skialpove-lyze'] = dict(short=True,
    title='Skialpové lyže – lyže na skialp | Sporteka',
    desc='Skialpové lyže pro túry, freeride i závody. Porovnejte ceny, délky a značky v českých obchodech a vyberte lehkost nebo stabilitu podle terénu.',
    intro='<p><strong>Skialpové lyže</strong> musí být lehké na výstup a stabilní při sjezdu. Čím víc se vám hodí stoupání, tím lehčí lyže, čím víc sjezd, tím širší a stabilnější. Délka a šířka záleží na terénu i na vaší váze.</p>'
          '<p>Na Sportece najdete lyže v českých obchodech. K nim patří <a href="/skialpove-vazani/">vázání</a>, <a href="/skialpove-boty/">boty</a> a <a href="/skialpove-pasy/">pásy</a>.</p>',
    guide='<h2>Jak vybrat skialpové lyže</h2>'
          '<p>U skialpu platí kompromis mezi hmotností a stabilitou. Lehké závodní lyže jsou úzké, krátké a nepříjemné na tvrdém sněhu v rychlosti. Širší freeridové lyže poskytují oporu v prašanu, ale jsou těžší a hůř se vyhazují na vrchol.</p>'
          '<h3>Druhy skialpových lyží</h3>'
          '<ul><li><strong>Závodní (race):</strong> velmi lehké a úzké, vhodné pro rychlé výstupy.</li>'
          '<li><strong>Univerzální túrové:</strong> vyvážené, nejčastější volba pro víkendové túry.</li>'
          '<li><strong>Freeride:</strong> širší a těžší, vhodné pro sjezdy v hlubokém sněhu.</li></ul>'
          '<h3>Délka</h3>'
          '<p>Skialpové lyže bývají o něco kratší než sjezdové, často sahají od brady po čelo. Přesnou délku určete podle váhy, schopností a terénu a zohledněte doporučení výrobce.</p>'
          '<h3>Pásy a vázání</h3>'
          '<p>K lyžím se kupují stoupací pásy, které se lepí na skluznici. Vybírejte pásy pro konkrétní model lyží nebo si je nechte zastřihnout. Vázání vyberte podle typu: úsporné pinové (tech) pro lehkost, rámové pro větší stabilitu při sjezdu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou lyže značek {B(("dynafit", "Dynafit"), ("kastle", "Kästle"), ("simond", "Simond"), ("hagan", "Hagan"), ("wedze", "Wedze"), ("k2", "K2"))}.</p>'
          '<h3>Bezpečnost</h3>'
          '<p>K túrám mimo sjezdovky patří lavinové vybavení (vyhledávač, sonda, lopata), znalost terénu a lavinového nebezpečí. Samotné lyže bezpečnost neřeší.</p>',
    faq=[('Jaké skialpové lyže vybrat?', 'Podle toho, jestli převažuje stoupání nebo sjezd. Pro rekreační túry se hodí univerzální středně široké lyže.'),
         ('Jak dlouhé skialpové lyže?', 'Obvykle od brady po čelo. Přesnou délku určuje váha, terén a doporučení výrobce.'),
         ('Co jsou pásy na skialpové lyže?', 'Jsou to nalepovací pásy s vlasem, které brání couvání při stoupání.'),
         ('Čím se liší skialpové lyže od sjezdových?', 'Jsou lehčí a mají vázání, které se dá uvolnit pro stoupání.'),
         ('Hodí se skialpové lyže na sjezdovku?', 'Dají se použít, ale sjezdové lyže jsou stabilnější a lépe drží hranu při vyšší rychlosti.')],
)

NEW['skialpove-boty'] = dict(short=True,
    title='Skialpové boty – boty na skialp | Sporteka',
    desc='Skialpové boty pro túry, freeride a závody. Porovnejte ceny a velikosti v českých obchodech a vyberte botu podle tuhosti a hmotnosti.',
    intro='<p><strong>Skialpové boty</strong> mají za úkol být lehké a pohodlné při stoupání a pevné při sjezdu. Většinou mají režim chůze, ve kterém se kotník uvolní. Výběr závisí na tom, jestli vás víc baví výstup, nebo sjezd.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K botám přidejte <a href="/skialpove-lyze/">lyže</a> a <a href="/skialpove-vazani/">vázání</a>.</p>',
    guide='<h2>Jak vybrat skialpové boty</h2>'
          '<p>Nejdůležitější je velikost a tvar nohy. Skialpová bota má sedět pevně v patě a nesmí tlačit v nártu, protože při dlouhém stoupání se otlaky tvoří rychle. Zkoušejte ji v lyžařských ponožkách a nechte si čas.</p>'
          '<h3>Hmotnost a tuhost</h3>'
          '<ul><li><strong>Race a lehké boty:</strong> minimální váha, určené pro rychlé výstupy a závody.</li>'
          '<li><strong>Univerzální túrové:</strong> kompromis mezi tuhostí a hmotností pro většinu jezdců.</li>'
          '<li><strong>Freeride:</strong> tužší a těžší, vhodné pro agresivní sjezd.</li></ul>'
          '<h3>Režim chůze a zapínání</h3>'
          '<p>Skialpová bota má přepínač mezi režimem sjezdu a chůze. Při chůzi se kotník uvolní, aby se noha mohla přirozeně pohybovat. Zapínání bývá přezkové nebo s kolečkem Boa.</p>'
          '<h3>Kompatibilita s vázáním</h3>'
          '<p>Ověřte, že bota má vložky pro pinové (tech) vázání. Většina skialpových bot je kompatibilní, ale závodní a freeridové modely se mohou lišit.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou boty značek {B(("dynafit", "Dynafit"), ("atomic", "Atomic"), ("fischer", "Fischer"), ("hagan", "Hagan"), ("dalbello", "Dalbello"), ("roxa", "Roxa"))}.</p>',
    faq=[('Jaké skialpové boty vybrat?', 'Podle stylu: lehké pro výstupy, univerzální pro víkendové túry, tužší pro freeride.'),
         ('Co je režim chůze?', 'Je to nastavení boty, které uvolní kotník, abyste mohli při stoupání přirozeně našlapovat.'),
         ('Funguje skialpová bota i na sjezdovce?', 'Dá se použít, ale tuhost a opora jsou nižší než u sjezdových bot.'),
         ('Jaké vázání pasuje na skialpové boty?', 'Většina modelů má vložky pro pinová (tech) vázání. Ověřte u konkrétního modelu.'),
         ('Jakou velikost zvolit?', 'Tu, která sedí v patě a netlačí v nártu. Zkoušejte ve lyžařských ponožkách.')],
)

NEW['skialpove-vazani'] = dict(short=True,
    title='Skialpové vázání – pinové a rámové | Sporteka',
    desc='Vázání na skialp: lehké pinové (tech) i rámové. Porovnejte ceny v českých obchodech a vyberte podle bot, hmotnosti a stylu jízdy.',
    intro='<p><strong>Skialpové vázání</strong> se při stoupání uvolní v patě a při sjezdu se zajistí jako klasické vázání. Vybírá se podle hmotnosti, stylu a hlavně podle bot, které k nim musí patřit.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K vázání patří <a href="/skialpove-lyze/">lyže</a> a <a href="/skialpove-boty/">boty</a>.</p>',
    guide='<h2>Jak vybrat skialpové vázání</h2>'
          '<p>Vázání musí odpovídat botě a lyžím. Nejprve si ověřte, že vaše boty mají vložky pro pinové vázání, a pak vyberte typ podle toho, jak budete jezdit.</p>'
          '<h3>Typy vázání</h3>'
          '<ul><li><strong>Pinové (tech):</strong> velmi lehké, bota se fixuje špičkou pomocí kolíků. Oblíbené pro výstupy a závody.</li>'
          '<li><strong>Rámové a hybridní:</strong> těžší a pevnější, bližší klasickému sjezdovému vázání, vhodné pro agresivní sjezd.</li></ul>'
          '<h3>Hmotnost a odpojování</h3>'
          '<p>Čím lehčí vázání, tím snazší stoupání, ale někdy se sníží komfort nebo možnost pojištění při pádu. Zkontrolujte, zda vázání umožňuje nastavit uvolnění podle vaší váhy, a nechte je seřídit v servisu.</p>'
          '<h3>Brzdy a pojistky</h3>'
          '<p>Při pohybu mimo sjezdovku se využívají brzdy nebo pojistné řemínky, aby se lyže neodkutálela. Podle terénu a pravidel vyberte řešení, které odpovídá vašemu stylu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou vázání značek {B(("dynafit", "Dynafit"), ("wedze", "Wedze"), ("marker", "Marker"), ("salomon", "Salomon"))} a další.</p>',
    faq=[('Jaké skialpové vázání vybrat?', 'Podle bot, stylu a hmotnosti. Pinové je lehčí, rámové pevnější.'),
         ('Co je tech vázání?', 'Je to pinové vázání, kde se bota fixuje špičkou na kolíky. Je velmi lehké.'),
         ('Hodí se skialpové vázání na sjezdovku?', 'Funguje, ale pro náročný sjezd je vhodnější pevnější rámové nebo klasické vázání.'),
         ('Může si vázání namontovat každý?', 'Montáž se doporučuje nechat servisu, protože na ní závisí bezpečnost.'),
         ('Jak nastavit uvolnění vázání?', 'Podle váhy, schopností a doporučení výrobce. Nejlépe v servisu.')],
)

NEW['skialpove-pasy'] = dict(short=True,
    title='Stoupací pásy na skialp | Sporteka',
    desc='Stoupací pásy na skialpové lyže, mohair i syntetika. Porovnejte ceny v českých obchodech a vyberte pásy podle lyží a šířky.',
    intro='<p><strong>Stoupací pásy</strong> se lepí na skluznici skialpových lyží a umožňují stoupat do svahu bez couvání. Vybírají se podle šířky a délky lyží a podle materiálu: mohair, syntetika nebo směs.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. Pásy patří k <a href="/skialpove-lyze/">skialpovým lyžím</a> a <a href="/skialpove-boty/">botám</a>.</p>',
    guide='<h2>Jak vybrat stoupací pásy</h2>'
          '<p>Pásy musí odpovídat vašim lyžím. Dvě možnosti jsou hotové pásy na konkrétní model nebo pásy z role, které si zastřihnete sami. Šířka pásu by měla pokrývat většinu skluznice a nechat volné hrany, aby lyže zachytila sníh.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Mohair:</strong> přírodní vlákno, výborně klouže a snižuje námahu, ale je dražší a méně odolné.</li>'
          '<li><strong>Syntetika:</strong> odolná, dobře zabírá a hodí se do náročných podmínek.</li>'
          '<li><strong>Směs:</strong> kombinuje klouzavost a trvanlivost.</li></ul>'
          '<h3>Péče o pásy</h3>'
          '<p>Po túře pásy ihned stáhněte z lyží, nechte je vysušit a slepte k ochranné fólii. Lepicí vrstva chrání před prachem a nečistotou, proto ji nelepte na špinavé povrchy.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou pásy značek {B(("pomoca", "Pomoca"), ("colltex", "Colltex"), ("nitro", "Nitro"), ("g3", "G3"), ("tyrolia", "Tyrolia"))}.</p>'
          '<h3>Kdy pásy vyměnit</h3>'
          '<p>Pokud lepicí vrstva ztrácí přilnavost nebo vlákno vypadá potrhaně, je čas na výměnu. Při opakovaném lepení pomáhá renovace lepidla ze servisu.</p>',
    faq=[('Jak vybrat pásy na skialp?', 'Podle šířky a délky lyží a podle materiálu: mohair, syntetika nebo směs.'),
         ('Co je lepší, mohair nebo syntetika?', 'Mohair lépe klouže, syntetika vydrží víc. Směs je kompromis.'),
         ('Jak se starat o pásy?', 'Po túře je stáhněte, vysušte a slepte k ochranné fólii.'),
         ('Kdy je čas pásy vyměnit?', 'Když ztrácí přilnavost nebo se potrhá vlákno.'),
         ('Mohu pásy zastřihnout sám?', 'Ano, pásy z role se přizpůsobí lyžím. Postupujte podle návodu výrobce.')],
)
