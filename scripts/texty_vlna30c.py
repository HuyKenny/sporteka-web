"""sporteka.cz — wave 30c (17. 11. 2026): long texts for buzoly-a-kompasy, neoprenove-boty-a-ponozky, esusy.
General true facts only, no prices, no product counts. Mils: NATO 6400 / former Warsaw Pact 6000 / Swedish 6300 (obsolete),
per the milliradian reference. Needle balancing zones per Suunto support pages (two-zone or global needle; older five zones).
Magnetic declination in Czechia given only as "a few degrees east", no exact figure. Etymology of "ešus" left out (unverified).
Material densities Al 2.7 / Ti 4.5 / steel about 7.9 g/cm3 are textbook values. Brands linked only if present in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ buzoly-a-kompasy
NEW['buzoly-a-kompasy'] = dict(long=True,
    title='Buzoly a kompasy: mapové, zrcátkové i vojenské',
    desc='Buzoly s destičkou na mapu, zrcátkové a vojenské buzoly i malé kompasy na klíče. Rozdíl buzola vs kompas, deklinace, azimut a nabídky českých e-shopů.',
    intro='<p><strong>Buzola</strong> je nejspolehlivější navigační pomůcka, jakou můžete do batohu přibalit. Nepotřebuje baterii ani signál, nevadí jí mráz a s papírovou mapou vás dovede i tam, kde telefon dávno ukazuje jen šedou plochu. Tahle kategorie zahrnuje mapové buzoly s průhlednou destičkou, zrcátkové buzoly pro přesné zaměření vzdáleného bodu, vojenské buzoly s průhledítkem a kovovým pouzdrem a také jednoduché kompasy na klíče nebo na řemínek hodinek, které slouží spíš jako rychlá orientace.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže vidíte, kde je model skladem, a nákup pak proběhne přímo u zvoleného prodejce. Najdete tu výrobky značek Silva, Suunto, Explorer nebo Mil-Tec. Nadřazenou kategorií jsou <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>, další drobnosti na cesty jsou mezi <a href="/outdoor-doplnky/">outdoorovými doplňky</a>.</p>',
    guide='<h2>Buzola, nebo kompas?</h2>'
          '<p>V běžné řeči se obě slova zaměňují, ale v češtině mezi nimi bývá rozdíl. Kompas je obecně přístroj se zmagnetovanou střelkou, která se natočí k magnetickému severu. Ukáže tedy, kudy je sever, a to je všechno. Buzola je kompas doplněný o otočný kruh se stupnicí a o pomůcky k zaměření směru, takže s ní změříte úhel mezi severem a cílem, tedy azimut. Mapová buzola má navíc průhlednou destičku s pravítky a měřítky, se kterou se pracuje přímo na mapě. Pro turistu, který chce chodit podle mapy, je proto správnou volbou buzola. Malý kompas na klíče se hodí jako záloha nebo pro dítě, které se učí, kde je sever.</p>'
          + T(['Typ', 'Jak vypadá', 'K čemu se hodí'], [
              ['Mapová buzola s destičkou', 'průhledná základna, pravítka, otočné pouzdro s ryskami', 'turistika, výuka, orientace v terénu podle mapy'],
              ['Zrcátková buzola', 'odklápěcí víčko se zrcátkem a záměrnou ryskou', 'přesné zaměření vzdáleného bodu, hory, delší přechody'],
              ['Vojenská buzola s průhledítkem', 'kovové pouzdro, hledí, lupa ke čtení stupnice', 'zaměřování v terénu, odolnost, dílcová stupnice'],
              ['Palcová buzola', 'malá destička, která se nasadí na palec', 'orientační běh, rychlé čtení mapy za pohybu'],
              ['Kompas na klíče či řemínek', 'malé pouzdro bez stupnice nebo jen s hrubým dělením', 'záloha, přibližný směr, dárek']]) +
          '<h2>Jak se pozná dobrá buzola</h2>'
          '<p>Střelka u kvalitních modelů plave v pouzdře naplněném kapalinou. Ta ji tlumí, takže se po zastavení rychle ustálí a nekmitá. Rysky v pouzdře, kterým se říká poledníkové nebo orientační čáry, mají být dobře čitelné i proti tmavé mapě. Otočný kruh by měl jít točit s mírným odporem, aby se nastavený azimut v kapse sám nepřetočil. Stupnice po dvou stupních je pro turistiku dostatečně jemná. Fosforeskující body na střelce a v pouzdře oceníte za šera, kdy se čísla na stupnici špatně čtou.</p>'
          '<p>U destičky se dívejte na měřítka podél hran. Pokud odpovídají měřítku vašich map, změříte vzdálenost bez přepočítávání. Lupa uprostřed destičky pomůže s drobným písmem v hustých mapách a gumové nožky na spodní straně brání tomu, aby buzola po mapě klouzala. Šňůrka na krk není maličkost: buzola v rukavicích vypadne snadno a v trávě se hledá špatně.</p>'
          '<h2>Deklinace: proč sever není jen jeden</h2>'
          '<p>Střelka neukazuje přesně k zeměpisnému severnímu pólu, ale k magnetickému severu. Úhel mezi oběma směry se nazývá magnetická deklinace. Liší se podle místa na Zemi a v čase se pomalu mění, protože se magnetický pól posouvá. V Česku je v současnosti deklinace jen několik stupňů a směřuje na východ, takže na krátké procházce ji turista téměř nepozná. Na delším přechodu v mlze nebo v lese ale chyba o pár stupňů znamená, že po několika kilometrech skončíte o kus vedle cíle.</p>'
          '<p>Na topografických mapách bývá hodnota deklinace uvedena v legendě nebo na okraji mapového listu, často i s údajem, o kolik se ročně mění. Na vojenských a některých dalších mapách se navíc rozlišuje sever souřadnicové sítě, protože svislé čáry mřížky nemusí přesně mířit k zeměpisnému pólu. Lepší buzoly mají nastavitelnou korekci deklinace: malým šroubkem posunete orientační šipku o příslušný úhel a dál už nic nepřepočítáváte. U jednodušších modelů se při východní deklinaci hodnota od azimutu změřeného na mapě odečte, abyste dostali azimut pro chůzi podle střelky.</p>'
          '<h2>Azimut z mapy krok za krokem</h2>'
          '<ul><li><strong>Spojte start a cíl:</strong> položte buzolu na mapu tak, aby hrana destičky vedla od místa, kde stojíte, k cíli, a šipka směru pochodu mířila k cíli.</li>'
          '<li><strong>Natočte pouzdro:</strong> otáčejte kruhem, dokud rysky v pouzdře nejsou rovnoběžné se svislými čarami mapy a sever pouzdra nemíří k hornímu okraji mapy.</li>'
          '<li><strong>Odečtěte azimut:</strong> na značce u základny přečtete úhel. Pokud buzola nemá korekci, upravte ho o deklinaci.</li>'
          '<li><strong>Zvedněte buzolu:</strong> držte ji vodorovně před sebou a otáčejte se celým tělem, až se severní konec střelky kryje s orientační šipkou v pouzdře.</li>'
          '<li><strong>Vyberte záchytný bod:</strong> šipka směru teď ukazuje k cíli. Zvolte si v tomto směru strom, skálu nebo sloup, dojděte k němu a postup opakujte.</li></ul>'
          '<p>Chůze od bodu k bodu je přesnější než snaha jít celou trasu se zrakem upřeným na střelku. V lese, kde nevidíte daleko, pomáhá jít ve dvou: jeden drží směr a druhého posílá dopředu jako záchytný bod. Kdo se chce v navigaci zlepšit, nejrychleji se to naučí na kurzu nebo na tréninku orientačního běhu, kde se práce s mapou a buzolou nacvičuje opakovaně.</p>'
          '<h2>Stupně, nebo dílce?</h2>'
          '<p>Turistické buzoly mají stupnici rozdělenou na 360 stupňů. Vojenské modely často nesou i dílcovou stupnici. Dílec je úhlová jednotka používaná v armádě a dělostřelectvu, protože se s ní snadno odhaduje vzdálenost: předmět široký jeden metr ve vzdálenosti jednoho kilometru odpovídá zhruba jednomu dílci. Různé armády ale nedělily kruh stejně. NATO používá 6 400 dílců, bývalý Sovětský svaz a armády Varšavské smlouvy 6 000 dílců a švédská armáda měla vlastních 6 300 dílců, od kterých už upustila. Pokud kupujete starší vojenskou buzolu nebo její repliku, podívejte se, které dělení stupnice nese, jinak budete přepočítávat úhly, které nesedí.</p>'
          '<h2>Zrcátko a průhledítko</h2>'
          '<p>Zrcátková buzola má víčko se zrcátkem a záměrnou ryskou. Při zaměřování ji držíte v úrovni očí, cíl sledujete přes zářez ve víčku a v zrcátku současně vidíte střelku i pouzdro. Odpadá tak skloněný pohled do dlaně a zaměření vzdáleného vrcholu je přesnější. Víčko zároveň chrání pouzdro v batohu. Vojenské buzoly s průhledítkem a lupou fungují podobně: hledím zaměříte cíl a lupou přečtete stupnici. Bývají v kovovém pouzdře, jsou odolné a dají se zaklapnout, s mapou se s nimi ale pracuje hůř než s průhlednou destičkou.</p>'
          '<h2>Na které polokouli chcete chodit</h2>'
          '<p>Magnetické pole Země nemíří vodorovně, ale skloněně k zemi, a na různých místech planety je ten sklon jiný. Výrobci proto střelky vyvažují pro určitou oblast. Starší buzoly Suunto se vyráběly pro pět zón, dnes firma podle svých stránek používá buď dvě zóny, severní a jižní, nebo globální střelku, která funguje kdekoli na Zemi a snese i mírný náklon pouzdra. Buzola koupená v Evropě je vyvážená pro severní polokouli. Pokud se chystáte na trek do Patagonie, Austrálie nebo na Nový Zéland, vyplatí se model s globální střelkou, jinak se střelka může naklánět a drhnout o pouzdro.</p>'
          '<h2>Co buzolu ruší</h2>'
          '<ul><li><strong>Kovy a magnety:</strong> nůž, karabiny, kovový rám batohu nebo magnetické zapínání pouzdra odchýlí střelku, pokud jsou blízko.</li>'
          '<li><strong>Elektronika:</strong> telefon, vysílačka nebo baterie celovky mají vlastní magnetické pole, při měření je odložte stranou.</li>'
          '<li><strong>Auto a vedení:</strong> uvnitř auta nebo pod elektrickým vedením buzola neměří spolehlivě.</li>'
          '<li><strong>Silný magnet:</strong> v těsné blízkosti může střelku přemagnetovat, takže pak ukazuje obráceně. Ověříte to podle slunce nebo jiné buzoly.</li></ul>'
          '<p>Občas se v pouzdře objeví malá bublina, typicky v mrazu nebo ve vyšší nadmořské výšce. Pokud se při návratu do tepla zmenší a pohyb střelky neovlivňuje, není důvod k obavám. Velká bublina, která se nezmenšuje, ukazuje spíš na netěsnost pouzdra.</p>'
          '<h2>Buzola, hodinky, nebo mobil?</h2>'
          '<p>Elektronický kompas mají dnes telefony i mnohé <a href="/sportovni-hodinky/">sportovní hodinky</a>. Je pohodlný, ale potřebuje kalibraci, nabitou baterii a nesnáší chlad, ve kterém baterie rychle slábne. Mechanická buzola je proto rozumná pojistka i pro toho, kdo jinak naviguje podle aplikace. Váží pár desítek gramů a v horní kapse <a href="/turisticke-batohy/">turistického batohu</a> nezabere skoro žádné místo. K nouzové výbavě na hory se k ní hodí <a href="/celovky-a-svitilny/">čelovka</a> a <a href="/outdoorove-noze-a-multitoola/">nůž nebo multitool</a>, pro pozorování krajiny pak dalekohled ze stejné nadřazené kategorie.</p>'
          '<h2>Zpětný azimut a cesta zpátky</h2>'
          '<p>Zpětný azimut je směr opačný k tomu, kterým jste přišli. Získáte ho tak, že k naměřenému úhlu přičtete 180 stupňů, nebo je odečtete, pokud je původní hodnota větší než 180. Hodí se, když se chcete vrátit k autu, chatě nebo k rozcestí, ze kterého jste odbočili do lesa. Prakticky to jde i bez počítání: necháte nastavený azimut na kruhu a při návratu natočíte tělo tak, aby se s orientační šipkou kryl jižní, obvykle bílý konec střelky. Zpětným azimutem se dá také ověřit vlastní poloha. Zaměříte dva vzdálené výrazné body, které najdete na mapě, a průsečík čar vedených z nich zpět ukáže, kde přibližně stojíte.</p>'
          '<h2>Buzola pro děti a začátečníky</h2>'
          '<p>Na první krůčky s mapou stačí jednoduchá mapová buzola s velkou stupnicí a výraznými čísly. Dětem se dobře učí na známém místě, třeba v parku za domem: nejprve najít sever, pak dojít k vybranému stromu podle azimutu a nakonec zkusit krátkou trasu po bodech. Malý kompas na klíče je vhodný jako hračka nebo připomínka, k výuce azimutu se ale nehodí.</p>'
          '<h2>Péče o buzolu</h2>'
          '<p>Buzolu skladujte mimo reproduktory, magnetické držáky nářadí a elektroniku. Nenechávejte ji dlouho na přímém slunci, třeba za předním sklem auta, kde se pouzdro může deformovat a kapalina unikat. Destičku stačí otřít vlhkým hadříkem, rozpouštědla a repelenty s agresivními látkami mohou průhledný plast zakalit. Před každou větší túrou ověřte, že střelka po vychýlení vždy dojde zpět ke stejnému směru.</p>',
    faq=[
        ('Jaký je rozdíl mezi buzolou a kompasem?', 'Kompas jen ukazuje magnetický sever. Buzola má navíc otočný kruh se stupnicí a zaměřovací pomůcky, takže s ní změříte azimut a pracujete s mapou.'),
        ('Jakou buzolu koupit na turistiku?', 'Mapovou buzolu s průhlednou destičkou, kapalinou tlumenou střelkou a měřítky, která odpovídají vašim mapám. Na hory a delší přechody se vyplatí zrcátkový model.'),
        ('Co je deklinace a musím ji řešit?', 'Je to úhel mezi zeměpisným a magnetickým severem. V Česku činí jen několik stupňů, na delší trase v mlze se ale chyba sčítá, proto se vyplatí ji korigovat.'),
        ('Kolik dílců má kruh?', 'Podle systému NATO 6 400, v armádách bývalé Varšavské smlouvy se používalo 6 000 dílců. Starší vojenské buzoly proto mohou mít jinou stupnici než nové.'),
        ('Funguje česká buzola na jižní polokouli?', 'Buzola vyvážená pro severní polokouli se na jihu může naklánět a drhnout. Na cesty do Austrálie či Jižní Ameriky je vhodnější model s globální střelkou.'),
        ('Proč mi buzola ukazuje špatně?', 'Nejčastěji ji ruší kov nebo elektronika v blízkosti, případně auto či elektrické vedení. Silný magnet může střelku i přemagnetovat.'),
        ('Nahradí buzolu mobil?', 'Na běžné výlety často ano, ale telefon potřebuje baterii a kalibraci a v zimě rychle vybíjí. Mechanická buzola je levná a lehká záloha.'),
        ('Kde vybranou buzolu koupím?', 'Na Sportece porovnáte nabídky několika českých e-shopů. Po výběru přejdete do obchodu, kde objednávku dokončíte.'),
    ])

# ------------------------------------------------------------------ neoprenove-boty-a-ponozky
NEW['neoprenove-boty-a-ponozky'] = dict(long=True,
    title='Neoprenové boty a ponožky do vody i k otužování',
    desc='Neoprenové ponožky a botičky od 2 do 7 mm pro potápění, surf, kajak, paddleboard i otužování. Jak vybrat tloušťku, podrážku a velikost, nabídky e-shopů.',
    intro='<p><strong>Neoprenové ponožky a boty</strong> drží nohy v teple tam, kde by jinak rychle prochladly: ve studené vodě, na kamenitém dně, na mokré palubě paddleboardu i při zimním otužování. Neopren je pěnová pryž plná drobných uzavřených bublinek vzduchu, která špatně vede teplo. Do botičky sice voda nateče, ale tenká vrstva, která zůstane u kůže, se od nohy ohřeje a dál se příliš nevyměňuje. Kategorie zahrnuje tenké neoprenové ponožky do ploutví, nízké botičky s podrážkou i vysoké boty na zip s pevnou podešví.</p>'
          '<p>Na Sportece najdete nabídky českých e-shopů pohromadě a objednávku dokončíte přímo u obchodu, který si vyberete. V nabídce jsou mimo jiné výrobky ' + B(('o-neill', "O'Neill")) + ', Aqualung, Hiko nebo Buddyswim. Nadřazená kategorie je <a href="/obuv-do-vody/">obuv do vody</a>, ke stejnému vybavení patří <a href="/neopreny/">neopreny</a>.</p>',
    guide='<h2>Ponožka, nebo bota?</h2>'
          '<p>Neoprenová ponožka má jen tenkou, často protiskluzově potištěnou spodní stranu. Je měkká a přiléhavá, takže se vejde do ploutve nebo do jiné boty. Potápěči a šnorchlaři ji nosí do ploutví s uzavřenou patou, kde zabrání odření a trochu zahřeje. Otužilci ji zase oceňují pro jednoduchost: rychle se obuje i v zimě na břehu. Neoprenová bota má pevnou pryžovou podrážku, někdy zesílenou patu a špičku, a chrání chodidlo před ostrými kameny, mušlemi nebo rozbitým sklem. Chodí se v ní i po souši, třeba po kamenité pláži nebo z parkoviště k vodě.</p>'
          + T(['Typ', 'Typická tloušťka', 'Kde se uplatní'], [
              ['Tenká neoprenová ponožka', 'přibližně 1,5 až 3 mm', 'do ploutví s uzavřenou patou, šnorchlování, pod jinou botu'],
              ['Nízká botička s podrážkou', 'přibližně 2 až 3 mm', 'koupání, kajak, paddleboard, kamenité pláže'],
              ['Surfová bota s dělenou špičkou', 'přibližně 3 až 5 mm', 'surf, windsurf, kite, cit pro prkno'],
              ['Vysoká bota na zip s tvrdou podešví', 'přibližně 5 až 7 mm', 'potápění s ploutvemi s otevřenou patou, chladná voda'],
              ['Silná ponožka nebo bota k otužování', '5 mm a více', 'zimní plavání, vstup do studené vody a pobyt na břehu']]) +
          '<p>Tloušťky v tabulce jsou orientační, výrobci je kombinují různě a jedna bota může mít podešev jinou než svršek. Pro výběr platí jednoduché pravidlo: čím chladnější voda a čím déle v ní budete, tím silnější neopren dává smysl. Silnější materiál ale omezuje pohyb a cit v chodidle.</p>'
          '<h2>Jak silný neopren zvolit</h2>'
          '<p>Na letní koupání a krátké vodní výlety stačí 2 až 3 mm. Taková bota chrání chodidlo, příliš nehřeje a v teplém dni se v ní noha nezapaří. Na jaře a na podzim, na přehradě nebo na horské řece se hodí 3 až 5 mm. Na potápění v jezerech, kde je v hloubce chladno i v létě, a na zimní otužování se nosí 5 až 7 mm. Každý ale snáší chlad jinak, a kdo má sklony ke studeným nohám, sáhne raději po silnější variantě. Nezapomeňte, že nohy chladnou i na břehu, kdy stojíte v mokré obuvi ve větru, proto se otužilcům hodí bota, ve které se dá pohodlně dojít k vodě i zpět.</p>'
          '<h2>Dělená, nebo kulatá špička</h2>'
          '<p>Surfové boty se vyrábějí ve dvou tvarech. Kulatá špička je klasika, ve které jsou všechny prsty pohromadě. Je teplejší, snadno se obouvá a vejde se i do jiné obuvi. Dělená špička, které se podle japonských ponožek říká tabi, odděluje palec od ostatních prstů. Noha v ní lépe drží na prkně, méně klouže uvnitř boty a jezdec má větší cit. Surfaři a kitaři ji proto mají rádi, pro plavání do ploutví nebo pro kajak taková výhoda odpadá. Kdo dělenou špičku nikdy nezkoušel, na první obutí si musí chvíli zvykat.</p>'
          '<h2>Podrážka, zip a švy</h2>'
          '<ul><li><strong>Podrážka:</strong> měkká a tenká dá dobrý cit, ale na ostrých kamenech může propíchnout. Tvrdší podešev s vzorkem je lepší na skalnatý vstup do vody a na chůzi po břehu.</li>'
          '<li><strong>Zip:</strong> vysoké boty mívají zip na boku, se kterým se obouvají snáz. Za zipem by měl být neoprenový klín, jinak skrz něj protéká voda.</li>'
          '<li><strong>Výška:</strong> nízká botička je pohodlná na souši, vysoká překryje lem neoprenových kalhot a nepouští dovnitř tolik studené vody.</li>'
          '<li><strong>Švy:</strong> plochý prošitý šov (flatlock) je pevný, ale propouští trochu vody. Lepené a zaslepené šité švy těsní lépe a na studenou vodu se hodí víc.</li>'
          '<li><strong>Zesílení:</strong> pata a špička z odolnější gumy prodlouží botě život, pokud v ní hodně chodíte po kamenech.</li></ul>'
          '<h2>Velikost a střih</h2>'
          '<p>Neopren má sedět přiléhavě, ale nesmí škrtit. Volná bota nabírá čerstvou vodu při každém pohybu a pak nehřeje, příliš těsná zase omezí prokrvení a nohy mrznou právě kvůli tomu. Prsty by se neměly opírat o špičku natvrdo. Silnější neopren uvnitř zabírá víc místa, proto se u 5 až 7mm bot vyplatí zkontrolovat velikostní tabulku výrobce a případně zvážit číslo navíc. Pokud nosíte botu s ploutví s otevřenou patou, vybírejte obě věci společně: velikost ploutve se řídí tím, jakou botu do ní obujete. Pro malé vodáky jsou tu i <a href="/detske-boty-do-vody/">dětské boty do vody</a>.</p>'
          '<h2>Pro jaké sporty se hodí</h2>'
          '<ul><li><strong>Potápění:</strong> vysoká bota s tvrdou podešví a ploutve s otevřenou patou jsou obvyklá kombinace, zvlášť při vstupu do vody z břehu. Ploutve najdete v kategorii <a href="/ploutve/">ploutve</a>.</li>'
          '<li><strong>Šnorchlování:</strong> tenká ponožka chrání nohu v gumové kapse ploutve a na kamenité pláži i před drobnými poraněními. Zbytek výbavy je v kategorii <a href="/snorchlovani/">šnorchlování</a>.</li>'
          '<li><strong>Paddleboard a kajak:</strong> nízká bota s pevnou podrážkou se hodí na nastupování z kamenů a na chladnější dny na vodě. Podívejte se i na <a href="/paddleboardy/">paddleboardy</a> a <a href="/kajaky-a-cluny/">kajaky a čluny</a>.</li>'
          '<li><strong>Surf, windsurf a kite:</strong> dělená špička a středně silný neopren, v zimních měsících i silnější.</li>'
          '<li><strong>Otužování a plavání v otevřené vodě:</strong> silné ponožky nebo boty zahřejí chodidla, která chladnou nejrychleji. Na závodech a v organizovaných akcích ale mohou platit pravidla, která neopren omezují, proto si je zjistěte předem.</li></ul>'
          '<h2>Bezpečnost ve studené vodě</h2>'
          '<p>Neoprenová bota zmírní chlad, ale tělo před podchlazením neochrání. Do studené vody vstupujte postupně, nikdy sami a s někým, kdo zůstane na břehu. Neopren je navíc lehčí než voda, takže nohy v silných botách mírně nadnáší, s čímž je dobré počítat při plavání. Na vodě s lodí nebo prknem patří k výbavě <a href="/plovaci-vesty/">plovací vesta</a> podle druhu aktivity.</p>'
          '<h2>Otužování: proč začínat od nohou</h2>'
          '<p>Chodidla a prsty patří k místům, která ve studené vodě bolí nejdřív. Krev se v chladu stahuje z končetin do trupu a nohy ztrácejí teplo rychleji než zbytek těla. Řada otužilců proto zjišťuje, že by ve vodě vydržela déle, kdyby je nebolely prsty. Neoprenové ponožky nebo nízké botičky tento problém zmírní a navíc ochrání před kluzkými kameny a ledem na břehu. Pro chůzi po zamrzlé nebo sněhem zapadané cestě k vodě se víc hodí bota s pevnou podrážkou než měkká ponožka. Po výstupu z vody se otužilci obvykle nejdřív zbaví mokrého neoprenu a obují suché teplé ponožky a boty, protože vlhký materiál začne na vzduchu ve větru studit.</p>'
          '<h2>Ponožky, boty a další neopren dohromady</h2>'
          '<p>Neoprenovou ponožku lze obout i pod sandál nebo běžnou botu do vody. Taková kombinace se osvědčuje na vodácké výpravě, kde chcete mít nohu v teple a zároveň pevnou podrážku na přenášení lodí. Pokud nosíte neoprenový oblek, sladěné boty a rukavice prodlouží dobu, kterou ve vodě zvládnete. Obleky, rukavice a kukly najdete v kategorii <a href="/neopreny/">neopreny</a>, další vybavení k vodě pak na stránce <a href="/vodni-sporty/">vodní sporty</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Tenká letní botička na zimní otužování, ve které nohy promrznou během pár minut.</li>'
          '<li>Bota o číslo větší, aby se snáz obouvala, do které pak při každém kroku proudí studená voda.</li>'
          '<li>Měkká ponožka bez podrážky na kamenitý vstup do moře, kde se snadno propíchne.</li>'
          '<li>Nákup ploutví a bot zvlášť, takže bota do kapsy ploutve nepasuje.</li>'
          '<li>Sušení na topení nebo na slunci, po kterém neopren ztvrdne a popraská.</li></ul>'
          '<h2>Obouvání a výměna</h2>'
          '<p>Přiléhavá bota se na suchou nohu obouvá ztuha. Pomůže ji nejprve shrnout jako ponožku a natáhnout postupně od špičky, nebo nohu i botu namočit. Za lem netahejte nehty, neopren se snadno natrhne. Botu je čas vyměnit, když se podrážka odlepuje, v patě se otevírá šev nebo materiál ztratil pružnost a už nepřiléhá. Malou trhlinku ve svršku lze zalepit lepidlem určeným na neopren, odlepenou podešev na kamenitém dně ale oprava dlouho nevydrží.</p>'
          '<p>Před koupí zvažte, kolikrát do roka botu obujete. Kdo jde k vodě jednou za léto, vystačí s jednoduchou botičkou. Pravidelný otužilec nebo potápěč, který vstupuje do vody každý týden, ocení pevnější podešev, kvalitnější švy a zip, protože obuv bude namáhat mnohem víc.</p>'
          '<h2>Jak o neopren pečovat</h2>'
          '<p>Po každém použití boty i ponožky propláchněte sladkou vodou, hlavně po moři nebo chlorovaném bazénu. Sůl a chlor materiál vysušují a zkracují jeho život. Sušte je obrácené naruby ve stínu a na vzduchu, ne na radiátoru ani na přímém slunci. Teplo a UV záření dělají neopren tvrdý a křehký. Když boty začnou zapáchat, pomůže speciální šampon na neopren nebo jemný prací prostředek bez bělidel. Do pračky a sušičky je nedávejte, pokud to výrobce výslovně nedovoluje. Zip občas propláchněte a namažte, aby ho sůl nezablokovala. Kdo se o neopren stará, vystačí s jedním párem několik sezón.</p>',
    faq=[
        ('Jak silné neoprenové ponožky na otužování?', 'Otužilci obvykle volí 5 mm a více. Tenčí ponožky chrání před kameny, ale v zimní vodě hřejí jen krátce.'),
        ('Jaký je rozdíl mezi neoprenovou ponožkou a botou?', 'Ponožka je tenká a měkká a nosí se do ploutví nebo pod jinou obuv. Bota má pevnou podrážku a chrání chodidlo i při chůzi po kamenech.'),
        ('K čemu je dělená špička?', 'Odděluje palec od ostatních prstů, takže noha lépe drží a má víc citu, což ocení hlavně surfaři. Kulatá špička je teplejší a obouvá se snáz.'),
        ('Mají neoprenové boty sedět těsně?', 'Přiléhavě, ale bez škrcení. Volná bota nabírá studenou vodu, příliš těsná zhorší prokrvení a nohy chladnou rychleji.'),
        ('Jakou botu do ploutví s otevřenou patou?', 'Neoprenovou botu s pevnou podešví, obvykle vyšší a se zipem. Velikost ploutve pak vybírejte podle obuté boty.'),
        ('Můžu neoprenové boty prát v pračce?', 'Jen pokud to výrobce povoluje. Bezpečnější je ruční praní ve vlažné vodě a sušení naruby ve stínu.'),
        ('Proč neoprenové boty zapáchají?', 'Uvnitř zůstává vlhko a pot. Pomůže důkladné proplachování, sušení naruby a občas šampon určený na neopren.'),
        ('Kde neoprenové boty a ponožky koupit?', 'Sporteka zobrazí nabídky několika českých obchodů. Nákup pak dokončíte na stránce prodejce, který vám vyhovuje.'),
    ])

# ------------------------------------------------------------------ esusy
NEW['esusy'] = dict(long=True,
    title='Ešusy: hliníkové, nerezové i titanové do přírody',
    desc='Ešusy z hliníku, nerezu i titanu, dvoudílné, trojdílné i vojenské. Jak vybrat materiál a objem, jak se o ešus starat a kde ho mají české e-shopy skladem.',
    intro='<p><strong>Ešus</strong> je hovorový název pro jídelní nádobu, kterou si lidé spojují s vojnou, skautem a trampováním. Jde o hrnec s víkem, které zároveň slouží jako pánvička nebo talíř, a se sklopným uchem nebo drátěnou rukojetí. Dnes se ešusy vyrábějí z hliníku, nerezové oceli i titanu, ve tvaru kulatém i oválném, jako jednoduché dvoudílné nádobí nebo jako sady, do kterých se vejde hrnek, miska a někdy i vařič s kartuší. Uvaříte v nich polévku, čaj, těstoviny i vajíčka na ohni.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů, takže hned vidíte, kde je ešus skladem, a nákup pak dokončíte v obchodě, který si vyberete. Najdete tu ešusy značek VAR, Yate, Nils Camp, Helikon-Tex, ' + B(('mfh', 'MFH')) + ' nebo King Camp. Ešusy patří do kategorie <a href="/kempingove-nadobi/">kempingové nádobí</a>, potřebné vybavení na vaření najdete mezi <a href="/varice-a-kartuse/">vařiči a kartušemi</a>.</p>',
    guide='<h2>Z čeho vybrat: hliník, nerez, nebo titan</h2>'
          '<p>Materiál rozhoduje o hmotnosti, o tom, jak rovnoměrně jídlo prohřeje, i o tom, jak se o ešus budete starat. Žádný není nejlepší na všechno, a proto má řada lidí doma dva: lehký na túry a odolný na chatu nebo k ohni.</p>'
          + T(['Materiál', 'Výhody', 'Na co dát pozor'], [
              ['Hliník neošetřený', 'lehký, levný, rychle a rovnoměrně vede teplo', 'reaguje s kyselými a slanými jídly, snadno se promáčkne'],
              ['Hliník eloxovaný', 'tvrdší povrch, méně reaguje s jídlem, lépe se myje', 'ochrannou vrstvu poškodí drátěnka a ostré náčiní'],
              ['Nerezová ocel', 'odolná, nereaguje s jídlem, vydrží oheň i drhnutí', 'těžší, teplo rozvádí hůř, jídlo se snáz připálí'],
              ['Titan', 'nejlehčí díky tenkým stěnám, pevný, nekoroduje', 'dražší, teplo drží v místě plamene, hodí se hlavně na vodu']]) +
          '<p>Rozdíly mají fyzikální základ. Hliník má hustotu asi 2,7 gramu na centimetr krychlový, titan asi 4,5 a ocel kolem 7,9. Titan tedy není lehčí než hliník jako materiál, ale je tak pevný, že stěny nádobí můžou být velmi tenké. Proto titanový ešus stejného objemu obvykle váží méně než hliníkový. Nevýhodou tenké stěny je, že teplo se nerozvede po dně a jídlo se v místě plamene připaluje. Na vaření vody, čaje a instantních jídel je titan výborný, na smažení a hustou omáčku méně.</p>'
          '<h2>Dvoudílný, trojdílný, nebo sada</h2>'
          '<ul><li><strong>Dvoudílný ešus:</strong> hrnec a víko, které poslouží jako pánvička nebo miska. Nejjednodušší a nejlehčí varianta pro jednoho.</li>'
          '<li><strong>Trojdílný ešus:</strong> navíc vnitřní nádoba nebo hrnek. Hodí se, když chcete současně vařit jídlo a mít kam nalít čaj.</li>'
          '<li><strong>Vojenský oválný ešus:</strong> plochý tvar, který se dobře vejde do batohu a přiléhá k zádům. Víko bývá s rukojetí a slouží jako pánev.</li>'
          '<li><strong>Kempingová sada:</strong> několik hrnců různých velikostí zasunutých do sebe, často s miskami a hrnky pro dva až čtyři lidi.</li>'
          '<li><strong>Hrnek s víčkem:</strong> nejmenší varianta pro toho, kdo jen ohřívá vodu na kávu a dehydrované jídlo.</li></ul>'
          '<h2>Jaký objem zvolit</h2>'
          '<p>Pro jednoho člověka, který si vaří polévku nebo ohřívá vodu, bývá dostatečný objem kolem jednoho litru. Pokud vaříte těstoviny nebo rýži, potřebujete víc místa, protože se musí vařit ve větším množství vody. Na dva lidi se vyplatí sáhnout po ešusu nebo sadě s alespoň jedním a půl litrem. Větší hrnec ale znamená víc hmotnosti a pomalejší ohřev na malém vařiči. Při výběru zkontrolujte, jestli výrobce uvádí objem po okraj, nebo užitný objem, protože plný ešus po okraj na vařiči přeteče.</p>'
          '<h2>Vaření na ohni, plynu a lihu</h2>'
          '<p>Ešus je dělaný pro otevřený oheň, ale i tam se vyplatí trocha opatrnosti. Plastové nebo silikonové části ucha a rukojeti do ohně nepatří a kovové úchyty se rozpálí natolik, že bez rukavice nebo hadru nejdou chytit. Hliník na příliš silném plameni nebo bez obsahu může zdeformovat, proto prázdný ešus nikdy nenechávejte na ohni. Na plynovém vařiči je důležité, aby šířka dna odpovídala hořáku, jinak se plameny derou ke stěnám a ohřívají spíš ucho než jídlo. Na lihových vařičích a na tabletách se dobře osvědčují nižší ešusy se širokým dnem. Kartuše, vařiče a stojánky najdete v kategorii <a href="/vareni-v-prirode/">vaření v přírodě</a>.</p>'
          '<p>Po vaření na ohni zůstane na vnější straně saze. Mnoho lidí je už neodstraňuje, protože tmavý povrch přijímá teplo lépe, ešus pak ale nosí v látkovém obalu nebo v igelitovém sáčku, aby neušpinil ostatní věci v batohu. Uvnitř ešusu se při přenášení dají schovat menší věci: kartuše, zapalovač, houbička nebo sáček s čajem. Že vybraná kartuše dovnitř opravdu vejde, si raději ověřte podle rozměrů obou výrobků.</p>'
          '<h2>Péče o hliníkový ešus</h2>'
          '<p>Neošetřený hliník není vhodný na dlouhé uchovávání kyselých a slaných jídel. Rajčatová omáčka, kysané zelí nebo jídlo s octem nechaná v ešusu přes noc mohou povrch zbarvit a jídlu dodat kovovou pachuť. Uvařit v něm takové jídlo a hned ho sníst ale běžně nevadí. Eloxovaný hliník má povrch zpevněný oxidickou vrstvou, která je tvrdší a s jídlem reaguje méně. Tu je potřeba chránit: myjte ho houbičkou, ne drátěnkou ani pískem, a k míchání používejte dřevěnou nebo plastovou lžíci.</p>'
          '<ul><li>Hliníkové ešusy nedávejte do myčky. Silné mycí prostředky povrch zmatní a zbarví.</li>'
          '<li>Po umytí ešus vysušte a skladujte otevřený, aby se uvnitř nedrželo vlhko.</li>'
          '<li>Připálené zbytky namočte do teplé vody a teprve pak opatrně odstraňte.</li>'
          '<li>Promáčknuté dno vyrovnejte co nejdřív, nerovná nádoba stojí na vařiči nejistě.</li></ul>'
          '<h2>Nerez a titan v praxi</h2>'
          '<p>Nerezový ešus je nejodolnější volba pro toho, kdo vaří hlavně na ohni, drhne nádobí pískem u potoka a nechce řešit, jestli nádobu nepoškodí. Snese i jídlo, které v ní zůstane do druhého dne. Je ale znatelně těžší a jídlo se v něm připaluje, pokud nemícháte. Titan se po zahřátí zbarvuje do modrých a zlatavých odstínů, které nejsou vada, ale přirozená oxidace povrchu. Titanový ešus je oblíbený u lidí, kteří počítají každý gram, například na dálkových trasách, kde se vaří hlavně voda na <a href="/outdoorova-strava/">dehydrovanou stravu</a> a kávu.</p>'
          '<h2>Na co se dívat při koupi</h2>'
          '<ul><li><strong>Ucho a rukojeť:</strong> musí se dát zajistit, aby se hrnec při nalévání nepřevrátil. Sklopná ucha šetří místo v batohu.</li>'
          '<li><strong>Víko:</strong> těsně dosedající víko zkrátí dobu ohřevu a ušetří palivo. Otvory na scezení oceníte u těstovin.</li>'
          '<li><strong>Stupnice objemu:</strong> vyražená ryska uvnitř pomáhá odměřit vodu pro dehydrované jídlo.</li>'
          '<li><strong>Tvar:</strong> kulatý ešus se hodí na vařič, oválný lépe sedí v batohu a k ohni.</li>'
          '<li><strong>Obal:</strong> látkový vak chrání batoh před sazemi a tlumí cinkání.</li></ul>'
          '<h2>Jak v ešusu vařit úsporně</h2>'
          '<p>Na túře se nosí každý gram paliva, a tak se vyplatí vařit chytře. Víko nechávejte nasazené, voda s ním dosáhne varu rychleji a vařič spotřebuje méně plynu. Hořák postavte do závětří nebo kolem něj dejte ochranu proti větru, ale nikdy ne tak, aby se přehřívala kartuše. Těstoviny a rýži stačí krátce povařit a pak je nechat dojít pod víkem mimo plamen. Vodu na kávu a na dehydrované jídlo ohřejte najednou a rozlijte, než ji začnete ohřívat podruhé. Ve studeném počasí trvá vaření déle a kartuše ztrácí tlak, proto si ji nechte do rána ve spacím pytli nebo v kapse.</p>'
          '<h2>Ešus na tábor a pro děti</h2>'
          '<p>Na letní tábor nebo do skautského oddílu se hodí jednoduchý ešus s pevným uchem a s víčkem, které dítě udrží v ruce i s horkým jídlem. Pomůže, když má nádobí výrazné označení nebo jméno, protože u výdeje jídla stojí vedle sebe desítky stejných ešusů. Děti by měly vědět, že kovové ucho se nad ohněm rozpálí a že se plný ešus nenosí přes cestu, kde se běhá. Hliníkový ešus je pro malé ruce lehčí, nerezový zase vydrží pády na kameny a drhnutí pískem u potoka.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Prázdný hliníkový ešus zapomenutý na plameni, který se zdeformuje.</li>'
          '<li>Titanový hrnek na smažení, ve kterém se jídlo připálí v jednom místě.</li>'
          '<li>Kyselé jídlo ponechané v neošetřeném hliníku přes noc.</li>'
          '<li>Drátěnka na eloxovaném povrchu, která naruší ochrannou vrstvu.</li>'
          '<li>Ešus příliš malý na to, co v něm chcete vařit, a voda vykypí do hořáku.</li></ul>'
          '<h2>Mytí ešusu v přírodě</h2>'
          '<p>Nejjednodušší je ešus vytřít kouskem pečiva nebo trávou a vypláchnout trochou vody. Saponát ani zbytky jídla nepatří přímo do potoka nebo jezera, i když jde o přípravek označený jako šetrný. Vodu na mytí naberte do ešusu, umyjte ho kousek dál od břehu a použitou vodu vylijte do země. Na delší výpravě se hodí malá houbička, kterou po umytí vyždímáte a uložíte do sáčku. Doma pak ešus umyjte důkladně a nechte ho vyschnout, než ho zabalíte k ostatní výbavě.</p>'
          '<h2>K čemu se ešus hodí doma i na cestě</h2>'
          '<p>Ešus není jen na vandr. Slouží jako nouzové nádobí na chatě, když vypadne proud a vaří se na plynové bombě, jako miska pro psa na výletě nebo jako součást pohotovostního batohu. Na rybách a na lovu v něm uvaříte čaj bez nutnosti nosit celou kuchyň, další výbavu pro lovce najdete v kategorii <a href="/lovecke-vybaveni/">lovecké vybavení</a>. K ešusu se dobře hodí <a href="/outdoorove-noze-a-multitoola/">nůž nebo multitool</a>, kovová lžíce a lahev na vodu z kategorie <a href="/lahve-a-termosky/">lahve a termosky</a>. Pokud chcete mít teplý čaj po ruce celý den, uvařte ho ráno v ešusu a přelijte do termosky.</p>',
    faq=[
        ('Je lepší ešus hliníkový, nebo nerezový?', 'Hliníkový je lehčí a rovnoměrně prohřeje jídlo, nerezový je těžší, ale odolnější a nereaguje s kyselými jídly. Na túry se víc nosí hliník, na oheň a chatu nerez.'),
        ('Můžu v hliníkovém ešusu vařit kyselá jídla?', 'Uvařit a hned sníst je běžně v pořádku. Kyselé nebo slané jídlo ale v neošetřeném hliníku nenechávejte stát dlouho, povrch se zbarví a jídlo může chutnat kovově.'),
        ('Proč je titanový ešus tak lehký?', 'Titan je velmi pevný, takže stěny mohou být tenké. Díky tomu titanový ešus obvykle váží méně než hliníkový stejného objemu, i když titan sám je hustší.'),
        ('Jaký objem ešusu stačí pro jednoho?', 'Na polévku, čaj a dehydrované jídlo obvykle stačí kolem jednoho litru. Na těstoviny nebo vaření pro dva se hodí 1,5 litru a víc.'),
        ('Můžu ešus dát do myčky?', 'Hliníkový ne, mycí prostředky ho zmatní a zbarví. Nerez myčku obvykle snese, ale vždy se řiďte pokyny výrobce.'),
        ('Co je dvoudílný a trojdílný ešus?', 'Dvoudílný má hrnec a víko, které slouží jako pánvička. Trojdílný přidává ještě vnitřní nádobu nebo hrnek.'),
        ('Proč se titanový ešus zbarvil?', 'Modré a zlatavé zbarvení je přirozená oxidace povrchu po zahřátí. Funkci ani bezpečnost nádoby neovlivňuje.'),
        ('Kde ešus koupit?', 'Na Sportece vidíte nabídky různých českých obchodů vedle sebe. Ešus pak objednáte přímo u prodejce, kterého si vyberete.'),
    ])
