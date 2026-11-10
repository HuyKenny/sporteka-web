"""sporteka.cz — facet landing texts wave 120: detske-vesty, inline-brusle-damske, sportovni-obleceni-damske, salomon-trekove-boty.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detske-vesty
NEW['detske-vesty'] = dict(
    title='Dětské vesty: zateplené, reflexní i plovací, velikosti',
    desc='Dětské vesty pro školu, hřiště, cestu za tmy i k vodě. Jak vybrat velikost podle výšky, kdy hodí softshell a čím se liší plovací vesta od plavecké.',
    intro='<p>Dětská vesta řeší hned několik různých úkolů. V chladnějším dni zahřeje dítěti trup a nechá volné ruce, za šera dělá z chodce viditelného účastníka provozu a u vody pomáhá udržet plavce nad hladinou. Pod jedno vyhledávání se tak vejde prošívaná vesta do školy, softshellová na hřiště, reflexní na cestu z kroužku, plovací k vodě i vojenská napodobenina pro hru. '
          'Na této stránce jsou vesty z kategorie <a href="/sportovni-vesty/">sportovní vesty</a> určené dětem od předškoláků po teenagery. Průvodce vysvětluje, jak vybrat velikost podle výšky a ne podle věku, kdy se vyplatí zateplená a kdy tenká vrstva, jak poznat rozdíl mezi plovací a plaveckou vestou a na co si dát pozor u kapuce a zipu. '
          'Dospělé střihy najdete v <a href="/panske-vesty/">pánských</a> a <a href="/damske-vesty/">dámských vestách</a>.</p>',
    guide='<h2>Proč dítěti koupit vestu a ne jen bundu</h2>'
          '<p>Děti se pohybují v nárazech: chvíli stojí u branky, vzápětí běží a za pět minut sedí na lavičce. Bunda s rukávy je pak buď příliš teplá, nebo málo, kdežto vesta chrání jádro těla a paže zůstávají vzdušné. Další výhoda je praktická. Vesta nemá rukávy, takže když dítě za sezonu povyroste, krátké zápěstí nevadí a dá se nosit déle než bunda. Nehodí se naopak samostatně v mrazu, to je úloha pro <a href="/zimni-bundy/">zimní bundy</a> nebo <a href="/nepromokave-bundy/">nepromokavé bundy</a>, pod které se vesta hodí jako střední vrstva.</p>'
          + T(['Typ dětské vesty', 'Hlavní předností', 'Na co dát pozor', 'Kdy ji nosit'], [
              ['Zateplená prošívaná', 'hřeje a málo váží, dobře se sbalí', 'prošívání netěsní, při dešti nasákne', 'škola, hřiště, jarní a podzimní dny'],
              ['Softshellová', 'zastaví vítr, lehce odpuzuje drobný déšť', 'sama o sobě málo hřeje', 'výlety, kolo, koloběžka'],
              ['Fleecová', 'měkká, prodyšná, příjemná na dotek', 'vítr jí prochází', 'střední vrstva pod bundu'],
              ['Reflexní', 'dítě je vidět v tmavých hodinách', 'neslouží jako ochrana před chladem', 'cesta do školy za tmy, kolo, kroužky'],
              ['Plovací a plavecká', 'pomáhá udržet tělo nad vodou', 'není náhradou dozoru dospělého', 'voda, loď, bazén, výuka plavání'],
              ['Hrací a taktická', 'vypadá jako armádní, má kapsy', 'je to vybavení do hry, ne ochrana', 'airsoft pro děti, hra, karneval']]) +
          '<h2>Velikost podle výšky, ne podle věku</h2>'
          '<p>Dětské oblečení se značí číslem, které odpovídá výšce dítěte v centimetrech. Věk je jen hrubá nápověda, protože dvě stejně staré děti se liší i o deset centimetrů. Změřte proto dítě bez bot, zády ke zdi, a vezměte nejbližší číslo. Zkontrolujte i obvod hrudníku a porovnejte jej s tabulkou konkrétního výrobce. Pokud dítě stojí mezi dvěma čísly, zvolte větší, protože pod vestu patří ještě mikina nebo tričko s dlouhým rukávem.</p>'
          + T(['Výška dítěte', 'Přibližný věk', 'Poznámka k výběru'], [
              ['92–98 cm', '2–3 roky', 'jednodušší zipy, bez šňůrek u krku'],
              ['104–116 cm', '4–6 let', 'ocení širší límec, který nedře'],
              ['122–134 cm', '7–9 let', 'zip samo zvládne zapnout, hodí se kapsy na zip'],
              ['140–152 cm', '9–12 let', 'začíná se lišit chlapecký a dívčí střih'],
              ['158–164 cm', '12–14 let', 'dospělé tvary, lze zvažovat i XS dospělé']]) +
          '<p>Věkové údaje jsou orientační a každá značka střihá jinak. Evropské značky s tradicí dětského oblečení obvykle střihají prostorněji, sportovní značky z dospělých řad přiléhavěji. Z tohoto důvodu se u každého kusu vyplatí otevřít velikostní tabulku a nespoléhat jen na číslo, které dítě nosilo loni.</p>'
          '<h2>Zateplená vesta: výplň, prošívání a zip</h2>'
          '<p>Většina dětských zateplených vest používá syntetickou výplň. Na rozdíl od peří zůstane hřejivá i po navlhnutí a dá se bez obav prát v pračce, což u dětského oblečení rozhoduje. Prošívání drží výplň na místě a zároveň vytváří tepelné mosty, proto se stejně dobře nehodí jako samostatná zimní vrstva. Při výběru sledujte hlavně tři věci. Zip s krytkou pod bradou neškrábe, takže dítě vestu zapne až nahoru. Kapsy na zip uchrání klíče a kartu na dopravu a boční kapsy by měly být dost hluboké pro ruce, aby se nevyplatilo strkat je do kapes kalhot. Pružný lem nebo stahování u pasu pak zabrání, aby studený vzduch profukoval zespodu.</p>'
          '<p>Kapuce a šňůrky patří k věcem, které se u dětí posuzují přísněji. Na dětském oblečení má být výrazně omezen počet šňůrek v oblasti krku, protože se mohou zachytit při hře nebo ve vozidle. Vesty pro menší děti proto často vůbec nemají stahovací šňůrky u kapuce. Pokud ji vesta má, zkontrolujte, zda je odepínací, a šňůrky řešte raději pružnými lemy.</p>'
          '<h2>Softshellová a fleecová vesta na pohyb</h2>'
          '<p>Dítě, které jezdí na kole, koloběžce nebo se pohybuje při sportovním kroužku, potřebuje tenčí vrstvu, ve které se nezapotí. Softshell zastaví vítr a udrží teplo u těla, ale je prodyšnější než bunda s membránou. Vesta z něj se hodí na výlet, na kolo i do lesa. Pro rychlé sušení je dobré, aby měla oděruvzdorný vnější povrch a měkčí vnitřní stranu. Fleecová vesta je ještě lehčí a pohodlná, ovšem vítr jí prochází, a proto ji kombinujte spíše pod bundu. Více o materiálech najdete v kategorii <a href="/softshellove-bundy/">softshellové bundy</a>.</p>'
          '<h2>Reflexní vesta: viditelnost před módou</h2>'
          '<p>V zimních měsících se děti vrací ze školy a kroužků za šera. Řidič vidí tmavě oblečené dítě podstatně později než dítě v odrazivém prvku. Reflexní vesta má dvě vlastnosti: fluorescenční barva zvyšuje viditelnost za šera, odrazivé pásky vrací světlo reflektorů v noci. Pro dětskou cestu je důležité, aby vesta byla vidět zpředu i zezadu a aby ji dítě nosilo vnější vrstvou, ne pod bundou. Při jízdě na kole nebo koloběžce se vyplatí ji doplnit helmou, viz <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>, a také světly. Hodí se i modely vyrobené tak, aby se daly přetáhnout přes zimní bundu a po použití svinout do batohu. Na silnici i u hřiště funguje principem „vidět a být viděn“.</p>'
          '<h2>Plovací a plavecká vesta: co je co</h2>'
          '<p>Tady se nejčastěji plete. <strong>Plavecká vesta</strong> je výuková pomůcka pro dítě, které se učí plavat v bazénu nebo na mělčině, a obvykle se skládá z nafukovacích nebo pěnových vložek. <strong>Plovací vesta</strong> neboli záchranná se nosí na lodi, paddleboardu, vodáckém výletu nebo při jízdě na vodním skútru a jejím úkolem je nadlehčit tělo. Hodnota v newtonech, například číslo před písmenem N, udává vztlak. Čím vyšší hodnota, tím větší nadlehčení a tím větší ochrana, ale také větší objem. U dětí vždy řešte velikost podle hmotnosti uvedené výrobcem, ne podle výšky. Správně sedí vesta tak, že ji při lehkém zatažení za ramena nelze přetáhnout přes hlavu, a poutka mezi nohama brání vyklouznutí. Vesta nikdy nenahrazuje dozor dospělého. Širší výběr najdete v kategorii <a href="/plovaci-vesty/">plovací vesty</a>.</p>'
          '<h2>Dívčí, chlapecký a unisex střih</h2>'
          '<p>Do zhruba osmi let se střihy prakticky neliší a odlišuje je hlavně barva nebo potisk. Později dívčí modely zužují ramena, zkracují délku nebo mírně tvarují pas, chlapecké mají rovnější linii a delší trup. Rozhodujte podle toho, jak vesta dítěti sedí v ramenou a na délku, ne podle štítku. Dívka s delším trupem může být spokojenější v chlapeckém střihu a naopak. Nabídka obsahuje značky jako ' + B(('kilpi', 'Kilpi'), ('4f', '4F'), ('alpine-pro', 'Alpine Pro'), ('didriksons', 'Didriksons'), ('reima', 'Reima'), ('kappa', 'Kappa'), ('regatta', 'Regatta'), ('the-north-face', 'The North Face')) + ', u vodních modelů pak ' + B(('bestway', 'Bestway'), ('aquadesign', 'Aquadesign'), ('zoggs', 'Zoggs')) + '. Vojenský styl pro hru zastupují například ' + B(('kombat', 'Kombat'), ('rothco', 'Rothco')) + '.</p>'
          '<h2>Vrstvení a péče</h2>'
          '<ol><li>Na tělo patří tričko s dlouhým rukávem z funkčního materiálu nebo bavlny podle aktivity.</li>'
          '<li>Na ně přijde mikina nebo tenká fleecová vrstva, pokud je zima.</li>'
          '<li>Vesta zahřeje trup a nechá volné ruce, takže dítě se v ní nezapotí v loktech.</li>'
          '<li>Při dešti nebo mrazu přichází navíc bunda, pod kterou se vesta vejde.</li></ol>'
          '<p>Většinu dětských vest lze prát při třiceti stupních, bez aviváže a se zapnutým zipem, aby nepoškodil výplň. Reflexní pásky nesnášejí žehlení a vysokou teplotu, plovací vestu po použití opláchněte sladkou vodou a sušte ve stínu. Prošívaná vesta se po vysušení zpravidla nadýchá, pomůže jí mírné protřepání.</p>'
          '<h2>Co zkontrolovat před koupí</h2>'
          '<ul><li><strong>Výška a obvod hrudníku:</strong> porovnejte s tabulkou výrobce, ne s věkem.</li>'
          '<li><strong>Určení:</strong> zateplená, softshell, reflexní nebo plovací mají každá jiný účel.</li>'
          '<li><strong>Zip a límec:</strong> musí jít zapnout dětskýma rukama a nesmí škrábat bradu.</li>'
          '<li><strong>Šňůrky:</strong> v oblasti krku a kapuce raději žádné nebo pružné.</li>'
          '<li><strong>Viditelnost:</strong> odrazivé prvky zepředu i zezadu.</li>'
          '<li><strong>Péče:</strong> plovací vestu v pračce raději neperte a řiďte se pokyny výrobce.</li></ul>'
          '<p>Obchody se liší tím, které velikosti mají skladem, proto při porovnání sledujte právě číslo, které dítě potřebuje. Chcete-li doplnit celý outfit, projděte <a href="/detske-sportovni-obleceni/">dětské sportovní oblečení</a> a <a href="/sportovni-bundy/">sportovní bundy</a>.</p>',
    faq=[
        ('Jaká velikost dětské vesty je správná?',
         'Vyberte podle výšky dítěte v centimetrech, ne podle věku. Změřte dítě bez bot a porovnejte údaj s tabulkou výrobce. Pokud padne mezi dvě čísla, zvolte větší, aby se pod vestu vešla mikina.'),
        ('Hodí se vesta pro dítě do zimy?',
         'Samotná jen na mírné mrazy a při pohybu. Při opravdové zimě slouží jako střední vrstva pod bundu, kde zahřeje trup a nezvětší objem rukávů.'),
        ('Jaký je rozdíl mezi plaveckou a plovací vestou?',
         'Plavecká je výuková pomůcka pro dítě, které se učí plavat. Plovací nadlehčuje tělo na lodi a při vodních sportech a její vztlak se udává v newtonech. Ani jedna nenahrazuje dozor dospělého.'),
        ('Je reflexní vesta pro děti povinná?',
         'Pravidla závisí na situaci a zemi, proto ověřte aktuální předpisy. Rozumné je ji nosit při cestě za šera a tmy, zvláště mimo osvětlené ulice. Vždy ji oblékněte jako vnější vrstvu.'),
        ('Mohou mít dětské vesty kapuci?',
         'Mohou, ale šňůrky v oblasti krku se u dětí omezují kvůli riziku zachycení. Praktičtější bývá kapuce odepínací nebo se stahováním na pružnou gumu.'),
        ('Jak vybrat vestu pro školáka na kolo nebo koloběžku?',
         'Zvolte softshellovou nebo lehkou reflexní vestu, která zastaví vítr a nezpůsobí zapocení. Ke kolu patří helma, světla a barva viditelná zepředu i zezadu.'),
        ('Dá se dětská vesta prát v pračce?',
         'Většina ano, zpravidla při třiceti stupních se zapnutým zipem a bez aviváže. Plovací vestu pouze opláchněte sladkou vodou a sušte ve stínu. Řiďte se štítkem uvnitř.'),
        ('Liší se dívčí a chlapecké vesty?',
         'Do osmi let málokdy, rozdíl je hlavně v barvě. Později bývají dívčí střihy užší v ramenou a chlapecké delší. Vyberte podle toho, jak vesta sedí, ne podle označení.'),
        ('Jsou taktické vesty pro děti ochranné?',
         'Ne, jde o hrací nebo kostýmní vybavení ve vojenském stylu. Neposkytují ochranu proti nárazu a hodí se na hru nebo karneval. Pro bezpečnost je potřeba helma a ochranné pomůcky určené pro daný sport.'),
        ('Jak dlouho dítěti vesta vydrží?',
         'Protože nemá rukávy, nevadí krátká zápěstí a často se dá nosit déle než bunda. Rozhoduje délka trupu a obvod hrudníku. Pokud se dítě rychle protáhne, vezměte o číslo větší, aby vesta vydržela celou sezonu.'),
    ],
)

# ------------------------------------------------------------------ inline-brusle-damske
NEW['inline-brusle-damske'] = dict(
    title='Inline brusle dámské: střih, velikost, kolečka a výběr',
    desc='Dámské inline brusle: užší pata a nižší manžeta, velikost, kolečka, rám, chrániče a značky. Jak vybrat pár pro rekreaci, fitness i dlouhé trasy.',
    intro='<p>Dámské inline brusle se od pánských liší tvarem boty víc, než by se zdálo. Pata bývá užší, špička přiléhavější, manžeta nižší a rám často kratší, aby se ženě s menší váhou a kratší nohou lépe řídil. U modelu, který nezapadne přesně na nohu, pak nepomůže ani drahé kolečko, protože se bota viklá a jízda bolí. '
          'Na této stránce jsou brusle z kategorie <a href="/inline-brusle/">inline brusle</a> určené ženám a dívkám, od lehkých rekreačních po fitness a freestyle modely. Průvodce vysvětluje, v čem je ženský střih jiný, jak vybrat velikost bez chyb, co znamenají rozměry koleček a ložiska, kdy zvolit tři a kdy čtyři kolečka a jaké chrániče si pořídit. '
          'Mužské verze najdete v <a href="/inline-brusle-panske/">pánských inline bruslích</a>, malé bruslařky v <a href="/detske-inline-brusle/">dětských</a>.</p>',
    guide='<h2>V čem se dámská inline brusle liší</h2>'
          '<p>Ženské chodidlo je v průměru užší v oblasti paty a štíhlejší nad kotníkem, lýtko bývá menší a celková hmotnost jezdce nižší. Výrobci proto upravují vnitřní tvar boty (takzvanou kopyto), výšku manžety a někdy i tuhost skořepiny. Označení „dámské“ ovšem není zárukou, že bota padne. Úzká noha se může cítit lépe v dámské řadě, širší noha může preferovat unisex model, a to bez ohledu na pohlaví.</p>'
          + T(['Prvek', 'Co se u dámské brusle mění', 'Proč na tom záleží'], [
              ['Pata a kopyto', 'užší pata, štíhlejší střih', 'noha se nevyklouzne a nevznikají puchýře'],
              ['Manžeta', 'nižší, někdy tvarovaná pro lýtko', 'nedře pod lýtkem a nepřetahuje se'],
              ['Rám', 'o něco kratší, často z lehčí slitiny', 'brusle se lépe zatáčí a méně váží'],
              ['Výplň a vnitřek', 'měkčí, vyšší komfort, líbivé barvy', 'pohodlí při delším rekreačním dni'],
              ['Barva a styl', 'širší paleta, pastelové nebo kontrastní prvky', 'jde o vzhled, funkci neovlivňuje']]) +
          '<p>Rozdíl se nejvíc projeví u fitness a rekreačních modelů s plnou botou, méně u agresivních a freestyle modelů, které se bez ohledu na pohlaví staví podobně. U značek jako ' + B(('k2', 'K2'), ('powerslide', 'Powerslide'), ('roces', 'Roces'), ('fila', 'Fila'), ('rollerblade', 'Rollerblade'), ('tempish', 'Tempish')) + ' se dámské verze často pozná podle slov Lady, Women nebo ženského jména v názvu modelu.</p>'
          '<h2>Velikost: jak ji určit a čeho se vyvarovat</h2>'
          '<p>Brusle sedí těsněji než běžná obuv, protože noha potřebuje pevnou oporu. Změřte délku chodidla od paty po nejdelší prst večer, kdy je noha nejširší, a porovnejte ji s tabulkou výrobce v milimetrech nebo centimetrech. Čísla od různých výrobců se liší až o jednu velikost, protože se používají evropské, americké i britské systémy. Některé rekreační a dětské brusle mají nastavitelnou velikost, takže pokryjí čtyři čísla. U dámských modelů ale pozor, že tabulky často uvádějí dámské americké velikosti, které se neshodují s evropskými.</p>'
          '<ul><li><strong>Špička:</strong> prsty se mají lehce dotýkat špičky, ale nezatínat.</li>'
          '<li><strong>Pata:</strong> při pokrčení kolen se nesmí zvedat, jinak vzniknou puchýře a špatné řízení.</li>'
          '<li><strong>Ponožky:</strong> zkoušejte v tenkých sportovních ponožkách, které budete nosit, viz <a href="/sportovni-ponozky/">sportovní ponožky</a>.</li>'
          '<li><strong>Boční tlak:</strong> mírné držení je v pořádku, bodový tlak na kotník znamená špatný tvar.</li>'
          '<li><strong>Zapínání:</strong> kombinace tkaniček, pásku a přezky drží kotník, jedna samotná přezka nestačí.</li></ul>'
          '<h2>Kolečka, ložiska a rám</h2>'
          '<p>Průměr koleček se uvádí v milimetrech. Menší kolečka kolem osmdesáti milimetrů jsou obratnější a hodí se začátečnicím a menším ženám, větší kolem sto deseti milimetrů jedou rychleji a plynuleji po delší trase, ale hůře se řídí. Tvrdost se udává v jednotkách A: měkčí kolečko tlumí nerovnosti a lépe drží, tvrdší jezdí rychleji a déle vydrží na hladkém povrchu. Ložiska se označují třídou ABEC, ale vyšší číslo ještě neznamená vyšší kvalitu bruslení, rozhoduje i čistota a mazání. Rám z hliníku je tuhší a lépe přenáší sílu, plastový je levnější a pružnější, což ocení rekreační jízda.</p>'
          + T(['Využití', 'Počet a velikost koleček', 'Vhodné pro'], [
              ['Začátky a rekreace', '4 × 76–84 mm, kratší rám', 'jistota a snadné řízení, cyklostezka a park'],
              ['Fitness a pravidelné bruslení', '4 × 80–90 mm nebo 3 × 100–110 mm', 'delší jízdy, vyšší rychlost'],
              ['Dlouhé vzdálenosti', '3 × 110 mm nebo 3 × 125 mm', 'zkušenější jezdkyně na kvalitním asfaltu'],
              ['Freestyle a slalom', 'menší kolečka, kratší rám', 'obraty, triky, jízda mezi kužely'],
              ['Rekreační „2 v 1“ a „4 v 1“', 'nastavitelná velikost, měnitelný systém', 'dívky, které rostou, a ty, co chtějí zkusit']]) +
          '<h2>Tři, nebo čtyři kolečka</h2>'
          '<p>Čtyři menší kolečka dávají delší základnu, takže brusle je stabilnější a snadněji se zatáčí. Tři větší kolečka jsou rychlejší a lépe překonávají praskliny, ale více vyžadují techniku. Většině začátečnic doporučujeme čtyři kolečka kolem osmdesáti milimetrů. Jakmile se naučíte brzdit, plynule zatáčet a jet na delší trase, můžete přejít na větší průměr. Více o základním výběru najdete v kategorii <a href="/rekreacni-brusle/">rekreační brusle</a>.</p>'
          '<h2>Chrániče a helma: s čím začít</h2>'
          '<p>Nejčastější úraz při bruslení je pád dopředu na ruku. Proto patří mezi první věc, kterou si pořídíte, chrániče zápěstí, a k nim kolena a lokty. Helma chrání při pádu dozadu nebo při střetu s překážkou. Sada chráničů s helmou je také nejlevnější způsob, jak snížit riziko zranění. Ve volbě pomáhá velikost podle obvodu zápěstí, kolene a lokte, protože univerzální rozměry často sedí špatně. Přehled najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Značky v nabídce a komu se hodí</h2>'
          '<p>Na dámských bruslích se v nabídce objevují značky ' + B(('powerslide', 'Powerslide'), ('roces', 'Roces'), ('fila', 'Fila'), ('rollerblade', 'Rollerblade'), ('raven', 'Raven'), ('tempish', 'Tempish'), ('k2', 'K2'), ('riedell', 'Riedell')) + ' a další. Řada Powerslide Phuzion je populární mezi bruslařkami, které směřují k freestyle nebo kombinují fitness s hrami na místě. Značka ' + B(('k2', 'K2')) + ' má v dámském programu řadu Alexis, kterou poznáte i podle názvu. ' + B(('tempish', 'Tempish')) + ' nabízí české modely s označením Lady, typicky pro rekreaci a fitness. Značky ' + B(('raven', 'Raven')) + ' a ' + B(('nils-extreme', 'Nils Extreme')) + ' se často objevují v nastavitelných rekreačních bruslích. Pokud hledáte brusle konkrétní značky, projděte i <a href="/inline-brusle-k2/">inline brusle K2</a> a <a href="/inline-brusle-bauer/">inline brusle Bauer</a>.</p>'
          '<h2>Styl jízdy určuje typ brusle</h2>'
          '<p>Fitness brusle mají delší rám, větší kolečka a pevnou botu, hodí se na pravidelné bruslení po cyklostezkách a na zlepšování kondice. Freestyle a slalomové modely mají kratší rám a vyšší manévrovatelnost, snesou obraty, couvání a jízdu mezi kužely. Rekreační „4 v 1“ nebo „2 v 1“ brusle se dají přestavět z inline na čtyřkolky a mají nastavitelnou velikost, což je výhodné pro dospívající dívky, které rychle rostou. Agresivní brusle s plastovým kluzným profilem patří do skateparku a pro běžnou jízdu se nehodí. Ženy, které jezdí hlavně pro zábavu a rozhýbání, mohou začít u rekreační a po roce přejít na fitness.</p>'
          '<h2>Brzdění a technika</h2>'
          '<p>Nejdostupnější způsob brzdění je patní brzda na pravé noze. Jedete s pokrčenými koleny, vysunete brzdící nohu dopředu a zvednete špičku, takže se brzda přitiskne k zemi. Pokročilejší bruslařky používají T-brzdu, při které zadní bruslí kolmo škrtají o povrch, nebo plynulé zatáčení do oblouku. Pokud brusle nemají patní brzdu, bývá to model pro zkušenější nebo freestyle. Jakmile ovládáte brzdění, naučte se jízdu z mírného kopce a vyhýbání překážkám. Dalším krokem je jízda po svahu a sjezd z nájezdu, vždy s chrániči a helmou.</p>'
          '<h2>Jak se naučit základy</h2>'
          '<ol><li>Najděte hladký rovný povrch bez provozu a vybavte se kompletní ochranou.</li>'
          '<li>Stůjte v mírném předklonu s pokrčenými koleny, váha je nad botami.</li>'
          '<li>Naučte se nejprve brzdit patní brzdou, teprve potom zrychlujte.</li>'
          '<li>Odrážejte se do strany a ne dozadu, nohy zůstávají v ose těla.</li>'
          '<li>Padat se učte na chrániče, ideálně dopředu na kolena a zápěstí.</li></ol>'
          '<h2>Údržba a bezpečné bruslení</h2>'
          '<p>Po jízdě na mokru brusle vysušte, ložiska občas vyčistěte a promažte a kolečka přehazujte, aby se opotřebovávala rovnoměrně. Kolečko s hranou nakloněnou na jednu stranu zhoršuje zatáčení. Při jízdě mimo pěší zóny respektujte provoz a nikdy nejezděte po silnici pro auta. Chcete-li k bruslím přidat oblečení, hodí se <a href="/leginy/">legíny</a> a <a href="/sportovni-podprsenky/">sportovní podprsenky</a>. Variantou pro lehký start jsou <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>.</p>'
          '<h2>Co zkontrolovat před koupí</h2>'
          '<ul><li><strong>Střih:</strong> pata drží, špička netlačí, manžeta nedře.</li>'
          '<li><strong>Velikost:</strong> podle délky chodidla v tabulce výrobce, ne podle běžných bot.</li>'
          '<li><strong>Kolečka:</strong> menší pro začátky, větší pro rychlost a vzdálenost.</li>'
          '<li><strong>Brzda:</strong> patní brzda je pro začátečnice samozřejmost.</li>'
          '<li><strong>Chrániče:</strong> zápěstí, kolena, lokty a helma.</li></ul>',
    faq=[
        ('Jaké dámské inline brusle jsou nejlepší pro začátečnici?',
         'Takové s měkčí botou, čtyřmi koleček kolem osmdesáti milimetrů, pevnou patou a patní brzdou. Dobrá stabilita a pohodlí jsou důležitější než rychlost. Přidejte chrániče zápěstí.'),
        ('Čím se dámské inline brusle liší od pánských?',
         'Mají užší patu a štíhlejší kopyto, nižší manžetu a často kratší rám. Rozdíl je největší u rekreačních a fitness modelů. Rozhodující je ale to, jak bota sedí na vaší noze.'),
        ('Jakou velikost brusle zvolit?',
         'Změřte chodidlo večer od paty po nejdelší prst a porovnejte s tabulkou výrobce. Brusle mají sedět těsněji než boty a pata se nesmí zvedat. Pozor na odlišné systémy velikostí.'),
        ('Tři, nebo čtyři kolečka?',
         'Čtyři menší jsou stabilnější a obratnější, hodí se pro začátky a rekreaci. Tři větší jsou rychlejší a lépe zvládají nerovnosti, ale vyžadují zkušenější techniku.'),
        ('Jak velká kolečka vybrat?',
         'Pro začátky a menší ženy kolem osmdesáti milimetrů, na delší jízdu a vyšší rychlost větší, kolem sto deseti. Větší kolečka jedou plynuleji, ale hůře se řídí a váží více.'),
        ('Jaké chrániče jsou nutné?',
         'Zápěstí, kolena, lokty a helma. Nejčastějším úrazem je pád dopředu na ruku, proto jsou chrániče zápěstí na prvním místě. Vybírejte velikost podle obvodu zápěstí, kolene a lokte.'),
        ('Mohu brusle používat i na silnici?',
         'Ne, silnice patří autům. Bruslete na cyklostezkách, v parcích a na uzavřených plochách. Dbejte na pravidla a na chodce.'),
        ('Jak poznat, že brusle sedí?',
         'Prsty se lehce dotýkají špičky, pata nezvedá při pokrčení kolen a nikde není bodový tlak. Pokud se po deseti minutách objeví bolest, má bota špatnou velikost nebo tvar.'),
        ('Kdy přejít na větší kolečka?',
         'Až se naučíte brzdit, plynule zatáčet a bruslit delší trasu. Větší kolečka dají vyšší rychlost, ale brusle se s nimi řídí hůř, proto s nimi nespěchejte.'),
        ('Jak o brusle pečovat?',
         'Po mokru je vysušte, ložiska čistěte a mažte, kolečka přehazujte, aby se obrušovala rovnoměrně. Zkontrolujte šrouby a brzdu před každou delší jízdou.'),
    ],
)

# ------------------------------------------------------------------ sportovni-obleceni-damske
NEW['sportovni-obleceni-damske'] = dict(
    title='Sportovní oblečení dámské: střih, velikosti, výběr',
    desc='Dámské sportovní oblečení: střihy pro ženy, velikosti, materiály a sestavení šatníku na běh, fitness, hory i vodu. Porovnejte nabídky obchodů.',
    intro='<p>Dámské sportovní oblečení není zmenšená verze pánského. Ženské střihy počítají s užšími rameny, výraznějším pasem a boky, kratším trupem a odlišnými potřebami při pohybu, od podprsenky až po délku nohavic. Správně vybraný kousek se pozná podle toho, že si ho při sportu nevšímáte: nesjíždí, nedře a nepromoká dřív, než má. '
          'Na této stránce jsou výrobky z kategorie <a href="/sportovni-obleceni/">sportovní oblečení</a> určené ženám, od triček a legín přes mikiny a bundy až po plavky. Průvodce ukazuje, jak se liší střih a velikosti, jak poskládat šatník podle aktivity, na co dát pozor u podprsenek a legín a jak se starat o funkční materiály. '
          'Pánské kousky najdete v <a href="/sportovni-obleceni-panske/">pánském oblečení</a>, dětské v <a href="/detske-sportovni-obleceni/">dětském sportovním oblečení</a>.</p>',
    guide='<h2>V čem je ženský střih jiný</h2>'
          '<p>Ženské tělo má v průměru užší ramena a výraznější rozdíl mezi pasem a boky. Dámský střih to zohledňuje: ramena jsou užší, trup kratší, pas přiléhavější a boky prostornější. Kalhoty mají jiný sed v pase a v rozkroku, rukávy jsou kratší a bundy mají úzký průřez. Když si žena obleče pánský střih, často narazí na široká ramena, příliš dlouhé rukávy nebo bundu, která se zachytí na bocích. Naopak štíhlá žena s širšími rameny může být spokojenější v unisex střihu, takže označení bere jako vodítko.</p>'
          + T(['Kousek', 'Co se u dámského střihu mění', 'Na co si dát pozor'], [
              ['Trička a topy', 'užší ramena, kratší délka, tvarování v pase', 'rukáv by neměl škrtit při zvednutí paží'],
              ['Mikiny a bundy', 'užší průřez, kratší rukáv, tvarovaný pas', 'u bund počítejte s vrstvou pod nimi'],
              ['Legíny a kalhoty', 'jiný sed v pasu a prostornější boky', 'délka nohavice a výška pasu se liší podle modelu'],
              ['Podprsenky', 'velikost obvodu hrudníku a košíčku', 'podpora se volí podle zátěže'],
              ['Plavky', 'tvar podle aktivity: bazén nebo pláž', 'sportovní plavky drží lépe než módní']]) +
          '<h2>Velikosti a jak se v nich vyznat</h2>'
          '<p>Dámské velikosti se označují čísly, nejčastěji 34 až 44, nebo písmeny od XS po XL. Každý výrobce ovšem střihá jinak. Sportovní značky střihají přiléhavěji, outdoorové a módní prostorněji. Číslo velikosti proto vždy ověřte v tabulce konkrétního výrobce, změřte si obvod hrudníku, pasu a boků a porovnejte. Pokud padnete mezi dvě velikosti, rozhoduje typ oblečení. U přiléhavých legín a topů bývá lepší menší pro pevnou oporu, u mikin a bund větší, abyste měla pod nimi místo na další vrstvu.</p>'
          '<ul><li><strong>Obvod hrudníku:</strong> měřte v nejširším místě pod podpažím a nad podprsenkou.</li>'
          '<li><strong>Obvod pasu:</strong> v nejužším místě trupu, nejčastěji nad pupkem.</li>'
          '<li><strong>Obvod boků:</strong> v nejširším místě.</li>'
          '<li><strong>Délka nohavice:</strong> změřte vnitřní stranu nohy a porovnejte s údajem u kalhot.</li>'
          '<li><strong>Materiál s elastanem:</strong> přizpůsobí se tělu, takže drobné rozdíly odpustí.</li></ul>'
          '<h2>Šatník podle aktivity</h2>'
          '<p>Nejsnazší cesta je sestavit si základ podle toho, co skutečně děláte. Nemusíte kupovat vše najednou, stačí tři až pět kusů, které spolu fungují, a kombinovat je s vrstvami podle počasí.</p>'
          + T(['Aktivita', 'Základ šatníku', 'Odkazy'], [
              ['Běh a kondice', 'funkční tričko, legíny nebo šortky, podprsenka s vyšší podporou', '<a href="/funkcni-tricka/">funkční trička</a>, <a href="/leginy/">legíny</a>, <a href="/sportovni-kratasy/">kraťasy</a>'],
              ['Posilovna a jóga', 'přiléhavé legíny, top, měkká mikina na rozcvičení', '<a href="/leginy/">legíny</a>, <a href="/mikiny/">mikiny</a>'],
              ['Turistika a hory', 'termoprádlo, softshell, nepromokavá vrstva', '<a href="/termopradlo/">termoprádlo</a>, <a href="/sportovni-bundy/">bundy</a>'],
              ['Zimní sporty', 'merino nebo syntetika na tělo, fleece, membránová bunda', '<a href="/kabaty-a-parky/">kabáty a parky</a>, <a href="/sportovni-rukavice/">rukavice</a>'],
              ['Voda a plavání', 'sportovní plavky, rychleschnoucí tričko', '<a href="/plavky/">plavky</a>'],
              ['Týmové sporty', 'dres, kraťasy, ponožky', '<a href="/dresy/">dresy</a>, <a href="/sportovni-ponozky/">ponožky</a>']]) +
          '<h2>Sportovní podprsenka: nejdůležitější kus</h2>'
          '<p>Správně zvolená podprsenka rozhoduje o pohodlí při běhu i skocích víc než kterýkoli jiný kus. Dělí se podle zátěže: nízká podpora pro jógu a pilates, střední pro kolo a fitness a vysoká pro běh, skoky a míčové sporty. Zvolte přesnou velikost, protože příliš velká neopře a příliš malá tlačí. Zkoušku proveďte pohybem: zvedněte ruce, předkloňte se a poskočte. Pokud se prsa výrazně pohybují, podpora nestačí. Přehled najdete v kategorii <a href="/sportovni-podprsenky/">sportovní podprsenky</a>. K tělu patří i <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>, bez švů, které při pohybu nedře.</p>'
          '<h2>Legíny a kalhoty: pas, délka a materiál</h2>'
          '<p>U legín rozhoduje výška pasu a pevnost materiálu. Vysoký pas drží břicho a nesjíždí při předklonu, nízký je pohodlný pro lehké aktivity. Materiál by měl být neprůsvitný i při hlubokém dřepu, což si ověříte otestováním před zrcadlem nebo v popisu. Délka nohavic se liší: sedmiosminové a kapri se hodí do tepla a na jógu, dlouhé na chlad a běh venku. Zimní varianty mají česanou vnitřní stranu. Více najdete v kategoriích <a href="/leginy/">legíny</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>'
          '<h2>Vrstvení pro chlad a vodu</h2>'
          '<p>Základem je třívrstvý systém: vrstva na kůži odvádí pot, střední zahřívá a vnější chrání před větrem a deštěm. Mnoho žen vnímá chlad na rukou, nohou a hlavě dřív než na trupu, proto se v zimě vyplatí kvalitní rukavice, čepice a ponožky, viz <a href="/cepice-a-celenky/">čepice a čelenky</a> a <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a>. Při vodních sportech a koupání dává smysl sportovní střih plavek, který se při pohybu neposouvá. U termoprádla zvažte merino pro dlouhé dny bez praní, syntetiku pro intenzivní pohyb.</p>'
          '<h2>Značky v dámském oblečení</h2>'
          '<p>Sportovní základ nabízejí ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('under-armour', 'Under Armour')) + ', outdoorové vrstvy ' + B(('columbia', 'Columbia'), ('the-north-face', 'The North Face'), ('haglofs', 'Haglöfs'), ('regatta', 'Regatta')) + ', běžecké a horské kousky ' + B(('dynafit', 'Dynafit'), ('craft', 'Craft'), ('kilpi', 'Kilpi'), ('4f', '4F')) + '. Norská značka ' + B(('kari-traa', 'Kari Traa')) + ' se soustředí právě na ženy a je známá vlněnými vrstvami. Plavecký sortiment zastupuje ' + B(('speedo', 'Speedo')) + '. Rozdíly mezi značkami jsou hlavně ve střihu a cíli použití, takže před koupí porovnejte tabulky velikostí.</p>'
          '<h2>Bundy a vesty podle ženského střihu</h2>'
          '<p>Bunda by měla v ramenou sedět přesně, protože tam se střih nejhůř koriguje. Rukáv musí po zvednutí paží zůstat nad zápěstím a zadní díl se nesmí vytahovat nad pás. Zkoušejte ji s vrstvou, kterou budete nosit pod ní, tedy s mikinou nebo fleecem. U bund s kapucí si ověřte, zda ji lze stáhnout, a u zimních kabátů pak, zda se dá zapnout zip přes bundu. Vesty jsou praktickou střední vrstvou, ale pozor na délku: při sedu na kole a při předklonu nesmí odhalit záda. Lehčí kousky na jaro a podzim najdete v kategoriích <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/zimni-bundy/">zimní a péřové bundy</a>.</p>'
          '<h2>Barvy, viditelnost a praktičnost</h2>'
          '<p>Tmavé barvy zakrývají pot, skvrny i drobné vady, ale venku za šera se ztrácejí. Pro běh nebo kolo ve večerních hodinách proto vybírejte svítivé barvy nebo kousky s odrazivými prvky. Světlé kousky jsou příjemné v létě, protože méně pohlcují teplo, vyžadují ale častější praní. Při skládání šatníku držte základ v neutrálních odstínech a přidejte jeden nebo dva barevné kusy, které oživí celek a půjdou kombinovat. Uvnitř švy a štítky ověřte dotykem, dráždivý štítek zkazí dlouhý trénink.</p>'
          '<h2>Kdy kupovat a jak dlouho oblečení vydrží</h2>'
          '<p>Zimní vrstvy se obvykle nejvýhodněji pořizují na konci sezony, letní kousky zase na začátku podzimu. Zvažte ale, zda vám sedí velikost, protože při výprodeji mohou zbývat jen okrajové velikosti. Životnost závisí na péči a intenzitě: funkční tričko a legíny na pravidelný trénink se po několika sezonách unaví, protože elastan ztrácí pružnost a materiál se vytahuje. Znamení, že je čas vyměnit podprsenku, je ztráta opory a roztažené ramínko, u legín průsvitnost v kolenou. Oblečení, které je ještě v pořádku, ale nepadne, odložte a nenoste přes sílu.</p>'
          '<h2>Péče o funkční materiály</h2>'
          '<ol><li>Perte při doporučené teplotě, obvykle třicet až čtyřicet stupňů.</li>'
          '<li>Nepoužívejte aviváž, zanáší vlákna a snižuje odvod vlhkosti.</li>'
          '<li>Zapněte zipy a u membránových bund použijte prostředek určený pro outdoorové prádlo, vodoodpudivá vrstva pak vydrží déle.</li>'
          '<li>Sušte na vzduchu, vysoká teplota poškodí elastan a potisk.</li>'
          '<li>Neskladujte vlhké oblečení v tašce, pach se zakoření.</li></ol>'
          '<h2>Co zkontrolovat před koupí</h2>'
          '<ul><li><strong>Střih:</strong> dámský nebo unisex podle vašich proporcí.</li>'
          '<li><strong>Velikost:</strong> podle míry a tabulky výrobce.</li>'
          '<li><strong>Účel:</strong> trénink, hory nebo městský styl, každý chce jiný materiál.</li>'
          '<li><strong>Sezóna:</strong> lehké vrstvy na léto, česané na zimu.</li>'
          '<li><strong>Neprůsvitnost a švy:</strong> zvlášť u legín a podprsenek.</li></ul>',
    faq=[
        ('Jaká velikost dámského sportovního oblečení mi sedne?',
         'Změřte obvod hrudníku, pasu a boků a porovnejte s tabulkou konkrétního výrobce. Sportovní značky střihají přiléhavěji než outdoorové. U přiléhavých kusů bývá lepší menší velikost, u mikin a bund větší.'),
        ('Čím se liší dámské a pánské sportovní oblečení?',
         'Dámské má užší ramena, kratší trup, tvarovaný pas a prostornější boky. Rukávy bývají kratší a kalhoty mají jiný sed. Při špatném střihu se oblečení vrásní, svírá nebo sklouzává.'),
        ('Jak vybrat sportovní podprsenku?',
         'Podle zátěže: nízká podpora na jógu, střední na kolo a fitness, vysoká na běh a skoky. Velikost musí být přesná. Zkuste ji s poskočením a zvednutím paží.'),
        ('Co si obléknout na běh venku?',
         'Funkční tričko, legíny nebo kraťasy a podprsenku s vyšší podporou. Při chladu přidejte lehkou větrovku nebo tenkou vrstvu s dlouhým rukávem. Bavlnu na kůži raději vynechte.'),
        ('Jaké legíny nejsou průsvitné?',
         'Takové, které mají hustší úplet a dostatečnou gramáž. Ověřte si to dřepem před zrcadlem nebo se podívejte na popisy a recenze. Tmavé barvy zakrývají lépe než světlé.'),
        ('Je lepší merino, nebo syntetika?',
         'Merino hřeje i za vlhka a méně zapáchá, hodí se na delší dny bez praní. Syntetika rychleji schne a lépe snáší intenzivní pohyb. Obojí je dobrá volba, záleží na aktivitě.'),
        ('Jak prát sportovní oblečení?',
         'Při třiceti až čtyřiceti stupních, bez aviváže a se zapnutými zipy. Sušte na vzduchu a vyhýbejte se žehlení. Outdoorové vrstvy perte speciálním prostředkem.'),
        ('Jak poskládat základní šatník na sport?',
         'Stačí tři až pět kusů: dvě trička, legíny nebo kraťasy, podprsenka a mikina. K tomu přidejte vrstvu podle počasí. Kombinujte je s ohledem na aktivitu.'),
        ('Mám brát unisex, nebo dámské?',
         'Rozhoduje střih na vašem těle. Štíhlá žena se širšími rameny může být spokojenější v unisex, užší postava v dámském. Vyzkoušejte a porovnejte tabulky.'),
        ('Kde najdu dámské oblečení pro konkrétní sport?',
         'V podkategoriích nad výpisem: trička, legíny, mikiny, bundy, plavky, termoprádlo, dresy a další. V každé porovnáte nabídky obchodů a velikosti skladem.'),
    ],
)

# ------------------------------------------------------------------ salomon-trekove-boty
NEW['salomon-trekove-boty'] = dict(
    title='Salomon trekové boty: modely, střih a výběr podle terénu',
    desc='Salomon trekové boty: lehké X Ultra, XA Pro, Quest a Outscape. Střih, velikosti, membrána GTX a rozdíl mezi nízkou a vysokou botou. Porovnejte nabídky.',
    intro='<p>Salomon je alpská značka, která se od lyžařských vázání dostala k obuvi pro horské prostředí. V trekových botách sází na rychlou a lehkou turistiku a z trailových bot převzala přiléhavou stavbu i způsob šněrování. Boty mají pevné držení paty, přiléhavou špičku, rychlé šněrování a podrážku s hrubým vzorkem. '
          'Na této stránce jsou boty značky Salomon z kategorie <a href="/trekova-obuv/">trekové boty</a>. Najdete tu nízké modely na cesty i vyšší na kamenitý terén, lehké boty pro rychlý pohyb i pevnější verze pro těžší batoh. Průvodce vysvětluje, jak se řady liší, co znamenají zkratky GTX, WP a Mid, jak sedí střih a jakou velikost zvolit. '
          'Rozdíly podle pohlaví řeší <a href="/trekove-boty-panske/">pánské</a>, <a href="/damske-trekove-boty/">dámské</a> a <a href="/detske-trekove-boty/">dětské trekové boty</a>.</p>',
    guide='<h2>Jak poznat sortiment Salomonu v trekových botách</h2>'
          '<p>Značka staví sortiment na několika řadách, které se podle názvu rozliší. Základní myšlenka je stejná: lehká konstrukce, pevné držení chodidla a podrážka pro jistý krok. Rozdíl je v tom, kolik tuhosti a ochrany bota nabízí. Pro orientaci poslouží přehled řad, které se v nabídce objevují.</p>'
          + T(['Řada', 'Pro koho a na co', 'Čím se pozná'], [
              ['X Ultra', 'rychlá turistika, jednodenní túry, nízké i polovysoké boty', 'varianty Mid a GTX, dámská verze s W v názvu'],
              ['XA Pro 3D', 'stabilní boty původem z trailu, rovnovážný krok, mix terénu', 'sportovní vzhled, často v dětské verzi'],
              ['Quest', 'těžší turistika a vícedenní trek s batohem', 'vyšší svršek, zesílená konstrukce, GTX'],
              ['X-Adventure Recon', 'náročnější terén a přístup k vrcholům', 'verze Mid a GTX, pevná špička'],
              ['Outscape, Extegra, Elixir, Shelter', 'vstup do turistiky a běžné túry', 'jednodušší konstrukce, verze WP'],
              ['Speedcross a Aero Glide', 'trailový a běžecký původ, rychlý pohyb', 'agresivnější vzorek nebo lehká konstrukce']]) +
          '<p>Jména modelů se v čase obměňují a číslo za názvem označuje generaci. Mezi trekovými botami se v nabídce objevují i modely původně běžecké, proto před koupí zkontrolujte popis určení. Pokud potřebujete lehčí trailovou botu, najdete ji v kategorii <a href="/trailove-boty/">trailové boty</a> a v odkazu <a href="/salomon-bezecke-boty/">Salomon běžecké boty</a>.</p>'
          '<h2>Zkratky v názvech a co znamenají</h2>'
          '<ul><li><strong>GTX:</strong> verze s membránou Gore-Tex, která zadrží vodu a propouští vodní páru.</li>'
          '<li><strong>WP:</strong> voděodolná verze s jinou membránou, často pro krátké deště a vlhkou trávu.</li>'
          '<li><strong>Mid:</strong> polovysoký svršek, který drží kotník a chrání před kamínky.</li>'
          '<li><strong>W:</strong> dámská verze s užším střihem a jinými barvami.</li>'
          '<li><strong>J:</strong> junior, dětská velikost.</li>'
          '<li><strong>LTR:</strong> kožený svršek místo textilu.</li></ul>'
          '<p>Membrána má smysl na mokré trávě, v dešti a při sněhu. V horku nebo při chůzi v suchu je naopak zbytečná, protože bota hůř prodýchává a pomaleji schne. U Salomonu proto stojí za zvážení nepromokavá a nemembránová verze téhož modelu.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Boty této značky jsou známé přiléhavým, spíše užším střihem s dobrým držením paty. Hodí se úzkému až střednímu chodidlu, širší noha může potřebovat širší verzi nebo jiný model. Salomon často používá čísla se zlomky, například třetinové velikosti, což pomáhá dolaďovat sed. Změřte délku chodidla, porovnejte s tabulkou a před špičkou nechte rezervu kolem jednoho centimetru, aby se prsty neopíraly při sestupu.</p>'
          '<ul><li><strong>Zkoušejte odpoledne:</strong> noha je větší a podobá se stavu po túře.</li>'
          '<li><strong>Vezměte ponožky na túru:</strong> tenké městské ponožky zkreslí výsledek, viz <a href="/sportovni-ponozky/">sportovní ponožky</a>.</li>'
          '<li><strong>Sestup:</strong> na šikmé ploše by se prsty neměly dotýkat špičky.</li>'
          '<li><strong>Pata:</strong> při chůzi do kopce nesmí vyskakovat, jinak vznikají puchýře.</li>'
          '<li><strong>Šněrování:</strong> rychlé stahování zrychluje obouvání, ale konec šňůrky je nutné zastrčit do kapsy na jazyku.</li></ul>'
          '<h2>Nízká, nebo polovysoká bota</h2>'
          '<p>Salomon se silně opírá o nízké modely, protože odpovídají jeho trailovému původu. Nízká bota je lehčí a rychle schne, ale kotník drží méně. Polovysoká přidá oporu a ochranu před kamením a hodí se na nerovný terén a těžší batoh. Vyšší boty s pevnějším svrškem pro náročné treky tvoří užší část nabídky, patří sem hlavně řada Quest. Nízké a vysoké najdete také v kategoriích <a href="/nizke-trekove-boty/">nízké trekové boty</a> a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>.</p>'
          + T(['Situace', 'Doporučení', 'Proč'], [
              ['Suché cesty, rychlá túra', 'nízká bota bez membrány', 'lehká, prodyšná, rychle schne'],
              ['Mokrá tráva a déšť', 'nízká nebo Mid s GTX', 'drží vodu mimo botu'],
              ['Kamenitý a nerovný terén', 'Mid s tužší podrážkou', 'opora kotníku a ochrana špičky'],
              ['Těžší batoh, vícedenní trek', 'řada Quest nebo jiná vyšší bota', 'tužší konstrukce a lepší držení'],
              ['Hřebeny a sněhová pole', 'pevný vzorek a vyšší svršek', 'jistější krok, ochrana před sněhem']]) +
          '<h2>Podrážka a držení</h2>'
          '<p>Salomon používá vlastní gumové směsi a hrubý vzorek, který dobře drží v blátě a na mokré trávě. Vzorek s hlubšími výstupky zabírá v měkkém terénu, naopak na hladkém chodníku se rychleji opotřebuje a hlučí. Pokud většinu cesty tvoří asfalt, nemusí být nejagresivnější vzorek ideální. Tuhost podrážky určuje, jak boty chrání chodidlo před kameny: čím pevnější, tím lepší ochrana při těžší zátěži, ale tím méně citu pro terén. Většinu lehkých modelů nelze znovu podrážkovat, takže se po opotřebení vyměňují za nové.</p>'
          '<h2>Salomon vs. jiné značky a další kategorie</h2>'
          '<p>Oproti tradičním alpským značkám s kožením svrškem je Salomon lehčí, přiléhavější a rychleji se rozchodí, ale jeho textilní modely snášejí hrubé zacházení hůře. Kdo chce srovnat s jiným výrobcem, může otevřít stránku <a href="/adidas-trekove-boty/">Adidas trekové boty</a>. Všechny nabídky značky v této kategorii najdete také na stránce <a href="/znacka/salomon/">Salomon</a>. K botám se hodí <a href="/trekove-hole/">trekové hole</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h2>Dámské a dětské modely značky</h2>'
          '<p>Dámské boty s písmenem W mají užší patu, štíhlejší střih a nižší manžetu, takže lépe obepnou ženskou nohu. Mezi dámskými modely v nabídce najdete například řady X Ultra 360 W a Aero Glide nebo lehčí Saliba. Ženy s širší nohou mohou zkusit unisex či pánskou verzi menší velikosti, ale pozor na délku. Dětské a juniorské modely, které poznáte podle písmene J nebo slov Kids a Junior, mají stejné technologie jako dospělé, ale menší velikost a často ohebnější podrážku. U rostoucích dětí nechte rezervu kolem jednoho centimetru, ale nepřehánějte, příliš velká bota se kroutí při chůzi. Další možnosti najdete v <a href="/damske-trekove-boty/">dámských trekových botách</a> a <a href="/detske-trekove-boty/">dětských trekových botách</a>.</p>'
          '<h2>Šněrování a nastavení</h2>'
          '<p>Rychlé stahování Quicklace se utahuje jedním tahem a drží sevřenou špičku, ale neumožňuje jemné nastavení jednotlivých zón. Klasické tkaničky jsou o něco pomalejší, zato vám dovolí povolit nárt pro dlouhý sestup a utáhnout kotník pro stoupání. Při dlouhém klesání se vyplatí boty povolit v oblasti špičky a utáhnout na kotníku, aby se noha nesunula dopředu. Při bolesti nártu zkuste šněrování přeskočit nebo vložit podložku pod jazyk. Podpatek jistí tzv. zamčená pata: protáhněte tkaničku horním očkem dvakrát a utáhněte, aby pata neklouzala.</p>'
          '<h2>První túra v nových botách</h2>'
          '<p>Novou botu nenechávejte na první dlouhou túru. Rozchoďte ji několika kratšími procházkami doma i venku a sledujte místa, kde se objevuje tlak. Textilní svršky se rozchodí rychle, kožené déle. Vezměte si na cestu náplast na puchýře a v případě tlaku na patě zastavte hned, protože drobné odření se za hodinu změní v ránu. Před každým výletem zkontrolujte tkaničky a podrážku, zda neobsahuje kamínky, které by zhoršovaly přilnavost.</p>'
          '<h2>Ponožky a vložky</h2>'
          '<p>Na túru se hodí ponožky z merina nebo syntetiky, které odvádějí vlhkost a netvoří rýhy. Bavlna navlhne a vede k puchýřům. Tloušťka ponožky mění sed boty, a proto zkoušejte s těmi, které budete nosit. Standardní vložky u lehkých modelů jsou tenké a při delším nošení se opotřebují, takže je lze nahradit tužší anatomickou vložkou. Pokud máte problém s vyklenutím nebo plochou nohou, poraďte se s odborníkem na obuv. Boty pak nemají přesahovat prostor, který ponožky zabírají.</p>'
          '<h2>Péče o boty</h2>'
          '<ol><li>Po túře vyndejte vložky a nechte boty vyschnout při pokojové teplotě, ne na topení.</li>'
          '<li>Očistěte bláto kartáčem a vlažnou vodou.</li>'
          '<li>Membránu a svršek občas ošetřete impregnací vhodnou pro daný materiál.</li>'
          '<li>Šněrovadla a rychlé stahování kontrolujte, opotřebovaná se vymění levně.</li>'
          '<li>Neskladujte mokré boty v tašce nebo kufru auta.</li></ol>'
          '<h2>Co zkontrolovat před koupí</h2>'
          '<ul><li><strong>Řada a určení:</strong> turistická, trailová nebo horská.</li>'
          '<li><strong>Výška svršku:</strong> nízká, Mid, vyšší.</li>'
          '<li><strong>Membrána:</strong> GTX nebo WP pro mokro, bez membrány pro teplo.</li>'
          '<li><strong>Střih:</strong> užší sedne spíše štíhlé noze.</li>'
          '<li><strong>Velikost skladem:</strong> v obchodech se liší, porovnejte.</li></ul>',
    faq=[
        ('Jaké Salomon trekové boty vybrat na běžnou turistiku?',
         'Pro jednodenní túry na cestách a lesních stezkách se hodí nízké nebo polovysoké modely řady X Ultra. Pokud čekáte vlhko, zvolte verzi GTX, v suchu stačí bez membrány.'),
        ('Co znamená GTX v názvu boty?',
         'Označuje membránu Gore-Tex, která zabrání proniknutí vody a zároveň propouští vodní páru. Hodí se na deštivé dny, mokrou trávu a sníh. V horku bývá teplejší než verze bez membrány.'),
        ('Jak sedí boty Salomon?',
         'Spíše přiléhavě a užší, s dobrým držením paty. Širší noha může potřebovat jiný model nebo širší verzi. Vždy zkontrolujte tabulku velikostí a zkoušejte s ponožkou na túru.'),
        ('Je lepší nízká, nebo polovysoká bota?',
         'Nízká je lehčí a rychleji schne, polovysoká drží kotník a chrání před kamínky. Na kamenitý terén a těžší batoh vybírejte Mid, na rychlé túry nízkou.'),
        ('Mohu v Salomonech jít na vícedenní trek?',
         'Ano, ale volte robustnější modely, například řadu Quest, s pevnější konstrukcí a lepší oporou. Lehčí modely vyžadují menší zátěž a zkušenější chůzi.'),
        ('Jak vybrat velikost?',
         'Změřte chodidlo odpoledne a porovnejte s tabulkou výrobce, před špičkou nechte rezervu kolem jednoho centimetru. Salomon používá i třetinové velikosti, takže se dá dolaďovat.'),
        ('Co znamenají W, J a Mid?',
         'W je dámská verze, J junior a Mid polovysoký svršek, který drží kotník. Označení pomáhá rychle rozlišit určení modelu bez čtení celého popisu.'),
        ('Jak o boty pečovat?',
         'Po túře je vysušte při pokojové teplotě, očistěte bláto vlažnou vodou a občas ošetřete impregnací. Šněrování a vložky kontrolujte před každou delší túrou.'),
        ('Jsou Speedcross trekové boty?',
         'Jde o trailovou běžeckou botu s agresivním vzorkem. Na rychlý pohyb v blátě se hodí, na dlouhé túry s batohem jsou vhodnější boty z turistických řad.'),
        ('Dají se boty znovu podrážkovat?',
         'U většiny lehkých modelů ne, protože mají lepenou konstrukci. Po opotřebení podrážky se vyměňují za nové. Těžší horské boty s prošívanou podrážkou se podrážkují častěji.'),
    ],
)
