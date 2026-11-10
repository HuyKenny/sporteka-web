"""sporteka.cz — wave 24m (5. 11. 2026): long texts for expedicni-stany, fatbike-elektrokola, skialpove-pasy, damska-elektrokola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ expedicni-stany
NEW['expedicni-stany'] = dict(long=True,
    title='Expediční a čtyřsezónní stany: jak vybrat do hor',
    desc='Expediční a čtyřsezónní stany do sněhu, větru a vysokých hor. Konstrukce, tyče, předsíň, kotvení a péče. Porovnejte nabídky českých obchodů.',
    intro='<p>Expediční stan má vydržet věci, které by turistický stan v létě nikdy nepotkaly: nápor větru, těžký mokrý sníh, mráz a několik dní zavření uvnitř při špatném počasí. Proto bývá pevnější, těžší a dražší než běžný model, a proto se vyplatí vybírat ho pečlivěji. Sporteka porovnává nabídky českých obchodů u tunelových, kupolových i geodetických stanů pro dvě až čtyři osoby, včetně lehčích modelů pro zimní túry. Text níže vysvětluje konstrukce, tyče, kotvení i péči, abyste poznali, co opravdu potřebujete.</p>'
          '<p>V kategorii najdete značky ' + B(('husky', 'Husky'), ('trimm', 'Trimm'), ('ferrino', 'Ferrino'), ('jurek', 'Jurek')) +
          '. Pro běžný kemping se hodí spíš <a href="/turisticke-stany/">turistické stany</a>, pro rodiny <a href="/rodinne-stany/">rodinné stany</a>, k vybavení patří <a href="/stanove-doplnky/">stanové doplňky</a>, <a href="/spaci-pytle/">spací pytle</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    guide='<h2>Čím se expediční stan liší od běžného</h2>'
          '<p>Hlavní rozdíl je v tom, na co je konstrukce navržená. Letní stan má především větrat a být lehký. Expediční stan má držet tvar při zatížení, nepropustit vítr a uvnitř udržet použitelný prostor, i když je venku sněhová vánice. K tomu slouží pevnější tyče, nižší profil, více kotvicích bodů a silnější tkanina.</p>'
          + T(['Vlastnost', 'Čtyřsezónní stan', 'Běžný turistický stan'], [
              ['Tyče', 'silnější, často hliníkové, více křížení', 'tenčí, hlavně pro lehkost'],
              ['Profil', 'nižší a aerodynamický', 'vyšší, více vzduchu uvnitř'],
              ['Kotvení', 'mnoho smyček a odtahů', 'základní kolíky v rozích'],
              ['Větrání', 'menší, uzavíratelné průduchy', 'velké průduchy a síťky'],
              ['Sníh a vítr', 'počítá se s nimi', 'na ně není stavěný'],
              ['Hmotnost', 'vyšší', 'nižší']]) +
          '<p>Pojem čtyřsezónní se v marketingu používá volně a není pevně vymezen. Proto se nespoléhejte na samotné označení, ale podívejte se na konstrukci, tyče a popis výrobce. Opravdu horský stan se pozná podle toho, že se dá bezpečně přivázat a že předsíň nenabírá vítr jako plachta.</p>'
          '<h2>Typy konstrukcí</h2>'
          '<ul><li><strong>Tunelový stan:</strong> několik rovnoběžných oblouků za sebou. Nabízí hodně prostoru za nízkou hmotnost, ale musí se postavit proti větru a pořádně napnout.</li>'
          '<li><strong>Kupolový stan:</strong> dvě nebo víc tyčí, které se kříží. Stojí i bez kolíků a lépe snáší vítr z různých směrů.</li>'
          '<li><strong>Geodetický a pologeodetický stan:</strong> víc křížících se tyčí vytváří velmi tuhý rám. Odolá sněhu i silnému větru, bývá těžší a stavba trvá déle.</li>'
          '<li><strong>Tunelový s křížem:</strong> kompromis mezi prostorností a stabilitou, často volba pro dvě až tři osoby.</li></ul>'
          '<p>Tvar rozhoduje také o tom, jak se v stanu sedí. V nízkém stanu se obvykle jen leží, což u dlouhé expedice znamená psychickou zátěž. Pokud počítáte se dny zavřenými uvnitř, volte větší vnitřní výšku nebo prostornou předsíň.</p>'
          '<h2>Tyče a materiály</h2>'
          '<p>Nejdůležitější součástí je tyčový systém. Hliníkové tyče mají dobrý poměr pevnosti a hmotnosti a při ohnutí je lze v nouzi narovnat. Skleněná vlákna jsou levnější a těžší, ve velkém mrazu však křehnou. U expedičních stanů se proto počítá hlavně s hliníkem.</p>'
          '<ul><li><strong>Plášť:</strong> nylon nebo polyester s polyuretanovým či silikonovým povlakem. Silikonový je lehčí a pevný, ale hůř se lepí.</li>'
          '<li><strong>Vnitřní stan:</strong> prodyšný materiál se síťkou nahoře, aby se uvnitř netvořila vlhkost.</li>'
          '<li><strong>Podlážka:</strong> silnější a nepromokavá, zvlášť ve sněhu, kde stan často stojí na mokrém podkladu.</li>'
          '<li><strong>Švy:</strong> zatmelené nebo přelepené, jinak se vlhkost dostane do stanu jejich okolím.</li></ul>'
          '<p>Vodní sloupec je údaj o odolnosti vůči dešti, ne o kvalitě celého stanu. U horských stanů je vedle něj důležitější pevnost tkaniny, odolnost proti roztržení a to, jak se látka chová při mrazu.</p>'
          '<h2>Velikost a počet lidí</h2>'
          '<p>Stany se označují podle počtu míst, ale ta jsou počítána úsporně. Stan pro dva lidi pojme dvě karimatky a nic víc. V zimě si ale berete bundy, boty, batohy a vařič a ty musí někam dát. Proto se u expedic často volí stan o osobu větší, než odpovídá počtu spáčů.</p>'
          '<ul><li><strong>Pro jednoho:</strong> nejlehčí varianta na sólo túry, ale tísnivá při špatném počasí.</li>'
          '<li><strong>Pro dva:</strong> nejčastější volba pro horské výstupy a zimní túry v páru.</li>'
          '<li><strong>Pro tři až čtyři:</strong> pro skupinu nebo dva lidi s velkým vybavením. Těžší a hůř se staví osamoceně.</li></ul>'
          '<p>Vybíráte-li model z nabídky v kategorii, všimněte si názvu: čísla jako 2, 2-3 nebo 3-4 ukazují, kolik lidí do stanu výrobce počítá. Číslo na konci názvu neříká nic o dalším vybavení, které je třeba přidat zvlášť.</p>'
          '<h2>Předsíň, větrání a kondenzace</h2>'
          '<p>Předsíň je v horách vedlejší místnost. V ní se vaří, ukládají boty a batohy a čeká se, než přejde vichřice. Velká předsíň je výhoda, ale také plocha, na kterou fouká vítr. Dobrý model má větrací otvory, které se dají zavřít zevnitř, a vstup, který se otevírá i při sněžení.</p>'
          '<p>Kondenzace je trvalý problém. V malém uzavřeném prostoru se z dechu a vaření sráží vlhkost na stěnách. Proti tomu pomáhají průduchy, dvouvrstvá konstrukce a kontrola tepla: v zimě je lepší stan trochu větrat, než se budit ve zmrzlé vlhkosti. Vaření uvnitř stanu je riziko požáru a otravy oxidem uhelnatým, proto se vždy dbá na dostatečné větrání a vařič se nikdy nenechává bez dozoru.</p>'
          '<h2>Kotvení ve sněhu a ve větru</h2>'
          '<p>Běžné kolíky se ve sněhu neudrží. Sníh potřebuje delší nebo širší kotvy. Jako kotvu lze použít také lyže, hole nebo pytle naplněné sněhem, které se zahrabou do vyhloubeného žlábku a zasypou a udusají. Kotvit je nutné všechna místa, kde stan nabírá vítr, nejen rohy.</p>'
          '<ul><li>Stan stavte zádí proti větru a nízkým koncem do větru.</li>'
          '<li>Použijte všechny odtahy a napněte je rovnoměrně.</li>'
          '<li>Ve sněhu kolíky zahrabte vodorovně a udusejte, ať se sníh pevně spojí.</li>'
          '<li>Nechte místo pro snadné odhrabání vchodu a vnitřní větrání.</li></ul>'
          '<p>Kolíky a odtahy se prodávají zvlášť, najdete je v kategorii <a href="/stanove-kolky/">stanové kolíky</a>. Při vyšším zatížení se vyplatí náhradní lanka a tyčová spojka na opravu.</p>'
          '<h2>Hmotnost a přenos</h2>'
          '<p>Expediční stan je těžší, protože musí být pevný. Přesto se dá hmotnost rozdělit mezi dva lidi: jeden nese vnitřní stan a plášť, druhý tyče a kolíky. U delších výstupů se řeší každý gram, ale nikdy nesmí být úspora na úkor odolnosti. Rozdíl mezi stanem, který stojí, a stanem, který se za noci zlomí, je v horách zásadní.</p>'
          '<p>Při přenosu pomáhá dobře navržený obal s kompresními popruhy. Zabalený stan se vejde do spodní části batohu nebo na jeho vnější stranu. Vybíráte-li nosný systém, podívejte se do kategorie <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Stan je třeba po každé výpravě vysušit, a to i tehdy, když se zdá suchý. Zabalený mokrý stan se začne za pár dní rozkládat, vznikají skvrny a povlak se začne odlupovat. Doma stan rozložte v místnosti s průvanem, zvlášť na švech a v rozích.</p>'
          '<ul><li>Nepoužívejte pračku, stačí vlažná voda a měkký kartáč.</li>'
          '<li>Stan neskladujte natěsno sbalený, ale volně v bavlněném nebo síťovém pytli.</li>'
          '<li>Zipy občas očistěte od písku a promažte přípravkem na zipy.</li>'
          '<li>Tyče zkontrolujte, zda nejsou ohnuté nebo prasklé, a nahraďte opotřebované gumové spojky.</li>'
          '<li>Poškozený plášť opravte lepicí záplatou nebo speciálním tmelem na švy.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Koupě jen podle ceny.</strong> Levný stan s tenkými tyčemi se v horách může zlomit.</li>'
          '<li><strong>Podcenění velikosti.</strong> Po několika dnech uvnitř se ukáže, že místa je málo.</li>'
          '<li><strong>Chybějící zkouška doma.</strong> Poprvé stavět stan až ve sněhu je zbytečné riziko.</li>'
          '<li><strong>Nekontrolované švy a zipy.</strong> Právě tam se po prvním roce objeví problém.</li>'
          '<li><strong>Špatná karimatka.</strong> Do mrazu patří izolační podložka, kterou najdete v kategorii <a href="/karimatky-a-matrace/">karimatky a matrace</a>.</li></ul>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Zimní túry v nižších horách:</strong> lehčí kupolový nebo tunelový stan pro dva s dobrým větráním.</li>'
          '<li><strong>Horské výstupy a vysoké hory:</strong> pevný geodetický stan s hliníkovými tyčemi.</li>'
          '<li><strong>Skupiny a základní tábory:</strong> větší tunelový stan pro tři až čtyři osoby.</li>'
          '<li><strong>Jarní a podzimní túry:</strong> kompromis, kdy stačí lehký stan s pevnějšími tyčemi.</li></ul>'
          '<h2>Co dalšího se hodí</h2>'
          '<p>K expedičnímu stanu patří také izolace od země, spací pytel odpovídající teplotám a vařič se závětřím. Pro zimní podmínky hledejte spacáky v kategorii <a href="/perove-spacaky/">péřové spacáky</a>, vložky v kategorii <a href="/vlozky-do-spacaku/">vložky do spacáků</a>. Pro přípravu jídla slouží <a href="/kempingove-nadobi/">kempingové nádobí</a>. Pokud stan potřebujete spíš na jednodušší kempování, projděte celou nabídku <a href="/stany/">stanů</a>.</p>'
          '<h2>Zkouška před výpravou</h2>'
          '<p>Stan, který jste nikdy nestavěli, patří doma na zahradu, ne poprvé na hřeben. Postavte ho, napněte, zkuste ho zavřít a otevřít zipy a projděte, kam co patří. Zjistíte, kolik času stavba zabere a zda ji zvládnete v rukavicích. Při zkoušce také ověříte, že v balení nic nechybí: kolíky, odtahy, záplaty a opravná spojka na tyče.</p>'
          '<h2>Jak číst nabídky na Sportece</h2>'
          '<p>Stejný stan může mít v různých obchodech jiný název nebo barvu, takže porovnávejte podle modelu a parametrů. Ověřte, zda v ceně je celý stan včetně tyčí, nebo jen plášť. U některých modelů se vnitřní stan prodává zvlášť. Po výběru si před nákupem projděte rozměry a hmotnost uvedené výrobcem.</p>',
    faq=[('Čím se liší expediční stan od turistického?', 'Má pevnější tyče, nižší tvar, více kotvicích bodů a odolnější tkaninu. Je stavěný na vítr, sníh a delší pobyt uvnitř při špatném počasí, proto bývá těžší.'),
         ('Co znamená čtyřsezónní stan?', 'Označení se používá pro stany, které mají zvládnout i zimní podmínky. Nemá pevnou definici, proto posuzujte konstrukci, tyče a popis výrobce, ne jen nálepku.'),
         ('Hodí se expediční stan i do léta?', 'Dá se použít, ale bývá těžší a hůře větraný. V horku se v něm uvnitř může dusit, proto pro letní kemping vyberte lehčí stan s velkými průduchy.'),
         ('Jak velký stan koupit pro dva lidi?', 'Pro expedici je dobré vzít stan o osobu větší, než kolik lidí v něm spí. Zbude místo na batohy, boty a vařič, které v zimě nechcete nechávat venku.'),
         ('Proč se u zimních stanů používají hliníkové tyče?', 'Hliník je pevný, lehký a snáší mráz. Skleněná vlákna ve velké zimě křehnou a snáz se zlomí, proto jsou méně vhodná pro náročné podmínky.'),
         ('Jak kotvit stan ve sněhu?', 'Používejte delší kolíky nebo širší kotvy, zahrabte je vodorovně a udusejte. Můžete využít i lyže, hole nebo pytle naplněné sněhem a kotvit všechny odtahy, ne jen rohy.'),
         ('Lze vařit uvnitř stanu?', 'Je to riziko požáru a otravy oxidem uhelnatým. Pokud nezbývá nic jiného, vařte v předsíni s dobrým větráním a vařič nikdy nenechávejte bez dozoru.'),
         ('Jak zabránit kondenzaci uvnitř stanu?', 'Větrejte průduchy, vyhýbejte se vaření uvnitř a nestavte stan v prohlubni, kde se hromadí vlhkost. Úplně se kondenzaci nevyhnete, ale dá se omezit.'),
         ('Jak stan po výpravě uložit?', 'Důkladně vysušit, očistit od nečistot a uložit volně v prodyšném pytli. Zabalený mokrý stan se rozkládá, vznikají skvrny a povlak se odlupuje.'),
         ('Mohu si stan před koupí vyzkoušet?', 'Většina internetových obchodů ho nechá vrátit v zákonné lhůtě. Doma ho postavte, zkontrolujte tyče, zipy a rozměry a teprve potom vyrazte do hor.')])

# ------------------------------------------------------------------ fatbike-elektrokola
NEW['fatbike-elektrokola'] = dict(long=True,
    title='Fatbike elektrokola: motor, baterie, pláště, výběr',
    desc='Fatbike elektrokola s tlustými plášti pro sníh, písek a terén. Výběr podle motoru, baterie, rámu a legálních parametrů. Porovnejte české obchody.',
    intro='<p>Fatbike elektrokolo spojuje tlusté pláště, které se nepropadají do sněhu a písku, a motor, který pomáhá i s těžší hmotností. Jede stabilně, pohodlně a na rozbitém povrchu se nebojí. Jenže se také liší od běžných e-biků: je těžší, má větší valivý odpor a legální provoz na silnici závisí na parametrech motoru. Sporteka porovnává nabídky českých obchodů u modelů s koly 20 i 26 palců, skládacích i klasických. Níže najdete přehled typů, motorů, baterií, legálních limitů, péče a rad k nákupu, aby výběr nebyl loterie.</p>'
          '<p>V nabídce najdete značky ' + B(('engwe', 'Engwe'), ('hitway', 'Hitway'), ('bodywel', 'Bodywel'), ('evercross', 'Evercross'), ('urlife', 'Urlife'), ('fafrees', 'Fafrees')) +
          '. Příbuzné jsou <a href="/elektrokola/">elektrokola</a>, <a href="/horska-elektrokola/">horská elektrokola</a>, <a href="/skladaci-elektrokola/">skládací elektrokola</a> a <a href="/mestska-elektrokola/">městská elektrokola</a>.</p>',
    guide='<h2>Co je fatbike a proč má tlusté pláště</h2>'
          '<p>Fatbike se vyznačuje pláštěm o šířce zhruba čtyř palců a většího objemu. Nižší tlak vzduchu zvětší stopu, kterou se plášť opírá o povrch, takže se kolo nezaboří do písku, sněhu ani bahna. Pláště také působí jako odpružení, takže model bývá komfortní i bez tlumiče. Cenou je vyšší hmotnost, větší odpor při jízdě po asfaltu a hlučnější chod na pevném povrchu.</p>'
          '<p>Elektrický pohon tuto nevýhodu částečně vyrovnává. Motor pomáhá do kopce i při jízdě po sypkém povrchu, kde by klasický fatbike znamenal velkou námahu. Proto se tyto modely staly oblíbenými u výletníků, rybářů, lovců a lidí, kteří chtějí jezdit po plážích a lesních cestách.</p>'
          '<h2>Typy fatbike elektrokol</h2>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['26palcový fatbike', 'větší kola, klasický rám', 'terén, sníh, delší vyjížďky'],
              ['20palcový fatbike', 'menší kola, kompaktnější rám', 'menší postavy, město, skladnost'],
              ['Skládací fatbike', 'rám se dá složit', 'auto, karavan, byt'],
              ['Step-thru rám', 'nízký nástup bez horní trubky', 'snadný nástup, starší jezdci'],
              ['Odpružený model', 'tlumič vpředu nebo i vzadu', 'rozbité cesty a sjezdy']]) +
          '<p>Velikost kola ovlivňuje chování. Menší kolo je ovladatelnější a nižší, větší kolo lépe přejíždí překážky. U fatbiků se 20 palců vyskytuje častěji než u jiných e-biků, protože tlusté pláště i tak dávají velký průměr.</p>'
          '<h2>Motor a legální parametry</h2>'
          '<p>Důležité je rozlišit, co je v Česku považováno za jízdní kolo. Elektrokolo s pomocným motorem do 250 W, který podporuje šlapání jen do rychlosti 25 km/h, se bere jako kolo a můžete s ním jezdit bez registrace a řidičského oprávnění. Silnější motory nebo vyšší rychlost už znamenají jiný režim, který vyžaduje registraci, pojištění a řidičské oprávnění. U dovážených fatbiků se často objevuje motor 500 W a víc, takže si údaj výrobce přečtěte pozorně.</p>'
          '<ul><li><strong>Výkon motoru:</strong> jmenovitý a špičkový výkon se liší, hledejte hodnotu jmenovitou.</li>'
          '<li><strong>Omezení rychlosti:</strong> podpora musí končit na 25 km/h, jinak jde o jiné vozidlo.</li>'
          '<li><strong>Plynový ovladač:</strong> pokud pohání motor bez šlapání, jde o jinou kategorii. Ověřte pravidla.</li>'
          '<li><strong>Moment motoru:</strong> určuje zrychlení a stoupání, ne legální rychlost.</li></ul>'
          '<p>Pravidla se mohou měnit, proto před koupí ověřte aktuální stav u dopravního úřadu nebo na stránkách ministerstva dopravy. Pro jízdu mimo veřejné komunikace, třeba na soukromém pozemku, platí jiné podmínky než na silnici.</p>'
          '<h2>Baterie a dojezd</h2>'
          '<p>Kapacita baterie se udává ve watthodinách (Wh) nebo v ampérhodinách (Ah) při určitém napětí. Pro porovnání jsou nejpřesnější watthodiny, které vznikají násobením napětí a kapacity. U názvů modelů se objevuje například 48 V a 15 Ah. Čím větší kapacita, tím delší dojezd, ale i vyšší hmotnost.</p>'
          '<ul><li><strong>Tlusté pláště a odpor:</strong> pohlcují energii, proto dojezd na asfaltu klesá víc než u úzkých plášťů.</li>'
          '<li><strong>Sníh a písek:</strong> dojezd se zkracuje, protože motor musí překonávat odpor podkladu.</li>'
          '<li><strong>Zima:</strong> baterie v mrazu ztrácí kapacitu. Vyplatí se uchovávat ji uvnitř a nasazovat těsně před jízdou.</li>'
          '<li><strong>Hmotnost jezdce a nákladu:</strong> těžší zátěž spotřebuje více energie.</li>'
          '<li><strong>Styl jízdy:</strong> nízký stupeň podpory a šlapání dojezd výrazně prodlužuje.</li></ul>'
          '<p>Udávané dojezdy výrobců jsou měřené za ideálních podmínek, takže berte údaj jako horní hranici. Vyjímatelná baterie je výhodou, protože ji lze dobíjet v bytě. Dvě baterie na jednom kole prodlužují trasu, ale zvyšují hmotnost.</p>'
          '<h2>Rám, převody a brzdy</h2>'
          '<p>Rám bývá z hliníku, někdy z oceli. Hliník je lehčí a odolnější proti korozi. Ocel se hůře láme, ale víc váží. U fatbiků hraje roli i šířka vidlice a zadní stavby, aby se do nich vešel široký plášť.</p>'
          '<ul><li><strong>Převody:</strong> řazení s vyšším počtem rychlostí pomůže při stoupání a při jízdě po tvrdém povrchu. Základní sedmirychlostní řazení stačí pro rovinu a lesní cesty.</li>'
          '<li><strong>Brzdy:</strong> kotoučové brzdy jsou při vysoké hmotnosti pomalejší než u lehkých kol. Hydraulické brzdy mají lepší dávkování, mechanické se dají snadno seřídit.</li>'
          '<li><strong>Odpružení:</strong> přední vidlice zmírní otřesy, plné odpružení se hodí do těžšího terénu, ale zvyšuje hmotnost.</li>'
          '<li><strong>Blatníky a nosič:</strong> užitečné při denní jízdě, ve sněhu zabrání rozstřiku.</li></ul>'
          '<p>Díly se dají zkompletovat podle potřeby. Brzdy, řidítka, sedla a pedály najdete v kategoriích <a href="/cyklo-brzdy/">brzdy</a>, <a href="/cyklo-riditka/">řídítka</a>, <a href="/cyklo-sedacky-a-voziky/">sedla a vozíky</a> a <a href="/cyklo-pedaly/">pedály</a>.</p>'
          '<h2>Hmotnost a přeprava</h2>'
          '<p>Fatbike e-bike je těžký, často výrazně víc než běžné elektrokolo. S tím souvisí nakládání do auta, přenos po schodech a jízda na nosiči. Před koupí se podívejte na nosnost nosiče a na maximální hmotnost jezdce a nákladu. Pro přepravu pomocí autonosiče musí být nosič dimenzován na hmotnost kola a širší pláště, viz <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>.</p>'
          '<p>Skládací modely usnadňují skladování a přepravu, ale složený fatbike zůstává objemný a těžký. Pokud ho budete denně vozit nebo nosit, ověřte skutečnou hmotnost výrobcem.</p>'
          '<h2>Pro koho se fatbike elektrokolo hodí</h2>'
          '<ul><li><strong>Výletníci a pohodoví jezdci:</strong> stabilita a komfort jsou důležitější než rychlost.</li>'
          '<li><strong>Zimní cyklisté:</strong> široké pláště zvládnou i rozbředlý sníh a zledovatělé úseky.</li>'
          '<li><strong>Rybáři a myslivci:</strong> projedou po rozbitých polních a lesních cestách k vodě nebo posedu.</li>'
          '<li><strong>Karavanisté a chataři:</strong> skládací model se vejde do zavazadlového prostoru.</li>'
          '<li><strong>Těžší jezdci:</strong> robustnější rám a pláště dávají jistotu.</li></ul>'
          '<p>Naopak pro dlouhé rychlé vyjížďky po silnici se hodí spíš <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel elektrokola</a>, pro každodenní dojíždění <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>.</p>'
          '<h2>Nákup: na co si dát pozor</h2>'
          '<p>Katalog fatbike elektrokol zahrnuje i modely dovážené z mimoevropských továren a prodávané pod nepříliš známými značkami. Samo o sobě to není špatně, ale vyplatí se zjistit si několik věcí předem.</p>'
          '<ul><li><strong>Servis:</strong> kdo kolo opraví a odkud pocházejí náhradní díly, hlavně baterie a řadicí jednotka.</li>'
          '<li><strong>Záruka:</strong> jak dlouhá je a kdo ji poskytuje, včetně záruky na baterii.</li>'
          '<li><strong>Certifikace baterie:</strong> kvalitní výrobce uvádí bezpečnostní certifikaci a doporučené nabíjení.</li>'
          '<li><strong>Parametry:</strong> výkon motoru, rychlost, kapacita a hmotnost mají být uvedeny jednoznačně.</li>'
          '<li><strong>Doručení a sestavení:</strong> kolo často přijde částečně smontované, zkontrolujte brzdy a šrouby.</li></ul>'
          '<h2>Péče o fatbike elektrokolo</h2>'
          '<p>Základní údržba odpovídá klasickému kolu a doplňuje ji péče o elektroniku. Po jízdě v bahnu nebo sněhu kolo opláchněte měkkým proudem vody a nikdy nemiřte tlakovou vodou přímo na motor, displej a konektory. Řetěz promazávejte po každé vlhké jízdě. Viz <a href="/cyklo-udrzba/">údržba kol</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<ul><li><strong>Tlak v plášti:</strong> u tlustých plášťů se pohybuje v nízkých hodnotách a mění se podle povrchu. Na sníh a písek méně, na asfalt více. Řiďte se údajem na boku pláště.</li>'
          '<li><strong>Baterie:</strong> nenechávejte ji dlouho zcela vybitou, v zimě ji skladujte v teple a nabíjejte originální nabíječkou.</li>'
          '<li><strong>Brzdy a řetěz:</strong> při vyšší hmotnosti se opotřebují rychleji, kontrolujte je častěji.</li>'
          '<li><strong>Šrouby:</strong> po prvním týdnu je dotáhněte, protože se nově sestavená kola uvolňují.</li></ul>'
          '<h2>Příslušenství a ochrana</h2>'
          '<p>K fatbiku se hodí kvalitní zámek, světla a helma. Vzhledem k vyšší hmotnosti kola a motoru je helma důležitější než u běžného kola. Najdete je v kategoriích <a href="/cyklo-zamky/">zámky</a>, <a href="/cyklo-svetla/">světla</a> a <a href="/mestske-cyklohelmy/">městské cyklohelmy</a>. Doplňte taky tašky a nosiče z kategorie <a href="/cyklo-tasky-a-nosice/">cyklotašky a nosiče</a>.</p>'
          '<h2>Chování na různých površích</h2>'
          '<p>Při jízdě se vyplatí počítat s tím, že tlusté pláště kolo zpomalují a že se dojezd i chování mění podle podkladu.</p>'
          '<p>Na sněhu se fatbike chová nejlépe tehdy, když je podklad udusaný nebo střední hloubky; v hlubokém sypkém sněhu se zabořuje i široký plášť a jízda se mění v tlačení. Na písku pomáhá nižší tlak a plynulý, rovnoměrný šlapací rytmus. Na bahně a kořenech oceníte nižší tlak v plášti a klidnější řídítka, na asfaltu naopak vyšší tlak a zvolnění, protože plášť hučí a valivý odpor roste. Do kopce je dobré podporu zvyšovat včas, ne až v okamžiku, kdy kolo zpomalí.</p>'
          '<h2>Jak číst nabídky na Sportece</h2>'
          '<p>Stejný model se v různých obchodech objevuje pod odlišnými názvy, často s označením napětí a kapacity baterie. Porovnávejte podle modelu a parametrů, ne podle fotografie. Zkontrolujte, zda je v ceně nabíječka, a ověřte dostupnost v českém nebo evropském skladu, protože doručení z mimoevropského skladu může být delší a komplikovanější při reklamaci.</p>',
    faq=[('Co je fatbike elektrokolo?', 'Elektrokolo s tlustými plášti, obvykle okolo čtyř palců na šířku, které se nepropadá do sněhu, písku ani bláta. Motor pomáhá překonávat odpor širokých plášťů a těžší hmotnost.'),
         ('Smím jezdit na fatbike elektrokole bez registrace?', 'Pokud má motor do 250 W a podpora končí na 25 km/h, považuje se za jízdní kolo. Silnější motory nebo vyšší rychlost vyžadují jiný režim, takže údaje výrobce ověřte.'),
         ('Jaký dojezd mohu čekat?', 'Záleží na kapacitě baterie, povrchu, hmotnosti a podpoře. Ve sněhu, písku a zimě dojezd klesá, takže údaj výrobce berte jako horní hranici a počítejte s rezervou.'),
         ('Proč jsou fatbiky těžší než jiná elektrokola?', 'Mají širší pláště, větší ráfky, robustnější rám a často větší baterii. Kombinace dává stabilitu, ale zvyšuje hmotnost, což ovlivňuje nakládání i přenos.'),
         ('Jaký tlak v plášti použít?', 'Řiďte se údajem na boku pláště. Obecně platí, že na sníh a písek se tlak snižuje, na tvrdý povrch zvyšuje. Příliš nízký tlak zvyšuje odpor a hrozí poškození ráfku.'),
         ('Hodí se fatbike do zimy?', 'Ano, široké pláště mají v sněhu a rozbředlé hlíně lepší záběr. Baterie ale v mrazu ztrácí kapacitu, takže ji uchovávejte v teple a nasazujte těsně před jízdou.'),
         ('Mám volit 20palcový, nebo 26palcový model?', 'Menší kolo je kompaktnější a lépe se skládá a ovládá, větší kolo lépe přejíždí překážky a má plynulejší jízdu. Rozhoduje výška postavy a účel použití.'),
         ('Je skládací fatbike dobrý nápad?', 'Pro karavan, auto nebo byt ano, přibude však spoj, který je nutné pravidelně kontrolovat. I složený model je těžký a objemný, proto ověřte reálnou hmotnost.'),
         ('Na co si dát pozor u levnějších dovozových modelů?', 'Ověřte servis, dostupnost baterie a náhradních dílů, délku záruky a jednoznačné parametry. Zjistěte také, ze kterého skladu se zboží odesílá.'),
         ('Jak pečovat o baterii?', 'Používejte originální nabíječku, neskladujte ji dlouho zcela vybitou a v zimě ji držte v teple. Před delší pauzou ji uložte částečně nabitou na suchém místě.')])

# ------------------------------------------------------------------ skialpove-pasy
NEW['skialpove-pasy'] = dict(long=True,
    title='Skialpové stoupací pásy: mohair, syntetika, lepidlo',
    desc='Stoupací pásy na skialpy, stoupací železa, lepidla a upevnění. Jak vybrat šířku, materiál, lepidlo a pečovat o pásy. Nabídky českých obchodů.',
    intro='<p>Stoupací pásy umožňují skialpovým lyžím vystoupat do svahu: nalepí se na skluznici a vlákna drží proti sklouznutí zpět, a ve směru jízdy kloužou. Kvalita pásů a jejich péče rozhoduje o tom, zda budete stoupat s lehkostí, nebo bojovat s odlepeným pásem v půli výstupu. Sporteka porovnává nabídku pásů, ale také lepidel, stoupacích želez, uchycení a pomůcek pro dolepení. Níže se dozvíte, jak vybrat šířku a materiál, jak pásy lepit, skladovat a kdy je vyměnit, aby stoupání nebylo zbytečně namáhavé.</p>'
          '<p>V nabídce jsou značky ' + B(('pomoca', 'Pomoca'), ('colltex', 'Colltex'), ('nitro', 'Nitro'), ('g3', 'G3'), ('tyrolia', 'Tyrolia'), ('salomon', 'Salomon'), ('wedze', 'Wedze')) +
          '. K pásům patří <a href="/skialpove-lyze/">skialpové lyže</a>, <a href="/skialpove-boty/">skialpové boty</a>, <a href="/skialpove-vazani/">skialpové vázání</a> a širší výběr v <a href="/skialpinismus/">skialpinismu</a>.</p>',
    guide='<h2>Jak stoupací pás funguje</h2>'
          '<p>Pás je pruh textilie s krátkým vlasem, který se přiloží na skluznici lyže. Vlákna leží ve směru od špičky ke konci lyže a při posunu dopředu hladce kloužou. Jakmile lyže začne couvat, vlákna se zapřou do sněhu a zastaví ji. Druhou částí pásu je lepicí vrstva, která drží pás na skluznici a dá se opakovaně odlepit a znovu přilepit. Třetí součástí jsou úchyty na špičce a patě, které pás zajišťují, i když lepidlo ztratí sílu.</p>'
          '<h2>Pásy, které se prodávají</h2>'
          + T(['Druh', 'Popis', 'Pro koho'], [
              ['Hotový pás na konkrétní lyže', 'střižený na rozměr modelu lyží', 'kdo chce pohodlí a přesné lepení'],
              ['Pás z role', 'metráž k ustřižení na míru', 'kdo má více lyží nebo upravuje délku'],
              ['Pásy na splitboard', 'dva samostatné pruhy pro rozdělenou desku', 'splitboardisté'],
              ['Syntetické pásy', 'trvanlivé vlákno, dobrý záběr', 'časté túry a náročné podmínky'],
              ['Mohairové a směsné', 'výborná klouzavost, nižší hmotnost', 'dlouhé túry a lehké stoupání']]) +
          '<p>Pokud vaše lyže jsou běžného modelu, existují pásy střižené právě na ně, jejichž lepení je snadné. U méně obvyklých lyží, širokých desek nebo splitboardů se hodí pás z role nebo sada s upravitelnou šířkou.</p>'
          '<h2>Šířka a délka pásu</h2>'
          '<p>Pás musí pokrýt většinu skluznice, ale nechat po stranách volné hrany. Hrany jsou potřeba při traverzech, tedy při stoupání po svahu napříč, kdy musí lyže zachytit sníh. Pás, který hranu překrývá, smeká a při traverzu nedrží. Příliš úzký pás zase nabízí menší záběr, a hlavně na tvrdém sněhu hůř drží.</p>'
          '<ul><li><strong>Šířka:</strong> volte podle nejširší části lyže, ne podle vázání. Pásy se prodávají v milimetrech.</li>'
          '<li><strong>Délka:</strong> pás má obsáhnout celou délku skluznice nebo jen její část. Kratší pás může trochu zvýšit klouzavost.</li>'
          '<li><strong>Špička a pata:</strong> musí odpovídat tvaru lyže, protože různé lyže mají různé zářezy.</li>'
          '<li><strong>Systém upevnění:</strong> špičkový háček, pata s gumou nebo klip, viz také uchycení Camlock v nabídce.</li></ul>'
          '<h2>Materiály: mohair, syntetika, směs</h2>'
          '<p>Mohair vzniká z vlny angorské kozy. Výborně klouže a je lehký, ale víc nasákne vodou, hůře odolává opotřebení a rychleji se ohladí. Syntetické pásy z nylonu a podobných vláken jsou trvanlivější a víc zabírají, ale kloužou hůř a jsou nepatrně těžší. Směsné pásy kombinují obě vlastnosti.</p>'
          '<ul><li><strong>Mohair:</strong> pro dlouhé túry, kde se šetří síla, a pro zkušené lyžaře, kteří o pásy pečují.</li>'
          '<li><strong>Syntetika:</strong> pro začátečníky, pro častou jízdu a pro místa s ledovými úseky.</li>'
          '<li><strong>Směs:</strong> univerzální volba pro většinu turistických tras.</li></ul>'
          '<p>Hustota vlasu ovlivňuje chování pásu. Hustší vlas lépe drží ve strmém svahu, řidší klouže líp na rovině. Většina značek v popisu uvádí, ke kterému typu túr je pás určen.</p>'
          '<h2>Lepidlo: nejčastější slabé místo</h2>'
          '<p>Dobrý pás s vyschlým lepidlem je k ničemu. Lepidlo se časem opotřebovává, nasákne nečistotami a v mrazu může ztrácet přilnavost. Existují dva základní systémy: pásy s klasickým lepidlem, které můžete po opotřebení znovu natřít z tuby nebo nastříkat, a pásy s pevnější lepicí vrstvou, kterou lze obnovit jen omezeně a podle pokynů výrobce. V kategorii jsou i samostatná lepidla v tubě a sady válečků na rozetření.</p>'
          '<ul><li><strong>Lepení na čistou skluznici:</strong> před lepením skluznici odmastěte a odstraňte zbytky vosku. Nové pásy nelepte na čerstvě navoskovanou lyži.</li>'
          '<li><strong>Doplnění lepidla:</strong> při ztrátě přilnavosti se nanáší nová vrstva dle návodu výrobce.</li>'
          '<li><strong>Zimní skladování:</strong> pásy po túře stáhněte, přilepte k ochranné fólii a uložte v suchu a chladu.</li>'
          '<li><strong>Při stoupání v mrazu:</strong> pásy držte na těle a nasaďte je těsně před nástupem do svahu.</li></ul>'
          '<h2>Stoupací železa</h2>'
          '<p>Stoupací železa, někdy zvaná skialpové hrany nebo harscheisen, se nasazují na vázání a při stoupání po tvrdém, zmrzlém nebo ledovém sněhu přidávají záběr. Pásy samy na ledu nestačí. Železa se vybírají podle šířky lyže a typu vázání. V kategorii najdete železa různých šířek, od užších po široké modely.</p>'
          '<ul><li><strong>Šířka železa:</strong> musí odpovídat šířce lyží pod vázáním, jinak se nemusí správně usadit.</li>'
          '<li><strong>Kompatibilita:</strong> každý výrobce vázání má vlastní uchycení, ověřte slučitelnost.</li>'
          '<li><strong>Hmotnost:</strong> železa jsou těžší než pásy, nosí se v batohu a nasazují jen při potřebě.</li></ul>'
          '<h2>Stoupání bez nehod</h2>'
          '<p>Stoupací pás je jen součástí vybavení. Do lavinového terénu patří také lavinový vyhledávač, sonda a lopata a hlavně znalost lavinového bulletinu. Pásy nemohou nahradit zkušenosti ani vybavení pro záchranu. Pro další výbavu se podívejte do kategorie <a href="/skialpove-boty/">skialpové boty</a>, <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/lyzarske-bryle/">lyžařské brýle</a>.</p>'
          '<h2>Péče o pásy po túře</h2>'
          '<p>Správně ošetřené pásy vydrží výrazně déle. Základem je nenechávat je vlhké ani znečištěné. Po sjezdu pás sundejte, setřete sníh a nechte jej uschnout v pokojové teplotě, ne na topení.</p>'
          '<ul><li>Pás přilepte k ochranné fólii, která zabrání slepení s vlasem sám na sebe.</li>'
          '<li>Neskladujte pásy v teplém autě, kde lepidlo měkne a vlákna se slepují.</li>'
          '<li>Při znečištění lepidla pásy opatrně otřete vlhkou utěrkou a nechte uschnout.</li>'
          '<li>Pásy neperte v pračce, nesuste v sušičce a nežehlete.</li>'
          '<li>Pro delší skladování je uložte volně rozložené v suchém a chladném místě.</li></ul>'
          '<h2>Impregnace a vosk</h2>'
          '<p>Při mokrém sněhu se pásy mohou nasáknout a na vlasu se tvoří hrudky ledu. Impregnace pomáhá odpuzovat vodu a prodlužuje kluzkost, ale nikdy ji nenanášejte na lepicí stranu. Použití těch přípravků se řídí návodem výrobce. Pro údržbu skluznice lyží a vosky se podívejte do kategorie <a href="/lyzarske-vosky/">lyžařské vosky</a>.</p>'
          '<h2>Zastřižení pásu z role krok za krokem</h2>'
          '<p>Pás z role vyžaduje trpělivost, ale výsledek sedí přesně na vaše lyže. Nejprve nalepte pás na čistou skluznici tak, aby přesahoval na obě strany a přes špičku. Potom pomocí ostrého nože nebo speciálního ořezávače vedeného podél hran odřízněte přesahující okraje. Zachovejte rovnoměrný odstup od hran, aby zůstal pruh volné hrany stejně široký po celé délce. Nakonec upravte špičku podle zakřivení lyže a nainstalujte úchyt na špičku a pásek na patu. Prvních několik túr kontrolujte, zda se pás neposouvá.</p>'
          '<h2>Stoupání a technika s pásy</h2>'
          '<p>Pásy dokážou hodně, ale technika stoupání rozhoduje o spotřebě sil. Lyže posouvejte plynule, bez zvedání, aby vlákna klouzala a nezasekávala se. Při strmém svahu dělejte serpentiny a obraty v mírnějším místě. Při traverzu zatěžujte hranu, aby lyže zabrala. Pokud se na pásu tvoří hrudky sněhu, setřete je lopatkou nebo hůlkou a na další túru zvažte impregnaci. U stoupání v teple pomáhá občas přestat a zkontrolovat, zda se pás nezačíná odlepovat po okrajích, než ztratíte celý úchyt.</p>'
          '<h2>Co dělat, když pás selže v terénu</h2>'
          '<p>Odlepený pás nemusí znamenat konec túry. Sundejte ho, osušte skluznici i pás, přitiskněte lepicí vrstvu rukou a přidržte v teple těla. Když nic nepomáhá, připevněte ho pomocí lepicí pásky nebo gumy kolem lyže a pokračujte opatrně, případně zvolte jiný výstup. Doma pak lepidlo obnovte nebo pás vyměňte.</p>'
          '<h2>Příslušenství v kategorii</h2>'
          '<p>Kromě pásů se tu nacházejí i drobnosti, které stojí za pozornost. Ochranné fólie zabrání slepení pásů, sada válečků pomáhá rovnoměrně nanést lepidlo, náhradní špičkové úchyty se hodí při ztrátě nebo poškození. Do batohu patří vždy lepicí páska a náhradní lepidlo, kdyby se pás cestou odlepil. Vybavení ke skialpům doplňte o <a href="/skialpove-vazani/">skialpové vázání</a> s kompatibilními železy.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Pás překrývá hrany.</strong> Lyže pak při traverzu klouže.</li>'
          '<li><strong>Zmrzlé pásy.</strong> Pásy uložené v nevytápěném autě se v mrazu těžko lepí.</li>'
          '<li><strong>Lepení na mokrou skluznici.</strong> Lepidlo nebude držet, skluznice musí být suchá.</li>'
          '<li><strong>Neodstraněný vosk.</strong> Nový pás se z lyže odlepuje, pokud je na ní zbytek vosku.</li>'
          '<li><strong>Neomezené používání.</strong> Opotřebovaný pás se vyplatí vyměnit včas, než se rozpadne uprostřed túry.</li></ul>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Začátečník:</strong> syntetický nebo směsný pás přesně na vaše lyže.</li>'
          '<li><strong>Dlouhé túry:</strong> mohair nebo směs pro lepší klouzavost.</li>'
          '<li><strong>Ledovcové a zledovatělé svahy:</strong> pás se silným záběrem a ověřená stoupací železa.</li>'
          '<li><strong>Splitboard:</strong> pásy určené právě pro rozdělenou desku.</li>'
          '<li><strong>Měníte lyže:</strong> pás z role, který si zastřihnete sami.</li></ul>'
          '<h2>Jak číst nabídky na Sportece</h2>'
          '<p>V nabídce jsou pásy, ale také příslušenství, takže ověřte, co přesně kupujete. U pásů hledejte rozměry v milimetrech a typ (hotový pás, role, splitboard), u železa šířku a kompatibilitu s vázáním. Stejný produkt se může prodávat pod mírně odlišnými názvy. Porovnávejte podle modelu a rozměru.</p>',
    faq=[('Jak vybrat správnou šířku stoupacího pásu?', 'Pás má pokrýt většinu skluznice a nechat po stranách volné hrany. Měřte nejširší místo lyže a vybírejte pás o něco užší. Hrany musí zůstat volné pro záběr při traverzu.'),
         ('Je lepší mohair, nebo syntetika?', 'Mohair lépe klouže a je lehčí, syntetika je odolnější a víc zabírá. Směs je kompromis. Rozhoduje, kolik stoupáte, jak o pásy pečujete a v jakém sněhu.'),
         ('Mám koupit hotový pás, nebo roli?', 'Hotový pás na konkrétní lyže je pohodlnější a přesnější. Role se hodí, pokud máte více lyží nebo nenajdete model přímo pro ně. Vyžaduje přesné zastřižení.'),
         ('Proč mi pás odpadává?', 'Příčinou bývá znečištěné nebo vlhké lepidlo, zbytky vosku na skluznici nebo zmrzlý pás. Pomůže čistá suchá skluznice, odmaštění a případné doplnění lepidla.'),
         ('Jak často je třeba vyměnit pásy?', 'Záleží na četnosti túr a péči. Vyměňte je, když přestane držet lepidlo i po obnovení, nebo když je vlas vyhlazený či potrhaný a stoupání se zhoršuje.'),
         ('K čemu slouží stoupací železa?', 'Přidávají záběr na zmrzlém a tvrdém sněhu, kde pás sám nestačí. Nasazují se na vázání a vybírají se podle šířky lyží a kompatibility s vázáním.'),
         ('Jak uložit pásy po túře?', 'Setřete sníh, nechte je uschnout při pokojové teplotě a přilepte je k ochranné fólii. Uložte v suchu a chladu, ne v teplém autě nebo na topení.'),
         ('Mohu pásy použít na splitboardu?', 'Ano, ale potřebujete pásy určené pro splitboard, které se lepí na dva samostatné pruhy desky. Klasické pásy na lyže se na splitboard většinou nehodí.'),
         ('Jak nalepit pásy na novou lyži?', 'Skluznici očistěte, odmastěte a nechte zcela uschnout. Zbytky vosku odstraňte, protože lepidlo na vosku nedrží. Pak pás pomalu přiložte od špičky a přitlačte.'),
         ('Stačí na túru jen pásy?', 'Ne. Ve strmém lavinovém terénu patří k výbavě také lavinový vyhledávač, sonda a lopata a znalost lavinového bulletinu. Pásy jsou jen jedna část vybavení.')])

# ------------------------------------------------------------------ damska-elektrokola
NEW['damska-elektrokola'] = dict(long=True,
    title='Dámská elektrokola: rám, motor, baterie, výběr',
    desc='Dámská elektrokola s nízkým nástupem, mid i zadním motorem. Jak vybrat rám, velikost, baterii a převody. Porovnejte nabídky českých obchodů.',
    intro='<p>Dámské elektrokolo se od unisex modelu liší hlavně rámem s nízkým nástupem, který usnadňuje nasedání a sesedání, a často také geometrií přizpůsobenou nižším postavám. Nemusí jít o kolo jen pro ženy: nízký rám oceníte při nákupech, s dětskou sedačkou i v pozdějším věku. Sporteka porovnává nabídky českých obchodů u městských, trekingových, skládacích i silničních modelů s nízkým i klasickým rámem. Níže vysvětlujeme rozdíly mezi typy, polohu motoru, velikost rámu, baterii i péči.</p>'
          '<p>V kategorii najdete značky ' + B(('olpran', 'Olpran'), ('ttgo', 'Ttgo'), ('urlife', 'Urlife'), ('pixar', 'Pixar'), ('fafrees', 'Fafrees'), ('van-rysel', 'Van Rysel'), ('insportline', 'Insportline')) +
          '. Příbuzné jsou <a href="/elektrokola/">elektrokola</a>, <a href="/mestska-elektrokola/">městská elektrokola</a>, <a href="/trekingova-elektrokola/">trekingová elektrokola</a>, <a href="/skladaci-elektrokola/">skládací elektrokola</a> a <a href="/damska-kola/">dámská kola</a>.</p>',
    guide='<h2>Co dámské elektrokolo znamená</h2>'
          '<p>Označení dámské se týká především rámu: horní trubka je snížena nebo úplně chybí, takže není třeba zvedat nohu přes příčku. Mnoho výrobců upravuje také velikost rámu, délku představce a řídítka, aby sedly menší postavě. Některé modely používají sedlo s širší zadní částí. Konstrukce motoru a baterie je ale shodná jako u jiných elektrokol.</p>'
          '<p>Důležité je si uvědomit, že nízký rám je kompromis. Je méně tuhý než rám s horní trubkou, a proto se u těžších jezdců nebo vysokého zatížení vyplatí zkontrolovat nosnost a výztuhu rámu. Pro běžné jízdy ve městě i na výletech je ale tuhost naprosto dostatečná.</p>'
          '<h2>Typy dámských elektrokol</h2>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Městské', 'nízký rám, blatníky, nosič, světla', 'každodenní dojíždění a nákupy'],
              ['Trekingové', 'lehčí, širší převody, vyšší dojezd', 'výlety a delší trasy'],
              ['Skládací', 'malá kola, složitelný rám', 'byt, auto, vlak, karavan'],
              ['Silniční a gravel', 'rychlý rám a úzké pláště', 'sportovní jízda po asfaltu'],
              ['S předním košem', 'koš nebo nosič vpředu', 'nákup a drobný náklad'],
              ['Nízký nástup (step-through)', 'zcela nízká horní trubka', 'snadný nástup, sukně, starší jezdci']]) +
          '<p>Většinu nabídky tvoří městské a trekingové modely. Z kategorie se vyskytují i skládací a sportovní kusy, které jsou určeny hlavně pro rychlejší jízdu. Při výběru určete hlavní účel a podle něj pak zvolte typ kola.</p>'
          '<h2>Poloha motoru: střední, zadní, přední</h2>'
          '<p>Motor v ose pedálů, tedy střední, je rozložen blízko těžiště kola a jízda působí nejpřirozeněji. Nabízí citlivější reakci na šlapání, proto je oblíbený u kvalitních městských a trekingových modelů. Zadní motor v náboji je jednodušší a levnější, přidá tlak na zadní kolo, ale kolo se s ním obtížněji rozjíždí do kopce. Přední motor bývá méně častý, mění tah řízení a hodí se spíš pro lehčí provoz.</p>'
          '<ul><li><strong>Střední motor:</strong> přirozená jízda, dobrá rovnováha, vhodný do kopců.</li>'
          '<li><strong>Zadní motor:</strong> jednodušší konstrukce, tichý chod, vhodný na rovinu.</li>'
          '<li><strong>Přední motor:</strong> mění vlastnosti řízení, na kluzkém povrchu méně stabilní.</li></ul>'
          '<p>Legální parametr zůstává stejný: elektrokolo s pomocným motorem do 250 W, který přestává podporovat při 25 km/h, se v Česku považuje za jízdní kolo. Dovážené modely občas mají parametry jiné, proto před koupí ověřte údaje výrobce.</p>'
          '<h2>Baterie a dojezd</h2>'
          '<p>Kapacita baterie se uvádí ve watthodinách nebo v ampérhodinách při daném napětí. Pro porovnání nejlépe poslouží watthodiny. Větší baterie znamená delší dojezd, ale také vyšší hmotnost kola. Důležitá je také poloha baterie: v rámu, na nosiči nebo na sedlové trubce. Baterie v rámu drží těžiště nízko, ale musí se vejít do nízké konstrukce, proto bývá menší.</p>'
          '<ul><li><strong>Vyjímatelná baterie:</strong> dobíjíte ji doma, nemusíte nosit celé kolo.</li>'
          '<li><strong>Zámek baterie:</strong> chrání před odcizením při odstavení.</li>'
          '<li><strong>Dojezd:</strong> klesá s kopci, větrem, hmotností nákladu, nízkou teplotou a vyšší úrovní podpory.</li>'
          '<li><strong>Zimní provoz:</strong> baterie v mrazu ztrácí kapacitu, skladujte ji v teple.</li></ul>'
          '<h2>Velikost rámu a nastavení</h2>'
          '<p>Správná velikost rámu je u elektrokola stejně důležitá jako u běžného. Označení rámu se uvádí v palcích nebo centimetrech a modely značky Olpran uvádějí například velikost 18 palců. Základním vodítkem je výška postavy a délka nohou. Při sezení na sedle by se chodidlo mělo dotknout země špičkami, při šlapání zůstat kolena mírně pokrčená.</p>'
          '<ul><li><strong>Výška sedla:</strong> příliš nízké sedlo zatěžuje kolena, příliš vysoké způsobuje kývání boků.</li>'
          '<li><strong>Vzdálenost k řídítkům:</strong> delší představec natahuje jezdce dopředu, kratší působí uvolněněji.</li>'
          '<li><strong>Výška řídítek:</strong> městské modely mají řídítka výš, aby jezdec seděl vzpřímeně.</li>'
          '<li><strong>Velikost kola:</strong> menší jezdci někdy preferují 26 palců, ostatním vyhovuje 27,5 nebo 28.</li></ul>'
          '<p>Při pochybnostech vyzkoušejte kolo osobně nebo zjistěte, jak funguje vrácení. Příslušenství na ladění pozice, jako sedla nebo řídítka, najdete v kategoriích <a href="/cyklo-sedacky-a-voziky/">sedla a vozíky</a> a <a href="/cyklo-riditka/">řídítka</a>.</p>'
          '<h2>Převody, brzdy a pohodlí</h2>'
          '<p>Převody určují, jak snadno se šlape do kopce. Plynulá náboj­ová převodovka je pohodlná ve městě, protože se dá přeřadit i ve stoje a vyžaduje méně údržby. Přehazovačka s více rychlostmi nabízí širší rozsah a lépe se hodí do kopcovitého terénu. Brzdy by měly být spolehlivé i při vyšší hmotnosti: kotoučové jsou silnější a v mokru lepší, ráfkové jednodušší na údržbu.</p>'
          '<ul><li><strong>Pružná vidlice:</strong> zmírňuje otřesy na dlažbě a nerovných cestách.</li>'
          '<li><strong>Odpružená sedlovka:</strong> zvyšuje komfort bez velkého nárůstu hmotnosti.</li>'
          '<li><strong>Blatníky a kryt řetězu:</strong> chrání oblečení a zjednodušují jízdu v běžných šatech.</li>'
          '<li><strong>Nosič a koš:</strong> usnadní nákup a dopravu zavazadel.</li></ul>'
          '<p>Vybavení pro komfort a bezpečnost najdete v kategoriích <a href="/cyklo-brzdy/">brzdy</a>, <a href="/cyklo-tasky-a-nosice/">cyklotašky a nosiče</a> a <a href="/cyklo-svetla/">světla</a>.</p>'
          '<h2>Hmotnost a skladování</h2>'
          '<p>Elektrokolo je těžší než běžné kolo kvůli motoru a baterii. U dámských modelů je to důležitý parametr: kolo bude třeba nosit po schodech, do sklepa nebo do auta. Zvažte, kde ho budete uchovávat. Pokud máte jen schodiště nebo výtah, preferujte lehčí model nebo skládací provedení.</p>'
          '<ul><li><strong>Bydlení v bytě:</strong> lehčí nebo skládací model s vyjímatelnou baterií.</li>'
          '<li><strong>Garáž nebo kolárna:</strong> těžší model s větším dojezdem není problém.</li>'
          '<li><strong>Převoz autem:</strong> zkontrolujte nosnost nosiče a schopnost vytahovat kolo, viz <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>.</li></ul>'
          '<h2>Pro koho se dámské elektrokolo hodí</h2>'
          '<ul><li><strong>Dojíždějící do práce:</strong> pohodlné kolo bez potu a s košem na věci.</li>'
          '<li><strong>Maminky a rodiny:</strong> stabilní model s nízkým nástupem a možností přepravy dítěte.</li>'
          '<li><strong>Starší jezdkyně:</strong> nízký nástup a pohodlná poloha.</li>'
          '<li><strong>Začátečnice:</strong> pomoc motoru do kopců, bez strachu z únavy.</li>'
          '<li><strong>Sportovně naladěné:</strong> silniční nebo trekingový model pro delší trasy.</li></ul>'
          '<p>Pro srovnání zvažte také <a href="/horska-elektrokola/">horská elektrokola</a> a <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel elektrokola</a>, pokud vás víc láká sport, nebo <a href="/detska-elektrokola/">dětská elektrokola</a> a <a href="/nakladni-elektrokola/">nákladní elektrokola</a> pro jiný účel.</p>'
          '<h2>Bezpečnost a výbava</h2>'
          '<p>Elektrokolo jede rychleji a s menší námahou, takže se hodí kvalitní helma a viditelnost. Povinná je správně seřízená brzda, světla a odrazky. Nejen kvůli zákonu, ale pro vlastní bezpečnost se vyplatí pořídit zámek, který vydrží pokusy o odcizení. Helmy najdete v kategoriích <a href="/mestske-cyklohelmy/">městské cyklohelmy</a> a <a href="/silnicni-cyklohelmy/">silniční cyklohelmy</a>, zámky v kategorii <a href="/cyklo-zamky/">zámky</a>.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Základní údržba odpovídá klasickému kolu a doplňuje ji péče o elektroniku. Po jízdě v dešti kolo otřete, řetěz občas promažte a nikdy nemiřte tlakovou vodou na motor, displej a konektory. Dbejte na správný tlak v pláštích, který je uveden na jejich boku.</p>'
          '<ul><li><strong>Baterie:</strong> nabíjejte originální nabíječkou, neskladujte ji dlouho vybitou ani v mrazu.</li>'
          '<li><strong>Řetěz:</strong> pravidelně čistěte a promazávejte.</li>'
          '<li><strong>Brzdy:</strong> kontrolujte destičky, protože těžší kolo je opotřebovává rychleji.</li>'
          '<li><strong>Servis:</strong> jednou ročně nechte zkontrolovat kolo i elektroniku v servisu.</li></ul>'
          '<p>Nářadí a doplňky najdete v kategoriích <a href="/cyklo-udrzba/">údržba kol</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Výběr podle terénu a trasy</h2>'
          '<p>Pro rovinaté město stačí menší motor a lehčí baterie, pro kopcovitou krajinu se vyplatí silnější motor ve středu a více převodů. Na dlažbě a prašných cestách pomůže širší plášť s větším objemem, protože tlumí otřesy a zlepšuje stabilitu. Pokud často jezdíte po nerovných cestách nebo s nákladem, volte pevnější rám a spolehlivé brzdy. Na dlouhé výlety se hodí větší baterie, ale počítejte i s vyšší hmotností kola při nabíjení a ukládání.</p>'
          '<h2>Úrovně podpory a jízda v praxi</h2>'
          '<p>Většina elektrokol má několik stupňů podpory od jemné po silnou. V rovině a při plynulé jízdě stačí nejnižší stupeň, který udržuje pohodlné tempo, vyšší stupně využijete v kopcích nebo při rozjezdu s nákladem. Plynulý rozjezd je důležitý ve městě: na křižovatce vyberte lehčí převod ještě před zastavením. Jízda s vyšší podporou spotřebuje baterii rychleji, takže na delší trase jí šetřete. Před první delší jízdou si vyzkoušejte brzdění a chování kola s nákladem na bezpečném místě.</p>'
          '<h2>Jak číst nabídky na Sportece</h2>'
          '<p>Stejný model se v různých obchodech objevuje pod odlišnými názvy, často s údaji o velikosti rámu a barvě v názvu. Porovnávejte podle modelu a parametrů, ne jen podle fotografie. Zkontrolujte, zda je v ceně nabíječka, a ověřte rámovou velikost, protože jedna a ta samá barva může být skladem jen v některých velikostech. U levnějších dovozových kusů se vyplatí ověřit servis a záruku na baterii.</p>',
    faq=[('Čím se dámské elektrokolo liší od unisex modelu?', 'Hlavně rámem s nízkým nástupem a často menšími velikostmi rámu. Motor i baterie jsou shodné. Nízký nástup oceníte při nasedání a s nákupem nebo dětskou sedačkou.'),
         ('Je nízký rám méně pevný?', 'Je o něco méně tuhý než rám s horní trubkou, ale pro běžnou jízdu je naprosto dostačující. U těžších jezdců a vysokého zatížení zkontrolujte nosnost, kterou výrobce uvádí.'),
         ('Jaký motor je pro město nejlepší?', 'Střední motor působí nejpřirozeněji a hodí se do kopců, zadní motor je jednodušší a tichý na rovinu. Důležité je, aby výkon motoru odpovídal legálním limitům jízdního kola.'),
         ('Jak velký rám zvolit?', 'Řiďte se výškou postavy a délkou nohou podle tabulky výrobce. Při sezení na sedle by se chodidlo mělo dotýkat země špičkami a při šlapání zůstat koleno mírně pokrčené.'),
         ('Jaká baterie stačí na každodenní dojíždění?', 'Záleží na délce trasy, kopcích, hmotnosti a úrovni podpory. Porovnávejte watthodiny a počítejte s rezervou. Vyjímatelná baterie se dá dobíjet doma nebo v práci.'),
         ('Potřebuji na dámské elektrokolo registraci?', 'Pokud má motor do 250 W a podpora končí při 25 km/h, považuje se za jízdní kolo a registrace není nutná. U dovážených modelů ověřte údaje výrobce.'),
         ('Jak se jede s elektrokolem v zimě?', 'Funguje normálně, ale baterie v mrazu ztrácí kapacitu. Uchovávejte ji v teple a nasazujte těsně před jízdou. Pozor na kluzký povrch a delší brzdnou dráhu.'),
         ('Hodí se skládací elektrokolo jako dámské?', 'Ano, hlavně pro byt, auto nebo vlak. Má menší kola a spoj, který je třeba kontrolovat. I složené kolo je těžší než běžné, takže ověřte reálnou hmotnost.'),
         ('Jaké vybavení k elektrokolu pořídit?', 'Helmu, kvalitní zámek, světla a případně nosič nebo koš. Pro jízdu v běžném oblečení se hodí blatníky a kryt řetězu.'),
         ('Jak pečovat o baterii?', 'Používejte originální nabíječku, neskladujte ji dlouho vybitou ani v mrazu a před delší pauzou ji uložte částečně nabitou na suchém místě.')])
