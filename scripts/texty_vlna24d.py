"""sporteka.cz — wave 24d (5. 11. 2026): long texts for lyzarske-termopradlo, jogove-pomucky, skialpove-boty, rybarske-lode-a-elektronika.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-termopradlo
NEW['lyzarske-termopradlo'] = dict(long=True,
    title='Lyžařské termoprádlo: merino, syntetika, velikosti',
    desc='Lyžařské termoprádlo pro dospělé i děti: trička, spodky, sety a kukly z merina a syntetiky. Jak vybrat vrstvu pod bundu a porovnat obchody.',
    intro='<p>Termoprádlo je vrstva, kterou na svahu nikdo nevidí, a přesto rozhoduje o tom, jestli vám bude celý den příjemně. Leží přímo na kůži, odvádí pot od těla a brání tomu, aby se po výjezdu vlekem zmáčené tričko změnilo v ledový obklad. Na Sportece porovnáváme nabídky českých obchodů u lyžařských triček, spodků, kompletních setů, kukel a dětských souprav z merina, syntetiky i jejich směsí.</p>'
          '<p>V kategorii najdete značky ' + B(('wedze', 'Wedze'), ('siroko', 'Siroko'), ('northfinder', 'Northfinder'), ('kari-traa', 'Kari Traa'), ('swedemount', 'Swedemount'), ('ulvang', 'Ulvang'), ('viking', 'Viking'), ('odlo', 'Odlo')) +
          '. Vrchní vrstvy hledejte mezi <a href="/lyzarske-bundy/">lyžařskými bundami</a> a <a href="/lyzarske-kalhoty/">kalhotami</a>, k nohám patří <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, ke krku <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>.</p>',
    guide='<h2>Co termoprádlo na lyžích skutečně dělá</h2>'
          '<p>Při lyžování se střídají dvě krajnosti. V jízdě tělo vyrábí teplo a potí se, na vleku nebo lanovce sedíte a vlhkost se začne rychle ochlazovat. Základní vrstva má pot odvést od pokožky do dalších vrstev, kde se může odpařit. Bavlněné tričko to nezvládne: nasákne, ztěžkne a dlouho schne. Proto se pod lyžařské oblečení nosí funkční materiály, které vodu nedrží u kůže.</p>'
          '<p>Termoprádlo samo o sobě moc neohřeje. Hřeje vzduch uzavřený mezi vlákny a mezi jednotlivými vrstvami oblečení, a termoprádlo má hlavně zajistit, aby ten vzduch zůstal suchý. Proto záleží na přiléhavosti: prádlo musí ležet na těle, jinak se vlhkost nepřenáší a vzniká studený prostor.</p>'
          '<h2>Jaké druhy lyžařského termoprádla najdete</h2>'
          + T(['Typ', 'Popis', 'Hodí se pro'], [
              ['Tričko s dlouhým rukávem', 'nejčastější horní díl, někdy s rolákem nebo zipem u krku', 'celodenní sjezdování, základ každé sestavy'],
              ['Tričko s krátkým rukávem', 'lehčí vrstva, často z merina', 'jarní lyžování, aktivní jízda, saunování pod bundou'],
              ['Spodky dlouhé', 'přiléhavé nohavice po kotník', 'téměř všechny zimní dny'],
              ['Set (tričko + spodky)', 'sladěné díly od jednoho výrobce', 'začátečníci, děti, dárky'],
              ['Kukla a nákrčník', 'tenká vrstva pro hlavu a krk pod helmu', 'mrazivé dny, závody, běžky'],
              ['Dětský komplet', 'měkčí střih, často bez výrazných švů', 'školní lyžáky a rodinná lyžování'],
              ['Zateplená vrstva', 'tlustší vlákno nebo počesaná vnitřní strana', 'dlouhé stání, extrémní mráz, pomalá jízda']]) +
          '<h2>Merino, syntetika nebo směs</h2>'
          '<p>Nejčastější otázka u termoprádla zní, jestli sáhnout po vlně, nebo po umělých vláknech. Obě varianty mají svůj smysl a rozhoduje styl lyžování.</p>'
          '<h3>Merino</h3>'
          '<p>Merino je jemná vlna z ovcí stejnojmenného plemene. Vlákna jsou tenká, takže nedrásají, a vlna pojme značné množství vlhkosti, aniž by na dotek působila mokře. Další výhodou je, že merino méně zapáchá, takže prádlo vydrží víc dní na horách bez praní. Nevýhodou je menší odolnost proti oděru a pomalejší schnutí než u syntetiky. Podrobnosti o materiálu najdete v kategorii <a href="/merino-pradlo/">merino prádlo</a>.</p>'
          '<h3>Syntetika</h3>'
          '<p>Polyester a polyamid schnou rychle, vydrží opakované praní a bývají pružné. Hodí se pro sportovnější jízdu, kdy se hodně potíte a prádlo potřebuje rychle uvolnit vlhkost. Slabinou je pach: syntetická vlákna zachycují bakterie, proto po náročném dni prádlo vyperte, případně zvolte typ s antibakteriální úpravou.</p>'
          '<h3>Směsi a kombinované konstrukce</h3>'
          '<p>Hodně výrobců šije prádlo ze směsi merina a syntetiky. Vlna bývá uvnitř u kůže a syntetika vně, takže prádlo kombinuje komfort a odolnost. Některé modely mají odlišné zóny: hustší pletení na hrudi a zádech, prodyšnější síťovina v podpaží a v pase. Takové prádlo je dobré pro sportovní lyžaře, kteří chtějí dobře regulovat teplotu.</p>'
          '<h2>Tloušťka a gramáž</h2>'
          '<p>Tloušťka prádla se obvykle uvádí v gramech na čtvereční metr. Tenké prádlo (zhruba do 150 g/m²) je vhodné na jarní lyžování a aktivní jízdu, střední váha (přibližně 200 g/m²) na typický zimní den a tlustší (od 250 g/m² výš) pro mráz a pomalé lyžování. Přesné hranice se mezi značkami liší, proto porovnávejte popisy a ne jen čísla.</p>'
          '<ul><li><strong>Tenké prádlo:</strong> pro rychlou jízdu, zahřátí při chůzi do kopce a teplé dny.</li>'
          '<li><strong>Střední váha:</strong> univerzální volba pro většinu lyžařů.</li>'
          '<li><strong>Tlusté prádlo:</strong> pro děti na vleku, začátečníky a ty, kdo rychle mrznou.</li></ul>'
          '<p>Pamatujte, že termoprádlo je jen jedna z vrstev. Mezi ním a bundou může být ještě <a href="/fleecove-mikiny/">fleecová mikina</a> nebo <a href="/funkcni-mikiny/">funkční mikina</a>.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Prádlo má sedět jako druhá kůže, ale nesmí škrtit. Při předklonu v jízdě se nesmí vyhrnout zády nahoru a nohavice nesmí vyjet nad boty. Vyberte velikost podle tabulky výrobce, kde se obvykle měří obvod hrudníku, pasu a boků. Pokud jste mezi dvěma velikostmi, bývá lepší menší u syntetiky a odpovídající u merina, které se při nošení trochu povolí.</p>'
          '<p>Ženy ocení střih navržený pro ženské tělo, který nezlobí v ramenou a na hrudi. Muži si často pochvalují delší záda. Prádlo s plochými švy nedře v místech, kde se tře o batoh, popruhy nebo lyžařské boty.</p>'
          '<h2>Termoprádlo pro děti</h2>'
          '<p>Děti rychleji chladnou, protože mají menší tělo a větší povrch vzhledem k objemu. Dětské prádlo by mělo být měkké, bez dráždivých štítků a s dostatečně dlouhými rukávy a nohavicemi. Nekupujte o dvě velikosti větší na vyrůstání, volné prádlo nehřeje. Praktické jsou dvoudílné sady, které se snadno obléknou. K lyžování patří i <a href="/detske-lyze/">dětské lyže</a>, <a href="/lyzarske-helmy/">helma</a> a <a href="/lyzarske-rukavice/">rukavice</a>.</p>'
          '<h2>Kukla, nákrčník a doplňky z funkčních materiálů</h2>'
          '<p>Tenká kukla pod helmou nebo funkční nákrčník dokážou udělat víc než další vrstva na trupu, protože hlava a krk bývají vystavené větru. V nabídce se objevují i termoaktivní kukly. Dbejte, aby neměla příliš silný šev u očí a dobře seděla pod helmu a <a href="/lyzarske-bryle/">lyžařské brýle</a>.</p>'
          '<h2>Jak prádlo pečovat</h2>'
          '<ul><li>Perte podle štítku, obvykle na nižší teplotu a s jemným prostředkem bez aviváže.</li>'
          '<li>Aviváž ucpává strukturu vlákna a snižuje schopnost odvádět vlhkost.</li>'
          '<li>Merino perte šetrným programem na vlnu, nesušte v sušičce a nevěšte na topení.</li>'
          '<li>Syntetiku neždímejte vysokými otáčkami a nežehlete.</li>'
          '<li>Po lyžování nenechávejte prádlo vlhké v tašce, vyvěste ho na vzduch.</li></ul>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Bavlněné tričko pod lyžařskou bundou. Po první zpocené jízdě je z něj studený obklad.</li>'
          '<li>Příliš volná velikost. Prádlo musí být u těla, jinak nefunguje.</li>'
          '<li>Dvě tlusté vrstvy místo jedné tenké a jedné střední. Víc látky neznamená víc tepla.</li>'
          '<li>Prádlo bez náhradního kusu na vícedenní výlet.</li>'
          '<li>Nošení stejného prádla příliš dlouho bez praní, i když je merino.</li></ul>'
          '<h2>Výběr podle typu lyžaře</h2>'
          '<ul><li><strong>Rekreační sjezdař:</strong> střední tloušťka z merina nebo směsi, dlouhé rukávy a spodky.</li>'
          '<li><strong>Sportovní jezdec:</strong> tenčí syntetika nebo kombinovaná konstrukce s prodyšnými zónami.</li>'
          '<li><strong>Freerider a skialpinista:</strong> lehké, rychle schnoucí prádlo, protože výstupy znamenají velké pocení, více v kategorii <a href="/skialpinismus/">skialpinismus</a>.</li>'
          '<li><strong>Běžkař:</strong> tenké a velmi prodyšné, viz <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</li>'
          '<li><strong>Dítě:</strong> měkký set s dlouhými rukávy a nohavicemi.</li>'
          '<li><strong>Zimomřivý:</strong> tlustší vrstva, kukla a nákrčník.</li></ul>'
          '<h2>Zipy, švy a drobnosti, které rozhodnou</h2>'
          '<p>U prádla stráveného celý den pod bundou záleží na detailech. Ploché švy se nezařezávají pod popruhy batohu a nedřou na ramenou. Krátký zip u krku umožní větrání po výstupu a zvedne límec při větru. Palcové otvory v rukávech drží manžetu na místě a chrání zápěstí mezi rukavicí a bundou. Zesílená kolena a lokty se hodí lyžařům, kteří častěji padají nebo klečí při upínání. Dámské spodky mívají vyšší pas, aby záda zůstala v teple při předklonu na lyžích.</p>'
          '<p>Pokud prádlo kupujete jako dárek nebo pro dítě, vyberte raději set od jednoho výrobce. Díly mají stejný střih i materiál, a když se jedna velikost nehodí, je snazší ji vyměnit. Před koupí si ověřte podmínky vrácení, hlavně u prádla, které se obtížně zkouší doma.</p>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Nabídku tvoří převážně pánská a dámská trička a spodky, dětské soupravy a několik kukel. Nejvíc modelů má Wedze, tedy značka obchodu Decathlon, následují Siroko, Northfinder, Kari Traa a Swedemount. Menší zastoupení mají Ulvang, Quechua, Viking, Montane, Odlo nebo Silvini. Pokud hledáte obecnější prádlo bez lyžařského zaměření, zkuste kategorii <a href="/termopradlo/">termoprádlo</a> nebo <a href="/merino-tricka/">merino trička</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Ve výpisu porovnáte nabídky několika českých obchodů vedle sebe. Filtrujte podle značky, velikosti a pohlaví a čtěte popis materiálu: u merina sledujte podíl vlny, u syntetiky složení vlákna. U sad zkontrolujte, zda obsahují oba díly. Poštovné, dostupnost velikostí a lhůty dodání se liší obchod od obchodu, takže se vyplatí otevřít detail nabídky. Pro celkovou lyžařskou výbavu navštivte také <a href="/lyzarske-obleceni/">lyžařské oblečení</a> a <a href="/lyzarske-doplnky/">lyžařské doplňky</a>.</p>',
    faq=[
        ('Jaké termoprádlo je nejlepší pod lyžařskou bundu?', 'Záleží na stylu jízdy. Pro rekreační lyžování se osvědčuje střední tloušťka z merina nebo ze směsi merina a syntetiky. Sportovní jezdci, kteří se hodně potí, často preferují tenčí syntetiku, která rychle schne. Důležitější než materiál je správná velikost: prádlo musí přiléhat k tělu.'),
        ('Je lepší merino, nebo syntetika?', 'Merino méně zapáchá a příjemně hřeje i při vlhkosti, ale je méně odolné a pomaleji schne. Syntetika schne rychle a vydrží víc praní, ale zapáchá dřív. Mnoho lyžařů proto kupuje obojí nebo si vybere kombinovaný materiál, který spojuje výhody obou.'),
        ('Má být termoprádlo těsné, nebo volné?', 'Má přiléhat, ale nemá omezovat pohyb ani škrtit. Volné prádlo nepřenáší vlhkost od kůže a vytváří studená místa. Při předklonu a dřepu se prádlo nesmí vyhrnovat a nohavice nesmí vyjet nad lyžařskou botu.'),
        ('Kolik vrstev oblečení mám na lyže nosit?', 'Nejběžnější sestava jsou tři vrstvy: termoprádlo u kůže, izolační vrstva (fleece nebo lehká péřovka) a svrchní bunda s membránou. Za teplejších dní se izolační vrstva vynechá. Při velkém mrazu nebo dlouhém stání se přidá další tenká vrstva nebo tlustší prádlo.'),
        ('Jak často termoprádlo prát?', 'Syntetiku vyperte po každém náročném dni, protože zachytává pach. Merino vydrží více dní bez praní, stačí ho větrat. Při praní používejte jemný prostředek bez aviváže a nízkou teplotu podle štítku.'),
        ('Dá se nosit bavlněné tričko pod termoprádlo?', 'Nedoporučuje se. Bavlna nasákne potem a dlouho schne, takže zruší efekt funkční vrstvy. Pokud chcete vrstvit, dejte na tělo funkční prádlo a až přes něj další oblečení.'),
        ('Jaké termoprádlo koupit dítěti na lyžák?', 'Měkký set s dlouhými rukávy a nohavicemi, bez drsných švů a štítků. Kupujte správnou velikost, ne větší na vyrůstání, protože volné prádlo nehřeje. Pro týdenní kurz se hodí dva sety, aby jeden mohl schnout.'),
        ('Potřebuji speciální termoprádlo pro ženy?', 'Dámské střihy respektují ženskou postavu v ramenou, hrudi a bocích, takže lépe sedí a nevyhrnují se. Pokud vám padne unisex nebo pánský střih, můžete ho nosit, jen kontrolujte přiléhavost.'),
        ('Je kukla pod helmu nutná?', 'Není povinná, ale v mrazu se výrazně vyplatí. Tenká funkční kukla nebo nákrčník chrání krk a uši a snižuje tlak helmy na čelo. Důležité je, aby neměla tlusté švy a dobře seděla pod helmou i brýlemi.'),
        ('Čím se liší lyžařské termoprádlo od běžného funkčního?', 'Lyžařské prádlo bývá delší v rukávech a nohavicích, často mírně silnější a je navržené pro statické chvíle na vleku i pohyb při jízdě. Prádlo na běh nebo kolo je obvykle tenčí a prodyšnější. V chladném počasí se ale obě kategorie dají kombinovat.'),
    ])

# ------------------------------------------------------------------ jogove-pomucky
NEW['jogove-pomucky'] = dict(long=True,
    title='Jógové bloky, popruhy a kola: výběr a péče',
    desc='Jógové bloky, popruhy, kolečka a zafu polštáře. Jak vybrat materiál, rozměr a tvrdost pro cvičení a porovnat nabídky českých obchodů.',
    intro='<p>Jógové pomůcky nejsou berličky pro začátečníky, jak se někdy říká. Blok přiblíží podlahu rukám, popruh pomůže spojit dlaně za zády a bolster podepře tělo v uvolněných pozicích, takže se můžete soustředit na dech a ne na bolavá záda. Správně zvolená pomůcka pozici zpřesní a zpříjemní, ať cvičíte doma, ve studiu nebo na cestách. Na Sportece porovnáváme nabídky českých obchodů u jógových bloků, popruhů, kol, zafu polštářů a souvisejících doplňků.</p>'
          '<p>Najdete zde značky ' + B(('merco', 'Merco'), ('sportago', 'Sportago'), ('sharp-shape', 'Sharp Shape'), ('xtrexo', 'Xtrexo'), ('manduka', 'Manduka'), ('kimjaly', 'Kimjaly'), ('casall', 'Casall'), ('domyos', 'Domyos')) +
          '. Pod pomůcky patří <a href="/joga-a-podlozky/">jógové podložky</a>, pro širší výběr se podívejte do kategorie <a href="/joga-a-pilates/">jóga a pilates</a> a na <a href="/pilates-pomucky/">pilates pomůcky</a>.</p>',
    guide='<h2>K čemu jógové pomůcky slouží</h2>'
          '<p>Pomůcky nahrazují flexibilitu, kterou ještě nemáte, nebo přidávají oporu tam, kde se tělo potřebuje uvolnit. Dobrá pomůcka umožní držet pozici správně a bezpečně, aniž byste kompenzovali pohyb zvednutými rameny nebo zakulacenými zády. Zkušení jogíni je používají stejně často jako začátečníci, třeba při jemné restorativní józe nebo dlouhém držení pozic v yin józe.</p>'
          '<h2>Přehled pomůcek</h2>'
          + T(['Pomůcka', 'K čemu je', 'Typické použití'], [
              ['Jógový blok (kostka)', 'zkracuje vzdálenost k podlaze, dává oporu', 'trojúhelník, půlměsíc, ryba, podpora pánve'],
              ['Popruh', 'prodlužuje paže a pomáhá spojit ruce nebo nohy', 'předklony, pozice holubice, protažení ramen'],
              ['Bolster', 'dlouhý polštář pod záda nebo kolena', 'restorativní jóga, relaxace, těhotenská jóga'],
              ['Zafu a polštáře na meditaci', 'zvyšují sed a uvolňují kyčle', 'meditace a dechová cvičení'],
              ['Jógové kolo', 'otevírá hrudník a prohlubuje záklony', 'zkušenější cvičenci, uvolnění zad'],
              ['Deka', 'zvyšuje pohodlí a drží teplo', 'závěrečná relaxace, sedy'],
              ['Podložka pod kolena nebo hlavu', 'tlumí tlak na kloubech', 'kleky, stoje na hlavě pod dohledem učitele']]) +
          '<h2>Jógové bloky</h2>'
          '<p>Blok je nejuniverzálnější pomůcka. Dá se položit na tři výšky: nízko, středně nebo naležato na nejvyšší hranu, takže jedním kusem pokryjete široké spektrum pozic. Nejčastěji se používá při stoji trojúhelníku, kdy blok zvedne podlahu k ruce, nebo pod pánev v sedu na zemi.</p>'
          '<ul><li><strong>Pěnový blok (EVA):</strong> lehký, levnější, příjemně měkký. Hodí se pro začátečníky a pro cvičení na cestách. Při dlouhodobém tlaku se může stlačit.</li>'
          '<li><strong>Korkový blok:</strong> těžší, tvrdší a stabilnější, nešmýká se. Dobře se hodí do pozic, kde na něj přenášíte váhu.</li>'
          '<li><strong>Dřevěný blok:</strong> nejtvrdší, pevný a dlouhověký, ale může tlačit a je hlučnější.</li>'
          '<li><strong>Recyklovaná pěna nebo kombinace:</strong> volba pro ty, kdo hledají kompromis mezi cenou a trvanlivostí.</li></ul>'
          '<p>Běžný rozměr bloku je zhruba 23 × 15 × 7,5 cm, ale na trhu najdete i větší a menší varianty. Menší bloky se hodí k dětem a drobnějším cvičencům, větší k těm, kdo mají delší paže nebo potřebují větší opěrnou plochu. Pokud cvičíte doma pravidelně, pořiďte si dva bloky, protože řada pozic využívá oba.</p>'
          '<h2>Jógový popruh</h2>'
          '<p>Popruh vypadá jako obyčejný pásek, ale umí hodně. Prodlouží vaši paži při předklonu, takže můžete zachytit chodidlo a nemusíte shrbit záda. Při protažení ramen ho držíte oběma rukama za hlavou a postupně zkracujete vzdálenost. Dobře poslouží i při stabilizaci kolen a kotníků.</p>'
          '<ul><li><strong>Délka:</strong> nejčastěji kolem dvou metrů, delší (okolo tří metrů) vyhovuje vyšším cvičencům nebo náročnějším pozicím.</li>'
          '<li><strong>Zapínání:</strong> kovová D-spona se dobře utahuje, plastová přezka je lehčí, ale někdy povolí. Existují i popruhy se smyčkami, bez spony.</li>'
          '<li><strong>Materiál:</strong> bavlna je příjemná na dotek a nesklouzává, polyesterové popruhy jsou lehčí a snáz se perou.</li>'
          '<li><strong>Šířka:</strong> široký popruh se méně zarývá do kůže.</li></ul>'
          '<h2>Bolstery a zafu</h2>'
          '<p>Podrobnosti o výběru zafu a bolsterů najdete v kategorii <a href="/meditace/">meditace</a>. Bolster je válcovitý nebo plochý polštář. Podkládá se pod záda při pozicích s otevřeným hrudníkem, pod kolena při ležení na zádech nebo pod hrudník při předklonech. Využívá se hlavně ve zklidňující józe, při uvolnění po náročném dni a v těhotenství, kdy pomáhá najít pohodlnou polohu. Plnivo bývá z bavlny, pohanky nebo pěny; pohanka se přizpůsobí tělu, ale je těžší a hlučnější.</p>'
          '<p>Zafu je kulatý polštář na meditační sed. Zvedne pánev nad kolena, takže se páteř narovná bez námahy. Vyberte výšku podle ohebnosti kyčlí: nižší pro pohyblivé, vyšší pro ty, kdo mají pocit, že kolena visí. Samostatný sedák na meditaci potřebuje pevné plnivo, které se příliš neproleží. Širší výběr meditačních polštářů najdete v kategorii <a href="/meditace/">meditace</a>.</p>'
          '<h2>Jógové kolo</h2>'
          '<p>Jógové kolo je pevný prstenec, o který se opřete zády a otevřete hrudník. Může pomoci při uvolnění ztuhlých zad, nenahrazuje ale radu lékaře či fyzioterapeuta. Začínejte pomalu a pod dohledem zkušeného učitele, protože kolo prohlubuje záklony a při unáhleném použití by přetížilo bederní část. Kolo se vyrábí z plastu s měkkým povrchem nebo z korku a bambusu.</p>'
          '<h2>Jak vybrat správnou pomůcku</h2>'
          '<ul><li><strong>Začátečník:</strong> sada blok a popruh. Pěnový blok stačí, popruh vezměte aspoň dva metry dlouhý.</li>'
          '<li><strong>Pokročilý cvičenec:</strong> dva bloky, bolster a případně kolo na uvolnění zad.</li>'
          '<li><strong>Restorativní a yin jóga:</strong> bolster, deka a polštář, protože pozice trvají několik minut.</li>'
          '<li><strong>Meditace:</strong> zafu nebo sedák, ke kterému se hodí podložka pod kolena.</li>'
          '<li><strong>Těhotenská jóga:</strong> větší bolster, bloky a popruh. O vhodnosti pozic se poraďte s lékařem a certifikovaným učitelem.</li>'
          '<li><strong>Cestování:</strong> skládací nebo lehké pěnové pomůcky.</li></ul>'
          '<h2>Materiály a ekologie</h2>'
          '<p>Většina pomůcek se dělá z pěny EVA, korku, bavlny nebo dřeva. Korek je přírodní a neklouže, ale bývá těžší a dražší. Bavlněné povrchy a plnivo z pohanky jsou příjemné, ale nelze je prát v pračce při vysoké teplotě. Pokud vás zajímají nezávadné materiály, hledejte popis na stránce produktu: výrobce často uvádí, zda pěna neobsahuje ftaláty a zda je povrch bez zápachu.</p>'
          '<h2>Péče o pomůcky</h2>'
          '<ul><li>Pěnový a korkový blok otřete vlhkým hadříkem s trochou jemného mýdla.</li>'
          '<li>Dřevěný blok jen otřete suchou nebo lehce navlhčenou utěrkou, nenamáčejte.</li>'
          '<li>Popruh z bavlny lze prát na šetrný program, vlhký nechte vyschnout rozložený.</li>'
          '<li>Potah bolsteru pravidelně vyperte podle štítku a plnivo vyvětrejte.</li>'
          '<li>Pomůcky neskladujte na přímém slunci ani u topení, protože se pěna deformuje.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Používat blok jako oporu proti bolesti. Pomůcka má pozici zpříjemnit a zpřesnit, ne zakrýt varovný signál těla.</li>'
          '<li>Kupovat příliš měkký blok pro pozice, kde na něj přenášíte váhu.</li>'
          '<li>Utahovat popruh příliš silně kolem kloubů.</li>'
          '<li>Zapomenout na protiskluz: pomůcky stojí na podložce, takže ta nesmí kloužat.</li>'
          '<li>Cvičit s kolem bez zahřátí a bez znalosti techniky.</li></ul>'
          '<h2>Pomůcky pro konkrétní pozice</h2>'
          '<p>Blok pod rukou při stoji trojúhelníku zvedne podlahu a umožní otevřít hruď bez přetahování zad. V pozici holubice poslouží pod pánví, aby se kyčle neprotáčely. Při mostu se blok vkládá pod křížovou kost a svaly na zádech se mohou uvolnit. Popruh obepnutý kolem chodidla v předklonu v sedu dovolí narovnat záda a dýchat do hrudníku. Při protažení ramen v pozici kravské hlavy spojí popruh dlaně, i když se prsty nedotknou. Bolster pod kolena při ležení na zádech může uvolnit bederní oblast a pomoci zklidnit dech.</p>'
          '<h2>Pro koho se pomůcky hodí</h2>'
          '<p>Pomůcky ocení lidé, kteří sedí celý den u počítače a mají ztuhlé kyčle, sportovci při regeneraci po tréninku, starší cvičenci s omezenější pohyblivostí i těhotné ženy po konzultaci s lékařem. Učitelé jógy je používají při výuce a při individuální korekci pozic. Pomůcky také vytvářejí příjemný rituál: když si připravíte blok, popruh a deku, tělo i mysl se naladí na klidnou praxi.</p>'
          '<h2>Jak často a jak dlouho cvičit s pomůckami</h2>'
          '<p>Pomůcky nemají předepsaný limit. Při aktivní józe je používejte tak dlouho, dokud pozice bez nich nezvládnete s čistým dechem a rovnou páteří, a klidně i dál, pokud vám dělají dobře. Při restorativních pozicích se zůstává tři až deset minut a pomůcky zajišťují, že tělo nebolí. Pokud při držení pozice cítíte brnění, ostrou bolest nebo tlak na kloub, uvolněte ji a upravte výšku opory. Nechte se vést tělem a v případě pochybností se poraďte s učitelem.</p>'
          '<h2>Co je v kategorii skutečně k dispozici</h2>'
          '<p>Nejvíc kusů mají české značky Merco a Sportago, následuje Sharp Shape a Xtrexo. Prémiové linie představuje Manduka, dále Kimjaly, Casall nebo Domyos. Kromě bloků a popruhů tu najdete jógová kola z korku i plastu, zafu a sedáky na meditaci, pěnové válce a v několika případech i sady, které kombinují více pomůcek. Pokud hledáte posilovací nebo regenerační náčiní, zkuste <a href="/fitness-pomucky/">fitness pomůcky</a> nebo <a href="/fitness/">fitness</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Ve výpisu porovnáte nabídky několika obchodů a vidíte i variantní barvy a rozměry. U bloků sledujte rozměr a hmotnost, u popruhu délku a typ spony, u bolsteru průměr a plnivo. Zdroj zboží se mění, takže před objednávkou ověřte dostupnost a dodací lhůtu v detailu nabídky. K cvičení se hodí i <a href="/sportovni-ponozky/">sportovní ponožky</a> nebo <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>',
    faq=[
        ('Potřebuje začátečník v józe blok a popruh?', 'Není to nutné, ale pomůžou. Blok přiblíží podlahu, když se nedotknete rukama, a popruh umožní zachytit chodidlo bez shrbení. Díky tomu se pozice naučíte správně a nezvyknete si na kompenzace. Pro první měsíce stačí jeden blok a popruh.'),
        ('Jaký blok je lepší, pěnový, nebo korkový?', 'Pěnový je lehký a měkčí, hodí se pro začátečníky a cestování. Korkový je těžší, stabilnější a nešmýká se, takže ho ocení ti, kdo na něj přenášejí váhu. Dřevěný je nejtvrdší a vydrží nejdéle. Vyberte podle způsobu cvičení.'),
        ('Jak dlouhý má být jógový popruh?', 'Většině lidí stačí zhruba dva metry. Vyšší cvičenci nebo ti, kdo chtějí popruh použít při náročnějších pozicích, uvítají délku kolem tří metrů. Krátký popruh se hůř nastavuje a méně vyhovuje při předklonu.'),
        ('Kolik bloků si mám koupit?', 'Pro domácí cvičení jsou praktické dva, protože mnoho pozic využívá oba najednou, třeba trojúhelník s oporou nebo podpora pod pánví. Začínáte-li, stačí jeden a druhý můžete dokoupit později.'),
        ('K čemu je bolster?', 'Bolster podepře záda, kolena nebo hrudník při restorativní józe a relaxaci. Díky němu mohou svaly povolit, když pozici držíte několik minut. Hodí se i v těhotenství, ale pozice konzultujte s lékařem a zkušeným učitelem.'),
        ('Čím vyplnit bolster, aby byl pohodlný?', 'Bavlněné nebo pěnové plnivo je lehké a snadno se čistí. Pohanka se přizpůsobí tvaru těla a drží ho, ale je těžší a při pohybu šustí. Volba je otázkou osobního pohodlí.'),
        ('Jak vyčistit jógové pomůcky?', 'Pěnu a korek otřete vlhkým hadříkem s mýdlem, dřevo jen setřete. Bavlněný popruh a potahy bolsterů se perou podle štítku na šetrný program. Nesušte je na topení a nenamáčejte korek ani dřevo.'),
        ('Je jógové kolo bezpečné pro začátečníky?', 'Kolo prohlubuje záklony, proto ho začátečníci používají jen pod vedením zkušeného učitele a s postupným zvyšováním náročnosti. Pokud máte bolesti zad nebo zdravotní omezení, poraďte se předem s lékařem.'),
        ('Mohu jógové pomůcky použít i na pilates a protahování?', 'Ano. Blok se hodí pod pánev při mostu, popruh při protahování nohou a bolster při relaxaci. Pro pilates ale existují i specializované pomůcky jako malý míč nebo kruh, které najdete v samostatné kategorii.'),
        ('Co je zafu a komu se hodí?', 'Zafu je kulatý polštář na meditační sed. Zvyšuje pánev, takže se páteř narovná a nohy se uvolní. Hodí se pro každého, kdo sedí na zemi déle než několik minut a chce se vyhnout bolestem kolen a zad.'),
    ])

# ------------------------------------------------------------------ skialpove-boty
NEW['skialpove-boty'] = dict(long=True,
    title='Skialpové boty: tuhost, hmotnost, velikost a výběr',
    desc='Skialpové boty pro túry, freeride i závody. Jak vybrat podle hmotnosti, tuhosti, lasty a kompatibility s vázáním a porovnat obchody.',
    intro='<p>Skialpová bota musí zvládnout dva úkoly, které si odporují. Při výstupu má být lehká a pohyblivá, aby vás nebolely nohy po tisíci výškových metrech, ve sjezdu pevná a přesná, aby lyže poslechla. Výsledkem je kompromis a každá značka ho nastavuje trochu jinak. Na Sportece porovnáváme nabídky českých obchodů u pánských i dámských skialpových bot od závodních modelů po freeridové boty s vyšší tuhostí.</p>'
          '<p>V nabídce převažuje ' + B(('dynafit', 'Dynafit'), ('fischer', 'Fischer'), ('atomic', 'Atomic'), ('hagan', 'Hagan'), ('dalbello', 'Dalbello'), ('scott', 'Scott'), ('k2', 'K2')) +
          '. K botám se hodí <a href="/skialpove-lyze/">skialpové lyže</a>, <a href="/skialpove-vazani/">skialpová vázání</a> a <a href="/skialpove-pasy/">skialpové pásy</a>. Širší přehled najdete v kategorii <a href="/skialpinismus/">skialpinismus</a>.</p>',
    guide='<h2>V čem se skialpová bota liší od sjezdové</h2>'
          '<p>Sjezdová bota je tuhá a těžká, protože ve sjezdu přenáší každý pohyb na lyži a nemusí se v ní chodit. Skialpová bota má pohyblivý kotník: stačí přepnout páčku nebo spony a horní část boty se předklání a zaklání, takže můžete při výstupu kráčet. Dole má rýhovanou podrážku s dobrou přilnavostí, protože se v ní chodí po sněhu, skalách i dřevěných schodech chat. Skialpová bota bývá výrazně lehčí než sjezdová, což na dlouhém stoupání ušetří hodně energie.</p>'
          '<p>Pokud lyžujete převážně na sjezdovkách a skialp je jen příležitostné zpestření, podívejte se také na <a href="/lyzarske-boty/">lyžařské boty</a>. Pokud chcete jen občas vystoupit za hranice areálu, hodí se lehčí univerzální skialpová bota.</p>'
          '<h2>Kategorie skialpových bot podle použití</h2>'
          + T(['Typ', 'Charakteristika', 'Pro koho'], [
              ['Závodní (race)', 'extrémně lehké, karbon, minimum přezek', 'závodníky skialpinismu a rychlé výstupy'],
              ['Lehké túrové', 'nízká hmotnost, velký rozsah chůze, střední tuhost', 'dlouhé túry a jarní skialp'],
              ['Univerzální (all-round)', 'kompromis mezi chůzí a sjezdem', 'většinu cvičenců, kombinace túr a lehkého freeridu'],
              ['Freeridové', 'tužší skořepina, více přezek, těžší', 'agresivní sjezd mimo trať a kratší výstupy'],
              ['Dámské', 'užší pata, nižší lýtko, jiné rozložení lasty', 'ženy s užší nohou a nižším lýtkem'],
              ['Použité a z předchozích sezón', 'starší modely nebo předvedené kusy', 'ti, kdo nechtějí nejnovější generaci']]) +
          '<h2>Hmotnost a tuhost, dvě čísla, která určují charakter</h2>'
          '<p>Hmotnost boty je pro výstup rozhodující: každých sto gramů na chodidle odpovídá při stovkách kroků zátěži navíc. Lehčí bota ale mívá nižší tuhost a méně přesný přenos síly. Tuhost, označovaná číslem flexu, ukazuje, jak odolně se bota předklání. Čím vyšší flex, tím přesnější přenos, ale také větší nároky na techniku. Značky používají různé škály, takže číslo porovnávejte jen u stejného výrobce a čtěte popis.</p>'
          '<ul><li><strong>Nižší tuhost:</strong> pohodlnější chůze a menší únava, hodí se pro lehčí jezdce a túry na pomalou jízdu.</li>'
          '<li><strong>Střední tuhost:</strong> všestranná volba pro většinu amatérů.</li>'
          '<li><strong>Vysoká tuhost:</strong> přesnost v tvrdém sněhu a při rychlé jízdě, ale těžší a méně komfortní při výstupu.</li></ul>'
          '<h2>Velikost a tvar nohy</h2>'
          '<p>Velikost skialpových bot se udává v tzv. mondopointu, tedy v délce chodidla v centimetrech. Je to přesnější než klasická velikost a při koupi si změřte nohu od paty po nejdelší prst. Důležitá je i šířka v nártu a v přední části. Skořepina má sedět tak, aby pata držela a prsty se mohly lehce pohnout. Boty, které tlačí v kotníku, vyvolají otlaky na dlouhém stoupání.</p>'
          '<p>Zkoušejte boty v ponožkách, které budete používat na túru. Vhodné jsou <a href="/lyzarske-ponozky/">lyžařské ponožky</a> střední tloušťky; příliš tlusté ponožky zmenšují prostor a snižují cit. Zkoušejte v odpoledních hodinách, kdy je noha mírně oteklá, a neuspěchejte nákup bez vyzkoušení: vyměňovat boty po koupi bývá komplikované.</p>'
          '<h2>Lastová vložka a termoformování</h2>'
          '<p>Většina kvalitních skialpových bot má vyjímatelnou vnitřní botu, tzv. lastu. Lze ji termoformovat: výrobce nebo servis ji zahřeje a nechá přilnout k tvaru nohy. Tím zmizí tlaky a boty sedí jako ušité na míru. Pokud máte specifickou nohu s vystouplým kloubem nebo širší nárt, nechte skořepinu případně vyfouknout v servisu. Nikdy ji nepřetvářejte doma bez zkušeností.</p>'
          '<h2>Zapínání a přezky</h2>'
          '<p>Skialpové boty používají přezky, ráčny, kabely nebo kolečko typu Boa. Přezky jsou jednoduché a spolehlivé a dají se opravit i v terénu. Kolečko je rychlé a přesné, ale vyžaduje úschovu klíče či náhradního lanka. Počet přezek se liší: závodní boty mají jednu nebo dvě, freeridové čtyři. Při dlouhém výstupu se hodí jednoduché povolení horní přezky, aniž byste museli sundávat rukavice.</p>'
          '<h2>Kompatibilita s vázáním</h2>'
          '<p>Skialpová bota musí být kompatibilní s typem vázání. Existují dva hlavní systémy. Tech vázání (pinové) používá kovové zárubně na špici a patě boty, je lehké a oblíbené u túrových jezdců. Rámové vázání se podobá sjezdovému a používá standardní podrážku, takže je pevnější, ale těžší. Většina moderních skialpových bot má zárubně pro tech a některé ještě kombinovanou podrážku, která funguje i s rámovým systémem. Před nákupem zkontrolujte popis boty a typ vázání, které máte či plánujete.</p>'
          '<p>K botám patří <a href="/skialpove-vazani/">skialpová vázání</a>. Pokud vybíráte celou sadu, začněte u lyží v kategorii <a href="/skialpove-lyze/">skialpové lyže</a>.</p>'
          '<h2>Režim chůze a rozsah pohybu</h2>'
          '<p>Rozsah kotníku v režimu chůze je jedním z hlavních kritérií. Čím větší, tím přirozenější krok, ale i tím větší vůle v horní části boty. Kvalitní boty mají pevný zámek, který se přepíná prstem nebo holí, aby se nemuseli sundávat rukavice. Zkuste si při zkoušení udělat několik kroků v režimu chůze a pak přepnout do sjezdu a zkontrolovat, jak pevně bota drží.</p>'
          '<h2>Výběr podle stylu</h2>'
          '<ul><li><strong>Dlouhé túry a výstupy na vrcholy:</strong> lehká nebo univerzální bota s velkým rozsahem chůze.</li>'
          '<li><strong>Freeride a sjezd mimo trať:</strong> tužší bota se čtyřmi přezkami, ochota nést větší váhu.</li>'
          '<li><strong>Závody:</strong> závodní bota s karbonovou skořepinou a minimem přezek.</li>'
          '<li><strong>Ženy:</strong> dámský model s upravenou lýtkovou částí.</li>'
          '<li><strong>Začátečník:</strong> univerzální bota se střední tuhostí a snadným přepínáním režimů.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Po túře vyndejte lastu a nechte ji vyschnout při pokojové teplotě, nikdy ne na topení.</li>'
          '<li>Skořepinu vytřete suchým hadrem a odstraňte sníh a písek ze zámků a přezek.</li>'
          '<li>Mechanismy chůze občas zkontrolujte a odstraňte zamrzlou vodu.</li>'
          '<li>V létě boty skladujte zapnuté lehce, na suchém a tmavém místě.</li>'
          '<li>Opotřebovanou gumovou podrážku lze nechat vyměnit v servisu.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Koupit příliš tuhou botu a pak trpět při výstupu.</li>'
          '<li>Podcenit šířku nohy a koupit botu jen podle délky.</li>'
          '<li>Neověřit kompatibilitu se současným vázáním.</li>'
          '<li>Nechat si boty poslat bez možnosti vrácení a bez vyzkoušení.</li>'
          '<li>Vybrat závodní botu na běžné túry, kde chybí komfort a podpora.</li></ul>'
          '<h2>Pohyb v botách při výstupu</h2>'
          '<p>Skialpový krok je delší a plynulejší než krok v turistických botách, protože pata se zvedá, zatímco lyže klouže po sněhu. Bota proto musí mít u paty dostatečný prostor pro ohyb, ale zároveň držet patu, aby se nezvedala. Při šikmých traverzech hraje roli i tvar podrážky a tuhost skořepiny v bocích: příliš měkká bota se na šikmině boří. Pokud vás zajímají stoupací pásy, podívejte se do kategorie <a href="/skialpove-pasy/">skialpové pásy</a>.</p>'
          '<h2>Přenášení a přeprava bot</h2>'
          '<p>V létě a při cestování se skialpové boty vyplatí chránit před otlačením. Zapněte je jen lehce, vložte do obalu a neukládejte pod těžké zavazadlo. Při letu je lepší vzít boty do příručního zavazadla, protože jejich ztráta nebo zpoždění zkomplikuje celou túru. Dobře vyschlá lasta se v kufru nezmačká a nezapáchá.</p>'
          '<h2>Teplo a vlhkost v botě</h2>'
          '<p>Skialpová bota je při výstupu horká a při sjezdu najednou studená. Dobrou kombinací je tenká ponožka bez nadbytečné vycpávky, kterou můžete během túry vyměnit za suchou. Mokrá ponožka při sjezdu rychle vychladí nohu, proto si na delší túru vezměte náhradní pár. Lasta s vrstvou, která se nenasákne, zkrátí dobu schnutí v noci na chatě.</p>'
          '<h2>Bezpečnost na túře</h2>'
          '<p>Skialpová výbava neznamená jen boty. Mimo trasy je nezbytná lavinová trojice, tedy lavinový vyhledávač, sonda a lopata, a také znalost lavinové situace. Pomůže i <a href="/lyzarske-helmy/">lyžařská helma</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a> a teplé vrstvy včetně <a href="/lyzarske-termopradlo/">termoprádla</a>. Před výpravou se informujte o stavu sněhu a absolvujte kurz.</p>'
          '<h2>Co je v kategorii</h2>'
          '<p>Převažují boty Dynafit, a to různé řady od závodních po freeridové, včetně dámských modelů. Dále najdete Fischer (například univerzální Transalp), Atomic (Backland), Hagan, Dalbello, Roxa, Scott a K2. V nabídce se objevují i použité kusy a předvedené modely z předchozích sezón; popis vždy čtěte pozorně. Nezapomeňte, že skialp je jen jedna z disciplín, pro sjezd na sjezdovkách se podívejte do kategorie <a href="/sjezdove-lyze/">sjezdové lyže</a>.</p>',
    faq=[
        ('Jaké skialpové boty vybrat na začátek?', 'Univerzální bota se střední tuhostí, velkým rozsahem chůze a snadným přepínáním režimů. Je dostatečně pohodlná pro výstupy a přitom ustojí sjezd po prašanu i sjezdovkách. Závodní a freeridové modely si nechte na později, až poznáte vlastní styl.'),
        ('Jak poznám správnou velikost skialpové boty?', 'Změřte délku chodidla v centimetrech a porovnejte s tabulkou mondopointu výrobce. Pata musí držet a prsty se nesmí zarážet do špice při sjezdu. Boty zkoušejte v ponožkách, které použijete na túře, a raději odpoledne.'),
        ('Pasují skialpové boty na každé vázání?', 'Nikoli. Většina bot má zárubně pro tech vázání, některé mají i rámovou podrážku. Před nákupem ověřte, jaký systém vaše vázání používá, a zkontrolujte popis boty. Nekompatibilní kombinace nemusí držet ani pustit bezpečně.'),
        ('Co znamená flex u skialpových bot?', 'Je to ukazatel tuhosti boty. Vyšší číslo znamená tužší botu s přesnějším přenosem síly, nižší pohodlnější botu pro chůzi. Každý výrobce používá vlastní škálu, takže čísla různých značek nelze přímo porovnávat.'),
        ('Dají se skialpové boty přizpůsobit noze?', 'Ano. Vnitřní lastu lze termoformovat, aby kopírovala tvar chodidla. Skořepinu může v servisu upravit zkušený technik. Doma ji neohřívejte ani neohýbejte, mohli byste ji poškodit.'),
        ('Kolik by měly skialpové boty vážit?', 'Záleží na kategorii. Závodní boty jsou výrazně lehčí než freeridové. Pro výstup je výhodnější nižší hmotnost, pro sjezd vyšší tuhost. Nejdůležitější je najít kompromis, který odpovídá vaší trase, a nehonit se jen za číslem na váze.'),
        ('Je možné ve skialpových botách sjíždět sjezdovky?', 'Ano, funguje to, ale s menší přesností než ve sjezdových botách. Lehčí skialpové boty se na tvrdé a rychlé sjezdovce rychle unaví. Pro převážně sjezdové lyžování zvolte klasické lyžařské boty.'),
        ('Čím se liší dámské skialpové boty?', 'Mívají užší patu, nižší a užší lýtkovou část a mírně odlišné nastavení tuhosti. Díky tomu lépe sedí na ženské noze a nedřou. Ženy s širší nohou mohou zvolit i pánský model.'),
        ('Jak pečovat o skialpové boty po túře?', 'Vyjměte lastu a nechte ji vyschnout při pokojové teplotě. Skořepinu vytřete, odstraňte sníh z mechanismů a nechte boty vyvětrat. Nesušte je na topení, protože teplo poškozuje plasty a lepidla.'),
        ('Co si vzít kromě bot na skialpovou túru?', 'Lavinovou trojici (vyhledávač, sondu, lopatu), helmu, brýle, teplé vrstvy a termoprádlo, mapu a nabitý telefon. Před túrou si přečtěte lavinovou prognózu a nepodceňujte kurz lavinové prevence.'),
    ])

# ------------------------------------------------------------------ rybarske-lode-a-elektronika
NEW['rybarske-lode-a-elektronika'] = dict(long=True,
    title='Rybářské lodě, motory a echolóty: jak vybrat',
    desc='Nafukovací rybářské čluny, elektromotory, echolóty a zavážecí lodičky. Jak vybrat podle revíru, nosnosti a porovnat nabídky českých obchodů.',
    intro='<p>Z lodi se loví jinak než z břehu. Dostanete se k místům, kam nedohodíte, vidíte pod hladinu a zavážecí lodička odveze návnadu k hraně dna, kde by ji nikdo neprohodil. Na druhou stranu je s lodí spojena i odpovědnost: nosnost, předpisy, bezpečnost a vybavení. Na Sportece porovnáváme nabídky českých obchodů u nafukovacích rybářských člunů, elektromotorů, echolotů a sonarů, zavážecích lodiček i příslušenství jako držáky nebo pumpy.</p>'
          '<p>V nabídce uvidíte ' + B(('garmin', 'Garmin'), ('deeper', 'Deeper'), ('ridgemonkey', 'RidgeMonkey'), ('master', 'Master'), ('mivardi', 'Mivardi'), ('funyak', 'Funyak'), ('insportline', 'Insportline'), ('fox', 'Fox')) +
          '. Navazující výbavu najdete v kategoriích <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/rybarske-navijaky/">navijáky</a>, <a href="/rybarske-obleceni/">rybářské oblečení</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>.</p>',
    guide='<h2>Co všechno patří mezi rybářské lodě a elektroniku</h2>'
          '<p>Kategorie spojuje tři skupiny. První jsou plavidla: nafukovací čluny a pontony. Druhou tvoří pohon, nejčastěji elektrické motory na zadní zrcadlo nebo na příď. Třetí je elektronika: echolot, sonar, držáky a příslušenství. K tomu přibývají zavážecí lodičky pro kaprařinu. Každá skupina řeší jiný problém a hodí se pro jiný způsob lovu.</p>'
          + T(['Skupina', 'Co řeší', 'Hodí se pro'], [
              ['Nafukovací rybářský člun', 'přeprava rybáře a výbavy po vodě', 'přívlač, feeder, lov z lodi na rybníce a přehradě'],
              ['Elektrický motor', 'tichý a bezemisní pohon', 'rybníky, přehrady a revíry se zákazem spalovacích motorů'],
              ['Echolot (sonar)', 'zobrazuje dno, hloubku a ryby', 'hledání lovných míst, zjišťování hloubky a struktury'],
              ['Zavážecí lodička', 'doveze návnadu nebo nástrahu na vzdálené místo', 'kaprařina, lov na položenou'],
              ['Přenosný sonar', 'zahodí se na vlasci nebo pošle z břehu', 'lov z břehu a z malé lodi'],
              ['Držáky a montáže', 'upevní sonar nebo snímač na člun', 'majitelé člunů a pontonů'],
              ['Pumpy a příslušenství', 'nafukují a opravují čluny', 'každý, kdo vlastní nafukovací plavidlo']]) +
          '<h2>Nafukovací rybářské čluny</h2>'
          '<p>Nafukovací člun se vejde do kufru auta a na vodě drží stabilitu díky velkému objemu vzduchových komor. Rybářské verze mají zesílené dno, madla, kroužky na lana, držáky na pruty a někdy i vlastní sedák. Pro rybáře je důležitá stabilita: v lodi se stoupá, nahazuje a dělají se prudší pohyby.</p>'
          '<ul><li><strong>Materiál:</strong> PVC je nejběžnější, odolné proti oděru a opravitelné. Tkaninou zesílené PVC vydrží víc, ale je dražší.</li>'
          '<li><strong>Nosnost:</strong> sečtěte hmotnost osádky, motoru, baterie a výbavy a nechte rezervu. Výrobce uvádí nosnost i počet osob.</li>'
          '<li><strong>Dno:</strong> nafukovací, lamelové nebo pevné, s různou tuhostí. Pevnější dno se snáze vstává, ale zabere víc místa.</li>'
          '<li><strong>Komory:</strong> víc nezávislých komor zvyšuje bezpečnost, protože průraz jedné nezpůsobí potopení.</li>'
          '<li><strong>Zrcadlo:</strong> zadní stěna pro motor. Ověřte, zda ji člun má a pro jaký výkon je určena.</li></ul>'
          '<p>Pro rybáře, kteří chtějí jen příležitostně zajít na rybník, stačí menší člun do dvou osob. Na přehradu nebo větší jezero hledejte stabilnější a nosnější typ. Pozor na malé nafukovací kousky určené spíše na koupání než na rybaření: nemají zesílení ani držáky.</p>'
          '<h2>Elektrické motory</h2>'
          '<p>Elektromotor je v českých podmínkách nejběžnější pohon. Na řadě revírů jsou spalovací motory zakázané a elektromotor je tichý, takže nevyplaší ryby. Výkon se udává tahem v librách nebo kilogramech. Pro malý člun stačí nižší tah, pro těžší nebo delší plavbu proti větru větší.</p>'
          '<ul><li><strong>Tah:</strong> řiďte se velikostí a zatížením člunu; příliš slabý motor se vybíjí a plavba trvá déle.</li>'
          '<li><strong>Napětí baterie:</strong> motory pracují nejčastěji na 12 V, silnější na 24 V i více. Vyšší napětí snižuje odběr proudu; výdrž určuje celková kapacita baterie.</li>'
          '<li><strong>Baterie:</strong> trakční nebo lithiová. Lithiová je lehčí a vydrží víc cyklů, olověná je levnější a těžší.</li>'
          '<li><strong>Typ montáže:</strong> na zrcadlo se hodí závěsný motor, příďový motor se používá u větších člunů a pro přesné držení polohy.</li>'
          '<li><strong>Ovládání:</strong> ruční páka je jednoduchá, dálkové ovládání nebo pedál ponechá ruce volné pro nahazování.</li></ul>'
          '<p>Vždy zkontrolujte pravidla daného revíru: povolení, zákaz motorů a předpisy o plavbě. Rybářský řád nebo provozovatel vodní nádrže vám dá přesné informace.</p>'
          '<h2>Echolot a sonar</h2>'
          '<p>Echolot vysílá zvukové impulzy ke dnu a z odrazů vytváří obraz. Ukáže hloubku, strukturu dna, překážky i ryby ve vodním sloupci. Pro rybáře je nejcennější mapa hloubek: díky ní najdete hrany, jámy a plató, kde se ryby drží. Aktuální nabídka zahrnuje vestavěné displeje i malé přenosné sonary.</p>'
          '<ul><li><strong>Displej:</strong> větší a kontrastnější usnadňuje čtení na slunci. Dotykové ovládání je pohodlné, ale v rukavicích může zlobit.</li>'
          '<li><strong>Paprsek (CHIRP, klasický, boční):</strong> CHIRP dává ostřejší obraz a lepší odlišení cílů, boční snímání ukazuje prostor kolem lodi. Řada Striker od Garminu je příklad dostupnější třídy.</li>'
          '<li><strong>GPS a mapování:</strong> zaznamenává lovná místa a trasu.</li>'
          '<li><strong>Snímač:</strong> upevňuje se na zrcadlo, přes trup nebo se zavěsí na tyči. U přenosných sonarů plave na hladině.</li>'
          '<li><strong>Napájení:</strong> vestavěný akumulátor nebo baterie lodě. Při zimě výdrž klesá.</li></ul>'
          '<p>Přenosné sonary jako Deeper se připojují k telefonu a hodí se pro lov z břehu i z malé lodi. Jsou praktické, ale displej je menší a spoléhají na signál mezi snímačem a mobilem.</p>'
          '<h2>Zavážecí lodičky</h2>'
          '<p>Zavážecí lodička je dálkově ovládané plavidlo, které odveze návnadu nebo nástrahu na vzdálené místo. Používá se hlavně při lovu kaprů. Základní rozlišení je podle nosnosti, dosahu, výdrže baterie a vybavení (GPS, sonar, světla). Silnější vítr, vlny nebo rostliny mohou její pohyb omezit, takže ji zkoušejte nejdřív na klidné vodě. U značek jako RidgeMonkey nebo Devict najdete různé velikosti. Před použitím se informujte, zda revír zavážecí lodičky povoluje: na mnoha vodách jsou zakázané nebo omezené.</p>'
          '<h2>Příslušenství, bezpečnost a péče</h2>'
          '<p>Na vodu patří plovací vesta, i pokud plavete dobře. Studená voda a pád z lodi znamenají rychlé ochlazení a vyčerpání. K výbavě patří pádlo, kotva, lano, signální píšťalka a vodotěsný obal na doklady a telefon. Plovací pomůcky najdete mezi <a href="/vodni-sporty/">vodními sporty</a>. Pro oblečení do vlhka a chladna se hodí <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>'
          '<ul><li>Po použití člun opláchněte čistou vodou a nechte úplně vyschnout, jinak plesniví.</li>'
          '<li>Skladujte volně sbalený nebo mírně nafouklý, mimo ostré předměty a hlodavce.</li>'
          '<li>Pumpu a opravnou sadu mějte stále u sebe.</li>'
          '<li>Baterie dobíjejte podle pokynů výrobce a v zimě je skladujte v teple.</li>'
          '<li>Snímač echolotu po vynoření očistěte a neponechávejte na slunci.</li></ul>'
          '<h2>Výběr podle způsobu rybaření</h2>'
          '<ul><li><strong>Lov kaprů:</strong> zavážecí lodička, případně malý člun s elektromotorem a přenosný sonar. K tomu <a href="/rybarske-spacaky/">rybářské spacáky</a> a <a href="/rybarske-stany/">rybářské stany</a>.</li>'
          '<li><strong>Přívlač:</strong> stabilní člun, tichý elektromotor a echolot pro nalezení hran.</li>'
          '<li><strong>Feeder a plavaná:</strong> menší člun a snímač na tyči pro rychlé zjištění hloubky.</li>'
          '<li><strong>Rybaření z břehu:</strong> přenosný sonar, který se hodí na zahozu.</li>'
          '<li><strong>Rodinné výlety:</strong> širší stabilní člun a lehký motor bez složité elektroniky.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupit člun podle ceny a ne podle nosnosti a použití.</li>'
          '<li>Podcenit baterii: motor pak vydrží jen pár hodin.</li>'
          '<li>Použít sonar bez zvládnutí základního nastavení citlivosti a hloubky.</li>'
          '<li>Opomenout povolení k plavbě nebo motoru na daném revíru.</li>'
          '<li>Vyrazit na vodu bez plovací vesty a lana.</li>'
          '<li>Skladovat vlhký člun v uzavřeném obalu.</li></ul>'
          '<h2>Převoz a doprava člunu</h2>'
          '<p>Nafukovací člun se sbalí do tašky nebo batohu, ale i tak váží několik desítek kilogramů. Spolu s motorem a baterií se přeprava prodlouží, takže počítejte s vozíkem nebo druhou osobou. Baterii vždy převážejte upevněnou, aby se nepřevrátila. Elektromotor ukládejte tak, aby se nepoškodila vrtule a kabely. Na vodě pak pamatujte, že těžiště se po naložení posune a člun bude citlivější na každý pohyb osádky.</p>'
          '<h2>Povětrnostní podmínky a zásady plavby</h2>'
          '<p>Nafukovací člun je lehký a vítr s ním zatočí. Při předpovědi silného větru raději zůstaňte na břehu, protože návrat proti větru vybíjí baterii i síly. Držte se blízko břehu, pokud ještě nemáte zkušenosti, a vždy informujte někoho blízkého o plánu. Při bouřce vodu okamžitě opusťte, protože na hladině jste nejvyšším bodem.</p>'
          '<h2>Co v kategorii najdete</h2>'
          '<p>V nabídce jsou především elektromotory (například Master a Rhino), echolóty a sonary Garmin a Deeper, zavážecí lodičky RidgeMonkey a Devict, nafukovací čluny Funyak, Intex nebo Mivardi a držáky či pumpy pro člun. Najdete i související položky jako zavážecí příslušenství a lodní pumpy. Pro další vybavení se podívejte do kategorie <a href="/rybareni/">rybaření</a> nebo <a href="/rybarske-tasky/">rybářské tašky</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Ve výpisu porovnáte nabídky českých obchodů a prověříte rozměry, nosnost a technické parametry. U elektroniky čtěte popis snímače, rozlišení displeje a zda je v balení kabel a držák. U člunů ověřte rozměr po nafouknutí, hmotnost balení a obsah (pádla, pumpa, opravná sada). Dostupnost se rychle mění, proto před objednávkou otevřete detail nabídky a zkontrolujte dodací lhůty.</p>',
    faq=[
        ('Jaký člun vybrat na rybaření na rybníce?', 'Menší stabilní nafukovací člun pro jednoho až dvě osoby s pevným dnem, držáky a zesíleným materiálem. Důležitá je nosnost včetně výbavy a motoru. Pokud plánujete jezdit i na větší vodu, zvolte větší a nosnější typ.'),
        ('Jaký tah elektromotoru potřebuji?', 'Řiďte se velikostí člunu a zatížením. Malý člun s jednou osobou vystačí s nižším tahem, těžší člun a plavba proti větru potřebují silnější motor. Výrobci obvykle uvádějí doporučené použití, vyplatí se mít rezervu výkonu.'),
        ('Jakou baterii k elektromotoru použít?', 'Nejčastěji se používá trakční olověná nebo lithiová baterie. Lithiová je lehčí a vydrží víc cyklů, olověná je levnější a těžší. Kapacita rozhoduje o výdrži, napětí musí odpovídat motoru.'),
        ('Co je CHIRP a je pro rybáře důležitý?', 'CHIRP je technologie, která vysílá širší rozsah frekvencí a vytváří ostřejší obraz a lépe oddělené cíle. Pro rybáře je užitečný při rozlišení ryb od struktury dna. Základní echolot ale také poslouží, zejména pokud hledáte hloubku a hrany.'),
        ('Lze použít přenosný sonar bez lodi?', 'Ano. Přenosné sonary se zahazují nebo přivážejí lodičkou a data posílají do telefonu. Hodí se k mapování hloubek z břehu. Dosah signálu a displej jsou omezené, takže pro delší používání na lodi je vhodnější pevný echolot.'),
        ('Je zavážecí lodička povolená na každém revíru?', 'Ne. Na řadě vod je zakázaná nebo omezená, protože může rušit ostatní rybáře a ryby. Před použitím si přečtěte řád konkrétního revíru a požádejte provozovatele o informace.'),
        ('Jak pečovat o nafukovací člun?', 'Po použití ho opláchněte čistou vodou, nechte úplně vyschnout a skladujte volně složený na suchém místě. Vyhněte se ostrým předmětům a dlouhému působení slunce. Opravná sada patří do každé výbavy.'),
        ('Potřebuji k elektromotoru povolení?', 'Pravidla se liší podle revíru a typu plavidla. Některé vody motory zakazují, jiné je povolují s omezeními. Zeptejte se správce vody a prostudujte místní řád a obecné předpisy o plavbě.'),
        ('Jak upevnit snímač echolotu na člun?', 'Snímač se obvykle připevňuje na zadní zrcadlo držákem, někdy na tyč přes bok člunu. Musí být ponořený, mířit kolmo ke dnu a nesmí kolidovat s motorem. Dodržujte návod výrobce, špatná poloha zhoršuje obraz.'),
        ('Co vzít na vodu kromě člunu a motoru?', 'Plovací vestu, pádlo, kotvu, lano, píšťalku, vodotěsný obal na telefon a doklady a opravnou sadu. V chladném počasí teplé a nepromokavé oblečení. Člun nenechávejte bez dozoru a nikdy neplavte sami bez informování blízkých.'),
    ])
