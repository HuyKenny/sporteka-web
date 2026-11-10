"""sporteka.cz — facet landing texts wave 138: lezecky-sedak, altra-bezecke-boty, ruzove-kopacky-nike, navijaky-penn.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lezecky-sedak
NEW['lezecky-sedak'] = dict(
    title='Lezecký sedák: jak vybrat úvazek na stěnu i skálu',
    desc='Lezecký sedák neboli sedací úvazek: rozdíly mezi sportovním a alpským modelem, velikost, nastavení, údržba a výběr značek i obchodů.',
    intro='<p>Lezecký sedák je jediná část výbavy, která drží lezce na laně, a proto se vybírá jinak než boty nebo oblečení. Rozhoduje, jestli sedí v pase i na stehnech, jestli nepřekáží ve zlezení a jestli ho unesete celý den na zádech. Sportovní model do lezecké haly má jiné priority než lehký alpský úvazek nebo celotělový dětský. Na této stránce najdete přehled typů, pravidla pro velikost a nastavení, péči o textil, rozdíly mezi dámským, pánským a dětským střihem a vodítko, jak poznat, kdy je čas sedák vyřadit. Doplňte jej o <a href="/lezecke-boty/">lezečky</a> a nezapomeňte, že sedák patří do širší sady popsané v kategorii <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky, přilby a pomůcky</a>.</p>',
    guide=(
        '<h2>Co je lezecký sedák a z čeho se skládá</h2>'
        '<p>Sedací úvazek tvoří pás kolem pasu, dvě smyčky na stehna a spojovací prvky, které je drží pohromadě. Na přední straně leží uzlový bod, kam se zavazuje lano, a nad ním pevná jisticí smyčka, v níž se zavěšuje jisticí pomůcka. Po obvodu pasu bývají poutka na materiál, do kterých se věší expresky, smyčky a pytlík na magnézium. Zadní část nese nejvíc zátěže při pádu, proto je na páteři silnější a širší než na bocích.</p>'
        '<p>Zapamatujte si jedno pravidlo: lano se zavazuje jen do určených uzlových bodů a jisticí smyčka slouží jen k jištění. Poutka na materiál nejsou dimenzovaná na držení těla a nikdy se do nich lano nevazí. Stejně tak se do nich nezavěšuje nic, co by drželo váhu člověka.</p>'
        '<h2>Typy sedáků podle použití</h2>'
        + T(['Typ', 'Pro koho', 'Na co si dát pozor'], [
            ['Sportovní', 'lezecká hala, sportovní cesty na skále', 'pevné polstrování, počet poutek, nastavení pasu'],
            ['Alpský a skialpový', 'vícedélkové cesty, horské túry, ledovce', 'nízká hmotnost, smyčky nastavitelné přes tlusté nohavice'],
            ['Celotělový dětský', 'malé děti, které nemají vyvinuté boky', 'kombinace sedáku a hrudního pásu, aby dítě nevypadlo'],
            ['Kombinovaný s hrudním pásem', 'ferraty, kurzy a lezci, kteří ještě nemají jistý styl', 'správné spojení obou částí, nastavení výšky hrudního pásu'],
            ['Vícedélkový a velká stěna', 'dlouhé dny v laně, bivak ve stěně', 'široké polstrování, množství místa na vybavení']]) +
        '<p>Sportovní úvazky bývají měkce polstrované a dobře drží tvar při visu v laně. Alpské modely pro vícedélkové cesty a <a href="/skialpinismus/">skialpinismus</a> šetří gramy na úkor pohodlí: pás a smyčky jsou tenčí a po skládání zabírají v batohu málo místa. Pokud chcete jeden sedák na všechno, hledejte střední cestu, tedy mírně polstrovaný model s nastavitelnými smyčkami na stehnech.</p>'
        '<h2>Značky sedáků v nabídce</h2>'
        '<p>V katalogu se objevují sedáky od výrobců ' + B(('petzl', 'Petzl'), ('camp', 'Camp'), ('singing-rock', 'Singing Rock'), ('black-diamond', 'Black Diamond'), ('edelrid', 'Edelrid'), ('ocun', 'Ocún'), ('climbing-technology', 'Climbing Technology')) + '. Petzl a Black Diamond jsou známé širokým sortimentem pro všechny disciplíny, Camp a Edelrid jsou spojeny především s lehkým horským vybavením a Singing Rock a Ocún patří mezi české značky s modely pro halu i skálu. Mezi dětskými úvazky lze najít také Edelweiss. Všechny uvedené firmy vyrábějí certifikovaný lezecký materiál, takže rozhodují detaily střihu a nastavení spíš než logo.</p>'
        '<h2>Jak zvolit velikost</h2>'
        '<p>Velikost sedáku se řídí obvodem pasu a obvodem stehna, nikoli konfekční velikostí oblečení. Výrobce uvádí rozsah pasu pro každou velikost a rozsah nastavení smyček. Při měření si oblečte to, co budete nosit při lezení, a pás veďte nad kyčelními kostmi, ne přes bříško. Sedák by měl při visu v laně sedět na bocích a nesmí klouzat nahoru, ani když si ho dotáhnete jen mírně.</p>'
        '<ul><li><strong>Pás:</strong> po dotažení musí zůstat mezi pásem a tělem rezerva zhruba na dlaň, jinak se vám bude těžko dýchat při visu.</li>'
        '<li><strong>Smyčky na stehna:</strong> pevné jsou lehčí a bez možnosti nastavení, nastavitelné se přizpůsobí zimnímu i letnímu oblečení.</li>'
        '<li><strong>Zadní popruh:</strong> kontrolujte, aby nezůstal trčet dolů, a aby podpíral spodní část zad.</li>'
        '<li><strong>Přezky:</strong> samosvorné přezky šetří čas a nelze je nechat nezajištěné, běžné se zajišťují protažením popruhu zpět.</li></ul>'
        '<p>U dětí rozhoduje výška a poměr těla. Dítě s užšími boky může mít klasický sedák příliš uvolněný, proto se pro malé děti volí celotělový úvazek s hrudním pásem. Kdy přejít na dospělý sedák, poradí výrobce a instruktor, ne věk dítěte.</p>'
        '<h2>Dámský a pánský sedák</h2>'
        '<p>Dámské úvazky mají kratší vzdálenost mezi pasem a smyčkami na stehna, užší pás a často širší smyčky, aby seděly na bocích. Pánské jsou ve středu rovnější a mají delší hrudní část. U unisex modelů je důležité správné nastavení, protože ženy s užším pasem a širšími boky často potřebují jinou velikost pásu a smyček. Podle rozměrů vyberte pásový rozsah a smyčky zvlášť a nepřebírejte slepě označení pro pohlaví.</p>'
        '<h2>Jak nastavit a zkontrolovat sedák před lezením</h2>'
        '<ol><li>Oblékněte sedák tak, aby smyčky na stehna ležely rovně a nebyly zkroucené.</li>'
        '<li>Pás dotáhněte nad kyčlemi a zkontrolujte, že přezka je správně protažená zpět.</li>'
        '<li>Stehenní smyčky dotáhněte tak, aby pod ně prošly dva prsty.</li>'
        '<li>Zkontrolujte spojku mezi pasem a smyčkami: na předním uzlovém bodě musí být nepoškozená.</li>'
        '<li>Partnerská kontrola: spolulezec se podívá na přezky, uzel a jisticí smyčku, než vstoupíte do cesty.</li></ol>'
        '<h2>Péče a životnost</h2>'
        '<p>Sedák je textilní výrobek a stárne i bez lezení. Ultrafialové záření, pot, sůl, písek, chemikálie a mechanické oděrky vlákna oslabují. Výrobci u svých úvazků uvádějí maximální dobu životnosti textilií, která se počítá od data výroby. Vždy ji zkontrolujte v návodu konkrétního modelu a nespoléhejte na paměť. Lezcům, kteří visí v laně každý týden, vydrží sedák kratší dobu než občasným návštěvníkům haly.</p>'
        '<ul><li>Perte ho ve vlažné vodě s jemným mýdlem, bez aviváže a bez chemických odstraňovačů skvrn.</li>'
        '<li>Sušte ho ve stínu, daleko od radiátoru a od ohně.</li>'
        '<li>Skladujte ho suchý, chráněný před světlem, palivy, rozpouštědly a kyselinou z baterií.</li>'
        '<li>Vyřaďte ho po velkém pádu, při proděravění, přetřených nosných švech nebo zjevném opotřebení uzlového bodu.</li></ul>'
        '<h2>Šedé a neutrální barvy</h2>'
        '<p>Sedáky se vyrábějí v pestrých barvách, ale šedá a béžová patří k praktickým: špína a pot se na ní méně vidí a po delším používání vypadá sedák pořád slušně. Na druhé straně výrazná barva pomůže, když lezec visí v laně a ostatní jej hledají očima ve stěně. Pro halu vybírejte podle chuti, pro skialpinismus a ledovec podle viditelnosti. Pro opotřebení nebo kontrolu švů barva nehraje roli, rozhoduje stav textilu.</p>'
        '<h2>Sedák a lezecké boty jako sada</h2>'
        '<p>Začínající lezec obvykle shání nejdřív sedák a boty. Sedák půjčený z haly ušetří při prvních pokusech, ale vlastní sedí lépe a víte, co se s ním dělo. U bot se vyplatí vybírat podle stylu lezení, a ne podle sedáku. Značky jako ' + B(('la-sportiva', 'La Sportiva'), ('scarpa', 'Scarpa'), ('red-chili', 'Red Chili')) + ' mají sortiment bot od pohodlných začátečnických po agresivní výkonnostní. Přehled najdete ve výběrech <a href="/la-sportiva-lezecky/">La Sportiva lezečky</a> a <a href="/ocun-lezecky/">Ocún lezečky</a> a v kategorii <a href="/lezecke-boty/">lezečky</a>.</p>'
        '<h2>Co dalšího k sedáku patří</h2>'
        '<p>K sedáku se kupuje jisticí pomůcka, karabiny, expresky a smyčky. Dohromady tvoří bezpečnostní řetěz, v němž nesmí být slabý článek. Batoh na výlet k cestě vyberte v kategorii <a href="/turisticke-batohy/">turistické batohy</a>. Přehled lan, karabin a ferrat je v kategorii <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>. Pro vícedélkové cesty a horské túry zase hledejte přilby a další vybavení ve <a href="/lezecke-sedaky-a-pomucky/">sdílené kategorii pomůcek</a> a širší výběr v části <a href="/horolezectvi/">horolezectví a ferraty</a>.</p>'
        '<h2>Časté chyby při koupi</h2>'
        '<ul><li>Kupovat podle hmotnosti na prospektu, aniž byste sedák vyzkoušeli. Lehký úvazek nemusí pohodlně držet při dlouhém visu.</li>'
        '<li>Přehlížet nastavení smyček. Pevné smyčky nejsou vhodné, pokud lezete v zimě i v létě.</li>'
        '<li>Nechat si sedák půjčit od kamaráda jiné postavy. Velikost se řídí vaším tělem.</li>'
        '<li>Používat sedák s neznámou historií. Stáří a pády nejde z pohledu odhadnout.</li>'
        '<li>Podceňovat polstrování při opakovaném visu v laně, například u projektování cest.</li></ul>'
        '<h2>Kdy kupovat a jak porovnat nabídky</h2>'
        '<p>Sedáky se objevují ve slevách při obměně modelové řady a na začátku sezóny se ceny obvykle drží. Před objednávkou ověřte rok výroby a poslední dostupnou velikost, protože sedák z dlouho ležícího skladu už mohl uplynout část životnosti. Při porovnávání se nedívejte jen na cenu, ale i na to, jestli obchod uvádí velikostní rozsah, hmotnost a certifikaci.</p>'
    ),
    faq=[
        ('Jaký je rozdíl mezi sedákem a úvazkem?', 'V češtině se oběma slovy označuje stejná věc: sedací úvazek, který drží lezce na laně. Slovo sedák se používá v hovorové řeči a v lezeckých obchodech, úvazek v návodech a v normách.'),
        ('Který sedák je nejlepší pro začátečníka?', 'Pro lezeckou halu a sportovní cesty se hodí polstrovaný sportovní sedák se čtyřmi poutky a nastavitelnými smyčkami na stehnech. Pohodlí při visu v laně je důležitější než nízká hmotnost.'),
        ('Mohu s jedním sedákem lézt v hale i v horách?', 'Ano, pokud zvolíte střední cestu: mírně polstrovaný model s nastavitelnými smyčkami. Na dlouhé túry s mnoha vrstvami oblečení se vyplatí lehčí alpský úvazek.'),
        ('Jak poznám správnou velikost sedáku?', 'Změřte obvod pasu nad kyčlemi a obvod stehna a porovnejte je s tabulkou výrobce. Při visu v laně musí sedák sedět na bocích a nesmí klouzat nahoru.'),
        ('Kam se zavazuje lano?', 'Pouze do předního uzlového bodu, který výrobce označuje v návodu. Do poutek na materiál se lano nevazí, nejsou na zachycení pádu určená.'),
        ('Jaký sedák vybrat pro dítě?', 'Pro malé děti se používá celotělový úvazek nebo kombinace sedáku a hrudního pásu, protože nemají dostatečně vyvinuté boky. Jakmile dítě vyroste, přechod na sedák doporučí výrobce nebo instruktor.'),
        ('Jak dlouho sedák vydrží?', 'Podle návodu konkrétního modelu a podle toho, jak často a v jakých podmínkách lezete. Výrobci udávají maximální dobu životnosti textilií od data výroby, často v řádu let. Po velkém pádu nebo poškození švů vyřaďte sedák hned.'),
        ('Jak sedák vyprat?', 'Ve vlažné vodě s jemným mýdlem, ručně a bez aviváže. Nesušte jej na radiátoru ani na přímém slunci, chraňte před chemikáliemi.'),
        ('Je dámský sedák něčím lepší než pánský?', 'Je tvarovaný na užší pas a širší boky, takže ženám často sedí pohodlněji. Rozhodují ale rozměry těla, ne pohlaví, proto zkontrolujte tabulku velikostí a rozsah nastavení.'),
    ],
)

# ------------------------------------------------------------------ altra-bezecke-boty
NEW['altra-bezecke-boty'] = dict(
    title='Altra běžecké boty: nulový drop a široká špice',
    desc='Altra běžecké boty s nulovým dropem a širokou špicí: které modely se hodí na trail a silnici, jak sedí, kdy přejít a s čím je porovnat.',
    intro='<p>Altra je americká značka, která se stala synonymem pro běžecké boty s nulovým dropem a prostornou špicí ve tvaru chodidla. Pata a přední část leží v jedné výšce, takže chodidlo stojí tak, jak ho učinila příroda. Většina nabídky míří na trail, kde se výrazně uplatňuje model Lone Peak, ale mezi přehledem najdete i silniční a tlumené typy. Na této stránce vysvětlíme, v čem se Altra liší od klasických bot, kterým běžcům sedí a jak přejít na nulový drop bez zranění. Základní kategorii najdete v <a href="/bezecka-obuv/">běžeckých botách</a>. Předem upozorňujeme, že žádná bota nevyhovuje všem, a proto uvádíme i situace, kdy se jiná značka hodí lépe.</p>',
    guide=(
        '<h2>Čím se Altra liší od ostatních značek</h2>'
        '<p>Dvě věci poznáte hned: tvar a drop. Špice je široká a dává prstům prostor, aby se při došlapu rozevřely. A drop, tedy výškový rozdíl mezi patou a špičkou, je nulový. Klasická běžecká obuv má obvykle několik milimetrů navíc pod patou, což mění postavení chodidla a zátěž lýtek a achilovky. Altra tuto stupňovitou stavbu nepoužívá, takže vaše chůze a došlap se mění trochu jinak než v botách jiných značek.</p>'
        '<p>Neznamená to, že jde o minimalistické boty bez tlumení. Značka nabízí modely s tlumením od lehčího až po vysoké, takže nulový drop a tlumení se spojit dají. Rozhoduje podrážka, ne drop.</p>'
        '<h2>Modely, které se v nabídce opakují</h2>'
        + T(['Model', 'Zaměření', 'Pro koho'], [
            ['Lone Peak', 'trail, technický i smíšený terén', 'běžci a turisté, kteří chtějí univerzální trailovou botu'],
            ['Timp', 'trail, delší vzdálenosti', 'běžci, kterým vyhovuje měkčí a stabilnější došlap'],
            ['Olympus', 'trail, vysoké tlumení', 'ultra běžci a těžší běžci, kteří chtějí víc měkkosti'],
            ['Experience Flow a Experience Wild', 'silnice i trail, lehčí běžecká obuv', 'běžci na rychlejší tréninky'],
            ['Torin', 'silnice, vysoké tlumení', 'běžci hledající komfort na asfaltu'],
            ['Paradigm', 'silnice, stabilita', 'běžci, kteří preferují podporu klenby'],
            ['Voyager', 'chůze a lehčí běh', 'začínající běžci, rychlá chůze']]) +
        '<p>Nejčastěji nabízený je Lone Peak, který se vyrábí v několika barevných provedeních, v pánské i dámské verzi, v široké variantě i s membránou Gore-Tex. Pokud neznáte typ svého chodidla ani styl, začněte s ním nebo s modelem Timp.</p>'
        '<h2>Pro koho jsou boty Altra vhodné</h2>'
        '<ul><li><strong>Běžci se širokým předonožím:</strong> boty nestlačují prsty a nevznikají otlaky na malíčku.</li>'
        '<li><strong>Trailoví běžci a turisté:</strong> rovná podrážka dává stabilitu v technickém terénu.</li>'
        '<li><strong>Lidé, kteří trpí na nohy v úzkých botách:</strong> prostor pro prsty uleví při otocích a při bolestech v předonoží.</li>'
        '<li><strong>Běžci na dlouhé tratě:</strong> chodidlo bobtná a prostor ve špici je důležitý.</li></ul>'
        '<p>Naopak pokud potřebujete boty s úzkým, přiléhavým střihem na rychlé tempo nebo na překážkové závody, Altra tak dobře sedět nebude. Zkuste užší model jiné značky, například z řady ' + B(('hoka', 'Hoka'), ('salomon', 'Salomon'), ('saucony', 'Saucony')) + '.</p>'
        '<h2>Přechod z klasických bot na nulový drop</h2>'
        '<p>Největší chyba je přejít hned na plný objem. Lýtka a achilovka jsou zvyklé na zvýšenou patu a při náhlé změně se rychle unaví nebo bolí. Postupujte opatrně:</p>'
        '<ol><li>Prvních pár týdnů noste boty jen na chůzi a krátké procházky.</li>'
        '<li>Při běhu začněte kratšími vzdálenostmi, a ne celým tréninkem.</li>'
        '<li>Střídejte nové boty s dosavadním párem.</li>'
        '<li>Posilujte lýtka a chodidlo, například výpony a chůzí naboso doma.</li>'
        '<li>Při bolesti achilovky nebo lýtek přestaňte a zvolte měkčí tlumení.</li></ol>'
        '<p>Přechod trvá u každého jinak. Rychlost nezkracujte a spoléhejte na pocit, ne na kalendář.</p>'
        '<h2>Jak vybrat velikost a šířku</h2>'
        '<p>Díky široké špici sedí Altra obvykle pohodlně v běžné velikosti, ale zůstává potřeba rezerva před palcem asi na šířku palce. Při dlouhých sbězích se noha posouvá dopředu, proto prsty nesmí narážet na špici. Kdo má opravdu široké chodidlo, najde u řady modelů širší provedení označené slovem Wide. Dámské verze mají užší patu a užší střed než pánské, ale špice zůstává prostorná.</p>'
        '<p>Velikostní tabulku výrobce vždy porovnejte s délkou chodidla změřenou večer a zvažte ponožky, které budete nosit. Pro dlouhé trailové běhy se vyplatí o půl čísla víc, aby se noha mohla rozšířit.</p>'
        '<h2>Silnice nebo trail</h2>'
        '<p>Altra je silná zejména v terénu. Hrubá podrážka s výrazným vzorkem na Lone Peak dobře drží na hlíně, kořenech a mokrých kamenech. Pokud běháte výhradně po asfaltu, hledejte tlumenější silniční modely, které pomohou kloubům. Orientovat se můžete v podkategoriích <a href="/trailove-boty/">trailové běžecké boty</a> a <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>. Pro smíšenou trasu s kratším úsekem po silnici postačí lehčí trailový model s méně agresivním vzorkem.</p>'
        '<h2>Membrána, tlumení a gramáž</h2>'
        '<p>Některé modely se prodávají i v provedení s membránou Gore-Tex. Ta ochrání před deštěm a blátem, ale hůř odvádí teplo, takže se hodí do chladu a vlhka, v létě přehřívá. Tlumení určuje, jak měkce bota působí: vysoké snese delší vzdálenosti, nízké zase poskytuje lepší cit pro terén. Hmotnost bývá u trailových modelů vyšší než u silničních, protože mají hrubší podrážku a výztuhy.</p>'
        '<h2>Srovnání s jinými značkami</h2>'
        '<p>Na rozdíl od ' + B(('adidas', 'Adidas'), ('nike', 'Nike')) + ' se Altra nesoustředí na módní a závodní boty, ale na přirozený tvar chodidla. Značka ' + B(('new-balance', 'New Balance')) + ' nabízí rovněž širší střih, ale s klasickým dropem. Boty ' + B(('hoka', 'Hoka')) + ' mají hodně tlumení a mírný drop, takže pokud hledáte měkkost, ale nechcete se vzdát prostoru pro prsty, vyberte Olympus nebo Torin. Širší výběr najdete v <a href="/adidas-bezecke-boty/">Adidas běžeckých botách</a>, <a href="/nike-bezecke-boty/">Nike běžeckých botách</a> a <a href="/bezecke-boty-hoka/">Hoka</a>. Pro dámy je tu <a href="/bezecke-boty-damske/">dámský výběr</a>, pro děti <a href="/detske-bezecke-boty/">dětské běžecké boty</a>.</p>'
        '<h2>Nejčastější otázky před koupí</h2>'
        '<p>Než objednáte, položte si tři otázky: kde převážně poběžím, jak široké mám chodidlo a jaké tlumení jsem zvyklý. Odpovědi vás nasměrují k Lone Peak, Timp nebo silničnímu modelu. Pokud jste dosud běhali v klasické obuvi s vyšším dropem, počítejte s adaptací a nekupujte rovnou dva páry. Teprve po několika týdnech poznáte, jestli vám nulový drop sedí, a pak se vyplatí objednat další kousek, třeba v jiné barvě nebo s membránou.</p>'
        '<h2>Barvy a označení v katalogu</h2>'
        '<p>Značka často pojmenovává barevné provedení anglicky a zkratkami, například Black, Gray, Tan nebo Dusty Olive. U stejného modelu proto najdete několik položek s různou barvou. Rozdíl je jen v odstínu, ne ve stavbě. Písmeno M v názvu značí pánskou verzi, W dámskou. Při porovnání nabídek se řiďte názvem modelu, velikostí a barvou, ne popisem obchodu.</p>'
        '<h2>Šněrování a ponožky pro široké chodidlo</h2>'
        '<p>I v prostorné špici může noha při sbězích klouzat dopředu, a proto se vyplatí zvládnout šněrování. Pro pevnější fixaci paty protáhněte konec tkaničky horním očkem a vytvořte smyčku, kterou prostrčíte druhou stranou a dotáhnete. Tím se pata nezvedá a prsty se nezarývají do špice. Pokud vás tlačí nárt, vynechte jedno očko nad ním. Ponožky volte tenčí až středně silné, protože silné frotté zaberou místo, které jste v široké botě hledali. Ve vlhku se osvědčují vlněné nebo syntetické ponožky, bavlna nasákne a třene.</p>'
        '<h2>Altra jako turistická bota a na chůzi</h2>'
        '<p>Model Lone Peak a podobné trailové řady využijí i turisté, kteří nechtějí těžkou pohorku. Nízká hmotnost a prostor ve špici se oceňují při několikahodinových výšlapech, kdy chodidlo bobtná. Nevýhodou je menší opora kotníku než u vysoké pohorky, takže s těžším batohem na nerovném terénu pomůže pevný krok a nižší tempo. Pro dlouhou chůzi po zpevněných cestách bývá lepší tlumenější model s hladší podrážkou.</p>'
        '<h2>Pro koho je dámská verze</h2>'
        '<p>Dámské modely mají užší patu a středový díl a míří na užší chodidlo. Pokud máte širokou nohu, vyzkoušejte i pánskou verzi v menší velikosti, kterou výrobce uvádí v převodní tabulce. U dětí a dorostu je užší nabídka, přehled najdete v kategorii <a href="/detske-bezecke-boty/">dětské běžecké boty</a>.</p>'
        '<h2>Péče o boty</h2>'
        '<ul><li>Po trailu vyčistěte vzorek a zbytky bláta, aby se nehromadily v drážkách.</li>'
        '<li>Sušte přirozeně, mimo radiátor, protože teplo poškozuje lepení a pěnu.</li>'
        '<li>Vyjměte vložky a nechte vyschnout odděleně.</li>'
        '<li>Střídejte páry: pěna mezipodešve potřebuje čas se vrátit do tvaru.</li>'
        '<li>Boty vyměňte, když podrážka ztratí vzorek nebo střed pěny působí tvrdě.</li></ul>'
        '<h2>Kdy nakupovat</h2>'
        '<p>Starší kolekce se vyprodávají po uvedení nové generace modelu. Rozdíly mezi sousedními verzemi bývají malé, takže se vyplatí vzít předchozí číslování, pokud sedí velikost. Před koupí prověřte, jestli obchod uvádí přesný model a rok, a vyhněte se položkám bez popisu velikostního rozsahu.</p>'
    ),
    faq=[
        ('Co znamená nulový drop u bot Altra?', 'Pata a špice leží ve stejné výšce, rozdíl mezi nimi je nulový. Chodidlo stojí rovně, na rozdíl od běžných bot, kde je pata o několik milimetrů výš.'),
        ('Jsou boty Altra vhodné pro začátečníky?', 'Ano, ale přechod z klasické obuvi je třeba zvládnout postupně. Začátečníkovi pomůže tlumenější model a kratší vzdálenosti na začátku.'),
        ('Jaký model Altra vybrat na trail?', 'Univerzální volbou je Lone Peak. Pro vyšší tlumení na dlouhé tratě se hodí Olympus a pro měkčí a stabilnější došlap Timp.'),
        ('Jak velké boty Altra kupovat?', 'Obvykle ve stejné velikosti jako jiné boty, s rezervou před palcem asi na šířku palce. Pro dlouhé běhy zvažte o půl čísla víc.'),
        ('Mají boty Altra široký střih?', 'Špice je široká u všech modelů, pata a střed jsou středně široké. U některých řad existuje navíc provedení Wide.'),
        ('Hodí se Altra na silnici?', 'Ano, například modely Torin a Paradigm míří na asfalt a mají vyšší tlumení. Trailové typy s hrubým vzorkem na tvrdém povrchu rychleji ztrácejí vzorek.'),
        ('Bolí z nulového dropu lýtka a achilovka?', 'Při rychlém přechodu může, protože lýtka a achilovka musí pracovat v delším rozsahu. Postupné navyšování zátěže a posilování chodidel potíže většinou zmírní.'),
        ('Co znamená M a W v názvu modelu?', 'M je pánská verze (men), W dámská (women). Liší se střihem a velikostní řadou, ne celkovým určením.'),
        ('Jak dlouho boty Altra vydrží?', 'Záleží na terénu, váze a stylu běhu. Měňte je, když se zploští podrážka nebo když pěna ztratí odezvu, a ne podle počtu kilometrů.'),
    ],
)

# ------------------------------------------------------------------ ruzove-kopacky-nike
NEW['ruzove-kopacky-nike'] = dict(
    title='Růžové kopačky Nike: modely, povrchy a velikosti',
    desc='Růžové kopačky Nike: modely Mercurial, Phantom a Legend, rozdíly podle povrchu FG, MG a AG, dětské verze, barevné odstíny a péče o kopačky.',
    intro='<p>Růžová na kopačkách Nike není jen módní doplněk. Svítí na trávníku, hráče je vidět a její odstín sahá od jemné pastelové přes sytou fuchsiovou až po lososovou. Pod barvou se skrývají stejné modelové řady jako u jiných barev: lehké Mercurial pro rychlé hráče, Phantom pro přesnou kontrolu míče a Legend pro klasický střih. Na této stránce vysvětlíme, jak se v řadách vyznat, jak vybrat podrážku podle povrchu a postu na hřišti, jak pečovat o světlý povrch, aby ušpiněná tráva nezůstala na špici, a kdy se vyplatí sáhnout po dětské variantě. Přehled úrovní Club, Academy a Pro vám usnadní rozhodnutí. Obecný přehled najdete v kategorii <a href="/kopacky/">kopačky</a>.</p>',
    guide=(
        '<h2>Modelové řady Nike, které se objevují v růžové</h2>'
        '<p>Nike dělí kopačky podle stylu hry. Každá řada má jiný střih špičky, jinou vrchní část a jinou filozofii.</p>'
        + T(['Řada', 'Styl hry', 'Charakter'], [
            ['Mercurial (Vapor, Superfly)', 'rychlí hráči, křídla, útočníci', 'lehké, přiléhavé, tvarované pro sprint'],
            ['Phantom', 'tvořiví hráči, střelba a přihrávky', 'texturovaný povrch pro cit pro míč'],
            ['Legend', 'všestranní hráči, klasika', 'pohodlný střih, často tradiční materiály'],
            ['Club a Academy', 'amatérská a mládežnická hra', 'odolnější materiály, příznivější pro rozpočet'],
            ['Pro a Elite', 'ambiciózní hráči a profesionálové', 'nejlehčí a nejpřesnější konstrukce']]) +
        '<p>Označení Zoom Vapor a Zoom Superfly odpovídají lehčím kopačkám s důrazem na rychlost, zatímco Academy a Club míří na každodenní trénink. Pro dospělého amatéra, který hraje jednou až dvakrát týdně, bývá nejpraktičtější úroveň Academy, protože je odolná a nestojí tolik jako Pro.</p>'
        '<h2>Jak vybrat podrážku podle povrchu</h2>'
        '<p>Kopačky se označují zkratkami, které říkají, pro jaký povrch jsou určené. Nike používá hlavně tato označení:</p>'
        '<ul><li><strong>FG</strong> (firm ground): pevná přírodní tráva, kolíky pevně sedí.</li>'
        '<li><strong>MG</strong> (multi-ground): univerzální podrážka pro tvrdou a trochu měkčí trávu, někdy i pro umělou trávu.</li>'
        '<li><strong>AG</strong> (artificial grass): kratší a početnější kolíky na umělou trávu s gumovým granulátem.</li>'
        '<li><strong>IC</strong> (indoor court): plochá podrážka na hladký sálový povrch.</li>'
        '<li><strong>TF</strong> (turf): drobné pupky na tvrdý umělý povrch nebo antuku.</li></ul>'
        '<p>Kombinace FG/MG se v nabídce objevuje často, protože se hodí na většinu trávníků. Pokud hrajete hlavně na umělce, vyberte AG nebo TF, jinak se kolíky rychle sedřou a zvyšuje se riziko zranění kolen. Na halu se kopačky nepoužívají, tam patří sálová obuv.</p>'
        '<h2>Růžová: odstíny a jak se liší</h2>'
        '<p>Růžový odstín značky Nike se v katalogu pohybuje od světle růžové po sytě fuchsiovou a v kombinaci s černou, bílou nebo oranžovou. Obchody ji označují slovem růžová nebo anglickým pink. Přesný odstín poznáte až na fotografii, protože popis nemusí být přesný. Světlé odstíny působí jemněji, sytější více vyniknou na tmavém trávníku.</p>'
        '<ul><li><strong>Viditelnost:</strong> růžová je dobře vidět při večerním tréninku a při hře pod umělým světlem.</li>'
        '<li><strong>Kombinace s dresem:</strong> růžová se nehodí ke všem klubovým barvám. Zkontrolujte pravidla týmu, protože některé kluby vyžadují jednotnou obuv.</li>'
        '<li><strong>Špína:</strong> na světlé barvě je vidět blátivá hlína i stopy po trávě.</li></ul>'
        '<h2>Mercurial: rychlost v růžovém</h2>'
        '<p>Mercurial je nejlehčí z řad. Úzký střih obepíná chodidlo a špice je vyztužená pro sprinty. Hodí se hráčům s užším chodidlem. Širší nohy mohou na bocích tlačit, proto zkoušejte kopačky v obchodě nebo si pečlivě přečtěte hodnocení. Mercurial v růžové najdete v několika verzích: Vapor, Superfly a jejich juniorské provedení.</p>'
        '<h2>Phantom: cit pro míč</h2>'
        '<p>Phantom je určený hráčům, kteří chtějí cit pro míč a přesnost při střelbě. Vrchní materiál bývá texturovaný nebo tvarovaný, aby zlepšil kontakt. Střih je o něco širší než u Mercurialu a bývá příjemnější pro začátečníky a středně široké nohy. Verze Phantom GX II Academy v růžovém provedení je v nabídce zastoupena několika variantami.</p>'
        '<h2>Legend: klasika</h2>'
        '<p>Legend nabízí pohodlnější a méně extrémní střih. Hodí se obráncům a středopolařům, kteří potřebují stabilitu a odolnost. Při výběru zvažte, jestli chcete lehkou kopačku, nebo takovou, která vydrží celou sezónu v tréninku.</p>'
        '<h2>Dětské růžové kopačky Nike</h2>'
        '<p>Děti rostou rychle, proto se nevyplatí kupovat nejdražší model. Pro dětské kopačky platí následující pravidla:</p>'
        '<ul><li>Velikost vybírejte s rezervou asi jednoho palce, ne víc, jinak noha uvnitř klouže.</li>'
        '<li>Hrají-li děti na trávě, zvolte FG/MG. Na umělce AG.</li>'
        '<li>Juniorské verze značené Jr nebo Junior mají stejné řady jako dospělé, ale bývají měkčí a vyráběné z jednodušších materiálů.</li>'
        '<li>Kontrolujte velikost každé tři až čtyři měsíce.</li></ul>'
        '<p>Více v kategorii <a href="/detske-kopacky/">dětské kopačky</a>.</p>'
        '<h2>Jak kopačky správně vyzkoušet</h2>'
        '<ol><li>Zkoušejte je odpoledne, kdy je noha největší.</li>'
        '<li>Vezměte si ponožky, ve kterých budete hrát.</li>'
        '<li>Palec by neměl narážet na špici a pata nesmí uhýbat při chůzi.</li>'
        '<li>Zkuste krátký sprint a zastavení, ať poznáte, zda špice netlačí.</li>'
        '<li>Syntetický materiál se nerozšlape tolik jako kůže, takže těsné kopačky se nikdy nespraví.</li></ol>'
        '<h2>Kopačky podle postu na hřišti</h2>'
        '<p>Barva i značka jsou druhotné, pokud kopačky nesedí k tomu, co děláte na hřišti. Útočníci a křídla ocení lehkost a přiléhavost, kterou nabízí Mercurial, protože každý gram a každý milimetr mezi nohou a míčem se při sprintu počítá. Tvůrčí záložníci, kteří rozdávají přihrávky a střílejí zpoza vápna, hledají cit a stabilní kontakt s míčem, proto sáhnou po Phantomu. Obránci stráví hodně času v zákrocích, zastavování a soubojích, takže jim vyhovuje odolnější Legend nebo Academy s pevnější špicí. Brankáři si obvykle volí lehčí kopačky s ohledem na odkopy a pohyb, rukavice jsou samostatná kapitola. Víc o disciplíně najdete v kategorii <a href="/fotbal/">fotbal</a>.</p>'
        '<h2>Materiál vrchu: syntetika a kůže</h2>'
        '<p>Většina kopaček v růžové barvě má syntetický vrch. Syntetika je lehká, nepřijímá vodu a nemění se po vlhku a barvy na ní vydrží zářivé. Nevýhodou je, že se tolik nerozšlape, takže kopačky musí od začátku sedět. Kůže se přizpůsobí tvaru nohy, ale ve vlhku nasákne a těžkne a barevné odstíny, jako je růžová, se u ní vyrábějí méně často. Pokud si chcete kopačky rozchodit, nenoste je celý den po městě, ale používejte je krátce na tréninku.</p>'
        '<h2>Ponožky, štulpny a chrániče</h2>'
        '<p>Do kopaček patří tenčí sportovní ponožky, které netlačí a drží se na noze. Kopačky se nosí bez volného prostoru, takže silná zimní ponožka bývá vyloženě na překážku. Přes ponožku se oblékají štulpny a pod ně chrániče holení, které povinně patří do výbavy v zápasech. Výběr najdete v kategorii <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>. Při chladném počasí zvolte tenkou termoponožku, nikoli silnější vrstvu.</p>'
        '<h2>Jak číst označení modelu</h2>'
        '<p>Název kopaček Nike nese několik informací najednou. Číslice za názvem řady značí generaci, například Vapor 16 nebo Superfly 10, takže novější číslo je novější verze. Zkratky Jr a Junior označují dětské provedení. Slovo Zoom naznačuje lehčí provedení, které míří na rychlost. U dlouhých kódových označení, jako jsou FQ nebo HF následované číslem, jde o interní číslo barevného provedení a konkrétní model musíte ověřit podle fotografie a popisu. Chcete-li identickou barvu a střih, držte se kódu a ověřte si u něj správný povrch a velikost.</p>'
        '<h2>Kdy kopačky vyměnit</h2>'
        '<ul><li>Kolíky jsou ohlazené nebo ulomené a bota klouže.</li>'
        '<li>Horní díl se odlepuje od podrážky nebo praskl v ohybu.</li>'
        '<li>Stélka se promáčkla a noha v botě drží špatně.</li>'
        '<li>Dítě vyrostlo a prsty se dotýkají špice.</li>'
        '<li>Zjistíte, že vám sedí lépe jiný střih.</li></ul>'
        '<p>Hrajete-li pravidelně dvakrát týdně, vydrží kopačky obvykle jednu až dvě sezóny. Při dvou párech, třeba na trávu a na umělku, se opotřebení rozdělí a každý pár vydrží déle.</p>'
        '<h2>Péče o světlé kopačky</h2>'
        '<p>Světlý povrch je citlivý na špínu a trávu. Po tréninku odstraňte hrubou špínu kartáčem, kopačky otřete vlhkým hadrem a nechte je vyschnout při pokojové teplotě. Nikdy je nesušte na radiátoru ani u kamen, lepidlo by povolilo a materiál se zdeformuje. Do vlhkých kopaček vložte noviny nebo papírové utěrky, které nasají vlhkost. Neperte je v pračce. Kopačky skladujte na suchém místě, ne v uzavřené tašce.</p>'
        '<h2>Další značky a odstíny</h2>'
        '<p>Pokud hledáte jiné modely, projděte si obecný výběr <a href="/kopacky-nike/">kopaček Nike</a> nebo jiné značky: <a href="/kopacky-adidas/">Adidas</a>, <a href="/kopacky-puma/">Puma</a>, <a href="/new-balance-kopacky/">New Balance</a>, <a href="/joma-kopacky/">Joma</a>, <a href="/mizuno-kopacky/">Mizuno</a> a <a href="/kopacky-under-armour/">Under Armour</a>. Každá značka má jiný střih: Mizuno je známé klasickými střihy, Adidas nabízí podobně široké řady pro různé styly hry, Puma má vlastní tvar špičky. Značky ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma')) + ' mají v růžové největší zastoupení.</p>'
        '<h2>Kdy koupit a na co si dát pozor</h2>'
        '<p>Kopačky se vyprodávají při uvedení nové generace řady, často po mistrovství nebo na konci sezóny. Barevné provedení se po vyprodání nemusí vrátit. Pokud se vám barva líbí a velikost sedí, neváhejte. Pozor na položky bez označení povrchu: kopačky pro špatný povrch zbytečně namáhají klouby.</p>'
    ),
    faq=[
        ('Jaký odstín růžové mají kopačky Nike?', 'Odstíny jsou od pastelově světlé po sytou fuchsiovou, často v kombinaci s černou, bílou nebo oranžovou. Přesný odstín posuďte podle fotografie.'),
        ('Které řady Nike jsou v růžové nejčastější?', 'V nabídce se objevují Mercurial (Vapor, Superfly), Phantom a Legend. Najdete je v úrovních Club, Academy a Pro.'),
        ('Co znamená FG/MG u kopaček Nike?', 'Kombinace FG a MG označuje podrážku pro pevný a univerzální trávník. Hodí se na většinu hřišť s přírodní trávou.'),
        ('Mohu hrát v kopačkách FG na umělé trávě?', 'Nedoporučuje se. Delší kolíky se na umělé trávě zasekávají a zvyšují riziko zranění kolen, použijte AG nebo TF.'),
        ('Jak vybrat velikost dětských kopaček?', 'Nechte rezervu asi jeden palec před špičkou a kontrolujte velikost každé tři až čtyři měsíce, protože dítě rychle roste.'),
        ('Je Mercurial vhodný pro široké chodidlo?', 'Střih je úzký a přiléhavý. Pokud máte široké chodidlo, zkuste Phantom nebo Legend, které bývají prostornější.'),
        ('Čím se liší Academy, Club a Pro?', 'Club a Academy jsou odolnější a určené pro trénink a amatérskou hru. Pro je lehčí, přesnější a obvykle dražší.'),
        ('Jak vyčistit světlé kopačky?', 'Kartáčem odstraňte hrubou špínu, otřete vlhkým hadrem a nechte vysušit při pokojové teplotě. Neperte je v pračce a nesušte u radiátoru.'),
        ('Mohu kopačky nosit i mimo hřiště?', 'Nedoporučuje se. Kolíky se na tvrdém povrchu sedřou a bota ztratí funkci. Na ulici a do školy si vezměte tenisky.'),
    ],
)

# ------------------------------------------------------------------ navijaky-penn
NEW['navijaky-penn'] = dict(
    title='Navijáky Penn: řady Spinfisher, Slammer a multiplikátory',
    desc='Navijáky Penn: přehled řad Spinfisher, Slammer, Battle, Clash a multiplikátorů Fathom, jak vybrat velikost a brzdu a kdy zvolit slanou vodu.',
    intro='<p>Penn je americká značka, která se dlouho specializuje na navijáky pro mořský rybolov a těžké přívlače. Ve výběru najdete odolné spinningové navijáky s kovovými těly a multiplikátory s brzdou pákovou nebo hvězdicovou. Rozhodující je řada, velikost a odolnost proti slané vodě, ne jen číslo na boku. Značku volí rybáři, kteří chtějí naviják na dlouhá léta a nevadí jim vyšší hmotnost. Níže vysvětlíme, v čem se Penn liší od konkurence, jak se orientovat v označení řad a velikostí a k čemu se jednotlivé typy hodí. Obecný přehled všech značek najdete v kategorii <a href="/rybarske-navijaky/">navijáky</a>. K navijáku patří i prut a vlasec, na které odkazujeme níže, abyste soupravu poskládali bez chyb.</p>',
    guide=(
        '<h2>Kde Penn vyniká</h2>'
        '<p>Značka vyrábí navijáky hlavně pro náročné podmínky: moře, silné ryby, dlouhé hody a těžké přívlače. Typické jsou pevná těla, utěsněné brzdy a převody, které snesou vysokou zátěž. Pro řeky a rybníky s drobnější rybou je Penn spíš nadstandard, ale mořský a kapitální rybolov se bez podobných navijáků neobejde.</p>'
        '<h2>Řady a typy, které se v nabídce objevují</h2>'
        + T(['Řada', 'Typ', 'Zaměření'], [
            ['Spinfisher', 'spinningový naviják, utěsněný', 'slaná voda, přívlač z pobřeží i lodi'],
            ['Slammer', 'spinningový, robustní', 'těžká mořská přívlač, velké ryby'],
            ['Battle', 'spinningový, kovové tělo', 'všestranný, od sladké vody po moře'],
            ['Clash', 'spinningový, kovové tělo', 'přívlač v moři a na pobřeží'],
            ['Pursuit', 'spinningový', 'základní řada pro začátečníky'],
            ['Fierce, Conflict, Wrath', 'spinningové střední třídy', 'přívlač ze břehu, mořský rybolov'],
            ['Authority', 'spinningový vyšší třídy', 'dlouhé boje s velkými rybami'],
            ['Vantage, Tidal, Rival Long Cast', 'dálkový hod, surfcasting', 'dlouhé nahazování z pláže a ze břehu'],
            ['Fathom, Squall, Senator, International', 'multiplikátory', 'hluboký mořský rybolov, jigging, trolling']]) +
        '<p>Řadu poznáte podle názvu, číslice za ním značí generaci. Velikost, například 4000, 6500 nebo 8500, určuje kapacitu cívky a sílu. Písmeno H znamená vysoký převod, písmeno C nebo LL jinou úpravu cívky.</p>'
        '<h2>Spinning nebo multiplikátor</h2>'
        '<p>Spinningový naviják je univerzální: vlasec odchází z pevné cívky a hod je jednodušší. Multiplikátor má otáčivý buben, který lépe zvládne těžké zátěže, ale vyžaduje cit při nahazování, jinak vzniká zacuchaný vlasec. Pro hlubokomořské rybaření a jigging se používá multiplikátor s pákovou brzdou. Pro začátečníky je rozumnější spinning.</p>'
        '<ul><li><strong>Spinning:</strong> jednoduchý hod, vhodný pro začátečníky i pokročilé.</li>'
        '<li><strong>Multiplikátor:</strong> vyšší síla a přesnější ovládání brzdy, vyžaduje cvik.</li>'
        '<li><strong>Elektrický multiplikátor:</strong> pro hlubokomořský rybolov, vyžaduje zdroj a samostatnou soupravu.</li></ul>'
        '<h2>Jak vybrat velikost</h2>'
        '<p>Velikost navijáku musí odpovídat prutu a lovené rybě. Příliš malý naviják nezvládne vlasec potřebné síly, příliš velký zbytečně váží a vyvažuje prut špatně. Pro orientaci:</p>'
        + T(['Velikost', 'Použití', 'Poznámka'], [
            ['1000–3000', 'lehká přívlač, drobné ryby', 'sladká voda, lehké pruty'],
            ['4000–5000', 'střední přívlač, štika, candát', 'univerzální velikost'],
            ['6000–7500', 'těžká přívlač, pobřeží', 'silné ryby, silnější splétaná šňůra'],
            ['8000 a víc', 'velké ryby, dálkový hod, moře', 'těžší, vyžaduje delší a pevnější prut']]) +
        '<p>Velikosti se mohou lišit podle výrobce, proto vždy kontrolujte kapacitu cívky a údaj o brzdě, ne jen číslo.</p>'
        '<h2>Brzda a převod</h2>'
        '<p>Brzda rozhoduje o tom, jestli rybu udržíte. Mořské navijáky mají brzdu s uhlíkovými podložkami, která se hladce rozbíhá a nepřehřívá. Převod určuje, kolik vlasce se navine na jednu otáčku. Vysoký převod, označený H, je rychlý a hodí se na rychlé vodění nástrah. Nízký je silnější a vhodný pro těžké ryby. Najít ten pravý poměr znamená rozhodnout, co chcete lovit.</p>'
        '<h2>Slaná a sladká voda</h2>'
        '<p>Penn mnoho modelů přímo navrhuje pro slanou vodu. Utěsněné těleso a brzda omezují vnikání soli. I tak se po použití v moři naviják vypláchne sladkou vodou a vysuší. Sůl rychle koroduje kov i ložiska, a pokud ji necháte zaschnout, opotřebí se i dobrý naviják. Do sladké vody se hodí všechny řady, ale dražší mořské typy zbytečně váží.</p>'
        '<h2>Údržba navijáku</h2>'
        '<ol><li>Po rybolovu naviják opláchněte jemným proudem vody, nikoli tlakovou myčkou.</li>'
        '<li>Povolte brzdu, aby se podložky nezmáčkly a neslepily.</li>'
        '<li>Nechte jej vyschnout při pokojové teplotě.</li>'
        '<li>Jednou za sezónu naneste olej na rukojeť a vodicí váleček. V nabídce je i speciální olej na navijáky.</li>'
        '<li>Při delším uložení uvolněte brzdu a vlasec.</li></ol>'
        '<h2>Jak naviják spárovat s prutem</h2>'
        '<p>Naviják a prut tvoří jednu soupravu. Pruty mají na štítku doporučenou hmotnost zátěže a sílu vlasce, a naviják s nimi musí souznít. Pokud pár zvolíte špatně, prut se přetěžuje nebo naopak zůstane měkký a neunese těžší rybu. Penn nabízí navijáky velikostí, které odpovídají mořským a těžkým přívlačovým prutům, proto s nimi nekombinujte jemné ultralight pruty. Výběr najdete v kategorii <a href="/rybarske-pruty/">rybářské pruty</a>.</p>'
        '<h2>Vlasec a splétaná šňůra</h2>'
        '<p>Na navijácích Penn se používá monofilní vlasec, splétaná šňůra nebo kombinace obou. Monofil je odolný, levnější a pružný, ale hůř přenáší záběr. Splétaná šňůra je tenčí, pevnější a přenáší záběr přesněji, ale nemá žádnou pružnost, takže brzdu musíte nastavit pečlivěji. Při přechodu na šňůru zvažte podložku z monofilu, aby šňůra neprokluzovala na cívce. Přehled najdete v kategorii <a href="/vlasce-a-snury/">vlasce a šňůry</a>.</p>'
        '<h2>Nastavení brzdy v praxi</h2>'
        '<p>Obecné pravidlo říká, že brzda se nastavuje na přibližně třetinu pevnosti vlasce. Nejlepší je ji vyzkoušet: vlasec protáhněte očky, uchopte jej a zatáhněte prutem, jako při záseku. Brzda má povolit dřív, než by vlasec praskl. Při zdolávání silné ryby ji dotahujte jen podle potřeby a ve stupních, aby se nepřehřála. Po rybolovu brzdu uvolněte, aby se podložky nesplácly.</p>'
        '<h2>Dálkový hod a surfcasting</h2>'
        '<p>Řady s označením Long Cast, Longcast nebo Spod mají větší cívku s mělčím profilem, aby vlasec odcházel s menším odporem. Hodí se pro nahazování na velké vzdálenosti z pláže nebo ze břehu, kde je cílem dostat nástrahu daleko. Takový naviják vyžaduje dlouhý a vyvážený prut s delší rukojetí. Pro krátký přívlačový hod z lodi nebo z mola nemá smysl.</p>'
        '<h2>Pravoruký a levoruký naviják</h2>'
        '<p>U multiplikátorů se při výběru zohledňuje strana, na které je klika. U některých modelů se prodává levoruká verze, u spinningů se klika přehazuje podle potřeby. Rozhodněte se podle toho, kterou rukou nahazujete a kterou točíte, a vyzkoušejte si obě varianty na prutu. Na štítku hledejte označení LH, levoruký.</p>'
        '<h2>Příslušenství</h2>'
        '<p>V nabídce Penn najdete i obal na naviják, olej a další drobnosti. Neoprenový obal, který se na multiplikátory nasazuje, chrání naviják při přepravě na lodi a v autě. Náhradní cívku zvažte, pokud střídáte vlasec a splétanou šňůru.</p>'
        '<h2>Srovnání s jinými značkami</h2>'
        '<p>' + B(('shimano', 'Shimano'), ('daiwa', 'Daiwa')) + ' se soustředí na lehké a hladké navijáky pro sladkou i slanou vodu. Penn se profiluje větší pevností a odolností, což zvyšuje hmotnost. ' + B(('okuma', 'Okuma'), ('dam', 'DAM'), ('westin', 'Westin')) + ' nabízejí střední třídu pro přívlač a feeder. Porovnejte je ve výběrech <a href="/navijaky-shimano/">Shimano</a>, <a href="/navijaky-daiwa/">Daiwa</a>, <a href="/navijaky-fox/">Fox</a> a <a href="/navijaky-dam/">DAM</a>.</p>'
        '<h2>Penn pro rybolov z lodi a z břehu</h2>'
        '<p>Na lodi se navijáku věnuje víc pozornosti a ruce jsou volné pro druhý prut, proto se tu uplatní pákové multiplikátory, které umožní rychle změnit zátěž brzdy. Z břehu a z mola převažuje spinning s větší cívkou, protože hod musí zvládnout překážky a vlny. V obou případech zkontrolujte, že prut a naviják vydrží zátěž a že máte po ruce náhradní cívku a olej. Pro přepravu navijáků na vodu je praktická <a href="/rybarske-tasky/">taška, pouzdro nebo krabička</a>, která naviják ochrání před nárazy a vlhkem.</p>'
        '<h2>Jak poznat kvalitní nabídku</h2>'
        '<ul><li>Název řady a velikost jsou uvedené plně, například Spinfisher VII a číslo velikosti.</li>'
        '<li>Je vidět převod, kapacita cívky a strana kliky.</li>'
        '<li>U multiplikátorů je zřejmé, jestli jde o levoruký nebo pravoruký model.</li>'
        '<li>V sadě nejsou skryté dodatečné položky, jako jsou obaly a oleje, které se často prodávají zvlášť.</li></ul>'
        '<p>Ostatní položky pro rybolov najdete v kategorii <a href="/rybarske-doplnky/">rybářské doplňky</a> a ve větším přehledu <a href="/rybareni/">rybaření</a>.</p>'
        '<h2>Opotřebení a kdy servis</h2>'
        '<p>Příznaky, že naviják potřebuje péči, jsou drhnutí při točení kličkou, kolísání brzdy a skřípání při záběru. Často stačí vyčistit a promazat, ale u dražších modelů se vyplatí svěřit práci servisu, protože rozebraný převod se špatně skládá zpátky. Za výměnu stojí cívka s poškozeným okrajem, protože takové místo vlasec trhá.</p>'
        '<h2>Komu se Penn vyplatí</h2>'
        '<ul><li><strong>Mořským rybářům:</strong> utěsněné těleso a silná brzda.</li>'
        '<li><strong>Přívlačářům na velké šelmy:</strong> štika, sumec, velké mořské ryby.</li>'
        '<li><strong>Rybářům, kteří cení robustnost před hmotností:</strong> pevné kovové tělo.</li>'
        '<li><strong>Cestovním rybářům:</strong> navijáky vydrží i hrubší zacházení.</li></ul>'
        '<p>Naopak pro lehkou přívlač na rybníce, ultralight a feeder jsou vhodnější lehčí navijáky jiných značek.</p>'
        '<h2>Kdy koupit</h2>'
        '<p>Starší generace řad se vyprodávají po uvedení novinek, často na jaře a na podzim. Rozdíly mezi sousedními generacemi bývají malé. Před koupí si ověřte, že obchod uvádí velikost a převod, protože se v nabídce často opakuje stejný název s různými velikostmi.</p>'
    ),
    faq=[
        ('Jaké řady navijáků Penn jsou nejčastější?', 'Najdete především Spinfisher, Slammer, Battle, Clash, Pursuit, Fierce a Conflict a multiplikátory Fathom, Squall a Senator.'),
        ('Je Penn vhodný do sladké vody?', 'Ano, ale mořské řady jsou těžší a robustnější. Pro lehkou přívlač do sladké vody vyberte menší velikost nebo jednodušší řadu.'),
        ('Co znamená písmeno H v názvu navijáku?', 'H označuje vysoký převod. Naviják sbírá víc vlasce na jednu otáčku a hodí se na rychlé vodění nástrah.'),
        ('Spinning nebo multiplikátor?', 'Pro začátečníky a většinu přívlače je jednodušší spinning. Multiplikátor se hodí na těžký mořský rybolov a vyžaduje cvik.'),
        ('Jakou velikost navijáku Penn zvolit?', 'Podle prutu a lovené ryby: 1000–3000 na lehkou přívlač, 4000–5000 jako univerzální a 6000 a víc na těžký rybolov a moře.'),
        ('Jak pečovat o naviják po moři?', 'Opláchněte jej sladkou vodou, povolte brzdu a nechte vysušit. Sůl rychle koroduje a bez oplachu zničí i kvalitní naviják.'),
        ('Je elektrický multiplikátor pro každého?', 'Ne. Je určen hlavně pro hlubokomořský rybolov a vyžaduje napájení a vhodný prut.'),
        ('Mohu na Penn navinout splétanou šňůru?', 'Ano, většina modelů je pro ni vhodná. Zkontrolujte, že cívka má kapacitu pro zvolený průměr, a pro jistotu použijte podložku z monofilu.'),
        ('Jak často mám naviják mazat?', 'Obvykle jednou za sezónu a po rybaření v moři ihned po oplachu. Použijte olej určený na navijáky a nepřehánějte množství.'),
    ],
)
