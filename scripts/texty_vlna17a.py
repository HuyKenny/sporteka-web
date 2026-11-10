"""sporteka.cz — wave 17a (4. 11. 2026): long texts (>= 1650 words) for plazove-doplnky, cyklisticke-kratasy-a-kalhoty, cyklisticke-dresy, cyklo-pohon.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ plazove-doplnky
NEW['plazove-doplnky'] = dict(long=True,
    title='Plážové doplňky: osušky, podložky, tašky',
    desc='Plážové doplňky a osušky: rychleschnoucí ručníky, plážové podložky, tašky i stínění. Jak vybrat na moře, bazén a jezero.',
    intro='<p>Dobrá pláž nebo koupaliště se nepozná jen podle vody, ale i podle toho, co si s sebou odnesete na dek. Do kategorie <strong>plážové doplňky</strong> patří osušky a pončo, '
          'plážové podložky a tašky, nafukovací kruhy a lehátka, míče, slunečníky i drobnosti, které rodinný den u vody zpříjemní. Spousta věcí vypadá podobně, ale liší se materiálem, '
          'velikostí po složení, odolností proti písku a tím, jak rychle po koupání uschne.</p>'
          '<p>Sporteka srovnává nabídky českých obchodů u stejného zboží vedle sebe, takže poznáte, kde je požadovaná barva nebo velikost skladem. Samostatně najdete '
          '<a href="/nafukovaci-hracky/">nafukovací hračky a lehátka do vody</a>, k plavání patří <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavky/">plavky</a>. '
          'Celý obor zastřešuje kategorie <a href="/vodni-sporty/">vodní sporty</a>. Dále vás provedeme výběrem podle místa, počtu lidí i toho, kolik zavazadlového prostoru máte.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Pod pojmem plážové doplňky se skrývá nečekaně široký sortiment. Aby se v něm dalo orientovat, rozdělíme ho podle účelu, který věc plní během dne u vody.</p>'
          + T(['Skupina', 'K čemu slouží', 'Na co se zaměřit'], [
              ['Osušky a plážové ručníky', 'osušení po koupání, podložka na dek', 'savost, rychlost schnutí, rozměr, hmotnost po zabalení'],
              ['Pončo a župany', 'převlékání na veřejném místě, zahřátí po vodě', 'kapuce, délka, materiál'],
              ['Podložky a plážové deky', 'sezení či ležení na písku nebo trávě', 'spodní vrstva proti vlhkosti, kapsy pro kolíky'],
              ['Plážové tašky a vodotěsné vaky', 'přenos osušek, jídla a drobností', 'velikost, úchyty, odolnost proti písku'],
              ['Nafukovací kruhy, matrace a lehátka', 'plavání a odpočinek na vodě', 'nosnost, tloušťka vinylu, typ ventilu'],
              ['Míče, raketové hry a lopatky', 'zábava na písku a v mělké vodě', 'velikost, věk dítěte, odolnost proti slanému písku'],
              ['Slunečníky a stínění', 'ochrana před sluncem a větrem', 'průměr, stabilita, uchycení do písku']]) +
          '<p>U každého kusu je dobré myslet na způsob, jakým ho dopravíte na místo. Dvoumetrová osuška s hlubokým vlasem je báječná doma, ale na výlet na kole nebo na vlak na koupaliště už se hodí spíš kompaktní varianta.</p>'
          '<h2>Osušky: savost versus váha</h2>'
          '<p>Rozhodující je materiál a gramáž. Klasická froté bavlna dobře saje a je příjemná na dotek, jenže je objemná, pomalu schne a po namočení těžká. Mikrovlákno se skládá do zlomku objemu, saje překvapivě dobře a uschne za pár desítek minut na slunci. '
          'Velur z bavlny má na lícové straně hladký povrch, ze kterého se lépe oklepává písek. Plážové osušky ve stylu tkaných pešteker jsou tenké, lehké a snadno se perou, ale vodu pojmou méně než froté.</p>'
          + T(['Materiál', 'Výhoda', 'Nevýhoda', 'Vhodné použití'], [
              ['Froté bavlna', 'měkká, dobře saje', 'těžká, pomalu schne', 'pláž u auta, hotel s vlastním pokojem'],
              ['Mikrovlákno', 'malý objem, rychle schne', 'zpočátku trochu jiný pocit na kůži', 'cestování, kemp, bazén po tréninku'],
              ['Bavlněný velur', 'hladký povrch, barevné motivy', 'střední rychlost schnutí', 'dovolená u moře'],
              ['Tkaná plážová osuška', 'lehká, skladná, dá se použít jako šátek či deka', 'méně savá', 'batoh, kolo, jednodenní výlet']]) +
          '<p>Při výběru velikosti pomůže jednoduché pravidlo. Dospělému stačí osuška v rozměrech zhruba jako přes rameno až ke kolenům, pokud ji používá jen na osušení. Chcete-li na ní ležet, hledejte větší, ideálně přes celou výšku. Děti ocení pončo s kapucí, protože se v něm převléknou bez obnažování a po koupání je zahřeje.</p>'
          '<h2>Jak vybrat podle místa</h2>'
          '<h3>Moře a písečné pláže</h3>'
          '<p>Písek, vítr a slaná voda dělají plážovému vybavení zle. Hledejte osušky, které nenasají písek do vlasu, a tašky s dobře dovíratelným zipem. Kovové součásti v zavírání slunečníku a podložek mohou na slaném vzduchu korodovat, takže po dovolené je omyjte sladkou vodou a nechte oschnout.</p>'
          '<h3>Jezera a rybníky</h3>'
          '<p>U přírodních koupališť se obvykle sedí na trávě. Plážová deka s nepromokavou spodní vrstvou drží vlhkost od země a po odpoledni ji stačí oklepat. Vyplatí se i obuv do vody z kategorie <a href="/obuv-do-vody/">obuv do vody</a>, když je dno kamenité.</p>'
          '<h3>Bazén a aquapark</h3>'
          '<p>Tady nikdo nepotřebuje plážovou deku. Stačí rychleschnoucí osuška, taška s oddělenou kapsou na mokré věci a případně pončo na cestu domů. Pokud trénujete plavání, ocení plavci i <a href="/plavecke-cepice/">plavecké čepice</a> a <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>'
          '<h2>Nafukovací doplňky a bezpečnost</h2>'
          '<p>Nafukovací kruh nebo matrace není záchranná vesta. Ať už jde o dětské pomůcky, nebo velké lehátko na hladinu, nesmí nahradit dohled dospělého. Větší nafukovací předměty mohou při vánku odplout směrem od břehu, takže je dobré je mít pod kontrolou a nenechávat děti bez dozoru. '
          'Pro začínající plavce je lepší pomůcka určená k výuce plavání, která se obléká na tělo; takové pomůcky najdete v kategorii <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>'
          '<p>Při nákupu sledujte údaje o nosnosti, věku a rozměrech. Silnější vinyl je odolnější proti poškrábání, ale nafoukne se pomaleji. Dvoukomorové konstrukce a bezpečnostní ventily dávají větší jistotu, pokud jedna komora povolí. '
          'Opravná záplata bývá součástí balení, přesto stojí za to ověřit, že je v krabici. Nafukovací věci neukládejte na horkém slunci ani v zavazadlovém prostoru auta v poledne, vzduch se rozpíná a ventil nebo švy mohou povolit.</p>'
          '<p>Oblíbená lehátka a ostrůvky do bazénu najdete v samostatné podkategorii <a href="/nafukovaci-hracky/">nafukovací hračky a lehátka do vody</a>, kde se dá filtrovat podle tvaru a velikosti. '
          'Větší bazény pro zahradu jsou v kategorii <a href="/bazeny/">bazény</a>.</p>'
          '<h2>Sluneční ochrana</h2>'
          '<p>Na vodě sluneční záření odráží hladina a kůže se spálí rychleji, než by člověk čekal, i když je zataženo. Stín je základ, ale nestačí sám. Slunečník s dostatečným průměrem a stabilním uchycením pomáhá, jenže spolehlivě chrání jen oblast pod ním a rozptýlené záření dopadá i mimo ni. '
          'Doplňte ho oděvem s UV ochranou a krémem s vhodným faktorem, který budete po koupání obnovovat. Oděvy s ochranným faktorem najdete v kategorii <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>.</p>'
          '<p>Slunečník se v písku drží lépe, pokud se zavrtá do vlhké vrstvy a podepře navršeným pískem. Při silnějším větru ho raději zavřete, protože může zranit lidi okolo. Na velmi větrnou pláž se lépe hodí stínící stan s uzavřenou zadní stěnou, který je ovšem těžší.</p>'
          '<h2>Plážové tašky a organizace věcí</h2>'
          '<p>Taška na pláž je často věcí, kterou kupujeme poslední, a přitom ovlivní, jak snadno všechno unesete. Síťovaná taška nechá propláchnout písek a rychle uschne, hodí se na mušle, míče a hračky. '
          'Nepromokavý vak s rolovacím uzávěrem ochrání telefon, klíče a doklady při plavbě na paddleboardu či loďce. Prostornější plážový batoh se hodí pro rodinu s dětmi, kde se vejde svačina, krém i oblečení na převlečení. '
          'Pokud k vodě jezdíte hlavně na kole, je lepší úzký batoh na záda než široká taška přes rameno. Větší výběr najdete v kategorii <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li><strong>Osušky</strong> perte při doporučené teplotě a bez aviváže, která snižuje savost a u mikrovlákna zalepuje vlákna.</li>'
          '<li><strong>Pončo a župany</strong> po koupání vysušte na slunci a vyvěste na ventilaci, vlhké v tašce začne zapáchat.</li>'
          '<li><strong>Nafukovací kusy</strong> před uložením opláchněte, úplně vysušte a vzduch vypusťte, aby se vinyl nelepil.</li>'
          '<li><strong>Slunečníky</strong> po slané vodě otřete vlhkou utěrkou a uložte do obalu až po oschnutí.</li>'
          '<li><strong>Plážové tašky</strong> vyklepejte od písku a promyjte, jinak písek při dalším použití obrušuje zip.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('bestway', 'Bestway'), ('intex', 'Intex'), ('nils', 'Nils'), ('sea-to-summit', 'Sea to Summit'), ('cocoon', 'Cocoon'), ('decathlon', 'Decathlon'), ('aquos', 'Aquos'), ('skandika', 'Skandika')) + '. '
          'Bestway a Intex vyrábějí nafukovací doplňky a bazénové potřeby, Sea to Summit a Cocoon jsou specialisté na lehké cestovní osušky a vaky, Nils a Aquos pokrývají široký sortiment vodních a kempingových potřeb. '
          'Značky s reklamními potisky se objevují u levnějších osušek, které se často dávají jako dárky nebo na akce.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Kdo ke koupání vyráží s celou rodinou, může potřebovat víc než jen osušky. Prohlédněte si <a href="/detske-plavky/">dětské plavky</a>, <a href="/damske-plavky/">dámské plavky</a> a <a href="/panske-plavky/">pánské plavky</a>. '
          'K vodě patří i <a href="/sandaly/">sandály</a>, na šnorchlování <a href="/snorchlovani/">šnorchly a masky</a>, na surfování <a href="/paddleboardy/">paddleboardy</a> a pro chladnější vodu <a href="/neopreny/">neopreny</a>. '
          'Pokud k vodě jezdíte i na pár dní, doplníte výbavu v kategorii <a href="/kemping/">kemping</a>.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit osušku jen podle barvy a motivu, bez ohledu na materiál a váhu.</li>'
          '<li>Podcenit objem po složení, když se vybavení veze v batohu nebo v malém kufru.</li>'
          '<li>Spoléhat na nafukovací pomůcku jako na ochranu před utonutím.</li>'
          '<li>Vzít si slunečník bez uchycení do písku nebo bez zátěže.</li>'
          '<li>Nechat vlhké věci v zavřené tašce přes noc, kde se rychle rozšíří zápach a plíseň.</li>'
          '<li>Použít aviváž při praní osušky z mikrovlákna.</li></ul>'
          '<h2>Pro koho je tato kategorie</h2>'
          '<p>Pro rodiny, které jezdí k vodě s dětmi a chtějí mít k ruce vše od hraček po stín. Pro cestovatele, kteří hledají co nejmenší a nejlehčí osušku do zavazadla. Pro plavce, kteří si po tréninku v bazénu potřebují rychle osušit tělo a vlasy. '
          'Pro ty, kdo vyrážejí s kempingovou výbavou k jezeru a ocení skladné lehátko či podložku. A také pro každého, kdo shání praktický dárek, třeba pončo pro dítě nebo pěknou plážovou tašku.</p>',
    faq=[('Jakou osušku vzít na cesty a do batohu?', 'Nejvíc se hodí mikrovlákno nebo tenká tkaná osuška. Po složení zabírají málo místa, rychle schnou a váží zlomek froté bavlny. Pokud potřebujete větší savost, vezměte rozměrnější kus a doma ho nechte vyschnout na vzduchu.'),
         ('Proč nepoužívat aviváž na plážové osušky?', 'Aviváž tvoří na vláknech vrstvu, která snižuje savost. U mikrovlákna navíc zalepuje jemná vlákna, takže osuška přestane dobře sát vodu. Stačí obyčejný prací prostředek a pořádné vypláchnutí.'),
         ('Jak velká plážová osuška stačí?', 'Pro pouhé osušení po koupání stačí kus přes rameno až ke kolenům. Pokud si na ni chcete lehnout, hledejte alespoň na výšku těla. Pro dvě osoby volte rozměrnější plážovou deku nebo dvě osušky vedle sebe.'),
         ('Je nafukovací kruh bezpečná pomůcka pro děti?', 'Není to záchranná pomůcka a nenahradí dohled dospělého. Dítě z něj může vyklouznout nebo se převrátit. Pro výuku plavání se hodí pomůcky, které se obléknou na tělo, a vždy platí, že dítě u vody musí být pod stálým dohledem.'),
         ('Jak se starat o nafukovací matraci, aby vydržela?', 'Po koupání ji opláchněte sladkou vodou, vysušte, vypusťte vzduch a uložte na suché a chladné místo. Nenechávejte ji dlouho na ostrém slunci, protože se vzduch rozpíná a může povolit ventil nebo šev.'),
         ('Jak ochránit pláž před větrem a sluncem zároveň?', 'Použijte stabilní slunečník zavrtaný do vlhkého písku nebo stínící stan s uzavřenou zadní stěnou. Doplňte oblečení s UV ochranou a krém s vhodným faktorem, protože stín chrání jen částečně a záření se odráží od hladiny.'),
         ('Hodí se bavlněné froté do kempu?', 'Jen pokud máte dost místa a čas na sušení. Bavlněné froté je těžké a po namočení schne pomalu, takže se v kempu dlouho nevysuší. V kempu se lépe osvědčí mikrovlákno nebo tkaná osuška.'),
         ('Jak vyprat plážovou tašku s pískem?', 'Nejdřív ji vyklepejte, pak vyperte ručně nebo v pračce podle štítku a nechte oschnout otevřenou. Zbylý písek ve švech může při dalším použití obrušovat zip a látku, proto s vysypáním nešetřete.'),
         ('Co vzít na pláž pro malé dítě?', 'Pončo s kapucí, plenkové plavky nebo dětské plavky, klobouček, UV oblečení, krém a dostatek pití. Hodí se také lopatka a kyblík, ale důležité je mít stín a pravidelně obnovovat ochranu před sluncem.'),
         ('Kde porovnám nabídky plážových doplňků?', 'Na Sportece otevřete konkrétní osušku, kruh nebo slunečník a uvidíte ceny českých obchodů vedle sebe. Při srovnání vždy zkontrolujte rozměry, materiál a skladovou dostupnost barvy či velikosti.')],
)


# ------------------------------------------------------------------ cyklisticke-kratasy-a-kalhoty
NEW['cyklisticke-kratasy-a-kalhoty'] = dict(long=True,
    title='Cyklistické kraťasy a kalhoty s vložkou',
    desc='Cyklistické kraťasy a kalhoty: s kšandami, s vložkou, volné MTB i zimní. Velikosti, materiály, péče a srovnání nabídek českých obchodů.',
    intro='<p>Kdo pár hodin sedí na kole, brzy zjistí, že kalhoty z obyčejného oblečení nejsou ten nejlepší nápad. Švy tlačí, látka se v pase svinuje a mokré tričko odvádí pozornost od cesty. '
          'Právě proto vznikly <strong>cyklistické kraťasy a kalhoty</strong>: s vložkou v sedací části, s pružným střihem, který nepřekáží při šlapání, a s materiálem odvádějícím pot. '
          'V nabídce najdete přiléhavé silniční modely s kšandami, volnější kraťasy na horská kola, trekingové kalhoty se zip-off nohavicemi i zimní izolované varianty.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného kousku a pomáhá najít správnou velikost i barvu. Ke kraťasům patří <a href="/cyklisticke-dresy/">dresy</a>, '
          '<a href="/cyklisticke-ponozky/">ponožky</a> a <a href="/cyklisticke-rukavice/">rukavice</a>. Celé oblečení najdete v kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>. Níže se dozvíte, podle čeho vybrat typ, vložku a velikost.</p>',
    guide='<h2>Typy cyklistických kraťasů a kalhot</h2>'
          '<p>Základní rozdělení je podle disciplíny a počasí. Každý typ má jiný střih, jiné materiály a jiný způsob, jak řeší vložku.</p>'
          + T(['Typ', 'Pro jaký styl jízdy', 'Hlavní znaky', 'Na co si dát pozor'], [
              ['Silniční kraťasy s kšandami', 'delší vyjížďky na silnici a gravelu', 'přiléhavý střih, kšandy drží vložku na místě', 'na toaletě je třeba sundat dres, proto jsou nepohodlné při zastávkách'],
              ['Silniční kraťasy bez kšand', 'kratší a středně dlouhé jízdy', 'pružný pás se silikonovým lemem', 'pás se u delších jízd může zařezávat'],
              ['MTB kraťasy volného střihu', 'horské kolo, trail, enduro', 'kapsy, odolný materiál, často bez vložky', 'vložku si lze koupit zvlášť jako spodní prádlo'],
              ['Dlouhé cyklistické kalhoty', 'podzim, jaro, chladné ráno', 'prodloužené nohavice, někdy zateplení na stehnech', 'musí mít pružné lemy a reflexní prvky'],
              ['Zimní kalhoty', 'jízda v zimě', 'větruodolná membrána na přední straně, tepelný úplet', 'nižší prodyšnost, hodí se jen na teploty kolem nuly'],
              ['Trekingové a městské kalhoty', 'dojíždění do práce, výlety', 'reflexní prvky, vyztužený sedák, zip-off nohavice', 'bez vložky bývají volnější a méně efektivní na dlouhé trasy'],
              ['Dětské a juniorské kraťasy', 'děti a mladí cyklisté', 'jednoduchá vložka, pružné lemy', 'rychle se z nich vyroste']]) +
          '<p>Pokud jezdíte jen občas, začněte základní variantou bez kšand a s jednoduchou vložkou. Větší investice se vyplatí až od chvíle, kdy trávíte na kole víc než hodinu v kuse a rozdíl v pohodlí je znát.</p>'
          '<h2>Vložka: srdce cyklistických kraťasů</h2>'
          '<p>Vložka, odborně chamois, je měkká a prodyšná pěna v sedací části. Má za úkol rozložit tlak mezi sedací kosti, omezit tření a odvádět vlhkost. Liší se tloušťkou, tvarem a použitou pěnou. '
          'Pro krátké jízdy stačí tenčí vložka, na hodiny v sedle se hodí silnější, ale ne vždy je tlustší vložka pohodlnější. Příliš objemná se může svinovat a způsobovat otlaky. Vložka musí k tělu přiléhat bez záhybů.</p>'
          '<ul><li><strong>Délka jízdy:</strong> do hodiny stačí tenká vložka, po dvou hodinách se začne projevovat kvalita pěny a tvaru.</li>'
          '<li><strong>Pohlaví:</strong> dámské vložky mají jiný tvar a rozložení než pánské, protože se liší pánevní anatomie. Neučiňte chybu a nekupujte unisex vložku, pokud existuje model pro vás.</li>'
          '<li><strong>Typ sedla:</strong> s užším závodním sedlem se hodí tenčí vložka, s širším komfortním sedlem může být vložka silnější.</li>'
          '<li><strong>Čištění:</strong> vložka se musí vyprat po každé jízdě, jinak se v ní množí bakterie a hrozí podráždění.</li></ul>'
          '<p>Kraťasy s vložkou se nosí bez spodního prádla. Spodní prádlo vytváří další švy, zadržuje vlhkost a způsobuje otlaky. To je asi nejčastější chyba začátečníků.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Cyklistické kraťasy sedí správně, když přiléhají k tělu, ale nijak neškrtí. Nohavice nesmí vyjíždět, lem má sedět těsně nad kolenem, u silničních modelů o něco výš, u volnějších MTB kraťasů nad koleny nebo i níž. '
          'Pás drží pevně, aniž by tlačil na břicho. Vyzkoušejte si polohu v sedle, v předklonu se pas nesmí propadat a záda nesmí zůstat odkrytá.</p>'
          + T(['Míra', 'Kde měřit', 'Jak se projeví při chybné velikosti'], [
              ['Pas', 'v nejužším místě trupu, ne pod pupkem', 'pás tlačí nebo se kraťasy sunou dolů'],
              ['Boky', 'v nejširším místě', 'látka se napíná, švy se nepříjemně otiskují'],
              ['Délka nohavice', 'od rozkroku ke kolenu', 'vyjíždějící nohavice nebo škrtící lem'],
              ['Obvod stehna', 'v nejsilnějším místě', 'lem se zařezává nebo stahuje dolů']]) +
          '<p>Každý výrobce používá vlastní velikostní tabulku, takže stejné označení M nemusí sedět stejně. Proto na stránce produktu vždy zkontrolujte rozměry a porovnejte je se svými. Pokud jste na hranici dvou velikostí, vyberte spíše větší pro volnější jízdu, menší pro závodní styl.</p>'
          '<h2>Materiály a funkce</h2>'
          '<p>Nejběžnější je elastický úplet z polyamidu a elastanu, někdy doplněný polyesterem. Tkanina má odvádět pot, rychle schnout a držet tvar. V létě se hledají lehké prodyšné materiály, na jaro a podzim silnější úplety s hřejivou povrchovou úpravou. '
          'Zimní kalhoty mají na přední straně větruodolnou vrstvu, vzadu prodyšnou. Modely s UV ochranou se hodí pro dlouhé výlety na prudkém slunci. Reflexní prvky na lýtkách zvyšují viditelnost večer a ráno.</p>'
          '<ul><li><strong>Silikonový lem</strong> na nohavicích drží kraťasy na místě bez škrcení.</li>'
          '<li><strong>Plochý steh</strong> omezuje tření a otlaky na vnitřní straně stehen.</li>'
          '<li><strong>Zipové kapsy</strong> uloží klíče nebo kartu u MTB modelů.</li>'
          '<li><strong>Kompresní zóny</strong> dodávají pocit opory a najdete je hlavně u závodních modelů; zdravotní účinek se od nich nečeká.</li></ul>'
          '<h2>Jak vybrat podle sezóny</h2>'
          '<h3>Léto</h3>'
          '<p>Na teplé dny stačí krátké kraťasy z lehkého úpletu. Vyplatí se světlejší barvy, které se tolik nehřejí. U silničních modelů se hledají kšandy z prodyšné síťoviny, ať v nich není vedro. Pro dlouhé výlety se hodí i tenké kolenní nebo nohavicové návleky z kategorie <a href="/cyklisticke-navleky/">cyklistické návleky</a>.</p>'
          '<h3>Jaro a podzim</h3>'
          '<p>V přechodném období se osvědčují tříčtvrteční kalhoty nebo krátké kraťasy s návleky, které se dají v případě oteplení sundat. Zde se hodí nepromokavá bunda a vesta z kategorie <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>.</p>'
          '<h3>Zima</h3>'
          '<p>Při nízkých teplotách chcete zateplené kalhoty s větruodolným předkem a případně kalhoty s kšandami. Důležité jsou i teplé ponožky z kategorie <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> a rukavice, protože právě nohy a ruce mrznou první.</p>'
          '<h2>Pro koho jaké kraťasy</h2>'
          '<p>Začátečník, který najede pár desítek kilometrů týdně, vystačí s kalhotami s jednoduchou vložkou a pružným pásem. Silniční jezdec trávící v sedle čtyři i více hodin ocení kšandy, kvalitní vložku a přiléhavý střih. '
          'Na horských kolech se hodí volnější kraťasy, často s odnímatelnou vložkou, které lépe sedí při velké pohyblivosti na trailu. Pro dojíždění do práce se hodí trekingové kalhoty s reflexními prvky, v nichž se v kanceláři neztratíte. '
          'Gravelové jezdce zajímá kombinace odolnosti a pohodlí na dlouhých trasách.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Perte po každé jízdě, nejlépe obrácené naruby, při doporučené teplotě na šetrný program.</li>'
          '<li>Nepoužívejte aviváž, která snižuje schopnost látky odvádět pot a ničí pěnu ve vložce.</li>'
          '<li>Nesušte v sušičce a nevěste na radiátor, elastan stárne vlivem tepla.</li>'
          '<li>Zip a suchý zip zapněte před praním, ať se nezachytí o jiné kusy.</li>'
          '<li>Kraťasy po několika stovkách hodin v sedle zvyknou ztratit pružnost, vložka se slisuje a přestane tlumit, což je signál k výměně.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíc zboží nabízí ' + B(('silvini', 'Silvini'), ('rockbros', 'Rockbros'), ('haven', 'Haven'), ('siroko', 'Siroko'), ('craft', 'Craft'), ('kilpi', 'Kilpi'), ('loffler', 'Löffler'), ('etape', 'Etape'), ('rockrider', 'Rockrider'), ('castelli', 'Castelli')) + '. '
          'Silvini a Etape jsou české značky se širokým sortimentem, Castelli a Craft se zaměřují na závodní kousky, Löffler je rakouský výrobce funkčního oblečení, Rockrider patří do sortimentu sportovního řetězce a Rockbros a Siroko pokrývají dostupnější nabídku. '
          'Haven je známý především dámským a pánským cyklistickým oblečením pro rekreační jezdce.</p>'
          '<h2>Související vybavení</h2>'
          '<p>K cyklistickému oblečení patří bezpečnost i drobné doplňky. Pro ochranu hlavy sáhněte po <a href="/cyklisticke-helmy/">cyklistické helmě</a>, na oči po <a href="/cyklisticke-bryle/">cyklistických brýlích</a>, na chodidla po <a href="/cyklisticka-obuv/">cyklistické obuvi</a>. '
          'Pro viditelnost používejte <a href="/cyklo-svetla/">světla</a>. Pro vybavení na kolo je pak ucelená kategorie <a href="/cyklistika/">cyklistika</a>.</p>'
          '<h2>Jak kraťasy vyzkoušet doma</h2>'
          '<p>Po doručení si kraťasy oblékněte a posaďte se do předkloněné polohy, jako byste seděli na kole. Zkontrolujte, zda se vložka nesvinuje, lem nohavice nestahuje dolů a pas nezůstává odkrytý. '
          'Projděte se po pokoji a udělejte několik dřepů, vyplatí se i krátká jízda na trenažeru. Švy by neměly být cítit, vložka nesmí tlačit v místech, kde budete na sedle opírat váhu. Neprané kousky lze obvykle vrátit podle podmínek konkrétního obchodu, proto je vhodné se s nimi seznámit před koupí.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Nosit pod kraťasy s vložkou spodní prádlo.</li>'
          '<li>Koupit příliš tlustou vložku v domnění, že čím víc pěny, tím větší pohodlí.</li>'
          '<li>Vybrat velikost podle dosavadního oblečení bez ověření velikostní tabulky.</li>'
          '<li>Zanedbat praní vložky hned po jízdě.</li>'
          '<li>Nechat si zimní kalhoty na jarní jízdu, ve které se člověk zbytečně přehřívá.</li>'
          '<li>Podcenit lem nohavice, který se při špatné velikosti zařezává.</li></ul>',
    faq=[('Nosí se pod cyklistické kraťasy spodní prádlo?', 'Ne. Vložka je navržena pro kontakt s tělem a spodní prádlo by vytvářelo další švy a zadržovalo vlhkost. Výjimkou jsou volné MTB kraťasy bez vložky, pod které se nosí speciální cyklistické spodní kalhotky s vložkou.'),
         ('Jak dlouho vydrží cyklistické kraťasy?', 'Záleží na kvalitě a intenzitě používání. Typickým znakem opotřebení je slisovaná vložka, která už netlumí, a ztráta pružnosti látky. Pravidelné praní bez aviváže životnost prodlouží.'),
         ('Jak vybrat správnou velikost?', 'Změřte pas, boky a obvod stehna a porovnejte s velikostní tabulkou konkrétního výrobce. Kraťasy mají sedět přiléhavě, ale nesmí škrtit. Při pochybnostech zvolte tu velikost, ve které se vám v předklonu nezařezává pas.'),
         ('Je lepší model s kšandami, nebo bez nich?', 'Kšandy drží vložku na místě a nezařezávají pás, takže se osvědčují na dlouhých vyjížďkách. Nevýhodou je, že na zastávkách je nutné sundat dres. Na kratší jízdy a rekreační cyklistiku stačí varianta bez kšand.'),
         ('Hodí se MTB kraťasy i na silnici?', 'Dají se použít, ale volný střih má víc tkaniny, která tře a je méně aerodynamická. Při delším šlapání v předklonu je pohodlnější přiléhavý silniční model s kvalitní vložkou.'),
         ('Mám si koupit kraťasy s vložkou, nebo bez?', 'Pro delší jízdy než hodinu je vložka výhodou. Pokud preferujete volné horské kraťasy, můžete zvolit model bez vložky a nosit pod ním spodní kalhotky s vložkou, takže si vybíráte kombinaci podle potřeby.'),
         ('Jak prát cyklistické kalhoty?', 'Po každé jízdě je vyperte nejlépe obrácené, při doporučené teplotě a bez aviváže. Nesušte je na topení ani v sušičce, protože teplo poškozuje elastan a pěnu ve vložce.'),
         ('Co nosit na kole při nule?', 'Dlouhé zateplené kalhoty s větruodolným předkem, pod nimi případně tenkou vrstvu. Důležité jsou i teplé ponožky a rukavice, protože právě nohy a ruce prochladnou nejdřív. Vrstvení umožňuje reagovat na změnu počasí.'),
         ('Jsou dámské cyklistické kalhoty opravdu jiné?', 'Ano. Dámské střihy mají jiné proporce v pase a kyčlích a vložka je tvarovaná pro ženskou anatomii. U unisex nebo pánského modelu může docházet k nepohodlí, proto se vyplatí hledat model určený pro vás.'),
         ('Co si vzít na dlouhou vícedenní túru na kole?', 'Alespoň dvoje kraťasy s vložkou, abyste mohli jedny prát a druhé nosit. Hodí se i tenké dlouhé kalhoty nebo návleky pro chladné ráno a lehké trekingové kalhoty na večer. Praní provádějte při každé příležitosti, vložka tak zůstane čistá.'),
         ('Kde porovnám nabídky cyklistických kraťasů?', 'Na Sportece otevřete konkrétní kousek a uvidíte nabídky českých obchodů vedle sebe, včetně dostupných velikostí. Před nákupem si ověřte velikostní tabulku a materiál.')],
)


# ------------------------------------------------------------------ cyklisticke-dresy
NEW['cyklisticke-dresy'] = dict(long=True,
    title='Cyklistické dresy: krátký i dlouhý rukáv',
    desc='Cyklistické dresy pro silnici, MTB i gravel: krátký a dlouhý rukáv, zip, kapsy, materiály a velikosti. Nabídky českých obchodů vedle sebe.',
    intro='<p>Cyklistický dres vypadá jako obyčejné tričko, jenže je to jeden z nejpromyšlenějších kousků vybavení. Má delší záda, aby se při předklonu nezvedal nad kalhoty, '
          'zip na hrudi pro rychlé větrání a kapsy na zádech, kam se vejde svačina, telefon i bunda. Látka odvádí pot, rychle schne a při jízdě netlačí. '
          'V kategorii <strong>cyklistické dresy</strong> najdete silniční modely s přiléhavým střihem, volnější MTB dresy s kratším zipem i trekingové kousky na výlety a každodenní dojíždění.</p>'
          '<p>Sporteka srovnává nabídky českých obchodů u stejného dresu, takže hned vidíte, kde mají vaši velikost. K dresu se hodí '
          '<a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy a kalhoty</a>, <a href="/cyklisticke-rukavice/">rukavice</a> a <a href="/cyklisticke-helmy/">helma</a>. '
          'Celkový přehled najdete v kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>. Následující text vysvětluje střihy, materiály i to, co po cyklistickém dresu skutečně chtít.</p>',
    guide='<h2>Druhy cyklistických dresů</h2>'
          '<p>Dresy se liší střihem, délkou rukávu i tloušťkou materiálu. Správná volba závisí na tom, kde a jak často jezdíte, a také na ročním období.</p>'
          + T(['Druh dresu', 'Typické použití', 'Střih a zip', 'Na co si dát pozor'], [
              ['Silniční dres s krátkým rukávem', 'léto, rychlá jízda na silnici', 'přiléhavý, delší záda, dlouhý zip', 'při větší tělesné stavbě je nutné ověřit velikost'],
              ['Volný MTB dres', 'horská kola, trail, enduro', 'volnější střih, kratší zip, často delší rukáv', 'může se při jízdě třepetat, pokud je příliš velký'],
              ['Dres s dlouhým rukávem', 'jaro, podzim, ráno', 'přiléhavý rukáv, často tenká zateplená vrstva', 'při oteplení se uvaří, vyplatí se zip'],
              ['Zimní dres a bunda', 'jízda v chladném počasí', 'zateplený, větruodolná přední strana', 'nepodceňujte vrstvení pod ním'],
              ['Triatlonový a závodní jednodílný oblek', 'soutěže, závody', 'extrémně přiléhavý, často bez kapes na zádech', 'pro rekreační jízdu zbytečně specializovaný'],
              ['Dětské dresy', 'děti a mládež', 'volnější střih, pružný materiál', 'děti rychle rostou, proto nekupujte příliš velké kusy'],
              ['Dámské dresy', 'ženy všech disciplín', 'jiné proporce v ramenou, hrudníku a pase', 'unisex velikost nemusí padnout']]) +
          '<p>Pokud pravidelně jezdíte na silnici, vyplatí se mít alespoň dva dresy, protože jeden je vždy v praní. Jezdci na horských kolech často kombinují volný dres se spodním tričkem a bundou, takže v teplém počasí nemusí kupovat nic navíc.</p>'
          '<h2>Střih, velikost a pohodlí</h2>'
          '<p>Dres má sedět těsně, ale ne škrtit. Přiléhavý střih omezuje vlání látky, která by při rychlé jízdě bubnovala, a také zlepšuje odvod potu od těla. V sedle se nesmí zvedat nad kalhoty, záda by měla sahat až přes pas a manžety rukávů ne zařezávat. '
          'U silničních modelů se doporučuje zkusit dres v předklonu na kole, nikoli ve stoje před zrcadlem, protože střih je kreslený pro polohu v sedle. Dlouhé zipy zlepšují větrání, ale u kratších lidí se mohou při předklonu rozevírat a odhalit hruď.</p>'
          + T(['Míra těla', 'Kde měřit', 'Kontrola při zkoušení'], [
              ['Hrudník', 'v nejširším místě pod pažemi', 'dres netlačí při hlubokém nádechu'],
              ['Pas', 'v nejužším místě trupu', 'dolní lem drží na místě, neroluje se'],
              ['Délka trupu', 'od krku k pasu a výš', 'záda jsou při předklonu stále zakryta'],
              ['Obvod paže', 'v nejsilnějším místě bicepsu', 'rukáv netlačí a nevyjíždí nahoru']]) +
          '<p>Výrobci mají odlišné velikostní tabulky, a to i mezi evropskými značkami. Proto si vždy porovnejte vlastní míry s tabulkou u konkrétního produktu a pokud jste na hranici dvou velikostí, vyberte podle toho, zda dres chcete nosit samostatně, nebo s vrstvami pod ním.</p>'
          '<h2>Materiály a technologie</h2>'
          '<p>Většina dresů je z polyesteru, někdy kombinovaného s elastanem pro pružnost. Syntetika odvádí pot od těla a rychle schne, takže při jízdě necítíte vlhkost. Hladký povrch snižuje tření, síťované zóny na zádech a pod pažemi zvyšují prodyšnost. '
          'Merino vlna, kterou někteří jezdci používají jako spodní vrstvu, je příjemná na dotek, hřeje i mokrá a zadržuje méně zápachu, ale schne pomaleji. Dresy s UV ochranou ocení lidé, kteří tráví na kole celé dny na slunci. Reflexní prvky na zádech zvyšují viditelnost za soumraku.</p>'
          '<ul><li><strong>Zip:</strong> plný zip umožňuje vyvětrat při stoupání, krátký zip je lehčí a méně se zasekává. Při nákupu zkontrolujte, zda je zip zakrytý, aby neškrábal o kůži.</li>'
          '<li><strong>Kapsy na zádech:</strong> většinou tři, uprostřed často zipová na doklady. Čím víc se do nich naloží, tím víc se dres propadá, takže těžké věci patří do batohu nebo brašny.</li>'
          '<li><strong>Silikonový lem:</strong> drží dres u pasu na místě a brání jeho svinování.</li>'
          '<li><strong>Prodyšné zóny:</strong> zlepšují chlazení, hodí se hlavně na léto a při vysoké intenzitě.</li></ul>'
          '<h2>Jak vybrat podle ročního období</h2>'
          '<h3>Léto</h3>'
          '<p>V horku se hledají lehké, tenké a světlé dresy s dlouhým zipem. Rozepnutý zip navíc zlepší větrání. Světlé barvy odrážejí sluneční záření, zatímco tmavé se více zahřívají. Při polední jízdě se vyplatí dres s UV ochranou a krém na odkryté části kůže.</p>'
          '<h3>Jaro a podzim</h3>'
          '<p>V přechodném období se osvědčuje dres s dlouhým rukávem nebo krátký rukáv s návleky z kategorie <a href="/cyklisticke-navleky/">cyklistické návleky</a>. Přes dres lze obléct větrovku nebo vestu z kategorie <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>. Vrstvení je flexibilnější než jedna silná bunda.</p>'
          '<h3>Zima</h3>'
          '<p>Při nízkých teplotách jde o systém tří vrstev. Spodní odvádí pot, střední hřeje a vnější chrání před větrem a deštěm. Samostatný zimní dres bývá zateplený, ale nenahradí kvalitní bundu. U delších jízd v mrazu dbejte na teplé <a href="/cyklisticke-rukavice/">rukavice</a> a <a href="/cyklisticke-ponozky/">ponožky</a>.</p>'
          '<h2>Silnice, gravel, MTB a město</h2>'
          '<p>Silniční jezdci preferují přiléhavé dresy z lehkého materiálu a delším zipem, protože zvládají vysokou rychlost a dlouhé výjezdy. Na gravelu se hodí něco mezi silnicí a terénem, často s odolnějším materiálem na ramenou a víc kapsami. '
          'Horští cyklisté volí volnější střih, který se nepřilepí k tělu při namáhavém výšlapu, a materiál odolný vůči otěru větvemi. Městští cyklisté mohou zvolit dres, který vypadá jako běžné tričko, ale má reflexní prvky a kapsu na záda. '
          'Pro dojíždění stačí funkční tričko, ale cyklistický dres při delší cestě vyřeší pot a kapsy.</p>'
          '<h2>Co dres neudělá</h2>'
          '<p>Cyklistický dres je funkční oblečení, ne ochranný prvek. Neslouží jako náhrada helmy, nechrání při pádu a ani sebelepší síťovina nezaručí, že se nespálíte. Proto se při výběru dresu zamyslete i nad dalším vybavením: <a href="/cyklisticke-helmy/">cyklistickou helmou</a>, <a href="/cyklisticke-bryle/">brýlemi</a> a <a href="/cyklo-svetla/">světly</a> pro viditelnost.</p>'
          '<h2>Péče o dres</h2>'
          '<ul><li>Perte po každé jízdě, ideálně obrácený, při teplotě uvedené na štítku.</li>'
          '<li>Zip před praním zapněte a suchý zip uzavřete, aby se látka nepoškodila.</li>'
          '<li>Nepoužívejte aviváž, která zalepuje vlákna a snižuje odvod potu, ani bělicí prostředky.</li>'
          '<li>Nesušte v sušičce, látku nevyžehlujte, potisk by se mohl poškodit.</li>'
          '<li>Skvrny od mazadla ošetřete okamžitě a lokálně, před praním je nenechte zaschnout.</li>'
          '<li>Při delším skladování držte dresy na suchém místě, aby nezapáchaly.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete mimo jiné ' + B(('silvini', 'Silvini'), ('siroko', 'Siroko'), ('rockbros', 'Rockbros'), ('haven', 'Haven'), ('eleven', 'Eleven'), ('loeffler', 'Loeffler'), ('kilpi', 'Kilpi'), ('keada-sports', 'Keada Sports'), ('etape', 'Etape'), ('arcore', 'Arcore')) + '. '
          'Silvini a Etape jsou české značky se širokou nabídkou střihů a barev. Loeffler je rakouský výrobce funkčního oblečení, Kilpi pokrývá outdoorové vybavení včetně cyklistiky. Siroko a Rockbros nabízejí kousky pro rekreační i ambicióznější jezdce a Haven se zaměřuje na pohodlí. '
          'Jednotlivé značky mají odlišné střihy, takže se vyplatí vždy projít velikostní tabulku.</p>'
          '<h2>Související kategorie</h2>'
          '<p>K dresu patří <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy a kalhoty</a> a <a href="/cyklisticka-obuv/">cyklistická obuv</a>. Na výlety do hor doplníte vybavení z kategorie <a href="/sportovni-ponozky/">sportovní ponožky</a> nebo <a href="/sportovni-rukavice/">sportovní rukavice</a>. '
          'Celý rozsah vybavení pro jízdu najdete v kategorii <a href="/cyklistika/">cyklistika</a> a díly pro údržbu v kategorii <a href="/cyklo-dily/">cyklistické díly</a>. Pokud často dojíždíte, hodí se <a href="/cyklo-tasky-a-nosice/">cyklistické tašky a nosiče</a> a <a href="/cyklo-lahve-a-drzaky/">láhve a držáky</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Zvolit příliš volný dres, který na silnici bubnuje ve větru.</li>'
          '<li>Zkoušet dres jen ve stoje, ne v předklonu jako na kole.</li>'
          '<li>Koupit dres bez kapes na zádech a pak řešit, kam dát telefon a svačinu.</li>'
          '<li>Podcenit viditelnost, zvlášť ráno a večer.</li>'
          '<li>Prát dres s aviváží, která zhoršuje odvod potu.</li>'
          '<li>Nosit bavlněné tričko pod dres, které nasákne potem a prochladí.</li></ul>'
          '<h2>Pro koho je tato kategorie</h2>'
          '<p>Pro každého, kdo tráví na kole víc než půl hodiny. Rekreační cyklisté ocení, že jim dres odvede pot, a pokud jezdí v týmu, ocení i shodné barvy. Závodníci hledají střih s co nejmenším odporem. '
          'Horští jezdci využijí odolné materiály a volnější střih. Dárek pro cyklistu se dá zvolit podle dosavadního oblečení nebo oblíbené barvy, jen je dobré nezapomenout na velikost. '
          'A sběratelé týmových dresů si mohou vybrat z různých motivů a barev.</p>',
    faq=[('Proč mají cyklistické dresy delší záda?', 'Při předklonu v sedle by se kratší tričko zvedlo a odhalilo záda. Delší zadní část zakrývá spodní záda i v nízké poloze a chrání je před chladem a vlhkostí. Zároveň zadní kapsy sedí níž, kde se do nich lépe nakládá.'),
         ('Jaký dres zvolit na silnici a jaký na MTB?', 'Na silnici se hodí přiléhavý střih z lehkého materiálu s delším zipem, který omezuje odpor vzduchu. Na horských kolech je lepší volnější a odolnější dres s kratším zipem, který se nepřilepí k tělu a snese kontakt s větvemi.'),
         ('Jak poznám správnou velikost dresu?', 'Změřte hrudník, pas a délku trupu a porovnejte s tabulkou výrobce. Dres má přiléhat, ale nesmí tlačit ani se zvedat při předklonu. Pokud váháte mezi dvěma velikostmi, zvolte podle toho, zda budete pod dresem nosit další vrstvu.'),
         ('Mohu v dresu jezdit v zimě?', 'Jen v zateplené verzi a s vhodnými vrstvami pod ním. Spodní vrstva odvádí pot, dres hřeje a vnější bunda chrání před větrem. Samotný letní dres na mráz nestačí.'),
         ('K čemu slouží kapsy na zádech?', 'Vejde se do nich svačina, telefon, klíče, oblékací vrstva nebo drobné nářadí. Mezi ně se rozděluje váha, aby se dres nehoupal. Těžké věci raději patří do brašny nebo batohu.'),
         ('Jak prát cyklistický dres?', 'Po každé jízdě, ideálně obrácený naruby, při teplotě podle štítku a bez aviváže. Zip zapněte, nesušte na radiátoru ani v sušičce a potisk nežehlete. Skvrny od mazadla ošetřete hned.'),
         ('Je lepší dres ze syntetiky, nebo z merina?', 'Syntetika rychle schne a odvádí pot, takže se hodí na intenzivní jízdu a horko. Merino je příjemné na dotek a méně zapáchá, ale schne pomaleji a bývá náročnější na péči. Mnoho jezdců používá merino jako spodní vrstvu.'),
         ('Jak zvolit dres pro dítě?', 'Dětský dres by měl mít pružný materiál a volnější střih, ale ne tak velký, aby se vlnil. Pro děti jsou důležité reflexní prvky a pohodlný zip. Vzhledem k rychlému růstu se vyplatí neinvestovat do výjimečně drahých kousků.'),
         ('Hodí se cyklistický dres na dojíždění do práce?', 'Ano, pokud trasa trvá delší dobu nebo jedete rychleji. Dres odvede pot a kapsy ukryjí drobnosti, ale do kanceláře je praktické mít převlečení. Pro pomalejší městské jízdy stačí funkční tričko s reflexními prvky.'),
         ('Kde porovnám nabídky cyklistických dresů?', 'Na Sportece otevřete konkrétní dres a uvidíte nabídky českých obchodů vedle sebe včetně dostupných velikostí. Před nákupem zkontrolujte velikostní tabulku konkrétní značky.')],
)


# ------------------------------------------------------------------ cyklo-pohon
NEW['cyklo-pohon'] = dict(long=True,
    title='Pohon kola: přehazovačky, řetězy, kazety',
    desc='Pohon kola: přehazovačky, řetězy, kazety, kliky, převodníky a řazení. Jak vybrat kompatibilní díly pro silnici, MTB a gravel a srovnat ceny.',
    intro='<p>Pohon je část kola, která pracuje při každém otočení pedálů a zároveň se opotřebovává nejrychleji. Řetěz se natahuje, zuby kazety se obrušují a lanka stárnou. '
          'V kategorii <strong>pohon</strong> najdete přehazovačky a přesmykače, řetězy, kazety a pastorky, kliky s převodníky, řadicí páky, lanka a bowdeny i náhradní díly pro opravu. '
          'Všechno je potřeba vybírat podle počtu rychlostí, typu řazení a rozměrů, takže jeden špatný údaj dokáže znehodnotit celý nákup.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného dílu, takže vidíte, kdo má skladem přesnou specifikaci. K pohonu patří <a href="/cyklo-pedaly/">pedály</a>, '
          '<a href="/cyklo-kola-a-rafky/">kola a ráfky</a> a <a href="/cyklo-brzdy/">brzdy</a>, přehled všech dílů najdete v <a href="/cyklo-dily/">cyklistických dílech</a>. '
          'Další text vysvětluje, jak se v kompatibilitě vyznat a kdy opravdu vyměnit celou skupinu.</p>',
    guide='<h2>Z čeho se skládá pohon</h2>'
          '<p>Pohon převádí sílu z nohou na zadní kolo a umožňuje měnit převod. Skládá se z několika dílů, které spolu musejí ladit.</p>'
          + T(['Díl', 'Co dělá', 'Co určuje kompatibilitu'], [
              ['Kliky a převodníky', 'přenášejí sílu z pedálů na řetěz', 'počet převodníků, rozteč šroubů, osa středového složení'],
              ['Středové složení', 'otočně uložené kliky v rámu', 'typ závitu nebo zalisování, šířka pouzdra rámu'],
              ['Řetěz', 'spojuje převodník a kazetu', 'počet rychlostí, šířka, spojka'],
              ['Kazeta nebo pastorky', 'sada ozubených kol na zadním náboji', 'počet rychlostí, typ unašeče, rozsah zubů'],
              ['Zadní přehazovačka', 'přehazuje řetěz po kazetě a napíná ho', 'počet rychlostí, maximální velikost zubů, délka ramínka'],
              ['Přesmykač', 'přesouvá řetěz mezi předními převodníky', 'typ uchycení, průměr trubky, počet převodníků'],
              ['Řadicí páky a lanka', 'ovládají přehazovačku a přesmykač', 'počet rychlostí, mechanické nebo elektronické řazení'],
              ['Bowdeny a lanka', 'vedou povel k řazení', 'průměr, délka, materiál']]) +
          '<p>Základní pravidlo je prosté: počet rychlostí musí souhlasit u řetězu, kazety a řadicí páky. Pokud je v jednom místě odlišný, řazení se bude trhat nebo vůbec nefungovat.</p>'
          '<h2>Počet rychlostí a typ kola</h2>'
          '<p>Dříve se jezdilo se dvěma nebo třemi převodníky vpředu, dnes je u horských kol i gravelu běžný jeden převodník s širokou kazetou. Silniční kola většinou drží dva převodníky a kazetu s menším rozsahem. '
          'Čím víc rychlostí, tím užší řetěz a tím přesnější nastavení. Starší sestavy s méně rychlostmi jsou odolnější, ale často už je dnes obtížné sehnat součástky.</p>'
          + T(['Typ kola', 'Obvyklé uspořádání', 'Poznámka'], [
              ['Silniční kolo', 'dva převodníky vpředu, široká sada pastorků vzadu', 'rovné přechody mezi rychlostmi, vyšší tempo'],
              ['Gravel', 'jeden nebo dva převodníky, širší kazeta', 'kompromis mezi rychlostí a lezením do kopce'],
              ['Horské kolo', 'obvykle jeden převodník a velmi široká kazeta', 'jednoduchá obsluha, žádný přesmykač'],
              ['Trekingové a městské kolo', 'často tři převodníky nebo moderní jeden vpředu', 'důležitá odolnost a jednoduchý servis'],
              ['Elektrokolo', 'zesílený řetěz a kazeta', 'vyšší zatížení vlivem motoru, viz '
               '<a href="/ebike-baterie/">baterie pro elektrokola</a>']]) +
          '<h2>Řetěz: opotřebení a výměna</h2>'
          '<p>Řetěz se při používání nenatahuje v pravém slova smyslu, ale opotřebovávají se čepy a pouzdra a řetěz se prodlužuje. Natažený řetěz pak obrušuje zuby kazety i převodníků, a pokud ho necháte příliš dlouho, vymění se i drahé díly. '
          'Opotřebení změříte speciálním měřidlem řetězu, které ukáže procento natažení. Při včasné výměně vydrží kazeta a převodníky výrazně déle. Řetěz čistěte a mažte vhodným olejem, který se nechová jako magnet na prach.</p>'
          '<ul><li><strong>Spojka:</strong> většina řetězů se dnes spojuje rychlospojkou, kterou lze opakovaně rozepnout. U některých systémů se používá jednorázový čep.</li>'
          '<li><strong>Šířka řetězu:</strong> musí odpovídat počtu rychlostí a typu kazety, jinak se bude chovat hlučně a bude se opotřebovávat.</li>'
          '<li><strong>Délka:</strong> řetěz se zkracuje podle největšího převodníku a pastorku s rezervou, aby se ramínko přehazovačky nepřetáhlo.</li>'
          '<li><strong>Směr:</strong> některé řetězy mají vnější a vnitřní stranu, kterou je nutno při montáži dodržet.</li></ul>'
          '<h2>Kazeta, pastorky a unašeč</h2>'
          '<p>Kazeta je sada ozubených koleček na zadním náboji. Nasazuje se na unašeč, který existuje v několika standardech podle výrobce a generace. Staré závitové věnce se našroubují přímo na náboj, novější kazety se nasouvají na drážkovaný unašeč a utahují maticí. '
          'Než koupíte novou kazetu, ověřte, jaký unašeč máte a kolik rychlostí zvládne. U moderních sestav s velmi širokou kazetou může být nutný jiný unašeč, než jaký je na kole teď. '
          'Rozsah kazety je dán nejmenším a největším pastorkem, větší rozsah usnadní lezení do kopce, ale přechody mezi rychlostmi budou větší.</p>'
          '<h2>Přehazovačka a přesmykač</h2>'
          '<p>Zadní přehazovačka mění převod tím, že řetěz posouvá po kazetě, a zároveň ho udržuje napnutý. Při výběru sledujte maximální velikost největšího pastorku, celkovou kapacitu a délku ramínka. '
          'Krátké ramínko je vhodné pro úzké kazety, dlouhé pro široké rozsahy. Přesmykač přesouvá řetěz mezi předními převodníky. Je třeba vybrat správný typ uchycení k rámu, průměr trubky a rozteč převodníků. '
          'Na kolech s jedním převodníkem se přesmykač vůbec nepoužívá.</p>'
          '<h3>Mechanické a elektronické řazení</h3>'
          '<p>Mechanické řazení využívá lanka a bowdeny, je jednoduché a snadno se opravuje v terénu. Elektronické řazení posílá povely bezdrátově nebo kabelem, řazení je přesnější a nastavuje se samo, ale vyžaduje baterie a dražší díly. '
          'Pro rekreační jezdce stačí mechanika, pro závodníky a nadšence může být elektronika příjemnou výhodou.</p>'
          '<h2>Kliky a převodníky</h2>'
          '<p>Kliky se vybírají podle délky, osy a uchycení převodníků. Standardní délky se pohybují zhruba mezi 165 a 175 mm. Delší kliky dávají větší páku, kratší umožňují vyšší kadenci a menší náročnost na klouby, ale ne každému sedí stejně. '
          'Převodník se vybírá podle počtu zubů, který ovlivňuje celkový převod. Menší převodník usnadní lezení, větší zvýší maximální rychlost. U moderních sestav často stačí vyměnit samotný převodník, aniž by se musely měnit kliky.</p>'
          '<p>Součástí pohonu je i středové složení. Jeho typ závisí na rámu a může být závitové nebo zalisované. Špatný výběr znamená, že se nevejde do pouzdra, nebo se na něm kliky nebudou správně otáčet. '
          'Bez kvalitního nářadí je lepší nechat montáž servisu. Nářadí najdete v kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>, další péči o kolo v kategorii <a href="/cyklo-udrzba/">údržba kola</a>.</p>'
          '<h2>Jak zjistit, co potřebujete</h2>'
          '<ol><li>Spočítejte pastorky na zadním kole a převodníky na klice.</li>'
          '<li>Zjistěte značku a řadu stávajících dílů, bývá vyražena na přehazovačce, klice a páce.</li>'
          '<li>Změřte opotřebení řetězu, abyste věděli, zda stačí výměna řetězu, nebo i kazety.</li>'
          '<li>Ověřte typ unašeče a šířku osy.</li>'
          '<li>Zapište si přesné označení a v nabídce porovnejte, které díly jsou kompatibilní.</li></ol>'
          '<h2>Kdy se vyplatí vyměnit celou skupinu</h2>'
          '<p>Když jsou opotřebované současně řetěz, kazeta, převodníky i lanka, bývá rozumné vyměnit je společně. Nové díly pak spolu zapadnou a řazení je hned přesné. '
          'Celá skupina dává smysl také při přechodu na jiný počet rychlostí, protože pak se mění páky, přehazovačka, kazeta i řetěz. Pokud jde jen o jeden poškozený kus, například ohnutou přehazovačku po pádu, stačí vyměnit právě ten a případně zkontrolovat závěs rámu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce zastoupené jsou ' + B(('shimano', 'Shimano'), ('sram', 'Sram'), ('kmc', 'KMC'), ('force', 'Force'), ('connex', 'Connex'), ('nexelo', 'Nexelo'), ('max1', 'Max1'), ('hms', 'HMS'), ('reverse', 'Reverse'), ('sunrace', 'SunRace'), ('unior', 'Unior'), ('microshift', 'Microshift')) + '. '
          'Shimano a Sram jsou velcí výrobci kompletních skupin, KMC se specializuje na řetězy, SunRace a Microshift nabízejí kazety a řazení pro širší škálu kol. Force, Connex, Nexelo, Max1 a HMS pokrývají levnější díly a doplňky, Unior vyrábí nářadí a Reverse nabízí cyklistické komponenty.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Pohon spolupracuje s dalšími díly. Na zadní kolo navazuje <a href="/cyklo-kola-a-rafky/">sada kol a ráfků</a>, pláště a duše najdete v kategorii <a href="/plaste-a-duse/">pláště a duše</a>. '
          'Pro ovládání patří k pohonu i <a href="/cyklo-riditka/">řídítka a představce</a> a <a href="/sedla-a-gripy/">gripy a sedla</a>. Při výběru celého kola se podívejte na <a href="/silnicni-kola/">silniční kola</a> nebo <a href="/cyklistika/">cyklistiku</a> obecně.</p>'
          '<h2>Údržba pohonu</h2>'
          '<ul><li>Řetěz po každé větší jízdě otřete a občas odmastěte, poté naneste vhodný olej a přebytek setřete.</li>'
          '<li>Kazetu a převodníky čistěte kartáčem, nejlépe po sundání zadního kola.</li>'
          '<li>Lanka a bowdeny kontrolujte, při zadrhávání výměna většinou pomůže víc než dotažení.</li>'
          '<li>Přehazovačku udržujte rovnou, ohnuté závěsné oko způsobuje nepřesné řazení.</li>'
          '<li>Pravidelně měřte natažení řetězu a vyměňte ho včas.</li>'
          '<li>Pokud řetěz přeskakuje pod zátěží, může být opotřebovaná kazeta nebo řetěz.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupit kazetu s jiným počtem rychlostí, než má řetěz a páka.</li>'
          '<li>Nechat řetěz natáhnout tak, že zničí kazetu i převodníky.</li>'
          '<li>Použít přehazovačku s malou kapacitou na kazetu s velkým rozsahem.</li>'
          '<li>Zaměnit typ unašeče a zjistit to až po doručení.</li>'
          '<li>Montovat díly bez dotažení předepsaným momentem a bez nářadí.</li>'
          '<li>Míchat díly různých výrobců, aniž byste ověřili jejich kompatibilitu.</li></ul>'
          '<h2>Pro koho je tato kategorie</h2>'
          '<p>Pro každého, kdo opravuje nebo vylepšuje své kolo. Začátečníkům postačí výměna řetězu a případně kazety po několika tisících kilometrů. Domácí mechanici si zde vyberou součástky na opravu a ti, kdo chtějí lehčí nebo rychlejší kolo, najdou výkonnější skupiny. '
          'Servisy a prodejce zajímají náhradní díly a nářadí. Dobrou zprávou je, že většinu dílů lze koupit samostatně, takže není nutné měnit celé kolo, aby fungovalo jako nové.</p>',
    faq=[('Jak poznám, kolik rychlostí mám?', 'Spočítejte pastorky na zadním kole a vynásobte počtem převodníků vpředu. Pro nákup dílů je důležitější počet pastorků vzadu, protože podle něj se vybírá řetěz, kazeta, přehazovačka i páka.'),
         ('Kdy vyměnit řetěz?', 'Když ho měřidlem opotřebení naměříte na hranici udávané výrobcem. Včasná výměna ušetří kazetu a převodníky, které by se jinak obrusovaly. Při pravidelné jízdě je dobré řetěz kontrolovat po několika stovkách kilometrů.'),
         ('Jde použít řetěz od jiného výrobce než kazetu?', 'Obvykle ano, pokud odpovídá počet rychlostí a šířka řetězu. U moderních sestav s více rychlostmi je vhodné držet kompatibilní řadu, aby řazení bylo hladké.'),
         ('Stačí vyměnit jen kazetu?', 'Pokud je opotřebovaný řetěz, měl by se měnit společně s kazetou. Nový řetěz na starou kazetu často přeskakuje, protože zuby mají jiný tvar. V ideálním případě se mění obojí současně.'),
         ('Jaký je rozdíl mezi kazetou a pastorky?', 'Kazeta je sada koleček nasazená na unašeč s drážkami, pastorky ve formě závitového věnce se našroubují přímo na náboj. Kazety jsou v dnešních kolech standardem, věnce se vyskytují u starších a levných kol.'),
         ('Hodí se jeden převodník vpředu?', 'Na horských kolech a gravelu ano, pohon je jednodušší a lehčí a odpadá přesmykač. Nevýhodou jsou větší skoky mezi rychlostmi. Silniční jezdci častěji zůstávají u dvou převodníků kvůli plynulejším přechodům.'),
         ('Čím mazat řetěz?', 'Vhodným olejem na řetěz, který odpovídá počasí a terénu. Suchý olej se hodí na prašné a suché trasy, vlhký na déšť. Po nanesení přebytek setřete, aby se na něm nelepil prach.'),
         ('Co je to kapacita přehazovačky?', 'Je to součet rozdílu mezi největším a nejmenším pastorkem a rozdílu mezi největším a nejmenším převodníkem, který přehazovačka zvládne. Pokud je kapacita nižší než potřeba, řetěz se v krajních kombinacích buď přepíná špatně, nebo se nenapne.'),
         ('Je elektronické řazení lepší než mechanické?', 'Je přesnější a nevyžaduje seřizování lanek, ale potřebuje baterii a stojí víc. Mechanika je jednodušší a snadno se opravuje. Pro běžnou rekreační jízdu stačí mechanika, elektronika je pohodlnou volbou pro náročnější jezdce.'),
         ('Kde porovnám nabídky dílů pohonu?', 'Na Sportece otevřete konkrétní díl a uvidíte nabídky českých obchodů vedle sebe. Před koupí vždy zkontrolujte počet rychlostí, typ unašeče a rozměry, aby se díl vešel na vaše kolo.')],
)
