"""sporteka.cz — wave 10c (4. 11. 2026): kayaks, SUP and the next big categories without a text. General true facts only, no prices.
Brands from the live catalogue; short entries (intro >= 50, guide >= 220 words)."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['kajaky-a-cluny'] = dict(short=True,
    title='Kajaky, kánoe a čluny – nafukovací i pevné | Sporteka',
    desc='Kajaky, kánoe, nafukovací čluny a pádla. Porovnejte ceny z českých obchodů a vyberte plavidlo podle vody, posádky a nosnosti.',
    intro='<p><strong>Kajak, kánoe nebo nafukovací člun</strong> se liší tím, kde a s kým je budete používat. Na klidnou řeku nebo rybník stačí stabilní nafukovací model, na delší túry vyhovuje pevnější kajak s dobrým sklouznutím.</p>'
          '<p>Ceny z různých českých obchodů vidíte pohromadě. Při výběru sledujte délku, nosnost, hmotnost a to, zda je v ceně pádlo a pumpa.</p>',
    guide='<h2>Jak vybrat kajak, kánoi nebo člun</h2>'
          '<p>Začněte tím, kolik lidí poveze a kde pojedete. Jednomístný kajak je rychlejší a lépe ovladatelný, dvoumístný se hodí pro pár nebo rodinu s dítětem. Kánoe nabízí víc místa na vybavení a je stabilní, ale hůře drží směr při větru.</p>'
          '<h3>Typy plavidel</h3>'
          + T(['Typ', 'Pro koho'], [['Nafukovací kajak', 'turistika na klidné vodě, snadná doprava a skladování'], ['Pevný kajak', 'rychlejší jízda, delší túry, trvalejší materiál'], ['Skládací kajak', 'kompromis mezi přepravou a jízdními vlastnostmi'], ['Kánoe', 'rodina, přeprava vybavení, vodácké túry'], ['Nafukovací člun', 'rybaření, rekreace, menší motor podle povolení výrobce']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Nosnost:</strong> počítejte posádku i vybavení a nechte rezervu.</li>'
          '<li><strong>Materiál:</strong> vícevrstvý PVC odolává škrábancům lépe než tenká fólie.</li>'
          '<li><strong>Ventily a komory:</strong> více komor zvyšuje bezpečnost při proražení.</li>'
          '<li><strong>Doplňky:</strong> pádlo, sedačky, pumpa a brašna na převoz.</li></ul>'
          '<h3>Bezpečnost na vodě</h3>'
          '<p>Plovací vestu mějte oblečenou vždy, ne jen vzít s sebou. Po každém výletu plavidlo opláchněte a před uskladněním úplně vysušte, jinak se objeví plíseň. Výběr vest najdete v kategorii <a href="/plovaci-vesty/">plovací vesty</a>. Pro stojící jízdu se hodí <a href="/paddleboardy/">paddleboardy</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš malý člun pro posádku a vybavení.</li><li>Nafouknutí na maximum na slunci, kdy se vzduch dále rozpíná.</li><li>Skladování vlhkého plavidla ve vaku.</li></ul>',
    faq=[('Jaký kajak je nejlepší pro začátečníka?', 'Stabilní nafukovací nebo širší pevný kajak s dobrým sezením. Úzké závodní modely jsou náročnější na rovnováhu.'),
         ('Vydrží nafukovací kajak delší túry?', 'Kvalitní vícevrstvý model ano. U levných fólií hrozí proražení o kameny, proto zvolte odolnější materiál.'),
         ('Jaká je rozdíl mezi kajakem a kánoí?', 'Kajak se pádluje dvoulistým pádlem vsedě s nohama dopředu, kánoe jednolistým vkleče nebo na lavičce.'),
         ('Potřebuji k člunu motor?', 'Jen u větších a pevnějších modelů. Maximální výkon motoru určuje výrobce.'),
         ('Jak kajak skladovat?', 'Čistý a suchý, volně a mimo přímé slunce. Nafukovací složte a vysypte z něj písek.'),
         ('Co všechno potřebuji kromě kajaku?', 'Pádlo, plovací vestu, vodotěsný vak a pumpu u nafukovacích modelů.')],
)

NEW['paddleboardy'] = dict(short=True,
    title='Paddleboardy a SUP – nafukovací sety | Sporteka',
    desc='Paddleboardy, nafukovací SUP sety, pádla a doplňky. Porovnejte nabídku českých obchodů a vyberte prkno podle váhy a vody.',
    intro='<p><strong>Paddleboard (SUP)</strong> je prkno, na kterém se jezdí vstoje s pádlem. Nafukovací modely se vejdou do batohu a dnes převažují, pevné se hodí pro sportovnější jízdu a zkušenější paddlery.</p>'
          '<p>Na Sportece najdete paddleboardy a sety s pádlem, pumpou a vakem. Vybírejte podle délky, šířky, tloušťky a nosnosti.</p>',
    guide='<h2>Jak vybrat paddleboard</h2>'
          '<p>Nosnost musí odpovídat vaší váze plus vybavení. Širší prkno je stabilnější a hodí se pro začátek, užší je rychlejší. Tloušťka kolem 15 cm u nafukovacích modelů zajišťuje tuhost.</p>'
          '<h3>Typy prken</h3>'
          + T(['Typ', 'Použití'], [['Allround', 'univerzální, rekreace, začátečníci'], ['Touring', 'delší túry, lepší sklouznutí'], ['Yoga a fitness', 'široká stabilní plocha'], ['Závodní', 'úzké a dlouhé, pro zkušené'], ['Dětské', 'kratší a lehčí']]) +
          '<h3>Co obsahuje set</h3>'
          '<ul><li>Prkno, pádlo a ploutev.</li><li>Pumpa s manometrem a vak na převoz.</li><li>Leash, tedy lanko, které vás drží u prkna.</li></ul>'
          '<h3>Pádlo a péče</h3>'
          '<p>Pádlo nastavte tak, aby přesahovalo vaši výšku zhruba o dlaň až o 20 cm. Nafukujte na tlak doporučený výrobcem. Po použití prkno opláchněte a pověste vysušit, aby se zabránilo plísni.</p>'
          '<h3>Bezpečnost</h3>'
          '<p>Při jízdě mějte leash, v chladné vodě neopren a na otevřené vodě plovací vestu. Podle počasí a větru volte zátoku nebo klidnou řeku. Pro vybavení viz <a href="/neopreny/">neopreny</a> a <a href="/plovaci-vesty/">plovací vesty</a>. Alternativa je <a href="/kajaky-a-cluny/">kajak</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš malé prkno vzhledem k váze.</li><li>Nafouknutí pod doporučený tlak, kdy se prkno prohýbá.</li><li>Jízda bez leashe na řece s proudem.</li></ul>',
    faq=[('Jak velký paddleboard potřebuji?', 'Podle váhy a zkušeností. Začátečník ocení šířku kolem 80 cm a delší prkno pro stabilitu.'),
         ('Je nafukovací SUP stejně dobrý jako pevný?', 'Pro rekreaci ano, je odolný a dá se snadno převážet. Pevný prkno je tužší a rychlejší.'),
         ('Kolik vzduchu do paddleboardu?', 'Podle štítku od výrobce, obvykle v řádu jednotek barů. Měřte manometrem.'),
         ('Jak si vybrat pádlo?', 'Podle výšky a stylu jízdy. Lehčí karbonové je pohodlnější na delší túry.'),
         ('Mohou jezdit i děti?', 'Ano na menších prknech a s dohledem a vestou. Na stojící jízdě je důležitá stabilita.'),
         ('Jak paddleboard skladovat?', 'Čistý a suchý, volně uložený a mimo přímé slunce.')],
)

NEW['funkcni-tricka'] = dict(short=True,
    title='Funkční trička pánská i dámská | Sporteka',
    desc='Funkční trička na běh, fitness a turistiku z polyesteru i merina. Porovnejte ceny českých obchodů a vyberte tričko podle sportu.',
    intro='<p><strong>Funkční tričko</strong> odvádí pot od těla a rychle schne. Pro běh, fitness a lehkou turistiku je výrazně praktičtější než bavlna, která se vlhkem těžkne a chladí.</p>'
          '<p>Na Sportece najdete trička z polyesteru i směsí, pro muže, ženy a děti. Vybírejte podle střihu, materiálu a pachové úpravy.</p>',
    guide='<h2>Jak vybrat funkční tričko</h2>'
          '<p>Rozhoduje materiál a střih. Polyester schne nejrychleji a je odolný, směsi s elastanem se lépe přizpůsobí tělu. Merino lépe udrží teplo a nezapáchá, ale schne pomaleji. Podrobnosti najdete v kategorii <a href="/merino-tricka/">merino trička</a>.</p>'
          '<h3>Materiály</h3>'
          + T(['Materiál', 'Vlastnosti'], [['Polyester', 'rychle schne, lehký, levnější'], ['Polyamid', 'hladký povrch, odolný'], ['Merino', 'regulace teploty, odolné proti pachům'], ['Směs s elastanem', 'pružnost a lepší přilnavost']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Švy:</strong> ploché nebo bezešvé zmenšují otěry při běhu.</li>'
          '<li><strong>Větrání:</strong> síťované panely zlepšují odvod vlhka.</li>'
          '<li><strong>Reflexní prvky:</strong> důležité při běhu za šera.</li>'
          '<li><strong>Střih:</strong> těsnější na kolo a běh, volnější na fitness a výlety.</li></ul>'
          '<h3>Péče o tričko</h3>'
          '<p>Perte na 30 až 40 °C bez aviváže, která zalepí vlákna a snižuje odvod potu. Nesušte na topení ani v horké sušičce. Pokud tričko zapáchá, dá se pachová zátěž obnovit praním ve sportovním přípravku.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("nike", "Nike"), ("mizuno", "Mizuno"), ("adidas", "Adidas"), ("progress", "Progress"), ("under-armour", "Under Armour"), ("craft", "Craft"))}. Další oblečení najdete v kategorii <a href="/sportovni-tricka/">sportovní trička</a>.</p>',
    faq=[('Čím se funkční tričko liší od bavlněného?', 'Odvádí pot od kůže a rychle schne. Bavlna vlhkost nasákne a chladí.'),
         ('Smrdí funkční trička?', 'Polyester si pach drží víc než merino. Pomáhá pravidelné praní a pachové úpravy.'),
         ('Jaká velikost funkčního trička?', 'Podle tabulky od výrobce. Na běh volte přiléhavý střih, na turistiku volnější.'),
         ('Mohu funkční tričko žehlit?', 'Nedoporučuje se, teplo poškozuje vlákno a potisk.'),
         ('Hodí se funkční tričko na zimu?', 'Jako první vrstva ano, spolu s teplou střední vrstvou a bundou.'),
         ('Jak často praní?', 'Po každém sportovním výkonu, aby se vlákno nezanášelo potem.')],
)

NEW['tilka'] = dict(short=True,
    title='Sportovní tílka a topy – dámské i pánské | Sporteka',
    desc='Sportovní tílka a topy na fitness, běh a léto. Porovnejte nabídku českých obchodů podle střihu, materiálu a velikosti.',
    intro='<p><strong>Sportovní tílko</strong> je nejvzdušnější vrstva pro horké dny, fitness a běh. Volný střih nebo přiléhavý top pro ženy zajistí pohyb bez omezení.</p>'
          '<p>Na Sportece najdete tílka a topy značek jako Adidas, Nike, Joma nebo Under Armour. Vybírejte podle sportu a materiálu.</p>',
    guide='<h2>Jak vybrat sportovní tílko</h2>'
          '<p>Na běh a fitness vyberte lehký materiál, který odvádí pot. Na vzpírání a posilovnu je praktický volnější střih s hlubšími průramky. Na každodenní nošení stačí směs s bavlnou, na sport raději syntetika.</p>'
          '<h3>Střihy</h3>'
          + T(['Střih', 'Kdy se hodí'], [['Pánské tílko', 'posilovna, běh, týmové sporty'], ['Dámské tílko', 'fitness, jóga, běh'], ['Crop top', 'fitness a léto, do vysokého pasu'], ['Sportovní top', 'tréninky s vyšší podporou, často s vyjímatelnými vycpávkami']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Materiál:</strong> polyester a elastan pro odvod potu a pružnost.</li>'
          '<li><strong>Průramky:</strong> příliš hluboké chladí a příliš těsné škrtí.</li>'
          '<li><strong>Délka:</strong> delší záda chrání při předklonu.</li>'
          '<li><strong>Švy:</strong> ploché zmenšují otěry u podpaží.</li></ul>'
          '<h3>Kombinace</h3>'
          '<p>Tílko kombinujte s <a href="/sportovni-kratasy/">sportovními kraťasy</a> nebo <a href="/leginy/">legínami</a>. Na chladnější dny se hodí navrch tričko nebo <a href="/mikiny/">mikina</a>. Pro vyšší podporu u žen viz <a href="/sportovni-podprsenky/">sportovní podprsenky</a>.</p>'
          '<h3>Péče</h3>'
          '<p>Perte na šetrný program bez aviváže a sušte na vzduchu. Tak vydrží barvy i pružnost materiálu.</p>',
    faq=[('Jaké tílko na běh?', 'Lehké z odvodního materiálu s plochými švy.'),
         ('Hodí se tílko i do posilovny?', 'Ano, volnější střih s hlubšími průramky nechá pohyb ramen volný.'),
         ('Jak velký crop top?', 'Podle tabulky. Delší střih zakryje pas při pohybu, kratší sedí těsněji.'),
         ('Mohu tílko nosit na sport i do města?', 'Lehké střihy ano, ale funkční materiál se hodí hlavně na sport.'),
         ('Jak prát tílko, aby nezmenšilo?', 'Při 30 °C a bez horkého sušení.'),
         ('Kdy je tílko lepší než tričko?', 'V horku a při intenzivním tréninku, kdy potřebujete větrání.')],
)

NEW['basketbal'] = dict(short=True,
    title='Basketbal – míče, boty, dresy a koše | Sporteka',
    desc='Basketbalové míče, obuv, dresy a doplňky. Porovnejte ceny českých obchodů a vyberte vybavení podle velikosti a hřiště.',
    intro='<p><strong>Basketbalové vybavení</strong> začíná míčem a obuví, které odpovídají hřišti a věku hráče. Venku potřebujete odolný povrch míče, v hale lepší přilnavost a tlumení.</p>'
          '<p>Na Sportece najdete míče, obuv, dresy a doplňky značek Nike, Adidas, Puma, Wilson, Spalding nebo Jordan.</p>',
    guide='<h2>Jak vybrat basketbalové vybavení</h2>'
          '<p>Míč vybírejte podle velikosti a prostředí. Gumový míč vydrží venku na asfaltu, kompozitní nebo kožený je určen pro halu. Boty musí držet kotník a tlumit dopady.</p>'
          '<h3>Velikosti míčů</h3>'
          + T(['Velikost', 'Kdo hraje'], [['5', 'děti zhruba do 11 let'], ['6', 'ženy a dívky, mladší dospívající'], ['7', 'muži a starší dorost'], ['3', 'minibasket']]) +
          '<h3>Obuv</h3>'
          '<p>Vysoká střiž nad kotník podepře kotník, nízká dává víc volnosti pohybu. Podrážka s dobrým vzorem drží na palubovce, venkovní si žádá odolnější směs. Přehled najdete v kategorii <a href="/basketbalova-obuv/">basketbalová obuv</a> a <a href="/basketbalove-mice/">basketbalové míče</a>.</p>'
          '<h3>Další vybavení</h3>'
          '<ul><li>Dresy a kraťasy z funkčního materiálu.</li><li>Ponožky s vyztužením u paty.</li><li>Chrániče kotníku a kolen, pokud hrajete často.</li><li>Pumpička na míč a taška na vybavení.</li></ul>'
          '<h3>Péče o míč</h3>'
          '<p>Míč nenafukujte přes limit uvedený na míči a skladujte mimo mráz a přímé slunce. Venkovní míč se po pár měsících obrousí, takže do haly ho nepoužívejte.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velký míč pro dítě.</li><li>Použití halové obuvi na asfaltu.</li></ul>',
    faq=[('Jaký míč pro děti?', 'Velikost 5, u menších hráčů i 3 nebo 4 pro minibasket.'),
         ('Rozdíl mezi venkovním a halovým míčem?', 'Venkovní má odolnější gumový povrch, halový lepší přilnavost a hodí se jen na palubovku.'),
         ('Jaké boty na basketbal?', 'S dobrou oporou kotníku, tlumením a podrážkou pro daný povrch.'),
         ('Kolik vzduchu v míči?', 'Podle údaje na míči. Při správném nahuštění míč odskočí zhruba do výše pasu až hrudi.'),
         ('Potřebuji speciální ponožky?', 'Ne, ale vyztužené ponožky pomáhají při dlouhých zápasech.'),
         ('Mohu hrát v běžeckých botách?', 'Nedoporučuje se, chybí boční opora.')],
)

NEW['nakrcniky-a-satky'] = dict(short=True,
    title='Nákrčníky, šátky a kukly – multifunkční | Sporteka',
    desc='Multifunkční nákrčníky, šátky a kukly na běh, kolo a lyže. Porovnejte nabídku českých obchodů podle materiálu a sezóny.',
    intro='<p><strong>Nákrčník nebo multifunkční šátek</strong> se nosí na krk, jako čelenka nebo jako čepice. V zimě chrání před větrem, v létě před sluncem a prachem.</p>'
          '<p>Na Sportece najdete nákrčníky, šátky a kukly od značek jako Buffalo, Rothco, Adidas, Mizuno nebo Finmark.</p>',
    guide='<h2>Jak vybrat nákrčník</h2>'
          '<p>Materiál volte podle sezóny. Lehký polyester nebo merino se hodí na jaro a podzim, fleecový a zateplený na zimu. Kukla chrání obličej a krk při běžkování i ve větru.</p>'
          '<h3>Materiály</h3>'
          + T(['Materiál', 'Kdy se hodí'], [['Polyester', 'běh, kolo, léto, rychlé schnutí'], ['Merino', 'chladno, nezapáchá'], ['Fleece', 'mráz a zima'], ['Bavlna', 'běžné nošení, méně sportovní']]) +
          '<h3>Způsoby nošení</h3>'
          '<ul><li>Jako šála kolem krku.</li><li>Přetažený přes ústa a nos při větru.</li><li>Jako čelenka nebo čepice pod helmu.</li><li>Jako pirátský šátek proti slunci.</li></ul>'
          '<h3>Pro koho</h3>'
          '<p>Běžci a cyklisté ocení lehký polyester, lyžaři a snowboardisté teplejší fleece nebo kuklu. Na hory se hodí i model s UV filtrem proti sněhové záři. Související kategorie: <a href="/cepice-a-celenky/">čepice a čelenky</a> a <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>.</p>'
          '<h3>Péče</h3>'
          '<p>Perte na 30 °C bez aviváže. Polyester rychle schne a nemusíte jej žehlit.</p>',
    faq=[('Čím se liší nákrčník od šály?', 'Je uzavřený do kruhu, takže nezaviává vítr a dá se nosit mnoha způsoby.'),
         ('Jaký nákrčník na zimu?', 'Fleecový nebo zateplený, případně merino na první vrstvu.'),
         ('Chrání nákrčník před sluncem?', 'Modely s UV filtrem ano.'),
         ('Jak velký nákrčník?', 'Univerzální velikost sedí většině lidí.'),
         ('Hodí se pod helmu?', 'Tenký nákrčník ano, nosí se místo čepice.'),
         ('Co je kukla?', 'Pokrývka hlavy a obličeje s otvorem pro oči a ústa, používá se v mrazu.')],
)

NEW['tenisova-obuv'] = dict(short=True,
    title='Tenisová obuv – na antuku, tvrdý povrch | Sporteka',
    desc='Tenisová obuv na antuku, tvrdý povrch i halu. Porovnejte ceny českých obchodů a vyberte boty podle povrchu a stylu hry.',
    intro='<p><strong>Tenisová obuv</strong> je navržena na rychlé boční pohyby a prudké zastavení. Podrážka a vyztužení se liší podle povrchu, proto stejné boty nemusí sedět na antuce i tvrdém kurtu.</p>'
          '<p>Na Sportece najdete tenisové boty značek Adidas, Head, K-Swiss, Asics, Mizuno nebo Lotto.</p>',
    guide='<h2>Jak vybrat tenisovou obuv</h2>'
          '<p>Nejdřív zjistěte povrch, na kterém hrajete nejčastěji. Antuka potřebuje vzor, který neklouže a nezanáší se, tvrdý povrch odolnou podrážku a tlumení.</p>'
          '<h3>Povrchy</h3>'
          + T(['Povrch', 'Podrážka'], [['Antuka', 'rybí kost, vzor který se neucpe'], ['Tvrdý povrch', 'odolná guma a tlumení'], ['Hala', 'hladší guma pro přilnavost'], ['Trávník', 'drobné výstupky, vzácnější']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Boční opora:</strong> zabraňuje podvrtnutí kotníku.</li>'
          '<li><strong>Tlumení:</strong> chrání klouby při dopadech.</li>'
          '<li><strong>Odolnost špičky:</strong> důležitá při tažení nohy.</li>'
          '<li><strong>Šířka:</strong> bota musí sedět bez tlaku na bocích.</li></ul>'
          '<h3>Životnost</h3>'
          '<p>Při pravidelné hře se podrážka opotřebuje po několika měsících. Vyměňte boty, když se vzor ztratí nebo začnou boky povolovat. Pro příbuzné sporty viz <a href="/salova-obuv/">sálová obuv</a> a <a href="/padel/">padel</a>. Další raketové sporty: <a href="/tenis/">tenis</a> a <a href="/badminton/">badminton</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Běžecké boty na kurtu bez boční opory.</li><li>Antuková obuv na tvrdém povrchu, která se rychle ničí.</li></ul>',
    faq=[('Mohu hrát tenis v běžeckých botách?', 'Nedoporučuje se, chybí boční opora a hrozí podvrtnutí.'),
         ('Jaká obuv na antuku?', 'S vzorem rybí kosti, který se nezanáší.'),
         ('Jak často měnit boty?', 'Při pravidelné hře asi po několika měsících, podle opotřebení podrážky.'),
         ('Jsou tenisové boty vhodné na padel?', 'Ano, ale padelová obuv má vhodnější vzor pro umělý povrch.'),
         ('Jak poznat správnou velikost?', 'Prsty se mají lehce hýbat a pata musí sedět pevně.'),
         ('Hodí se i na každodenní nošení?', 'Ano, ale podrážka se rychleji opotřebuje.')],
)

NEW['treninkova-obuv'] = dict(short=True,
    title='Fitness a tréninková obuv – do posilovny | Sporteka',
    desc='Fitness a tréninková obuv do posilovny, na crossfit a cvičení. Porovnejte nabídku českých obchodů podle stability a tlumení.',
    intro='<p><strong>Tréninková obuv</strong> je určená do posilovny, na funkční trénink a skupinové lekce. Má stabilnější podrážku než běžecká bota a lépe drží při bočním pohybu.</p>'
          '<p>Na Sportece najdete modely značek Skechers, Nike, Adidas, Joma, Wilson nebo Puma.</p>',
    guide='<h2>Jak vybrat tréninkovou obuv</h2>'
          '<p>Zvolte podle toho, co cvičíte. Na vzpírání je potřeba pevná plochá podrážka, na lekce a kruhové tréninky univerzální bota s tlumením.</p>'
          '<h3>Typy tréninku</h3>'
          + T(['Typ tréninku', 'Obuv'], [['Silový trénink', 'pevná a plochá podrážka'], ['Crossfit a HIIT', 'stabilní, odolná, s tlumením'], ['Aerobik a lekce', 'lehká s boční oporou'], ['Kardio na stroji', 'běžecká nebo lehčí tréninková']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Stabilita:</strong> široká patní část pro dřepy a mrtvé tahy.</li>'
          '<li><strong>Odolnost:</strong> vyztužená špička a boky při laně a švihadle.</li>'
          '<li><strong>Vzdušnost:</strong> prodyšný svršek pro delší trénink.</li>'
          '<li><strong>Hmotnost:</strong> lehčí obuv je pohodlnější při skocích.</li></ul>'
          '<h3>Čistota a péče</h3>'
          '<p>Obuv do haly používejte jen v hale, aby se podrážka neznečistila venku a nepoškodila palubovku. Po tréninku boty vyvětrejte. Související: <a href="/barefoot-obuv/">barefoot obuv</a> a <a href="/fitness/">fitness</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Měkká běžecká bota při těžkých dřepech.</li><li>Příliš těžké boty na skoky.</li></ul>',
    faq=[('Mohu cvičit v běžeckých botách?', 'Na kardio ano. Na silový trénink je lepší stabilní podrážka.'),
         ('Jaké boty na crossfit?', 'Stabilní s odolným svrškem a dobrou přilnavostí.'),
         ('Jsou tréninkové boty vhodné i na běh?', 'Na krátký běh ano, ale nemají tolik tlumení.'),
         ('Jak často měnit obuv?', 'Podle opotřebení podrážky a pohodlí, obvykle jednou za 6 až 12 měsíců.'),
         ('Hodí se plochá podrážka?', 'Na vzpírání ano, na skoky a kardio raději tlumenou.'),
         ('Smím je nosit venku?', 'Podrážka se rychleji ničí, na hale je ideální.')],
)

NEW['polokosile'] = dict(short=True,
    title='Polokošile pánské a dámské – sportovní | Sporteka',
    desc='Sportovní a casual polokošile pánské i dámské. Porovnejte ceny z českých obchodů a vyberte polo tričko podle materiálu a střihu.',
    intro='<p><strong>Polokošile</strong> je stylové tričko s límečkem a knoflíky. Hodí se na golf, tenis i do práce. Sportovní varianty z funkčního materiálu odvádějí pot.</p>'
          '<p>Na Sportece najdete polokošile značek US Polo Assn, Celio, Under Armour, Polo Ralph Lauren, Lotto nebo Helly Hansen.</p>',
    guide='<h2>Jak vybrat polokošili</h2>'
          '<p>Rozhoduje materiál a účel. Bavlněný piqué je klasický a prodyšný, polyesterová sportovní polokošile schne rychleji a je pružnější.</p>'
          '<h3>Materiály</h3>'
          + T(['Materiál', 'Charakter'], [['Bavlněný piqué', 'klasika, prodyšné, každodenní'], ['Polyester', 'sport, rychle schne'], ['Směs s elastanem', 'pružnost pro pohyb'], ['Merino', 'regulace teploty']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Límeček:</strong> pevný se drží tvaru, měkký je pohodlnější.</li>'
          '<li><strong>Střih:</strong> slim přiléhá, regular je volnější.</li>'
          '<li><strong>Délka:</strong> delší záda drží kalhoty při pohybu.</li>'
          '<li><strong>Tkanina:</strong> hustší piqué lépe skryje potu.</li></ul>'
          '<h3>Kdy ji nosit</h3>'
          '<p>Na golf a tenis, do práce s casual dress code i na letní procházky. Pro sportovní účely viz <a href="/golfove-obleceni-a-obuv/">golfové oblečení</a> a <a href="/sportovni-tricka/">sportovní trička</a>.</p>'
          '<h3>Péče</h3>'
          '<p>Perte obrácenou na 30 až 40 °C, aby límeček nepelichal. Žehlete na nižší teplotu a polyester raději vůbec.</p>',
    faq=[('Čím se polokošile liší od trička?', 'Má límeček a zapínání na knoflíky.'),
         ('Hodí se polokošile na sport?', 'Funkční polyesterová ano, třeba na golf a tenis.'),
         ('Jak velká polokošile?', 'Podle tabulky. Slim střih sedí přiléhavě.'),
         ('Zmenšuje se bavlněná polokošile?', 'Při vysoké teplotě ano, perte šetrně.'),
         ('Jak se starat o límeček?', 'Perte obrácenou a nežehlete ho příliš horkým železem.'),
         ('Hodí se do práce?', 'Do neformálního prostředí ano.')],
)

NEW['outdoorove-noze-a-multitoola'] = dict(short=True,
    title='Outdoorové nože a multitoolly | Sporteka',
    desc='Outdoorové nože, kapesní nože a multitoolly. Porovnejte ceny českých obchodů a vyberte nůž podle použití, oceli a pouzdra.',
    intro='<p><strong>Outdoorový nůž nebo multitool</strong> patří k základní výbavě na túru i kempování. Nůž řeže, štípe a loupe, multitool přidá kleště, šroubovák nebo otvírák.</p>'
          '<p>Na Sportece najdete nože značek Victorinox, Mikov, Albainox, Smith &amp; Wesson, K25 nebo Morakniv.</p>',
    guide='<h2>Jak vybrat nůž nebo multitool</h2>'
          '<p>Zvolte podle použití. Pevná čepel bez pantu je odolnější a vhodná na práci v přírodě, zavírací nůž se lépe nosí. Multitool nahradí několik nástrojů.</p>'
          '<h3>Typy</h3>'
          + T(['Typ', 'Použití'], [['Pevný nůž', 'bushcraft, vaření, práce v lese'], ['Zavírací nůž', 'běžné nošení, kapsa'], ['Multitool', 'oprava, drobné práce'], ['Kapesní nůž', 'lehká výbava, běžné řezání']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Ocel:</strong> nerezová je odolná proti korozi, uhlíková se lépe brousí, ale rezne.</li>'
          '<li><strong>Rukojeť:</strong> protiskluzová, aby nůž seděl v ruce i mokré.</li>'
          '<li><strong>Pouzdro:</strong> bezpečné nošení.</li>'
          '<li><strong>Zajištění:</strong> u zavíracího nože zamezí zavření na prsty.</li></ul>'
          '<h3>Péče a zákon</h3>'
          '<p>Nůž udržujte suchý, naolejujte čepel a brousil pravidelně. Nošení nožů se řídí zákonem a okolnostmi, takže nůž neukazujte na veřejnosti a nenoste ho tam, kde je zakázán. Související: <a href="/kempingove-nadobi/">kempingové nádobí</a>, <a href="/vareni-v-prirode/">vaření v přírodě</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš malý nůž na práci v lese.</li><li>Použití nože jako páčidla.</li></ul>',
    faq=[('Jaký nůž na kemp?', 'Pevný nůž s čepelí zhruba 10 cm je univerzální.'),
         ('Co je multitool?', 'Nástroj s kleštěmi a dalšími nástroji v jednom těle.'),
         ('Jaká ocel je nejlepší?', 'Nerezová je odolná proti rzi, uhlíková se lépe brousí.'),
         ('Jak nůž brousit?', 'Brouskem nebo brusným kamenem pod stálým úhlem.'),
         ('Smím nůž nosit na veřejnosti?', 'Řiďte se zákony a místními pravidly.'),
         ('Co je Victorinox?', 'Švýcarská značka kapesních nožů, známá multifunkčními noži.')],
)

NEW['vlasce-a-snury'] = dict(short=True,
    title='Vlasce a šňůry na rybaření – pletené, ocelové | Sporteka',
    desc='Rybářské vlasce, pletené šňůry a návazcové materiály. Porovnejte ceny z českých obchodů a vyberte vlasec podle lovu a nosnosti.',
    intro='<p><strong>Vlasec nebo pletená šňůra</strong> je spojením mezi rybářem a rybou. Správný průměr a nosnost rozhodují o dosahu hodu, citlivosti a bezpečném vyproštění.</p>'
          '<p>Na Sportece najdete vlasce a šňůry značek Daiwa, Mikado, Fox, Delphin, Korda nebo Westin.</p>',
    guide='<h2>Jak vybrat vlasec nebo šňůru</h2>'
          '<p>Rozhodněte, jaký lov chcete provozovat. Monofil je pružný a odpouští chyby, pletená šňůra je tenká, nenatahuje se a lépe přenáší záběr.</p>'
          '<h3>Druhy</h3>'
          + T(['Druh', 'Vlastnosti'], [['Monofil', 'pružný, levnější, odpouští chyby'], ['Pletená šňůra', 'tenká, bez natažení, citlivá'], ['Fluorocarbon', 'téměř neviditelný pod vodou'], ['Návazcový materiál', 'měkký nebo tuhý podle techniky']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Nosnost:</strong> volte podle velikosti ryb a typu lovu.</li>'
          '<li><strong>Průměr:</strong> tenčí vlasec letí dál a méně se vidí.</li>'
          '<li><strong>Odolnost proti otěru:</strong> důležitá v kamenech a vodní vegetaci.</li>'
          '<li><strong>Barva:</strong> nenápadná v čisté vodě, výrazná pro lepší kontrolu.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Vlasec po sezóně vyměňte, protože ztrácí pevnost. Po rybaření v moři jej opláchněte. Související: <a href="/rybarske-navijaky/">rybářské navijáky</a>, <a href="/rybarske-pruty/">pruty</a> a <a href="/rybareni/">rybaření</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš tenká šňůra v kamenech.</li><li>Špatný uzel, který snižuje pevnost.</li></ul>',
    faq=[('Vlasec nebo pletená šňůra?', 'Vlasec je pružný a odpouští, šňůra citlivější a bez natažení.'),
         ('Jak často vlasec měnit?', 'Podle používání, obvykle jednou za sezónu.'),
         ('Co je fluorocarbon?', 'Materiál s indexem lomu blízkým vodě, takže je pod hladinou méně vidět.'),
         ('Jaká nosnost?', 'Podle velikosti ryb a vybavení, nikdy ne víc než snese prut.'),
         ('Jaký uzel?', 'Prověřený rybářský, například palomar, který drží vysoký podíl pevnosti.'),
         ('Jak vlasec skladovat?', 'Mimo slunce a vlhko, aby neztratil pevnost.')],
)

NEW['sportovni-vesty'] = dict(short=True,
    title='Sportovní vesty – softshell, péřové, outdoor | Sporteka',
    desc='Sportovní a outdoorové vesty: zateplené, péřové, softshellové a běžecké. Porovnejte ceny z českých obchodů.',
    intro='<p><strong>Vesta</strong> zahřeje trup a nechá volné ruce. Na podzim se nosí na běh, na kolo i do města, v zimě jako střední vrstva pod bundu.</p>'
          '<p>Na Sportece najdete vesty značek Regatta, Rockbros, Northfinder, Celio, Columbia nebo Helly Hansen.</p>',
    guide='<h2>Jak vybrat vestu</h2>'
          '<p>Rozhodněte, k čemu ji budete používat. Zateplená vesta slouží jako střední vrstva, softshellová chrání před větrem, běžecká je lehká a skladná.</p>'
          '<h3>Typy</h3>'
          + T(['Typ', 'Použití'], [['Péřová nebo prošívaná', 'střední vrstva, chladné dny'], ['Softshellová', 'vítr a lehká mlha'], ['Fleecová', 'teplá vrstva, suchá zima'], ['Běžecká', 'lehká, skladná, reflexní'], ['Cyklistická', 'vítr na hrudi, vzdušná záda']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Výplň:</strong> péří je lehké, syntetika snáší vlhko.</li>'
          '<li><strong>Kapsy:</strong> zapínací chrání telefon a klíče.</li>'
          '<li><strong>Střih:</strong> přiléhavý pro běh, volnější do města.</li>'
          '<li><strong>Zip:</strong> kvalitní chrání před větrem.</li></ul>'
          '<h3>Kombinace</h3>'
          '<p>Vestu kombinujte s <a href="/funkcni-tricka/">funkčním tričkem</a> nebo mikinou a v mrazu s bundou. Související: <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>.</p>'
          '<h3>Péče</h3>'
          '<p>Vestu perte podle štítku, péřovou ve speciálním přípravku a vysušte společně s míčky, aby se péří nepolepilo.</p>',
    faq=[('K čemu je vesta?', 'Zahřeje jádro těla a nechá pohyb rukou volný.'),
         ('Péřová nebo syntetická?', 'Péřová je lehčí, syntetická lépe odolá vlhku.'),
         ('Hodí se vesta na běh?', 'Lehká a skladná ano.'),
         ('Jak velká vesta?', 'Podle tabulky, přes tenkou vrstvu.'),
         ('Jak vestu prát?', 'Dle štítku, péřovou šetrně a sušit s míčky.'),
         ('Mohu ji nosit pod bundu?', 'Ano, je to oblíbená střední vrstva.')],
)

NEW['nepromokave-bundy'] = dict(short=True,
    title='Nepromokavé a outdoorové bundy | Sporteka',
    desc='Nepromokavé bundy s membránou, pláštěnky a outdoorové bundy. Porovnejte ceny českých obchodů a vyberte bundu na déšť a horskou túru.',
    intro='<p><strong>Nepromokavá bunda</strong> chrání před deštěm a větrem při túrách, na kole i ve městě. Rozhoduje membrána, zatmelené švy a prodyšnost.</p>'
          '<p>Na Sportece najdete bundy značek Trespass, Regatta, Dare2b, Viking, Columbia nebo Helly Hansen.</p>',
    guide='<h2>Jak vybrat nepromokavou bundu</h2>'
          '<p>Zvolte podle intenzity aktivity a počasí. Nepromokavost se udává ve vodním sloupci v milimetrech, prodyšnost v gramech vodní páry. Čím vyšší hodnoty, tím lepší ochrana.</p>'
          '<h3>Jak číst parametry</h3>'
          + T(['Parametr', 'Význam'], [['Vodní sloupec', 'odolnost proti pronikání vody'], ['Prodyšnost', 'schopnost odvádět vlhkost zevnitř'], ['Zatmelené švy', 'ochrana v místech sešití'], ['Kapuce', 'stavitelná, s kšiltem']]) +
          '<h3>Na co se dívat</h3>'
          '<ul><li><strong>Membrána:</strong> například Gore-Tex nebo vlastní membrány značek.</li>'
          '<li><strong>Větrání:</strong> zipy pod paží odvádí teplo.</li>'
          '<li><strong>Kapuce a límec:</strong> musí sedět i s helmou.</li>'
          '<li><strong>Skladnost:</strong> bunda do batohu pro případ deště.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Perte speciálním přípravkem a obnovte impregnaci, když voda přestane perlit. Dobře udržovaná membrána funguje déle. Související: <a href="/softshellove-bundy/">softshellové bundy</a>, <a href="/vetrovky/">větrovky</a> a <a href="/kabaty-a-parky/">kabáty a parky</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těsná bunda bez místa na vrstvy.</li><li>Praní s aviváží, která zničí membránu.</li></ul>',
    faq=[('Co znamená vodní sloupec?', 'Výška vodního sloupce v milimetrech, který látka udrží, než propustí vodu.'),
         ('Rozdíl mezi nepromokavou a voděodolnou?', 'Nepromokavá má membránu a zatmelené švy, voděodolná jen odpuzuje drobný déšť.'),
         ('Jak často impregnovat?', 'Když voda přestane perlit, zhruba po několika sezónách.'),
         ('Mohu bundu prát v pračce?', 'Ano, speciálním přípravkem bez aviváže.'),
         ('Je Gore-Tex nutný?', 'Ne, kvalitní membrány mají i jiné značky.'),
         ('Jak bunda dýchá?', 'Membrána odvádí vodní páru ven.')],
)

NEW['fotbal'] = dict(short=True,
    title='Fotbal – míče, dresy, rukavice a doplňky | Sporteka',
    desc='Fotbalové míče, dresy, brankářské rukavice, chrániče a doplňky. Porovnejte ceny z českých obchodů a vyberte výbavu podle povrchu.',
    intro='<p><strong>Fotbalová výbava</strong> se skládá z míče, kopaček, chráničů a dresu. Správná kopačka a míč odpovídající povrchu zlepší hru i sníží riziko zranění.</p>'
          '<p>Na Sportece najdete vybavení značek Puma, Adidas, Powershot, Nike, Kipsta nebo Merco.</p>',
    guide='<h2>Jak vybrat fotbalové vybavení</h2>'
          '<p>Základem je správný povrch. Pro trávu a umělou trávu platí jiné kopačky, v hale se hraje v sálové obuvi. Míč volte podle věku a velikosti hřiště.</p>'
          '<h3>Velikosti míčů</h3>'
          + T(['Velikost', 'Kdo hraje'], [['3', 'mladší děti'], ['4', 'děti zhruba do 12 let'], ['5', 'dospělí a dorost'], ['Futsal', 'menší, méně skákavý míč']]) +
          '<h3>Další vybavení</h3>'
          '<ul><li>Kopačky podle povrchu: <a href="/kopacky/">kopačky</a>.</li><li>Chrániče a štulpny: <a href="/fotbalove-chranice-a-stulpny/">fotbalové chrániče a štulpny</a>.</li><li>Brankářské <a href="/brankarske-rukavice/">rukavice</a>.</li><li>Fotbalové <a href="/fotbalove-mice/">míče</a>.</li></ul>'
          '<h3>Dresy a oblečení</h3>'
          '<p>Dres z funkčního materiálu odvádí pot a nebrání pohybu. Týmové dresy mají unikátní potisk čísla, který se hodí vyprat šetrně. Pro trénink se hodí <a href="/teplaky/">tepláky</a> a <a href="/dresy/">dresy</a>.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Kopačky na špatný povrch.</li><li>Příliš velký míč pro dítě.</li><li>Zanedbání chráničů při tréninku.</li></ul>',
    faq=[('Jaký míč pro dítě?', 'Velikost 3 nebo 4 podle věku.'),
         ('Jaké kopačky na umělou trávu?', 'S výstupky určenými pro umělý povrch.'),
         ('Jsou chrániče povinné?', 'V zápase ano, v tréninku se důrazně doporučují.'),
         ('Jak péče o míč?', 'Nafouknout dle štítku a skladovat mimo mráz.'),
         ('Co je futsal?', 'Sálová varianta s menším míčem a pravidly pro hru v hale.'),
         ('Jak často měnit kopačky?', 'Dle opotřebení, nejpozději když povolí upevnění.')],
)
