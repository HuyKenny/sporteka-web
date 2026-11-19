"""Guides wave 5a (2026-11-19): cviky-na-bricho, tabata, burpees, drepy.

Demand (CZ / month): cviky na břicho 3 800, tabata 1 400, burpees 600, dřepy 350.

Sources used for the facts:
- Spot reduction: Vispute et al. 2011, J Strength Cond Res (PMID 21804427): 24 volunteers, 7 abdominal exercises,
  2 x 10 reps, 5 days a week for 6 weeks, no significant effect on body weight, body fat, abdominal fat or waist
  circumference compared with the control group; abdominal muscular endurance improved. NSCA "Trainer tips: spot
  reduction" summary; Wikipedia "Spot reduction".
- Core anatomy (rectus abdominis, external and internal obliques, transversus abdominis, erector spinae, multifidus,
  diaphragm and pelvic floor as parts of the "core"): standard anatomy textbooks / Wikipedia "Core (anatomy)".
- WHO 2020 guidelines on physical activity: adults should do muscle-strengthening activities on 2 or more days a week.
- Tabata: Tabata I. et al. 1996, Med Sci Sports Exerc 28(10):1327-1330 (PubMed 8897392): 6 weeks, intermittent group
  7-8 bouts of 20 s at about 170 % of VO2max with 10 s rest on a cycle ergometer; endurance group 60 min at 70 % VO2max
  5 days a week; VO2max of the intermittent group rose by about 7 ml/kg/min and anaerobic capacity by 28 %, the
  endurance group's anaerobic capacity did not increase significantly.
- Burpees: Wikipedia "Burpee (exercise)", Task & Purpose and Morning Chalk Up "History of the burpee": named after
  physiologist Royal H. Burpee (Teachers College, Columbia University, thesis 1939/1940), original four-count
  movement used as a quick fitness test, US Army used it ("squat thrust") in WWII-era fitness testing; push-up and
  jump were added later.
- Squats: Fry, Smith & Schilling 2003, J Strength Cond Res (PubMed 14636100): restricting forward knee travel lowered
  knee torque but greatly increased hip torque and trunk lean; a later replication did not find the same magnitude,
  so the text only says the load shifts to the hips and lower back.
Left out because not verified: exact VO2max percentage gains often quoted for Tabata (14 % / 10 %), the year Burpee
finished his PhD (sources differ, 1939 vs 1940 - text says "in the late 1930s"), the year the jump/push-up were
added, any calorie numbers for burpees, Tabata or ab exercises, any fixed "safe" squat depth for people with knee
problems, the claim that Tabata was developed for the Japanese speed-skating team.
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- cviky-na-bricho
CORE = T(['Sval', 'Kde leží', 'Co dělá', 'Typické cviky'], [
    ['Přímý sval břišní', 'Vpředu od hrudní kosti ke stydké kosti, „pekáč buchet“', 'Ohýbá trup dopředu, přibližuje hrudník k pánvi', 'Crunch, zvedání nohou, hollow hold'],
    ['Zevní a vnitřní šikmý sval', 'Po stranách břicha', 'Rotace a úklon trupu, brzdí nežádoucí rotaci', 'Ruská rotace, boční plank, dřevorubec'],
    ['Příčný sval břišní', 'Nejhlouběji, obepíná břicho jako pás', 'Zpevňuje břišní stěnu a stabilizuje páteř', 'Plank, dead bug, vtažení břicha'],
    ['Vzpřimovače páteře a multifidy', 'Podél páteře na zádech', 'Narovnávají trup a drží páteř', 'Superman, bird dog, hyperextenze'],
    ['Bránice a pánevní dno', 'Strop a dno břišní dutiny', 'Spolu s břišními svaly drží tlak v trupu', 'Dýchání do břicha, většina stabilizačních cviků'],
])

ABS_PLAN = T(['Úroveň', 'Cviky', 'Série × opakování', 'Kolikrát týdně'], [
    ['Začátečník (týden 1–4)', 'Dead bug, plank na předloktí, boční plank na kolenou, bird dog, crunch', '2 × 8–10 nebo 2 × 20–30 s', '2–3×'],
    ['Mírně pokročilý (týden 5–8)', 'Plank s dotykem ramen, boční plank, zvedání nohou vleže, ruská rotace, hollow hold', '3 × 10–12 nebo 3 × 30–45 s', '3×'],
    ['Pokročilý', 'Zvedání kolen ve visu, posilovací kolečko, dřevorubec s gumou, L-sed, plank s vahou', '3–4 × 8–12 nebo 3 × 45–60 s', '3–4×'],
])

GUIDES['cviky-na-bricho'] = dict(
    name='Cviky na břicho',
    h1='Cviky na břicho: nejlepší cviky doma i v posilovně',
    seo_title='Cviky na břicho: 12 nejlepších cviků doma i v posilovně',
    seo_desc='Cviky na břicho s popisem techniky: plank, dead bug, zvedání nohou, kolečko i rotace. Plán pro začátečníky i pokročilé, chyby a proč břicho nehubne cvičením.',
    intro_html=(
        '<p><strong>Jaké cviky na břicho jsou nejlepší?</strong> Ty, které zapojí celý střed těla, ne jen přímý sval břišní. '
        'Základ tvoří plank a boční plank, dead bug, bird dog, zvedání nohou vleže a ve visu, ruská rotace a jízda s posilovacím kolečkem. '
        'Doma vám stačí podložka, v posilovně přidáte kladku, hrazdu nebo kotouč. Cvičte dvakrát až čtyřikrát týdně, techniku stavte před počet opakování a přidávejte postupně.</p>'
        '<p>V článku najdete stručnou anatomii břišních svalů, dvanáct cviků s popisem provedení, plán pro začátečníky i pokročilé a nejčastější chyby. '
        'Vysvětlíme i to, proč samotné cviky na břicho tuk z břicha nespálí. Sporteka nic neprodává, jen porovnává nabídky českých e-shopů, proto pod některými částmi uvidíte podložky a pomůcky na cvičení.</p>'
        '<p>Máte bolesti zad, kýlu, rozestup břišních svalů, jste těhotná nebo po porodu? Pak se před začátkem poraďte s lékařem nebo fyzioterapeutem, které cviky jsou pro vás vhodné.</p>'
    ),
    sections=[
        dict(h2='Co je „core“ a proč nestačí dělat sklapovačky',
             html=(
                 '<p>Slovem <strong>core</strong> (střed těla) se označuje skupina svalů, které obklopují bederní páteř a pánev. Nepatří sem jen viditelný „pekáč buchet“, ale i hluboké svaly a svaly zad.</p>'
                 + CORE +
                 '<p>Přímý sval břišní hlavně ohýbá trup. Většinu času ale břišní svaly v běžném životě i sportu pohyb spíš <strong>brzdí</strong>: drží trup, když nesete nákup v jedné ruce, když dopadáte z výskoku nebo když zvedáte činku nad hlavu. '
                 'Proto dobrý trénink břicha obsahuje tři typy cviků:</p>'
                 '<ul><li><strong>anti-extenze</strong> – trup se nesmí prohnout (plank, dead bug, posilovací kolečko),</li>'
                 '<li><strong>anti-rotace a anti-úklon</strong> – trup se nesmí stočit ani naklonit (boční plank, Pallofův tlak, nošení činky v jedné ruce),</li>'
                 '<li><strong>flexe a rotace</strong> – trup se aktivně ohýbá nebo otáčí (crunch, zvedání nohou, ruská rotace, dřevorubec).</li></ul>'
                 '<p>Kdo dělá jen sedy-lehy, posiluje hlavně jeden sval a jeden směr pohybu. Kombinace všech tří skupin dá pevnější a odolnější střed těla.</p>'
             )),
        dict(h2='Proč cvičením břicha nezhubnete na břiše',
             html=(
                 '<p>Představa, že posilováním určité partie spálíte tuk právě v ní, se nazývá <strong>lokální hubnutí</strong> (anglicky spot reduction). Výzkumy ji nepotvrzují. '
                 'Ve studii Vispute a kol. z roku 2011 cvičili dobrovolníci šest týdnů pětkrát týdně sedm cviků na břicho. Oproti kontrolní skupině se jim nezměnila hmotnost, procento tuku, množství břišního tuku ani obvod pasu. Zlepšila se jen vytrvalost břišních svalů.</p>'
                 '<p>Tuk se z těla ubírá jako celek a to, odkud mizí dřív, z velké části určují genetika, pohlaví a věk. Na viditelné břišní svaly má proto větší vliv celkový energetický příjem, pohyb během dne a kvalitní spánek než počet sklapovaček. '
                 'Více o jídle pro sportovce najdete v článku <a href="/vyziva-pro-zacatecniky/">výživa pro začátečníky</a>, o spalování energie v článku <a href="/kardio-doma/">kardio doma</a>.</p>'
                 '<p>Cviky na břicho mají přesto smysl: zlepšují držení těla, přenos síly mezi horní a dolní polovinou těla a pomáhají při běhu, zvedání i v míčových sportech.</p>'
             )),
        dict(h2='Cviky na břicho doma: 8 cviků jen s podložkou',
             html=(
                 '<p>Na všechny následující cviky stačí protiskluzová podložka. Tvrdá podlaha tlačí do páteře a kostrče, a když se pod vámi podložka posouvá, ztrácíte kontrolu nad pohybem.</p>'
                 '<ol>'
                 '<li><strong>Plank na předloktí.</strong> Lokty pod rameny, tělo v jedné linii od hlavy po paty, hýždě a břicho zpevněné. Pánev nepropadá ani netrčí nahoru. Začněte na 20–30 sekundách a dýchejte normálně.</li>'
                 '<li><strong>Boční plank.</strong> Opora o předloktí a bok chodidla, loket pod ramenem, boky zvednuté tak, aby tělo tvořilo rovnou čáru. Lehčí verze je opora o kolena. Cvičte obě strany stejně dlouho.</li>'
                 '<li><strong>Dead bug.</strong> Vleže na zádech ruce nahoru ke stropu, kolena pokrčená nad boky. Bedra přitlačte k podložce a pomalu spouštějte opačnou ruku a nohu k zemi. Bedra se nesmí odlepit. Vynikající cvik pro začátečníky.</li>'
                 '<li><strong>Bird dog.</strong> Na čtyřech, ruce pod rameny, kolena pod boky. Natáhněte opačnou ruku a nohu do prodloužení trupu, chvíli vydržte a vraťte se. Pánev se nesmí natáčet do strany.</li>'
                 '<li><strong>Crunch.</strong> Vleže, kolena pokrčená, chodidla na zemi. Zvedněte jen hlavu a lopatky, bedra zůstávají na podložce. Netahejte se rukama za hlavu, ruce mohou ležet na hrudníku.</li>'
                 '<li><strong>Zvedání nohou vleže.</strong> Vleže na zádech, ruce podél těla nebo pod hýžděmi. Nohy zvedejte do svislé polohy a pomalu spouštějte jen tak nízko, dokud bedra zůstávají přitisknutá. S pokrčenými koleny je cvik lehčí.</li>'
                 '<li><strong>Ruská rotace.</strong> V sedu se zakloňte asi o 45 stupňů, záda rovná, a otáčejte trupem ze strany na stranu. Pohyb vychází z hrudníku, ne jen z rukou. Pokročilí zvednou chodidla nebo drží kotouč.</li>'
                 '<li><strong>Hollow hold.</strong> Vleže zvedněte lopatky a nohy nad zem, bedra tlačte do podložky a tělo vytvoří mělkou „lodičku“. Výdrž 15–30 sekund. Kdo bedra neudrží, pokrčí kolena nebo dá ruce k tělu.</li>'
                 '</ol>'
                 '<p>Podložky různé tloušťky a délky najdete v kategorii <a href="/joga-a-podlozky/">jóga a podložky</a>. Na posilování stačí 6–10 mm, na klečení se hodí silnější.</p>'
             ), cat='joga-a-podlozky', n=4),
        dict(h2='Cviky na břicho v posilovně a s pomůckami',
             html=(
                 '<ol start="9">'
                 '<li><strong>Posilovací kolečko (ab wheel).</strong> Z kleku vyjíždějte kolečkem dopředu, dokud udržíte bedra bez prohnutí, a vraťte se silou břicha. Začněte s krátkým rozsahem, třeba proti zdi, která kolečko zastaví. Patří mezi nejnáročnější cviky typu anti-extenze.</li>'
                 '<li><strong>Zvedání kolen nebo nohou ve visu.</strong> Na hrazdě nebo v opoře o předloktí na bradlech zvedejte kolena k hrudníku a podsaďte pánev. Nekmitejte, pohyb má být pomalý. Pokročilí zvedají propnuté nohy.</li>'
                 '<li><strong>Dřevorubec na kladce nebo s gumou.</strong> Kladku nebo odporovou gumu uchyťte vysoko a táhněte diagonálně přes tělo dolů k opačnému boku. Pohyb vede trup, paže zůstávají skoro propnuté. Existuje i varianta zespodu nahoru.</li>'
                 '<li><strong>Pallofův tlak.</strong> Stůjte bokem ke kladce nebo k uchycené gumě, rukojeť držte u hrudníku a vytlačte ji před sebe. Guma vás táhne do rotace a vy se nesmíte natočit. Cvik je nenápadný, ale šikmé svaly pracují naplno.</li>'
                 '</ol>'
                 '<p>Hodí se i složené cviky, které břicho zapojí vedlejšně: farmářská chůze s jednou činkou, mrtvý tah, dřepy s činkou nebo kettlebellem. Kdo je dělá pravidelně, potřebuje izolovaných cviků na břicho méně.</p>'
                 '<p>Posilovací kolečka, gumy a další drobnosti srovnáváme v kategorii <a href="/fitness-pomucky/">fitness pomůcky</a>, odporové gumy samostatně v kategorii <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
             ), cat='fitness-pomucky', n=4),
        dict(h2='Plán cvičení na břicho pro začátečníky i pokročilé',
             html=(
                 '<p>Světová zdravotnická organizace doporučuje dospělým posilovat všechny hlavní svalové skupiny alespoň dvakrát týdně. Břicho do toho patří, nemusíte ho ale trénovat každý den. Svaly potřebují mezi tréninky čas na zotavení.</p>'
                 + ABS_PLAN +
                 '<p>Jak plán používat:</p>'
                 '<ol><li>Vyberte 4–5 cviků tak, aby byl zastoupen každý typ: jeden anti-extenzní, jeden anti-rotační nebo boční, jeden s ohybem trupu a jeden s rotací.</li>'
                 '<li>Mezi sériemi odpočívejte 30–60 sekund. Celý blok zabere 10–15 minut, můžete ho zařadit na konec běžného tréninku.</li>'
                 '<li>Přidávejte postupně: nejdřív opakování nebo délku výdrže, potom těžší variantu cviku, nakonec zátěž.</li>'
                 '<li>Když technika na konci série povolí (prohýbají se bedra, cuká se krk), sérii ukončete. Další opakování už posilují spíš zlé návyky.</li></ol>'
                 '<p>Pro kompletní trénink celého těla doma se hodí kombinace s dřepy a kliky. Inspiraci najdete v článcích <a href="/drepy/">dřepy</a> a <a href="/domaci-posilovna/">domácí posilovna</a>.</p>'
             )),
        dict(h2='Nejčastější chyby při cvičení břicha',
             html=(
                 '<ul>'
                 '<li><strong>Prohnutá bedra.</strong> U zvedání nohou, planku i kolečka je to chyba číslo jedna. Když se bedra odlepí od podložky nebo propadnou, zkraťte rozsah nebo zvolte lehčí variantu.</li>'
                 '<li><strong>Tahání za hlavu.</strong> Při crunchi ruce za hlavou jen lehce podpírají. Brada nemá padat na hrudník, mezi bradou a hrudníkem udržte asi pěst.</li>'
                 '<li><strong>Zadržování dechu.</strong> Krátký nádech a zpevnění před pohybem je v pořádku, dlouhé zadržení dechu ne. Vydechujte při nejtěžší fázi cviku.</li>'
                 '<li><strong>Rychlost místo kontroly.</strong> Sto rychlých sklapovaček udělá méně práce než dvacet pomalých. Kývání a švihy přenášejí práci na kyčelní flexory.</li>'
                 '<li><strong>Jen jeden typ cviku.</strong> Samé crunche bez planku a rotací vynechávají hluboké a šikmé svaly i záda.</li>'
                 '<li><strong>Zapomenutá záda.</strong> Na každý cvik ohýbající trup dopředu zařaďte i cvik na zádové svaly, třeba bird dog nebo supermana.</li>'
                 '<li><strong>Trénink každý den do vyčerpání.</strong> Více není lépe. Dva až čtyři kvalitní tréninky týdně stačí.</li>'
                 '</ul>'
             )),
        dict(h2='Vybavení: co se vyplatí mít doma',
             html=(
                 '<p>Většinu cviků na břicho odcvičíte jen s vlastní vahou. Pár věcí ale trénink zpříjemní a umožní přidávat zátěž:</p>'
                 '<ul><li><strong>Podložka</strong> s protiskluzovým povrchem, alespoň 180 cm dlouhá, aby se vešla celá záda i hlava.</li>'
                 '<li><strong>Posilovací kolečko</strong>, ideálně se širším kolem nebo dvojitým kolečkem, které je stabilnější. Pod kolena se hodí měkký polštářek.</li>'
                 '<li><strong>Odporové gumy</strong> na Pallofův tlak a dřevorubce. Gumu uchyťte do pevného bodu, ne za kliku dveří, která se může otevřít.</li>'
                 '<li><strong>Jednoruční činka nebo kettlebell</strong> na ruskou rotaci, farmářskou chůzi a zatížené planky.</li>'
                 '<li><strong>Hrazda do dveří</strong> pro zvedání kolen ve visu. Ověřte nosnost a šířku zárubně.</li></ul>'
                 '<p>Činky a kettlebelly najdete v kategoriích <a href="/jednorucni-cinky/">jednoruční činky</a> a <a href="/kettlebelly/">kettlebelly</a>. Krátký intervalový trénink, do kterého se cviky na břicho dobře vejdou, popisuje článek <a href="/tabata/">tabata</a>.</p>'
             ), cat='jednorucni-cinky', n=4),
    ],
    faq=[
        ('Jaký je nejlepší cvik na břicho?',
         '<p>Jediný nejlepší cvik neexistuje. Dobrý základ tvoří kombinace planku, bočního planku, dead bugu a zvedání nohou. Pokročilí přidají posilovací kolečko a zvedání nohou ve visu.</p>'),
        ('Jak často cvičit břicho?',
         '<p>Dvakrát až čtyřikrát týdně stačí. Mezi tréninky nechte den odpočinku. Každodenní cvičení do vyčerpání nepřináší lepší výsledky a zvyšuje riziko přetížení.</p>'),
        ('Zhubnu cvičením na břicho na břiše?',
         '<p>Ne přímo. Studie ukazují, že posilování břicha samo o sobě nesnižuje tuk na břiše. O úbytku tuku rozhoduje hlavně celkový energetický příjem a výdej, cviky na břicho zlepšují sílu a vytrvalost svalů.</p>'),
        ('Jsou sedy-lehy škodlivé?',
         '<p>Pro zdravého člověka nejsou nebezpečné, ale nejsou ani nutné. Plné sedy-lehy hodně zapojují kyčelní flexory. Pro posílení břicha stačí crunch, kde se zvedají jen lopatky, a cviky typu plank nebo dead bug.</p>'),
        ('Jak dlouho držet plank?',
         '<p>Začátečníkům stačí 20–30 sekund v dobré technice, opakované ve dvou až třech sériích. Delší výdrže přes dvě minuty už přinášejí málo. Je lepší přejít na těžší variantu, třeba plank s dotykem ramen.</p>'),
        ('Můžu cvičit břicho při bolestech zad?',
         '<p>Záleží na příčině bolesti. Někomu pomáhají stabilizační cviky jako dead bug nebo bird dog, jinému mohou uškodit. Při bolestech zad se vždy nejdřív poraďte s lékařem nebo fyzioterapeutem.</p>'),
        ('Co cvičit na břicho po porodu?',
         '<p>Po porodu se může objevit rozestup přímých břišních svalů. Vhodné cviky a vhodný čas pro návrat k posilování by měl určit lékař nebo fyzioterapeut se zaměřením na tuto oblast. Tento článek odbornou konzultaci nenahrazuje.</p>'),
        ('Proč mě při cvičení bolí krk?',
         '<p>Nejčastěji se při crunchi táhnete rukama za hlavu nebo tlačíte bradu na hrudník. Uvolněte ruce, dívejte se šikmo ke stropu a zvedejte se z břicha. Pomůže i kratší rozsah pohybu.</p>'),
        ('Jakou podložku na cvičení břicha vybrat?',
         '<p>Protiskluzovou, dlouhou alespoň 180 cm a silnou 6–10 mm. Tenčí jógová podložka na posilování tlačí v oblasti kostrče, příliš měkká zase zhoršuje stabilitu při planku.</p>'),
    ],
    cats=['joga-a-podlozky', 'fitness-pomucky', 'posilovaci-gumy', 'jednorucni-cinky', 'kettlebelly'],
    updated='2026-11-19')

# ---------------------------------------------------------------- tabata
TABATA_WORKOUTS = T(['Trénink', 'Cvik v intervalech 1–8', 'Pro koho'], [
    ['Bez vybavení', 'Dřepy, kliky, horolezec, výskoky – každý cvik 2× za sebou', 'Začátečníci po zaučení techniky'],
    ['Kardio', 'Skipping, jumping jacks, burpees, rychlé výpady – střídat', 'Ti, kdo chtějí hlavně zadýchání'],
    ['S kettlebellem', 'Švihy kettlebellem ve všech osmi intervalech', 'Pokročilí se zvládnutou technikou švihu'],
    ['Na rotopedu nebo veslovacím trenažéru', 'Maximální úsilí ve všech osmi intervalech', 'Nejbližší původnímu protokolu'],
    ['Švihadlo', 'Přeskoky snožmo nebo střídavě, pokročilí dvojšvihy', 'Kdo má zvládnuté skákání přes švihadlo'],
])

GUIDES['tabata'] = dict(
    name='Tabata',
    h1='Tabata: co to je, jak cvičit a ukázkové tréninky',
    seo_title='Tabata: co to je, jak cvičit a ukázkové tréninky',
    seo_desc='Tabata je intervalový trénink 20 s zátěže a 10 s pauzy, osmkrát za sebou. Odkud pochází, jak ho cvičit doma, ukázkové tréninky a pro koho se nehodí.',
    intro_html=(
        '<p><strong>Co je tabata?</strong> Krátký intervalový trénink, ve kterém se 20 sekund cvičí s maximálním nebo téměř maximálním úsilím a 10 sekund odpočívá. '
        'Tento cyklus se opakuje osmkrát, takže jedno kolo trvá čtyři minuty. Název pochází od japonského vědce Izumiho Tabaty, který protokol v roce 1996 zkoumal ve studii na rotopedu. '
        'Doma se tabata nejčastěji cvičí s vlastní vahou: dřepy, kliky, burpees, horolezec nebo výskoky. Před ní se musíte zahřát a po ní vydýchat.</p>'
        '<p>V článku vysvětlíme, co přesně studie zjistila a co ne, jak si tabatu poskládat, kolik kol stačí, ukážeme pět hotových tréninků a upozorníme na chyby. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů, takže pod některými částmi najdete pomůcky, které se k tabatě hodí.</p>'
        '<p>Tabata je velmi náročná na srdce a oběhový systém. Pokud máte onemocnění srdce, vysoký krevní tlak, jste těhotná, po úrazu nebo dlouho jste nesportovali, poraďte se před začátkem s lékařem.</p>'
    ),
    sections=[
        dict(h2='Odkud tabata pochází: studie z roku 1996',
             html=(
                 '<p>Izumi Tabata a jeho kolegové publikovali v roce 1996 v odborném časopise Medicine and Science in Sports and Exercise studii, která porovnávala dva způsoby tréninku po dobu šesti týdnů:</p>'
                 '<ul><li><strong>Vytrvalostní skupina</strong> šlapala na rotopedu 60 minut v mírné intenzitě, kolem 70 % maximální spotřeby kyslíku (VO<sub>2</sub>max), pět dní v týdnu.</li>'
                 '<li><strong>Intervalová skupina</strong> šlapala 7–8 úseků po 20 sekundách v intenzitě kolem 170 % VO<sub>2</sub>max s 10sekundovými pauzami.</li></ul>'
                 '<p>Výsledek: maximální spotřeba kyslíku vzrostla v obou skupinách. U intervalové skupiny stoupla zhruba o 7 ml/kg/min a anaerobní kapacita, tedy schopnost podat krátký maximální výkon, o 28 %. '
                 'Vytrvalostní skupina anaerobní kapacitu významně nezlepšila. Krátký, ale extrémně intenzivní trénink tak zlepšil oba systémy zároveň.</p>'
                 '<p>Je dobré vědět, co studie <strong>neříká</strong>. Zkoumala malou skupinu mladých sportujících mužů na rotopedu s přesně změřenou zátěží. Intenzita 170 % VO<sub>2</sub>max znamená, že po sedmi až osmi intervalech už účastníci nebyli schopni pokračovat. '
                 'Většina „tabata“ lekcí s dřepy a kliky takové intenzity nedosáhne. Pořád jde o užitečný intervalový trénink, jen ne o přesnou kopii původního protokolu.</p>'
             )),
        dict(h2='Jak cvičit tabatu krok za krokem',
             html=(
                 '<ol>'
                 '<li><strong>Zahřátí 8–10 minut.</strong> Klus na místě, krouživé pohyby v ramenou a kyčlích, několik pomalých dřepů a kliků. Do maximálního úsilí nesmíte jít se studenými svaly.</li>'
                 '<li><strong>Nastavte časovač.</strong> Stačí aplikace v telefonu nebo sportovní hodinky s intervalovým režimem: 20 s práce, 10 s pauza, 8 opakování.</li>'
                 '<li><strong>Zvolte cvik</strong>, který zvládáte technicky i ve velké únavě. Složité cviky s činkou nad hlavou do tabaty nepatří.</li>'
                 '<li><strong>Cvičte naplno.</strong> Během 20 sekund dělejte co nejvíc kvalitních opakování. Počítejte je, ať můžete výkon příště porovnat.</li>'
                 '<li><strong>V pauze stůjte nebo přešlapujte.</strong> Deset sekund je málo, nesedejte si, jen se připravte na další interval.</li>'
                 '<li><strong>Po čtyřech minutách</strong> chvíli volně přecházejte. Pokud chcete další kolo, odpočívejte mezi koly 1–2 minuty.</li>'
                 '<li><strong>Vychladnutí a protažení</strong> 5 minut: pomalá chůze, uvolnění lýtek, stehen a ramen.</li>'
                 '</ol>'
                 '<p>Intervalové časovače mají i mnohé běžecké a chytré hodinky. Srovnání najdete v kategorii <a href="/sportovni-hodinky/">sportovní hodinky</a>.</p>'
             ), cat='sportovni-hodinky', n=4),
        dict(h2='Pět ukázkových tabata tréninků',
             html=(
                 '<p>Každý řádek tabulky je jedno čtyřminutové kolo. Začátečníci zvládnou jedno nebo dvě kola, zkušenější tři až čtyři s pauzou mezi nimi.</p>'
                 + TABATA_WORKOUTS +
                 '<p><strong>Ukázka celého tréninku bez vybavení (asi 25 minut):</strong></p>'
                 '<ol><li>Zahřátí 8 minut.</li>'
                 '<li>Kolo 1: dřepy (intervaly 1–4) a kliky (intervaly 5–8). Pauza 2 minuty.</li>'
                 '<li>Kolo 2: horolezec (1–4) a výpady střídavě (5–8). Pauza 2 minuty.</li>'
                 '<li>Kolo 3: burpees (1–4) a plank s dotykem ramen (5–8).</li>'
                 '<li>Vychladnutí a protažení 5 minut.</li></ol>'
                 '<p>Techniku burpees krok za krokem popisuje článek <a href="/burpees/">burpees</a>, správný dřep článek <a href="/drepy/">dřepy</a>. Kettlebelly ve všech hmotnostech srovnáváme v kategorii <a href="/kettlebelly/">kettlebelly</a>.</p>'
             ), cat='kettlebelly', n=4),
        dict(h2='Pro koho se tabata hodí a pro koho ne',
             html=(
                 '<p><strong>Hodí se</strong> pro zdravé lidi s alespoň základní kondicí, kteří mají málo času a chtějí trénink zpestřit. Dobře doplní běh, kolo nebo posilování. Sportovci ji využívají k rozvoji schopnosti opakovaně podat krátký maximální výkon.</p>'
                 '<p><strong>Opatrnost je na místě</strong>, pokud:</p>'
                 '<ul><li>úplně začínáte se sportem – nejdřív si vybudujte základ mírnějším pohybem, třeba svižnou chůzí, lehkým během nebo cvičením podle článku <a href="/kardio-doma/">kardio doma</a>,</li>'
                 '<li>máte nemoc srdce, vysoký krevní tlak, cukrovku nebo jinou chronickou nemoc,</li>'
                 '<li>jste těhotná nebo krátce po porodu,</li>'
                 '<li>zotavujete se z úrazu kloubů nebo zad,</li>'
                 '<li>máte nadváhu a skokové cviky zatěžují kolena – volte varianty bez výskoku nebo rotoped.</li></ul>'
                 '<p>Ve všech těchto případech se o vhodnosti intenzivního intervalového tréninku poraďte s lékařem. Tabata není léčba a tento článek nenahrazuje odbornou radu.</p>'
             )),
        dict(h2='Jak často tabatu zařadit a jak se zlepšovat',
             html=(
                 '<p>Protože jde o velmi intenzivní zátěž, dvě až tři tabaty týdně obvykle stačí. Mezi nimi nechte alespoň jeden den lehčího pohybu nebo odpočinku. Ve zbytku týdne může být klidnější vytrvalostní trénink a posilování.</p>'
                 '<p>Pokrok sledujte jednoduše:</p>'
                 '<ul><li>Zapisujte počet opakování v každém intervalu. Zajímavý je součet i nejslabší interval, který ukazuje, jak dobře zvládáte únavu.</li>'
                 '<li>Po několika týdnech přidejte druhé kolo, ne hned tři.</li>'
                 '<li>Těžší variantu cviku zvolte, až když počty opakování přestanou stoupat a technika je stabilní.</li>'
                 '<li>Měříte-li tep, sledujte, jak rychle po kole klesá. Rychlejší pokles bývá známkou lepší kondice.</li></ul>'
                 '<p>Na skákací cviky se vyplatí tréninková obuv s pevnou patou a stabilní podrážkou. Výběr najdete v kategorii <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
             ), cat='treninkova-obuv', n=4),
        dict(h2='Tabata, HIIT, EMOM a AMRAP: v čem se liší',
             html=(
                 '<p>Ve fitness se potkáte s více zkratkami pro intervalový trénink. Liší se tím, co je pevně dané: čas, počet opakování, nebo obojí.</p>'
                 '<ul><li><strong>HIIT</strong> (high-intensity interval training) je obecný pojem pro střídání krátkých intenzivních úseků s odpočinkem. Délka práce i pauzy může být libovolná, třeba 30/30 nebo 40/20 sekund.</li>'
                 '<li><strong>Tabata</strong> je jedna konkrétní podoba HIIT s poměrem 20/10 a osmi opakováními. Pauza je kratší než práce, takže se únava rychle sčítá.</li>'
                 '<li><strong>EMOM</strong> (every minute on the minute) znamená, že na začátku každé minuty uděláte daný počet opakování a zbytek minuty odpočíváte. Čím rychleji cvičíte, tím delší máte pauzu.</li>'
                 '<li><strong>AMRAP</strong> (as many rounds as possible) je co nejvíc kol nebo opakování za pevně daný čas, třeba za deset minut. Tempo si určujete sami.</li></ul>'
                 '<p>Pro začátečníka bývá příjemnější HIIT s delší pauzou, například 20 sekund práce a 40 sekund odpočinku. Až když zvládne osm takových intervalů v dobré technice, může přejít na pravou tabatu. '
                 'Kdo chce střídat, může si týden rozdělit: jeden den tabatu, jiný den EMOM s dřepy nebo burpees a mezi tím klidný vytrvalostní trénink.</p>'
             )),
        dict(h2='Jak poznat, že cvičíte dost intenzivně',
             html=(
                 '<p>V laboratoři se intenzita měří přesně, doma se musíte řídit pocitem a tepem. Vodítka:</p>'
                 '<ul><li>V posledních intervalech byste neměli být schopni mluvit v celých větách.</li>'
                 '<li>Počet opakování v posledních intervalech obvykle klesne. Když zůstává stejný jako v prvním, máte ještě rezervu.</li>'
                 '<li>Po skončení kola se potřebujete chvíli vydýchat a nemáte chuť hned pokračovat.</li></ul>'
                 '<p>Hrudní pás nebo hodinky s měřením tepu ukážou, jak vysoko se tep během kola dostane. Konkrétní hodnoty se ale mezi lidmi hodně liší, proto je porovnávejte jen sami se sebou. '
                 'Pozor na opačný extrém: závrať, nevolnost, bolest na hrudi nebo neobvyklá dušnost jsou důvod okamžitě přestat a obrátit se na lékaře.</p>'
             )),
        dict(h2='Nejčastější chyby',
             html=(
                 '<ul>'
                 '<li><strong>Vynechané zahřátí.</strong> Skok do maximálního úsilí bez rozehřátí je nejsnazší cesta ke zranění svalů a šlach.</li>'
                 '<li><strong>Technicky náročné cviky.</strong> Ve třetí minutě přijde velká únava. Výpony s činkou nad hlavu nebo přemístění velké váhy tam nepatří.</li>'
                 '<li><strong>Prodlužování pauz.</strong> Kdo si odpočine 20 sekund místo 10, cvičí jiný intervalový trénink. To není chyba, jen to už není tabata.</li>'
                 '<li><strong>Šetření sil.</strong> Osm intervalů v polovičním tempu je pohodlný kruhový trénink. Tabata funguje jen tehdy, když je úsilí opravdu vysoké.</li>'
                 '<li><strong>Tabata každý den.</strong> Tělo se z vysoké intenzity zotavuje pomaleji. Denní opakování vede k únavě a horším výkonům.</li>'
                 '<li><strong>Kluzký povrch.</strong> Při skocích a burpees je potřeba stabilní podložka nebo podlaha, ne tenký koberec.</li>'
                 '</ul>'
                 '<p>Švihadla, podložky a další pomůcky na intervalový trénink doma najdete v kategoriích <a href="/svihadla/">švihadla</a> a <a href="/joga-a-podlozky/">jóga a podložky</a>.</p>'
             ), cat='svihadla', n=4),
    ],
    faq=[
        ('Co znamená tabata?',
         '<p>Je to intervalový trénink pojmenovaný po japonském vědci Izumim Tabatovi. Skládá se z osmi intervalů po 20 sekundách maximálního úsilí s 10 sekundami pauzy, celkem čtyři minuty.</p>'),
        ('Stačí čtyři minuty tabaty jako celý trénink?',
         '<p>Pokud je úsilí opravdu maximální, jsou čtyři minuty velmi náročné. Většina lidí si ale zaslouží delší trénink: zahřátí, dvě až čtyři kola tabaty a protažení, celkem 20–30 minut.</p>'),
        ('Jak často cvičit tabatu?',
         '<p>Dvakrát až třikrát týdně, s alespoň jedním dnem lehčího pohybu mezi tréninky. Častěji se tělo nestihne zotavit.</p>'),
        ('Hubne se tabatou?',
         '<p>Tabata zvyšuje energetický výdej jako každý pohyb, ale čtyřminutové kolo samo o sobě spálí jen omezené množství energie. Na hubnutí má větší vliv celkový pohyb během týdne a strava.</p>'),
        ('Jaké cviky jsou na tabatu nejlepší?',
         '<p>Jednoduché cviky zapojující velké svalové skupiny: dřepy, výpady, kliky, burpees, horolezec, švihy kettlebellem, skákání přes švihadlo, rotoped nebo veslovací trenažér.</p>'),
        ('Můžu tabatu cvičit jako začátečník?',
         '<p>Ano, ale v upravené podobě: cviky bez skoků, jedno nebo dvě kola a úsilí, které udržíte v dobré technice. Úplní začátečníci by měli nejdřív pár týdnů budovat základní kondici.</p>'),
        ('Jaký je rozdíl mezi tabatou a HIIT?',
         '<p>HIIT je obecný název pro vysoce intenzivní intervalový trénink s různou délkou práce a pauzy. Tabata je jeden konkrétní protokol HIIT: 20 sekund práce, 10 sekund pauzy, osmkrát.</p>'),
        ('Potřebuji na tabatu nějaké vybavení?',
         '<p>Ne nutně. Stačí časovač a místo na cvičení. Podložka, švihadlo nebo kettlebell trénink zpestří, rotoped umožní cvičit blíž původní studii.</p>'),
        ('Je tabata bezpečná?',
         '<p>Pro zdravé lidi se základní kondicí a dobrou technikou obvykle ano. Při nemocech srdce, vysokém tlaku, těhotenství nebo po úrazu se nejdřív poraďte s lékařem.</p>'),
    ],
    cats=['sportovni-hodinky', 'kettlebelly', 'svihadla', 'treninkova-obuv', 'joga-a-podlozky'],
    updated='2026-11-19')

# ---------------------------------------------------------------- burpees
BURPEE_VARIANTS = T(['Varianta', 'Jak se liší', 'Obtížnost'], [
    ['Burpee bez výskoku a kliku', 'Dřep, odskok do planku, přiskok, postavit se', 'Lehká'],
    ['Krokový burpee', 'Nohy do planku i zpět se pokládají po jedné, bez skoku', 'Lehká, šetrná ke kloubům'],
    ['Burpee u vyvýšené opory', 'Ruce na lavici nebo schodu místo na zemi', 'Lehká až střední'],
    ['Klasický burpee', 'Dřep, plank, klik, přiskok, výskok s tlesknutím', 'Střední'],
    ['Burpee s přeskokem', 'Místo výskoku přeskok přes nízkou překážku nebo stranou', 'Střední až těžká'],
    ['Burpee s výskokem na bednu', 'Po přiskoku následuje výskok na stabilní bednu', 'Těžká'],
    ['Burpee s kettlebellem nebo činkami', 'Opora o činky, po postavení přítah nebo nadhoz', 'Těžká'],
])

BURPEE_PLAN = T(['Týden', 'Varianta', 'Trénink (3× týdně)'], [
    ['1–2', 'Krokový burpee', '5 sérií × 5 opakování, pauza 60 s'],
    ['3–4', 'Burpee bez kliku s malým výskokem', '5 × 6–8, pauza 60 s'],
    ['5–6', 'Klasický burpee', '5 × 5, pauza 60–90 s'],
    ['7–8', 'Klasický burpee', '10 opakování každou minutu, 6–8 minut'],
    ['od 9', 'Klasický nebo těžší varianta', 'Tabata nebo co nejvíc opakování za 5 minut, s měřením'],
])

GUIDES['burpees'] = dict(
    name='Burpees',
    h1='Burpees: technika, varianty a plán pro začátečníky',
    seo_title='Burpees: správná technika, varianty a plán na 8 týdnů',
    seo_desc='Jak správně dělat burpees krok za krokem, lehčí i těžší varianty, nejčastější chyby a osmitýdenní plán progrese. Kdo burpees vymyslel a pro koho se nehodí.',
    intro_html=(
        '<p><strong>Jak se dělají burpees?</strong> Z postoje přejdete do podřepu a položíte ruce na zem, odskokem nohou se dostanete do vzporu ležmo (planku), uděláte klik, přiskočíte nohama zpět k rukám, postavíte se a vyskočíte s rukama nad hlavou. '
        'Celý pohyb trvá pár sekund a zapojí nohy, hýždě, hrudník, paže i břicho. Začátečníci vynechají klik a výskok a nohy pokládají po jedné, pokročilí přidávají přeskoky, bednu nebo činky.</p>'
        '<p>V článku popíšeme techniku po krocích, sedm variant od nejlehčí po nejtěžší, chyby, které přetěžují záda a zápěstí, a plán na osm týdnů. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů, proto pod některými částmi uvidíte pomůcky a obuv na trénink.</p>'
        '<p>Burpees jsou dynamický cvik se skokem a rychlou změnou polohy těla. Při potížích se srdcem, krevním tlakem, zády, koleny či zápěstími, v těhotenství nebo po úrazu se nejdřív poraďte s lékařem nebo fyzioterapeutem.</p>'
    ),
    sections=[
        dict(h2='Kdo burpees vymyslel',
             html=(
                 '<p>Cvik nese jméno amerického fyziologa <strong>Royala H. Burpeeho</strong>, který na konci třicátých let na Teachers College Kolumbijské univerzity v New Yorku hledal jednoduchý test zdatnosti. '
                 'Původní burpee byl „čtyřdobý“: dřep s rukama na zemi, odskok do vzporu ležmo, přiskok zpět do dřepu a postavení. Klik ani výskok v něm nebyly.</p>'
                 '<p>Testovaný udělal čtyři opakování za sebou a Burpee porovnával tepovou frekvenci před cvičením a po něm. Během druhé světové války převzala cvik americká armáda do testů zdatnosti pod názvem squat thrust, už jako opakování na čas. '
                 'Klik a výskok přibyly později. Dnešní šestidobá verze je náročnější, než její autor zamýšlel.</p>'
             )),
        dict(h2='Správná technika burpees krok za krokem',
             html=(
                 '<ol>'
                 '<li><strong>Postoj.</strong> Chodidla na šířku boků, váha rovnoměrně na celých chodidlech, ruce volně podél těla.</li>'
                 '<li><strong>Podřep a ruce na zem.</strong> Pokrčte kolena a kyčle, jako byste si sedali, a položte dlaně na zem na šířku ramen kousek před chodidla. Záda zůstávají rovná, nekulatá.</li>'
                 '<li><strong>Odskok do planku.</strong> Přeneste váhu na ruce a odskočte nohama dozadu do vzporu ležmo. Tělo tvoří rovnou linii, břicho a hýždě jsou zpevněné, bedra nepropadají.</li>'
                 '<li><strong>Klik.</strong> Spusťte hrudník k zemi s lokty asi 45 stupňů od těla a vytlačte se zpět. Kdo klik nezvládne v rovné linii, spustí se na kolena nebo klik vynechá.</li>'
                 '<li><strong>Přiskok.</strong> Z planku přitáhněte nohy skokem zpět k rukám, chodidla dopadnou celou plochou na šířku boků nebo o něco víc.</li>'
                 '<li><strong>Postavení a výskok.</strong> Zvedněte hrudník, postavte se a vyskočte s rukama nad hlavou. Dopadněte měkce na přední část chodidel a plynule přejděte do dalšího opakování.</li>'
                 '</ol>'
                 '<p>Dýchejte rytmicky: výdech při kliku a při výskoku, nádech při přiskoku. Tempo zrychlujte, až když každý krok zvládáte bez kompromisů. Na tvrdé podlaze se hodí protiskluzová podložka, ruce pak nekloužou a dopady jsou příjemnější.</p>'
             ), cat='joga-a-podlozky', n=4),
        dict(h2='Varianty burpees od nejlehčí po nejtěžší',
             html=(
                 '<p>Burpees se dají přizpůsobit téměř každé úrovni. Začněte variantou, kterou zvládnete v dobré technice alespoň pětkrát za sebou.</p>'
                 + BURPEE_VARIANTS +
                 '<p>Lehčí varianty nejsou „ošizené“. Krokový burpee zapojí stejné svaly, jen bez nárazů a prudkých skoků. Hodí se pro lidi s vyšší hmotností, pro začátečníky i pro dny, kdy chcete šetřit klouby.</p>'
                 '<p>Pro varianty se zátěží jsou vhodné šestihranné činky, které se po položení nekutálejí, nebo kettlebelly s plochým dnem. Najdete je v kategoriích <a href="/jednorucni-cinky/">jednoruční činky</a> a <a href="/kettlebelly/">kettlebelly</a>.</p>'
             ), cat='jednorucni-cinky', n=4),
        dict(h2='Nejčastější chyby',
             html=(
                 '<ul>'
                 '<li><strong>Propadlá bedra v planku.</strong> Když břicho povolí, páteř se prohne a zátěž jde do beder. Zpevněte trup, nebo dělejte burpees bez kliku.</li>'
                 '<li><strong>„Žabí“ klik.</strong> Hrudník zůstane nahoře a k zemi dopadne nejdřív břicho a boky. Takový klik nic neposiluje, jen zatěžuje záda.</li>'
                 '<li><strong>Kulatá záda v podřepu.</strong> Ruce se dostanou na zem jen předklonem bez pokrčení kolen. Při stovkách opakování to bedra nepotěší.</li>'
                 '<li><strong>Tvrdý dopad.</strong> Dopadat na paty s propnutými koleny přetěžuje kolena i páteř. Dopadejte měkce na přední část chodidla a kolena nechte lehce pokrčená.</li>'
                 '<li><strong>Ruce daleko před tělem.</strong> Ruce položené moc daleko zvětšují rozsah planku a zatěžují ramena. Pokládejte je asi na délku chodidla před špičky.</li>'
                 '<li><strong>Kolena padající dovnitř.</strong> Při přiskoku a výskoku mají kolena mířit stejným směrem jako špičky.</li>'
                 '<li><strong>Rychlost na úkor kvality.</strong> V závodech o počet opakování se technika rozpadá rychle. V běžném tréninku zpomalte a zachovejte všech šest kroků.</li>'
                 '</ul>'
             )),
        dict(h2='Plán na 8 týdnů: od prvního burpee k plynulé sérii',
             html=(
                 '<p>Plán počítá se třemi tréninky týdně a dnem pauzy mezi nimi. Burpees zařaďte po zahřátí, před ostatní cvičení, dokud nejste unavení.</p>'
                 + BURPEE_PLAN +
                 '<p>Jak s plánem pracovat:</p>'
                 '<ol><li>Pokud týden nezvládnete v dobré technice, zopakujte ho. Postup podle kalendáře není závod.</li>'
                 '<li>„Každou minutu“ znamená: na začátku minuty uděláte zadaný počet a zbytek minuty odpočíváte. Když už na odpočinek nezbývá čas, snižte počet opakování.</li>'
                 '<li>Po osmi týdnech si změřte, kolik kvalitních opakování uděláte za pět minut, a test opakujte jednou za měsíc.</li></ol>'
                 '<p>Burpees se výborně hodí i do intervalového tréninku. Jak na to, popisuje článek <a href="/tabata/">tabata</a>, kombinaci s posilováním středu těla článek <a href="/cviky-na-bricho/">cviky na břicho</a>.</p>'
             )),
        dict(h2='Jaké svaly burpees posilují a co od nich čekat',
             html=(
                 '<p>Burpees jsou cvik na celé tělo. V podřepu a při výskoku pracují <strong>stehna, hýždě a lýtka</strong>, v planku a při kliku <strong>hrudník, ramena a tricepsy</strong>, během celého pohybu drží trup <strong>břišní a zádové svaly</strong>. '
                 'Rychlé střídání poloh zvedá tep, takže burpees zároveň trénují vytrvalost.</p>'
                 '<p>Nejsou to ale náhrada klasického posilování. Klik i výskok jsou s vlastní vahou, a kdo chce budovat sílu nohou, bude potřebovat i dřepy se zátěží. Postup popisuje článek <a href="/drepy/">dřepy</a>. '
                 'Burpees se hodí jako rychlá kondiční vložka, na rozcvičení nebo na konec tréninku.</p>'
                 '<p>Na skákání je lepší tréninková obuv s nízkým a stabilním podpatkem než měkce odpružená běžecká bota, ve které se chodidlo při doskoku víc kroutí. Výběr najdete v kategorii <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
             ), cat='treninkova-obuv', n=4),
        dict(h2='Burpee výzvy: kdy dávají smysl',
             html=(
                 '<p>Na sociálních sítích kolují výzvy typu „30 dní burpees“, kde se každý den přidává několik opakování. Pro motivaci mohou fungovat, mají ale dvě slabiny: chybí v nich dny odpočinku a počty rostou rychleji, než se zlepšuje technika.</p>'
                 '<p>Pokud se do výzvy pustíte, upravte si ji: cvičte obden, opakování rozdělte do několika menších sérií během dne a v den, kdy vás bolí zápěstí nebo záda, přejděte na krokovou variantu. '
                 'Pro zkušenější sportovce je užitečnější test než výzva: jednou za měsíc změřte, kolik čistých opakování zvládnete za pět minut, a mezi testy trénujte podle plánu výše.</p>'
             )),
        dict(h2='Kde a s čím burpees cvičit',
             html=(
                 '<ul><li><strong>Podlaha:</strong> rovná, neklouzavá, ideálně podložka nebo gumová puzzle podlaha. Na dlažbě a parketách dopady víc zatěžují klouby.</li>'
                 '<li><strong>Prostor:</strong> stačí plocha zhruba na délku vašeho těla a nad hlavou místo na výskok s rukama nahoru. Pozor na lustry a nízké stropy v podkroví.</li>'
                 '<li><strong>Oblečení:</strong> pružné a přiléhavé, aby se nezachytávalo v planku. Hodí se legíny nebo kraťasy a funkční tričko.</li>'
                 '<li><strong>Venku:</strong> tráva nebo hřiště s umělým povrchem. Na štěrku a mokré trávě hrozí uklouznutí a odřené dlaně.</li></ul>'
                 '<p>Oblečení na trénink srovnáváme v kategoriích <a href="/funkcni-tricka/">funkční trička</a> a <a href="/leginy/">legíny</a>.</p>'
             ), cat='funkcni-tricka', n=4),
    ],
    faq=[
        ('Kolik burpees denně dělat?',
         '<p>Denní cvičení není nutné. Pro začátečníka stačí třikrát týdně několik sérií po 5–10 opakováních. Výzvy typu sto burpees denně vedou při špatné technice spíš k přetížení zápěstí a zad.</p>'),
        ('Jaké svaly burpees posilují?',
         '<p>Stehna, hýždě a lýtka při podřepu a výskoku, hrudník, ramena a tricepsy při kliku a břišní i zádové svaly, které drží trup v planku. Zároveň zvedají tep a trénují vytrvalost.</p>'),
        ('Jak burpees zjednodušit?',
         '<p>Vynechejte klik a výskok, nohy do planku i zpět pokládejte po jedné nebo se opírejte rukama o lavici či schod. Takto upravené burpees zvládne většina začátečníků.</p>'),
        ('Proč mě při burpees bolí záda?',
         '<p>Nejčastěji kvůli propadlým bedrům v planku nebo kulatým zádům v podřepu. Zpomalte, zpevněte břicho a zvolte lehčí variantu. Pokud bolest přetrvává, poraďte se s lékařem nebo fyzioterapeutem.</p>'),
        ('Pomáhají burpees hubnout?',
         '<p>Jsou náročné a zvyšují energetický výdej, ale samy o sobě o hubnutí nerozhodnou. Rozhoduje celkový pohyb během týdne a strava.</p>'),
        ('Kolik burpees za minutu je dobrý výsledek?',
         '<p>Univerzální norma neexistuje, záleží na variantě, výšce a hmotnosti. Smysluplnější je porovnávat se sám se sebou: změřte počet kvalitních opakování za minutu nebo za pět minut a test opakujte po několika týdnech.</p>'),
        ('Je lepší burpee s klikem, nebo bez?',
         '<p>S klikem je cvik náročnější na horní polovinu těla. Pokud klik zvládnete jen s propadlými bedry, je lepší ho vynechat a posilovat zvlášť.</p>'),
        ('Můžu dělat burpees s bolavými koleny?',
         '<p>Zkuste variantu bez výskoku a nohy pokládejte krokem, ne skokem. Při bolesti kolen nebo po úrazu se o vhodnosti cviku nejdřív poraďte s lékařem či fyzioterapeutem.</p>'),
        ('Jak dýchat při burpees?',
         '<p>Vydechujte při kliku a při výskoku, nadechujte se při přiskoku a postavení. Hlavně dech nezadržujte, ve vyšším tempu se rytmus dechu ustálí sám.</p>'),
    ],
    cats=['treninkova-obuv', 'joga-a-podlozky', 'jednorucni-cinky', 'kettlebelly', 'funkcni-tricka'],
    updated='2026-11-19')

# ---------------------------------------------------------------- drepy
SQUAT_TYPES = T(['Druh dřepu', 'Zátěž', 'Na co se zaměřuje', 'Pro koho'], [
    ['Dřep s vlastní vahou', 'Bez zátěže', 'Technika, rozsah pohybu, vytrvalost', 'Každý začátečník'],
    ['Goblet dřep', 'Kettlebell nebo činka u hrudníku', 'Vzpřímený trup, hloubka, síla nohou', 'Začátečníci a mírně pokročilí'],
    ['Dřep s činkou na zádech (back squat)', 'Velká činka na trapézech', 'Maximální síla stehen a hýždí', 'Pokročilí, ideálně pod dohledem trenéra'],
    ['Přední dřep (front squat)', 'Velká činka na předních ramenou', 'Přední stehna, vzpřímený trup', 'Pokročilí s dobrou mobilitou'],
    ['Sumo dřep', 'Bez zátěže nebo činka mezi nohama', 'Vnitřní stehna a hýždě', 'Kdo má pohodlnější široký postoj'],
    ['Bulharský dřep', 'Vlastní váha nebo činky', 'Každá noha zvlášť, rovnováha', 'Mírně pokročilí'],
    ['Výskok z dřepu', 'Vlastní váha', 'Výbušnost, kondice', 'Kdo zvládá dřep bez chyb'],
])

GUIDES['drepy'] = dict(
    name='Dřepy',
    h1='Dřepy: správná technika, druhy dřepů a které svaly posilují',
    seo_title='Dřepy: technika, druhy a které svaly posilují',
    seo_desc='Jak dělat dřepy správně: postoj, hloubka, kolena a záda. Dřep s vlastní vahou, goblet, s činkou na zádech i bulharský. Které svaly posilují a čeho se vyvarovat.',
    intro_html=(
        '<p><strong>Jak se správně dělá dřep?</strong> Postavte se na šířku ramen se špičkami mírně vytočenými ven, zpevněte břicho a spouštějte se současně v kyčlích i kolenou, jako byste si sedali na židli za sebou. '
        'Kolena míří stejným směrem jako špičky, paty zůstávají na zemi a záda jsou rovná. Jděte tak hluboko, jak zvládnete bez podsazení pánve a kulacení beder, obvykle alespoň do roviny stehen s podlahou, a vytlačte se zpět nahoru přes celá chodidla.</p>'
        '<p>Dřepy posilují hlavně přední stehna, hýždě a přitahovače, ale pracují i zadní stehna, lýtka a svaly trupu. V článku najdete postup krok za krokem, přehled sedmi druhů dřepů, odpověď na otázku, jestli kolena smějí přes špičky, nejčastější chyby a jednoduchý plán. '
        'Sporteka nic neprodává, jen porovnává nabídky českých e-shopů, proto pod některými částmi uvidíte činky, kettlebelly a obuv.</p>'
        '<p>Máte-li bolesti kolen, kyčlí nebo zad, jste po operaci, úrazu nebo těhotná, probírejte zatížení dřepem nejdřív s lékařem nebo fyzioterapeutem.</p>'
    ),
    sections=[
        dict(h2='Které svaly dřepy posilují',
             html=(
                 '<ul>'
                 '<li><strong>Čtyřhlavý sval stehenní</strong> (přední strana stehna) – narovnává koleno, při dřepu pracuje nejvíc.</li>'
                 '<li><strong>Velký hýžďový sval</strong> – narovnává kyčel, s hloubkou dřepu se jeho zapojení zvyšuje.</li>'
                 '<li><strong>Přitahovače stehna</strong> (vnitřní strana) – výrazně pomáhají hlavně v hlubokém a širokém dřepu.</li>'
                 '<li><strong>Zadní stehenní svaly a lýtka</strong> – stabilizují koleno a kotník.</li>'
                 '<li><strong>Břišní svaly a vzpřimovače páteře</strong> – drží trup, u dřepu s činkou na zádech velmi intenzivně.</li>'
                 '</ul>'
                 '<p>Dřep proto patří mezi základní cviky silového tréninku a odpovídá pohybům z běžného života: sednout si a vstát, zvednout dítě, vyjít schody. Silné nohy pomáhají při běhu, lyžování, cyklistice i v míčových sportech.</p>'
             )),
        dict(h2='Technika dřepu s vlastní vahou krok za krokem',
             html=(
                 '<ol>'
                 '<li><strong>Postoj.</strong> Chodidla zhruba na šířku ramen, špičky mírně ven, obvykle 10–30 stupňů. Každý má trochu jinou stavbu kyčlí, vyzkoušejte, kde se cítíte nejstabilněji.</li>'
                 '<li><strong>Zpevnění.</strong> Nadechněte se do břicha, zpevněte trup a lehce „zašroubujte“ chodidla do země, aby klenba nepropadala.</li>'
                 '<li><strong>Spouštění.</strong> Začněte pohyb současně v kyčlích a kolenou. Pánev jde dozadu a dolů, kolena dopředu a mírně ven nad špičky.</li>'
                 '<li><strong>Dolní poloha.</strong> Jděte do hloubky, kterou udržíte s rovnými zády a patami na zemi. Trup je mírně nakloněný dopředu, hrudník směřuje spíš dopředu než k zemi.</li>'
                 '<li><strong>Výstup.</strong> Tlačte se celým chodidlem do podlahy, kolena držte nad špičkami a vydechněte za nejtěžším místem pohybu.</li>'
                 '<li><strong>Nahoře</strong> se postavte vzpřímeně, ale nezamykejte kolena prudce do propnutí.</li>'
                 '</ol>'
                 '<p>Pomůcka pro začátečníky: dřepujte na lavici nebo židli a jen se jí lehce dotkněte hýžděmi. Postupně snižujte výšku. Tréninková obuv s pevnou plochou podrážkou je stabilnější než měkká běžecká bota, výběr najdete v kategorii <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
             ), cat='treninkova-obuv', n=4),
        dict(h2='Jak hluboký má dřep být',
             html=(
                 '<p>Obecně se doporučuje jít alespoň do <strong>paralely</strong>, tedy do polohy, kdy jsou stehna rovnoběžně s podlahou a kyčelní kloub je ve výšce kolene. Hlubší dřep víc zapojí hýždě a přitahovače a zlepšuje pohyblivost.</p>'
                 '<p>Správná hloubka je ale ta, kterou zvládnete technicky čistě. Signály, že jste šli příliš hluboko:</p>'
                 '<ul><li>pánev se v dolní poloze podsadí a bedra se zakulatí (anglicky „butt wink“),</li>'
                 '<li>paty se zvednou ze země,</li>'
                 '<li>trup se překlopí výrazně dopředu a dřep se mění v předklon.</li></ul>'
                 '<p>Omezením bývá hlavně pohyblivost kotníků a kyčlí. Pomůže širší postoj, víc vytočené špičky, tenká podložka pod paty nebo vzpěračská obuv se zvýšenou patou. Hloubku lze zvětšovat postupně spolu s protahováním. '
                 'Kdo má potíže s koleny nebo kyčlemi, měl by vhodný rozsah řešit s fyzioterapeutem.</p>'
             )),
        dict(h2='Smějí kolena přes špičky?',
             html=(
                 '<p>Rada „kolena nesmí přes špičky“ se drží dlouho, ale v obecné podobě neplatí. U většiny lidí se kolena v dřepu přirozeně posunou před špičky, zvlášť u vyšších postav s dlouhými stehny nebo při vzpřímeném trupu.</p>'
                 '<p>Studie Fry, Smith a Schilling z roku 2003 porovnávala dřep s činkou, při kterém se kolena volně posouvala dopředu, s dřepem, kde jim v tom bránila překážka. Omezený pohyb kolen snížil zatížení kolenního kloubu, ale výrazně zvýšil zatížení kyčlí a vedl k většímu předklonu trupu, tedy k vyššímu zatížení beder. '
                 'Pozdější měření přineslo menší rozdíl, směr ale zůstal stejný: zátěž z kolen se přesune jinam.</p>'
                 '<p>Důležitější než poloha kolen vůči špičkám je jejich <strong>směr</strong>. Kolena mají mířit nad špičky a nepadat dovnitř. Paty zůstávají na zemi a pohyb je plynulý. '
                 'Lidé s bolestí kolene nebo po operaci mohou mít jiná doporučení, ta patří lékaři nebo fyzioterapeutovi.</p>'
             )),
        dict(h2='Druhy dřepů: od vlastní váhy po činku na zádech',
             html=(
                 SQUAT_TYPES +
                 '<p><strong>Goblet dřep</strong> je ideální druhý krok po dřepu s vlastní vahou. Kettlebell nebo jednoruční činku držíte svisle u hrudníku za horní část. Zátěž vepředu působí jako protiváha, trup zůstává vzpřímenější a hlubší dřep se tak učí snáz. Lokty v dolní poloze míří mezi kolena.</p>'
                 '<p><strong>Dřep s činkou na zádech</strong> umožňuje největší zátěž. Činka leží na horní části trapézových svalů (vysoká poloha) nebo o něco níž přes zadní deltové svaly (nízká poloha), nikdy na krčních obratlích. '
                 'Cvičte ho ve stojanu s bezpečnostními tyčemi nastavenými těsně pod dolní polohu dřepu, případně s dopomocí. Techniku se vyplatí nacvičit s trenérem a teprve potom zvyšovat váhu.</p>'
                 '<p>Kettlebelly všech hmotností najdete v kategorii <a href="/kettlebelly/">kettlebelly</a>, velké činky a kotouče v kategorii <a href="/cinky-a-kotouce/">činky a kotouče</a>.</p>'
             ), cat='kettlebelly', n=4),
        dict(h2='Nejčastější chyby při dřepu',
             html=(
                 '<ul>'
                 '<li><strong>Kolena padají dovnitř.</strong> Při výstupu se kolena stáčejí k sobě. Myslete na to, že kolena tlačíte ven nad špičky, a snižte zátěž. Pomůže i lehká guma kolem kolen při rozcvičení.</li>'
                 '<li><strong>Zvedající se paty.</strong> Váha jde na špičky, kolena a kotníky se přetěžují. Příčinou bývá ztuhlý kotník nebo moc úzký postoj.</li>'
                 '<li><strong>Kulatá záda.</strong> V dolní poloze se zakulatí bedra, nahoře hrudník padá dopředu. Zkraťte rozsah a posilujte trup.</li>'
                 '<li><strong>Začátek pohybu jen koleny.</strong> Kolena vyrazí dopředu a pánev zůstane na místě. Pohyb má začít současně v kyčlích i kolenou.</li>'
                 '<li><strong>Odraz ze dna.</strong> Prudké „pérování“ v dolní poloze se zátěží zatěžuje kolena. Dolní polohu kontrolujte a výstup začněte plynule.</li>'
                 '<li><strong>Příliš velká váha příliš brzy.</strong> Činka zkracuje rozsah a rozbíjí techniku. Přidávejte malé kroky a jen tehdy, když jsou všechna opakování čistá.</li>'
                 '<li><strong>Pohled dolů nebo vysoko nahoru.</strong> Krk držte v prodloužení páteře, pohled směřuje dopředu nebo mírně dolů.</li>'
                 '</ul>'
             )),
        dict(h2='Plán: kolik dřepů dělat a jak přidávat',
             html=(
                 '<p>Pro zdravého začátečníka stačí dva až tři tréninky nohou týdně s alespoň jedním dnem pauzy. Jednoduchý postup:</p>'
                 '<ol><li><strong>Týden 1–3:</strong> dřep na lavici nebo s vlastní vahou, 3 série po 10–15 opakováních, pomalé spouštění na 3 sekundy.</li>'
                 '<li><strong>Týden 4–6:</strong> goblet dřep s lehkým kettlebellem nebo činkou, 3–4 série po 8–12 opakováních.</li>'
                 '<li><strong>Týden 7 a dál:</strong> těžší goblet dřep, bulharský dřep nebo nácvik dřepu s velkou činkou, 3–5 sérií po 5–8 opakováních.</li></ol>'
                 '<p>Zátěž zvyšujte, když všechna opakování ve všech sériích zvládnete s dobrou technikou a pár opakování by ještě šlo navíc. Pro ženy i muže začínající s goblet dřepem se často hodí kettlebell 8–16 kg, záleží ale na zkušenostech a síle.</p>'
                 '<p>Výskoky z dřepu a burpees jsou kondiční varianty pro intervalový trénink, viz články <a href="/burpees/">burpees</a> a <a href="/tabata/">tabata</a>. Pro sestavení celého domácího tréninku se hodí článek <a href="/domaci-posilovna/">domácí posilovna</a>.</p>'
             ), cat='cinky-a-kotouce', n=4),
        dict(h2='Vybavení na dřepy doma i v posilovně',
             html=(
                 '<ul><li><strong>Kettlebell nebo jednoruční činka</strong> na goblet dřep. Kettlebell se drží pohodlněji za ucho, činka se nastavitelnými kotouči umožní zvyšovat zátěž po malých krocích.</li>'
                 '<li><strong>Velká činka, kotouče a stojan</strong> s bezpečnostními zarážkami na dřep s činkou na zádech. Bez stojanu a zarážek dřep s velkou zátěží doma necvičte.</li>'
                 '<li><strong>Lavice</strong> na bulharský dřep a jako cíl hloubky pro začátečníky. Výběr najdete v kategorii <a href="/posilovaci-lavice/">posilovací lavice</a>.</li>'
                 '<li><strong>Odporová guma</strong> nad kolena na rozcvičení hýždí.</li>'
                 '<li><strong>Obuv s plochou pevnou podrážkou</strong> nebo vzpěračská obuv se zvýšenou patou pro lidi s ztuhlými kotníky.</li></ul>'
                 '<p>Kdo posiluje i střed těla, najde doplňkové cviky v článku <a href="/cviky-na-bricho/">cviky na břicho</a>. Odporové gumy srovnáváme v kategorii <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
             ), cat='posilovaci-gumy', n=4),
    ],
    faq=[
        ('Jaké svaly posilují dřepy?',
         '<p>Hlavně čtyřhlavý sval stehenní, velký hýžďový sval a přitahovače stehna. Pomáhají zadní stehenní svaly a lýtka, trup drží břišní svaly a vzpřimovače páteře.</p>'),
        ('Jak hluboký má být dřep?',
         '<p>Ideálně alespoň do roviny stehen s podlahou, pokud to zvládnete s rovnými zády a patami na zemi. Hlubší dřep je v pořádku, když se pánev v dolní poloze nepodsazuje.</p>'),
        ('Můžou kolena při dřepu přes špičky?',
         '<p>U většiny lidí ano, je to přirozené. Násilné držení kolen za špičkami přesouvá zátěž do kyčlí a beder. Důležité je, aby kolena mířila stejným směrem jako špičky a nepadala dovnitř.</p>'),
        ('Kolik dřepů denně dělat?',
         '<p>Denní dřepy nejsou nutné. Pro začátečníka stačí dva až tři tréninky týdně po třech sériích s 10–15 opakováními. Se zátěží se počet opakování snižuje a mezi tréninky je potřeba víc pauzy.</p>'),
        ('Jsou dřepy špatné pro kolena?',
         '<p>Pro zdravá kolena je správně provedený dřep běžnou a vhodnou zátěží. Při bolesti kolene, po úrazu nebo operaci se o vhodném rozsahu a zátěži poraďte s lékařem nebo fyzioterapeutem.</p>'),
        ('Co je goblet dřep?',
         '<p>Dřep s kettlebellem nebo jednoruční činkou drženou svisle u hrudníku. Zátěž vpředu pomáhá udržet vzpřímený trup, proto je goblet dřep vhodný na nácvik techniky.</p>'),
        ('Proč se mi při dřepu zvedají paty?',
         '<p>Nejčastěji kvůli ztuhlým kotníkům, úzkému postoji nebo přenášení váhy na špičky. Zkuste širší postoj, víc vytočené špičky, tenkou podložku pod paty a protahování lýtek.</p>'),
        ('Jakou váhu kettlebellu zvolit na dřepy?',
         '<p>Takovou, se kterou uděláte 10–12 čistých opakování a pár by ještě šlo navíc. Začátečníkům často sedí 8–16 kg, záleží ale na síle a zkušenostech.</p>'),
        ('Jak dýchat při dřepu?',
         '<p>Nadechněte se a zpevněte břicho před spouštěním, vydechněte až za nejtěžší částí výstupu. U lehkých dřepů můžete dýchat volněji, dech ale nezadržujte dlouho.</p>'),
        ('V jakých botách dělat dřepy?',
         '<p>V obuvi s pevnou a plochou podrážkou, která se pod zátěží neprobořuje. Měkce odpružené běžecké boty snižují stabilitu. Lidem se ztuhlými kotníky pomáhá vzpěračská obuv se zvýšenou patou.</p>'),
    ],
    cats=['cinky-a-kotouce', 'kettlebelly', 'jednorucni-cinky', 'posilovaci-lavice', 'treninkova-obuv'],
    updated='2026-11-19')
