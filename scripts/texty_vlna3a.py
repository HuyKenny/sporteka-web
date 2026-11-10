"""sporteka.cz — texts of wave 2, part A: camping and hiking (3. 11. 2026). Merged into src/texts/kategorie.json by texty-export.py.
Same rules as texty_vlna1a.py: general true facts, no prices, no superlatives, no invented statistics."""
from texty_vlna1a import T

NEW = {}

NEW['kemping'] = dict(short=True,
    title='Kemping – vybavení a porovnání cen v e-shopech | Sporteka',
    desc='Kempingové vybavení na jednom místě: stany, spacáky, karimatky, vaření i nábytek. Porovnejte ceny a dostupnost v českých outdoorových obchodech.',
    intro='<p><strong>Kempingové vybavení</strong> se skládá z několika věcí, které na sebe navazují: střecha nad hlavou, spaní, vaření a sezení. Základ tvoří <a href="/stany/">stan</a>, <a href="/spaci-pytle/">spacák</a> a '
          '<a href="/karimatky-a-matrace/">karimatka nebo matrace</a>. Teprve potom se vyplatí řešit <a href="/vareni-v-prirode/">vaření</a>, <a href="/kempingovy-nabytek/">nábytek</a>, <a href="/chladici-boxy/">chladicí boxy</a> a <a href="/hamaky/">hamaky</a>.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného zboží, takže uvidíte cenu, slevu i skladové velikosti. Výběr zúžíte podle značky, ceny a parametrů. Pokud jedete pěšky, přečtěte si nejdřív sekci '
          '<a href="/outdoor/">outdoor a turistika</a>, protože váha tam rozhoduje víc než pohodlí.</p>',
    guide='<h2>Jak si sestavit kempingovou výbavu</h2>'
          '<p>Výbava se liší podle toho, jak se na místo dostanete. Kdo přijede autem, může vzít velký rodinný stan, skládací židle a chladicí box. Kdo půjde několik dní pěšky, počítá každých sto gramů. '
          'Před nákupem proto odpovězte na tři otázky: <strong>kolik vás je</strong>, <strong>jak se budete přepravovat</strong> a <strong>v jakém období pojedete</strong>.</p>'
          '<h3>Základní trojice: stan, spacák, podložka</h3>'
          '<p>Na těchto třech věcech nešetřete. Spacák a podložka musí vydržet nejchladnější noc, kterou čekáte, a stan musí odolat dešti. Teprve pak má smysl dokupovat pohodlí.</p>'
          '<ul><li><strong>Stan:</strong> kapacita, vodní sloupec a počet vchodů najdete u <a href="/stany/">stanů</a>.</li>'
          '<li><strong>Spacák:</strong> komfortní teplota rozhoduje, ne extrémní, viz <a href="/spaci-pytle/">spací pytle</a>.</li>'
          '<li><strong>Podložka:</strong> izoluje od země, bez ní ztratíte teplo i v létě. Typy popisují <a href="/karimatky-a-matrace/">karimatky a matrace</a>.</li></ul>'
          '<h3>Vaření a jídlo</h3>'
          '<p>Plynový vařič je nejjednodušší a nejrychlejší. Do skupiny se hodí dvouplotýnkový kempingový vařič na kartuši, na pěší túry stačí malý hořák. Nezapomeňte na nádobí, hrnek, příbor a zapalovač. '
          'Kompletní nabídku najdete v kategorii <a href="/vareni-v-prirode/">vaření v přírodě</a> a <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>'
          '<h3>Sezení, stoly a chlazení</h3>'
          '<p>Skládací židle a stolek udělají z tábořiště místo, kde se dobře žije. U <a href="/kempingovy-nabytek/">kempingového nábytku</a> sledujte nosnost, rozměry po složení a hmotnost. '
          'Na delší pobyty přijde vhod <a href="/chladici-boxy/">chladicí box</a>, který udrží potraviny chladné i bez elektřiny.</p>'
          '<h3>Doplňky, které se hodí</h3>'
          '<ul><li>čelovka nebo svítilna, viz <a href="/celovky-a-svitilny/">čelovky a svítilny</a>,</li>'
          '<li>láhev nebo termoska na vodu, viz <a href="/lahve-a-termosky/">lahve a termosky</a>,</li>'
          '<li>sada první pomoci a repelent, viz <a href="/prvni-pomoc/">první pomoc</a>,</li>'
          '<li><a href="/hamaky/">hamak</a> na odpočinek mezi stromy.</li></ul>'
          '<h3>Kontrolní seznam před odjezdem</h3>'
          '<p>Vyzkoušejte stan doma na zahradě. Zjistíte, jestli nechybí tyčky nebo kolíky, a v kempu nebudete řešit stavbu za tmy. Zkontrolujte, že spacák nemá vlhké výplně a že plynová kartuše je plná.</p>',
    faq=[('Co potřebuji na první kempování?', 'Stan, spacák, podložku, čelovku, vařič s nádobím a základní lékárničku. Na víkend s autem stačí tohle a nějaké sezení, na túru zvolte hlavně lehké věci.'),
         ('Jak vybrat stan do kempu?', 'Podle počtu lidí přidejte jedno místo navíc pro věci. U přívalových dešťů sledujte vodní sloupec nejméně 2000 mm u podlážky a 1500 mm u pláště.'),
         ('Jaký spacák na léto a jaký na jaro?', 'Na léto stačí komfortní teplota kolem 10 °C, na jaro a podzim volte komfortní teplotu 0 až 5 °C. Vždy se řiďte komfortní, ne extrémní hodnotou.'),
         ('Kolik stojí základní kempingová výbava?', 'Cena se liší podle značky a kvality. Aktuální ceny stanů, spacáků a podložek vedle sebe uvidíte na Sportece u každého zboží.'),
         ('Jak chránit jídlo před teplem v kempu?', 'Pomůže chladicí box s ledovými vložkami, který stojí ve stínu. Pro několikadenní pobyt volte box s izolací vyšší tloušťky a zavíráním na těsnění.'),
         ('Jaký vařič do kempu?', 'Pro skupinu dvouplotýnkový vařič na plynovou kartuši, na pěší výlet lehký hořák na šroubovací kartuši. Vždy vařte venku nebo v dobře větraném přístřešku.')],
)

