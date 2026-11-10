"""sporteka.cz — wave 2 extension: longer intros + extra guide sections (brands from the live catalogue on 3. 11. 2026, mistakes, when to buy).
Appended by texty-export.py to the entries of texty_vlna3a.py / texty_vlna3b.py."""
from texty_vlna1x import B

EXTRA = {}

EXTRA['kemping'] = dict(
    intro='<p>Nákup nejlépe rozdělte na dvě části. Nejdřív koupíte „spací systém“ a stan, ty rozhodují o komfortu, a potom doplňky podle toho, co vám při prvním výletě chybělo.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>V kempingu je největší výběr od značek {B(("husky", "Husky"), ("skandika", "Skandika"), ("quechua", "Quechua"), ("yate", "Yate"), ("nils-camp", "Nils Camp"), ("sea-to-summit", "Sea to Summit"), ("naturehike", "Naturehike"), ("petromax", "Petromax"))}. '
          'České a středoevropské značky nabízejí dobrý poměr ceny a výbavy pro víkendové kempování, specializovaní výrobci lehké výbavy jsou dražší, ale ušetří hmotnost na delších trasách.</p>'
          '<h3>Časté chyby začátečníků</h3>'
          '<ul><li>Koupě stanu, který vyzkoušíte až na místě. Rozložte ho doma, ať víte, jak se staví.</li>'
          '<li>Podcenění podložky. Zima často nejde od vzduchu, ale od země.</li>'
          '<li>Příliš těžká výbava na pěší výlet. Každý kilogram navíc se po pár kilometrech násobí.</li>'
          '<li>Zapomenuté drobnosti: kolíky, zapalovač, čelovka a náhradní baterie.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Nejvíc se kempingová výbava prodává na jaře. Slevy bývají na konci léta a na podzim, kdy obchody uvolňují sklady. Sporteka ukazuje aktuální ceny napříč obchody, takže poznáte, jestli je sleva skutečná.</p>',
)

EXTRA['stany'] = dict(
    intro='<p>U každého stanu proto sledujte váhu, kapacitu, vodní sloupec a to, zda se dodává s kolíky. Rozhodnutí usnadňuje filtr značky a ceny.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší nabídku stanů na Sportece mají značky {B(("skandika", "Skandika"), ("husky", "Husky"), ("quechua", "Quechua"), ("jurek", "Jurek"), ("3f-ul-gear", "3F UL Gear"), ("trimm", "Trimm"), ("nils-camp", "Nils Camp"), ("hannah", "Hannah"), ("high-peak", "High Peak"))}. '
          'Pro rodiny jsou zajímavé větší stany s několika ložnicemi, na pěší túry ultralehké modely.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Výběr stanu podle kapacity bez zavazadel. Počítejte raději o jednoho člověka víc.</li>'
          '<li>Stavba bez podložky. Chrání podlážku před kamínky a vlhkem.</li>'
          '<li>Špatně napnutá plachta. Plachta se nesmí dotýkat vnitřního stanu, jinak promokne.</li>'
          '<li>Stavění pod stromy za bouřky, kde hrozí spadlé větve.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Stany bývají nejlevnější na podzim a v zimě, kdy je mimo sezónu. Na jaře a v létě ceny stoupají a rychle se vyprodají oblíbené velikosti.</p>',
)

EXTRA['karimatky-a-matrace'] = dict(
    intro='<p>Při výběru nezapomeňte, že R-hodnota se sčítá. Když na studený podklad položíte dvě podložky, jejich izolace se sečte.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Největší nabídku karimatek a matrací mají značky {B(("yate", "Yate"), ("husky", "Husky"), ("therm-a-rest", "Therm-a-Rest"), ("pinguin", "Pinguin"), ("sea-to-summit", "Sea to Summit"), ("sedco", "Sedco"), ("crossroad", "Crossroad"), ("naturehike", "Naturehike"))}. '
          'Therm-a-Rest a Sea to Summit patří mezi lehké nafukovací modely, české značky nabízejí cenově dostupné pěnové a samonafukovací.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš nafouknutá matrace. Tvrdá podložka se nepřizpůsobí tělu, mírně ji vypusťte.</li>'
          '<li>Nízká R-hodnota na zimu. Studí hlavně zespodu.</li>'
          '<li>Pěnová karimatka bez zadního pytle, která se na batohu poškrábe a promokne.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Slevy bývají na podzim, kdy se uvolňuje zboží z letní sezóny. Zimní izolované matrace jsou nejlevnější na jaře.</p>',
)

