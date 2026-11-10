"""sporteka.cz — texts of wave 1, part C: bikes and cycling (3. 11. 2026). Same rules as texty_vlna1a.py."""
from texty_vlna1a import T

NEW = {}

NEW['jizdni-kola'] = dict(
    title='Jízdní kola – porovnání cen v e-shopech | Sporteka',
    desc='Jízdní kola horská, silniční, gravel, trekingová, skládací i dětská. Porovnejte ceny a dostupnost v českých obchodech a vyberte správnou velikost rámu.',
    intro='<p><strong>Jízdní kola</strong> se dělí podle toho, kde na nich pojedete. <a href="/horska-kola/">Horská kola</a> zvládnou terén, <a href="/silnicni-kola/">silniční kola</a> jsou rychlá na asfaltu, <a href="/gravel-kola/">gravel kola</a> zvládnou i šotolinu, '
          '<a href="/trekingova-kola/">trekingová</a>, <a href="/krosova-kola/">krosová</a> a <a href="/mestska-kola/">městská kola</a> se hodí na výlety a do města, <a href="/damska-kola/">dámská kola</a> mají nízký nástup, <a href="/skladaci-kola/">skládací</a> do bytu a vlaku. Pro děti je tu kategorie <a href="/detska-kola/">dětská kola</a>.</p>'
          '<p>Na Sportece porovnáte ceny kol z českých obchodů a uvidíte, které modely jsou skladem. Výběr zúžíte podle značky, velikosti rámu, ceny nebo typu. Součástí přehledu jsou i '
          '<a href="/elektrokola/">elektrokola</a>. Správná velikost rámu je při koupi nejdůležitější, protože kolo s nevhodným rámem bolí záda i zápěstí.</p>',
    guide='<h2>Jak vybrat jízdní kolo</h2>'
          '<p>Nejdřív si ujasněte, kde budete jezdit nejčastěji. Kolo na všechno neexistuje, každý typ je kompromisem. Pokud budete střídat povrchy, vybírejte podle toho, kde strávíte nejvíc času.</p>'
          '<h3>Typy kol</h3>'
          '<ul><li><strong>Horské kolo (MTB):</strong> široké pláště, odpružená vidlice, nižší převody. Pro lesní cesty, kopce a terén.</li>'
          '<li><strong>Silniční kolo:</strong> úzké pláště, spodní řídítka (beranidlo) a lehký rám. Rychlé na asfaltu a dlouhých tratích.</li>'
          '<li><strong>Gravel:</strong> kombinace silničního a horského. Zvládne šotolinu i asfalt, vhodný na dlouhé výlety.</li>'
          '<li><strong>Trekingové a crossové kolo:</strong> pohodlná poloha, nosič a blatníky, na výlety a do práce.</li>'
          '<li><strong>Městské a skládací kolo:</strong> praktické na krátké vzdálenosti, skládací se vejde do auta nebo bytu.</li>'
          '<li><strong>BMX a dirt:</strong> malé pevné kolo na triky, viz <a href="/bmx-a-dirt-kola/">BMX a dirt kola</a>.</li></ul>'
          '<h3>Velikost rámu</h3>'
          '<p>Rám se vybírá podle výšky postavy a délky nohou. Orientační hodnoty pro horské kolo uvádí tabulka, silniční rámy se značí v centimetrech. Při váhání zkuste kolo v obchodě nebo si ověřte tabulku výrobce.</p>'
          + T(['Výška postavy', 'Horské kolo (rám)', 'Silniční kolo (rám)'], [['155–165 cm', 'S (15–16")', '50–52 cm'], ['165–175 cm', 'M (17–18")', '52–54 cm'], ['175–185 cm', 'L (19")', '56–58 cm'], ['185–195 cm', 'XL (20–21")', '58–60 cm']]) +
          '<p>Hodnoty jsou orientační, geometrie rámů se u značek liší.</p>'
          '<h3>Velikost kol a převody</h3>'
          '<p>Horská kola mají obvykle kola 27,5" nebo 29", menší rámy se často prodávají s menším kolem. Víc převodů zvládne kopce, počet převodů ale nerozhoduje o kvalitě. '
          'Důležitější je kvalita brzd: kotoučové hydraulické brzdy brzdí spolehlivě i v dešti, ráfkové jsou levnější a lehčí.</p>'
          '<h3>Odpružení</h3>'
          '<p>Pevné kolo (hardtail) má odpruženou jen vidlici, je lehčí a levnější. Celoodpružené kolo (full) je pohodlnější v náročném terénu, ale těžší a dražší na údržbu. Na silnici a výlety odpružení nepotřebujete.</p>'
          '<h3>Dětská kola</h3>'
          '<p>Dětské kolo se vybírá podle výšky dítěte a velikosti kol: 12" zhruba pro nejmenší, 16" pro předškoláky, 20" pro prvňáčky a 24" pro starší děti. Důležitá je lehkost a dosažitelné brzdy. '
          'Pro úplné začátečníky jsou vhodná <a href="/odrazedla/">odrážedla</a>.</p>'
          '<h3>Co k tomu</h3>'
          '<p>K novému kolu patří <a href="/cyklisticke-helmy/">helma</a> (do 18 let je povinná), <a href="/cyklo-zamky/">zámek</a>, <a href="/cyklo-svetla/">světla</a> a pumpa. '
          'Ceny kol se u stejného modelu mezi obchody liší, proto porovnávejte nabídky včetně dopravy a servisních podmínek.</p>',
    faq=[('Jak vybrat velikost jízdního kola?', 'Podle výšky postavy a délky nohou. Horské kolo se značí v palcích (S až XL), silniční v centimetrech. Při váhání si kolo vyzkoušejte nebo se řiďte tabulkou výrobce.'),
         ('Jaké kolo na asfalt a jaké do lesa?', 'Na asfalt silniční nebo trekingové kolo, do lesa horské. Pokud střídáte, vyberte gravel nebo crossové kolo.'),
         ('Jaké brzdy jsou lepší, kotoučové, nebo ráfkové?', 'Kotoučové hydraulické brzdí spolehlivěji, hlavně v dešti, ráfkové jsou lehčí a levnější. Pro rekreační jízdu stačí obojí.'),
         ('Hardtail, nebo celoodpružené kolo?', 'Hardtail je lehčí, levnější a jednodušší na údržbu, full je pohodlnější v těžkém terénu. Na většinu lesních cest stačí hardtail.'),
         ('Jaké kolo pro dítě?', 'Podle výšky dítěte: 12" pro nejmenší, 16" pro předškoláky, 20" pro prvňáčky a 24" pro starší. Důležitá je nízká hmotnost a brzdy, na které děti dosáhnou.'),
         ('Je helma na kole povinná?', 'Pro cyklisty do 18 let ano. Dospělým se doporučuje, protože výrazně snižuje riziko zranění hlavy.')],
)

