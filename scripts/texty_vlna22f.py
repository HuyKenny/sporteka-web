"""sporteka.cz — wave 22f (4. 11. 2026): long texts (>= 1650 words) for lyzarske-kombinezy, bezecke-boty, bezecke-vesty-a-batohy, outdoor-doplnky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-kombinezy
NEW['lyzarske-kombinezy'] = dict(long=True,
    title='Lyžařské kombinézy a soupravy: děti, ženy, muži',
    desc='Lyžařské kombinézy, overaly a soupravy pro děti i dospělé. Jak vybrat velikost, zateplení a membránu a porovnat nabídky českých obchodů.',
    intro='<p>Jednodílná kombinéza je pro lyžování stvořená: žádná mezera mezi bundou a kalhotami, kudy by se při pádu dostal sníh k zádům, a oblékání zabere minutu. Proto ji rodiče volí hlavně pro menší děti, které padají, válejí se ve sněhu a nedokážou si ohlídat, aby měly v pase zasunuto. Dospělí ale sahají po kombinézách také, ať už kvůli klasickému retro vzhledu, nebo kvůli pohodlí na svahu a při běžkování.</p>'
          '<p>V kategorii najdete dětské overaly, dámské a pánské jednodílné modely, ale i dvoudílné <strong>lyžařské soupravy</strong>, tedy bundu s kalhotami prodávanou jako sladěný set. Sporteka porovnává nabídky obchodů u značek '
          + B(('didriksons', 'Didriksons'), ('helly-hansen', 'Helly Hansen'), ('2117-of-sweden', '2117 of Sweden'), ('slope', 'Slope'), ('whistler', 'Whistler'), ('kilpi', 'Kilpi'), ('scott', 'Scott'), ('reima', 'Reima')) +
          '. Pokud sháníte jednotlivé kusy, mrkněte do <a href="/lyzarske-bundy/">lyžařských bund</a> a <a href="/lyzarske-kalhoty/">lyžařských kalhot</a>.</p>',
    guide='<h2>Co všechno tu najdete</h2>'
          '<p>Pod jedním názvem najdete několik typů oblečení, které se při nákupu chovají odlišně, proto je dobré je rozlišit už při prvním pohledu na výpis.</p>'
          + T(['Typ', 'Charakter', 'Pro koho'], [
              ['Dětský overal', 'jeden kus, zip přes celé tělo, často s kapucí', 'batolata a děti do školního věku'],
              ['Dospělá kombinéza', 'jednodílná, často retro nebo sportovní střih', 'pohodlná jízda, focení, zábava na svahu'],
              ['Lyžařská souprava', 'bunda plus kalhoty se stejným vzorem', 'dospělí a větší děti, flexibilní vrstvení'],
              ['Běžkařská kombinéza', 'tenká, elastická, často softshell', 'rychlé tempo, běžecké tratě']]) +
          '<p>U dětí převládají jednodílné modely, ale najdete i dětské dvoudílné sety, zatímco u dospělých převládají soupravy. Jednodílné dospělé kombinézy jsou menšina, ale mají své fanoušky, kteří oceňují jednoduchost a to, že nic nesjíždí.</p>'
          '<h2>Kombinéza, nebo bunda s kalhotami</h2>'
          '<p>Rozhodnutí závisí hlavně na věku a způsobu lyžování. U nejmenších dětí vítězí kombinéza, protože se nemusí řešit zastrčení bundy a poklopec. U školáků už často stačí dvoudílný set, protože si děti umějí odložit vrchní vrstvu v bufetu nebo když je teplo. Dospělí si většinou ponechají dva kusy, aby po lyžování mohli vyměnit bundu za něco lehčího.</p>'
          '<ul><li><strong>Výhody kombinézy:</strong> utěsněné tělo, rychlé obléknutí, jedna věc na hlídání a žádné odhalené záda při předklonu.</li>'
          '<li><strong>Nevýhody kombinézy:</strong> složitější toaletní pauza, hůř se reguluje teplota a při zničení zipu je třeba řešit celý kus.</li>'
          '<li><strong>Výhody soupravy:</strong> lze měnit velikost bundy a kalhot zvlášť a po sezoně použít bundu na procházky.</li>'
          '<li><strong>Nevýhody soupravy:</strong> mezi kusy se může dostat sníh, pokud sedí špatně nebo chybí sněhová zástěra.</li></ul>'
          '<h2>Výběr velikosti u dětí</h2>'
          '<p>Dětské oblečení se vybírá podle výšky, nikoli podle věku, protože věk je jen orientační. Změřte dítě v ponožkách a porovnejte údaj s tabulkou výrobce, protože značky jako Reima, Didriksons nebo Mckinley mají střih trochu jiný. Počítejte s rezervou, v kombinéze se dítě musí pohodlně předklonit i dřepnout a pod ní má mít termoprádlo i fleece.</p>'
          '<p>Praktické jsou modely s prodloužitelnými rukávy a nohavicemi, které lze prodloužit nastavitelnou manžetou a vydrží druhou sezonu. Pozor ale na přehnané rezervy. Příliš dlouhá kombinéza brání v pohybu, o nohavice se zaklesnou boty a dítě zakopává. Čím menší dítě, tím víc záleží na tom, aby oblečení sedělo.</p>'
          '<h2>Velikost u dospělých</h2>'
          '<p>Dospělé kombinézy a soupravy se zkouší s oblečením, které budete na svahu nosit. Zkontrolujte délku rozkroku, protože u jednodílného kusu rozhoduje o pohodlí. Když je rozkrok příliš krátký, tahá vás při předklonu za ramena, když je příliš dlouhý, brání pohybu a nohavice padají do bot. Zvedněte ruce nad hlavu, dřepněte a předkloňte se, ať ověříte, že nic netahá.</p>'
          '<p>Dámské a pánské střihy se liší hlavně v bocích a délce rukávů. Unisex střihy bývají volnější a hodí se pro snowboardisty, kteří preferují uvolněný styl. Pro rychlejší carvingovou jízdu se víc hodí přiléhavější střih, který nešustí a nebrzdí vzduchem.</p>'
          '<h2>Membrána a vodní sloupec</h2>'
          '<p>Vodní sloupec udává, jak velký tlak vody látka vydrží, než začne propouštět. Čím vyšší hodnota, tím větší odolnost vůči mokrému sněhu, ale ještě důležitější je kvalita zpracování. I vynikající membrána selže, pokud švy nejsou přelepené a zipy nemají překrytí. V popisu produktů hledejte slova jako přelepené švy, odolný zip nebo sněhová zástěra.</p>'
          + T(['Vlastnost', 'K čemu slouží', 'Na co si dát pozor'], [
              ['Vodní sloupec', 'odolnost proti mokrému sněhu a dešti', 'vyšší hodnota znamená menší prodyšnost u levnějších materiálů'],
              ['Prodyšnost', 'odvod vlhkosti zevnitř', 'bez ní se dítě potí a následně mrzne'],
              ['Přelepené švy', 'zabraňují proniknutí vody dírkami po jehle', 'u rekreační jízdy stačí část švů, u deště všechny'],
              ['Sněhová zástěra', 'uzavírá spodní okraj bundy nebo nohavice', 'u kombinézy bývá vestavěná a pevná'],
              ['Zesílená kolena a zadek', 'odolnost proti oděru a vlhkosti', 'důležité pro děti a snowboardisty']]) +
          '<p>Dětem a rekreačním lyžařům postačí střední úroveň vodotěsnosti. Pokud často jezdíte při oblevě nebo se děti válejí v mokrém sněhu, zvolte vyšší odolnost a vždy se podívejte na prodyšnost. Nepromokavost bez prodyšnosti vede jen k tomu, že se potíte zevnitř.</p>'
          '<h2>Zateplení: peří, syntetika, fleece</h2>'
          '<p>Zateplení rozhoduje o tom, jak velkou vrstvu pod kombinézu potřebujete. Syntetická izolace se hodí pro děti, protože drží teplo i vlhká a snese praní. Peří je lehčí a lépe stlačitelné, ale u dětí a mokrého sněhu je méně praktické. Některé soupravy mají jen lehkou výplň a počítají s tím, že si pod ně obléknete fleece. Jiné mají silnou izolaci a hodí se do mrazu na stání u vleku.</p>'
          '<p>Nepodceňujte větrání. Zipy v podpaží a na stehnech umožní rychle odvětrat teplo při stoupání nebo při jízdě za slunce. U jednodílné kombinézy chybí možnost vyměnit vrstvu, takže vnitřní větrací otvory a prodyšná podšívka hrají důležitější roli než u dvoudílného oblečení.</p>'
          '<h2>Co obléknout pod kombinézu</h2>'
          '<p>Základem je funkční <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>, které odvádí pot od kůže. Pak přijde střední vrstva, třeba tenký fleece, a teprve nakonec kombinéza. Bavlněné tričko nahraďte syntetikou nebo merinem, jinak vlhkost zůstane u těla. Do toho patří i kvalitní <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, <a href="/lyzarske-rukavice/">rukavice</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>.</p>'
          '<p>U dětí raději vrstvěte tenčí kusy než jednu tlustou. Kdykoli dítě ochladne nebo se přehřeje, můžete jednu vrstvu sundat. Přilba má vždy patřit do základní výbavy, protože i na dětské sjezdovce se mohou stát srážky. Vhodnou si vyberete mezi <a href="/lyzarske-helmy/">lyžařskými helmami</a> a doplníte <a href="/lyzarske-bryle/">lyžařskými brýlemi</a>.</p>'
          '<h2>Funkce, které se vyplatí</h2>'
          '<ul><li><strong>Kapsa na skipas:</strong> ušetří hledání při průchodu turniketem. Nejlepší je s rukávovou kapsou.</li>'
          '<li><strong>Reflexní prvky:</strong> hodí se na večerní lyžování i na dětskou sjezdovku, kde je plno lidí.</li>'
          '<li><strong>Odepínací kapuce:</strong> dobrá pod přilbu i na procházku po svahu.</li>'
          '<li><strong>Zip s dvojitým jezdcem:</strong> usnadní toaletní pauzu a větrání u kombinézy.</li>'
          '<li><strong>Nastavitelné manžety:</strong> utěsní rukavice a zabrání dostání sněhu do rukávu.</li>'
          '<li><strong>Zesílená spodní hrana nohavice:</strong> ochrání látku před hranami lyží a snowboardových bot.</li></ul>'
          '<h2>Výběr podle aktivity</h2>'
          '<p>Na sjezdovém lyžování se hodí vodotěsné modely s prodyšnou vrstvou a zesíleným materiálem na kolenou. Snowboardisté oceňují volnější střih a vyztužený zadek, protože hodně sedí a padají na dřevo. Pro běžecké lyžování a skialpy je lepší lehká, elastická kombinéza z <em>softshellu</em>, v níž se dá rychle pohybovat. Taková kombinéza nahrazuje klasické zateplené oblečení, takže zvolte tu, která odpovídá vaší aktivitě a teplotám. Navazuje na ni <a href="/bezecke-lyzovani/">běžecké lyžování</a> s potřebnými botami a lyžemi.</p>'
          '<p>Pro prvňáčky a školky se hodí výrazné barvy, které rodiče snadno najdou na sjezdovce. Na vlek s dětmi navíc ocení kapsu na kapesníky nebo sladkost. Pro lyžařskou školu je užitečné oblečení bez volných popruhů, které se nemohou zachytit.</p>'
          '<h2>Péče o kombinézu</h2>'
          '<p>Praní provádějte přesně podle štítku, zpravidla na nízkou teplotu s tekutým prostředkem bez aviváže, která zalepí póry membrány. Po několika sezonách pomůže impregnace, aby se na povrchu opět tvořily kapky. Před uskladněním kombinézu dokonale usušte a ukládejte volně, ne stlačenou pod těžkými věcmi. Zipy občas očistěte měkkým kartáčkem, aby se do nich nezanášela špína a sůl.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě příliš velké kombinézy na růst. Bude překážet v pohybu a dítě zbytečně vyčerpá.</li>'
          '<li>Výběr jen podle vzhledu bez kontroly vodního sloupce a švů.</li>'
          '<li>Zapomenutí na termoprádlo. I nejlepší overal nebude hřát, když pod ním bude bavlna.</li>'
          '<li>Nezkoušení pohybu: zdvih rukou, dřep, předklon, krok do strany.</li>'
          '<li>Nákup soupravy, u které neodpovídá velikost bundy a kalhot, což vede k mezeře v pase.</li></ul>'
          '<h2>Kdy kombinézu nekupovat</h2>'
          '<p>Pokud lyžujete jen párkrát za zimu a půjčujete si vybavení, dostačí skromnější varianta. Kombinéza také nemusí být ideální pro dospívající, kteří chtějí vypadat jako ostatní a oblékají se po vrstvách. Rozhodněte se podle toho, kolik dní ročně budete ve sněhu trávit a jestli vám jednodílné řešení skutečně ulehčí den na horách.</p>'
          '<h2>Jak číst nabídku obchodů</h2>'
          '<p>Stejný model se v obchodech často objevuje s rozdílnou dostupností velikostí. U dětských kombinéz dochází nejrychleji střední velikosti, protože jich rodiče kupují nejvíc. Sporteka seskupuje nabídky téhož produktu, takže vidíte, kde je právě vaše velikost a jaká je doprava. Při porovnání ověřte, že jde o stejnou barevnou variantu, protože dostupnost velikostí se mezi variantami liší.</p>'
          '<p>Pokud kupujete na další sezonu, projděte si také <a href="/lyzarske-obleceni/">lyžařské a snowboardové oblečení</a>, kde najdete bundy, kalhoty i termoprádlo. A když ještě řešíte boty a lyže, pomůže vám <a href="/lyzarske-boty/">kategorie lyžařských bot</a> a <a href="/lyze-komplety/">lyžařské sady</a>.</p>',
    faq=[('Jakou kombinézu vybrat pro malé dítě?', 'Hledejte jednodílný overal podle výšky dítěte, s prodyšnou membránou, přelepenými švy, nastavitelnými manžetami a zesílenými koleny. Raději trochu volnější, ale ne příliš dlouhý.'),
         ('Jaký je rozdíl mezi kombinézou a lyžařskou soupravou?', 'Kombinéza je jednodílná, souprava se skládá z bundy a kalhot prodávaných společně. Souprava umožňuje lepší regulaci tepla a oddělenou výměnu velikostí.'),
         ('Je kombinéza vhodná i pro dospělé?', 'Ano, hodí se pro pohodlnou jízdu, retro styl nebo snowboard. Nevýhodou je složitější toaletní pauza a nižší možnost větrání.'),
         ('Jak poznám správnou velikost dětské kombinézy?', 'Změřte výšku dítěte a porovnejte ji s tabulkou výrobce. Zkoušejte s vrstvami, které bude mít pod ní, a ověřte předklon i dřep.'),
         ('Co obléknout pod lyžařskou kombinézu?', 'Funkční termoprádlo z umělých vláken nebo merina a lehký fleece. Bavlna drží vlhkost a rychle ochladí tělo.'),
         ('Na co se dívat u vodotěsnosti?', 'Na vodní sloupec, přelepené švy, kvalitní zipy a prodyšnost. Samotné číslo nestačí, rozhoduje zpracování.'),
         ('Jak kombinézu vyprat?', 'Podle štítku na nízkou teplotu a bez aviváže. Po několika sezonách ji obnovte impregnací určenou pro membrány a pořádně usušte.'),
         ('Hodí se kombinéza na běžky?', 'Ano, ale vybírejte tenčí, elastický a prodyšný model, často ze softshellu. Klasická zateplená lyžařská kombinéza by byla při tempu běžkování příliš teplá.'),
         ('Vydrží dětská kombinéza dvě sezony?', 'Pokud má prodloužitelné rukávy a nohavice a nebyla koupena příliš těsná, často ano. Rozhoduje, jak rychle dítě roste a jak se oblečení používá.'),
         ('Má smysl kupovat sladěný set pro celou rodinu?', 'Je to hlavně otázka vzhledu. Výhodou jsou výrazné barvy, ve kterých se rodina snadno najde na sjezdovce, ale důležitější je správný střih a funkce.')])

# ------------------------------------------------------------------ bezecke-boty
NEW['bezecke-boty'] = dict(long=True,
    title='Boty na běžky: klasika, skate a kombi, NNN i Prolink',
    desc='Boty na běžecké lyžování pro klasiku, bruslení i kombi. Jak vybrat systém vázání, velikost a zateplení a porovnat nabídky českých obchodů.',
    intro='<p>Kategorie <strong>boty na běžky</strong> neobsahuje běžecké tenisky, ale obuv určenou k zacvaknutí do vázání na běžeckých lyžích. Pokud hledáte boty na běhání po silnici nebo v terénu, pokračujte do <a href="/bezecka-obuv/">běžecké obuvi</a>, <a href="/silnicni-bezecke-boty/">silničních bot</a> nebo <a href="/trailove-boty/">trailových bot</a>.</p>'
          '<p>Pro zimní stopy tu najdete modely pro klasiku, bruslení i univerzální kombi, a to pánské, dámské i dětské. Sporteka porovnává nabídky obchodů u značek '
          + B(('alpina', 'Alpina'), ('fischer', 'Fischer'), ('rossignol', 'Rossignol'), ('madshus', 'Madshus'), ('salomon', 'Salomon'), ('inovik', 'Inovik')) +
          '. Než začnete vybírat, zjistěte, jaké vázání máte na lyžích, protože bota musí odpovídat systému. Teprve potom řešte velikost, zateplení a to, jestli chcete jezdit v upravené stopě, nebo po výletních cestách.</p>',
    guide='<h2>Jak je to s názvem a co tu je</h2>'
          '<p>V katalogu jde výhradně o boty pro běžecké lyžování. Slovo běžecké se tu pojí s lyžemi, nikoli s asfaltem. Obuv se zvenku podobá zimní botě, ale má specifickou špičku, která zapadá do vázání, a flexibilní nebo naopak tuhou podrážku podle stylu. Z velké části ji tvoří modely značky Alpina, následované Fischerem, Rossignolem, Madshusem a Salomonem.</p>'
          '<p>Najdete také cestovní nebo trekové boty pro stopy mimo upravené trati, které mají vyšší sklon a silnější izolaci. Hodí se pro lesní cesty, kde se nehoní tempo, ale užívá se krajina. Pokud plánujete spíš výlety než tréninky, hledejte označení touring nebo outdoor.</p>'
          '<h2>Klasika, skate a kombi</h2>'
          '<p>Nejdůležitější rozhodnutí je styl jízdy. Boty se pro každý z nich liší výškou, tuhostí i podrážkou, takže je nelze svobodně zaměňovat.</p>'
          + T(['Styl', 'Typ boty', 'Charakteristika'], [
              ['Klasika', 'nižší, pružná bota', 'volný pohyb v nártu a kotníku, krok v připravené stopě'],
              ['Skate (bruslení)', 'vyšší, tužší bota', 'opora kotníku, tuhá podešev, jízda po upravené trati'],
              ['Kombi', 'kompromis mezi oběma', 'rekreační jezdci, jeden pár na všechno'],
              ['Touring a outdoor', 'robustní, teplá, vyšší', 'výlety mimo stopu, lesní cesty, delší túry']]) +
          '<p>Klasická bota se ohýbá snáz, aby noha mohla odrazit. Skate bota má vyztuženou patu a zpevněný kotník, protože při bruslení noha pracuje do strany. Kombi bota pro oba styly míchá vlastnosti obou, a proto je pro začátečníky a příležitostné jezdce nejpraktičtější. Kdo trénuje rychlost nebo se chystá na závody, zvolí specializovanou botu.</p>'
          '<h2>Systém vázání: NNN, SNS a Prolink</h2>'
          '<p>Základem je shoda mezi botou a vázáním. Na trhu existuje několik systémů a ne všechny jsou vzájemně kompatibilní. NNN a Prolink se obvykle dají kombinovat, kdežto starší SNS je s nimi nekompatibilní, takže u konkrétní dvojice boty a vázání ověřte údaj výrobce. Nejčastěji se setkáte s <strong>NNN</strong> a jeho vývojem, dále se systémem <strong>Prolink</strong> značky Salomon a se zbytky staršího SNS. Informace najdete na botě, na vázání nebo v popisu produktu. U lyží si ji můžete ověřit v kategorii <a href="/bezecke-vazani/">běžecká vázání</a>.</p>'
          '<ul><li><strong>NNN:</strong> široce rozšířený systém se dvěma lištami ve špičce, používají ho Alpina, Fischer, Rossignol i Madshus.</li>'
          '<li><strong>Prolink:</strong> systém Salomonu, který se objevuje u bot značky Salomon a Atomic, na lyžích bývá kompatibilní s vybranými vázáními.</li>'
          '<li><strong>Kompatibilita:</strong> nespoléhejte se jen na vzhled. Zkontrolujte přesné označení a případně zkuste botu přímo na vázání.</li>'
          '<li><strong>Vázání s nastavením:</strong> některé platformy se dají měnit, ale bota musí mít stejný typ špičky.</li></ul>'
          '<p>Pokud kupujete lyže i boty najednou, začněte lyžemi a vázáním a bota vyberte podle nich. Připravené sety najdete v kategorii <a href="/lyze-komplety/">lyžařské komplety</a> a <a href="/bezecke-lyze/">běžecké lyže</a>.</p>'
          '<h2>Velikost a pohodlí</h2>'
          '<p>Při zkoušení stoupněte na obě nohy a zatlačte patu do zadní části. Špička nesmí tlačit a pata nesmí zvedat, když předkloníte koleno. Jedna až půl velikosti navíc je normální, pokud obujete teplejší běžeckou ponožku, ale větší rezerva způsobuje otlaky a ztrátu kontroly. Značky mají různé střihy: Alpina bývá širší, Fischer a Rossignol užší a závodní modely Madshus tvarem připomínají sportovní tenisku.</p>'
          '<p>Při online nákupu porovnávejte vnitřní délku stélky v centimetrech, kterou výrobce často uvádí. Pokud stojíte mezi dvěma velikostmi, vyberte tu, ve které si můžete pohodlně pohnout prsty a zároveň neklouže pata. U dětí vždy počítejte s růstem, ale nepřehánějte to, protože bota s velkou vůlí nedrží.</p>'
          '<h2>Zateplení, membrána a ponožky</h2>'
          '<p>Při pohybu se nohy zahřívají, ale při stání, pomalé jízdě nebo mrazu potřebují izolaci. Rekreační boty mívají vnitřní zateplení a odolnější materiál. Závodní modely jsou tenké a lehké, aby se noha nepotila a boty tolik nevážily. Některé mají membránu proti vlhkosti, ale membrána ale neznamená zateplení.</p>'
          '<p>Důležité je správně zvolit ponožky. Vyberte tenké až středně silné, ideálně s vlnou nebo syntetikou. V mnoha případech pomůže volnější sezení boty, protože ponožky tlačící v botě jsou častou příčinou chladu v nohou. Bavlněné ponožky se nehodí, drží vlhkost a rychle vychladnou. Vhodné modely najdete v <a href="/merino-ponozky/">merino ponožkách</a> a <a href="/sportovni-ponozky/">sportovních ponožkách</a>.</p>'
          '<h2>Výběr podle zkušeností</h2>'
          '<ul><li><strong>Začátečník:</strong> kombi bota s teplým vnitřkem a stabilním kotníkem, nejlépe v nabídce lyží a vázání jako komplet.</li>'
          '<li><strong>Rekreační jezdec:</strong> klasická nebo kombi bota pro víkendové vyjížďky v upravené stopě.</li>'
          '<li><strong>Sportovec:</strong> specializovaná skate nebo klasická bota podle disciplíny, lehčí a tužší.</li>'
          '<li><strong>Dítě:</strong> teplejší, nastavitelný model s jednoduchým zapínáním, aby si ho zvládlo obout samo.</li>'
          '<li><strong>Výlet mimo stopu:</strong> touring bota, která snese delší chůzi a mokrý sníh.</li></ul>'
          '<h2>Zapínání a konstrukce</h2>'
          '<p>Boty se zavazují klasickými tkaničkami, kombinací tkaniček a zipu nebo systémem rychlého zapínání. Tkaničky umožní jemné nastavení, ale na mrazu zamrzají. Rychlé zapínání ušetří čas, jenže při nepřesné velikosti ztrácí oporu. Zip drží boty u sebe a chrání před sněhem, ale kvůli němu musí být přes nárt dostatek místa. Kvalitní manžeta u kotníku je důležitá hlavně u skate, kde bota drží kotník při bočním zatížení.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po jízdě boty vysušte při pokojové teplotě, ne na topení, protože by se mohly deformovat. Vyndejte vložky, vytáhněte tkaničky a vyčistěte špičku od sněhu a zbytků nečistot, aby se vázání dobře zacvaklo i na další výlet. Pravidelně kontrolujte lištu ve špičce, poškozená špička způsobí, že bota neuchytí. Přes léto boty skladujte na suchém místě bez přímého slunce.</p>'
          '<p>Mokré boty nenechávejte v kufru auta ani v kapse batohu. Po návratu je vyjměte, vymáčkněte vlhkost a naplňte novinovým papírem. Zvýší se tím životnost materiálu i podešve a boty bez problémů vydrží několik sezon.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě bot bez kontroly vázání, které máte na lyžích.</li>'
          '<li>Výběr příliš tuhé skate boty pro klasický pohyb.</li>'
          '<li>Příliš velká velikost, která vede k puchýřům a ztrátě přenosu síly.</li>'
          '<li>Zkoušení bot v tenkých ponožkách a následné nošení tlustých.</li>'
          '<li>Nákup podle fotografie bez ohledu na to, že každá značka sedí jinak.</li>'
          '<li>Zanedbání zateplení u dětí, které se při pomalé jízdě rychle ochladí.</li></ul>'
          '<h2>Jak boty sedí při jízdě</h2>'
          '<p>Správně zvolená bota se pozná za první hodinu na trati. Pata drží na místě, prsty se mohou volně pohnout a nárt netlačí na jazyk. Pokud při odrazu cítíte, že se noha v botě posouvá dopředu, je bota příliš velká nebo špatně zavázaná. Když naopak brní prsty, nejspíš je příliš těsná nebo ponožka příliš silná. U klasiky je důležitá pružnost podrážky pod prsty, u bruslení pevné držení pod kotníkem.</p>'
          '<p>Před koupí si uvědomte, že boty se při zahřátí nohy trochu roztáhnou, ale nikdy tolik, aby se ztráta velikosti vyrovnala. Zkoušejte je odpoledne, kdy je noha mírně oteklá, a pohybujte se v nich po obchodě. Dvojí zavázání a zalomení jazyka pomůže zabránit tlaku na nárt. Když máte široké chodidlo nebo vysoký nárt, začněte u modelů značek, které mají širší kopyto, a neváhejte si pár kusů porovnat.</p>'
          '<h2>Dětské a juniorské boty</h2>'
          '<p>Dětské boty bývají jednodušší a teplejší než dospělé a často se zapínají zipem nebo suchým zipem. Děti rostou rychle, proto je rozumné koupit botu s malou rezervou a přidat druhou stélku nebo silnější ponožku. Důležitá je podrážka, která drží vázání, a opora kotníku, aby dítě mělo jistotu při prvních pokusech. Starší děti, které trénují v oddílu, často přecházejí na dospělé velikosti a specializované modely.</p>'
          '<p>Boty pro děti vyberte spolu s lyžemi a hůlkami z kategorie <a href="/lyze-komplety/">lyžařských kompletů</a>. Zeptejte se v klubu nebo v půjčovně, které systémy používají, ať se nemusíte potýkat s nekompatibilitou. Pokud dítě jezdí jen pár dní za zimu, je vhodná sada s jednoduchým vázáním a botou, kterou zvládne obout bez pomoci.</p>'
          '<h2>Kdy boty vyměnit</h2>'
          '<p>Botu je třeba vyměnit, když je podrážka rozpadlá nebo odlepená, prasklá špička nebo nesedí do vázání tak pevně jako dřív. Sledujte také vnitřní vložku, která se časem slisuje a přestane hřát. Pokud vám studnou nohy i v dobře zvolených ponožkách, může být příčinou zničená izolace nebo mokrý materiál. Při nejistotě nechte boty zkontrolovat v servisu, kde posoudí stav špičky a podešve a doporučí opravu nebo nákup nového páru. Staré boty nevyhazujte hned, někdy stačí vyměnit vložky nebo tkaničky a ušetříte.</p>'
          '<h2>Co dál k lyžím</h2>'
          '<p>K botám patří lyže, vázání a hole, případně vosk. Další informace najdete v kategorii <a href="/bezecke-lyzovani/">běžecké lyžování</a>, v lyžařských <a href="/lyzarske-vosky/">voscích</a> a v lyžařském oblečení, třeba <a href="/lyzarske-termopradlo/">termoprádle</a> a <a href="/lyzarske-rukavice/">rukavicích</a>. Pro dlouhé túry se hodí také <a href="/bezecke-opasky/">běžecký opasek</a> a <a href="/bezecke-vesty-a-batohy/">vesta nebo batoh</a>, do kterého uložíte lahev s teplým čajem.</p>',
    faq=[('Jsou boty na běžky stejné jako běžecké tenisky?', 'Ne. Jsou to boty se špičkou přizpůsobenou vázání na běžeckých lyžích. Na běhání po silnici nebo v terénu se nehodí.'),
         ('Jak poznám, jaké vázání mám na lyžích?', 'Najdete ho na vázání, na lyžích nebo v popisu výrobku. Nejčastěji jde o NNN nebo Prolink. Bota musí odpovídat vázání; NNN a Prolink se obvykle kombinovat dají, starší SNS ne.'),
         ('Jaký je rozdíl mezi klasickou a skate botou?', 'Klasická bota je nižší a pružnější, skate bota je vyšší a tužší s oporou kotníku. Kombi bota spojuje obojí a hodí se rekreačním jezdcům.'),
         ('Jaká velikost bot na běžky je správná?', 'Taková, ve které pata nezvedá, špička netlačí a máte místo na tenkou až středně silnou ponožku. U online nákupu porovnávejte délku stélky.'),
         ('Mám koupit kombi, nebo specializovanou botu?', 'Pro rekreaci a začátky stačí kombi. Specializovanou botu ocení ti, kdo jezdí převážně jedním stylem a řeší výkon.'),
         ('Jaké ponožky se hodí do bot na běžky?', 'Tenké až střední z vlny nebo syntetiky. Bavlna není vhodná, protože drží vlhkost.'),
         ('Hodí se boty na běžky i pro pěší výlety?', 'Touring modely ano, ale jsou určeny hlavně pro pohyb na lyžích. Pro delší chůzi bez lyží zvolte turistickou obuv.'),
         ('Jak o boty pečovat?', 'Vysušte je při pokojové teplotě, vyčistěte špičku od sněhu a pravidelně kontrolujte lištu. Neskladujte je u radiátoru.'),
         ('Kdy volit teplejší boty?', 'Při pomalé jízdě, mrazu, stání u stopy a u dětí. Při sportovním tempu stačí tenčí závodní model.'),
         ('Vybírám boty pro dítě. Na co se zaměřit?', 'Na snadné obouvání, teplé vnitřní zateplení, dostatečnou oporu kotníku a vázání, které odpovídá lyžím.')])

# ------------------------------------------------------------------ bezecke-vesty-a-batohy
NEW['bezecke-vesty-a-batohy'] = dict(long=True,
    title='Běžecké vesty a batohy: objem, hydratace, velikost',
    desc='Běžecké vesty a batohy na trail, ultra i běžné běhání. Jak vybrat objem, uložení vody, velikost a porovnat nabídky českých obchodů.',
    intro='<p>Na kratší běh se obejdete bez zavazadla, jenže jakmile se vydáte na delší trail, do hor nebo na dlouhé tréninky, potřebujete vodu, jídlo, větrovku a telefon po ruce. Běžecká vesta nebo malý batoh drží náklad těsně na těle, aby se nehoupal a neodíral. Na rozdíl od klasických turistických zavazadel jsou běžecké vesty menší, přiléhavé a počítají s rychlým pohybem.</p>'
          '<p>V kategorii najdete vesty s měkkými lahvemi vpředu, malé běžecké batohy, hydratační vaky, ale i drobnosti, třeba pásky a doplňky; reflexní bezpečnostní vesty pro běh za tmy jsou jiný typ výrobku než hydratační vesta a slouží hlavně k viditelnosti. Ve výběru jsou značky '
          + B(('salomon', 'Salomon'), ('dynafit', 'Dynafit'), ('deuter', 'Deuter'), ('camelbak', 'Camelbak'), ('silva', 'Silva'), ('on', 'On'), ('compressport', 'Compressport'), ('adidas', 'Adidas')) +
          '. Sporteka porovnává nabídky českých obchodů, takže snadno najdete konkrétní velikost a barvu. Pro základ vybavení se podívejte i na <a href="/bezecka-obuv/">běžeckou obuv</a> a <a href="/bezecke-opasky/">běžecké opasky</a>.</p>',
    guide='<h2>Co tu najdete</h2>'
          '<p>Kategorie sdružuje několik typů výrobků, které spojuje to, že se nosí při běhání. Rozdíly jsou důležité, protože správná volba závisí na délce trasy, počtu věcí a na tom, jestli vám vadí, když se vám něco pohybuje na zádech.</p>'
          + T(['Typ', 'Popis', 'Pro koho'], [
              ['Hydratační vesta', 'obepíná trup, lahve nebo vak vpředu a vzadu', 'trail, ultra, dlouhé tréninky'],
              ['Běžecký batoh', 'malý batoh s popruhy a hrudním pásem', 'běžci, kteří vozí víc věcí'],
              ['Lehká vesta bez lahví', 'minimální kapsy na telefon, gely a klíče', 'kratší trasy, závody, město'],
              ['Hydratační vak', 'rezervoár s hadičkou do vesty nebo batohu', 'pití bez zastavení'],
              ['Zátěžová vesta', 'vesta s přidanou váhou pro trénink', 'silový nebo vytrvalostní trénink, ne pro delší trasy']]) +
          '<p>V nabídce se objevují i modely značky Silva, které jsou známé hlavně z navigace a orientačního běhu, a vesty Dynafit a Salomon určené pro hory a trail. Deuter a Camelbak mají v sortimentu lehké batohy, které přesahují do turistiky a kola, ale na běhání jsou stejně vhodné.</p>'
          '<h2>Vesta, nebo batoh</h2>'
          '<p>Vesta sedí blíž k tělu a rozkládá váhu po hrudi a zádech. Obvykle má kapsy vpředu na lahve a gely, takže se nemusíte zastavovat a sundavat ji. Batoh je jednodušší, pojme víc objemu a má pevnější záda, ale víc se pohybuje a hůř odvětrává. Pokud nosíte jen vodu, jídlo a telefon, zvolte vestu. Pokud vozíte větší bundu, náhradní oblečení a výbavu na celodenní výlet, může se hodit batoh.</p>'
          '<ul><li><strong>Vesta:</strong> menší hmotnost na těle, snadný přístup, těsné přilnutí.</li>'
          '<li><strong>Batoh:</strong> větší objem, pevnější záda, lepší pro vození více věcí.</li>'
          '<li><strong>Kombinace:</strong> některé lehké batohy s hrudním pásem se chovají jako vesta a spojují výhody obou.</li></ul>'
          '<h2>Objem v litrech</h2>'
          '<p>Objem se udává v litrech a pro orientaci se dělí podle délky aktivity. Čím delší běh a čím horší počasí, tím víc výbavy potřebujete. Zbytečně velký objem ale znamená, že se věci pohybují, takže vždy vybírejte nejmenší, který pokryje vaše potřeby.</p>'
          + T(['Objem', 'Typické použití', 'Co se vejde'], [
              ['Do 5 l', 'běžný trénink, kratší závody', 'telefon, klíče, gely, malá lahev'],
              ['5–8 l', 'trail na několik hodin', 'voda, jídlo, tenká větrovka, čelovka'],
              ['8–12 l', 'dlouhý trail, hory', 'bunda, vrstva navíc, lékárnička, jídlo na celý den'],
              ['Nad 12 l', 'ultra a delší výpravy', 'povinná výbava závodu, více oblečení a jídla']]) +
          '<p>Mnoho závodů v horách předepisuje povinnou výbavu, například bundu, čelovku, píšťalku a folii. Před závodem se podívejte do propozic a vyberte vestu, do které se všechno spolehlivě vejde, aby vás nepřekvapil nedostatek místa.</p>'
          '<h2>Hydratace: lahve, vak, nebo oboje</h2>'
          '<p>Do vest se pití ukládá dvěma způsoby. Měkké lahve do předních kapes jsou nenápadné, snadno se doplňují a vidíte, kolik tekutiny zbývá. Vak s hadičkou umožní pít bez zastavení a pojme víc, ale hůř se čistí a hůř se sleduje stav. Mnoho vest nabízí obě možnosti. Rozhodněte se podle délky tras a toho, jak často se budete moci doplnit.</p>'
          '<p>Lahve a vaky se prodávají zvlášť, někdy jsou součástí balení, jindy ne, takže si v popisu ověřte, co koupíte. Zajímat vás mohou i <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a> nebo <a href="/lahve-a-termosky/">lahve a termosky</a>. Na dlouhé výpravy se hodí také <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>, vždy ale pamatujte, že jídlo a pití mají odpovídat vaší toleranci a zkušenosti.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Vesty se vybírají podle obvodu hrudníku a ne podle konfekční velikosti oblečení. Změřte hrudník těsně pod podpažím a porovnejte údaj s tabulkou výrobce. Dámské modely mají kratší záda a upravená ramena, protože se musí vyrovnat s jiným tvarem hrudníku. Pokud jste na hranici dvou velikostí, vybírejte podle toho, jak moc budete nosit a zda máte pod ní tlustší vrstvu.</p>'
          '<p>Při zkoušení naplňte vestu vodou, aby se chovala jako při běhu. Seskákejte pár kroků a ověřte, že se nehýbe a nedře. Hrudní pásy i boční stahování se dají nastavit, ale pokud vesta vyžaduje extrémní utažení, je pravděpodobně nevhodná velikost. Výběr bývá otázkou pohodlí, takže dejte přednost vestě, na kterou si zvyknete.</p>'
          '<h2>Rozložení kapes</h2>'
          '<p>Dobrá vesta má kapsy rozmístěné logicky: vpředu na lahve a rychlé jídlo, na hrudi telefon, vzadu hlavní oddíl na bundu. Boční kapsy a gumové šňůry na hole nebo bundu zvyšují praktičnost. Ověřte, že se vám telefon vejde bez zápasení, a pokud nosíte hole, vyberte model s úchyty. Zipy by měly být lehce ovladatelné jednou rukou a klíče mají mít bezpečnou kapsu s karabinou.</p>'
          '<ul><li><strong>Přední kapsy na lahve:</strong> zkontrolujte, zda lahev snadno vytáhnete i vrátíte za běhu.</li>'
          '<li><strong>Hlavní oddíl:</strong> pojme větrovku, náhradní vrstvu a lékárničku.</li>'
          '<li><strong>Zipová kapsa:</strong> pro doklady a klíče.</li>'
          '<li><strong>Úchyty na hole:</strong> důležité pro horské závody.</li>'
          '<li><strong>Reflexní prvky:</strong> užitečné při večerním a ranním běhání.</li></ul>'
          '<h2>Materiály a komfort</h2>'
          '<p>Většina vest je ze síťoviny a lehkého nylonu, které prodyšně sedí na těle. Měkké elastické popruhy se přizpůsobí pohybu hrudníku při dýchání. Ve vlhku a pocení se mohou objevit otlaky, hlavně pod rameny a na boku. Pomůže tričko bez švů, případně vazelína na místa tření. Pro chladnější dny doplňte vrstvu z kategorie <a href="/lyzarske-termopradlo/">termoprádla</a> nebo jiného funkčního oblečení pod vestu.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<ul><li><strong>Silniční a městský běh:</strong> lehká vesta nebo opasek, který pojme klíče a telefon. Podívejte se do <a href="/silnicni-bezecke-boty/">silničních bot</a> a opasků.</li>'
          '<li><strong>Trail a hory:</strong> hydratační vesta s kapsami vpředu a prostorem na bundu. K tomu patří <a href="/trailove-boty/">trailové boty</a>.</li>'
          '<li><strong>Ultra:</strong> větší vesta s úchyty na hole a dostatkem místa na jídlo a vrstvy.</li>'
          '<li><strong>Běžky:</strong> malá vesta nebo batoh s izolovanou lahví, protože voda v mrazu tuhne. Podpoří vás <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</li>'
          '<li><strong>Turistika s během:</strong> lehký batoh, který se dá použít i na procházky. Další možnosti najdete v <a href="/turisticke-batohy/">turistických batozích</a>.</li></ul>'
          '<h2>Zátěžové vesty a navigace</h2>'
          '<p>Mezi zbožím se vyskytují také zátěžové vesty s kovovými závažími, které slouží jako tréninkový doplněk pro silový nebo kondiční trénink. Na dlouhé běhy se nehodí, protože zvyšují zátěž kloubů a nemají kapsy na pití. Silva zase nabízí vesty spojené s orientačním během, kde se nosí buzola, mapa a čelovka. Přečtěte si pozorně název produktu, ať víte, jestli kupujete vestu na pití, vestu k orientaci, nebo trénink se zátěží.</p>'
          '<p>Ke každé vestě se hodí i <a href="/sportovni-hodinky/">sportovní hodinky</a> pro sledování tempa a trasy a <a href="/celovky-a-svitilny/">čelovka</a> pro ranní a večerní trasy. Nezapomeňte také na <a href="/powerbanky-a-nabijeni/">powerbanku</a> při delších závodech a výpravách.</p>'
          '<h2>Jak vestu nastavit</h2>'
          '<p>Nejdřív povolte všechny popruhy, oblečte vestu a utáhněte hrudní pásy tak, aby seděla pevně, ale dýchání zůstalo volné. Pak dotáhněte boční stahování, dokud se vesta nehýbe při chůzi. Těžší věci uložte blíž k tělu a doprostřed zad, lehké dopředu. Jakmile se objem lahví během běhu zmenší, vesta se uvolní, a tak ji občas znovu dotáhněte.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Po použití vestu vyvěste, aby proschla. Pot a sladké nápoje v kapsách způsobují zápach, a tak ji občas vyperte v ruce nebo v jemném cyklu podle štítku. Nepoužívejte aviváž, která poškodí síťovinu a zip. Hydratační vak po každém použití propláchněte a nechte oschnout otevřený, nejlépe zavěšený. Lahve čistěte kartáčkem a občas je vydezinfikujte prostředkem určeným na hydratační vaky a lahve. Věci v kapsách nehromaďte, protože těžká vesta se nepříjemně pohybuje.</p>'
          '<h2>Jak vestu zabalit</h2>'
          '<p>Těžké věci, jako je voda ve vaku nebo náhradní vrstva, patří doprostřed zad blízko k tělu. Jídlo a gely dejte do předních kapes, kde na ně dosáhnete bez zastavení. Bundu srolujte do úzkého válce, aby nezabírala místo, a telefon uložte tak, aby se nehoupal. Před delším během vyzkoušejte celé zabalení na krátké trase, abyste odhalili místa, kde se věci pohybují nebo tlačí. Upravte pak popruhy a přesuňte těžší kousky níž, dokud vesta nesedí jako přilepená. Při dalším běhu ověřte, že nic netře a že se k lahvím dostanete bez nepohodlí.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš velká vesta, ve které se věci houpou.</li>'
          '<li>Nezkoušení s plnými lahvemi, takže vesta po přidání váhy tře.</li>'
          '<li>Koupě podle designu bez kontroly počtu a polohy kapes.</li>'
          '<li>Podcenění objemu před horským závodem s povinnou výbavou.</li>'
          '<li>Použití bavlněného trika pod vestou, které se v ní otírá a nasákne potem.</li></ul>',
    faq=[('Jaký objem běžecké vesty zvolit?', 'Na běžné tréninky stačí kolem 5 litrů, na horský trail několik hodin přibližně 8 litrů a na dlouhé výpravy víc. Vybírejte nejmenší objem, který pokryje vaše potřeby.'),
         ('Je lepší vesta, nebo běžecký batoh?', 'Vesta sedí těsněji a nabízí rychlý přístup k pití. Batoh pojme víc, ale víc se pohybuje. Pro delší běhy v horách bývá praktičtější vesta.'),
         ('Jaké pití se do vesty hodí, lahve, nebo vak?', 'Měkké lahve se snadno doplňují a vidíte stav. Vak umožní pít bez zastavení, ale hůř se čistí. Mnoho vest zvládne obojí.'),
         ('Jak změřit velikost vesty?', 'Změřte obvod hrudníku pod podpažím a porovnejte s tabulkou výrobce. Vesta má sedět pevně, ale nesmí omezovat dýchání.'),
         ('Co všechno vozit na dlouhém běhu v horách?', 'Pití, jídlo, větrovku, telefon, čelovku a případně lékárničku. Přesný seznam závisí na počasí, délce trasy a pravidlech závodu.'),
         ('Hodí se vesta i na běžky?', 'Ano, ale pamatujte, že voda v mrazu tuhne. Vezměte izolovanou lahev nebo teplý nápoj a noste ji blíž k tělu.'),
         ('Jak vestu vyprat?', 'Podle štítku, nejčastěji ručně nebo v jemném cyklu bez aviváže. Poté ji nechte uschnout zavěšenou mimo přímé teplo.'),
         ('Co jsou zátěžové vesty a hodí se na trail?', 'Jsou to vesty s přidanou váhou pro silový trénink. Na dlouhé běhy se nehodí a nemají kapsy na pití.'),
         ('Jak předejít otlakům od vesty?', 'Vyberte správnou velikost, noste funkční tričko bez výrazných švů a v případě potřeby použijte krém proti tření. Ujistěte se, že je vesta správně nastavená.'),
         ('Mohu vestu použít i na turistiku nebo kolo?', 'Ano, pokud potřebujete lehké zavazadlo bez velkého objemu. Na delší výlety s těžší výbavou je lepší klasický batoh.')])

# ------------------------------------------------------------------ outdoor-doplnky
NEW['outdoor-doplnky'] = dict(long=True,
    title='Outdoorové doplňky: pouzdra, cestovní a kempové drobnosti',
    desc='Outdoorové doplňky: modulární pouzdra, popruhy, zámky, kryty batohů, cestovní hygiena a kempové nádobí. Porovnejte nabídky českých obchodů.',
    intro='<p>Outdoorové doplňky nejsou jeden druh zboží, ale sbírka drobností, které z turistiky, cestování a kempování dělají pohodlnější a organizovanější zážitek. Najdete tu modulární pouzdra a kapsy na batoh, popruhy a opasky, kombinační zámky, pláštěnky na batohy, cestovní lahvičky, prací plátky, kempový hrnek i drobné pomůcky do koupelny. Společné mají to, že jsou malé, lehké a řeší konkrétní nepříjemnost.</p>'
          '<p>Nabídka se opírá o tři značky: '
          + B(('tasmanian-tiger', 'Tasmanian Tiger'), ('lifeventure', 'LifeVenture'), ('travel-safe', 'Travel Safe')) +
          '. Tasmanian Tiger přináší taktický a modulární styl, LifeVenture cestovní a kempové vybavení a Travel Safe malé pomůcky pro cesty. Sporteka porovnává nabídky obchodů, takže snadno najdete konkrétní kus. Větší vybavení najdete v <a href="/turisticke-batohy/">turistických batozích</a>, <a href="/turisticke-stany/">stanech</a> a <a href="/kemping/">kempingu</a>.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Kategorie je smíšená, takže je užitečné ji rozdělit podle účelu. Při výběru se pak můžete soustředit na to, co skutečně potřebujete, místo abyste procházeli celý seznam.</p>'
          + T(['Skupina', 'Příklady', 'K čemu slouží'], [
              ['Modulární pouzdra a kapsy', 'pouzdra na rádio, brýle, doklady, malé kapsy', 'organizace výbavy na opasku nebo batohu'],
              ['Popruhy a opasky', 'popruh, modulární opasek, stahovací pásy', 'upevnění nákladu a nošení výbavy'],
              ['Ochrana batohu a zavazadel', 'pláštěnky na batoh, vodotěsné pytle, zámky', 'ochrana před deštěm a krádeží'],
              ['Cestovní hygiena', 'dávkovací lahve, prací plátky, gely, věšák', 'čistota na cestách a v kempu'],
              ['Kempové a cestovní nádobí', 'termokrus, drobné nádobí', 'pití a jídlo mimo domov']]) +
          '<p>Tasmanian Tiger tvoří největší část kategorie. Značka je spojená s taktickým stylem a systémem MOLLE, lidově řečeno popruhovým systémem na batozích. LifeVenture se věnuje cestovním a kempingovým drobnostem. Travel Safe nabízí hlavně praktické pomůcky pro cesty, třeba kryty na zavazadla a sady lahviček.</p>'
          '<h2>Modulární pouzdra a systém MOLLE</h2>'
          '<p>Modulární systém znamená, že pouzdra mají na zadní straně popruhy, kterými se prostrčí do poutek na batohu, opasku nebo vestě. Díky tomu lze výbavu přeskupovat podle výletu. Pouzdro na rádio, na brýle nebo na malou lékárničku si připnete tam, kde se vám nejlépe sahá. Menší kapsy na doklady a drobnosti ulehčí přístup k věcem, které nechcete hledat na dně batohu.</p>'
          '<ul><li><strong>Velikost pouzdra:</strong> vyberte podle věcí, které chcete nosit. Příliš velké pouzdro zbytečně vyčnívá.</li>'
          '<li><strong>Způsob uchycení:</strong> zkontrolujte, zda se hodí pro váš batoh, opasek nebo vestu.</li>'
          '<li><strong>Materiál:</strong> odolný nylon snese oděr a vlhkost, ale vodotěsnost nečekejte u každého modelu.</li>'
          '<li><strong>Zapínání:</strong> zip, suchý zip nebo patent. Při práci v rukavicích je nejjednodušší zip s oušky.</li>'
          '<li><strong>Barva:</strong> olivová, khaki a hnědá se hodí do přírody, černá se hodí ke každému oblečení.</li></ul>'
          '<h2>Opasky a popruhy</h2>'
          '<p>Modulární opasek je pevný pás s poutky, na který se věší pouzdra a další výbava. Pomáhá rozložit váhu a drží věci blízko těla. Popruh o šířce několika milimetrů se hodí na stahování batohu, spacáku nebo karimatky a ve městě třeba na zajištění zavazadla. Při výběru sledujte šířku, délku a způsob zapínání. Plastová spona je lehká, kovová pevnější, ale těžší.</p>'
          '<h2>Pláštěnky na batoh a vodotěsné pytle</h2>'
          '<p>Pláštěnka na batoh je lehký kryt s pružným okrajem, který přetáhnete přes celý batoh. Ochrání ho před deštěm a blátem. Hodí se i na letišti, kde zabrání zachycení popruhů o dopravní pásy. Velikost se vybírá podle objemu batohu, takže si ověřte litry. Pytle typu dry bag mají rolovací uzávěr a chrání věci i v případě, že batoh promokne. Používají se při kajaku, na kole nebo v dešti, a hodí se pro elektroniku a spací oblečení.</p>'
          '<p>Tyto pomůcky nenahrazují kvalitní batoh, ale doplňují ho. Nejlepší ochranu poskytuje kombinace vodotěsného vaku uvnitř a krytu zvenku. Další možnosti najdete také v kategorii <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>'
          '<h2>Zámky a bezpečnost zavazadel</h2>'
          '<p>Kombinační zámek se hodí na batoh, kufr, skříňku v šatně nebo hostelový locker. Číselný kód nevyžaduje klíč, který se může ztratit. Některé modely mají označení TSA, které umožňuje kontrolním orgánům otevřít zámek bez poškození. Nepovažujte zámek za ochranu před profesionálním zlodějem, ale spíše za překážku, která odradí příležitostné krádeže. Kód si nepište na telefon ve zjevné podobě a nepoužívejte datum narození.</p>'
          '<h2>Cestovní hygiena a drobnosti</h2>'
          '<p>V kategorii jsou i kapesní sady, které se hodí na pěší túru, víkendový výlet nebo dovolenou. Dávkovací lahvičky umožní přenášet šampon, krém nebo gel v malých objemech, aniž byste vozili celé balení. Prací plátky usnadní vyprání ponožek a spodního prádla v kempu. Cestovní věšák a zátka do umyvadla se hodí ve stísněném pokoji hostelu. Obdobné věci platí pro osušky: lehké, rychleschnoucí modely se skládají do malého balíčku.</p>'
          '<ul><li><strong>Lahvičky:</strong> vybírejte pevné, nepropustné a s víčkem, které se nepovolí.</li>'
          '<li><strong>Prací plátky:</strong> lehké a úsporné, ale zkontrolujte kompatibilitu s tvrdou vodou.</li>'
          '<li><strong>Rychleschnoucí ručník:</strong> vhodný na cesty a do kempu.</li>'
          '<li><strong>Čisticí gely:</strong> užitečné, ale nenahrazují mytí vodou a mýdlem, pokud je k dispozici.</li></ul>'
          '<h2>Kempové pití a nádobí</h2>'
          '<p>Termokrus nebo malý hrnek se hodí k ranní kávě ve stanu i na lavičce u chaty. Dvojitá stěna drží nápoj déle teplý a chrání ruce. Víčko zabrání rozlití v batohu. Podrobnější nabídku najdete v kategoriích <a href="/lahve-a-termosky/">lahve a termosky</a> a <a href="/kempingove-nadobi/">kempingové nádobí</a>. U potravin a jídla pomůže <a href="/outdoorova-strava/">outdoorová strava</a>.</p>'
          '<h2>Jak vybrat kvalitní kus</h2>'
          '<p>U drobných doplňků se kvalita pozná podle švů, zipů a použitého materiálu. Zkontrolujte, zda jsou švy zesílené v místech zatížení a zda zip nezadrhává. Nylon bývá označen údajem o hustotě vlákna, vyšší hodnota obvykle znamená odolnější tkaninu. Při koupi popruhů ověřte nosnost, u zámků jejich konstrukci a u hygienických pomůcek materiál lahviček. Mnohem víc než značka rozhoduje to, zda doplněk odpovídá vašemu použití a zda ho budete skutečně brát s sebou.</p>'
          '<p>Praktická je také barva. Výrazné pouzdro se v tmavém batohu snáze najde, zatímco tlumená khaki splyne s oblečením. U společných výletů se vyplatí sjednotit značení, například označit pytle s oblečením a jídlem různými barvami. Dobře uspořádané doplňky ušetří čas při rozbalování a pomáhají udržet pořádek ve stanu.</p>'
          '<h2>Výběr podle typu výletu</h2>'
          '<ul><li><strong>Jednodenní výlet:</strong> malé pouzdro na doklady a telefon, pláštěnka na batoh a drobné hygienické potřeby.</li>'
          '<li><strong>Víkend v kempu:</strong> termokrus, prací plátky, lahvičky a vodotěsný pytel na oblečení. Kombinujte se <a href="/kempingove-doplnky/">kempingovými doplňky</a>.</li>'
          '<li><strong>Cestování letadlem:</strong> kombinační zámek, obal na batoh, dávkovací lahvičky v povoleném objemu.</li>'
          '<li><strong>Taktický nebo airsoftový styl:</strong> modulární opasek, pouzdra a popruhy. Další výbavu najdete v <a href="/outdoorove-noze-a-multitoola/">nožích a multitoolech</a>.</li>'
          '<li><strong>Trekking:</strong> lehké pouzdro na brýle, popruh na stažení spacáku a krytí batohu, spolu s <a href="/celovky-a-svitilny/">čelovkou</a>.</li></ul>'
          '<h2>Jak doplňky zabalit</h2>'
          '<p>Nejtěžší věci patří blízko zad a ve výšce lopatek, lehké a objemné dolů a nahoru. Pouzdra s často potřebnými věcmi připněte na popruhy nebo na bok. Vodotěsné pytle rozdělte podle účelu, oblečení zvlášť, jídlo zvlášť, a barevně je rozlište, ať nemusíte hledat. Na cesty letadlem si ověřte pravidla dopravce týkající se tekutin a zámků.</p>'
          '<h2>Doplňky a předpisy na cestách</h2>'
          '<p>Při cestování letadlem a vlakem si předem zjistěte, co smíte vzít do příručního a co do odbaveného zavazadla. Multitoola a nože patří vždy do odbaveného, tekutiny musí splňovat limity a zámky se ideálně hodí k TSA. Pokud cestujete do zahraničí, ověřte také, zda jsou v dané zemi povoleny některé pomůcky, třeba nože nebo pepřové spreje. Informace najdete na stránkách dopravce, letiště nebo v turistických průvodcích.</p>'
          '<h2>Péče o doplňky</h2>'
          '<p>Nylonová pouzdra a opasky omyjte vlažnou vodou s jemným mýdlem a nechte uschnout mimo přímé slunce. Zipy občas očistěte od písku a hlíny. Kombinační zámky se mohou zadřít, pokud do nich zateče špína, proto je občas pročistěte a ověřte nastavený kód. Pláštěnku na batoh po použití vysušte, než ji zabalíte, jinak se může objevit plíseň. Dávkovací lahvičky umyjte před novým použitím, zvlášť po kosmetice.</p>'
          '<h2>Pro koho jsou doplňky vhodné</h2>'
          '<p>Hodí se pěším turistům, kteří chtějí mít drobnosti po ruce, cestovatelům s jedním batohem a rodinám, které potřebují udržet pořádek v zavazadlech. Dobře poslouží i fotografům, vodákům a lidem, kteří při práci venku potřebují rychle sáhnout po rádiu, brýlích nebo dokladech. Naopak pokud chodíte jen na krátké procházky, většinu věcí nepotřebujete, takže začněte s minimem a doplňujte podle zkušeností. Po prvním víkendu poznáte, které kusy jste skutečně použili.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě pouzdra bez ověření, jestli se hodí k vašemu batohu nebo opasku.</li>'
          '<li>Výběr pláštěnky na batoh jiné velikosti, než je objem zavazadla.</li>'
          '<li>Spoléhání na zámek jako na jedinou ochranu cenných věcí.</li>'
          '<li>Nákup příliš mnoha drobností, které pak zvyšují váhu batohu.</li>'
          '<li>Zapomenutí na pravidla pro přepravu tekutin v letadle.</li></ul>'
          '<p>Větší vybavení pro pohyb v přírodě najdete v <a href="/outdoor/">kategorii outdoor</a>. Doplňky jsou naopak drobné pomůcky, které mají výbavu zpřehlednit, ne ji zvětšit, a proto u každé věci zvažte, jaký konkrétní problém řeší.</p>',
    faq=[('Co jsou outdoorové doplňky?', 'Jde o drobné pomůcky pro turistiku, cestování a kempování, třeba modulární pouzdra, popruhy, zámky, kryty batohů, cestovní lahvičky a kempové hrnky.'),
         ('Co znamená systém MOLLE?', 'Je to popruhový systém s poutky na batozích, vestách a opascích. Pouzdra s odpovídajícími popruhy se do něj zasouvají a můžete je přeskupovat.'),
         ('Jak vybrat pláštěnku na batoh?', 'Podle objemu batohu v litrech. Kryt musí batoh celý zakrýt a držet na pružném okraji, ale ne být zbytečně velký.'),
         ('Pro koho jsou kombinační zámky?', 'Pro batohy, kufry a skříňky na cestách. Slouží jako překážka proti příležitostným krádežím, ne jako ochrana před zkušeným zlodějem.'),
         ('Co znamená označení TSA u zámku?', 'Označuje zámek, který může kontrola na letišti otevřít speciálním klíčem bez jeho poškození. Hodí se při cestování letadlem.'),
         ('K čemu slouží vodotěsné pytle?', 'Chrání oblečení, elektroniku a spacák před vlhkostí. Hodí se do batohu, na kajak i na kolo, ale musí se správně rolovat.'),
         ('Jak přepravovat tekutiny v letadle?', 'Použijte malé lahvičky a dodržujte limity dopravce. Aktuální pravidla si ověřte u letecké společnosti nebo na letišti.'),
         ('Jak pečovat o nylonová pouzdra a opasky?', 'Omýt vlažnou vodou a jemným mýdlem, nechat uschnout a občas vyčistit zipy. Nesušit na topení.'),
         ('Hodí se Tasmanian Tiger i do civilu?', 'Ano, modulární pouzdra a opasky používají lidé nejen v přírodě, ale i na cestách, při fotografování nebo ve městě. Záleží hlavně na tom, co do nich vložíte.'),
         ('Co vzít na víkend do kempu z doplňků?', 'Termokrus, prací plátky, lahvičky na hygienu, vodotěsný pytel a pláštěnku na batoh. Seznam doplňte podle délky pobytu a počasí.')])
