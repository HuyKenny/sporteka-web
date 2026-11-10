"""sporteka.cz — wave 23d (4. 11. 2026): long texts (>= 1650 words) for lyzarske-cepice-a-nakrcniky, tanecni-obleceni, rodinne-stany, skladaci-elektrokola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-cepice-a-nakrcniky
NEW['lyzarske-cepice-a-nakrcniky'] = dict(long=True,
    title='Lyžařské čepice, nákrčníky a kukly: výběr a porovnání',
    desc='Lyžařské čepice, nákrčníky, čelenky a kukly pod helmu i mimo ni. Jak vybrat materiál, tloušťku a velikost a porovnat nabídky českých obchodů.',
    intro='<p>Hlava a krk bývají při jízdě na svahu vystavené větru, a proto je důležité je chránit. Správná čepice, nákrčník nebo kukla proto rozhodují o tom, jestli vydržíte celý den na sjezdovce, nebo se po dvou jízdách schováte v chatě. Sporteka porovnává nabídky českých obchodů u pletených čepic, tenkých čepic pod helmu, fleecových nákrčníků, kukel i multifunkčních šátků a ukazuje, co se skutečně prodává.</p>'
          '<p>V kategorii najdete značky ' + B(('wedze', 'Wedze'), ('beany', 'Beany'), ('lemon-explore', 'Lemon Explore'), ('rossignol', 'Rossignol'), ('the-north-face', 'The North Face'), ('4f', '4F'), ('rockbros', 'Rockbros')) +
          '. K hlavě se hodí <a href="/lyzarske-helmy/">lyžařské helmy</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a> a <a href="/lyzarske-rukavice/">rukavice</a>, celé vybavení doplní <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>',
    guide='<h2>Co všechno do kategorie patří</h2>'
          '<p>Pod pojmem lyžařská pokrývka hlavy se skrývá několik různých kousků a každý řeší trochu jiný problém. Klasická pletená čepice se nosí na sjezdovce bez helmy, při pěší chůzi a v lyžařském areálu mezi jízdami. Tenká čepice pod helmu je z pružné pleteniny nebo fleecu a tvoří jen jemnou vrstvu mezi hlavou a skořepinou. Nákrčník je tubus z elastického materiálu, který se navlékne přes hlavu a chrání krk i bradu. Kukla spojuje čepici a nákrčník do jednoho kusu a při silném větru zakryje i část tváře. K tomu přibývají čelenky pro aktivní jízdu a trojúhelníkové šátky.</p>'
          + T(['Typ', 'Hlavní výhoda', 'Kdy ho zvolit'], [
              ['Pletená čepice', 'teplo a styl, snadno se nasazuje', 'procházky, pauzy, jízda bez helmy'],
              ['Tenká čepice pod helmu', 'minimální objem, těsné přilnutí', 'sjezdové lyžování s helmou'],
              ['Nákrčník', 'chrání krk, jde stáhnout na bradu i nos', 'vítr, vleky, rychlé sjezdy'],
              ['Kukla', 'jedna vrstva pro hlavu i krk', 'silný mráz, vysoké hory'],
              ['Čelenka', 'zakryje uši, hlava se nepřehřívá', 'běžky, skialpinismus, jarní lyžování']]) +
          '<h2>Jak vybrat podle způsobu použití</h2>'
          '<h3>Sjezdové lyžování s helmou</h3>'
          '<p>Helma přebírá část ochrany před větrem, proto stačí tenká a pružná čepice. Silná pletená čepice pod skořepinou způsobí, že helma sedí vysoko a při pádu se může posunout. Zkoušejte čepici vždy s helmou, kterou budete používat, a ověřte, že švy netlačí na čelo ani nad uši. Pokud potřebujete helmu vybrat teprve teď, prohlédněte si nabídku <a href="/lyzarske-helmy/">lyžařských helem</a>. Mnoho lidí kombinuje tenkou čepici s nákrčníkem, který zakryje krk a umožní regulovat teplo během dne.</p>'
          '<h3>Snowboard a freeride</h3>'
          '<p>Snowboardisté často padají a sedí ve sněhu, proto oceňují čepici, která se nemění v mokrý hadr. Pro hlubší sníh a lesní pasáže se hodí kukla nebo nákrčník, který zabrání vniknutí sněhu za límec. U <a href="/lyzarske-bundy/">lyžařských bund</a> sledujte, aby kapuce sedla přes helmu a nákrčník se k ní dal přizpůsobit, jinak vznikne mezi bundou a čepicí nechráněné místo.</p>'
          '<h3>Běžky a skialpinismus</h3>'
          '<p>Při pohybu do kopce se tělo zahřívá rychle a nejhorší chyba je nosit příliš teplou čepici. Vhodnější je tenká čelenka nebo lehká čepice, která dobře odvádí pot. Při sjezdu si pak stačí navléknout nákrčník nebo přidat tenkou čepici. Materiál musí rychle schnout, protože zvlhlá pokrývka hlavy v mrazu prudce chladne.</p>'
          '<h3>Děti na svahu</h3>'
          '<p>Dětské čepice by měly mít měkký lem bez tlačících švů, zakrývat uši a nesmí kloužit do očí. Pro malé děti je praktické zavazování nebo pružný nákrčník, který nelze ztratit. Děti se potí a rychle prochládají, proto je vhodné mít v batohu náhradní suchou čepici. K dětskému vybavení se hodí i <a href="/lyzarske-termopradlo/">termoprádlo</a> a <a href="/lyzarske-kombinezy/">kombinézy</a>.</p>'
          '<h2>Materiály: co hřeje a co ne</h2>'
          '<p>Materiál určuje teplo, váhu, odvod potu i to, jak čepice zapáchá po třetím dni na horách. Žádný není dokonalý, vždy jde o kompromis.</p>'
          + T(['Materiál', 'Výhody', 'Nevýhody'], [
              ['Merino vlna', 'hřeje i vlhká, méně zapáchá, příjemná na dotek', 'pomaleji schne, citlivější na praní a mechanické poškození'],
              ['Syntetika (polyester, polyamid)', 'rychle schne, pevná, snadná údržba', 'časem pohlcuje pachy'],
              ['Fleece', 'lehký, měkký, dobře izoluje', 'propouští vítr, pokud nemá větruodolnou membránu'],
              ['Akryl a směsi s vlnou', 'běžná pletenina, barevné vzory', 'méně prodyšný než merino'],
              ['Bavlna', 'příjemná v suchu', 'nasákne a rychle chladne, na svah se nehodí']]) +
          '<p>Větruodolná vložka v oblasti uší pomůže na vrcholu, kde fouká. Plnohodnotná membrána ale snižuje prodyšnost, takže se hodí hlavně na odpočinek nebo pomalou jízdu. Podšívka z jemného fleecu zlepšuje komfort, ale zvyšuje objem pod helmou.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Čepice se vybírá podle obvodu hlavy měřeného přes čelo a nad ušima. Pletenina je pružná, přesto jedna univerzální velikost nesedí všem. Příliš těsná čepice vyvolá tlak a bolest hlavy, příliš volná se sesouvá a nechává uši nechráněné. U nákrčníků je důležitá délka tubusu: delší se dá přeložit na dvojitou vrstvu a v mrazu zahřeje víc. Kukly mají otvor pro obličej, který nesmí tlačit na nos a brýle. Zkuste si ji s <a href="/lyzarske-bryle/">lyžařskými brýlemi</a>, protože okraj často určuje, jestli se brýle budou zamlžovat.</p>'
          '<h2>Značky, které v kategorii najdete</h2>'
          '<p>Nabídku tvoří směs sportovních značek a specializovaných výrobců. ' + B(('wedze', 'Wedze'), ('rossignol', 'Rossignol'), ('the-north-face', 'The North Face'), ('4f', '4F')) +
          ' nabízejí klasické lyžařské pokrývky hlavy, často sladěné s bundami a rukavicemi. ' + B(('beany', 'Beany'), ('lemon-explore', 'Lemon Explore')) +
          ' jsou zastoupeny hlavně pletenými čepicemi s výraznými vzory. Mezi menšími značkami najdete ' + B(('siroko', 'Siroko'), ('sulov', 'Sulov'), ('litex', 'Litex'), ('rockbros', 'Rockbros')) +
          ', které ukazují typické fleecové kukly a nákrčníky. Při porovnání nabídek sledujte nejen cenu, ale i materiál a velikost, protože stejně vypadající kousky se mohou lišit složením.</p>'
          '<h2>Jak o čepice a nákrčníky pečovat</h2>'
          '<p>Většinu pletených a fleecových kousků lze prát v pračce na šetrný program při nízké teplotě. Merino vyžaduje jemný prací prostředek bez aviváže, protože avivážní látky zanášejí vlákna a snižují odvod vlhkosti. Syntetické materiály snesou běžné prací prostředky, přesto je nesušte na radiátoru ani v sušičce na vysokou teplotu, protože se deformují a ztrácejí pružnost. Po dni na svahu čepici vyvěste, aby vyschla, a nenechávejte ji v batohu vlhkou. Nákrčník s reflexními nebo potištěnými prvky perte naruby.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li><strong>Příliš tlustá čepice pod helmu:</strong> helma sedí volně a ztrácí ochranu.</li>'
          '<li><strong>Bavlna na svahu:</strong> po zpocení rychle chladne a způsobuje promrznutí.</li>'
          '<li><strong>Jediná silná vrstva:</strong> při změně teploty se nedá regulovat, lepší je tenká čepice a nákrčník zvlášť.</li>'
          '<li><strong>Zapomenuté uši:</strong> uši a čelo omrzají nejdřív, proto je při větru kryjte.</li>'
          '<li><strong>Špatná velikost nákrčníku:</strong> příliš úzký tlačí na krk, příliš volný se sesouvá.</li>'
          '<li><strong>Nekontrolované švy:</strong> hrubý šev na čele způsobí otlaky, zvlášť pod helmou.</li></ul>'
          '<h2>Jak si složit vrstvy na hlavě a krku</h2>'
          '<p>Stejně jako u těla funguje i na hlavě princip vrstvení. Základ tvoří tenká čepice nebo čelenka, kterou doplníte nákrčníkem. Při mrazu přidáte kuklu přes helmu nebo kapuci bundy. Při slunném počasí stačí čelenka a nákrčník stažený na krku. Takové rozložení umožňuje reagovat na vítr, nadmořskou výšku i změny tempa. K celé výbavě patří také <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, aby tělo bylo chráněno rovnoměrně.</p>'
          '<h2>Co dalšího do batohu</h2>'
          '<p>Na celodenní výlet doporučujeme vzít náhradní tenkou čepici nebo nákrčník. Mokrou pokrývku můžete usušit v kapse bundy u těla, suchá slouží pro odpolední jízdy. K dispozici je i řada příslušenství v kategorii <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>, kde si pro mokré věci vyberete samostatnou kapsu.</p>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>Sporteka sbírá nabídky českých obchodů a sloučí identické modely do jedné karty, takže vidíte, kde je dostupná vaše velikost a barva. U čepic sledujte, zda obchod uvádí složení a zda je produkt skladem. Filtrujte podle značky a kategorie, a pokud hledáte kompletní set, přidejte do porovnání také <a href="/lyzarske-obleceni/">lyžařské oblečení</a>. Nepodléhejte jen slevě: čepice z kvalitního materiálu vydrží několik sezón, zatímco levná akrylová se vytahuje už po první.</p>',
    faq=[('Jakou čepici nosit pod lyžařskou helmu?', 'Tenkou, těsnou a pružnou, nejlépe z merina nebo syntetiky, aby odváděla pot. Silná pletená čepice zvedne helmu a zhoršuje její dosednutí.'),
         ('Je lepší nákrčník, nebo kukla?', 'Nákrčník se dá stáhnout na bradu a hodí se při proměnlivé teplotě. Kukla chrání víc, ale hůře se reguluje, proto se volí spíš do silného mrazu.'),
         ('Hodí se pletená čepice na lyže?', 'Ano, pokud jedete bez helmy nebo ji používáte při procházkách a v pauzách. Pod helmu se silná pletená čepice nehodí.'),
         ('Jak poznám správnou velikost?', 'Změřte obvod hlavy nad ušima a přes čelo a porovnejte s tabulkou výrobce. Čepice má sedět pevně, ale bez tlaku.'),
         ('Proč se vyhnout bavlně?', 'Bavlna nasákne potem a sněhem, pomalu schne a odebírá teplo. Na svah patří merino, syntetika nebo fleece.'),
         ('Jak prát lyžařské čepice a nákrčníky?', 'Šetrně při nízké teplotě, bez aviváže a bez sušičky na vysoký stupeň. Merino prát jemným prostředkem určeným na vlnu.'),
         ('Potřebují děti jinou čepici než dospělí?', 'Měkký lem bez tlačících švů, zakryté uši a dobré držení na hlavě jsou důležitější než silná izolace. Praktické je zavazování nebo pružný nákrčník.'),
         ('Co je multifunkční šátek?', 'Elastický tubus, který lze nosit jako nákrčník, čelenku, čepici nebo kuklu. Hodí se jako lehká vrstva do batohu na proměnlivé počasí.'),
         ('Zamlžují se brýle, když nosím kuklu?', 'Může se to stát, pokud výdech proudí nahoru podél nosu. Pomůže nákrčník s prodyšnou látkou, správné dosednutí brýlí a menší krytí nosu.'),
         ('Kolik kusů si vzít na celý den?', 'Alespoň jednu náhradní tenkou čepici nebo nákrčník. Vlhká pokrývka hlavy v mrazu rychle chladne a suchý kus výrazně zvýší komfort odpoledne.')],
)

# ------------------------------------------------------------------ tanecni-obleceni
NEW['tanecni-obleceni'] = dict(long=True,
    title='Taneční a baletní oblečení: trikoty, sukně, legíny',
    desc='Taneční a baletní oblečení pro děti i dospělé: trikoty, sukně, legíny a kraťasy. Jak vybrat velikost a materiál a porovnat nabídky obchodů.',
    intro='<p>Taneční a baletní oblečení má jednu hlavní funkci: nechat tělo volně se pohybovat a zároveň ukázat linii, kterou učitel potřebuje vidět. Trikot, sukně, legíny nebo kraťasy se proto vybírají podle stylu tance, věku a požadavků školy, ne jen podle barvy. Sporteka porovnává nabídky českých obchodů a v kategorii najdete baletní trikoty, sukýnky, zavinovací blůzy, dětské fitness a gymnastické oblečení i další kousky, které se při tanci a cvičení používají.</p>'
          '<p>Zastoupeny jsou značky ' + B(('domyos', 'Domyos'), ('puma', 'Puma'), ('papillon', 'Papillon'), ('kesi-w-oski', 'Kesi Włoski'), ('agama', 'Agama'), ('adidas', 'Adidas')) +
          '. K oblečení patří <a href="/baletni-obuv/">baletní obuv</a>, <a href="/tanecni-obuv/">taneční obuv</a> a <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>, vše najdete v sekci <a href="/tanec-a-gymnastika/">tanec a gymnastika</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Kategorie sdružuje oblečení určené pro balet, moderní a společenský tanec, aerobik, gymnastiku i dětské taneční kroužky. Hlavní skupinu tvoří baletní trikoty bez rukávů nebo s ramínky, dlouhé a krátké baletní sukně a zavinovací svetříky a blůzy, které se navlékají přes trikot během zahřátí. Dále tu jsou legíny, kraťasy a topy v elastických materiálech pro hip-hop a fitness tance. V nabídce se mohou objevit i sportovní trička a dresy, které eshopy zařadily do širšího výběru, ale pro tanec nejsou určené. U každého kusu proto stojí za to přečíst popis a ověřit, k čemu je určený.</p>'
          + T(['Kousek', 'K čemu slouží', 'Poznámka'], [
              ['Baletní trikot', 'základ oblečení na balet', 'sedí těsně, bez vložek a bez zbytečných ozdob'],
              ['Baletní sukýnka', 'doplněk trikotu na hodinách i vystoupení', 'krátká, dlouhá nebo zavinovací'],
              ['Zavinovací blůza', 'zahřátí svalů a ramen', 'nosí se přes trikot, snadno se sundá'],
              ['Legíny a kalhoty', 'moderní tanec, jazz, hip-hop', 'elastické, nepropínají se'],
              ['Kraťasy a top', 'aerobik, gymnastika, taneční kroužky', 'lehké, prodyšné, nepřekážejí pohybu']]) +
          '<h2>Balet: trikoty a sukně</h2>'
          '<p>Baletní oblečení je tradičně jednoduché a přiléhavé, protože učitel musí vidět polohu ramen, pánve a nohou. Většina škol stanovuje barvy: dívky často nosí černý, růžový nebo tmavomodrý trikot, chlapci bílé triko a černé legíny. Před nákupem se proto zeptejte v kroužku na dress code. Trikot má sedět na těle bez záhybů, ramínka nesmí řezat a výstřih se nemá při předklonu odchlipovat. U sukně je podstatné, aby nebyla příliš těžká a neomezovala práci nohou. Sukýnky z jemného šifonu jsou lehké, tuhý tyl vypadá efektně, ale hodí se spíš na vystoupení než na každodenní trénink.</p>'
          '<h2>Moderní tanec, jazz a hip-hop</h2>'
          '<p>Pro moderní a pouliční styly se hodí volnější a pružnější oblečení. Legíny mají vysoký pas, který se nesbalí při zvednutí nohy, a materiál se nesmí propínat při hlubokém dřepu. Kraťasy by měly mít dostatečně široký lem, aby neomezovaly pohyb, a top nebo tričko delší střih. Dostupné jsou také <a href="/leginy/">legíny</a> a další kousky, které se hodí i na fitness lekce. Na hip-hop volte praktické a pohodlné kousky, které vydrží odření o podlahu.</p>'
          '<h2>Gymnastika a aerobik</h2>'
          '<p>Gymnastické oblečení bývá z přiléhavých materiálů, které nepřekáží při převratech a mostech. U dívek jde o trikoty a kraťasy, u chlapců o lehké kalhoty a tričko. Při výběru sledujte pevné švy, rozumnou délku nohavic a kvalitní sedící lem. Pokud trénujete také doma, doplňte oblečení o <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>. U aerobiku a zumby stačí lehký top a legíny, které odvádějí pot.</p>'
          '<h2>Materiály a střihy</h2>'
          '<p>Taneční oblečení se šije z pružných materiálů, které se přizpůsobí tělu a po natažení se vrátí do tvaru. Základ tvoří směsi bavlny a elastanu, polyamid s elastanem a mikrovlákno.</p>'
          + T(['Materiál', 'Výhody', 'Na co dát pozor'], [
              ['Bavlna s elastanem', 'příjemná na kůži, prodyšná', 'pomaleji schne, může se vytahovat'],
              ['Polyamid s elastanem', 'hladký, pevný, pružný', 'méně savý, při dlouhém potu méně komfortní'],
              ['Mikrovlákno', 'rychle schne, lehké', 'může se elektrizovat'],
              ['Tyl a šifon', 'efektní na sukních', 'křehčí, vyžaduje šetrné praní'],
              ['Fleece a pletené svetříky', 'zahřátí před tréninkem', 'nehodí se na vlastní cvičení']]) +
          '<p>Střih ovlivňuje pohodlí víc než materiál. Trikot s širokými ramínky působí sportovněji a lépe drží prsa i zad, tenká ramínka jsou elegantnější. Hluboký výstřih zad vypadá dobře při vystoupení, ale na každodenní hodinu nemusí být praktický. Zkontrolujte, zda je rozkrok bez tlačících švů a zda lze oblečení snadno obléknout i dětem.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Děti rostou rychle, proto je pokušení kupovat o číslo větší. U tance to ale nefunguje: přílišná volnost vytváří záhyby, skrývá linii těla a trikot se sesouvá. Změřte výšku, obvod hrudníku, pasu a boků a porovnejte s tabulkou výrobce. Dětské velikosti bývají označeny věkem nebo výškou. Tabulky různých značek se liší, proto ověřte každou zvlášť. Dospělé oblečení nabízí běžné velikosti i sortiment ve větších číslech, například od značky ' + B(('kesi-w-oski', 'Kesi Włoski')) + '. Při váhání mezi dvěma velikostmi zvolte tu, která nestahuje a nezanechává otlaky.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Specializované taneční oblečení vyrábí například ' + B(('papillon', 'Papillon'), ('agama', 'Agama')) +
          ' s trikoty, sukněmi a zavinovacími kousky. Sportovní řadu pro děti a aerobik nabízejí ' + B(('domyos', 'Domyos'), ('decathlon', 'Decathlon')) +
          '. Univerzální sportovní značky ' + B(('puma', 'Puma'), ('adidas', 'Adidas'), ('under-armour', 'Under Armour'), ('errea', 'Errea')) +
          ' přidávají trička, kraťasy a legíny pro trénink. V nabídce jsou i kousky ' + B(('fanatics', 'Fanatics'), ('starever', 'Starever'), ('powershot', 'Powershot')) +
          ', u kterých se vyplatí zkontrolovat určení, protože nejde vždy o taneční produkt.</p>'
          '<h2>Jak o oblečení pečovat</h2>'
          '<p>Elastické materiály nemají rády horkou vodu a aviváž. Perte při nízké teplotě, nejlépe v ochranném pytlíku na jemné prádlo, aby se zip nebo háčky nezachytily o sítě. Tyl a šifon nikdy nemačkejte, nechte je volně uschnout. Nesušte na topení, pružnost se tím sníží. Sukýnku skladujte rozloženou nebo zavěšenou. Zvlášť děti si chtějí hned po hodině sundat vlhký trikot, aby je nezastudilo, proto mějte v tašce suché oblečení a svetřík.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li><strong>Nezjištěný dress code:</strong> škola může vyžadovat konkrétní barvu a střih.</li>'
          '<li><strong>Příliš velký trikot:</strong> vytváří záhyby a skrývá postoj.</li>'
          '<li><strong>Špatný materiál:</strong> tuhá tkanina bez pružnosti omezuje pohyb.</li>'
          '<li><strong>Zbytečné ozdoby:</strong> flitry a kamínky se při tréninku loupou a dráždí.</li>'
          '<li><strong>Zaměněné určení:</strong> fotbalový dres nebo fanouškovské tričko není taneční oblečení.</li>'
          '<li><strong>Přeprané kousky:</strong> aviváž a vysoká teplota zničí pružnost vláken.</li></ul>'
          '<h2>Pro koho je které oblečení</h2>'
          '<p>Pro začátečníky a nejmenší děti se hodí pohodlné a odolné kousky bez složitých střihů. Pokročilé tanečnice si vybírají střihy, které lépe podtrhují linii a vydrží každodenní trénink. Dospělé začátečnice ocení volnější legíny a topy, protože se v nich cítí pohodlně. Chlapci potřebují jednoduché a pružné kalhoty. Výběr obuvi řešte zvlášť: <a href="/baletni-obuv/">baletní obuv</a> a <a href="/tanecni-obuv/">taneční obuv</a> mají vlastní pravidla pro velikost.</p>'
          '<h2>Kde porovnávat nabídky</h2>'
          '<p>Sporteka shromažďuje nabídky českých obchodů a zobrazuje jejich dostupnost. U každého kousku zkontrolujte velikostní tabulku a materiál a při výběru velikosti počítejte s růstem dítěte. Pro hlubší výběr můžete vyhledat také v nadřazené sekci <a href="/tanec-a-gymnastika/">tanec a gymnastika</a> a pro cvičení doma zkontrolovat <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>',
    faq=[('Jaký trikot koupit na balet?', 'Přiléhavý, z pružného materiálu a v barvě, kterou škola vyžaduje. Měl by sedět bez záhybů a nesmí tlačit v podpaží ani v rozkroku.'),
         ('Potřebuje dítě na balet sukýnku?', 'Záleží na škole. Mnohé kroužky ji vyžadují jen na vystoupení a na hodinách stačí trikot a punčocháče nebo legíny.'),
         ('K čemu je zavinovací blůza?', 'Zahřeje ramena a záda při rozcvičení. Po zahřátí se snadno sundá, protože se zapíná přes trup.'),
         ('Jak vybrat velikost dětského tanečního oblečení?', 'Podle výšky a obvodů hrudníku, pasu a boků. Nekupujte o dvě čísla větší, oblečení by mělo přiléhat.'),
         ('Jaký materiál je na tanec nejlepší?', 'Elastická bavlna nebo polyamid s elastanem. Oba se přizpůsobí tělu a nebrání pohybu.'),
         ('Co nosit na hip-hop?', 'Volnější legíny nebo kalhoty, kraťasy a delší top. Důležité je, aby oblečení neomezovalo pohyb a nepropínalo se.'),
         ('Jak prát taneční oblečení?', 'Při nízké teplotě, bez aviváže a v ochranném pytlíku. Tyl a šifon nechte volně uschnout a nesušte je na topení.'),
         ('Hodí se fitness legíny na tanec?', 'Ano, pro moderní tanec a aerobik. Na balet obvykle potřebujete přiléhavé baletní legíny nebo punčocháče.'),
         ('Jaké oblečení pro dospělé začátečníky?', 'Pohodlné legíny, přiléhavý top nebo trikot a lehký svetřík. Volte materiály, které odvádějí pot a nebrání pohybu.'),
         ('Může se do kategorie dostat i sportovní dres?', 'Ano, některé obchody řadí široký sportovní textil i do tanečního oddílu. Vždy proto zkontrolujte popis a určení produktu.')],
)

# ------------------------------------------------------------------ rodinne-stany
NEW['rodinne-stany'] = dict(long=True,
    title='Rodinné a kempingové stany pro 4 až 10 osob',
    desc='Rodinné a kempingové stany pro 4 až 10 osob: tunelové, kopulové, s ložnicemi a předsíní. Jak vybrat velikost a vodní sloupec a porovnat obchody.',
    intro='<p>Rodinný stan je malý domov na dovolenou: musí pojmout spaní, uložení věcí i místo na přečkání deště. Proto se liší od lehkého turistického stanu, kde každé deko váží, a vybírá se podle komfortu, prostornosti a snadnosti stavby. Sporteka porovnává nabídky českých obchodů u tunelových, kopulových a prutových stanů s více ložnicemi, rychlorozkládacích modelů i velkých stanů pro 8 a více osob a ukazuje, co vám která konstrukce nabídne.</p>'
          '<p>V kategorii se objevují značky ' + B(('skandika', 'Skandika'), ('quechua', 'Quechua'), ('husky', 'Husky'), ('pinguin', 'Pinguin'), ('coleman', 'Coleman'), ('high-peak', 'High Peak'), ('nils-camp', 'NILS Camp')) +
          '. K stanu patří <a href="/stanove-kolky/">stanové kolíky</a>, <a href="/stanove-doplnky/">stanové doplňky</a> a <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</p>',
    guide='<h2>Druhy rodinných stanů</h2>'
          '<p>Základní dělení vychází z tvaru konstrukce a z toho, jak je stan rozdělen uvnitř. Tunelový stan má několik oblouků vedle sebe a nabízí nejvíc místa za danou hmotnost, často s odděleným obytným prostorem. Kopulový stan stojí samostatně a lépe se staví, ale poskytuje menší vnitřní objem. Prutový stan používá pevné trubky nebo prutové tyče a je stabilní, ale těžší. Rychlorozkládací modely se postaví během chvíle a hodí se na krátké pobyty.</p>'
          + T(['Typ', 'Výhody', 'Nevýhody'], [
              ['Tunelový stan', 'hodně místa, často více ložnic a předsíň', 'vyžaduje kolíky a vyztužení, citlivý na bok větru'],
              ['Kopulový stan', 'stabilní, rychlá stavba', 'menší vnitřní prostor'],
              ['Prutový stan', 'pevný, vysoký strop', 'vyšší hmotnost, větší sbalený rozměr'],
              ['Rychlorozkládací stan', 'stavba za minuty', 'větší objem, méně stabilní ve větru'],
              ['Stan s ložnicemi a předsíní', 'soukromí a skladování věcí', 'vyšší hmotnost a delší stavba']]) +
          '<h2>Jak vybrat velikost</h2>'
          '<p>Údaj o počtu osob označuje, kolik lidí se vejde vedle sebe na spací podložky, bez zavazadel. Pokud počítáte s většími spacáky a batohy v ložnici, vyberte stan o jednu velikost větší než počet cestujících. Čtyřčlenná rodina proto často sáhne po stanu pro pět nebo šest osob. Důležitá je také výška: pokud se v něm chcete pohybovat vzpřímeně, ověřte výšku ve středu. Předsíň nebo vestavěný společenský prostor se hodí na špatné počasí, kdy se jídlo a hry přesouvají pod střechu.</p>'
          '<h3>Počet ložnic</h3>'
          '<p>Stany s více ložnicemi nabízejí soukromí a tmavé spaní, hodí se pro rodiny s dětmi a skupiny přátel. Ložnice jsou odděleny textilními stěnami, které brání světlu. Tmavá ložnice pomáhá dětem spát ráno déle, když slunce rychle prohřeje stan. Více příček ale znamená menší sdílený prostor a delší stavbu.</p>'
          '<h2>Voděodolnost a materiály</h2>'
          '<p>Voděodolnost se udává v milimetrech vodního sloupce. Vyšší číslo znamená větší odolnost vůči dešti, ale samo o sobě není všechno: rozhoduje také kvalita zalepených švů, podlážka a ventilace. Podlážka má mít vyšší vodní sloupec než plachta, protože je namáhána váhou těla a stojící vodou. Dvouplášťový stan má vnitřní prodyšný stan a vnější voděodolný plášť, který snižuje kondenzaci uvnitř. Jednoplášťové stany jsou jednodušší, ale hůře odvádějí vlhkost.</p>'
          '<ul><li><strong>Polyester:</strong> nenasákne a drží barvu, je nejčastější.</li>'
          '<li><strong>Bavlna nebo polybavlna:</strong> dýchá a je tichá, ale těžší a delší schnutí.</li>'
          '<li><strong>Tyče:</strong> sklolaminát je levnější a pružný, hliník lehčí a pevnější.</li>'
          '<li><strong>Zipy a okna:</strong> kvalitní zipy a síťky proti hmyzu výrazně zlepšují komfort.</li></ul>'
          '<h2>Stavba, hmotnost a převoz</h2>'
          '<p>Rodinné stany váží často desítky kilogramů a po sbalení zaberou velkou část kufru. Před koupí zkontrolujte rozměr sbaleného stanu a ujistěte se, že se vejde do auta spolu s dalším vybavením. Stavba velkého stanu zabere i při zkušenosti desítky minut a je lepší ji zvládnout ve dvou. Zkuste si stan postavit doma na zahradě před první cestou, abyste se naučili postup a ověřili, že chybějící kolíky nebo lana nezkomplikují první noc.</p>'
          '<h2>Vybavení pod stanem</h2>'
          '<p>Stan je jen začátek. Pro pohodlné spaní potřebujete <a href="/karimatky-a-matrace/">karimatky a matrace</a> nebo nafukovací postele a vhodné <a href="/spaci-pytle/">spací pytle</a>. Pro vaření a sezení se hodí <a href="/kempingove-nadobi/">kempingové nádobí</a> a <a href="/kempingovy-nabytek/">kempingový nábytek</a>. K ukotvení kupte kvalitní <a href="/stanove-kolky/">stanové kolíky</a>, protože ty dodávané v balení často nestačí na tvrdou nebo písčitou půdu. Další užitečné drobnosti najdete ve <a href="/stanove-doplnky/">stanových doplňcích</a> a <a href="/kempingove-doplnky/">kempingových doplňcích</a>.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>Nejpočetnější je ' + B(('skandika', 'Skandika')) + ' s širokou řadou tunelových stanů s ložnicemi. Francouzská ' + B(('quechua', 'Quechua')) +
          ' nabízí stany s oblíbenými konstrukcemi pro rodiny i turisty a ' + B(('simond', 'Simond')) + ' odlehčené modely. České značky ' + B(('husky', 'Husky'), ('trimm', 'Trimm'), ('kubisport', 'Kubisport')) +
          ' zaměřují pozornost na praktické turistické a kempingové stany. ' + B(('coleman', 'Coleman'), ('pinguin', 'Pinguin'), ('high-peak', 'High Peak'), ('nils-camp', 'NILS Camp')) +
          ' doplňují nabídku s různými konstrukcemi a ' + B(('vidaxl', 'Vidaxl')) + ' pokrývá nenáročné víkendové použití. Pro lehčí varianty zkuste <a href="/turisticke-stany/">turistické stany</a>.</p>'
          '<h2>Jak pečovat o stan</h2>'
          '<p>Stan sbalte suchý. Pokud musíte balit mokrý, doma ho co nejdřív rozložte a nechte uschnout, jinak se objeví plíseň a zápach. Nepoužívejte agresivní čisticí prostředky, stačí vlažná voda a jemná houba. Prát v pračce se nedoporučuje, protože se poškodí impregnace. Před sezónou zkontrolujte šev a podlážku, případně ji přelepte páskou. Tyče po použití očistěte od písku, aby se spoje nezadrhávaly. Uložení v suchu a mimo přímé slunce prodlouží životnost plachty, protože UV záření postupně narušuje impregnaci.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Počet osob podle údaje výrobce:</strong> bez zavazadel se do něj vejdete, s nimi je těsný.</li>'
          '<li><strong>Podceněný vítr:</strong> velký stan chytá vítr jako plachta, proto potřebuje kvalitní kolíky a lana.</li>'
          '<li><strong>Špatná ventilace:</strong> bez větracích otvorů se uvnitř tvoří kondenzace.</li>'
          '<li><strong>Chybná podlážka:</strong> tenká podlážka praská na kamenité půdě, pomůže podložka.</li>'
          '<li><strong>Nezkoušená stavba:</strong> první stavba na kempu za deště je zbytečný stres.</li>'
          '<li><strong>Příliš těžký stan na převoz:</strong> zkontrolujte hmotnost i rozměr balení.</li></ul>'
          '<h2>Výběr podle typu kempování</h2>'
          '<p>Pro autokempink bez omezení hmotnosti volte velký tunelový nebo prutový stan s předsíní. Pokud jezdíte na festival nebo pobyt na jednu noc, zvažte rychlorozkládací stan, který se postaví samotný. Pro menší rodinu s malými dětmi se hodí stan s tmavou ložnicí, kde děti usnou i za světla. Pokud potřebujete jen stín nebo místo pro hry, podívejte se na <a href="/pristresky-a-party-stany/">přístřešky a party stany</a>. Pro menší děti na zahradu jsou určeny <a href="/detske-stany/">dětské stany</a>. Obecný přehled najdete v kategorii <a href="/stany/">stany</a> a širší výběr v sekci <a href="/kemping/">kemping</a>.</p>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>Sporteka sdružuje stejné modely z různých obchodů do jedné karty, takže vidíte, kdo má stan skladem. Sledujte údaje o vodním sloupci, počtu ložnic, hmotnosti a rozměrech sbaleného stanu. Pozor na různé označení: stejný model může být nabízen jako stan pro čtyři nebo pro šest osob, podle metody měření. Nesrovnávejte jen cenu, ale také příslušenství v balení, zda jsou součástí kolíky, tyče a lana.</p>',
    faq=[('Kolik osob se vejde do rodinného stanu?', 'Údaj výrobce platí pro osoby na karimatkách bez zavazadel. S výbavou počítejte s jednou velikostí navíc.'),
         ('Jaký vodní sloupec je potřeba?', 'Pro běžný kempink stačí střední hodnota, důležitější je kvalita švů a podlážky. Podlážka má mít vyšší odolnost než plachta.'),
         ('Je lepší tunelový, nebo kopulový stan?', 'Tunelový nabízí víc prostoru a ložnic, kopulový je stabilnější a rychlejší na stavbu. Záleží na počtu lidí a na větru v místě.'),
         ('Co znamená tmavá ložnice?', 'Textilní příčka a materiál, který propouští méně světla. Pomáhá s ranním spaním, když stan prohřeje slunce.'),
         ('Jak dlouho trvá postavit rodinný stan?', 'U menších modelů desítky minut, u velkých tunelových stanů déle, zvlášť poprvé. Lepší je stavět ve dvou.'),
         ('Co dělat s kondenzací uvnitř stanu?', 'Otevřete větrací otvory a při spaní nechte lehký průvan. Dvouplášťový stan kondenzaci omezuje lépe než jednoplášťový.'),
         ('Jak stan sbalit, když je mokrý?', 'Pokud musíte, rozložte jej doma co nejdřív. Zabalený mokrý stan začne plesnivět a zapáchat.'),
         ('Potřebuji kvalitní kolíky?', 'Ano, kolíky přiložené ke stanu často nestačí na tvrdou nebo písčitou půdu. Vyberte typ podle terénu a pevně ukotvěte všechna lana.'),
         ('Hodí se rodinný stan do hor?', 'Spíše ne. Je těžký a objemný a pro horské túry jsou vhodnější turistické nebo expediční stany.'),
         ('Jak často stan impregnovat?', 'Podle opotřebení. Pokud voda přestane perlit na plachtě, použijte impregnační přípravek na textil a stan před tím očistěte.')],
)

# ------------------------------------------------------------------ skladaci-elektrokola
NEW['skladaci-elektrokola'] = dict(long=True,
    title='Skládací elektrokola: výběr, baterie a porovnání',
    desc='Skládací elektrokola s motorem do bytu, auta i vlaku. Jak vybrat velikost kol, baterii, hmotnost a způsob skládání a porovnat obchody.',
    intro='<p>Skládací elektrokolo řeší jednu konkrétní situaci: potřebujete kolo s motorem, ale nemáte kam ho dát nebo ho musíte vozit v autě, ve vlaku či výtahu. Menší kola, kloub uprostřed rámu a sklopný řídítkový sloupek proto mění objemný stroj na kus zavazadla. Sporteka porovnává nabídky českých obchodů a v kategorii najdete jak městské skládačky s malými koly, tak robustnější modely s širokými pneumatikami nebo odpružením, které se skládají méně kompaktně.</p>'
          '<p>Zastoupeny jsou například značky ' + B(('engwe', 'Engwe'), ('fafrees', 'Fafrees'), ('samebike', 'Samebike'), ('dyu', 'DYU'), ('flebi', 'Flebi'), ('moma-bikes', 'Moma Bikes')) +
          '. Pro srovnání se podívejte na <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>, <a href="/fatbike-elektrokola/">fatbike elektrokola</a> a <a href="/skladaci-kola/">skládací kola bez motoru</a>.</p>',
    guide='<h2>Co skládací elektrokolo nabízí</h2>'
          '<p>Hlavní předností je kompaktnost: po složení zabere zlomek místa a dá se uložit ve skříni, pod stolem nebo v zavazadlovém prostoru. Motor pomáhá překonat kopce a vítr a nahrazuje tak sílu, kterou by malá kola musela vynaložit. Skládací elektrokolo se hodí pro dojíždění kombinované s vlakem a MHD, pro majitele karavanů a lodí i pro lidi, kteří nechtějí nechat drahé kolo venku.</p>'
          '<p>Nevýhodou je vyšší hmotnost, než jakou má běžné skládací kolo, protože v rámu je navíc baterie a motor. Menší kola se hůř vyrovnávají s dírami a obrubníky a řídí se citlivěji, na což si rychle zvyknete. Skládací kloub je navíc místo, které se časem může uvolnit, proto vyžaduje pravidelnou kontrolu.</p>'
          '<h2>Typy skládacích elektrokol v nabídce</h2>'
          + T(['Typ', 'Charakteristika', 'Pro koho'], [
              ['Městská skládačka 16–20"', 'lehčí rám, menší baterie, kompaktní složení', 'dojíždění, vlak, malý byt'],
              ['Větší skládačka 24–27,5"', 'pohodlnější jízda, větší baterie', 'delší trasy, vyšší lidé'],
              ['Fat bike skládačka', 'široké pneumatiky, často odpružení', 'písek, štěrk, sníh, rekreace'],
              ['Odpružená skládačka', 'tlumiče vpředu i vzadu', 'nerovné cesty a komfort'],
              ['Odlehčená skládačka', 'karbon nebo hliník, pásový pohon', 'minimální váha, pravidelné nošení']]) +
          '<p>Rozdíl mezi nimi je velký. Malá skládačka s 16palcovými koly vás do vlaku vezme jako zavazadlo, ale na štěrku se bude třást. Fat bike model je pohodlný v terénu, ale jeho složená velikost a váha omezují přenášení. Před výběrem si ujasněte, co budete dělat častěji: jezdit, nebo nosit.</p>'
          '<h2>Hmotnost, skládání a rozměry</h2>'
          '<p>U skládacího elektrokola je nejdůležitější údaj hmotnost a velikost po složení. Zeptejte se sami sebe, kolik schodů budete nést a zda zvládnete kolo zvednout jednou rukou. Rychlost skládání se liší: některé modely mají jeden kloub a sklopný sloupek, jiné vyžadují několik kroků. Zkontrolujte pojistky, které drží rám při jízdě, a zda se po složení kolo samo zajistí, aby se nerozevíralo při přenášení. Lehký model s menší baterií se pohodlně nosí, těžší robustní stroj je lepší na místa, kde ho jen vyvezete z garáže.</p>'
          '<h2>Baterie, motor a dojezd</h2>'
          '<p>Baterie určuje, jak daleko dojedete. Udává se v ampérhodinách a voltech, z čehož lze spočítat kapacitu ve watthodinách, a ta je vhodnější pro porovnání. Dojezd závisí na hmotnosti jezdce, terénu, větru, teplotě, stupni asistence a tlaku v pneumatikách. Výrobcem uváděný dojezd je obvykle za ideálních podmínek, ve skutečnosti bývá nižší. Vyjímatelná baterie se dá nabíjet doma v bytě a je praktická, pokud kolo parkuje venku nebo na chodbě.</p>'
          '<p>Motor bývá umístěn v zadním nebo předním kole nebo v středu rámu. Zadní motor je nejběžnější a jednoduchý, středový nabízí lepší vyvážení a lepší výkon do kopce. Sledujte také typ displeje a stupně asistence. Pokud jezdíte po městě, stačí tři nebo pět stupňů.</p>'
          '<h2>Legislativa a provoz</h2>'
          '<p>Elektrokolo, které se v Česku považuje za jízdní kolo, musí mít motor s jmenovitým výkonem do 250 W a podpora se vypíná při 25 km/h. Modely s vyšším výkonem nebo škrtivou pákou bez šlapání se v praxi blíží motorovému vozidlu a vyžadují jiný režim. Dovážené kousky ověřte u prodejce: parametry v popisu se mohou lišit od toho, co smíte provozovat na veřejných komunikacích. Přilba není u dospělých povinná, ale doporučená, vhodné modely najdete mezi <a href="/cyklisticke-helmy/">cyklistickými helmami</a>.</p>'
          '<h2>Brzdy, pláště a bezpečnost</h2>'
          '<p>Kvalita brzd je důležitější než maximální rychlost. Kotoučové brzdy, mechanické nebo hydraulické, dávají lepší zpomalení než čelisťové, zvláště na mokru a při zátěži. Menší kola jsou citlivější na prudké brzdění, proto brzděte plynule. Zkontrolujte pláště: široké mají větší komfort, úzké vyšší rychlost. Světla jsou nutná při provozu za snížené viditelnosti, vyberte z kategorie <a href="/cyklo-svetla/">cyklo světla</a>. Proti krádeži poslouží kvalitní <a href="/cyklo-zamky/">zámek</a>, i když skládací kolo můžete většinou vzít s sebou dovnitř.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejčastěji se setkáte s modely značek ' + B(('engwe', 'Engwe'), ('fafrees', 'Fafrees'), ('samebike', 'Samebike'), ('dyu', 'DYU')) +
          ', které nabízejí široké spektrum od kompaktních po robustnější skládačky s tlustými pneumatikami. Menší zastoupení mají ' + B(('flebi', 'Flebi'), ('jobobike', 'Jobobike'), ('urlife', 'Urlife'), ('onesport', 'Onesport'), ('evercross', 'Evercross'), ('hitway', 'Hitway'), ('spirit', 'Spirit'), ('moma-bikes', 'Moma Bikes')) +
          '. Protože jde převážně o dovážené modely, věnujte pozornost záruce, servisu v Česku a dostupnosti náhradních dílů, hlavně baterie.</p>'
          '<h2>Servis a péče</h2>'
          '<p>Skládací kloub je nejnamáhanější část kola. Před každou jízdou zkontrolujte, zda je pevně zajištěný, a čas od času utáhněte šrouby podle návodu. Baterii nenechávejte dlouho zcela vybitou ani trvale nabitou na maximum, ideální je skladovat ji při středním stavu nabití a v suchu. V zimě ji uchovávejte uvnitř, protože mráz zkracuje dojezd i životnost. Řetěz promazávejte po dešti a po delší jízdě, aby nekorodoval. Elektroniku nemyjte tlakovou vodou, pouze navlhčeným hadříkem.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Kupovat podle dojezdu z reklamy:</strong> reálná hodnota bývá nižší.</li>'
          '<li><strong>Ignorovat hmotnost:</strong> těžké kolo se do vlaku nosí špatně.</li>'
          '<li><strong>Podcenit servis:</strong> u dovážených kousků je klíčová záruka a dostupnost dílů.</li>'
          '<li><strong>Nezkontrolovat legální parametry:</strong> výkon a omezení rychlosti musí odpovídat pravidlům.</li>'
          '<li><strong>Zapomenout na zámek kloubu:</strong> uvolněný kloub je bezpečnostní riziko.</li>'
          '<li><strong>Špatná velikost rámu a sedla:</strong> malé kolo se musí vejít vaší výšce.</li></ul>'
          '<h2>Pro koho se skládací elektrokolo hodí</h2>'
          '<p>Pro dojíždějící, kteří kombinují vlak a poslední kilometry na kole. Pro lidi z paneláků bez sklepa. Pro majitele karavanů a lodí. Pro ty, kdo hledají pohodlí a nechtějí potit v kopcích. Pokud ale plánujete delší túry nebo terén, vhodnější jsou <a href="/horska-elektrokola/">horská elektrokola</a> a <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a>. Pro nakupování a převoz nákladu pomohou <a href="/nakladni-elektrokola/">nákladní elektrokola</a>. Celý přehled najdete v kategorii <a href="/elektrokola/">elektrokola</a>, příslušenství v sekci <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>.</p>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>Sporteka sleduje nabídky českých obchodů a spojuje stejné modely do jedné karty. Při porovnání sledujte kapacitu baterie ve watthodinách, hmotnost, velikost kol a záruku. Pozor na názvy: některé modely se prodávají pod různými značkami a mírně odlišnými parametry. Nesrovnávejte jen cenu, ale i dobu dodání, podmínky záruky a to, zda je součástí nabíječka, blatníky nebo světla.</p>',
    faq=[('Kolik váží skládací elektrokolo?', 'Obvykle desítky kilogramů. Lehčí modely mají menší baterii, robustní fat bike modely jsou těžší.'),
         ('Jaká kola mají skládací elektrokola?', 'Nejčastěji 16 až 20 palců, větší modely 24 až 27,5 palce. Menší kola jsou obratná, ale citlivější na nerovnosti.'),
         ('Vezmou skládací elektrokolo do vlaku?', 'Po složení se často přepravuje jako zavazadlo, ale podmínky se liší podle dopravce. Ověřte je předem.'),
         ('Jak daleko dojedu na jedno nabití?', 'Záleží na baterii, terénu, hmotnosti jezdce a stupni asistence. Údaj výrobce je za ideálních podmínek.'),
         ('Jaký výkon motoru je legální?', 'Pro kolo bez registrace platí jmenovitý výkon do 250 W a podpora do 25 km/h. Dovážené modely vždy ověřte.'),
         ('Musím mít helmu?', 'Dospělí ji mít nemusí, ale je doporučena. Děti do 18 let ji musejí nosit.'),
         ('Jak často kontrolovat skládací kloub?', 'Před každou jízdou. Uvolněný kloub je riziko pádu, proto jej pravidelně dotahujte.'),
         ('Jak skladovat baterii přes zimu?', 'V suchu a v teple, ideálně při středním stavu nabití. Plně vybitá ani plně nabitá baterie dlouhé uložení nesnáší.'),
         ('Hodí se skládací elektrokolo do terénu?', 'Jen robustnější modely s širšími pneumatikami nebo odpružením. Kompaktní městské skládačky jsou určeny na asfalt.'),
         ('Na co dát pozor u dovážených modelů?', 'Na záruku, servis v Česku a dostupnost náhradních dílů, hlavně baterie. Ověřte také, zda jsou parametry v souladu s předpisy.')],
)

# ------------------------------------------------------------------ extra sections (appended to the guides above)
NEW['lyzarske-cepice-a-nakrcniky']['guide'] += (
    '<h2>Teplota, vítr a nadmořská výška</h2>'
    '<p>Pocit chladu na hlavě nezávisí jen na teploměru. Při jízdě rychlostí desítek kilometrů v hodině se k mrazu přidává náporový vítr a stejná teplota na vleku a ve sjezdu se výrazně liší. Na ledovci nebo v hřebenových partiích je navíc více slunce i větru, takže se vyplatí vrstva, kterou lze rychle upravit. Za bezvětří a jarního slunce stačí čelenka, při mlze a mrazu si oblečete tenkou čepici, nákrčník a případně kuklu. Proto je lepší koupit dva menší kusy než jeden těžký.</p>'
    '<h2>Nákrčník a kukla do detailu</h2>'
    '<p>Nákrčník bývá z elastické pleteniny, fleecu nebo jejich kombinace. Fleecový tubus je teplejší, ale při vlhkosti z dechu ztvrdne a nepříjemně studí, proto ho při intenzivní jízdě střídejte s lehčím. Pletený tubus z merina nebo syntetiky dýchá lépe a lze ho nosit i přes nos. Některé kousky mají na krku volnější část s lemem, který se dá stáhnout. Kukla pod helmu má obvykle tenčí látku v oblasti hlavy a silnější v oblasti krku. Klade se důraz na švy, které se nesmí otírat o bradu. U kukel přes helmu platí, že musejí být dost velké, aby se nasadily přes skořepinu.</p>'
    '<h2>Dospělí, mladí a senioři</h2>'
    '<p>Starší lidé a děti mají citlivější reakci na chlad a pomaleji se zahřívají, proto jim doporučujeme teplejší pokrývku hlavy a nákrčník navíc. Mladí sportovci jezdící rychle ocení lehké kousky, které odvádějí pot. Pokud nosíte brýle, vybírejte tenčí lem a bez silných švů v oblasti spánků. Lidé s dlouhými vlasy zjistí, že čepice pod helmou se nejlépe nosí s volně spleteným copem, který netlačí na týl.</p>'
    '<h2>Reflexní prvky a viditelnost</h2>'
    '<p>Na svahu sice platí jiná pravidla než na silnici, ale výrazná barva čepice nebo nákrčníku pomáhá ostatním lyžařům vás zpozorovat, zvlášť při špatné viditelnosti. Děti proto doporučujeme vybavit svítivými barvami. Při běžeckém lyžování po setmění se hodí reflexní proužky a čelovka, kterou lze nasadit přes tenkou čepici nebo čelenku bez tlaku na hlavu.</p>'
    '<h2>Dárek a sezónní nákup</h2>'
    '<p>Čepice a nákrčníky jsou oblíbeným dárkem, protože velikost bývá univerzální a chyba ve výběru je menší než u obuvi, přesto ale zkontrolujte obvod hlavy podle tabulky výrobce. Přesto zkontrolujte barvu, vzor a materiál podle toho, jak dárek použije. Nákup začíná na podzim, ale nejlepší dostupnost mívají kousky na začátku sezóny, zatímco v únoru a březnu už některé velikosti nebo barvy chybějí. Na Sportece si můžete porovnat, ve kterém obchodě je kus skladem.</p>')

NEW['tanecni-obleceni']['guide'] += (
    '<h2>Oblečení podle věku</h2>'
    '<p>Nejmenší děti v přípravných kroužcích potřebují především pohodlí: trikot nebo šaty, které se snadno oblékají i svlékají a mají jednoduché zapínání, a obuv, kterou zvládnou samy. Žákyně v prvních ročnících baletu už nosí uniformní trikot a sukýnku podle požadavků školy. Teenageři často přecházejí na legíny a krátký top, protože se zajímají o moderní tanec. Dospělé tanečnice sladí oblečení s hodinou: pro balet přiléhavý trikot, pro latinu volnější kousky.</p>'
    '<h2>Společenský tanec a latina</h2>'
    '<p>Pro společenský tanec existují jiné kousky než pro balet. Sukně do tanečních mají plnější střih a volný pas, aby se při otáčení neomotávaly. Pánská taneční výbava je prostá: kalhoty s dostatečným rozkrokem, košile a obuv s hladkou podrážkou. Pro trénink stačí pohodlné sportovní oblečení, na turnaje se kupuje speciální výbava. K oblečení patří <a href="/tanecni-obuv/">taneční obuv</a>, kterou vybíráme podle typu tance a povrchu parketu.</p>'
    '<h2>Vystoupení a závěrečné hodiny</h2>'
    '<p>Pro vystoupení si často kupujeme kostýmy, které se liší od tréninkového oblečení. Škola obvykle sama sdělí požadavky na barvu a střih. Nekupujte nic předem a počítejte s tím, že dítě do vystoupení povyroste. Před vystoupením vyzkoušejte, zda kostým nedrhne, ramínka se nezahrnují a lze v něm provést všechny pohyby. Čistý a vyžehlený trikot působí lépe než zdobený a pomačkaný.</p>'
    '<h2>Doplňky k tanečnímu oblečení</h2>'
    '<p>K oblečení patří punčocháče, ohřívače nohou, spony a gumičky do vlasů, taška na tréninkové věci a lahev na pití. Punčocháče by měly být pružné a bez švu, ohřívače nohou pomáhají udržet teplé svaly v chladných sálech. Vlasy se spínají do drdolu, který nepřekáží ve výskoku. Do tašky patří náhradní tričko a ručník. Pomůcky na cvičení doma najdete v sekci <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>'
    '<h2>Kdy oblečení vyměnit</h2>'
    '<p>Taneční oblečení se opotřebuje rychleji než běžné: elastan ztrácí pružnost, látka se vytahuje a vybledá. Vyměňte kus, když začne tvořit záhyby, propouštět světlo nebo když dítě přeroste velikost a pohyb je omezený. Starší kousky můžete nosit doma na cvičení nebo předat mladší sestře či kamarádce. Tím také šetříte rodinný rozpočet a snižujete odpad.</p>')

NEW['rodinne-stany']['guide'] += (
    '<h2>Kam stan postavit a jak ho zajistit</h2>'
    '<p>Dobře zvolené místo ušetří spoustu problémů. Hledejte rovný, mírně zvýšený pozemek, kde se po dešti nebude držet voda, a odstraňte kameny a šišky. Velký stan stavte dveřmi po větru, aby se nemohl zachytit. Tunelový stan je nejstabilnější, když je užší čelo namířeno proti větru. Všechna lana je nutné napnout a ukotvit, protože každý uvolněný bod snižuje stabilitu. Pod podlážku se hodí ochranná podložka, která zabrání prodření od kamínků a zvýší tepelnou izolaci od země. Nestavte stan pod osamělými stromy a na okraji lesa, kde hrozí odlomené větve.</p>'
    '<h2>Počasí a bouřky</h2>'
    '<p>Velký stan má velkou plochu, kterou vítr využije, proto při silném větru raději sundejte předsíň a napněte a zkontrolujte všechna lana. Při dešti se ujistěte, že voda stéká po vnějším plášti a nedotýká se vnitřního stanu, jinak začne prosakovat. Za horka stan otevřete na obou stranách a vyberte stinné místo, protože na slunci se uvnitř rychle zvyšuje teplota. Stan před bleskem nechrání a kovové tyče ochranou nejsou. Při bouřce se nezdržujte pod stromy ani v otevřeném terénu a pokud je to možné, přesuňte se do auta nebo pevné budovy.</p>'
    '<h2>Rodinný stan a děti</h2>'
    '<p>Pro děti je stan dobrodružství, ale i riziko. Zipy a síťky musí být odolné a dobře dostupné, aby je zvládly samy. Provazy kolem stanu označte jasnou barvou, aby se o ně nezakopli. Uvnitř držte věci uspořádané, aby se na tmavé ložnici nic nešlapalo. Pokud vaříte, dělejte to mimo stan, v předsíni jen se zvláštní opatrností a s dostatečným větráním, protože hrozí požár a otrava plynem. Stan s tmavou ložnicí a odděleným prostorem pomáhá dětem spát a rodičům mít večer klid.</p>'
    '<h2>Zimní a celoroční použití</h2>'
    '<p>Většina rodinných stanů je určena pro léto a přechodná období. Pro silný mráz nebo sníh nejsou stavěny, protože neunesou zatížení sněhem ani nenabídnou izolaci. Při chladných nocích pomůže silnější izolační podložka, dobrý spací pytel a těsné zavření všech otvorů. Pokud plánujete zimní pobyt, hledejte stany, které výrobce označuje jako čtyřsezónní, nebo zvažte jiné ubytování. Obecný přehled variant najdete v kategorii <a href="/stany/">stany</a> a v kategorii <a href="/expedicni-stany/">expediční stany</a>.</p>'
    '<h2>Údržba před sezónou a po ní</h2>'
    '<p>Před cestou stan postavte na zahradě, zkontrolujte počet kolíků, délku lan a funkčnost zipů. Zjistěte, zda nechybí tyč a zda se nepoškodily spoje. Po návratu stan vyčistěte od písku a rostlinných zbytků, nechte důkladně vyschnout a skladujte volně nebo v prodyšném pytli. Opravná sada s lepicí páskou a náhradním spojem tyčí patří do každé výbavy. Včasná oprava malé trhliny je levnější než koupě nového stanu.</p>')

NEW['skladaci-elektrokola']['guide'] += (
    '<h2>Velikost uživatele a nastavení</h2>'
    '<p>Malá skládací kola mají obvykle jednu velikost rámu a přizpůsobují se pomocí výškově nastavitelného sedla a sloupku řídítek. Vyšší lidé musí zkontrolovat maximální výšku sloupku a maximální nosnost, protože výrobce určuje hmotnostní limit pro jezdce i zavazadla. Při nastavování sedla byste měli dosáhnout na zem špičkami a při šlapání mít koleno mírně pokrčené. Špatně nastavené sedlo způsobuje bolest kolen a zad. Pokud kolo používá více lidí, jsou užitečné rychloupínáky, které se dají přenastavit bez nářadí.</p>'
    '<h2>Převoz v autě, vlaku a MHD</h2>'
    '<p>V autě kolo zabere zavazadlový prostor a těžší modely je nutné vyzvednout do kufru dvěma lidmi. Chraňte lak a kabely před poškozením, například přikrývkou. Ve vlaku a v MHD se podmínky přepravy liší, ověřte je předem. Obecně platí, že skládací kolo, které se složí do pytle, bývá přijímáno snáze než kolo na kolečkách. Před nástupem vypněte motor a displej, abyste zabránili nechtěnému rozjezdu. Baterii vyjměte, pokud je to vyžadováno, a vezměte s sebou.</p>'
    '<h2>Nabíjení doma a v práci</h2>'
    '<p>Baterie se nabíjí běžnou domácí zásuvkou, doba nabíjení trvá několik hodin. Používejte originální nabíječku a nenabíjejte bez dozoru na hořlavém povrchu. Pokud kolo ukládáte v kanceláři, ověřte u zaměstnavatele pravidla nabíjení. Nenechávejte baterii nabíjet přes noc na chodbě bez ochrany, nabíjejte při pokojové teplotě a nevystavujte ji přímému slunci. Dlouhá životnost závisí na šetrném zacházení, takže nepoužívejte nabíječku z jiného zařízení.</p>'
    '<h2>Doplňky a příslušenství</h2>'
    '<p>Skládací elektrokolo potřebuje stejné příslušenství jako běžné kolo: světla, zvonek, blatníky a případně nosič. Pozor na kompatibilitu nosičů s malými koly a sklopným rámem. Úložné prostory pomohou <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>, pro nošení kola po schodech se hodí přenosná taška nebo pouzdro. Kapsa na zadní straně sedla nebo malá brašna na rám pojme nářadí a klíče. Pokud vozíte děti, ověřte, zda rám a nosič přepravu dětí vůbec dovolují.</p>'
    '<h2>Skládací kolo bez motoru, nebo s ním</h2>'
    '<p>Klasické <a href="/skladaci-kola/">skládací kolo bez motoru</a> je lehčí, jednodušší a levnější na servis, ale kopce a vítr vyžadují sílu. Elektrokolo je těžší, drží si ale tempo a zvládne delší vzdálenosti v běžném oblečení. Pokud vás čeká jen pár stovek metrů do vlaku, může stačit kolo bez motoru. Při dojíždění několika kilometrů a při kopcovité trase se motor vyplatí. Pro větší pohodlí a jiný styl jízdy se podívejte také na <a href="/damska-elektrokola/">dámská elektrokola</a>.</p>')

NEW['tanecni-obleceni']['guide'] += (
    '<h2>Hygiena a výměna v průběhu týdne</h2>'
    '<p>Kdo tančí několikrát týdně, potřebuje alespoň dva trikoty nebo sady, aby jedna mohla schnout, zatímco druhá je v používání. Pot se v elastických vláknech drží a zápach se zhoršuje, pokud oblečení zůstane v tašce přes noc. Po hodině ho proto vyndejte a vyvěste. Dětem pomáhá pevná rutina: vyndat věci z tašky, připravit čisté na příště a zkontrolovat, zda nic nechybí. Takový režim ušetří stres před hodinou.</p>')
NEW['rodinne-stany']['guide'] += (
    '<h2>Ekologie a rozumný nákup</h2>'
    '<p>Dobrý stan vydrží mnoho sezón, pokud o něj pečujete, takže je lepší vybrat pevnější konstrukci než nejlevnější variantu, kterou po jednom roce vyhodíte. Poškozenou plachtu lze opravit záplatou, ulomenou tyč nahradit náhradním dílem. Na kempu uklízejte po sobě a nepoužívejte kolíky tam, kde je to zakázáno. Při koupi ověřte, zda prodejce nabízí náhradní díly a servis, protože ty prodlouží životnost stanu a ušetří vám nový nákup.</p>')
NEW['skladaci-elektrokola']['guide'] += (
    '<h2>Zkušební jízda a první týdny</h2>'
    '<p>Pokud je to možné, vyzkoušejte skládací elektrokolo před koupí, zejména skládání, nošení a chování malých kol při rozjezdu. První dny jezděte opatrněji, protože motor reaguje jinak než nohy a malá kola jsou citlivější na řízení. Zkontrolujte všechny šrouby a tlak v pneumatikách a po prvních kilometrech znovu dotáhněte kloub. Zapamatujte si postup skládání, aby se z něj stala rutina.</p>')
