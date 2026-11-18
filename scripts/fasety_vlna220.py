"""sporteka.cz — facet landing texts wave 220 (men's facets and one brand facet of wave 32):
panska-cepice, jordan-mikina, panska-mikina-na-zip, panska-nepromokava-bunda (panske-kalhoty and panska-softshellova-bunda were dropped on 18. 11.: they duplicate panske-sportovni-kalhoty and softshellova-bunda-panska).
Assortment described from the live catalogue copy (brands and model names as they appear in product names).
Sources checked: head heat-loss myth traced to 1950s US Army experiments, head roughly 7-10 % of heat loss when the rest of the body
is covered (BMJ 2008 report via Live Science, BBC Science Focus); New Era silhouettes 59FIFTY fitted / 9FIFTY snapback / 39THIRTY
stretch fit / 9FORTY adjustable / 9TWENTY unstructured (neweracap.com silhouette guides), 59FIFTY designed 1954 by Harold Koch and
New Era exclusive on-field cap supplier of MLB from 1993 (National Baseball Hall of Fame "Capping it off"); Jumpman logo debut on Air
Jordan III in 1988 and Jordan Brand launched as a Nike division on 9 September 1997 (Wikipedia Air Jordan / Jumpman); Polartec-style
fleece grades 100 / 200 / 300 by fabric weight (Polartec, Backpacking Light, Bergfreunde); Icebreaker 200 / 260 numbers = fabric
weight in g/m2 (Icebreaker base layer guide, REI); BDU introduced by the US Army on 1 October 1981 and replaced by the ACU from 2004
(army.mil, Wikipedia); Fjällräven G-1000 = 65 % polyester / 35 % cotton, Greenland Wax gives water resistance, not waterproofness
(fjallraven.com); GORE-TEX INFINIUM WINDSTOPPER renamed WINDSTOPPER products by GORE-TEX LABS, windproof and water-repellent, not
waterproof (gore-tex.com); EN 343:2019 rain protection classes 1-4 for water penetration and breathability (class 4 added in 2019),
breathability tested to ISO 11092 (Wenaas, SATRA, Tranemo); RET bands 0-6 / 6-13 / 13-20 vary by source (Wikipedia Breathability,
Decathlon); Helly Hansen founded 1877 in Moss, Norway, linseed-oil oilskins, Helly Tech from 1980 (Encyclopedia.com, Wikipedia);
Regatta Isotex, Columbia Omni-Tech and The North Face DryVent as the brands' own waterproof-breathable technologies (regatta.com,
columbia.com, thenorthface.com).
Left out (not verified): Mammut Ultimate membrane name, Trespass fabric codes, exact cm ranges of fleece weights.
No prices, counts, stock claims, no medical promises."""
from texty_vlna1a import T

NEW = {}

