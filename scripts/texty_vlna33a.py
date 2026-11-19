"""sporteka.cz — wave 33a (19. 11. 2026): long texts for the new shoe categories volejbalova-obuv and boxerske-boty.
General true facts only, no prices, no product counts, no test results. Model names were checked against the local
catalogue copy (Mizuno Wave Lightning / Momentum / Luminous / Voltage / Stealth, Cyclone Speed, Thunder Blade Z, Asics Sky
Elite FF MT, Netburner Ballistic FF, Gel-Rocket, Upcourt, Nike Zoom/React Hyperset, Adidas Crazyflight, Joma V.Blok /
V.Impulse; Nike Hyperko 3, Machomai 3, Inflict 3, Asics Matflex 7, Snapdown 4, Split Elite, Matcontrol, Adidas Box Hog,
Leone 1947, Everlast Elite 2, Lonsdale, Benlee). Brands linked only if present in src/texts/znacky.json.

Sources:
- Mizuno EU product pages Wave Lightning Z8 (emea.mizuno.com): volleyball indoor shoe, Mizuno Wave plate, Enerzy foam,
  a MID version is sold; Wave Momentum 3 reviews (weartesters.com): wide stable base, Enerzy + Wave
- FIVB Official Beach Volleyball Rules 2025-2028 (via EDB Hong Kong infographic and UN Inter-Agency Games rules): players play
  barefoot unless the referee authorises socks or shoes
- asics.com "How to choose the best wrestling shoes": snug fit without wiggle room, finger test at the ankle, split sole =
  flexibility, unisole = durability, high-top for ankle support, boxing shoes flat for pivoting vs wrestling grip at any angle
- AIBA Technical Rules (2015) and boxing explainers: competitors box in light boots or shoes without spikes or heels
- Wrestling explainers (NBC Olympics "Wrestling 101 equipment"): shoes close firmly around the ankle, no heels, nails,
  buckles or metal parts; NCAA women's rulebook: laces taped or secured against unfastening
- Retailer pages (made4fighters, Sport Chek, Dick's): Machomai 3 mid-cut, mesh upper, gum rubber outsole; Hyperko 2 high
  boot with support around ankle and midfoot
Left out (not verifiable): sole heights in mm, weights of individual models, the Leone 1947 founding story, which Mizuno
or Asics model is meant for which volleyball position beyond the maker's own wording, whether Nike Tawa is still made.
"""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ volejbalova-obuv
NEW['volejbalova-obuv'] = dict(long=True,
    title='Volejbalové boty – sálovky na volejbal Mizuno, Asics',
    desc='Volejbalové boty do haly: nízké i mid, podrážka z gumy, tlumení při dopadu a boční opora. Porovnejte nabídky českých obchodů.',
    intro='<p><strong>Volejbalové boty</strong> jsou sálová obuv postavená pro výskoky, dopady a rychlé kroky do strany. Mají gumovou podrážku, která na palubovce drží a nedělá černé šmouhy, a mezipodešev, která tlumí doskok po smeči nebo bloku. Od běžecké boty se liší hlavně nízko položenou patou a pevnějším bokem, od obyčejné tenisky tím, že vydrží stovky odrazů za trénink.</p>'
          '<p>V kategorii najdete modely, které se v českých halách objevují nejčastěji: Mizuno Wave Lightning, Wave Momentum, Wave Luminous a Cyclone Speed, Asics Sky Elite FF, Netburner Ballistic a Gel-Rocket, Nike Hyperset, Adidas Crazyflight nebo Joma V.Blok. Jsou tu pánské, dámské i juniorské verze v nízkém a středně vysokém střihu. Ke každému páru uvidíte nabídky českých e-shopů. Další boty do tělocvičny jsou v kategorii <a href="/salova-obuv/">sálová obuv</a>, míče a sítě v sekci <a href="/volejbal/">volejbal</a>.</p>',
    guide='<h2>Čím se volejbalová bota liší od jiné sálovky</h2>'
          '<p>Volejbal je sport, ve kterém se hodně skáče a při tom se málo běhá rovně. Hráč udělá za zápas desítky výskoků, dopadá často na jednu nohu a mezi tím se pohybuje krátkými kroky do stran. Bota proto potřebuje dobré tlumení pod přední částí chodidla i pod patou, pevnou patní část a podrážku, která se na palubovce nesmeká, ale zároveň umožní rychlé otočení.</p>'
          '<p>Házenkářské a squashové boty jsou volejbalovým podobné, a proto je některé obchody řadí dohromady. Například Mizuno Wave Stealth nebo Adidas Crazyflight se prodávají pro házenou i volejbal. Basketbalová bota bývá těžší a vyšší, tenisová má odolnější podrážku navrženou spíš pro antuku nebo tvrdý kurt. Běžecká bota se do haly nehodí vůbec: má vysokou a měkkou patu, úzkou základnu a při došlapu do strany se v ní kotník snadno podvrtne.</p>'
          '<h2>Podrážka: guma, která nešpiní palubovku</h2>'
          '<p>Většina volejbalových bot má podrážku z měkké gumy, často v barvě karamelu nebo průhledně medovou. Taková guma na čisté palubovce i na umělém povrchu dobře drží. Haly obvykle vyžadují obuv, která nezanechává stopy, takže venkovní tenisky s tmavou tvrdou podrážkou do tělocvičny nepatří. Na podrážce bývá vzor s kruhovým bodem pod bříškem palce, kolem kterého se noha otáčí.</p>'
          '<p>Měkká guma se na asfaltu a betonu rychle obrousí a nasbírá prach, který pak v hale klouže. Volejbalky proto nenoste ven a do haly je noste v tašce. Přilnavost se zlepší, když podrážku před zápasem otřete vlhkým hadříkem. Hráči si mezi výměnami často přejíždějí dlaní po podrážce právě proto, aby z ní setřeli prach.</p>'
          '<h2>Tlumení a stabilita</h2>'
          '<p>Každý výrobce má vlastní řešení. Mizuno používá v mezipodešvi plastovou destičku ve tvaru vlny, které říká Wave. Ta rozkládá sílu při dopadu a zároveň zpevňuje botu do stran. Novější modely Mizuno kombinují Wave s pěnou Enerzy. Asics staví na pěně FlyteFoam, kterou nese zkratka FF v názvech Sky Elite FF a Netburner Ballistic FF, a na gelových vložkách, podle nichž se jmenuje řada Gel. Nike má v Hypersetu pěnu React nebo Zoom podle verze.</p>'
          '<p>Obecně platí, že lehký hráč, který hraje rychle u sítě, ocení nízkou a lehkou botu s dobrým odrazem. Těžší hráč nebo ten, kdo hodně skáče na smeč, potřebuje víc tlumení a širší základnu. Prodejci například popisují Wave Lightning jako botu pro rychlé a hodně skákající hráče, Wave Momentum má širší a stabilnější střed. Rozdíly mezi řadami se ale s každou novou verzí mění, takže je dobré číst popis konkrétního modelu.</p>'
          '<h2>Nízké, nebo mid?</h2>'
          + T(['Střih', 'Pro koho', 'Na co myslet'], [
              ['Nízký (low)', 'smečaři, nahrávači, rychlí hráči', 'nejlehčí, kotník volný, větší volnost pohybu'],
              ['Středně vysoký (mid, MT)', 'hráči po výronu, blokaři, těžší hráči', 'límec kolem kotníku, pocitově jistější, o něco těžší'],
              ['Juniorský (GS, JR)', 'děti a mládež', 'užší kopyto, menší velikosti, často jednodušší konstrukce']]) +
          '<p>Středně vysoký střih poznáte podle zkratky Mid nebo MT v názvu, například Asics Sky Elite FF MT, Mizuno Wave Lightning Mid, Wave Momentum Mid nebo Adidas Crazyflight Mid. Vyšší límec dává pocit pevnosti, ale sám o sobě výronu nezabrání. Kdo měl kotník zraněný, má si nechat od lékaře nebo fyzioterapeuta poradit, zda použít ortézu nebo tejpování. Ortézy a chrániče najdete v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Volejbalová bota má sedět pevně v patě a nad nártem, ale prsty potřebují malou rezervu. Při doskoku se noha v botě posune dopředu a palec nesmí narážet do špičky. Většinou stačí zhruba půl centimetru mezi nejdelším prstem a koncem boty. Zkoušejte ve sportovních ponožkách, ve kterých budete hrát, a odpoledne, kdy je noha mírně oteklá.</p>'
          '<p>Mizuno i Asics jsou japonské značky, ale šířka kopyta se liší model od modelu, nejen mezi značkami. Spolehlivější než číslo je délka chodidla v centimetrech. Změřte ji podle návodu v článku <a href="/tabulka-velikosti/">tabulka velikostí</a> a porovnejte s tabulkou výrobce. U dámských modelů je kopyto užší a v patě menší, proto ženy s širokou nohou často sáhnou po pánské verzi v menším čísle.</p>'
          '<h2>Materiál svršku</h2>'
          '<p>Svršek bývá z mesh tkaniny, která dobře větrá, se zesílením v místech, kde se noha opírá o bok boty. Moderní modely mají pletený nebo jednodílný svršek s vnitřní ponožkou, který obepne nohu bez tlaku. Nahrávači a libera, kteří často klečí nebo padají na zem, ocení zesílenou špičku, protože o palubovku se nejvíc odírá právě ona. Kůže se u volejbalových bot používá málo, je těžká a hůř dýchá.</p>'
          '<h2>Boty pro začátečníky a rekreační hráče</h2>'
          '<p>Kdo hraje jednou týdně s kamarády, nepotřebuje vrcholový model. Stačí lehčí sálová bota s gumovou podrážkou a slušným tlumením, například Asics Gel-Rocket nebo Upcourt, Mizuno Cyclone Speed nebo Joma V.Impulse. Jsou jednodušší a obvykle levnější, přesto mají podrážku vhodnou do haly. Dražší modely se vyplatí hráčům, kteří trénují několikrát týdně a hrají soutěž, protože vydrží víc odrazů a lépe drží nohu při prudkých změnách směru.</p>'
          '<p>Děti rostou rychle a bota jim vydrží jednu nebo dvě sezóny. Pro ně dávají smysl juniorské verze s označením GS nebo JR. Velikost nekupujte „na vyrůstání“ o dvě čísla větší, v příliš volné botě noha klouže a dítě se snáz zraní.</p>'
          '<h2>A co plážový volejbal?</h2>'
          '<p>Plážový volejbal se podle pravidel FIVB hraje naboso. Rozhodčí může povolit ponožky nebo obuv, typicky když je písek rozpálený nebo naopak studený. Halové volejbalky se na písek nehodí, písek se dostane dovnitř a guma k tomu není určená. Na beach se používají neoprenové ponožky do písku, které chrání chodidlo před horkem a drobnými kamínky. Podobné ponožky najdete v kategorii <a href="/obuv-do-vody/">obuv do vody</a>, míče na beach mezi <a href="/volejbalove-mice/">volejbalovými míči</a>.</p>'
          '<h2>Ponožky, vložky a doplňky</h2>'
          '<p>K volejbalovým botám se hodí sportovní ponožky s polstrováním v patě a pod bříškem prstů. Bavlněné ponožky nasáknou pot a noha v botě začne klouzat, lépe fungují směsi polyesteru nebo polyamidu. Hráči často nosí vyšší ponožky, které chrání lýtko při pádu. Pokud máte předepsané ortopedické vložky, vyjměte z boty tu původní a vyzkoušejte, zda se ta vaše do boty vejde. Výběr najdete v kategoriích <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/vlozky-do-bot/">vložky do bot</a>. Na kolena, o která se při pádech opíráte, patří <a href="/ortezy-na-koleno/">chrániče kolen</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Po tréninku boty vyndejte z tašky, povolte tkaničky a vyjměte vložky, aby vyschly. Nedávejte je na topení ani do sušičky, lepené spoje a pěna teplem trpí. Prát v pračce se nedoporučuje, svršek stačí otřít vlhkým hadříkem a podrážku umýt vlažnou vodou. Tlumení se postupně opotřebuje dřív, než je bota vidět sešlapaná. Když po doskoku začnou bolet paty nebo kolena, které dřív nebolely, nebo je podrážka pod bříškem prstů hladká, je čas na nový pár.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U stejného modelu se v obchodech prodává několik generací, například Wave Lightning Z7 a Z8 nebo Sky Elite FF MT 3 a 4. Starší generace bývá výrazně levnější a pro většinu hráčů je stejně dobrá. Kontrolujte, zda jde o pánskou, dámskou nebo juniorskou verzi, střih low nebo mid a velikostní systém (EU, UK, US). Pozor také na lifestylové tenisky se jménem sportovní řady, které mají tvrdou podrážku a do haly nejsou. Volejbalky najdete i u značek ' + B(('mizuno', 'Mizuno'), ('asics', 'Asics'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('joma', 'Joma')) + '.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Hraní v běžeckých botách. Vysoká měkká pata a úzká podešev nedrží nohu při pohybu do strany.</li>'
          '<li>Nošení halových bot venku. Guma se obrousí a podrážka pak v hale klouže.</li>'
          '<li>Bota o číslo větší. Noha v ní při doskoku jezdí a odírá se.</li>'
          '<li>Spoléhání na mid střih místo ortézy nebo tejpu po zranění kotníku.</li>'
          '<li>Sušení na topení, po kterém se podrážka začne odlepovat.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi volejbalovou a běžeckou botou?', 'Volejbalová bota má nízko položenou patu, širokou základnu a gumovou podrážku do haly. Běžecká bota je navržená pro pohyb dopředu a do strany nohu nedrží.'),
        ('Můžu hrát volejbal v házenkářských botách?', 'Většinou ano. Házenkářské boty jsou stavbou podobné a některé modely se prodávají pro oba sporty.'),
        ('Vybrat nízké, nebo vysoké volejbalové boty?', 'Nízké jsou lehčí a dávají volnost pohybu. Mid střih dává kotníku pocit opory, ale po zranění nenahradí ortézu ani tejp.'),
        ('Jak poznat, že volejbalky nedělají šmouhy?', 'Hledejte gumovou podrážku označenou jako non-marking nebo vhodnou do haly. Světlá karamelová guma je u volejbalek obvyklá.'),
        ('Jak velké volejbalové boty koupit?', 'Před nejdelším prstem nechte zhruba půl centimetru. Měřte délku chodidla v centimetrech a porovnejte ji s tabulkou výrobce.'),
        ('Sedí Mizuno a Asics stejně?', 'Ne vždy. Šířka a tvar kopyta se liší i mezi modely jedné značky, proto porovnávejte délku chodidla s tabulkou výrobce.'),
        ('Hraje se plážový volejbal v botách?', 'Podle pravidel FIVB se hraje naboso. Ponožky nebo obuv může povolit rozhodčí, typicky na rozpáleném písku.'),
        ('Jak dlouho vydrží volejbalové boty?', 'Záleží na počtu tréninků a hmotnosti hráče. Opotřebené tlumení poznáte podle bolesti pat nebo kolen a hladké podrážky.'),
        ('Můžu volejbalky prát v pračce?', 'Raději ne. Svršek otřete vlhkým hadříkem, podrážku omyjte vodou a boty nechte vyschnout volně, ne na topení.'),
        ('Kde koupit volejbalové boty?', 'Sporteka u každého modelu zobrazí nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ boxerske-boty
NEW['boxerske-boty'] = dict(long=True,
    title='Boxerské a zápasnické boty – obuv do ringu a na žíněnku',
    desc='Boxerské a zápasnické boty: tenká podrážka, opora kotníku, split sole a velikosti. Porovnejte nabídky českých obchodů na jednom místě.',
    intro='<p><strong>Boxerské a zápasnické boty</strong> jsou lehké vysoké boty s tenkou podrážkou, ve kterých noha cítí podlahu ringu nebo žíněnku. Podrážka nemá podpatek ani výrazné tlumení, takže boxer stojí nízko a rychle se otáčí na špičce. Vysoký svršek se šněrováním až nad kotník drží nohu při úkrocích a tlačení. Zápasnická bota je podobná, má ale podrážku stavěnou na úchop v jakémkoli úhlu nohy.</p>'
          '<p>V kategorii jsou boxerské boty Nike Hyperko, Machomai a Inflict, zápasnické Asics Matflex, Snapdown, Split Elite a Matcontrol, Adidas Box Hog a dále boxerské boty Leone 1947, Everlast, Lonsdale nebo Benlee. Najdete pánské, dámské i dětské velikosti. Ke každému páru uvidíte nabídky českých e-shopů. Rukavice a další výbavu do ringu najdete v sekci <a href="/bojove-sporty/">bojové sporty</a>.</p>',
    guide='<h2>Proč nebojovat v běžných teniskách</h2>'
          '<p>Běžecká nebo fitness bota má silnou mezipodešev a zvýšenou patu. Boxer v ní stojí výš, hůř cítí podlahu a při otočce na přední části chodidla může podrážka zabrat a kotník nebo koleno se stočí jinam než tělo. Na žíněnce je tlustá bota ještě horší: je těžká, špatně se v ní pracuje nohama a tvrdou hranou podrážky může soupeře zranit. Pravidla amatérského boxu proto požadují lehkou obuv bez hrotů a bez podpatku a zápasnická pravidla obuv bez podpatku, hřebíků, přezek a kovových částí.</p>'
          '<p>Na kondiční trénink v posilovně nebo na skákání přes švihadlo stačí obyčejná <a href="/treninkova-obuv/">tréninková obuv</a>. Boxerské boty mají smysl, jakmile začnete sparovat, trénovat práci nohou v ringu nebo zápasit.</p>'
          '<h2>Boxerské, nebo zápasnické?</h2>'
          + T(['', 'Boxerská bota', 'Zápasnická bota'], [
              ['Podrážka', 'plochá, s bodem pro otočku pod bříškem', 'obepíná nohu, úchop v různých úhlech'],
              ['Klenba', 'spíš plochá', 'výraznější tvarování'],
              ['Typický pohyb', 'krok, úkrok, otočka na špičce', 'klek, převalování, tlak do strany'],
              ['Příklady', 'Nike Hyperko, Machomai, Everlast Elite 2, Leone 1947', 'Asics Matflex, Snapdown, Split Elite, Adidas Box Hog']]) +
          '<p>Asics ve své poradně píše, že boxerské boty jsou plošší a stavěné pro otáčení na místě, kdežto zápasnické mají tvarovanou klenbu a podrážku, která drží i při ohnutém nebo vytočeném chodidle. V praxi se obě skupiny často prolínají. Hodně lidí, kteří chodí na kickbox, krav magu nebo MMA tréninky v tělocvičně, nosí zápasnické boty, protože jsou dostupnější a odolné. Na čistý box v ringu je ale lepší boxerská bota.</p>'
          '<p>MMA, brazilské jiu-jitsu, judo a thajský box se trénují a zápasí naboso. Boty se tu nosí nanejvýš na rozcvičku, do zápasu ne. Kdo dělá kickbox, ten se řídí pravidly své disciplíny a pořadatele: některé formy se boxují v botách, jiné naboso s chrániči nártů.</p>'
          '<h2>Podrážka: split sole a celá podrážka</h2>'
          '<p>U zápasnických a některých boxerských bot existují dva typy podrážky. Dělená podrážka (split sole) má zvlášť kus gumy pod přední částí a pod patou, střed je jen z látky. Bota je díky tomu ohebnější a lehčí, typickým příkladem je Asics Split Elite. Celistvá podrážka (unisole) vede gumu po celé délce. Je odolnější a pod klenbou drží víc. Pro začátečníky a pro rekreační trénink je celistvá podrážka obvykle praktičtější, split sole volí zkušenější zápasníci, kteří chtějí co nejvíc cítit žíněnku.</p>'
          '<p>Boxerské boty mají gumovou podrážku, na kterou se dá dobře točit. Na podlaze ringu, která je potažená plachtou, i na sálové podlaze nesmí podrážka lepit ani klouzat. Proto se boxerky stejně jako zápasnické boty mimo tělocvičnu nenosí. Prach a písek z ulice snižují úchop a obrušují tenkou gumu.</p>'
          '<h2>Výška a opora kotníku</h2>'
          '<p>Boxerské boty se vyrábějí ve třech výškách. Nízké sahají pod kotník a jsou nejlehčí. Středně vysoké, jako Nike Machomai, končí zhruba na kotníku. Vysoké, jako Nike Hyperko nebo klasické boty Leone 1947 a Everlast Elite 2, sahají nad kotník a obepínají spodní část lýtka. Vysoká bota nohu drží, tkaničky se ale šněrují déle. Zápasnické boty jsou téměř vždy vysoké.</p>'
          '<p>Vysoký svršek pomáhá kotník stabilizovat a chrání ho před odřením o žíněnku. Výronu ale nezabrání a nenahradí tejpování ani ortézu. Pokud se po starém zranění kotník snadno podvrtne, poraďte se s lékařem nebo fyzioterapeutem, jaká opora je pro vás vhodná.</p>'
          '<h2>Jak má bota sedět</h2>'
          '<p>Boxerská i zápasnická bota má sedět těsně. Asics doporučuje zkusit vsunout prsty mezi botu a kotník: pokud se vejdou, je bota spíš velká. Na rozdíl od běžecké boty tu nehledáte volné místo před prsty, stačí, když palec nenaráží do špičky. Svršek ze syntetické kůže nebo mesh se nošením trochu povolí, takže bota, která je nová v pohodě, za pár týdnů může být volná.</p>'
          '<p>Střih se liší podle značky i modelu, proto boty pokud možno zkoušejte. U boxerek se často uvádějí velikosti v systému US nebo UK. Přepočet podle obecné tabulky nemusí odpovídat, raději porovnejte délku chodidla v centimetrech s tabulkou konkrétního výrobce. Návod na měření najdete v článku <a href="/tabulka-velikosti/">tabulka velikostí</a>. Zkoušejte v tenkých sportovních ponožkách, ve kterých budete trénovat. Tlusté ponožky v těsné botě způsobí, že noha nemá kontakt s podlahou.</p>'
          '<h2>Tkaničky a jejich zajištění</h2>'
          '<p>Vysoké boty se šněrují přes celý nárt až nad kotník. Některé modely mají pásek přes horní část nebo kapsu na tkaničky. Rozvázaná tkanička v ringu znamená přerušení a na žíněnce za ni může soupeř zachytit prsty. Pravidla zápasu proto často vyžadují tkaničky zajistit, obvykle páskou nebo krytem. Tkaničky si tedy po zavázání zastrčte nebo přelepte. Asymetrické šněrování, které posouvá řadu dírek mimo střed nártu, umožní botu stáhnout pevněji a nedře přes šlachy.</p>'
          '<h2>Materiál svršku</h2>'
          '<p>Starší a klasické boxerské boty mají svršek ze semišové nebo hladké kůže, novější modely kombinují syntetiku a síťovinu. Kůže vydrží déle a nohu drží pevně, ale hůř odvádí pot. Síťovina je lehká a vzdušná, na tréninku ve vydýchané tělocvičně je příjemnější. Důležité jsou pevné švy, protože při úkrocích a tlačení se na svršek působí silou do stran. U levných bot povolují nejdřív švy v místě, kde se ohýbá chodidlo.</p>'
          '<h2>Ring, tělocvična, nebo posilovna?</h2>'
          '<p>Boxerské boty jsou dělané na podlahu ringu a na sálovou podlahu. Pro trénink v posilovně, kde se zvedají činky, nemají potřebnou oporu ani tlumení, na kondiční běh venku vůbec nejsou. Mezi boxerskými kluby se běžně trénuje v jedněch botách a do zápasu se bere druhý, méně opotřebený pár. Zápasníci mají podobný zvyk: tréninkové boty s celistvou podrážkou a lehčí soutěžní boty.</p>'
          '<p>Na trénink doma, třeba na <a href="/boxovaci-pytle/">boxovací pytel</a> v garáži, boxerské boty potřeba nejsou. Postačí obuv s tenkou podrážkou, na které se dá točit. Pokud pytel visí na betonu nebo dlažbě, dejte pod sebe gumovou podložku, ta chrání podrážku i kolena.</p>'
          '<h2>Boty pro děti</h2>'
          '<p>Dětské a juniorské verze mají označení GS, Jr nebo Kids. Asics Matflex se například prodává v juniorské řadě GS. Dítě vyroste z boty rychleji, než ji ošoupe, ale ani tady neplatí kupovat o dvě čísla větší. Volná bota se v ní posouvá a dítě v ní ztrácí rovnováhu. Před nákupem se zeptejte trenéra, zda klub boty vůbec vyžaduje. V některých oddílech děti začínají naboso nebo v obyčejných sálovkách.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po tréninku boty vyndejte z tašky, povolte šněrování a vytáhněte vložku, pokud jde vyjmout. Nechte je schnout při pokojové teplotě, ne na topení. Kožené boty jednou za čas ošetřete přípravkem na kůži, aby nepraskaly. Podrážku otírejte vlhkým hadříkem, nikdy nepoužívejte lak nebo silikon, které by ji udělaly kluzkou. Silný zápach z bot, kde se potí bosá noha, řeší ponožky a pravidelné sušení. Pomůže i dezinfekční sprej na boty, který najdete mezi <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
          '<h2>Co dalšího si k botám pořídit</h2>'
          '<p>Boxer potřebuje kromě bot <a href="/boxerske-rukavice/">boxerské rukavice</a>, bandáže na ruce a <a href="/chranice-zubu/">chránič zubů</a>, na sparing i helmu. Zápasníci a MMA bojovníci nosí <a href="/chranice-bojove-sporty/">chrániče</a> uší a holení podle disciplíny. Oblečení najdete v kategorii <a href="/obleceni-bojove-sporty/">kimona a oblečení</a>.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Kontrolujte, zda jde o boxerskou, nebo zápasnickou botu, výšku svršku, typ podrážky a velikostní systém. Některé obchody řadí boxerky mezi tenisky nebo tréninkovou obuv, a název tak neprozradí, k čemu bota je. U značky Leone 1947 si všimněte, že vedle boxerských bot prodává i dětské lifestylové tenisky, které do ringu nejsou. Boxerské a zápasnické boty najdete u značek ' + B(('nike', 'Nike'), ('asics', 'Asics'), ('adidas', 'Adidas')) + ' i u specialistů na bojové sporty.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Bota o číslo větší. V ringu v ní noha jezdí a kotník nemá oporu.</li>'
          '<li>Nošení boxerek venku. Tenká guma se rychle obrousí a v ringu pak klouže.</li>'
          '<li>Volné tkaničky. Vždy je zastrčte nebo zajistěte páskou.</li>'
          '<li>Tlusté bavlněné ponožky, ve kterých bota nesedí a noha se potí.</li>'
          '<li>Spoléhání na vysoký svršek po zranění kotníku místo konzultace s fyzioterapeutem.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi boxerskými a zápasnickými botami?', 'Boxerská bota má plošší podrážku stavěnou na otáčení na špičce. Zápasnická má tvarovanou klenbu a úchop i při vytočeném chodidle.'),
        ('Můžu boxovat v zápasnických botách?', 'Na tréninku ano a mnoho lidí to dělá. Na box v ringu je pohodlnější plošší boxerská bota.'),
        ('Co znamená split sole?', 'Podrážka je rozdělená na přední a zadní díl, střed je z látky. Bota je ohebnější, celistvá podrážka je zase odolnější.'),
        ('Jak mají boxerské boty sedět?', 'Těsně, bez volného místa kolem kotníku. Když mezi botu a kotník vsunete prsty, je bota spíš velká.'),
        ('Potřebuju boxerské boty jako začátečník?', 'Na první tréninky stačí sálovka s tenkou podrážkou. Boxerky dávají smysl, jakmile začnete sparovat nebo pracovat v ringu.'),
        ('Nosí se boty v MMA nebo thajském boxu?', 'Ne, MMA, thajský box, judo i jiu-jitsu se zápasí naboso. Boty se nosí nanejvýš na rozcvičku.'),
        ('Proč se tkaničky přelepují páskou?', 'Rozvázaná tkanička přeruší zápas a na žíněnce za ni může soupeř zachytit prsty. Pravidla zápasu to často vyžadují.'),
        ('Ochrání vysoká bota kotník před výronem?', 'Kotník drží pevněji, ale výronu nezabrání. Po zranění se poraďte s lékařem nebo fyzioterapeutem o tejpu nebo ortéze.'),
        ('Můžu v boxerských botách chodit venku?', 'Ne. Tenká gumová podrážka se na asfaltu rychle obrousí a nasbírá prach, takže v ringu klouže.'),
        ('Kde koupit boxerské boty?', 'Sporteka u každého páru zobrazí nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])
