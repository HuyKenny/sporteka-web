"""sporteka.cz — facet landing texts wave 112: detske-termopradlo, elektrokola-vyprodej, calvin-klein-plavky, panske-polokosile.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detske-termopradlo
NEW['detske-termopradlo'] = dict(
    title='Dětské termoprádlo: velikosti, materiál a vrstvení',
    desc='Dětské termoprádlo pro lyžák, sáňkování i školu v přírodě. Jak vybrat velikost podle výšky, merino nebo syntetiku a kolik sad pořídit. Srovnání obchodů.',
    intro='<p>Dětské termoprádlo má jiný úkol než dospělé: malé dítě se u lyžařského vleku, na saních nebo při hře ve sněhu střídavě zahřívá a rychle chladne, a samo často nepoví, že mu je zima nebo že se potí. Spodní vrstva proto musí odvádět vlhkost, nedrhnout a sedět na těle jako druhá kůže. Tato stránka shrnuje, jak vybírat podle výšky dítěte místo podle věku, kdy zvolit merino a kdy syntetiku, kolik sad se vyplatí mít doma a jak prádlo vrstvit pod lyžařský overal. Porovnáte tu nabídky obchodů u dětských sad, triček a spodků a podíváte se i na prádlo, které dítě může zdědit po sourozenci.</p>',
    guide=(
        '<h2>Proč dítě nemůže nosit totéž co dospělý</h2>'
        '<p>Dítě má vzhledem k hmotnosti větší povrch těla než dospělý, takže tepelné ztráty jsou rychlejší. Zároveň se pohybuje v nárazech: pět minut zběsile běhá, pak stojí ve frontě na vlek nebo sedí na lavičce. Mokrá spodní vrstva při tomto střídání vychladne za chvíli a dítě, které si nestěžuje, se může během odpoledne dostat do nepříjemného chladu. Funkční prádlo vlhkost odvádí od kůže, takže po zastavení nezůstane na těle studená látka.</p>'
        '<p>Další rozdíl je v citlivosti pokožky. Dětská kůže snáší hůř štítky, hrubé švy a silné chemické úpravy, proto se u dětských kousků vyplatí hledat ploché švy, štítky natištěné přímo na látku a měkkou pleteninu. Obecné principy spodní vrstvy najdete v hlavní kategorii <a href="/termopradlo/">funkční a termo prádlo</a>; níže se věnujeme jen tomu, co je specifické pro děti.</p>'
        '<h2>Velikost podle výšky, ne podle věku</h2>'
        '<p>Dětské termoprádlo se prodává podle tělesné výšky v centimetrech, nikoli podle věku. Věk je jen orientační údaj, protože dvě stejně staré děti se mohou lišit o dvě velikosti. Změřte dítě bez bot, ve stoje u zdi, a porovnejte výšku s tabulkou výrobce. Jestliže je mezi dvěma velikostmi, vezměte u funkčního prádla spíš menší: spodní vrstva musí přiléhat, jinak mezi látkou a kůží zůstane vzduch a odvod potu nefunguje. Naopak u dítěte, které rychle roste, nechte rukávy a nohavice krátce přesahovat, protože přiléhavý střih je pružný.</p>'
        + T(['Výška dítěte', 'Orientační věk', 'Na co dbát'], [
            ['86–98 cm', 'batole až předškolák', 'snadné oblékání, rozparek nebo pružný pás, žádné hrubé štítky'],
            ['104–116 cm', 'předškolák až prvňáček', 'dlouhé rukávy bez škrcení, nohavice do ponožek'],
            ['122–134 cm', 'mladší školák', 'sady triko plus spodky, delší trup a ruce'],
            ['140–152 cm', 'starší školák', 'střihy blízké dospělým, větší rozdíl mezi dívčími a chlapeckými tvary'],
            ['158 cm a víc', 'teenager', 'často se vyplatí zkusit pánskou nebo dámskou XS, protože sedí lépe']]) +
        '<p>Věkové údaje v tabulce jsou jen hrubé vodítko. Nejspolehlivější je tabulka přímo u produktu, protože každý výrobce počítá s mírně jiným střihem. Pro dospívající, kteří dorostli do vyšších velikostí, se podívejte i na nabídku <a href="/termopradlo-panske/">pánského termoprádla</a> a <a href="/termopradlo-damske/">dámského termoprádla</a>, kde bývá užší velikost XS.</p>'
        '<h2>Syntetika, merino nebo směs</h2>'
        '<p>Pro děti platí stejné rozdělení materiálů jako pro dospělé, ale priority se mění. Syntetika (polyester, polyamid, polypropylen) rychle schne, přečká časté praní a zvládne stálé trhání, takže je rozumným základem. Merino vlna hřeje i mírně vlhká, nepáchne a bývá příjemná na kůži, ale je dražší na údržbu, pomaleji schne a při divokém dětském provozu se prodře dřív. Dobrým řešením je směs, kde vlna dodává pohodlí a syntetika odolnost.</p>'
        '<ul><li><strong>Syntetické prádlo:</strong> pro aktivní lyžování, běh, každodenní nošení ve škole a pro děti, které spodní vrstvu rychle ušpiní.</li>'
        '<li><strong>Merino a směsi s vlnou:</strong> pro děti, které se v zimě často potí a zároveň mrznou, pro dlouhé dny venku a pro cestování, kde se prádlo nemusí prát každý večer.</li>'
        '<li><strong>Bavlna:</strong> jen na klidné dny doma; při pohybu nasákne a vychladne.</li></ul>'
        '<p>Pokud má dítě atopickou nebo citlivou pokožku, vyzkoušejte nejdřív kratší nošení, protože vlna dráždí individuálně. Trička z jemné vlny najdete mezi <a href="/merino-tricka/">merino tričky</a> a teplé ponožky v kategorii <a href="/merino-ponozky/">merino ponožky</a>.</p>'
        '<h2>Značky v nabídce a komu se hodí</h2>'
        '<p>V dětských kouscích se nejčastěji objevují české a středoevropské značky zaměřené na lyžování a outdoor, například ' + B(('sensor', 'Sensor'), ('klimatex', 'Klimatex'), ('progress', 'Progress'), ('alpine-pro', 'Alpine Pro'), ('viking', 'Viking'), ('craft', 'Craft')) + '. Severské značky orientované na děti, například ' + B(('reima', 'Reima'),) + ', myslí na dětské střihy od základu. Ve výběru jsou také ' + B(('lasting', 'Lasting'), ('arcore', 'Arcore'), ('dare2b', 'Dare2b'), ('husky', 'Husky'), ('kilpi', 'Kilpi'), ('odlo', 'Odlo')) + '. Značky se liší hlavně střihem, tloušťkou pleteniny a tím, zda nabízejí samostatné díly nebo celé sady.</p>'
        '<p>Chcete-li dítě vybavit na jednu zimní sezónu, stačí obvykle sada od středně známé značky. Pro dítě, které lyžuje pravidelně v kroužku nebo v závodním oddíle, se vyplatí pevnější pletenina s výztuží v místech otěru. Nejlepší je porovnat několik sad vedle sebe, protože stejná značka může mít několik řad pro různé aktivity.</p>'
        '<h2>Jak dítě obléknout vrstvu po vrstvě</h2>'
        '<ol><li><strong>Spodní vrstva:</strong> termoprádlo s dlouhým rukávem a dlouhé spodky přímo na kůži, bez spodního prádla z bavlny navíc, pokud to výrobce nedoporučuje.</li>'
        '<li><strong>Střední vrstva:</strong> fleece nebo lehká mikina, která hřeje a zároveň propouští vlhkost.</li>'
        '<li><strong>Svrchní vrstva:</strong> lyžařská bunda a kalhoty nebo overal chránící před větrem a mokrem, viz <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a> a <a href="/lyzarske-bundy/">lyžařské bundy</a>.</li>'
        '<li><strong>Doplňky:</strong> čepice, nákrčník, rukavice a ponožky, které se podrobněji řeší u <a href="/lyzarske-ponozky/">lyžařských ponožek</a> a <a href="/lyzarske-rukavice/">lyžařských rukavic</a>.</li></ol>'
        '<p>Hlavní pravidlo zní, že tepla neubude, když oblečete více vrstev přes sebe. Příliš těsný oblek zabrání proudění vzduchu a dítě se zahřeje a zpotí. Raději zvolte tenké vrstvy a během dne je přidávejte nebo ubírejte podle toho, jak dítě vypadá, zda má studené ruce a krk nebo naopak vlhké vlasy.</p>'
        '<h2>Kolik sad koupit a jak je prát</h2>'
        '<p>Pro týdenní lyžařský kurz nebo školu v přírodě se vyplatí mít alespoň dvě až tři sady, aby se dalo střídat a prát. Pro pobyt doma stačí jedna sada na týden s rezervou na nehody. Během sezóny se hodí i lehčí prádlo na běžný den ve škole a tlustší na mráz. Vyhněte se přehnanému předzásobení, protože děti rychle vyrostou.</p>'
        '<ul><li>Perte při teplotě uvedené na štítku, obvykle třicet až čtyřicet stupňů, a jemným pracím prostředkem.</li>'
        '<li>Nepoužívejte aviváž, protože zanáší vlákna a snižuje odvod vlhkosti.</li>'
        '<li>Prádlo ze směsí s vlnou sušte na vzduchu, syntetické po vyprání rychle uschnou i na radiátoru, ale ne přímo na něm.</li>'
        '<li>Před praním zavřete zipy a suché zipy, aby nedrhly.</li></ul>'
        '<h2>Prádlo po sourozenci a na přenos</h2>'
        '<p>Dětské termoprádlo se dobře předává dál, pokud je pletenina zachovalá a nemá ztracenou pružnost. Zkontrolujte lokty, kolena a manžety. Prádlo, které zešedlo nebo se vytahalo, už nevede vlhkost tak, jak má. U velikostí o stupeň větších není radno kupovat prádlo předem: volná spodní vrstva se překládá a tře, takže s příliš velkou velikostí dítě neušetří, spíše mu bude nepohodlně.</p>'
        '<h2>Kde dětské termoprádlo využijete</h2>'
        '<p>Nejčastější využití je lyžařský kurz, sáňkování, bruslení a pobyt na horách. Funkční vrstva se ale hodí i k běžnému chladnému dni ve škole, při procházkách se psem nebo při pobytu na hřišti. Pro spaní venku se hodí v kombinaci s teplými <a href="/detske-spacaky/">dětskými spacáky</a>, kde spodní vrstva přidává pár stupňů komfortu. Pro začínající lyžaře tu je i širší nabídka kategorie <a href="/detske-lyze/">dětské lyže</a>, kde je dobré myslet na to, že dítě se v oblečení musí volně hýbat.</p>'
        '<p>Pro rodiče malých dětí je rozhodující rychlost oblékání: sada s jemným pasem, bez nepohodlných knoflíků a s dostatečně širokým výstřihem usnadní každodenní rutinu. Pro starší děti je naopak důležitější vzhled a střih, protože prádlo, které se jim líbí, ho skutečně nosí.</p>'
    ),
    faq=[
        ('Jak poznám, jakou velikost dětského termoprádla koupit?', 'Změřte dítě bez bot a porovnejte výšku v centimetrech s tabulkou výrobce. Věk je jen orientační. Mezi dvěma velikostmi zvolte u spodní vrstvy spíše menší, protože má přiléhat. Konkrétní rozměry se u značek mírně liší, proto se vždy dívejte na tabulku u daného produktu.'),
        ('Je lepší pro dítě merino, nebo syntetika?', 'Syntetika je odolnější, rychle schne a snáší časté praní, proto je rozumnou volbou pro aktivní děti. Merino je příjemné na kůži a nepáchne, ale je citlivější na praní a opotřebení. Mnoho rodičů volí směs. Rozhodněte podle toho, jak dítě prádlo používá a zda mu vlna nevadí.'),
        ('Může dítě nosit termoprádlo celý den ve škole?', 'Ano, pokud je to tenčí prádlo a ve třídě není přetopeno. V teple se dítě může zpotit, i když látka vlhkost odvádí. Na vyučování se hodí lehká vrstva, na dlouhý pobyt venku tlustší. Dítě by se mělo cítit sucho, ne zahřáté.'),
        ('Pod lyžařský overal bundu nebo mikinu?', 'Na spodní vrstvu přijde termoprádlo, na něj tenká mikina nebo fleece a teprve potom overal nebo bunda. Pod overal nedávejte tlustý svetr, protože zabrání proudění vzduchu a dítě se zahřeje. Raději používejte několik tenkých vrstev, které se dají ubírat.'),
        ('Kolik sad dětského termoprádla potřebuji?', 'Na týdenní lyžařský kurz se vyplatí dvě až tři sady, aby se střídaly a mohly se prát. Pro běžné používání doma stačí jedna sada s rezervou. Sady se dají kombinovat po dílech, takže pokud je jedna část špinavá, zbytek lze použít s jinou.'),
        ('Dá se dětské termoprádlo prát v pračce a jak často?', 'Dá, obvykle při třiceti až čtyřiceti stupních, bez aviváže a jemným prostředkem. Po každém intenzivním použití je rozumné prát, protože pot zanáší vlákna. Merino a směsi s vlnou přežijí delší nošení bez praní lépe než syntetika, ale ani ty není dobré zanedbávat.'),
        ('Je termoprádlo vhodné pro děti s citlivou pokožkou?', 'Může být, pokud je měkké, bez drsných švů a štítků. Hledejte ploché švy a jemnou pleteninu. Syntetika bývá často snesitelnější než hrubší vlna, ale u jemného merina záleží na dítěti. Při první zkoušce nenoste prádlo celý den, ale jen několik hodin.'),
        ('Má smysl kupovat prádlo o číslo větší, aby dítě vyrostlo?', 'U spodní vrstvy to nedoporučujeme. Volná látka se mačká, tře a nepřenáší pot, takže funkce klesá. Lepší je koupit odpovídající velikost a po sezóně ji předat dál nebo dokoupit další. Přiléhavý střih je pružný a malé rozdíly ve výšce snese.'),
        ('Do čeho oblékat dítě při sáňkování a bruslení?', 'Použijte stejný princip jako při lyžování: spodní vrstva z funkčního materiálu, střední z fleecu a svrchní vrstva proti větru a vlhku. Při sáňkování dítě sedí a méně se hýbe, proto hlídejte hlavně ruce, nohy a krk. Při bruslení se spíš zahřeje, takže vrstev může být méně.'),
    ],
)

# ------------------------------------------------------------------ elektrokola-vyprodej
NEW['elektrokola-vyprodej'] = dict(
    title='Elektrokola výprodej: jak poznat skutečnou slevu',
    desc='Elektrokola ve výprodeji: kdy se slevuje, na co si dát pozor u baterie, záruky a servisu a jak poznat skutečně dobrou nabídku. Porovnání obchodů.',
    intro='<p>Výprodej elektrokol láká, protože jde o jednu z nejdražších věcí, které se v sortimentu sportovního zboží prodávají. Zároveň je to zboží s baterií, motorem a elektronikou, kde se sleva může skrývat za zastaralým modelem, starší výrobní sérií nebo baterií, která dlouho ležela ve skladu. Na této stránce najdete elektrokola, u kterých obchody uvádějí snížení ceny oproti dřívější nabídce. Průvodce níže vysvětluje, kdy se opravdu slevuje, jak ověřit stáří modelu, na co se zeptat u baterie, jaká je role záruky a servisu a které typy kol se nejlépe vyprodávají. Nechybí kontrolní seznam, který si můžete vzít k obchodu nebo k objednávce.</p>',
    guide=(
        '<h2>Kdy se u elektrokol skutečně slevuje</h2>'
        '<p>Elektrokola mají sezónní rytmus. Největší zájem je na jaře, kdy se lidé chystají na výlety a dojíždění, proto se v tu dobu slevuje nejméně. Nejvíce snížených cen se objevuje na podzim a v zimě, kdy obchody uvolňují sklad pro další modelový ročník. Další vlna přichází při představení nových modelů, často koncem léta, kdy výrobci mění barvy, komponenty nebo software motoru. Slevy bývají také při kampaních typu Black Friday nebo v době, kdy se obchod zbavuje vystavených kusů.</p>'
        '<p>Neznamená to, že každá sleva je dobrá. Nejlepší jsou slevy na model, který se nezměnil technicky, jen vyšel nový ročník nebo nová barva. Nejméně zajímavé jsou slevy na kus, který se nerozprodává proto, že by byl zastaralý, ale protože má potíže s dostupností servisních dílů. Obchod to vám obvykle sám neřekne, proto je dobré znát otázky, které se vyplatí položit.</p>'
        '<h2>Jak poznat skutečnou slevu</h2>'
        '<ul><li><strong>Sledujte historii nabídky:</strong> stejný model často visí u více obchodů, takže porovnání ukáže, zda je sleva skutečná, nebo jde o nafouknutou původní cenu.</li>'
        '<li><strong>Zjistěte modelový rok:</strong> ročník bývá v názvu nebo v popisu; starší ročník bez rozdílu v komponentech je dobrý nákup, starší ročník s jiným motorem nebo baterií je potřeba zvážit.</li>'
        '<li><strong>Ověřte výrobní datum baterie:</strong> na štítku nebo v servisním menu bývá rok výroby a počet nabíjecích cyklů.</li>'
        '<li><strong>Zjistěte, zda je kolo nové, vystavené nebo vrácené:</strong> vystavené nebo vrácené kolo může mít drobné stopy použití.</li>'
        '<li><strong>Zkontrolujte, co je v ceně:</strong> nabíječka, klíče, blatníky nebo světla bývají součástí, ale ne vždy.</li></ul>'
        '<p>Obecné rady pro výběr kola, motoru a baterie najdete v hlavní kategorii <a href="/elektrokola/">elektrokola</a>; tady se soustředíme na to, co je při slevě jiné.</p>'
        '<h2>Baterie: nejdůležitější a nejdražší součást</h2>'
        '<p>Baterie je u elektrokola nejdražší a nejcitlivější součást. Lithium-iontové články stárnou nejen používáním, ale i časem a způsobem skladování. Baterie, která je několik let plně nabitá nebo úplně vybitá ve skladu, může mít menší kapacitu, než slibuje štítek. Proto se u slevy vyplatí zeptat, kdy byla baterie vyrobena, zda byla v obchodě dobíjena a jak dlouho kolo stálo.</p>'
        '<p>Na kapacitu se dívejte v watthodinách (Wh), ne jen v ampérhodinách: Wh vyjadřuje skutečné množství energie a dá se porovnat napříč napětími. Zkontrolujte také, zda se baterie vyjímá, protože bez vyjímatelné baterie se kolo složitě dobíjí v bytě a zhoršuje se přístup k výměně. Cena nové baterie může tvořit velkou část původní ceny kola, takže při výprodeji rozhodněte, zda má smysl koupit kolo s nepříliš čerstvou baterií, nebo raději o něco dražší s novou.</p>'
        '<h2>Záruka, servis a díly</h2>'
        '<p>U elektrokol je záruka jednou z hlavních věcí, které slevovou nabídku ospravedlňují nebo znehodnocují. Zákonná záruka platí pro nové zboží stejně jako za plnou cenu, ale baterie se podle obchodních podmínek často posuzuje samostatně a může mít kratší lhůtu. Zeptejte se, kdo kolo servisuje, zda je v blízkosti autorizovaný servis a jak dlouho se čeká na díly.</p>'
        + T(['Otázka', 'Proč na ní záleží'], [
            ['Je kolo nové, nebo vystavené?', 'stopy použití a délka skladování ovlivňují stav baterie a lakování'],
            ['Jaký je modelový rok?', 'novější ročník má často lepší software a dostupnější díly'],
            ['Kdo kolo servisuje?', 'servis a diagnostika motoru často řeší jen autorizovaná dílna'],
            ['Jaká záruka platí na baterii?', 'baterie bývá posuzována zvlášť a stárne rychleji než zbytek kola'],
            ['Dá se dokoupit náhradní baterie a nabíječka?', 'bez náhradních dílů se kolo po pár letech obtížně udržuje'],
            ['Co je v balení?', 'světla, blatníky a nosič mohou chybět a doplnit je stojí navíc']]) +
        '<p>Elektrokolo koupené mimo obvyklý prodej, například od neznámého dovozce, může být za zlomek ceny, ale servis se tu hledá obtížně. Naopak u etablovaných značek má i zlevněné kolo obvykle dílenskou podporu.</p>'
        '<h2>Které typy elektrokol se nejčastěji vyprodávají</h2>'
        '<p>Výprodeje se nejčastěji týkají jednodušších typů, které se vyrábějí ve velkých sériích, a modelů, kterým končí ročník. Pro každodenní dojíždění jsou to <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>, pro víkendové výlety <a href="/horska-elektrokola/">horská elektrokola</a> a pro byt <a href="/skladaci-elektrokola/">skládací elektrokola</a>. Specializovaná kola, například <a href="/nakladni-elektrokola/">nákladní</a>, <a href="/fatbike-elektrokola/">fatbike</a> nebo <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel</a>, se slevují méně často, ale když, bývá to výrazné.</p>'
        '<p>Pro rodiny je zajímavá nabídka <a href="/damska-elektrokola/">dámských elektrokol</a> s nízkým nástupem i <a href="/detska-elektrokola/">dětských elektrokol</a>. U dětských dbejte na hmotnost a maximální rychlost, protože rozdíl mezi dětským a dospělým kolem je zásadní. Pro uživatele hledající stroj pro muže je tu odkaz na <a href="/panska-elektrokola/">pánská elektrokola</a>.</p>'
        '<h2>Značky ve výprodeji</h2>'
        '<p>V nabídce se objevují jak specializovaní výrobci, jako ' + B(('specialized', 'Specialized'), ('trek', 'Trek'), ('crussis', 'Crussis')) + ', tak značky zaměřené na přímý prodej přes internet, například ' + B(('engwe', 'Engwe'), ('fafrees', 'Fafrees'), ('samebike', 'Samebike'), ('onesport', 'Onesport'), ('hitway', 'Hitway'), ('evercross', 'Evercross')) + '. Rozdíl je v tom, jak se kolo servisuje a jak dostupné jsou náhradní díly. Zavedené značky mají dealerskou síť, přímé značky spoléhají na servis dodavatele nebo na univerzální díly. Při porovnání se podívejte i na konkrétní kombinaci motoru, baterie a komponentů, ne jen na značku.</p>'
        '<p>Při hledání zajímavých kusů zkuste také stránku <a href="/elektrokola-crussis/">elektrokola Crussis</a> pro kola české značky, kde je servisní zázemí často snazší.</p>'
        '<h2>Převzetí a první jízda</h2>'
        '<p>Elektrokola se často dodávají částečně složená, s řidítky a pedály v krabici. Pokud nejste zběhlí v seřizování, nechte kolo před první jízdou zkontrolovat v dílně: brzdy, dotažení šroubů, tlak v pneumatikách a nastavení displeje rozhodují o bezpečnosti. Hlavně u kol z přímého prodeje je kontrola rozumná pojistka, protože výrobní závod složí kolo rychle a často bez individuálního seřízení.</p>'
        '<p>Při první jízdě vyzkoušejte všechny stupně podpory, brzdy při rozjezdu a chování motoru ve stoupání. Pokud motor vynechává, displej hlásí chybu nebo se baterie rychle vybíjí, reklamujte kolo ihned, dokud je v záruční lhůtě a nemáte pochybnosti o příčině. Nezapomeňte také zkontrolovat nabíječku: měla by být originální a odpovídat napětí baterie.</p>'
        '<h2>Kontrolní seznam před koupí zlevněného elektrokola</h2>'
        '<ol><li>Zjistěte přesný model, ročník a velikost rámu a ověřte, že sedí pro vaši výšku.</li>'
        '<li>Zeptejte se na stáří baterie a stav nabití, případně na počet nabíjecích cyklů.</li>'
        '<li>Zkontrolujte, co je součástí balení, zejména nabíječku, klíče a displej.</li>'
        '<li>Ověřte záruku na rám, motor a baterii a podmínky vrácení.</li>'
        '<li>Zjistěte nejbližší servis a dostupnost náhradních dílů.</li>'
        '<li>Porovnejte stejný model u více obchodů, včetně dopravy a případného složení kola.</li>'
        '<li>Po převzetí zkontrolujte kolo před první jízdou a vyzkoušejte všechny stupně podpory.</li></ol>'
        '<p>Zlevněné elektrokolo je dobrý nákup, pokud víte, co kupujete a kdo vám pomůže, až se něco pokazí. Sleva, která tyto otázky nezodpoví, často jen přesouvá náklady na pozdější dobu.</p>'
    ),
    faq=[
        ('Kdy se elektrokola nejvíc zlevňují?', 'Nejčastěji na podzim a v zimě, kdy obchody uvolňují sklad pro nové ročníky, a při větších kampaních, například Black Friday. Na jaře je poptávka největší, proto jsou slevy menší. Přesné termíny se různí podle obchodu a značky, proto se vyplatí sledovat nabídku dlouhodoběji.'),
        ('Je zlevněné elektrokolo horší než nové za plnou cenu?', 'Nemusí být. Často jde o stejný model z minulého ročníku nebo o jinou barvu. Potíž je jen tehdy, pokud je baterie starší nebo je kolo zastaralé a špatně se servisuje. Ověřte rok výroby a dostupnost servisu a pak se můžete rozhodovat jen podle ceny.'),
        ('Jak ověřím, že je baterie v dobrém stavu?', 'Zeptejte se na datum výroby, počet nabíjecích cyklů a to, jak dlouho kolo stálo. U vystavených nebo vrácených kusů si vyžádejte informaci o použití. Po převzetí baterii nabijte a sledujte, zda displej ukazuje rozumný dojezd. Zjevně slabý výkon reklamujte.'),
        ('Platí na zlevněné elektrokolo stejná záruka?', 'U nového zboží platí zákonná záruka stejně jako za plnou cenu. Baterie se ale často posuzuje zvlášť a lhůta může být kratší, než u rámu nebo motoru. U vystavených či použitých kusů se podmínky mohou lišit. Vše si ověřte v obchodních podmínkách před objednáním.'),
        ('Na co si dát pozor u neznámých značek?', 'Hlavně na servis a dostupnost náhradních dílů. Kolo může být zajímavé na papíře, ale bez dealerské sítě se opravy komplikují. Zeptejte se, kdo kolo servisuje, jak se objednávají baterie a nabíječky a jaké jsou reklamační lhůty. Pomoci může i recenze od skutečných uživatelů.'),
        ('Kolik ampérhodin nebo watthodin má baterie mít?', 'Záleží na využití. Pro dojíždění po rovině stačí menší kapacita, pro hory a dlouhé trasy je užitečná větší. Porovnávejte ve watthodinách, protože údaj v ampérhodinách bez napětí nic neříká. Dojezd závisí také na hmotnosti jezdce, terénu a stupni podpory.'),
        ('Je lepší koupit zlevněné skládací, nebo horské elektrokolo?', 'Záleží na účelu. Skládací kolo se hodí do bytu, vlaku nebo na loď a pro krátké trasy. Horské kolo se hodí do terénu a na kopce, ale vyžaduje více údržby. Pro každodenní dojíždění po městě bývá nejpraktičtější trekingové nebo městské kolo s blatníky a nosičem.'),
        ('Mohu elektrokolo po koupě vrátit?', 'U nákupu přes internet platí obecně právo odstoupit od smlouvy ve stanovené lhůtě, ale podmínky se u jednotlivých obchodů liší, zejména u kol, která už byla použita. Před objednáním si přečtěte pravidla vrácení a zjistěte, kdo hradí dopravu u velkého a těžkého zboží.'),
        ('Jak poznám, že je sleva skutečná?', 'Porovnejte stejný model u více obchodů a sledujte, jak se nabídka vyvíjí. Všímejte si modelového roku a toho, zda se změnil motor nebo baterie. Sleva je zajímavá, pokud kolo stále odpovídá současné nabídce značky a pokud je servis a záruka v pořádku.'),
    ],
)

# ------------------------------------------------------------------ calvin-klein-plavky
NEW['calvin-klein-plavky'] = dict(
    title='Calvin Klein plavky: dámské, pánské a jak vybrat',
    desc='Calvin Klein plavky: jednodílné, bikiny, plavkové kalhotky a pánské koupací šortky. Střih, velikosti a kombinace dílů, srovnání nabídek obchodů.',
    intro='<p>Calvin Klein plavky patří do módnější části plavkového sortimentu: nejde o závodní kusy pro pravidelné plavání, ale o plážové a bazénové oblečení s minimalistickým vzhledem a výrazným logem. V nabídce najdete především jednodílné dámské plavky, horní a spodní díly bikin, plavkové podprsenky a kalhotky, a také pánské koupací šortky různých délek. Níže se dozvíte, jak se jednotlivé typy střihů liší, jak vybírat velikost a které díly spolu kombinovat, jak plavky nosit u bazénu i u moře a jak je ošetřovat. Dostanete také srovnání s jinými značkami a poznáte, kdy je lepší sáhnout po sportovních plavkách, které pro pravidelné plavání obstojí líp.</p>',
    guide=(
        '<h2>Co v sortimentu Calvin Klein plavek najdete</h2>'
        '<p>Značka Calvin Klein vychází z módy a spodního prádla, a to je na plavkách vidět. Převažují jednoduché barvy, hladké tvary a logo na pásku nebo na hrudi. Ve výběru se objevují dámské kousky v několika střizích a pánské šortky. Pro děti se podívejte do kategorie <a href="/detske-plavky/">dětské plavky</a>, kde je výběr širší. Hlavní skupiny jsou:</p>'
        '<ul><li><strong>Jednodílné plavky:</strong> hladký střih, často s vyšším zadním dílem a širšími ramínky.</li>'
        '<li><strong>Horní díly bikin:</strong> plavkové podprsenky, trojúhelníčkové a sportovnější topy.</li>'
        '<li><strong>Spodní díly bikin a kalhotky:</strong> klasické, vyšší v pase nebo s bočními pásky.</li>'
        '<li><strong>Pánské koupací šortky:</strong> střední délky, s tkaničkou a vnitřním slipem nebo bez něj.</li></ul>'
        '<p>Ve srovnání s kategorií <a href="/plavky/">plavky</a> jako celkem je tato stránka zaměřená na módní segment. Podrobnější rady o materiálech, ochraně proti chloru a velikostech jsou v hlavní kategorii; zde se věnujeme tomu, co je typické pro tuto značku.</p>'
        '<h2>Střih a styl: čím se liší od sportovních plavek</h2>'
        '<p>Plavky určené pro sport jsou navrženy tak, aby při plavání nepřekážely, odolávaly chlóru a při zrychlení zůstaly na místě. Módní plavky mají jiné priority: dobrý vzhled na pláži, pohodlí při opalování a snadnou kombinaci s oblečením. To neznamená, že se v nich nedá plavat, ale při pravidelném tréninku jsou praktičtější sportovní modely, například značek ' + B(('speedo', 'Speedo'), ('arena', 'Arena')) + '. Srovnání jejich nabídek najdete na stránkách <a href="/speedo-plavky/">Speedo plavky</a> a <a href="/arena-plavky/">Arena plavky</a>.</p>'
        '<p>Calvin Klein plavky se obvykle nosí u bazénu hotelu, na pláži a při krátkém koupání. Pro tyto situace stačí dobrá střihová a materiálová kvalita, nejdůležitější je pohodlí a správná velikost. Při intenzivním plavání v chlorované vodě se doporučuje plavky po každém použití opláchnout, protože chlór a slaná voda zkracují životnost elastických vláken.</p>'
        '<h2>Velikosti: jak vybrat správnou</h2>'
        '<p>U dámských dílů se běžně setkáte s písmennými velikostmi, u pánských šortek s písmeny nebo s obvodem pasu. Střih je spíše přiléhavý, ale ne kompresní. Podívejte se do tabulky u produktu, protože každý typ má jiné rozměry. Změřte obvod hrudníku pod prsy, přes nejplnější část prsou, obvod pasu a boků a porovnejte je s údaji výrobce.</p>'
        + T(['Typ plavek', 'Co změřit', 'Na co si dát pozor'], [
            ['Jednodílné plavky', 'hrudník, pas, boky a délka trupu', 'u dlouhého trupu zvažte větší velikost, aby ramínka netlačila'],
            ['Horní díl bikin', 'obvod pod prsy a přes prsa', 'podprsenka musí držet bez škrcení, popruhy nemají zarývat'],
            ['Spodní díl bikin', 'boky a pas', 'vyšší střih potřebuje delší stehno, nižší střih odkryje víc'],
            ['Pánské šortky', 'pas a délka nohavice', 'šortky mají sedět na bocích, ne klouzat při chůzi z vody']]) +
        '<p>Pokud jste na hranici dvou velikostí, vyberte podle nejméně pohodlné části těla: u kalhotek podle boků, u podprsenky podle obvodu pod prsy. Plavky se po namočení mírně roztáhnou, takže příliš volná velikost po pár koupáních sedí hůř.</p>'
        '<h2>Jak kombinovat díly a typy</h2>'
        '<p>Dvoudílné plavky se prodávají jako samostatné horní a spodní díly, což umožňuje kombinovat velikosti a barvy. Pokud má horní část jiný obvod než spodní, nemusíte kupovat větší velikost celé sady. Pro stejný vzhled hledejte stejnou řadu, protože odstíny černé, bílé nebo béžové se mezi řadami mohou mírně lišit.</p>'
        '<ul><li><strong>Pro pohodlí na pláži:</strong> jednodílné plavky nebo bikiny s pevnějším střihem.</li>'
        '<li><strong>Pro opalování bez viditelných pásů:</strong> topy bez ramínek a nízké kalhotky.</li>'
        '<li><strong>Pro aktivnější koupání:</strong> jednodílné plavky nebo sportovnější top s širokými ramínky.</li>'
        '<li><strong>Pro dovolenou s minimem zavazadel:</strong> neutrální barvy, které se dají kombinovat mezi sebou.</li></ul>'
        '<p>Podrobnější přehled podle pohlaví najdete v kategoriích <a href="/damske-plavky/">dámské plavky</a> a <a href="/panske-plavky/">pánské plavky</a>. Pro porovnání s jinými módními značkami se podívejte na stránku <a href="/damske-plavky-calvin-klein/">dámské plavky Calvin Klein</a>.</p>'
        '<h2>Značka v kontextu ostatních</h2>'
        '<p>Mezi módními a sportovními značkami plavek je Calvin Klein spíše v módní části. Sportovní značky jako ' + B(('nike', 'Nike'), ('adidas', 'Adidas')) + ' kladou větší důraz na odolnost materiálu a střih pro plavání, vedle nich se dají porovnat nabídky na stránkách <a href="/plavky-nike/">plavky Nike</a> a <a href="/plavky-adidas/">plavky Adidas</a>. Značky jako ' + B(('roxy', 'Roxy'),) + ' se zaměřují na surfový styl, viz <a href="/roxy-plavky/">plavky Roxy</a>. Calvin Klein osloví ty, kdo hledají jednoduchý minimalistický vzhled a rozpoznatelné logo.</p>'
        '<p>V nabídce obchodů se může vyskytovat i značka ' + B(('calvin-klein-jeans', 'Calvin Klein Jeans'),) + ', což je samostatná řada značky. Při porovnání se dívejte na přesný název modelu, protože se liší střihem a cílovou skupinou.</p>'
        '<h2>Péče o plavky, aby vydržely</h2>'
        '<p>Elastická vlákna v plavkách snášejí chlór, sůl, opalovací krémy a pot jen omezeně. Plavky po každém koupání opláchněte čistou vodou, nenechávejte je sušit na přímém slunci a nesušte je na topení. Perte v ruce nebo v pračce na jemný program ve studené vodě, nikdy v horké.</p>'
        '<ol><li>Opláchněte plavky po koupání v čisté sladké vodě.</li>'
        '<li>Vymačkejte přebytečnou vodu jemným stlačením, ne ždímáním.</li>'
        '<li>Sušte ve stínu, rozložené naplocho nebo na šňůře.</li>'
        '<li>Neperte s drsnými tkaninami a nepoužívejte aviváž.</li>'
        '<li>Uložte suché a čisté, ne zmačkané v mokré tašce.</li></ol>'
        '<p>Tmavé a černé plavky mívají dlouhou životnost barvy, ale světlejší odstíny, například bílé nebo béžové, mohou při opalování s krémem zežloutnout, zejména při kontaktu s opalovacím olejem. Rozhodnete-li se pro světlý odstín, myjte plavky co nejdříve po použití.</p>'
        '<h2>Pro koho jsou Calvin Klein plavky</h2>'
        '<p>Značka cílí na kupující, kteří chtějí jednoduché plavky s vlastním stylem a nehledají výkonnostní vybavení. Dámské jednodílné plavky s hladkým střihem se hodí k bazénu v hotelu i na plážový den, bikiny s kontrastním páskem jsou typické pro hravější styl. Pánské šortky jsou praktické v tom, že se dají nosit i jako krátké kalhoty při procházce po pláži, protože mají neutrální vzhled a rychle schnou.</p>'
        '<p>Pro koho nejsou: pro plavce, kteří pravidelně uplavou několik bazénů týdně, pro surfaře a pro ty, kdo potřebují oporu při aquaaerobiku. Tam rozhoduje pevnější uchycení, odolnější materiál a střih, který se nesroluje. Pro tyto aktivity vybírejte plavky z kategorií sportovní nebo surfové a Calvin Klein si nechte na dovolenou.</p>'
        '<h2>Plavky na cesty a na každý den u vody</h2>'
        '<p>Na dovolenou se vyplatí zabalit plavky, které se dají snadno kombinovat: například jednodílné plavky černé nebo tmavě modré, doplněné barevným pareem nebo košilí přes ramena. Pánské šortky stejné řady lze nosit od snídaně u bazénu až po večerní procházku po promenádě. Prostor v kufru ušetří neutrální barvy, které se k sobě hodí bez ohledu na to, co si zrovna oblečete.</p>'
        '<p>Na bazénu se plavky potkávají s chlorovanou vodou, na pláži s pískem a solí. Písek plavky otírá, proto si na něj raději rozložte ručník. Sezení na horkých schodech nebo na hrubém dřevě může poškodit jemnou pleteninu a vytvořit na látce vytahané nitky. Při opalování používejte krém, který se nechá před oblečením vsáknout, aby nezůstaly mastné stopy.</p>'
        '<h2>Praktické poznámky k nákupu</h2>'
        '<p>Při srovnání nabídek se zaměřte na přesný název dílu a velikost, protože u Calvin Klein se spodní a horní díly často prodávají samostatně a může se stát, že k vybranému topu chybí kalhotky stejné řady. Zkontrolujte také, zda je u dílu uvedeno složení a zda nemá vyjímatelné vycpávky. Při výběru plavek na dovolenou je rozumné zvolit dvě sady, které se dají střídat, aby jedna stihla uschnout.</p>'
    ),
    faq=[
        ('Jsou Calvin Klein plavky vhodné na plavání v bazénu?', 'Na rekreační plavání ano, ale nejsou určené pro pravidelný trénink. Sportovní plavky jsou odolnější proti chlóru a lépe drží při plavání. Pokud plavete jen občas, stačí je po použití důkladně opláchnout. Pro pravidelný trénink hledejte kousky značek zaměřených na plavání.'),
        ('Jak vybrat velikost Calvin Klein plavek?', 'Změřte obvod hrudníku, pasu a boků a porovnejte s tabulkou u produktu. Střih bývá spíše přiléhavý. Při výběru mezi dvěma velikostmi vezměte tu, která je pohodlná v nejširší části. Horní díl vybírejte podle obvodu pod prsy, spodní podle boků.'),
        ('Dají se horní a spodní díly kombinovat v různých velikostech?', 'Ano, horní a spodní díly bikin se prodávají samostatně, takže velikosti můžete kombinovat. Pro jednotný vzhled hledejte stejnou řadu a stejný odstín. Při online nákupu ověřte, že nabízený spodní díl patří ke stejnému modelu jako horní.'),
        ('Jak dlouho Calvin Klein plavky vydrží?', 'Záleží na používání. Při občasném koupání a správné péči vydrží několik sezón. Chlór, sůl, opalovací krémy a sušení na slunci zkracují životnost elastických vláken. Plavky opláchněte, nesušte na topení a nepoužívejte horkou vodu.'),
        ('Jak se Calvin Klein plavky liší od sportovních značek?', 'Jsou módnější a minimalističtější, s logem a hladkými tvary. Sportovní značky se soustředí na odolnost materiálu a střih pro plavání. Pro dovolenou a pláž jsou Calvin Klein plavky vhodné, pro pravidelné plavání praktičtější sportovní modely.'),
        ('Kde najdu pánské Calvin Klein plavky?', 'V nabídce jsou pánské koupací šortky, které se liší střihem a délkou. Podívejte se do kategorie pánské plavky nebo použijte filtr podle typu. U šortek zkontrolujte, zda mají vnitřní slip, a vybírejte podle obvodu pasu a požadované délky nohavice.'),
        ('Je v nabídce i Calvin Klein Jeans?', 'Ano, obchody mohou nabízet řadu Calvin Klein Jeans, která je cílena na mladší a streetovější styl. Střihy a materiály se mohou lišit od hlavní řady. Při porovnávání se dívejte na přesný název modelu a velikostní tabulku konkrétního produktu.'),
        ('Mají plavky vycpávky a dají se vyjmout?', 'U plavkových podprsenek a některých jednodílných plavek jsou vycpávky součástí, jinde ne. Zkontrolujte popis produktu, zda jsou vyjímatelné. Pokud jsou pevně přišité, nesušte plavky na slunci ani na topení, protože se mohou deformovat.'),
        ('Mohou světlé plavky po opalování zežloutnout?', 'Světlejší odstíny, zejména bílé nebo béžové, mohou při kontaktu s opalovacími krémy a oleji zežloutnout. Pomůže plavky po koupání co nejdříve opláchnout a vyprat. Tmavé a černé odstíny jsou praktičtější, pokud se barva a krém nevzájemně nepotkávají.'),
    ],
)

# ------------------------------------------------------------------ panske-polokosile
NEW['panske-polokosile'] = dict(
    title='Pánské polokošile: střih, materiál a velikosti',
    desc='Pánské polokošile pro golf, tenis, kancelář i volný čas. Jak vybrat střih, materiál a velikost, srovnání značek a rady, jak polokošili nosit a prát.',
    intro='<p>Pánská polokošile je u mužů jeden z nejuniverzálnějších kusů šatníku: vejde se na golfové hřiště, na tenisový kurt, do kanceláře s neformálním dress codem i na víkendový výlet. U pánských modelů ale rozhoduje několik věcí, které se u dámských řeší jinak, zejména délka trupu, šířka v ramenou, tvar límce a to, jak polokošile sedí v pasu a při zasunutí do kalhot. Na této stránce se dozvíte, jak se střihy liší, jak správně změřit velikost, kdy zvolit bavlněné piké a kdy funkční materiál, jak nosit polokošili, aby vypadala upraveně, a které značky jsou ve výběru. Pomůže vám také tabulka kombinací s oblečením.</p>',
    guide=(
        '<h2>Střihy pánských polokošil</h2>'
        '<p>Pánské polokošile se šijí v několika základních střizích. Nejčastější je klasický (regular), který je volnější v trupu a vhodný pro každodenní nošení. Štíhlý střih (slim) sedí blíže k tělu a hodí se pro postavy bez většího břicha. Sportovní střih, typický pro golf a tenis, bývá delší vzadu, aby se polokošile nevysunula z kalhot při švihu nebo úderu. Volnější střih (relaxed) nabízí pohodlí pro širší postavy a pro vyšší teploty.</p>'
        '<ul><li><strong>Klasický střih:</strong> univerzální volba pro každý den, dostatečně prostorný v ramenou a pase.</li>'
        '<li><strong>Slim střih:</strong> užší v trupu a v rukávu, zdůrazňuje postavu, vyžaduje přesnou velikost.</li>'
        '<li><strong>Sportovní střih:</strong> delší záda, elastičtější materiál, volnější rukáv pro pohyb paže.</li>'
        '<li><strong>Volný střih:</strong> prostorný, pohodlný pro teplé dny a pro ty, kdo nechtějí přiléhavou látku.</li></ul>'
        '<p>Pro srovnání s ženskými modely se podívejte na stránku <a href="/damske-polokosile/">dámské polokošile</a>, kde najdete užší ramena a kratší trup. Hlavní kategorie <a href="/polokosile/">polokošile</a> obsahuje obecné informace o historii a materiálech; tady se věnujeme tomu, co je pro pánský střih specifické.</p>'
        '<h2>Velikost: co změřit a jak číst tabulku</h2>'
        '<p>Pánské polokošile jsou nejčastěji v písmenných velikostech S až XXL, někdy i větších, některé značky používají čísla obvodu hrudníku nebo evropské velikosti. Nejdůležitější rozměr je šířka přes ramena a hrudník. Změřte obvod hrudníku v nejširším místě a porovnejte s tabulkou výrobce. Pokud se nacházíte mezi velikostmi, vezměte větší, pokud nosíte polokošili volně, nebo menší, pokud preferujete přiléhavý styl.</p>'
        + T(['Rozměr', 'Jak změřit', 'Na co se zaměřit'], [
            ['Obvod hrudníku', 'metr pod paže přes nejširší část hrudníku', 'polokošile má sedět bez napětí, ale nemá viset'],
            ['Šířka ramen', 'od ramenního švu k ramennímu švu na zádech', 'ramenní šev má ležet na kosti ramene'],
            ['Délka trupu', 'od krku po spodní okraj', 'delší záda znamenají lepší držení při zasunutí'],
            ['Rukáv', 'od ramenního švu po manžetu', 'rukáv by měl končit v polovině nadloktí']]) +
        '<p>Delší zadní díl a mírně zaoblený spodní lem jsou užitečné, protože se polokošile při pohybu nevysouvá z kalhot. Pokud ji nosíte přes kalhoty, nemá sahat níže než do půli rozkroku, jinak vypadá jako tričko.</p>'
        '<h2>Materiál: piké, žerzej a funkční vlákna</h2>'
        '<p>Piké je klasická struktura s drobným vzorem, tužší a prodyšná, dobře drží tvar a límec. Žerzej je hladší a měkčí, lehčí a méně formální. Funkční materiály z polyesteru rychle schnou a odvádějí pot, vhodné jsou pro sport a pro horké dny. Směsi s elastanem zlepšují pružnost a pomáhají udržet tvar.</p>'
        '<ul><li><strong>Bavlněné piké:</strong> pro město, kancelář a volný čas; příjemné na kůži, ale po vypocení pomalejší.</li>'
        '<li><strong>Bavlna s elastanem:</strong> lepší pružnost a nemačkavost, lepší pro štíhlejší střihy.</li>'
        '<li><strong>Polyester a funkční směsi:</strong> pro golf, tenis, běh a aktivní dny.</li>'
        '<li><strong>Merino a přírodní směsi:</strong> pro cestování, kde se nemá prát každý den.</li></ul>'
        '<p>Pokud hledáte polokošili spíše na sport, projděte i kategorii <a href="/sportovni-tricka/">sportovní trička</a> a <a href="/funkcni-tricka/">funkční trička</a>, kde jsou aktivní střihy bez límce. Pro golfové hřiště se hodí <a href="/golfove-obleceni-a-obuv/">golfové oblečení</a>, které často vyžaduje límec a delší zadní díl.</p>'
        '<h2>Límec, rozparek a detaily, které poznáte po prvním nošení</h2>'
        '<p>U polokošile rozhoduje límec o celkovém dojmu. Pevný límec s vyztužením stojí lépe, pletený se zvedá méně pevně, ale je měkčí. Rozparek se zapíná na dva až tři knoflíky a u sportovních modelů bývá kratší. Zkontrolujte, zda knoflíky drží a zda je lem dobře ušitý. Boční rozparky ve spodním lemu usnadňují nošení přes kalhoty a zlepšují pohodlí při sezení.</p>'
        '<p>Logo na hrudi je u mnoha značek znak rozpoznání. Jestliže chcete střídmější vzhled, hledejte kousky s malým nebo žádným logem. Při dlouhém praní se potisk i vyšitý znak opotřebují pomaleji, než polepený štítek.</p>'
        '<h2>Značky pánských polokošil v nabídce</h2>'
        '<p>Výběr zahrnuje sportovní, módní i outdoorové značky. Z módního a klasického segmentu jsou v nabídce ' + B(('lacoste', 'Lacoste'), ('polo-ralph-lauren', 'Polo Ralph Lauren'), ('tommy-hilfiger', 'Tommy Hilfiger'), ('fred-perry', 'Fred Perry'), ('us-polo-assn', 'US Polo Assn'), ('gant', 'Gant')) + '. Sportovní kousky najdete u značek ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('fila', 'Fila'), ('kappa', 'Kappa'), ('lotto', 'Lotto')) + '. Pro aktivní venkovní použití jsou tu značky ' + B(('helly-hansen', 'Helly Hansen'), ('columbia', 'Columbia'), ('regatta', 'Regatta'), ('kilpi', 'Kilpi')) + '. Všedního a přístupného střihu se drží například ' + B(('celio', 'Celio'), ('gap', 'Gap')) + '.</p>'
        '<p>Pro srovnání jedné klasické značky se podívejte na stránku <a href="/lacoste-polokosile/">Lacoste polokošile</a>. Značky se liší nejen vzhledem, ale i střihem: módní bývají užší, sportovní vzdušnější a delší vzadu, outdoorové z funkčního materiálu.</p>'
        '<h2>Jak polokošili kombinovat</h2>'
        + T(['Příležitost', 'Spodní díl', 'Poznámka'], [
            ['Kancelář s neformálním dress codem', 'chino kalhoty nebo tmavé džíny', 'jednobarevná polokošile bez výrazného loga, zasunutá'],
            ['Volný čas a město', 'džíny, kraťasy', 'klasický nebo volnější střih, vyšší nošení'],
            ['Golf a tenis', 'sportovní kalhoty nebo kraťasy', 'funkční materiál, delší zadní díl'],
            ['Večerní příležitost', 'tmavé kalhoty a sako', 'úzký střih, pevný límec, tlumená barva'],
            ['Cestování a léto', 'lehké kalhoty nebo šortky', 'rychle schnoucí materiál nebo lehké piké']]) +
        '<p>Polokošili můžete nosit zasunutou i volnou. Zasunutá působí upraveněji a hodí se k pásku a chino kalhotám, volná je pohodlnější a méně formální. Pokud ji nosíte volně, nemá viset přes celý zadek. Límec stavějte jen tehdy, když vás chrání před sluncem; v běžném životě vypadá nejlépe položený.</p>'
        '<h2>Jak polokošili poznat po koupi</h2>'
        '<p>Dobrá polokošile po prvním vyprání drží tvar, límec nepodléhá a rozparek leží rovně. Pokud se límec stáčí nahoru nebo rozparek vlní, je to známka slabšího zpracování. Pokud se po vyprání výrazně zkrátí délka, vybírejte příště větší velikost nebo materiál s elastanem. Vyplatí se také koupit dvě polokošile ve stejném střihu, protože střídání prodlužuje životnost obou.</p>'
        '<h2>Polokošile podle sportu</h2>'
        '<p>Polokošile má sportovní původ a v několika sportech zůstala součástí oblečení dodnes. Na <a href="/golf/">golfu</a> je límec často vyžadován pravidly klubu, proto hráči volí polokošile z funkčního materiálu s delším zadním dílem. V <a href="/tenis/">tenise</a> se hodí lehká látka a volný rukáv, který nebrání úderu. Fanoušci zase sahají po týmových modelech z klubových kolekcí. Pro každodenní oblečení do města je lepší klasická bavlna.</p>'
        '<p>Alternativou k polokošili je klasická <a href="/kosile/">košile</a>, když potřebujete formálnější vzhled, a funkční tričko, když jde o čistě sportovní nasazení. Polokošile je kompromis mezi nimi.</p>'
        '<h2>Údržba a vlastnosti, které vydrží</h2>'
        '<p>Bavlněné piké perte při třiceti až čtyřiceti stupních, nejlépe naruby, aby se potisk a logo neotíraly. Nepoužívejte přílišné množství prostředku a vyhněte se sušičce, která tkaninu srazí. Funkční materiály nepotřebují aviváž, protože zanáší vlákna. Límec po vyprání zformujte rukama a polokošili zavěste na ramínko nebo ji položte naplocho.</p>'
        '<ol><li>Před praním rozepněte knoflíky, aby se nenamáhaly.</li>'
        '<li>Perte podle štítku, nejlépe naruby a s podobnými barvami.</li>'
        '<li>Sušte na vzduchu, ne na topení, abyste zachovali tvar a barvu.</li>'
        '<li>Žehlete na střední teplotu naruby, logo nežehlete přímo.</li>'
        '<li>Uskladněte přehnutou, ne zavěšenou na tenkém ramínku, které by deformovalo ramena.</li></ol>'
    ),
    faq=[
        ('Jakou velikost pánské polokošile zvolit?', 'Změřte obvod hrudníku a porovnejte ho s tabulkou u produktu. Mezi velikostmi vyberte větší, pokud chcete volnější styl, a menší, pokud preferujete přiléhavý. Vždy zkontrolujte šířku ramen a délku trupu, protože jednotlivé značky se liší střihem.'),
        ('Je lepší polokošile z piké, nebo z žerzeje?', 'Piké je pevnější a formálnější, lépe drží límec a hodí se do kanceláře i města. Žerzej je lehčí a měkčí, vhodný pro volnější styl. Pro sport zvolte funkční materiál, který rychle schne a odvádí pot.'),
        ('Nosí se polokošile zasunutá, nebo volná?', 'Obojí je možné. Zasunutá působí upraveněji a hodí se k chino kalhotám a pásku. Volná je pohodlnější a méně formální. Delší zadní díl a mírně zaoblený lem jsou důležité pro volné nošení a pro sportovní střih.'),
        ('Dá se polokošile nosit do kanceláře?', 'Ano, pokud to dress code dovoluje. Zvolte jednobarevnou polokošili z piké bez výrazného loga a zasuňte ji do kalhot. Tmavé odstíny působí formálněji. Při styku s klienty je bezpečnější klasická košile.'),
        ('Jak se liší pánská polokošile od dámské?', 'Pánská má širší ramena, delší trup a méně přiléhavý pas. Dámská bývá užší a kratší, někdy s jiným tvarem límce. Pokud jste menší postavy, může vám sedět dámská, ale vyzkoušejte podle tabulky velikostí a střihu.'),
        ('Jak prát polokošili, aby se nesrazila?', 'Perte při třiceti až čtyřiceti stupních, naruby a bez sušičky. Bavlna se může srazit při vysoké teplotě. Funkční materiály nepotřebují aviváž. Po vyprání upravte límec a polokošili sušte na vzduchu, ne přímo na topení.'),
        ('Mohu nosit polokošili ke sportu?', 'Ano, pokud je z funkčního materiálu. Pro golf a tenis je ideální polokošile s delším zadním dílem a pružnou látkou. Bavlněné piké při pocení nasákne a pomalu schne. Na intenzivnější sporty vyberte spíše funkční triko.'),
        ('Které barvy polokošil jsou nejuniverzálnější?', 'Tmavě modrá, bílá, šedá a černá se dobře kombinují s většinou kalhot. Pro letní měsíce můžete zvolit světlejší odstíny, pro město tlumené barvy. Výrazné barvy a proužky jsou vhodnější pro volný čas.'),
        ('Jak poznám kvalitní polokošili?', 'Zkontrolujte pevné švy, rovný lem, dobře přišité knoflíky a stabilní límec. Materiál by měl být hustě pletený a po natažení by se měl vrátit do původního tvaru. Cena sama o kvalitě nerozhoduje, rozhoduje střih, materiál a zpracování.'),
    ],
)
