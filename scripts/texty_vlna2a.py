"""sporteka.cz — texts of the new bike-type categories (3. 11. 2026): gravel, road, full-suspension, city, cross, women's, tricycles
and the e-bike types. Shorter than the wave-1 texts (entries carry short=True: intro ≥ 70 words, guide ≥ 280). Same rules as texty_vlna1a.py."""
from texty_vlna1a import T

NEW = {}

NEW['gravel-kola'] = dict(short=True,
    title='Gravel kola – porovnání cen a modelů | Sporteka',
    desc='Gravel kola na asfalt, šotolinu i lesní cesty. Porovnejte ceny a dostupnost modelů v českých obchodech a vyberte velikost rámu a šířku plášťů.',
    intro='<p><strong>Gravel kola</strong> jsou něco mezi silničním a horským kolem. Mají beranidlové řídítko jako silničky, ale širší pláště, kotoučové brzdy a pohodlnější geometrii, takže zvládnou asfalt, '
          'šotolinu i polňačky. Hodí se na dlouhé výlety, dojíždění i vícedenní cestování s brašnami. Pokud jezdíte jen po silnici, stačí <a href="/silnicni-kola/">silniční kolo</a>, na terén s kořeny <a href="/horska-kola/">horské</a>.</p>'
          '<p>Na Sportece porovnáte ceny gravelů z českých obchodů a uvidíte, které velikosti jsou skladem.</p>',
    guide='<h2>Jak vybrat gravel</h2>'
          '<p>Nejdřív si ujasněte, kde budete jezdit. Čím víc šotoliny a terénu, tím širší pláště a nižší převody se vyplatí. Čím víc asfaltu, tím lehčí a rychlejší bude kolo.</p>'
          '<h3>Pláště a převody</h3>'
          '<p>Gravelové pláště bývají zhruba 35 až 50 mm široké. Užší jsou rychlejší na asfaltu, širší pohodlnější a lépe drží na šotolině. Převody se dělají buď s jedním předním převodníkem (1x), '
          'který je jednodušší a odolnější, nebo se dvěma (2x), který nabízí jemnější odstupňování pro delší tratě.</p>'
          '<h3>Materiál rámu</h3>'
          '<ul><li><strong>Hliník:</strong> nejdostupnější, pevný, trochu tvrdší jízda.</li>'
          '<li><strong>Karbon:</strong> lehčí a tlumí vibrace, ale je dražší a citlivější na nárazy.</li>'
          '<li><strong>Ocel a titan:</strong> pružné a odolné, vyšší hmotnost a cena.</li></ul>'
          '<h3>Velikost rámu</h3>'
          + T(['Výška postavy', 'Orientační velikost rámu'], [['165–170 cm', '52 cm'], ['170–175 cm', '54 cm'], ['175–180 cm', '56 cm'], ['180–185 cm', '58 cm']]) +
          '<p>Hodnoty jsou orientační, geometrie se u značek liší. Při váhání si kolo vyzkoušejte nebo se řiďte tabulkou výrobce.</p>'
          '<h3>Výbava pro delší výlety</h3>'
          '<p>Na vícedenní cesty hledejte závity pro nosiče a blatníky a upevnění na brašny. Hodí se <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>, světla a <a href="/cyklo-zamky/">zámek</a>, pumpa a náhradní duše.</p>',
    faq=[('Jaký je rozdíl mezi gravelem a silničním kolem?', 'Gravel má širší pláště, pohodlnější geometrii a kotoučové brzdy, takže zvládne šotolinu a polňačky. Silniční kolo je lehčí a rychlejší na asfaltu.'),
         ('Hodí se gravel do města?', 'Ano, je pohodlný a zvládne dlouhé trasy i nerovnosti. Pokud potřebujete blatníky a nosič, hledejte model se závity.'),
         ('Jak široké pláště na gravel?', 'Obvykle 35 až 50 mm. Užší na rychlý asfalt, širší na šotolinu a terén.'),
         ('Jaká velikost rámu gravelu je správná?', 'Podle výšky postavy a délky nohou, přibližně jako u silničního kola. Při váhání se řiďte tabulkou výrobce.'),
         ('Je gravel vhodný na vícedenní cestování?', 'Ano, mnoho modelů má upevnění na brašny a nosiče. Počítejte s hmotností zavazadel a zvolte pevnější pláště.')],
)

