"""sporteka.cz — facet landing texts wave 141: detska-elektrokolobezka, lyzarske-bryle-uvex, mizuno-bezecke-boty, nike-dresy.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detska-elektrokolobezka
NEW['detska-elektrokolobezka'] = dict(
    title='Dětská elektrokoloběžka: jak vybrat bezpečný model',
    desc='Dětská elektrokoloběžka: jaký výkon, rychlost a nosnost zvolit podle věku a výšky dítěte, na co dát pozor u brzd, helmy i baterie. Porovnání obchodů.',
    intro='<p>Dětská elektrokoloběžka je jiný stroj než zmenšená verze dospělého modelu. Má slabší motor, nižší nejvyšší rychlost, nižší nášlapnou desku a často řidítka, která lze přizpůsobit růstu. Dítě na ní nezíská sílu, ale pohodlí: při rozjezdu mu pomůže motor, takže se nemusí odrážet nohou. '
          'Tahle stránka zužuje kategorii <a href="/elektrokolobezky/">elektrokoloběžky</a> na modely označené jako dětské, tedy ty, které výrobce staví pro školáky zhruba od šesti do dvanácti let. Průvodce vysvětluje, jak podle výšky a váhy určit vhodnou velikost, jaké parametry jsou u dětí důležitější než výkon, jak řešit brzdy, osvětlení a ochranné pomůcky a kdy je lepší začít obyčejnou <a href="/detska-kolobezka/">dětskou koloběžkou</a>. Nabídky českých obchodů u každého modelu porovnáte na jednom místě.</p>',
    guide='<h2>Od kolika let a pro jak velké dítě</h2>'
          '<p>Výrobci uvádějí doporučený věk, ale spolehlivější je dívat se na výšku a hmotnost dítěte a na to, jak jistě už jezdí na běžné koloběžce. Dítě, které se neumí samo rozjet, zabrzdit a zatočit bez pádu, na elektrickém modelu nic nezlepší. Motor jen rychleji vytvoří situaci, kterou dítě nezvládne. Jako zkouška slouží běžná koloběžka: pokud na ní jezdí plynule a klidně, může přejít na elektrickou.</p>'
          + T(['Věk', 'Orientační výška', 'Na co se zaměřit'], [
              ['6–7 let', 'zhruba 115–130 cm', 'nízká hmotnost, nízká nášlapná deska, nízký strop rychlosti, brzda dosažitelná malou rukou'],
              ['8–10 let', 'zhruba 130–145 cm', 'nastavitelná řidítka, kvalitnější brzdy, větší kola, lepší dojezd'],
              ['11–12 let', 'zhruba 145–160 cm', 'delší deska, nosnost s rezervou, zvažte už model pro mladistvé']]) +
          '<p>Údaje v tabulce jsou jen orientační, děti stejného věku se výškou liší i o patnáct centimetrů. Důležité je, aby při stání na desce zůstala ramena uvolněná a ruce držely řidítka zhruba ve výšce pasu. Pokud musí dítě tahat paže nahoru nebo se kvůli nízkému řidítku hrbit, jízda unavuje a ztrácí jistotu.</p>'
          '<h2>Výkon, rychlost a nosnost</h2>'
          '<p>U dětské elektrokoloběžky je rozumný nižší motor. Slabší motor se plynule rozjíždí a při chybě odpustí víc než silný. Dětské modely v nabídce mívají maximální rychlost zhruba od deseti do dvaceti kilometrů v hodině, a u části z nich ji lze v nastavení omezit, aby rodič přizpůsobil stroj tomu, jak dítě jezdí. Takové omezení hledejte v popisu produktu, protože se liší model od modelu. Nosnost nechte s rezervou: koloběžka postavená na hranici zatížení vyžaduje rychlejší opotřebení kol i brzd.</p>'
          '<ul><li><strong>Nižší výkon motoru:</strong> pro děti stačí střed rozumných hodnot, vysoký výkon znamená prudší rozjezd a delší brzdnou dráhu.</li>'
          '<li><strong>Režimy rychlosti:</strong> vypínatelné stupně, kdy se nejprve nastaví nejpomalejší, jsou praktický pojistný ventil.</li>'
          '<li><strong>Pozvolný rozjezd:</strong> motor, který se zapíná až po odrazu nohou, je bezpečnější než ten, který reaguje na plyn okamžitě.</li>'
          '<li><strong>Nosnost:</strong> dítě roste, vyberte model, který zvládne i pozdější váhu, jinak ho za rok budete měnit.</li></ul>'
          '<h2>Brzdy, kola a tlumení</h2>'
          '<p>Brzdění je důležitější než rozjezd. Spolehlivé dětské modely mívají zadní kotoučovou nebo bubnovou brzdu, často doplněnou elektronickou brzdou na motoru a šlapací brzdou přes zadní blatník. Elektronická brzda sama o sobě obvykle bývá slabší, takže se nespoléhejte jen na ni. Zkontrolujte, zda páčka dosáhne i malá ruka a zda se dá sevřít bez velké síly. Dětem vyhovuje páčka s menším rozevřením nebo nastavitelná vzdálenost.</p>'
          '<p>Kola ovlivňují stabilitu víc, než se čeká. Malá plná kolečka jsou bez údržby, jenže na každé nerovnosti trhají řidítka. Menší nafukovací pneumatiky, které se u dětských modelů objevují v rozměrech kolem šesti až sedmi palců, mají lepší komfort, ale vyžadují občas dofouknout a opravit duši. Větší kola jsou stabilnější na chodníkové dlažbě a lépe překonávají hrany. Odpružení se u dětských modelů vyskytuje spíš výjimečně a s nízkou rychlostí není nutné.</p>'
          '<h2>Baterie, nabíjení a dojezd pro dítě</h2>'
          '<p>Dětská koloběžka jezdí kratší vzdálenosti, proto obvykle postačí menší baterie a ušetříte na hmotnosti. Vyplatí se ale zkontrolovat dobu nabíjení: u dětí je dojezd často omezený a nabíjet se musí po každé vyjížďce. Hmotnost stroje má význam: pokud dítě koloběžku nezvedne na schodech, nosíte ji vy. Skládací konstrukce se prodává ve většině nabídky a usnadňuje převoz v autě i uložení v bytě.</p>'
          + T(['Parametr', 'Co hledat u dětského modelu', 'Proč'], [
              ['Hmotnost', 'co nejnižší, dítě by mělo koloběžku zvednout o patro', 'snazší manipulace a lepší ovládání při jízdě'],
              ['Nabíjení', 'jasně uvedená doba a nabíječka s ochranou', 'rodič ví, kdy je stroj připraven'],
              ['Skládání', 'pevná západka, kterou dítě samo neotevře', 'zabrání nechtěnému sklopení za jízdy'],
              ['Displej', 'rychlost a stav baterie na očích', 'dítě vidí, kdy je čas se vrátit'],
              ['Voděodolnost', 'ochrana proti stříkající vodě', 'ne na jízdu v dešti, ale na vlhké dlaždice']]) +
          '<p>Při zacházení s baterií platí pravidla jako u jiných lithiových článků: nabíjet pod dohledem, nenechávat nabíječku v zásuvce přes noc a držet baterii mimo mráz i horko. Pokud dítě koloběžku používá jen občas, ukládejte ji částečně nabitou.</p>'
          '<h2>Značky v nabídce dětských modelů</h2>'
          '<p>Dětské modely v katalogu nabízejí například ' + B(('iscooter', 'Iscooter'), ('eljet', 'Eljet'), ('rcb', 'RCB'), ('bluetouch', 'Bluetouch'), ('globber', 'Globber'), ('hitway', 'Hitway'), ('segway', 'Segway'), ('navee', 'Navee'), ('oxelo', 'Oxelo')) + '. '
          'Značky se liší zaměřením. Iscooter a RCB mají řadu skládacích modelů s Bluetooth reproduktorem, LED osvětlením a třemi rychlostními stupni, Eljet pracuje se stylovými barevnými provedeními pro mladší děti. Globber je původně výrobce dětských koloběžek a elektrické modely staví na jejich konstrukci, Segway s modelem Ninebot cílí na jednoduché ovládání a nízkou rychlost, Oxelo patří do sortimentu sportovního řetězce. Seznam se mění, proto si u každého kusu ověřte, jaké parametry výrobce uvádí.</p>'
          '<h2>Ochranné pomůcky a pravidla jízdy</h2>'
          '<p>K dětské elektrokoloběžce patří helma, a vyplatí se přidat i chrániče kolen a loktů a rukavice. Padání na dlažbě si způsobí odřeniny častěji než vážné úrazy, ale hlava je jiný případ. Přilba musí pevně sedět a mít správnou velikost podle obvodu hlavy. Vhodné pomůcky najdete v kategoriích <a href="/chranice-a-helmy/">chrániče a helmy</a> a <a href="/cyklo-chranice/">chrániče pro cyklisty</a>.</p>'
          '<p>Pravidla provozu pro elektrokoloběžky (věk řidiče, použití chodníku, cyklostezky a silnice, povinná přilba) určuje zákon o silničním provozu a mění se. Před nákupem je ověřte u ministerstva dopravy nebo u obce, kde dítě pojede. Na soukromém pozemku, hřišti nebo uzavřeném areálu mohou platit jiná pravidla než na veřejné komunikaci. Pokud nevíte, začněte jízdou v klidném prostoru a dítě naučte základy předem.</p>'
          '<h2>Dětská elektrokoloběžka, nebo klasická koloběžka</h2>'
          '<p>Elektrický pohon má smysl u dětí, které už výrazně přerostly jednoduchou koloběžku, a to hlavně kvůli delším trasám nebo kopcům. Pro mladší děti, které se učí rovnováze, je lepší klasický model, protože odraz nohou je i trénink. Širší výběr najdete v kategorii <a href="/kolobezky/">koloběžky</a>. Pokud chcete větší stroj pro dospívající, projděte <a href="/elektrokolobezka-levne/">levné elektrokoloběžky</a>, ale u mladších dětí nevolte kompromis na úkor brzd.</p>'
          '<h3>Kontrola před každou jízdou</h3>'
          '<ol><li>Zkontrolujte tlak v pneumatikách a stav kol.</li>'
          '<li>Vyzkoušejte brzdu na místě dřív, než dítě vyjede.</li>'
          '<li>Ověřte, že je pevně utažená západka skládání a řidítka.</li>'
          '<li>Nastavte nejnižší rychlostní stupeň pro méně zkušené dítě.</li>'
          '<li>Dítě musí mít helmu pevně dotaženou pod bradou.</li></ol>',
    faq=[
        ('Od jakého věku může dítě jezdit na elektrokoloběžce?', 'Výrobci obvykle uvádějí zhruba od šesti let, ale rozhoduje výška, váha a zkušenost. Dítě by mělo jistě ovládat klasickou koloběžku, umět se rozjet, zabrzdit a zatočit bez pádu. Zákonné podmínky jízdy na veřejných komunikacích si před nákupem ověřte v aktuálním znění zákona o silničním provozu.'),
        ('Jakou maximální rychlost má dětská elektrokoloběžka?', 'U dětských modelů se typicky pohybuje od deseti do zhruba dvaceti kilometrů v hodině. Některé stroje mají přepínání rychlostních stupňů, takže rodič zvolí nejpomalejší stupeň pro začátek. Konkrétní hodnotu najdete v popisu produktu a doporučujeme začít na nejnižší.'),
        ('Jaký výkon motoru stačí pro dítě?', 'Stačí slabší motor v řádu stovek wattů nebo méně. Silnější pohon zrychluje prudčeji a prodlužuje brzdnou dráhu, což dětem nic nepřináší. Důležitější je plynulý rozjezd a spolehlivé brzdy než údaj o výkonu v inzerátu.'),
        ('Je důležitá nosnost?', 'Ano, měla by mít rezervu nad váhou dítěte. Koloběžka provozovaná na hranici nosnosti rychleji opotřebuje brzdy, kola i ložiska. Pokud dítě rychle roste, zvolte model s vyšším limitem a nastavitelnými řidítky, aby vydržel víc sezón.'),
        ('Jaké brzdy zvolit?', 'Nejlepší je kombinace zadní kotoučové nebo bubnové brzdy s ruční páčkou a šlapací brzdou přes blatník. Elektronická brzda motoru sama nestačí. Zkuste, zda páčka dosáhne i na malou ruku a dítě ji zvládne stisknout bez velké síly.'),
        ('Jak dlouho se dětská elektrokoloběžka nabíjí a kolik ujede?', 'Doba nabíjení bývá několik hodin a dojezd se pohybuje v řádu jednotek až desítek kilometrů, podle kapacity baterie a stylu jízdy. Reálná vzdálenost je kratší než údaj výrobce, protože ten platí na rovině pro lehkého jezdce při stálé rychlosti.'),
        ('Potřebuje dítě helmu a chrániče?', 'Ano. Helma je základ, chrániče kolen, loktů a rukavice výrazně sníží následky pádu na dlažbě. Helma musí mít velikost podle obvodu hlavy a sedět pevně. V pravidlech provozu může být helma povinná, takže si ověřte aktuální předpisy.'),
        ('Dá se dětská elektrokoloběžka složit do auta?', 'Většina modelů v nabídce má skládací konstrukci, takže se vejde do kufru a na schodiště. Ověřte, že západka drží pevně a že dítě nemůže stroj samo nechtěně sklopit. Zeptejte se také na hmotnost, kterou zvládnete vy při nošení.'),
        ('Je lepší klasická koloběžka, nebo elektrická?', 'Pro malé děti je klasická koloběžka vhodnější, protože odraz nohou trénuje rovnováhu a koordinaci. Elektrický model se hodí pro starší děti, které chtějí jezdit na delší trasy nebo do kopce. Přechod zvolte až po zvládnutí základní jízdy.'),
        ('Dá se u dětské elektrokoloběžky vyměnit duše či pneumatiky?', 'U modelů s nafukovacími koly ano, v nabídce najdete i duše pro elektrokoloběžky v běžných rozměrech. Při koupi si zjistěte rozměr pláště i typ ventilku. Plná kola se nepoškodí píchnutím, ale jízda je tužší a výměna bývá obtížnější.'),
    ],
)

# ------------------------------------------------------------------ lyzarske-bryle-uvex
NEW['lyzarske-bryle-uvex'] = dict(
    title='Lyžařské brýle Uvex: řady, zorníky a výběr',
    desc='Lyžařské brýle Uvex: přehled řad Pwdr, Ignite, Provoqe, Blast a Speedy Nova, význam označení FM, CV a S1–S3 a rady pro výběr zorníku a velikosti.',
    intro='<p>Uvex je německý výrobce ochranných pomůcek, který kromě lyžařských brýlí vyrábí i helmy a sportovní optiku. V našem katalogu najdete jeho brýle v řadách s názvy jako Pwdr, Ignite, Provoqe, Blast, Gravity, Scenic a Speedy Nova pro děti. Liší se tvarem zorníku, zorným polem, typem skla a velikostí rámu. '
          'Tahle stránka vybírá z kategorie <a href="/lyzarske-bryle/">lyžařské brýle</a> jen modely značky Uvex a pomáhá rozklíčovat označení v názvech, třeba FM, CV, LG nebo S2. Najdete tu rozdíly mezi řadami, rady, jak zvolit zorník podle počasí a velikost podle helmy, a také srovnání s dalšími značkami. U každého modelu pak vidíte nabídky českých obchodů.</p>',
    guide='<h2>Co znamenají označení v názvech Uvex</h2>'
          '<p>Kdo poprvé otevře nabídku, najde názvy jako Uvex Ignite FM, Blast CV, Provoqe V nebo Ignite LG. Zkratky popisují zorník a jeho povrch. Na rámu bývá také údaj o kategorii filtru, tedy S1, S2 nebo rozsah S1–3. Pro přehled poslouží tabulka. Ověřujte vždy popis konkrétního kusu, protože výrobce zkratky používá v různých kombinacích.</p>'
          + T(['Označení', 'Co obvykle znamená', 'Na co se hodí'], [
              ['FM', 'full mirror, zrcadlový povrch zorníku', 'slunečné dny, kdy chcete omezit odlesky'],
              ['CV', 'ColorVision, zorník zvyšující kontrast', 'proměnlivé světlo, rozlišení hrbolů a stop'],
              ['LG', 'laser gold, zlatý zrcadlový povrch', 'střední až slunečné světlo'],
              ['V', 'variomatic, zorník se přizpůsobí světlu', 'jeden zorník na celý den'],
              ['S1, S2, S3', 'kategorie propustnosti světla', 'čím vyšší číslo, tím tmavší zorník'],
              ['OTG', 'možnost nosit pod brýlemi dioptrické brýle', 'dioptrie a lyžování']]) +
          '<p>Označení S1–3 u variomatic modelů říká, že se čočka pohybuje v rozsahu více kategorií. Kategorii 0 a 1 využijete při mlze a večerním lyžování, kategorii 3 za jasného slunce. Pokud potřebujete jen jedny brýle na celou sezónu v českých horách, je rozumná střední kategorie nebo variomatic.</p>'
          '<h2>Řady Uvex v nabídce</h2>'
          '<p>Katalog obsahuje několik řad, které se liší zaměřením. Berte popis jako orientační, rozdíly se mění s novými ročníky.</p>'
          '<ul><li><strong>Pwdr:</strong> nabízí se v dospělé i junior velikosti, bývá zaměřená na freeride a široký rozsah zorného pole, často se zrcadlovým povrchem.</li>'
          '<li><strong>Ignite:</strong> univerzální řada pro běžné lyžování, v nabídce s povrchem FM i LG a v provedení s možností nosit dioptrické brýle pod nimi.</li>'
          '<li><strong>Provoqe:</strong> nabízí se v zrcadlové i variomatic variantě, tvar je určený pro širší zorné pole.</li>'
          '<li><strong>Blast:</strong> rozsáhlejší řada od základního modelu až po variantu pro proměnlivé světlo, v nabídce i s variomatic zorníkem.</li>'
          '<li><strong>Gravity, Scenic, Athletic, Downhill 2100:</strong> další modely, které se liší rámem, tvarem a typem zorníku, dohledatelné v katalogu podle názvu.</li>'
          '<li><strong>Speedy Nova a Speedy Pro:</strong> dětské brýle s menším rámem, často s barevnými rámy.</li></ul>'
          '<p>Rozdíly mezi řadami nejlépe poznáte v praxi. Pro začátek rozhodněte, zda jezdíte hlavně po sjezdovkách, nebo mimo ně, protože od toho se odvíjí požadovaný rozsah zorného pole. Nejširší pole nabízí větší válcový nebo kulový zorník. Pro většinu lyžařů na upravených svazích bohatě stačí univerzální řada a rozumná kategorie zorníku.</p>'
          '<h2>Jak vybrat zorník podle počasí</h2>'
          '<p>Rozhodující je, kdy a kde lyžujete. Jedny brýle nepokryjí všechny podmínky, proto buď zvolte variomatic zorník, nebo si pořiďte druhý zorník do kapsy. Nejtmavší zorníky se hodí na ledovec a jasné slunce, nejsvětlejší na mlhu a sněžení.</p>'
          + T(['Podmínky', 'Kategorie', 'Poznámka'], [
              ['Jasno, ledovec, vysoké hory', 'S3', 'tmavý zorník, často zrcadlový'],
              ['Polojasno, běžná sjezdovka', 'S2', 'nejuniverzálnější volba'],
              ['Sněžení, mlha, zataženo', 'S1', 'kontrast bez tmavnutí'],
              ['Večerní lyžování, hustá mlha', 'S0', 'téměř čirý zorník'],
              ['Měnící se počasí během dne', 'S1–3', 'variomatic nebo výměnný zorník']]) +
          '<p>Pokud brýle ztratí zorník nebo se poškrábou, hledejte kategorii <a href="/nahradni-zorniky/">náhradní zorníky</a>. Zorník musí odpovídat přesně řadě a ročníku rámu, protože se mezi modely nedají zaměnit.</p>'
          '<h2>Velikost, helma a dioptrie</h2>'
          '<p>Brýle musí navazovat na helmu bez mezery na čele. Nad brýlemi nemá být holé místo, jinak vás tam při jízdě bude studit a hrozí nárazy hranou helmy. Zkoušejte brýle vždy s helmou, kterou budete nosit. Vhodné kousky najdete v kategorii <a href="/lyzarske-helmy/">lyžařské helmy</a>. U dětí i malých dospělých vybírejte menší rámy, jinak brýle zatlačí na nos nebo sklouzávají. Dětské varianty hledejte i na stránce <a href="/detske-lyzarske-bryle/">dětské lyžařské brýle</a>.</p>'
          '<p>Kdo nosí dioptrické brýle, hledá model s označením OTG, který má větší vnitřní prostor a výřezy pro obruby. Rám musí být dost vysoký, aby se brýle nedotýkaly zorníku, jinak se budou zamlžovat. Alternativou jsou dioptrické vložky, které se připevní uvnitř rámu.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Zorník otírejte jen měkkou textilií, která se dodává s brýlemi, a nikdy mokrou rukavicí nebo papírovým kapesníkem. Antifogová vrstva uvnitř čočky se otěrem poškodí a zrcadlová vrstva je citlivá na škrábance. Po jízdě brýle vysušte při pokojové teplotě, nikoli na topení. Uložte je do měkkého pouzdra, ne do kapsy s klíči.</p>'
          '<h2>Uvex v porovnání s jinými značkami</h2>'
          '<p>V nabídce kategorie jsou i další výrobci: ' + B(('alpina', 'Alpina'), ('smith', 'Smith'), ('scott', 'Scott'), ('poc', 'Poc'), ('oakley', 'Oakley'), ('salomon', 'Salomon'), ('rossignol', 'Rossignol')) + '. '
          'Alpina je další německá značka s podobným pojetím, Smith a Oakley patří k hlavním jménům v segmentu freeridu a sofistikovanější optiky, Scott a Poc mají vlastní řešení pro helmu a rám. Uvex se v kategorii vyznačuje velkým počtem řad pro různé výběry a pro děti. Konkrétní rozdíl poznáte při porovnání zorného pole a kompatibility s vaší helmou. Podobné stránky najdete také pro <a href="/lyzarske-bryle-oakley/">Oakley</a> a <a href="/lyzarske-bryle-poc/">Poc</a>, pro pánské varianty <a href="/lyzarske-bryle-panske/">pánské lyžařské brýle</a> a pro ženy <a href="/damske-lyzarske-bryle/">dámské lyžařské brýle</a>.</p>'
          '<h3>Co zkontrolovat před nákupem</h3>'
          '<ol><li>Řadu a rok modelu, pokud chcete později dokoupit zorník.</li>'
          '<li>Kategorii filtru a typ zorníku podle vašeho lyžování.</li>'
          '<li>Kompatibilitu s helmou a velikost rámu.</li>'
          '<li>Označení OTG, pokud nosíte dioptrie.</li>'
          '<li>Součástí balení: pouzdro, náhradní zorník nebo jen samotné brýle.</li></ol>',
    faq=[
        ('Co znamená FM u brýlí Uvex?', 'Zkratka označuje full mirror, tedy zrcadlový povrch zorníku. Zrcadlová vrstva odráží část světla ještě před čočkou, takže je pohled příjemnější na jasném slunci. Přesné provedení najdete v popisu konkrétního modelu, protože kombinace se liší.'),
        ('Jaký je rozdíl mezi S1, S2 a S3?', 'Jde o kategorie propustnosti světla. S1 je světlejší zorník pro mlhu a sněžení, S2 je univerzální volba pro polojasno a S3 je tmavý zorník pro jasné slunce. Čím vyšší číslo, tím méně světla projde.'),
        ('Co jsou brýle s označením V nebo S1–3?', 'Jde o brýle s variomatic zorníkem, který se přizpůsobuje světlu. Za slunce ztmavne, ve stínu se projasní, takže nemusíte při změně počasí měnit zorník. Reakce přichází s mírným zpožděním a v chladu je pomalejší.'),
        ('Jak poznám velikost pro dítě?', 'Dětské řady, například Speedy Nova nebo Pwdr v junior provedení, mají menší rám. Zkoušejte je vždy s dětskou helmou a zkontrolujte, zda nezatlačí na nos a zda přiléhají po stranách. U rychle rostoucích dětí vybírejte spíš rozumnější větší velikost.'),
        ('Dají se Uvex nosit přes dioptrické brýle?', 'Ano, pokud mají označení OTG, tedy větší vnitřní prostor. Rám má dostatek výšky pro obruby a zorník se jich nedotýká. Druhou možností jsou dioptrické vložky, které se upevní do rámu brýlí.'),
        ('Dají se k Uvex dokoupit náhradní zorníky?', 'U řady modelů ano, ale zorník musí odpovídat přesné řadě a ročníku rámu. Před koupí si ověřte kód modelu a barvu zorníku. Dostupné kusy najdete v kategorii náhradních zorníků a příslušenství.'),
        ('Jak zabránit mlžení?', 'Mlžení omezují dvojitý zorník, antifogová vrstva a větrání rámu. Nezvedejte brýle na čelo, když se zahřejete, protože vlhkost se pak usadí uvnitř. Vrstvu uvnitř zorníku nikdy neotírejte prsty ani rukavicí a po jízdě brýle vysušte.'),
        ('Sedí Uvex s každou helmou?', 'Většinou ano, ale kombinace musí navazovat bez mezery na čele. Brýle vždy zkoušejte s helmou, kterou nosíte. Některé tvary rámu se k určitým helmám hodí lépe, jiné vytvoří mezeru, která tlačí nebo studí.'),
        ('Který model vybrat na celou sezónu?', 'Pro nejširší využití zvolte střední kategorii S2 nebo variomatic zorník a rám, který sedí k vaší helmě. Pokud lyžujete také večer nebo při mlze, doplňte světlý zorník. Další varianty porovnáte v kategorii lyžařských brýlí.'),
    ],
)

# ------------------------------------------------------------------ mizuno-bezecke-boty
NEW['mizuno-bezecke-boty'] = dict(
    title='Mizuno běžecké boty: řady Wave, Neo a Hyperwarp',
    desc='Mizuno běžecké boty: jak se liší řady Wave Rider, Inspire, Sky, Neo Zen a Hyperwarp, pro koho jsou a jak vybrat velikost. Porovnání nabídek obchodů.',
    intro='<p>Mizuno je japonská sportovní značka s dlouhou historií v běžecké obuvi, známá deskou Wave ve střední části podešve. Do katalogu patří řady Wave Rider, Wave Inspire, Wave Sky, Wave Ultima, novější Neo Zen a Neo Vista a rychlejší Hyperwarp, k tomu terénní Wave Daichi a Wave Mujin. '
          'Tato stránka vybírá z kategorie <a href="/bezecka-obuv/">běžecké boty</a> jen obuv značky Mizuno. Průvodce vysvětluje, jak se liší jednotlivé řady, kdo si má vybrat neutrální a kdo stabilní model, jak porovnat Mizuno s jinými výrobci a jak vybrat velikost. Pro každý model si pak můžete prohlédnout nabídky českých obchodů.</p>',
    guide='<h2>Deska Wave a charakter bot Mizuno</h2>'
          '<p>Základem mnoha bot Mizuno je deska Wave, vlnitý plastový prvek ve střední části podešve. Rozděluje náraz při došlapu, přispívá ke stabilitě a drží tvar boty. Jednotlivé řady ji doplňují různými pěnovými mezipodešvemi a svršky. Řady Neo používají jiné pojetí s modernější pěnou, kde je deska Wave nahrazena jinou konstrukcí. Konkrétní technologie najdete v popisu každého kusu. Boty Mizuno mají pověst pevných a odolných a jsou oblíbené mezi běžci, kteří preferují přesný, ne přehnaně měkký došlap.</p>'
          '<h2>Přehled řad a pro koho jsou</h2>'
          + T(['Řada', 'Charakter', 'Pro koho'], [
              ['Wave Rider', 'neutrální, univerzální trénink', 'většina rekreačních běžců, každodenní kilometry'],
              ['Wave Inspire a Horizon', 'stabilnější, s podporou vnitřní strany', 'běžci s výraznější pronací nebo těžší běžci'],
              ['Wave Sky a Skyrise', 'více tlumené, měkčí', 'dlouhé pomalé běhy, pohodlí na silnici'],
              ['Wave Ultima', 'lehčí neutrální bota', 'tempové tréninky, běžci s nižší hmotností'],
              ['Neo Zen, Neo Vista, Neo Cosmo', 'novější řady s jinou pěnou', 'pohodlné tréninky, běžci hledající živější došlap'],
              ['Hyperwarp, Wave Rebellion', 'rychlé, lehké boty', 'tempo, závody, kratší tratě'],
              ['Wave Daichi, Mujin, Neo Daichi', 'terénní, s hrubším vzorkem', 'lesní cesty, kopce, bahno'],
              ['Fortrush', 'jednodušší základní model', 'začátečníci, občasný běh']]) +
          '<p>Rozdělení je zjednodušené: výrobce řady v čase upravuje a nové ročníky přicházejí s číslem na konci názvu, například Wave Rider 29. Pokud si koupíte starší ročník, který už obchody vyprodávají, bývá rozdíl proti nové verzi menší, než uvádí marketing, a výrazně vám to ušetří peníze. Vždy si ale ověřte, že máte svou velikost a že jde o stejný typ boty.</p>'
          '<h2>Neutrální, nebo stabilní bota</h2>'
          '<p>Nejčastější otázka u značky Mizuno je volba mezi Riderem a Inspire. Rider je neutrální, nechává noze volný pohyb. Inspire je pevnější na vnitřní straně a pomáhá, když se chodidlo po došlapu výrazně propadá dovnitř. Rozhodněte podle sešlapání podrážky a podle toho, zda vás po delších bězích bolí kolena nebo holeně. Nejste-li si jisti, začněte neutrální botou. Rozbor došlapu na pásu nabídnou běžecké obchody a ušetří zkoušení naslepo.</p>'
          '<h2>Silnice, nebo terén</h2>'
          '<p>Mizuno má obojí. Silniční boty jsou lehčí, mají hladší podešev a dobře tlumí tvrdý povrch. V nabídce je filtrované pod stránkami <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>. Terénní modely, například Wave Daichi nebo Wave Mujin, mají hrubší vzorek podrážky a pevnější špičku. Najdete je i mezi <a href="/trailove-boty/">trailovými botami</a>. U některých terénních modelů je i verze s membránou, označená zkratkou GTX, která chrání před vlhkem, ale hůř odvětrává. Pro léto je zbytečná.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Běžecká bota má být o něco větší než běžná obuv, aby před špičkou zůstal prostor zhruba na šířku palce. Mizuno bývá spíše klasičtější až užší střih, ale liší se řada od řady, a proto si prostudujte popis šířky a recenze. Pokud máte širší nárt, zkuste model, který výrobce nabízí v širší variantě, nebo zvolte jinou řadu. Vždy se řiďte délkou stélky v centimetrech, kterou obchody uvádějí, a změřte si chodidlo odpoledne, kdy je největší.</p>'
          '<ul><li><strong>Délka:</strong> prostor před nejdelším prstem zhruba šířka palce.</li>'
          '<li><strong>Šířka:</strong> v přední části se nesmí tlačit prsty, ale pata musí sedět pevně.</li>'
          '<li><strong>Šněrování:</strong> při klouzání paty využijte poslední očko.</li>'
          '<li><strong>Ponožky:</strong> zkoušejte v těch, v nichž budete běhat.</li></ul>'
          '<h2>Dámské a pánské provedení</h2>'
          '<p>Katalog obsahuje boty pro ženy i muže, někdy v modelech se stejným názvem. Dámský střih je obvykle užší v patě a v nártu a může mít jiné barevné provedení. Porovnat můžete také na stránce <a href="/bezecke-boty-damske/">dámské běžecké boty</a>. Pokud máte užší nohu a nosíte velikost mezi dvěma čísly, zvolte vždy menší šířku. Pro děti hledejte přehled <a href="/detske-bezecke-boty/">dětské běžecké boty</a>.</p>'
          '<h2>Mizuno v porovnání s jinými značkami</h2>'
          '<p>V kategorii jsou nejvíc zastoupeny ' + B(('adidas', 'Adidas'), ('asics', 'Asics'), ('nike', 'Nike'), ('puma', 'Puma'), ('new-balance', 'New Balance'), ('hoka', 'Hoka'), ('saucony', 'Saucony'), ('brooks', 'Brooks'), ('on', 'On')) + '. '
          'Asics je z podobné japonské školy a nabízí srovnatelné kategorie neutrálních a stabilních bot. Hoka a On sázejí na výraznější tlumení a nezvyklý tvar podešve, Brooks a Saucony jsou tradiční tréninkové značky. Mizuno bývá volbou pro ty, kdo chtějí pevnější, vyvážený došlap bez extrémního tlumení. Další značky můžete porovnat na stránkách <a href="/bezecke-boty-asics/">Asics</a>, <a href="/nike-bezecke-boty/">Nike</a>, <a href="/adidas-bezecke-boty/">Adidas</a> a <a href="/new-balance-bezecke-boty/">New Balance</a>.</p>'
          '<h3>Jak dlouho bota vydrží</h3>'
          '<p>Běžecká bota se používá zhruba stovky kilometrů, než ztratí tlumení. Přesné číslo závisí na hmotnosti běžce, povrchu a konstrukci. Sledujte sešlapaný vzorek, popraskanou pěnu a pocit, že bota už nepruží. Střídání dvou párů prodlužuje životnost pěny, protože se stihne zregenerovat.</p>',
    faq=[
        ('Jaký je rozdíl mezi Mizuno Wave Rider a Wave Inspire?', 'Wave Rider je neutrální univerzální trénink, nechává noze volný pohyb. Wave Inspire má pevnější vnitřní stranu a pomáhá při větší pronaci. Pokud si nejste jisti, začněte u Rideru a stabilní model volte, až když vás bolí kolena nebo holeně.'),
        ('Co je deska Wave?', 'Jde o vlnitý plastový prvek ve střední části podešve, který rozděluje náraz při došlapu a dodává botě stabilitu. Nové řady Neo používají jiné konstrukce. Přesné technologie najdete vždy u popisu konkrétního modelu.'),
        ('Jak vypadá velikost Mizuno?', 'Velikost se liší podle řady, proto vždy porovnejte délku stélky v centimetrech s délkou svého chodidla. Před špičkou by měl zůstat prostor zhruba na šířku palce. Mnoho řad sedí užším střihem, širší nohy by měly číst popis šířky.'),
        ('Které Mizuno je vhodné na dlouhé trasy?', 'Na dlouhé pomalé běhy se hodí tlumenější řady jako Wave Sky nebo Wave Skyrise. Pro běžný trénink poslouží Wave Rider. Pro tempo a rychlejší tréninky zvolte lehčí Wave Ultima nebo Hyperwarp.'),
        ('Jsou Mizuno boty vhodné do terénu?', 'Ano, v nabídce jsou trailové modely, například Wave Daichi a Wave Mujin, s hrubším vzorkem a zesílenou špičkou. Na asfalt se hodí méně, protože se vzorek rychle sjíždí. Pokud běháte střídavě, zvolte hybridní botu s mělkým vzorkem.'),
        ('Co znamená GTX u terénních bot?', 'Jde o membránu proti vlhkosti a vodě. Chrání před promočením v chladnějších měsících, ale hůř odvětrává a bota schne pomaleji. V létě je často zbytečná, v zimě a na mokrých cestách se může hodit.'),
        ('Mám koupit starší ročník, nebo nejnovější?', 'Starší ročník zpravidla nabízí podobný komfort za příznivější cenu, hlavně když se liší jen detaily svršku. Zkontrolujte, že je dostupná vaše velikost a že jde o stejný typ boty. U závodních modelů bývá rozdíl mezi ročníky větší.'),
        ('Jak dlouho bota vydrží?', 'Obvykle několik stovek kilometrů, ale záleží na váze běžce, povrchu a konstrukci. Známkou opotřebení je sešlapaný vzorek, popraskaná pěna nebo ztráta pružnosti. Střídání dvou párů prodlužuje životnost obou.'),
        ('Má smysl kupovat dámské a pánské provedení zvlášť?', 'Ano, dámský střih bývá užší v patě a nártu a odlišně tvarovaný. Ženy s širším chodidlem ale mohou být spokojenější v pánském modelu a naopak. Rozhodujte podle toho, jak bota sedí, ne podle označení.'),
    ],
)

# ------------------------------------------------------------------ nike-dresy
NEW['nike-dresy'] = dict(
    title='Nike dresy: fotbalové, tréninkové, NFL i brankářské',
    desc='Nike dresy: rozdíly mezi tréninkovými Dri-FIT Park a Academy, replikami, brankářskými a americkými dresy NFL. Střih, velikost a péče o dres.',
    intro='<p>Nike je jedním z největších výrobců dresů a v katalogu pokrývá víc sportů, než se čeká. Najdete tu tréninkové a týmové dresy Dri-FIT Park, Academy a Stripped pro fotbal, brankářské modely, rozhodcovské dresy Ref a také dresy amerických lig NFL a MLB a repliky reprezentací a klubů. '
          'Stránka vybírá z kategorie <a href="/dresy/">dresy</a> modely značky Nike a ukazuje, jak se jednotlivé typy liší střihem, materiálem a určením. Průvodce vysvětluje rozdíly mezi tréninkovým a fanouškovským dresem, pomáhá s velikostí a s výběrem pro dítě a srovnává Nike s dalšími značkami. U každého kusu vidíte nabídky českých obchodů.</p>',
    guide='<h2>Jaké typy dresů Nike se prodávají</h2>'
          '<p>Sortiment značky Nike v kategorii dresů se dá rozdělit do několika skupin, které se liší účelem i střihem. Teprve podle toho, k čemu dres potřebujete, má smysl řešit barvu a velikost.</p>'
          + T(['Typ', 'Příklady řad', 'Pro koho a k čemu'], [
              ['Týmový a tréninkový dres', 'Dri-FIT Park, Academy, Stripped', 'kluby, školy, amatérské týmy, trénink'],
              ['Brankářský dres', 'Dry Park, Gardien', 'brankáři, zesílené rukávy a odlišné barvy'],
              ['Rozhodcovský dres', 'Dri-FIT Ref', 'rozhodčí a organizátoři zápasů'],
              ['Replika klubu nebo reprezentace', 'sezónní domácí a venkovní dresy', 'fanoušci, nošení ve městě'],
              ['Americké ligy', 'NFL, MLB, NBA', 'fanoušci a sběratelé, objemný střih'],
              ['Dětské a dámské varianty', 'Park a Stripped v junior velikosti, dámské střihy', 'dětské týmy, dívky a ženy']]) +
          '<p>Největší skupinu tvoří týmové a tréninkové dresy, které se prodávají v mnoha barvách a mají jednoduchý vzhled bez složitého potisku. Právě na nich se hodí hromadný nákup pro celý tým, protože stejná řada se objevuje v desítkách barev a ve velikostech od dětských po dospělé.</p>'
          '<h2>Dri-FIT: materiál na pot</h2>'
          '<p>Dri-FIT je označení Nike pro funkční vlákna, která odvádějí pot od pokožky k povrchu látky, kde se rychle odpařuje. Tréninkový dres z tohoto materiálu zůstává při zátěži sušší než bavlněné triko. Funkčnost si udržuje, když se pere podle návodu. Nepoužívejte aviváž, která zalepuje vlákna, a vyhněte se sušičce na vysokou teplotu. Dres perte i sušte naruby, aby se potisk a znaky neotíraly. Funkční dresy pomalu pohlcují zápach, takže je nenechávejte vlhké v batohu.</p>'
          '<h2>Tréninkový dres, nebo replika</h2>'
          '<p>Fanouškovská replika vypadá jako zápasový dres, ale střih je volnější a materiál odolnější. Tréninkový dres Park nebo Academy je jednodušší a levnější na obnovu, snese časté praní a hodí se pro týmy a děti. U Nike se v popisu setkáte s označeními Stadium (volnější střih pro fanoušky) a Match nebo Vapor (těsnější provedení blízké zápasovému). Přiléhavý střih vyžaduje velikost podle míry a není vhodný pro každodenní nošení. Pokud dres kupujete na tribunu, dejte přednost volnějšímu střihu.</p>'
          '<h2>Dresy NFL, MLB a NBA</h2>'
          '<p>Značná část nabídky Nike v kategorii jsou dresy amerických lig. Tyto dresy mají objemnější střih než fotbalové, delší záda a široké rukávy, protože se nosí přes ramenní chrániče. Existují zápasové (game) a limitované série (například s označením Rivalries Game nebo City Connect). Číslo a jméno hráče bývá našité nebo nažehlené, takže se při praní chovejte opatrně. Pokud dres chcete nosit ve městě, vyberte velikost o jednu až dvě menší než pro hru, nebo si ověřte tabulku. Konkrétní hráči a týmy se mění s každou sezónou, takže starší ročníky se časem stávají sběratelskými.</p>'
          '<h2>Brankářské a rozhodcovské dresy</h2>'
          '<p>Brankářský dres se liší výraznou barvou, aby ho nezaměnili s hráči v poli, a dlouhým rukávem, někdy s vycpávkami na loktech. Barvy v nabídce bývají reflexní neon, modrá nebo oranžová. Rozhodcovský dres Ref III se nabízí v černé a dalších barvách a hodí se i k tréninku trenérů. Podrobnější informace o přípravě na zápas najdete v kategorii <a href="/fotbal/">fotbal</a>, kde jsou také <a href="/kopacky/">kopačky</a> a doplňky.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Velikostní tabulka se liší podle typu dresu a pohlaví. Dětské velikosti jsou označovány podle věku nebo výšky, dámský střih je užší v pase a kratší. Při pochybnostech změřte hrudník nejširším místem a porovnejte s tabulkou výrobce. Při výběru pro rostoucí dítě je lákavé koupit větší velikost, ale příliš velký dres překáží při hře. Rozumná je velikost o jedno číslo větší.</p>'
          '<ul><li><strong>Měřte hrudník:</strong> a porovnejte s tabulkou výrobce u konkrétní řady.</li>'
          '<li><strong>Dětské velikosti:</strong> řiďte se výškou, ne jen věkem.</li>'
          '<li><strong>Americké ligy:</strong> počítejte s objemným střihem.</li>'
          '<li><strong>Těsný střih:</strong> vyberte přesnou velikost, jen když chcete zápasové provedení.</li></ul>'
          '<p>Pro děti je užitečné prohlédnout stránku <a href="/detske-dresy/">dětské dresy</a>, kde najdete modely ve všech značkách. Pro fanoušky klubů je tu přehled <a href="/real-madrid-dresy/">dresů Real Madrid</a>.</p>'
          '<h2>Nike v porovnání s jinými značkami dresů</h2>'
          '<p>V kategorii jsou zastoupeny také ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('mitchell-ness', 'Mitchell &amp; Ness'), ('fanatics', 'Fanatics'), ('errea', 'Errea'), ('joma', 'Joma'), ('kipsta', 'Kipsta'), ('jako', 'Jako')) + '. '
          'Adidas a Puma jsou hlavní konkurenti v klubových a reprezentačních dresech, Mitchell &amp; Ness a Fanatics se zaměřují na retro a licencované dresy amerických lig. Errea, Joma a Jako dodávají týmové sady pro amatérské kluby. Nike vyniká šířkou nabídky: od základního trika pro děti po licencované dresy lig. Další oblečení téže značky najdete na stránkách <a href="/nike-mikina/">Nike mikiny</a> a <a href="/nike-teplaky/">Nike tepláky</a>, obuv v kategoriích <a href="/kopacky-nike/">kopačky Nike</a> a <a href="/nike-bezecke-boty/">běžecké boty Nike</a>.</p>'
          '<h3>Praní a údržba</h3>'
          '<ol><li>Perte naruby při teplotě do třiceti až čtyřiceti stupňů.</li>'
          '<li>Nepoužívejte aviváž ani bělidlo.</li>'
          '<li>Sušte na vzduchu, mimo přímé slunce.</li>'
          '<li>Potisk a znaky nežehlete přímo.</li>'
          '<li>Dres nenechávejte vlhký v batohu, vznikne zápach.</li></ol>',
    faq=[
        ('Co znamená Dri-FIT?', 'Je to označení Nike pro funkční materiál, který odvádí pot od pokožky k povrchu látky. Dres zůstává při zátěži sušší než bavlněné triko. Funkčnost zachováte praním bez aviváže a sušením na vzduchu.'),
        ('Čím se liší Park, Academy a Stripped?', 'Jsou to řady tréninkových a týmových dresů, které se liší střihem, vzorem a barvami. Park je základní týmový dres, Academy bývá tréninkové triko a Stripped má pruhy. Přesný popis najdete u každého modelu.'),
        ('Jaký je rozdíl mezi replikou a zápasovým dresem?', 'Replika má volnější střih a odolnější materiál, je určená fanouškům. Zápasové provedení, označované jako Match nebo Vapor, je těsnější a lehčí. Pro nošení ve městě je pohodlnější replika.'),
        ('Jak vybrat velikost dětského dresu?', 'Řiďte se výškou dítěte a tabulkou výrobce, ne jen věkem. Dres by měl být o něco volnější, ale ne tak velký, aby překážel při hře. U rostoucího dítěte je rozumná velikost o jedno číslo nahoru.'),
        ('Jak velké jsou dresy NFL?', 'Mají objemný střih, delší záda a široké rukávy, protože se původně nosí přes chrániče. Pro nošení ve městě volí mnoho lidí menší velikost než pro hru. Ověřte tabulku konkrétní řady a vlastní míry.'),
        ('Čím se liší brankářský dres?', 'Má výraznou barvu, aby se odlišil od hráčů v poli, dlouhý rukáv a někdy vycpávky na loktech. Barvy v nabídce bývají reflexní neon, modrá, oranžová nebo žlutá. Je určen pro pády a skluzy.'),
        ('Jak prát dres s potiskem?', 'Perte naruby při nízké teplotě, bez aviváže a bez sušičky. Potisk, číslo a znak nežehlete přímo a nenechávejte dres vlhký v batohu. Při dodržení těchto zásad vydrží potisk celou sezónu.'),
        ('Je dres Nike vhodný pro celý tým?', 'Ano, řada Park se prodává v mnoha barvách a velikostech od dětských po dospělé, takže tým může mít jednotný vzhled. Při hromadném nákupu zvolte stejný ročník a řadu, aby se barvy shodovaly. Číslování a potisk se řeší zvlášť.'),
        ('Najdu i dámské dresy Nike?', 'Ano, v nabídce jsou dámské střihy například v řadě Park a Academy. Mají užší pas a kratší délku. Pokud ženě vyhovuje volnější střih, může zvolit i pánský či unisex model.'),
    ],
)


# ---- extra sections (appended to reach the word target)
NEW['detska-elektrokolobezka']['intro'] = NEW['detska-elektrokolobezka']['intro']
NEW['detska-elektrokolobezka']['guide'] += (
    '<h2>První jízdy: jak dítě zacvičit</h2>'
    '<p>Nejlepší začátek je rovná plocha bez aut a chodců, třeba prázdné parkoviště nebo hřiště s hladkým povrchem. Dítě se nejprve rozjede bez zapnutého motoru, aby si zvyklo na hmotnost stroje, potom zkusí nejpomalejší stupeň a teprve po několika vyjížďkách přidá. Důležité je naučit ho brzdit oběma způsoby a zastavit na vyznačeném místě. Cvičte také zatáčení, vyhýbání překážkám a pohled přes rameno. Teprve když tyto věci zvládá bez přemýšlení, má smysl vyjet na rušnější místa.</p>'
    '<p>Rodič stojí vedle, nikoli za dítětem, a vysvětluje pravidla slušné jízdy: dávat přednost chodcům, nepředjíždět těsně, nejezdit mezi zaparkovanými auty a za šera být vidět. Na kolech i na řidítkách pomáhají reflexní prvky a zvonek. Pokud dítě nechce jet pomalu a neposlouchá, stroj nechte nabíjet a vraťte se ke klasické koloběžce.</p>'
    '<h2>Jiné možnosti pro aktivní děti</h2>'
    '<p>Pro malé jezdce, kteří teprve začínají, jsou rozumnější klasické značky, třeba <a href="/kolobezka-micro/">koloběžky Micro</a> nebo <a href="/kolobezka-yedoo/">koloběžky Yedoo</a>. Starší děti, které hledají trik a skok, ocení <a href="/freestyle-kolobezky/">freestyle koloběžky</a>, kde elektrický pohon nemá místo. Elektrický model volte tehdy, když vám jde o delší trasy, ne o trénink dovedností.</p>'
)

NEW['lyzarske-bryle-uvex']['guide'] += (
    '<h2>Dětské brýle Uvex a růst dítěte</h2>'
    '<p>U dětí rozhoduje komfort víc než technologie. Dětský rám je menší, nižší na nose a má kratší popruh, takže se po helmě neposouvá. Vybírejte model, který dítě samo pohodlně nasadí a sundá, a nepřehánějte velikost kvůli růstu. Příliš velký rám se při pádu otočí a přestává chránit. Pro děti se hodí zorník střední kategorie, protože stejné brýle zvládnou slunečné i zamračené dny. Barevné rámy pomáhají rodičům najít dítě ve svahu a dítě si brýle rádo obleče.</p>'
    '<p>Při kontrole sedu zkuste dětskou hlavu s helmou nahnout dopředu a zpět: brýle mají zůstat na místě a po stranách netlačit. Ohnutý rám nebo uvolněný popruh jsou důvodem k výměně. Další dětské modely i jiných značek porovnáte na stránce <a href="/detske-lyzarske-bryle/">dětské lyžařské brýle</a>.</p>'
    '<h2>Ochrana očí a poškození</h2>'
    '<p>Každé kvalitní lyžařské brýle mají filtr proti ultrafialovému záření, a to i u světlého zorníku. Oko na sněhu vystavené oslnění trpí i za mlhy, protože mraky záření neblokují zcela. Nenechávejte proto brýle doma jen proto, že je zataženo. Zorník by měl být bez hlubokých škrábanců, protože ty odrážejí světlo a zhoršují kontrast. Rám při chladu zůstává pružný, ale po letech se může zkřehnout, a pokud se při ohnutí zdá tuhý nebo praská, je čas na novou sadu.</p>'
    '<p>Pěna při obličeji se časem opotřebuje a přestává těsnit. Znamená to průvan, mlžení a studené oči, a to i při jinak zachovalém zorníku. Doplňkem ke kompletní výbavě je <a href="/lyzarske-obleceni/">lyžařské oblečení</a>, které by mělo mít ladící barvy a dostatečné větrání. Nezapomeňte na <a href="/sportovni-bryle/">sportovní a sluneční brýle</a> pro dny mimo svah.</p>'
)

NEW['mizuno-bezecke-boty']['intro'] = NEW['mizuno-bezecke-boty']['intro'].replace('Pro každý model si pak můžete prohlédnout nabídky českých obchodů.','Pro každý model si pak můžete prohlédnout nabídky českých obchodů a porovnat, kde je zrovna skladem vaše velikost a barva.')
NEW['mizuno-bezecke-boty']['guide'] += (
    '<h2>Jak zkoušet boty a na co se zaměřit</h2>'
    '<p>Při koupi pomůže několik jednoduchých testů. Na obchodní podlaze udělejte pár kroků a poklusů, ne jen stůjte. Pata nesmí klouzat nahoru, prsty se mají mírně rozpínat a nárt nesmí tlačit od jazyku. Zkontrolujte, že jazyk zůstane na místě a švy nedrásají kůži u kotníku. Pokud kupujete na dálku, vyzkoušejte botu doma na měkké podložce a nepoužívejte ji hned na dlouhý běh. Většina obchodů nabízí vrácení nepoužité obuvi, takže si ověřte podmínky.</p>'
    '<p>Při přechodu z jiné značky počítejte s adaptací. Změna dropu, tlumení nebo tuhosti zatěžuje jiné svaly a šlachy než dosavadní bota. Prvních několik běhů zkraťte, a pokud nic nebolí, vraťte se k běžné délce. Nejrychleji se přizpůsobí pohodlná neutrální řada, nejpomaleji lehká závodní.</p>'
    '<h2>Tréninkový plán a výběr páru</h2>'
    '<p>Běžec s několika tréninky týdně vyjde nejlépe s dvěma páry. Jedna tlumená bota na pomalé a dlouhé běhy a druhá lehčí na tempo a intervaly. U Mizuno může jít například o kombinaci řady Wave Sky nebo Rider s rychlejším modelem Hyperwarp. Závodní botu si nechte na soutěže a na pár tréninků před nimi, protože se opotřebuje rychleji a hodí se jen na kratší úseky. Běžec, který teprve začíná, zpočátku vystačí s jedním univerzálním párem.</p>'
    '<h2>Údržba bot</h2>'
    '<p>Po zablácené trase boty vypláchněte vlažnou vodou a vyčistěte kartáčem, nikdy je nedávejte do pračky ani na topení. Vyndejte vložky a nechte je vyschnout zvlášť. Boty naplňte novinovým papírem, který vlhkost nasaje. Sušení u radiátoru deformuje pěnu a rozpouští lepidlo. Podrážku zkontrolujte po každém běhu na ostré kamínky, které se do vzorku zaklínily. Dobře udržovaný pár vydrží déle a chrání klouby.</p>'
)

NEW['nike-dresy']['intro'] = NEW['nike-dresy']['intro'].replace('U každého kusu vidíte nabídky českých obchodů.','U každého kusu vidíte nabídky českých obchodů a snadno poznáte, kde je skladem vaše velikost.')
NEW['nike-dresy']['guide'] += (
    '<h2>Dresy pro děti a růst</h2>'
    '<p>Dětský tým potřebuje dresy, které vydrží opakované praní a několik měsíců růstu. Nejpraktičtější je rozhodnout se pro jednu řadu a barvu a sledovat velikostní tabulku. Mladší děti dres nosí často i mimo hřiště, proto vybírejte měkký materiál bez drsných švů u krku. Pokud dítě hraje v týmu s přidělenými čísly, zeptejte se trenéra, zda klub vyžaduje konkrétní odstín, aby se nelišil od ostatních. Dětské dresy v nabídce se prodávají v celé škále barev od černé po tyrkysovou.</p>'
    '<h2>Číslo, jméno a personalizace</h2>'
    '<p>Fanouškovské dresy mívají předtištěné jméno a číslo hráče, a to na dresech klubů i lig. Týmové dresy se prodávají bez potisku a čísla se přidávají zvlášť, nejčastěji nažehlením nebo sítotiskem. Potisk dělá obvykle specializovaná firma a objednává se až po výběru velikostí, protože každý hráč musí mít své. Před potiskem zkontrolujte, zda se dres nesráží. Pokud se hráči v týmu mění, objednejte několik velikostí navíc.</p>'
    '<h2>Retro a sběratelské kousky</h2>'
    '<p>Starší dresy klubů a lig mají silný sběratelský půvab. Hodnotu ovlivňuje stav, originální štítek a znak, nikoli značka sama. Při koupi staršího nebo použitého kusu si prohlédněte švy, potisk a štítek s praním. Nová sada je ale většinou praktičtější, protože se dá bez obav nosit a prát. Pokud chcete kus do vitríny, ptejte se na stav a původ, a pokud ho chcete nosit, zvolte aktuální ročník.</p>'
)

# ---- second extension
NEW['lyzarske-bryle-uvex']['guide'] += (
    '<h3>Brýle a lyžařské vybavení jako celek</h3>'
    '<p>Při výběru brýlí myslete i na kombinaci s nákrčníkem, čepicí a helmou. Nákrčník přetažený přes nos vede teplý dech nahoru k zorníku a zvyšuje mlžení, proto jej nosíte raději pod nosem nebo zvolte materiál s větráním. Brýle připevněné k helmě magnetem nebo popruhem se při krátké pauze nejspíš nezamlží, pokud je neponecháte nasazené na čele. V kabině lanovky je dejte do kapsy nebo pouzdra, ne na kolena, kde se zorník snadno poškrábe.</p>'
)
NEW['mizuno-bezecke-boty']['guide'] += (
    '<h2>Mizuno a jiné sporty</h2>'
    '<p>Značka je známá i mimo běh, hlavně halovými sporty, a stejná firma tak rozumí tvrdým povrchům a rychlým změnám směru. U běžecké obuvi to znamená, že boty dobře drží při došlapu a nemají přehnaně vysokou, nestabilní podešev. Pro běh na dráze nebo na trávníku však zvolte botu s odpovídající podrážkou. Běžecký model se nehodí na sály a naopak, pro každý povrch existuje obuv se vhodným vzorkem a tlumením.</p>'
    '<h2>Počasí a roční období</h2>'
    '<p>V zimě používejte botu s hustší pleteninou nebo se svrškem odolnějším proti vodě a pod ni teplejší ponožku, ale nezužujte prostor pro prsty. Na led pomohou návleky s hroty, nikoli sama podrážka. V létě stačí lehký svršek z prodyšné sítoviny. Na deštivé dny je užitečný tmavší, snadno čistitelný model. Při výběru barvy myslete na viditelnost v šeru a ve městě, protože světlé nebo reflexní prvky pomáhají řidičům i cyklistům vás včas zahlédnout.</p>'
)
NEW['nike-dresy']['guide'] += (
    '<h2>Barvy týmů a viditelnost na hřišti</h2>'
    '<p>Při výběru barev v týmu myslete na kontrast se soupeřem a s brankářem. Světle žlutá nebo bílá se v šeru a na umělém osvětlení vyjímá, tmavé odstíny hůř vynikají a v horku se více zahřívají. Záleží také na tom, zda tým hraje doma, nebo venku, protože si organizátor může vyžádat odlišnou sadu. Brankář má mít barvu odlišnou od obou týmů i od rozhodčího, proto se brankářské dresy prodávají ve výrazných odstínech. Totéž platí v dětských soutěžích, kde často pomáhají rozlišovací vesty.</p>'
    '<p>Výběr pro sebe nebo pro hráče, který se v klubu často střídá, zjednodušte volbou střední velikosti, která sedí většině postav. Poslední kontrola patří švům: ramena a podpaží se při pohybu namáhají nejvíc, proto zkuste zvednout ruce a zkontrolujte, že se dres nezvedá nad pas.</p>'
)
