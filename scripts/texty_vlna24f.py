"""sporteka.cz — wave 24f (5. 11. 2026): long texts for cyklo-chranice, gravel-kola, rybarske-spacaky, snowboardove-chranice.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklo-chranice
NEW['cyklo-chranice'] = dict(long=True,
    title='Chrániče pro cyklisty: kolena, lokty, záda, zápěstí',
    desc='Cyklistické chrániče kolen, loktů, zad a zápěstí pro MTB, enduro i děti. Jak vybrat typ, velikost a materiál a porovnat nabídky českých obchodů.',
    intro='<p>Pád z kola je otázka času, ať jezdíte po cyklostezce, v bikeparku nebo na technických singletrecích. Chrániče nezabrání pádu, ale změní jeho následky: chrániče pomáhají zmírnit následky a snížit riziko sedřené kůže a naražených kloubů. Sporteka porovnává nabídky českých obchodů u chráničů kolen a loktů, zad, zápěstí, stehen a boků, dětských sad i drobností, jako je chránič přehazovačky.</p>'
          '<p>V kategorii najdete značky ' + B(('tsg', 'TSG'), ('alpinestars', 'Alpinestars'), ('leatt', 'Leatt'), ('o-neal', "O'neal"), ('fox-racing', 'FOX Racing'), ('seven', 'Seven'), ('rockrider', 'Rockrider'), ('k2', 'K2'), ('cariboo', 'Cariboo')) +
          '. K chráničům se hodí <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/mtb-a-integralni-helmy/">integrální helmy</a> a rukavice, které najdete v rozcestníku <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>',
    guide='<h2>Jaké druhy cyklistických chráničů existují</h2>'
          '<p>Chrániče se dělí podle části těla a podle míry ochrany. Na silnici a v běžném provozu bývá nejužitečnější helma a rukavice, v terénu přibývají kolena, lokty a záda. V bikeparku a při enduru se nosí skoro všechno najednou, protože rychlost a skoky zvyšují sílu nárazu.</p>'
          + T(['Typ', 'Co chrání', 'Hodí se pro'], [
              ['Chrániče kolen', 'čéšku a holeň, často s bočními křidélky', 'MTB, enduro, downhill, děti na kole a koloběžce'],
              ['Chrániče loktů', 'loket a předloktí', 'technické sjezdy, bikepark, pumptrack'],
              ['Chránič páteře', 'záda od krční po bederní část', 'enduro, downhill, rychlé sjezdy, freeride'],
              ['Chrániče zápěstí', 'zápěstí při pádu na dlaně', 'začátečníci, děti, kolečkové sporty'],
              ['Chránič stehen a hýždí', 'boky, kostrč a stehna', 'downhill, dirt, ostré sjezdy'],
              ['Sady pro děti', 'kolena, lokty a zápěstí v jednom balení', 'první kola, odrážedla, koloběžky'],
              ['Chránič přehazovačky', 'zadní měnič při převrácení kola', 'cestování, gravel a horská kola s drahým pohonem']]) +
          '<p>Kategorie nese jméno cyklo-chrániče, ale najdete v ní i univerzální dětské sady, které se hodí na kolo, koloběžku a brusle. Chránič měniče je spíš doplněk kola než ochrana jezdce, protože zabrání ohnutí patky a poškození pohonu při pádu. Pohon samotný najdete v kategorii <a href="/cyklo-pohon/">cyklo pohon</a>.</p>'
          '<h2>Chrániče kolen a loktů</h2>'
          '<p>Kolena a lokty jsou ty části těla, které se při pádu odřou nebo naruší jako první. Tenké elastické návleky s pěnou jsou lehké a pohodlné, takže se hodí na delší výjezdy s technickým sjezdem. Tvrdá skořepina s hustou pěnou chrání víc, ale hřeje a na stoupání je vnímat. Jezdci na endurové trati proto často volí kompromis, tedy měkký chránič se zesílenou čéškou.</p>'
          '<ul><li><strong>Měkká pěna a vnitřní vložky:</strong> pohodlí na celý den, vhodné pro mírný terén a děti. Ochrana proti tupým nárazům je střední.</li>'
          '<li><strong>Technologie s vlastnostmi tlumení nárazu:</strong> materiály typu D3O nebo VPD jsou měkké při běžném pohybu a při nárazu ztuhnou. Přesné parametry určuje výrobce, proto zkoumejte jeho popis.</li>'
          '<li><strong>Tvrdá skořepina:</strong> pro bikepark a downhill, kde jde víc o rychlost a skoky než o dlouhé stoupání.</li>'
          '<li><strong>Boční křidélka:</strong> chrání i kost na straně kolena, což ocení při pádu na bok.</li></ul>'
          '<p>Zásadní je, aby chránič při jízdě nesklouzával. Kontrolujte silikonové pásky u horního a spodního okraje a nastavitelné suché zipy. Při šlapání má koleno téměř plnou ohybovou dráhu, tak se ujistěte, že chránič nesvírá podkolenní jamku.</p>'
          '<h2>Chránič páteře a bederní část</h2>'
          '<p>Páteřák je nejdražší a pro mnoho jezdců nejzbytečnější část výbavy, dokud nezažijí pád na záda. Existují dvě varianty: samostatná vesta s vyjímatelnou vložkou, nebo batoh s integrovaným chráničem. Druhá možnost se hodí na celodenní výlet, protože se do ní vejde pití, bunda i náhradní duše. Mezi vyhledávané značky patří Leatt, Alpinestars, Poc a Scott.</p>'
          '<p>U velikostí buďte pozorní. Chránič má krýt záda od krční po bederní část, takže se vybírá podle délky zad, nikoli podle konfekční velikosti oblečení. Změřte vzdálenost od sedmého krčního obratle (hrbolek na šíji) po bederní část a porovnejte s tabulkou výrobce. Příliš dlouhý chránič brání ohnutí v sedle, příliš krátký odkrývá bederní část a křížovou kost.</p>'
          '<h2>Zápěstí, dlaně a děti</h2>'
          '<p>Při pádu dopředu automaticky vystřelíte ruce, a protože zápěstí je malé a křehké, bývá zlomené častěji než jiné klouby. Chrániče zápěstí mají pevnou dlahu na dlani nebo hřbetu, která brání přehnutí. Cyklisté je kombinují s rukavicemi, kolečkoví bruslaři a snowboardisti je nosí i bez nich. Všechny typy podrobněji řešíme u jiných sportů, třeba v kategorii <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>.</p>'
          '<p>Pro děti je nejpraktičtější komplet kolena, lokty a zápěstí. Menší jezdci se k zemi dostanou zblízka, ale padají často, takže sada s pohodlným suchým zipem se vyplatí. Značky jako Cariboo nebo licenční sady s motivy z pohádek jsou více rekreační a pro první kilometry bohatě stačí. Při přechodu na horská kola s delším sjezdem se ale vyplatí vyměnit je za odborné chrániče. Dětskou helmu najdete v kategorii <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>, kola v <a href="/detska-kola/">dětských kolech</a>.</p>'
          '<h2>Jak vybrat velikost a ověřit padnutí</h2>'
          '<ol><li><strong>Změřte:</strong> obvod stehna nad kolenem, obvod lýtka, obvod paže nad loktem a délku zad. U kolen se většinou měří dva obvody, protože chránič musí sedět nad i pod kloubem.</li>'
          '<li><strong>Porovnejte s tabulkou:</strong> každá značka má vlastní střih. Alpinestars a Leatt bývají sportovnější, TSG volnější.</li>'
          '<li><strong>Vyzkoušejte na kole:</strong> doma si sedněte na sedlo nebo udělejte dřep a zkontrolujte, zda se chránič neposouvá. Při pohybu nesmí tlačit v ohybu kolena.</li>'
          '<li><strong>Zkontrolujte kombinaci:</strong> kolena se mají nasadit pod kraťasy nebo přes ně podle střihu. Pokud nosíte volné MTB šortky, hodí se chrániče, které se dají navléknout zdola.</li></ol>'
          '<h2>Výběr podle stylu jízdy</h2>'
          '<ul><li><strong>Cross-country a výlety:</strong> lehké textilní návleky na kolena a lokty. Dají se sbalit do batohu a nasadit až před sjezdem.</li>'
          '<li><strong>Trail a all-mountain:</strong> měkké chrániče s pěnou, které se dají nosit celý den, a páteřák v batohu.</li>'
          '<li><strong>Enduro:</strong> pevnější kolena, lokty a páteřák s větší plochou. Vhodná jsou i <a href="/celoodpruzena-horska-kola/">celoodpružená horská kola</a>.</li>'
          '<li><strong>Bikepark a downhill:</strong> tvrdé chrániče, integrální helma, chránič stehen a boků. V tomto případě se nevyplatí šetřit.</li>'
          '<li><strong>Dirt a pumptrack:</strong> kolena, lokty a zápěstí, vzhledem k častým pádům na tvrdý povrch. Hodí se <a href="/bmx-a-dirt-kola/">BMX a dirt kola</a>.</li>'
          '<li><strong>Městská jízda a děti:</strong> základní chrániče kolen a loktů, rukavice a helma.</li></ul>'
          '<h2>Ochrana pro různé věkové skupiny a pohlaví</h2>'
          '<p>Dámské chrániče mívají užší pas a jiné tvarování kolem hrudníku a boků, takže na ženské postavě sedí stabilněji než unisex střih. Dětské velikosti mají kratší pásky a menší pěnové plochy. Teenageři na hraně mezi dětskou a dospělou velikostí se řídí hlavně délkou zad a obvodem stehna, ne věkem. Pokud sdílíte chrániče v rodině, ověřte, že nastavitelné pásky opravdu pokryjí rozdíl velikostí.</p>'
          '<h2>Jak chránič nosit v praxi</h2>'
          '<p>Chránič kolen se obléká před výjezdem na kopec a při stoupání se může stáhnout pod kolena. Páteřák se zapíná těsně, ale tak, abyste se mohli volně nadechnout, a při jízdě se kontroluje, zda nesjel nahoru. Pod chránič se nosí funkční tričko, které odvádí pot. Mokrá pěna vlhne, proto se vyplatí mít na delší výlety náhradní tričko a po sjezdu chránič vysušit.</p>'
          '<ul><li>Před sjezdem zkontrolujte suché zipy a pásky.</li><li>Při prudkém stoupání chrániče stáhněte pod koleno, ať nehřejí.</li><li>Na dětech zkontrolujte, zda je nic neškrábe.</li></ul>'
          '<h2>Péče o chrániče</h2>'
          '<p>Chránič, který se z tašky vytáhne zapáchající, se přestane nosit. Po jízdě jej vyndejte z batohu, nechte uschnout při pokojové teplotě a nesušte u radiátoru ani na slunci, protože pěna a lepidla tuhnou. Většinu měkkých chráničů lze ručně vyprat v teplé vodě s jemným mýdlem, tvrdé skořepiny stačí otřít vlhkým hadrem. Suché zipy očistěte od vláken a vlasů, aby držely.</p>'
          '<p>Po silném nárazu chránič zkontrolujte. Pokud je pěna trvale promáčknutá, trhlinky v plastu viditelné nebo materiál tuhne, přestává plnit funkci a patří vyměnit. Zvlášť to platí u tvrdých skořep a technologií, které se po zásahu přestanou chovat jako dřív.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Chránič kupovaný o číslo větší s tím, že dítě doroste. Volný chránič sjede mimo kloub a nic nechrání.</li>'
          '<li>Podcenění zad. Mnoho jezdců investuje do kolen a zapomíná na páteř.</li>'
          '<li>Chránič, který se nedá nosit celý den. Pokud hřeje nebo tlačí, zůstane v tašce.</li>'
          '<li>Spoléhání na jedinou součást. Chrániče nenahradí helmu a rukavice.</li>'
          '<li>Neověřená kompatibilita s oblečením a protektory. Zkoušejte je s tím, co nosíte na kole.</li></ul>'
          '<h2>Co dalšího se hodí k cyklistické ochraně</h2>'
          '<p>Výbava nekončí chrániči. Na delší túru se vyplatí <a href="/cyklo-tasky-a-nosice/">cyklistické tašky a nosiče</a>, na údržbu kola <a href="/cyklo-udrzba/">cyklo údržba</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Rozjíždíte-li se po setmění, nezapomeňte na <a href="/cyklo-svetla/">cyklo světla</a>. Souhrn doplňků najdete v <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu, ukazujeme dostupné velikosti a odlišujeme výprodeje. Při nákupu otevřete tabulku velikostí výrobce a ověřte, zda je uvedena pro obě strany těla, protože u některých sad se prodávají kusy jednotlivě. Zjistěte také, jestli je chránič určený pro dámy, pány či děti, protože střih se liší.</p>',
    faq=[
        ('Potřebuji chrániče na horské kolo?', 'Záleží na terénu. Na lehké výlety stačí helma a rukavice, ale ve sjezdech a bikeparku se kolena, lokty a záda vyplatí, protože tam rychlost a překážky zvyšují riziko vážného zranění.'),
        ('Jaký je rozdíl mezi měkkými a tvrdými chrániči?', 'Měkké se lépe nosí na delší výlety a mají lehkou až střední ochranu. Tvrdé skořepiny odolají hrubšímu nárazu a oděru, ale jsou těžší a hřejí.'),
        ('Jak poznám správnou velikost chráničů kolen?', 'Změřte obvod stehna nad kolenem a lýtka pod ním a porovnejte s tabulkou výrobce. Chránič má sedět pevně, ale netlačit v ohybu a nesmí sjíždět při šlapání.'),
        ('Je chránič páteře nutný?', 'Není povinný, ale při rychlých sjezdech a skocích chrání páteř před tupým nárazem. Dá se koupit jako vesta nebo v batohu a vybírá se podle délky zad.'),
        ('Mohu používat chrániče z inline bruslí na kolo?', 'Pro děti a pomalou jízdu ano, protože zápěstí, lokty a kolena jsou chráněná podobně. Pro terénní sjezdy jsou ale odborné cyklistické chrániče pohodlnější a mají lepší ochranu.'),
        ('Jak často chrániče měnit?', 'Po silném nárazu nebo když pěna ztuhne, popraská nebo se trvale zdeformuje. Bez nehody záleží na používání a skladování, ale po několika sezonách se pěna obvykle unaví.'),
        ('Jak vyprat cyklistické chrániče?', 'Vyjměte tvrdé části, měkké chrániče ručně vyperte ve vlažné vodě s jemným mýdlem a nechte je uschnout na vzduchu. Nesušte je u radiátoru ani na přímém slunci.'),
        ('Co je chránič přehazovačky?', 'Je to doplněk kola, který chrání zadní měnič a patku rámu při pádu nebo převrácení. Nechrání jezdce, ale může ušetřit drahou opravu pohonu.'),
        ('Jaké chrániče koupit pro dítě?', 'Komplet kolen, loktů a zápěstí s pohodlným suchým zipem v přesné velikosti. K tomu helma určená pro děti, která dobře sedí a nesjíždí do čela.'),
        ('Lze chrániče nosit pod oblečením?', 'Tenké a elastické chrániče ano, tvrdé skořepiny ne. Při nákupu zkontrolujte, zda je chránič určený pod nebo přes kalhoty a šortky.'),
    ],
)

# ------------------------------------------------------------------ gravel-kola
NEW['gravel-kola'] = dict(long=True,
    title='Gravel kola: geometrie, výbava, výběr velikosti rámu',
    desc='Gravel kola pro šotolinu, asfalt i lesní cesty. Jak vybrat rám, pláště, pohon a velikost a porovnat nabídky gravelových kol v českých obchodech.',
    intro='<p>Gravel kolo vzniklo z touhy jet dlouho, daleko a nezávisle na povrchu. Má beranidlové řídítko jako silnice, kotoučové brzdy, širší pláště a delší rozvor, takže na šotolině drží stopu a na asfaltu se nenudí. Sporteka porovnává nabídky českých obchodů u gravelových kol od základních modelů s hliníkovým rámem po karbonové stroje s elektronickým řazením.</p>'
          '<p>V nabídce jsou značky ' + B(('van-rysel', 'VAN Rysel'), ('trek', 'Trek'), ('kellys', 'Kellys'), ('bottecchia', 'Bottecchia'), ('specialized', 'Specialized'), ('sava', 'Sava'), ('kross', 'Kross'), ('author', 'Author'), ('ghost', 'Ghost'), ('ridley', 'Ridley')) +
          '. Hranice k <a href="/silnicni-kola/">silničním kolům</a>, <a href="/krosova-kola/">krosovým kolům</a> i <a href="/horska-kola/">horským kolům</a> je plynulá, proto níže rozebíráme, v čem se gravel liší a komu se opravdu vyplatí.</p>',
    guide='<h2>Čím se gravel liší od silničky a krosu</h2>'
          '<p>Na první pohled vypadá gravel jako silniční kolo, při bližším pohledu je ale všechno uvolněnější. Rám má delší rozvor a nižší středové složení pro stabilitu, trubky jsou odolnější proti prázdnému terénu a vidlice i rám nabízejí prostor pro širší plášť. Poloha je mírně vzpřímenější než u závodní silničky, takže záda vydrží celý den.</p>'
          + T(['Kolo', 'Řídítka', 'Pláště', 'Silná stránka'], [
              ['Silniční', 'beran, závodní poloha', 'úzké, hladké', 'rychlost na asfaltu'],
              ['Gravel', 'beran s rozšířenými konci', 'střední, jemný vzorek', 'univerzálnost, dlouhé trasy'],
              ['Krosové', 'rovné řídítko', 'střední, kombinovaný vzorek', 'pohodlí, přehled v provozu'],
              ['Horské', 'rovné, široké řídítko', 'široké, hrubý vzorek, odpružení', 'technický terén'],
              ['Treking', 'rovné nebo vzpřímené', 'střední, dobře odolné', 'nosiče, blatníky, cestování']]) +
          '<p>Pokud je vaší hlavní jízdou silnice, vyplatí se spíš <a href="/silnicni-kola/">silniční kolo</a>. Pokud vozíte batoh a jezdíte po cestách ve městě, stačí <a href="/krosova-kola/">krosové</a> nebo <a href="/trekingova-kola/">trekingové</a>. Společná kategorie obou je <a href="/silnicni-a-gravel-kola/">silniční a gravel kola</a>. Zájemci o motor najdou nabídku v <a href="/silnicni-a-gravel-elektrokola/">silničních a gravel elektrokolech</a>.</p>'
          '<h2>Rám: hliník, ocel, karbon</h2>'
          '<p>Materiál rámu určuje hmotnost, tlumení a cenu, i když výsledný dojem záleží na geometrii a plášti stejně tolik. Většina gravelů ve střední třídě má hliníkový rám a karbonovou nebo hliníkovou vidlici. Karbon nabízí nízkou hmotnost a tlumení vibrací, hliník je odolný proti údržbě a běžným nárazům, ocel je pružná a opravitelná, ale těžší.</p>'
          '<ul><li><strong>Hliník:</strong> nejčastější volba u modelů pro začátečníky, nenáročný na péči.</li>'
          '<li><strong>Karbon:</strong> lehký a tlumí hrubý povrch, vyžaduje opatrné utahování šroubů a ochranu při přepravě.</li>'
          '<li><strong>Ocel a titan:</strong> vyhledávané u dobrodružných kol a cestovatelů, protože se dobře opravují.</li>'
          '<li><strong>Průchod kabelů a úchyty:</strong> rám s oky pro nosiče, blatníky a láhve se hodí k cestování.</li></ul>'
          '<h2>Pláště a kola</h2>'
          '<p>Plášť je nejdůležitější součást gravelu. Typická šířka se pohybuje zhruba od 35 do 50 mm podle značky a rámu. Širší plášť jede měkčeji a drží na štěrku, užší je rychlejší na asfaltu. Většina kol používá průměr 700C, některé se dají přezout na 650B s ještě širším pláštěm. Prostor v rámu limituje, proto ověřte maximální šířku pláště v parametrech.</p>'
          '<p>Stále více gravelů je připraveno pro bezdušové pláště, což snižuje počet defektů a umožňuje nižší tlak. Podle zátěže a povrchu se tlak liší, výrobce kola i pláště uvádí doporučený rozsah. Příslušenství najdete v kategoriích <a href="/cyklo-kola-a-rafky/">kola a ráfky</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Pohon a řazení</h2>'
          '<p>Gravelové skupiny využívají zdrobnělé převody a široký rozsah kazety, protože při jízdě s batohem a v kopcích potřebujete lehký převod. Typickou volbou je jedna převodnice vpředu (1×) nebo dvě (2×). Jednopřevodníkový systém je jednodušší a čistější, dvoupřevodníkový nabízí jemnější odstupňování a vyšší rychlost na rovině.</p>'
          '<ul><li><strong>1× pohon:</strong> méně součástí, menší riziko shození řetězu, užitečný pro terén a dlouhé cestování.</li>'
          '<li><strong>2× pohon:</strong> širší rozsah a menší skoky mezi převody, vhodný pro rychlejší jezdce a vyváženou jízdu po asfaltu.</li>'
          '<li><strong>Mechanické a elektronické řazení:</strong> elektronika řadí přesně a bez ladění lanek, ale je dražší a vyžaduje nabíjení baterie.</li>'
          '<li><strong>Specifické skupiny pro gravel:</strong> zahrnují klece pro delší řetěz, spojku proti kmitání řetězu a odolnější konstrukci.</li></ul>'
          '<p>K údržbě a výměně součástek se hodí <a href="/cyklo-pohon/">cyklo pohon</a>, <a href="/cyklo-brzdy/">brzdy</a>, <a href="/cyklo-riditka/">řídítka</a> a <a href="/cyklo-pedaly/">pedály</a>.</p>'
          '<h2>Brzdy: kotouče a hydraulika</h2>'
          '<p>Gravelová kola mají téměř vždy kotoučové brzdy. Mechanické se nastavují lankem a opraví se kdekoli, hydraulické brzdí citlivěji a s menším tlakem prstů, což ocení dlouhé sjezdy se zátěží. Velikost kotouče určuje brzdný výkon a odvod tepla. U těžších kol a na dlouhých sjezdech se hodí větší kotouč.</p>'
          '<h2>Jak vybrat velikost rámu</h2>'
          '<p>Nejpřesněji se velikost vybere podle délky nohavice a dosahu na řídítka, nikoli jen podle výšky postavy. Výrobci uvádějí tabulky s doporučeným rozpětím výšky a často uvádějí také tzv. stack a reach. U modelů, které se prodávají na internetu, ověřte rozměry rámu v centimetrech a porovnejte je s kolem, na kterém dobře sedíte.</p>'
          '<ol><li>Změřte vnitřní délku nohavice (od rozkroku k podlaze).</li>'
          '<li>Porovnejte s tabulkou výrobce, která uvádí doporučenou velikost rámu.</li>'
          '<li>Zkontrolujte délku horní trubky a představce. Pokud mezi dvěma velikostmi váháte, menší rám se dá doladit delším představcem, větší ne.</li>'
          '<li>Nastavte sedlo tak, aby noha v dolní poloze byla jen lehce pokrčená.</li></ol>'
          '<h2>Výběr podle způsobu jízdy</h2>'
          '<ul><li><strong>Rekreační jezdec:</strong> hliník, širší plášť, jednodušší skupina a pohodlná geometrie. Stačí rozumné brzdy a spolehlivé náboje.</li>'
          '<li><strong>Dojíždění do práce:</strong> závitová oka na blatníky a nosiče, <a href="/cyklo-blatniky/">blatníky</a> a <a href="/cyklo-svetla/">světla</a>. Dobře se hodí také <a href="/cyklo-zamky/">zámek</a>.</li>'
          '<li><strong>Bikepacking a cestování:</strong> kolo s více úchyty, rám se prostorem pro brašny. Vhodné jsou <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a> a láhve v <a href="/cyklo-lahve-a-drzaky/">držácích</a>.</li>'
          '<li><strong>Sportovní jezdec a závodník:</strong> karbonový rám, lehká kola, elektronické řazení.</li>'
          '<li><strong>Zájemci o terén:</strong> širší pláště, geometrie s nižším středovým složením. Pokud jedete technické singletraily, zvažte <a href="/horska-kola/">horské kolo</a>.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Většina modelů jsou celá kola v různých velikostech rámu, od základních s mechanickými brzdami po sportovní karbony. Často jde o varianty stejného modelu v několika barvách a velikostech, třeba řady Kellys Soot nebo Specialized Diverge. Nejvíce je zastoupen VAN Rysel, dále Trek, Kellys, Bottecchia a Specialized. Najdou se i levnější gravely značek Storm nebo Sava.</p>'
          '<h2>Příslušenství, které gravel využije</h2>'
          '<p>Gravel je platforma, kterou si doplníte podle způsobu jízdy. Na delší trasy se hodí brašna pod rám, brašna na řídítka a sedlová brašna, na jednodenní výlet postačí batoh a láhev. Dobré sedlo a ergonomická omotávka řídítek rozhodují o pohodlí po třech hodinách v sedle. Pedály volte podle bot: platformové pro běžné tenisky, nášlapné pro sportovní jízdu. Svítilnu a zadní blikačku mějte i při jízdě za dne, protože polní cesty vedou často lesem a stíny.</p>'
          '<ul><li><strong>Sedlo:</strong> širší pro dlouhé trasy, užší pro sportovní jízdu. Viz <a href="/cyklo-sedacky-a-voziky/">sedla a vozíky</a>.</li>'
          '<li><strong>Cyklopočítač:</strong> navigace pro neznámé cesty, viz <a href="/cyklo-computery/">cyklopočítače</a>.</li>'
          '<li><strong>Zámek:</strong> pevný U-zámek nebo řetěz na zastávky v obci.</li>'
          '<li><strong>Základní nářadí:</strong> multiklíč, duše, montážní páky a pumpa vždy v tašce.</li></ul>'
          '<h2>Jaký tlak a jaké nastavení zvolit</h2>'
          '<p>Nižší tlak v pláštích zvýší záběr a pohodlí, ale zvyšuje riziko proražení ráfku a odpor na asfaltu. S těžším jezdcem nebo zavazadly je potřeba tlak zvednout, v mokru a na hrubé šotolině naopak snížit. Vyzkoušejte pár hodnot a najděte kompromis. Pozor na minimální a maximální tlak uvedený na boku pláště.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Po jízdě v blátě omyjte kolo vodou z hadice a osušte řetěz. Na čištění nepoužívejte tlakovou myčku přímo na ložiska.</li>'
          '<li>Řetěz pravidelně mažte olejem určeným na kola a přebytek setřete. Na prašných trasách se hodí suché mazivo.</li>'
          '<li>Kontrolujte tlak v plášti před každou delší jízdou.</li>'
          '<li>Brzdové destičky kontrolujte po každém dlouhém sjezdu, mohou se vyrábět rychleji než na silnici.</li>'
          '<li>Karbonové součásti utahujte momentovým klíčem podle předpisu výrobce.</li></ul>'
          '<p>Další rady a nářadí najdete v kategorii <a href="/cyklo-udrzba/">cyklo údržba</a>.</p>'
          '<h2>Kdy se vyplatí koupit</h2>'
          '<p>Nové modely se představují obvykle na přelomu léta a podzimu a minulý ročník pak bývá výhodnější. Velikosti uprostřed řady se vyprodají první, krajní zůstávají déle. Pokud kolo neplánujete jen na víkend, počítejte i s drobnými náklady navíc, jako jsou pedály (některé kompletní kola je nemají), zvonek, světla a helma. Se Sportekou snadno uvidíte, ve kterém obchodě je vaše velikost skladem a jaká je dostupnost.</p>'
          '<p>Před koupí také rozhodněte, zda potřebujete kolo bez kompromisů, nebo spíš univerzální. Univerzální gravel s hliníkovým rámem a rozumnou výbavou je pro většinu rekreačních jezdců lepší volba než extrémně lehký karbon, který se hůře opravuje a s nímž se hůř zachází.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr podle vzhledu a ne podle velikosti rámu. Špatný rám trápí zápěstí, záda a krk.</li>'
          '<li>Koupě silniční kola s tím, že se na ně dají dát široké pláště. Rám často nemá prostor.</li>'
          '<li>Podcenění brzd a kol při těžším nákladu.</li>'
          '<li>Nezjištěná dostupnost náhradních dílů, zejména u méně rozšířených standardů.</li>'
          '<li>Chybějící ochrana. K jízdě patří <a href="/cyklisticke-helmy/">cyklistická helma</a> a při terénu <a href="/cyklo-chranice/">chrániče</a>.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu a ukazujeme, které velikosti rámu jsou skladem. U kola ověřte rok modelu, velikost rámu, skupinu a šířku pláště. Pamatujte, že kolo je potřeba před jízdou sestavit a zkontrolovat, což zvládne prodejna nebo servis.</p>',
    faq=[
        ('Jaký je rozdíl mezi gravelem a silničním kolem?', 'Gravel má širší pláště, delší rozvor a odolnější konstrukci pro neasfaltované cesty. Silniční kolo je lehčí a rychlejší na asfaltu, ale na šotolině je nestabilnější.'),
        ('Pro koho je gravel kolo vhodné?', 'Pro jezdce, kteří střídají asfalt, polňačky a lesní cesty, i pro ty, kteří chtějí jedno kolo na dlouhé výlety, dojíždění a cestování s brašnami.'),
        ('Jak široký plášť zvolit?', 'Na převážně zpevněné cesty stačí užší plášť kolem 35 mm, na šotolinu a lesní cesty se hodí širší. Maximum určuje prostor v rámu a vidlici.'),
        ('Je lepší 1× nebo 2× pohon?', '1× je jednodušší a méně náchylný k poruchám, 2× nabízí jemnější odstupňování. Pro terén a cestování většinou stačí 1×, pro sportovní jízdu po asfaltu se hodí 2×.'),
        ('Jak vybrat velikost rámu?', 'Podle délky nohavice, dosahu na řídítka a tabulky výrobce. Nevybírejte jen podle výšky, protože střih rámu se liší mezi značkami.'),
        ('Lze na gravel nasadit blatníky a nosič?', 'Pokud má rám a vidlice oka na jejich montáž. Zkontrolujte parametry modelu, protože závodněji laděné gravely je často nemají.'),
        ('Jsou kotoučové brzdy nutné?', 'U gravelu jsou standardem, protože brzdí spolehlivě v blátě i za mokra. Hydraulické brzdí citlivěji, mechanické se snadněji opraví.'),
        ('Hodí se gravel na dojíždění?', 'Ano, pokud má oka na blatníky a nosič a zvolíte odolnější pláště. Sedí se vzpřímeněji než na silničce a pláště zvládnou obrubníky a štěrk.'),
        ('Je gravel vhodný pro začátečníka?', 'Je, protože je stabilní a odpouští chyby, pokud zvolíte správnou velikost a jednodušší výbavu. Sportovní karbonové modely nejsou pro první kolo nutné.'),
        ('Jak často servisovat gravelové kolo?', 'Základní kontrolu dělejte před každou jízdou, mazání řetězu po mokré jízdě a servis ložisek a brzd podle najetých kilometrů. Doporučený interval uvádí výrobce.'),
    ],
)

# ------------------------------------------------------------------ rybarske-spacaky
NEW['rybarske-spacaky'] = dict(long=True,
    title='Rybářské spacáky a lehátka se spacákem: výběr',
    desc='Rybářské spacáky a lehátka se spacákem pro kapraře: teplota, vodoodpudivost, rozměry a sleep systémy. Porovnejte nabídky českých obchodů.',
    intro='<p>Kdo přespává u vody, ví, že noc na břehu je jiná než noc na kempu. Vlhký vzduch, ranní rosa, studená zem a nepředvídatelné počasí vyžadují spací výbavu, která je větší, odolnější a pohodlnější než ta turistická. Kapraři proto často kupují celé sleep systémy, tedy lehátko a spacák společně. Sporteka porovnává nabídky českých obchodů u rybářských spacáků, lehátek se spacákem i samostatných spacích pytlů.</p>'
          '<p>V kategorii najdete značky ' + B(('fox', 'Fox'), ('delphin', 'Delphin'), ('trakker-products', 'Trakker Products'), ('giants-fishing', 'Giants Fishing'), ('mikado', 'Mikado'), ('prologic', 'Prologic'), ('jrc', 'JRC'), ('gardner', 'Gardner')) +
          '. K výbavě patří <a href="/rybarske-stany/">rybářské stany</a>, <a href="/rybarske-tasky/">rybářské tašky</a> a <a href="/rybarske-obleceni/">rybářské oblečení</a>, obecné modely najdete v <a href="/spaci-pytle/">spacích pytlích</a>.</p>',
    guide='<h2>Jaké druhy rybářských spacích systémů existují</h2>'
          '<p>Na výběr je několik řešení podle toho, jak často a kde přespáváte. Krátký výlet na jednu noc nevyžaduje stejnou výbavu jako týdenní výjezd s několika kaprovými nástrahami. Společné mají to, že spacák musí být dost široký pro pohodlné otáčení a dost hřejivý, aby noční teplota u hladiny nebyla problém.</p>'
          + T(['Typ', 'Co obsahuje', 'Hodí se pro'], [
              ['Samostatný spací pytel', 'jen spacák, často větší střih', 'kdo už má lehátko nebo spí na zemi'],
              ['Spacák s přehozem', 'spacák doplněný o vrchní vrstvu proti vlhku', 'změny počasí a chladnější noci'],
              ['Lehátko se spacákem', 'komplet na jedno nákupní rozhodnutí', 'kapraři na vícedenních výjezdech'],
              ['Sleep systém', 'lehátko, spacák a někdy přehoz nebo polštář', 'celoroční rybaření'],
              ['Lehký spacák', 'úsporný, kompresní', 'letní nocování, krátké výlety'],
              ['Čtyřsezónní spacák', 'silná výplň, kompresní vak', 'jaro, podzim a studenější noci']]) +
          '<p>Lehátko se spacákem je ucelená varianta: spací pytel často drží přímo v rámu lehátka nebo se k němu připíná, takže se nesune. Samostatný spací pytel zase můžete použít i na jiné účely, třeba na kempování ve stanu. Obecné typy najdete v kategoriích <a href="/perove-spacaky/">péřové spacáky</a>, <a href="/dekove-spacaky/">dekové spacáky</a> a <a href="/detske-spacaky/">dětské spacáky</a>.</p>'
          '<h2>Teplota a sezónnost</h2>'
          '<p>Výrobci rybářských spacáků často používají označení sezón (třeba tři nebo pět), místo přesných teplot. Čím víc sezón, tím silnější výplň a teplejší spacák. Jenže tato označení nejsou jednotná a každá značka je vykládá trochu jinak, takže se vyplatí hledat číselné údaje o komfortní a extrémní teplotě, pokud je výrobce uvádí. Norma EN 13537 je u turistických spacáků běžná, rybářské často uvádějí jen přibližné hodnoty.</p>'
          '<ul><li><strong>Léto:</strong> tenčí spacák nebo rozepnutý model, protože noční teplota u vody bývá chladnější než přes den.</li>'
          '<li><strong>Jaro a podzim:</strong> střední výplň a přehoz. Většina rybářských výjezdů probíhá právě v této době.</li>'
          '<li><strong>Zima:</strong> silný čtyřsezónní nebo pětisezónní spacák, izolační podložka pod lehátkem a čepice na spaní.</li>'
          '<li><strong>Rezerva:</strong> pamatujte, že chlad přichází také ze země. Spacák ohřeje shora, ale lehátko nebo karimatka musí izolovat zdola.</li></ul>'
          '<h2>Lehátko: rám, nohy a výška</h2>'
          '<p>Rybářské lehátko je robustnější než turistické, protože stojí na nerovném břehu, v blátě a na kamení. Nejdůležitější je počet nohou a jejich nastavení. Šestinohá a osminohá lehátka rozloží váhu lépe a stabilizují se na svažitém břehu, nastavitelné nohy pomáhají vyrovnat terén. Nízká konstrukce je lehčí, vyšší umožňuje sednout si na okraj a obout se bez ležení v blátě.</p>'
          '<ul><li><strong>Nosnost:</strong> ověřte maximální zatížení a rozměr ležící plochy. Větší jezdec potřebuje širší lehátko.</li>'
          '<li><strong>Výška a sklon:</strong> sklopné opěradlo se hodí na čtení a sezení u prutů.</li>'
          '<li><strong>Rozložená a složená velikost:</strong> lehátko musí projít zavazadlovým prostorem auta spolu s dalším vybavením.</li>'
          '<li><strong>Hmotnost:</strong> lehátko, které se těžko nese od auta k vodě, se brzy přestane používat.</li></ul>'
          '<h2>Materiál, vodoodpudivost a výplň</h2>'
          '<p>Rybářský spacák má povrch z odolné tkaniny, která snese ostré větvičky a vlhkost. Mnoho modelů má vodoodpudivou povrchovou úpravu, která chrání před rosou. Nejde o nepromokavost a pod deštěm bez stanu by spacák zvlhl. Podšívka bývá hladká nebo flísová a výplň je téměř vždy syntetická, protože na rozdíl od peří izoluje i při částečném provlhnutí.</p>'
          '<ul><li><strong>Syntetická výplň:</strong> snese vlhko, rychleji schne a má nižší nároky na péči.</li>'
          '<li><strong>Dutá vlákna:</strong> nabízejí větší objem a hřejivost při nižší hmotnosti.</li>'
          '<li><strong>Kamufláž:</strong> hodí se, pokud nechcete u břehu zbytečně vyčnívat. Žádný vliv na teplotu nemá.</li>'
          '<li><strong>Zipy:</strong> robustní s krytím proti průvanu a kapsou na drobnosti. Oboustranný zip umožňuje větrání nohou.</li></ul>'
          '<h2>Střih, rozměry a pohodlí</h2>'
          '<p>Rybářský spacák bývá širší a delší než turistická mumie. Důvodem je pohodlí: rybáři často spí v oblečení a potřebují se uvnitř volně otáčet. Širší střih ale znamená, že je uvnitř víc vzduchu a spacák se hůře ohřívá. Proto výrobci doplňují přehozy a šité přepážky, které objem rozdělí.</p>'
          '<p>Při výběru porovnejte rozměry spacáku s postavou a se šířkou lehátka. Příliš široký spacák na úzkém lehátku se svine, příliš úzký tlačí. Většina modelů nabízí oboustranný zip, který se dá celý rozepnout a použít jako deka. Menší střihy se hodí i pro <a href="/detske-spacaky/">děti</a>.</p>'
          '<h2>Výběr podle doby pobytu</h2>'
          '<ul><li><strong>Jedna noc:</strong> jednoduchý spacák na lehátko, případně samotný pytel na karimatce.</li>'
          '<li><strong>Víkend nebo několik nocí:</strong> lehátko se spacákem, plus přehoz na chladné ráno.</li>'
          '<li><strong>Dlouhé výjezdy:</strong> kompletní sleep systém s osminohým lehátkem, silným spacákem a doplňky. Vyplatí se i <a href="/vlozky-do-spacaku/">vložka do spacáku</a>, kterou lze snadno vyprat.</li>'
          '<li><strong>Zimní rybaření:</strong> teplejší výplň, izolace pod lehátkem a stan s dobrou ochranou proti větru, třeba z kategorie <a href="/rybarske-stany/">rybářské stany</a>.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie obsahuje samostatné spacáky, kompletní lehátka se spacákem i sleep systémy značek Fox, Delphin a Trakker, dále Giants Fishing, Mikado a Prologic. Najdete i obecné velké spací pytle s kompresním vakem. Běžné je, že jeden model existuje v několika velikostech a barevných variantách, třeba řady Fox Ventec a Camolite nebo Trakker Levelite.</p>'
          '<h2>Příslušenství k lehátku a spacáku</h2>'
          '<p>Spací systém se dá doplnit o několik drobností, které rozhodnou o kvalitě spánku. Přehoz proti vlhku zvyšuje komfort o několik stupňů, polštář s nastavitelnou výškou ulevuje krku, a nepromokavý vak ochrání spacák při přepravě. Pokud lehátko stojí na měkké půdě, pomůže pod nohy podložit desky nebo speciální patky. Ke každému večeru patří také čelovka, kterou mějte po ruce hned vedle lehátka.</p>'
          '<ul><li><strong>Přehoz:</strong> lehká vrstva navíc, která se při zahřátí odhodí.</li><li><strong>Polštář:</strong> menší nafukovací nebo pěnový.</li><li><strong>Moskytiéra a odpuzovače:</strong> v létě u vody nezbytné.</li><li><strong>Přepravní vak:</strong> udrží spacák suchý a čistý.</li></ul>'
          '<h2>Jak se vyspat u vody</h2>'
          '<p>Rozložte lehátko na rovné místo a zkontrolujte, zda nohy nezapadají. Spacák vyvětrejte před uložením do vaku a nechte ho nabrat objem, protože stlačená výplň izoluje hůře. Na spaní neoblékejte těsné vrstvy, které brání prokrvení, a čepici nebo šálu použijte, když fouká. Snídaně či teplý nápoj z termosky zlepší ranní komfort. U vody je rozdíl teplot mezi dnem a nocí větší než v lese.</p>'
          '<p>Při koupi zvažte také hmotnost celé sestavy v zabaleném stavu. Kapraři přenášejí kromě lehátka také pruty, stan, rybářskou tašku a nástrahy, takže každý kilogram navíc se počítá. Rozložení spacáku do transportního vaku s popruhy usnadňuje nošení z auta k vodě.</p>'
          '<h2>Péče o spacák a lehátko</h2>'
          '<ul><li>Po výjezdu vyndejte spacák z kompresního vaku a nechte ho vyschnout. Zavlhlá výplň ztrácí izolaci a zapáchá.</li>'
          '<li>Skladujte spacák volně nebo ve velkém prodyšném pytli, ne dlouhodobě stlačený.</li>'
          '<li>Perte podle štítku, obvykle jemně a při nízké teplotě. Ostré prostředky a aviváže zbytečně poškozují vlákna.</li>'
          '<li>Rám lehátka po použití očistěte od bláta a vysušte, aby se nezačal kazit kloub a šrouby.</li>'
          '<li>Zkontrolujte zip a šití. Včas opravený zip vydrží víc sezón.</li></ul>'
          '<h2>Pro koho je rybářský spací systém vhodný</h2>'
          '<p>Hlavní skupinou jsou kapraři, kteří tráví u vody dlouhé hodiny a spí přímo u prutů, aby slyšeli signalizátor záběru. Hodí se ale i každému, kdo kempuje u auta a chce pohodlí větší, než dává turistická karimatka. Pro dlouhé pěší túry je těžký, proto jej nevybírejte jako batohovou výbavu. Pokud rybaříte jen přes den, spací systém nepotřebujete a víc se vám bude hodit rybářská židle nebo taška z kategorie <a href="/rybarske-tasky/">rybářské tašky</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Spoléhání na spacák bez izolace zespodu. Chlad ze země je největší zloděj tepla.</li>'
          '<li>Výběr podle počtu sezón bez ověření teplotních údajů.</li>'
          '<li>Příliš těžká sestava, která se těžko nosí k vodě. Vždy počítejte s tím, kolik toho unesete na jeden zátah.</li>'
          '<li>Zanedbání vlhkosti. Vlhký spacák hřeje výrazně hůř.</li>'
          '<li>Koupě lehátka bez ověření rozměru v dopravě. Někdy se nevejde do kufru spolu s vybavením.</li></ul>'
          '<h2>Co dalšího se hodí k nocování u vody</h2>'
          '<p>Kromě spacích systémů pomáhají <a href="/rybarske-doplnky/">rybářské doplňky</a>, <a href="/rybarske-obleceni/">oblečení</a> a <a href="/rybarske-tasky/">tašky</a>. Pokud se pouštíte do dalších činností, podívejte se na <a href="/rybareni/">rybaření</a> jako celek, <a href="/rybarske-pruty/">pruty</a>, <a href="/rybarske-navijaky/">navijáky</a> a <a href="/rybarske-lode-a-elektronika/">čluny a elektroniku</a>. Další bivaky najdete v <a href="/stany/">stanech</a>, <a href="/expedicni-stany/">expedičních stanech</a> a <a href="/turisticke-stany/">turistických stanech</a>.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu, zobrazujeme dostupné velikosti a barevné varianty. Při nákupu zkontrolujte rozměry, nosnost lehátka a typ výplně. U kompletů si ověřte, zda spacák a lehátko tvoří jeden produkt, nebo zda se kupují odděleně.</p>',
    faq=[
        ('Čím se rybářský spacák liší od turistického?', 'Bývá širší a odolnější, často s vodoodpudivým povrchem a robustním zipem. Je určený pro delší pobyt na jednom místě, takže nevadí vyšší hmotnost a objem.'),
        ('Co je sleep systém?', 'Je to komplet lehátka, spacáku a případně přehozu nebo polštáře, který se prodává jako jeden celek. Díky tomu k sobě díly rozměrově sedí a spacák se nesunuje.'),
        ('Kolik sezón spacák potřebuji?', 'Na léto stačí lehčí, na jaro a podzim střední a na zimu pětisezónní. Hledejte raději uvedené teploty, protože označení sezón se u značek liší.'),
        ('Je spacák vodotěsný?', 'Většinou jen vodoodpudivý, takže zvládne rosu a lehkou vlhkost. V dešti bez stanu by promokl, proto je potřeba přístřešek nebo stan.'),
        ('Proč má lehátko víc nohou?', 'Víc nohou rozloží váhu a umožňuje vyrovnat nerovný terén na břehu. Šest nebo osm nohou je stabilnější než čtyři, hlavně na měkké zemi.'),
        ('Potřebuji i izolaci pod lehátkem?', 'V chladných nocích ano. Spacák se pod vahou těla stlačí a zespodu málo izoluje, proto pomůže karimatka nebo izolační vložka.'),
        ('Jak vybrat velikost spacáku?', 'Porovnejte délku a šířku s výškou postavy a šířkou lehátka. Příliš velký spacák hůře drží teplo, příliš malý omezuje pohyb.'),
        ('Jak spacák sušit a skladovat?', 'Po použití ho vyvěste a nechte vyschnout. Skladujte volně v prodyšném pytli, ne dlouhodobě stlačený v kompresním vaku.'),
        ('Hodí se rybářský spacák na kempování?', 'Ano, zejména při pobytu u auta, protože je velký a hřejivý. Na turistiku s batohem je těžký a objemný.'),
        ('Jaká výplň je lepší, syntetika nebo peří?', 'U rybářských spacáků dominuje syntetika, která lépe snáší vlhko a rychleji schne. Peří je lehčí a lépe se komprimuje, ale při navlhnutí ztrácí izolaci.'),
    ],
)

# ------------------------------------------------------------------ snowboardove-chranice
NEW['snowboardove-chranice'] = dict(long=True,
    title='Chrániče páteře a boků na lyže a snowboard',
    desc='Chrániče páteře, boků a kostrče na lyže a snowboard: vesty, kraťasy, dětské a dámské modely. Jak vybrat velikost a porovnat nabídky obchodů.',
    intro='<p>Na sjezdovce se padá jinak než na kole. Snowboardista padá často na zadek a na záda, lyžař spíše na bok a při rychlém pádu naráží na ledový povrch. Chrániče páteře a boků proto patří mezi nejpraktičtější doplňky začátečníků i freeriderů. Sporteka porovnává nabídky českých obchodů u vest s chráničem zad, kraťasů s chráničem kostrče, chráničů pánve a dětských modelů. Kategorie je určena pro lyžaře i snowboardisty.</p>'
          '<p>V nabídce jsou značky ' + B(('dreamscape', 'Dreamscape'), ('scott', 'Scott'), ('qunature', 'Qunature'), ('salomon', 'Salomon'), ('poc', 'Poc'), ('cairn', 'Cairn'), ('atomic', 'Atomic'), ('head', 'Head'), ('alpina', 'Alpina')) +
          '. K ochraně se hodí <a href="/lyzarske-helmy/">lyžařské helmy</a>, <a href="/lyzarske-rukavice/">lyžařské rukavice</a> a pro začátečníky komplet z kategorie <a href="/snowboardove-sety/">snowboardové sety</a>.</p>',
    guide='<h2>Jaké druhy chráničů existují</h2>'
          '<p>Chrániče na sjezdovku se dělí podle místa, které chrání. Nejčastěji jde o záda, kostrč a boky, někdy i kolena a zápěstí. Páteřák se nosí buď jako vesta, nebo jako kratší chránič se šněrováním a popruhy, a dá se pod bundu schovat téměř neviditelně. Kraťasy s vloženou pěnou se hodí hlavně začátečníkům, kteří padají na zadek.</p>'
          + T(['Typ', 'Co chrání', 'Hodí se pro'], [
              ['Páteřová vesta', 'záda, často i žebra a ramena', 'freeride, rychlé lyžování, parky'],
              ['Chránič páteře na popruzích', 'páteř bez zbytečné vrstvy', 'všechny typy jezdců, kteří nechtějí vestu'],
              ['Kraťasy s chráničem kostrče', 'kostrč a boky', 'začátečníci na snowboardu a lyžích'],
              ['Chránič pánve', 'pánev a kyčle', 'parky, skoky, tvrdé pády'],
              ['Dětské vesty a kraťasy', 'záda, kostrč, boky', 'děti ve školách a kroužcích'],
              ['Dámské střihy', 'stejné části v užším střihu', 'ženy, které chtějí stabilnější padnutí'],
              ['Bagy a batohy s chráničem', 'záda v kombinaci s nosností', 'skialp, freeride, výlety mimo sjezdovku']]) +
          '<p>V kategorii najdete i věci, které s chrániči jen souvisejí, třeba cyklistický batoh s chráničem páteře nebo sjezdové lyže s vázáním. Pro sezónu je důležité vědět, že některé chrániče jsou určeny pro víc sportů zároveň. Pokud jezdíte také na kole, podívejte se do kategorie <a href="/cyklo-chranice/">chrániče pro cyklisty</a>.</p>'
          '<h2>Chránič zad a páteře</h2>'
          '<p>Páteřový chránič se skládá z pěny, plastových segmentů nebo kombinace obojího. Pěnové varianty jsou měkké a pohodlné, segmentové se lépe přizpůsobí ohybu těla a při zásahu rozloží sílu na větší plochu. Dnes se používají i materiály, které jsou měkké při pohybu a při nárazu ztuhnou. Přesný princip popisuje výrobce, proto čtěte popis konkrétního modelu.</p>'
          '<ul><li><strong>Délka chrániče:</strong> má krýt záda od horních obratlů po kostrč. Vybírá se podle délky zad, ne jen podle konfekční velikosti.</li>'
          '<li><strong>Odvětrání:</strong> perforace a prodyšné textilie zabrání přehřátí při sjezdu i při stoupání.</li>'
          '<li><strong>Zapínání:</strong> pás kolem břicha a popruhy přes ramena drží chránič na místě i při pádu.</li>'
          '<li><strong>Vyjímatelná vložka:</strong> usnadňuje praní a přenos mezi dvěma vestami.</li></ul>'
          '<p>Chránič páteře není záchranná vesta a nezaručuje bezpečí. Snižuje riziko odřenin a tupého nárazu, ale proti těžkým pádům a vysokým rychlostem nestačí. Vždy ho kombinujte s helmou a rozumnou jízdou.</p>'
          '<h2>Kostrč, boky a pánev</h2>'
          '<p>Kostrč je pro začátečníky nejzranitelnější část těla. Pád na zadek na tvrdém sněhu je velmi bolestivý a bolest může trvat týdny. Chránič kostrče a boků je proto většinou prvním nákupem snowboardisty. Kraťasy s vloženou pěnou se oblékají pod kalhoty, nejsou vidět a nepřekážejí. Existují i varianty s pevnějšími vložkami, které se hodí do snowparku.</p>'
          '<p>Při výběru ověřte, že pěna chrání nejen kostrč, ale i boky a horní část stehen, a že kraťasy neklouzají. Dámské kraťasy mají jiný střih v pase a v bocích, proto se dámské nosí lépe než pánské. Dětské verze jsou kratší a lehčí.</p>'
          '<h2>Chrániče pro děti</h2>'
          '<p>Děti se učí jezdit často a padají víc než dospělí. Dětský chránič proto musí mít správnou velikost a krýt záda, kostrč a boky, jinak svou roli neplní. Nejpraktičtější je vesta nebo kraťasy, které se obléknou pod bundu. Sleduje se pohodlí: pokud chránič tlačí nebo škrábe, dítě ho bude odmítat. Dětské modely jsou dostupné například od značek Scott, Cairn nebo Dreamscape.</p>'
          '<ul><li>Vybírejte podle výšky a délky zad dítěte, ne podle věku.</li>'
          '<li>Počítejte s tím, že dítě roste, ale příliš velký chránič nesedí a může sklouznout.</li>'
          '<li>K chrániči patří i <a href="/lyzarske-helmy/">dětská lyžařská helma</a>.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<ol><li><strong>Změřte délku zad:</strong> od sedmého krčního obratle po kostrč, a obvod hrudníku a pasu.</li>'
          '<li><strong>Porovnejte s tabulkou výrobce:</strong> střihy se liší. Poc a Scott bývají přesně tvarované, Dreamscape volnější.</li>'
          '<li><strong>Zkuste s vrstvami:</strong> chránič se nosí pod bundou, ale nad termoprádlem. Zkoušejte jej v oblečení, které budete nosit na sjezdovce.</li>'
          '<li><strong>Zkontrolujte pohyb:</strong> předkloňte se, zakloňte a otočte trup. Chránič nesmí škrtit ani sjíždět.</li></ol>'
          '<h2>Výběr podle stylu jízdy</h2>'
          '<ul><li><strong>Začátečník na snowboardu:</strong> kraťasy s chráničem kostrče a boků a ochrana zápěstí. K tomu <a href="/snowboardove-boty/">snowboardové boty</a>, které sedí.</li>'
          '<li><strong>Začátečník na lyžích:</strong> lehká vesta na záda a kostrč. Pro skluz se hodí také <a href="/lyzarske-vosky/">mazání lyží</a>.</li>'
          '<li><strong>Snowpark:</strong> pevný chránič kostrče a pánve, páteřová vesta a helma s dobrým krytím.</li>'
          '<li><strong>Freeride a skialpinismus:</strong> vesta, nebo batoh s chráničem páteře a lavinovou výbavou. Pokud se vydáváte mimo sjezdovku, podívejte se do <a href="/skialpinismus/">skialpinismu</a>.</li>'
          '<li><strong>Rekreační jezdec:</strong> lehký chránič páteře pod bundou, který nezasahuje do pohybu.</li>'
          '<li><strong>Děti:</strong> měkké chrániče s pohodlným padnutím.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Většina nabídky jsou páteřové vesty, chrániče páteře na popruzích a kraťasy nebo chrániče pánve značek Dreamscape, Scott, Qunature, Salomon, Poc a Cairn. Najdete i dětské, dámské a juniorské modely. Do kategorie se občas dostane i související zboží, například sjezdové lyže s vázáním nebo batohy s chráničem páteře, takže podle názvu poznáte, o co jde.</p>'
          '<h2>Jak se chránit i mimo sjezdovku</h2>'
          '<p>Na skialpových túrách a freeridu se chránič páteře kombinuje s lavinovou výbavou, což vyžaduje batoh, ve kterém vše sedí. Takový batoh s integrovaným chráničem zvyšuje komfort, protože se nedá zapomenout doma. Při zimní turistice a na ledu se také hodí chrániče zápěstí a kolen, protože pády na zledovatělé cestě jsou podobné jako na sjezdovce. Dbejte na to, aby chránič neomezoval přístup k lavinovým pomůckám.</p>'
          '<h2>Chrániče v parku a při skocích</h2>'
          '<p>Ve snowparku se skáče, jezdí po bednách a zábradlích a pády jsou prudší. Zde se hodí pevnější chránič kostrče a boků, ochrana zápěstí a páteřová vesta s větší plochou. Před prvními skoky si trasu projděte, zjistěte velikost doskoku a začněte na menších překážkách. Chrániče nejsou důvod riskovat víc, jsou pojistkou pro případ, že se něco nepovede.</p>'
          '<h2>Kdy chránič nasadit a kdy odložit</h2>'
          '<p>Chránič nasaďte už při první jízdě, kdy je riziko pádu největší, a při změně podmínek, například na tvrdém nebo ledovatém sněhu. Chránič se nosí celý den, i na snadné sjezdovce, protože k pádu dochází i při pomalé jízdě; zkušení jezdci ho proto neodkládají. Zkoušení v obchodě je užitečné, ale ověřte pohodlí i po hodině jízdy, kdy se teprve ukáže, zda někde netlačí.</p>'
          '<p>Před koupí také zvažte, zda budete chránič používat i při jiných sportech. Univerzální modely lze využít na kole, kolečkových bruslích i na skialpu, což zvyšuje hodnotu nákupu. Specializovaný snowparkový chránič naopak může být pro jiné sporty příliš tuhý.</p>'
          '<h2>Péče o chrániče</h2>'
          '<ul><li>Po sezoně vyperte chránič podle štítku, vyjměte vložky a nechte je uschnout na vzduchu.</li>'
          '<li>Nesušte ho u radiátoru ani na slunci, aby pěna neztvrdla.</li>'
          '<li>Uložte chránič plochý nebo zavěšený, ne pod těžkými předměty.</li>'
          '<li>Po silném nárazu zkontrolujte pěnu a plastové segmenty. Promáčknutá pěna nebo prasklý plast znamenají výměnu.</li>'
          '<li>Zkontrolujte zipy, sponky a popruhy, hlavně před začátkem sezony.</li></ul>'
          '<h2>Pro koho jsou chrániče určené</h2>'
          '<p>Nejčastěji je kupují začátečníci a rodiče dětí, ale pomáhají i zkušeným jezdcům, kteří se rozhodli zkoušet nové triky nebo jezdit rychleji. Pokud jezdíte jen občas a pomalu, bohatě stačí lehký chránič pod bundou. Když jezdíte často, na led a v davu nebo trénujete skoky, vyplatí se kvalitnější model s lepším tlumením. Pro lyžaře, kteří se vydávají mimo trať, existuje také kombinace s batohem.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Špatná velikost. Příliš volný chránič sklouzne a nechrání, příliš těsný omezuje dýchání.</li>'
          '<li>Spoléhání na jediný chránič. Zápěstí, kolena a hlava potřebují vlastní ochranu.</li>'
          '<li>Koupě na poslední chvíli. Zkoušejte doma a zvykejte si na ně, než poprvé vyrazíte.</li>'
          '<li>Pocit absolutní bezpečnosti. Rychlost a skoky riziko zvyšují, i když chrániče nosíte.</li>'
          '<li>Neodpovídající typ. Pro snowpark nestačí tenký textilní chránič a pro začátečníka je zbytečná těžká vesta.</li></ul>'
          '<h2>Co dalšího se hodí na sjezdovku</h2>'
          '<p>Kromě chráničů se hodí kompletní výbava. <a href="/snowboardy/">Snowboardy</a>, <a href="/snowboardova-vazani/">vázání</a> a <a href="/snowboardove-boty/">boty</a> tvoří základ, <a href="/lyzarske-bryle/">lyžařské brýle</a> a <a href="/lyzarske-rukavice/">rukavice</a> doplňují komfort. Souhrn najdete v kategoriích <a href="/snowboarding/">snowboarding</a> a <a href="/zimni-sporty/">zimní sporty</a>. Pro lyžaře je určena <a href="/lyzarske-helmy/">helma</a>, a pokud hledáte společnou ochranu hlavy a těla, prohlédněte si <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu, zobrazujeme dostupné velikosti a odlišujeme výprodeje. Při nákupu ověřte délku chrániče, střih (dámský, pánský, dětský) a to, zda je určen pro lyže, snowboard nebo oba sporty. V zimní sezoně se rychle vyprodávají nejčastější velikosti, proto s nákupem nečekejte na poslední chvíli.</p>',
    faq=[
        ('Potřebuje začátečník na snowboardu chránič páteře?', 'Hodí se, protože začátečníci padají hodně a často na záda. Pro první dny ale většinou víc pomůže chránič kostrče a boků, spolu s helmou a zápěstími.'),
        ('Jaký je rozdíl mezi vestou a chráničem na popruzích?', 'Vesta kryje i ramena a žebra, takže chrání víc, ale je objemnější. Chránič na popruzích se lépe schová pod bundu a stačí na běžnou jízdu.'),
        ('Jak změřit velikost chrániče zad?', 'Změřte vzdálenost od hrbolku na šíji po kostrč a obvod hrudníku a pasu. Pak porovnejte s tabulkou výrobce, protože střih se liší mezi značkami.'),
        ('Hodí se chránič na lyže i na snowboard?', 'Většina páteřových chráničů je určena pro oba sporty. Rozdíl je spíš ve zvyku: snowboardisté padají na zadek a záda, lyžaři na bok.'),
        ('Je chránič páteře dostatečná ochrana?', 'Ne, snižuje riziko odřenin a tupého nárazu, ale nenahrazuje helmu ani opatrnou jízdu. Při velké rychlosti a skocích ochranu neplní.'),
        ('Co jsou kraťasy s chráničem kostrče?', 'Jsou to elastické kalhotky s pěnovými vložkami na kostrči a bocích. Nosí se pod kalhotami a hodí se hlavně začátečníkům.'),
        ('Jak vybrat chránič pro dítě?', 'Podle výšky a délky zad, ne podle věku. Měkká vesta nebo kraťasy s pohodlným zapínáním, které dítě nebude odmítat.'),
        ('Dá se chránič nosit pod bundou?', 'Ano, většina vest a chráničů je navržena tak, aby se vešla pod lyžařskou bundu. Při zkoušce ověřte, že se bunda zapíná bez tlaku a pohyb není omezený.'),
        ('Jak praní a sušení ovlivňuje chránič?', 'Perte podle štítku, vyjměte vložky a sušte na vzduchu. Teplo z radiátoru nebo slunce může ztvrdit pěnu a snížit její schopnost tlumit.'),
        ('Kdy chránič vyměnit?', 'Po silném nárazu, když je pěna promáčknutá, plast prasklý nebo popruhy poškozené. Bez nehody záleží na používání, ale po několika sezonách pěna obvykle ztrácí pružnost.'),
    ],
)