NEW['stany'] = dict(short=True,
    title='Stany – turistické, rodinné i pop-up | Porovnání cen',
    desc='Stany pro 1 až 8 osob: turistické, rodinné, expediční i pop-up. Porovnejte ceny, vodní sloupec a dostupnost v českých outdoorových obchodech.',
    intro='<p><strong>Stan</strong> je nejdůležitější část kempingové výbavy, protože musí odolat dešti, větru i celé noci vedle vás. Liší se kapacitou, váhou, vodním sloupcem a konstrukcí. '
          '<a href="/turisticke-stany/">Turistické stany</a> jsou lehké a malé po složení, <a href="/rodinne-stany/">rodinné stany</a> mají velkou předsíň a výšku na stání, '
          '<a href="/pop-up-a-plazove-stany/">pop-up stany</a> se rozloží za pár vteřin a <a href="/expedicni-stany/">expediční</a> vydrží i hory v zimě.</p>'
          '<p>Na Sportece porovnáte ceny stanů v českých obchodech a vyberete podle počtu osob, značky a hmotnosti. Vedle stanů najdete i <a href="/stanove-doplnky/">stanové doplňky</a> pro vybranou kategorii.</p>',
    guide='<h2>Jak vybrat stan</h2>'
          '<p>Nejlepší stan je ten, který odpovídá tomu, jak ho budete používat. Dvoudenní víkend u řeky a týdenní trek se stanem na zádech jsou dvě různé situace. Dívejte se na pět parametrů.</p>'
          '<h3>Kapacita</h3>'
          '<p>Údaj „3 osoby“ znamená, že se vejdete těsně vedle sebe bez zavazadel. Pokud chcete mít pohodlí a místo na batohy, vyberte stan o jedno místo větší. U dvojice to bývá třímístný stan.</p>'
          '<h3>Vodní sloupec</h3>'
          '<p>Vodní sloupec udává odolnost látky vůči tlaku vody. Pro běžné kempování stačí 2000 mm u pláště, u podlážky bývá 3000 mm i víc. Do hor a na vítr volte vyšší hodnoty a dobře přelepené švy.</p>'
          + T(['Použití', 'Doporučený vodní sloupec pláště'], [['Letní víkend', '1500–2000 mm'], ['Třísezónní kempování', '2000–3000 mm'], ['Hory, deštivé oblasti', '3000 mm a více']]) +
          '<h3>Konstrukce a stavba</h3>'
          '<ul><li><strong>Tunelové stany:</strong> prostorné vzhledem k váze, vyžadují dobré ukotvení.</li>'
          '<li><strong>Kupolové stany:</strong> samonosné, stabilní ve větru, vhodné na tvrdou zem.</li>'
          '<li><strong>Pop-up stany:</strong> postaví se samy, hodí se na pláž a festival.</li>'
          '<li><strong>Tipi a lavvu:</strong> jednoduché, prostorné, s ohništěm uprostřed, viz <a href="/tipi-a-lavvu/">tipi a lavvu</a>.</li></ul>'
          '<h3>Hmotnost a rozměry po složení</h3>'
          '<p>Na pěší túru počítejte s váhou do 2–3 kg na dvě osoby. U auta váhu neřešíte, vyberete místo a výšku. Zkontrolujte, že se stan vejde do kufru nebo batohu.</p>'
          '<h3>Předsíň a větrání</h3>'
          '<p>Předsíň uloží boty a batohy mimo spací část. Větrací okénka a sítě proti hmyzu snižují kondenzaci, která v zavřeném stanu vzniká z dechu.</p>'
          '<h3>Péče o stan</h3>'
          '<p>Stan nikdy neskladujte mokrý, jinak se objeví plíseň. Doma ho rozložte, vysušte a ukládejte volně. Poškozená tyčka nebo díra v plachtě se dá opravit sadou, kterou najdete v <a href="/stanove-doplnky/">stanových doplňcích</a>. Kolíky doplňují <a href="/stanove-kolky/">stanové kolíky</a>.</p>'
          '<p>Pokud kempujete celé léto v dešti, pořiďte pod stan ochrannou podložku a nad ním tarp. Obojí stan chrání a prodlužuje jeho životnost.</p>',
    faq=[('Jaký stan pro dva lidi?', 'Pro pohodlí vyberte třímístný stan. Dvoumístný se vejde na túru, ale zavazadla se budou nosit do předsíně.'),
         ('Jaký vodní sloupec musí mít stan?', 'Pro běžné kempování stačí 2000 mm na plášti a 3000 mm na podlážce. Do hor a do deště volte víc.'),
         ('Jaký stan do hor?', 'Kupolový nebo tunelový třísezónní stan se dvěma tyčkami, pevným pláštěm a vyšším vodním sloupcem. Na zimu expediční model.'),
         ('Je pop-up stan dobrý na víkend?', 'Pro krátké pobyty za dobrého počasí ano, postavíte ho za pár vteřin. Na silný vítr a déšť nejsou ideální.'),
         ('Jak stan správně uskladnit?', 'Vždy suchý, volně složený a mimo přímé slunce. Mokrý stan v pytli za pár dní zplesniví.'),
         ('Jak velký stan pro rodinu?', 'Počítejte s kapacitou o jedno až dvě místa vyšší, než je počet lidí, a s předsíní. Rodinné stany mají výšku na stání a oddělené ložnice.')],
)

