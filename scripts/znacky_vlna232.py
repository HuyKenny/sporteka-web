"""sporteka.cz — brand page texts wave 232: horsefeathers, keen, osprey, dc-shoes, victorinox, hoka.
General facts only, no prices or counts; assortment taken from the local catalogue copy (17. 11. 2026).

Sources (checked 17. 11. 2026):
- Horsefeathers: methodmag.com (30 Years Of Horsefeathers, interview with the owners), seznamzpravy.cz (Horsefeathers slaví třicet let),
  cc.cz (Třicetiletý nesmysl z kanadských hor), Horsefeathers catalogues on issuu.com (owners Hanuš Salz & Pavel Kubíček).
- Keen: en.wikipedia.org/wiki/Keen_(shoe_company) (2003, Martin Keen + Rory Fuerst, Alameda → Portland 2006, Newport toe bumper).
- Osprey: osprey.com history/about pages (1974 Santa Cruz, Dolores 1990, Cortez 1994, All Mighty Guarantee),
  businesswire.com / sgbonline.com (Helen of Troy acquisition, 29. 11. 2021).
- DC Shoes: en.wikipedia.org/wiki/DC_Shoes (June 1994, Damon Way, Ken Block, Clayton Blehm, Droors Clothing, Quiksilver 2004,
  parent Authentic Brands Group); blue-tomato.com / skatedeluxe.com (WNT = winter version of Pure High-Top).
- Victorinox: victorinox.com history timeline (1884 Ibach, 1891 soldier's knife, 1897 officer's knife patent, 1909 Victoria,
  1921 Inox, 2005 Wenger).
- Hoka: en.wikipedia.org/wiki/Hoka_(brand) (2009, Nicolas Mermoud + Jean-Luc Diard ex-Salomon, Annecy, Māori name,
  Deckers, rebrand 2021); irunfar.com (Speedgoat named after Karl Meltzer).
Left out (not verifiable or conflicting): exact Deckers deal year for Hoka (2012 vs 2013), Keen Uneek launch year,
Osprey move-to-Dolores year (1987 vs 1990), Horsefeathers registered seat, DC "WC" abbreviation, airline knife rules in detail.
"""
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ horsefeathers
NEW['horsefeathers'] = dict(
    title='Horsefeathers: snowboardové bundy, čepice a termoprádlo',
    desc='Horsefeathers v katalogu: snowboardové bundy a kalhoty, zimní čepice, termoprádlo, brýle, ponožky i cyklodresy. Jak vybrat velikost a srovnat obchody.',
    intro='<p>Horsefeathers je česká značka, která vyrostla ze snowboardingu a skateboardingu. Kořeny má v Plzni a u nás ji zná skoro každý, kdo v posledních třiceti letech jezdil na prkně. '
          'V nabídce převažují zimní čepice, lyžařské a snowboardové bundy a kalhoty, termoprádlo, brýle a ponožky na sníh. Vedle zimní výbavy najdete i trička, mikiny, košile, legíny, městské batohy a v posledních sezónách také oblečení na kolo. '
          'Sporteka.cz na této stránce shromažďuje nabídky českých e-shopů se zbožím Horsefeathers, takže na jednom místě uvidíte, kdo má konkrétní model, barvu a velikost. Objednávku pak dokončíte v obchodě, který si vyberete. Ceny se mezi obchody liší hlavně podle sezóny a barevné varianty, proto se vyplatí porovnávat stejný model napříč nabídkami. '
          'Pod tímto úvodem je průvodce historií značky, jednotlivými skupinami oblečení, střihy a péčí o membránové bundy.</p>',
    guide='<h2>Jak vznikla značka Horsefeathers</h2>'
          '<p>Příběh začíná na konci osmdesátých let v kanadské Britské Kolumbii. Hanuš Salz tam s partou kamarádů patřil k prvním snowboardistům v okolí a slovo horsefeathers, které v angličtině znamená zhruba nesmysl, si vzali za svůj vnitřní vtip. Po návratu do Československa studoval Salz na střední škole v Plzni a potkal tam Pavla Kubíčka. Oba dali dohromady úspory a v roce 1993 nechali vyrobit první trička s logem.</p>'
          '<p>Z malého projektu se postupně stala firma a v polovině devadesátých let otevřeli zakladatelé v Plzni obchod se skateboardovým a snowboardovým vybavením. Na konci devadesátých let přišla první kolekce svrchního oblečení na snowboard, která se stala hlavním pilířem značky. Salz a Kubíček vedou firmu dodnes a podle českého tisku se oblečení Horsefeathers prodává zhruba ve dvaceti zemích. Značka sponzoruje vlastní tým jezdců, s nimiž vyvíjí i podpisové modely.</p>'
          '<h2>Co v katalogu najdete</h2>'
          '<p>Nejpočetnější skupinou jsou <a href="/cepice-a-celenky/">zimní čepice</a>, pletené kulichy s výrazným logem nebo jednoduchou nášivkou. Druhý pilíř tvoří <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a> a k nim <a href="/lyzarske-kalhoty/">kalhoty na sjezdovku</a>. Pod oblečení na hory patří <a href="/termopradlo/">termoprádlo</a>, ochranu očí zajistí <a href="/lyzarske-bryle/">lyžařské brýle</a> a v létě <a href="/sportovni-bryle/">sluneční brýle</a>. Doplňují je <a href="/nakrcniky-a-satky/">nákrčníky</a>, ponožky, <a href="/mikiny/">mikiny</a>, trička a košile. Menší, ale rostoucí část nabídky tvoří <a href="/cyklisticke-dresy/">cyklistické dresy</a> a <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy na kolo</a>.</p>'
          + '<div class="tw"><table class="ct"><thead><tr><th>Skupina</th><th>Příklady modelů v nabídce</th><th>Kdy se hodí</th></tr></thead><tbody>'
          '<tr><td>Snowboardové bundy</td><td>Larra, Pearl, Tala, Fiora, Neva</td><td>sjezdovka, freeride, zimní město</td></tr>'
          '<tr><td>Kalhoty na sníh</td><td>Rowen, Orca, Diane</td><td>jízda na prkně i na lyžích</td></tr>'
          '<tr><td>Termoprádlo</td><td>Riley (pánské), Mirra (dámské)</td><td>první vrstva pod bundu</td></tr>'
          '<tr><td>Čepice</td><td>Fuse, Gaine, Matteo, Paula</td><td>celá zima, město i hory</td></tr>'
          '<tr><td>Trička a mikiny</td><td>Vertical Logo, Canned, Sylas</td><td>volný čas, vrstvení</td></tr>'
          '<tr><td>Cyklo oblečení</td><td>Spike, Fury, Stoker</td><td>trail, enduro, výlety na kole</td></tr>'
          '</tbody></table></div>'
          '<h2>Snowboardové bundy a kalhoty</h2>'
          '<p>Bundy Horsefeathers jsou šité tak, aby se v nich dalo volně hýbat na prkně. Bývají delší než běžná lyžařská bunda, aby kryly bedra i při sezení na sněhu, a mají kapuci, do které se vejde helma. Typické prvky jsou sněhový pás uvnitř, kapsa na skipas na rukávu a větrací zipy v podpaží. Některé modely jsou zateplené syntetickou výplní, jiné jsou jen membránovou skořepinou, pod kterou si oblečete vlastní vrstvy. Pokud jezdíte v mrazu a nechcete řešit vrstvení, sáhněte po zateplené verzi. Na jarní lyžování a túry je univerzálnější skořepina.</p>'
          '<p>Kalhoty na sníh mají obvykle volnější nohavice s návleky proti sněhu, zesílený lem dole, který chrání látku před hranami prkna, a možnost připnout šle nebo opasek. Některé modely jsou s laclem, které lépe drží sníh mimo záda při pádu v hlubokém prašanu. Při zkoušení si dřepněte a zvedněte koleno k hrudi: kalhoty nesmí táhnout v rozkroku ani se sesouvat.</p>'
          '<h2>Vodní sloupec a prodyšnost</h2>'
          '<p>U membránových bund a kalhot se uvádějí dvě čísla. Vodní sloupec v milimetrech říká, jaký tlak vody látka vydrží, než začne propouštět. Prodyšnost v gramech na metr čtvereční za den udává, kolik vodní páry projde ven. Vyšší hodnoty znamenají vhodnost pro mokrý sníh a náročnější pohyb, nižší stačí na suché mrazivé dny a občasné ježdění. Údaje porovnávejte jen mezi modely, které je uvádějí stejně, protože metodika měření se mezi výrobci liší. U oblečení na sníh je stejně důležité, zda má bunda podlepené švy.</p>'
          '<h2>Termoprádlo Riley a Mirra</h2>'
          '<p>Pánská řada Riley a dámská Mirra tvoří základ první vrstvy: trika s dlouhým rukávem, spodky a dámské legíny. Funkční prádlo má odvádět pot od těla, takže pod bundou nezůstanete mokří ani při výstupu nebo při čekání na lanovku. Mělo by sedět těsně, ale neškrtit. Pokud chcete hřejivější materiál, který tolik nepáchne, podívejte se i na <a href="/merino-pradlo/">merino prádlo</a>; syntetika zase rychleji schne a lépe snáší častější praní.</p>'
          '<h2>Čepice, nákrčníky a brýle</h2>'
          '<p>Kulichy jsou nejsilnější kategorií značky a nosí se i mimo hory. Liší se střihem (přiléhavý, delší s přehnutým lemem, s bambulí), materiálem a podšívkou. Pod helmu volte tenkou čepici bez bambule, do města klidně silnější pletení. Nákrčníky chrání krk a obličej při jízdě v mrazu a větru. V nabídce jsou také lyžařské brýle a sluneční brýle. U lyžařských sledujte tvar zorníku, kategorii filtru podle světelných podmínek a to, zda brýle pasují k vaší helmě, aby mezi nimi nezůstávala mezera.</p>'
          '<h2>Léto: trička, cyklodresy a batohy</h2>'
          '<p>Mimo zimu značka nabízí trička s potiskem, košile, mikiny, kšiltovky a dámské <a href="/leginy/">legíny</a>. Cyklistické oblečení je šité ve stylu trailového a endurového ježdění: volnější dresy s dlouhým nebo krátkým rukávem a kraťasy, pod které se oblékají vnitřní kalhoty s vložkou. Na každodenní nošení jsou určené <a href="/mestske-batohy/">městské batohy</a>, například Clout, Roller nebo Shift. Na sjezdovku ani na delší túru nejsou, do školy a do práce stačí.</p>'
          '<h2>Velikosti a střih</h2>'
          '<p>Oblečení Horsefeathers vychází ze snowboardové a skateboardové módy, a tak mnoho modelů padne volněji než klasické lyžařské oblečení. Bundy bývají delší a kalhoty širší. Pokud jste zvyklí na přiléhavý střih, zvažte o číslo menší velikost; pokud plánujete pod bundu fleece, nechte si rezervu. U dámských modelů je střih vypasovanější. Ponožky se prodávají v rozsazích velikostí, u některých se uvádí americké číslování, proto si převod ověřte v tabulce obchodu. Při porovnávání nabídek kontrolujte, zda jde o pánský, dámský nebo dětský model, protože názvy se mezi kategoriemi opakují.</p>'
          '<h2>Jak se obléct na svah</h2>'
          '<p>Oblečení na sníh funguje nejlépe ve vrstvách. Na tělo patří funkční nebo merino prádlo, které odvádí pot. Druhá vrstva hřeje, typicky <a href="/fleecove-mikiny/">fleecová mikina</a> nebo tenká zateplená vesta. Navrch přijde bunda a kalhoty, které chrání před větrem, sněhem a vlhkem. Bavlněné tričko pod bundu nedávejte, nasákne potem a na lanovce pak zebe. Do batohu se hodí náhradní rukavice a čepice. Pokud jezdíte v parku nebo ve volném terénu, kde častěji padáte, oceníte i <a href="/snowboardove-chranice/">chrániče</a> a kvalitní <a href="/lyzarske-ponozky/">ponožky na lyže</a>, které nemají v místě boty silné švy.</p>'
          '<h2>Péče o membránové oblečení</h2>'
          '<ul><li>Bundy a kalhoty perte podle štítku, se zapnutými zipy a v prostředku určeném pro funkční textil.</li>'
          '<li>Aviváž a běžný prášek nepoužívejte, ucpávají membránu a snižují odpudivost vody.</li>'
          '<li>Když voda přestane na povrchu perlit, obnovte úpravu <a href="/impregnace/">impregnací</a> ve spreji nebo do pračky.</li>'
          '<li>Termoprádlo perte na nízkou teplotu a nesušte na topení, syntetika může ztratit tvar.</li>'
          '<li>Pletené čepice perte ručně nebo na vlnový program a suště naplocho, aby se nevytahaly.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejný model se obvykle prodává v několika barvách a v různých sezónách. Názvy obchody zapisují odlišně: někde najdete jen jméno modelu, jinde celý popis s barvou. Hledejte proto podle názvu modelu a porovnejte fotky. U bund a kalhot se vyplatí zkontrolovat, z které kolekce kus pochází, protože se mohou lišit parametry membrány i zateplení. Zimní oblečení zlevňuje po skončení sezóny, letní kusy na konci léta. Starší barevné varianty bývají levnější i během sezóny.</p>'
          '<h2>Horsefeathers a podobné značky</h2>'
          '<p>Na sjezdovce se Horsefeathers potkává s dalšími značkami z prostředí snowboardingu a surfu, například '
          + B(('roxy', 'Roxy'), ('dc-shoes', 'DC Shoes')) +
          '. Kdo hledá spíše klasický lyžařský střih, najde ho u výrobců, jako jsou '
          + B(('scott', 'Scott'), ('mammut', 'Mammut')) +
          '. Pro jezdce na prkně se hodí i obecný přehled kategorie <a href="/snowboarding/">snowboarding</a>, kde jsou prkna, boty, vázání a chrániče.</p>',
    faq=[
        ('Je Horsefeathers česká značka?',
         'Ano. Firmu vedou Hanuš Salz a Pavel Kubíček, kteří se potkali v Plzni. Myšlenka a jméno vznikly v kanadské Britské Kolumbii na přelomu osmdesátých a devadesátých let.'),
        ('Co znamená název Horsefeathers?',
         'Jde o anglický hovorový výraz pro nesmysl. Zakladatelé si ho vybrali jako vtip z doby, kdy spolu jezdili na snowboardu.'),
        ('Na co se značka zaměřuje?',
         'Hlavně na oblečení na snowboard a lyže: bundy, kalhoty, čepice, termoprádlo, brýle a ponožky. K tomu přibývá oblečení do města a na kolo.'),
        ('Jak padnou bundy Horsefeathers?',
         'Bývají delší a volnější než klasické lyžařské bundy. Kdo chce přiléhavější střih, může zvolit menší velikost, kdo plánuje silné vrstvy, ponechá si rezervu.'),
        ('Je bunda Horsefeathers vhodná i na lyže?',
         'Ano. Volnější snowboardový střih lyžování nevadí. Rozhoduje spíše zateplení, parametry membrány a podlepené švy. Na skialpy nebo dlouhé výstupy se hodí lehčí skořepina bez výplně.'),
        ('Jaký je rozdíl mezi termoprádlem Riley a Mirra?',
         'Riley je pánská řada, Mirra dámská. Obě slouží jako první vrstva pod lyžařské oblečení a odvádějí pot od těla.'),
        ('Prodává Horsefeathers i oblečení na kolo?',
         'Ano, v nabídce jsou cyklistické dresy, kraťasy a trička ve stylu trailového a endurového ježdění.'),
        ('Jak prát snowboardovou bundu?',
         'Podle štítku, se zapnutými zipy a v prostředku na funkční textil, bez aviváže. Když přestane voda perlit, pomůže impregnace.'),
        ('Kdy bývají zimní kolekce levnější?',
         'Obvykle po skončení sezóny, tedy koncem zimy a na jaře. Starší barvy zlevňují i v průběhu sezóny, když dorazí nová kolekce.'),
        ('Prodává sporteka.cz oblečení Horsefeathers?',
         'Ne. Sporteka porovnává nabídky českých e-shopů a odkáže vás do obchodu, kde nákup dokončíte za jeho podmínek.'),
    ],
)

