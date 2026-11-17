"""sporteka.cz — wave 29b (17. 11. 2026): long texts for mikiny-na-zip, mikiny-s-kapuci, jednorucni-cinky, cestovni-tasky.
General true facts only, no prices, no product counts. Product lines (Nike Tech Fleece, Adidas Firebird/SST, Puma T7, UA Rival,
Champion Reverse Weave, TNF Base Camp Duffel, Osprey Transporter/Daylite, Deuter Duffel Pro, Gregory Alpaca, Eagle Creek Pack-It)
named only in general terms; airline cabin baggage limits not quoted — they differ per airline. Children's drawstring rule mentioned
without the standard number. Brands linked only if present in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ mikiny-na-zip
NEW['mikiny-na-zip'] = dict(long=True,
    title='Mikiny na zip: s kapucí, se stojáčkem i sportovní',
    desc='Mikina na zip s kapucí i bez, sportovní track top, fleecová nebo technická. Jak vybrat zip, materiál a střih a porovnat nabídky českých e-shopů.',
    intro='<p><strong>Mikina na zip</strong> se propíná odshora dolů, takže se obléká a svléká jako lehká bunda. To je její hlavní výhoda proti mikině přes hlavu: když se zahřejete, stačí ji rozepnout, a nemusíte si kvůli tomu cuchat vlasy ani sundávat čepici. Celopropínací mikiny se prodávají s kapucí i bez ní, se stojáčkem, jako sportovní track top s lampasy, ve fleecovém i technickém provedení. Nosí se na trénink, na výlet, do města i doma. Při výběru rozhoduje hlavně materiál, protože bavlněná mikina se chová úplně jinak než fleecová nebo funkční.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých obchodů u jednotlivých modelů a objednávku pak dokončíte v e-shopu, který si vyberete. Zastoupeny jsou značky ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('nike', 'Nike'), ('under-armour', 'Under Armour'), ('gap', 'Gap')) + ', Jack Wolfskin nebo Napapijri. Mikiny na zip patří do kategorie <a href="/mikiny/">mikiny</a>; přes hlavu se obléká většina modelů v kategorii <a href="/mikiny-s-kapuci/">mikiny s kapucí</a>, na hory se hodí <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>',
    guide='<h2>Typy mikin na zip</h2>'
          '<p>Pod jedním názvem se skrývají kusy, které by v šatníku jen těžko zastoupily jeden druhý. Bavlněná mikina s kapucí je na volný čas, track top s lesklým povrchem k teplákům, fleecová mikina je hřejivá vrstva pod bundu a technická mikina patří na sport.</p>'
          + T(['Typ', 'Typický materiál', 'Kdy se hodí'], [
              ['Mikina na zip s kapucí', 'bavlna nebo směs bavlny s polyesterem', 'každý den, cestování, chladnější večery'],
              ['Mikina se stojáčkem', 'bavlněná směs, úplet, fleece', 'pod bundu, do kanceláře, na kolo'],
              ['Track top (sportovní mikina)', 'polyesterový trikot s hladkým povrchem', 'k teplákové soupravě, retro styl'],
              ['Fleecová mikina na zip', 'polyesterový fleece', 'turistika, hory, střední vrstva'],
              ['Technická mikina', 'pružný funkční úplet, mřížkový fleece', 'běh, skialpy, trénink venku'],
              ['Zateplená mikina', 'podšívka z beránku nebo flauše', 'zima, místo lehké bundy']]) +
          '<h2>Na zip, nebo přes hlavu</h2>'
          '<p>Celopropínací mikina lépe reguluje teplotu. Při chůzi do kopce ji rozepnete, na vrcholu zase zapnete až ke krku, a když slunce svítí víc, sundáte ji bez zastavení. Přes rozepnutou mikinu je vidět tričko, takže se snadno kombinuje. Mikina přes hlavu má zase klidnější vzhled bez kovového pruhu uprostřed, často velkou klokaní kapsu a víc se hodí jako samostatný kousek na volný čas. Mezi oběma stojí mikiny se zipem jen ke hrudníku, kterým se říká half zip nebo quarter zip. Obléknou se přes hlavu, ale u krku se dají větrat.</p>'
          '<h2>Zip: maličkost, která rozhoduje</h2>'
          '<p>Zip je nejvíc namáhaná část mikiny a také ta, která se nejčastěji pokazí. Spirálový plastový zip je lehký, ohebný a v zimě nestudí, kovový zip vypadá masivněji a k bavlněným mikinám se hodí stylově. U kvalitnějších mikin bývají zipy renomovaných výrobců, například YKK, a jezdec jde hladce bez zadrhávání. Pomůže prohlédnout fotografie detailů nebo popis produktu.</p>'
          '<ul><li><strong>Dvoucestný zip</strong> se dá rozepnout i zespodu. Hodí se u delších mikin, při jízdě na kole a při sezení v autě.</li>'
          '<li><strong>Garáž zipu</strong> je malý látkový kryt nahoře, který chrání bradu před studeným kovem a třením.</li>'
          '<li><strong>Kryt zipu zevnitř</strong> zabraňuje, aby zip nepříjemně tlačil a aby jím táhlo.</li>'
          '<li><strong>Kapsy na zip</strong> udrží klíče a telefon, i když se při sportu ohýbáte.</li></ul>'
          '<h2>Materiály a gramáž</h2>'
          '<p>Bavlněné mikiny se pletou nejčastěji ze dvou druhů úpletu. Teplákovina s počesaným rubem je uvnitř měkká a chlupatá a hřeje víc. French terry má na rubu drobné smyčky, je vzdušnější a hodí se do přechodného období. Směs bavlny s polyesterem méně sráží, rychleji schne a déle drží barvu. Údaj o gramáži, tedy hmotnosti látky na metr čtvereční, prozradí, jak hutná mikina bude: čím vyšší číslo, tím těžší a teplejší úplet.</p>'
          '<p>Track topy jsou z hladkého polyesterového trikotu, který se nemačká, nežmolkuje a dobře snáší praní. Technické mikiny bývají z pružných syntetických úpletů, které odvádějí pot a rychle schnou. Mřížkový fleece má na rubu drobné čtverečky, mezi kterými proudí vzduch, a je proto lehčí a prodyšnější než klasický fleece. Na nejchladnější dny se vyplatí také <a href="/merino-mikiny/">merino mikiny</a>, vlna hřeje i ve vlhku a nezapáchá.</p>'
          '<h2>Známé řady velkých značek</h2>'
          '<p>Mnoho mikin na zip se hledá přímo podle názvu řady. Adidas Originals má klasické track topy Firebird a SST se třemi pruhy na rukávech, které patří k retro teplákovým soupravám. Nike Tech Fleece je řada z hladkého oboustranného úpletu s přiléhavějším střihem a typickými kapsami na zip. Puma nabízí track topy řady T7 s lampasem na rukávu. Under Armour prodává mikiny na zip například v řadě Rival Fleece z měkké bavlněné směsi. Outdoorové značky jako Jack Wolfskin vsázejí hlavně na fleece a technické materiály, Napapijri a Gap spíš na městský styl s výrazným logem. Při výběru podle řady si ale vždy přečtěte, z čeho je konkrétní kus ušitý, protože se materiály mezi sezónami mění.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Střihy se liší i u stejné značky. Slim fit přiléhá k tělu a hodí se pod bundu, regular je klasický, oversized má spadlá ramena a volnější trup. Mikinu na zip nosíte často rozepnutou, takže se volnější střih nepozná tolik jako u mikiny přes hlavu. Pokud chcete mikinu nosit pod <a href="/softshellove-bundy/">softshellovou bundu</a>, vyberte užší střih bez objemné kapuce, jinak se pod bundou zmačká. Sledujte i délku rukávů: s manžetou z pružného úpletu se rukáv dá vyhrnout, bez ní zůstane přes zápěstí.</p>'
          '<p>Velikostní tabulky jednotlivých značek se liší, proto porovnávejte šířku přes hrudník a délku zad s mikinou, kterou už máte a která vám sedí. Bavlněné mikiny se mohou po prvním praní trochu srazit, směsi a polyester skoro vůbec.</p>'
          '<h2>Mikina na sport, nebo na každý den</h2>'
          '<p>Na běh, kolo nebo skialpy se hodí technická mikina, která odvádí pot a rychle schne. Bavlna při sportu nasákne, ztěžkne a na větru studí. Do posilovny poslouží jak bavlněná mikina na rozcvičení, tak lehký track top. Na každý den, do školy a na cesty je pohodlná klasická mikina s kapucí na zip. K tréninku i volnu ji lze doplnit <a href="/teplaky/">tepláky</a>, sladěný komplet najdete mezi <a href="/teplakove-soupravy/">teplákovými soupravami</a>.</p>'
          '<h2>Mikina na zip jako vrstva v zimě</h2>'
          '<p>V chladných měsících se mikina na zip stává střední vrstvou. Nosí se mezi funkčním tričkem a bundou a díky zipu se dá v teple obchodu nebo v tramvaji rychle rozepnout, aniž byste museli svlékat bundu. Pro tento účel je lepší tenčí mikina bez velké kapuce, která by se pod límcem bundy hrnula. Na lyže nebo běžky se hodí fleecová či technická mikina, protože bavlna po zpocení v mrazu nepříjemně studí. Pokud mikinu potřebujete i jako samostatnou vrstvu na podzimní procházky, zvolte zateplenou variantu s podšívkou nebo silnější teplákovinu, která udrží teplo i ve větru.</p>'
          '<p>Mikina na zip s kapucí se hodí také na cesty. V letadle nebo ve vlaku, kde se teplota mění podle klimatizace, ji podle potřeby rozepnete nebo přetáhnete kapuci přes hlavu a použijete jako polštář.</p>'
          '<h2>Dětské mikiny na zip</h2>'
          '<p>Dětem se mikina na zip obléká snadněji než mikina přes hlavu, zvlášť těm menším, které se ještě neumějí samy svlékat. Hodí se zip s velkým jezdcem nebo poutkem, které se dá chytit i v rukavicích. U mikin pro menší děti výrobci podle bezpečnostních pravidel nedávají do kapuce a kolem krku šňůrky, aby se dítě nemohlo zachytit na prolézačce. Kupujte s malou rezervou, ne však tak velkou, aby rukávy zakrývaly dlaně.</p>'
          '<h2>Péče a praní</h2>'
          '<ul><li><strong>Zip zapnout:</strong> před praním mikinu zapněte až nahoru, rozepnutý zip v bubnu trhá jiné prádlo a ničí vlastní látku.</li>'
          '<li><strong>Naruby:</strong> chrání potisk a výšivku a omezuje tvorbu žmolků na lícní straně.</li>'
          '<li><strong>Bez aviváže u funkčních materiálů:</strong> aviváž zanáší vlákna a funkční mikina pak hůř odvádí pot.</li>'
          '<li><strong>Šetrné sušení:</strong> sušička bavlnu sráží a fleece může ztratit objem, pověšená mikina vydrží déle.</li>'
          '<li><strong>Zadrhávající zip:</strong> pomůže ho vyčistit kartáčkem a přejet tužkou nebo voskem.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Bavlněná mikina na sport, při kterém se hodně potíte.</li>'
          '<li>Objemná mikina s kapucí pod úzkou bundu.</li>'
          '<li>Výběr jen podle písmena velikosti bez pohledu do tabulky.</li>'
          '<li>Mikina s levným zipem, který se rozjede po první sezóně.</li>'
          '<li>Praní s rozepnutým zipem.</li></ul>'
          '<h2>Jak nakoupit přes Sporteku</h2>'
          '<p>U každé mikiny vidíte, které obchody ji mají v nabídce a ve kterých velikostech. Oblíbené barvy a velikosti mizí jako první, proto se vyplatí sledovat více e-shopů zároveň. Před objednávkou porovnejte i dopravu a podmínky vrácení; nákup dokončíte přímo v obchodě. Lehčí mikiny na trénink najdete také v kategorii <a href="/funkcni-mikiny/">funkční mikiny</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi mikinou na zip a mikinou přes hlavu?', 'Mikina na zip se propíná po celé délce a obléká se jako bunda, takže se snadno větrá a svléká. Mikina přes hlavu nemá zip vpředu, bývá s klokaní kapsou a hodí se spíš na volný čas.'),
        ('Co je track top?', 'Sportovní mikina na zip z hladkého polyesterového trikotu, obvykle se stojáčkem a pruhy na rukávech. Typickým příkladem jsou řady Adidas Firebird a SST nebo Puma T7.'),
        ('Je lepší kovový, nebo plastový zip?', 'Spirálový plastový zip je lehký, pružný a v zimě nestudí. Kovový působí masivněji a k bavlněným mikinám se hodí vzhledem. Důležitější než materiál je kvalita jezdce a zubů.'),
        ('Co znamená dvoucestný zip?', 'Zip se dvěma jezdci, který se dá rozepnout shora i zespodu. Ocení ho cyklisté a ti, kdo v mikině dlouho sedí.'),
        ('Sráží se mikina na zip po praní?', 'Bavlněné mikiny se mohou trochu srazit, hlavně v sušičce. Směsi s polyesterem a syntetické mikiny drží rozměr lépe.'),
        ('Jakou mikinu na zip na hory?', 'Fleecovou nebo technickou mikinu z rychleschnoucího materiálu, ideálně se stojáčkem. Bavlna na horách po zpocení studí.'),
        ('Prodává Sporteka mikiny přímo?', 'Ne, Sporteka porovnává nabídky českých e-shopů. Objednávku dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ mikiny-s-kapuci
NEW['mikiny-s-kapuci'] = dict(long=True,
    title='Mikiny s kapucí: klokanky, oversized i týmové',
    desc='Mikina s kapucí přes hlavu, oversized mikina, klokanka, týmová NFL a NHL i technická mikina s kapucí. Jak vybrat střih, materiál a velikost.',
    intro='<p><strong>Mikina s kapucí</strong>, anglicky hoodie, je nejrozšířenější mikinou vůbec. Klasika přes hlavu s velkou klokaní kapsou na břiše se nosí do školy, na trénink i na víkend a mnoho lidí jich má v šatníku několik. Vedle ní se prodávají volné oversized mikiny se spadlými rameny, týmové mikiny s logy klubů NFL, NHL nebo NBA a technické mikiny s přiléhavou kapucí, které na horách slouží jako hřejivá vrstva pod bundu. Liší se materiálem, střihem i tím, jak dlouho vydrží vypadat jako nové. Než začnete vybírat, ujasněte si, zda mikinu chcete hlavně na volný čas, na sport, nebo jako dárek pro fanouška.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů a nakoupíte přímo v obchodě, který vám nejvíc vyhovuje. V kategorii najdete například značky ' + B(('under-armour', 'Under Armour'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('lacoste', 'Lacoste'), ('dynafit', 'Dynafit'), ('champion', 'Champion')) + '. Nadřazenou kategorií jsou <a href="/mikiny/">mikiny</a>, celopropínací modely najdete mezi <a href="/mikiny-na-zip/">mikinami na zip</a> a na trénink se hodí <a href="/funkcni-mikiny/">funkční mikiny</a>.</p>',
    guide='<h2>Druhy mikin s kapucí</h2>'
          '<p>Většina mikin s kapucí se obléká přes hlavu. Liší se hlavně střihem a tím, k čemu jsou určené. Podle toho se také vybírá materiál.</p>'
          + T(['Typ', 'Co ho odlišuje', 'Kdy se hodí'], [
              ['Klokanka', 'mikina přes hlavu s velkou kapsou na břiše', 'každý den, škola, volný čas'],
              ['Oversized mikina', 'volný trup, spadlá ramena, delší rukávy', 'streetwear, pohodlí doma i venku'],
              ['Zkrácená mikina', 'kratší délka nad pasem', 'k vysokým leginám a kalhotám'],
              ['Týmová licencovaná', 'logo klubu a ligy, oficiální licence', 'fanoušci, dárky'],
              ['Technická mikina s kapucí', 'přiléhavý střih, funkční úplet, kapuce pod helmu', 'hory, běh, skialpy'],
              ['Zateplená mikina', 'podšívka z beránku nebo silná teplákovina', 'zima, místo lehké bundy']]) +
          '<h2>Oversized mikina: jak vybrat velikost</h2>'
          '<p>Oversized mikina je záměrně volná. Má široký trup, ramenní švy posazené níž na pažích a často delší rukávy, které se shrnují u zápěstí. Pokud je mikina v popisu označená jako oversized, nekupujte ji o číslo nebo dvě větší, výrobce s volností už počítal. Větší velikost má smysl jen u klasického střihu, ze kterého chcete volný vzhled udělat sami. V takovém případě ale počítejte s tím, že se prodlouží i rukávy a délka a mikina může zakrývat polovinu stehen.</p>'
          '<p>Rozhodující jsou rozměry v tabulce: šířka přes hrudník, délka od ramene a délka rukávu. Nejjednodušší je změřit oblíbenou mikinu, kterou máte doma, a porovnat ji s údaji obchodu. U oversized střihu se zaměřte hlavně na délku, protože právě ta rozhoduje, zda mikina působí záměrně volně, nebo jen o několik čísel větší.</p>'
          '<h2>Kapuce, šňůrky a kapsy</h2>'
          '<p>Kvalitní kapuce bývá dvouvrstvá, takže drží tvar a nepadá do očí. Šňůrky umožní kapuci stáhnout ve větru, někteří výrobci je ale vynechávají kvůli čistšímu vzhledu. Klokaní kapsa je na zahřátí rukou a drobnosti, na telefon a klíče je jistější kapsa na zip. Technické mikiny mají přiléhavou kapuci, která se dá nosit pod přilbou, a otvory na palce v manžetách, díky nimž se rukáv při pohybu neshrnuje.</p>'
          '<h2>Materiál a gramáž</h2>'
          '<p>Běžné mikiny jsou z bavlny nebo ze směsi bavlny s polyesterem. Počesaný rub je měkký a teplý, smyčkový rub francouzského froté je lehčí a dýchá. Silnější mikiny s vyšší gramáží drží tvar, nevytahají se v loktech a působí luxusněji, ale déle schnou. Čistá bavlna je příjemná na kůži, víc se ale sráží a snáz se vytahá. Polyesterová složka přidá odolnost proti žmolkování a stálost barev.</p>'
          '<p>Zvláštní konstrukci mají mikiny Champion Reverse Weave. Látka je v nich otočená tak, aby vlákna vedla napříč, a díky tomu se mikina po praní méně sráží do délky. Po stranách bývají pružné vsadky, které usnadňují pohyb. Technické mikiny značek jako Dynafit nebo Under Armour jsou z polyesterových a pružných úpletů, které odvádějí pot, rychle schnou a nemačkají se.</p>'
          '<h2>Jak poznat kvalitní mikinu</h2>'
          '<p>Na fotografii vypadají mikiny podobně, rozdíl se ukáže až po několika praních. Kvalitní mikina má pevně všité manžety a spodní lem z pružného žebrového úpletu, který se po čase nevytahá do tvaru zvonu. Švy jsou rovné, bez volných nití, a na ramenou bývají zpevněné páskou. Kapuce drží tvar, protože je ušitá ze dvou vrstev. U levných mikin se často po pár týdnech objeví žmolky, potisk začne praskat a dolní lem se zvlní.</p>'
          '<p>Pomůže přečíst složení a gramáž v popisu produktu, případně recenze zákazníků v e-shopu, kteří o mikině píšou i po delším nošení. U potisku je odolnější výšivka nebo kvalitní sítotisk než tenký nažehlovaný obrázek, který se po čase loupe.</p>'
          '<h2>Mikina s kapucí, nebo na zip?</h2>'
          '<p>Mikina přes hlavu působí uceleně, nic na ní nezvoní ani netlačí a velká kapsa na břiše je pohodlná na zahřátí rukou. Hodí se jako samostatný kus oblečení na podzim a jaro nebo doma. Celopropínací modely v kategorii <a href="/mikiny-na-zip/">mikiny na zip</a> se zase rychleji svlékají a lépe regulují teplotu, a proto se víc hodí pod bundu a na sport. Mnoho lidí má v šatníku obojí: klokanku na volno a mikinu na zip na cesty a trénink.</p>'
          '<h2>Týmové mikiny NFL, NHL a NBA</h2>'
          '<p>Velkou skupinu tvoří licencované mikiny s logy amerických klubů. Oficiální licenci nese například ' + B(('fanatics', 'Fanatics')) + ', retro mikiny se starými logy klubů prodává ' + B(('mitchell-ness', 'Mitchell &amp; Ness')) + ' a dětské a juniorské velikosti často ' + B(('outerstuff', 'Outerstuff')) + '. Licencovaný kus má na sobě oficiální logo ligy i týmu a výrobce za jeho použití platí. Při výběru dárku si ověřte nejen tým, ale také to, zda nejde o dámský nebo dětský střih. Hokejoví fanoušci najdou další oblečení v kategorii <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>, týmové kšiltovky mezi <a href="/ksiltovky/">kšiltovkami</a>.</p>'
          '<h2>Mikina s kapucí na hory a sport</h2>'
          '<p>Na túru nebo skialpy patří technická mikina, ne bavlněná. Bavlna nasákne potem a na větru na hřebeni rychle prochladne. Technická mikina s kapucí slouží jako střední vrstva: pod ní je funkční tričko, nad ní větrovka nebo nepromokavá bunda. Kapuce ochrání krk a hlavu při zastávce, pod přilbou nahradí tenkou čepici. Na běh v zimě se hodí lehký model s přiléhavou kapucí a reflexními prvky. Do posilovny poslouží i obyčejná klokanka na rozcvičení, během tréninku ji ale většina lidí stejně svlékne.</p>'
          '<h2>Dětské mikiny s kapucí</h2>'
          '<p>Dětské mikiny pro menší děti se podle bezpečnostních pravidel šijí bez šňůrek v kapuci a v oblasti krku. Šňůrka by se mohla zachytit na skluzavce nebo ve dveřích autobusu. Pokud máte starší mikinu se šňůrkou a dáváte ji menšímu dítěti, šňůrku vytáhněte. U dětí se vyplatí odolná směs bavlny s polyesterem, která vydrží časté praní, a zesílené lokty.</p>'
          '<h2>Mikina s kapucí jako dárek</h2>'
          '<p>Mikina s kapucí patří k nejčastějším dárkům, protože se nosí v každém věku. Pokud neznáte přesnou velikost, sáhněte spíš po volnějším střihu, menší mikina se nosí hůř než o něco větší. Užitečné je zjistit, jaký střih obdarovaný nosí, a podívat se na štítek mikiny, kterou už má. Barva je bezpečnější v neutrálních odstínech, výrazné barvy a velká loga jsou otázkou vkusu. Pro fanoušky jsou dobrou volbou týmové mikiny oblíbeného klubu, pro sportovce technická mikina od značky, kterou už znají.</p>'
          '<h2>Barvy a potisky</h2>'
          '<p>Tmavé barvy jako černá, tmavě modrá nebo šedý melír se nosí nejčastěji, protože se snadno kombinují a skryjí drobné skvrny. Světlé mikiny působí svěže, ale na manžetách a kapse se na nich dřív ukáže špína. Šedý melír má navíc tu nevýhodu, že je na něm vidět pot v podpaží a na zádech, proto ho na trénink volí méně lidí. U potisků zvažte, zda se má mikina nosit i za pár let. Velké sezonní motivy rychle zestárnou, malé logo na hrudi nebo výšivka vydrží v módě déle.</p>'
          '<h2>Jak mikinu prát, aby vydržela</h2>'
          '<ul><li><strong>Naruby a s podobnými barvami:</strong> tmavé mikiny pouštějí barvu hlavně při prvních praních.</li>'
          '<li><strong>Nižší teplota:</strong> většině mikin stačí třicet stupňů, potisk pak déle vydrží.</li>'
          '<li><strong>Žmolky:</strong> vznikají třením o batoh a pásek. Odstraní je žmolkovač, neodstraní je ale navždy.</li>'
          '<li><strong>Bez sušičky:</strong> horko bavlnu sráží a potisk praská.</li>'
          '<li><strong>Šňůrky v kapuci:</strong> před praním zavažte konce, aby se nevytáhly.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Oversized mikina koupená ještě o dvě čísla větší.</li>'
          '<li>Bavlněná mikina jako jediná vrstva na horskou túru.</li>'
          '<li>Týmová mikina v jiném střihu, než obdarovaný nosí.</li>'
          '<li>Mikina se šňůrkami pro malé dítě.</li>'
          '<li>Tenká mikina s nízkou gramáží v očekávání zimního tepla.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>U každé mikiny vidíte nabídky obchodů vedle sebe a podle dostupných velikostí poznáte, kde je vaše číslo skladem. Objednávku dokončíte v e-shopu a vrácení se řídí jeho podmínkami. Hřejivou alternativu na chladné dny nabízejí <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>',
    faq=[
        ('Co je klokanka?', 'Mikina s kapucí přes hlavu, která má na břiše velkou společnou kapsu pro obě ruce. Je to nejrozšířenější typ mikiny s kapucí.'),
        ('Mám oversized mikinu kupovat o číslo větší?', 'Ne, pokud je střih označený jako oversized. Výrobce už volnost do střihu započítal. Větší číslo dává smysl jen u klasického střihu, ze kterého chcete volnější vzhled.'),
        ('Co znamená gramáž mikiny?', 'Hmotnost látky na metr čtvereční. Čím vyšší, tím hutnější a teplejší úplet, který lépe drží tvar.'),
        ('Proč dětské mikiny nemají šňůrky?', 'Šňůrka v kapuci nebo u krku by se mohla zachytit na prolézačce či ve dveřích, a proto ji bezpečnostní pravidla u mikin pro menší děti nepřipouštějí.'),
        ('Je bavlněná mikina vhodná na hory?', 'Jako jediná vrstva ne. Bavlna nasákne potem a na větru studí. Na hory vyberte technickou nebo fleecovou mikinu.'),
        ('Jak poznám licencovanou týmovou mikinu?', 'Nese oficiální logo ligy a týmu a prodávají ji zavedené značky jako Fanatics, Mitchell &amp; Ness nebo Outerstuff. Výrobce za licenci platí lize.'),
        ('Jaká mikina s kapucí se hodí pod bundu?', 'Tenčí mikina s užším střihem a jednovrstvou kapucí, která se pod límcem bundy nehrne. Objemná oversized klokanka se pod úzkou bundou zmačká a omezuje pohyb.'),
        ('Co je Champion Reverse Weave?', 'Mikina, u které je úplet otočený tak, aby vlákna vedla napříč. Díky tomu se po praní méně sráží do délky. Po stranách mívá pružné vsadky pro volnější pohyb.'),
        ('Jak zabránit žmolkování mikiny?', 'Perte ji naruby, s podobnými látkami a bez sušičky. Odolnější proti žmolkům bývají směsi s polyesterem než čistá bavlna.'),
    ])

# ------------------------------------------------------------------ jednorucni-cinky
NEW['jednorucni-cinky'] = dict(long=True,
    title='Jednoruční činky: pevné, nakládací, hexagon i chrom',
    desc='Jednoruční činky pevné i nakládací, gumové hexagon, chromové, neoprenové a PU. Jak zvolit hmotnost, systém a stojan a porovnat nabídky e-shopů.',
    intro='<p><strong>Jednoruční činky</strong> jsou nejuniverzálnější zátěží pro posilování doma i v posilovně. Cvičí se s nimi tlaky, přítahy, výpady, dřepy i izolované cviky na paže a ramena, každou rukou zvlášť, takže se snadno odhalí rozdíl mezi silnější a slabší stranou. Na rozdíl od velké osy zaberou málo místa a dají se uklidit pod postel nebo do stojanu v rohu pokoje. Pár jednoruček stačí na celotělový trénink, a proto s nimi začíná většina domácích posiloven.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a nakoupíte v e-shopu, který si vyberete. Najdete tu pevné jednoručky v gumové, chromové, neoprenové nebo polyuretanové úpravě i nakládací činky s kotouči, například od značek ' + B(('hms', 'HMS'), ('insportline', 'inSPORTline')) + ', Sharp Shape, Sportago nebo Gorilla Sports. Jednoručky patří do kategorie <a href="/cinky-a-kotouce/">činky a kotouče</a>, k uložení slouží <a href="/stojany-na-cinky/">stojany na činky</a> a ke cvičení vleže <a href="/posilovaci-lavice/">posilovací lavice</a>.</p>',
    guide='<h2>Pevné, nebo nakládací jednoručky</h2>'
          '<p>Základní rozhodnutí je, zda chcete činky s pevnou hmotností, nebo činky, jejichž hmotnost si měníte sami. Pevná jednoručka je hned připravená, nic se na ní neuvolní a mezi cviky stačí sáhnout po jiném páru. Pro rostoucí sílu ale potřebujete víc párů a ty zaberou místo. Nakládací činka má krátkou tyč, na kterou nasazujete kotouče a zajistíte je maticí nebo rychloupínací objímkou. Jedna sada tak nahradí mnoho párů pevných činek.</p>'
          + T(['Systém', 'Výhody', 'Nevýhody'], [
              ['Pevné jednoručky', 'okamžitě připravené, bezpečné, odolné', 'pro každou hmotnost další pár, zabírají místo'],
              ['Nakládací se šroubovací maticí', 'jemné odstupňování, rozšiřitelné dalšími kotouči', 'výměna kotoučů zabere čas, matici je třeba dotahovat'],
              ['Nakládací s rychloupínací objímkou', 'rychlejší výměna než u matice', 'objímka musí sedět k průměru tyče'],
              ['Nastavitelné s voličem', 'změna hmotnosti otočením nebo zasunutím voliče', 'objemnější tvar, mechanismus nesnese pády'],
              ['Sada v kufříku', 'tyče a kotouče pohromadě, snadné uklizení', 'omezený rozsah hmotností']]) +
          '<p>Pro začátky doma je praktická sada nakládacích činek nebo několik párů pevných jednoruček v nižších hmotnostech. Kdo cvičí pravidelně a chce rychle přecházet mezi cviky a sériemi, ocení pevné činky ve stojanu nebo nastavitelné činky s voličem, u kterých se hmotnost změní během několika vteřin.</p>'
          '<h2>Materiály a povrch</h2>'
          '<ul><li><strong>Gumové hexagonové činky</strong> mají šestihranné hlavy z litiny potažené gumou. Neodvalují se po podlaze, tlumí nárazy a dají se použít i jako opora při kliku. Nová guma může zpočátku výrazně vonět, zápach během týdnů na vzduchu slábne.</li>'
          '<li><strong>Polyuretanové (PU) činky</strong> jsou odolnější proti oděru a praskání než guma a skoro nezapáchají. Najdete je hlavně v lépe vybavených posilovnách.</li>'
          '<li><strong>Chromové činky</strong> jsou kompaktní a lesklé. Bývají v nižších hmotnostech pro aerobic a cviky na paže, při pádu ale poškodí podlahu.</li>'
          '<li><strong>Neoprenové a vinylové činky</strong> jsou lehké, barevné a příjemné do ruky. Hodí se na kondiční cvičení, rehabilitaci a pro začátečníky.</li>'
          '<li><strong>Litinové činky bez povrchové úpravy</strong> jsou nejodolnější, ve vlhkém sklepě ale korodují.</li>'
          '<li><strong>Plastové kotouče s výplní</strong> jsou u nakládacích sad levnější variantou kovu. Jsou objemnější a při pádu mohou prasknout.</li></ul>'
          '<h2>Úchop a rukojeť</h2>'
          '<p>Rukojeť bývá vroubkovaná, aby v ruce neklouzala ani při zpocených dlaních. Ostré vroubkování drží jistě, ale bez rukavic může na dlaních tvořit mozoly. Jemnější vroubkování je příjemnější, při těžších cvicích ale ruka víc klouže. Silnější rukojeť víc zapojuje předloktí, tenčí se snáz drží. Pokud vám činky v ruce kloužou nebo tlačí, pomohou <a href="/sportovni-rukavice/">sportovní rukavice</a>. U nakládacích činek zkontrolujte, zda je tyč dost dlouhá pro tolik kotoučů, kolik plánujete nasadit, a zda zajišťovací matice drží pevně.</p>'
          '<h2>Jakou hmotnost zvolit</h2>'
          '<p>Hmotnost se odvíjí od cviku, ne od jednoho čísla. Na tlaky na lavici a veslování zvládnete výrazně víc než na upažování nebo bicepsový zdvih. Proto se vyplatí mít několik párů nebo nakládací systém, který pokryje lehčí i těžší cviky. Rozumné je zvolit hmotnost, se kterou zvládnete zamýšlený počet opakování technicky čistě, a až pak přidávat. U pevných činek sledujte odstupňování. Mezi lehkými páry stačí malé kroky, u těžších se přechází po větších skocích.</p>'
          '<p>Při objednávce si ověřte, zda nabídka platí za jeden kus, nebo za pár. Obchody to uvádějí různě a dvě činky jsou při cvičení skoro vždy potřeba.</p>'
          '<h2>Nastavitelné činky s voličem</h2>'
          '<p>Nastavitelné jednoručky s voličem jsou kompromisem mezi pevnými a nakládacími činkami. Celá sada kotoučů leží v podstavci a otočením kolečka nebo zasunutím kolíku si vyberete, kolik z nich zůstane na rukojeti, když činku zvednete. Jeden pár tak nahradí celou řadu pevných jednoruček a vejde se pod postel nebo do skříně. Nevýhodou je složitější mechanismus, který nesnese pouštění na zem, a objemnější tvar. U některých cviků, například při přítazích v předklonu nebo při tlaku nad hlavou, může delší činka překážet. Před koupí zjistěte, v jakých krocích se dá hmotnost měnit a jakou nejvyšší hmotnost sada nabízí.</p>'
          '<h2>Co se s jednoručkami dá cvičit</h2>'
          '<p>Jednoručky pokryjí prakticky všechny svalové skupiny. Na hrudník se cvičí tlak na rovné nebo šikmé lavici a rozpažování vleže. Na záda přítah v předklonu s oporou o lavici. Na ramena tlak nad hlavou, upažování a předpažování. Na nohy dřep s činkou u hrudníku, výpady a rumunský mrtvý tah. Na paže bicepsový zdvih a francouzský tlak. Protože každá ruka pracuje samostatně, zapojují se víc stabilizační svaly a cviky jsou náročnější na koordinaci než s osou. Kdo s posilováním začíná, udělá dobře, když si techniku nechá ukázat trenérem.</p>'
          + T(['Partie', 'Příklady cviků s jednoručkami', 'Co se hodí navíc'], [
              ['Hrudník', 'tlak na lavici, rozpažování vleže', 'posilovací lavice'],
              ['Záda', 'přítah v předklonu, přítah jednoruč s oporou', 'lavice nebo pevná židle'],
              ['Ramena', 'tlak nad hlavou, upažování', 'lehčí pár činek'],
              ['Nohy a hýždě', 'dřep, výpady, rumunský mrtvý tah', 'těžší pár činek'],
              ['Paže', 'bicepsový zdvih, tlak za hlavou', 'lehčí a střední pár']]) +
          '<h2>Kde a jak činky skladovat</h2>'
          '<p>Činky pohozené na podlaze jsou nejčastější příčinou ukopnutých prstů a poškrábaných parket. Vyplatí se <a href="/stojany-na-cinky/">stojan na činky</a>, v němž jsou páry srovnané podle hmotnosti a nemusíte se pro ně ohýbat až k zemi. Pod místo, kde cvičíte, dejte gumovou podložku, která chrání podlahu a tlumí hluk. Chromové a litinové činky skladujte v suchu, ve vlhku se na nich může objevit rez.</p>'
          '<h2>Bezpečnost při cvičení</h2>'
          '<ul><li>Před každým cvičením zkontrolujte matice a objímky nakládacích činek. Uvolněný kotouč může sklouznout na nohu.</li>'
          '<li>Činky po sérii pokládejte, nepouštějte je z výšky, i když jsou pogumované.</li>'
          '<li>Při tlacích vleže na <a href="/posilovaci-lavice/">lavici</a> činky odkládejte kontrolovaně podél těla.</li>'
          '<li>Pokud máte zdravotní potíže se zády nebo klouby, poraďte se o vhodném cvičení s lékařem nebo fyzioterapeutem.</li>'
          '<li>Děti ke cvičení s činkami nepouštějte bez dozoru a činky jim neukládejte na dosah.</li></ul>'
          '<h2>Jednoručky v domácí posilovně</h2>'
          '<p>Kdo si doma zařizuje koutek na cvičení, obvykle začíná pár jednoručkami a podložkou. Postupně přibývá <a href="/posilovaci-lavice/">lavice</a>, stojan a případně těžší zátěž. Je proto rozumné hned na začátku myslet na to, kam se sada bude rozšiřovat. Nakládací činky jsou levnější vstupenkou, protože se k nim dají dokupovat kotouče stejného průměru. Pevné jednoručky jsou pohodlnější, ale každý nový pár zabere další místo ve stojanu. Při plánování počítejte i s prostorem kolem sebe: na tlak vleže, výpady nebo upažování potřebujete volné místo do stran i dopředu, ne jen plochu pod podložkou.</p>'
          '<p>Hluk a otřesy řeší hlavně lidé v panelových domech. Gumová nebo PU úprava, silnější podložka pod místem cvičení a pokládání činek místo pouštění výrazně sníží hluk, který slyší sousedé pod vámi. Kdo cvičí brzy ráno nebo pozdě večer, ocení i tišší pogumované kotouče u nakládacích sad.</p>'
          '<h2>Jednoručky, nebo kettlebell</h2>'
          '<p>Jednoruční činka má těžiště v ose ruky, takže se dobře hodí na pomalé a kontrolované cviky. <a href="/kettlebelly/">Kettlebell</a> má těžiště pod rukojetí a vyniká ve švihových a dynamických pohybech. Obě zátěže se doplňují a mnoho lidí doma používá obě. Kdo chce cvičit bez kovu, může zátěž doplnit také <a href="/posilovaci-gumy/">posilovacími gumami</a>.</p>'
          '<h2>Na co se zaměřit při výběru</h2>'
          '<ol><li>Rozhodněte se mezi pevnými a nakládacími činkami podle místa, které máte.</li>'
          '<li>U nakládacích sad zkontrolujte průměr tyče a otvoru kotoučů, abyste mohli sadu později rozšířit.</li>'
          '<li>Vyberte povrch podle podlahy: guma a PU chrání podlahu nejlépe.</li>'
          '<li>Zvažte stojan už při nákupu činek, ať mají kde ležet.</li>'
          '<li>Ověřte, zda cena v nabídce platí za kus, nebo za pár.</li></ol>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Jediný pár činek pro všechny cviky.</li>'
          '<li>Neutažené matice nakládacích činek.</li>'
          '<li>Chromové činky na dlaždicích bez podložky.</li>'
          '<li>Objednávka jednoho kusu v domnění, že jde o pár.</li>'
          '<li>Skladování litiny ve vlhkém sklepě.</li></ul>',
    faq=[
        ('Jsou lepší pevné, nebo nakládací jednoručky?', 'Pevné jsou okamžitě připravené a odolné, ale pro každou hmotnost potřebujete další pár. Nakládací ušetří místo a dají se rozšiřovat, výměna kotoučů ale zabere čas.'),
        ('Proč mají hexagonové činky šest hran?', 'Šestihranná hlava se neodvaluje po podlaze. Činku tak lze bezpečně položit a použít i jako oporu při klicích.'),
        ('Proč gumové činky zapáchají?', 'Nová guma uvolňuje výrazný pach, který během týdnů na vzduchu slábne. Polyuretanové činky zapáchají výrazně méně.'),
        ('Jakou hmotnost činek koupit na začátek?', 'Takovou, se kterou zvládnete zamýšlený počet opakování technicky čistě. Na různé cviky budete potřebovat různé hmotnosti, proto se hodí nakládací sada nebo několik párů.'),
        ('Platí cena za kus, nebo za pár?', 'Každý obchod to uvádí jinak. Před objednávkou si to v popisu nabídky ověřte, ke cvičení většinou potřebujete pár.'),
        ('Ničí činky podlahu?', 'Chromové a litinové při pádu ano. Pomůže gumová podložka, stojan a pogumované nebo PU činky.'),
        ('Co jsou nastavitelné činky s voličem?', 'Jednoručky, u kterých se hmotnost mění otočením kolečka nebo zasunutím kolíku přímo ve stojanu. Jeden pár nahradí řadu pevných činek, mechanismus ale nesnese pouštění na zem.'),
        ('Potřebuji k jednoručkám lavici?', 'Ne nutně, mnoho cviků zvládnete vestoje. Pro tlaky vleže, rozpažování a přítahy s oporou je ale posilovací lavice velmi užitečná.'),
        ('Jak činky uložit?', 'Ve stojanu podle hmotnosti a v suchu. Litina a chrom ve vlhku rezaví.'),
    ])

# ------------------------------------------------------------------ cestovni-tasky
NEW['cestovni-tasky'] = dict(long=True,
    title='Cestovní tašky a duffel bagy: s popruhy i na kolečkách',
    desc='Cestovní taška nebo duffel bag s popruhy na záda, na kolečkách i skládací. Objem, materiál, příruční zavazadlo a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Cestovní taška</strong> je jednoduchý vak s velkým hlavním prostorem, do kterého se vejde oblečení na víkend, na týden u moře nebo na expedici. Pro odolné tašky z pevné laminované tkaniny se ujal anglický název duffel bag. Většina dnešních duffelů má kromě uch i popruhy na záda, takže se nosí jako batoh, některé jezdí na kolečkách s výsuvnou rukojetí. Proti kufru jsou tašky lehčí, přizpůsobí se obsahu a v autě nebo v zavazadlovém prostoru autobusu se snáz někam vmáčknou. Při výběru rozhoduje hlavně to, jak budete cestovat a kolik věcí s sebou vozíte.</p>'
          '<p>Sporteka vám ukáže, které české e-shopy danou tašku nabízejí, a nákup dokončíte přímo v obchodě. V nabídce jsou například ' + B(('the-north-face', 'The North Face'), ('deuter', 'Deuter')) + ', Osprey, Gregory, Eagle Creek nebo Sea to Summit. Kategorie patří pod <a href="/sportovni-tasky/">sportovní tašky</a>. Kdo hledá spíš cestovní batoh, podívejte se na <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/mestske-batohy/">městské batohy</a>.</p>',
    guide='<h2>Druhy cestovních tašek</h2>'
          '<p>Cestovní tašky se liší hlavně tím, jak se nosí. Podle toho se vybírají i na konkrétní cestu: na letiště, do auta, na loď nebo na expedici.</p>'
          + T(['Typ', 'Jak se nosí', 'Kdy se hodí'], [
              ['Duffel s popruhy na záda', 'ucha, ramenní popruh i nosný systém batohu', 'cesty, expedice, kombinace letadla a chůze'],
              ['Taška na kolečkách', 'tažení za výsuvnou rukojeť', 'letiště, nádraží, rovné chodníky'],
              ['Víkendová taška (weekender)', 'ucha a popruh přes rameno', 'krátké cesty, auto, vlak'],
              ['Skládací taška', 'sbalí se do vlastní kapsy', 'záložní taška na cestu zpět, nákupy'],
              ['Cestovní batoh', 'záda, otevírá se jako kufr', 'cestování s batohem, příruční zavazadlo'],
              ['Kufr', 'kolečka a pevná skořepina', 'citlivé věci, delší pobyty v jednom místě']]) +
          '<h2>Duffel bag: proč je tak oblíbený</h2>'
          '<p>Klasický duffel je válec nebo kvádr z odolné tkaniny s jedním velkým otvorem na zip. Nemá pevnou kostru, takže se do něj vejdou i nepravidelné věci, jako jsou boty, helma, potápěčská výstroj nebo spacák. Prázdný se dá složit a uložit do skříně. Nejznámějším příkladem je The North Face Base Camp Duffel z pevné laminované tkaniny, s otvorem ve tvaru písmene D, který se otevírá široce jako víko. Podobně robustní duffely vyrábí Deuter v řadě Duffel Pro nebo Gregory pod názvem Alpaca. Osprey prodává duffely Transporter s nosným systémem batohu a lehčí Daylite pro kratší cesty.</p>'
          '<p>Na výpravy, kde se taška hází na střechu terénního auta nebo do podpalubí lodi, je důležitá odolnost materiálu a švů. Laminovaná tkanina odpuzuje vodu a otírá se o kameny bez poškození, zip však zůstává nejslabším místem. Velký kryt zipu nebo zip krytý klopou pomůže proti dešti i prachu.</p>'
          '<h2>Objem: kolik litrů vybrat</h2>'
          '<p>Objem se udává v litrech a u duffelů bývá i v označení velikosti, třeba S, M nebo L. Pro prodloužený víkend obvykle stačí menší taška, týden u moře se vejde do středního objemu, na expedici nebo lyžařský pobyt s výbavou je potřeba velká taška. Při výběru myslete i na hmotnost plné tašky. Velký duffel naplněný po okraj se nese těžko a u letadla snadno překročí povolenou hmotnost odbaveného zavazadla. Kdo cestuje s menším zavazadlem, má obvykle pohodlnější cestu.</p>'
          '<h2>Taška jako příruční zavazadlo</h2>'
          '<p>Rozměry a hmotnost příručního zavazadla určuje každá letecká společnost sama a podmínky se liší také podle tarifu letenky. Některé společnosti zahrnují v základní ceně jen malou tašku pod sedadlo, jiné i větší zavazadlo do schránky nad hlavou. Před cestou proto vždy zkontrolujte aktuální pravidla na webu dopravce. Rozměry se měří včetně uch, koleček a vnějších kapes. Měkká taška se do měřicího rámu vejde snáz než kufr, pokud není přeplněná. Na kolečkách ale počítejte s tím, že rám a kolečka snižují využitelný objem a přidávají hmotnost.</p>'
          '<h2>Kolečka, nebo popruhy na záda</h2>'
          '<p>Taška na kolečkách šetří záda na letišti a na rovných chodnících. Po dlažbě, štěrku nebo sněhu se ale táhne špatně a kolečka i rukojeť přidávají hmotnost. Duffel s popruhy na záda nesete jako batoh, takže zvládnete schody, nádraží bez eskalátorů i cestu z autobusu do horské chaty. Pro cesty, kde nevíte, jaký terén vás čeká, je univerzálnější. Některé modely kombinují obojí, mají kolečka i popruhy schované v kapse na zádech.</p>'
          '<h2>Cestovní taška, nebo cestovní batoh?</h2>'
          '<p>Cestovní batoh má plnohodnotný nosný systém s bederním pásem, takže ho unesete i na delší vzdálenost. Často se otevírá po celé délce jako kufr, což usnadňuje balení. Hodí se pro cestování s přesuny mezi městy, kdy taháte zavazadlo po nádražích a ulicích. Duffel s popruhy na záda je jednodušší a robustnější, popruhy ale slouží spíš na kratší přesuny, třeba z parkoviště na chatu nebo z autobusu na letiště. Kdo jezdí hlavně autem nebo na lodi a zavazadlo nese jen pár set metrů, vystačí si s taškou. Kdo chodí s věcmi celé dny, ocení batoh.</p>'
          '<p>Batohy s objemem kolem příručního zavazadla se staly oblíbenými u lidí, kteří cestují nalehko a nechtějí platit za odbavené zavazadlo. Pro výlety do hor ale pořád patří klasický turistický batoh s nosným systémem stavěným na celodenní chůzi.</p>'
          '<h2>Organizace obsahu</h2>'
          '<p>Velký hlavní prostor duffelu je výhodou i nevýhodou: vejde se do něj všechno, ale věci se v něm promíchají. Pomohou cestovní organizéry, tedy obaly na oblečení a kompresní pytle. Známé jsou například obaly Eagle Creek Pack-It nebo lehké organizéry Sea to Summit. Oblečení v nich zůstane srovnané, čisté oddělené od špinavého a obaly se po příjezdu jen přendají do skříně. Hodí se také boční kapsa na boty a vnitřní kapsa na doklady.</p>'
          '<ul><li><strong>Oddělená kapsa na boty</strong> udrží špínu mimo oblečení.</li>'
          '<li><strong>Vnitřní kapsa na zip</strong> pro doklady, nabíječky a drobnosti.</li>'
          '<li><strong>Poutko na jmenovku</strong> pro rychlou identifikaci na letištním pásu.</li>'
          '<li><strong>Zip s očky na zámek</strong> pro cestování letadlem.</li>'
          '<li><strong>Kompresní popruhy</strong> zmenší objem poloprázdné tašky.</li></ul>'
          '<h2>Materiál a odolnost</h2>'
          '<p>Levnější tašky bývají z tenkého polyesteru, který se na cestách snadno odře. Odolnější modely jsou z nylonu s vyšší hustotou tkaniny nebo z laminovaných materiálů, které vodu nepropustí ani při delším dešti. Dno je nejvíc namáhaná část, proto se vyplatí zesílené dno nebo dvojitá vrstva. Zkontrolujte, jak jsou přišitá ucha a kotvení ramenních popruhů. Pokud se tam látka trhá, taška je nepoužitelná, i když je jinak celá.</p>'
          '<h2>Cestovní taška na sport</h2>'
          '<p>Duffely nosí sportovci na soustředění, potápěči na výbavu a lyžaři na boty a helmu. Pro lyže a hůlky samotné se ale hodí specializované <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a> a hokejisté potřebují rozměrné <a href="/hokejove-tasky/">hokejové tašky</a>. Pro trénink v posilovně je zase příjemnější menší sportovní taška s větranou kapsou na boty.</p>'
          '<h2>Balení do duffelu</h2>'
          '<p>Těžké věci, jako jsou boty, toaletní taška nebo elektronika, dejte ke dnu a k místu, které bude při nošení na zádech nejblíž tělu. Oblečení rolujte, zabere méně místa a méně se zmačká. Prázdná místa vyplňte ponožkami nebo spodním prádlem. Na cestu letadlem uložte léky, doklady, nabíječky a cennosti do příručního zavazadla, ne do odbavené tašky. Při balení se vyplatí nechat v tašce trochu místa na věci, které přivezete zpět. Pokud cestujete s tekutinami, zabalte kosmetiku do uzavíratelného sáčku, aby případný únik nezničil oblečení. Na dlouhé cesty se hodí i lehká skládací taška navíc, která se po cestě sbalí do malé kapsy a na zpáteční cestě pojme suvenýry nebo špinavé prádlo.</p>'
          '<h2>Péče o tašku</h2>'
          '<ul><li>Po cestě tašku vyprázdněte, vyklepejte písek a nechte ji vyschnout otevřenou.</li>'
          '<li>Laminované duffely stačí otřít vlhkým hadříkem, do pračky nepatří.</li>'
          '<li>Zip čas od času vyčistěte od písku a soli, zvlášť po pobytu u moře.</li>'
          '<li>Skladujte prázdnou a složenou v suchu, ne v zatuchlém sklepě.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Taška na kolečkách pro cestu po horských stezkách.</li>'
          '<li>Příliš velký duffel, který se pak naplní zbytečnými věcmi.</li>'
          '<li>Spoléhání na obecné rozměry příručního zavazadla bez kontroly u dopravce.</li>'
          '<li>Tenká tkanina bez zesíleného dna na expedici.</li>'
          '<li>Taška bez organizace obsahu na delší cestu s přesuny.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>U každé tašky porovnáte nabídky několika obchodů včetně dostupnosti a dopravy a objednávku dokončíte přímo v e-shopu. Pokud kromě tašky potřebujete i zavazadlo na pracovní cesty, podívejte se na <a href="/batohy-na-notebook/">batohy na notebook</a>.</p>',
    faq=[
        ('Co je duffel bag?', 'Cestovní taška z odolné tkaniny s jedním velkým hlavním prostorem na zip, obvykle s uchy, ramenním popruhem a často i popruhy na záda. Nemá pevnou kostru, takže se přizpůsobí obsahu.'),
        ('Vejde se duffel jako příruční zavazadlo?', 'Menší modely ano, ale rozměry a hmotnost určuje každá letecká společnost sama podle tarifu. Před cestou si pravidla ověřte na webu dopravce a měřte včetně uch a kapes.'),
        ('Je lepší cestovní taška na kolečkách, nebo s popruhy?', 'Kolečka šetří záda na letišti a rovném povrchu. Popruhy na záda jsou lepší na schody, dlažbu a terén. Některé modely mají obojí.'),
        ('Jaký objem cestovní tašky zvolit?', 'Podle délky cesty a výbavy. Na víkend stačí menší taška, na týden střední a na expedici nebo lyžařský pobyt velká. Myslete i na hmotnost plné tašky.'),
        ('Čím se liší cestovní taška od cestovního batohu?', 'Cestovní batoh má plnohodnotný nosný systém a otevírá se často jako kufr. Duffel je hlavně taška, popruhy na záda slouží na kratší přesuny.'),
        ('Je duffel vodotěsný?', 'Laminované duffely vodu odpuzují a krátký déšť vydrží, zip ale vodotěsný být nemusí. Na vodu jsou určeny vodotěsné vaky se svařenými švy.'),
        ('Co jsou cestovní organizéry?', 'Lehké obaly na oblečení a drobnosti, často na zip nebo s kompresí. Udrží věci v tašce srovnané, oddělí čisté od špinavého a po příjezdu se jen přendají do skříně.'),
        ('Jak cestovní tašku vyčistit?', 'Laminované duffely stačí otřít vlhkým hadříkem a nechat uschnout otevřené. Ze zipu vykartáčujte písek a sůl. Do pračky tašky s laminací nedávejte.'),
        ('Prodává Sporteka tašky přímo?', 'Ne, porovnává nabídky českých e-shopů. Tašku objednáte v obchodě, který si vyberete.'),
    ])
