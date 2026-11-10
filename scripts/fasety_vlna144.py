"""sporteka.cz — facet landing texts wave 144: detske-dresy, navijaky-fox, sportovni-obleceni-panske, cyklisticke-dresy-damske.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detske-dresy
NEW['detske-dresy'] = dict(
    title='Dětské dresy: velikosti, střihy a výběr podle sportu',
    desc='Dětské dresy na fotbal, hokej, basketbal i kolo. Jak vybrat velikost podle výšky dítěte, rozlišit repliku od tréninkového dresu a ušetřit při růstu.',
    intro='<p>Dětský dres má dvě nesplnitelná zadání najednou: musí sedět dnes a vydržet i při růstu o několik centimetrů za sezónu. Rodiče proto často sahají po větší velikosti, jenže příliš dlouhý dres se při běhu motá a u cyklistických modelů dokonce zavazí. Na této stránce jsou dresy určené dětem a mládeži ze sortimentu kategorie <a href="/dresy/">dresy</a>: fotbalové, hokejové, basketbalové, cyklistické i fanouškovské repliky klubů a reprezentací. Průvodce vysvětluje, jak se dětské velikosti značí podle výšky, čím se liší replika od tréninkového kusu, jak zadat objednávku pro celý tým a co udělat, aby dres přežil pračku i sourozence. Ceny a dostupnost velikostí u obchodů uvidíte vedle sebe u každého kusu.</p>',
    guide='<h2>Dětská velikost se počítá na výšku, ne na věk</h2>'
          '<p>Nejčastější chyba při koupi dresu pro dítě je řídit se číslem věku. Dvě desetileté děti se od sebe snadno liší o deset centimetrů a výrobci mezi sebou počítají velikosti jinak. Spolehlivější je změřit výšku dítěte bez bot, u zdi, a porovnat ji s tabulkou u konkrétního kusu. Většina evropských značek uvádí dětské velikosti právě v centimetrech výšky, často po dvanácti centimetrech, takže dítě na hranici se obvykle vejde do větší velikosti.</p>'
          + T(['Výška dítěte', 'Orientační označení', 'Poznámka k výběru'], [
              ['kolem 110–116 cm', '110–116, 4–6 let', 'nejmenší velikosti, dres sahá hluboko přes pas'],
              ['kolem 122–128 cm', '122–128, 7–8 let', 'první školní věk, často už se řeší číslování týmu'],
              ['kolem 134–140 cm', '134–140, 9–10 let', 'období rychlého růstu, ověřte délku rukávu'],
              ['kolem 146–152 cm', '146–152, 11–12 let', 'u fotbalu a hokeje přechod na střih blízký dospělým'],
              ['kolem 158–164 cm', '158–164, 13–14 let', 'někdy lépe padne nejmenší dospělá velikost S']]) +
          '<p>Tabulka je jen orientace, protože každá značka kreslí střih po svém. Adidas a Puma uvádějí dětské řady většinou podle výšky, Nike používá označení Junior nebo Youth s písmeny, u amerických replik se objevuje výraz mládežnická velikost. Mezi velikostmi se vyplatí rozhodnout podle ramen: dres, který visí z ramen téměř k loktům, je příliš velký, i když délkou vypadá dobře. Rukáv by měl končit v polovině nadloktí a dolní lem sahat přes opasek kalhot, ale ne ke stehnům.</p>'
          '<h2>Replika, tréninkový dres, nebo zápasová verze</h2>'
          '<p>Pro děti se prodávají hlavně tři druhy dresů a každý má jiný účel. Replika je určena fanouškům a pro běžné nošení. Tréninkový dres je určen k pohybu a časté péči. Zápasový dres s přiléhavým střihem je pro děti zřídka potřebný, protože dětská těla rostou a technologie závodního střihu se nepromítnou.</p>'
          '<ul><li><strong>Replika klubu nebo reprezentace:</strong> kopíruje vzhled hráčského dresu, ale střih je volnější a materiál odolnější. Hodí se na tribunu, do školy i na hřiště. Znak bývá nažehlený nebo vyšitý, proto dresy obracejte na ruby a perte na nízkou teplotu.</li>'
          '<li><strong>Tréninkový dres:</strong> jednodušší, bez drahých znaků a sponzorských nášivek, z lehkého úpletu, který rychle schne. Právě tyto kusy vybírají oddíly pro celé týmy, například řady jako Tiro, Entrada nebo Squadra u Adidasu a Parku u Nike.</li>'
          '<li><strong>Brankářský dres:</strong> má zesílené rukávy, někdy lokty s vycpávkou. Dítě v bráně ocení delší rukávy a možnost vzít si pod něj tričko.</li>'
          '<li><strong>Dlouhý rukáv:</strong> vyplatí se na podzimní a jarní tréninky venku, v zimě ho děti nosí pod bundou jako spodní vrstvu.</li></ul>'
          '<p>U fotbalu se obvykle vyplatí začít jedním tréninkovým dresem na každodenní používání a repliku pořídit jako dárek či na zápas oblíbeného týmu. Hodí se k ní <a href="/kopacky/">kopačky</a> a <a href="/fotbalove-chranice-a-stulpny/">chrániče se štulpnami</a>, k lehčímu tréninku <a href="/sportovni-kratasy/">sportovní kraťasy</a>.</p>'
          '<h2>Fotbalové dresy pro děti a mládež</h2>'
          '<p>Nejvíc dětských dresů se prodává pro <a href="/fotbal/">fotbal</a>. Značky Adidas, Nike, Puma a Joma mají samostatné dětské řady s označením Junior, JR nebo Y, a to jak pro kluby, tak pro školní a oddílové týmy. Italská značka Errea a španělská Joma se specializují na týmové vybavení a dětské střihy v nich často znamenají vyrovnané barevné řady pro více hráčů. U Kipsta, značky obchodního řetězce Decathlon, najdete jednoduché a odolné kusy pro začátečníky.</p>'
          '<p>Při výběru fotbalového dresu pro dítě sledujte tři věci. První je materiál: lehký polyesterový úplet s drobnými otvory odvádí pot a nelepí se. Druhý je okraj krku, který nesmí škrábat. Třetí je vzorování, protože výrazné proužky a sponzorská loga u dětí ztrácejí barvu rychleji než jednobarevný dres, zejména při praní se zipy a suchými zipy v jedné várce.</p>'
          '<p>Rodiče, kteří dres pořizují pro týmovou objednávku, by měli předem zjistit, jestli oddíl potřebuje stejnou sérii. Dresy téže řady se v různých sezónách mírně liší odstínem a vzorem, proto je vhodné objednat všechny kusy najednou, nejlépe od jednoho prodejce, a o jednu velikost nahoru pro dvě nejmenší děti, které ještě porostou.</p>'
          '<h2>Replika klubu nebo reprezentace pro malé fanoušky</h2>'
          '<p>Dětské repliky mají oproti dospělým jednodušší znak a pružnější materiál. Dres reprezentace nebo klubu se obvykle kupuje s rezervou, protože ho dítě chce nosit celou sezónu. Dostupné jsou často tři varianty: domácí, venkovní a třetí. Domácí je klasická volba, venkovní bývá v kontrastní barvě a třetí je módnější kousek. Pokud sháníte repliku konkrétního klubu, prohlédněte si landingy <a href="/nike-dresy/">Nike dresy</a> a <a href="/real-madrid-dresy/">Real Madrid dresy</a>, kde jsou dětské kusy také zastoupené.</p>'
          '<p>Jméno a číslo hráče na zádech se tiskne podle aktuální sezóny. Po odchodu hráče z klubu nebo změně sestavy ztrácí potisk pro dítě význam, takže se někdy vyplatí neutrální dres bez jména. Naopak sběratelsky zajímavý kus se samolepkou z minulé sezóny si děti schovávají. U potištěných dresů vždy ověřte, zda je číslo součástí nabídky, nebo se platí zvlášť.</p>'
          '<h2>Hokejové, basketbalové a americké dresy</h2>'
          '<p>Dětský hokejový dres je delší a volnější než fotbalový, aby se nedostal z kalhot a neomezoval pohyb ramen v chráničích. Tréninkové kusy výrobců hokejového vybavení, mezi které patří například Bauer, mají zpevněné lokty a hrubší úplet. Fanouškovské hokejové dresy jsou lehčí a jejich střih je pohodlnější na denní nošení, ale na led se tolik nehodí. Víc najdete v kategorii <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>.</p>'
          '<p>Značka Outerstuff dodává mládežnické repliky dresů amerických lig, zejména basketbalu a amerického fotbalu. Střih je volný a materiál pevnější než u tréninkových kusů. Basketbalový dres bez rukávů dítě nosí buď samostatně v létě, nebo přes tričko, což je ideální na hřiště i do školy. Pokud dítě začíná s basketbalem, podívejte se i na <a href="/basketbal/">kategorii basketbal</a> a vyberte kraťasy po kolena, které se k dresu nosí.</p>'
          '<h2>Cyklistické dresy pro děti</h2>'
          '<p>Dětské cyklistické dresy mají na zádech kapsy a zip na hrudi stejně jako dospělé, jen v menším provedení. Značky Force a Silvini nabízejí dětské MTB a enduro dresy, které jsou volnější a mají delší rukáv, aby chránily před prachem a sluncem. Dítě na kole se hýbe víc než dospělý, proto kupujte dres pružný a bez švů v místech, kde se tře o popruhy batohu. Tmavé barvy se na silnici hůř vidí, proto při jízdě v provozu zvolte výraznou fluorescenční nebo světlou variantu a přidejte <a href="/detske-cyklohelmy/">dětskou cyklohelmu</a>. Pro starší děti jsou vhodné i rozsáhlejší nabídky <a href="/cyklisticke-dresy/">cyklistických dresů</a>.</p>'
          '<h2>Jak koupit dětský dres na růst a nezbytně nepřeplatit</h2>'
          '<ul><li><strong>Měřte výšku, ne věk.</strong> Dítě měřte bez bot a porovnejte s tabulkou u konkrétního kusu.</li>'
          '<li><strong>Vyberte o jednu velikost větší jen u volného střihu.</strong> U přiléhavého a pružného střihu to nepomáhá.</li>'
          '<li><strong>Dres s dlouhým rukávem kupujte s ohledem na délku paží.</strong> Zbytečně dlouhý rukáv překáží v držení hole nebo brankářských rukavic.</li>'
          '<li><strong>Nechte si čas na výměnu.</strong> Dítě by dres mělo doma vyzkoušet v pohybu, ne jen na stání.</li>'
          '<li><strong>Zkontrolujte rok sezóny.</strong> Repliky starších sezón bývají k dispozici déle za zvýhodněnou cenu.</li></ul>'
          '<h2>Péče o dětský dres</h2>'
          '<p>Dětské dresy se perou častěji a rychleji, proto se vyplatí držet pár pravidel. Dres otočte na ruby, aby se chránily potisky a znak, perte na nízkou teplotu a bez aviváže, která zalepuje póry funkčního materiálu. Znak a čísla se nesmějí žehlit přímo. Sušte volně rozložený na vzduchu a ne na topení, protože tepelně zpracované potisky se deformují. Skvrny od trávy a bláta nejdříve namočte, teprve potom perte, a nepoužívejte bělidla, která vyblednou barvy týmu. Zpocený dres nenechávejte ve sportovní tašce přes noc, ztrácí svěžest a pach se do materiálu zažere. Po sezóně dres dobře vyperte, usušte a uložte jako vzpomínku, případně jej předejte mladšímu sourozenci nebo kamarádovi.</p>'
          '<h2>Související výběry</h2>'
          '<p>Chcete-li dítěti složit kompletní výbavu, pokračujte v kategorii <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/teplaky/">tepláky</a> a <a href="/sportovni-obleceni/">sportovní oblečení</a>. Pestrý výběr dětských značek najdete u <a href="/znacka/adidas/">Adidasu</a>, <a href="/znacka/puma/">Pumy</a>, <a href="/znacka/nike/">Nike</a> a <a href="/znacka/errea/">Errey</a>. Pokud hledáte spíše repliku amerických lig, podívejte se na <a href="/znacka/outerstuff/">Outerstuff</a>.</p>',
    faq=[
        ('Jak vybrat velikost dětského dresu?', 'Změřte dítěti výšku bez bot a porovnejte ji s tabulkou u konkrétního dresu. Věk je jen orientační údaj, protože výrobci značí velikosti různě. Pokud je dítě mezi dvěma velikostmi, vezměte u volného střihu větší, u přiléhavého spíš menší.'),
        ('Je lepší koupit dres o číslo větší?', 'U volného fotbalového nebo basketbalového dresu ano, o jednu velikost, protože vydrží celou sezónu. Příliš velký dres se ale při běhu motá, zvedá se nad pás a omezuje pohyb. U přiléhavého cyklistického a hokejového dresu větší velikost nedoporučujeme.'),
        ('Čím se liší dětská replika od tréninkového dresu?', 'Replika kopíruje vzhled klubu nebo reprezentace s oficiálním znakem a hodí se na tribunu a běžné nošení. Tréninkový dres je jednodušší, lehčí a levnější na obnovu, a proto se hodí pro oddíl a časté praní.'),
        ('Jak se starat o dres, aby vydržel?', 'Perte ho naruby na nízké teplotě, bez aviváže a bělidel, a suste na vzduchu. Potisk a znak nežehlete přímo. Skvrny od trávy předem namočte a teprve potom perte.'),
        ('Kde mohu koupit dres pro celý tým najednou?', 'Nejjistější je vybrat stejnou řadu a dresy objednat v jedné dávce od jednoho obchodu, aby se nelišil odstín. Na stránce vidíte u jednotlivých kusů obchody a velikosti skladem, takže poznáte, kde mají kompletní sadu.'),
        ('Mohu dítěti koupit dospělou velikost S?', 'U starších dětí kolem 160 cm často ano. Dospělé střihy mají delší rukávy a širší ramena, takže vždy porovnejte hrudník a délku s tabulkou. Pro menší děti se dospělý dres nehodí.'),
        ('Lze na dětské dresy pořídit číslo a jméno?', 'Některé repliky se prodávají již s potiskem hráče, jiné bez něj. U týmových dresů si potisk obvykle objednává oddíl zvlášť. Před koupí v popisu zkontrolujte, zda je potisk součástí nabídky.'),
        ('Který dres je vhodný na kolo?', 'Na kolo se hodí cyklistický dres s kapsami na zádech a zipem na hrudi, například dětské modely Force nebo Silvini. Fotbalový dres je pro delší jízdu méně praktický, protože nemá kapsy a při předklonu se zvedá nad pás.'),
        ('Proč se dětské dresy liší podle značek?', 'Každý výrobce používá vlastní střih a velikostní tabulku. Adidas a Puma uvádějí velikosti podle výšky, Nike a americké repliky podle označení Youth nebo Junior. Proto si před koupí vždy ověřte údaje u konkrétního kusu.'),
        ('Kdy se dětské dresy zlevňují?', 'Nejčastěji na konci sezóny nebo při obměně kolekce klubu, kdy vychází nová domácí a venkovní varianta. Starší repliky bývají dostupné za nižší cenu, velikosti však rychle mizí, proto se vyplatí sledovat nabídku obchodů vedle sebe.'),
    ],
)

# ------------------------------------------------------------------ navijaky-fox
NEW['navijaky-fox'] = dict(
    title='Navijáky Fox: kaprařské navijáky EOS a jak vybrat',
    desc='Navijáky Fox pro kapraře: řada EOS ve velikostech 8000 až 14000, rozdíl F a FD, kapacita cívky, volnoběh a pouzdro na naviják. Porovnání obchodů.',
    intro='<p>Fox patří k nejznámějším jménům kaprařského rybolovu a jeho navijáky míří na dlouhé sezení u vody, daleké náhozy a zdolávání větších ryb. V nabídce srovnávače jde hlavně o řadu EOS ve velkých velikostech, doplněnou o další modely a praktické pouzdro na naviják. Tato stránka vybírá z kategorie <a href="/rybarske-navijaky/">navijáky</a> jen kusy značky Fox a vysvětluje, co znamenají velké čtyřmístné velikosti, kdy se hodí označení F a FD, proč u kaprařiny rozhoduje kapacita cívky a jak naviják spárovat s prutem a vlascem. Najdete tu i srovnání s jinými značkami, tipy na péči a rady, na co se zeptat prodejce dřív, než zadáte objednávku, aby naviják sloužil mnoho sezón.</p>',
    guide='<h2>Fox v kaprařském rybolovu</h2>'
          '<p>Značka Fox vznikla jako dodavatel vybavení pro lov kaprů a dodnes se zaměřuje hlavně na tuto disciplínu. Jejím sortimentem jsou pruty, navijáky, bivaky, lehátka, tašky i drobné doplňky, takže řada kaprařů vybavuje u jedné značky celý břeh. Navijáky Fox proto nejsou univerzální přívlačové modely na okouna, ale robustní kusy pro dlouhé náhozy, těžké olovo a delší zdolávání ryby. Pokud jde o jemný rybolov na malou rybu, vybírejte radši menší modely z <a href="/navijaky-shimano/">navijáků Shimano</a> nebo <a href="/navijaky-daiwa/">navijáků Daiwa</a>.</p>'
          '<h2>Co znamenají velikosti 8000 až 14000</h2>'
          '<p>U navijáků s pevnou cívkou se velikost označuje číselnou řadou. Čtyřmístná čísla v řádu tisíců, jako jsou 8000, 10000, 12000 nebo 14000, patří velkým modelům stavěným na dlouhou šňůru a těžší zátěž. Čím vyšší číslo, tím větší cívka, vyšší hmotnost a větší kapacita vlasce. Přesné údaje o kapacitě se u každé řady liší, proto je vždy hledejte v popisu konkrétního kusu, kde výrobce uvádí délku vlasce při daném průměru.</p>'
          + T(['Velikost', 'Obvyklé určení', 'Na co si dát pozor'], [
              ['8000', 'běžný kaprový rybolov na středně velkých vodách', 'nižší kapacita než největší modely, ale lehčí v ruce'],
              ['10000', 'univerzální volba na rybníky, jezera a řeky', 'dobrá rovnováha mezi kapacitou a hmotností'],
              ['12000', 'dlouhé náhozy na velkých vodách', 'těžší prut a cívka musí odpovídat'],
              ['14000', 'extrémně daleké náhozy, velké ryby, spodování', 'největší hmotnost, souprava se může překlápět dopředu']]) +
          '<p>Praktické pravidlo zní, že větší cívka navíjí na jedno otočení více vlasce, ale vyžaduje silnější prut. Pokud lovíte na menších vodách do sto metrů, největší velikost nepotřebujete a zbytečně přidáte hmotnost na prut. Pro velké nádrže a dlouhé vzdálenosti je naopak velká cívka přínosem, protože při náhozu vlasec odtéká s menším odporem.</p>'
          '<h2>Označení F a FD</h2>'
          '<p>V názvech navijáků značky Fox se objevují zkratky F a FD. FD obvykle znamená přední brzdu, v angličtině front drag, kde se brzda nastavuje na přední straně cívky. Nastavení je jednodušší dostupné i za chodu, brzdný mechanismus bývá větší a plynulejší. Označení F se používá u modelů s volnoběhem nebo jiným provedením brzdy, přesný význam si ověřte v popisu u konkrétního výrobku. Pokud nevíte, kterou variantu zvolit, začněte u popisu na stránce obchodu a ptejte se prodejce, protože u kaprařských navijáků se výbava liší od kusu ke kusu.</p>'
          '<h2>Brzda, volnoběh a kapacita cívky</h2>'
          '<p>Tři vlastnosti rozhodují u kaprařského navijáku víc než cokoli jiného. Prvním je brzda: při záběru kapra nesmí cukat, musí pracovat plynule a dlouho, aby nepřehřála cívku. Nastavujte ji tak, aby ryba odtáhla vlasec, ale prut se jen mírně ohnul. Druhým je volnoběh neboli baitrunner, který uvolní vlasec bez brzdy a nechává rybu odplout bez odporu. Díky němu prut nespadne z podložek. Třetím je kapacita cívky: pro daleké náhozy přes sto metrů se hodí cívka s hlubokým nábojem pro silnější vlasec.</p>'
          '<ul><li><strong>Brzda:</strong> plynulý rozjezd bez zaseknutí, snadná úprava jednou rukou.</li>'
          '<li><strong>Volnoběh:</strong> spolehlivé zapnutí a vypnutí, pojistka proti samovolnému rozjetí.</li>'
          '<li><strong>Cívka:</strong> hladký okraj, aby se vlasec při náhozu nezasekl.</li>'
          '<li><strong>Převod:</strong> střední převod je univerzální, rychlejší šetří čas při navíjení z velké dálky.</li>'
          '<li><strong>Rukojeť a kliky:</strong> pevná, bez vůle, vhodná na dlouhé sezení.</li></ul>'
          '<h2>Jak naviják spárovat s prutem a vlascem</h2>'
          '<p>Velký naviják vyžaduje prut stejné váhové třídy. Kaprařský prut s testovací křivkou kolem tří liber se obvykle páruje s navijákem velikosti 8000 až 10000, těžší prut a daleké náhozy zvládne model 12000 a větší. Souprava má ležet v ruce téměř vodorovně a nemá se překlápět; pokud se naviják zdá příliš těžký, vyberte menší velikost nebo prut s lepším vyvážením. Podívejte se na naši kategorii <a href="/rybarske-pruty/">rybářské pruty</a>, kde najdete pruty pro různé délky a zatížení.</p>'
          '<p>Vlasec volte podle přístupu. Monofilní vlasec má natažení, které tlumí záběry, a odpouští chyby při zdolávání. Pletená šňůra přenáší záběr přesněji, ale potřebuje prut s jemnějšími vodítky a dobře nastavenou brzdu. V obou případech hledejte v obchodě <a href="/vlasce-a-snury/">vlasce a šňůry</a> s odpovídajícím průměrem pro cívku, kterou jste si zvolili.</p>'
          '<h2>Fox ve srovnání s jinými značkami</h2>'
          + T(['Značka', 'Zaměření', 'Pro koho'], [
              ['Fox', 'kaprařský rybolov, velké cívky, sada doplňků', 'kaprař, který vybavuje celé stanoviště'],
              ['Shimano', 'široká nabídka od přívlače po moře', 'univerzální rybář i specialista na jemný rybolov'],
              ['Daiwa', 'přívlač, feeder, moře, speciální řady', 'pro rybáře hledajícího přesné nastavení'],
              ['Penn', 'robustní mořské a těžké modely', 'mořský rybolov a těžké nástrahy'],
              ['DAM', 'střední třída, dostupné navijáky', 'začátečník, který hledá solidní základ']]) +
          '<p>Rozdíly nejsou v tom, že jedna značka je lepší, ale v tom, na co je stavěná. Fox se v kategorii kaprařských navijáků hodí tehdy, kdy ocení kompletní řadu na jednom místě. Pokud lovíte přívlačí nebo plavanou, podívejte se do výběru <a href="/navijaky-penn/">navijáků Penn</a> nebo <a href="/navijaky-dam/">navijáků DAM</a>, případně do kategorie <a href="/muskareni/">muškaření</a>, kde se používají jiné konstrukce.</p>'
          '<h2>Pouzdro na naviják a ochrana při přepravě</h2>'
          '<p>V nabídce značky Fox se objevuje také pouzdro na naviják, které stojí za pozornost. Naviják je citlivý na nárazy, prach a písek, a zvlášť při převozu v autě nebo v tašce na bivak se cívka snadno poškrábe nebo ohne rukojeť. Tvrdé nebo polstrované pouzdro ochrání mechanismus, brzdu i cívku. Pokud skládáte vlastní výbavu, hodí se také <a href="/rybarske-tasky/">tašky, pouzdra a krabičky</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>. Před uložením naviják zbavte písku a bláta, protože zrnka dřív nebo později poškodí ložiska.</p>'
          '<h2>Péče a údržba navijáku</h2>'
          '<ol><li>Po rybolovu naviják osušte hadříkem, zejména po použití ve slané nebo bahnité vodě.</li>'
          '<li>Povolte brzdu při delším uložení, aby se nepřetěžovaly kotouče.</li>'
          '<li>Cívku, kliku a ložiska občas promažte kapkou oleje určeného pro navijáky, ale nepřeplňujte ji.</li>'
          '<li>Vlasec po sezóně vyměňte, protože ztrácí pevnost a zkrucuje se.</li>'
          '<li>Neodkládejte naviják na slunci nebo u topení, plasty mohou měknout a těsnění vysychat.</li></ol>'
          '<h2>Kdy se vyplatí rozdělit výbavu a kdy vzít celou sadu</h2>'
          '<p>Kapraři často řeší, zda koupit dva nebo tři stejné navijáky pro více prutů. Stejná řada má výhodu, že kliky, cívky i náhradní díly jsou zaměnitelné, takže při poruše přehodíte cívku z jednoho kusu na druhý. Při výběru dvou a více kusů proto kupujte ze stejné řady a stejné velikosti a ověřte, že se k nim prodává náhradní cívka. U jediné soupravy pro začátečníka naopak stačí jeden dobrý naviják a rozumný prut; peníze za druhý kus je lepší investovat do kvalitního vlasce, olova a podběráku.</p>'
          '<p>Před první sezónou si naviják vyzkoušejte při suchém tréninku: nasaďte vlasec, nastavte brzdu, přetáhněte ručně a zkontrolujte, zda se brzda rozjíždí bez cukání. Při prvním výjezdu k vodě se zaměřte na to, jak vlasec ukládá cívka. Pokud se tvoří smyčky nebo vlasec padá z okraje, je cívka přeplněná. Vlasec má končit zhruba dva až tři milimetry pod okrajem cívky, ne výš.</p>'
          '<h2>Co zvažovat před koupí</h2>'
          '<p>Nejdřív si ujasněte, kde budete lovit. Menší rybník vyžaduje jiný naviják než velká přehrada, na které potřebujete dálkové náhozy. Potom zkontrolujte, zda ke koupi patří náhradní cívka a jaká je záruka. Zeptejte se, jak se mění jednotlivé díly, protože u velkých navijáků se může opotřebovat ložisko nebo kolečko. Porovnejte vždy stejný model u více obchodů, protože se mohou lišit dostupnou velikostí, i když jde o stejnou řadu. Pokud budete naviják používat pravidelně, vyplatí se investovat do kvalitnějšího kusu s lepší brzdou. Pro obecné rady o typech a velikostech si přečtěte průvodce v kategorii <a href="/rybareni/">rybaření</a> a v hlavní kategorii <a href="/rybarske-navijaky/">navijáky</a>. Značku najdete také na stránce <a href="/znacka/fox/">Fox</a>.</p>',
    faq=[
        ('Pro jaký rybolov jsou navijáky Fox určeny?', 'Fox se zaměřuje hlavně na kaprařský rybolov. Navijáky jsou robustní, s velkou cívkou a vhodné pro daleké náhozy a zdolávání větších ryb. Na jemnou přívlač nebo plavanou jsou obvykle příliš velké.'),
        ('Co znamenají čísla 8000, 10000, 12000 a 14000?', 'Jde o označení velikosti navijáku. Vyšší číslo znamená větší cívku, vyšší hmotnost a větší kapacitu vlasce. Přesnou kapacitu uvádí výrobce v popisu každého modelu pro konkrétní průměr vlasce.'),
        ('Jak velký naviják Fox zvolit?', 'Pro běžné kapraření na rybníku stačí 8000 nebo 10000. Pro velké nádrže a dlouhé náhozy volte 12000 a větší. Rozhodující je i prut: souprava se nemá překlápět dopředu a naviják musí odpovídat testovací křivce.'),
        ('Co je volnoběh a proč ho kapraři potřebují?', 'Volnoběh je mechanismus, který uvolní vlasec bez brzdy, takže kapr po záběru může odplavat, aniž by prut spadl z podložek. Při zdolávání se přepne zpět na normální brzdu.'),
        ('Co znamená označení FD v názvu navijáku?', 'Obvykle jde o přední brzdu, tedy front drag. Brzda se nastavuje otáčením knoflíku na přední straně cívky. Konkrétní provedení si ověřte v popisu daného modelu.'),
        ('Mohu na naviják Fox použít pletenou šňůru?', 'Ano, pokud je cívka vhodná a prut má kvalitní vodítka. Pletená šňůra se nenatahuje, proto je důležité správně nastavit brzdu. Při změně vlasce kontrolujte doporučený průměr uvedený výrobcem.'),
        ('Jak naviják ochránit při převozu?', 'Použijte tvrdé nebo polstrované pouzdro, které chrání cívku, brzdu a rukojeť před nárazy, prachem a pískem. Pouzdro značky Fox je určeno právě pro tento účel a patří k nabídce stránky.'),
        ('Jak často vyměňovat vlasec?', 'Záleží na četnosti rybolovu a typu vlasce. Monofilní vlasec se doporučuje měnit alespoň jednou za sezónu, pletená šňůra vydrží déle, ale je nutné ji kontrolovat. Poškozený nebo zkroucený vlasec vyměňte hned.'),
        ('Čím se navijáky Fox liší od Shimano nebo Daiwa?', 'Fox se orientuje na kapraře a nabízí velké kaprařské modely, zatímco Shimano a Daiwa mají širší nabídku od přívlače po moře. Volba závisí na technice lovu, ne na tom, kdo je lepší.'),
        ('Kde porovnat ceny navijáků Fox?', 'U každého kusu na této stránce vidíte nabídky obchodů vedle sebe i s dopravou. Před koupí si ověřte velikost, typ brzdy a dostupnost náhradních dílů.'),
    ],
)

# ------------------------------------------------------------------ sportovni-obleceni-panske
NEW['sportovni-obleceni-panske'] = dict(
    title='Sportovní oblečení pánské: střihy, značky, výběr',
    desc='Pánské sportovní oblečení: střihy a velikosti, rozdíly mezi značkami Nike, Adidas, Puma, Under Armour a Columbia, vrstvení a výběr podle sportu a sezóny.',
    intro='<p>Pánské sportovní oblečení se liší od dámského hlavně střihem v ramenou a hrudi, délkou rukávů i způsobem, jakým látka sedí v pase. Sortiment je obrovský: od funkčního spodního prádla přes trička, mikiny a bundy až po kraťasy, tepláky a soupravy. Tato stránka zúžila kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a> na kusy pro muže a chlapce ve větších velikostech. Průvodce vysvětluje, jak vybrat velikost, jak se liší střihy značek, kdy sáhnout po funkčním materiálu a kdy stačí bavlna, a jak z kusů složit výbavu pro běh, posilovnu, outdoor a každodenní nošení. Zahrnuje i tipy na sezónní nákup, srovnání značek a praktickou péči o oblečení.</p>',
    guide='<h2>Čím se pánský střih liší</h2>'
          '<p>Pánské sportovní oblečení je stavěno na širší ramena, rovnější linii pasu a delší trup. Rukávy jsou delší, průramky větší a lem mikin a triček sahá níž přes pás. Nejde jen o velikost, ale o poměry. Muž s úzkými rameny a vyšší postavou se často cítí lépe v modelech s úzkým střihem, silnější postava naopak ocení volný střih nebo model s pružným materiálem. Většina značek dnes nabízí tři základní střihy.</p>'
          + T(['Střih', 'Jak sedí', 'Kdy se hodí'], [
              ['Přiléhavý (slim, fitted, tight)', 'tělo obepíná, rukávy a boky bez záhybů', 'běh, kompresní vrstva, kolo, silový trénink'],
              ['Běžný (regular)', 'bez tlaku, s malou rezervou', 'každodenní nošení, fitness, trénink v týmu'],
              ['Volný (relaxed, oversize)', 'prostorný, delší, nižší průramky', 'streetwear, basketbal, volný čas'],
              ['Atletický (athletic fit)', 'širší hrudník, užší pas', 'silnější ramena a hrudník, aktivní cvičení']]) +
          '<p>Při výběru velikosti porovnejte svůj obvod hrudníku, pasu a délku paže s tabulkou značky. Pokud jste mezi velikostmi, rozhodněte podle účelu: u přiléhavé vrstvy bývá lepší menší velikost, u mikiny a bundy větší, aby se pod ni vešla další vrstva.</p>'
          '<h2>Základní kusy pánské sportovní výbavy</h2>'
          '<ul><li><strong>Trička:</strong> funkční na běh a trénink, bavlněná na každý den. Výběr najdete v kategorii <a href="/sportovni-tricka/">sportovní trička</a> a <a href="/funkcni-tricka/">funkční trička</a>.</li>'
          '<li><strong>Mikiny:</strong> střední vrstva, vhodná i do města, kategorie <a href="/mikiny/">mikiny</a>.</li>'
          '<li><strong>Bundy a větrovky:</strong> od lehkých <a href="/vetrovky/">větrovek</a> po zimní kusy, vše v <a href="/sportovni-bundy/">sportovních bundách</a>.</li>'
          '<li><strong>Kalhoty a tepláky:</strong> <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/teplaky/">tepláky</a> pro trénink i volný čas.</li>'
          '<li><strong>Kraťasy:</strong> lehké na běh, delší do posilovny, viz <a href="/sportovni-kratasy/">sportovní kraťasy</a>.</li>'
          '<li><strong>Spodní vrstva:</strong> <a href="/termopradlo/">termoprádlo</a> a <a href="/leginy/">legíny</a> pod kalhoty při chladu.</li>'
          '<li><strong>Soupravy:</strong> sladěné <a href="/soupravy/">soupravy</a> pro pohodlný a jednotný vzhled.</li></ul>'
          '<h2>Rozdíly mezi značkami</h2>'
          '<p>Největší nabídku v pánském sportovním oblečení mají značky jako New Era, Nike, Adidas, Puma a Under Armour. New Era je známá hlavně kšiltovkami a licencovanými kousky týmů amerických lig, Mitchell &amp; Ness retro dresy a oblečením s klubovými motivy. Nike a Adidas pokrývají širokou paletu od běhu přes fotbal po streetwear. Puma bývá oblíbená pro střihy blízké životnímu stylu, Under Armour pro přiléhavé tréninkové vrstvy.</p>'
          '<p>Další značky mají jiné zaměření. Columbia, The North Face, Helly Hansen a Haglöfs patří do outdooru: bundy, fleecy a větrovky na hory a chladné počasí. Regatta a Trespass nabízejí outdoorové oblečení širší veřejnosti, Kilpi a Northfinder jsou domácí značky s praktickým poměrem funkce a použití. Champion, Fila, Gap a Tommy Hilfiger se pohybují blíž ke sportovnímu stylu každodenního nošení. Dynafit se zaměřuje na horské lyžování a běh v terénu, Speedo na plavání. Odkazy na značky: ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('champion', 'Champion'), ('columbia', 'Columbia'), ('the-north-face', 'The North Face'), ('helly-hansen', 'Helly Hansen'), ('new-era', 'New Era')) + '.</p>'
          '<h2>Vrstvení pro muže: tři vrstvy od kůže ven</h2>'
          '<p>Vrstvení funguje stejně u mužů i u žen, ale muži obecně více pocí a rychleji se zahřívají při pohybu, proto je u nich důležitější prodyšný spodní materiál. Spodní kus pracuje s potem, střední drží teplo a vnější brání větru. Při zimním běhu stačí tričko s dlouhým rukávem a větrovka, při túře přidejte fleece nebo funkční mikinu. Bavlněné tričko na kůži vypadá pohodlně, ale po zpocení chladí. Nejlépe fungují polyester, polyamid nebo merino. Velmi podrobně se vrstvení věnuje průvodce v hlavní kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>'
          '<h2>Výběr podle sportu</h2>'
          + T(['Sport', 'Základ výbavy', 'Na co si dát pozor'], [
              ['Běh', 'lehké tričko, kraťasy nebo legíny, větrovka', 'reflexní prvky, švy bez tření, prodyšnost'],
              ['Posilovna', 'funkční tričko, kraťasy, sportovní kalhoty', 'volnost v ramenou, pružný materiál při dřepech'],
              ['Fotbal a týmové sporty', 'dres, kraťasy, tepláky, mikina na rozcvičku', 'odolnost proti praní, jednotná barva týmu'],
              ['Turistika', 'funkční tričko, kalhoty, fleece, bunda', 'rychleschnoucí materiál, rezerva na změnu počasí'],
              ['Kolo', 'cyklistický dres, kraťasy se vložkou', 'delší záda, kapsy, viditelnost'],
              ['Plavání', 'plavky nebo plavecké kraťasy', 'chlór poškozuje elastan, po použití vypláchnout']]) +
          '<p>Pokud pravidelně provozujete víc sportů, začněte univerzálními kusy, které použijete všude: dobré funkční tričko, pohodlné kraťasy a lehkou větrovku. Specializované kousky přikupujte až podle potřeby.</p>'
          '<h2>Materiály a na co dát pozor</h2>'
          '<p>Polyester je nejběžnější materiál funkčních triček. Rychle schne a drží tvar, ale může zadržovat pach. Bavlna je příjemná na dotek, ale po zpocení těžkne. Směsi bavlny s polyesterem jsou kompromis, který se hodí do posilovny a na každodenní nošení. Elastan přidává pružnost, merino vlna hřeje i za vlhka a pomalu pachne. Fleece izoluje při nízké hmotnosti, ale nezastaví vítr. Membrány v bundách zadrží déšť, ale ztěžují odvod vlhkosti, proto se hodí hlavně do špatného počasí a při klidnější aktivitě.</p>'
          '<h2>Sezónní nákup: kdy sportovní oblečení koupit</h2>'
          '<p>Slevy se objevují na konci sezóny, kdy obchody uvolňují místo nové kolekci. Zimní bundy a mikiny bývají levnější na jaře, letní trička a kraťasy na podzim. Velikosti, které se rozprodávají poslední, jsou obvykle nejčastější, tedy střední. Mimo sezónu proto stojí za to hledat i neobvyklejší velikosti, například XS nebo 3XL, které prodejce zvýhodňuje spíše výjimečně. Pokud nepotřebujete nejnovější kolekci, kusy z minulé sezóny jsou často stejně kvalitní. Ve srovnávači vidíte nabídky více obchodů vedle sebe, takže jednoduše poznáte, který model je zrovna dostupný ve vaší velikosti.</p>'
          '<h2>Velké a malé postavy, vyšší a nižší muži</h2>'
          '<p>Standardní tabulky počítají se střední postavou, jenže muži se liší výškou i stavbou víc než velikost označená písmenem. Vysoký štíhlý muž bývá v běžné velikosti L krátký v rukávech a v pase, zatímco menší a silnější postava má v téže velikosti rukávy příliš dlouhé. Pomůže vybírat podle rozměrů v tabulce, ne jen podle písmene. Mnoho značek nabízí velikosti přes XL a 3XL i XXS, ale ne vždy ve všech střizích, proto při neobvyklé velikosti porovnejte nabídky více obchodů vedle sebe. U kalhot a tepláků zkontrolujte vnitřní délku nohavice a u mikin délku rukávu, protože právě tam se nejčastěji ukáže, že kus nesedí.</p>'
          '<h2>Teplákovka, nebo funkční oblečení</h2>'
          '<p>Klasická teplákovka z bavlny a směsí je příjemná, hřeje a dobře vypadá ve městě, doma i na lehkém tréninku. Při intenzivním pohybu ale nasákne potem a pomalu schne. Funkční kusy z polyesteru jsou lehčí, drží tvar a rychleji schnou, na dotek ale působí sportovněji. Pro běh, kolo a týmové sporty zvolte funkční materiál, pro posilovnu a volný čas stačí směs. Někteří muži kombinují oboje: funkční tričko na tělo a teplou mikinu zvenku.</p>'
          '<h2>Jak zkoušet a na co si dát pozor</h2>'
          '<ul><li>Zvedněte ruce nad hlavu: tričko a mikina se nesmí vyhrnout nad pás a rukávy nesmí zalézat k lokti.</li>'
          '<li>Udělejte dřep a předklon: kalhoty a kraťasy by měly držet na místě a nikde netlačit.</li>'
          '<li>Zkontrolujte švy v podpaží a u rozkroku, právě tam vznikají odřeniny při běhu.</li>'
          '<li>Prohlédněte si složení v etiketě: čím vyšší podíl polyesteru nebo polyamidu, tím rychleji kus schne.</li>'
          '<li>U bund ověřte, zda se kapuce nastavuje a zda rukávy dovolují nosit rukavice.</li></ul>'
          '<h2>Péče o pánské sportovní oblečení</h2>'
          '<ul><li>Funkční materiály perte bez aviváže, která zalepuje póry a snižuje odvod potu.</li>'
          '<li>Potištěné kusy otočte naruby, aby se potisk nepoškodil.</li>'
          '<li>Bundy s membránou perte vhodným prostředkem a po vyschnutí krátce zahřejte, aby se obnovila impregnace.</li>'
          '<li>Sušte na vzduchu nebo při nízké teplotě, vysoké teplo poškozuje elastan.</li>'
          '<li>Zpocené oblečení nenechávejte ve sportovní tašce, pach se vsákne do vláken.</li></ul>'
          '<h2>Další výběry</h2>'
          '<p>Pokud hledáte i pro ostatní členy rodiny, podívejte se na stránky <a href="/sportovni-obleceni-damske/">sportovní oblečení dámské</a> a <a href="/detske-sportovni-obleceni/">dětské sportovní oblečení</a>. K sadě se hodí i <a href="/sportovni-ponozky/">sportovní ponožky</a>, <a href="/dresy/">dresy</a> a oblečení pro <a href="/beh/">běh</a> nebo <a href="/fitness/">fitness</a>.</p>',
    faq=[
        ('Čím se pánské sportovní oblečení liší od dámského?', 'Hlavně střihem a proporcemi. Pánské kusy mají širší ramena, rovnější pas a delší rukávy a trup. Dámské jsou užší v ramenou a pase a vyšší v boku. Rozdíly se projeví při dlouhém nošení.'),
        ('Jak vybrat velikost pánského sportovního oblečení?', 'Změřte obvod hrudníku, pasu a délku paže a porovnejte je s tabulkou výrobce. Mezi velikostmi volte menší u přiléhavé vrstvy a větší u mikiny nebo bundy, pod které chcete vrstvit.'),
        ('Které značky jsou vhodné na běh?', 'Pro běh nabízejí lehké a prodyšné kusy například Nike, Adidas, Puma a Under Armour. Dynafit je zaměřený na terénní běh. Důležitější než značka je střih, materiál a reflexní prvky.'),
        ('Je lepší bavlna, nebo funkční materiál?', 'Na pohyb, při kterém se zapotíte, je lepší polyester nebo merino, protože rychle odvádí vlhkost. Bavlna je vhodná na volný čas, posilovnu při nízké zátěži a každodenní nošení.'),
        ('Co si obléknout na zimní běh?', 'Základem je funkční tričko s dlouhým rukávem, větrovka nebo lehká bunda, čepice a rukavice. Při velmi nízkých teplotách přidejte termoprádlo. Oblečení volte o vrstvu lehčí než na procházku, tělo se při běhu zahřeje.'),
        ('Čím se liší outdoorové značky od sportovních?', 'Outdoorové značky, jako Columbia, The North Face, Helly Hansen nebo Haglöfs, se zaměřují na ochranu před počasím. Sportovní značky, například Nike nebo Adidas, kladou důraz na pohyb a styl.'),
        ('Jak prát sportovní oblečení, aby vydrželo?', 'Perte při nižší teplotě bez aviváže, potištěné kusy naruby. Nesušte při vysoké teplotě, poškodí se elastan a potisk. Bundy s membránou perte speciálním prostředkem a obnovte impregnaci.'),
        ('Kdy se sportovní oblečení nejvíc zlevňuje?', 'Na konci sezóny a při obměně kolekce. Zimní kusy jsou levnější na jaře, letní na podzim. Ve srovnávači vidíte nabídky více obchodů, takže poznáte, kde je váš model aktuálně nejvýhodnější.'),
        ('Mohu nosit sportovní oblečení i do města?', 'Ano, mikiny, tepláky, trička a bundy se nosí i ve městě. Pro delší nošení vybírejte střih regular nebo relaxed, jednobarevné kusy a materiály, které se nemačkají.'),
        ('Jak složit základní sportovní výbavu pro muže?', 'Začněte dvěma funkčními tričky, kraťasy, sportovními kalhotami, mikinou a lehkou větrovkou. Doplňte ponožky a spodní vrstvu podle sportu. Specializované kusy přikupujte až podle toho, co skutečně potřebujete.'),
    ],
)

# ------------------------------------------------------------------ cyklisticke-dresy-damske
NEW['cyklisticke-dresy-damske'] = dict(
    title='Cyklistické dresy dámské: střih, velikost a značky',
    desc='Dámské cyklistické dresy: střih v ramenou a pase, velikosti, silniční a MTB varianty, značky Silvini, Siroko, Rockbros či Löffler a péče o dres.',
    intro='<p>Dámský cyklistický dres není jen zmenšená verze pánského. Má užší ramena, kratší záda, tvarovaný pas a výstřih i zip upravené pro ženskou postavu, aby se při předklonu v sedle nezvedal a netlačil. Rozdíl je znát hlavně při delší jízdě, kdy špatně padnoucí dres tře, bublá nebo se vyhrnuje. Stránka vybírá z kategorie <a href="/cyklisticke-dresy/">cyklistické dresy</a> kusy určené ženám a dívkám, od lehkých silničních modelů přes volnější MTB dresy po kousky na výlety a dojíždění. Průvodce popisuje velikosti, střihy, materiály, rozdíly mezi značkami, vrstvení v jednotlivých ročních obdobích i to, jak dres správně vyzkoušet a udržovat, aby vydržel několik sezón. Cenu a dostupnost velikostí porovnáte přímo u každého dresu.</p>',
    guide='<h2>V čem se dámský dres liší od pánského</h2>'
          '<p>Rozdíly jsou drobné, ale při delší jízdě znatelné. Ženské postavy mají obvykle užší ramena a kratší trup, výraznější pas a bok a odlišné proporce v místě hrudníku. Dámský dres to reflektuje v několika místech.</p>'
          + T(['Část dresu', 'Dámská úprava', 'Proč na tom záleží'], [
              ['Ramena a průramky', 'užší, jemněji tvarované', 'dres nesklouzává a netře v podpaží'],
              ['Délka těla', 'kratší záda a lem, často lehce tvarovaný', 'nezvedá se nad kalhoty a nepřekáží v sedle'],
              ['Pas a boky', 'zúžený pas, volnější boky', 'dres sedí bez vrásek a nebublá'],
              ['Zip a výstřih', 'kratší nebo hlouběji sahající zip, někdy skrytý', 'větrání bez odhalení při předklonu'],
              ['Rukávy', 'užší a kratší manžety', 'netlačí na paži a nesjíždí nahoru'],
              ['Silikonový lem', 'tenčí pás po obvodu lemu', 'drží na místě bez tlaku na žebra']]) +
          '<p>Platí, že pokud vám vyhovuje unisex nebo pánský dres, nemusíte ho měnit. Ženy s širšími rameny nebo vyšší postavou ho někdy preferují. Pro většinu cyklistek ale dámský střih znamená větší pohodlí na kole, zejména při dlouhých trasách a v předklonu na silničním kole.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Velikosti dámských cyklistických dresů se značně liší podle výrobce. Evropské značky používají označení XS až XXL, ale tabulky se mohou lišit až o celou velikost. Proto je potřeba změřit obvod hrudníku v nejširším místě, pas v nejužším místě a boky a poté je porovnat s tabulkou konkrétního kusu. Dres má sedět přiléhavě, ale nesmí tlačit při hlubokém nádechu. Pokud jste mezi velikostmi, u silničního dresu zvažte menší, u volného MTB dresu větší.</p>'
          '<ul><li><strong>Hrudník:</strong> dres by neměl tlačit pod prsy ani na ramena.</li>'
          '<li><strong>Délka:</strong> záda musí v předklonu zakrývat spodek zad a lem nesmí sjíždět.</li>'
          '<li><strong>Rukávy:</strong> manžeta nesmí zařezávat do paže ani stoupat nahoru.</li>'
          '<li><strong>Zip:</strong> při předklonu se nesmí otevírat a nesmí škrábat na krku.</li>'
          '<li><strong>Kapsy:</strong> vzadu na zádech, hluboké, aby telefon nevypadl při jízdě v nerovném terénu.</li></ul>'
          '<p>Dres vždy zkoušejte v pozici, v jaké budete jezdit, tedy v předklonu a s napnutými pažemi. Ve stoje před zrcadlem budou vypadat všechny střihy jinak.</p>'
          '<h2>Silniční, MTB a výletní dres</h2>'
          + T(['Typ dresu', 'Střih', 'Kdy se hodí'], [
              ['Silniční', 'přiléhavý, delší záda, dlouhý zip', 'rychlá jízda po silnici, sportovní výlety'],
              ['MTB a trail', 'volnější, kratší zip, někdy delší rukáv', 'jízda v terénu, lesní trasy, enduro'],
              ['Výletní a trekingový', 'pohodlný, běžný střih', 'dojíždění, vyjížďky, cykloturistika'],
              ['S dlouhým rukávem', 'přiléhavý rukáv, tenká zateplená vrstva', 'jaro, podzim, ranní jízda'],
              ['Lehký na horko', 'tenký prodyšný úplet, síťované vložky', 'letní vedra, dlouhé stoupání']]) +
          '<p>Silniční dres je nejlépe přizpůsoben aerodynamickému postoji a bývá nejpřiléhavější. MTB dresy jsou volnější, protože při jízdě v terénu jezdkyně více mění polohu a potřebuje volnost. Pro dojíždění stačí pohodlný střih, který se dá nosit i mimo kolo. Více o druzích dresů se dočtete v kategorii <a href="/cyklisticke-dresy/">cyklistické dresy</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr dámských cyklistických dresů mají značky ' + B(('silvini', 'Silvini'), ('siroko', 'Siroko'), ('rockbros', 'Rockbros')) + '. Silvini je italská značka zaměřená na cyklistické oblečení pro silnici i horská kola, Siroko španělská značka s důrazem na střihy a vzory a Rockbros čínský výrobce cyklistického vybavení s širokým sortimentem pro začátečníky. Dále najdete ' + B(('haven', 'Haven'), ('loeffler', 'Löffler'), ('kilpi', 'Kilpi'), ('etape', 'Etape'), ('sportful', 'Sportful'), ('craft', 'Craft'), ('rockrider', 'Rockrider'), ('northwave', 'Northwave'), ('crussis', 'Crussis'), ('sensor', 'Sensor')) + '.</p>'
          '<p>Löffler, Craft a Sportful bývají oblíbené u ambicióznějších jezdců pro střihy a materiály určené na delší trasy. Etape je česká značka zaměřená na cyklistické oblečení, Kilpi nabízí outdoorové a cyklistické kusy pro širší veřejnost. Rockrider patří obchodnímu řetězci Decathlon a míří na začátečníky a pokročilé amatéry. Pokud nevíte, kterou značku zvolit, vyberte podle střihu, který vám sedí, a ne podle jména.</p>'
          '<h2>Materiály a funkce</h2>'
          '<ul><li><strong>Polyester:</strong> základ většiny dresů, rychle schne a odvádí pot.</li>'
          '<li><strong>Elastan:</strong> dodává pružnost, aby se dres přizpůsobil poloze v sedle.</li>'
          '<li><strong>Merino:</strong> hřeje i za vlhka, pomalu pachne, ale je citlivější při praní.</li>'
          '<li><strong>Síťované vložky:</strong> zlepšují větrání v místech největšího pocení.</li>'
          '<li><strong>Reflexní prvky:</strong> zvyšují viditelnost při jízdě za šera.</li>'
          '<li><strong>UV ochrana:</strong> užitečná při dlouhých letních trasách bez stínu.</li></ul>'
          '<p>Při výběru barev si pamatujte, že světlé dresy odráží slunce a na silnici jsou lépe vidět, tmavé jsou praktické, ale v létě se víc zahřívají. Fluorescenční barvy se dají použít jako bezpečnostní prvek, ale rychleji blednou praním.</p>'
          '<h2>Dres a sportovní podprsenka</h2>'
          '<p>Pod cyklistický dres se obvykle nosí <a href="/sportovni-podprsenky/">sportovní podprsenka</a>, protože dámský dres je střižen s ohledem na prsa, ale nenahrazuje podporu. Při jízdě na silnici stačí lehčí podpora, u terénního kola s otřesy volte silnější. Podprsenka by neměla mít silné švy na ramenou ani na zádech, kde se opírá o kapsy dresu. Při výběru dresu proto vždy zkoušejte spolu s podprsenkou, kterou budete na kole nosit.</p>'
          '<h2>Dres podle ročního období</h2>'
          + T(['Období', 'Co si obléknout', 'Poznámka'], [
              ['Léto', 'lehký dres s krátkým rukávem, světlá barva', 'síťované vložky, UV ochrana, dostatek tekutin'],
              ['Jaro a podzim', 'dres s dlouhým rukávem nebo krátký s návleky', 'ráno chladno, odpoledne teplo, zip se hodí'],
              ['Zima', 'zateplený dres nebo bunda přes spodní vrstvu', 'větruodolná přední část, dlouhé kalhoty'],
              ['Déšť', 'lehká bunda přes dres', 'pláštěnka s prodyšností, reflexní prvky']]) +
          '<p>Základem je vrstvení: jedna dobře zvolená vrstva pod dresem vás zahřeje lépe než jeden příliš silný dres. Při první jízdě v nové sezóně počítejte s tím, že se po deseti minutách zahřejete, a obléknete se o něco lehčeji, než by se zdálo. Lehká <a href="/vetrovky/">větrovka</a> v kapse zachrání nečekaný vítr a studený sjezd.</p>'
          '<h2>Dres pro začátečnice a pro ty, co jezdí často</h2>'
          '<p>Kdo s cyklistikou začíná, nemusí kupovat nejdražší model. Pro první sezónu stačí pohodlný dres s kapsami a střih regular, který dovoluje volný pohyb. Pokud jezdíte několikrát týdně, vyplatí se mít alespoň tři dresy, aby jeden vždy čekal čistý. Pravidelné jezdkyně často poznají rozdíl až po delší trase: dres s kvalitním úpletem při deseti hodinách v sedle netře, nešpiní se a nezapáchá. U drahých dresů zkontrolujte rovněž stahování zipu a strukturu lemů, na kterých se tvoří první obtíže.</p>'
          '<h2>Jak dres kombinovat</h2>'
          '<p>Dres je jen jedna část výbavy. K němu se nosí <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy a kalhoty</a> s vložkou, <a href="/cyklisticke-rukavice/">rukavice</a>, <a href="/cyklisticke-helmy/">helma</a> a <a href="/cyklisticke-bryle/">brýle</a>. V chladu přidejte spodní vrstvu a větrovku. Pro srovnání dámských a pánských střihů se podívejte na landing <a href="/cyklisticke-dresy-panske/">cyklistické dresy pánské</a>. Celkový přehled najdete v kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>'
          '<h2>Péče o cyklistický dres</h2>'
          '<ol><li>Perte dres po každé jízdě, pot a krém na opalování zanechávají v materiálu zbytky.</li>'
          '<li>Použijte nízkou teplotu a jemný prací prostředek bez aviváže.</li>'
          '<li>Zapněte zip, aby se nezachytil a nepoškodil jiné prádlo.</li>'
          '<li>Sušte na vzduchu, ne na topení nebo v sušičce.</li>'
          '<li>Nežehlete potisky a reflexní prvky.</li></ol>'
          '<p>Správně udržovaný dres vydrží několik sezón. Pokud po praní zjistíte, že látka už neodvádí pot a lepí se na tělo, nejspíš ji ucpala aviváž nebo zbytky pracího prášku. Pomůže prát bez aviváže a dvakrát vypláchnout.</p>'
          '<h2>Chyby, kterým se vyhnout</h2>'
          '<ul><li>Nákup příliš velkého dresu, ve kterém látka vlaje a tře.</li>'
          '<li>Výběr podle barvy bez kontroly velikostní tabulky.</li>'
          '<li>Pranutí s aviváží, které snižuje odvod potu.</li>'
          '<li>Použití bavlněného trička místo dresu na delší trasy.</li>'
          '<li>Ignorování viditelnosti při jízdě v provozu.</li></ul>',
    faq=[
        ('Čím se dámský cyklistický dres liší od pánského?', 'Má užší ramena, kratší záda, tvarovaný pas a upravený zip i manžety. Díky tomu v předklonu nesjíždí a netlačí. Pokud vám sedí unisex dres, nemusíte ho měnit.'),
        ('Jak vybrat správnou velikost dámského dresu?', 'Změřte hrudník, pas a boky a porovnejte je s tabulkou výrobce. Dres má přiléhat, ale netlačit při nádechu. Zkoušejte ho v předklonu, ne ve stoje.'),
        ('Jaký dres zvolit na silnici a jaký na horská kola?', 'Na silnici se hodí přiléhavý dres s dlouhým zipem a delšími zády, na MTB volnější s kratším zipem. Na dojíždění stačí pohodlný běžný střih.'),
        ('Z jakého materiálu má být cyklistický dres?', 'Nejčastěji z polyesteru s elastanem, který rychle schne a je pružný. Merino se hodí do chladu a na delší trasy. Bavlna se nehodí, protože po zpocení těžkne.'),
        ('Jak často prát cyklistický dres?', 'Nejlépe po každé jízdě. Pot a zbytky krémů se do vláken zažerou, zhoršují odvod vlhkosti a způsobují pach. Perte při nízké teplotě a bez aviváže.'),
        ('Jaká barva dresu je nejlepší?', 'Do provozu světlá nebo výrazná, která je lépe vidět, do terénu libovolná. Světlé barvy odrážejí slunce a v létě méně hřejí, tmavé se víc zahřívají.'),
        ('Mohu používat pánský cyklistický dres?', 'Ano, pokud vám sedí v ramenou a v pase. Pánské střihy bývají širší a delší, proto je u menších žen může při jízdě vyhrnovat. Zkuste oba střihy v předklonu a vyberte ten pohodlnější.'),
        ('Co si obléct pod cyklistický dres v chladu?', 'Funkční spodní tričko z polyesteru nebo merina. Vyhněte se bavlně. Při nižších teplotách přidejte větrovku nebo lehkou vestu, kterou můžete při oteplení sbalit do kapsy.'),
        ('Kde koupit dámský cyklistický dres?', 'Na této stránce vidíte nabídky více obchodů vedle sebe. Před koupí zkontrolujte velikostní tabulku konkrétní značky, dostupnost své velikosti a podmínky vrácení.'),
    ],
)
