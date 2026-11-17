"""sporteka.cz — wave 30a (17. 11. 2026): long texts for snehule, cargo-kalhoty, zateplene-leginy, vlozky-do-bot.
General true facts only, no prices, no product counts. Temperature ratings of snow boots described as the maker's own estimate,
no norms. Thermal leggings and insoles without health or medical promises; orthopaedic insoles are left to a doctor
(public health insurance contributes only to custom-made insoles on prescription, serial ones are not covered).
Brands linked only if present in src/texts/znacky.json, the rest are named as plain text."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ snehule
NEW['snehule'] = dict(long=True,
    title='Sněhule dámské, pánské i dětské: do sněhu i do města',
    desc='Dámské, pánské a dětské sněhule s gumovou vanou, vyjímatelnou vložkou nebo kožíškem. Jak vybrat velikost, zateplení a podrážku a kde je mají e-shopy.',
    intro='<p><strong>Sněhule</strong> jsou vysoké zimní boty stavěné do hlubokého sněhu, rozbředlé břečky a kaluží. Spodní část bývá z gumy nebo jiného nepromokavého materiálu, horní z nylonu, kůže či semiše a uvnitř je silná izolace, často s vyjímatelnou vložkou. Od běžných zimních bot se liší hlavně výškou, větším objemem a tím, že počítají s dlouhým stáním a chozením ve sněhu, nikoli s rychlou chůzí na dlouhé vzdálenosti.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u vybraného páru uvidíte, kdo ho prodává a ve kterých velikostech. Nákup pak proběhne v obchodě, jehož nabídku si zvolíte. Mezi značkami najdete například '
          + B(('cmp', 'CMP'), ('trespass', 'Trespass'), ('o-neill', "O'Neill"), ('reima', 'Reima')) +
          ', dále Ugg, Tamaris nebo Didriksons. Sněhule jsou podskupinou kategorie <a href="/zimni-obuv/">zimní boty a sněhule</a>, na mokré podzimní dny se hodí spíš <a href="/holinky/">holínky</a>.</p>',
    guide='<h2>Co dělá sněhuli sněhulí</h2>'
          '<p>Typická sněhule má tři části. Dole je vana, tedy nepromokavá skořepina, která obepíná chodidlo a sahá zhruba ke kotníku. Nad ní pokračuje vysoký svršek, který brání sněhu napadat dovnitř a bývá ukončený stahovací šňůrkou nebo manžetou. Uvnitř je izolace: buď pevně všitá, nebo ve formě vložky z plsti či syntetické vaty, kterou lze vytáhnout a vysušit. Podrážka je silnější než u městské obuvi a má hlubší vzorek, aby se nezanášela sněhem.</p>'
          '<p>Vedle tohoto klasického tvaru se jako sněhule prodávají i nižší zateplené boty s chlupatou podšívkou, přezůvkové boty typu après-ski s nafouknutým svrškem a módní kozačky z ovčí kůže. Všechny hřejí, ale do mokrého sněhu se hodí jen ty, které mají opravdu nepromokavou spodní část.</p>'
          + T(['Typ', 'Konstrukce', 'Kam se hodí'], [
              ['Klasická sněhule s vanou', 'gumová spodní část, textilní svršek, často vyjímatelná vložka', 'hluboký sníh, sáňkování, delší pobyt venku'],
              ['Sněhule s membránou', 'svršek z textilu nebo kůže s nepromokavou vrstvou uvnitř', 'mokrý sníh i chůze po městě'],
              ['Après-ski a moon boot styl', 'objemný prošívaný svršek, měkká podrážka', 'krátké přesuny na horách, suchý mráz'],
              ['Kozačky z ovčí kůže', 'semiš nebo kůže, vlněná podšívka, plochá podešev', 'suchý mráz, chodníky bez břečky'],
              ['Dětské sněhule na suchý zip', 'široké otevírání, nižší hmotnost, reflexní prvky', 'školka, hřiště, kopec za domem']]) +
          '<h2>Jak sněhule vybrat podle toho, kde je budete nosit</h2>'
          '<p>Kdo jezdí na hory a tráví celé dny ve sněhu, potřebuje vysoký svršek, nepromokavou vanu a stahování u lýtka. Při procházkách s kočárkem nebo psem po zasněžené obci stačí nižší model, který se rychle obouvá. Pro město s rozbředlým sněhem a solí je důležitá hlavně nepromokavost spodní části a podrážka, která neklouže na mokré dlažbě. Krásná semišová bota bez úpravy tam rychle nasákne a na kůži zůstanou bílé mapy od soli.</p>'
          '<p>Na dlouhé zimní túry sněhule ideální nejsou. Mají měkčí podešev, menší oporu kotníku a víc váží, takže při delším stoupání nohy unaví. Pro zimní turistiku je lepší sáhnout po zateplených <a href="/vysoke-trekove-boty/">vysokých trekových botách</a>, případně je doplnit o <a href="/snezky/">sněžnice</a>, když leží hodně prašanu.</p>'
          '<h2>Zateplení a teplotní údaje</h2>'
          '<p>Někteří výrobci uvádějí u sněhulí teplotu, do které má bota hřát. Berte ji jako orientační vodítko: není to sjednocený údaj a každá značka ho určuje vlastním způsobem. Výsledek navíc hodně ovlivňuje, jestli stojíte, nebo se hýbete, jakou máte ponožku a zda je bota suchá. Při stání na místě, třeba u dětí na kopci, mrznou nohy rychleji než při chůzi.</p>'
          '<ul><li><strong>Vyjímatelná vložka</strong> se dá večer vytáhnout a vysušit zvlášť. Na vícedenních pobytech je to velká výhoda.</li>'
          '<li><strong>Syntetická izolace</strong> hřeje i při mírném navlhnutí a rychleji schne.</li>'
          '<li><strong>Ovčí vlna a kožíšek</strong> jsou příjemné na dotek a hřejí, ale na mokro se nehodí, pokud bota nemá nepromokavou vrstvu.</li>'
          '<li><strong>Tepelně izolační stélka</strong> omezuje chlad od podložky. Pokud ji bota nemá, dá se dokoupit mezi <a href="/vlozky-do-bot/">vložkami do bot</a>.</li></ul>'
          '<h2>Velikost: kolik místa nechat</h2>'
          '<p>Sněhule se nosí se silnější ponožkou, takže by v nich mělo zůstat trochu volného prostoru. Bota, která tlačí, hřeje hůř, protože stlačená izolace má méně vzduchu a krev do prstů proudí hůře. Příliš volná bota zase dře na patě a noha v ní klouže. Při zkoušení si vezměte ponožku, kterou budete opravdu nosit, a projděte se po místnosti. Prsty se mají volně hýbat a pata by se při chůzi neměla zvedat.</p>'
          '<p>Velikostní tabulky se mezi značkami liší a sněhule s vložkou bývají uvnitř menší, než by napovídalo číslo. Pomůže změřit délku chodidla od paty po nejdelší prst a porovnat ji s délkou stélky, kterou výrobce uvádí. U dětí se obvykle doporučuje rezerva zhruba jeden centimetr, aby bota vydržela celou zimu, ale nebyla tak velká, že by dítě zakopávalo.</p>'
          '<h2>Dámské, pánské a dětské sněhule</h2>'
          '<p>Dámské sněhule se nejčastěji hledají a nabídka je u nich nejpestřejší: od sportovních modelů s vanou po vyšší kozačky s kožíškem a boty na mírném klínu. Dámské střihy bývají užší v kotníku a lýtku, což je dobré mít na paměti při silnějším lýtku nebo při nošení zastrčených kalhot. Pánské modely mívají širší kopyto a robustnější podrážku. Porovnat můžete třeba <a href="/damske-zimni-boty/">dámské</a> a <a href="/panske-zimni-boty/">pánské zimní boty</a> v celé šíři kategorie.</p>'
          '<p>U <a href="/detske-zimni-boty/">dětských zimních bot</a> rozhoduje snadné obouvání. Suchý zip nebo rychlošněrování dítě zvládne samo i v rukavicích. Výhodou je široké otevírání v přední části a poutko na patě. Tmavší spodek skryje špínu z hřiště, reflexní prvky pomohou v prosincovém šeru.</p>'
          '<h2>Podrážka a protiskluz</h2>'
          '<p>Na ušlapaném sněhu a ledu rozhoduje směs i vzorek. Měkčí guma zůstává pružná i v mrazu a lépe se přimkne k nerovnostem, tvrdá podrážka v chladu ztuhne a klouže víc. Hluboké drážky s většími mezerami se méně zanášejí sněhem. Žádná běžná podrážka ale na hladkém ledu spolehlivě nedrží. Pokud chodíte po neposypaných cestách, vyplatí se mít v kapse <a href="/nesmeky/">nesmeky</a>, které se navléknou přes botu.</p>'
          '<h2>Péče o sněhule</h2>'
          '<ul><li>Po návratu vytáhněte vložku i stélku a nechte vše schnout při pokojové teplotě, ne přímo na radiátoru nebo u kamen.</li>'
          '<li>Sůl z chodníků otřete vlhkým hadříkem ještě týž den, jinak na kůži a semiši zanechá skvrny.</li>'
          '<li>Svršek z textilu, kůže či semiše jednou za čas ošetřete vhodným přípravkem z kategorie <a href="/impregnace/">impregnace</a>.</li>'
          '<li>Na jaře boty vyčistěte, vysušte a uložte vycpané papírem, aby si držely tvar.</li>'
          '<li>Gumovou vanu kontrolujte v místě, kde se ohýbá. Prasklina se tam objevuje nejdřív.</li></ul>'
          '<h2>Materiál svršku</h2>'
          '<p>Nylonový nebo polyesterový svršek je lehký, snese hrubší zacházení a rychle se otře. Často bývá povrchově upravený proti vodě, ta úprava ale časem slábne a je potřeba ji obnovovat. Kůže je odolná a hezky stárne, potřebuje však krém nebo vosk, jinak v mokru tmavne a po vyschnutí tvrdne. Semiš a nubuk vypadají elegantně, jenže vodu i sůl snášejí nejhůř ze všech. Textil s vnitřní membránou je kompromis: zvenku vypadá jako běžná bota, uvnitř drží vodu venku a přitom pustí ven část vlhkosti z nohy.</p>'
          '<p>Ovčí kůže s vlnou uvnitř je samostatná kapitola. Hřeje příjemně a dobře se v ní chodí naboso, ale do břečky a na posolené chodníky se bez impregnace nehodí. Kozačky tohoto typu nosí lidé hlavně v suchém mrazu a na krátké cesty, na sníh po kolena patří spíš klasická sněhule s gumovou vanou.</p>'
          '<h2>Zapínání a stahování</h2>'
          '<p>Šněrování umožní botu dotáhnout přesně podle nártu, v mrazu a v rukavicích se ale zavazuje špatně. Rychlošněrování se stopkou nebo kolečkem se utáhne jedním pohybem. Suchý zip je nejrychlejší, s věkem boty ale ztrácí přilnavost, hlavně když se do něj nabalí sníh a chlupy. Zipy po straně usnadňují obouvání u vysokých modelů, jejich slabinou je místo, kde může protéct voda, pokud zip nemá krycí légu. U vysokých sněhulí ověřte, že horní okraj jde stáhnout kolem lýtka nebo kalhot, jinak se do boty při brodění nabírá sníh.</p>'
          '<h2>Kdy sněhule vybírat</h2>'
          '<p>Poptávka roste s prvními mrazy a vrcholí kolem Vánoc a jarních prázdnin. Tehdy se nejrychleji vyprodávají běžná čísla. Kdo vybírá už na podzim, má větší jistotu, že najde svou velikost i barvu. Dětské boty je lepší kupovat až těsně před zimou, protože noha mezitím může povyrůst. Na Sportece uvidíte u každého páru, ve kterých obchodech je vaše číslo právě nabízené.</p>'
          '<h2>Hmotnost a pohodlí při chůzi</h2>'
          '<p>Objemná sněhule s gumovou vanou a silnou vložkou je těžší než běžná zimní bota. Na kopci se to neprojeví, na procházce s kočárkem po rozbředlých chodnících ale ano. Pokud víte, že budete hodně chodit, zkuste lehčí model s membránou a pružnější podrážkou, který se při kroku ohýbá v přední části. Vysoký tuhý svršek může tlačit na holeň, hlavně když boty nosíte s tenkými kalhotami. Rozdíl ucítíte už při pár krocích po bytě, proto boty po doručení vyzkoušejte doma na koberci, dokud je lze bez problémů vrátit.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Semišové kozačky s kožíškem kupované do mokrého sněhu a břečky.</li>'
          '<li>Sněhule těsné na doraz, bez místa pro teplejší ponožku.</li>'
          '<li>Bavlněné ponožky, které nasáknou potem a noha v nich vychladne.</li>'
          '<li>Sušení na topení, po kterém guma ztvrdne a kůže popraská.</li>'
          '<li>Dlouhé zimní výlety ve sněhulích místo turistických bot.</li></ul>'
          '<p>Teplou vrstvu na nohou doplní <a href="/lyzarske-ponozky/">lyžařské ponožky</a> nebo <a href="/merino-ponozky/">merino ponožky</a>. Kdo hledá zimní obuv s co nejtenčí podrážkou, najde zateplené modely i mezi <a href="/barefoot-obuv/">barefoot botami</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi sněhulemi a zimními botami?', 'Sněhule jsou vyšší, objemnější a mají nepromokavou spodní část určenou do hlubokého sněhu. Běžné zimní boty jsou nižší, lehčí a lépe se v nich chodí po městě.'),
        ('Jsou sněhule nepromokavé?', 'Spodní gumová vana ano, u svršku záleží na materiálu a švech. Textilní horní část bez membrány může při dlouhém brodění v mokrém sněhu navlhnout.'),
        ('O kolik větší sněhule koupit?', 'Tak, aby se v nich s teplou ponožkou volně hýbaly prsty a pata se nezvedala. U dětí se nechává rezerva zhruba jeden centimetr.'),
        ('Co znamená teplota uvedená u sněhulí?', 'Je to odhad výrobce, do jakých mrazů bota hřeje. Není sjednocený mezi značkami a hodně záleží na tom, jestli se hýbete, nebo stojíte.'),
        ('Jak usušit sněhule?', 'Vytáhněte vložku a stélku, boty vycpěte papírem a nechte schnout při pokojové teplotě. Přímé teplo z topení škodí gumě i kůži.'),
        ('Hodí se sněhule na zimní túry?', 'Na krátké procházky ano, na dlouhé výstupy méně. Mají měkkou podešev a menší oporu kotníku, pro túry jsou vhodnější zateplené trekové boty.'),
        ('Proč mi ve sněhulích mrznou nohy?', 'Nejčastěji kvůli vlhku z potu, těsné botě nebo bavlněné ponožce. Pomůže suchá vložka, volnější velikost a ponožka z vlny nebo syntetiky.'),
        ('Hodí se sněhule do města?', 'Na zasněžené a rozbředlé chodníky ano, hlavně lehčí modely s membránou. Na suchou dlažbu jsou zbytečně těžké a objemné.'),
        ('Kde sněhule koupit?', 'Na Sportece porovnáte nabídky českých e-shopů u každého páru včetně dostupných velikostí. Objednávku dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ cargo-kalhoty
NEW['cargo-kalhoty'] = dict(long=True,
    title='Cargo kalhoty a kapsáče: outdoorové i volnočasové',
    desc='Pánské a dámské cargo kalhoty, outdoorové kapsáče i cargo tepláky. Jak vybrat materiál, střih a kapsy a kde nabídky porovnat napříč českými e-shopy.',
    intro='<p><strong>Cargo kalhoty</strong>, u nás často prostě <strong>kapsáče</strong>, poznáte podle velkých kapes na stehnech. Původně šlo o pracovní a vojenský střih, kde se do kapes vešla mapa, obvaz nebo nářadí. Dnes se nosí na výlety, na chatu, do města i na trénink, protože kapsy jsou prostě praktické. Vedle pevných outdoorových kalhot z odolné tkaniny sem patří lehké letní kapsáče, cargo tepláky se stahovacím lemem a dámské střihy s vyšším pasem.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů, takže u konkrétního modelu vidíte, kde ho mají a v jakých velikostech. Kalhoty si pak objednáte v obchodě, který vám vyhovuje. Najdete tu outdoorové kapsáče značek '
          + B(('fjallraven', 'Fjällräven'), ('helly-hansen', 'Helly Hansen')) +
          ' i sportovní cargo tepláky od '
          + B(('nike', 'Nike'), ('under-armour', 'Under Armour')) +
          '. Kategorie patří pod <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>',
    guide='<h2>Tři skupiny cargo kalhot</h2>'
          '<p>Pod jedním názvem se schovávají kalhoty s dost odlišným určením. Outdoorové kapsáče jsou šité z pevné tkaniny, mají zesílená místa a počítají s lezením přes kameny i s trním. Volnočasové cargo kalhoty jsou měkčí, bývají z bavlněného kepru a slouží hlavně na běžné nošení. Cargo tepláky a joggery vycházejí ze sportovního úpletu, mají gumu v pase a stažené nohavice, kapsy na stehnech jsou spíš doplněk střihu.</p>'
          + T(['Skupina', 'Typický materiál', 'Kdy sáhnout'], [
              ['Outdoorové kapsáče', 'směs polyesteru a bavlny, polyamid, ripstop, softshell', 'turistika, chata, práce na zahradě, cesty'],
              ['Volnočasové cargo', 'bavlněný kepr, plátno, směs s elastanem', 'město, víkendy, cestování'],
              ['Cargo tepláky a joggery', 'bavlněný nebo polyesterový úplet, fleece', 'trénink, cesta na hřiště, domov'],
              ['Odepínací kapsáče 2 v 1', 'lehká syntetika, zipy nad kolenem', 'léto na horách, cesty s malým zavazadlem'],
              ['Zateplené cargo', 'tkanina s podšívkou nebo počesaným rubem', 'zimní procházky, práce venku v chladu']]) +
          '<h2>Materiál: co vydrží a co rychle schne</h2>'
          '<p>Pro outdoor je dobrá hustá tkanina ze směsi syntetiky a bavlny. Syntetika přidává pevnost a rychlejší schnutí, bavlna příjemný dotek a menší šustění. Některé tkaniny se napouštějí voskem, který zvyšuje odolnost proti větru a lehkému dešti. Typickým příkladem je materiál G-1000 od Fjällräven, který se po vyprání znovu voskuje. Ripstop poznáte podle drobné mřížky. Zesílená vlákna v ní zastaví roztržení, takže malá dírka se dál nešíří.</p>'
          '<p>Čistě bavlněné kapsáče jsou příjemné na každý den, ale v dešti nasáknou a schnou pomalu, takže na celodenní túru v proměnlivém počasí se moc nehodí. Lehké polyamidové kalhoty naopak uschnou za chvíli, jenže víc šustí a v létě na přímém slunci mohou hřát. Elastan přidaný do tkaniny zlepší volnost v kolenou a při lezení do schodů. Pro chladné měsíce existují i <a href="/softshellove-kalhoty/">softshellové kalhoty</a> s kapsami na stehnech.</p>'
          '<h2>Na co se dívat u střihu</h2>'
          '<ul><li><strong>Předtvarovaná kolena</strong> umožní dřep a výstup do svahu bez toho, aby látka táhla.</li>'
          '<li><strong>Klínek v rozkroku</strong> přidává prostor při velkém kroku a snižuje napětí ve švech.</li>'
          '<li><strong>Zesílení</strong> na kolenou, sedu a lemech nohavic prodlužuje životnost v terénu.</li>'
          '<li><strong>Stahování u kotníku</strong> šňůrkou nebo patentem udrží nohavici nad botou a nepouští dovnitř klíšťata ani sníh.</li>'
          '<li><strong>Pás</strong> s poutky na opasek, gumou v bocích nebo integrovaným páskem. Na turistiku s batohem je příjemný plochý pás bez tlustých švů.</li></ul>'
          '<p>Kapsy samy o sobě nestačí, záleží na tom, jak jsou udělané. Kapsa s měchem se rozšíří a pojme i telefon nebo mapu, plochá našitá kapsa je spíš ozdoba. Zip drží obsah lépe než suchý zip, ten zase jde otevřít jednou rukou. Když v kapse nosíte telefon, hodí se, aby byla dostatečně hluboká a umístěná na boku stehna, ne vpředu, kde by při chůzi tlačila.</p>'
          '<h2>Pánské a dámské cargo kalhoty</h2>'
          '<p>Pánské kapsáče mají rovnější nohavici a delší rozkrok, nabídka je u nich nejširší. Dámské cargo kalhoty bývají v pase užší a v bocích prostornější, často s vyšším pasem a s volnějšími nohavicemi. Ve městě se nosí dámské cargo i v širokém střihu s rovnými nohavicemi, na turistiku jsou praktičtější užší modely, které se nezachytávají o větve. Pokud nevíte, jak střih padne, porovnejte obvod pasu a délku vnitřního švu s kalhotami, které už doma máte.</p>'
          '<h2>Velikost a délka nohavic</h2>'
          '<p>Kromě obvodu pasu rozhoduje délka. Výrobci ji uvádějí jako délku vnitřního švu nebo jako zkrácenou a prodlouženou variantu. Kalhoty na turistiku by měly zakrýt vršek boty i při kroku do schodu. Moc dlouhé nohavice se ale prošlapou o podrážku a rychle se roztřepí. Cargo tepláky se stahovacím lemem jsou v délce tolerantnější, protože guma drží nohavici u kotníku.</p>'
          '<h2>Cargo tepláky a joggery</h2>'
          '<p>Sportovní značky dělají cargo střih i z úpletu. Výsledek je pohodlný jako <a href="/teplaky/">tepláky</a>, ale do kapsy na stehně se vejde telefon nebo klíče. Hodí se na cestu do posilovny, na rozcvičení a na volný den. Na turistiku v dešti se úplet nehodí, protože vodu nasaje a dlouho schne. Pro tyto situace jsou vhodnější <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> z tkaniny.</p>'
          '<h2>Péče a praní</h2>'
          '<ul><li>Před praním vyprázdněte kapsy, zapněte zipy i suché zipy a kalhoty obraťte naruby.</li>'
          '<li>Perte podle visačky, obvykle na nižší teplotu, aby se směsová tkanina nesrazila.</li>'
          '<li>Aviváž u funkčních a voskovaných tkanin vynechejte, zhoršuje odpudivost vody.</li>'
          '<li>Voskované kalhoty po vyprání znovu navoskujte a vosk zažehlete nebo nahřejte fénem podle návodu výrobce.</li>'
          '<li>Úplné odpuzování vody obnoví sprej z kategorie <a href="/impregnace/">impregnace</a>.</li></ul>'
          '<h2>Odepínací nohavice a zkrácené délky</h2>'
          '<p>Kapsáče 2 v 1 mají nad kolenem zip, po jehož rozepnutí se z kalhot stanou kraťasy. Na horách se to hodí, když ráno mrzne a odpoledne svítí slunce. Zip bývá barevně odlišený, aby se nohavice nepletly, a u dobrých modelů jde nohavici odepnout i přes botu. Nevýhodou je o něco vyšší hmotnost a šev přes stehno, který u některých lidí může třít. Kdo chodí hlavně v létě, může zvážit tříčtvrteční cargo délku, která kryje kolena a nechává volné lýtko.</p>'
          '<h2>Kapsáče na chatu, zahradu a práci</h2>'
          '<p>Na práci se hodí kapsáče s hustší tkaninou a zesílením na kolenou. Některé pracovní modely mají na kolenou kapsy pro vkládací chrániče, což ocení každý, kdo pokládá dlažbu nebo pracuje na zahradě vkleče. Poutka na kladivo a kapsy na metr jsou typické spíš pro pracovní oděvy než pro outdoor, i tady ale platí, že těžké nářadí se lépe nosí v opasku než v kapse na stehně. Tmavé barvy skryjí špínu, světlé khaki je zase v létě chladnější.</p>'
          '<h2>Kapsy na cesty</h2>'
          '<p>Na cestování se vyplatí kalhoty s alespoň jednou kapsou na zip, ideálně skrytou nebo umístěnou tak, aby se do ní nedalo nepozorovaně sáhnout. Doklady a peněženka jsou v ní bezpečnější než v zadní kapse. Lehká syntetická tkanina se dá v hotelu vyprat v umyvadle a do rána uschne. Kalhoty, které se příliš nemačkají, vypadají slušně i po celém dni v letadle nebo autobusu. Pokud kalhoty nosíte s batohem, zkuste, zda bederní pás netlačí na přezky nebo nýty v pase.</p>'
          '<h2>Barvy a vzory</h2>'
          '<p>Klasické barvy jsou olivová, khaki, písková a černá. Do přírody, kde nechcete rušit zvěř, se hodí tlumené zemité odstíny, maskovací vzory jsou spíš doménou myslivců a najdete je v kategorii <a href="/lovecke-obleceni/">lovecké oblečení</a>. Ve městě se cargo kalhoty nosí i v béžové, šedé nebo tmavě modré. Pokud chcete jedny kalhoty na všechno, tmavší neutrální barva se nejsnáz kombinuje a méně na ní vynikne špína z cesty.</p>'
          '<h2>Jak kalhoty vyzkoušet po doručení</h2>'
          '<p>Doma si kalhoty oblékněte s botami, ve kterých je budete nosit. Udělejte hluboký dřep, vykročte na židli a zkuste si sednout se zkříženýma nohama. Látka by neměla táhnout přes kolena ani se zařezávat do rozkroku. Do kapes dejte telefon a klíče a projděte se po bytě, ať víte, zda vám obsah nebude bouchat do stehen. Visačky nechte na místě, dokud si nejste jisti, abyste mohli kalhoty v obchodě případně vrátit nebo vyměnit za jinou velikost.</p>'
          '<h2>Opasek, nebo guma v pase</h2>'
          '<p>Outdoorové kapsáče mají často kombinaci poutek a pružného pásu v bocích, takže drží i bez opasku a snesou drobné změny postavy. Klasický opasek s velkou kovovou přezkou může pod bederním pásem batohu tlačit, plochý textilní pásek je pohodlnější. Cargo tepláky spoléhají na gumu se šňůrkou, ta by měla být široká a neměla by se při nošení stáčet.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Bavlněné kapsáče na vícedenní túru, kde se dá čekat déšť.</li>'
          '<li>Kapsy přecpané těžkými věcmi, které při chůzi bouchají do stehen.</li>'
          '<li>Volné nohavice do lesa s klíšťaty a do kosodřeviny.</li>'
          '<li>Praní s aviváží a sušení v sušičce u kalhot, kterým to výrobce nedoporučuje.</li></ul>'
          '<p>Na léto se hodí <a href="/sportovni-kratasy/">kraťasy</a>, k turistickému oblečení pak <a href="/kosile/">outdoorové košile</a> a pohodlné <a href="/trekova-obuv/">trekové boty</a>.</p>',
    faq=[
        ('Co jsou kapsáče?', 'Hovorový název pro cargo kalhoty, tedy kalhoty s velkými kapsami na stehnech. Nosí se na turistiku, na práci venku i na běžné nošení.'),
        ('Jaký materiál vybrat na turistiku?', 'Pevnou tkaninu ze syntetiky nebo směsi syntetiky s bavlnou, ideálně s příměsí elastanu. Čistá bavlna v dešti nasákne a pomalu schne.'),
        ('Jsou cargo kalhoty nepromokavé?', 'Běžně ne. Voskovaná nebo impregnovaná tkanina odpudí lehký déšť, na vytrvalý déšť je potřeba nepromokavá vrstva přes kalhoty.'),
        ('Jak dlouhé mají kapsáče být?', 'Při stání mají zakrýt vršek boty a nevláčet se po zemi. Délku vnitřního švu porovnejte s kalhotami, které vám sedí.'),
        ('Čím se liší cargo tepláky od kapsáčů?', 'Cargo tepláky jsou z úpletu, mají gumu v pase a stažené nohavice. Kapsáče jsou z tkaniny, pevnější a lépe snášejí terén.'),
        ('Jak prát voskované kalhoty?', 'Podle visačky a bez aviváže. Po vyprání je výrobci obvykle doporučují znovu navoskovat, aby se obnovila odolnost proti vodě a větru.'),
        ('Hodí se kapsáče pro ženy?', 'Ano, dámské cargo kalhoty mají střih přizpůsobený pasu a bokům. Ve městě se nosí širší, na túry užší modely.'),
        ('Mají kapsáče na kolenou kapsy na chrániče?', 'Jen některé pracovní modely. Do kapes se vkládají měkké chrániče, které ocení každý, kdo pracuje vkleče.'),
        ('Jsou cargo kalhoty vhodné na cesty?', 'Ano, hlavně lehké syntetické modely s kapsou na zip. Rychle schnou, málo se mačkají a doklady v nich nosíte bezpečněji.'),
        ('Kde cargo kalhoty porovnat?', 'Sporteka zobrazí u každého modelu nabídky českých e-shopů a dostupné velikosti. Kalhoty pak koupíte přímo v obchodě, který si zvolíte.'),
    ])

# ------------------------------------------------------------------ zateplene-leginy
NEW['zateplene-leginy'] = dict(long=True,
    title='Zateplené a termo legíny na běh, lyže i do zimy',
    desc='Zateplené legíny s počesaným rubem, termo legíny jako spodní vrstva i běžecké zimní legíny. Jak vybrat materiál a velikost a kde nabídky porovnat.',
    intro='<p><strong>Zateplené legíny</strong> mají na vnitřní straně počesaný, mírně chlupatý povrch, který drží teplý vzduch u těla. <strong>Termo legíny</strong> se obvykle myslí jako funkční spodní vrstva pod lyžařské nebo turistické kalhoty. Obě skupiny se ale prolínají: běžecké zimní legíny se nosí samostatně, tenké termo legíny zase pod kalhoty do práce i na běžky. Výběr se řídí tím, jestli se budete hodně hýbat, nebo spíš stát venku, a jestli legíny budou vnější, nebo spodní vrstva.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů u jednotlivých legín a nakoupíte pak v obchodě, který si vyberete. V nabídce jsou například '
          + B(('litex', 'Litex'), ('dynafit', 'Dynafit')) +
          ', Salewa, Klimatex nebo Swix. Kategorie spadá pod <a href="/leginy/">legíny</a>, celé spodní vrstvy najdete ve <a href="/termopradlo/">funkčním a termo prádle</a>.</p>',
    guide='<h2>Zateplené, nebo termo: v čem je rozdíl</h2>'
          '<p>Rozdíl není v názvu, ale v tom, jak legíny pracují. Zateplené legíny jsou vnější vrstva. Mají hustší úplet, počesaný vnitřek a někdy i větruodolné panely vpředu na stehnech. Nosí se samy, třeba na zimní běh, na procházku se psem nebo pod sukni. Termo legíny jsou tenčí a přiléhavější, odvádějí pot od kůže a hřejí hlavně tím, že kůže zůstává suchá. Patří pod další vrstvu, ať jsou to <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, softshell, nebo obyčejné džíny.</p>'
          + T(['Typ', 'Jak hřeje', 'Použití'], [
              ['Termo legíny jako spodní vrstva', 'odvádí vlhkost, tenká vrstva vzduchu u kůže', 'pod lyžařské a turistické kalhoty'],
              ['Běžecké zimní legíny', 'počesaný rub, někdy větruodolná přední část', 'zimní běh, běžky, jízda na kole v chladu'],
              ['Legíny s fleecem či kožíškem', 'silný chlupatý vnitřek', 'procházky, nošení do města, pod šaty'],
              ['Merino legíny', 'vlna hřeje i ve vlhku a méně zapáchá', 'vícedenní túry, skialpy, pomalý pohyb v chladu'],
              ['Legíny se zipem u kotníku', 'těsný střih, snadné obouvání', 'běh a běžky s vyšší botou']]) +
          '<h2>Materiály</h2>'
          '<p><strong>Polyester a polypropylen</strong> téměř nesají vodu a pot rychle posílají dál. Hodí se na intenzivní pohyb, kdy se hodně zpotíte. Jejich slabinou je pach, který se v syntetice drží déle. <strong>Polyamid s elastanem</strong> je pevný a hladký, takže legíny dobře drží tvar a méně se žmolkují. Počesaná varianta tohoto materiálu se v cyklistice nazývá Roubaix a stejnou konstrukci mají i mnohé běžecké zimní legíny.</p>'
          '<p><strong>Merino vlna</strong> hřeje i ve chvíli, kdy navlhne, a pach v ní vzniká pomaleji, proto ji ocení každý, kdo legíny nosí několik dní za sebou. Je ale choulostivější na otěr a dražší. Často se proto kombinuje se syntetikou, která přidá pevnost. Čistě merino kousky najdete v kategorii <a href="/merino-pradlo/">merino spodní prádlo a legíny</a>. <strong>Bavlna</strong> do zateplených sportovních legín nepatří: nasákne potem a pak chladí.</p>'
          '<h2>Gramáž a tloušťka</h2>'
          '<p>U termo prádla výrobci často uvádějí gramáž, tedy hmotnost látky na metr čtvereční. Čím vyšší číslo, tím silnější a teplejší úplet. Tenká vrstva se hodí na intenzivní pohyb, kdy se tělo zahřeje samo, silnější na pomalejší aktivity a stání. Pro sjezdové lyžování s dlouhým sezením na lanovce si lidé obvykle berou teplejší variantu než na běžky, kde se zahřejí do pár minut. Každý ale snáší chlad jinak, takže je dobré vycházet z vlastní zkušenosti.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Termo legíny mají sedět těsně, ale neškrtit. Volná spodní vrstva neodvádí pot, protože se kůže nedotýká, a vzduch pod ní proudí. Zateplené legíny na běh mohou být o něco volnější, pořád ale přiléhavé, aby se nehrnuly u kolen. Zkontrolujte délku: na běh se hodí nohavice ke kotníku, pod lyžařskou botu musí končit nad jejím okrajem nebo se do ní hladce zasunout bez zmačkaných záhybů, které by tlačily.</p>'
          '<ul><li><strong>Vyšší pas</strong> nesjíždí při předklonu a kryje bedra.</li>'
          '<li><strong>Ploché švy</strong> netlačí pod další vrstvou a v lyžařské botě.</li>'
          '<li><strong>Kapsa na zádech nebo v pase</strong> se hodí na klíče a gel při běhu.</li>'
          '<li><strong>Reflexní prvky</strong> jsou užitečné, protože v zimě se běhá často za tmy.</li></ul>'
          '<h2>Dámské, pánské a dětské termo legíny</h2>'
          '<p>Dámské zateplené legíny jsou nejhledanější skupinou. Kromě sportovních modelů sem patří i měkké legíny s kožíškem na běžné nošení, které nahrazují punčocháče v zimě. Pánské termo legíny se častěji prodávají jako spodky k termo prádlu, v nabídce jsou ale i běžecké zimní modely. U dětí se termo legíny nosí pod kombinézu nebo zimní kalhoty, na lyžáku i na sáňkování. Celou nabídku pro děti najdete v <a href="/detske-termopradlo/">dětském termoprádle</a>, na sjezdovku se hodí <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>.</p>'
          '<h2>Vrstvení v praxi</h2>'
          '<p>Na zimní běh obvykle stačí jedny zateplené legíny, při silném větru nebo mrazu lze přidat lehké větruodolné kalhoty. Na sjezdovku patří termo legíny jako první vrstva a přes ně lyžařské kalhoty. Na skialpy a dlouhé túry se osvědčuje tenčí spodní vrstva, protože při výstupu se zahřejete a teplo se snáz ubere sundáním svrchní vrstvy. Do města si můžete vzít tenké termo legíny pod kalhoty, které se pod látkou neprokreslí.</p>'
          '<h2>Péče a praní</h2>'
          '<ul><li>Perte na teplotu uvedenou na visačce, funkční materiály obvykle snesou mírné teploty.</li>'
          '<li>Nepoužívejte aviváž, ucpává vlákna a legíny pak hůř odvádějí vlhkost.</li>'
          '<li>Merino perte na vlnu nebo v ruce s jemným prostředkem a sušte naplocho.</li>'
          '<li>Počesaný vnitřek nesušte na topení ani v sušičce, pokud to výrobce nepovoluje.</li>'
          '<li>Legíny obraťte naruby, ochráníte tím vnější stranu před žmolky.</li></ul>'
          '<h2>Větruodolné panely a nohavice se zipem</h2>'
          '<p>Při běhu nebo na běžkách proti větru chladnou nejvíc stehna a kolena. Proto mají některé zimní legíny vpředu vsazené panely z tkaniny, která vítr zastaví, zatímco zadní strana zůstává prodyšná. Ve větru je rozdíl znát hned, při bezvětří a vyšším tempu se v nich ale člověk zpotí rychleji. Zip u kotníku usnadní obouvání a sundávání přes běžeckou botu. Na zádech nebo v pase bývá malá kapsa na klíče, jen se ujistěte, že se v ní telefon při běhu nehoupe.</p>'
          '<h2>Legíny na běžky a skialpy</h2>'
          '<p>Na běžkách se tělo zahřeje rychle a pot je potřeba odvést, ne zadržet. Proto se tu nosí spíš tenčí zateplené legíny nebo kombinace termo legín a lehkých kalhot, které se dají sundat. Skialpinisté vrství podobně: při výstupu jdou často jen v tenké spodní vrstvě a softshellu, při sjezdu přidávají. Značky zaměřené na běžky a skialpy, například Swix nebo Dynafit, mají v nabídce legíny přímo pro tyto sporty. Více výbavy najdete v sekcích <a href="/bezecke-lyzovani/">běžecké lyžování</a> a <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h2>Legíny s kožíškem do města</h2>'
          '<p>Silné legíny s chlupatým vnitřkem se nosí jako teplejší náhrada punčocháčů pod šaty, sukni nebo dlouhý svetr. Existují i varianty v tělové barvě, které zvenku připomínají silonky a zevnitř mají fleece. Na sport se většinou nehodí, protože odvádějí pot hůř a v pohybu jsou příliš teplé. Při nákupu sledujte hlavně pružnost v pase a to, zda se látka při natažení přes koleno neprosvítá.</p>'
          '<h2>Jak poznat dobře ušité legíny</h2>'
          '<ul><li>Klínek v rozkroku zabrání tomu, aby se švy sbíhaly do jednoho bodu a dřely.</li>'
          '<li>Při předklonu se látka nemá prosvítat ani na sedu.</li>'
          '<li>Gumu v pase by mělo jít mírně roztáhnout, aniž by se na ní dělaly vlnky.</li>'
          '<li>Švy na vnitřní straně stehen mají být ploché, jinak při běhu odírají.</li>'
          '<li>Počesaný vnitřek má být rovnoměrný, bez míst, kde je úplet zjevně tenčí.</li></ul>'
          '<h2>Zápach a nošení více dní</h2>'
          '<p>Syntetické legíny po tréninku vyperte co nejdřív, pach se v nich jinak usadí. Pokud jste na horách a pračka není po ruce, je praktičtější merino, které se dá vyvětrat a nosit znovu. Část syntetických legín má antibakteriální úpravu, která vznik pachu omezuje. Ani ta ale nenahradí praní a časem slábne.</p>'
          '<h2>Viditelnost a barvy</h2>'
          '<p>V zimě se často běhá před svítáním nebo po setmění. Černé legíny jsou praktické, protože na nich není vidět špína od rozbředlého sněhu, řidič vás v nich ale uvidí pozdě. Reflexní potisk na lýtkách se při běhu hýbe a upoutá pozornost lépe než reflexní prvek na trupu. Kdo běhá podél silnic, může legíny doplnit o <a href="/reflexni-vesty/">reflexní vestu</a> nebo čelovku.</p>'
          '<h2>Kdy zateplené legíny kupovat</h2>'
          '<p>Zájem o ně stoupá s prvními mrazy na podzim a drží se až do konce zimy. Na začátku sezóny je výběr velikostí a barev největší. Ke konci zimy se dají najít výprodeje, jenže nejběžnější velikosti v té době často chybějí. Sporteka u každého modelu ukazuje, které obchody ho mají v nabídce, takže hned vidíte, kde je vaše velikost.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Bavlněné legíny jako spodní vrstva na lyže.</li>'
          '<li>Moc teplé legíny na intenzivní běh, ve kterých se člověk propotí a pak prochladne.</li>'
          '<li>Spodní vrstva o velikost větší, která se pod kalhotami shrnuje.</li>'
          '<li>Volný pas, který při každém kroku sjíždí.</li></ul>'
          '<p>K zimnímu běhu se hodí také <a href="/funkcni-tricka/">funkční trička</a>, <a href="/sportovni-rukavice/">rukavice</a> a <a href="/kompresni-ponozky/">kompresní ponožky</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi zateplenými a termo legínami?', 'Zateplené legíny jsou silnější vnější vrstva s počesaným vnitřkem. Termo legíny jsou tenčí spodní vrstva, která odvádí pot a nosí se pod další kalhoty.'),
        ('Hodí se zateplené legíny na běh v zimě?', 'Ano, běžecké zimní legíny jsou na to stavěné. Při silném větru nebo mrazu se přes ně dá přidat lehká větruodolná vrstva.'),
        ('Jaké termo legíny pod lyžařské kalhoty?', 'Přiléhavé, z funkčního materiálu nebo merina, s plochými švy. Délkou by neměly vytvářet záhyby v lyžařské botě.'),
        ('Mají termo legíny sedět těsně?', 'Ano, spodní vrstva má přiléhat ke kůži, jinak pot neodvádí. Neměla by ale škrtit v pase ani u kotníků.'),
        ('Je lepší merino, nebo syntetika?', 'Merino hřeje i ve vlhku a méně zapáchá, syntetika rychleji schne a je odolnější. Hodně legín kombinuje obojí.'),
        ('Proč nepoužívat aviváž?', 'Aviváž zanechává na vláknech film, který zhoršuje odvod vlhkosti. Funkční legíny pak přestanou dobře pracovat.'),
        ('Co jsou legíny s kožíškem?', 'Legíny se silným chlupatým vnitřkem určené hlavně na procházky a běžné nošení v zimě. Na intenzivní sport jsou většinou příliš teplé.'),
        ('Jaké legíny na běžky?', 'Spíš tenčí zateplené legíny nebo termo vrstvu s lehkými kalhotami přes ni. Na běžkách se rychle zahřejete a pot je potřeba odvádět.'),
        ('Kde koupit termo legíny?', 'Sporteka u každého kusu ukáže nabídky českých e-shopů a dostupné velikosti. Nákup pak proběhne v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ vlozky-do-bot
NEW['vlozky-do-bot'] = dict(long=True,
    title='Vložky do bot: gelové, zimní, vyhřívané i sportovní',
    desc='Vložky a stélky do bot: gelové, pěnové, zimní vlněné, vyhřívané a sportovní. Jak vybrat velikost a typ a kde porovnat nabídky českých e-shopů.',
    intro='<p><strong>Vložky do bot</strong> nahrazují nebo doplňují stélku, která je v botě z výroby. Mohou přidat tlumení, zlepšit pocit z chůze, zahřát nohu v zimě nebo vyplnit botu, která je trochu volná. Liší se tvarem, tloušťkou a materiálem: od tenkých vlněných stélek přes gelové a pěnové vložky po sportovní stélky s tvarovanou patou a vyhřívané modely s baterií. Nejde o zdravotnickou pomůcku na míru, to je jiná kategorie, o které rozhoduje lékař.</p>'
          '<p>Sporteka ukazuje nabídky českých e-shopů vedle sebe, takže u každé vložky vidíte, kde ji prodávají a v jakých velikostech. Objednávku dokončíte v obchodě, který vám nejvíc vyhovuje. Mezi značkami jsou Svorto, Footgel, Sidas, Pedag nebo Be Lenka. Kategorie patří do skupiny <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>',
    guide='<h2>Druhy vložek a k čemu slouží</h2>'
          '<p>Než začnete vybírat, ujasněte si, co od vložky čekáte. Jiná se hodí do zimních bot, jiná do běžeckých a jiná do pracovní obuvi, ve které stojíte celý den. Tabulka ukazuje hlavní skupiny, se kterými se v nabídce setkáte.</p>'
          + T(['Druh vložky', 'Materiál', 'K čemu se používá'], [
              ['Gelové', 'silikonový nebo polymerový gel, často jen pod patou a přední částí', 'tlumení nárazů při chůzi po tvrdém povrchu'],
              ['Pěnové a paměťové', 'PU pěna, paměťová pěna, EVA', 'měkčí došlap, vyplnění volnější boty'],
              ['Zimní a vlněné', 'ovčí vlna, plsť, hliníková fólie', 'izolace od studené podložky'],
              ['Vyhřívané', 'topné vlákno a baterie, někdy dálkové ovládání', 'stání v mrazu, lov, rybaření, stavba'],
              ['Sportovní tvarované', 'tužší pata, tvarovaná podpora klenby', 'běh, turistika, lyžařské boty'],
              ['Tepelně tvarovatelné', 'materiál, který se po zahřátí přizpůsobí chodidlu', 'lyžařská a treková obuv'],
              ['Korkové a kožené', 'korek, usňová kůže', 'domácí a vycházková obuv, sandály']]) +
          '<h2>Ortopedické vložky: kdy patří k lékaři</h2>'
          '<p>Slovo ortopedické se v nabídce objevuje často, sériová vložka z obchodu ale není ortopedická pomůcka vyrobená podle vaší nohy. Pokud vás nohy dlouhodobě bolí nebo máte potíže s klenbou, kotníky, koleny či zády, obraťte se na ortopeda nebo podiatra. Ten posoudí, zda vložku potřebujete a jakou. Vložky vyrobené na zakázku podle lékařského předpisu jsou samostatná kategorie a zdravotní pojišťovna na ně za určitých podmínek přispívá, na sériové vložky z běžného prodeje nikoli. Vložky v této kategorii berte jako pomůcku pro pohodlí, ne jako řešení zdravotních potíží.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Většina vložek se prodává ve velikostech podle čísla bot, často v rozpětí dvou čísel. Na spodní straně bývají vyznačené linky, podle kterých se vložka ve špičce zastřihne nůžkami. Nejspolehlivější postup je vytáhnout původní stélku z boty, položit ji na novou vložku a obkreslit ji. Stříhejte raději po menších kouscích a průběžně zkoušejte, protože ustřižené už vrátit nejde.</p>'
          '<p>Myslete také na tloušťku. Silná zimní nebo gelová vložka zabere v botě místo, takže noha bude výš a v těsnější botě mohou začít tlačit prsty nebo se pata zvedat z opatku. Do bot, které sedí přesně, se proto hodí tenká vložka jako náhrada původní stélky, ne další vrstva navíc.</p>'
          '<h2>Vložky do zimních bot</h2>'
          '<p>Chlad do nohou z velké části proniká zespodu, ze zmrzlé země přes podrážku. Zimní vložka z ovčí vlny nebo plsti tuto cestu zpomalí a zároveň pohltí trochu vlhkosti. Některé mají na spodní straně hliníkovou fólii, která odráží teplo zpátky k noze. Vlněné vložky je dobré po každém nošení vytáhnout a vysušit, aby v nich nezůstávala vlhkost. Hodí se do <a href="/snehule/">sněhulí</a>, <a href="/holinky/">holínek</a> i zimních <a href="/barefoot-obuv/">barefoot bot</a>, kde nahradí tenkou stélku, aniž by ubraly pocit ze země.</p>'
          '<h2>Vyhřívané vložky</h2>'
          '<p>Vyhřívané vložky mají v sobě topné vlákno napájené baterií. Ta bývá zabudovaná v patě nebo připojená kabelem na vnější stranu boty. Teplota se nastavuje tlačítkem, aplikací nebo dálkovým ovladačem a výdrž závisí na zvoleném stupni a velikosti baterie. Hodí se lidem, kteří dlouho stojí nebo sedí v mrazu: rybářům, myslivcům, lyžařům na lanovce nebo divákům na stadionu. Při výběru zkontrolujte, jestli se vložka dá zastřihnout a kde přesně vede topný prvek, protože ten se stříhat nesmí. Vedle elektrických existují i jednorázové chemické ohřívače, které se po rozbalení samy zahřejí na vzduchu. Další vyhřívané doplňky jsou v kategorii <a href="/vyhrivane-obleceni/">vyhřívané oblečení a doplňky</a>.</p>'
          '<h2>Vložky do sportovní obuvi</h2>'
          '<p>Do <a href="/bezecka-obuv/">běžeckých bot</a> a <a href="/trekova-obuv/">trekové obuvi</a> se dávají vložky s pevnější patní miskou, které drží patu na místě a stabilizují došlap. U lyžařských bot jsou oblíbené tepelně tvarovatelné stélky, které se přizpůsobí chodidlu po zahřátí, často s pomocí odborníka v prodejně. Pokud vám ale bota sedí a nic vás netlačí, výměna stélky není nutná. Kdo zkouší novou vložku před závodem nebo dlouhou túrou, měl by ji nejdřív vyzkoušet na kratších vycházkách.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Vložky vytahujte a sušte mimo botu, zvlášť po dni v zimě nebo po tréninku.</li>'
          '<li>Pěnové a gelové stélky omyjte vlažnou vodou s mýdlem, do pračky je dávejte jen tehdy, když to výrobce dovoluje.</li>'
          '<li>Vlněné vložky nesušte na topení, vlna se může srazit a zkroutit.</li>'
          '<li>Stlačenou pěnu, která se už nevrací do původního tvaru, je čas vyměnit.</li>'
          '<li>Proti pachu pomůže pravidelné větrání bot, střídání dvou párů a deodorant do obuvi.</li></ul>'
          '<h2>Podpatěnky, polovložky a vložky do společenské obuvi</h2>'
          '<p>Ne každá vložka zabírá celou délku boty. Gelové podpatěnky se lepí do zadní části a zmírňují tvrdý došlap na patu. Polovložky pod přední část chodidla se dávají do lodiček a bot na podpatku, kde se váha přesouvá dopředu. Samolepicí pásky za patu zase pomohou u bot, ze kterých noha vyklouzává. Tyto drobnosti zaberou málo místa, takže se vejdou i do obuvi, kde by celá vložka byla příliš silná.</p>'
          '<h2>Barefoot obuv a tenké stélky</h2>'
          '<p>Barefoot boty mají tenkou podrážku a nechávají chodidlu volnost. Silná tvarovaná vložka by jejich smysl popřela, proto se do nich dávají hlavně tenké ploché stélky. V zimě to bývá vlna nebo plsť, které přidají teplo, ale nezmění tvar boty. Be Lenka a další výrobci barefoot obuvi prodávají i vlastní stélky do své obuvi. Pokud nosíte běžné boty a teprve na barefoot přecházíte, dejte nohám čas a nespoléhejte na to, že rozdíl vyrovná vložka.</p>'
          '<h2>Celodenní stání a pracovní obuv</h2>'
          '<p>Kdo celý den stojí na betonu nebo dlažbě, většinou hledá měkčí došlap. Pěnové a gelové vložky tvrdý povrch příjemně ztlumí. Pozor jen na objem: pracovní obuv bývá šitá na konkrétní stélku a silnější vložka v ní může zmenšit prostor pro prsty. U bezpečnostní obuvi s ochrannou špicí je dobré se řídit doporučením výrobce, protože výměna stélky může změnit její vlastnosti. Pomůže také mít dva páry vložek a střídat je, aby každá stihla vyschnout.</p>'
          '<h2>Vložky proti pachu</h2>'
          '<p>Některé vložky mají vrstvu s aktivním uhlím nebo antibakteriální úpravu, která omezuje pach. Na nohy, které se hodně potí, je to užitečná pomoc, jenže sama nestačí. Důležité je botu po nošení vyvětrat, vložku vytáhnout a vysušit a ponožky volit z materiálu, který odvádí vlhkost. Takové vložky mají kratší životnost, protože schopnost pohlcovat pach se postupně vyčerpá.</p>'
          '<h2>Vložky do lyžařských a bruslařských bot</h2>'
          '<p>Skelet lyžařské boty je tuhý a noha v něm nemá kam uhnout, takže každá nerovnost pod chodidlem je cítit. Stélky dodávané s botou bývají ploché a tenké. Mnoho lyžařů je nahrazuje tvarovanou nebo tepelně tvarovatelnou vložkou, kterou připraví odborník v servisu nebo prodejně. Pokud boty upravuje servis, zmiňte novou vložku hned na začátku, protože ovlivní, jak hluboko noha v botě sedí. Podobně je to u bruslí a <a href="/lyzarske-boty/">lyžařských bot</a> pro děti, kde se ale noha rychle mění a individuální úpravy se vyplatí méně.</p>'
          '<h2>Jak poznat, že vložka sedí</h2>'
          '<ul><li>Okraje vložky lícují s vnitřní stranou boty a nikde se neohýbají nahoru.</li>'
          '<li>Pata leží v patní misce a při chůzi z ní nevyjíždí.</li>'
          '<li>Prsty mají nad sebou stejný prostor jako s původní stélkou.</li>'
          '<li>Vložka se v botě neposouvá ani při zouvání.</li>'
          '<li>Po hodině chůze necítíte žádné nové tlakové místo.</li></ul>'
          '<p>Vložku vždy zkoušejte s ponožkami, které k botám nosíte. Silná zimní ponožka a tenká běžecká mění objem tak, že stejná vložka může v jednom případě sedět a ve druhém tlačit.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Silná vložka do bot, které už tak sedí přesně.</li>'
          '<li>Zastřižení podle oka bez šablony původní stélky.</li>'
          '<li>Spoléhání na sériovou vložku při dlouhodobých bolestech místo návštěvy lékaře.</li>'
          '<li>Dvě vložky na sobě, po kterých noha v botě klouže.</li>'
          '<li>Nová sportovní stélka vyzkoušená poprvé až na závodě.</li></ul>'
          '<p>K vložkám se hodí <a href="/sportovni-ponozky/">sportovní ponožky</a> a pro péči o svršek <a href="/impregnace/">impregnace</a>. Při nestabilním kotníku vybírejte spíš <a href="/ortezy-na-kotnik/">ortézy na kotník</a> po konzultaci s lékařem.</p>',
    faq=[
        ('Jak zjistit velikost vložky do bot?', 'Vycházejte z čísla bot a vložku zastřihněte podle původní stélky. Většina vložek má na spodní straně vyznačené linky pro střih.'),
        ('Jsou vložky z obchodu ortopedické?', 'Sériové vložky jsou pomůcka pro pohodlí, ne zdravotnický prostředek na míru. Při bolestech nohou rozhoduje o vhodné vložce ortoped nebo podiatr.'),
        ('Přispívá pojišťovna na vložky?', 'Jen na ortopedické vložky vyrobené na zakázku podle předpisu lékaře, a to za určitých podmínek. Sériové vložky z běžného prodeje nehradí.'),
        ('Jaké vložky do zimních bot?', 'Vlněné, plstěné nebo s hliníkovou fólií, které izolují od studené země. Po nošení je vytáhněte a vysušte.'),
        ('Jak fungují vyhřívané vložky?', 'Mají v sobě topné vlákno napájené baterií a teplota se nastavuje ovladačem, tlačítkem nebo aplikací. Výdrž závisí na stupni vyhřívání.'),
        ('Dají se vyhřívané vložky zastřihnout?', 'Často jen v části bez topného prvku. Vždy se řiďte vyznačenými linkami a návodem výrobce.'),
        ('Kdy vložku vyměnit?', 'Když je pěna stlačená, gel popraskaný nebo vložka v botě klouže a deformuje se. Pak už neplní svou funkci.'),
        ('Hodí se vložky do barefoot bot?', 'Jen tenké a ploché, typicky vlněné nebo plstěné na zimu. Tvarované vložky by změnily to, proč se barefoot obuv nosí.'),
        ('Co jsou podpatěnky?', 'Malé vložky jen pod patu, často gelové a samolepicí. Ztlumí došlap a zaberou v botě málo místa.'),
        ('Kde koupit vložky do bot?', 'Sporteka u každé vložky ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])