NEW['spaci-pytle'] = dict(short=True,
    title='Spací pytle – letní, zimní, péřové a dětské | Sporteka',
    desc='Spací pytle pro kemping a trek: letní, třísezónní, zimní, péřové i dětské. Porovnejte ceny a komfortní teploty v českých outdoorových obchodech.',
    intro='<p><strong>Spací pytel</strong> rozhoduje o tom, jestli budete spát, nebo jen přežívat noc. Při výběru se řiďte komfortní teplotou, tedy hodnotou, při které se vám bude pohodlně spát. '
          'Extrémní teplota udává limit, při kterém ještě přežijete. Rozlišujeme <strong>péřové</strong> spacáky, které jsou lehké a dobře se stlačí, a <strong>syntetické</strong>, které snesou vlhko a jsou levnější.</p>'
          '<p>Pro děti vybírejte z <a href="/detske-spacaky/">dětských spacáků</a>, které rostou s dítětem. Na Sportece porovnáte ceny z českých obchodů a vedle spacáku najdete i '
          '<a href="/karimatky-a-matrace/">karimatky a matrace</a>, bez kterých teplo od země uniká.</p>',
    guide='<h2>Jak vybrat spací pytel</h2>'
          '<p>Správný spacák se vybírá podle teploty, hmotnosti a výplně. Přesvědčte se, že údaje vycházejí z normy EN 13537, která výrobci sjednocuje.</p>'
          '<h3>Teplotní údaje</h3>'
          '<ul><li><strong>Komfortní teplota:</strong> při ní se vyspí průměrná žena bez prochladnutí.</li>'
          '<li><strong>Limitní teplota:</strong> při ní se vyspí průměrný muž v klubíčku.</li>'
          '<li><strong>Extrémní teplota:</strong> hranice přežití, spát se v ní nedá.</li></ul>'
          + T(['Sezóna', 'Komfortní teplota'], [['Léto', '10 °C a více'], ['Třísezónní', '0 až 5 °C'], ['Zima', '−5 °C a méně']]) +
          '<h3>Péří, nebo syntetika</h3>'
          '<p>Péřová výplň je při stejné teplotě lehčí a po složení menší. Nevýhodou je vyšší cena a ztráta izolace v mokru. Syntetika izoluje i vlhká, dobře schne a snese praní, ale váží víc.</p>'
          '<h3>Tvar a velikost</h3>'
          '<ul><li><strong>Mumie:</strong> přiléhá k tělu, nejlépe udrží teplo, hodí se na trek.</li>'
          '<li><strong>Dekový:</strong> prostorný a rozepínací, vhodný do auta a do kempu.</li>'
          '<li><strong>Dětský:</strong> menší, často s prodloužením pro rostoucí dítě.</li></ul>'
          '<p>Zkontrolujte délku. Spacák, který je příliš dlouhý, vyplní studený vzduch, příliš krátký tlačí a tlumí izolaci.</p>'
          '<h3>Péče a skladování</h3>'
          '<p>Spacák nenechávejte stlačený v sáčku. Skladujte ho volně, ve větší bavlněné tašce, aby se výplň nesesedla. Pere se jen podle návodu, péřové s přípravkem určeným na péří.</p>'
          '<p>K nočnímu komfortu přispívá i vložka, která chrání od potu a prodlužuje dobu mezi praním, a čepice na hlavu, protože se tudy ztrácí hodně tepla.</p>',
    faq=[('Jaký spacák na léto?', 'Dekový nebo lehký mumie spacák s komfortní teplotou kolem 10 °C. Na chladnější noci vezměte vložku.'),
         ('Co je komfortní teplota spacáku?', 'Je to teplota, při které se v něm vyspí průměrná žena bez prochladnutí. Pro běžný výběr se řiďte právě touto hodnotou.'),
         ('Péřový, nebo syntetický spacák?', 'Péřový je lehčí a menší po sbalení, syntetický lépe snáší vlhko a bývá levnější. Do mokrého klimatu a pro děti je lepší syntetika.'),
         ('Jak často prát spacák?', 'Jen když je potřeba, obvykle jednou za sezónu nebo po výrazném znečištění. Dodržujte pokyny výrobce.'),
         ('Jaký spacák pro dítě?', 'Dětský spacák s výplní podle teploty, ideálně s možností prodloužení. Vybírejte podle výšky dítěte.'),
         ('Jak skladovat spací pytel?', 'Volně, v prodyšné velké tašce nebo zavěšený. V malém sáčku se výplň trvale stlačí a ztratí izolaci.')],
)

