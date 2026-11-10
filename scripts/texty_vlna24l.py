"""sporteka.cz — wave 24l (5. 11. 2026): long texts for detske-trikolky, hokejove-cepele-a-nasady, skialpove-lyze, golfove-micky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detske-trikolky
NEW['detske-trikolky'] = dict(long=True,
    title='Dětské tříkolky: typy, věk, vodicí tyč, výběr',
    desc='Dětské tříkolky s vodicí tyčí, multifunkční 3v1 a 5v1 i samostatné. Jak vybrat podle věku, stability a materiálu a porovnat nabídky českých obchodů.',
    intro='<p>První tříkolka bývá pro dítě prvním vlastním dopravním prostředkem. Stojí na pomezí kočárku, hračky a sportovní pomůcky: v prvních měsících dítě vozí rodič, později se učí šlapat a řídit samo. Proto je v nabídce tolik rozdílných konstrukcí, od jednoduchých tříkolek bez vybavení po modely s otočným sedadlem, stříškou, košíkem a odnímatelnou tyčí. Sporteka porovnává nabídky českých obchodů a ukazuje, které varianty jsou právě skladem.</p>'
          '<p>V kategorii najdete například značky ' + B(('petite-mars', 'Petite Mars'), ('hypermotion', 'Hypermotion'), ('arcore', 'Arcore'), ('qplay', 'Qplay'), ('lionelo', 'Lionelo'), ('smoby', 'Smoby'), ('coccolle', 'Coccolle'), ('globber', 'Globber'), ('razor', 'Razor')) +
          '. Až dítě tříkolku přeroste, přijdou na řadu <a href="/odrazedla/">odrážedla</a>, <a href="/detska-kola-12-14-palcu/">dětská kola 12 a 14 palců</a> nebo <a href="/kolobezky/">koloběžky</a>.</p>',
    guide='<h2>Jaké druhy dětských tříkolek existují</h2>'
          '<p>Rozdíl mezi modely nejlépe vystihne otázka, kdo tříkolku většinu času ovládá. Prvních několik měsíců řídí rodič přes tyč, později se řízení postupně předává dítěti. Podle toho se tříkolky dělí do několika skupin.</p>'
          + T(['Typ', 'Jak funguje', 'Hodí se pro'], [
              ['Tříkolka s vodicí tyčí', 'rodič tlačí a řídí tyčí, pedály se dají zafixovat', 'první jízdy, děti kolem prvních narozenin'],
              ['Multifunkční 3v1', 'z kočárkového režimu se mění na samostatnou tříkolku', 'rodiny, které chtějí jeden kus na delší dobu'],
              ['Multifunkční 5v1 a 8v1', 'navíc odrážedlo, odnímatelná stříška, otočné sedadlo, ochranná tyč', 'nejširší využití, ale větší hmotnost'],
              ['Samostatná tříkolka', 'bez tyče, dítě šlape a řídí samo', 'děti od zhruba dvou do čtyř let'],
              ['Tříkolka s pohonem pákou nebo bez pedálů', 'netradiční pohon, často sportovní vzhled', 'starší děti, které chtějí zábavu'],
              ['Tříkolka-koloběžka (trike)', 'kombinace odrážení a sedátka, přední kolo dvě', 'děti, které přecházejí na koloběžku']]) +
          '<p>V nabídce se objevuje i několik netypických kusů, třeba tříkolka ve stylu koloběžky nebo drift tříkolka s plastovými zadními koly. Ty se hodí pro starší děti, které už šlapou jistě, a nejsou náhradou první tříkolky s tyčí.</p>'
          '<h2>Věk dítěte a velikost</h2>'
          '<p>Výrobci uvádějí rozsah věku, ale důležitější je, co dítě zvládá. Pro tříkolku s tyčí stačí, aby dítě samo sedělo a drželo hlavičku. Šlapat se děti učí obvykle později, někdy až kolem druhého roku. Řízení bývá nejobtížnější, protože vyžaduje koordinaci rukou a nohou současně.</p>'
          '<ul><li><strong>Výška sedla a vzdálenost k pedálům:</strong> dítě má dosáhnout na pedály s lehce pokrčenými koleny. Výškově nastavitelné sedlo prodlouží používání o několik měsíců.</li>'
          '<li><strong>Držení těla:</strong> má-li dítě záda opřená a ruce na řídítkách v pohodlné vzdálenosti, neunaví se tak rychle.</li>'
          '<li><strong>Maximální nosnost:</strong> udává výrobce a vyplatí se ji respektovat, protože souvisí se stabilitou rámu i s kvalitou ložisek.</li>'
          '<li><strong>Rezerva na růst:</strong> o něco větší tříkolka vydrží déle, ale příliš velká dítěti ztěžuje šlapání a vede k nepohodlí.</li></ul>'
          '<h2>Vodicí tyč: proč je důležitá a co sledovat</h2>'
          '<p>Vodicí tyč je pro rodiče nejpraktičtější prvek, protože tříkolku řídí bez shýbání a dítě se může soustředit na pozorování okolí. Kvalitní tyč má tři vlastnosti: nastavitelnou výšku, pevné uchycení a možnost odejmutí, když dítě začne jezdit samo.</p>'
          '<ul><li><strong>Řízení tyčí:</strong> tyč může jen tlačit, nebo ovlivňovat i směr předního kola. Druhá varianta je pohodlnější, ale mechanismus je složitější.</li>'
          '<li><strong>Zámek řízení:</strong> umožňuje jet rovně, i když dítě tahá za řídítka. Odemknutí dá dítěti svobodu, až bude připravené.</li>'
          '<li><strong>Volnoběh pedálů:</strong> pedály se mohou při tlačení otáčet nebo je lze zafixovat, aby dítěti neuhodily do nohou.</li>'
          '<li><strong>Odnímatelná tyč:</strong> po odmontování se z tříkolky stane samostatný dopravní prostředek.</li></ul>'
          '<h2>Bezpečnost a pohodlí</h2>'
          '<p>Malé děti se často zhoupnou do strany, nakloní se za hračkou nebo se zkusí postavit. Tříkolka proto musí stát stabilně a nabízet oporu. U modelů s výklopným sedadlem a ochrannou tyčí sledujte, jak snadno se zajišťuje, protože dítě by se nemělo samo dostat ven.</p>'
          '<ul><li><strong>Pásy a bezpečnostní tyč:</strong> přidržují dítě, dokud nesedí jistě. Pětibodový pás je pevnější než jednoduché zapínání.</li>'
          '<li><strong>Rozchod kol:</strong> širší zadní kola zmenšují riziko překlopení při zatáčení.</li>'
          '<li><strong>Brzda nebo zadní zámek kol:</strong> pomůže rodiči při zastavení, hlavně z kopce.</li>'
          '<li><strong>Stříška a ochrana proti slunci:</strong> větší stříška zakrývá dítě při delší vyjížďce, ale zvyšuje odpor větru.</li>'
          '<li><strong>Označení shody:</strong> u dětských produktů hledejte CE a údaje o dovozci nebo výrobci. Chybějící označení je důvod k opatrnosti.</li></ul>'
          '<p>Dítě by mělo jezdit na tříkolce vždy pod dohledem dospělé osoby a ne na silnici. Pro starší děti se hodí <a href="/detske-cyklohelmy/">dětská cyklistická helma</a>, na kterou si zvykne ještě před přesunem na kolo.</p>'
          '<h2>Materiál a konstrukce</h2>'
          '<p>Rámy bývají z oceli nebo z lehčích slitin, případně z plastu s kovovými prvky. Ocel je pevná a tišší, ale těžší, plast je lehký a levnější na výrobu, jenže při větším zatížení může praskat. Pro každodenní jízdu po chodníku stačí solidní ocelový rám a plná nebo pěnová kola.</p>'
          '<ul><li><strong>Plastová plná kola:</strong> nepotřebují údržbu, ale jsou hlučnější a na hrubém povrchu méně komfortní.</li>'
          '<li><strong>Pěnová kola:</strong> tlumí nerovnosti, nepropíchnou se a jsou tišší.</li>'
          '<li><strong>Nafukovací pneumatiky:</strong> nejlepší komfort a přilnavost, ale vyžadují dohušťování a mohou se propíchnout.</li>'
          '<li><strong>Sedlo:</strong> měkčí čalounění a opěrka zad prodlouží vyjížďky, snímatelný potah se dá vyprat.</li>'
          '<li><strong>Doplňky:</strong> košík, držák lahve, zvonek nebo světlo jsou příjemné, ale nejsou důležitější než pevnost rámu.</li></ul>'
          '<h2>Pro koho se která tříkolka hodí</h2>'
          '<ul><li><strong>Pro dítě kolem prvních narozenin:</strong> tříkolka s vodicí tyčí, stříškou a pásy, kde dítě nemusí šlapat.</li>'
          '<li><strong>Pro rodinu, která chce jednu tříkolku na více let:</strong> multifunkční model s odnímatelnými částmi.</li>'
          '<li><strong>Pro aktivní dvouleté a tříleté děti:</strong> samostatná tříkolka s nízkým sedlem a širokými koly.</li>'
          '<li><strong>Pro často cestující rodiče:</strong> skládací nebo lehká tříkolka, která se vejde do kufru.</li>'
          '<li><strong>Pro darování:</strong> jednodušší model bez výbavy je levnější na doplňky a snáz se opravuje.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě příliš velké tříkolky v domnění, že dítě „doroste". Dítě na velké tříkolce nedosáhne na pedály a jízda ho nebaví.</li>'
          '<li>Podcenění hmotnosti. Tříkolka s mnoha funkcemi může být těžká a rodič ji nezvedne do auta ani po schodech.</li>'
          '<li>Výběr podle barvy a vzhledu bez kontroly zámku řízení, brzdy nebo výškové regulace.</li>'
          '<li>Opomenutí údržby: šroubové spoje se po několika týdnech uvolní a je třeba je dotáhnout.</li>'
          '<li>Pořízení tříkolky s funkcemi, které se nikdy nepoužijí. Někdy je lepší jednodušší model než „vše v jednom".</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Tříkolku venku nenechávejte, protože déšť a slunce poškodí plasty, čalounění i ložiska. Otřete ji vlhkou utěrkou, nechte uschnout a přibližně jednou za sezonu zkontrolujte šrouby, kola a upevnění tyče. Plasty vystavené trvalému slunci blednou a křehnou. Pokud tříkolku skládáte, ujistěte se, že se při tom nezachytí prsty dítěte.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Stejná tříkolka se prodává ve více obchodech a rozdíl bývá nejen v ceně, ale i v dostupnosti barev, doplňků a dopravě. Z karty produktu zjistíte, kdo ji má skladem, a porovnáte, jestli je součástí balení tyč, stříška nebo taška. Zvláštní pozornost věnujte tomu, zda jde o novou věc, nebo o použitý kus, a zda se uvádí záruka.</p>',
    faq=[
        ('Od kdy může dítě jezdit na tříkolce?', 'Na tříkolce s vodicí tyčí, opěrkou zad a bezpečnostním pásem může dítě jezdit, jakmile samo sedí. Šlapat se většina dětí naučí později. Řiďte se schopnostmi dítěte a návodem výrobce.'),
        ('Je lepší tříkolka s vodicí tyčí, nebo bez?', 'Pro nejmenší děti je vodicí tyč praktická, protože rodič řídí tříkolku sám. Pro samostatné jezdce je tyč zbytečná váha, proto je dobré, když jde odmontovat.'),
        ('K čemu je multifunkční tříkolka 3v1 nebo 5v1?', 'Číslo udává, v kolika režimech lze tříkolku používat. Typicky jde o kočárkový režim, tříkolku s tyčí, samostatnou tříkolku a odrážedlo. Konkrétní funkce se u modelů liší, proto čtěte popis.'),
        ('Na co se při výběru zaměřit nejdřív?', 'Na stabilitu, pevný rám, nastavení sedla a bezpečnostní prvky. Barvy a doplňky jsou až na druhém místě.'),
        ('Jaká kola jsou nejlepší?', 'Pěnová kola jsou tichá a nepropíchnou se, nafukovací mají nejlepší komfort. Plná plastová kola jsou nejlevnější, ale hlučnější a méně pohodlná.'),
        ('Má smysl kupovat tříkolku s pásy?', 'Ano, pro menší děti rozhodně. Pásy nebo ochranná tyč zabraňují vypadnutí při náklonu a zatáčení. Starším dětem už stačí normální sedlo.'),
        ('Jak poznám, že dítě tříkolku přerostlo?', 'Kolena zasahují do řídítek, dítě nemá dostatečně pokrčené nohy při šlapání nebo se tříkolka stává nestabilní. Pak je čas přejít na odrážedlo nebo dětské kolo.'),
        ('Dá se tříkolka používat v zimě?', 'Na suchém povrchu ano, ale plastová kola na ledu kloužou a ložiska trpí solí a vlhkostí. Po jízdě v mokru ji osušte a skladujte v suchu.'),
        ('Co je lepší pro starší dítě, tříkolka, nebo odrážedlo?', 'Starší děti, které už jistě chodí, obvykle více pokročí s odrážedlem nebo koloběžkou, protože se učí rovnováhu. Tříkolka je vhodnější pro začátek a pro mladší děti.'),
        ('Mohu tříkolku vzít do auta nebo do letadla?', 'Záleží na hmotnosti a skládání. Tříkolky s odnímatelnou tyčí a sklopným rámem se vejdou do kufru snadněji. Před cestou letadlem se informujte u dopravce o podmínkách přepravy.'),
    ])

# ------------------------------------------------------------------ hokejove-cepele-a-nasady
NEW['hokejove-cepele-a-nasady'] = dict(long=True,
    title='Hokejové čepele a násady: profil, ohyb, výběr',
    desc='Hokejové čepele, násady, nástavce a držáky nožů. Jak zvolit profil, ohyb, tuhost a materiál a porovnat nabídky českých hokejových obchodů.',
    intro='<p>Dvoudílná hokejka dovolí vyměnit jen opotřebenou část, takže hráč nemusí kupovat celou hokejku a ušetří. Hokejová čepel vydrží zlomek doby, kterou vydrží násada, protože se opotřebovává o led, puk a bandu. Proto má smysl vyměnit jen ji. Sporteka porovnává nabídky českých obchodů u čepelí na hokejky, samostatných násad, nástavců, držáků a výměnných nožů pro brusle, tedy u kusů, které se v běžných kategoriích hokejek ztrácejí.</p>'
          '<p>V kategorii jsou značky ' + B(('winnwell', 'Winnwell'), ('fischer', 'Fischer'), ('ccm', 'CCM'), ('sherwood', 'Sherwood'), ('bauer', 'Bauer')) +
          '. Celé hokejky najdete v kategorii <a href="/hokejky/">hokejky</a>, k nim pasují <a href="/hokejove-pasky-a-doplnky/">hokejové pásky a doplňky</a>, <a href="/hokejove-puky-a-branky/">puky a tréninkové pomůcky</a> a <a href="/hokejove-brusle/">brusle</a>.</p>',
    guide='<h2>Co všechno tato kategorie obsahuje</h2>'
          '<p>Název slibuje čepele a násady, ale ve skutečnosti se tu potkává několik odlišných druhů součástek. Aby se při nákupu nespletlo, je užitečné je rozlišit.</p>'
          + T(['Součástka', 'K čemu slouží', 'Na co dát pozor'], [
              ['Hokejová čepel', 'spodní část hokejky, která se dotýká puku', 'profil, ohyb, strana a způsob upevnění do násady'],
              ['Násada (shaft)', 'dlouhá horní část, kterou hráč drží', 'délka, tuhost, materiál, tvar průřezu'],
              ['Nástavec násady', 'prodlužuje krátkou hokejku nebo násadu', 'průřez shodný s násadou, způsob zalepení'],
              ['Chránič čepele', 'obal proti poškození při přepravě', 'délka a šířka čepele'],
              ['Držák nožů (holder)', 'plastový nosník u brusle, do něhož se nasazuje nůž', 'kompatibilita s botou a velikostí'],
              ['Výměnný nůž brusle', 'ocelová hrana, která se po opotřebení vyměňuje', 'délka a výška nože, systém uchycení']]) +
          '<p>Součástí nabídky jsou i systémy výměnných nožů a držáků brusle. Patří do stejné kategorie jen proto, že jde o doplňkové a výměnné součásti. Pro pochopení brusle se vyplatí číst i kategorii <a href="/hokejove-brusle/">hokejové brusle</a>.</p>'
          '<h2>Jak čepel zapadá do hokejky</h2>'
          '<p>Dvoudílné hokejky se skládají z násady a čepele. Čepel má na horním konci trn, který se zasune do dutého konce násady, a obvykle se zalepí tavným lepidlem nebo speciálním tmelem. Při výměně se čepel zahřeje a vytáhne, nový trn se zalepí. Proces zvládne zkušenější hráč, ale většinou ho dělají prodejny hokejového vybavení.</p>'
          '<ul><li><strong>Shoda průřezu:</strong> trn čepele musí odpovídat dutině násady. U některých značek jsou rozdíly, proto se vyplatí kupovat čepel a násadu od stejného výrobce.</li>'
          '<li><strong>Délka trnu:</strong> příliš krátký trn se může po zalepení uvolnit.</li>'
          '<li><strong>Zkrácení násady:</strong> hokejky se řežou shora, čepel se tím nemění. Před řezem je třeba měřit s bruslemi na nohou.</li></ul>'
          '<h2>Profil čepele a ohyb</h2>'
          '<p>Profil čepele určuje, jak hráč s pukem pracuje. Označení se liší mezi výrobci, ale princip zůstává stejný: popisuje se ohyb čepele, jeho místo, otevření a stranu. Označení typu PS1 nebo P92 se v nabídce objevují často, přestože pro různé značky nemusí znamenat zcela totéž.</p>'
          '<ul><li><strong>Strana čepele:</strong> levá nebo pravá čepel se určuje podle toho, kterou rukou hráč drží násadu dole. Zde se hráči často mýlí. Levák drží hokejku levou rukou dole.</li>'
          '<li><strong>Ohyb (křivka):</strong> větší ohyb pomáhá při zvedání puku, ale ztěžuje přihrávky po ledě a bekhendy. Menší ohyb je univerzálnější.</li>'
          '<li><strong>Místo ohybu:</strong> blízko paty čepele usnadňuje rychlé střely, blíž ke špičce lépe zvedá puk.</li>'
          '<li><strong>Otevření:</strong> míra, do které čepel ukazuje směrem od hráče nebo k němu, ovlivňuje zpracování puku.</li>'
          '<li><strong>Tvar špičky:</strong> zaoblená špička je tolerantnější, hranatá poskytuje větší plochu k vedení puku.</li></ul>'
          '<p>Nejjistější způsob, jak trefit profil, je vzít čepel, kterou hráč používá a je spokojený, a hledat stejné označení. Hráč, který zkouší nový profil, by si měl nejdřív vyzkoušet hokejku kamaráda nebo si ji půjčit v hokejové prodejně.</p>'
          '<h2>Materiál čepele</h2>'
          '<p>Čepele se vyrábějí z několika materiálů a každý z nich hraje jinak. Dřevo bylo dlouho standardem, dnes vedle něj stojí kompozity a plasty.</p>'
          '<ul><li><strong>Dřevěné čepele:</strong> často s laminací a skelným vláknem, příjemný pocit puku, nižší cena, kratší životnost při intenzivním hraní.</li>'
          '<li><strong>Kompozitní čepele:</strong> uhlíková vlákna a pěnové jádro, nižší hmotnost a rychlá odezva, vyšší cena a při nárazu hrozí prasknutí.</li>'
          '<li><strong>Plastové čepele:</strong> hodí se pro nácvik na asfaltu, ale i pro hokejbal. V nabídce se objevují čepele označené jako plastové pro tréninky mimo led.</li>'
          '<li><strong>Hybridní čepele:</strong> pěnové jádro s vnější vrstvou kompozitu, kompromis mezi pocitem a odolností.</li></ul>'
          '<h2>Násady: délka, tuhost, průřez</h2>'
          '<p>Násada, anglicky shaft, je ta část hokejky, kterou hráč drží. Ovlivňuje pocit, přenos síly a odezvu. Mezi hlavní parametry patří:</p>'
          '<ul><li><strong>Délka:</strong> hokejka v bruslích má sahat zhruba k bradě nebo k nosu. Delší násada dává větší dosah, kratší lepší práci s pukem.</li>'
          '<li><strong>Tuhost (flex):</strong> udává, jak snadno se násada prohýbá při střele. Měkčí násada se hodí pro lehčí hráče, tuhá pro silné a zkušené. Zhruba se tuhost volí podle poloviny tělesné hmotnosti hráče, ale přesná čísla se liší podle značky.</li>'
          '<li><strong>Průřez:</strong> kulatější nebo hranatější profil mění uchopení. Některé násady mají textilní nebo gumový povrch pro lepší přilnavost.</li>'
          '<li><strong>Materiál:</strong> dřevo je levnější a ztuhlejší, kompozit lehčí a pružnější.</li>'
          '<li><strong>Věková kategorie:</strong> označení YTH, JR, INT a SR odpovídá dětským, juniorským, přechodovým a seniorským délkám a tuhostem.</li></ul>'
          '<p>Nástavce násady se používají, když rostoucí hráč potřebuje delší hokejku nebo když se násada zkrátila příliš. Nástavec se zasune do dutiny násady a zalepí. Levnější dřevěné nástavce jsou vhodné pro mládež, kompozitní lehčí a tužší.</p>'
          '<h2>Držáky a výměnné nože brusle</h2>'
          '<p>Několik položek v kategorii se netýká hokejky, ale brusle. Moderní hokejové brusle mají plastový držák s výměnným ocelovým nožem. Když se nůž opotřebuje nebo poškodí, vymění se bez vyhazování celé brusle. Systém je pohodlný pro hráče, kteří hrají často nebo jezdí na různém ledu.</p>'
          '<ul><li><strong>Kompatibilita:</strong> každý systém výrobce má vlastní rozměry a uchycení. Držák a nůž musejí odpovídat modelu brusle, proto se kupují podle návodu výrobce.</li>'
          '<li><strong>Délka nože:</strong> vychází z velikosti boty, ale u držáků se liší označení.</li>'
          '<li><strong>Broušení:</strong> nože se musejí brousit, aby držely hranu. Hrubá hrana je nebezpečná a hráč hůř brzdí.</li>'
          '<li><strong>Výměna:</strong> většina hráčů ji svěřuje servisu, kde mají nářadí a znají postup.</li></ul>'
          '<h2>Pro koho se co hodí</h2>'
          '<ul><li><strong>Děti a junioři:</strong> levnější dřevěné nebo plastové čepele a dřevěné nástavce, protože rostou a čepele rychle ničí.</li>'
          '<li><strong>Rekreační hráči:</strong> univerzální profil se středním ohybem, dřevěná nebo hybridní čepel.</li>'
          '<li><strong>Ambiciózní hráči a dospělí:</strong> kompozitní čepele se zvoleným profilem a násada s vhodnou tuhostí.</li>'
          '<li><strong>Hokejbaloví a uliční hráči:</strong> plastové čepele, které snesou asfalt.</li>'
          '<li><strong>Brankáři:</strong> mají odlišné hokejky a čepele, proto si vybírejte z kategorie <a href="/hokejove-brankarske-vybaveni/">brankářská výstroj</a>.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Záměna levé a pravé strany. Strana čepele se řídí tím, kterou rukou hráč drží násadu dole, ne tím, kterou rukou píše, a proto se hráči často mýlí.</li>'
          '<li>Kupování čepele jiné značky, aniž se ověří, že trn pasuje do násady.</li>'
          '<li>Příliš tuhá násada pro lehkého hráče. Nedostane ji do ohybu a střela ztrácí sílu.</li>'
          '<li>Zkrácení násady bez měření v bruslích. Řez je nevratný.</li>'
          '<li>Vynechání pásky a chrániče. Čepel bez pásky ztrácí kontrolu nad pukem a chrániče ochrání čepel při přepravě.</li></ul>'
          '<h2>Péče o čepele a násady</h2>'
          '<p>Po tréninku čepel otřete suchým hadrem a nenechávejte ji mokrou v tašce, protože dřevěné a laminované čepele nasávají vlhkost a deformují se. Na přepravu použijte chránič čepele. Hokejky skladujte svisle nebo ležící, nikoli opřené o zeď s ohýbáním. Praskliny, odlupování laminátu nebo změna tuhosti jsou důvod k výměně, protože prasklá čepel nebo násada se může při hře zlomit. Nože brusle po tréninku osušte, ať nezrezaví.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>V této kategorii se často prodává stejný profil ve více variantách: levá a pravá, juniorská a seniorská. Při porovnávání proto sledujte, aby karta produktu odpovídala vašemu označení, a u držáků a nožů ověřte kompatibilitu v popisu. Případné rozdíly v ceně mezi obchody jsou důležité, ale u součástek je jistota správné velikosti ještě důležitější než nejnižší nabídka.</p>',
    faq=[
        ('Jak poznám, jestli potřebuji levou, nebo pravou čepel?', 'Záleží na tom, kterou rukou držíte násadu dole. Levák drží hokejku levou rukou dole a potřebuje levou čepel. Pokud si nejste jistí, vezměte hokejku do rukou před zrcadlem nebo ve své sportovní prodejně.'),
        ('Mohu dát čepel jedné značky do násady jiné?', 'Někdy ano, ale rozměr trnu a dutiny se mezi značkami liší. Bezpečnější je kombinace od stejného výrobce nebo ověření kompatibility u prodejce.'),
        ('Jaký ohyb čepele je nejuniverzálnější?', 'Střední ohyb s mírným otevřením se hodí pro většinu rekreačních hráčů. Extrémní ohyby doporučujeme jen hráčům, kteří vědí, co od nich chtějí.'),
        ('Je lepší dřevěná, nebo kompozitní čepel?', 'Dřevěná čepel je levnější a má jiný pocit, kompozit je lehčí a odezva je rychlejší. Kompozity vydrží méně úderů do desky, proto je děti často nepotřebují.'),
        ('Jak dlouhá má být hokejová násada?', 'S bruslemi na nohou by měla sahat zhruba k bradě. Kratší násada je lepší pro práci s pukem, delší pro dosah a obranu.'),
        ('Co znamená tuhost násady?', 'Tuhost popisuje, jak moc se násada prohýbá při střele. Vyšší číslo znamená tužší násadu. Správná tuhost zvyšuje výkon, špatná ho snižuje.'),
        ('Dá se kompozitní čepel opravit?', 'Praskliny v kompozitu se spolehlivě opravit nedají a poškozenou čepel doporučujeme vyměnit. Povrchová poškození lze zakrýt páskou, ale konstrukce je oslabena.'),
        ('Proč jsou v kategorii i držáky a nože brusle?', 'Jde o výměnné součásti vybavení. Nepatří k hokejce, ale k bruslím, a kupují se podobným způsobem, tedy po opotřebení jednotlivých dílů.'),
        ('Je potřeba čepel lepit sám?', 'Správné zalepení vyžaduje zahřátí a čas na vytvrdnutí. Nezkušenému hráči doporučujeme nechat výměnu na servisu nebo prodejně hokejového vybavení.'),
        ('Jak poznám, že se čepel opotřebovala?', 'Špička je ztupená, hrana se odlupuje, čepel ztrácí tuhost nebo se v ní objevují praskliny. Takovou čepel je vhodné vyměnit, aby nezpomalila hru a neohrozila hráče.'),
    ])

# ------------------------------------------------------------------ skialpove-lyze
NEW['skialpove-lyze'] = dict(long=True,
    title='Skialpové lyže: šířka, délka, váha, výběr',
    desc='Skialpové lyže i kompletní sety s vázáním a pásy. Jak zvolit šířku, délku, váhu a rádius podle terénu a porovnat nabídky českých obchodů.',
    intro='<p>Skialpové lyže jsou kompromis mezi tím, co chcete vynést do kopce, a tím, co chcete cítit při sjezdu. Čím užší a lehčí lyže, tím méně sil spotřebujete při výstupu, ale tím víc je nutné uzpůsobit styl jízdy. Širší lyže zase vynesou do prašanu, ovšem jsou těžší. Sporteka porovnává nabídky českých obchodů u samotných lyží, kompletních setů s vázáním a pásy i u použitých kusů. Najdete tu i doplňky jako stoupací pásy nebo pásky.</p>'
          '<p>V kategorii jsou značky ' + B(('dynafit', 'Dynafit'), ('kastle', 'Kästle'), ('simond', 'Simond'), ('hagan', 'Hagan'), ('wedze', 'Wedze'), ('k2', 'K2'), ('dynastar', 'Dynastar'), ('toko', 'Toko')) +
          '. K lyžím patří <a href="/skialpove-boty/">skialpové boty</a>, <a href="/skialpove-vazani/">skialpová vázání</a>, <a href="/skialpove-pasy/">stoupací pásy</a> a obecný přehled v kategorii <a href="/skialpinismus/">skialpinismus</a>.</p>',
    guide='<h2>Co skialpová lyže dělá jinak než sjezdová</h2>'
          '<p>Skialpová lyže se musí dobře nosit na zádech, přenášet na botě a stoupat s pásy. Proto bývá lehčí než sjezdová, často se světlejším jádrem, a ne tak tuhá. Hrany a rocker se přizpůsobují stoupání a jízdě po různém sněhu. Lyže mívají zářez nebo úchyt na špičce a patě pro stoupací pásy a hodí se pro vázání s pinovou technologií, které se na ně montuje šrouby.</p>'
          + T(['Druh', 'Typická šířka pod vázáním', 'Zaměření'], [
              ['Závodní (race)', 'velmi úzké, kolem 60 až 70 mm', 'rychlé výstupy a soutěže'],
              ['Lehké túrové', 'zhruba 75 až 85 mm', 'dlouhé túry, výstupy na hřebeny'],
              ['Univerzální túrové', 'zhruba 85 až 95 mm', 'nejširší využití v našich horách a Alpách'],
              ['Freetouring', 'zhruba 95 až 105 mm', 'sjezd v prašanu, kratší výstupy'],
              ['Freeride', 'nad 105 mm', 'volný terén, těžší a stabilnější']]) +
          '<p>Rozmezí šířek jsou orientační a výrobci je vymezují odlišně. Pro orientaci v nabídce se ale hodí: modely označené čísly 80 až 90 jsou univerzální, kolem 100 míří na sjezd v prašanu. V nabídce vidíte modely Radical, Seven Summits, TX, Wayback nebo M-Vertical, jejichž čísla většinou odpovídají šířce pod vázáním.</p>'
          '<h2>Šířka lyže a sníh</h2>'
          '<p>Šířka se volí podle terénu. V našich horách se většinou lyžuje po upraveném nebo těžkém sněhu, a proto nejlépe slouží lyže s užším tělem, které se snadno otáčí. V Alpách a ve vyšších horách ocení lyžaři širší model do prašanu a rozbitého sněhu.</p>'
          '<ul><li><strong>Úzká lyže:</strong> lehčí, lépe drží hranu na tvrdém sněhu a stoupá úsporněji.</li>'
          '<li><strong>Široká lyže:</strong> nese v prašanu, ale ve strmé a zmrzlé trase je méně přesná a hůř se obrací.</li>'
          '<li><strong>Středně široká:</strong> pro většinu uživatelů nejbezpečnější volba na jednu lyži.</li></ul>'
          '<h2>Délka lyží</h2>'
          '<p>Skialpové lyže bývají o něco kratší než sjezdové. Obvykle sahají mezi bradu a čelo, ale přesnou délku ovlivňuje váha, kondice, styl jízdy a terén. Kratší lyže jsou lehčí a obratnější v úzkých žlebech, delší stabilnější a lépe nesou. Výrobce často doporučuje délky pro tělesnou výšku a váhu, proto se je vyplatí zkontrolovat.</p>'
          '<ul><li><strong>Lyžaři ve strmém terénu:</strong> kratší lyže pro rychlejší otáčení.</li>'
          '<li><strong>Těžší lyžaři a zkušení:</strong> o něco delší pro nosnost.</li>'
          '<li><strong>Ženy a lehčí uživatelé:</strong> dámské modely se vyrábějí s měkčím flexem a kratšími délkami. V nabídce jsou označeny W.</li></ul>'
          '<h2>Hmotnost</h2>'
          '<p>Hmotnost je u skialpových lyží klíčový parametr, protože se na každém kroku zvedá. Každých několik set gramů navíc se v dlouhém výstupu projeví únavou. Lehké lyže mají méně materiálu a bývají nervóznější při rychlé jízdě. Uvažujte o celém balíku: lyže, vázání, boty a pásy. U poměrně těžkých lyží má smysl zvolit lehčí vázání a boty.</p>'
          '<h2>Rádius, rocker a konstrukce</h2>'
          '<ul><li><strong>Rádius:</strong> udává, jak ostře lyže zatáčí. Menší rádius je hbitější, větší stabilnější.</li>'
          '<li><strong>Rocker (zdvih):</strong> zvednutá špička a patka usnadňují jízdu v prašanu. Moc velký rocker zhoršuje stabilitu na tvrdém sněhu.</li>'
          '<li><strong>Jádro:</strong> dřevěné jádro nabízí příjemný pocit, kompozitní nebo pěnové je lehčí.</li>'
          '<li><strong>Tvar špičky a patky:</strong> háček pro pásy na špičce a výřez na patce jsou potřeba pro univerzální pásy.</li></ul>'
          '<h2>Lyže, set nebo samostatné součásti</h2>'
          '<p>V nabídce je několik úrovní kompletace. Rozdíly jsou praktické i finanční.</p>'
          '<ul><li><strong>Samotné lyže bez vázání:</strong> pro zkušené, kteří mají vlastní vázání a boty a řeší jen lyži.</li>'
          '<li><strong>Lyže s vázáním a pásy:</strong> pro začátečníky, kteří chtějí vše pohromadě a smontované. Pro takový set je dobré ověřit, zda je vázání namontované obchodem.</li>'
          '<li><strong>Dámské a dětské sety:</strong> s přizpůsobenými délkami, tuhostí a vázáním.</li>'
          '<li><strong>Použité sety:</strong> levnější cesta, ale vyžadují kontrolu stavu hran, skluznice, vázání a funkce uvolňování. Starší vázání je dobré nechat zkontrolovat v servisu.</li></ul>'
          '<p>Při sestavování celku sledujte, zda lyže, vázání a boty spolu pasují. Pro pinové vázání potřebujete boty s příslušnými vložkami, pro rámové vázání zase boty s klasickou podrážkou. Vyberte je v kategoriích <a href="/skialpove-vazani/">skialpová vázání</a> a <a href="/skialpove-boty/">skialpové boty</a>.</p>'
          '<h2>Stoupací pásy</h2>'
          '<p>Pásy jsou textilie s lepicí vrstvou, které se přilepí na skluznici a umožní stoupání. Pro každý model lyží se vyrábějí pásy na míru nebo univerzální na zastřižení. Pásy mají špičkové a patní uchycení. Po sezoně je třeba chránit lepicí vrstvu a pásy přilepit na ochrannou fólii. Větší nabídku najdete v kategorii <a href="/skialpove-pasy/">skialpové stoupací pásy</a>. Pásky na lyže, které se v kategorii vyskytují, slouží ke spojení lyží při nošení.</p>'
          '<h2>Pro koho se které lyže hodí</h2>'
          '<ul><li><strong>Začátečník:</strong> univerzální túrová lyže s nižší hmotností, kompletní set s vázáním.</li>'
          '<li><strong>Víkendový turista:</strong> lyže kolem 85 až 95 mm, vyvážené mezi hmotností a stabilitou.</li>'
          '<li><strong>Sjezdově orientovaný:</strong> širší model s vyšší stabilitou, zbytek výbavy odpovídající.</li>'
          '<li><strong>Závodník:</strong> závodní úzká lyže a lehká výbava.</li>'
          '<li><strong>Rodiče s dětmi:</strong> juniorské sety, které rostou s dítětem. Pro děti je bezpečnost vázání důležitější než hmotnost.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Volba lyží podle sjezdu bez ohledu na výstup. Většinu času se na túře stoupá.</li>'
          '<li>Příliš široké lyže pro začátečníka, který jezdí v našich horách po upraveném terénu.</li>'
          '<li>Nekompatibilní vázání, boty a lyže. Před koupí si ověřte, co spolu funguje.</li>'
          '<li>Podcenění bezpečnostního vybavení. Ke skialpinismu patří i lavinový set, o němž se informujte u horských vůdců a odborných kurzů.</li>'
          '<li>Zanedbání skluznice a hran. Lyže s poškozenou skluznicí se špatně klouže a ztrácí stabilitu.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Po túře lyže osušte, zejména hrany, aby nerezly. Skluznici je dobré pravidelně voskovat a poškození opravit. Pro vosky a péči slouží kategorie <a href="/lyzarske-vosky/">lyžařské vosky</a>. Pásy sundejte, slepte je lepicími stranami k sobě nebo na ochrannou fólii a skladujte v suchu. Lyže nenechávejte přes léto na slunci ani v horku, mohou se deformovat. Před sezonou nechte zkontrolovat vázání a seřídit uvolňování.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Stejný model se prodává v různých délkách a barevných provedeních a dostupnost se mezi obchody liší. Důležité je porovnat, co je součástí balení: pouze lyže, lyže s vázáním, nebo i pásy. Zvláštní pozornost věnujte ročníku, protože starší ročník bývá obvykle stejně kvalitní, jen s jinou grafikou.</p>',
    faq=[
        ('Jakou šířku skialpových lyží zvolit na začátek?', 'Pro většinu začátečníků se hodí univerzální šířka kolem 85 až 95 mm pod vázáním. Je dost lehká na stoupání a stále stabilní při sjezdu.'),
        ('Jak dlouhé mají skialpové lyže být?', 'Obvykle sahají mezi bradu a čelo, ale přesnou délku ovlivňuje váha, terén a styl. Řiďte se doporučením výrobce a ověřte si tabulku ke konkrétnímu modelu.'),
        ('Kolik by skialpová lyže měla vážit?', 'Čím méně, tím snazší výstup, ale i nervóznější jízda. Pro začátek zvolte rozumný kompromis a celkově řešte lehké boty a vázání, protože celek rozhoduje.'),
        ('Potřebuji speciální vázání?', 'Ano, skialpová vázání umožňují zvednutí paty při stoupání. Existují pinová a rámová a každé potřebuje odpovídající boty.'),
        ('Co jsou stoupací pásy a proč je potřebuji?', 'Jsou to pásy, které se přilepí na skluznici a nedovolí lyžím klouzat zpět. Bez nich se do svahu nevystoupí.'),
        ('Dá se jezdit na skialpových lyžích na sjezdovce?', 'Ano, ale lehké lyže jsou na tvrdém upraveném svahu méně stabilní než sjezdové. Pro občasné sjezdovky stačí, pro pravidelnou jízdu je lepší sjezdové lyže.'),
        ('Je použitý skialpový set dobrý nákup?', 'Může být, pokud jsou hrany a skluznice v pořádku a vázání se nechá zkontrolovat v servisu. Bezpečnost vázání se nikdy nepodceňuje.'),
        ('Jaký je rozdíl mezi dámskou a pánskou lyží?', 'Dámské modely bývají lehčí, kratší a s měkčím flexem, protože se počítá s nižší hmotností lyžařek. Přesná konstrukce se u značek liší.'),
        ('Jak skladovat skialpové lyže přes léto?', 'V suchu a ve stabilní teplotě. Hrany promažte voskem, pásy slepte a lyže nenechávejte na přímém slunci, kde by se mohla deformovat skluznice nebo lepidlo pásů.'),
        ('Co ještě potřebuji ke skialpinismu kromě lyží?', 'Boty, vázání, pásy, hole a lavinovou výbavu. Základní bezpečnostní vybavení a znalosti si ověřte u odborníků a v kurzu.'),
    ])

# ------------------------------------------------------------------ golfove-micky
NEW['golfove-micky'] = dict(long=True,
    title='Golfové míčky: konstrukce, kompresní, výběr',
    desc='Golfové míčky pro začátečníky i pokročilé: dvouvrstvé, vícevrstvé, hrané a barevné. Jak vybrat a porovnat nabídky českých obchodů.',
    intro='<p>Golfový míček je malý, ale určuje, jak se hra cítí. Liší se konstrukcí, tvrdostí, počtem vrstev a povrchem, a tyto rozdíly ovlivňují dolet, rotaci i pocit při puttu. Sporteka porovnává nabídky českých obchodů u míčků v krabičkách po dvanácti kusech, ve větších baleních i u hraných míčků, a také u barevných a dárkových sad. Najdete tu i doplňky, které s míčky souvisejí, například šablonu na značení.</p>'
          '<p>V kategorii jsou značky ' + B(('inesis', 'Inesis'), ('srixon', 'Srixon'), ('volvik', 'Volvik'), ('titleist', 'Titleist'), ('taylormade', 'TaylorMade'), ('wilson', 'Wilson'), ('bridgestone', 'Bridgestone'), ('callaway', 'Callaway')) +
          '. Do bagu patří také <a href="/golfove-hole/">golfové hole</a>, <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a>, <a href="/golfove-obleceni-a-obuv/">oblečení a obuv</a> a <a href="/golfove-doplnky/">golfové doplňky</a>.</p>',
    guide='<h2>Z čeho se golfový míček skládá</h2>'
          '<p>Míčky se od sebe liší konstrukcí. Jádro, vrstvy a obal tvoří celek, jehož charakter určuje, jak míček reaguje na úder holí. Čím víc vrstev, tím víc se dá hrou ovlivnit, ale míček je dražší a vyžaduje větší techniku.</p>'
          + T(['Konstrukce', 'Charakter', 'Pro koho'], [
              ['Dvouvrstvý', 'pevné jádro a tvrdší obal, dolet, nižší spin', 'začátečníci a rekreační hráči'],
              ['Třívrstvý', 'střední vrstva zlepšuje kontrolu a pocit', 'pokročilejší hráči s pravidelnou hrou'],
              ['Čtyř- a pětivrstvý', 'precizní kontrola na krátkých úderech', 'zkušení hráči a soutěžící'],
              ['Distanční míček', 'tvrdý obal, maximalizuje dolet a odolnost', 'hráči s pomalejším švihem nebo na rovné hřiště'],
              ['Měkký míček (soft)', 'nízká komprese, příjemný pocit', 'hráči, kteří chtějí měkký pocit při puttu']]) +
          '<p>V nabídce uvidíte pojmy jako Pro V1, Pro V1x, Tour Soft, TruFeel nebo Distance. Jde o pojmenování řad, ne o přesnou konstrukci. Konstrukční informace najdete v popisu každého výrobce.</p>'
          '<h2>Komprese a pocit</h2>'
          '<p>Komprese označuje, jak moc se míček při úderu stlačí. Nízká komprese znamená měkčí pocit a snadnější práci s menší rychlostí švihu. Vysoká komprese se hodí k rychlému švihu a lepšímu přenosu energie. Výrobci tento údaj uvádějí rozdílně a ne vždy. Spolehlivější je vyzkoušet několik řad a vybrat tu, která hráči vyhovuje.</p>'
          '<ul><li><strong>Pomalejší švih:</strong> měkké míčky s nižší kompresí obvykle pomohou dosáhnout lepšího doletu.</li>'
          '<li><strong>Rychlý švih:</strong> pevnější míček lépe využije rychlost a drží tvar.</li>'
          '<li><strong>Chip a putt:</strong> měkký obal znamená přesnější cit, ale zároveň rychlejší opotřebení.</li></ul>'
          '<h2>Dolet, spin a ovladatelnost</h2>'
          '<p>Dolet a spin jsou protichůdné vlastnosti. Míček, který letí daleko, bývá méně ovladatelný v okolí jamky. Míček s větším spinem se dobře zastaví na greenu, ale s dlouhou holí je citlivější na chyby a kroutí se do stran. Proto se rozhodnutí o míčku opírá o to, co hráč nejvíc potřebuje.</p>'
          '<ul><li><strong>Dlouhé hole:</strong> nižší spin znamená přímější let a menší kroutění při chybách.</li>'
          '<li><strong>Krátké hole a wedge:</strong> vyšší spin dává kontrolu a zastavení na greenu.</li>'
          '<li><strong>Začínající hráči:</strong> mají prospěch z míčku, který odpouští nepřesný úder.</li></ul>'
          '<h2>Povrch, dimply a barva</h2>'
          '<p>Povrch míčku pokrývají důlky, takzvané dimply, které stabilizují let. Jejich tvar a počet se u řad liší a ovlivňují trajektorii. Obal je z ionomeru nebo z polyuretanu. Ionomer je tvrdší a odolnější, polyuretan měkčí a s lepším citem, ale rychleji se ošoupe.</p>'
          '<ul><li><strong>Bílé míčky:</strong> klasika, dobře viditelné na trávníku, pro většinu hráčů dostačují.</li>'
          '<li><strong>Žluté míčky:</strong> lépe viditelné za šera a v listí. Barevné míčky v nabídce se objevují u řady značek.</li>'
          '<li><strong>Neonové a reflexní míčky:</strong> pomáhají najít míček v rough, ale ne každá barva je vidět všude: na zvadlé trávě pomůže výrazný odstín a na sněhu je nejlepší výrazně kontrastní barva, třeba oranžová.</li>'
          '<li><strong>Značení:</strong> každý hráč by měl svůj míček označit fixem nebo šablonou, aby ho odlišil od cizích. Šablony na míčky se v nabídce také objevují.</li></ul>'
          '<h2>Typy balení a hrané míčky</h2>'
          '<p>Nejčastější balení je krabička po dvanácti kusech neboli dozen. Najdete také tříkusová a čtyřkusová balení, dárkové sady s markerem a větší balení po dvaceti čtyřech nebo více kusech. Samostatnou skupinou jsou hrané míčky, tedy použité míčky vytříděné podle kvality. Označují se třídou nebo písmenem a jsou levnější cestou, jak si zahrát bez obav o ztrátu.</p>'
          '<ul><li><strong>Nové míčky:</strong> garantovaný stav a charakter, ideální pro soutěže.</li>'
          '<li><strong>Hrané míčky:</strong> vhodné pro trénink, začátečníky a hřiště s vodou. Hodnocení kvality dělá prodejce a liší se mezi obchody.</li>'
          '<li><strong>Dárkové a tematické sady:</strong> mají design, ale konstrukce bývá jednodušší. V nabídce jsou i sady s postavami a markery.</li>'
          '<li><strong>Míčky s potiskem:</strong> pro firemní dárky a turnaje, často v dlouhém dodacím čase.</li></ul>'
          '<h2>Jak vybrat míček podle úrovně hry</h2>'
          '<ul><li><strong>Začátečník:</strong> dvouvrstvý míček s nižší cenou a pevným obalem. Ztráty jsou časté, proto se levnější hrané míčky vyplatí.</li>'
          '<li><strong>Rekreační hráč:</strong> měkčí dvouvrstvý nebo třívrstvý míček s příjemným citem.</li>'
          '<li><strong>Pokročilý hráč:</strong> třívrstvý a vícevrstvý míček s vyšší kontrolou.</li>'
          '<li><strong>Soutěžní hráč:</strong> míček s odpovídajícím charakterem a stejná řada v celé sadě.</li>'
          '<li><strong>Senioři a hráči s pomalejším švihem:</strong> měkké míčky s nižší kompresí a přímým letem.</li></ul>'
          '<h2>Pravidla a hraní s míčkem</h2>'
          '<p>Na oficiálních turnajích se obvykle hraje míčkem, který je na seznamu schválených míčků řídícího orgánu golfu. Rekreační hráči se tím nemusí řídit, ale pokud plánujete soutěže, ověřte si podmínky turnaje. Je dobré svůj míček označit a rozlišit od ostatních, což pravidla golfu doporučují. Odlišné míčky se nemají střídat v průběhu jamky, pokud pravidla neříkají jinak.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupování drahého tour míčku začátečníkem. Přínos se projeví až při pravidelné a přesné hře.</li>'
          '<li>Střídání řad bez systému. Pro srovnání je lepší hrát jednou řadou, než poznáte její chování.</li>'
          '<li>Podcenění viditelnosti. Bílý míček v rough nebo za soumraku se hledá hůř.</li>'
          '<li>Nákup velkého balení bez vyzkoušení. Vyzkoušejte několik kusů a pak teprve vezměte větší balení.</li>'
          '<li>Nekontrolování stavu hraných míčků. Poškozený obal nebo odřený povrch míček zhoršuje.</li></ul>'
          '<h2>Péče o míčky</h2>'
          '<p>Míčky se nemusí nijak složitě ošetřovat, stačí je po hře opláchnout vlažnou vodou s trochou saponátu a osušit. Vyhněte se extrémním teplotám: míčky ponechané v autě na slunci nebo v mrazu mohou změnit pocit. Zkontrolujte obal, zda nemá rýhy po úderu o železo. Míček s hlubokým poškozením se pro vážnější hru nehodí. Pro cvičení používejte levnější nebo hrané míčky a nové si nechte na kola.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Stejná řada míčků se liší dostupností, množstvím v balení a balením. Při porovnání proto sledujte počet kusů, a ne jen celkovou částku, a zkontrolujte, zda je zboží nové, nebo hrané. U míčků s potiskem a dárkových sad se podívejte na dodací lhůtu. Pokud hledáte konkrétní míček, hodí se vyhledávat podle řady a konstrukce.</p>',
    faq=[
        ('Jaký golfový míček je nejlepší pro začátečníka?', 'Pro začátek se hodí dvouvrstvý míček s pevným obalem a měkkým pocitem. Odpouští chybné údery, dobře letí a vydrží. Dražší tour míčky se vyplatí až při pravidelné hře.'),
        ('Čím se liší dvouvrstvý a třívrstvý míček?', 'Třívrstvý míček má další střední vrstvu, která zlepšuje kontrolu a pocit na krátkých úderech. Dvouvrstvý je pevnější a míří spíše na dolet a odolnost.'),
        ('Co je komprese míčku?', 'Komprese popisuje, jak moc se míček při úderu stlačí. Nižší komprese je měkčí a hodí se pomalejšímu švihu, vyšší lépe využije silné údery.'),
        ('Má smysl kupovat hrané míčky?', 'Ano, pro trénink, začátečníky a hřiště s překážkami. Kvalitní hrané míčky jsou levnější cesta, jen je třeba věřit prodejci při třídění podle kvality.'),
        ('Jak dlouho vydrží golfový míček?', 'Záleží na obalu a způsobu hry. Ionomerový obal vydrží déle, polyuretanový se rychleji ošoupe. Míček s viditelným poškozením vyměňte.'),
        ('Proč mají míčky důlky?', 'Důlky, tzv. dimply, ovlivňují obtékání vzduchu a stabilizují let. Jejich tvar a počet se u řad liší.'),
        ('Jakou barvu míčku zvolit?', 'Bílé míčky jsou standard. Žluté a neonové jsou lépe viditelné v rough nebo za šera. Záleží na vašich preferencích a podmínkách.'),
        ('Proč si míček značit?', 'Aby se odlišil od míčků ostatních hráčů, protože na hřišti se často hrají stejné řady. Fixem nebo šablonou označte vždy stejně, třeba symbolem.'),
        ('Mohu míčky různých značek míchat?', 'Při volné hře ano, ale chování se liší. Pro srovnání a postupné učení je lepší hrát jednou řadou a změnu dělat vědomě.'),
        ('Jak poznám, že míček není vhodný pro golf?', 'U golfového míčku najdete v popisu konstrukci (počet vrstev), počet kusů v balení a označení řady. Chybí-li tyto údaje, zboží raději ověřte u obchodu.'),
    ])


# ------------------------------------------------------------------ doplnění sekcí
NEW['detske-trikolky']['guide'] += (
    '<h2>Tříkolka v rodinném provozu: auto, byt, výlety</h2>'
    '<p>Praktické parametry často rozhodují víc než výbava. Tříkolka, která se špatně skládá nebo se nevejde do předsíně, zůstane brzy nevyužitá. Před koupí si proto představte, kde bude stát a jak se bude přenášet. Starší budovy bez výtahu a dlouhé schody znamenají, že se hodí lehčí rám a odnímatelná tyč.</p>'
    '<ul><li><strong>Rozměry po složení:</strong> ověřte, zda se tříkolka vejde do kufru auta spolu s kočárkem nebo koloběžkou.</li>'
    '<li><strong>Hmotnost:</strong> těžší modely s mnoha funkcemi se hůř zvedají, hlavně když v nich sedí dítě.</li>'
    '<li><strong>Povrch výletů:</strong> na dlažbě a asfaltu stačí plná nebo pěnová kola, na štěrku a trávě jsou potřeba větší a pružnější kola.</li>'
    '<li><strong>Parkování doma:</strong> chodba, sklep nebo balkon musejí unést rozměry, a kdo bydlí v paneláku, ocení kompaktní tvar.</li></ul>'
    '<h2>Co po tříkolce následuje</h2>'
    '<p>Tříkolka je přechodná etapa. Děti, které se naučí šlapat a řídit, obvykle brzy chtějí rychlejší nebo méně stabilní stroj. Nejčastější pokračování je <a href="/odrazedla/">odrážedlo</a>, na kterém se dítě učí držet rovnováhu bez pedálů, nebo <a href="/kolobezky/">koloběžka</a>. Později přichází první kolo, například <a href="/detska-kola-12-14-palcu/">dětské kolo 12 nebo 14 palců</a> a poté <a href="/detska-kola-16-palcu/">16palcové kolo</a>. Pro dítě s koloběžkou se hodí <a href="/freestyle-kolobezky/">freestyle koloběžky</a> až pro starší děti. Pokud tříkolku brzy nahradíte jinou, zvažte použitý kus nebo jednodušší model, protože dlouhodobý význam složitých funkcí je v tomto případě menší.</p>'
    '<p>Při přechodu pomůže, když dítě zná základní pravidla: brzdí, zatáčí v rozumné rychlosti a nejezdí k silnici. Pomoc s ochranou hlavy zajistí <a href="/detske-cyklohelmy/">dětská cyklistická helma</a>, která by měla dobře sedět a nesmí se pohybovat.</p>')
NEW['detske-trikolky']['faq'] += [
    ('Jak se tříkolka čistí?', 'Plasty a rám stačí otřít vlhkou utěrkou s jemným mýdlem. Textilní potahy se u většiny modelů dají sundat a vyprat, ale vždy dodržte pokyny výrobce.'),
    ('Je lepší nová, nebo použitá tříkolka?', 'Použitá tříkolka je rozumná volba, pokud je rám celý, kola se točí a pásy i zámky fungují. Nová dává jistotu stavu a záruku, což se hodí hlavně u modelů se složitým mechanismem.'),
    ('Kdy dát dítěti helmu?', 'Jakmile dítě začne jezdit samo a rychleji, než jde dospělý. Helma musí sedět pevně a nemá se pohybovat. Zvyk na ni se hodí i na pozdější kolo.'),
]
NEW['skialpove-lyze']['guide'] += (
    '<h2>Skialpové lyže v různých podmínkách</h2>'
    '<p>Stejná lyže se chová jinak podle sněhu. Na jaře na firnu je výhodou úzká lyže s dobrou hranou, v zimě na prašanu naopak ocení každý milimetr šířky navíc. Zvykněte si proto uvažovat o tom, kde budete lyžovat nejčastěji, a ne o výjimečných případech.</p>'
    '<ul><li><strong>Firn a jarní túry:</strong> hrana a nízká hmotnost, ranní start a krátké sjezdy.</li>'
    '<li><strong>Prašan:</strong> širší lyže se zdvihnutou špičkou a patkou.</li>'
    '<li><strong>Zledovatělý a rozbitý sníh:</strong> užší a tužší lyže drží stopu lépe.</li>'
    '<li><strong>Lesní túry v nížinách:</strong> kratší a obratné lyže pro úzké průseky.</li></ul>'
    '<h2>Lyže, boty a tuhost: ladění celku</h2>'
    '<p>Lyže nikdy nehrají samostatně. Přenos síly závisí na botě: měkká bota nevyužije tuhou a širokou lyži a naopak. Lehké lyže se snáz kombinují s lehkými botami, ale výhodu pro sjezd má tužší sada. Při nákupu proto zvažte, zda už máte boty. Pokud ne, zvolte nejdřív <a href="/skialpove-boty/">skialpové boty</a>, protože na komfortu nohy záleží nejvíc, a pak k nim hledejte lyže a <a href="/skialpove-vazani/">vázání</a>.</p>'
    '<p>Pro oblečení a doplňky na túru se hodí <a href="/lyzarske-helmy/">lyžařské helmy</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a>, <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-rukavice/">rukavice</a> a <a href="/lyzarske-termopradlo/">termoprádlo</a>. Při výstupu se vyplatí vrstvení a výměna triček, protože se člověk potí. Na sjezd se přidá teplejší vrstva. Pro zajímavost, <a href="/bezecke-lyze/">běžecké lyže</a> a <a href="/sjezdove-lyze/">sjezdové lyže</a> mají odlišný účel.</p>')
NEW['skialpove-lyze']['faq'] += [
    ('Má smysl kupovat dětský skialpový set?', 'Pro děti, které s rodiči chodí na túry pravidelně, ano. Pozor na rychlé dorůstání: lyže a boty se mění po několika sezonách. Dětský set se hodí také z druhé ruky, pokud je vázání zkontrolované.'),
    ('Jak se starat o stoupací pásy?', 'Po túře je osušte a slepte nebo přilepte na ochrannou fólii. Lepicí vrstvu chraňte před prachem a nečistotou. Při dlouhém skladování je uložte v suchu mimo teplo.'),
    ('Mohu na skialpových lyžích jezdit i mimo sníh?', 'Ne, lyže jsou určené pro sníh. Nošení po kamenech a štěrku poškodí skluznici i hrany.'),
]
NEW['golfove-micky']['guide'] += (
    '<h2>Míčky a hole: jak do sebe zapadají</h2>'
    '<p>Míček se vybírá vždy s ohledem na výbavu a styl. Hráč s pomalejším švihem a staršími holemi prospěje měkkému míčku s nízkou kompresí, zatímco silný hráč s moderními holemi potřebuje míček, který unese rychlost. Přepnutí na lepší míček nikdy nenahradí kvalitní trénink, ale rozdíl při krátkých úderech se dá cítit.</p>'
    '<ul><li><strong>Driver a dřevo:</strong> nízký spin pomáhá k přímému letu. Informace o vhodné holi najdete v kategorii <a href="/golfove-hole/">golfové hole</a>.</li>'
    '<li><strong>Železa a wedge:</strong> tady se projeví spin a kontrola. Měkký obal tolerantně reaguje na úder.</li>'
    '<li><strong>Putter:</strong> pocit míčku při puttu je subjektivní. Hráči často zkoušejí měkčí a tvrdší varianty.</li></ul>'
    '<h2>Příslušenství, tašky a oblečení</h2>'
    '<p>Míčky se nosí v kapse tašky, proto je dobré zvolit praktické uložení. V kategorii <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a> najdete modely s dostatkem kapes pro několik balení míčků. K hraní patří <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a> a drobnosti z kategorie <a href="/golfove-doplnky/">golfové doplňky</a>, například markery a tee. Jako příbuzný sport se nabízí <a href="/discgolf/">discgolf</a>, který je levný na vstup a nevyžaduje míčky. Obecný přehled je v kategorii <a href="/golf/">golf</a>.</p>'
    '<h2>Kolik míčků si vzít na kolo</h2>'
    '<p>Prakticky stačí tři až šest míčků pro rekreační hru, začátečník by měl počítat s větší rezervou, protože vodní překážky a rough míčky často spolknou. Jedno balení po dvanácti kusech vydrží začátečníkovi na několik kol a zkušenějšímu hráči na delší dobu. Při trénování na cvičišti je rozumné použít hrané míčky a soutěžní si nechat na hřiště.</p>')
NEW['golfove-micky']['faq'] += [
    ('Kolik míčků si vzít na kolo?', 'Pro rekreační kolo obvykle stačí tři až šest kusů. Začátečník by měl vzít víc kvůli ztrátám ve vodě a v roughu.'),
    ('Dají se míčky prát?', 'Stačí je opláchnout vlažnou vodou s malým množstvím saponátu a utřít. Silná chemie a mytí v myčce nejsou vhodné, mohou poškodit obal.'),
    ('Jaký je rozdíl mezi míčkem s ionomerovým a polyuretanovým obalem?', 'Ionomer je tvrdší, odolnější a obvykle levnější. Polyuretan je měkčí, dává větší cit a spin, ale rychleji se ošoupe.'),
]
NEW['hokejove-cepele-a-nasady']['guide'] += (
    '<h2>Čepel, násada a ostatní výstroj</h2>'
    '<p>Při skládání hokejky se hodí vědět, jak součásti spolupracují. Hráč s ochrannou výstrojí, <a href="/hokejove-chranice/">chrániči</a> a <a href="/hokejove-helmy-a-mrizky/">helmou s mřížkou</a>, má sice jiné nároky než dítě na rekreačním bruslení, ale hokejka patří k základům u všech. Pro přenášení i skladování se hodí <a href="/hokejove-tasky/">hokejová taška</a> s prostorem pro čepel a nástavce.</p>'
    '<p>Pro přehled různých hokejek vám poslouží kategorie <a href="/hokejky/">hokejky</a>, pro trénink střelby <a href="/hokejove-puky-a-branky/">puky a branky</a> a pro hráče pozemního hokeje samostatná kategorie <a href="/pozemni-hokej/">pozemní hokej</a>. Pro oblečení slouží <a href="/hokejove-dresy-a-obleceni/">dresy a hokejové oblečení</a>.</p>')
NEW['hokejove-cepele-a-nasady']['faq'] += [
    ('K čemu je chránič čepele?', 'Chrání čepel při přepravě a skladování před nárazy a otěrem, a také chrání ostatní výstroj před ostrým koncem. Nasazuje se na čepel mimo led.'),
]

NEW['hokejove-cepele-a-nasady']['faq'] += [
    ('Jak často měnit čepel?', 'Neexistuje pevný interval. Při pravidelném hraní se dřevěná čepel opotřebuje za několik týdnů, kompozitní vydrží déle, ale může prasknout při nárazu. Sledujte tvar špičky, tuhost a trhliny a podle toho čepel vyměňte. Hráči, kteří hrají na ledu několikrát týdně, ji mění častěji než rekreační hráči.'),
    ('Mohu používat hokejbalovou čepel na led?', 'Plastová čepel pro hokejbal je určená pro asfalt a lepší skluz na ledu nenabídne, protože materiál i tvar jsou jiné. Na led používejte čepele určené pro led.'),
]
NEW['skialpove-lyze']['faq'] += [
    ('Jaký je rozdíl mezi skialpovou lyží a lyží na freeride?', 'Freeridová lyže je širší, těžší a stabilnější, určená především pro sjezd. Skialpová je lehčí, aby se snadno stoupalo, a proto mívá užší tělo. Mezi nimi leží freetouringové modely, které kombinují obojí.'),
    ('Kdy je lepší zvolit lyže bez vázání?', 'Když už máte vázání, které chcete přemontovat, nebo když vybíráte vázání zvlášť podle bot. Montáž vázání patří do servisu, aby bylo správně nastavené a bezpečné.'),
]
NEW['golfove-micky']['faq'] += [
    ('Jaký míček zvolit pro hru v zimě nebo za chladu?', 'V chladu míčky tvrdnou a letí kratší, proto se hodí měkčí míčky s nižší kompresí. Barevné míčky jsou lépe vidět na zvadlé trávě, na sněhu je lepší výrazně kontrastní barva, třeba oranžová.'),
    ('Kolik stojí vyzkoušet několik řad míčků?', 'Praktické je koupit menší balení po třech kusech nebo hrané míčky a vyzkoušet několik řad. Cena je u nich nižší než u dvanáctikusových krabiček a rozhodnutí se opírá o vlastní pocit.'),
]