NEW['elektrokola'] = dict(
    title='Elektrokola – porovnání cen a modelů | Sporteka',
    desc='Elektrokola horská, trekingová, městská, skládací i nákladní. Porovnejte ceny, dojezd a baterie v českých obchodech a vyberte správný motor.',
    intro='<p><strong>Elektrokolo</strong> pomáhá při šlapání motorem a baterií, takže zvládnete delší trasy a kopce s menší námahou. Mají podobnou konstrukci jako běžná kola, a proto se dělí podobně: '
          '<a href="/horska-elektrokola/">horská elektrokola</a>, <a href="/mestska-elektrokola/">městská</a>, <a href="/trekingova-elektrokola/">trekingová</a>, <a href="/fatbike-elektrokola/">fatbike</a>, <a href="/skladaci-elektrokola/">skládací</a>, <a href="/damska-elektrokola/">dámská</a> a <a href="/nakladni-elektrokola/">nákladní</a>.</p>'
          '<p>Na Sportece porovnáte ceny elektrokol z českých obchodů. Vybírat můžete podle značky, typu a ceny a uvidíte, které modely jsou skladem. Důležité parametry jsou umístění motoru, kapacita baterie a dojezd, '
          'které vysvětlujeme v průvodci níže.</p>',
    guide='<h2>Jak vybrat elektrokolo</h2>'
          '<p>Elektrokolo vybíráte jako běžné kolo, jen s dalšími parametry: motor, baterie, displej a hmotnost. Nejprve rozhodněte, kde a jak daleko budete jezdit.</p>'
          '<h3>Typ elektrokola</h3>'
          '<ul><li><strong>Horské:</strong> odpružené, s širokými plášti a výkonným středovým motorem. Pro terén a kopce.</li>'
          '<li><strong>Trekingové a crossové:</strong> pohodlné, s nosičem a blatníky, na dlouhé výlety.</li>'
          '<li><strong>Městské:</strong> nižší nástup, praktické vybavení, na dojíždění.</li>'
          '<li><strong>Skládací:</strong> menší kola, vejdou se do auta nebo vlaku.</li>'
          '<li><strong>Nákladní:</strong> pro přepravu dětí a nákupu.</li></ul>'
          '<h3>Motor</h3>'
          '<p>Středový motor (u pedálů) dává přirozenější jízdu, lepší rozložení váhy a stoupání do kopce. Zadní motor je jednodušší a levnější, přední hůř přenáší trakci. '
          'Podle zákona u nás platí, že elektrokolo s pomocným motorem do 250 W, který pomáhá jen při šlapání a vypíná se při 25 km/h, je považováno za jízdní kolo. Nepotřebuje řidičák, registraci ani pojištění.</p>'
          '<h3>Baterie a dojezd</h3>'
          '<p>Kapacita se udává ve watthodinách (Wh). Běžné baterie mají zhruba 400 až 750 Wh. Dojezd závisí na zátěži, terénu, větru a zvolené úrovni asistence, proto výrobce uvádí rozpětí, ne jedno číslo. '
          'Většina elektrokol se nabíjí několik hodin ze zásuvky. Baterii skladujte v suchu a při pokojové teplotě, mráz zkracuje dojezd.</p>'
          + T(['Využití', 'Doporučená baterie'], [['Krátké dojíždění do práce', 'kolem 400 Wh'], ['Víkendové výlety', '500–625 Wh'], ['Dlouhé trasy a hory', '625 Wh a víc, případně druhá baterie']]) +
          '<p>Hodnoty jsou orientační.</p>'
          '<h3>Velikost rámu a hmotnost</h3>'
          '<p>Velikost rámu se určuje podle výšky postavy podobně jako u běžného kola. Elektrokola jsou těžší (obvykle 20 až 28 kg), takže si ověřte, zda ho zvládnete zvednout na nosič nebo do sklepa. '
          'Přečtěte si i nosnost, hlavně pokud kolo využijete s dítětem.</p>'
          '<h3>Servis a záruka</h3>'
          '<p>U elektrokola záleží na dostupnosti servisu motoru. Vybírejte značku, která má v ČR servisní síť a dobu záruky na baterii. Nezapomeňte na bezpečnost: helma, světla a zámek jsou nutnost.</p>',
    faq=[('Jak vybrat elektrokolo?', 'Podle typu jízdy: horské do terénu, trekingové na výlety, městské na dojíždění. Pak sledujte motor (nejlépe středový), kapacitu baterie, hmotnost a servis.'),
         ('Kolik váží elektrokolo?', 'Obvykle 20 až 28 kg podle typu a baterie. Skládací a lehčí modely mohou být lehčí, horská celoodpružená těžší.'),
         ('Jak dlouho se elektrokolo nabíjí?', 'Většinou několik hodin ze zásuvky, podle kapacity baterie a výkonu nabíječky. Přesný údaj najdete v popisu modelu.'),
         ('Potřebuji na elektrokolo řidičský průkaz nebo pojištění?', 'Pokud má motor do 250 W a pomáhá jen při šlapání do 25 km/h, považuje se za jízdní kolo, takže registrace, pojištění ani řidičák nejsou potřeba. U výkonnějších modelů to neplatí.'),
         ('Jaký dojezd má elektrokolo?', 'Podle baterie, terénu a zátěže se pohybuje v desítkách až stovkách kilometrů. Výrobce uvádí rozmezí, protože záleží na úrovni asistence.'),
         ('Jaký motor je lepší, středový, nebo zadní?', 'Středový motor dává přirozenější jízdu a lepší výkon do kopce, zadní je jednodušší a levnější. Pro terén a kopce je lepší středový.')],
)