EXTRA['turisticke-batohy'] = dict(
    intro='<p>Nejdůležitější je si batoh vyzkoušet naložený. Obchody s kamennou prodejnou nabízejí zátěž a změření zad, online si pomůžete tabulkou výrobce a vyplatí se i vrácení zboží do 14 dnů.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Turistické batohy nabízejí hlavně {B(("deuter", "Deuter"), ("osprey", "Osprey"), ("fjallraven", "Fjällräven"), ("regatta", "Regatta"), ("husky", "Husky"), ("highlander", "Highlander"), ("mfh", "MFH"), ("ferrino", "Ferrino"), ("loap", "Loap"))}. '
          'Deuter a Osprey mají propracované zádové systémy a více velikostí zad, Fjällräven klasický design a odolný materiál, Husky a Loap příznivou cenu.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velký batoh. Co se vejde, to se nosí, a váha pak zbytečně roste.</li>'
          '<li>Špatná velikost zad. Bederní pás pak neleží na kostech a ramena nesou celou váhu.</li>'
          '<li>Nejtěžší věci dole. Zadní část batohu se pak při chůzi houpe.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Batohy bývají nejlevnější po sezóně a při obměně kolekce. Starší barevné verze mají stejné parametry a jsou obvykle výrazně levnější.</p>',
)

EXTRA['outdoor'] = dict(
    intro='<p>Přehled kategorií si projděte shora dolů: batoh, obuv, oblečení, hole a doplňky. U každé zjistíte, na co se při výběru dívat, a porovnáte ceny.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Outdoorovou nabídku vedou značky {B(("deuter", "Deuter"), ("fjallraven", "Fjällräven"), ("osprey", "Osprey"), ("mfh", "MFH"), ("rothco", "Rothco"), ("adidas", "Adidas"), ("nike", "Nike"))}. '
          'Najdete tu klasiku pro turistiku i městský outdoor styl.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Bavlněné oblečení na túru. Nasákne potem a pomalu schne.</li>'
          '<li>Nové boty bez rozchození na dlouhou túru. Puchýře vznikají hlavně na novém páru.</li>'
          '<li>Podceněná voda. Na běžný den počítejte nejméně půl litru na každou hodinu chůze.</li></ul>',
)

EXTRA['kopacky'] = dict(
    intro='<p>Pokud hrajete na různých površích, bude potřeba víc párů. Jedny kopačky na všechno znamenají kompromis, který se projeví při zatáčení nebo při deštivém zápase.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Kopačky na Sportece vedou značky {B(("adidas", "Adidas"), ("puma", "Puma"), ("joma", "Joma"), ("nike", "Nike"), ("mizuno", "Mizuno"), ("skechers", "Skechers"), ("lotto", "Lotto"), ("kipsta", "Kipsta"), ("new-balance", "New Balance"))}. '
          'Adidas, Nike a Puma mají široké řady od základních po špičkové, Joma a Lotto jsou oblíbené u amatérských týmů, Mizuno klade důraz na přírodní kůži.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Lisovky na umělou trávu. Dlouhé kolíky se zaseknou a zatěžují koleno.</li>'
          '<li>Velké kopačky „na vyrůstání“. Dítě v nich ztrácí cit pro míč.</li>'
          '<li>Sušení na topení. Kůže se zdeformuje a lepidlo podrážky povolí.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Slevy se objevují po uvedení nové kolekce, obvykle před sezónou a po jejím skončení. Starší modely mají stejné vlastnosti za nižší cenu.</p>',
)

EXTRA['dresy'] = dict(
    intro='<p>U dresů se vyplatí hlídat sezónu. Dres aktuální sezóny bývá nejdražší, o rok starší verze je obvykle levnější a pro většinu lidí stejně dobrá.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Dresy nabízejí značky {B(("mitchell-ness", "Mitchell & Ness"), ("nike", "Nike"), ("adidas", "Adidas"), ("puma", "Puma"), ("fanatics", "Fanatics"), ("errea", "Errea"), ("force", "Force"), ("silvini", "Silvini"))}. '
          'Mitchell & Ness a Fanatics se zaměřují na retro dresy a americké ligy, Nike, Adidas a Puma na kluby a reprezentace.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Koupě dresu bez kontroly tabulky velikostí. Americké a evropské velikosti se liší.</li>'
          '<li>Prádlo v sušičce, po které se potisk zdeformuje.</li>'
          '<li>Nákup neoficiální kopie, která nemá stejný materiál ani střih.</li></ul>',
)

