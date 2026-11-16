"""sporteka.cz — wave 28e (16. 11. 2026): long texts for turfy, mma-rukavice, tejpy, arginin-a-citrulin.
General true facts only, no prices, no product counts, no dosing advice. Taping: no medical promises, physiotherapist recommended.
Arginine and citrulline have no authorised EU health claim — said plainly. Brands with an indexed page (znacky.json):
adidas, puma, nike, joma, mizuno, skechers, gymbeam; other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ turfy
NEW['turfy'] = dict(long=True,
    title='Turfy: kopačky na umělou trávu a tvrdý povrch',
    desc='Turfy na umělou trávu, škváru i tvrdé hřiště. Čím se liší od kopaček FG, AG a sálovek, jak vybrat velikost a svršek a nabídky českých obchodů.',
    intro='<p>Turfy jsou fotbalová obuv s pryžovou podrážkou posetou spoustou nízkých výstupků. Místo několika vysokých kolíků mají desítky malých nopků, které rozloží tlak do celé plochy chodidla a drží na krátké umělé trávě, na tvrdém a suchém trávníku i na škváře. U výrobců je poznáte podle zkratky TF, Puma používá označení TT a Mizuno AS. Hrají v nich rekreační týmy na umělce, trenéři, děti na školním hřišti i hráči malé kopané. Pro mnoho hráčů jsou to vůbec první fotbalové boty, protože jedny turfy pokryjí většinu hřišť ve městě.</p>'
          '<p>Na Sportece porovnáte, za jakých podmínek turfy nabízejí české obchody, a nákup dokončíte na webu vybraného prodejce. Najdete tu modely ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('nike', 'Nike'), ('joma', 'Joma'), ('mizuno', 'Mizuno'), ('skechers', 'Skechers')) + ' a dalších značek. Patří do kategorie <a href="/kopacky/">kopačky</a>, vedle nich stojí <a href="/salova-obuv/">sálová obuv</a> pro halu.</p>',
    guide='<h2>Co přesně jsou turfy</h2>'
          '<p>Turfy vznikly pro hřiště, na kterých běžné kopačky nefungují dobře. Na tvrdém povrchu se vysoký kolík nezaboří, takže hráč stojí jen na několika bodech a snadno podklouzne. Tlak se navíc soustředí do malých ploch pod kolíky, což je na chodidle nepříjemně znát. Podrážka turfů funguje jinak: má mnoho krátkých výstupků z pryže, které se do povrchu nezapichují, ale drží ho třením, podobně jako běžecká bota na trailu. Proto v nich lze hrát i na hřištích, kde jsou kolíky nevhodné nebo zakázané.</p>'
          '<p>Slovo turf v angličtině znamená trávník a zkratka TF prostě odkazuje na umělou trávu. V češtině se ale ujalo jako název celé skupiny bot, a tak se běžně říká „koupit turfy“ nebo „hrát v turfech“.</p>'
          '<h2>Turfy, kopačky a sálovky: srovnání podrážek</h2>'
          + T(['Označení', 'Podrážka', 'Na jaký povrch'], [
              ['TF, TT, AS (turfy)', 'mnoho nízkých pryžových výstupků', 'krátká umělá tráva, tvrdý suchý trávník, škvára'],
              ['FG (firm ground)', 'pevné lisované kolíky', 'suchá přírodní tráva, podle výrobce i část umělých trávníků'],
              ['AG (artificial grass)', 'kratší a početnější kolíky, často duté', 'umělá tráva s delším vlasem a gumovým granulátem'],
              ['MG (multi ground)', 'kombinace kolíků vhodná na více povrchů', 'přírodní i umělá tráva'],
              ['SG (soft ground)', 'vyměnitelné kovové nebo kombinované kolíky', 'měkký a mokrý přírodní trávník'],
              ['IN, IC (sálovky)', 'plochá podrážka z nebarvící pryže', 'parkety, hala, futsal']]) +
          '<p>Na umělé trávě s dlouhým vlasem a granulátem, tedy na moderních hřištích třetí a čtvrté generace, drží nejlépe kopačky AG nebo FG, které výrobce pro umělou trávu výslovně uvádí. Turfy se tam dají použít také, při prudkých obratech ale kloužou víc. Na staré pískové umělce s krátkým vlasem, na škváře a na tvrdém hřišti jsou naopak turfy lepší volbou než kolíky. Některá hřiště mají vlastní pravidla, například zákaz kovových kolíků, a turfy obvykle projdou všude.</p>'
          '<h2>Kde turfy dávají smysl</h2>'
          '<ul><li><strong>Malá kopaná a hobby ligy:</strong> hraje se často na menších umělých hřištích, kde turfy stačí a nohu tolik neunaví.</li>'
          '<li><strong>Trénink na umělce v zimě:</strong> když je tráva zmrzlá a tvrdá, pryžové nopky drží lépe než kolíky.</li>'
          '<li><strong>Škola a sídliště:</strong> dítě si v jedněch botách zahraje na hřišti s tartanem, umělkou i na škváře.</li>'
          '<li><strong>Trenéři a rozhodčí:</strong> při chození po hřišti a předvádění cviků potřebují stabilitu, ne kolíky.</li>'
          '<li><strong>Doplněk ke kopačkám:</strong> mnoho hráčů má turfy na tréninky na umělce a kopačky FG na zápasy na trávě.</li></ul>'
          '<h2>Na co se dívat při výběru</h2>'
          '<h3>Svršek</h3>'
          '<p>Většina turfů má svršek ze syntetického materiálu, který je lehký, snadno se čistí a moc se nevytahuje. Pletené svršky obepnou nohu jako ponožka a dobře cítí míč, bývají ale méně odolné na drsném povrchu. Přírodní kůže se objevuje u klasických modelů: časem se přizpůsobí tvaru nohy a příjemně tlumí míč, potřebuje ale péči a po namočení pomalu schne. Na škváru a beton volte svršek se zesílenou špičkou, protože právě tam se boty odírají nejvíc.</p>'
          '<h3>Střih a řady modelů</h3>'
          '<p>Výrobci staví turfy na stejných řadách jako kopačky. U Adidasu jsou to například Predator, Copa nebo F50, u Nike Mercurial, Phantom a Tiempo, u Pumy Future, Ultra a King. Lehké rychlostní řady bývají užší a s tenkým svrškem, klasické řady jako Copa, Tiempo nebo King širší a s měkčím, často koženým nebo kůži připomínajícím materiálem. Joma a Mizuno mají v nabídce i modely se širším kopytem, které ocení hráči s plnější nohou.</p>'
          '<h3>Tkaničky, nebo suchý zip</h3>'
          '<p>Dětské turfy se často prodávají na suchý zip, aby si je dítě obulo samo. Pro starší děti a dospělé jsou lepší tkaničky, které botu přitáhnou k noze přesněji. Některé modely mají tkaničky schované pod jazykem nebo bezšněrovací svršek s pružným lemem kolem kotníku.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Turfy by měly sedět těsněji než běžné tenisky, aby noha v botě neklouzala při obratech. Mezi palcem a špičkou ale nechte zhruba půl centimetru až centimetr. Zkoušejte je odpoledne, kdy je noha nejvíc oteklá, a ve fotbalových ponožkách nebo <a href="/fotbalove-chranice-a-stulpny/">štulpnách</a>, ve kterých budete hrát. Syntetický svršek se skoro nevytahuje, takže bota, která v obchodě tlačí, bude tlačit i po měsíci. Kůže povolí o něco víc.</p>'
          '<p>Velikostní tabulky se mezi značkami liší a i v rámci jedné značky mají rychlostní řady jiný střih než klasické. Pokud kupujete na internetu, porovnejte délku chodidla v centimetrech s tabulkou konkrétního výrobce. Dětem kupujte turfy s malou rezervou, ne o dvě čísla větší; v příliš velké botě dítě klopýtá a podrážka se láme na špatném místě.</p>'
          '<h2>Odolnost a povrch</h2>'
          '<p>Pryžové nopky se na škváře a betonu obrušují rychleji než na umělé trávě. Kdo hraje převážně na tvrdém povrchu, by měl hledat podrážku z tvrdší pryže a se zesílenou špičkou. Gumový granulát z umělé trávy se dostane do bot i do ponožek, proto turfy po hře vyklepejte a nenechávejte je zavřené v tašce. Mokré boty sušte při pokojové teplotě s vycpávkou z novin, ne na topení, protože horko rozlepuje podrážku a deformuje svršek.</p>'
          '<h2>Turfy mimo hřiště</h2>'
          '<p>Díky ploché pryžové podrážce se v turfech dá i chodit, takže se z nich staly oblíbené boty na cestu na trénink nebo na sobotní procházku s míčem v parku. Na celodenní nošení ale nejsou stavěné: mají tenkou vložku, malé odpružení a nopky se na asfaltu rychle opotřebí. Na každodenní nošení se hodí spíš <a href="/tenisky/">tenisky</a>, na běh <a href="/bezecka-obuv/">běžecká obuv</a>.</p>'
          '<h2>Generace umělé trávy a co z toho plyne</h2>'
          '<p>Starší umělá hřiště, kterým se říká první a druhá generace, mají krátký a tuhý vlas zasypaný pískem. Povrch je tvrdý a klouzavý a turfy jsou na něm ideální. Novější hřiště třetí generace mají delší a měkčí vlas a mezi stébly gumový granulát, který napodobuje pružnost trávníku. Tady se pryžové nopky turfů neboří tak dobře a hráči, kteří hrají hodně a rychle, sáhnou spíš po kopačkách AG. Pokud nevíte, na jakém povrchu váš tým hraje, zeptejte se trenéra nebo správce hřiště, případně se podívejte, v čem hrají ostatní.</p>'
          '<h2>Ponožky, vložky a pohodlí</h2>'
          '<p>Podrážka turfů je plochá a tvrdší, takže na tvrdém hřišti se chodidlo unaví dřív než na trávě. Pomůže kvalitní fotbalová ponožka, případně ponožka s protiskluzovými prvky na chodidle, které drží nohu v botě na místě. Původní vložku lze vyměnit za měkčí, jen musí být stejně tenká, jinak bota začne tlačit na nártu. Kdo má citlivé paty, ocení model se zesílenou patní částí.</p>'
          '<h2>Dámské a dětské modely</h2>'
          '<p>Většina turfů je unisex a dámské verze se liší spíš barvou než střihem. Ženy s užší nohou proto často sáhnou po menších pánských nebo juniorských velikostech, které bývají užší. Juniorské řady kopírují modely dospělých, mívají ale jednodušší svršek a měkčí podrážku. U dětí, které rychle rostou, se vyplatí kontrolovat velikost aspoň dvakrát za sezonu.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Turfy koupené na moderní umělou trávu s dlouhým vlasem, kde by lépe držely kopačky AG.</li>'
          '<li>Sálovky místo turfů na venkovní hřiště; plochá podrážka na umělé trávě klouže.</li>'
          '<li>Výběr velikosti bez fotbalových ponožek.</li>'
          '<li>Pletený svršek pro hráče, který hraje hlavně na škváře.</li>'
          '<li>Sušení na topení, po kterém se podrážka odlepí.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě modelu se ukážou nabídky různých obchodů a velikosti, které mají skladem, a objednávku pak dokončíte u prodejce. Nejprve si ujasněte, na jakém povrchu budete nejčastěji hrát, potom vybírejte střih a svršek. K turfům se hodí <a href="/fotbalove-mice/">fotbalový míč</a> a <a href="/fotbalove-chranice-a-stulpny/">chrániče holení</a>, na halový fotbal <a href="/salova-obuv/">sálovky</a> a na zápasy na přírodní trávě klasické <a href="/kopacky/">kopačky</a>.</p>',
    faq=[
        ('Co znamená TF na kopačkách?', 'TF je zkratka anglického turf, tedy trávník. Označuje obuv s pryžovou podrážkou s mnoha nízkými výstupky pro krátkou umělou trávu a tvrdý povrch. Puma používá zkratku TT a Mizuno AS.'),
        ('Můžu hrát v turfech na moderní umělé trávě?', 'Můžete, ale na umělé trávě s dlouhým vlasem a granulátem obvykle lépe drží kopačky AG nebo FG určené pro umělý povrch. Turfy tam při prudkých obratech kloužou víc.'),
        ('Jaký je rozdíl mezi turfy a sálovkami?', 'Turfy mají pryžové nopky pro venkovní umělou trávu a tvrdé hřiště. Sálovky mají plochou nebarvící podrážku na parkety v hale. Na umělé trávě sálovky kloužou a turfy by v hale mohly odírat podlahu.'),
        ('Jsou turfy vhodné pro děti?', 'Ano, jsou mezi dětmi velmi oblíbené, protože zvládnou školní hřiště, umělku i škváru. Menším dětem se hodí zapínání na suchý zip, starším tkaničky.'),
        ('Mají turfy sedět těsně?', 'Těsněji než běžné tenisky, aby noha neklouzala, ale s rezervou zhruba půl až jeden centimetr u špičky. Zkoušejte je ve fotbalových ponožkách.'),
        ('Můžu turfy nosit i na běžnou chůzi?', 'Krátce ano, na celodenní nošení ale nejsou stavěné. Mají malé odpružení a nopky se na asfaltu rychle obrušují.'),
        ('Jak turfy čistit a sušit?', 'Vyklepejte z nich granulát a hlínu, umyjte je vlažnou vodou a kartáčkem a sušte při pokojové teplotě s vycpávkou z papíru. Topení a sušička mohou rozlepit podrážku.'),
    ])

# ------------------------------------------------------------------ mma-rukavice
NEW['mma-rukavice'] = dict(long=True,
    title='MMA rukavice: váha v oz, sparing, pytel a grappling',
    desc='MMA rukavice s otevřenými prsty na sparing, zápasy i práci na pytli. Co znamená 4 až 7 oz, jak vybrat velikost a čím se liší od boxerských.',
    intro='<p>MMA rukavice mají otevřené prsty a polstrování soustředěné nad klouby. Díky tomu se v nich dá udeřit i chytit soupeře, provést úchop, páku nebo se zapřít o žíněnku. Jsou výrazně lehčí a tenčí než boxerské rukavice, a proto se v nich jinak trénuje: chrání ruku i partnera méně, zato nebrání v zápasení. Kdo začíná se smíšenými bojovými umění, obvykle si pořídí jedny MMA rukavice na sparing a k nim boxerské na práci na pytli. Na co se zaměřit, závisí na tom, jestli budete víc zápasit, nebo boxovat.</p>'
          '<p>Sporteka ukazuje nabídky českých e-shopů k jednotlivým rukavicím, objednávku pak provedete přímo v obchodě. V kategorii najdete rukavice RDX, Venum, DBX Bushido, Lonsdale, Leone a dalších výrobců bojového vybavení. Nadřazenou kategorií jsou <a href="/boxerske-rukavice/">boxerské rukavice</a>, ostatní ochrana je v kategorii <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>.</p>',
    guide='<h2>Jak se MMA rukavice liší od boxerských</h2>'
          '<p>Boxerská rukavice obalí celou pěst, palec je přišitý k tělu rukavice a prsty jsou sevřené uvnitř. Váží obvykle od 8 do 16 oz a velká vrstva výplně tlumí úder do hlavy partnera i do pytle. MMA rukavice nechává prsty volné, dlaň je otevřená nebo jen slabě krytá a výplň je tenká. Ruka tak může chytat, svírat a zápasit. Za to se platí menší ochranou kloubů i partnera, a proto se v MMA rukavicích obvykle nesparuje stejnou silou jako v boxerských.</p>'
          '<h2>Co znamenají unce</h2>'
          '<p>Hmotnost rukavic se tradičně uvádí v uncích, zkratkou oz. Jedna unce je zhruba 28 gramů. U MMA rukavic se nejčastěji setkáte s rozsahem od 4 do 7 oz.</p>'
          + T(['Hmotnost', 'Typické použití', 'Poznámka'], [
              ['4 oz', 'zápasové rukavice, profesionální MMA', 'nejtenčí výplň, minimum ochrany při tréninku'],
              ['5 až 6 oz', 'trénink, lapy, lehčí sparing', 'kompromis mezi ochranou a volností prstů'],
              ['7 oz', 'sparingové MMA rukavice', 'silnější výplň nad klouby, někdy částečně krytý palec'],
              ['grapplingové a shooto rukavice', 'zápas na zemi, ground and pound na figurínu', 'tenké polstrování, otevřená dlaň']]) +
          '<p>Zápasové rukavice s váhou 4 oz se nosí v profesionálních zápasech a pro trénink se hodí jen omezeně. Sparingové modely kolem 7 oz mají silnější a delší výplň, která chrání klouby i obličej partnera. Amatérské soutěže mívají vlastní pravidla, někdy i seznam schválených modelů, proto si před zápasem ověřte požadavky pořadatele.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>MMA rukavice se prodávají ve velikostech S, M, L a XL, výrobci k nim uvádějí obvod dlaně nebo délku ruky v centimetrech. Obvod se měří kolem dlaně pod klouby, bez palce. Tabulky se mezi značkami liší, takže jedna velikost od RDX nemusí odpovídat stejné velikosti od Venumu. Rukavice by měla sedět pevně, prsty musí volně projít otvory a po sevření pěsti nesmí výplň sjíždět z kloubů. Počítejte i s tím, že pod rukavicí budete mít bandáž, která ruku trochu zvětší.</p>'
          '<h2>Bandáže pod rukavice</h2>'
          '<p>Bandáž zpevní zápěstí a drobné kůstky ruky a chrání klouby. Pod MMA rukavice se hodí kratší bandáže, protože v tenké rukavici není pro dlouhou bandáž místo a prsty musí zůstat volné. Někdo používá tenké vnitřní rukavice s gelovou výplní nad klouby, které se nasadí rychleji než klasická bandáž. Na zápasech se ruce obvykle bandážují gázou a páskou podle pravidel soutěže.</p>'
          '<h2>Materiál a zapínání</h2>'
          '<ul><li><strong>Přírodní kůže:</strong> odolná, časem se přizpůsobí ruce, potřebuje vysušení a občasnou péči.</li>'
          '<li><strong>Syntetická kůže:</strong> lehčí na údržbu a dostupnější, kvalita se mezi modely výrazně liší.</li>'
          '<li><strong>Výplň:</strong> vícevrstvá pěna, u některých modelů s gelovou vrstvou nad klouby.</li>'
          '<li><strong>Zapínání:</strong> široký suchý zip kolem zápěstí; delší pásek zápěstí lépe zpevní.</li>'
          '<li><strong>Prsty:</strong> elastické nebo prošité smyčky, u kterých záleží na tom, zda neškrtí při sevření.</li>'
          '<li><strong>Dlaň:</strong> plně otevřená pro grappling, nebo s tenkou vrstvou pro lepší ochranu.</li></ul>'
          '<h2>Trénink na pytli a lapách</h2>'
          '<p>Na pytel se MMA rukavice používají hlavně tehdy, když chcete trénovat kombinace úderů s úchopy nebo údery ze země na figurínu. Pro dlouhé série silných úderů do pytle jsou boxerské rukavice vhodnější, protože tenká výplň MMA rukavic tolik nechrání klouby a zápěstí. Pokud trénujete doma, podívejte se i na <a href="/boxovaci-pytle/">boxovací pytle</a>, ke kterým se boxerské i MMA rukavice dají kombinovat podle cviku.</p>'
          '<h2>Sparing a bezpečnost</h2>'
          '<p>Při sparingu v lehkých rukavicích dopadá úder na menší plochu a s menším tlumením. Proto se sparing v MMA rukavicích dělá obvykle v nižší intenzitě, s chráničem zubů, a pro údery do hlavy mnoho klubů volí rukavice 7 oz nebo sparuje postoj zvlášť v boxerských rukavicích. Dodržujte pravidla svého klubu a trenéra. Kromě rukavic patří k základní výbavě <a href="/chranice-bojove-sporty/">chránič zubů a suspenzor</a>, u začátečníků i chrániče holení.</p>'
          '<h2>Hygiena a péče</h2>'
          '<p>Rukavice nasáknou potem a v uzavřené tašce se v nich rychle množí bakterie, které způsobují zápach. Po tréninku je vyndejte, rozepněte suchý zip a nechte je vyschnout na vzduchu, ne na topení. Vnitřek můžete přetřít antibakteriálním sprejem určeným na sportovní vybavení. Rukavice nepůjčujte, zvlášť pokud má někdo na rukou odřeniny, a stejně tak nesdílejte bandáže. Kožené rukavice občas ošetřete přípravkem na kůži, aby nepraskaly.</p>'
          '<h2>Dětské MMA rukavice</h2>'
          '<p>Pro děti se vyrábějí menší modely, obvykle s větší výplní, protože dětské tréninky se zaměřují na techniku a bezpečnost, ne na tvrdé údery. Kluby pro děti často vyžadují konkrétní typ rukavic, proto se před nákupem zeptejte trenéra. U rostoucí ruky se vyplatí sledovat, jestli rukavice stále sedí a výplň zůstává nad klouby.</p>'
          '<h2>Kdo MMA rukavice používá</h2>'
          '<p>Nejen zápasníci smíšených bojových umění. Lehké rukavice s otevřenými prsty nosí lidé na kurzech sebeobrany a krav magy, kde se cvičí údery i úchopy, a také ti, kdo trénují kondiční box ve skupině a chtějí mít rukavice malé a rychle nasaditelné. Grappleři z brazilského jiu-jitsu nebo zápasu je občas berou na tréninky, kde se kombinuje zápas s údery. Pro každé z těchto použití se hodí jiná váha a výplň, proto si před nákupem ujasněte, co budete v rukavicích dělat nejčastěji.</p>'
          '<h2>Kdy rukavice vyměnit</h2>'
          '<p>Výplň se postupně stlačuje a po čase přestává tlumit tak, jak má. Poznáte to podle toho, že klouby při úderu cítíte víc než dřív, nebo že pěna nad klouby je znatelně tenčí a měkčí. Dalším signálem jsou roztržené švy kolem prstů, odpárané smyčky a suchý zip, který už nedrží. Ošoupaná kůže na dlani nevadí, poškozená výplň nad klouby ano. Rukavice, které už nechrání, nepoužívejte na sparing, protože ohrožujete partnera i vlastní ruce.</p>'
          '<h2>Tréninková figurína a ground and pound</h2>'
          '<p>Pro trénink úderů ze země se používají zápasnické figuríny nebo pytle položené na žíněnce. Tady mají MMA rukavice smysl, protože umožňují figurínu chytit, převrátit a zároveň udeřit. Údery do figuríny jdou často šikmo a v nepřirozeném úhlu, takže zápěstí pracuje víc než při úderu ve stoje. Pevná bandáž a dobře utažený suchý zip jsou při tomto tréninku důležitější než obvykle.</p>'
          '<h2>Barva a vzhled</h2>'
          '<p>Výrobci jako Venum nebo RDX nabízejí stejný model v mnoha barvách a s různými potisky. Funkci to nemění, v klubu ale pomůže, když si své rukavice snadno poznáte v hromadě na lavičce. Světlé rukavice na sobě dřív ukážou špínu a pot, tmavé vypadají déle jako nové. Některé kluby a soutěže předepisují barvu rukou podle rohu, ve kterém zápasník nastupuje, takže na zápas můžete potřebovat červené nebo modré rukavice.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Zápasové 4oz rukavice pro začátečníka na sparing.</li>'
          '<li>Výběr velikosti bez ohledu na bandáž, kterou budete nosit pod rukavicí.</li>'
          '<li>Trénink silových sérií na pytli jen v MMA rukavicích.</li>'
          '<li>Rukavice ponechané po tréninku vlhké v tašce.</li>'
          '<li>Nákup bez ověření, jaké rukavice vyžaduje klub nebo soutěž.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě rukavic vidíte nabídky více obchodů i dostupné velikosti a nákup pak uzavřete v e-shopu, který vyberete. Nejdřív si ujasněte, zda rukavice potřebujete na sparing, na grappling, nebo na zápas, a podle toho volte váhu. K tréninku se hodí <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a>, pro zápas v kimonu <a href="/kimona/">kimona</a> a celou nabídku najdete v kategorii <a href="/bojove-sporty/">bojové sporty</a>.</p>',
    faq=[
        ('Jakou váhu MMA rukavic zvolit?', 'Na trénink a sparing se nejčastěji volí 6 až 7 oz, protože mají silnější výplň. Rukavice 4 oz jsou zápasové a chrání méně. Grapplingové modely s tenkou výplní se hodí hlavně na zápas na zemi.'),
        ('Mohu v MMA rukavicích trénovat na pytli?', 'Krátce a na kombinace s úchopy ano. Na dlouhé série silných úderů jsou lepší boxerské rukavice, které klouby a zápěstí chrání víc.'),
        ('Jak zjistím svou velikost?', 'Změřte obvod dlaně pod klouby bez palce a porovnejte ho s tabulkou konkrétního výrobce. Počítejte s bandáží pod rukavicí. Rukavice má sedět pevně a výplň nesmí sjíždět z kloubů.'),
        ('Potřebuji pod MMA rukavice bandáže?', 'Bandáž zpevní zápěstí a chrání klouby. Pod MMA rukavice se hodí kratší bandáže nebo tenké vnitřní rukavice, aby zůstaly prsty volné.'),
        ('Jaký je rozdíl mezi MMA a grapplingovými rukavicemi?', 'Grapplingové rukavice mají tenčí výplň a otevřenou dlaň, takže se v nich lépe zápasí na zemi. Klasické MMA rukavice mají víc polstrování nad klouby na údery.'),
        ('Jsou kožené rukavice lepší než syntetické?', 'Kůže bývá odolnější a přizpůsobí se ruce, potřebuje ale péči. Kvalitní syntetika je lehčí na údržbu. Rozhoduje spíš zpracování, výplň a střih než samotný materiál.'),
        ('Jak poznám, že rukavice potřebuji vyměnit?', 'Když klouby při úderu cítíte víc než dřív, výplň nad nimi je znatelně tenčí nebo jsou roztržené švy a suchý zip přestává držet. Opotřebené rukavice na sparing nepoužívejte, ohrožujete sebe i partnera.'),
        ('Jak odstranit zápach z rukavic?', 'Po každém tréninku je vyndejte z tašky, rozepněte a nechte vyschnout na vzduchu. Pomůže antibakteriální sprej na sportovní vybavení. Na topení je nesušte.'),
    ])

# ------------------------------------------------------------------ tejpy
NEW['tejpy'] = dict(long=True,
    title='Tejpy a kineziologické pásky: kinesio i tuhý tejp',
    desc='Kineziologické tejpy, tuhé sportovní tejpy, podtejpovací pásky i předstřižené aplikace. Rozdíly, šířky, základy lepení a nabídky obchodů.',
    intro='<p>Tejpy jsou lepicí pásky, které se nalepují přímo na kůži. Pod tímto slovem se ale skrývají dvě odlišné věci. Kineziologický tejp, často nazývaný kinesio tejp, je pružný a barevný a pohyb neomezuje. Tuhý sportovní tejp je naopak nepružný, bílý a používá se tam, kde má kloub zůstat zpevněný, třeba kotník při volejbalu nebo prsty při lezení. Kromě rolí se prodávají předstřižené aplikace na konkrétní místa, podtejpovací pěnové pásky a nůžky. Než začnete tejpovat sami, nechte si techniku ukázat od fyzioterapeuta.</p>'
          '<p>Nabídky českých obchodů najdete na Sportece pohromadě a koupi dokončíte v e-shopu, který si zvolíte. Zastoupené jsou značky Temtex, Kinesio, Yate, Rehabiq, Sedco, ' + B(('gymbeam', 'GymBeam')) + ' nebo lezecký Beal. Tejpy patří do kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, souvisí s nimi také <a href="/prvni-pomoc/">první pomoc</a> a <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>',
    guide='<h2>Kineziologický, nebo tuhý tejp?</h2>'
          + T(['Vlastnost', 'Kineziologický tejp', 'Tuhý sportovní tejp'], [
              ['Pružnost', 'pruží podélně, podobně jako kůže', 'nepružný'],
              ['Účel', 'nalepí se a nechá kloubu volnost pohybu', 'zpevní kloub a omezí jeho pohyb'],
              ['Doba nošení', 'obvykle několik dní, i při sprchování', 'jen po dobu tréninku nebo zápasu'],
              ['Typická šířka', '5 cm, dále 2,5, 7,5 a 10 cm', '2,5 až 5 cm, trhá se rukou'],
              ['Kdo ho lepí', 'fyzioterapeut, po zaškolení i sportovec sám', 'fyzioterapeut, trenér nebo zkušený sportovec']]) +
          '<h2>Kineziologický tejp</h2>'
          '<p>Kineziologický tejp vznikl v Japonsku v sedmdesátých letech minulého století a jeho autorem je Kenzo Kase. Širší veřejnost si ho všimla hlavně díky vrcholovým sportovcům, kteří s barevnými pruhy na ramenou a lýtkách nastupovali na velkých soutěžích. Páska je obvykle z bavlny s příměsí elastanu, novější varianty jsou ze syntetických vláken. Lepidlo na akrylátové bázi je nanesené ve vlnkách, aby kůže pod tejpem mohla dýchat a pot se odpařoval.</p>'
          '<p>Tejp se dá podélně natáhnout a vrátí se zpět, podobně jako pokožka. Míra natažení se při lepení mění podle techniky. Fyzioterapeuti ho používají jako doplněk terapie, sportovci kvůli pocitu opory při pohybu. Je férové říct, že výsledky vědeckých studií o účinku kineziologického tejpování jsou nejednotné a tejp sám nic neléčí. Pokud vás něco bolí, začněte návštěvou lékaře nebo fyzioterapeuta, který zjistí příčinu a případně vám ukáže, jak tejp nalepit.</p>'
          '<h3>Bavlna, nebo syntetika</h3>'
          '<p>Bavlněné tejpy dobře dýchají a jsou příjemné na kůži, ve vodě a při silném pocení ale drží o něco hůř. Syntetické tejpy z nylonu nebo polyesteru bývají odolnější vůči vodě a hodí se plavcům, triatlonistům nebo na dlouhé běhy v horku. Barva na funkci nemá vliv, je to jen otázka vkusu; tělové odstíny jsou méně nápadné, černá a výrazné barvy jsou typické pro sport.</p>'
          '<h3>Role a předstřižené tejpy</h3>'
          '<p>Nejběžnější role mají šířku 5 cm a délku 5 m, fyzioterapeuti kupují dlouhé role kolem 30 m. Předstřižené aplikace mají tvar připravený na konkrétní místo, například na koleno, rameno nebo achilovku, a stačí sejmout krycí papír. Jsou dražší na jedno použití, ale ušetří stříhání a zaoblování rohů a pro začátečníka jsou jednodušší.</p>'
          '<h2>Tuhý sportovní tejp</h2>'
          '<p>Tuhý tejp je obvykle bavlněná páska s lepidlem na bázi oxidu zinečnatého nebo s jiným pevným lepidlem. Nepruží, a proto kloub skutečně zpevní a omezí v pohybu. Typicky se jím tejpují kotníky ve volejbale, basketbale a v míčových sportech, zápěstí ve vzpírání nebo prsty ve volejbale a při lezení. Trhá se rukou, takže lepení jde rychle i v šatně. Pod tuhý tejp se často dává tenká pěnová podtejpovací páska, která chrání kůži a chloupky.</p>'
          '<p>Tuhý tejp se lepí jen na dobu výkonu a po tréninku se sundává. Pokud kloub zpevňujete opakovaně, nechte si techniku ukázat od fyzioterapeuta: příliš utažený tejp může zhoršit prokrvení a špatně vedené pruhy kloub nezpevní tam, kde je potřeba.</p>'
          '<h2>Další pásky v kategorii</h2>'
          '<ul><li><strong>Podtejpovací páska (underwrap):</strong> tenká pěna pod tuhý tejp, chrání kůži.</li>'
          '<li><strong>Elastický lepicí obvaz:</strong> pruží jen částečně, používá se k fixaci a kompresi.</li>'
          '<li><strong>Samofixační kohezivní obinadlo:</strong> lepí samo na sebe, ne na kůži, hodí se k fixaci obvazu.</li>'
          '<li><strong>Lezecký tejp:</strong> úzký pevný tejp, například od Bealu, chrání prsty a hřbet ruky při lezení spár.</li>'
          '<li><strong>Nůžky na tejp a odstraňovač lepidla:</strong> drobnosti, které práci výrazně usnadní.</li></ul>'
          '<p>Hokejové pásky na čepel hokejky a na štulpny jsou jiný výrobek a najdete je v kategorii <a href="/hokejove-pasky-a-doplnky/">hokejové pásky a doplňky</a>.</p>'
          '<h2>Základy lepení kineziologického tejpu</h2>'
          '<ol><li>Kůže musí být čistá, suchá a bez krému. Hustší chloupky je lepší předem oholit, tejp pak drží lépe a sundání méně bolí.</li>'
          '<li>Pásku nastříhejte na potřebnou délku a rohy zaoblete nůžkami. Ostré rohy se zachytávají o oblečení a odlepují se.</li>'
          '<li>Začátek a konec tejpu, takzvané kotvy, lepte bez natažení, jinak se budou odlepovat a mohou dráždit kůži.</li>'
          '<li>Po nalepení tejp několikrát přejeďte dlaní. Lepidlo se aktivuje teplem a lépe přilne.</li>'
          '<li>Nalepte ho s předstihem před sportem nebo sprchou, výrobci obvykle uvádějí zhruba půl hodiny až hodinu.</li>'
          '<li>Mokrý tejp nesušte fénem na horký vzduch, stačí ho opatrně vysušit ručníkem.</li></ol>'
          '<p>Tejp sundávejte pomalu, ve směru růstu chloupků, a kůži přitom přidržujte. Pokud drží pevně, nejdřív ho namočte nebo potřete olejem. Při svědění, pálení nebo zarudnutí ho okamžitě sundejte. Tejp nelepte na rány, popáleniny, podrážděnou kůži ani na místa s kožním onemocněním. Lidé s citlivou pokožkou mohou nejdřív vyzkoušet malý proužek na malé ploše.</p>'
          '<h2>Tejpování achilovky a tejp na rameno</h2>'
          '<p>Achilovka a rameno patří k místům, kde lidé tejpy hledají nejčastěji. U achilovky se pásky obvykle vedou od paty po lýtku, u ramene kolem kloubu a přes lopatku. Konkrétní tvar a míru natažení ale volí fyzioterapeut podle toho, co vás trápí, protože bolest achilovky i ramene může mít různé příčiny. Návody z videí jsou dobrá inspirace, nenahradí však vyšetření. Pokud bolest trvá, zhoršuje se nebo vás omezuje v běžném pohybu, tejp neodkládejte k lékaři až na později.</p>'
          '<p>Pro opakované lepení stejné aplikace se hodí předstřižené tejpy na achilovku nebo rameno. Fyzioterapeut vám může ukázat, jak si je nalepit sami, a pak už je jen měníte podle potřeby.</p>'
          '<h2>Tejpy v různých sportech</h2>'
          '<p>Volejbalisté si tuhým tejpem zpevňují prsty, často dva sousední prsty k sobě, a kotníky před zápasem. Lezci chrání kůži na hřbetu ruky a na prstech úzkým pevným tejpem, který snese tření o skálu. Běžci a triatlonisté sahají spíš po kineziologických tejpech na koleno, lýtko nebo achilovku, protože jim nevadí v pohybu a vydrží i pot. Vzpěrači a crossfiteři tejpují palce a zápěstí, aby si nezraňovali kůži o osu. Hokejisté a florbalisté pak používají vlastní typy pásek na hokejky a štulpny.</p>'
          '<h2>Tejp, nebo ortéza</h2>'
          '<p>Tuhý tejp a ortéza dělají podobnou práci: zpevní kloub. Tejp je tenčí a lépe sedí v botě, při každém nasazení ho ale musíte znovu lepit a jednou použitý se vyhazuje. Ortéza se nasadí za pár vteřin a dá se použít opakovaně, je ale objemnější. Mnoho sportovců má doma obojí: ortézu na trénink, tejp na zápas. Výběr mezi nimi proberte s fyzioterapeutem, zvlášť po zranění.</p>'
          '<h2>Citlivá kůže a skladování</h2>'
          '<p>Akrylátové lepidlo snáší většina lidí dobře, u citlivé pokožky se ale může objevit zarudnutí nebo svědění. Zkuste nejprve malý kousek na méně exponovaném místě a sledujte reakci do druhého dne. Tejpy skladujte při pokojové teplotě, mimo přímé slunce a v původním obalu. V horku lepidlo měkne a role se může slepit, v chladu naopak hůř drží na kůži. Načatou roli uložte do sáčku, aby se okraje nezaprášily.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Lepení na kůži namazanou krémem nebo zpocenou.</li>'
          '<li>Natažené kotvy na začátku a konci tejpu.</li>'
          '<li>Ostré rohy, které se zachytávají o oblečení.</li>'
          '<li>Tuhý tejp nechaný na kotníku přes noc.</li>'
          '<li>Spoléhání na tejp místo vyšetření dlouhodobé bolesti.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě tejpu najdete nabídky více obchodů vedle sebe, takže porovnáte šířku, délku role i dopravu; objednávka pak proběhne v e-shopu. Nejprve se rozhodněte mezi pružným a tuhým tejpem, pak mezi rolí a předstřiženou aplikací. Pro zpevnění kloubu, které se dá nasadit a sundat, se podívejte na <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, na regeneraci na <a href="/kompresni-ponozky/">kompresní ponožky</a> a pro lezce na kategorii <a href="/horolezectvi/">horolezectví</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi kinesio tejpem a tuhým tejpem?', 'Kineziologický tejp je pružný, pohyb neomezuje a dá se nosit několik dní. Tuhý tejp je nepružný, kloub zpevní a omezí v pohybu a lepí se jen na dobu tréninku nebo zápasu.'),
        ('Jak dlouho vydrží kineziologický tejp na těle?', 'Výrobci obvykle uvádějí několik dní, často tři až pět. Záleží na kůži, pocení a na tom, jak pečlivě byl nalepený. Při svědění nebo zarudnutí ho sundejte dřív.'),
        ('Funguje kineziologické tejpování?', 'Výsledky vědeckých studií jsou nejednotné a tejp sám nic neléčí. Fyzioterapeuti ho používají jako doplněk terapie. Při bolesti se nejdřív poraďte s lékařem nebo fyzioterapeutem.'),
        ('Jak natejpovat achilovku?', 'Pásky se obvykle vedou od paty po lýtku, konkrétní tvar a natažení ale určuje fyzioterapeut podle příčiny potíží. Pro opakované lepení se hodí předstřižené tejpy na achilovku.'),
        ('Záleží na barvě tejpu?', 'Ne, barva funkci neovlivňuje. Volba mezi tělovou, černou nebo výraznou barvou je jen otázka vkusu.'),
        ('Mohu se s tejpem sprchovat a plavat?', 'Kineziologický tejp sprchu vydrží, pokud byl nalepený s předstihem. Do vody se hodí spíš syntetické tejpy, které drží lépe než bavlněné. Po koupání ho vysušte ručníkem.'),
        ('Jak tejp sundat, aby to nebolelo?', 'Pomalu, ve směru růstu chloupků, a kůži přitom přidržujte. Pevně držící tejp nejdřív namočte nebo potřete olejem.'),
        ('Mohu tejp nalepit na podrážděnou kůži?', 'Ne. Tejp nelepte na rány, popáleniny, podrážděnou kůži ani na místa s kožním onemocněním. Při svědění nebo pálení ho okamžitě sundejte.'),
        ('Co je podtejpovací páska?', 'Tenká pěnová páska, která se dává pod tuhý tejp. Chrání kůži a chloupky a usnadní sundání tejpu.'),
    ])

# ------------------------------------------------------------------ arginin-a-citrulin
NEW['arginin-a-citrulin'] = dict(long=True,
    title='Arginin a citrulin: AAKG, citrulin malát a formy',
    desc='L-arginin, AAKG, L-citrulin a citrulin malát v prášku i kapslích. Formy, poměry na etiketě, co o nich víme bez přikrášlení a nabídky obchodů.',
    intro='<p>Arginin a citrulin jsou aminokyseliny, které se ve sportovní výživě objevují samostatně i jako součást předtréninkových směsí. L-arginin je běžnou součástí bílkovin v potravě a tělo si ho umí částečně vyrobit samo. L-citrulin se v bílkovinách nevyskytuje a jméno má podle melounu, latinsky Citrullus, ze kterého byl poprvé izolován. V těle se citrulin mění na arginin. Hned na začátku je potřeba říct: pro arginin ani pro citrulin nemá Evropská unie schválené žádné zdravotní tvrzení. Text níže proto popisuje formy a etikety, ne sliby účinku.</p>'
          '<p>Na Sportece najdete nabídky českých obchodů pohromadě, objednáváte pak v e-shopu, který si vyberete. V kategorii jsou čisté prášky, kapsle a tablety i kombinované přípravky od značek Amix, BioTech USA, OstroVit, Prom-In, ' + B(('gymbeam', 'GymBeam')) + ', Nutrend nebo ATP Nutrition. Nadřazenou kategorií jsou <a href="/aminokyseliny-bcaa/">aminokyseliny a BCAA</a>, souvisí s ní <a href="/predtreninkove-boostery/">předtréninkové boostery</a>.</p>',
    guide='<h2>Co jsou arginin a citrulin</h2>'
          '<p>L-arginin patří mezi aminokyseliny, které se označují jako podmíněně esenciální. Zdravý dospělý si ho vyrobí dost, v některých situacích, například v období rychlého růstu, ho ale tělo potřebuje víc, než si vytvoří. V jídle je obsažen v bílkovinách: v mase, rybách, mléčných výrobcích, luštěninách, ořeších a semínkách, například v dýňových semínkách nebo arašídech. V těle slouží mimo jiné jako výchozí látka pro tvorbu oxidu dusnatého a močoviny.</p>'
          '<p>L-citrulin vzniká v těle jako meziprodukt močovinového cyklu a v ledvinách se přeměňuje zpět na arginin. Z potravin ho obsahuje nejvíc vodní meloun, zejména bílá část pod slupkou. Protože část argininu přijatého ústy se rozloží už ve střevě a v játrech, zkoumá se citrulin jako způsob, jak hladinu argininu v krvi zvýšit oklikou. Některé studie skutečně ukazují, že citrulin hladinu argininu v krvi zvyšuje spolehlivěji než arginin sám. To ale ještě neznamená žádný konkrétní přínos pro výkon nebo zdraví.</p>'
          '<h2>Žádné schválené tvrzení</h2>'
          '<p>Evropský úřad pro bezpečnost potravin posuzoval u argininu řadu žádostí o zdravotní tvrzení, mimo jiné o rozšiřování cév, tvorbě růstového hormonu nebo o fyzické výkonnosti. V žádném případě nepovažoval souvislost za dostatečně prokázanou a Evropská komise žádné tvrzení pro arginin neschválila. Pro citrulin ani citrulin malát schválené tvrzení také neexistuje.</p>'
          '<p>V praxi to znamená, že výrobce nesmí na obalu tvrdit, že arginin nebo citrulin zlepšuje výkon, prokrvení svalů, regeneraci nebo potenci. Pojmy jako „pumpa“ nebo „NO booster“ v názvu výrobku jsou marketingové označení, ne ověřený účinek. Pokud kombinovaný přípravek nějaké schválené tvrzení nese, týká se jiné složky, typicky vitamínu nebo minerálu, a smí ho použít jen při dostatečném obsahu této složky.</p>'
          '<h2>Formy v nabídce</h2>'
          + T(['Forma', 'Co to je', 'Na co se dívat'], [
              ['L-arginin (báze)', 'čistá aminokyselina', 'výrazně zásaditá, hořkosladká chuť'],
              ['Arginin hydrochlorid (HCl)', 'arginin ve formě soli s kyselinou chlorovodíkovou', 'obsah čistého argininu je nižší než hmotnost soli'],
              ['AAKG', 'arginin alfa-ketoglutarát, arginin vázaný na kyselinu alfa-ketoglutarovou', 'poměr 1:1 nebo 2:1, arginin tvoří jen část hmotnosti'],
              ['L-citrulin', 'čistá aminokyselina', 'neutrálnější chuť, menší porce prášku'],
              ['Citrulin malát', 'citrulin spojený s kyselinou jablečnou', 'poměr 2:1 znamená asi dvě třetiny citrulinu, 1:1 polovinu'],
              ['Kombinace', 'arginin a citrulin v předtréninkových směsích', 'kofein, beta-alanin, kreatin a další složky']]) +
          '<h2>Jak číst etiketu</h2>'
          '<p>U solí a sloučenin se vyplatí přepočet. Když obal uvádí 3 g citrulin malátu 2:1, obsahuje porce zhruba 2 g citrulinu, zbytek tvoří kyselina jablečná. U AAKG výrobci uvádějí poměr 1:1 nebo 2:1, a v obou případech tvoří arginin jen část hmotnosti. Proto porovnávejte výrobky podle obsahu účinné látky na porci, ne podle hmotnosti celé sloučeniny nebo čísla v názvu.</p>'
          '<ul><li><strong>Množství na porci:</strong> v gramech nebo miligramech, ideálně s přepočtem na čistou látku.</li>'
          '<li><strong>Velikost porce:</strong> počet kapslí nebo odměrek; u kapslí jich bývá na porci několik.</li>'
          '<li><strong>Poměr u citrulin malátu a AAKG:</strong> 2:1, nebo 1:1.</li>'
          '<li><strong>Příchuť a sladidla:</strong> neochucené prášky jsou kyselé nebo hořké, ochucené obsahují sladidla a aroma.</li>'
          '<li><strong>Další složky:</strong> kofein, beta-alanin, kreatin, dusičnany z červené řepy a rostlinné extrakty.</li>'
          '<li><strong>Doporučené dávkování:</strong> velikost porce a maximální denní množství určuje výrobce, nepřekračujte je.</li></ul>'
          '<h2>Prášek, nebo kapsle</h2>'
          '<p>Prášek vychází na porci obvykle výhodněji, neochucený citrulin malát je ale výrazně kyselý a arginin báze má nepříjemnou zásaditou chuť. Proto se často míchá do ochuceného nápoje nebo do předtréninkové směsi. Kapsle a tablety chuť obejdou, jen jich na jednu porci bývá potřeba víc, protože se do jedné kapsle vejde omezené množství. U ochucených prášků zkontrolujte sladidla a barviva.</p>'
          '<h2>Samostatně, nebo v předtréninkovce</h2>'
          '<p>Mnoho lidí se s citrulinem a argininem setká nejdřív v <a href="/predtreninkove-boostery/">předtréninkovém boosteru</a>. Množství jednotlivých látek ve směsi bývá ale různé a výrobci je u „proprietárních směsí“ nemusí uvádět jednotlivě. Samostatný prášek nebo kapsle dávají větší přehled o tom, co a kolik přijímáte. Pokud užíváte kombinovaný přípravek, nezapomeňte, že obsahuje i další látky, zejména kofein, jehož celkový denní příjem včetně kávy a energetických nápojů je dobré hlídat.</p>'
          '<h2>Arginin a citrulin v jídle</h2>'
          '<p>Kdo jí dostatek bílkovin, přijímá arginin běžně z jídla. Nejbohatšími zdroji jsou ořechy a semínka, luštěniny, maso, ryby a mléčné výrobky. Citrulin obsahuje hlavně vodní meloun a další tykvovité rostliny, v menší míře i okurka. Z jídla ale nikdy nedostanete takové množství jako z koncentrovaného doplňku, a proto u doplňků platí opatrnost a respekt k etiketě.</p>'
          '<h2>Kdy dát pozor</h2>'
          '<p>Vyšší množství argininu i citrulinu může způsobit zažívací potíže, například nadýmání nebo průjem. Arginin může ovlivnit krevní tlak a působit spolu s některými léky. Lidé, kteří užívají léky na krevní tlak, nitráty na srdce, léky na erektilní dysfunkci nebo na ředění krve, by ho neměli užívat bez porady s lékařem. Totéž platí pro lidi s nízkým tlakem, onemocněním srdce, ledvin nebo jater, pro těhotné a kojící ženy a pro děti. Kdo užívá jakékoli léky nebo má chronické onemocnění, ať se před užíváním poradí s lékařem nebo lékárníkem.</p>'
          '<h2>Dusičnany z řepy: jiná látka</h2>'
          '<p>V předtréninkových směsích se vedle argininu a citrulinu často objevuje extrakt z červené řepy nebo dusičnan draselný a sodný. Jde o jinou skupinu látek, dusičnany, které se zkoumají ze stejného důvodu jako arginin, tedy kvůli tvorbě oxidu dusnatého. Na etiketě je proto hledejte zvlášť a nepočítejte je k obsahu argininu. Ani u nich neberte názvy jako „pump“ nebo „vascular“ jako záruku účinku.</p>'
          '<h2>Vegani a vegetariáni</h2>'
          '<p>Arginin i citrulin pro doplňky se dnes vyrábějí převážně fermentací pomocí mikroorganismů, ne z živočišných surovin. Prášek je tak obvykle vhodný i pro vegany, u kapslí ale zkontrolujte, zda obal není želatinový. Vegetariáni a vegani přijímají arginin běžně z luštěnin, ořechů a semínek, takže jejich strava ho obsahuje dost.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Čisté aminokyseliny v prášku přitahují vlhkost, citrulin malát zvlášť. Dózu proto zavírejte hned po nabrání, odměrku používejte suchou a balení neskladujte v koupelně ani v kuchyni u varné konvice. Spečený prášek se dá rozdrolit, ale je to znamení, že se k němu dostala vlhkost. U velkých balení si spočítejte, zda je stihnete spotřebovat před datem minimální trvanlivosti.</p>'
          '<h2>Kvalita a soutěžní sport</h2>'
          '<p>Arginin ani citrulin nejsou na seznamu látek zakázaných Světovou antidopingovou agenturou. U doplňků stravy ale vždy existuje riziko, že výrobek bude obsahovat nečistoty nebo nepřiznané látky, zejména u kombinovaných předtréninkových směsí. Soutěžící sportovci by proto měli volit výrobky testované nezávislou laboratoří, například s certifikací Informed Sport nebo uvedené na Kölnské listině.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Porovnávání výrobků podle hmotnosti sloučeniny místo obsahu čistého argininu nebo citrulinu.</li>'
          '<li>Očekávání účinku, který žádné schválené tvrzení nepotvrzuje.</li>'
          '<li>Přehlédnutý kofein v kombinovaném přípravku.</li>'
          '<li>Užívání bez porady s lékařem při léčbě krevního tlaku nebo srdce.</li>'
          '<li>Neochucený citrulin malát koupený bez představy, jak kyselý je.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu porovnáte nabídky několika obchodů a velikosti balení, objednávka pak proběhne přímo v e-shopu. Nejprve se rozhodněte mezi argininem, citrulinem a kombinovaným přípravkem, pak mezi práškem a kapslemi. Prášky skladujte v suchu a dobře uzavřené, protože vlhkost je spéká. Další doplňky najdete v kategoriích <a href="/kreatin/">kreatin</a>, <a href="/glutamin/">glutamin</a> a <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>',
    faq=[
        ('Má arginin nebo citrulin schválené zdravotní tvrzení?', 'Ne. Evropský úřad pro bezpečnost potravin posuzoval u argininu několik žádostí, například o rozšiřování cév nebo výkonnosti, a souvislost nepovažoval za prokázanou. Pro citrulin ani citrulin malát schválené tvrzení také není.'),
        ('Jaký je rozdíl mezi argininem a citrulinem?', 'Arginin je součástí bílkovin v jídle. Citrulin se v bílkovinách nevyskytuje a v těle, hlavně v ledvinách, se mění na arginin. Některé studie ukazují, že citrulin zvyšuje hladinu argininu v krvi spolehlivěji než arginin sám.'),
        ('Co znamená citrulin malát 2:1?', 'Že na dva díly citrulinu připadá jeden díl kyseliny jablečné. Citrulin tak tvoří zhruba dvě třetiny hmotnosti. U poměru 1:1 tvoří polovinu.'),
        ('Co je AAKG?', 'Arginin alfa-ketoglutarát, tedy arginin vázaný na kyselinu alfa-ketoglutarovou. Arginin tvoří jen část hmotnosti, proto porovnávejte obsah čistého argininu na porci.'),
        ('Kolik argininu nebo citrulinu užívat?', 'Velikost porce a maximální denní množství stanoví výrobce na etiketě a nemělo by se překračovat. Při užívání léků nebo zdravotních potížích se poraďte s lékařem.'),
        ('Kdo by neměl arginin užívat bez porady s lékařem?', 'Lidé, kteří berou léky na tlak, nitráty, léky na erektilní dysfunkci nebo na ředění krve, lidé s nízkým tlakem, onemocněním srdce, ledvin nebo jater, těhotné a kojící ženy a děti.'),
        ('Jsou arginin a citrulin dopingem?', 'Nejsou na seznamu zakázaných látek Světové antidopingové agentury. Soutěžící by přesto měli volit výrobky testované nezávislou laboratoří, protože doplňky mohou obsahovat nepřiznané látky.'),
        ('Je lepší prášek, nebo kapsle?', 'Prášek vychází na porci obvykle výhodněji, ale neochucený je kyselý nebo hořký. Kapsle chuť obejdou, jen jich na porci bývá víc.'),
    ])
