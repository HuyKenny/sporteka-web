"""sporteka.cz — wave 29a (16. 11. 2026): long texts for boby, sanky, whey-proteiny, veganske-proteiny.
General true facts only, no prices, no product counts. Child safety for bobs and sleds without citing standard numbers.
Protein health claims only in the wording of authorised EU claims (Reg. 432/2012), no dosing advice beyond the label;
WPC/WPI protein shares given only as the usual definition ranges. Brands linked only if present in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ boby
NEW['boby'] = dict(long=True,
    title='Boby s volantem i bez řízení: dětské boby na sníh',
    desc='Boby na sníh s volantem a brzdami, boby bez řízení i dvoumístné. Jak vybrat velikost, na co dát pozor u brzd a nabídky českých e-shopů na jednom místě.',
    intro='<p><strong>Boby</strong> jsou plastové saně, na kterých se sedí podobně jako v malém autě. Vpředu bývá volant, po stranách páky brzd a pod sedákem lyžiny nebo tvarované dno. Dětem se líbí hlavně to, že se dají řídit. Rodiče ocení, že bob je lehký, nerezaví a po zimě stačí ho opláchnout a uklidit do sklepa. Vedle řiditelných bobů s volantem se prodávají i jednodušší boby bez řízení, které připomínají větší kluzák s opěrkou a madly po stranách.</p>'
          '<p>Sporteka vám ukáže, které české e-shopy vybraný bob nabízejí, a objednávku pak dokončíte přímo u obchodu, který vám vyhovuje. V nabídce se objevují boby značek Plastkon, Sulov, Prosperplast, AlpenGaudi nebo Hamax. Boby spadají do kategorie <a href="/sane-a-boby/">sáně a boby</a>. Pokud dítě chce rychlou jízdu bez řízení, podívejte se na <a href="/kluzaky-na-snih/">kluzáky na sníh</a>, klasiku s ocelovými sanicemi najdete mezi <a href="/sanky/">sáňkami</a>.</p>',
    guide='<h2>Bob s volantem, nebo bez řízení</h2>'
          '<p>Řiditelný bob má vpředu otočnou lyžinu, kterou natáčí volant. Na udusaném sněhu tak dítě opravdu zatočí a objede překážku, v hlubokém prašanu nebo na ledu je ale účinek řízení menší. Bob bez řízení se ovládá jako sáně: přenesením váhy a patami ve sněhu. Má méně dílů, které se mohou ulomit, bývá lehčí a malé dítě ho snáz vytáhne do kopce samo. Pro první zimu na sněhu proto často stačí jednodušší model, bob s volantem dává smysl, když už dítě jezdí samo a chce mít jízdu pod kontrolou.</p>'
          + T(['Typ bobu', 'Jak se ovládá', 'Pro koho se hodí'], [
              ['Bob s volantem a přední lyžinou', 'volant natáčí přední lyžinu, po stranách dvě brzdy', 'děti, které už zvládnou zatáčet'],
              ['Bob na lyžích (snow racer)', 'řízení přední lyží, dvě zadní lyže drží směr', 'větší děti a upravené svahy'],
              ['Bob bez řízení s opěrkou', 'přenesením váhy, brzdí se nohama', 'menší děti pod dohledem'],
              ['Dvoumístný bob', 'řídí ten, kdo sedí vpředu', 'rodič s dítětem nebo sourozenci'],
              ['Bob s tažnou šňůrou', 'po rovině ho táhne dospělý', 'cesta na kopec i zimní procházka']]) +
          '<h2>Brzdy: na co se dívat</h2>'
          '<p>Většina bobů má po stranách dvě páky. Po zatažení se do sněhu zaryjí ozubené hřebeny z plastu nebo kovu a bob zpomalí. Brzdit se dá oběma pákami najednou, nebo jen jednou, a tím se bob zároveň stočí na tu stranu. Před koupí si ověřte, jestli dítě na páky pohodlně dosáhne a má dost síly je stáhnout i v zimních rukavicích. U malých dětí se to nejlépe zkouší doma na koberci, kde je hned vidět, zda jde pohyb přirozeně.</p>'
          '<p>Brzdy fungují dobře na sněhu, který se dá rozrýt. Na zledovatělé dráze nebo na tvrdém firnu jejich účinek výrazně klesá a bob jede rychleji, než by dítě čekalo. V takových podmínkách pomůže jen volba mírnějšího svahu s dlouhým rovným doběhem. Nacvičte s dítětem zastavení dřív, než pojede z vyššího kopce: nejprve brzdy, potom paty do sněhu, a když nic nepomáhá, raději se převrátit na bok do měkkého sněhu.</p>'
          '<h2>Materiál a odolnost v mrazu</h2>'
          '<p>Boby se lisují z plastu, nejčastěji z polyethylenu. Ten zůstává pružný i v mrazu, zatímco některé levnější plasty za silného mrazu křehnou a při nárazu na kámen nebo zmrzlý hrbol praskají. Prohlédněte si hlavně spoj volantu s přední lyžinou a uchycení brzdových pák, protože tam se při nárazu soustředí největší síla. Šrouby a čepy by neměly vyčnívat do prostoru, kde má dítě nohy. Hrany sedadla i madel mají být zaoblené, aby se o ně dítě při pádu neuhodilo.</p>'
          '<p>Barva je víc než otázka vkusu. Výrazně červený, oranžový nebo žlutý bob je na bílém svahu dobře vidět z dálky, a to ocení jak rodič, který dítě hlídá, tak ostatní jezdci.</p>'
          '<h2>Velikost, nosnost a doporučený věk</h2>'
          '<p>Výrobce u každého bobu uvádí nosnost a věk, pro který je určen. Berte je vážně, protože dětský bob se při přetížení prohne a řízení začne drhnout. Dítě by mělo sedět s mírně pokrčenýma nohama, chodidla opřená o stupačky nebo přední část, a na volant dosáhnout bez natahování. Když sedí s koleny u brady, je bob už malý. Dospělý se do běžného dětského bobu nevejde rozumně a zatíží ho nad mez, se kterou konstrukce počítá. Pokud chcete jezdit společně, vyberte dvoumístný model s nosností pro dvě osoby.</p>'
          '<h2>Bezpečnost na kopci</h2>'
          '<ul><li><strong>Helma:</strong> pro děti je vhodná, ideálně <a href="/lyzarske-helmy/">lyžařská helma</a>, která kryje i zátylek a dá se nosit s čepicí pod ní jen tenkou.</li>'
          '<li><strong>Daleko od silnic:</strong> svah nesmí končit u cesty, parkoviště, potoka ani rybníka. Doběh má být rovný a volný.</li>'
          '<li><strong>Bez stromů a sloupů v dráze:</strong> i dobře řiditelný bob se na zledovatělém místě může utrhnout ze stopy.</li>'
          '<li><strong>Dohled dospělého:</strong> malé děti by neměly jezdit bez dozoru, i když jde o malý kopec za domem.</li>'
          '<li><strong>Nohama napřed a vsedě:</strong> jízda vleže hlavou dolů je mnohem nebezpečnější.</li>'
          '<li><strong>Nikdy za autem, čtyřkolkou ani skútrem:</strong> bob není stavěný na tahání motorovým vozidlem.</li>'
          '<li><strong>Po jízdě z dráhy:</strong> dole hned uhnout stranou a do kopce chodit po kraji, ne středem.</li></ul>'
          '<p>Za šera a v noci je dítě na sněhu špatně vidět. Pokud se sáňkuje odpoledne do tmy, pomůže reflexní prvek na bundě nebo malá blikačka na bobu. Rukavice nepromokavé a dost dlouhé, aby za ně nepadal sníh, dítěti zase prodlouží zábavu, protože se nevrací domů po první půlhodině se zmrzlými prsty.</p>'
          '<h2>Bob, sáně, nebo kluzák?</h2>'
          '<p>Každý typ se hodí na jiný sníh. Dřevěné nebo kovové saně se sanicemi jedou nejlépe po uježděné cestě a vydrží desítky zim. Kluzák bez lyžin klouže i v hlubším sněhu, je nejlehčí a nejjednodušší, ale řídí se jen tělem. Bob stojí mezi nimi: na upraveném kopci jede svižně, dá se řídit a brzdit, v čerstvém prašanu se ale může zabořit lyžinou. Rodiny s více dětmi často kombinují, protože každé dítě si oblíbí něco jiného. Celou zimní nabídku pro děti i dospělé najdete v sekci <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<h2>Snow racer: bob na lyžích</h2>'
          '<p>Zvláštní skupinou jsou boby postavené na třech lyžích, kterým se často říká snow racer nebo skibob. Jezdec sedí na podlouhlém sedadle nad dvěma zadními lyžemi a volantem natáčí přední lyži. Na upravené sjezdovce nebo na pevném uježděném sněhu jsou rychlejší a stabilnější než klasický bob s plastovým dnem a lépe drží stopu v zatáčce. Lyže ale potřebují pevný podklad. V čerstvém hlubokém sněhu se zaboří a jízda se zastaví. Tyto modely jsou proto vhodné spíš pro starší děti, které už mají s řízením zkušenosti, a pro kopce, kde je sníh ušlapaný.</p>'
          '<p>Na některých sjezdovkách a v lyžařských areálech jsou boby a saně na sjezdových tratích zakázané nebo povolené jen na vyhrazeném svahu. Než bob vezmete na hory, podívejte se do provozního řádu střediska.</p>'
          '<h2>Dvoumístný bob a jízda s rodičem</h2>'
          '<p>Dvoumístné boby mají delší sedadlo, na kterém sedí řidič vpředu a spolujezdec za ním. Pro rodiče s malým dítětem je praktické, když dítě sedí vpředu mezi nohama dospělého, který ho drží, a řídí nebo brzdí dospělý. Ověřte si ale, jak je bob postavený: u části modelů dosáhne na volant jen přední jezdec. Dvoumístný bob je těžší a do kopce se táhne hůř, zato vydrží i sourozencům, kteří se o jedno místo hádat nemusí. Pro rodiny, kde se na kopec vyráží společně, je to často praktičtější než dva menší boby.</p>'
          '<h2>Kdy bob koupit</h2>'
          '<p>Zájem o boby prudce stoupá s prvním sněhem, nejvíc v prosinci a lednu. Oblíbené modely pak během několika dní zmizí ze skladů a obchody je doplňují až s odstupem. Kdo vybírá s předstihem, má větší výběr barev i variant. Na Sportece u každého bobu vidíte, kde je právě skladem, a při objednávce v sezóně se vyplatí zkontrolovat i termín doručení, aby bob nedorazil až po oblevě.</p>'
          '<h2>Údržba a skladování</h2>'
          '<ul><li>Po jízdě bob oklepejte od sněhu a nechte oschnout, hlavně v okolí brzd a osy řízení.</li>'
          '<li>Před sezónou zkontrolujte, zda volant nemá vůli a obě brzdy se vracejí do původní polohy.</li>'
          '<li>Přes léto bob uložte do stínu. Dlouhé slunce plast vysušuje a postupně ho dělá křehčím.</li>'
          '<li>Neukládejte na něj těžké věci, sedák i lyžiny se mohou trvale prohnout.</li>'
          '<li>Prasklý díl nelepte, ale vyměňte, nebo bob vyřaďte. Lepený plast se při další ráně rozlomí znovu.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Bob kupovaný „na vyrůstání“, na kterém malé dítě nedosáhne na volant ani brzdy.</li>'
          '<li>Dětský bob pro dospělého, který ho přetíží.</li>'
          '<li>Spoléhání na brzdy na zledovatělém svahu.</li>'
          '<li>Jízda bez helmy na kopci, který končí u silnice nebo v lese.</li>'
          '<li>Objednávka až v den, kdy napadne sníh.</li></ul>',
    faq=[
        ('Od kolika let je bob s volantem vhodný?', 'Rozhoduje doporučení výrobce a to, zda dítě dosáhne na volant a stáhne brzdy. Menším dětem obvykle stačí bob bez řízení nebo jízda s rodičem pod dohledem.'),
        ('Jak bob brzdí?', 'Většinou dvěma pákami po stranách, které zaryjí ozubené hřebeny do sněhu. Na ledu a tvrdém firnu jsou méně účinné, proto vybírejte mírný svah s dlouhým doběhem.'),
        ('Může na bobu jezdit dospělý?', 'Jen na modelu, jehož nosnost to dovoluje, typicky na dvoumístném bobu. Běžný dětský bob dospělý přetíží a řízení i brzdy pak nefungují, jak mají.'),
        ('Potřebuje dítě na bob helmu?', 'Helma je pro děti vhodná, nejlépe lyžařská. Při jízdě z kopce mohou snadno narazit do jiného jezdce, stromu nebo zmrzlého hrbolu.'),
        ('Čím se liší bob od kluzáku?', 'Bob má sedadlo, často volant a brzdy a jezdí po lyžinách. Kluzák je jednoduchá plastová plocha bez řízení, která lépe klouže v hlubokém sněhu.'),
        ('Jak bob uskladnit přes léto?', 'Suchý, ve stínu a bez zátěže na sedáku. Před další zimou zkontrolujte vůli volantu a to, zda se brzdy vracejí do výchozí polohy.'),
        ('Kde je bob skladem?', 'Na kartě produktu vidíte nabídky českých e-shopů včetně dostupnosti. Objednávka i doručení proběhnou přímo v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ sanky
NEW['sanky'] = dict(long=True,
    title='Sáňky a saně: dřevěné, kovové i skládací s opěrkou',
    desc='Dřevěné sáně, kovové a skládací sáňky, saně s opěrkou a ohrádkou pro nejmenší. Jak vybrat délku, sanice a šňůru a kde je mají české e-shopy skladem.',
    intro='<p><strong>Sáňky</strong> patří k zimě odjakživa a dobré dřevěné saně vydrží celé generaci dětí. Dnes se vedle klasických dřevěných saní s okovanými sanicemi prodávají také kovové saně s trubkovým rámem, skládací sáňky, které se vejdou do kufru auta, a modely s opěrkou nebo ohrádkou, ve kterých se vozí nejmenší děti. Každý typ se hodí na něco jiného: některé na rychlou jízdu z kopce, jiné spíš na tažení po zasněžené cestě. Než začnete vybírat, ujasněte si, kolik dětí a jak starých bude na saních jezdit, kde budete sáňkovat a jestli saně budete vozit autem na hory, nebo jen táhnout na kopec za domem. Podle toho se rozhoduje mezi těžšími dřevěnými saněmi pro dva a lehčími sáňkami, které unese i dítě.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů u jednotlivých saní a pak nakoupíte v obchodě, který si sami zvolíte. Zastoupeny jsou například značky Sulov, Rulyt a KHW. Sáňky jsou součástí kategorie <a href="/sane-a-boby/">sáně a boby</a>; pro děti, které chtějí řídit volantem, jsou určeny <a href="/boby/">boby</a>, lehčí alternativou jsou <a href="/kluzaky-na-snih/">kluzáky na sníh</a>.</p>',
    guide='<h2>Druhy saní a sáněk</h2>'
          '<p>Saně se liší hlavně materiálem, délkou a tím, kdo na nich bude sedět. Malé dítě potřebuje oporu zad a jistotu, že nevypadne, školák chce jezdit sám a rychle, rodič s dítětem ocení dlouhé saně pro dva.</p>'
          + T(['Typ', 'Konstrukce', 'Hodí se pro'], [
              ['Dřevěné saně', 'dřevěné ližiny a sedák, sanice okované ocelovým páskem', 'jízdu z kopce, jednoho i dva jezdce'],
              ['Kovové saně', 'ocelový trubkový rám, sedák z dřevěných latí nebo plastu', 'děti i dospělé, uježděný sníh'],
              ['Skládací sáňky', 'kovový rám se sklopnými díly', 'cestování autem, malý byt'],
              ['Saně s opěrkou', 'odnímatelné opěradlo za zády', 'menší děti, které už sedí samy'],
              ['Saně s ohrádkou', 'ohrádka kolem sedáku, často s pásem', 'nejmenší děti při tažení po rovině'],
              ['Saně s vodicí tyčí', 'tlačné madlo pro dospělého', 'procházky se dvěma rukama na řízení'],
              ['Rohaté saně (rohačky)', 'velké dřevěné saně se zvednutými rohy vpředu', 'dospělé, tradiční jízda z kopce']]) +
          '<h2>Dřevěné saně: klasika, která vydrží</h2>'
          '<p>Tradiční dřevěné saně mají dvě prohnuté ližiny spojené příčkami a sedák z latí. Na spodní hraně ližin je přišroubovaný ocelový pásek, kterému se říká okování. Díky němu saně dobře kloužou po uježděném sněhu i po ledu a dřevo se o kameny a štěrk neodírá. Ve sněhu se saně řídí nohama a tahem za přední část. Kdo sedí vpředu, pomáhá si patami, zkušenější jezdci přenášejí váhu a přitahují špičku saní provázkem nebo rukama. V obchodech se dřevěné saně prodávají i pod tradičními modelovými jmény, například Tatra nebo Davos.</p>'
          '<p>Při výběru se dívejte na délku. Krátké saně stačí jednomu dítěti, delší pojmou dospělého s dítětem před sebou. Dřevo by mělo být lakované nebo napuštěné, bez trhlin a s pevnými spoji. Uvolněná příčka se dá většinou dotáhnout, prasklá ližina ale znamená konec saní. Hmotnost dřevěných saní je vyšší než u plastových kluzáků, menší dítě je proto do kopce samo vytáhne jen s obtížemi.</p>'
          '<h2>Kovové a skládací sáňky</h2>'
          '<p>Kovové saně mají rám z ocelových trubek a sedák z dřevěných latí, plastu nebo pevné tkaniny. Jsou méně citlivé na vlhko než dřevo a po uježděném sněhu jedou rychle. Skládací varianty se po uvolnění pojistky sklopí do ploché podoby, takže se vejdou do kufru auta i do skříně na chodbě. Před každou jízdou zkontrolujte, že je zámek rozložení dobře zacvaknutý, protože povolený kloub by se mohl pod jezdcem sklopit. Kovové díly po sezóně otřete do sucha, jinak se ve spojích objeví rez.</p>'
          '<h2>Sáňky pro nejmenší</h2>'
          '<p>Pro batolata a malé děti jsou určeny saně s opěrkou, ohrádkou a často i bezpečnostním pásem. Některé mají vzadu vodicí tyč, takže je rodič tlačí před sebou a má přehled, co dítě dělá. Tyto modely slouží hlavně k tažení po rovině a na procházku, ne ke sjíždění kopce. Dítě, které sedí bez pohybu, prochladne mnohem rychleji než to, které běhá. Proto ho oblékněte tepleji než sebe, pod sebe dejte izolační podložku a fusak nebo deku a na procházce pravidelně kontrolujte, jestli nemá studené ruce a nohy.</p>'
          '<p>Opěrka a ohrádka bývají odnímatelné, takže saně porostou s dítětem: z vozítka pro batole se později stanou běžné sáňky. Zkontrolujte, zda se opěrka dá připevnit pevně a nekývá se, a zda ohrádka nemá mezery, kterými by dítě mohlo prostrčit nohu.</p>'
          '<h2>Jak vybrat sáňky podle věku</h2>'
          + T(['Věk a zkušenost', 'Vhodný typ', 'Na co myslet'], [
              ['Batole, které ještě samo nesedí jisté', 'saně s ohrádkou a pásem, tažené po rovině', 'teplá podložka, fusak, krátké procházky'],
              ['Malé dítě, které sedí samo', 'saně s opěrkou, jízda s rodičem', 'mírný kopec, rodič sedí vzadu a řídí'],
              ['Předškolák a mladší školák', 'krátké dřevěné nebo kovové sáňky', 'helma, dozor, svah s volným doběhem'],
              ['Starší děti', 'delší saně, případně bob nebo kluzák', 'dítě si saně vytáhne do kopce samo'],
              ['Dospělí a rodiny', 'dlouhé dřevěné saně pro dva, rohačky', 'nosnost a pevné spoje']]) +
          '<h2>Saně pro dva a rodinné výlety</h2>'
          '<p>Dlouhé dřevěné saně jsou nejlepší společník na zimní výlet s dětmi. Dospělý sedí vzadu, nohama řídí a brzdí, dítě sedí vpředu a drží se. Při jízdě dvou osob se rychlost zvyšuje, protože saně jsou těžší, a proto vybírejte kopec, na kterém se dá včas zastavit. Na výletě po horské cestě se saně táhnou za šňůru a do kopce může dítě sedět na nich, z kopce pak jede celá rodina společně. Na lesních cestách sledujte, zda na stejné cestě nejezdí auta, lesní technika nebo koně se saněmi.</p>'
          '<p>Rohačky jsou velké saně se zahnutými rohy vpředu, za které se při jízdě drží a které slouží i k řízení. Dříve se na nich na horách sváželo dřevo a seno, dnes se na nich jezdí hlavně pro radost a na tradičních závodech. Jsou těžké a rychlé a na kopec patří jen dospělým, kteří vědí, jak je ubrzdit.</p>'
          '<h2>Šňůra a tažení</h2>'
          '<p>Šňůra má být tak dlouhá, aby saně při chůzi nenarážely do pat, ale zároveň se po ní dítě nemohlo zamotat. Dětem ji nikdy neomotávejte kolem zápěstí ani krku a nedovolte jim to ani při hře. Na rovině se saně táhnou lehce, do kopce pomáhá široké madlo nebo popruh přes rameno. Šňůru po zimě zkontrolujte a roztřepenou vyměňte, protože právě ona se nejčastěji přetrhne v nevhodnou chvíli.</p>'
          '<h2>Bezpečné sáňkování</h2>'
          '<ul><li>Sáňkujte jen na svahu, který nekončí u silnice, železnice, vody ani u plotu.</li>'
          '<li>Dětem nasaďte helmu, například <a href="/lyzarske-helmy/">lyžařskou</a>; při pádu ze saní narážejí hlavou nejčastěji.</li>'
          '<li>Jezděte vsedě a nohama napřed, ne vleže hlavou dolů.</li>'
          '<li>Malé děti nechte jezdit jen pod dozorem a na saních bez opěrky je nepouštějte na prudší kopec.</li>'
          '<li>Na jedněch saních jen tolik jezdců, pro kolik jsou stavěné.</li>'
          '<li>Saně nikdy nepřipojujte za auto, traktor ani sněžný skútr.</li></ul>'
          '<p>Na upravených sáňkařských drahách v horských střediscích mívá provozovatel vlastní řád. Někde se jezdí jen na zapůjčených saních, jinde je povinná helma nebo minimální věk. Informace bývají na webu střediska a u pokladny.</p>'
          '<h2>Oblečení na sáňkování</h2>'
          '<p>Při sáňkování se střídá zahřátí při výstupu a prochladnutí při jízdě dolů a sníh se dostane všude. Dětem se nejlépe osvědčí <a href="/lyzarske-kombinezy/">lyžařská kombinéza</a>, která nepropustí sníh v pase, nepromokavé rukavice s dlouhou manžetou a zimní boty s pevnou podrážkou, protože se nohama i brzdí. Vlněná nebo funkční vrstva na těle odvede pot lépe než bavlna.</p>'
          '<h2>Péče o saně</h2>'
          '<ul><li><strong>Sušení:</strong> dřevěné saně nechte oschnout volně, ne u topení. Rychlé sušení dřevo kroutí a praská.</li>'
          '<li><strong>Okování:</strong> rez na sanicích obruste jemným smirkovým papírem a lehce namažte voskem nebo parafínem, saně pak lépe kloužou.</li>'
          '<li><strong>Dřevo:</strong> odřený lak obnovte, než do dřeva začne vnikat voda.</li>'
          '<li><strong>Šrouby:</strong> před sezónou je dotáhněte, spoje se během zimy uvolňují.</li>'
          '<li><strong>Uložení:</strong> v suché kůlně nebo ve sklepě, nejlépe zavěšené na stěně.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Krátké saně pro rodiče, který chce jezdit s dítětem.</li>'
          '<li>Saně s ohrádkou použité ke sjíždění kopce.</li>'
          '<li>Skládací saně bez kontroly pojistky.</li>'
          '<li>Dítě v saních oblečené stejně jako rodič, který jde pěšky.</li>'
          '<li>Výběr až po prvním sněhu, kdy oblíbené modely chybí na skladě.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>U každých saní vidíte nabídky obchodů, které je mají v katalogu, a zjistíte, kde jsou k dodání ještě před víkendem na horách. Objednávku dokončíte v e-shopu. Celé zimní vybavení najdete v sekci <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[
        ('Jaké sáňky koupit pro batole?', 'Saně s opěrkou, ohrádkou a pásem, ideálně s vodicí tyčí. Slouží k tažení po rovině, ne ke sjíždění kopce, a dítě v nich potřebuje teplou podložku a deku.'),
        ('Jsou lepší dřevěné, nebo kovové saně?', 'Dřevěné s okovanými sanicemi vydrží desítky zim a dobře jedou po uježděném sněhu. Kovové jsou odolnější proti vlhku a skládací varianty se snadno převážejí.'),
        ('Jak dlouhé saně vybrat pro dva?', 'Takové, na které se vejde dospělý s dítětem před sebou bez přesahu nohou. Výrobce u delších modelů obvykle uvádí, že jsou určeny pro dvě osoby, a uvádí i nosnost.'),
        ('Proč saně špatně kloužou?', 'Nejčastěji kvůli rzi na okování nebo mokrému sněhu. Rez obruste jemným smirkovým papírem a sanice ošetřete voskem nebo parafínem.'),
        ('Potřebuje dítě na sáňky helmu?', 'Helma je vhodná, protože při pádu ze saní dopadají děti často na hlavu. Poslouží lyžařská helma, která kryje i zátylek.'),
        ('Jak skladovat dřevěné saně?', 'V suchu, mimo topení a přímé slunce, nejlépe zavěšené. Odřený lak obnovte a před zimou dotáhněte šrouby.'),
        ('Co jsou rohačky?', 'Velké dřevěné saně se zahnutými rohy vpředu, za které se jezdec drží a kterými řídí. Dříve sloužily ke svážení dřeva a sena z hor, dnes hlavně k zábavě a tradičním závodům. Jsou těžké a rychlé, proto patří dospělým.'),
        ('Prodává Sporteka saně přímo?', 'Ne. Sporteka porovnává nabídky českých e-shopů a nákup dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ whey-proteiny
NEW['whey-proteiny'] = dict(long=True,
    title='Whey protein: syrovátkový koncentrát, izolát i clear',
    desc='Whey protein a syrovátkový protein: koncentrát WPC, izolát WPI, hydrolyzát i clear whey. Jak číst etiketu, laktóza a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Whey protein</strong>, česky syrovátkový protein, je nejrozšířenější doplněk sportovní výživy. Vyrábí se ze syrovátky, tekutiny, která zbývá při výrobě sýra, a obsahuje mléčné bílkoviny v koncentrované podobě. Pod jedním názvem se ale skrývá několik výrobků. Koncentrát WPC je nejběžnější, izolát WPI obsahuje víc bílkovin a méně laktózy a tuku, hydrolyzát je částečně naštěpený a clear whey se pije jako ovocná limonáda, ne jako mléčný koktejl. Liší se i obsahem bílkovin na porci, chutí a tím, jak se rozmíchá v šejkru. Kdo kupuje protein poprvé, obvykle začíná koncentrátem s oblíbenou příchutí. Kdo má citlivé trávení nebo hlídá každý gram tuku, sáhne spíš po izolátu.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů a nákup proběhne v obchodě, který si vyberete. Najdete tu proteiny značek ' + B(('gymbeam', 'GymBeam')) + ', MyProtein, BioTech USA, Nutrend, Extrifit nebo Amix. Nadřazenou kategorií jsou <a href="/proteiny/">proteiny</a>, kdo nesnáší mléko, najde náhradu mezi <a href="/veganske-proteiny/">veganskými proteiny</a>. K wheyi se často kupuje <a href="/kreatin/">kreatin</a> a <a href="/sejkry/">šejkr</a>.</p>',
    guide='<h2>Odkud se syrovátkový protein bere</h2>'
          '<p>Kravské mléko obsahuje dvě hlavní skupiny bílkovin: kasein a syrovátkové bílkoviny. Při výrobě sýra se kasein sráží do sýřeniny a syrovátkové bílkoviny zůstávají rozpuštěné v tekuté syrovátce. Ta se pak filtruje, aby se oddělila voda, laktóza, tuk a minerály, a nakonec suší na prášek. Podle toho, jak důkladná filtrace je, vzniká koncentrát, nebo izolát. Existuje také takzvaný nativní syrovátkový protein, který se získává filtrací přímo z mléka, bez výroby sýra.</p>'
          '<h2>Koncentrát, izolát, hydrolyzát a clear</h2>'
          + T(['Forma', 'Bílkoviny v sušině', 'Laktóza a tuk', 'Typické použití'], [
              ['Koncentrát (WPC)', 'u sportovních výrobků obvykle kolem 70–80 %', 'obsahuje laktózu i trochu tuku', 'běžné doplnění bílkovin, kaše, pečení'],
              ['Izolát (WPI)', '90 % a více', 'laktózy a tuku jen málo', 'při citlivosti na laktózu, při dietě'],
              ['Hydrolyzát (WPH)', 'podle výchozí suroviny', 'záleží na tom, zda vznikl z WPC, nebo WPI', 'kdo chce snadno stravitelnou formu'],
              ['Clear whey', 'obvykle na bázi izolátu', 'velmi málo', 'osvěžující nápoj s vodou'],
              ['Směs (blend)', 'kombinace WPC, WPI, případně kaseinu', 'podle podílu složek', 'kompromis mezi chutí a složením']]) +
          '<p>Označení WPC80 znamená koncentrát s přibližně 80 % bílkovin v sušině suroviny. Hotový výrobek s příchutí, sladidly a zahušťovadly má bílkovin na 100 g méně, proto vždy čtěte tabulku nutričních hodnot, ne jen název. Izolát vzniká jemnější filtrací, například mikrofiltrací nebo iontovou výměnou, a je v něm méně všeho, co není bílkovina. Hydrolyzát prošel enzymatickým štěpením na kratší peptidy. Bývá výrazně hořčí a jeho výroba je nákladnější, takže se často přidává jen jako podíl do směsi.</p>'
          '<h2>Clear whey: protein, který nepřipomíná mléko</h2>'
          '<p>Clear protein je izolát upravený tak, aby se ve vodě rozpustil do čirého nápoje. Příchutě bývají ovocné, třeba citron, malina nebo mojito, a výsledek chutná spíš jako limonáda. Míchá se jen s vodou, s mlékem ne. Po protřepání vytvoří pěnu, která za chvíli opadne, proto je dobré nechat šejkr minutu stát. Clear whey si oblíbili lidé, kterým po tréninku nejde do žaludku hustý mléčný koktejl, a také ti, kdo protein pijí v létě.</p>'
          '<h2>Laktóza a mléčná alergie</h2>'
          '<p>Koncentrát obsahuje laktózu, mléčný cukr, a lidé s intolerancí laktózy po něm mohou mít nadýmání nebo jiné trávicí potíže. Izolát má laktózy podstatně méně a mnoho lidí s mírnou intolerancí ho snáší dobře. Bez laktózy ale být nemusí, pokud to výrobce výslovně neuvádí. Jinak je to s alergií na bílkovinu kravského mléka. Syrovátkový protein je mléčná bílkovina, takže při alergii nepřipadá v úvahu žádná jeho forma a vhodnější je rostlinná alternativa.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<ul><li><strong>Bílkoviny na 100 g a na porci:</strong> hlavní údaj pro porovnání výrobků. Velikost porce se mezi značkami liší, proto porovnávejte údaj na 100 g.</li>'
          '<li><strong>Pořadí složek:</strong> syrovátková bílkovina by měla být na prvním místě. Složky se uvádějí sestupně podle množství.</li>'
          '<li><strong>Aminokyselinový profil:</strong> seriózní výrobci uvádějí aminogram. Volné aminokyseliny jako glycin nebo taurin přidané do proteinu mohou uměle zvýšit naměřený obsah dusíku, tedy i deklarované bílkoviny.</li>'
          '<li><strong>Cukr a sladidla:</strong> běžná je sukralóza nebo acesulfam K, některé řady slazené steviolglykosidy, varianty bez příchuti jsou neslazené.</li>'
          '<li><strong>Emulgátory:</strong> lecitin, nejčastěji slunečnicový nebo sójový, zlepšuje rozpustnost u instantních proteinů.</li>'
          '<li><strong>Alergeny:</strong> mléko vždy, podle výroby i sója nebo lepek ve stopovém množství.</li></ul>'
          '<h2>Co smí výrobce slibovat</h2>'
          '<p>Pro bílkoviny schválila Evropská unie tři zdravotní tvrzení. Bílkoviny přispívají k růstu svalové hmoty. Bílkoviny přispívají k udržení svalové hmoty. Bílkoviny přispívají k udržení normálního stavu kostí. Výrobce je smí použít jen u potraviny, která je přinejmenším zdrojem bílkovin, tedy když bílkoviny tvoří alespoň 12 % její energetické hodnoty; u proteinového prášku je tato podmínka splněna snadno. Sliby typu „spaluje tuk“, „zrychlí regeneraci“ nebo „zvýší testosteron“ mezi schválená tvrzení pro bílkoviny nepatří.</p>'
          '<p>Svaly samy od sebe nerostou ani z nejlepšího proteinu. Rozhoduje trénink, celkový příjem energie a bílkovin z běžné stravy a spánek. Protein je pohodlný způsob, jak doplnit bílkoviny tam, kde je z jídla nezískáte.</p>'
          '<h2>Jak se whey používá</h2>'
          '<p>Nejčastěji se rozmíchá ve vodě nebo mléce v šejkru. S mlékem je koktejl hustší a krémovější, s vodou lehčí a rychleji připravený. Whey jde přidat i do ovesné kaše, jogurtu, tvarohu nebo palačinek; při pečení se ale chová jinak než mouka a těsto může vysychat. Velikost porce a počet porcí za den stanoví etiketa výrobku, ten je třeba dodržovat. Pokud chcete vědět, kolik bílkovin skutečně potřebujete, poraďte se s nutričním terapeutem.</p>'
          '<h2>Whey, kasein, nebo gainer?</h2>'
          '<p>Syrovátkové bílkoviny se v trávicím traktu rozkládají rychle, kasein pomaleji, protože v žaludku vytvoří sraženinu. Kasein se proto oblíbil jako proteinový nápoj na večer nebo jako náhrada svačiny, po které člověk dlouho nemá hlad. Mnoho výrobců prodává obě bílkoviny i ve směsi, které se říká vícesložkový protein. <a href="/gainery/">Gainery</a> jsou jiná kategorie: obsahují bílkoviny, ale hlavně velké množství sacharidů a energie, a jsou určené lidem, kteří potřebují zvýšit celkový příjem kalorií. Kdo chce doplnit jen bílkoviny, sáhne po čistém wheyi.</p>'
          '<p>Syrovátkový protein přirozeně obsahuje i aminokyseliny s rozvětveným řetězcem, které se jinak prodávají samostatně jako <a href="/aminokyseliny-bcaa/">aminokyseliny BCAA</a>. Pokud proteinové výrobky chcete mít po ruce i mimo domov, existují <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>, často také s whey proteinem ve složení.</p>'
          '<h2>Whey v kuchyni</h2>'
          '<p>Syrovátkový protein se nemusí jen pít. Neutrální nebo vanilková varianta se přidává do ovesných vloček, do tvarohového krému, do jogurtu s ovocem nebo do lívanců. Při vaření a pečení je dobré vědět, že se bílkoviny teplem mění a protein v těstě váže vodu, takže pečivo může být sušší. Pomůže přidat víc tekutiny, jogurtu nebo rozmačkaný banán a protein nahradit jen část mouky, ne celou. Pokud protein přimícháváte do teplé kaše, vmíchejte ho až po odstavení z plotny, jinak se mohou dělat hrudky. Clear whey se do vaření nehodí, jeho místem je sklenice s ledovou vodou.</p>'
          '<h2>Původ mléka a značení</h2>'
          '<p>Na obalech se objevují označení jako grass-fed, tedy mléko od krav krmených převážně pastvou, nebo údaje o zemi původu suroviny. Jde o informaci o původu, ne o zdravotní účinek. Některé proteiny nesou také certifikaci nezávislé laboratoře, že neobsahují látky zakázané ve sportu. To ocení hlavně závodní sportovci, kteří podléhají antidopingovým kontrolám.</p>'
          '<h2>Příchutě a rozpustnost</h2>'
          '<p>Kvalitní instantní protein se rozmíchá v šejkru během několika vteřin, bez hrudek. Neutrální varianta bez příchuti se hodí do vaření, ochucené řady nabízejí čokoládu, vanilku, jahodu, slaný karamel nebo kokos. Pokud příchuť neznáte, vyzkoušejte nejdřív malé balení nebo vzorek. Velké balení se vyplatí až u osvědčené chuti, jinak zůstane dóza napůl plná v kuchyňské skříni.</p>'
          '<h2>Kdy dát pozor</h2>'
          '<p>Protein je potravina, ne lék, a pro většinu zdravých dospělých je běžnou součástí jídelníčku. Lidé s onemocněním ledvin by měli příjem bílkovin konzultovat s lékařem. Těhotné a kojící ženy a děti by měly sportovní doplňky užívat jen po poradě s odborníkem. Proteinový nápoj nemá nahrazovat pestrou stravu.</p>'
          '<h2>Skladování</h2>'
          '<p>Dózu nebo sáček po použití dobře uzavřete a skladujte v suchu, mimo vlhkou koupelnu a horko. Vlhkost způsobuje hrudky a zkracuje trvanlivost. Odměrku nabírejte suchou rukou, nikdy mokrou lžící.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Porovnávání podle velikosti balení místo obsahu bílkovin na 100 g.</li>'
          '<li>Koncentrát při intoleranci laktózy, kde by stačil izolát.</li>'
          '<li>Velké balení neznámé příchuti.</li>'
          '<li>Víra, že protein nahradí trénink nebo jídlo.</li>'
          '<li>Přehlédnutí alergenů ve složení.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi WPC a WPI?', 'Koncentrát WPC obsahuje méně bílkovin a víc laktózy a tuku. Izolát WPI prošel důkladnější filtrací, bílkovin má v sušině 90 % a více a laktózy jen málo.'),
        ('Co je clear whey?', 'Izolát upravený tak, aby se ve vodě rozpustil do čirého nápoje s ovocnou příchutí. Míchá se jen s vodou a chutná spíš jako limonáda než mléčný koktejl.'),
        ('Mohu whey při intoleranci laktózy?', 'Izolát mnoho lidí s mírnou intolerancí snáší, laktózy má ale jen méně, ne nulu, pokud to není výslovně uvedeno. Při alergii na mléčnou bílkovinu není vhodná žádná forma.'),
        ('Je syrovátkový protein totéž co whey?', 'Ano. Whey je anglický název pro syrovátku, syrovátkový protein a whey protein znamenají totéž.'),
        ('Co protein skutečně dělá?', 'Podle schválených tvrzení EU bílkoviny přispívají k růstu svalové hmoty, k udržení svalové hmoty a k udržení normálního stavu kostí. Další sliby schválené nejsou.'),
        ('Kolik proteinu denně?', 'Velikost a počet porcí uvádí etiketa výrobku. Celkovou potřebu bílkovin ovlivňuje strava, hmotnost i trénink; přesně ji určí nutriční terapeut.'),
        ('Lze whey použít na pečení?', 'Ano, neutrální nebo vanilkový whey se přidává do lívanců, kaše nebo tvarohu. Nahraďte jím jen část mouky a přidejte víc tekutiny, jinak bude pečivo suché. Clear whey se na pečení nehodí.'),
        ('Čím se liší whey a kasein?', 'Obě jsou mléčné bílkoviny. Syrovátkové bílkoviny se tráví rychleji, kasein pomaleji, protože v žaludku vytváří sraženinu, a proto se často pije večer.'),
        ('Mohu whey míchat s mlékem?', 'Klasický whey ano, koktejl je pak hustší. Clear whey se míchá jen s vodou.'),
    ])

# ------------------------------------------------------------------ veganske-proteiny
NEW['veganske-proteiny'] = dict(long=True,
    title='Vegan protein: rostlinné proteiny z hrachu, sóji i rýže',
    desc='Vegan protein a rostlinný protein z hrachu, sóji, rýže a konopí i jejich směsi. Aminokyselinový profil, chuť, etiketa a nabídky českých e-shopů.',
    intro='<p><strong>Veganský protein</strong> se vyrábí z rostlin, nejčastěji z hrachu, sóji, hnědé rýže, konopných nebo dýňových semínek. Kupují ho vegani a vegetariáni, ale také lidé, kterým nesedí mléčné výrobky, nebo ti, kdo chtějí v jídelníčku víc rostlinných zdrojů bílkovin. Jednotlivé rostliny se liší složením aminokyselin, chutí i tím, jak se rozmíchají. Proto výrobci rostlinné zdroje často kombinují do směsí, které se svým složením přiblíží proteinům živočišného původu. V nabídce najdete jednodruhové proteiny, například čistý hrachový nebo konopný, i směsi tří a více zdrojů. Liší se nejen chutí a hustotou, ale i obsahem bílkovin na 100 g a tím, jak se hodí do kuchyně.</p>'
          '<p>Sporteka shromažďuje nabídky českých obchodů k jednotlivým výrobkům a objednávku dokončíte přímo v e-shopu, který vám vyhovuje. Veganské řady mají i velcí výrobci sportovní výživy, například ' + B(('gymbeam', 'GymBeam')) + ', MyProtein nebo BioTech USA. Kategorie spadá pod <a href="/proteiny/">proteiny</a>; pro srovnání se podívejte i na <a href="/whey-proteiny/">whey proteiny</a>, k rozmíchání se hodí <a href="/sejkry/">šejkry</a>.</p>',
    guide='<h2>Z čeho se rostlinné proteiny vyrábějí</h2>'
          '<p>Rostlinný protein vzniká tak, že se ze suroviny oddělí škrob, vláknina a tuk a zbylá bílkovina se usuší na jemný prášek. Hrachový protein se získává ze žlutého hrachu, sójový ze sójových bobů, rýžový z hnědé rýže. Každý zdroj má svoje silné a slabé stránky a žádný není univerzálně nejlepší.</p>'
          + T(['Zdroj', 'Vlastnosti', 'Na co pamatovat'], [
              ['Hrách', 'dobře se rozpouští, jemná chuť, bohatý na lysin', 'méně methioninu, proto se kombinuje'],
              ['Sója', 'obsahuje všechny esenciální aminokyseliny v dobrém poměru', 'patří mezi hlavní alergeny'],
              ['Hnědá rýže', 'snadno stravitelná, neutrální', 'méně lysinu, ideální partner hrachu'],
              ['Konopí', 'obsahuje vlákninu a tuk, zemitá chuť', 'nižší podíl bílkovin v prášku'],
              ['Dýňová semínka', 'výrazná chuť, zelenavá barva', 'častěji jako součást směsi'],
              ['Směs (blend)', 'spojuje silné stránky několika zdrojů', 'podíl složek uvádí etiketa']]) +
          '<h2>Proč se rostlinné zdroje míchají</h2>'
          '<p>Bílkoviny se skládají z aminokyselin a devět z nich si tělo neumí vyrobit, musí je dostat z potravy. Říká se jim esenciální. Živočišné bílkoviny je obsahují všechny ve vyváženém poměru, rostlinné často některé z nich v menším množství. Hrachu chybí hlavně methionin, rýži lysin. Když se oba zdroje spojí, jeden doplní slabinu druhého a výsledný profil je vyrovnanější. Proto mají směsi hrachu a rýže v nabídce takové zastoupení. Sója je mezi rostlinami výjimka, protože esenciální aminokyseliny obsahuje v poměru blízkém živočišným bílkovinám.</p>'
          '<p>Rostlinné bílkoviny obecně obsahují méně leucinu než syrovátka. Někteří výrobci proto do směsí přidávají volné aminokyseliny, případně uvádějí obsah leucinu na porci zvlášť. Úplný aminogram na obalu nebo na webu výrobce je dobrým znamením, že výrobce nemá co skrývat.</p>'
          '<h2>Jak se měří kvalita bílkovin</h2>'
          '<p>Pro srovnání kvality bílkovin se používá skóre PDCAAS. Bere v úvahu obsah esenciálních aminokyselin i to, jak dobře je tělo dokáže strávit, a nejvyšší hodnota je 1,0. Sója se pohybuje blízko horní hranice, jednotlivé obilné a luštěninové zdroje bývají níž, správně namíchané směsi se k vrcholu přibližují. Novější metodou je DIAAS, která stravitelnost hodnotí podrobněji, pro jednotlivé aminokyseliny zvlášť. Pro běžný nákup stačí vědět, že směs několika zdrojů nebo sója mají vyrovnanější složení než jediná surovina.</p>'
          '<h2>Chuť, textura a rozmíchání</h2>'
          '<p>Rostlinný protein chutná jinak než mléčný. Hrachový bývá jemně luštěninový, konopný zemitý, rýžový moučný. Nápoj je obvykle hustší a v šejkru potřebuje o něco víc vody nebo delší protřepání. Výrazné příchutě jako čokoláda, lískový oříšek nebo slaný karamel tyto tóny dobře překryjí. Velmi dobře se rostlinné proteiny hodí do smoothie s banánem, do ovesné kaše nebo do palačinek, kde se jejich hustota stává výhodou. S rostlinným mlékem, třeba ovesným nebo mandlovým, je koktejl krémovější než s vodou.</p>'
          '<h2>Na co se dívat na etiketě</h2>'
          '<ul><li><strong>Bílkoviny na 100 g:</strong> rostlinné proteiny mívají obvykle o něco nižší podíl než syrovátkový izolát, konopný ještě nižší.</li>'
          '<li><strong>Zdroje a jejich podíl:</strong> u směsí hledejte, které suroviny a v jakém pořadí obsahují.</li>'
          '<li><strong>Označení vegan:</strong> certifikát nebo logo vegan potvrzuje, že výrobek neobsahuje živočišné složky.</li>'
          '<li><strong>Alergeny:</strong> sója je alergen; pokud se výrobek balí na lince, kde se zpracovává mléko, uvádí výrobce, že může obsahovat jeho stopy.</li>'
          '<li><strong>Sladidla a přísady:</strong> stévie, sukralóza, zahušťovadla, někdy trávicí enzymy nebo přidaný vitamín B12.</li></ul>'
          '<h2>Schválená tvrzení platí pro rostlinné bílkoviny stejně</h2>'
          '<p>Zdravotní tvrzení EU nerozlišují, zda bílkovina pochází z rostliny, nebo z mléka. I u rostlinného proteinu tedy smí výrobce uvést, že bílkoviny přispívají k růstu svalové hmoty, k udržení svalové hmoty a k udržení normálního stavu kostí. Podmínkou je, že potravina je alespoň zdrojem bílkovin. Slova jako „detox“, „nakopne metabolismus“ nebo „čistí tělo“ schváleným tvrzením nejsou a k proteinu nepatří.</p>'
          '<h2>Čistota surovin</h2>'
          '<p>Rostliny přijímají z půdy kromě živin i stopové prvky, mezi nimi těžké kovy. U rostlinných proteinů, zejména rýžových, se proto občas sleduje obsah olova nebo kadmia. Zavedení výrobci pravidelně nechávají suroviny testovat a výsledky rozborů některé z nich zveřejňují. Pokud vám na tom záleží, hledejte značky, které takové informace nabízejí, a střídejte zdroje bílkovin v jídelníčku. Střídání má i další výhodu: každá rostlina přináší jiné spektrum živin a jídelníček je pak pestřejší, než kdybyste celý rok pili jediný druh proteinu.</p>'
          '<h2>Rostlinný protein v kuchyni</h2>'
          '<p>Díky hustší konzistenci se rostlinné proteiny výborně hodí do jídel. Přidávají se do ovesné kaše, chia pudinku, do těsta na palačinky a lívance nebo do domácích energetických kuliček z datlí a ořechů. Neochucená varianta se dá přimíchat i do slaných jídel, třeba do pomazánky nebo polévky, kde hrachová chuť nevadí. Při pečení protein vysušuje těsto podobně jako mouka s vysokým obsahem bílkovin, proto přidejte víc tekutiny nebo ovoce. Do horké kaše ho vmíchejte až po odstavení, aby nevznikly hrudky.</p>'
          '<p>Kdo nechce míchat vlastní recepty, najde rostlinné bílkoviny i v hotových výrobcích. Mnoho <a href="/proteinove-tycinky-a-snacky/">proteinových tyčinek a snacků</a> má veganskou variantu a další nápady nabízí kategorie <a href="/fit-potraviny/">fit potraviny</a>.</p>'
          '<h2>Rostlinný protein a další doplňky</h2>'
          '<p>Vegani se často ptají, zda jsou pro ně vhodné i další doplňky sportovní výživy. <a href="/kreatin/">Kreatin</a> v doplňcích se obvykle vyrábí synteticky, ne z masa, a je proto běžně označený jako veganský; přesto se vyplatí zkontrolovat, z čeho je vyrobena kapsle, protože želatina je živočišného původu. Aminokyseliny BCAA se dnes většinou vyrábějí fermentací rostlinných surovin. U vitamínu D3 se rozlišuje živočišný zdroj z ovčího lanolinu a rostlinný z lišejníku. Pokud vám jde o veganský jídelníček do důsledku, hledejte na obale logo vegan nebo informaci o původu.</p>'
          '<h2>Jak rostlinný protein vybrat</h2>'
          '<ol><li>Rozhodněte se, zda chcete jediný zdroj, nebo směs. Pro většinu lidí je praktičtější směs hrachu a rýže nebo sójový protein.</li>'
          '<li>Zkontrolujte alergeny. Pokud nesnášíte sóju nebo lepek, hledejte výrobek, který je výslovně neobsahuje.</li>'
          '<li>Porovnejte obsah bílkovin na 100 g a aminogram, ne jen velikost balení.</li>'
          '<li>Vyzkoušejte příchuť v menším balení. Chuť rostlinných proteinů se mezi výrobci liší víc než u syrovátky.</li>'
          '<li>Zvažte, k čemu protein použijete. Do kuchyně se hodí neutrální, na pití po tréninku ochucený.</li></ol>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Rostlinné proteiny obsahují víc vlákniny a u konopného nebo dýňového i tuk, který může při dlouhém skladování v teple žluknout. Balení proto uchovávejte uzavřené, v suchu a chladu, mimo přímé slunce. Sáček se zipem po každém použití dobře uzavřete a vytlačte z něj vzduch. Pokud protein změní vůni nebo chuť, nepoužívejte ho, i když datum minimální trvanlivosti ještě neuplynulo. Větší balení se vyplatí jen tehdy, když ho během několika měsíců spotřebujete.</p>'
          '<h2>Pro koho je rostlinný protein</h2>'
          '<p>Hodí se pro vegany a vegetariány, pro lidi s alergií na mléčnou bílkovinu a pro ty, kterým laktóza dělá potíže i v malém množství. Někdo ho volí prostě proto, že mu chutná nebo že chce omezit živočišné potraviny. Kdo nemá důvod mléko vynechávat, nemusí rostlinný protein považovat za lepší ani horší volbu, jde hlavně o osobní preference. Velikost porce a jejich počet se řídí etiketou výrobku. Vegani, kteří chtějí doplnit i další živiny, najdou užitečné doplňky v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Hrachový nebo rýžový protein samostatně tam, kde by se hodila směs.</li>'
          '<li>Přehlédnutí sóji ve složení u alergika.</li>'
          '<li>Míchání v malém množství vody, ze kterého vznikne hustá kaše.</li>'
          '<li>Očekávání, že bude chutnat jako mléčný koktejl.</li>'
          '<li>Výběr jen podle obsahu bílkovin bez pohledu na aminogram.</li></ul>',
    faq=[
        ('Který rostlinný protein je nejlepší?', 'Žádný jednotlivý zdroj nevyhrává ve všem. Vyvážené složení mají sójový protein a směsi hrachu s rýží, u kterých se aminokyseliny navzájem doplňují.'),
        ('Je vegan protein plnohodnotný?', 'Sója obsahuje všechny esenciální aminokyseliny v dobrém poměru, ostatní zdroje se kombinují do směsí. Správně namíchaná směs má vyrovnaný aminokyselinový profil.'),
        ('Co znamená PDCAAS?', 'Skóre kvality bílkovin, které hodnotí obsah esenciálních aminokyselin a jejich stravitelnost. Nejvyšší hodnota je 1,0, novější metodou je DIAAS.'),
        ('Je rostlinný protein vhodný při alergii na mléko?', 'Ano, neobsahuje mléčné bílkoviny. Zkontrolujte ale upozornění na stopy mléka z výrobní linky a u sóji také to, zda nejste alergičtí na ni.'),
        ('Proč je rostlinný protein hustší?', 'Rostlinné bílkoviny vážou víc vody. Přidejte do šejkru víc tekutiny, protřepejte déle nebo použijte rostlinné mléko.'),
        ('Mohou být v rostlinném proteinu těžké kovy?', 'Rostliny je přijímají z půdy, proto se jejich stopy sledují hlavně u rýžových proteinů. Seriózní výrobci suroviny testují a rozbory někdy zveřejňují.'),
        ('Je kreatin vhodný pro vegany?', 'Kreatin v doplňcích se obvykle vyrábí synteticky, ne z masa. Zkontrolujte ale, zda kapsle nejsou z želatiny, která je živočišného původu.'),
        ('Jak dlouho vydrží otevřený rostlinný protein?', 'Řiďte se datem minimální trvanlivosti a skladujte ho uzavřený v suchu a chladu. Konopný a dýňový protein obsahují tuk, který může v teple žluknout, proto je spotřebujte dřív.'),
        ('Kde koupit vegan protein?', 'Sporteka ukáže nabídky českých e-shopů u konkrétního výrobku vedle sebe. Objednávku dokončíte v obchodě, který si vyberete.'),
    ])
