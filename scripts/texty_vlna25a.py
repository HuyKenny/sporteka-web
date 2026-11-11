"""sporteka.cz — wave 25a (11. 11. 2026): long texts for rotopedy, behaci-pasy, elipticke-trenazery, veslovaci-trenazery.
General true facts only, no prices. Brands verified in the live catalogue sample."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ rotopedy
NEW['rotopedy'] = dict(long=True,
    title='Rotopedy a spinning kola: typy, odpor, setrvačník',
    desc='Rotopedy, spinning kola, air bike i cyklotrenažéry. Jak vybrat typ odporu, setrvačník a nosnost, a porovnat nabídky českých obchodů.',
    intro='<p>Rotoped je nejpřístupnější kardio stroj pro domácí cvičení. Zabere málo místa, nezatěžuje klouby nárazy a jezdit na něm můžete u televize, při práci nebo brzy ráno, když venku prší. Sporteka porovnává nabídky českých obchodů u magnetických a mechanických rotopedů, spinningových kol, vzduchových air bike, lehátkových modelů, dětských rotopedů i cyklotrenažérů pro vlastní kolo.</p>'
          '<p>V nabídce jsou značky ' + B(('hms', 'HMS'), ('insportline', 'Insportline'), ('skandika', 'Skandika'), ('kubisport', 'Kubisport'), ('hop-sport', 'Hop-sport'), ('domyos', 'Domyos'), ('acra-sport', 'ACRA Sport'), ('zipro', 'Zipro')) +
          '. Další kardio stroje najdete v kategorii <a href="/kardio-trenazery/">rotopedy a trenažéry</a>, souvisejícím zařízením se věnují také <a href="/behaci-pasy/">běžecké pásy</a> a <a href="/elipticke-trenazery/">eliptické trenažéry</a>.</p>',
    guide='<h2>Jaké typy rotopedů existují</h2>'
          '<p>Slovem rotoped se v obchodech označuje několik odlišných strojů. Liší se polohou těla, způsobem zatížení i tím, jak moc připomínají jízdu na skutečném kole. Než začnete porovnávat parametry, vyberte nejdřív typ, který odpovídá vašemu cíli.</p>'
          + T(['Typ', 'Princip', 'Hodí se pro'], [
              ['Magnetický rotoped', 'odpor vzniká magnetem u setrvačníku, nastavuje se knoflíkem nebo elektronicky', 'pravidelné cvičení doma, tichý provoz'],
              ['Mechanický rotoped', 'odpor vytváří třecí podložka nebo pásek, nastavuje se šroubem', 'nenáročné rekreační použití'],
              ['Spinning kolo', 'těžký setrvačník, pevný převod, jízda ve stoje i v sedle', 'intervaly, skupinové lekce, trénink připomínající silnici'],
              ['Air bike (vzduchový rotoped)', 'odpor vytváří lopatky větráku a rukojeti zapojují paže', 'intenzivní intervaly, funkční trénink'],
              ['Lehátkový rotoped (recumbent)', 'sedátko se zádovou opěrkou, nohy před tělem', 'zátěž pro záda, rehabilitační a seniorský trénink'],
              ['Mini rotoped', 'pedálová sada bez sedla, položí se na zem nebo pod stůl', 'pohyb u stolu a rozcvička'],
              ['Cyklotrenažér', 'zařízení pro upevnění vlastního kola', 'zimní příprava cyklistů'],
              ['Dětský rotoped', 'nižší rám a menší rozsah nastavení', 'hravé cvičení dětí']]) +
          '<h2>Magnetický, mechanický a elektromagnetický odpor</h2>'
          '<p>Odpor je to, co z rotopedu dělá trénink. U mechanického stroje se na obvod setrvačníku přitlačuje třecí element, který se postupně opotřebovává a při zatížení vydává zvuk. Magnetický rotoped brzdí setrvačník magnety, ke kterým se nic nedotýká, takže je tišší a bez údržby. Elektromagnetický rotoped má brzdu řízenou elektronikou a často obsahuje tréninkové programy, měření výkonu a tepu. Některé modely se dají spárovat s aplikací v telefonu nebo tabletu, takže se ovládají přes Bluetooth.</p>'
          '<p>Pro začátečníka je magnetický rotoped rozumný výchozí bod. Zjednodušeně řečeno nabízí nejlepší poměr mezi klidným chodem a jednoduchostí obsluhy. Mechanická varianta se hodí tam, kde nechcete elektroniku a nevadí vám občas seřídit přítlak.</p>'
          '<h2>Setrvačník, převod a plynulost záběru</h2>'
          '<p>Setrvačník je rotující těleso uvnitř stroje. Čím je těžší, tím plynuleji se šlape, protože po každém šlápnutí si stroj udrží pohyb. Lehký setrvačník se projevuje trhavým záběrem a pocitem, že se pedály při největším zatížení propadají. Výrobci hmotnost uvádějí v kilogramech, ale nejde o jediný ukazatel, protože záleží i na průměru a převodu. Spinning kola s přímým pohonem, kde se pedály točí současně s setrvačníkem, nedovolují volnoběh. To je záměr, protože drží nohy v pohybu a přibližuje jízdu silničnímu kolu.</p>'
          '<p>Pohon je buď řetězový, nebo řemenový. Řemen je tišší a nevyžaduje mazání, řetěz je odolnější proti prokluzu a napodobuje kolo. Při volbě se vyhněte modelům, u kterých si nejste jistí, jak se vyměňuje opotřebovaná část.</p>'
          '<h2>Ergonomie: sedlo, řídítka a nastavení výšky</h2>'
          '<p>Nejčastější důvod, proč lidé rotoped odloží, je nepohodlí. Správně nastavené sedlo má být tak vysoko, aby se při spodní poloze pedálu noha lehce nepřevyšovala v koleni. Sedlo se tedy musí dát posouvat nahoru a dolů, ideálně i dopředu a dozadu. Řídítka by měla jít také zvedat a měnit vzdálenost, jinak se vyšší nebo menší postava zbytečně přetěžuje v zádech a zápěstích. U lehátkového modelu se hlídá nastavení vzdálenosti sedátka od pedálů.</p>'
          '<p>Pomůže vyměnit sedlo za pohodlnější, pokud jde o standardní uchycení. Spinningová kola většinou používají univerzální uchycení, takže se sedlo dá vyměnit za kolářské, a i pedály se dají přizpůsobit.</p>'
          '<h2>Nosnost, rozměry a stabilita</h2>'
          '<p>Maximální hmotnost uživatele je údaj, který se vyplatí brát vážně. Pokud se uživatel k limitu blíží, hledejte robustnější rám s širokou podstavou a vyšší nosností. Kvalitní rotoped stojí pevně i při intenzivním šlapání ve stoje, nekývá se a nevrže. Zkontrolujte také podstavu se stavitelnými nožkami, které vyrovnají nerovnou podlahu. Rozměry stroje porovnejte s volným místem, a nezapomeňte na prostor kolem pro nastupování. Řada modelů se dá sklopit a opřít o zeď.</p>'
          '<h2>Počítač, tep a doplňkové funkce</h2>'
          '<p>Základní displej ukazuje čas, vzdálenost, rychlost a odhad spálených kalorií. Údaj o kaloriích berte jako orientační, protože stroj nezná váš věk, váhu a skutečný výkon. Přesnější je měření tepu hrudním pásem nebo hodinkami. Senzory na rukojetích bývají méně přesné. Zajímavým doplňkem je držák na tablet nebo láhev. Chytrý rotoped s aplikací může cvičení zpestřit, ale jen pokud ho budete opravdu používat, jinak jde o zbytečné navýšení.</p>'
          '<h2>Pro koho který rotoped</h2>'
          '<ul><li><strong>Začátečník a rekreační cvičenec:</strong> magnetický rotoped se stavitelným sedlem, tichý a bez údržby.</li>'
          '<li><strong>Senior nebo cvičení po zranění:</strong> lehátkový model nebo model s nízkým nástupem, vždy po konzultaci s lékařem nebo fyzioterapeutem.</li>'
          '<li><strong>Intervalový trénink:</strong> spinning kolo s těžkým setrvačníkem nebo air bike.</li>'
          '<li><strong>Cyklista:</strong> cyklotrenažér pro vlastní kolo, ověřte uchycení osy a velikost kol.</li>'
          '<li><strong>Kancelář a malý byt:</strong> mini rotoped pod stůl.</li>'
          '<li><strong>Děti:</strong> dětský model s nižším rámem, pouze pod dohledem dospělého.</li></ul>'
          '<h2>Časté chyby při koupi rotopedu</h2>'
          '<ul><li>Výběr podle počtu tréninkových programů místo podle kvality rámu a setrvačníku.</li>'
          '<li>Podcenění hluku, který ve vícepodlažním domě slyší i sousedé.</li>'
          '<li>Zapomenutí na výšku stropu u spinningu, kdy se jezdí ve stoje.</li>'
          '<li>Nákup bez ověření maximální uživatelské hmotnosti a výšky postavy.</li>'
          '<li>Nepoužívání ochranné podložky, která tlumí hluk a chrání podlahu.</li></ul>'
          '<h2>Správný trénink na rotopedu</h2>'
          '<p>Začněte rozcvičkou s lehkým odporem a zvyšujte zátěž postupně. Při šlapání držte záda rovně, ramena uvolněná a kolena směřující dopředu, ne dovnitř. Frekvence otáček okolo 70 až 90 za minutu je pro rekreační jízdu obvyklá, ale vždy se řiďte pocitem a tepem. Po tréninku nechte tělo vychladnout několik minut lehkého šlapání. Pro regeneraci se hodí <a href="/masazni-pomucky/">masážní pomůcky</a>. Chcete-li zvyšovat zátěž systematicky, kombinujte rotoped s <a href="/posilovaci-gumy/">posilovacími gumami</a> a cvičením s vlastní vahou.</p>'
          '<h2>Údržba a životnost</h2>'
          '<p>Rotoped vyžaduje jen málo péče, ale nulová není. Otírejte ho od potu vlhkým hadrem, protože sůl koroduje kov a poškozuje čalounění. Jednou za čas utáhněte šrouby pedálů, sedla a řídítek, které se vibracemi uvolňují. U mechanického přítlaku sledujte opotřebení třecí podložky, u řetězu občas přidejte mazivo. Skladujte ho v suchu, mimo vlhké sklepy. Pod stroj položte <a href="/fitness-pomucky/">fitness podložku</a>, která tlumí vibrace a chrání parkety.</p>'
          '<h2>Jak ušetřit při nákupu rotopedu</h2>'
          '<p>Sporteka zobrazuje nabídky z více českých obchodů, proto stačí otevřít kartu produktu a porovnat prodejce včetně poštovného. U velkých a těžkých strojů se dopravné výrazně liší, a proto ho vždy započítejte. Sledujte také dostupnost náhradních dílů a záruční podmínky. Stejný model se někdy prodává pod několika názvy nebo v několika barvách, takže stojí za to hledat shodné parametry. Když potřebujete cvičit na jiném druhu stroje, podívejte se do kategorie <a href="/fitness/">fitness</a> nebo <a href="/posilovaci-stroje/">posilovací stroje</a>.</p>',
    faq=[
        ('Jaký rotoped vybrat pro začátečníka?', 'Obvykle magnetický rotoped se stavitelným sedlem a řídítky. Je tichý, nevyžaduje údržbu a odpor se nastavuje snadno. Důležitější než počet programů je pevný rám a pohodlné sedlo.'),
        ('Jaký je rozdíl mezi rotopedem a spinning kolem?', 'Spinning kolo má těžký setrvačník a pevný převod, pedály se točí společně s ním, takže nelze šlapat naprázdno. Hodí se na intervaly a jízdu ve stoje. Klasický rotoped bývá pohodlnější a méně náročný.'),
        ('Je lepší magnetický, nebo mechanický rotoped?', 'Magnetický je tišší a bez opotřebení brzdy, proto se pro domácí použití doporučuje častěji. Mechanický je jednodušší, ale vydává více zvuku a třecí část se opotřebovává.'),
        ('Na co se při koupi rotopedu dívat?', 'Na hmotnost setrvačníku, nastavitelnost sedla a řídítek, maximální nosnost, stabilitu a hlučnost. Až potom na displej a doplňkové funkce.'),
        ('Co je air bike a komu se hodí?', 'Je to rotoped, u kterého odpor vytváří větrák. Čím rychleji šlapete, tím větší je odpor. Zapojují se i paže, proto se hodí na náročné intervaly. Pro klidnou jízdu u televize je méně vhodný.'),
        ('Hodí se lehátkový rotoped pro seniory?', 'Často ano, protože má zádovou opěrku a snadný nástup. Před zahájením cvičení je ale rozumné poradit se s lékařem, zejména při srdečních nebo kloubních potížích.'),
        ('Dá se jezdit na rotopedu každý den?', 'Mnoho lidí cvičí denně při nízké zátěži, ale u intenzivního tréninku je vhodné zařazovat dny odpočinku. Řiďte se pocitem a doporučením lékaře nebo trenéra.'),
        ('Jak snížit hluk rotopedu?', 'Pomůže tlumicí podložka, vyrovnání nožek, utažení šroubů a výběr stroje s magnetickou brzdou a řemenovým pohonem.'),
        ('Co je cyklotrenažér a jak se liší od rotopedu?', 'Cyklotrenažér nemá vlastní rám. Upevníte do něj své jízdní kolo, a trénujete tak na stejné geometrii, na jakou jste zvyklí. Rotoped je kompletní samostatný stroj.'),
        ('Kolik místa rotoped zabere?', 'Standardní model potřebuje půdorys zhruba jako dětská postýlka, ale k tomu je potřeba rezerva pro nastupování. Přesné rozměry najdete v popisu produktu, mnoho modelů je navíc skládacích.'),
    ])

# ------------------------------------------------------------------ behaci-pasy
NEW['behaci-pasy'] = dict(long=True,
    title='Běžecké a chodicí pásy: motor, plocha, sklon, skládání',
    desc='Elektrické i mechanické běžecké pásy a walking pady. Jak vybrat motor, délku plochy, sklon a tlumení, a porovnat nabídky českých obchodů.',
    intro='<p>Běžecký pás umožňuje běhat nebo svižně chodit bez ohledu na počasí, tmu i rozvrh. Tempo a sklon nastavíte přesně, takže trénink je dobře opakovatelný a snadno měřitelný. Sporteka porovnává nabídky českých obchodů u elektrických pásů s motorem, odpružených i skládacích modelů, úzkých chodicích pásů walking pad pod stůl a také mechanických pásů bez motoru, které ženete vlastním krokem.</p>'
          '<p>V nabídce najdete například značky ' + B(('hms', 'HMS'), ('citysports', 'Citysports'), ('kubisport', 'Kubisport'), ('master', 'Master'), ('lifefit', 'Lifefit'), ('insportline', 'Insportline'), ('hop-sport', 'Hop-sport'), ('thunder', 'Thunder')) +
          '. Další stroje najdete v kategorii <a href="/kardio-trenazery/">rotopedy a trenažéry</a>, kromě toho se podívejte na <a href="/rotopedy/">rotopedy</a> nebo <a href="/elipticke-trenazery/">eliptické trenažéry</a>.</p>',
    guide='<h2>Jak vybrat běžecký pás</h2>'
          '<p>Rozhodující je odpověď na jednoduchou otázku: budete především chodit, nebo běhat? Pás na chůzi může mít kratší plochu a slabší motor, běžecký stroj musí zvládnout nárazy kroku, vyšší rychlost i delší trénink. Podle toho se výrazně liší rozměry, hmotnost i konstrukce.</p>'
          + T(['Typ pásu', 'Charakteristika', 'Hodí se pro'], [
              ['Walking pad', 'úzká plocha, nízká maximální rychlost, často bez madel', 'chůze při práci, regenerace, malé byty'],
              ['Chodicí pás se sklonem a madly', 'delší plocha, ruční nebo elektrický sklon', 'svižná chůze, seniorský a rehabilitační pohyb'],
              ['Elektrický běžecký pás', 'silnější motor, delší plocha, tlumení', 'pravidelný běh doma'],
              ['Skládací pás', 'plocha se sklopí nahoru', 'malé prostory'],
              ['Mechanický pás', 'bez motoru, pohyb pásu vytváří chodidla', 'doplňkový pohyb, nenáročné použití'],
              ['Pás pro děti', 'menší rozměry a nižší rychlost', 'hravé používání pod dohledem'],
              ['Příslušenství', 'ochranná podložka, mazivo na pás', 'ochrana podlahy a prodloužení životnosti']]) +
          '<h2>Délka a šířka běžecké plochy</h2>'
          '<p>Plocha, po které běžíte, určuje pohodlí a bezpečnost. Při běhu se krok prodlužuje, proto potřebuje vyšší člověk a rychlejší běžec delší plochu. Rozumný základ pro chůzi bývá kratší pás, na běh se hledají modely s plochou, na které se při plném kroku nemusíte bát, že šlápnete za okraj. Šířka má stejný význam: na úzkém pásu se hůř udržuje stopa. Pokud chcete jen chodit, úzký pás stačí, při běhu je širší pohodlnější. Výrobci uvádějí rozměry v centimetrech, a proto je porovnávejte přímo.</p>'
          '<h2>Motor: trvalý a špičkový výkon</h2>'
          '<p>Motor v pásu pohání válec, který tahá běžeckou plochu. Údaj o výkonu uvádí obchodník často jako špičkový, tedy krátkodobě dosažitelný. Důležitější je trvalý výkon, který motor zvládne dlouhodobě. Čím těžší uživatel a čím vyšší rychlost, tím víc výkonu potřebujete. Slabý motor se přehřívá, zpomaluje se při došlápnutí a rychle se opotřebovává. Pás s nedostatečným motorem poznáte i podle toho, že se při běhu cukavě rozjíždí.</p>'
          '<p>Rozumné je dívat se i na rozsah rychlosti a zrychlení. Pro chůzi stačí nižší maximum, na běh a intervaly potřebujete rezervu nad tempem, které běžně držíte.</p>'
          '<h2>Sklon: ruční, elektrický a obousměrný</h2>'
          '<p>Sklon simuluje stoupání a zvyšuje zátěž bez toho, že byste museli běžet rychleji. Levnější pásy mají ruční nastavení: sklon se mění pomocí pružiny nebo čepu ještě před cvičením a za běhu ho změnit nelze. Elektrický sklon se ovládá tlačítky na panelu a umožňuje intervaly s různým stoupáním. Některé modely nabízejí také negativní sklon, který připomíná běh z kopce. Pro dlouhodobé používání je elektrický sklon pohodlnější. Pro začátečníka na chůzi nebo lehký běh by ruční sklon měl stačit.</p>'
          '<h2>Tlumení a ochrana kloubů</h2>'
          '<p>Běh na pásu bývá šetrnější než běh po asfaltu, protože deska pod pásem je odpružená nebo vybavená elastickými prvky. Dobrá soustava tlumení zmírňuje dopad v oblasti kotníků a kolen. Příliš měkká plocha ale může být nestabilní a ztěžuje odraz. Ideální je kompromis, který si vyzkoušíte u kamaráda nebo v posilovně. K tomu přispívá správná obuv, takže ji nepodceňujte: vhodné <a href="/bezecka-obuv/">běžecké boty</a> se hodí i do interiéru.</p>'
          '<h2>Skládání a skladování</h2>'
          '<p>Skládací pás se zvedne do svislé polohy a zabere výrazně méně místa. Mechanika by měla být opatřena pístem nebo pružinou, aby se plocha zvedla bez námahy a nespadla. Zkontrolujte rozměry po složení, protože výška stroje se může s přidaným panelem blížit výšce dveří. Pás s kolečky se snáz přesouvá. Walking pady se skládají na plocho nebo se zasunou pod postel či gauč, což je u nich hlavní výhoda.</p>'
          '<h2>Panel, programy a připojení</h2>'
          '<p>Základní displej ukazuje rychlost, čas, vzdálenost a odhad energetického výdeje. Programy automaticky mění tempo a sklon podle předvoleného profilu, což zpestří trénink. Měření tepu z madel bývá orientační, přesnější je pás s hrudním snímačem. Některé stroje se připojují přes Bluetooth k aplikacím, jiné mají držák na telefon nebo tablet. Důležitý je bezpečnostní klíč: po vytažení stroj okamžitě zastaví a při pádu může zabránit úrazu.</p>'
          '<h2>Pro koho který pás</h2>'
          '<ul><li><strong>Chůze při práci:</strong> walking pad nebo pás s nízkou rychlostí a tichým motorem.</li>'
          '<li><strong>Začínající běžec:</strong> elektrický pás s delší plochou, odpružením a ručním sklonem.</li>'
          '<li><strong>Pravidelný běžec:</strong> širší plocha, silnější motor a elektrický sklon.</li>'
          '<li><strong>Senior nebo rehabilitace:</strong> pás s madly a nízkým nástupem po konzultaci s lékařem.</li>'
          '<li><strong>Malý byt:</strong> skládací model nebo walking pad.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Spoléhání na špičkový výkon motoru místo trvalého.</li>'
          '<li>Podcenění hluku, který se šíří podlahou do bytu pod vámi.</li>'
          '<li>Koupě pásu, jehož plocha je pro vaši postavu příliš krátká.</li>'
          '<li>Opomenutí výšky stropu při zvýšení sklonu a rozměrů po rozložení.</li>'
          '<li>Pořízení bez ochranné podložky, která tlumí vibrace a chrání parkety.</li></ul>'
          '<h2>Péče o běžecký pás a jeho životnost</h2>'
          '<p>Většina potíží vzniká ze zanedbané údržby. Pás je třeba udržovat čistý, protože prach a nečistoty zvyšují tření a zatěžují motor. Pod pásem se podle návodu občas aplikuje silikonové mazivo, někdy je plocha opatřena materiálem, který mazání nevyžaduje. Kontrolujte vystředění pásu: když se při běhu sunuje na jednu stranu, upravte ho imbusovými šrouby na zadním válci. Po tréninku ho otřete od potu a odpojte ze sítě. Pod pás patří <a href="/fitness-pomucky/">fitness podložka</a>, která tlumí vibrace.</p>'
          '<h2>Bezpečnost na běžeckém pásu</h2>'
          '<p>Nastupujte vždy při nízké rychlosti, rozjeďte pás a teprve potom na něj vstupte. Bezpečnostní klíč připevněte na oblečení. Nedívejte se dlouho dolů a nesnažte se na pásu telefonovat při vyšší rychlosti. Dětem i domácím zvířatům zabraňte v přístupu, a pokud pás nepoužíváte, vytáhněte klíč. Před zahájením pravidelného běhání se při zdravotních potížích poraďte s lékařem.</p>'
          '<h2>Jak ušetřit při nákupu</h2>'
          '<p>Porovnávejte prodejce přímo na kartě produktu a započítejte dopravu, protože pás je těžký a objemný. Zjistěte, zda je v ceně montáž nebo zda jde o rozložené zboží. Sledujte záruku na motor a plochu, protože jde o nejdražší díly. Hledáte-li alternativu pro nižší zátěž kloubů, zvažte <a href="/rotopedy/">rotoped</a>, případně <a href="/veslovaci-trenazery/">veslovací trenažér</a>. Výbavu ke cvičení najdete v kategorii <a href="/fitness/">fitness</a>.</p>',
    faq=[
        ('Jaký běžecký pás vybrat do bytu?', 'Skládací model s tichým motorem a odpruženou plochou, případně walking pad pod postel. Změřte prostor po složení i při provozu a zjistěte maximální uživatelskou hmotnost.'),
        ('Jaký je rozdíl mezi běžeckým pásem a walking padem?', 'Walking pad má úzkou plochu, nižší rychlost a obvykle bez madel, je určený na chůzi. Běžecký pás má delší a širší plochu, silnější motor a vyšší rychlost.'),
        ('Na co se u motoru běžeckého pásu dívat?', 'Na trvalý výkon, nikoli špičkový. Čím těžší uživatel a vyšší tempo, tím víc rezervy potřebujete. Slabý motor se přehřívá a rychle opotřebovává.'),
        ('Jak dlouhá má být běžecká plocha?', 'Pro chůzi stačí kratší, na běh potřebujete delší a širší, aby se krok nezkracoval. Vyšší a rychlejší běžci by měli hledat delší plochu.'),
        ('Je lepší ruční, nebo elektrický sklon?', 'Elektrický sklon se mění za běhu a hodí se na intervaly. Ruční je jednodušší a stačí pro lehký trénink nebo chůzi.'),
        ('Je běh na pásu šetrnější ke kloubům než venku?', 'Odpružená plocha dopad mírně zmírňuje, ale záleží na obuvi, technice a tempu. Při bolestech kloubů se poraďte s lékařem nebo fyzioterapeutem.'),
        ('Jak často mazat běžecký pás?', 'Podle návodu výrobce. Některé pásy mazivo vyžadují, jiné ne. Pravidelně kontrolujte čistotu a vystředění pásu.'),
        ('Pomůže pás pod stůl při sedavé práci?', 'Chůze během dne zvyšuje pohyb, ale nenahradí cílený trénink. Zvolte tichý walking pad a pomalé tempo, aby nebyla ohrožena soustředěnost.'),
        ('Je potřeba pod běžecký pás podložka?', 'Doporučuje se. Tlumí vibrace a hluk, chrání podlahu a usnadňuje úklid prachu, který se pod strojem hromadí.'),
        ('Jak pás zabezpečit před dětmi?', 'Vytáhněte po cvičení bezpečnostní klíč, odpojte stroj ze sítě a skládací pás sklopte do svislé polohy.'),
    ])

# ------------------------------------------------------------------ elipticke-trenazery
NEW['elipticke-trenazery'] = dict(long=True,
    title='Eliptické trenažéry: odpor, délka kroku, setrvačník',
    desc='Magnetické, mechanické i elektromagnetické eliptické trenažéry a crosstrainery. Jak vybrat délku kroku a setrvačník a porovnat české obchody.',
    intro='<p>Eliptický trenažér, říká se mu také crosstrainer, spojuje pohyb nohou jako při chůzi a běhu s prací paží. Chodidla se nezvedají z pedálů, a proto stroj nezatěžuje klouby nárazy, což je oblíbená výhoda pro domácí cvičení. Sporteka porovnává nabídky českých obchodů u mechanických, magnetických a elektromagnetických modelů, úsporných mini trenažérů pod stůl i větších strojů s dlouhým krokem a těžkým setrvačníkem.</p>'
          '<p>V nabídce jsou značky ' + B(('hms', 'HMS'), ('hop-sport', 'Hop-sport'), ('zipro', 'Zipro'), ('skandika', 'Skandika'), ('insportline', 'Insportline'), ('horizon-fitness', 'Horizon Fitness'), ('master', 'Master'), ('kettler', 'Kettler')) +
          '. Pro širší výběr kardio strojů navštivte <a href="/kardio-trenazery/">rotopedy a trenažéry</a>, porovnejte také <a href="/rotopedy/">rotopedy</a> nebo <a href="/behaci-pasy/">běžecké pásy</a>.</p>',
    guide='<h2>Jak eliptický trenažér funguje</h2>'
          '<p>Pedály se pohybují po eliptické dráze a madla se kývou souběžně s nimi. Tělo se přirozeně vyrovnává, nohy kopírují kroky a ruce přenášejí část práce. Protože chodidlo nespadne na podložku, nevznikají nárazy, které znáte z běhu. Zapojuje se hlavně spodní polovina těla, ale pohyblivá madla přidávají práci paží, ramen a zad. Stroj lze obvykle používat i dozadu, což mírně změní zaměření zátěže.</p>'
          '<h2>Typy odporu</h2>'
          + T(['Typ', 'Princip', 'Poznámka'], [
              ['Mechanický', 'třecí pásek nebo podložka u setrvačníku', 'jednoduchý a levnější, hlučnější a opotřebovává se'],
              ['Magnetický', 'magnety brzdí setrvačník bez dotyku', 'tichý a bez údržby, nejběžnější volba'],
              ['Elektromagnetický', 'elektronika řídí brzdu, programy a měření výkonu', 'komfortní, potřebuje napájení nebo generátor'],
              ['Vzduchový (air)', 'větrák zvyšuje odpor s rychlostí', 'vhodný na intervaly, může být hlučný'],
              ['Mini trenažér', 'pouze pedálová sestava', 'pod stůl, k rehabilitaci a lehkému pohybu'],
              ['Samonapájecí', 'bez zásuvky, displej napájí generátor', 'zvýhodní umístění bez dosahu zásuvky']]) +
          '<h2>Setrvačník a plynulost chodu</h2>'
          '<p>Pro eliptický trenažér platí totéž co pro rotoped: těžší setrvačník vede k plynulejšímu a tišímu chodu. Lehký se projevuje cuknutím při změně směru pedálu. Hmotnost uvádí výrobce v kilogramech a platí, že u kvalitnějších strojů je setrvačník výrazně těžší než u základních modelů. Důležité je i umístění: setrvačník vpředu nebo vzadu mění geometrii pohybu a velikost stroje, proto se vyplatí porovnat, kam budou při šlapání směřovat kolena.</p>'
          '<h2>Délka kroku a ergonomie</h2>'
          '<p>Délka kroku je vzdálenost, kterou pedál urazí při jednom cyklu. Příliš krátký krok je nepřirozený a unavuje kolena, delší dává pocit plynulé chůze. Nižší postavy vystačí s kratším krokem, vyšší hledají stroj s delším. Pohodlí zvyšují i široké pedály s protiskluzem, vhodný rozsah madel a bezpečný nástup. Pokud stroj umožňuje měnit sklon nebo délku, lépe se přizpůsobí různým uživatelům v domácnosti.</p>'
          '<h2>Madla, displej a tréninkové funkce</h2>'
          '<p>Pevná madla slouží jako opora, pohyblivá zapojují paže. Dobré je mít obojí. Na displeji sledujete čas, vzdálenost, rychlost a odhad energetického výdeje, který je orientační. Měření tepu z madel není tak přesné jako z hrudního pásu. Chytré modely se spojují s aplikací, mají tréninkové programy a nastavení odporu na dálku. Zvažte, zda to opravdu využijete. Pro mnohé lidi je důležitější tichý chod než dvacet programů.</p>'
          '<h2>Nosnost, stabilita a rozměry</h2>'
          '<p>Eliptický trenažér je delší než rotoped a vyžaduje i prostor pro pohyb paží. Změřte délku i šířku stroje a ověřte výšku stropu, protože při chůzi se tělo zvedá. Maximální hmotnost uživatele je důležitý parametr: při jeho blízkosti vybírejte robustní rám a širokou podstavu. Stabilní stroj stojí pevně a nehoupe se do stran. Stavitelné nožky vyrovnají nerovnou podlahu. Pro bytové použití se hodí modely s kolečky, které se dají odsunout ke zdi.</p>'
          '<h2>Pro koho je eliptický trenažér</h2>'
          '<ul><li><strong>Kdo chce šetrný kardio trénink:</strong> bez nárazů, a proto oblíbený u lidí, kteří se nechtějí zatěžovat během. Při potížích s klouby se poraďte s lékařem.</li>'
          '<li><strong>Domácnost se sdíleným strojem:</strong> model s nastavitelným krokem a tichou magnetickou brzdou.</li>'
          '<li><strong>Celotělový trénink:</strong> stroj s pohyblivými madly.</li>'
          '<li><strong>Kancelář a rehabilitace:</strong> mini trenažér pod stůl.</li>'
          '<li><strong>Intervaly:</strong> elektromagnetický nebo vzduchový stroj s vyšším rozsahem odporu.</li></ul>'
          '<h2>Eliptický trenažér, rotoped, nebo běžecký pás</h2>'
          '<p>Jde o tři různé způsoby, jak trénovat vytrvalost. Rotoped je nejtišší a zabere nejméně místa, pás nejlépe napodobuje přirozený běh a chůzi, eliptický trenažér nabízí plynulý pohyb celého těla bez dopadů. Rozhodněte podle toho, co vás baví a kolik máte místa. Pokud nejste jistí, začněte rotopedem nebo si stroje vyzkoušejte v posilovně. Další alternativu najdete v kategorii <a href="/veslovaci-trenazery/">veslovací trenažéry</a>, která zapojuje záda a paže ještě výrazněji.</p>'
          '<h2>Správná technika a trénink</h2>'
          '<p>Stůjte vzpřímeně, hlavu držte v prodloužení páteře a nenaklánějte se na madla. Chodidla držte celá na pedálech a pohybu využívejte celé nohy. Začněte lehkým odporem a trénink prodlužujte postupně. Při tréninku je vhodné měnit směr a zátěž. Po cvičení protáhněte lýtka a stehna, případně využijte <a href="/masazni-pomucky/">masážní pomůcky</a>. Nezapomeňte pít a mít pohodlné <a href="/treninkova-obuv/">tréninkové boty</a> s pevnou podrážkou.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš lehký setrvačník a z něj vyplývající trhaný chod.</li>'
          '<li>Podcenění délky kroku pro vyšší postavy.</li>'
          '<li>Neověření nosnosti a stability stroje.</li>'
          '<li>Opírání celé váhy o madla místo práce nohama.</li>'
          '<li>Chybějící podložka pod strojem, která tlumí hluk a vibrace.</li></ul>'
          '<h2>Údržba a životnost</h2>'
          '<p>Eliptický trenažér má více pohyblivých dílů než rotoped, a proto je důležité čas od času zkontrolovat pevnost šroubů v kloubech ramen a pedálů. Otírejte stroj od potu a skladujte v suchu. Ložiska a pohyblivé části podle návodu občas promažte. Pokud se při chodu objeví klepání, příčinou bývá uvolněný šroub nebo opotřebované pouzdro. Řada výrobců nabízí náhradní díly, takže před nákupem zjistěte, zda je zajištěn servis.</p>'
          '<h2>Jak ušetřit při nákupu</h2>'
          '<p>Na kartě produktu porovnáte více českých obchodů a zjistíte, který má zboží skladem a za jakých podmínek doručí. Započítejte dopravu, protože jde o objemné a těžké balení. Sledujte i záruku a dostupnost dílů. Pokud se cvičením teprve rozkoukáváte, můžete začít levnějším magnetickým modelem a později přejít na kvalitnější stroj. Související vybavení najdete v kategoriích <a href="/fitness/">fitness</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>.</p>',
    faq=[
        ('Co je eliptický trenažér?', 'Je to kardio stroj s pedály pohybujícími se po eliptické dráze a s madly pro ruce. Napodobuje chůzi a běh bez nárazů, protože chodidla zůstávají na pedálech.'),
        ('Je lepší magnetický, nebo mechanický eliptický trenažér?', 'Magnetický je tišší a bez údržby brzdy. Mechanický je jednodušší, ale hlučnější a opotřebovává se. Pro domácí použití se obvykle volí magnetický.'),
        ('Jaká má být délka kroku?', 'Pro vyšší postavu delší, pro nižší stačí kratší. Příliš krátký krok je nepřirozený a unavuje kolena, proto se vyplatí zkontrolovat parametry u produktu.'),
        ('Jaký setrvačník je dobrý?', 'Těžší znamená plynulejší a tišší chod. Lehký setrvačník se projevuje trhavým pohybem, zvlášť při vyšším odporu.'),
        ('Jak se eliptický trenažér liší od rotopedu?', 'U rotopedu sedíte a pohybujete nohama, u eliptického trenažéru stojíte a do pohybu zapojujete i paže. Eliptický stroj je delší a zabere víc místa.'),
        ('Hodí se eliptický trenažér při bolesti kloubů?', 'Protože nemá nárazy, bývá pro klouby šetrnější než běh. Před zahájením cvičení se při zdravotních potížích poraďte s lékařem nebo fyzioterapeutem.'),
        ('Dá se šlapat opačným směrem?', 'U většiny strojů ano. Změní se zaměření zátěže na svaly, ale pohyb vyžaduje cvik a opatrnost.'),
        ('Je vhodný mini eliptický trenažér?', 'Pro lehký pohyb u stolu nebo rehabilitaci ano. Plnohodnotný trénink celého těla s ním nezískáte, protože nemá madla a velký krok.'),
        ('Jak se starat o eliptický trenažér?', 'Otírat od potu, kontrolovat utažení šroubů, občas promazat pohyblivé části podle návodu a skladovat v suchu.'),
        ('Jak dlouho cvičit?', 'Začátečník může začít krátkými úseky, třeba deseti minutami, a postupně zvyšovat. Tempo upravte podle kondice a doporučení lékaře.'),
    ])

# ------------------------------------------------------------------ veslovaci-trenazery
NEW['veslovaci-trenazery'] = dict(long=True,
    title='Veslovací trenažéry: typy odporu, kolejnice, sedlo',
    desc='Veslovací trenažéry a rowery: magnetické, vzduchové, vodní i dřevěné. Jak vybrat odpor, délku kolejnice a nosnost a porovnat české obchody.',
    intro='<p>Veslovací trenažér napodobuje pohyb veslaře a zapojuje nohy, záda, paže i střed těla v jednom plynulém tahu. Je to jeden z nejkomplexnějších kardio strojů pro domácí cvičení. Sporteka porovnává nabídky českých obchodů u magnetických, vzduchových, vodních i hydraulických veslovacích trenažérů, skládacích modelů do bytu a také strojů s dřevěným rámem, které se hodí do obývacího pokoje.</p>'
          '<p>V nabídce jsou značky ' + B(('skandika', 'Skandika'), ('insportline', 'Insportline'), ('hop-sport', 'Hop-sport'), ('kubisport', 'Kubisport'), ('merach', 'Merach'), ('domyos', 'Domyos'), ('virtufit', 'Virtufit'), ('tunturi', 'Tunturi')) +
          '. Další stroje najdete v kategorii <a href="/kardio-trenazery/">rotopedy a trenažéry</a>, porovnejte také <a href="/rotopedy/">rotopedy</a>, <a href="/behaci-pasy/">běžecké pásy</a> a <a href="/elipticke-trenazery/">eliptické trenažéry</a>.</p>',
    guide='<h2>Jak veslovací trenažér funguje</h2>'
          '<p>Sedíte na pojízdném sedátku, nohy opřete o podnožky a oběma rukama táhnete držadlo k tělu. Pohyb má čtyři fáze: nástup s pokrčenými koleny, odraz nohama, náklon trupu a tah paží, potom návrat do výchozí polohy. Odpor vzniká v setrvačníku, vodní nádrži, magnetu nebo pístu, podle typu stroje. Správná technika rozděluje práci mezi nohy, záda a paže přibližně v tomto pořadí, tedy začíná se nohama.</p>'
          '<h2>Typy odporu veslovacích trenažérů</h2>'
          + T(['Typ', 'Princip', 'Charakteristika'], [
              ['Magnetický', 'magnet brzdí setrvačník, odpor se nastavuje v úrovních', 'tichý chod, vhodný do bytu'],
              ['Vzduchový', 'lopatky větráku, odpor roste s rychlostí tahu', 'přirozený pocit, vyšší hluk'],
              ['Vodní', 'lopatky se otáčejí v nádrži s vodou', 'plynulý tah, příjemný zvuk, těžší stroj'],
              ['Hydraulický', 'písty zadržují pohyb ramen', 'kompaktní a levnější, méně přirozený pohyb'],
              ['Elektromagnetický', 'elektronika řídí zátěž a programy', 'komfortní měření a aplikace'],
              ['Samonapájecí', 'displej bez zásuvky', 'umístění bez ohledu na síť'],
              ['Dětský', 'menší rozměry a nižší odpor', 'hravé cvičení pod dohledem']]) +
          '<h2>Který odpor zvolit</h2>'
          '<p>Magnetický veslovací trenažér je tichý a snadno se obsluhuje, odpor nastavujete otočným knoflíkem nebo elektronicky. Pro většinu domácností je rozumná volba. Vzduchový a vodní stroj reagují na sílu tahu: čím víc zabereš, tím víc se brzdí. Pocit blíží skutečnému veslování, ale vzduchový stroj dělá hluk srovnatelný s větrákem a vodní vyžaduje plnění nádrže. Hydraulické modely jsou kompaktní, jenže pohyb paží je omezený a při delším tréninku méně plynulý.</p>'
          '<h2>Kolejnice, sedlo a podnožky</h2>'
          '<p>Kolejnice určuje, jak dlouhý pohyb můžete provést. Vyšší postava potřebuje delší dráhu, jinak se tah zkracuje a ztrácí účinek. Sedátko má jezdit tiše a plynule po kolejnici, a pokud možno být dostatečně vysoké, aby se pohodlně vstávalo. Podnožky se stavitelnými popruhy drží chodidlo při tahu. Ergonomické tvarování sedla ocení při delším cvičení. Důležitá je i konstrukce kolejnice: pevná, rovná a bez vůle, jinak sedátko drhne.</p>'
          '<h2>Rám: ocel, hliník a dřevo</h2>'
          '<p>Ocelový rám je odolný a obvykle těžší, hliníkový lehčí a přenosný. Dřevěné rowery jsou také velmi oblíbené: vypadají jako nábytek, často bývají tišší a můžete je mít v obývacím pokoji. Ať zvolíte jakýkoli materiál, hledejte pevné svary nebo spoje a stabilní podstavu. Veslování vyvolává dynamické tahy a stroj se nesmí viklat. Pro malé prostory vyberte model, který se po cvičení složí a postaví na výšku.</p>'
          '<h2>Rozměry, skládání a skladování</h2>'
          '<p>Veslovací trenažér je delší než ostatní kardio stroje, takže rozměry určitě změřte. Délka v rozloženém stavu se pohybuje v řádu dvou metrů. Skládací model sklopí kolejnici nebo se zdvihne do svislé polohy, zabírá výrazně méně místa a hodí se do malého bytu. Pro dřevěné modely platí, že se obvykle stavějí na výšku. Kolečka usnadňují přesun. Zeptejte se také na hmotnost stroje, aby ho zvládl přenést dospělý.</p>'
          '<h2>Displej, tep a připojení</h2>'
          '<p>Displej obvykle ukazuje čas, počet záběrů, tempo, vzdálenost a odhad energetického výdeje. Pro veslování je užitečné sledovat tempo na vteřinu a počet záběrů za minutu. Měření tepu je přesnější s hrudním pásem. Některé stroje se připojují k aplikacím přes Bluetooth a nabízejí lekce nebo závody. Jde o příjemný doplněk, ale nevolte stroj jen kvůli aplikaci, pokud ho nezvládne po mechanické stránce.</p>'
          '<h2>Pro koho je veslovací trenažér</h2>'
          '<ul><li><strong>Celotělový kardio trénink:</strong> zapojuje nohy, záda, paže a střed těla v jednom pohybu.</li>'
          '<li><strong>Kdo se nechce zatěžovat během:</strong> pohyb probíhá vsedě a bez dopadů.</li>'
          '<li><strong>Kdo hledá nenápadný stroj:</strong> dřevěný nebo skládací model do obýváku.</li>'
          '<li><strong>Pokročilí:</strong> vzduchový nebo vodní stroj s měřením výkonu.</li>'
          '<li><strong>Děti a mladiství:</strong> pouze pod dohledem dospělého a s menším strojem.</li></ul>'
          '<p>Při problémech se zády, rameny nebo koleny se před zahájením tréninku poraďte s lékařem či fyzioterapeutem. Technika má zásadní význam a špatně provedený pohyb může zatížit bederní páteř.</p>'
          '<h2>Správná technika veslování</h2>'
          '<p>Začněte nohama: z předklonu s koleny pokrčenými zatlačte do podnožek, potom se zakloňte do mírného záklonu a nakonec přitáhněte držadlo k hrudi. Návrat probíhá v opačném pořadí: nejdřív natáhněte paže, pak se předkloňte a nakonec pokrčte kolena. Záda držte rovná, ramena uvolněná a hlavu v prodloužení páteře. Nezakulacujte hrudník a netrhejte držadlem. Začínejte nižším odporem a soustřeďte se na plynulý rytmus.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Tah pouze pažemi a ztráta síly nohou.</li>'
          '<li>Zakulacená záda při návratu do předklonu.</li>'
          '<li>Příliš vysoký odpor ještě před nácvikem techniky.</li>'
          '<li>Podcenění délky kolejnice u vyšší postavy.</li>'
          '<li>Koupě bez změření prostoru a bez promyšleného skladování.</li></ul>'
          '<h2>Péče a životnost</h2>'
          '<p>Kolejnici otírejte od prachu, aby sedátko klouzalo bez drhnutí. Pokud výrobce předepisuje mazání, použijte doporučený prostředek. U vodního stroje se podle návodu používá čistá voda a doplňují se čisticí tablety, aby se nezkazila, a nádrž se vypouští před delším skladováním. Šrouby se čas od času dotahují a držadlo i lanko se kontrolují, zda nejsou odřené. Stroj skladujte v suchu. Pod něj patří <a href="/fitness-pomucky/">fitness podložka</a>, která tlumí hluk.</p>'
          '<h2>Jak ušetřit při nákupu</h2>'
          '<p>Porovnejte prodejce na kartě produktu a započítejte dopravu, protože balení je dlouhé a těžké. Zjistěte, zda je stroj dodán smontovaný, a sledujte záruku. Podobné stroje se někdy prodávají pod několika názvy, proto porovnávejte parametry. Pokud váháte nad celotělovým strojem, zvažte i <a href="/posilovaci-stroje/">posilovací stroje</a> nebo doplňte trénink o <a href="/posilovaci-gumy/">posilovací gumy</a>. Širší výběr výbavy najdete v kategorii <a href="/fitness/">fitness</a>.</p>',
    faq=[
        ('Jaký veslovací trenažér vybrat do bytu?', 'Magnetický skládací model s tichým chodem, nebo dřevěný stroj, který se postaví na výšku. Změřte délku a ověřte maximální nosnost.'),
        ('Který odpor je nejlepší?', 'Pro domácí cvičení se nejčastěji volí magnetický, protože je tichý a dobře ovladatelný. Vzduchový a vodní stroj nabízejí přirozenější pocit, ale vyžadují víc místa a bývají hlasitější.'),
        ('Zapojuje veslování jen paže?', 'Ne. Většinu práce vykonávají nohy, potom záda a nakonec paže. Správná technika rozděluje zátěž na celé tělo.'),
        ('Jak dlouhá má být kolejnice?', 'Taková, aby se vyšší postava mohla úplně natáhnout i předklonit. Kratší dráha omezuje záběr a zkresluje trénink.'),
        ('Je veslovací trenažér vhodný pro záda?', 'Při správné technice může být příjemným pohybem, ale při potížích s páteří se vždy poraďte s lékařem nebo fyzioterapeutem. Špatná technika může záda zatížit.'),
        ('Kolik místa trenažér zabere?', 'V rozloženém stavu je dlouhý okolo dvou metrů. Skládací a dřevěné modely se dají postavit na výšku, což ušetří místo.'),
        ('Jak se starat o vodní veslovací trenažér?', 'Používat čistou vodu, podle návodu doplňovat čisticí tablety a před delším skladováním nádrž vypustit.'),
        ('Jaký je rozdíl mezi veslovacím trenažérem a veslovacím strojem?', 'Slovo stroj se často používá pro posilovací zařízení s deskami, například model s kotouči. Trenažér je obvykle kardio zařízení s odporem a displejem.'),
        ('Hodí se veslování pro začátečníky?', 'Ano, pokud se naučí správnou techniku a začne s nižším odporem a krátkými úseky. Při zdravotních potížích se vždy poraďte s lékařem.'),
        ('Je trenažér hlučný?', 'Záleží na typu. Magnetický a dřevěný model je tichý, vzduchový vydává šum větráku a vodní plynulé zurčení.'),
    ])

# ------------------------------------------------------------------ doplnění (intro + další oddíly)
NEW['rotopedy']['intro'] += '<p>Na této stránce najdete průvodce, který vysvětluje rozdíly mezi typy rotopedů a pomůže vám vybrat stroj podle prostoru, postavy i cíle.</p>'
NEW['rotopedy']['guide'] += (
    '<h2>Rotoped v malém bytě</h2>'
    '<p>Kdo bydlí v panelovém bytě, řeší hlavně hluk a místo. Magnetický stroj s řemenovým pohonem je nejtišší možnost. Pod kola nebo nožky se hodí gumová podložka, která zachytí vibrace, a při šlapání v noci pomůže také jemnější odpor. Skládací rotoped s vertikálním uložením se vejde do skříně nebo za dveře. Pokud neustále hledáte místo, zvažte mini rotoped, který se po cvičení schová pod gauč.</p>'
    '<h2>Jak často a jak dlouho jezdit</h2>'
    '<p>Pro začátek stačí krátké jízdy ve snadném tempu, třeba třikrát týdně, a postupně se prodlužují. Důležitější než jednorázový výkon je pravidelnost. Tempo se dá střídat: několik minut svižnějšího šlapání a potom odpočinek při lehkém odporu. Doporučení k dávkování zátěže ale vždy konzultujte s lékařem nebo trenérem, zejména při srdečních či kloubních potížích.</p>')

NEW['behaci-pasy']['intro'] += '<p>Průvodce níže popisuje parametry, kterým se vyplatí věnovat pozornost, a upozorňuje na chyby, které kupující dělají nejčastěji.</p>'
NEW['behaci-pasy']['guide'] += (
    '<h2>Pás pod stolem a chůze při práci</h2>'
    '<p>Úzký chodicí pás se v posledních letech používá i v kancelářích a pracovnách. Rychlost chůze při psaní na počítači bývá nízká, a proto stačí tichý motor a jednoduchý panel s dálkovým ovladačem. Při koupi sledujte rozsah rychlosti, hlučnost, nosnost a možnost složení pod nábytek. Pás s madly se pro práci nehodí, protože zabere místo. Nezapomeňte, že chůze při práci vyžaduje chvíli zvyku, takže začněte krátkými úseky.</p>'
    '<h2>Příprava místnosti</h2>'
    '<p>Před dodávkou zvolte místo s rovnou podlahou a zásuvkou v dosahu bez prodlužovacího kabelu. Za pásem nechte volný prostor, aby případný pád nebyl nebezpečný, a vedle něj prostor na nastupování. Větrání místnosti zlepší komfort, protože při běhu se hodně potíte. Zvažte také ventilátor a držák na láhev. Pokud se pás stěhuje, vytáhněte kabel a nepřevracejte stroj bez návodu.</p>'
    '<h2>Mechanický pás bez motoru</h2>'
    '<p>Mechanický pás nepotřebuje zásuvku, protože ho pohánějí vaše kroky. Je jednodušší a levnější na provoz, ale pohyb je méně plynulý než u motorového stroje. Hodí se pro chůzi nebo lehké tempo, pro vážný běh je méně vhodný. Výhodou je ticho a nezávislost na elektřině.</p>')

NEW['elipticke-trenazery']['intro'] += '<p>Následující průvodce vysvětluje typy odporu, délku kroku a další parametry, aby výběr stroje nebyl pouze loterií.</p>'
NEW['elipticke-trenazery']['guide'] += (
    '<h2>Délka kroku podle výšky postavy</h2>'
    '<p>Výrobci udávají délku kroku v centimetrech. Při kroku kratším, než je přirozená chůze, stroj připomíná šlapání na místě a unavuje kolena. U nižších osob nebo dětí tato otázka tolik nevadí, u vyššího uživatele je rozhodující. Pokud ve vaší domácnosti cvičí lidé různého vzrůstu, hledejte stroj s delším krokem, který je pohodlnější pro všechny. Při váhání si stroj zkuste v prodejně a pamatujte, že u eliptických trenažérů s nastavitelným krokem se pohodlí zvyšuje.</p>'
    '<h2>Mini eliptický trenažér pod stůl</h2>'
    '<p>Mini model je pouze pedálová sestava s odporem, položená na zemi. Hodí se pro kancelář, rehabilitaci nebo seniory a hravé zapojení do pohybu při sledování televize. Nenahradí plnohodnotný stroj, ale zabere nepatrné místo a váží málo. Při koupi sledujte protiskluzovou podložku, pevnost pedálů a možnost nastavit odpor. Důležité je, aby se pod stolem nehýbal po podlaze.</p>'
    '<h2>Cvičení a oblečení</h2>'
    '<p>Při cvičení na eliptickém trenažéru se hodí lehké <a href="/funkcni-tricka/">funkční tričko</a> a <a href="/leginy/">legíny</a> nebo kraťasy, které nebrání v pohybu. Obuv volte s pevnou podrážkou, aby chodidlo na pedálu nesjíždělo. Při delším tréninku se vyplatí ručník a láhev s vodou, protože se potíte víc, než byste čekali.</p>')

NEW['veslovaci-trenazery']['intro'] += '<p>Průvodce níže popisuje jednotlivé typy odporu, správnou techniku i chyby, kterým se při prvním nákupu stroje vyhnete.</p>'
NEW['veslovaci-trenazery']['guide'] += (
    '<h2>Vodní, vzduchový, nebo magnetický</h2>'
    '<p>Při rozhodování pomůže si představit, kde bude stroj stát. V ložnici nebo bytě v paneláku hrozí zvuk větráku u vzduchového stroje, zatímco magnetický zůstává tichý. Vodní model je příjemný na pohled i poslech, jenže je těžší a potřebuje přísun vody. Jestli vám záleží hlavně na pohodlném tréninku v klidu, zvolte magnetický stroj. Když chcete co nejpřirozenější tah, rozhodněte se pro vodní nebo vzduchový.</p>'
    '<h2>Intervaly a vytrvalost na veslovacím stroji</h2>'
    '<p>Veslovací trenažér se hodí jak na dlouhé rovnoměrné tempo, tak na intervaly. Začátečník může střídat několik minut klidného veslování s krátkou pauzou. Pokročilý používá tempo na vteřinu jako orientaci a drží stálý rytmus. Dbejte na rozcvičení, zejména zad, ramen a nohou, a na protažení po cvičení. K regeneraci se hodí <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>'
    '<h2>Kde stroj umístit</h2>'
    '<p>Veslovací trenažér potřebuje rovnou podlahu a prostor za sedátkem i před držadlem. Při tahu se paže pohybují široce, a proto nechte volné místo po stranách. Pokud stroj stojí na parketách, podložte ho, aby nepoškrábal podlahu. Při skladování na výšku zkontrolujte pojistku, aby se kolejnice nerozevřela.</p>')

# ------------------------------------------------------------------ doplnění 2
NEW['behaci-pasy']['guide'] += (
    '<h2>Rychlost, zrychlení a intervaly</h2>'
    '<p>Rozsah rychlosti určuje, kolik prostoru máte pro růst. Rekreační běžec nepotřebuje nejvyšší maximum, ale oceníte plynulé zvyšování po malých krocích. Rychlá tlačítka s předvolenými hodnotami usnadňují intervaly: stisknete tlačítko a pás sám zrychlí na dohodnuté tempo. Zkontrolujte také, jak rychle stroj zastaví, protože prudké brzdění je nepříjemné.</p>')

NEW['elipticke-trenazery']['guide'] += (
    '<h2>Jak poznat kvalitní stroj</h2>'
    '<p>Kvalitní eliptický trenažér poznáte už při prvním použití. Chod je plynulý bez cukání, pedály nemají vůli, madla se nekývají a rám se při tahu nehýbe. Šrouby jsou zajištěné a kryty pohyblivých částí dobře drží. U levnějších strojů se vůle objeví po několika měsících, proto se vyplatí číst zkušenosti dalších kupujících a sledovat délku záruky. Výrobce by měl uvádět jasné parametry: nosnost, hmotnost setrvačníku, délku kroku a počet úrovní odporu.</p>'
    '<h2>Počet úrovní odporu</h2>'
    '<p>Úrovně odporu se pohybují od několika po desítky. Samotné číslo o kvalitě nevypovídá. Důležité je, aby nejnižší úroveň byla opravdu lehká pro zahřátí a nejvyšší dostatečně náročná, abyste i po měsících tréninku měli kam růst. Plynulé přechody mezi úrovněmi jsou lepší než skokové. Při elektronickém ovládání se úroveň mění tlačítkem a při magnetickém knoflíkem.</p>'
    '<h2>Umístění a zapojení</h2>'
    '<p>Stroj postavte na pevnou rovnou podlahu a zkontrolujte, zda nehoupe. Pokud používáte napájení ze sítě, nepřetahujte kabel přes místo, kudy chodíte. Samonapájecí modely se obejdou bez zásuvky, ale displej se rozsvítí až po rozšlapání. Za strojem nechte prostor pro bezpečný sestup.</p>')

NEW['veslovaci-trenazery']['guide'] += (
    '<h2>Jak poznat kvalitní veslovací trenažér</h2>'
    '<p>Kvalitní stroj poznáte podle toho, že sedátko jezdí tiše a bez drhnutí, držadlo se plynule vrací a rám se při tahu nekývá. Podnožky jsou pevné a popruh dobře drží. Kolejnice nemá žádný průhyb ani spáry. Důležité je i značení nosnosti a uvedení délky kolejnice v popisu. Nejistí kupující by měli číst zkušenosti dalších uživatelů a ověřit podmínky záruky a servisu.</p>'
    '<h2>Počet úrovní odporu a nastavení</h2>'
    '<p>U magnetických modelů se odpor mění v úrovních, jejichž počet se u modelů liší. Pro domácí trénink stačí pár úrovní, které se citelně liší. U vzduchových a vodních strojů se odpor reguluje otevřením klapky nebo množstvím vody a silou tahu. Pamatujte, že vyšší odpor neznamená lepší trénink: pokud se zhorší technika, pomalu odpor snižte.</p>'
    '<h2>Veslování a oblečení</h2>'
    '<p>Při cvičení se hodí pružné oblečení, které nebrání v pohybu kolen a ramen, například <a href="/leginy/">legíny</a> nebo <a href="/sportovni-kratasy/">kraťasy</a>. Boty mohou být lehké tréninkové, protože se chodidlo upíná do podnožek. Rukavice nejsou nutné, ale při delších trénincích chrání dlaně před mozoly.</p>')