# ------------------------------------------------------------------ keen
NEW['keen'] = dict(
    title='Keen: sandály Newport, trekové boty Targhee, zimní obuv',
    desc='Boty Keen v katalogu: sandály Newport a Clearwater, trekové boty Targhee, tenisky Jasper, dětské sandály Seacamp a zimní obuv. Jak vybrat velikost.',
    intro='<p>Keen je americká značka obuvi, kterou poznáte podle gumové špičky přes prsty u sandálů. Právě uzavřený sandál Newport stál u jejího vzniku a dodnes je nejznámějším modelem. '
          'V katalogu převažují sandály pro dospělé i děti, dál turistické a trekové boty, tenisky do města, zimní obuv, pantofle a ponožky. Mezi nejčastějšími řadami jsou Targhee, Newport, Clearwater, Seacamp, Zionic, Jasper a Elle. '
          'Sporteka.cz porovnává nabídky českých obchodů, které boty Keen prodávají, abyste viděli, kde je skladem vaše velikost a barva. Samotný nákup proběhne v e-shopu, který si vyberete. Hodně modelů se vyrábí v pánské, dámské i dětské verzi a v mnoha barvách, takže se vyplatí sledovat více obchodů najednou. '
          'Níže najdete stručnou historii značky, přehled modelových řad, rady k velikostem a péči a tipy, jak porovnávat nabídky jednotlivých obchodů.</p>',
    guide='<h2>Odkud Keen pochází</h2>'
          '<p>Firmu Keen založili v roce 2003 Martin Keen a Rory Fuerst v kalifornském Alamedě. Martin Keen přišel s nápadem sandálu, který chrání prsty, už koncem devadesátých let, když hledal obuv na plachtění. Výsledkem byl Newport: otevřený sandál s pevnou gumovou špičkou, který jde nosit do vody i na kamenitou cestu. První boty se začaly vyrábět v roce 2003 a rychle se rozšířily mezi vodáky a turisty.</p>'
          '<p>V roce 2006 se sídlo přesunulo do Portlandu v Oregonu, kde firma působí dodnes. Keen je soukromá společnost a sortiment postupně rozšířil o turistickou obuv, zimní boty, městské tenisky, pracovní obuv a doplňky. Ochranná špička se ale objevuje u velké části modelů a zůstala poznávacím znamením značky.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Největší skupinou jsou <a href="/sandaly/">sandály</a>, pro které máme samostatnou stránku <a href="/sandaly-keen/">sandály Keen</a>. Následují <a href="/tenisky/">tenisky</a> a městské boty, <a href="/trekova-obuv/">treková obuv</a> v nízkém i kotníkovém provedení a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>. Dále jsou v nabídce <a href="/trailove-boty/">trailové boty</a>, <a href="/zimni-obuv/">zimní obuv</a> včetně dětských sněhulí, <a href="/pantofle-a-zabky/">pantofle</a> a <a href="/sportovni-ponozky/">ponožky</a>. Na zimní modely se zaměřuje přehled <a href="/keen-zimni-boty/">zimní boty Keen</a>.</p>'
          + '<div class="tw"><table class="ct"><thead><tr><th>Řada</th><th>Typ</th><th>Na co se hodí</th></tr></thead><tbody>'
          '<tr><td>Newport, Newport H2</td><td>uzavřený sandál s gumovou špičkou</td><td>voda, kemp, výlety v létě</td></tr>'
          '<tr><td>Clearwater CNX, Hyperport H2</td><td>sportovní sandál na vodu</td><td>sjíždění řek, pláž, brodění</td></tr>'
          '<tr><td>Seacamp II CNX</td><td>dětský uzavřený sandál</td><td>školka, hřiště, dovolená</td></tr>'
          '<tr><td>Elle, Whisper</td><td>dámský sandál</td><td>město, cestování</td></tr>'
          '<tr><td>Targhee, Circadia, Hightrail</td><td>trekové boty</td><td>turistika s batohem</td></tr>'
          '<tr><td>Zionic, Nxis</td><td>lehká turistická a trailová obuv</td><td>rychlejší túry, cesty a pěšiny</td></tr>'
          '<tr><td>Jasper, KNX</td><td>tenisky a vycházková obuv</td><td>město, lehké výlety</td></tr>'
          '<tr><td>Kanibou, Puffrider, Greta, Revel</td><td>zimní boty</td><td>sníh, mráz, zimní procházky</td></tr>'
          '</tbody></table></div>'
          '<h2>Sandály: Newport, Clearwater a další</h2>'
          '<p>Newport má horní část z popruhů, gumovou špičku a stahovací šňůrku s rychlouzávěrem. Verze H2 má popruhy z textilu, který snáší vodu a dá se umýt, klasický Newport mívá svršek z kůže, která se do vody tolik nehodí. Clearwater CNX je lehčí sportovní sandál s pružnější podešví, vhodný na vodu a teplé dny. Hyperport H2 kombinuje uzavřenou špičku s textilním svrškem, který rychle schne. Model Uneek se pozná podle svršku spleteného ze dvou šňůr, které se přizpůsobí tvaru nohy.</p>'
          '<p>Uzavřené sandály chrání prsty před kameny na dně řeky a před nárazem do kořene. Proto je mají rádi vodáci i rodiče malých dětí. Pokud chodíte do vody často, hledejte modely s označením H2 nebo textilním svrškem. Na dlouhé pochody s batohem ale sandál nenahradí trekovou botu s pevnou podešví a oporou kotníku. Pro čisté plavání nebo koupání u moře se hodí i lehčí <a href="/obuv-do-vody/">obuv do vody</a>.</p>'
          '<h2>Dětská obuv</h2>'
          '<p>Keen nabízí řadu dětských modelů, nejčastěji sandály Seacamp II CNX a Newport H2 v dětských velikostech, zimní boty Kanibou a Puffrider a tenisky KNX. Dětské velikosti se v názvech dělí na Children a Youth, tedy menší a větší děti. Uzavřená špička je u dětí praktická, protože nohy kopou do všeho. Nechte v botě rezervu kolem jednoho centimetru na růst a pohyb prstů a velikost kontrolujte každých pár měsíců.</p>'
          '<h2>Trekové a turistické boty</h2>'
          '<p>Targhee je dlouholetá turistická řada Keen. Existuje v nízké i kotníkové verzi, s membránou označenou WP nebo bez ní. Kotníková Mid verze lépe drží nohu na kamenitém terénu a s těžším batohem. Circadia, Hightrail, Headout nebo Skua jsou další turistické modely, Zionic a Nxis lehčí obuv na rychlejší chůzi a pěšiny. Modely s membránou KEEN.DRY drží vodu venku, ale v létě jsou teplejší. Pokud chodíte hlavně v suchu, zvažte verzi bez membrány, ve které se noha méně potí.</p>'
          '<h2>Zimní boty</h2>'
          '<p>Zimní nabídka zahrnuje hlavně dětské sněhule Kanibou a Puffrider, dámské boty Greta a Hoodromeo a vyšší modely Revel. Většina má nepromokavou úpravu a zateplení. Při výběru sledujte, jak vysoko jde nepromokavá část, jak je podešev měkká v mrazu a zda je bota zateplená do teplot, ve kterých ji budete nosit. Na stavění sněhuláků a hraní venku jsou vhodné vyšší <a href="/snehule/">sněhule</a>, na chůzi po městě nižší zimní boty.</p>'
          '<h2>Tenisky, pantofle a ponožky</h2>'
          '<p>Mimo sandály a trekovou obuv má Keen i boty do města. Jasper vychází z lezeckých nástupových bot a má semišový svršek a šněrování až ke špičce. Lehké tenisky KNX mají tenčí a pružnější podešev; některé obchody je řadí mezi <a href="/barefoot-obuv/">barefoot obuv</a>, ale než takové označení přijmete, zkontrolujte tloušťku podešve a převýšení paty nad špičkou. Pantofle Howser s prošívaným nebo plstěným svrškem jsou určené na doma a ke krátkému výběhu ven, Yogui a Shanti jsou lehké nazouváky z měkkého materiálu. Keen prodává také ponožky v různých výškách, od nízkých po trekové.</p>'
          '<h2>Pro koho se Keen hodí</h2>'
          '<p>Značka sedí lidem, kteří tráví hodně času venku a chtějí pohodlnou obuv bez dlouhého zahořování. Sandály ocení vodáci, rodiny s dětmi u vody a cestovatelé, kteří potřebují jedny boty na pláž i na procházku po kamenité cestě. Trekové boty Targhee jsou spolehlivá volba na běžnou turistiku v našich horách. Pro vysokohorské výstupy s mačkami ale hledejte pevnější obuv, kterou najdete mezi <a href="/vysoke-trekove-boty/">vysokými trekovými botami</a> jiných výrobců.</p>'
          '<h2>Velikosti a šířka</h2>'
          '<p>Keen je známý širší přední částí boty, takže prsty mají víc místa než v mnoha jiných značkách. Lidé s širší nohou si to chválí, kdo má úzkou nohu, může mít pocit, že v botě plave. Velikosti se mezi modely liší, proto si změřte délku chodidla v centimetrech a porovnejte ji s tabulkou konkrétního obchodu. Obchody uvádějí evropské, britské i americké číslování, což při srovnávání nabídek mate. Do trekových bot počítejte s rezervou na silnější ponožky, například z <a href="/merino-ponozky/">merina</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupovat sandály těsně: prsty mají mít před gumovou špičkou trochu místa, jinak do ní při chůzi z kopce narážejí.</li>'
          '<li>Brát nepromokavou botu na horké léto, kdy se v membráně noha zbytečně potí.</li>'
          '<li>Vybírat trekovou botu podle čísla, ne podle délky chodidla. Mezi modely se velikost liší.</li>'
          '<li>Zkoušet boty dopoledne; noha během dne mírně otéká, a večer pak bota tlačí.</li>'
          '<li>Zapomenout na ponožky: do trekových bot zkoušejte ty, ve kterých budete chodit.</li></ul>'
          '<h2>Péče</h2>'
          '<ul><li>Sandály s textilními popruhy opláchněte po koupání ve slané nebo chlorované vodě čistou vodou.</li>'
          '<li>Boty nesušte u topení ani na přímém slunci, lepení podešve by mohlo povolit.</li>'
          '<li>Kožené svršky ošetřujte přípravkem na kůži, semiš a nubuk kartáčkem a sprejem.</li>'
          '<li>U trekových bot s membránou obnovujte odpudivost svršku <a href="/impregnace/">impregnací</a>.</li>'
          '<li>Zápach u sandálů pomůže omezit pravidelné vyprání stélky, pokud to výrobce dovoluje.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Názvy modelů Keen obsahují zkratky, které je dobré znát. WP znamená nepromokavou verzi, Mid kotníkovou výšku, H2 sandál určený do vody a CNX lehčí provedení s pružnější podešví. Men, Women, Youth a Children označují pánskou, dámskou a dětskou verzi. Barvy jsou pojmenované anglicky a obchody je někdy překládají, jindy nechávají v originále. Hledejte proto podle čísla generace (Targhee III, Targhee IV) a porovnejte fotky. Sandály zlevňují koncem léta, zimní obuv na konci zimy.</p>'
          '<h2>Keen a podobné značky</h2>'
          '<p>Sportovní sandály a turistickou obuv nabízejí také '
          + B(('merrell', 'Merrell'), ('salomon', 'Salomon'), ('columbia', 'Columbia')) +
          '. Kdo hledá spíš pohodlné pantofle do města s anatomickou stélkou, může se podívat na '
          + B(('birkenstock', 'Birkenstock')) +
          '. Keen se od nich odlišuje hlavně uzavřenou špičkou a širším tvarem.</p>',
    faq=[
        ('Odkud pochází značka Keen?',
         'Z USA. Založili ji v roce 2003 Martin Keen a Rory Fuerst v kalifornském Alamedě, od roku 2006 sídlí v Portlandu v Oregonu.'),
        ('Proč mají sandály Keen gumovou špičku?',
         'Chrání prsty před kameny a nárazy. Sandál Newport vznikl jako obuv na plachtění a do vody, kde je ochrana prstů užitečná.'),
        ('Jaký je rozdíl mezi Newport a Newport H2?',
         'H2 má svršek z textilních popruhů, které snášejí vodu a dají se umýt. Klasický Newport mívá kožený svršek, vhodnější na suchou chůzi.'),
        ('Co znamená WP a Mid v názvu?',
         'WP označuje nepromokavou verzi s membránou, Mid kotníkovou výšku boty. Nízké modely zkratku Mid nemají.'),
        ('Jsou boty Keen široké?',
         'Ano, většina modelů má širší přední část. Vyhovuje lidem s širší nohou, úzká noha se v nich může hýbat.'),
        ('Jakou velikost vybrat dítěti?',
         'Změřte délku chodidla a přidejte zhruba centimetr rezervy. Dětské modely se dělí na Children a Youth podle věku a velikosti.'),
        ('Hodí se sandály Keen na turistiku?',
         'Na lehké výlety, brodění a kemp ano. Na dlouhé túry s těžkým batohem je lepší treková bota s oporou kotníku a tužší podešví, která na kamenech méně unavuje chodidlo.'),
        ('Jak čistit sandály Keen?',
         'Opláchnout vodou, stélku podle možností vyprat a sušit mimo topení a přímé slunce. Koženou verzi ošetřovat přípravkem na kůži.'),
        ('Které zimní boty Keen jsou v nabídce?',
         'Nejčastěji dětské Kanibou a Puffrider, dámské Greta a Hoodromeo a vyšší modely Revel.'),
        ('Prodává sporteka.cz boty Keen?',
         'Ne. Sporteka srovnává nabídky českých obchodů, ukáže dostupné velikosti a pošle vás do e-shopu, kde nákup dokončíte.'),
    ],
)

