"""sporteka.cz — wave 13b (4. 11. 2026): long texts (>= 1650 words) for hokej, volny-cas, merino-tricka, sipky.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ hokej
NEW['hokej'] = dict(long=True,
    title='Hokejové vybavení: hokejky, brusle, chrániče | Sporteka',
    desc='Hokejové vybavení pro děti i dospělé: brusle, hokejky, helmy, chrániče, brankářská výstroj. Průvodce výběrem a nabídky českých e-shopů na jednom místě.',
    intro='<p><strong>Hokejové vybavení</strong> se skládá z mnoha částí a každá z nich plní jiný úkol: jedna nese váhu hráče na ostří, další chrání kosti před pukem a hokejkou, jiná zajišťuje, aby šlo puk vést a střílet. Kdo začíná od nuly, často nakoupí v nepořádku a pak doplácí. Rozumnější je jít po pořadí důležitosti, od věcí, které rozhodují o bezpečí, k těm, které ladí styl hry.</p>'
          '<p>Na Sportece najdete celou výbavu rozdělenou podle částí těla i podle role na ledě: <a href="/hokejove-brusle/">hokejové brusle</a>, <a href="/hokejky/">hokejky</a>, <a href="/hokejove-chranice/">výstroj a chrániče</a>, <a href="/hokejove-helmy-a-mrizky/">helmy s mřížkami</a> i samostatnou <a href="/hokejove-brankarske-vybaveni/">brankářskou výstroj</a>. U každého kusu vidíte nabídky více českých obchodů vedle sebe a můžete vybírat podle velikosti, dostupnosti a podmínek doručení.</p>',
    guide=(
        '<h2>Od čeho začít, když sestavujete výbavu</h2>'
        '<p>Hokej je rychlý a kontaktní sport, a proto se výbava nekupuje jako jedna položka, ale jako soubor, jehož části na sebe navazují. Nejdřív se řeší to, co chrání hlavu a nohy a co se nedá napravit dodatečně: helma, brusle a chrániče. Teprve potom přichází hokejka, rukavice a doplňky. Pořadí má praktický důvod. Pokud hráč špatně sedí v bruslích, nenaučí se správně bruslit, a pokud nemá dobře padnoucí chrániče, nemůže se na hru soustředit.</p>'
        '<p>Než začnete vybírat konkrétní kusy, ujasněte si tři věci. První je věk a velikostní řada: děti, junioři, dorost a dospělí mají různé střihy a ne vždy se dá jedna řada „přeskočit“. Druhá je úroveň hry. Kdo hraje jednou týdně pro radost, nepotřebuje stejné materiály jako hráč v pravidelné soutěži. Třetí je prostředí. Ledová plocha, inline hokej, hokejbal a pozemní hokej používají různé vybavení a části výstroje nejsou zaměnitelné.</p>'
        '<h3>Přehled částí výbavy</h3>'
        + T(['Část výbavy', 'K čemu slouží', 'Na co dát pozor'], [
            ['<a href="/hokejove-brusle/">Brusle</a>', 'nosí hráče po ledě, určují stabilitu a rychlost', 'délka a šířka kopyta, tuhost boty, stav ostří'],
            ['<a href="/hokejky/">Hokejka</a>', 'vedení puku, přihrávky, střelba', 'délka, ohebnost, zahnutí čepele, strana'],
            ['<a href="/hokejove-helmy-a-mrizky/">Helma a mřížka</a>', 'chrání hlavu a obličej', 'velikost, nastavení, kompatibilní mřížka'],
            ['<a href="/hokejove-chranice/">Chrániče a výstroj</a>', 'chrání ramena, lokty, boky, holeně', 'střih podle výšky, volnost pohybu'],
            ['<a href="/hokejove-brankarske-vybaveni/">Brankářská výstroj</a>', 'samostatný soubor pro brankáře', 'velikost podle postavy, role chráničů'],
            ['<a href="/hokejove-tasky/">Taška</a>', 'převoz a sušení vybavení', 'délka, kolečka, větrání'],
            ['<a href="/hokejove-pasky-a-doplnky/">Pásky a doplňky</a>', 'úprava čepele, tkaničky, vosk', 'spotřební, je dobré mít zásobu']]) +
        '<h2>Hokejové brusle</h2>'
        '<p>Brusle jsou nejdůležitější a obvykle nejtěžší část výběru. Hokejová bota je pevnější než bota na rekreační bruslení, protože musí držet kotník při prudkých změnách směru. Skořepina bývá z tvrdého plastu nebo kompozitu, vnitřek z pěn a textilu. Čím lepší bota, tím lépe se tvaruje podle nohy a tím efektivněji přenáší sílu do ostří. U nižších řad bývá bota měkčí, což začátečníkům a dětem ve skutečnosti vyhovuje, protože je pohodlnější.</p>'
        '<p>Velikost bruslí je nižší než číslo běžné obuvi, často o jedno až dvě čísla, ale výrobci se liší, a proto je vždycky dobré porovnat délku chodidla s tabulkou konkrétní značky. Zvlášť důležité je rozlišit šířku. Užší kopyto drží patu a prsty ve stálé poloze, širší je pohodlnější pro objemnější nohu. Pata nesmí zvedat, když se předkloníte, a prsty se mají jen lehce dotýkat špičky.</p>'
        '<ul><li>Kupujte brusle podle stylu hry: lehčí a pružnější pro obratné hráče, tužší pro výkonnostní.</li>'
        '<li>Dětem nekupujte brusle „na vyrůstání“, příliš velká bota brání učení techniky a hrozí otlaky.</li>'
        '<li>Po koupi nechte ostří nabrousit odborným servisem a brousit je pravidelně podle hry.</li>'
        '<li>Brusle po tréninku osušte a odstraňte chrániče ostří, jinak vlhkost způsobí korozi.</li></ul>'
        '<p>Kdo hraje pouze občas na kluzišti pro veřejnost, vystačí si i s modelem z kategorie <a href="/brusle/">zimní brusle</a> nebo <a href="/rekreacni-brusle/">rekreační brusle na led</a>. Hokejová bota má ale výhodu stability a ochrany nártu. Pro bruslení bez hokejky na jemném ledu se naopak hodí <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a>, které mají jiný tvar ostří a vyšší botu.</p>'
        '<h2>Hokejky: délka, ohebnost a čepel</h2>'
        '<p>Správná délka hokejky se dá orientačně změřit tak, že ji postavíte před sebe na špičku čepele. V bruslích by horní konec měl sahat zhruba k bradě, bez bruslí k nosu. Kratší hokejka umožňuje lepší vedení puku a hráči v útoku ji často volí. Delší hokejka zvyšuje dosah a obranáři ji upřednostňují. Kdo hokejku zkrátí, mění zároveň její ohebnost, proto se kratší šaft stává tužším.</p>'
        '<p>Ohebnost, anglicky flex, udává, jak moc se hokejka prohne při střelbě. Příliš tuhá hokejka se začátečníkovi neohne a střela nemá sílu, příliš měkká se zlomí nebo je nepřesná. U dětských hokejek se flex nastavuje podle věku a hmotnosti, u dospělých podle preferencí. Hodnota se uvádí na šaftu a výrobci ji používají pro vlastní stupnici, takže porovnávat je nejlépe v rámci jedné značky.</p>'
        '<p>Čepel určuje, jak puk padne do ruky a jak se chová při střelbě. Zahnutí neboli křivka ovlivňuje zvedání puku: výraznější zahnutí usnadňuje zvedání, rovnější čepel je přesná při přihrávkách. Nezapomeňte na stranu: levá a pravá hokejka se kupuje podle toho, která ruka je při držení nahoře. Pokud si nejste jistí, zkuste obě varianty v obchodě a vyberte tu, ve které se vám vede puk přirozeněji. Samostatné díly najdete v kategorii <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>, a to je výhodné u hráčů, kteří často lámou čepel nebo chtějí upravit délku šaftu.</p>'
        + T(['Materiál šaftu', 'Vlastnosti', 'Pro koho'], [
            ['Dřevo', 'odolné, těžší, nižší citlivost', 'děti, začátečníci, hokej na trénink'],
            ['Kompozit', 'lehký, pružný, citlivější', 'pravidelní hráči, soutěže'],
            ['Hybrid', 'kompozitový šaft s dřevěnou čepelí a naopak', 'hráči, kteří si ladí hokejku']]) +
        '<h2>Helma, mřížka a chrániče</h2>'
        '<p>Helma je jediná část, u které se nehraje na kompromis. Musí mít schválení pro hokej a dobře sedět, protože volná helma při pádu sklouzne. Nastavitelná velikost se hodí pro rostoucí děti, ale po každém zvětšení znovu zkontrolujte, zda helma nesedí příliš vysoko na čele. Mřížka se připevňuje k helmě a musí být kompatibilní se zvoleným modelem. U dětských soutěží se obvykle vyžaduje celá obličejová ochrana. Nabídku najdete v kategorii <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>. Poškozenou helmu po silnějším nárazu vyměňte, i když navenek vypadá v pořádku.</p>'
        '<p>Chrániče se kupují jako sada a hlavní zásadou je střih podle postavy. Ramenní chrániče mají sahat přes klíční kost a lopatky, ale nesmí omezovat zvedání paží. Loketní chránič musí držet na lokti a nepřetáčet se při pohybu. Hokejové kalhoty chrání boky a stehna, vybírají se podle obvodu pasu a délky. Chrániče holení se kupují podle vzdálenosti mezi středem kolena a horním okrajem boty. Rukavice mají překrývat zápěstí a zároveň nechat prsty volné pro úchop. Kompletní přehled najdete v kategorii <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>.</p>'
        '<ul><li>Ramena a hrudník, lokty, rukavice, kalhoty a holeně tvoří základní sadu.</li>'
        '<li>Krk a hrdlo se chrání zvláštním chráničem, který se hodí hlavně pro děti.</li>'
        '<li>Suspenzor nebo chránič třísel je povinný ve většině soutěží.</li>'
        '<li>Zuby chrání chránič zubů, který je vhodné nechat vytvarovat.</li></ul>'
        '<h2>Brankářská výstroj</h2>'
        '<p>Brankář nepoužívá stejné vybavení jako hráč v poli. Má větší chrániče, lapačku, vyrážečku, speciální helmu s mřížkou a brusle s ochranným krytem. Výstroj je těžší a jednotlivé části musí na sebe navazovat tak, aby se mezi nimi netvořily mezery. Dětem a začátečníkům se doporučují sady, které jsou lehčí a levnější a tolik se neopotřebují. Kdo hraje v soutěži, obvykle dává přednost modelům na míru podle postavy. Nabídku najdete v samostatné kategorii <a href="/hokejove-brankarske-vybaveni/">brankářská výstroj</a>.</p>'
        '<h2>Trénink, puky a doplňky</h2>'
        '<p>K tréninku mimo led se hodí <a href="/hokejove-puky-a-branky/">puky, branky a tréninkové pomůcky</a>. Plastové puky s nižším odrazem a plastové branky umožní trénovat střelbu na zahradě nebo na dvorku, aniž by se poškodila omítka. Trénovat lze i na střelecké podložce, která imituje led a dovoluje cvičit zpracování puku v domácím prostředí. Pro hráče je takový trénink užitečný hlavně v letní pauze.</p>'
        '<p>Spotřební doplňky najdete v kategorii <a href="/hokejove-pasky-a-doplnky/">pásky, tkaničky a doplňky</a>. Hokejová páska na čepel zlepšuje úchop a chrání dřevo nebo kompozit, tkaničky se opotřebují dřív než bota a vosk na pásku zlepšuje vedení puku. Dobré je mít vždy v tašce zásobu a doplnit ji před sezónou, ne uprostřed zápasu.</p>'
        '<h2>Taška, dresy a oblečení</h2>'
        '<p>Výbavu přepravuje <a href="/hokejove-tasky/">hokejová taška nebo batoh</a>, který musí být dostatečně velký a dobře větraný. Kolečka se vyplatí pro děti, protože plně naložená taška je těžká. Důležitější než velikost je ventilace: vlhká výbava v uzavřené tašce zahnívá a zapáchá. Po tréninku proto výstroj vyndejte a nechte ji uschnout při pokojové teplotě.</p>'
        '<p>Pod chrániče patří <a href="/termopradlo/">funkční spodní prádlo</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>, které odvádějí pot a snižují riziko puchýřů. Dresy a oblečení pro fanoušky a hráče najdete v kategorii <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>. Sběratelé a fanoušci mohou procházet <a href="/hokejove-suveniry-a-karty/">hokejové karty a suvenýry</a>.</p>'
        '<h2>Značky v nabídce</h2>'
        '<p>Největší sortiment mají ' + B(('bauer', 'Bauer'), ('ccm', 'CCM'), ('winnwell', 'Winnwell'), ('sherwood', 'Sherwood'), ('warrior', 'Warrior'), ('fischer', 'Fischer'), ('balling', 'Balling'), ('freez', 'Freez')) + '. Bauer a CCM pokrývají celou škálu od základních řad až po soutěžní vybavení. Winnwell a Sherwood jsou oblíbené u začínajících hráčů a pro dětské sady. Warrior je známý hlavně hokejkami a brankářským vybavením, Fischer a Balling nabízejí také tréninkové a rekreační hokejové vybavení.</p>'
        '<h2>Péče o výbavu a časté chyby</h2>'
        '<ul><li>Neskladujte vlhkou výstroj v zavřené tašce. Pot se nevysuší a chrániče zapáchají i drobí se.</li>'
        '<li>Brusle neodkládejte s nasazenými chrániči, kondenzace vede ke korozi ostří.</li>'
        '<li>Čepel obaluje páska, která se po několika hrách opotřebuje. Obnovujte ji dřív, než se začne odlupovat.</li>'
        '<li>Chrániče perte podle štítku a nesušte na topení, aby pěna neztratila tvar.</li>'
        '<li>Nepřeskakujte velikosti. Příliš velká výstroj nechrání, protože se při nárazu posune.</li></ul>'
        '<p>Mezi hokejové disciplíny patří i <a href="/pozemni-hokej/">pozemní hokej</a>, ale používá zcela jiné vybavení než ledový hokej. Kdo hraje v hale, může hledat i <a href="/florbal/">florbalové vybavení</a>, které je lehčí a nemá chrániče. Neplette si proto jednotlivé kategorie a vždy zkontrolujte, pro jaký sport je výrobek určen.</p>'
        '<h2>Pro koho jaká výbava</h2>'
        '<p>Rodiče dětí mají nejjednodušší cestu přes sadu základních chráničů v nižší řadě a přes výměnu nebo bazar pro nejrychleji rostoucí kusy. Dospívající hráč už potřebuje juniorské velikosti a bezpečnost se nesmí podceňovat. Dospělý rekreační hráč uspoří, když sáhne po střední řadě a investuje do bruslí a helmy. Brankář si musí počítat, že jeho výbava je samostatný soubor, na který se připravuje delší dobu.</p>'
        '<h2>Jak nakupovat hokejové vybavení online</h2>'
        '<p>Stejný model se v různých obchodech liší dostupnými velikostmi a termínem doručení. Sporteka je proto porovnává na jedné stránce a vy vybíráte podle toho, co vám vyhovuje. U bruslí a helem ověřte před koupí, zda můžete zboží vrátit nebo vyměnit. Po doručení vyzkoušejte brusle doma na koberci a nechte si ostří nabrousit, než vyrazíte na led. Pokud nakupujete výbavu pro dítě, počítejte s tím, že nové vybavení se nasazuje postupně a že ho dítě rychle přeroste.</p>'
        '<p>Nejvíc se hokejové vybavení prodává před začátkem sezóny na přelomu léta a podzimu, kdy bývá nejširší výběr velikostí. Slevy se objevují obvykle po skončení sezóny. Pokud nepotřebujete nejnovější model, hodí se nakupovat mimo sezónu.</p>'
    ),
    faq=[
        ('Jaké hokejové vybavení je nezbytné pro začátek?',
         'Základ tvoří helma s mřížkou, brusle, hokejka, rukavice, chrániče loktů, ramen, kalhoty a chrániče holení. Zapomenout se nesmí ani chránič zubů a suspenzor. Na malých dětech často stačí osvědčená základní sada, kterou postupně doplňujete.'),
        ('Jakou velikost hokejových bruslí vybrat?',
         'Hokejové brusle bývají o jedno až dvě čísla menší než běžná obuv. Rozhodující je délka chodidla a šířka kopyta, proto vždycky porovnejte měření s tabulkou konkrétní značky. Pata musí držet pevně a prsty se mají jen lehce dotýkat špičky.'),
        ('Jak poznám správnou délku hokejky?',
         'Postavte hokejku svisle před sebe na špičku čepele. V bruslích by měl horní konec sahat k bradě, bez bruslí asi k nosu. Hráči v útoku často volí kratší hokejku pro lepší vedení puku, obránci delší pro větší dosah.'),
        ('Co znamená ohebnost hokejky?',
         'Ohebnost, neboli flex, popisuje, jak moc se šaft prohne při střelbě. Příliš tuhá hokejka se začátečníkovi neohne, příliš měkká není přesná. Hodnoty výrobců nejsou jednotné, proto porovnávejte hokejky ve stejné značce a při volbě vezměte v potaz hmotnost hráče.'),
        ('Jak často brousit hokejové brusle?',
         'Záleží na frekvenci hraní a na kvalitě ledu. Brousí se, když ostří přestane kousat, tedy když hráč hůř brzdí nebo se klouže při zatáčení. Pravidelní hráči nechávají brusle brousit častěji než rekreační. Po každém broušení ostří důkladně osušte.'),
        ('Jak dlouho hokejová helma vydrží?',
         'Řiďte se certifikací a datem výroby, které uvádí výrobce, protože materiál časem stárne. Po silnějším nárazu ji vyměňte, i když vypadá celá. Dětské helmy s nastavitelnou velikostí lze používat déle, ale vždy po úpravě zkontrolujte, zda dobře sedí.'),
        ('Jak vyprat hokejové chrániče?',
         'Čistěte je podle štítku, nejčastěji šetrným praním na nízké teplotě nebo ručním omytím. Nesušte je na topení ani v sušičce, protože teplo narušuje pěnu a lepení. Nejlepší je pověsit je na vzdušné místo. Vyhnete se tak plísním a zápachu.'),
        ('Čím se liší brankářská výstroj od hráčské?',
         'Brankář nosí větší chrániče nohou, lapačku, vyrážečku, speciální helmu a brusle s krytem. Výstroj je těžší a musí na sebe navazovat bez mezer. Hráčské chrániče se pro brankáře nehodí, protože nechrání před puky stejným způsobem.'),
        ('Mám kupovat levou, nebo pravou hokejku?',
         'Strana se určuje podle toho, která ruka je při držení hokejky nahoře. Pokud to nevíte, zkuste vést puk oběma způsoby. Pro většinu hráčů je jednoznačně přirozenější jedna varianta. Dětem je dobré nechat vybrat, ve které se jim hraje lépe.'),
        ('Je lepší dřevěná, nebo kompozitová hokejka?',
         'Dřevěná je odolnější a levnější, proto se hodí pro děti a trénink. Kompozitová je lehčí a pružnější, hráč s ní lépe cítí puk. Pro pravidelné hráče a soutěže se obvykle volí kompozit, pro začátky stačí dřevo.'),
        ('Jak nakupovat dětské hokejové vybavení?',
         'Volte bezpečnost a pohodlí, ne velikost „na vyrůstání“. Helmu, brusle a chrániče vybírejte podle aktuálních rozměrů dítěte a po půl roce je znovu zkontrolujte. U rychle rostoucích dětí se vyplatí cenově dostupnější řady.'),
    ])

# ------------------------------------------------------------------ volny-cas
NEW['volny-cas'] = dict(long=True,
    title='Hry a volný čas: šipky, trampolíny, lukostřelba | Sporteka',
    desc='Hry a volný čas: šipky, trampolíny, lukostřelba, hry na zahradu a discgolf. Průvodce výběrem a porovnání nabídek českých obchodů na jednom místě.',
    intro='<p><strong>Hry a volný čas</strong> je kategorie pro všechno, co se hraje pro radost: u stolu, na zahradě, na trávníku i na dětském hřišti. Nepatří sem závodní výbava, spíše vybavení pro rodinná odpoledne, kroužky, hospodské turnaje a letní víkendy. Přesto platí, že kvalitnější kus vydrží víc sezón a hra s ním baví víc než hra s levným náhražkem. Proto se vyplatí chvíli věnovat tomu, co a pro koho vybíráte.</p>'
          '<p>Najdete tu <a href="/sipky/">šipky</a>, <a href="/trampoliny/">trampolíny</a>, <a href="/lukostrelba/">lukostřelbu</a>, <a href="/hry-na-zahradu/">hry na zahradu a pláž</a> a <a href="/discgolf/">discgolf a frisbee</a>. Sporteka porovnává nabídky českých obchodů, takže vidíte dostupnost, doručení i varianty jednoho produktu pohromadě.</p>',
    guide=(
        '<h2>Jak vybírat vybavení pro hry a volný čas</h2>'
        '<p>Na rozdíl od klasických sportů tady nerozhoduje výkon, ale spíš pohodlí, bezpečnost a to, kolik lidí si zahraje. Dobré je začít otázkou, kde a s kým se bude hrát. Něco jiného potřebuje rodina se zahradou, něco jiného byt s jednou volnou zdí a něco jiného parta, která se potkává u stolu v hospodě. Venkovní hry vyžadují odolnost vůči počasí, domácí hry hlavně ochranu zdi a podlahy.</p>'
        '<h3>Přehled podkategorií</h3>'
        + T(['Kategorie', 'Kde se hraje', 'Pro koho'], [
            ['<a href="/sipky/">Šipky</a>', 'doma, v klubu, v hospodě', 'dospělí a starší děti, parta, turnaje'],
            ['<a href="/trampoliny/">Trampolíny</a>', 'zahrada, v hale u menších modelů', 'děti, rodiny, kondiční skákání'],
            ['<a href="/lukostrelba/">Lukostřelba</a>', 'střelnice, zahrada s ochranou', 'začátečníci a hobby střelci'],
            ['<a href="/hry-na-zahradu/">Hry na zahradu a pláž</a>', 'zahrada, pláž, kemp', 'rodiny, společné odpoledne'],
            ['<a href="/discgolf/">Discgolf a frisbee</a>', 'park, louka, hřiště', 'všechny věkové skupiny']]) +
        '<h2>Šipky</h2>'
        '<p>Šipky patří mezi nejoblíbenější domácí hry, protože se dají hrát po práci i o víkendu. Klasické steel šipky mají kovový hrot a hrají se na sisalový terč, soft šipky mají plastový hrot a používají se na elektronický terč. Obojí lze koupit v samostatných kategoriích <a href="/sipkove-terce/">šipkové terče a stojany</a> a <a href="/sipkove-doplnky/">letky, násadky, hroty a pouzdra</a>. Podrobný průvodce najdete na stránce <a href="/sipky/">šipky</a>, tady jen stručně: vybírejte hmotnost podle ruky, začněte spíše lehčími šipkami a terč věšte do správné výšky a vzdálenosti. Na stěnu pod terč patří ochranný kryt, aby se zeď nepoškodila.</p>'
        '<h2>Trampolíny</h2>'
        '<p>Zahradní trampolína je největší položka v této kategorii a také ta, u které se nejvíc vyplácí rozmyslet výběr. Důležitý je průměr, který určuje, kolik se dá skákat a kolik místa potřebujete. Rozhodněte, zda bude na ní skákat jedno dítě, několik dětí, nebo dospělí. Zkontrolujte nosnost a ochrannou síť, která patří na každou trampolínu s dětmi. Rám by měl být z pozinkované oceli a skákací plocha z materiálu odolného proti UV záření. Pružiny musí být kryté měkkým lemem, aby si skákající neprotlačil nohu mezi nimi.</p>'
        '<ul><li>Postavte trampolínu na rovnou plochu s dostatečným volným prostorem všude kolem a nad ní.</li>'
        '<li>Na trampolíně skáče jeden člověk, aby se předešlo srážkám a zranění.</li>'
        '<li>Před zimou zkontrolujte pružiny a síť, případně trampolínu zakryjte.</li>'
        '<li>Po dešti nechte plochu oschnout, mokrá je kluzká.</li></ul>'
        '<p>Mezi nejznámější značky patří ' + B(('insportline', 'Insportline'), ('marimex', 'Marimex'), ('springos', 'Springos')) + '. Pro malé děti existují i menší trampolíny s držadlem pro pokoj. Zahradní trampolínu v zimě zakryjte nebo uložte a řiďte se návodem výrobce k zatížení sněhem; pro děti, které se rády vyřádí venku i v zimě, jsou jinou volbou <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a>.</p>'
        '<h2>Lukostřelba</h2>'
        '<p>Lukostřelba je sport pro trpělivé a soustředěné, který se dá hrát i rekreačně. Pro začátečníky jsou vhodné jednoduché luky s menší silou tahu, které dovolují naučit se techniku bez namáhání. Důležitá je správná velikost luku podle délky tahu a síla, kterou zvládnete natahovat bez třesu. Šípy se vybírají podle délky tahu a síly luku. Střílí se na terč s dostatečně hlubokým zachycovačem, který zastaví šipku, a vždy s bezpečným prostorem za terčem. Ochrana předloktí a prstů zabrání zbytečným zraněním.</p>'
        '<p>V kategorii <a href="/lukostrelba/">lukostřelba</a> najdete luky, šípy, terče i doplňky. Nabízejí je například ' + B(('insportline', 'Insportline'), ('geologic', 'Geologic')) + '. Střelbu na zahradě je potřeba přizpůsobit místním pravidlům a bezpečnosti, nikdy nestřílejte směrem k lidem nebo sousedům.</p>'
        '<h2>Hry na zahradu a pláž</h2>'
        '<p>Do této části patří vybavení, které zvládne každý: koulení, házecí hry, plážové sady, jednoduché míčové hry a další. Takové hry fungují jako společná zábava pro více generací. Kvalitní koule na pétanque nebo házecí kroužky vydrží roky, zatímco lacinější plastové sady se rychle poškodí. U her pro děti hlídejte věkové doporučení a velikost drobných částí. Pokud hrajete na pláži, ocení se barva, která je vidět na písku, a lehké pouzdro pro přenášení.</p>'
        '<p>Do kategorie <a href="/hry-na-zahradu/">hry na zahradu a pláž</a> nabízí produkty například ' + B(('geologic', 'Geologic')) + ' a další výrobci. Společná hra na zahradě se dobře kombinuje s vybavením pro <a href="/kemping/">kemping</a>, takže ji vezmete s sebou i na výlet. Pro rodinné aktivity na hřišti se hodí i <a href="/badminton/">badminton</a> a <a href="/stolni-tenis/">stolní tenis</a>, které jsou jednoduché a levné na vybavení.</p>'
        '<h2>Discgolf a frisbee</h2>'
        '<p>Discgolf spojuje házení disku s principem golfu: hráč se snaží trefit koš na co nejméně hodů. Sada pro začátečníka obvykle obsahuje tři typy disků: driver pro dlouhé hody, midrange pro střední vzdálenosti a putter pro krátké hody a vhazování do koše. Disky se liší stabilitou, tedy tím, jak se za letu stáčejí. Začátečníkům se doporučují pomalejší a méně stabilní (understable) disky, které při slabším hodu letí rovněji. Pro obyčejné házení v parku postačí i klasické frisbee.</p>'
        '<p>V kategorii <a href="/discgolf/">discgolf a frisbee</a> najdete například značky ' + B(('eleven', 'Eleven'), ('aerobie', 'Aerobie'), ('kensis', 'Kensis')) + '. Plastové disky stárnou a po opakovaných nárazech do stromů se mění jejich let; zkušení hráči toho někdy využívají a opotřebený disk nechají jako disk s jiným letem.</p>'
        '<h2>Jak plánovat hry podle ročního období</h2>'
        '<p>Na jaře a v létě se využívají hlavně zahradní hry, trampolína, discgolf a lukostřelba, protože jsou venku nejpříjemnější. Na podzim a v zimě se těžiště přesouvá dovnitř, kde dobře fungují šipky, stolní tenis a společenské hry. Kdo plánuje nákup velké věci, jako je trampolína, ušetří čas tím, že ji pořídí před sezónou a postaví v klidu. Menší hry se hodí jako dárky, protože nezaberou místo a dají se použít okamžitě.</p>'
        '<p>Pokud hrajete hodně venku, myslete na ochranu před sluncem a na přenášení věcí. Lehký batoh na vodu, svačinu a menší hry nebo sadu disků udělá z krátkého výletu pohodlné odpoledne. Ve skupině dětí se osvědčují hry, kde se nesoutěží o výsledek, protože zapojí i menší nebo méně zdatné hráče a nikdo se necítí vyřazený.</p>'
        '<h2>Bezpečnost a zdraví</h2>'
        '<p>U her, při kterých se hází nebo střílí, platí jednoduché pravidlo: vždy kontrolujte prostor za cílem a kolem hráčů. U trampolín dohlížejte na děti, u šipek dbejte na bezpečný odstup od terče a u lukostřelby na pevný zachycovač. Doma hrajte tak, aby kolem nebyly překážky, a mimo cestu ostatních. Při hře venku používejte ochranu před sluncem a dbejte na pitný režim, hlavně v létě. Pro delší pobyt venku se hodí i <a href="/batohy/">batohy</a> na vodu a svačinu.</p>'
        '<h2>Značky v nabídce</h2>'
        '<p>V šipkách vedou ' + B(('harrows', 'Harrows'), ('bull-s', "Bull's"), ('mission', 'Mission'), ('winmau', 'Winmau'), ('unicorn', 'Unicorn'), ('target-darts', 'Target')) + ', v trampolínách ' + B(('insportline', 'Insportline'), ('marimex', 'Marimex'), ('springos', 'Springos')) + ' a v discgolfu ' + B(('eleven', 'Eleven'), ('aerobie', 'Aerobie'), ('kensis', 'Kensis')) + '. Pokud nechcete platit za značku, vybírejte podle parametrů, ne podle loga. Přečtěte si údaje o rozměrech, materiálu a nosnosti, a porovnejte je mezi produkty.</p>'
        '<h2>Péče a skladování</h2>'
        '<ul><li>Venkovní hry skladujte v suchu, aby nekorodovaly kovové části a nesplesnivěly textilie.</li>'
        '<li>Plastové disky a koule chraňte před dlouhým pobytem na přímém slunci.</li>'
        '<li>Luky skladujte nenapnuté, aby se nezničilo vlákno a rameno.</li>'
        '<li>Trampolínu na zimu zakryjte nebo rozeberte, hlavně u modelů bez zimní odolnosti.</li></ul>'
        '<h2>Časté chyby</h2>'
        '<p>Nejčastější chybou je nákup příliš velkého nebo příliš malého výrobku. Trampolína, která se nevejde na zahradu, zůstane v krabici. Šipky, které jsou příliš těžké, ztěžují učení. Luk, který je příliš silný, vede ke špatné technice. Druhou chybou je podceňování bezpečnostních prvků, jako je ochranná síť, kryt terče nebo zachycovač šípů. Třetí chybou je koupě podle ceny bez čtení parametrů, protože stejně vypadající kusy se liší materiálem i odolností.</p>'
        '<h2>Pro koho jaká hra</h2>'
        '<p>Rodiny s dětmi ocení zahradní trampolínu nebo sadu her pro více hráčů. Starší děti a dospívající najdou zábavu v discgolfu, šipkách nebo lukostřelbě pod dohledem. Dospělí, kteří se chtějí po práci odreagovat, začnou šipkami, protože zabírají málo místa a hrát je dá i o samotě. Seniory potěší klidné hry na zahradě bez velké fyzické zátěže, třeba koulení.</p>'
        '<h2>Jak nakupovat online</h2>'
        '<p>Objemné zboží, jako trampolíny nebo stojany, se doručuje jinak než malé balíky. Zkontrolujte tedy cenu dopravy, termín dodání a podmínky pro vrácení. U malých her porovnejte doručení a dostupnost mezi obchody, protože stejný výrobek se v obchodech liší dostupností variant. Přečtěte si parametry, protože stejné jméno může skrývat odlišné rozměry. Před nákupem trampolíny si změřte místo na zahradě, včetně rezervy kolem.</p>'
    ),
    faq=[
        ('Jakou trampolínu vybrat na zahradu?',
         'Rozhoduje průměr, nosnost a to, kolik místa máte. Zkontrolujte ochrannou síť, krytí pružin a pozinkovaný rám. Pro rodiny s menšími dětmi se hodí menší model s vnitřní sítí. Starší děti a dospělí potřebují větší plochu a vyšší nosnost.'),
        ('Je trampolína bezpečná pro děti?',
         'Při správném použití ano, ale vyžaduje dohled. Na trampolíně by měl skákat jen jeden člověk, aby nedošlo ke srážce. Důležitá je ochranná síť, krytí pružin a rovný povrch. Malé děti by neměly skákat bez dospělého.'),
        ('Čím začít, když chci hrát šipky?',
         'Stačí sada steel šipek střední hmotnosti, sisalový terč a ochrana zdi. Začněte lehčími šipkami, aby se technika učila snáz. Terč věšte do správné výšky a respektujte vzdálenost od čáry. Podrobnosti jsou v kategorii šipky.'),
        ('Jaký je rozdíl mezi steel a soft šipkami?',
         'Steel šipky mají kovový hrot a hrají se na sisalový terč. Soft šipky mají plastový hrot a používají se na elektronický terč. Soft šipky jsou obvykle lehčí. Terče pro obě varianty nejsou zaměnitelné.'),
        ('Je lukostřelba vhodná pro začátečníky?',
         'Ano, pokud začínáte s lehčím lukem a držíte se pravidel bezpečnosti. Ideální je vyzkoušet několik hodin pod vedením zkušeného střelce. Luk volte podle délky tahu a síly, kterou zvládnete natáhnout bez třesu.'),
        ('Co je discgolf a čím se liší od frisbee?',
         'Discgolf je hra, při které se házením disku snažíte trefit koš na co nejméně hodů. Používá několik typů disků s různou stabilitou. Frisbee je obyčejný disk na volné házení. Pro začátek discgolfu stačí sada driver, midrange a putter.'),
        ('Kam umístit terč na šipky v bytě?',
         'Vyberte pevnou zeď bez rozvodů a bez cenných předmětů v okolí, nejlépe s ochranným krytem. Střed terče má být 173 cm nad podlahou a hrací čára 237 cm od terče, aby se hrálo podle pravidel. Před terčem nechte volný prostor a zajistěte, aby kolem nechodili lidé.'),
        ('Jak pečovat o zahradní hry a vybavení?',
         'Skladujte je v suchu, chraňte před dlouhým slunečním zářením a po použití očistěte. Kovové části prohlédněte a případně natřete, textilní sítě vyperte. Plastové disky a koule stačí opláchnout. Luky skladujte nenapnuté.'),
        ('Jaké hry hrát s celou rodinou?',
         'Dobře fungují koulení, házecí hry, badminton, stolní tenis, frisbee a trampolína pro děti. Důležité je, aby se hra dala hrát na různých úrovních dovedností, takže zvládnou hrát děti i dospělí.'),
        ('Na co se zaměřit při online nákupu objemných her?',
         'Zkontrolujte rozměry, nosnost, hmotnost a způsob doručení. Zjistěte, zda jde zboží vrátit, a porovnejte, jak obchody účtují dopravu. Před nákupem změřte místo, kam zboží umístíte, a připočtěte bezpečnostní rezervu.'),
    ])

# ------------------------------------------------------------------ merino-tricka
NEW['merino-tricka'] = dict(long=True,
    title='Merino trička a tílka: pánská, dámská, dětská | Sporteka',
    desc='Merino trička a tílka: výběr gramáže, střihu a velikosti, péče a značky. Porovnejte nabídky českých obchodů a vyberte první vrstvu na sport i cestování.',
    intro='<p><strong>Merino triko</strong> je vrstva, kterou lidé kupují jednou a pak nechtějí nosit nic jiného. Vlna z merino ovcí je jemnější než běžná vlna, takže nedrbe, a přitom reguluje teplotu: v chladu zahřívá, v teple pomáhá odvádět vlhkost. Triko po dni nošení nezapáchá tak rychle jako syntetika a dá se vyvětrat místo praní.</p>'
          '<p>Na Sportece porovnáte nabídky <strong>merino triček a tílek</strong> z českých obchodů a přitom vidíte rozdíly v gramáži, střihu i značce, což je u merina důležité, protože dvě podobně vypadající trička mohou sloužit zcela odlišně. Navazuje na ně celé <a href="/merino/">merino oblečení</a>, včetně <a href="/merino-pradlo/">merino prádla a legín</a>, <a href="/merino-ponozky/">merino ponožek</a>, <a href="/merino-mikiny/">merino mikin a svetrů</a> a <a href="/merino-doplnky/">merino čepic, nákrčníků a rukavic</a>.</p>',
    guide=(
        '<h2>Proč merino a komu se hodí</h2>'
        '<p>Merino vlákno je tenké a poddajné, proto se při kontaktu s kůží nepíchá jako hrubá vlna. Vlákna zároveň pojmou vlhkost, aniž by se tělo cítilo mokré, a pomalu ji odpařují. Na vlně se hůř usazují bakterie, a proto triko dlouho nezapáchá. Hodí se tedy pro lidi, kteří chodí na hory, cestují s malým zavazadlem, mají sedavé zaměstnání s dojížděním na kole, nebo jednoduše chtějí funkční triko do každého počasí.</p>'
        '<p>Merino ale není všelék. V extrémním horku při intenzivním výkonu může být někomu příjemnější syntetické triko, které schne rychleji. Merino je také citlivější na mechanické poškození než polyester a při neopatrné péči se může srazit. Proto je dobré vědět, co od něj čekat, a podle toho vybrat gramáž a složení.</p>'
        '<h3>Gramáž a sezóna</h3>'
        '<p>Gramáž udává hmotnost materiálu na metr čtvereční a určuje, jak je triko tenké a hřejivé. Platí hrubé vodítko: lehčí triko se hodí do tepla a na pohyb, těžší do chladna a pro pomalejší aktivity. Hodnoty různých výrobců se ale liší a stejná gramáž může u jedné značky působit jinak než u jiné, protože záleží i na plétení a směsi.</p>'
        + T(['Gramáž', 'Typické použití', 'Poznámka'], [
            ['lehká', 'léto, běh, kolo, cestování', 'rychle schne, ale méně hřeje'],
            ['střední', 'celoroční turistika, městské nošení', 'nejuniverzálnější volba'],
            ['těžká', 'zima, hory, nehybné aktivity', 'jako první vrstva pod fleece nebo bundu']]) +
        '<h3>Střih a délka rukávu</h3>'
        '<p>Merino funguje nejlépe, když je blízko pokožky, proto se jako první vrstva vybírá přiléhavý střih. Volné triko hřeje o něco hůř, ale lépe se nosí jako běžné denní oblečení. Krátký rukáv je volbou na léto a pro běh, dlouhý rukáv chrání před sluncem, chladem a komáry. Tílka se hodí pro horké dny a jako spodní vrstva pod lehkou košili. Zvolte i délku podle použití: kdo jezdí na kole, ocení delší záda.</p>'
        '<ul><li>Pro běh vybírejte lehké triko s plochými švy, které netřou.</li>'
        '<li>Pro turistiku pod batohem dává smysl střední gramáž a přiléhavý střih.</li>'
        '<li>Na každý den stačí volnější střih s dobře padnoucím límcem.</li>'
        '<li>V zimě se hodí dlouhý rukáv a rolák nebo zip u krku.</li></ul>'
        '<h2>Složení: čisté merino, nebo směs</h2>'
        '<p>Čisté merino je nejjemnější a nejpřirozenější, ale je i méně odolné proti oděru. Směsi s nylonem nebo polyesterem jsou pevnější, rychleji schnou a lépe drží tvar. Často se používá jádrové předení, kde je syntetické vlákno obalené vlnou. Navenek se tak triko cítí jako vlna, zevnitř ho zpevňuje pevné jádro. Pro hodně opotřebovávané triko, třeba pod batohem, je směs rozumnější. Pro každodenní nošení a cestování je čisté merino komfortnější.</p>'
        + T(['Složení', 'Výhody', 'Nevýhody'], [
            ['čisté merino', 'jemnost, pohodlí, málo zápachu', 'nižší odolnost, delší schnutí'],
            ['merino se syntetikou', 'pevnost, rychlejší schnutí', 'o něco méně přírodní pocit'],
            ['merino s dalšími vlákny', 'pružnost nebo hedvábný omak', 'záleží na konkrétním výrobku']]) +
        '<h2>Velikost a střih podle postavy</h2>'
        '<p>Velikost vybírejte podle tabulky konkrétní značky, ne podle obvyklého čísla v jiné značce. Změřte obvod hrudníku a porovnejte. Merino se při nošení mírně roztáhne, proto je lepší volit přesnou velikost, ne větší. Ženy by měly zvolit dámský střih, protože je zúžený v pase a rukávy jsou kratší. Děti potřebují trochu volnější střih s rezervou na růst, ale ne příliš velký, aby triko přiléhalo.</p>'
        '<h2>Merino pro děti a pro cestování</h2>'
        '<p>Dětské merino trička jsou oblíbená na zimní sporty a v mrazivém počasí. Jsou jemná, nedrbou a děti je snášejí lépe než hrubší vlnu. Vyberte podle výšky dítěte a nechte si malou rezervu na růst. Merino triko se také hodí na cestování. Zabírá málo místa, nemusí se prát po každém dni a po vyvětrání je znovu připravené k nošení. Dva až tři kusy tak často stačí na týdenní výlet.</p>'
        '<h2>Pro sport a každodenní nošení</h2>'
        '<p>Merino triko se dá kombinovat s dalšími vrstvami. Na běh stačí samotné lehké triko, na zimní túru se přidá <a href="/funkcni-mikiny/">funkční mikina</a> nebo <a href="/fleecove-mikiny/">fleecová mikina</a>. Pokud potřebujete spodní vrstvu i pro ostatní části těla, podívejte se na <a href="/termopradlo/">funkční a termo prádlo</a>. V kategorii <a href="/funkcni-tricka/">funkční trička</a> a <a href="/sportovni-tricka/">sportovní trička a tílka</a> najdete syntetické varianty, které se hodí při maximálním výkonu a v horku. Pro vodu a slunce slouží <a href="/lycra-a-uv-tricka/">lycra a UV trička do vody</a>.</p>'
        '<h2>Vrstvení: kam merino triko zapadá</h2>'
        '<p>Merino triko se obvykle nosí jako první vrstva přímo na těle. Nad ním následuje izolační vrstva, například fleece nebo lehká péřová mikina, a navrch ochranná bunda proti větru a dešti. Takový systém se hodí na hory, protože umožňuje vrstvy přidávat a ubírat podle počasí. První vrstva přitom nemusí být tlustá. Důležité je, aby přiléhala a odváděla vlhkost, jinak se pot hromadí a tělo se v klidu rychle ochladí.</p>'
        '<p>Při pohybu v teple lze merino triko nosit samotné. Ve městě se dobře kombinuje s košilí nebo s lehkým svetrem. Pod batohem pomáhá, když jsou ramena a záda v kontaktu s hladkým materiálem bez švů. Pokud nosíte těžký batoh, hlídejte, aby popruhy netřely stále na stejném místě, protože vlna je k oděru citlivější než syntetika.</p>'
        '<h2>Značky v nabídce</h2>'
        '<p>Největší nabídku mají ' + B(('icebreaker', 'Icebreaker'), ('sensor', 'Sensor'), ('lasting', 'Lasting'), ('smartwool', 'Smartwool'), ('helly-hansen', 'Helly Hansen'), ('devold', 'Devold'), ('progress', 'Progress'), ('viking', 'Viking'), ('mons-royale', 'Mons Royale'), ('woolcano', 'Woolcano')) + '. Icebreaker a Smartwool se specializují právě na merino, Sensor a Lasting nabízejí české a slovenské varianty v širším rozsahu gramáží. Devold a Helly Hansen mají severskou tradici vlněného prádla, Mons Royale je spojený s lyžováním a cyklistikou.</p>'
        '<h2>Péče o merino triko</h2>'
        '<p>Správná péče prodlužuje životnost víc než cokoli jiného. Merino se nejlépe pere na nízkou teplotu a jemný program, nejlépe v praní pro vlnu nebo v síťce. Používejte jemný prací prostředek bez zjasňovačů. Aviváž se nedoporučuje, protože zalepuje vlákna a snižuje schopnost odvádět vlhkost. Sušte na vzduchu mimo přímé slunce a topení, v sušičce se merino snadno sráží. Mezi jednotlivými nošeními stačí triko vyvětrat.</p>'
        '<ul><li>Pro čištění skvrn použijte vlažnou vodu a jemný prostředek.</li>'
        '<li>Při praní nepoužívejte vysoké odstřeďování.</li>'
        '<li>Nepoužívejte bělidla ani aviváže.</li>'
        '<li>Aby triko vydrželo, hlídejte tření popruhů batohu a dbejte na to, aby se nedřelo o hrubé součástky.</li>'
        '<li>Díry od molů předejdete skladováním v čistém a suchém prostředí.</li></ul>'
        '<h2>Časté chyby při výběru</h2>'
        '<p>První chybou je koupě příliš těžkého trika pro letní použití, které pak působí horko. Druhou je volný střih jako první vrstva, který nepřiléhá a nefunguje tak, jak má. Třetí chybou je nákup podle ceny bez ohledu na složení, protože směs se syntetikou se opotřebuje jinak než čisté merino. Čtvrtou je praní při příliš vysoké teplotě, které způsobí srážení. Vyhnout se jim pomůže čtení štítku a porovnání parametrů v nabídce.</p>'
        '<h2>Pro koho jaké merino triko</h2>'
        '<p>Běžec ocení lehké triko s plochými švy a krátkým rukávem. Turista si vybere střední gramáž s dlouhým rukávem. Cestovatel potřebuje čisté merino v neutrální barvě, které se dobře kombinuje. Lyžař nebo skialpinista bude chtít těžší gramáž s límcem. Dítě potřebuje měkké, dobře padnoucí triko s rezervou, a ten, kdo hledá triko do práce, vybere střih blízký běžnému tričku.</p>'
        '<h2>Merino na túře a při běhu</h2>'
        '<p>Pro delší túry a běh s vestou se merino hodí díky tomu, že netrpí zápachem při vícedenním používání. Pod <a href="/turisticke-batohy/">turistickým batohem</a> nebo <a href="/bezecke-vesty-a-batohy/">běžeckou vestou</a> se vyplatí přiléhavý střih bez záhybů a na vícedenní akce střídání dvou kusů, aby se vlákna nenamáhala stále na stejných místech.</p>'
        '<h2>Jak nakupovat chytře</h2>'
        '<p>Stejné triko se v různých obchodech liší dostupností velikostí i barev. Na Sportece vidíte nabídky vedle sebe a můžete vybrat obchod, který vám vyhovuje. Při porovnání se dívejte na gramáž, složení a střih, ne jen na název modelu. Výhodné nákupy jsou obvykle mimo sezónu, kdy se vyprodávají předchozí kolekce. Pokud potřebujete více kusů, vybírejte stejnou značku, aby sedělo velikostní značení.</p>'
    ),
    faq=[
        ('Jaká gramáž merino trička je nejuniverzálnější?',
         'Pro celoroční nošení se nejlépe osvědčuje střední gramáž. Lehká se hodí do léta a na běh, těžší do zimy a pro pomalejší aktivity. Hodnoty výrobců se liší, proto porovnávejte i střih a složení.'),
        ('Nepíchá merino triko?',
         'Kvalitní merino má jemná vlákna a nedrbe jako hrubá vlna. Citlivost je ale individuální. Pokud máte velmi citlivou pokožku, začněte lehčím a jemnějším trikem a vyzkoušejte ho doma.'),
        ('Jak prát merino triko?',
         'Perte na nízkou teplotu na jemný program, nejlépe v síťce a s prostředkem pro vlnu. Nepoužívejte aviváž ani bělidlo. Sušte na vzduchu mimo topení a přímé slunce. Mezi nošením stačí triko vyvětrat.'),
        ('Srazí se merino při praní?',
         'Může, pokud ho perete při vysoké teplotě, silně odstřeďujete nebo sušíte v sušičce. Při respektování pokynů na štítku se obvykle nesráží. Směsi se syntetikou drží tvar lépe než čisté merino.'),
        ('Je lepší čisté merino, nebo směs?',
         'Čisté merino je jemnější a příjemnější, ale méně odolné. Směs se syntetikou je pevnější a rychleji schne. Na intenzivní sport a pod batoh se hodí směs, na každodenní nošení a cestování čisté merino.'),
        ('Jak poznám správnou velikost?',
         'Změřte obvod hrudníku a porovnejte s tabulkou konkrétní značky. Pro funkci první vrstvy volte přiléhavý střih, nikoli větší velikost. Ženám sedí dámský střih lépe než pánský.'),
        ('Hodí se merino triko i do horka?',
         'Lehká gramáž dobře odvádí vlhkost a pomáhá udržet pohodlí, takže ji lze nosit i v teple. U extrémně intenzivního výkonu ale někomu vyhovuje syntetické triko, které schne rychleji.'),
        ('Proč merino nezapáchá?',
         'Na vlněných vláknech se hůř množí bakterie a vlákno pojme vlhkost uvnitř vlákna, takže zápach vzniká později než u syntetických materiálů. Po delším nošení ale i merino potřebuje vyprat.'),
        ('Je merino triko vhodné pro děti?',
         'Ano, dětské merino je jemné a hřeje i při vlhku. Hodí se pod zimní oblečení. Vyberte velikost podle výšky dítěte s malou rezervou a perte podle pokynů na štítku.'),
        ('Kolik merino triček potřebuji na cestu?',
         'Pro týdenní cestu často stačí dva až tři kusy, protože merino stačí vyvětrat. Vybírejte neutrální barvy, které se dobře kombinují, a vezměte jeden kus s dlouhým rukávem pro chladnější večery.'),
    ])

# ------------------------------------------------------------------ sipky
NEW['sipky'] = dict(long=True,
    title='Šipky a šipkové terče: steel, soft, doplňky | Sporteka',
    desc='Šipky, terče a doplňky: steel i soft šipky, sisalové terče, letky, násadky a pouzdra. Průvodce výběrem a nabídky českých obchodů na jednom místě.',
    intro='<p><strong>Šipky</strong> jsou hra, kterou zvládne začít kdokoli, ale kvalitní vybavení rozdíl znát je. Šipka, která vám sedí v ruce, letí rovněji, terč, který nezničí hroty, vydrží roky a správné doplňky dokážou ušetřit nervy při každé hře. Nabídka je široká a pro nováčka často nepřehledná, protože se v ní míchají pojmy jako barrel, letka, steel a soft. Začátečník by přitom měl řešit hlavně hmotnost šipky, typ hrotu a typ terče, protože ty určují, jak se bude hrát.</p>'
          '<p>Na Sportece najdete <a href="/sipkove-terce/">šipkové terče a stojany</a> i <a href="/sipkove-doplnky/">letky, násadky, hroty a pouzdra na šipky</a>. Sporteka porovnává nabídky českých obchodů, takže vidíte, kde je daná šipka dostupná a v jaké variantě. Tento průvodce ukáže, jak vybrat hmotnost, tvar, hrot i terč.</p>',
    guide=(
        '<h2>Steel, nebo soft: dva světy šipek</h2>'
        '<p>Dva základní typy šipek se liší hrotem a terčem. Steel šipky mají kovový hrot a hrají se na sisalový terč. Používají se v klasických turnajích, kluby a hospody je znají nejlépe. Soft šipky mají plastový hrot a používají se na elektronický terč, který počítá body sám. Obě varianty nejsou vzájemně zaměnitelné, protože kovový hrot by poškodil elektronický terč a plastový by v sisalu nedržel.</p>'
        + T(['Typ', 'Hrot', 'Terč', 'Typické prostředí'], [
            ['Steel', 'kovový', 'sisalový', 'kluby, hospody, domácí trénink'],
            ['Soft', 'plastový', 'elektronický', 'domácí hra, party, herny']]) +
        '<p>Soft šipky bývají lehčí než steel. Steel šipky se typicky vyrábějí zhruba od 18 do 28 gramů, soft šipky bývají do 20 gramů, takže u steel je větší prostor pro výběr. Pokud nevíte, kterou hru zvolit, začněte tou, ke které máte terč.</p>'
        '<h2>Hmotnost šipky</h2>'
        '<p>Hmotnost šipky se udává v gramech a určuje, jak rychle a po jaké dráze letí. Lehčí šipka letí rychleji a po plošší dráze, těžší pomaleji a stabilněji. Žádná hmotnost není ta pravá pro všechny. Záleží na síle hodu, stylu a zvyku. Začátečník by měl zkusit několik hmotností a vybrat tu, ve které se mu hází nejpohodlněji. Příliš těžká šipka se při hodu stáčí dolů, příliš lehká se pohybuje nepředvídatelně.</p>'
        '<h2>Tělo šipky a úchop</h2>'
        '<p>Tělo šipky, anglicky barrel, je část, kterou držíte. Může být hladké, rýhované, vroubkované nebo s hrubším povrchem. Čím výraznější povrch, tím pevnější úchop, ale u hrubších těl hrozí otlaky na prstech. Tvar může být válcový, torpédový nebo kuželový. Různá poloha těžiště mění, jak šipka letí: těžiště vpředu vytváří plošší dráhu, vzadu dráhu zakřivenější.</p>'
        '<ul><li>Válcový tvar má stejnou tloušťku po celé délce a je oblíbený u začátečníků.</li>'
        '<li>Torpédový tvar má těžiště vpředu, šipka se při letu chová stabilně.</li>'
        '<li>Delší a tenčí těla se hodí pro hráče, kteří mají jemnější úchop.</li>'
        '<li>Materiál ovlivňuje hustotu: wolframové šipky jsou štíhlejší než mosazné stejné hmotnosti.</li></ul>'
        '<h2>Materiál: mosaz, nikl, wolfram</h2>'
        '<p>Šipky se vyrábějí z několika kovů. Mosaz je dostupná a snadno obrobitelná, ale protože je méně hustá, je šipka při dané hmotnosti objemnější. Nikl-stříbro je kompromis. Wolframové slitiny jsou nejhustší, takže šipka stejné hmotnosti je štíhlejší a hráč může umístit více šipek těsně vedle sebe. Wolframové šipky jsou obvykle pro náročnější hráče, ale začátečník si vystačí i s mosazí. Povrch může být upravený, například niklováním, kterým se zlepšuje vzhled a odolnost.</p>'
        '<h2>Letky a stonky</h2>'
        '<p>Letka stabilizuje let šipky a stonek spojuje letku s tělem. Tvar letky mění chování: větší letka brzdí a stabilizuje, menší letka je rychlejší, ale vyžaduje čistší hod. Standardní tvar je klasický, ale existují i slim, kite a fantail. Stonky se liší délkou a materiálem: delší stonek zvedá zadní konec a mění úhel šipky, kratší jej snižuje. Zkoušením kombinací zjistíte, jak se šipka chová. Tyto součásti najdete v kategorii <a href="/sipkove-doplnky/">letky, násadky, hroty a pouzdra</a>.</p>'
        + T(['Součást', 'Co ovlivňuje', 'Co zkoušet'], [
            ['Letka', 'stabilita a rychlost letu', 'velikost a tvar'],
            ['Stonek', 'úhel a vyvážení šipky', 'délka a materiál'],
            ['Hrot', 'zapíchnutí a odskok', 'délka, povrch, typ'],
            ['Pouzdro', 'ochrana při přenášení', 'velikost a počet šipek']]) +
        '<h2>Terč a jeho umístění</h2>'
        '<p>Klasický terč je vyrobený ze sisalových vláken, které se po zásahu uzavírají a hroty se do nich zapichují bez poškození. Kvalitnější terč vydrží déle a má méně odskoků. Podstatný je i drát, který rozděluje pole: tenký drát způsobuje méně odskoků. Pro domácí hru potřebujete pevný závěs a ochranu zdi. Terč pověste tak, aby jeho střed byl ve výšce 173 cm od podlahy, a čáru pro hod vyznačte ve vzdálenosti 237 cm měřené vodorovně od terče. Tyto rozměry platí pro steel i soft, u soft her se někdy hraje z kratší vzdálenosti, proto si je případně ověřte podle pravidel dané soutěže. Nabídku najdete v kategorii <a href="/sipkove-terce/">šipkové terče a stojany</a>.</p>'
        '<p>Elektronický terč počítá body automaticky, hodí se pro soft šipky a hry s rodinou, protože se nemusí zapisovat. Vybírejte podle počtu hráčů a her, které nabízí, i podle odolnosti plastových polí. Důležitý je zdroj napájení a výměnné segmenty.</p>'
        '<h2>Doplňky a výbava</h2>'
        '<ul><li><strong>Pouzdro</strong> chrání šipky při přenášení a drží letky pohromadě.</li>'
        '<li><strong>Náhradní hroty</strong> se hodí, protože se zničí o prkna a kov.</li>'
        '<li><strong>Letky a stonky</strong> si pořiďte do zásoby, hlavně pokud často trefujete šipky mezi sebou.</li>'
        '<li><strong>Kryt na zeď</strong> chrání omítku a nepouští šipky do dveří a nábytku.</li>'
        '<li><strong>Brousek na hroty</strong> udržuje špičku ostrou, aby neodskakovala.</li></ul>'
        '<h2>Značky v nabídce</h2>'
        '<p>Největší nabídku mají ' + B(('harrows', 'Harrows'), ('bull-s', "Bull's"), ('mission', 'Mission'), ('winmau', 'Winmau'), ('unicorn', 'Unicorn'), ('shot', 'Shot'), ('target-darts', 'Target'), ('red-dragon', 'Red Dragon'), ('designa', 'Designa'), ('condor', 'Condor'), ('windson', 'Windson')) + '. Harrows, Winmau, Unicorn a Target jsou známé šipkařské značky se širokým rozsahem od základních po náročné modely. Bull\'s, Designa a Condor nabízejí doplňky a vybavení pro rekreační i klubové hráče. Red Dragon a Shot se zaměřují na šipky a doplňky pro turnajové hráče.</p>'
        '<h2>Jak začít</h2>'
        '<p>Pro první týdny stačí sada steel šipek střední hmotnosti, sisalový terč a ochrana zdi. Postupně vyzkoušejte lehčí i těžší šipky a různé letky, ale měňte vždy jen jednu věc najednou, abyste věděli, co způsobilo rozdíl. Hrajte pravidelně a krátce, protože technika se učí opakováním. Naučte se základní hry a počítání bodů, které se stupňují od jednoduchých her až po klasickou 501.</p>'
        '<h2>Péče o šipky a terč</h2>'
        '<p>Šipky po hře očistěte suchým hadříkem a skladujte v pouzdře. Hroty kontrolujte a ostré špičky udržujte. Šroubové spoje dotahujte, aby se šipka nerozpadala za letu. Letky vyměňte, pokud se ohnou nebo roztřepí. Terč občas pootočte, aby se zásahy rozložily rovnoměrně a vlákna se nevytlačila na jednom místě. Skladujte ho v suchu a mimo přímé slunce.</p>'
        '<h2>Časté chyby</h2>'
        '<ul><li>Příliš těžké šipky hned na začátku. Lehčí se lépe učí technika.</li>'
        '<li>Terč ve špatné výšce nebo vzdálenosti. Dodržujte rozměry hry.</li>'
        '<li>Hra bez ochrany zdi. Kryt zabrání poškození omítky.</li>'
        '<li>Používání steel šipek na elektronický terč. Poškodí ho.</li>'
        '<li>Neustálé měnění vybavení. Technika se zlepšuje spíš tréninkem než novými šipkami.</li></ul>'
        '<h2>Nejčastější hry a počítání</h2>'
        '<p>Nejznámější hrou je 501: každý hráč začíná na 501 bodech a odečítá si hozené body, přičemž hru musí ukončit zásahem do zdvojnásobujícího pole, takzvaného double. Existují i varianty 301 pro rychlejší hru. Další oblíbená hra se jmenuje cricket a spočívá v zavírání čísel od patnácti do dvacítky a středu terče. Hodí se pro hráče s různou úrovní, protože hra není tak závislá na vysokém skóre. Pro trénink přesnosti se používá házení na jedno číslo, dokud se nezasáhne třikrát. Při hře ve více lidech dává smysl psát body na tabulku, která se dá koupit jako doplněk.</p>'
        '<p>Základem technického zlepšení je stálé postavení a uvolněný hod. Nohy se staví stabilně, hodnotný je stálý úchop a dokončení pohybu v dráze šipky. Kdo hraje pravidelně, brzy pozná, že velkou roli hraje rytmus, a proto je lepší hrát častěji a kratší dobu, než jednou týdně dlouho.</p>'
        '<h2>Šipky jako součást volného času</h2>'
        '<p>Šipky jsou jednou z mnoha her, které jdou hrát doma i v kolektivu. Celý přehled najdete v kategorii <a href="/volny-cas/">hry a volný čas</a>. Na zahradu se hodí <a href="/hry-na-zahradu/">hry na zahradu a pláž</a>, pro rodinné odpoledne i <a href="/stolni-tenis/">stolní tenis</a> a <a href="/badminton/">badminton</a>. Pro rozvoj přesnosti a soustředění můžete zkusit <a href="/lukostrelba/">lukostřelbu</a>, pro děti s přebytkem energie <a href="/trampoliny/">trampolíny</a> a pokud preferujete hru venku, <a href="/discgolf/">discgolf a frisbee</a>.</p>'
        '<h2>Jak nakupovat online</h2>'
        '<p>Šipky jsou malé zboží, ale rozdíly mezi variantami jsou velké. Před koupí zkontrolujte hmotnost, materiál, délku těla i typ hrotu. U terčů se dívejte na typ, rozměr a způsob uchycení. Sporteka porovnává nabídky obchodů a ukazuje vám stejné produkty vedle sebe. Pokud si nejste jistí, začněte s jednou levnější sadou a po několika týdnech zkuste jinou hmotnost nebo tvar. Pozor na nabídky šipek v sadách: mohou obsahovat jednoduchá pouzdra a letky nižší kvality.</p>'
    ),
    faq=[
        ('Jaké šipky vybrat pro začátečníka?',
         'Pro začátek se hodí steel šipky střední hmotnosti s válcovým tělem a běžnými letkami. Důležitější než značka je pohodlný úchop. Vyzkoušejte několik hmotností a vyberte tu, ve které se vám hází nejsnáz.'),
        ('Jaký je rozdíl mezi steel a soft šipkami?',
         'Steel šipky mají kovový hrot a hrají se na sisalový terč. Soft šipky mají plastový hrot a patří na elektronický terč. Nejsou zaměnitelné. Soft šipky bývají lehčí.'),
        ('Jakou hmotnost šipek zvolit?',
         'Neexistuje univerzální hmotnost. Lehčí šipky letí rychleji a po plošší dráze, těžší jsou stabilnější. Začátečník by měl zkusit několik hmotností a vybrat tu, kde je hod přirozený.'),
        ('Z čeho jsou šipky nejlepší?',
         'Mosazné šipky jsou cenově dostupné, ale objemnější. Niklové a wolframové jsou hustší, takže štíhlejší při stejné hmotnosti. Wolframové volí náročnější hráči, začátečník si vystačí i s mosazí.'),
        ('Do jaké výšky a vzdálenosti věšet terč?',
         'Střed terče se věší do výšky a vzdálenosti určené pravidly hry. Konkrétní rozměry si ověřte v oficiálních pravidlech, protože se liší pro steel a soft. Doma si vyznačte čáru pro hod podlahovou páskou.'),
        ('Jak často měnit letky a hroty?',
         'Letky vyměňte, když se ohnou nebo roztřepí a šipka začne létat nepravidelně. Hroty kontrolujte a při ohnutí nebo ztupení je vyměňte. Dobré je mít vždy zásobu náhradních dílů.'),
        ('Je lepší sisalový, nebo elektronický terč?',
         'Sisalový terč je klasický, odolný a používá se se steel šipkami. Elektronický počítá body, hodí se pro soft šipky a rodinnou hru. Vyberte podle toho, jaký typ hry preferujete a kde hrajete.'),
        ('Jak ochránit zeď při hře doma?',
         'Použijte ochranný kryt nebo desku kolem terče, která zachytí odskoky. Zeď za terčem by měla být pevná. Dbejte i na to, aby v dosahu hodu nebylo okno nebo dveře.'),
        ('K čemu je pouzdro na šipky?',
         'Pouzdro chrání hroty a letky při přenášení a drží šipky pohromadě. Bez něj se snadno ohnou letky nebo poškodí hroty. Hodí se hlavně pro hráče, kteří šipky berou s sebou do klubu.'),
        ('Mohu kombinovat díly různých značek?',
         'Ano, většina letek, stonků a hrotů je kompatibilní podle velikosti závitu. Vždy ale zkontrolujte typ závitu a délku. Kombinováním dílů si můžete šipku doladit podle sebe.'),
    ])
