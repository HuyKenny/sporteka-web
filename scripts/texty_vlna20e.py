"""sporteka.cz — wave 20e (4. 11. 2026): long texts (>= 1650 words) for kempingovy-nabytek, boxerske-rukavice, cyklo-pedaly, rybarske-obleceni.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ kempingovy-nabytek
NEW['kempingovy-nabytek'] = dict(long=True,
    title='Kempingový nábytek: židle, stoly a lehátka',
    desc='Skládací kempingové židle, křesla, stoly, lehátka a stolky k táboření i na zahradu. Jak vybrat nosnost, rám a velikost a porovnat obchody.',
    intro='<p>Kempingový nábytek promění trávník nebo štěrkovou plochu u stanu v místo, kde se dá pohodlně jíst, číst i povídat do tmy. '
          'Skládací židle, křeslo s držákem na nápoje, stůl s nastavitelnými nohami nebo polohovací lehátko zabírají po složení jen malou část kufru a rozloží se za pár vteřin. '
          'Rozhodují tři věci: kolik místa máte k dispozici v autě nebo na zádech, jak dlouho budete sedět a jakou zátěž má konstrukce vydržet.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Springos, Eurotrail, Nils, Skandika, King Camp, Regatta nebo Naturehike. '
          'K nábytku se hodí <a href="/stany/">stany</a>, <a href="/karimatky-a-matrace/">karimatky a matrace</a>, <a href="/vareni-v-prirode/">vaření v přírodě</a> a <a href="/chladici-boxy/">chladicí boxy</a>. '
          'Níže najdete přehled typů, srovnání materiálů a rady, jak nábytek vybrat a udržet v dobrém stavu.</p>',
    guide='<h2>Co do kempingového nábytku patří</h2>'
          '<p>Kategorie sdružuje všechno, na čem se v táboře sedí, leží nebo odkládají věci. Základ tvoří skládací židle a křesla, doplňují je stoly, stolky a stojany na nádobí, lehátka a podnožníky. '
          'Samostatnou skupinu tvoří dětský nábytek a malé stoličky pro turisty, kteří nesou všechno na zádech. Každý typ řeší trochu jiný problém, a proto se vyplatí nejdřív sepsat, co budete skutečně potřebovat.</p>'
          + T(['Typ', 'Hlavní přednost', 'Hodí se na'], [
              ['Skládací židle', 'nízká váha, jednoduchá obsluha', 'víkend u vody, festival, výlet autem'],
              ['Křeslo s područkami', 'pohodlí na delší sezení, držák na nápoje', 'autokemping, dlouhé večery, rybaření'],
              ['Stolička a trojnožka', 'minimální velikost', 'pěší túra, krátká zastávka, focení'],
              ['Skládací stůl', 'rovná plocha na jídlo a vaření', 'rodinný kemp, grilování, hry'],
              ['Lehátko a polohovací křeslo', 'možnost ležet', 'odpočinek na pláži, zahrada, karavan'],
              ['Sady stůl a židle', 'jednotný vzhled a nosnost', 'rodiny s dětmi, delší pobyt na jednom místě']]) +
          '<h2>Rám a materiál</h2>'
          '<h3>Ocel, hliník a tvrzené plasty</h3>'
          '<p>Ocelový rám je pevný a odolný, ale těžší a při vlhku časem koroduje, pokud nemá kvalitní povrchovou úpravu. Hliník váží výrazně méně a nerezaví, avšak tenké trubky snesou méně nárazů a nevhodně zatížené se ohnou. '
          'U nejlehčích modelů se kombinují duralové tyče a pevný popruh, které jsou oblíbené u turistů. Plastové spoje a patky musí být dostatečně silné, protože právě tam se nejčastěji láme první díl.</p>'
          '<h3>Potah a sedák</h3>'
          '<p>Nejběžnější je polyesterová tkanina, často s označením například 600D, kde vyšší číslo značí hrubší a odolnější vlákno. Tkanina by měla být odolná proti otěru a rychle schnout. '
          'Síťovina na zádech zlepšuje větrání v horku, plný potah zase hřeje při chladnějších večerech. Lehké čalounění z pěny zvyšuje pohodlí, ale pomaleji schne. Ověřte, že potah je přišitý nebo uchycen pevně, a ne jen přeložený přes trubku.</p>'
          '<h2>Nosnost, výška a rozměry</h2>'
          '<p>Údaj o nosnosti uvádí výrobce na štítku a vždy se počítá se statickým zatížením, tedy s klidným sedem. Dynamické namáhání, třeba prudké dosednutí, zatěžuje rám víc, proto nevybírejte model těsně na hranici své váhy. '
          'Výšku sedáku volte podle toho, jak se vám dobře vstává: nízké křeslo je pohodlné, ale hůř se z něj vstává, vysoká židle se hodí ke stolu. Pozor na kombinaci, protože u nízké židle a vysokého stolu nemáte kam položit lokty.</p>'
          '<p>Důležitá je i sbalená velikost. Do kufru osobního auta se vejde několik židlí do tvaru dlouhé tyče, zatímco křesla s pevným rámem vyžadují hodně místa. Délku a průměr sbaleného kusu si přeměřte dopředu, hlavně pokud nábytek vozíte na střeše nebo na kole.</p>'
          '<h2>Židle a křesla podle použití</h2>'
          '<ul><li><strong>Autokemping a rodina:</strong> křeslo s područkami, držákem na nápoje a mírným sklonem opěradla. Váha není tak důležitá jako stabilita a pohodlí. Rozumné je koupit sadu stejných židlí, aby se daly skládat jedna do druhé.</li>'
          '<li><strong>Pěší túra a trek:</strong> ultralehká stolička nebo skládací sedák, který se vejde do bočního zavazadla. Podrobněji o nošení výbavy píše kategorie <a href="/turisticke-batohy/">turistické batohy</a>.</li>'
          '<li><strong>Rybaření:</strong> nízké křeslo s nastavitelnými nohami, které se postaví na nerovný břeh. Rybářské varianty najdete v kategorii <a href="/bivaky-a-kresla/">bivaky a křesla</a> a doplní je <a href="/rybarske-doplnky/">rybářské doplňky</a>.</li>'
          '<li><strong>Festival a pláž:</strong> lehké a levné skládací židle bez zbytečných funkcí, u kterých nevadí, že se zašpiní.</li>'
          '<li><strong>Karavan a zahrada:</strong> polohovací křesla s širokým sedákem, která plní i roli zahradního nábytku a vydrží celé léto venku.</li></ul>'
          '<h2>Stoly a stolky</h2>'
          '<p>Stůl se vybírá podle počtu strávníků a podle toho, co na něm budete dělat. Pro vaření potřebujete pevnou a rovnou desku, na které se nehoupe hrnec. Pro svačinu stačí lehký stolek s rolovací deskou z hliníkových latí. '
          'Nastavitelné nohy pomáhají na svahu a umožňují přizpůsobit výšku židlím. Rámy ze slitiny hliníku jsou lehké, ale deska s rolovacími latěmi snese méně tepla než plná. Desku z umělé hmoty opatrně pokládejte u vařiče, protože horký hrnec ji může deformovat. '
          'K vaření patří kategorie <a href="/varice-a-kartuse/">vařiče a kartuše</a> a <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>'
          '<h2>Lehátka, hamaky a podnožníky</h2>'
          '<p>Skládací lehátko s polohovacím opěradlem nahradí na zahradě i v karavanu postel na odpoledne. Při koupi sledujte délku, aby se vám nohy nedotýkaly země, a pevnost opěrek pro záda. '
          'Pokud preferujete zavěšení mezi stromy, zvažte <a href="/hamaky/">hamaky</a>, které váží méně a dají se rozložit i ve svahu. Podnožník přidá pohodlí ke křeslu a zlepší cirkulaci krve při dlouhém sezení. Na noc se k nábytku hodí <a href="/spaci-pytle/">spací pytle</a>.</p>'
          '<h2>Skládání, přenášení a obsluha</h2>'
          '<p>Dobře navržený kus se rozloží jednou rukou, bez nářadí a bez nebezpečí skřípnutí prstů. Zkontrolujte zámek, který drží křeslo rozložené, a nepoužívejte nábytek, kde se rám zavírá sám při zatížení. '
          'Praktický je obal s popruhem na rameno, v němž nic nepřečnívá a rám se nezašpiní. Pokud nábytek často stěhujete, zvolte model, jehož části jsou stejné a snadno se vymění při poškození.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po návratu domů nábytek otřete vlhkým hadříkem, nechte úplně vyschnout a teprve potom složte. Zbytky písku z kloubů vyfoukejte nebo vyklepejte, jinak se spojení rychle opotřebuje. '
          'Kovové čepy a pružiny čas od času potřete kapkou oleje. Potahy neperte v pračce při vysoké teplotě a nikdy je nesušte na topení. Vlhký složený kus uložený v obalu zplesniví, což je nejčastější příčina předčasné smrti kempingové židle.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě podle vzhledu bez kontroly nosnosti a rozměrů po složení.</li>'
          '<li>Příliš lehká stolička pro dlouhé sezení u ohně, po hodině bolí záda.</li>'
          '<li>Podcenění stability na měkké zemi: úzké nohy se bořívají, patky s plochým chodidlem pomáhají.</li>'
          '<li>Vysoké křeslo a nízký stůl, případně opačně.</li>'
          '<li>Nákup pro celou rodinu naráz, aniž byste vyzkoušeli, jak se vejdou do auta.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete nábytek od značek ' + B(('springos', 'Springos'), ('eurotrail', 'Eurotrail'), ('nils', 'Nils'), ('nils-camp', 'NILS Camp'), ('skandika', 'Skandika'), ('king-camp', 'King Camp'), ('regatta', 'Regatta'), ('naturehike', 'Naturehike'), ('quechua', 'Quechua'), ('outwell', 'Outwell')) + '. '
          'Rozdíly nejsou jen v ceně: levnější kusy mají jednodušší rám a tenčí potah, dražší zlepšují klouby, výplně a sbalenou velikost. Vedle sebe se dá porovnat řada modelů s podobnými parametry, takže nemusíte obcházet jednotlivé e-shopy.</p>'
          '<h2>Kde porovnat nabídky</h2>'
          '<p>Sporteka sleduje české obchody a u každého kusu ukazuje dostupné nabídky vedle sebe. Při výběru nejprve filtrujte podle typu a značky, poté zkontrolujte rozměry a nosnost v popisu. '
          'Pokud skládáte celou výbavu pro tábor, projděte také <a href="/kemping/">kemping</a>, <a href="/stanove-doplnky/">stanové doplňky</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>. Světlo na večer najdete v kategorii <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</p>',
    faq=[
        ('Jakou nosnost má mít kempingová židle?', 'Vyberte model, který má nosnost znatelně nad vaší hmotností, protože údaj platí pro klidné sezení. Při prudkém dosednutí se rám zatěžuje víc. Rodiny s dospělými i dětmi se vyplatí kupovat jednu pevnější řadu.'),
        ('Je lepší ocelový, nebo hliníkový rám?', 'Ocel je pevnější a odolnější proti nárazům, ale těžší a při poškození povrchu koroduje. Hliník je lehký a nerezaví, hodí se do batohu i na kolo. Pro autokemping se hodí obě varianty, pro túru hliník.'),
        ('Jak vybrat výšku židle ke stolu?', 'Sedák má být asi o dvacet až třicet centimetrů pod deskou stolu. Nízké křeslo se ke stolu nehodí, protože se u něj nedá pohodlně jíst. Pokud kupujete sadu, zkontrolujte, zda rozměry odpovídají.'),
        ('Dá se kempingový nábytek nechat venku?', 'Krátkodobě ano, ale slunce a vlhko zkracují životnost potahu i rámu. Při delším pobytu ho zakryjte nebo večer složte. Na zimu ho uložte v suchu a ve vyvětraném prostoru.'),
        ('Jak vyčistit potah židle?', 'Lehké nečistoty smyjte vlažnou vodou s jemným mýdlem a kartáčem. Silné zašpinění nepereme v pračce při vysoké teplotě, protože se poškodí impregnace a lepení. Před složením nechte kus úplně vyschnout.'),
        ('Je lepší sada stůl a židle, nebo samostatné kusy?', 'Sada je pohodlná a obvykle se stejně vejde do jednoho obalu. Samostatné kusy dávají větší volnost při výběru pro konkrétní účel, ale musí se k sobě rozměrově hodit. Pro čtyřčlennou rodinu bývá sada praktičtější.'),
        ('Co si vzít na pěší túru místo židle?', 'Nejlepší je ultralehká stolička nebo skládací sedák, které váží v řádu stovek gramů. Nabídnou oporu při zastávce, ale nenahradí pohodlné křeslo. Pro delší pobyt v jednom táboře se vyplatí vzít něco většího.'),
        ('Jak se vyhnout rozbití spojů na židli?', 'Nenechávejte zatížení jen na jedné straně a neseďte na područkách, pokud nejsou určeny k nosnosti. Klouby udržujte čisté a promazané. Zkontrolujte šrouby a nýty před sezónou a vadný kus nepoužívejte.'),
        ('Hodí se kempingový nábytek i na zahradu a balkon?', 'Ano, lehké skládací židle a stolky se často používají i doma. Zvolte materiály odolné proti slunci a vlhku, například hliník a polyester s UV úpravou. Pro trvalé použití jsou lepší pevné zahradní sestavy.'),
        ('Jaké jsou rozdíly u dětského kempingového nábytku?', 'Dětské židle jsou menší, lehčí a mají nižší nosnost, často s veselým potiskem. Rám musí být stabilní, aby se nepřevrátil, a bez ostrých hran, kde by se dítě skřípnulo. S rostoucím dítětem se rychle stane malým.'),
    ])

# ------------------------------------------------------------------ boxerske-rukavice
NEW['boxerske-rukavice'] = dict(long=True,
    title='Boxerské rukavice: velikost, uncí a materiál',
    desc='Boxerské rukavice na trénink, sparing, pytel i zápasy. Jak vybrat unce, kůži nebo syntetiku a velikost a porovnat obchody.',
    intro='<p>Boxerské rukavice chrání dvě strany: ruce boxera a soupeře. Vnitřní vycpávka tlumí náraz, vnější kůže nebo syntetika drží tvar a zevnitř je zpevněný palec a zápěstí. '
          'Správný výběr závisí na tom, k čemu je budete používat. Na pytel se hodí jiný model než na sparing, a ten se liší od soutěžních rukavic pro amatérské zápasy. Důležitá je velikost, uncová hmotnost, zapínání a tvar vycpávky.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek DBX Bushido, Venum, Bushido, Leone 1947, Benlee, Fairtex, RDX, ACRA Sport, Adidas nebo Hayabusa. '
          'K rukavicím patří <a href="/boxovaci-pytle/">boxovací pytle</a>, <a href="/chranice-bojove-sporty/">chrániče</a>, <a href="/bandaze-a-ortezy/">bandáže</a> a <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a>. '
          'Níže najdete přehled typů, vysvětlení uncí i rady, jak rukavice vybrat a udržet v dobrém stavu.</p>',
    guide='<h2>Co rukavice řeší</h2>'
          '<p>Při úderu se energie přenáší přes pěst na cíl a bez ochrany by hrozilo poranění kloubů, zápěstí i prstů. Rukavice rozkládá náraz do vycpávky a drží ruku ve správné poloze, protože zpevněný palec brání jeho vyvrknutí. '
          'Používání rukavic ale nezbavuje nutnosti správné techniky: i s nejlepším modelem se dá zraněním předejít jen správným držením pěsti a bandážemi.</p>'
          + T(['Typ', 'Určení', 'Co sledovat'], [
              ['Tréninkové rukavice', 'práce s pytlem, lapami, kondiční box', 'pevné zapínání, odolnost materiálu'],
              ['Sparingové rukavice', 'tréninkový souboj', 'větší vycpávka, vyšší uncová hmotnost'],
              ['Pytlové rukavice', 'práce na těžkém pytli', 'tuhá vycpávka, pevné zápěstí'],
              ['Soutěžní rukavice', 'amatérské a profesionální zápasy', 'schválení svazem, předepsaná hmotnost'],
              ['Rukavice na lapy a rychlý pytel', 'rychlost a technika', 'lehčí, tenčí vycpávka'],
              ['Rukavice pro děti', 'začátečníci a mládež', 'menší velikost, měkčí vycpávka'],
              ['MMA a rukavice s volnými prsty', 'MMA, grappling', 'otevřené prsty, tenká vycpávka']]) +
          '<h2>Unce a hmotnost</h2>'
          '<p>Unce označuje hmotnost rukavice, přičemž jedna unce odpovídá zhruba 28 gramům. Vyšší číslo znamená víc vycpávky a hmotnější rukavici. Větší rukavice nejsou vždy lepší: u sparingu chrání soupeře víc vycpávky, zatímco u pytle je důležitá rovnováha mezi ochranou a citem.</p>'
          + T(['Unce', 'Použití', 'Poznámka'], [
              ['8 až 10 oz', 'rychlý trénink, lapy, soutěže lehkých vah', 'lehká a rychlá, málo vycpávky'],
              ['12 oz', 'univerzální trénink, pytel', 'oblíbená volba pro většinu dospělých'],
              ['14 až 16 oz', 'sparing, těžší a vyšší sportovci', 'víc ochrany pro oba účastníky'],
              ['18 oz a víc', 'těžké váhy, silný sparing', 'velmi velká a těžká rukavice']]) +
          '<p>Při výběru se často vychází z hmotnosti sportovce, ale dobrý trenér poradí podle způsobu tréninku. Dospělí ve středním rozsahu obvykle začínají u dvanácti uncí a pro sparing si přidají čtrnáct nebo šestnáct. Děti pracují s menšími rukavicemi, které odpovídají velikosti dlaně.</p>'
          '<h2>Materiál: kůže, syntetika a mikrovlákno</h2>'
          '<p>Pravá kůže vydrží roky, přizpůsobí se ruce a lépe dýchá, ale vyžaduje péči a bývá dražší. Syntetické materiály jsou lehké, snadno se čistí a hodí se pro začátečníky. '
          'Mikrovlákno se snaží kůži napodobit a dobře snáší pot. Kvalita se pozná na švech: dvojité šití, zpevněné rohy a pevné zapínání prodlužují životnost. U levných rukavic se nejdřív rozpadne palec nebo vycpávka v hřbetu.</p>'
          '<h2>Vycpávka a konstrukce</h2>'
          '<p>Vnitřní pěna určuje, jak se rukavice chová. Vícevrstvá pěna se tlumí náraz postupně a drží tvar, měkká jednovrstvá vycpávka se po čase propadne. Dobré rukavice mají zpevněnou hranu u zápěstí a palec přichycený k tělu, aby se neodchýlil. '
          'Tvar dlaně je anatomický a pěst se v něm přirozeně svírá. Při zkoušce zkuste sevřít pěst: nesmí se vám pěna tlačit mezi prsty ani být hmatná pod klouby.</p>'
          '<h2>Zapínání: suchý zip, šněrování a elastika</h2>'
          '<p>Suchý zip je rychlý a pohodlný, takže ho najdete u většiny tréninkových rukavic. Šněrování drží zápěstí nejpevněji, ale vyžaduje pomoc druhé osoby. Elastické manžety se hodí pro lehké tréninkové modely a rychlý pytel. '
          'Zkontrolujte, zda zip drží i po delším používání, protože zanesený suchý zip přestane přilnout. Široký pás nad zápěstím poskytuje oporu a snižuje riziko vyvrknutí.</p>'
          '<h2>Velikost a pohodlí</h2>'
          '<p>Rukavice s uncí se označuje také velikostí, například S, M, L nebo XL, která se odvíjí od obvodu dlaně. Podle toho, zda rukavice dobře obepíná ruku s bandáží, poznáte správnou velikost. '
          'Prsty by měly dosahovat až ke konci, ale špičky se nesmí opírat o stěnu. Při příliš velké rukavici se ruka uvnitř posouvá a vzniká tření, při malé zase hrozí stlačení prstů. Zkoušejte vždy s bandážemi, ne bez nich.</p>'
          '<h2>Bandáže a doplňky</h2>'
          '<p>Bandáž fixuje zápěstí a klouby a zároveň vstřebává pot, který by jinak nasákl do vycpávky. Používá se elastická nebo polostrukturovaná. Další doplňky tvoří <a href="/chranice-bojove-sporty/">chrániče zubů, holení a hlavy</a>, '
          'rukavice pod rukavice, pytel s <a href="/boxovaci-pytle/">boxovacím stojanem</a> a lapy pro trenéra. Pro lepší kondici pomáhají <a href="/svihadla/">švihadla</a> a <a href="/funkcni-trenink/">funkční trénink</a>. '
          'Po tréninku se hodí <a href="/masazni-pomucky/">masážní pomůcky</a> na uvolnění předloktí a ramen.</p>'
          '<h2>Výběr podle cíle</h2>'
          '<ul><li><strong>Začátečník a kondiční box:</strong> univerzální rukavice dvanáct uncí, suchý zip, syntetický materiál. Cenově dostupná varianta stačí, dokud nezjistíte, jak často budete trénovat.</li>'
          '<li><strong>Pravidelný trénink v klubu:</strong> kožené nebo kvalitní syntetické rukavice, případně dva páry: lehčí na pytel a těžší na sparing.</li>'
          '<li><strong>Soutěžící:</strong> rukavice schválené svazem s předepsanou uncovou hmotností a uzavřenou konstrukcí. Zeptejte se trenéra, jaké požadavky platí pro vaši soutěž.</li>'
          '<li><strong>Děti a mládež:</strong> menší modely s měkčí vycpávkou, které se dají snadno nasadit a zapnout.</li>'
          '<li><strong>MMA a thaiboxing:</strong> pro thaibox se hodí rukavice s širší vycpávkou a pohyblivější manžetou pro klinč, pro MMA otevřené prsty. Širší nabídku najdete v kategorii <a href="/bojove-sporty/">bojové sporty</a>.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Pot je největším nepřítelem rukavice. Po tréninku je vyndejte z tašky, rozevřete a nechte vyschnout na vzduchu, ne u radiátoru. Vnitřek lze občas vytřít vlhkým hadříkem a dezinfekčním sprejem, aby se zabránilo pachu. '
          'Absorbční vložky do rukavic pomáhají odvádět vlhkost. Kůži z vnější strany ošetřete jednou za čas vhodným přípravkem, aby nepopraskala. Uložit je do <a href="/sportovni-tasky/">sportovní tašky</a> s větráním je lepší než do vzduchotěsného sáčku.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě rukavic bez bandáží, takže pak nesedí.</li>'
          '<li>Příliš malé unce při sparingu, kdy trpí soupeř.</li>'
          '<li>Použití tréninkových rukavic ke všemu, včetně těžkého pytle, kde se vycpávka rychle propadne.</li>'
          '<li>Uložení mokrých rukavic v tašce přes noc.</li>'
          '<li>Pokračování v používání rukavic, které už ztratily vycpávku nebo mají roztržené švy.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete modely značek ' + B(('dbx-bushido', 'DBX Bushido'), ('venum', 'Venum'), ('bushido', 'Bushido'), ('leone-1947', 'Leone 1947'), ('benlee', 'Benlee'), ('fairtex', 'Fairtex'), ('rdx', 'RDX'), ('acra-sport', 'ACRA Sport'), ('adidas', 'Adidas'), ('top-king', 'TOP King'), ('hayabusa', 'Hayabusa'), ('twins', 'Twins')) + '. '
          'Každá značka má vlastní střih a sklon k určitému stylu: thajské značky často nabízejí pevnější palec a více vycpávky, evropské výrobce zajímá spíše univerzální použití. Porovnáním více kusů zjistíte, který tvar vám sedí.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka sleduje české obchody a u každého páru ukazuje dostupné nabídky vedle sebe. Filtrujte podle značky, velikosti a velikosti v uncích a ověřte dostupnost zvolené velikosti. '
          'Pokud skládáte výbavu celou, projděte <a href="/sportovni-rukavice/">sportovní rukavice</a>, <a href="/treninkova-obuv/">tréninkovou obuv</a> a <a href="/fitness/">fitness</a>.</p>',
    faq=[
        ('Kolik uncí mají mít boxerské rukavice pro začátečníka?', 'Většina dospělých začíná u dvanácti uncí, které jsou univerzální pro pytel i lehký trénink. Lehčí lidé a mládež mohou začínat s menší hodnotou. Na sparing doporučuje trenér obvykle čtrnáct nebo šestnáct uncí.'),
        ('Čím se liší tréninkové a sparingové rukavice?', 'Sparingové mají víc vycpávky, bývají těžší a chrání soupeře. Tréninkové jsou lehčí a vhodné k pytli, lapám a kondičnímu boxu. Pro začátek se pořizuje jeden pár, později se doplní druhý.'),
        ('Je lepší kůže, nebo syntetika?', 'Kůže vydrží déle a lépe se přizpůsobí ruce, ale je dražší a potřebuje péči. Syntetika je lehčí, snadno se čistí a stačí pro začátečníky. Při častém tréninku se kůže zpravidla vyplatí.'),
        ('Mám používat bandáže?', 'Ano, bandáže stabilizují zápěstí a klouby a zároveň chrání rukavice před potem. Správně omotané zlepšují pocit v pěsti a snižují riziko zranění. Je dobré nechat si ukázat omotávání od trenéra.'),
        ('Jak poznám správnou velikost?', 'Ruka v bandáži se musí vejít, aniž by se prsty tlačily do konce. Palec nesmí být volný a zápěstí musí pevně držet. Při sevření pěsti se vám vycpávka nesmí tlačit mezi klouby.'),
        ('Jak odstranit zápach z rukavic?', 'Po tréninku je vždy otevřete a nechte vyschnout. Vnitřek občas vytřete a použijte dezinfekční nebo deodorační sprej určený pro sportovní vybavení. Pomáhají také absorbční vložky a vysoušeče.'),
        ('Dají se rukavice prát v pračce?', 'Většinou ne, protože voda poškodí vycpávku, lepení a kůži. Lépe je čistit je ručně vlhkým hadříkem a nechat vyschnout při pokojové teplotě. Pračka zkracuje životnost i tvar rukavice.'),
        ('Kdy rukavice vyměnit?', 'Když vycpávka ztvrdne nebo propadne, palec se uvolní, švy praskají nebo suchý zip nedrží. Při pravidelném tréninku to bývá po několika sezónách, při intenzivním sparingu dříve.'),
        ('Hodí se boxerské rukavice i na thajský box nebo kickbox?', 'Ano, pro kickbox a thaibox se používají obdobné rukavice, často s o něco měkčí vycpávkou. Thajské značky nabízejí i modely určené pro kombinaci s nízkými kopy.'),
        ('Mají děti jiné rukavice než dospělí?', 'Dětské rukavice jsou menší a lehčí, aby seděly na malou ruku. Mají měkčí vycpávku a snadné zapínání. S růstem ruky se musí měnit velikost, protože příliš velké rukavice zhoršují techniku.'),
    ])

# ------------------------------------------------------------------ cyklo-pedaly
NEW['cyklo-pedaly'] = dict(long=True,
    title='Pedály na kolo: plošinové, nášlapné a SPD',
    desc='Pedály na horské, silniční, trekové i BMX kolo. Plošinové, nášlapné SPD a magnetické: jak vybrat typ, závit a materiál a porovnat obchody.',
    intro='<p>Pedály jsou jediné místo, kudy se výkon z nohou přenáší do kola. Přesto se vybírají podle vzhledu, protože na první pohled vypadají podobně. '
          'Rozdíl mezi plošinovým pedálem s kolíky, nášlapným systémem a lehkým silničním modelem je přitom velký a promítne se do jistoty při jízdě, účinnosti šlapání i bezpečnosti při pádu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Rockbros, Force, HT, Reverse, Race Face, Shimano, Magped, Crankbrothers nebo Wolf Tooth. '
          'K pedálům se vážou <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklisticka-obuv/">cyklistická obuv</a>, <a href="/cyklo-pumpy-a-naradi/">nářadí</a> a <a href="/cyklo-dily/">další díly</a>. '
          'Níže najdete přehled typů, rozdíly mezi materiály a praktické rady k montáži a údržbě.</p>',
    guide='<h2>Základní typy pedálů</h2>'
          '<p>Pedály se dělí podle způsobu, jakým se bota spojuje s kolem. Plošinové pedály mají širokou plochu a nohu jen podpírají. Nášlapné pedály drží botu mechanicky s pomocí kufru. Magnetické pedály se jedním kontaktem připojí k plechu v podrážce a snadno se uvolní. '
          'Nejdůležitější je si ujasnit, jak budete jezdit, protože každý typ nabízí něco jiného.</p>'
          + T(['Typ', 'Princip', 'Typické použití'], [
              ['Plošinové (flat) pedály', 'široká plocha s kolíky nebo gripem', 'MTB, enduro, BMX, městské kolo'],
              ['Nášlapné pedály (SPD)', 'kufr v podrážce drží v pedálu', 'cross-country, trek, cyklistika na dlouhé tratě'],
              ['Silniční zarážky a pedály', 'velký kufr, lehké tělo', 'silniční kolo, závodní jízda'],
              ['Kombinované (hybridní) pedály', 'jedna strana nášlapná, druhá plochá', 'městské a treking kolo'],
              ['Magnetické pedály', 'magnet v pedálu a plech v botě', 'začátečníci, rekreační jízda, městské kolo'],
              ['Pedály s reflexními prvky', 'zvýšená viditelnost', 'město, jízda za šera']]) +
          '<h2>Plošinové pedály</h2>'
          '<p>Plošinové pedály vybírejte podle rozměrů, kolíků a ložisek. Široká plocha dává větší jistotu a lépe rozkládá tlak. Kolíky ze šroubků se dají vyměnit, takže opotřebené je jednoduše obnovíte. '
          'Příliš ostré kolíky bolestivě zraňují lýtka, pokud sklouznete, ale zajistí přilnavost i v mokru. Pro horské kolo se hodí pedály ze slitiny hliníku nebo hořčíku, pro městské a dětské levnější plast. '
          'Nylonové pedály jsou lehké a levné, ale méně pevné. Kvalitnější modely mají uzavřená ložiska a dají se rozebrat a promazat.</p>'
          '<h2>Nášlapné systémy</h2>'
          '<p>Nášlapný pedál se spojí s kufrem přišroubovaným v podrážce boty. Noha je tak pevně vedena a výkon se přenáší i při zdvihu. Pro horské a trekové jízdy se používá menší kufr, který se dá schovat do podrážky a umožňuje chůzi. '
          'Silniční systémy mají větší kufr, dávají větší oporu, ale na chůzi nejsou vhodné. Při první jízdě nastavte uvolňovací sílu na minimum, abyste se z pedálu snadno dostali. '
          'Zvyknout si na výstup z pedálu je nutné procvičit na místě a až potom vyrazit do provozu.</p>'
          '<h3>Kufry a cyklistická obuv</h3>'
          '<p>Kufr musí odpovídat systému pedálu a obuvi. Obuv s dvěma šrouby se hodí pro horskou jízdu, tříšroubová pro silnici. Správné nastavení pozice kufru ovlivňuje zátěž kolen, proto ho měňte po malých krocích. Zkoušejte <a href="/cyklisticka-obuv/">cyklistickou obuv</a> s pedály, které si vyberete, aby se do sebe dobře zasunuly.</p>'
          '<h2>Magnetické pedály</h2>'
          '<p>Magnetický systém spojuje silný magnet v pedálu s kovovou destičkou v botě. Nohu lze odpojit bez nutnosti natáčení paty, což oceníte při jízdě městem a při prvních výjezdech. '
          'Držení není tak pevné jako u mechanických systémů, ale pro rekreační jízdu stačí. Pozor na to, že magnet přitahuje drobné kovové částice a zablácený pedál se musí čistit.</p>'
          '<h2>Materiál, hmotnost a ložiska</h2>'
          '<ul><li><strong>Hliník:</strong> nejběžnější volba, pevný a lehký, vyrábí se frézováním nebo litím.</li>'
          '<li><strong>Hořčík a titan:</strong> méně váhy, ale obvykle jsou dražší a hořčík je citlivý na korozi.</li>'
          '<li><strong>Nylon a kompozit:</strong> lehké a odolné proti korozi, pro rekreační jízdu a děti.</li>'
          '<li><strong>Ocelová osa:</strong> pevnější, často se kombinuje s hliníkovým tělem. Při špatné údržbě se osa zadírá do kliky.</li></ul>'
          '<p>Ložiska se dělí na kuličková a průmyslová, přičemž průmyslová mívají lepší těsnění a delší životnost. Uzavřený pedál zůstává dlouho čistý, ale servis bývá náročnější. Hmotnost se udává za pár a pro běžnou rekreační jízdu není rozhodující.</p>'
          '<h2>Závit a montáž</h2>'
          '<p>Většina dospělých kol má pedály se závitem devět šestnáctin palce, dětská a starší kola mohou mít menší průměr. Pravý pedál má pravotočivý závit, levý levotočivý, ale oba se utahují ve směru jízdy: pravý ve směru hodinových ručiček, levý proti nim. '
          'Před montáží závit vyčistěte a naneste vrstvu maziva. Pedály označené L a R se nesmí zaměnit, jinak zničíte závit v klice. Utahovací moment hledejte v návodu výrobce, obvykle se používá klíč o velikosti patnáct milimetrů nebo imbus. '
          'Kliky najdete v kategorii <a href="/cyklo-pohon/">cyklo pohon</a>.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<ul><li><strong>Horské kolo a enduro:</strong> široké plošinové pedály s kolíky nebo nášlapné systémy, pokud preferujete výkon. Podívejte se na <a href="/horska-kola/">horská kola</a> a <a href="/mtb-a-integralni-helmy/">helmy</a>.</li>'
          '<li><strong>Silniční a gravel kolo:</strong> lehké nášlapné pedály s širším kufrem, pro gravel malý kufr s možností chůze. Podrobnosti o strojích najdete u <a href="/silnicni-a-gravel-kola/">silničních a gravel kol</a>.</li>'
          '<li><strong>Trekové a městské kolo:</strong> hybridní nebo plošinové pedály s reflexními prvky. Na výběr kola se hodí <a href="/trekingova-kola/">trekingová kola</a> a <a href="/mestska-kola/">městská kola</a>.</li>'
          '<li><strong>BMX a dirt:</strong> malé pevné plošinové pedály s kolíky, často hliníkové nebo nylonové. Viz <a href="/bmx-a-dirt-kola/">BMX a dirt kola</a>.</li>'
          '<li><strong>Dětská kola:</strong> jednoduché plastové pedály, které odpovídají závitu a nemají ostré hrany. Pro menší děti nabídka <a href="/detska-kola/">dětských kol</a>.</li>'
          '<li><strong>Elektrokola:</strong> kvůli vyšší hmotnosti a výkonu pevné a široké pedály, často s reflexními prvky. Viz <a href="/elektrokola/">elektrokola</a>.</li></ul>'
          '<h2>Údržba a servis</h2>'
          '<p>Pedály jsou namáhány vodou, blátem a nárazy o překážky. Nejméně dvakrát za rok je zkontrolujte, zda se netočí s vůlí, a ložiska promažte, pokud to konstrukce dovoluje. '
          'Opotřebené kolíky vyměňte, protože podkluz boty zhoršuje ovládání. U nášlapných pedálů čistěte mechanismus od bláta a občas mírně naolejujte pružiny. '
          'Při pádu může dojít k ohnutí osy, takže se ujistěte, že se pedál otáčí hladce. Nářadí a mazivo najdete v kategorii <a href="/cyklo-udrzba/">cyklo údržba</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nové nášlapné pedály nastavené na největší sílu uvolnění.</li>'
          '<li>Špatně zvolená velikost pedálu pro velikost chodidla.</li>'
          '<li>Záměna levého a pravého pedálu při montáži.</li>'
          '<li>Použití plastových pedálů při náročné horské jízdě.</li>'
          '<li>Zanedbání mazání ložisek a osy.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete pedály značek ' + B(('rockbros', 'Rockbros'), ('force', 'Force'), ('ht', 'HT'), ('reverse', 'Reverse'), ('race-face', 'Race Face'), ('max1', 'Max1'), ('shimano', 'Shimano'), ('magped', 'Magped'), ('nexelo', 'Nexelo'), ('m-wave', 'M-Wave'), ('author', 'Author'), ('wolf-tooth', 'Wolf Tooth'), ('crankbrothers', 'Crankbrothers'), ('laceto', 'Laceto')) + '. '
          'Rockbros a Force pokrývají hlavně plošinové a rekreační pedály, Shimano, HT a Crankbrothers mají nášlapné systémy a Magped se zaměřuje na magnetické upínání. Při výběru porovnejte váhu, rozměry a typ ložisek.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka sleduje české obchody a u každého pedálu ukazuje dostupné nabídky vedle sebe. Vyberte typ, sledujte závit a velikost plochy, zkontrolujte, zda je v balení jeden pár, a porovnejte obchody. '
          'K nákupu se hodí i <a href="/cyklo-svetla/">světla</a>, <a href="/cyklisticke-obleceni/">oblečení</a> a <a href="/cyklo-computery/">computery</a>.</p>',
    faq=[
        ('Jaký pedál zvolit na horské kolo?', 'Začátečníkům se hodí široké plošinové pedály s vyměnitelnými kolíky, protože se z nich lehce vystupuje. Pokročilí jezdci často volí nášlapné pedály, které dávají jistotu při výkonu. Rozhodněte se podle terénu.'),
        ('Co jsou pedály SPD?', 'SPD je systém, ve kterém se kufr v podrážce zasune do pedálu a zachytí se pružinou. Bota je pevně spojena, ale po vytočení paty ven se uvolní. Používá se v horské i trekové jízdě.'),
        ('Je nutné používat cyklistickou obuv s nášlapnými pedály?', 'Ano, kufr se přišroubuje do podrážky speciální boty. Obuv má tuhou podrážku, která zlepšuje přenos výkonu. S běžnou botou nášlapný pedál použít nelze.'),
        ('Jak poznám levý a pravý pedál?', 'Pedály jsou označeny písmeny L a R na ose nebo na těle. Levý má levotočivý závit a pravý pravotočivý. Oba se utahují ve směru jízdy, tedy pravý ve směru hodinových ručiček a levý proti nim, a proto se při šlapání samy neuvolňují.'),
        ('Jaké jsou rozměry závitu?', 'Dospělá kola mají nejčastěji závit devět šestnáctin palce. Dětská a starší jednoduchá kola mohou mít menší, proto před koupí ověřte závit na kole. Adaptér lze použít jen výjimečně.'),
        ('Jak často pedály promazávat?', 'Podle způsobu jízdy dvakrát za rok, po jízdě v blátě a dešti častěji. Pokud mají utěsněná ložiska, stačí kontrola vůle a čištění povrchu. Opotřebená ložiska vyměňte.'),
        ('Jak vybrat pedály pro elektrokolo?', 'Hledejte pevnou konstrukci, široký povrch a reflexní prvky. Elektrokolo je těžší a při rozjezdu působí větší síla, takže slabé plastové pedály nejsou vhodné. Hodí se kombinované modely pro městskou jízdu.'),
        ('Jsou magnetické pedály bezpečné?', 'Pro rekreační jízdu fungují dobře, protože bota se snadno uvolní. Upnutí je slabší než u mechanických systémů, takže se nehodí pro výkonnostní jízdu. Při prudkém šlapání nebo hrubém terénu se může noha uvolnit.'),
        ('Jak vyměnit kolíky v plošinovém pedálu?', 'Kolíky se šroubují z druhé strany pedálu malým imbusem. Vyšroubujte opotřebené a našroubujte nové, případně použijte jinou délku. Pedál můžete postupně dostat zpět do stavu, kdy drží botu.'),
        ('Hodí se pedály z nylonu?', 'Nylonové pedály jsou lehké a nerezaví, a proto se hodí pro rekreační jízdu a děti. Pro náročný terén nebo vysoké zatížení doporučujeme kov. Zkontrolujte, zda se při zatížení neohýbají.'),
    ])

# ------------------------------------------------------------------ rybarske-obleceni
NEW['rybarske-obleceni'] = dict(long=True,
    title='Rybářské oblečení a obuv: bundy, prsačky, boty',
    desc='Rybářské bundy, kalhoty, prsačky, brodicí boty, termooblek a rukavice. Jak vybrat vodotěsnost, vrstvy a velikost a porovnat obchody.',
    intro='<p>Rybář tráví u vody hodiny na jednom místě, často v chladu, větru nebo dešti. Dobré oblečení rozhoduje o tom, zda vydrží celou noc i svítání, nebo se vrátí domů po hodině. '
          'Kategorie zahrnuje nepromokavé bundy a kalhoty, termooblek, prsačky a brodicí boty, čepice, rukavice i brýle. U přívlače, kapra a muškaření se potřeby liší, ale zásada zůstává: vrstvit a chránit před vlhkem.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Fox, Grundéns, Caperlan, Fox Rage, Delphin, Westin, Simms, Mikado, Vision, Kinetic nebo Trakker. '
          'K oblečení se hodí <a href="/rybarske-pruty/">pruty</a>, <a href="/rybarske-tasky/">tašky</a>, <a href="/rybarske-spacaky/">spacáky</a>, <a href="/rybarske-stany/">stany</a> a <a href="/rybarske-doplnky/">doplňky</a>. '
          'Níže najdete přehled typů, vrstvení a rady pro nákup.</p>',
    guide='<h2>Základní skupiny</h2>'
          '<p>Rybářský šatník se skládá z několika vrstev, které se doplňují a kombinují podle počasí. Nejblíže k tělu leží spodní prádlo, uprostřed izolace a navrchu nepromokavá a větruodolná vrstva. '
          'K tomu přistupuje obuv, která řeší vodu i chlad od země, a doplňky chránící hlavu a ruce. Brodění vyžaduje navíc prsačky nebo brodicí kalhoty.</p>'
          + T(['Skupina', 'Funkce', 'Typické použití'], [
              ['Bundy a kabáty', 'ochrana před deštěm a větrem', 'celoroční rybaření, loď'],
              ['Kalhoty a overaly', 'vodotěsnost od pasu dolů', 'sezení u vody, loďka'],
              ['Termooblek a zimní soupravy', 'izolace v mrazu', 'kaprařina v zimě, pstruh v chladu'],
              ['Prsačky a brodicí kalhoty', 'ochrana při stání ve vodě', 'muškaření, pstruh, přívlač v řece'],
              ['Brodicí boty', 'pevná opora na dně', 'řeka, potok, kameny'],
              ['Gumové a zimní boty', 'teplo a vodotěsnost', 'břeh, bahno, loď'],
              ['Čepice, rukavice, brýle', 'ochrana hlavy, rukou a očí', 'chlad, slunce, odlesky']]) +
          '<h2>Vrstvení: spodní, střední a vnější</h2>'
          '<h3>Spodní vrstva</h3>'
          '<p>Základem je prádlo odvádějící pot od kůže. Merino zůstane teplé i vlhké a méně zapáchá, syntetika rychleji schne. Bavlnu raději vynechte, protože nasákne a odvádí teplo. Podrobnosti o prádle najdete v kategoriích <a href="/termopradlo/">termoprádlo</a> a <a href="/merino/">merino</a>.</p>'
          '<h3>Střední vrstva</h3>'
          '<p>Fleece nebo lehká izolační bunda zadržuje teplo vzduchu u těla. U rybaření, kde sedíte bez pohybu, počítejte s větší izolací než při chůzi. Zateplená vesta nechává volnost paží při nahazování. Souvisí s tím <a href="/fleecove-mikiny/">fleecové mikiny</a> a <a href="/sportovni-vesty/">sportovní vesty</a>.</p>'
          '<h3>Vnější vrstva</h3>'
          '<p>Nepromokavá bunda s kapucí, zalepenými švy a zipy chrání před deštěm. Vodní sloupec udává odolnost proti vodě, ale důležitější je prodyšnost, aby se pot neukládal uvnitř. Delší střih chrání záda při sezení. Další modely najdete u <a href="/nepromokave-bundy/">nepromokavých bund</a> a <a href="/zimni-bundy/">zimních bund</a>.</p>'
          '<h2>Bundy a kalhoty</h2>'
          '<p>Pro pstruhové a přívlačové rybaření se hodí lehké prodyšné bundy s mnoha kapsami a skrytou kapucí. Pro kaprařinu a dlouhé sezení je lepší zateplený kabát nebo overal, který nesvazuje pohyb. '
          'Švy mají být zalepené, zipy kryté lištou a manžety nastavitelné. Kapsy ať jsou vodotěsné nebo krytí chlopní, aby se do nich nedostala voda. '
          'Pokud často stojíte u rozbouřeného jezera nebo na člunu, zvolte kalhoty s laclem a vyšším pasem. Najdete je i v sekci <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>.</p>'
          '<h2>Prsačky a brodicí kalhoty</h2>'
          '<p>Prsačky sahají po hruď, brodicí kalhoty jen po pás. Prsačky chrání víc, ale jsou těžší a při pádu do hluboké vody nebezpečnější. Pásek kolem pasu snižuje riziko, že se do nohavic nahrne voda. '
          'Materiály se dělí na neopren, který hřeje a je pružný, a prodyšné laminátové, vhodné na celé léto. Neopren se hodí do chladné vody, laminát pro aktivní přívlač a muškaření. Prsačky s neoprenovou ponožkou se kombinují s brodicí botou, prsačky s nohavicí s vysokou botou. '
          'Při velikosti vybírejte podle výšky a obvodu, nikoli jen podle kalhot, protože prsačky potřebují prostor v rozkroku a ramenou. Při brodění používejte bezpečnostní pásek, hůl a nikdy nevstupujte do vody, jejíž proud neznáte.</p>'
          '<h2>Brodicí a rybářské boty</h2>'
          '<p>Brodicí boty se nosí s prsačkami s ponožkovou částí, nohavice prsaček se obouvá do vysoké boty. Podrážka z plsti drží na kluzkých kamenech, ale ve vodě s nánosy a na blátě se hodí spíše guma s hřeby. '
          'Vyztužená špička chrání prsty před kameny a pevná pata drží kotník. Zvolte velikost s rezervou na silnější ponožky, nikoli příliš velkou, aby noha neplavala. Zimní boty s izolací zajistí teplo u kaprařiny. Rozmanitější nabídka je v kategorii <a href="/obuv-do-vody/">obuv do vody</a> a <a href="/zimni-obuv/">zimní obuv</a>.</p>'
          '<h2>Termooblek a zimní rybaření</h2>'
          '<p>Při dlouhém sezení v mrazu nestačí běžná bunda. Termooblek, který se skládá z kombinézy nebo kalhot s kabátem, obsahuje silnou izolaci. Plovoucí jsou jen obleky výslovně označené jako flotation, běžný termooblek neplave. Ani plovoucí oblek nenahrazuje záchrannou vestu. '
          'Při volbě sledujte rozsah teplot, který výrobce udává, a nezapomeňte na rukavice a čepici. Ohřívač rukou a termoska se hodí jako doplněk. Více v <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>'
          '<h2>Čepice, rukavice, brýle a doplňky</h2>'
          '<p>Nezakrytá hlava a ruce se chladí nejrychleji, proto je chraňte čepicí a rukavicemi. Čepice nebo kulich zadrží teplo a kšiltovka s polarizačními brýlemi zlepší výhled do vody. Polarizace odfiltruje odlesky a umožní vidět ryby i dno. '
          'Rukavice s odstřiženými prsty udrží cit při navazování, silnější se hodí na zimu. Šátky a nákrčníky chrání krk. Podobné kusy jsou v kategoriích <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/sportovni-rukavice/">sportovní rukavice</a> a <a href="/sportovni-bryle/">sportovní brýle</a>.</p>'
          '<h2>Výběr podle způsobu lovu</h2>'
          '<ul><li><strong>Kapr a dlouhá zasedání:</strong> zateplená bunda, kalhoty nebo overal, teplé boty a pevný kabát na noc. Vyplatí se vybrat tlumené barvy.</li>'
          '<li><strong>Přívlač a feeder:</strong> lehká nepromokavá bunda, volné rukávy a pohodlné kalhoty. Pohyb mezi stanovišti vyžaduje prodyšnost.</li>'
          '<li><strong>Muškaření:</strong> prsačky nebo brodicí kalhoty, boty s plstěnou podrážkou, krátká bunda, aby nevadila při brodění. Související výbava je v kategorii <a href="/muskareni/">muškaření</a>.</li>'
          '<li><strong>Rybaření z lodi:</strong> plovoucí oblek nebo vesta, nepromokavé kalhoty a boty s protiskluzovou podrážkou. Viz <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>.</li>'
          '<li><strong>Zima a led:</strong> termooblek, silné rukavice, kulich, boty s izolací. Doplňte <a href="/nesmeky/">nesmeky</a> pro bezpečnou chůzi po ledu.</li></ul>'
          '<h2>Velikost a střih</h2>'
          '<p>Rybářské oblečení má být volnější než sportovní, aby se do něj vešly vrstvy. Přesto velká bunda s širokými rukávy vadí při nahazování. Vybírejte podle výšky a obvodu hrudníku, zkoušejte s vrstvami, které budete nosit. '
          'Rukávy musí při natažení paží krýt zápěstí a zadní část dosahovat až k pasu. U prsaček zkontrolujte, zda se dá sednout bez napětí v rozkroku. Velikostní tabulky se liší podle značky, proto je porovnejte před nákupem.</p>'
          '<h2>Péče a oprava</h2>'
          '<p>Po výpravě bundy a kalhoty opláchněte od bláta a nechte vyschnout. Impregnaci obnovte sprejem nebo prostředkem do pračky, aby se voda dál perlila. Neopren se myje sladkou vodou a suší ve stínu, ne na slunci. '
          'Prsačky obraťte naruby a nechte vyschnout a zkontrolujte švy. Malé díry lze zalepit speciálním lepidlem a záplatou. Boty vysušte, vyndejte vložky a vyčistěte plstěnou podrážku.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Bavlněné prádlo pod nepromokavou vrstvou, které se zapotí a nahřeje.</li>'
          '<li>Příliš těsné boty bez rezervy na silné ponožky, a tedy studené nohy.</li>'
          '<li>Prsačky bez pásku při brodění v hlubší vodě.</li>'
          '<li>Nákup podle ceny bez kontroly švů, zipů a vodotěsnosti.</li>'
          '<li>Pozdní nákup zimního oblečení, když už jsou velikosti vyprodané.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete modely značek ' + B(('fox', 'Fox'), ('grundens', 'Grundéns'), ('caperlan', 'Caperlan'), ('fox-rage', 'Fox Rage'), ('delphin', 'Delphin'), ('westin', 'Westin'), ('simms', 'Simms'), ('mikado', 'Mikado'), ('vision', 'Vision'), ('kinetic', 'Kinetic'), ('trakker-products', 'Trakker'), ('savage-gear', 'Savage Gear'), ('ridgemonkey', 'RidgeMonkey'), ('dam', 'DAM')) + '. '
          'Fox, Trakker a RidgeMonkey cílí na kapraře, Simms a Grundéns na brodění a loď a Westin nebo Savage Gear na přívlač. Porovnejte materiály, švy a střihy mezi značkami.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka sleduje české obchody a u každého kusu ukazuje dostupné nabídky vedle sebe. Filtrujte podle typu a značky, ověřte velikost a vodotěsnost a porovnejte obchody. '
          'Celou výbavu doplníte kategoriemi <a href="/rybareni/">rybaření</a>, <a href="/rybarske-navijaky/">navijáky</a> a <a href="/vlasce-a-snury/">vlasce a šňůry</a>.</p>',
    faq=[
        ('Jaké oblečení na kapraření v zimě?', 'Zateplený termooblek nebo overal, teplé boty s izolací, silná čepice a rukavice. Pod to vrstvěte merino nebo syntetiku a fleece. Důležité je neprodýchat se potem, když se při obsluze hýbete.'),
        ('Čím se liší prsačky od brodicích kalhot?', 'Prsačky sahají do úrovně hrudi a chrání při hlubokém brodění. Brodicí kalhoty končí v pase a jsou lehčí a pohodlnější. Do hlubší vody patří prsačky, na mělčinu stačí kalhoty.'),
        ('Je lepší neopren, nebo prodyšný laminát?', 'Neopren hřeje a je pružný, hodí se do studené vody a pro delší stání. Prodyšný laminát je lehčí a lépe odvádí pot, takže se hodí pro aktivní pohyb. Rozhodněte se podle teploty a stylu lovu.'),
        ('Jaká podrážka je nejlepší na brodicí boty?', 'Plstěná podrážka drží na kluzkých kamenech, ale nesnáší bahnité dno ani kluzký jíl. Gumová s hřeby se hodí na bláto a kameny. Některé modely nabízejí výměnné podrážky.'),
        ('Jak poznám, že je bunda skutečně nepromokavá?', 'Podívejte se na zalepené švy, krytí zipů a údaj o vodním sloupci. Vyšší číslo značí lepší odolnost, ale důležitá je i prodyšnost. U dlouhého deště se vyplatí kapuce se zpevněným kšiltem.'),
        ('Jak obnovit impregnaci?', 'Bundu vyperte šetrným prostředkem a aplikujte sprej nebo prostředek do pračky určený pro funkční textil. Poté ji vysušte při mírném teple, které zpevní povrchovou úpravu. Postup opakujte po několika sezónách.'),
        ('Hodí se plovoucí oblek jako náhrada záchranné vesty?', 'Ne, plovoucí oblek udrží tělo na hladině a hřeje, ale záchranná vesta zajišťuje bezpečné držení hlavy nad vodou. Na lodi je nejlepší kombinace, případně vesta s dostatečnou vztlakovou silou.'),
        ('Jaké rukavice zvolit na přívlač?', 'Tenké rukavice s odstřiženými prsty umožňují cit při navazování a držení prutu. V chladu se hodí neoprenové rukavice nebo kombinace odkrývacích a zateplených. Důležitý je protiskluzový povrch dlaně.'),
        ('Na co dbát při výběru velikosti bundy?', 'Bunda má být volnější, abyste pod ni dali fleece a termoprádlo, ale rukávy nesmí překážet při nahazování. Délka záda má pokrýt pás i při sezení. Zkoušejte s vrstvami, které budete nosit.'),
        ('Jak pečovat o neoprenové prsačky?', 'Po výpravě je opláchněte sladkou vodou, otočte a nechte vyschnout ve stínu. Nesušte je na slunci ani na topení, neopren se zkřehne. Švy a záplaty kontrolujte před každou sezónou.'),
    ])

# ------------------------------------------------------------------ doplnění sekcí
NEW['kempingovy-nabytek']['guide'] += (
    '<h2>Jak nábytek naplánovat do auta a na tábořiště</h2>'
    '<p>Než začnete kupovat, představte si typický víkend. Kolik lidí bude sedět současně, kolik jídel se bude připravovat a kolik místa zbude po stanu, spacácích a chladicím boxu? '
    'Počítejte s tím, že nábytek se vozí v poslední řadě zavazadel a musí se dostat ven bez vykládání všeho ostatního. Úzké a dlouhé obaly se do kufru skládají lépe než široké, a proto se židle ve tvaru tyče vyplatí pro čtyři a více osob.</p>'
    '<p>Na tábořišti hraje roli podloží. Na trávě a písku se úzké nohy bořívají, na kamenité půdě se naopak kývají a rozdílná výška nohou nutí k podkládání. Kdo často táboří na nerovném terénu, ocení stoly s teleskopickými nohami a židle s širokými patkami. '
    'Poblíž ohně nebo grilu nenechávejte potahy z umělých vláken, protože jiskry v nich vypálí díry a tkanina se taví. Zvláštní pozornost si zaslouží děti, které na židlích rády houpají: úzký rám se může překlopit, takže mají mít pevnou sadu s nižším těžištěm.</p>'
    '<h2>Doplňky ke komfortu</h2>'
    '<p>K nábytku se hodí drobnosti, které z něj dělají použitelnější vybavení. Držák na nápoje a boční kapsa na telefon a knihu jsou praktické u křesel. Polstrovaný sedák nebo nafukovací polštář zvýší pohodlí na tvrdých židlích. '
    'Přehoz nebo deka udrží teplo při večerním sezení a stolní ubrus s klipy zabrání odletění při větru. Pokud kempujete s psem, vezměte lehkou podložku, která chrání potah před drápy. '
    'Při přípravě jídla se hodí stolek s ochranou proti horku a dvojice stohovatelných nádob, které slouží i jako úložný prostor.</p>')
NEW['boxerske-rukavice']['guide'] += (
    '<h2>Jak rukavice zkoušet a na co se dívat při nákupu</h2>'
    '<p>Nejlepší je rukavice nasadit s bandáží, zapnout je a několikrát sevřít pěst. Palec má být vedle prstů přichycený, ne volně visící. Zkontrolujte, že se rukavice nesplácne při úderu do dlaně druhé ruky a že vycpávka rovnoměrně pokrývá hřbet i spodní část. '
    'Před koupí si prohlédněte švy kolem palce, na hřbetu a u zápěstí: právě tam se rukavice rozpadá nejdřív. Pokud zkoušení není možné, spolehněte se na velikostní tabulku výrobce a na informace o délce předloktí.</p>'
    '<p>Vzhled není vedlejší. Barvu často určuje klub nebo soutěž, ve které se používá modrá a červená, ale pro trénink ji vybírejte podle toho, co se hůře špiní a snáz se čistí. Tmavé rukavice skryjí otěr, světlé rychle zešednou. '
    'Při tréninku ve skupině se hodí označit rukavice jménem, protože se snadno zaměňují a pot se přenáší na cizí vybavení.</p>'
    '<h2>Rukavice pro různé styly</h2>'
    '<p>Západní box používá rukavice s kompaktním tvarem a pevným palcem, kde se klade důraz na přesné údery. Thajský box a kickbox znají rukavice s širší vycpávkou na hřbetě, které chrání při uzavřené obraně a při bloku. '
    'Pro kondiční box a cardio tréninky stačí lehčí model, jehož zápěstí je zpevněné, ale ne příliš tuhé. U sparingu s vysokou intenzitou by se neměly používat staré a ztvrdlé rukavice, protože tvrdost vycpávky zvyšuje riziko pro hlavu soupeře. '
    'Specifickou skupinou jsou rukavice pro boj v klinči, kdy jde spíše o držení než o údery.</p>')
NEW['cyklo-pedaly']['intro'] = NEW['cyklo-pedaly']['intro'].replace(
    'Níže najdete přehled typů',
    'Dobře zvolený pár přitom vydrží mnoho sezón, zatímco špatně sladěný s botou a stylem jízdy otravuje při každém výjezdu. Níže najdete přehled typů')
NEW['cyklo-pedaly']['guide'] += (
    '<h2>Velikost plochy, úhel a vedení boty</h2>'
    '<p>U plošinových pedálů záleží na tom, jak velká je opěrná plocha. Velká noha na malé plošině se kývá a snáze sklouzne, zatímco malá noha na příliš velké plošině nemá oporu uprostřed. '
    'Chodidlo má ležet přibližně středem na ose, takže se vyplatí vyzkoušet, v jaké poloze se cítíte nejjistěji. Tenčí profil pedálu zlepšuje světlou výšku v zatáčkách a chrání před zavadením o zem. '
    'U nášlapných systémů se nastavuje vůle, tedy volný pohyb paty kolem osy. Nulová vůle přináší pevné vedení, ale může zatěžovat koleno, a proto začátečníkům vyhovuje větší hra.</p>'
    '<h2>Kdy pedály vyměnit</h2>'
    '<p>Důvodem k výměně bývá vůle v ložisku, zadrhávání otáčení, ohnutá osa nebo vylomené kolíky. U nášlapných systémů je varováním pro výměnu situace, kdy se bota neuvolňuje stejně lehce na obou stranách. '
    'Starší pedály se vyplatí vyměnit i při přechodu na jiný druh jízdy: lidé, kteří začali s plošinami a potom přešli k dlouhým výjezdům, často sáhnou po lehčím nášlapném modelu. '
    'Při výměně zkontrolujte i závit v klice. Poškozený závit může spravit servis vložkou, ale častěji se vyplatí klika nová, protože opravy jsou náročné.</p>'
    '<h2>Světlo, viditelnost a bezpečnost</h2>'
    '<p>V provozu pomáhají reflexní prvky na pedálech, které se při šlapání pohybují a jsou dobře vidět zboku i zezadu. Doplňují ostatní vybavení, například <a href="/cyklo-svetla/">světla</a> a <a href="/cyklisticke-bundy-a-vesty/">reflexní vestu</a>. '
    'Při jízdě za šera nikdy nespoléhejte jen na pedály, ale použijte alespoň přední a zadní světlo. Ke správné bezpečnosti patří i <a href="/cyklisticke-helmy/">helma</a>.</p>')
NEW['rybarske-obleceni']['guide'] += (
    '<h2>Barvy, hluk a maskování</h2>'
    '<p>Ryby v čiré vodě vnímají pohyb a silné kontrasty, ne tolik barvu bundy. Přesto se vyplatí tlumené tóny jako zelená, hnědá nebo šedá, které splynou s břehem. U lovu v mělké čisté vodě nenoste jasně červené nebo bílé svrchní vrstvy, protože při pohybu vynikají. '
    'Důležitější je tichost: šustivý materiál a cinkající zipy se nesou nad klidnou hladinou. Některé bundy mají měkčí tkaninu, která při pohybu skoro nezní. '
    'Na loď a při lovu za šera ale naopak ocení reflexní prvky, které zvyšují bezpečnost.</p>'
    '<h2>Kapsy, uchycení a praktické detaily</h2>'
    '<p>Dobrá rybářská bunda má kapsy na drobnosti, které se dají zavřít, a očko nebo kroužek na nůžky. Kapsa na hrudi poslouží pro telefon a pouzdro na háčky, zadní kapsa na vodotěsný obal. '
    'U prsaček se hodí kapsa na hrudi, nastavitelné ramínko a zesílená kolena, protože do nich se při klečení opírá nejvíc zátěže. Manžety s neoprenovou nebo elastickou úpravou zabrání vtékání vody k rukám. '
    'Kapuce má být tvarovatelná, aby kryla hlavu i s čepicí a nezasahovala do výhledu. Větrné počasí snadno sfoukne kapuci, takže ji lze stáhnout šňůrkou.</p>'
    '<h2>Bezpečnost u vody</h2>'
    '<p>Mokré oblečení je těžké a při pádu do vody vás táhne ke dnu. Proto je u lodi a v rychlé řece rozumné nosit záchrannou vestu a nenavlékat těžké zimní boty bez možnosti rychlého svlečení. '
    'Opatrnost vyžaduje i led: bezpečnost se řídí tloušťkou, kterou nelze určit pohledem, a rozhodně nikdy nechoďte na led sami. Pokud se noříte do vody po pás, volte pásek na prsačkách. Základní pomůckou je i lékárnička, kterou najdete v kategorii <a href="/prvni-pomoc/">první pomoc</a>.</p>')

NEW['cyklo-pedaly']['guide'] += (
    '<h2>Pedály a velikost chodidla</h2>'
    '<p>Pro větší chodidla, třeba od velikosti obuvi čtyřicet pět výše, se vyplatí širší plocha, aby se noha neotáčela kolem osy a tlak se rozložil. '
    'Děti a lidé s menší nohou naopak ocení kompaktní plošinu, která nevadí v zatáčkách. Pokud sdílíte kolo v rodině, vyberte univerzální plošinové pedály s menšími kolíky, na kterých se dá jezdit v běžné obuvi.</p>')
