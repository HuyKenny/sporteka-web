"""sporteka.cz — wave 17d (4. 11. 2026): long texts (>= 1650 words) for bandaze-a-ortezy, snowboarding, plavecke-bryle, celovky-a-svitilny.
General true facts only, no prices, no medical claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bandaze-a-ortezy
NEW['bandaze-a-ortezy'] = dict(long=True,
    title='Bandáže a ortézy na kolena, zápěstí, kotníky',
    desc='Bandáže a ortézy na koleno, kotník, zápěstí, loket i záda: typy, velikosti, materiály a praxe. Nabídky českých obchodů vedle sebe na jednom místě.',
    intro='<p>Bandáž je pružný návlek, ortéza pevnější pomůcka s výztuhami a mezi nimi leží celá škála dílů, které sportovci nosí na kolenou, kotnících, zápěstích, loktech či zádech. '
          'Kategorie <strong>bandáže a ortézy</strong> sdružuje neoprenové návleky, elastické pásy, stabilizační ortézy s kovovými či plastovými dlahami, ale i tejpovací pásky a rukavice na ochranu dlaně. '
          'Tyto produkty slouží jako opora při zátěži, jako doplněk tréninku nebo jako ochrana v kontaktních sportech.</p>'
          '<p>Na Sportece vidíte stejné modely u několika českých obchodů vedle sebe a můžete porovnat velikosti, které jsou skladem. Texty níže mají jen obecný informační charakter a nenahrazují radu lékaře nebo fyzioterapeuta. '
          'Tipy na doplňky pro cvičení najdete ve <a href="/fitness/">fitness</a>, na sportovní ponožky v kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a> a podpůrnou péči o klouby v <a href="/kolagen-a-klouby/">kolagenu a kloubech</a>.</p>',
    guide='<h2>Co je bandáž a co ortéza</h2>'
          '<p>Slova se v obchodech často míchají, ale význam mají odlišný. <strong>Bandáž</strong> bývá měkká, elastická a tvarovaná na daný kloub, drží teplo a poskytuje lehký tlak. '
          '<strong>Ortéza</strong> má pevnější konstrukci, často výztuhy po stranách nebo popruhy, které omezují pohyb v určitém směru. Rozdíl pocítíte i na pohodlí: bandáž lze nosit celý trénink, ortéza je tužší a vyžaduje přesné nasazení. '
          'Třetí skupinou jsou ovazy a pásky, které se omotávají kolem kloubu nebo prstů a drží pohromadě třením nebo suchým zipem. Sem patří i boxerské bandáže na zápěstí a klouby ruky, které zpevňují zápěstí a chrání kůži při úderech, kineziologický tejp, který se lepí na kůži a jen lehce podporuje sval či kloub, a tejpovací pásky, jimiž se pevně fixují prsty nebo kotník. Samostatnou skupinou jsou kompresní návleky na lýtko, stehno či loket, které podporují prokrvení a nenahrazují zpevnění kloubu.</p>'
          '<p>Pokud máte akutní potíž, zvolte výrobek podle doporučení odborníka. Obchod ani srovnávač cen nemůže posoudit, jaká pomůcka je pro konkrétní situaci vhodná, proto se u zranění vždy obraťte na lékaře.</p>'
          '<h2>Přehled typů podle části těla</h2>'
          + T(['Část těla', 'Běžné provedení', 'Kde se nosí', 'Na co dát pozor'], [
              ['Koleno', 'neoprenový návlek, otevřená či uzavřená patella, ortéza s bočními výztuhami', 'běh, volejbal, basketbal, posilování', 'obvod nad a pod kloubem a správný střih kolem čéšky'],
              ['Kotník', 'elastický návlek, šněrovací, s popruhy ve tvaru osmičky', 'míčové hry, tenis, squash, florbal', 'musí se vejít do boty, tlusté provedení potřebuje větší velikost obuvi'],
              ['Zápěstí', 'krátký neoprenový pásek, delší dlaha, popruh přes dlaň', 'posilování, gymnastika, box', 'obvod zápěstí měřte těsně nad kostí'],
              ['Loket', 'tenisový pás pod loktem, návlek přes celý kloub', 'tenis, squash, vzpírání', 'pás se nasazuje na předloktí, ne na kloub'],
              ['Záda a bedra', 'pás s výztuhami, vzpěračský opasek, korzetová ortéza', 'zvedání těžkých břemen, dlouhé sezení, běžecké tréninky', 'šířka a pevnost podle činnosti'],
              ['Rameno a hrudník', 'stahovací popruhy, ortéza s ramenním popruhem', 'plavání, házená, bojové sporty', 'velikost podle obvodu hrudníku i paže'],
              ['Prsty a dlaně', 'tejpovací pásky, ochranné návleky, rukavice s výztuhou', 'lezení, gymnastika, vzpírání', 'páska se přikládá hladce, bez zvlnění']]) +
          '<p>Opravdu praktický je zvyk nosit stejný typ ochrany u stejné činnosti. Kdo hraje <a href="/volejbal/">volejbal</a> nebo <a href="/basketbal/">basketbal</a>, hledá obvykle návleky na kotníky a kolena, zatímco v posilovně se hodí zápěstní pásky a opasky. '
          'Pro rekreační <a href="/beh/">běh</a> lidé volí lehké elastické návleky na lýtka a kolena, které snáší pot a nesklouzávají.</p>'
          '<h2>Materiály a jejich vlastnosti</h2>'
          '<ul><li><strong>Neopren</strong> drží teplo a dobře přilne k tělu. Při dlouhém nošení se ale potíte a pod návlekem může kůže podráždit, proto se vyplatí prodyšné varianty s perforací.</li>'
          '<li><strong>Elastické úplety</strong> z bavlny, nylonu nebo polyesteru jsou lehčí a prodyšnější. Hodí se pro delší aktivity a pro horké dny.</li>'
          '<li><strong>Kompresní tkaniny</strong> jsou hustě tkané a pevně obepínají svalovou skupinu. Mívají gradovaný tlak, silnější u kloubu a slabší dál od něj.</li>'
          '<li><strong>Výztuhy</strong> z oceli, hliníku nebo plastu bývají zasunuté po stranách kloubu. Zvyšují pevnost, ale i hmotnost a složitost nasazení.</li>'
          '<li><strong>Suchý zip a popruhy</strong> umožňují dotáhnout ortézu přesně. Po čase zanášejí vlasy a vlákna z oblečení, takže je občas očistěte kartáčkem.</li></ul>'
          '<h2>Jak vybrat správnou velikost</h2>'
          '<p>Většina chyb při nákupu vychází z nepřesného měření. Obvod kloubu změřte krejčovským metrem na kůži, ne přes oblečení, a změřte ho vždy ve stejné poloze, zpravidla ve stoje s uvolněnou končetinou. '
          'Výrobci uvádějí rozpětí obvodu pro každou velikost a ty se liší podle značky, dokonce i podle řady. Pokud padnete mezi dvě velikosti, řiďte se tabulkou výrobce. U běžné bandáže bývá lepší menší velikost pro pevnější držení, u pevné ortézy ale výběr velikosti raději konzultujte s odborníkem, protože špatná velikost snižuje její funkci.</p>'
          + T(['Kdy zvolit větší', 'Kdy zvolit menší'], [
              ['otok nebo citlivá kůže, kdy bandáž tlačí', 'bandáž se po chvíli sjíždí dolů'],
              ['dlouhodobé nošení při práci', 'krátký výkon, kdy chcete pevný tlak'],
              ['obvod končetiny je na horní hranici rozmezí', 'obvod končetiny je na spodní hranici rozmezí'],
              ['obvod padne mezi dvě velikosti', 'rozhodněte se podle tabulky výrobce, u ortézy po poradě s odborníkem']]) +
          '<p>Stejné pravidlo platí pro děti a dospívající, kteří rychle rostou. Kupujte vždy podle aktuálního obvodu, ne na vyrůstání, protože příliš volná bandáž neplní svůj účel a sjíždí.</p>'
          '<h2>Pro jaký sport co hledat</h2>'
          '<h3>Běh a pohybové sporty</h3>'
          '<p>Na dlouhé běžecké tratě nepotřebujete pevnou ortézu, stačí lehký návlek, který neomezuje ohyb. Důležité je, aby nesjížděl a nedrhl za kolenem. Dobře se doplňuje s kvalitní <a href="/bezecka-obuv/">běžeckou obuví</a> a ponožkami.</p>'
          '<h3>Míčové a halové hry</h3>'
          '<p>Rychlé změny směru, výskoky a doskoky kladou nároky na kotníky a kolena. Lidé zde často volí šněrovací kotníkové ortézy nebo elastické návleky s popruhy, které se nasazují snadno a uvnitř boty se nehýbou. '
          'Podobné vybavení potřebují hráči <a href="/florbal/">florbalu</a>, <a href="/squash/">squashe</a> a <a href="/tenis/">tenisu</a>.</p>'
          '<h3>Silový trénink</h3>'
          '<p>V posilovně se hodí pásky na zápěstí pro tlaky a zvedání, kolenní bandáže při dřepech a opasek při těžkých tazích. Opasek nebo pás pomáhá cítit trup, ale nenahrazuje techniku ani postupné navyšování zátěže. '
          'Nářadí potřebné pro práci najdete v kategoriích <a href="/cinky-a-kotouce/">činky a kotouče</a> a <a href="/posilovaci-stroje/">posilovací stroje</a>.</p>'
          '<h3>Bojové a kontaktní sporty</h3>'
          '<p>Při boxu, kickboxu a MMA se chrání zápěstí, prsty i holeně. Vhodné jsou bandáže na ruce pod rukavice, chrániče zubů a návleky na kolena. Více vybavení je v kategorii <a href="/bojove-sporty/">bojové sporty</a> a <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Správné nasazení a nošení</h2>'
          '<p>Bandáž nasazujte na čistou a suchou pokožku, pokud možno bez krémů. Při navlékání se vyvarujte kroucení, protože se po chvíli sama stáčí a vytváří záhyby, které tlačí. '
          'Dotáhněte ji tak, abyste pod ni vsunuli jeden prst, ale necítili pulzování ani brnění. Kdykoliv se objeví bolest, mravenčení nebo promodrání, bandáž sundejte. '
          'Nenoste ji celý den bez přestávky, pokud to výslovně neurčil odborník, protože kůže potřebuje vzduch a svaly přirozenou práci.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Neoprenové návleky perte ručně v lehce teplé vodě s jemným mýdlem a sušte je volně rozložené, ne na radiátoru.</li>'
          '<li>Návleky se suchým zipem zapněte před praním, aby nepoškodily látku ani sebe.</li>'
          '<li>Pevné ortézy s kovovými výztuhami nenamáčejte do horké vody a při čištění vyjměte výztuhy, pokud to konstrukce dovoluje.</li>'
          '<li>Po každém tréninku vyvětrejte, aby se nezahnízdil zápach.</li>'
          '<li>Při ztrátě pružnosti, natržení nebo prasklé výztuze vyměňte výrobek za nový.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Kupovat podle obrázku bez měření obvodu.</li>'
          '<li>Spoléhat se na pomůcku místo odpočinku nebo správné techniky.</li>'
          '<li>Nosit pevnou ortézu, která nebyla doporučena, a oslabovat tak přirozenou práci svalů.</li>'
          '<li>Zaměnit levou a pravou verzi u dílů, které jsou asymetrické.</li>'
          '<li>Nechat v praxi bandáž sjíždět a místo úpravy velikosti ji dotahovat popruhy.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete například značky ' + B(('mueller', 'Mueller'), ('mcdavid', 'McDavid'), ('zamst', 'Zamst'), ('thuasne', 'Thuasne'), ('adidas', 'Adidas'), ('asics', 'Asics'), ('cep', 'Cep'), ('tsg', 'TSG'), ('venum', 'Venum'), ('4fizjo', '4FIZJO'), ('select', 'Select'), ('power-system', 'Power System')) + '. '
          'Mueller, McDavid, Zamst a Thuasne se zaměřují přímo na podporu kloubů, Venum a TSG na kontaktní sporty, Cep na kompresní návleky a Adidas či Asics nabízejí širší sportovní řadu.</p>'
          '<h2>Co dalšího se hodí k tréninku</h2>'
          '<p>Po zátěži přijde vhod regenerace. Na uvolnění svalů se používají válce a míčky z kategorie <a href="/masazni-pomucky/">masážní pomůcky</a>. '
          'Základem pohodlí je kvalitní <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>, protože švy pod bandáží mohou dráždit. '
          'Pro pohodlné držení nářadí slouží <a href="/sportovni-rukavice/">sportovní rukavice</a> a při malém zranění má být po ruce <a href="/prvni-pomoc/">lékárnička</a>.</p>',
    faq=[('Jaký je rozdíl mezi bandáží a ortézou?', 'Bandáž je měkká a elastická, ortéza má pevnější konstrukci s výztuhami nebo popruhy. U zranění nebo operace se výběr řídí radou lékaře.'),
         ('Mám nosit bandáž při každém tréninku?', 'Ne nutně. Pomůcku nosí hráči, kteří ji potřebují kvůli opoře nebo pocitu jistoty. Pokud ji máte nasazenou pořád, poraďte se s odborníkem, zda to dává smysl.'),
         ('Jak změřím velikost bandáže na koleno?', 'Změřte obvod nad čéškou a pod ní ve stoje, na holé kůži. Porovnejte s tabulkou výrobce, protože značky mají velikostní řady odlišné.'),
         ('Hodí se neopren i do horka?', 'Neopren drží teplo a vede k pocení. V horku se hodí prodyšné elastické úplety nebo perforované návleky. Při dlouhém nošení kontrolujte stav pokožky.'),
         ('Jak často praní bandáž snese?', 'Většinu návleků lze prát ručně po každých několika použitích. Záleží na materiálu a pokynech výrobce na štítku. Sušte je rozložené, mimo přímé teplo.'),
         ('Může bandáž zabránit zranění?', 'Žádná bandáž nic nezaručuje. Může poskytnout oporu nebo pocit jistoty, ale nenahrazuje rozcvičení, správnou techniku, vhodnou obuv a postupné zvyšování zátěže.'),
         ('Co dělat, když bandáž sjíždí?', 'Zkontrolujte velikost a nasazení. Pokud se sjíždí i při správné velikosti, zkuste model s protiskluzovou vrstvou nebo silikonovým lemem. Nepřitahujte ji natolik, abyste omezili krevní oběh.'),
         ('Mohou bandáže nosit děti?', 'Existují dětské velikosti, ale ve věku růstu je rozumné poradit se s lékařem nebo fyzioterapeutem. Vybírejte podle skutečného obvodu, ne na vyrůstání.'),
         ('Jak poznám, že je ortéza příliš těsná?', 'Brnění, promodrání, chlad nebo pulzování pod ortézou jsou důvod ji uvolnit nebo sundat. Správně nasazená pomůcka tlačí rovnoměrně a nebolí.'),
         ('Jak porovnat nabídky obchodů?', 'Otevřete konkrétní model a prohlédněte si nabídky obchodů vedle sebe. U bandáží kontrolujte velikost, stranu (levá, pravá) a to, zda je v balení jeden kus, nebo pár.')],
)

# ------------------------------------------------------------------ snowboarding
NEW['snowboarding'] = dict(long=True,
    title='Snowboarding: prkna, boty, vázání a výbava',
    desc='Snowboarding: snowboardy, boty, vázání, chrániče a oblečení na svah. Průvodce výběrem podle stylu jízdy, velikosti a úrovně, nabídky obchodů vedle sebe.',
    intro='<p>Na snowboardu stojíte bokem, obě nohy jsou připnuté k jednomu prkně a směr dáváte celým tělem. Díky tomu se jízda učí jinak než na lyžích a výbava má vlastní pravidla. '
          'V kategorii <strong>snowboarding</strong> najdete prkna, boty, vázání, chrániče a sety, které spojují vše potřebné pro začátek. Každý díl ovlivňuje ostatní: tužší bota potřebuje vázání s odpovídající oporou, větší boty zase širší prkno.</p>'
          '<p>Porovnáváme nabídky českých obchodů u stejných modelů, takže vidíte, kde jsou skladem velikosti a délky. Výběr začněte u <a href="/snowboardy/">snowboardů</a>, <a href="/snowboardove-boty/">snowboardových bot</a> a <a href="/snowboardova-vazani/">vázání</a>. '
          'Šetřit nemá smysl na ochraně, proto zvažte i <a href="/snowboardove-chranice/">chrániče</a> a <a href="/lyzarske-helmy/">helmu</a>. Celý obor shrnuje kategorie <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    guide='<h2>Co všechno k snowboardingu patří</h2>'
          '<p>Základní trojice se skládá z prkna, bot a vázání. K tomu přistupuje ochranná výbava a oblečení. Kdo teprve začíná, bývá ušetřen rozhodování, když sáhne po <a href="/snowboardove-sety/">snowboardovém setu</a>, v němž jsou díly sladěné. '
          'Pokročilejší jezdci si skládají výbavu po kouskách a hledí na styl jízdy, terén a pohodlí.</p>'
          + T(['Díl', 'K čemu slouží', 'Na co se při výběru dívat'], [
              ['Snowboard', 'nese jezdce a přenáší pohyb na sníh', 'délka, šířka, profil, tvrdost, styl jízdy'],
              ['Boty', 'přenášejí pohyb nohy na prkno', 'velikost, tuhost, způsob šněrování, kompatibilita s vázáním'],
              ['Vázání', 'spojují botu s prknem', 'velikost, tuhost, typ upevnění, kompatibilita s děrováním'],
              ['Helma a brýle', 'chrání hlavu a oči', 'obvod hlavy, sklo pro dané světlo, prodyšnost'],
              ['Chrániče', 'tlumí pády na zápěstí, kostrč a páteř', 'velikost, rozsah ochrany, pohodlí v pohybu'],
              ['Oblečení', 'drží teplo a suchu', 'nepromokavost, prodyšnost, pohyblivost']]) +
          '<h2>Typy snowboardů podle stylu</h2>'
          '<p>Styl jízdy určuje tvar prkna víc než cokoliv jiného. Prkna se vyrábějí ve třech hlavních variantách (all-mountain, freestyle a freeride) a čtvrtým zvláštním typem je splitboard. Liší se profilem, délkou a tvrdostí.</p>'
          '<ul><li><strong>All-mountain</strong> je univerzální prkno na upravené trasy, prašan i terénní park. Hodí se pro většinu rekreačních jezdců a začátečníků.</li>'
          '<li><strong>Freestyle</strong> je kratší a měkčí, s tvarem, který usnadňuje otáčky na překážkách a v parku. Často je symetrické, aby šlo jezdit i pozpátku.</li>'
          '<li><strong>Freeride</strong> je delší a tužší, s tvarem optimalizovaným pro vyšší rychlost a prašan. Zpravidla má širší špičku a užší zadní část.</li>'
          '<li><strong>Splitboard</strong> se dělí na dvě části a slouží k výstupům v terénu se stoupacími pásy. Je to speciální nářadí pro zkušené.</li></ul>'
          '<h2>Délka a šířka prkna</h2>'
          '<p>Starou radu, že prkno postavené na špičku má dosáhnout mezi bradu a nos, dnes výrobci doplňují vlastními tabulkami, které zohledňují hmotnost, ne výšku. '
          'Kratší prkno se snáze otáčí a hodí se začátečníkům i parkovým jezdcům, delší je stabilní při vyšší rychlosti a v prašanu. Pokud jste těžší nebo máte větší boty, hledejte širší model, aby se špička a pata nezarývaly do sněhu při zatáčce.</p>'
          + T(['Situace', 'Doporučený směr'], [
              ['první sezóny, upravené sjezdovky', 'kratší, měkčí all-mountain'],
              ['park a překážky', 'kratší a měkčí freestyle'],
              ['rychlé oblouky a hlubší sníh', 'delší, tužší prkno s užším zadkem'],
              ['velká noha (obuv nad běžnou velikostí)', 'širší model nebo široká verze'],
              ['děti', 'dětské prkno, které se nesmí zdát příliš dlouhé']]) +
          '<h2>Profil prkna a jeho vliv</h2>'
          '<p>Profil neboli rocker a camber popisuje, jak se prkno prohýbá v klidu. Camber je klasický prohyb s vyvýšením uprostřed, který dává pevné hrany a svižný odskok. '
          'Rocker je obrácený prohyb, špička a pata jsou zvednuté, takže prkno plave na sněhu a odpouští chyby. Mnoho modelů kombinuje obojí. Začátečníci častěji oceňují rocker či hybrid, protože se hrany nezachytávají o sníh.</p>'
          '<h2>Snowboardové boty</h2>'
          '<p>Bota je nejdůležitější spojnice mezi tělem a prknem. Musí sedět pevně, aby se pata nezvedala, ale nesmí tlačit prsty. Na rozdíl od lyžařské je měkčí, protože se jezdec opírá o hrany pohybem kotníku. '
          'Tuhost se uvádí jako číslo nebo popis, měkčí boty jsou vhodné pro park a začátečníky, tužší pro freeride a rychlou jízdu.</p>'
          '<ul><li><strong>Klasické tkaničky</strong> dobře drží, ale při mrazu se těžko dotahují.</li>'
          '<li><strong>Rychlošněrování</strong> funguje stažením jediného lanka a hodí se pro pohodlí.</li>'
          '<li><strong>Systém Boa</strong> používá kolečko s ocelovým lankem, které dotáhne botu otočením. Je rychlý a přesný.</li>'
          '<li><strong>Vnitřní bota</strong> se často vyjímá a suší zvlášť, což přináší výhodu při vícedenním použití.</li></ul>'
          '<p>Zkoušejte boty v ponožkách, které budete na svahu nosit, a po zavázání několik minut chodte. Teplo, pohodlí a pevná pata jsou důležitější než design. Na ponožky sáhněte do kategorie <a href="/lyzarske-ponozky/">lyžařské ponožky</a>.</p>'
          '<h2>Vázání</h2>'
          '<p>Vázání se připevňuje na prkno šrouby přes otvory na horní straně. Většina prken používá standardní děrování, ale systémy některých výrobců mají vlastní provedení, proto zjistěte předem, zda vybrané vázání s prknem sedí. '
          'Velikost se volí podle bot, ne podle prkna. Tužší vázání dává přesnější odezvu, měkčí odpouští chyby a hodí se do parku.</p>'
          + T(['Typ vázání', 'Princip', 'Pro koho'], [
              ['Klasické s popruhy', 'dva popruhy přes botu', 'všestranné použití, nejrozšířenější'],
              ['Rychlé (stepin)', 'bota se zaklapne dozadu nebo zespodu', 'pohodlí, rychlé připnutí a odepnutí'],
              ['Se zadním opěradlem sklopným', 'zadní díl se sklopí a boty se nasadí zezadu', 'snadný nástup, rekreační jezdci'],
              ['Splitboardové', 'umožňují chůzi se stoupacími pásy a jízdu', 'turisté a freeriders v terénu']]) +
          '<p>Nastavení úhlu nohou je věc osobní. Mnoho začátečníků začíná mírně rozevřenými špičkami, tedy kladným úhlem vpředu a nulovým či mírně záporným vzadu, a upravuje podle pocitu. Přesné nastavení rádi provedou ve snowboardovém servisu.</p>'
          '<h2>Regular nebo goofy</h2>'
          '<p>Regular znamená, že dopředu směřuje levá noha, goofy pravá. Který styl zvolit, zjistíte nejlépe tak, že se necháte jemně postrčit zezadu a zjistit, která noha udělá krok vpřed. '
          'Rozdíl je jen v preferenci, nelze říci, že by jeden styl byl lepší. Dobrý trik je vyzkoušet obě pozice na malém svahu nebo na umělém povrchu.</p>'
          '<h2>Bezpečnost a ochrana</h2>'
          '<p>Při snowboardingu jsou nejčastějším typem pádů pády na zápěstí a kostrč. Ochranu zápěstí řeší rukavice s výztuhou nebo samostatné chrániče, ochranu páteře a boků kalhoty a vesty z kategorie '
          '<a href="/snowboardove-chranice/">snowboardové chrániče</a>. Helma je u snowboardingu samozřejmost. Vybírejte podle obvodu hlavy a zkontrolujte ji po každém větším nárazu. '
          'K ochraně očí slouží <a href="/lyzarske-bryle/">lyžařské brýle</a> s antifogovou úpravou. Dobře padnoucí kombinaci doplní <a href="/lyzarske-rukavice/">rukavice</a> s vodotěsnou membránou.</p>'
          '<h2>Oblečení na svah</h2>'
          '<p>Na kůži patří <a href="/lyzarske-termopradlo/">termoprádlo</a>, které odvádí pot, uprostřed izolační vrstva a navrchu nepromokavá <a href="/lyzarske-bundy/">bunda</a> s <a href="/lyzarske-kalhoty/">kalhotami</a>. '
          'Snowboardisté se často dostávají do sedu a klečení, proto je důležité zesílení na sedací části a kolenou. Teplo kolem krku zajistí <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a> a hlavu <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>. '
          'Pro ty, kdo chtějí jednodílné řešení, existují <a href="/kombinezy/">kombinézy</a>.</p>'
          '<h2>Pro koho jaká výbava</h2>'
          '<h3>Úplný začátečník</h3>'
          '<p>Zvolte kratší měkčí all-mountain prkno s rockerem nebo hybridním profilem, měkké pohodlné boty a klasické vázání s popruhy. Využijte zkušební den v půjčovně, než investujete do vlastní výbavy.</p>'
          '<h3>Pokročilí na sjezdovce</h3>'
          '<p>Přejděte na tužší prkno s pevnějšími hranami, tužší boty a vázání. Ocení se rychlé zatáčky a stabilita při vyšší rychlosti.</p>'
          '<h3>Parkoví jezdci</h3>'
          '<p>Hledejte kratší a měkčí twin prkno, měkké boty a odpouštějící vázání. Součástí výbavy mají být chrániče zápěstí a páteře.</p>'
          '<h3>Děti a mládež</h3>'
          '<p>Děti rostou rychle, ale výbava na vyrůstání zhoršuje ovládání. Vybírejte raději dětské délky a boty, které dobře drží nohu, a zvažte bazar či půjčovnu.</p>'
          '<h2>Péče o výbavu</h2>'
          '<ul><li>Po jízdě otřete prkno suchým hadříkem a hrany lehce promažte, aby nerezavěly.</li>'
          '<li>Skluznici nechte pravidelně navoskovat. Vosky najdete v kategorii <a href="/lyzarske-vosky/">lyžařské vosky</a>.</li>'
          '<li>Vázání po sezóně zkontrolujte a utáhněte šroubky.</li>'
          '<li>Boty vysušte při pokojové teplotě, ne na topení, a vyjměte vložku.</li>'
          '<li>Prkno skladujte v suchu, nejlépe v obalu z kategorie <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupit příliš dlouhé prkno kvůli „růstu“ nebo víře, že delší je lepší.</li>'
          '<li>Podcenit boty a kupovat je po internetu bez zkoušení.</li>'
          '<li>Vybrat vázání, které neladí s děrováním prkna.</li>'
          '<li>Šetřit na helmě, brýlích a chráničích.</li>'
          '<li>Mít všechno nové a neodzkoušené najednou těsně před sezónou.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('burton', 'Burton'), ('nitro', 'Nitro'), ('ride', 'Ride'), ('head', 'Head'), ('raven', 'Raven'), ('gravity', 'Gravity'), ('bataleon', 'Bataleon'), ('union', 'Union'), ('k2', 'K2'), ('capita', 'Capita'), ('nidecker', 'Nidecker'), ('salomon', 'Salomon')) + '. '
          'Burton, Nitro, Ride, Bataleon a Capita patří mezi specialisty na snowboard, Union je známá vázáními, Salomon a K2 nabízejí širší zimní sortiment. Raven a Gravity jsou české či středoevropské značky se širokou nabídkou.</p>',
    faq=[('Jak vybrat délku snowboardu?', 'Řiďte se tabulkou výrobce, která kombinuje hmotnost a výšku jezdce. Obecně platí, že kratší prkno se snáze ovládá, delší je stabilnější při rychlosti.'),
         ('Jak poznat, zda jsem regular, nebo goofy?', 'Regular vede levá noha, goofy pravá. Nejlépe to poznáte při krátkém vyzkoušení na svahu nebo při prostém pokusu, kterou nohou instinktivně vykročíte vpřed při lehkém postrčení.'),
         ('Jaký je rozdíl mezi camberem a rockerem?', 'Camber je prohnutí s vyvýšením uprostřed, které dává pevné hrany a odpich. Rocker je opačný tvar se zvednutými konci, prkno snadno otáčí a odpouští chyby.'),
         ('Hodí se set pro začátečníky?', 'Ano, spojuje prkno, vázání a někdy i boty, které jsou k sobě vyladěné. Ušetříte hledání kompatibility, ale i tak je dobré boty vyzkoušet na noze.'),
         ('Na co dát pozor u bot?', 'Pata se nesmí zvedat, prsty nemají tlačit ani se bortit. Zkoušejte je s ponožkami, které budete nosit na svahu, a nechte je několik minut zavázané.'),
         ('Sedí každé vázání na každé prkno?', 'Většina používá standardní děrování, ale existují systémy s vlastním upevněním. Před koupí zkontrolujte popis u prkna i vázání, případně se zeptejte prodejce.'),
         ('Je nutná helma i chrániče?', 'Helma je u snowboardingu rozumný základ. Chrániče zápěstí, kostrče a páteře doporučují instruktoři hlavně začátečníkům a parkovým jezdcům, kdy jsou pády častější.'),
         ('Jak dlouho vydrží snowboard?', 'Záleží na četnosti jízdy, péči a terénu. Pravidelný servis hran a skluznice a suché skladování prodlouží životnost. Praskliny nebo poškozené hrany řešte u servisu.'),
         ('Kupovat novou výbavu, nebo bazar?', 'Pro děti a první sezónu je rozumný bazar nebo půjčovna. Boty a helmu raději kupujte nové, protože u nich záleží na tvaru a životnosti ochrany.'),
         ('Jak porovnat nabídky obchodů?', 'Otevřete konkrétní prkno nebo botu a prohlédněte si nabídky obchodů vedle sebe. U prken sledujte délku a šířku, u bot velikost podle evropské i palcové stupnice.')],
)

# ------------------------------------------------------------------ plavecke-bryle
NEW['plavecke-bryle'] = dict(long=True,
    title='Plavecké brýle: do bazénu, na vodu i závody',
    desc='Plavecké brýle pro bazén, otevřenou vodu, triatlon a děti: tvary, skla, těsnění a velikosti. Návod na výběr a nabídky českých obchodů vedle sebe.',
    intro='<p>Dobré plavecké brýle poznáte podle toho, že na ně během tréninku zapomenete. Netlačí kolem očí, nepouštějí vodu a sklo se nezamlžuje. Špatně padnoucí kus naopak zkazí každou délku: voda se dostane k oku, zorné pole se zamlží a člověk se vrací zpátky, aby si brýle upravil. '
          'Kategorie <strong>plavecké brýle</strong> pokrývá rekreační modely do bazénu, závodní brýle s nízkým profilem, velké masky na otevřenou vodu a dětské verze se širšími pásky.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u stejného modelu, včetně dostupných barev skel a velikostí nosního můstku. K brýlím se hodí <a href="/plavecke-cepice/">plavecké čepice</a>, <a href="/plavecke-pomucky/">plavecké pomůcky</a> a <a href="/plavky/">plavky</a>. '
          'Celý obor popisuje hlavní kategorie <a href="/vodni-sporty/">vodní sporty</a>.</p>',
    guide='<h2>Typy plaveckých brýlí</h2>'
          '<p>Brýle se liší velikostí zorného pole, hloubkou rámu a způsobem těsnění. Každý typ je vhodný pro jiný styl plavání a jinou tvář.</p>'
          + T(['Typ', 'Pro koho', 'Hlavní přednost', 'Na co dát pozor'], [
              ['Rekreační do bazénu', 'začátečníci, plavání pro zdraví, děti', 'pohodlí, měkké těsnění, nízká hmotnost', 'bývají širší a méně hydrodynamické'],
              ['Závodní (racing)', 'pokročilí a soutěžní plavci', 'nízký profil, tvrdé těsnění, minimální odpor', 'těsné, na rekreaci se mohou zdát nepohodlné'],
              ['Trénink', 'pravidelné plavání, kondiční bazénové tréninky', 'kompromis mezi komfortem a výkonem', 'rám bývá o něco větší než u závodních'],
              ['Pro otevřenou vodu', 'plavání v jezerech a moři, triatlon', 'velké zorné pole, tmavé nebo zrcadlové sklo', 'objemnější, v bazénu méně pohodlné'],
              ['Dětské', 'děti od předškolního věku', 'menší rám, široký pásek, měkké těsnění', 'rychle se z nich vyroste'],
              ['Masky a polomasky', 'plavání s nosem, snorchlování', 'zakrývají i nos', 'nehodí se pro dlouhé tempo plavání kraulem']]) +
          '<p>Pro rodiny je důležité, že velikost nemusí odpovídat věku. Dospívající může mít menší rám než dospělý, proto sledujte popisek velikosti a vždy zkoušejte přitisknutím k očním důlkům.</p>'
          '<h2>Jak brýle padnou</h2>'
          '<p>Správné posazení se ověřuje jednoduchým způsobem. Přitiskněte brýle k očím bez nasazení pásku. Pokud se přisají a drží několik sekund sami, těsnění odpovídá tvaru očního důlku. Pokud spadnou, zkuste větší či menší model, nebo jiný nosní můstek.</p>'
          '<ul><li><strong>Nosní můstek</strong> bývá výměnný nebo nastavitelný. Správná šířka zabrání prosakování mezi očima a netlačí na kořen nosu.</li>'
          '<li><strong>Těsnění</strong> z měkkého silikonu je pohodlné, závodní brýle mívají tužší okraj, který drží lépe, ale vyžaduje, aby pásek seděl přesně.</li>'
          '<li><strong>Pásek</strong> bývá jednoduchý, dělený nebo dvojitý. Dělený pásek drží pevněji nad a pod uchem, dvojitý pohodlněji zapadne na čepici.</li>'
          '<li><strong>Nastavení pásku</strong> dotahujte až poslední. Příliš utažený způsobuje tlak a rudé kruhy kolem očí, příliš volný pouští vodu.</li></ul>'
          '<h2>Skla a jejich barvy</h2>'
          '<p>Barva skla se volí podle prostředí. V krytém bazénu s umělým světlem se hodí čirá nebo lehce zbarvená skla, která dávají dobrý přehled. Na slunci nebo v otevřené vodě se prosazují tmavá, zrcadlová či polarizovaná skla, která omezují oslnění. '
          'Modré a zelené odstíny jsou oblíbené v bazénu, žlutá a oranžová zlepšují kontrast při zamračeném počasí nebo v zakalené vodě.</p>'
          + T(['Prostředí', 'Vhodné sklo'], [
              ['kryté bazény s umělým osvětlením', 'čiré nebo světlé, případně lehce zbarvené'],
              ['venkovní bazén za slunečného dne', 'tmavší nebo zrcadlové'],
              ['jezera a moře za jasného počasí', 'tmavé, zrcadlové, polarizované'],
              ['zamračeno, večer, zakalená voda', 'žluté, oranžové nebo světlé'],
              ['smíšené podmínky', 'výměnná skla, brýle se zesvětlovací vrstvou']]) +
          '<h2>Proti zamlžení a poškrábání</h2>'
          '<p>Většina brýlí má na vnitřní straně skla antifog vrstvu. Chrání před rosením, ale rychle se ztrácí, pokud ji budete utírat prsty nebo ručníkem. '
          'Brýle po koupání jen vypláchněte čistou vodou a nechte oschnout. Antifog sprej nebo kapky pomohou prodloužit životnost vrstvy. Jemné poškrábání skla nejde odstranit, takže brýle nenoste v kapse s klíči a uchovávejte je v pouzdře.</p>'
          '<h2>Dioptrické brýle</h2>'
          '<p>Kdo nosí dioptrie, může zvolit brýle s předpřipravenými dioptrickými skly. Dioptrie se udávají v dioptriích, většinou v krocích po půl dioptrii. Nejjistější postup je zjistit hodnotu u očního lékaře nebo v optice a koupit brýle odpovídající té hodnotě. '
          'Dioptrické plavecké brýle jsou jednoduchý kompromis, ale nesedí všem. Při rozdílu mezi očima nebo astigmatismu se poraďte s odborníkem o vhodném řešení.</p>'
          '<h2>Plavecké brýle pro jednotlivé aktivity</h2>'
          '<h3>Bazén a kondiční plavání</h3>'
          '<p>Pro pravidelné plavání stačí tréninkové brýle: pohodlné těsnění, dobré zorné pole a antifog. K vybavení se hodí <a href="/plavecke-cepice/">plavecká čepice</a>, která drží pásek a chrání vlasy, a <a href="/plavecke-pomucky/">pomůcky</a> na nácvik techniky.</p>'
          '<h3>Triatlon a otevřená voda</h3>'
          '<p>Při závodě v otevřené vodě nejde jen o brýle, ale i o orientaci. Velké zorné pole usnadní vyhledávání bójí. Tmavé nebo polarizované sklo zmírní odlesky. '
          'Často se kombinují s neoprenem. Podrobnosti o oblečení najdete v kategoriích <a href="/triatlon/">triatlon</a> a <a href="/neopreny/">neopreny</a>.</p>'
          '<h3>Děti a výuka plavání</h3>'
          '<p>U dětí je klíčové, aby brýle nebolely a nesklouzávaly. Hravé barvy pomáhají motivaci, ale o koupi rozhoduje těsnění a pásek. S oblečením souvisí <a href="/detske-plavky/">dětské plavky</a>, s pomůckami pak <a href="/plovaci-vesty/">plovací vesty</a>.</p>'
          '<h3>Snorchlování a rekreace u vody</h3>'
          '<p>Plavecké brýle nezakrývají nos a nepropouštějí vzduch. Pro pozorování pod hladinou se používá maska, kterou najdete v kategorii <a href="/snorchlovani/">šnorchlování</a>. Na dovolenou se hodí <a href="/plazove-doplnky/">plážové doplňky</a>, <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> a <a href="/obuv-do-vody/">obuv do vody</a>.</p>'
          '<h2>Péče o brýle</h2>'
          '<ul><li>Po každém plavání brýle opláchněte sladkou vodou, zejména po bazénu s chlórem a po moři.</li>'
          '<li>Nedotýkejte se vnitřní strany skla prsty ani ručníkem.</li>'
          '<li>Sušte na vzduchu mimo přímé slunce, které poškozuje silikon.</li>'
          '<li>Skladujte v tvrdém pouzdře, aby se nezdeformoval rám a nepoškrábalo sklo.</li>'
          '<li>Při prasklém pásku nebo roztrženém těsnění vyměňte brýle nebo díl, pokud výrobce prodává náhradu.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Kupovat podle barvy, a ne podle tvaru obličeje.</li>'
          '<li>Utáhnout pásek příliš moc kvůli prosakování, místo aby se vyřešila velikost.</li>'
          '<li>Vybrat závodní brýle na rekreační plavání, ve kterých pak člověka bolí tvář.</li>'
          '<li>Utírat antifog vrstvu a divit se, že rosí.</li>'
          '<li>Zapomenout na náhradní nosní můstek či sklo při cestě.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('speedo', 'Speedo'), ('arena', 'Arena'), ('aqua-sphere', 'Aqua Sphere'), ('tyr', 'Tyr'), ('nike', 'Nike'), ('zoggs', 'Zoggs'), ('finis', 'Finis'), ('swans', 'Swans'), ('mad-wave', 'Mad Wave'), ('zone3', 'Zone3'), ('cressi', 'Cressi'), ('aqua-speed', 'Aqua Speed')) + '. '
          'Speedo, Arena, Tyr a Finis se profilují závodním plaváním, Aqua Sphere a Zone3 otevřenou vodou a triatlonem, Zoggs a Aqua Speed rekreačním plaváním a dětskými modely, Cressi vodními sporty obecně.</p>'
          '<h2>K brýlím se hodí</h2>'
          '<p>Při plavání potřebujete funkční <a href="/panske-plavky/">pánské</a> či <a href="/damske-plavky/">dámské plavky</a>, které drží tvar i po chlóru. '
          'Na otevřené vodě se hodí skla s tmavším nebo zrcadlovým povrchem, která tlumí odlesky. Při pobytu u vody se uplatní <a href="/paddleboardy/">paddleboardy</a>, <a href="/ploutve/">ploutve</a> a jiné vodní vybavení.</p>',
    faq=[('Jaké plavecké brýle zvolit do bazénu?', 'Pro pravidelné plavání se hodí tréninkové brýle s měkkým těsněním, dobrým zorným polem a antifog vrstvou. Důležitější než značka je, aby brýle seděly kolem očí.'),
         ('Jak poznám, že brýle správně těsní?', 'Přitiskněte je k očím bez pásku. Pokud se přisají a několik sekund drží, těsnění sedí. Pokud ne, zkuste jiný nosní můstek nebo tvar.'),
         ('Proč mi brýle rosí?', 'Antifog vrstva se časem odírá, zejména při utírání prsty či ručníkem. Pomůže sprej nebo kapky na plavecké brýle, případně nový kus.'),
         ('Jaká barva skla je nejlepší?', 'Do krytého bazénu čirá nebo světlá, na slunci tmavá či zrcadlová. V zakalené vodě a za šera pomáhají žlutá nebo oranžová.'),
         ('Mohu plavat v brýlích s dioptriemi?', 'Existují modely s dioptrickými skly v různých hodnotách. Správnou hodnotu zjistěte v optice, případně se poraďte s očním lékařem o vhodném řešení.'),
         ('Jsou závodní brýle vhodné pro začátečníka?', 'Spíše ne. Mají tužší okraj a těsněji padnou, což na delší plavání nemusí být pohodlné. Začátečníkům vyhovují měkčí rekreační nebo tréninkové brýle.'),
         ('Jak často vyměnit plavecké brýle?', 'Neexistuje pevný limit. Měňte je, když těsnění ztvrdne či praskne, pásek ztratí pružnost nebo sklo zhrubne a nejde očistit.'),
         ('Jak vybrat brýle pro dítě?', 'Hledejte dětskou velikost s měkkým těsněním a širokým páskem. Nechte dítě brýle vyzkoušet, nesmí tlačit na nos ani přes ně prosakovat voda.'),
         ('Mohu brýle prát v pračce?', 'Ne. Stačí je opláchnout sladkou vodou po každém plavání a nechat uschnout. Pračka a vysoká teplota poškodí silikon i antifog vrstvu.'),
         ('Jak porovnat nabídky obchodů?', 'Otevřete konkrétní model a prohlédněte si nabídky obchodů vedle sebe. Zkontrolujte barvu skla, velikost a to, zda je v balení náhradní nosní můstek.')],
)

# ------------------------------------------------------------------ celovky-a-svitilny
NEW['celovky-a-svitilny'] = dict(long=True,
    title='Čelovky a svítilny: na túru, běh i do lesa',
    desc='Čelovky a svítilny na túru, běh, lezení, kemp i práci: svítivost, dosvit, baterie a upevnění. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p>Kdo se někdy vracel z hor za soumraku, ví, že světlo v ruce nebo na čele rozhoduje o bezpečném návratu. Čelovka nechává ruce volné pro hůlky, lano či vařič, kapesní svítilna se hodí na rychlý pohled do stanu a lucerna osvětlí celý tábor. '
          'Kategorie <strong>čelovky a svítilny</strong> sdružuje lehké čelovky pro běh a túru, výkonné modely s dosvitem na desítky metrů, kempingové lucerny, tužkové baterky a pracovní svítilny.</p>'
          '<p>Na Sportece porovnáváte nabídky českých obchodů u stejného modelu a vidíte, kde je skladem i varianta s baterií nebo bez ní. K světlu se hodí <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a>, '
          '<a href="/turisticke-batohy/">turistické batohy</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>. Celý obor řeší hlavní kategorie <a href="/outdoor/">outdoor</a>.</p>',
    guide='<h2>Typy svítilen v nabídce</h2>'
          '<p>Na první pohled se zdá, že baterka je baterka, ale konstrukce se liší podle toho, co s ní chcete dělat. Níže je přehled hlavních typů.</p>'
          + T(['Typ', 'Pro koho', 'Hlavní přednost', 'Na co dát pozor'], [
              ['Čelovka', 'turisté, běžci, lezci, kempaři', 'volné ruce, nízká hmotnost', 'držák a páska musí pohodlně sedět'],
              ['Kapesní svítilna', 'práce, kutilství, údržba, domácnost', 'úzký a dalekosáhlý paprsek, odolné pouzdro', 'v ruce zabírá jednu ruku'],
              ['Kempingová lucerna', 'tábor, stan, chata', 'rozptýlené světlo do všech stran', 'objemnější, těžší'],
              ['Tužková svítilna', 'rychlé kontroly, kapsa, příslušenství', 'velmi malá a lehká', 'omezený dosah a výdrž'],
              ['Pracovní svítilna s magnetem či stojánkem', 'dílna, auto, údržba', 'stabilně svítí bez držení', 'někdy bývá napájena síťovým kabelem'],
              ['Hurikánová a petrolejová lucerna', 'zahrada, chata, atmosféra', 'tradiční světlo, dlouhá životnost', 'pracuje s otevřeným plamenem, vyžaduje opatrnost']]) +
          '<h2>Světelný tok (lumeny) a dosvit</h2>'
          '<p>Světelný tok se udává v lumenech a vyjadřuje celkové množství vyzářeného světla. Ale číslo samo o sobě nestačí. Důležitý je tvar paprsku: široký rozptyl osvětluje okolí, úzký bodový paprsek se dostane daleko, ale ostře. '
          'Mnoho čelovek proto nabízí oba režimy. Vyšší číslo také znamená vyšší spotřebu a rychlejší vybíjení, proto se většina světla využívá jen na chvíli. Údaj o dosvitu uvádějí výrobci v metrech za zvláštních podmínek, takže berte jej jako orientační srovnání mezi modely stejného výrobce.</p>'
          + T(['Aktivita', 'Co je důležité'], [
              ['běh a trail', 'nízká hmotnost, stabilní držení, široký dobrý paprsek'],
              ['túra a trek', 'výdrž baterie, kombinace širokého a dálkového světla'],
              ['horolezectví a ferraty', 'robustnost, odolnost proti vodě, volné ruce'],
              ['kemp a stan', 'jemné rozptýlené světlo, červený režim, malá hmotnost'],
              ['rybaření a lov', 'červené nebo zelené světlo, tichost ovládání'],
              ['práce a kutění', 'odolnost, nabíjení, magnet nebo stojánek']]) +
          '<h2>Napájení: baterie, akumulátor, nabíjení</h2>'
          '<ul><li><strong>Tužkové baterie AA či AAA</strong> se kupují všude. Jsou vhodné na cesty, kde není možné nabíjet, a dají se vyměnit i uprostřed noci.</li>'
          '<li><strong>Zabudovaný akumulátor</strong> se nabíjí přes kabel. Šetří náklady při častém používání, ale bez nabíječky se vám v dlouhé výpravě vybije.</li>'
          '<li><strong>Výměnné akumulátory typu 18650</strong> se používají u výkonných svítilen. Dají se nabít v samostatné nabíječce a mít po ruce náhradní.</li>'
          '<li><strong>Hybridní systém</strong> umožňuje použít jak akumulátor, tak běžné baterie. Je to dobrý kompromis pro vícedenní výpravy.</li></ul>'
          '<p>Na dlouhé cesty bez elektřiny se vyplatí vzít <a href="/powerbanky-a-nabijeni/">powerbanku</a> a kabel. Při mrazu baterie výrazně ztrácejí kapacitu. Držte náhradní kusy v kapse u těla, ne v batohu.</p>'
          '<h2>Režimy svícení a funkce</h2>'
          '<p>Moderní čelovky mají několik režimů. Základní jsou nízký stupeň pro čtení a vaření, střední pro chůzi a plný výkon pro orientaci. Další funkce jsou praktické:</p>'
          '<ul><li><strong>Červené světlo</strong> neoslňuje spolunocležníky a šetří noční vidění. Hodí se v táboře i při rybaření.</li>'
          '<li><strong>Blikací režim</strong> upozorňuje na vás při běhu u silnice a při nouzovém signálu.</li>'
          '<li><strong>Zámek</strong> brání zapnutí v batohu, které vybije baterii.</li>'
          '<li><strong>Indikátor baterie</strong> ukáže, kdy je čas na výměnu.</li>'
          '<li><strong>Nastavitelný náklon</strong> umožní sklopit paprsek při čtení mapy.</li></ul>'
          '<h2>Odolnost proti vodě</h2>'
          '<p>Označení IPX udává odolnost proti vodě. Čím vyšší číslo, tím větší odolnost, ale přesné významy zjistíte u konkrétního výrobce. Pro túru stačí odolnost proti dešti, pro paddleboarding a lezení v dešti je rozumné hledat vyšší krytí. '
          'Svítilna určená pro potápění je jiná kategorie a v tomto výběru není. Při koupi sledujte i odolnost proti pádu a nárazu, zvláště pokud ji budete nosit na lezeckých trasách.</p>'
          '<h2>Pohodlí a upevnění</h2>'
          '<p>Čelovku neurčuje jen jas, ale i pohodlí. Dobrá čelovka má měkkou pásku, která nedrhne a nesjíždí, a držák s nastavitelným náklonem. Baterie vzadu na hlavě vyvažuje hmotnost a hodí se pro dlouhé použití. '
          'Pro běh a rychlý pohyb se dává přednost malé čelovce s lehkou páskou. K lezeckým helmám se čelovka upevňuje popruhy nebo klipy. Na delší túry se hodí také <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, kde je kapsa pro záložní světlo.</p>'
          '<h2>Pro koho jaká svítilna</h2>'
          '<h3>Turisté a trekaři</h3>'
          '<p>Základem je spolehlivá čelovka s dvěma až třemi režimy, červeným světlem a dostatečnou výdrží. Patří do každého batohu, i když plánujete návrat za světla. K výbavě patří <a href="/trekove-hole/">trekové hole</a>, <a href="/turisticke-stany/">stan</a> a <a href="/prvni-pomoc/">lékárnička</a>.</p>'
          '<h3>Běžci</h3>'
          '<p>Lehká čelovka s širokým světelným kuželem a pohodlnou páskou. Pro noční trail se hodí model s vyšším výkonem a stabilním držením. K nočnímu běhu patří také <a href="/trailove-boty/">trailové boty</a>, další vybavení najdete v části <a href="/beh/">běh</a>.</p>'
          '<h3>Lezci a skialpinisté</h3>'
          '<p>Odolnost proti vodě, nárazu a chladu je tady důležitější než maximální výkon. Čelovka musí fungovat s rukavicemi a nesmí se vypnout při úderu. Související vybavení nabízí <a href="/horolezectvi/">horolezectví</a> a <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h3>Kempaři a rodiny</h3>'
          '<p>Do stanu se hodí lucerna s jemným světlem. Čelovka zůstane v kapse pro noční výpravu na toaletu. Světlo si užijí i děti, jen pozor, aby jim nemířilo do očí. Další nápady najdete u <a href="/kemping/">kempingu</a> a <a href="/vareni-v-prirode/">vaření v přírodě</a>.</p>'
          '<h3>Rybáři a lovci</h3>'
          '<p>Volte svítilnu s červeným nebo zeleným režimem, který neplaší zvěř ani ryby. K tomu <a href="/rybareni/">rybaření</a> a <a href="/lov-a-priroda/">lov a příroda</a>.</p>'
          '<h2>Péče o svítilnu</h2>'
          '<ul><li>Nenechávejte baterie ve svítilně při dlouhém skladování, mohou vytéct.</li>'
          '<li>Po použití za deště nebo v blátě svítilnu otřete a nechte oschnout.</li>'
          '<li>Pravidelně čistěte kontakty a těsnění, aby zůstala odolnost proti vodě.</li>'
          '<li>Akumulátory skladujte částečně nabité a v suchu.</li>'
          '<li>Kontrolujte spodek čelovky, aby nebyl zasypaný pískem ani zbytky soli.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Honit se za nejvyšším číslem lumenů bez ohledu na dobu svícení a hmotnost.</li>'
          '<li>Zapomenout na náhradní baterie nebo powerbanku na vícedenní výpravu.</li>'
          '<li>Vybrat čelovku bez možnosti nastavit náklon.</li>'
          '<li>Nechat zapnutou svítilnu v batohu bez zámku.</li>'
          '<li>Počítat s tím, že se obrázek na krabici shoduje se skutečným dosvitem.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('ledlenser', 'Ledlenser'), ('silva', 'Silva'), ('petzl', 'Petzl'), ('black-diamond', 'Black Diamond'), ('nitecore', 'Nitecore'), ('olight', 'Olight'), ('lupine', 'Lupine'), ('nextorch', 'Nextorch'), ('mag-lite', 'Mag-lite'), ('feuerhand', 'Feuerhand'), ('speras', 'Speras'), ('superfire', 'Superfire')) + '. '
          'Ledlenser, Silva, Petzl a Black Diamond jsou zavedené značky čelovek pro outdoor, Nitecore, Olight a Nextorch se věnují kapesním svítilnám, Lupine špičkovým světlům pro kola a trail, Mag-lite klasickým kovovým svítilnám a Feuerhand tradičním lucernám.</p>'
          '<h2>Světla pro jiné využití</h2>'
          '<p>Při cyklistice slouží místo čelovky světla na řídítka a přilbu, která najdete v kategorii <a href="/cyklo-svetla/">cyklo světla</a>. Pro pozorování a orientaci doplňují svítilnu <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>, '
          'pro univerzální řezání, opravu a práci <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoolly</a>. Do výbavy kempu dále patří <a href="/hamaky/">hamaky</a> a <a href="/outdoor-doplnky/">outdoorové doplňky</a>.</p>',
    faq=[('Kolik lumenů potřebuji na túru?', 'Číslo samo o sobě rozhoduje málo. Pro běžnou túru stačí střední výkon s kvalitním tvarem paprsku a dostatečnou výdrží. Vyšší výkon se hodí do náročného terénu.'),
         ('Jsou lepší baterie, nebo akumulátor?', 'Baterie se dají koupit kdekoli a hodí se na cesty. Akumulátor se vyplatí při častém používání, ale potřebuje nabíjení. Hybridní modely nabízejí obojí.'),
         ('K čemu je červené světlo?', 'Neoslňuje ostatní, šetří noční vidění a v táboře nepřitahuje tolik hmyzu. Hodí se i při rybaření nebo pozorování zvěře.'),
         ('Co znamená označení IPX?', 'Udává odolnost proti vodě. Vyšší číslo znamená větší odolnost. Přesné podmínky najdete v popisu výrobce, pro běžný déšť stačí nižší krytí.'),
         ('Jak dlouho vydrží čelovka na jedno nabití?', 'Záleží na režimu a kapacitě. Výrobce udává dobu svícení při nízkém a vysokém výkonu, ale reálně se liší podle teploty a stáří baterie.'),
         ('Mám brát čelovku i na denní túru?', 'Ano, doporučuje se. Zdržení, zranění nebo špatná orientace mohou způsobit, že se vrátíte po setmění. Malá lehká čelovka zabere v batohu minimum místa.'),
         ('Co dělat v mrazu s bateriemi?', 'Baterie v zimě rychle ztrácejí kapacitu. Držte náhradní kusy v kapse u těla a čelovku v bundě, dokud ji nepotřebujete.'),
         ('Hodí se čelovka i na běh?', 'Ano, ale vybírejte lehký model s pohodlnou páskou, která nesjíždí. Pro noční trail pomůže širší světelný kužel a vyšší výkon.'),
         ('Jak uchovávat svítilnu při dlouhém skladování?', 'Vyjměte z ní baterie, uložte ji na suchém místě a pravidelně zkontrolujte akumulátory. Přebytečně vybité nebo plně nabité akumulátory ztrácejí životnost.'),
         ('Jak porovnat nabídky obchodů?', 'Otevřete konkrétní model a prohlédněte si nabídky obchodů vedle sebe. Zkontrolujte, zda je v balení baterie, nabíjecí kabel a držák na helmu.')],
)

# ------------------------------------------------------------------ extensions (extra sections appended to the guides)
NEW['bandaze-a-ortezy']['guide'] += (
    '<h2>Jak číst značení a popis u výrobku</h2>'
    '<p>V e-shopech narazíte na výrazy, které nejsou na první pohled srozumitelné. Pojem „stupeň podpory“ popisuje, jak pevně pomůcka kloub drží, a mívá tři úrovně od lehké po silnou. '
    'Lehká podpora se hodí k běžnému cvičení, silná vyžaduje pečlivější nasazení a obvykle ji doporučuje odborník. Značka „univerzální velikost“ znamená, že návlek se přizpůsobí širšímu rozpětí obvodu, ale pevnost držení se pak hůř odhaduje. '
    'Zaměřte se také na údaj, zda je výrobek oboustranný, nebo je určen na pravou či levou končetinu. U asymetrických ortéz se strany liší a záměna by vedla k nepohodlí.</p>'
    '<p>Dalším údajem je příslušenství v balení. Některé kusy mají výměnné vložky, náhradní popruhy nebo pytlík na praní, jiné jen samotný návlek. Při porovnání cen mezi obchody proto sledujte nejen cenu, ale i obsah balení a počet kusů, protože pár a jednotlivý kus se v nabídkách snadno spletou.</p>'
    '<h2>Kdy se obrátit na odborníka</h2>'
    '<p>Pomůcky z této kategorie slouží jako podpora při sportu a v běžném životě, ne jako náhrada léčby. Bolest, která se vrací, otok, ztuhnutí kloubu nebo pocit nestability jsou důvodem k návštěvě lékaře nebo fyzioterapeuta. '
    'Ti určí, zda je vhodné pomůcku nosit, jak dlouho a jakého typu, případně doporučí cviky na posílení okolních svalů. Samotný nákup bandáže potíž neřeší, a pokud ji používáte místo odpočinku, můžete si ublížit víc.</p>'
    '<h2>Cestování a ukládání</h2>'
    '<p>Bandáže zabírají v tašce málo místa, ale při skladování je dobré zavřít suchý zip a uložit kus rozložený, aby se neztrácel tvar. Do sportovní tašky patří odděleně od mokrého oblečení, nejlépe v textilním sáčku. '
    'Pokud ji vezete letadlem nebo na soustředění, přibalte náhradní kus, protože při zapomenutí v šatně se vybavení těžko shání. Mnoho týmů a oddílů má pravidla, která stanovují, jaké pomůcky se smějí nosit v zápase, takže si v případě soutěže ověřte předpisy.</p>')

NEW['snowboarding']['guide'] += (
    '<h2>Půjčovna, bazar, nebo nová výbava</h2>'
    '<p>Prvních pár dní na svahu je zbytečné platit za plnou výbavu. Půjčovny nabízejí prkno, boty i vázání po dni nebo po týdnu a poradí s nastavením. Pokud ale jezdíte pravidelně, vlastní boty se vyplatí jako první investice, protože přesně sedí na vaši nohu. '
    'Bazar a použité prkno jsou rozumnou volbou, jen u nich zkontrolujte hrany, skluznici a stav závitů pro vázání. Helmu a chrániče páteře kupujte raději nové, protože ochranná pěna se časem opotřebovává a nepoznáte, co už zažila.</p>'
    '<h2>Příprava na sezónu</h2>'
    '<p>Před první jízdou zkontrolujte, zda se šrouby vázání nepovolily, a vyzkoušejte, že se popruhy pevně zapínají. Nechte prkno naostřit a navoskovat, pokud jste ho přes léto neošetřili. '
    'Lehké protažení a posílení nohou před sezónou usnadní první dny. Mnoho jezdců využívá doma balanční prvky, například <a href="/balancni-pomucky/">balanční pomůcky</a>, a při zvýšené zátěži ocení <a href="/funkcni-trenink/">funkční trénink</a>.</p>'
    '<h2>Doprava a uskladnění</h2>'
    '<p>Prkno se na střeše auta převáží v obalu, jinak hrozí poškození skluznice a hran. Do vaku se vejdou i boty a vázání, a pokud cestujete vlakem nebo letadlem, ušetří to starosti s manipulací. '
    'Při přepravě v autě sundejte vázání z prkna nebo je alespoň nechte rozepnuté, aby se neprotlačilo skrz obal. Na chatě nebo v penzionu sušte vybavení mimo přímé teplo kamen a topení, protože vysoká teplota poškozuje lepidla v botách i skluznici.</p>')

NEW['plavecke-bryle']['guide'] += (
    '<h2>Anatomie brýlí a výměnné díly</h2>'
    '<p>Plavecké brýle se skládají z několika dílů, které se při pravidelném plavání opotřebovávají nerovnoměrně. Nejdřív bývá unavený pásek, který ztrácí pružnost a povoluje. Následuje těsnění, které tvrdne po opakovaném působení chlóru a slunce. '
    'Sklo vydrží nejdéle, ale jeho vnitřní vrstva proti zamlžení se po čase stírá. Dobré modely nabízejí výměnné nosní můstky v několika šířkách a někdy i samostatné pásky. '
    'Při nákupu proto zjistěte, zda výrobce prodává díly zvlášť, a po nutné výměně nemusíte kupovat celé brýle.</p>'
    '<h2>Brýle na vlastní tvář: jak se zorientovat</h2>'
    '<p>Každý obličej je jiný a stejný model nemusí sedět všem. Lidé s hlubokými očními důlky ocení větší a měkčí těsnění, lidé s výraznějšími lícními kostmi užší a nižší rámy. '
    'Při užším nosu a menší tváři zkuste brýle s nižším rámem a výměnným nosním můstkem v užší šířce. Kdo má větší hlavu nebo hustší vlasy, využije dělený pásek, který se dá nastavit nezávisle na spodní a horní straně. '
    'Nejjistější postup je vyzkoušet několik tvarů a zjistit, který z nich se přisaje bez pásku a netlačí na kořen nosu.</p>'
    '<h2>Jak plavat s brýlemi bez problémů</h2>'
    '<p>Nasazujte brýle nejdřív na oči a teprve potom přetáhněte pásek přes zadní část hlavy. Pokud nosíte plaveckou čepici, přetáhněte pásek přes ni, aby brýle při skoku nesklouzly. '
    'Vyhněte se tomu, aby pásek drhl o uši nebo se zamotával do vlasů. Při skoku na startovním bloku se hodí závodní brýle s pevným těsněním a pásek přes čepici, protože tlak vody při vstupu může brýle posunout.</p>'
    '<p>Před plaváním jednoduše zkontrolujte, zda máte sklo suché a čisté. Pokud brýle použijete po delší době, prohlédněte silikon, zda není popraskaný, a prstem zkuste jeho pružnost. '
    'Proti zamlžení často pomůže jednoduchý trik: sklo před vstupem do vody navlhčete čistou vodou, ne slinami, které mohou antifog vrstvu poškodit.</p>'
    '<h2>Čím se liší bazénové a venkovní plavání</h2>'
    '<p>V bazénu je voda čistá a světlo stabilní, zorné pole je důležité hlavně kvůli stěně a plavcům v dráze. V jezeře, rybníku nebo moři potřebujete vidět dál, odhadovat vzdálenost a vyhýbat se překážkám. '
    'Proto mají venkovní brýle větší sklo, měkčí těsnění a často tmavší barvu. Při plavání v otevřené vodě nikdy neplavte sami, vyhněte se místům s lodní dopravou a označte se výrazným plovákem nebo čepicí. '
    'Čepice v zářivé barvě pomáhá, aby vás ostatní viděli, a brýle samy toho moc neřeší.</p>')

NEW['celovky-a-svitilny']['guide'] += (
    '<h2>Jak číst parametry v popisu</h2>'
    '<p>Údaje u svítilen vypadají přesně, ale jejich smysl bývá zkreslený. Lumeny popisují celkový světelný tok, ne to, jak daleko dosáhne paprsek. Dosvit v metrech zase říká, kde ještě dopadá slabé světlo, což neznamená, že vidíte detaily. '
    'Doba svícení se měří obvykle při určitém výkonu a po poklesu na nižší úroveň, takže je rozumné číst graf nebo tabulku výrobce, pokud je k dispozici. '
    'Vyplatí se také sledovat, zda svítilna udržuje stálý výkon, nebo po chvíli ztlumí kvůli přehřívání. U kvalitnějších modelů je výkon regulovaný tak, že se snižuje plynule, ne skokem.</p>'
    '<h2>Světlo v přírodě a ohleduplnost</h2>'
    '<p>Silné světlo ruší zvěř, spolunocležníky i astronomy. V přírodní rezervaci nebo na vrcholu s ostatními turisty používejte spíš nižší stupně a červené světlo. '
    'Nesviťte do očí lidem, které míjíte na stezce, a při odpočinku čelovku vypněte nebo sklopte. V horách s pastvou a zvěří se tlumené světlo hodí i proto, že zbytečně neplaší zvířata. '
    'Při jízdě na kole nebo v silničním provozu používejte světla určená pro tuto činnost.</p>'
    '<h2>Příprava před výpravou</h2>'
    '<p>Před odjezdem svítilnu vyzkoušejte, zkontrolujte stav baterie a přibalte náhradní zdroj. Do batohu uložte čelovku tak, aby ji bylo možné snadno nahmatat, třeba do horní kapsy nebo víka. '
    'U delších tras doporučujeme mít dvě světla, hlavní a záložní malou, například tužkovou. Jedno světlo na čele a druhé v kapse vás zachrání při selhání nebo při potřebě svítit do dvou směrů. '
    'Při přípravě trasy počítejte s dobou, za kterou se setmí, a plánujte návrat s rezervou. Čelovka je zálohou a nesmí být důvodem k riskantním plánům.</p>')

NEW['celovky-a-svitilny']['guide'] += (
    '<p>Při sdílení stanu dohodněte pravidla předem: tlumené světlo večer, červený režim při ranním balení a čelovka namířená k zemi, ne na obličej. '
    'Takové drobnosti rozhodují o náladě skupiny víc než jas svítilny a nic nestojí.</p>')
