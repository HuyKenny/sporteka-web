"""sporteka.cz — wave 23g (4. 11. 2026): long texts for horska-elektrokola, baseball-a-softball, silnicni-a-gravel-kola, snowboardove-boty.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ horska-elektrokola
NEW['horska-elektrokola'] = dict(long=True,
    title='Horská elektrokola: e-MTB, motory, baterie, rámy',
    desc='Horská elektrokola e-MTB: hardtail, celoodpružené, středové motory a baterie. Jak vybrat velikost rámu, brzdy a odpružení a porovnat obchody.',
    intro='<p>Horské elektrokolo, běžně zkracované na e-MTB, spojuje terénní kolo s pomocným motorem, který zesiluje vaše šlapání až do rychlosti, kterou zákon u těchto kol povoluje. Díky tomu zvládnete delší stoupání, víc výškových metrů za den a trasy, které byste na klasickém kole neplánovali. Kategorie na Sportece zahrnuje špičkové celoodpružené modely, praktické hardtaily i levnější kola s motorem v zadním náboji. Při výběru se vyplatí hlídat nejen motor a baterii, ale také brzdy, odpružení, velikost rámu a hmotnostní limit jezdce, protože právě tyto parametry rozhodují o bezpečnosti a o tom, jak dlouho vám kolo bude dobře sloužit.</p>'
          '<p>Nabídky českých obchodů tu porovnáte u značek ' + B(('engwe', 'Engwe'), ('specialized', 'Specialized'), ('crussis', 'Crussis'), ('rockrider', 'Rockrider'), ('olpran', 'Olpran'), ('kross', 'Kross'), ('kellys', 'Kellys')) +
          '. Příbuzné skupiny jsou <a href="/elektrokola/">elektrokola</a> obecně, <a href="/horska-kola/">horská kola</a> bez motoru a <a href="/celoodpruzena-horska-kola/">celoodpružená horská kola</a>.</p>',
    guide='<h2>Co dělá z elektrokola skutečné horské kolo</h2>'
          '<p>Nálepka horské na rámu ještě nic nezaručuje. Opravdové e-MTB poznáte podle odpružené vidlice s rozumným zdvihem, širokých plášťů s agresivním vzorkem, hydraulických kotoučových brzd a geometrie, která drží stabilitu ve svahu. Řada levných kol s tlustými plášti a motorem v zadním kole vypadá terénně, ale na kamenitém sjezdu rychle narazí na limity vidlice, brzd i rámu.</p>'
          '<p>Při procházení nabídky proto čtěte specifikace víc než fotografie. Zjistěte typ motoru, kapacitu baterie, zdvih odpružení, velikost kol a výrobcem uvedenou maximální hmotnost jezdce včetně výbavy. Právě poslední údaj lidé přehlížejí, přitom u těžkého kola s motorem je důležitý.</p>'
          '<h2>Typy horských elektrokol</h2>'
          + T(['Typ', 'Charakter', 'Hodí se pro'], [
              ['Hardtail e-MTB', 'odpružená jen přední vidlice, jednodušší rám', 'lesní a polní cesty, dojíždění, rekreační výlety'],
              ['Celoodpružené trail e-MTB', 'odpružení vpředu i vzadu, střední zdvih', 'univerzální horská jízda, stoupání i sjezd'],
              ['Lehké e-MTB s menším motorem', 'nižší hmotnost, menší baterie, přirozený pocit', 'sportovní jezdci, kteří chtějí kolo podobné klasickému'],
              ['Enduro e-MTB', 'velký zdvih, robustní rám a plášť', 'bikepark, technické sjezdy, těžký terén'],
              ['Levné kolo s nábojovým motorem', 'motor v zadním kole, často pevný rám', 'rovinaté a mírně kopcovité trasy, nenáročná jízda']]) +
          '<p>Pokud hledáte kolo hlavně na asfalt a zpevněné cesty, podívejte se raději na <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>. Horská verze je těžší a pomalejší na silnici. Pro sníh a písek existují <a href="/fatbike-elektrokola/">fatbike elektrokola</a> a pro rychlou jízdu po štěrku <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel elektrokola</a>.</p>'
          '<h2>Motor: střední, nebo v náboji</h2>'
          '<p>Motor ve středu rámu, u pedálů, působí přímo na řetěz a využívá převody kola. Proto dobře táhne do strmých kopců a rozložení hmotnosti zůstává nízko a uprostřed, což pomáhá ovladatelnosti. Motor v zadním náboji je jednodušší a levnější, ale na prudkém stoupání nemá k dispozici převodový poměr a rychleji se zahřívá. Taková kola se hodí na mírný terén.</p>'
          '<p>U středových motorů sledujte točivý moment v newtonmetrech a typ senzoru. Vyšší točivý moment pomůže ve stoupání a při rozjezdu s nákladem, ale dojezd tím obvykle klesá. Pedálový senzor, který měří sílu vašeho šlapání, dává přirozenější odezvu než jednoduchý senzor otáčení kliky. V horském terénu to rozhoduje o kontrole nad kolem.</p>'
          '<p>Dalším tématem je ovládání. Malý displej na řídítkách ukazuje úroveň asistence a stav baterie, ovladač pod palcem umožňuje měnit režim bez sundání ruky. U některých modelů najdete aplikaci pro telefon, ve které se dá doladit odezva motoru.</p>'
          '<h2>Baterie, dojezd a nabíjení</h2>'
          '<p>Kapacita baterie se udává ve watthodinách. Vyšší hodnota znamená víc energie, ale také vyšší hmotnost a delší nabíjení. Dojezd, který výrobce uvádí, vzniká za ideálních podmínek, a skutečná hodnota závisí na sklonu terénu, hmotnosti jezdce, teplotě, tlaku v pláštích a zvolené úrovni asistence. Když jedete pořád v nejsilnějším režimu do kopce, počítejte s mnohem kratší trasou než při střídání režimů.</p>'
          '<ul><li><strong>Vyjímatelná baterie:</strong> nabíjíte ji doma u zásuvky, nemusíte nosit celé kolo. Hodí se pro byt v paneláku.</li>'
          '<li><strong>Integrovaná baterie:</strong> je skrytá v rámu, kolo vypadá čistěji a těžiště je nižší, ale výměna bývá složitější.</li>'
          '<li><strong>Druhá baterie:</strong> u dlouhých túr se někdy vozí náhradní v batohu, jestli ji výrobce pro daný model nabízí.</li>'
          '<li><strong>Zima:</strong> v mrazu kapacita dočasně klesá. Baterii je dobré skladovat uvnitř a nabíjet ji při pokojové teplotě.</li></ul>'
          '<h2>Rám, velikost a velikost kol</h2>'
          '<p>Rámy se vyrábějí z hliníku nebo z karbonu. Hliník je odolný a cenově dostupnější, karbon je lehčí a tužší, ale citlivější na bodové nárazy. U e-MTB se hmotnost rámu promítá do celkové váhy méně než u klasického kola, protože baterie a motor přidávají několik kilogramů navíc. Důležitější než materiál je správná velikost rámu.</p>'
          '<p>Velikost vyberte podle výšky postavy a podle výrobcovy tabulky, nikoli podle toho, co je zrovna skladem. Příliš velký rám znamená nepohodlný sed a těžké ovládání v zatáčkách, příliš malý omezuje sílu šlapání a vede k přetížení zad. Mezi velikostmi se zpravidla rozhodujte podle délky předloktí a stylu jízdy.</p>'
          + T(['Velikost kol', 'Vlastnost', 'Poznámka'], [
              ['26 palců', 'obratná, nižší setrvačnost', 'najdete ji hlavně u levnějších modelů a menších jezdců'],
              ['27,5 palce', 'živější v zatáčkách a v technickém terénu', 'oblíbená u nižších postav a enduro kol'],
              ['29 palců', 'lepší přejíždění překážek a stabilita', 'standard pro většinu trailových a cross-country e-MTB'],
              ['Směs 29 vpředu a 27,5 vzadu', 'stabilní předek, hravý zadek', 'používá se u některých enduro modelů']]) +
          '<h2>Odpružení, brzdy a pláště</h2>'
          '<p>Vidlice a zadní tlumič musí zvládat vyšší hmotnost elektrokola. Při nákupu proto upřednostněte vidlice s nastavitelným tlumením a možností změnit tlak podle jezdce. Zdvih kolem 120 až 150 milimetrů se hodí pro všestranný trail, vyšší hodnoty pro enduro. Levná vidlice s pružinou a bez nastavení se dá brzy zahřát a přestane účinně pracovat.</p>'
          '<p>Brzdy jsou u e-MTB důležitější než u klasického kola. Hydraulické kotoučové brzdy s kotouči o průměru 180 až 203 milimetrů mají dost výkonu na to, aby zastavily těžší stroj ve svahu. Mechanické kotoučové brzdy u levných modelů fungují, ale při dlouhém sjezdu se unaví ruka a bržděním roste riziko přehřátí. Pláště by měly mít označení pro elektrokola nebo alespoň zesílenou kostru a vzorek s dobrým záběrem.</p>'
          '<h2>Pohon a převody</h2>'
          '<p>Většina moderních e-MTB používá jeden převodník vpředu, kombinovanou s širokou kazetou vzadu, která má obvykle deset až dvanáct rychlostí. Pohon je u elektrokola zatížen víc, protože motor přidává točivý moment, a proto se řetěz a kazeta opotřebují dřív než u kola bez motoru. Pravidelné mazání a včasná výměna jsou levnější než oprava poškozeného zubu na ozubeném kole.</p>'
          '<p>Při řazení pod zátěží pomáhá krátce povolit tlak na pedály. Moderní motory některé řazení tlumí samy, přesto se šetrný styl vyplatí. Po zásahu do pohonu zkontrolujte napnutí řetězu a seřízení přehazovačky.</p>'
          '<h2>Pro koho je horské elektrokolo</h2>'
          '<ul><li><strong>Začátečník s kondicí pod průměrem:</strong> motor vyrovnává rozdíl mezi členy skupiny a umožní jet s kolegy na stejné trase.</li>'
          '<li><strong>Zkušený jezdec:</strong> více sjezdů za den, delší túry v horách a trénink techniky bez únavy z výjezdů.</li>'
          '<li><strong>Dojíždějící do práce hrbolatou trasou:</strong> hardtail s dobrou vidlicí zvládne polňačky i lesní zkratku.</li>'
          '<li><strong>Rodina nebo páry s rozdílnou výkonností:</strong> pomocný motor posunuje limit slabšího jezdce a výlet se odehrává tempem celé skupiny.</li></ul>'
          '<h2>Co obvykle chybí v rozpočtu</h2>'
          '<p>K elektrokolu patří výbava, kterou je lepší počítat hned. Přilba je základ, a to nejlépe s rozšířenou ochranou zátylku, viz <a href="/cyklisticke-helmy/">cyklistické helmy</a>. Rukavice, brýle a pevné boty snižují následky pádu. Pro terén se vyplatí <a href="/cyklo-chranice/">chrániče pro cyklisty</a>, zvlášť na prudších sjezdech. Na delší trasy se hodí <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a>, <a href="/cyklo-pumpy-a-naradi/">pumpa a nářadí</a> a <a href="/cyklo-zamky/">zámek na kolo</a>, protože cena elektrokola láká zloděje.</p>'
          '<h2>Servis a péče</h2>'
          '<ul><li>Po jízdě v blátě kolo omyjte jemným proudem vody a nemiřte přímo na motor, displej, konektory ani ložiska. Tlaková myčka vtlačí vodu tam, kam nepatří.</li>'
          '<li>Řetěz promazávejte pravidelně, nejlépe po každém umytí kola, a po zaschnutí přebytek utřete. Prostředky pro údržbu najdete v kategorii <a href="/cyklo-udrzba/">údržba kola</a>.</li>'
          '<li>Brzdové destičky jsou spotřební materiál. Při mokrém terénu a vyšší hmotnosti se opotřebovávají rychleji.</li>'
          '<li>Odpružení i tlumič potřebují pravidelný servis podle intervalu výrobce, jinak ztrácejí citlivost.</li>'
          '<li>Při delším skladování nenechávejte baterii úplně vybitou ani plně nabitou. Střední stav nabití je pro dlouhodobé uložení vhodnější.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Výběr podle nejvyššího udaného dojezdu místo reálného terénu a váhy jezdce.</li>'
          '<li>Podcenění brzd a odpružení, zvlášť u kol se silným motorem.</li>'
          '<li>Koupě kola bez záruky servisu a dostupných náhradních dílů, hlavně u málo známých značek.</li>'
          '<li>Zanedbání doprovodné výbavy, tedy přilby a zámku.</li>'
          '<li>Nepřevzetí hmotnosti kola do úvahy při nošení po schodech nebo vyvěšování na nosič v autě. Použít lze <a href="/cyklo-nosice-na-auto/">nosiče kol na auto</a>, ale ověřte jejich nosnost.</li></ul>'
          '<h2>Jak porovnat nabídky na Sportece</h2>'
          '<p>Stejný model se v různých obchodech liší rokem výroby, velikostí rámu, dostupností a dopravou. Zkontrolujte tedy, že porovnáváte shodnou velikost i modelový rok. U kol z lokálních e-shopů ověřte, zda nabízejí předprodejní seřízení a servis. U cizojazyčných nabídek se zeptejte na záruku a vrácení zboží. Kolo je rozměrné a vrácení stojí čas i peníze.</p>',
    faq=[('Jaké horské elektrokolo vybrat na začátek?', 'Pro lesní cesty a mírné terény stačí hardtail se středovým motorem, hydraulickými brzdami a odpruženou vidlicí. Celoodpružené modely mají smysl, pokud často jezdíte technické sjezdy.'),
         ('Je lepší motor ve středu, nebo v zadním kole?', 'Středový motor využívá převody kola, táhne lépe do prudkých kopců a lépe rozkládá hmotnost. Motor v náboji je jednodušší a levnější, ale na strmém stoupání je omezenější.'),
         ('Kolik Wh má mít baterie na horské túry?', 'Záleží na délce trasy a na stoupání. Na půldenní výlety obvykle stačí střední kapacita, na celodenní túry v horách se hodí vyšší kapacita nebo náhradní baterie, pokud ji výrobce nabízí.'),
         ('Jak velký rám mám zvolit?', 'Řiďte se výškou postavy a velikostní tabulkou konkrétního výrobce. Geometrie se mezi značkami liší, proto stejné písmeno velikosti neznamená vždy stejný rozměr.'),
         ('Může horské elektrokolo jezdit po silnici?', 'Může. Jízdu zpomalují hrubé pláště a větší odpor, ale pro dojíždění je to schůdné. Pro převážně silniční použití je ovšem lepší trekingový nebo městský model.'),
         ('Jaké brzdy jsou pro e-MTB vhodné?', 'Hydraulické kotoučové brzdy s většími kotouči a kvalitními destičkami. Elektrokolo je těžší než klasické kolo, takže slabé brzdy se brzy přehřívají.'),
         ('Dá se baterie nabíjet kdekoli?', 'Nabíjejte ji běžnou zásuvkou původní nabíječkou při pokojové teplotě. Použití cizí nabíječky může baterii poškodit a ztratit záruku.'),
         ('Platí pro e-MTB omezení rychlosti?', 'Pomocný motor má u elektrokol v běžném provozu asistenci omezenou na dvacet pět kilometrů v hodině. Nad touto rychlostí motor přestane pomáhat a jedete jen vlastní silou.'),
         ('Jak často je třeba servis?', 'Základní kontrola brzd, pohonu a šroubů se vyplatí před sezonou a po náročnějším období. Odpružení a motor mají intervaly stanovené výrobcem, které je dobré dodržet kvůli záruce.'),
         ('Pomůže pojištění a zámek před krádeží?', 'Dobrý zámek s pevným řetězem nebo obloukem a zamykání k pevnému bodu snižují riziko. Pojištění si ověřte u své pojišťovny, protože podmínky pro elektrokola se liší.'),
         ('Co ověřit u levných kol s motorem?', 'Zjistěte hmotnostní limit, kvalitu brzd, dostupnost náhradních dílů a servisu. Pokud výrobce neuvádí typ motoru nebo kapacitu baterie, buďte opatrní.')],
)

# ------------------------------------------------------------------ baseball-a-softball
NEW['baseball-a-softball'] = dict(long=True,
    title='Baseball a softball: pálky, rukavice, míčky, sety',
    desc='Baseball a softball: pálky, rukavice, míčky a startovní sady. Jak vybrat délku pálky, velikost rukavice a materiál a porovnat obchody.',
    intro='<p>Baseball a softball spolu sdílejí základní vybavení, přesto se míče, pálky i rukavice mírně liší velikostí a použitím. V kategorii Sporteky najdete pálky ze dřeva, hliníku i kompozitu, kožené i syntetické rukavice, míče a kompletní sady pro děti. Hodí se pro oddíly, školní hodiny tělesné výchovy i hru na zahradě. Důležité je vybírat podle věku, výšky hráče a pravidel soutěže, protože velikost pálky a rukavice rozhoduje o tom, zda hra bude bavit a zda se hráč naučí správnou techniku od začátku.</p>'
          '<p>Nabídky českých obchodů zde porovnáte u značek ' + B(('barnett', 'Barnett'), ('merco', 'Merco'), ('kipsta', 'Kipsta'), ('rawlings', 'Rawlings'), ('louisville-slugger', 'Louisville Slugger'), ('sedco', 'Sedco'), ('spartan-sport', 'Spartan Sport')) +
          '. Sousední sporty najdete v kategoriích <a href="/micove-sporty/">míčové sporty</a> a <a href="/ragby-a-americky-fotbal/">ragby a americký fotbal</a>.</p>',
    guide='<h2>Co se v kategorii prodává</h2>'
          '<p>Základní sada na baseball se skládá z pálky, rukavice a míče. V kategorii najdete hlavně startovní sady, samostatné pálky, rukavice a míče. Specializované vybavení, jako jsou chrániče chytače nebo tréninkové sítě, bývá méně běžné, takže ho hledejte spíš v užších kategoriích.</p>'
          + T(['Zboží', 'Použití', 'Na co si dát pozor'], [
              ['Pálky dřevěné', 'tradiční hra, trénink síly a techniky', 'dřevo se může zlomit, vyberte druh a délku'],
              ['Pálky hliníkové a kompozitní', 'školní hra, rekreace, oddíly', 'lehčí a odolnější, pravidla ligy mohou typ omezit'],
              ['Rukavice kožené', 'pravidelné hraní, delší životnost', 'je třeba je rozhrát a ošetřovat'],
              ['Rukavice syntetické', 'děti, školy, příležitostná hra', 'lehčí a bez rozhrávání, nižší životnost'],
              ['Míče baseball a softball', 'trénink i zápasy', 'baseballový míč je menší než softballový'],
              ['Soupravy pálka, rukavice, míč', 'začátečníci a děti', 'zkontrolujte velikost podle věku']]) +
          '<h2>Baseball nebo softball: čím se liší</h2>'
          '<p>Baseballový míč je menší a tvrdší, má obvod kolem devíti palců a nadhazuje se rychle shora z větší vzdálenosti. Softballový míč je větší, obvykle dvanáct palců, a nadhazuje se zespodu z menší vzdálenosti. Rukavice jsou proto pro softball často větší a s hlubší kapsou. Pálky se liší délkou, váhou i průměrem hlavy, proto je lepší nekombinovat vybavení z jednoho sportu s druhým, pokud to pravidla neumožňují.</p>'
          '<p>Na rekreační úrovni se rozdíly stírají. Rodiny, které hrají pro zábavu na zahradě, často používají měkčí míče z pěny nebo gumy a lehčí plastové pálky. Jsou bezpečnější pro malé děti a nepoškodí okna. Pro oddílovou hru ale potřebujete vybavení podle pravidel své soutěže.</p>'
          '<h2>Pálky: materiál, délka, váha</h2>'
          '<p>Dřevo patří k tradici baseballu. Používají se druhy jako javor, jasan nebo buk, každý má jiné vlastnosti. Jasan je pružnější, javor tvrdší, buk se uplatňuje u levnějších a tréninkových pálek. Dřevěná pálka při špatném zásahu praskne, takže je dobré mít náhradu. Hliníkové pálky jsou dutější, lehčí a trvanlivé, vydrží tisíce úderů a mají širší sladké místo, tedy oblast, kde je úder nejefektivnější.</p>'
          '<p>Délka se měří v palcích. Jednoduché pravidlo říká, že pálka má při postavení svisle vedle těla sahat zhruba k boku nebo ke kyčli hráče. Je-li příliš dlouhá, nedá se kontrolovat, a je-li příliš krátká, pálkař nedosáhne na vnější nadhoz. Váha se udává v uncích a parametr „drop“ je rozdíl mezi délkou v palcích a váhou v uncích; nižší číslo znamená těžší pálku. Dítě by mělo pálku zvládnout udržet před tělem aspoň několik sekund bez třesu paže.</p>'
          '<ul><li><strong>Děti a začátečníci:</strong> lehčí pálky v kratší délce, aby se osvojila správná technika švihu.</li>'
          '<li><strong>Dospívající:</strong> přechod k delší pálce se provádí postupně podle výšky a síly.</li>'
          '<li><strong>Dospělí rekreační hráči:</strong> hliník nebo kompozit pro pohodlí a trvanlivost.</li>'
          '<li><strong>Trénink:</strong> těžší pálky nebo obtížnější vybavení slouží k posílení, ale používejte je s mírou, aby nezhoršily švih.</li></ul>'
          '<h2>Rukavice: velikost, kůže, ruka</h2>'
          '<p>Rukavice se vyrábějí pro pravou i levou ruku. Pravidlo je pro někoho nepřirozené, protože rukavice patří na ruku, kterou nehážete. Praváci tedy nosí rukavici na levé ruce a levorucí naopak. U značení, jako RH nebo LH, je třeba ověřit, zda označuje ruku, na které se rukavice nosí, nebo ruku, kterou se hází. Různí výrobci to píší různě, proto se informace vyplatí zkontrolovat v popisu.</p>'
          '<p>Velikost rukavice se uvádí v palcích od hrany prstů k dlani. Děti začínají u zhruba deseti až jedenácti palců, dospělí zpravidla u dvanácti až třinácti. Pozice na hřišti určuje tvar: vnější polař potřebuje delší rukavici, vnitřní hráč kratší a mělčí, aby se míč snadno vyndal a hodil dál. Chytač a první metař mají specializované tvary.</p>'
          '<h3>Kůže, nebo syntetika</h3>'
          '<p>Kožené rukavice jsou zpočátku tuhé a vyžadují rozhrání, ale vydrží roky a přizpůsobí se ruce. Syntetické modely se obejdou bez rozhrávání, jsou lehčí a odolnější vůči vlhku, ale opotřebují se rychleji. Pro děti v růstu je syntetika praktickou volbou, protože rukavice se stejně brzy vymění. Pro dospívající a dospělé hráče pravidelně trénující se vyplatí kůže.</p>'
          '<h3>Jak rukavici rozhrát a ošetřit</h3>'
          '<ul><li>Opakovaně vhazujte míč do kapsy a zavírejte rukavici, aby kůže změkla v místě, kde se chytá.</li>'
          '<li>Používejte prostředek na ošetření kůže vhodný pro rukavice a nepřehánějte jeho množství, jinak rukavice ztěžkne.</li>'
          '<li>Rukavici uložte s míčem v kapse a převázanou, aby si udržela tvar.</li>'
          '<li>Nesušte ji u radiátoru, kůže praská a ztrácí pružnost.</li></ul>'
          '<h2>Míče a trénink</h2>'
          '<p>Míče se liší jádrem a povrchem. Soutěžní míče mají korkové nebo gumové jádro obalené vlnou a koženým nebo syntetickým povrchem a jsou tvrdé. Tréninkové a rekreační míče jsou měkčí, často z pěny nebo z plastu, a hodí se pro děti nebo pro hru v úzkém prostoru. Softballové míče se vyrábějí v několika barvách, žlutá je na hřišti dobře vidět.</p>'
          '<p>Pokud trénujete pálkování doma, pomůže tréninková síť nebo závěsný míč na gumě. Menší děti mohou začít na stojanu na nadhazování, kde je míč opřen o tyč a pálkař se učí švihu bez nadhazovače. Pro přihrávky, chytání a hozená cvičení slouží <a href="/ostatni-micove-sporty/">další míčové sporty a příslušenství</a>, kde najdete různé typy míčů.</p>'
          '<h2>Bezpečnost</h2>'
          '<p>Baseball je kontaktní jen zčásti, ale míč letí rychle. Helma pro pálkaře s ochranou uší je u organizovaného baseballu a softballu povinnost, u dětí je vhodná i při tréninku. Chytač potřebuje masku, chránič hrudi a holení. Pro mladší hráče existují měkké míče, které snižují riziko zranění. V rekreační hře mějte dostatečný odstup mezi pálkařem a ostatními. Pokud se hraje na veřejném hřišti, zvažte ochranu okolí, protože tvrdý míč dokáže poškodit okna a automobily.</p>'
          '<p>Podobný přístup k ochraně platí i v jiných sportech. Přehled chráničů najdete v kategoriích <a href="/chranice-a-helmy/">chrániče a helmy</a> a <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>, kde vybíráte podle typu zátěže a velikosti.</p>'
          '<h2>Startovní sady pro děti</h2>'
          '<p>Sady, které obsahují pálku, míč a rukavici, jsou pro začátečníky praktické. Nakupujete víc kusů najednou a máte jistotu, že vybavení k sobě pasuje. Zaměřte se na velikost podle věku, protože příliš velká pálka zkazí první zkušenosti s hrou. Kvalitní sada vydrží i několik sezon, ale děti rychle rostou, takže se dá čekat výměna za větší velikost.</p>'
          '<p>Rodiče by měli dítěti nechat vyzkoušet, jestli se mu líbí chytání, hození nebo pálkování. Někdo začne od jedné dovednosti a ostatní přibere postupně. U oddílů se spolu zeptejte trenéra, jaké vybavení klub používá, aby se nekupovalo zbytečně.</p>'
          '<h2>Jak porovnat nabídky</h2>'
          '<ul><li>Zkontrolujte rozměr: délka pálky v palcích, obvod míče, velikost rukavice a ruku, na kterou se nosí.</li>'
          '<li>Rozlišujte soutěžní a rekreační vybavení. Levná sada pro děti nenahradí vybavení pro ligu a naopak.</li>'
          '<li>U dřevěných pálek se podívejte na druh dřeva a zda je pálka určena ke hře, nebo jen dekorativní.</li>'
          '<li>Sledujte dostupnost velikostí v obchodech, protože u sportovních sad se často vyprodá právě ta nejpoužívanější.</li></ul>'
          '<h2>Oddílová hra a pravidla</h2>'
          '<p>Kdo hraje v lize nebo v oddíle, měl by vybavení konzultovat s trenérem. Svazy a soutěže mohou omezit materiál pálek, rozměry rukavic nebo typ míče, zvlášť v mládežnických kategoriích. Pálka, která se hodí na zahradu, nemusí být v zápase povolena. Také barva a značení míčů se v soutěžích předepisuje. Pokud hrajete rekreačně, můžete si vybavení vybrat podle pohodlí a bezpečnosti bez těchto omezení.</p>'
          '<p>Důležitá je i hra ve více lidech. Na jedno hřiště potřebujete vícero rukavic, aspoň dva míče a pálku, kterou si mohou půjčovat. Při školních lekcích se často používají lehké pálky z plastu nebo pěny, které lze snadno sdílet. Zvažte také tašku na vybavení, která ochrání rukavice před vlhkem a pálky před poškrábáním.</p>'
          '<h2>Základní dovednosti, na které se vybavení váže</h2>'
          '<ul><li><strong>Pálkování:</strong> důležitý je postoj, držení pálky oběma rukama a švih od boků. Lehčí pálka pomáhá udržet techniku.</li>'
          '<li><strong>Chytání:</strong> rukavice se otevírá směrem k míči, druhá ruka kryje míč při chycení, aby nevypadl.</li>'
          '<li><strong>Házení:</strong> krok vpřed, rotace trupu a uvolnění zápěstí zabrání přetížení ramene.</li>'
          '<li><strong>Běh po metách:</strong> pevná obuv s dobrým držením, na hřišti se osvědčují i běžecké boty z kategorie <a href="/bezecka-obuv/">běžecká obuv</a>.</li></ul>'
          '<h2>Související kategorie</h2>'
          '<p>Pokud se zajímáte o sporty s pálkou a míčem, podívejte se také na <a href="/tenis/">tenis</a>, <a href="/badminton/">badminton</a> nebo <a href="/padel/">padel</a>, kde se používají rakety. Pro týmové sporty s míčem na hřišti slouží <a href="/fotbal/">fotbal</a>, <a href="/basketbal/">basketbal</a> a <a href="/volejbal/">volejbal</a>.</p>',
    faq=[('Jak dlouhou baseballovou pálku vybrat?', 'Postavte pálku svisle vedle těla. Měla by sahat zhruba ke kyčli nebo k pasu. U dětí vybírejte spíše kratší a lehčí variantu, aby zvládly kontrolovat švih.'),
         ('Je lepší dřevěná, nebo hliníková pálka?', 'Dřevo je tradiční a používá se v profesionálních soutěžích. Hliník je lehčí, trvanlivější a pro rekreaci i děti praktičtější. Pravidla vaší soutěže mohou typ omezit.'),
         ('Čím se liší softball od baseballu?', 'Softballový míč je větší a nadhazuje se zespodu, baseballový je menší a nadhazuje se shora. Liší se i velikost hřiště a často velikost rukavic.'),
         ('Jakou velikost rukavice koupit dítěti?', 'Malé děti obvykle začínají u deseti až jedenácti palců, starší u dvanácti. Rukavice nesmí být příliš velká, aby se dala zavřít kolem míče.'),
         ('Na kterou ruku patří rukavice?', 'Nosí se na ruce, kterou nehážete. Pravák ji tedy má na levé ruce. Při nákupu zkontrolujte označení RH a LH, protože výrobci ho používají různě.'),
         ('Jak rozhrát koženou rukavici?', 'Opakovaně do ní házejte míč, ohýbejte ji v místě kapsy a občas ji ošetřete prostředkem na kůži. Na noc ji nechte zavřenou s míčem uvnitř.'),
         ('Mohu hrát baseball se softballovým míčem?', 'Mechanicky to jde, ale míče se liší velikostí a váhou, a proto se mění i chytání, házení a pálkování. Pro soutěžní hru používejte míč, který předepisují pravidla.'),
         ('Potřebuje dítě helmu na trénink?', 'Pro pálkaře je helma vhodná vždy, v organizovaném baseballu často povinná. Chrání hlavu při zásahu míčem a při nárazu pálky.'),
         ('Jaké míče jsou vhodné pro malé děti?', 'Měkké pěnové nebo gumové míče. Jsou lehčí, bezpečnější a při hře na zahradě nepoškodí okolí.'),
         ('Jak pečovat o pálku?', 'Dřevěnou pálku skladujte v suchu a pravidelně kontrolujte trhliny. Hliníkovou očistěte od bláta a zkontrolujte promáčkliny, které mohou snížit pevnost.'),
         ('Proč jsou některé sady levnější než samostatné vybavení?', 'Sady míří na začátečníky a rekreační hru, takže používají jednodušší materiály. Pro pravidelný trénink v oddíle je lepší kupovat kusy odpovídající požadavkům soutěže.')],
)

# ------------------------------------------------------------------ silnicni-a-gravel-kola
NEW['silnicni-a-gravel-kola'] = dict(long=True,
    title='Silniční a gravel kola: rámy, převody, brzdy, pláště',
    desc='Silniční, gravelová a triatlonová kola: karbon, hliník, kotoučové brzdy a převody. Jak vybrat velikost rámu a porovnat nabídky obchodů.',
    intro='<p>Silniční kolo je stavěné na rychlost po asfaltu, gravel na dlouhé trasy, kde se střídá štěrk, polňačka a silnice. Obě skupiny mají beraní nebo rovné řídítko, úzké až středně široké pláště a rám zaměřený na efektivní šlapání. Na Sportece sem patří silniční kola, gravelová kola a triatlonové stroje. Před koupí si ujasněte, kde budete nejčastěji jezdit, jak dlouhé trasy plánujete a jaké pláště a převody vám budou vyhovovat, a teprve potom porovnávejte konkrétní modely a nabídky.</p>'
          '<p>Nabídky obchodů tu porovnáte u značek ' + B(('van-rysel', 'VAN Rysel'), ('sava', 'Sava'), ('trek', 'Trek'), ('kellys', 'Kellys'), ('pinarello', 'Pinarello'), ('lapierre', 'Lapierre'), ('bottecchia', 'Bottecchia'), ('specialized', 'Specialized')) +
          '. Podskupiny jsou <a href="/silnicni-kola/">silniční kola</a> a <a href="/gravel-kola/">gravel kola</a>, širší pohled nabízí <a href="/jizdni-kola/">jízdní kola</a>.</p>',
    guide='<h2>Čím se silniční a gravel kolo liší</h2>'
          '<p>Na první pohled vypadají podobně, ale geometrie a výbava míří jinam. Silniční kolo má kratší rozvor, nižší řídítka a užší pláště, aby se na hladkém povrchu rychle zrychlovalo a málo bránilo vzduchu. Gravelové kolo má delší rozvor, vyšší předek, širší pláště a často rezervní závity na brašny či blatníky. Na hrbolaté cestě je stabilnější a pohodlnější, na rovině o něco pomalejší.</p>'
          + T(['Typ kola', 'Pláště a geometrie', 'Hodí se pro'], [
              ['Závodní silniční', 'úzké pláště, agresivní poloha', 'rychlé jízdy, závody, kondiční výkony'],
              ['Vytrvalostní silniční', 'širší pláště, vzpřímenější poloha', 'dlouhé trasy, pohodlí, zahájení sezony'],
              ['Aero silniční', 'tvarované trubky, integrované kabely', 'rovinaté tratě a vysoké rychlosti'],
              ['Gravel', 'široké pláště, kotoučové brzdy, lepší prostor', 'štěrk, polní cesty, výlety s brašnami'],
              ['Triatlon a časovka', 'extrémně aerodynamická poloha, nástavce', 'závody s individuálním startem a triatlon'],
              ['Silniční turistické', 'odolná konstrukce, upevnění blatníků', 'cykloturistika, dojíždění, začátečníci']]) +
          '<p>Pokud nevíte, zda si vyzkoušet gravel, uvažujte, kolik z vašich tras vede po nezpevněném povrchu. Když necelá čtvrtina, bohatě stačí silniční vytrvalostní kolo se širšími plášti. Když polovina a víc, dává smysl gravel. Fanoušci mají obvykle dvě sady kol, jednu úzkou na asfalt a druhou širokou na štěrk.</p>'
          '<h2>Materiál rámu: hliník, karbon, ocel, titan</h2>'
          '<p>Hliník je odolný, cenově příznivý a často vidíte hliníkové rámy u začátečnických i středních modelů. Karbon umožňuje tvarovat trubky a lépe tlumit vibrace, váha je nižší, ale rám je citlivější na nárazy a při poškození se špatně opravuje. Ocel je tradiční materiál s příjemnou pružností, titan je odolný proti korozi, ale vzácný. V katalogu převažují hliník a karbon.</p>'
          '<p>U gravelu je rozhodující prostor pro pláště a výrobcem udaná maximální šířka. Pokud plánujete jízdu v blátě, potřebujete víc volného místa. Zkontrolujte také úchyty pro blatníky, nosiče a lahve, bez nich se z kola těžko stane dlouhodobý dopravní prostředek.</p>'
          '<h2>Velikost rámu a nastavení</h2>'
          '<p>Silniční kolo musí sedět přesně. Příliš dlouhý rám zatěžuje záda a ramena, příliš krátký stlačuje kolena a zhoršuje dýchání. Rozhodující je kombinace výšky postavy, délky rozkroku a délky trupu a paží. Tabulky výrobců obsahují doporučené rozsahy, ale nezaručují, že vám kolo bude sedět. Pro prvním nákupu využijte měření v prodejně nebo bike fitting, hlavně pokud plánujete jezdit víc než pár hodin týdně.</p>'
          '<ul><li><strong>Výška sedla:</strong> noha v nejnižším bodě pedálu má zůstat lehce pokrčená, nikdy napnutá.</li>'
          '<li><strong>Délka představce:</strong> určuje dosah na řídítka. Kratší představec zpříjemní postoj, delší jej natáhne.</li>'
          '<li><strong>Šířka řídítek:</strong> obvykle odpovídá šířce ramen. Gravelová řídítka bývají širší a mírně rozšířená dolů pro lepší ovládání.</li>'
          '<li><strong>Délka klik:</strong> většina jezdců využije standardní délku, vyšší nebo nižší postavy mohou zkusit jinou.</li></ul>'
          '<h2>Převody: kolik převodníků a jaké rozpětí</h2>'
          '<p>Silniční kola mají tradičně dva převodníky vpředu a kazetu vzadu, dohromady dvaadvacet až čtyřiadvacet rychlostí. Kompaktní převodníky dávají lehčí převody do kopce, velké převodníky vyšší rychlost na rovině. Gravel často používá jediný přední převodník a široké kazety, které zjednoduší ovládání a lépe snášejí bláto. Řazení může být mechanické, nebo elektronické. Elektronické řazení, které se v katalogu objevuje u dražších modelů, přeřazuje přesně a bez námahy, ale potřebuje nabíjet akumulátor.</p>'
          '<p>Hodnotu rychlostí neberte jako ukazatel kvality. Důležité je rozpětí, tedy poměr nejlehčího a nejtěžšího převodu. Do hor potřebujete lehký převod, na rovinu těžký. Začátečník v kopcovitém terénu využije kompaktní sadu nebo gravelový převod s velkou kazetou, závodník na rovině nižší stupně nepotřebuje.</p>'
          '<h2>Brzdy: kotoučové, nebo ráfkové</h2>'
          '<p>Moderní silniční i gravelová kola mají téměř vždy hydraulické kotoučové brzdy. Brzdí spolehlivě i za deště, zvládají delší sjezdy a umožňují použít širší pláště. Ráfkové brzdy se objevují u starších modelů a v nejlevnějších kategoriích. Jsou lehčí, ale při mokru ztrácejí výkon. Pokud kupujete použité kolo nebo výprodejový kus, ověřte, zda jsou součástky, jako destičky a kotouče, dostupné.</p>'
          '<p>U kotoučových brzd rozlišujte hydraulické a mechanické ovládání. Hydraulika dává lepší modulaci a menší sílu na páčku. Mechanické brzdy se snáze seřizují v terénu, ale nedosahují stejné účinnosti. Pro gravel na dlouhé výlety se hodí kotouč o něco větší, pro silnici stačí menší.</p>'
          '<h2>Kola a pláště</h2>'
          '<p>Kola mají největší vliv na pocit z jízdy. Lehká a tuhá kola zlepšují akceleraci, aerodynamická kola s vyšším profilem ušetří sílu při rychlé jízdě, ale na bočním větru jsou nestabilní. Bezdušová soustava, tubeless, snižuje riziko defektu a umožňuje jezdit s nižším tlakem, což zvyšuje pohodlí. Vyžaduje ale tmel a trochu zručnosti. Klasický plášť s duší je jednodušší a méně náročný na údržbu.</p>'
          + T(['Šířka pláště', 'Charakter', 'Použití'], [
              ['25 až 28 mm', 'rychlý, nízký odpor', 'závodní a rychlé silniční jízdy'],
              ['30 až 35 mm', 'pohodlný, univerzální', 'vytrvalostní silnice, mírný štěrk'],
              ['38 až 45 mm', 'stabilní na štěrku a drnu', 'gravel a cykloturistika'],
              ['nad 45 mm', 'terénní, tlumí hrbolky', 'náročný gravel a bikepacking']]) +
          '<p>Tlak v pláštích je třeba přizpůsobit hmotnosti, šířce a povrchu. Příliš vysoký tlak je nepohodlný a na nerovném povrchu zpomaluje, příliš nízký zvyšuje riziko proražení. Tabulky tlaků nabízejí výrobci plášťů a kol.</p>'
          '<h2>Triatlonová a časovkářská kola</h2>'
          '<p>V katalogu se objevují i triatlonová kola s nástavci na řídítka, aerodynamickými rámy a někdy se snímačem výkonu. Tyto stroje jsou vytvořeny pro jízdu osamoceně, bez drafování, a pro maximální aerodynamiku. Ve skupinové jízdě nejsou povolené a obtížně se s nimi manévruje. Pokud trénujete na triatlon, ale jezdíte ve skupině, je lepší silniční kolo s přídavnými nástavci.</p>'
          '<h2>Výbava a příslušenství</h2>'
          '<p>Ke kolu patří přilba, světla, zámek a základní nářadí. Přehled najdete v kategoriích <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/cyklo-svetla/">světla na kolo</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Pro dlouhé trasy se hodí <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a <a href="/cyklisticka-obuv/">cyklistické tretry</a>, které vyžadují kompatibilní <a href="/cyklo-pedaly/">pedály</a>. Pro kontrolu tempa slouží <a href="/cyklo-computery/">cyklopočítače a navigace</a>.</p>'
          '<p>Gravel a bikepacking potřebují brašny a nosiče, které najdete v kategorii <a href="/cyklo-tasky-a-nosice/">brašny, nosiče a košíky</a>. Bezpečnost zvyšují <a href="/cyklo-zamky/">zámky na kolo</a> a jasné <a href="/cyklo-svetla/">světlomety</a> pro jízdu za šera.</p>'
          '<h2>Pro koho které kolo</h2>'
          '<ul><li><strong>Začátečník s ambicí:</strong> hliníkový rám, kotoučové brzdy, kompaktní převody a pláště kolem třiceti milimetrů, které jsou pohodlné.</li>'
          '<li><strong>Závodník:</strong> lehký karbonový rám, aerodynamická kola, elektronické řazení a důraz na tuhost.</li>'
          '<li><strong>Cykloturista:</strong> gravel nebo vytrvalostní silniční kolo s úchyty pro blatníky a brašny.</li>'
          '<li><strong>Dojíždějící:</strong> robustní silniční turistické kolo nebo gravel, který zvládne i dlažbu a štěrk.</li>'
          '<li><strong>Triatlonista:</strong> aerodynamické kolo s nástavci, pokud trénuje hlavně samostatně.</li></ul>'
          '<h2>Kde jezdit a jak plánovat trasy</h2>'
          '<p>Gravel otevírá možnosti, které silniční kolo nenabízí, například polní a lesní cesty, štěrkové úseky nebo spojnice mezi vesnicemi bez silničního provozu. Při plánování trasy sledujte převýšení, typ povrchu a dostupnost občerstvení. Na delších výletech se vyplatí vozit dvě duše nebo sadu pro opravu bezdušového pláště, hustilku a multifunkční nářadí. U silničního kola stačí kratší sada, protože trasy vedou po údržbě silnic.</p>'
          '<p>Pro začátečníky je vhodné začít krátkými okruhy a postupně přidávat vzdálenost. Tělo si musí zvyknout na sed i na polohu rukou, jinak se objeví bolest zad, zápěstí a sedacích kostí. Kvalitní kalhoty s vložkou a rukavice zlepšují pohodlí zásadně.</p>'
          '<h2>Péče a servis</h2>'
          '<ul><li>Řetěz čistěte a mažte pravidelně, jinak se rychle opotřebí a poškodí i kazetu.</li>'
          '<li>Tlak v pláštích kontrolujte před každou delší jízdou, zvlášť když jste kolo dlouho nepoužívali.</li>'
          '<li>Brzdové destičky a kotouče kontrolujte vizuálně, destičky zbytečně nepřehřívejte dlouhým stálým brzděním.</li>'
          '<li>Karbonové součásti neutahujte nadměrnou silou, používejte momentový klíč a montážní pastu.</li>'
          '<li>Kolo skladujte v suchu a jednou ročně nechte provést kontrolu v servisu.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Výběr podle vzhledu a ceny bez ohledu na velikost rámu.</li>'
          '<li>Podcenění šířky pláště. Moderní trend je širší pláště a nižší tlak, které zlepšují pohodlí i přilnavost.</li>'
          '<li>Kupování závodního kola na turistiku, kde se hodí pohodlnější geometrie.</li>'
          '<li>Opomenutí kompatibility s pedály a tretrami nebo s nosiči a brašnami.</li>'
          '<li>Nákup bez prověření dostupnosti servisu a náhradních dílů.</li></ul>'
          '<p>Rozdíl mezi dvěma nabídkami téhož modelu bývá v modelovém roce, velikosti rámu, barvě a době dodání. Při porovnání nabídek proto hlídejte shodnou velikost a verzi výbavy.</p>',
    faq=[('Jaký je rozdíl mezi silničním a gravel kolem?', 'Silniční kolo má užší pláště a agresivnější polohu pro rychlost na asfaltu. Gravel má širší pláště, delší rozvor a pohodlnější geometrii pro štěrk a dlouhé trasy.'),
         ('Mám začít se silničním, nebo gravel kolem?', 'Když jezdíte hlavně po asfaltu, vyberte silniční vytrvalostní kolo. Pokud vedou trasy často po polňačkách a štěrku, gravel je univerzálnější a poslouží i jako dojíždění.'),
         ('Jak vybrat velikost rámu silničního kola?', 'Podle výšky postavy, délky rozkroku a délky paží. Tabulka výrobce poskytuje orientaci, přesné nastavení se ověřuje při zkušební jízdě nebo bike fittingu.'),
         ('Je karbonový rám lepší než hliníkový?', 'Karbon je lehčí a lépe tlumí vibrace, ale je dražší a citlivější na nárazy. Moderní hliníkové rámy jsou pro začátečníky a pro kondiční jízdu výbornou, odolnou volbou.'),
         ('Jsou kotoučové brzdy nutnost?', 'Dnes jsou standardem a lépe brzdí v dešti i při dlouhých sjezdech. Ráfkové brzdy najdete u starších a nejlevnějších modelů.'),
         ('Jaká šířka pláště je vhodná?', 'Pro rychlou jízdu na asfaltu kolem 25 až 28 milimetrů, pro pohodlí 30 až 35 a pro gravel 38 a víc. Širší plášť snese nižší tlak a více odpouští.'),
         ('Co znamená bezdušová soustava tubeless?', 'Plášť se utěsní na ráfku tmelem bez duše. Snižuje riziko defektů a umožňuje nižší tlak, ale vyžaduje kontrolu tmelu a trochu zručnosti při montáži.'),
         ('Hodí se triatlonové kolo do skupinové jízdy?', 'Ne. Nástavce na řídítka mají zlepšit aerodynamiku při samostatné jízdě. Ve skupině zhoršují ovladatelnost a bývají zakázány.'),
         ('Jaký převod zvolit do kopců?', 'Kompaktní sadu s malým předním převodníkem nebo kazetu se širokým rozpětím. Na gravelu se často využívá jediný přední převodník se širokou kazetou.'),
         ('Mohu na silniční kolo namontovat blatníky a nosič?', 'Jen když má rám úchyty pro blatníky a nosiče a dostatečný prostor pro pláště. U gravelových a turistických modelů je to obvyklé, u závodních ne.'),
         ('Jak často vyměňovat řetěz?', 'Podle najetých kilometrů a stavu. Opotřebovaný řetěz je třeba vyměnit včas, jinak ničí kazetu i převodník. Měří se speciální měrkou.')],
)

# ------------------------------------------------------------------ snowboardove-boty
NEW['snowboardove-boty'] = dict(long=True,
    title='Snowboardové boty: zapínání, tuhost, velikost, péče',
    desc='Snowboardové boty pánské, dámské a dětské: Boa, rychlošněrování, tuhost a velikost. Jak vybrat boty k vázání a porovnat obchody.',
    intro='<p>Snowboardová bota je kontaktní bod mezi tělem a prknem, takže ovlivňuje pohodlí, přesnost zatáčení i teplo v nohou. Na rozdíl od lyžařské je měkčí a nižší, aby kotník mohl pracovat. V kategorii Sporteky najdete pánské, dámské a dětské modely se šněrováním, rychlošněrováním a systémem Boa, včetně bot pro vázání Step On. Správný výběr stojí na třech věcech, tedy na velikosti a tvaru chodidla, na tuhosti odpovídající stylu jízdy a na zapínání, které zvládnete i v rukavicích na mrazu.</p>'
          '<p>Nabídky českých obchodů porovnáte u značek ' + B(('vans', 'Vans'), ('nitro', 'Nitro'), ('head', 'Head'), ('northwave', 'Northwave'), ('burton', 'Burton'), ('ride', 'Ride'), ('nidecker', 'Nidecker'), ('k2', 'K2')) +
          '. Ke správné botě patří <a href="/snowboardova-vazani/">snowboardová vázání</a> a <a href="/snowboardy/">snowboardy</a>.</p>',
    guide='<h2>Jak má snowboardová bota sedět</h2>'
          '<p>Bota je dobře zvolená, když drží patu na místě, prsty se jí lehce dotýkají špičky a noha se nehýbe ani při předklonu. Mírný pohyb prstů je žádoucí, protože nohy v zimě potřebují prokrvení. Příliš velká bota způsobuje zdvihání paty, bolest kotníků a ztrátu kontroly nad hranou. Příliš těsná bota tlačí, zhoršuje prokrvení a nohy rychleji mrznou.</p>'
          '<p>Vložka, která je v botě, se po několika dnech rozšlape a bota povolí. Prodavači často radí volit o něco těsnější verzi, pokud sedí bez bolesti. Nová bota má sedět pevně, ale ne bolestivě. Vyzkoušejte ji ve stejných ponožkách, v jakých budete jezdit.</p>'
          '<h2>Zapínání: šněrování, rychlé šněrování, Boa a Step On</h2>'
          + T(['Zapínání', 'Přednosti', 'Slabiny'], [
              ['Klasické šněrování', 'jemné nastavení, nízká cena, snadná výměna tkaniček', 'dotahuje se pomalu, v rukavicích je to těžké'],
              ['Rychlé šněrování TLS a podobné', 'jedním tahem se dotáhne celá bota', 'méně nastavení v jednotlivých zónách'],
              ['Boa kolečko', 'plynulé dotažení, funguje v rukavicích, dá se rozdělit na zóny', 'při poruše vyžaduje výměnu dílu'],
              ['Step On', 'nastupujete bez sklonění, rychlý zámek', 'potřebuje kompatibilní vázání a boty']]) +
          '<p>Pro začátečníky je nejsnazší rychlé šněrování nebo Boa, protože se dotahuje bez námahy. Klasické šněrování mají rádi jezdci, kteří chtějí přesné vedení a snadnou opravu. Systém Step On je novější a hodí se pro ty, kdo nechtějí sedět ve sněhu při obouvání. U Step On musí být vázání i bota od kompatibilních výrobců, takže nejde kombinovat libovolné značky.</p>'
          '<p>Velkou výhodou kolečka je rychlost. Při pádu nebo kontaktu s ledem se lanko může poškodit, proto se doporučuje mít náhradní lanko nebo vědět, jak se dá bota provizorně dotáhnout. Moderní boty mají často dvě kolečka, jedno na nohu a jedno na lýtko, a tak umožňují nastavit tlak zvlášť.</p>'
          '<h2>Tuhost: měkké, střední, tuhé boty</h2>'
          '<p>Tuhost se obvykle udává na stupnici od jedné do deseti, ale každý výrobce ji pojímá jinak. Obecně platí, že měkká bota se hodí do parku a pro začátečníky, dává volnost a odpouští chyby. Střední tuhost je univerzální pro celodenní jízdu na sjezdovce a částečně v neupraveném terénu. Tuhé boty vyhovují freeridu, rychlému carvingu a velkým skokům, protože lépe přenášejí sílu na hranu.</p>'
          + T(['Styl jízdy', 'Doporučená tuhost', 'Proč'], [
              ['Začátečník na sjezdovce', 'měkká až střední', 'pohodlí a odpouštění chyb při učení'],
              ['Freestyle a park', 'měkká až střední', 'volnost při skocích a trikách'],
              ['Univerzální jízda', 'střední', 'kompromis pohodlí a přesnosti'],
              ['Freeride a rychlá jízda', 'střední až tuhá', 'rychlejší odezva na hranu a lepší opora'],
              ['Carving', 'tuhá', 'přesný přenos síly při vysokých rychlostech']]) +
          '<h2>Velikost a vázání</h2>'
          '<p>Velikost bot se udává v EU, US nebo v mondopointech, což je délka chodidla v centimetrech. Nejspolehlivější je změřit chodidlo a porovnat s tabulkou výrobce. Snowboardové boty se vyrábějí v celých i půlových velikostech a značky se v tabulkách liší. Například Vans bývají širší, zatímco jiné značky mají štíhlejší střih. Při koupi na dálku zkontrolujte délku stélky.</p>'
          '<p>Důležitá je shoda s vázáním. Vázání mají velikostní rozpětí a bota musí do něj zapadnout bez vůle. Pokud je bota na hranici, zkontrolujte, zda špička nebo pata nepřesahují okraj vázání nebo prkna. Příliš vyčnívající špička způsobuje takzvaný toe drag, kdy se bota při zatáčení dotýká sněhu a může způsobit pád. Pro větší boty a širší stopu se vybírají širší snowboardy, viz <a href="/snowboardy/">snowboardy</a>.</p>'
          '<h2>Pánské, dámské a dětské boty</h2>'
          '<p>Dámské modely mají užší patu, vyšší lýtko a nižší tuhost vzhledem k nižší hmotnosti. Pánské boty jsou širší a tužší. Unisex modely se dají vybrat podle tvaru nohy. Dětské boty musí být měkké, a protože děti rychle rostou, volí se správná velikost nebo maximálně o půl čísla větší. Dětské modely mívají rychlé šněrování nebo jednoduchý uzávěr, který zvládne i dítě bez pomoci dospělého.</p>'
          '<h2>Teplo, vložka a ponožky</h2>'
          '<p>Teplo nohou zajišťují vložky, izolace a ponožky. Vyjímatelná vložka je lehčí, dá se vysušit a při opotřebení vyměnit. Termoformovatelné vložky se přizpůsobí tvaru nohy po zahřátí, což zlepšuje sedění. U snowboardových bot se doporučují tenké nebo střední ponožky z vlny nebo syntetiky, ne bavlněné, které nasávají vlhkost. Přečtěte si kategorii <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, která obsahuje podobné výrobky použitelné i při snowboardingu, a <a href="/merino-doplnky/">merino doplňky</a>.</p>'
          '<p>Ruce a hlava patří k teplu také. Zkontrolujte <a href="/lyzarske-rukavice/">lyžařské rukavice a palčáky</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/lyzarske-bryle/">lyžařské brýle</a>, které se používají i na snowboardu.</p>'
          '<h2>Co všechno patří k výbavě</h2>'
          '<ul><li><strong>Oblečení:</strong> bundy a kalhoty s membránou, viz <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a> a <a href="/lyzarske-kalhoty/">kalhoty</a>.</li>'
          '<li><strong>Ochrana:</strong> chrániče zápěstí, kolen a zadku. Najdete je v kategorii <a href="/snowboardove-chranice/">chrániče páteře a boků</a>.</li>'
          '<li><strong>Termoprádlo:</strong> funkční vrstva pod bundu v <a href="/lyzarske-termopradlo/">lyžařském termoprádle</a>.</li>'
          '<li><strong>Údržba prkna:</strong> <a href="/lyzarske-vosky/">vosky a mazání</a> pro rychlejší skluz.</li>'
          '<li><strong>Doprava:</strong> <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a> ochrání vybavení při cestě.</li></ul>'
          '<h2>Vans, Burton, Nitro a další: čeho si všímat u značek</h2>'
          '<p>Značky mají vlastní filozofii střihu. Vans nabízejí oblíbené modely s širším tvarem a zaměřením na park a street, Nitro a Burton pokrývají široké spektrum od začátečníků po pokročilé, Head a Northwave nabízejí systém Boa a pohodlné modely pro celodenní jízdu. Ride a Nidecker se zaměřují na kvalitní konstrukci a vysokou přesnost. Značka sama o sobě nic nezaručuje, důležitější je střih, který vám sedí.</p>'
          '<h2>Boty podle terénu a sezony</h2>'
          '<p>V parku a na malých skocích potřebujete měkčí boty s dobrým tlumením dopadu, protože se opakovaně přistává na tvrdý sníh. Na freeridu v hlubokém sněhu oceníte vyšší manžetu, tužší podporu kotníku a lepší izolaci, protože se často stojí a čeká. Na upravených sjezdovkách přes celý den se hodí střední tuhost s pohodlným přizpůsobením, aby se noha neunavila. Pro jarní lyžování, kdy je sníh mokrý a teploty vyšší, stačí tenčí izolace, kdežto za mrazu se sluší mít silnější vložku.</p>'
          '<p>Na vlhkém sněhu se vyplatí hydrofobní svršek a přelepené švy, které brání prosáknutí vodou. Doporučuje se také zkontrolovat gumovou podrážku, jejíž vzor ovlivňuje chůzi po zledovatělých cestách k lanovce. Nepříjemné je, když bota klouže na dlaždicích v areálu, proto je jemný vzorek a měkčí guma výhoda.</p>'
          '<h2>Jak boty zapadají do vázání</h2>'
          '<p>Rozhodující je vztah mezi botou, vázáním a prknem. Vázání drží botu pod patou, v oblasti nártu a přes špičku, a pokud bota nesedí, tlak se přenáší špatně a objeví se bolest chodidla nebo kotníku. Před sezonou zkontrolujte, zda se stopa boty vejde mezi pásky a že páska nepřetlačuje šněrování. Boty s velkým Boa kolečkem někdy potřebují jiné nastavení pásku, aby nedocházelo k tlaku na kolečko. Úhly vázání a postoj, tedy pravá noha vpředu nebo vzadu, jsou osobní věc, kterou si každý vyzkouší na sněhu.</p>'
          '<h2>Péče o boty</h2>'
          '<ul><li>Po jízdě vyndejte vložky a nechte boty i vložky oschnout při pokojové teplotě. Radiátor, kamna ani sušič vlasů nepoužívejte.</li>'
          '<li>Vnější část otřete vlhkým hadříkem, aby se odstranila sůl a špína ze sjezdovky.</li>'
          '<li>Šněrování nebo lanko Boa pravidelně kontrolujte, v případě poškození je včas vyměňte.</li>'
          '<li>Boty uchovávejte v suchu a čistotě mimo přímé slunce, nejlépe ve vaku na boty.</li>'
          '<li>Na konci sezony nechte boty úplně vyschnout a uskladněte je s papírem uvnitř, aby si udržely tvar.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupování větších bot do zásoby, které pak způsobí zdvihání paty.</li>'
          '<li>Podcenění tuhosti: příliš měkká bota nedrží pozici při rychlé jízdě, příliš tuhá unavuje začátečníka.</li>'
          '<li>Neověření kompatibility s vázáním, hlavně u systému Step On.</li>'
          '<li>Výběr jen podle vzhledu bez vyzkoušení tvaru.</li>'
          '<li>Použití bavlněných ponožek, které způsobí vlhko a chlad.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Ve výsledcích sledujte velikost a modelový rok. Starší kolekce bývají výhodné, ale jejich velikosti se rychle vyprodají. Při koupi online si ověřte možnost výměny velikosti, protože bota nemusí sedět napoprvé. Stejný model se může prodávat pod jinou barvou v různých obchodech, ale konstrukce zůstává stejná. Pokud potřebujete vybírat i vázání, porovnejte s botou jeho velikostní rozsah, aby nedošlo k nekompatibilitě. Nabídka bot obsahuje i speciální modely pro splitboard nebo skialpinismus. Takové boty vyžadují vázání pro stejnou techniku, proto si ověřte, k čemu jsou určeny.</p>',
    faq=[('Jak poznám, že mi snowboardová bota sedí?', 'Pata zůstává na místě, prsty se lehce dotýkají špičky a noha se nehýbe při předklonu. Bota nesmí tlačit ani bolet, mírný pohyb prstů je v pořádku.'),
         ('Jaké zapínání vybrat?', 'Pro pohodlí a rychlost Boa nebo rychlé šněrování, pro jemné nastavení klasické šněrování. Step On vyžaduje kompatibilní vázání.'),
         ('Jaká tuhost je vhodná pro začátečníka?', 'Měkká až střední. Bota odpouští chyby a nezatěžuje kotník, což usnadňuje učení.'),
         ('Mohu použít lyžařské ponožky na snowboard?', 'Ano, snowboardové ponožky jsou často podobné lyžařským. Vybírejte tenké nebo střední ponožky z vlny či syntetiky a vyhněte se bavlně.'),
         ('Jak velkou botu koupit dítěti?', 'Dítě potřebuje pohodlí a teplo, takže mírná rezerva ve špičce je přijatelná. Příliš velká bota ale ztrácí kontrolu, proto neměňte velikost o víc než půl čísla.'),
         ('Co je toe drag?', 'Situace, kdy špička boty přesahuje okraj prkna a při zatáčení zavadí o sníh. Řeší se kombinací šířky prkna, úhlů vázání a velikosti boty.'),
         ('Hodí se dámské boty pro ženy se širší nohou?', 'Záleží na tvaru nohy. Dámské modely bývají užší, takže ženy se širší nohou mohou zkusit unisex nebo pánský střih v malé velikosti.'),
         ('Jak sušit snowboardové boty?', 'Vyjměte vložky a vysušte je při pokojové teplotě. Radiátor poškodí lepené spoje a materiály, jejich životnost se zkracuje.'),
         ('Jsou boty Vans vhodné pro celodenní jízdu?', 'Mnoho modelů je určeno pro univerzální jízdu a park. Střih je často širší, což se hodí pro jezdce s širší nohou. Pro rychlou jízdu hledejte tužší model.'),
         ('Dá se kombinovat jakákoli bota s libovolným vázáním?', 'Většinou ano pro klasické systémy, pokud velikost boty zapadá do rozsahu vázání. U Step On musí být kompatibilní jak bota, tak vázání.'),
         ('Jak často vyměnit boty?', 'Když se rozbije vložka, přestane držet pata nebo bota ztratí oporu. Při pravidelné jízdě výdrž odpovídá několika sezonám podle intenzity.')],
)
