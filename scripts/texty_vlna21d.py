"""sporteka.cz — wave 21d (4. 11. 2026): long texts (>= 1650 words) for chranice-bojove-sporty, panske-plavky, jezdecke-doplnky, cyklo-kola-a-rafky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ chranice-bojove-sporty
NEW['chranice-bojove-sporty'] = dict(long=True,
    title='Chrániče na bojové sporty: zuby, suspenzory, holeně',
    desc='Chránič zubů, suspenzor, holeně a tlapy pro box, MMA, kickbox i hokej. Jak vybrat velikost, tvarování a péči a porovnat obchody.',
    intro='<p>Chrániče jsou ta část výbavy, o které se nepřemýšlí, dokud ji člověk nepotřebuje. Chránič zubů zadrží náraz na čelist, suspenzor uchrání citlivé místo a pevné holeně zmírní kopy při sparringu. '
          'V tréninku bojových sportů se k nim proto hlásí většina trenérů jako k základu, ještě než se kupují drahé rukavice nebo oblečení. Podobné kousky ale využijí také hokejisté, florbalisté a brankáři.</p>'
          '<p>V této kategorii na Sportece porovnáte nabídky českých obchodů u značek Winnwell, Safe Jawz, ACRA Sport, Opro, Venum, DBX Bushido, Bauer, Sisu nebo RDX. '
          'K výběru se hodí i <a href="/boxerske-rukavice/">boxerské rukavice</a>, <a href="/boxovaci-pytle/">boxovací pytle</a>, <a href="/obleceni-bojove-sporty/">oblečení na bojové sporty</a> a <a href="/bojove-sporty/">přehled bojových sportů</a>. '
          'Níže najdete rozdělení podle účelu, rady k velikosti a údržbě i seznam chyb, kterým se dá vyhnout.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Sortiment je širší, než by název napovídal. Převažují chrániče zubů a suspenzory, k nim přibývají holeně s nárty, pomůcky pro trenéry a ochrana určená pro hokej či florbal. '
          'Než začnete porovnávat nabídky, ujasněte si, který sport budete provozovat a jaký kontakt vás čeká, protože podle toho se mění potřebná tuhost i rozsah ochrany.</p>'
          + T(['Druh chrániče', 'Co chrání', 'Typické použití'], [
              ['Chránič zubů', 'zuby, dásně, částečně čelist', 'box, MMA, kickbox, karate, hokej'],
              ['Suspenzor a kraťasy se suspenzorem', 'rozkrok', 'všechny kontaktní sporty, hokej, florbal'],
              ['Chrániče holení a nártů', 'holenní kost, nárt', 'muay thai, kickbox, MMA, taekwondo'],
              ['Chrániče loktů a kolen', 'klouby při pádech', 'grappling, judo, tréninky pádů'],
              ['Chránič hrudníku', 'žebra a hrudní kost', 'sparring s plným kontaktem, děti'],
              ['Tlapy a terče', 'ruce trenéra', 'nácvik kombinací a kopů']]) +
          '<h2>Chránič zubů: tvarování a velikost</h2>'
          '<p>Chránič zubů je nejčastěji kupovaná položka a také ta, u které rozhoduje správné přizpůsobení. Univerzální kus z pěny se prostě nasadí, ale sedí hůř a při úderu se může posunout. '
          'Tvarovatelné modely se ponoří do horké vody, vloží do úst a prstem a jazykem se přitlačí na zuby; pak se zchladí a materiál si zapamatuje tvar chrupu. '
          'Postup vždy dodržte podle návodu výrobce, protože příliš horká voda materiál zdeformuje, příliš studená ho dostatečně neobměkčí.</p>'
          '<ul><li><strong>Jednovrstvé modely</strong> jsou nejlevnější a stačí pro lehký kontakt a děti.</li>'
          '<li><strong>Dvouvrstvé modely</strong> mají tužší vnější část a měkčí vnitřní, takže lépe tlumí nárazy.</li>'
          '<li><strong>Dětské a juniorské velikosti</strong> mají menší oblouk, aby se vešly do úst, kde rostou zuby.</li>'
          '<li><strong>Modely s rovným průchodem vzduchu</strong> usnadňují dýchání, což ocení hlavně vytrvalejší sparringy.</li>'
          '<li><strong>Chrániče pro rovnátka</strong> jsou upravené tak, aby nedráždily zámky a drátky; zeptejte se ortodontisty.</li></ul>'
          '<p>Nasazený chránič nesmí tlačit na patro ani vyvolávat dávivý reflex a při zavřených ústech by měl držet i bez zatnutých čelistí. V nabídce jsou značky Safe Jawz, Opro, Venum, Sisu a DBX Bushido, které se liší tvarem i tuhostí materiálu.</p>'
          '<h2>Suspenzory pro muže, ženy a brankáře</h2>'
          '<p>Suspenzor patří mezi chrániče, které se kupují nejdřív. Protože jde o osobní kus výbavy, vybírá se hlavně podle velikosti, tvaru a způsobu nošení. '
          'Existují samostatné chrániče s pásem, kompresní kalhoty s kapsou na vložku a kraťasy, ve kterých je ochrana ušitá napevno. '
          'Hokejisté a florbalisté si tak pořizují takzvaný jock, brankáři zvolí pevnější konstrukci s širším krytem; dámské varianty se označují jako jill a mají jiný tvar a výplň.</p>'
          + T(['Provedení', 'Výhoda', 'Na co si dát pozor'], [
              ['Samostatný suspenzor s pásem', 'volba tvrdosti a velikosti', 'musí se správně zapnout, aby neujížděl'],
              ['Kompresní kalhoty s kapsou', 'drží vše na místě, zároveň podpírají svaly', 'kapsa musí odpovídat vložce'],
              ['Kraťasy se suspenzorem', 'jedna vrstva, rychlé oblékání', 'ochrana se těžko vymění samostatně'],
              ['Brankářský suspenzor', 'větší kryt a tužší materiál', 'může omezit pohyb v nízkém postoji'],
              ['Dámský chránič', 'tvarovaný pro ženskou anatomii', 'sjednocovat velikost s kalhotkami či kraťasy']]) +
          '<p>Z praxe: velikost se řídí obvodem pasu nebo kyčlí, rozhodně ne velikostí tričkových oděvů. Pokud se chránič při dřepu nebo výpadu otáčí, je buď velký, nebo špatně zapnutý. Značky Winnwell, CCM, Bauer, Salming a RDX mají různé střihy, proto vždy porovnejte jejich tabulky.</p>'
          '<h2>Chrániče holení a nártů</h2>'
          '<p>V stand-upových sportech, kde se kope, mají holeně velký význam. Kop do holenní kosti bolí soupeře i toho, kdo kope, a nechráněná kost snáší nárazy špatně. '
          'Proto se v kickboxu a thajském boxu používají tvrdší a větší chrániče, kdežto pro MMA a taekwondo se volí lehčí a anatomicky tvarované modely.</p>'
          '<ul><li><strong>Neoprenové chrániče</strong> padnou těsně jako ponožka a jsou lehké, vhodné pro grappling a lehčí trénink.</li>'
          '<li><strong>Chrániče s pěnovou či EVA výplní</strong> mají měkké jádro a drží tvar, hodí se na technický sparring.</li>'
          '<li><strong>Kožené a koženkové modely</strong> vydrží víc, ale jsou těžší a hůř se čistí.</li>'
          '<li><strong>Chrániče s nártem</strong> pokrývají přední část chodidla a chrání při kopech.</li></ul>'
          '<p>Při výběru zkontrolujte, zda chrániče nekloužou po lýtku, zda nepřekáží při ohnutí kolena a zda řemínky zapínáte bez zátěže pro cévy. U závodů je dobré zjistit, jestli organizace, například IMMAF, vyžaduje schválený typ.</p>'
          '<h2>Pomůcky pro trenéra: tlapy a terče</h2>'
          '<p>Ve vybraných nabídkách se objeví i pomůcky, které nechrání bojovníka, nýbrž trenéra. Tlapy, terče a jejich kombinace umožňují procvičovat údery a kopy v pohybu a pracovat s odezvou. '
          'Povrch bývá z koženky nebo kůže a výplň z pěny. Při výběru se řiďte velikostí dlaně a pohodlím zápěstí, zvláště když na tlapách pracujete dlouho. Pro nácvik kombinací vybírejte pár, který má stejně tuhé povrchy, aby se údery nelišily.</p>'
          '<h2>Chrániče pro hokej a florbal</h2>'
          '<p>Část nabídky tvoří chrániče vyrobené pro týmové sporty. Hokejové a florbalové suspenzory, brankářské jocky a chrániče zubů se kupují podle věkových řad: dětská, junior a senior. '
          'Širší ochranu hokejistů najdete v kategorii <a href="/hokejove-chranice/">hokejové chrániče</a>, kde jsou i helmy, nárameníky a lokty. '
          'Pro obecnější přehled slouží <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Jak vybrat podle sportu a úrovně</h2>'
          '<p>Začátečník, který chodí na kondiční box, vystačí s chráničem zubů a jednoduchým suspenzorem. Kdo začne sparovat, přidá holeně a rukavice s větší výplní. Závodník řeší schválení podle pravidel a ochranu doplní helmou, vestou a chrániči hrudníku. '
          'Děti by měly dostat výbavu v pořadí, které doporučí trenér; hlavně chránič zubů a rozkroku, protože i při lehkém kontaktu dokáží zabránit zbytečnému úrazu. '
          'Pokud trénujete grappling nebo judo, zaměřte se na ochranu kloubů, bandáže a ortézy z kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>'
          '<h2>Péče a hygiena</h2>'
          '<p>Chrániče se potí a ústa jsou prostředím, kde se rychle množí bakterie. Chránič zubů po každém tréninku opláchněte studenou vodou, jednou za čas ho vyčistěte zubním kartáčkem a mýdlem a nechte uschnout. '
          'Odkládejte ho do větraného pouzdra, nikoli do vlhké tašky. Suspenzory a kompresní kalhoty perte podle návodu, nejlépe na šetrný program, a nesušte je na topení. '
          'Holeně a tlapy z koženky otírejte vlhkým hadříkem a nechte vyschnout při pokojové teplotě; sluneční žár a topení materiály křehčí.</p>'
          '<h3>Kdy chránič vyměnit</h3>'
          '<ul><li>Chránič zubů, který má praskliny, ztenčený okraj nebo ztratil tvar, nahraďte.</li>'
          '<li>Rostoucí děti potřebují nový chránič zubů častěji, protože se mění chrup.</li>'
          '<li>Výplň suspenzoru, která je mačkaná či popraskaná, už nechrání.</li>'
          '<li>Rozpadající se suchý zip na holeních je důvod ke koupi nových.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce nabídek v kategorii mají ' + B(('winnwell', 'Winnwell'), ('safe-jawz', 'Safe Jawz'), ('acra-sport', 'ACRA Sport'), ('opro', 'Opro'), ('venum', 'Venum'), ('dbx-bushido', 'DBX Bushido'), ('bauer', 'Bauer'), ('sisu', 'Sisu'), ('bushido', 'Bushido'), ('ccm', 'CCM'), ('rdx', 'RDX')) + '. '
          'Winnwell, Bauer a CCM mají silné zázemí v hokeji, Safe Jawz, Opro a Sisu se soustředí na chrániče zubů, Venum, RDX a Bushido mají k dispozici pestrou výbavu pro bojové disciplíny.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupě chrániče zubů bez tvarování, který se při sparringu posouvá.</li>'
          '<li>Vybrání suspenzoru podle věku, a ne podle obvodu pasu.</li>'
          '<li>Úsporná koupě holení bez ohledu na sport, takže chrániče muay thai nahrazuje měkká neoprenová varianta.</li>'
          '<li>Nošení stejného chrániče zubů celé roky, přestože se zmenšil nebo opotřebil.</li>'
          '<li>Skladování ve vlhké tašce, kde chrániče zapáchají a plesniví.</li>'
          '<li>Ignorování pravidel soutěže, která mohou určovat typ chráničů.</li></ul>'
          '<h2>Kde pokračovat</h2>'
          '<p>Chrániče fungují nejlépe ve spojení s dalšími kousky výbavy. Rukavice najdete v kategorii <a href="/boxerske-rukavice/">boxerské rukavice</a>, nácvik úderů zajistí <a href="/boxovaci-pytle/">boxovací pytle a hrušky</a>, kondici posílí <a href="/svihadla/">švihadla</a> a pohodlí zajistí <a href="/sportovni-kratasy/">sportovní kraťasy</a>. Úplný přehled nabízí stránka <a href="/bojove-sporty/">bojové sporty</a>.</p>',
    faq=[
        ('Kdy je chránič zubů povinný?', 'Povinnost určují pravidla soutěže a oddíl. V boxu, MMA a kickboxu se nosí při sparringu i v zápasech, u dětí často už na tréninku. Zeptejte se trenéra, ale rozumné je používat ho při jakémkoli kontaktu hlavy.'),
        ('Jak se tvaruje chránič zubů?', 'Většina modelů se ponoří na zhruba půl minuty do horké, ale nevařící vody, krátce se zchladí a vloží se do úst. Pak ho přitlačte jazykem a prsty ke chrupu a nechte ve studené vodě ztuhnout. Řiďte se pokyny výrobce.'),
        ('Dá se chránič zubů nosit s rovnátky?', 'Ano, ale vyberte model určený pro rovnátka, který nepřiléhá na zámky tak těsně. Nejlépe se předem zeptejte ortodontisty, zda doporučuje konkrétní typ nebo zákaznický chránič z ordinace.'),
        ('Jak vybrat velikost suspenzoru?', 'Změřte obvod pasu či kyčlí a porovnejte s tabulkou výrobce. Při dřepu a výpadu se nesmí posouvat ani tlačit. Hokejové a bojové značky mají různé střihy, proto nespoléhejte na číslo ze starší výbavy.'),
        ('Liší se suspenzor pro ženy?', 'Ano. Dámské modely bývají označené jako jill nebo pro ženy a mají jiný tvar krytu a pásu. Kraťasy či kompresní kalhoty pro ženy se vybírají podle velikosti oblečení.'),
        ('Jaké chrániče holení potřebuji na kickbox?', 'Obvykle plnější chrániče s pěnovou výplní a chráničem nártu, které drží při kopech. Pro MMA stačí lehčí, přiléhavější varianta. U soutěží si ověřte, zda pravidla nežádají schválený typ.'),
        ('Je lepší neopren, nebo koženka?', 'Neopren je pohodlný, lehký a drží na noze, ale tlumí méně. Koženka a tužší výplň chrání lépe při silných kopech, jenže jsou těžší a hůře se čistí. Vyberte podle intenzity sparringu.'),
        ('Jak často vyměnit chránič zubů?', 'Jakmile je poškozený, ztenčený nebo ztratí tvar. Děti a mladiství vyměňují častěji, protože se jim mění chrup. U dospělých záleží na intenzitě používání a péči o chránič.'),
        ('Jak vyčistit chrániče a zabránit zápachu?', 'Chránič zubů opláchněte po tréninku a občas umyjte mýdlem. Textilní části perte podle štítku a nechte volně uschnout. Nikdy nenechávejte vlhké chrániče zavřené v tašce přes noc.'),
        ('Hodí se chrániče z této kategorie i na hokej a florbal?', 'Některé ano. Hokejové a florbalové suspenzory, brankářské jocky a chrániče zubů jsou přímo v nabídce. Chrániče holení pro box se ale s hokejovými nenahradí, protože každé odpovídají jinému zatížení.'),
        ('Jak poznat, že chránič sedí správně?', 'Drží na místě i při pohybu, nebrání dýchání ani mluvení a nic netlačí. Ochranu otestujte při lehkém tréninku, než ji použijete při plném sparringu.'),
    ],
)

# ------------------------------------------------------------------ panske-plavky
NEW['panske-plavky'] = dict(long=True,
    title='Pánské plavky: slipy, jammery, boardshorty',
    desc='Pánské plavky slipy, jammery, trunks i boardshorty a závodní obleky. Průvodce střihem, materiálem a velikostí a nabídky českých obchodů.',
    intro='<p>Pánské plavky nejsou jedna kategorie, ale několik odlišných střihů pro odlišné situace. Na dráze v bazénu se prosazují přiléhavé slipy a jammery, na pláži volnější šortky a boardshorty a na závodech speciální startovní obleky. '
          'Správná volba záleží na tom, kde a jak často plavete, jak pohodlně se cítíte a jakou odolnost vůči chlóru potřebujete. Stejné plavky přitom nemusí fungovat všude: model na týdenní dovolenou u moře se pro denní trénink v chlorované vodě hodí jen omezeně, a naopak závodní kus není vhodný k posezení na pláži.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Speedo, Arena, Tyr, Finis, Volcom, Atlantic nebo Funky Trunks. '
          'Hodí se i <a href="/damske-plavky/">dámské plavky</a>, <a href="/detske-plavky/">dětské plavky</a>, <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plavecké čepice</a>. '
          'Níže jsou rady ke střihu, materiálu, velikosti a údržbě.</p>',
    guide='<h2>Střihy pánských plavek</h2>'
          '<p>Základní rozdíl je v délce nohavičky a těsnosti. Čím kratší a těsnější střih, tím menší odpor ve vodě, ale také menší krytí. Naopak volné šortky jsou pohodlné na pláži a dají se nosit i do vody při hrách, nehodí se však na trénink, protože při plavání bortí a zpomalují.</p>'
          + T(['Střih', 'Délka nohavičky', 'Hodí se na'], [
              ['Slipy (brief)', 'bez nohavičky', 'závodní a výkonnostní plavání, krátké tratě'],
              ['Jammery', 'po kolena nebo těsně nad ně', 'pravidelný trénink, závodění, vytrvalost'],
              ['Trunks a kraťásky', 'do půli stehna', 'rekreační plavání, bazén i pláž'],
              ['Boardshorty', 'ke kolenům nebo pod ně', 'pláž, surf, vodní hry, dovolená'],
              ['Startovní obleky', 'dlouhé nohavice, kompresní materiál', 'soutěže a vrcholový trénink']]) +
          '<h2>Materiál: chlór, tvar a rychlé schnutí</h2>'
          '<p>Plavky na pravidelné plavání v bazénu se vyplatí ušít z materiálů odolných vůči chlóru. Označení jako Endurance, PBT nebo podobné se v nabídkách u značek objevuje právě proto, že vlákno snáší chlorovanou vodu lépe než klasický elastan. '
          'Plavky z obyčejného nylonu s elastanem vypadají pěkně na dovolené, ale v chlóru ztrácejí pružnost rychleji, takže se po sezóně prodlouží nebo prosvítají.</p>'
          '<ul><li><strong>Polyesterová vlákna</strong> drží barvu i tvar, dobře odolávají chlóru a pomalu stárnou.</li>'
          '<li><strong>Nylon s elastanem</strong> je měkký a pružný, vhodný pro rekreační použití.</li>'
          '<li><strong>Boardshortové materiály</strong> jsou lehké, rychle schnou a snášejí slanou vodu a slunce.</li>'
          '<li><strong>Kompresní tkaniny</strong> v závodních oblecích zpevňují trup a snižují odpor, ale hůř se oblékají.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Velikost určuje obvod pasu, někdy i boků, a podle výrobce se liší. Klasické oblečení v konfekčních číslech neplatí; závodní značky jako Speedo nebo Arena uvádějí vlastní číselné velikosti, které neodpovídají konfekčním, takže vždy porovnejte svůj obvod s tabulkou výrobce. '
          'Plavky mají sedět těsně, ale nesmí řezat. V mokrém stavu se mírně rozšíří, takže příliš volné v suchu sjíždějí při skoku. '
          'Pokud nakupujete online, měřte obvod v pasu a přes největší část boků a zkontrolujte stahovací šňůrku nebo pás.</p>'
          '<h3>Rychlá kontrola před koupí</h3>'
          '<ul><li>Pás dobře drží i po namočení a nestahuje břicho.</li>'
          '<li>Nohavičky nezajíždějí a netlačí při dřepu.</li>'
          '<li>Podšívka v přední části je dostatečně pevná a neprosvítá.</li>'
          '<li>Šňůrka nebo vázání je dostatečně dlouhé a dá se zajistit na uzel.</li></ul>'
          '<h2>Plavky na bazén a trénink</h2>'
          '<p>Kdo plave pravidelně, dostane z jammerů a slipů nejvíc. Jammery sahají po kolena nebo těsně nad ně a drží svaly, takže se v nich plave pohodlně i při dlouhém tréninku. '
          'Slipy jsou kratší a nejméně brzdí, ale vyžadují jistotu. Pro začátečníky a rekreační plavce je rozumným kompromisem krátká nohavička. '
          'Při výběru zkontrolujte zapínání: vnitřní stahovací šňůrka v pasu drží plavky lépe než samotná guma. Doplněním výbavy jsou <a href="/plavecke-pomucky/">plavecké pomůcky</a> a <a href="/plavecke-cepice/">čepice</a>.</p>'
          '<h2>Boardshorty a plážové plavky</h2>'
          '<p>Plážové šortky, které najdete u značek jako Volcom, jsou delší a volnější, často s kapsou a zapínáním na suchý zip nebo šněrování. Hodí se na dovolenou, surfování a hry u vody. '
          'Nezapomeňte, že hustá tkanina nasákne víc než tenká, a když stejné šortky nosíte do restaurace, vybírejte barvy, které se po namočení nepoznají. '
          'Doplňky na pláž a ochranu před sluncem najdete v kategorii <a href="/plazove-doplnky/">plážové doplňky</a>, obecný přehled pak na stránce <a href="/plavky/">plavky</a>.</p>'
          '<h2>Závodní obleky a jammery pro výkon</h2>'
          '<p>Startovní obleky jsou nejtěsnější typ plavek. Pokrývají stehna, často až ke kolenům, a mají kompresní konstrukci, která drží svaly a omezuje vibrace. Oblékání trvá delší dobu a materiál se nedá tahat, proto se oblékají opatrně a bez nehtů. '
          'Obleky pro závody podléhají pravidlům federace, takže ověřte schválení pro soutěž, než ho koupíte. Pro vrcholový trénink existují i modely pro chlapce a juniory.</p>'
          '<h2>Plavky pro různé sporty ve vodě</h2>'
          '<p>Plavání není jediná disciplína. Vodní pólo vyžaduje pevné šortky s dostatečně silným švem, protože se při hře často tahá za látku. Triatlonisté nosí jednodílné či dvoudílné oblečení, které se dá použít i na kole a při běhu. '
          'Potápěči a šnorchlisté spoléhají na dlouhé šortky nebo na kompresní kalhoty, které chrání před otěrem a mírně hřejí. Kdo cvičí aquafitness, ocení volnější trunks z rychleschnoucí tkaniny. Pro každou z těchto činností platí, že švy mají být ploché, aby nedřely, a podšívka dostatečně pevná.</p>'
          + T(['Aktivita', 'Vhodný střih', 'Klíčová vlastnost'], [
              ['Plavecký trénink', 'jammery, slipy', 'odolnost chlóru, přiléhavost'],
              ['Vodní pólo', 'pevné šortky nebo jammery', 'pevné švy a odolná tkanina'],
              ['Aquafitness', 'trunks nebo kratší šortky', 'rychlé schnutí, volnost pohybu'],
              ['Dovolená u moře', 'boardshorty, trunks', 'odolnost slané vodě a slunci'],
              ['Závod', 'startovní oblek, jammery', 'komprese a splnění pravidel']]) +
          '<h2>Jak se chovat k vybavení u bazénu</h2>'
          '<p>Před vstupem do bazénu se omyjte pod sprchou, což je nejen slušnost, ale také ochrana plavek před nečistotami. Na hrubé okraje nesedejte, protože plavky se o beton zadírají. '
          'Z mokrých plavek se nevyplatí dělat pytel: po plavání je vyndejte z tašky a nechte vyschnout. Zip a suchý zip u boardshortů zavřete před praním, aby nezachytily jemnější tkaniny.</p>'
          '<h2>Péče o plavky</h2>'
          '<p>Správná péče prodlužuje životnost plavek o několik sezón. Po každém plavání opláchněte plavky ve sladké vodě, aby se odplavil chlór a sůl. Perte je ručně nebo v pračce na jemném programu při nízké teplotě. '
          'Nepoužívejte aviváž, která zalepí vlákna, a nesušte plavky na radiátoru či na přímém slunci. Plavky vyždímejte bez kroucení, rozložte na vzduchu a střídejte dva páry, pokud plavete denně.</p>'
          '<h2>Plavky pro různé postavy a pohyb</h2>'
          '<p>Každý střih sedí jinak na štíhlé, sportovní či robustnější postavě. Kdo má širší stehna, ocení delší nohavičku s pružným lemem, který neřeže, kdo má užší pas, potřebuje spolehlivé stahování uvnitř. '
          'Vyšší plavci hledají delší vnitřní švy a jammery, které sahají aspoň těsně nad koleno, a menší plavci spíš kratší trunks, aby je nohavice nepřekážely při obrátce. '
          'Pokud nosíte plavky při skocích do vody, zvolte pevnější pás a zkuste je před koupí natáhnout, abyste viděli, jak se materiál chová.</p>'
          '<h2>Jak plavky zapadají do výbavy</h2>'
          '<p>K plavkám se hodí taška s větraným oddílem na mokré věci, ručník z rychle schnoucího materiálu a pantofle do sprch. Brýle a čepice vybírejte spolu, aby se nepřekrývaly popruhy. '
          'Při pravidelném plavání se vyplatí mít dvoje plavky a střídat je: každý pár má čas důkladně vyschnout a vydrží déle. Při dovolené stačí jedny boardshorty a jedny přiléhavější plavky do hotelového bazénu.</p>'
          '<h3>Kdy se plavky vyplatí koupit</h3>'
          '<p>Nejširší výběr bývá na začátku sezóny na jaře, největší slevy se objevují po jejím konci a při výprodeji kolekcí. Kdo plave celoročně, nakupuje podle opotřebení, ne podle kalendáře. '
          'V přehledu Sporteky si lze nabídky seřadit a porovnat mezi českými obchody, aby bylo jasné, kde je právě dostupná vaše velikost.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(('speedo', 'Speedo'), ('arena', 'Arena'), ('tyr', 'Tyr'), ('finis', 'Finis'), ('volcom', 'Volcom'), ('atlantic', 'Atlantic'), ('aqua-sphere', 'Aqua Sphere'), ('funky-trunks', 'Funky Trunks')) + '. '
          'Speedo, Arena, Tyr a Finis stojí především na závodních a tréninkových modelech, Volcom na plážových šortkách a Funky Trunks nabízí výrazné vzory v trunks střihu.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Pořízení módních plavek na trénink, které chlór brzy zničí.</li>'
          '<li>Vybrání velikosti podle běžného oblečení, nikoli podle tabulky výrobce.</li>'
          '<li>Koupě příliš volných šortek na plavání, ve kterých se zpomaluje.</li>'
          '<li>Praní v pračce s aviváží a sušení na topení.</li>'
          '<li>Natahování závodního obleku silou nebo s ostrými nehty, při kterém se snadno roztrhne.</li>'
          '<li>Koupě závodního obleku bez ověření pravidel soutěže.</li></ul>'
          '<h2>Kam dál</h2>'
          '<p>K plavkám se hodí také <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-cepice/">čepice</a> a <a href="/plavecke-pomucky/">pomůcky</a>. Pro ženy a děti máte k dispozici <a href="/damske-plavky/">dámské</a> a <a href="/detske-plavky/">dětské plavky</a>, pro cestu k vodě <a href="/sportovni-tasky/">sportovní tašky</a>.</p>',
    faq=[
        ('Jaké plavky zvolit na pravidelné plavání v bazénu?', 'Přiléhavé jammery, slipy nebo krátké trunks z materiálu odolného chlóru. Vyhněte se volným šortkám, které ve vodě brzdí. Rozhodující je pohodlí pasu a to, že plavky drží i při skoku.'),
        ('Jaký je rozdíl mezi jammery a slipy?', 'Slipy nemají nohavičku a jsou nejkratší, jammery sahají po kolena nebo těsně nad ně a podpírají svaly stehen. Slipy nabízejí maximální volnost, jammery větší krytí a vyšší pohodlí při dlouhém tréninku.'),
        ('Jak poznám správnou velikost?', 'Změřte obvod pasu a boků a porovnejte s tabulkou konkrétní značky. Plavky mají sedět těsně bez řezání. U závodních obleků zvolte velikost podle návodu a počítejte s tím, že se nasazují obtížně.'),
        ('Vydrží plavky chlór?', 'Záleží na materiálu. Modely označené jako odolné chlóru vydrží daleko déle než klasické z nylonu s elastanem. Po každém plavání je ale i tak opláchněte sladkou vodou.'),
        ('Mohou boardshorty sloužit na plavání?', 'Na rekreační plavání v moři nebo v jezeře ano. Na dráhu v bazénu se nehodí, protože volná tkanina se nafoukne a brzdí. Pro trénink zvolte přiléhavější střih.'),
        ('Jak plavky prát?', 'Ručně nebo v pračce na jemný program při nízké teplotě, bez aviváže a bělidel. Nekruťte je, nežmýkejte a nesušte na radiátoru. Po každém plavání je opláchněte sladkou vodou.'),
        ('Co jsou startovní obleky?', 'Kompresní plavky s dlouhými nohavicemi určené pro závody. Zlepšují stabilitu a snižují odpor. Před koupí zkontrolujte, zda je schválila federace, ve které budete soutěžit.'),
        ('Je lepší nosit slipy, nebo jammery na tréninky?', 'Obojí je v pořádku, volí se podle pohodlí. Jammery obvykle lépe drží a vydrží déle, slipy nejméně brzdí. Mnozí plavci střídají obojí podle typu tréninku.'),
        ('Jak dlouho plavky vydrží?', 'Při pravidelném plavání několik měsíců až rok, protože chlór a tření vlákna postupně unaví. Rekreační plavky vydrží déle. Obměnit je třeba, když ztratí pružnost nebo prosvítají.'),
        ('Hodí se plavky z bazénu i na moře?', 'Ano, pokud jsou z kvalitního materiálu. Slaná voda a slunce ale vlákna také unavují, takže je po koupání vždy opláchněte sladkou vodou. Přiléhavé tréninkové plavky si na dovolenou klidně vezměte, jen nezapomeňte na krém a sušení ve stínu.'),
        ('Proč plavky prosvítají?', 'Materiál se po čase ztenčí chlórem a slunečním světlem. Pomůže plavky střídat, opláchnout je po použití a vybírat modely s podšívkou nebo hustší tkaninou.'),
    ],
)

# ------------------------------------------------------------------ jezdecke-doplnky
NEW['jezdecke-doplnky'] = dict(long=True,
    title='Jezdecké doplňky: ostruhy, kartáče, rukavice, airbagy',
    desc='Jezdecké doplňky od ostruh a bičíků po kartáče, péči o kůži, rukavice a ochranné vesty. Výběr podle disciplíny a nabídky českých obchodů.',
    intro='<p>Kromě sedla, uzdy a helmy potřebuje jezdec ještě spoustu drobností, které každodenní práci s koněm usnadňují. Ostruhy a bičíky slouží k jemné komunikaci, kartáče a hřbílka patří ke každé péči, vodítka a pomůcky usnadní práci ze země a kožený tuk prodlouží život výbavy. '
          'V této kategorii najdete také rukavice, kšiltovky, kopytní přípravky, ochranné vesty a airbagy.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Fouganza, Galop Wear, Waldhausen, Topvet, AKO, Cavalliera, Imperial Riding, Kerbl nebo Horze. '
          'Hodí se i <a href="/jezdectvi/">jezdectví</a>, <a href="/jezdecke-helmy/">jezdecké helmy</a>, <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a>, <a href="/jezdecka-obuv/">jezdecká obuv</a> a <a href="/vybaveni-pro-kone/">vybavení pro koně</a>. '
          'Přehled níže popisuje, k čemu které doplňky slouží.</p>',
    guide='<h2>Skupiny doplňků</h2>'
          '<p>Sortiment je pestrý, takže pomůže rozdělit si ho podle účelu: pomůcky pro jezdce, péče o koně a péče o výbavu. Každá skupina má jiná kritéria výběru. U věcí, které přicházejí do kontaktu s koněm, rozhoduje šetrnost k srsti a kůži, u jezdecké ochrany bezpečnost a u kožené výbavy kvalita ošetření.</p>'
          + T(['Skupina', 'Příklady', 'Na co se zaměřit'], [
              ['Pomůcky pro jezdce', 'ostruhy, bičíky, rukavice, kšiltovky', 'velikost, délka, pohodlí'],
              ['Ochrana', 'chrániče páteře, airbagy, bezpečnostní vesty', 'střih a certifikace'],
              ['Péče o koně', 'kartáče, hřbílka, kopytní přípravky', 'měkkost a účel čištění'],
              ['Práce ze země', 'vodítka, lonže, pomůcky pro trénink', 'délka a pevnost materiálu'],
              ['Péče o výbavu', 'tuky a mýdla na kůži, obaly na dečky', 'kompatibilita s materiálem'],
              ['Tréninkové pomůcky', 'chrániče šlach, zvonky', 'disciplína a pravidla soutěže']]) +
          '<h2>Ostruhy a bičíky</h2>'
          '<p>Ostruhy a bičíky jsou pomůcky, které doplňují a zjemňují komunikaci, nikoli nahrazují jezdecký sed. Správný výběr proto závisí na zkušenostech jezdce i na citlivosti koně. Začátečníci by měli konzultovat s trenérem, zda ostruhy vůbec používat. '
          'Ostruhy se liší délkou krčku a tvarem konce, a také připevněním. Kulatý hrot je jemnější než hranatý, který působí přesněji. Při nasazování dbejte, aby seděly nad patou a nepřetáčely se.</p>'
          '<ul><li><strong>Krátký krček</strong> je vhodný pro jemné zásahy a pro jezdce, kteří hledají dotek spíš než tlak.</li>'
          '<li><strong>Hranatý nebo kulatý hrot</strong> určuje, jak výrazně je zásah vnímán.</li>'
          '<li><strong>Řemínky</strong> bývají kožené nebo syntetické; důležitá je délka, aby šly zapnout přes botu.</li>'
          '<li><strong>Drezurní bičíky</strong> jsou dlouhé, jízdní kratší; rozdíl je v disciplíně.</li>'
          '<li><strong>Dětské bičíky</strong> bývají kratší a lehčí, aby je dítě udrželo.</li></ul>'
          '<p>Vždy dodržujte pravidla svého oddílu a soutěží, protože u některých disciplín jsou povolené jen určité typy. Pomůcky nikdy nepoužívejte k trestání koně.</p>'
          '<h2>Rukavice, kšiltovky a oděvní doplňky</h2>'
          '<p>Jezdecké rukavice musí udržet otěže i ve vlhku a nesmí klouzat. Zajímavé jsou modely s protiskluzovou dlaní a elastickými vsadkami, které se hodí pro drezuru i skoky. Zimní rukavice mívají podšívku, letní jsou prodyšné. '
          'Velikost se určuje podle obvodu dlaně; příliš velké rukavice se bortí, příliš malé brání cítit otěže. Kšiltovky a čepice slouží při práci ze země či při péči o koně, ale nenahrazují jezdeckou helmu. Pro jízdu vyberte helmu z kategorie <a href="/jezdecke-helmy/">jezdecké helmy</a>.</p>'
          '<h2>Ochranné vesty, chrániče páteře a airbagy</h2>'
          '<p>Ochrana těla patří k věcem, kde se nevyplatí improvizovat. Chránič páteře je vybavení s pevnými plastovými či pěnovými segmenty, které se nosí pod nebo přes oblečení a pohlcují část nárazu při pádu. '
          'Airbagová vesta se při pádu nafoukne po aktivaci lanka připevněného k sedlu a po použití je potřeba vyměnit bombičku. Proto se v nabídce objevují také náhradní bombičky do airbagu. '
          'Při výběru zkontrolujte velikost podle výšky a obvodu hrudníku, protože ochrana má sedět těsně, ale nesmí omezovat dýchání. Zapínání musí fungovat bez dlouhého nastavování. '
          'Děti a mladiství potřebují modely upravené na jejich postavu a při růstu je třeba velikost pravidelně přehodnocovat.</p>'
          '<h3>Co před koupí zjistit</h3>'
          '<ul><li>Zda se vesta hodí pro vaši disciplínu, například skoky, drezuru nebo vyjížďky v terénu.</li>'
          '<li>Zda ji váš jezdecký oddíl či soutěž povoluje.</li>'
          '<li>Jaký servis vyžaduje airbag po aktivaci a kde sehnat náhradní bombičku.</li>'
          '<li>Jak se vesta zapíná a zda ji zvládnete obléct bez cizí pomoci.</li></ul>'
          '<h2>Péče o koně: kartáče a hřbílka</h2>'
          '<p>Základem čištění je sada kartáčů, z nichž každý má jiný úkol. Tvrdý kartáč odstraní hrubou špínu a vyčeše bahno, měkký vyleští srst a dokončí práci. Hřbílko se používá k uvolnění zaschlé nečistoty z podsady a kartáč na hřívu a ocas k rozčesání. '
          'Pro mazlivé koně a koně s citlivou kůží se vyplatí měkčí štětiny. Kdo cestuje na závody, ocení kufřík či tašku, kam se sada vejde přehledně. Podobné nástroje najdete také v kategorii <a href="/vybaveni-pro-kone/">vybavení pro koně</a>.</p>'
          + T(['Nástroj', 'K čemu slouží', 'Poznámka'], [
              ['Hřbílko', 'uvolnění hrubé špíny a rozčesání srsti', 'nepoužívat na kosti a citlivá místa'],
              ['Tvrdý kartáč', 'odstranění bláta a odumřelých chlupů', 'vhodný při pelichání'],
              ['Měkký kartáč', 'vyleštění srsti', 'na závěr péče'],
              ['Kartáč na hřívu', 'rozčesání hřívy a ocasu', 'šetrně, ať se nevytrhávají chlupy'],
              ['Kopytní háček', 'čištění kopyt před jízdou i po ní', 'dbát na bezpečný postoj koně']]) +
          '<h2>Kopyta a přípravky pro kopyta</h2>'
          '<p>Zdravá kopyta jsou základem a péče o ně by měla být rutinní. Před každou jízdou kopyta vyčistěte kopytním háčkem a zkontrolujte případné poranění. Přípravky v nabídce zahrnují séra, oleje a mazadla na kopytní růžek, které pomáhají udržet jeho pružnost. '
          'Žádný přípravek nenahrazuje pravidelnou péči kováře či podkovářského mistra. Doplňky a krmivo najdete i v souvisejících sekcích značek Topvet a Kerbl.</p>'
          '<h2>Péče o kožené vybavení</h2>'
          '<p>Kůže sedel, uzdeček a popruhů vydrží roky, pokud se pravidelně ošetřuje. Po jízdě odstraňte špínu vlhkým hadříkem a na očištěnou kůži naneste glycerinové mýdlo, které ji čistí a zjemňuje. Tuk na kůži zajistí pružnost a ochranu před vlhkem. '
          'Použijte jen malé množství, protože přemazaná kůže měkne a špiní oděv. Sedla a uzdečky skladujte na suchém místě bez přímého slunce a topení.</p>'
          '<h2>Pomůcky pro práci ze země</h2>'
          '<p>Vodítka, lonže a pomůcky pro práci ze země slouží k výcviku bez jezdce. Pro práci z ruky se hodí lehčí vodítko o délce několika metrů, na lonžování delší popruh s karabinou. Vždy kontrolujte stav karabiny a švů, protože porušené materiály mohou selhat. '
          'Ochranné rukavice zabrání spálení dlaní při tahu. Chrániče šlach patří k tréninkovým pomůckám; šlachové chrániče se obvykle nosí při skokovém tréninku a v terénu.</p>'
          '<h2>Jak vybrat podle disciplíny</h2>'
          '<p>Drezurní jezdci hledají dlouhé bičíky, jemné ostruhy a elegantní rukavice. Skokani a drezuristé sázejí na ochranu šlach a pevný chránič páteře. Terénní a vyjížďkoví jezdci ocení praktické kšiltovky, vesty a kapsy. '
          'Rekreační jezdci si nejdřív pořizují základ, tedy kartáče, rukavice a bič, a pozdější nákupy podřizují potřebám konkrétního koně. Další oblečení najdete v kategorii <a href="/jezdecke-obleceni/">jezdecké oblečení</a>.</p>'
          '<h2>Stáj, vyjížďky a závody: co s sebou</h2>'
          '<p>Na vyjížďku do terénu se hodí malá taška na sedlo s kopytním háčkem, náhradním vodítkem a rukavicemi. Na závody patří navíc kufřík s kartáči, houba na ošetření kůže a sada pomůcek na rychlé čištění před startem. '
          'Ve stáji se kartáče skladují v krabici, aby se nezanášely prachem, a kožené věci visí mimo vlhké stěny. Při převozu koně v přívěsu nezapomeňte na pevné vodítko a rukavice, protože nakládání je častý moment, kdy se zvíře splaší.</p>'
          '<h3>Jak se doplňky přenášejí mezi jezdci</h3>'
          '<p>Rostoucí jezdci a děti si vybavení často půjčují nebo přebírají po sourozencích. Kartáče a nástroje na péči se předávají bez problémů, u ochranných vest a helem ale platí opatrnost: ochrana, která už něco zažila, nemusí fungovat, takže se do ní raději neinvestuje druhá ruka. '
          'Ostruhy, bičíky a rukavice lze nosit dál, pokud jsou v pořádku a sedí.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(('fouganza', 'Fouganza'), ('galop-wear', 'Galop Wear'), ('waldhausen', 'Waldhausen'), ('topvet', 'Topvet'), ('ako', 'AKO'), ('cavalliera', 'Cavalliera'), ('imperial-riding', 'Imperial Riding'), ('kerbl', 'Kerbl'), ('horze', 'Horze')) + '. '
          'Fouganza a Imperial Riding nabízejí širokou výbavu pro jezdce, Waldhausen, Kerbl a Topvet se soustředí na péči o koně a stáj, Galop Wear a Cavalliera na jezdecké oblečení a doplňky.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupě ochranné vesty bez vyzkoušení nebo bez změření hrudníku.</li>'
          '<li>Volba ostruh bez konzultace s trenérem.</li>'
          '<li>Pořízení jednoho tvrdého kartáče pro všechno, který dráždí citlivou kůži.</li>'
          '<li>Použití příliš velkého množství tuku, po kterém kůže měkne.</li>'
          '<li>Zanedbání výměny bombičky po aktivaci airbagu.</li>'
          '<li>Rukavice o číslo větší, ve kterých se nedá cítit otěž.</li></ul>'
          '<h2>Kam dál</h2>'
          '<p>Navazující nabídky najdete v kategoriích <a href="/jezdectvi/">jezdectví</a>, <a href="/jezdecka-obuv/">jezdecká obuv a chapsy</a> a <a href="/jezdecke-kalhoty/">jezdecké kalhoty a rajtky</a>.</p>',
    faq=[
        ('Jaké doplňky potřebuje začínající jezdec?', 'Pro začátek stačí helma, vhodná obuv, rukavice a základní kartáče na péči o koně. Ostruhy a další pomůcky si pořizujte až po domluvě s trenérem. Většina oddílů navíc doporučí ochrannou vestu.'),
        ('Kdy jsou ostruhy vhodné?', 'Používají se u jezdců, kteří mají klidný sed a potřebují jemně doladit komunikaci. Nejsou náhradou za výcvik ani nástrojem k donucení. Rozhodnutí patří trenérovi a pravidlům disciplíny.'),
        ('Jak vybrat jezdecké rukavice?', 'Podle velikosti dlaně a ročního období. Dlaň má mít protiskluzový povrch, švy nesmí tlačit. Letní rukavice jsou prodyšné, zimní podšité. Dobře padnoucí rukavice nesmí sklouzávat ani omezovat cit.'),
        ('Co je chránič páteře?', 'Vesta nebo pás s tvrdšími segmenty, který se nosí při jízdě a chrání zádovou část při pádu. Nenahrazuje helmu. Důležité je správně vybrat velikost a ověřit, zda ho povoluje váš oddíl.'),
        ('Jak funguje airbagová vesta?', 'Vesta je spojena lankem se sedlem. Při pádu lanko vyvolá nafouknutí vesty, která tlumí náraz. Po použití je potřeba vyměnit bombičku, proto se prodávají i náhradní.'),
        ('Jaké kartáče koupit na každodenní péči?', 'Hřbílko, tvrdý a měkký kartáč, kartáč na hřívu a kopytní háček. Pro citlivé koně vyberte měkčí štětiny. Sada, kterou lze přenášet v kufříku, se hodí na závody.'),
        ('Jak ošetřovat kožené sedlo a uzdečky?', 'Po jízdě očistěte vlhkým hadříkem, naneste glycerinové mýdlo a podle potřeby tenkou vrstvu tuku. Skladujte v suchu, mimo topení. Přemazání kůže změkčuje a mastí oblečení.'),
        ('K čemu slouží chrániče šlach?', 'Chrání končetiny koně při skocích a v terénu před nárazy a údery. Musí sedět pevně, nesmí škrtit a po jízdě se mají vyčistit. Pravidla soutěže určují, jaké typy jsou povoleny.'),
        ('Dají se doplňky půjčovat nebo dědit po jiných jezdcích?', 'Kartáče, ostruhy, rukavice a bičíky ano, pokud jsou v dobrém stavu a sedí. Ochranné vesty, airbagy a helmy po pádu už nemusí chránit, proto je lepší kupovat nové a nevěřit starému kusu s neznámou historií.'),
        ('Mohu kšiltovku nosit místo helmy?', 'Ne. Kšiltovka chrání před sluncem při práci ze země, ale při jízdě nepomůže. K jízdě používejte schválenou jezdeckou helmu, která sedí a má správně zapnutý řemínek.'),
        ('Jak často čistit kopyta?', 'Před každou jízdou i po ní, abyste odstranili kamínky a zkontrolovali poranění. Přípravky na kopyta ošetřování doplňují, ale nenahrazují kováře.'),
    ],
)

# ------------------------------------------------------------------ cyklo-kola-a-rafky
NEW['cyklo-kola-a-rafky'] = dict(long=True,
    title='Zapletená kola, ráfky a náboje na kolo',
    desc='Zapletená kola, ráfky a náboje pro horská, silniční i trekingová kola. Jak vybrat průměr, rozteč, osu a brzdy a porovnat obchody.',
    intro='<p>Zapletená kola patří k součástem jízdního kola, které ovlivní jízdu nejvíc. Rozhodují o hmotnosti, tuhosti, zrychlení i o tom, zda zvládnete nerovný terén. Ať opravujete poškozený ráfek, měníte náboj, nebo kupujete celou zapletenou sadu, musí díly sedět na rám, vidlici, brzdy i pohon. '
          'Chyba v rozměru nebo rozteči znamená, že kolo nenasadíte, a proto se vyplatí údaje porovnat ještě před objednávkou. Pomůže i fotografie starého náboje nebo popisek na boku ráfku, případně zeptejte se přímo prodejce na kompatibilitu s vaším rámem.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Shimano, Mach1, Force, Remerx, Novatec, Nexelo, Author nebo Rockbros. '
          'K výběru patří i <a href="/cyklo-dily/">díly a pláště</a>, <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklo-brzdy/">brzdy</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Níže vysvětlujeme rozměry, typy os a postup výběru.</p>',
    guide='<h2>Co všechno spadá do kategorie</h2>'
          '<p>Nabídka zahrnuje tři základní skupiny: zapletená kola, tedy hotové sady s ráfkem, špicemi a nábojem, samostatné ráfky pro přeplétání a náboje, které se používají jako předek nebo zadek. '
          'Zapletené kolo se montuje bez další práce, kdežto ráfek či náboj vyžaduje zkušeného mechanika. Zda koupit hotové kolo, nebo díly zvlášť, záleží na tom, co opravujete a jak velkou zkušenost máte.</p>'
          + T(['Díl', 'K čemu slouží', 'Kdy ho kupovat'], [
              ['Zapletené kolo', 'hotová sada připravená k nasazení', 'výměna celého kola nebo upgrade'],
              ['Ráfek', 'obruč, na kterou se montuje plášť', 'při prasknutí či deformaci obruče'],
              ['Přední náboj', 'střed předního kola, otáčí se na ložiscích', 'při vůli, zničených ložiscích či změně osy'],
              ['Zadní náboj', 'obsahuje volnoběh nebo upínání kazety', 'při změně pohonu nebo výměně volnoběhu'],
              ['Vnitřní (převodový) náboj', 'převody uvnitř náboje', 'městská a trekingová kola']]) +
          '<h2>Průměry a rozměry kol</h2>'
          '<p>Průměr kola musí odpovídat rámu, vidlici a plášťům. Nejčastější jsou 26, 27,5 a 29 palců u horských kol, u silničních a gravelových kol se používá rozměr 622 mm, označovaný jako 700C, nebo 28 palců. Dětská kola mají menší průměry od 12 do 24 palců. '
          'ISO rozměr, například 622 × 19, určuje průměr sedla pláště a šířku ráfku. Při výměně se řiďte označením na stávajícím ráfku nebo plášti, a ne odhadem podle palcových údajů.</p>'
          '<ul><li><strong>20 až 24 palců</strong> se používá na dětských a juniorských kolech.</li>'
          '<li><strong>26 palců</strong> najdete na starších horských a levnějších kolech.</li>'
          '<li><strong>27,5 palce</strong> přináší hbitější chování v technickém terénu.</li>'
          '<li><strong>29 palců</strong> lépe přejíždí překážky a drží rychlost.</li>'
          '<li><strong>622 mm (700C)</strong> je standard pro silniční, gravelová a trekingová kola.</li></ul>'
          '<h2>Typ brzd: ráfkové, nebo kotoučové</h2>'
          '<p>Brzdný systém určuje, jaké ráfky a náboje potřebujete. Ráfkové brzdy brzdí o boční stěnu ráfku, proto musí mít tuto brzdnou plochu. Kotoučové brzdy potřebují náboje s upevněním kotouče a ráfek, který brzdnou plochu mít nemusí. '
          'Kotouč se upevňuje buď šesti šrouby, nebo systémem Center Lock s drážkováním a maticí. Ráfky pro kotoučové brzdy bývají lehčí, protože nemusí odolávat tření brzdových špalků. Zkontrolujte tedy, zda koupíte kompatibilní kombinaci. Související díly najdete v kategorii <a href="/cyklo-brzdy/">brzdy a brzdové destičky</a>.</p>'
          '<h2>Osy, rozteče a uchycení</h2>'
          '<p>Častým důvodem vrácení zboží je nesprávná rozteč nebo typ osy. Moderní kola používají pevné osy, které procházejí rámem a pevně jej spojují s vidlicí. Starší kola mají rychloupínák, který se upíná skrz dutou osu. '
          'Běžná rozteč předního náboje je 100 mm; osa rychloupínáku má 9 mm, pevná osa 15 mm. Zadní náboj má rozteč 130 mm (silniční kola), 135 mm (trekingová a horská kola s rychloupínákem) nebo 142 mm (pevná osa). Boost standard rozšiřuje rozteče na 110 mm vpředu a 148 mm vzadu.</p>'
          + T(['Označení', 'Použití', 'Poznámka'], [
              ['100 × 9 mm', 'přední rychloupínák', 'klasika u starších a levnějších kol'],
              ['100 × 15 mm', 'přední pevná osa', 'tužší spojení s vidlicí'],
              ['130 × 5 mm', 'zadní rychloupínák', 'silniční kola s ráfkovými brzdami'],
              ['135 × 5 mm', 'zadní rychloupínák', 'trekingová a horská kola'],
              ['142 × 12 mm', 'zadní pevná osa', 'moderní horská kola'],
              ['110 × 15 mm a 148 × 12 mm', 'Boost', 'širší rozteče pro tužší kola']]) +
          '<p>Než něco koupíte, změřte vzdálenost mezi vidlicí a zadní stavbou a ověřte typ osy v dokumentaci kola. Nejlepší je porovnat údaje se starým nábojem, který vyndáte z kola.</p>'
          '<h2>Volnoběh a kazeta</h2>'
          '<p>Zadní náboj musí být navržený pro konkrétní sadu pastorků. Starší kola používají šroubovací věnec, dnes převládají kazetová těla pro kazetu, která se nasouvá na drážkování. Pro Shimano se používá označení HG, u moderních převodů více rychlostí existují systémy, které potřebují speciální tělo. '
          'Počet rychlostí a typ tělesa se musí shodovat s kazetou a řetězem, jinak řazení nefunguje. Další pohon najdete v kategorii <a href="/cyklo-pohon/">pohon: přehazovačky, řetězy, kazety a kliky</a>.</p>'
          '<h2>Počet špic a materiál ráfku</h2>'
          '<p>Ráfky a náboje se vyrábějí s počtem děr, obvykle 28, 32 nebo 36. Počet děr v ráfku a v náboji musí být stejný. Čím víc špic, tím pevnější a trvanlivější kolo, což se hodí pro těžší jezdce, zavazadla či terén. '
          'Nižší počet špic zlehčuje kolo, ale je méně odolný. Ráfky bývají z hliníku, který je levný a opravitelný, nebo z karbonu, který je lehčí a tužší, ale choulostivější a dražší. Pro běžné jezdce a cestování je hliník rozumnější volba.</p>'
          '<h3>Šířka ráfku a pláště</h3>'
          '<p>Vnitřní šířka ráfku musí odpovídat plášti. Příliš úzký ráfek s širokým pláštěm dělá kolo nestabilní, příliš široký ráfek zase deformuje profil pláště. Výrobci uvádějí doporučená rozmezí šířky pláště pro každý ráfek, proto je před koupí zkontrolujte. '
          'Ráfky určené pro bezdušové pláště mají speciální okraj a těsnicí pásku; více o pláštích najdete v kategorii <a href="/cyklo-dily/">díly a pláště</a>.</p>'
          '<h2>Zapletené kolo, nebo vlastní plétání</h2>'
          '<p>Hotové kolo ušetří práci a je vycentrované z výroby. Přeplétání ráfku na starý náboj dává smysl, když má náboj dobrý stav a chcete obnovit jen ráfek. Plétání vyžaduje centrovací stojan, správné špice a zkušenost. '
          'Špatně napnuté špice se uvolní, ráfek se zdeformuje nebo praskne. Pokud nemáte zkušenost, nechte kolo zaplést v servisu.</p>'
          '<h2>Péče o kola a náboje</h2>'
          '<ul><li>Pravidelně kontrolujte vůli v ložiscích a otáčení náboje.</li>'
          '<li>Nechte občas zkontrolovat napnutí špic a vycentrování.</li>'
          '<li>Po jízdě v blátě kolo omyjte a promažte jen části, které to vyžadují.</li>'
          '<li>Opotřebovaný brzdný povrch ráfku vyžaduje výměnu, jinak hrozí selhání při brzdění.</li>'
          '<li>Při transportu chraňte kotouč před ohnutím.</li></ul>'
          '<p>Údržbu usnadňují produkty z kategorie <a href="/cyklo-udrzba/">údržba kola</a> a nářadí z kategorie <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Měření a kontrola před objednávkou</h2>'
          '<p>Než zboží objednáte, udělejte si krátkou kontrolu v několika krocích. Změřte rozteč zadní stavby a vidlice, vyčtěte typ osy a prohlédněte kotouč či brzdné plochy. Na stávajícím ráfku najdete také označení výrobce a rozměru, ze kterého vyjdete při hledání náhrady. '
          'Zkontrolujte, zda je ráfek určený pro duše, nebo bezdušové pláště, a zda má ventilkový otvor odpovídající typu ventilku. Pokud kolo používáte s bočními nosiči či přívěsem, ověřte také maximální hmotnost jezdce doporučenou výrobcem kol.</p>'
          '<h3>Ventilky a pásky</h3>'
          '<p>Ráfek s hlubším profilem potřebuje delší ventilek. Ráfková páska chrání duši před hlavičkami špic; nemá-li ráfek vlastní zakrytí, bez ní duše brzy praskne. U bezdušového systému se pásku nahrazuje utěsňovací fólií a mléko slouží k vyplnění drobných průrazů.</p>'
          '<h2>Jak vybrat podle typu jízdy</h2>'
          '<p>Silniční cyklisté hledají lehká kola s vyšším profilem, gravelová kola preferují širší ráfky pro širší pláště a horská kola volí robustní ráfky a více špic. '
          'Městská a trekingová kola často používají vnitřní převodový náboj, který je chráněný před špínou a nevyžaduje seřizování přehazovačky. Děti potřebují lehká kola o menším průměru. '
          'Při úpravě kola pro zátěž, například při vození dítěte nebo zavazadel, volte odolnější ráfek a vyšší počet špic.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce nabídek mají ' + B(('shimano', 'Shimano'), ('mach1', 'Mach1'), ('force', 'Force'), ('remerx', 'Remerx'), ('novatec', 'Novatec'), ('nexelo', 'Nexelo'), ('34r', '34R'), ('rockbros', 'Rockbros'), ('author', 'Author')) + '. '
          'Shimano a Novatec jsou známé nábojem, Mach1 a Force ráfky a komplety, Remerx a Nexelo zapletená kola, Author nabízí i komplety pro vlastní značku kol.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupě nábojů bez ověření rozteče a typu osy.</li>'
          '<li>Záměna kotoučových a ráfkových brzd, a tím nekompatibilní kombinace.</li>'
          '<li>Rozdílný počet děr v ráfku a v náboji.</li>'
          '<li>Neověření kazety, volnoběhu a počtu rychlostí.</li>'
          '<li>Výběr příliš lehkého ráfku pro těžší jezdce.</li>'
          '<li>Plétání bez zkušeností a bez stojanu na centrování.</li></ul>'
          '<h2>Kam dál</h2>'
          '<p>K výbavě patří také <a href="/cyklo-riditka/">řídítka, představce a sedlovky</a>, <a href="/cyklo-pedaly/">pedály</a>, <a href="/cyklo-blatniky/">blatníky</a> a <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>. Širší přehled nabízí stránka <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>.</p>',
    faq=[
        ('Jak poznám, jaký ráfek potřebuji?', 'Odečtěte označení z boku ráfku nebo pláště, například 622 × 19, a zkontrolujte typ brzd a počet děr. Ráfek musí odpovídat průměru kola, šířce pláště a brzdnému systému.'),
        ('Jaký je rozdíl mezi 622 mm a 700C?', 'Jde o stejný rozměr. Označení 622 mm je přesná hodnota průměru sedla pláště, 700C je tradiční označení. Stejný rozměr se označuje také jako 28 palců, i když se nejedná o skutečný průměr.'),
        ('Co je rozteč náboje?', 'Vzdálenost mezi vnějšími hranami matic nebo osy, kterou rám či vidlice drží. Typicky 100 mm vpředu a 135 nebo 142 mm vzadu. Špatná rozteč znamená, že kolo nelze nasadit.'),
        ('Čím se liší rychloupínák a pevná osa?', 'Rychloupínák prochází dutým nábojem a upíná se pákou, pevná osa je tlustší a našroubuje se do vidlice. Pevná osa dává tužší spojení a používá se na moderních kolech. Typ osy nelze libovolně měnit.'),
        ('Jak vybrat náboj pro kotoučovou brzdu?', 'Zjistěte, zda kotouč drží šest šroubů, nebo systém Center Lock. Náboj musí mít odpovídající upevnění a také správnou rozteč a osu. Ověřte rovněž, zda se hodí k pohonu.'),
        ('Kolik špic má mít ráfek?', 'Většinou 28, 32 nebo 36. Počet v ráfku a v náboji se musí shodovat. Více špic znamená odolnější kolo, což se hodí pro těžší jezdce a terén, méně špic je lehčí.'),
        ('Hodí se karbonové ráfky pro každého?', 'Karbon je lehký a tuhý, ale choulostivější vůči nárazům a dražší. Pro běžnou jízdu a cestování bývá rozumnější hliník, který je odolnější a opravitelný.'),
        ('Mohu na ráfek dát libovolně široký plášť?', 'Ne. Výrobce ráfku uvádí rozmezí šířek, pro které je profil správný. Příliš úzký plášť na širokém ráfku nebo naopak snižují stabilitu a bezpečnost.'),
        ('Kdy vyměnit celé kolo místo ráfku?', 'Když jsou náboj i ráfek opotřebované nebo když chcete změnit systém, například přejít na kotoučové brzdy. Výměna jednotlivých dílů se vyplatí, pokud je zbytek kola v dobrém stavu.'),
        ('Pasují ráfky z různých značek k nábojům Shimano?', 'Ano, pokud se shoduje počet děr, typ brzd a rozměry. Značka sama o sobě nerozhoduje, ale kompatibilita. U kotoučových nábojů navíc ověřte typ upevnění kotouče a u zadních typ volnoběhu a osy.'),
        ('Jak často nechat kola vycentrovat?', 'Po prvních stovkách kilometrů a poté podle jízdy, například ročně či při viditelném házení. Kolo se centruje hlavně po nárazu nebo uvolnění špic. Servis ji vyřeší rychle.'),
    ],
)