NEW['silnicni-kola'] = dict(short=True,
    title='Silniční kola – porovnání cen a modelů | Sporteka',
    desc='Silniční kola pro rychlou jízdu po asfaltu: endurance, aero i horské stoupáky. Porovnejte ceny a dostupnost v českých obchodech a vyberte velikost rámu.',
    intro='<p><strong>Silniční kola</strong> jsou stavěná na rychlost a dlouhé tratě po asfaltu. Mají úzké pláště, beranidlové řídítko a lehký rám. Rozdíly jsou v geometrii: endurance modely jsou pohodlnější na celodenní jízdu, '
          'aero modely rychlejší na rovině a lehké stoupací modely se hodí do kopců. Pro smíšený terén vyberte <a href="/gravel-kola/">gravel</a>.</p>'
          '<p>Na Sportece porovnáte ceny silničních kol z českých obchodů a uvidíte, které velikosti jsou skladem.</p>',
    guide='<h2>Jak vybrat silniční kolo</h2>'
          '<p>Rozhodněte, jak dlouho a jak rychle budete jezdit. Pro začátečníky a dlouhé výlety je lepší pohodlnější endurance geometrie, pro závody a rychlé skupinové jízdy agresivnější.</p>'
          '<h3>Typy silničních kol</h3>'
          '<ul><li><strong>Endurance:</strong> vzpřímenější poloha, pohodlí na celodenní trasy.</li>'
          '<li><strong>Aero:</strong> aerodynamický rám, rychlost na rovině a v klesání.</li>'
          '<li><strong>Lehké stoupací:</strong> nízká hmotnost, hodí se do kopců.</li></ul>'
          '<h3>Převody a komponenty</h3>'
          '<p>Skupiny Shimano se řadí od základních (Claris, Sora) přes Tiagra, 105 a Ultegra až po Dura-Ace, u SRAM jsou to Apex, Rival, Force a Red. Vyšší skupiny jsou lehčí a přesnější, '
          'ale pro rekreační jízdu stačí střední. Elektronické řazení (Di2, AXS) je pohodlné a přesné, ale dražší.</p>'
          '<h3>Rám a velikost</h3>'
          '<p>Hliníkový rám je dostupný, karbonový lehčí a tlumí vibrace. Velikost se udává v centimetrech podle výšky postavy.</p>'
          + T(['Výška postavy', 'Orientační velikost rámu'], [['165–170 cm', '52 cm'], ['170–175 cm', '54 cm'], ['175–180 cm', '56 cm'], ['180–185 cm', '58 cm']]) +
          '<p>Hodnoty jsou orientační, geometrie se u značek liší.</p>'
          '<h3>Pláště a brzdy</h3>'
          '<p>Dnes se běžně montují pláště 28 až 32 mm, které jsou pohodlnější a mají nižší valivý odpor, než dřívější úzké. Kotoučové brzdy brzdí spolehlivě i v dešti a nahradily ráfkové.</p>',
    faq=[('Jaké silniční kolo pro začátečníka?', 'Endurance model s hliníkovým rámem a kotoučovými brzdami. Je pohodlný a cenově dostupný, vyšší skupiny nejsou nutné.'),
         ('Jak vybrat velikost rámu silničního kola?', 'Podle výšky postavy a délky nohou. Velikost se udává v centimetrech, například 54 nebo 56 cm. Při váhání se řiďte tabulkou výrobce.'),
         ('Je lepší karbon, nebo hliník?', 'Karbon je lehčí a tlumí vibrace, hliník je levnější a odolnější. Pro rekreační jízdu stačí hliník.'),
         ('Co znamenají skupiny Tiagra, 105 a Ultegra?', 'Jsou to úrovně komponentů Shimano. Čím vyšší, tím lehčí a přesnější. Pro většinu rekreačních jezdců postačí 105 nebo Tiagra.'),
         ('Jak široké pláště na silniční kolo?', 'Dnes běžně 28 až 32 mm. Širší jsou pohodlnější a mají nižší odpor, užší jsou o něco lehčí.')],
)

NEW['celoodpruzena-horska-kola'] = dict(short=True,
    title='Celoodpružená horská kola – porovnání cen | Sporteka',
    desc='Celoodpružená horská kola (full) pro trail, enduro a náročný terén. Porovnejte ceny a modely v českých obchodech a vyberte zdvih a velikost rámu.',
    intro='<p><strong>Celoodpružená horská kola</strong> mají odpružení vpředu i vzadu. Lépe drží stopu na kořenech a kamenech, tlumí nárazy a jsou pohodlnější v dlouhých sjezdech. Za to jsou těžší, dražší a vyžadují víc údržby než pevná kola (hardtail). '
          'Pokud jezdíte spíš po lesních cestách, stačí <a href="/horska-kola/">horské kolo</a> s odpruženou vidlicí.</p>'
          '<p>Na Sportece porovnáte ceny celoodpružených kol z českých obchodů a uvidíte, které velikosti jsou skladem.</p>',
    guide='<h2>Jak vybrat celoodpružené kolo</h2>'
          '<p>Rozhoduje zdvih, tedy jak hluboko odpružení pracuje. Větší zdvih zvládne drsnější terén, ale kolo je těžší a pomalejší do kopce.</p>'
          + T(['Využití', 'Zdvih'], [['Cross-country (XC), maratony', 'zhruba 100–120 mm'], ['Trail, univerzální jízda', 'zhruba 130–150 mm'], ['Enduro, bikeparky', 'zhruba 160 mm a víc']]) +
          '<h3>Rám a kola</h3>'
          '<p>Hliníkový rám je dostupnější, karbonový lehčí. Kola jsou nejčastěji 29", menší rámy se dělají i s 27,5". Velikost rámu se určuje podle výšky postavy, u horských kol obvykle S až XL.</p>'
          '<h3>Brzdy a vidlice</h3>'
          '<p>Hydraulické kotoučové brzdy jsou standard. Vidlice a tlumič mají nastavitelné tlaky podle váhy jezdce, bez správného nastavení kolo neodpruží, jak má. Nastavení vám v obchodě ukáží.</p>'
          '<h3>Údržba</h3>'
          '<p>Odpružení vyžaduje pravidelný servis, obvykle po určitém počtu hodin jízdy. Ložiska zadní stavby a tlumič trpí blátem a prachem, proto kolo po jízdě umývejte a mažte.</p>',
    faq=[('Je celoodpružené kolo lepší než hardtail?', 'Pohodlnější a stabilnější v náročném terénu, ale těžší, dražší a vyžaduje víc údržby. Pro lesní cesty často stačí hardtail.'),
         ('Jaký zdvih potřebuji?', 'Na cross-country 100 až 120 mm, na trail 130 až 150 mm, na enduro 160 mm a víc.'),
         ('Jak velké kolo 29", nebo 27,5"?', 'Větší kola lépe překonávají překážky, menší jsou hravější. Menší rámy jsou často s 27,5" koly.'),
         ('Jak často servisovat odpružení?', 'Podle návodu výrobce, obvykle jednou za rok nebo po stanoveném počtu hodin jízdy. Častěji při jízdě v blátě.'),
         ('Hodí se celoodpružené kolo na silnici?', 'Ne, je těžší a odpružení ztrácí energii. Na silnici je lepší silniční kolo nebo gravel.')],
)