NEW['karimatky-a-matrace'] = dict(short=True,
    title='Karimatky a matrace – samonafukovací i nafukovací | Sporteka',
    desc='Karimatky a matrace do stanu: pěnové, samonafukovací i nafukovací s R-hodnotou. Porovnejte ceny a rozměry v českých outdoorových obchodech.',
    intro='<p><strong>Karimatka nebo matrace</strong> izoluje tělo od studené země. Bez ní uniká teplo i v létě, i když máte kvalitní spacák. Rozhodují tři věci: <strong>R-hodnota</strong> (izolace), hmotnost a rozměr po složení. '
          'Pěnové karimatky jsou levné a nezničitelné, samonafukovací jsou pohodlnější a nafukovací nejlehčí na přenášení.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a vyberete podle tloušťky, značky a typu. Doplňte je o <a href="/spaci-pytle/">spací pytel</a> a <a href="/stany/">stan</a> a máte základ kempingové výbavy, '
          'kterou popisuje kategorie <a href="/kemping/">kemping</a>.</p>',
    guide='<h2>Jak vybrat karimatku nebo matraci</h2>'
          '<p>Při výběru rozhoduje, kde budete spát a kolik toho unesete. Karimatka do stanu na louce a matrace do zimních hor jsou dvě rozdílné věci.</p>'
          '<h3>R-hodnota</h3>'
          '<p>R-hodnota udává odolnost proti úniku tepla. Čím vyšší, tím víc izoluje. Pro teplé noci stačí hodnoty kolem 2, na jaro a podzim 3 až 4, na zimu 5 a víc.</p>'
          + T(['Období', 'Doporučená R-hodnota'], [['Léto', '1–3'], ['Jaro a podzim', '3–4'], ['Zima a sníh', '5 a více']]) +
          '<h3>Typy</h3>'
          '<ul><li><strong>Pěnová karimatka:</strong> levná, lehká a odolná, ale objemná a méně pohodlná.</li>'
          '<li><strong>Samonafukovací matrace:</strong> kombinuje pěnu a vzduch, pohodlná a střední váha.</li>'
          '<li><strong>Nafukovací matrace:</strong> nejmenší po složení a nejlehčí, vyžaduje pumpu nebo sílu plic.</li></ul>'
          '<h3>Rozměry</h3>'
          '<p>Standardní délka je kolem 180 cm, širší modely mají 65 cm a víc. Pokud se v noci hodně otáčíte, vezměte širší. U dětí stačí kratší verze.</p>'
          '<h3>Hluk a komfort</h3>'
          '<p>Nafukovací matrace někdy hlasitě šustí a můžou klouzat po stanové podlážce. Neklouzavý povrch a tichý materiál oceníte hlavně ve dvou. Zkontrolujte, jestli má matrace ventil, který se dá zavřít jedním tahem.</p>'
          '<h3>Oprava a údržba</h3>'
          '<p>K nafukovacím modelům patří záplata na propíchnutí. Matraci skladujte rozbalenou nebo volně srolovanou, ne stlačenou. Před použitím ji očistěte od kamínků a trnů, které poškozují povrch.</p>'
          '<p>Další spaní popisuje kategorie <a href="/hamaky/">hamaky</a>, které jsou alternativou pro lesní tábory a lehké výpravy.</p>',
    faq=[('Co je R-hodnota karimatky?', 'Je to míra izolace od země. Čím vyšší, tím méně tepla uniká. Na léto stačí 2, na zimu 5 a víc.'),
         ('Pěnová karimatka, nebo nafukovací matrace?', 'Pěnová je levnější a odolná, nafukovací pohodlnější a menší. Na trek volte nafukovací, do auta cokoliv.'),
         ('Jak velká karimatka je správná?', 'Standardně kolem 180 cm na délku. Pokud se hodně otáčíte, zvolte širší verzi.'),
         ('Jak opravit propíchnutou matraci?', 'Najděte únik ponořením do vody, osušte a přelepte záplatou. Pro každý model výrobce přikládá opravnou sadu.'),
         ('Hodí se samonafukovací matrace do zimy?', 'Ano, pokud má vysokou R-hodnotu, tedy 5 a víc. Pod ni případně přidejte pěnovou podložku.'),
         ('Jak karimatku skladovat?', 'Volně rozloženou nebo srolovanou, ne trvale stlačenou. Nafukovací matrace ukládejte s otevřeným ventilem.')],
)

