"""sporteka.cz — seasonal guides, wave 1c (16. 11. 2026): winter with kids, ice skates, nutrition for beginners.
General, true facts only; no prices, no studies; health claims only in the wording of EU-authorised claims."""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------------------------------------------------------------
GUIDES['zimni-radovanky-s-detmi'] = dict(
    name='Zimní radovánky s dětmi',
    h1='Sáňky, boby, nebo kluzák? Zimní radovánky s dětmi',
    seo_title='Zimní radovánky s dětmi: sáňky, boby, kluzák, oblečení',
    seo_desc='Jak vybrat sáňky, boby nebo kluzák podle věku dítěte, jak se obléct do mrazu a jak zůstat v bezpečí na kopci. Přehled nabídek českých e-shopů.',
    intro_html=(
        '<p>První sníh umí rodinu vytáhnout z domu rychleji než cokoli jiného. Jenže hned první víkend se ukáže, že čtyřletému dítěti '
        'se na dlouhých bobech nelíbí, osmiletému zase přijdou malé sáňky nudné a rodič stojí na kopci a nemůže se zahřát. '
        'Dobré vybavení na zimu nemusí být rozsáhlé, ale mělo by odpovídat věku dětí a tomu, kam s nimi jezdíte.</p>'
        '<p>Průvodce prochází jednotlivé věci v pořadí, v jakém se o nich obvykle rozhoduje: <a href="#sane-a-boby">čím se budete spouštět z kopce</a>, '
        'jak dítě obléct, aby mu nebyla zima, ale ani se nepotilo, co si dát na hlavu a na ruce a co pomůže rodičům, kteří stojí dole. '
        'Sporteka sama nic neprodává, jen porovnává nabídky českých e-shopů. Cenu a dostupnost uvidíte vedle sebe a nakupujete přímo v obchodě, který vám vyhovuje.</p>'
    ),
    sections=[
        dict(h2='Sáňky, boby, kluzák nebo talíř: co se hodí na jaký věk', html=(
            '<p>Všechny čtyři věci kloužou po sněhu, ale každá jinak. Liší se tím, jak se řídí, jak se brzdí a kolik toho po dítěti chtějí. '
            'Menším dětem se hodí to, co je pevně drží a co jede přímo. Starší děti hledají rychlost a možnost zatáčet.</p>'
            + T(['Typ', 'Řízení', 'Brzdění', 'Pro jaký věk'], [
                ['Sáňky s opěrkou a vodítkem', 'Táhne dospělý, dítě neřídí', 'Brzdí dospělý, nebo dítě patami', 'Batolata a předškoláci, nejlépe s popruhem a zábranou'],
                ['Klasické dřevěné nebo plastové sáňky', 'Přenášením váhy nebo tahem za provaz', 'Nohama, u dětí často jen výběhem', 'Zhruba od předškolního věku podle zkušeností dítěte'],
                ['Boby s volantem nebo řídítky', 'Volant, řídítka nebo lanka', 'Páka nebo brzdy, jejich kvalitu je dobré vyzkoušet', 'Obvykle školáci, u malých jen s dospělým'],
                ['Kluzák (sněhový kluzák, kluzák s řídítky)', 'Řídítky nebo naklánění', 'Patami a vahou', 'Starší děti a teenageři, kteří už zvládnou ovládat rychlost'],
                ['Talíř nebo plastový kruh', 'Žádné, točí se', 'Žádné', 'Mírný a krátký svah s dlouhým rovným výběhem bez překážek'],
            ]) +
            '<p>Údaj o věku u konkrétního produktu si vždy ověřte. Výrobci ho uvádějí rozdílně a dítě stejného věku může být výrazně menší nebo větší, '
            'než odpovídá tabulce. Hmotnostní limity a rozměry najdete v popisu produktu.</p>'
        )),
        dict(h2='Sáně a boby: co sledovat před koupí', cat='sane-a-boby', n=6, html=(
            '<p>V kategorii <a href="/sane-a-boby/">sáně a boby</a> je široký výběr od plastových sáněk po dřevěné. '
            'Při srovnávání se vyplatí dívat se na několik věcí, které na fotografii nepoznáte. Plast je lehký a odolný vůči vlhku, '
            'ale v mrazu může být křehčí a při nárazu může prasknout. Dřevo je tradiční a dobře se opravuje, jenže vyžaduje trochu péče a dřevěné sáňky jsou těžší. '
            'U sáněk pro nejmenší pomáhá opěrka zad, popruh nebo zábrana, která dítě drží. K tahání se hodí pevný provaz, který dobře padne do ruky.</p>'
            '<p>Boby s řízením je potřeba vyzkoušet. Zjistěte, jak fungují brzdy, a dítěti ukažte, jak se používají. Sáně a boby, například od značky '
            '<a href="/znacka/merco/">Merco</a>, se prodávají v několika velikostech, takže zvolte takovou, která vyhovuje nejen dítěti, ale i autu nebo sklepu. '
            'Sáně, které se skládají, se lépe vozí a skladují.</p>'
        )),
        dict(h2='Kluzáky na sníh', cat='kluzaky-na-snih', n=4, html=(
            '<p>Kluzák je pro děti, které už sáňky přerostly a chtějí něco rychlejšího. Podle typu se na něm sedí nízko a řídí řídítky, nebo se jezdí vkleče či vleže. '
            'Najdete je v kategorii <a href="/kluzaky-na-snih/">kluzáky na sníh</a>. Protože se jezdí rychleji, patří k nim vždy helma a pevné rukavice. '
            'Před koupí zkontrolujte, jak je kluzák ovladatelný a jestli se dá brzdit patami, což je pro děti nejjednodušší a nejpřirozenější způsob.</p>'
            '<p>Kluzáky jsou obvykle krátké a lehké, takže se s nimi děti rychle naučí zacházet. Jsou ale také náročné na terén: potřebují sjetý, ne příliš hluboký sníh a svah s bezpečným výběhem. '
            'Na ledovém povrchu jedou rychle a těžko se zastavují.</p>'
        )),
        dict(h2='Bezpečnost na kopci', html=(
            '<p>Nejčastější úrazy při sáňkování nevznikají tím, že vybavení selhalo, ale tím, že se sáňky dostaly tam, kde neměly být. Několik zásad platí všude:</p>'
            '<ul>'
            '<li><strong>Žádné silnice.</strong> Svah nesmí končit na komunikaci ani vést přes ni, ani když tam jezdí málo aut.</li>'
            '<li><strong>Volný výběh.</strong> Na konci kopce musí být dost místa na zastavení, bez plotu, stromů, kamenů, potoka nebo parkoviště.</li>'
            '<li><strong>Helma.</strong> Při rychlejší jízdě a u dětí je přilba rozumnou volbou. Lyžařská helma vyhovuje, viz <a href="/lyzarske-helmy/">lyžařské helmy</a>.</li>'
            '<li><strong>Sedět čelem po směru jízdy.</strong> Jízdě vleže na břiše hlavou napřed nebo pozpátku se vyhněte, dítě pak nevidí, kam jede.</li>'
            '<li><strong>Jeden po druhém.</strong> Další vyjede, až předchozí opustí dráhu. Dole se nestojí a nahoře se nečeká uprostřed trati.</li>'
            '<li><strong>Dohled dospělého.</strong> Menší děti doprovází dospělý, nebo na ně aspoň vidí od startu až do cíle.</li>'
            '</ul>'
            '<p>Svah si před prvním sjezdem projděte pěšky. Pod sněhem se často skrývá pařez, led nebo nerovnost, kterou shora nepoznáte. '
            'Pokud je svah tvrdý a zledovatělý, je lepší jet jindy nebo jinde.</p>'
        )),
        dict(h2='Kde sáňkovat', html=(
            '<p>Nejbezpečnější bývají místa, která někdo upravuje a hlídá: sáňkařské svahy u lyžařských areálů, městské kopce, které správa udržuje, nebo '
            'mírně skloněná louka s plochým výběhem. Před cestou se vyplatí zjistit, jestli provozovatel nemá omezení, třeba zákaz kluzáků nebo vlastní '
            'pravidla jízdy. Hledejte svah s mírným sklonem, který dítě zvládne. Lepší je delší a mírný svah než krátký a strmý.</p>'
            '<p>V horách pamatujte na to, že sáňkařské trasy se někde sdílejí s pěšími a běžkaři. Dívejte se na značení a dodržujte ho. '
            'Pokud nevíte, kam jet, zeptejte se v informačním centru nebo na recepci ubytování.</p>'
            '<p>Počítejte i s tím, že sníh se během dne mění. Dopoledne bývá povrch pevný a rychlý, odpoledne po oblevě těžký a mokrý a večer po zamrznutí tvrdý a kluzký. '
            'Stejný svah tak může být jinak nebezpečný ráno a jinak po poledni. Krátká cesta ke svahu pomáhá i dětem: když je kopec blízko, vydrží venku déle a nepřijdou na něj unavené. '
            'Pokud jedete autem, vezměte do kufru suché náhradní oblečení a něco teplého k pití.</p>'
        )),
        dict(h2='Jak oblékat děti do mrazu', html=(
            '<p>Děti se v zimě potí i mrznou rychleji než dospělí. Aktivní hra je zahřívá, jenže stačí chvíle stání a vlhké oblečení začne chladit. '
            'Proto se osvědčuje oblékání ve vrstvách, které lze podle potřeby sundat nebo přidat.</p>'
            '<ol>'
            '<li><strong>Spodní vrstva</strong> je těsně na těle, odvádí pot a nemá být bavlněná. Vhodné je funkční prádlo nebo tenký merino úplet.</li>'
            '<li><strong>Střední vrstva</strong> drží teplo. Fleece nebo tenký svetr stačí, tlusté vrstvy se hodí jen pro opravdu velký mráz.</li>'
            '<li><strong>Svrchní vrstva</strong> chrání před větrem a vlhkem. Nepromokavý kabát nebo kombinéza by měly být zateplené podle teploty a dobře se uzavírat u zápěstí a kotníků.</li>'
            '</ol>'
            '<p>Důležité jsou také ruce, nohy a hlava. Ruce mrznou první, a když jsou mokré, je to dítěti velmi nepříjemné. Přibalte náhradní rukavice, ponožky a čepici. '
            'Mokré věci vyměňte hned, jakmile se dítě začne třást nebo si postěžuje, že mu je zima. Pod helmu patří tenká čepice, která netlačí.</p>'
        )),
        dict(h2='Lyžařské kombinézy a oblečení pro děti', cat='lyzarske-kombinezy', n=6, html=(
            '<p>Jednodílná <a href="/lyzarske-kombinezy/">lyžařská kombinéza</a> je pro menší děti praktická, protože se sníh nedostane za záda ani do pasu. '
            'Starší děti ocení dvoudílné oblečení, které se lépe nosí a odkládá. Při výběru sledujte nepromokavost, uvedenou obvykle v mm vodního sloupce, '
            'prodyšnost, zesílená kolena a sedací část, nastavitelné manžety a odnímatelnou kapuci. Reflexní prvky pomáhají za šera.</p>'
            '<p>Na výběr jsou značky zaměřené na děti i outdoorové firmy, například <a href="/znacka/helly-hansen/">Helly Hansen</a> nebo <a href="/znacka/peak-mountain/">Peak Mountain</a>. '
            'Kupujte raději o číslo větší než příliš těsné, ale ne tak velké, aby dítě zakopávalo. U dětského oblečení se často dá upravit délka nohavic, což prodlouží jeho životnost.</p>'
        )),
        dict(h2='Helmy', cat='lyzarske-helmy', n=6, html=(
            '<p>Na sáňkách nebo kluzáku není helma povinná, ale děti si na ni zvyknou snadno a při pádu nebo srážce ji ocení. '
            'Běžně se používá <a href="/lyzarske-helmy/">lyžařská helma</a>, která je určená do chladu a má nastavitelný obvod. Dobře padnoucí helma nehybně sedí, '
            'nepadá do očí a řemínek je pod bradou utažený tak, aby se pod něj dal vsunout jen prst. Dětská hlava roste, proto jsou obvyklé helmy s kolečkem vzadu, kterým se obvod zmenší nebo zvětší.</p>'
            '<p>V nabídce jsou značky jako <a href="/znacka/alpina/">Alpina</a> nebo <a href="/znacka/salomon/">Salomon</a>. Helmu zkoušejte s tenkou čepicí, '
            'kterou bude dítě nosit. Po silném nárazu je rozumné ji vyměnit i bez viditelného poškození. Výrobci to uvádějí v návodu a stejný postup platí pro cyklistické i lyžařské přilby.</p>'
        )),
        dict(h2='Rukavice', cat='lyzarske-rukavice', n=6, html=(
            '<p>U dětských rukavic je důležité, aby šly snadno navléknout a aby nepromokaly. Palčáky jsou teplejší než prstové rukavice, protože prsty se navzájem zahřívají, '
            'prstové dávají větší obratnost. Pro malé děti jsou vhodné palčáky s dlouhou manžetou, která sahá přes rukáv. '
            'Podívejte se do kategorie <a href="/lyzarske-rukavice/">lyžařské rukavice</a> a u konkrétního kusu zkontrolujte, zda má zesílenou dlaň a nepromokavou membránu.</p>'
            '<p>Rukavice se ztrácejí, proto se vyplatí pořídit dva páry nebo šňůrku, která rukavice spojí. Na kopci se hodí i tenké náhradní rukavice do batohu. '
            'Značky jako <a href="/znacka/viking/">Viking</a> nebo <a href="/znacka/rossignol/">Rossignol</a> nabízejí dětské i dospělé velikosti.</p>'
        )),
        dict(h2='Vyhřívané doplňky pro rodiče', cat='vyhrivane-obleceni', n=4, html=(
            '<p>Dítě se při hře hýbe, rodič stojí. Dospělý, který půl hodiny sleduje sáňkování, mrzne mnohem dřív než jeho potomek. '
            'Do kategorie <a href="/vyhrivane-obleceni/">vyhřívané oblečení</a> patří vyhřívané vesty, rukavice a vložky do bot, které využívají baterii. '
            'Vždy zkontrolujte kapacitu baterie, dobu provozu na jednotlivých stupních a to, kolik hodin vydrží v chladu, protože v mrazu výkon baterie klesá.</p>'
            '<p>Pokud nechcete investovat do elektroniky, pomohou i chemické ohřívače do rukavic a bot, termoska s čajem a sedátko, které vás oddělí od studené lavičky. '
            'Pro delší pobyt venku se hodí i dobrá <a href="/zimni-obuv/">zimní obuv</a>, protože rodičům zebou nejdřív nohy.</p>'
        )),
    ],
    faq=[
        ('Od kolika let může dítě sáňkovat?', '<p>Pevný věk není, záleží na vybavení. Nejmenší děti vozí rodiče na sáňkách s opěrkou a popruhem, a to pomalu a na rovině. Samostatně z kopce děti obvykle jezdí, až když umí sedět, držet se a poslouchat pokyny. Doporučení výrobce si vždy přečtěte.</p>'),
        ('Je na sáňkách potřeba helma?', '<p>Povinná nebývá, ale při rychlejší jízdě, u kluzáků a u dětí je vhodná. Bezpečnost ale zajišťuje hlavně výběr svahu, volný výběh a jízda po jednom. Helma je dobrý doplněk, ne náhrada těchto zásad.</p>'),
        ('Jak dlouho děti na mrazu nechat?', '<p>Pevná hranice není. Sledujte dítě: zima, červené ruce, třas nebo bledá až bílá místa na tvářích, nose či uších jsou signál jít dovnitř a převléknout se. U menších dětí dělejte kratší pauzy a dejte jim teplé pití.</p>'),
        ('Co je lepší, sáňky, nebo boby?', '<p>Sáňky jsou jednodušší, často lehčí a pro menší děti bezpečnější, protože jedou méně rychle. Boby mají řízení a dají se ovládat i v zatáčkách, vyžadují ale zkušenost. Na rodinný výlet se hodí obojí, pokud je svah vhodný.</p>'),
        ('Dá se kombinéza koupit na dorost?', '<p>Trochu větší velikost je rozumná, protože se dítě oblékne i s vrstvami. Příliš velká kombinéza ale brání pohybu a navlhne na kolenou, proto kupujte maximálně o číslo větší. Některé modely mají prodlužovací manžety, které prodlouží životnost.</p>'),
        ('Kde porovnám ceny sáněk a oblečení?', '<p>Na Sportece, která sama nic neprodává a jen porovnává nabídky českých e-shopů. U každého produktu uvidíte obchody, ceny a dostupnost a kliknutím přejdete přímo do vybraného obchodu, kde nákup dokončíte.</p>'),
    ],
    cats=['sane-a-boby', 'lyzarske-kombinezy'],
    updated='2026-11-16')

