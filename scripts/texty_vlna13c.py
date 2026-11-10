"""sporteka.cz — wave 13c (4. 11. 2026): long texts (>= 1650 words) for cyklisticke-obleceni, zimni-bundy, mestske-batohy, lyzarske-bundy.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklisticke-obleceni
NEW['cyklisticke-obleceni'] = dict(long=True,
    title='Cyklistické oblečení: dresy, kraťasy, bundy | Sporteka',
    desc='Cyklistické oblečení na silnici, MTB i do města. Průvodce vrstvením, šámem, velikostmi a péčí, nabídky českých e-shopů porovnané na jednom místě.',
    intro='<p><strong>Cyklistické oblečení</strong> se od běžného sportovního liší tím, že vzniklo pro jednu konkrétní polohu těla: předklon, ruce na řídítkách, hodiny v sedle a stálý proud vzduchu. Proto mají dresy delší záda, kalhoty vloženou vycpávku a rukavice zesílené dlaně. Dobrý kus se pozná až po první delší vyjížďce, kdy nic netře, nevlaje a nenasákne potem. Právě tuto zkušenost se snaží přehled níže usnadnit.</p>'
          '<p>Na Sportece najdete celou škálu pohromadě: <a href="/cyklisticke-dresy/">dresy</a>, <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy a kalhoty</a>, <a href="/cyklisticke-rukavice/">rukavice</a>, <a href="/cyklisticke-bundy-a-vesty/">bundy a vesty</a>, <a href="/cyklisticke-ponozky/">ponožky</a> i <a href="/cyklisticke-navleky/">návleky a rukávky</a>. U každého kusu vidíte nabídky více českých obchodů vedle sebe a můžete porovnat dostupné velikosti i dobu doručení.</p>',
    guide='<h2>Z čeho se cyklistický outfit skládá</h2>'
          '<p>Kompletní výbava není jeden kus, ale sada dílů, které spolu spolupracují. Spodní vrstva odvádí pot, dres a kalhoty drží tvar a pohodlí, vrchní vrstva řeší vítr a vodu. Pokud některý díl vynecháte nebo ho nahradíte civilním oblečením, pocítíte to hlavně po první hodině jízdy.</p>'
          + T(['Díl výbavy', 'K čemu slouží', 'Na co si dát pozor'], [
              ['<a href="/cyklisticke-dresy/">Dres</a>', 'odvádí pot, má kapsy na záda a delší zadní díl', 'zip a materiál, střih podle polohy na kole'],
              ['<a href="/cyklisticke-kratasy-a-kalhoty/">Kraťasy a kalhoty</a>', 'vložka v sedlové části tlumí tlak', 'velikost a tvar vložky, šev v rozkroku'],
              ['<a href="/cyklisticke-rukavice/">Rukavice</a>', 'chrání dlaně a tlumí otřesy z řídítek', 'délka prstů podle ročního období'],
              ['<a href="/cyklisticke-bundy-a-vesty/">Bundy a vesty</a>', 'zastaví vítr a lehký déšť', 'sbalitelnost a odvětrání'],
              ['<a href="/cyklisticke-ponozky/">Ponožky</a>', 'odvádí vlhkost z chodidla', 'bezešvé zpracování a výška manžety'],
              ['<a href="/cyklisticke-navleky/">Návleky a rukávky</a>', 'dají se přidat nebo sundat za jízdy', 'protiskluzové lemy a přesná délka']]) +
          '<h2>Vrstvení podle počasí</h2>'
          '<p>Ráno vyjíždíte v chladu a v poledne se může oteplit o deset stupňů, proto se vyplatí skládat výbavu z kusů, které se dají odepnout nebo schovat do kapsy. Nejčastější chybou je oblečení podle teploty na zápraží. Za pár minut jízdy tělo vytvoří teplo a vítr naopak odebírá víc, než se čeká, takže správná vrstva je trochu chladná při startu a příjemná po rozjetí.</p>'
          + T(['Podmínky', 'Trup', 'Nohy a ruce'], [
              ['teplý letní den', 'lehký dres s krátkým rukávem', 'kraťasy se šámem, krátké rukavice'],
              ['jaro a podzim', 'dres s dlouhým rukávem nebo rukávky, <a href="/vetrovky/">větrovka</a> v kapse', 'kalhoty nebo <a href="/cyklisticke-navleky/">návleky</a>, rukavice s delšími prsty'],
              ['chladný den kolem nuly', '<a href="/termopradlo/">termoprádlo</a>, zateplený dres, vesta', 'dlouhé kalhoty, zateplené rukavice'],
              ['vytrvalý déšť', '<a href="/nepromokave-bundy/">nepromokavá bunda</a> s manžetou', 'návleky, rukavice, které rychle schnou']]) +
          '<h2>Dres: střih a materiál</h2>'
          '<p>Cyklistický dres je střižen tak, aby zadní díl zakryl záda i při předklonu a rukávy se nezvedaly od zápěstí. Přední díl bývá kratší, aby se nenabíral na břiše. Zip dělený až k hrudi umožní větrání při stoupání, kapsy na zádech pojmou pláštěnku, jídlo nebo klíče. Materiál je téměř vždy syntetický, protože vlákna z polyesteru nasaknou málo a schnou rychle. Merino je jemnější na dotek a méně zapáchá, hodí se na chladnější jízdy.</p>'
          '<p>Rozlišujte střih závodní a volnočasový. Závodní přiléhá těsně a snižuje vlání, volnější střih je pohodlnější na turistické jízdě a v městském provozu. Na horské kolo se kromě těsných modelů používají i volnější dresy s větším průřezem rukávů a odolnější látkou, která snese pád do křoví. Při online nákupu proto sledujte, zda tabulka velikostí udává obvod hrudníku, a porovnejte ho s vlastním měřením.</p>'
          '<h2>Kalhoty a šám</h2>'
          '<p>Šám je profilovaná vložka v sedlové části. Nezvyšuje měkkost jako polštář, ale rozkládá tlak a omezuje tření. Nosí se přímo na kůži bez spodního prádla, protože švy prádla by se mezi vložkou a pokožkou otíraly. Tvar vložky se liší u dámských a pánských modelů, takže dámy by měly vybírat dámský střih. Kalhoty mají někdy kšandy, které drží kus na místě a nestahují pás, jiné mají pružný lem s protiskluzovou páskou na stehnech.</p>'
          '<ul><li><strong>Krátké kalhoty</strong> jsou základ od jara do podzimu, na delší trasy je upřednostní většina jezdců.</li>'
          '<li><strong>Tříčtvrteční a dlouhé kalhoty</strong> udrží kolena v teple, což ocení hlavně ti, kdo jezdí za chladných rán.</li>'
          '<li><strong>Volné MTB kraťasy</strong> se nosí přes vnitřní kraťasy se šámem a mají kapsy i odolnější materiál.</li>'
          '<li><strong>Zimní kalhoty</strong> mají zateplení vpředu a prodloužená záda proti průvanu v kříži.</li></ul>'
          '<h2>Rukavice, ponožky a návleky</h2>'
          '<p>Rukavice patří mezi díly, které si lidé nejčastěji odpouštějí, a právě ony chrání při pádu dlaň i zápěstí. Gelové nebo pěnové zesílení tlumí vibrace, které jinak způsobují mravenčení v prstech. Letní modely mají krátké prsty a prodyšný hřbet, zimní jsou delší a mají větrnou membránu. Rukavice sedí bez záhybů na dlani a špičky prstů se lehce dotýkají konců.</p>'
          '<p>Ponožky pro kolo bývají vyšší než běžné sportovní a mají vzdušnou horní část. Šev na špičce by měl být zploštělý, aby netlačil v tuhé botě. Návleky na nohy a rukávky fungují jako rychlá změna za jízdy: v chladném ránu je navlečete, po rozjetí sundáte. Důležité jsou lemy se silikonovým proužkem, které nesjíždějí. Při nákupu pamatujte i na <a href="/cyklisticka-obuv/">cyklistickou obuv</a>, <a href="/cyklisticke-helmy/">helmu</a> a <a href="/cyklisticke-bryle/">brýle</a>, které doplňují celý outfit.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(('rockbros', 'Rockbros'), ('silvini', 'Silvini'), ('siroko', 'Siroko'), ('craft', 'Craft'), ('haven', 'Haven'), ('r2', 'R2'), ('eleven', 'Eleven'), ('kilpi', 'Kilpi'), ('etape', 'Etape'), ('klimatex', 'Klimatex'), ('loeffler', 'Loeffler'), ('castelli', 'Castelli')) + '. Silvini, Etape a Haven jsou střižené na evropskou postavu a často nabízejí širší řadu velikostí. Craft a Loeffler sázejí na sportovní spodní vrstvy a technické materiály, Castelli je známé závodním střihem. Siroko a Rockbros mají velkou paletu od základních dílů po doplňky. Střih se mezi značkami liší, proto se řiďte vždy tabulkou konkrétního výrobce.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Cyklistické oblečení má sedět přiléhavě, ale ne dusivě. Pokud dres po obvodu tlačí, při předklonu se zadní díl vyhrne a zip se napne. Naopak příliš volný kus vlaje a v rychlejší jízdě vám bude dělat odpor. Vyzkoušejte si polohu na kole a zkontrolujte, zda se rukáv nezvedá a pas neobnažuje záda.</p>'
          + T(['Díl', 'Správné sedění', 'Špatné znamení'], [
              ['Dres', 'přiléhá na hrudník, záda zakrývají kříž při předklonu', 'zip napnutý nebo látka vlající'],
              ['Kalhoty se šámem', 'vložka sedí přesně pod sedacími kostmi', 'vložka se posouvá nebo tvoří záhyby'],
              ['Rukavice', 'dlaň bez záhybů, špičky prstů těsně u konce', 'prázdný prostor ve špičkách'],
              ['Ponožky', 'pata a špička sedí na svých místech', 'ponožka se sesouvá do boty']]) +
          '<p>Měřte hrudník, pas a boky a hodnoty porovnejte s tabulkou. U dámských střihů hledejte označení výrobce pro cyklistiku, protože kalhoty a dresy se liší tvarem v oblasti pasu a boků. U dětí vyberte raději správnou velikost, i když je trochu větší, a ne příliš velký kus, v němž dítě zakopává o vlastní oblečení.</p>'
          '<h2>Viditelnost a bezpečnost</h2>'
          '<p>Při jízdě po silnici či mezi auty nestačí zvolit pěkný dres. Světlé nebo fluorescenční barvy a reflexní prvky na zádech, na bocích a na lemech nohavic zvyšují šanci, že vás řidič zahlédne. V šeru a za deště se vyplatí kombinovat viditelné oblečení s předním a zadním světlem.</p>'
          '<h2>Péče o cyklistické oblečení</h2>'
          '<p>Technické materiály vydrží několik sezón, pokud s nimi zacházíte šetrně. Perte je na nízkou teplotu a bez aviváže, protože ta zalepuje vlákna a zhoršuje odvod potu. Kus se šámem otočte naruby, zapněte zip a nenechte ho dlouho ležet vlhký v tašce. Sušení v sušičce zkracuje životnost pružných vláken, a proto nechte oblečení vyschnout na vzduchu mimo přímé slunce.</p>'
          '<ul><li>Po jízdě dres a kalhoty ihned vyndejte z batohu, aby nepáchly.</li>'
          '<li>Rukavice perte zvlášť, aby se jim neopotřebovaly suché zipy.</li>'
          '<li>Membránové bundy občas obnovte impregnací určenou pro funkční textil.</li>'
          '<li>Vložku se šámem nepřežehlujte a nepoužívejte na ni bělidla.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<p>Nejčastější omyl je kupovat podle designu, ne podle použití. Závodní dres z lehké sítě nebude příjemný v chladu a zimní termo kalhoty zase uvaří ve vedru. Druhou chybou je podcenění šámu: lidé kupují nejlevnější vložku a po dvou hodinách v sedle začnou řešit odřeniny. Třetí chybou je spoléhání na bavlněné tričko, které po hodině nasákne a studí.</p>'
          '<ul><li>Nošení spodního prádla pod kalhoty se šámem.</li>'
          '<li>Kupování příliš velké velikosti v naději, že bude pohodlnější.</li>'
          '<li>Absence rukavic na krátkých jízdách, kde pád přijde nečekaně.</li>'
          '<li>Podcenění větrné vrstvy na sjezdech, kde rychle klesá pocitová teplota.</li></ul>'
          '<h2>Pro koho jaký typ</h2>'
          '<p>Silniční jezdec ocení těsný střih, lehké materiály a minimum švů. Horský cyklista potřebuje odolnost, volnější střih a kapsy, které se nezachytí o větve. Městský cyklista většinou vystačí s běžným oblečením doplněným reflexními prvky a bundou do deště, ke komfortu však přispěje i vložka v kalhotách. Při turistice na kole s dětmi se hodí volnější dresy a kalhoty, protože tempo je pomalejší a častěji se zastavuje. Úplní začátečníci mohou začít jedním dresem, jedněmi kalhotami se šámem a rukavicemi a výbavu postupně rozšiřovat.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Cyklistické oblečení se prodává v sezónních kolekcích, ale základní kusy se mezi lety téměř nemění. Na Sportece proto můžete porovnat stejný model v několika obchodech a vybrat si podle dostupnosti velikosti i podmínek vrácení. Před nákupem zkontrolujte materiál a střih, pak teprve barvu a značku. Kdo kombinuje více dílů, často narazí na to, že různé značky mají jiný střih, a proto je lepší držet se u jednoho výrobce alespoň u kalhot a dresu. Vše, co patří k <a href="/cyklistika/">cyklistice</a>, najdete v nadřazené kategorii.</p>',
    faq=[('Co si obléct na kolo na první jízdu?', 'Stačí funkční tričko, kraťasy nebo kalhoty a rukavice. Pokud se rozhodnete pro pravidelnější jízdu, pořiďte si dres a kalhoty se šámem, které výrazně zvyšují komfort.'),
         ('K čemu je šám v cyklistických kalhotách?', 'Je to profilovaná vložka, která rozkládá tlak a omezuje tření mezi tělem a sedlem. Nepůsobí jako měkký polštář, ale snižuje riziko odřenin.'),
         ('Nosí se pod kalhoty se šámem spodní prádlo?', 'Ne. Šám je navržený pro nošení přímo na pokožce, protože švy prádla by se otíraly a vlhkost by se v nich držela.'),
         ('Jak poznám správnou velikost dresu?', 'Změřte obvod hrudníku a porovnejte ho s tabulkou výrobce. Dres má přiléhat, ale zip se nesmí napínat a zadní díl musí při předklonu zakrýt záda.'),
         ('Proč mají dresy kapsy na zádech?', 'Při předklonu jsou záda nejlépe přístupná a váha věcí v kapsách nepřekáží. Pojmou jídlo, pláštěnku, telefon nebo klíče.'),
         ('Jak se oblékat v chladném počasí?', 'Skládejte vrstvy: termoprádlo, zateplený dres a větrovku, na nohy dlouhé kalhoty nebo návleky. Nejsilnější je chlad na začátku jízdy, po rozjetí se tělo zahřeje.'),
         ('Hodí se bavlněné tričko na kolo?', 'Na krátkou jízdu po městě ano. Na delší trasy se nehodí, protože nasákne potem, těžkne a při větru studí. Lepší je syntetika nebo merino.'),
         ('Jak prát cyklistické oblečení?', 'Na nízkou teplotu a bez aviváže, naruby a se zapnutým zipem. Nesušte v sušičce a nenechávejte mokré v tašce, aby se materiál nezničil a nezapáchal.'),
         ('Jsou rukavice nutné i v létě?', 'Doporučují se. Chrání dlaň při pádu, tlumí otřesy a zlepšují úchop při pocení rukou. Letní modely mají krátké prsty a prodyšný hřbet.'),
         ('Čím se liší dámské a pánské cyklistické oblečení?', 'Střihem v pase a v boku a hlavně tvarem vložky v kalhotách. Dámské modely respektují odlišnou anatomii, takže jsou při delší jízdě pohodlnější.'),
         ('Kdy se hodí návleky na nohy a rukávky?', 'V přechodném období, kdy ráno mrzne a odpoledne hřeje. Navléknete je při startu a po rozjetí je můžete sundat a schovat do kapsy.')],
)

# ------------------------------------------------------------------ zimni-bundy
NEW['zimni-bundy'] = dict(long=True,
    title='Zimní a péřové bundy: výběr podle mrazu | Sporteka',
    desc='Zimní, péřové a zateplené bundy pro město, hory i procházky se psem. Jak vybrat výplň, délku a velikost, nabídky českých e-shopů na jednom místě.',
    intro='<p><strong>Zimní bunda</strong> je kus oblečení, který rozhoduje o tom, zda vás zima bude bavit, nebo otravovat. Jedna má hřát při čekání na zastávce, druhá při svižné chůzi lesem, třetí při práci na zahradě. Podle toho se liší výplň, délka, kapuce i povrchová úprava, a proto se vyplatí nevybírat jen podle vzhledu. Tento přehled vám pomůže zvolit správnou kombinaci tepla, hmotnosti a ochrany.</p>'
          '<p>Na Sportece porovnáte zimní a péřové bundy z českých obchodů a hned vedle najdete příbuzné kategorie: <a href="/lyzarske-bundy/">lyžařské bundy</a> na svah, <a href="/softshellove-bundy/">softshellové bundy</a> pro pohyb, <a href="/nepromokave-bundy/">nepromokavé bundy</a> do mokra a <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> na přechodné období. U každého modelu vidíte více nabídek vedle sebe včetně dostupných velikostí.</p>',
    guide='<h2>Na čem záleží u zimní bundy</h2>'
          '<p>Bunda hřeje tím, že uvnitř zadrží vrstvu vzduchu, kterou ohřeje vaše tělo. Čím víc nehybného vzduchu výplň udrží, tím je bunda teplejší, a čím lépe okolí těsní, tím méně se teplo ztrácí větrem. Samotná tloušťka tedy nerozhoduje: tenčí bunda s dobrým límcem, manžetami a kapucí může hřát víc než nafouklý kabát, kterým profukuje.</p>'
          + T(['Kritérium', 'Co sledovat', 'Proč na tom záleží'], [
              ['Výplň', 'peří, syntetická izolace nebo kombinace', 'určuje teplo, váhu a chování ve vlhku'],
              ['Střih a délka', 'k boku, ke stehnům nebo delší parka', 'krytí při stání a volnost při chůzi'],
              ['Povrch', 'vodoodpudivá úprava nebo membrána', 'ochrana proti sněhu a dešti'],
              ['Těsnění', 'kapuce, límec, manžety, stažení v pase', 'zabrání proudění studeného vzduchu'],
              ['Kapsy', 'zapínání, výška, podšívka', 'ruce v teple a bezpečné uložení věcí']]) +
          '<h2>Výplň: peří, syntetika, nebo kombinace</h2>'
          '<p>Peří je nejlehčí způsob, jak udržet teplo, a dá se stlačit do malého balíku. Jeho slabinou je vlhkost: pokud peří zvlhne, slepí se a přestane izolovat. Hodí se do chladného a suchého počasí, na výlety, na cesty a do měst s mrazivými zimami. Syntetická výplň je těžší a objemnější při stejném teple, ale hřeje i vlhká, rychle schne a hůř se ničí praním, takže ji ocení lidé z vlhčích oblastí nebo ti, kdo se v bundě hodně potí.</p>'
          '<p>Hybridní konstrukce kombinují obě řešení: peří na trupu, kde je teplo potřeba, a syntetiku na ramenou a v podpaží, kde se bunda nejvíc vlhčí. Tenké prošívané bundy slouží spíše jako střední vrstva pod plášť než jako samostatná bunda do silného mrazu.</p>'
          '<h2>Délka a střih podle použití</h2>'
          '<ul><li><strong>Krátká bunda k pasu</strong> se hodí k pohybu, při chůzi nebo při řízení auta se nesvazuje.</li>'
          '<li><strong>Středně dlouhá k půlce stehen</strong> zakryje boky a spodní část zad, takže je nejuniverzálnější pro každodenní nošení.</li>'
          '<li><strong>Parka ke kolenům</strong> hřeje při čekání venku, ale omezuje při rychlé chůzi nebo běhu do schodů.</li>'
          '<li><strong>Vesta</strong> pomáhá udržet teplo trupu, je ale bez rukávů a doplňuje jinou bundu, ne ji nahrazuje.</li></ul>'
          '<p>Dalším aspektem je rezerva v rukávech a v ramenou. Bunda by měla umožnit zvednout ruce nad hlavu, aniž by se zvedl pás. Kdo nosí pod bundou svetr nebo <a href="/fleecove-mikiny/">fleecovou mikinu</a>, měl by to při zkoušení vzít v úvahu, protože na tričko vybraná velikost bude později těsná.</p>'
          '<h2>Vrstvení pod bundou</h2>'
          '<p>Ani nejlepší zimní bunda nenahradí vrstvení. Pod ni patří vrstva, která odvádí pot, například <a href="/termopradlo/">termoprádlo</a>, a případně lehká izolace. Bavlněné tričko drží vlhkost u těla a vy pak mrznete i v silné bundě. Při klidných procházkách stačí jedna vrstva navíc, při pohybu je lepší mít tenčí spodek a bundu rozepnout či sundat. Do mrazu patří i doplňky: <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/sportovni-rukavice/">rukavice</a> a teplé ponožky odvedou více práce než další vrstva trupu.</p>'
          '<h2>Pro jaké použití jakou bundu</h2>'
          + T(['Použití', 'Doporučený typ', 'Doplňky'], [
              ['město, dojíždění', 'středně dlouhá prošívaná nebo péřová bunda s kapucí', 'šála, čepice, rukavice'],
              ['procházky se psem a rodinou', 'delší bunda s odolným povrchem', 'teplá obuv a nepromokavé kalhoty'],
              ['pěší túry v zimě', 'lehká péřová nebo hybridní bunda, <a href="/softshellove-bundy/">softshell</a> jako druhá vrstva', '<a href="/turisticke-batohy/">batoh</a>, <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>'],
              ['svah, lyže a snowboard', '<a href="/lyzarske-bundy/">lyžařská bunda</a> s membránou a sněhovou manžetou', 'lyžařské kalhoty, rukavice, brýle'],
              ['práce venku', 'odolná bunda s dostatkem kapes', 'pevná obuv a pracovní rukavice']]) +
          '<h2>Voda, sníh a vítr</h2>'
          '<p>Většina zimních bund má povrchovou úpravu, která na tkanině vytváří odpudivou vrstvu. Sníh a drobné mrholení po ní stékají, ale při dlouhém dešti se tkanina přesto nasákne. Proti vytrvalému mokru pomůže membrána nebo samostatná <a href="/nepromokave-bundy/">nepromokavá bunda</a> navrch. Pokud často chodíte ve větru, sledujte, zda je tkanina hustě tkaná, protože řídká látka sice dobře dýchá, ale vítr jí proniká. Na poloviční cestě mezi těmito světy jsou <a href="/vetrovky/">větrovky</a> a softshelly.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete bundy od značek ' + B(('regatta', 'Regatta'), ('trespass', 'Trespass'), ('columbia', 'Columbia'), ('dare2b', 'Dare2b'), ('celio', 'Celio'), ('the-north-face', 'The North Face'), ('adidas', 'Adidas'), ('fjallraven', 'Fjällräven'), ('champion', 'Champion'), ('haglofs', 'Haglöfs'), ('helly-hansen', 'Helly Hansen'), ('alpine-pro', 'Alpine Pro'), ('didriksons', 'Didriksons'), ('puma', 'Puma')) + '. Regatta, Trespass a Alpine Pro se zaměřují hlavně na praktické outdoorové oblečení, Columbia a Haglöfs na výlety a hory, Helly Hansen a Didriksons mají tradici v oblečení do vlhkého a větrného počasí. Celio, Champion a Puma nabízejí spíše městský styl.</p>'
          '<h2>Velikost a zkoušení</h2>'
          '<p>Zimní bunda má mít dostatečnou rezervu v ramenou, aby se pod ní vešla alespoň jedna teplá vrstva. Při zkoušení zvedněte ruce nad hlavu a předkloňte se: pokud bunda vyjede nad pas nebo rukávy sklouznou na půl předloktí, je malá. Naopak příliš volná bunda nezadrží teplo, protože se uvnitř hýbe vzduch. Dětem kupujte bundu jen s malou rezervou na růst, s prodloužitelnými rukávy a šňůrkami, ať nezakopávají o lem.</p>'
          '<p>Dámské střihy bývají užší v pase a delší v zádech, pánské širší v ramenou. Kdo se do žádného střihu nevejde, může zkusit unisex model nebo druhou značku. Při online nákupu si nejdřív změřte obvod hrudníku a boků a srovnejte je s tabulkou výrobce. Čísla se mezi značkami liší, takže stejné označení nemusí sedět stejně.</p>'
          '<h2>Péče o péřové a syntetické bundy</h2>'
          '<p>Péřová bunda se pere zřídka, ale pořádně: s prostředkem určeným pro péřové výrobky, při nízké teplotě a šetrném programu. Důležité je dlouhé a opatrné sušení, při kterém se peří rozbíjí. Pomáhá sušení při nízké teplotě s několika čistými tenisovými míčky v sušičce, nebo sušení na vzduchu s častým protřepáním. Syntetické bundy perte podle štítku, bez aviváže, která poškozuje vodoodpudivou úpravu.</p>'
          '<ul><li>Neskladujte bundu natěsno stlačenou, výplň ztrácí objem.</li>'
          '<li>Mokrou bundu nezavírejte do tašky, nejdřív ji vysušte, jinak zapáchá.</li>'
          '<li>Po několika sezónách obnovte impregnaci sprejem nebo prostředkem do pračky.</li>'
          '<li>Skvrny odstraňujte co nejdříve vlhkým hadříkem a jemným prostředkem.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je koupě jen podle vzhledu a ceny, aniž by si kupující ujasnil, v jaké teplotě a při jaké aktivitě bundu bude nosit. Pak se stane, že v městské prošívané bundě na túře mrznete nebo naopak péřová bunda zvlhne za deště. Druhou chybou je ignorování těsnění: bunda s mohutnou výplní, ale bez dobré kapuce a manžet, hřeje jen zdánlivě, protože teplo uniká krkem a rukávy.</p>'
          '<ul><li>Příliš těsná bunda, která nepropustí další vrstvu.</li>'
          '<li>Péřová bunda do mokrého počasí bez náhradní vrstvy.</li>'
          '<li>Kapuce bez možnosti stažení, která v mrazu sklouzne z hlavy.</li>'
          '<li>Absence vnitřní kapsy nebo zapínání kapes na zip, takže z nich za pohybu vypadne telefon.</li></ul>'
          '<h2>Pro koho jak vybrat</h2>'
          '<p>Kdo stráví zimu hlavně v kanceláři a v autě, vystačí s lehčí městskou bundou a doplňky. Pro rodiče malých dětí je důležitá praktičnost: snadné zapínání, odolná tkanina, kapsy na kapesníky a rukavice. Aktivní chodci ocení lehkou a stlačitelnou péřovku, která se vejde do batohu. Lyžaři si mají pořídit specializovanou <a href="/lyzarske-bundy/">lyžařskou bundu</a>, protože sjezdová zátěž je jiná než městská.</p>'
          '<h2>Zimní bunda a doprava</h2>'
          '<p>Kdo jezdí autem, si musí uvědomit, že objemná bunda mění sezení za volantem a bezpečnostní pás přes ni nedoléhá těsně. Pro delší jízdu proto bundu raději rozepněte nebo sundejte. Cyklisté a lidé jezdící na kole do práce potřebují naopak střih s delšími zády a manžetami, které nevyjíždějí. Při cestách MHD oceníte bundu, která se dá snadno svléknout a složit, protože vytopené vozy a mrazivé zastávky se střídají velmi rychle.</p>'
          '<p>Pro děti ve školce a ve škole je dobré ověřit, zda jde bunda snadno zapnout, zda má reflexní prvky a jestli ji zvládne obléknout samo. Odolnější tkanina na loktech a na zadku vydrží dětské hry ve sněhu mnohem déle.</p>'
          '<h2>Kdy a jak nakupovat</h2>'
          '<p>Nové zimní kolekce přicházejí na podzim, kdy je výběr velikostí největší. Slevy se objevují po Vánocích a na konci sezóny, kdy ale zůstávají hlavně krajní velikosti. Na Sportece proto vidíte nabídky více obchodů vedle sebe a můžete vybírat podle skladové dostupnosti i podmínek vrácení. Pokud bundu kupujete pro konkrétní sport, projděte si i nadřazenou kategorii <a href="/sportovni-bundy/">sportovních bund a vest</a>, kde jsou vedle sebe všechny typy.</p>',
    faq=[('Jaká zimní bunda je nejteplejší?', 'Obvykle péřová s větším množstvím kvalitní výplně, dobře těsnící kapucí a delším střihem. Ve vlhkém prostředí ale může lépe obstát bunda se syntetickou izolací.'),
         ('Péřová, nebo syntetická bunda?', 'Péřová je při stejném teple lehčí a lépe se sbaluje, ale vlhkost jí škodí. Syntetická hřeje i vlhká a snáze se pere, je však těžší a objemnější.'),
         ('Jak vybrat velikost zimní bundy?', 'Podle tabulky výrobce a s rezervou na svetr nebo fleece. Při zkoušení zvedněte ruce a předkloňte se, rukávy ani spodní lem by neměly vyjet.'),
         ('Jak prát péřovou bundu?', 'S prostředkem určeným na péří, na nízkou teplotu a šetrný program. Důležité je pečlivé vysušení s občasným protřepáním, aby se peří nezlepilo.'),
         ('Hodí se městská zimní bunda na lyže?', 'Na procházky ano, na svah ne. Lyžařská bunda má membránu, sněhovou manžetu a odolnější tkaninu, které městská bunda většinou nemá.'),
         ('Je lepší delší, nebo kratší bunda?', 'Delší více hřeje při stání a čekání venku, kratší nebrání pohybu. Pro každodenní nošení je nejuniverzálnější délka po půlku stehen.'),
         ('Musí mít zimní bunda kapuci?', 'Není to nutné, ale v mrazu a při větru pomáhá. Důležité je, aby se dala stáhnout a nepřekážela při otáčení hlavy. Odnímatelná kapuce je kompromis.'),
         ('Co nosit pod zimní bundu?', 'Spodní vrstvu, která odvádí pot, a podle mrazu fleece nebo tenký svetr. Bavlněné tričko nasákne a v mrazu ochlazuje.'),
         ('Jak poznám, že bunda je nepromokavá?', 'Vodoodpudivá úprava zvládne sníh a mrholení. Na vytrvalý déšť potřebujete membránu nebo další plášť, což se uvádí v popisu výrobce.'),
         ('Jak dlouho zimní bunda vydrží?', 'Při šetrném zacházení několik sezón. Životnost zkracuje časté praní, stlačené skladování a zanedbaná impregnace povrchu.'),
         ('Kdy je nejlepší doba na nákup?', 'Největší výběr velikostí je na podzim, nižší ceny bývají po Vánocích. Na konci sezóny ale zůstávají hlavně okrajové velikosti.')],
)

# ------------------------------------------------------------------ mestske-batohy
NEW['mestske-batohy'] = dict(long=True,
    title='Městské a sportovní batohy: výběr a velikost | Sporteka',
    desc='Městské a sportovní batohy do práce, školy, na trénink i cesty. Průvodce objemem, zády, materiály a péčí, nabídky českých e-shopů na jednom místě.',
    intro='<p><strong>Městský batoh</strong> nosíte nejčastěji a nejdéle ze všech batohů, přesto se mu při výběru věnuje nejméně pozornosti. Do práce a do školy s ním chodíte každý den, často s notebookem, svačinou, lahví a bundou. Špatně zvolený model pak způsobí bolavá ramena, propocená záda nebo zničenou techniku, kterou sebou nosíte.</p>'
          '<p>Na Sportece najdete městské a sportovní batohy z českých obchodů vedle sebe. Pokud hledáte specializované řešení, podívejte se do příbuzných kategorií: <a href="/skolni-batohy/">školní batohy</a>, <a href="/turisticke-batohy/">turistické batohy</a> nebo <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>. U každého modelu vidíte dostupné barvy a nabídky více obchodů, takže si snadno ověříte, kde je váš oblíbený kus skladem a v jaké barvě.</p>',
    guide='<h2>Jaký typ městského batohu potřebujete</h2>'
          '<p>Městské batohy dnes pokrývají několik odlišných použití a jeden model je málokdy ideální pro všechna. Kdo jezdí s notebookem do kanceláře, potřebuje vyztužené záda a polstrovanou kapsu. Student chce prostor na sešity a svačinu, sportovec oddělenou přihrádku na boty nebo mokré oblečení. Kdo cestuje, ocení kapsy blízko zad a zapínání, které se neotevře za jízdy v tramvaji.</p>'
          + T(['Typ', 'Typické vlastnosti', 'Pro koho'], [
              ['Kancelářský', 'polstrovaná kapsa na notebook, organizér, čisté linie', 'dojíždění, práce, schůzky'],
              ['Univerzitní', 'velká hlavní kapsa, přední kapsy, odolný materiál', 'studenti a mladí lidé na cestách'],
              ['Sportovní', 'větrané záda, boční kapsy na lahev, přihrádka na obuv', 'cesta do posilovny nebo na trénink'],
              ['Rolltop', 'stahovací otvor, voděodolná tkanina', 'cyklisté a lidé v deštivém klimatu'],
              ['Malý denní', 'kompaktní tvar, málo oddílů', 'procházky, volný čas, festivaly'],
              ['Cestovní', 'rozevírání k zádům, skryté kapsy', 'cesty vlakem a letadlem']]) +
          '<h2>Objem: kolik litrů stačí</h2>'
          '<p>Objem se udává v litrech a určuje, kolik věcí se vejde dovnitř. Větší není lepší: prázdný velký batoh se hroutí a svádí k tomu, aby se do něj nacpalo víc, než je zdrávo. Správná velikost odpovídá tomu, co sebou skutečně nosíte. Pro každodenní dojíždění bývá většina lidí spokojena s objemem v rozmezí zhruba dvaceti až třiceti litrů.</p>'
          + T(['Objem', 'Co se obvykle vejde', 'Použití'], [
              ['do 15 l', 'peněženka, láhev, mikina, drobnosti', 'procházky, kapesní verze na festival'],
              ['15 až 25 l', 'tablet nebo malý notebook, svačina, oblečení navíc', 'škola, kancelář, krátké cesty'],
              ['25 až 35 l', 'notebook, sportovní vybavení, bunda, obědový box', 'dojíždění se sportem, víkendové výlety'],
              ['nad 35 l', 'oblečení na několik dní', 'cestování, spíše turistický batoh']]) +
          '<h2>Záda, popruhy a ergonomie</h2>'
          '<p>Pohodlí batohu rozhodují záda a ramenní popruhy. Polstrovaný zádový panel s vyvýšenými pásy odděluje batoh od zad a umožňuje proudění vzduchu, což oceníte v létě. Popruhy mají být široké, měkké a dostatečně dlouhé, aby batoh seděl na zádech a ne na kříži. Hrudní popruh stabilizuje zátěž při chůzi a běhu, bederní pás přenáší část váhy na boky u těžších zavazadel.</p>'
          '<p>Základní pravidlo zní: nejtěžší věci ukládejte blízko zad a nahoru do středu, lehké dopředu. Notebook patří do vyztužené kapsy u zad, láhev do boční kapsy. Při chůzi by se měl batoh pohybovat spolu s tělem, ne se houpat. Pokud jej nosíte na jednom rameni, zátěž se nerovnoměrně rozkládá a časem dělá potíže zádům, takže vždy používejte oba popruhy.</p>'
          '<h2>Materiály a odolnost</h2>'
          '<ul><li><strong>Polyester</strong> je lehký a levný na výrobu, snese běžné použití a dobře se čistí.</li>'
          '<li><strong>Nylon</strong> je pevnější v tahu a odolnější proti otěru, proto se používá u modelů do náročnějšího provozu.</li>'
          '<li><strong>Bavlněné plátno</strong> vypadá stylově, ale víc nasákne a po deštích dlouho schne.</li>'
          '<li><strong>Voděodolné povlaky</strong> zvládnou mrholení, ne dlouhý liják, a švy musí být zatmelené nebo zakryté.</li>'
          '<li><strong>Recyklované tkaniny</strong> jsou stále častější a svými vlastnostmi se blíží klasickým materiálům.</li></ul>'
          '<p>Důležité jsou zipy a švy, kde se většinou batoh nejdřív poškodí. Hrubší zipy s většími jezdci se lépe ovládají v rukavicích a míň se zadírají. Spodní díl bývá vyztužený proti otěru o zem.</p>'
          '<h2>Kapsy, organizace a bezpečnost</h2>'
          '<p>Dobře navržený batoh má logické rozdělení. Hlavní komora na větší věci, přední kapsa na doklady a drobnosti, boční kapsy na lahev nebo deštník a vnitřní oddíl pro techniku. Skrytá kapsa u zad na peněženku a telefon je v davu praktická, protože k ní nikdo nedosáhne bez vašeho vědomí. U cyklistických a městských batohů se hodí reflexní prvky a úchyt na světlo, jinak batoh v šeru splývá s okolím.</p>'
          '<p>Při cestování ve vlaku nebo letadle ocení lidé model, který se otevírá na plochu jako kufr. Naopak rolltop se hodí tam, kde potřebujete flexibilní objem a ochranu před vodou. Když svou techniku nosíte denně, hledejte batoh, který dno nezačne při položení na zem ihned propouštět vlhkost, a notebook v něm udržte v polstrované kapse oddělené od podlahy batohu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr mají ' + B(('fjallraven', 'Fjällräven'), ('deuter', 'Deuter'), ('adidas', 'Adidas'), ('vans', 'Vans'), ('the-north-face', 'The North Face'), ('nike', 'Nike'), ('jansport', 'Jansport'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('eastpak', 'Eastpak'), ('rains', 'Rains'), ('calvin-klein', 'Calvin Klein')) + '. Fjällräven je známý nadčasovým tvarem a pevným plátnem, Deuter ergonomickými zády a promyšleným rozložením zátěže. Jansport a Eastpak jsou tradiční značky studentských batohů. Adidas, Nike, Puma a Under Armour se zaměřují na sportovní styl a trénink, Rains na vodotěsné a minimalistické modely.</p>'
          '<h2>Jak batoh zkoušet</h2>'
          '<p>V obchodě nebo po doručení nasaďte batoh a naplňte ho tím, co běžně nosíte. Sledujte, kde batoh sedí vůči ramenům, zda popruhy netlačí na klíční kosti a zda se dno nedotýká beder. Projděte se po místnosti, předkloňte se a zhoupněte, abyste vyzkoušeli, jak se zátěž chová. Zkontrolujte, že se všechny zipy dobře ovládají a že lze nastavit délku popruhů.</p>'
          '<h2>Péče o batoh</h2>'
          '<p>Nejlepší péče je pravidelné vyklepání drobných nečistot a vysušení po dešti. Pokud se musí vyprat, použijte vlažnou vodu, jemný prostředek a měkký kartáč, nikdy nepoužívejte pračku s vysokými otáčkami, protože poškodí vyztužení a lepení. Batoh nechte vyschnout na vzduchu s otevřenými kapsami. Zip občas potřete svíčkou nebo speciálním přípravkem, aby se nezadíral.</p>'
          '<ul><li>Nenechávejte v batohu mokré oblečení přes noc, zapáchá a plesniví.</li>'
          '<li>Nepřetěžujte zip nejvíc zatíženého oddílu.</li>'
          '<li>Voděodolnou úpravu čas od času obnovte impregnací.</li>'
          '<li>Skladujte volně naplněný papírem nebo oblečením, aby si zachoval tvar.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<p>Chybou číslo jedna je koupě příliš velkého batohu. Prostor se vždy zaplní a ramena to odnesou. Chybou číslo dvě je ignorování zad: rovný a tvrdý panel bez ventilace v létě zaručí propocené tričko. Další častou chybou je vybírat jen podle designu, bez ohledu na kapsy a velikost, takže se pak notebook nevejde. A konečně se často podceňuje nutnost nosit oba popruhy, což dlouhodobě škodí držení těla.</p>'
          '<h2>Pro koho jaký batoh</h2>'
          '<p>Pro děti a mladší studenty je rozumné hledat v kategorii <a href="/skolni-batohy/">školních batohů</a> s pevnými zády a reflexními prvky. Pro vysokoškoláky a zaměstnance se hodí kancelářské modely s kapsou na notebook. Sportovci a návštěvníci posilovny ocení oddělenou přihrádku na obuv a mokré věci, často v kombinaci se <a href="/sportovni-tasky/">sportovní taškou</a>, pokud potřebují víc místa. Kdo rád nosí tašku na jednom rameni, může zvážit <a href="/tasky-pres-rameno/">tašky přes rameno</a>, které jsou praktičtější na krátké pochůzky bez těžkého nákladu.</p>'
          '<h2>Denní scénáře: co si zabalit</h2>'
          '<p>Batoh se používá nejlépe, když víte, co do něj patří. Pro kancelářský den bude stačit notebook v polstrované kapse, nabíječka v přední kapse, láhev v boční a tenká bunda nahoře. Na trénink po práci přibude sáček na obuv a ručník, což je dobré oddělit od elektroniky, aby vlhkost nepoškodila techniku. Pro školní den s vyšším počtem učebnic je důležité rozložit těžké knihy k zádům a pevně dotáhnout popruhy, jinak batoh táhne dozadu.</p>'
          '<ul><li><strong>Dojíždění vlakem:</strong> kapsa na jízdenku nebo kartu na dosah a zip, který nejde otevřít zvenčí.</li>'
          '<li><strong>Cesta na kole:</strong> stabilní tvar, který nehoupe, hrudní popruh a reflexní prvky.</li>'
          '<li><strong>Víkendový výlet městem:</strong> menší batoh se základní výbavou a vodou, který nezatěžuje.</li>'
          '<li><strong>Služební cesta:</strong> model s rozevíráním, který projde jako příruční zavazadlo, a kapsa na doklady.</li></ul>'
          '<p>Při každodenním používání je dobré batoh občas vyprázdnit a prohlédnout. V kapsách se drží drobky, zapomenuté účtenky a zbytky tekutin, které časem způsobí zápach nebo poškodí podšívku. Po vyprázdnění vyklepejte dno a otevřete všechny zipy, aby se vnitřek vysušil.</p>'
          '<h2>Pro kombinaci se sportem a cestou</h2>'
          '<p>Kdo kombinuje batoh s kolem, najde další doplňky v kategorii <a href="/cyklo-tasky-a-nosice/">cyklistických tašek a nosičů</a>, kde jsou brašny na nosič a rámové tašky. Pro lyžařské výlety existuje samostatná sekce <a href="/lyzarske-vaky-a-tasky/">lyžařských vaků a tašek</a>. Láhev nebo termosku do bočních kapes vyberete mezi <a href="/lahve-a-termosky/">lahvemi a termoskami</a>, které se liší průměrem i těsností.</p>'
          '<h2>Nákup na Sportece</h2>'
          '<p>Stejný batoh se může lišit dostupnými barvami a termínem doručení podle obchodu. Proto je výhodné porovnat nabídky vedle sebe a vybrat podle toho, co potřebujete. Před nákupem si ověřte rozměry a objem v litrech, nespoléhejte jen na označení velikosti. Pro delší pobyt v přírodě existuje samostatná kategorie <a href="/batohy/">batohů</a>, kde najdete i specializované řady.</p>',
    faq=[('Jak velký městský batoh vybrat?', 'Pro běžné dojíždění obvykle stačí přibližně dvacet až třicet litrů. Větší batoh svádí k přetěžování, menší nepojme notebook a oblečení navíc.'),
         ('Jak poznám, že se do batohu vejde notebook?', 'Podívejte se na rozměry polstrované kapsy a porovnejte je s úhlopříčkou svého notebooku. Počítejte i s tloušťkou a obalem.'),
         ('Musí mít městský batoh hrudní popruh?', 'Není povinný, ale při delší chůzi nebo jízdě na kole stabilizuje zátěž a odlehčuje ramena. U malých modelů se často vynechává.'),
         ('Jaký materiál je nejodolnější?', 'Nylon a hustě tkaný polyester jsou odolné proti otěru. Plátno je pevné, ale víc nasákne a déle schne.'),
         ('Je voděodolný batoh totéž co vodotěsný?', 'Ne. Voděodolný zvládne déšť a mrholení, vodotěsný má zatmelené švy a uzávěr, například rolltop, a chrání i při větší vodě.'),
         ('Jak nosit batoh, aby nebolela záda?', 'Oba popruhy dotažené tak, aby batoh seděl těsně u zad, těžké věci blízko zad a nahoru. Nenoste ho na jednom rameni.'),
         ('Hodí se městský batoh do posilovny?', 'Ano, pokud má oddělenou přihrádku na obuv nebo mokré věci a snadno se čistí. Pro větší vybavení je lepší sportovní taška.'),
         ('Jak batoh vyprat?', 'Ručně ve vlažné vodě s jemným prostředkem, bez pračky s vysokými otáčkami. Sušte na vzduchu s otevřenými kapsami, ne na topení.'),
         ('Jak zabránit kapesní krádeži z batohu v davu?', 'Používejte skrytou kapsu u zad pro cennosti a zipy zajišťujte. Do vnějších kapes nedávejte peněženku ani telefon.'),
         ('Kdy je batoh příliš těžký?', 'Pokud tlačí na ramena, tahá vás dozadu nebo způsobuje bolest zad, je těžký. Vyndejte, co nepotřebujete, a těžké věci přesuňte blíže k zádům.'),
         ('Jak poznám kvalitní zip na batohu?', 'Má větší a pevný jezdec, plynule se pohybuje a nezadírá se v rozích. Kvalitní zip se dobře ovládá i v rukavicích a vydrží opakované zatěžování.'),
         ('Mohu městský batoh použít i na výlet?', 'Na krátký výlet ano. Na delší túru je lepší turistický batoh s nosným systémem, protože městský nemá bederní pás ani dostatečně polstrovaná záda.')],
)

# ------------------------------------------------------------------ lyzarske-bundy
NEW['lyzarske-bundy'] = dict(long=True,
    title='Lyžařské a snowboardové bundy: výběr | Sporteka',
    desc='Lyžařské a snowboardové bundy: membrána, zateplení, střih a velikost. Průvodce výběrem pro svah i skialp, nabídky českých e-shopů na jednom místě.',
    intro='<p><strong>Lyžařská bunda</strong> musí zvládnout věc, kterou městská nedokáže: celodenní pobyt ve sněhu, větru a mrazu a k tomu intenzivní pohyb. Zdánlivě stačí hřát, ve skutečnosti ale musí také chránit před vodou, odvádět vlhkost, vydržet pády a nebránit pohybu. Rozdíl mezi dobrou a průměrnou bundou se projeví nejvíc na vleku a při čekání ve frontě.</p>'
          '<p>Na Sportece porovnáte nabídky lyžařských a snowboardových bund z českých obchodů. Pro kompletní výbavu navazují <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/lyzarske-kombinezy/">kombinézy</a> a <a href="/lyzarske-termopradlo/">termoprádlo</a>, pro ochranu hlavy a očí <a href="/lyzarske-helmy/">helmy</a> a <a href="/lyzarske-bryle/">brýle</a>. U každého modelu najdete dostupné velikosti a barvy, takže vybíráte rychle a bez obcházení obchodů.</p>',
    guide='<h2>Co dělá bundu lyžařskou</h2>'
          '<p>Od běžné zimní bundy se lyžařská liší konstrukcí. Má sněhovou sukni, která zabrání proniknutí sněhu při pádu, zapínání kapes na zip, prodloužená záda, kapuci přes helmu a manžety s úchytem na palec nebo kapsu na skipas. Švy bývají zatmelené, aby jimi neprosakovala voda, a rukávy střižené tak, aby při předklonu nevyjížděly. Tyto detaily dohromady rozhodují o tom, zda vám bude na svahu příjemně.</p>'
          + T(['Prvek', 'K čemu je', 'Na co si dát pozor'], [
              ['Membrána a tkanina', 'zadržuje vodu zvenčí, propouští páru', 'u deště a mokrého sněhu potřebujete vyšší odolnost'],
              ['Zateplení', 'udržuje teplo při stání', 'moc zateplená bunda se při jízdě přehřeje'],
              ['Sněhová sukně', 'brání vniknutí sněhu zespodu', 'musí jít zapnout na kalhoty nebo dotáhnout'],
              ['Kapuce', 'chrání při větru a sněžení', 'musí sednout přes helmu a nesmí omezovat výhled'],
              ['Větrací zipy', 'umožní odvětrání pod pažemi', 'měly by být zakryté chlopní'],
              ['Manžety', 'těsní kolem rukavic', 'případně i s palcovým otvorem']]) +
          '<h2>Zateplená, nebo skořepinová bunda</h2>'
          '<p>Zateplená bunda má izolaci přímo v sobě, takže ji oblečete jednou rukou a nemusíte řešit vrstvy. Hodí se pro ty, kdo ve sněhu tráví čas pomaleji, jezdí s dětmi nebo v chladnějších lokalitách. Slabinou je horší regulace: v jarním slunci se v ní snadno přehřejete. Skořepinová, anglicky shell, bunda je tenká vrchní vrstva s membránou bez izolace. Teplo řešíte vrstvením pod ní, takže ji využijete v mrazu i při jarním lyžování. Pro zkušenější lyžaře a freeridery bývá flexibilnější, vyžaduje ale dobře promyšlené podvrstvy.</p>'
          '<p>Třetí variantou jsou lehčí <a href="/softshellove-bundy/">softshellové bundy</a>, které se hodí pro <a href="/bezecke-lyzovani/">běžecké lyžování</a> a skialpinismus. Nejsou tak nepromokavé, ale lépe dýchají a lépe se v nich pohybuje. Na svah s vlekem byste měli volit spíše plnohodnotnou lyžařskou bundu.</p>'
          '<h2>Vrstvení pod bundou</h2>'
          '<p>Lyžování je střídání pohybu a stání, proto se tělo střídavě zahřívá a ochlazuje. Systém tří vrstev to řeší nejlépe. První vrstva na těle odvádí pot, například <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>. Druhá vrstva izoluje, nejčastěji fleece nebo lehká vesta. Třetí vrstvou je bunda, která zastaví vítr a vodu. Bavlněné tričko pod bundou je nejčastější chyba, protože zadržuje vlhkost a ochlazuje.</p>'
          + T(['Podmínky', 'Spodní vrstva', 'Střední vrstva', 'Bunda'], [
              ['jarní lyžování, slunce', 'tenké funkční triko', 'obvykle žádná', 'skořepinová nebo lehce zateplená'],
              ['běžný zimní den', 'termoprádlo', 'fleece', 'zateplená nebo skořepinová'],
              ['silný mráz a vítr', 'silnější termoprádlo', 'zateplená mikina nebo vesta', 'zateplená s kapucí'],
              ['čekání ve frontě, výuka dětí', 'termoprádlo', 'fleece', 'zateplená a delší střih']]) +
          '<h2>Lyže, snowboard a skialp</h2>'
          '<p>Snowboardisté vyhledávají volnější střih, delší rukávy a hlubší kapsy, protože při sedání a vstávání na svahu je oblečení víc v kontaktu se sněhem. Sjezdoví lyžaři preferují užší střih, který nevlaje v rychlosti. Kdo vyráží na <a href="/skialpove-lyze/">skialpové túry</a>, hledá lehké, stlačitelné bundy s dobrým odvětráním, protože při výstupu se tělo zahřívá a při sjezdu ochlazuje. Dětské bundy bývají vybaveny prodlužovacími rukávy a reflexními prvky, což oceníte i při rychlém dorůstání.</p>'
          '<p>Pro snowboardisty existují i kompletní řešení, například <a href="/snowboardove-sety/">snowboardové sety</a>, a pro rodiny s dětmi <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a>, které jsou jednodušší na oblékání a ochrání před sněhem celé tělo.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce jsou bundy značek ' + B(('rossignol', 'Rossignol'), ('dare2b', 'Dare2b'), ('trespass', 'Trespass'), ('helly-hansen', 'Helly Hansen'), ('kilpi', 'Kilpi'), ('o-neill', "O'Neill"), ('protest', 'Protest'), ('picture', 'Picture'), ('loap', 'Loap'), ('alpine-pro', 'Alpine Pro'), ('hannah', 'Hannah'), ('4f', '4F')) + '. Rossignol patří k lyžařským klasikám, Helly Hansen a Picture k technickému oblečení do náročných podmínek. O\'Neill, Protest a Picture cílí na snowboardový styl. Kilpi, Loap, Alpine Pro a Hannah jsou středoevropské značky zaměřené na praktické oblečení za dostupné ceny, Dare2b a Trespass nabízejí širokou škálu pro rodiny.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Lyžařská bunda má sedět s rezervou na středovou vrstvu, ale nesmí být tak velká, aby se pod ní hýbal vzduch. Zkontrolujte délku rukávů při zvednutých rukou, výšku límce a sukni, která má zakrýt pás. Zasunutá do kalhot nebo zapnutá na kalhoty zabrání vniknutí sněhu při pádu. Kapuce musí sedět přes helmu, což zjistíte jen s ní na hlavě, takže vyzkoušejte kombinaci v obchodě nebo si ověřte údaj výrobce.</p>'
          '<ul><li>U dětí počítejte jen s malou rezervou na růst, delší rukávy se dají podehnout.</li>'
          '<li>Dámské střihy jsou užší v pase a delší v zádech.</li>'
          '<li>Pánské střihy mají širší ramena a delší rukávy.</li>'
          '<li>Při nejistotě mezi dvěma velikostmi zvolte větší a doplňte stahováním.</li></ul>'
          '<h2>Kapsy a doplňky</h2>'
          '<p>Dobrá lyžařská bunda má kapsu na skipas na předloktí, vnitřní kapsu na telefon blízko těla, kde se lépe udrží baterie v mrazu, a kapsu na brýle s měkkou podšívkou. Kapsy na zip by měly mít velké jezdce, aby šly otevřít v rukavicích. Součástí výbavy jsou <a href="/lyzarske-rukavice/">lyžařské rukavice</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, které doplňují bundu v místech, kde uniká nejvíc tepla.</p>'
          '<h2>Kde uniká teplo</h2>'
          '<p>I dobrá bunda se může ocitnout v problému, pokud ji doplňují špatné detaily. Teplo nejvíc uniká krkem, zápěstím a pasem, proto sledujte, zda límec sahá do výšky brady, zda manžety těsní přes rukavice a zda se sukně dá dotáhnout. Kapuce s úpravou obvodu zlepší těsnost na hlavě. U modelů, které mají všechno, ale špatně sedí, je lepší zvolit o číslo jinou velikost než se smířit s vlajícími rukávy.</p>'
          '<h2>Péče a impregnace</h2>'
          '<p>Membrána funguje jen tehdy, když je čistá. Pot, krém na opalování a špína zalepují póry a snižují prodyšnost. Lyžařskou bundu perte podle štítku, na nízkou teplotu, s prostředkem určeným pro funkční textil, bez aviváže. Po vyprání obnovte povrchovou úpravu impregnačním sprejem nebo přípravkem do pračky. Při sušení respektujte pokyny výrobce, někdy pomáhá krátké zahřátí v sušičce, které povrchovou úpravu oživí.</p>'
          '<ul><li>Po sezóně bundu vyperte a skladujte volně zavěšenou.</li>'
          '<li>Mokrou bundu nenechávejte stlačenou v kufru nebo tašce.</li>'
          '<li>Zip čistěte měkkým kartáčkem a případně namažte.</li>'
          '<li>Drobné trhliny v tkanině opravte samolepicí záplatou, než se rozšíří.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je přehnaně silné zateplení: bunda je skvělá při čekání, ale při jízdě se v ní tělo přehřeje a pot ochladí. Druhou chybou je podcenění kapuce a sněhové sukně, bez nichž vám sníh pronikne za límec nebo do pasu. Třetí chybou je výběr podle barvy bez ohledu na viditelnost: na svahu se hodí výraznější barvy, protože usnadňují vzájemné nalezení ve skupině a v mlze.</p>'
          '<h2>Pro koho jaká bunda</h2>'
          '<p>Rekreační lyžař, který jezdí několik dní v sezóně, si vystačí s univerzální zateplenou bundou. Pro pravidelné jezdce na ledovci a ve vysokých horách je lepší skořepina s vrstvením. Rodiče s dětmi ocení odolnou tkaninu a výrazné barvy, které usnadní dohled. Zimní sportovci i mimo svah mohou zvážit též běžnou <a href="/zimni-bundy/">zimní bundu</a> pro každodenní nošení, a pro kompletní nabídku slouží kategorie <a href="/lyzarske-obleceni/">lyžařského a snowboardového oblečení</a>. K bundě patří i vhodné <a href="/lyzarske-boty/">lyžařské boty</a>, bez kterých je výbava neúplná.</p>'
          '<h2>Jak se bunda chová na svahu</h2>'
          '<p>Při sjezdu se tělo zahřívá rychleji, než čekáte, a po zastavení rychle vychladne. Proto se vyplatí mít bundu s odvětrávacími zipy pod pažemi, které otevřete při stoupání nebo na vleku v teplejším dni. Dobré větrání omezí potřebu bundu svlékat, a tím i riziko, že vám bude zima, když ji znovu oblékáte na větru. Na lanovce a vleku naopak oceníte vyšší límec a kapuci, protože vítr je tam nejsilnější.</p>'
          '<p>Při pádu vás chrání odolnější tkanina na ramenou, loktech a bocích. Některé modely mají v těchto místech zesílení. Pokud často jezdíte mimo upravené trasy, hledejte bundu s pevnějším materiálem a vnitřní kapsou na lavinový vyhledávač nebo jiné bezpečnostní vybavení. Pro jezdce mimo sjezdovku jsou důležité také prostorné kapsy na mapy a rukavice, které se vejdou i s tlustými prsty.</p>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Lyžařské bundy se prodávají v sezónních kolekcích, ale základní střihy se opakují několik let. Na Sportece proto můžete porovnat stejný model v několika obchodech a rozhodnout se podle skladové dostupnosti. Před nákupem si ověřte údaje o membráně, zateplení a kapuci, pak teprve barvu a značku. Při nákupu pro děti počítejte s růstem, ale ne s přemírou, protože příliš volná bunda funguje hůř.</p>',
    faq=[('Čím se lyžařská bunda liší od běžné zimní?', 'Má sněhovou sukni, kapuci přes helmu, zatmelené švy, kapsu na skipas a odolnější povrch. Je navržena pro pohyb a pády na svahu, ne pro městské nošení.'),
         ('Zateplená, nebo skořepinová bunda?', 'Zateplená je jednodušší a hodí se pro rekreační lyžování a rodiny. Skořepina je flexibilnější, protože teplo regulujete vrstvami pod ní.'),
         ('Jak se oblékat pod lyžařskou bundu?', 'Použijte termoprádlo, případně fleece nebo lehkou izolační vestu. Bavlněné tričko vyměňte za funkční, protože bavlna zadržuje vlhkost.'),
         ('Musí mít bunda sněhovou sukni?', 'Je výhodou. Sukně zabrání vniknutí sněhu při pádu a udržuje pas v teple, zvlášť pokud ji lze spojit s kalhotami.'),
         ('Jak poznám správnou velikost?', 'Podle tabulky výrobce a s rezervou na střední vrstvu. Při zvednutých rukou nesmí bunda vyjet nad pas a rukávy by neměly sklouznout k loktům.'),
         ('Musí kapuce sedět přes helmu?', 'Pokud jezdíte s helmou, ano. Kapuce přes helmu chrání před větrem a sněhem, ale při zkoušení ověřte, že neomezuje výhled a otáčení hlavy.'),
         ('Jak lyžařskou bundu vyprat?', 'Na nízkou teplotu s prostředkem na funkční textil, bez aviváže a bělidel. Po vyprání obnovte impregnaci podle pokynů výrobce.'),
         ('Hodí se lyžařská bunda na snowboard?', 'Ano, ale snowboardisté často preferují volnější střih a delší rukávy. Konstrukce s membránou a sněhovou sukní je pro obě disciplíny podobná.'),
         ('Co je lepší pro děti?', 'Odolná zateplená bunda s výraznou barvou, prodlužovacími rukávy a snadným zapínáním. Počítejte s rezervou na růst, ale ne s příliš velkou velikostí.'),
         ('Hodí se softshell na svah?', 'Na běžky a skialp ano, protože dýchá. Na sjezdovku s vlekem je lepší bunda s membránou, která zvládne vlhký sníh a zadrží vítr.'),
         ('Jak často lyžařskou bundu impregnovat?', 'Podle používání, obvykle po několika vyprání nebo když voda přestane stékat po povrchu a tkanina nasákne. Použijte přípravek určený pro funkční textil.'),
         ('Kdy lyžařskou bundu kupovat?', 'Největší výběr velikostí je na podzim, slevy přicházejí v průběhu sezóny. Základní střihy se opakují, takže starší kolekce často nic neztrácí.')],
)
