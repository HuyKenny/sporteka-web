"""sporteka.cz — wave 20b (4. 11. 2026): long texts (>= 1650 words) for snowboardy, cyklo-blatniky, kajaky-a-cluny, tanec-a-gymnastika.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ snowboardy
NEW['snowboardy'] = dict(long=True,
    title='Snowboardy: prkna, délka, profil a tuhost',
    desc='Snowboardy pánské, dámské a dětské od značek Raven, Gravity, Ride, Nitro či Burton. Jak zvolit délku, profil a tuhost a porovnat nabídky obchodů.',
    intro='<p>Snowboard určuje, jak se bude jezdit: jeho délka, šířka, profil a tuhost rozhodují o tom, jak se bude chovat na sněhu zasypaném prachem, na upraveném svahu i v parku. '
          'Kdo vybírá poprvé, většinou řeší, jestli koupit samotné prkno, nebo hotovou sadu s vázáním. Zkušenější jezdec se spíš ptá, jaký tvar a jaký prohyb sedí k jeho stylu. Do výběru promlouvá také váha, velikost boty a terén, na kterém budete trávit nejvíc času.</p>'
          '<p>Na Sportece vedle sebe uvidíte nabídky českých obchodů u prken značek Raven, Gravity, Ride, Nitro, Hatchey, Head, Burton, K2, Capita nebo Bataleon. '
          'Hotové komplety najdete v kategorii <a href="/snowboardove-sety/">snowboardy s vázáním</a>, k nim patří <a href="/snowboardove-boty/">snowboardové boty</a> a <a href="/snowboardova-vazani/">vázání</a>. '
          'Níže je přehled profilů, tvarů, velikostí a péče, aby bylo jasné, co hledat a čemu se při nákupu vyhnout.</p>',
    guide='<h2>Jak snowboard funguje</h2>'
          '<p>Deska je sendvič z dřevěného jádra, vrstev laminátu a spodní skluznice s ocelovými hranami. Jádro určuje živost a pružnost, laminát tuhost a skluznice rychlost i to, jak dobře snese vosk. '
          'Při zatáčení se prkno ohýbá a hrana se zakusuje do sněhu, takže tvar bočního oblouku a profil po délce rozhodují, jestli budete mít pocit jistoty, nebo neustálého boje s hranou. '
          'Dva kusy se stejnou délkou se proto mohou jezdit naprosto odlišně a samotná délka nikdy nestačí.</p>'
          '<h2>Typy snowboardů podle stylu jízdy</h2>'
          + T(['Typ', 'Charakter', 'Pro koho'], [
              ['Allmountain', 'univerzální, zvládne svah, mulděnku i prašan', 'většina rekreačních jezdců a pokročilých začátečníků'],
              ['Freestyle a park', 'měkčí, kratší, symetrický tvar', 'skoky, boxy, jízda po rampách, hravější styl'],
              ['Freeride', 'tužší, delší, často směrový tvar a širší špička', 'hluboký sníh, strmé svahy, mimo upravené trasy'],
              ['Carving', 'úzké a tuhé, ostře profilované', 'zkušení jezdci, rychlé oblouky po tvrdém podkladu'],
              ['Splitboard a speciály', 'dělitelné prkno pro skialpinismus, kratší powder prkna', 'cílená zkušenost, nikoli první nákup']]) +
          '<p>Většina nabídky ve Sportece spadá do prvních dvou řádků, protože to jsou prkna pro běžné lyžařské areály. Pokud jezdíte v Česku nebo na Slovensku a občas vyrazíte do Alp, je allmountain nejrozumnější základ.</p>'
          '<h2>Profil prkna</h2>'
          '<p>Profil popisuje, jak je deska prohnutá při pohledu zboku. Je to nejdůležitější parametr po délce.</p>'
          '<ul><li><strong>Camber:</strong> klasický prohyb se středem nad sněhem. Dobře drží hranu a dává pružný výskok, ale míň odpouští chyby.</li>'
          '<li><strong>Rocker (reverzní camber):</strong> prkno je prohnuté dolů ke středu, špička a pata se zvedají. Snadno se otáčí, nezaboří se do prašanu a hodí se pro učení i park.</li>'
          '<li><strong>Hybrid:</strong> kombinace obou, například camber mezi nohama a rocker na koncích. Je to nejrozšířenější kompromis pro univerzální jízdu.</li>'
          '<li><strong>Plochý profil:</strong> stabilní a předvídatelný, dobrý pro začátečníky a jízdu po rampách.</li></ul>'
          '<h2>Tvar a směr</h2>'
          '<p>Twin je symetrický, špička i pata jsou stejné, takže se dá jet oběma směry stejně dobře. Hodí se pro park a jízdu v obou postojích. Directional je upravený pro jízdu dopředu, má delší špičku a nese lépe v prašanu. '
          'Directional twin je mezistupeň: téměř symetrický tvar s mírně posunutým postojem. Širší špička a zužující se pata, typická pro freeride, pomáhají při plavání ve sněhu, ale ztěžují jízdu pozpátku. '
          'U začátečníků bývá nejpraktičtější twin nebo directional twin, protože chyby při zatáčení odpustí víc.</p>'
          '<h2>Délka, šířka a váha</h2>'
          '<p>Zlaté pravidlo říká, že prkno ve stoje sahá zhruba mezi bradu a nos. Záleží ale hlavně na váze: lehčí jezdec potřebuje měkčí a kratší desku, těžší delší a tužší, jinak by se prkno ohýbalo víc, než je zdrávo. '
          'Výrobci uvádějí rozsah váhy pro každou délku, a tak je nejspolehlivější vycházet z tabulky u konkrétního modelu. Kratší deska se lépe otáčí a je pohodlnější pro začátečníky, delší je stabilnější při rychlosti a v prašanu.</p>'
          '<h3>Wide prkna</h3>'
          '<p>Pokud máte velkou botu, hrozí, že při zatáčení zavadí špička nebo pata o sníh. Takové jezdce míří k širšímu prknu označenému Wide, které má větší šířku v pase. Rozumná hranice je zhruba velikost obuvi kolem 44 a víc, ale rozhodně ji ověřte u výrobce. Širší deska se hůř naklání do hrany, takže pro menší nohu škodí.</p>'
          '<h2>Tuhost</h2>'
          '<p>Měkké prkno odpouští chyby, snadno se ohýbá a hodí se pro začátečníky, děti a park. Střední tuhost je univerzální. Tuhé prkno je stabilní při vyšší rychlosti a drží hranu na tvrdém sněhu, ale unaví a odrazí každý váhový nepořádek. Výrobci udávají tuhost na stupnici, kterou je ale potřeba porovnávat jen u jedné značky, protože každá si ji definuje jinak.</p>'
          '<h2>Snowboard samotný, nebo sada</h2>'
          '<p>Hotová sada s vázáním je výhodná pro první sezónu, protože šetří starosti s kompatibilitou a výběrem. Ve výpisu najdete i komplety, například od značek Raven, Gravity a Hatchey, ve kterých je prkno spárované s vázáním. Pokročilejší jezdec si sestavuje výbavu sám, aby měl vázání podle stylu a bot. '
          'Kompletní nabídku sad najdete v kategorii <a href="/snowboardove-sety/">snowboardové sety</a>. Samostatné <a href="/snowboardova-vazani/">snowboardové vázání</a> dobře vybírejte podle velikosti boty a stylu jízdy.</p>'
          '<h2>Výběr podle zkušeností</h2>'
          + T(['Úroveň', 'Doporučený profil', 'Tuhost a délka'], [
              ['Úplný začátečník', 'rocker nebo plochý, twin', 'měkké, spíš kratší prkno'],
              ['Pokročilý začátečník', 'hybrid, directional twin', 'středně měkké až střední'],
              ['Pokročilý a rekreační jezdec', 'hybrid s cambrem, allmountain', 'střední tuhost, délka podle váhy'],
              ['Expert a freerider', 'camber nebo směrový hybrid', 'tužší, delší, případně wide']]) +
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p>Dámská prkna bývají užší, měkčí a lehčí, protože zohledňují nižší váhu a menší nohu. Mnoho žen ale s úspěchem jezdí i na unisex modelech, hlavně pokud potřebují větší stabilitu. '
          'Dětské snowboardy jsou krátké a měkké, často s rockerem, a dítě z nich za dvě sezóny vyroste. Při volbě délky tedy počítejte s postupným růstem, ale nekupujte výrazně větší prkno než dítěti sahá k bradě.</p>'
          '<h2>Nastavení postoje</h2>'
          '<p>Regular postoj znamená levou nohu vpředu, goofy pravou. Zkuste se nechat lehce postrčit zezadu a zjistěte, kterou nohou se zachytíte. Šířka postoje se vždy nastavuje podle výrobce, ale obvykle odpovídá šířce ramen. '
          'Úhly vázání bývají u začátečníků lehce dopředu na obou nohách, v parku symetrické, u freeridu více dopředu na přední noze a téměř rovně vzadu.</p>'
          '<h2>Příslušenství a další výbava</h2>'
          '<ul><li><a href="/snowboardove-boty/">Snowboardové boty</a> musí padnout těsně na patě a nesmí tlačit na prstech.</li>'
          '<li><a href="/snowboardove-chranice/">Chrániče</a> na zápěstí, kolena a páteř se vyplatí hlavně při učení a v parku.</li>'
          '<li><a href="/lyzarske-helmy/">Helma</a> a <a href="/lyzarske-bryle/">brýle</a> patří k základu.</li>'
          '<li><a href="/lyzarske-rukavice/">Rukavice</a> s vyztuženým zápěstím chrání před častým dotykem se sněhem.</li>'
          '<li>Pytel nebo taška chrání prkno při přepravě, k tomu slouží také <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>.</li></ul>'
          '<p>Oblečení se řídí mírou namáhání a počasím. Kalhoty a bundu najdete mezi <a href="/lyzarske-kalhoty/">lyžařskými kalhotami</a> a <a href="/lyzarske-bundy/">lyžařskými bundami</a>, pod ně patří <a href="/lyzarske-termopradlo/">termoprádlo</a> a <a href="/lyzarske-ponozky/">ponožky</a>. Širší přehled nabízí rubrika <a href="/snowboarding/">snowboarding</a> a obecnější <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<h2>Co v kategorii najdete navíc</h2>'
          '<p>Kategorie nese nejen samotné desky, ale i příbuzné zboží, které se snowboardem souvisí, například střešní nosiče na lyže a snowboardy značky Menabo, ochranné kraťasy nebo oblečení pro zimní sporty. Při procházení proto sledujte název produktu, zda jde o prkno, nebo doplněk. Pro porovnání nabídek stejného modelu slouží stránka produktu, kde jsou obchody seřazené podle ceny a dostupnosti velikostí.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíc kusů mají ' + B(("raven", "Raven"), ("gravity", "Gravity"), ("ride", "Ride"), ("hatchey", "Hatchey"), ("nitro", "Nitro"), ("head", "Head")) +
          '. Prémiovější řady vyrábí ' + B(("burton", "Burton"), ("k2", "K2"), ("capita", "Capita"), ("bataleon", "Bataleon"), ("nidecker", "Nidecker"), ("jones", "Jones"), ("thirtytwo", "Thirtytwo"), ("rossignol", "Rossignol"), ("salomon", "Salomon")) + '. '
          'Cenově dostupné značky sází hlavně na hotové komplety, specialisté na freestyle, freeride nebo carving na samostatná prkna. Konkrétní parametry si ověřte u každého modelu, nespoléhejte na jméno značky.</p>'
          '<h2>Péče a servis</h2>'
          '<p>Po sezóně očistěte skluznici, zkontrolujte hrany a prkno natřete tlustší vrstvou vosku, která zabrání vysychání. Skladujte je v suchu a bez mrazu, nejlépe v pytli nebo na stojanu. '
          'Drobné škrábance se dají vyplnit opravnou hmotou, hluboké poškození jádra patří do servisu. Před sezónou se vyplatí nechat prkno vybrousit a navoskovat, protože rozdíl v kluzu se pozná hned. Pomůže vosk z kategorie <a href="/lyzarske-vosky/">lyžařské vosky</a>.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Kupovat prkno jen podle designu a ignorovat váhu a velikost boty.</li>'
          '<li>Vybírat příliš tuhý model, protože ho doporučuje zkušený kamarád. Začátečníkovi tuhé prkno komplikuje učení.</li>'
          '<li>Opomenout šířku prkna u velkých bot.</li>'
          '<li>Spojit prkno s vázáním, které se k jeho montáži nehodí. Kontrolujte rozteč děr a velikost vázání.</li>'
          '<li>Zanedbat boty. Skvělé prkno s nepohodlnou botou je špatná investice.</li></ul>'
          '<h2>Kdy kupovat</h2>'
          '<p>Největší nabídka velikostí je na podzim, kdy obchody doplňují sklady. Starší ročníky se často prodávají se slevou po sezóně, funkčně se ale mění jen málo, hlavně u základních prken. '
          'Pokud znáte svoji délku a typ, vyplatí se sledovat vývoj nabídky u více obchodů a sáhnout po prknu ve chvíli, kdy je skladem vaše velikost.</p>',
    faq=[
        ('Jak dlouhý snowboard potřebuji?', 'Orientačně sahá prkno mezi bradu a nos, ale důležitější je váha. Každý výrobce uvádí rozsah váhy pro danou délku, takže vyjděte z tabulky konkrétního modelu a zohledněte styl jízdy.'),
        ('Který profil je nejlepší pro začátečníka?', 'Nejlépe se učí na rockeru nebo plochém profilu, případně na hybridu. Takové prkno se snadno otáčí a odpustí chyby, kdežto klasický camber vyžaduje přesnější práci s hranou.'),
        ('Jaký je rozdíl mezi twin a directional prknem?', 'Twin má symetrický tvar a jede se na něm stejně dopředu i pozpátku, hodí se do parku. Directional je upravený pro jízdu dopředu a lépe nese v prašanu i při rychlosti.'),
        ('Kdy potřebuji široké prkno (wide)?', 'Když vám při zatáčení bota přesahuje přes hranu prkna a zavadí o sníh. Hranice se liší podle modelu, obvykle se týká větších velikostí obuvi.'),
        ('Je lepší koupit snowboard samostatně, nebo v sadě?', 'Pro první sezónu je sada jednodušší, protože vázání už je zvolené a namontované. Zkušený jezdec si raději skládá výbavu sám podle stylu a boty.'),
        ('Jak poznám tuhost snowboardu?', 'Výrobci ji uvádějí na stupnici, ale každý jinak, proto porovnávejte jen u jedné značky. Měkké prkno je pro začátečníky a park, tuhé pro rychlost a tvrdý sníh.'),
        ('Kolik let vydrží snowboard?', 'Při běžné péči mnoho sezón. Rozhoduje hlavně stav hran, skluznice a jádra. Pokud je prkno opotřebované nebo ztratilo pružnost, jízda se zhorší a vyplatí se výměna.'),
        ('Jaký snowboard je vhodný pro děti?', 'Krátký, měkký a lehký, nejlépe s rockerem nebo plochým profilem. Dítě by mělo prkno unést, otočit a mít u něj vázání nastavené podle velikosti boty.'),
        ('Jak snowboard skladovat přes léto?', 'Očistěte ho, navoskujte skluznici silnější vrstvou a uložte na suchém místě bez mrazu a přímého slunce. Vázání před uložením očistěte od soli a nečistot a zkontrolujte šrouby i popruhy.'),
        ('Musím snowboard před sezónou servisovat?', 'Doporučuje se zkontrolovat hrany, vybrousit skluznici a navoskovat ji. Servis zlepší klouzání i ovladatelnost a prodlouží životnost prkna.'),
    ])

# ------------------------------------------------------------------ cyklo-blatniky
NEW['cyklo-blatniky'] = dict(long=True,
    title='Blatníky na kolo: sady, přední a zadní, výběr',
    desc='Blatníky na kolo: sady na trekking a silnici, MTB blatníky, nasazovací a pod sedlo. Jak zvolit šířku, průměr kola a upevnění, porovnejte obchody.',
    intro='<p>Blatník nezdobí kolo, ale chrání jezdce před vodou a blátem z kol a před ušpiněným zadkem i mokrými zády, a to i při krátké cestě do práce. Chrání také řetěz, pohon a spodní část rámu před nánosem špíny, která se jinak vetře do ložisek a urychlí opotřebení. '
          'Na trhu je několik základních konstrukcí: pevné blatníky přišroubované k rámu, nasazovací modely s gumovými pásky nebo sponami, krátké kousky pod sedlem a nízké přední štítky na horská kola. '
          'Správná volba závisí na průměru kola, šířce pláště, rámu a hlavně na tom, kde jezdíte.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u blatníků značek Topeak, SKS, Force, Polisport, Author, Reverse, ASS Savers, M-Wave nebo Rockrider. '
          'Související zboží najdete v kategoriích <a href="/cyklo-dily/">díly a pláště</a>, <a href="/cyklo-prislusenstvi/">příslušenství</a> a <a href="/cyklo-chranice/">chrániče</a>. '
          'Níže je přehled typů, rozměrů, montáže a péče.</p>',
    guide='<h2>K čemu blatník je</h2>'
          '<p>Pneumatika při jízdě po mokru nese vodu až nahoru a vrhá ji dozadu a dopředu. Zadní kolo stříká na záda a zadní část sedla, přední na nohy, boty, spodní trubku rámu a pohon. '
          'Dobře zvolený blatník vodu odvede dolů, takže jezdec zůstane relativně suchý a kolo se nemusí po každé jízdě čistit. Zadní chrání jezdce a ty, kdo jedou za ním. Přední chrání nohy, boty, pohon a spodní část rámu. '
          'Kdo jezdí po silnici ve skupině, dává zadní blatník i ohledu na ty, kdo jedou za ním.</p>'
          '<h2>Typy blatníků</h2>'
          + T(['Typ', 'Upevnění', 'Pro koho'], [
              ['Pevné celé blatníky', 'šrouby na očkách rámu a vidlice, vzpěry', 'trekking, městská kola, denní dojíždění'],
              ['Sada nasazovacích blatníků', 'pásky, svorky nebo sponky na rámu', 'silnice, gravel, kola bez ok'],
              ['Krátký blatník pod sedlem', 'upevnění na sedlovku nebo kolejničky', 'horská a silniční kola, rychlé nasazení'],
              ['Přední MTB štítek', 'pásky na vidlici nebo korunce', 'terén, bláto, odlehčená kola'],
              ['Blatníky na dětská kola a odrážedla', 'šrouby nebo svorky, menší rozměr', 'dětská kola 12 až 24 palců'],
              ['Blatníky pro koloběžky a malá kola', 'šroubované na osu', 'skládací a městské vozítko']]) +
          '<p>Pevné blatníky nabídnou nejlepší krytí, ale vyžadují očka na rámu a vidlici a dostatek místa mezi pláštěm a vidlicí. Nasazovací varianty jdou sundat a hodí se ke sportovnímu kolu, které používáte jen občas v dešti. Krátká pláštěnka za sedlem je minimalistická, ale na silnější déšť nestačí.</p>'
          '<h2>Průměr kola a šířka pláště</h2>'
          '<p>Blatník musí odpovídat průměru kola, tedy 20, 24, 26, 27,5 nebo 28 palců a v případě moderních horských kol i 29 palců. K tomu je nutná šířka pláště: blatník, který je užší než plášť, nechrání a stříká podél kol. '
          'U sad pro silnice se uvádí šířka do zhruba 28 mm, trekingové jsou širší, horská kola a gravel potřebují modely pro plášť 40 mm a víc. Šířka blatníku se obvykle volí o pár milimetrů větší než plášť, aby byl mezi nimi vzduch. '
          'Zkontrolujte také, že za plášť s blátem a zátěží zbyde dost místa, jinak se do blatníku zahrabe kámen a zablokuje kolo.</p>'
          '<h3>Prostor u rámu a vidlice</h3>'
          '<p>Blatník vyžaduje volný prostor mezi pláštěm a rámem, hlavně u brzdy a pod sedlovou trubkou. U silničních kol s kotoučovými brzdami je prostor omezený, a proto se do nich hodí specializované řady. U kol s odpruženou vidlicí použijte přední blatník, který se upevňuje na vidlici, ne k rámu, jinak by se při propružení otíral o plášť.</p>'
          '<h2>Materiály</h2>'
          '<ul><li><strong>Plast:</strong> lehký, levný a tichý, při nárazu se prohne a vrátí. Na horské i silniční modely je nejčastější.</li>'
          '<li><strong>Hliník:</strong> pevný, odolný a dlouhodobý, vhodný na trekingová a městská kola. Při nárazu se může zdeformovat.</li>'
          '<li><strong>Uhlík a kompozity:</strong> velmi lehké, určené na závodní kola.</li>'
          '<li><strong>Pryž a pěna:</strong> na ochranu spodní trubky nebo na malé štítky pod sedlo.</li></ul>'
          '<h2>Blatníky na silniční kolo</h2>'
          '<p>Silniční kolo má malé mezery a úzký plášť, proto se používají nasazovací sady z tenkého plastu. Mnoho z nich se připíná gumovými pásky nebo se zasouvá mezi plášť a rám a vyžaduje jen pár minut práce. '
          'V zimě a při jízdě v dešti se hodí kompletní sada, na krátké výlety stačí jen zadní díl. Zvláštní kategorii tvoří blatníky pro gravel, které jsou širší a odolnější. Při výběru dbejte na kompatibilitu s kotoučovými brzdami a s osou o průchozí oko.</p>'
          '<h2>Blatníky na horské kolo</h2>'
          '<p>Terén znamená bláto, kamení a větve. Přední štítek je vyrobený z pružného plastu, který se připevňuje stahovacími páskami a drží i při nárazu. Zadní je krátký a přichycený pod sedlem. Hodí se na odlehčený horský trail, kde nechcete rušit hmotnost nebo aerodynamiku. '
          'Dlouhé klasické blatníky jsou na MTB při jízdě v bahně na škodu, protože se mezi ně a plášť nasbírá bláto. Pro silnější deště a trailové jezdce se vyrábějí kratší štíty, které lze rychle sundat. Kola, která k terénu přesedlají, najdete mezi <a href="/horska-kola/">horskými koly</a> a <a href="/celoodpruzena-horska-kola/">celoodpruženými koly</a>.</p>'
          '<h2>Blatníky na trekingové a městské kolo</h2>'
          '<p>Treking a město nabízejí největší pohodlí. Pevný blatník celé kolo ochrání, jezdec zůstane čistý a může jet v běžném oblečení. Součástí jsou vzpěry, které drží blatník v pevné vzdálenosti od kola a zabraňují vibracím. '
          'Mnoho modelů má vzadu odrazku nebo místo pro světlo. Pokud plánujete nosič, zvolte blatníky kompatibilní s nosičem, jinak se díly mezi sebou perou o místo. Kola na dojíždění najdete mezi <a href="/trekingova-kola/">trekingovými koly</a> a <a href="/mestska-kola/">městskými koly</a>. K blatníkům patří také <a href="/cyklo-svetla/">cyklistická světla</a> a <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>.</p>'
          '<h2>Dětská kola a elektrokola</h2>'
          '<p>Na dětská kola se hodí blatníky, které lze snadno sundat a které se nepoškodí při pádu. Hledejte hladké hrany bez ostrých rohů a rozměr podle průměru kola v rozsahu 12 až 24 palců. Informace k výběru kol najdete v kategorii <a href="/detska-kola/">dětská kola</a>. '
          'Elektrokola jedou rychleji a při jízdě po mokru je spršť vody větší, proto se u nich vyplatí kompletní blatníky s dostatečnou šířkou. U modelů s motorem v zadním kole si ověřte, kam se zadní blatník upevňuje a zda nezakrývá součásti baterie nebo kabely.</p>'
          '<h2>Příslušenství k blatníkům</h2>'
          '<p>Při nákupu se vyplatí pomyslet také na doplňky. Stabilizační vzpěry a šrouby přijdou vhod, pokud se některé vám při montáži ztratí. Bezpečnostní odrazky a LED světla na zadním blatníku zvýší viditelnost. Chránič řetězu a ochrana před blátem na spodní trubce doplňují ochranu pohonu. Pro údržbu používejte <a href="/cyklo-udrzba/">čisticí a mazací prostředky</a> a <a href="/cyklo-pumpy-a-naradi/">nářadí</a>, které usnadní montáž.</p>'
          '<h2>Montáž krok za krokem</h2>'
          '<ol><li>Změřte průměr kola a šířku pláště a zkontrolujte, že se blatník vejde mezi plášť a vidlici.</li>'
          '<li>Zvolte přední a zadní díl a rozhodněte, zda budete upevňovat na očka, nebo bez nich.</li>'
          '<li>Blatník předběžně nasaďte, vycentrujte nad plášť a mezeru nastavte rovnoměrně po celém obvodu.</li>'
          '<li>Dotáhněte šrouby a vyzkoušejte, že se plášť otáčí volně, bez drnčení či otírání.</li>'
          '<li>Po prvních kilometrech kontrolu zopakujte, protože se vibracemi mohou uvolnit šrouby.</li></ol>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš úzký blatník na široký plášť, který stříká do stran.</li>'
          '<li>Pevný blatník na kolo, které nemá očka, nebo dostatek místa nad pláštěm.</li>'
          '<li>Nedotažené šrouby, které způsobí drnčení nebo vypadnutí blatníku za jízdy.</li>'
          '<li>Dlouhý blatník na trailové MTB, který se zahrabe blátem.</li>'
          '<li>Nepřipravená zima: bez blatníků a s tenkým pláštěm se kolo rychle zanáší solí a špínou.</li></ul>'
          '<h2>Zima, sůl a mokré silnice</h2>'
          '<p>Od listopadu do března se na silnicích sype sůl, která s vodou vytváří agresivní roztok. Kompletní blatníky zabrání, aby se dostal na řetěz, kazety a brzdové třmeny, a výrazně sníží počet čištění. Při zimním dojíždění je lepší zvolit širší sadu a po jízdě kolo opláchnout čistou vodou. Zadní blatník s prodloužením chrání také toho, kdo jede za vámi.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejširší zastoupení mají ' + B(("topeak", "Topeak"), ("sks", "SKS"), ("reverse", "Reverse"), ("force", "Force"), ("polisport", "Polisport"), ("author", "Author"), ("ass-savers", "ASS Savers"), ("m-wave", "M-Wave")) +
          '. Další nabídku mají ' + B(("rockbros", "Rockbros"), ("rrp", "RRP"), ("urbis", "Urbis"), ("yedoo", "Yedoo"), ("elops", "Elops"), ("max1", "Max1"), ("mucky-nutz", "Mucky Nutz"), ("zefal", "Zefal"), ("eurofender", "Eurofender")) + '. '
          'SKS a Eurofender jsou typické pro klasické trekingové sady, Topeak a ASS Savers pro nasazovací řešení, Mucky Nutz a Reverse pro horská kola. Najdete tu také díly pro koloběžky a malá kola, například od značky Oxelo.</p>'
          '<h2>Údržba a skladování</h2>'
          '<p>Blatník se jednou za čas umyje vodou a jemným čisticím prostředkem. Šrouby a svorky se kontrolují v rámci běžného servisu a gumové pásky se vyměňují, když ztratí pružnost. Plastové modely na zimu uložte mimo přímé slunce, UV záření materiál časem zkřehne. '
          'Pokud blatník používáte jen občas, nasazovací varianta se po jízdě sundá a uloží, aby se nezanášela. Před zimním uložením blatníky otřete od bláta a zkontrolujte, zda jsou šrouby a držáky pevně dotažené.</p>'
          '<h2>Jak vybírat v obchodech</h2>'
          '<p>Při porovnání zkontrolujte u každého produktu průměr kola, šířku blatníku a způsob upevnění, protože se u stejné značky liší i několik desítek variant. Na Sportece uvidíte u každého blatníku nabídky více obchodů a rychle poznáte, kdo má hledaný rozměr skladem. Hledáte-li celé kolo, přejděte do kategorie <a href="/cyklistika/">cyklistika</a>; k blatníkům se hodí i <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>.</p>',
    faq=[
        ('Jak vybrat blatník podle průměru kola?', 'Blatník musí odpovídat průměru kola, například 26, 27,5, 28 nebo 29 palců, a zároveň šířce pláště. Údaj najdete na boku pláště a v popisu blatníku.'),
        ('Dají se blatníky namontovat na kolo bez ok?', 'Dá se použít nasazovací sada s pásky nebo sponami, která se upíná na rám a vidlici bez šroubů. Takové blatníky jsou lehčí, ale kryjí méně než pevné modely.'),
        ('Je lepší plastový, nebo hliníkový blatník?', 'Plast je lehký a pružný, na MTB a silnici nejpoužívanější. Hliník je pevnější a dlouhodobější, hodí se na trekingová a městská kola.'),
        ('Potřebuji blatník i na horské kolo?', 'Na suchých trailech ne, v bahnitém terénu však přední štítek chrání obličej a oči a zadní zlepšuje komfort. Zvolte kratší model, který se zahrabe méně.'),
        ('Proč blatník drnčí?', 'Nejčastěji je špatně vycentrovaný nebo mají volné šrouby a vzpěry. Dotáhněte spoje a zkontrolujte, zda se mezi plášť a blatník nezapletl kamínek.'),
        ('Dají se blatníky použít na elektrokole?', 'Ano, u elektrokol se doporučují kompletní blatníky, protože se jezdí rychleji a stříká více vody. Zkontrolujte kompatibilitu s nosičem, motorem a kabeláží.'),
        ('Jaké blatníky se hodí na silniční kolo?', 'Nasazovací sady z tenkého plastu nebo specializované modely pro kotoučové brzdy. Vybírejte podle šířky pláště a prostoru u rámu.'),
        ('Jak namontovat zadní blatník pod sedlo?', 'Přichytí se na sedlovku, kolejničky sedla nebo pomocí pásků. Seřiďte jej tak, aby kryl záda a nedotýkal se pláště, a pevně dotáhněte upevnění.'),
        ('Mají být blatníky pro dětská kola jiné?', 'Měly by mít hladké okraje, jednoduché upevnění a rozměr podle průměru kola. Při pádu se nesmí zachytit ani zlomit na ostré hrany.'),
        ('Jak dlouho blatník vydrží?', 'Při běžném užívání několik sezón. Plast časem zkřehne od slunce a mrazu, proto se kontroluje drží-li upevnění a nevznikají praskliny.'),
    ])

# ------------------------------------------------------------------ kajaky-a-cluny
NEW['kajaky-a-cluny'] = dict(long=True,
    title='Kajaky a čluny: nafukovací, kánoe, pádla, pumpy',
    desc='Nafukovací kajaky, kánoe a čluny včetně pádel, pump a tašek. Jak vybrat typ, počet míst a materiál a porovnat nabídky českých obchodů.',
    intro='<p>Kajak nebo člun otevírá vodu stejně jako kolo otevírá silnici: dostanete se na klidnou řeku, k jezeru nebo na přehradu, kam se pěšky nedojde. Dnešní nabídka je ale široká a snadno se splete nafukovací kajak, kánoe pro dva, rybářský člun a pevná loď, přestože se každá hodí na jiné vody a jinou posádku. '
          'Rozhoduje, kolik lidí pojede, kolik věcí povezete, jak daleko budete přenášet loď k vodě a zda ji budete skládat do auta, nebo vozit na střeše.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u nafukovacích kajaků, kánoí a člunů od značek Aqua Marina, Gumotex, Intex, Bestway, Sevylor, Spinera, Itiwit nebo Dagger, včetně pádel, pump a tašek. '
          'K tématu patří také <a href="/paddleboardy/">paddleboardy</a>, <a href="/vodni-sporty/">vodní sporty</a> a <a href="/plovaci-vesty/">plovací vesty</a>. Níže najdete typy lodí, materiály, příslušenství a bezpečnost.</p>',
    guide='<h2>Typy lodí</h2>'
          + T(['Typ', 'Charakter', 'Pro koho'], [
              ['Nafukovací kajak', 'sedí se na nízkých sedačkách, pohání se dvoulistým pádlem', 'rekreační pádlování, klidná voda, jednoduchá přeprava'],
              ['Nafukovací kánoe', 'otevřená loď, jednolistové pádlo, více místa na zavazadla', 'rodiny, výlety s batohy, dvojice a trojice'],
              ['Hybrid kánoe a kajak', 'konstrukce na přechodu, často s dropstitch podlahou', 'univerzální loď pro jednoho až tři'],
              ['Nafukovací člun', 'širší trup, lavice, vesla nebo motor', 'rybaření, rodinné výlety, jezero, přehrada'],
              ['Pevný kajak', 'plast nebo kompozit, větší rychlost a stabilita na rovině', 'zkušení pádlaři, delší trasy, řeka'],
              ['Sportovní a vodácké čluny', 'vyztužené nafukovací lodě pro divokou vodu', 'zkušení vodáci, peřeje']]) +
          '<p>Většinu nabídky ve Sportece tvoří nafukovací lodě, protože se vejdou do kufru a po použití se skládají do tašky. Pevné lodě se vyrábějí z plastu, skla nebo uhlíku a vozí se na střeše, což je nepohodlné, ale vynahradí to lepší plavební vlastnosti.</p>'
          '<h2>Počet míst a nosnost</h2>'
          '<p>Jednomístný kajak se hodí pro sólového pádlaře, dvoumístný nejčastěji bere dva dospělé a málo vybavení, třímístný už nese rodinu s dítětem nebo dvojici s lehčími zavazadly. Rozhodující je nosnost uváděná výrobcem, nikoli počet sedadel. '
          'Do nosnosti se počítá váha posádky i veškerá výbava, takže při výletech na víc dní se vyplatí vybrat loď s rezervou. Loď přetížená nad doporučenou hranici je méně stabilní a hůř ovladatelná. Rozměry, hlavně délku a šířku, porovnávejte i s tím, kam ji uložíte.</p>'
          '<h2>Materiály a konstrukce</h2>'
          '<ul><li><strong>PVC:</strong> nejběžnější materiál nafukovacích lodí, pevný, odolný a snadno se opravuje lepením. Kvalita se liší tloušťkou a počtem vrstev.</li>'
          '<li><strong>Nylon s potahem:</strong> lehčí, pružnější, často dražší a výhodný pro přenášení.</li>'
          '<li><strong>Hypalon a podobné kaučukové materiály:</strong> velmi odolné vůči slunci, používají se u profesionálních a vojenských člunů.</li>'
          '<li><strong>Dropstitch (zpevněná podlaha):</strong> tisíce nití mezi vrstvami umožňují vyšší tlak a pevnější dno. Loď se pak chová spíš jako tuhá deska.</li>'
          '<li><strong>Polyetylen a kompozity:</strong> pevné kajaky, těžší, ale s lepší stopou a delší životností.</li></ul>'
          '<h2>Komory, ventily a tlak</h2>'
          '<p>Loď se skládá z několika vzduchových komor. Víc komor znamená vyšší bezpečnost: při proražení jedné zbylé stále nesou. Ventily se plní pumpou a u vyšších tlaků se používá vysokotlaká nebo dvoukomorová pumpa. '
          'Tlak udává výrobce, a je-li loď podhuštěná, ztrácí tvar a špatně klouže. Naopak přehuštění na slunci může komory poškodit, protože se vzduch zahřívá a rozpíná. Proto lodě na pláži hlídejte a podle potřeby tlak upouštějte. Pumpy a další doplňky najdete mezi příslušenstvím.</p>'
          '<h2>Pádlo</h2>'
          '<p>Kajakářské pádlo má dva listy a sedí se k němu nízko. Kánoe se pohání jednolistým pádlem a pádluje se z kolenou nebo v sedě na lavičce. Pádlo musí odpovídat výšce a šířce lodi: čím širší trup, tím delší pádlo. '
          'Hliníkové jsou levnější a těžší, skleněné nebo uhlíkové lehčí a příjemnější na dlouhé trasy. Dělené pádlo je praktické pro přepravu, nastavitelné pak zvládne více jezdců. Jako náhradu mějte u sebe alespoň jedno další, pokud jedete do divokého terénu.</p>'
          '<h2>Příslušenství, které se vyplatí</h2>'
          '<ul><li><strong>Plovací vesta:</strong> základní doporučená výbava každého pádlaře, u dětí a neplavců nutná. Viz <a href="/plovaci-vesty/">plovací vesty</a>.</li>'
          '<li><strong>Pumpa s manometrem:</strong> nejlépe s měřením tlaku, aby nebyla loď přehuštěna.</li>'
          '<li><strong>Opravná sada:</strong> záplaty a lepidlo na PVC patří do každé tašky.</li>'
          '<li><strong>Vodotěsný vak:</strong> udrží v suchu telefon, doklady a oblečení.</li>'
          '<li><strong>Kotva, lano a plovák:</strong> pro rybáře a výlety na jezeře.</li>'
          '<li><strong>Sedačka a opěrka:</strong> rozhodují o pohodlí na delších trasách.</li>'
          '<li><strong>Taška na přepravu:</strong> loď složená do batohu se snáz nese k vodě.</li></ul>'
          '<h2>Oblečení a obuv</h2>'
          '<p>Pádlování znamená vodu na rukou, na kalhotách i na nohou. V létě stačí rychleschnoucí oblečení, v přechodném období se přidává <a href="/neopreny/">neopren</a> a <a href="/obuv-do-vody/">obuv do vody</a>, v chladu také bunda a rukavice. '
          'Pro ochranu před sluncem se hodí <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>, na vodě také sportovní brýle a čepice. Pokud se bojíte, že padnete do vody, vezměte si navíc náhradní oblečení v nepromokavém vaku.</p>'
          '<h2>Výběr podle vody</h2>'
          + T(['Voda', 'Vhodná loď', 'Na co dbát'], [
              ['Rybník, jezero, přehrada', 'nafukovací kajak nebo člun', 'stabilita, vítr, držení kurzu'],
              ['Klidná řeka', 'kánoe nebo kajak s dropstitch dnem', 'odolnost materiálu, opravná sada'],
              ['Řeka s jezy a peřejemi', 'pevný nebo vyztužený nafukovací kajak', 'zkušenosti, helma, vesta, nácvik'],
              ['Moře a pobřeží', 'pevný mořský kajak, větší nafukovací modely', 'počasí, proudy, signalizace, vesty'],
              ['Rybaření', 'stabilní člun nebo kánoe', 'nosnost, opěrky, úchyty na pruty']]) +
          '<p>Vždy ověřte, kde se na vodě smí jezdit. Některé přehrady, říční úseky nebo přírodní rezervace mají omezení a na rybářských revírech platí vlastní pravidla.</p>'
          '<h2>Bezpečnost</h2>'
          '<p>Na vodu patří vesta, mobil v pouzdře a znalost trasy. Před výletem se informujte o počasí a o hladině řeky. Nikdy nejezděte sami po neznámé vodě a nechávejte někoho informovaného o plánu. '
          'Studená voda je nebezpečná i v létě, protože při pádu může způsobit šok. Při převrácení se držte lodi a plavte s ní ke břehu. Alkohol a pádlování nepatří k sobě. Začátečníkům se vyplatí první výlety s kamarádem, který má zkušenost.</p>'
          '<h2>Přeprava a skladování</h2>'
          '<p>Nafukovací loď se po použití opláchne, důkladně osuší a uloží složená v tašce na suchém a chladném místě. Mokrá loď uložená v pytli začne plesnivět a lepené spoje se mohou rozlepit. Pevné lodě se vozí na střešních nosičích, k tomu slouží kategorie <a href="/cyklo-nosice-na-auto/">nosiče na auto</a> a podobné držáky. '
          'Chraňte loď před slunečním zářením, ostrými hranami a dlouhodobým stlačením. Kontrolujte ventily a lepené spoje, protože drobná netěsnost se na vodě projeví nejhůř.</p>'
          '<h2>Co v kategorii najdete navíc</h2>'
          '<p>Vedle lodí se v nabídce objevují také pádla, SUP pádla, pumpy, tlakoměry, tašky, záchranné pomůcky a příslušenství k rybaření nebo bushcraftu. Doplňky se liší typem lodi i použitím, proto u každého produktu ověřte, zda se hodí k vaší lodi. '
          'Proto sledujte název produktu a popis. Pro paddleboardy mají vlastní kategorii <a href="/paddleboardy/">paddleboardy</a>, rybářské vybavení najdete v <a href="/rybareni/">rybaření</a>.</p>'
          '<h2>Kajak na dovolenou a do batohu</h2>'
          '<p>Pokud loď potřebujete vzít do vlaku, letadla nebo na kole, hledejte lehčí modely do desíti až patnácti kilogramů, které se složí do batohu s popruhy. Při plánování cesty počítejte i s pumpou, pádlem a vestou, protože právě ty zaberou v zavazadle místo. '
          'Takové lodě mívají menší nosnost a kratší trup, hodí se pro klidnou vodu a jednodenní výlet. Delší expedice vyžadují pevnější a stabilnější konstrukci s prostorem pro vak a stan.</p>'
          '<h2>Rybaření z lodi</h2>'
          '<p>Rybáři oceňují stabilní plochou loď s rozumnou nosností, úchyty na pruty a místem pro podběrák a krabici. Širší kánoe a čluny se nepřevrhnou při tahu na pruty a poskytnou větší klid při obsluze nástrah. '
          'Elektrický motor se na nafukovací člun připevňuje na zrcadlo, které je třeba vyztužit. Zjistěte předem, zda je na daném revíru loď povolena, a na vodě mějte vždy vestu. Rybářské vybavení najdete v rubrice <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce lodí a pádel jsou zastoupeny ' + B(("decathlon", "Decathlon"), ("aqua-marina", "Aqua Marina"), ("gumotex", "Gumotex"), ("intex", "Intex"), ("bestway", "Bestway"), ("sevylor", "Sevylor"), ("spinera", "Spinera"), ("itiwit", "Itiwit"), ("caperlan", "Caperlan")) +
          '. Další nabídku mají ' + B(("dagger", "Dagger"), ("tahe", "Tahe"), ("hydro-force", "Hydro-Force"), ("plastimo", "Plastimo"), ("padla-panda", "Panda"), ("x-paddle-boards", "X Paddle Boards")) + '. '
          'Gumotex je známý z českého nafukovacího segmentu, Aqua Marina a Intex nabízejí rekreační lodě, Dagger se zaměřuje na pevné kajaky. Parametry porovnávejte u konkrétního modelu, ne podle značky.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš malá loď: dvoumístný kajak pro dospělého a dítě s kempinkovým vybavením přetíží nosnost.</li>'
          '<li>Levný člun do divoké vody. Rekreační modely nejsou určeny pro peřeje.</li>'
          '<li>Opomenutí pumpy. Ruční pumpa může nafukování protáhnout na desítky minut.</li>'
          '<li>Koupě lodi bez plánu uskladnění a převozu.</li>'
          '<li>Podcenění bezpečnosti: vesta, mobil, voda a informace o počasí patří k výbavě.</li></ul>',
    faq=[
        ('Jak vybrat nafukovací kajak?', 'Podle počtu osob, nosnosti, typu vody a zkušeností. Pro rekreaci stačí PVC model s více komorami, pro řeku se hodí odolnější loď s tuhým dnem.'),
        ('Čím se liší kajak od kánoe?', 'Kajak se pádluje dvoulistým pádlem v nízkém sedu, kánoe má otevřený prostor a jednolistá pádla. Kánoe nese víc zavazadel, kajak je rychlejší a obratnější.'),
        ('Kolik lidí unese dvoumístný kajak?', 'Vždy záleží na nosnosti udávané výrobcem. Počítejte celkovou váhu posádky i výbavy a nechte si rezervu, protože přetížená loď je nestabilní.'),
        ('Co je to dropstitch?', 'Dropstitch je konstrukce s množstvím nití mezi vrstvami materiálu, která umožňuje větší tlak a vytvoří tuhou podlahu. Loď se pak lépe ovládá a lépe drží tvar.'),
        ('Jak dlouho trvá nafouknout kajak?', 'Elektrickou pumpou několik minut, ruční pumpou i desítky minut. Proto se vyplatí pumpa s tlakoměrem, která zvládne požadovaný tlak.'),
        ('Potřebuji na kajak plovací vestu?', 'Ano, plovací vesta je základní součást bezpečné výbavy. Děti a neplavci ji nosí vždy a dospělí také, zvlášť na řekách a otevřených vodách.'),
        ('Jak opravit proděravělou nafukovací loď?', 'Najděte místo úniku vodou s mýdlem, očistěte okolí a přelepte záplatou s lepidlem na PVC. Větší trhliny nebo poškození ve švu patří do servisu.'),
        ('Dá se nafukovací loď používat na peřejích?', 'Jen modely určené pro divokou vodu, s vyztuženou konstrukcí a podle zkušeností pádlaře. Běžný rekreační člun se do peřejí nehodí.'),
        ('Jak loď po použití uložit?', 'Opláchněte ji čistou vodou, důkladně osušte, mírně napudrujte talkem a složte volně do tašky. Skladujte na suchém místě bez přímého slunce.'),
        ('Je lepší pevný, nebo nafukovací kajak?', 'Nafukovací se lépe převáží a skladuje. Pevný lépe drží směr, bývá rychlejší a vydrží víc, ale potřebuje střešní nosič a místo na uskladnění.'),
        ('Unese nafukovací kajak i rybářskou výbavu?', 'Záleží na nosnosti a na šířce trupu. Pro rybaření se hodí stabilní širší lodě s úchyty na pruty, počítejte ale s váhou posádky, výbavy i úlovku.'),
        ('Jakou pumpu k nafukovací lodi použít?', 'Nejlépe pumpu s tlakoměrem, která zvládne tlak udávaný výrobcem. Ruční dvoukomorová pumpa stačí na menší kajak, na větší lodě je pohodlnější elektrická s automatickým vypnutím.'),
    ])

# ------------------------------------------------------------------ tanec-a-gymnastika
NEW['tanec-a-gymnastika'] = dict(long=True,
    title='Tanec, balet a gymnastika: obuv, dresy, náčiní',
    desc='Taneční a baletní obuv, trikoty, sukýnky a gymnastické náčiní, stuhy, míče, kruhy a kladiny. Jak vybrat velikost a porovnat obchody.',
    intro='<p>Tanec a gymnastika spojují pohyb, ohebnost a přesnost, a proto je výbava pro ně specifická. Taneční obuv musí mít správnou přilnavost i otáčivost podle povrchu, trikot a sukýnka nesmí překážet v pohybu a gymnastické náčiní musí odpovídat věku, výšce i disciplíně. '
          'Rodiče nejčastěji kupují první dětskou výbavu do kroužku, dospělí hledají boty na společenský tanec nebo pomůcky na doma, trenéři doplňují vybavení tělocvičen.</p>'
          '<p>Na Sportece najdete jednou stránkou nabídky českých obchodů s <a href="/baletni-obuv/">baletní obuví</a>, <a href="/tanecni-obuv/">taneční obuví</a>, <a href="/tanecni-obleceni/">tanečním oblečením</a> a <a href="/gymnasticke-pomucky/">gymnastickými pomůckami</a>. '
          'Zastoupeny jsou značky Domyos, Sybai, Papillon, Indigo Sports, HMS nebo Insportline. Pro další pohybovou výbavu přejděte na <a href="/fitness/">fitness</a> nebo <a href="/joga-a-pilates/">jógu a pilates</a>. '
          'Níže je přehled disciplín, velikostí, materiálů a péče.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          + T(['Skupina', 'Obsah', 'Typický kupující'], [
              ['Baletní obuv', 'piškoty, špičky, měkké baletní cvičky', 'děti v baletních kroužcích, dospělé začátečníky'],
              ['Taneční obuv', 'společenské, latinskoamerické, jazz a street', 'taneční páry, kurzy, soutěžní tanečníky'],
              ['Taneční a baletní oblečení', 'trikoty, sukýnky, legíny, bolera, úbory', 'děti i dospělí, nejčastěji ženy a dívky'],
              ['Gymnastické pomůcky', 'míče, stuhy, kruhy, obruče, kladiny, žíněnky, hrazdy', 'oddíly, školy, domácí cvičení'],
              ['Rehabilitační a cvičební míče', 'velké míče, kruhy, gumy pro cvičení doma', 'rehabilitace, pilates, cvičení pro děti']]) +
          '<p>Obsah je široký, protože každá disciplína potřebuje jiné vybavení. Pro přehlednost doporučujeme začít ve vhodné podkategorii a teprve pak hledat podle značky, velikosti nebo materiálu.</p>'
          '<h2>Baletní obuv</h2>'
          '<h3>Piškoty a cvičky</h3>'
          '<p>Měkká baletní obuv z kůže, plátna nebo textilu se přizpůsobí noze a umožňuje cítit podlahu. Rozlišují se dva střihy: celá podrážka a dělená podrážka s koženou částí pod špičkou a patou. Dělená dovolí lépe protáhnout nárt. '
          'Děti většinou začínají plátěnými nebo koženými cvičkami s pružným stahováním přes nárt, aby nespadly. Velikost se vybírá s minimální rezervou, boty mají sedět těsně, protože se mírně rozšlapou.</p>'
          '<h3>Špičky</h3>'
          '<p>Špičky jsou tuhé boty s vyztuženou špičkou. Nesmí se kupovat naslepo: tvar špičky, šířka, výška nártu a tuhost musí odpovídat noze a síle tanečnice. Dětem se špičky dávají teprve po delším tréninku, a až o jejich nasazení rozhodne učitel. '
          'Nesprávné špičky mohou poškodit kosti a klouby, proto se kupují v kamenném obchodě s odborným měřením nebo po konzultaci s učitelem.</p>'
          '<h2>Taneční obuv</h2>'
          '<p>Společenské a standardní boty mají jemnou podrážku z kůže nebo semiše, která dobře klouže po parketách. Latinskoamerické boty mají otevřenou špičku a vyšší podpatek, hodí se pro rumbu, sambu a podobné tance (dámské modely s otevřenou špičkou). '
          'Jazzové a street dance boty mají pružnou podrážku, často dělenou, a jsou určené pro dynamický pohyb. Taneční tenisky mají zpevněný střed a hodí se pro hip hop a aerobik. Při koupi rozhoduje druh tance a povrch sálu. '
          'Podpatek se u začátečníků volí nižší, aby se zvykla na rovnováhu. Podrážku semišových bot pravidelně čistěte drátěným kartáčem, aby neztratila přilnavost.</p>'
          '<h2>Taneční a baletní oblečení</h2>'
          '<p>Trikot je základ, na který se doplňuje sukýnka, bolerko nebo legíny. Dětem se doporučuje jednoduchý jednobarevný trikot s pohodlným střihem, ve škole baletu bývají určené barvy. Důležité je složení: bavlna je příjemná, ale u intenzivního pohybu nasákne potem, polyamid s elastanem drží tvar a rychle schne. '
          'Sukýnky se dělají z tylu, šifonu nebo pružného úpletu a krátké neoprenové varianty zahřejí svaly při tréninku. K tomu se hodí <a href="/leginy/">legíny</a>, <a href="/sportovni-sukne-a-saty/">sportovní sukně a šaty</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>. '
          'Dospělé zaujmou také funkční <a href="/sportovni-podprsenky/">sportovní podprsenky</a>. Střih nesmí škrtit, aby se dalo plně dýchat.</p>'
          '<h2>Gymnastické pomůcky</h2>'
          '<p>Moderní gymnastika používá pět základních předmětů: míč, stuhu, kruh (obruč), kužele a švihadlo. Kruhy se vyrábějí z plastu nebo dřeva, míče z gumy se vzorem, stuhy z hladkého saténu s tyčkou. '
          'Pro začátečníky stačí menší míč a kratší stuha, soutěžní vybavení musí odpovídat pravidlům federace. Sportovní gymnastika potřebuje žíněnky, kladiny, kruhy a hrazdy, které se instalují jen v bezpečném prostředí. '
          'Pro domácí cvičení jsou praktické skládací kladiny, žebřiny a nízké kladinky, které zvládnou i děti. Navazují <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>, <a href="/svihadla/">švihadla</a>, <a href="/trampoliny/">trampolíny</a> a <a href="/balancni-pomucky/">balanční pomůcky</a>.</p>'
          '<h3>Míče, stuhy, kruhy</h3>'
          '<p>Míč na moderní gymnastiku má průměr kolem dvaceti centimetrů a má být dostatečně pružný, aby se odrážel. Stuha se vybírá podle délky a váhy tyčky, začátečnice stačí kratší. Obruč má správný průměr, pokud sahá gymnastce přibližně k pasu. '
          'Výběr barev je často estetický, ale pro soutěže existují pravidla pro vzhled. Při trénincích se hodí odolnější a nenáročné na údržbu.</p>'
          '<h3>Kladiny, žíněnky, žebřiny</h3>'
          '<p>Domácí kladina musí být stabilní, protiskluzová a mít nastavitelnou výšku. Žíněnka chrání před pády a její tloušťka se volí podle disciplíny. Žebřiny se upevňují do zdi nebo se používají jako samostatně stojící. '
          'Při instalaci vždy dodržujte pokyny výrobce a zajistěte měkkou plochu pod náčiním. Děti cvičí pod dohledem dospělého.</p>'
          '<h2>Cvičební a rehabilitační míče</h2>'
          '<p>Velké míče o průměru 55 až 75 centimetrů slouží k sezení, protahování a posilování. Správná velikost míče závisí na výšce: při sezení mají být kolena zhruba v pravém úhlu. Nafukují se pomalu a mají protiskluzový povrch, aby bezpečně nesklouzly. '
          'Doplňují je <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/joga-a-podlozky/">podložky na jógu</a>, <a href="/pilates-pomucky/">pilates pomůcky</a> a <a href="/masazni-pomucky/">masážní pomůcky</a>, které pomohou při regeneraci po tréninku.</p>'
          '<h2>Výběr podle věku</h2>'
          + T(['Věk', 'Výbava', 'Na co dbát'], [
              ['Předškolní děti', 'cvičky, jednoduchý trikot, lehké náčiní', 'pohodlí, pružnost, snadné oblékání'],
              ['Školní věk', 'baletní obuv, trikot, stuha a míč', 'růst nohy, doporučení lektora'],
              ['Dorost a soutěžní tanečníci', 'specializovaná obuv, předepsané oblečení, soutěžní náčiní', 'pravidla federací, kvalita'],
              ['Dospělí začátečníci', 'taneční tenisky nebo jazzovky, legíny', 'podrážka, podpora nártu'],
              ['Rekreační cvičenci', 'míče, gumy, podložky', 'uložení doma, jednoduchá údržba']]) +
          '<h2>Velikost a pohodlí</h2>'
          '<p>Nohu měřte večer, kdy je největší, na papíře od paty ke špičce nejdelšího prstu. Porovnejte délku s tabulkou značky, protože taneční velikosti se obvykle liší od konfekčních bot. '
          'Piškoty a taneční boty mají sedět těsně, ale bez bolesti, a po několika hodinách se přizpůsobí. Trikot vybírejte podle výšky a obvodu hrudníku a boků, příliš malý trikot omezuje pohyb a příliš velký se nabírá a překáží. '
          'Děti rychle rostou, proto se rozměry kontrolují před každou sezónou.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Boty po tréninku vyvětrejte a nenechávejte zavřené v tašce, aby nezapáchaly a neplesnivěly.</li>'
          '<li>Plátěné cvičky lze prát v ruce, kožené jen otírat vlhkým hadříkem.</li>'
          '<li>Trikoty perte při nízké teplotě a bez aviváže, která zhoršuje pružnost materiálu.</li>'
          '<li>Stuhy a kruhy skladujte volně, aby se nedeformovaly, a nenechávejte je na slunci.</li>'
          '<li>Míče uchovávejte mírně nafouknuté, mimo radiátor a ostré hrany.</li></ul>'
          '<h2>Pro koho je kategorie</h2>'
          '<p>Pro rodiče dětí, které začínají s tancem nebo gymnastikou, pro lektory, kteří doplňují hodiny, pro školy a tělocvičny a pro dospělé, kteří se k pohybu vrací. Dobře ji využijí také kdo cvičí doma a hledá míč nebo podložku. '
          'Podobné pohybové aktivity pokrývají <a href="/joga-a-pilates/">jóga a pilates</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>. K tréninku se hodí i <a href="/sportovni-tasky/">sportovní tašky</a> na přenášení bot a oblečení.</p>'
          '<h2>První výbava do kroužku</h2>'
          '<p>Před nákupem se zeptejte lektora, jaké oblečení a obuv škola vyžaduje, protože mnoho kroužků předepisuje barvu trikotu nebo typ cviček. Základní sada pro dítě zahrnuje obuv, trikot nebo tričko s legínami, vlasovou gumičku a tašku. '
          'Další kusy se dokupují podle potřeby, například sukýnka na vystoupení, ponožky nebo teplá vrstva na rozcvičku. Pokud dítě zkouší více aktivit najednou, vyplatí se univerzální kusy, které použijete v tanci, gymnastice i při tělocviku. '
          'Na soutěže a vystoupení se oblečení pořizuje zvlášť, často ve spolupráci s trenérem nebo oddílem. V takovém případě ověřte termíny a velikosti s dostatečným předstihem.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejširší zastoupení mají ' + B(("domyos", "Domyos"), ("hms", "HMS"), ("sybai", "Sybai"), ("indigo-sports", "Indigo Sports"), ("papillon", "Papillon"), ("ledragomma", "Ledragomma"), ("lifefit", "Lifefit")) +
          '. Další nabídku mají ' + B(("insportline", "Insportline"), ("gymnic", "Gymnic"), ("eljet", "Eljet"), ("sedco", "Sedco"), ("rucanor", "Rucanor"), ("agama", "Agama"), ("gymbeam", "GymBeam"), ("decathlon", "Decathlon")) + '. '
          'Sybai je zaměřená na náčiní pro moderní gymnastiku, Papillon na taneční obuv a Domyos na cenově dostupnější sportovní výbavu pro děti a začátečníky. '
          'V kategorii se mohou objevit i obecné sportovní produkty, takže vždy hlídejte název a určení u konkrétního kusu.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Špičky bez konzultace s učitelem a bez řádného fitu.</li>'
          '<li>Příliš velké boty "na růst": taneční a baletní obuv musí padnout.</li>'
          '<li>Koupě soutěžního náčiní bez znalosti pravidel federace.</li>'
          '<li>Nevhodný materiál trikotu pro intenzivní trénink.</li>'
          '<li>Gymnastická kladina nebo hrazda bez měkkého dopadu a bez dozoru dospělého.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Nejprve určete disciplínu a velikost, potom porovnejte cenu, dostupnost a podmínky vrácení u několika obchodů. Obuv je citlivá na velikost, takže se vyplatí obchod s jednoduchou výměnou. Na Sportece uvidíte seřazené nabídky a snadno zjistíte, kde je vaše velikost skladem.</p>',
    faq=[
        ('Kdy dát dítěti první špičky?', 'Až když to doporučí učitel baletu, obvykle po několika letech tréninku a při dostatečné síle chodidel a lýtek. Příliš brzké špičky mohou poškodit nohu.'),
        ('Jak vybrat velikost baletních piškotů?', 'Změřte délku chodidla a porovnejte s tabulkou výrobce. Piškoty mají sedět těsně bez tlaku na prsty, protože se po několika hodinách mírně rozšlapou.'),
        ('Jaký je rozdíl mezi celou a dělenou podrážkou?', 'Celá podrážka je jednodušší a pevnější, dělená se skládá z dvou částí a lépe umožňuje protáhnout nárt. Volbu často doporučuje lektor.'),
        ('Jaká obuv se hodí pro společenské tance?', 'Obuv s jemnou koženou nebo semišovou podrážkou, která dobře klouže po parketách. Dámské boty mají podpatek, pánské nižší, a obě musí pevně držet nohu.'),
        ('Z čeho vybrat trikot na balet nebo gymnastiku?', 'Z elastického materiálu s polyamidem a elastanem, který drží tvar a schne. Bavlna je příjemná, ale při velkém pohybu nasákne potem.'),
        ('Jak vybrat velikost míče pro moderní gymnastiku?', 'Podle věku a kategorie. Začátečníci používají menší a lehčí míč, soutěžní velikosti určuje federace. Míč musí být dobře nafouknutý a pružný.'),
        ('Kterou kladinu koupit domů?', 'Stabilní, protiskluzovou, s nastavitelnou výškou a nosností odpovídající váze dítěte. Pod ni vždy položte měkkou žíněnku.'),
        ('Jak velký má být cvičební míč?', 'Při sezení mají být kolena přibližně v pravém úhlu. Pro dospělé o výšce 160 až 175 cm se používá nejčastěji míč o průměru kolem 65 cm, vždy ale zkontrolujte údaj výrobce.'),
        ('Jak prát taneční oblečení?', 'Při nižší teplotě, jemným prostředkem a bez aviváže. Sušte mimo radiátor a přímé slunce, aby si elastické materiály zachovaly pružnost.'),
        ('Jak se starat o taneční boty?', 'Po tréninku je vyvětrejte, podrážku čistěte kartáčem a nenechávejte boty na slunci. Kožené modely občas ošetřete a při opotřebení vyměňte.'),
        ('Co koupit dítěti do prvního tanečního kroužku?', 'Zeptejte se lektora na požadavky. Obvykle stačí pohodlná obuv, elastické oblečení, taška a gumička do vlasů, specializované kousky se dokupují až později.'),
        ('Jak často měnit taneční obuv u dětí?', 'Zpravidla jednou za sezónu nebo když dítěti povyroste noha. Kontrolujte, zda se prsty nedotýkají špičky a zda podrážka není opotřebovaná.'),
    ])
