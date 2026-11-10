"""sporteka.cz — texts of wave 1, part A: footwear (3. 11. 2026). Merged into src/texts/kategorie.json by texty-export.py.

Every entry: title (≤ 60), desc (≤ 155), intro (above the listing, 120–180 words), guide (HTML below the listing, 600+ words),
faq [(question, answer)] (≥ 5). Facts stay general and true; no prices, no superlatives, no invented statistics.
Questions come from the Marketing Miner suggestions and the long-tail phrases of kw-all.json (3. 11. 2026)."""


def T(head, rows):
    """Table in the style of the listing tables (.tw .ct)."""
    h = ''.join(f'<th>{c}</th>' for c in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tw"><table class="ct"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


NEW = {}

NEW['sportovni-obuv'] = dict(
    title='Sportovní obuv – porovnání cen bot v e-shopech | Sporteka',
    desc='Sportovní obuv pánská, dámská i dětská: běžecké, trekové, tréninkové boty a tenisky. Porovnejte ceny a velikosti skladem napříč českými obchody.',
    intro='<p><strong>Sportovní obuv</strong> není jedna kategorie, ale několik různých nástrojů. Běžecká bota je odpružená a lehká, <a href="/trekova-obuv/">trekové boty</a> drží kotník a chrání před kameny, '
          '<a href="/treninkova-obuv/">tréninková obuv</a> má plochou a stabilní podrážku a <a href="/tenisky/">tenisky</a> se nosí hlavně na každý den. Proto je nejdřív potřeba vědět, co v botách budete dělat.</p>'
          '<p>Na Sportece vedle sebe vidíte nabídky českých sportovních obchodů k téže botě: cenu, velikosti, které má obchod právě skladem, a slevu. Zúžit výběr můžete podle pohlaví, značky, velikosti a ceny. '
          'Pokud hledáte konkrétní disciplínu, otevřete rovnou <a href="/bezecka-obuv/">běžecké boty</a>, <a href="/kopacky/">kopačky</a> nebo <a href="/sandaly/">sandály</a>.</p>',
    guide='<h2>Jak vybrat sportovní obuv</h2>'
          '<p>Nejčastější chyba při koupi je výběr podle vzhledu nebo slevy. Bota určená pro jiný sport vás pak tlačí, klouže, nebo se rychle zničí. Nejdřív si odpovězte na tři otázky: <strong>na jakém povrchu</strong> '
          'budete chodit nebo běhat, <strong>jak často</strong> a <strong>v jakém počasí</strong>. Teprve potom řešte značku a barvu.</p>'
          '<h3>Typ obuvi podle sportu</h3>'
          '<ul><li><strong>Běh po silnici:</strong> lehká bota s odpružením a hladší podrážkou, viz <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>.</li>'
          '<li><strong>Běh v terénu:</strong> hrubší vzorek podrážky a pevnější špička, viz <a href="/trailove-boty/">trailové boty</a>.</li>'
          '<li><strong>Turistika:</strong> pevná podrážka a opora kotníku, u delších tras s membránou, viz <a href="/trekova-obuv/">trekové boty</a>.</li>'
          '<li><strong>Posilovna a kondiční kurzy:</strong> plošší, stabilnější podrážka, viz <a href="/treninkova-obuv/">tréninková obuv</a>.</li>'
          '<li><strong>Míčové sporty:</strong> <a href="/kopacky/">kopačky</a>, <a href="/basketbalova-obuv/">basketbalová obuv</a>, <a href="/salova-obuv/">sálová obuv</a> a <a href="/tenisova-obuv/">tenisová obuv</a> mají podrážku přesně na svůj povrch.</li>'
          '<li><strong>Každodenní nošení:</strong> <a href="/tenisky/">tenisky</a>, případně <a href="/barefoot-obuv/">barefoot obuv</a> pro ty, kdo chtějí přirozený došlap.</li></ul>'
          '<h3>Velikost a střih</h3>'
          '<p>Chodidlo měřte večer, kdy je nejširší, a před špičkou nechte rezervu zhruba 0,5 až 1 cm. U běhu a turistiky se počítá s větší rezervou, protože noha při zátěži mírně otéká a prsty se v klesání posouvají dopředu. '
          'Každá značka střihá jinak, proto vždy sáhněte po její velikostní tabulce, ne jen po čísle ze staré boty. Širší chodidlo ocení modely s širší špičkou nebo označením pro širší nohu.</p>'
          + T(['Délka chodidla', 'Orientační velikost EU'], [['24 cm', '38'], ['25 cm', '40'], ['26 cm', '41'], ['27 cm', '43'], ['28 cm', '44'], ['29 cm', '46']]) +
          '<p>Hodnoty jsou jen orientační a u konkrétních značek se liší o půl až jednu velikost.</p>'
          '<h3>Podrážka, odpružení a materiál</h3>'
          '<p>Měkčí mezipodešev tlumí nárazy a hodí se těžším běžcům a delším tratím, tvrdší a tenčí dává lepší cit pro zem a rychlost. Síťovina je prodyšná a v létě příjemná. Membrána (GORE-TEX a podobné) drží vodu venku, '
          'ale hůř odvádí pot, takže se vyplatí hlavně na podzim, v zimě a v horách. Zimní boty mají navíc zateplení a podrážku s lepší přilnavostí na sněhu.</p>'
          '<h3>Kdy boty vyměnit</h3>'
          '<p>Běžecké boty vydrží obvykle 600 až 800 km, podle váhy, povrchu a stylu běhu i méně. Vyměnit je čas, když mezipodešev ztvrdne a nevrací tvar, podrážka se nerovnoměrně sjede nebo vás bolí klouby, které dřív bolet nezačínaly. '
          'Turistická obuv vydrží déle, ale podrážka a lepení stárnou i bez nošení.</p>'
          '<h3>Jak využít porovnání cen</h3>'
          '<p>Stejná bota stojí v různých obchodech různě a liší se i dostupné velikosti. U každého produktu proto vidíte všechny obchody najednou. Při slevě sledujte, kolik velikostí zbývá, a po doručení vždy zkuste boty doma na čistém povrchu. '
          'Obchody běžně přijímají vrácení do 14 dnů, podmínky ale ověřte v konkrétním e-shopu.</p>',
    faq=[('Jak vybrat správnou velikost sportovní obuvi?', 'Změřte délku chodidla večer a přičtěte 0,5 až 1 cm rezervy. U běhu a turistiky počítejte s rezervou spíš větší. Řiďte se velikostní tabulkou výrobce, protože značky střihají odlišně.'),
         ('Jaký je rozdíl mezi běžeckou a tréninkovou obuví?', 'Běžecká bota je odpružená a navržená pro pohyb dopředu. Tréninková má plošší a stabilnější podrážku, která lépe drží při bočních pohybech a zvedání činek.'),
         ('Musí mít turistická obuv membránu?', 'Nemusí. Membrána pomáhá v dešti a ve sněhu, ale v horku se v ní noha víc potí. Na letní výlety v suchu stačí prodyšná bota bez membrány.'),
         ('Kdy se vyplatí kupovat sportovní boty se slevou?', 'Dobře fungují modely z minulé sezóny, které se liší hlavně barvou. Zkontrolujte, zda jsou ještě skladem vaše velikost a šíře, a porovnejte cenu v několika obchodech.'),
         ('Je lepší koupit boty o číslo větší?', 'Ne vždy. Příliš velká bota se při běhu a chůzi posouvá a způsobuje puchýře. Vhodná je rezerva 0,5 až 1 cm před prsty, ne větší.'),
         ('Jak poznám, že je bota určená na můj sport?', 'Podívejte se na popis výrobce a na podrážku. Hladká a odpružená je na silnici, hrubý vzorek patří do terénu, plochá a široká do posilovny, specifická kolíková nebo sálová podrážka k míčovým sportům.')],
)

NEW['tenisky'] = dict(
    title='Tenisky – porovnání cen pánských a dámských | Sporteka',
    desc='Tenisky pánské, dámské i dětské od značek jako Adidas, Nike nebo Puma. Porovnejte ceny, slevy a velikosti skladem v českých obchodech.',
    intro='<p><strong>Tenisky</strong> jsou obuv na každý den, která vzešla ze sportovní. Dnes se nosí do města, do školy i na procházky a vedle klasických bílých modelů najdete retro střihy, platformy i lehké kožené boty. '
          'Pokud chcete boty přímo na sport, podívejte se spíš na <a href="/bezecka-obuv/">běžecké boty</a> nebo <a href="/treninkova-obuv/">tréninkovou obuv</a>, tenisky na ně nestačí.</p>'
          '<p>Na Sportece najdete tenisky z českých obchodů s porovnáním ceny, slevy a skladových velikostí. Výběr zúžíte podle značky, velikosti a ceny. U oblíbených modelů, například Adidas Stan Smith, vidíte nabídky '
          'všech obchodů vedle sebe, takže poznáte, kde se vyplatí koupit.</p>',
    guide='<h2>Jak vybrat tenisky</h2>'
          '<p>Tenisky vybíráte podle toho, jak a kde je budete nosit. Pro denní chůzi po městě záleží na pohodlí a tlumení, pro příležitostné nošení spíš na vzhledu a kombinovatelnosti s oblečením. '
          'Koupě podle módy je v pořádku, jen počítejte s tím, že tenisky nejsou určené pro dlouhý běh ani turistiku.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Kůže:</strong> udrží tvar, snadno se otírá a vydrží déle, ale je těžší a hůř prodyšná. Kvalitní kůže se časem rozchodí.</li>'
          '<li><strong>Textil a síťovina:</strong> lehké a prodyšné, vhodné do tepla. Hůř se čistí a méně odolávají vodě.</li>'
          '<li><strong>Semiš a nubuk:</strong> působí elegantně, ale špatně snášejí mokro a skvrny a chtějí impregnaci.</li>'
          '<li><strong>Syntetika:</strong> bývá levnější a lehčí, rychle se čistí, ale hůř dýchá.</li></ul>'
          '<h3>Podrážka a tlumení</h3>'
          '<p>Plochá gumová podrážka je typická pro klasické modely a dává stabilní došlap. Tenisky s pěnovou mezipodešvou jsou měkčí a hodí se na celodenní chůzi. Platformová podrážka přidává výšku, ale zhoršuje stabilitu. '
          'Pokud po bytě nebo městě chodíte hodně, zvažte model s odpružením, který se nosí podobně jako lehká běžecká obuv.</p>'
          '<h3>Velikost</h3>'
          '<p>Tenisky mívají odlišné střihy: některé jsou úzké a malé, jiné velké a volné. Ověřte si délku chodidla a porovnejte ji s tabulkou značky. U kožených modelů počítejte s tím, že se rozchodí. '
          'V nabídce vidíte, které velikosti obchod právě drží, takže se nestane, že vyberete boty, které v číslu, co potřebujete, nejsou.</p>'
          '<h3>Čištění a údržba</h3>'
          '<p>Bílé tenisky se čistí jemným čisticím prostředkem, vlažnou vodou a měkkým kartáčkem. Tkaničky a vložky vyndejte a vyperte zvlášť. Kožené boty po vyčištění setřete do sucha a potřete přípravkem pro kůži, '
          'semišové čistěte suchým kartáčkem nebo gumou. Tenisky nesušte na topení ani na slunci, guma a lepení se tím poškodí. Do pračky patří jen ty, které to povoluje výrobce, a na šetrný program bez ždímání.</p>'
          '<h3>Jak vybírat podle účelu</h3>'
          '<p>Na kancelář a město sáhněte po minimalistickém modelu v neutrální barvě, na pěší výlety po zpevněných cestách po botě s odpružením a pevnější podrážkou. '
          'Pokud plánujete i lehký trénink, hledejte v kategorii <a href="/treninkova-obuv/">tréninková obuv</a>. Ceny se u stejného modelu v obchodech liší, proto se vyplatí srovnat nabídky.</p>',
    faq=[('Jak vyčistit bílé tenisky?', 'Vyndejte tkaničky a vložky, povrch otřete kartáčkem s vlažnou vodou a jemným čisticím prostředkem a pak setřete do sucha. Neperte je horkou vodou a nesušte na topení.'),
         ('Mohu tenisky prát v pračce?', 'Pouze pokud to výrobce povoluje. Použijte šetrný program do 30 °C, bez ždímání, nejlépe v pytlíku na praní. Kožené a semišové boty do pračky nepatří.'),
         ('Jsou tenisky vhodné na běhání?', 'Na delší běh ne. Běžecká obuv má odpružení a tvar určený pro pohyb dopředu. Tenisky jsou určené pro chůzi, krátké úseky a každodenní nošení.'),
         ('Jaké tenisky nosit k šatům nebo sukni?', 'Dobře fungují bílé nebo světlé kožené tenisky v nízkém střihu. Barvu volte podle zbytku outfitu a drobné vzory raději neskládejte.'),
         ('Jak poznám správnou velikost tenisek?', 'Změřte chodidlo večer, přidejte asi 0,5 až 1 cm a porovnejte s velikostní tabulkou značky. Střihy se liší, takže u jiné značky může sedět jiné číslo.'),
         ('Jak dlouho tenisky vydrží?', 'Při každodenním nošení zhruba jeden až dva roky. Delší životnost mají kožené modely, rychleji se opotřebují lehké textilní s tenkou podrážkou.')],
)

NEW['bezecka-obuv'] = dict(
    title='Běžecké boty – porovnání cen silniční i trail | Sporteka',
    desc='Běžecké boty pánské a dámské na silnici i do terénu. Porovnejte ceny, slevy a velikosti skladem u českých sportovních obchodů a vyberte správný model.',
    intro='<p><strong>Běžecké boty</strong> poznáte podle toho, že při běhu vnímáte nohy co nejméně. Rozhoduje povrch, váha, délka tratí a způsob došlapu. Na asfalt jsou nejlepší <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, '
          'v lese a na kamenech se osvědčí <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<p>V nabídce Sportek porovnáte ceny běžecké obuvi z českých obchodů a vidíte, které velikosti jsou skladem. Hledáte-li něco na rychlé tréninky a závody, zaměřte se na lehčí, pružnější modely. Pro začátečníky a delší běhy je lepší měkčí odpružení. '
          'Všechny pánské, dámské i dětské boty se dají filtrovat podle značky a ceny.</p>',
    guide='<h2>Jak vybrat běžecké boty</h2>'
          '<p>Správná bota ušetří klouby a zvyšuje chuť běhat. Nejdřív určete, kde poběžíte nejčastěji. Pokud budete střídat povrchy, vezměte univerzální model, nebo si pořiďte dva páry: silniční a trailový.</p>'
          '<h3>Silnice nebo terén</h3>'
          '<ul><li><strong>Silniční boty:</strong> hladká podrážka, více odpružení, nižší hmotnost. Nejsou vhodné na bahno a mokré kořeny.</li>'
          '<li><strong>Trailové boty:</strong> hrubý vzorek, pevnější špička a boky, často tužší mezipodešev. Na asfaltu se rychleji sjedou a bývají tvrdší.</li>'
          '<li><strong>Univerzální boty:</strong> kompromis pro chodníky, parky a lehčí terén. Pro rekreační běžce často stačí.</li></ul>'
          '<h3>Odpružení a hmotnost</h3>'
          '<p>Těžší běžci a delší tratě ocení měkčí mezipodešev. Lehčí a pružnější bota se hodí na rychlé tréninky a závody, ale víc zatěžuje nohy. Rozdíl výšky paty a špičky (drop) bývá od 0 do 12 mm. '
          'Nižší drop zatěžuje víc lýtka a Achillovku, vyšší chrání kolena. Pokud jste zvyklí na vyšší drop, změnu dělejte postupně.</p>'
          '<h3>Pronace a stabilita</h3>'
          '<p>Pokud se vám kotník při došlapu výrazně propadá dovnitř, zkuste stabilnější model. Většina rekreačních běžců si vystačí s neutrální botou. Rozbor došlapu nabízí řada běžeckých obchodů a stojí za to, '
          'pokud vás bolí kolena nebo holeně.</p>'
          '<h3>Velikost</h3>'
          '<p>Před palcem mějte zhruba centimetr rezervy, pata nesmí vyklouzávat. Při delším běhu noha otéká, proto zkoušejte boty odpoledne nebo večer. Ověřte si i šířku: úzká špička tlačí a způsobuje puchýře. '
          'Při výběru na internetu využijte možnost vrácení a vyzkoušejte boty doma na koberci.</p>'
          + T(['Typ běhu', 'Na co se zaměřit'], [['Krátké rychlé tréninky', 'nižší hmotnost, pružná mezipodešev'], ['Dlouhé pomalé běhy', 'měkčí odpružení, širší špička'], ['Terén a bahno', 'hluboký vzorek, ochrana špičky'], ['Zimní běh', 'membrána nebo zateplení, hrubší podrážka']]) +
          '<h3>Kdy vyměnit běžecké boty</h3>'
          '<p>Obvykle po 600 až 800 km. Znamením je ztvrdlá mezipodešev, nerovnoměrně sjetá podrážka a bolest kloubů, která dřív nebyla. Boty střídejte: dva páry dávají pěně čas vrátit tvar a obvykle déle vydrží.</p>',
    faq=[('Jak vybrat běžecké boty?', 'Určete povrch (silnice, terén), svou váhu a délku tratí. Těžším běžcům a dlouhým tratím sedí měkčí odpružení, na rychlé tréninky lehčí a pružnější bota. Rezerva před prsty je asi 1 cm.'),
         ('Potřebuji speciální boty na trail?', 'Na lesní a kamenité cesty ano. Hrubší vzorek podrážky lépe drží na bahně a mokrých kořenech a výztuž špičky chrání prsty před kameny.'),
         ('Kolik kilometrů vydrží běžecké boty?', 'Obvykle 600 až 800 km. Podle váhy, povrchu a stylu běhu se životnost liší. Boty střídejte, vydrží déle.'),
         ('Jak poznám, jestli mám boty správně velké?', 'Při došlapu nesmí palec narážet na špičku a pata nesmí vyklouzávat. Rezerva asi 1 cm před prsty je běžná, protože noha při běhu otéká.'),
         ('Hodí se běžecké boty na chůzi a do města?', 'Ano, jsou pohodlné i na denní chůzi. Jen se rychleji sjedou, pokud je používáte všude.'),
         ('Jak vybrat dámské běžecké boty?', 'Dámské modely bývají užší a mají jinak tvarovanou patu a lehčí odpružení. Pokud vám sedí unisex nebo pánský střih, dámská verze není nutnost.')],
)

NEW['trailove-boty'] = dict(
    title='Trailové boty – porovnání cen do terénu | Sporteka',
    desc='Trailové běžecké boty pánské i dámské s hrubým vzorkem pro terén, bahno a kameny. Porovnejte ceny a velikosti skladem v českých obchodech.',
    intro='<p><strong>Trailové boty</strong> jsou běžecká obuv do lesa, na louky, kamenité cesty a do hor. Oproti silničním mají hrubší vzorek podrážky, pevnější špičku a často tužší konstrukci, '
          'která chrání chodidlo před kameny a kořeny. Pokud běháte hlavně po asfaltu, vyberte raději <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>.</p>'
          '<p>Ve Sportece uvidíte trailové boty od českých obchodů vedle sebe: pánské, dámské i dětské, s cenou, slevou a skladovými velikostmi. '
          'Filtry zúží výběr podle značky, velikosti a ceny. Celý přehled běžecké obuvi najdete v kategorii <a href="/bezecka-obuv/">běžecké boty</a>.</p>',
    guide='<h2>Jak vybrat trailové boty</h2>'
          '<p>Trailová bota musí držet na různých površích a chránit nohu. Při výběru sledujte vzorek podrážky, tuhost, ochranu špičky a prodyšnost nebo vodoodolnost. Podle trasy se doporučení liší.</p>'
          '<h3>Vzorek podrážky</h3>'
          '<ul><li><strong>Hluboké hrbolky (zhruba 5 mm a víc):</strong> bahno, tráva, sníh. Na tvrdém povrchu se rychleji sjedou.</li>'
          '<li><strong>Střední vzorek:</strong> smíšené trasy, lesní cesty, pěšiny. Nejuniverzálnější volba.</li>'
          '<li><strong>Nízký vzorek:</strong> udusané cesty a mírný terén, kde se střídá asfalt a les.</li></ul>'
          '<h3>Ochrana a tuhost</h3>'
          '<p>Gumová ochrana špičky chrání před nárazem do kamene. Skalní destička v podrážce zabraňuje bolesti od ostrých kamenů, ale snižuje cit a přidává hmotnost. Boty na dlouhé horské trasy mívají pevnější konstrukci, '
          'na rychlé lesní běhy se hodí lehčí a ohebnější.</p>'
          '<h3>Membrána, nebo prodyšnost</h3>'
          '<p>Membrána (například GORE-TEX) drží vodu venku, ale v horku se noha víc potí a boty se po promočení hůř suší. Na letní trasy a časté brody se osvědčují prodyšné modely bez membrány. '
          'Na podzim, na jaře a v zimě má membrána smysl, v kombinaci s vyšším zateplením nohy.</p>'
          '<h3>Velikost</h3>'
          '<p>V klesání prsty narážejí na špičku, proto zvolte rezervu asi jeden centimetr, u dlouhých tratí spíš o něco víc. Pata musí sedět pevně. '
          'Při zkoušení stupňujte zátěž: v obchodě si zkuste seběhnout schody nebo šikmou plochu.</p>'
          '<h3>Péče</h3>'
          '<p>Po terénu boty vyklepejte, očistěte kartáčem a sušte při pokojové teplotě. Nikdy je nedávejte na topení nebo do blízkosti ohně, lepení a pěna se zničí. Na dlouhou životnost střídejte dva páry.</p>',
    faq=[('Co jsou trailové boty?', 'Běžecká obuv pro terén. Má hrubší vzorek podrážky, pevnější špičku a konstrukci, která chrání nohu před kameny, kořeny a bahnem.'),
         ('Mohu v trailových botách běhat po asfaltu?', 'Ano, ale podrážka se rychleji sjede a bota bývá tvrdší než silniční. Na pravidelný běh po silnici je lepší silniční model.'),
         ('Mají mít trailové boty membránu?', 'Záleží na podmínkách. V dešti a ve sněhu se membrána hodí, v létě a při častých brodech je lepší prodyšná bota bez ní.'),
         ('Jaká velikost trailových bot je správná?', 'Přibližně o centimetr delší než chodidlo, aby prsty v klesání nenarážely na špičku. Pata musí držet a nesmí vyklouzávat.'),
         ('Jak se starat o trailové boty?', 'Po běhu je vyklepejte, očistěte kartáčem a sušte při pokojové teplotě. Nesušte je na topení a nepoužívejte pračku.'),
         ('Jaký drop mají mít trailové boty?', 'Drop se pohybuje od 0 do zhruba 10 mm. Pokud jste zvyklí na silniční boty s vyšším dropem, přecházejte na nižší postupně, aby se nepřetížila lýtka.')],
)

NEW['trekova-obuv'] = dict(
    title='Trekové boty – porovnání cen pánských a dámských | Sporteka',
    desc='Trekové boty nízké i vysoké, s membránou i bez. Porovnejte ceny pánských, dámských a dětských trekových bot a velikosti skladem v českých obchodech.',
    intro='<p><strong>Trekové boty</strong> jsou obuv na turistiku a pěší výlety. Mají pevnější podrážku, výztuž špičky a paty a u vyšších modelů oporu kotníku. Hodí se od nedělní procházky po náročné horské trasy. '
          'Pokud hledáte lehčí variantu, podívejte se na <a href="/nizke-trekove-boty/">nízké trekové boty</a>, na delší túry s batohem na <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>.</p>'
          '<p>Sporteka porovnává ceny trekové obuvi z českých obchodů. U každého páru uvidíte nabídky vedle sebe, slevu a velikosti skladem. Výběr zúžíte podle pohlaví, značky, velikosti a ceny. '
          'Letní trasy vyžadují jinou obuv než zimní, proto sledujte popis materiálu a membrány.</p>',
    guide='<h2>Jak vybrat trekové boty</h2>'
          '<p>Správné trekové boty mají sedět pevně, držet chodidlo a mít podrážku, která přilne na kamenech i mokré trávě. Rozhodují délka tras, hmotnost batohu, povrch a roční doba.</p>'
          '<h3>Nízké, nebo vysoké</h3>'
          '<ul><li><strong>Nízké boty:</strong> lehké a pohodlné, vhodné na kratší a mírné trasy bez těžkého batohu.</li>'
          '<li><strong>Vysoké boty:</strong> opora kotníku, ochrana před kamením a vodou, lepší s těžším batohem a na nerovném terénu.</li>'
          '<li><strong>Středně vysoké (mid):</strong> kompromis mezi lehkostí a oporou.</li></ul>'
          '<h3>Membrána, nebo prodyšnost</h3>'
          '<p>Boty s membránou jsou voděodolné, ale v horku hůř větrají. Prodyšné bez membrány se hodí na léto a suchá období. Na podzim a v zimě se vyplatí membrána a zateplení. '
          'Pokud často procházíte brody a vlhkou trávou, počítejte s tím, že i membrána má limity.</p>'
          '<h3>Podrážka a tuhost</h3>'
          '<p>Pevná podrážka chrání chodidlo před kameny a nese váhu batohu. Hrubý vzorek zlepšuje přilnavost v terénu. Příliš tuhá bota se ale hůř ohýbá při chůzi po rovině, proto si vybírejte podle terénu: '
          'pro hory pevnější, pro lesní a pěší cesty ohebnější.</p>'
          '<h3>Velikost</h3>'
          '<p>Boty zkoušejte odpoledne s ponožkami, v jakých budete chodit. Prsty mají mít při klesání rezervu asi 1 cm, pata nesmí vyklouzávat. Pokud při šlapání z kopce vaše prsty narážejí na špičku, je bota malá. '
          'Nové boty před dlouhou túrou rozchoďte na kratších trasách.</p>'
          + T(['Trasa', 'Vhodná obuv'], [['Procházky a mírné výlety', 'nízké boty, prodyšný materiál'], ['Celodenní túry s lehkým batohem', 'středně vysoké boty'], ['Vícedenní trek s těžkým batohem', 'vysoké boty, pevná podrážka'], ['Podzim, zima, sníh', 'membrána, zateplení, hrubý vzorek']]) +
          '<h3>Péče o boty</h3>'
          '<p>Po túře boty očistěte, vytáhněte vložky a sušte při pokojové teplotě. Kůži ošetřujte přípravkem, membránové boty podle návodu výrobce. Nepoužívejte topení, hrozí vysušení a odlepení podrážky.</p>',
    faq=[('Jak vybrat trekové boty?', 'Podle délky tras, hmotnosti batohu a ročního období. Nízké se hodí na lehké trasy, vysoké na hory s batohem. Na podzim a v zimě zvolte membránu.'),
         ('Musí mít trekové boty membránu?', 'Nemusí. Membrána drží vodu venku, ale v horku se noha potí víc. Na léto stačí prodyšná bota bez membrány.'),
         ('Jaká velikost trekových bot je správná?', 'Přibližně o 1 cm delší než chodidlo, zkoušená odpoledne s turistickými ponožkami. Pata nesmí vyklouzávat a prsty nesmí narážet na špičku.'),
         ('Mohu v trekových botách chodit i po městě?', 'Ano, ale podrážka se rychleji sjede a bota je tvrdší. Na každodenní nošení je pohodlnější nižší trekový model nebo tenisky.'),
         ('Jak často měnit trekové boty?', 'Záleží na používání, obvykle po stovkách až tisících kilometrů. Vyměnit je čas, když se podrážka sjede, odlepuje nebo bota propouští vodu.'),
         ('Jaké trekové boty na zimu?', 'Zateplené modely s membránou a hrubou podrážkou, případně o číslo větší, aby se vešla tlustší ponožka a zůstal prostor pro oběh krve.')],
)