NEW['mestska-kola'] = dict(short=True,
    title='Městská kola – porovnání cen a modelů | Sporteka',
    desc='Městská kola pro každodenní dojíždění: s nízkým rámem, blatníky a nosičem. Porovnejte ceny a dostupnost v českých obchodech a vyberte velikost.',
    intro='<p><strong>Městská kola</strong> jsou praktická na každodenní dojíždění, nákupy a krátké výlety. Mívají vzpřímenou polohu, blatníky, nosič a světla a převody, které se dají řadit i na místě. '
          'Velmi pohodlné jsou modely s nízkým nástupem. Na delší výlety se hodí spíš <a href="/trekingova-kola/">trekingová kola</a>, pro ženy máme zvlášť <a href="/damska-kola/">dámská kola</a>.</p>'
          '<p>Na Sportece porovnáte ceny městských kol z českých obchodů a uvidíte, které velikosti jsou skladem.</p>',
    guide='<h2>Jak vybrat městské kolo</h2>'
          '<p>Městské kolo vybírejte podle toho, jak daleko budete jezdit, kolik věcí vozíte a jestli máte kolo kde uložit. Důležitější než lehký rám je pohodlí a výbava.</p>'
          '<h3>Rám a poloha</h3>'
          '<p>Nízký rám bez horní trubky usnadňuje nasedání, hodí se do sukně i s nákupem. Pevnější klasický rám je tužší. Vzpřímená poloha šetří záda a dává přehled v provozu.</p>'
          '<h3>Převody</h3>'
          '<ul><li><strong>Přehazovačka:</strong> běžný systém, lehčí a levnější, vyžaduje občasné seřízení.</li>'
          '<li><strong>Nábojová převodovka (3 až 8 rychlostí):</strong> chráněná v náboji, řadí se i při stání, nenáročná na údržbu.</li>'
          '<li><strong>Jedna rychlost:</strong> nejjednodušší, vhodná na rovinu.</li></ul>'
          '<h3>Výbava</h3>'
          '<p>Blatníky chrání oblečení, nosič a koš slouží na nákupy a řetězový kryt na kalhoty. Světla jsou povinná za tmy, dynamo nebo dobíjecí LED. Pevný <a href="/cyklo-zamky/">zámek</a> je ve městě nutnost.</p>'
          '<h3>Velikost</h3>'
          '<p>Rám se vybírá podle výšky postavy a délky nohou. U městských kol se velikost udává v palcích nebo písmeny. Při sedání na sedlo se má špička nohy mírně dotýkat země.</p>',
    faq=[('Jaké kolo do města?', 'Městské nebo trekingové kolo s vzpřímenou polohou, blatníky, nosičem a světly. Pohodlí je důležitější než nízká hmotnost.'),
         ('Jaké převody do města?', 'Nábojová převodovka je nenáročná na údržbu a řadí se i na místě, přehazovačka je lehčí a levnější.'),
         ('Jaká velikost rámu městského kola?', 'Podle výšky postavy a délky nohou. Při sezení na sedle se má špička nohy mírně dotýkat země.'),
         ('Potřebuji ve městě světla?', 'Ano, za snížené viditelnosti jsou povinná přední bílé a zadní červené světlo, případně odrazky.'),
         ('Jak zabezpečit kolo proti krádeži?', 'Pevným U-zámkem nebo řetězem, připoutáním rámu a kola k pevnému bodu. Lanka a tenké zámky se dají rychle přeříznout.')],
)