# ------------------------------------------------------------------ panska-cepice
NEW['panska-cepice'] = dict(
    title='Pánská čepice: zimní kulich, kšiltovka i trucker',
    desc='Pánské čepice: pletené kulichy, merino a funkční čepice, kšiltovky New Era, 47 Brand či Mitchell & Ness. Jak vybrat typ, materiál a velikost.',
    intro='<p><strong>Pánská čepice</strong> může být teplý pletený kulich na mrazivé ráno, tenká funkční čepice pod helmu nebo na běh, ale také kšiltovka, kterou muži nosí celý rok. '
          'Na této stránce jsou pánské modely z kategorie <a href="/cepice-a-celenky/">čepice, kšiltovky a čelenky</a> s nabídkami českých obchodů. '
          'Velkou část nabídky tvoří kšiltovky s logy amerických týmů z NFL, NHL, MLB a NBA, vedle nich najdete zimní čepice sportovních a outdoorových značek. '
          'Průvodce níže vysvětluje, jaké typy čepic existují, z čeho se pletou, jak změřit obvod hlavy a co znamenají označení kšiltovek New Era jako 59FIFTY nebo 9FORTY. '
          'Kdo hledá jen kšiltovky, může rovnou přejít na stránku <a href="/panska-ksiltovka/">pánská kšiltovka</a>.</p>',
    guide='<h2>Jaké pánské čepice existují</h2>'
          '<p>Slovo čepice zahrnuje dvě skupiny pokrývek hlavy. Jedna má za úkol hřát, druhá hlavně stínit oči a dotvářet oblečení. Obě se dají nosit při sportu i ve městě, jen každá na jiné počasí.</p>'
          + T(['Typ', 'Kdy se hodí', 'Na co dát pozor'], [
              ['pletený kulich s manžetou', 'zima ve městě, procházky, cesta do práce', 'dvojitá manžeta hřeje víc nad ušima'],
              ['kulich s bambulí', 'zima, hory, sáňkování', 'bambule překáží pod kapucí a helmou'],
              ['tenká funkční čepice', 'běh, běžky, skialpy, pod lyžařskou helmu', 'má odvádět pot, ne jen hřát'],
              ['merino čepice', 'celý den venku, vícedenní výlety', 'jemná vlna nekouše a nepáchne tak rychle'],
              ['kšiltovka', 'jaro až podzim, slunce, každodenní nošení', 'typ zapínání a tvar štítku'],
              ['trucker', 'léto, festival, rybaření', 'síťovaná zadní část dobře větrá']]) +
          '<p>Kdo chce jednu čepici na všechno, obvykle sáhne po středně silném kulichu bez bambule. Vejde se pod kapuci, nevadí pod ní ani širší nákrčník a na rychlou chůzi v mrazu stačí. Na běh a lyže je ale lepší tenký funkční model.</p>'
          '<h2>Proč nosit čepici, i když hlava neztrácí půlku tepla</h2>'
          '<p>Rozšířená poučka, že hlavou uniká skoro polovina tělesného tepla, se vykládá jako fakt, ale pochází z vojenských pokusů z padesátých let minulého století. Lidé v nich měli zabalené tělo a nezakrytou hlavu, takže teplo logicky unikalo hlavně hlavou. '
          'Pozdější rozbor publikovaný v britském lékařském časopise BMJ uvádí, že u oblečeného člověka připadá na nekrytou hlavu zhruba sedm až deset procent tepelných ztrát, tedy přibližně tolik, kolik odpovídá její ploše. '
          'Čepice má přesto smysl. Hlava a uši jsou na chlad citlivé, vítr je rychle prochladí a nepříjemný pocit chladu pak vnímáte po celém těle. Teplý kulich spolu s rukavicemi a nákrčníkem dokáže udělat ze zimní procházky pohodlnou záležitost.</p>'
          '<h2>Z čeho se zimní čepice pletou</h2>'
          '<p><strong>Akryl</strong> je nejčastější materiál pletených kulichů. Je lehký, drží tvar, dá se prát v pračce a nekouše. Hřeje slušně, při pocení ale vlhkost tolik neodvádí. '
          '<strong>Vlna</strong> hřeje i ve chvíli, kdy navlhne, hrubší vlna ale může na čele štípat. Proto mají vlněné čepice často fleecovou podšívku nebo pruh na čele. '
          '<strong>Merino</strong> je jemná ovčí vlna, která na kůži nekouše, dobře reguluje teplotu a pomaleji začne zapáchat. Hodí se na celodenní pobyt venku a na sport, kde se člověk potí. Čepice z jemné vlny najdete v kategorii <a href="/merino-doplnky/">merino čepice, nákrčníky a rukavice</a>. '
          '<strong>Fleece</strong> je měkký polyesterový úplet, rychle schne a dobře hřeje, ale vítr jím prochází. Často slouží jako podšívka pletených čepic. '
          '<strong>Funkční úplety</strong> z polyesteru a elastanu jsou tenké, přiléhavé a odvádějí pot, takže se hodí na běh nebo pod přilbu.</p>'
          '<h2>Jak změřit obvod hlavy</h2>'
          '<p>Krejčovský metr veďte kolem hlavy přibližně centimetr nad obočím a nad ušima, vzadu přes nejvystouplejší místo týla. Metr má přiléhat, ale netlačit. Pletené čepice se většinou prodávají v jedné univerzální velikosti, protože úplet se roztáhne. '
          'U funkčních a značkových čepic se setkáte s velikostmi S/M a L/XL. Kdo má obvod hlavy na hranici dvou velikostí, vezme u pletené čepice spíš menší a u pevné kšiltovky spíš větší.</p>'
          '<h2>Kšiltovky New Era: co znamenají čísla v názvu</h2>'
          '<p>Většinu kšiltovek v této nabídce vyrábí americká firma <a href="/znacka/new-era/">New Era</a>. Názvy jejích střihů jsou čísla psaná slovy a podle nich poznáte tvar i zapínání:</p>'
          + T(['Označení', 'Zapínání', 'Tvar'], [
              ['59FIFTY', 'žádné, pevná velikost (fitted)', 'vysoká tvarovaná přední část, rovný štítek'],
              ['9FIFTY', 'plastový pásek snapback', 'vysoká tvarovaná přední část, rovný štítek'],
              ['39THIRTY', 'uzavřená, pružný pás uvnitř (stretch fit)', 'zahnutý štítek, velikosti typu S/M a L/XL'],
              ['9FORTY', 'nastavitelný pásek vzadu', 'zahnutý štítek'],
              ['9TWENTY', 'pásek s kovovou sponou', 'nízká nevyztužená čepice, zahnutý štítek']]) +
          '<p>Model 59FIFTY navrhl v roce 1954 Harold Koch, syn zakladatele firmy. Od roku 1993 je New Era výhradním dodavatelem čepic, ve kterých hrají hráči americké baseballové ligy MLB. '
          'Velikosti fitted kšiltovek se uvádějí americkými čísly jako 7 1/4 nebo 7 3/8. Číslo zhruba odpovídá průměru hlavy v palcích, takže velikost 7 1/4 sedí na obvod hlavy kolem 58 centimetrů. Ověřte si to v tabulce obchodu, protože se jednotlivé kolekce mohou mírně lišit. '
          'Kdo si velikostí není jistý, zvolí raději 9FORTY nebo 9FIFTY, které se dají nastavit. Podrobný přehled modelů je na stránce <a href="/new-era-ksiltovka/">kšiltovka New Era</a>.</p>'
          '<h2>Týmové čepice a fanouškovské kolekce</h2>'
          '<p>Kromě New Era nabízí čepice s licencovanými logy lig a týmů <a href="/znacka/47-brand/">47 Brand</a>, <a href="/znacka/mitchell-ness/">Mitchell &amp; Ness</a>, <a href="/znacka/fanatics/">Fanatics</a> a American Needle. '
          'Mitchell &amp; Ness je známý retro kšiltovkami s historickými logy týmů. V názvech takových modelů se objevují označení jako Hardwood Classics nebo Vintage. 47 Brand dělá měkčí kšiltovky typu Clean Up a snapbacky MVP. '
          'V nabídce jsou i zimní pletené čepice s logem týmu, často s manžetou a bambulí. Ty se nosí spíš na stadion a do města než na hory, protože jde hlavně o fanouškovské zboží. V názvech uvidíte jména kolekcí jako Sideline, Draft nebo City Connect, které se mění každou sezonu.</p>'
          '<h2>Sportovní a outdoorové čepice</h2>'
          '<p>Zimní čepice na sport mají v nabídce <a href="/znacka/under-armour/">Under Armour</a>, Nike, Adidas a Puma, z outdoorových značek The North Face, Columbia a Hannah. Pletené kulichy s výrazným designem dodávají Barts, Horsefeathers, Meatfly nebo O\'Neill. '
          'Pro hokejisty a fanoušky hokeje jsou tu čepice CCM. Pod lyžařskou nebo cyklistickou přilbu se hodí jen tenká čepice bez bambule a bez silných švů, které by tlačily. Další modely pro zimní sporty najdete v kategorii <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>, kukly pod helmu na stránce <a href="/kukly/">kukly (balaclavy)</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Bambule pod helmou.</strong> Na lyže pod přilbu patří tenká čepice, bambule se pod helmu nevejde a tlačí.</li>'
          '<li><strong>Bavlna na sport.</strong> Bavlněná čepice nasaje pot a pak studí. Na běh a skialpy volte funkční úplet nebo merino.</li>'
          '<li><strong>Fitted kšiltovka bez změření hlavy.</strong> Pevnou velikost nejde povolit. Nejdřív změřte obvod hlavy.</li>'
          '<li><strong>Čepice, která nezakryje uši.</strong> Krátké kulichy posazené vysoko na temeni vypadají dobře, ale v mrazu nechají uši prochladnout.</li></ul>'
          '<h2>Péče o čepice a kšiltovky</h2>'
          '<p>Akrylové kulichy se většinou dají prát v pračce na nízkou teplotu, vlněné a merino čepice raději ručně ve vlažné vodě s prostředkem na vlnu. Sušte je naplocho, na topení se mohou srazit. '
          'Kšiltovky s vyztuženou přední částí do pračky nedávejte, vyztužení se zdeformuje a štítek může prasknout. Skvrny vyčistěte vlhkou houbičkou a trochou jemného mýdla. Pot na pásku uvnitř otřete vlhkým hadříkem a čepici nechte uschnout na hlavě z balonu nebo na sklenici.</p>'
          '<h2>Kšiltovka a slunce</h2>'
          '<p>V létě kšiltovka stíní oči a čelo, takže se při běhu nebo na kole méně mhouříte do slunce. Uši, krk a tváře ale nechává odkryté, proto je na celodenní pobyt na slunci potřeba i opalovací krém. Na túry v horku se hodí lehká kšiltovka z funkčního materiálu, která rychle schne, nebo trucker se síťovanou zadní částí.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Nejdřív si ujasněte, jestli hledáte čepici do zimy, nebo kšiltovku, a u kšiltovek i typ zapínání. Teprve pak má smysl porovnávat barvy a týmová loga. U týmových modelů se stejný název často objevuje v několika barevných verzích. Sporteka ukazuje nabídky českých obchodů vedle sebe, nákup dokončíte u prodejce. '
          'Ke kompletní zimní výbavě patří i <a href="/panske-rukavice/">pánské rukavice</a> a <a href="/nakrcniky-a-satky/">nákrčníky</a>, přehled čepic podle značek je na stránkách <a href="/cepice-nike/">čepice Nike</a>, <a href="/puma-cepice/">čepice Puma</a> a <a href="/the-north-face-cepice/">čepice The North Face</a>.</p>',
    faq=[
        ('Jakou pánskou čepici vybrat na zimu?', 'Do města stačí pletený kulich z akrylu nebo vlny, ideálně s manžetou přes uši. Na hory a celodenní pobyt venku je lepší merino nebo čepice s fleecovou podšívkou.'),
        ('Jakou čepici nosit pod lyžařskou helmu?', 'Tenkou funkční čepici bez bambule a bez silných švů. Silný kulich pod helmu nepatří, helma pak špatně sedí. Většina lyžařských helem má vlastní vnitřní polstrování.'),
        ('Uniká hlavou většina tepla?', 'Ne. Údaj o polovině tepla vznikl při pokusech, kde měli lidé zakryté tělo a volnou hlavu. U oblečeného člověka připadá na hlavu zhruba sedm až deset procent ztrát. Čepice se přesto vyplatí kvůli uším a větru.'),
        ('Jak zjistit velikost čepice?', 'Změřte obvod hlavy metrem asi centimetr nad obočím a nad ušima. Pletené čepice bývají univerzální, funkční a značkové se prodávají ve velikostech S/M a L/XL.'),
        ('Co znamená 59FIFTY?', 'Je to kšiltovka New Era v pevné velikosti, bez pásku vzadu, s vysokou přední částí a rovným štítkem. Velikost se uvádí americkým číslem, třeba 7 1/4.'),
        ('Jaký je rozdíl mezi 9FORTY a 9FIFTY?', '9FORTY má zahnutý štítek, 9FIFTY rovný štítek a vysokou vyztuženou přední část. Obě se dají vzadu nastavit páskem, takže nevyžadují přesnou velikost.'),
        ('Kouše merino čepice?', 'Většinou ne. Merino má jemná vlákna, která na kůži nepíchají. Citlivější lidé mohou vnímat lehké šimrání u silnějších pletenin, pak pomůže čepice s podšívkou.'),
        ('Můžu kšiltovku prát v pračce?', 'Kšiltovky s vyztuženou přední částí raději ne, mohou se zdeformovat. Čistěte je ručně vlhkou houbičkou. Některé měkké modely bez vyztužení výrobce praní povoluje, řiďte se štítkem.'),
        ('Co je trucker čepice?', 'Kšiltovka s pěnovým nebo látkovým předkem a síťovanou zadní částí. Dobře větrá, proto se nosí hlavně v létě. Zapíná se obvykle plastovým páskem.'),
        ('Kde porovnat ceny pánských čepic?', 'Na této stránce jsou nabídky českých e-shopů pohromadě. Vyberete model a nákup dokončíte v obchodě, kde ještě ověříte velikost a barvu.'),
    ])