NEW['turisticke-batohy'] = dict(short=True,
    title='Turistické batohy – objem, velikost zad, ceny | Sporteka',
    desc='Turistické batohy 20 až 80 litrů: na výlet, trek i vícedenní túry. Porovnejte ceny, objem a velikosti zad v českých outdoorových obchodech.',
    intro='<p><strong>Turistický batoh</strong> má pohodlně sedět na zádech, rozložit váhu na boky a mít správný objem. Pro jednodenní výlet stačí 20 až 30 litrů, na víkend 40 až 50, na trek se spaním venku 55 a víc. '
          'Dámské modely mají kratší záda a užší ramenní popruhy.</p>'
          '<p>Na Sportece porovnáte ceny batohů z českých obchodů a vyberete podle objemu, značky a ceny. Kromě turistických batohů najdete <a href="/mestske-batohy/">městské</a> a <a href="/skolni-batohy/">školní</a>. '
          'K túře se hodí i <a href="/trekove-hole/">trekové hole</a> a <a href="/trekova-obuv/">trekové boty</a>.</p>',
    guide='<h2>Jak vybrat turistický batoh</h2>'
          '<p>Nejdůležitější je, aby batoh seděl. I drahý batoh nepohodlně tlačí, když nemá správnou velikost zad. Vyberte tedy nejdřív délku zad a teprve potom objem.</p>'
          '<h3>Objem podle délky túry</h3>'
          + T(['Typ túry', 'Objem batohu'], [['Denní výlet', '20–30 l'], ['Víkend se spaním v chatě', '30–45 l'], ['Víkend ve stanu', '45–60 l'], ['Týdenní trek', '60–80 l']]) +
          '<h3>Velikost zad</h3>'
          '<p>Velikost zad se měří od sedmého krčního obratle k hřebenům pánevních kostí. Většina značek nabízí tři velikosti, S, M a L. Vybírejte podle naměřené délky, ne podle výšky postavy.</p>'
          '<h3>Nosný systém</h3>'
          '<ul><li><strong>Bederní pás:</strong> přenáší až 80 % váhy na boky, měl by být vypolstrovaný.</li>'
          '<li><strong>Zádový systém:</strong> vzdušný vyvětrává záda, těsný drží zátěž blíž k tělu.</li>'
          '<li><strong>Hrudní popruh:</strong> stabilizuje ramena při chůzi.</li></ul>'
          '<h3>Funkce a kapsy</h3>'
          '<p>Praktické jsou boční kapsy na láhev, upevnění na hole, dešťová pláštěnka a přístup do hlavní komory zespodu. Další funkce se hodí podle způsobu použití.</p>'
          '<h3>Jak batoh sbalit</h3>'
          '<p>Nejtěžší věci patří blízko zad a do výšky lopatek, lehké dolů, věci k rychlému přístupu nahoru nebo do kapes. Takhle se batoh houpe méně a nenamáhá záda.</p>'
          '<p>Před koupí batoh zatižte, ideálně na 8 až 10 kg, a vyzkoušejte popruhy. Pokud některé část tlačí nebo se ramena sklouzávají, zkuste jinou velikost.</p>',
    faq=[('Jaký batoh na jednodenní výlet?', 'Obvykle 20 až 30 litrů, s kapsou na láhev a nepromokavým potahem. Pro děti kratší záda a menší objem.'),
         ('Jak změřit velikost zad batohu?', 'Od sedmého krčního obratle k hřebenům pánevních kostí. Hodnotu porovnejte s tabulkou výrobce.'),
         ('Kolik litrů na týdenní trek?', 'Zhruba 60 až 80 litrů, podle spacího vybavení a ročního období. Lehké pojetí zvládne i 50 až 55 litrů.'),
         ('Čím se liší dámský batoh od pánského?', 'Má kratší záda a užší, zakřivené ramenní popruhy. Bederní pás je tvarovaný na širší boky.'),
         ('Jak batoh vyčistit?', 'Ručně vlažnou vodou a jemným mýdlem, bez pračky a sušičky. Nechte ho vyschnout na vzduchu mimo slunce.'),
         ('Je potřeba pláštěnka na batoh?', 'Ano, pokud batoh sám není nepromokavý. Většina modelů má integrovanou pláštěnku ve spodní kapse.')],
)

