"""sporteka.cz — brand page texts wave 233: oakley, ellesse, scott, salewa, roxy, mammut.
General facts only, no prices or counts; assortment taken from the live catalogue (17. 11. 2026).

Sources (checked 17. 11. 2026):
- Oakley: en.wikipedia.org/wiki/Oakley,_Inc. (Jim Jannard 1975, motocross grips, dog Oakley Anne, O-Frame 1980,
  Luxottica 2007, EssilorLuxottica); gearpatrol.com Jannard origin story; oakley.com Line Miner product pages
  (Prizm Snow lenses, L/M fit); oakleyforum.com Line Miner review (sizes).
- Ellesse: en.wikipedia.org/wiki/Ellesse (Leonardo Servadio, Perugia 1959, initials L. S., Jet Pant,
  half-ball logo = tennis ball + ski tips, Pentland Group); highsnobiety.com ellesse story.
- Scott: scott-sports.com/company/history (Ed Scott, Sun Valley 1958, tapered aluminium ski pole,
  European HQ Givisiez 1978); scott-sports.com Ultimate Dryo 10 product page (10 000 mm / 10 000 g, DRYOsphere 2L).
- Salewa: salewa.com/our-history (8. 7. 1935 Munich, Josef Liebhart, saddlery + leather goods, Oberalp 1990,
  Bolzano); oberalp.com press kit (SAttler LEder WAren); salewa.com Mountain Trainer 2 Mid GTX page
  (3F System, Vibram sole); Pedroc PTX listings (Powertex membrane).
- Roxy: en.wikipedia.org/wiki/Quiksilver (Roxy 1990, heart from two mirrored Quiksilver logos);
  retailgazette.co.uk 2023 (Authentic Brands Group acquires Boardriders).
- Mammut: mammut.com/heritage, mammut.prezly.com 160 years (Kaspar Tanner, Dintikon 1862, ropes,
  HQ Seon, Barryvox 1969); en.wikipedia.org/wiki/Mammut_Sports_Group.
- Norms (EN 958 via ferrata sets, EN 12492 climbing helmets, EN 12277 harnesses, EN 892 dynamic ropes,
  EN 1077 ski helmets, EN 1078 bike helmets, EN ISO 18527-1 goggles, EN ISO 12312-1 sunglasses): CEN catalogue.
Left out (not verified): Salewa tubular ice screw claim, Mammut current owner after Telemos (Jacobs Capital),
Scott ownership (Youngone stake), athletes who wore Ellesse, Roxy 1991–1992 pause."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ oakley
NEW['oakley'] = dict(
    title='Oakley: sluneční a lyžařské brýle, helmy a oblečení',
    desc='Oakley v katalogu: sluneční brýle Sutro a Radar, lyžařské brýle Line Miner a Flight Deck, helmy MOD a ARO, mikiny a trička. Jak vybrat velikost a skla.',
    intro='<p>Oakley je americká značka, kterou zná většina lidí podle sportovních slunečních brýlí. V katalogu sporteka.cz tvoří brýle zdaleka největší část nabídky: cyklistické a běžecké štíty Sutro, Radar EV nebo Sphaera, městské modely Holbrook a lyžařské brýle Line Miner, Flight Deck, Fall Line či Target Line. '
          'Druhou skupinou jsou přilby, ať už lyžařské řady MOD, nebo cyklistické ARO. Doplňuje je oblečení s logem: mikiny, trička, kraťasy, lyžařské bundy a kalhoty, čepice, rukavice a batohy. '
          'Sporteka sama nic neprodává. Sbírá nabídky českých e-shopů a ukazuje je vedle sebe, takže snadno uvidíte, kde je konkrétní model, barva skla a velikost obrouček k mání. '
          'V průvodci níže vysvětlujeme, co znamenají označení Prizm, M a L, jak vybrat filtr na sníh i na kolo a jak se o skla starat. Brýle Oakley nenosí jen sportovci, proto v nabídce nechybí ani klasičtější tvary do auta a na procházky.</p>',
    guide='<h2>Odkud Oakley pochází</h2>'
          '<p>Firmu založil v roce 1975 v Kalifornii Jim Jannard. Začínal s velmi malým kapitálem a prodával gripy na řídítka motokrosových motorek z kufru auta. Jméno značky si vypůjčil od svého psa, anglického setra jménem Oakley Anne. V roce 1980 přišly první brýle, motokrosové O-Frame, a teprve potom sluneční brýle pro cyklisty a běžce, které značku proslavily. '
          'V roce 2007 Jannard Oakley prodal italské skupině Luxottica. Dnes je značka součástí koncernu EssilorLuxottica, pod který patří i Ray-Ban.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Nejpočetnější jsou <a href="/sportovni-bryle/">sportovní a sluneční brýle</a>, za nimi následují <a href="/lyzarske-bryle/">lyžařské brýle</a>. Pozor na to, že některé obchody řadí i lyžařské modely mezi sluneční brýle, proto stojí za to projít obě kategorie. Třetí velkou skupinou jsou <a href="/lyzarske-helmy/">lyžařské helmy</a> MOD1, MOD5 nebo MOD BC. Pro jezdce na kole jsou v nabídce <a href="/cyklisticke-helmy/">cyklistické helmy</a> ARO3 a ARO5, menší výběr najdete také mezi <a href="/mtb-a-integralni-helmy/">helmami na MTB</a>. '
          'Oblečení zastupují <a href="/mikiny/">mikiny</a> B1B nebo Ellipse, <a href="/sportovni-tricka/">trička</a> s potiskem, kraťasy, <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>, <a href="/cepice-a-celenky/">čepice a kšiltovky</a> a <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>. Z batohů je nejčastější městský Kitchen Sink nebo Holbrook.</p>'
          + T(['Řada', 'Typ', 'Na co se hodí'], [
              ['Sutro, Sutro Lite', 'velký jednodílný štít', 'silniční kolo, gravel, běh'],
              ['Radar EV Path', 'štít s vyšším horním okrajem', 'cyklistika v předklonu, běh'],
              ['Sphaera, Encoder', 'sportovní obroučky s panoramatickým sklem', 'kolo, běh, outdoor'],
              ['Holbrook', 'klasický tvar s plnou obroučkou', 'město, auto, volný čas'],
              ['Line Miner, Flight Deck', 'lyžařské brýle s velkým zorným polem', 'sjezd a snowboard'],
              ['Fall Line, Target Line, Flight Tracker', 'lyžařské brýle v různých tvarech', 'sjezd, skialpy, menší verze na užší obličej'],
              ['MOD1, MOD5', 'lyžařské helmy, některé s MIPS', 'sjezd, freeride, park'],
              ['ARO3, ARO5', 'cyklistické helmy', 'silnice, gravel']]) +
          '<h2>Co znamená Prizm</h2>'
          '<p>Prizm je označení skel, která výrobce ladí tak, aby zvýraznila barvy a kontrast v konkrétním prostředí. Proto existují varianty Prizm Road pro silnici, Prizm Trail pro les, Prizm Snow pro sníh a řada dalších. Nejde o jeden typ skla, ale o celou rodinu s různou propustností světla. '
          'U lyžařských brýlí výrobce uvádí propustnost v procentech: tmavé sklo Prizm Snow Black Iridium propouští jen asi šest procent světla a hodí se na ostré slunce, světlejší varianty jsou určené do střídavé oblačnosti. Na mlhu a večerní lyžování je vhodné sklo s vysokou propustností.</p>'
          '<h2>Filtrační kategorie skel</h2>'
          '<p>Sluneční brýle se v Evropě hodnotí podle normy EN ISO 12312-1 a dělí se do kategorií 0 až 4. Na běžné letní slunce stačí kategorie 2 nebo 3. Kategorie 4 propouští velmi málo světla a podle normy se nesmí používat při řízení auta. U lyžařských brýlí platí obdobná stupnice S0 až S4 podle normy EN ISO 18527-1. '
          'Kategorii najdete na nožičce, v popisu nabídky nebo v technickém listu. Pokud obchod uvádí jen název skla, dohledejte si propustnost na stránce výrobce, protože u dvou podobně pojmenovaných skel se může výrazně lišit.</p>'
          '<h2>Velikosti M, L a S</h2>'
          '<p>Lyžařské brýle Oakley se prodávají ve velikostech, které se píšou přímo do názvu, například Line Miner M a Line Miner L. Verze L má větší rám i zorník a hodí se na větší obličej a širší helmu, verze M sedí lépe na užší tvář. Podobně jsou rozlišené i sluneční modely, třeba Sutro a Sutro S nebo Flight Deck M a L. '
          'Rozměry slunečních obrouček se často uvádějí jako trojice čísel, například 59/18. První číslo je šířka jednoho skla v milimetrech, druhé šířka můstku. Pokud už máte brýle, které vám sedí, porovnejte tyto údaje.</p>'
          '<ol><li>Lyžařské brýle zkuste ideálně s vlastní helmou. Mezi horním okrajem rámu a helmou by neměla zůstat mezera.</li>'
          '<li>Rám nesmí tlačit na kořen nosu, jinak se při jízdě zhorší dýchání a brýle se rychleji mlží.</li>'
          '<li>Sluneční brýle na kolo by se neměly při pohybu hlavy posouvat. Nožičky mají přiléhat, ale netlačit za ušima.</li>'
          '<li>U helmy změřte obvod hlavy krejčovským metrem nad obočím a porovnejte jej s rozsahem velikosti.</li></ol>'
          '<h2>Helmy na lyže a na kolo</h2>'
          '<p>Lyžařské helmy MOD musí splňovat normu EN 1077, cyklistické helmy ARO normu EN 1078. U některých modelů najdete v názvu zkratku MIPS. Jde o vložku, která se při šikmém nárazu může vůči skořepině lehce posunout, a tím snížit rotační síly působící na hlavu. Helmu po vážném pádu vyměňte, i když na ní není vidět prasklina. '
          'Ke značkové helmě se obvykle dobře hodí brýle stejné značky, ale není to podmínka. Rozhodující je, zda horní okraj brýlí navazuje na helmu a nezakrývá větrací otvory nad čelem. Výběr dalších modelů najdete v přehledu <a href="/lyzarske-bryle-oakley/">lyžařské brýle Oakley</a> a <a href="/oakley-slunecni-bryle/">sluneční brýle Oakley</a>.</p>'
          '<h2>Brýle na kolo a běh</h2>'
          '<p>Na silnici se osvědčily velké štíty jako Sutro nebo Radar EV Path. Kryjí větší část zorného pole a chrání oči před větrem, hmyzem i odletujícími kamínky. Radar EV Path má vyšší horní okraj, takže při jízdě v hlubokém předklonu nepřekáží ve výhledu. Na běh se hodí lehčí modely, které na obličeji neposkakují, třeba Sutro Lite nebo Encoder. '
          'Kdo jezdí lesem, kde se rychle střídá stín a slunce, ocení světlejší sklo Prizm Trail. Na noční a zimní jízdy je lepší čiré nebo velmi světlé sklo. Pokud nosíte dioptrické brýle, řešte dioptrickou úpravu u optika, protože běžné nabídky v e-shopech ji neobsahují.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Oblečení Oakley vychází ze snowboardové a surfové kultury, proto převažují volnější střihy, mikiny s velkým logem a trička s potiskem. Lyžařské bundy a kalhoty mají membránu a v popisu bývá uveden vodní sloupec i prodyšnost, podle kterých se dají porovnat s jinými značkami. '
          'V nabídce jsou i taktické rukavice řady Factory Lite, které se používají při střelbě, práci s lanem nebo na airsoft. Pod bundu se hodí <a href="/termopradlo/">termoprádlo</a>, na krk <a href="/nakrcniky-a-satky/">nákrčník</a>.</p>'
          '<h2>Péče o skla a obroučky</h2>'
          '<ul><li>Skla čistěte mikrovláknovým sáčkem, který bývá součástí balení. Papírové kapesníky a tričko sklo poškrábou.</li>'
          '<li>Vnitřní stranu lyžařského zorníku neotírejte, když je mokrá. Je na ní vrstva proti mlžení, kterou snadno setřete. Nechte ji volně uschnout.</li>'
          '<li>Brýle neodkládejte skly dolů a nenechávejte je za horka na palubní desce auta.</li>'
          '<li>Na sjezdovce brýle nenoste nasazené na čele pod čepicí. Teplo a vlhkost z hlavy je zamlží.</li></ul>'
          '<p>Poškrábaný zorník se dá u řady modelů vyměnit, náhradní skla najdete v kategorii <a href="/nahradni-zorniky/">náhradní zorníky</a>. Při objednání vždy ověřte, že sklo je určené přesně pro váš model a velikost, protože zorníky Line Miner M a L nejsou zaměnitelné.</p>'
          '<h2>Jak srovnat nabídky obchodů</h2>'
          '<p>U brýlí Oakley se jeden model prodává v mnoha kombinacích barvy rámu a skla. Při porovnání proto nesledujte jen název modelu, ale celé označení skla, třeba Prizm Road, Prizm Snow Sapphire nebo Prizm Black Polarized. Polarizace pomáhá u vody a mokré silnice, na sníh se ale každému nehodí, protože může ztížit čtení zledovatělých míst. '
          'Dále ověřte, zda balení obsahuje pouzdro nebo druhé sklo, jestli jde o aktuální verzi modelu a jakou velikost obchod skutečně posílá. Některé e-shopy uvádějí kód modelu ve tvaru OO 9208 nebo OO7070, podle kterého se dá stejný kus dohledat v jiném obchodě.</p>',
    faq=[
        ('Odkud se vzalo jméno Oakley?',
         'Zakladatel Jim Jannard pojmenoval firmu po svém psovi, anglickém setrovi jménem Oakley Anne.'),
        ('Komu dnes značka Oakley patří?',
         'Od roku 2007 patří italské skupině Luxottica, která je dnes součástí koncernu EssilorLuxottica.'),
        ('Co znamená Prizm u brýlí Oakley?',
         'Prizm je rodina skel laděných pro konkrétní prostředí, například silnici, les nebo sníh. Zvýrazňuje barvy a kontrast, propustnost se mezi variantami liší.'),
        ('Jaký je rozdíl mezi Line Miner M a L?',
         'Verze L má větší rám i zorník a hodí se na větší obličej a širší helmy. Verze M sedí lépe na užší tvář.'),
        ('Jakou filtrační kategorii vybrat na lyže?',
         'Na slunečné dny kategorii S3, do zatažena a mlhy S1 nebo S2. Kdo jezdí za každého počasí, může zvolit model s výměnným sklem. Kategorie S4 je určená do extrémního slunce na ledovcích.'),
        ('Můžu brýle kategorie 4 nosit za volantem?',
         'Ne. Norma EN ISO 12312-1 brýle kategorie 4 pro řízení vylučuje, protože propouštějí příliš málo světla.'),
        ('Co znamená MIPS u helmy Oakley?',
         'Je to vložka, která se při šikmém nárazu může vůči skořepině lehce posunout. Tím má snížit rotační síly působící na hlavu. Velikost helmy vybírejte podle obvodu hlavy, MIPS na ní nic nemění.'),
        ('Dá se koupit náhradní zorník?',
         'U mnoha lyžařských modelů ano. Hledejte sklo určené přesně pro váš model a velikost, zorníky různých velikostí nejsou zaměnitelné.'),
        ('Jak čistit zamlžené lyžařské brýle?',
         'Vnitřní stranu neotírejte za mokra, abyste nesetřeli vrstvu proti mlžení. Brýle nechte uschnout a pak je jemně očistěte mikrovláknem.'),
        ('Prodává sporteka.cz brýle Oakley přímo?',
         'Ne. Sporteka srovnává nabídky českých e-shopů. Nákup, záruku i případnou reklamaci řešíte s obchodem, u kterého objednáte.'),
    ],
)

# ------------------------------------------------------------------ ellesse
NEW['ellesse'] = dict(
    title='Ellesse: tenisky, mikiny, trička a tepláky',
    desc='Ellesse v katalogu: tenisky, trička s půlkulatým logem, mikiny, tepláky, kraťasy, plavky a ledvinky. Jak padnou velikosti a jak srovnat nabídky.',
    intro='<p>Ellesse je italská značka s oranžovo-červeným logem ve tvaru půlky míčku. Začínala lyžařskými kalhotami, proslavila se tenisovým oblečením a dnes ji lidé kupují hlavně jako sportovní módu na každý den. '
          'V katalogu sporteka.cz jsou nejpočetnější tenisky, ať už bílé kožené modely, semišové kousky, nebo boty s masivnější podrážkou. Dále najdete trička, mikiny s kapucí i bez ní, tepláky, kraťasy, polokošile, plavky, zimní bundy, čepice, ponožky a ledvinky přes rameno. '
          'Sporteka nabídky jednotlivých obchodů jen shromažďuje a řadí vedle sebe, takže hned vidíte, kde je vaše velikost a barva skladem. Objednávka pak proběhne v e-shopu, který si vyberete. '
          'Níže najdete stručnou historii značky, přehled toho, co v nabídce převažuje, rady k velikostem a péči a tipy, jak se v nabídkách vyznat. Většina kousků je určená na volný čas, do školy a do města. Pro sport je výběr menší, ale najdete i několik funkčních triček, legín a sportovních podprsenek.</p>',
    guide='<h2>Krátká historie Ellesse</h2>'
          '<p>Značku založil v roce 1959 v italské Perugii krejčí Leonardo Servadio. Název vznikl z jeho iniciál, tedy L a S, vyslovených po italsku. Prvními výrobky byly lyžařské kalhoty, mezi nimi model Jet Pant s vyztuženými koleny a širší nohavicí, která šla přetáhnout přes lyžařskou botu. '
          'V sedmdesátých letech se Ellesse přesunula do tenisu a v té době vzniklo i dnešní logo. Půlkulatý tvar připomíná polovinu tenisového míčku a zároveň dvě špičky lyží. Dnes značka patří britské skupině Pentland, pod kterou spadají také Speedo nebo Berghaus.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Zdaleka nejvíc je <a href="/tenisky/">tenisek</a>. Druhou velkou skupinou jsou <a href="/sportovni-tricka/">trička</a>, většinou bavlněná s výrazným logem na hrudi, a <a href="/mikiny/">mikiny</a> v přetahovací i propínací verzi. Na ně navazují <a href="/teplaky/">tepláky</a>, <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/polokosile/">polokošile</a>. '
          'Menší podíl mají <a href="/plavky/">plavky</a>, <a href="/zimni-bundy/">zimní bundy</a>, <a href="/cepice-a-celenky/">čepice</a>, <a href="/sportovni-ponozky/">ponožky</a> a <a href="/tasky-pres-rameno/">ledvinky a tašky přes rameno</a>, například model Rosca. Dětské oblečení se v katalogu objevuje jen výjimečně.</p>'
          + T(['Skupina', 'Typické modely', 'Poznámka'], [
              ['Tenisky', 'Jerry, Cody Suede, Onyx, Panaro Cupsole, New Mitchell, Queen', 'kůže, semiš i syntetika'],
              ['Mikiny', 'Pershuta, Gottero, Jazana, Illkestone', 'pánské i dámské, s kapucí i bez'],
              ['Trička', 'Silinto, Reino, Beckana a další', 'bavlna, logo na hrudi'],
              ['Tepláky a kraťasy', 'Cravo, Majana, Molla, Tour', 'volnočasové střihy'],
              ['Plavky a doplňky', 'jednodílné plavky, ledvinky, ponožky', 'menší výběr']]) +
          '<h2>Tenisky: jak se vyznat v modelech</h2>'
          '<p>Většina tenisek Ellesse je určená do města, ne na sportování. Často se objevuje označení cupsole. Jde o konstrukci, kdy je svršek vsazený do podrážky ve tvaru vaničky a po obvodu prošitý nebo přilepený. Taková bota je pevná a dobře drží tvar, ale bývá těžší a tužší než běžecká obuv. '
          'Kožené bílé modely působí čistě a dají se kombinovat s riflemi i teplákovou soupravou. Semišové verze, například Cody Suede, jsou měkčí, ale citlivější na vodu a sůl. Pokud hledáte botu na tenisový kurt, potřebujete spíš specializovanou <a href="/tenisova-obuv/">tenisovou obuv</a> s podrážkou pro daný povrch.</p>'
          '<h2>Velikosti obuvi</h2>'
          '<p>V nabídkách se střídají evropská a britská čísla a některé obchody uvádějí i délku stélky. Nejspolehlivější je změřit vlastní chodidlo. Postavte se na papír, obkreslete patu a nejdelší prst, změřte vzdálenost a přidejte asi půl až jeden centimetr na pohyb prstů. '
          'Tenisky s pevnou podrážkou cupsole se během nošení moc nepovolí. Pokud jste mezi dvěma čísly, vezměte raději větší a dorovnejte ho silnější ponožkou. U semišových bot počítejte s tím, že se svršek trochu přizpůsobí noze, ale délka zůstane stejná.</p>'
          '<h2>Oblečení: střih a materiál</h2>'
          '<p>Trička a mikiny Ellesse se prodávají v pánských i dámských střizích. Dámská trička bývají kratší a užší, některé modely jsou přiznaně cropped, tedy zkrácené nad pas. Pánské mikiny mají rovný střih a pružný lem v pase. Pokud chcete volnější styl, je bezpečnější zvolit o číslo větší velikost než hledat oversize střih podle fotek. '
          'Materiálem je obvykle bavlna nebo směs bavlny s polyesterem, uvnitř mikin často počesaná. Pro sport je lepší funkční tričko z polyesteru, které rychle schne. V katalogu je funkčních kousků od Ellesse jen málo, takže na běh nebo do posilovny se podívejte i do kategorie <a href="/funkcni-tricka/">funkční trička</a>.</p>'
          '<h2>Tepláky, soupravy a kraťasy</h2>'
          '<p>Tepláky jsou většinou bavlněné, s pružným pasem a zúženou nohavicí s manžetou. Některé modely mají rovnou nohavici bez manžety, což je v popisu uvedeno jako straight nebo open hem. Kdo chce mít vrchní díl a kalhoty ve stejné barvě, najde ucelené kombinace v přehledu <a href="/teplakove-soupravy/">teplákové soupravy</a>. '
          'Kraťasy se dělí na bavlněné na volný čas a lehké šortky z polyesteru, které se hodí i k vodě. U dámských elastických šortek sledujte délku nohavice, protože se mezi modely výrazně liší.</p>'
          '<h2>Mikiny s kapucí, nebo bez</h2>'
          '<p>Mikina s kapucí je praktičtější na podzim a do větru, ale pod bundou s vlastní kapucí může překážet. Přetahovací mikina bez kapuce, tedy klasický crewneck, se snadno nosí pod kabát i přes košili. Propínací modely na zip se rychle svléknou, když se oteplí, a dají se sladit s tepláky do kompletu. '
          'Ellesse u mikin často používá výrazné logo přes celou hruď, jindy jen menší výšivku. Pokud chcete mikinu nosit i do práce, zvolte spíš decentnější variantu v tmavé barvě. Konkrétní typy najdete v kategoriích <a href="/mikiny-s-kapuci/">mikiny s kapucí</a> a <a href="/mikiny-na-zip/">mikiny na zip</a>.</p>'
          '<h2>Plavky, bundy a doplňky</h2>'
          '<p>Plavky Ellesse jsou hlavně dámské jednodílné a pánské koupací šortky. Hodí se k bazénu a k moři, na tréninkové plavání jsou vhodnější specializované značky s materiálem odolným proti chlóru. Zimní bundy jsou spíš městské, prošívané nebo s kapucí, a na hory ani na lyže určené nejsou. '
          'Ledvinky a malé tašky přes rameno se hodí na doklady, klíče a telefon při cestování nebo na koncert. Ponožky se prodávají obvykle v balení po více párech, takže při srovnání sledujte, kolik párů balení obsahuje.</p>'
          '<h2>Barvy a kombinování</h2>'
          '<p>Typická paleta značky stojí na bílé, černé, tmavě modré a oranžovočervené barvě loga. Bílé tenisky se tak snadno sladí s tričkem nebo mikinou stejné značky. Na světlých kouscích je rychleji vidět špína, proto je perte odděleně od tmavých. V nabídce jsou i béžové a zelené odstíny, které jsou na nošení ve městě méně choulostivé.</p>'
          '<h2>Sportovní kousky</h2>'
          '<p>Funkčních věcí je v nabídce Ellesse málo, ale pár jich najdete: sportovní podprsenky, legíny, funkční trička a sportovní sukně a šaty. Hodí se na lehký trénink, jógu nebo rekreační tenis. U sportovní podprsenky sledujte míru opory, kterou výrobci označují jako nízkou, střední nebo vysokou; na běh potřebujete vysokou. '
          'Legíny zkontrolujte v předklonu proti světlu, zda nejsou průsvitné. Na pravidelný běh nebo posilovnu se vyplatí projít i specializované kategorie <a href="/sportovni-podprsenky/">sportovní podprsenky</a> a <a href="/leginy/">legíny</a>, kde je výběr mnohem širší.</p>'
          '<h2>Péče o tenisky a oblečení</h2>'
          '<ul><li>Kožené tenisky čistěte vlhkým hadříkem a jemným mýdlem. Do pračky je nedávejte, kůže by mohla popraskat a lepení podrážky povolit.</li>'
          '<li>Semiš chraňte impregnací ještě před prvním nošením. Zaschlé bláto vykartáčujte kartáčkem na semiš.</li>'
          '<li>Trička a mikiny s potiskem perte naruby na nižší teplotu. Potisk pak vydrží déle a nepraská.</li>'
          '<li>Bavlněné mikiny nesušte v sušičce na vysokou teplotu, mohly by se srazit.</li></ul>'
          '<h2>Pro koho se Ellesse hodí</h2>'
          '<p>Ellesse je volba pro ty, kdo chtějí sportovní vzhled na každý den a líbí se jim retro styl inspirovaný tenisem osmdesátých let. Sedne do školy, do města i na víkend. Pro výkonnostní sport je výběr omezený. '
          'Pokud porovnáváte podobné značky, podívejte se také na '
          + B(('fila', 'Fila'), ('kappa', 'Kappa'), ('lotto', 'Lotto')) +
          ', které mají kořeny ve stejné éře sportovní módy.</p>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>U tenisek Ellesse se název modelu v e-shopech často zkracuje nebo nahrazuje číslem, třeba 116 Jerry nebo 388 Cody Suede. Hledejte proto podle názvu i podle fotek podrážky a svršku. U oblečení ověřte, zda jde o pánský, dámský nebo unisex střih, protože obchody to ne vždy píšou do názvu. '
          'Dále sledujte materiál, dostupnost konkrétní velikosti a podmínky vrácení. Při nákupu bot je dobré vybrat obchod, který umožní výměnu velikosti bez komplikací.</p>',
    faq=[
        ('Co znamená název Ellesse?',
         'Vznikl z iniciál zakladatele Leonarda Servadia, tedy z písmen L a S vyslovených po italsku.'),
        ('Co představuje logo Ellesse?',
         'Půlkulatý tvar odkazuje na polovinu tenisového míčku a zároveň na dvě špičky lyží. Spojuje tak oba sporty, se kterými je historie značky spjatá.'),
        ('Je Ellesse italská značka?',
         'Založena byla v italské Perugii v roce 1959. Dnes patří britské skupině Pentland.'),
        ('Jak padnou tenisky Ellesse?',
         'Záleží na modelu. Boty s pevnou podrážkou cupsole se moc nepovolí, proto při váhání mezi čísly volte raději větší. Nejjistější je porovnat délku stélky v centimetrech s délkou vlastního chodidla.'),
        ('Co znamená cupsole?',
         'Je to podrážka ve tvaru vaničky, do které je vsazený a prošitý svršek. Bota je pevná a dobře drží tvar.'),
        ('Hodí se tenisky Ellesse na tenis?',
         'Většina modelů je určená do města. Na kurt je lepší specializovaná tenisová obuv s podrážkou pro daný povrch, například antuku nebo tvrdý povrch, a se zpevněnou boční částí.'),
        ('Jsou dámská trička Ellesse kratší?',
         'Často ano. Některé modely jsou zkrácené nad pas, proto si v popisu ověřte délku a střih. Kdo chce delší tričko, může zvolit pánský nebo unisex model v menší velikosti.'),
        ('Jak prát mikiny s potiskem?',
         'Naruby, na nižší teplotu a bez vysoké teploty v sušičce. Potisk pak vydrží déle a mikina se nesrazí.'),
        ('Prodává Ellesse i dětské oblečení?',
         'V katalogu se dětské kousky objevují jen výjimečně. Většina nabídky je pro dospělé. Menším dospívajícím mohou padnout nejmenší dámské velikosti.'),
        ('Kde koupit Ellesse přes sporteka.cz?',
         'Sporteka ukáže nabídky různých e-shopů vedle sebe. Objednávku dokončíte přímo v obchodě, který si vyberete. Dopravu, platbu i vrácení zboží řešíte s ním.'),
    ],
)

# ------------------------------------------------------------------ scott
NEW['scott'] = dict(
    title='Scott: běžecké boty, lyžařské bundy, brýle a cyklo',
    desc='Scott v katalogu: běžecké boty Kinabalu a Pursuit, lyžařské bundy Ultimate a Vertic, brýle, helmy a oblečení na kolo. Jak vybrat velikost.',
    intro='<p>Scott je značka, která začínala lyžařskými holemi a dnes vyrábí vybavení na kolo, lyže i běh. V katalogu sporteka.cz má široký záběr. Nejpočetnější jsou běžecké boty, na silnici řada Pursuit a do terénu Kinabalu nebo Supertrac. '
          'Silně jsou zastoupené také přechodové a lyžařské bundy, lyžařské kalhoty, kraťasy, trička, mikiny a funkční trička. K zimnímu vybavení patří lyžařské brýle, helmy a rukavice, k cyklistice dresy, kraťasy s vložkou, tretry a pedály. Jízdní kola Scott se v katalogu objevují jen ojediněle. '
          'Sporteka nabídky obchodů porovnává, sama nic neprodává, takže vidíte, kdo má danou velikost skladem. '
          'V průvodci najdete stručnou historii, vysvětlení názvů řad a rady, jak vybrat velikost bot, bund a brýlí. Značku ocení hlavně lidé, kteří sportují celý rok: v létě běhají nebo jezdí na kole a v zimě lyžují či chodí na skialpy. Výhodou je, že brýle, helmu i oblečení lze sladit od jednoho výrobce.</p>',
    guide='<h2>Historie značky Scott</h2>'
          '<p>Zakladatel Ed Scott byl inženýr a lyžařský závodník ze Sun Valley v americkém Idahu. V roce 1958 přišel s kuželovitou hliníkovou lyžařskou holí, která nahradila hole z bambusu a oceli. Na ní vyrostla firma, která postupně přidala lyžařské brýle, motokrosové vybavení a později jízdní kola. '
          'V roce 1978 otevřela evropské sídlo v Givisiez nedaleko švýcarského Fribourgu, kde má centrálu dodnes. Z původního Scott USA se v roce 2005 stal Scott Sports.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Největší skupinou jsou <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> a <a href="/trailove-boty/">trailové boty</a>. Hned za nimi jsou <a href="/sportovni-kratasy/">kraťasy</a>, přechodové bundy a trička. Na zimu jsou v nabídce <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a> a kombinézy, k nim <a href="/lyzarske-bryle/">lyžařské brýle</a> Faze II nebo Shield a <a href="/lyzarske-helmy/">lyžařské helmy</a>. '
          'Cyklisté najdou <a href="/cyklisticke-dresy/">dresy</a>, <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy na kolo</a> s vložkou, <a href="/cyklisticka-obuv/">tretry</a> se zapínáním Boa a pedály SPD. Kola jsou zastoupená jen jednotlivými modely, například celoodpružený Spark nebo horské elektrokolo Aspect eRide.</p>'
          + T(['Řada', 'Co to je', 'Použití'], [
              ['Kinabalu, Supertrac', 'trailové boty s hrubším vzorkem', 'lesní cesty, hory, mokro'],
              ['Pursuit', 'silniční boty s výraznějším tlumením', 'asfalt, delší tréninky'],
              ['RC Run', 'lehké oblečení na běh', 'trénink a závody'],
              ['Ultimate Dryo, Ultimate GTX', 'zateplené lyžařské bundy a kalhoty', 'sjezdovka'],
              ['Vertic, Line Chaser', 'freeride a skialpové oblečení', 'terén mimo upravené tratě'],
              ['Explorair 3L', 'třívrstvá nepromokavá bunda', 'hory, déšť, skialpy'],
              ['Insuloft', 'bundy se syntetickým zateplením', 'chladné dny, vrstva pod hardshell'],
              ['Endurance, Trail Vertic', 'cyklistické kraťasy a dresy', 'silnice, MTB']]) +
          '<h2>Běžecké boty: silnice a trail</h2>'
          '<p>Pursuit je silniční bota s měkčím tlumením, určená na asfalt a delší klidné tréninky. Kinabalu a Supertrac mají hrubší vzorek podrážky, který drží na blátě, kořenech a kamení. Supertrac má výraznější zuby a je spíš na měkký a mokrý terén, Kinabalu je univerzálnější. Některé modely mají membránu Gore-Tex, poznáte je podle zkratky GTX. '
          'Membrána udrží vodu venku, ale bota v ní hůř větrá a po namočení přes kotník schne déle. Na letní běh je proto lepší verze bez membrány. Více o rozdílech píšeme v kategorii <a href="/bezecka-obuv/">běžecká obuv</a>.</p>'
          '<h2>Velikost běžeckých bot</h2>'
          '<p>Běžecká bota by měla mít před palcem rezervu zhruba šířku palce, protože noha se při běhu prodlužuje a v kopci dopředu posouvá. Boty zkoušejte odpoledne, kdy je chodidlo mírně oteklé, a s ponožkami, ve kterých běháte. U trailových modelů dbejte na pevné držení paty, aby noha v klesání nejela dopředu.</p>'
          '<h2>Lyžařské bundy a kalhoty</h2>'
          '<p>Lyžařské oblečení Scott se dělí podle stylu. Řada Ultimate je určená na sjezdovku, má zateplení a sněhový pás. U modelu Ultimate Dryo 10 výrobce uvádí vodní sloupec 10 000 mm a prodyšnost 10 000 g na metr čtvereční za den, což na běžný sjezdový den stačí. Ultimate GTX používá membránu Gore-Tex. '
          'Řada Vertic a skialpové kalhoty Line Chaser jsou střižené volněji a mají větrací zipy, protože při výstupu se člověk zapotí. Třívrstvá Explorair 3L nemá zateplení a obléká se přes vrstvy. Kdo chodí na <a href="/skialpinismus/">skialpy</a>, ocení právě tuto kombinaci. Pod zateplenou bundu se hodí <a href="/funkcni-tricka/">funkční triko</a>, pod hardshell <a href="/fleecove-mikiny/">fleece</a> nebo bunda Insuloft.</p>'
          '<h2>Brýle a helmy</h2>'
          '<p>Lyžařské brýle Scott, například Faze II, se prodávají s různými skly. Sledujte filtrační kategorii S0 až S4: na slunce S3, do mlhy S1 nebo S2. Helmy jako Element MIPS musí splňovat normu EN 1077 a vložka MIPS má při šikmém nárazu snížit rotační síly. Brýle vždy zkuste s helmou, aby na sebe navazovaly. Na kolo a běh jsou v nabídce i sluneční brýle Stride.</p>'
          '<h2>Cyklistické oblečení</h2>'
          '<p>Kraťasy na kolo se dělí na přiléhavé silniční s vložkou a volné MTB kraťasy, pod které se nosí vnitřní kalhotky s vložkou. Řada Endurance je spíš na silnici a delší vyjížďky, Trail Vertic a Trail Flow na horské kolo. Vložku vybírejte podle délky jízd: na hodinu stačí tenká, na celodenní túru je lepší hustší a tvarovaná. '
          'Tretry se zapínáním Boa se utahují kolečkem, které jde dotáhnout i za jízdy. Pro zapnutí do pedálu potřebují kompatibilní kufry; silniční tretry mají tři šrouby, MTB dva. Pedály najdete v kategorii <a href="/cyklo-pedaly/">pedály</a>. Na delší běh nebo trail ve vedru přijde vhod <a href="/bezecke-vesty-a-batohy/">běžecká vesta</a> s místem na lahve.</p>'
          '<h2>Oblečení na běh</h2>'
          '<p>Běžecká řada RC Run zahrnuje trička, kraťasy, legíny a lehké bundy. Bunda RC Run WB je tenká vrstva proti větru, kterou lze sbalit do malé kapsy nebo do vesty. Běžecké kraťasy mají obvykle vnitřní slipy a malou kapsu na klíče, u konkrétního modelu to ověřte v popisu. '
          'Na chladné dny jsou v nabídce <a href="/leginy/">legíny</a> a funkční trička s dlouhým rukávem. U běžeckého oblečení sledujte reflexní prvky, protože v zimě se běhá hlavně za tmy, a ploché švy, které neodírají.</p>'
          '<h2>Rukavice, čepice a doplňky</h2>'
          '<p>Zimní doplňky tvoří pletené čepice řady MTN, lyžařské rukavice a palčáky, včetně dětských palčáků Ultimate. Palčáky hřejí lépe než prstové rukavice, protože se prsty navzájem zahřívají, ale hůř se v nich ovládají zipy a vázání. Na skialpy se hodí tenké rukavice na výstup a teplejší na sjezd. Na kolo jsou v nabídce letní rukavice s krátkými prsty i delší podzimní.</p>'
          '<h2>Kola Scott v katalogu</h2>'
          '<p>Jízdní kola jsou dnes pro značku velmi důležitá, české obchody, které sporteka.cz sleduje, je ale nabízejí jen výjimečně. Najdete tu například celoodpružené horské kolo Spark nebo horské elektrokolo Aspect eRide. U kol vždy porovnejte rok modelu, velikost rámu a osazení komponentů, protože stejné jméno modelu se prodává v mnoha verzích. '
          'Široký výběr jiných značek najdete v kategoriích <a href="/celoodpruzena-horska-kola/">celoodpružená horská kola</a> a <a href="/horska-elektrokola/">horská elektrokola</a>.</p>'
          '<h2>Vesty a hybridní bundy</h2>'
          '<p>Scott nabízí i sportovní vesty a hybridní bundy, které kombinují zateplený trup s pružnými rukávy. Hodí se na skialpy, zimní běh nebo na kolo za chladného rána. Vesta hřeje na trupu a nechává volné paže, takže se v ní člověk tolik nezapotí. Některé bundy Insuloft mají syntetickou výplň Primaloft, která hřeje i ve vlhku. '
          'Nosí se jako vrstva pod nepromokavou bundu nebo samostatně za suchého počasí. Další modely najdete v kategorii <a href="/sportovni-vesty/">sportovní vesty</a>.</p>'
          '<h2>Péče o membrány</h2>'
          '<ul><li>Bundy s membránou perte podle štítku, obvykle na 30 °C, s tekutým pracím prostředkem bez aviváže.</li>'
          '<li>Před praním zapněte všechny zipy a suché zipy, aby nepoškodily látku.</li>'
          '<li>Když voda přestane perlit, obnovte vodoodpudivou úpravu impregnací. Některé materiály ji podle výrobce aktivuje i teplo v sušičce.</li>'
          '<li>Běžecké boty nesušte na topení. Vyndejte vložku a vycpěte je novinami.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Scott v názvech používá zkratky M\'s a W\'s pro pánské a dámské střihy, u bot pak číslo verze, například Kinabalu 3. Starší verze bývají levnější, ale mohou mít jinou podrážku nebo tlumení, proto čtěte popis. U oblečení se v některých nabídkách objevuje slovo vzorek. Jde o vzorkové kusy, které mohou mít jen jednu velikost, často M nebo S. '
          'Srovnejte proto velikost, verzi modelu a podmínky vrácení. Pokud porovnáváte se značkami jako '
          + B(('dynafit', 'Dynafit'), ('specialized', 'Specialized'), ('salomon', 'Salomon')) +
          ', zaměřte se na technické parametry, ne na název řady.</p>',
    faq=[
        ('Kdo založil značku Scott?',
         'Ed Scott, inženýr a lyžařský závodník ze Sun Valley v Idahu. V roce 1958 vyvinul hliníkovou lyžařskou hůl, která nahradila hole z bambusu a oceli.'),
        ('Kde má Scott sídlo?',
         'Centrála je v Givisiez u Fribourgu ve Švýcarsku, kde firma otevřela evropské sídlo v roce 1978.'),
        ('Jaký je rozdíl mezi Kinabalu a Pursuit?',
         'Kinabalu je trailová bota s hrubým vzorkem do terénu. Pursuit je silniční bota s měkčím tlumením na asfalt. Kdo běhá po obou površích, zvolí spíš univerzálnější trailový model s nižším vzorkem.'),
        ('Co znamená Dryo u lyžařských bund?',
         'Je to označení vlastní membrány Scott. U modelu Ultimate Dryo 10 výrobce uvádí vodní sloupec 10 000 mm.'),
        ('Co znamená slovo vzorek v nabídce Scott?',
         'Jde o vzorkový kus z kolekce. Bývá jen v jedné velikosti, proto si ji před objednáním ověřte.'),
        ('Najdu na sporteka.cz kola Scott?',
         'Jen ojediněle. Většinu nabídky tvoří obuv, oblečení a lyžařské a cyklistické doplňky. Kola jiných značek najdete v cyklistických kategoriích.'),
        ('Jak vybrat velikost běžeckých bot?',
         'Před palcem nechte rezervu zhruba na šířku palce. Boty zkoušejte odpoledne a s ponožkami, ve kterých běháte.'),
        ('Potřebuju běžecké boty s Gore-Tex?',
         'Hodí se na mokro, bláto a chladné počasí. V létě je bota bez membrány vzdušnější a rychleji schne. Když voda nateče přes kotník, membránová bota schne naopak déle.'),
        ('Jak prát lyžařskou bundu Scott?',
         'Podle štítku, obvykle na 30 °C s tekutým prostředkem bez aviváže. Zipy zapněte a vodoodpudivou úpravu občas obnovte. Aviváž ucpává póry membrány a zhoršuje prodyšnost.'),
        ('Prodává sporteka.cz zboží Scott?',
         'Ne, sporteka.cz jen porovnává nabídky obchodů. Nákup a dopravu domlouváte s e-shopem, který si vyberete.'),
    ],
)

# ------------------------------------------------------------------ salewa
NEW['salewa'] = dict(
    title='Salewa boty, bundy a vybavení na via ferraty',
    desc='Salewa v katalogu: trekové boty Mountain Trainer, Alp Trainer, Pedroc a Wildfire, bundy Puez a Ortles, via ferrata sety a přilby. Jak vybrat velikost.',
    intro='<p>Salewa je horská značka s orlem v logu, která vznikla v Mnichově a dnes sídlí v jihotyrolském Bolzanu. V katalogu sporteka.cz má velmi široký sortiment a nejčastěji ji lidé hledají kvůli botám. '
          'Převažují nízké i vysoké trekové boty, například Mountain Trainer, Alp Trainer, Pedroc, Puez nebo nástupové boty Wildfire. K nim patří bundy s membránou, softshelly, fleecové mikiny, outdoorové kalhoty, trička, košile, zimní a péřové bundy, batohy, čepice a rukavice. '
          'Pro lezce a ferratisty jsou v nabídce via ferrata sety, sedáky, přilby a rukavice. '
          'Sporteka nabídky e-shopů jen porovnává, takže snadno zjistíte, kde je vaše číslo boty skladem. '
          'Níže vysvětlujeme řady bot, zkratky jako GTX, PTX a DST, velikosti a péči o kůži a membrány. Nejvíc prostoru věnujeme botám, protože o ně je u této značky největší zájem, včetně rozdílu mezi nízkou a vysokou verzí.</p>',
    guide='<h2>Odkud Salewa pochází</h2>'
          '<p>Firmu založil 8. července 1935 v Mnichově Josef Liebhart jako sesterskou společnost družstva sedlářů. Název je složený ze začátků německých slov Sattler, Leder a Waren, tedy sedlář, kůže a zboží. Z kožené galanterie se firma postupně přesunula k vybavení do hor. '
          'V roce 1990 ji koupil Heiner Oberrauch a začlenil do skupiny Oberalp. Sídlo se pak přestěhovalo do Bolzana v Jižním Tyrolsku. Do stejné skupiny patří i '
          + B(('dynafit', 'Dynafit')) +
          '. Řada modelů nese jména hor a horských skupin z Dolomit a okolí, například Puez, Sella, Brenta nebo Ortles.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Zdaleka nejvíc je <a href="/trekova-obuv/">trekové obuvi</a>, a to v nízkém i vysokém provedení. Samostatně můžete procházet <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> a <a href="/trailove-boty/">trailové boty</a>. Z oblečení jsou nejpočetnější přechodové bundy, trička a mikiny, dále <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a>, košile, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/nepromokave-bundy/">nepromokavé bundy</a>. '
          'Menší, ale zajímavou část tvoří lezecké vybavení: přilby Toxo 3.0, Aria a Pura 2.0, ferratové sety, sedáky, <a href="/turisticke-batohy/">turistické batohy</a> a spacáky.</p>'
          + T(['Řada', 'Typ', 'Na co se hodí'], [
              ['Mountain Trainer 2, MTN Trainer 3', 'pevná treková bota, nízká i Mid', 'túry v horách, kamenité stezky, ferraty'],
              ['Alp Trainer 2', 'lehčí horská bota', 'hory, ferraty, delší túry'],
              ['Wildfire', 'nástupová bota s lezeckou špičkou', 'cesta pod skálu, lehké ferraty'],
              ['Pedroc', 'lehké boty a oblečení na rychlou turistiku', 'speed hiking, běh do kopce'],
              ['Puez', 'trekové boty, bundy, mikiny a kalhoty', 'běžná turistika'],
              ['Ortles', 'technické oblečení a rukavice', 'vysokohorská turistika'],
              ['Premium Attac, Ergo Core, Ergo Zip', 'via ferrata sety s tlumičem pádu', 'zajištěné cesty']]) +
          '<h2>Boty Salewa: jak vybrat řadu</h2>'
          '<p>Mountain Trainer je nejznámější treková bota značky. Kombinuje pevný svršek s podrážkou Vibram a má přední část s lezeckou zónou, takže drží i na skále. Verze Mid sahá nad kotník a hodí se na delší túry s batohem. Alp Trainer je o něco lehčí a hodí se na celodenní túry i na ferraty. '
          'Wildfire je nástupová bota, tedy obuv na cestu pod skálu a lehké lezecké pasáže. Pedroc je naopak lehká a měkčí, určená na rychlou chůzi a krátké túry. Pokud nevíte, kterou zvolit, začněte u terénu: na kamení a sutě tužší podrážka, na lesní cesty měkčí.</p>'
          '<h2>Zkratky GTX, PTX, DST a 3F</h2>'
          '<p>GTX znamená membránu Gore-Tex, PTX je vlastní membrána Salewa s názvem Powertex. Obě udrží vodu venku, ale zhorší odvětrání, takže v létě se v nich noha víc potí. DST označuje strečový materiál Durastretch, který se používá u kalhot a softshellů. '
          '3F system je systém kevlarových lanek, která propojují šněrování s patou a pomáhají ji držet na místě. Najdete ho například u Mountain Trainer 2 Mid nebo u některých modelů Pedroc. RDS u péřových bund znamená, že peří je certifikované podle standardu Responsible Down Standard.</p>'
          '<h2>Velikosti a střih bot</h2>'
          '<p>Salewa vyrábí boty v pánských a dámských verzích, dámské mají užší patu a nižší nárt. V nabídkách se objevují britská i evropská čísla, často ve tvaru UK 7,5, proto si převod ověřte v tabulce. Trekové boty zkoušejte s ponožkami, ve kterých chodíte, a odpoledne. '
          'Při chůzi z kopce nesmí prsty narážet do špičky. Pokud máte širší chodidlo, hledejte modely s volnější přední částí nebo vyzkoušejte jinou řadu. Porovnání s jinými výrobci najdete v přehledech <a href="/damske-trekove-boty/">dámské trekové boty</a> a <a href="/trekove-boty-panske/">pánské trekové boty</a>.</p>'
          '<h2>Vybavení na via ferraty</h2>'
          '<p>Salewa patří k výrobcům, kteří mají kompletní vybavení na zajištěné cesty. Základem je via ferrata set s tlumičem pádu a dvěma karabinami, například Premium Attac, Ergo Core nebo Ergo Zip. Set musí splňovat normu EN 958 a výrobce u něj uvádí rozsah hmotnosti uživatele. Lehčí děti proto potřebují ještě jištění lanem. '
          'Dále je potřeba sedák podle normy EN 12277, třeba Via Ferrata Evo, a přilba podle normy EN 12492, například Toxo 3.0. Ferratové rukavice chrání dlaně před ocelovým lanem. Přehled všech potřebných věcí najdete v kategorii <a href="/via-ferrata/">via ferrata</a>, další doplňky v kategoriích <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky a pomůcky</a> a <a href="/lezecka-lana-a-karabiny/">lana a karabiny</a>.</p>'
          '<ul><li>Ferratový set kupujte nový a se známou historií. Tlumič pádu po zachyceném pádu vyřaďte.</li>'
          '<li>Po každé sezóně zkontrolujte švy, popruhy a funkci zámků karabin.</li>'
          '<li>Výrobce uvádí maximální životnost textilních částí, sledujte ji v návodu.</li></ul>'
          '<h2>Bundy, kalhoty a vrstvy</h2>'
          '<p>Bundy Puez s membránou Powertex jsou lehké a hodí se na běžnou turistiku. Řada Ortles je technickější a počítá s vysokohorskými podmínkami. Do zimy jsou v nabídce <a href="/perove-bundy/">péřové bundy</a> a bundy se syntetickou výplní. Kalhoty Pedroc a Puez z materiálu Durastretch pruží při výstupu a rychle schnou. '
          'Hodně se prodávají i trička s logem orla, bavlněná na volný čas i funkční z polyesteru. Při vrstvení dodržujte pravidlo: funkční vrstva u těla, fleece jako hřejivá vrstva a nahoře bunda proti větru a dešti.</p>'
          '<h2>Batohy, spacáky a doplňky</h2>'
          '<p>Batohy Salewa jsou převážně turistické, například lehký Ultralight 22 l. Na jednodenní ferratu stačí batoh kolem dvaceti litrů s možností připnout přilbu zvenku. Ve výběru jsou také <a href="/spaci-pytle/">spací pytle</a>, například Rozes, a <a href="/lahve-a-termosky/">lahve a termosky</a>. '
          'Na ruce se při práci s lanem hodí kožené rukavice řady Ortles, na hlavu pletené čepice a čelenky s logem orla.</p>'
          '<h2>Jedny boty na všechno?</h2>'
          '<p>Kromě trekové obuvi jsou v nabídce i tenisky a lehčí boty, které se hodí do města a na výlety po rovině. Na kamenité stezky v horách je ale nenahradí. Pokud hledáte jedny boty na většinu letních výletů, zvolte nízkou trekovou botu s membránou, například Alp Trainer 2 GTX. Zvládne turistiku i jednodušší ferratu a v mokré trávě udrží nohy v suchu.</p>'
          '<h2>Trička, košile a mikiny</h2>'
          '<p>Trička s logem orla patří k nejčastějším kouskům v nabídce. Bavlněná verze se hodí do města a k táboráku, na túru je lepší funkční tričko, které rychle schne a nestudí, když se zapotíte. Košile Salewa bývají z lehkého materiálu s krátkým i dlouhým rukávem a v létě chrání ramena před sluncem. '
          'Mikiny řad Puez a Pedroc jsou z technických materiálů a slouží jako hřejivá vrstva pod bundu. Do chladného rána se pod ně hodí <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<h2>Péče o boty a oblečení</h2>'
          '<ul><li>Boty po túře očistěte kartáčem a vlhkým hadříkem, vyndejte vložky a nechte je uschnout při pokojové teplotě, ne na topení.</li>'
          '<li>Kůži ošetřujte přípravkem určeným pro boty s membránou, aby neucpal její póry.</li>'
          '<li>Bundy s membránou perte na nízkou teplotu bez aviváže a obnovte impregnaci.</li>'
          '<li>Péřovou bundu perte se speciálním prostředkem na peří a sušte s tenisovými míčky, aby se peří nerozlepilo.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>Salewa vydává modely v několika verzích, například Mountain Trainer 2 a 3, a v různých kombinacích kůže a membrány. Při porovnání vždy kontrolujte celé označení: číslo verze, výšku Mid nebo Low, membránu GTX nebo PTX a zda jde o pánskou, nebo dámskou verzi. Starší verze bývají v doprodeji výhodnější. '
          'Pokud porovnáváte s jinými horskými značkami, podívejte se také na '
          + B(('la-sportiva', 'La Sportiva'), ('mammut', 'Mammut'), ('the-north-face', 'The North Face')) +
          '.</p>',
    faq=[
        ('Co znamená název Salewa?',
         'Je složený ze začátků německých slov Sattler, Leder a Waren, tedy sedlář, kůže a zboží.'),
        ('Je Salewa italská, nebo německá značka?',
         'Vznikla v Mnichově v roce 1935. Od roku 1990 patří do skupiny Oberalp a sídlí v Bolzanu v Jižním Tyrolsku.'),
        ('Jaký je rozdíl mezi GTX a PTX?',
         'GTX je membrána Gore-Tex, PTX je vlastní membrána Salewa Powertex. Obě jsou nepromokavé, liší se výrobcem a materiálem. V obou případech platí, že v horkém létě se v botě s membránou noha víc potí.'),
        ('Jak padnou boty Salewa?',
         'Dámské verze mají užší patu a nižší nárt. Ověřte převod britských čísel na evropská a zkoušejte s trekovými ponožkami. Při chůzi z kopce nesmí prsty narážet do špičky.'),
        ('Jaký je rozdíl mezi Mountain Trainer a Alp Trainer?',
         'Mountain Trainer je pevnější treková bota do náročného terénu. Alp Trainer je lehčí a hodí se na delší túry a ferraty.'),
        ('Co je 3F system?',
         'Systém lanek, která propojují šněrování s patou a pomáhají ji držet v botě na místě. Najdete ho například u Mountain Trainer 2 Mid.'),
        ('Co potřebuju na via ferratu?',
         'Ferratový set podle normy EN 958, sedák podle EN 12277, lezeckou přilbu podle EN 12492 a ideálně ferratové rukavice.'),
        ('Můžu koupit ferratový set z druhé ruky?',
         'Nedoporučuje se. Neznáte historii setu a tlumič pádu po zachyceném pádu už nemusí fungovat. Bezpečnostní vybavení kupujte nové a schovejte si návod.'),
        ('Jak se starat o kožené boty s membránou?',
         'Po túře je očistěte a usušte při pokojové teplotě. Kůži ošetřujte přípravkem, který neucpe póry membrány. Na semiš používejte sprej, ne vosk.'),
        ('Prodává sporteka.cz boty Salewa?',
         'Ne, sporteka.cz jen srovnává nabídky obchodů. Vyberete si e-shop a objednávku dokončíte přímo u něj.'),
    ],
)

# ------------------------------------------------------------------ roxy
NEW['roxy'] = dict(
    title='Roxy: snowboardové bundy, plavky a neopreny',
    desc='Roxy v katalogu: dámské a dívčí snowboardové bundy a kalhoty, plavky, lycra trička, neopreny, žabky a čepice. Jak vybrat velikost a porovnat nabídky.',
    intro='<p>Roxy je dámská značka, která vzešla ze surfové firmy Quiksilver. V katalogu sporteka.cz se dělí na dvě sezóny. Na zimu jsou tu snowboardové a lyžařské bundy, kalhoty, rukavice, brýle, helmy a čepice, mezi nimi modely Stated, Stormdash, Dawnrae, Jetty nebo Backyard. '
          'Na léto plavky, dvoudílné i jednodílné, lycrová trička s UV ochranou, surfové neopreny, žabky a plážové ručníky. Většina nabídky je pro ženy, menší část pro dívky. '
          'Sporteka nabídky e-shopů porovnává a ukazuje vedle sebe, objednávat budete u obchodu, který si zvolíte. '
          'V průvodci se dočtete, co znamenají údaje 10K a 15K u bund, jak vybrat velikost plavek a neoprenu a jak o věci pečovat, aby vydržely více sezón. Pro snadnou orientaci zimní a letní část nabídky rozebíráme zvlášť. Značka se hodí snowboardistkám a lyžařkám, které chtějí barevnější oblečení, i ženám, které na dovolené surfují, plavou nebo jen leží u moře. Velikosti odpovídají běžné dámské konfekci.</p>',
    guide='<h2>Odkud Roxy pochází</h2>'
          '<p>Roxy vznikla v roce 1990 jako dámská linie australsko-americké surfové značky Quiksilver. Začínala plavkami a postupně přidala oblečení, snowboardové vybavení a doplňky. Logo ve tvaru srdce vzniklo ze dvou zrcadlově otočených log Quiksilver. '
          'Od roku 2023 patří Roxy americké skupině Authentic Brands Group, která tehdy koupila mateřskou firmu Boardriders. Do stejné rodiny značek patří i '
          + B(('dc-shoes', 'DC Shoes')) +
          '.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Největší skupinou jsou <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>, druhou <a href="/plavky/">plavky</a> a třetí <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>. Dále jsou silně zastoupené <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>, <a href="/neopreny/">neopreny</a>, mikiny, čepice a <a href="/damske-plavky/">dámské plavky</a> prodávané po dílech. '
          'Menší podíl mají <a href="/zimni-bundy/">zimní bundy</a> do města, <a href="/kabaty-a-parky/">parky</a>, <a href="/pantofle-a-zabky/">žabky</a>, <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-bryle/">brýle</a> a <a href="/plazove-doplnky/">plážové doplňky</a>. Hledáte-li jen plavky této značky, mrkněte do přehledu <a href="/roxy-plavky/">plavky Roxy</a>.</p>'
          + T(['Skupina', 'Typické modely', 'Poznámka'], [
              ['Snowboardové bundy', 'Stated, Stormdash, Dawnrae, Jetty, Meade, Snowstorm', 'membrány 10K až 20K, u některých Gore-Tex'],
              ['Snowboardové kalhoty', 'Nadia, Backyard, Creek, modely na šlech', 'volnější střih, sněhové návleky'],
              ['Dívčí bundy', 'Galaxy, Sandrift, Jet Ski', 'velikosti podle věku nebo výšky'],
              ['Plavky', 'jednodílné, bikiny, díly zvlášť', 'surfové i plážové střihy'],
              ['Lycra a UV trička', 'Whole Hearted, Enjoy Waves', 'krátký i dlouhý rukáv, UPF'],
              ['Neopreny', 'Prologue, Swell Series, Elite', 'tloušťky 2 mm, 3/2 mm, 4/3 mm']]) +
          '<h2>Snowboardové bundy: co znamená 10K a 15K</h2>'
          '<p>Čísla 10K, 15K nebo 20K v názvu bundy udávají vodní sloupec membrány v tisících milimetrů. Bunda 10K stačí na běžný den na sjezdovce a občasné sněžení, 15K a 20K vydrží déle v mokrém sněhu a dešti. Některé modely, například Stormday, mají membránu Gore-Tex. Druhý údaj, prodyšnost, se uvádí v gramech na metr čtvereční za den a čím je vyšší, tím lépe bunda odvádí páru. '
          'Snowboardové bundy jsou obvykle delší a volnější než lyžařské. Kryjí bedra při sezení na sněhu a nechávají prostor pro vrstvy. Sledujte sněhový pás, kapuci, kterou jde přetáhnout přes helmu, a větrací zipy v podpaží.</p>'
          '<h2>Kalhoty a velikosti</h2>'
          '<p>Kalhoty Roxy se prodávají v klasickém střihu s pasem i na šlech, které lépe drží a nepouštějí sníh k zádům. Dámské velikosti odpovídají běžné konfekci XS až XL, ale u snowboardových kalhot počítejte s volnějším střihem. Pokud pod ně nosíte chrániče nebo silnější termoprádlo, ověřte obvod boků v tabulce. '
          'Dívčí modely mají velikosti podle věku nebo výšky. Při výběru nechte rezervu na rok růstu, ale ne víc, jinak budou rukávy překážet v rukavicích. Další modely najdete v přehledech <a href="/damska-lyzarska-bunda/">dámská lyžařská bunda</a> a <a href="/damske-lyzarske-kalhoty/">dámské lyžařské kalhoty</a>.</p>'
          '<h2>Plavky na surf i na pláž</h2>'
          '<p>Roxy rozlišuje plavky na koupání a opalování a plavky na aktivní sport. Surfové střihy mají širší ramínka, pevnější lemy a spodní díl, který při vlnách drží na místě. Plážové bikiny mají často menší střih a zavazování. Spodní díly typu cheeky jsou vzadu výrazně vykrojené. '
          'Díly se často prodávají zvlášť, takže můžete zvolit jinou velikost nahoře a dole. U horního dílu sledujte, zda má vyjímatelné vycpávky a zda jde o typ bralette, nebo s kosticí. Srovnání s dalšími značkami najdete v přehledu <a href="/damske-plavky-roxy/">dámské plavky Roxy</a>.</p>'
          '<h2>Lycra, neopreny a UV ochrana</h2>'
          '<p>Lycrová trička neboli rashguardy chrání při surfování před odřením o prkno a před sluncem. Hodnota UPF udává, kolikrát méně UV záření projde látkou. Nezakrytá místa ale stále potřebují opalovací krém. '
          'Neopreny se značí tloušťkou v milimetrech, například 4/3 mm, kde první číslo platí pro trup a druhé pro rukávy a nohy. Krátký neopren 2 mm je na léto, 3/2 mm na teplejší moře a jaro, 4/3 mm do chladnější vody. Zip na hrudi lépe těsní, zip na zádech se snadněji obléká. Neopren musí sedět těsně, ale nesmí omezovat dýchání a pohyb ramen.</p>'
          '<h2>Rukavice, brýle a helmy</h2>'
          '<p>K bundám se hodí rukavice a palčáky, některé s membránou Gore-Tex nebo zateplením Primaloft. Snowboardistky často volí palčáky nebo rukavice s delší manžetou, kterou lze přetáhnout přes rukáv. Brýle Roxy se vyrábějí i v dětských velikostech, například model Missy, které sednou k menší helmě. '
          'U brýlí sledujte filtrační kategorii skla: na slunce S3, do mlhy S1 nebo S2. <a href="/lyzarske-helmy/">Lyžařské helmy</a> musí splňovat normu EN 1077. Před nákupem změřte obvod hlavy nad obočím a helmu vyzkoušejte s brýlemi.</p>'
          '<h2>Jak se obléknout na snowboard</h2>'
          '<p>Na snowboardu se střídá námaha a sezení na sněhu, proto se vyplatí vrstvení. U těla funkční triko nebo <a href="/termopradlo/">termoprádlo</a>, které odvádí pot. Jako druhá vrstva tenká mikina nebo fleece, navrch bunda a kalhoty s membránou. Bavlněné tričko pod bundu nepatří, protože nasákne potem a začne studit. Začátečnice ocení chrániče zápěstí a kostrče, pro které je potřeba nechat v kalhotách trochu místa.</p>'
          '<h2>Oblečení mimo sezónu</h2>'
          '<p>Mezi zimou a létem nabízí Roxy mikiny, trička s potiskem, tepláky, šaty a legíny. Střihy jsou volnější a inspirované plážovým stylem, s motivy vln, květin a srdcového loga. Mikiny bývají z počesané bavlny nebo fleecu. Do města jsou v nabídce prošívané bundy a parky, které nejsou určené na svah, ale do mrazu na chodník. Dívkám jsou určená menší čísla plavek, lycrová trička s UV ochranou a dětské žabky.</p>'
          '<h2>Výbava pro začátečnice i pokročilé</h2>'
          '<p>Na první sezóny na prkně stačí bunda a kalhoty s membránou 10K, sněhovým pásem a dostatkem kapes. Více se vyplatí investovat do pohodlných bot a dobře padnoucí helmy. Kdo jezdí často, i mimo upravené tratě nebo v mokrém sněhu, ocení membránu 15K, 20K nebo Gore-Tex, podlepené švy a větrání v podpaží. '
          'Na jarní lyžování se hodí lehčí bunda bez zateplení, pod kterou podle teploty přidáte vrstvy.</p>'
          '<h2>Žabky a plážové doplňky</h2>'
          '<p>K plavkám nabízí Roxy žabky, například řadu Viva, a plážové ručníky. Žabky jsou určené na pláž a k bazénu, na delší chůzi se nehodí, protože nepodpírají klenbu a pata v nich klouže. Pro děti jsou v nabídce žabky z měkké gumy. K vodě se hodí i <a href="/obuv-do-vody/">obuv do vody</a>, která chrání chodidla před kameny a ježovkami.</p>'
          '<h2>Péče o oblečení Roxy</h2>'
          '<ul><li>Plavky a lycru po koupání v moři nebo bazénu vymáchejte ve sladké vodě a sušte ve stínu.</li>'
          '<li>Neopren oplachujte zevnitř i zvenku, sušte naruby na širokém ramínku a nedávejte ho na přímé slunce.</li>'
          '<li>Snowboardovou bundu perte podle štítku s prostředkem bez aviváže a obnovte vodoodpudivou úpravu.</li>'
          '<li>Rukavice Gore-Tex sušte volně, ne na radiátoru, aby se nepoškodila membrána.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>Roxy každý rok obnovuje kolekce a stejný název bundy se objevuje v několika ročnících s jinými barvami a někdy i jinou membránou. Při porovnání proto sledujte nejen název, ale i údaj 10K či 15K, kód modelu a sezónu. Starší ročníky bývají v doprodeji, ale zbývají v nich obvykle jen krajní velikosti. '
          'U plavek ověřte, zda nabídka obsahuje celý komplet, nebo jen jeden díl. Názvy jako plavková podprsenka nebo plavkové kalhotky prozradí, že jde o samostatný díl. Nejvýhodnější bývá nákup snowboardového oblečení na jaře a plavek na konci léta, kdy obchody doprodávají končící kolekci. Počítejte ale s tím, že oblíbené velikosti S a M mizí jako první.</p>',
    faq=[
        ('Komu patří značka Roxy?',
         'Roxy vznikla v roce 1990 jako dámská linie Quiksilver. Od roku 2023 ji vlastní Authentic Brands Group.'),
        ('Co znamená logo Roxy?',
         'Srdce vzniklo ze dvou zrcadlově otočených log Quiksilver.'),
        ('Co znamená 10K u snowboardové bundy?',
         'Vodní sloupec membrány 10 000 mm. Na běžný den na sjezdovce stačí, do mokrého sněhu je lepší 15K a víc. Sledujte i prodyšnost, která se uvádí v gramech.'),
        ('Jsou snowboardové bundy Roxy jen dámské?',
         'Většina ano, menší část je určená dívkám. Pánské modely značka nevyrábí. Dívčí bundy mají velikosti podle věku nebo výšky.'),
        ('Můžu koupit horní a spodní díl plavek v jiné velikosti?',
         'Ano, díly se často prodávají zvlášť. Podle názvu nabídky si ověřte, zda kupujete celý komplet, nebo jeden díl. Barvy a vzory dílů z jedné kolekce k sobě obvykle ladí.'),
        ('Jakou tloušťku neoprenu vybrat?',
         'Na léto stačí 2 mm, do teplejšího moře 3/2 mm, do chladnější vody 4/3 mm. Neopren musí sedět těsně, ale nesmí omezovat dýchání.'),
        ('Nahradí lycrové triko opalovací krém?',
         'Ne úplně. Látka s UPF chrání zakrytá místa, obličej, ruce a nohy je potřeba namazat krémem. Při surfování krém obnovujte, protože ho voda smývá.'),
        ('Jak vybrat velikost dívčí bundy?',
         'Podle výšky dítěte s rezervou zhruba na rok. Příliš dlouhé rukávy překážejí v rukavicích. Pod bundu počítejte s mikinou nebo fleecem.'),
        ('Jak se starat o neopren?',
         'Po každém použití ho opláchněte ve sladké vodě a usušte naruby ve stínu na širokém ramínku. Neperte ho v pračce a nežehlete, teplo materiál poškodí.'),
        ('Prodává sporteka.cz zboží Roxy?',
         'Ne. Sporteka.cz ukazuje nabídky obchodů vedle sebe, nákup proběhne u e-shopu, který si vyberete.'),
    ],
)

# ------------------------------------------------------------------ mammut
NEW['mammut'] = dict(
    title='Mammut: trekové boty, bundy, batohy a lezecká lana',
    desc='Mammut v katalogu: trekové boty Ducan, Sertig a Kento, bundy Ultimate, batohy, fleece, lezecká lana Crag a lavinový vyhledávač Barryvox. Jak vybrat.',
    intro='<p>Mammut je švýcarská horská značka, která začínala výrobou lan a dnes má vybavení od bot po lavinové vyhledávače. V katalogu sporteka.cz jsou nejvíc zastoupené trekové boty, nízké i vysoké, například Ducan, Sertig, Nova nebo Kento. '
          'Následují přechodové a softshellové bundy řady Ultimate, čepice a kšiltovky, tenisky Aenergy a Alnasca, turistické batohy, mikiny, trička a kalhoty. Pro lezce jsou v nabídce lana Crag a pro skialpinisty lavinový vyhledávač Barryvox. '
          'Sporteka nabídky obchodů srovnává, sama nic neprodává. Vidíte tak, kde je konkrétní model a velikost dostupná. '
          'V průvodci najdete historii značky, vysvětlení zkratek HS, SO a ML, rady k výběru bot a lan a tipy na péči. Mammut se hodí turistům, lezcům i lidem, kteří chodí do hor v zimě. Mnoho lidí ho nosí i ve městě, protože softshell nebo hardshell z hor dobře poslouží i cestou do práce. Nabídka zahrnuje pánské, dámské i dětské modely.</p>',
    guide='<h2>Od lan k horskému vybavení</h2>'
          '<p>Historie Mammutu začíná v roce 1862 ve švýcarském Dintikonu, kde si Kaspar Tanner otevřel provaznickou dílnu. První lana sloužila hlavně v zemědělství. Jméno Mammut firma začala používat až o desítky let později. V padesátých letech přišla s nylonovými horolezeckými lany. Dnes do sortimentu patří i lavinový vyhledávač Barryvox. '
          'Od sedmdesátých a osmdesátých let se z výrobce lan postupně stal dodavatel oblečení, bot a batohů. Sídlo firmy je v Seonu v kantonu Aargau.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Nejvíc je <a href="/trekova-obuv/">trekové obuvi</a>, zvlášť můžete procházet <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>. Silně jsou zastoupené přechodové bundy a <a href="/softshellove-bundy/">softshelly</a>, <a href="/cepice-a-celenky/">čepice a kšiltovky</a>, tenisky a <a href="/turisticke-batohy/">turistické batohy</a>. '
          'Dále jsou v nabídce mikiny, trička, <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a> a péřové bundy. Lezecké vybavení zastupují <a href="/lezecka-lana-a-karabiny/">lana a karabiny</a>, menší část <a href="/horolezectvi/">horolezeckých</a> doplňků a v kategorii <a href="/outdoor-doplnky/">outdoor doplňky</a> i lavinový vyhledávač.</p>'
          + T(['Řada', 'Typ', 'Na co se hodí'], [
              ['Ducan', 'lehké trekové boty, Low a High', 'turistika, delší túry'],
              ['Sertig II', 'trekové boty Low a Mid s Gore-Tex', 'turistika v každém počasí'],
              ['Nova IV', 'vysoké trekové boty', 'túry s batohem, kamenité stezky'],
              ['Kento', 'vysokohorské a turistické boty', 'hory, ferraty, lehké výstupy'],
              ['Aenergy, Saentis', 'lehké boty a oblečení', 'rychlá turistika, trail'],
              ['Ultimate', 'softshellové bundy a boty', 'vítr, chladné dny, hory'],
              ['Crag', 'lezecká lana a kalhoty', 'lezení ve skalách a na stěně']]) +
          '<h2>Jak číst názvy oblečení</h2>'
          '<p>Mammut v názvech používá zkratky, které hned prozradí funkci. HS znamená hardshell, tedy nepromokavou bundu s membránou. SO je softshell, který dobře dýchá a chrání před větrem, ale v silném dešti promokne. ML označuje midlayer, tedy hřejivou vrstvu typu fleece, a IN zateplenou bundu. '
          'Díky tomu snadno poskládáte vrstvy: funkční triko, fleecová mikina řady Innominata nebo Aenergy ML a navrch bunda HS nebo SO. Softshell Ultimate je vhodný na vítr a chladný suchý den, při dešti sáhněte po hardshellu.</p>'
          '<h2>Trekové boty: výběr a velikost</h2>'
          '<p>Ducan je lehká bota pro běžnou turistiku, Sertig II stojí mezi turistickou a trekovou obuví a Nova je vysoká bota pro delší túry s batohem. Kento je techničtější a jeho vysoké verze se hodí do skalnatého terénu a na ferraty. GTX v názvu znamená membránu Gore-Tex. '
          'Boty zkoušejte odpoledne a s trekovou ponožkou. Pata nesmí při chůzi klouzat a prsty nesmí narážet do špičky při chůzi z kopce. Pokud máte širší nohu, ověřte, zda daný model nabízí i širší verzi, nebo porovnejte s jinými značkami, například '
          + B(('salewa', 'Salewa'), ('la-sportiva', 'La Sportiva')) +
          '.</p>'
          '<h2>Lezecká lana Crag</h2>'
          '<p>Lana Crag jsou jednoduchá dynamická lana, určená na lezení ve skalách a na stěnách. Musí splňovat normu EN 892. Prodávají se v průměrech 9,5 a 9,8 mm a délkách například 30 nebo 50 metrů. Tenčí lano je lehčí, ale rychleji prokluzuje jisticí pomůckou, takže chce pozornější jištění. Silnější déle vydrží opotřebení, proto se hodí začátečníkům a na stěnu. '
          'Označení Dry znamená, že lano má impregnaci proti nasákavosti. To se hodí v horách, na sněhu a při dešti. Lano chraňte před chemikáliemi, ostrými hranami a UV zářením, skladujte je volně stočené v suchu. Po pádu velkou silou nebo při viditelném poškození opletu je vyřaďte.</p>'
          '<h2>Lavinový vyhledávač Barryvox</h2>'
          '<p>Barryvox je lavinový vyhledávač pro skialpinisty a freeridery. Spolu s lopatou a sondou tvoří základní lavinovou výbavu. Vyhledávač sám o sobě nikoho nezachrání; je potřeba umět ho používat a pravidelně trénovat hledání. Před každou túrou zkontrolujte baterie a proveďte test skupiny. '
          'Další vybavení na túry na lyžích najdete v kategorii <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h2>Batohy</h2>'
          '<p>Batohy Mammut se dělí na městské a turistické. Seon Courier je městský batoh na notebook, Lithium a Ducan jsou turistické. U turistického batohu sledujte objem: na jednodenní túru stačí kolem 20 až 30 litrů, na víkend s přespáním 35 až 50 litrů. Důležitý je bederní pás, který přenáší váhu na boky, a nastavitelná délka zad. Dámské verze mají kratší záda a jinak tvarované ramenní popruhy.</p>'
          '<h2>Tenisky a lehká obuv</h2>'
          '<p>Kromě trekových bot jsou v nabídce i lehčí boty řady Aenergy a Alnasca. Alnasca vychází z nástupové obuvi, tedy bot na cestu pod skálu, a dobře se nosí i na výletech a ve městě. Aenergy je lehká bota na rychlou turistiku a kratší túry. Trailové boty Saentis TR jsou určené na běh a svižnou chůzi po stezkách. Na delší túru s těžkým batohem ale potřebujete pevnější botu s vyšším kotníkem.</p>'
          '<h2>Čepice, kšiltovky a doplňky</h2>'
          '<p>Kšiltovky a čepice s logem mamuta tvoří velkou část nabídky. Kšiltovky jsou bavlněné nebo z lehkého syntetického materiálu, který rychle schne. Na zimu jsou pletené čepice a kukly, například Arctic WS, které chrání obličej v mrazivém větru. Ve výběru jsou i lyžařské ponožky a nákrčníky. Další modely najdete v kategorii <a href="/ksiltovky/">kšiltovky</a>.</p>'
          '<h2>Zimní a péřové bundy</h2>'
          '<p>Do mrazu jsou v nabídce péřové bundy, například Whitehorn, a zateplené bundy Linard. Péří hřeje nejlépe v poměru k hmotnosti, ale po namočení ztrácí objem. Syntetická výplň hřeje i ve vlhku a lépe snáší praní. Na túry v zimě je praktická lehká zateplená bunda, kterou oblečete při zastávce, tlustou péřovku si nechte na dlouhé stání v mrazu.</p>'
          '<h2>Dětské oblečení</h2>'
          '<p>Mammut nabízí i dětské bundy, například hardshell Taiss HS, a dětské lezecké kalhoty Crag. Velikost vybírejte podle výšky a nechte rezervu na růst, u lezeckých kalhot ale ne příliš velkou, aby nohavice nepřekážely. Lezecké kalhoty by měly být z pružného materiálu a neomezovat vysoké kroky.</p>'
          '<h2>Kalhoty na túry a lezení</h2>'
          '<p>Outdoorové kalhoty Mammut se dělí na turistické, například řady Hiking nebo Ducan, a lezecké Crag. U turistických kalhot sledujte, zda jsou z pružného a rychleschnoucího materiálu, jestli mají kapsy na zip a zda jde o letní, nebo zateplené provedení. Odepínací nohavice jsou praktické v létě, ale zipy na koleni mohou dřít. '
          'U lezeckých kalhot je důležitá volnost v sedu a v kolenou. Více modelů najdete v přehledech <a href="/panske-outdoorove-kalhoty/">pánské outdoorové kalhoty</a> a <a href="/damske-outdoorove-kalhoty/">dámské outdoorové kalhoty</a>.</p>'
          '<h2>Péče</h2>'
          '<ul><li>Hardshell perte na nízkou teplotu s prostředkem bez aviváže a obnovujte impregnaci.</li>'
          '<li>Softshell nesušte na topení, látka by mohla ztratit pružnost.</li>'
          '<li>Boty po túře očistěte, vyndejte vložky a sušte při pokojové teplotě.</li>'
          '<li>Lano nešlapte a nenechávejte ho v autě na slunci.</li></ul>'
          '<h2>Jak srovnat nabídky</h2>'
          '<p>U bot Mammut sledujte číslo verze, například Sertig II nebo Nova IV, a výšku Low, Mid či High. Starší verze se mohou lišit podrážkou i střihem. U oblečení zkontrolujte zkratky HS, SO a ML, protože stejný název řady může zahrnovat úplně jiné kusy. '
          'Dámské modely mají v názvu písmeno W nebo slovo Women, pánské Men. U lan ověřte průměr, délku a úpravu Dry. Péřové bundy porovnávejte podle plnivosti a podílu peří, softshelly podle tloušťky a pružnosti materiálu. Stejně důležité jsou podmínky vrácení, protože boty i bundy je lepší vyzkoušet doma s vlastním vybavením. Další horské značky najdete na stránce '
          + B(('the-north-face', 'The North Face')) +
          ' nebo v přehledech jednotlivých kategorií.</p>',
    faq=[
        ('Odkud pochází značka Mammut?',
         'Ze Švýcarska. Začínala v roce 1862 jako provaznická dílna Kaspara Tannera v Dintikonu, dnes sídlí v Seonu v kantonu Aargau.'),
        ('Co znamenají zkratky HS, SO a ML?',
         'HS je hardshell s membránou, SO softshell, ML hřejivá vrstva typu fleece. IN označuje zateplenou bundu.'),
        ('Jaký je rozdíl mezi Ducan a Sertig?',
         'Ducan je lehká bota na běžnou turistiku. Sertig II je univerzální treková bota, v katalogu hlavně ve verzích s membránou Gore-Tex. Obě řady se prodávají v nízkém i vyšším provedení, takže si vyberte podle terénu a zátěže.'),
        ('Jaký průměr lana Crag vybrat?',
         'Na stěnu a pro začátečníky spíš 9,8 mm, které déle vydrží. Lano 9,5 mm je lehčí, ale vyžaduje pozornější jištění.'),
        ('Co znamená Dry u lana?',
         'Lano má impregnaci proti nasákavosti. Hodí se do hor, na sníh a do vlhka. Mokré lano je těžší a hůř se s ním manipuluje.'),
        ('Podle jaké normy se zkouší lezecká lana?',
         'Dynamická lezecká lana musí splňovat normu EN 892. Údaje o počtu normových pádů a průtažnosti najdete v technickém listu lana.'),
        ('Co je Barryvox?',
         'Lavinový vyhledávač Mammut. Spolu s lopatou a sondou tvoří základ lavinové výbavy, používání je potřeba trénovat. Před túrou vždy zkontrolujte baterie.'),
        ('Jak velký batoh vybrat na túru?',
         'Na jednodenní túru kolem 20 až 30 litrů, na víkend s přespáním 35 až 50 litrů. Důležitý je bederní pás a správná délka zad.'),
        ('Je softshell nepromokavý?',
         'Ne úplně. Chrání před větrem a slabým deštěm, do vytrvalého deště patří hardshell s membránou. U Mammutu ho poznáte podle zkratky HS v názvu.'),
        ('Prodává sporteka.cz zboží Mammut?',
         'Ne. Sporteka.cz jen porovnává nabídky e-shopů, objednávka proběhne u obchodu, který si vyberete. Tam řešíte i dopravu, záruku a případné vrácení.'),
    ],
)