EXTRA['hokej'] = dict(
    intro='<p>Nejdřív se rozhodněte, jestli kupujete pro dítě, juniora, nebo dospělého. Velikostní řady se liší a model určený pro dospělé dítěti neposlouží.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Hokejové vybavení nabízejí hlavně {B(("bauer", "Bauer"), ("winnwell", "Winnwell"), ("ccm", "CCM"), ("sherwood", "Sherwood"), ("fischer", "Fischer"), ("warrior", "Warrior"))}. '
          'Bauer a CCM mají nejširší nabídku bruslí a hokejek, Winnwell a Sherwood příznivější cenu pro začátečníky a děti.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velké brusle „na vyrůstání“. Noha se v nich pohybuje a hráč se hůř učí.</li>'
          '<li>Nevyměněná čepel nebo páska. Mokrá nebo opotřebovaná čepel vede puk hůř.</li>'
          '<li>Skladování výbavy v zavřené tašce. Pot se nevysuší a chrániče zapáchají.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Nejvíc se prodává před sezónou na přelomu léta a podzimu. Výhodnější ceny bývají na konci zimy a na jaře.</p>',
)

EXTRA['hokejky'] = dict(
    intro='<p>Hokejku si pokud možno vyzkoušejte v ruce. Online porovnání cen vám ukáže, kde je ta samá hokejka levnější a ve kterém obchodě mají vaše provedení skladem.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Hokejky vedou značky {B(("bauer", "Bauer"), ("winnwell", "Winnwell"), ("ccm", "CCM"), ("sherwood", "Sherwood"), ("balling", "Balling"), ("freez", "Freez"), ("fischer", "Fischer"), ("warrior", "Warrior"))}. '
          'Bauer a CCM nabízejí kompozity pro všechny úrovně, Winnwell a Sherwood příznivější dřevěné a základní kompozitové hole.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš tuhá hokejka. Hráč ji neohne a střelba ztrácí sílu i přesnost.</li>'
          '<li>Příliš dlouhá hokejka. Obtížně se s ní vede puk a unavuje záda.</li>'
          '<li>Opomenutí směru čepele. Levá a pravá hokejka nejdou zaměnit.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Hokejky jdou v sezóně na odbyt, nejlépe se kupují mimo ni. Před turnaji a zahájením ligy se vybírají oblíbené řady i velikosti.</p>',
)

EXTRA['kolobezky'] = dict(
    intro='<p>Zkontrolujte maximální nosnost a hmotnost koloběžky. Pro děti jsou důležitější nízká váha a nastavitelná řídítka, aby koloběžka vydržela několik let.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Koloběžky nabízejí značky {B(("micro", "Micro"), ("core", "Core"), ("divine", "Divine"), ("striker", "Striker"), ("urbis", "Urbis"), ("nils-extreme", "Nils Extreme"), ("ethic", "Ethic"), ("slamm", "Slamm"), ("chilli", "Chilli"))}. '
          'Micro je známá dětskými modely s naklápěním, Core a Striker freestyle koloběžkami, Urbis a Chilli městskými.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš malá kola na rozbité chodníky. Nárazy se přenášejí na ruce.</li>'
          '<li>Koloběžka bez brzdy pro dítě, které se rozjíždí z kopce.</li>'
          '<li>Zapomenutá údržba. Šrouby řídítek a ložiska je dobré zkontrolovat každé tři měsíce.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Koloběžky se nejvíc prodávají na jaře. Zajímavé slevy najdete na podzim a po Vánocích, kdy se uvolňují sklady.</p>',
)

EXTRA['elektrokolobezky'] = dict(
    intro='<p>Do rozpočtu počítejte i helmu, zámek a světla. Skutečná cena kompletní výbavy je vyšší než cena samotné koloběžky.</p>',
    guide='<h3>Značky v nabídce</h3>'
          f'<p>Elektrokoloběžky nabízejí značky {B(("eljet", "Eljet"), ("navee", "Navee"), ("iscooter", "iScooter"), ("bluetouch", "Bluetouch"), ("todimart", "Todimart"), ("city-boss", "City Boss"), ("hitway", "Hitway"), ("btwin", "Btwin"))}. '
          'Nabídka se pohybuje od lehkých městských modelů po výkonnější s odpružením, proto porovnávejte hlavně dojezd, hmotnost a záruku.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Spoléhání na maximální dojezd z popisu. Skutečná hodnota je nižší, hlavně v kopcích a v zimě.</li>'
          '<li>Podceněná hmotnost. Pokud ji budete nosit do schodů, vyberte model do 15 kg.</li>'
          '<li>Koupě bez servisu v ČR. U elektrických zařízení se vyplatí oficiální záruka a dostupné náhradní díly.</li></ul>'
          '<h3>Kdy kupovat</h3>'
          '<p>Nejlevnější bývají na podzim a v zimě. Na jaře ceny stoupají a oblíbené modely se vyprodají.</p>',
)
