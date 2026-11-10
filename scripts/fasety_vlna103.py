"""sporteka.cz — facet landing texts wave 103: kopacky-adidas, nike-leginy, detska-kolobezka, damske-kratasy.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ kopacky-adidas
NEW['kopacky-adidas'] = dict(
    title='Kopačky Adidas: F50, Predator a Copa podle stylu hry',
    desc='Kopačky Adidas v řadách F50, Predator a Copa. Jak poznat rozdíl mezi rychlostními a kontrolními modely, vybrat povrch a velikost a porovnat obchody.',
    intro='<p>Adidas staví nabídku kopaček na třech základních řadách, které dávají smysl i bez znalosti marketingu: F50 pro rychlé hráče, Predator pro ty, kdo chtějí mít míč pod kontrolou, a Copa pro příznivce měkkého dotyku a klasického střihu. Starší modely X Crazyfast v obchodech doznívají a často se ještě objevují za výhodnější nabídku. '
          'Na této stránce jsou kopačky této značky z kategorie <a href="/kopacky/">kopačky</a>, od dětských modelů po dospělé verze pro trávu, umělku i halu. Průvodce vysvětluje, jak se řady liší, co znamenají zkratky a přípony v názvech, jak vybrat úroveň League, Club nebo Pro a v čem se Adidas liší od konkurence, třeba od <a href="/kopacky-nike/">Nike</a> nebo <a href="/kopacky-puma/">Pumy</a>. Pro mladé hráče se hodí i výběr <a href="/detske-kopacky/">dětských kopaček</a>.</p>',
    guide='<h2>Tři řady, tři povahy hráče</h2>'
          '<p>Kdo poprvé otevře nabídku kopaček Adidas, narazí na názvy, které nic neříkají. Za nimi se skrývá poměrně přehledné členění. Každá řada má jiný důraz a podle něj ji zvolíte lépe než podle barvy nebo podle toho, co nosí oblíbený hráč.</p>'
          + T(['Řada', 'Zaměření', 'Pro koho'], [
              ['F50', 'rychlost, lehká a tenká svrchní část', 'křídla, útočníci, hráči, kteří běží s míčem a často sprintují'],
              ['Predator', 'kontrola míče, potah s texturou pro tření o míč', 'středopolaři, tvůrci hry, střelci spoléhající na přesnost'],
              ['Copa', 'měkký dotek a pohodlí od prvního tréninku', 'hráči, kteří chtějí klasický pocit a bezproblémové rozchození'],
              ['X Crazyfast', 'předchozí rychlostní řada, dnes dobíhající', 'hráči hledající starší model za zajímavější nabídku']]) +
          '<p>Rozdělení není absolutní. Obrance může s radostí hrát ve F50, pokud ho baví dlouhé sprinty do prostoru, a křídelník se může cítit lépe v Predatoru. Řada říká, co se výrobce snažil zdůraznit, ne co smíte nosit. Dobré pravidlo zní vyzkoušet jedny kopačky při tréninku a teprve potom kupovat na celou sezonu.</p>'
          '<h2>League, Club a Pro: kolik opravdu potřebujete</h2>'
          '<p>Stejný model se prodává ve více úrovních a v názvech se objevují slova League, Club a Pro. Úroveň League stojí uprostřed a pro většinu amatérských hráčů je rozumný kompromis. Bývá odolnější a poctivěji vyrobená než nejlevnější Club, který míří na děti, začátečníky a hobby kopání, a nemá takové zpracování jako špičková Pro. Pokud hrajete jednou týdně v lize nebo na turnajích, League vás nezklame. Pokud hrajete třikrát týdně a kopačky pořádně zatěžujete, vyplatí se podívat po vyšší úrovni, která víc drží tvar. Kdo hraje jen občas, ocení nižší úroveň a pohodlné rozchození bez zbytečných kompromisů.</p>'
          '<h3>Co znamenají přípony v názvech</h3>'
          + T(['Přípona', 'Význam', 'Poznámka'], [
              ['FG', 'pevný povrch, přírodní tráva', 'nejčastější varianta, kolíky tvarované pro drn'],
              ['MG / FG/MG', 'multi-ground, více povrchů', 'kompromis pro trávu i umělou trávu'],
              ['AG', 'umělá tráva', 'krátké kolíky rozložené po celé podrážce'],
              ['SG', 'měkká a rozbředlá tráva', 'méně a delší kolíky'],
              ['TF / Turf', 'umělka a tvrdý povrch', 'nopy místo kolíků, oblíbené u dětí a na tréninku'],
              ['IN / Indoor', 'hala', 'rovná guma, bez kolíků'],
              ['J / Kid', 'dětská verze', 'menší velikosti, někdy jednodušší materiály'],
              ['Laceless', 'bez tkaniček', 'čistší povrch, ale bez možnosti upravit utažení']]) +
          '<p>Nejvíc chyb vzniká u povrchu. Kdo má doma jen jeden pár a hraje střídavě na trávě a na umělce, měl by hledat variantu FG/MG, která drží i na umělé trávě a zároveň se dá nosit na přírodní. Na trvale tvrdém povrchu škvárového hřiště nebo na starší umělce vyhrají nopy typu Turf a na hale potřebujete Indoor. Další informace o površích najdete v kategorii <a href="/kopacky/">kopačky</a>.</p>'
          '<h2>Střih a velikost u Adidasu</h2>'
          '<p>Adidas nabízí obvykle dvě základní šířky podle řady. Predator a Copa bývají o něco volnější v přední části, F50 sedí těsněji kolem střední části nohy. Přesné rozdíly se u každé generace mění, proto ověřujte délku vložky v centimetrech a porovnávejte ji se skutečnou délkou chodidla. Postavte nohu na papír, označte nejdelší prsty a patu a přidejte zhruba půl centimetru až centimetr rezervy. Kdo má širší nohu, může s kopačkami F50 bojovat. Hledejte u něj raději Copa nebo širší pozdější variantu Predatoru, kde bývá víc místa v přední části.</p>'
          '<p>U dětí se spoléhejte na to, že chodidlo roste rychle. Dětské kopačky ve značení J nebo Kid mají zdvojenou náplň v zadní části a lehčí podrážku. Rezervu nechte kolem půl centimetru, víc dětem při hře vadí. Ve stejné nabídce najdete i Predator a F50 v dětské verzi, takže mladý hráč může mít stejný styl jako starší sourozenec.</p>'
          '<h2>Materiály a rozchození</h2>'
          '<p>Svršek kopaček Adidas bývá z jemné syntetiky, často v kombinaci s pletenou nebo síťovanou vrstvou. Syntetika nenasákne vodou tolik jako klasická useň, rychleji schne a nevyžaduje tak pečlivou údržbu. Copa zůstává modelem, který se k tradici přibližuje nejvíc, a proto se u ní vyplatí důkladně se rozchodit na trénincích. Pokud kopačky koupíte před zápasem, vezměte je alespoň dvakrát na lehký trénink, aby se tvar přizpůsobil noze. Při nošení nových kopaček v mokru se snadno stane, že se otlačí paty a malíčky, proto zkoušejte nejdřív na suchu.</p>'
          '<h3>Jak o kopačky pečovat</h3>'
          '<ul><li>Po zápase vyndejte vložky, vytáhněte tkaničky a nechte boty vyschnout při pokojové teplotě. Radiátor ani auto je nevysušují šetrně.</li>'
          '<li>Bláto smyjte vlažnou vodou a měkkým kartáčem. Agresivní čisticí prostředky poškozují povrchovou vrstvu.</li>'
          '<li>Do mokrých kopaček nacpěte noviny a po hodině je vyměňte, aby vysychaly zevnitř.</li>'
          '<li>Střídejte dva páry, pokud hrajete víc než dvakrát týdně. Kopačkám se tím prodlouží životnost.</li>'
          '<li>Kolíky pravidelně kontrolujte, hlavně u verzí SG s výměnnými kolíky. Zaoblené kolíky na tvrdém povrchu klouzou a zvyšují riziko zranění.</li></ul>'
          '<h2>Adidas v porovnání s konkurencí</h2>'
          '<p>Z hlediska nabídky patří Adidas k největším značkám v kategorii a skoro každý styl hry tu najde svůj model. Nike staví na rychlých modelech jako Mercurial a lehkých střelách, o nich se dozvíte víc na stránce <a href="/kopacky-nike/">kopaček Nike</a>. Puma se zaměřuje na pohodlný střih a široký rozsah úrovní, viz <a href="/kopacky-puma/">kopačky Puma</a>. Joma bývá oblíbená v klubovém prostředí díky praktické nabídce, podrobněji u <a href="/joma-kopacky/">kopaček Joma</a>, zatímco <a href="/mizuno-kopacky/">Mizuno</a> láká příznivce japonského zpracování a měkčí kůže. Další alternativy jsou <a href="/new-balance-kopacky/">New Balance</a> a <a href="/kopacky-under-armour/">Under Armour</a>. Z hlediska ceny a kvality platí, že rozdíl mezi značkami je menší než rozdíl mezi úrovněmi jedné značky.</p>'
          '<p>Příznivci růžové a pastelové palety najdou podobné barevné řešení na stránce <a href="/ruzove-kopacky-nike/">růžových kopaček Nike</a>. Značkové kopačky se prodávají v mnoha barevných edicích a barva často určuje rychlost, s jakou se model vyprodá. Pokud vám záleží na konkrétní variantě, sledujte dostupnost více obchodů najednou.</p>'
          '<h2>Co ke kopačkám koupit</h2>'
          '<p>K nové obuvi patří vhodné <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>, bez nich se nehraje ani na tréninku. Podle povrchu a úrovně se vyplatí zvolit i správný <a href="/fotbalove-mice/">fotbalový míč</a> a pro brankáře <a href="/brankarske-rukavice/">brankářské rukavice</a>. Na cestu na hřiště a z hřiště se hodí lehká <a href="/sportovni-obuv/">sportovní obuv</a>, ať si kopačky šetříte na zápas. Celý svět tohoto sportu najdete v sekci <a href="/fotbal/">fotbal</a>.</p>'
          '<h2>Jak číst nabídku obchodů</h2>'
          '<p>Stejný pár může mít v několika obchodech různý název. Někde stojí kompletní označení s barevnou kombinací, jinde jen řada a povrch. Při porovnávání proto sledujte tři věci: řadu, povrch a úroveň. Zkontrolujte také, zda obchod uvádí velikost v evropském značení, v britském nebo americkém, protože hodnoty se liší. Nákup přes obchod, který vrací zboží bez potíží, má smysl hlavně u kopaček, protože velikost se dá ověřit jen vyzkoušením. Nechte si proto vždy možnost vrátit, pokud by pár nesedl.</p>',
    faq=[
        ('Jaký je rozdíl mezi kopačkami Adidas F50 a Predator?',
         'F50 je řada pro rychlost, s lehkou a tenkou svrchní částí a těsnějším střihem. Predator klade důraz na kontrolu míče a přesné zakončení a bývá volnější v přední části. Výběr závisí na tom, jak hrajete, ne na tom, na jakém postu.'),
        ('Co znamená zkratka FG v názvu kopaček?',
         'FG označuje kopačky pro pevný povrch, tedy přirozenou trávu. Mají pevné kolíky stavěné pro drn. Na umělé trávě vydrží také, ale kolíky se tam rychleji opotřebují a mohou zatěžovat klouby.'),
        ('Mohu v kopačkách FG/MG hrát na umělé trávě?',
         'Ano, varianta FG/MG je navržená pro trávu i pro umělou trávu nové generace. Pokud hrajete hodně na umělce, hledejte raději AG, které má podrážku přesně upravenou pro tento povrch. FG/MG je rozumný kompromis pro střídavé používání.'),
        ('Jaký je rozdíl mezi úrovní League, Club a Pro?',
         'Club je základní verze pro děti, začátečníky a občasné hráče. League stojí uprostřed a hodí se pro většinu amatérů. Pro je špičková verze s nejlepším zpracováním a lehčí konstrukcí, určená pro hráče, kteří hrají často a na vyšší úrovni.'),
        ('Jak vybrat velikost kopaček Adidas?',
         'Změřte chodidlo v centimetrech, přidejte půl až jeden centimetr rezervy a porovnejte s délkou vložky uvedenou v obchodě. U šířky se orientujte podle řady: F50 sedí těsněji, Predator a Copa dávají víc místa. Nejistotu vyřeší zkouška na hřišti.'),
        ('Jsou dětské kopačky Adidas jiné než dospělé?',
         'Dětské modely ve značení J nebo Kid mají menší velikosti, upravenou podrážku a často jednodušší materiály svršku. Stylem odpovídají dospělým řadám, takže dítě může mít Predator nebo F50 stejně jako starší hráči. Rezerva do špičky by u dětí měla zůstat kolem půl centimetru.'),
        ('Proč jsou některé kopačky bez tkaniček?',
         'Laceless modely mají hladký svršek a nahrazují tkaničky pevným nasazením přes kotník. Povrch je čistší pro kontakt s míčem. Nevýhodou je, že nastavení utažení se řídí jen střihem a nelze ho jemně upravit.'),
        ('Jak poznat, že kopačky jsou vhodné na halu?',
         'Halové kopačky mají v názvu Indoor nebo IN a rovnou gumovou podrážku bez kolíků. Podrážka nesmí zanechávat stopy a musí držet na parketách. Do venku se nehodí, protože se rychle opotřebují a drží hůř než kolíky.'),
        ('Jak dlouho kopačky vydrží?',
         'Záleží na četnosti hraní, povrchu a péči. Při pravidelném tréninku několikrát týdně vydrží pár často jen jednu sezonu. Hraje-li hráč jednou týdně a boty po zápase čistí a suší, vydrží déle. Znamením konce je opotřebená podrážka a roztržený svršek.'),
        ('Proč se kopačky stejného modelu liší mezi obchody v názvu?',
         'Obchody přebírají názvy z různých datových zdrojů, někde je celý, jinde zkrácený a někdy v cizím jazyce. Rozhodující je řada, povrch a úroveň, ne přesný text. Porovnávejte tyto tři údaje a barvu, abyste neporovnávali odlišné modely.')
    ],
)

# ------------------------------------------------------------------ nike-leginy
NEW['nike-leginy'] = dict(
    title='Nike legíny: One, Pro a Swift podle činnosti',
    desc='Nike legíny řad One, Pro, Swift a Fast pro jógu, trénink i běh. Jak se liší střih, výška pasu a délka a kde porovnat dostupné velikosti.',
    intro='<p>Sortiment legín od Nike se dá rozdělit podle činnosti jednodušeji, než vypadá. Řada One je univerzální na cvičení, Pro míří na trénink s pevnějším přilnutím, Swift a Fast patří běhu a Sportswear Classic obvyklému nošení po městě. Ke každému typu existují varianty s různou délkou, výškou pasu a lehkou kapsou. '
          'Na této stránce jsou legíny značky Nike z kategorie <a href="/leginy/">legíny</a>, pro ženy, muže i děti. Průvodce vysvětluje, co se pod jednotlivými názvy skrývá, jak zvolit délku a pas, kdy se vyplatí Dri-FIT a jak se Nike liší od <a href="/under-armour-leginy/">Under Armour</a>, <a href="/gymbeam-leginy/">GymBeam</a> a dalších výrobců. Doplňkově si prohlédněte výběr <a href="/cerne-leginy/">černých legín</a>, protože právě černá tvoří většinu nabídky značky.</p>',
    guide='<h2>Rozluštění názvů: One, Pro, Swift, Fast a ostatní</h2>'
          '<p>Nike dává modelům krátká jména a ta se v nabídce obchodů opakují. Pokud je znáte, zjistíte rychle, na co kus míří. Přehled níže vychází z názvů, které se v nabídce skutečně objevují, a z obecného zaměření řad.</p>'
          + T(['Řada', 'Zaměření', 'Typické použití'], [
              ['One', 'univerzální sportovní legíny', 'fitness, cvičení, jóga, každodenní nošení'],
              ['Pro', 'přiléhavý tréninkový střih', 'posilovna, kondiční trénink, vrstva pod oblečení'],
              ['Swift', 'běžecké legíny, 7/8 délka, kapsa', 'běh po silnici a stezkách'],
              ['Fast', 'výkonnostní běh', 'rychlejší běh, tréninkové jednotky'],
              ['Tempo, Epic Fast', 'lehčí běžecké modely', 'běh v teplejším počasí'],
              ['Zenvy', 'měkčí materiál, nižší opora', 'jóga, pilates, protahování'],
              ['Sportswear Classic', 'volnočasová řada', 'město, škola, cestování']]) +
          '<p>Rozdělení slouží jako první orientace. Hranice mezi řadami nejsou přesné a výrobce je občas přeznačuje, ale jméno vždy napoví, zda se kus hodí na intenzivní pohyb, nebo na pohodlný den.</p>'
          '<h2>Výška pasu, délka a opora</h2>'
          '<p>U legín se rozhoduje dvěma volbami: výškou pasu a délkou. Vysoký pas drží břicho a zůstává na místě při dřepech a předklonech. Střední pas je pohodlný pro každodenní nošení, kdežto nízký se u sportovních legín skoro nenosí, protože sjíždí. Délky se označují způsobem, který jinde najdete u jiných značek: plná, 7/8, 3/4 a krátké. Plná délka se hodí na chladnější dny, 7/8 sahá těsně nad kotník a je běžná u běžeckých modelů, 3/4 se nosí v teple a krátká verze nahrazuje kraťasy.</p>'
          + T(['Délka', 'Kdy dává smysl', 'Poznámka'], [
              ['Plná', 'chladnější počasí, posilovna, jóga', 'nejuniverzálnější volba'],
              ['7/8', 'běh, fitness, každodenní nošení', 'neleze pod kotník, vypadá čistě'],
              ['3/4', 'teplejší dny, cvičení v sále', 'nechává volný kotník a lýtko'],
              ['Krátká', 'horko, tréninky s důrazem na pohyb', 'pod kraťasy nebo samostatně']]) +
          '<h3>Opora a komprese</h3>'
          '<p>Slovo komprese se v sortimentu používá volně. U legín Nike Pro jde o přiléhavý střih s pevnějším hmatem, který drží svaly, ale nejde o lékařskou kompresi. Pokud potřebujete skutečnou kompresi s měřeným tlakem, hledejte výslovně kompresní výrobky určené k regeneraci. Pro běžný trénink poskytuje pevnější úplet hlavně pocit jistoty a pomáhá při rychlých pohybech, kdy by volnější látka zbytečně přeskakovala po kůži.</p>'
          '<h2>Dri-FIT a materiály</h2>'
          '<p>Dri-FIT je označení látky Nike, která odvádí pot od kůže a rychle schne. V praxi znamená polyesterový úplet s elastanem, který dobře odvádí vlhkost a v noci vysychá na sušáku. Naproti tomu legíny z bavlněné směsi, často u řady Sportswear, jsou měkčí na dotek, ale po propocení déle schnou a na intenzivní sport se nehodí. Kdo cvičí ve vyhřátém sále nebo běhá v létě, ocení syntetiku. Kdo legíny nosí do školy nebo na výlet, preferuje pohodlnou bavlněnou směs.</p>'
          '<p>Zkouška neprůhlednosti patří k nejdůležitějším při koupi. Natáhněte látku přes dlaň a podívejte se, zda skrz prosvítá. U světlých barev a při hlubokém dřepu je průhlednost častější, tmavé odstíny jsou odolnější. Černá, kterou Nike v nabídce nejčastěji používá, je i praktická, protože maskuje pot a skvrny.</p>'
          '<h2>Pro ženy, muže i děti</h2>'
          '<p>Nabídka značky obsahuje legíny pro ženy, pánské elasťáky a termolegíny a také dívčí a dětské varianty. Dámské střihy mají tvarovaný pas a boky a často jsou v nabídce označené jako 7/8 s kapsou. Pánské modely se nosí jako spodní vrstva pod kraťasy, na běh v chladu a při tréninku. Pánské varianty najdete i v samostatném výběru <a href="/panske-leginy/">pánských legín</a>. Dětské a dívčí legíny, často z řady Sportswear nebo ve variantě Pro Dri-FIT, vydrží školní tělocvik i hraní venku. U dětí volte velikost spíš větší, protože legíny vydrží déle, když sedí volněji v délce.</p>'
          '<h3>Termolegíny a podvlékání</h3>'
          '<p>Pánské termolegíny se nosí jako základní vrstva pod kalhoty při běhu v zimě, na kole nebo při lyžování. Mají hladký vnitřek nebo jemné počesání. Pro zimní trénink je dobré vrstvit: termo vrstvu pod vlastní běžecké kalhoty nebo kraťasy a při větru navíc vrchní vrstvu. Podobné termoprádlo najdete u dalších značek v kategorii <a href="/leginy/">legíny</a>.</p>'
          '<h2>Nike v porovnání s ostatními značkami</h2>'
          '<p>Nike patří mezi největší sportovní značky a legíny staví na jasně rozlišených řadách a rozpoznatelném logu. Výhodou je široký výběr velikostí a barev a jednoduchá orientace v názvech. Konkurence nabízí podobné výrobky s jiným důrazem. <a href="/under-armour-leginy/">Under Armour</a> je tradičně spojený s přiléhavým střihem a kompresním pocitem, <a href="/gymbeam-leginy/">GymBeam</a> cílí na fitness komunitu a levnější ucelené kolekce. Z menších značek najdete u Nike jen o něco užší výběr spodních vrstev, protože se soustředí na tréninkové a běžecké kusy. Pokud chcete vyzkoušet jinou barvu, podívejte se na <a href="/hnede-leginy/">hnědé legíny</a> jako módnější alternativu k černé.</p>'
          '<h2>Jak velikost sedí</h2>'
          '<p>Při výběru velikosti sledujte tabulku výrobce a změřte obvod pasu a boků. Legíny mají být těsné, ale ne škrtící. Při zdvihu nohy nesmí žádná část sjíždět dolů a v kolenou se látka nesmí nadměrně nafukovat. Pokud se pohybujete mezi dvěma velikostmi, vezměte menší u běžeckých a tréninkových kusů a větší u volnočasových. Velikosti se mohou lišit podle řady a podle toho, zda jde o dámský nebo pánský střih, proto vždy čtěte údaje u konkrétního modelu.</p>'
          '<h2>Péče o legíny</h2>'
          '<ul><li>Perte na 30 °C s jemnými prostředky bez aviváže. Avivážní zbytky ucpávají vlákna a zhoršují odvod potu.</li>'
          '<li>Obracejte je naruby, aby se potisk a povrch neotíraly o buben.</li>'
          '<li>Nesušte na topení ani v sušičce, vysoké teploty ničí elastan.</li>'
          '<li>Perte odděleně od suchých zipů a bund s přezkami, které látku nabírají.</li>'
          '<li>Po tréninku je nenechávejte ve vlhké tašce, zápach vzniká už po pár hodinách.</li></ul>'
          '<p>K legínám se hodí <a href="/sportovni-podprsenky/">sportovní podprsenka</a> a <a href="/sportovni-tricka/">funkční tričko</a>. Pokud hledáte alternativu pro horko, vyberte <a href="/sportovni-kratasy/">kraťasy</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi legínami Nike One a Nike Pro?',
         'One je univerzální řada pro cvičení, fitness i každodenní nošení. Pro je přiléhavější tréninkový střih s pevnějším úpletem, který drží svaly při intenzivním pohybu. Pokud chcete jedny legíny na všechno, volte One, pokud trénujete tvrdě, zkuste Pro.'),
        ('Co znamená Dri-FIT u legín Nike?',
         'Je to značka funkčního úpletu, který odvádí pot od kůže a rychle schne. Vyrábí se hlavně z polyesteru s elastanem. Hodí se na běh a posilovnu, u volnočasových legín pro každodenní nošení není nutný.'),
        ('Které legíny Nike jsou nejlepší na běh?',
         'Na běh se hodí řady Swift, Fast, Tempo a podobné modely s délkou 7/8 a kapsou na telefon. Mají lehký úplet a vyšší pas, který při běhu nesjíždí. Pro chladnější dny zvolte plnou délku nebo termolegíny.'),
        ('Jak poznám, že legíny jsou neprůhledné?',
         'Natáhněte látku přes dlaň a podívejte se na světlo. Pokud skrz prosvítá kůže, při hlubokém dřepu bude prosvítat ještě víc. Tmavé odstíny jsou bezpečnější než světlé, ale ověřit se dá i recenzemi.'),
        ('Jakou výšku pasu zvolit?',
         'Pro sport je nejlepší vysoký pas, který drží břicho a nesjíždí při pohybu. Střední pas stačí pro volný čas a jógu. Nízký pas se u sportovních legín nehodí, protože se při předklonu otevírá.'),
        ('Mám volit 7/8, nebo plnou délku?',
         '7/8 končí těsně nad kotníkem a je ideální na běh, fitness a letní nošení. Plná délka hřeje víc a hodí se do chladna, na jógu a do posilovny, kde chcete krýt celou nohu. Pokud máte kratší nohy, plná délka bývá vhodnější než 7/8.'),
        ('Jsou legíny Nike i pro muže a děti?',
         'Ano, nabídka obsahuje pánské elasťáky a termolegíny, dívčí varianty i dětské modely. Pánské kusy se nosí hlavně pod kraťasy, při běhu v chladu a při tréninku. Dětské legíny z řady Sportswear zvládnou školu i hřiště.'),
        ('Jak legíny prát, aby vydržely?',
         'Perte je naruby na 30 °C s jemným prostředkem bez aviváže. Nesušte na topení ani v sušičce, protože vysoké teploty ničí elastan. Při správné péči si zachovají tvar a odvod potu po mnoho sezon.'),
        ('Dá se legíny Nike nosit i mimo sport?',
         'Určitě, hlavně řady Sportswear a One. Kombinují se s mikinou, dlouhým svetrem nebo tunikou. Na sport se doporučují legíny z funkčního úpletu, na běžné nošení pohodlnější směs s bavlnou.'),
        ('Čím se Nike liší od Under Armour nebo GymBeam?',
         'Nike nabízí přehledné řady podle činnosti a velký výběr velikostí a barev. Under Armour bývá spojený s přiléhavým kompresním pocitem, GymBeam s fitness komunitou a širokou kolekcí. Rozdíl je především v střihu, takže vyzkoušejte, který z nich vám sedí.')
    ],
)

# ------------------------------------------------------------------ detska-kolobezka
NEW['detska-kolobezka'] = dict(
    title='Dětská koloběžka: jak vybrat podle věku a výšky dítěte',
    desc='Dětská koloběžka pro 2 až 12 let. Jak vybrat tříkolku, dvoukolku nebo skládací model podle věku a výšky dítěte, bezpečnost a porovnání obchodů.',
    intro='<p>Dětská koloběžka není jen zmenšená dospělá. U dětí rozhoduje výška řídítek, šířka stání, brzda a stabilita, protože malé tělo má jiné těžiště a jiné reakce. Dvouleté dítě potřebuje tříkolku s naklápěním, čtyřleté už stabilní dvoukolku a školák model, který vydrží přenášení v MHD. '
          'Na této stránce jsou koloběžky pro děti z kategorie <a href="/kolobezky/">koloběžky</a>, od prvních modelů po větší městské a freestyle kousky. Průvodce vysvětluje, jak vybrat podle věku i výšky, jak poznat dobře nastavená řídítka, co kontrolovat na brzdě a kolečkách a kdy dává smysl <a href="/elektrokolobezky/">elektrokoloběžka</a> nebo <a href="/freestyle-kolobezky/">freestyle model</a>. Pro nejmenší se hodí <a href="/odrazedla/">odrážedla</a> a každou jízdu doplňují <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>',
    guide='<h2>Podle věku: co dítě zvládne</h2>'
          '<p>Věk je jen orientační údaj, protože děti se vyvíjejí různě rychle. Přesto platí několik společných pravidel, kterými se vyplatí řídit. Čím mladší dítě, tím víc stability a tím níž nad zemí stojí. Starší děti ocení lehkost a rychlé brzdění.</p>'
          + T(['Věk', 'Vhodný typ', 'Na co dbát'], [
              ['2–3 roky', 'tříkolka s naklápěním, odrážedlo', 'široký rozvor, nízká plošina, měkká kolečka'],
              ['3–5 let', 'dvoukolka s širokou stojnou plochou', 'nastavitelná řídítka, pevná brzda, snadné ovládání'],
              ['5–8 let', 'klasická dětská koloběžka', 'lehký rám, větší kolečka, držadla pro dětskou ruku'],
              ['8–12 let', 'větší městská nebo skládací', 'pevné skládání, výška řídítek až do hrudníku'],
              ['starší děti', 'freestyle, případně elektrická', 'odolná konstrukce, ověřit omezení věku u výrobce']]) +
          '<p>Při pochybnostech vyberte spíš stabilnější model. Dítě se na něm rychleji naučí a získá jistotu, což u koloběžky vede k bezpečnější jízdě než u rychlého modelu, na kterém se bojí. Pro mladší děti platí, že dospělý by měl být nablízku a hlídat okolí.</p>'
          '<h2>Výška řídítek a velikost plošiny</h2>'
          '<p>Řídítka by měla sahat zhruba do poloviny těla dítěte, mezi pas a hrudník. Příliš nízká nutí dítě předklánět se a ztěžují zatáčení, příliš vysoká zvedá ramena a unavuje ruce. Dobrá koloběžka má řídítka nastavitelná po několika centimetrech, aby vydržela růst. Plošina má být dost široká, aby se na ni vešly obě nohy vedle sebe při klouzání, a dost nízká, aby se dítě bez problému odráželo. Nízká plošina nabízí větší stabilitu a méně nebezpečný pád.</p>'
          '<h3>Jak nastavit koloběžku doma</h3>'
          '<ul><li>Postavte dítě vedle koloběžky a nastavte řídítka přibližně do výše pasu až hrudníku.</li>'
          '<li>Zkontrolujte, zda má dítě volně narovnaná záda a zápěstí.</li>'
          '<li>Zatáhněte za brzdu a ověřte, že se pohybuje hladce a dítě na ni dosáhne celou dlaní.</li>'
          '<li>Utáhněte všechny šrouby a pojistky skládacího mechanismu.</li>'
          '<li>Při růstu dítěte nastavení každé tři až čtyři měsíce znovu zkontrolujte.</li></ul>'
          '<h2>Tříkolka, dvoukolka, skládací model</h2>'
          '<p>Tříkolka s naklápěním má dvě kolečka vpředu nebo vzadu a zatáčí se pohybem těla, ne otáčením řídítek. Drží ji jistě i batole a učí dítě základy rovnováhy. Dvoukolka s širokou plošinou je logický další krok, protože dítě už rovnováhu zná. Po ní přichází klasický model s řídítky a dvěma většími koly. Skládací modely s jedním kloubem na hlavní trubce se vyplatí tam, kde se koloběžka často vozí v autě nebo MHD. Důležité je ověřit, že se skládací mechanismus nemůže při jízdě sám uvolnit.</p>'
          '<h2>Brzda, kolečka a rám</h2>'
          '<p>Zadní šlapací brzda funguje tak, že dítě zašlápne na blatník nad zadním kolečkem. Je jednoduchá, ale dětem mladším než pět let často nejde, protože musí stát na jedné noze. Ruční brzda na řídítkách je pro malé děti pohodlnější, pokud mají dost síly pro stisk páčky. U větších modelů se objevují obě. Při výběru se nejvíc vyplatí vyzkoušet, jak dítě brzdí v klidném prostředí.</p>'
          '<p>Kolečka z polyuretanu jedou tišeji a jemněji než tvrdá plastová. U větších koleček je jízda plynulejší a překážky se přejíždějí snáz, ale koloběžka je těžší. Rám z hliníku je lehký a nerezne, ocel je pevnější a těžší. Dětská koloběžka musí mít jednoduchou konstrukci bez ostrých hran a bez drobných dílů, které se dají uvolnit.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete známé výrobce dětských koloběžek, mezi nimi ' + B(('micro', 'Micro'), ('kostka', 'Kostka'), ('yedoo', 'Yedoo')) + '. Podrobnější přehled nabídky najdete na stránkách <a href="/kolobezka-micro/">koloběžek Micro</a>, <a href="/kolobezka-kostka/">koloběžek Kostka</a> a <a href="/kolobezka-yedoo/">koloběžek Yedoo</a>. Každá značka klade důraz na něco jiného. Micro je spojená se skládacími modely a tříkolkami pro nejmenší, Kostka a Yedoo patří k tradičním evropským výrobcům s širokou nabídkou pro různé věkové kategorie. Přesný rozdíl u konkrétního kusu vždy ověřte v popisu.</p>'
          '<h2>Bezpečnost a výbava</h2>'
          '<p>Přilba by měla být samozřejmostí od první jízdy. Správně nasazená sedí rovně na čele, nad obočím, a popruhy tvoří trojúhelník pod ušima. K přilbě patří <a href="/chranice-a-helmy/">chrániče kolen a loktů</a> pro děti, které rychle jezdí nebo zkoušejí triky. Oblečení by mělo být světlé nebo s reflexními prvky, hlavně v podzimních měsících. Boty musí mít pevnou podrážku, dětské sandály a pantofle nejsou pro koloběžku vhodné.</p>'
          '<h3>Kam s dítětem jezdit</h3>'
          '<p>Nejlepší jsou rovné a hladké povrchy bez provozu, třeba parky, cyklostezky a dětská hřiště. Hrubý štěrk a prasklý beton zpomalují a destabilizují malá kolečka. Mladší děti by měly mít dospělého v dosahu, u větších se vyplatí domluvit pravidla pro jízdu mezi chodci. Na silnici s provozem koloběžka pro dítě nepatří.</p>'
          '<h2>Starší děti: freestyle a elektrokoloběžky</h2>'
          '<p>Pro starší děti a teenagery nabízí obchody <a href="/freestyle-kolobezky/">freestyle koloběžky</a> určené do skateparku. Mají pevný rám, malá kolečka a jednoduchou konstrukci pro skoky a triky. Hodí se pro zkušenější jezdce, na každodenní dojíždění nejsou ideální. Elektrokoloběžky jsou jiný typ vozidla s vlastními pravidly a omezením věku, proto si před koupí ověřte, kde a od kolika let je smí dítě používat. Najdete je v sekci <a href="/elektrokolobezky/">elektrokoloběžky</a>.</p>'
          '<h2>Jak číst nabídku</h2>'
          '<p>Při porovnávání obchodů sledujte nosnost, rozsah nastavení řídítek, váhu koloběžky a typ brzdy. Hmotnost je u dětských modelů zásadní, protože rodič ji nosí v ruce, když dítě unaví. Zkontrolujte také, zda jsou k dispozici náhradní díly, hlavně kolečka a brzda. Nejlevnější modely často nemají žádné, a po prvním opotřebení tak končí v koši. Pokud hledáte první koloběžku, podívejte se i na <a href="/odrazedla/">odrážedla</a>, která jsou pro nejmenší jednodušší než jakákoli koloběžka.</p>',
    faq=[
        ('Od kolika let může dítě jezdit na koloběžce?',
         'Zhruba od dvou let na tříkolce s naklápěním, od tří až čtyř let na dvoukolce s širokou plošinou. Věk je orientační, důležitější je, zda dítě udrží rovnováhu a zvládne brzdit. Mladší dítě potřebuje dospělého poblíž.'),
        ('Jak poznám správnou výšku řídítek?',
         'Řídítka by měla sahat zhruba mezi pas a hrudník dítěte. Dítě má stát vzpřímeně, s mírně pokrčenými lokty. Příliš nízká nutí dítě předklánět se, příliš vysoká zvedá ramena.'),
        ('Je lepší tříkolka, nebo dvoukolka?',
         'Pro nejmenší děti okolo dvou až tří let je lepší tříkolka s naklápěním, protože je stabilnější. Jakmile dítě drží rovnováhu, přechází se na dvoukolku. U většiny dětí je přechod plynulý mezi třetím a pátým rokem.'),
        ('Jaká brzda je pro dítě nejlepší?',
         'Pro malé děti je dobrá zadní šlapací brzda, pokud zvládnou stát na jedné noze. Ruční brzda je pro některé pohodlnější, ale vyžaduje dostatek síly v ruce. U větších modelů bývají obě a dítě si vybere, co mu vyhovuje.'),
        ('Má cenu kupovat větší koloběžku „do růstu“?',
         'U koloběžky je to riskantní, protože příliš vysoká řídítka a velká plošina dítě rozhazují. Vybírejte model s nastavitelnými řídítky, který dítěti sedí teď a vydrží další dvě až tři sezony. Naopak příliš malá koloběžka dítě brzy omrzí.'),
        ('Jaká kolečka jsou nejlepší?',
         'Polyuretanová kolečka jedou hladce a tiše a snášejí hrubší povrch lépe než plastová. Větší průměr zlepšuje plynulost, ale zvyšuje hmotnost. Pro školáka je dobrý kompromis středně velké kolečko s kvalitními ložisky.'),
        ('Potřebuje dítě na koloběžce helmu?',
         'Ano, helma by měla být samozřejmostí od první jízdy. Má sedět rovně na čele a popruhy se zapínají pod bradou tak, aby se pod ně vešel jen prst. Chrániče kolen a loktů se hodí zvláště u rychlejších dětí a při zkoušení triků.'),
        ('Jak se starat o dětskou koloběžku?',
         'Po mokré jízdě otřete koloběžku do sucha a čas od času zkontrolujte šrouby a brzdu. Ložiska občas očistěte a namažte, kolečka měňte, když jsou nerovnoměrně opotřebovaná. Skládací mechanismus udržujte čistý a bez písku.'),
        ('Hodí se pro dítě freestyle nebo elektrická koloběžka?',
         'Freestyle koloběžky jsou určené pro starší děti a skatepark, na běžné dojíždění se hodí méně. Elektrokoloběžky mají vlastní pravidla a omezení věku. Před koupí si ověřte, kde a od kolika let je dítě smí používat.'),
        ('Čím se liší značky Micro, Kostka a Yedoo?',
         'Micro je silná v segmentu dětských skládacích modelů a tříkolek, Kostka a Yedoo patří k evropským výrobcům s širokou nabídkou pro různé věky. Konkrétní rozdíly určuje model, proto porovnejte váhu, rozsah nastavení a typ brzdy.')
    ],
)

# ------------------------------------------------------------------ damske-kratasy
NEW['damske-kratasy'] = dict(
    title='Dámské kraťasy: střih, délka a materiál podle sportu',
    desc='Dámské kraťasy na běh, fitness, turistiku i kolo. Jak se liší střih, délka a vnitřní kalhotky, jak vybrat velikost a porovnat obchody na jednom místě.',
    intro='<p>Dámské kraťasy se od pánských neliší jen barvou. Mají jiný střih pasu a boků, kratší nohavice, často vnitřní kalhotky a jiné místo pro kapsu. Rozhodne, zda budete běhat, cvičit nebo vyrazíte na turistiku, a podle toho zvolíte délku, materiál a vedení švů. '
          'Na této stránce jsou kraťasy a šortky pro ženy z kategorie <a href="/sportovni-kratasy/">kraťasy</a>, od lehkých běžeckých po cyklistické a volnočasové. Průvodce ukazuje, jak se liší dámský střih, co znamenají délky, kdy se hodí vnitřní kalhotky a jak pohodlně sedí velikosti. Zároveň porovnává nabídku značek, třeba <a href="/nike-kratasy/">Nike</a>, <a href="/gymbeam-kratasy/">GymBeam</a> a <a href="/jordan-kratasy/">Jordan</a>. Na horké dny se hodí kombinace s <a href="/sportovni-tricka/">funkčním tričkem</a> a <a href="/sportovni-podprsenky/">sportovní podprsenkou</a>.</p>',
    guide='<h2>V čem se dámský střih liší</h2>'
          '<p>Dámské modely mají obvykle užší pas, širší boky a kratší rozkrok než pánské. Nohavice jsou vyšší na stehně, aby se při pohybu neotíraly, a pas bývá tvarovaný nebo vyšší. Pánské kraťasy ženám často dobře nesedí, protože pas sjíždí z boků nebo naopak tlačí. Opačně to ale platí také: muži si mohou vybrat dámský střih, pokud chtějí kratší délku, a děti mají samostatné velikosti.</p>'
          + T(['Část', 'Dámská úprava', 'Co přináší'], [
              ['Pas', 'užší, vyšší nebo tvarovaný, často široká guma', 'drží na místě a netlačí na břicho'],
              ['Boky a stehna', 'více prostoru v bocích, delší vnitřní délka nohavice', 'pohyb bez ztuhlosti a odírání'],
              ['Délka', 'kratší, často krátká nad kolenem', 'volný pohyb nohou při běhu'],
              ['Kapsy', 'menší, často na boku nebo na zadní straně', 'telefon, klíče, gely'],
              ['Vnitřní slipy', 'běžně integrované u běžeckých modelů', 'není potřeba spodní prádlo']]) +
          '<h2>Délka podle činnosti</h2>'
          '<p>Nejdůležitější volbou je délka. Krátké kraťasy s vnitřními kalhotkami mají nohavici sotva pod rozkrokem a dávají nohám maximální volnost při běhu a rychlých tréninzích. Střední délka sahá do poloviny stehna a funguje na fitness, jógu i každodenní nošení. Delší šortky nad kolena chrání stehna před otěrem o kamení nebo větve na stezce. Cyklistické kraťasy jsou přiléhavé a obvykle mají vycpávku v rozkroku. Turistické šortky bývají volnější a se zipovými kapsami.</p>'
          + T(['Sport', 'Střih a délka', 'Na co dát pozor'], [
              ['Běh', 'krátké nebo střední, vnitřní slipy, lehká látka', 'bez tlustých švů, kapsa na telefon'],
              ['Fitness a posilovna', 'střední délka, pružný a neprůhledný materiál', 'dřep bez prosvítání'],
              ['Jóga a pilates', 'přiléhavé, elastické, vyšší pas', 'pas, který nesjíždí při předklonu'],
              ['Turistika', 'volnější, odolná látka, zipové kapsy', 'rychleschnoucí materiál'],
              ['Cyklistika', 'přiléhavé, s vycpávkou v rozkroku', 'kvalitní vložka, bez švů v místě sedla'],
              ['Tenis a týmové sporty', 'lehčí, volnější, často s kapsami na míčky', 'volný pohyb při výpadech']]) +
          '<p>Výše zmíněné rozdělení se hodí jako výchozí bod. Najdete ale i univerzální modely, které se dají nosit na více činností. Čím víc se kus snaží dělat vše, tím menší bývá jeho výkon v konkrétním sportu.</p>'
          '<h2>Vnitřní kalhotky a ochrana před otěrem</h2>'
          '<p>Integrované vnitřní kalhotky jsou u běžeckých kraťasů běžné a ušetří vás nošení dalšího prádla. Zabraňují odírání a drží přirozeně tvar, jenže se hodí jen tehdy, pokud vám je střih příjemný. Pokud je nechcete, hledejte kraťasy bez vnitřní vrstvy a nosit je můžete se sportovním prádlem nebo pod nimi legíny. Při dlouhém běhu na horké dny se vyplatí sáhnout po kusu, který je kratší a měkčí v oblasti stehen, kde nejčastěji vzniká otěr.</p>'
          '<h3>Kombinace s legínami</h3>'
          '<p>Krátké sportovní kraťasy se v zimě nosí přes <a href="/leginy/">legíny</a>. Tato kombinace chrání teplo a zároveň poskytuje volnost. Přes těsné legíny má smysl zvolit kraťasy s jemnějším střihem, které se nesvírají. Pro letní trénink naopak zvolte jen kraťasy bez další vrstvy.</p>'
          '<h2>Materiály a péče</h2>'
          '<p>Běžecké a tréninkové kraťasy bývají z polyesteru, který odvádí pot a rychle schne. Elastan zajišťuje pružnost a po praní se vrací do tvaru. Bavlněné modely jsou měkké a příjemné na procházky, ale po propocení těžknou. Turistické šortky využívají hustě tkané syntetické materiály, které odolávají odření. Nevhodné jsou příliš hrubé úplety, které se na zadní straně stehen třou o sedačku nebo o kůži.</p>'
          '<ul><li>Perte na 30 až 40 °C a bez aviváže, aby se nezanesly vlákna.</li>'
          '<li>Zip a suchý zip před praním zapněte, aby nepoškodily látku.</li>'
          '<li>Nesušte v horké sušičce, mohou se srazit a ztratit pružnost.</li>'
          '<li>Reflexní a potištěné části nežehlete.</li>'
          '<li>Po tréninku je nenechávejte zabalené ve vlhké tašce.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Měřte obvod pasu na nejužším místě a boků v nejširším místě a porovnejte s tabulkou výrobce. Kraťasy mají sedět na pasu, aniž by se zařezávaly, a nohavice nesmějí vyjíždět při chůzi po schodech. Pokud jste mezi velikostmi, u běžeckých a fitness modelů zvolte menší, u volnočasových a turistických větší. Vyzkoušejte dřep a zvedání nohy, pokud je to možné. U nákupu přes internet vybírejte obchody, které přijímají vrácení, protože střih se různí podle výrobce.</p>'
          '<h2>Značky a výběr</h2>'
          '<p>V nabídce najdete velké sportovní značky jako ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('under-armour', 'Under Armour')) + ', tréninkovou značku ' + B(('gymbeam', 'GymBeam')) + ' i řadu outdoorových výrobců. Podrobnější přehled nabídek najdete na stránkách <a href="/nike-kratasy/">kraťasů Nike</a>, <a href="/gymbeam-kratasy/">kraťasů GymBeam</a> a <a href="/jordan-kratasy/">kraťasů Jordan</a>. Značky se liší střihem a délkou, a proto je rozumné vyzkoušet jednu konkrétní řadu a pak ji znovu kupovat, pokud vám sedí.</p>'
          '<h2>Jak číst nabídku</h2>'
          '<p>Stránka sdružuje modely označené pro ženy a dívky. Kategorie obsahuje také pánské a dětské kusy, a proto se u některých modelů vyplatí zkontrolovat popis. Sledujte materiál, délku, přítomnost vnitřních kalhotek a velikostní tabulku. Některé obchody uvádějí velikosti v evropském značení, jiné v americkém nebo britském. Pro každodenní nošení stačí obyčejné šortky, pro sport hledejte funkční materiál s pružností.</p>'
          '<p>Pro další oblečení si prohlédněte <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-obuv/">sportovní obuv</a>. Při plavání či u vody se hodí <a href="/plavky/">plavky</a>.</p>',
    faq=[
        ('Čím se dámské kraťasy liší od pánských?',
         'Mají užší pas, více místa v bocích a kratší nohavice. Často obsahují integrované kalhotky a menší kapsy na boku nebo vzadu. Pánský střih ženám často nesedí, protože pas sjíždí nebo tlačí.'),
        ('Jaká délka kraťasů se hodí na běh?',
         'Na běh se hodí krátká až střední délka, aby se nohavice netřela o stehna. Vnitřní kalhotky chrání před otěrem. Na delší trasy v horku volte lehký a prodyšný materiál.'),
        ('Mám volit kraťasy s vnitřními kalhotkami?',
         'Pokud běháte nebo trénujete a nechcete další prádlo, jsou praktické. Pokud nosíte vlastní sportovní spodní prádlo nebo legíny, vezměte model bez vnitřní vrstvy. Rozhodují osobní pocity, nejlepší je vyzkoušet oba typy.'),
        ('Jaké kraťasy jsou nejlepší do posilovny?',
         'Střední délka z pružného a neprůhledného materiálu, který se při dřepu neprohýbá. Vyšší pas drží na místě a netlačí. Vyhněte se kusům z tenké látky, které prosvítají.'),
        ('Jak poznám správnou velikost?',
         'Změřte pas a boky a porovnejte s tabulkou výrobce. Kraťasy mají sedět bez zařezávání a při chůzi po schodech nevyjíždět. U sportovních modelů zvolte při pochybnosti menší, u volnočasových větší.'),
        ('Vydrží kraťasy z polyesteru v pračce?',
         'Ano, funkční polyesterové kraťasy vydrží mnoho cyklů při 30 až 40 °C bez aviváže. Nesušte je v horké sušičce. Při správné péči zachovají pružnost i odvod potu.'),
        ('Jak se liší cyklistické kraťasy od běžných?',
         'Cyklistické kraťasy jsou přiléhavé a mají v rozkroku vycpávku. Běžné sportovní šortky mají vnitřní kalhotky nebo žádnou vložku a jsou volnější. Vložka pro kolo se do běhu ani do posilovny nehodí.'),
        ('Mohu kraťasy nosit přes legíny?',
         'Ano, v chladnějším počasí je to oblíbená kombinace. Krátké kraťasy přes legíny hřejí, ale nesvírají. Zvolte kraťasy s lehčím střihem, aby se nepřiléhaly k legínám a nekroutily.'),
        ('Co dělat, když se kraťasy odírají o stehna?',
         'Zvolte delší nohavice nebo model s vnitřními kalhotkami. Pomáhá měkčí materiál a bezešvé zpracování. Můžete také nosit tenké přiléhavé šortky pod volnějšími kraťasy.'),
        ('Dají se v kategorii najít i dětské a pánské kraťasy?',
         'Stránka je zaměřená na ženy a dívky, ale u některých kusů se popis liší. Zkontrolujte vždy pohlaví a velikost v detailu. Pánské, dětské a sportovní kraťasy najdete v hlavní kategorii.')
    ],
)

# ------------------------------------------------------------------ doplňky (rozšíření průvodců)
NEW['nike-leginy']['guide'] += (
    '<h2>Jak sestavit outfit z legín Nike</h2>'
    '<p>K černým legínám se hodí téměř každý svršek, proto jsou nejprodávanější. Barevné modely, třeba fialové, zelené nebo oranžové, dobře fungují s neutrálním černým nebo bílým topem, aby se barvy nehádaly. K běžeckým legínám 7/8 patří nízké ponožky nebo kotníkové, k plným délkám delší ponožka do běžecké obuvi. Na chladné ráno přidejte větrovku nebo tenkou vrstvu, protože legíny samy kryjí jen nohy.</p>'
    '<p>Kdo kombinuje legíny s volným oblečením, může sáhnout po dlouhé mikině nebo košili a nechat legíny jako hlavní tvarující prvek. U sportovního outfitu naopak volte přiléhavý top, který doplní střih legín a neplete se při pohybu. Pro jógu a pilates se hodí kratší top a vysoký pas, aby se při pohybu nic neposouvalo.</p>'
    '<h2>Kdy legíny vyměnit</h2>'
    '<p>Legíny se vyměňují, když ztratí pružnost a začnou ztenčovat látku v oblasti stehen a kolen. Nejdřív to poznáte tak, že přestanou být neprůhledné při dřepu, nebo že se pas sám sroluje dolů. Další signál je zápach, který nezmizí ani po praní. Pokud trénujete často, mít v rotaci dva až tři páry se vyplatí, protože každý vydrží déle a můžete vždy vzít čistý kus. Starší legíny se dají využít na domácí cvičení nebo do postele, i když na běh už nejsou ideální.</p>'
    '<h2>Co sledovat u pásku a švů</h2>'
    '<p>Pas je nejdůležitější konstrukční prvek. Široká guma rozkládá tlak a nesvírá, úzká se zařezává. Plochý šev v rozkroku a po stranách zabraňuje otěru. Kapsa na telefon je užitečná u běžeckých modelů, zvláště pokud je vedená po boku nebo vzadu v pase a nemá drnčet. Pokud chcete mít v kapse i klíče, ověřte, že je dost hluboká a zajištěná, aby se věci při běhu nepohybovaly.</p>')

NEW['detska-kolobezka']['guide'] += (
    '<h2>Jak se dítě učí jezdit</h2>'
    '<p>Nejsnazší je začít na rovné ploše bez provozu, kde dítě nemusí řešit okolí. Naučte ho stát obouma nohama na plošině, jednou nohou se odrážet a druhou brzdit nebo odpočívat. Pak postupně přidejte zatáčení do velkých oblouků a zastavení na dané místo. Většina dětí zvládne základ za jedno až dvě odpoledne. Netlačte na rychlost, důležitější je jistota a opakování. Dítě, které se cítí bezpečně, se učí rychleji, než kdyby se muselo držet řídítek ve strachu.</p>'
    '<p>Při učení se vyplatí chodit vedle dítěte, ale nedržet je za řídítka. Drží-li dospělý koloběžku, dítě nezíská cit pro rovnováhu a bude spoléhat na cizí ruku. Pomoc stačí nabízet jen před překážkou nebo při zastavení.</p>'
    '<h2>Údržba a skladování</h2>'
    '<p>Dětské koloběžky se kvůli nárazům a pádům povolují častěji než dospělé. Jednou za měsíc zkontrolujte šrouby řídítek, osy koleček a pojistku skládacího mechanismu. Kolečka měňte, když se jejich hrany opotřebují nerovnoměrně, protože ovlivňují zatáčení. Koloběžku skladujte v suchu, venku jí vadí déšť i mráz, který poškozuje plasty a ložiska. Po dešti ji otřete a nechte oschnout, ložiska pak zůstanou v lepším stavu.</p>'
    '<h2>Kdy koloběžku vyměnit za větší</h2>'
    '<p>Když dítě stojí na plošině s pokrčenými koleny a řídítka už nesahají nad pas, je čas na větší model. Dalším znakem je, že se dítě odráží s nepřirozeně vytočenou nohou nebo že mu nestačí plošina pro obě nohy. Starší koloběžka často přejde na mladšího sourozence, takže pořízení kvalitního kusu se vyplatí. Při výměně vybírejte model, který má stejnou nebo lepší brzdu než předchozí, aby dítě nemuselo přeučovat základní návyky.</p>')

NEW['damske-kratasy']['guide'] += (
    '<h2>Délka a velikost při různé postavě</h2>'
    '<p>Stejné kraťasy sedí jinak na vysoké a nižší postavě. Vyšší ženy často ocení delší vnitřní délku nohavice, aby se nohavice nestahovaly nahoru. Nižší postavy naopak využijí kratší nohavici, která neviditelně prodlouží nohu. Při širších bocích hledejte model s tvarovaným pasem a pružnou gumou, která nesvírá, ale zároveň nesjíždí. U štíhlejší postavy je dobré zvolit model se stahovací šňůrkou, kterou se pas dotáhne přesně.</p>'
    '<h2>Kapsy a praktické detaily</h2>'
    '<p>Kapsa na telefon je dnes standard, ale rozhodují detaily. Boční kapsa s přesahem nebo zipem drží telefon při běhu bez houpání. Zadní kapsa u pasu je lepší na klíče nebo gely. Šňůrka v pase umožňuje doladit velikost, pokud se kraťasy při běhu pohybují. Reflexní prvky se hodí na večerní běh. Pokud kraťasy používáte na turistiku, zkontrolujte také zip na kapse, aby věci při chůzi nevypadly.</p>'
    '<h2>Letní nošení mimo sport</h2>'
    '<p>Sportovní kraťasy se v létě nosí i na výlety, k vodě a na pohodlné procházky. Nejlépe se kombinují s jednoduchým tričkem nebo tílkem a pohodlnou obuví. Pro volný čas stačí střední délka a měkký materiál. Pokud chcete kraťasy nosit celodenně, vyberte model s trochu volnějším střihem a bez vnitřní vrstvy, ten větrá lépe a není tak pevný na pasu. Barvy, které nepůsobí sportovně, jako béžová, olivová nebo tmavě modrá, se snáz zapojí do městského outfitu.</p>'
    '<h2>Jak porovnat obchody</h2>'
    '<p>Jednu a tutéž řadu značka prodává u více obchodů, často s rozdílnou dostupností velikostí. Proto je dobré sledovat nabídky souběžně a vybrat obchod, který má vaši velikost skladem a vrací zboží bez potíží. Při koupi si ověřte popis materiálu, délku nohavice a údaj o vnitřních kalhotkách. Zkontrolujte také, zda obchod uvádí evropské velikosti. Pokud nákup plánujete na sezonu, začněte v předstihu, protože oblíbené barvy a střihy bývají na jaře první vyprodané.</p>')