# ------------------------------------------------------------------ osprey
NEW['osprey'] = dict(
    title='Osprey: turistické batohy Atmos, Kestrel, Talon a další',
    desc='Batohy Osprey v katalogu: turistické Atmos, Kestrel, Talon a Hikelite, cestovní Farpoint, městské Arcane, cyklo Escapist i vaky. Jak vybrat velikost zad.',
    intro='<p>Osprey je americký výrobce batohů, který začínal šitím zakázkových krosen v Kalifornii. Dnes nabízí batohy na turistiku, cestování, kolo, běh i do města a k nim vaky, tašky a hydratační vaky. '
          'V katalogu převažují turistické batohy od lehkých denních modelů po velké krosny na vícedenní přechody. Dále najdete městské batohy Arcane, cestovní Farpoint, Fairview a tašky Transporter, cyklistické batohy a brašny Escapist, běžecké vesty Duro a Dyna, ledvinky a lehké vaky Dry Sack. '
          'Sporteka.cz staví vedle sebe nabídky českých e-shopů, abyste viděli, kde je konkrétní model, objem a velikost zad k dostání. Nákup dokončíte v obchodě, který si vyberete. U batohů hraje roli nejen objem a barva, ale hlavně velikost zad, a ta bývá skladem jen u některých prodejců. '
          'Následující průvodce vám pomůže vybrat správnou řadu, velikost a objem.</p>',
    guide='<h2>Historie značky Osprey</h2>'
          '<p>Osprey založil v roce 1974 Mike Pfotenhauer v kalifornském Santa Cruz. Batohy tehdy šil sám na zakázku a prodával je z dílny v domě. Později se firma přestěhovala do Colorada, nejprve do městečka Dolores a v roce 1994 do Cortezu, kde má sídlo dodnes. Od roku 2021 patří Osprey americké skupině Helen of Troy.</p>'
          '<p>K pověsti značky přispěla záruka All Mighty Guarantee. Osprey podle ní opraví poškození nebo vadu batohu bez ohledu na to, kdy byl koupen; pokud oprava není možná, výrobek nahradí. Podmínky a postup reklamace v Evropě najdete na stránkách výrobce. Opotřebení zipu nebo prodřené dno proto nemusí znamenat konec batohu.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Většinu nabídky tvoří <a href="/turisticke-batohy/">turistické batohy</a>, pro které máme i stránku <a href="/osprey-batoh/">batohy Osprey</a>. Následují <a href="/mestske-batohy/">městské batohy</a>, <a href="/cyklo-tasky-a-nosice/">cyklistické brašny a batohy</a>, cestovní a <a href="/sportovni-tasky/">sportovní tašky</a>, <a href="/ledvinky/">ledvinky</a> a crossbody tašky. Menší skupinu tvoří <a href="/bezecke-vesty-a-batohy/">běžecké vesty</a>, hydratační vaky a <a href="/lahve-a-termosky/">měkké lahve</a> Hydraulics a vodotěsné vaky.</p>'
          + '<div class="tw"><table class="ct"><thead><tr><th>Pánská / unisex řada</th><th>Dámská obdoba</th><th>Určení</th></tr></thead><tbody>'
          '<tr><td>Atmos AG</td><td>Aura AG</td><td>vícedenní túry, pohodlné nesení</td></tr>'
          '<tr><td>Kestrel</td><td>Kyte</td><td>univerzální turistika, hory</td></tr>'
          '<tr><td>Talon</td><td>Tempest</td><td>lehké denní túry, rychlá chůze</td></tr>'
          '<tr><td>Stratos</td><td>Sirrus</td><td>túry s větraným zádovým systémem</td></tr>'
          '<tr><td>Exos</td><td>Eja</td><td>lehké vícedenní přechody</td></tr>'
          '<tr><td>Farpoint</td><td>Fairview</td><td>cestování, letadlo, hostely</td></tr>'
          '<tr><td>Syncro, Raptor</td><td>Salida, Raven</td><td>horské kolo, hydratace</td></tr>'
          '<tr><td>Duro</td><td>Dyna</td><td>běh v terénu</td></tr>'
          '</tbody></table></div>'
          '<h2>Pánské a dámské verze</h2>'
          '<p>Osprey vyrábí většinu turistických řad ve dvou verzích. Dámská verze má jinak tvarované ramenní popruhy, kratší záda a bederní pás přizpůsobený ženské pánvi. Neplatí ale, že ženy musí nosit dámský a muži pánský model: rozhoduje délka zad a tvar postavy. Řady jako Hikelite, Sportlite nebo Daylite jsou unisex. Pro rychlou orientaci jsou užitečné i výběry <a href="/damsky-batoh/">dámský batoh</a> a <a href="/pansky-batoh/">pánský batoh</a>.</p>'
          '<h2>Jak zjistit velikost zad</h2>'
          '<p>Turistické batohy Osprey se prodávají ve velikostech podle délky trupu, nikoli podle výšky postavy. Změřte vzdálenost od výrazného obratle na spodní straně krku po pomyslnou spojnici horních hran pánevních kostí. Výsledek v centimetrech porovnejte s tabulkou výrobce u konkrétního modelu. Velikosti se značí například S/M, M/L nebo L/XL a některé modely mají nastavitelná záda. U nastavitelných zad si systém doladíte podle sebe, u pevných je přesná velikost důležitější.</p>'
          '<p>Při zkoušení naložte batoh zhruba tou zátěží, kterou budete nosit. Bederní pás má sedět na hranách pánve a nést většinu váhy, ramenní popruhy mají přiléhat bez mezery a stabilizační popruhy nad rameny držet horní část batohu u těla. Pokud vás batoh tlačí do krku nebo bederní pás sjíždí na břicho, zkuste jinou velikost.</p>'
          '<h2>Objem podle délky túry</h2>'
          '<ul><li>Do 20 litrů: běh, kolo, krátký výlet s pitím a bundou (Talon, Daylite, Hikelite).</li>'
          '<li>Kolem 20 až 35 litrů: celodenní túra, horská chata s přespáním (Talon, Stratos, Kestrel).</li>'
          '<li>Kolem 35 až 50 litrů: víkend, chata nebo nocleh pod širákem s lehkou výbavou (Kestrel, Exos).</li>'
          '<li>Nad 50 litrů: vícedenní přechod se stanem, spacákem a vařičem (Atmos, Aura, Kestrel, Kyte).</li></ul>'
          '<p>Větší batoh svádí k tomu, nabalit víc. Pokud máte lehký spacák a stan, často vám stačí menší objem a ušetříte záda. Když vybíráte batoh pro dítě, podívejte se na výběr <a href="/detsky-batoh/">dětské batohy</a>; Osprey má i dětskou verzi Daylite.</p>'
          '<h2>Lehké denní batohy Hikelite, Sportlite a Daylite</h2>'
          '<p>Na kratší výlety nabízí Osprey několik jednodušších řad. Hikelite má síťovinu odsazenou od zad a často i pláštěnku, takže se hodí na letní túry. Sportlite je sportovně střižený batoh s pevnějším bederním pásem pro rychlejší pohyb. Daylite je nejjednodušší řada: menší batohy, ledvinky a crossbody tašky na každý den, které jde připnout i k většímu batohu Osprey. Pokud chcete jen jeden batoh na výlety i do práce, podívejte se i na modely s přihrádkou na notebook mezi <a href="/batohy-na-notebook/">batohy na notebook</a>.</p>'
          '<h2>Zádové systémy</h2>'
          '<p>Řady Atmos a Aura AG používají systém Anti-Gravity: napnutou síťovinu, která obepíná záda i bederní oblast a nechá vzduch proudit mezi batohem a tělem. Stratos a Sirrus mají síťovinu odsazenou od zad, takže se méně potíte. Kestrel a Kyte mají záda polstrovaná a blíže k tělu, což je stabilnější v náročném terénu. Při výběru zvažte, zda dáváte přednost větrání, nebo stabilitě na skalnatém terénu.</p>'
          '<h2>Cestování, město a kolo</h2>'
          '<p>Farpoint a Fairview se otevírají po celém obvodu jako kufr a mají zádový systém, který lze schovat. Hodí se na letecké cestování a pobyty s častým přejížděním. Tašky Transporter Duffel mají odnímatelné popruhy a dají se nést jako batoh; podobné zavazadlo hledejte i mezi <a href="/cestovni-tasky/">cestovními taškami</a>. Arcane je městský batoh na notebook a každodenní nošení. Pro kolo jsou určené batohy Syncro, Raptor a Metron a brašny Escapist na řídítka, rám a podsedlovku.</p>'
          '<h2>Jak batoh správně sbalit</h2>'
          '<p>Těžké věci, jako je jídlo, voda nebo vařič, patří do středu batohu blízko zad. Těžiště pak zůstane u těla a batoh vás nestahuje dozadu. Spacák dejte na dno, lehké a objemné věci do horní části a na okraje. Pláštěnku, čelovku a lékárničku mějte ve víku nebo v boční kapse, abyste se k nim dostali rychle. Řady Kestrel a Kyte mají vestavěnou pláštěnku na batoh. U ostatních modelů ji dokupte, nebo věci uvnitř zabalte do vodotěsných vaků.</p>'
          '<h2>Běh, hydratace a vaky</h2>'
          '<p>Běžecké vesty Duro a Dyna se nosí přiléhavě jako tričko a mají na prsou kapsy na měkké lahve. Velikost se u nich vybírá podle obvodu hrudníku, nikoli podle délky zad. Hydratační vaky Hydraulics se zasouvají do přihrádky v batohu a hadička vede přes rameno, takže pijete bez zastavování. Lehké vaky Ultralight Dry Sack a Dry Sack s průhledným okénkem slouží k organizaci a ochraně věcí před vodou, a to v batohu i na lodi. Dětské nosítko Poco je samostatná kategorie; při výběru sledujte nosnost a doporučený věk dítěte podle výrobce.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Volit velikost podle výšky postavy místo délky trupu.</li>'
          '<li>Nosit váhu na ramenou: bederní pás má být utažený na hranách pánve, ne na břiše.</li>'
          '<li>Koupit příliš velký objem a pak ho zbytečně plnit.</li>'
          '<li>Zkoušet prázdný batoh. Rozdíly v pohodlí se ukážou až se zátěží.</li>'
          '<li>Přehlédnout dámskou verzi, která může sedět lépe i menším mužům, a naopak.</li></ul>'
          '<h2>Péče o batoh</h2>'
          '<ul><li>Batoh neperte v pračce; nečistoty odstraňte kartáčem a vlažnou vodou s jemným mýdlem.</li>'
          '<li>Sušte ho volně ve stínu, rozepnutý a vyprázdněný.</li>'
          '<li>Zipy občas vyčistěte od písku, jinak se rychleji opotřebují.</li>'
          '<li>Hydratační vak po každém použití propláchněte a nechte vyschnout otevřený.</li>'
          '<li>Při poškození zjistěte, zda se na opravu nevztahuje záruka výrobce.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Číslo v názvu udává objem v litrech, ale u některých modelů se liší podle velikosti zad. Obchody často zapisují model různě, například s velikostí, kódem nebo jen barvou. Porovnávejte proto název řady, objem i velikost zad a dejte pozor na generaci modelu, protože starší a novější verze se mohou lišit hmotností i zádovým systémem. Některé e-shopy zařazují batohy do nečekaných kategorií, proto hledejte hlavně podle jména modelu.</p>'
          '<h2>Osprey a podobné značky</h2>'
          '<p>Turistické batohy se srovnatelným zaměřením nabízejí také '
          + B(('deuter', 'Deuter'), ('the-north-face', 'The North Face'), ('mammut', 'Mammut'), ('fjallraven', 'Fjällräven')) +
          '. Rozdíly jsou hlavně v zádových systémech a střihu, proto vybírejte podle toho, jak vám batoh sedí, nikoli podle loga.</p>',
    faq=[
        ('Odkud pochází Osprey?',
         'Z USA. Mike Pfotenhauer začal batohy šít v roce 1974 v kalifornském Santa Cruz, dnes firma sídlí v Cortezu v Coloradu.'),
        ('Jakou záruku Osprey dává?',
         'All Mighty Guarantee: výrobce opraví poškození nebo vadu bez ohledu na stáří batohu, a pokud to nejde, výrobek nahradí. Podrobnosti uvádí na svém webu.'),
        ('Jak zjistím velikost batohu?',
         'Změřte délku trupu od výrazného obratle na krku po spojnici horních hran pánve a porovnejte ji s tabulkou u konkrétního modelu.'),
        ('Jaký je rozdíl mezi Atmos a Aura?',
         'Jde o stejnou řadu se systémem Anti-Gravity. Atmos je pánská verze, Aura dámská s jinými popruhy a bederním pásem.'),
        ('Kestrel, nebo Talon?',
         'Talon je lehčí batoh na rychlé denní túry, Kestrel robustnější s polstrovanými zády na hory a delší výlety. Kestrel má navíc vestavěnou pláštěnku, u Talonu ji musíte dokoupit.'),
        ('Jaký objem potřebuji na víkend?',
         'Obvykle 35 až 50 litrů. S lehkým spacákem a stanem stačí spodní hranice, s objemnější výbavou spíš horní.'),
        ('Hodí se Osprey na letecké cestování?',
         'Ano, řady Farpoint a Fairview se otevírají jako kufr. Rozměry příručního zavazadla si ale vždy ověřte u letecké společnosti.'),
        ('Mohu batoh Osprey prát v pračce?',
         'Ne. Čistěte ho ručně vlažnou vodou s jemným mýdlem a nechte volně uschnout ve stínu. Pračka může poškodit povrchovou úpravu látky, pěny v zádech i přezky.'),
        ('Má Osprey batohy na kolo a běh?',
         'Ano. Na kolo Syncro, Raptor a brašny Escapist, na běh vesty Duro a dámské Dyna.'),
        ('Prodává sporteka.cz batohy Osprey?',
         'Ne. Sporteka srovnává nabídky českých obchodů a odkáže vás do e-shopu, kde nákup dokončíte. Záruku a vrácení řešíte s obchodem, záruku výrobce s firmou Osprey.'),
    ],
)