# ------------------------------------------------------------------ jordan-mikina
NEW['jordan-mikina'] = dict(
    title='Jordan mikina: Brooklyn Fleece, Jumpman, Dri-FIT',
    desc='Mikiny Jordan pánské, dámské i dětské: Brooklyn Fleece, Jumpman, Essentials a tréninkové Dri-FIT. Typy, střihy, velikosti a péče o mikinu.',
    intro='<p><strong>Jordan mikina</strong> patří k oblečení značky, která vznikla kolem basketbalových bot Michaela Jordana a dnes vyrábí celou kolekci od tenisek po tepláky. '
          'Na této stránce jsou mikiny Jordan z kategorie <a href="/mikiny/">mikiny</a> s nabídkami českých obchodů: bavlněné mikiny přes hlavu s kapucí, rozepínací modely na zip, mikiny bez kapuce i lehčí tréninkové mikiny z funkčního materiálu. '
          'Najdete tu pánské, dámské i dětské velikosti. Průvodce vysvětluje, čím se liší řady Brooklyn Fleece, Jumpman, Essentials a Sport, jak vybrat velikost u amerického střihu, jak poznat barevnou variantu podle kódu a jak o mikinu pečovat. '
          'Ke stejnému stylu se hodí <a href="/jordan-teplaky/">tepláky Jordan</a> a <a href="/jordan-ksiltovka/">kšiltovka Jordan</a>.</p>',
    guide='<h2>Odkud se značka Jordan vzala</h2>'
          '<p>Nike začal vyrábět boty Air Jordan pro Michaela Jordana v roce 1985. Silueta skákajícího hráče s míčem, známá jako Jumpman, se poprvé objevila na botě Air Jordan III v roce 1988 a postupně nahradila starší logo s křídly. '
          'V září 1997 Nike představil Jordan jako samostatnou značku v rámci firmy. Od té doby pod ní vychází nejen basketbalové boty, ale i oblečení na hřiště, trénink a volný čas. '
          'V obchodech se proto setkáte s názvy Jordan, Air Jordan i Nike Jordan. Jde o stejnou značku, liší se jen tím, jak ji prodejce v názvu produktu uvede. Přehled celé značky najdete na stránce <a href="/znacka/jordan/">Jordan</a>.</p>'
          '<h2>Řady mikin Jordan v nabídce</h2>'
          + T(['Řada', 'Materiál a charakter', 'Na co'], [
              ['Brooklyn Fleece', 'bavlněná směs s počesaným rubem, mikiny přes hlavu, na zip i bez kapuce', 'každodenní nošení, město'],
              ['Jumpman Fleece', 'teplá mikina s výrazným logem Jumpman', 'volný čas, do školy'],
              ['Essentials', 'jednoduché mikiny s menším logem, přes hlavu i na zip', 'základ šatníku, ke všemu'],
              ['Sport, Sport Crossover', 'funkční úplet Dri-FIT nebo směs s polyesterem', 'trénink, basketbal, rozcvičení'],
              ['Air Dri-FIT (tréninková na zip)', 'lehká funkční mikina s kapucí a zipem', 'trénink a cesta na hřiště'],
              ['Flight, Wordmark, sezonní edice', 'mikiny s nápisy a grafikou', 'pro fanoušky značky']]) +
          '<p>Kromě toho se v nabídce objevují speciální kousky, třeba vánoční mikina s motivem Jumpmana nebo mikina s maskovacím vzorem Realtree. Takové edice se vyrábějí krátce a v obchodech rychle mizí.</p>'
          '<h2>Fleece, nebo Dri-FIT</h2>'
          '<p>Většina mikin Jordan je z takzvaného fleece, tedy pleteniny z bavlny a polyesteru, která má zevnitř počesaný měkký povrch. Hřeje, je příjemná na kůži a hodí se na běžné nošení. Při intenzivním sportu ale nasákne potem a dlouho schne. '
          'Dri-FIT je označení funkčních materiálů Nike z polyesteru, které odvádějí pot od těla k povrchu látky, kde se odpaří. Mikiny z tohoto materiálu jsou lehčí, rychleji schnou a hodí se na trénink nebo na rozcvičení před zápasem. Na sezení ve studené hale nebo na zimní procházku hřejí méně než fleece. '
          'Kdo chce mikinu hlavně do města, vybere fleece. Kdo v ní bude hrát basketbal nebo chodit do posilovny, sáhne po řadě Sport nebo Dri-FIT. Pro srovnání stojí za pohled i <a href="/nike-tech-fleece/">Nike Tech Fleece</a>, což je tenčí a hladší materiál mateřské značky.</p>'
          '<h2>Přes hlavu, nebo na zip</h2>'
          '<p>Mikina přes hlavu, často s klokaní kapsou vpředu, je klasika streetwearu. Lépe drží tvar, logo na hrudi je vidět celé a vítr se k tělu nedostane přes zip. '
          'Mikina na zip je praktičtější, když se často převlékáte nebo střídáte teplo a chlad. Rozepnete ji, aniž byste ji museli sundat, a přes tričko vypadá jako lehká bunda. Rozepínací mikiny všech značek jsou pohromadě v kategorii <a href="/mikiny-na-zip/">mikiny na zip</a>, pánské na stránce <a href="/panska-mikina-na-zip/">pánská mikina na zip</a>. '
          'Mikina bez kapuce s kulatým výstřihem, v názvech označovaná jako crew nebo crew-neck, se dobře nosí pod bundu a nevadí pod ní kapuce bundy.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Mikiny Jordan mají americké velikosti XS až XXL a u některých modelů i větší. Řiďte se obvodem hrudníku v tabulce prodejce, ne jen písmenem, které nosíte u jiných značek. '
          'Střih se liší podle řady. Některé mikiny jsou volnější a delší, jiné sedí blíž k tělu. Údaj o střihu, například standardní nebo volný, výrobce uvádí v popisu produktu. Pokud chcete mikinu nosit volně v duchu basketbalové módy, vezměte o číslo větší. '
          'Dětské mikiny se prodávají v dětských velikostech podle věku nebo výšky. Dámské řady, například Brooklyn Fleece pro ženy nebo Wordmark Fleece, mají kratší délku a jinak tvarované rukávy.</p>'
          '<h2>Kód produktu a barva</h2>'
          '<p>Nike a Jordan označují každý model kódem, který najdete na štítku uvnitř mikiny a často i v názvu nabídky, například FJ7774 nebo DQ7870. Trojčíslí za pomlčkou určuje barevnou variantu. '
          'Kód se hodí při srovnávání nabídek. Pomůže rozlišit dva podobně pojmenované modely a ověřit, že ve dvou obchodech jde opravdu o stejnou mikinu. Pokud obchod kód neuvádí, porovnejte fotky loga, kapes a zipu.</p>'
          '<h2>Na co si dát pozor při nákupu</h2>'
          '<ul><li><strong>Padělky.</strong> Jordan patří k často padělaným značkám. Nakupujte v ověřených obchodech a buďte opatrní u nabídek, které se výrazně liší od ostatních.</li>'
          '<li><strong>Dětská velikost v pánské kategorii.</strong> V názvech se někdy objevují zkratky pro dětské modely. Zkontrolujte velikostní tabulku dřív, než mikinu objednáte.</li>'
          '<li><strong>Fleece na trénink.</strong> Teplá bavlněná mikina se při sportu rychle propotí. Na hřiště volte funkční řadu.</li>'
          '<li><strong>Barva podle fotky.</strong> Na displeji se odstíny liší. Pokud řešíte konkrétní barvu, hledejte podle kódu barevné varianty.</li></ul>'
          '<h2>Péče o mikinu</h2>'
          '<p>Mikinu perte naruby na teplotu uvedenou na štítku, obvykle 30 nebo 40 °C, a se zapnutým zipem. Potisk a logo vydrží déle, když se neperou zvenku a nesuší se v horké sušičce. '
          'Funkční materiály Dri-FIT nemají rády aviváž, která ucpává vlákna a zhoršuje odvod potu. Bavlněný fleece se po prvních praních může mírně srazit, proto ho nesušte na topení. Žmolky na povrchu odstraníte odžmolkovačem.</p>'
          '<h2>S čím mikinu Jordan kombinovat</h2>'
          '<p>Nejčastěji se mikina nosí v kompletu s tepláky stejné řady, třeba Brooklyn Fleece nebo Essentials. K tomu se hodí boty <a href="/jordan-1/">Air Jordan 1</a> nebo <a href="/jordan-4/">Air Jordan 4</a> a na hřiště <a href="/basketbalova-obuv/">basketbalové boty</a>. '
          'Na léto doplní kolekci <a href="/jordan-tricko/">trička Jordan</a> a <a href="/jordan-kratasy/">kraťasy Jordan</a>. Kdo chce srovnat mikiny i jiných značek, najde výběr na stránkách <a href="/nike-mikina/">mikiny Nike</a> a <a href="/panska-mikina/">pánské mikiny</a>.</p>'
          '<h2>Mikina na basketbal a trénink</h2>'
          '<p>Na hřišti se mikina nosí hlavně při rozcvičce, mezi zápasy a na cestě z haly. Hodí se lehčí model, který se rychle obléká a nenasákne potem. Tréninková mikina Air Dri-FIT na celý zip se dá přehodit přes dres a po rozehřátí snadno sundat. '
          'Mikiny řady Sport Crossover mají střih, který neomezuje pohyb paží při střelbě nebo přihrávce. Do posilovny se hodí spíš mikina bez kapuce, která nepřekáží na lavici a při cvičení s osou na zádech.</p>'
          '<h2>Co zkontrolovat po doručení</h2>'
          '<p>Mikinu si vyzkoušejte doma s tričkem, které pod ní budete nosit, a štítky zatím nestříhejte. Zkontrolujte délku rukávů, šířku v ramenou a délku trupu při předklonu. Podívejte se i na kód modelu na vnitřním štítku a porovnejte ho s nabídkou. '
          'Pokud mikina nesedí, můžete ji u nákupu na internetu vrátit bez udání důvodu do 14 dnů od převzetí. Přesné podmínky vrácení a výměny velikosti najdete v obchodních podmínkách prodejce.</p>'
          '<h2>Mikina jako dárek</h2>'
          '<p>Mikina Jordan je častý dárek pro teenagery i dospělé fanoušky basketbalu. Pokud neznáte přesnou velikost, zkuste nenápadně zjistit obvod hrudníku z mikiny, kterou obdarovaný rád nosí, a porovnejte ho s tabulkou. Univerzálnější volbou je mikina na zip nebo volnější střih, kde o číslo menší nebo větší tolik nevadí. '
          'Klasické barvy, tedy černá, šedá a červená, se kombinují snadněji než sezonní odstíny. U dárku se vyplatí zkontrolovat, jak dlouho obchod umožňuje výměnu velikosti.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Vyberte si řadu a typ, tedy přes hlavu nebo na zip, a potom porovnejte nabídky stejného kódu. Ceny se mezi obchody liší podle barvy a velikosti, které mají na skladě. Sporteka zobrazuje nabídky českých e-shopů vedle sebe, objednávku dokončíte u vybraného prodejce.</p>',
    faq=[
        ('Je Jordan stejná značka jako Nike?', 'Jordan je samostatná značka, kterou Nike představil v roce 1997. Patří do skupiny Nike, a proto se v názvech produktů objevuje i spojení Nike Jordan nebo Air Jordan.'),
        ('Co je Brooklyn Fleece?', 'Řada mikin a tepláků Jordan z bavlněné směsi s počesaným rubem. Jsou měkké a teplé, hodí se na každodenní nošení. Vyrábí se pánské, dámské i dětské verze.'),
        ('Jaký je rozdíl mezi fleece a Dri-FIT mikinou?', 'Fleece je teplá pletenina z bavlny a polyesteru na běžné nošení. Dri-FIT je funkční polyesterový materiál Nike, který odvádí pot a rychle schne, proto se hodí na trénink.'),
        ('Jak vybrat velikost mikiny Jordan?', 'Podle obvodu hrudníku v tabulce prodejce. Velikosti jsou americké a střih se liší podle řady. Na volnější styl vezměte o číslo větší.'),
        ('Co znamená kód FJ7774 nebo DQ7870?', 'Je to kód modelu Nike a Jordan. Trojčíslí za pomlčkou určuje barvu. Podle kódu ověříte, že ve dvou obchodech jde o stejnou mikinu.'),
        ('Má Jordan mikiny na zip?', 'Ano, například Brooklyn Fleece Full-Zip, Essentials Full Zip nebo tréninkovou mikinu Air Dri-FIT s kapucí. Kdo chce srovnat i jiné značky, najde je v kategorii mikiny na zip.'),
        ('Jsou mikiny Jordan i pro děti a ženy?', 'Ano. Dětské mikiny se prodávají podle věku nebo výšky, dámské řady mají kratší délku a jiný tvar rukávů.'),
        ('Jak prát mikinu Jordan?', 'Naruby, se zapnutým zipem, na teplotu ze štítku. Bez aviváže, hlavně u funkčních materiálů. Nesušte v horké sušičce ani na topení.'),
        ('Jak poznat originální mikinu Jordan?', 'Nakupujte v ověřených obchodech, kontrolujte kód produktu na štítku a kvalitu výšivky nebo potisku loga. Podezřelé jsou nabídky výrazně odlišné od ostatních prodejců.'),
        ('Kde porovnat ceny mikin Jordan?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Vyberete model, porovnáte prodejce a nákup dokončíte v e-shopu.'),
    ])

