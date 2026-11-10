"""sporteka.cz — wave 18a (4. 11. 2026): long texts (>= 1650 words) for lyzarske-boty, padel, kabaty-a-parky, plastenky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-boty
NEW['lyzarske-boty'] = dict(long=True,
    title='Lyžařské boty: velikost, flex, tvar a výběr',
    desc='Sjezdové lyžařské boty pánské, dámské i dětské. Jak zvolit Mondopoint, flex, šířku skeletu a zapínání a kde porovnat nabídky obchodů.',
    intro='<p>Lyžařská bota je spojnicí mezi tělem a lyží, a proto o pohodlí i o ovladatelnosti rozhoduje velkou měrou. '
          'Příliš velká bota nechá nohu klouzat a zatáčky se rozmažou, příliš těsná zastaví krevní oběh a zkazí odpoledne. Správná bota drží patu, nechává prstům trochu místa a přenáší pohyb holeně na hranu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u pánských, dámských i dětských modelů od značek jako Rossignol, K2, Head, Nordica nebo Tecnica. '
          'Při skládání celé výbavy se podívejte i na <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyzarske-vazani/">lyžařské vázání</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/lyzarske-helmy/">helmy</a>. '
          'Níže najdete postup od změření nohy po péči o boty po sezóně.</p>',
    guide='<h2>Z čeho se sjezdová bota skládá</h2>'
          '<p>Většina sjezdových bot má plastovou skořepinu s přezkami, plastovou manžetu kolem lýtka a vnitřní botu z pěnových materiálů. Skořepina určuje tuhost a geometrii, vnitřní bota komfort a teplo. Pod patou a špičkou jsou normované patky, do kterých zapadá vázání. '
          'Právě proto nejde obuv kombinovat libovolně: klasické sjezdové vázání vyžaduje klasickou patku a některé hybridní boty mají patky odlišné. Než model objednáte, ověřte u výrobce, s jakým typem vázání spolupracuje.</p>'
          + T(['Část boty', 'Funkce', 'Co sledovat'], [
              ['Skořepina', 'drží tvar a přenáší sílu', 'šířka skeletu, tuhost plastu'],
              ['Manžeta', 'opírá holeň', 'výška, nastavení náklonu a vůle'],
              ['Vnitřní bota', 'tlumí a izoluje', 'materiál, možnost tepelného tvarování'],
              ['Přezky a pásek', 'zavírají botu', 'počet přezek, mikronastavení, kovové nebo plastové'],
              ['Podrážka', 'styk s vázáním a zemí', 'typ patek, režim chůze, vyměnitelné patky']]) +
          '<h2>Velikost: Mondopoint a vnitřní délka</h2>'
          '<p>Lyžařské boty se nekupují podle čísla běžné obuvi. Základem je Mondopoint, který odpovídá délce chodidla v centimetrech. Chodidlo změřte ve stoje na papíře od paty k nejdelšímu prstu a výsledek porovnejte s tabulkou výrobce. '
          'Dvě značky se stejným údajem mohou sedět jinak, protože mají odlišný tvar vnitřní boty a rozdílnou délku vnitřního prostoru. Ten se označuje jako délka v milimetrech a rozhoduje o tom, zda bota nepůsobí stísněně.</p>'
          '<p>U zkoušky stoupněte do boty, zapněte přezky a předkloňte se do postoje. Pata se má opřít vzadu, prsty se mírně odtáhnou od špičky. V obchodě by bota měla tlačit o něco víc, než je příjemné při chůzi, protože vnitřní vložka se po několika dnech uleží. '
          'Pokud ale po deseti minutách palec ztrácí cit nebo se na nártu vytváří ostrý tlak, je model tvarem nevhodný, a ne jen nový.</p>'
          '<h2>Šířka skeletu a tvar nohy</h2>'
          '<p>Lyžařské boty mají udanou šířku skeletu v milimetrech, která se měří v přední části skořepiny. Užší modely kolem pravé stovky milimetrů padnou štíhlé noze a závodnějšímu stylu, širší rozměry jsou pohodlnější pro objemnější chodidlo. '
          'Výrobci jako Lange, Dalbello nebo Tecnica nabízejí oba extrémy a různé hodnoty mezi nimi. Šířka není to samé jako objem: dva lidé se stejnou délkou chodidla mohou mít odlišnou výšku nártu i objem lýtka.</p>'
          + T(['Typ nohy', 'Co se děje v ose', 'Co hledat'], [
              ['Úzká noha s nízkým nártem', 'noha se v botě pohybuje', 'užší skelet, těsnější vnitřní bota'],
              ['Široká noha', 'tlak na malíku a hlavičkách kostí', 'širší skelet, možnost rozšíření v servisu'],
              ['Vysoký nárt', 'tlak na horní straně nohy', 'bota s větším objemem a měkčím jazykem'],
              ['Silné lýtko', 'manžeta nejde zapnout', 'širší manžeta, nastavitelné zapínání']]) +
          '<h2>Flex: jak tuhá má bota být</h2>'
          '<p>Flex je číslo, které vyjadřuje tuhost manžety. Nižší hodnota se předkloní snadno, vyšší vyžaduje sílu i dobrou techniku. Porovnávat lze jen v rámci jednoho výrobce, protože každý měří trochu jinak. '
          'Pravidlo je prosté: bota má být tak tuhá, aby přenášela vaše úsilí, ale ne tak tvrdá, aby se v ní nedalo pracovat s kolenem.</p>'
          + T(['Úroveň lyžaře', 'Orientační flex', 'Charakter boty'], [
              ['Děti a úplní začátečníci', 'zhruba 40–70', 'měkká, odpouští chyby'],
              ['Rekreační a lehčí lyžaři', 'zhruba 70–100', 'pohodlná, snadno ovladatelná'],
              ['Pokročilí', 'zhruba 100–120', 'přesnější, vyžaduje techniku'],
              ['Sportovní a závodní styl', '120 a víc', 'tuhá, úzká, nízký komfort']]) +
          '<p>Tuhost ovlivňuje i tělesná hmotnost. Těžší lyžař ohne měkkou botu snadněji a získá méně opory, lehčí lyžař zase tvrdou botu neprohne. Nejde o to, co je lepší, ale co odpovídá vám. Mnoho rekreačních lyžařů kupuje příliš tuhé boty podle pocitu „profesionála“ a v nich pak jezdí v zadním posedu.</p>'
          '<h2>Typy bot podle způsobu lyžování</h2>'
          '<h3>Sjezdové rekreační</h3>'
          '<p>Nejpočetnější skupina. Cílí na pohodlí, jednoduché zapínání, širší skelet a měkčí flex. Velká část nabídky Rossignol, Nordica, Atomic a Salomon patří právě sem. Vhodné pro ty, kdo jezdí týden v roce a chtějí mít v noze teplo.</p>'
          '<h3>Sportovní a závodní</h3>'
          '<p>Užší, tužší, s nízkým objemem. Přenášejí sílu bez ztráty, ale v chůzi a při dlouhém sezení v lanovce jsou méně pohodlné. Dávají smysl, když lyžujete rychle a agresivně, jinak je zbytečně tvrdá bota spíš na škodu.</p>'
          '<h3>Boty s režimem chůze</h3>'
          '<p>Mají odblokovatelnou manžetu a často profilovanou podrážku s lepším záběrem. Hodí se pro freeride a lyžování mimo sjezdovku, případně pro ty, kdo chtějí snadno přejít do restaurace na svahu. Pokud plánujete výstupy na pásech, patří spíš do kategorie <a href="/skialpove-boty/">skialpové boty</a>.</p>'
          '<h3>Dětské boty</h3>'
          '<p>Rostoucí noha potřebuje bezpečný prostor, ale ne příliš velký. Dětské boty mají často kolečko nebo mikropřezky pro doladění a měkký flex. Boty se nekupují o dvě velikosti větší, protože dítě by v nich nemohlo lyži řídit. Při koupi je vhodné zkontrolovat, zda nesedí příliš volně v patě. K dětem patří <a href="/detske-lyze/">dětské lyže</a> a <a href="/lyzarske-helmy/">helma</a>.</p>'
          '<h2>Zapínání: přezky, BOA a hybridy</h2>'
          '<p>Nejčastější je čtyřpřezkový systém: dvě přezky na skořepině, jedna na nártu a pásek přes holeň. Mikronastavení umožňuje přizpůsobit utažení po milimetrech. Alternativou je systém BOA se kolečkem a ocelovými lanky. '
          'Utáhnete jedním pohybem a rovnoměrněji rozložíte tlak na nártu, ale oprava lanka bývá složitější než výměna přezky.</p>'
          '<p>Přezky se nemají přetahovat. Nejtěsněji zapněte nárt, který drží patu, a manžetu už jen pevně, ne tak, aby škrtila. Přetažená bota studí a bolí, protože tlačí na cévy.</p>'
          '<h2>Vnitřní bota, vložky a tepelné tvarování</h2>'
          '<p>Vnitřní bota není jen výplň. Termoformovatelná vložka se v servisu zahřeje a přizpůsobí kotníku, takže vymizí tlakové body. Pomůže i vkládání vlastní stélky, pokud máte problémy s klenbou nebo nestandardní postojem. '
          'Brusič v servisu může také upravit skořepinu v místě kosti, aniž by poškodil její konstrukci. Takové úpravy dělejte jen u odborníka.</p>'
          '<h2>Chůze, přenášení a doplňky</h2>'
          '<p>Hluboký profil podrážky a výměnné patky zlepšují jistotu na sněhu i na ledu před chatou. Do auta a v autobuse se boty přenášejí ve speciálním vaku, který chrání zapnuté přezky. Vaky a tašky najdete v kategorii <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a>. '
          'Na lyžování do mrazu pomáhají ohřívače nohou nebo zateplené návleky, ale základem zůstává tenká ponožka bez záhybů. Dvě vrstvy ponožek nepomáhají a zhoršují přenos pohybu.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Přehled srovnává modely značek {B(("rossignol", "Rossignol"), ("k2", "K2"), ("head", "Head"), ("nordica", "Nordica"), ("atomic", "Atomic"), ("salomon", "Salomon"), ("tecnica", "Tecnica"), ("fischer", "Fischer"), ("dalbello", "Dalbello"), ("lange", "Lange"), ("scarpa", "Scarpa"))}. '
          'Každá má své typické tvary. Někdo staví na úzkém závodním lastě, jiný na širším komfortním. Proto nenakupujte podle loga, ale podle toho, jak vám bota sedí.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě o číslo větší „pro jistotu“. Noha se pohybuje, lyže se hůř ovládá a prsty trpí tlakem při brzdění.</li>'
          '<li>Výběr podle vzhledu a ceny bez zkoušení. Dvě stejně velké boty od různých výrobců sedí rozdílně.</li>'
          '<li>Příliš tuhá bota pro rekreačního lyžaře, která zhoršuje ovládání.</li>'
          '<li>Dvě ponožky přes sebe. Zvýšený tlak a mokré nohy.</li>'
          '<li>Neodborně doladěná bota. Vybroušení a tepelné tvarování patří do servisu.</li></ul>'
          '<h2>Péče po jízdě a mimo sezónu</h2>'
          '<p>Po lyžování vyndejte vnitřní botu a nechte ji vyschnout při pokojové teplotě, ne na topení. Plastová skořepina by neměla být dlouho na horku, protože změkne a deformuje se. Přes léto boty uložte zapnuté na jednu přezku, aby manžeta nezůstala natažená. '
          'Před sezónou zkontrolujte přezky, pružiny a stav podrážky. Když se podrážka opotřebí a je jiná než norma patky, vázání může boty uvolnit jindy než má. Seřízení vázání nechte provést v servisu.</p>'
          '<h2>Na co se zeptat před koupí</h2>'
          '<p>Když si nevíte rady, vybavte se otázkami: jak často lyžujete, jak široké je vaše chodidlo, kde nejčastěji tlačí běžná obuv a jak zvládáte tuhou botu. Odpovědi vám zúží výběr víc než jakýkoli žebříček. '
          'Pro kompletní zimní vybavení zvolte i <a href="/lyzarske-bryle/">lyžařské brýle</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-termopradlo/">termoprádlo</a>, případně <a href="/lyzarske-obleceni/">oblečení</a>. Celý obor shrnuje kategorie <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[('Jak poznám správnou velikost lyžařských bot?', 'Změřte chodidlo a porovnejte hodnotu s Mondopointem u výrobce. Zkoušená bota má držet patu, prsty se mají v lyžařském postoji lehce odtáhnout od špičky a po deseti minutách nesmí nic bolet.'),
         ('Co znamená číslo flexu?', 'Je to tuhost manžety. Nižší číslo se snáz předkloní a hodí se pro děti, začátečníky a lehčí lyžaře. Vyšší patří pokročilým a sportovním lyžařům. Čísla se srovnávají jen v rámci jedné značky.'),
         ('Mohu lyžařské boty koupit online?', 'Ano, pokud znáte svůj Mondopoint a tvar nohy a obchod umožňuje vrácení. U první koupě je jistější vyzkoušet boty v prodejně nebo si nechat změřit nohu v servisu.'),
         ('Jaký je rozdíl mezi úzkou a širokou botou?', 'Šířka skeletu se udává v milimetrech v přední části skořepiny. Úzká sedí štíhlé noze a dává přesnější přenos, široká je pohodlnější. Špatná šířka způsobuje tlak na malíku nebo klouzání nohy.'),
         ('Jsou dámské boty jen zmenšené pánské?', 'Dámské modely mívají nižší manžetu, užší lýtko a měkčí flex a často jinak umístěnou přezku. Ženy s silnější nohou ale mohou sedět v pánském modelu, rozhodující je tvar nohy.'),
         ('Proč mě bota po čase přestane tlačit?', 'Vnitřní bota se po několika dnech uleží a zformuje se podle nohy. Ostrý bodový tlak ale neustoupí a řeší se úpravou skořepiny nebo tepelným tvarováním v servisu.'),
         ('Hodí se skialpové boty na sjezdovku?', 'Dají se použít, jsou lehčí a mají režim chůze, ale obvykle jsou měkčí a méně přesné. Jinak je řešením sjezdová bota s režimem chůze nebo klasická sjezdová. Kompatibilitu s vázáním ověřte u výrobce.'),
         ('Kolik ponožek obout do lyžáků?', 'Jednu tenkou lyžařskou ponožku bez švů, která sahá pod koleno. Více vrstev zvyšuje tlak, zhoršuje prokrvení a nohy pak studí. Bavlněné ponožky nepoužívejte, drží vlhkost.'),
         ('Jak boty skladovat přes léto?', 'Suché, v chladu, mimo přímé slunce a topení. Vnitřní botu předem vyndejte a vysušte, skořepinu zapněte na nejslabší stupeň. Boty ukládejte ve vaku, ne zbalené pod těžkými předměty.'),
         ('Jak dlouho bota vydrží?', 'Záleží na počtu dnů na svahu, péči a stavu podrážky. Měkne vnitřní bota, ztrácí se tlumení a pružiny v přezkách slábnou. Až když bota drží nohu volně nebo praskne skořepina, je čas na výměnu.'),
         ('Mám volit boty s BOA?', 'BOA zapíná rychleji a rovnoměrněji, ale dá se hůř opravit. Přezkový systém je osvědčený a opravitelný. Rozhodněte podle toho, co vám vyhovuje při nasazování v rukavicích.')])

# ------------------------------------------------------------------ padel
NEW['padel'] = dict(long=True,
    title='Padel: rakety, míče, obuv a výbava pro hráče',
    desc='Padelové rakety, míče, obuv a tašky. Jak zvolit tvar, váhu, vyvážení a materiál rakety a kde porovnat nabídky českých obchodů.',
    intro='<p>Padel je raketová hra, která se hraje ve dvojicích na uzavřeném kurtu s prosklenými stěnami. Rakety nemají struny, ale plný perforovaný povrch na pěnovém jádře, míč je podobný tenisovému s nižším tlakem a odraz od stěn se stává součástí hry. '
          'Díky tomu se základní údery učí snadno a hra baví i lidi, kteří dosud žádný raketový sport nezkusili.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u raket, míčů, obuvi, tašek a oblečení od značek jako Bullpadel, Kuikma, Head, Babolat nebo Wilson. '
          'Pokud váháte, jestli padel není pro vás, srovnejte si ho s příbuznými sporty jako <a href="/tenis/">tenis</a>, <a href="/squash/">squash</a> a <a href="/badminton/">badminton</a>. '
          'Další text vás provede tvarem, váhou i materiálem a doplní, jak se vyhnout nákupům, které pak leží ve skříni.</p>',
    guide='<h2>Co potřebujete na první zápas</h2>'
          '<p>Základní výbava je skromná. Potřebujete raketu, tlakové míče, obuv, která drží na kurtu, a pohodlné oblečení. Většina klubů nabízí půjčení rakety, takže první hodiny nemusíte nic kupovat. Teprve když zjistíte, že vás hra baví, má smysl vlastní vybavení. '
          'Padel se hraje dvojicemi, proto se často sdílejí míče: každý z týmu přinese jednu tubu a sady se střídají.</p>'
          + T(['Položka', 'K čemu je', 'Na co se zaměřit'], [
              ['Raketa', 'úder a kontrola míče', 'tvar, váha, vyvážení, materiál povrchu'],
              ['Míče', 'hra a trénink', 'tlak, určení pro padel, čerstvost'],
              ['Obuv', 'záběr a stabilita', 'vzorek podrážky, boční opora'],
              ['Taška nebo batoh', 'přenos výbavy', 'oddělení na raketu, ventilace'],
              ['Oblečení', 'volný pohyb', 'prodyšný materiál, kraťasy nebo sukně bez omezení'],
              ['Doplňky', 'držení a ochrana', 'omotávka, ochranná páska, poutko, potítko']]) +
          '<h2>Tvar rakety</h2>'
          '<p>Základní rozdělení je podle obrysu hlavy. Kulatý tvar má střed těžiště blíž k ruce, ideální bod odpalu je velký a odpouští chybný zásah. Diamant má těžiště vysoko v hlavě, dává sílu při smeči, ale vyžaduje přesnost. '
          'Slza leží mezi těmito extrémy a bývá výchozí volbou pro většinu hráčů, kteří už mají základní návyky.</p>'
          + T(['Tvar', 'Charakter', 'Komu vyhovuje'], [
              ['Kulatý', 'kontrola, velký sladký bod', 'začátečníkům a hráčům, kteří chtějí jistotu'],
              ['Slza (hybrid)', 'vyvážení výkonu a kontroly', 'středně pokročilým, univerzálním hráčům'],
              ['Diamant', 'síla, menší sladký bod', 'útočným hráčům s dobrou technikou']]) +
          '<p>Výrobci tvary pojmenovávají trochu jinak a hybridní konstrukce se těžko řadí. Spolehlivější než název je údaj o vyvážení a o poloze těžiště. Pokud popis nenapovídá, vyhledejte k modelu technický list nebo recenzi.</p>'
          '<h2>Váha a vyvážení</h2>'
          '<p>Padelové rakety jsou kolem tří set šedesáti gramů, v běžném rozmezí od lehčích po těžší. Nižší hmotnost šetří zápěstí a zrychluje reakce u sítě, vyšší dodá sílu do smečí a dlouhých úderů. '
          'Dlouhodobě je při výběru nejdůležitější, jak raketa leží v ruce: při koupi ji zvedněte, zamávejte s ní a poslouchejte tělo.</p>'
          '<p>Vyvážení určuje, jak se hmotnost rozděluje mezi hlavu a rukojeť. Raketa s hlavou vyváženou vpředu (head heavy) dává více síly a zátěže, raketa vyvážená vzadu je lehčí na ovládání a méně zatěžuje loket. '
          'Tenisový loket nebo bolest ramene nejsou u padelu neznámé, a proto je dobré začínat s lehčí, vyváženější raketou a těžší vyzkoušet až později.</p>'
          '<h2>Materiály: povrch a jádro</h2>'
          '<p>Rámy jsou nejčastěji z karbonových nebo skelných vláken, případně jejich kombinace. Karbon je tuhý, odezva je přímější a raketa lépe dává sílu. Sklolaminát je měkčí, odpouští a hodí se pro začátek. '
          'Jádro tvoří pěnová hmota EVA nebo podobné materiály s odlišnou tvrdostí. Měkčí jádro dává pohodlí a velký únik energie do míče, tvrdé zase přesnost a odezvu, ale vibrace jsou citelnější.</p>'
          + T(['Materiál', 'Vlastnost', 'Pro koho'], [
              ['Sklolaminát', 'měkčí, odpouští chyby, nižší tuhost', 'začátečníci, rekreační hráči'],
              ['Karbon', 'tuhý, přesný, vysoký výkon', 'pokročilí, soutěžní hráči'],
              ['Měkké jádro', 'komfort, menší vibrace', 'hráči s citlivým loktem'],
              ['Tvrdé jádro', 'rychlá odezva', 'útočné hráčky a hráči']]) +
          '<p>Povrch rakety bývá hladký nebo strukturovaný. Strukturovaný zvyšuje tření na míči a umožňuje silnější rotaci, ale se časem opotřebuje. Hladký je odolnější a přehlednější.</p>'
          '<h2>Rukojeť a omotávky</h2>'
          '<p>Rukojeť určuje, jak raketa sedí v dlani. Obvod má být takový, aby mezi prsty a dlaní zbylo místo na menší prst. Příliš silná omotávka brzdí zápěstí, příliš tenká způsobuje tlak. '
          'Omotávky se kupují zvlášť. Pokud se po několika zápasech lepí, ztrácí savost nebo se rozmotává, vyměňte ji. Poutko kolem zápěstí je v padelu povinné a mělo by být pevné, nepoškozené a pořádně utažené.</p>'
          '<h2>Míče</h2>'
          '<p>Míče na padel vypadají jako tenisové, ale mají nižší vnitřní tlak a srst je upravena pro hru na uzavřeném kurtu. Míče z tenisu se nehodí, jsou rychlejší a při odrazu od skla se chovají jinak. '
          'Nové míče mají živější odraz, po několika zápasech tlak klesá a hra zpomaluje. Skladujte je v tlakové tubě a uzavřete ji po každém tréninku. Pro tréninková kola lze koupit levnější míče, pro zápas čerstvé.</p>'
          '<h2>Obuv na padel</h2>'
          '<p>Tenisová, běžecká ani fotbalová obuv nenahradí padelovou. Kurt má umělou trávu s pískem a podrážka s rybí kostí nebo drobnými kuličkami drží na povrchu, aniž by se zasekla. '
          'Dobrá obuv má pevnou patu, boční oporu a ventilaci. Pokud hrajete víckrát týdně, mrkněte do kategorie <a href="/tenisova-obuv/">tenisová obuv</a> a <a href="/salova-obuv/">sálová obuv</a>, ale pro padel hledejte specifické označení. Základní přehled obuvi najdete v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Tašky a oblečení</h2>'
          '<p>Padelová taška má oddělení na jednu až tři rakety, boční kapsu na míče a oddíl na mokré věci. Prosté sportovní tašky se hodí, pokud rakety nosíte v ochranném obalu. Taška v autě na slunci nezůstává kvůli pěnovému jádru. '
          'Najít ji můžete v kategorii <a href="/sportovni-tasky/">sportovní tašky a ledvinky</a> nebo mezi <a href="/mestske-batohy/">městskými batohy</a>. Oblečení volte prodyšné. Hra je intenzivní a krátké kraťasy nebo sukně a funkční tričko jsou lepší než bavlna. '
          'Související kategorie: <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/funkcni-tricka/">funkční trička</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>'
          '<h2>Jak vybrat podle úrovně</h2>'
          '<h3>Začátečník</h3>'
          '<p>Kulatá nebo slzová raketa s měkčím jádrem a sklolaminátovým povrchem. Střední váha, vyvážení blíž k ruce. Cílem je velký sladký bod a pohodlí.</p>'
          '<h3>Rekreační hráč</h3>'
          '<p>Slza, případně hybrid s karbonovým povrchem. Pokud hrajete týdně a rádi smečujete, můžete zkusit raketu o málo těžší, ale vždy s ohledem na zápěstí.</p>'
          '<h3>Pokročilý a soutěžní</h3>'
          '<p>Diamant nebo agresivní slza, karbon a tvrdší jádro. Raketa odpouští málo a vyžaduje čistý zásah. Doporučujeme vyzkoušet zapůjčený model na klubovém kurtu.</p>'
          '<h2>Výběr pro děti a mládež</h2>'
          '<p>Dětské rakety jsou kratší a lehčí, ale i dospívající může hrát s lehčí dospělou raketou. Základem je, aby dítě zvládlo raketu bez únavy a udrželo ji pevně. Poutko je důležité i u malých. '
          'Pro mládež stačí začít s univerzální raketou, protože vyhraněný styl se teprve utváří.</p>'
          '<h2>Základy hry a pravidel</h2>'
          '<p>Padel se hraje ve čtyřech na kurtu o rozměrech menších než tenisový, rozděleném sítí. Podání probíhá zespodu: míč se před úderem nechá jednou odskočit od země, udeří se pod úrovní pasu a dopadne do diagonálního pole soupeře. Po dopadu se smí odrazit od zdi a hraje se dál, což prodlužuje výměny a dává prostor taktice. '
          'Počítá se jako v tenisu, hraje se na sady a gamy. Při výběru rakety zohledněte, že se hodně hraje z obrany od stěn, kde se hodí kontrola, a u sítě, kde je důležitá rychlost.</p>'
          '<h2>Kde hrát a jak otestovat raketu</h2>'
          '<p>Kurty najdete ve sportovních klubech a centrech, často s možností rezervace po hodinách. Mnoho z nich půjčuje rakety nebo nabízí testovací dny. Pokud můžete, vyzkoušejte dvě až tři rakety různého tvaru během jedné hodiny. Sledujte, zda se vám lépe hraje obrana od stěny, nebo smeč u sítě, a jak reaguje zápěstí po hodině hry. '
          'Pamatujte, že hodnocení na internetu je subjektivní a každá ruka je jiná.</p>'
          '<h2>Rozcvičení a prevence zranění</h2>'
          '<p>Rychlé změny směru a údery v předklonu zatěžují kotníky, kolena, rameno a loket. Před zápasem se pět až deset minut rozcvičte, zahřejte ramena a lehce se rozběhejte. Při bolesti lokte zkuste lehčí raketu s vyvážením blíž k rukojeti, případně se poraďte s trenérem o technice. '
          'Oporu kotníků poskytují bandáže z kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, i když zdravotní problémy patří k lékaři.</p>'
          '<h2>Péče o výbavu</h2>'
          '<p>Rakety nenechávejte v horkém autě, pěnové jádro se zahřátím opotřebuje a ztrácí odezvu. Po zápase utřete povrch a uložte raketu do obalu. Ochranná páska na okraji rámu zabrání škrábancům, protože i drobný šrám může postupně ohrozit rám. '
          'Míče po tréninku vraťte do tuby. Obuv vysušte a očistěte od písku, aby se podrážka nezanášela.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Raketa pro pokročilé hned na začátku. Diamantový tvar odpouští málo a zatěžuje zápěstí.</li>'
          '<li>Tenisová nebo běžecká obuv. Chybí záběr i boční opora, hrozí podvrtnutí.</li>'
          '<li>Zapomenuté poutko nebo jeho opotřebení. Letící raketa může zranit spoluhráče.</li>'
          '<li>Starý míč. Hra zpomalí a chybí odraz od stěn.</li>'
          '<li>Výběr jen podle reklamy značky. Důležitější je, jak raketa sedí.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V nabídce jsou {B(("bullpadel", "Bullpadel"), ("kuikma", "Kuikma"), ("head", "Head"), ("babolat", "Babolat"), ("wilson", "Wilson"), ("dunlop", "Dunlop"), ("adidas", "Adidas"), ("asics", "Asics"), ("mizuno", "Mizuno"), ("siux", "Siux"), ("joma", "Joma"))}. '
          'Pro obecný přehled míčových her sledujte kategorii <a href="/micove-sporty/">míčové a raketové sporty</a>, pro tenisové doplňky <a href="/tenisove-rakety/">tenisové rakety</a>.</p>',
    faq=[('Jakou raketu zvolit na začátek?', 'Kulatý nebo slzový tvar, střední až nižší váhu a vyvážení blíž k ruce. Měkčí jádro a sklolaminátový povrch odpouštějí chyby a šetří zápěstí.'),
         ('Čím se padel liší od tenisu?', 'Hraje se ve dvojicích na menším kurtu se stěnami, podává se zespodu a míč se může odrazit od skla. Raketa nemá struny, ale plný perforovaný povrch.'),
         ('Mohu hrát s tenisovým míčem?', 'Nedoporučuje se. Padelové míče mají nižší tlak a jinak upravený povrch, takže se na kurtu chovají předvídatelněji. Tenisový míč je rychlejší a letí jinak.'),
         ('Jak těžká by měla být padelová raketa?', 'Běžně kolem tří set šedesáti gramů, lehčí jsou pro začátečníky a ženy, těžší pro silné útočné hráče. Důležité je, jak raketa leží v ruce a zda nezatěžuje zápěstí.'),
         ('Je karbonová raketa lepší než sklolaminátová?', 'Není automaticky lepší. Karbon je tuhý a výkonný, ale odpouští méně chyb. Sklolaminát je měkčí a pro začátečníky pohodlnější.'),
         ('Jakou obuv na padel?', 'Obuv určenou pro padel s podrážkou, která drží na umělé trávě s pískem. Pevná pata a boční opora chrání kotník. Běžecké boty nejsou vhodné.'),
         ('Proč je poutko u rakety důležité?', 'Chrání před uvolněním rakety z ruky, takže neletí na spoluhráče. U padelu je poutko běžnou součástí pravidel, proto kontrolujte jeho stav před každým zápasem.'),
         ('Jak dlouho vydrží raketa?', 'Záleží na četnosti hry, zacházení a uložení. Pěnové jádro po čase ztrácí odezvu, rám se může poškrábat. Raketu nenechávejte na horku a chraňte okraj páskou.'),
         ('Lze padel hrát ve venkovním i krytém kurtu?', 'Ano, kurty jsou venkovní i kryté. Vítr a slunce ovlivňují míč, v hale je hra stabilnější. Povrch a obuv zůstávají stejné.'),
         ('Kolik míčů je potřeba na hru?', 'Obvykle jedna tuba o třech míčích, kterou si týmy půjčují. Pro soutěžní hru se používají nové míče, na trénink stačí starší.'),
         ('Jak často měnit omotávku?', 'Když přestane být lepivá a savá nebo se zlomí. Při častém hraní stačí výměna po několika týdnech, při občasném i po měsících. Omotávka je levná část výbavy.')])

# ------------------------------------------------------------------ kabaty-a-parky
NEW['kabaty-a-parky'] = dict(long=True,
    title='Kabáty a parky: zimní, outdoorové, dámské, pánské',
    desc='Parky a kabáty pro chladné dny: zateplení, vodoodpudivost, střih, kapuce a péče. Jak vybrat dámskou, pánskou nebo outdoorovou parku.',
    intro='<p>Parka je dlouhá zimní bunda s kapucí, která sahá aspoň do poloviny stehen a chrání před větrem, chladem i mokrem. Původně šlo o praktický oděv pro severské podnebí, dnes se nosí od města po turistiku. '
          'Kabát je v tomhle ohledu spíš městský: elegantnější střih, často z vlněné směsi nebo syntetiky, méně technických detailů a méně zateplení. Rozdíl je důležitý, protože obojí řeší jiné situace.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u modelů od značek jako Peak Mountain, Didriksons, Fjällräven, Helly Hansen, Regatta nebo The North Face. '
          'Pokud se rozhodujete mezi kategoriemi, mrkněte také na <a href="/zimni-bundy/">zimní a péřové bundy</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a> a <a href="/sportovni-bundy/">sportovní bundy</a>. '
          'Níže najdete rady k zateplení, délce, kapuci i péči.</p>',
    guide='<h2>Kabát, parka a bunda: v čem je rozdíl</h2>'
          '<p>Slova se v obchodech míchají, ale praktický význam se liší. Bunda sahá k pasu nebo k boku a poskytuje volnost pohybu, hodí se při aktivitě. Parka je delší, chrání stehna, mívá kapuci a často i zateplení. '
          'Kabát je nejdelší a nejformálnější, cílí na každodenní městské nošení a zateplení řeší spíš vrstvením pod ním.</p>'
          + T(['Typ', 'Délka', 'Zateplení', 'Nejlepší použití'], [
              ['Bunda', 'k bokům', 'lehčí až střední', 'aktivita, jaro a podzim'],
              ['Parka', 'do poloviny stehen', 'střední až silné', 'zima, město, turistika, čekání venku'],
              ['Kabát', 'ke kolenům nebo pod ně', 'lehčí, vrstvením', 'práce, společenské příležitosti'],
              ['Pláštěnka a nepromokavý plášť', 'po stehna až kolena', 'žádné', 'déšť']]) +
          '<h2>Zateplení: peří, syntetika a vlna</h2>'
          '<p>Základní otázkou je, čím je parka zateplená. Husí nebo kachní peří má vysokou izolační schopnost vzhledem k váze a dá se stlačit, ale po zmoknutí ztrácí účinek a schne pomalu. '
          'Syntetická výplň drží teplo i vlhká, rychleji schne a je levnější na péči, jenže je objemnější. Vlněné kabáty hřejí díky vzduchovým kapsám ve vlákně, příjemně se nosí a vlna se nepotí tolik jako syntetika, ale je těžší a pomalu schne.</p>'
          + T(['Výplň', 'Výhody', 'Nevýhody', 'Vhodné pro'], [
              ['Peří', 'lehké, velmi teplé, dobře stlačitelné', 'vlhko mu škodí, náročnější praní', 'suchý mráz, cestování'],
              ['Syntetika', 'drží teplo za vlhka, snadná péče', 'objemnější, těžší', 'vlhká zima, aktivní nošení'],
              ['Vlna', 'přirozená regulace teploty, elegantní vzhled', 'váha, pomalé schnutí', 'město, kancelář'],
              ['Fleecová podšívka', 'měkká, prodyšná', 'sama o sobě málo větruodolná', 'přechodné období, vrstvení']]) +
          '<p>Teplotní údaje uváděné výrobci jsou jen orientační. Záleží na vašem metabolismu, aktivitě a větru. Zkušení lidé si vybírají zateplení podle toho, jak vypadá jejich typický den: čekání na zastávce, nebo pochod lesem? '
          'Při chůzi se zahřejete a silná parka je spíš na obtíž, při stání naopak chrání.</p>'
          '<h2>Vodoodolnost a větruodolnost</h2>'
          '<p>Většina parek má na povrchu vodoodpudivou úpravu, která nechá kapky stékat. Nejde o plně nepromokavou ochranu, a to platí i pro modely označené jako voděodolné. Lepené švy a membrána zvyšují odolnost proti dešti, ale snižují prodyšnost. '
          'Pokud chodíte v dešti dlouho, volte parku s membránou nebo si kupte samostatnou <a href="/plastenky/">pláštěnku</a>. Pro většinu městských dnů stačí vodoodpudivá úprava. '
          'Upozorňujeme, že impregnace časem slábne a obnovuje se praním a ošetřením přípravkem k tomu určeným.</p>'
          '<p>Větruodolnost zajistí hustě tkaná tkanina, větrná lišta za zipem a manžety s elastickým zakončením. Dobré parky mívají dvojitý zip (zip a druk), takže se vítr nedostane skrz.</p>'
          '<h2>Kapuce, límec a manžety</h2>'
          '<p>Kapuce je hlavní důvod, proč se parka kupuje. Měla by jít stáhnout šňůrkou, aby nepřekážela ve výhledu, a mít zesílený lem, který drží tvar. Odnímatelná kapuce se hodí do města, kde se kapuce tolik nenosí. '
          'Kožešinový lem, ať skutečný, nebo umělý, tvoří ochranu před větrem kolem obličeje. Vysoký límec chrání krk, ale pod bradou nesmí škrtit. Manžety s elastickým prvkem nebo suchým zipem utahují rukáv, aby dovnitř nefoukalo.</p>'
          '<h2>Délka a střih</h2>'
          '<p>Délka parky ovlivňuje teplo i pohyb. Parka jen těsně pod boky umožňuje volné sedání na kolo nebo do auta, delší chrání stehna, ale při chůzi do schodů a při řízení omezuje. Pánské střihy bývají rovné, dámské zúžené v pase a rozšířené v bocích. '
          'Pamatujte, že pod parku patří mikina, fleece nebo svetr, proto vybírejte o něco volnější velikost. Ověřte, že se můžete natáhnout, aniž by rukávy vyjely výš než k zápěstí.</p>'
          '<h3>Podle vašeho použití</h3>'
          '<ul><li><strong>Město a dojíždění:</strong> parka s kapucí, vodoodpudivá, s kapsami na hrudi i u boků. Důležité je pohodlí při sezení.</li>'
          '<li><strong>Turistika a zimní procházky:</strong> prodyšnější, s větracími zipy a prostornými kapsami na rukavice a mapu. Pokud se hodně potíte, vybírejte lehčí zateplení.</li>'
          '<li><strong>Chladné dny při stání:</strong> silné zateplení, dlouhý střih, vysoký límec. Hodí se pro čekání u hřiště, rybaření nebo pro zimní práci venku.</li>'
          '<li><strong>Děti:</strong> pevný zip, reflexní prvky, odnímatelná kapuce bez šňůrky na krku, aby se nezachytila.</li></ul>'
          '<h2>Vrstvení pod parku</h2>'
          '<p>Parka funguje nejlépe jako vnější vrstva. Pod ní se nosí <a href="/termopradlo/">funkční prádlo</a> nebo <a href="/merino/">merino</a>, přes ně mikina z kategorie <a href="/fleecove-mikiny/">fleecové mikiny</a> a případně lehčí <a href="/sportovni-vesty/">vesta</a> místo druhé bundy. '
          'Bavlněné tričko u těla drží vlhkost a při zastavení studí. Nezapomeňte na <a href="/nakrcniky-a-satky/">nákrčník</a> a <a href="/cepice-a-celenky/">čepici</a>, protože ztráty tepla se projeví na uších a krku dřív než v trupu. Do mrazu patří i <a href="/sportovni-rukavice/">rukavice</a>.</p>'
          '<h2>Materiály a ekologie</h2>'
          '<p>Vnější tkanina bývá z polyesteru nebo polyamidu, případně z bavlněné směsi. Polyester je lehký, rychle schne a dobře drží impregnaci. Bavlněné směsi mají tradiční vzhled a příjemný omak, ale po zmoknutí jsou těžké. '
          'Výrobci stále častěji používají recyklované vlákno nebo bezfluorové impregnace, takže si u modelu ověřte údaje v popisu. Pokud hledáte oděv, který dlouho vydrží, sledujte pevnost zipů, švů a poutek na kapuci.</p>'
          '<h2>Kapsy, zipy a detaily, které se hodí</h2>'
          '<p>Praktické parky mají vnitřní kapsu na telefon nebo doklady, boční kapsy s klopou nebo zipem a prostornou náprsní kapsu. Zip by měl být kvalitní a dvoucestný, aby se dal rozepnout zespodu při sezení nebo jízdě. '
          'Šňůrka v pase a na spodním lemu umožňuje upravit siluetu a zabránit průvanu. Reflexní prvky, rukávové kapsy a poutka na zavěšení uvítají lidé, kteří chodí za tmy nebo se pohybují v hlubokém sněhu. Zkontrolujte i pevnost knoflíků a patentek.</p>'
          '<h2>Jak zkoušet parku</h2>'
          '<p>Při zkoušce si oblečte vrstvy, které budete nosit, rozepněte a zapněte zip, nasaďte kapuci a zvedněte obě ruce nad hlavu. Rukávy nesmí vyjet nad zápěstí a záda nesmí vystoupat nad pas. Posaďte se, předkloňte a zkuste, jestli střih netlačí na bedra. '
          'Při online nákupu porovnejte míry z tabulky výrobce a pamatujte, že kabát se zpravidla měří přes hrudník a podle délky zad.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Na Sportece najdete {B(("peak-mountain", "Peak Mountain"), ("didriksons", "Didriksons"), ("fjallraven", "Fjällräven"), ("helly-hansen", "Helly Hansen"), ("regatta", "Regatta"), ("loap", "Loap"), ("the-north-face", "The North Face"), ("quechua", "Quechua"), ("columbia", "Columbia"), ("alpine-pro", "Alpine Pro"), ("patagonia", "Patagonia"), ("hannah", "Hannah"))}. '
          'Švédské a norské značky se tradičně zaměřují na pevné tkaniny pro chladný vlhký klimat, klasické outdoorové značky na technické materiály, módní značky na střih. Velikostní tabulky se liší, proto vždy zkontrolujte rozměry konkrétního modelu.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Praní se řídí štítkem. Peřové modely se perou speciálním prostředkem a suší s dostatkem času, aby peří nesplihlo. Syntetické parky snesou běžné praní při nižší teplotě bez aviváže, která zalepuje vlákna a poškozuje impregnaci. '
          'Po vyprání se obnovuje impregnace sprejem nebo přísadou do pračky podle návodu. Vlněné kabáty se čistí šetrně, často stačí vysušit, vykartáčovat a vyvětrat. Na léto parku uložte volně v prodyšném obalu, ne stlačenou. Zip občas promažte specializovaným voskem.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš silné zateplení pro chůzi. Zpotíte se a pak vychladnete.</li>'
          '<li>Příliš těsný střih. Nelze nosit vrstvy a zateplení ztrácí účinek.</li>'
          '<li>Spoléhání na vodoodpudivost při dlouhém dešti. Je třeba membrána nebo pláštěnka.</li>'
          '<li>Praní s aviváží. Vlákna se zalepí a impregnace přestane fungovat.</li>'
          '<li>Podceňování kapuce. Špatně padnoucí kapuce nezastaví vítr a překáží ve výhledu.</li></ul>'
          '<h2>Pro koho je parka vhodná</h2>'
          '<p>Parka je rozumná volba pro každého, kdo tráví v zimě hodně času venku bez pohybu: rodiče na hřišti, majitele psů, dojíždějící, fotografy nebo rybáře. Kdo se naopak v zimě hodně hýbe, spokojí se s kratší bundou, ve které se nepřehřeje. '
          'Pro velmi vysoké nebo naopak drobné postavy zkontrolujte délku rukávů i zad, protože některé značky nabízejí zkrácené a prodloužené střihy.</p>'
          '<p>Rozhodněte se také podle toho, jak často parku použijete. Jedna univerzální černá nebo tmavě zelená sedí k většině věcí a opravdu se v ní vyjde. Výrazné barvy se hodí do hor a do tmy, kde pomáhají být vidět.</p>'
          '<h2>Další kategorie, které se hodí</h2>'
          '<p>Při výběru oblečení na zimu se podívejte i do kategorií <a href="/softshellove-bundy/">softshellové bundy</a>, <a href="/vetrovky/">větrovky</a>, <a href="/sportovni-obleceni/">sportovní oblečení</a> a <a href="/zimni-obuv/">zimní boty</a>. Pro delší výlety přidejte <a href="/turisticke-batohy/">turistický batoh</a>.</p>',
    faq=[('Jaký je rozdíl mezi parkou a zimní bundou?', 'Parka je delší, sahá do poloviny stehen nebo níž a obvykle má kapuci. Zimní bunda končí u pasu nebo boků a dává víc volnosti pohybu. Parka lépe chrání při stání venku.'),
         ('Je lepší peří, nebo syntetika?', 'Peří je lehčí a teplejší vzhledem k váze, ale za vlhka ztrácí izolaci. Syntetika drží teplo i vlhká a lépe snáší běžnou péči. Pro vlhké zimy je praktičtější syntetika.'),
         ('Je každá parka nepromokavá?', 'Ne. Většina má jen vodoodpudivou úpravu, která zvládne drobný déšť a mokrý sníh. Při dlouhém dešti nebo silném lijáku je potřeba membrána s lepenými švy nebo pláštěnka.'),
         ('Jakou velikost zvolit?', 'O něco volnější než u běžné bundy, aby se pod ní vešla mikina nebo fleece. Rukávy musí zůstat dost dlouhé i při zvednutých rukou a ramena nesmí tlačit.'),
         ('Jak se perou peřové parky?', 'Podle štítku, šetrným prostředkem určeným na peří a při nižší teplotě. Důležité je důkladné vysušení se sušicími míčky nebo opakovaným protřepáním, aby peří nesplihlo.'),
         ('Jak obnovit impregnaci?', 'Po vyprání naneste sprej nebo přidejte přípravek do pračky podle návodu. Většinou stačí jednou za sezónu, častěji u intenzivně nošených kusů. Fluorové a bezfluorové produkty se liší, řiďte se pokyny.'),
         ('Hodí se parka na turistiku?', 'Na zimní procházky ano, pokud je prodyšná a nemáte tendenci se potit. Při náročných výstupech je lepší vrstvit tenčí oděvy a parku si vzít do batohu na přestávky.'),
         ('Je kožešinový lem nutný?', 'Není, ale lem kolem obličeje zmírňuje vítr a chrání pleť. Umělá nebo odnímatelná kožešina je praktická a snadno se pere. Zkontrolujte, zda lem nepřekáží ve výhledu.'),
         ('Co s parkou přes léto?', 'Vyprat, dobře vysušit a uložit volně v prodyšném obalu, ne stlačenou v pytli. Zimní vybavení nikdy neskladujte vlhké, vznikla by plíseň.'),
         ('Jak dlouho parka vydrží?', 'Při správné péči i několik zim. Klíčová je kvalita zipu, švů a tkaniny. První, co se obvykle poškodí, je zip a impregnace, obojí se dá obnovit nebo opravit.'),
         ('Mohu parku nosit i do města?', 'Ano, většina parek je určena právě pro každodenní nošení. Vybírejte střih a barvu, které se hodí k běžnému oblečení, a ověřte, že kapsy vyhovují telefonu i klíčům.')])

# ------------------------------------------------------------------ plastenky
NEW['plastenky'] = dict(long=True,
    title='Pláštěnky a pončo: do deště, na kolo, na túru',
    desc='Pláštěnky, pončo a nepromokavé pláště pro turistiku, kolo i festival. Jak vybrat materiál, velikost, kapuci, švy a péči. Srovnání obchodů.',
    intro='<p>Pláštěnka je nejlevnější a nejlehčí ochrana před deštěm, a přitom se často vybírá nesprávně. Po prvním dešti si lidé všimnou, že rukávy nesahají k zápěstí, kapuce padá do očí nebo se pod plastem uvaří. '
          'Kategorie <strong>pláštěnky a pončo</strong> zahrnuje klasické jednorázové kusy, skládací pláštěnky do kapsy, delší pláštěnky s rukávy, pončo přes batoh i sady kalhot a bundy proti dešti.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u modelů od značek jako Helly Hansen, Viking, Regatta, Trespass, Tatonka nebo Vaude. '
          'Pokud dáváte přednost bundě, podívejte se do kategorie <a href="/nepromokave-bundy/">nepromokavé a outdoorové bundy</a>, pro nohy na <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> nebo <a href="/holinky/">holínky</a>. '
          'Další text vysvětlí rozdíl mezi pláštěnkou a pončem, jak zvolit velikost podle batohu a jak pláštěnku udržovat, aby vám vydržela dlouho.</p>',
    guide='<h2>Pláštěnka, pončo, bunda: co zvolit</h2>'
          '<p>Základní rozhodnutí se týká tvaru. Pláštěnka s rukávy a zipem se podobá bundě, pončo je kus látky s otvorem pro hlavu, který zakryje i batoh. Nepromokavá bunda je technická varianta s membránou, která umožňuje prodyšnost. Každé řešení má své místo.</p>'
          + T(['Typ', 'Krytí', 'Hmotnost a objem', 'Nejlepší použití'], [
              ['Pláštěnka s rukávy', 'tělo, ruce, často i batoh', 'lehká, skládací', 'město, kolo, výlet'],
              ['Pončo', 'tělo a batoh, volné boky', 'velmi lehké, různé velikosti', 'turistika s batohem, festival'],
              ['Jednorázová pláštěnka', 'základní krytí', 'minimální', 'nouzové použití, záloha v autě'],
              ['Nepromokavá bunda s membránou', 'tělo, ruce, kapuce', 'střední', 'dlouhé túry, horské podmínky'],
              ['Pláštěnkové kalhoty a návleky', 'nohy', 'lehké', 'cyklisté, rybáři']]) +
          '<h2>Pončo: výhody a omezení</h2>'
          '<p>Pončo je pověstný turistický oděv, protože pokryje batoh a ruce zároveň a nechá se rychle navléknout bez zouvání. Dobře vzdušně větrá, takže se pod ním zpotíte méně než v uzavřené bundě. Je univerzální, protože s větší plochou může sloužit i jako přístřešek nebo plachta. '
          'Naopak vítr ho zvedá a ruce nejsou pevně zakryty. Na kole se nehodí, protože pončo se zachytí v řídítkách a ve větru se zvedá. Při chůzi s holemi jsou praktičtější klasické pláštěnky s rukávy.</p>'
          '<h2>Materiály a vodní sloupec</h2>'
          '<p>Základní pláštěnky bývají z PVC nebo polyetylenu, který voda nepropustí vůbec, ale ani vlhkost z těla. Pod takovým oděvem se při pohybu zpotíte. Lepší modely mají polyesterovou nebo nylonovou tkaninu s polyuretanovou úpravou, případně s membránou. '
          'Vodní sloupec udává odolnost tkaniny proti tlaku vody v milimetrech. Vyšší číslo znamená lepší odolnost při silném dešti, ale není to jediná vlastnost. Důležité jsou lepené švy, kryté zipy a kvalitní kapuce.</p>'
          + T(['Materiál', 'Prodyšnost', 'Pevnost', 'Poznámka'], [
              ['PVC, polyetylen', 'žádná', 'nízká až střední', 'levné, na pár použití'],
              ['Polyester s PU povrchem', 'omezená', 'střední', 'běžné pláštěnky a pončo'],
              ['Nylon s povlakem', 'omezená', 'vysoká', 'lehké, skládací modely'],
              ['Laminát s membránou', 'dobrá', 'vysoká', 'technické oděvy, vyšší nároky na péči']]) +
          '<h2>Švy, zipy a kapuce</h2>'
          '<p>Švy jsou nejslabší místo. Prosté šité švy propouštějí vodu otvory po jehle, lepené nebo svařované švy ji zastaví. U levných pláštěnek často chybí, proto se při déle trvajícím dešti propustí. '
          'Zip má být krytý přesahující légou. Kapuce se stahuje šňůrkou a ideálně má kšilt, který odvádí vodu od očí. Nastavitelné manžety a spodní lem pomáhají udržet tvar ve větru.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Pláštěnka se kupuje větší než běžné oblečení, protože pod ní nosíte vrstvy a často i batoh. Pokud nosíte velký batoh, vyberte pončo nebo pláštěnku s rozšířenými zády. Délka by měla zakrýt zadek a stehna, jinak voda stéká do kalhot. '
          'Pro děti jsou vhodné modely s výraznou barvou a reflexními prvky, aby byly vidět v šeru. Při výběru zkontrolujte, zda se kapuce dá obléci přes helmu, pokud jezdíte na kole nebo lezete.</p>'
          '<h3>Podle činnosti</h3>'
          '<ul><li><strong>Turistika:</strong> lehké pončo nebo skládací pláštěnka přes batoh, vzdušné větrání pod rukávy. Do hor raději technickou <a href="/nepromokave-bundy/">nepromokavou bundu</a>.</li>'
          '<li><strong>Kolo:</strong> pláštěnka s předlouženými zády a krátkými rukávy na zápěstí, aby nepřekážely řídítka. Doplňte <a href="/cyklisticke-bundy-a-vesty/">cyklistickou bundu</a> a <a href="/cyklo-blatniky/">blatníky</a>.</li>'
          '<li><strong>Festival a kemp:</strong> jednoduché pončo nebo jednorázová pláštěnka v batůžku. Pro kemp najdete víc v kategorii <a href="/kemping/">kemping</a>.</li>'
          '<li><strong>Rybaření a lov:</strong> pevný materiál, tichá tkanina, dlouhé kalhoty. Odkazy: <a href="/rybarske-obleceni/">rybářské oblečení</a>, <a href="/lovecke-obleceni/">lovecké oblečení</a>.</li>'
          '<li><strong>Děti a škola:</strong> jasná barva, bezpečné zapínání, snadné oblékání s rukavicemi.</li></ul>'
          '<h2>Pláštěnka na batoh</h2>'
          '<p>Batoh můžete chránit zvlášť pláštěnkou na batoh, která se natáhne přes obsah a zajistí se gumou. Přesto potřebujete i osobní ochranu, protože zády přiléhající část batohu zůstane mokrá od potu a zespodu. Důležité věci uložte do nepromokavých vaků, protože ani pláštěnka na batoh nezabrání vniknutí vody zespodu. '
          'Batohy najdete v kategorii <a href="/batohy/">batohy</a>, vaky a tašky v <a href="/sportovni-tasky/">sportovních taškách</a>.</p>'
          '<h2>Vrstvení při dešti</h2>'
          '<p>Pláštěnka je jen horní vrstva. Pod ní se nosí funkční tričko z kategorie <a href="/funkcni-tricka/">funkční trička</a>, případně <a href="/merino-tricka/">merino</a>. Bavlna při pohybu pije pot a zůstane studená. Při chladném dešti přidejte <a href="/fleecove-mikiny/">fleecovou mikinu</a>. '
          'Na nohy patří nepromokavá obuv, případně <a href="/nesmeky/">návleky</a>, a při výletu s dětmi i záložní ponožky v sáčku.</p>'
          '<h2>Pláštěnky pro konkrétní situace</h2>'
          '<h3>Jednodenní výlet a přeháňky</h3>'
          '<p>Stačí lehká skládací pláštěnka do kapsy batohu, která váží minimum a po použití se sbalí do malého pouzdra. Ušetří vás před mokrým oblečením při náhlém dešti a nezabírá místo.</p>'
          '<h3>Vícedenní túra</h3>'
          '<p>Při vícedenním pochodu volte odolnější materiál, ideálně pončo s očky nebo technickou bundu s kalhotami. Mokré oblečení pomalu schne a zhoršuje spánek, proto počítejte s rezervou. K vybavení se hodí <a href="/stany/">stan</a> a <a href="/spaci-pytle/">spací pytel</a>, které je dobré v nepromokavém vaku chránit samostatně.</p>'
          '<h3>Vodní sporty a plachtění</h3>'
          '<p>U vody se používají pevnější oděvy z vodotěsné tkaniny, protože sprška a vlny mají větší sílu než déšť. Nabídku najdete i v kategorii <a href="/vodni-sporty/">vodní sporty a plavání</a>. Při plavbě lodí nebo paddleboardu myslete na <a href="/plovaci-vesty/">plovací vestu</a>, která patří přes pláštěnku, aby fungovala a byla dobře vidět.</p>'
          '<h3>Město a dojíždění</h3>'
          '<p>V městském provozu se hodí pláštěnka, kterou lze sbalit do tašky a přes kancelářské oblečení rychle navléknout. Pozor na větrné nárazy mezi budovami, kde se široké pončo nafukuje. Menší, dobře padnoucí kus je praktičtější než objemný.</p>'
          '<h2>Pláštěnka versus deštník</h2>'
          '<p>Deštník chrání hlavu a ramena a je ideální při chůzi po městě, ale nechrání před šikmým deštěm a nelze ho použít při jízdě na kole nebo při práci s hůlkami. Pláštěnka kryje celé tělo a nechá volné ruce. Často se kombinují: pláštěnka na cestu, deštník na krátkou chvíli před vchodem. '
          'Při rozhodování myslete na aktivitu, rychlost větru a to, jak dlouho budete venku.</p>'
          '<h2>Pro koho je pláštěnka vhodná</h2>'
          '<p>Pláštěnku ocení každý, kdo se nechce spoléhat na předpověď: turisté, cyklisté, rodiče na hřišti, návštěvníci festivalů i lidé, kteří dojíždějí pěšky. Jeden kvalitní kus na dlouhé roky je lepší než série jednorázových, které skončí v odpadu. '
          'Při výběru zvažte, kolik místa máte v batohu, jak často s ní počítáte a zda ji budete nosit jako hlavní oděv, nebo jen záložní pro případ nouze.</p>'
          '<p>Přemýšlejte i o barvě. Výrazná žlutá, oranžová nebo zelená zvyšuje viditelnost v šeru a v mlze, tmavé kusy se hodí do města. U dětí a při jízdě na kole je viditelnost důležitější než vzhled.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>V nabídce jsou {B(("helly-hansen", "Helly Hansen"), ("viking", "Viking"), ("regatta", "Regatta"), ("trespass", "Trespass"), ("tatonka", "Tatonka"), ("vaude", "Vaude"), ("ferrino", "Ferrino"), ("helikon-tex", "Helikon-Tex®"), ("mil-tec", "Mil-tec®"), ("fjallraven", "Fjällräven"), ("didriksons", "Didriksons"), ("loap", "Loap"), ("columbia", "Columbia"))}. '
          'Vojenské a taktické značky nabízejí robustní pončo s očky pro stavbu přístřešku, outdoorové lehčí kusy do batohu a norské a švédské značky pevné pláštěnky pro severské počasí.</p>'
          '<h2>Péče a opravy</h2>'
          '<p>Po použití pláštěnku vyvěste a nechte uschnout, aby neplesnivěla. Prach a bláto setřete vlhkým hadříkem, perte jen pokud to štítek výslovně dovoluje. Povrchy z PVC se neperou ve vysoké teplotě a nesmí se žehlit. '
          'Uložte volně nebo ve vlastním obalu, lépe ne sbalenou natěsno na několik měsíců, protože v záhybech může materiál praskat. Drobné díry lze zalepit samolepicí záplatou, na švech se hodí těsnicí páska.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš malá velikost. Rukávy sahají k lokti a záda se namočí.</li>'
          '<li>Pláštěnka bez větrání. Pod plastem se zpotíte a oblečení je mokré zevnitř.</li>'
          '<li>Pončo na kolo. Zachytí se v řídítkách a ve větru se zvedá.</li>'
          '<li>Skladování mokré. Plíseň a zápach.</li>'
          '<li>Očekávání horské ochrany od jednorázové pláštěnky. Je to jen nouzová pomůcka.</li></ul>'
          '<h2>Co mít s sebou</h2>'
          '<p>Na túru s předpovědí deště nestačí jen pláštěnka. Vezměte i čelovku z kategorie <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, lékárničku z <a href="/prvni-pomoc/">první pomoci</a> a láhev z kategorie <a href="/lahve-a-termosky/">láhve a termosky</a>. '
          'Širší přehled najdete v kategorii <a href="/outdoor/">outdoor a turistika</a>.</p>',
    faq=[('Jaký je rozdíl mezi pláštěnkou a pončem?', 'Pláštěnka má rukávy a zapínání jako bunda. Pončo je kus látky s otvorem pro hlavu, který zakryje i batoh, ale nechává boky volné. Pončo více větrá, pláštěnka lépe drží ve větru.'),
         ('Zvládne pláštěnka celodenní déšť?', 'Záleží na materiálu a švech. Kvalitní model s lepenými švy a dobrou kapucí ano. Jednorázová pláštěnka je jen nouzové řešení a při delším dešti se prodere nebo propustí vlhkost.'),
         ('Co znamená vodní sloupec?', 'Číslo v milimetrech vyjadřuje, jaký tlak vody tkanina vydrží, než ji propustí. Vyšší hodnota znamená lepší odolnost, ale prodyšnost a švy rozhodují stejně.'),
         ('Jak velkou pláštěnku zvolit?', 'O číslo větší než běžné oblečení, abyste se vešli s vrstvami a batohem. Délka má zakrýt zadek a stehna a rukávy mají sahat na zápěstí i při zvednutých rukou.'),
         ('Hodí se pončo na kolo?', 'Nehodí. Zachytává se v řídítkách, ve větru se zvedá a omezuje výhled. Na kolo je lepší pláštěnka s prodlouženými zády nebo cyklistická bunda.'),
         ('Jak se zbavit potu pod pláštěnkou?', 'Zvolte model s větracími otvory pod pažemi a prodyšným materiálem, případně pončo. Pod plastem noste funkční vrstvu, ne bavlnu. Při zastavení si pláštěnku rozepněte.'),
         ('Mohu pláštěnku prát v pračce?', 'Jen když to výslovně povoluje štítek. Většina se omývá vlhkým hadříkem, PVC se nesmí prát v horké vodě ani žehlit. Po očištění ji nechte volně uschnout.'),
         ('Jak zalepit díru?', 'Samolepicí záplatou určenou pro nepromokavé tkaniny nebo páskou na švy. Povrch odmastěte a očistěte, záplatu přiložte a přitlačte. Opravy fungují dobře u drobných poškození.'),
         ('Chrání pončo i batoh?', 'Většina pončo je dost velká, aby zakryla batoh na zádech. Zkontrolujte rozměry, zejména u objemných batohů. Hřbet batohu může zůstat vlhký, proto cennosti ukládejte do nepromokavých vaků.'),
         ('Co s pláštěnkou přes zimu?', 'Vysušit, uložit volně v suchu a mimo mráz. Při skladování natěsno nebo v mrazu se může materiál lámat v záhybech. Před sezónou zkontrolujte švy a kapuci.'),
         ('Hodí se pláštěnka pro děti?', 'Ano, pokud je dětská velikost, jasná barva a bezpečné zapínání bez šňůr na krku. Kapuce se má dát stáhnout a nesmí padat do očí. Dítě si pláštěnku vyzkouší doma s oblečením a batohem.')])
