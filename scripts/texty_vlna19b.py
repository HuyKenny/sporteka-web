"""sporteka.cz — wave 19b (4. 11. 2026): long texts (>= 1650 words) for karimatky-a-matrace, chranice-a-helmy, lyzarske-vosky, ploutve.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ karimatky-a-matrace
NEW['karimatky-a-matrace'] = dict(long=True,
    title='Karimatky a matrace: R-hodnota, typy a výběr',
    desc='Pěnové, samonafukovací i nafukovací karimatky a matrace do stanu. Jak číst R-hodnotu, vybrat rozměr a péči a kde porovnat nabídky obchodů.',
    intro='<p>Chlad se do spícího člověka nedostává zvenku, ale zespodu. Tělo tlačí na zem váhou, izolační vrstva ve spacáku se pod ním stlačí a teplo začne unikat do podkladu. Právě proto je podložka stejně důležitá jako samotné zavazadlo se spaním, a někdy důležitější. '
          'Správně zvolená karimatka rozhodne o tom, zda se ráno probudíte odpočatí, nebo promrzlí.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u pěnových, samonafukovacích i nafukovacích modelů od značek jako Yate, Husky, Therm A Rest, Pinguin nebo Sea to Summit. '
          'Podložka je součástí širší výbavy: podívejte se na <a href="/spaci-pytle/">spací pytle</a>, <a href="/stany/">stany</a>, <a href="/hamaky/">hamaky</a> a celý přehled <a href="/kemping/">kempingu</a>. Níže vysvětlujeme, jak číst parametry a čemu se při nákupu vyhnout.</p>',
    guide='<h2>Proč podložka rozhoduje o spánku venku</h2>'
          '<p>Spací pytel hřeje tím, že zadržuje vzduch v izolační výplni. Pod váhou těla se však výplň zploští a pod zády téměř neizoluje. Podložka tuto chybějící vrstvu nahrazuje: mezi tělem a podkladem vytvoří buď pěnu s uzavřenými buňkami, nebo vzduchovou komoru, případně jejich kombinaci. '
          'Kromě tepla řeší i komfort, protože vyrovnává kořeny, kameny a nerovnosti terénu. Dobrá podložka tedy plní dvě role najednou a obě se při výběru musí zvážit.</p>'
          '<h2>Tři základní typy</h2>'
          + T(['Typ', 'Princip', 'Hlavní výhoda', 'Hlavní nevýhoda'], [
              ['Pěnová karimatka', 'pěna s uzavřenými buňkami, jedno nebo více vrstev', 'nepropíchnete ji a nic nemusíte nafukovat', 'objemná a méně pohodlná'],
              ['Samonafukovací', 'pěnové jádro v plášti, nasaje vzduch po otevření ventilu', 'dobrý poměr komfortu a izolace', 'těžší a po složení stále velká'],
              ['Nafukovací matrace', 'vzduchové komory, někdy s izolační fólií nebo výplní', 'nejmenší sbalení při velké tloušťce', 'může se propíchnout a potřebuje pumpičku']]) +
          '<p>Pěnová karimatka je nejjednodušší volba pro člověka, který ji potřebuje jen občas, nebo pro ty, kteří ji berou na festival, k vodě nebo do chaty. Samonafukovací se hodí do auta a na kempování na jedno místo. Nafukovací matrace je přirozená volba pro pěší výpravy, kde každý litr objemu v batohu něco znamená.</p>'
          '<h2>R-hodnota: jak ji číst</h2>'
          '<p>R-hodnota vyjadřuje odpor proti prostupu tepla. Čím je vyšší, tím méně tepla z těla odchází do země. Hodnota se skládá, takže dvě podložky přes sebe mají hodnotu přibližně součtovou. To je užitečné v zimě: pěnovou karimatku lze dát pod nafukovací matraci a dosáhnout vyšší izolace i bezpečné rezervy při propíchnutí. '
          'Porovnávat spolehlivě lze jen hodnoty měřené stejným způsobem, proto se při výběru držte údajů výrobce a dívejte se, zda uvádí, podle jakého postupu je měřil.</p>'
          + T(['Podmínky', 'Orientační R-hodnota', 'Poznámka'], [
              ['Teplé letní noci', 'zhruba 1 až 2', 'stačí tenká pěna nebo lehká matrace'],
              ['Tři roční období', 'zhruba 3 až 4', 'jaro, podzim a studené letní noci v horách'],
              ['Zima, sníh, zmrzlá zem', '5 a více', 'často se kombinuje dvojitá podložka'],
              ['Spaní na betonu nebo kameni', 'o stupeň výš než obvykle', 'tvrdé podklady odebírají teplo rychleji']]) +
          '<p>Hodnoty jsou jen orientační. Zmrzlý člověk si kromě podložky často stěžuje i na vlhký spacák, jídlo před spaním a oblečení, které na noc zůstalo mokré. Podložku proto hodnoťte jako součást celku, ne jako kouzelný prostředek.</p>'
          '<h2>Rozměry: délka, šířka, tloušťka</h2>'
          '<p>Standardní délka většiny podložek odpovídá dospělému člověku do běžné výšky, kratší verze se hodí pro děti nebo pro lehké varianty, kde spíte s batohem pod nohama. Šířka se pohybuje od úzkých modelů po široké varianty pro ty, kdo se ve spánku hodně otáčejí. '
          'Tloušťka souvisí s komfortem na boku: kdo spí na boku, ocení víc vzduchu pod kyčlí a ramenem, zatímco spáč na zádech vystačí s tenčím modelem. Do úzkého stanu se širší podložka nemusí vejít, takže si ověřte i vnitřní rozměr <a href="/turisticke-stany/">turistického stanu</a>.</p>'
          '<h3>Tvary a speciální konstrukce</h3>'
          '<p>Mumiový tvar ušetří váhu a objem, protože u nohou zůstává užší. Obdélníková podložka je prostornější a lépe se kombinuje do dvojice. Některé nafukovací matrace mají spojitelné okraje nebo ventil, který lze použít i pro nafukování pomocí vaku, aby se do matrace nedostávala vlhkost z dechu. '
          'Vlhkost uvnitř je u péřových modelů i u vzduchových komor s izolační výplní nepřítel, takže pumpa nebo nafukovací vak bývá chytřejší cestou než plíce.</p>'
          '<h2>Výběr podle způsobu využití</h2>'
          '<h3>Pěší trek a lehký batoh</h3>'
          '<p>Rozhodují váha a objem po sbalení. Nafukovací matrace nabízí nejlepší poměr, pěnová skládací karimatka je odolnější a hodí se tam, kde nechcete řešit riziko propíchnutí. Podložka se obvykle nosí zvenku <a href="/turisticke-batohy/">turistického batohu</a>, takže musí odolat větvím a dešti.</p>'
          '<h3>Kemp u auta</h3>'
          '<p>Tady nerozhoduje váha, ale pohodlí. Široká samonafukovací nebo silná nafukovací matrace s dobrým povrchem změní spaní ve stanu na něco, co se podobá posteli. Ke kempu patří i <a href="/kempingovy-nabytek/">kempingový nábytek</a> a <a href="/vareni-v-prirode/">vybavení pro vaření</a>.</p>'
          '<h3>Děti a rodinné stany</h3>'
          '<p>Děti se v noci pohybují víc a kopou do stěn, proto se hodí robustní podložky, které se snadno utřou. Pěnové modely snesou i ostré hrany a špínu. V rodinném stanu lze podložky spojit do plochy, aby se mezi nimi neotevíraly mezery. Pro zvolení správné velikosti stanu pomůže kategorie <a href="/rodinne-stany/">rodinné stany</a>.</p>'
          '<h3>Hamak, bivak a alternativy</h3>'
          '<p>V <a href="/hamaky/">hamaku</a> se izolace přidává zespodu jiným způsobem, protože zespodu proudí vzduch a stlačená výplň nepomáhá. Pod bivak se hodí tenčí pěnová podložka, která je zároveň sedátkem. Při táboření se hodí i <a href="/stanove-doplnky/">stanové doplňky</a> jako podlážka nebo kolíky, které chrání materiál podložky.</p>'
          '<h2>Povrch, ventil a materiály</h2>'
          '<p>Povrch rozhoduje o tom, zda podložka po stanové podlážce klouže. Protiskluzová úprava nebo jemný potah z polyesteru pomáhá, hladký nylon klouže víc. Vnější látka musí odolat otěru; silnější materiál váží víc, ale přežije kamínky. '
          'Ventil má být velký, aby se matrace rychle nafoukla i vypustila, a dobře zavíratelný. Některé modely mají dva ventily, jeden pro nafouknutí a druhý pro rychlé vypuštění. Pro pěnové podložky je důležité, aby byla pěna s uzavřenými buňkami, protože nenasákne vodou.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Před použitím vždy zkontrolujte povrch terénu a odstraňte šišky, kameny a trny.</li>'
          '<li>Pod stan odstraňte ostré předměty a použijte podložku pod stan, aby se podlážka i matrace nepoškodily.</li>'
          '<li>Po použití matraci vysušte, otřete vlhkost z vnitřku a skladujte ji rozbalenou nebo volně srolovanou s otevřeným ventilem.</li>'
          '<li>Samonafukovací modely nenechávejte dlouho stlačené v pytli, pěna by ztratila schopnost nasát vzduch.</li>'
          '<li>Před cestou vždy vyzkoušejte nafouknutí doma a nechte matraci přes noc ležet, aby se projevil případný únik.</li>'
          '<li>Opravná sada patří do každého sbaleného zavazadla, i když se zdá, že matrace je v perfektním stavu.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<p>Nejčastější chybou je kupovat podle tloušťky bez pohledu na R-hodnotu: silná matrace bez izolace v zimě stejně studí. Druhá chyba je přílišná tvrdost, kdy člověk matraci nafoukne příliš, aby neležel nízko, a tělo pak neleží, ale balancuje. '
          'Třetí past je ignorování rozměru po složení. Podložka, která se nevejde do batohu, skončí připevněná venku a trpí. Čtvrtou chybou je nákup podle dojmu z obchodu bez ověření, zda se matrace vejde do stanu a zda je ve dvou vedle sebe dost místa.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší zastoupení mají {B(("yate", "Yate"), ("husky", "Husky"), ("therm-a-rest", "Therm A Rest"), ("pinguin", "Pinguin"), ("sea-to-summit", "Sea to Summit"), ("sedco", "Sedco"), ("crossroad", "Crossroad"), ("naturehike", "Naturehike"), ("nils", "Nils"), ("trimm", "Trimm"), ("hannah", "Hannah"), ("highlander", "Highlander"))}. '
          'České značky bývají silné u pěnových a samonafukovacích podložek, zahraniční výrobci jako Therm A Rest a Sea to Summit u lehkých nafukovacích. Porovnávat ale nemá smysl jen podle logotypu: srovnávejte hmotnost, rozměr, R-hodnotu a typ ventilu.</p>'
          '<h2>Jak nakupovat přes porovnání obchodů</h2>'
          '<p>Stejná podložka se v různých obchodech liší nejen cenou, ale i dostupností velikostí a barev, dobou dodání a možností vrácení. Na Sportece vidíte vedle sebe více nabídek a můžete se rozhodnout podle toho, který obchod má skladem právě tu verzi, kterou potřebujete. '
          'Zkontrolujte název modelu, rozměry a R-hodnotu, protože v některých řadách se liší jen jedním číslem. Při koupi pro víc lidí se vyplatí vzít stejný model, aby se podložky daly spojit.</p>'
          '<p>K podložce se hodí i <a href="/vlozky-do-spacaku/">vložky do spacáků</a> pro hygienu a teplo, <a href="/perove-spacaky/">péřové spacáky</a> a <a href="/dekove-spacaky/">dekové spacáky</a> podle typu výletu. Pro cvičení a doma slouží zcela jiná kategorie <a href="/joga-a-podlozky/">jóga a podložky</a>.</p>',
    faq=[('Jaká R-hodnota je správná pro stanování na jaře a na podzim?', 'Na studené noci mimo léto se obvykle hodí R-hodnota kolem 3 až 4. Při noční teplotě kolem nuly nebo na zmrzlé půdě je lepší jít výš, případně položit pod hlavní podložku tenkou pěnu.'),
         ('Je lepší pěnová karimatka, nebo nafukovací matrace?', 'Záleží na využití. Pěnová je odolná, bez rizika propíchnutí a levnější na údržbu, nafukovací je pohodlnější a po sbalení výrazně menší. Na pěší túry se obvykle volí nafukovací, do auta cokoli.'),
         ('Jak poznám, že se matrace propíchla?', 'Večer ji nafoukněte a nechte přes noc. Pokud ráno změkne, hledejte únik ponořením do vody nebo potřením mýdlovou pěnou, kde začnou vznikat bublinky. Místo osušte, označte a přelepte opravnou záplatou.'),
         ('Jaká délka a šířka podložky je vhodná?', 'Vhodná je taková, na které leží celé tělo od ramen po paty a do které se vejdete i při otočení. Kdo spí neklidně, zvolí širší model. Rozměry se musí vejít do stanu vedle spolunocležníka.'),
         ('Můžu spojit dvě podložky přes sebe?', 'Ano, R-hodnoty se skládají přibližně jako součet, takže kombinace pěny a nafukovací matrace zvyšuje izolaci i bezpečnost při propíchnutí. Pěna se pokládá dole, matrace nahoře.'),
         ('Jak podložku nafukovat, aby uvnitř nebyla vlhkost?', 'Nejlepší je pumpička nebo nafukovací vak, protože vzduch z plic je teplý a vlhký. Vlhkost uvnitř může zhoršit izolační vlastnosti a časem způsobí plísně, proto matraci po použití vysušte.'),
         ('Jak skladovat samonafukovací karimatku?', 'Doma ji nechte rozbalenou s otevřeným ventilem, třeba pod postelí nebo ve skříni. Dlouhodobě stlačená pěna ztrácí schopnost nasát vzduch a podložka se pak nafukuje pomaleji.'),
         ('Hodí se matrace do hamaku?', 'Standardní matrace v hamaku obvykle sjíždí na stranu a nedrží tvar. Do hamaku se používá speciální izolační podložka nebo spodní přikrývka, která kopíruje tvar hamaku a nestlačí se.'),
         ('Hodí se karimatka i na cvičení?', 'Silnější pěnová karimatka se použít dá, ale na cvičení se obvykle vybírají podložky s vhodným povrchem a protiskluzovou úpravou. Takové najdete v samostatné kategorii jóga a podložky.'),
         ('Kdy je nejlepší čas na nákup?', 'Sezónní zboží bývá výhodné mimo hlavní sezónu, tedy na podzim a v zimě. Na Sportece lze pozorovat vývoj nabídek obchodů a porovnat, kdy se právě objevily nové skladové zásoby.')],
)

# ------------------------------------------------------------------ chranice-a-helmy
NEW['chranice-a-helmy'] = dict(long=True,
    title='Chrániče a helmy: výběr, velikost a použití',
    desc='Helmy, chrániče kolen a loktů, páteře i holení pro kolo, brusle, koloběžku a kontaktní sporty. Jak vybrat velikost, certifikaci a péči o ochranu.',
    intro='<p>Ochranná výbava neslouží k tomu, aby zabránila pádu, ale aby z něj udělala nepříjemný zážitek, a ne zranění. Přilba tlumí náraz do hlavy, chrániče kolen a loktů chrání klouby, které se při pádu zasahují nejčastěji, a speciální chrániče páteře, holení nebo hrudníku řeší rizika konkrétních sportů. '
          'Aby ochrana fungovala, musí dobře sedět, být určená pro daný sport a nesmí být poškozená.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u helem a chráničů od značek jako Met, Bauer, Bluegrass, Rossignol, Opro nebo Arcore. Podle sportu navazují kategorie <a href="/inline-brusle/">inline brusle</a>, <a href="/kolobezky/">koloběžky</a>, <a href="/skateboardy/">skateboardy</a>, <a href="/cyklisticke-helmy/">cyklistické helmy</a> a <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>. Níže najdete postup výběru a časté chyby.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Kategorie sdružuje ochranné pomůcky, které se nevešly do užších oddílů nebo se používají napříč sporty. Najdete tu přilby pro jízdu na kole, koloběžce a bruslích, dětské i dospělé, chrániče kolen, loktů a zápěstí, chrániče páteře a hrudníku, holenní chrániče a boxerské helmy. '
          'Úzce specializované sady zůstávají ve vlastních oddílech: <a href="/hokejove-chranice/">hokejové chrániče</a>, <a href="/hokejove-helmy-a-mrizky/">hokejové helmy a mřížky</a>, <a href="/snowboardove-chranice/">snowboardové chrániče</a> nebo <a href="/jezdecke-helmy/">jezdecké helmy</a>. Je dobré se podívat i tam, pokud sportujete mimo střed této nabídky.</p>'
          + T(['Ochrana', 'Kryje', 'Typické použití'], [
              ['Přilba', 'hlava a lebka', 'kolo, koloběžka, brusle, skate'],
              ['Chrániče kolen', 'kolenní kloub a čéška', 'brusle, skate, MTB, volejbal'],
              ['Chrániče loktů', 'loket a předloktí', 'brusle, skate, koloběžka'],
              ['Chrániče zápěstí', 'zápěstí a dlaň', 'brusle, snowboard, longboard'],
              ['Chránič páteře', 'záda a páteř', 'MTB, enduro, lyžování, jízda na koni'],
              ['Chrániče holení', 'holeň a nárt', 'fotbal, thajský box, kickbox'],
              ['Boxerská helma', 'hlava při tréninku', 'box, MMA, sparing']]) +
          '<h2>Přilba: jak má sedět</h2>'
          '<p>Přilba plní svou funkci jen tehdy, když sedí rovně a pevně. Okraj by měl být zhruba dva prsty nad obočím, nikoli posunutý dozadu. Řemínky tvoří trojúhelník kolem uší a zapínání pod bradou má dovolit prostrčit jen jeden prst. '
          'Přilba se při zatřesení hlavou nesmí posouvat. Nejlepší je kombinace měření obvodu hlavy, výrobní tabulky a zkoušky v obchodě. Dětské helmy mají často kolečko na zadní straně, kterým se přizpůsobí obvodu, a rostou s dítětem.</p>'
          '<h3>MIPS a podobné systémy</h3>'
          '<p>Některé helmy obsahují systém, který umožňuje vnitřní vrstvě mírně se posunout vůči skořepině při šikmém nárazu. Funguje to jako dodatečná vrstva, která má omezit rotační pohyb hlavy. Takové modely nabízí například Met v řadách pro město i terén. Systém je přínosem, ale neřeší základní předpoklad: správnou velikost a nepoškozenou přilbu.</p>'
          '<h3>Typy přileb</h3>'
          '<ul><li><strong>Silniční a gravel:</strong> lehké, větrané, s malým kšiltem nebo bez něj.</li>'
          '<li><strong>MTB a terénní:</strong> hlouběji sahají do týlu a mají kšilt, viz <a href="/mtb-a-integralni-helmy/">MTB a integrální helmy</a>.</li>'
          '<li><strong>Městské:</strong> často s integrovaným světlem, viz <a href="/mestske-cyklohelmy/">městské cyklistické helmy</a>.</li>'
          '<li><strong>Skate a freestyle:</strong> kulatější tvar, silnější skořepina a menší větrání.</li>'
          '<li><strong>Dětské:</strong> více pěny kolem čela a barevnější provedení, viz <a href="/detske-cyklohelmy/">dětské cyklistické helmy</a>.</li></ul>'
          '<h2>Chrániče kolen, loktů a zápěstí</h2>'
          '<p>Kloub, který se při pádu zasahuje jako první, je zápěstí, následují lokty a kolena. Proto sady chráničů obsahují obvykle všechny tři části. Měkké neoprenové chrániče nabízejí komfort a hodí se na jízdu, kde jde hlavně o odřeniny. Tvrdá skořepina z plastu rozloží náraz na větší plochu a hodí se na brusle a skate, kde se klouže po asfaltu. '
          'Kolena chraňte vždy, pokud jezdíte na terénu s hrbolky. Pro dospělé i děti se hodí kombinace chráničů s délkou, která kryje čéšku a část holeně.</p>'
          + T(['Konstrukce', 'Výhoda', 'Nevýhoda'], [
              ['Měkká pěna a neopren', 'pohodlná, nenápadná', 'chrání hlavně před odřením'],
              ['Tvrdá skořepina', 'rozloží náraz a klouže po povrchu', 'je méně prodyšná a těžší'],
              ['Hybridní stavba', 'komfort s ochranou pro kritická místa', 'bývá dražší a složitější na čištění']]) +
          '<p>Velikost chráničů se volí podle obvodu nad a pod kloubem, protože chránič musí držet při pohybu na místě. Pokud sjíždí, bývá buď příliš velký, nebo má měkké zapínání. Příliš těsný chránič naopak omezuje oběh krve a nepohodlí vás přiměje ho sundat.</p>'
          '<h2>Chrániče páteře a hrudníku</h2>'
          '<p>Chránič páteře se nosí jako vesta nebo samostatný segmentový pás. Řady od Arcore, Bluegrass nebo Rossignol jsou pro terénní jízdu, lyžování a podobné sporty, kde hrozí pád na záda. Pěna v kombinaci s pevnými segmenty rozloží náraz do větší plochy. '
          'Důležité je, aby chránič držel zakrytá místa po celou dobu pohybu. Nosí se pod nebo přes oblečení podle konstrukce, a velikost se volí hlavně podle délky zad, nikoli podle konfekční velikosti. Pro snowboard a lyže vyberte v kategorii <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/snowboardove-chranice/">snowboardové chrániče</a>.</p>'
          '<h2>Kontaktní sporty: boxerské helmy a holenní chrániče</h2>'
          '<p>Na tréninku se používá helma, která chrání hlavu a obličej při sparingu. Kožená či syntetická skořepina s vnitřní pěnou pokrývá spánky, čelo a v některých modelech i nos. Značky jako Leone 1947, Bushido nebo RDX nabízejí modely s různou výplní a zapínáním. '
          'Helma má zůstat pevně na hlavě a nesmí omezit zorné pole. Holenní chrániče si vybírejte podle délky holeně a podle sportu: pro thajský box se hodí delší a pevnější, pro fotbal lehčí a užší. K tréninku patří i <a href="/boxerske-rukavice/">boxerské rukavice</a> a další vybavení v kategorii <a href="/bojove-sporty/">bojové sporty</a>. Chrániče zubů, například od značky Opro, se tvarují podle chrupu a řeší jinou rovinu ochrany než přilba.</p>'
          '<h2>Výběr podle sportu</h2>'
          '<h3>Inline brusle a skateboard</h3>'
          '<p>Základ tvoří přilba a trojice chráničů kolen, loktů a zápěstí. Brusle patří do skupiny <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a>. Začátečníkům se doporučuje nosit celou sadu, protože první pády bývají nejčastější.</p>'
          '<h3>Koloběžky a odrážedla</h3>'
          '<p>Pro koloběžku volte lehkou přilbu s dobrou ventilací a chrániče na kolena a lokty u dětí. U elektrických modelů je rozumné zvolit pevnější přilbu s delším krytím týlu. Podívejte se i do kategorie <a href="/elektrokolobezky/">elektrokoloběžky</a> a <a href="/freestyle-kolobezky/">freestyle koloběžky</a>.</p>'
          '<h3>Cyklistika</h3>'
          '<p>Pro kolo vybírejte přilbu podle disciplíny a doplňte ji o <a href="/cyklo-chranice/">cyklistické chrániče</a>. Na silnici stačí lehká přilba, v terénu sáhněte po pevnější s kšiltem a chrániči kolen.</p>'
          '<h3>Děti</h3>'
          '<p>Děti potřebují helmu ve správné velikosti, nikoli o číslo větší, aby do ní dorostly. Dětské helmy Met a Bluegrass mají jednoduché nastavení obvodu. Doma zkuste, zda dítě s přilbou normálně sedí, a hlavně zda ji ochotně nosí, protože i dobrá ochrana, která zůstane doma, nechrání.</p>'
          '<h2>Normy a označení</h2>'
          '<p>Na přilbách bývá označení CE a odkaz na normu pro daný sport, například EN 1078 pro kolo, koloběžku a brusle nebo EN 1077 pro lyžování. U ochranných pomůcek jiných sportů se řiďte údajem výrobce o určení. Chrániče obvykle uvádějí, pro jakou činnost jsou určeny. Vyhněte se výrobkům, které uvádějí jen velikost a barvu bez určení účelu. Ochrana pro jízdu na kole není stejná jako ochrana pro box a naopak, proto výrobce vždy ověřte u konkrétního modelu.</p>'
          '<h2>Péče a výměna</h2>'
          '<ul><li>Po pádu nebo silném nárazu přilbu vyměňte, i když vypadá neporušená. Pěna se mohla stlačit.</li>'
          '<li>Čistěte vlažnou vodou a jemným mýdlem, žádná rozpouštědla nebo agresivní chemie.</li>'
          '<li>Neskladujte na slunci nebo u topení, kde by se plast a pěna mohly poškodit.</li>'
          '<li>Pravidelně kontrolujte řemínky, přezky a nastavovací kolečko.</li>'
          '<li>Chrániče po použití vysušte, aby neplesnivěly a nezapáchaly.</li>'
          '<li>U dětí kontrolujte velikost každou sezónu, protože hlava roste a chrániče se brzy změní z ochranných na zbytečné.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<p>Nejčastější chybou je nákup příliš velké přilby na dorost. Druhá je přilba nasazená dozadu, která nechrání čelo. Třetí je kupovat chrániče bez ohledu na typ sportu, protože výrobek pro skate se nehodí na box. Čtvrtá je používání po pádu, protože poškozená ochrana se na první pohled nemusí zdát poškozená. '
          'A pátá, velmi častá chyba je ušetřit na tom, co se nosí nejvíc, a koupit velmi levnou přilbu bez řádného zapínání, kterou dítě po týdnu přestane používat.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii najdete značky {B(("met", "Met"), ("bauer", "Bauer"), ("bluegrass", "Bluegrass"), ("rossignol", "Rossignol"), ("opro", "Opro"), ("arcore", "Arcore"), ("leone-1947", "Leone 1947"), ("alpina", "Alpina"), ("bushido", "Bushido"))}. '
          'Přehled na Sportece vám umožní porovnat nabídky obchodů u jednoho modelu a vybrat tu s dostupnou velikostí. Dívejte se na rozměry, typ upevnění a určení pro sport, nikoli pouze na barvu. Doplnit lze například <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, které slouží při zotavování po úrazech, a <a href="/odrazedla/">odrážedla</a> pro nejmenší jezdce.</p>',
    faq=[('Jak zjistím správnou velikost přilby?', 'Změřte obvod hlavy krejčovským metrem nad obočím a nad ušima. Výsledek porovnejte s tabulkou výrobce a přilbu vždy vyzkoušejte: nesmí se hýbat, okraj sedí nad obočím a řemínky tvoří trojúhelník kolem uší.'),
         ('Je nutné vyměnit přilbu po pádu?', 'Ano, doporučuje se ji vyměnit. Pěna uvnitř se při nárazu stlačí a při dalším nárazu už tlumí hůř, i když skořepina vypadá bez poškození.'),
         ('Jaká helma je vhodná pro dítě?', 'Taková, která sedí, má nastavitelný obvod a je pro daný sport určená. Neplatí pravidlo, že dítě do přilby dorůstá, protože příliš velká helma se pohybuje a nechrání.'),
         ('Co znamená systém MIPS?', 'Je to doplňková vrstva, která umožňuje mírný posun vnitřní části přilby při šikmém nárazu. Má omezit rotační pohyb hlavy. Je to doplněk, ne náhrada správné velikosti.'),
         ('Jak vybrat chrániče kolen a loktů?', 'Podle sportu, obvodu končetiny a konstrukce. Pro brusle a skate se hodí tvrdší skořepina, pro rekreační jízdu stačí měkčí pěna. Chránič nesmí při pohybu sjíždět.'),
         ('Potřebuji chránič páteře?', 'Při terénní jízdě na kole, lyžování nebo snowboardu, kde hrozí pád na záda, je užitečný. Pro běžnou jízdu po cyklostezce obvykle nezbytný není, ale rozhodnutí závisí na riziku a vašem stylu.'),
         ('Čím se liší boxerská helma od cyklistické?', 'Boxerská helma chrání při sparingu proti úderům a nosí se spolu s rukavicemi. Cyklistická je určená pro náraz při pádu. Používat je mají jen pro ten sport, pro který jsou vyrobené.'),
         ('Jak čistit helmu a chrániče?', 'Vlažnou vodou a jemným mýdlem, bez rozpouštědel. Po vyčištění nechte vyschnout na vzduchu mimo přímé slunce a topení. Textilní popruhy a vnitřní vložky lze u většiny modelů vyprat podle návodu výrobce.'),
         ('Jak dlouho helma vydrží?', 'Záleží na výrobci, ale obecně se doporučuje měnit helmy po několika letech používání, protože pěna a plasty stárnou vlivem slunce, potu a teploty. Údaje najdete v pokynech výrobce.'),
         ('Mohou si děti půjčit helmu po sourozenci?', 'Pokud sedí, je v dobrém stavu, nebyla v pádu a je určena pro daný sport, může. Jinak je lepší koupit novou, protože použitá přilba mohla utrpět neviditelné poškození.')],
)

# ------------------------------------------------------------------ lyzarske-vosky
NEW['lyzarske-vosky'] = dict(long=True,
    title='Lyžařské vosky: druhy, teploty a mazání lyží',
    desc='Vosky na sjezdové i běžecké lyže a snowboard: skluzné, stoupací, základní, odstraňovače a nářadí. Jak vybrat podle teploty sněhu a jak mazat.',
    intro='<p>Skluznice lyže je porézní plast, který při nepoužívání vysychá, matní a ztrácí rychlost. Vosk dodá skluznici zpět tuk, zaplní póry a vytvoří tenký film, který na sněhu snižuje tření. Dobře namazané lyže jedou rychleji, lépe reagují při zatáčení a skluznice déle vydrží. '
          'U běžek navíc vosk často rozhoduje o tom, zda lyže stoupají do kopce, nebo prokluzují.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů u vosků a příslušenství od značek jako Swix, Star Ski Wax, Holmenkol, Toko nebo Vauhti. Údržba lyží navazuje na oddíly <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/bezecke-lyze/">běžecké lyže</a>, <a href="/snowboardy/">snowboardy</a> a <a href="/lyzarske-doplnky/">lyžařské doplňky</a>. Níže najdete rozbor druhů vosků, postup mazání i seznam toho, co do dílny patří.</p>',
    guide='<h2>K čemu se vosk používá</h2>'
          '<p>Voskování má tři úkoly. Zaprvé snižuje tření mezi skluznicí a sněhem, takže lyže lépe kloužou. Zadruhé chrání materiál před vysycháním a oxidací, které se projevují šedým, matným povrchem. Zatřetí vylepšuje ovladatelnost: lyže s vyživenou skluznicí drží stopu a nelepí se ve vlhkém sněhu. '
          'Na umělém sněhu, na starém sněhu s nečistotami nebo při velmi nízkých teplotách se rozdíly zvětšují, a proto závodníci vosk volí velmi pečlivě.</p>'
          '<h2>Základní druhy vosků</h2>'
          + T(['Druh', 'Použití', 'Poznámka'], [
              ['Skluzný vosk tuhý', 'nanáší se žehličkou nebo třením', 'vsákne se do skluznice, vydrží nejdéle'],
              ['Skluzný vosk tekutý nebo sprej', 'rychlé doplnění, aplikace houbičkou', 'hodí se na trasu, nenahradí důkladné mazání'],
              ['Základní vosk', 'příprava nové nebo suché skluznice', 'bývá měkčí a nasákne hlouběji'],
              ['Stoupací vosk a stick', 'střed klasické běžky', 'dává záběr při odrazu'],
              ['Klistr a pásky', 'mokrý nebo kluzký sníh', 'používá se tam, kde stoupací vosk nestačí'],
              ['Odstraňovač a čistič', 'odstranění starého vosku a nečistot', 'před novým nanášením']]) +
          '<p>Většina výrobců rozlišuje vosky podle teplotního rozsahu, často značeného barvou a údajem o teplotě sněhu. Teplý vosk je měkčí a hodí se pro vlhký sníh, studený je tvrdší a lépe odolává ostrým krystalům při mrazu. '
          'Univerzální vosky pokrývají široké rozmezí a pro rekreační lyžaře jsou praktickou volbou, protože netřeba hlídat teploměr.</p>'
          '<h2>Skluzné vosky pro sjezd a snowboard</h2>'
          '<p>U sjezdových lyží a snowboardů se obvykle používá skluzný vosk nanášený horkou cestou. Rozehřátá žehlička rozpustí vosk, který zateče do pórů skluznice. Po vychladnutí se přebytek seškrábe plastovou škrabkou a povrch se vykartáčuje. '
          'Postup je stejný pro lyže i snowboard, rozdíl je pouze v tom, že snowboard má jedinou širokou plochu a často se voskuje dvakrát za sezónu. Na umělém sněhu a při rozmrzání je užitečné vzít si sprej, který lze nanést přímo na svahu.</p>'
          '<h2>Běžecké lyže: skluz a záběr</h2>'
          '<p>Běžecké lyže mají dvě různé zóny. Skluzná část na špičce a patě se voskuje stejně jako sjezdovka, jen se používají jemnější vosky. Střední stoupací část u klasických lyží potřebuje vosk nebo klistr, který se zachytí o sníh při odrazu. '
          'Skate lyže voskujete jen na skluz, což je jednodušší. U lyží s šupinami nebo stoupacím pásem vosk na záběr nepotřebujete, ale skluzná část se mazat musí.</p>'
          + T(['Podmínky', 'Skluzný vosk', 'Záběr u klasiky'], [
              ['Mráz a suchý sníh', 'tvrdší, studený vosk', 'tvrdší stoupací vosk'],
              ['Kolem nuly', 'střední vosk', 'tvrdý nebo měkký podle zrna'],
              ['Mokrý sníh nad nulou', 'měkký, teplý vosk', 'klistr nebo speciální vosk'],
              ['Umělý sníh', 'odolnější vosk s přísadami', 'podle teploty a vlhkosti']]) +
          '<p>Tabulka je jen orientační. Skutečné podmínky se mění během dne, a proto se vyplatí řídit se pokyny výrobce vosku a po první zkoušce upravit volbu. Zkušení běžkaři si proto vozí několik tyčinek a kombinují je podle toho, co zrovna stopa dělá.</p>'
          '<h2>Postup mazání krok za krokem</h2>'
          '<ol><li>Lyži upněte do svěráku nebo na stojan skluznicí nahoru.</li>'
          '<li>Skluznici očistěte čističem a nechte oschnout.</li>'
          '<li>Nanášejte vosk na rozehřátou žehličku a nechte ho kapat na skluznici po celé délce.</li>'
          '<li>Rozetřete vosk rovnoměrně žehličkou, která se neustále pohybuje, aby se skluznice nepřehřála.</li>'
          '<li>Počkejte, až vosk úplně vychladne, obvykle půl hodiny nebo déle.</li>'
          '<li>Seškrábejte přebytek plastovou škrabkou od špičky k patě.</li>'
          '<li>Vykartáčujte skluznici nylonovým nebo koňským kartáčem, aby se vyčistila struktura.</li></ol>'
          '<p>Při práci větrejte, protože roztavený vosk uvolňuje páry, a nikdy nenechávejte horkou žehličku bez dozoru. Používejte žehličku určenou pro lyže, protože běžná domácí nemá stabilní teplotu a může skluznici spálit.</p>'
          '<h2>Nářadí do dílny</h2>'
          '<ul><li><strong>Žehlička na lyže:</strong> s regulací teploty, aby se vosk neroztavil příliš ani málo.</li>'
          '<li><strong>Plastová škrabka:</strong> plexi o tloušťce kolem pěti milimetrů je standard.</li>'
          '<li><strong>Kartáče:</strong> nylonový na odstranění zbytků, jemný koňský nebo mosazný podle potřeby.</li>'
          '<li><strong>Svěrák nebo stojan:</strong> lyže se při škrábání nesmí pohybovat.</li>'
          '<li><strong>Ostřič hran:</strong> k údržbě hran před mazáním, viz <a href="/lyzarske-doplnky/">lyžařské doplňky</a>.</li>'
          '<li><strong>Čistič a utěrky:</strong> bez nich se vosk nanáší na špínu.</li></ul>'
          '<h2>Jak často mazat</h2>'
          '<p>Nejjednodušší pravidlo zní: skluznice by nikdy neměla vypadat suše a šedě. Před sezónou se vyplatí dvě vrstvy základního vosku, následně doplňování podle používání. Pro rekreační lyžaře, kteří jezdí pár dnů v zimě, stačí namazat lyže před sezónou a případně jednou v průběhu. '
          'Pro pravidelné jezdce a běžkaře se mazání opakuje po několika dnech provozu nebo před důležitou akcí. Na konci sezóny naneste silnější vrstvu vosku a nechte ho na skluznici, aby ji přes léto chránil.</p>'
          '<h2>Skladování a ochrana</h2>'
          '<p>Lyže skladujte na suchém a chladném místě s ochranou hran proti rzi. Přepravní vaky a pouzdra najdete v kategorii <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>. Před uskladněním očistěte skluznici a hrany, hrany lehce přetřete olejem nebo voskem a lyže stáhněte páskem, aby se nepřekřížily. '
          'Nevystavujte je přímému slunci ani topení. Jen tak zůstanou ploché a skluznice nevyschne.</p>'
          '<h2>Pro koho jaký vosk</h2>'
          '<h3>Začátečník</h3>'
          '<p>Stačí univerzální vosk, plastová škrabka, kartáč a jednoduchá žehlička. Pokud ještě nechcete mazat sami, svěřte lyže servisu a sledujte, jak se skluznice mění. Výbavu doplňte o <a href="/lyzarske-boty/">lyžařské boty</a> a <a href="/lyzarske-vazani/">vázání</a>, které se musí seřídit samostatně.</p>'
          '<h3>Rekreační běžkař</h3>'
          '<p>Klasik potřebuje skluzný vosk a stoupací vosk nebo klistr. Praktická je sada, která pokryje běžné podmínky. Doplňte ji o <a href="/bezecke-boty/">běžecké boty</a> a <a href="/bezecke-vazani/">běžecké vázání</a>, které stejně určují pohodlí.</p>'
          '<h3>Skialpinista</h3>'
          '<p>Důležitější než skluz je u skialpinismu údržba stoupacích pásů a jejich lepidla, viz <a href="/skialpove-pasy/">skialpové pásy</a>. Skluz se doplňuje sprejem nebo tekutým voskem přímo na túře. Další výbavu najdete v kategorii <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h3>Závodník</h3>'
          '<p>Závodníci pracují se systémem základních vosků, skluzných vosků podle teploty a vlhkosti a často i s práškem nebo fluorem. Fluorované vosky jsou v závodech FIS zakázané a v EU kvůli látkám PFAS omezené, proto pro rekreační lyžování volte bezfluorové vosky a pro závody ověřte aktuální pravidla organizátora. Strukturování skluznice je samostatná disciplína.</p>'
          '<h2>Časté chyby</h2>'
          '<p>Nejčastěji se maže na špinavou skluznici, takže vosk drží jen na nečistotách. Druhá chyba je přehřátí žehličky: skluznice zešedne, zdeformuje se a ztratí vlastnosti. Třetí chyba spočívá v nedostatečném seškrábání, kdy zbytek vosku vytváří brzdu. '
          'Čtvrtou chybou je volba příliš studeného vosku na vlhký sníh, který pak neklouže. A pátá, zvláště u klasických běžek, je přílišná vrstva stoupacího vosku, která se zachycuje o sníh i při skluzu a běžec nejede dopředu.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii najdete značky {B(("swix", "Swix"), ("star-ski-wax", "Star Ski Wax"), ("holmenkol", "Holmenkol"), ("toko", "Toko"), ("vauhti", "Vauhti"), ("druchema", "Druchema"), ("vola", "Vola"), ("skivo", "Skivo"))}. '
          'Mnoho z nich nabízí celé řady od základního mazání po závodní sady. Při porovnání obchodů si ověřte gramáž balení, teplotní rozsah a zda jde o vosk, nebo o příslušenství, protože se v nabídce prolíná. Pro celkový přehled se vraťte do kategorie <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[('Jak často mazat lyže?', 'Sjezdové lyže před sezónou a poté podle používání, pokud skluznice vypadá šedě a suše. Běžecké lyže častěji, někdy po několika dnech provozu nebo před důležitou jízdou.'),
         ('Jaký vosk zvolit pro začátek?', 'Univerzální skluzný vosk, který pokrývá širší teplotní rozmezí. K němu se hodí plastová škrabka, nylonový kartáč a žehlička s regulací teploty.'),
         ('Čím se liší tuhý vosk od spreje?', 'Tuhý se vpravuje horkou cestou a drží déle. Sprej a tekutý vosk se aplikují rychle a hodí se na doplnění v terénu, ale hlubší voskování nenahradí.'),
         ('Je vosk na lyže a snowboard stejný?', 'Skluzné vosky pro sjezdové lyže a snowboard jsou obvykle zaměnitelné. Běžecké lyže mají vlastní vosky pro skluz i pro záběr, podle stylu jízdy.'),
         ('Mohu mazat obyčejnou domácí žehličkou?', 'Nedoporučuje se. Domácí žehlička nemá stabilní teplotu a má otvory, které vosk zaplní. Lyžařská žehlička má hladkou desku a přesnou regulaci, takže skluznici nepřehřeje.'),
         ('Co je základní vosk?', 'Měkčí vosk, který se nanáší na novou nebo vysušenou skluznici. Prosákne hlouběji a připraví povrch na hlavní skluzný vosk.'),
         ('K čemu slouží stoupací vosk?', 'Používá se ve střední části klasických běžek a dává záběr při odrazu. Rozlišuje se podle teploty a typu sněhu a u mokrého sněhu může být nahrazen klistrem.'),
         ('Proč lyže po voskování nejedou?', 'Nejčastější příčinou je nevhodný vosk pro dané teploty, špinavá skluznice nebo nedostatečně seškrábaný přebytek. Zkuste skluznici očistit, znovu vykartáčovat a případně použít jiný vosk.'),
         ('Jak odstranit starý vosk?', 'Použijte čistič skluznice a utěrku, případně horký měkký vosk, který starý rozpustí, a seškrábněte ho za tepla. Poté skluznici vykartáčujte a naneste čerstvou vrstvu.'),
         ('Jak lyže skladovat přes léto?', 'Naneste silnější vrstvu vosku a nechte ji na skluznici, hrany přetřete olejem. Lyže uložte v suchu a chladu, svázané tak, aby se nepřekřížily a zůstaly rovné.')],
)

# ------------------------------------------------------------------ ploutve
NEW['ploutve'] = dict(long=True,
    title='Plavecké a potápěčské ploutve: výběr a velikost',
    desc='Krátké plavecké, páskové potápěčské, botičkové a šnorchlovací ploutve. Jak zvolit velikost, tuhost a typ podle bazénu, moře i freedivingu.',
    intro='<p>Ploutev prodlužuje nohu a mění úsilí svalů v pohyb vpřed. V bazénu se používá k nácviku techniky a posílení nohou, na moři umožňuje plavat dlouho s malým úsilím a při potápění nahrazuje většinu práce rukou. '
          'Pro každý účel se hodí jiný tvar, délka i tuhost a špatně zvolené ploutve mohou způsobit křeče, otlaky nebo rychlou únavu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u ploutví značek Speedo, Aqualung, Mares, Finis, Arena, Cressi nebo Apeks. K ploutvím patří i <a href="/plavecke-pomucky/">plavecké pomůcky</a>, <a href="/snorchlovani/">šnorchlování</a>, <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/neopreny/">neopreny</a>. Níže najdete rozdíl mezi typy a postup volby velikosti.</p>',
    guide='<h2>Hlavní typy ploutví</h2>'
          + T(['Typ', 'Konstrukce', 'Typické použití'], [
              ['Krátké plavecké', 'celobotička, krátká čepel', 'bazén, nácvik techniky a tempa'],
              ['Dlouhé plavecké', 'delší čepel, často s plovoucím tvarem', 'plavání, rozvoj síly a pocitu pro vodu'],
              ['Botičkové', 'uzavřená bota z měkké pryže', 'šnorchlování z břehu a lodi, v teplé vodě'],
              ['Páskové', 'otevřená pata a nastavitelný pásek', 'potápění v neoprenových botách, cestování'],
              ['Freedivingové', 'dlouhá a úzká čepel', 'apnoe, hlubší potápění na nádech'],
              ['Dětské', 'menší velikosti a měkčí materiál', 'hra a učení plavat']]) +
          '<p>Základní rozdíl je mezi botičkovými a páskovými ploutvemi. Botičková ploutev se obouvá jako střevíc na bosou nohu, je lehčí a pro pláž nebo bazén je nejpohodlnější. Páskovou ploutev nosíte přes potápěčskou botu, hodí se do studené vody a na skalnatá místa, kde je potřeba chodit k vodě po kamenech. '
          'Pásek lze přizpůsobit a při cestování se ploutev snadno vejde do kufru.</p>'
          '<h2>Plavecké ploutve do bazénu</h2>'
          '<p>Krátké plavecké ploutve jsou určeny k tréninku, ne k rychlému přesunu. Kratší čepel zachovává přirozený rytmus nohou a nutí svaly pracovat v jemnějším tempu. Dlouhé ploutve zvyšují rychlost a zatíží svaly víc, takže jsou vhodné spíš pro pokročilé. '
          'Na bazénu se často používají s <a href="/plavecke-pomucky/">plaveckými pomůckami</a>, jako jsou pull-buoy, pádla nebo plavecká deska, a stoupá tím variabilita tréninku. Značky Speedo a Finis mají v nabídce několik modelů, které se liší tuhostí a zahnutím špičky.</p>'
          '<h3>Pro koho jsou krátké ploutve</h3>'
          '<ul><li>Pro plavce, kteří se učí kraul a potřebují udržet tělo ve správné poloze.</li>'
          '<li>Pro triatlonisty, kteří chtějí zlepšit sílu odrazu nohou.</li>'
          '<li>Pro děti, kterým pomáhají naučit se kopat nohama bez velké únavy.</li>'
          '<li>Pro všechny, kdo trénují techniku obratů a odrazů od stěny.</li></ul>'
          '<h2>Potápěčské a šnorchlovací ploutve</h2>'
          '<p>Při šnorchlování stačí lehká, ohebná ploutev, která dává pohyb při nízké námaze. U potápění s přístrojem jde o ploutev, která musí táhnout i s těžším vybavením, takže bývá tužší a delší. Mares, Aqualung, Cressi a Apeks patří mezi značky, které se těmito typy zabývají nejvíc. '
          'Na šnorchlování se hodí kombinace s maskou a šnorchlem, které najdete v kategorii <a href="/snorchlovani/">šnorchlování</a>. Pro delší výlety v chladné vodě je třeba doplnit neopren a boty: <a href="/neopreny/">neopreny</a> tvoří druhou polovinu výbavy.</p>'
          '<h3>Freediving</h3>'
          '<p>Freedivingové ploutve mají dlouhou a úzkou čepel, která využívá pomalý a hluboký kop. Při potápění na nádech jde o úsporu kyslíku, proto se klade důraz na efektivitu. Pro začátečníky je takový typ zbytečně náročný, takže jej volte až po zvládnutí techniky pod dohledem zkušeného instruktora. '
          'Potápění vždy provádějte se zkušeným parťákem a po vhodném výcviku.</p>'
          '<h2>Velikost a tuhost</h2>'
          '<p>Velikost ploutví se řídí velikostí chodidla, ale výrobci uvádějí rozmezí, protože jedna velikost ploutve pokrývá dvě až tři velikosti obuvi. Botička má sedět pevně, ale nesmí tlačit na prsty. Pata nesmí vyskakovat. Pokud ploutev tlačí, hrozí otlaky; pokud je volná, uniká síla kopu. '
          'U páskových ploutví se velikost řídí obuví, kterou na ně navlékáte, proto zkoušejte s botou nebo neoprenovou ponožkou. Tuhost určuje, jak velký odpor čepel klade. Měkká ploutev je šetrná ke kloubům a hodí se pro začátečníky, tuhá přenese víc síly, ale vyžaduje silné svaly.</p>'
          + T(['Tuhost', 'Pro koho', 'Poznámka'], [
              ['Měkká', 'děti, začátečníci, delší šnorchlování', 'šetrná ke kolenům a lýtkům'],
              ['Střední', 'rekreační plavci a potápěči', 'univerzální kompromis'],
              ['Tuhá', 'zkušení plavci, freediving, trénink síly', 'více síly, vyšší riziko křečí']]) +
          '<h2>Materiál a tvar čepele</h2>'
          '<p>Nejčastěji se používá pryž nebo termoplastický polymer. Pryž je pružná a pohodlná, polymer je lehčí a tvarově stabilní. Kompozitní a karbonové čepele jsou výsadou závodních a freedivingových modelů a mají samostatnou cenovou skupinu. '
          'Tvar čepele ovlivňuje chování: větrací kanály a drážky směrují vodu, takže ploutev kope efektivněji a nenapíná nohu tak intenzivně. Otevřené otvory u některých modelů zlepšují odtok vody.</p>'
          '<h2>Jak se starat o ploutve</h2>'
          '<ul><li>Po každém použití je opláchněte sladkou vodou, zejména po moři nebo chlorované vodě.</li>'
          '<li>Sušte je ve stínu, ne na přímém slunci, kde by pryž zkřehla.</li>'
          '<li>Nenechávejte je v autě v létě ani u topení, protože se mohou deformovat.</li>'
          '<li>Skladujte je rovně a bez zatížení čepelí, aby se nezkroutily.</li>'
          '<li>U páskových ploutví zkontrolujte pásek, přezky a pružiny před každou sezónou.</li>'
          '<li>Vyměňte pásek při prvních trhlinách, jinak se vám ploutev může uvolnit ve vodě.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je koupit příliš tuhou ploutev, protože vypadá profesionálně. Následují křeče v lýtkách a rychlá únava. Druhou chybou je nesprávná velikost, kdy volná ploutev vyskakuje z paty a těsná způsobuje puchýře. '
          'Třetí chybou je použití šnorchlovací ploutve pro plavecký trénink, kde se ukáže, že čepel je příliš dlouhá a rytmus nohou se rozbije. Čtvrtou chybou je nákup bez zkoušky, i když lze jednoduše porovnat tabulky velikostí výrobce.</p>'
          '<h2>Výběr podle situace</h2>'
          '<h3>Dovolená u moře</h3>'
          '<p>Lehké botičkové nebo páskové ploutve doplňte maskou a šnorchlem. Pokud chodíte po kamenité pláži, volte pásková varianta s potápěčskou botou. V kategorii <a href="/plazove-doplnky/">plážové doplňky</a> najdete další vybavení k vodě.</p>'
          '<h3>Plavecký trénink</h3>'
          '<p>Krátké bazénové ploutve a doplňky z kategorie <a href="/plavecke-cepice/">plavecké čepice</a> a <a href="/plavecke-bryle/">plavecké brýle</a> dávají tréninku základ. Ploutve nepoužívejte po celou jednotku, ale střídejte je s plaváním bez nich, aby se technika nezkreslila.</p>'
          '<h3>Děti</h3>'
          '<p>Dětské ploutve musí být měkké a dobře sedět. Dítě je vyzkoušejte v mělké vodě pod dohledem. Doplňte je o <a href="/plovaci-vesty/">plovací vesty</a>, pokud se učí plavat, a o <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h3>Potápění a freediving</h3>'
          '<p>Páskové potápěčské ploutve s vyšší tuhostí a delší čepelí pro potápění s přístrojem, dlouhé úzké pro freediving. Před nákupem se poraďte s instruktorem nebo potápěčským klubem a nezapomeňte, že vybavení se po pár sezónách kontroluje a servisuje.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V kategorii najdete značky {B(("speedo", "Speedo"), ("aqualung", "Aqualung"), ("mares", "Mares"), ("finis", "Finis"), ("arena", "Arena"), ("aqua-speed", "Aqua Speed"), ("apeks", "Apeks"), ("cressi", "Cressi"), ("agama", "Agama"), ("mad-wave", "Mad Wave"))}. '
          'Speedo je nejčastější u bazénových modelů, Aqualung, Mares a Apeks u potápěčských. Při porovnání obchodů srovnávejte typ, velikostní rozmezí a barvu, protože se mezi řadami liší jen málo, a zkontrolujte, zda jde o samostatné ploutve, nebo o sadu s maskou. Pro přehled celé sekce se vraťte do <a href="/vodni-sporty/">vodních sportů</a>.</p>',
    faq=[('Jaké ploutve zvolit pro bazén?', 'Krátké plavecké ploutve s botičkou, které zachovávají přirozený rytmus nohou. Dlouhé jsou náročnější a hodí se pro pokročilé plavce, kteří chtějí posílit nohy.'),
         ('Čím se liší botičkové a páskové ploutve?', 'Botičková se obouvá na bosou nohu a je lehčí. Páskovou nasazujete přes potápěčskou botu a pásek upravíte, proto se hodí do studené vody a na kamenité pláže.'),
         ('Jak poznám správnou velikost?', 'Podle tabulky výrobce a zkoušky. Pata nesmí vyskakovat, prsty nesmí tlačit do špičky. U páskových ploutví zkoušejte s botou nebo ponožkou, kterou budete ve vodě nosit.'),
         ('Mám zvolit tuhou, nebo měkkou ploutev?', 'Začátečníci a děti obvykle měkkou, protože šetří klouby a svaly. Tuhá se hodí pro zkušené plavce a freediving, ale zvyšuje riziko křečí a únavy.'),
         ('Hodí se šnorchlovací ploutve na trénink v bazénu?', 'Nehodí. Mají delší čepel a jiné nastavení, takže rozbíjejí přirozený rytmus nohou. Pro bazén vybírejte krátké plavecké modely.'),
         ('Jak o ploutve pečovat?', 'Po použití opláchněte sladkou vodou, sušte ve stínu a skladujte rovně bez zatížení čepele. Nenechávejte je v horkém autě, kde by se pryž mohla zdeformovat.'),
         ('Co jsou freedivingové ploutve?', 'Dlouhé a úzké ploutve, které využívají pomalý hluboký kop a šetří kyslík. Pro začátečníky jsou zbytečně náročné, k potápění na nádech patří řádný výcvik a parťák.'),
         ('Mohou děti používat ploutve?', 'Ano, měkké dětské ploutve v odpovídající velikosti pod dohledem dospělého. Pomáhají s kopem nohama a hravým učením, ale nenahrazují plovací vestu pro neplavce.'),
         ('Z jakých materiálů se ploutve vyrábějí?', 'Nejčastěji z pryže a termoplastických polymerů. Pryž je pružná a pohodlná, polymer lehčí a tvarově stálejší. Závodní modely používají i kompozity.'),
         ('Proč mi ploutve způsobují křeče?', 'Častou příčinou je příliš tuhá ploutev nebo špatná velikost. Zkuste měkčí model, zkraťte dobu použití a před plaváním se protáhněte. Při opakovaných potížích se poraďte s trenérem nebo lékařem.')],
)


# ------------------------------------------------------------------ extra sections (inserted before the brand block)
_MARK = '<h2>Značky v nabídce</h2>'


def _add(slug, html, intro_add=''):
    g = NEW[slug]['guide']
    assert g.count(_MARK) == 1
    NEW[slug]['guide'] = g.replace(_MARK, html + _MARK)
    NEW[slug]['intro'] = NEW[slug]['intro'].replace('</p>', intro_add + '</p>', 1) if intro_add else NEW[slug]['intro']


_add('karimatky-a-matrace',
     '<h2>Hlučnost a komfort ve dvou</h2>'
     '<p>Nafukovací matrace někdy šustí při každém pohybu, což ve společném stanu vadí spolunocležníkovi. Materiály s měkkým povrchem a tlumenými komorami jsou tišší. Spát ve dvou lze na dvou samostatných podložkách nebo na široké dvojité matraci; samostatné podložky mají tu výhodu, že se při otočení druhý člověk nepohupuje.</p>'
     '<h2>Co si vzít k podložce</h2>'
     '<p>Do batohu patří opravná sada, malá pumpička nebo nafukovací vak a případně tenký polštář. Přidejte i pytel na přenášení, který matraci chrání před otěrem a vlhkostí.</p>')

_add('chranice-a-helmy',
     '<h2>Zkouška v praxi</h2>'
     '<p>Před prvním použitím vše vyzkoušejte doma. Nasaďte přilbu, zapněte řemínek a několikrát zavrtěte hlavou. Chrániče obujte a třikrát se předkloňte i dřepněte, abyste zjistili, zda nesjíždějí. Pokud se po pár minutách objeví tlak nebo škrcení, je lepší je vyměnit hned, dokud je lze vrátit.</p>'
     '<p>Hodnotit lze také hmotnost a větrání. Velmi těžká přilba unavuje šíji, málo větraná v létě zbytečně zahřívá hlavu. Dětem pomůže, když si sami vyberou barvu nebo motiv, protože pak ochranu nosí raději.</p>')

_add('lyzarske-vosky',
     '<h2>Strukturování a hrany</h2>'
     '<p>Kromě vosku ovlivňuje rychlost i struktura skluznice, tedy jemné rýhy, které odvádějí vodní film. Hrubší struktura je vhodná pro mokrý sníh, jemná pro mráz. Strukturu vytváří servis na stroji, ale lze ji pozměnit i ručním strukturním kartáčem. Hrany se před mazáním ostří a odjehlí, protože ostré hrany drží stopu a nepoškodí vosk při jízdě.</p>'
     '<h2>Vosk a životní prostředí</h2>'
     '<p>Roztavený vosk a seškrábané třísky sbírejte na papír nebo do nádoby a vyhazujte do směsného odpadu, nikoli do kanalizace. Při práci používejte větrání a vyberte vosky bez zbytečných přísad, pokud nepotřebujete závodní výkon. Zbytek hobliny z lyží je znečištěný, takže se nevyplatí znovu použít.</p>'
     '<h2>Jak číst označení na obalu</h2>'
     '<p>Na tyčince nebo bloku vosku najdete teplotní rozsah snášenlivosti, barevné označení a doporučení pro aplikaci. Údaj o teplotě se vztahuje ke sněhu, ne ke vzduchu, takže ranní mráz se může rychle změnit v mokrý odpolední sníh. Při pochybnostech zvolte vosk, který pokryje oba stavy, nebo použijte dvě vrstvy: tvrdší základ a měkčí povrch.</p>')

_add('ploutve',
     '<h2>Bezpečnost ve vodě</h2>'
     '<p>Ploutve zvyšují rychlost i dosah, ale nenahrazují plaveckou dovednost. Plavte vždy v blízkosti břehu nebo lodi, v případě šnorchlování s plovoucí bójí, a nikdy sami. Dítě s ploutvemi musí mít stálý dozor dospělého. Při prvním použití volte mělkou vodu, aby se pohyb s dlouhou nohou osvojil bez zbytečného rizika.</p>'
     '<h2>Rozcvička a technika kopu</h2>'
     '<p>Před plaváním s ploutvemi se protáhněte lýtka, předkolení a chodidlo. Kop vychází z kyčlí a stehen, nikoli z kolen, a kotník zůstává uvolněný. Příliš prudký kop vyčerpává a zvedá vodu, kterou ploutev nestihne využít. Lepší je pomalejší, delší pohyb s lehce nataženou špičkou.</p>'
     '<h2>Cestování s ploutvemi</h2>'
     '<p>Ploutve se do zavazadla ukládají tak, aby čepele nebyly ohnuté. Páskové modely zabírají méně místa, protože se pata odpojí a čepel se zasune mezi další věci. Botičkové modely se hodí do tašky přes rameno, ale jejich uchování v teple pryž deformuje. Při letecké dopravě se vyplatí zkontrolovat pravidla dopravce pro rozměry příručního zavazadla.</p>'
     '<h2>Ploutve a ostatní plavecké vybavení</h2>'
     '<p>Správný trénink nespoléhá na jednu pomůcku. Ploutve střídejte s deskou a plaveckými pádly, aby se zlepšila souhra těla. V kategorii najdete i ploutve na surf a bodyboard a šnorchlovací sady; ty se vybírají podle jiných pravidel než plavecké. K výbavě patří i <a href="/plavky/">plavky</a>, <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> pro ochranu před sluncem a <a href="/paddleboardy/">paddleboardy</a> pro doplňkovou aktivitu na vodě. Lehké vybavení se vyplatí sbalit do sportovní tašky z kategorie <a href="/sportovni-tasky/">sportovní tašky</a>.</p>',
     intro_add=' Správná volba šetří klouby i peněženku.')

_add('lyzarske-vosky',
     '<h2>Voskování na svahu a na túře</h2>'
     '<p>Když lyže během dne přestanou klouzat, pomůže rychlé doplnění. Sprejový nebo tekutý vosk se nanese na čistou a suchou skluznici, vetře korkem nebo houbičkou a krátce se vykartáčuje. Takový zásah vydrží kratší dobu než horké mazání, ale na dlouhém sjezdu či přejezdu mezi stopami často stačí. Mějte po ruce také malou utěrku na zbytky sněhu.</p>')

_add('ploutve',
     '<h2>Jak vybrat podle chodidla a kotníku</h2>'
     '<p>Široké chodidlo potřebuje širší botičku, aby palec neměl nepříjemný tlak z boku. Vysoký nárt oceníte u modelů s měkkou pryží v oblasti nártu a u pásků s větším rozsahem nastavení. Kdo má citlivé kotníky nebo po úrazu oslabené šlachy, měl by zvolit měkčí a kratší ploutev a postupně přidávat zátěž. Doporučuje se začít krátkými úseky a sledovat, jak lýtka reagují.</p>'
     '<p>Při koupi pro dospívajícího počítejte s tím, že noha dál roste. Páskové ploutve s širším rozsahem velikostí vydrží déle než botičkové, kde je rozdíl o číslo znát hned.</p>')