# ------------------------------------------------------------------ dc-shoes
NEW['dc-shoes'] = dict(
    title='DC Shoes: skate tenisky Manteca, Court Graffik a Pure',
    desc='Boty DC Shoes v katalogu: skate tenisky Manteca 4, Court Graffik, Pure, Stag a Crisis 2, zimní verze WNT i snowboardové boty. Jak vybrat velikost.',
    intro='<p>DC Shoes je kalifornská značka obuvi a oblečení, která vyrostla ze skateboardingu devadesátých let. Je známá masivními teniskami s polstrovaným jazykem, které se nosí na prkně i do města. '
          'V katalogu tvoří naprostou většinu nabídky tenisky: Manteca 4 ve verzích nízké, vysoké i na platformě, Court Graffik, Pure a Pure High-Top, Stag, Crisis 2, Manual, Teknic nebo Kalynx Zero. Menší část připadá na zimní varianty, snowboardové boty, čepice a pár kusů oblečení na sníh. '
          'Sporteka.cz zde řadí vedle sebe nabídky českých e-shopů, takže uvidíte, kde je konkrétní model, barva a velikost skladem. Zboží si pak objednáte v obchodě, který vám vyhovuje. '
          'Pod úvodem najdete průvodce hlavními modely, rozdíly mezi typy podrážek, radu k velikostem, péči o semiš a kůži a tipy, jak se vyznat v kódech, které obchody uvádějí v názvech produktů.</p>',
    guide='<h2>Jak vznikla DC Shoes</h2>'
          '<p>Firmu založili v červnu 1994 v jižní Kalifornii Damon Way, Ken Block a Clayton Blehm. Zkratka DC původně znamenala Droors Clothing, podle oděvní značky, se kterou zakladatelé začínali. Boty DC si rychle získaly jezdce na skateboardu, kteří potřebovali obuv odolnou proti brusnému papíru na desce a s dobrým polstrováním při dopadech. Později se značka rozšířila o snowboardové boty, oblečení a doplňky.</p>'
          '<p>V roce 2004 koupil DC Shoes výrobce surfového oblečení Quiksilver a sídlo se o několik let později přesunulo do Huntington Beach. Dnes značka patří pod skupinu Authentic Brands Group. Na botách se objevuje typické logo DC a od roku 2011 také logo ve tvaru vlajky, které značka zavedla při omlazení své image.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Téměř celá nabídka spadá do kategorie <a href="/tenisky/">tenisky</a>. Část obchodů řadí skate boty mezi vybavení na <a href="/skateboardy/">skateboard</a>, jiné k běžné vycházkové obuvi. K zimě jsou v nabídce verze s teplou podšívkou, které najdete i mezi <a href="/zimni-obuv/">zimní obuví</a>, a několik párů <a href="/snowboardove-boty/">snowboardových bot</a>. Menší skupinu tvoří <a href="/cepice-a-celenky/">čepice</a>, <a href="/lyzarske-bundy/">lyžařské bundy</a> a <a href="/mikiny/">mikiny</a>.</p>'
          + '<div class="tw"><table class="ct"><thead><tr><th>Model</th><th>Charakter</th><th>Na co se hodí</th></tr></thead><tbody>'
          '<tr><td>Manteca 4 (Hi, Platform)</td><td>skate bota se semišovým nebo koženým svrškem</td><td>skateboard, město</td></tr>'
          '<tr><td>Court Graffik</td><td>masivní tvar, polstrovaný jazyk a límec</td><td>každodenní nošení, město</td></tr>'
          '<tr><td>Pure, Pure High-Top</td><td>jednoduchý svršek, nízká i kotníková verze</td><td>město, skate</td></tr>'
          '<tr><td>Pure High-Top WNT</td><td>zimní verze s teplou podšívkou</td><td>chladné dny ve městě</td></tr>'
          '<tr><td>Stag, Net, Central</td><td>vycházkové tenisky</td><td>běžné nošení</td></tr>'
          '<tr><td>Crisis 2, Kalynx Zero, Teknic</td><td>lehčí skate a lifestyle modely</td><td>skate, léto, město</td></tr>'
          '<tr><td>Phase, Control</td><td>snowboardové boty s utahováním Boa</td><td>sjezdovka, park</td></tr>'
          '</tbody></table></div>'
          '<h2>Manteca 4 a Court Graffik</h2>'
          '<p>Manteca 4 je v nabídce nejčastější model. Má svršek ze semiše nebo kůže, zesílenou špičku a polstrovaný límec. Verze Hi sahá ke kotníku, Platform má vyšší podrážku. Court Graffik je masivnější bota s typickým tvarem objemných skate tenisek: široký jazyk, výrazné polstrování a pevná podrážka. Lidé, kteří na prkně nejezdí, ji nosí jako pohodlnou botu do města, skateři oceňují ochranu nohy při dopadech.</p>'
          '<h2>Pure a zimní verze WNT</h2>'
          '<p>Pure je jednodušší, střídmější silueta v nízké a kotníkové verzi. U modelu Pure High-Top se objevují varianty se zkratkou WNT, což je zimní provedení s teplou podšívkou z umělé kožešiny nebo podobného materiálu. Nejde ale o specializované nepromokavé zimní boty. Do mokrého sněhu a břečky je ošetřete <a href="/impregnace/">impregnací</a> a počítejte s tím, že déle vydrží spíš v suchém mrazu než v rozbředlém sněhu. Na hory a do hlubokého sněhu se hodí vyšší boty s nepromokavou membránou.</p>'
          '<h2>Typy podrážek u skate bot</h2>'
          '<p>Skate tenisky se obecně dělí podle konstrukce podrážky. Vulkanizovaná podrážka je tenčí a ohebnější, takže je v ní dobře cítit deska; bota se rychle rozchodí, ale méně tlumí dopady. Lepená podrážka, takzvaný cupsole, je tužší a silnější a lépe chrání chodidlo při skocích ze schodů, za cenu menšího citu. DC vyrábí oba typy a u konkrétního modelu najdete informaci v popisu výrobce nebo obchodu. Pro začátečníky a pro každodenní nošení bývá pohodlnější pevnější podrážka.</p>'
          '<h2>Na co se dívat u skate bot</h2>'
          '<ul><li>Semiš vydrží odírání o brusný papír na desce déle než plátno.</li>'
          '<li>Zesílená špička a místo pro ollie oddálí prodření boty.</li>'
          '<li>Polstrovaný jazyk a límec chrání nárt a kotník před nárazem desky.</li>'
          '<li>Gumová podrážka s jemným vzorkem drží na desce, hrubý vzorek se hodí spíš na chůzi.</li>'
          '<li>Šněrování chráněné v průchodkách se tak rychle nepřetrhne.</li></ul>'
          '<h2>Snowboardové boty</h2>'
          '<p>DC vyrábí i boty na snowboard, v nabídce jsou například modely Phase a Control. Utahují se kolečkem Boa, které nahrazuje tkaničky a jde ovládat v rukavicích. Některé verze jsou kompatibilní se systémem Step On, u kterého se bota cvakne do vázání bez páček; takové boty potřebují odpovídající <a href="/snowboardova-vazani/">vázání</a>. Snowboardové boty se vybírají podle délky chodidla a tuhosti: měkčí odpustí chyby a hodí se do parku, tužší lépe přenášejí sílu při rychlé jízdě. Doporučujeme vyzkoušet je s ponožkami, ve kterých budete jezdit. Nové boty se v prvních dnech na svahu ještě usadí, proto by měly zpočátku sedět pevně, ale nesmí tlačit ani brnět prsty.</p>'
          '<h2>Velikosti</h2>'
          '<p>DC uvádí velikosti v amerických číslech a obchody je převádějí na evropská, někdy i na britská. Převod se mezi obchody může o půl čísla lišit, proto se řiďte délkou chodidla v centimetrech. Dětské modely mají v názvu označení pro chlapce nebo dívky, případně Youth. Skate tenisky s masivním polstrováním působí v botě objemněji, ale délka zůstává stejná. Pokud nosíte vlastní ortopedické <a href="/vlozky-do-bot/">vložky do bot</a>, vyzkoušejte, zda se vejdou pod jazyk.</p>'
          '<h2>Péče o semiš, nubuk a kůži</h2>'
          '<ul><li>Prach a zaschlé bláto odstraňte suchým kartáčem na semiš.</li>'
          '<li>Skvrny čistěte gumou na semiš nebo mírně vlhkým hadříkem, ne v pračce.</li>'
          '<li>Kůži otřete vlhkým hadříkem a občas ošetřete krémem.</li>'
          '<li>Před zimou boty ošetřete sprejem proti vodě a soli.</li>'
          '<li>Mokré boty vycpěte papírem a nechte vyschnout mimo topení.</li></ul>'
          '<h2>Jak se vyznat v názvech</h2>'
          '<p>Obchody přebírají názvy z různých zdrojů, a tak se u stejné boty můžete setkat s francouzským slovem Baskets, kódem výrobce nebo jen s obecným popisem. Hledejte podle jména modelu (Manteca 4, Court Graffik, Pure High-Top) a porovnávejte fotky. Kódy jako ADYS nebo ADJS označují konkrétní model a barvu u výrobce a pomohou najít stejný kus v jiném obchodě. Zkratky Hi nebo HT znamenají kotníkovou verzi a WNT zimní provedení.</p>'
          '<h2>Pro koho jsou boty DC</h2>'
          '<p>Skateři hledají hlavně odolnost a cit na desce, takže volí semišové modely s pevnou špičkou a dobře padnoucí patou. Pro každodenní nošení do školy nebo do práce rozhoduje spíš pohodlí a vzhled, proto si lidé vybírají Court Graffik, Manteca 4 nebo Stag. Platformové verze přidávají pár centimetrů výšky a jsou oblíbené u dívek a žen. Na sport, kde se hodně běhá, například na fotbal nebo tenis, skate boty nehledejte; jsou těžší a nemají potřebnou oporu pro rychlé změny směru. Na běh je určená <a href="/bezecka-obuv/">běžecká obuv</a>.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Vedle bot nabízí DC i čepice, <a href="/ksiltovky/">kšiltovky</a>, mikiny a trička s logem a v zimní sezóně bundy a kalhoty na sníh. V našem katalogu je oblečení menšina, většinu tvoří obuv. Lyžařské a snowboardové bundy DC mají volnější střih typický pro prkno, kapuci a sněhový pás. Pokud k teniskám hledáte ponožky, vyberte vyšší <a href="/sportovni-ponozky/">sportovní ponožky</a>, které chrání kotník před odřením o límec boty.</p>'
          '<h2>Kdy kupovat</h2>'
          '<p>Tenisky se prodávají celý rok, slevy přicházejí hlavně při obměně kolekcí a na konci sezóny. Zimní verze WNT bývají nejlevnější na konci zimy. Oblíbené barvy klasických modelů, jako je černá Manteca nebo Court Graffik v kombinaci černé a bílé, se vracejí každý rok, takže se na ně dá počkat. Pokud vám jde o konkrétní velikost, sledujte vývoj nabídky v několika obchodech.</p>'
          '<h2>DC Shoes a podobné značky</h2>'
          '<p>Skate tenisky a obuv do města se podobným stylem nabízejí také '
          + B(('vans', 'Vans'), ('converse', 'Converse'), ('puma', 'Puma')) +
          '. Klasické skate boty má i výběr <a href="/tenisky-vans/">tenisky Vans</a>. Na snowboardu potkáte DC vedle oblečení '
          + B(('horsefeathers', 'Horsefeathers'), ('roxy', 'Roxy')) +
          '; celou výbavu na prkno najdete v kategorii <a href="/snowboarding/">snowboarding</a>.</p>',
    faq=[
        ('Kdo založil DC Shoes?',
         'Damon Way, Ken Block a Clayton Blehm v červnu 1994 v jižní Kalifornii. Značka dnes patří pod skupinu Authentic Brands Group.'),
        ('Co znamená zkratka DC?',
         'Původně Droors Clothing, podle oděvní značky zakladatelů. Dnes se používá jen jako název DC Shoes.'),
        ('Jaký je rozdíl mezi Manteca 4 a Court Graffik?',
         'Manteca 4 je střídmější skate bota se semišovým nebo koženým svrškem. Court Graffik je masivnější s výrazným polstrováním jazyka a límce.'),
        ('Co znamená WNT v názvu boty?',
         'Zimní verzi modelu, například Pure High-Top WNT, s teplou podšívkou. Nejde ale o plně nepromokavou zimní obuv.'),
        ('Jsou boty DC vhodné na skateboard?',
         'Ano, značka z prostředí skateboardingu vychází. Na prkno se hodí modely se semišovým svrškem, zesílenou špičkou a polstrováním. Plátěné tenisky se na desce prodřou rychleji.'),
        ('Jak vybrat velikost DC Shoes?',
         'Řiďte se délkou chodidla v centimetrech. Obchody převádějí americká čísla na evropská a převod se může o půl čísla lišit. Měřte večer a nechte si malou rezervu na prsty.'),
        ('Vyrábí DC i snowboardové boty?',
         'Ano, v nabídce jsou například modely Phase a Control s utahováním Boa, některé verze jsou kompatibilní se systémem Step On.'),
        ('Jak čistit semišové tenisky?',
         'Suchým kartáčem a gumou na semiš, nikdy v pračce. Před zimou je ošetřete sprejem proti vodě. Mokré boty vycpěte papírem a sušte mimo topení, aby kůže neztvrdla.'),
        ('Proč mají stejné boty v různých obchodech jiný název?',
         'Obchody přebírají popisy z různých zdrojů, někdy i v cizím jazyce. Hledejte podle jména modelu nebo kódu výrobce a porovnejte fotky.'),
        ('Prodává sporteka.cz boty DC?',
         'Ne. Sporteka srovnává nabídky českých obchodů a pošle vás do e-shopu, kde nákup dokončíte za jeho podmínek.'),
    ],
)

