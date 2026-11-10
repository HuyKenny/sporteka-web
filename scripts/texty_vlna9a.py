"""sporteka.cz — snowboards, ski goggles, sleeping bags (3. 11. 2026): full rewrites of three category texts + new sub-categories.
Search phrases from Marketing Miner (cs, 11/2026). Brands from the live catalogue. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ snowboardy
NEW['snowboardy'] = dict(
    title='Snowboardy – pánské, dámské, dětské | Sporteka',
    desc='Snowboardy pánské, dámské a dětské, camber, rocker i hybrid, sety s vázáním. Porovnejte ceny a značky v českých obchodech a vyberte prkno podle váhy.',
    intro='<p><strong>Snowboard</strong> vybíráte podle váhy, stylu jízdy a zkušeností. Na Sportece najdete <strong>pánské, dámské i dětské snowboardy</strong> z českých obchodů na jednom místě a můžete je řadit podle ceny nebo slevy. Nabídku zúžíte filtry podle profilu (camber, rocker, hybrid), tvaru (twin, directional), tuhosti, úrovně jezdce a typu použití.</p>'
          '<p>Kdo začíná, často sáhne po <a href="/snowboardove-sety/">kompletním setu snowboardu s vázáním</a>, kde je kompatibilita vyřešená předem. K prknu patří <a href="/snowboardove-boty/">snowboardové boty</a>, <a href="/snowboardova-vazani/">vázání</a> a <a href="/snowboardove-chranice/">chrániče</a>. Hlavní stránkou celého oboru je <a href="/snowboarding/">snowboarding</a>.</p>',
    guide='<h2>Jak vybrat snowboard</h2>'
          '<p>Prkno musí sedět na vaši váhu a umět to, co od něj chcete. Příliš dlouhý snowboard se hůř otáčí, příliš krátký je v rychlosti nestabilní. Výrobci u každého modelu uvádějí rozsah hmotnosti jezdce, ve kterém deska funguje nejlépe, proto se řiďte jím a ne jen výškou.</p>'
          '<h3>Délka podle hmotnosti</h3>'
          + T(['Hmotnost jezdce', 'Orientační délka'], [['do 50 kg', '135–145 cm'], ['50–65 kg', '145–152 cm'], ['65–80 kg', '152–158 cm'], ['80–95 kg', '158–164 cm'], ['nad 95 kg', '162 cm a více']]) +
          '<h3>Profil desky</h3>'
          '<ul><li><strong>Camber:</strong> klasický prohnutý profil, stabilní a přesný na hranách, vyžaduje trochu zkušeností.</li>'
          '<li><strong>Rocker:</strong> prohnutí opačným směrem, deska odpouští chyby, snadno se otáčí a lépe plave v prašanu.</li>'
          '<li><strong>Hybrid:</strong> kombinace obou profilů, vhodná pro většinu rekreačních jezdců.</li>'
          '<li><strong>Flat:</strong> rovná deska bez prohnutí, plynulá a předvídatelná v parku.</li></ul>'
          '<h3>Tvar a typ použití</h3>'
          '<p><strong>Twin</strong> je symetrický a jede se oběma směry stejně, proto je oblíbený u freestylu. <strong>Directional</strong> má jasný předek a hodí se na rychlou jízdu a freeride. Mezi nimi stojí directional twin.</p>'
          '<ul><li><strong>All-mountain:</strong> univerzální deska na sjezdovku i mimo ni.</li>'
          '<li><strong>Freestyle:</strong> kratší, měkčí a lehčí prkno do parku.</li>'
          '<li><strong>Freeride:</strong> delší a tužší deska na prašan a svahy mimo trať.</li>'
          '<li><strong>Splitboard:</strong> prkno, které se rozdělí na dvě lyže s tulením pásem na stoupání.</li></ul>'
          '<h3>Tuhost a úroveň</h3>'
          '<p>Měkčí deska odpouští chyby a hodí se pro začátečníky a park, tužší drží stopu v rychlosti a na tvrdém sněhu. Výrobci úroveň jezdce označují jako začátečník, pokročilý nebo expert, tento údaj najdete ve filtru.</p>'
          '<h3>Široká deska</h3>'
          '<p>Jezdci s velkou botou, zhruba od velikosti 45, potřebují širší desku, aby jim špičky a paty nezasahovaly do sněhu. Označuje se jako wide.</p>'
          '<h3>Děti a dospívající</h3>'
          '<p>Dětské desky jsou kratší, měkčí a lehčí. Vybírejte podle výšky a váhy dítěte a nekupujte na vyrůstání, protože příliš dlouhé prkno dítě znechutí. Praktický je set s předem namontovaným vázáním.</p>'
          '<h3>Set, nebo samostatně</h3>'
          '<p>Set ušetří starosti s kompatibilitou a bývá cenově výhodnější. Zkušení jezdci si obvykle skládají desku, vázání a boty podle svého stylu. Hotové sety najdete v kategorii <a href="/snowboardove-sety/">snowboardy s vázáním</a>.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou snowboardy značek {B(("raven", "Raven"), ("gravity", "Gravity"), ("ride", "Ride"), ("nitro", "Nitro"), ("head", "Head"), ("hatchey", "Hatchey"), ("beany", "Beany"), ("k2", "K2"), ("burton", "Burton"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Výběr podle výšky místo podle hmotnosti.</li><li>Příliš tuhá deska pro začátečníka, která se hůř ovládá.</li><li>Dětský snowboard kupovaný o několik velikostí navíc.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Po sezóně očistěte skluznici, nechte desku osychat na vzduchu a naneste skluzný vosk. Skladujte ji v obalu na suchém místě, ideálně s uvolněnými vázáními.</p>',
    faq=[('Jak dlouhý snowboard si vybrat?', 'Podle hmotnosti a stylu jízdy. Pro většinu jezdců sahá deska zhruba od brady po nos, přesný rozsah hmotnosti udává výrobce u každého modelu.'),
         ('Jaký snowboard je vhodný pro začátečníka?', 'Spíše měkčí deska s rockerem nebo hybridním profilem, která odpouští chyby a snadno se otáčí. Praktický je set s vázáním.'),
         ('Co je snowboard set?', 'Prkno prodávané společně s vázáním. Kompatibilita je vyřešená předem a set bývá cenově výhodnější než samostatné díly.'),
         ('Jaký je rozdíl mezi twin a directional?', 'Twin je symetrický a jede se oběma směry stejně, directional má jasný předek a hodí se na rychlou jízdu a freeride.'),
         ('Jaký je rozdíl mezi camberem a rockerem?', 'Camber je prohnutý nahoru uprostřed a drží hrany přesněji. Rocker je prohnutý opačně, odpouští chyby a lépe plave v prašanu.'),
         ('Jak poznám, že potřebuju širokou desku?', 'Když jsou špičky nebo paty boty zřetelně přes hranu desky, zhruba od velikosti 45 se vyplatí wide model.'),
         ('Jaký snowboard pro dítě?', 'Krátký, měkký a lehký, podle výšky a váhy dítěte. Příliš dlouhé prkno se špatně ovládá.'),
         ('Jaký snowboard na freestyle a park?', 'Kratší a měkčí twin deska, která snadno rotuje a odpouští dopady.')],
)

# ------------------------------------------------------------------ snowboardove-sety
NEW['snowboardove-sety'] = dict(short=True,
    title='Snowboard s vázáním – komplet a sety | Sporteka',
    desc='Snowboardy s vázáním v setu: pánské, dámské a dětské komplety. Porovnejte ceny a značky v českých obchodech a vyberte hotovou sadu na svah.',
    intro='<p><strong>Snowboard s vázáním</strong> v setu je nejjednodušší cesta na svah. Prkno a vázání jsou k sobě vybraná tak, aby seděly a nemusíte řešit kompatibilitu. Hodí se hlavně pro začátečníky, děti a rekreační jezdce.</p>'
          '<p>Na Sportece porovnáte sety z českých obchodů, pánské, dámské i dětské. Samotná prkna najdete v kategorii <a href="/snowboardy/">snowboardy</a>, k setu ještě vyberte <a href="/snowboardove-boty/">boty</a>.</p>',
    guide='<h2>Jak vybrat snowboard set</h2>'
          '<p>U setu platí stejná pravidla jako u samotné desky: délku vybírejte podle hmotnosti jezdce a zkontrolujte, pro jakou úroveň je prkno určené. Nejčastěji jde o sety pro začátečníky a děti s měkčími deskami.</p>'
          '<h3>Co je v setu</h3>'
          '<p>Set obsahuje snowboard a vázání, často už s namontovanými disky. Boty, helma a chrániče se kupují zvlášť. Vázání v setech jsou spíše univerzální a měkčí, což začátečníkovi vyhovuje.</p>'
          '<h3>Velikost vázání</h3>'
          '<p>Vázání musí odpovídat velikosti boty. Menší velikost se hodí pro boty zhruba do EU 40, střední a větší pak pro dospělé. Dětské sety mají menší vázání s úzkými popruhy.</p>'
          '<h3>Kdy je lepší koupit zvlášť</h3>'
          '<p>Zkušený jezdec chce ladit tuhost, profil a vázání podle svého stylu. Pro takové zákazníky jsou vhodné samostatné <a href="/snowboardy/">snowboardy</a> a <a href="/snowboardova-vazani/">snowboardová vázání</a>.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Hotové sety nabízejí hlavně značky {B(("raven", "Raven"), ("gravity", "Gravity"), ("hatchey", "Hatchey"), ("beany", "Beany"))}.</p>'
          '<h3>Další výbava</h3>'
          '<p>Ke snowboardu se hodí <a href="/snowboardove-chranice/">chrániče</a>, <a href="/lyzarske-helmy/">helma</a> a <a href="/lyzarske-bryle/">brýle</a>.</p>',
    faq=[('Co obsahuje snowboard set?', 'Snowboard a vázání, často už s namontovanými disky. Boty a ochranné vybavení se kupují zvlášť.'),
         ('Vyplatí se snowboard set?', 'Pro začátečníky a děti obvykle ano, protože díly jsou sladěné a nákup je jednodušší.'),
         ('Jak vybrat velikost snowboardu v setu?', 'Podle hmotnosti jezdce, stejně jako u samotné desky. Výrobce uvádí doporučený rozsah.'),
         ('Sedí vázání v setu na každou botu?', 'Vázání má velikostní rozsah. Před nákupem zkontrolujte, do jaké velikosti boty je určené.'),
         ('Hodí se set pro dítě?', 'Ano, dětské sety mají kratší a měkčí desku a menší vázání. Vybírejte podle výšky dítěte.')],
)

# ------------------------------------------------------------------ lyzarske-bryle
NEW['lyzarske-bryle'] = dict(
    title='Lyžařské brýle – dětské, dámské, pánské | Sporteka',
    desc='Lyžařské a snowboardové brýle: fotochromatické, OTG, s výměnnými zorníky, dětské i dámské. Porovnejte ceny v českých obchodech a vyberte kategorii filtru.',
    intro='<p><strong>Lyžařské brýle</strong> chrání oči před sluncem, větrem a odleskem sněhu. Rozhoduje kategorie zorníku (S0 až S4), jeho tvar a to, jak brýle navazují na helmu. Světlejší zorník se hodí do mlhy a za šera, tmavý na slunce. Dobré brýle nemlží a netlačí.</p>'
          '<p>Na Sportece porovnáte brýle z českých obchodů a nabídku zúžíte podle kategorie filtru, tvaru zorníku (cylindrický, sférický), pro koho jsou a podle vlastností, jako jsou <strong>fotochromatické</strong> zorníky, <strong>OTG</strong> přes dioptrické brýle, magnetická výměna nebo antifog. Brýle se hodí i na snowboard.</p>'
          '<p>K brýlím patří <a href="/lyzarske-helmy/">helma</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice nebo nákrčník</a>. Náhradní zorníky najdete v kategorii <a href="/nahradni-zorniky/">náhradní zorníky a příslušenství</a>.</p>',
    guide='<h2>Jak vybrat lyžařské brýle</h2>'
          '<p>Brýle mají pevně sedět na obličeji a navazovat na okraj helmy bez mezery. Při zkoušení je vždy nasaďte s helmou, jinak můžou tlačit nebo vytvořit mezeru na čele.</p>'
          '<h3>Kategorie zorníku</h3>'
          + T(['Kategorie', 'Podmínky'], [['S0', 'noc, velmi špatná viditelnost'], ['S1', 'mlha, zataženo, večer'], ['S2', 'proměnlivé počasí'], ['S3', 'slunce, běžná sjezdovka'], ['S4', 'vysoké hory, ledovec']]) +
          '<h3>Tvar zorníku</h3>'
          '<p><strong>Cylindrický</strong> zorník je prohnutý jen vodorovně, bývá cenově dostupnější. <strong>Sférický</strong> je zakřivený i svisle, nabízí širší výhled a méně zkreslení.</p>'
          '<h3>Zorníky a technologie</h3>'
          '<ul><li><strong>Fotochromatické:</strong> mění propustnost podle světla, vhodné pro proměnlivé počasí.</li>'
          '<li><strong>Polarizační:</strong> omezují odlesky, užitečné na ledovci a v otevřeném terénu.</li>'
          '<li><strong>Zrcadlové:</strong> odrážejí část světla a lépe snášejí ostré slunce.</li>'
          '<li><strong>Výměnné nebo magnetické:</strong> druhý zorník do mlhy nasadíte bez nářadí.</li>'
          '<li><strong>Dvojitý zorník s antifogem:</strong> méně mlžení.</li></ul>'
          '<h3>OTG pro brýlaře</h3>'
          '<p>Modely označené OTG mají dostatek místa, aby šly nasadit přes dioptrické brýle. Zkontrolujte, že se brýle pohodlně vejdou i do helmy.</p>'
          '<h3>Děti a dámské střihy</h3>'
          '<p>Menší obličej vyžaduje menší rám, dětské a dámské modely mají užší střih. Dětem se hodí brýle s popruhem, který jde zkrátit pro menší helmu, a s UV ochranou zorníku 100 %.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("alpina", "Alpina"), ("uvex", "Uvex"), ("relax", "Relax"), ("rossignol", "Rossignol"), ("smith", "Smith"), ("salomon", "Salomon"), ("scott", "Scott"), ("dragon", "Dragon"), ("meatfly", "Meatfly"))}.</p>'
          '<h3>Péče o zorník</h3>'
          '<p>Zorník se snadno poškrábe, proto brýle po jízdě osušte volně na vzduchu a nečistěte je hrubou látkou. Uložte je do měkkého pouzdra a nenoste je na čele, kde se zamlží a ztratí antifog vrstvu.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Zkoušení brýlí bez helmy.</li><li>Tmavý zorník do mlhy, ve kterém se špatně vidí hrbolky.</li><li>Brýle nošené na čele, kde mlží.</li></ul>',
    faq=[('Jaké lyžařské brýle vybrat?', 'Podle kategorie zorníku a kompatibility s helmou. Pro proměnlivé počasí jsou praktické fotochromatické nebo výměnné zorníky.'),
         ('Co znamená kategorie zorníku?', 'Číslo od 0 do 4 udává, kolik světla zorník propustí. Vyšší číslo znamená tmavší zorník na slunce.'),
         ('Jak zabránit mlžení brýlí?', 'Nezvedat je na čelo, dopřát jim větrání a vybrat model s antifogem a dvojitým zorníkem.'),
         ('Hodí se lyžařské brýle i na snowboard?', 'Ano, brýle jsou určené pro oba sporty.'),
         ('Jaké brýle pro dítě?', 'Dětský střih s měkkým rámem, UV ochranou a nastavitelným popruhem, který sedí na dětskou helmu.'),
         ('Co jsou OTG brýle?', 'Lyžařské brýle s dostatečným prostorem pro nasazení přes dioptrické brýle.'),
         ('Jaký je rozdíl mezi cylindrickým a sférickým zorníkem?', 'Cylindrický je zakřivený jen vodorovně, sférický i svisle a nabízí širší výhled s menším zkreslením.'),
         ('Jak čistit zorník?', 'Měkkou látkou, bez tření, a nechat uschnout na vzduchu.')],
)

# ------------------------------------------------------------------ nahradni-zorniky
NEW['nahradni-zorniky'] = dict(short=True,
    title='Náhradní zorníky a čočky do lyžařských brýlí | Sporteka',
    desc='Náhradní zorníky, čočky a pouzdra pro lyžařské a snowboardové brýle. Porovnejte ceny a dostupnost v českých obchodech a vyberte zorník ke svému modelu.',
    intro='<p><strong>Náhradní zorníky</strong> se hodí, když se původní zorník poškrábe nebo když potřebujete jiný pro mlhu či ostré slunce. Zorník vždy vybírejte přesně k modelu brýlí, protože zorníky různých řad se tvarem a uchycením liší.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů, zorníky, čočky a pouzdra. Samotné brýle najdete v kategorii <a href="/lyzarske-bryle/">lyžařské brýle</a>.</p>',
    guide='<h2>Jak vybrat náhradní zorník</h2>'
          '<p>Nejdůležitější je kompatibilita. Zorník musí odpovídat modelu brýlí, často i konkrétnímu ročníku, a způsobu uchycení: magnetického, na patenty nebo vsazovaného do rámu.</p>'
          '<h3>Kategorie podle počasí</h3>'
          + T(['Podmínky', 'Vhodná kategorie'], [['mlha, šero, večerní lyžování', 'S1 nebo S0'], ['proměnlivé počasí', 'S2'], ['slunečný den', 'S3'], ['ledovec a vysoké hory', 'S4']]) +
          '<h3>Typy zorníků</h3>'
          '<p>Kromě klasických barevných existují zorníky zrcadlové a fotochromatické. Zrcadlová vrstva lépe snáší ostré slunce, fotochromatický zorník mění propustnost podle světla.</p>'
          '<h3>Výměna a ochrana</h3>'
          '<p>Zorník měňte v suchu, bez tlaku na střed čočky a nedotýkejte se vnitřní strany prsty. Náhradní zorník skladujte v pouzdře, aby se nepoškrábal.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Náhradní zorníky nabízejí značky {B(("alpina", "Alpina"), ("r2", "R2"), ("relax", "Relax"), ("rossignol", "Rossignol"), ("briko", "Briko"))}.</p>',
    faq=[('Jak poznám správný náhradní zorník?', 'Podle modelu brýlí uvedeného u zorníku. Zorníky různých řad se obvykle nedají zaměnit.'),
         ('Jaká kategorie zorníku do mlhy?', 'Světlejší, tedy S1 nebo S0. Zvyšují kontrast ve slabém světle.'),
         ('Jak vyměnit zorník?', 'Podle systému brýlí: u magnetických jednoduše odtáhnout, u ostatních uvolnit patenty. Dotýkejte se jen okraje.'),
         ('Jak chránit náhradní zorník?', 'Skladovat v měkkém pouzdře a nikdy ho nečistit hrubou látkou.'),
         ('Hodí se zorníky i na snowboardové brýle?', 'Ano, lyžařské a snowboardové brýle používají stejný typ zorníků.')],
)

# ------------------------------------------------------------------ spaci-pytle
NEW['spaci-pytle'] = dict(
    title='Spací pytle – letní, zimní, péřové a dětské | Sporteka',
    desc='Spací pytle a spacáky pro kemping a trek: letní, zimní, péřové, mumie i dekové. Porovnejte ceny a komfortní teploty v českých outdoorových obchodech.',
    intro='<p><strong>Spací pytel</strong> rozhoduje o tom, jestli se v noci vyspíte, nebo jen přečkáte. Při výběru se řiďte komfortní teplotou, tedy hodnotou, při které se vám bude pohodlně spát. Extrémní teplota je hranice přežití. Rozlišujeme <strong>péřové</strong> spacáky, které jsou lehké a dobře se sbalí, a <strong>syntetické</strong>, které snesou vlhko a jsou levnější.</p>'
          '<p>Na Sportece porovnáte spacáky z českých obchodů a nabídku zúžíte podle teploty použití, výplně, tvaru (mumie, dekový), sezóny, hmotnosti a strany zipu. Hotové kategorie: <a href="/perove-spacaky/">péřové spacáky</a>, <a href="/dekove-spacaky/">dekové spacáky</a>, <a href="/detske-spacaky/">dětské spacáky</a>, <a href="/rybarske-spacaky/">rybářské spacáky</a> a <a href="/vlozky-do-spacaku/">vložky a obaly</a>.</p>'
          '<p>Pod spacák patří <a href="/karimatky-a-matrace/">karimatka nebo matrace</a>, bez izolace od země teplo uniká i z nejlepšího pytle. Pro delší výlety vybírejte i <a href="/stany/">stan</a>.</p>',
    guide='<h2>Jak vybrat spací pytel</h2>'
          '<p>Správný spacák se vybírá podle teploty, hmotnosti a výplně. Zkontrolujte, zda údaje vycházejí z normy EN 13537, která výrobci sjednocuje. Bez normy jsou čísla těžko porovnatelná.</p>'
          '<h3>Teplotní údaje</h3>'
          '<ul><li><strong>Komfortní teplota:</strong> při ní se vyspí průměrná žena bez prochladnutí.</li>'
          '<li><strong>Limitní teplota:</strong> při ní se vyspí průměrný muž stočený do klubíčka.</li>'
          '<li><strong>Extrémní teplota:</strong> hranice přežití, spát se v ní nedá.</li></ul>'
          + T(['Sezóna', 'Komfortní teplota'], [['Léto', '10 °C a více'], ['Třísezónní', 'zhruba 0 až 5 °C'], ['Zima', '−5 °C a méně'], ['Extrémní mráz', 'pod −10 °C']]) +
          '<h3>Péří, nebo syntetika</h3>'
          '<p>Péřová výplň je při stejné teplotě lehčí a po složení menší. Nevýhodou je vyšší cena a ztráta izolace v mokru. Syntetika izoluje i vlhká, dobře schne a snese praní, ale váží víc. Podrobnosti najdete v kategorii <a href="/perove-spacaky/">péřové spacáky</a>.</p>'
          '<h3>Tvar a velikost</h3>'
          '<ul><li><strong>Mumie:</strong> přiléhá k tělu, nejlépe udrží teplo, hodí se na trek.</li>'
          '<li><strong>Dekový:</strong> prostorný a rozepínací, vhodný do auta a do kempu.</li>'
          '<li><strong>Dětský:</strong> menší, často s prodloužením pro rostoucí dítě.</li></ul>'
          '<p>Zkontrolujte délku. Příliš dlouhý spacák vyplní studený vzduch, příliš krátký tlačí a stlačuje izolaci. U zipu rozhodněte, zda potřebujete levý, nebo pravý, a u dvou spacáků do páru dbejte, aby se daly spojit.</p>'
          '<h3>Hmotnost a velikost po sbalení</h3>'
          '<p>Na trek je důležitá hmotnost, do kempu a auta pohodlí. Ultralehké modely vychází z péří a tenkého materiálu, ale jsou dražší a méně odolné.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Spacáky nabízejí hlavně značky {B(("husky", "Husky"), ("trimm", "Trimm"), ("hannah", "Hannah"), ("pinguin", "Pinguin"), ("yate", "Yate"), ("sir-joseph", "Sir Joseph"), ("highlander", "Highlander"), ("sea-to-summit", "Sea to Summit"), ("deuter", "Deuter"), ("ferrino", "Ferrino"))}.</p>'
          '<h3>Péče a skladování</h3>'
          '<p>Spacák nenechávejte stlačený v sáčku. Skladujte ho volně ve větší bavlněné tašce, aby se výplň nesesedla. Pere se podle návodu, péřové s přípravkem určeným na péří. Chránit ho pomůže <a href="/vlozky-do-spacaku/">vložka</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Řízení se extrémní teplotou. Rozhodující je komfortní, jinak budete mrznout.</li>'
          '<li>Spaní ve vlhkém oblečení, které teplo bere.</li>'
          '<li>Spacák bez podložky, protože izolace pod tělem je při stlačení výplně minimální.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Zimní spacáky bývají levnější na jaře, letní na konci sezóny. Dětské velikosti se vyplatí koupit včas, před tábory je nejvíc vyprodané.</p>',
    faq=[('Jaký spacák na léto?', 'Dekový nebo lehký mumie spacák s komfortní teplotou kolem 10 °C. Na chladnější noci vezměte vložku.'),
         ('Co je komfortní teplota spacáku?', 'Teplota, při které se v něm vyspí průměrná žena bez prochladnutí. Pro běžný výběr se řiďte právě touto hodnotou.'),
         ('Péřový, nebo syntetický spacák?', 'Péřový je lehčí a menší po sbalení, syntetický lépe snáší vlhko a bývá levnější. Do mokrého klimatu a pro děti je lepší syntetika.'),
         ('Jaký spacák do zimy?', 'Se zimní komfortní teplotou o několik stupňů pod očekávaným mrazem, nejlépe mumie s kapucí a podložkou s dobrou izolací.'),
         ('Jaký je rozdíl mezi mumií a dekovým spacákem?', 'Mumie přiléhá k tělu a udrží víc tepla, dekový je prostornější, rozepíná se a hodí se do kempu.'),
         ('Jaký spacák pro dítě?', 'Dětský spacák s výplní podle teploty, ideálně s možností prodloužení. Vybírejte podle výšky dítěte.'),
         ('Jak často prát spacák?', 'Jen když je potřeba, obvykle jednou za sezónu nebo po výrazném znečištění. Dodržujte pokyny výrobce.'),
         ('Jak skladovat spací pytel?', 'Volně, v prodyšné velké tašce nebo zavěšený. V malém sáčku se výplň trvale stlačí a ztratí izolaci.')],
)

# ------------------------------------------------------------------ perove-spacaky
NEW['perove-spacaky'] = dict(short=True,
    title='Péřové spacáky – lehké mumie do zimy | Sporteka',
    desc='Péřové spacáky a spací pytle: lehké, malé po sbalení, pro trek i zimní túry. Porovnejte ceny a komfortní teploty v českých obchodech.',
    intro='<p><strong>Péřový spacák</strong> nabízí nejlepší poměr tepla, hmotnosti a velikosti po sbalení. Proto ho volí trekaři a horolezci, kteří nesou všechno na zádech. Slabinou péří je vlhkost, kterou snáší hůř než syntetika.</p>'
          '<p>Na Sportece porovnáte péřové spacáky z českých obchodů. Obecný přehled najdete v kategorii <a href="/spaci-pytle/">spací pytle</a>, pod spacák se hodí <a href="/karimatky-a-matrace/">karimatka</a>.</p>',
    guide='<h2>Jak vybrat péřový spacák</h2>'
          '<p>U péřových spacáků sledujte komfortní teplotu, množství a kvalitu výplně a hmotnost. Čím vyšší hodnota nadouvání (údaj v kubických palcích), tím víc tepla péří při stejné váze izoluje.</p>'
          '<h3>Výhody a nevýhody</h3>'
          '<ul><li><strong>Lehkost:</strong> při stejné teplotě váží méně než syntetický spacák.</li>'
          '<li><strong>Sbalení:</strong> péří se dobře stlačí, spacák zabere málo místa.</li>'
          '<li><strong>Vlhko:</strong> mokré péří ztrácí izolaci a schne pomalu, proto se hodí obal nebo membrána.</li>'
          '<li><strong>Cena:</strong> bývá vyšší, ale výdrží mnoho let.</li></ul>'
          '<h3>Péče o péřový spacák</h3>'
          '<p>Skladujte ho volně, ne stlačený. Pere se jen speciálním přípravkem na péří a suší se s pomocí míčků, aby se výplň nezlepila.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Péřové spacáky nabízejí hlavně {B(("sir-joseph", "Sir Joseph"), ("ferrino", "Ferrino"), ("warmpeace", "Warmpeace"), ("patizon", "Patizon"), ("hannah", "Hannah"), ("sea-to-summit", "Sea to Summit"), ("husky", "Husky"), ("deuter", "Deuter"))}.</p>',
    faq=[('Proč zvolit péřový spacák?', 'Je lehčí a menší po sbalení než syntetický, což ocení každý, kdo spacák nese na trek.'),
         ('Jak se starat o péřový spacák?', 'Skladovat volně, prát přípravkem na péří a pečlivě vysušit.'),
         ('Vadí vlhko péřovému spacáku?', 'Mokré péří ztrácí izolaci, proto spacák chraňte před vlhkem a na mokré túry zvažte syntetiku.'),
         ('Jaká komfortní teplota stačí na třísezónní turistiku?', 'Obvykle kolem 0 až 5 °C, v horách s rezervou i níže.'),
         ('Pere se péřový spacák v pračce?', 'Lze jen podle návodu výrobce, s přípravkem na péří a šetrným programem.')],
)

# ------------------------------------------------------------------ dekove-spacaky
NEW['dekove-spacaky'] = dict(short=True,
    title='Dekové spacáky – pohodlné do kempu a auta | Sporteka',
    desc='Dekové spacáky a spací pytle: prostorné, celorozepínací, na kemping i do chaty. Porovnejte ceny a rozměry v českých obchodech a vyberte spacák.',
    intro='<p><strong>Dekový spacák</strong> se po rozepnutí zip dá rozložit jako přikrývka. Je prostorný a pohodlný, proto se hodí do kempu, na chatu a do auta. Na hmotnost a velikost po sbalení tolik nehledí, ten je výhodný hlavně pohodlím.</p>'
          '<p>Na Sportece porovnáte dekové spacáky z českých obchodů. Přehled všech typů najdete v kategorii <a href="/spaci-pytle/">spací pytle</a>.</p>',
    guide='<h2>Jak vybrat dekový spacák</h2>'
          '<p>Dekový spacák vybírejte podle teploty použití, rozměru a zipu. Pohodlí vychází z prostoru, ale prostorný pytel hůř drží teplo než přiléhavá mumie.</p>'
          '<h3>Výhody a omezení</h3>'
          '<ul><li><strong>Prostor:</strong> ve spacáku se dá otáčet, vhodné pro neklidné spáče.</li>'
          '<li><strong>Rozepínání:</strong> po rozepnutí slouží jako deka nebo se dva spojí do dvojitého.</li>'
          '<li><strong>Teplo:</strong> prostor navíc se musí vyhřát, proto bývá méně vhodný na mráz.</li>'
          '<li><strong>Hmotnost:</strong> je vyšší než u mumie, na trek se obvykle nehodí.</li></ul>'
          '<h3>Spojení dvou spacáků</h3>'
          '<p>Pokud chcete spát ve dvou, vybírejte spacáky s levým a pravým zipem téže řady, které se dají spojit.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Dekové spacáky nabízejí značky {B(("skandika", "Skandika"), ("husky", "Husky"), ("trimm", "Trimm"), ("cattara", "Cattara"), ("crossroad", "Crossroad"), ("hannah", "Hannah"))}.</p>',
    faq=[('Pro koho je dekový spacák?', 'Pro kempování, chatu a spaní v autě, kde nevadí vyšší hmotnost a záleží na pohodlí.'),
         ('Dají se dva dekové spacáky spojit?', 'Ano, pokud jsou z téže řady, jeden s levým a druhý s pravým zipem.'),
         ('Hodí se dekový spacák na zimu?', 'Jen s nízkou komfortní teplotou. Prostor navíc se hůř vyhřívá, na mráz je lepší mumie.'),
         ('Jak se dekový spacák skladuje?', 'Volně nebo volně složený, ne stlačený v sáčku na celou sezónu.'),
         ('Jaký rozměr vybrat?', 'Podle výšky, délka by měla přesahovat tělo o 10 až 20 cm.')],
)

# ------------------------------------------------------------------ vlozky-do-spacaku
NEW['vlozky-do-spacaku'] = dict(short=True,
    title='Vložky do spacáku a obaly – bavlna, hedvábí | Sporteka',
    desc='Vložky do spacího pytle, spacákové přikrývky a kompresní obaly. Porovnejte ceny a materiály v českých obchodech a prodlužte život svému spacáku.',
    intro='<p><strong>Vložka do spacáku</strong> chrání výplň před potem a nečistotou a zároveň přidá zhruba několik stupňů tepla. Dá se vyprat, takže spacák perete méně často. Lehká hedvábná nebo bavlněná vložka se hodí i jako samostatné lůžko v horké noci.</p>'
          '<p>Na Sportece najdete také kompresní vaky a obaly na spacáky. Samotné spacáky jsou v kategorii <a href="/spaci-pytle/">spací pytle</a>.</p>',
    guide='<h2>Jak vybrat vložku do spacáku</h2>'
          '<p>Vložku vybírejte podle tvaru spacáku a materiálu. Měla by mít stejný tvar jako spacák, mumie nebo dekový, aby se nemačkala a neomezovala pohyb.</p>'
          '<h3>Materiály vložek</h3>'
          '<ul><li><strong>Bavlna:</strong> příjemná, dobře pere, ale těžší a pomalu schne.</li>'
          '<li><strong>Hedvábí:</strong> velmi lehká a malá po sbalení, nejlepší na trek.</li>'
          '<li><strong>Syntetika a fleece:</strong> lehká, rychle schne a přidává trochu tepla.</li></ul>'
          '<h3>Kompresní vaky a obaly</h3>'
          '<p>Kompresní vak zmenší spacák na část objemu, hodí se na batoh. Voděodolný obal chrání výplň před vlhkem, především u péřových modelů. Spacák ale nenechávejte v kompresním vaku trvale.</p>'
          '<h3>Spacáková přikrývka a bivak</h3>'
          '<p>Cestovní spacáková přikrývka nahrazuje spacák v teplých podmínkách. Bivakový obal přidává ochranu před větrem a vlhkem.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("sea-to-summit", "Sea to Summit"), ("cocoon", "Cocoon"), ("ferrino", "Ferrino"), ("lifeventure", "LifeVenture"), ("naturehike", "Naturehike"), ("trimm", "Trimm"))}.</p>',
    faq=[('K čemu je vložka do spacáku?', 'Chrání výplň před potem a špínou, dá se vyprat a spacák tak perete méně často.'),
         ('Hřeje vložka do spacáku?', 'Mírně, zhruba o několik stupňů, podle materiálu. Nejvíc přidává fleece.'),
         ('Jaká vložka na trek?', 'Hedvábná, protože je nejlehčí a nejmenší po sbalení.'),
         ('Mohu spacák skladovat v kompresním vaku?', 'Jen na cestě. Dlouhodobé stlačení poškozuje výplň, doma spacák skladujte volně.'),
         ('Jak velkou vložku vybrat?', 'Stejného tvaru jako spacák, mumie do mumie, dekový do dekového, a o něco delší než tělo.')],
)

# ------------------------------------------------------------------ rybarske-spacaky
NEW['rybarske-spacaky'] = dict(short=True,
    title='Rybářské spacáky a lehátka se spacákem | Sporteka',
    desc='Rybářské spacáky a lehátka se spacákem pro kapraře: 5 sezón, kamufláž, hřejivé a vodoodpudivé. Porovnejte ceny v českých obchodech a vyberte komplet.',
    intro='<p><strong>Rybářský spacák</strong> musí vydržet dlouhé noci u vody, vlhko a často i mráz. Proto bývá větší, hřejivější a z odolnějšího materiálu než turistický. Kapráři často kupují spacák společně s lehátkem jako <strong>sleep systém</strong>.</p>'
          '<p>Na Sportece porovnáte rybářské spacáky a lehátka se spacákem z českých obchodů. Obecné spacáky najdete v kategorii <a href="/spaci-pytle/">spací pytle</a>, rybářské stany v <a href="/rybarske-stany/">rybářských stanech</a>.</p>',
    guide='<h2>Jak vybrat rybářský spacák</h2>'
          '<p>Důležité jsou teplota použití, velikost a odolnost proti vlhku. Při dlouhém sezení u vody si každý stupeň navíc vyplatí a rozměr spacáku by měl odpovídat lehátku, na kterém spíte.</p>'
          '<h3>Sezóna a teplota</h3>'
          '<p>Rybářské spacáky se dělí podle sezón. Třísezónní stačí na jaro a podzim, čtyř a pětisezónní se hodí na zimní lov. Údaj o sezóně není normovaný, proto sledujte komfortní teplotu.</p>'
          '<h3>Lehátko se spacákem</h3>'
          '<p>Sleep systém spojuje lehátko a spacák, často s vodoodolným potahem a rámem s nastavitelnými nohami. Hodí se, když chcete mít spaní, sedačku a lehátko v jednom.</p>'
          '<h3>Velikost a kamufláž</h3>'
          '<p>Větší spacáky mají víc místa na oblečení uvnitř. Kamufláž se ocení u rybářů, kteří nechtějí vyrušovat ryby u břehu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("fox", "Fox"), ("delphin", "Delphin"), ("trakker-products", "Trakker"), ("giants-fishing", "Giants Fishing"), ("mikado", "Mikado"), ("prologic", "Prologic"))}.</p>',
    faq=[('Jaký spacák na rybaření?', 'Hřejivý, vodoodpudivý a dostatečně velký, s komfortní teplotou podle ročního období, ve kterém rybaříte.'),
         ('Co je sleep systém?', 'Lehátko se spacákem v jednom balení, často s vodoodolným potahem a nastavitelnými nohami.'),
         ('Stačí třísezónní spacák na podzimní lov?', 'Obvykle ano na jaro a podzim, na zimní lov volte čtyř nebo pětisezónní model.'),
         ('Na co dát pozor u rybářského spacáku?', 'Na komfortní teplotu, velikost a odolnost proti vlhku u vody.'),
         ('Hodí se rybářský spacák i na kemping?', 'Ano, ale bývá těžší a objemnější než turistický, takže se hodí hlavně do auta.')],
)