NEW['krosova-kola'] = dict(short=True,
    title='Krosová kola – porovnání cen a modelů | Sporteka',
    desc='Krosová (crossová) kola na asfalt, cyklostezky i lehký terén. Porovnejte ceny a dostupnost modelů v českých obchodech a vyberte velikost rámu.',
    intro='<p><strong>Krosová kola</strong> (crossová, fitness) jsou univerzální: rovné řídítko jako horské kolo, kola 28" a užší pláště jako silničky. Zvládnou asfalt, cyklostezky i zpevněné lesní cesty a jsou svižnější než trekingová kola. '
          'Na dlouhé výlety s bagáží vyberte raději <a href="/trekingova-kola/">trekingová kola</a>, na terén <a href="/horska-kola/">horská</a>.</p>'
          '<p>Na Sportece porovnáte ceny krosových kol z českých obchodů a uvidíte, které velikosti jsou skladem.</p>',
    guide='<h2>Jak vybrat krosové kolo</h2>'
          '<p>Krosové kolo je kompromis. Hodí se, když jezdíte po silnicích a cyklostezkách a občas i po šotolině, a nechcete se sklánět jako na silničce.</p>'
          '<h3>Pláště a kola</h3>'
          '<p>Nejčastěji 28" kola a pláště široké zhruba 32 až 45 mm. Čím užší plášť, tím rychlejší jízda po asfaltu, čím širší, tím víc pohodlí na šotolině. Odpružená vidlice se hodí na nerovné cesty, pevná vidlice je lehčí.</p>'
          '<h3>Převody a brzdy</h3>'
          '<p>Většina krosových kol má 8 až 27 rychlostí, hydraulické kotoučové brzdy jsou spolehlivější než ráfkové, hlavně v dešti.</p>'
          '<h3>Velikost rámu</h3>'
          + T(['Výška postavy', 'Orientační velikost rámu'], [['160–170 cm', '17" (S)'], ['170–180 cm', '19" (M)'], ['180–190 cm', '21" (L)'], ['190 cm a víc', '23" (XL)']]) +
          '<p>Hodnoty jsou orientační, u značek se liší.</p>'
          '<h3>Výbava</h3>'
          '<p>Na dojíždění doplňte blatníky, nosič a světla. Pro delší trasy se vyplatí pohodlnější sedlo a rukojeti.</p>',
    faq=[('Čím se liší krosové kolo od trekingového?', 'Krosové je lehčí a svižnější, trekingové mívá nosič, blatníky a světla od výrobce a je určeno na delší výlety.'),
         ('Hodí se krosové kolo do terénu?', 'Na zpevněné cesty a lehký terén ano. Na kořeny a kameny je lepší horské kolo.'),
         ('Jaké pláště na krosové kolo?', 'Obvykle 32 až 45 mm. Užší jsou rychlejší na asfaltu, širší pohodlnější na šotolině.'),
         ('Jak vybrat velikost krosového kola?', 'Podle výšky postavy a délky nohou, rámy jsou v palcích. Při váhání se řiďte tabulkou výrobce.'),
         ('Mohu na krosové kolo namontovat nosič?', 'Většina modelů má závity na nosič a blatníky. Ověřte to v popisu konkrétního modelu.')],
)

NEW['damska-kola'] = dict(short=True,
    title='Dámská kola – porovnání cen a modelů | Sporteka',
    desc='Dámská kola s nízkým rámem: městská, trekingová a krosová. Porovnejte ceny a dostupnost v českých obchodech a vyberte správnou velikost.',
    intro='<p><strong>Dámská kola</strong> mají nižší nástup a často i kratší rám, takže se na ně snadno nasedá i v sukni nebo šatech. Najdete mezi nimi městská, trekingová i krosová kola. '
          'Mnoho modelů je ale unisex a sedí ženám stejně dobře jako mužům, proto se vyplatí zkoušet i <a href="/mestska-kola/">městská kola</a> bez označení.</p>'
          '<p>Na Sportece porovnáte ceny dámských kol z českých obchodů a uvidíte, které velikosti jsou skladem.</p>',
    guide='<h2>Jak vybrat dámské kolo</h2>'
          '<p>Dámský rám je nižší a hodí se, pokud chcete pohodlné nasedání. Pokud vám nevadí vyšší rám, můžete vybírat i z unisex nebo pánských modelů, hlavně při sportovní jízdě.</p>'
          '<h3>Rám</h3>'
          '<p>Nízký průlez usnadní nasedání. Nižší rám bývá o něco méně tuhý, což ocení hlavně pohodlná jízda po městě. Pro sportovnější jízdu nebo těžší náklad zvolte pevnější rám.</p>'
          '<h3>Sedlo a řídítka</h3>'
          '<p>Dámská sedla bývají širší v zadní části. Vzpřímená poloha a zvednutá řídítka šetří záda. Správně nastavená výška sedla znamená, že při dolní poloze pedálu máte mírně pokrčené koleno.</p>'
          '<h3>Velikost</h3>'
          '<p>Rám vybírejte podle výšky postavy a vnitřní délky nohy. Při sezení na sedle se má špička nohy dotýkat země. Pokud jste mezi velikostmi, vyberte menší a upravte sedlo.</p>'
          '<h3>Výbava</h3>'
          '<p>Praktické jsou blatníky, kryt řetězu, nosič a košík, hlavně ve městě. Nezapomeňte na <a href="/cyklisticke-helmy/">helmu</a>, světla a zámek.</p>'
          '<h3>Typy dámských kol</h3>'
          '<ul><li><strong>Městská:</strong> vzpřímená poloha, nízký nástup, blatníky a nosič na každodenní jízdy.</li>'
          '<li><strong>Trekingová:</strong> pohodlná i na delší trasy, často s odpruženou vidlicí a více rychlostmi.</li>'
          '<li><strong>Krosová:</strong> svižnější, rovné řídítko, na silnici i zpevněné cesty.</li></ul>'
          '<p>Pokud chcete jezdit s motorem, podívejte se na <a href="/damska-elektrokola/">dámská elektrokola</a>.</p>',
    faq=[('Čím se liší dámské kolo od pánského?', 'Hlavně nižším rámem bez horní trubky, často širším sedlem a kratším dosahem k řídítkům. Rozdíl nemusí být výrazný a mnoho modelů je unisex.'),
         ('Jak vybrat velikost dámského kola?', 'Podle výšky postavy a vnitřní délky nohy. Při sezení na sedle se má špička nohy dotýkat země.'),
         ('Jaké dámské kolo do města?', 'Městské kolo s nízkým rámem, blatníky, nosičem a světly. Důležité je pohodlí a snadné nasedání.'),
         ('Mohu jezdit na pánském nebo unisex kole?', 'Ano, pokud vám sedí velikost a poloha. Rozhoduje geometrie, ne označení.'),
         ('Kde sehnat dámská elektrokola?', 'V sekci dámská elektrokola najdete modely s nízkým nástupem a motorem pro pohodlnou jízdu.')],
)