# ------------------------------------------------------------------ victorinox
NEW['victorinox'] = dict(
    title='Victorinox: švýcarské kapesní nože, multitooly a nože',
    desc='Victorinox v katalogu: kapesní nože Classic, Huntsman, Spartan a Ranger Grip, kleště SwissTool, kuchyňské nože, škrabky, pouzdra a brousky.',
    intro='<p>Victorinox je švýcarský výrobce nožů z obce Ibach, který proslavil červený kapesní nůž s křížem ve štítu. Pod označením Swiss Army Knife ho zná celý svět. '
          'V katalogu převažují kapesní nože v různých délkách a výbavách, od malého Classic SD na klíče po velké zavírací nože s pojistkou čepele. Následují multitooly SwissTool, nože s pevnou čepelí, kuchyňské nože Swiss Classic a Swiss Modern, škrabky, piknikové sady a doplňky: pouzdra, brousky, olej a přívěsky. '
          'Sporteka.cz shromažďuje nabídky českých e-shopů, které Victorinox prodávají, a ukazuje je vedle sebe, abyste viděli, kde je konkrétní model a barva k dostání. Objednávku dokončíte v obchodě, který si vyberete. Stejný nůž se často prodává v několika barvách a edicích, které se liší jen střenkou, proto se vyplatí porovnat více obchodů. '
          'Níže je průvodce historií firmy, velikostmi a výbavou kapesních nožů, rozdíly mezi řadami a péčí o čepele.</p>',
    guide='<h2>Historie firmy Victorinox</h2>'
          '<p>Karl Elsener otevřel v roce 1884 nožířskou dílnu v Ibachu ve švýcarském kantonu Schwyz. V roce 1891 dodal spolu s dalšími švýcarskými nožíři první vojenské nože švýcarské armádě. O šest let později, v roce 1897, si nechal patentovat původní Swiss Officer’s and Sports Knife, tedy důstojnický a sportovní nůž s více nástroji. Z něj vychází celá dnešní řada kapesních nožů.</p>'
          '<p>V roce 1909 zvolil Elsener jako obchodní jméno křestní jméno své matky Victorie a zaregistroval znak kříže ve štítu. Po vynálezu nerezové oceli, zkráceně inox, vzniklo v roce 1921 spojením obou slov jméno Victorinox. V roce 2005 firma převzala dlouholetého konkurenta, výrobce nožů Wenger z Delémontu. Kromě nožů dnes Victorinox vyrábí i hodinky a cestovní zavazadla, ta ale v naší nabídce nenajdete.</p>'
          '<h2>Co v katalogu najdete</h2>'
          '<p>Většinu nabídky tvoří kapesní nože a nářadí v kategorii <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitooly</a>. Pouzdra, škrabky, brousky a drobnosti jsou mezi <a href="/outdoor-doplnky/">outdoorovými doplňky</a>. Kuchyňské nože, piknikové příbory a teleskopická vidlička na opékání se hodí ke <a href="/kempingove-nadobi/">kempingovému nádobí</a> a <a href="/vareni-v-prirode/">vaření v přírodě</a>. Obchody je ale zařazují různě, takže hledejte hlavně podle názvu modelu.</p>'
          + '<div class="tw"><table class="ct"><thead><tr><th>Délka zavřeného nože</th><th>Příklady modelů</th><th>Na co se hodí</th></tr></thead><tbody>'
          '<tr><td>58 mm</td><td>Classic SD, Midnite Manager</td><td>klíče, kabelka, drobné opravy</td></tr>'
          '<tr><td>84 mm</td><td>Bantam</td><td>kapsa, lehká výbava</td></tr>'
          '<tr><td>91 mm</td><td>Spartan, Huntsman, Climber, Tinker, Swiss Champ</td><td>výlety, kemp, univerzální použití</td></tr>'
          '<tr><td>111 mm</td><td>Workchamp, Hunter, Rescue Tool</td><td>práce, myslivost, záchranáři</td></tr>'
          '<tr><td>130 mm</td><td>řada Ranger Grip</td><td>náročnější outdoor, práce v rukavicích</td></tr>'
          '<tr><td>multitool</td><td>SwissTool, SwissTool X, MXBS</td><td>kutilství, kolo, auto</td></tr>'
          '</tbody></table></div>'
          '<h2>Kapesní nože: délka a výbava</h2>'
          '<p>Kapesní nože Victorinox se liší délkou ve složeném stavu a počtem nástrojů. Nejmenší Classic SD má malou čepel, nůžky, pilník se šroubovákem, pinzetu, párátko a kroužek na klíče. Hodí se na drobnosti, jako je otevření balíčku nebo zastřižení nitě. Modely o délce 91 mm jsou nejrozšířenější. Spartan má dvě čepele, otvírák na konzervy a lahve, vývrtku a šídlo. Huntsman k tomu přidává nůžky a pilku na dřevo, což je praktické v kempu. Swiss Champ patří k nejvybavenějším modelům a obsahuje i kleštičky, lupu nebo propisku.</p>'
          '<p>Víc nástrojů ale znamená širší a těžší nůž. Před nákupem si sepište, co skutečně použijete. Na výlety obvykle stačí čepel, nůžky, pilka a otvírák; na kolo se hodí šroubováky a imbus, který mají některé speciální modely. Nůž, který kvůli váze necháte doma, vám nepomůže.</p>'
          '<h2>Střenky: Cellidor, Alox a dřevo</h2>'
          '<p>Klasické červené střenky jsou z plastu Cellidor a existují i v průhledných nebo barevných verzích. Řada Alox má střenky z eloxovaného hliníku s jemným rýhováním. Je tenčí a odolnější proti poškrábání, ale nemá pinzetu a párátko, protože pro ně v hliníkové střence není drážka. Dřevěné střenky jsou na omak příjemné a časem získávají patinu. Ranger Grip má dvousložkové pogumované střenky, které drží v ruce i za mokra nebo v rukavicích.</p>'
          '<h2>Pojistka čepele a jednoruční otevírání</h2>'
          '<p>Menší kapesní nože nemají pojistku čepele, čepel drží jen pružina. Při práci proto netlačte na hřbet čepele směrem ke střence a nepoužívejte nůž jako páčidlo. Velké modely o délce 111 a 130 mm mají většinou zámek čepele, který brání nechtěnému zavření na prsty. Některé verze mají otvor nebo výstupek pro otevírání jednou rukou, což se hodí při práci, kdy druhou rukou něco držíte. Pro děti vybírejte menší nůž a první řezání s nimi trénujte pod dohledem.</p>'
          '<h2>Multitooly SwissTool a nože s pevnou čepelí</h2>'
          '<p>SwissTool je multitool s kombinačkami, ke kterým se přidávají čepele, šroubováky, pilník a další nástroje. Nástroje jsou zajištěné pojistkou, takže se při práci nezavřou. Hodí se do auta, na chatu i k údržbě kola, kde doplní <a href="/cyklo-pumpy-a-naradi/">cyklo nářadí</a>. Pro bushcraft a práci se dřevem jsou určené nože s pevnou čepelí, například Venture, které se nosí v pouzdru na opasku a snesou větší zátěž než zavírací nůž. Do přírody se k nim hodí i <a href="/celovky-a-svitilny/">čelovka</a> a <a href="/prvni-pomoc/">lékárnička</a>.</p>'
          '<h2>Kuchyňské nože a škrabky</h2>'
          '<p>Kromě kapesních nožů má Victorinox rozsáhlou kuchyňskou řadu. V nabídce jsou nože na zeleninu a rajčata s vlnkovaným ostřím, steakové nože, kuchařské nože Swiss Modern, vykosťovací nože Fibrox, sady nožů a škrabky Rapid, Rex nebo Ypso. Malý nůž na zeleninu se skládací čepelí nebo v pouzdře je praktický na <a href="/kemping/">kemping</a> a piknik, kde potřebujete krájet chleba a zeleninu. Piknikové sady příborů Swiss Classic zase nahradí jednorázové plastové příbory.</p>'
          '<h2>Doplňky</h2>'
          '<ul><li>Pouzdra z kůže, nylonu nebo silikonu chrání nůž a umožní nosit ho na opasku.</li>'
          '<li>Brousky, včetně kapesních s keramickými kolečky, udrží ostří v dobrém stavu.</li>'
          '<li>Olej na multitooly udrží klouby lehce pohyblivé.</li>'
          '<li>Přívěsky a karabiny pomohou připnout malý nůž ke klíčům.</li>'
          '<li>Závěsy na opasek drží nůž po ruce, aniž by se v kapse otíral o klíče a telefon.</li></ul>'
          '<h2>Jak vybrat nůž podle použití</h2>'
          '<ul><li>Klíče a kabelka: malý nůž o délce 58 mm s nůžkami a pilníkem.</li>'
          '<li>Výlety a kemp: model 91 mm s pilkou, nůžkami a otvírákem.</li>'
          '<li><a href="/rybareni/">Rybaření</a>: nůž s čepelí, nůžkami na vlasec a háčkem, případně multitool s kleštěmi.</li>'
          '<li>Myslivost a <a href="/lovecke-vybaveni/">lovecké vybavení</a>: větší zavírací nůž s pojistkou, například Hunter.</li>'
          '<li>Dílna, auto, kolo: SwissTool s kleštěmi a šroubováky.</li>'
          '<li>Piknik: skládací nůž na zeleninu nebo sada příborů v pouzdře.</li></ul>'
          '<h2>Broušení</h2>'
          '<p>I kvalitní ocel se časem otupí. Kapesní nože se nejsnáze brousí na kapesním brousku s keramickými kolečky nebo na brusném kameni. Držte stálý úhel a táhněte čepel celou délkou ostří, jinak vznikne zub. Po broušení nůž opláchněte, aby na něm nezůstaly kovové piliny. Vlnkované ostří nožů na rajčata se brousí obtížněji a vyžaduje kulatou brusnou tyčinku, proto ho svěřte odborníkovi nebo použijte brousek, který výrobce pro takové čepele uvádí. Pravidelné lehké přebroušení je šetrnější než jedno razantní broušení tupého nože.</p>'
          '<h2>Péče o nože</h2>'
          '<p>Po použití kapesní nůž opláchněte teplou vodou, otevřete a zavřete nástroje, aby se vyplavily nečistoty z kloubů, a nechte ho vyschnout. Občas na klouby kápněte olej. Kapesní nože do myčky nedávejte, agresivní prostředky a horká pára škodí střenkám i pružinám. Kuchyňské nože myjte raději ručně a hned osušte, ostří tak vydrží déle. Nerezová ocel odolává korozi, ale ne nekonečně: po kontaktu se slanou vodou nebo kyselými potravinami nůž vždy opláchněte. Tupé ostří obnovte broušením, nečekejte, až nůž začne trhat místo řezat.</p>'
          '<h2>Cestování s nožem</h2>'
          '<p>Kapesní nůž je užitečný na cestách, ale u bezpečnostní kontroly na letišti může být problém. Pravidla pro příruční zavazadla jsou přísná a liší se podle letiště i dopravce. Před letem si je ověřte; nejjistější je uložit nůž do odbavovaného zavazadla. Na výlet ho noste v kapse nebo v pouzdře a nenechávejte ho volně v batohu mezi ostatními věcmi.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Kapesní nože mají v názvu délku v milimetrech a u mnoha obchodů i katalogové číslo výrobce. Stejný model se často prodává v několika barvách a limitovaných edicích. Porovnávejte proto název modelu, délku a výbavu, ne jen barvu. U kuchyňských nožů sledujte délku čepele a typ ostří. Některé obchody uvádějí jen obecný název, například kapesní nůž, a model poznáte až podle kódu nebo fotky.</p>',
    faq=[
        ('Odkud pochází Victorinox?',
         'Ze Švýcarska. Karl Elsener otevřel v roce 1884 nožířskou dílnu v Ibachu v kantonu Schwyz, kde firma začínala.'),
        ('Co znamená název Victorinox?',
         'Spojení jména Victoria, podle matky zakladatele, a zkratky inox pro nerezovou ocel. Název se používá od roku 1921.'),
        ('Jaký kapesní nůž vybrat na výlety?',
         'Nejčastěji model o délce 91 mm s čepelí, nůžkami, pilkou a otvírákem, například Huntsman. Na klíče stačí malý Classic SD, na náročnější práci se hodí větší nůž s pojistkou čepele.'),
        ('Jaký je rozdíl mezi Spartan a Huntsman?',
         'Oba mají délku 91 mm. Huntsman navíc obsahuje nůžky a pilku na dřevo, je tedy o něco širší a těžší.'),
        ('Co je řada Alox?',
         'Kapesní nože se střenkami z eloxovaného hliníku. Jsou tenčí a odolnější proti poškrábání, ale nemají pinzetu ani párátko.'),
        ('Mají nože Victorinox pojistku čepele?',
         'Velké modely o délce 111 a 130 mm ji většinou mají. Malé kapesní nože drží čepel jen pružinou.'),
        ('Mohu kapesní nůž mýt v myčce?',
         'Ne. Opláchněte ho teplou vodou, několikrát otevřete a zavřete nástroje, nechte vyschnout a klouby občas promažte olejem na multitooly.'),
        ('Mohu nůž vzít do letadla?',
         'Pravidla pro příruční zavazadla jsou přísná a liší se podle letiště. Nejjistější je uložit nůž do odbavovaného zavazadla, jinak vám ho u bezpečnostní kontroly mohou odebrat.'),
        ('Prodává Victorinox i kuchyňské nože?',
         'Ano. V nabídce jsou nože na zeleninu, steakové a kuchařské nože, sady nožů, škrabky i piknikové příbory. Menší skládací nože na zeleninu se hodí i do kempu.'),
        ('Prodává sporteka.cz nože Victorinox?',
         'Ne. Sporteka srovnává nabídky českých obchodů a odkáže vás do e-shopu, kde nákup dokončíte.'),
    ],
)