# ------------------------------------------------------------------ panska-mikina-na-zip
NEW['panska-mikina-na-zip'] = dict(
    title='Pánská mikina na zip: s kapucí, fleece i merino',
    desc='Pánské mikiny na zip: celé rozepínací s kapucí, fleecové, merino i sportovní s krátkým zipem. Jak vybrat materiál, střih, zip a velikost.',
    intro='<p><strong>Pánská mikina na zip</strong> se dá rozepnout, aniž byste ji museli sundávat, a proto se hodí na dny, kdy se střídá teplo a chlad. '
          'Na této stránce jsou pánské modely z kategorie <a href="/mikiny-na-zip/">mikiny na zip</a> s nabídkami českých obchodů: bavlněné mikiny s kapucí na celý zip, fleecové mikiny na turistiku, hřejivé merino mikiny i tenké sportovní mikiny s krátkým zipem u krku. '
          'Průvodce vysvětluje, jaký je rozdíl mezi celým, polovičním a čtvrtinovým zipem, z jakých materiálů se mikiny vyrábějí a co znamenají čísla jako 100, 200 nebo 260 v názvech. '
          'Kdo hledá spíš mikinu přes hlavu, najde ji na stránce <a href="/panska-mikina/">pánská mikina</a>, funkční modely pod <a href="/panska-funkcni-mikina/">pánská funkční mikina</a>.</p>',
    guide='<h2>Celý, poloviční, nebo čtvrtinový zip</h2>'
          '<p>Délka zipu rozhoduje o tom, jak mikinu nosíte. Mikina rozepínací po celé délce funguje skoro jako lehká bunda, mikina s krátkým zipem se obléká přes hlavu a zip slouží hlavně k větrání u krku.</p>'
          + T(['Typ zipu', 'V názvech', 'Výhody', 'Kdy se hodí'], [
              ['celý zip', 'full zip, FZ, rozepínací', 'snadné oblékání, dobré větrání, nosí se i rozepnutá', 'město, turistika, vrstva pod bundu'],
              ['poloviční zip', 'half zip, 1/2 zip', 'méně švů, lepší ochrana před větrem', 'turistika, skialpy, běžky'],
              ['čtvrtinový zip', 'quarter zip, 1/4 zip', 'lehká, přiléhavá, větrání u krku', 'běh, trénink, golf, sport v chladu'],
              ['dvoucestný zip', 'two-way zip', 'rozepíná se i zespodu', 'delší mikiny, sezení a jízda na kole']]) +
          '<p>Na sport, při kterém se hodně zahřejete, je praktická mikina s krátkým zipem. Je lehčí a pod bundou nenabírá látku. Na každodenní nošení a jako vrstvu, kterou během dne sundáváte a znovu oblékáte, je pohodlnější celý zip.</p>'
          '<h2>Materiály a co od nich čekat</h2>'
          '<p><strong>Bavlněná teplákovina</strong> je klasika volnočasových mikin. Bývá ze směsi bavlny a polyesteru, zevnitř hladká se smyčkami nebo počesaná do měkkého povrchu. Je příjemná na kůži a dobře snáší praní, ale při pocení nasákne a pomalu schne. Typické jsou mikiny s kapucí od <a href="/znacka/champion/">Champion</a>, Calvin Klein, Napapijri, Lacoste nebo Timberland. '
          '<strong>Polyesterový fleece</strong> je lehký, hřeje i v mírné vlhkosti a rychle schne. Vítr jím ale prochází, proto se v horách nosí pod bundu. Fleecové mikiny na zip mají v nabídce <a href="/znacka/columbia/">Columbia</a>, Trespass, Jack Wolfskin nebo The North Face. '
          '<strong>Merino</strong> je jemná vlna, která hřeje, reguluje teplotu a pomaleji zapáchá. Merino mikiny na zip najdete například u <a href="/znacka/icebreaker/">Icebreaker</a> a Sensor. '
          '<strong>Funkční úplety</strong> z polyesteru a elastanu jsou tenké, pružné a odvádějí pot. Používají je hlavně sportovní značky, například <a href="/znacka/under-armour/">Under Armour</a>, Puma, Adidas nebo Craft.</p>'
          '<h2>Co znamenají čísla v názvech</h2>'
          '<p>U fleecových mikin se setkáte s čísly 100, 200 a 300. Tato řada pochází od výrobce fleecu Polartec a označuje hmotnost látky. Stovka je lehká a prodyšná, hodí se na pohyb. Dvoustovka je střední a nejuniverzálnější. Třístovka je nejtěžší a nejteplejší, ale při rychlé chůzi do kopce v ní bývá horko. '
          'U merina udávají čísla jako 200, 260 nebo 400 hmotnost látky v gramech na metr čtvereční. Icebreaker 260 je tedy středně silná pletenina na chladné dny, 400 RealFleece silná merino mikina na opravdu chladné dny. Hmotnost ale neříká všechno, záleží i na struktuře pleteniny a na střihu.</p>'
          '<h2>Mikina jako vrstva pod bundu</h2>'
          '<p>Turisté a lyžaři nosí oblečení ve vrstvách. Nejblíž k tělu je funkční triko, které odvádí pot, uprostřed hřejivá mikina a navrch bunda, která chrání před větrem a deštěm. Mikina na zip je ideální prostřední vrstva, protože ji při výstupu rozepnete a na vrcholu zase zapnete. '
          'Na tuto roli se hodí fleece nebo merino, bavlna méně, protože vlhkost ze zad drží u těla. Mikina by neměla být příliš objemná, jinak se pod bundou mačká. Na chladnější dny se k mikině hodí i <a href="/panske-vesty/">pánská vesta</a>. Více materiálů na túry je v kategoriích <a href="/fleecove-mikiny/">fleecové mikiny</a> a <a href="/merino-mikiny/">merino mikiny a svetry</a>.</p>'
          '<h2>Podle čeho poznat kvalitní zip</h2>'
          '<p>Zip je nejčastější místo, které na mikině selže. Dobrý zip jde hladce, jezdec nedrží jen na jedné straně a zuby se po zapnutí nerozjíždějí. Velká část výrobců používá zipy japonské firmy YKK, jejíž značku najdete na jezdci. '
          'U sportovních mikin se hodí kryt zipu na bradě, který zabrání odření krku, a vnitřní lišta za zipem, která brání průniku větru. Kapsy na zip udrží klíče a telefon i při běhu. Před praním zip vždy zapněte, otevřené zuby trhají ostatní prádlo a samy se ohýbají.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Mikiny se prodávají ve velikostech S až XXL a větších. Řiďte se obvodem hrudníku v tabulce obchodu. Volnočasové mikiny mají rovný a volnější střih, sportovní a outdoorové přiléhají víc k tělu, aby se daly nosit pod bundou. '
          'Rukáv má při předpažení dosáhnout na zápěstí a spodní okraj zakrýt pas i při předklonu. Pokud mikinu chcete nosit přes silnější vrstvu, vezměte o číslo větší. U modelů s pružným lemem na rukávech a v pase drží mikina teplo lépe než u volných okrajů.</p>'
          '<h2>Týmové mikiny na zip</h2>'
          '<p>Část nabídky tvoří mikiny s logy amerických lig NHL, NFL a NBA od výrobců jako Antigua nebo <a href="/znacka/fanatics/">Fanatics</a>. Jde o fanouškovské oblečení, často s velkou výšivkou nebo potiskem. Na sport se příliš nehodí, ale na zápas nebo do města ano. '
          'Pro fanoušky basketbalu jsou tu i <a href="/jordan-mikina/">mikiny Jordan</a>, například řady Brooklyn Fleece nebo Essentials ve verzi na celý zip.</p>'
          '<h2>Péče o mikinu na zip</h2>'
          '<p>Před praním zapněte zip a mikinu obraťte naruby. Bavlněné mikiny snesou 30 až 40 °C, fleece a funkční úplety perte na nižší teplotu a bez aviváže. Merino perte na vlnu nebo ručně a sušte rozložené naplocho. Fleece nesušte v horké sušičce, vlákna se mohou spéct a žmolkovat. '
          'Zasekávající se zip pomůže promazat grafitovou tužkou nebo voskem. Pokud jezdec přestane zuby spojovat, dá se často vyměnit v opravně oděvů bez výměny celého zipu.</p>'
          '<h2>Mikina na zip na běh a do posilovny</h2>'
          '<p>Na běh v chladu se hodí přiléhavá mikina s krátkým zipem z funkčního úpletu. Při rozběhu ji necháte zapnutou, po zahřátí rozepnete zip u krku a teplo odchází ven bez sundávání. Reflexní prvky na rukávech a zádech zvýší viditelnost za šera. '
          'Pod Under Armour, Puma nebo Adidas najdete i tréninkové mikiny s polovičním zipem, které se nosí na rozcvičku před zápasem. Do posilovny se víc hodí volnější bavlněná mikina s kapucí na celý zip, kterou mezi sériemi snadno odložíte. Merino mikina s krátkým zipem je dobrou volbou na běžky a skialpy, protože ani po hodinách pohybu tolik nezapáchá.</p>'
          '<h2>Kapuce, nebo stojáček</h2>'
          '<p>Kapuce chrání krk a hlavu před větrem a hodí se do města, kde ji na zastávce přetáhnete přes čepici. Pod bundou s vlastní kapucí ale může překážet a dělat na zádech val. '
          'Mikina se stojáčkem, tedy vyšším límcem na zip, je pro turistiku a sport praktičtější. Zakryje krk až k bradě, pod bundou se nemačká a dá se snadno kombinovat s nákrčníkem. Kdo nosí mikinu hlavně jako samostatnou vrchní vrstvu, zvolí kapuci. Kdo ji bude nosit pod bundou, sáhne po stojáčku.</p>'
          '<h2>Volnočasová, nebo outdoorová mikina</h2>'
          '<p>Volnočasové mikiny na zip od značek jako Champion, Calvin Klein nebo Superdry kladou důraz na vzhled, logo a měkký materiál. Na procházku, do školy nebo na cestování jsou ideální. '
          'Outdoorové mikiny Columbia, Dynafit nebo Trespass jsou navržené jako vrstva do hor. Mají delší záda, užší rukávy s pružným lemem a materiál, který rychle schne. Rozdíl poznáte i podle hmotnosti a podle toho, jestli výrobce uvádí typ fleecu nebo podíl merina. Kdo mikinu potřebuje na obojí, zvolí jednoduchý fleece v tlumené barvě.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Nejdřív si ujasněte, kde budete mikinu nosit, potom zvolte materiál a délku zipu. Srovnávejte konkrétní modely podle materiálu a hmotnosti látky, ne jen podle vzhledu. Sporteka sdružuje nabídky českých e-shopů na jednom místě. '
          'Ke kompletu se hodí <a href="/panske-teplaky/">pánské tepláky</a> nebo hotová <a href="/teplakova-souprava-panska/">pánská tepláková souprava</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi full zip a half zip?', 'Full zip se rozepíná po celé délce a obléká se jako bunda. Half zip má zip jen do půlky hrudníku, obléká se přes hlavu a lépe drží teplo.'),
        ('Co znamená 1/4 zip?', 'Krátký zip u krku, zhruba na čtvrtinu délky trupu. Mikiny s ním jsou lehké a přiléhavé, používají se na běh, trénink a sport v chladu.'),
        ('Jaká mikina na zip na turistiku?', 'Fleecová nebo merino mikina, která hřeje i v mírné vlhkosti a rychle schne. Bavlněná mikina na túru není ideální, protože nasákne potem.'),
        ('Co znamená fleece 100, 200 a 300?', 'Hmotnostní řadu fleecu podle výrobce Polartec. Stovka je lehká na pohyb, dvoustovka střední a univerzální, třístovka nejteplejší na nižší aktivitu.'),
        ('Co znamená číslo u merino mikiny?', 'Hmotnost látky v gramech na metr čtvereční. Čím vyšší číslo, tím silnější pletenina. Například 260 je středně silná, 400 silná mikina.'),
        ('Jak vybrat velikost mikiny na zip?', 'Podle obvodu hrudníku v tabulce obchodu. Pokud ji chcete nosit přes silnější vrstvu, vezměte o číslo větší. Rukáv má sahat k zápěstí.'),
        ('Proč se zip na mikině zasekává?', 'Často kvůli nečistotám nebo ohnutým zubům. Pomůže promazat zip grafitem nebo voskem. Opotřebený jezdec se dá vyměnit v opravně oděvů.'),
        ('Jak prát mikinu na zip?', 'Se zapnutým zipem, naruby a na teplotu ze štítku. Fleece a funkční materiály bez aviváže, merino na program pro vlnu.'),
        ('Hodí se mikina na zip pod bundu?', 'Ano, je to typická prostřední vrstva. Při výstupu ji rozepnete, na zastávce zapnete. Nemá být příliš objemná, aby se pod bundou nemačkala.'),
        ('Kde porovnat ceny pánských mikin na zip?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Vyberete model a nákup dokončíte v e-shopu, kde ověříte velikost a barvu.'),
    ])