NEW['detske-trikolky'] = dict(short=True,
    title='Dětské tříkolky – porovnání cen a modelů | Sporteka',
    desc='Dětské tříkolky s vodící tyčí, multifunkční 5v1 i s ochrannou stříškou. Porovnejte ceny a dostupnost v českých obchodech a vyberte podle věku dítěte.',
    intro='<p><strong>Dětské tříkolky</strong> učí děti pedálovat a držet rovnováhu, než přejdou na <a href="/odrazedla/">odrážedlo</a> nebo kolo. Najdete klasické tříkolky, modely s vodící tyčí pro rodiče a multifunkční verze, '
          'které se s dítětem mění od kočárku po samostatnou tříkolku. Většina je určená zhruba pro věk od 1 do 4 let.</p>'
          '<p>Na Sportece porovnáte ceny tříkolek z českých obchodů a uvidíte, které modely jsou skladem. Pro větší děti se podívejte na <a href="/detska-kola/">dětská kola</a>.</p>',
    guide='<h2>Jak vybrat dětskou tříkolku</h2>'
          '<p>Při výběru sledujte věk a velikost dítěte, způsob ovládání a bezpečnostní prvky. Tříkolka má být stabilní, lehká a mít pohodlné sedátko.</p>'
          '<h3>Vodící tyč, nebo samostatná</h3>'
          '<ul><li><strong>S vodící tyčí:</strong> rodič tříkolku tlačí a řídí, dítě se učí šlapat. Vhodná od jednoho roku.</li>'
          '<li><strong>Samostatná:</strong> pro děti, které už samy sedí a zvládnou šlapat, zhruba od dvou let.</li>'
          '<li><strong>Multifunkční (3v1, 5v1):</strong> mění se z kočárku na tříkolku, rostou s dítětem.</li></ul>'
          '<h3>Bezpečnost</h3>'
          '<p>Důležité jsou pásy nebo bezpečnostní tyč, která drží dítě, stabilní konstrukce proti překlopení a brzdy nebo volnoběh. U tříkolek se stříškou sledujte průchodnost vzduchu a UV ochranu. '
          'Při koupi hledejte označení shody (CE) a splnění norem pro dětské hračky.</p>'
          '<h3>Materiál a kola</h3>'
          '<p>Kovový rám je pevnější, plastový lehčí. Pěnová nebo gumová kola jsou tichá a nepropíchnou se, nafukovací pohodlnější na nerovném povrchu.</p>'
          '<h3>Kdy přejít na kolo</h3>'
          '<p>Když dítě zvládne šlapat a udržet rovnováhu, obvykle ve třech až čtyřech letech, můžete zkusit <a href="/detska-kola-12-14-palcu/">kolo s 12" nebo 14" koly</a> s pomocnými kolečky nebo bez nich.</p>',
    faq=[('Od kolika let může dítě jezdit na tříkolce?', 'Tříkolky s vodící tyčí se používají od zhruba jednoho roku, samostatné od dvou let. Řiďte se údajem výrobce.'),
         ('Jaká tříkolka je nejlepší?', 'Záleží na věku dítěte. Mladším dětem sedí model s vodící tyčí a pásem, starším samostatná lehká tříkolka s brzdou.'),
         ('Co je tříkolka 5v1?', 'Multifunkční tříkolka, která se mění z kočárku na tříkolku s vodící tyčí a nakonec na samostatnou. Roste s dítětem.'),
         ('Kdy přejít z tříkolky na kolo?', 'Když dítě zvládne šlapat a udržet rovnováhu, často ve třech až čtyřech letech. Začít se dá s pomocnými kolečky nebo odrážedlem.'),
         ('Na co dát pozor u bezpečnosti?', 'Na stabilní konstrukci, bezpečnostní pás nebo tyč, brzdu a označení shody CE. Nepoužívejte tříkolku poblíž silnice.')],
)

