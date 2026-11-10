"""sporteka.cz — wave 16c (4. 11. 2026): long texts (>= 1650 words) for paddleboardy, tasky-pres-rameno, sportovni-podprsenky, vitaminy-a-mineraly.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ paddleboardy
NEW['paddleboardy'] = dict(long=True,
    title='Paddleboardy a kajaky: SUP sety a čluny | Sporteka',
    desc='Paddleboardy, nafukovací SUP sety, kajaky a čluny. Jak vybrat prkno podle váhy a vody, co patří do setu a kolik toho potřebujete na první výlet.',
    intro='<p><strong>Paddleboard</strong> neboli SUP je široké plovoucí prkno, na kterém se stojí a pohání se jedním dlouhým pádlem. Vedle něj sem patří také <strong>kajaky, kánoe a nafukovací čluny</strong>, tedy všechno, na čem se dá vyrazit po vodě bez motoru. Nafukovací provedení dnes převažuje, protože po vypuštění vzduchu se vejde do vaku a doveze se v kufru osobního auta, kdežto pevné prkno potřebuje střešní nosič a místo ve sklepě.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů vedle sebe a u každého kusu uvidíte rozměry, nosnost a obsah balení. Značek je široká škála, třeba <a href="/znacka/aqua-marina/">Aqua Marina</a>, <a href="/znacka/jobe/">Jobe</a>, <a href="/znacka/spinera/">Spinera</a>, <a href="/znacka/intex/">Intex</a> nebo <a href="/znacka/f2/">F2</a>. K výbavě se hodí <a href="/plovaci-vesty/">plovací vesty</a>, <a href="/vodni-sporty/">vodní sporty</a> a <a href="/obuv-do-vody/">boty do vody</a>.</p>',
    guide='<h2>Jaké typy plavidel tu najdete</h2>'
          '<p>Kategorie spojuje několik odlišných věcí, které mají společné jen to, že plavou. Než začnete porovnávat jednotlivé kusy, rozhodněte se, jakou pozici chcete na vodě zaujmout: stát, sedět, nebo ležet. Podle toho se zužuje výběr na jednu z následujících skupin.</p>'
          + T(['Typ', 'Pozice a pohon', 'Hodí se pro'], [
              ['Nafukovací paddleboard', 'vstoje nebo vkleče, jedno pádlo', 'výlety na jezera a pomalé řeky, začátečníky, cestování'],
              ['Pevný paddleboard', 'vstoje, jedno pádlo', 'sportovní jízdu, vlny, časté vyjíždění z jednoho místa'],
              ['Kajak', 'vsedě, dvoulisté pádlo', 'delší túry, rychlejší pohyb po vodě, vítr'],
              ['Kánoe a otevřené čluny', 'vsedě nebo klečmo, jednolisté pádlo', 'rodiny, převoz zavazadel, klidné řeky'],
              ['Nafukovací čluny', 'vesla nebo pádla', 'rybaření, rekreaci, krátké přejezdy']]) +
          '<p>Rozsáhlou a pestrou nabídku člunů najdete v podkategorii <a href="/kajaky-a-cluny/">kajaky a čluny</a>, kde jsou jednomístné i vícemístné modely včetně nafukovacích tandemů. Samotná prkna zůstávají v hlavní kategorii.</p>'
          '<h2>Rozměry prkna a co znamenají</h2>'
          '<p>V popisu paddleboardu narazíte na čtyři čísla a každé z nich ovlivňuje jízdu jiným způsobem. Nesledujte jen jedno z nich, protože se navzájem doplňují.</p>'
          '<ul><li><strong>Délka</strong> určuje rychlost a směrovou stabilitu. Delší prkno jede přímočařeji a snáz udržuje kurz, kratší se lépe otáčí a snáz se s ním manipuluje na břehu.</li>'
          '<li><strong>Šířka</strong> je hlavním činitelem stability. Širší prkno se méně kymácí, a proto je vhodné pro začátečníky, jógu a rodinné výlety. Užší prkno klouže rychleji, ale vyžaduje cvik.</li>'
          '<li><strong>Tloušťka</strong> souvisí s objemem. U nafukovacích modelů bývá běžná tloušťka kolem patnácti centimetrů, protože tenčí prkno se pod váhou ohýbá.</li>'
          '<li><strong>Nosnost a objem</strong> říkají, kolik váhy prkno unese bez toho, aby se zanořilo. Počítejte vlastní váhu, váhu batohu, případně dítěte nebo psa.</li></ul>'
          '<p>Nosnost raději volte s rezervou. Prkno zatížené na mez se zanořuje, ztrácí rychlost a hůř reaguje na pádlování. Pokud váháte mezi dvěma velikostmi, bezpečnější volbou je ta větší.</p>'
          '<h2>Výběr podle způsobu jízdy</h2>'
          '<p>Stejné prkno nebude ideální pro všechno. Jednotlivé disciplíny kladou rozdílné nároky na tvar, délku a výbavu.</p>'
          '<h3>Rekreace a výlety</h3>'
          '<p>Pro většinu lidí je to nejrozumnější začátek: všestranný nafukovací model střední délky s dostatečnou šířkou, upevňovacími gumami na zavazadla a držákem na pádlo. Na jezeře nebo rybníce takové prkno oceníte hlavně pro stabilitu.</p>'
          '<h3>Jóga a cvičení na vodě</h3>'
          '<p>Hodí se široké prkno s velkou rovnou plochou a měkkou protiskluzovou podložkou. Pokud chcete cvičit, hledejte model bez výrazně zakřivené špičky a s dostatečnou tloušťkou, aby se nepropadal při zatížení v kleku.</p>'
          '<h3>Touring a delší trasy</h3>'
          '<p>Delší a užší prkno se špičatým nosem udrží kurz, takže nemusíte tolik přepádlovávat. Praktické jsou pevné upevňovací body na zavazadla a vyměnitelné ploutve. Na takové trasy se vyplatí promyslet i pitný režim, tedy <a href="/lahve-a-termosky/">láhev nebo termosku</a>, a zabalit si <a href="/prvni-pomoc/">lékárničku</a>.</p>'
          '<h3>Rodina a děti</h3>'
          '<p>Děti vozte vsedě před dospělým paddlerem a vždy ve vestě s poutkem v rozkroku. Širší prkno s nosností pro dvě osoby plus psa je praktické, ale zkuste ho zvážit s ohledem na přenášení: čím větší prkno, tím těžší vak.</p>'
          '<h3>Rybaření a fotografování</h3>'
          '<p>Stabilní plošina bez zbytečných výstupků je rozumnou volbou. Doplňky k <a href="/rybareni/">rybaření</a> se montují na upevňovací body, takže zjistěte jejich počet před koupí.</p>'
          '<h2>Co obsahuje typický set</h2>'
          '<p>Sety jsou obvykle výhodnější než samostatné prkno, protože na první vyjížďku potřebujete víc než jen nafouknutý trup. Obsah se mezi nabídkami liší, a proto si ho před objednávkou prohlédněte položku po položce.</p>'
          + T(['Součást', 'K čemu slouží', 'Na co si dát pozor'], [
              ['Pumpa s manometrem', 'nafouknutí na provozní tlak', 'ruční dvoučinná je pomalejší na ruce, elektrická rychlejší, ale vyžaduje zdroj'],
              ['Pádlo', 'pohon prkna', 'nastavitelná délka, dělitelný dřík, materiál listu a dříku'],
              ['Vak nebo batoh', 'přenášení a skladování', 'kapacita pro prkno, pumpu a pádlo najednou'],
              ['Leash (bezpečnostní lanko)', 'spojení jezdce s prknem', 'typ podle vody: kotník, lýtko nebo pas'],
              ['Ploutve', 'směrová stabilita', 'systém uchycení a možnost vyměnit nebo sundat'],
              ['Opravná sada', 'zalepení drobné netěsnosti', 'kompatibilita s materiálem prkna']]) +
          '<p>Nejčastěji pod pozornost unikne pádlo. Dobrý set má pádlo, které se nastaví podle výšky a rozloží na tři díly, protože pak se vejde do vaku. Levnější pevné jednodílné pádlo je pohodlné doma, ale komplikuje cestování.</p>'
          '<h2>Pádlo, délka a materiál</h2>'
          '<p>Pádlo na paddleboard bývá o patnáct až dvacet centimetrů vyšší než postava jezdce a nastavuje se tak, aby se při tahu dostalo celý list pod hladinu. Na delší trasy je lepší lehké pádlo, protože hmotnost se při několika tisících tahů projeví. Materiály se liší: hliníkový dřík je odolný a nenáročný, sklolaminát lehčí a pevnější, karbon nejlehčí. List z plastu snese náraz o kámen, laminátový je jemnější. Pokud nevíte, začněte u nastavitelného pádla ze sklolaminátu nebo hliníku a pak si klidně pořiďte lepší.</p>'
          '<h2>Bezpečnost na vodě</h2>'
          '<p>Plovací vesta nepatří do vaku, ale na tělo. V sortimentu <a href="/plovaci-vesty/">plovacích a záchranných vest</a> najdete modely z pěny i automaticky nafukovací vesty, které se nosí jako pásek. Velikost se volí podle váhy a obvodu hrudníku, proto vždy zkontrolujte tabulku výrobce. Dětem patří vesta s poutkem v rozkroku, aby jim nevyklouzla přes hlavu.</p>'
          '<ul><li><strong>Leash</strong> se nosí vždy. Prkno ve větru odjede rychleji, než dokážete plavat. Na tekoucí vodě volte model s rychlým uvolněním kvůli riziku zachycení.</li>'
          '<li><strong>Vítr od břehu</strong> je největší nebezpečí na jezerech: prkno unáší na otevřenou vodu. Vyjíždějte proti větru, ať se vracíte s větrem v zádech.</li>'
          '<li><strong>Teplota vody</strong> rozhoduje o oblečení. Ve studené vodě pomůže <a href="/neopreny/">neopren</a>, v teple stačí <a href="/lycra-a-uv-tricka/">lycra nebo UV tričko</a> a <a href="/plavky/">plavky</a>.</li>'
          '<li><strong>Informujte o trase</strong> někoho na břehu a vezměte si telefon v nepromokavém pouzdru.</li></ul>'
          '<h2>Oblečení a vybavení kolem prkna</h2>'
          '<p>Na vodě se nezvykle rychle ochladíte, i když svítí slunce, a zároveň se spálíte, protože odraz od hladiny zesiluje záření. Praktická je vrstva, která rychle schne. Na nohy patří <a href="/obuv-do-vody/">boty do vody</a> nebo neoprenové botky, hlavně kvůli kamenitému dnu a ostrým lasturám. K ochraně očí slouží polarizační <a href="/sportovni-bryle/">sportovní brýle</a>, nejlépe s plovoucím řemínkem. Na pláži se hodí <a href="/plazove-doplnky/">plážové doplňky</a> a na přesun věcí <a href="/sportovni-tasky/">sportovní tašky</a>. Pokud chcete na prkně i plavat nebo se osvěžit, sáhněte po <a href="/plavecke-pomucky/">plaveckých pomůckách</a>, pro šnorchlování existuje samostatná kategorie <a href="/snorchlovani/">šnorchlování a potápění</a>.</p>'
          '<h2>Nafukování, údržba a skladování</h2>'
          '<p>Nafukovací prkno se nafukuje na tlak uvedený výrobcem přímo na prkně nebo u ventilu. Příliš nízký tlak má za následek ohýbání uprostřed a špatnou jízdu, příliš vysoký namáhá švy. Při nafukování na slunci nechte prkno trochu dofouknout později, protože se vzduch ohřeje a roztáhne. Po jízdě na slané nebo špinavé vodě prkno opláchněte sladkou vodou a nechte úplně vyschnout v rozloženém stavu, aby se neusadila plíseň. Pak ho volně srolujte od zadní části k přední, čímž vytlačíte zbytek vzduchu. Skladujte na suchém místě mimo přímé slunce a bez ostrých předmětů. Ventily čistěte od písku, protože drobné zrnko stačí na pomalé uniknutí vzduchu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě podle designu bez kontroly nosnosti. Hezké prkno s příliš nízkou nosností se bude zanořovat.</li>'
          '<li>Podcenění váhy vaku. Velký set je těžký a při přepravě bez auta se stane zátěží.</li>'
          '<li>Vynechání vesty a leashe, které se pak dokupují pozdě.</li>'
          '<li>Příliš krátké prkno pro vyšší nebo těžší osobu: je nestabilní a pomalé.</li>'
          '<li>Volba pevného prkna, i když není kde a čím ho vozit.</li>'
          '<li>Nafukování na nízký tlak, aby to bylo rychleji hotové.</li></ul>'
          '<h2>Jak vybírat na Sportece</h2>'
          '<p>V kategorii si můžete filtrovat podle značky a řadit nabídky. U každého prkna sledujte nosnost, rozměry a obsah setu. U více obchodů vedle sebe se rozdíly v balení ukážou rychle: jedno nabízí jen prkno, jiné prkno s pádlem, pumpou i vakem. Chcete-li zkusit něco jiného než vstoje, projděte <a href="/kajaky-a-cluny/">kajaky a čluny</a>, a pokud vás láká celé odvětví, otevřete nadřazenou kategorii <a href="/vodni-sporty/">vodní sporty a plavání</a>. Pro koupání s dětmi se hodí <a href="/nafukovaci-hracky/">nafukovací hračky a lehátka do vody</a> a pro zahradu <a href="/bazeny/">bazény</a>.</p>',
    faq=[('Jaký paddleboard je vhodný pro úplného začátečníka?', 'Širší nafukovací prkno střední délky s dostatečnou nosností a tloušťkou kolem patnácti centimetrů. Stabilita je důležitější než rychlost a set s pumpou, pádlem a vakem ušetří dohledávání doplňků.'),
         ('Jak poznám, jestli prkno unese mou váhu?', 'Porovnejte svou váhu včetně batohu a případného dítěte či psa s údajem o nosnosti výrobce. Doporučuje se mít rezervu, protože prkno zatížené na maximum se zanořuje a hůř se řídí.'),
         ('Je nafukovací paddleboard stejně dobrý jako pevný?', 'Pro rekreaci a výlety zcela postačí, je lehčí na přepravu a odolnější proti nárazu o kameny. Pevné prkno má lepší klouzavost a hodí se pro sportovní jízdu, ale vyžaduje prostor a nosič.'),
         ('Jakou délku pádla zvolit?', 'Obvykle o patnáct až dvacet centimetrů nad výškou jezdce. Nastavitelné pádlo se přizpůsobí různým lidem a jednotlivým situacím, takže je pro rodinu praktičtější než pevné.'),
         ('Na jaký tlak se nafukuje prkno?', 'Na hodnotu, kterou uvádí výrobce u ventilu nebo v návodu. Použijte pumpu s manometrem a nepřefukujte. Při nafukování na přímém slunci tlak po ochlazení klesá, proto ho po vodě zkontrolujte.'),
         ('Potřebuji vestu, když umím plavat?', 'Doporučuje se ji nosit vždy. Pád do studené vody, únava nebo úder o prkno mohou i dobrého plavce přivést do potíží, a vesta rozhodne, zda se dostanete zpět na prkno v klidu.'),
         ('Co je leash a proč ho používat?', 'Je to lanko, které spojuje jezdce s prknem. Zabrání tomu, aby prkno odplulo po pádu. Na tekoucí vodě volte typ s rychlým uvolněním, aby se nemohl zachytit o překážku.'),
         ('Jak prkno opravit při malé díře?', 'Najděte únik pomocí mýdlové vody, osušte místo a použijte opravnou sadu určenou pro materiál prkna. Většina sad obsahuje záplatu a lepidlo. Větší poškození nechte posoudit výrobcem nebo servisem.'),
         ('Jak prkno skladovat přes zimu?', 'Zcela vyschlé, volně srolované nebo lehce nafoukané, na suchém a tmavém místě bez ostrých předmětů. Vlhkost je největší nepřítel, protože v uzavřeném vaku vzniká plíseň.'),
         ('Hodí se paddleboard i pro děti a psy?', 'Ano, na klidné vodě a pod dohledem dospělého. Dítě musí mít vestu s poutkem a sedí nebo leží uprostřed prkna. Pro psa zvolte širší prkno a protiskluzovou plochu a zvyšujte nosnost o jeho váhu.')])

# ------------------------------------------------------------------ tasky-pres-rameno
NEW['tasky-pres-rameno'] = dict(long=True,
    title='Tašky přes rameno a dokladovky | Sporteka',
    desc='Crossbody tašky, dokladovky, ledvinky a tašky na doklady a telefon. Jak vybrat velikost, materiál a uchycení a kde porovnat nabídky obchodů.',
    intro='<p><strong>Taška přes rameno</strong> je malá až střední taška, která visí na dlouhém popruhu napříč hrudníkem a nechává volné ruce. Menší provedení se říká <strong>dokladovka</strong>: vejde se do ní telefon, peněženka, klíče a doklady, nic víc. Hodí se do města, na cestování, na festival i na krátkou vycházku, kdy se vám nechce brát celý batoh. Rozhoduje hlavně velikost, materiál a šířka popruhu, a právě na ně se tenhle text zaměřuje.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a najdete tu <a href="/znacka/fjallraven/">Fjällräven</a>, <a href="/znacka/rothco/">Rothco</a>, <a href="/znacka/calvin-klein/">Calvin Klein</a>, <a href="/znacka/helikon-tex/">Helikon-Tex</a>, <a href="/znacka/the-north-face/">The North Face</a>, <a href="/znacka/tommy-hilfiger/">Tommy Hilfiger</a> nebo <a href="/znacka/lacoste/">Lacoste</a>. Větší zavazadla jsou v <a href="/batohy/">batozích</a> a <a href="/sportovni-tasky/">sportovních taškách</a>.</p>',
    guide='<h2>Jaké druhy tašek se tu skrývají</h2>'
          '<p>Pod názvem se skrývá několik tvarů, které vypadají podobně, ale slouží k různým věcem. Nejdřív zvažte, co do tašky skutečně dáváte, a až potom vybírejte barvu.</p>'
          + T(['Typ', 'Typická velikost a tvar', 'Na co se hodí'], [
              ['Dokladovka', 'malá, často svislá, jedno až dvě kapsy', 'telefon, doklady, karty, klíče při procházce nebo cestování'],
              ['Crossbody taška', 'střední, vodorovná nebo čtvercová', 'peněženka, láhev, drobnosti na celý den ve městě'],
              ['Messenger', 'širší s klopou přes celou přední stranu', 'tablet, sešity, menší notebook, každodenní nošení'],
              ['Ledvinka nošená přes rameno', 'plochá, pásek upravitelný', 'rychlý přístup k věcem, festival, kolo, cestování'],
              ['Fotografická nebo technická taška', 'polstrovaná s přihrádkami', 'fotoaparát, objektivy, kabely, powerbanka'],
              ['Taktická nebo army taška', 'robustní materiál, systém úchytů', 'outdoor, výlety, nošení vybavení']]) +
          '<p>Pokud potřebujete spíš plochou kapsu na pás, podívejte se do <a href="/sportovni-tasky/">sportovních tašek a ledvinek</a>. Pro běhání jsou určené <a href="/bezecke-opasky/">běžecké opasky a pouzdra</a>, které se k tělu přimknou a neposkakují.</p>'
          '<h2>Velikost a objem: kolik se do tašky vejde</h2>'
          '<p>Nejčastější chybou je koupě příliš malé tašky, do které se nevejde telefon s obalem, nebo příliš velké, která se plní zbytečnostmi a po hodině táhne rameno dolů. Při výběru si položte vedle sebe věci, které nosíte pokaždé, a změřte je. Telefon dnes bývá delší než dřívější modely, proto ověřte vnitřní rozměr hlavní kapsy, ne jen vnější délku tašky. Doklady a karty se vejdou do plochých přihrádek, klíče je lepší dát do zvláštní kapsy, aby neškrábaly displej.</p>'
          '<ul><li><strong>Objem do tří litrů</strong> stačí na telefon, peněženku, klíče a drobnosti. Je to klasická dokladovka.</li>'
          '<li><strong>Zhruba tři až šest litrů</strong> pojme navíc láhev, malý deštník, powerbanku nebo lehkou bundu rolovanou.</li>'
          '<li><strong>Nad šest litrů</strong> už je to spíš malá taška nebo lehký batoh. Pokud do ní dáváte víc věcí, zvažte <a href="/mestske-batohy/">městský batoh</a>.</li></ul>'
          '<h2>Materiál, který vydrží</h2>'
          '<p>Od materiálu se odvíjí hmotnost, odolnost proti vodě i cena údržby. Kromě tkaniny sledujte zipy, švy a kování, protože právě tam taška obvykle selže jako první.</p>'
          + T(['Materiál', 'Vlastnosti', 'Poznámka'], [
              ['Nylon a polyester', 'lehké, rychle schnou, odolné proti oděru', 'nejčastější volba pro sportovní a outdoorové tašky'],
              ['Bavlněné plátno', 'pevné, měkké na dotek, stárne vzhledově', 'bez impregnace nasákne vodou'],
              ['Hrubá tkanina typu cordura', 'hrubší a velmi odolná proti oděru', 'těžší než lehký nylon, vhodná pro náročné použití'],
              ['Syntetická kůže', 'snadno se otírá, drží tvar', 'stárne jinak než pravá kůže, může popraskat'],
              ['Pravá kůže', 'elegantní, vyžaduje péči', 'těžší, nevhodná do deště bez impregnace'],
              ['Voděodolná tkanina s povrchovou úpravou', 'odpuzuje drobný déšť', 'úprava časem slábne a dá se obnovit']]) +
          '<p>Slovo <em>voděodolný</em> znamená, že taška vydrží lehký déšť, <em>vodotěsný</em> předpokládá zalepené švy a zip, který neprosakuje. Pro cestu na kole nebo na vodu hledejte specializované řešení, třeba nepromokavé vaky z <a href="/vodni-sporty/">vodních sportů</a>.</p>'
          '<h2>Uchycení a pohodlí nošení</h2>'
          '<p>Popruh je u tašky přes rameno nejdůležitější součást. Měl by být dostatečně široký, aby se nezařezával do ramene, a nastavitelný, protože jinak se taška nedá upravit podle postavy ani vrstev oblečení. Prověřte, jak je popruh přichycen k tašce: kovové karabiny jsou pohodlné, ale mohou se rozevřít, zatímco prošité poutko drží pevněji. Praktická je bezpečnostní přezka, která umožňuje popruh rychle rozepnout. Někteří lidé dávají přednost tašce nošené vpředu, a to z důvodu přehledu v davu.</p>'
          '<p>Pro hodiny strávené na nohou je rozhodující rozložení váhy. Těžší předměty dejte blíž k tělu a lehčí dál. Pokud tašku přetížíte, popruh se zařezává do trapézu a rameno se unaví rychleji než záda s dobře nastaveným batohem.</p>'
          '<h2>Kapsy, zipy a bezpečnost obsahu</h2>'
          '<p>Dobrá taška má víc než jednu komoru. Hlavní kapsa na objemnější předměty, zadní plochá kapsa na doklady a vnitřní zipová kapsa na klíče nebo drobné se používají nejčastěji. Zipy by měly být dostatečně velké na prsty v rukavicích a mít poutko, které se dá uchopit. Kapsa na zádech přilehlá k tělu je pro zloděje hůře dostupná, ale hůř se k ní dostanete i vy, proto do ní patří věci, které nepotřebujete často. Na festivalech a v turistických centrech se oceňují zipy zajištěné proti otevření. Zkontrolujte také, zda má taška průchod pro kabel od sluchátek nebo powerbanky, pokud ji chcete nabíjet za pochodu. Kdo cestuje s elektronikou, najde v kategorii <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a> přenosné zdroje.</p>'
          '<h2>Pro koho a na co</h2>'
          '<h3>Město a každodenní nošení</h3>'
          '<p>Pro město se hodí čisté tvary, neutrální barvy a lehčí materiály. Značky jako Calvin Klein, Tommy Hilfiger nebo Lacoste dávají důraz na módní vzhled, outdoorové značky spíš na funkčnost. K tašce se pěkně hodí <a href="/tenisky/">tenisky a volnočasové boty</a> nebo <a href="/mikiny/">mikina</a>.</p>'
          '<h3>Cestování a dovolená</h3>'
          '<p>Na cestách oceníte tašku, která má zajištěný zip a plochý profil pod bundou. Na letišti se hodí jako osobní zavazadlo, do které patří cestovní doklady, peněženka a telefon. Pro delší túry je lepší <a href="/turisticke-batohy/">turistický batoh</a>, malá taška přes rameno je jen doplněk.</p>'
          '<h3>Outdoor a výlety</h3>'
          '<p>Taktické a army tašky jsou odolné a mají systém úchytů, takže na ně jde připnout další pouzdra. Hodí se na vycházky do lesa, fotografování nebo jako doplněk k batohu, ať už jde o <a href="/outdoor/">outdoor a turistiku</a>, nebo <a href="/kemping/">kemping</a>.</p>'
          '<h3>Sport a aktivní den</h3>'
          '<p>Pro krátký trénink se vejde taška s láhví, ručníkem a klíči. Chcete-li přenášet sportovní oblečení, zvolte <a href="/sportovni-tasky/">sportovní tašku</a>. Na kolo je užitečnější <a href="/cyklo-tasky-a-nosice/">brašna nebo taška na rám</a>, protože se nehoupe při šlapání.</p>'
          '<h3>Škola a práce</h3>'
          '<p>Messenger s polstrovanou přihrádkou pojme tablet nebo tenký notebook a pro studenty bývá alternativou k <a href="/skolni-batohy/">školnímu batohu</a>. Při pravidelném nošení těžších věcí je batoh šetrnější k zádům než taška na jednom rameni.</p>'
          '<h2>Značky, které tu najdete</h2>'
          '<p>Každá značka má vlastní styl a konstrukční zvyklosti, proto se vyplatí se v nich orientovat. '
          f'Ze zastoupených {B(("fjallraven", "Fjällräven"), ("the-north-face", "The North Face"), ("deuter", "Deuter"))} patří k outdoorovým značkám se silným důrazem na funkčnost a trvanlivost. '
          f'{B(("rothco", "Rothco"), ("helikon-tex", "Helikon-Tex®"))} nabízejí vojenský a taktický střih s úchyty na doplňky. '
          f'{B(("calvin-klein", "Calvin Klein"), ("tommy-hilfiger", "Tommy Hilfiger"), ("lacoste", "Lacoste"))} patří mezi módní značky s designem pro město. '
          f'{B(("nike", "Nike"), ("aoking", "Aoking"))} doplňují sportovní a levnější segment. Rozdíly poznáte hlavně na zpracování zipů a švů a na šířce popruhu.</p>'
          '<h2>Jak tašku nosit, aby netlačila</h2>'
          '<p>Popruh nastavte tak, aby taška visela zhruba v úrovni pasu až boku a nebouchala o stehno. Při chůzi do schodů nebo při běhu ji lehce přidržte rukou. V zimě, kdy nosíte silnou bundu, popruh povolte, v létě ho zase zkraťte. Těžké věci, jako je láhev nebo powerbanka, patří ke straně přilehlé k tělu. Po celodenním nošení stojí za to dát rameno do klidu a tašku střídavě přehodit na druhou stranu.</p>'
          '<h2>Péče o tašku</h2>'
          '<p>Nylonové a polyesterové tašky vyperete ručně ve vlažné vodě s jemným mycím prostředkem a necháte uschnout na vzduchu, mimo topení a přímé slunce. Do pračky se vkládají jen pokud to povoluje výrobce, protože pračka může poškodit povrchovou úpravu. Bavlněné plátno se čistí kartáčem a vlhkým hadříkem, silné skvrny jen místně. Kůži otřete vlhkým hadříkem a pravidelně ošetřete přípravkem určeným pro daný typ kůže. Zipy občas vyčistěte od prachu a promažte jemným tukem nebo voskem. Tašku před uložením vyprázdněte, aby si nezachovala tvar po předmětech a nezačala zapáchat.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš malá taška, do které se telefon vejde jen bez obalu.</li>'
          '<li>Úzký popruh, který bolí po prvních dvaceti minutách.</li>'
          '<li>Podcenění zipů a švů, přestože se rozpadají jako první.</li>'
          '<li>Přetěžování tašky na jedno rameno místo volby batohu.</li>'
          '<li>Koupě podle fotky bez kontroly rozměrů. Stejný tvar může mít rozdílný objem.</li>'
          '<li>Očekávání, že voděodolná taška vydrží celodenní liják.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>V kategorii vyberte značku, porovnejte více nabídek stejného modelu a sledujte rozměry v popisu. Barevné varianty jednoho modelu mají někdy různé ceny a dostupnost, takže stojí za to zkontrolovat všechny. Pokud hledáte větší zavazadla, prohlédněte <a href="/batohy/">batohy</a>, na každodenní cestu se hodí <a href="/mestske-batohy/">městské a sportovní batohy</a> a pro cestování <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    faq=[('Čím se liší dokladovka od tašky přes rameno?', 'Dokladovka je menší a pojme jen nezbytné věci, tedy telefon, doklady, karty a klíče. Taška přes rameno bývá větší a pojme navíc láhev, drobnosti nebo tenký tablet.'),
         ('Jak poznám, že se do tašky vejde můj telefon?', 'Změřte telefon i s obalem a porovnejte s vnitřními rozměry hlavní kapsy, které uvádí výrobce. Vnější rozměr tašky nic neříká o tom, kolik místa je uvnitř.'),
         ('Na kterém rameni se taška nosí?', 'Je to věc zvyku. Důležité je střídat strany, aby se nezatěžovalo pořád jedno rameno. Taška přes tělo je stabilnější než taška přehozená jen přes rameno.'),
         ('Jaký materiál zvolit do deště?', 'Nejlépe nylon nebo polyester s voděodolnou povrchovou úpravou, případně taška s laminovanými švy. Bavlněné plátno a kůže potřebují impregnaci a stejně se nehodí na delší déšť.'),
         ('Hodí se taška přes rameno na túru?', 'Na krátkou procházku ano, na delší trasu je lepší turistický batoh, který rozloží váhu na záda a boky. Taška na jednom rameni při chůzi hůř drží a unavuje.'),
         ('Jak chránit doklady před kapesními zloději?', 'Noste tašku vpředu, zavřete všechny zipy a doklady dejte do vnitřní kapsy blíž k tělu. Některé tašky mají zipy zajištěné proti otevření a skrytou kapsu u těla.'),
         ('Lze tašku prát v pračce?', 'Jen pokud to výrobce výslovně povoluje. Bezpečnější je ruční praní ve vlažné vodě s jemným prostředkem a sušení na vzduchu. Kůže a potištěné materiály se perou jen místně.'),
         ('Můžu tašku použít jako příruční zavazadlo v letadle?', 'Malá taška se obvykle počítá jako osobní předmět a může se vejít vedle příručního zavazadla. Podmínky určují aerolinky, proto zkontrolujte jejich pravidla a rozměry.'),
         ('Jakou barvu zvolit?', 'Tmavé a neutrální barvy se hůř špiní a hodí se ke všemu. Výrazné barvy zlepšují viditelnost v davu a u outdoorových tašek i za šera, ale jsou méně univerzální.'),
         ('Je lepší messenger, nebo crossbody?', 'Messenger má větší klopu a víc místa na tablet či sešity, crossbody je kompaktnější a lépe drží u těla. Podle toho, co nosíte, rozhodněte, zda vám objem nebo pohodlí přijde důležitější.')])

# ------------------------------------------------------------------ sportovni-podprsenky
NEW['sportovni-podprsenky'] = dict(long=True,
    title='Sportovní podprsenky: výběr podle zátěže | Sporteka',
    desc='Sportovní podprsenky na běh, jógu, fitness i kolo. Jak vybrat velikost, míru podpory a střih, a kde porovnat nabídky českých obchodů.',
    intro='<p><strong>Sportovní podprsenka</strong> se od běžné liší střihem, materiálem a hlavně tím, že má při pohybu držet. Dobrá volba omezuje poskakování, nezařezává se, odvádí pot a během tréninku si jí prakticky nevšimnete. Neexistuje jedna univerzální podprsenka: na jógu stačí jemná podpora, na běh nebo skákání je potřeba pevný střih, a na každodenní nošení zase pohodlný top bez kostic. Tahle stránka vysvětluje rozdíly mezi střihy i velikostmi a pomůže vám vybrat správně.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a najdete tu značky <a href="/znacka/champion/">Champion</a>, <a href="/znacka/gymbeam/">GymBeam</a>, <a href="/znacka/adidas/">Adidas</a>, <a href="/znacka/reebok/">Reebok</a>, <a href="/znacka/puma/">Puma</a>, <a href="/znacka/under-armour/">Under Armour</a> nebo <a href="/znacka/nike/">Nike</a>. K podprsence se hodí <a href="/leginy/">legíny</a>, <a href="/tilka/">tílka a topy</a> a <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>.</p>',
    guide='<h2>Míra podpory podle sportu</h2>'
          '<p>Základní pravidlo zní: čím větší náraz, tím pevnější podpora. Výrobci používají tři stupně, které se označují nízká, střední a vysoká podpora, i když přesné hranice si každý určuje po svém. Proto vždy vezměte v úvahu popis modelu a ne jen název kategorie.</p>'
          + T(['Podpora', 'Typické sporty', 'Jak vypadá střih'], [
              ['Nízká', 'jóga, pilates, chůze, protahování, nordic walking', 'měkký top, tenký materiál, často bez zapínání a bez kostic'],
              ['Střední', 'kolo, posilovna, aerobik, turistika, tanec', 'pevnější spodní pás, široká ramínka, někdy podšité košíčky'],
              ['Vysoká', 'běh, skoky, kondiční tréninky, tenis, míčové sporty', 'kompresní nebo zapouzdřený střih, pevný pás, zadní zapínání či zkřížená záda']]) +
          '<p>Pokud děláte sporty s různou intenzitou, kupte raději dvě podprsenky než jednu kompromisní. Podprsenka na jógu bude při běhu poskakovat a podprsenka na běh bude na józe zbytečně pevná. Pro každodenní cvičení se hodí několik kusů, protože je můžete střídat a prát po každém tréninku. Při obměně vždy zkuste vybrat podobný střih, na který jste zvyklí, a teprve potom experimentujte s novým.</p>'
          '<h2>Kompresní a zapouzdřené střihy</h2>'
          '<p>Kompresní podprsenka přitiskne prsa k tělu a rozloží zatížení po celé ploše. Je jednodušší na obléknutí a bývá bez švů, ale u větších velikostí nemusí stačit. Zapouzdřený střih má každou stranu zvlášť v košíčku, čímž lépe drží pohyb každého prsu. U vyšších velikostí se často kombinuje obojí, doplněné o nastavitelná ramínka a zapínání vzadu. Vybírejte podle toho, co potřebujete: komfort a hladký vzhled, nebo maximální podporu.</p>'
          '<h2>Velikost a správné padnutí</h2>'
          '<p>Většina potíží vzniká nesprávnou velikostí, ne špatnou značkou. Sportovní podprsenky se prodávají ve dvou systémech: ve velikostech S až XL, které se odvíjejí od obvodu hrudníku, a v klasických velikostech s obvodem pod prsy a košíčkem, například 75B. Tabulky se liší mezi výrobci, a proto použijte tabulku konkrétní značky, ne jen zažitý odhad.</p>'
          '<ul><li><strong>Obvod pod prsy</strong> změřte pevně, ale bez zařezávání. Pás má držet většinu podpory, ne ramínka.</li>'
          '<li><strong>Pás</strong> nesmí vyjíždět nahoru a při zvednutí paží má zůstat na místě. Pod pás se mají vejít dva prsty, ne víc.</li>'
          '<li><strong>Košíčky</strong> mají prsa celá obepnout, bez přetékání a bez prázdných záhybů.</li>'
          '<li><strong>Ramínka</strong> se nesmí zařezávat ani sklouzávat. Pokud musíte ramínka utahovat na maximum, je podprsenka pravděpodobně velká v pásu.</li>'
          '<li><strong>Zkouška pohybu</strong>: předkloňte se, zvedněte ruce a zaskákejte na místě. Pokud cítíte nepříjemné poskakování, zkuste menší pás nebo pevnější model.</li></ul>'
          '<p>Velikost se může měnit během měsíce i v průběhu života. Podprsenky, které dlouho seděly, mohou přestat padnout, proto se vyplatí občas přeměřit.</p>'
          '<h2>Materiály a péče o pot</h2>'
          '<p>Sportovní podprsenky se nejčastěji vyrábějí z polyamidu nebo polyesteru s příměsí elastanu, který zajišťuje pružnost. Takové materiály dobře odvádějí pot a rychle schnou. Bavlna příjemně hladí na kůži, ale nasákne potem a pomalu schne, proto se hodí na jógu a odpočinek, ne na intenzivní trénink. Merino vlna nese pot, zůstává příjemná a méně zapáchá, což oceníte při dlouhých výletech, viz kategorie <a href="/merino-pradlo/">merino spodní prádlo a legíny</a>. Bezešvé provedení zmenšuje riziko otlaků, kdežto ploché švy jsou odolnější u pevných modelů.</p>'
          '<h2>Výběr podle aktivity</h2>'
          '<h3>Běh</h3>'
          '<p>Při běhu se prsa pohybují nahoru, dolů i do stran, proto potřebujete vysokou podporu. Hledejte pevný pás, kvalitní ramínka a materiál bez drsných švů. Podprsenku nosíte s <a href="/bezecka-obuv/">běžeckými botami</a> a <a href="/funkcni-tricka/">funkčním tričkem</a>. Další vybavení najdete v kategorii <a href="/beh/">běh, triatlon a atletika</a>.</p>'
          '<h3>Fitness a posilování</h3>'
          '<p>V posilovně se hodí střední podpora a volné ramínkové vedení, které neomezuje při tlacích nad hlavu. Pokud děláte skoky, švihadla nebo kondiční cvičení, volte vyšší podporu. Kompletní oblečení hledejte v <a href="/fitness/">fitness a posilování</a>.</p>'
          '<h3>Jóga a pilates</h3>'
          '<p>Měkké materiály, nízká podpora a nezařezávající pás jsou nejlepší volbou. Ramínka se mohou křížit a otevřená záda dovolují volnost při ohybech. Kombinujte s <a href="/joga-a-pilates/">oblečením a pomůckami na jógu</a> a pružnými legínami.</p>'
          '<h3>Kolo a turistika</h3>'
          '<p>Na kole hrozí tření podpaží a ramen, proto vybírejte hladké okraje a pevný pás, který nesklouzává. Při turistice s batohem pozor na tlustá ramínka a plastové zapínání, které se pod popruhy batohu zařezává. K cyklistice se hodí <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a dres přes podprsenku.</p>'
          '<h3>Tanec a gymnastika</h3>'
          '<p>V tanci a gymnastice záleží na vzhledu a volnosti pohybu. Hledají se kompaktní topy, někdy s cvičebním dresem. Další výběr najdete v <a href="/tanec-a-gymnastika/">tanci, baletu a gymnastice</a>.</p>'
          '<h3>Plavání a vodní sporty</h3>'
          '<p>Plavecké topy a sportovní dvoudílné plavky mají jiný materiál, odolný proti chloru. Běžná sportovní podprsenka se nehodí do bazénu. Podívejte se do <a href="/damske-plavky/">dámských plavek</a> a <a href="/vodni-sporty/">vodních sportů</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší zastoupení má {B(("champion", "Champion"), ("gymbeam", "GymBeam"), ("adidas", "Adidas"), ("reebok", "Reebok"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("nike", "Nike"), ("4f", "4F"), ("on", "On"), ("the-north-face", "The North Face"))}. '
          'Střih a velikostní řada se mezi značkami liší, takže si u každé zkontrolujte tabulku. Některé značky nabízejí podprsenky jen v obvyklých písmenných velikostech, jiné i v košíčkových. Pokud chcete vyzkoušet novou značku, zvolte model s nastavitelnými ramínky a zapínáním, který se přizpůsobí lépe než vytahaný top.</p>'
          '<h2>Kostice, zapínání a další detaily</h2>'
          '<p>Kostice se u sportovních modelů používají zřídka, protože tlačí při pohybu, a nahrazuje je pevný spodní pás a širší ramínka. Zapínání vzadu dovoluje přesné nastavení obvodu a hodí se pro větší velikosti. Modely bez zapínání se nazouvají přes hlavu, jsou jednodušší a lépe sedí u menších velikostí, ale hůř se oblékají zpocené. Zkřížená záda, takzvaný racerback, drží ramínka na místě i při velkých pohybech paží. Ramínka nastavitelná na výšku se hodí pro různé postavy, avšak zvyšují počet švů a míst možného tření. Reflexní prvky a kapsy na klíč nebo kartu najdete spíš u běžeckých modelů. Při výběru si všímejte i vnitřního lemu: měkký lem se nezařezává a nedře kůži při dlouhém pohybu.</p>'
          '<h2>Jak o podprsenku pečovat</h2>'
          '<p>Praktická podprsenka má vydržet řadu pracích cyklů, ale jen tehdy, když ji neničíte. Perte ji po každém potu na jemný program nebo ručně ve vlažné vodě, nejlépe v ochranném sáčku. Nepoužívejte aviváž, protože pokrývá vlákna a zhoršuje odvod potu. Nesušte v sušičce ani na topení, vysoká teplota poškozuje elastan. Zapínání před praním zapněte, aby se nezachytávalo o jiné prádlo. Střídání dvou až tří kusů prodlužuje životnost každé z nich.</p>'
          '<p>Kdy vyměnit? Když podprsenka ztratí pružnost, pás vyjíždí nahoru, ramínka se vytahují nebo se materiál zrnitě rozpadá. Pokud musíte zapínat na nejvolnější háček a podprsenka přesto nedrží, nebo ani na nejtěsnější nedrží pevně, je čas na novou.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Volba podle vzhledu místo podpory. Hezký top na jógu nezvládne běh.</li>'
          '<li>Koupě o číslo větší, aby se lépe dýchalo. Pak pás nedrží a podpora zmizí.</li>'
          '<li>Nošení jedné podprsenky několik dní po sobě bez praní a střídání.</li>'
          '<li>Ignorování tabulky velikostí konkrétní značky.</li>'
          '<li>Používání staré, vytahané podprsenky, protože „ještě drží".</li>'
          '<li>Pro intenzivní sport volba bavlněného topu bez podpory.</li></ul>'
          '<h2>Kdy a kde nakupovat</h2>'
          '<p>Sportovní podprsenky se nejvíc prodávají před jarní a podzimní sezónou, kdy lidé začínají znovu cvičit. Na konci kolekce se objevují slevy na barvy, které se vyprodávají, ale velikostní řada bývá neúplná. Pokud znáte svůj oblíbený model, sledujte jeho dostupnost ve více obchodech a nečekejte na poslední kus ve vaší velikosti. Při první koupi nové značky objednejte raději dvě sousední velikosti a nevhodnou vraťte.</p>'
          '<h2>Jak sladit celé oblečení</h2>'
          '<p>Podprsenka je jen první vrstva. Na horké dny ji nosíte samostatně nebo pod <a href="/sportovni-tricka/">tričkem a tílkem</a>. V chladu ji pokryjete <a href="/funkcni-tricka/">funkčním trikem s dlouhým rukávem</a> nebo <a href="/termopradlo/">termoprádlem</a>. Dokonalým doplňkem jsou <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-kratasy/">kraťasy</a>. Chcete-li hotový set, podívejte se do <a href="/soupravy/">souprav a kompletů</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>V nabídce porovnejte více obchodů u stejného modelu a sledujte skladové velikosti. Barvy a velikosti se vyprodávají nerovnoměrně, takže výhodnější nabídku často najdete u jiného prodejce než u prvního obchodu, který zkusíte. Při koupi na dálku se řiďte tabulkou velikostí a zjistěte podmínky vrácení. Vlastní zkouška v pohybu zůstává nejlepší test, proto zvažte možnost výměny.</p>',
    faq=[('Jak poznám správnou míru podpory?', 'Řiďte se sportem. Pro jógu a chůzi stačí nízká podpora, pro kolo a posilovnu střední a pro běh a skoky vysoká. Při pochybnostech raději zvolte vyšší podporu.'),
         ('Je vhodné nosit sportovní podprsenku celý den?', 'Pokud je pohodlná a nezařezává se, nic nebrání. Pro každodenní nošení jsou praktičtější měkké bezešvé topy než pevné kompresní modely určené na intenzivní sport.'),
         ('Jak změřit velikost?', 'Změřte obvod hrudníku pod prsy a v nejobjemnějším místě. Porovnejte s tabulkou konkrétní značky, protože se liší. Pásek metru nesmí být zkroucený ani příliš utažený.'),
         ('Jak často měnit sportovní podprsenku?', 'Když ztratí pružnost, pás vyjíždí nahoru, ramínka se vytahují nebo se materiál rozpadá. Při častém cvičení se projeví dříve, proto mějte několik kusů na střídání.'),
         ('Má smysl kupovat vycpávané košíčky?', 'Vyjímatelné vycpávky se hodí pro tvarování a lehkou oporu, ale při intenzivním sportu o podpoře rozhoduje hlavně pás a střih. Vyjímatelné vložky před praním vyndejte, aby se nezdeformovaly.'),
         ('Jak prát sportovní podprsenku?', 'Na jemný program ve vlažné vodě, nejlépe v sáčku a bez aviváže. Nesuší se v sušičce ani na topení, protože vysoká teplota poškozuje elastan a ztrácí se pružnost.'),
         ('Hodí se bavlněná podprsenka na sport?', 'Na klidné aktivity ano, třeba na jógu. Při intenzivním pohybu bavlna nasákne potem a pomalu schne, takže lepší je polyamid, polyester nebo merino.'),
         ('Jaká je nejlepší podprsenka na běh?', 'Taková, která při běhu nepodskakuje a nezařezává se: pevný pás, kompresní nebo zapouzdřený střih, dobrá ramínka a hladké švy. Konkrétní model záleží na velikosti a vašem pocitu.'),
         ('Proč mi vyjíždí pás nahoru?', 'Nejčastěji je podprsenka v pásu příliš velká nebo vytahaná. Zkuste menší obvod a větší košíček, případně model s pevnějším pásem a zapínáním vzadu.'),
         ('Jaká podprsenka se hodí pro větší velikosti?', 'Hledejte zapouzdřené košíčky, široká nastavitelná ramínka, pevný pás a zapínání vzadu. Důležitá je přesná velikost v pásu, protože právě pás nese většinu zátěže, ne ramínka.'),
         ('Lze sportovní podprsenku použít na plavání?', 'Běžná sportovní podprsenka se pro bazén nehodí. Chlor a voda poškozují materiál, a navíc nasákne. Použijte plavky nebo plavecký top vyrobený pro vodu.')])

# ------------------------------------------------------------------ vitaminy-a-mineraly
NEW['vitaminy-a-mineraly'] = dict(long=True,
    title='Vitamíny, minerály a omega-3 | Sporteka',
    desc='Vitamíny, minerály a omega-3 pro sportovce i běžnou stravu. Jak číst etiketu, porovnat formy a dávky a kde najdete nabídky obchodů vedle sebe.',
    intro='<p>V kategorii <strong>vitamíny, minerály a omega-3</strong> najdete doplňky stravy ve formě tablet, kapslí, šumivých tablet, kapek i prášku. Jde o jednosložkové přípravky, třeba samotný vitamin D, hořčík nebo zinek, i o multivitaminové kombinace a rybí oleje. Všechno jsou to doplňky stravy, ne léky, a mají doplnit pestrou stravu, nikoli ji nahradit. Tahle stránka vysvětluje, jak číst etiketu a čím se liší formy a dávky.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a najdete tu značky <a href="/znacka/gymbeam/">GymBeam</a>, <a href="/znacka/greenfood-nutrition/">GreenFood Nutrition</a>, <a href="/znacka/medpharma/">MedPharma</a>, <a href="/znacka/viridian/">Viridian</a> nebo <a href="/znacka/ostrovit/">OstroVit</a>. Příbuzné skupiny jsou <a href="/sportovni-vyziva/">sportovní výživa</a>, <a href="/ostatni-doplnky-stravy/">další doplňky stravy</a> a <a href="/kolagen-a-klouby/">kolagen a kloubní výživa</a>. Před užíváním se poraďte s lékařem nebo lékárníkem.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Etikety a doporučení se mění podle země, a proto vždy čtěte pokyny výrobce a nepovažujte tento text za zdravotní doporučení. Má sloužit k orientaci v nabídce.</p>'
          '<p>Skupina je široká a pokrývá látky, které se v těle účastní řady procesů a které se přijímají hlavně potravou. Na stránce se potkávají tři hlavní typy přípravků, které se liší složením i tím, jak se etiketa čte.</p>'
          + T(['Skupina', 'Příklady v nabídce', 'Na co se dívat'], [
              ['Vitamíny', 'vitamin C, D, B-komplex, E, K a multivitaminy', 'forma vitaminu, množství v jedné dávce, kombinace s jinými látkami'],
              ['Minerály a stopové prvky', 'hořčík, zinek, železo, vápník, selen, draslík', 'sloučenina, ze které je minerál vyrobený, a obsah samotného prvku'],
              ['Omega-3 mastné kyseliny', 'rybí olej, krillový olej, řasový olej', 'obsah EPA a DHA, původ oleje, čerstvost a obal'],
              ['Multivitaminy a komplexy', 'komplexy pro sportovce, ženy, muže, seniory', 'seznam všech složek, ne jen název komplexu'],
              ['Šumivé a rozpustné formy', 'tablety do vody, prášky, kapky', 'obsah sladidel, pomocných látek a chuť']]) +
          '<p>Přípravky pro specifické skupiny, třeba pro klouby nebo vlasy, najdete jinde: kloubní výživa je v kategorii <a href="/kolagen-a-klouby/">kolagen a kloubní výživa</a>, rostlinné extrakty a probiotika v kategorii <a href="/ostatni-doplnky-stravy/">další doplňky stravy</a>.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<p>Etiketa vypovídá o přípravku víc než reklamní věta na obalu. Všímejte si několika údajů, které se u kvalitních výrobců uvádějí srozumitelně.</p>'
          '<ul><li><strong>Dávka a počet dávek v balení.</strong> Údaj „120 tablet" neříká nic, dokud nevíte, kolik jich tvoří jednu dávku. Jedna dávka může být jedna kapsle, nebo čtyři.</li>'
          '<li><strong>Množství látky v dávce.</strong> Vitaminy se uvádějí v miligramech nebo mikrogramech, někdy v jednotkách. Údaj bývá doplněn procentem referenční hodnoty příjmu.</li>'
          '<li><strong>Forma látky.</strong> Stejný minerál existuje v různých sloučeninách a obsah samotného prvku se v nich liší. Etiketa má uvádět, zda jde o obsah prvku, nebo sloučeniny.</li>'
          '<li><strong>Pomocné látky.</strong> Plnidla, protispékavé látky, sladidla a barviva jsou v seznamu složek. Alergici a vegani zkontrolují složení kapsle, protože může být želatinová.</li>'
          '<li><strong>Datum spotřeby a šarže.</strong> U olejů a omega-3 mastných kyselin je čerstvost obzvlášť důležitá.</li>'
          '<li><strong>Upozornění.</strong> Maximální doporučená denní dávka a pokyny pro těhotné nebo děti nesou povinnou informační hodnotu.</li></ul>'
          '<h2>Formy a jak se liší</h2>'
          '<p>Tablety jsou obvykle nejúspornější a mají dlouhou trvanlivost, ale mohou obsahovat více pomocných látek. Kapsle jsou měkké na polykání a bez chuti, přesto se u nich dávka počítá na kusy. Šumivé tablety se rozpouštějí ve vodě a hodí se pro ty, kdo nechtějí polykat, často však obsahují sladidla a kyselinu. Prášky a kapky umožňují jemnější dávkování, ovšem kapky se po otevření obvykle kazí rychleji. Omega-3 se prodávají v měkkých kapslích, kdy je olej uzavřený před kyslíkem, a v lahvičkách, kde se po otevření oxiduje. Vyberte formu, kterou opravdu budete užívat pravidelně: i nejlepší složení je k ničemu, když zůstane v zásuvce.</p>'
          '<h2>Rozdíly mezi vitaminy rozpustnými v tucích a ve vodě</h2>'
          '<p>Vitaminy se dělí do dvou základních skupin. Vitaminy A, D, E a K se rozpouštějí v tucích a ukládají se v těle, vitaminy skupiny B a vitamin C se rozpouštějí ve vodě. To je obecná informace z výživy a vysvětluje, proč etikety u vitaminů rozpustných v tucích doporučují užívání s jídlem, které obsahuje tuk. Také proto se u nich více dbá na dodržení doporučené dávky. Přesné množství a vhodnost pro vás vám řekne lékař nebo lékárník.</p>'
          '<h2>Multivitamin, nebo jednotlivé látky</h2>'
          '<p>Multivitamin je pohodlný, protože v jedné dávce poskytuje širokou škálu látek. Hodí se pro ty, kdo chtějí obecný doplněk bez řešení detailů. Jednosložkové přípravky se hodí tam, kde potřebujete konkrétní látku, a umožňují dávku nastavit přesněji. U multivitaminů sledujte, aby se na etiketě objevilo množství každé složky, ne jen název. U přípravků s mnoha složkami se také často stává, že se do tablety vejde jen malé množství každé látky.</p>'
          '<h2>Omega-3: rybí, krillový a řasový olej</h2>'
          '<p>Omega-3 mastné kyseliny EPA a DHA se získávají z mořských ryb, krillu nebo řas. Řasový olej je rostlinný, proto ho volí vegani a vegetariáni. U rybích olejů sledujte celkový obsah EPA a DHA v jedné dávce, ne jen množství oleje, protože tučný olej může obsahovat jen část těchto kyselin. Kvalitní výrobce uvádí původ a způsob zpracování a zpravidla i antioxidant, který olej chrání před žlukáním. Pozor na zápach: silně zatuchlý olej je znamením, že se zkazil. Oleje skladujte v chladu a tmě a po otevření dodržujte pokyn na obalu.</p>'
          '<h2>Pro koho jsou doplňky určeny</h2>'
          '<p>Běžný jídelníček obvykle většinu látek pokryje. Doplňky se proto nabízejí lidem, kteří mají zvláštní potřeby, třeba vegany, těhotné, seniory, sportovce se zvýšeným tréninkem nebo lidi s omezeným jídelníčkem. Jestli se vás to týká, zeptejte se lékaře, který zná vaši situaci. Samostatné rozhodování o vysokých dávkách nebo kombinacích s léky není rozumné. U dětí a těhotných se řiďte výhradně radou odborníka.</p>'
          '<h2>Sportovci a doplňky</h2>'
          '<p>Sportovci hledají doplňky nejčastěji v souvislosti s tréninkem a regenerací. Je dobré vědět, že doplňky nenahradí spánek, jídlo a odpočinek. Mají smysl až po tom, co jsou základy v pořádku. Vyvážený jídelníček kombinujte s <a href="/proteiny/">proteiny</a>, <a href="/iontove-napoje/">iontovými nápoji</a> nebo <a href="/energeticke-gely-a-tycinky/">energetickými gely a tyčinkami</a>. Pro stavbu svalů si prohlédněte <a href="/kreatin/">kreatin</a> a <a href="/aminokyseliny-bcaa/">aminokyseliny</a>. Závodní sportovci by měli ověřit, zda doplněk neobsahuje látky ze seznamu zakázaných.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Mezi nejčastější značky patří {B(("gymbeam", "GymBeam"), ("greenfood-nutrition", "GreenFood Nutrition"), ("medpharma", "MedPharma"), ("viridian", "Viridian"), ("ostrovit", "OstroVit"), ("movit-energy", "Movit Energy"), ("movit", "MOVit"), ("terezia", "Terezia"), ("vitaharmony", "VitaHarmony"), ("vitar", "Vitar"))}. '
          'Jejich nabídka se liší tím, na koho míří: některé míří na sportovce a nabízejí komplexy a šumivé tablety, jiné na běžné zákazníky s jednosložkovými přípravky nebo rostlinnými formami. Rozdíly poznáte z etikety, ne z názvu značky.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Srovnávání jen podle počtu tablet v balení, ne podle obsahu látky v dávce.</li>'
          '<li>Kombinování několika přípravků se stejnou látkou. Součet může překročit doporučenou dávku.</li>'
          '<li>Očekávání zázraků. Doplněk stravy není lék a nemá léčit.</li>'
          '<li>Opomenutí data spotřeby a podmínek skladování.</li>'
          '<li>Přehlédnutí alergenů a složení kapsle.</li>'
          '<li>Užívání na vlastní pěst při dlouhodobých obtížích. Příčinu má zjistit lékař.</li></ul>'
          '<h2>Jak porovnat dva podobné přípravky</h2>'
          '<p>Zvolte jednotný základ: vydělte cenu obchodu počtem dávek, nikoli počtem tablet, a porovnejte obsah látky v jedné dávce. Teprve potom srovnávejte formu látky, pomocné látky a velikost balení. Pamatujte, že větší balení se vyplatí jen tehdy, pokud ho stihnete spotřebovat před datem spotřeby. Na Sportece se obchody řadí vedle sebe, takže rozdíly v balení a dostupnosti uvidíte na první pohled.</p>'
          '<h2>Jak doplněk zařadit do dne</h2>'
          '<p>Při pravidelném užívání se vyplatí navázat dávku na zavedený zvyk, třeba na snídani nebo večeři. Přípravky s tukem rozpustnými složkami bývají doporučeny k jídlu, přípravky ve vodě rozpustné lze podle pokynu užít i mimo jídlo. Neslučujte několik nových přípravků najednou, protože pak nepoznáte, co vám vyhovuje a co ne. Zaznamenejte si, kdy jste začali a jakou dávku užíváte, a po uplynutí doby uvedené na obalu zhodnoťte, zda v užívání pokračovat. Součet všech dávek z různých přípravků nesmí překročit maximum uvedené výrobcem. Při jakýchkoli obtížích užívání ukončete a poraďte se s odborníkem.</p>'
          '<h2>Skladování</h2>'
          '<p>Doplňky skladujte na suchém místě bez přímého slunce a mimo dosah dětí. Koupelna je kvůli vlhkosti horší místo než kuchyňská skříňka. Lahvičku vždy pevně uzavřete a nevyhazujte sáček s pohlcovačem vlhkosti, pokud je v balení. Oleje a přípravky s probiotiky mohou vyžadovat chladničku, což je uvedeno na obalu.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>V kategorii porovnejte stejný přípravek u více obchodů a hlídejte velikost balení i počet dávek. Dva stejně vypadající produkty mohou obsahovat rozdílné množství látky, proto čtěte popis. Chcete-li doplnit i další oblasti, projděte <a href="/sportovni-vyziva/">sportovní výživu</a>, <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a> nebo <a href="/gainery/">gainery</a>. Pro regeneraci po tréninku se hodí i <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>',
    faq=[('Potřebuji vitaminy, když jím pestře?', 'Pestrá strava obvykle většinu potřebných látek pokryje. Doplňky mají smysl u určitých skupin nebo situací, o kterých nejlépe rozhodne lékař nebo lékárník podle vašeho stavu.'),
         ('Jaký je rozdíl mezi doplňkem stravy a lékem?', 'Doplněk stravy je potravina určená k doplnění stravy a nesmí tvrdit, že léčí onemocnění. Lék prochází jiným schvalováním a je určen k léčbě nebo prevenci nemoci.'),
         ('Jak číst údaj o množství v dávce?', 'Hledejte množství látky v jedné dávce a počet kusů na dávku. Údaj o obsahu prvku může být odlišný od celkové hmotnosti sloučeniny, proto čtěte, zda jde o samotný prvek.'),
         ('Mohu užívat vitaminy společně s léky?', 'Některé látky mohou s léky interagovat. Před kombinací se vždy poraďte s lékařem nebo lékárníkem a řiďte se příbalovým textem a pokyny výrobce.'),
         ('Kdy je lepší užívat vitaminy rozpustné v tucích?', 'Etikety obvykle radí užívat je s jídlem, které obsahuje tuk. Konkrétní pokyn najdete na obalu, případně ho zjistíte od lékárníka.'),
         ('Co je EPA a DHA?', 'Jsou to dva druhy omega-3 mastných kyselin obsažených v mořských olejích. Na etiketě rybího oleje sledujte jejich součet v jedné dávce, ne jen celkové množství oleje.'),
         ('Jaký je rozdíl mezi rybím, krillovým a řasovým olejem?', 'Liší se zdrojem: ryby, korýši krill nebo řasy. Řasový olej je rostlinný, takže ho zvolí vegani. Složení a obsah EPA a DHA se mezi přípravky liší.'),
         ('Jak poznat zkažený rybí olej?', 'Typicky silným žluklým zápachem nebo chutí. Pokud olej zapáchá nebo se obal poškodil, nepoužívejte ho. Dodržujte datum spotřeby a podmínky skladování uvedené na obalu.'),
         ('Je lepší užívat doplněk ráno, nebo večer?', 'Záleží na přípravku a pokynu výrobce na obalu. Důležitější než denní doba je pravidelnost a to, zda se užívá s jídlem nebo bez něj, jak etiketa uvádí.'),
         ('Mohou doplňky užívat děti a těhotné?', 'Jen po poradě s lékařem. Dávky a vhodnost se pro děti a těhotné liší od dospělých a některé látky se v těhotenství nedoporučují.'),
         ('Kde skladovat vitaminy?', 'Na suchém, tmavém místě mimo dosah dětí a mimo vlhkost koupelny. Lahvičku vždy pevně zavřete a dodržujte případné pokyny o chlazení, třeba u olejů a probiotik.')])
