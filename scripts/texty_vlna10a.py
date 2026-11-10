"""sporteka.cz — wave 10a (3. 11. 2026): the biggest categories that had no text of their own.
Search phrases from Marketing Miner (cs, 11/2026). Brands from the live catalogue. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ rybareni
NEW['rybareni'] = dict(short=True,
    title='Rybářské potřeby – pruty, navijáky, nástrahy | Sporteka',
    desc='Rybářské potřeby na jednom místě: pruty, navijáky, vlasce, nástrahy a oblečení. Porovnejte ceny z českých obchodů a vyberte výbavu pro svůj způsob lovu.',
    intro='<p><strong>Rybářské potřeby</strong> se dělí podle způsobu lovu, a ten je prvním rozhodnutím při nákupu. Jiný prut a naviják potřebuje přívlačář na štiku, jiný kapr na vodě s dlouhými nahazovanými vzdálenostmi a jiný muškař na říčním pstruhu. Proto je tahle kategorie rozdělená na pruty, navijáky, vlasce, nástrahy a doplňky.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů na jednom místě. Začít můžete u <a href="/rybarske-pruty/">rybářských prutů</a>, <a href="/rybarske-navijaky/">navijáků</a> a <a href="/vlasce-a-snury/">vlasců a šňůr</a>, pro přívlač vybrat <a href="/nastrahy-a-navnady/">nástrahy a návnady</a> a pro muškaření sáhnout po <a href="/muskareni/">muškařské výbavě</a>. Praktické jsou i <a href="/rybarske-tasky/">tašky a krabičky</a> a pro dlouhé pobyty u vody <a href="/bivaky-a-kresla/">bivaky, lehátka a křesla</a>.</p>',
    guide='<h2>Jak vybrat rybářskou výbavu</h2>'
          '<p>Nejdřív si ujasněte, na jakou rybu a na jaké vodě chcete lovit. Teprve potom vybírejte prut, naviják a vlasec, které k sobě musí ladit. Komplet sestavený z dílů různých kategorií je častý zdroj zklamání.</p>'
          '<h3>Podle způsobu lovu</h3>'
          + T(['Způsob lovu', 'Typická výbava'], [['Přívlač (štika, candát, okoun)', 'kratší rychlejší prut, malý až střední naviják, splétaná šňůra, gumové a tvrdé nástrahy'], ['Kaprařina a feeder', 'delší prut s testní křivkou, naviják s volným chodem, silnější vlasec, návnady a háčky'], ['Muškaření', 'muškařský prut a naviják podle třídy šňůry, mušky, vázaný návazec'], ['Mořský rybolov', 'odolné pruty a navijáky proti soli, těžší olova a návazce'], ['Sbírka pro děti', 'krátký lehký prut, jednoduchý naviják, plováky a háčky']]) +
          '<h3>Prut a naviják</h3>'
          '<p>Prut se vybírá podle délky, akce a hmotnosti nástrahy, kterou unese. Naviják musí odpovídat velikostí a převodem. Příliš těžký naviják na lehkém prutu nevyváží celou sestavu.</p>'
          '<h3>Vlasec a šňůra</h3>'
          '<p>Monofilní vlasec se natahuje a odpouští chyby, splétaná šňůra je tenčí a přesně přenáší záběr, ale potřebuje vhodný naviják a návazec. Na štiku se používá ocelové nebo fluorocarbonové návazce, na kapra silnější vlasec.</p>'
          '<h3>Nástrahy a návnady</h3>'
          '<p>Ke každému způsobu lovu patří jiné nástrahy. Gumové nástrahy, wobblery, třpytky a jigy se používají na dravce, boilies a pelety na kapra a živé nebo umělé návnady na plotice a okouny.</p>'
          '<h3>Rybářské oblečení a doplňky</h3>'
          '<p>Voděodolná bunda, nepromokavé kalhoty, rybářská obuv a čepice se hodí hlavně na podzim a jaro. Tašky, pouzdra a krabičky udrží háčky a nástrahy v pořádku, podložky a kleště pomáhají s bezpečným zacházením s rybou.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("daiwa", "Daiwa"), ("shimano", "Shimano"), ("mikado", "Mikado"), ("delphin", "Delphin"), ("westin", "Westin"), ("rapala", "Rapala"), ("savage-gear", "Savage Gear"), ("fox", "Fox"), ("sybai", "Sybai"), ("hends", "Hends"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Nákup sestavy bez ohledu na způsob lovu.</li><li>Příliš silný vlasec, který omezuje nahazování a odrazuje ryby.</li><li>Zanedbaná brzda navijáku, která při záseku pustí vlasec příliš těžce nebo příliš lehce.</li></ul>'
          '<h3>Péče o výbavu</h3>'
          '<p>Po každém výletě naviják opláchněte čistou vodou, vysušte pruty a vlasec u zimních výprav zkontrolujte. Nástrahy skladujte odděleně, aby si nepoškodily barvy a háčky.</p>',
    faq=[('Co potřebuji, abych mohl začít s rybařením?', 'Prut, naviják, vlasec, háčky, plováky nebo nástrahy a rybářský lístek. Další vybavení se přidává podle toho, jak lovíte.'),
         ('Jak vybrat prut?', 'Podle způsobu lovu: délka, akce a hmotnost nástrahy se řídí tím, na jakou rybu a jak daleko lovíte.'),
         ('Jaký vlasec zvolit?', 'Monofilní je univerzální a odpouští chyby, splétaná šňůra je tenčí a citlivější. Záleží na způsobu lovu.'),
         ('Co je přívlač?', 'Lov dravých ryb na umělé nástrahy, které prut vede vodou jako kořist.'),
         ('Co je kaprařina?', 'Lov kaprů na boilies a další návnady, často s vícero pruty a dlouhým pobytem u vody.'),
         ('Jak vybrat výbavu pro dítě?', 'Krátký lehký prut, jednoduchý naviják a plováky nebo malé nástrahy. Pro první pokusy stačí malá sada.'),
         ('Jak pečovat o naviják?', 'Po výletě ho opláchnout čistou vodou a nechat uschnout, před sezónou zkontrolovat brzdu a promazat podle návodu.')],
)

# ------------------------------------------------------------------ cepice-a-celenky
NEW['cepice-a-celenky'] = dict(short=True,
    title='Čepice, kšiltovky a čelenky – sport a styl | Sporteka',
    desc='Čepice, kšiltovky a čelenky: sportovní, zimní, fanouškovské i běžecké. Porovnejte ceny z českých obchodů a vyberte velikost a materiál podle sportu.',
    intro='<p><strong>Kšiltovky, čepice a čelenky</strong> ochrání hlavu před sluncem, větrem i chladem a zároveň patří k nejčastějším doplňkům sportovců i fanoušků. Kšiltovka chrání oči před sluncem při běhu a cyklistice, zimní čepice zadrží teplo a čelenka drží vlasy a pot mimo oči.</p>'
          '<p>Na Sportece najdete <strong>kšiltovky pánské, dámské i dětské</strong>, pletené čepice, nákrčníky a čelenky z českých obchodů na jednom místě a porovnáte jejich ceny. Zvlášť vybraný sortiment pro zimní sporty je v kategorii <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>, doplnit je můžete o <a href="/nakrcniky-a-satky/">nákrčníky a kukly</a> a <a href="/merino-doplnky/">merino doplňky</a>.</p>',
    guide='<h2>Jak vybrat čepici nebo kšiltovku</h2>'
          '<p>Rozhodněte, k čemu ji budete nosit. Kšiltovka na běh má být lehká a prodyšná, fanouškovská a módní se hodí do města a zimní čepice musí především hřát a držet na hlavě.</p>'
          '<h3>Typy kšiltovek</h3>'
          '<ul><li><strong>Baseballová kšiltovka:</strong> zahnutý kšilt a uzavřená zadní část, univerzální.</li>'
          '<li><strong>Snapback:</strong> rovný kšilt a plastový pásek vzadu, oblíbená u fanoušků týmů.</li>'
          '<li><strong>Trucker:</strong> síťovinový zadní díl pro lepší větrání.</li>'
          '<li><strong>Běžecká a cyklistická:</strong> lehká, rychle schnoucí, často s reflexními prvky.</li></ul>'
          '<h3>Velikost a střih</h3>'
          '<p>Obvod hlavy změřte měkkým metrem nad ušima. Čepice se vyrábějí v pevných velikostech, nastavitelné s páskem nebo se zapínáním na suchý zip. Dětské modely mají menší obvod a lehčí materiál.</p>'
          '<h3>Materiály</h3>'
          '<ul><li><strong>Bavlna:</strong> příjemná a prodyšná, ale pomalu schne.</li>'
          '<li><strong>Polyester a funkční vlákna:</strong> rychle schnou a odvádějí pot.</li>'
          '<li><strong>Merino a vlna:</strong> hřejí i při vlhku a méně zapáchají.</li>'
          '<li><strong>Fleece:</strong> lehký a hřejivý, vhodný pro chladné dny.</li></ul>'
          '<h3>Čelenky</h3>'
          '<p>Sportovní čelenka odvádí pot a drží vlasy, zimní chrání uši před chladem. Ke sportu se hodí pružná a široká, která se nesesouvá. Pro děti existují také měkké modely bez švů.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce najdete {B(("new-era", "New Era"), ("47-brand", "47 Brand"), ("mitchell-ness", "Mitchell &amp; Ness"), ("fjallraven", "Fjällräven"), ("adidas", "Adidas"), ("nike", "Nike"), ("under-armour", "Under Armour"), ("kappa", "Kappa"))}. Fanouškovské kšiltovky jsou k dispozici s logy klubů a týmů.</p>'
          '<h3>Péče o čepice a kšiltovky</h3>'
          '<p>Kšiltovku perte ručně a nesušte ji na radiátoru, kšilt by se zdeformoval. Pletené čepice perte šetrně a sušte vleže, aby se nevytáhly.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Bavlněná kšiltovka na dlouhý běh, která se nasákne potem.</li><li>Příliš těsná čepice, která tlačí a bolí hlava.</li><li>Zimní čepice bez krytí uší při větru.</li></ul>',
    faq=[('Jakou kšiltovku vybrat na sport?', 'Lehkou, prodyšnou a rychle schnoucí z polyesteru. Při běhu pomůže také reflexní detail a pásek na zátylku.'),
         ('Jak změřit velikost čepice?', 'Měkkým metrem kolem hlavy nad ušima a nad obočím, hodnotu porovnejte s tabulkou výrobce.'),
         ('Co je snapback?', 'Kšiltovka s rovným kšiltem a plastovým pásem vzadu pro nastavení velikosti.'),
         ('Jak prát kšiltovku?', 'Ručně v teplé vodě, bez ždímání, sušit na vzduchu. Pračka může deformovat kšilt.'),
         ('Jaká čepice do zimy?', 'Pletená z vlny nebo merina, ideálně s podšívkou z fleece, která zakryje uši.'),
         ('Hodí se čelenka na běhání?', 'Ano, odvádí pot a drží vlasy. V zimě existují čelenky, které chrání uši.'),
         ('Jak vybrat čepici pro dítě?', 'Podle obvodu hlavy, z měkkého materiálu bez škrábavých švů a s úpravou, která chrání před větrem.')],
)

# ------------------------------------------------------------------ micove-sporty
NEW['micove-sporty'] = dict(short=True,
    title='Míčové a raketové sporty – výbava | Sporteka',
    desc='Výbava pro míčové a raketové sporty: hokej, basketbal, fotbal, florbal, padel, tenis, stolní tenis a další. Porovnejte ceny z českých obchodů.',
    intro='<p><strong>Míčové a raketové sporty</strong> patří mezi nejoblíbenější v Česku. Od hokejových branek po tenisové rakety a padelové pálky, každý sport má specifickou výbavu. Při výběru se řiďte úrovní hráče, podkladem, na kterém hrajete, a tím, jak často trénujete.</p>'
          '<p>Na Sportece najdete vybavení k těmto sportům z českých obchodů na jednom místě: <a href="/hokej/">hokej</a>, <a href="/basketbal/">basketbal</a>, <a href="/fotbal/">fotbal</a>, <a href="/florbal/">florbal</a>, <a href="/padel/">padel</a>, <a href="/tenis/">tenis</a>, <a href="/stolni-tenis/">stolní tenis</a>, <a href="/badminton/">badminton</a>, <a href="/volejbal/">volejbal</a>, <a href="/squash/">squash</a> a <a href="/hazena/">házenou</a>. Porovnáte ceny a sledujete slevy.</p>',
    guide='<h2>Jak vybrat výbavu pro míčový sport</h2>'
          '<p>Výbava se liší podle sportu, ale společné jsou tři věci: správná obuv pro podklad, ochrana a sportovní oblečení. Raketové sporty přidávají hmotnost, vyvážení a velikost hlavy rakety.</p>'
          '<h3>Rychlý přehled podle sportu</h3>'
          + T(['Sport', 'Základní výbava'], [['Hokej a florbal', 'hokejka nebo florbalka, ochranné vybavení, brusle, resp. sálová obuv'], ['Basketbal a volejbal', 'míč, halová obuv s dobrým tlumením, chrániče kolen'], ['Fotbal', 'kopačky podle povrchu, míč, chrániče holení'], ['Tenis, squash, badminton', 'raketa, míče nebo košíky, sálová nebo tenisová obuv'], ['Padel', 'padelová pálka, specifické míče, obuv s vhodnou podrážkou'], ['Stolní tenis', 'pálka, míčky, pryžové potahy a vhodná obuv']]) +
          '<h3>Obuv podle povrchu</h3>'
          '<p>Hala, antuka, tvrdý povrch a umělá tráva vyžadují každý jinou podrážku. Špatná obuv zhoršuje přilnavost a zvyšuje riziko zranění kotníků. Ověřte si označení podrážky u každého modelu.</p>'
          '<h3>Rakety a pálky</h3>'
          '<p>U raket sledujte hmotnost, vyvážení a velikost hlavy. Lehčí rakety zrychlují švih, těžší dávají větší sílu. Začátečníkům se hodí větší hlava a odpouštějící zóna, pokročilí volí podle stylu hry.</p>'
          '<h3>Ochrana</h3>'
          '<p>Při kontaktních sportech se vyplatí chrániče, ochranné pomůcky a doplňky podle pravidel. Pro děti dbejte na správnou velikost, protože příliš velké chrániče nesedí a nechrání.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("bauer", "Bauer"), ("ccm", "CCM"), ("nike", "Nike"), ("adidas", "Adidas"), ("puma", "Puma"), ("wilson", "Wilson"), ("head", "Head"), ("mizuno", "Mizuno"), ("sherwood", "Sherwood"), ("merco", "Merco"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Výběr obuvi bez ohledu na povrch.</li><li>Raketa příliš těžká pro začátečníka.</li><li>Ochranné vybavení kupované s rezervou na vyrůstání.</li></ul>',
    faq=[('Který míčový sport je pro začátečníka nejsnazší?', 'Záleží na zálibě. Stolní tenis, badminton a basketbal potřebují málo vybavení a hrají se rekreačně.'),
         ('Jaká obuv se hodí na halu?', 'Sálová obuv s gumovou podrážkou, která dobře přilne a nezanechává stopy na podlaze.'),
         ('Jak vybrat tenisovou raketu?', 'Podle úrovně: začátečník větší hlavu a nižší hmotnost, pokročilý vyvážení podle stylu hry.'),
         ('Co je padel?', 'Raketový sport pro čtyři hráče, hraje se na kurtu se skleněnými stěnami a plnou pálkou bez strun.'),
         ('Potřebují děti ochranné pomůcky?', 'U kontaktních sportů ano, ve správné velikosti, ne na vyrůstání.'),
         ('Jak často měnit sálovou obuv?', 'Když podrážka ztratí přilnavost nebo se opotřebí vrchní materiál, zvláště při pravidelném tréninku.')],
)

# ------------------------------------------------------------------ sportovni-bundy-jaro-podzim
NEW['sportovni-bundy-jaro-podzim'] = dict(short=True,
    title='Jarní a podzimní bundy – softshell, větrovky | Sporteka',
    desc='Jarní a podzimní bundy pánské, dámské a dětské: softshell, větrovky, lehké zateplené a nepromokavé. Porovnejte ceny v českých obchodech a vyberte bundu.',
    intro='<p><strong>Jarní a podzimní bunda</strong> musí zvládnout proměnlivé počasí, tedy vítr, slabý déšť a ranní chlad, a přitom nepřehřát při chůzi. Zatímco zimní bunda hřeje, přechodová bunda hlavně chrání a skládá se s dalšími vrstvami. Na výběru se podílí materiál, zateplení a střih.</p>'
          '<p>Na Sportece najdete <strong>jarní bundy dámské, pánské i dětské</strong> z českých obchodů na jednom místě, filtrovat je můžete podle velikosti, barvy a značky. Teplejší modely hledejte v <a href="/zimni-bundy/">zimních a péřových bundách</a>, nepromokavé v <a href="/nepromokave-bundy/">nepromokavých bundách</a> a lehké vrstvy v <a href="/fleecove-mikiny/">fleecových mikinách</a>.</p>',
    guide='<h2>Jak vybrat jarní a podzimní bundu</h2>'
          '<p>Přechodová bunda je kompromis mezi větrem, deštěm a prodyšností. Rozhodněte, jestli ji budete nosit hlavně do města, na túru nebo na kolo.</p>'
          '<h3>Typy bund</h3>'
          '<ul><li><strong>Softshell:</strong> pružný, větruodolný a částečně vodoodpudivý, příjemný při pohybu.</li>'
          '<li><strong>Větrovka:</strong> velmi lehká, chrání před větrem a lehkým deštěm, skládá se do kapsy.</li>'
          '<li><strong>Lehce zateplená:</strong> s lehkou izolací, hodí se na chladné ráno a večer.</li>'
          '<li><strong>Hardshell:</strong> plně nepromokavá, s membránou, pro déšť a horské túry.</li></ul>'
          '<h3>Vodní sloupec a prodyšnost</h3>'
          '<p>Vodní sloupec udává odolnost vůči vodě v milimetrech. Pro lehký déšť stačí nižší hodnota, pro vytrvalý déšť potřebujete vyšší a zalepené švy. Prodyšnost určuje, jak snadno odchází pára z těla.</p>'
          '<h3>Střih a velikost</h3>'
          '<p>Bunda má sedět tak, aby pod ní šla obléct vrstva a omezený pohyb nebránil. Zkontrolujte délku rukávů a zadní část pro sezení na kole nebo při sedu.</p>'
          '<h3>Praktické detaily</h3>'
          '<ul><li>Kapuce, která se dá stáhnout nebo odepnout.</li><li>Kapsy na zip, aby se věci neztratily.</li><li>Reflexní prvky pro večerní provoz.</li><li>Úpravy na manžetách a v pase pro lepší těsnění.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("regatta", "Regatta"), ("trespass", "Trespass"), ("nike", "Nike"), ("adidas", "Adidas"), ("columbia", "Columbia"), ("helly-hansen", "Helly Hansen"), ("dare2b", "Dare2b"), ("dynafit", "Dynafit"), ("haglofs", "Haglöfs"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Bundy s membránou perte šetrně a podle štítku, aby se neodmyla impregnace. Obnovit ji lze sprejem nebo přípravkem určeným do pračky.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Zimní bunda do přechodného počasí, ve které se pocení.</li><li>Bunda bez membrány na vytrvalý déšť.</li><li>Příliš těsný střih, který neumožní oblékat vrstvy.</li></ul>',
    faq=[('Jaká bunda na jaro?', 'Lehká větrovka nebo softshell, které chrání před větrem a mírným deštěm a nepřehřívají.'),
         ('Jaký je rozdíl mezi softshellem a hardshellem?', 'Softshell je pružný a prodyšný s omezenou odolností vůči vodě, hardshell má membránu a odolá dlouhému dešti.'),
         ('Co znamená vodní sloupec?', 'Kolik milimetrů vodního sloupce látka vydrží, než propustí vodu. Vyšší číslo znamená vyšší odolnost.'),
         ('Jak pečovat o bundu s membránou?', 'Prát šetrně se speciálním přípravkem a čas od času obnovit impregnaci.'),
         ('Jakou bundu pro děti?', 'Lehkou a odolnou, s kapucí a reflexními prvky a s dostatečnou rezervou na pohyb. Dětem se hodí barevné modely.'),
         ('Kdy přejít ze zimní bundy na přechodovou?', 'Když ranní teploty stoupají nad nulu a přes den bývá mírně, obvykle na jaře a začátkem podzimu.')],
)

# ------------------------------------------------------------------ vodni-sporty
NEW['vodni-sporty'] = dict(short=True,
    title='Vodní sporty a plavání – výbava a pomůcky | Sporteka',
    desc='Vybavení pro vodní sporty a plavání: paddleboardy, kajaky, plavecké brýle, neopreny, šnorchlování a bazény. Porovnejte ceny z českých obchodů.',
    intro='<p><strong>Vodní sporty</strong> přinášejí radost po celé léto a vybavení se liší podle toho, jestli plavete, pádlujete nebo se potápíte. Pro plavání stačí brýle, čepice a plavky, pro paddleboarding nebo kajak potřebujete plavidlo, pádlo a vestu, pro šnorchlování masku a ploutve.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů na jednom místě: <a href="/paddleboardy/">paddleboardy a kajaky</a>, <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-cepice/">plavecké čepice</a>, <a href="/plavecke-pomucky/">plavecké pomůcky</a>, <a href="/neopreny/">neopreny</a>, <a href="/snorchlovani/">šnorchlování a potápění</a>, <a href="/bazeny/">bazény a nafukovadla</a>, <a href="/plazove-doplnky/">plážové doplňky</a> a <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>.</p>',
    guide='<h2>Jak vybrat vybavení pro vodní sporty</h2>'
          '<p>Nejdřív určete, co chcete na vodě dělat a kde. Řeka, rybník, moře a bazén vyžadují odlišné vybavení a bezpečnostní prvky. Vždy myslete na záchrannou vestu a ochranu před sluncem.</p>'
          '<h3>Podle aktivity</h3>'
          + T(['Aktivita', 'Základ'], [['Plavání v bazénu', 'plavky, brýle, čepice, pomůcky pro trénink'], ['Paddleboarding', 'nafukovací paddleboard, pádlo, vesta, pumpa, leash'], ['Kajak a čluny', 'kajak nebo člun, pádlo, vesta, vodotěsný vak'], ['Šnorchlování', 'maska, šnorchl, ploutve, případně neopren'], ['Moře a pláž', 'UV trička, osuška, ochrana před sluncem'], ['Zahrada a rodina', 'bazén, nafukovadla, hračky a míče do vody']]) +
          '<h3>Bezpečnost</h3>'
          '<p>Plovací vesta patří na vodu pro děti i dospělé, hlavně u paddleboardů a čluny. Ověřte velikost podle váhy a pohyb pro paddling. U moře dávejte pozor na proudy a vlnobití.</p>'
          '<h3>Ochrana před sluncem</h3>'
          '<p>Lycra a UV trička chrání kůži i při dlouhém pobytu na vodě. Přidejte klobouk, brýle a voděodolný krém. Slunce se odráží od hladiny a pálí víc, než čekáte.</p>'
          '<h3>Neopren a teplota vody</h3>'
          '<p>Neopren zlepšuje komfort ve studené vodě, plave se v něm déle. Tloušťka se volí podle teploty, od tenkých letních po silné zimní modely. Musí těsně sedět, ale nesmí omezovat pohyb.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("speedo", "Speedo"), ("arena", "Arena"), ("aqualung", "Aqualung"), ("mares", "Mares"), ("intex", "Intex"), ("bestway", "Bestway"), ("o-neill", "O\'Neill"), ("craft", "Craft"), ("aqua-speed", "Aqua Speed"))}.</p>'
          '<h3>Péče o vybavení</h3>'
          '<p>Po slané vodě vše opláchněte sladkou vodou a nechte uschnout ve stínu. Nafukovací plavidla skladujte vyschlá a lehce vypuštěná, aby se materiál nelámal.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Plavání nebo paddleboarding bez vesty.</li><li>Nafukovací člun s příliš nízkou nosností pro rodinu.</li><li>Zapomenutá ochrana před sluncem při dlouhém pobytu.</li></ul>',
    faq=[('Co potřebuji na paddleboarding?', 'Paddleboard, pádlo, plovací vestu, pumpu a leash. Hodí se také vodotěsný vak na telefon.'),
         ('Jak vybrat plavecké brýle?', 'Podle tvaru obličeje a typu plavání. Při tréninku vyberte utěsněný model, na rekreační plavání pohodlné s antifogem.'),
         ('Je vesta nutná?', 'Při paddleboardingu, kajaku a plavbě s dětmi ji doporučujeme vždy.'),
         ('Co je neopren?', 'Pěnový materiál, který drží tělesné teplo a zlepšuje komfort ve studené vodě.'),
         ('Jak skladovat nafukovací plavidla?', 'Suché, lehce vypuštěné a mimo sluneční záření.'),
         ('Jak chránit kůži na vodě?', 'UV tričkem, kloboukem a voděodolným krémem. Slunce se odráží od hladiny a pálí intenzivněji.')],
)

# ------------------------------------------------------------------ merino
NEW['merino'] = dict(short=True,
    title='Merino oblečení – trička, prádlo, ponožky | Sporteka',
    desc='Merino oblečení pánské, dámské a dětské: trička, spodní prádlo, ponožky, mikiny a doplňky. Porovnejte ceny z českých obchodů a vyberte gramáž.',
    intro='<p><strong>Merino</strong> je vlna z ovcí plemene merino, jemná, hřejivá a nepáchnoucí. Proto ji sportovci a cestovatelé milují na trička, spodní prádlo a ponožky. Merino reguluje teplotu, v chladu hřeje a v teple chladí, a přitom se dá nosit několik dní bez nepříjemného zápachu.</p>'
          '<p>Na Sportece najdete merino od českých obchodů: <a href="/merino-tricka/">merino trička a tílka</a>, <a href="/merino-pradlo/">spodní prádlo a legíny</a>, <a href="/merino-ponozky/">ponožky</a>, <a href="/merino-mikiny/">mikiny a svetry</a> a <a href="/merino-doplnky/">čepice, nákrčníky a rukavice</a>. Filtrovat můžete podle velikosti, barvy a značky.</p>',
    guide='<h2>Jak vybrat merino oblečení</h2>'
          '<p>Rozhodující je gramáž materiálu a použití. Lehké merino se hodí na léto a běh, střední na celoroční nošení a těžké na zimu a hory. Kombinace s funkčními vlákny přidává odolnost.</p>'
          '<h3>Gramáž a použití</h3>'
          + T(['Gramáž', 'Použití'], [['do 150 g/m²', 'léto, běh, cestování v teple'], ['150–220 g/m²', 'celoroční triko, turistika, jaro a podzim'], ['nad 220 g/m²', 'zimní vrstva, hory, spodní prádlo do mrazu']]) +
          '<h3>Výhody merina</h3>'
          '<ul><li><strong>Termoregulace:</strong> hřeje v zimě a při teple neprohřívá tolik jako syntetika.</li>'
          '<li><strong>Zápach:</strong> vlna zadržuje pach méně, takže triko vydrží nosit déle.</li>'
          '<li><strong>Vlhkost:</strong> pohlcuje pot a hřeje i vlhké.</li>'
          '<li><strong>Měkkost:</strong> jemné vlákno nedrásá.</li></ul>'
          '<h3>Nevýhody</h3>'
          '<p>Merino je dražší než syntetika, pomaleji schne a jemné modely se při hrubém zacházení snáz poškodí. Směsi s polyesterem nebo nylonem jsou odolnější a rychleji schnou.</p>'
          '<h3>Vrstvení</h3>'
          '<p>Merino se nejčastěji nosí jako první vrstva přímo na těle. Doplňte je fleecem nebo mikinou a svrchní bundou. Pro sporty s vysokou intenzitou je často lepší lehčí gramáž.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("icebreaker", "Icebreaker"), ("smartwool", "Smartwool"), ("lasting", "Lasting"), ("devold", "Devold"), ("sensor", "Sensor"), ("kama", "Kama"), ("mons-royale", "Mons Royale"), ("helly-hansen", "Helly Hansen"), ("husky", "Husky"))}.</p>'
          '<h3>Péče o merino</h3>'
          '<p>Perte šetrně na nízkou teplotu, bez aviváže a sušte vleže. Sušička merino zhrbí. Větrání mezi nošením prodlužuje čas do dalšího praní.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těžká gramáž na intenzivní sport v teple.</li><li>Praní na vysokou teplotu a sušení v sušičce.</li><li>Očekávání, že merino bude schnout stejně rychle jako syntetika.</li></ul>',
    faq=[('Jaké je merino oblečení?', 'Jemná vlna z ovcí merino. Hřeje, odvádí pot a méně zapáchá než syntetika.'),
         ('Jakou gramáž merino trika vybrat?', 'Na léto a běh lehkou do 150 g/m², na celý rok střední 150–220 g/m², na zimu a hory těžší.'),
         ('Je merino kousavé?', 'Kvalitní merino má velmi jemná vlákna a nedrásá. Hrubší vlna může být nepříjemná.'),
         ('Jak prát merino?', 'Šetrně na nízkou teplotu, bez aviváže a sušit volně vleže.'),
         ('Kdy merino zvolit místo syntetiky?', 'Když potřebujete oblečení nosit několik dní, cestujete nebo je vám na těle chladno a vlhko.'),
         ('Hodí se merino pro děti?', 'Ano, jemné merino je příjemné na citlivou pleť a dobře hřeje, pro děti existují trička, spodní prádlo i ponožky.')],
)

# ------------------------------------------------------------------ batohy
NEW['batohy'] = dict(short=True,
    title='Batohy – školní, městské, turistické | Sporteka',
    desc='Batohy pánské, dámské a dětské: školní, městské, na notebook, do letadla i turistické. Porovnejte ceny z českých obchodů a vyberte objem a značku.',
    intro='<p><strong>Batoh</strong> je jeden z nejčastěji hledaných doplňků a každý typ má jiné nároky. Do školy potřebujete pevná záda a přihrádky, do města a do práce čistý design s kapsou na notebook, na turistiku nosný systém, který přenese váhu na boky. Na cestu letadlem pak záleží na rozměrech.</p>'
          '<p>Na Sportece najdete <strong>batohy pánské, dámské a dětské</strong> z českých obchodů na jednom místě, porovnáte ceny a vyberete podle objemu. Hlavní kategorie jsou <a href="/turisticke-batohy/">turistické batohy</a>, <a href="/mestske-batohy/">městské a sportovní batohy</a> a <a href="/skolni-batohy/">školní a studentské batohy</a>.</p>',
    guide='<h2>Jak vybrat batoh</h2>'
          '<p>Nejdřív určete použití, potom objem. Batoh má sedět na zádech, mít pohodlné popruhy a odpovídat výšce zad. Důležitější než design je stavba zad a nastavení.</p>'
          '<h3>Objem podle použití</h3>'
          + T(['Použití', 'Orientační objem'], [['Škola a každodenní nošení', '15–25 l'], ['Město, notebook, kancelář', '18–30 l'], ['Jednodenní túra', '20–35 l'], ['Víkendový výlet', '35–50 l'], ['Týdenní trek', '50–70 l'], ['Příruční zavazadlo do letadla', 'podle rozměrů dopravce, často kolem 40 × 30 × 20 cm']]) +
          '<h3>Nosný systém</h3>'
          '<p>Turistické batohy mají nastavitelná záda, bederní pás a hrudní popruh, které převedou váhu na boky. Městské batohy mají jednodušší popruhy. Nastavte délku zad podle trupu, ne podle výšky.</p>'
          '<h3>Školní batohy</h3>'
          '<p>Pro děti vybírejte lehký batoh s pevnými zády, širokými popruhy a reflexními prvky. Neměl by vážit prázdný víc než nezbytné, protože dítě nese i učebnice. Pomáhá hrudní popruh, který drží batoh u těla.</p>'
          '<h3>Další funkce</h3>'
          '<ul><li>Kapsa na notebook s polstrováním.</li><li>Přihrádka na láhev na boku.</li><li>Pláštěnka nebo voděodolné materiály.</li><li>Zámky a skryté kapsy pro cestování.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("deuter", "Deuter"), ("osprey", "Osprey"), ("fjallraven", "Fjällräven"), ("the-north-face", "The North Face"), ("baagl", "Baagl"), ("nike", "Nike"), ("adidas", "Adidas"), ("vans", "Vans"), ("puma", "Puma"), ("regatta", "Regatta"), ("jansport", "Jansport"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Batoh vysypte, vyklepejte a vyperte podle návodu nebo ručně vlažnou vodou. Nesuší se na slunci ani na radiátoru, poškodil by se materiál.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velký batoh, který se naplní zbytečnou váhou.</li><li>Špatně nastavený bederní pás na trek.</li><li>Dětský batoh se slabými zády.</li></ul>',
    faq=[('Jaký objem batohu vybrat?', 'Do školy 15–25 l, na jednodenní túru 20–35 l, na víkend 35–50 l a na týdenní trek 50–70 l.'),
         ('Jak poznám, že batoh sedí?', 'Váha spočívá na bocích, ramenní popruhy neškrtí a záda nejsou příliš dlouhá ani krátká. Zkuste ho s nákladem.'),
         ('Jaký batoh do letadla?', 'Podle rozměrů příručního zavazadla dopravce. Rozměry se liší, vždy je ověřte před cestou.'),
         ('Jak vybrat školní batoh?', 'Lehký s pevnými zády, širokými popruhy a reflexními prvky, ve velikosti podle věku.'),
         ('Jaký batoh na notebook?', 'S polstrovanou kapsou odpovídající úhlopříčce notebooku a pevnými zády.'),
         ('Jak prát batoh?', 'Ručně ve vlažné vodě s jemným čisticím prostředkem a sušit na vzduchu, nikdy ne v sušičce.'),
         ('Co je hrudní popruh?', 'Popruh přes hrudník, který stahuje ramenní popruhy k sobě a zlepšuje stabilitu batohu.')],
)

# ------------------------------------------------------------------ sandaly
NEW['sandaly'] = dict(short=True,
    title='Sportovní sandály – turistické, trekové, dámské | Sporteka',
    desc='Sportovní a turistické sandály dámské, pánské a dětské: trekové, vodní i barefoot. Porovnejte ceny z českých obchodů a vyberte velikost a podrážku.',
    intro='<p><strong>Sportovní sandály</strong> nabízejí vzdušnou obuv na léto, která zvládne chůzi, vodu i krátké túry. Na rozdíl od módních sandálů mají pevnější podrážku, pásky držící patu a materiály, které nepromokají nebo rychle schnou. Právě podle toho se liší určení: do města, na cestování, do vody nebo do hor.</p>'
          '<p>Na Sportece najdete <strong>sandály dámské, pánské i dětské</strong> z českých obchodů, porovnáte ceny a vyberete velikost. K sandálům se hodí <a href="/sportovni-ponozky/">sportovní ponožky</a> nebo <a href="/trekova-obuv/">trekové boty</a> na chladnější dny.</p>',
    guide='<h2>Jak vybrat sportovní sandály</h2>'
          '<p>Sandály vybírejte podle toho, kam v nich půjdete. Pro městské procházky stačí pohodlné, pro túry potřebujete podrážku s protiskluzem a pevné uchycení paty. Do vody se hodí materiál, který neztratí tvar.</p>'
          '<h3>Typy sandálů</h3>'
          '<ul><li><strong>Trekové sandály:</strong> pevná podrážka s vzorkem, nastavitelné pásky, chrání prsty.</li>'
          '<li><strong>Vodní sandály:</strong> rychle schnoucí, s protiskluzovou podrážkou do vody a na kameny.</li>'
          '<li><strong>Sportovní městské:</strong> lehké a pohodlné, s pěnovou stélkou.</li>'
          '<li><strong>Barefoot:</strong> tenká flexibilní podrážka bez drop, blíž chůzi naboso.</li>'
          '<li><strong>Dětské:</strong> s uzavřenou špičkou a suchým zipem pro rychlé nasazení.</li></ul>'
          '<h3>Velikost a uchycení</h3>'
          '<p>Chodidlo má při chůzi tendenci otékat, proto sandály zkoušejte odpoledne. Prsty nesmí přesahovat, pata musí zůstat pevně. Pásky se nastavují podle šířky chodidla.</p>'
          '<h3>Podrážka a stélka</h3>'
          '<p>Na túry vyberte podrážku s tlumením a protiskluzem, do města postačí lehká. Anatomická stélka podpoří klenbu, u dětí je důležitá měkkost a flexibilita.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou sandály značek {B(("keen", "Keen"), ("teva", "Teva"), ("crocs", "Crocs"), ("skechers", "Skechers"), ("geox", "Geox"), ("columbia", "Columbia"), ("adidas", "Adidas"), ("rieker", "Rieker"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Po koupání sandály opláchněte a nechte uschnout ve stínu, ne na slunci. Odstraňte písek, který může při chůzi dřít. Stélku čas od času vyperte.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Sandály bez uchycení paty na túru.</li><li>Zkoušení ráno, kdy je chodidlo menší.</li><li>Pěnová podrážka na kluzký kámen bez protiskluzu.</li></ul>',
    faq=[('Jaké sandály vybrat na turistiku?', 'Trekové s pevnou podrážkou, protiskluzem a nastavitelnými pásky, které drží patu.'),
         ('Jaký je rozdíl mezi sportovními a běžnými sandály?', 'Sportovní mají pevnější podrážku, lepší uchycení a materiály, které snesou vodu a delší chůzi.'),
         ('Hodí se sandály i do vody?', 'Vodní a trekové modely ano, mají rychle schnoucí materiály a protiskluz. Městské se hodí jen na pláž.'),
         ('Co jsou barefoot sandály?', 'Sandály s tenkou flexibilní podrážkou bez zvýšené paty, které napodobují chůzi naboso.'),
         ('Jak vybrat sandály pro dítě?', 'S uzavřenou špičkou, suchým zipem a měkkou stélkou ve správné velikosti, ne příliš velké.'),
         ('Kdy sandály zkoušet?', 'Odpoledne, kdy je chodidlo nejvíc otékající, a s ponožkou, pokud ji budete nosit.')],
)

# ------------------------------------------------------------------ kosile
NEW['kosile'] = dict(short=True,
    title='Turistické a outdoorové košile | Sporteka',
    desc='Turistické a outdoorové košile pánské i dámské: rychleschnoucí, s UV ochranou, lehké i taktické. Porovnejte ceny z českých obchodů a vyberte velikost.',
    intro='<p><strong>Turistická košile</strong> je lehká vrstva, která chrání před sluncem, hmyzem a větrem a při tom odvádí pot. Na rozdíl od běžné košile bývá z rychle schnoucího materiálu s prodyšnými záložkami, rukávy se dají vyhrnout a zajistit patkou. Hodí se na túry, cestování, kolo i taktické aktivity.</p>'
          '<p>Na Sportece porovnáte <strong>pánské i dámské outdoorové košile</strong> z českých obchodů a filtrujete je podle velikosti, barvy a značky. Doplnit je můžete <a href="/funkcni-tricka/">funkčním tričkem</a>, <a href="/outdoorove-kalhoty/">outdoorovými kalhotami</a> a <a href="/sportovni-bundy-jaro-podzim/">lehkou bundou</a>.</p>',
    guide='<h2>Jak vybrat outdoorovou košili</h2>'
          '<p>Vybírejte podle materiálu, střihu a použití. Pro horké dny je důležitá prodyšnost a UV ochrana, pro chladnější část roku se hodí těžší látky a košile jako vrstva pod bundu.</p>'
          '<h3>Materiály</h3>'
          '<ul><li><strong>Polyester a nylon:</strong> rychle schnou, lehké, často s UV filtrem.</li>'
          '<li><strong>Bavlna:</strong> příjemná v teple, ale po zmoknutí pomalu schne.</li>'
          '<li><strong>Merino:</strong> hřeje i při vlhku a nezapáchá, vhodné na dlouhé cesty.</li>'
          '<li><strong>Směsi:</strong> kombinují odolnost a příjemný omak.</li></ul>'
          '<h3>Funkce, které se hodí</h3>'
          '<ul><li>Patky na rukávech pro zajištění vyhrnutého rukávu.</li><li>Větrací záložky na zádech.</li><li>Kapsy na zip, aby se věci neztratily.</li><li>Ochrana před sluncem (UPF) a ochrana proti hmyzu.</li></ul>'
          '<h3>Střih a velikost</h3>'
          '<p>Outdoorové košile bývají střižené tak, aby nebránily pohybu. Zkontrolujte délku rukávů při zvednutých rukou a délku v zadní části, aby neodhalovala záda při předklonu.</p>'
          '<h3>Taktické a pracovní</h3>'
          '<p>V nabídce jsou také taktické košile s kapsami a zesílením loktů, určené pro airsoft, lov a práci v terénu. Rozhodují odolnost, kamufláž a počet kapes.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("fjallraven", "Fjällräven"), ("nike", "Nike"), ("adidas", "Adidas"), ("celio", "Celio"), ("gap", "Gap"), ("tommy-hilfiger", "Tommy Hilfiger"), ("calvin-klein", "Calvin Klein"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Perte podle štítku a nesušte na slunci. Impregnované a UV materiály nepoužívejte s aviváží, snižuje funkci vlákna.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Bavlněná košile na intenzivní túru v dešti.</li><li>Příliš těsný střih, který se při zvednutí rukou vytahuje.</li><li>Zapomenutá ochrana krku a zátylku před sluncem.</li></ul>',
    faq=[('Jaká košile na turistiku?', 'Lehká rychle schnoucí z polyesteru nebo směsi, s UV ochranou a možností vyhrnutí rukávů.'),
         ('Hodí se bavlněná košile na túru?', 'Na krátké suché výlety ano, na delší nebo vlhké dny je lepší syntetika nebo merino.'),
         ('Co znamená UPF?', 'Ochranný faktor před UV zářením u látek. Vyšší číslo znamená lepší ochranu pokožky.'),
         ('Jak se starat o outdoorovou košili?', 'Prát šetrně podle štítku, bez aviváže a sušit ve stínu.'),
         ('Jaké jsou taktické košile?', 'Odolné košile s kapsami a zesílením loktů pro lov, airsoft a práci v terénu.'),
         ('Jak vybrat velikost?', 'Podle tabulky výrobce a obvodu hrudníku, s rezervou na vrstvu pod košili.')],
)

# ------------------------------------------------------------------ fleecove-mikiny
NEW['fleecove-mikiny'] = dict(short=True,
    title='Fleecové mikiny – pánské, dámské, dětské | Sporteka',
    desc='Fleecové mikiny pánské, dámské a dětské: na zip, s kapucí, lehké i zimní. Porovnejte ceny z českých obchodů a vyberte velikost a gramáž fleece.',
    intro='<p><strong>Fleecová mikina</strong> je lehká a hřejivá vrstva, kterou ocení každý, kdo potřebuje teplo bez objemu. Fleece dobře odvádí pot, rychle schne a váží málo, proto se používá jako střední vrstva pod bundu na túru, na lyže i na každodenní nošení.</p>'
          '<p>Na Sportece najdete <strong>fleecové mikiny pánské, dámské a dětské</strong> z českých obchodů, porovnáte ceny a vyberete podle velikosti, barvy a značky. Doplnit je můžete o <a href="/merino-mikiny/">merino mikiny</a> nebo <a href="/zimni-bundy/">zimní bundy</a> pro silný mráz.</p>',
    guide='<h2>Jak vybrat fleecovou mikinu</h2>'
          '<p>Rozhoduje použití a gramáž. Tenký fleece se hodí na pohyb a jako střední vrstva, silnější na chladné dny nebo samostatné nošení. Zip zlepšuje větrání, kapuce přidává ochranu.</p>'
          '<h3>Gramáž fleece</h3>'
          + T(['Gramáž', 'Použití'], [['100–150 g/m²', 'lehká vrstva, pohyb, jaro a podzim'], ['200 g/m²', 'všestranná mikina na túry a běžné nošení'], ['300 g/m² a více', 'zima, chladné dny a odpočinek']]) +
          '<h3>Typy fleecových mikin</h3>'
          '<ul><li><strong>Na celý zip:</strong> lépe se větrá a navléká přes jiné vrstvy.</li>'
          '<li><strong>Na půl zip:</strong> lehčí, často pro sport a pod bundu.</li>'
          '<li><strong>S kapucí:</strong> přidává ochranu hlavy a krku.</li>'
          '<li><strong>Dětské:</strong> měkké a odolné, často s kapsami a reflexními prvky.</li></ul>'
          '<h3>Vrstvení</h3>'
          '<p>Fleecová mikina patří doprostřed. Pod ni vezměte funkční nebo merino triko, přes ni vítrovku nebo hardshell. Samotný fleece vítr propouští, proto potřebuje svrchní vrstvu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("nike", "Nike"), ("columbia", "Columbia"), ("regatta", "Regatta"), ("trespass", "Trespass"), ("under-armour", "Under Armour"), ("helly-hansen", "Helly Hansen"), ("dare2b", "Dare2b"), ("adidas", "Adidas"), ("viking", "Viking"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Perte na nízkou teplotu bez aviváže, která zalepí vlákna. Nesušte na topení ani v sušičce na vysoké teplotě, fleece by se zdeformoval.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Fleece bez svrchní vrstvy ve větru.</li><li>Příliš těsná mikina, která stlačí vrstvy pod sebou.</li><li>Praní s aviváží.</li></ul>',
    faq=[('Jaká fleecová mikina na túru?', 'Lehká až střední gramáž na zip, která se dobře větrá a vejde se pod bundu.'),
         ('Hřeje fleece i mokrý?', 'Fleece drží teplo i při vlhku a rychle schne, proto se hodí do proměnlivého počasí.'),
         ('Co znamená gramáž fleece?', 'Hmotnost materiálu v gramech na metr čtvereční. Vyšší číslo znamená teplejší a silnější látku.'),
         ('Jak prát fleece?', 'Šetrně na nízkou teplotu, bez aviváže, sušit volně.'),
         ('Potřebuji bundu přes fleece?', 'Ve větru ano, fleece sám vítr propouští a doporučuje se svrchní větruvzdorná vrstva.'),
         ('Jak vybrat dětskou fleecovou mikinu?', 'Měkkou a odolnou, na zip pro rychlé oblékání, s rezervou na růst jen o jednu velikost.')],
)

# ------------------------------------------------------------------ sportovni-ponozky
NEW['sportovni-ponozky'] = dict(short=True,
    title='Sportovní ponožky – běžecké, turistické, merino | Sporteka',
    desc='Sportovní ponožky pánské, dámské a dětské: běžecké, turistické, cyklistické a merino. Porovnejte ceny z českých obchodů a vyberte velikost a délku.',
    intro='<p><strong>Sportovní ponožky</strong> rozhodují o tom, jestli vás po deseti kilometrech nebo celodenní túře bolí nohy. Dobrá ponožka odvádí pot, nesesouvá se, nemá drsné švy a v nejvíc namáhaných místech je zesílená. Běh, turistika, kolo, fotbal i zimní sporty mají své typy.</p>'
          '<p>Na Sportece najdete <strong>sportovní ponožky</strong> z českých obchodů, porovnáte ceny a vyberete velikost a délku. Zvláštní kategorie tvoří <a href="/merino-ponozky/">merino ponožky</a> a <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, k ponožkám patří <a href="/silnicni-bezecke-boty/">běžecké boty</a>.</p>',
    guide='<h2>Jak vybrat sportovní ponožky</h2>'
          '<p>Vybírejte podle sportu, délky a materiálu. Běžecká ponožka je tenká a plochá, turistická tlustší s tlumením na patě a špičce, cyklistická vyšší a vzdušná.</p>'
          '<h3>Typy podle sportu</h3>'
          + T(['Sport', 'Vlastnosti ponožky'], [['Běh', 'tenká, bezešvá, s ventilací a zesílením paty'], ['Turistika', 'střední až silné tlumení, často merino nebo směs'], ['Cyklistika', 'vyšší, lehká, vzdušná'], ['Fotbal a halové sporty', 'podkolenky nebo kotníkové, odolné proti odření'], ['Zimní sporty', 'vyšší, hřejivé, bez tlačících švů']]) +
          '<h3>Materiály</h3>'
          '<ul><li><strong>Syntetika (polyamid, polyester):</strong> rychle schne a je odolná.</li>'
          '<li><strong>Bavlna:</strong> příjemná, ale nasákne a hůř odvádí pot.</li>'
          '<li><strong>Merino:</strong> hřeje a nezapáchá, vhodné na dlouhé túry.</li>'
          '<li><strong>Elastan:</strong> zajišťuje tvar a přilnutí k noze.</li></ul>'
          '<h3>Délka a střih</h3>'
          '<p>Kotníkové a nízké ponožky se hodí do nízké obuvi, vyšší chrání před otlaky trekové boty. Střih pro pravou a levou nohu a zesílené zóny zvyšují komfort při delší zátěži.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("adidas", "Adidas"), ("nike", "Nike"), ("smartwool", "Smartwool"), ("lasting", "Lasting"), ("under-armour", "Under Armour"), ("on", "On"), ("fila", "Fila"), ("dynafit", "Dynafit"), ("errea", "Errea"))}.</p>'
          '<h3>Péče</h3>'
          '<p>Perte naruby na nízkou teplotu, bez aviváže a nesušte na radiátoru. Opotřebené ponožky se zesílenou patou vyměňte, protože ztrácejí tlumení.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Bavlněné ponožky na delší túru nebo běh.</li><li>Příliš velká ponožka, která se krčí.</li><li>Praní s aviváží, která snižuje odvádění potu.</li></ul>',
    faq=[('Jaké ponožky na běhání?', 'Tenké, bezešvé a prodyšné ze syntetiky nebo směsi, s lehkým tlumením na patě.'),
         ('Jaké ponožky na turistiku?', 'Střední až silné s tlumením a ideálně z merina nebo směsi, aby nezapáchaly a drželi teplo.'),
         ('Je bavlna na sport špatná?', 'Bavlna nasákne potem a hůř schne, proto se na delší výkon nehodí.'),
         ('Jak velkou ponožku zvolit?', 'Podle velikosti nohy, ponožka musí těsně přiléhat a nekrčit se.'),
         ('Jak často měnit sportovní ponožky?', 'Když zeslábne tlumení, objeví se díry nebo se začnou drolit švy.'),
         ('Jak prát sportovní ponožky?', 'Naruby na nízké teplotě, bez aviváže a sušit vleže nebo na šňůře.')],
)

# ------------------------------------------------------------------ silnicni-bezecke-boty
NEW['silnicni-bezecke-boty'] = dict(short=True,
    title='Silniční běžecké boty – pánské a dámské | Sporteka',
    desc='Silniční běžecké boty pánské a dámské: tlumené, rychlé, stabilní i karbonové. Porovnejte ceny z českých obchodů a vyberte boty podle došlapu a vzdálenosti.',
    intro='<p><strong>Silniční běžecké boty</strong> jsou určené na asfalt, štěrkové a zpevněné cesty. Mají tlumenou podrážku, pružnou střední část a prodyšnou vrchní vrstvu. Správný pár záleží na vašem došlapu, váze, vzdálenosti a tempu, proto jsou na trhu boty od velmi tlumených po závodní.</p>'
          '<p>Na Sportece najdete <strong>pánské a dámské běžecké boty</strong> z českých obchodů a porovnáte ceny a slevy. Pro terén sáhněte po <a href="/trailove-boty/">trailových botách</a>, doplňte je <a href="/sportovni-ponozky/">sportovními ponožkami</a> a podívejte se na <a href="/bezecka-obuv/">všechny běžecké boty</a>.</p>',
    guide='<h2>Jak vybrat silniční běžecké boty</h2>'
          '<p>Nejdůležitější je pohodlí. Bota má při zkoušce sedět bez tlaku, pata nesmí vyskakovat a prsty mají mít prostor. Měřte vždy večer, kdy je noha největší, a přidejte půl až celé číslo oproti běžné obuvi.</p>'
          '<h3>Typ boty podle použití</h3>'
          + T(['Typ', 'Pro koho a na co'], [['Tlumené (cushioned)', 'delší vzdálenosti, těžší běžci, regenerační tempo'], ['Neutrální', 'běžci bez výrazné pronace, univerzální každodenní trénink'], ['Stabilní', 'běžci s pronací, kteří potřebují oporu klenby'], ['Rychlé a závodní', 'tempové tréninky a závody, lehká konstrukce'], ['S karbonovou deskou', 'závodní boty pro rychlejší odraz, vyšší cena']]) +
          '<h3>Drop a tlumení</h3>'
          '<p>Drop je výškový rozdíl mezi patou a špičkou. Vyšší chrání lýtka a Achillovku, nižší je blíž přirozenému došlapu. Tlumení určuje, jak měkká je jízda, ale příliš měkká bota ztrácí odraz.</p>'
          '<h3>Pronace a došlap</h3>'
          '<p>Většina běžců používá neutrální obuv. Pokud se vám kolena nebo kotníky dlouhodobě stáčejí dovnitř, může pomoci stabilní bota. Spolehlivý údaj dá analýza došlapu v obchodě.</p>'
          '<h3>Životnost</h3>'
          '<p>Běžecká bota vydrží zhruba několik set kilometrů, podle hmotnosti a povrchu. Když cítíte, že ztratila odpružení, nebo vás po běhu bolí chodidla, je čas na novou.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("asics", "Asics"), ("mizuno", "Mizuno"), ("nike", "Nike"), ("adidas", "Adidas"), ("on", "On"), ("new-balance", "New Balance"), ("saucony", "Saucony"), ("puma", "Puma"), ("under-armour", "Under Armour"), ("salomon", "Salomon"))}.</p>'
          '<h3>Péče o boty</h3>'
          '<p>Boty po běhu vyndejte z tašky, vyjměte vložky a nechte vyschnout při pokojové teplotě. Do pračky ani sušičky je nedávejte, rozpadly by se lepené části.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš malá velikost, která drtí prsty při delším běhu.</li><li>Nákup podle vzhledu místo podle pohodlí.</li><li>Běhání ve starých botách, které ztratily tlumení.</li></ul>',
    faq=[('Jaké běžecké boty vybrat?', 'Podle vzdálenosti, tempa a došlapu. Pro začátek volte tlumený neutrální model s dostatečným prostorem pro prsty.'),
         ('Jaká velikost běžeckých bot?', 'Zhruba o půl až celé číslo větší než běžná obuv, s prostorem asi palec před špičkou.'),
         ('Co je drop?', 'Výškový rozdíl mezi patou a špičkou boty. Vyšší drop odlehčuje lýtka, nižší je blíž přirozenému došlapu.'),
         ('Kdy potřebuji stabilní boty?', 'Když máte výraznou pronaci, tedy stáčení nohy dovnitř, a dlouhodobě vás bolí kolena nebo kotníky.'),
         ('Jak dlouho běžecká bota vydrží?', 'Obvykle několik set kilometrů. Záleží na váze běžce, povrchu a tempu.'),
         ('Kdy se vyplatí karbonová deska?', 'Při závodech a rychlých trénincích, kde chcete zlepšit odraz. Pro běžný trénink není nutná.'),
         ('Jaké boty na asfalt?', 'Silniční běžecké s tlumenou podrážkou a hladším vzorkem, ne trailové s hrubým vzorkem.')],
)