# ---------------------------------------------------------------------------------------------------------------------
GUIDES['brusle-na-led'] = dict(
    name='Brusle na led',
    h1='Brusle na led: jak vybrat pro děti i dospělé',
    seo_title='Brusle na led: jak vybrat pro děti i dospělé | Sporteka',
    seo_desc='Rekreační, krasobruslařské a hokejové brusle: rozdíly, výběr velikosti, dětské posuvné brusle, broušení nožů a první kroky na ledě. Přehled nabídek e-shopů.',
    intro_html=(
        '<p>Brusle na led se nejčastěji kupují ve dvou chvílích: když začne sezona a rodina zjistí, že jsou dětem malé, a když se kluziště zaplní a půjčovna nemá potřebnou velikost. '
        'Přitom rozdíl mezi botami, které sedí a jsou správného typu, a těmi, které jen dobře vypadají, je při bruslení obrovský. Špatná brusle bolí, nedrží kotník a z jízdy dělá dřinu.</p>'
        '<p>Průvodce vás provede třemi hlavními typy bruslí (rekreačními, krasobruslařskými a hokejovými), poradí s velikostí, dětskými nastavitelnými modely i údržbou nožů a ukáže, '
        'jak zvládnout první kroky na ledě. Na Sportece porovnáte nabídky českých e-shopů vedle sebe, nic zde neprodáváme a nakupujete přímo v obchodě. '
        'Pokud už víte, co hledáte, podívejte se rovnou do <a href="/brusle/">kategorie brusle</a>.</p>'
    ),
    sections=[
        dict(h2='Rozdíly mezi typy bruslí', html=(
            '<p>Brusle se na první pohled podobají, ale liší se konstrukcí boty i nože. Typ vybírejte podle toho, co na ledě chcete dělat, ne podle vzhledu.</p>'
            + T(['Typ', 'Bota', 'Nůž', 'Hodí se na'], [
                ['Rekreační', 'Měkčí, často s vnitřní botou a zapínáním přezkami nebo šněrováním', 'Delší a rovnější, aby jízda byla stabilní', 'Veřejné bruslení, kluziště, rodinné výlety'],
                ['Krasobruslařské', 'Pevnější a vyšší kotník, kůže nebo syntetika', 'Se zoubky na špičce pro skoky a otáčky', 'Krasobruslení, pokročilejší figury'],
                ['Hokejové', 'Pevná skořepina a ochrana nártu', 'Kratší a zakulacený, lepší obratnost', 'Hokej, rychlé změny směru'],
            ]) +
            '<p>Rekreační brusle prominou víc chyb a pro začátečníky jsou nejpohodlnější. Hokejové brusle jsou nízké a pevně obepínají nohu, což umožňuje prudké zatáčení a brzdění, '
            'netrénovaným nohám ale nemusí být dlouhé bruslení v nich příjemné. Krasobruslařské mají na špičce zoubky, o které nezkušený bruslař snadno zakopne, proto se na rušné veřejné kluziště příliš nehodí.</p>'
        )),
        dict(h2='Rekreační brusle', cat='rekreacni-brusle', n=6, html=(
            '<p>Pro většinu rodin jsou nejlepší volbou na začátek <a href="/rekreacni-brusle/">rekreační brusle</a>. Mají měkčí vnitřní botu, dobrou oporu kotníku a zapínání, '
            'které zvládnou samy i děti. Dospělým se hodí šněrování v kombinaci s přezkami, protože umožňují jemně přizpůsobit utažení v různých místech nohy. '
            'U dětí je důležitější snadné zapínání než dokonalé utažení, hlavně když s ním nebudete pomáhat při každém bruslení.</p>'
            '<p>V nabídce uvidíte značky jako <a href="/znacka/bauer/">Bauer</a> a <a href="/znacka/fila/">Fila</a>, vedle nich i další výrobce. '
            'Všímejte si materiálu, výstelky a toho, jestli má bota dostatečně pevný kotník, který se neprohýbá do strany. Brusle, ve kterých kotník padá dovnitř, brzdí začátečníka víc než cokoli jiného.</p>'
        )),
        dict(h2='Velikost a nastavitelné dětské brusle', html=(
            '<p>Velikost bruslí se nemusí shodovat s velikostí běžné obuvi a mezi výrobci se liší. Rozhodující je proto velikostní tabulka konkrétního výrobce, která obvykle uvádí délku chodidla. '
            'Změřte nohu doma a porovnejte ji s tabulkou. Prsty by se měly dotýkat špičky, ale nesmí být stlačené. Pata sedí pevně a nezvedá se při předklonu. '
            'Brusle zkoušejte v ponožkách, ve kterých budete bruslit, obvykle tenkých. Silné ponožky moc tepla nepřidají a spíš zhoršují cit.</p>'
            '<p>Děti rostou rychle a brusle nejsou levné, proto jsou oblíbené <strong>nastavitelné brusle</strong>. Posuvné modely se obvykle dají nastavit o tři až čtyři čísla, '
            'takže vydrží více sezon. Dávají smysl hlavně pro rekreační jízdu. Posuvný mechanismus je ale kompromis a bota bývá méně tuhá než u pevné velikosti. '
            'Pro dítě, které trénuje, je vhodnější pevná velikost.</p>'
            '<p>Nikdy nekupujte brusle o dvě čísla větší s tím, že do nich dítě doroste. Noha ve volné botě klouže, nemá oporu a dítě se bruslení zprotiví dřív, než se ho naučí.</p>'
        )),
        dict(h2='Krasobruslařské brusle', cat='krasobruslarske-brusle', n=4, html=(
            '<p>V nabídce <a href="/krasobruslarske-brusle/">krasobruslařských bruslí</a> najdete modely pro děti, které teprve začínají v kroužku, i pro pokročilé. '
            'Bílé kožené brusle jsou typické pro dívky a černé pro chlapce, barva je ale hlavně věcí zvyku. '
            'Pro začátek se hodí syntetické modely s nastavitelným šněrováním, které jsou lehčí a levnější než plně kožené; pro trénink je ale lepší pevná bota.</p>'
            '<p>V katalogu se objevují značky jako <a href="/znacka/winnwell/">Winnwell</a> a další. Nůž se u některých modelů prodává zvlášť a je nutné ho namontovat u odborníka, což stojí čas i peníze. '
            'Zeptejte se trenéra, jaký typ u dítěte doporučuje. Brusle koupené bez konzultace mohou být pro trénink slabé nebo naopak zbytečně pevné.</p>'
        )),
        dict(h2='Šněrování, přezky a nastavení', html=(
            '<p>Způsob zapínání ovlivňuje pohodlí víc, než se zdá. Šněrování umožňuje utáhnout každou část boty zvlášť, volněji přes nárt a pevněji kolem kotníku, ale vyžaduje cvik a u malých dětí je zdlouhavé. '
            'Přezky a suché zipy jsou rychlé a dítě je zvládne samo, jenže botu tolik nepřizpůsobí tvaru nohy. Mnoho rekreačních modelů kombinuje obojí: šněrování v přední části a přezky na kotníku.</p>'
            '<p>Správně utažená brusle drží patu pevně, prsty se mohou lehce pohybovat a kotník se nehýbá do stran. Jazyk boty nemá tlačit na přední část kotníku. '
            'Po prvních desítkách minut zastavte a šněrování dolaďte, protože se vnitřní bota usadí. Pokud bruslení bolí, neodkládejte to na později. Zkuste jiné utažení, jiné ponožky nebo jinou velikost.</p>'
            '<p>Nové brusle je rozumné vyzkoušet krátce doma na koberci, než s nimi půjdete na led. Ověříte si velikost a případně je vrátíte, dokud jsou nepoužité; podmínky vrácení zboží si ale zjistěte u konkrétního obchodu.</p>'
        )),
        dict(h2='Hokejové brusle', cat='hokejove-brusle', n=6, html=(
            '<p>Hokejová bota je tvrdá a těsná, a to je záměr. Drží nohu při prudkém zatáčení a chrání ji před ranou pukem. '
            '<a href="/hokejove-brusle/">Hokejové brusle</a> pro dospělé i mládež tvoří jednu z nejširších nabídek, z velkých jmen v ní najdete '
            '<a href="/znacka/bauer/">Bauer</a> a <a href="/znacka/ccm/">CCM</a>. Velikosti hokejových bruslí se od běžné obuvi liší podle výrobce, proto se řiďte jeho tabulkou: brusle má sedět těsně a pata se v ní nesmí zvedat.</p>'
            '<p>Rozdíly mezi modely jsou v tuhosti boty, materiálu a nože. Vyšší řady mají tvarovatelnou botu, která se po zahřátí přizpůsobí noze. '
            'Pro rekreační hokej nebo dětský trénink stačí střední třída. Rostoucí dítě potřebuje brusle často měnit za větší, takže investice do nejvyšší řady nemá smysl.</p>'
        )),
        dict(h2='Chrániče a helmy', cat='chranice-a-helmy', n=6, html=(
            '<p>Při prvních krocích na ledě se nejčastěji padá dozadu nebo na bok. Rozumnou výbavou pro děti i dospělé začátečníky je helma a chrániče zápěstí, kolen a loktů. '
            'Najdete je v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>. Helma nemusí být přímo hokejová, ale musí pevně sedět a zakrývat čelo. U dětí i dospělých ji vybírejte podle velikostní tabulky výrobce a obvodu hlavy.</p>'
            '<p>Chrániče zápěstí chrání před nejčastějším poraněním při pádu na ruku, kdy se člověk instinktivně opře. Kolena a lokty ocení hlavně děti. '
            'Hokejisté a pokročilejší děti ocení i rukavice, které chrání před říznutím nožem při pádu vedle jiných bruslařů.</p>'
        )),
        dict(h2='Broušení nožů', html=(
            '<p>Nový nůž bývá vybroušený z výroby, ale po několika hodinách na ledě tupne. Tupý nůž ujíždí, nedrží hranu a bruslař ztrácí oporu. Nabrousit ho můžete v servisu na zimním stadionu, '
            'v obchodě s hokejovým vybavením nebo u trenéra. Hokejisté brousí podle vlastní potřeby, rekreační bruslař obvykle před sezónou a po několika desítkách hodin.</p>'
            '<p>Po bruslení brusle <strong>vždy utřete</strong> a mokré nože nenechávejte zavřené v pouzdře, protože rezaví. Na chůzi mimo led používejte chrániče nožů. '
            'Při chůzi po betonu nebo dlažbě se nůž poškodí během několika minut. Pro cestu k ledu se hodí i gumové chrániče, které se nasadí a v šatně sundají.</p>'
        )),
        dict(h2='Nesmeky na cestu ke kluzišti', cat='nesmeky', n=6, html=(
            '<p>Cesta k ledu často vede po zledovatělém chodníku nebo sněhu. Pomohou <a href="/nesmeky/">nesmeky</a>, tedy gumové návleky s kovovými zuby nebo řetízky, které se natahují na běžné boty. '
            'Nehodí se pro chůzi po dlažbě uvnitř budovy, protože tam kovové prvky kloužou a poškozují podlahu. Na cestě k ledu je nasadíte, před vstupem do šatny zase sundáte.</p>'
            '<p>V katalogu jsou značky jako <a href="/znacka/viking/">Viking</a> a mnoho dalších. U dětí zkontrolujte velikost, protože nesmeky, které padají z boty, jsou horší než žádné. '
            'Dobré jsou ty, které drží i na zimní botě a nepřekážejí při chůzi.</p>'
        )),
        dict(h2='První kroky na ledě', html=(
            '<p>Začátečník by měl hlavně zůstat vzpřímený a uvolněný. Pár pravidel pomůže:</p>'
            '<ul>'
            '<li><strong>Mírně pokrčená kolena</strong> a mírný předklon zajistí stabilitu, napnutá záda vedou k pádům dozadu.</li>'
            '<li><strong>Dívejte se před sebe</strong>, ne na špičky bot.</li>'
            '<li><strong>Chůze po ledě v malých krocích</strong>, špičky mírně ven, jako při chůzi s nohama do V.</li>'
            '<li><strong>Naučte se padat</strong>: do strany, s pokrčenými koleny, ruce nenatahujte daleko před sebe, držte je mírně před tělem. Vstávejte pak přes pozici na čtyřech, ne rovnou na nohy.</li>'
            '<li><strong>Držet se mantinelu</strong> v prvních minutách je v pořádku. Dětem pomůže opora, například židle.</li>'
            '</ul>'
            '<p>Dítě se obvykle naučí bruslit po několika návštěvách, dospělému to trvá o něco déle. Nespěchejte a skončete dřív, než přijde únava, protože ta způsobuje pády. '
            'Pokud chcete s dětmi pokračovat i v dalších zimních aktivitách, podívejte se i na <a href="/zimni-radovanky-s-detmi/">zimní radovánky s dětmi</a>.</p>'
        )),
        dict(h2='Oblečení na led', html=(
            '<p>Na kluzišti se zahřejete rychleji, než čekáte, ale led chladí zespodu a v hale bývá chladno. Oblékejte se po vrstvách: tenké funkční prádlo, mikina nebo fleece a lehká bunda. '
            'Rukavice jsou nutnost i v teplé hale, protože chrání dlaně při pádu. Na hlavu patří tenká čepice nebo helma. Dlouhé kalhoty chrání kolena před odřením.</p>'
            '<p>Pro kluziště na venkovním stadionu přibalte teplejší vrstvu na čekání a termosku. Děti by se pod mnoha vrstvami neměly potit, proto volte spíš méně kusů, ale kvalitnějších. '
            'Víc tipů na oblékání dětí najdete v průvodci o zimních radovánkách.</p>'
        )),
        dict(h2='Zamrzlé rybníky a přírodní led', html=(
            '<p>Přírodní led je lákavý, ale není předvídatelný. Nelze jej posoudit pohledem a může být tenký i tam, kde to nevypadá. '
            'Platí jednoduché pravidlo: <strong>na přírodní led jen tam, kde je led úředně nebo správcem uvolněn, nikdy sami.</strong> '
            'Neuvolněný led nezkoušejte ani na malých rybnících, ani na tocích, kde proud ztenčuje vrstvu.</p>'
            '<p>Pokud bruslíte na uvolněné ploše, buďte alespoň ve dvojici a mějte u sebe mobil. Děti držte blízko břehu, u správce se zeptejte na pokyny a respektujte zákazy. '
            'Pro většinu rodin je jistější umělá ledová plocha, kde je led pravidelně upravován a obsluha dohlíží na provoz.</p>'
        )),
    ],
    faq=[
        ('Jakou velikost bruslí koupit dítěti?', '<p>Nejlépe podle délky chodidla a velikostní tabulky výrobce. Prsty se mají dotýkat špičky, ale nesmí být stlačené, pata sedí pevně. Nekupujte o dvě čísla větší. Pokud dítě rychle roste, zvažte nastavitelné brusle, které bývají posuvné o tři až čtyři čísla.</p>'),
        ('Jsou posuvné dětské brusle dobrý nápad?', '<p>Pro rekreační jízdu ano, vydrží několik sezón. Bota je méně pevná než u pevných modelů, takže pro pravidelný trénink se víc hodí pevná velikost podle nohy.</p>'),
        ('Mohu v hokejových bruslích jezdit rekreačně?', '<p>Můžete, ale jsou tvrdší a těsnější než rekreační. Pro rodinné bruslení bývá příjemnější rekreační model, který je pohodlnější a snáze se zapíná.</p>'),
        ('Jak často brousit brusle?', '<p>Záleží na počtu hodin na ledě a na potřebách jezdce. Rekreačnímu bruslaři stačí brousit brusle na začátku sezony a pak ve chvíli, kdy přestanou dobře držet na hraně. Hokejisté brousí častěji.</p>'),
        ('Jak chránit nože při přenášení?', '<p>Používejte pouzdra nebo chrániče na chůzi mimo led. Po bruslení nože osušte, aby nerezavěly, a neukládejte je zavřené v mokrém pouzdře.</p>'),
        ('Kde porovnám ceny bruslí?', '<p>Sporteka porovnává nabídky českých e-shopů, sama nic neprodává. U produktu uvidíte obchody a ceny vedle sebe a nákup dokončíte přímo v obchodě.</p>'),
    ],
    cats=['brusle'],
    updated='2026-11-16')

