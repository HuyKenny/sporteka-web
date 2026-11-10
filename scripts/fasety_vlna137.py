"""sporteka.cz — facet landing texts wave 137: proteiny-v-akci, bila-sportovni-podprsenka, hannah-lyzarska-bunda, boxerske-rukavice-venum.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ proteiny-v-akci
NEW['proteiny-v-akci'] = dict(
    title='Proteiny v akci: jak poznat opravdovou slevu',
    desc='Proteiny ve slevě: jak poznat skutečnou akci, přepočítat cenu na porci bílkovin, hlídat trvanlivost a porovnat nabídky českých obchodů.',
    intro='<p>Proteiny ve slevě lákají k nákupu do zásoby, jenže na prášku v akci se dá ušetřit i prodělat. Rozhoduje, z čeho se sleva počítá, kolik bílkovin je v jedné porci a jak dlouho vydrží trvanlivost na obalu. '
          'Tato stránka sbírá nabídky z kategorie <a href="/proteiny/">proteiny</a>, u kterých obchod snížil cenu proti dřívější ceně. Průvodce ukazuje, jak ověřit, že jde o skutečnou slevu, jak přepočítat cenu na gram bílkovin místo na kilogram prášku, proč se v akci často objevují krátké expirace a které druhy se do zásoby hodí. '
          'V nabídce se pravidelně střídají značky jako <a href="/znacka/gymbeam/">GymBeam</a> nebo <a href="/znacka/extrifit/">Extrifit</a>. Jde o obecné informace o nakupování, ne o zdravotní doporučení.</p>',
    guide='<h2>Co se skrývá za slovem akce</h2>'
          '<p>U sportovní výživy se pod označením akce schovává několik různých situací a jen některé z nich jsou pro kupujícího opravdu výhodné. Obchod může snížit cenu proti té, za kterou produkt prodával dřív. Může přidat dárek zdarma, třeba šejkr nebo malé balení jiné příchutě. Může nabízet větší balení za výhodnější poměr, nebo vyprodávat zboží, kterému se blíží konec trvanlivosti. Každá z těchto variant vyžaduje jiný způsob porovnání.</p>'
          + T(['Typ akce', 'Jak funguje', 'Na co si dát pozor'], [
              ['Snížená cena', 'obchod ukazuje původní a aktuální cenu', 'zkontrolujte, zda původní cena někdy opravdu platila'],
              ['Dárek k nákupu', 'k balení přibalí šejkr, tyčinku nebo tester', 'dárek nemá hodnotu, pokud ho nepoužijete'],
              ['Množstevní sleva', 'víc kusů nebo větší balení za výhodnější poměr', 'ověřte, zda protein stihnete spotřebovat'],
              ['Výprodej příchutě nebo obalu', 'obchod uvolňuje sklad před novou verzí', 'často kratší trvanlivost nebo vyřazená příchuť'],
              ['Kód na košík', 'sleva se připočítá až v objednávce', 'srovnávejte konečnou částku včetně dopravy']]) +
          '<p>Základní pravidlo: porovnávejte vždy výslednou cenu za stejné množství stejně kvalitní bílkoviny, nikoli procento slevy. Dvacet procent z nadsazené ceny může být horší než stálá nižší cena u jiného obchodu. Procento slevy je marketingový údaj, cena za porci je údaj, který se dá spočítat.</p>'
          '<h2>Jak poznat skutečnou slevu</h2>'
          '<p>Na přeškrtnuté ceně nezáleží, pokud ji obchod nikdy nevyžadoval. Proto se vyplatí udělat tři rychlé kontroly dřív, než dáte položku do košíku.</p>'
          '<ol><li><strong>Podívejte se na ostatní obchody.</strong> Stejný protein bývá k dispozici ve více e-shopech. Na stránce produktu na Sportece vidíte nabídky vedle sebe, takže rozdíl poznáte hned.</li>'
          '<li><strong>Sledujte cenu několik týdnů.</strong> Pokud o nákupu přemýšlíte předem, cena v oblíbeném obchodě se obvykle pohybuje v určitém pásmu. Akce je zajímavá, jen když z pásma vybočuje dolů.</li>'
          '<li><strong>Ověřte přesné složení a velikost balení.</strong> Obchody někdy porovnávají starší sedmistovkové balení s novějším menším obsahem, takže se cena na kilogram vůbec nezměnila.</li>'
          '<li><strong>Zahrňte dopravu.</strong> Doprava zdarma nad určitou hranici může výhodu akce zvýšit, ale také vás přimět koupit víc, než potřebujete.</li></ol>'
          '<p>Skutečně výhodná nabídka přitom nemusí mít velké procento. Některé obchody drží nízké ceny stabilně a ostatním stačí jen hlídat, kdy dojdou nejlevnější varianty. Druhá možnost je počkat na tematické týdny, o kterých píšeme níže.</p>'
          '<h2>Cena za porci bílkovin, ne za kilogram</h2>'
          '<p>Kilogram prášku není stejný jako kilogram bílkoviny. Koncentrát syrovátky obsahuje obvykle menší podíl bílkovin než izolát a gainer jich má na kilogram ještě méně. Proto se vyplatí spočítat si, kolik gramů čisté bílkoviny dostanete za zaplacenou částku. Postup je jednoduchý: vezměte hmotnost balení, vynásobte podílem bílkovin v prášku, který je uvedený na etiketě, a výslednou částku vydělte cenou.</p>'
          + T(['Údaj', 'Kde ho najdete', 'Proč na něm záleží'], [
              ['Hmotnost balení', 'v názvu produktu', 'určuje celkový počet porcí'],
              ['Podíl bílkovin v 100 g', 'v tabulce výživových hodnot', 'rozlišuje koncentrát, izolát a gainer'],
              ['Velikost porce', 'na etiketě, obvykle kolem třiceti gramů', 'každý výrobce ji určuje jinak'],
              ['Bílkoviny na porci', 'v tabulce na etiketě', 'slouží k přímému porovnání dvou prášků'],
              ['Sladidla a příchutě', 'v seznamu složek', 'mění chuť i vhodnost pro citlivé žaludky']]) +
          '<p>Díky tomuto výpočtu zjistíte, že levnější balení s nižším podílem bílkovin bývá ve výsledku dražší než o něco dražší kus s vysokým obsahem. Podrobné rozdíly mezi druhy najdete v kategorii <a href="/proteiny/">proteiny</a>, kde jsou popsané koncentrát, izolát, kasein i rostlinné směsi.</p>'
          '<h2>Datum minimální trvanlivosti</h2>'
          '<p>Nejčastější důvod, proč je prášek výrazně zlevněn, je blížící se datum minimální trvanlivosti. Neznamená to automaticky, že je potravina nevhodná, ale znamená to, že výrobce po tomto datu nezaručuje plnou kvalitu chuti a vlastností. Protein v suchém sáčku je stabilní potravina, přesto je rozumné jít do akce s jasným plánem spotřeby.</p>'
          + T(['Zbývající doba', 'Co to znamená', 'Doporučení'], [
              ['více než půl roku', 'běžná zásoba', 'bez obav, hlídejte jen skladování'],
              ['zhruba tři až šest měsíců', 'krátká zásoba', 'kupujte jen množství, které stihnete spotřebovat'],
              ['méně než tři měsíce', 'výprodej', 'smysl má jen u malých balení nebo při denním užívání'],
              ['po uplynutí data', 'zboží by se mělo prodávat jen s upozorněním', 'neobjednávejte, pokud to není výslovně uvedeno']]) +
          '<p>Datum bývá uvedené na stránce produktu v e-shopu. Pokud chybí, zeptejte se obchodu ještě před objednávkou. U méně oblíbených příchutí se navíc často liší chuť od očekávání, takže při prvním nákupu nového prášku raději nesahejte po velkém balení.</p>'
          '<h2>Kdy se proteiny obvykle zlevňují</h2>'
          '<p>Slevy nejsou náhodné. Řídí se kalendářem obchodů a sezónou, ve které lidé řeší cvičení. Zde jsou typické okamžiky, kdy se akce objevují častěji.</p>'
          '<ul><li><strong>Konec listopadu:</strong> týden slev kolem Black Friday je obdobím, kdy se přidávají nejen procenta, ale i dárky.</li>'
          '<li><strong>Leden:</strong> po novoročních předsevzetích obchody lákají nové zákazníky na začátek cvičení.</li>'
          '<li><strong>Jaro:</strong> před sezónou formování postavy se objevují balíčky s šejkrem a kreatinem.</li>'
          '<li><strong>Změna receptury nebo obalu:</strong> výrobce vyprodává starý design a zákazník ušetří bez ztráty kvality.</li>'
          '<li><strong>Výročí obchodu a tematické dny:</strong> jednorázové akce na vybrané značky nebo příchutě.</li></ul>'
          '<p>Rozdíl mezi nimi je výrazný. Černý pátek přináší široký výběr, ale také nejvíc nafouknutých původních cen. Změna obalu přináší menší procento slevy, ale zboží je stejné jako dřív.</p>'
          '<h2>Co v akci kupovat a co raději ne</h2>'
          + T(['Druh', 'Do zásoby v akci?', 'Poznámka'], [
              ['Syrovátkový koncentrát', 'ano', 'dlouhá trvanlivost a každodenní použití'],
              ['Syrovátkový izolát', 'ano', 'vyplatí se při citlivosti na laktózu'],
              ['Kasein', 'spíše menší balení', 'méně populární, pomaleji se spotřebuje'],
              ['Rostlinné směsi', 'opatrně', 'příchuť rozhoduje, nejdřív vyzkoušejte malé balení'],
              ['Proteinové tyčinky a snacky', 'jen krátká zásoba', 'kratší trvanlivost, snadno se zhorší chuť'],
              ['Příchutě na zkoušku', 'ne velké balení', 'chuť je subjektivní věc']]) +
          '<p>Jestliže už znáte svou oblíbenou příchuť a značku, je akce na velké balení rozumná. Jestliže zkoušíte, použijte raději testery nebo malé balení. Zkoušení nových příchutí ve velkém je nejčastější způsob, jak se zásoba proteinu změní na nepoužitý přebytek.</p>'
          '<h2>Značky v nabídce a jak se liší</h2>'
          '<p>Mezi zlevněnými nabídkami se často objevují produkty od <a href="/znacka/gymbeam/">GymBeam</a>, <a href="/znacka/extrifit/">Extrifit</a>, <a href="/znacka/isostar/">Isostar</a> nebo <a href="/znacka/insportline/">Insportline</a>. Najdete tu i jiné značky z výživy pro sport. Značka sama nic neříká o vhodnosti pro vás. Rozhoduje typ bílkoviny, složení a chuť. U každého kusu ověřte údaje na etiketě a zvolte takový, který odpovídá vašemu jídelníčku. Další přehled nabídek jedné značky je na stránce <a href="/gymbeam-proteiny/">GymBeam proteiny</a>.</p>'
          '<h2>Okolní produkty, které se vyplatí sledovat</h2>'
          '<p>Při nákupu proteinu v akci se často nabízejí i další doplňky. Mezi nejčastější patří <a href="/kreatin/">kreatin</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny</a> nebo <a href="/gainery/">gainery</a>. Pro lidi, kteří chtějí bílkoviny přijímat v pevné formě, existují <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>. Celkový přehled najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>. Pokud řešíte širší doplňkovou výživu, pomohou i <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>. Spalovače tuku jsou samostatná skupina, které se věnuje kategorie <a href="/spalovace-tuku/">spalovače tuku</a>; sleva na ně nic nemění na tom, že jejich účinek je omezený a že je dobré poradit se s odborníkem.</p>'
          '<h2>Kontrolní seznam před objednávkou</h2>'
          '<ol><li>Je původní cena skutečná a odpovídá ostatním obchodům?</li>'
          '<li>Kolik gramů bílkovin dostanete za zaplacenou částku?</li>'
          '<li>Jaké je datum minimální trvanlivosti a stihnete protein spotřebovat?</li>'
          '<li>Znáte příchuť, nebo je to první nákup?</li>'
          '<li>Platí v ceně doprava, nebo se připočítá?</li>'
          '<li>Neobsahuje prášek složku, na kterou máte alergii?</li></ol>'
          '<p>Pokud odpovíte na všechny otázky souhlasně, pravděpodobně nakupujete dobře. Pokud ne, počkejte, další akce se objeví za pár týdnů.</p>',
    faq=[
        ('Jak poznám, že je sleva na proteinu skutečná?', 'Porovnejte stejný produkt ve více obchodech a sledujte jeho cenu několik týdnů. Pokud akční cena není nižší než běžná cena u konkurence, jde spíš o marketing. Na Sportece vidíte nabídky obchodů vedle sebe, takže rozdíl poznáte rychle.'),
        ('Je protein s blížící se expirací nebezpečný?', 'Datum minimální trvanlivosti neznamená, že je potravina po jeho uplynutí zkažená, ale že výrobce přestává ručit za plnou kvalitu. Suchý prášek je stabilní, ale chuť se může zhoršit. Kupujte jen množství, které stihnete spotřebovat.'),
        ('Mám kupovat protein na zásobu, když je v akci?', 'Má to smysl u prášku, který znáte a užíváte pravidelně. Počítejte, kolik porcí spotřebujete za měsíc, a podle toho zvolte velikost balení. Příchutě na zkoušku si raději kupte v malém balení.'),
        ('Jak spočítám cenu za gram bílkovin?', 'Vynásobte hmotnost balení podílem bílkovin v prášku uvedeným na etiketě a získáte celkové gramy bílkovin. Cenu balení vydělte tímto číslem. Takto porovnáte koncentrát s izolátem nebo gainerem, které mají jiný obsah bílkovin.'),
        ('Dává smysl dárek zdarma, třeba šejkr?', 'Jen pokud ho opravdu použijete. Dárek je často způsob, jak obchod zvýší hodnotu košíku, aniž by snížil cenu. Porovnejte celkovou cenu s nabídkou bez dárku u jiného obchodu a rozhodněte podle ní.'),
        ('Kdy se proteiny zlevňují nejvíc?', 'Největší vlny bývají kolem konce listopadu, po Novém roce a před jarní sezónou. Menší akce se objevují při změně obalu nebo receptury. Pokud nepospícháte, na tyto termíny počkejte.'),
        ('Je levnější protein stejný jako dražší?', 'Ne vždy. Liší se typ bílkoviny, podíl bílkovin na porci, sladidla i chuť. Levnější koncentrát může být stejně dobrý pro běžné užívání, ale nelze ho přímo srovnat s izolátem. Rozhoduje složení na etiketě, nikoli cena.'),
        ('Mohu v akci kupovat i rostlinné proteiny?', 'Ano, ale s opatrností. Rostlinné směsi mají výraznější chuť a konzistenci, proto je dobré nejdřív vyzkoušet malé balení. Teprve když vám chuť vyhovuje, využijte akci na větší kus.'),
        ('Co dělat, když protein přijde s krátkou trvanlivostí?', 'Napište obchodu a ověřte, zda zboží odpovídá popisu. Pokud datum není uvedeno, máte právo na informaci před nákupem. Při velmi krátké expiraci můžete využít zákonné možnosti odstoupení od smlouvy při online nákupu.'),
        ('Jsou slevy na tyčinky a snacky stejné jako na prášek?', 'Obvykle ne. Tyčinky mají kratší trvanlivost a zlevňují se častěji kvůli výprodeji. Kupte je v takovém množství, které sníte v řádu týdnů, a před nákupem se podívejte na složení a obsah cukrů.'),
    ])

# ------------------------------------------------------------------ bila-sportovni-podprsenka
NEW['bila-sportovni-podprsenka'] = dict(
    title='Bílá sportovní podprsenka: průsvitnost a praní',
    desc='Bílá sportovní podprsenka: na co si dát pozor u průsvitnosti, potu a žloutnutí, jak ji kombinovat a prát. Srovnání nabídek českých obchodů.',
    intro='<p>Bílá sportovní podprsenka vypadá čistě a svěže, ale je nejnáročnější barvou na materiál i péči. Světlá tkanina prosvítá, na potu a deodorantu časem žloutne a každá skvrna je vidět. Zároveň se hodí pod světlé topy, k bílým teniskám i ke všem barvám legín. '
          'Tato stránka shromažďuje bílé modely z kategorie <a href="/sportovni-podprsenky/">sportovní podprsenky</a>, od jemných topů na jógu po pevné modely na běh. Průvodce vysvětluje, jak poznat dvouvrstvý materiál, co dělat s průsvitností, jak bílou podprsenku prát, aby nezešedla, a s čím ji kombinovat. '
          'Mezi bílými modely se objevují značky jako <a href="/znacka/champion/">Champion</a>, <a href="/znacka/adidas/">Adidas</a> nebo <a href="/znacka/reebok/">Reebok</a>. Míru podpory podle sportu najdete v hlavní kategorii.</p>',
    guide='<h2>Proč právě bílá a čím je jiná</h2>'
          '<p>Barva podprsenky nemění její podporu ani střih, mění ale praktické chování látky. Bílá odráží světlo a v létě se na slunci méně přehřívá než černá nebo tmavě modrá. Pod bílým tričkem nebo tílkem je navíc méně znatelná než tmavá, protože tmavá vrstva pod světlým oblečením vytváří kontrast. Naopak je ze všech barev nejméně odpustivá k potu, make-upu, hlíně i kapkám deodorantu a po několika praních může ztratit čistě bílý odstín.</p>'
          + T(['Vlastnost', 'Bílá', 'Proč to záleží'], [
              ['Průsvitnost', 'vyšší u jednovrstvých látek', 'rozhoduje při cvičení v bílém tričku i při ostrém světle'],
              ['Viditelnost skvrn', 'největší ze všech barev', 'pot, deodorant a make-up nejsou skryté'],
              ['Přehřívání na slunci', 'nižší než u tmavých barev', 'příjemnější při venkovním běhu a v létě'],
              ['Kombinace', 'jde ke všemu světlému i tmavému', 'hodí se jako základní kus výbavy'],
              ['Odolnost proti zešednutí', 'nižší při praní s tmavým prádlem', 'vyžaduje samostatné praní'],
              ['Pod světlým oblečením', 'může prosvítat jako světlá plocha', 'pod bílým tričkem je méně vidět tělový odstín']]) +
          '<p>Bílá je proto vhodná pro ty, kdo mají podprsenku jako viditelnou součást outfitu nebo ji kombinují se světlým tílkem. Jestliže hledáte skrytou podprsenku pod průsvitnými tričky, hledejte spíš tělové odstíny. U cvičení v samostatném topu je bílá nejatraktivnější varianta.</p>'
          '<h2>Průsvitnost: jak ji poznat před nákupem</h2>'
          '<p>Průsvitnost je největší slabinou světlé sportovní podprsenky, zvlášť po natažení látky při pohybu. U fotografií na e-shopu je ještě těžší ji odhadnout. Existuje několik vodítek, jak se vyhnout nepříjemnému překvapení.</p>'
          '<ul><li><strong>Dvouvrstvý přední díl:</strong> podšité košíčky nebo zdvojená přední část látku zpevní a skryjí tvar tělesných detailů.</li>'
          '<li><strong>Hustší úplet:</strong> kompresní materiál s vyšším podílem elastanu je při natažení méně průhledný než jemný pletený topík.</li>'
          '<li><strong>Vyjímatelné vycpávky:</strong> odnímatelné košíčky vytvářejí vrstvu, která pomáhá, ale při praní se někdy posunou.</li>'
          '<li><strong>Popis produktu:</strong> pokud popis zmiňuje podšívku nebo neprůsvitný materiál, je to dobré znamení. Chybí-li, hledejte fotografie z různých úhlů.</li>'
          '<li><strong>Recenze a otázky:</strong> kupující často napíšou, zda se bílá po natažení nepřesvítá.</li></ul>'
          '<p>Při zkoušce doma si podprsenku oblečte před oknem na denním světle a mírně se předkloňte. Pokud neprosvítá, je to pro většinu situací dostačující. Pro klidné cvičení stačí méně, pro běh venku je dobré mít jistotu.</p>'
          '<h2>Míra podpory a střih nezávisí na barvě</h2>'
          '<p>Barva je poslední kritérium, když už máte vybranou míru podpory. Nejprve rozhodněte, jestli potřebujete nízkou, střední nebo vysokou podporu podle sportu, a teprve pak zvolte barvu. Bílé modely se vyskytují ve všech skupinách. Jemné topy bez kostic jsou vhodné na jógu a pilates, střední podporu najdete u modelů pro posilovnu a kolo, vysokou podporu u kompresních a zapouzdřených střihů pro běh. Podrobný přehled střihů a velikostí je v hlavní kategorii <a href="/sportovni-podprsenky/">sportovní podprsenky</a>.</p>'
          '<p>Jakmile vám sedí střih, zjistěte, zda výrobce nabízí stejný model i v jiné barvě. Mnohé řady mají bílou, černou a několik sezónních odstínů. Bílou a černou verzi si pak můžete střídat a při praní je rozdělit na dvě várky. To je nejjednodušší způsob, jak zabránit zešednutí.</p>'
          '<h2>Jak prát bílou sportovní podprsenku</h2>'
          '<p>Správná péče rozhoduje o tom, jestli zůstane bílá, nebo za pár měsíců zežloutne či zešedne. Elastické vlákno nesnáší vysokou teplotu ani agresivní chemii, takže ani u bílé nesáhněte po drastických postupech.</p>'
          '<ol><li><strong>Perte hned po tréninku.</strong> Zaschlý pot je hlavní příčinou žloutnutí, protože reaguje s deodorantem.</li>'
          '<li><strong>Perte odděleně od barevného prádla.</strong> Barva z tmavých kousků se přenáší a světlou tkaninu zašedí.</li>'
          '<li><strong>Zvolte jemný program do čtyřiceti stupňů</strong> a prací prostředek určený pro sportovní nebo jemné prádlo.</li>'
          '<li><strong>Nepoužívejte aviváž.</strong> Ucpává póry materiálu, snižuje odvod potu a podporuje zápach.</li>'
          '<li><strong>Vyhněte se chlóru a silným odbarvovačům.</strong> Poškozují elastan a mohou vlákno zbarvit do žluta.</li>'
          '<li><strong>Sušte na vzduchu a mimo přímé slunce.</strong> Sušička a radiátor poškozují pružnost.</li></ol>'
          '<p>Na skvrny od deodorantu a potu pomůže namočení ve vodě s trochou jemného pracího prostředku nebo jemné mýdlo na skvrny, a slabý roztok kyseliny citronové zmírní zežloutlé stopy. Vždy se řiďte pokyny na štítku konkrétního kusu a zkuste postup nejprve na nenápadném místě. Praní v pračce se doporučuje v ochranném pytlíku, aby se háčky a ramínka nezachytily o ostatní prádlo.</p>'
          '<h2>S čím bílou podprsenku kombinovat</h2>'
          '<p>Díky neutrální barvě se bílá podprsenka hodí k téměř všemu. Rozdíl je v tom, jak výrazně má vyniknout a jak chcete být vidět.</p>'
          + T(['Kombinace', 'Efekt', 'Poznámka'], [
              ['S černými legínami', 'výrazný kontrast, sportovní vzhled', 'klasika pro posilovnu a jógu, viz <a href="/cerne-leginy/">černé legíny</a>'],
              ['S barevnými legínami', 'bílá zklidní výraznou barvu', 'hodí se k pastelovým i sytým odstínům'],
              ['S bílým tílkem', 'jednolitý světlý look', 'pozor na vzájemné prosvítání, viz <a href="/tilka/">tílka a topy</a>'],
              ['Pod volným tričkem', 'podprsenka je skrytá', 'tělový odstín je diskrétnější'],
              ['Se šedou mikinou', 'jemný kontrast při cestě na trénink', 'bílý lem může vykukovat z výstřihu']]) +
          '<p>Další oblečení, které tvoří sadu s podprsenkou, najdete v kategoriích <a href="/leginy/">legíny</a> a <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>. Pro stejný model a stejnou značku se vyplatí prohlédnout nabídky jednotlivých výrobců, třeba <a href="/sportovni-podprsenka-nike/">sportovní podprsenky Nike</a>, <a href="/sportovni-podprsenka-under-armour/">Under Armour</a> a <a href="/sportovni-podprsenka-calvin-klein/">Calvin Klein</a>.</p>'
          '<h2>Bílá podle sportu</h2><p>U jógy a pilates je bílá nejsnazší: pohyb je klidný, pot minimální a světlý top působí lehce. V posilovně se naopak často setkáte s dotykem činky, lavice a kovových částí, které světlou látku špiní, proto se vyplatí mít po ruce ručník. Při běhu venku hrozí stříkance bláta a pot v horku, ale světlá barva je ve slunci chladnější a v šeru lépe viditelná. Při kole nebo turistice pod funkční vrstvou se barva podprsenky skoro neprojeví, proto tu rozhoduje hlavně střih a švy. Pro tanec a aerobik, kde je podprsenka vidět, je bílá oblíbená pro čistý vzhled.</p><h2>Značky a jejich bílé modely</h2>'
          '<p>Bílou variantu dnes nabízí většina výrobců sportovního oblečení. V nabídce najdete <a href="/znacka/champion/">Champion</a> s pohodlnými tréninkovými topy, <a href="/znacka/adidas/">Adidas</a> a <a href="/znacka/reebok/">Reebok</a> s tradičními sportovními střihy, <a href="/znacka/nike/">Nike</a>, <a href="/znacka/puma/">Puma</a> a <a href="/znacka/under-armour/">Under Armour</a> s modely pro aktivnější sporty, ale i <a href="/znacka/craft/">Craft</a>, <a href="/znacka/kari-traa/">Kari Traa</a>, <a href="/znacka/dare2b/">Dare2b</a>, <a href="/znacka/athlecia/">Athlecia</a> a <a href="/znacka/gymbeam/">GymBeam</a>. Střihy a velikostní tabulky se mezi značkami liší, takže u každé zkontrolujte vlastní tabulku podle obvodu pod prsy a výšky košíčku. Zda je daný model skladem v bílé v právě vaší velikosti, ukáže přehled obchodů u konkrétního produktu.</p>'
          '<h2>Na co se zaměřit při výběru</h2>'
          '<ul><li><strong>Materiál:</strong> směs polyamidu nebo polyesteru s elastanem odvádí pot a drží tvar, bavlněné topy jsou příjemné na pohodu, ale při intenzivním cvičení nasáknou.</li>'
          '<li><strong>Švy:</strong> bezešvé nebo ploché švy se u světlé látky méně otlačují a nedělají na kůži stopy.</li>'
          '<li><strong>Zapínání:</strong> zadní zapínání usnadňuje nastavení, přes hlavu se obléká rychleji, ale pevný střih se hůř svléká.</li>'
          '<li><strong>Ramínka:</strong> široká ramínka rozloží tlak, zkřížená záda dají volnost pohybu paží.</li>'
          '<li><strong>Štítky a nášivky:</strong> měkké nebo potištěné štítky netlačí a nedráždí kůži.</li></ul>'
          '<p>Při pochybnostech o střihu vyberte raději pevnější model než volnější. Světlý a příliš měkký top se po natažení znatelně přesvítí. Naopak pevný dvouvrstvý střih je u bílé nejpraktičtější volba.</p>',
    faq=[
        ('Prosvítá bílá sportovní podprsenka?', 'Záleží na materiálu. Jednovrstvé jemné úplety po natažení prosvítají, zatímco dvouvrstvé nebo podšité modely výrazně méně. Před koupí hledejte v popisu podšívku nebo vyjímatelné košíčky a pročtěte si recenze. Doma zkoušejte na denním světle.'),
        ('Čím se liší bílá od tělové podprsenky pod světlým tričkem?', 'Tělová barva splyne s pokožkou, a proto je pod tenkým bílým tričkem méně vidět. Čistě bílá může pod látkou prosvítat jako jasná plocha. Bílá je vhodnější jako viditelná součást oblečení při cvičení.'),
        ('Proč bílá sportovní podprsenka žloutne?', 'Pot a zbytky deodorantu zaschnou ve vláknech a reagují s teplem nebo sluncem. Pomáhá praní ihned po tréninku, jemný prací prostředek a sušení ve stínu. Aviváž a chlór žloutnutí spíše zhoršují.'),
        ('Mohu bílou podprsenku prát spolu s bílým tričkem?', 'Ano, pokud jsou oba kusy z podobného materiálu a čistě bílé. Doporučuje se jemný program a ochranný pytlíček. Nikdy ji neperte s tmavým nebo barevným prádlem, které pouští barvu.'),
        ('Je bílá barva vhodná na běh?', 'Ano, pokud má model dostatečnou podporu a nepřesvítá. Světlá barva je v létě příjemná na slunci. Venku je ale vidět každá skvrna od bláta nebo deště, takže počítejte s častějším praním.'),
        ('Dá se použít bělidlo?', 'Chlórová a jiná silná bělidla se nedoporučují. Poškozují elastické vlákno a mohou způsobit nažloutlý nádech. Použijte mýdlo na skvrny, jemný prací prostředek a výrobcem povolené metody uvedené na štítku.'),
        ('Kolik bílých podprsenek mít?', 'Praktické je mít alespoň dva kusy na střídání, abyste mohli po každém tréninku jednu prát. Bílou a černou nebo jinou tmavou variantu pak perete zvlášť a obě déle vydrží.'),
        ('Jak velikost sportovní podprsenky změřit?', 'Změřte obvod pod prsy pevně, ale bez zařezávání, a obvod v nejplnějším místě. Hodnoty porovnejte s tabulkou konkrétní značky, protože S, M a L se mezi výrobci liší. Pás má držet většinu podpory.'),
        ('Hodí se bílá podprsenka pro děti a dospívající?', 'Ano, ale pro dívky je důležitá velikost a pohodlí, ne barva. Dětské a dívčí modely mají jiné velikostní řady a často měkčí střih. Podle délky těla i obvodu hrudníku zvolte tabulku určenou pro mládež.'),
        ('Jak dlouho bílá sportovní podprsenka vydrží?', 'Při správné péči i několik sezón. Elastan se časem unavuje, takže když pás povolí nebo podprsenka přestane držet, je čas na výměnu bez ohledu na barvu. Střídání více kusů prodlouží životnost každého.'),
    ])

# ------------------------------------------------------------------ hannah-lyzarska-bunda
NEW['hannah-lyzarska-bunda'] = dict(
    title='Hannah lyžařská bunda: sortiment a výběr modelu',
    desc='Hannah lyžařská bunda pro muže, ženy i děti: jak číst názvy modelů, rozdíl mezi membránou a bez ní, velikosti a srovnání s Kilpi či Alpine Pro.',
    intro='<p>Hannah patří k českým značkám outdoorového a lyžařského oblečení a její bundy se na svazích potkávají u dospělých i dětí. Model se pozná podle jména, například Ritta, Xavier nebo Kigali, a podle toho, zda má membránu, zateplení a střih pro muže, ženy nebo juniory. '
          'Tato stránka ukazuje bundy značky <a href="/znacka/hannah/">Hannah</a> z kategorie <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>. Průvodce vysvětluje, jak číst popisy, co znamená označení s membránou, jak vybrat velikost pro dospělé a růst dětskou, a v čem se Hannah liší od jiných značek jako <a href="/znacka/kilpi/">Kilpi</a> nebo <a href="/znacka/alpine-pro/">Alpine Pro</a>. Konkrétní popis vždy ověřte, protože sortiment se mezi obchody i sezónami střídá, a stejný model se může objevit v několika barvách i velikostních řadách.</p>',
    guide='<h2>Hannah v kostce: pro koho je a co nabízí</h2>'
          '<p>Hannah je česká značka, jejíž oblečení je zaměřené na rekreační pohyb v horách: turistiku, lyžování, zimní procházky a cestování. V kategorii lyžařských bund najdete modely pro muže, ženy i děti, v typických zimních barvách i ve výraznějších odstínech, které se hodí do sněhu. Značka se obvykle drží praktického střihu a běžného zimního použití, ne extrémního freeridu. Pokud hledáte bundu pro víkendové lyžování, svah s vlekem, dětskou lyžařskou školu nebo zimní dovolenou, je to rozumná volba. Pro náročné skialpové túry nebo hluboký prašan jsou vhodnější specializované skořepiny. Základní průvodce konstrukcí bund najdete v hlavní kategorii <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>.</p>'
          + T(['Skupina', 'Co v popisu hledat', 'Poznámka'], [
              ['Pánské modely', 'označení Pánská lyžařská bunda', 'střih pro širší ramena a delší rukávy'],
              ['Dámské modely', 'označení Dámská lyžařská bunda', 'užší pas, kratší rukávy, často výraznější barvy'],
              ['Dětské a juniorské', 'označení JR nebo Dětská a rozmezí výšky', 'velikost podle výšky dítěte, ne věku'],
              ['S membránou', 'výslovně uvedeno s membránou', 'zvýšená odolnost proti vlhkosti'],
              ['Bez uvedené membrány', 'v názvu nic není', 'zateplená bunda s ochranou proti větru a drobné vlhkosti']]) +
          '<p>Většina názvů začíná jménem modelu, po kterém následuje druh a barva. Stejné jméno se někdy objeví ve více barevných variantách, tak si u každého kusu zkontrolujte, zda jde o pánský, dámský nebo dětský střih. Označení JR u dětí a juniorů se v katalogu objevuje velmi často.</p>'
          '<h2>Membrána, nebo bez ní</h2>'
          '<p>Nejdůležitější rozdíl mezi modely stejné značky je přítomnost membrány. Membrána je tenká vrstva, která zadržuje vodu zvenčí a propouští vodní páru zevnitř. U lyžařské bundy znamená, že vám neprosákne mokrý sníh a že se při pohybu uvnitř méně zapaříte. U bundy bez uvedené membrány se spoléhá hlavně na impregnaci tkaniny a těsné švy. Obě varianty mají své místo.</p>'
          + T(['Podmínky', 'Vhodnější volba', 'Důvod'], [
              ['suchý mráz, slunečný svah', 'zateplená bunda bez membrány nebo s lehkou', 'dobře izoluje a je lehčí'],
              ['mokrý sníh, mlha, tání', 'bunda s membránou', 'lépe zadrží vlhkost a vítr'],
              ['dlouhé stání, výuka dětí', 'zateplená s kapucí', 'důležité je teplo'],
              ['intenzivní jízda a pot', 'membrána a větrací zipy', 'odvod páry je důležitější než teplo'],
              ['městský zimní provoz', 'lehčí zateplená', 'lyžařské detaily nejsou nutné']]) +
          '<p>Odolnost tkaniny proti vodě se vyjadřuje hodnotou vodního sloupce a prodyšnost hodnotou propustnosti páry. Vyšší číslo značí lepší vlastnost, ale bez ohledu na čísla musí být bunda dobře ušitá. Zajímejte se, zda jsou švy zatmelené a zipy kryté chlopní, jinak voda proniká i skrz kvalitní materiál. Podrobně jsou principy popsané v hlavním průvodci kategorie.</p>'
          '<h2>Velikost: dospělí, ženy a děti</h2>'
          '<p>Bunda se při lyžování nosí přes několik vrstev, proto by neměla být upnutá. Zároveň nesmí být tak volná, aby ve větru vlála a nasávala sníh. Dospělí si zvolí velikost podle obvodu hrudníku a délky rukávu a tabulku vždy ověří u konkrétního produktu. Při váhání vyberte spíše větší velikost, pod kterou se vejde fleece, než těsnou, v níž se špatně hýbou ramena.</p>'
          '<p>U dětí rozhoduje výška, ne věk. Dětské modely mají čísla jako 116, 122, 134, 146 nebo 158 a vždy jde o rozmezí výšky v centimetrech. Dítě v pohybu potřebuje mít rukávy dostatečně dlouhé, aby se při předklonu nesunuly nahoru, ale ne tak dlouhé, aby se zasouvaly přes rukavice.</p>'
          + T(['Výška dítěte', 'Typická řada velikostí', 'Poznámka'], [
              ['do zhruba 110 cm', '104 až 110', 'nejmenší děti, nejdůležitější je pohodlí'],
              ['zhruba 116 až 128 cm', '116 až 128', 'začínající lyžaři, ověřte délku rukávu'],
              ['zhruba 134 až 146 cm', '134 až 146', 'prostor pro růst v dalších sezónách'],
              ['zhruba 152 až 164 cm', '152 až 164', 'přechod na dospělé střihy']]) +
          '<p>Rezerva na růst by neměla přesáhnout jednu velikost. Příliš velká bunda dítěti překáží, vlaje a ruce se ztrácí v rukávech. Mnoho dětských bund má prodloužitelné rukávy nebo nastavitelné manžety, tato vlastnost sezónu navíc prodlouží. Kombinujte ji s kvalitními rukavicemi z kategorie <a href="/detske-lyzarske-rukavice/">dětské lyžařské rukavice</a> a s přilbou z přehledu <a href="/detske-lyzarske-helmy/">dětské lyžařské helmy</a>.</p>'
          '<h2>Čeští výrobci: Hannah, Kilpi a Alpine Pro</h2>'
          '<p>Hannah, <a href="/znacka/kilpi/">Kilpi</a> i <a href="/znacka/alpine-pro/">Alpine Pro</a> jsou české značky, které mají v obchodech velké zastoupení. Všechny cílí na rekreační lyžaře a turisty, takže se jejich nabídky částečně překrývají. Rozdíl najdete v detailech: střih, barevná paleta, zakončení kapes, tvar kapuce nebo velikostní tabulka. Neexistuje obecné pravidlo, že jedna značka je lepší, takže při srovnání se dívejte na konkrétní model, jeho materiál a popis. Srovnání jednotlivých nabídek jsou na stránkách <a href="/kilpi-lyzarska-bunda/">Kilpi lyžařská bunda</a> a <a href="/alpine-pro-lyzarska-bunda/">Alpine Pro lyžařská bunda</a>.</p>'
          '<p>Pokud chcete poznat jiný přístup, porovnejte s norskou značkou <a href="/znacka/helly-hansen/">Helly Hansen</a>, která je zaměřená spíš na technické horské oblečení, nebo s americkou značkou <a href="/znacka/columbia/">Columbia</a>. Srovnávací stránky jsou <a href="/helly-hansen-lyzarska-bunda/">Helly Hansen lyžařská bunda</a> a <a href="/lyzarska-bunda-columbia/">lyžařská bunda Columbia</a>. Střihy se mezi výrobci liší v délce těla a šířce ramen, proto se vždy držte tabulky výrobce a nespoléhejte na zkušenost s jinou značkou.</p>'
          '<h2>Jak vybrat konkrétní model Hannah</h2>'
          '<ol><li><strong>Určete skupinu:</strong> pánský, dámský nebo dětský střih. Stejný název modelu se může lišit podle pohlaví.</li>'
          '<li><strong>Rozhodněte se pro membránu.</strong> Pro mokrý sníh a časté lyžování je výhodnější, pro slunečné dny stačí lehčí zateplená bunda.</li>'
          '<li><strong>Zkontrolujte výbavu:</strong> sněhová sukně, kapuce přes helmu, větrací zipy, kapsa na skipas a manžety s palcovým otvorem.</li>'
          '<li><strong>Vyberte barvu:</strong> výrazná se lépe najde na svahu, tmavá je univerzálnější a lépe se kombinuje.</li>'
          '<li><strong>Porovnejte obchody:</strong> stejný model nabízí více prodejců a v každém jsou skladem jiné velikosti.</li></ol>'
          '<h2>Barva a viditelnost na svahu</h2><p>Na svahu hraje barva i bezpečnostní roli. Výrazná bunda v růžové, oranžové nebo žluté se z dálky dobře vidí, což ocení rodiče hledající dítě ve skupině lyžařské školy. Černá, šedá a tmavě modrá jsou univerzální a méně špiní, ale v mlze a při šeru splývají s okolím. V katalogu značky najdete obě skupiny, takže si vyberte podle toho, kdo bude bundu nosit a jak často.</p><h2>Co k bundě přikoupit</h2>'
          '<p>Hannah nabízí i další lyžařské oblečení a bunda často tvoří sadu s kalhotami. Návazný výběr je v kategorii <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a> a na stránce <a href="/hannah-lyzarske-kalhoty/">Hannah lyžařské kalhoty</a>. Pod bundu se hodí <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a> a pro ruce <a href="/lyzarske-rukavice/">lyžařské rukavice</a>. Chráníte-li hlavu, projděte <a href="/lyzarske-helmy/">lyžařské helmy</a>. Pokud bundu nepotřebujete jen na sjezdovku, zvažte i lehčí <a href="/softshellove-bundy/">softshellové bundy</a>.</p>'
          '<h2>Péče o lyžařskou bundu</h2>'
          '<p>Bunda zachová své vlastnosti, pokud ji správně vyperete. Nejprve zavřete všechny zipy a suché zipy a vyndejte věci z kapes. Perte ji na nízké teplotě s jemným pracím prostředkem určeným pro funkční oblečení, bez aviváže, která zalepuje póry membrány. Po vyprání ji pověste a nechte uschnout, nebo ji podle štítku krátce dosušte při nižší teplotě, což pomáhá obnovit impregnaci. Když tkanina začne nasávat vodu místo toho, aby ji odpuzovala, obnovte impregnaci speciálním přípravkem. Před uložením na léto bundu čistou a suchou pověste na ramínko, nesbalujte ji pevně do pytle.</p>',
    faq=[
        ('Pro koho jsou lyžařské bundy Hannah vhodné?', 'Pro rekreační lyžaře, rodiny s dětmi, turisty a všechny, kdo tráví zimní den na sjezdovce nebo v horách. Sortiment pokrývá pánské, dámské i dětské střihy. Pro extrémní freeride nebo skialpinismus je vhodnější specializovaná skořepinová bunda.'),
        ('Jak poznám, zda má bunda membránu?', 'V názvu nebo popisu je uvedeno slovo membrána. Pokud chybí, počítejte s tkaninou s impregnací a zateplením. Membrána pomáhá hlavně v mokrém sněhu a při intenzivní jízdě, kdy je důležitý odvod vlhkosti.'),
        ('Podle čeho zvolit velikost dětské bundy?', 'Podle výšky dítěte, nikoli věku. Změřte dítě bez bot a porovnejte se tabulkou výrobce. Rezerva na růst by měla být nanejvýš jedna velikost, jinak bunda překáží při pohybu.'),
        ('Co znamená označení JR v názvu?', 'Je to zkratka pro junior a označuje dětský nebo mládežnický střih. Takové modely mají jiné proporce než dospělé velikosti. Vždy ověřte rozmezí výšky v centimetrech, na které je bunda určená.'),
        ('Je Hannah lepší než Kilpi nebo Alpine Pro?', 'Všechny tři značky jsou české a zaměřené na rekreační lyžaře. Rozdíly jsou v detailech střihu, barvách a konkrétních modelech. Nelze říct, že jedna je obecně lepší, rozhodněte podle popisu a velikosti.'),
        ('Dá se v bundě Hannah jezdit i na snowboardu?', 'Ano, pokud vám sedí střih. Snowboardisté obvykle preferují volnější bundu s delším tělem a hlubšími kapsami. Zkontrolujte, zda je materiál odolný na sezení a zda kapuce sedí přes helmu.'),
        ('Můžu bundu používat i mimo svah?', 'Ano, zateplená lyžařská bunda funguje i v zimě ve městě nebo na procházku. Je ale konstruovaná pro pohyb ve sněhu, takže v městských podmínkách se může zdát výrazně teplejší. Pro jarní lyžování zvažte lehčí vrstvy.'),
        ('Jak bundu prát, aby vydržela?', 'Perte ji na nízké teplotě s jemným prostředkem určeným pro funkční oblečení, bez aviváže. Po vyprání bundu nechte uschnout na vzduchu nebo ji dosušte podle štítku. Impregnaci obnovte, když přestane odpuzovat vodu.'),
        ('Jaká vrstva patří pod lyžařskou bundu?', 'Funkční termoprádlo na tělo a fleece nebo lehká izolační vrstva podle počasí. Bavlněné tričko se nehodí, protože drží vlhkost. Při mrazu přidejte silnější střední vrstvu, při jarním lyžování stačí tenké funkční triko.'),
        ('Kde koupit bundu Hannah ve správné velikosti?', 'Porovnejte nabídky obchodů u konkrétního modelu. V každém jsou skladem jiné velikosti a barvy. Sportek vám ukáže, kde je právě vaše velikost k dispozici a jaké jsou podmínky dopravy.'),
    ])

# ------------------------------------------------------------------ boxerske-rukavice-venum
NEW['boxerske-rukavice-venum'] = dict(
    title='Boxerské rukavice Venum: řady, unce a srovnání',
    desc='Boxerské rukavice Venum: rozdíl mezi řadami Challenger, Contender a Elite, volba uncí, dětské a MMA modely i srovnání s Leone, Fairtex a DBX Bushido.',
    intro='<p>Venum je značka specializovaná na bojové sporty a její rukavice patří k nejčastěji hledaným v nabídkách českých obchodů. Modely se jmenují Challenger, Contender, Elite, Giant nebo Impact a každý z nich míří na jiného cvičence. Jinou rukavici vezme začátečník na trénink do klubu, jinou sparingový partner nebo dítě v kroužku. '
          'Tato stránka shrnuje rukavice značky <a href="/znacka/venum/">Venum</a> z kategorie <a href="/boxerske-rukavice/">boxerské rukavice</a>. Průvodce vysvětluje, jak se řady přibližně liší, kolik uncí zvolit, co je u syntetické kůže důležité, jak vybrat dětský model a čím se Venum liší od značek jako Leone 1947, Fairtex nebo DBX Bushido. Údaje o konkrétním modelu vždy ověřte v popisu.</p>',
    guide='<h2>Venum a jeho rukavice</h2>'
          '<p>Venum se zaměřuje na bojové sporty včetně MMA, thajského boxu a boxu. Kromě rukavic nabízí také oblečení, chrániče a doplňky pro trénink. Rukavice mívají výrazný design, od klasických jednobarevných po maskáčové a barevné kombinace, a velká část nabídky se prodává s popisem trénink nebo sparing. Pro většinu lidí je důležitější než vzhled to, jak rukavice drží ruku, jaká je vycpávka a jak dobře se zapíná. Obecné rady ke všem značkám najdete v kategorii <a href="/boxerske-rukavice/">boxerské rukavice</a>, tady jde o to, co je u Venum specifické.</p>'
          + T(['Řada', 'Obecné zaměření', 'Pro koho'], [
              ['Challenger', 'základní řada pro pravidelný trénink', 'začátečníci a rekreační boxeři'],
              ['Contender', 'středně pokročilý trénink, pytel a lapy', 'cvičenci s pravidelnou docházkou'],
              ['Elite', 'vyšší řada s důrazem na zpracování', 'pokročilí a ti, kdo dbají na vzhled'],
              ['Giant a Impact', 'tréninkové a sparingové modely', 'těžší sportovci a delší tréninky'],
              ['Kids a Junior', 'zmenšené rukavice pro děti', 'děti v kroužcích bojových sportů'],
              ['MMA rukavice', 'otevřené prsty, tenká vycpávka', 'MMA a grappling, ne klasický box']]) +
          '<p>Rozdělení je orientační. Přesné parametry se u jednotlivých verzí mění a stejná řada existuje často v několika generacích, například Challenger 3.0 a 4.0. Nenechte se zmást číslem v názvu: vyšší číslo je novější verze, ale není automaticky lepší pro vás. Podívejte se na popis a recenze konkrétního kusu a porovnejte, jaké uncové velikosti jsou skladem.</p>'
          '<h2>Jak vybrat uncovou velikost u Venum</h2>'
          '<p>Hmotnost rukavice se udává v uncích a u Venum se obvykle prodává v řadě od deseti po šestnáct uncí, u některých modelů i víc. Pro dospělého začátečníka je nejčastější volba dvanáct uncí pro pytel a lapy a čtrnáct nebo šestnáct pro sparing. Menší rukavice jsou rychlejší, ale méně chrání ruce i soupeře. Větší jsou těžší a při dlouhém tréninku unavují ramena.</p>'
          + T(['Vaše situace', 'Doporučená unce', 'Důvod'], [
              ['Lehčí dospělý, trénink na pytel', 'kolem deseti až dvanácti', 'rychlost a cit'],
              ['Průměrný dospělý, univerzální trénink', 'dvanáct', 'kompromis mezi ochranou a rychlostí'],
              ['Sparing nebo těžší postava', 'čtrnáct až šestnáct', 'více vycpávky pro obě strany'],
              ['Dítě v kroužku', 'čtyři až osm podle věku a rozměru dlaně', 'rukavice nesmí být příliš velká'],
              ['Soutěž', 'podle pravidel svazu', 'předepsaná hmotnost podle váhové kategorie']]) +
          '<p>Vždy zvažte, kdo bude rukavice používat a k čemu. Společná rukavice pro pytel a sparing neexistuje, ale čtrnáct uncí je nejuniverzálnější kompromis. Pokud trénujete pod vedením trenéra, zeptejte se, jaké vybavení klub vyžaduje.</p>'
          '<h2>Zapínání, palec a velikost ruky</h2><p>Většina tréninkových rukavic se zapíná na suchý zip, který se nasazuje i sundává bez cizí pomoci. Šněrování se objevuje u soutěžních a tradičních modelů a bez partnera se zapíná těžko. Palec bývá přišitý k tělu rukavice, aby se nemohl vyvrknout, a zápěstní manžeta má být dostatečně dlouhá a pevná. Pokud se vám při sevření pěsti pálí kůže nebo rukavice při úderu klouže, je nejspíš špatně zvolená velikost. Velikosti S, M a L se mezi řadami liší a vázat se na ně nelze, proto zkontrolujte tabulku obvodu dlaně a doporučenou hmotnost sportovce. Rukavice by měla držet pěst pevně, ale nesmí tlačit v kloubech prstů.</p><p>Při koupi si ověřte, zda se do rukavice vejde bandáž. Bandážované zápěstí zabere víc místa a těsná rukavice se pak špatně nasazuje. Když budete rukavice nosit s dlouhými bandážemi, volte raději o stupeň větší velikost. Pro trénink pod vedením trenéra je dobré mít stejný model, jaký používají ostatní, protože se pak snáz srovnávají zkušenosti. Širší přehled bojových sportů najdete v kategorii <a href="/bojove-sporty/">bojové sporty</a>.</p><h2>Syntetická kůže a údržba</h2>'
          '<p>V popisech modelů Venum se často objevuje syntetická kůže, ale u vyšších řad najdete i pravou kůži. Syntetika je lehčí na údržbu, snáší pot a bývá dostupnější. Pravá kůže se časem přizpůsobí ruce, ale vyžaduje péči a delší rozcvičení. Pro začátečníky je rozumná syntetická verze, která snese základní zacházení. Rozhodující je kvalita švů, zapínání a vycpávky, ne samotný název materiálu.</p>'
          '<ul><li><strong>Po tréninku:</strong> rukavice vyvětrejte, nezavírejte je do tašky mokré.</li>'
          '<li><strong>Vnitřek:</strong> otřete vlhkým hadříkem a občas použijte dezinfekční sprej na sportovní výbavu.</li>'
          '<li><strong>Sušení:</strong> mimo radiátor a přímé slunce, teplo deformuje vycpávku.</li>'
          '<li><strong>Bandáže:</strong> používejte je při každém tréninku, ušetří rukavice od potu a vaše zápěstí od zátěže, viz <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</li>'
          '<li><strong>Skladování:</strong> na suchém a větraném místě, s rozevřeným zapínáním.</li></ul>'
          '<p>Rukavice, které čpí, jsou signálem, že se neosušily. Pomáhá pohlcovač pachu určený do rukavic nebo prosté vyvětrání po každém tréninku. Při dodržení těchto zásad vydrží rukavice několik let.</p>'
          '<h2>Dětské rukavice Venum</h2>'
          '<p>Venum nabízí dětské varianty známých řad, často s označením Kids. Děti potřebují rukavice, které odpovídají velikosti dlaně a jsou dostatečně pevně uchycené na zápěstí. Příliš velká rukavice nechrání, jen se kýve a může zranit prsty. Pro malé děti jde o hru a seznámení se sportem, pro starší o tréninky pod dohledem trenéra. Zvolte menší uncovou velikost, měkčí vycpávku a snadné zapínání. K rukavicím patří i ochrana zubů a ostatních částí těla, kterou najdete v přehledu <a href="/detske-chranice/">dětské chrániče</a>.</p>'
          '<h2>MMA a boxerské rukavice: nezaměňujte</h2>'
          '<p>Mezi nabídkami Venum najdete i MMA rukavice s otevřenými prsty. Jsou to jiný druh výbavy: mají tenkou vycpávku a umožňují úchop při grapplingu. Do klasického boxu se nehodí, protože chrání ruku slaběji a nejsou určené pro sparing s klasickou technikou. Pro pytel i box vyberte klasickou boxerskou rukavici. MMA model si kupte jen tehdy, pokud trénujete tento sport. Pokud chcete oblečení pro stejný sport, podívejte se do kategorie <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a>.</p>'
          '<h2>Venum a konkurence</h2>'
          '<p>Při výběru rukavic se vyplatí porovnat více značek. Mezi nimi jsou <a href="/znacka/dbx-bushido/">DBX Bushido</a> a <a href="/znacka/leone-1947/">Leone 1947</a> s evropským zaměřením, <a href="/znacka/fairtex/">Fairtex</a> s thajskou tradicí, <a href="/znacka/hayabusa/">Hayabusa</a> s důrazem na pokročilý trénink, <a href="/znacka/benlee/">Benlee</a> a <a href="/znacka/rdx/">RDX</a> s širokou nabídkou pro začátečníky. Rozdíly jsou v tvaru vycpávky, tuhosti palce a šířce rukavice. Někomu sedí užší rukavice, jiný potřebuje širší. Nejjistější je vyzkoušet, nebo si přečíst, jak model sedí lidem se stejným typem ruky.</p>'
          '<h2>Jak odlišit originál</h2>'
          '<p>Oblíbené značky bývají předmětem padělků. Pokud je cena výrazně nižší než u ostatních obchodů, buďte opatrní. Kontrolujte, zda obchod uvádí přesný název modelu a zda se obrázek shoduje. Všímejte si jednotného značení, rovného šití, pevného suchého zipu a čistě provedeného loga. Nákup u zavedeného prodejce s vratnou lhůtou je nejjednodušší cesta, jak se vyhnout nepříjemnému překvapení. Srovnání obchodů u konkrétního modelu pomůže poznat nejnižší cenu a důvěryhodného prodejce.</p>'
          '<h2>Co přikoupit k rukavicím</h2>'
          '<p>Rukavice samy nestačí. Pro trénink potřebujete <a href="/bandaze-a-ortezy/">bandáže</a>, chránič zubů a při sparingu i ostatní <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>. Pro samostatný trénink doma se hodí <a href="/boxovaci-pytle/">boxovací pytel</a>. Pokud rukavice vybíráte jako dárek, pomůže znát velikost ruky a úroveň sportovce, případně zvolit univerzální dvanáct nebo čtrnáct uncí. Ke každodennímu tréninku patří také pitný režim a případně <a href="/sportovni-vyziva/">sportovní výživa</a>, kterou je ale vhodné řešit až po rukavicích a základní výbavě.</p>',
    faq=[
        ('Jaký je rozdíl mezi řadami Challenger a Elite?', 'Challenger je základní tréninková řada pro začátečníky a rekreační boxery, Elite je vyšší řada s lepším zpracováním. Přesné parametry se liší podle generace a verze, proto se řiďte popisem konkrétního modelu a dostupností velikostí.'),
        ('Kolik uncí zvolit pro začátečníka?', 'Většina dospělých začíná u dvanácti uncí, které stačí na pytel i lapy. Pro sparing si přidejte čtrnáct nebo šestnáct uncí. Lehčí a menší lidé mohou začít u deseti, větší a těžší raději u čtrnácti.'),
        ('Hodí se Venum rukavice i na sparing?', 'Ano, pokud zvolíte dostatečně velkou uncovou velikost. Pro sparing se používají obvykle čtrnáct nebo šestnáct uncí. Nesparujte v malých rukavicích určených na pytel, protože chrání soupeře i vás méně.'),
        ('Je syntetická kůže horší než pravá?', 'Není horší, jen jiná. Syntetika je odolná, snáší pot a snadno se čistí. Pravá kůže je pohodlnější po rozcvičení, ale vyžaduje péči. Pro začátečníka je syntetická volba rozumná.'),
        ('Čím se liší MMA rukavice od boxerských?', 'MMA rukavice mají otevřené prsty a tenkou vycpávku, určené pro úchopy a údery v MMA. Boxerské rukavice mají větší vycpávku a chrání ruku při úderech do pytle i při sparingu. Nejsou zaměnitelné.'),
        ('Jak vybrat dětské rukavice Venum?', 'Podle velikosti dlaně a věku dítěte. Zvolte menší uncovou velikost, měkčí vycpávku a snadné zapínání. Příliš velká rukavice dítěti překáží. Pokud je dítě v kroužku, poraďte se s trenérem.'),
        ('Jak čistit a sušit boxerské rukavice?', 'Po tréninku je vyvětrejte a otřete vlhkým hadříkem. Nesušte je na radiátoru ani na přímém slunci, deformuje se tím vycpávka. Pomáhá pohlcovač vlhkosti a bandáže, které brání vnikání potu.'),
        ('Jsou rukavice Venum vhodné i pro ženy?', 'Ano, žádný model není omezen na pohlaví. Důležitější než označení je velikost ruky a hmotnost sportovce. Ženy a menší cvičenci často volí deset nebo dvanáct uncí pro pytel a čtrnáct pro sparing.'),
        ('Jak poznám padělek?', 'Padělky bývají výrazně levnější, mají nepřesné logo, slabé šití a špatné zapínání. Kupujte u ověřených prodejců, kontrolujte přesný název modelu a porovnejte ceny. Při pochybnostech se zeptejte obchodu na původ zboží.'),
        ('Co potřebuji k rukavicím kromě bandáží?', 'Pro trénink stačí bandáže a chránič zubů. Při sparingu přidejte další chrániče a případně přilbu. Na samostatný trénink se hodí pytel nebo lapy. Doplňky najdete v příbuzných kategoriích na Sportece.'),
    ])
