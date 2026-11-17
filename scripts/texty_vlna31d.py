"""sporteka.cz — wave 31d (17. 11. 2026): long texts for hokejove-rukavice, chranice-zubu, joga-bloky, kotouce-na-cinky,
zavazi-na-kotniky. General true facts only, no prices, no product counts.

Verified facts and sources:
- Hockey glove sizes in inches by category (YTH 8–9", JR 10–11", INT 12–13", SR 14–15" on Bauer's chart; other brands
  overlap, the catalogue has JR 12" and SR 13" models): Bauer size chart via prostockhockey.com/blog/hockey-glove-sizing-guide,
  hockeymonkey.com product pages. Fit types only described generally (traditional = roomier, tapered = snug;
  icewarehouse.com Tapered Glove Fit category). Palm material "nash" = generic synthetic suede, repalming offered by shops
  (prostockhockey.com/blog/pro-stock-hockey-gloves-palms, hejduksport.cz/en/repair-of-gloves). Drying without high heat.
- Mouthguard types stock / boil-and-bite / custom by dentist, stock = least adapted fit, braces under dentist supervision,
  replacement when worn: ada.org (Athletic mouth protectors), deltadental.com. SISU: hot but not boiling water, remouldable
  repeatedly per maker (sisuguard.com/faq, sisuguard.com/fitting).
- Yoga block standard ~9 × 6 × 3 in (≈ 23 × 15 × 7.5 cm, also a catalogue product name), 4 in thick variant; cork denser
  and heavier, foam lighter and slightly compressible (manduka.com guide to yoga blocks, asivanayoga.com).
- Olympic bar men 20 kg / 2200 mm / 28 mm grip / 50 mm sleeve, women 15 kg / 2010 mm / 25 mm (eleiko.com product sheets,
  crossliftor.com). IWF bumper colours 10 green, 15 yellow, 20 blue, 25 red, diameter 450 mm (roguefitness.com IWF plates,
  gymequipment.co.uk). Hole sizes 25 / 30–31 / 50–51 mm as seen in the catalogue names.
- Ankle weights: physiotherapists advise against running/brisk walking with them, use for controlled strength exercises,
  joint problems or osteoporosis → doctor/physio first (uhhospitals.org 2024, livestrong.com quoting a PT, Mayo Clinic via
  livestrong).
Left out (not verified): IWF colours of change plates and collars, exact age ranges per glove size, rules that make
mouthguards mandatory in specific Czech competitions, recommended number of yoga blocks.
Brands linked only if present in src/texts/znacky.json, the rest are plain text."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ hokejove-rukavice
NEW['hokejove-rukavice'] = dict(long=True,
    title='Hokejové rukavice YTH, JR, INT a SR: velikost a výběr',
    desc='Hokejové a hokejbalové rukavice Bauer, CCM, Warrior, Sherwood a Winnwell. Jak určit velikost v palcích, střih a materiál dlaně a jak je sušit.',
    intro='<p><strong>Hokejové rukavice</strong> chrání prsty, hřbet ruky a zápěstí před sekem hokejkou, zásahem pukem i pádem na led. Zvenku mají pevný plášť s pěnovými a plastovými výztuhami, dlaň je naopak tenká a měkká, aby hráč cítil hokejku. Prodávají se ve čtyřech věkových kategoriích, tedy YTH, JR, INT a SR, a velikost se udává v palcích. Kromě ledního hokeje se nosí i na hokejbal, kde je řada hráčů používá ve stejném provedení.</p>'
          '<p>Sporteka sbírá nabídky českých e-shopů, takže u konkrétního modelu vidíte, kdo ho má a ve kterých velikostech. Objednávka pak proběhne přímo v obchodě. V katalogu jsou rukavice značek '
          + B(('bauer', 'Bauer'), ('ccm', 'CCM'), ('winnwell', 'Winnwell')) +
          ', dále Warrior, Sherwood nebo Knapper. Rukavice patří do kategorie <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>, kde najdete i ramena, lokty a holeně.</p>',
    guide='<h2>Z čeho se hokejová rukavice skládá</h2>'
          '<p>Hřbet a prsty kryjí válce nebo segmenty z tvrdší pěny, často doplněné plastovými destičkami. Každý prst je rozdělený na několik dílů, aby se dal ohnout kolem hokejky. Palec mívá výztuhu, která brání jeho prudkému ohnutí dozadu. Na rukavici navazuje manžeta, tedy prodloužení kolem zápěstí, které má krýt mezeru mezi rukou a loketním chráničem. Dlaň je z tenkého syntetického materiálu a právě ona se opotřebuje nejdřív.</p>'
          '<p>Rukavice se liší hmotností, tuhostí a tím, jak volně se v nich hýbe zápěstí. Lehčí a pružnější modely vyhovují hráčům, kteří hodně pracují s pukem. Masivnější rukavice s vyšší manžetou volí ti, kdo chtějí víc krytí. Brankáři mají vlastní lapačku a vyrážečku, ty najdete v sekci <a href="/hokejove-brankarske-vybaveni/">brankářská výstroj</a>.</p>'
          '<h2>Velikosti v palcích podle kategorie</h2>'
          '<p>Číslo v palcích zhruba odpovídá délce rukavice. Kategorie YTH, JR, INT a SR rozlišují dětské, juniorské, přechodové a dospělé střihy. Tabulky se mezi výrobci liší a na hranách se překrývají, takže stejná velikost u Bauer a u Sherwood nemusí sedět úplně stejně.</p>'
          + T(['Kategorie', 'Obvyklé velikosti', 'Pro koho'], [
              ['YTH (youth)', '8" a 9"', 'nejmenší děti, první výstroj'],
              ['JR (junior)', '10" a 11", u některých značek i 12"', 'starší děti'],
              ['INT (intermediate)', '12" a 13"', 'dospívající a hráči s menší rukou'],
              ['SR (senior)', '13", 14" a 15"', 'dospělí']]) +
          '<p>Pro odhad velikosti se měří ruka od špičky prostředníčku směrem k zápěstí a výsledek se porovná s tabulkou dané značky. Každý výrobce má postup trochu jiný, proto se vyplatí přečíst jeho návod. Pokud vycházíte mezi dvěma čísly, rozhoduje délka manžety a to, jak velká mezera zůstane k loketnímu chrániči.</p>'
          '<h2>Jak má rukavice sedět</h2>'
          '<ul><li>Konečky prstů nemají narážet do konce rukavice, ale před nimi nemá zůstat ani několik centimetrů prázdna.</li>'
          '<li>Manžeta končí kousek pod loketním chráničem. Velká mezera nechává předloktí bez ochrany.</li>'
          '<li>Při sevření hokejky se rukavice nemá vrásnit v dlani ani tlačit na kloubech.</li>'
          '<li>Zápěstí musí jít ohnout do stran i dopředu, jinak se špatně střílí a přihrává.</li></ul>'
          '<p>Nejlepší zkouška je s hokejkou v ruce. Dětem nekupujte rukavice o dvě čísla větší „na růst“. Ruka v nich plave, hůř se drží hůl a prsty se dostanou do míst, kde chybí výztuha.</p>'
          '<h2>Střih: volnější, nebo přiléhavý</h2>'
          '<p>Výrobci nabízejí v podstatě dvě skupiny střihů. Tradiční střih má víc prostoru uvnitř a ruka se v něm může trochu pohybovat, což mnoha hráčům vyhovuje kvůli pocitu volnosti. Užší, tzv. tapered střih, obepíná prsty i zápěstí těsněji a rukavice působí jako prodloužení ruky. Mezi nimi existují kompromisy. Každá značka své řady pojmenovává po svém, proto čtěte popis konkrétního modelu, nikoli jen název série.</p>'
          '<h2>Dlaň a její výměna</h2>'
          '<p>Dlaně bývají ze syntetického semiše, kterému se v hokejové hantýrce říká nash, nebo z jiných mikrovláken. Tenčí dlaň dává lepší cit pro hokejku, ale rychleji se prodře. Na místech s největším třením mají některé modely zesílené záplaty. Vlhko, pot a sušení na topení dlaň vysušují, takže ztvrdne a praskne.</p>'
          '<p>Když je plášť rukavice v pořádku a prodřená je jen dlaň, nabízejí některé hokejové servisy její výměnu. U dražších rukavic to může dávat smysl, u dětských, ze kterých se stejně brzy vyroste, spíš ne. Opravu je dobré řešit dřív, než se díra rozšíří ke švům.</p>'
          '<h2>Hokejbal a pozemní hokej</h2>'
          '<p>Na hokejbal se běžně používají klasické hokejové rukavice. Někteří výrobci, například Knapper nebo Winnwell, mají i modely označené jako hokejbalové. Hra na asfaltu nebo umělém povrchu dává dlani zabrat jinak než led, takže se vyplatí sledovat, jak rychle se opotřebovává. Pozemní hokej je jiný sport s lehčími rukavicemi, často jen na jednu ruku, a má vlastní kategorii <a href="/pozemni-hokej/">pozemní hokej</a>.</p>'
          '<h2>Péče a sušení</h2>'
          '<p>Po tréninku vytáhněte rukavice z tašky hned, jak to jde. Rozevřete manžetu, postavte je prsty nahoru nebo je zavěste a nechte uschnout při pokojové teplotě. Přímé teplo z radiátoru nebo fénu škodí dlani i lepeným výplním. Vlhká výstroj zavřená přes noc v tašce rychle zapáchá a materiál se rozkládá. Případné praní řešte podle pokynů výrobce, ne všechny materiály ho snesou stejně.</p>'
          '<p>Na převoz výstroje se hodí taška s větráním z kategorie <a href="/hokejove-tasky/">hokejové tašky a batohy</a>. Doma pak výstroj vyndejte a rozložte, i když jedete na další trénink druhý den.</p>'
          '<h2>Vyšší a nižší řady</h2>'
          '<p>Většina značek má několik úrovní stejné série. Vyšší modely bývají lehčí a používají odolnější materiály, levnější verze jsou těžší a jednodušší. Pro rekreačního hráče nebo dítě, které ještě roste, často stačí nižší řada. Při porovnávání sledujte hmotnost, tvar manžety, konstrukci palce a materiál dlaně.</p>'
          '<h2>Pravá a levá ruka</h2>'
          '<p>Hokejové rukavice se prodávají jako pár a nejsou stavěné zvlášť pro leváky nebo praváky. Držení hole se liší podle toho, kterou rukou hráč drží horní konec, ale rukavice zůstávají stejné. Jinak je to u brankářů, kde se lapačka a vyrážečka volí podle ruky, a v pozemním hokeji. Při objednávce brankářské výstroje proto sledujte, zda jde o provedení pro „regular“, nebo „full right“, a ověřte si význam v popisu výrobce.</p>'
          '<h2>Jak rukavice vyzkoušet</h2>'
          '<p>V obchodě i doma po doručení si rukavice navlékněte na čistou a suchou ruku. Sevřete hokejku tak, jak ji držíte při hře, a několikrát zkuste pohyb jako při střele a přihrávce. Pak ruku úplně zatněte v pěst a zase povolte. Rukavice by neměla v ohybu prstů tlačit a palec se nemá dostat mimo výztuhu. Nakonec si nasaďte loketní chránič a zkontrolujte, jak na sebe obě části navazují. Při nákupu přes internet mějte na paměti, že zboží zkoušené s výstrojí je vhodné vracet čisté a bez známek použití, proto zkoušku dělejte doma na koberci, ne na ledě.</p>'
          '<h2>Kdy je čas na nové rukavice</h2>'
          '<p>Rukavice nemusíte měnit každou sezónu, ale opotřebení ochrany je dobré hlídat. Varovné znaky jsou díra v dlani, která se šíří ke švům, prasklé plastové vložky na hřbetu, rozpadlá nebo stlačená pěna v prstech a povolené švy u manžety. U dětí přijde výměna nejčastěji tehdy, když konečky prstů narážejí na konec rukavice nebo manžeta už nedosahuje k loketnímu chrániči. Poškozená rukavice může vypadat v pořádku, ale při zásahu pukem už nechrání tak, jak má.</p>'
          '<h2>První rukavice pro začínajícího hráče</h2>'
          '<p>Dítě, které s hokejem teprve začíná, nepotřebuje profesionální model. Důležitější je správná velikost, lehkost a to, aby se rukavice snadno navlékaly a sundávaly i bez pomoci. Než rukavice koupíte, zeptejte se trenéra v klubu, jestli má k výstroji nějaká doporučení. Barva klubu ochranu nijak nemění, takže pokud v ní zrovna požadovaná velikost chybí, vyplatí se sáhnout po jiném provedení. Rodiče, kteří kupují výstroj na několik sezón, často kombinují nové rukavice s ostatními chrániči z druhé ruky. U rukavic je ale dobré prohlédnout dlaň a pěnu v prstech, protože jsou nejvíc namáhané.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Výběr podle barvy klubu bez vyzkoušení s hokejkou.</li>'
          '<li>Příliš velké dětské rukavice, ve kterých ruka klouže.</li>'
          '<li>Mezera mezi manžetou a loketním chráničem.</li>'
          '<li>Sušení na topení, po kterém dlaň ztvrdne.</li>'
          '<li>Koupě INT velikosti bez ověření tabulky, i když hráč potřebuje JR nebo SR.</li></ul>'
          '<p>K rukavicím patří i ostatní výstroj: <a href="/hokejky/">hokejky</a>, <a href="/hokejove-brusle/">hokejové brusle</a> a <a href="/hokejove-helmy-a-mrizky/">helmy s mřížkou</a>. Omotávku na hůl a tkaničky najdete mezi <a href="/hokejove-pasky-a-doplnky/">hokejovými páskami a doplňky</a>.</p>',
    faq=[
        ('Jak vybrat velikost hokejových rukavic?', 'Změřte ruku od špičky prostředníčku k zápěstí a porovnejte ji s tabulkou dané značky. Pak zkontrolujte, jak manžeta navazuje na loketní chránič.'),
        ('Co znamená YTH, JR, INT a SR?', 'Jde o kategorie youth, junior, intermediate a senior. Určují dětský, juniorský, přechodový nebo dospělý střih a k nim patří typická čísla v palcích.'),
        ('Jakou velikost rukavic potřebuje dospělý?', 'Většina dospělých nosí 13" až 15". Hráči s menší rukou často sáhnou po INT 13", proto je dobré rukavice vyzkoušet.'),
        ('Mají se kupovat dětské rukavice na růst?', 'Spíš ne. Ve velkých rukavicích se špatně drží hokejka a prsty nejsou tam, kde je výztuha. Stačí malá rezerva.'),
        ('Jaký je rozdíl mezi tradičním a tapered střihem?', 'Tradiční střih je uvnitř volnější, tapered přiléhá k prstům i zápěstí. Volba je hlavně otázkou pohodlí a hracího stylu.'),
        ('Dá se vyměnit prodřená dlaň?', 'Některé hokejové servisy výměnu dlaně nabízejí. Vyplatí se hlavně u kvalitnějších rukavic s nepoškozeným pláštěm.'),
        ('Jak sušit hokejové rukavice?', 'Vytáhnout z tašky, rozevřít manžetu a nechat uschnout volně při pokojové teplotě. Topení a fén dlaň vysušují.'),
        ('Hodí se hokejové rukavice na hokejbal?', 'Ano, na hokejbal se běžně používají. Někteří výrobci mají i speciální hokejbalové modely.'),
        ('Proč se dlaň rukavic rychle prodře?', 'Kvůli tření o hokejku, potu a špatnému sušení. Tenká dlaň dává lepší cit, ale vydrží méně.'),
        ('Kde porovnat nabídky hokejových rukavic?', 'Na Sportece vidíte u každého modelu obchody a dostupné velikosti v palcích. Nakupujete pak v e-shopu, který si vyberete.'),
    ])

# ------------------------------------------------------------------ chranice-zubu
NEW['chranice-zubu'] = dict(long=True,
    title='Chránič zubů na box, MMA, hokej i ragby: jak ho vybrat',
    desc='Chrániče zubů hotové, tvarovací v horké vodě i dětské. Jak chránič vytvarovat, udržovat a kdy ho vyměnit. Opro, Safejawz, Sisu, Venum, RDX a další.',
    intro='<p><strong>Chránič zubů</strong>, kterému sportovci říkají i guma nebo mouthguard, je pružný kryt nasazený obvykle na horní zuby. Při úderu nebo nárazu rozkládá sílu na větší plochu a odděluje zuby od rtů a tváří. Používá se v boxu, kickboxu, MMA a dalších bojových sportech, ale také v ragby, americkém fotbale, hokeji nebo basketbale. Chránič snižuje riziko poranění zubů, nezaručuje však, že k němu nedojde, a není to zdravotnický prostředek.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u konkrétního chrániče, ať jde o dětskou, nebo dospělou velikost. Nákup dokončíte v e-shopu podle vlastní volby. Najdete tu chrániče značek Opro, Safejawz, Sisu, Shock Doctor, Venum, Bushido, RDX, Everlast nebo Leone. Kategorie spadá pod <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>.</p>',
    guide='<h2>Tři druhy chráničů</h2>'
          '<p>Chrániče se dělí podle toho, jak se přizpůsobí tvaru zubů. Americká zubařská asociace ADA rozlišuje hotové chrániče, chrániče tvarované v ústech a chrániče na zakázku od zubaře.</p>'
          + T(['Druh', 'Jak se přizpůsobí', 'Na co si dát pozor'], [
              ['Hotový (stock)', 'nijak, nasadí se rovnou', 'sedí nejméně přesně, v ústech se může posouvat'],
              ['Tvarovací v horké vodě (boil and bite)', 'změkne v horké vodě a vytvaruje se skusem', 'je nutné dodržet návod, jinak sedí špatně'],
              ['Na zakázku', 'zubař sejme otisk a chránič vyrobí laboratoř', 'vyžaduje návštěvu zubaře, nekupuje se v e-shopu']]) +
          '<p>V e-shopech převažují tvarovací chrániče. Některé hotové dětské modely se prodávají jako připravené k okamžitému použití, například řada Snap-Fit od Opro. Zvláštní skupinu tvoří tenké chrániče Sisu, které se také tvarují teplem, ale jsou výrazně tenčí než klasická guma. Výrobce uvádí, že je lze přetvarovat opakovaně.</p>'
          '<h2>Jak vytvarovat chránič v horké vodě</h2>'
          '<p>Postup se u značek liší v teplotě vody a čase, proto vždy platí návod v balení. Obecně vypadá takto:</p>'
          '<ol><li>Chránič ponořte do horké vody na dobu, kterou uvádí výrobce. Některé značky výslovně píšou, že voda nemá vřít.</li>'
          '<li>Vyndejte ho, nechte okapat a krátce vyčkejte, aby nespálil rty.</li>'
          '<li>Nasaďte ho na horní zuby, skousněte a jazykem i prsty ho přitlačte k zubům a dásním. Zároveň z něj vysajte vzduch.</li>'
          '<li>Po chvíli ho vyndejte a ochlaďte ve studené vodě, aby tvar ztuhl.</li></ol>'
          '<p>Dobře vytvarovaný chránič drží na zubech i bez skousnutí, nepřekáží v dýchání a dá se v něm krátce promluvit. Když padá nebo tlačí, většinu tvarovacích chráničů jde nahřát a tvarovat znovu. U dětí stojí za to postup udělat společně s rodičem.</p>'
          '<h2>Velikost a tloušťka</h2>'
          '<p>Chrániče se prodávají v dětské (junior) a dospělé velikosti, některé značky mají i více stupňů. Dětské chrániče jsou menší a měkčí, aby se vešly do menších úst. Tloušťka se liší podle modelu. Tenčí chrániče se lépe nosí při mluvení a pití, masivnější kryjí zuby větší vrstvou materiálu. Kterou cestou jít v konkrétním sportu, je dobré probrat s trenérem.</p>'
          '<p>Na trhu jsou i chrániče s páskem pro připevnění k helmě, používané hlavně v amerických sportech, a modely s výřezy pro snazší dýchání. Pro sporty s vysokým tempem hraje pohodlí velkou roli. Nepohodlný chránič hráč vyndá a pak nechrání nic.</p>'
          '<h2>Ve kterých sportech se chránič používá</h2>'
          '<ul><li><strong>Box, kickbox, thajský box a MMA</strong>: chránič patří ke standardní výbavě na sparing i zápas. Doplňují ho <a href="/boxerske-rukavice/">boxerské rukavice</a> a u MMA <a href="/mma-rukavice/">MMA rukavice</a>.</li>'
          '<li><strong>Ragby a americký fotbal</strong>: kontaktní hra s častými srážkami. Výstroj najdete v kategorii <a href="/ragby-a-americky-fotbal/">ragby a americký fotbal</a>.</li>'
          '<li><strong>Hokej</strong>: chránič se nosí i pod <a href="/hokejove-helmy-a-mrizky/">helmu s mřížkou</a> nebo plexi.</li>'
          '<li><strong>Basketbal, házená, florbal</strong>: zuby často ohrozí loket soupeře nebo míček.</li></ul>'
          '<p>V některých soutěžích je chránič povinný. Pravidla se liší podle svazu a věkové kategorie, proto si je ověřte u klubu nebo pořadatele.</p>'
          '<h2>Rovnátka a zubní náhrady</h2>'
          '<p>Kdo nosí fixní rovnátka, by neměl chránič vybírat naslepo. Některé značky mají řady pro rovnátka, například Safejawz Ortho, ale o vhodném typu a postupu tvarování má rozhodnout ortodontista. Zuby se během léčby posouvají a chránič je potřeba průběžně kontrolovat nebo měnit. Totéž platí u můstků, implantátů a snímatelných náhrad: poraďte se se zubařem.</p>'
          '<h2>Hygiena a skladování</h2>'
          '<p>Po každém použití chránič opláchněte ve studené nebo vlažné vodě a jemně ho očistěte kartáčkem. Horká voda by mohla změnit tvar. Nechte ho oschnout a uložte do větraného pouzdra, které bývá v balení nebo se dá dokoupit. Neschovávejte ho vlhký do zavřené tašky a nenechávejte ho v rozpáleném autě. Chránič nepůjčujte a nesdílejte s ostatními.</p>'
          '<h2>Kdy chránič vyměnit</h2>'
          '<p>Vyměňte ho, když je prokousnutý, natržený, deformovaný nebo přestane držet na zubech. Chrániče z volného prodeje se postupně opotřebují, a proto se často mění každou sezónu. U dětí, kterým rostou a mění se zuby, bývá výměna potřeba častěji. Při preventivní prohlídce můžete chránič vzít s sebou a nechat zubaře zkontrolovat, jak sedí.</p>'
          '<h2>Chránič u dětí</h2>'
          '<p>Dětem se mění chrup a čelisti rostou, proto jim tvarovací chránič často přestane sedět dřív než dospělým. Při tvarování by měl pomáhat dospělý, protože jde o práci s horkou vodou a dítě snadno chránič přikousne nakřivo. Vybírejte juniorskou velikost a sledujte, zda výrobce uvádí doporučený věk. Když dítě začne chránič vyndávat, protože ho tlačí nebo se mu v něm špatně dýchá, je to signál k novému tvarování nebo výměně. O vhodnosti chrániče u dětí s mléčnými a stálými zuby současně se můžete poradit s dětským zubařem.</p>'
          '<h2>Na co chránič nestačí</h2>'
          '<p>Chránič zubů je jen jedna část ochrany. V hokeji nenahrazuje helmu s mřížkou nebo plexi, v boxu na sparingu nenahrazuje přilbu a v ragby nenahrazuje správnou techniku skládky. Nechrání ani před úrazem hlavy, i když se tak někdy tvrdí v reklamách. Pokud dojde k úderu do úst a zub se uvolní, odštípne nebo vypadne, je potřeba co nejdřív vyhledat zubaře, ne pokračovat ve hře.</p>'
          '<h2>Na co se dívat při porovnání nabídek</h2>'
          '<ul><li><strong>Velikost</strong>: junior, nebo dospělý, u některých značek i více stupňů.</li>'
          '<li><strong>Způsob úpravy</strong>: hotový, tvarovací v horké vodě, nebo tenký přetvarovatelný.</li>'
          '<li><strong>Pouzdro</strong>: zda je součástí balení a jestli má větrací otvory.</li>'
          '<li><strong>Určení</strong>: řady pro rovnátka, modely s páskem k helmě nebo bez něj.</li>'
          '<li><strong>Barva a vzor</strong>: licenční motivy, tesáky nebo vlajky ochranu nemění, jde jen o vzhled.</li></ul>'
          '<p>U týmových sportů se vyplatí podepsat si pouzdro jménem. Chrániče stejné barvy se v šatně snadno zamění a cizí chránič už nikdo nenasadí.</p>'
          '<h2>Chránič na zakázku od zubaře</h2>'
          '<p>Individuální chránič vzniká podle otisku zubů, který sejme zubař. Laboratoř ho pak vyrobí tak, aby přesně kopíroval chrup, a zubař při předání zkontroluje skus. Taková ochrana obvykle drží nejlépe a méně překáží při mluvení i dýchání. Nevýhodou je, že vyžaduje návštěvu ordinace a při změnách chrupu je nutné ji udělat znovu. U dětí a dospívajících, kterým se zuby mění, se proto často volí kompromis v podobě tvarovacího chrániče, který se dá vyměnit levněji a častěji.</p>'
          '<h2>Sliby na obalu</h2>'
          '<p>Někteří výrobci uvádějí, že jejich chránič zlepšuje dýchání, výkon nebo soustředění. Takové údaje berte s rezervou, zvlášť pokud k nim chybí nezávislé měření. Pro běžného sportovce je podstatné, aby chránič seděl, nepadal, nepřekážel a dal se nosit celý trénink. Během zápasu ho na střídačce nebo v rohu ringu odkládejte do pouzdra, ne na lavici nebo zem, kde se zašpiní.</p>'
          '<h2>Po vytvarování: zkouška na tréninku</h2>'
          '<p>Nový chránič si nejdřív vyzkoušejte na běžném tréninku, ne rovnou na zápase. Za hodinu poznáte, jestli se v něm dá dýchat při zátěži, jestli nedráždí ke zvracení a jestli při mluvení nevypadává. Když zadní okraj tlačí na patro, většinou pomůže nové tvarování. Chránič ořezávejte jen tehdy, když to návod výslovně dovoluje, a jen v místech, která výrobce označí. Příliš zkrácený chránič nekryje stoličky a hůř drží. Pokud ani po opakovaném tvarování nesedí, zkuste jiný model nebo se obraťte na zubaře.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Tvarování ve vroucí vodě, i když výrobce předepisuje nižší teplotu.</li>'
          '<li>Ořezávání chrániče nůžkami, dokud nepřestane překážet, místo nového tvarování.</li>'
          '<li>Žvýkání chrániče mezi koly, které ho rychle zničí.</li>'
          '<li>Dospělá velikost v dětských ústech.</li>'
          '<li>Chránič uložený mokrý v tašce s ostatní výstrojí.</li></ul>'
          '<p>Další ochranu pro trénink najdete mezi <a href="/chranice-bojove-sporty/">chrániči</a> a v celé sekci <a href="/bojove-sporty/">bojové sporty</a>.</p>',
    faq=[
        ('Jaký chránič zubů vybrat na box?', 'Většina boxerů používá tvarovací chránič na horní zuby, který po vytvarování drží bez skousnutí. Nejpřesněji sedí chránič vyrobený zubařem.'),
        ('Jak vytvarovat chránič zubů?', 'Ponořit do horké vody podle návodu, krátce nechat vychladnout, nasadit, skousnout a přitlačit k zubům. Pak ho ochladit studenou vodou.'),
        ('Smí se chránič zubů dát do vroucí vody?', 'Záleží na značce. Někteří výrobci výslovně uvádějí horkou, ale ne vroucí vodu. Řiďte se návodem v balení.'),
        ('Nosí se chránič na horní, nebo dolní zuby?', 'Běžně na horní. Pokud máte neobvyklý skus, rovnátka nebo zubní náhradu, poraďte se se zubařem.'),
        ('Můžu chránič zubů používat s rovnátky?', 'Existují modely určené pro rovnátka, ale výběr a tvarování má posoudit ortodontista. Zuby se během léčby posouvají.'),
        ('Jak čistit chránič zubů?', 'Opláchnout ve studené nebo vlažné vodě, jemně vykartáčovat a nechat oschnout ve větraném pouzdru. Horká voda může změnit tvar.'),
        ('Jak často chránič měnit?', 'Když je poškozený nebo přestane držet, běžně každou sezónu. Dětem kvůli rostoucím zubům i častěji.'),
        ('Je dětský chránič jiný než dospělý?', 'Je menší a obvykle měkčí, aby se vešel do dětských úst. Dospělá velikost by dítěti nesedla.'),
        ('Ochrání chránič zubů úplně?', 'Snižuje riziko poranění zubů a měkkých tkání, ale nezaručí, že ke zranění nedojde. Není to zdravotnický prostředek.'),
        ('Kde porovnat chrániče zubů?', 'Sporteka u každého chrániče ukáže obchody, které ho nabízejí, včetně barev a velikostí. Objednáváte v e-shopu, který si zvolíte.'),
    ])

# ------------------------------------------------------------------ joga-bloky
NEW['joga-bloky'] = dict(long=True,
    title='Jóga bloky z pěny, korku i dřeva: rozměry a výběr',
    desc='Jógové bloky a cihličky z EVA pěny, korku i dřeva. Jaké rozměry a materiál zvolit, kolik bloků pořídit a jak je čistit. Porovnání nabídek e-shopů.',
    intro='<p><strong>Jógový blok</strong>, někdy také jóga cihlička, je pevný kvádr, který při cvičení „přiblíží zem“. Opřete se o něj rukou, když na podložku ještě nedosáhnete, sednete si na něj, aby se pánev zvedla, nebo ho podložíte pod záda či křížovou kost. Používá se v józe, pilatesu i při protahování po tréninku. Vyrábí se hlavně z EVA pěny a korku, méně často ze dřeva nebo bambusu.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u konkrétního bloku uvidíte, kdo ho prodává a v jakých barvách. Nakupujete pak přímo v obchodě. Bloky nabízí například '
          + B(('merco', 'Merco'), ('hms', 'HMS'), ('nike', 'Nike')) +
          ', dále Casall, Bodhi, Tunturi nebo Myga. Jsou součástí kategorie <a href="/jogove-pomucky/">jógové bloky, popruhy a bolstery</a> a doplňují <a href="/joga-a-podlozky/">jógové podložky</a>.</p>',
    guide='<h2>K čemu jógový blok slouží</h2>'
          '<p>Blok zkracuje vzdálenost mezi tělem a podložkou. Ve stojných pozicích, kdy se ruka má dotknout země, ji místo toho opřete o blok a udržíte rovná záda. V sedu ho podložíte pod hýždě, aby se pánev naklopila a předklon byl pohodlnější. Vleže slouží jako opora pod křížovou kost nebo lopatky, při posilovacích cvicích se drží mezi stehny nebo dlaněmi.</p>'
          '<p>Blok má tři různé výšky podle toho, na kterou stranu ho položíte. Naležato je nejnižší a nejstabilnější, nastojato nejvyšší. Začátečníci tak mohou s jedním blokem postupně snižovat oporu, jak se zlepšuje pohyblivost. Blok však nenahrazuje lektora: pokud vás cvik bolí, přestaňte a postup proberte s instruktorem, případně s lékařem.</p>'
          '<h2>Rozměry</h2>'
          '<p>Nejběžnější rozměr je přibližně 23 × 15 × 7,5 cm, což odpovídá americkému standardu 9 × 6 × 3 palce. Vedle něj se prodávají silnější bloky s výškou kolem 10 cm, které dají víc opory. Ploché bloky jsou nižší a hodí se pod kolena, zápěstí nebo hlavu. Najdete i zaoblené či jinak tvarované bloky, ty jsou ale spíš doplněk než náhrada klasického kvádru.</p>'
          '<p>Kdo má menší ruce, drží užší a tenčí blok snáz. Vyšší a mohutnější blok naopak ocení cvičenci s kratšími pažemi nebo menší pohyblivostí. Rozměry si před nákupem porovnejte v popisu, název „standardní“ neznamená u všech značek stejné číslo.</p>'
          '<h2>Materiály</h2>'
          + T(['Materiál', 'Vlastnosti', 'Komu sedne'], [
              ['EVA pěna', 'lehká, měkčí, pod tlakem mírně povolí, omyvatelná', 'začátečníci, domácí cvičení, cesty'],
              ['Korek', 'těžší a pevnější, stabilní, přírodní materiál', 'kdo se o blok opírá celou vahou'],
              ['Dřevo a bambus', 'tvrdé, těžké, hladký povrch', 'pevná opora, méně vhodné pro zpocené ruce'],
              ['Pěna s vyšší hustotou', 'pevnější než běžná EVA, stále lehká', 'kompromis mezi pěnou a korkem']]) +
          '<p>Pěnové bloky mají příjemný povrch a při pádu ani při položení pod záda nebolí. Mírně se ale stlačí a u levnějších kusů se po čase mohou otlačit hrany. Korek je výrazně stabilnější a víc „drží“ na podložce, je však těžší a jeho hrany se při hrubém zacházení mohou odštípnout. Dřevěné bloky jsou nejtvrdší, takže se hodí spíš jako pevná opora pod ruce než pod záda.</p>'
          '<h2>Jeden blok, nebo dva</h2>'
          '<p>Pro začátek stačí jeden blok. Ve studiích se ale často pracuje se dvěma, protože některé pozice vyžadují oporu pod obě ruce nebo pod obě strany těla najednou. Bloky se také dají postavit na sebe a získat tak větší výšku. Pokud cvičíte podle online lekcí, podívejte se, kolik bloků lektor používá.</p>'
          '<h2>Jak vybrat blok podle cvičení</h2>'
          '<ul><li><strong>Hatha a jemná jóga</strong>: měkčí pěnový blok, který lze bez obav podložit pod záda.</li>'
          '<li><strong>Dynamická jóga</strong>: korek nebo hustá pěna, které neujíždějí a nestlačí se.</li>'
          '<li><strong>Pilates a posilování</strong>: lehký blok, který se dobře drží mezi koleny nebo dlaněmi.</li>'
          '<li><strong>Protažení po běhu nebo posilovně</strong>: jakýkoli stabilní blok standardní velikosti.</li></ul>'
          '<h2>Péče o jógový blok</h2>'
          '<p>Pěnový blok otřete vlhkým hadříkem s trochou jemného mýdla a nechte ho volně uschnout. Korek nenamáčejte, jen ho otřete vlhkým hadříkem a vysušte, delší kontakt s vodou mu neprospívá. Dřevo stačí utřít nasucho nebo mírně navlhčenou utěrkou. Bloky skladujte mimo přímé slunce a zdroje tepla, aby pěna nezkřehla a korek nevysychal.</p>'
          '<h2>Co se k bloku hodí</h2>'
          '<p>Blok bývá v kombinaci s popruhem, který pomůže dosáhnout na chodidla v předklonu, a s bolsterem pro relaxační pozice. Obojí najdete v kategorii <a href="/jogove-pomucky/">jógové pomůcky</a>. Pro pilates jsou připravené kruhy a míče mezi <a href="/pilates-pomucky/">pilates pomůckami</a>, na stabilitu a rovnováhu <a href="/balancni-podlozky-bosu/">balanční podložky a BOSU</a>. Lehké posilování doplní <a href="/posilovaci-gumy/">posilovací gumy</a>. Celou nabídku najdete v sekci <a href="/joga-a-pilates/">jóga, pilates a meditace</a>.</p>'
          '<h2>Příklady použití v pozicích</h2>'
          '<p>Následující příklady jsou obecné a slouží pro představu. Konkrétní provedení vám nejlépe ukáže lektor.</p>'
          '<ul><li><strong>Trojúhelník a půlměsíc</strong>: spodní ruka se opře o blok vedle chodidla, takže hrudník zůstane otevřený a záda se nehrbí.</li>'
          '<li><strong>Předklon v sedu</strong>: sed na bloku zvedne pánev, kolena se mohou mírně pokrčit a předklon vychází z kyčlí.</li>'
          '<li><strong>Podpořený most</strong>: blok pod křížovou kostí nese pánev a pozice se dá chvíli držet bez svalové práce.</li>'
          '<li><strong>Pozice dítěte</strong>: blok pod čelem pomůže, když hlava nedosáhne na podložku.</li>'
          '<li><strong>Holubice</strong>: blok pod hýždí přední nohy vyrovná pánev, pokud kyčel nedosedne na zem.</li>'
          '<li><strong>Posilování</strong>: blok stisknutý mezi stehny při mostu nebo mezi dlaněmi zapojí vnitřní svaly stehen a paží.</li></ul>'
          '<p>Blok nepokládejte tam, kde by ujížděl, například na kluzkou podlahu bez podložky. Ve stojných pozicích ho mějte na podložce vedle chodidla, ne daleko před sebou.</p>'
          '<h2>Na co se dívat v popisu</h2>'
          '<p>U bloků se vyplatí porovnat přesné rozměry a hmotnost. Korkový blok standardní velikosti je znatelně těžší než pěnový, což oceníte při opírání, ale ne v batohu cestou na lekci. Sledujte také, zda má blok zaoblené hrany, které jsou příjemnější pod zády a v dlani. Některé bloky se prodávají v páru, jiné po jednom kuse, a cena v nabídce se pak vztahuje k jinému množství. U pěny se výrobci často zmiňují o hustotě nebo pevnosti, u korku o tom, zda je lisovaný z jemné, nebo hrubší drti.</p>'
          '<h2>Blok, válec, nebo bolster</h2>'
          '<p>Jógový blok se snadno zamění s jinými pomůckami. Masážní válec je kulatý a slouží k uvolnění svalů po tréninku, na opírání ve stojných pozicích se nehodí. Bolster je velký měkký polštář pro relaxační a regenerační pozice, kde blok bývá příliš tvrdý. Mnoho cvičenců má postupně všechny tři, ale pro začátek jógy dává největší smysl právě blok, protože pomůže v řadě běžných pozic.</p>'
          '<h2>Korek a životní prostředí</h2>'
          '<p>Korek se získává z kůry korkového dubu. Kůra se loupe ze živých stromů, které ji postupně znovu obnovují, takže se strom kvůli ní nekácí. Bloky z korku se proto často nabízejí jako přírodní varianta. EVA pěna je plast, některé značky ale používají pěnu z recyklovaného materiálu. Pokud je pro vás původ materiálu důležitý, hledejte tuto informaci v popisu konkrétního bloku, protože se mezi výrobky liší.</p>'
          '<h2>Kdy blok vyměnit</h2>'
          '<p>Dobrý blok vydrží roky. Výměnu zvažte, když se pěna trvale stlačila a blok se pod rukou prohýbá, když se korek na hranách drolí nebo když povrch začal klouzat a ruka po něm ujíždí. U pěnových bloků se někdy po letech objeví praskliny v rozích. Takový blok už nedává jistou oporu a v pozicích, kde se o něj opíráte, může nečekaně sklouznout.</p>'
          '<h2>Cvičení doma</h2>'
          '<p>Pro domácí jógu stačí podložka, jeden nebo dva bloky a popruh. Vše se vejde do skříně nebo pod postel. Pěnové bloky jsou lehké a dají se vzít s sebou na dovolenou, korkové zůstávají spíš doma. Pokud cvičíte na hladké podlaze, mějte blok vždy na podložce, aby při opření neujel.</p>'
          '<h2>Blok jako sedátko</h2>'
          '<p>Při meditaci nebo dechových cvičeních v sedu se blok dá použít místo meditačního polštáře. Když si na něj sednete, pánev se zvedne nad kolena a záda se snáz narovnají. Pro vyšší sed lze položit dva bloky na sebe nebo jeden postavit na užší stranu. Pěnový blok je při delším sezení příjemnější než korkový nebo dřevěný. Pokud vám v sedu se zkříženýma nohama tuhnou kolena, zkuste blok podložit i pod ně.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Stoupání na měkký pěnový blok, který se pod váhou prohne.</li>'
          '<li>Blok příliš malý pro dlouhé paže, takže stejně nedosáhnete.</li>'
          '<li>Dřevěný blok pod bederní páteř při relaxaci.</li>'
          '<li>Namáčení korku při mytí.</li>'
          '<li>Snaha dosáhnout na zem za každou cenu místo použití vyšší strany bloku.</li></ul>',
    faq=[
        ('Jaký je standardní rozměr jógového bloku?', 'Nejčastěji přibližně 23 × 15 × 7,5 cm. Prodávají se i silnější bloky kolem 10 cm a ploché varianty.'),
        ('Pěnový, nebo korkový blok?', 'Pěnový je lehčí a měkčí, korkový těžší, pevnější a stabilnější. Začátečníkům obvykle stačí pěna, kdo se o blok hodně opírá, ocení korek.'),
        ('Kolik jógových bloků potřebuji?', 'Na začátek stačí jeden. Ve studiích se často používají dva, protože některé pozice potřebují oporu pod obě ruce.'),
        ('K čemu je jóga cihlička?', 'Je to jiný název pro jógový blok. Pomáhá dosáhnout na zem, zvedá pánev v sedu a slouží jako opora pod záda.'),
        ('Jak vyčistit pěnový jógový blok?', 'Otřete ho vlhkým hadříkem s jemným mýdlem a nechte volně uschnout. Nesušte ho na topení.'),
        ('Jak vyčistit korkový blok?', 'Jen vlhkým hadříkem a hned osušit. Korek nenamáčejte a neskladujte na přímém slunci.'),
        ('Hodí se jógový blok i na pilates?', 'Ano, drží se mezi koleny nebo dlaněmi a slouží jako opora pod hlavu či pánev.'),
        ('Je dřevěný blok lepší než pěnový?', 'Je tvrdší a pevnější, ale těžší a na zpocených rukou klouže. Pod záda je pěna příjemnější.'),
        ('Může blok nahradit lektora?', 'Ne. Usnadní pozice, ale správné provedení je dobré probrat s instruktorem. Při bolesti cvik přerušte.'),
        ('Kde koupit jógový blok?', 'Sporteka u každého bloku ukazuje nabídky českých e-shopů včetně barev. Objednávka proběhne v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ kotouce-na-cinky
NEW['kotouce-na-cinky'] = dict(long=True,
    title='Kotouče na činky a osy: olympijské, litinové i bumper',
    desc='Kotouče na činky s otvorem 25, 30 i 50 mm, litinové, pogumované a bumper, olympijské a EZ osy. Jak vybrat průměr, materiál, uzávěry a podlahu.',
    intro='<p><strong>Kotouče na činky</strong>, často nazývané talíře nebo závaží, se nasazují na osu a podle potřeby se přidávají a ubírají. Doma i v posilovně tak z jedné tyče vznikne činka s různou zátěží. Kotouče se liší materiálem, tvarem a hlavně průměrem středového otvoru, který musí odpovídat ose. Do kategorie patří i samotné osy: dlouhé rovné, olympijské, zalomené EZ osy a krátké jednoruční.</p>'
          '<p>Sporteka sbírá nabídky českých e-shopů, takže u vybraného kotouče nebo osy uvidíte, kdo je prodává a v jakých hmotnostech. Nákup pak dokončíte v obchodě. V nabídce jsou kotouče a osy značek '
          + B(('hms', 'HMS'), ('insportline', 'inSPORTline'), ('gymbeam', 'GymBeam'), ('merco', 'Merco')) +
          ', dále Sedco, Tunturi nebo Actiget. Kategorie je součástí sekce <a href="/cinky-a-kotouce/">činky a kotouče</a>, k uložení zátěže slouží <a href="/stojany-na-cinky/">stojany na činky a kotouče</a>.</p>',
    guide='<h2>Průměr otvoru rozhoduje</h2>'
          '<p>Než začnete porovnávat materiály, zjistěte, jakou osu máte nebo chcete. Kotouč s malým otvorem na olympijskou osu nenasadíte a velký otvor na tenké ose plave a kotouč nejde pořádně zajistit. V popisech se uvádí otvor o milimetr větší než průměr osy, proto se setkáte s čísly 30 i 31 mm nebo 50 i 51 mm.</p>'
          + T(['Otvor kotouče', 'Na jakou osu', 'Kde se používá'], [
              ['25 mm', 'tenčí osy 25 mm', 'menší domácí sady'],
              ['30–31 mm', 'osy a jednoruční činky 30 mm', 'nejběžnější domácí systém'],
              ['50–51 mm', 'olympijské osy s konci 50 mm', 'posilovny, vzpírání, powerlifting, domácí garáže']]) +
          '<p>Olympijská osa má tenčí úchop a silnější otočné konce, na které se kotouče nasazují. Nelze tedy říct, že osa „má 50 mm“ po celé délce. Úchop pánské osy měří 28 mm, ženské 25 mm.</p>'
          '<h2>Materiály kotoučů</h2>'
          '<ul><li><strong>Litinové</strong>: kovové, relativně tenké, takže se jich na osu vejde hodně. Při nárazu na zem nebo o sebe jsou hlučné a mohou poškodit podlahu.</li>'
          '<li><strong>Pogumované</strong>: litinové jádro s gumovým potahem. Jsou tišší, šetrnější k podlaze i ke stojanu a lépe se drží. Na pouštění ze záhlaví ale určené nejsou.</li>'
          '<li><strong>Bumper</strong>: z pevné pryže, obvykle s kovovým středem. Těžší kusy mají stejný vnější průměr, takže osa leží na zemi vždy ve stejné výšce. Jsou stavěné na pouštění z výšky na vhodnou podložku při vzpírání a funkčním tréninku.</li>'
          '<li><strong>Kotouče s úchopy</strong>: mají v ploše otvory pro prsty. Lépe se přenášejí a dají se použít i samostatně, například na výpady nebo rotace.</li></ul>'
          '<p>Malé kotouče od 0,5 kg slouží k jemnému navyšování zátěže, kdy skok o celé 2,5 kg na každé straně je moc. Hodí se hlavně na tlak nad hlavu nebo bench press, kde se váha zvyšuje pomaleji.</p>'
          '<h2>Barvy a průměr bumper kotoučů</h2>'
          '<p>Soutěžní a závodní bumper kotouče podle pravidel Mezinárodní vzpěračské federace IWF mají vnější průměr 450 mm a barevné značení: 10 kg zelená, 15 kg žlutá, 20 kg modrá a 25 kg červená. Řada tréninkových kotoučů tyto barvy přebírá, mnoho výrobců však dělá kotouče jen černé s barevným nápisem. Barva je tak jen orientace, vždy kontrolujte číslo hmotnosti na kotouči.</p>'
          '<p>Kalibrované kotouče mají velmi malou odchylku od uvedené hmotnosti a používají se v soutěžích. Na domácí trénink stačí tréninkové, u kterých výrobce uvádí větší toleranci.</p>'
          '<h2>Osy: olympijské, rovné, EZ a jednoruční</h2>'
          + T(['Osa', 'Typické parametry', 'Použití'], [
              ['Olympijská pánská', '220 cm, 20 kg, úchop 28 mm, konce 50 mm', 'dřep, mrtvý tah, bench, vzpírání'],
              ['Olympijská ženská', '201 cm, 15 kg, úchop 25 mm, konce 50 mm', 'vzpírání a silový trénink žen'],
              ['Kratší olympijské', 'zhruba 120–200 cm, lehčí', 'menší prostory, domácí stojany'],
              ['Rovná osa 30 mm', 'často se závitem a maticemi', 'domácí posilování s 30mm kotouči'],
              ['EZ (lomená) osa', 'zalomený úchop', 'bicepsový zdvih, tricepsové cviky'],
              ['Jednoruční osa', 'krátká, 30 nebo 50 mm', 'vlastní jednoruční činky z kotoučů']]) +
          '<p>Rozměry kratších os se liší podle výrobce, proto před koupí změřte rozteč háků na stojanu nebo lavici. Výrobci u os uvádějí nosnost, tedy maximální zátěž. Údaj se nedá porovnávat napříč značkami do detailu, ale vypovídá o tom, pro jaké zatížení je osa stavěná. Do sady kotoučů s 30mm otvorem se dají dokoupit i <a href="/jednorucni-cinky/">jednoruční činky</a> na stejný systém.</p>'
          '<h2>Uzávěry</h2>'
          '<p>Kotouče se na ose vždy zajišťují. Používají se pružinové svorky, plastové rychlouzávěry s páčkou nebo šroubovací matice na osách se závitem. Uzávěr musí odpovídat průměru konce osy, tedy 25, 30 nebo 50 mm. Nezajištěné kotouče se při nerovném zdvihu sesunou a osa se prudce překlopí na jednu stranu.</p>'
          '<h2>Kolik kotoučů pořídit</h2>'
          '<p>Kotouče se kupují v párech, aby byla osa vyvážená. Na začátek stačí několik párů od menších hmotností po větší, které dovolí plynule přidávat. Kdo plánuje dřep a mrtvý tah, potřebuje víc zátěže než ten, kdo cvičí převážně horní polovinu těla. Před nákupem si spočítejte i hmotnost osy, protože ta se do celkové zátěže započítává.</p>'
          '<h2>Podlaha a bezpečnost</h2>'
          '<ul><li>Pod činky dejte pryžovou podložku nebo desky, zvlášť pokud cvičíte v bytě. Litina na dlažbě nebo parketách nadělá škody.</li>'
          '<li>Litinové a pogumované kotouče nepouštějte z výšky, na to jsou bumper kotouče a vzpěračská plocha.</li>'
          '<li>Na bench press a dřep s větší váhou používejte stojan s bezpečnostními zarážkami nebo dopomoc.</li>'
          '<li>Kotouče skladujte na stojanu, ne opřené o zeď, kde se mohou svalit na nohy nebo na dítě.</li>'
          '<li>Nepřekračujte nosnost osy, stojanu ani lavice.</li></ul>'
          '<p>Technika dřepu nebo mrtvého tahu se nejlépe učí s trenérem. Kdo má zdravotní potíže nebo se vrací po zranění, měl by se před silovým tréninkem poradit s lékařem.</p>'
          '<h2>Nakládání a sundávání kotoučů</h2>'
          '<p>Kotouče nasazujte střídavě na obě strany osy, aby se činka ve stojanu nepřevrátila. Platí to i při sundávání: když z jedné strany odeberete všechno a druhá zůstane plně naložená, osa se může z háků vyklopit. Těžší kotouče patří blíž ke středu, lehčí ven, aby uzávěr dosedl. Velké kotouče zvedejte z podřepu s rovnými zády, ne předklonem z natažených nohou.</p>'
          '<h2>Posilování v bytě</h2>'
          '<p>V paneláku nebo podkrovním bytě rozhoduje hluk a nosnost podlahy. Pogumované kotouče jsou tišší než holá litina a pod pryžovou podložkou se zvuk ještě ztlumí. Činku pokládejte, nepouštějte, a cviky jako mrtvý tah dělejte s kotouči, které při dosednutí nezvoní. Kdo potřebuje šetřit místo, zvolí tenčí litinové kotouče a kratší osu, které se vejdou do rohu místnosti.</p>'
          '<h2>Péče o kotouče a osy</h2>'
          '<p>Litinové kotouče s nátěrem mohou na odřených místech rezivět, proto je skladujte v suchu, ne ve vlhkém sklepě nebo garáži bez větrání. Osu po tréninku otřete od potu a magnezia, rýhování se dá vyčistit tuhým kartáčkem. Pravidelně kontrolujte, zda se otočné konce olympijské osy volně točí a zda nejsou kotouče prasklé. U bumper kotoučů sledujte, jestli se neuvolňuje kovový střed.</p>'
          '<h2>Osy pro konkrétní cviky</h2>'
          '<p>Vedle rovných a lomených os nabízejí e-shopy i speciální tvary. Šestihranná osa, často označovaná jako hex nebo trap bar, se při mrtvém tahu obstoupí zevnitř rámu, takže zátěž je blíž těžišti a úchop je neutrální. Multiúchopová osa má několik rovnoběžných rukojetí a dovolí tlaky s dlaněmi proti sobě. Tricepsová osa má uzavřený rám s příčnými úchopy. Lehké krátké osy s malými kotouči se používají při skupinových lekcích zaměřených na vytrvalost. Speciální osy mají většinou olympijské konce, proto si ověřte, zda vaše kotouče pasují.</p>'
          '<h2>Stojany, háky a trny</h2>'
          '<p>Než koupíte osu a kotouče, ověřte, jestli se hodí ke stojanu nebo lavici, kterou máte. Rozteč háků musí odpovídat délce úchopové části osy, jinak se kotouče opřou o stojan. Stojany na kotouče mají trny určené pro konkrétní průměr otvoru, takže olympijské kotouče na trny pro 30mm kotouče nenasadíte. Kdo začíná s 30mm systémem a později plánuje přejít na olympijský, měl by s tím počítat už při výběru stojanu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kotouče s otvorem 30 mm koupené k olympijské ose nebo naopak.</li>'
          '<li>Cvičení bez uzávěrů.</li>'
          '<li>Pouštění litinových kotoučů na podlahu.</li>'
          '<li>Dlouhá olympijská osa do místnosti, kam se nevejde.</li>'
          '<li>Nákup jen velkých kotoučů bez menších na postupné přidávání.</li></ul>'
          '<p>K činkám se hodí <a href="/posilovaci-lavice/">posilovací lavice</a>, kompaktní <a href="/posilovaci-veze/">posilovací věže</a> a pro funkční trénink <a href="/kettlebelly/">kettlebelly</a>. Další vybavení najdete v sekci <a href="/fitness/">fitness a posilování</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi kotouči 30 mm a 50 mm?', 'Kotouče s otvorem 30–31 mm patří na běžné domácí osy 30 mm, kotouče 50–51 mm na olympijské osy. Navzájem nejsou zaměnitelné.'),
        ('Co je olympijský kotouč?', 'Kotouč s otvorem kolem 50 mm určený na olympijskou osu. Může být litinový, pogumovaný i bumper.'),
        ('Kolik váží olympijská osa?', 'Pánská olympijská osa dlouhá 220 cm váží 20 kg, ženská 15 kg. Kratší olympijské osy jsou lehčí podle délky.'),
        ('Co jsou bumper kotouče?', 'Pryžové kotouče se stejným průměrem u větších hmotností. Jsou stavěné na pouštění z výšky na vhodnou podložku, hlavně při vzpírání.'),
        ('Můžu pouštět pogumované kotouče na zem?', 'Pogumování chrání podlahu při položení, ale na pouštění ze záhlaví určené není. Na to slouží bumper kotouče.'),
        ('Co znamenají barvy kotoučů?', 'Podle pravidel IWF je 10 kg zelená, 15 kg žlutá, 20 kg modrá a 25 kg červená. Tréninkové kotouče barvy dodržovat nemusí, platí číslo na kotouči.'),
        ('K čemu je EZ osa?', 'Zalomený úchop ulehčuje polohu zápěstí při bicepsovém zdvihu a tricepsových cvicích. Vyrábí se pro 30 mm i olympijské kotouče.'),
        ('Jaké uzávěry na osu potřebuji?', 'Uzávěry podle průměru konce osy: 25, 30 nebo 50 mm. Používají se pružinové, rychloupínací nebo šroubovací.'),
        ('Proč mají kotouče otvor 31 mm nebo 51 mm?', 'Otvor je o něco větší než osa, aby se kotouč dal nasunout. Kotouč 31 mm patří na osu 30 mm, kotouč 51 mm na olympijskou.'),
        ('Kde porovnat kotouče a osy?', 'Sporteka u každého kotouče a osy ukazuje nabídky českých e-shopů a dostupné hmotnosti. Nakupujete v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ zavazi-na-kotniky
NEW['zavazi-na-kotniky'] = dict(long=True,
    title='Závaží na kotníky a zápěstí: neoprenová i silikonová',
    desc='Závaží na nohy, kotníky a zápěstí od 0,5 kg, neoprenové s pískem, nastavitelné i silikonové. Jak zvolit hmotnost, upnout je a kdy být opatrní.',
    intro='<p><strong>Závaží na kotníky a zápěstí</strong> jsou manžety s náplní, které se upnou kolem nohy nebo ruky a přidají cvikům odpor. Používají se při posilování nohou a hýždí v lehu i na všech čtyřech, v pilatesu, kondičním cvičení nebo při lehkém posilování paží. Bývají z neoprenu nebo nylonu s pískem či kovovou drtí uvnitř, novější typ tvoří silikonové náramky. Prodávají se obvykle v páru, nejčastěji v hmotnostech od půl kilogramu do několika kilogramů na kus.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů u konkrétního páru závaží. Objednáte pak v obchodě, jehož nabídku si zvolíte. Najdete tu zátěže značek '
          + B(('hms', 'HMS'), ('merco', 'Merco'), ('adidas', 'Adidas')) +
          ', dále Tunturi, Xtrexo, Sedco nebo Sharp Shape. Kategorie patří do sekce <a href="/cinky-a-kotouce/">činky a kotouče</a> a navazuje na <a href="/fitness-pomucky/">fitness pomůcky</a>.</p>',
    guide='<h2>Druhy závaží</h2>'
          + T(['Typ', 'Konstrukce', 'Na co se hodí'], [
              ['Manžeta s pískem nebo drtí', 'neopren či nylon, plnivo ve švech, suchý zip', 'cviky na nohy v lehu, kondiční cvičení'],
              ['Nastavitelná manžeta', 'kapsičky s vyjímatelnými závažími', 'postupné přidávání, sdílení v rodině'],
              ['Silikonový náramek', 'pružný kruh nebo pásek s kovovou náplní', 'pilates, barre, lehké posilování paží'],
              ['Univerzální sada', 'stejný pár na zápěstí i kotník', 'domácí cvičení s různými cviky']]) +
          '<p>Klasická manžeta je nejlevnější na výrobu i nejrozšířenější. Nastavitelná varianta dovolí začít s nižší váhou a přidávat, když cvik přestane být výzvou. Silikonové náramky se snadno omývají a nemají suchý zip, zato je obvykle najdete jen v nižších hmotnostech.</p>'
          '<h2>Jak číst hmotnost na obalu</h2>'
          '<p>Údaj „2 × 1 kg“ znamená pár, ve kterém váží každá manžeta jeden kilogram. Nejde tedy o dvě kila na noze. Některé sady jsou jen pro zápěstí, jiné výrobce označuje jako univerzální pro zápěstí i kotník. Pro kotník bývá potřeba delší pásek, proto u zápěstních modelů kontrolujte obvod, na který stačí.</p>'
          '<h2>K čemu se závaží používají</h2>'
          '<ul><li><strong>Nohy a hýždě</strong>: unožování v lehu na boku, zanožování na všech čtyřech, zvedání natažené nohy v lehu na zádech.</li>'
          '<li><strong>Pilates a barre</strong>: malé kontrolované pohyby, kde i půl kilogramu udělá rozdíl.</li>'
          '<li><strong>Paže a ramena</strong>: kroužení a předpažování v lehké zátěži, kdy se jednoruční činka hůř drží.</li>'
          '<li><strong>Kondiční cvičení doma</strong>: doplněk k cvičení s vlastní vahou.</li></ul>'
          '<p>Závaží na kotníku působí na dlouhé páce. Proto i lehká manžeta citelně ztěžuje cvik s nataženou nohou. Pohyb provádějte pomalu a pod kontrolou, ne švihem.</p>'
          '<h2>Jak zvolit hmotnost</h2>'
          '<p>Na začátek se volí lehčí zátěž, typicky 0,5 až 1 kg na manžetu. Těžší kusy kolem 2 až 5 kg dávají smysl u silových cviků v lehu a u lidí, kteří už cvičí pravidelně. Kdo neví, jakou váhu zvolit, udělá lépe s nastavitelnou manžetou. Zátěž je správná, když zvládnete plánovaný počet opakování v plném rozsahu a bez prohýbání beder.</p>'
          '<h2>Upnutí a pohodlí</h2>'
          '<p>Manžeta na kotník se upíná nad kotník, ne přes kostěný výběžek. Má sedět pevně, aby neklouzala, ale nesmí škrtit. Na zápěstí se nasazuje nad kloub, aby ruka mohla volně ohýbat. Pásek se suchým zipem a kroužkem pro přitažení drží spolehlivěji než samotný suchý zip. U širších kotníků nebo silnějších zápěstí si ověřte délku pásku v popisu.</p>'
          '<h2>Kdy být opatrní</h2>'
          '<p>S těžším závažím na kotnících neběhejte a neskákejte, pokud vám to výslovně nedoporučil odborník. Fyzioterapeuti upozorňují, že zátěž na konci nohy mění krok a zvyšuje zatížení kotníků, kolen a kyčlí. Podobně opatrně se k závažím přistupuje při rychlé chůzi a chůzi do schodů. Mnohem vhodnější jsou na kontrolované posilovací cviky v klidném tempu.</p>'
          '<p>Kdo má potíže s klouby, osteoporózu, se zotavuje po úrazu nebo má jiné zdravotní omezení, má se před cvičením se zátěží poradit s lékařem nebo fyzioterapeutem. Závaží nejsou zdravotnická ani rehabilitační pomůcka. Pokud je fyzioterapeut do cvičení zařadí, řiďte se jeho pokyny ohledně hmotnosti i cviků. Při bolesti cvičení přerušte.</p>'
          '<h2>Péče</h2>'
          '<p>Neoprenové a nylonové manžety s pískem do pračky nepatří. Otřete je vlhkým hadříkem a nechte uschnout. Silikonové náramky se dají opláchnout vodou s mýdlem. Občas zkontrolujte švy a suchý zip: jakmile se šev otevře, začne se sypat plnivo a manžeta ztrácí hmotnost i tvar. Skladujte je v suchu, vlhko škodí lepidlu i suchému zipu.</p>'
          '<h2>Alternativy a doplňky</h2>'
          '<p>Podobný odpor dají <a href="/posilovaci-gumy/">posilovací gumy</a>, které se dají rozprostřít kolem kolen nebo kotníků. Na paže je často praktičtější jednoruční činka z kategorie <a href="/jednorucni-cinky/">jednoruční činky</a>, na pilates zase kruhy a míče z <a href="/pilates-pomucky/">pilates pomůcek</a>. Pro cvičení vleže se hodí kvalitní <a href="/joga-a-podlozky/">podložka</a>.</p>'
          '<h2>Jak zařadit závaží do cvičení</h2>'
          '<p>Nejdřív se zahřejte bez zátěže, například chůzí na místě nebo krouživými pohyby v kloubech. Každý cvik si nejprve vyzkoušejte bez závaží, abyste měli jistotu v rozsahu a poloze těla. Pak manžety nasaďte a cvičte v klidném tempu s krátkou pauzou mezi sériemi. Zátěž zvyšujte až ve chvíli, kdy cvik zvládnete s dobrou technikou, a to po malých krocích. Pokud se začnete prohýbat v bedrech nebo zvedat nohu švihem, je závaží příliš těžké.</p>'
          '<h2>Závaží na zápěstí při aerobiku a tanci</h2>'
          '<p>Lehké manžety na zápěstí se objevují v aerobních a tanečních lekcích. I tady platí, že by měly být lehké a pohyby kontrolované. Prudké švihy s nataženou paží zatěžují ramena a lokty víc, než se zdá. Kdo má potíže s rameny nebo zápěstím, měl by se před cvičením se zátěží poradit s fyzioterapeutem. Pro silové cviky na paže je často vhodnější malá činka, kterou máte pevně v ruce.</p>'
          '<h2>Na co se dívat v popisu</h2>'
          '<ul><li><strong>Hmotnost jednoho kusu</strong>: zda údaj platí pro manžetu, nebo pro celý pár.</li>'
          '<li><strong>Obvod</strong>: rozsah, na který pásek dosáhne, hlavně u kotníků.</li>'
          '<li><strong>Nastavitelnost</strong>: počet vyjímatelných dílků a nejmenší krok.</li>'
          '<li><strong>Materiál</strong>: neopren, nylon, nebo silikon, a jestli má manžeta měkkou vnitřní stranu.</li>'
          '<li><strong>Zapínání</strong>: suchý zip s kroužkem, nebo navlékací náramek.</li></ul>'
          '<p>Pro děti závaží obvykle nejsou potřeba. Starší lidé by je měli zařadit až po domluvě s lékařem nebo fyzioterapeutem, zvlášť pokud mají potíže s rovnováhou či klouby.</p>'
          '<h2>Manžety na kladku nejsou závaží</h2>'
          '<p>V nabídce posilování se objevují i kotníkové manžety s kovovým kroužkem, které se připínají ke kladce posilovací věže nebo stroje. Ty samy nic neváží, slouží jen k uchycení lanka. Pokud hledáte zátěž na volné cvičení doma, dívejte se na údaj o hmotnosti. Pokud máte doma <a href="/posilovaci-veze/">posilovací věž</a> s kladkou, hodí se naopak manžeta s kroužkem.</p>'
          '<h2>Zátěžová vesta a závaží na kotníky</h2>'
          '<p>Zátěžová vesta rozkládá hmotnost na trup, tedy blíž těžišti. Mění pohyb nohou méně než manžety na kotnících, a proto se používá spíš při chůzi nebo cvičení s vlastní vahou. I u vesty ale platí, že začít se má s malou hmotností a při potížích se zády nebo klouby se poradit s odborníkem. Závaží na kotníky se naopak hodí tam, kde chcete zatížit konkrétní pohyb nohy.</p>'
          '<h2>Životnost</h2>'
          '<p>Nejrychleji se opotřebí suchý zip, který časem přestane držet, a švy kolem kapes s plnivem. Manžety, které se často nosí na boso nebo na zpocenou pokožku, mohou ztratit tvar a začít zapáchat. Silikonové náramky vydrží déle, ale při ohýbání ostrými hranami se mohou natrhnout. Poškozenou manžetu s vysypaným plnivem raději vyměňte, protože ztrácí rovnováhu a hůř drží na noze.</p>'
          '<h2>Poloha těla při cvicích vleže</h2>'
          '<p>Většina cviků se závažím na kotnících se dělá vleže nebo na všech čtyřech, proto se hodí měkká podložka. Při unožování v lehu na boku mějte boky nad sebou a nepřetáčejte pánev dozadu. Na všech čtyřech držte záda rovně a břicho zpevněné, aby se bedra neprohýbala. Dýchejte plynule a nezadržujte dech. Pohyb zastavte v místě, kde ho ještě ovládáte, a nohu spouštějte pomalu, ne volným pádem. Mezi sériemi si manžety klidně nechte na noze, ale po cvičení je sundejte.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Běh nebo skákání s těžkými závažími na kotnících.</li>'
          '<li>Příliš těžká zátěž, kvůli které se cvik dělá švihem.</li>'
          '<li>Manžeta upnutá přes kotník tak pevně, že brní noha.</li>'
          '<li>Záměna hmotnosti jednoho kusu a celého páru.</li>'
          '<li>Praní manžet s pískem v pračce.</li></ul>',
    faq=[
        ('Jakou váhu závaží na kotníky zvolit?', 'Na začátek obvykle 0,5 až 1 kg na manžetu. Těžší kusy se hodí pro zkušenější cvičence a silové cviky v lehu.'),
        ('Můžu běhat se závažím na kotnících?', 'S těžším závažím se to nedoporučuje. Mění krok a zatěžuje klouby. Pokud vám ho nedoporučil odborník, používejte závaží jen na kontrolované cviky.'),
        ('Co znamená 2 × 1 kg?', 'Jde o pár, každá manžeta váží 1 kg. Na jedné noze nebo ruce tedy máte jeden kilogram.'),
        ('Dají se závaží použít na zápěstí i kotníky?', 'Univerzální sady ano. U zápěstních modelů kontrolujte délku pásku, na kotník bývá potřeba delší.'),
        ('Jsou závaží na nohy vhodná při bolesti kloubů?', 'Při potížích s klouby nebo po úrazu se nejprve poraďte s lékařem či fyzioterapeutem. Závaží nejsou zdravotnická pomůcka.'),
        ('Pomůže chůze se závažím na nohou?', 'Fyzioterapeuti k ní bývají zdrženliví, protože zatěžuje kotníky a kolena a mění krok. Vhodnější jsou posilovací cviky v pomalém tempu.'),
        ('Jak závaží na kotníky upnout?', 'Nad kotník, pevně, ale bez škrcení. Pásek s kroužkem drží lépe než jen suchý zip.'),
        ('Dají se závaží s pískem prát?', 'V pračce ne. Otřete je vlhkým hadříkem a nechte uschnout, silikonová stačí opláchnout.'),
        ('Jaký je rozdíl mezi neoprenovými a silikonovými závažími?', 'Neoprenové manžety se upínají suchým zipem a bývají i těžší. Silikonové náramky se snadno myjí, obvykle ale mají nižší hmotnost.'),
        ('Stačí jeden pár závaží?', 'Pro domácí cvičení obvykle ano, pokud je nastavitelný. U pevných manžet si časem lidé dokupují druhý, těžší pár, aby mohli zátěž postupně zvyšovat.'),
        ('Kde porovnat závaží na kotníky?', 'Sporteka u každého páru ukazuje nabídky českých e-shopů. Objednávku dokončíte v obchodě, který si zvolíte.'),
    ])