# ---------------------------------------------------------------------------------------------------------------------
GUIDES['vyziva-pro-zacatecniky'] = dict(
    name='Výživa pro začátečníky',
    h1='Začínáte cvičit? Co z doplňků výživy dává smysl',
    seo_title='Výživa pro začátečníky: jaké doplňky stravy dávají smysl',
    seo_desc='Protein, kreatin, vitamín D, hořčík nebo iontové nápoje: co znamenají pro začátečníky, jak číst etiketu a na co nespoléhat. Porovnání nabídek e-shopů.',
    intro_html=(
        '<p>Se začátkem cvičení přichází i záplava reklam na doplňky: proteiny, spalovače, předtréninkové směsi, kreatin. Reklama vás má přesvědčit, že bez nich výsledky nepřijdou. '
        'Pravda je střízlivější. U většiny začátečníků rozhoduje, jak jedí, kolik spí a jestli cvičí pravidelně. Doplněk to může doplnit, ale nenahradí.</p>'
        '<p>Tento průvodce vysvětluje, co je základ, jak si přečíst etiketu a které doplňky mají v běžném životě pro začátečníka smysl. Zmiňuje jen tvrzení, která schvaluje Evropská unie, '
        'a nic neslibuje. Sporteka sama nic neprodává, porovnává nabídky českých e-shopů. Nákup dokončíte přímo v obchodě. Pokud teprve hledáte vhodný druh pohybu, přečtěte si i průvodce '
        '<a href="/domaci-posilovna/">domácí posilovna</a> a <a href="/bezky-pro-zacatecniky/">běžky pro začátečníky</a>.</p>'
    ),
    sections=[
        dict(h2='Základ je jídlo a spánek', html=(
            '<p>Svaly se nestavějí v posilovně, ale při odpočinku, pokud jim tělo dodá, co potřebují. Pro začátečníka to znamená tři věci, které nestojí nic navíc:</p>'
            '<ul>'
            '<li><strong>Pravidelná pestrá strava</strong> s dostatkem bílkovin ze zdrojů jako maso, ryby, vejce, mléčné výrobky, luštěniny a ořechy.</li>'
            '<li><strong>Spánek</strong> delší než pět až šest hodin. Nedostatek spánku zhoršuje regeneraci i chuť k jídlu.</li>'
            '<li><strong>Dostatek tekutin</strong> během dne i při cvičení.</li>'
            '</ul>'
            '<p>Teprve když tohle funguje, přicházejí ke slovu doplňky. Slouží k doplnění živin, které se z jídla získávají obtížně, '
            'nebo k pohodlí, třeba když nemáte čas jíst po tréninku. Žádný doplněk nenahradí stravu.</p>'
        )),
        dict(h2='Kolik cvičit a jak začít', html=(
            '<p>Druhou částí základu je samotný pohyb. Dvě až tři tréninky týdně stačí, aby si tělo zvyklo. Zátěž přidávejte postupně, protože přetížení vede k bolestem a často i k tomu, že člověk se cvičením přestane. '
            'Dny odpočinku jsou součástí plánu. Svaly rostou, když dostanou čas na obnovu.</p>'
            '<p>Pokud nevíte, jak začít, vyberte si jednoduchý plán: základní cviky s vlastní vahou, chůze nebo lehký běh. Ruku v ruce s tím jde stravování, které vydržíte i za rok, ne dieta na tři týdny. '
            'Pokud máte zdravotní potíže nebo jste dlouho necvičili, nechte si před začátkem poradit od lékaře.</p>'
        )),
        dict(h2='Jak číst etiketu', html=(
            '<p>Na obalu doplňku stravy je několik údajů, které stojí za pozornost:</p>'
            '<ul>'
            '<li><strong>Složení a obsah účinné látky</strong>, ne jen velikost balení. U proteinu je to podíl bílkovin v porci, u kreatinu množství na dávku.</li>'
            '<li><strong>Doporučené denní množství</strong> od výrobce. Řiďte se jím a nezvyšujte ho v domnění, že víc znamená lépe.</li>'
            '<li><strong>Alergeny</strong>, například mléko, sója, ořechy, lepek. Ve složení jsou zvýrazněné.</li>'
            '<li><strong>Sladidla a přídatné látky</strong>. Proteiny a nápoje je často obsahují a některým lidem nevyhovují.</li>'
            '<li><strong>Datum minimální trvanlivosti</strong> a způsob skladování.</li>'
            '<li><strong>Upozornění</strong>, kdo doplněk nemá užívat, například děti nebo těhotné.</li>'
            '</ul>'
            '<p>Věřte hlavně údajům na etiketě a v popisu produktu u prodejce. Marketingové slogany jako „spaluje tuky“ nebo „výbušný růst“ nejsou informace. '
            'Povolená zdravotní tvrzení musí být v seznamu tvrzení schválených EU a týkají se konkrétní látky, ne celého výrobku.</p>'
        )),
        dict(h2='Proteiny', cat='proteiny', n=6, html=(
            '<p>Bílkoviny přispívají k nárůstu a udržení svalové hmoty. To platí pro bílkoviny ze stravy stejně jako z doplňku. <a href="/proteiny/">Proteinový prášek</a> '
            'je tedy prostě pohodlný zdroj bílkovin: rozmícháte ho s vodou nebo mlékem a máte porci bílkovin bez vaření. Kdo má bílkovin ze stravy dost, ho proto nepotřebuje.</p>'
            '<p>Nejčastější typy jsou syrovátkový protein (z mléka), kaseinový (z mléka, pomaleji se tráví) a rostlinné, například hrachový nebo sójový. '
            'Lidé s intolerancí laktózy hledají izoláty nebo rostlinné směsi. Mezi nabízenými značkami jsou například <a href="/znacka/gymbeam/">GymBeam</a> a další. '
            'Srovnávejte obsah bílkovin v porci a příchuť – nápoj budete pít několikrát týdně. Pro zdravé dospělé platí doporučení na obalu. '
            'Při onemocnění ledvin nebo jiných chronických potížích se předem poraďte s lékařem.</p>'
        )),
        dict(h2='Kreatin', cat='kreatin', n=6, html=(
            '<p>Kreatin patří k nejlépe prozkoumaným doplňkům. Podle tvrzení schváleného v EU <strong>kreatin zvyšuje fyzickou výkonnost při po sobě jdoucích krátkodobých intervalech velmi intenzivní fyzické aktivity</strong>, '
            'a to při denním příjmu 3 g. Týká se to dospělých, kteří cvičí vysoce intenzivně, tedy například při silovém tréninku nebo sprintu. Pro rekreační chůzi nebo lehké kardio nemá smysl.</p>'
            '<p>V nabídce <a href="/kreatin/">kreatinu</a> se objevuje nejčastěji monohydrát v prášku a kapslích. Porovnávejte čistotu a velikost balení. '
            'Dávkování řiďte podle doporučení na obalu. Pijte při užívání dostatek tekutin. Kreatin je určen dospělým, děti a těhotné ho neužívají. Při zdravotních potížích se poraďte s lékařem.</p>'
        )),
        dict(h2='Vitamín D', cat='vitamin-d', n=4, html=(
            '<p>Vitamín D přispívá k normální funkci svalů a imunitního systému a k udržení normálního stavu kostí. V zimě se v našich zeměpisných šířkách tvoří v kůži málo a přísun z jídla bývá omezený. '
            'Doplňky najdete v kategorii <a href="/vitamin-d/">vitamín D</a>, často jako kapky nebo kapsle.</p>'
            '<p>Dávkování řiďte podle obalu, případně podle doporučení lékaře. Než začnete dlouhodobě užívat vyšší dávky, poraďte se s odborníkem, '
            'protože vitamín D je rozpustný v tucích a jeho nadbytek se může hromadit. Pokud užíváte léky, zeptejte se i lékárníka.</p>'
        )),
        dict(h2='Hořčík', cat='horcik', n=6, html=(
            '<p>Hořčík přispívá k normální funkci svalů a ke snížení míry únavy a vyčerpání. Tvrzení se týká normální funkce, nikoli léčby křečí. '
            'V <a href="/horcik/">kategorii hořčík</a> uvidíte různé formy: citrát, bisglycinát, malát nebo oxid. Liší se obsahem čistého hořčíku a snášenlivostí. '
            'Údaj o obsahu hořčíku v jedné dávce je důležitější než váha tablety.</p>'
            '<p>Hořčík získáte i ze stravy, například z ořechů, semínek, luštěnin a celozrnných produktů. Při dlouhodobých křečích nebo jiných potížích se obraťte na lékaře, '
            'nevyřešíte to jen doplňkem. Příliš vysoká dávka může způsobovat průjem, dodržte proto doporučení na obalu.</p>'
        )),
        dict(h2='Fit potraviny', cat='fit-potraviny', n=6, html=(
            '<p>Kromě doplňků existují <a href="/fit-potraviny/">fit potraviny</a>: tyčinky, kaše, müsli, ořechová másla, nízkosacharidové těstoviny nebo proteinové pečivo. '
            'Dobře fungují jako pohodlná svačina, ale nápis „fit“ na obalu ještě neznamená, že jde o zdravé jídlo. Některé tyčinky mají tolik cukru nebo tuku jako běžná sladkost.</p>'
            '<p>Čtěte složení a nutriční tabulku, ne jen označení. Porovnejte energii, bílkoviny, cukry a vlákninu v porci. Pro začátečníka je často lepší obyčejné jídlo než speciální produkt, '
            'ale na cesty a do práce se tyčinka nebo kaše hodí.</p>'
        )),
        dict(h2='Iontové nápoje', cat='iontove-napoje', n=6, html=(
            '<p>Při běžném cvičení do hodiny stačí voda. <a href="/iontove-napoje/">Iontové nápoje</a> začínají dávat smysl při delším nebo intenzivnějším výkonu a ve vedru, '
            'kdy se potem ztrácejí minerály. Obsahují sodík, draslík a často cukry jako zdroj energie. Podle schváleného tvrzení přispívají sacharidovo-elektrolytové roztoky k udržení vytrvalostního výkonu při dlouhodobém vytrvalostním cvičení.</p>'
            '<p>Prášky a tablety se rozpouštějí ve vodě a vyplatí se při dlouhých trasách. Porovnávejte obsah sacharidů a minerálů a sledujte, jak vám nápoj chutná při chůzi nebo běhu. '
            'Zimnímu běhu se věnuje průvodce <a href="/zaciname-behat-v-zime/">začínáme běhat v zimě</a>.</p>'
        )),
        dict(h2='Jak si doplňky poskládat', html=(
            '<p>Začátečník nepotřebuje celou polici. Rozumný postup je jednoduchý: nejdřív několik týdnů pravidelně cvičit a jíst přiměřeně, a teprve potom zvažovat, co chybí. '
            'Zeptejte se sami sebe, jakou potřebu má doplněk řešit. Když po tréninku nestíháte jíst, poslouží proteinová směs nebo tyčinka. Na zimní nedostatek slunce je tu vitamín D, ovšem po konzultaci s lékařem nebo lékárníkem. '
            'Při delším vytrvalostním výkonu se hodí iontový nápoj. Kreatin je určen těm, kdo trénují silově a intenzivně.</p>'
            '<p>Zavádějte vždy jen jednu novinku. Pokud začnete užívat tři nové doplňky současně a objeví se potíže, nepoznáte, který je způsobil. '
            'Poznamenejte si, co užíváte a jak se cítíte. U každého výrobku porovnejte více nabídek, protože ceny za stejné balení se mezi obchody liší, a vybírejte velikost balení, kterou do konce trvanlivosti opravdu spotřebujete.</p>'
            '<p>Nekupujte doplňky podle doporučení influencerů, kteří je zároveň prodávají, ani podle slibů o rychlých výsledcích. Důvěryhodnější je výrobce, který uvádí úplné složení, množství účinných látek a nepřisuzuje látkám víc, než dokazatelně dělají. '
            'Pokud je cena nápadně nízká nebo naopak vysoká, zjistěte důvod: bývá v obsahu účinné látky nebo ve velikosti porce.</p>'
        )),
        dict(h2='Spalovače tuků a co od doplňků nečekat', html=(
            '<p>Spalovače tuků jsou kategorie, ve které se nejvíc slibuje a nejméně plní. Žádný doplněk samotný nezpůsobí hubnutí. Úbytek hmotnosti vzniká dlouhodobým energetickým deficitem, '
            'tedy pohybem a stravou. Výrobky bývají založeny na kofeinu a podobných látkách, které mohou způsobit bušení srdce, nervozitu nebo problémy se spánkem. '
            'Pokud o nich uvažujete, čtěte pozorně upozornění a množství kofeinu v porci.</p>'
            '<p>Čekejte, že doplněk <strong>doplní</strong> stravu, ne že nahradí trénink. Sliby typu „X kilo za týden“ nejsou realistické. '
            'Pokud chcete hubnout, poraďte se s lékařem nebo nutričním terapeutem, který vám navrhne postup podle vašeho zdravotního stavu.</p>'
        )),
        dict(h2='Bezpečnost: komu je lepší se poradit', html=(
            '<p>Doplněk stravy není lék a nemá léčit nemoci. Před užíváním se poraďte s lékařem nebo lékárníkem, pokud:</p>'
            '<ul>'
            '<li>jste <strong>těhotná nebo kojíte</strong>,</li>'
            '<li>jde o <strong>dítě nebo mladistvého</strong>,</li>'
            '<li>užíváte <strong>léky</strong>, zejména na srdce, tlak, ledviny nebo krevní srážlivost,</li>'
            '<li>máte <strong>chronické onemocnění</strong>, například ledvin, jater nebo štítné žlázy,</li>'
            '<li>jste alergik a ve složení si nejste jistí.</li>'
            '</ul>'
            '<p>Dodržujte doporučení na obalu a nekombinujte více výrobků se stejnou látkou, například tři směsi s vitamínem D. '
            'Při nežádoucích příznacích užívání ukončete a vyhledejte lékaře. Skladujte mimo dosah dětí a nepoužívejte po datu trvanlivosti.</p>'
        )),
    ],
    faq=[
        ('Potřebuje začátečník protein?', '<p>Ne nutně. Bílkoviny přispívají k nárůstu a udržení svalové hmoty, ale získáte je i ze stravy. Prášek je jen pohodlnější zdroj, hodí se, když nestíháte jíst nebo vám bílkovin ve stravě chybí.</p>'),
        ('Co kreatin skutečně dělá?', '<p>Kreatin zvyšuje fyzickou výkonnost při po sobě jdoucích krátkodobých intervalech velmi intenzivní fyzické aktivity, a to při denním příjmu 3 g. Pro běžnou chůzi, lehké kardio nebo rekreační cvičení se nehodí. Dávkujte podle doporučení na obalu.</p>'),
        ('Mám v zimě užívat vitamín D?', '<p>Vitamín D přispívá k normální funkci svalů a imunitního systému. Zda je pro vás vhodný a v jaké dávce, vám řekne lékař nebo lékárník, zvlášť pokud užíváte léky nebo jste těhotná.</p>'),
        ('Pomůže hořčík na křeče?', '<p>Hořčík přispívá k normální funkci svalů, ale doplněk není lék na křeče. Pokud se křeče opakují, nechte si poradit od lékaře, příčin může být víc.</p>'),
        ('Jak poznám kvalitní doplněk?', '<p>Podle jasné etikety: složení s množstvím účinné látky, dávkování, alergeny a výrobce. Pozor na slibované zázraky. Čtěte i popis na stránce obchodu a porovnávejte produkty stejné kategorie.</p>'),
        ('Pomohou spalovače tuků zhubnout?', '<p>Žádný doplněk sám hubnutí nezpůsobí. Spalovače obsahují často kofein, který může způsobit nervozitu nebo potíže se spánkem. Základem je strava a pohyb a při hubnutí se vyplatí konzultace s odborníkem.</p>'),
        ('Kde porovnám nabídky doplňků?', '<p>Sporteka porovnává nabídky českých e-shopů a sama nic neprodává. U produktu uvidíte obchody a ceny vedle sebe, nákup dokončíte přímo v obchodě.</p>'),
    ],
    cats=['proteiny', 'kreatin'],
    updated='2026-11-16')