NEW['mestska-elektrokola'] = dict(short=True,
    title='Městská elektrokola – porovnání cen a modelů | Sporteka',
    desc='Městská elektrokola na dojíždění a každodenní jízdu: s nízkým rámem, blatníky a nosičem. Porovnejte ceny a baterie v českých obchodech.',
    intro='<p><strong>Městská elektrokola</strong> usnadňují dojíždění do práce a nákupy: motor pomáhá při rozjezdu a do kopce, takže přijedete bez zpocení. Mívají vzpřímenou polohu, blatníky, nosič a světla, často i nízký nástup. '
          'Na delší výlety se hodí spíš <a href="/trekingova-elektrokola/">trekingová elektrokola</a>, do terénu <a href="/horska-elektrokola/">horská</a>.</p>'
          '<p>Na Sportece porovnáte ceny městských elektrokol z českých obchodů a uvidíte, které modely jsou skladem.</p>',
    guide='<h2>Jak vybrat městské elektrokolo</h2>'
          '<p>Při výběru sledujte motor, baterii, hmotnost a výbavu. Pro denní dojíždění je důležitý dojezd a snadné nabíjení.</p>'
          '<h3>Motor</h3>'
          '<p>Středový motor (u pedálů) dává přirozenou jízdu a dobře rozkládá váhu, motor v zadním kole je jednodušší a levnější. Podle zákona je elektrokolo s motorem do 250 W, který pomáhá jen při šlapání do 25 km/h, '
          'považováno za jízdní kolo. Výkonnější modely jsou něco jiného a vyžadují registraci a pojištění.</p>'
          '<h3>Baterie a dojezd</h3>'
          + T(['Využití', 'Orientační baterie'], [['Do 15 km denně', 'kolem 300–400 Wh'], ['20–40 km denně', '400–500 Wh'], ['Delší trasy, kopce', '500 Wh a víc']]) +
          '<p>Skutečný dojezd závisí na zátěži, terénu a úrovni asistence. Baterii nabíjejte při pokojové teplotě, mráz dojezd zkracuje. Vyjímatelná baterie se dá nabíjet v bytě.</p>'
          '<h3>Výbava a hmotnost</h3>'
          '<p>Praktické jsou blatníky, nosič, kryt řetězu, světla napájená z baterie a stojánek. Elektrokolo váží obvykle 20 až 28 kg, ověřte, zda ho zvládnete zvednout do schodů nebo na nosič.</p>'
          '<h3>Bezpečnost</h3>'
          '<p>Nezapomeňte na <a href="/cyklisticke-helmy/">helmu</a> a kvalitní <a href="/cyklo-zamky/">zámek</a>, elektrokola jsou častým cílem krádeží.</p>',
    faq=[('Jaké elektrokolo do města?', 'Městské s nízkým rámem, blatníky, nosičem a baterií 400 až 500 Wh. Motor do 250 W, který pomáhá do 25 km/h, se považuje za jízdní kolo.'),
         ('Jaký dojezd má městské elektrokolo?', 'Podle baterie a zátěže od desítek po stovky kilometrů. Výrobce uvádí rozmezí, protože záleží na úrovni asistence a terénu.'),
         ('Potřebuji na městské elektrokolo pojištění?', 'Pokud má motor do 250 W a pomáhá do 25 km/h, považuje se za jízdní kolo a pojištění ani registrace nejsou povinné.'),
         ('Kolik váží městské elektrokolo?', 'Obvykle 20 až 28 kg. Lehčí modely mají menší baterii nebo hliníkový rám.'),
         ('Jak dlouho se nabíjí baterie?', 'Většinou několik hodin ze zásuvky. Přesný údaj najdete u konkrétního modelu.')],
)

NEW['trekingova-elektrokola'] = dict(short=True,
    title='Trekingová elektrokola – porovnání cen a modelů | Sporteka',
    desc='Trekingová a crossová elektrokola na delší výlety: s nosičem, blatníky a velkou baterií. Porovnejte ceny a modely v českých obchodech.',
    intro='<p><strong>Trekingová elektrokola</strong> jsou stavěná na delší výlety po silnici, cyklostezkách i zpevněných cestách. Mívají nosič, blatníky, světla, pohodlnou polohu a baterii s větší kapacitou. '
          'Pro denní dojíždění stačí <a href="/mestska-elektrokola/">městské elektrokolo</a>, do terénu je lepší <a href="/horska-elektrokola/">horské</a>.</p>'
          '<p>Na Sportece porovnáte ceny trekingových elektrokol z českých obchodů a uvidíte, které modely jsou skladem.</p>',
    guide='<h2>Jak vybrat trekingové elektrokolo</h2>'
          '<p>Při výběru sledujte motor, kapacitu baterie, výbavu pro cestování a velikost rámu.</p>'
          '<h3>Motor a baterie</h3>'
          '<p>Středový motor dává lepší stoupání a rozloženou váhu, zadní je jednodušší. Na výlety se hodí baterie od zhruba 500 Wh výš, případně druhá baterie na delší trasy. '
          'Dojezd klesá v kopcích, při protivětru a v zimě, počítejte s rezervou.</p>'
          '<h3>Výbava</h3>'
          '<ul><li><strong>Nosič a brašny:</strong> na vícedenní výlety a nákupy.</li>'
          '<li><strong>Blatníky a kryt řetězu:</strong> pro jízdu i v dešti bez znečištění oblečení.</li>'
          '<li><strong>Světla:</strong> napájená z baterie, bez výměny článků.</li>'
          '<li><strong>Odpružená vidlice nebo sedlovka:</strong> pohodlí na nerovných cestách.</li></ul>'
          '<h3>Velikost rámu</h3>'
          '<p>Vybírejte podle výšky postavy a délky nohou, trekingové rámy se udávají v palcích nebo centimetrech. Pro pohodlí hledejte model s možností nastavit řídítka.</p>'
          '<h3>Údržba</h3>'
          '<p>Pravidelně kontrolujte brzdy, řetěz a tlak v pláštích. Elektrokola jsou těžší a více opotřebovávají brzdové destičky a řetěz. Elektroniku nemyjte tlakovou vodou.</p>',
    faq=[('Jaké elektrokolo na výlety?', 'Trekingové s baterií od 500 Wh, nosičem, blatníky a světly. Pro delší trasy zvažte druhou baterii.'),
         ('Jaký motor je lepší na výlety?', 'Středový motor, který dává přirozenější jízdu a lepší stoupání. Zadní je jednodušší a levnější.'),
         ('Kolik km ujede trekingové elektrokolo?', 'Podle baterie, zátěže a asistence desítky až přes sto kilometrů na jedno nabití. Přesný údaj dává výrobce jako rozmezí.'),
         ('Mohu na trekingové elektrokolo nasadit dětskou sedačku?', 'Ověřte nosnost nosiče a povolení výrobce. Ne každý nosič je pro sedačku určen.'),
         ('Jaká velikost rámu je vhodná?', 'Podle výšky postavy a délky nohou. Při váhání se řiďte tabulkou výrobce a model vyzkoušejte.')],
)