NEW['outdoor'] = dict(short=True,
    title='Outdoor a turistika – vybavení | Porovnání cen',
    desc='Outdoor a turistika: batohy, trekové hole, čelovky, láhve, lezecké vybavení a doplňky. Porovnejte ceny a dostupnost v českých outdoorových obchodech.',
    intro='<p><strong>Outdoorové vybavení</strong> pokrývá všechno od jednodenního výletu po vícedenní trek v horách. Základem je <a href="/turisticke-batohy/">batoh</a>, <a href="/trekova-obuv/">boty</a>, '
          '<a href="/outdoorove-kalhoty/">kalhoty</a> a <a href="/trekove-hole/">hole</a>. Důležitá je také <a href="/celovky-a-svitilny/">čelovka</a>, <a href="/lahve-a-termosky/">láhev</a> a první pomoc.</p>'
          '<p>Na Sportece najdete outdoorové zboží z českých obchodů na jednom místě. Ceny vidíte vedle sebe a výběr zúžíte podle značky, ceny a parametrů. Na přespání venku se podívejte do kategorie '
          '<a href="/kemping/">kemping</a>.</p>',
    guide='<h2>Jak se vybavit na turistiku</h2>'
          '<p>Na túru nepotřebujete všechno nejdražší, ale pár věcí nešetřete. Dobrá obuv, vrstvené oblečení a rozumný batoh udělají větší rozdíl než jakýkoli doplněk.</p>'
          '<h3>Oblečení po vrstvách</h3>'
          '<ul><li><strong>Spodní vrstva:</strong> odvádí pot, ideálně funkční nebo merino, viz <a href="/merino-tricka/">merino trička</a>.</li>'
          '<li><strong>Střední vrstva:</strong> izoluje, například <a href="/funkcni-mikiny/">funkční mikina</a> nebo fleece.</li>'
          '<li><strong>Vnější vrstva:</strong> chrání před větrem a deštěm, bunda s membránou.</li></ul>'
          '<h3>Obuv</h3>'
          '<p>Nízké boty stačí na pohodlné cesty, vysoké drží kotník na kamenitých stezkách. Přehled obou typů popisují <a href="/nizke-trekove-boty/">nízké trekové boty</a> a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>. '
          'Boty kupujte odpoledne, kdy je noha mírně oteklá, a vždy s ponožkami, ve kterých půjdete.</p>'
          '<h3>Batoh a hole</h3>'
          '<p>Správný objem batohu odpovídá délce túry. Trekové hole šetří kolena v klesání a pomáhají při stoupání, vyberte nastavitelné a nepříliš těžké. Další informace najdete u <a href="/turisticke-batohy/">turistických batohů</a>.</p>'
          '<h3>Světlo, voda, první pomoc</h3>'
          '<p>I na denní výlet patří do batohu čelovka, láhev nebo termoska a základní lékárnička. Při pobytu v lese pomáhá <a href="/hygiena-a-repelenty/">repelent</a> proti klíšťatům a komárům.</p>'
          '<h3>Orientace a bezpečnost</h3>'
          '<p>Mapa, kompas a nabitý telefon s powerbankou patří do výbavy, i když se spoléháte na navigaci. Při dlouhých trasách informujte někoho blízkého o plánu. Technické doplňky najdete v kategoriích '
          '<a href="/powerbanky-a-nabijeni/">powerbanky</a> a <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>.</p>'
          '<h3>Kdy kupovat</h3>'
          '<p>Sezónní zboží bývá nejdražší na začátku sezóny. Za výrazně lepší ceny se dá koupit na konci léta nebo na jaře předchozí sezóny. Sporteka ukazuje vývoj nabídek, takže dobrou cenu poznáte.</p>',
    faq=[('Co vzít na jednodenní túru?', 'Batoh, vodu, svačinu, čelovku, lékárničku, pláštěnku a mapu. Oblečte se po vrstvách a zvolte pevnou obuv.'),
         ('Jak se oblékat na hory?', 'Po vrstvách: spodní odvádí pot, střední izoluje, vnější chrání před větrem a deštěm. Bavlna na túru není vhodná.'),
         ('Potřebuji trekové hole?', 'Nejsou povinné, ale šetří klouby v klesání a pomáhají při dlouhých túrách. Vybírejte nastavitelné a lehké.'),
         ('Jaké boty na turistiku?', 'Na běžné stezky stačí nízké trekové boty, na kamenitý a náročnější terén vyberte vysoké s kotníkovou oporou.'),
         ('Kdy je nejlepší doba na nákup outdoorového vybavení?', 'Ceny bývají nižší na konci sezóny, tedy na podzim pro letní zboží a na jaře pro zimní. Sporteka ukazuje aktuální slevy.'),
         ('Co patří do lékárničky na túru?', 'Náplasti, obvaz, dezinfekce, izolační fólie, léky proti bolesti a osobní léky. Sady najdete v kategorii první pomoc.')],
)
