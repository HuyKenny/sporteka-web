"""sporteka.cz — wave 24h: long texts for golfove-tasky-a-voziky, meditace, dekove-spacaky, triatlon.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ golfove-tasky-a-voziky
NEW['golfove-tasky-a-voziky'] = dict(long=True,
    title='Golfové tašky a vozíky: bagy, stojany, elektrovozíky',
    desc='Golfové bagy, ruční i elektrické vozíky, kryty a náhradní díly. Jak vybrat bag na vozík, stojánkový bag nebo dětský a porovnat nabídky obchodů.',
    intro='<p>Kompletní sada holí je těžká a na hřišti se s ní nachodí několik kilometrů, takže bag a případně vozík rozhodují o tom, zda vás kolo bude bavit, nebo bolet záda. Sporteka porovnává nabídky českých obchodů u golfových bagů na vozík, stojánkových bagů, nepromokavých modelů, dětských bagů, ručních a elektrických vozíků i příslušenství jako jsou konzole, popruhy, síťky a cestovní kryty. U každé nabídky vidíte, pro jaký způsob hry je určená.</p>'
          '<p>V kategorii najdete značky ' + B(('inesis', 'Inesis'), ('sun-mountain', 'SUN Mountain'), ('callaway', 'Callaway'), ('titleist', 'Titleist'), ('taylormade', 'Taylormade'), ('trolem', 'Trolem'), ('citysports', 'Citysports')) +
          '. K bagu dokoupíte <a href="/golfove-hole/">golfové hole</a>, <a href="/golfove-micky/">golfové míčky</a>, <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a> a <a href="/golfove-doplnky/">golfové doplňky</a>.</p>',
    guide='<h2>Jaké druhy golfových bagů existují</h2>'
          '<p>Golfový bag není jen obal na hole. Podle způsobu přepravy se liší tvarem, nosným systémem, počtem přihrádek i hmotností. Než začnete porovnávat jednotlivé modely, rozhodněte se, jak budete po hřišti chodit: s bagem na zádech, s vozíkem, nebo v golfovém autíčku.</p>'
          + T(['Typ bagu', 'Charakteristika', 'Hodí se pro'], [
              ['Stojánkový bag', 'lehký, s dvojicí nožek a dvěma popruhy', 'hráče, kteří bag nosí na zádech'],
              ['Bag na vozík', 'širší hrdlo, pevné dno, úchyty pro popruhy vozíku', 'hráče s ručním nebo elektrickým vozíkem'],
              ['Nepromokavý bag', 'svařované švy, vodotěsné zipy, někdy bez dělení', 'deštivé měsíce a hráče, co hrají za každého počasí'],
              ['Dětský bag', 'zmenšený, lehký, pro krátké hole', 'děti a juniory podle věkových skupin'],
              ['Cestovní bag nebo kryt', 'polstrovaný obal na přepravu v letadle či autě', 'výjezdy na zahraniční hřiště'],
           ]) +
          '<h2>Stojánkový bag a trojnožka</h2>'
          '<p>Stojánkový bag má sklopné nožky, které se při odložení samy rozevřou, takže bag stojí na svahu i v trávě a hole nemusíte klást na zem. Kvůli nošení má dva ramenní popruhy, v lepším provedení s polstrováním a rozdělením zátěže na obě ramena. Nevýhodou je vyšší hmotnost prázdného bagu oproti variantě na vozík, protože nožky a mechanismus něco váží. Pokud chodíte převážně nižší hřiště nebo jen devítku, jde o praktickou volbu bez dalších investic.</p>'
          '<h2>Bag na vozík</h2>'
          '<p>Bagy na vozík se vyrábějí širší a plošší, protože se k vozíku upevňují popruhy a nemusí vážit co nejméně. Pozor na tvar dna: některé vozíky mají kulaté lůžko, jiné ploché nebo čtvercové, a bag s ním musí lícovat, jinak se na trase naklání. Praktické jsou čtyřcestné nebo čtrnáctidílné dělení hrdla, které oddělí hole od sebe a usnadní tahání správné hole. Pravidla golfu povolují nosit nejvýše čtrnáct holí, takže větší počet přihrádek než čtrnáct nevyužijete.</p>'
          '<h3>Dělení hrdla a manipulace s holemi</h3>'
          '<p>Čtyřcestné dělení stačí na základní sadu a bag zůstane jednodušší. Čtrnáctidílné dělení drží každou hůl na samostatném místě a chrání dříky před otěrem. Vyplatí se také úchyt na ručník, držák na deštník a přihrádka na dálkoměr, na kterou dosáhnete bez sundávání bagu z vozíku.</p>'
          '<h2>Dětský golfový bag</h2>'
          '<p>Děti rostou rychle, a proto se dětské bagy dělí podle věkových skupin, v nabídce například pro osmiletého až desetiletého hráče a pro jedenáctiletého až třináctiletého. Takový bag je kratší, užší a lehčí, aby ho dítě uneslo a hole z něj nevyčnívaly o půl metru. Pro začínajícího juniora často stačí stojánkový model s jednoduchým systémem popruhů a jednou přihrádkou na míčky a tee. Při koupi sledujte, zda se hole zasunují bez zaseknutí a zda se dá bag přenášet i bez ramenních popruhů za držadlo.</p>'
          '<h2>Ruční golfový vozík</h2>'
          '<p>Ruční vozík se táhne nebo tlačí a nese váhu bagu místo vás. Rozhodujícím parametrem je počet koleček. Dvoukolečkový model je jednodušší, levněji se opravuje a stačí na rovné hřiště. Tříkolečkový vozík se lépe řídí, nepřevrací se na svahu a snáze se tlačí jednou rukou. Dnešní konstrukce se skládají do malého rozměru, takže se vejdou do kufru kompaktního auta. Pozornost věnujte pevnosti rámu, kvalitě kloubů při skládání a tomu, zda sedí konzole bagu.</p>'
          '<h2>Elektrický golfový vozík</h2>'
          '<p>Elektrický vozík jezdí sám a hráči zbývá jen řídit směr. Hodí se na kopcovitá hřiště, pro starší hráče nebo pro každého, kdo chce na kolo zachovat sílu. Hlavní otázkou je baterie: kapacita rozhoduje, kolik jamek zvládnete na jedno nabití, a baterie je zároveň nejtěžší součást, kterou musíte při dopravě zvednout. Vozíky s odnímatelnou baterií se přenášejí snadněji. Zajímejte se o dálkové ovládání, regulaci rychlosti, brzdu na svahu a o to, zda je k dostání náhradní baterie i nabíječka.</p>'
          + T(['Vlastnost', 'Ruční vozík', 'Elektrický vozík'], [
              ['Pohon', 'sílou hráče', 'elektromotor a baterie'],
              ['Hmotnost při přenášení', 'nižší', 'vyšší kvůli baterii'],
              ['Údržba', 'kola a klouby', 'baterie, nabíječka, kola'],
              ['Vhodné hřiště', 'rovinaté nebo mírně zvlněné', 'kopcovité a delší'],
           ]) +
          '<h2>Příslušenství a náhradní díly</h2>'
          '<p>Kategorie zahrnuje i drobnosti, bez kterých vozík nebo bag nefunguje, jak má. Nejčastěji se kupují náhradní konzole na vozík s dvěma nebo třemi kolečky, protože plast praská a pásky se opotřebují. Dále síťky na úložný prostor, popruhy pro náhradní nošení bagu na zádech, kryty na konzoly a ochranné obaly na bag při přepravě. Před koupí si ověřte, pro jaký typ vozíku je díl určený: konzole pro dvoukolečkový vozík nemusí sedět na tříkolečkový.</p>'
          '<h2>Materiál, švy a voděodolnost</h2>'
          '<p>Většina bagů je ze syntetické tkaniny nebo z umělé kůže. Umělá kůže se snadno otírá, ale bývá těžší. Syntetická tkanina je lehčí a po sundání z vozíku rychle schne. U nepromokavých bagů hledejte svařované nebo zalepené švy a zipy s krycí lištou. Obyčejný zip na bagu z běžné tkaniny nezabrání pronikání vody při delším dešti, takže hole a rukavice pak zůstanou mokré. Dno vyztužené plastem chrání před hrubým povrchem a před vlhkostí z trávy.</p>'
          '<h2>Výběr podle způsobu hry</h2>'
          '<ul><li><strong>Chodíte hřiště pěšky bez vozíku:</strong> volte lehký stojánkový bag s polstrovanými popruhy.</li>'
          '<li><strong>Táhnete vozík:</strong> hledejte bag na vozík s plochým dnem, který sedí na vaši konzoli.</li>'
          '<li><strong>Hrajete i v dešti:</strong> zvolte nepromokavý model nebo si vezměte kryt.</li>'
          '<li><strong>Cestujete s holemi:</strong> pořiďte polstrovaný cestovní obal nebo kryt na bag.</li>'
          '<li><strong>Vybavujete dítě:</strong> dětský bag podle věku, ne bag pro dospělého, do kterého dítě doroste.</li></ul>'
          '<h2>Cestování s holemi</h2>'
          '<p>Přeprava golfových holí v letadle má svá pravidla, která určuje každý dopravce zvlášť. Obecně platí, že golfový bag se odbavuje jako speciální zavazadlo, často za příplatek, a nejlépe v pevném nebo polstrovaném obalu. Hole v obalu srovnejte tak, aby hlavy držely pohromadě a dříky se neohýbaly o stěnu. Před odjezdem zjistěte podmínky dopravce, abyste je nezjišťovali u přepážky. Pokud jezdíte pouze autem, postačí pouhý kryt, který ochrání bag před špínou a hole před otlučením.</p>'
          '<h2>Péče o bag a vozík</h2>'
          '<p>Po každém kole vytřete bag vlhkým hadříkem a nechte ho se sundanými kryty vyschnout, hlavně pokud jste hráli v mokru. Zipy občas ošetřete vhodným mazivem, aby se nezadrhávaly o písek. Vozík očistěte od trávy a hlíny, zkontrolujte osy kol a po sezóně vyčistěte klouby od prachu. Baterii elektrického vozíku skladujte podle pokynů výrobce, obvykle částečně nabitou a na suchém místě, aby neztrácela kapacitu.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Nabídka je rozdělená mezi stojánkové bagy a modely na vozík, nepromokavé varianty, dětské velikosti, ruční vozíky se dvěma a třemi kolečky a elektrické vozíky, doplněné konzolami, popruhy, síťkami a cestovními kryty. Největší zastoupení má značka Inesis, následuje SUN Mountain a několik hráčských značek jako Callaway, Titleist nebo Taylormade. Ve skupině jsou i modely na přání s výrazným barevným provedením, takže si dokážete vybrat i podle vzhledu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě bagu na vozík bez ověření, zda se hodí k vaší konzoli.</li>'
          '<li>Výběr těžkého stojánkového bagu s mnoha kapsami, které pak nikdy nezaplníte.</li>'
          '<li>Podcenění baterie elektrického vozíku a následný nedostatek energie na posledních jamkách.</li>'
          '<li>Vybavení dítěte bagem pro dospělé, ze kterého hole nejdou vytáhnout.</li>'
          '<li>Zapomenutí na nepromokavý kryt, když hrajete celoročně.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka nic neprodává, jen porovnává nabídky obchodů, takže objednávku dokončíte u prodejce. Porovnávejte nabídky téhož modelu, ověřte barvu a velikost v popisu a u vozíků zkontrolujte, zda je v balení nabíječka a baterie. Další pomůcky na hřišti najdete v kategoriích <a href="/golf/">golf</a> a <a href="/sportovni-tasky/">sportovní tašky</a>, pro volnočasové vybavení pak v oddílu <a href="/volny-cas/">volný čas</a>.</p>',
    faq=[
        ('Jaký bag zvolit, když chodím hřiště pěšky?', 'Lehký stojánkový bag s polstrovanými dvojitými popruhy, které rozloží zátěž na obě ramena. Důležité je, aby se nožky samy rozevíraly a bag stál stabilně i na svahu.'),
        ('Kolik přihrádek na hole bag potřebuje?', 'Podle pravidel golfu smíte nosit nejvýše čtrnáct holí, takže víc přihrádek nepotřebujete. Čtyřcestné dělení stačí na základní sadu, čtrnáctidílné lépe chrání dříky.'),
        ('Jaký je rozdíl mezi bagem na vozík a stojánkovým bagem?', 'Bag na vozík je plošší a širší, s úchyty pro popruhy vozíku, a nemusí být tak lehký. Stojánkový bag má nožky a ramenní popruhy, ale nese se na zádech.'),
        ('Dvě, nebo tři kolečka u ručního vozíku?', 'Dvoukolečkový je jednodušší a stačí na rovnější hřiště. Tříkolečkový se lépe řídí a na svahu se méně převrací, takže se hodí do zvlněného terénu.'),
        ('Na co dát pozor při koupi elektrického vozíku?', 'Hlavně na kapacitu a odnímatelnost baterie, brzdu na svahu, ovládání rychlosti a dostupnost náhradní baterie i nabíječky. Baterie je nejtěžší díl, který budete zvedat do auta.'),
        ('Jak velký bag potřebuje dítě?', 'Dětské bagy se dělí podle věkových skupin, například 8 až 10 a 11 až 13 let. Bag má sedět proporčně ke krátkým holím a být dost lehký, aby ho dítě uneslo samo.'),
        ('Pasuje každý bag na každý vozík?', 'Ne vždy. Liší se tvar spodního lůžka a způsob uchycení popruhů, proto před koupí zkontrolujte, zda je bag určený pro váš typ vozíku nebo zda má univerzální dno.'),
        ('Jak převážet golfový bag v letadle?', 'Většinou jako speciální zavazadlo v polstrovaném nebo pevném obalu. Podmínky určuje dopravce, proto je ověřte předem a hole v obalu uspořádejte tak, aby se nepoškodily dříky.'),
        ('Je nepromokavý bag opravdu potřeba?', 'Pokud hrajete jen za sucha, ne. Kdo chodí na hřiště celoročně, ocení svařované švy a vodotěsné zipy, protože vlhké rukojeti a mokrý bag jsou nepříjemné i pro hole.'),
        ('Jak pečovat o golfový vozík po sezóně?', 'Očistěte rám a kola od hlíny, zkontrolujte klouby a osy a uložte ho na suchém místě. U elektrického vozíku postupujte podle výrobce a baterii skladujte částečně nabitou.'),
    ],
)

# ------------------------------------------------------------------ meditace
NEW['meditace'] = dict(long=True,
    title='Meditace: polštáře zafu, bolstery a podložky',
    desc='Meditační polštáře zafu, jógové bolstery a podložky na sezení. Jak vybrat výšku, náplň a potah, pečovat o ně a porovnat nabídky českých obchodů.',
    intro='<p>Pro delší sezení na zemi potřebuje tělo podpůrnou pomůcku, která zvedne pánev nad kolena a umožní zachovat přirozené prohnutí zad. Sporteka porovnává nabídky českých obchodů u meditačních polštářů zafu, kulatých i válcových bolsterů, polštářků s pohankovými slupkami a kulatých podložek na sezení. U každé nabídky sledujte výšku, náplň a to, pro jaký styl sezení se polštář hodí.</p>'
          '<p>V kategorii najdete značky ' + B(('phoenix', 'Phoenix'), ('yogi-yogini', 'Yogi &amp; Yogini'), ('bodhi', 'Bodhi'), ('om', 'OM'), ('manduka', 'Manduka'), ('xtrexo', 'Xtrexo'), ('kimjaly', 'Kimjaly'), ('myga', 'Myga'), ('kurma', 'Kurma'), ('casall', 'Casall')) +
          '. K sezení se hodí i <a href="/joga-a-podlozky/">jóga a podložky</a>, <a href="/jogove-pomucky/">jógové pomůcky</a>, <a href="/joga-a-pilates/">jóga a pilates</a> a <a href="/pilates-pomucky/">pilates pomůcky</a>.</p>',
    guide='<h2>K čemu meditační pomůcky slouží</h2>'
          '<p>Při sezení se zkříženýma nohama se pánev bez opory snadno sklopí dozadu a bederní páteř se zakulatí. Polštář pod sedací kosti zvedne pánev, kolena klesnou k zemi a záda zůstanou vzpřímená bez velkého svalového úsilí. Správně zvolená pomůcka nezaručí pohodlí navždy, ale může zpříjemnit delší sezení a odlehčit kyčlím, kolenům a zádům. Kategorie nepatří jen meditujícím: stejné pomůcky využívají lidé v józe, při dechových cvičeních a při protahování.</p>'
          '<h2>Jaké typy pomůcek existují</h2>'
          + T(['Pomůcka', 'Tvar a náplň', 'Využití'], [
              ['Zafu', 'kulatý nebo kopulovitý polštář, obvykle pohanka nebo kapok', 'klasické sezení v lotosu, půllotosu nebo turecky'],
              ['Zabuton', 'plochá podložka pod zafu', 'ochrana kolen a kotníků na tvrdé podlaze'],
              ['Bolster', 'válec nebo plochý polštář vyšší a delší', 'restorativní jóga, podpora zad a kolen'],
              ['Podložka na sezení', 'kulatá nízká podložka', 'krátké sezení a protahování'],
              ['Sedák s opěrkou', 'nízká stolička nebo skládací sedák', 'sezení na klečení nebo s podepřením zad'],
           ]) +
          '<h2>Zafu: tvar a výška</h2>'
          '<p>Zafu je tradiční japonský polštář, v kategorii se objevuje pod různými názvy včetně modelů s lotosovým motivem. Kulatý tvar umožňuje změnit polohu sezení a hodí se pro lotos, půllotos nebo sezení v tureckém stylu. Výška polštáře by měla odpovídat pružnosti kyčlů: čím tužší kyčle, tím vyšší polštář je potřeba, aby kolena klesla. Příliš vysoký polštář naopak nepříjemně tlačí na stehna a způsobuje, že se tělo kymácí. Pro začátek volte střední výšku a podle potřeby nastavte množství náplně.</p>'
          '<h2>Náplň: pohanka, kapok, pěna</h2>'
          '<ul><li><strong>Pohankové slupky:</strong> přizpůsobí se tělu a drží tvar, lze je přesypat a upravit výšku, ale šustí a jsou těžší.</li>'
          '<li><strong>Kapok:</strong> přírodní rostlinné vlákno, měkčí a lehčí, s časem se však stlačuje a vyžaduje občasné načechrání.</li>'
          '<li><strong>Pěna nebo vata:</strong> pružná a tichá, ale nelze ji nastavit a časem ztrácí tvar.</li></ul>'
          '<p>Pohanka je nejoblíbenější, protože výšku určíte sami: stačí otevřít zip a část slupek odebrat nebo přidat. Pokud má někdo alergii na pohanku, hledejte alternativu s jinou náplní.</p>'
          '<h2>Potah a zip</h2>'
          '<p>Bavlněný potah dýchá a příjemně se dotýká kůže, organická bavlna je navíc šetrnější k pokožce. Pevné šití a boční držadlo pomáhají při přenášení. Zip by měl být snadno přístupný, aby šla náplň upravit a potah sundat k praní. Levnější kusy mívají potah z polyesteru, který je odolný, ale méně příjemný při pocení.</p>'
          '<h2>Bolster: kdy sáhnout po válci</h2>'
          '<p>Bolster je podlouhlý polštář, v kategorii existuje jako válcový, plochý i kulatý. Využívá se v restorativní józe: podložíte jím záda v záklonu, kolena v leže nebo hrudník v předklonu. Pro meditaci v sedě se používá méně, zato může posloužit při ležení, když sezení z nějakého důvodu nejde. Při výběru sledujte rozměr a pevnost náplně. Příliš tvrdý válec tlačí, příliš měkký sjede, když se na něm opíráte.</p>'
          '<h3>Pohankový bolster nebo bavlněný válec</h3>'
          '<p>Pohankový bolster se přizpůsobí tělu a drží tvar, ale je těžší a při pohybu zvuk slupek vadí citlivým. Bavlněná výplň je tišší a lehčí, ale hůř drží výšku. Rozhodněte se podle toho, zda bolster budete používat dlouhodobě v klidu, nebo ho budete často přenášet.</p>'
          '<h2>Výběr podle polohy a pohyblivosti</h2>'
          '<ul><li><strong>Pružné kyčle, začátečník:</strong> nižší zafu nebo kulatá podložka.</li>'
          '<li><strong>Tužší kyčle:</strong> vyšší polštář, případně zabuton pod kolena.</li>'
          '<li><strong>Problémy s koleny:</strong> sezení na vyšším polštáři nebo na lavičce, aby kolena nebyla zatížená.</li>'
          '<li><strong>Klečení:</strong> sedací lavička nebo bolster mezi lýtka a stehna.</li>'
          '<li><strong>Cestování:</strong> lehčí složitelná podložka nebo polštář, jehož náplň lze vysypat.</li></ul>'
          '<h2>Jak sedět, aby polštář pomáhal</h2>'
          '<p>Usaďte se na přední polovinu polštáře, ne doprostřed, aby se pánev mírně sklopila dopředu. Kolena by měla spočívat na podložce, nebo alespoň být těsně nad ní. Pokud vám nad podložkou visí, přidejte pod ně složenou deku nebo zabuton. Bedra jsou přirozeně prohnutá, ramena uvolněná a brada lehce přitažená. Po deseti až dvaceti minutách se může objevit brnění v nohou, což je běžné. Změňte polohu nohou a pokračujte, bolest v kloubu je ale signál přestat.</p>'
          '<h2>Pomůcky do mimořádných situací</h2>'
          '<p>Někdo meditaci provozuje na židli, jiný vleže. V takovém případě pomůže tvrdší pohankový bolster pod kolena, aby se odlehčily záda, nebo tenký polštářek pod hlavu. Dechová cvičení v leže zvládnete i bez speciálních pomůcek, ale bolster zlepšuje komfort a zabrání tlaku v dolní části zad.</p>'
          '<h2>Péče o polštáře</h2>'
          '<p>Potah perte podle štítku, obvykle při nízké teplotě, aby se bavlna nesrazila. Náplň z pohanky nevystavujte vlhkosti, jinak může zplesnivět. Vysypanou pohanku nechte vyschnout na vzduchu a před vracením vyvětrejte. Kapok občas načechrejte a vyvětrejte na slunci, ale ne na přímém a dlouhém horku. Polštář skladujte na suchém místě mimo dosah drobných škůdců.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Většinu nabídky tvoří meditační polštáře zafu s pohankovou náplní a jógové bolstery od značek Phoenix, Yogi &amp; Yogini, Bodhi nebo OM. Doplňují je kulaté podložky, například od značek Manduka nebo Myga, pohankové válce a polštáře s motivem čaker. Najdete tu i modely z organické bavlny a kombinace s jógovou podložkou, takže pořídíte sadu najednou.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš vysoký polštář, na kterém tělo nemá stabilitu.</li>'
          '<li>Zafu bez možnosti upravit náplň, když se výška nedá dodatečně změnit.</li>'
          '<li>Ignorování potahu, který se nedá sundat a vyprat.</li>'
          '<li>Podcenění zabutonu, když sedíte na tvrdé podlaze.</li>'
          '<li>Nákup bolsteru, ačkoli hledáte klasický sedák.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka sama neprodává a neřeší doručení, pouze porovnává nabídky obchodů. U polštářů porovnávejte rozměry, druh náplně a barvu, protože stejný název může mít několik variant. Širší výběr cvičebních pomůcek najdete v oddílu <a href="/fitness/">fitness</a> a mezi <a href="/fitness-pomucky/">fitness pomůckami</a>.</p>',
    faq=[
        ('Jak vysoký má být meditační polštář?', 'Takový, aby kolena klesla k podložce nebo ji lehce dotýkala. Při tužších kyčlích volte vyšší polštář, při pružných nižší, a nejlépe model s nastavitelnou náplní.'),
        ('Čím se liší zafu od bolsteru?', 'Zafu je kulatý polštář určený k sezení, bolster je podlouhlý a využívá se hlavně v restorativní józe jako podpora pro záda, hrudník nebo kolena.'),
        ('Je lepší pohanka, nebo kapok?', 'Pohanka drží tvar a dá se upravit množství, ale šustí a je těžší. Kapok je měkčí a lehčí, časem se však stlačuje a vyžaduje načechrání.'),
        ('Mám sedět na celém polštáři?', 'Lépe jen na jeho přední části. Pánev se tak mírně sklopí dopředu, bedra se přirozeně prohnou a záda zůstanou vzpřímená bez námahy.'),
        ('Co dělat, když mi při sezení brní nohy?', 'Brnění je při delším sezení běžné, změňte polohu nohou nebo zvyšte polštář. Pokud pociťujete bolest v kloubech, sezení přerušte a v případě potíží se poraďte s odborníkem.'),
        ('Dá se potah prát v pračce?', 'U většiny polštářů je potah snímatelný a pere se při nízké teplotě. Před praním vysypte náplň a vždy zkontrolujte štítek výrobce.'),
        ('Co je zabuton a potřebuji ho?', 'Zabuton je plochá podložka pod zafu. Chrání kolena a kotníky před tvrdou podlahou, takže se hodí hlavně při sezení na dřevě nebo dlažbě.'),
        ('Mohu na polštáři sedět i při jógových pozicích?', 'Ano, polštáře a bolstery se v józe používají jako opora v sedu i v leže. Pro dynamickou jógu se však hodí spíš podložka než vysoký polštář.'),
        ('Je pohanka vhodná pro alergiky?', 'Pohankové slupky mohou někomu vadit. Alergici by měli zvolit jinou náplň, například bavlnu, a při pochybnostech se poradit s lékařem.'),
        ('Jak skladovat pohankový polštář?', 'Na suchém, větraném místě, mimo vlhkost a dosah škůdců. Vlhká pohanka může zplesnivět, proto ji po vyprání nebo vysypání nechte důkladně vyschnout.'),
    ],
)

# ------------------------------------------------------------------ dekove-spacaky
NEW['dekove-spacaky'] = dict(long=True,
    title='Dekové spacáky: rozměry, zip, teplota a výběr',
    desc='Dekové spacáky a spací pytle pro kemping, chatu a auto. Jak vybrat rozměr, teplotu, zip a podhlavník a porovnat nabídky českých obchodů.',
    intro='<p>Dekový spacák se dá celý rozepnout a rozložit jako přikrývka, takže nevyžaduje zalézání do úzkého pytle. Je pohodlný pro neklidné spáče, vhodný na kemping, chatu, festival i spaní v autě. Sporteka porovnává nabídky českých obchodů u dekových spacáků pro léto i třísezónní použití, s levým i pravým zipem, s podhlavníkem a v kombinacích s karimatkou. U každé nabídky sledujte, pro jakou teplotu a jaký rozměr je spacák určený.</p>'
          '<p>V nabídce najdete značky ' + B(('skandika', 'Skandika'), ('husky', 'Husky'), ('cattara', 'Cattara'), ('crossroad', 'Crossroad'), ('progarden', 'Progarden'), ('trimm', 'Trimm'), ('kubisport', 'Kubisport'), ('pinguin', 'Pinguin'), ('hannah', 'Hannah')) +
          '. Ke spaní pasují <a href="/karimatky-a-matrace/">karimatky a matrace</a>, <a href="/stany/">stany</a>, <a href="/kemping/">kemping</a>, <a href="/kempingovy-nabytek/">kempingový nábytek</a> a <a href="/vlozky-do-spacaku/">vložky do spacáků</a>.</p>',
    guide='<h2>Co dekový spacák vlastně je</h2>'
          '<p>Základem je obdélníkový střih bez zúžení u nohou, na rozdíl od mumie, která kopíruje tělo. Díky tomu se v něm dá otáčet, pokrčit kolena a ráno ho po rozepnutí zipu rozložit na sušení nebo použít jako deku. Nevýhodou je větší vnitřní objem, který se musí prohřát, takže při stejné izolaci bývá méně teplý než mumie. Dekový spacák je proto stavěný pro pohodlí a nízkou i střední zátěž, ne pro nošení v batohu.</p>'
          '<h2>Teplotní rozsah a roční období</h2>'
          '<p>Na štítku se uvádějí různé teploty, nejčastěji komfortní a extrémní. Komfortní teplota udává, kdy by měla typická žena spát v klidu příjemně, a podle ní vybírejte. Extrémní teplota je hranice, od které hrozí podchlazení, a není určena pro běžné spaní. Teplota samotná také závisí na karimatce, oblečení, větru a na tom, jak citlivě vnímáte chlad.</p>'
          + T(['Označení', 'Obvyklé použití', 'Poznámka'], [
              ['Letní, kolem 10 °C', 'teplé noci, chaty, festivaly', 'lehká výplň, často bez izolace u zad'],
              ['Přechodový, kolem 0 až 5 °C', 'jaro, podzim, kemping', 'univerzální volba pro auto a stan'],
              ['Třísezónní, pod nulou', 'chladné noci, podzim', 'silnější výplň, vyšší hmotnost'],
              ['Hybrid mumie a deka', 'zasouvání kapuce, zúžení u nohou', 'kompromis mezi teplem a prostorem'],
           ]) +
          '<h2>Rozměry a délka</h2>'
          '<p>Dekové spacáky se vyrábějí obvykle v délce kolem 190 až 220 centimetrů a v šířce 70 až 90 centimetrů. Délka by měla přesahovat výšku o deset až dvacet centimetrů, aby se na konci nestlačovala izolace. Příliš velký spacák se zbytečně chladí, příliš krátký tlačí na chodidla. Některé modely nabízejí prodlouženou délku nebo vysokou verzi pro vyšší postavy. Pro děti existují samostatné <a href="/detske-spacaky/">dětské spacáky</a>, které lépe drží teplo.</p>'
          '<h2>Zip: levý, pravý a spojitelné spacáky</h2>'
          '<p>Zip se označuje podle strany, na které je při ležení na zádech. Levý a pravý zip téže řady se dají spojit do dvojitého spacáku pro dva, ale jen pokud mají kompatibilní zipy. Spojování funguje jen u výrobců, kteří to výslovně uvádějí. Praktický je zip, který nezadrhává látku, a krycí lišta proti průvanu. Jednosměrný zip stačí, dvousměrný umožní odvětrat nohy.</p>'
          '<h2>Výplň a povrchový materiál</h2>'
          '<p>Většina dekových spacáků má syntetickou výplň z dutého vlákna. Hmotnost výplně se udává v gramech na metr čtvereční a čím vyšší číslo, tím teplejší spacák. Syntetika snáší vlhko a rychle schne, což oceníte ve stanu na zahradě i v mokru. Obal bývá z polyesteru, někdy z bavlny: bavlna je příjemnější na kůži, ale těžší a pomaleji schne. Prošívání zabraňuje přesunu výplně a vytváření studených míst.</p>'
          '<h3>Podhlavník a kapuce</h3>'
          '<p>Podhlavník je zvýšená část, která drží hlavu na vhodné úrovni, případně kapsa, do které zasunete složené oblečení nebo polštář. V levnějších spacácích bývá jen prošitá nebo lehce vycpaná, v dražších větší s lepší výplní. Kapuce je u dekových modelů spíše výjimkou, najdete ji u hybridů s mumií. V chladné noci pomáhá čepice a kapuce mikiny.</p>'
          '<h2>Spaní v autě, chatě a kempu</h2>'
          '<p>V autě se hodí menší rozměr a rozepínací zip, aby se spacák vešel na zadní sedadla nebo do kufru. Na chatě pomůže vyšší hmotnost výplně, protože nevytopený objekt může být chladný. Při kempování pod stanem ocení hlavně rozepnutí a vyvětrání po vlhké noci. Dekový spacák zabere po sbalení víc místa než mumie, počítejte s velkou taškou nebo kompresním popruhem.</p>'
          '<h2>Karimatka a izolace od země</h2>'
          '<p>Větší část tepla odchází do země, takže výběr spacáku nedává smysl bez ohledu na podložku. Samonafukovací matrace nebo kvalitní pěnová karimatka zvyšují komfort a snižují pocit chladu zespodu. V kategorii se objevují i sety spacáku a karimatky, které se hodí na festival. Samotná výplň pod tělem se totiž stlačí a izoluje jen minimálně.</p>'
          '<h2>Péče o spacák</h2>'
          '<p>Skladujte ho volně, ve velkém bavlněném pytli nebo na polici, ne stlačený v sáčku po celou sezónu, protože výplň se trvale stlačí a hůř izoluje. Perte jen podle štítku, obvykle při nízké teplotě šetrným prostředkem, a pečlivě vysušte, nejlépe rozprostřený na vzduchu. Před uložením ho vyvětrejte. Zip čistěte od písku a jehličí, aby se nezadíral. Skvrny odstraňte lokálně vlhkým hadříkem, pokud je to možné, bez zbytečného praní.</p>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Chata a letní noci:</strong> lehký model kolem 10 °C s bavlněným podšitím.</li>'
          '<li><strong>Kemping jaro až podzim:</strong> přechodový spacák a dobrá karimatka.</li>'
          '<li><strong>Spaní ve dvou:</strong> pár spacáků se zipem levý a pravý od stejného výrobce.</li>'
          '<li><strong>Festival:</strong> set spacáku a karimatky, který rychle schne.</li>'
          '<li><strong>Auto a výlety:</strong> kompaktní model s podhlavníkem a taškou k přenášení.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Nabídka obsahuje letní a třísezónní dekové spacáky s levým i pravým zipem, modely s podhlavníkem, set s karimatkou a maskáčové provedení od značek jako Mil-Tec nebo Sedco. Největší zastoupení mají Skandika a Husky, dále Kubisport, Cattara, Crossroad a Progarden. Najdete i kombinované mumie s přechodem na deku, které zúžením u nohou lépe drží teplo.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Spoléhání na extrémní teplotu místo komfortní.</li>'
          '<li>Kupování spacáku na vysokou horu, když je stavěný pro auto a chatu.</li>'
          '<li>Vynechání karimatky a pak stížnost na chlad.</li>'
          '<li>Spojování spacáků, které k tomu nejsou určené, a rozdílné délky zipů.</li>'
          '<li>Skladování ve stlačeném sáčku celé měsíce.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka jen porovnává nabídky obchodů, takže koupě probíhá u prodejce. Porovnávejte rozměry, teplotu a typ zipu, protože stejný model bývá ve více verzích. Na zimu hledejte v oddílu <a href="/spaci-pytle/">spacích pytlů</a>, na lehčí výlety do <a href="/outdoor/">outdooru</a> a mezi <a href="/stanove-doplnky/">stanové doplňky</a>.</p>',
    faq=[
        ('Pro koho je dekový spacák vhodný?', 'Pro kempování u auta, chatu, festival a spaní v autě, kde záleží na pohodlí a nevadí vyšší hmotnost a větší objem po sbalení.'),
        ('Dají se dva dekové spacáky spojit?', 'Ano, pokud jsou ze stejné řady, jeden s levým a druhý s pravým zipem a stejné délky zipu. Výrobce to musí výslovně uvádět.'),
        ('Je dekový spacák vhodný do mrazu?', 'Spíše ne. Větší vnitřní objem se hůř vyhřívá, takže na mráz je lepší zúžená mumie s kapucí nebo třísezónní model s vyšší gramáží výplně.'),
        ('Jakou teplotu na štítku sledovat?', 'Komfortní teplotu, při které by průměrný člověk měl spát příjemně. Extrémní teplota je určená pro krajní situace a ke každodennímu výběru se nehodí.'),
        ('Jaký rozměr spacáku vybrat?', 'Délka by měla přesahovat vaši výšku o 10 až 20 cm, šířka se pohybuje kolem 70 až 90 cm. Příliš velký spacák se zbytečně chladí.'),
        ('Dá se dekový spacák prát v pračce?', 'U většiny syntetických spacáků ano, při nízké teplotě a podle štítku. Poté důkladně vysušte, aby se výplň nezlepila a nezpůsobila zápach.'),
        ('Jak skladovat spacák mezi sezónami?', 'Volně v prostorném pytli nebo na polici, ne stlačený. Dlouhé stlačení výplň trvale zhutní a spacák pak hůř izoluje.'),
        ('Je potřeba karimatka, když mám silný spacák?', 'Ano. Výplň pod tělem se stlačí a téměř neizoluje, takže chlad od země prostupuje. Samonafukovací matrace nebo pěnová karimatka rozdíl výrazně zmenší.'),
        ('Čím se dekový spacák liší od mumie?', 'Má obdélníkový střih a je prostornější, zato hůř drží teplo a je těžší. Mumie kopíruje tělo, je teplejší a lépe se nosí v batohu.'),
        ('Jak poznat kvalitní zip?', 'Má se plynule posouvat, nezachytávat látku a mít krycí lištu proti průvanu. Dvousměrný zip umožní větrat nohy, jednosměrný ale pro běžné použití stačí.'),
    ],
)

# ------------------------------------------------------------------ triatlon
NEW['triatlon'] = dict(long=True,
    title='Triatlon: kombinézy, neopreny, tretry a přilby',
    desc='Triatlonové kombinézy, neopreny, plavecké potřeby, tretry a přilby. Jak vybrat vybavení pro plavání, kolo i běh a porovnat nabídky obchodů.',
    intro='<p>Triatlon spojuje plavání, kolo a běh bez přerušení, takže vybavení musí fungovat ve vodě, na silnici i při běhu. Sporteka porovnává nabídky českých obchodů u triatlonových kombinéz a obleků, neoprenů, plaveckých čepic, bójek, triatlonových tretr, přileb a doplňků pro přechodovou zónu. U každého produktu vidíte, pro jaký závod nebo úroveň je určený.</p>'
          '<p>V nabídce najdete značky ' + B(('van-rysel', 'VAN Rysel'), ('zone3', 'Zone3'), ('2xu', '2XU'), ('huub', 'Huub'), ('mako', 'Mako'), ('keada-sports', 'Keada Sports'), ('fizik', 'Fizik'), ('aqua-sphere', 'Aqua Sphere'), ('mad-wave', 'Mad Wave'), ('arena', 'Arena')) +
          '. Související vybavení najdete v <a href="/neopreny/">neoprenech</a>, <a href="/plavecke-bryle/">plaveckých brýlích</a>, <a href="/plavecke-cepice/">plaveckých čepicích</a>, <a href="/cyklisticke-helmy/">cyklistických helmách</a> a <a href="/silnicni-bezecke-boty/">silničních běžeckých botách</a>.</p>',
    guide='<h2>Z čeho se triatlonová výbava skládá</h2>'
          '<p>Na krátkém závodě vystačíte s malým množstvím věcí, na delších tratích přibývá vybavení, které řeší výživu, regeneraci a přechody. Základ tvoří kombinéza nebo dvojice oblečení pro všechny tři disciplíny, doplněná o neopren, plavecké brýle, čepici, kolo s helmou a běžeckou obuv.</p>'
          + T(['Část výbavy', 'K čemu slouží', 'Poznámka'], [
              ['Triatlonová kombinéza', 'jedno oblečení na všechny disciplíny', 's vložkou pod sedlo nebo bez ní'],
              ['Neopren', 'nadnášení a izolace ve vodě', 'jen tam, kde je dovolený'],
              ['Plavecká čepice a brýle', 'viditelnost a výhled', 'více brýlí pro různé světlo'],
              ['Přilba', 'povinná na kole', 'silniční nebo časovkářská'],
              ['Tretry', 'přenos síly na pedály', 'rychlé obouvání v přechodu'],
              ['Bójka a doplňky', 'viditelnost při plavání na volné vodě', 'plus vak na věci'],
           ]) +
          '<h2>Triatlonová kombinéza a dvoudílný set</h2>'
          '<p>Kombinéza, česky též trisuit, se obléká na začátku a nosí se přes plavání, kolo i běh. Má tenkou vložku pod sedlo, která na kole tlumí tlak, ale při běhu nebrání pohybu a po plavání rychle schne. Existují jednodílné kombinézy, dvoudílné sety s tričkem a kraťasy a verze bez rukávů nebo s rukávy. Bezrukávová varianta lépe odvětrává a lépe se kombinuje s neoprenem. Rukávy dávají ochranu před sluncem a mírně zlepšují aerodynamiku.</p>'
          '<h3>Velikost a střih</h3>'
          '<p>Kombinéza má sedět těsně, ale nesmí omezovat dýchání a pohyb ramen. Příliš volný střih nasákne vodou a při jízdě vlaje. Vložku ověřte při sezení v pozici na kole: ať netlačí a nevyčnívá. Pro děti existují kombinézy na krátkou trať, které se vyrábějí podle věku a výšky.</p>'
          '<h2>Neopren: kdy, jaký a jak velký</h2>'
          '<p>Neopren v triatlonu zvyšuje plavání díky vztlaku a chrání před chladem. Použít se smí obvykle jen do určité teploty vody, kterou stanoví pravidla závodu, proto vždy zkontrolujte propozice. Triatlonové neopreny mají tenčí a pružnější materiál na ramenou než potápěčské, aby neomezovaly záběr. Existují modely s rukávy i bez, dámské a pánské střihy a verze s vyšším nadnášením, které pomáhají plavcům se slabším polohováním těla. Velikost volte podle výšky a hmotnosti v tabulce výrobce a zkuste se zhluboka nadechnout a posunout ramena.</p>'
          '<h3>Oblékání a sundávání</h3>'
          '<p>Na kůži lze použít speciální lubrikant nebo pěnu, která usnadní oblékání i rychlé svlečení v přechodové zóně. Oblékejte neopren opatrně, natahujte ho pomalu od kotníků vzhůru a dávejte pozor, aby ho nehty neprotrhly. V přechodu ho stáhněte od ramen přes boky a nohy sundejte při chůzi ke kolu.</p>'
          '<h2>Plavecké brýle, čepice a bójka</h2>'
          '<p>Při plavání na volné vodě se hodí brýle s větším zorným polem, protože potřebujete vidět bóje a ostatní plavce. Čirá nebo světlá skla se hodí do šera, zrcadlová a tmavá na ostré slunce. Silikonová čepice drží brýle a zlepšuje viditelnost, pokud je výrazně barevná. Bójka se táhne za pasem, pomáhá s viditelností pro lodě a poskytuje oporu v případě únavy. Mnoho modelů má vak, do kterého se dají uložit klíče a mobil.</p>'
          '<h2>Přilba na kole</h2>'
          '<p>Přilba je v triatlonu povinná, před startem se kontrola provádí v přechodové zóně. Silniční helma je lehká a dobře větraná, časovkářská má protáhlý tvar zlepšující aerodynamiku, ale hůř chladí a vyžaduje pozici na speciálním nástavci. Sledujte nastavení velikosti a upevnění pásků. V nabídce se objevují modely s technologií MIPS a modely s protáhlým zadním dílem, tedy aero verze.</p>'
          '<h2>Tretry a přechodová zóna</h2>'
          '<p>Triatlonové tretry mají obvykle jednoduchý systém zapínání, jeden velký pásek nebo kolečko, a drenážní otvory, aby voda odtékala. Často mají vysoký jazyk nebo zadní poutko, které usnadňuje nazouvání. Karbonová podrážka přenáší sílu efektivněji, ale je tužší a pro chůzi po zemi méně příjemná. Některé závodníci nechají tretry zapnuté na pedálech a obouvají se až za pochodu, což vyžaduje trénink.</p>'
          '<h2>Výběr podle délky závodu</h2>'
          '<ul><li><strong>Sprint a krátká trať:</strong> jednodílná kombinéza, jednoduchý neopren, silniční helma.</li>'
          '<li><strong>Olympijská trať:</strong> komfortnější kombinéza s lepší vložkou a neopren s dobrým nadnášením.</li>'
          '<li><strong>Delší tratě:</strong> kombinéza s kapsami na gely, pohodlná vložka, případně časovkářská helma.</li>'
          '<li><strong>Začátečník:</strong> půjčený neopren, kombinéza nebo cyklistické kraťasy a běžecké tričko.</li>'
          '<li><strong>Děti a mládež:</strong> dětská kombinéza na krátkou trať a neopren podle výšky.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie obsahuje pánské i dámské triatlonové obleky s rukávy i bez rukávů, kombinézy na krátkou trať, dětskou verzi, neopreny od značek Zone3, Orca nebo Mako, tretry Fizik a Tri-Sixty, helmy včetně časovkářských a doplňky jako silikonové čepice, bójky a sprchové gely proti chloru. Největší zastoupení má VAN Rysel a Keada Sports.</p>'
          '<h2>Péče o výbavu</h2>'
          '<p>Neopren po každém použití opláchněte sladkou vodou, sušte na tvarovaném ramínku ve stínu a skladujte rozvěšený nebo volně složený. Kombinézu perte při nízké teplotě bez aviváže, která poškozuje elastické vlákno. Brýle a čepici opláchněte a nenechávejte na slunci. Tretry po závodě vysušte a vyjměte vložky, aby nezapáchaly.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě neoprenu bez ověření, že na závodě bude povolený.</li>'
          '<li>Příliš velká kombinéza, která se plní vodou.</li>'
          '<li>Ignorování vložky: dlouhé úseky na kole pak končí nepohodlím.</li>'
          '<li>Nové tretry nebo brýle poprvé až na závodě.</li>'
          '<li>Podcenění přechodové zóny a nácviku obouvání a svlékání.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka sama neprodává, jen porovnává nabídky obchodů. Porovnávejte konkrétní velikost, střih (pánský, dámský, dětský) a barvu, protože stejný název se hodí různě. Další vybavení najdete v oddílech <a href="/vodni-sporty/">vodní sporty</a>, <a href="/beh/">běh</a> a <a href="/cyklistika/">cyklistika</a>.</p>',
    faq=[
        ('Potřebuji na triatlon neopren?', 'Ne vždy. Záleží na teplotě vody a pravidlech závodu, které určí, zda je neopren povolený nebo povinný. Začátečníkovi může stačit i kombinéza.'),
        ('Čím se triatlonový neopren liší od potápěčského?', 'Je tenčí a pružnější v ramenou, aby neomezoval záběr, a často má hladší povrch pro rychlejší svlékání. Potápěčský je určený spíš na izolaci.'),
        ('Co je triatlonová kombinéza a proč ji nosit?', 'Je to jednodílné nebo dvoudílné oblečení s tenkou vložkou, které se nosí přes všechny tři disciplíny. Nemusíte se převlékat a ušetříte čas v přechodu.'),
        ('Jakou velikost kombinézy zvolit?', 'Těsnou, ale takovou, která nebrání dýchání a pohybu ramen. Orientujte se podle tabulky výrobce a vložku ověřte při sezení v pozici na kole.'),
        ('Je přilba v triatlonu povinná?', 'Ano, na kole je obvykle povinná a kontroluje se v přechodové zóně před startem. Musí být správně nastavená a bez poškození.'),
        ('Jak pečovat o neopren?', 'Po použití ho opláchněte sladkou vodou, nechte uschnout ve stínu na širokém ramínku a nevystavujte ho přímému slunci ani teplu. Skladujte volně.'),
        ('Kdy se hodí časovkářská helma?', 'Na delších tratích s časovkářskou pozicí na kole. Je aerodynamičtější, ale hůř větrá, takže pro běžný závod a začátečníka stačí silniční helma.'),
        ('Proč mají triatlonové tretry otvory?', 'Slouží k odtoku vody po plavání, takže se tretry po vodě neplní. Obvykle mají též jednoduché zapínání a poutko pro rychlé obutí.'),
        ('K čemu je plavecká bójka?', 'Táhne se za pasem při plavání na volné vodě, zvyšuje viditelnost pro lodě a poskytuje opěrný bod při únavě. Často slouží i jako vodotěsný vak na drobnosti.'),
        ('Mám vybavení zkoušet před závodem?', 'Ano. Neopren, brýle, tretry i kombinézu vyzkoušejte při tréninku, abyste věděli, kde tře nebo tlačí. Nová věc na závodě bývá častým zdrojem potíží.'),
    ],
)

# ------------------------------------------------------------------ extensions (extra sections appended to the guides)
NEW['golfove-tasky-a-voziky']['guide'] += (
    '<h2>Další kapsy, držáky a drobnosti</h2>'
    '<p>Praktický bag má izolovanou kapsu na nápoje, velkou kapsu na oblečení a menší, často vyztuženou kapsu na cennosti, kterou dosáhnete bez shýbání. Na kapse na míčky záleží méně, než by se zdálo, protože hráč bere na kolo jen pár kusů, ale měkká výstelka chrání například dálkoměr. Držák na deštník by měl být pevný, protože bag s deštníkem je při větru nestabilní. Zkontrolujte i kryty hlav holí, které chrání kovy před otěrem, a pevné uchycení bagu na vozík. Všechny dodatečné součásti zvyšují hmotnost, takže pokud bag nosíte, vybírejte střídmě.</p>')
NEW['meditace']['guide'] += (
    '<h2>Kulatá podložka a sezení na zemi bez polštáře</h2>'
    '<p>Mezi nabídkami najdete i kulaté jógové podložky s motivem mandaly nebo s protiskluzovým povrchem. Hodí se pod polštář, aby neklouzal po hladké podlaze, nebo jako samostatný podklad při krátkém sezení. Kulatý tvar zabere méně místa než klasická obdélníková jógamatka a snadno se vleze do batohu. Na dlouhé sezení ale přidejte polštář, protože tenká vrstva pěny pánev nezvedne. Pokud sedíte na koberci nebo parketách, stačí jemnější podložka, na dlažbě oceníte silnější.</p>'
    '<h2>Zabudování do domácího prostoru</h2>'
    '<p>Meditační kout nepotřebuje velký prostor. Stačí rovná plocha o velikosti jedné jógamatky, klidné místo bez průvanu a pravidelný čas. Polštář a podložku nechte stále na stejném místě, aby se vytvořil zvyk. Dobře funguje i krátká rutina v ranních hodinách nebo večer před spaním. Pokud sdílíte byt, použijte skládací sedák nebo polštář s držadlem a uložte jej do skříně. Při vybavování kouta se může hodit i <a href="/funkcni-trenink/">funkční trénink</a> a <a href="/masazni-pomucky/">masážní pomůcky</a> na uvolnění svalů po sezení.</p>'
    '<h2>Meditace, jóga a regenerace</h2>'
    '<p>Pomůcky v této kategorii se překrývají s jógou a pilates. Bolster podepře záda v restorativních pozicích, polštář poslouží při dechových cvičeních a podložka drží tělo při protahování. Chcete-li kombinovat meditaci s lehkým pohybem, vezměte si k polštáři ještě pěnový válec nebo blok. Pro pohyb na podložce hledejte v kategoriích <a href="/joga-a-podlozky/">jóga a podložky</a> a <a href="/pilates-pomucky/">pilates pomůcky</a>. Nic z toho nenahrazuje lékařskou péči, při bolestech zad či kloubů se poraďte s odborníkem.</p>'
    '<h2>Barva, vzor a materiál podle prostředí</h2>'
    '<p>Tmavý potah je praktický, ale ukáže prach a chlupy. Světlý a přírodní odstín působí klidněji, ale rychleji se špiní. Organická bavlna s certifikací je volba pro citlivou pokožku. Vzory, jako je mandala nebo motiv lotosu, jsou čistě estetická záležitost a funkci nemění. Pokud polštář používáte venku, zvažte vodoodpudivou látku, která snese vlhkou trávu.</p>')
NEW['dekove-spacaky']['guide'] += (
    '<h2>Dekový spacák pro děti a mladé</h2>'
    '<p>Dospělý model na dítě nepasuje: je dlouhý, prostorný a dítě se v něm nezahřeje, protože vlastní teplo nevyplní velký objem. Pro mladší děti hledejte samostatné <a href="/detske-spacaky/">dětské spacáky</a> nebo model s kratší délkou. U vyšších náctiletých má dekový spacák smysl, pokud jezdí na tábory s pevnými stany nebo spí v chatkách. Praktický je spacák, který se při sbalení vejde do menšího batohu a má pevné popruhy.</p>'
    '<h2>Dekový spacák jako přikrývka</h2>'
    '<p>Rozepnutý zcela, funguje jako teplá deka na gauč, do auta při čekání nebo na pláž. Tuto vlastnost oceníte i při běžných vyjížďkách na zahradu, kde se hodí na lehátko nebo pod hlavu. Při použití doma vyberte model s bavlněným podšitím, které je příjemnější na kůži než hladký polyester. Zajímavostí jsou verze s potiskem, které se používají hlavně u dětí a na chatách.</p>'
    '<h2>Praní, sušení a zápach</h2>'
    '<p>Syntetické dekové spacáky se perou při nízké teplotě šetrným prostředkem bez aviváže. Aviváž zalepí vlákna výplně a snižuje izolaci. Po vyprání spacák několikrát protřepte a sušte rozložený, nejlépe venku v polostínu nebo v suchém větraném prostoru. Pokud spacák zapáchá po vlhku, vyvětrejte ho dříve, než ho zabalíte. Pravidelné větrání po každé noci, tedy rozvěšení na slunci na hodinu či dvě, prodlouží jeho životnost.</p>'
    '<h2>Spací pytel, vložka a doplňky</h2>'
    '<p>Pokud je spacák na vaše potřeby mírně chladný, přidejte tenkou <a href="/vlozky-do-spacaku/">vložku</a>, která zvedne teplotu o několik stupňů a chrání spacák před potem. Dalším doplňkem je nafukovací polštářek nebo kompresní pytel. Do kempu se hodí i <a href="/kempingove-doplnky/">kempingové doplňky</a> a <a href="/hamaky/">hamaky</a>, pokud nechcete spát přímo na zemi.</p>')
NEW['triatlon']['intro'] = NEW['triatlon']['intro'].replace('U každého produktu vidíte, pro jaký závod nebo úroveň je určený.', 'U každého produktu vidíte, pro jaký závod nebo úroveň je určený, a můžete rychle porovnat, kolik obchodů daný kus nabízí. Soustředíme se na vybavení pro plavání, kolo a běh, tedy neopreny, plavecké potřeby, cyklistickou a běžeckou výbavu.')
NEW['triatlon']['guide'] += (
    '<h2>Přechodová zóna: pořádek ušetří minuty</h2>'
    '<p>Přechodová zóna se v triatlonu nazývá čtvrtou disciplínou, protože se v ní dá získat i ztratit čas bez jediného kroku navíc. Připravte si ručník, láhev s nápojem, tretry nebo běžecké boty a čepici či vizír tak, aby se nic nehledalo. Na kolo patří přilba zapnutá před sundáním kola ze stojanu a startovní číslo na pásku, který se otáčí vpředu nebo vzadu podle disciplíny. Vše vyzkoušejte při tréninku, ne až na závodě. Při přípravě se hodí <a href="/bezecke-opasky/">běžecké opasky</a> a <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>.</p>'
    '<h2>Výživa a pití během závodu</h2>'
    '<p>Na krátkých tratích stačí voda, na delších řešíte příjem energie na kole, kde se dobře jí a pije. Gely a tyčinky se uloží do kapes kombinézy nebo na rám, bidon patří do držáku. Pití a jídlo při závodě vyzkoušejte předem, protože žaludek citlivě reaguje na novou věc. Obecné informace o výživě a doplňcích nenahradí radu lékaře nebo výživového poradce, zvlášť při zdravotních potížích. Pro ukládání tekutin pomůže <a href="/cyklo-lahve-a-drzaky/">láhev a držák na kolo</a> a <a href="/iontove-napoje/">iontové nápoje</a>.</p>'
    '<h2>Trénink a příprava výbavy</h2>'
    '<p>Kombinované tréninky, tzv. bricky, spojují kolo s navazujícím během a zvykají nohy na těžký start běhu po jízdě. Při těchto trénincích si ověříte, zda vám kombinéza nedře a zda se v tretrách dobře běhá. V bazénu se plavání dá trénovat s pomůckami, na volné vodě je třeba přidat orientaci a plavání v davu. Pomůcky najdete v <a href="/plavecke-pomucky/">plaveckých pomůckách</a>, na vodu pak pomohou <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> pro ochranu před sluncem při tréninku.</p>'
    '<h2>Začínáme s rozumným rozpočtem</h2>'
    '<p>Nejlevnější start je kombinéza, jednoduché plavecké brýle a stávající kolo s přilbou. Neopren si lze na první závod půjčit, tretry nejsou povinné. Až po několika startech poznáte, co vám opravdu chybí, a výbavu doplníte cíleně: lepší kombinézou, vlastním neoprenem a tretrami. Nešetřete na přilbě a na plaveckých brýlích, protože ovlivňují bezpečnost a výhled.</p>')

NEW['golfove-tasky-a-voziky']['guide'] += (
    '<h2>Doplňky na bag a hřiště</h2>'
    '<p>K bagu a vozíku se běžně dokupují <a href="/golfove-hole/">golfové hole</a> ve správné délce, <a href="/golfove-micky/">míčky</a> a <a href="/golfove-doplnky/">doplňky</a> jako rukavice, tee a značky. Do kapes bagu patří také <a href="/golfove-obleceni-a-obuv/">nepromokavé oblečení a obuv</a> pro případ deště a <a href="/lahve-a-termosky/">láhev nebo termoska</a>. Pokud bag nosíte na zádech, přidejte i <a href="/sportovni-tasky/">sportovní tašku</a> na obuv, aby se špína z hřiště nedostala do auta.</p>')
NEW['meditace']['guide'] += (
    '<h2>Jak často a jak dlouho sedět</h2>'
    '<p>Začátečníkovi stačí pět až deset minut denně a délku postupně prodlužovat podle pohodlí těla. Důležitější než délka je pravidelnost a stabilní poloha, ve které nehrozí brnění a bolest. Při delším sezení můžete střídat polohy nohou a polštář nastavit výš. Pokud sedíte na zemi poprvé po dlouhé době, začněte krátce a před sezením protáhněte kyčle a hamstringy, kterým pomohou i jemné <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>')
NEW['dekove-spacaky']['guide'] += (
    '<h2>Jak spacák zabalit a převážet</h2>'
    '<p>Dekový spacák se balí dvojím přeložením nebo smotáním od zadní strany k zipu, aby vzduch unikal ven. Do přepravního vaku ho stlačujte jen mírně, protože silná komprese ničí výplň. Pro přepravu v autě stačí volná taška, kterou položíte na zadní sedadlo nebo do kufru. Při cestě na kolech nebo pěšky je vhodnější model s kompresním pytlem a popruhem na batoh, případně <a href="/outdoor-doplnky/">outdoorový doplněk</a> na přichycení, který zabrání houpání.</p>')
NEW['triatlon']['guide'] += (
    '<h2>Počasí, voda a bezpečnost</h2>'
    '<p>Voda se v otevřených nádržích mění den ode dne, proto sledujte oficiální informace pořadatele. Při plavání v chladu pomůže silikonová čepice, případně druhá přes ni nebo neoprenová čepice, při teplém počasí hrozí přehřátí a vyžaduje častější pití. Při jízdě na kole mějte na paměti viditelnost, v dešti zvažte <a href="/cyklisticke-bundy-a-vesty/">cyklistickou bundu či vestu</a>. Běh po kole začínejte klidně, protože nohy bývají těžké. Na povrch tratě se volí <a href="/trailove-boty/">trailové boty</a> jen u terénních triatlonů.</p>')

NEW['meditace']['guide'] += (
    '<h2>Dárek a výběr pro druhé</h2>'
    '<p>Polštář na sezení je častý dárek pro začínající cvičence. Pokud nevíte, jak vysoký má být, zvolte model s nastavitelnou náplní, který si obdarovaný upraví sám. Neutrální barva a přírodní potah se hodí do každého interiéru a vzor s mandalou či lotosem udělá radost spíš těm, kdo ho dopředu ocení.</p>')
NEW['dekove-spacaky']['guide'] += (
    '<h2>Na co se zaměřit při porovnání nabídek</h2>'
    '<p>Stejný spacák se prodává ve více barvách, rozměrech a s levým či pravým zipem, a každá varianta může mít jinou nabídku obchodů. Před objednávkou proto ověřte, zda je uvedený správný zip a délka. Sledujte také, zda obsahuje obal nebo kompresní vak, jestli je v popisu uvedená gramáž výplně a zda se jedná o samostatný spacák nebo set s karimatkou. Rozdíl mezi obchody bývá nejen v ceně, ale i v dostupnosti a dodání.</p>'
    '<p>Recenze ostatních kupujících pomohou zjistit, zda zip drží i po delší době a zda údaje o teplotě odpovídají skutečnosti. Pokud spacák kupujete na konkrétní akci, myslete na dodací lhůtu a rezervu na vyzkoušení doma v suchu.</p>')
NEW['triatlon']['guide'] += (
    '<h2>Sprchové gely a péče o pokožku</h2>'
    '<p>Po plavání v chlorované vodě pomáhá opláchnutí a šetrný sprchový gel určený pro plavce, který odstraní zápach chloru z pokožky a vlasů. Na dlouhých tratích se hodí ochrana proti otěru v místech tření, například pod pažemi nebo na vnitřní straně stehen, a krém na opalování odolný vodě. U citlivé kůže volte výrobky bez silné parfemace.</p>')