NEW['horska-elektrokola'] = dict(short=True,
    title='Horská elektrokola – porovnání cen a modelů | Sporteka',
    desc='Horská elektrokola (e-MTB) pro terén, kopce a trail: hardtail i celoodpružená. Porovnejte ceny, motory a baterie v českých obchodech.',
    intro='<p><strong>Horská elektrokola</strong> (e-MTB) kombinují terénní kolo s motorem, který pomáhá do kopce. Zvládnete tak delší trasy a stoupání, na která byste jinak neměli sílu. Najdete mezi nimi pevné modely (hardtail) i '
          '<a href="/celoodpruzena-horska-kola/">celoodpružené</a>. Pro pohodlí na silnici zvolte <a href="/trekingova-elektrokola/">trekingové elektrokolo</a>.</p>'
          '<p>Na Sportece porovnáte ceny horských elektrokol z českých obchodů a uvidíte, které modely jsou skladem.</p>',
    guide='<h2>Jak vybrat horské elektrokolo</h2>'
          '<p>Při výběru sledujte motor, baterii, odpružení a hmotnost. Kvalita brzd a odpružení je u terénních kol důležitější než u městských.</p>'
          '<h3>Motor a baterie</h3>'
          '<p>Středové motory mají obvykle točivý moment zhruba 50 až 90 Nm, vyšší zvládne strmější stoupání. Baterie bývají od 500 Wh výš, na delší trasy až přes 700 Wh. Dojezd závisí na terénu, váze a úrovni asistence.</p>'
          '<h3>Hardtail, nebo celoodpružené</h3>'
          '<ul><li><strong>Hardtail:</strong> odpružená jen vidlice, lehčí a levnější, vhodný na lesní cesty.</li>'
          '<li><strong>Celoodpružené:</strong> pohodlnější a stabilnější v náročném terénu, těžší a dražší.</li></ul>'
          '<h3>Brzdy a pláště</h3>'
          '<p>Hydraulické kotoučové brzdy s většími kotouči jsou nutnost, protože elektrokolo je těžší. Pláště s hrubším vzorkem drží v terénu a mají být určené pro vyšší zátěž.</p>'
          '<h3>Hmotnost a péče</h3>'
          '<p>Elektrokola do terénu váží obvykle 20 až 28 kg. Po jízdě v blátě kolo opláchněte (ne tlakovou vodou na motor a baterii) a promažte řetěz. Odpružení pravidelně servisujte.</p>',
    faq=[('Jaké horské elektrokolo vybrat?', 'Podle terénu: hardtail na lesní cesty, celoodpružené na náročný trail. Sledujte motor, baterii a kvalitu brzd.'),
         ('Kolik váží horské elektrokolo?', 'Obvykle 20 až 28 kg podle rámu a baterie. Celoodpružené je těžší než hardtail.'),
         ('Jak velký točivý moment potřebuji?', 'Pro běžný terén stačí zhruba 50 až 70 Nm, na strmé stoupání a těžší jezdce se hodí víc.'),
         ('Je horské elektrokolo vhodné na silnici?', 'Ano, ale s hrubými plášti je pomalejší a hlučnější. Na silnici je lepší trekingové nebo městské.'),
         ('Jak dlouho vydrží baterie horského elektrokola?', 'Při správném zacházení zhruba několik set až tisíc nabíjecích cyklů, pak kapacita klesá. Udržujte ji při pokojové teplotě.')],
)

