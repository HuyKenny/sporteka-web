"""sporteka.cz — facet landing texts wave 101: damsky-batoh, kopacky-nike, nike-teplaky, nike-mikina.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ damsky-batoh
NEW['damsky-batoh'] = dict(
    title='Dámský batoh: střih, objem a výběr podle použití',
    desc='Dámský batoh se užším ramenním popruhem, kratšími zády a tvarovaným pasem. Jak vybrat objem a styl pro město, školu i túru a porovnat obchody.',
    intro='<p>Dámský batoh se od unisex modelu liší hlavně tím, jak sedí na užších ramenech a kratším trupu. Popruhy bývají užší a více prohnuté, záda kratší a bederní pás tvarovaný na boky místo na rovný pas. U malého městského batůžku to ladíte spíš vzhledem, u batohu na několikadenní túru je střih rozdílem mezi pohodlnou nocí a bolavými rameny. '
          'Na této stránce jsou batohy z kategorie <a href="/batohy/">batohy</a> určené ženám a dívkám, od lehkých městských modelů přes školní a sportovní kousky až po nosné systémy pro trek. Průvodce vysvětluje, v čem je ženský střih opravdu jiný, jak změřit délku zad, jak zvolit objem podle plánu a které detaily u městského batohu nejvíc ovlivní pohodlí. Další výběry najdete v <a href="/mestske-batohy/">městských</a>, <a href="/turisticke-batohy/">turistických</a> a <a href="/skolni-batohy/">školních batozích</a>.</p>',
    guide='<h2>V čem je dámský batoh opravdu jiný</h2>'
          '<p>Ženy jsou v průměru menší než muži, mají užší ramena, kratší trup a výraznější přechod mezi pasem a boky. Většina unisex batohů je přitom stavěná na střední mužskou postavu. Když na ženě sedí takový batoh špatně, popruhy se jí zařezávají do podpaží nebo sklouzávají z ramen a bederní pás leží na žebrech místo na kyčlích. Dámská řada tyto rozdíly opravuje několika konkrétními úpravami.</p>'
          + T(['Část batohu', 'Dámská úprava', 'Proč na tom záleží'], [
              ['Ramenní popruhy', 'užší, více prohnuté, nasazené blíž k sobě', 'nesklouzávají ze štíhlých ramen a netlačí na prsa ani podpaží'],
              ['Délka zad', 'kratší nosný systém, často menší rozsah nastavení', 'váha spočine na kyčlích, ne na bedrech'],
              ['Bederní pás', 'kratší, kónický, s měkčím tvarem po bocích', 'obepne boky místo rovného pasu'],
              ['Objem a váha', 'o něco nižší celková hmotnost prázdného batohu', 'menší tělo unese menší absolutní zátěž'],
              ['Barvy a detaily', 'širší paleta, často lehčí látky', 'jde o vzhled, nikoli o nosnost']]) +
          '<p>Tyto úpravy se nejvíc projeví u batohů nad dvacet pět litrů. U malého denního batůžku se rozdíl omezí na kratší popruhy a tvar zad, takže pokud vám sedí unisex model, nemusíte se omezovat jen na dámské řady. Opačně platí totéž: štíhlejší muž nebo větší dívka může být spokojenější v modelu označeném jako dámský. Označení je vodítko, ne pravidlo.</p>'
          '<h2>Jak změřit délku zad a sednout si do batohu</h2>'
          '<p>U turistických a cestovních batohů rozhoduje délka zad, nikoli celková výška. Měří se od výrazného krčního obratle na přechodu krku a ramen k hornímu okraji kyčelní kosti, kterou nahmatáte po stranách pasu. Jako pomocníka si vezměte metr a druhou osobu. Číslo si pak vyhledejte v tabulce konkrétní značky; označení S, M a L totiž nemá jednotný význam.</p>'
          '<ul><li><strong>Nejprve naložte, potom dotahujte:</strong> batoh vždy zkoušejte s alespoň několika kilogramy zátěže, prázdný působí vždy lépe.</li>'
          '<li><strong>Bederní pás na kyčle:</strong> okraj pásu by měl být přibližně na úrovni kyčelních hřebenů a nést většinu váhy.</li>'
          '<li><strong>Popruhy na ramenou:</strong> přiléhají bez mezer, konce nemají končit u podpaží.</li>'
          '<li><strong>Zátěžové popruhy:</strong> malé popruhy nad rameny batoh přitahují k tělu, ale nemají nést váhu místo pasu.</li>'
          '<li><strong>Hrudní popruh:</strong> upněte jej ve výšce ramen, jinak se popruhy rozjíždějí na stranu.</li></ul>'
          '<p>Značky Deuter a Osprey označují dámské verze svých turistických batohů zvláštní řadou a v popisu najdete zkratky nebo názvy sérií, které tuto úpravu naznačují. Hledejte například slova jako SL, women nebo dámský. Podrobnější průvodce nosnými systémy je v kategorii <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h2>Objem podle toho, kam jdete</h2>'
          '<p>Nepřeceňujte velikost. Batoh, který je příliš velký, se zaplní zbytečnostmi a váha zatěžuje záda. Příliš malý zase nutí připevňovat věci zvenku a narušuje rozložení hmotnosti. Pro orientaci poslouží následující přehled.</p>'
          + T(['Účel', 'Objem', 'Na co se zaměřit'], [
              ['Kabelka na každý den, město', 'kolem 10–18 l', 'organizér, zip proti krádeži, tvar, který nebolí v rameni'],
              ['Škola, univerzita, notebook', '18–28 l', 'polstrovaná kapsa na notebook, vyztužená záda'],
              ['Fitness, plavání, tanec', '20–30 l', 'oddělená kapsa na mokré věci a boty'],
              ['Jednodenní výlet', '20–32 l', 'prodyšná záda, boční kapsy na lahev, pláštěnka'],
              ['Víkendová túra', '35–45 l', 'bederní pás, nastavení zad, přístup do hlavní komory'],
              ['Dlouhý trek', '45–60 l', 'plný nosný systém ve správné velikosti, dobrá ventilace'],
              ['Příruční zavazadlo v letadle', 'podle rozměrů dopravce', 'změřte batoh naplněný a ověřte limit konkrétní linky']]) +
          '<p>Chcete-li pokrýt víc situací jedním kouskem, zvolte střední velikost kolem dvaceti pěti litrů s pevnými zády. Pro cestu je pak praktičtější odepínací malý batůžek, který se použije jako taška na výlet.</p>'
          '<h2>Městský dámský batoh: na co se dívat</h2>'
          '<p>V městském provozu rozhoduje pohodlí na dojíždění a jednoduchost. Ze všech nosných prvků je nejdůležitější vyztužení zad, aby se batoh nedeformoval a neztlačoval se do páteře. Další je tvarovaná polstrovaná záda s ventilací, která v tramvaji nebo v létě omezuje pocení. Mezi značkami v nabídce se objevují sportovní firmy jako ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('vans', 'Vans')) + ', outdoorové ' + B(('deuter', 'Deuter'), ('the-north-face', 'The North Face'), ('osprey', 'Osprey'), ('loap', 'Loap'), ('vuch', 'Vuch')) + ' i módní domy jako ' + B(('calvin-klein', 'Calvin Klein'), ('tommy-hilfiger', 'Tommy Hilfiger'), ('guess', 'Guess')) + '.</p>'
          '<ul><li><strong>Kapsa na notebook:</strong> měkce vystlaná a umístěná u zad, ne u vnější strany.</li>'
          '<li><strong>Zip a otevírání:</strong> kapsy na zip vedené k zádům proti kapesním krádežím, hlavní komora s dostatečně širokým otvorem.</li>'
          '<li><strong>Materiál:</strong> polyester nebo nylon snáší déšť, kožený batoh vypadá reprezentativně, ale hůř snáší vodu.</li>'
          '<li><strong>Hrudní popruh a madlo:</strong> madlo se hodí při zavěšení v šatně, hrudní popruh při jízdě na kole.</li>'
          '<li><strong>Vzhled:</strong> jednobarevný batoh se lépe kombinuje, výrazný se zase rychle najde na stojanu a v šatně.</li></ul>'
          '<p>Chcete-li batoh na ruku i na záda, vyberte model s odnímatelnými popruhy. Pro práci s notebookem je praktický i klasický tvar s horním otevřením a vnější kapsou na dokumenty. Pokud potřebujete nejtmavší a nejuniverzálnější variantu, najdete ji ve výběru <a href="/cerny-batoh/">černý batoh</a>.</p>'
          '<h2>Školní batoh pro dívky a studentky</h2>'
          '<p>Školní batoh pro dívku musí především unést učebnice a nezatěžovat záda. Pro mladší děti platí zásada, že plný batoh by neměl vážit víc než zhruba desetinu tělesné hmotnosti. Pro starší školačky a studentky je nejdůležitější pevná zadní stěna, nastavitelné popruhy a vnitřní členění na sešity, penál a lahev. Dívčí modely obvykle mají užší ramenní popruhy a menší celkový profil. Podrobnější rady najdete v kategorii <a href="/skolni-batohy/">školní batohy</a> a ve výběrech značek <a href="/baagl-batoh/">Baagl</a> a <a href="/oxybag-batoh/">Oxybag</a>.</p>'
          '<h2>Turistický a sportovní dámský batoh</h2>'
          '<p>Při chůzi ve volném terénu přenáší většinu váhy bederní pás, který ženám nesmí klouzat nahoru k žebrům. Proto je důležité vyzkoušet velikost pásu a při nákupu na dálku se řídit tabulkou obvodu pasu a boků. U delších tras je potřeba ocenit ventilaci zad: napnutá síť nad nosnou deskou vytváří vzduchovou mezeru, zatímco přiléhavý polstr hřeje a hůř odvádí pot. Pro rychlý běh a trailové tréninky slouží odlehčené vesty z kategorie <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>.</p>'
          '<p>Na výlety se vyplatí vybrat model s vnějším držákem na lahev, protože vytahování lahve z hlavní komory za chůze je nepraktické. Podstatné jsou i oddělená spodní komora na spací pytel a pláštěnka, často ukrytá v samostatné kapse. Z menších značek nabízejí české a evropské sportovní obchody modely ' + B(('tatonka', 'Tatonka'), ('ferrino', 'Ferrino'), ('gregory', 'Gregory'), ('lowe-alpine', 'Lowe Alpine'), ('montane', 'Montane')) + '. Obecné srovnání značek najdete na stránkách <a href="/osprey-batoh/">Osprey</a>, <a href="/deuter-batohy/">Deuter</a>, <a href="/vuch-batoh/">Vuch</a> a <a href="/the-north-face-batoh/">The North Face</a>.</p>'
          '<h2>Jak nastavit a nosit batoh, aby nebolelo</h2>'
          '<ol><li>Povolte všechny popruhy a naložte nejtěžší věci blízko zad a nahoře uprostřed.</li>'
          '<li>Nasaďte batoh a zapněte nejprve bederní pás, aby seděl na kyčlích.</li>'
          '<li>Dotáhněte ramenní popruhy tak, aby batoh přilnul k zádům, ale nezvedal se z pasu.</li>'
          '<li>Zapněte hrudní popruh a upravte jej do výšky těsně pod klíčními kostmi.</li>'
          '<li>Po půl hodině chůze zkontrolujte tlakové body a popruhy znovu přizpůsobte.</li></ol>'
          '<p>Častou chybou je batoh nosit na jednom rameni. U menších městských modelů je to okamžitě pohodlné, ale dlouhodobě zatěžuje jednu stranu trupu. Pokud to děláte pravidelně, střídejte strany nebo přejděte na batoh s oběma popruhy.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Batohy z technických tkanin čistěte vlhkým hadříkem a jemným mýdlem, v pračce je zbytečně ničíte. Před uložením je vždy vysušte rozevřené, jinak v nich zůstane vlhkost a zápach. Pokud máte batoh s membránou nebo voděodolnou úpravou, obnovte ji impregnací po sezóně. Zipy občas očistěte kartáčkem a promažte, aby nevázly. Pokud na batohu vidíte nadměrné roztřepení švů, zasáhněte brzy, než se rozpárá celá kapsa.</p>'
          '<h2>Jak hledat v nabídce</h2>'
          '<p>Při srovnávání ověřujte u každé nabídky objem v litrech, rozměry a hmotnost, ne jen fotografii. Stejně vypadající batohy mohou mít odlišné zadní panely i počet komor. Ke komplexnímu vybavení se hodí <a href="/sportovni-tasky/">sportovní tašky</a>, a pokud chcete praktickou chladicí variantu pro výlet, najdete ji u modelů s izolovanou kapsou. Když se vám dámský střih nelíbí, srovnejte jej s výběrem <a href="/pansky-batoh/">pánský batoh</a> a zkuste menší velikost.</p>',
    faq=[
        ('Čím se dámský batoh liší od unisex modelu?', 'Má užší a více prohnuté ramenní popruhy, kratší zádovou část a kónický bederní pás, který se přizpůsobí bokům. U malých městských batohů je rozdíl hlavně v popruzích, u turistických se projeví v nosném systému. Rozhoduje také hmotnost prázdného batohu, která u dámských řad bývá o něco nižší.'),
        ('Jak poznám správnou délku zad?', 'Změřte vzdálenost od krčního obratle na přechodu krku a ramen k úrovni horního okraje kyčelních kostí. Hodnotu v centimetrech porovnejte s tabulkou výrobce, protože velikosti S, M a L se mezi značkami liší. Ideální je batoh vyzkoušet s alespoň několika kilogramy zátěže.'),
        ('Jaký objem zvolit do města a na školu?', 'Pro každodenní dojíždění stačí zhruba patnáct až dvacet pět litrů. Pokud nosíte notebook a učebnice, sáhněte po objemu kolem dvaceti pěti až osmadvaceti litrů s vyztuženými zády. Příliš velký batoh se plní zbytečnostmi a zbytečně zatěžuje páteř.'),
        ('Hodí se mi i pánský batoh?', 'Ano, pokud vám sedí popruhy a délka zad. Štíhlejší postava se v unisex nebo pánském modelu cítí často pohodlně, zejména u menších objemů. U turistických batohů je ale lepší dámský střih, protože bederní pás a rozteč popruhů jsou přizpůsobeny ženské postavě.'),
        ('Jak dlouho vydrží dámský batoh?', 'Záleží na materiálu, nošení a zatížení. Kvalitní nylonový nebo polyesterový batoh vydrží několik let při pravidelné péči, zatímco levnější model s tenkými švy se častěji roztřepí. Zkontrolujte šití u popruhů, kvalitu zipů a výztuž na místech, kde se batoh nejvíc namáhá.'),
        ('Dá se dámský batoh prát v pračce?', 'Spíše ne. Pračka poškozuje pěnové výztuže, lepené spoje i impregnaci. Použijte vlhký hadřík, jemný saponát a kartáček, pak batoh nechte vyschnout rozevřený. Pokud výrobce praní výslovně dovoluje, použijte jemný program bez ždímání.'),
        ('Co zkontrolovat u batohu, který bere na palubu letadla?', 'Zjistěte maximální rozměry příručního zavazadla u konkrétního dopravce a změřte batoh naplněný. Prázdný batoh bývá menší, než je pak v zaplněném stavu. Nízkonákladové společnosti mívají přísnější limity než klasické aerolinky, ověřte je před odletem.'),
        ('Jaká barva je nejpraktičtější?', 'Černá a tmavě šedá skryjí otěr a drobné skvrny, proto se hodí do města. Světlé odstíny jsou v terénu viditelnější a v šeru bezpečnější. Žádná barva neovlivní nosnost, takže vybírejte hlavně podle střihu a objemu.'),
        ('Jak se vyhnout bolesti zad při nošení batohu?', 'Zátěž nahoře blízko zad, upevněný bederní pás na kyčlích a popruhy dotažené tak, aby se batoh nehoupal. Nenoste ho na jednom rameni a nepřetěžujte. Při opakovaných bolestech zkontrolujte, zda velikost nosného systému odpovídá délce vašich zad, případně se poraďte s lékařem.'),
    ])

# ------------------------------------------------------------------ kopacky-nike
NEW['kopacky-nike'] = dict(
    title='Kopačky Nike: Mercurial, Phantom, Tiempo a Premier',
    desc='Kopačky Nike řad Mercurial, Phantom, Tiempo a Premier. Jak se liší, jak vybrat povrch FG, MG, TF či IC, úroveň Elite až Club a dětskou velikost.',
    intro='<p>Kopačky Nike se dělí do několika řad podle toho, jaký typ hráče mají podpořit. Mercurial je řada pro rychlé hráče a krajní útočníky, Phantom pro kontrolu míče a přihrávky, Tiempo navazuje na klasickou kopačku s prvotřídním kontaktem a Premier připomíná ručně šitou starší školu. '
          'Na této stránce jsou kopačky této značky z kategorie <a href="/kopacky/">kopačky</a>, od dětských modelů po vrcholové verze. Průvodce vysvětluje, v čem se jednotlivé řady liší, jak číst označení úrovně od Club po Elite, jak správně zvolit podrážku pro trávu, umělku nebo halu a jak vybrat velikost pro rostoucího hráče. Chcete-li srovnat s jinými značkami, otevřete <a href="/kopacky-adidas/">kopačky Adidas</a>, <a href="/kopacky-puma/">kopačky Puma</a> nebo <a href="/detske-kopacky/">dětské kopačky</a>.</p>',
    guide='<h2>Čtyři řady Nike a pro koho jsou</h2>'
          '<p>Značka dlouhodobě staví své kopačky kolem několika pojmenovaných řad. Jména řad se v nabídce opakují a nové ročníky se objevují s číslem generace, například Mercurial Vapor nebo Superfly, Phantom GX a Phantom 6, Tiempo Legend 10 nebo Premier. Čísla označují pořadí vydání, nikoliv velikost. Starší ročníky bývají v obchodech často v nabídce za zvýhodněných podmínek, i když se tvar a materiál od nejnovějších modelů mírně liší.</p>'
          + T(['Řada', 'Charakter', 'Hodí se pro'], [
              ['Mercurial (Vapor, Superfly)', 'úzká, lehká, přiléhavá kopačka pro rychlost', 'křídla, útočníci, hráči s důrazem na běh a driblink'],
              ['Phantom', 'strukturovaný svršek pro kontakt s míčem', 'záložníci, tvůrci hry, přihrávky a střelba'],
              ['Tiempo (Legend, Ligera)', 'klasičtější střih, měkký materiál, pohodlí', 'obránci, záložníci, hráči s širším chodidlem'],
              ['Premier', 'retro vzhled a jemný dotek, jednodušší linie', 'hráči, kteří preferují hladký kontakt a tradici']]) +
          '<p>V praxi se rozdíl pozná už při navlékání. Mercurial sedí těsně kolem nártu a špičky, což vyhovuje štíhlým chodidlům. Tiempo a Premier mají větší vnitřní objem a pohodlnější příjezd, proto je volí hráči s širším nártem. Phantom leží někde mezi nimi. Žádná řada není pro některý post povinná, jde o osobní preferenci a tvar nohy.</p>'
          '<h2>Úrovně Elite, Pro, Academy a Club</h2>'
          '<p>Stejná řada se nabízí v několika kvalitativních úrovních a přípona v názvu říká, o kterou jde. Nejvyšší Elite používají profesionálové a mají nejlehčí a nejcitlivější svršek. Pro je zjednodušená verze se stejným designem, Academy je určená pro trénink a ambiciózní amatéry a Club pro rekreační hráče a děti. Čím nižší úroveň, tím odolnější a těžší bývá materiál a tím méně zásadní jsou technické detaily.</p>'
          '<ul><li><strong>Elite:</strong> nejlehčí svršek, nejcitlivější dotek, vyšší nároky na péči.</li>'
          '<li><strong>Pro:</strong> blízko elitní verzi, mírně jednodušší materiály.</li>'
          '<li><strong>Academy:</strong> velmi dobrý poměr výkonu a výdrže, často zvolená volba pro ligové kluby mládeže.</li>'
          '<li><strong>Club:</strong> odolná základní kopačka, ideální pro začátečníky a pro děti, které rychle rostou.</li></ul>'
          '<p>Většina hráčů z amatérských lig si vystačí s úrovní Academy, protože rozdíl proti vrcholové kopačce se projeví hlavně při velmi vysoké intenzitě. Dětem v růstu se víc vyplatí robustní Club než nejdražší model, který za sezónu překonají velikostí.</p>'
          '<h2>Povrch: FG, MG, TF a hala</h2>'
          '<p>Označení v názvu kopaček Nike určuje podrážku. FG je pro přírodní trávu, MG kombinuje kolíky pro přírodní i umělý povrch, TF má drobné nopy pro umělku a tvrdší hřiště, IC patří do haly. Kombinace jako FG/MG se v nabídce vyskytují často, protože takové kopačky pokryjí trávu i většinu umělých ploch. Ve všech případech platí, že kolíky patří jen na povrch, pro který jsou určené. Rozbor všech zkratek je v kategorii <a href="/kopacky/">kopačky</a>.</p>'
          + T(['Označení', 'Povrch', 'Poznámka'], [
              ['FG', 'přírodní tráva', 'pevné kolíky, nejčastější volba na zápasy'],
              ['MG', 'přírodní i umělá tráva', 'kompromis pro hráče, kteří střídají povrchy'],
              ['FG/MG', 'tráva i většina umělek', 'univerzální kopačka pro rekreační hráče a mládež'],
              ['TF', 'umělka, tvrdé a suché hřiště', 'krátké nopy, lehčí na klouby'],
              ['IC', 'hala, parkety, sportovní podlaha', 'plochá podrážka bez kolíků']]) +
          '<p>Častá chyba je koupě vrcholového modelu FG pro hru na umělce. Kolíky se v umělé hmotě zaklesnou a zatěžují koleno. Jestli hrajete obě varianty stejně často, začněte s FG/MG a halovou obuv doplňte zvlášť. Pro halu je lepší uvažovat o samostatných <a href="/sportovni-obuv/">sportovních botách</a> než o kopačkách s přerušenou podrážkou.</p>'
          '<h2>Nike a svršek: jak sedí a jak se nosí</h2>'
          '<p>Nike používá u fotbalových kopaček syntetické materiály, často s pleteným nebo texturovaným povrchem. Vysoký svršek s ponožkovým tvarem, který má kolem kotníku nástavec, drží nohu pevně, ale hůře se navléká. Nižší klasický střih je pohodlnější při rychlém přezouvání. Pletený materiál se při několika nošeních přizpůsobí tvaru chodidla, ale nesmí se napínat. Pokud kopačku koupíte příliš těsnou, svršek ji sice vyrovná, ale obtlačený palec bude trápit.</p>'
          '<p>Syntetika se dá bez obav utírat vlhkým hadříkem po každém tréninku. Po zápasu na blátě odstraňte hlínu z podrážky, vytáhněte vložky a nechte kopačky vyschnout při pokojové teplotě. Nikdy je nesušte na radiátoru, protože lepené spoje a tvar svršku se rychle poškodí. Kdo hraje několikrát týdně, ušetří střídáním dvou párů.</p>'
          '<h2>Dětské a juniorské kopačky Nike</h2>'
          '<p>Dětské modely mají v názvu zkratku Jr, případně GS nebo Dětské. Používají stejné řady jako dospělé kopačky, jen v menších velikostech a s jednodušším svrškem. Pro rostoucí nohu je důležitější kolík přiměřený váze dítěte než vysoká cena. Kopačka by měla mít u špičky rezervu zhruba šířky palce, aby se noha nezarazila při sprintu. Dítě stoupne do kopačky se zimními ponožkami v zimním tréninku a s tenkými v létě, proto zkoušejte s tím, co dítě skutečně nosí.</p>'
          '<ul><li>Pro děti na hřišti s trávou stačí FG/MG, pro umělku TF nebo MG.</li>'
          '<li>Zkontrolujte vnitřní stélku, měkká a vyjímatelná je pro ortopedickou vložku ideální.</li>'
          '<li>U velmi malých hráčů zvažte lehčí kolíky, aby se kopačka nezabořovala.</li>'
          '<li>Rodiče, kteří potřebují přehled ve všech značkách, najdou víc v <a href="/detske-kopacky/">dětských kopačkách</a>.</li></ul>'
          '<h2>Nike mezi ostatními značkami</h2>'
          '<p>Nike je spolu s Adidasem a Pumou jednou ze tří největších fotbalových značek na trhu. Obecně se tvarem řadí k užším a výraznějším kopačkám, zatímco jiní výrobci nabízejí širší nebo konzervativnější střih. Nelze to brát jako pravidlo, rozdíly jsou i uvnitř řad. Podívejte se na srovnání u <a href="/kopacky-adidas/">Adidas</a>, <a href="/kopacky-puma/">Puma</a>, <a href="/new-balance-kopacky/">New Balance</a>, <a href="/joma-kopacky/">Joma</a>, <a href="/mizuno-kopacky/">Mizuno</a> a <a href="/kopacky-under-armour/">Under Armour</a>. Pokud hledáte nápadnější barvu, pomůže výběr <a href="/ruzove-kopacky-nike/">růžové kopačky Nike</a>.</p>'
          '<h2>Co ještě patří k výbavě</h2>'
          '<p>Ke kopačkám patří <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>, <a href="/fotbalove-mice/">fotbalové míče</a> a vhodná trénovací obuv. Pro širší přehled sportu se vyplatí otevřít sekci <a href="/fotbal/">fotbal</a>. Značka Nike nabízí také <a href="/nike-dresy/">dresy</a> a <a href="/nike-kratasy/">kraťasy</a>, takže si můžete sladit výstroj. V sortimentu se občas objeví i sneakersy s označením kopačkového designu, které nejsou určené na hru. Zkontrolujte popis produktu, jestli se skutečně jedná o fotbalovou obuv s kolíky.</p>'
          '<h2>Jak kopačky rozchodit</h2>'
          '<p>Nové kopačky se nenosí poprvé rovnou do zápasu. Obujte je doma na pár hodin, potom na lehký trénink a teprve poté na plný zápas. Syntetický svršek se přizpůsobí, ale podrážka potřebuje čas, aby se uvolnila a přestala tlačit. Pokud při prvním tréninku cítíte tlak na malíčku nebo na nártu, zkuste jiné šněrování. Šněrování přes jedno očko a pevné zavázání pomáhá odlehčit nárt a přidržet patu.</p>'
          '<h2>Jak vybrat velikost a nenechat se zmást</h2>'
          '<p>Velikost kopaček Nike se uvádí v evropské a často i americké nebo britské stupnici. Porovnávejte vždy délku stélky v centimetrech, protože stejné číslo sedí na různých řadách odlišně. Mercurial bývá úzký a spíš kratší, Tiempo shovívavější. Pokud váháte mezi dvěma velikostmi, měřte večer, kdy je noha mírně oteklá, a berte v úvahu ponožky, v nichž hrajete.</p>'
          '<p>Při nákupu přes internet si ověřte podmínky vrácení u konkrétního obchodu a kopačky zkoušejte nejprve doma na měkké podložce, nikoli na venkovním hřišti. Kopačky, které byly použity na zemi, se většinou vrátit nedají. Starší kolekce a poslední kusy bývají dostupné jen v několika velikostech, proto srovnávejte i dostupnost.</p>',
    faq=[
        ('Jaký je rozdíl mezi řadami Mercurial, Phantom a Tiempo?', 'Mercurial je úzká a lehká kopačka pro rychlost a driblink, Phantom má strukturovaný svršek pro kontrolu míče a Tiempo klasičtější střih s měkčím materiálem a pohodlím. Žádná řada není určená výhradně pro daný post. Rozhoduje tvar chodidla a styl hry.'),
        ('Co znamená Elite, Pro, Academy a Club?', 'Jde o úrovně kvality téže řady. Elite je nejlehčí a nejcitlivější verze pro profesionály, Pro je jednodušší varianta, Academy je rozumný kompromis pro trénink i zápasy a Club je odolná základní kopačka. Pro děti a rekreační hráče bývá nejlepší Club nebo Academy.'),
        ('Co znamená FG, MG a TF v názvu?', 'FG je podrážka pro přírodní trávu, MG pro přírodní i umělou trávu, TF s drobnými nopy pro umělku a tvrdý povrch. IC je určená do haly. Pokud hrajete na více površích, začněte univerzální FG/MG a halovou obuv přidejte zvlášť.'),
        ('Dají se kopačky FG používat na umělé trávě?', 'Technicky ano, ale nedoporučuje se to. Dlouhé kolíky se zaklesnou do umělého povrchu, zatěžují kolena a rychleji se opotřebují. Pro umělku jsou vhodnější MG nebo TF. Výjimkou jsou hřiště s moderní umělou trávou označená pro kolíkové kopačky.'),
        ('Jak velké kopačky zvolit pro rostoucí dítě?', 'Rezerva před špičkou by měla odpovídat zhruba šířce palce. Zkoušejte s ponožkami, které dítě nosí na tréninku. Příliš velká kopačka zhoršuje stabilitu a zvyšuje riziko přetížení, proto nekupujte o dvě čísla navíc.'),
        ('Jak se starat o kopačky Nike?', 'Po tréninku odstraňte hlínu z podrážky, otřete svršek vlhkým hadříkem a vyjměte stélky. Kopačky nechte schnout při pokojové teplotě, nikdy na topení. Nepřevážejte je mokré v igelitové tašce. Střídání dvou párů výrazně prodlužuje životnost.'),
        ('Jsou kopačky Nike úzké?', 'Řada Mercurial sedí úzce, Phantom středně a Tiempo či Premier bývají prostornější. Rozdíly se liší podle generace i velikosti. Pokud máte široké chodidlo, zaměřte se na Tiempo a zkoušejte půl čísla větší, případně porovnejte i jiné značky.'),
        ('Mají kopačky Nike ortopedické vložky?', 'Standardní stélka je tenká a snímatelná, proto se do většiny modelů vejde ortopedická vložka. Při koupi počítejte s tím, že vložka zmenší vnitřní prostor, a zkoušejte s ní. U velmi úzkých elitních modelů je možnost omezená.'),
        ('Mám vybírat nejnovější model, nebo starší ročník?', 'Starší ročníky se obvykle liší jen jemnými úpravami svršku a podrážky, takže pro amatérského hráče je rozdíl v praxi malý. Dostupnost velikostí je ale omezenější. Pokud vám sedí tvar, je starší model rozumná cesta k úrovni Pro nebo Elite.'),
    ])

# ------------------------------------------------------------------ nike-teplaky
NEW['nike-teplaky'] = dict(
    title='Nike tepláky: Club Fleece, Tech Fleece, jogger a soupravy',
    desc='Nike tepláky pro muže, ženy i děti. Rozdíl mezi Club Fleece, Tech Fleece a Dri-FIT, střih jogger a straight, velikosti a péče. Porovnejte nabídky.',
    intro='<p>Nike tepláky nejsou jedna věc, ale několik různých kalhot pod stejným logem. Club Fleece je měkká bavlněná směs na každý den, Tech Fleece tenčí a tvarovaná pletenina do města, Dri-FIT je lehký trénink a týmové modely z lig jako NFL se nosí jako fanouškovský oblek. '
          'Na této stránce najdete tepláky značky z kategorie <a href="/teplaky/">tepláky</a>: pánské, dámské i dětské, samostatné kalhoty i <a href="/soupravy/">soupravy</a>. Průvodce vysvětluje, jak se liší materiály a střihy, jak číst názvy řad, jak vybrat velikost a jak tepláky prát, aby neztratily tvar. Podobné kousky u jiných značek najdete u <a href="/teplaky-puma/">Pumy</a>, <a href="/teplaky-tommy-hilfiger/">Tommy Hilfigeru</a> nebo u <a href="/jordan-teplaky/">Jordanu</a>, bez Nike pak v kategorii <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>',
    guide='<h2>Jak číst názvy: Club, Tech, Park a Sportswear</h2>'
          '<p>Nike tepláky se hledají snadněji, když rozumíte pojmenování. První slovo obvykle označuje sérii a druhé materiál nebo účel. Sportswear je označení lifestylové kolekce, která se nosí ve městě, Club je základní bavlněná řada, Tech Fleece jemnější konstrukce a Park klasický trénink pro týmy. Studio odkazuje na fitness a jógu, ACG na outdoorové oblečení a Jordan na vlastní basketbalovou kolekci.</p>'
          + T(['Označení', 'Charakter', 'Hodí se na'], [
              ['Club Fleece', 'měkká bavlněná směs s vnitřním počesáním', 'každodenní nošení, odpočinek, jaro a podzim'],
              ['Tech Fleece', 'tenčí strukturovaná pletenina, úzký střih', 'město, kombinace s bundou, chladnější dny'],
              ['Dri-FIT', 'lehká technická pletenina odvádějící pot', 'běh, fitness, tréninkový den'],
              ['Park', 'tréninková kalhota, často s manžetou nebo zipem', 'fotbal, tréninky týmů, školní sport'],
              ['Studio Fleece', 'vysoký pas, měkká pletenina', 'domácí cvičení, jóga, městský styl'],
              ['ACG', 'outdoorový design a odolnější materiál', 'výlety, lehký pohyb v přírodě'],
              ['Týmové modely (NFL a jiné ligy)', 'licencovaný potisk, často sideline střih', 'fanoušci, volný čas']]) +
          '<p>Pokud vám slovo Fleece nic neříká, jde o označení měkké pleteniny s počesanou vnitřní stranou. Nejde o technický fleece z turistických mikin, ale o bavlněnou pleteninu, která hřeje a je pohodlná. Pro srovnání mikin se stejnými názvy se podívejte na stránku <a href="/nike-mikina/">Nike mikina</a>, protože série se často prodávají jako sada.</p>'
          '<h2>Střih: jogger, straight a široké nohavice</h2>'
          '<p>Nike nabízí tepláky v několika střizích a názvy často prozradí, o který jde. Jogger má zúžené nohavice s manžetou, straight rovné bez manžety a širší kalhoty s volným dolním lemem se hodí pro uvolněný styl. Zúžená nohavice vypadá sportovně a nezachytí se o řetěz kola ani o kliku na schodech, rovná je pohodlnější při sedavé práci a lépe sedí přes boty.</p>'
          '<ul><li><strong>Jogger:</strong> manžeta u kotníku, vhodný k teniskám, nejčastější střih u řad Club a Tech.</li>'
          '<li><strong>Straight (rovný):</strong> bez manžety, delší nohavice, působí upraveněji.</li>'
          '<li><strong>Zip na nohavici:</strong> usnadňuje obouvání bot, běžné u tréninkových a fotbalových kalhot.</li>'
          '<li><strong>Vysoký pas u dámských modelů:</strong> hodí se ke zkráceným mikinám a na cvičení, kde se nemá sundávat.</li>'
          '<li><strong>Oversize:</strong> volné a prostorné, doporučuje se zvolit o velikost menší, pokud nechcete příliš široký tvar.</li></ul>'
          '<h2>Pánské, dámské a dětské tepláky Nike</h2>'
          '<p>Pánské střihy mají širší pas a rovnější linii boků, dámské užší pas a zakulacený bok, proto se nehodí vždy zaměnit. Dámské modely často nabízejí delší rozkrok a vyšší pas. Žena, která jinak chodí v pánské S, může být spokojenější v pánském než v dámském, pokud chce volný styl, ale pro úzký tréninkový střih vyberte dámský model.</p>'
          '<p>Dětské tepláky mají velikosti podle výšky nebo věku, proto je nejspolehlivější změřit dítě. Vedle samostatných kalhot se prodávají i teplákové soupravy a sety pro nejmenší včetně kojeneckých, které se kupují o půl až celou velikost větší. Dětské Club Fleece vydrží běžné hraní, ale kolena se otřou rychleji u dětí, které často klečí. Pokud je dítě mezi velikostmi, vezměte větší, protože pas se dá upravit šňůrkou.</p>'
          '<h2>Tepláková souprava, nebo samostatné kalhoty</h2>'
          '<p>Souprava za jednu cenu s mikinou či bundou má výhodu v tom, že obě části ladí odstínem i materiálem. Pro dlouhodobé nošení je ale praktičtější koupit díly zvlášť, protože tepláky se obvykle ošoupou dřív než mikina. Pokud se vám jedna část zničí, u jednotlivých kousků ji snadno doplníte. Soupravy hledejte v kategorii <a href="/soupravy/">soupravy</a>, mikiny v kategorii <a href="/mikiny/">mikiny</a> a trička v kategorii <a href="/sportovni-tricka/">sportovní trička</a>.</p>'
          '<h2>Na co se tepláky Nike hodí v praxi</h2>'
          '<ul><li><strong>Trénink a běh:</strong> zvolte lehčí Dri-FIT, ne bavlněný Club, který nasákne potem a zůstane těžký.</li>'
          '<li><strong>Fotbal a tým:</strong> řada Park má pevné manžety a zipy, které se hodí na kopačky.</li>'
          '<li><strong>Doma a na cesty:</strong> Club nebo Studio, měkké a nenáročné, bez vnitřního tlaku v pase.</li>'
          '<li><strong>Zimní dny:</strong> Tech Fleece vrstvěte s <a href="/termopradlo/">termoprádlem</a> a bundou, pokud je opravdu chladno.</li>'
          '<li><strong>Cestování:</strong> tmavý jogger s kapsami na zip je praktičtější než světlý, který viditelně zašpiníte.</li></ul>'
          '<p>Chcete-li si vybrat podle účelu, projděte také kategorii <a href="/leginy/">legíny</a> pro přiléhavý trénink a <a href="/sportovni-bundy/">sportovní bundy</a> k venkovnímu vrstvení. Pro návaznost na nabídku Nike otevřete <a href="/nike-leginy/">Nike legíny</a>.</p>'
          '<h2>Velikost a nošení</h2>'
          '<p>Velikost Nike odpovídá obvodu pasu a boků a rozsah se mírně liší podle řady. Tech Fleece je přiléhavější než Club, takže pokud váháte, vezměte spíše větší. Dolní okraj nohavice má končit u kotníku, aby se při chůzi neobtíral o podlahu. Šňůrka v pase pomáhá doladit obvod, ale neměla by být jediným prvkem, který tepláky drží. Pokud při zkoušce visí v rozkroku, šňůrka to nenapraví.</p>'
          '<p>Při online nákupu si ověřte, jestli je velikostní tabulka v centimetrech nebo v evropských značkách. Zkontrolujte délku nohavic (inseam), protože vyšší lidé narazí na krátké modely. U dětských a kojeneckých souprav zvolte velikost podle výšky, nikoli podle věku, protože děti rostou odlišně.</p>'
          '<h2>Péče, aby tepláky nepoztrácely tvar</h2>'
          '<p>Bavlněné směsi perte při nižší teplotě a obracejte je naruby, aby se omezilo žmolkování a vyblednutí potisku. Pokud máte tepláky s technickou pleteninou, nepoužívejte aviváž, která brání odvodu potu. Při sušení v sušičce volte nižší teplotu, protože vyšší teplota zkracuje bavlnu a zhoršuje pružnost lemů. Sušení ve vodorovné poloze zachová tvar kolen.</p>'
          '<ul><li>Světlé tepláky perte zvlášť, aby nezískaly šedý nádech.</li>'
          '<li>Potisky a loga nežehlete přímo, ale přes látku.</li>'
          '<li>Žmolky odstraňujte strojkem na textil, ne nůžkami.</li></ul>'
          '<h2>Co vám řeknou kapsy, manžety a pas</h2>'
          '<p>Detaily rozhodují o tom, jak budou tepláky fungovat po půl roce. Kapsy na zip nevypadnou klíče ani telefon při běhu nebo na kole, zatímco otevřené šikmé kapsy jsou pohodlnější při sezení. Zadní kapsa se hodí na peněženku, ale u joggeru ji ocení hlavně ti, kdo tepláky nosí do města. Manžeta má pevně držet, ale nesmí škrtit lýtko, a pas se šňůrkou a gumou má sedět tak, aby šňůrka sloužila jen k doladění.</p>'
          '<p>Vnitřní strana látky se u bavlněné směsi opotřebuje nejdřív na vnitřní straně stehen, kde se kalhoty o sebe třou. Proto u dlouhodobého nošení hledejte hustší pleteninu a dobrý šev v rozkroku. Zesílená kolena mají u dětských modelů smysl, protože právě tam se nejčastěji prodřou.</p>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Nike tepláky se prodávají v mnoha barvách a ročnících, takže stejný název může mít v různých obchodech odlišné složení. Čtěte popis: poměr bavlny a polyesteru ovlivňuje pružnost a sušení. Dále sledujte, zda je v nabídce uvedeno zboží z licencovaných týmových kolekcí, které je určené spíš pro fanoušky než pro sport. Při výběru z podobných značek porovnejte <a href="/gymbeam-teplaky/">GymBeam</a> a <a href="/teplaky-puma/">Pumu</a>.</p>'
          '<p>Dobré pravidlo zní nekupovat podle fotografie, ale podle složení, délky nohavice a střihu. Barva na obrázku se v obchodech liší, takže se podívejte na označení odstínu. Pokud hledáte tepláky na konkrétní sport, zkontrolujte, zda je vhodnější lehčí technická varianta, nebo měkký bavlněný kus na volný čas.</p>',
    faq=[
        ('Čím se liší Club Fleece od Tech Fleece?', 'Club Fleece je klasická měkká bavlněná směs s počesanou vnitřní stranou, pohodlná na každý den. Tech Fleece je tenčí a strukturovanější pletenina s úzkým střihem, vhodná do města a na vrstvení. Club je volnější a levnější na údržbu, Tech tvarovaný a elegantnější.'),
        ('Jak vybrat velikost Nike tepláků?', 'Řiďte se obvodem pasu a boků z tabulky výrobce a délkou nohavice. Tech Fleece sedí přiléhavěji než Club, proto při váhání zvolte větší. Šňůrka v pase pomáhá s obvodem, ale nevyřeší špatně zvolenou velikost v rozkroku a stehnech.'),
        ('Hodí se Nike tepláky na běh a trénink?', 'Záleží na řadě. Bavlněný Club Fleece nasákne potem a zůstane těžký, proto na běh zvolte Dri-FIT nebo jiný lehký technický materiál. Park a Studio se hodí na lehčí trénink a fotbal, Tech Fleece spíš do chladného města než do posilovny.'),
        ('Jak jsou na tom dětské tepláky Nike?', 'Dětské tepláky mají velikosti podle výšky nebo věku a existují i soupravy včetně kojeneckých. Zvolte raději o trochu větší velikost, protože dítě rychle roste a pas se dá doladit šňůrkou. Na kolenou se tepláky otřou nejdřív, proto se vyplatí robustní bavlněná směs.'),
        ('Mám koupit soupravu, nebo jen tepláky?', 'Souprava ladí barvou i materiálem a vypadá jednotně. Samostatné kalhoty doplníte jinou mikinou a při opotřebení vyměníte jen jednu část. Pokud nosíte teplákovou část často, bývá praktičtější koupit díly zvlášť.'),
        ('Jak prát Nike tepláky?', 'Perte je naruby při nižší teplotě bez aviváže, zejména technické materiály. Sušte při nízké teplotě nebo ve vodorovné poloze. Potisky nežehlete přímo a světlé barvy perte zvlášť, aby nezískaly šedý odstín.'),
        ('Co jsou týmové tepláky NFL a podobných lig?', 'Jde o licencované sportovní kalhoty s logem klubu, často v sideline střihu. Slouží primárně fanouškům, ne tréninku. Materiál bývá podobný bavlněným řadám, ale potisk je citlivější na praní, proto jej perte naruby.'),
        ('Mají tepláky Nike zip na nohavici?', 'Některé tréninkové a fotbalové modely ano, usnadňuje to obouvání bot. Jogger s manžetou zip většinou nemá. Pokud potřebujete tepláky na tělocvik nebo fotbalový trénink, hledejte v popisu zmínku o zipu u kotníku.'),
        ('Jak poznám dámský a pánský střih?', 'Dámský střih má užší pas, zaoblené boky a často vyšší pas, pánský rovnější linii. Označení najdete v názvu produktu i v kategorii. Pokud chcete volnější tvar, vyzkoušejte menší velikost pánského modelu, ale může být v rozkroku příliš prostorná.'),
    ])

# ------------------------------------------------------------------ nike-mikina
NEW['nike-mikina'] = dict(
    title='Nike mikina: Club Fleece, Tech Fleece, Park a Dri-FIT',
    desc='Nike mikina pánská, dámská i dětská. Club Fleece, Tech Fleece, Park a Dri-FIT: rozdíly, střihy, velikosti, vrstvení a praní. Porovnejte nabídky obchodů.',
    intro='<p>Nike mikina může znamenat měkký bavlněný pulovr do města, tenkou technickou vrstvu na běh nebo fanouškovský kus s logem týmu. Značka dělí mikiny do řad podle použití a rozdíl mezi nimi je větší než rozdíl mezi barvami. Club Fleece je klasika na každý den, Tech Fleece strukturovanější a úzký, Park tréninkový a Dri-FIT odvádí pot. '
          'Tato stránka nabízí mikiny značky z kategorie <a href="/mikiny/">mikiny</a>, od pánských a dámských po dětské a týmové modely. Průvodce vysvětluje názvy řad, střihy s kapucí a bez, na zip i přes hlavu, velikosti, vrstvení a praní. Pro fleecové vrstvy se podívejte do <a href="/fleecove-mikiny/">fleecových mikin</a> a pro trénink do <a href="/funkcni-mikiny/">funkčních mikin</a>.</p>',
    guide='<h2>Řady mikin Nike a jejich smysl</h2>'
          '<p>Názvy v nabídce se opakují a podle nich poznáte, k čemu je kus určený. Slovo Fleece u Nike označuje měkkou pleteninu s počesanou vnitřní stranou, nikoli turistický fleece z polyesteru. Výběr proto začněte tím, v jaké situaci mikinu vezmete na sebe nejčastěji.</p>'
          + T(['Řada', 'Materiál a střih', 'Nejlepší využití'], [
              ['Club Fleece', 'bavlněná směs, klasický střih s kapucí nebo bez', 'město, volný čas, jaro a podzim'],
              ['Tech Fleece', 'tenčí strukturovaná pletenina, přiléhavý střih', 'městské vrstvení, chladné dny, minimalistický styl'],
              ['Park (Fleece)', 'tréninkový fleece, pevné manžety', 'fotbal, týmové tréninky, školní sport'],
              ['Dri-FIT', 'lehká technická pletenina odvádějící vlhkost', 'běh, fitness, rychlé tempo'],
              ['Sportswear (oversize)', 'volný střih, často měkčí bavlna nebo modal', 'volný čas, dámský uvolněný styl'],
              ['Týmové modely (NFL, MLB, NBA)', 'licencovaný potisk, často hoodie', 'fanoušci, tribuny, město']]) +
          '<p>U týmových mikin se hledí především na licenci a potisk. Materiál bývá podobný řadě Club, ale potisk je citlivější na praní, takže je vhodné prát naruby. Pokud kupujete mikinu jako dárek fanouškovi, ověřte přesný název týmu a ročník kolekce, protože se barevné varianty mění.</p>'
          '<h2>Kapuce, zip, nebo přes hlavu</h2>'
          '<p>Střih ovlivňuje praktičnost víc, než čekáte. Mikina s kapucí chrání před větrem a drobným deštěm, ale kapuce při jízdě v autě nebo s batohem tlačí. Mikina na zip se lépe svléká při změně teploty a hodí se při sportu s proměnlivou intenzitou. Pulovr s kulatým výstřihem je nejčistší a snadno se vrství pod bundu, ale bez zipu je těžší se při zahřátí odvětrat.</p>'
          '<ul><li><strong>Hoodie (s kapucí):</strong> nejuniverzálnější, nejčastější volba pro město a výlet.</li>'
          '<li><strong>Full-zip:</strong> praktický pro vrstvení, trénink a rychlé svlékání.</li>'
          '<li><strong>Crew (kulatý výstřih):</strong> minimalistický vzhled, snadno se kombinuje se košilí nebo bundou.</li>'
          '<li><strong>Quarter-zip:</strong> krátký zip u krku pro odvětrání, oblíbený u běžců a golfistů.</li>'
          '<li><strong>Cropped (zkrácená):</strong> dámský trend, hodí se k vysokému pasu a legínám.</li></ul>'
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p>Pánské mikiny mají širší ramena a rovnější linii, dámské jsou užší v pase a často o něco kratší. Dámské Sportswear oversize modely jsou záměrně volné a stejně dobře je nosí i muži, kteří hledají širší střih. U dětských kusů záleží na výšce dítěte víc než na věku a také na tom, jestli mikina vydrží sezónu. Kvalitní Club nebo Park fleece vydrží běžné hraní, ale rukávy se na loktech nejdříve ošoupou.</p>'
          '<p>Mezi dětskými kusy najdete jak jednobarevné modely, tak potištěné s logem Nike. Zvolte raději tmavší barvu na každodenní nošení a světlejší na výlet. Pokud se dítě pohybuje mezi velikostmi, vezměte větší, aby mikina přečkala růst a rukávy se daly přehrnout.</p>'
          '<h2>Velikost: jak sedí Nike</h2>'
          '<p>Nike mikiny sedí spíše standardně až o něco volněji, přičemž Tech Fleece je přiléhavější a oversize naopak výrazně volné. Měřte šířku v ramenou a délku od ramene k lemu a porovnejte ji s vlastní oblíbenou mikinou. Pokud plánujete pod mikinu nosit další vrstvy, zvolte o velikost větší. Pro sportovní účely je lepší přiléhavější sedící kus, který nepřekáží v pohybu.</p>'
          + T(['Situace', 'Doporučení k velikosti'], [
              ['Mikina k přímému nošení na tričko', 'standardní velikost podle ramen'],
              ['Vrstvení pod bundu', 'jedna velikost navíc nebo tenčí řada, např. Tech'],
              ['Volný dámský styl', 'oversize model v běžné velikosti, nebo menší pánský'],
              ['Běh a trénink', 'přiléhavější střih, nesmí se při pohybu zdvihat'],
              ['Dítě v růstu', 'o jednu velikost větší, rukáv se dá přehrnout']]) +
          '<h2>Vrstvení: jak mikinu zkombinovat</h2>'
          '<p>Mikina funguje jako střední vrstva. Pod ni patří <a href="/sportovni-tricka/">sportovní tričko</a> nebo <a href="/termopradlo/">termoprádlo</a>, nad ni v chladu <a href="/sportovni-bundy/">sportovní bunda</a>. Při vrstvení hlídejte tloušťku: tlustá bavlněná mikina pod tlustou bundou omezuje pohyb a nasákne potem. Tech Fleece je tenčí a v těsné bundě vypadá lépe, Club se víc hodí jako vnější vrstva za suchého počasí.</p>'
          '<p>K mikině se nejčastěji kombinují <a href="/nike-teplaky/">Nike tepláky</a>, <a href="/leginy/">legíny</a> nebo džíny. Pokud chcete jednotný vzhled, vyberte kus ze stejné řady. Pro sladění barev funguje jednoduché pravidlo: jedna výrazná barva a zbytek neutrální. Pro univerzální kombinace se hodí tmavé tóny z výběru <a href="/cerna-mikina/">černá mikina</a>.</p>'
          '<p>Při výběru barvy počítejte s praním a s tím, že světlé odstíny zvýrazní skvrny od jídla i od prachu. Tmavě modrá, šedá a černá jsou nejmíň náročné, zatímco bílá a pastelové tóny vypadají svěže jen krátce. Výrazné barvy se hodí do sportovních kolekcí, kde mikina slouží i jako viditelná vrstva při večerním běhu nebo jízdě na kole.</p>'
          '<h2>Pro koho je Nike mikina vhodná</h2>'
          '<ul><li><strong>Student a každodenní nošení:</strong> Club Fleece s kapucí, tmavá barva, jedna velikost navíc na vrstvení.</li>'
          '<li><strong>Běžec a aktivní sportovec:</strong> Dri-FIT nebo quarter-zip, který rychle schne.</li>'
          '<li><strong>Fanoušek:</strong> týmový hoodie ze sportovní ligy, nejlépe s ověřenou licencí.</li>'
          '<li><strong>Trenér a hráč fotbalu:</strong> řada Park, odolná a s pevnými manžetami.</li>'
          '<li><strong>Rodič školáka:</strong> odolný pulovr nebo full-zip v tmavé barvě, aby se skvrny méně projevily.</li></ul>'
          '<p>Mikiny se často srovnávají s dalšími značkami, a to nejen z oblasti sportu. Podívejte se na srovnání v kategorii <a href="/panska-mikina/">pánská mikina</a> a na stránce <a href="/gap-mikina/">Gap mikina</a>.</p>'
          '<h2>Detaily, které se vyplatí zkontrolovat</h2>'
          '<p>U mikiny sledujte nejprve lem a manžety. Žebrovaná pletenina má po natažení vracet tvar, jinak se rukávy rychle rozvolní. Kapsa typu klokanka je pohodlná pro ruce, ale hůř drží věci, zatímco boční zipové kapsy uloží klíče a telefon. Dále se dívejte na šněrování kapuce, na výztuž krku a na to, zda je vnitřní strana hladká, nebo počesaná. Hladká se lépe nosí na tričko, počesaná hřeje, ale při praní víc žmolkuje.</p>'
          '<p>Další rozdíl udělá střih ramen. Spuštěné rameno je volné a pohodlné, zatímco klasické nasazené rameno drží tvar při sportu. U dámských oversize kusů se spuštěné rameno počítá jako součást návrhu, takže se nemá zaměňovat s příliš velkou velikostí. Pokud mikinu vybíráte jako dárek, dejte přednost neutrální barvě a střední velikosti, kterou lze v nejhorším případě snadno vyměnit.</p>'
          '<h2>Péče, aby mikina vydržela</h2>'
          '<p>Perte ji naruby při nízké teplotě, protože fleece a potisk jsou citlivé na horkou vodu. Aviváž ucpává pleteninu, snižuje hřejivost a odvod potu, proto ji vynechte. Mikinu nenechávejte dlouho vlhkou a sušte ji bez přímého tepla. V sušičce ji zařaďte na nízký výkon, vyšší teplota způsobí žmolky a smrštění. Žmolky ze starších kusů odstraňte strojkem na textil a mikina vypadá znovu novější.</p>'
          '<ul><li>Světlé a tmavé kusy perte odděleně.</li>'
          '<li>Při praní zapněte zip, aby neškrábal ostatní prádlo.</li>'
          '<li>Potisky a vyšívaná loga nežehlete přímo, přikryjte je látkou.</li></ul>'
          '<h2>Na co si dát pozor při srovnávání</h2>'
          '<p>Stejný název se může objevit v pánské, dámské i dětské variantě a v různých ročnících. Proto kontrolujte pohlaví, složení a velikostní tabulku. Do nabídky patří i licencované týmové mikiny, které jsou jiným typem zboží než sportovní Club a Park. Pokud hledáte funkční kousek na pohyb, upřednostněte výběr v kategorii <a href="/funkcni-mikiny/">funkční mikiny</a>, pro teplo zase <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi Club Fleece a Tech Fleece?', 'Club Fleece je klasická, měkká bavlněná směs s volnějším střihem, vhodná na každý den. Tech Fleece je tenčí, strukturovanější a přiléhavější, proto se lépe vrství pod bundu a dobře vypadá ve městě. Club je praktičtější na praní, Tech střízlivější a tvarovanější.'),
        ('Hodí se Nike mikina na běh?', 'Bavlněná Club mikina na běh není ideální, protože nasákne potem. Vhodnější jsou řady s technickou pleteninou, například Dri-FIT nebo quarter-zip. Fleece nechte na chlad, kde slouží jako teplá vrstva po rozcvičení.'),
        ('Jak vybrat správnou velikost?', 'Porovnejte šířku v ramenou a délku s vaší oblíbenou mikinou. Standardní řady sedí běžně až mírně volněji, Tech Fleece přiléhavěji a oversize výrazně volně. Chcete-li ji vrstvit, zvolte o velikost větší.'),
        ('Čím se liší dámská mikina od pánské?', 'Dámská je v pase užší a častěji kratší, pánská má širší ramena a rovnější linii. Oversize dámské kusy jsou záměrně volné, proto se často nosí i unisex. Pokud chcete volný vzhled, zkuste menší velikost pánského modelu.'),
        ('Jak dlouho vydrží fleecová mikina?', 'Při šetrném praní několik sezón. Žmolky se tvoří při vysoké teplotě a při tření v sušičce, proto perte na nízkých stupních a bez aviváže. Nejdřív se ošoupou lokty a manžety, u dětí kolena a lokty při hraní.'),
        ('Jsou týmové mikiny NFL a MLB teplé?', 'Bývají podobné řadě Club nebo mají hřejivou vnitřní stranu, ale cílí hlavně na fanoušky. Potisk je citlivější na praní a na žehlení. Jestli potřebujete mikinu na sport, vyberte raději řadu Park, Dri-FIT nebo fleece z kategorie funkčních mikin.'),
        ('Jak perou mikiny s potiskem?', 'Naruby, na nižší teplotu, s jemným prostředkem a bez aviváže. Vyhněte se vysoké teplotě sušení, která popraská potisk. Při žehlení potisk přikryjte látkou a nikdy nežehlete přímo na loga.'),
        ('Kdy zvolit mikinu na zip a kdy přes hlavu?', 'Zip vyhovuje při změnách teploty, při sportu a při vrstvení, protože se snadno ventiluje. Přes hlavu je čistější, bezpečnější pro děti a skvěle sedí pod bundou. Quarter-zip kombinuje obojí a hodí se při běhu.'),
        ('Je lepší koupit mikinu s kapucí nebo bez?', 'S kapucí se hodí do větru a deště a vypadá uvolněně. Bez kapuce je elegantnější, nepřekáží při řízení ani s batohem a dobře se vrství pod bundu. Rozhodněte podle toho, jak často nosíte batoh nebo bundu s vlastní kapucí.'),
    ])
