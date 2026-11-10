"""sporteka.cz — wave 24n (5. 11. 2026): long texts for bmx-a-dirt-kola, rybarske-stany, baletni-obuv, nakladni-elektrokola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bmx-a-dirt-kola
NEW['bmx-a-dirt-kola'] = dict(long=True,
    title='BMX a dirt kola: rám, převod, velikost a výběr',
    desc='BMX a dirt kola na triky, skatepark i pumptrack. Jak vybrat velikost rámu, převod, brzdy a materiál a porovnat nabídky českých obchodů.',
    intro='<p>BMX je malé, pevné a jednoduché kolo s dvacetipalcovými koly, postavené pro skoky, triky a jízdu na dráze. Na rozdíl od běžného kola nemá přehazovačku ani odpružení a každý díl je dimenzovaný na dopady. Sporteka porovnává nabídky českých obchodů u modelů pro děti, teenagery i dospělé, od lehčích hliníkových rámů po ocelové kousky na parky. Tato stránka vysvětluje, čím se jednotlivé stavby liší, jak zvolit velikost podle výšky jezdce a na co si dát pozor u levnějších kol.</p>'
          '<p>V nabídce se objevují značky ' + B(('khebikes', 'Khebikes'), ('hiland', 'Hiland'), ('galaxy', 'Galaxy')) +
          '. Pro porovnání s jinými malými koly se podívejte na <a href="/detska-kola-20-palcu/">dětská kola 20 palců</a> a <a href="/detska-kola/">dětská kola</a>, pro jízdu po městě na <a href="/mestska-kola/">městská kola</a>.</p>',
    guide='<h2>Co je BMX a v čem se liší od běžného kola</h2>'
          '<p>Zkratka označuje bicycle motocross, tedy sport, který vznikl z napodobování motokrosu na kolech. Dnes pod ním najdete několik disciplín s odlišnými nároky na stavbu stroje. Společné mají jedno: kolo je krátké, nízké a ovladatelné, takže jezdec s ním může v letu pohybovat, otáčet řidítky a přistávat na obou kolech. Žádné zbytečné příslušenství, žádný nosič, blatníky ani světla, protože by se při prvním pádu ulomily.</p>'
          '<p>Nejviditelnější rozdíl je v převodu. Většina BMX má jedinou rychlost a zadní kolo se otáčí volnoběhem nebo kazetovou hlavou. Jednoduchost zajišťuje, že se nic nedeformuje a že se kolo dá opravit klíčem a imbusem. Nevýhodou je, že na delších stoupáních nebo při dlouhé jízdě po rovině se unavíte dřív než na kole s převodníky, proto BMX není ideální dopravní prostředek.</p>'
          '<h2>Disciplíny: street, park, dirt, flatland a race</h2>'
          '<p>Každá disciplína má trochu jiné nároky, i když kolo na sobě nese stejnou silueta. Při výběru se vyplatí vědět, kde chcete jezdit nejčastěji, protože od toho se odvíjí hmotnost, výbava a tuhost rámu.</p>'
          + T(['Disciplína', 'Typ povrchu', 'Na co dbát při výběru'], [
              ['Street', 'schody, zídky, chodníky, zábradlí', 'odolný rám, pevná hlava řízení, kolíky na osách'],
              ['Park a skatepark', 'betonové mísy, rampy, box jumpy', 'lehčí rám, tuhé vidlice, kvalitní ložiska'],
              ['Dirt', 'hliněné hrbolky a odrazové můstky', 'robustní kola, širší pláště, často přední brzda místo zadní'],
              ['Flatland', 'rovná hladká plocha', 'krátký rám, speciální geometrie, kolíky na obou stranách'],
              ['Race', 'dráha s klopenými zatáčkami a vlnami', 'lehký hliníkový rám, delší zadní stavba, vysoké plášťové tlaky'],
              ['Univerzální', 'hřiště, pumptrack, chodníky', 'vyvážený rám střední hmotnosti, bezpečné brzdy']]) +
          '<p>Většina kol v kategorii je navržená jako univerzální BMX pro začátečníky a pokročilejší rekreační jezdce. Závodní dráhové modely a speciální flatlandové rámy jsou spíš výjimka a jejich výběr stojí za rozhovor s trenérem klubu. Pumptrack, tedy uzavřený okruh vln a zatáček, zvládne běžné BMX i bez triků a je dobrým místem, jak získat cit pro rovnováhu.</p>'
          '<h2>Rám: ocel, hliník a hmotnost</h2>'
          '<p>Rámy se nejčastěji vyrábějí z oceli nebo z hliníkové slitiny. Ocelový rám je těžší, ale snáší tvrdé přistání, dá se při malé deformaci narovnat a opravit svářečem. Hliník je lehčí, hůř se opravuje a při vážném úderu nebo ohybu může prasknout. Hmotnost kola s ocelovým rámem se pohybuje kolem dvanácti kilogramů, hliníkové modely bývají o kilo až dvě lehčí, což se projeví při skocích a při nošení po schodech.</p>'
          '<p>Důležitý je také tvar a způsob svaření trubek. Silnější výztuhy u hlavy řízení a pod sedlem prozrazují rám určený pro zátěž. Název v nabídce často uvádí údaj o hmotnosti a materiálu, což usnadňuje rychlé srovnání. U dospělých a starších teenagerů se vyplatí sáhnout po rámu s delší horní trubkou, protože s ní se jezdec nepřetěžuje při dlouhých jízdách.</p>'
          '<h2>Velikost: palce kol a délka horní trubky</h2>'
          '<p>Většina BMX má kola s průměrem dvacet palců a to platí pro děti od zhruba osmi let po dospělé. Rozhodující není průměr kol, ale délka horní trubky, tedy vzdálenost mezi hlavou řízení a sedlovou trubkou. Označuje se čísly, třeba 18,5 až 21 palce, a podle ní se vybírá rám podle výšky jezdce. Příliš krátký rám nutí k zahrbené poloze, příliš dlouhý ztěžuje kontrolu při skoku.</p>'
          '<ul><li><strong>Menší děti:</strong> kolo s krátkou horní trubkou a nižším sedlem. Pro nejmenší jezdce se hodí spíš <a href="/detska-kola-16-palcu/">dětská kola 16 palců</a> nebo <a href="/odrazedla/">odrážedla</a>.</li>'
          '<li><strong>Mladší školáci a teenageři:</strong> rám střední délky s možností zvednout sedlo. Roste se rychle, takže pomůže rezerva v nastavení.</li>'
          '<li><strong>Dospělí:</strong> delší rám, často označený jako XL nebo pro dospělé, s vyšší hlavou řízení a delšími klikami.</li>'
          '<li><strong>Větší kola:</strong> v nabídce se občas objeví i model s čtyřiadvacetipalcovými koly, který nabízí delší základnu a hodí se pro vyšší jezdce nebo pro pohodovější jízdu po městě.</li></ul>'
          '<p>Přesnou volbu nejlépe ověříte tak, že se na kolo postavíte a zkusíte, zda se kolena nedotýkají řidítek při zatáčení. Přehled větších dětských modelů najdete v kategorii <a href="/detska-kola-24-palcu/">dětská kola 24 palců</a>.</p>'
          '<h2>Převody, kliky a brzdy</h2>'
          '<p>Jedna rychlost má poměr mezi předním a zadním ozubeným kolem, který se udává jako dvě čísla, například 25 zubů vpředu a 9 vzadu. Vyšší poměr znamená rychlejší jízdu po rovině a těžší rozjezd, nižší poměr dává snazší rozjezd a lepší stoupání. Pro začátečníky a pumptrack je lepší střední poměr, pro dráhové závody se naopak používá náročnější převod s vyšší maximální rychlostí.</p>'
          '<p>Kliky bývají tříkusové nebo jednodílné ocelové. Tříkusové jsou v běžné nabídce častější, mají střední osu s ložisky a dají se rozebrat při opravě. Kolo bez brzdy, takzvaný fixed styl, je oblíbený pouze mezi pokročilými street jezdci a pro běžný provoz nedoporučujeme. Zadní brzda s takzvaným rotorem (gyro) vede lanko přes otočnou spojku a umožňuje točit řidítky dokola bez zamotání lanka. Jednodušší modely mají lanko vedené klasicky, což funguje, jen se omezuje úhel otáčení. Některá kola mají i přední brzdu, ta se hodí především na dirt a rychlejší zatáčky.</p>'
          '<h2>Ráfky, pláště, pedály a další díly</h2>'
          '<p>Pláště BMX jsou kratší a širší než silniční, s menším vzorkem pro skatepark a výraznějším pro hlínu. Tlak se volí podle povrchu: tvrdší pláště valí lépe po betonu, měkčí lépe drží v hlíně a tlumí údery. Ráfky jsou dvoustěnné, aby vydržely dopady a vychýlení. Dbejte na to, aby měly dostatečný počet špic, protože právě drátěné kolo se při tvrdém dopadu nejčastěji zdeformuje.</p>'
          '<p>Pedály jsou plošinové, často nylonové nebo kovové s kolíky pro lepší sevření boty. Sedlo bývá malé, nízké a tvrdé. Zvedat ho je nutné spíš pro pohodlí než pro efekt, protože při tricích jezdec většinou stojí na pedálech. Kolíky na osách kol slouží pro triky na zábradlí a zídkách, jejich přítomnost zvyšuje zábavu, ale také opotřebení dílů.</p>'
          '<h2>Výbava a bezpečnost</h2>'
          '<p>BMX je kolo rizikové už tím, jak se používá. Základem je pevná helma a rukavice. Pro park a dirt se přidávají chrániče kolen, loktů a zápěstí, a pokud někdo skáče vyšší překážky, pomáhá i chránič páteře. Vhodné jsou boty s plochou podrážkou, které se dobře drží na pedálech. Přehled ochranných pomůcek najdete v kategoriích <a href="/chranice-a-helmy/">chrániče a helmy</a>, <a href="/mtb-a-integralni-helmy/">MTB a integrální helmy</a> a <a href="/cyklisticke-helmy/">cyklistické helmy</a>.</p>'
          '<p>U dětí je zásadní správná velikost helmy a utažení pásku. Každému jezdci pomůže, když se triky učí postupně, na plochém terénu, a ne rovnou na rampě. První skok je lepší absolvovat s dospělým, který hlídá bezpečný prostor kolem.</p>'
          '<h2>Údržba a časté závady</h2>'
          '<p>BMX je relativně nenáročné na servis, ale pádům a nárazům se neubrání. Po každé delší jízdě zkontrolujte šrouby na řidítkách, hlavě řízení a pedálech. Pokud se kolo houpe nebo drnčí, bývá to uvolněná hlava řízení nebo ložisko. Utáhněte matice kol, protože se při skocích lehce povolují.</p>'
          '<ul><li><strong>Řetěz:</strong> mazat podle potřeby a udržovat správné napnutí. Příliš volný řetěz spadne, příliš napnutý ničí ložiska.</li>'
          '<li><strong>Pláště:</strong> pravidelně kontrolovat tlak a stav gumy, protože propíchnutí o hřeb na hřišti se stává často.</li>'
          '<li><strong>Špice:</strong> uvolněné nebo prasklé zjistíte tak, že se zadní kolo při roztočení houpe ze strany na stranu.</li>'
          '<li><strong>Brzdové lanko:</strong> při prověšení ho napnout a zkontrolovat, zda neprotírá obal.</li></ul>'
          '<p>Základní nářadí a pumpy najdete v kategoriích <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> a <a href="/cyklo-udrzba/">údržba kol</a>. Díly jako pedály, řetězy a pláště jsou ve skupinách <a href="/cyklo-pedaly/">pedály</a> a <a href="/cyklo-kola-a-rafky/">kola a ráfky</a>.</p>'
          '<h2>Na co si dát pozor u levnějších kol</h2>'
          '<p>Nejlevnější BMX z hypermarketů mívají těžký rám, měkké ráfky a ložiska bez těsnění, takže po několika týdnech skatepark začnou vrzat a drhnout. Pokud dítě chce jezdit pravidelně, vyplatí se zvolit kolo od specializovaného výrobce s dostupnými náhradními díly. Název produktu často prozradí vybavení: zmínka o hliníkovém rámu, celkové hmotnosti a počtu palců usnadní srovnání. U kol ze zahraničních e-shopů ověřte, zda je k dispozici záruka a servis v ČR.</p>'
          '<p>Důležité je i složení balíku. Některé nabídky obsahují zvonek, blatníky nebo odrazky, což je u dětského kola pro silniční provoz potřeba. Pro skatepark jde o zbytečnost a lépe je ji sundat, aby se nepoškodila.</p>'
          '<h2>Pro koho je BMX vhodné</h2>'
          '<ul><li><strong>Začátečník od školního věku:</strong> univerzální ocelový model s tříkusovými klikami a dobrou zadní brzdou. Hodí se na hřiště a chodníky.</li>'
          '<li><strong>Teenager do skateparku:</strong> lehčí hliníkový rám a kvalitní ložiska, kolíky podle toho, jak moc chce jezdit po zábradlích.</li>'
          '<li><strong>Dospělý rekreační jezdec:</strong> delší rám, vyšší hlava řízení a delší kliky. Může jít o zábavu pro pumptrack nebo nostalgii.</li>'
          '<li><strong>Dojíždění:</strong> BMX na delší trasu nestačí. Zvažte <a href="/mestska-kola/">městská kola</a>, <a href="/skladaci-kola/">skládací kola</a> nebo <a href="/kolobezky/">koloběžky</a>.</li>'
          '<li><strong>Freestyle na jiných strojích:</strong> alternativou jsou <a href="/freestyle-kolobezky/">freestyle koloběžky</a> nebo <a href="/skateboardy/">skateboardy</a>.</li></ul>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>V kategorii se sbírají nabídky několika českých obchodů a každé kolo vidíte s cenami všech prodejců a dostupností. Sledujte hmotnost, materiál rámu, počet palců a rozměr horní trubky. Pokud název některé údaje neuvádí, ověřte je na stránce obchodu. Před koupí si vždy zkontrolujte, zda je kolo skládané z výroby nebo ho budete muset sestavit sami, protože nesprávně utažená hlava řízení je častý důvod pádu.</p>',
    faq=[
        ('Jakou velikost BMX zvolit podle výšky dítěte?', 'Rozhoduje délka horní trubky rámu, ne velikost kol. Menší děti si vystačí s kratším rámem a nižší polohou sedla, vyšší teenageři a dospělí potřebují delší horní trubku. Při zkoušce by se kolena neměla dotýkat řidítek a zadní část těla se musí pohodlně pohybovat nad sedlem.'),
        ('Je lepší ocelový, nebo hliníkový rám?', 'Ocel je těžší a odolnější proti opakovaným nárazům, hliník je lehčí a hodí se pro skoky a závody. Při velmi tvrdém pádu se hliník hůř opravuje. Pro začátečníky a dětské jezdce je rozumnou volbou ocel, pro zkušenější jezdce hliník.'),
        ('Dá se s BMX jezdit po silnici a do školy?', 'Dá, ale pohodlné to není. Kolo má jednu rychlost, malá kola a pevnou geometrii, takže delší trasy jsou namáhavé. Pro každodenní dojíždění je praktičtější městské nebo skládací kolo.'),
        ('Potřebuje BMX brzdu?', 'Pro běžné rekreační použití ano, zejména pro děti a dospělé na veřejných cestách. Zadní brzda s rotorem (gyro) umožňuje otáčet řidítky bez zamotání lanka. Kola bez brzdy jsou určená pro zkušené street jezdce.'),
        ('Co jsou kolíky a potřebuji je?', 'Kolíky jsou trubičky nasazené na osy kol, po kterých se dá klouzat na zábradlích a zídkách. Pro začátečníka nejsou nutné a při špatném odrazu mohou zranit holeň. Nejprve si osvojte základy jízdy a skoků.'),
        ('Jak často mám kolo kontrolovat?', 'Šrouby na řidítkách, matice kol a pedály zkontrolujte před každou delší jízdou, protože se při skocích uvolňují. Jednou za několik týdnů zkontrolujte řetěz, tlak v pláštích a stav špic. Dětem pomůže, když to dělají společně s dospělým.'),
        ('Jakou helmu a chrániče si vzít?', 'Základem je dobře padnoucí helma a rukavice. Do skateparku a na dirt přidejte chrániče kolen, loktů a zápěstí, při vyšších skocích i chránič zad. Helmu vyměňte po větším pádu, i když na ní nejsou viditelné škody.'),
        ('Hodí se BMX pro dospělého?', 'Ano, existují kola s delším rámem a vyšší hlavou řízení označená pro dospělé. Jsou vhodná na pumptrack, skatepark a rekreační triky. Při výběru ověřte maximální nosnost a rozměry rámu.'),
        ('Proč mají některá BMX 24 palců a většina jen 20?', 'Větší kola dávají delší základnu a stabilnější jízdu, hodí se pro vyšší jezdce nebo pro méně agresivní užití. Dvacetipalcová kola jsou ovladatelnější, lehčí a mají větší nabídku dílů, proto jsou mnohem častější.'),
        ('Co zvolit, když dítě začíná a ještě neumí jezdit?', 'Nejprve odrážedlo nebo dětské kolo s menšími koly a pomocnými kolečky, až poté BMX. Dítě by mělo bezpečně brzdit a udržet rovnováhu, než ho vezmete na hřiště s rampami.'),
    ])

# ------------------------------------------------------------------ rybarske-stany
NEW['rybarske-stany'] = dict(long=True,
    title='Rybářské stany a bivaky: typy, látka, podlážka',
    desc='Rybářské stany, bivaky na kapry a podlážky. Jak vybrat velikost, vodní sloupec, konstrukci a doplňky a porovnat nabídky českých obchodů.',
    intro='<p>Rybářský stan je přístřeší, které přežije dlouhé sezení u vody, déšť, vítr i ranní mlhu. Podstatné je, aby se v něm dalo pohodlně sedět u prutů, spát na lehátku a hlavně aby šel rychle postavit a po týdnu u jezera snadno sbalit. Sporteka porovnává nabídky českých obchodů u klasických bivaků, kaprařských stanů s čelní stěnou, malých vaků a stanů pro dvě až tři osoby, ale i podlážek a dalších dílů. Tato stránka vysvětluje, jak se jednotlivé typy liší a co kontrolovat před koupí.</p>'
          '<p>V nabídce najdete značky ' + B(('caperlan', 'Caperlan'), ('vidaxl', 'Vidaxl'), ('trimm', 'Trimm'), ('sir-joseph', 'Sir Joseph'), ('solognac', 'Solognac')) +
          '. K výbavě se hodí <a href="/rybarske-spacaky/">rybářské spacáky</a>, <a href="/rybarske-tasky/">rybářské tašky</a> a <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>',
    guide='<h2>Jaké druhy rybářských stanů existují</h2>'
          '<p>Nabídka se dělí podle toho, jak dlouho a jak daleko od auta rybář zůstává. Nejmenší bivak postačí na noc s lehkým vybavením, zatímco velký kaprařský stan unese lehátko, stůl i vařič. Každý typ má svá specifika a výběr podle stylu rybaření ušetří zbytečné peníze.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Bivak (bivvy)', 'nízký kupolový stan s předsíní', 'jedna až dvě osoby, noční lov kaprů'],
              ['Bivak s čelní stěnou', 'odnímatelná přední stěna, větší vstup', 'lov z břehu, pozorování prutů'],
              ['Kaprařský stan s přístřeškem', 'prostornější, otevřený přední díl', 'delší výjezdy, spaní i vaření v zázemí'],
              ['Týpí a bushcraft stan', 'kuželový tvar, jeden pól uprostřed', 'nenáročný pobyt, přírodní styl'],
              ['Žďárský vak a závěsný stan', 'lehký přístřešek nebo bivakovací vak', 'dojíždění pěšky nebo na kole'],
              ['Turistický stan', 'nízký lehký stan do dvou osob', 'krátké výjezdy a rybaření na cestách'],
              ['Podlážka a doplňky', 'tuhá nebo textilní podlaha', 'ochrana proti vlhku a prachu']]) +
          '<p>Kategorie zahrnuje i jednotlivé díly, například podlážky určené do konkrétních modelů bivaků. Při vyhledávání proto dávejte pozor, zda opravdu kupujete celý stan, nebo jen doplněk, protože názvy jsou si podobné.</p>'
          '<h2>Konstrukce a rychlost stavění</h2>'
          '<p>Rybář stan staví často za šera, v dešti a s mokrýma rukama, proto je zásadní jednoduchost. Pop-up modely se rozevřou jedním pohybem a drží tvar díky pružné obruči. Klasické kupole mají tyče z hliníku nebo sklolaminátu, které se provlékají tunýlky. Rychlost stavění vyzkoušejte doma na zahradě, ne poprvé na břehu.</p>'
          '<ul><li><strong>Tyčová kupole:</strong> stabilnější ve větru, ale stavba trvá déle. Hliníkové tyče jsou lehčí a pevnější než sklolaminát.</li>'
          '<li><strong>Pop-up kostra:</strong> postavíte za minutu, hůř ale vzdoruje silnému větru a těžko se skládá bez praxe.</li>'
          '<li><strong>Tunýlky a pásky:</strong> kvalitní tunýlky mají pevné šití, aby tyč nepraskla látku.</li>'
          '<li><strong>Kolíky a odtahy:</strong> každý stan bez pořádného ukotvení vítr odfoukne, i když váží několik kilogramů.</li></ul>'
          '<h2>Látka, vodní sloupec a vodotěsné švy</h2>'
          '<p>Plachta stanu bývá z polyesteru nebo polyamidu s polyuretanovým či silikonovým povrchem. Vodní sloupec udává, jak velký tlak vody látka vydrží, než propustí první kapky. Čím vyšší hodnota, tím lepší ochrana při vytrvalém dešti, ale vyšší sloupec samo o sobě neznamená kvalitní stan. Rozhodují také švy: pokud nejsou přelepené, voda jimi proniká i přes nejlepší látku.</p>'
          '<p>Dalším faktorem je prodyšnost. Nepropustný stan bez větrání zapaří a uvnitř se sráží kondenzace, takže mokrý spacák se špatně suší. Proto kvalitní bivaky mají větrací okénka, kterými proudí vzduch, a komínek nad otvorem. Při chladných nocích u vody dává dobrý smysl dvouplášťová konstrukce, kde vnitřní stan zajišťuje komfort a vnější plášť odvádí déšť.</p>'
          '<h2>Barva a nenápadnost</h2>'
          '<p>U rybářských stanů hraje roli maskování. Olivová, hnědá a tmavě zelená barva splyne s břehem a neplaší ryby, zároveň v krajině působí méně rušivě. Bílé a výrazné stany zvolte jen tam, kde potřebujete být viditelní, třeba na turistických trasách. Barva plochy ovlivňuje i teplotu uvnitř: tmavý stan se na slunci zahřeje víc.</p>'
          '<h2>Velikost a vnitřní prostor</h2>'
          '<p>Údaj o počtu osob je orientační. Rybář nespí jen na zemi, ale potřebuje lehátko, boxy, stoleček a vedle prutů místo na podběrák. Pro jednoho rybáře s lehátkem se hodí stan pro dvě osoby, pro dva rybáře minimálně pro tři. Ověřte rozměry podlahy a výšku uprostřed: aby šlo u lehátka sedět s nohama dole, potřebujete víc než metr výšky.</p>'
          '<ul><li><strong>Samotář na noc:</strong> malý bivak se širokým vstupem, kde se vejde lehátko a pár věcí.</li>'
          '<li><strong>Dva rybáři na víkend:</strong> větší bivak s předsíní nebo kaprařský stan s přístřeškem.</li>'
          '<li><strong>Rodinný výlet k vodě:</strong> prostornější stan, případně kombinace s <a href="/pristresky-a-party-stany/">přístřešky a party stany</a>.</li>'
          '<li><strong>Dlouhé tahy:</strong> lehčí turistický nebo týpí stan, který lze nést.</li></ul>'
          '<p>Rozdíl mezi pobytovým stanem a rybářským stanem vysvětlují kategorie <a href="/turisticke-stany/">turistické stany</a> a <a href="/rodinne-stany/">rodinné stany</a>.</p>'
          '<h2>Podlážky a ochrana proti vlhku</h2>'
          '<p>Podlážka je pevná vrstva, která se ukládá pod stan nebo do něj. Chrání před vlhkem, nerovnostmi a bahnem a prodlužuje život vlastní podlahy. Některé jsou ušité přesně na konkrétní model a mají otvory na tyče, jiné se prodávají jako univerzální plachta. Při koupi si ověřte, že rozměr odpovídá půdorysu stanu, jinak se do podlážky nasaje voda a zatéká pod stan.</p>'
          '<p>Studená země zvlášť na podzim chladí zespodu, proto se pod lehátko vkládá izolační podložka. Užitečná je i vlastní podložka pod spacák, o kterou byste neměli přijít. Pokud chcete podložku, prohlédněte si <a href="/rybarske-spacaky/">rybářské spacáky</a> a obecnější <a href="/spaci-pytle/">spací pytle</a>.</p>'
          '<h2>Stavba v terénu a ukotvení</h2>'
          '<p>Vyberte rovné suché místo mimo prohlubně, kde se hromadí voda. Stan stavte vstupem po větru, aby při otevření nenasál déšť. Kolíky zarážejte šikmo a u měkké půdy dlouhé nebo šroubovací kolíky. V písku a štěrku pomůže zatížit lanka kameny nebo pytlem písku.</p>'
          '<ul><li>Před zarážením kolíků očistěte plochu od kamenů a větví, které by protlačily podlahu.</li>'
          '<li>Natáhněte všechna odtahová lanka a zkontrolujte, zda tyče nejsou prověšené.</li>'
          '<li>Při silné bouřce stan sbalte a přemístěte pryč od vody a vysokých stromů.</li>'
          '<li>Nikdy nevařte uvnitř uzavřeného stanu, hrozí požár i otrava oxidem uhelnatým. Vařič používejte v předsíni s dobrým větráním nebo venku. Odpovídající výbavu najdete v kategorii <a href="/stanove-doplnky/">stanové doplňky</a>.</li></ul>'
          '<h2>Sezóna: léto, podzim a zima</h2>'
          '<p>V létě je největší problém horko a hmyz, takže se hodí síťovaná okna a odnímatelná přední stěna. Na jaře a na podzim převládá vlhko a chlad, takže potřebujete těsný dvouplášťový stan a dobrou izolaci. V zimě se hodí odolnější kupole se sníženým profilem, silnější lehátko a spacák s dostatečnou teplotní rezervou. Pro opravdové mrazy a vítr jsou lepší <a href="/expedicni-stany/">expediční a čtyřsezónní stany</a>.</p>'
          '<h2>Údržba, sušení a skladování</h2>'
          '<p>Po návratu stan rozložte doma a nechte důkladně vyschnout, i když byl jen vlhký od rosy. Zavlhlá plachta za pár dnů zplesniví a povrchová úprava látky se začne odlupovat. Stan čistěte měkkým kartáčem a studenou vodou, nepoužívejte pračku ani agresivní prostředky. Švy a zipy občas ošetřete sprejem nebo voskem. Nejlepší je ukládat stan volně nebo v prodyšném obalu na suchém místě, ne ve zmuchlaném vaku v garáži.</p>'
          '<p>Mezi časté opravy patří lepení trhliny, výměna tyče a nový šev. Většina výrobců dodává záplaty. Dobrým zvykem je mít v tašce sadu kolíků navíc, protože při rozebírání tábora se kolíky ztrácejí snadno.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Podcenění větru:</strong> velká plocha stanu se chová jako plachta. Bez pevných odtahů se stan i s lehátkem převrátí.</li>'
          '<li><strong>Nevhodná velikost:</strong> příliš malý stan znamená, že se vybavení musí nechat venku a zmoknout.</li>'
          '<li><strong>Špatné větrání:</strong> v uzavřeném stanu se sráží vlhkost a spacák je ráno vlhký.</li>'
          '<li><strong>Zaměnění stanu za jeho doplněk:</strong> podlážka není stan a naopak. Zkontrolujte, co přesně nabídka obsahuje.</li>'
          '<li><strong>Špatná váha:</strong> těžký stan se hůř nosí. Pokud chodíte pěšky, volte lehčí model.</li></ul>'
          '<h2>Pravidla revíru</h2>'
          '<p>Při koupi stanu myslete i na pravidla místa: na mnoha revírech a v chráněných územích se smí stanovat jen na vyhrazených plochách a po dobu uvedenou v řádu. Před výjezdem si proto přečtěte podmínky revíru a nechte po sobě břeh čistý.</p>'
          '<h2>Co dalšího se vám hodí k vodě</h2>'
          '<p>Vedle stanu potřebujete lehátko nebo postel, spacák, osvětlení, hodně suchého oblečení a dobrý zdroj tepla. Podrobnosti o prutech a navijácích najdete v kategoriích <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/rybarske-navijaky/">rybářské navijáky</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>. Elektroniku a čluny sledujte v <a href="/rybarske-lode-a-elektronika/">lodích a elektronice</a>, celé téma pak shrnuje <a href="/rybareni/">rybaření</a>. Pro krátké výlety do přírody stačí i obecnější <a href="/stany/">stany</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi bivakem a běžným stanem?', 'Bivak je nízká, často jednoplášťová kupole s širokým vstupem určená pro sezení u prutů a spaní na lehátku. Běžný turistický stan je lehčí a nižší a není uspořádaný kolem rybaření. Bivak má větší předsíň a lépe odolává dlouhému pobytu na jednom místě.'),
        ('Na co se dívat u vodního sloupce?', 'Čím vyšší hodnota, tím větší tlak vody látka vydrží, ale rozhodují i přelepené švy a kvalita podlahy. Pro trvalý déšť volte vyšší sloupec a pro pobyt v létě stačí nižší. Údaj uvedený výrobcem berte jako orientační.'),
        ('Je podlážka nutná?', 'Není povinná, ale chrání před vlhkem, kameny a bahnem a prodlužuje životnost stanu. Pokud stanujete na mokré louce nebo na štěrku, vyplatí se. Hlídejte, aby rozměry sedly na váš model.'),
        ('Kolik osob má mít stan, když rybařím sám?', 'Pro jednoho rybáře s lehátkem a boxem je vhodný stan pro dvě osoby. Údaj výrobce počítá jen se spacími místy, vybavení potřebuje další prostor. Při pobytu více nocí je větší stan pohodlnější.'),
        ('Jaká barva stanu je nejlepší?', 'Olivová, hnědá a tmavě zelená se maskují v přírodě a neruší ostatní návštěvníky. Světlé barvy jsou lépe vidět, ale zároveň se uvnitř tolik nezahřívají. Rozhodnutí závisí na místě i vaší preferenci.'),
        ('Dá se v rybářském stanu vařit?', 'Uvnitř zavřeného stanu ne, hrozí požár a otrava oxidem uhelnatým. Vařič používejte v otevřené předsíni nebo venku, vždy daleko od plachty. Vařič postavte na rovný stabilní podklad.'),
        ('Jak se starat o stan po výletu?', 'Stan rozložte doma a nechte ho úplně vyschnout, jinak plesniví. Čistěte měkkým kartáčem a studenou vodou, bez pračky a agresivních prostředků. Skladujte ho na suchém místě, ideálně volně nebo v prodyšném obalu.'),
        ('Jak ukotvit stan, aby ho neodfoukl vítr?', 'Použijte všechny kolíky a odtahová lanka, kolíky zarážejte šikmo. V písku nebo v měkké půdě pomůžou delší kolíky nebo zatížení kameny. Přední stranu otočte po větru a při bouřce stan raději sbalte.'),
        ('Jaký stan zvolit na zimu?', 'Dvouplášťový stan s dobrou izolací, nízkým profilem a silným spacákem. Pod lehátko vložte izolační podložku, protože studená země chladí nejvíc. Při opravdových mrazech zvažte expediční stan určený pro nízké teploty.'),
        ('Mohu rybářský stan použít i na běžné kempování?', 'Ano, ale je často těžší a hůře se nosí než lehký turistický stan. Pro krátké pěší výlety je výhodnější menší a lehčí model. Pro autokempink a tábor u vody se rybářský stan hodí dobře.'),
    ])

# ------------------------------------------------------------------ baletni-obuv
NEW['baletni-obuv'] = dict(long=True,
    title='Baletní obuv a piškoty: podešev, velikost, péče',
    desc='Baletní piškoty a baletní obuv pro děti i dospělé. Jak vybrat podešev, velikost, materiál a péči a porovnat nabídky českých obchodů.',
    intro='<p>Baletní piškoty jsou lehká měkká obuv, ve které chodidlo cítí podlahu a může pracovat do špičky. Používají se na hodinách klasického tance, při gymnastice i v tanečních kroužcích pro děti. Obuv musí padnout těsně jako druhá kůže, ale nesmí tlačit, jinak brání správnému postavení nohy. Sporteka porovnává nabídky českých obchodů u plátěných a kožených modelů s celou nebo dělenou podešví, v růžové i černé barvě. Stránka vysvětluje rozdíl mezi typy podešve, výběr velikosti a péči o obuv.</p>'
          '<p>V nabídce se objevují značky ' + B(('papillon', 'Papillon'), ('rucanor', 'Rucanor'), ('domyos', 'Domyos'), ('burtan', 'Burtan')) +
          '. Související výběr najdete v kategoriích <a href="/tanecni-obuv/">taneční obuv</a>, <a href="/tanecni-obleceni/">taneční oblečení</a> a <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>',
    guide='<h2>Co je baletní obuv a čím se liší od špiček</h2>'
          '<p>Pod pojmem baletní obuv se skrývá několik druhů. Nejběžnější jsou měkké piškoty, které používají začátečníci, děti i dospělí na hodinách baletu a gymnastiky. Špičky, tedy tvrdé baletní boty s vyztuženou špičkou, se obléknou až po několika letech tréninku a pod dohledem učitele. Do kategorie proto nepatří tvrdé špičky, ale měkká obuv pro trénink, cvičení a zábavu. Pokud dítě začíná, je to jediná správná volba.</p>'
          '<p>Piškoty nemají zpevněnou špičku ani pevnou stélku. Jejich účelem je chránit nohu před otěry a studenou podlahou, nikoli ji nést. Díky tomu se v nich dobře trénují základní polohy, pozice chodidla a práce s nártem. Nárt je klíčový při tanci, protože se při špičce prodlužuje linie nohy.</p>'
          '<h2>Druhy podešví</h2>'
          '<p>Rozhodující vlastností piškot je podešev, která určuje flexibilitu i dojem z nohy. Obvykle se setkáte se dvěma základními variantami.</p>'
          + T(['Podešev', 'Vlastnosti', 'Pro koho'], [
              ['Celá (jednodílná)', 'jeden kus kůže nebo zesílené látky po celé délce chodidla', 'začátečníci a menší děti, které teprve posilují nárty'],
              ['Dělená', 'kůže pouze pod patou a přední části, uprostřed pružná látka', 'pokročilejší tanečníci, kteří potřebují zvýraznit oblouk'],
              ['Neoprenová nebo elastická', 'měkká elastická vložka pro cvičení', 'příležitostné použití a gymnastika'],
              ['Neklouzavá', 'drsnější povrch, nebrání otáčkám', 'tanec na hladké podlaze, začátečníci']]) +
          '<p>Celá podešev poskytuje větší oporu a chodidlo se v ní lépe vede, ale hůř se v ní ukáže oblouk nohy. Dělená podešev je lehčí a pružnější, vyžaduje však silnější svaly nohy a dobré vedení. Učitel obvykle doporučí typ, který odpovídá úrovni žáka, a vyplatí se jeho radu respektovat.</p>'
          '<h2>Materiál: plátno, kůže a mikrovlákno</h2>'
          '<p>Volba materiálu ovlivňuje pohodlí, životnost i péči. Plátěné piškoty jsou lehké, prodyšné a snadno se perou, kožené jsou odolnější a lépe tvarují nohu. Mikrovlákno je syntetická alternativa, která se hodí pro cvičení a gymnastiku a snadno se čistí.</p>'
          '<ul><li><strong>Plátno:</strong> cenově dostupné, dobře dýchá, při častém praní se však vytahuje a postupně ztrácí tvar.</li>'
          '<li><strong>Kůže:</strong> měkká a přizpůsobivá, po rozchození obepíná nohu. Vyžaduje trochu péče a nemá se prát v pračce.</li>'
          '<li><strong>Mikrovlákno:</strong> pružné a nenáročné, hodí se na moderní gymnastiku a rekreační cvičení.</li>'
          '<li><strong>Elastické bočnice:</strong> pomáhají obuvi sedět těsně, zvláště u dětí s rychle rostoucí nohou.</li></ul>'
          '<h2>Barva a pravidla školy</h2>'
          '<p>Nejtypičtější je světle růžová, ale mnoho škol vyžaduje i černou, bílou nebo tělovou barvu. Před nákupem zjistěte, co škola požaduje. V nabídce najdete u dětí i dospělých obě nejběžnější varianty, růžovou a černou. Černé piškoty se hodí na modernu, jazz a lekce, kde není předepsaná tradiční barva, protože na nich není vidět špína.</p>'
          '<h2>Správná velikost: jak měřit</h2>'
          '<p>Piškoty se nenosí volné. Správná velikost je těsná, ale prsty se nesmí kroutit ani ohýbat. Prsty by měly ležet rovně a lehce se dotýkat špičky boty. Příliš velká obuv se při tanci sune, zvyšuje riziko zakopnutí a nepodpoří nohu. Příliš malá způsobuje otlaky a bolest.</p>'
          '<ul><li>Chodidlo změřte večer, kdy je noha mírně oteklá, od paty po nejdelší prst.</li>'
          '<li>Porovnejte délku s tabulkou výrobce, protože velikosti se mezi značkami liší.</li>'
          '<li>Dětem nekupujte obuv o dvě čísla větší do zásoby, správná je maximálně o půl čísla větší.</li>'
          '<li>Piškoty z kůže se rozchodí a mírně povolí, plátěné sedí od začátku.</li>'
          '<li>Pokud je noha široká nebo má vysoký nárt, hledejte model s elastickým prostředkem nebo šněrováním.</li></ul>'
          '<p>Nohy dětí rostou rychle, proto je rozumné ověřovat velikost každých několik měsíců. Děti někdy chtějí piškoty menší, protože jim větší připadají nezvyklé, ale příliš těsná obuv tlačí a brzdí vývoj správného postavení nohy. Pomáhá, když obuv vyzkoušíte přímo s ponožkou, kterou dítě na hodinách nosí, nebo bez ní podle toho, co škola předepisuje.</p>'
          '<h2>Pro děti, začátečníky a dospělé</h2>'
          '<p>Dětské piškoty bývají menší, lehčí a s elastickými šňůrkami, aby se děti obuly samy. Dospělí začátečníci potřebují stejný typ obuvi, jen ve větších velikostech a s důrazem na oporu klenby. Mezi dámskými a dětskými modely se liší střih i šířka, proto raději nekupujte dětskou verzi pro dospívající nohu. U chlapců je častá černá barva, ale existují i modely, které nesou unisex označení.</p>'
          '<ul><li><strong>Předškolní děti:</strong> měkká celá podešev, elastické přichycení a pohodlí, které dítě nevnímá.</li>'
          '<li><strong>Školní děti:</strong> kožené nebo plátěné piškoty s dělenou nebo celou podešví podle doporučení učitele.</li>'
          '<li><strong>Dospívající:</strong> pevnější střih, pokud se tanečnice připravuje na špičky.</li>'
          '<li><strong>Dospělí rekreační:</strong> pohodlné piškoty pro lekce baletu pro dospělé, fitness a pilates.</li>'
          '<li><strong>Gymnastky:</strong> lehčí mikrovlákno nebo plátno, které chrání chodidlo na koberci. Další vybavení najdete v kategorii <a href="/tanec-a-gymnastika/">tanec a gymnastika</a>.</li></ul>'
          '<h2>Jak obuv ošetřovat</h2>'
          '<p>Piškoty se pokaždé vyvětrají a po hodinách se nenechávají v tašce. Plátěné lze prát ručně ve vlažné vodě s jemným mýdlem a sušit na vzduchu mimo topení. Kožené otřete vlhkým hadříkem a nechte oschnout. Pračka většinu obuvi zdeformuje a zničí lepení podešve. Sušení u radiátoru zase smrští kůži a plátno.</p>'
          '<ul><li>Po hodině obuv vyndejte z tašky a nechte vyschnout.</li>'
          '<li>Pokud se uvolnil šev nebo šňůrka, dá se obuv často jednoduše přišít.</li>'
          '<li>Neklouzavá podešev se může zanést prachem, očistěte ji suchým kartáčkem.</li>'
          '<li>Obuv používejte jen v sále, venku se ničí. Pro cestu na hodinu použijte běžné boty.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li><strong>Příliš velká velikost:</strong> pocitově bezpečná, ale zhoršuje práci nohy a zvyšuje riziko pádu.</li>'
          '<li><strong>Špatná barva:</strong> škola často předepisuje konkrétní odstín a vrácení obuvi bývá složité.</li>'
          '<li><strong>Nevhodná podešev:</strong> začátečník s dělenou podešví nemá dost opory a učitel mu často doporučí vrátit se k celé. Před koupí si ověřte, co škola preferuje.</li>'
          '<li><strong>Špičky bez učitele:</strong> tvrdé špičky se kupují až po doporučení pedagoga, jinak hrozí poškození kloubů.</li>'
          '<li><strong>Zanedbání péče:</strong> zapařená obuv zapáchá a nevydrží.</li></ul>'
          '<h2>Co dalšího se hodí na hodinu</h2>'
          '<p>K piškotům patří oblečení, které nebrání pohybu a ukazuje linii těla. Trikot, sukýnku, punčocháče a vlasové doplňky najdete v kategorii <a href="/tanecni-obleceni/">taneční oblečení</a>. Pro zahřátí a protažení se hodí <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>, podložky a gumy. Do tašky patří i láhev s vodou a náhradní gumička do vlasů. K přenášení věcí poslouží <a href="/skolni-batohy/">školní batohy</a>.</p>'
          '<h2>První hodina: jak se připravit</h2>'
          '<p>Před první lekcí zjistěte, zda škola vyžaduje konkrétní obuv, oblečení a úpravu vlasů. Většina kroužků počítá s piškoty, přiléhavým trikotem nebo tričkem, punčocháči a sukýnkou nebo legínami. Dítě se v obuvi nejprve projde po bytě, aby si zvyklo na ten pocit. Nezapomeňte na kontrolu nehtů: dlouhé nehty na nohou tlačí do špičky piškot a při práci na špičkách způsobují bolest.</p>'
          '<p>Ponožky se nosí podle zvyku školy. V některých třídách se tančí v punčocháčích, v jiných bosky v obuvi. Tenká ponožka nebo bezšvová punčocha zabrání otlakům, zatímco silná froté ponožka obuv zbytečně zmenší. Učitel také upozorní, zda se má šňůrka u kotníku zavázat a schovat pod okraj, aby se při cvičení nerozvazovala.</p>'
          '<h2>Gumičky, šňůrky a drobné úpravy</h2>'
          '<p>Většina piškot se prodává s jednou nebo dvěma gumičkami, které se přišívají přes nárt. Přišití se provádí podle individuální nohy: gumička vede od středu vnitřní strany pod klenbou k vnější straně paty a zajišťuje, že obuv nesjíždí. Přišívají se obvykle sami rodiče nebo učitelé. Pokud je u obuvi stahovací šňůrka v lemu, stáhněte ji, aby obuv obepnula nohu, uzel schovejte dovnitř a přebytek odstřihněte. Šněrovadlo nesmí z boty viset, protože by se o ně dalo zakopnout.</p>'
          '<p>Při správné velikosti není nutné obuv upravovat víc než touto drobnou prací. Pokud však noha v botě zřetelně plave, nevyřeší to ani nejpevnější šněrování a je potřeba menší číslo.</p>'
          '<h2>Jak porovnávat na Sportece</h2>'
          '<p>Každý produkt ukazuje nabídky několika obchodů, včetně dostupnosti velikostí. Sledujte označení pro dámy, děti a barvu, zkontrolujte popis podešve a materiálu. Pokud se v názvu uvádí dělená podešev, jde o pokročilejší model. U cizích značek bývá velikostní tabulka v popisu obchodu, kterou si nezapomeňte porovnat s rozměrem chodidla.</p>',
    faq=[
        ('Jaké piškoty zvolit pro začátečníka?', 'Měkké piškoty s celou podešví, které poskytují oporu a učí pracovat s nohou. Dělená podešev se hodí až později, když má tanečník silnější svaly a ví, jak nohu vést. Poraďte se s učitelem, protože některé školy preferují konkrétní model.'),
        ('Jak poznám správnou velikost?', 'Obuv má sedět těsně, prsty leží rovně a lehce se dotýkají špičky. Chodidlo změřte od paty po nejdelší prst a porovnejte s tabulkou výrobce. Příliš velká obuv se sune, příliš malá tlačí.'),
        ('Jaký je rozdíl mezi plátěnými a koženými piškoty?', 'Plátěné jsou lehčí, prodyšné a snadno se perou, kožené jsou odolnější a lépe obepínají nohu. Plátno se vytahuje, kůže po rozchození sedí lépe. Volba často závisí na požadavcích školy.'),
        ('Je lepší růžová, nebo černá obuv?', 'Záleží na pravidlech školy. Růžová je tradiční pro děvčata, černá se hodí na moderní tanec a pro chlapce. Zjistěte předepsanou barvu před nákupem, aby nedošlo k nákupu zbytečné obuvi.'),
        ('Můžu piškoty prát v pračce?', 'Nedoporučuje se, protože obuv ztrácí tvar a lepení podešve povolí. Plátěné perte ručně ve vlažné vodě a sušte na vzduchu. Kožené otřete vlhkým hadříkem.'),
        ('Kdy dítě potřebuje špičky?', 'Špičky se kupují až po několika letech tréninku a vždy po doporučení učitele. Dítě musí mít dostatečně silné nohy a správnou techniku. Příliš brzké použití může poškodit chodidlo.'),
        ('Má smysl kupovat větší velikost do zásoby?', 'Ne, příliš velká obuv zhoršuje práci nohy a zvyšuje riziko zakopnutí. Výjimečně se toleruje o půl čísla navíc pro rychle rostoucí nohu. Raději měřte nohu častěji.'),
        ('Jaká je dělená podešev a komu pomáhá?', 'Je to podešev ze dvou kusů kůže, mezi nimiž je pružná látka. Zvýrazňuje oblouk nohy a usnadňuje pohyb, ale vyžaduje silnější svaly. Pokročilejší tanečníci ji preferují.'),
        ('Mohu piškoty použít i pro gymnastiku nebo cvičení?', 'Ano, měkká obuv chrání chodidlo na koberci a při cvičení. Pro gymnastiku se hodí lehká plátěná nebo mikrovláknová varianta. Na hodiny baletu se držte typu, který doporučí učitel.'),
        ('Co sledovat v popisu nabídky?', 'U baletní obuvi hledejte velikost, materiál, druh podešve a barvu. Pokud některý údaj chybí, porovnejte nabídku s tabulkou výrobce nebo se zeptejte prodejce, aby se předešlo zbytečnému vracení zboží.'),
    ])

# ------------------------------------------------------------------ nakladni-elektrokola
NEW['nakladni-elektrokola'] = dict(long=True,
    title='Nákladní elektrokola a tříkolky: výběr a nosnost',
    desc='Nákladní elektrokola, longtaily a elektrické tříkolky pro nákupy, děti i řemeslo. Nosnost, baterie, brzdy a legislativa při výběru a srovnání cen.',
    intro='<p>Nákladní elektrokolo (cargo bike) je prodloužený nebo zesílený stroj s motorem, který unese víc než běžné kolo: nákup na týden, dvě děti, boxy s nářadím nebo zásilky po městě. Najdete tu longtaily s dlouhým nosičem za sedlem, kompaktní rodinné modely i elektrické tříkolky s košem a širokým rozchodem. Sporteka porovnává nabídky českých obchodů a ukazuje je včetně dostupnosti. Stránka vysvětluje rozdíl mezi konstrukcemi, jak číst nosnost a baterii a čeho si všímat, aby kolo nahradilo druhé auto a nestalo se z něj těžký sklad ve sklepě.</p>'
          '<p>V nabídce jsou značky ' + B(('fafrees', 'Fafrees'), ('hitway', 'Hitway'), ('btwin', 'Btwin'), ('moma-bikes', 'Moma Bikes'), ('eskute', 'Eskute'), ('jobobike', 'Jobobike'), ('onesport', 'Onesport')) +
          '. Pro srovnání s jinými typy jsou tu <a href="/elektrokola/">elektrokola</a>, <a href="/trekingova-elektrokola/">trekingová elektrokola</a> a <a href="/skladaci-elektrokola/">skládací elektrokola</a>.</p>',
    guide='<h2>Jaké druhy nákladních elektrokol existují</h2>'
          '<p>Termín cargo se používá pro několik podobných, ale odlišných konstrukcí. Liší se způsobem, jakým je náklad uložen, a jízdními vlastnostmi. Před nákupem je vhodné si připravit, co budete převážet, protože právě to určuje typ.</p>'
          + T(['Typ', 'Popis', 'Hodí se pro'], [
              ['Longtail', 'prodloužený zadní nosič a dlouhý rám, kolo vypadá jako běžné, jen delší', 'děti na zadním sedátku, nákupy, dojíždění'],
              ['Kompaktní cargo', 'kratší rám s malými koly a nosičem', 'úzká města, výtah, menší prostory'],
              ['Přední nakládací (bakfiets)', 'velká bedna před řidičem, často dvě kola vpředu', 'těžší náklad, děti v boxu'],
              ['Elektrická tříkolka', 'dvě kola vzadu nebo vpředu, široký rozchod, koš', 'senioři, nákupy, lehká rozvážka'],
              ['Nákladní kolo s tlustými pláštěmi', 'široké pláště a robustní rám', 'nerovné cesty, štěrk a sníh'],
              ['Rodinný model', 'sedačky, madla a podnožky pro děti', 'jízda s dětmi do školy a školky']]) +
          '<p>V kategorii najdete longtaily, kompaktní kola, rodinné modely i elektrické tříkolky, často s označením cargo nebo triker. Značky se v názvu liší, ale konstrukce má vždy stejný cíl: bezpečně převézt víc než jednu osobu nebo nákup.</p>'
          '<h2>Nosnost: co znamenají čísla v popisu</h2>'
          '<p>Nosnost bývá udávána jako maximální celková hmotnost, tedy jezdec, náklad a případně děti dohromady. Tuto hodnotu lze porovnávat jen u modelů s podobným rámem. Rozdíl je mezi nosností nosiče a celkovou nosností: nosič může unést jen část váhy a zbytek je určen rámu. Při koupi ověřte obě čísla, zejména pokud plánujete vozit dvě děti nebo těžké nákupy.</p>'
          '<p>Důležité je i rozložení hmotnosti. Náklad blízko středu kola a nízko nad zemí se vozí lépe než vysoká hromada zavazadel za sedlem. U longtailu se těžké věci ukládají do bočních brašen těsně nad zadní osu, u přední bedny je nutné počítat s citlivějším řízením. Při přetížení ztrácí kolo stabilitu a brzdy mají dlouhou brzdnou dráhu.</p>'
          '<h2>Motor a baterie: kde se bere dojezd</h2>'
          '<p>Většina kol má motor s jmenovitým výkonem čtvrt kilowattu, což odpovídá evropským pravidlům pro elektrokola. Rozdíl se projeví hlavně v kroutícím momentu, tedy síle, se kterou kolo vyjede kopec s nákladem. Motor v zadním náboji je jednodušší a běžný u levnějších modelů, středový motor lépe rozkládá váhu a dobře zvládá stoupání. U nákladních kol se hodí kolo se silnějším točivým momentem, protože s plně naloženým strojem je rozjezd do svahu mnohem těžší.</p>'
          '<p>Kapacita baterie se udává ve voltech a ampérhodinách. Vyšší napětí a kapacita znamenají delší dojezd, ale také těžší baterii. Údaje o dojezdu v nabídkách berte jako orientační maximum, které platí pro nízkou hmotnost jezdce, rovinu a nízkou úroveň asistence. S dvěma dětmi, kopcem a větrem bude skutečný dojezd výrazně kratší. Některé modely mají dvě baterie, které zvyšují dojezd, ale také hmotnost. Pro delší cesty se hodí vyjímatelná baterie, kterou lze nabít v bytě.</p>'
          '<h2>Brzdy, rám a stabilita</h2>'
          '<p>S těžkým nákladem jsou brzdy nejdůležitější bezpečnostní prvek. Kotoučové hydraulické brzdy brzdí spolehlivěji než ráfkové, zejména za mokra a při dlouhém klesání. Mechanické kotoučové jsou lehčí a jednodušší na seřízení, ale vyžadují častější nastavování. Kontrolujte průměr kotouče, protože větší kotouče lépe odvádějí teplo a nehřejí se.</p>'
          '<ul><li><strong>Rám:</strong> hliník je lehčí, ocel pevnější. Svary musí být čisté a rovnoměrné, protože nosný rám nese zátěž.</li>'
          '<li><strong>Stojánek:</strong> dvounohý stojan drží kolo při nakládání dětí, jednonohý se při nákladu převrací.</li>'
          '<li><strong>Pláště:</strong> široké a pevné pláště snesou větší hmotnost a tlumí nerovnosti. Tlak upravte podle nákladu.</li>'
          '<li><strong>Kola:</strong> menší dvacetipalcová kola mají nižší těžiště, ale hůř překonávají výmoly.</li>'
          '<li><strong>Řízení:</strong> delší kolo má větší poloměr otáčení, proto zkuste jízdu v úzkých zatáčkách ještě před nákupem.</li></ul>'
          '<h2>Tříkolka, nebo dvoukolový longtail</h2>'
          '<p>Tříkolky stojí stabilně i při nakládání a rozjezdu, takže se hodí pro seniory a pro lidi, kteří mají problém s rovnováhou. Nevýhodou je větší šířka, těžší manévrování v davu a nutnost projet úzkou brankou nebo výtahem. Zatáčky se projíždějí pomaleji, protože při příliš rychlé jízdě se může jedno kolo zvednout. Longtail je ovladatelný jako běžné kolo, ale při nakládání vyžaduje oporu a cit. Rozhodnout pomůže zkušební jízda, kterou někteří prodejci umožňují.</p>'
          '<p>Pro stabilitu je důležité také ukládání: tříkolka zabere ve sklepě nebo před domem víc místa a nejde snadno nahodit na stojan v autě. Pokud nemáte garáž, zvažte, kam kolo na noc zamknete.</p>'
          '<h2>Převoz dětí a bezpečnost</h2>'
          '<p>Děti se na nákladním kole převážejí na speciálním sedátku nebo v boxu s pásy. Podnožky a madla musí být pevná, aby se dítě drželo a nohy nezachytily kolo. Důležité je i chránění nohou: kryt zadního kola zabrání zachycení do špic. Dítě musí mít vždy cyklistickou helmu, v nabídce najdete <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>. Pro dospělé jsou připravené <a href="/cyklisticke-helmy/">cyklistické helmy</a> a <a href="/mestske-cyklohelmy/">městské cyklohelmy</a>.</p>'
          '<p>Před jízdou ověřte, zda daný model smí přepravovat děti, a pro jaký věk je sedátko určené. Právní podrobnosti ohledně převozu dětí a vybavení se mohou měnit, proto si pravidla ověřte u oficiálních zdrojů. Při první jízdě s dětmi jeďte pomalu a vyberte klidné místo.</p>'
          '<h2>Pravidla provozu a elektrokolo</h2>'
          '<p>Elektrokolo s motorem do čtvrt kilowattu a asistencí do rychlosti pětadvacet kilometrů v hodině se u nás obecně považuje za jízdní kolo. Silnější stroje se chovají jako moped a vyžadují jiné podmínky. Při koupi proto sledujte údaje o výkonu a omezovači rychlosti. Pokud model nabízí škrtící plynovou rukojeť bez šlapání, ověřte si pravidla pro takovou konstrukci. Zákon se mění, takže důležité informace hledejte v aktuálních předpisech.</p>'
          '<h2>Servis, údržba a péče o baterii</h2>'
          '<p>Nákladní kolo je namáhané víc než běžné, proto vyžaduje častější kontrolu. Prohlédněte brzdové obložení, napnutí řetězu a tlak v pláštích. Těžký náklad opotřebovává řetěz a kazetu rychleji, vyplatí se jejich včasná výměna. Čistěte kolo vlhkým hadrem, vyhněte se tlakové myčce u motoru a elektrických konektorů.</p>'
          '<ul><li>Baterii skladujte v suchu při pokojové teplotě, ne dlouhodobě vybitou nebo zcela nabitou.</li>'
          '<li>V zimě baterii přenášejte do tepla, protože v mrazu klesá dojezd.</li>'
          '<li>Používejte originální nabíječku, neimprovizujte s levnými adaptéry.</li>'
          '<li>Při dlouhém skladování baterii jednou za pár týdnů dobijte.</li>'
          '<li>Pro servis motoru a řídicí jednotky se obraťte na autorizovaný servis. Základní díly najdete v kategoriích <a href="/cyklo-dily/">cyklo díly</a> a <a href="/cyklo-brzdy/">cyklo brzdy</a>.</li></ul>'
          '<h2>Doplňky: zámek, brašny, světla</h2>'
          '<p>Těžké elektrokolo je lákavý cíl pro zloděje, takže potřebuje kvalitní zámek, ideálně dva různé. Přehled najdete v kategorii <a href="/cyklo-zamky/">cyklo zámky</a>. Dále se hodí brašny a koše z kategorie <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>, silná <a href="/cyklo-svetla/">světla</a> a <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>. Pro bezpečné sezení dětí zkontrolujte <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>. Pokud potřebujete kolo na cesty autem, ověřte nosnost <a href="/cyklo-nosice-na-auto/">nosičů na auto</a>, protože hmotnost nákladního kola je často mimo limity.</p>'
          '<h2>Pro koho se nákladní kolo hodí</h2>'
          '<ul><li><strong>Rodiny s dětmi:</strong> cesta do školy a školky, nákup cestou zpět, bez hledání parkování.</li>'
          '<li><strong>Dojíždění s nákupem:</strong> longtail nebo kompakt, který se vejde do výtahu nebo na chodbu.</li>'
          '<li><strong>Senioři:</strong> tříkolka se stabilním podvozkem a nízkým nástupem.</li>'
          '<li><strong>Řemeslníci a drobné podnikání:</strong> přední nakládací model nebo tříkolka s bednou pro nářadí a zásilky.</li>'
          '<li><strong>Kdo nepotřebuje náklad:</strong> běžné <a href="/mestska-elektrokola/">městské elektrokolo</a> bude levnější, lehčí a praktičtější.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Na Sportece vidíte u každého kola nabídky více obchodů a dostupnost. Sledujte nosnost, kapacitu baterie, typ brzd, rozměry a hmotnost kola. Mnohé modely mají obdobný název, ale liší se výbavou, proto si prohlédněte parametry v popisu obchodu. Ověřte také, zda prodejce nabízí servis v Česku a dostupnost náhradních dílů. Před koupí si vždy změřte místo, kde bude kolo stát, a výšku dveří a výtahu.</p>',
    faq=[
        ('Co je longtail a čím se liší od nákladní tříkolky?', 'Longtail je dvoukolové kolo s prodlouženým rámem a zadním nosičem, jezdí se na něm jako na běžném kole. Tříkolka má tři kola a je stabilnější při stání a rozjezdu, ale širší a hůř se vyhýbá v úzkých místech. Výběr závisí na tom, co a koho převážíte.'),
        ('Jakou nosnost nákladního kola potřebuji?', 'Počítejte hmotnost jezdce, dětí a nákladu dohromady a přidejte rezervu. Ověřte i nosnost nosiče, ta bývá nižší než celková. Pokud často vozíte dvě děti a nákup, vybírejte model s nosností určenou výslovně pro rodinné použití.'),
        ('Jaký dojezd mohu čekat s nákladem?', 'Údaj výrobce je orientační maximum za příznivých podmínek. S plným nákladem, kopcem a vysokou asistencí bude dojezd výrazně kratší. Pro delší trasy se hodí vyjímatelná baterie nebo model se dvěma bateriemi.'),
        ('Jaké brzdy zvolit?', 'Pro těžké kolo je nejlepší kotoučová brzda, nejlépe hydraulická s větším kotoučem. Lépe brzdí za mokra i s nákladem a méně se zahřívá. Brzdové obložení častěji kontrolujte.'),
        ('Je nákladní elektrokolo v Česku považováno za kolo?', 'Pokud má motor s jmenovitým výkonem do čtvrt kilowattu a asistence se vypíná při omezené rychlosti, obvykle se chová jako jízdní kolo. Silnější stroje nebo kola s plynem podléhají jiným pravidlům. Aktuální předpisy si ověřte u oficiálních zdrojů.'),
        ('Mohu na nákladním kole vozit děti?', 'Ano, pokud kolo má schválené sedátko nebo box s pásy a podnožkami. Dítě musí mít helmu a nohy chráněné před kolem. Přesné pokyny najdete v návodu a v pravidlech platných pro vaši zemi.'),
        ('Vejde se nákladní kolo do výtahu nebo do sklepa?', 'Longtail je delší, ale úzký a často se vejde do větších výtahů. Tříkolka je širší a do běžných dveří nepůjde. Před koupí změřte délku, šířku a výšku kola a porovnejte s místem uložení.'),
        ('Jak pečovat o baterii?', 'Skladujte ji v suchu při pokojové teplotě a ne dlouho vybitou. V zimě ji přenášejte do tepla. Používejte originální nabíječku a při dlouhém odstavení ji občas dobijte.'),
        ('Je lepší střední motor, nebo motor v zadním náboji?', 'Středový motor lépe rozkládá hmotnost a zvládá stoupání, ale stojí víc a vyžaduje speciální servis. Motor v zadním náboji je jednodušší a častější v levnějších modelech. S těžkým nákladem se silnější točivý moment vyplatí.'),
        ('Jaké doplňky jsou nejdůležitější?', 'Kvalitní zámek, dobré světlo, brašny a dvounohý stojan. Pro děti také helmy a chrániče nohou. Zámek volte robustní, protože těžké elektrokolo je lákavý cíl.'),
    ])