NEW['fatbike-elektrokola'] = dict(short=True,
    title='Fatbike elektrokola – porovnání cen a modelů | Sporteka',
    desc='Fatbike elektrokola s tlustými pláštěmi pro sníh, písek a terén. Porovnejte ceny, motory a baterie v českých obchodech a ověřte parametry.',
    intro='<p><strong>Fatbike elektrokola</strong> mají tlusté pláště (obvykle 3 až 4 palce), které se nepropadají do písku, sněhu ani bláta. Jsou pohodlná, stabilní a oblíbená na výlety i terénní jízdu. Mnoho modelů jde navíc složit. '
          'Za to jsou těžší a mají větší odpor než běžné <a href="/horska-elektrokola/">horské elektrokolo</a>.</p>'
          '<p>Na Sportece porovnáte ceny fatbike elektrokol z českých obchodů. U každého ověřte výkon motoru a rychlost: pro jízdu po silnici jako jízdní kolo platí limit 250 W a 25 km/h.</p>',
    guide='<h2>Jak vybrat fatbike elektrokolo</h2>'
          '<p>Rozhoduje, kde chcete jezdit, a hlavně jak je model legální pro provoz na silnici.</p>'
          '<h3>Motor a legální parametry</h3>'
          '<p>U některých dovážených modelů je uveden motor s výkonem 500 W a víc nebo rychlost nad 25 km/h. Takové kolo se nepovažuje za jízdní kolo a vyžaduje registraci, pojištění a řidičské oprávnění. '
          'Pokud chcete jezdit bez nich, vyberte model s motorem do 250 W a omezením na 25 km/h a ověřte označení výrobce.</p>'
          '<h3>Baterie a dojezd</h3>'
          '<p>Tlusté pláště zvyšují odpor, proto se u fatbiků vyplatí větší baterie, často kolem 500 až 1000 Wh. Dojezd klesá ve sněhu a v písku, počítejte s rezervou.</p>'
          '<h3>Složitelné modely</h3>'
          '<p>Skládací fatbiky zabírají míň místa v autě a bytě, mají ale menší kola a víc spojů, které je potřeba kontrolovat. Hmotnost je obvykle 25 až 35 kg.</p>'
          '<h3>Servis a záruka</h3>'
          '<p>Před koupí ověřte servisní zázemí, dostupnost baterií a záruku. U levnějších dovozových modelů bývá servis složitější, a proto se vyplatí zeptat se obchodu předem.</p>',
    faq=[('Co je fatbike elektrokolo?', 'Elektrokolo s tlustými pláštěmi (3 až 4 palce), které se nepropadá do sněhu a písku. Je stabilní a pohodlné v terénu.'),
         ('Potřebuji na fatbike elektrokolo registraci?', 'Pokud má motor do 250 W a pomáhá jen do 25 km/h, považuje se za jízdní kolo a registrace není potřeba. Výkonnější modely ji vyžadují.'),
         ('Kolik váží fatbike elektrokolo?', 'Obvykle 25 až 35 kg, podle rámu, baterie a zda jde o skládací model.'),
         ('Jaký dojezd má fatbike elektrokolo?', 'Záleží na baterii, terénu a asistenci. Ve sněhu a písku je dojezd kratší než na silnici.'),
         ('Hodí se fatbike do města?', 'Dá se používat, ale je těžký a pomalejší. Na dojíždění je pohodlnější městské nebo trekingové elektrokolo.')],
)

NEW['skladaci-elektrokola'] = dict(short=True,
    title='Skládací elektrokola – porovnání cen a modelů | Sporteka',
    desc='Skládací elektrokola do bytu, auta i vlaku: s menšími koly a motorem. Porovnejte ceny, hmotnost a baterie v českých obchodech.',
    intro='<p><strong>Skládací elektrokola</strong> se vejdou do kufru, výtahu i vlaku. Mají menší kola (obvykle 16 až 20 palců) a kloub, který kolo složí. Jsou praktická pro dojíždění kombinované s vlakem nebo autem a pro lidi z malých bytů. '
          'Pro delší výlety se hodí spíš <a href="/trekingova-elektrokola/">trekingové elektrokolo</a>.</p>'
          '<p>Na Sportece porovnáte ceny skládacích elektrokol z českých obchodů a uvidíte, které modely jsou skladem.</p>',
    guide='<h2>Jak vybrat skládací elektrokolo</h2>'
          '<p>Při výběru sledujte hmotnost, způsob skládání, velikost po složení a dojezd. Hlavní výhodou je kompaktnost, proto neplatí nižší cena za každou cenu.</p>'
          '<h3>Hmotnost a skládání</h3>'
          '<p>Skládací elektrokola váží obvykle 17 až 25 kg a hmotnost je důležitá, protože kolo budete nosit po schodech a do vlaku. Vyzkoušejte, jak rychle a snadno se skládá, a jestli drží kloub pevně.</p>'
          '<h3>Velikost kol</h3>'
          '<p>Menší kola jsou obratná a kolo je kompaktnější, ale hůř přejíždějí nerovnosti. Pro hladký asfalt jsou vhodná, na hrubý povrch méně.</p>'
          '<h3>Baterie a dojezd</h3>'
          '<p>Menší rám bývá omezen i velikostí baterie, často 250 až 500 Wh. Pro dojíždění stačí, na delší výlety vyberte model s větší baterií.</p>'
          '<h3>Legální parametry</h3>'
          '<p>U dovážených modelů ověřte výkon motoru a omezení rychlosti. Pro provoz bez registrace platí limit 250 W a 25 km/h.</p>',
    faq=[('Jaká je hmotnost skládacího elektrokola?', 'Obvykle 17 až 25 kg. Lehčí modely mají menší baterii.'),
         ('Jaké kola mají skládací elektrokola?', 'Nejčastěji 16 až 20 palců. Menší kola jsou obratná, ale citlivější na nerovnosti.'),
         ('Vejde se skládací elektrokolo do vlaku?', 'Po složení většinou ano, v mnoha vlacích se skládací kolo přepravuje jako zavazadlo. Ověřte podmínky dopravce.'),
         ('Jaký dojezd má skládací elektrokolo?', 'Podle baterie desítky kilometrů. Přesný údaj dává výrobce jako rozmezí.'),
         ('Jak často kontrolovat kloub?', 'Před každou jízdou. Kloub musí být pevně zajištěný, uvolněný kloub je bezpečnostní riziko.')],
)