NEW['cyklistika'] = dict(
    title='Cyklistika – kola, helmy, oblečení a doplňky | Sporteka',
    desc='Vše pro cyklistiku na jednom místě: jízdní kola, elektrokola, helmy, oblečení, světla, zámky a servis. Porovnejte ceny v českých obchodech.',
    intro='<p><strong>Cyklistika</strong> začíná kolem, ale bezpečná a pohodlná jízda stojí na dalších věcech: <a href="/cyklisticke-helmy/">helma</a>, <a href="/cyklisticke-obleceni/">oblečení</a>, <a href="/cyklo-svetla/">světla</a> a <a href="/cyklo-zamky/">zámek</a>. '
          'Vybírat můžete mezi <a href="/jizdni-kola/">jízdními koly</a>, <a href="/elektrokola/">elektrokoly</a> a díly pro opravy a údržbu.</p>'
          '<p>Na Sportece porovnáte ceny z českých cyklistických a sportovních obchodů a uvidíte, které velikosti a modely jsou skladem. Vybírat můžete podle značky a ceny. '
          'Hledáte-li něco konkrétního, použijte <a href="/cyklo-dily/">cyklo díly</a>, <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> nebo <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>.</p>',
    guide='<h2>Jak si vybavit na cyklistiku</h2>'
          '<p>Základem je kolo, ale k němu patří vybavení, které chrání, zvyšuje komfort a umožní opravy na cestě. Pořadí podle důležitosti se mírně liší podle toho, zda jezdíte po městě, silnici nebo terénu.</p>'
          '<h3>Bezpečnost na prvním místě</h3>'
          '<ul><li><strong>Helma:</strong> nosí se na každé jízdě, do 18 let je povinná. Musí sedět pevně a nemá se kývat, viz <a href="/cyklisticke-helmy/">cyklistické helmy</a>.</li>'
          '<li><strong>Světla:</strong> přední bílé a zadní červené jsou povinné za snížené viditelnosti. LED světla se dobíjejí přes USB, viz <a href="/cyklo-svetla/">světla na kolo</a>.</li>'
          '<li><strong>Reflexní prvky:</strong> odrazky a reflexní vesty zvyšují viditelnost.</li>'
          '<li><strong>Zámek:</strong> pevný U-zámek nebo řetěz je nutný ve městě, viz <a href="/cyklo-zamky/">cyklo zámky</a>.</li></ul>'
          '<h3>Oblečení</h3>'
          '<p>Cyklistické kalhoty s vložkou chrání při delších jízdách, dres odvádí pot a má kapsy na zádech. V chladu se hodí návleky na ruce a nohy a bunda proti větru. '
          'Kompletní přehled najdete v <a href="/cyklisticke-obleceni/">cyklistickém oblečení</a>, boty s tuhou podrážkou v <a href="/cyklisticka-obuv/">cyklistické obuvi</a>.</p>'
          '<h3>Opravy a údržba</h3>'
          '<p>Na výlet patří pumpa, náhradní duše, montpáky a multiklíč. Doma se hodí mazání řetězu a čištění, viz <a href="/cyklo-udrzba/">cyklo údržba</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. '
          'Pravidelná kontrola brzd, řetězu a tlaku v pláštích snižuje poruchy.</p>'
          '<h3>Přeprava</h3>'
          '<p>Pro převoz kola na autě slouží <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>. Na zavazadla a nákupy se hodí <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a> a pro děti <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>.</p>'
          '<h3>Sledování a navigace</h3>'
          '<p><a href="/cyklo-computery/">Cyklopočítače</a> zobrazují rychlost, vzdálenost a trasu, některé se spojují s telefonem a hodinkami. Pro začátek stačí jednoduchý model.</p>'
          + T(['Typ jízdy', 'Základní vybavení'], [['Město', 'helma, zámek, světla, blatníky, nosič'], ['Silnice', 'helma, dres a kalhoty s vložkou, pumpa, náhradní duše'], ['Terén', 'helma, rukavice, chrániče, nářadí'], ['Rodina s dětmi', 'dětská helma, sedačka nebo vozík, reflexní prvky']]) +
          '<h3>Jak využít porovnání cen</h3>'
          '<p>Ceny cyklistického vybavení se mezi obchody liší, často o desítky procent. Sledujte i dopravu a možnost vrácení, protože u helem a oblečení se vyplatí zkoušet doma.</p>',
    faq=[('Co potřebuji na kole kromě kola?', 'Helmu, světla (přední bílé a zadní červené), zámek, pumpu a náhradní duši. Podle délky jízdy i vhodné oblečení a vodu.'),
         ('Je helma na kole povinná?', 'Pro cyklisty do 18 let ano. Dospělým se doporučuje na každé jízdě.'),
         ('Jaká světla na kolo jsou povinná?', 'Za snížené viditelnosti přední bílé a zadní červené světlo, případně odrazky. Moderní LED světla se nabíjí přes USB.'),
         ('Jak vybrat cyklistické oblečení?', 'Podle sezóny a délky jízd. Na delší trasy kalhoty s vložkou, v chladu bunda proti větru a návleky. Na kratší jízdy stačí běžné sportovní oblečení.'),
         ('Co mít s sebou na delší výlet?', 'Pumpu, náhradní duši, montpáky, multiklíč, vodu a telefon. Pro jistotu i lehkou bundu a základní lékárničku.'),
         ('Jak přepravit kolo autem?', 'Nosičem na tažné zařízení, na střechu nebo na zadní dveře, případně po složení menších kol do kufru. Nosič vybírejte podle počtu kol a typu auta.')],
)