# ------------------------------------------------------------------ hoka
NEW['hoka'] = dict(
    title='Hoka: běžecké boty Clifton, Bondi, Speedgoat a další',
    desc='Boty Hoka v katalogu: silniční Clifton, Bondi, Mach a Arahi, trailové Speedgoat, Challenger a Mafate, turistické Anacapa a Kaha. Jak vybrat velikost.',
    intro='<p>Hoka je značka běžecké obuvi z francouzských Alp, kterou poznáte podle výrazně vysoké a měkké mezipodešve. Když se před lety objevila na závodech v horách, působila zvláštně, dnes ji nosí rekreační běžci, ultramaratonci i lidé, kteří hodně chodí. '
          'V katalogu převažují silniční běžecké boty, například Clifton, Bondi, Mach, Rincon a Arahi, a trailové modely Speedgoat, Challenger, Mafate Speed, Torrent nebo Stinson. Doplňují je turistické boty Anacapa a Kaha, vycházková obuv Transport a pantofle Ora. '
          'Sporteka.cz zde porovnává nabídky českých obchodů, abyste viděli, kde je konkrétní model, generace a velikost skladem. Nákup dokončíte v e-shopu, který si vyberete. Protože Hoka modely často obnovuje, v nabídce se potkává aktuální generace s doprodejem starší, a porovnání tak může ušetřit peníze. '
          'Níže je průvodce historií značky, jednotlivými modely a tím, jak vybrat velikost a srovnávat nabídky.</p>',
    guide='<h2>Historie značky Hoka</h2>'
          '<p>Hoka založili v roce 2009 v Annecy Nicolas Mermoud a Jean-Luc Diard, dva bývalí zaměstnanci firmy Salomon. Chtěli boty, ve kterých by se dalo rychleji a s menší námahou běhat z kopce. Řešením byla výrazně vyšší mezipodešev s velkým objemem pěny a zaobleným tvarem podrážky. Původní jméno Hoka One One vychází z maorského výrazu, který se volně překládá jako létat nad zemí.</p>'
          '<p>Brzy po založení značku koupila americká skupina Deckers, do které patří také '
          + B(('ugg', 'UGG')) +
          '. Na konci roku 2021 se jméno zkrátilo na Hoka. Vývojové pracoviště má firma dál v Annecy. Trailový model Speedgoat nese přezdívku amerického ultramaratonce Karla Meltzera.</p>'
          '<h2>Co v katalogu převažuje</h2>'
          '<p>Nejvíc je <a href="/silnicni-bezecke-boty/">silničních běžeckých bot</a>, těsně za nimi <a href="/trailove-boty/">trailové boty</a>; obě skupiny shrnuje stránka <a href="/bezecke-boty-hoka/">běžecké boty Hoka</a>. Část modelů obchody řadí mezi <a href="/tenisky/">tenisky</a>, protože se nosí i na běžnou chůzi. Dále jsou v nabídce turistické boty v kategorii <a href="/trekova-obuv/">treková obuv</a> a pantofle Ora mezi <a href="/pantofle-a-zabky/">pantoflemi</a>.</p>'
          + '<div class="tw"><table class="ct"><thead><tr><th>Model</th><th>Typ</th><th>Pro koho</th></tr></thead><tbody>'
          '<tr><td>Clifton</td><td>silniční, měkká, univerzální</td><td>každodenní tréninky</td></tr>'
          '<tr><td>Bondi</td><td>silniční, nejvíce tlumení</td><td>dlouhé pomalé běhy, chůze</td></tr>'
          '<tr><td>Mach, Rincon</td><td>silniční, lehčí a svižnější</td><td>rychlejší tréninky, tempo</td></tr>'
          '<tr><td>Arahi, Gaviota</td><td>silniční se stabilizací</td><td>běžci, jimž se noha stáčí dovnitř</td></tr>'
          '<tr><td>Challenger</td><td>silnice i lehký terén</td><td>kombinace asfaltu a cest</td></tr>'
          '<tr><td>Speedgoat, Mafate Speed</td><td>trailové s hrubým vzorkem</td><td>hory, kamení, bláto</td></tr>'
          '<tr><td>Torrent, Stinson</td><td>trailové, lehčí / více tlumení</td><td>rychlé traily / dlouhé vzdálenosti</td></tr>'
          '<tr><td>Anacapa, Kaha</td><td>turistické boty</td><td>túry s batohem</td></tr>'
          '</tbody></table></div>'
          '<h2>Silniční modely</h2>'
          '<p>Clifton je nejčastějším modelem v nabídce a pro mnoho lidí první Hoka. Má měkké tlumení a nízkou hmotnost na takto vysokou botu, a hodí se proto na většinu tréninků. Bondi přidává ještě více pěny a je vhodný na dlouhé pomalé běhy i na celodenní chůzi, například pro lidi, kteří v práci stojí. Mach a Rincon jsou lehčí a svižnější, vhodné na rychlejší tréninky. Arahi a Gaviota mají stabilizační prvky v mezipodešvi a hodí se pro běžce, jejichž chodidlo se při dopadu výrazně stáčí dovnitř. Pro výběr podle pohlaví pomohou přehledy <a href="/damske-silnicni-bezecke-boty/">dámské silniční boty</a> a <a href="/panske-bezecke-boty/">pánské běžecké boty</a>.</p>'
          '<h2>Trailové modely</h2>'
          '<p>Speedgoat patří k nejznámějším trailovým botám vůbec. Má hrubý vzorek podrážky, který drží na kamení, kořenech i v blátě, a dostatek tlumení na dlouhé horské běhy. Mafate Speed je robustnější s velkým objemem pěny, Torrent lehčí s nižší mezipodešví pro rychlé běhy, kde chcete cítit terén. Stinson nabízí maximální tlumení pro ultra vzdálenosti. Challenger je hybridní bota na kombinaci asfaltu a zpevněných cest, ideální, pokud vybíháte z města do lesa. Modely s označením GTX mají membránu Gore-Tex; v blátě a na sněhu ji oceníte, v létě v ní může být teplo.</p>'
          '<h2>Turistická a vycházková obuv</h2>'
          '<p>Anacapa je turistická bota s vysokým tlumením v nízké i kotníkové verzi, Kaha robustnější kotníková bota na delší túry s batohem, ve verzi Frost i do zimy. Transport je vycházková bota na každý den a dojíždění do práce. Pantofle Ora Recovery Slide jsou měkké nazouváky, které se nosí po běhu nebo doma. Jde o obyčejnou obuv, nikoli o zdravotnický prostředek. Na turistiku v horách s těžkým batohem zvažte i klasičtější <a href="/nizke-trekove-boty/">nízké trekové boty</a> s tužší podešví.</p>'
          '<h2>Proč je bota tak vysoká</h2>'
          '<p>Vysoká mezipodešev u Hoka neslouží k tomu, aby byl běžec vyšší, ale aby bylo pod chodidlem dost pěny na tlumení. Podrážka je navíc zaoblená do tvaru kolébky, kterou Hoka nazývá Meta-Rocker, a bota se tak při kroku přirozeně převaluje z paty na špičku. Mnoho běžců to vnímá jako pohodlné na dlouhých tratích. Někomu ale vysoká bota nesedí, protože má menší pocit kontaktu se zemí a na nerovném terénu může působit méně stabilně. Tlumení je věc pocitu a stylu běhu, nikoli léčba. Pokud máte bolesti kloubů, zad nebo se zotavujete ze zranění, poraďte se s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Hoka uvádí velikosti v amerických číslech a obchody je převádějí na evropská a britská, často s polovičními čísly. Změřte délku chodidla v centimetrech večer, kdy je noha nejdelší, a přidejte zhruba půl až jeden centimetr rezervy na prsty. Při běhu z kopce se noha v botě posouvá dopředu a těsná bota tlačí na nehty. Vybrané modely, například Clifton nebo Bondi, existují i v širší verzi označené Wide. Zkoušejte boty s běžeckými <a href="/sportovni-ponozky/">ponožkami</a>, ve kterých budete běhat.</p>'
          '<h2>Generace modelů</h2>'
          '<p>Model si po čase opotřebení vyměňte: pěna v mezipodešvi postupně ztrácí pružnost, i když svršek vypadá jako nový. Jasným znakem je prošlapaný vzorek podrážky nebo nerovnoměrně stlačená pata. Hoka modely pravidelně obnovuje a číslo v názvu označuje generaci, například Clifton 10 a Clifton 11 nebo Speedgoat 6 a Speedgoat 7. Mezi generacemi se může změnit pěna, výška mezipodešve, svršek i střih. Pokud jste byli spokojení se starší verzí, porovnejte parametry nové a zvažte, zda nevyužít doprodej té původní, která bývá levnější. Výjimkou jsou reedice, třeba Speedgoat 2, které vracejí starší podobu modelu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupovat boty těsně na délku. Na delším běhu noha oteče a prsty narážejí do špičky.</li>'
          '<li>Brát trailovou botu na asfalt; hrubý vzorek se na silnici rychle ochodí.</li>'
          '<li>Volit model jen podle barvy, a ne podle tratí, které běháte.</li>'
          '<li>Přejít z nízké minimalistické boty na vysoké tlumení ze dne na den bez postupného zvykání.</li>'
          '<li>Kupovat verzi GTX na letní běhání, kdy se v ní noha zbytečně potí.</li></ul>'
          '<h2>Výbava k botám</h2>'
          '<p>Na delší běhy v terénu se hodí <a href="/bezecke-vesty-a-batohy/">běžecká vesta</a> s měkkými lahvemi, do které uložíte pití, bundu a telefon. Tempo, vzdálenost a převýšení pomůže sledovat <a href="/sportovni-hodinky/">sportovní hodinky</a>. Ponožky volte z funkčního materiálu bez silných švů a v délce, která chrání kotník před odřením. Pokud běháte za tmy, vybavte se reflexními prvky nebo čelovkou. Boty, vesta i ponožky by si měly navzájem sednout, proto je vyzkoušejte na kratším běhu dřív, než s nimi vyrazíte na závod.</p>'
          '<h2>Péče o běžecké boty</h2>'
          '<ul><li>Bláto a prach otřete vlhkým hadříkem nebo měkkým kartáčem.</li>'
          '<li>Do pračky boty nedávejte, pěna i lepení podrážky trpí teplem a mechanickým namáháním.</li>'
          '<li>Mokré boty vycpěte papírem a sušte při pokojové teplotě, ne na topení.</li>'
          '<li>Vložky vyjměte a vysušte zvlášť.</li>'
          '<li>Sledujte opotřebení vzorku a stlačení pěny; ochozená bota už tolik netlumí.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Obchody přebírají názvy z různých jazyků, takže u stejné boty se objeví francouzské Chaussures de running, anglické Running Shoes nebo jen kód modelu. Hledejte podle jména a čísla generace a kontrolujte, zda jde o pánskou, nebo dámskou verzi a zda nejde o širší Wide či verzi GTX. Barvy mají výrobcem dané anglické názvy, které obchody překládají různě. Starší generace a méně oblíbené barvy zlevňují, když přijde nová verze modelu.</p>'
          '<h2>Hoka a podobné značky</h2>'
          '<p>Běžecké boty s výrazným tlumením vyrábějí i '
          + B(('on', 'On'), ('asics', 'Asics'), ('saucony', 'Saucony'), ('new-balance', 'New Balance')) +
          '. V trailovém běhu je Hoka častým soupeřem bot '
          + B(('salomon', 'Salomon')) +
          '. Zajímá-li vás bota s nulovým převýšením a širokou špičkou, podívejte se na <a href="/altra-bezecke-boty/">boty Altra</a>. Pro kompletní výběr běžecké výbavy slouží kategorie <a href="/beh/">běh</a>.</p>',
    faq=[
        ('Odkud pochází značka Hoka?',
         'Z francouzského Annecy. Založili ji v roce 2009 Nicolas Mermoud a Jean-Luc Diard, bývalí zaměstnanci Salomonu. Dnes patří americké skupině Deckers.'),
        ('Co znamená název Hoka?',
         'Vychází z maorského výrazu, který se volně překládá jako létat nad zemí. Do roku 2021 se značka jmenovala Hoka One One.'),
        ('Jaký je rozdíl mezi Clifton a Bondi?',
         'Clifton je lehčí univerzální silniční bota. Bondi má ještě více tlumení a hodí se na dlouhé pomalé běhy a chůzi.'),
        ('Která Hoka je nejlepší do terénu?',
         'Záleží na terénu. Speedgoat a Mafate Speed jsou na hory a bláto, Torrent na rychlé traily, Challenger na kombinaci asfaltu a cest.'),
        ('Co znamená GTX v názvu?',
         'Bota má membránu Gore-Tex, která brání průniku vody. V létě je ale teplejší než verze bez membrány.'),
        ('Jak vybrat velikost bot Hoka?',
         'Podle délky chodidla v centimetrech s rezervou zhruba půl až jeden centimetr. Některé modely jsou i v širší verzi Wide.'),
        ('Jsou boty Hoka vhodné na chůzi?',
         'Ano, řada lidí nosí Clifton nebo Bondi na celodenní chůzi. Na chůzi i do města je určen také model Transport, na túry s batohem turistické boty Anacapa a Kaha.'),
        ('Pomohou boty Hoka při bolesti kloubů?',
         'Boty nejsou zdravotnický prostředek a tlumení je věc pocitu. Při bolestech nebo po zranění se poraďte s lékařem či fyzioterapeutem.'),
        ('Proč se liší čísla jako Clifton 10 a Clifton 11?',
         'Číslo označuje generaci modelu. Nové generace mohou mít jinou pěnu, svršek i střih, starší bývají ve výprodeji.'),
        ('Prodává sporteka.cz boty Hoka?',
         'Ne. Sporteka srovnává nabídky českých obchodů a odkáže vás do e-shopu, kde nákup dokončíte za jeho podmínek dopravy, výměny a vrácení.'),
    ],
)