# ------------------------------------------------------------------ panske-kalhoty
NEW['panska-nepromokava-bunda'] = dict(
    title='Pánská nepromokavá bunda: membrána, švy a vrstvy',
    desc='Pánské nepromokavé bundy na túry, do města i na kolo: membrána, vodní sloupec, prodyšnost, podlepené švy a bundy 3v1. Jak vybrat a pečovat.',
    intro='<p><strong>Pánská nepromokavá bunda</strong> má jediný hlavní úkol: udržet vás v suchu, i když prší celý den. Dobrá bunda přitom pustí ven páru z těla, aby se pod ní člověk nezpotil. '
          'Na této stránce jsou pánské modely z kategorie <a href="/nepromokave-bundy/">nepromokavé a outdoorové bundy</a> s nabídkami českých obchodů: lehké bundy do batohu, turistické bundy s membránou, odolné hardshelly do hor, městské pláštěnky i bundy 3v1 s vyjímatelnou vložkou. '
          'Průvodce vysvětluje, co znamená vodní sloupec a prodyšnost, jak se liší dvouvrstvá a třívrstvá konstrukce, proč záleží na švech a jak bundu prát, aby si udržela vlastnosti. '
          'Dámské modely najdete na stránce <a href="/damska-nepromokava-bunda/">dámská nepromokavá bunda</a>.</p>',
    guide='<h2>Jak nepromokavá bunda funguje</h2>'
          '<p>Většina dnešních nepromokavých bund stojí na membráně. Je to tenká vrstva s póry, které jsou příliš malé pro kapky vody, ale propustí molekuly vodní páry. Déšť tedy zůstane venku a pot se může odpařit ven. '
          'Membrána je citlivá, proto se kombinuje se svrchní tkaninou a s podšívkou nebo ochranným potiskem. Svrchní tkanina má vodoodpudivou úpravu, po které voda stéká v kapkách. Když úprava přestane fungovat, látka se nasákne, membrána přestane dýchat a člověk má pocit, že bunda promokla, i když ve skutečnosti jde o kondenzaci zevnitř.</p>'
          '<h2>Vodní sloupec a prodyšnost</h2>'
          '<p>Vodní sloupec se udává v milimetrech a vyjadřuje, jak velký tlak vody látka vydrží, než začne propouštět. Výrobci uvádějí hodnoty od několika tisíc až po desítky tisíc milimetrů. Vyšší číslo znamená spolehlivější ochranu, zvlášť na ramenou pod popruhy batohu a při sezení na mokrém. '
          'Prodyšnost se uvádí dvěma způsoby. Hodnota RET vyjadřuje odpor látky proti prostupu páry, čím nižší, tím lépe. Často se uvádí, že RET pod 6 je velmi prodyšná látka, 6 až 13 prodyšná a 13 až 20 ještě vyhovující, jednotliví výrobci ale používají mírně odlišné hranice. Druhý údaj, MVTR v gramech na metr čtvereční za 24 hodin, ukazuje, kolik páry projde, a tam je naopak vyšší číslo lepší. '
          'Pracovní a ochranné oděvy se zkoušejí podle evropské normy EN 343. Ta od roku 2019 dělí nepromokavost i prodyšnost do čtyř tříd, kde čtyřka je nejlepší. U sportovních bund se s ní setkáte méně často, většina výrobců uvádí vlastní hodnoty.</p>'
          '<h2>Dvě, dvě a půl, nebo tři vrstvy</h2>'
          + T(['Konstrukce', 'Jak je složená', 'Pro koho'], [
              ['2L (dvouvrstvá)', 'svrchní látka s membránou a volná podšívka', 'město, procházky, nenáročné túry'],
              ['2,5L', 'svrchní látka s membránou a tenký ochranný potisk místo podšívky', 'lehké bundy do batohu, běh, kolo'],
              ['3L (třívrstvá)', 'svrchní látka, membrána a podšívka spojené do jedné vrstvy', 'hory, vícedenní trek, skialpy, časté nošení s batohem'],
              ['3v1', 'nepromokavá svrchní bunda a vyjímatelná fleecová nebo zateplená vložka', 'kdo chce jednu bundu na podzim i zimu']]) +
          '<p>Třívrstvé bundy, často označované jako hardshell, jsou nejodolnější a nejlépe snášejí odírání batohem. Bývají ale tužší a šustí. Dvou a půl vrstvé bundy jsou lehké a sbalí se do malého prostoru, hodí se jako bunda pro případ deště. Bunda 3v1 je praktická do města a na rodinné výlety, protože vložku můžete nosit i samostatně.</p>'
          '<h2>Švy, zipy a kapuce</h2>'
          '<p>Membrána nestačí, když voda projde švy. Nepromokavá bunda proto musí mít švy podlepené páskou zevnitř. Levnější modely mají někdy podlepené jen hlavní švy, v popisu pak hledejte údaj, že jsou podlepené všechny. '
          'Hlavní zip by měl být zakrytý légou nebo mít vodoodolnou úpravu, a totéž platí pro kapsy. Kapuce na hory se nastavuje stahováním vzadu i po stranách a má vyztužený kšilt, který udrží vodu mimo obličej. Zipy v podpaží pomohou odvětrat bundu při výstupu, kdy ani nejlepší membrána nestačí odvést všechen pot.</p>'
          '<h2>Technologie a značky v nabídce</h2>'
          '<p>Kromě membrán Gore-Tex mají velcí výrobci vlastní technologie. <a href="/znacka/regatta/">Regatta</a> používá materiály Isotex, Columbia technologii Omni-Tech a The North Face DryVent, dříve nazývanou HyVent. Hodnoty vodního sloupce a prodyšnosti uvádí každý výrobce u konkrétního modelu, proto je srovnávejte v popisu, ne podle názvu technologie. '
          'Nejvíc pánských nepromokavých bund v nabídce mají <a href="/znacka/trespass/">Trespass</a>, Regatta a <a href="/znacka/dare2b/">Dare2b</a>. Dále tu jsou <a href="/znacka/columbia/">Columbia</a> s modely Hikebound nebo Bugaboo, Kilpi, Salewa, Northfinder s lehkou bundou Northkit, The North Face, Viking, Haglöfs, Husky a Montane. '
          'Norská <a href="/znacka/helly-hansen/">Helly Hansen</a> začala v roce 1877 v Moss vyrábět nepromokavé oděvy z plátna napuštěného lněným olejem. Od roku 1980 používá vlastní prodyšný materiál Helly Tech. V nabídce jsou například modely Dubliner nebo Crew. '
          'Pro běžce jsou tu lehké bundy Compressport, do města pláštěnky Rains a Didriksons. Fjällräven nabízí i nepromokavé bundy z materiálu Hydratic, zatímco jeho bundy z materiálu G-1000 jsou jen voděodolné.</p>'
          '<h2>Jak vybrat střih a velikost</h2>'
          '<p>Nepromokavá bunda je vrchní vrstva, takže musí jít zapnout přes mikinu, na podzim přes <a href="/fleecove-mikiny/">fleecovou mikinu</a> nebo tenkou zateplenou vestu. Zkoušejte ji s vrstvou, kterou pod ni budete nosit. '
          'Při zvednutých rukou nemá lem vyjet nad pas a rukávy mají zakrýt zápěstí. Turistické bundy bývají delší vzadu, aby voda nestékala za kalhoty. Na kolo se hodí bunda s prodlouženými zády, na hory kapuce, která se vejde přes helmu.</p>'
          '<h2>Výbava do deště</h2>'
          '<p>Samotná bunda nestačí, když prší celý den. Doplňte ji o <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>, nepromokavé boty, třeba <a href="/trekove-boty-panske/">pánské trekové boty</a> s membránou, a věci v batohu zabalte do <a href="/nepromokave-vaky/">nepromokavých vaků</a>. '
          'Na chladné deštivé dny se pod bundu hodí <a href="/termopradlo-panske/">pánské termoprádlo</a>, v zimě rovnou <a href="/panska-zimni-bunda/">pánská zimní bunda</a>.</p>'
          '<h2>Péče o nepromokavou bundu</h2>'
          '<p>Bundu perte, když je špinavá nebo propocená, protože nečistoty a mastnota z kůže zhoršují funkci membrány. Použijte prostředek na funkční oblečení, nikdy aviváž ani běžný prášek s bělidly. Zapněte všechny zipy a suché zipy a perte na teplotu uvedenou na štítku. '
          'Když voda na povrchu přestane tvořit kapky, obnovte vodoodpudivou úpravu prostředkem z kategorie <a href="/impregnace/">impregnace</a>. Mnoho výrobců doporučuje bundu po praní krátce vysušit v sušičce na nízkou teplotu nebo prožehlit přes látku, protože teplo úpravu oživí. Řiďte se ale štítkem.</p>'
          '<h2>Bunda na kolo a na běh</h2>'
          '<p>Na kolo a na běh se nehodí těžký hardshell. Lepší je lehká bunda konstrukce 2,5L, která se sbalí do kapsy dresu nebo do běžecké vesty. Na kolo by měla mít prodloužená záda, delší rukávy a reflexní prvky, kapuce buď žádná, nebo taková, která se vejde pod helmu. '
          'Běžecké nepromokavé bundy jsou přiléhavé a velmi lehké. Při rychlém pohybu se v nich ale člověk zpotí i při nejlepší membráně, proto je dobré je oblékat jen do deště a v suchu nosit větrovku nebo nic.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Nepodlepené švy.</strong> Bunda z nepromokavé látky bez podlepených švů v dešti propouští vodu na ramenou.</li>'
          '<li><strong>Těsná bunda.</strong> Pokud se pod bundu nevejde mikina, na podzim v ní bude zima. Zkoušejte ji s vrstvou.</li>'
          '<li><strong>Kapuce bez nastavení.</strong> Volná kapuce se ve větru stahuje z hlavy a při otočení hlavy zakrývá výhled.</li>'
          '<li><strong>Praní s aviváží.</strong> Aviváž zničí vodoodpudivou úpravu i prodyšnost membrány. Používejte prostředek na funkční oblečení.</li>'
          '<li><strong>Bunda do sucha.</strong> Kdo nosí nepromokavou bundu i za sucha při rychlé chůzi, zbytečně se zpotí. Na suché a větrné dny je lepší softshell.</li></ul>'
          '<h2>Lehká bunda do batohu, nebo bunda na každý den</h2>'
          '<p>Kdo potřebuje bundu hlavně pro jistotu na túře, ocení lehký model, který se sbalí do vlastní kapsy a v batohu skoro nezabere místo. Takovou bundu oblékáte jen v dešti, takže prodyšnost a odolnost nejsou tak důležité jako hmotnost. '
          'Pro každodenní nošení do práce nebo se psem je lepší pevnější bunda s podšívkou, delším střihem a kapsami na ruce. Vydrží časté oblékání, odírání od tašky přes rameno a nevadí jí ani silnější mikina pod ní.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Nejdřív si ujasněte, k čemu bundu potřebujete, potom srovnejte konstrukci, vodní sloupec, prodyšnost a podlepení švů. Barva a střih přijdou na řadu až nakonec. Sporteka sdružuje nabídky českých e-shopů, takže uvidíte, kde mají váš model a velikost. '
          'Na větrné dny bez deště se hodí <a href="/softshellova-bunda-panska/">pánská softshellová bunda</a>, na přechodné období <a href="/panska-podzimni-bunda/">pánská podzimní bunda</a>.</p>',
    faq=[
        ('Jaký vodní sloupec má mít nepromokavá bunda?', 'Čím vyšší, tím spolehlivější ochrana. Bundy na hory a s batohem mívají vyšší hodnoty než městské modely. Stejně důležité jsou podlepené švy a kvalitní zipy.'),
        ('Co znamená RET?', 'Odpor látky proti prostupu vodní páry. Čím nižší číslo, tím je látka prodyšnější. Hodnoty pod 6 se obvykle považují za velmi prodyšné, hranice se ale u výrobců liší.'),
        ('Jaký je rozdíl mezi 2L, 2,5L a 3L?', '2L má volnou podšívku, 2,5L tenký ochranný potisk místo podšívky a 3L všechny vrstvy spojené do jedné. Třívrstvé bundy jsou nejodolnější, 2,5L nejlehčí.'),
        ('Proč jsem v nepromokavé bundě mokrý?', 'Často jde o pot, který nestihne projít membránou, nebo o nasáklou svrchní látku. Pomůže větrání, správné vrstvy a obnova vodoodpudivé úpravy.'),
        ('Co je bunda 3v1?', 'Nepromokavá svrchní bunda s vyjímatelnou fleecovou nebo zateplenou vložkou. Obě části můžete nosit zvlášť i spolu, takže bunda poslouží na podzim i v zimě.'),
        ('Co znamená norma EN 343?', 'Evropská norma pro oděvy chránící před deštěm. Dělí nepromokavost a prodyšnost do čtyř tříd, kde čtyřka je nejlepší. Používá se hlavně u pracovních oděvů.'),
        ('Jak prát nepromokavou bundu?', 'V prostředku na funkční oblečení, bez aviváže, se zapnutými zipy a na teplotu ze štítku. Po praní pomůže krátké sušení na nízkou teplotu, pokud ho štítek dovoluje.'),
        ('Jak obnovit nepromokavost bundy?', 'Membrána obvykle funguje dál, slábne vodoodpudivá úprava povrchu. Bundu vyperte a naneste impregnaci ve spreji nebo prací impregnaci.'),
        ('Je hardshell totéž co nepromokavá bunda?', 'Hardshell je nepromokavá bunda s pevnou, většinou třívrstvou konstrukcí do hor. Každý hardshell je nepromokavý, ale ne každá nepromokavá bunda je hardshell.'),
        ('Kde porovnat ceny pánských nepromokavých bund?', 'Na této stránce jsou nabídky českých obchodů pohromadě. Vyberete model a nákup dokončíte v e-shopu, kde ověříte velikost a barvu.'),
    ])
