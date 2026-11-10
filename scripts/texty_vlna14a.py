"""sporteka.cz — wave 14a (4. 11. 2026): long texts (>= 1650 words) for zimni-obuv, basketbal, lahve-a-termosky, nakrcniky-a-satky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ zimni-obuv
NEW['zimni-obuv'] = dict(long=True,
    title='Zimní boty a sněhule: výběr a nabídky obchodů | Sporteka',
    desc='Zimní boty a sněhule pánské, dámské i dětské: membrána, zateplení, podešev a velikost. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Zimní obuv</strong> má za úkol tři věci současně: udržet nohu v teple, v suchu a pevně na zemi. Žádná bota nevyhraje ve všech třech disciplínách naráz, takže se vyplatí nejdřív určit, kde ji budete nosit. Cesta do práce po posypaném chodníku klade jiné nároky než brodění sněhem po kolena nebo celodenní pobyt venku s dětmi.</p>'
          '<p>Na Sportece najdete <strong>zimní boty a sněhule</strong> pánské, dámské i dětské z českých obchodů a u každého páru porovnáte nabídky vedle sebe. Rozcestník je vhodné doplnit o <a href="/sportovni-ponozky/">sportovní ponožky</a>, <a href="/merino-ponozky/">merino ponožky</a>, <a href="/nesmeky/">nesmeky</a> a <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>. Pro delší výlety v zimní krajině se hodí také <a href="/trekova-obuv/">trekové boty</a> a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>.</p>',
    guide='<h2>Jak vybrat zimní boty, aby noha nemrzla</h2>'
          '<p>Studené nohy způsobuje málokdy samotná tloušťka zateplení. Častěji za to může vlhkost, těsná bota nebo studená podešev, která odvádí teplo do země. Proto se při výběru dívejte se na botu jako na systém: svršek, podšívka, stélka, podrážka a ponožka spolu musí fungovat. Slabý článek zkazí celek, i když ostatní části vypadají skvěle.</p>'
          '<h3>Tři základní situace</h3>'
          + T(['Situace', 'Na co dbát', 'Co hledat'], [
              ['Město a dojíždění', 'protiskluz na mokrých dlažbách, lehkost, rychlé zouvání', 'nízká nebo středně vysoká bota s vodoodolnou úpravou, hrubší vzorek'],
              ['Sníh a delší pobyt venku', 'vodotěsnost, výška svršku, izolace od země', 'sněhule nebo bota s vyšším lýtkem, silná podešev, uzavřený jazyk'],
              ['Zimní túra a náročný terén', 'stabilita, tuhost podrážky, prodyšnost', 'membránová bota s pevným okopem, viz <a href="/trekova-obuv/">trekové boty</a>'],
              ['Děti na hřišti a sáňkování', 'suchá noha, snadné obouvání, bezpečnost', 'rychlé zapínání, zateplení, reflexní prvky, pevná špice']]) +
          '<h2>Typy zimní obuvi a jejich rozdíly</h2>'
          '<p>Pod pojmem zimní boty se skrývá několik odlišných konstrukcí. Každá je dobrá na něco jiného, a proto nemá smysl hledat jednu univerzální.</p>'
          '<ul><li><strong>Městské zateplené boty</strong> bývají z kůže, textilu nebo kombinace, mají podšívku a mírný vzorek. Hodí se na suché mrazivé dny a běžné chození.</li>'
          '<li><strong>Boty s membránou</strong> propouštějí vodní páru z nohy ven, ale zabraňují průniku kapek zvenku. Pomáhají proti promoknutí v tajícím sněhu, ale membrána sama nehřeje.</li>'
          '<li><strong>Sněhule</strong> mají vysoký svršek, často z nepromokavé části v oblasti spodku a z textilu nahoře. Jsou určené do sněhu a kaluží, nikoli na dlouhé pěší túry.</li>'
          '<li><strong>Zimní trekové boty</strong> kombinují tuhou podrážku s izolací. Najdete je ve skupině <a href="/vysoke-trekove-boty/">vysokých trekových bot</a>.</li>'
          '<li><strong>Chlupaté a pohodlné zimní boty</strong> typu měkkých kozaček jsou určené hlavně pro suchý chlad a krátké vzdálenosti, ne pro hluboký sníh.</li>'
          '<li><strong>Holínky s podšívkou</strong> jsou vodotěsné, avšak nedýchají, proto se hodí na blátivé zimy bez mrazu, více v kategorii <a href="/holinky/">holínky</a>.</li></ul>'
          '<h2>Materiál svršku a podšívka</h2>'
          '<p>Kožené boty jsou odolné a dají se ošetřit voskem nebo impregnací, ale na dlouhé vystavení vodě potřebují péči. Textilní a syntetické svršky jsou lehčí a rychleji schnou, jenže při průniku vody v šicích švech zmokne i ten nejlepší materiál. Důležité je, zda je jazyk našitý až k svršku. Takzvaný měchový jazyk brání vniknutí sněhu při chůzi závějí a je jedním z nejlevnějších vylepšení, na které se při výběru zapomíná.</p>'
          '<p>Podšívka z umělého rouna, ovčí vlny nebo podobného materiálu zadržuje vzduch a ten izoluje. Pozor ale na to, že s každou vrstvou zateplení ubývá v botě místa. Pokud je zateplená bota naplněná do posledního milimetru, stlačený materiál izoluje hůř než volnější vrstva. Právě proto se u zimních bot vyplatí koupit o něco větší velikost.</p>'
          '<h2>Podešev, vzorek a protiskluz</h2>'
          '<p>Podrážka je nejdůležitější část z hlediska bezpečnosti. Tvrdá plastová směs v mrazu ztrácí pružnost a po ledu klouže. Měkčí pryž se přizpůsobí nerovnostem a drží lépe, ale rychleji se obrušuje. Hluboké a široce rozestavěné vroubky se nezanášejí sněhem a dobře kousají do mokrého podkladu. Na čistý led žádná běžná podešev nestačí a pomůže jen nasazená kovová nebo gumová pomůcka. Takové návleky najdete v kategorii <a href="/nesmeky/">nesmeky a protiskluzové návleky</a>.</p>'
          '<p>Podrážka má také izolační funkci. Zima se do nohy dostává zespodu, takže silnější mezivrstva a pěnová stélka dělají víc než silná podšívka. Hodí se kontrolovat, zda se stélka dá vyjmout. S vyjmutou stélkou se bota snáze vysuší, případně nahradí vlastní vložkou, viz <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>'
          '<h2>Velikost a ponožky</h2>'
          '<p>Zimní bota se zkouší vždy v ponožce, ve které ji budete nosit. Prsty se nesmějí dotýkat špičky ani při sestupu z kopce a pata nemá cestovat nahoru a dolů. Příliš těsná bota stlačuje cévy, nohy rychleji prochladnou a vzduch kolem nich přestane izolovat. Ideální je několik milimetrů rezervy před prsty a pevné držení v oblasti paty a nártu.</p>'
          '<p>Ponožka je třetí vrstva izolace. Bavlněná se při pocení namočí a ochlazuje, zatímco syntetická nebo vlněná odvádí vlhkost. Přehled najdete v <a href="/sportovni-ponozky/">sportovních ponožkách</a> a hlavně v <a href="/merino-ponozky/">merino ponožkách</a>, které hřejí i trochu zvlhlé. Nenavlékejte dvě silné ponožky najednou, pokud bota není určená na silnější vrstvu, protože stlačují nohu a zhoršují prokrvení.</p>'
          '<h2>Zimní boty pro děti</h2>'
          '<p>Dětská noha roste a drží méně tepla než dospělá, proto se vyplatí kupovat bezpečně, ne co nejlevněji. Důležitá je suchá noha, protože mokré dítě rychle zmrzne a přestane bavit i sáňkování. Rychlé zapínání usnadní obouvání na hřišti a před školkou. Ověřte, že se v botě dítě může volně hýbat prsty a že podrážka není tuhá jako prkno. Bota větší o půl velikosti vystačí lépe, ale neměla by být natolik velká, aby dítě zakopávalo.</p>'
          '<p>Na zimní radovánky se hodí i další výbava: <a href="/sane-a-boby/">sáně a boby</a>, <a href="/lyzarske-rukavice/">rukavice</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>. Pokud dítě začíná na lyžích, potřebuje už specializované <a href="/lyzarske-boty/">lyžařské boty</a>, běžná zimní obuv do vázání nepatří.</p>'
          '<h2>Zimní boty podle sportu a aktivity</h2>'
          '<ul><li>Na <a href="/snezky/">sněžnice</a> se nosí vodotěsná vysoká bota s dostatečně pevnou podrážkou. Přesný typ určuje vázání sněžnic.</li>'
          '<li>K zimní chůzi s <a href="/trekove-hole/">trekovými holemi</a> se hodí stabilní bota s vyšším svrškem, který zpevní kotník.</li>'
          '<li>Pro zimní běh jsou určené zimní <a href="/bezecka-obuv/">běžecké boty</a>, často s membránou nebo hustší tkaninou svršku.</li>'
          '<li>Snowboard a lyže mají vlastní obuv: <a href="/snowboardove-boty/">snowboardové boty</a>, <a href="/skialpove-boty/">skialpové boty</a>.</li>'
          '<li>Na ledovou kru a rybaření se uplatní zateplená bota s vysokým svrškem a silnou podešví.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Mezi nejčastěji nabízenými jsou ' + B(('geox', 'Geox'), ('loap', 'Loap'), ('skechers', 'Skechers'), ('o-neill', "O'Neill"), ('moon-boot', 'Moon Boot'), ('primigi', 'Primigi'), ('reima', 'Reima'), ('alpine-pro', 'Alpine Pro'), ('trespass', 'Trespass'), ('columbia', 'Columbia'), ('sorel', 'Sorel'), ('ugg', 'Ugg')) + '. Geox a Primigi mají široké zastoupení v dětských a městských botách, Loap, Alpine Pro, Reima a Trespass jsou častou volbou pro praktické zimní boty. Moon Boot, Sorel a Ugg patří k tomu, co lidé chtějí do chladných měst, a Columbia se pohybuje spíš na outdoorové straně. Značku si nevybírejte slepě, rozhodující je střih a použitý materiál konkrétního modelu.</p>'
          '<h2>Péče o zimní obuv</h2>'
          '<p>Hlavní nepřítel zimních bot je sůl a vlhkost. Po příchodu domů z posypaných chodníků boty očistěte vlhkým hadrem, protože sůl vysouší kůži a zanechává bílé skvrny. Vyjměte stélky, uvolněte tkaničky a nechte boty vyschnout při pokojové teplotě. U radiátoru, kamen nebo v troubě se lepidlo uvolní, kůže popraská a materiál se zdeformuje. Do mokré boty pomůže nacpat zmačkané noviny, které vlhkost nasají.</p>'
          '<p>Impregnaci obnovujte podle materiálu: kůže vosk nebo krém, textil sprej. Impregnace membránu nenahrazuje, jen zlepšuje stékání vody po povrchu a tím udržuje prodyšnost. Pokud se po dešti svršek vsákne a zmokne, membrána dýchá hůř. Také si pamatujte, že boty se vyplatí střídat. Dvě různé dvojice za sebou vyschnou lépe než jedna nošená každý den.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit botu těsně na tenkou ponožku a pak do ní nacpat silnou.</li>'
          '<li>Spoléhat na to, že vodoodolná úprava je totéž co vodotěsná membrána.</li>'
          '<li>Zvolit hladkou podrážku do města, kde se střídá sníh s ledem.</li>'
          '<li>Sušit mokré boty přímo na topení.</li>'
          '<li>Koupit dětské boty o příliš velkou velikost a doufat, že vydrží dvě zimy.</li>'
          '<li>Zapomenout na doplňky, jako jsou nesmeky nebo vložky, které se vyplatí i u nejlepší boty.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>U každého páru vidíte nabídky více českých obchodů vedle sebe, takže si můžete ověřit, kde je potřebná velikost skladem. Zimní velikosti se prodávají rychle, proto se vyplatí neotálet, jakmile se objeví první sníh. Filtrování podle značky a velikosti zkrátí hledání. Širší nabídku pro chladnou sezónu najdete v kategorii <a href="/zimni-sporty/">zimní sporty</a>, kde navazují bundy, kalhoty, čepice a další vybavení, například <a href="/zimni-bundy/">zimní bundy</a> a <a href="/termopradlo/">termoprádlo</a>.</p>',
    faq=[('Jaké zimní boty vybrat do města?', 'Do města stačí lehčí zateplená bota s vodoodolnou úpravou a hrubším vzorkem podrážky. Přednost mají boty, které se rychle obouvají a mají sundavací stélku, aby se daly po sušení znovu použít.'),
         ('Jaký je rozdíl mezi vodoodolnou a vodotěsnou botou?', 'Vodoodolná bota odpuzuje vodu jen na povrchu a po delším působení promokne. Vodotěsná má uvnitř membránu nebo uzavřenou konstrukci, která kapky nepustí dovnitř, a to i po delší době.'),
         ('Jakou velikost zimních bot koupit?', 'Zhruba o půl velikosti větší, než nosíte v létě, aby se vešla silnější ponožka a kolem prstů zůstal vzduch. Prsty se však nesmí dotýkat špičky a pata se nemá zvedat.'),
         ('Jsou sněhule vhodné na dlouhé túry?', 'Většinou ne. Sněhule jsou teplé a vysoké, ale mají měkčí podrážku a menší oporu kotníku. Na dlouhé zimní túry se hodí trekové boty s tužší podrážkou a membránou.'),
         ('Jak poznat dobrý protiskluz?', 'Hledejte hluboké a široce rozestavěné vroubky z měkčí pryže, která v mrazu nezatvrdne. Na čistý led nestačí ani nejlepší podešev, tam pomůžou jen nesmeky nasazené přes obuv.'),
         ('Jak sušit zimní boty?', 'Vyjměte stélky, rozvažte tkaničky a nechte boty schnout při pokojové teplotě. Vnitřek lze vycpat novinami. Radiátor, kamna a fén poškozují lepidlo, kůži i membránu.'),
         ('Jak odstranit sůl z bot?', 'Sůl otřete vlhkým hadříkem co nejdříve po příchodu domů, případně použijte roztok vody s trochou octa. Pak nechte boty uschnout a u kůže ošetřete krémem nebo voskem.'),
         ('Jaké ponožky nosit v zimních botách?', 'Nejlépe vlněné, merino nebo syntetické, které odvádějí pot a hřejí i vlhké. Bavlna zvlhne a ochlazuje. Dvě silné ponožky přes sebe většinou škodí, protože stlačí nohu a zhorší prokrvení.'),
         ('Jaké zimní boty pro malé děti?', 'Teplé, vodotěsné nebo alespoň dobře impregnované, s rychlým zapínáním a pevnou špicí. Podrážka má být pružná, aby dítě mohlo přirozeně našlapovat, a bota nesmí tlačit prsty.'),
         ('Hodí se zimní boty také na sněžnice a procházky se psem?', 'Ano, pokud jsou vodotěsné, mají dostatečně vysoký svršek a stabilní podešev. Pro sněžnice ověřte, že bota drží ve vázání a že není příliš objemná.'),
         ('Kdy se zimní boty vyplatí koupit?', 'Při prvním sněhu bývá nejširší výběr velikostí, ale také nejvíce zájemců. Sledujte vývoj nabídek obchodů, protože sezónní doprodeje často začínají už po Novém roce.')],
)

# ------------------------------------------------------------------ basketbal
NEW['basketbal'] = dict(long=True,
    title='Basketbal: míče, boty, dresy a vybavení | Sporteka',
    desc='Basketbalové míče, boty, dresy a doplňky pro hráče všech úrovní. Průvodce výběrem velikosti míče, obuvi a oblečení a nabídky českých obchodů.',
    intro='<p><strong>Basketbal</strong> je hra, kde se vybavení pozná hlavně na nohách a v rukou. Míč musí mít správnou velikost a povrch pro hřiště, na kterém hrajete, boty musí snést neustálé zastavování, skoky a změny směru. Zbytek tvoří pohodlné oblečení, které nebrání pohybu a odvádí pot.</p>'
          '<p>Na Sportece najdete <a href="/basketbalove-mice/">basketbalové míče a koše</a>, <a href="/basketbalova-obuv/">basketbalové boty</a>, <a href="/dresy/">dresy</a>, <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/sportovni-ponozky/">ponožky</a>, <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> a další doplňky z českých obchodů. U každého kusu porovnáte nabídky vedle sebe a vyberete velikost, která je zrovna skladem. Text níže vysvětluje, jak zvolit velikost míče podle věku, čím se liší halová a venkovní hra, na co se dívat u bot a jak se starat o výbavu, aby vydržela celou sezónu a nezkazila radost z hry.</p>',
    guide='<h2>Co potřebuje basketbalista a od čeho začít</h2>'
          '<p>Na první trénink stačí tři věci: míč, vhodné boty a oblečení, ve kterém se dá volně hýbat. Cokoli dalšího se dá přikupovat podle toho, jak často hrajete a kde. Hráč na venkovním hřišti potřebuje trochu jinou výbavu než hráč v tělocvičně a mladý začátečník jinou než dospělý v amatérské lize. Než otevřete e-shop, určete, kde budete hrát nejčastěji, protože na tom závisí povrch míče i podrážka boty.</p>'
          + T(['Kde hrajete', 'Míč', 'Obuv'], [
              ['Venkovní hřiště (beton, asfalt)', 'gumový nebo kompozitní míč s odolným povrchem', 'bota s odolnou, tvrdší podrážkou, která se nebrousí tak rychle'],
              ['Hala nebo tělocvična', 'kožený nebo kompozitní míč s lepším úchopem', 'bota s lepivější, tenčí podrážkou pro přilnavost na parketách'],
              ['Obojí střídavě', 'kompozitní míč pro vnitřní i venkovní použití', 'kompromis, nebo dva páry na každé prostředí'],
              ['Hra doma na koš', 'menší nebo lehčí míč podle věku', 'běžná sportovní obuv, viz <a href="/treninkova-obuv/">fitness a tréninková obuv</a>']]) +
          '<h2>Míče: velikost a povrch</h2>'
          '<p>Basketbalové míče se vyrábějí v několika velikostech podle věku a kategorie. Označují se čísly, přičemž čím vyšší číslo, tím větší obvod a hmotnost. Nejmenší míče jsou pro nejmladší děti, střední velikosti pro starší děti a juniory, největší pro dospělé hráče a hráčky. Přesné rozdělení určuje basketbalová federace, proto je vhodné ověřit označení u konkrétního míče a pro oficiální soutěže se zeptat trenéra. Špatně zvolený míč naučí dítě špatný hod, protože se mu bude vymykat z ruky.</p>'
          '<p>Povrch rozhoduje o chování míče. Kožené míče mají nejlepší úchop v hale, ale venku se rychle obrousí. Kompozitní a syntetické mají stabilnější odrazy a snesou víc zacházení. Gumové míče jsou nejodolnější a dobře se hodí na venkovní hřiště, jen je jejich úchop méně pohodlný. Před každou hrou zkontrolujte tlak: míč s příliš nízkým tlakem se špatně odráží a ztěžuje driblink, příliš tvrdý bolí v prstech. Pro hodnocení stačí upustit míč z úrovně ramen a sledovat, jak vysoko se odrazí. Více se dozvíte v kategorii <a href="/basketbalove-mice/">basketbalové míče a koše</a>.</p>'
          '<p>K vlastnímu míči patří také koš. Domácí koše se prodávají jako přenosné s nastavitelnou výškou, nebo jako nástěnné. U přenosných dbejte na stabilní základnu a závaží, aby se při smeči nepřevrhl.</p>'
          '<h2>Basketbalové boty</h2>'
          '<p>Basketbalová obuv se liší od běžecké tím, že je určená pro boční pohyby a doskoky. Běžecká bota je měkká a nízká, basketbalová má pevnější patu, zesílený střed a bezpečnější vedení nohy. Hlavní kategorie jsou nízké, střední a vysoké střihy. Vyšší střih nabízí větší oporu kotníku, nižší je lehčí a rychlejší. Který je lepší, záleží na hráči a jeho stylu: pivot často volí větší oporu, rozehrávač spíš nižší a svižnější botu. Žádný střih ale kotník neochrání před zraněním, jen ho podpoří.</p>'
          '<ul><li><strong>Tlumení:</strong> pěnová mezipodešev pohlcuje nárazy při doskoku. Měkčí tlumení je pohodlnější, ale méně stabilní.</li>'
          '<li><strong>Přilnavost:</strong> vzor na podrážce má držet na parketách, ale nesmí být tak lepivý, aby bránil prokluzu při změně směru.</li>'
          '<li><strong>Váha:</strong> lehčí bota znamená rychlejší pohyb, těžší většinou větší trvanlivost a podporu.</li>'
          '<li><strong>Prodyšnost:</strong> síťovaný svršek odvádí teplo, ale rychleji se opotřebuje než syntetická kůže.</li></ul>'
          '<p>Velikost zkoušejte v ponožkách, ve kterých budete hrát. Prst by neměl narážet do špičky při prudkém zastavení a pata se nesmí zvedat. Podrobnější nabídku najdete v <a href="/basketbalova-obuv/">basketbalových botách</a>, pro hru v tělocvičně obecně také v <a href="/salova-obuv/">sálové a halové obuvi</a>.</p>'
          '<h2>Oblečení: dres, kraťasy a vrstvy</h2>'
          '<p>Základem je prodyšný dres bez rukávů a volné kraťasy, které nebrání v pohybu. Dres je široký v průramech, aby paže měly volnost, a dlouhý, aby se při driblinku nezvedal. Na tréninky stačí běžné <a href="/sportovni-tricka/">sportovní tričko</a> nebo <a href="/funkcni-tricka/">funkční tričko</a>, které odvádí pot. Kraťasy se vybírají podle délky a pohodlí, nabídku najdete v <a href="/sportovni-kratasy/">sportovních kraťasech</a>.</p>'
          '<p>Před hrou a po ní se hodí teplejší vrstva, aby se svaly nezchladily. K tomu poslouží <a href="/teplaky/">tepláky</a> a <a href="/mikiny/">mikiny</a>. Hráči, kteří si chtějí pod dres obléknout kompresní vrstvu, najdou ji mezi <a href="/funkcni-trenink/">funkčním tréninkem</a>. Kolekce týmových dresů jsou součástí kategorie <a href="/dresy/">dresy</a>. Při nákupu zkontrolujte, zda je u dresu nabídka s potiskem čísla, nebo zda se potisk objednává zvlášť.</p>'
          '<h2>Ochrana a doplňky</h2>'
          '<ul><li><a href="/bandaze-a-ortezy/">Bandáže a ortézy</a> podpoří kotník, koleno nebo zápěstí. Vybírejte podle dosavadních obtíží, ne preventivně všechno najednou, protože příliš tuhá opora může omezovat pohyb.</li>'
          '<li><a href="/sportovni-ponozky/">Ponožky</a> s tlumením v oblasti paty a chodidla snižují otlaky a zlepšují komfort.</li>'
          '<li>Čelenky a potítka odvádějí pot z čela a zápěstí, což zlepšuje úchop při driblinku.</li>'
          '<li><a href="/sportovni-tasky/">Sportovní tašky</a> a <a href="/batohy/">batohy</a> pomáhají nosit míč, boty a náhradní oblečení. Dobře je vybavit je oddělenou kapsou na mokré věci.</li>'
          '<li>Pitný režim zajistí <a href="/lahve-a-termosky/">láhev na vodu</a> a v teplých dnech také <a href="/iontove-napoje/">iontové nápoje</a>.</li></ul>'
          '<h2>Basketbal pro děti a začátečníky</h2>'
          '<p>Dítě nemusí mít nejdražší výbavu, ale míč a obuv by měly odpovídat jeho věku a síle. Příliš těžký míč vede k hodům z boku a k bolesti zápěstí. Nižší koš nebo koš s nastavitelnou výškou umožní dítěti nacvičit správnou techniku střelby. Boty musí pevně držet nohu a mít pružnou podrážku, protože děti rychle rostou a špatná obuv by jim mohla zkazit chuť do hry. Pokud se dítě chystá do kroužku, zeptejte se trenéra, zda klub vyžaduje konkrétní barvu dresu nebo typ obuvi do haly.</p>'
          '<p>Začátečníkovi pomáhá také pestrá výbava na cvičení doma. Pro rozvoj kondice a rychlosti jsou užitečná <a href="/svihadla/">švihadla</a>, <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>. Další míčové hry najdete v kategorii <a href="/micove-sporty/">míčové sporty</a>, podobné sálové sporty jsou <a href="/volejbal/">volejbal</a>, <a href="/hazena/">házená</a> a <a href="/florbal/">florbal</a>.</p>'
          '<h2>Rozcvička a prevence zranění</h2>'
          '<p>Basketbal zatěžuje kotníky, kolena a zápěstí. Před hrou je dobré několik minut zvyšovat tepovou frekvenci, protáhnout lýtka, předloktí a kyčle a zacvičit si doskoky na místě. Nejčastější úraz je podvrtnutí kotníku při dopadu na nohu soupeře, proto pomáhá posilování lýtkových svalů a nácvik rovnováhy na jedné noze, například s <a href="/balancni-pomucky/">balančními pomůckami</a>. Pravidelné protažení po hře zkracuje dobu zotavení. Při bolesti, která nepřechází, nehrajte přes ni a poraďte se s lékařem.</p>'
          '<h2>Základní dovednosti a pomůcky na trénink</h2>'
          '<p>Technika se učí postupně: driblink, přihrávka, střelba, doskakování a obrana. Pro driblink se hodí trénink s méně dominantní rukou a s pohledem zvednutým od míče. Střelbu zlepšuje opakování správného postoje a pohybu zápěstí. Doma pomůže zeď na přihrávky nebo koš v zahradě, viz <a href="/hry-na-zahradu/">hry na zahradu</a>. Kondiční složku posilují běh a skákání, takže se hodí i <a href="/beh/">běh</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce basketbalu dominují ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('jordan', 'Jordan'), ('under-armour', 'Under Armour')) + ', které pokrývají obuv i oblečení. Míče najdete u značek ' + B(('wilson', 'Wilson'), ('spalding', 'Spalding'), ('molten', 'Molten'), ('kipsta', 'Kipsta')) + ', mezi nimiž Wilson a Spalding jsou tradiční názvy. Kipsta a Molten nabízejí míče pro školní i klubové použití. Základní hodnotící měřítko ale zůstává stejné: velikost míče, povrch a pocit v ruce.</p>'
          '<h2>Péče o míče a boty</h2>'
          '<p>Míč nevozte v horkém autě a nenechávejte ho na slunci, plyn uvnitř zvětšuje tlak a materiál stárne. Venkovní míč používejte jen venku, protože drsný povrch hřiště ničí kožený potah. Mokrý míč osušte hadrem a nechte vyschnout při pokojové teplotě. Pro dofouknutí použijte pumpu s jehlou, kterou předem zvlhčíte, aby nepoškodila ventilek. U bot je užitečné vyndat stélky a nechat je po hře větrat. Vzorek podrážky na parketách se hodí čas od času otřít vlhkým hadříkem, protože prach snižuje přilnavost.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Hrát venku s halovým koženým míčem, který se brzy zničí.</li>'
          '<li>Nosit běžné běžecké boty, které nedrží nohu při bočním pohybu.</li>'
          '<li>Hrát s nedofouknutým míčem, který se špatně odráží a ztěžuje driblink.</li>'
          '<li>Koupit dítěti obuv o dvě čísla větší a čekat, že dorůstá.</li>'
          '<li>Zapomenout na rozcvičku, bez které hrozí podvrtnutí kotníku i při dobré obuvi.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého produktu vidíte nabídky více českých obchodů najednou, včetně dostupnosti velikostí. Obuv i oblečení rychle ubývají v nejběžnějších číslech, takže vyplatí se sledovat, které obchody je mají skladem. Hledání zúžíte podle značky, velikosti nebo podkategorie. Nabídku míčů a košů najdete v kategorii <a href="/basketbalove-mice/">basketbalové míče a koše</a>, obuv v <a href="/basketbalova-obuv/">basketbalových botách</a> a týmové oblečení v <a href="/dresy/">dresech</a>.</p>',
    faq=[('Jaká velikost basketbalového míče je správná?', 'Záleží na věku a kategorii. Velikost 7 je pro muže, velikost 6 pro ženy a starší dívky, velikost 5 pro děti a mládež, menší míče pro nejmladší. Přesné značení ověřte u výrobce nebo u trenéra, protože se liší podle soutěže.'),
         ('Jaký je rozdíl mezi halovým a venkovním míčem?', 'Halový míč bývá kožený nebo kompozitní s lepším úchopem a ztrácí se na hrubém povrchu. Venkovní míč má odolnější povrch, často gumový nebo kompozitní, který snese asfalt či beton.'),
         ('Kolik by měl mít míč vzduchu?', 'Tlak určuje výrobce, najdete ho většinou přímo na míči u ventilku. Míč je správně nafouknutý, když se po pádu z výšky ramen odrazí zhruba do výšky pasu a nepůsobí příliš tvrdě.'),
         ('Jaké boty zvolit na basketbal?', 'Basketbalové, s pevnou patou a dobrou přilnavostí podrážky. Běžecké boty jsou měkké a nízké, nechrání před bočním pohybem, a proto se na hru nehodí.'),
         ('Jsou vysoké basketbalové boty lepší než nízké?', 'Vysoké nabízejí větší pocit opory kotníku, nízké jsou lehčí a rychlejší. Kotník neochrání žádný střih zcela, proto záleží na stylu hry a zdravotní historii hráče.'),
         ('Jak poznat správnou velikost basketbalových bot?', 'Zkoušejte je s hrací ponožkou a ujistěte se, že mezi špičkou a palcem zůstává pár milimetrů. Pata musí pevně sedět a při zastavení prsty nesmějí narážet do špičky.'),
         ('Co si vzít na trénink?', 'Míč, boty, prodyšné tričko, kraťasy, ponožky a láhev na vodu. Na chladnější tělocvičnu se hodí tepláky a mikina na zahřátí před hrou.'),
         ('Hodí se kompresní oblečení pod dres?', 'Některým hráčům vyhovuje, protože drží svaly a odvádí pot. Není to povinná součást výbavy, ale pro tréninky v chladné hale nebo při pocení může být pohodlné.'),
         ('Kdy použít bandáž nebo ortézu?', 'Při předchozím zranění kotníku, kolena nebo zápěstí, případně podle rady lékaře či fyzioterapeuta. Bandáž nenahrazuje rozcvičení a nemá se nosit preventivně všude bez rozmyslu.'),
         ('Jak vybrat basketbalový koš pro děti?', 'Zvolte koš s nastavitelnou výškou, aby dítě nemuselo házet příliš vysoko. Zkontrolujte stabilitu základny a materiál desky. Pro domácí použití je lepší lehčí míč než oficiální velikost pro dospělé.'),
         ('Jak se starat o basketbalový míč?', 'Nenechávejte ho na slunci ani v mrazu, venku používejte jen odolný míč a po zmoknutí ho osušte. Tlak kontrolujte před každou hrou a pro nafukování používejte jehlu.')],
)

# ------------------------------------------------------------------ lahve-a-termosky
NEW['lahve-a-termosky'] = dict(long=True,
    title='Láhve a termosky: výběr podle materiálu | Sporteka',
    desc='Sportovní láhve, termosky, termohrnky, hydrovaky a šejkry: nerez, tritan, objem i víčka. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Láhev na pití</strong> vypadá jako nejjednodušší kus výbavy, ale právě na ní se dají udělat nejvíc drobných chyb. Příliš těžká na běh, nepohodlná na kolo, s víčkem, které teče v batohu, nebo termoska, která po týdnu zapáchá. Správná volba závisí na tom, co budete pít, jak dlouho a při jaké činnosti.</p>'
          '<p>Na Sportece najdete <strong>sportovní láhve, termosky, termohrnky, hydrovaky a šejkry</strong> z českých obchodů a u každého kusu porovnáte nabídky vedle sebe. S pitným režimem souvisí i <a href="/iontove-napoje/">iontové nápoje</a>, <a href="/cyklo-lahve-a-drzaky/">cyklistické láhve a držáky</a>, <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/kempingove-nadobi/">kempingové nádobí</a>. Průvodce níže vás provede materiály, uzávěry, objemem i čištěním, abyste nekoupili nic, co skončí na dně skříně.</p>',
    guide='<h2>Jak si vybrat láhev nebo termosku</h2>'
          '<p>Než porovnáte konkrétní modely, odpovězte si na tři otázky. Co do ní budete nalévat: vodu, čaj, kávu, nebo sladký nápoj? Jak dlouho má tekutina vydržet teplá či studená? A kam ji budete dávat: do batohu, do držáku na kole, do kapsy bundy, nebo ji ponesete v ruce? Odpovědi vás nasměrují k materiálu, objemu a typu uzávěru dřív než reklamní popis.</p>'
          + T(['Použití', 'Hlavní požadavek', 'Typ'], [
              ['Běh a lehký trénink', 'nízká váha, snadné pití za pohybu', 'měkká nebo plastová láhev, běžecká vesta s měkkými flaskami'],
              ['Kolo', 'tvar pro držák, pití jednou rukou', 'láhev se sportovním víčkem, viz <a href="/cyklo-lahve-a-drzaky/">cyklistické láhve a držáky</a>'],
              ['Turistika, celý den', 'objem a odolnost', 'širokohrdlá láhev nebo hydrovak do batohu'],
              ['Zimní výlet, čaj', 'udržení tepla', 'nerezová termoska s dvojitou stěnou'],
              ['Kancelář, škola', 'těsnost, snadné čištění', 'nerezová nebo skleněná láhev, dětská láhev s pevným víčkem'],
              ['Posilovna a protein', 'míchání prášku', 'šejkr s kuličkou nebo sítkem, viz <a href="/proteiny/">proteiny</a>']]) +
          '<h2>Materiál: nerez, tritan, plast, sklo</h2>'
          '<p>Materiál ovlivňuje váhu, trvanlivost, chuť nápoje i údržbu. Neexistuje jednoznačně nejlepší volba, jen vhodnější pro konkrétní situaci.</p>'
          '<ul><li><strong>Nerezová ocel</strong> je odolná, nepohlcuje pachy a hodí se na termosky, protože se z ní snadno dělá vakuová dvojitá stěna. Nevýhodou je vyšší váha a promáčknutí po pádu.</li>'
          '<li><strong>Tritan a podobné čiré plasty</strong> jsou lehké, odolné proti rozbití a dobře se čistí. Neudrží teplo, ale hodí se na vodu a sportovní nápoje.</li>'
          '<li><strong>Měkký polyetylen</strong> se používá u cyklistických a běžeckých lahví, které se dají zmáčknout. Některé typy zadržují pachy a je třeba je často prát.</li>'
          '<li><strong>Sklo</strong> nemění chuť a je dokonale hygienické, ale křehké. Hodí se do kanceláře nebo domů, méně na sport. Často se prodává s ochranným silikonovým obalem.</li>'
          '<li><strong>Hliník s vnitřním lakem</strong> je lehčí než nerez, ale vnitřní vrstva se může po čase poškrábat.</li></ul>'
          '<p>Pokud kupujete láhev na kyselé šťávy, kávu nebo iontový nápoj, zvolte materiál, který se čistí bez problémů. Těžko dostupné rohy a úzké hrdlo vedou k tomu, že se uvnitř usazuje sediment, který se pak špatně odstraňuje.</p>'
          '<h2>Termosky a termoláhve</h2>'
          '<p>Termoska udržuje teplotu díky vakuové vrstvě mezi dvěma stěnami: vzduch mezi nimi chybí, takže se teplo přenáší hůř. Nejdůležitější je víčko a těsnění, protože tudy teplo uniká nejvíc. Před nalitím horkého čaje pomůže termosku předehřát horkou vodou. Pokud chcete studený nápoj, zchlaďte ji předem naopak. Na dlouhou zimní túru se hodí širší hrdlo, kterým se naleje i vývar nebo polévka, na kancelář užší hrdlo s pitným otvorem.</p>'
          '<ul><li>Termoska s tlačítkovým uzávěrem se otevírá jednou rukou, ale může při tlaku v batohu povolit. U kupovaného kusu ověřte, zda je uzávěr jistý.</li>'
          '<li>Termohrnek (takzvaný cestovní) se hodí na kávu na cestu, ale nedržte ho v batohu naležato, pokud není výrobcem označen jako těsný.</li>'
          '<li>Termosky na jídlo mají široké hrdlo a lžičku v příslušenství. Jsou určené na polévku nebo kaši a hodí se také na dětské svačiny.</li>'
          '<li>Nikdy neplňte termosku sycenými nápoji, protože tlak plynu může uzávěr vystřelit nebo poškodit těsnění.</li></ul>'
          '<h2>Uzávěry a pití za pohybu</h2>'
          '<p>Uzávěr rozhoduje o tom, jestli se vám bude s láhví dobře žít. Šroubovací víčko je spolehlivé a těsné, ale vyžaduje dvě ruce. Sportovní víčko s ventilem se otevírá zubem nebo rukou a umožňuje pít za chůze nebo jízdy na kole. Slámkové víčko je pohodlné pro děti, ale hůř se čistí. Širokohrdlá láhev se snadno plní ledem a myje, avšak snadněji se z ní vylije obsah při pohybu. Zajímavé řešení nabízejí magnetické uzávěry, které lze pustit z jedné ruky. Ať vyberete cokoli, těsnění by mělo být vyměnitelné.</p>'
          '<h2>Hydrovaky a měkké flasky</h2>'
          '<p>Hydrovak je vak s hadičkou, který se vkládá do batohu, takže pijete bez zastavení a bez sundání batohu. Pomáhá hlavně na trailu, kole a při delších túrách, kdy se zastavovat nechcete. V zimě hadička zamrzá a volně visící náustek se snadno zablátí. Vak se po každém použití vyplachuje a suší s roztaženou přihrádkou, aby neplesnivěl. Běžecké vesty používají místo vaku často měkké flasky vpředu na hrudi, takže mají pití po ruce. Vhodné vesty najdete v <a href="/bezecke-vesty-a-batohy/">běžeckých vestách a batozích</a>, nosné řešení pro trasy pak v <a href="/turisticke-batohy/">turistických batozích</a>.</p>'
          '<h2>Objem: kolik vody s sebou</h2>'
          '<p>Nejde o jediné univerzální číslo, protože potřeba pití závisí na teplotě, námaze a také na tom, jak snadno doplníte zásoby po cestě. Na krátkou procházku s dostupným doplněním stačí malá láhev. Na celodenní túru s několika hodinami bez pramene je třeba počítat s větším objemem, případně s rezervní lahví nebo filtrem na vodu. Při delší akci ve vedru je lepší nést více menších nádob než jednu velkou, protože se dají rozdělit do batohu a jedna rozlitá nezničí celý přísun. Mějte na paměti, že každý litr vody váží kilogram, což se na dlouhé trase projeví.</p>'
          '<h2>Láhve podle sportu</h2>'
          '<ul><li><strong>Cyklistika:</strong> láhev musí zapadnout do držáku, snadno se otevírat a nesmí unikat při otřesech. Kdo jezdí delší trasy, bere dvě.</li>'
          '<li><strong>Běh:</strong> ruční láhev s poutkem nebo vesta s měkkými flaskami. Pozor na přenášení váhy v jedné ruce při delším běhu.</li>'
          '<li><strong>Turistika a trek:</strong> širokohrdlé láhve se hodí k doplňování z pramenů a k úpravě vody, viz <a href="/hygiena-a-repelenty/">hygiena, repelenty a úprava vody</a>.</li>'
          '<li><strong>Posilovna:</strong> šejkr s mixážní kuličkou rozmíchá <a href="/proteiny/">protein</a> a <a href="/kreatin/">kreatin</a>.</li>'
          '<li><strong>Kemping:</strong> větší nádoby a kanystry doplní <a href="/kempingove-nadobi/">kempingové nádobí</a> a <a href="/vareni-v-prirode/">vaření v přírodě</a>.</li></ul>'
          '<h2>Děti a škola</h2>'
          '<p>Dětská láhev musí být hlavně těsná a odolná proti pádům. Slámkové víčko nebo víčko s pitným otvorem usnadní pití, ale rodič by měl ověřit, že se dá rozebrat a umýt, protože v zákoutí se rychle usadí zbytky šťávy. Barva a motiv motivují k pití, přesto neplatí, že nejdražší je nejlepší. Pro školní batoh se hodí tvar, který se vejde do bočního kapsy, viz <a href="/skolni-batohy/">školní batohy</a>. Pokud dítě nosí sladké nápoje, zvolte materiál, který nepohlcuje pachy.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejčastěji nabízené jsou ' + B(('laken', 'Laken'), ('thermos', 'Thermos'), ('camelbak', 'Camelbak'), ('nalgene', 'Nalgene'), ('primus', 'Primus'), ('b-box', 'B.box'), ('kambukka', 'Kambukka'), ('thermocafe', 'THERMOcafé')) + '. Thermos je tradiční název pro termosky. Camelbak je spojený s hydrovaky a sportovními lahvemi. Nalgene se prosadil širokými plastovými lahvemi do outdoorové výbavy. Laken, Primus a Kambukka nabízejí nerezové a turistické varianty. Mezi cyklistickými doplňky najdete ' + B(('rockbros', 'Rockbros'), ('topeak', 'Topeak'), ('force', 'Force'), ('fidlock', 'Fidlock')) + ', například láhve a držáky.</p>'
          '<h2>Bezpečnost a hygiena nápoje</h2>'
          '<p>Na sport lijte do láhve vodu nebo ředěný iontový nápoj, který se nehodí nechávat dlouho stát. Sladké a mléčné nápoje se v teplé láhvi kazí rychleji. Při pití z pramenů a potoků vodu upravte filtrem nebo tabletami, na něž slouží kategorie <a href="/hygiena-a-repelenty/">hygiena, repelenty a úprava vody</a>. Dbejte na to, aby láhev nezůstala dlouho v horkém autě, kde se může zahřát a změnit chuť. Pokud se láhev používá více lidmi, každý by měl mít vlastní víčko.</p>'
          '<h2>Čištění a péče</h2>'
          '<p>Láhev se myje po každém použití. Rozeberte víčko, vyjměte těsnění a propláchněte všechny části. Hrdlo vyčistíte kartáčem na láhve, na slámku se hodí úzký kartáček. Zápach se odstraní sodou rozpuštěnou ve vodě, případně octovým roztokem, který nechte působit a pak důkladně vypláchněte. Termosky myjte ručně, protože horká voda a mycí prostředky v myčce můžou poškodit vnější povrch nebo těsnění. Po umytí nechte láhev odkrytou a obrácenou, aby uschla, jinak v ní zůstává vlhkost. Starší těsnění vyměňte, pokud je popraskané nebo trvale zapáchá.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Pořídit si těžkou nerezovou láhev na běh, kde každé gramy vadí.</li>'
          '<li>Koupit termosku s úzkým hrdlem a pak do ní chtít nalévat polévku.</li>'
          '<li>Nalévat do láhve sycené nápoje, na které není určená.</li>'
          '<li>Zapomenout na to, že se láhev musí vejít do držáku nebo batohu.</li>'
          '<li>Nečistit víčko a těsnění, kde se tvoří plíseň.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Porovnáte nabídky více obchodů vedle sebe a zjistíte, který model je právě dostupný v požadované barvě a objemu. Hledání zúžíte podle značky. Navazující kategorie jsou <a href="/outdoor-doplnky/">outdoorové doplňky</a>, <a href="/cyklo-lahve-a-drzaky/">cyklistické láhve a držáky</a>, <a href="/chladici-boxy/">chladicí boxy</a> a <a href="/kemping/">kemping</a>.</p>',
    faq=[('Jaká láhev je nejlepší na sport?', 'Lehká, těsná a s víčkem, které se otevírá jednou rukou. Na běh a kolo se hodí plast nebo tritan, na posilovnu šejkr, na turistiku širokohrdlá láhev nebo hydrovak.'),
         ('Jak dlouho termoska drží teplo?', 'Doba závisí na kvalitě vakuové vrstvy, víčku a objemu. Větší objem drží teplotu déle než malý. Předehřátí horkou vodou prodlouží udržení tepla.'),
         ('Mohu do termosky nalít sycený nápoj?', 'Nedoporučuje se. Plyn vytváří tlak, který může vystřelit uzávěr nebo poškodit těsnění. Termosky se plní vodou, čajem, kávou nebo polévkou podle určení.'),
         ('Jak odstranit zápach z láhve?', 'Naplňte ji teplou vodou se sodou nebo octem, nechte působit a pak důkladně vypláchněte. Pomůže i rozebrat víčko a vyčistit těsnění kartáčem.'),
         ('Dá se láhev mýt v myčce?', 'Záleží na materiálu a pokynech výrobce. Plastové a nerezové láhve bývají označené, termosky se většinou myjí ručně, protože myčka může poškodit povrch a těsnění.'),
         ('Co je lepší, hydrovak nebo láhev?', 'Hydrovak umožňuje pít bez zastavení a je pohodlný na trail a kolo. Láhev se snáze plní, čistí a kontroluje se množství. Mnoho lidí používá kombinaci.'),
         ('Kolik vody s sebou na túru?', 'Podle teploty, délky trasy a dostupnosti pramenů. Na delší túru je lepší mít rezervu a znát místa, kde lze vodu doplnit nebo upravit filtrem.'),
         ('Jaký materiál je pro děti nejlepší?', 'Odolný plast nebo nerez s těsným víčkem, které se dá rozebrat a umýt. Sklo je pro školní batoh méně praktické, protože hrozí rozbití.'),
         ('Jak vybrat láhev na kolo?', 'Musí zapadnout do držáku, mít ventilové víčko a snadno se mačkat. Měkká láhev je pohodlnější, avšak rigidní nerezová drží teplotu déle.'),
         ('Jak pečovat o těsnění?', 'Po každém umytí je vyjměte, nechte uschnout a pravidelně kontrolujte. Při popraskání nebo zápachu je vyměňte, těsnění je levnější než celá láhev.'),
         ('Jaké láhve zvolit do kanceláře?', 'Nerezovou nebo skleněnou s těsným víčkem a širším hrdlem, které se snadno čistí. Při přenášení v tašce je důležité, aby víčko nepropouštělo.')],
)

# ------------------------------------------------------------------ nakrcniky-a-satky
NEW['nakrcniky-a-satky'] = dict(long=True,
    title='Nákrčníky a kukly: multifunkční šátky a výběr | Sporteka',
    desc='Multifunkční nákrčníky, šátky, kukly a čelenky pro zimu, kolo, běh i hory. Průvodce materiály, použitím a péčí a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Nákrčník</strong> je kus látky v kroužku, který umí být šálou, čepicí, čelenkou, rouškou na obličej i kuklou. Váží zlomek bundy, vejde se do kapsy a řeší chlad, vítr i slunce. Právě proto skončil v batohu běžců, cyklistů, lyžařů, rybářů i lidí, kteří jen venčí psa za ranního mrazu.</p>'
          '<p>Na Sportece najdete <strong>nákrčníky, multifunkční šátky, kukly a čelenky</strong> z českých obchodů a u každého kusu porovnáte nabídky vedle sebe. Přehled doplňujeme o <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>, <a href="/merino-doplnky/">merino doplňky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a>. Níže se dozvíte, který materiál vybrat na běh, lyže nebo kolo, jak nákrčník nosit, jak ho prát a čeho se při nákupu vyvarovat.</p>',
    guide='<h2>K čemu se nákrčník hodí</h2>'
          '<p>Nákrčník funguje na principu vrstvení. Teplo uniká nejvíc tam, kde je vrstva tenká a kde proudí vzduch, a krk je pro to typický příklad. Obyčejný šál se často rozmotá, uvolní se a navíc vadí pod bundou. Nákrčník se naopak navleče, drží tvar a nikam se nerozmotá. Díky tomu jej oblíbili sportovci, ale také lidé na cestu do práce.</p>'
          + T(['Aktivita', 'Co je důležité', 'Vhodný typ'], [
              ['Zimní běh', 'prodyšnost, rychlé schnutí', 'tenký syntetický nebo merino nákrčník'],
              ['Lyžování a snowboard', 'teplo, ochrana proti větru', 'fleece nebo silnější merino, někdy s kuklou, viz <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>'],
              ['Kolo za chladu', 'ochrana krku a uší pod helmou', 'tenký nákrčník nebo čepice pod <a href="/cyklisticke-helmy/">cyklistickou helmu</a>'],
              ['Léto, slunce, prach', 'UV ochrana, prodyšnost, lehkost', 'lehký bezešvý šátek z hladké látky'],
              ['Rybaření a lov', 'neviditelnost, teplo při nehybnosti', 'tlumená barva, vrstvená nebo flísová varianta'],
              ['Motorky a rychlá jízda', 'ochrana tváře před větrem', 'delší nákrčník nebo kukla bez švů']]) +
          '<h2>Co je nákrčník a čím se liší od kukly a šály</h2>'
          '<p>Klasický nákrčník je bezešvá trubice, kterou lze nosit mnoha způsoby. Kukla je střižená tak, aby kryla hlavu a krk a zanechala otvor pro oči nebo obličej. Hodí se pod helmu, do mrazu a do větru, kde nestačí čepice. Šála je dlouhá a může být pohodlná na procházky, ale při pohybu a rychlosti se uvolňuje, někdy i nebezpečně. Čelenka kryje jen uši a čelo, což se hodí pro mírný chlad nebo namáhavé aktivity, při nichž se hlava rychle zahřeje. Multifunkční šátek v praxi nahradí všechny čtyři, jen ne tak dobře jako specializovaná varianta.</p>'
          '<h2>Materiály a jejich vlastnosti</h2>'
          '<ul><li><strong>Merino vlna</strong> hřeje i vlhká, příliš nezapáchá a příjemně se nosí na kůži. Je dražší na údržbu a obecně méně odolná vůči otěru. Více v kategorii <a href="/merino-doplnky/">merino doplňky</a>.</li>'
          '<li><strong>Polyester a mikrovlákno</strong> rychle schnou, odvádějí vlhkost a snášejí časté praní. Při intenzivním potu ale mohou zapáchat.</li>'
          '<li><strong>Fleece</strong> je hřejivý, měkký a rychle schne, ale méně chrání proti silnému větru.</li>'
          '<li><strong>Bavlna</strong> je příjemná na dotek a vhodná pro volný čas, při sportu ale nasákne a zchladí.</li>'
          '<li><strong>Kombinace materiálů</strong> často spojují teplou a prodyšnou vrstvu: například flís vpředu a tenký šátek vzadu.</li>'
          '<li><strong>Technické úpravy</strong> mohou zahrnovat UV filtr nebo antibakteriální vlákno. Zkontrolujte přesný popis výrobce.</li></ul>'
          '<h2>Jak nákrčník nosit</h2>'
          '<p>Možností je víc než zdá. Nejprostší je navléknout ho na krk a zakrýt si bradu. Přetažením přes nos a pusu vznikne ochrana před studeným větrem. Dvojitým omotáním získáte silnější vrstvu na krku. Přetažením přes hlavu se promění v čepici a zavázáním zadního okraje v pirátský šátek. Čelenka vznikne složením a narolováním látky. Pod helmou je nejpohodlnější tenká verze, která netvoří záhyby a netlačí na čelo. Pokud nosíte brýle, nasaďte nákrčník tak, aby dech nestoupal k čočkám, jinak se zamlží. V kategorii <a href="/lyzarske-bryle/">lyžařských brýlí</a> a <a href="/sportovni-bryle/">sportovních brýlí</a> najdete modely s lepším odvětráním.</p>'
          '<h2>Zima, sníh a mráz</h2>'
          '<p>V zimě je nákrčník především ochrana proti větru a vlhkosti. Při běžeckém lyžování nebo běhu v mrazu je dech přes materiál vlhký a látka brzy navlhne. Proto mějte se sebou druhý kus na výměnu, zejména na delší výpravy. Na svah se hodí varianta s flísovou vrstvou, která drží teplo a nepřekáží pod <a href="/lyzarske-helmy/">lyžařskou helmou</a>. Pro běžky a výlety v chladu viz <a href="/bezecke-lyzovani/">běžecké lyžování</a>. Přehled ostatní zimní výbavy najdete v kategorii <a href="/zimni-sporty/">zimní sporty</a>, kde navazují <a href="/lyzarske-rukavice/">lyžařské rukavice</a> a <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<h2>Jaro, léto a podzim</h2>'
          '<p>V teplém počasí slouží tenký šátek jako ochrana proti slunci a prachu. Namočený v chladné vodě umí krk během horké túry příjemně zchladit. Při jízdě na kole nebo motorce chrání obličej před hmyzem a prachem. Na túru s deštěm se hodí materiál, který rychle schne, a na táborový večer pak teplejší varianta. Pro slunce a vodu najdete další pomůcky v <a href="/lycra-a-uv-tricka/">lycře a UV tričkách</a> a v <a href="/plazove-doplnky/">plážových doplňcích</a>.</p>'
          '<h2>Velikost, délka a střih</h2>'
          '<p>Většina nákrčníků má univerzální velikost a díky pružnosti sedí všem. Rozdíl je v délce: kratší se hodí na krk, delší lze přetáhnout přes hlavu nebo omotat dvakrát. Dětské verze jsou menší, aby nepřekážely a nesklouzávaly. Kukla má pevnější střih a měla by dobře padnout na hlavu, aniž by tlačila na uši. Pokud nosíte helmu, zkuste ji spolu s kuklou, protože spojená tloušťka někdy změní, jak helma sedí. Správně zvolená vrstva nesmí nikdy omezovat dýchání ani výhled.</p>'
          '<h2>Pro koho se nákrčník vybírá</h2>'
          '<ul><li><strong>Běžci a trailaři:</strong> tenký a prodyšný, který se dá stáhnout na krk, když se zahřejete.</li>'
          '<li><strong>Cyklisté:</strong> tenká varianta pod helmu, případně <a href="/cyklisticke-navleky/">cyklistické návleky</a> a rukavice pro zbytek těla.</li>'
          '<li><strong>Lyžaři a snowboardisté:</strong> teplejší a vyšší, často s fleecem nebo merinem.</li>'
          '<li><strong>Turisté:</strong> univerzální šátek, který se hodí na slunce, vítr i do spacáku.</li>'
          '<li><strong>Rybáři a lovci:</strong> tlumené barvy a tichý materiál, viz <a href="/rybareni/">rybaření</a> a <a href="/lov-a-priroda/">lov a příroda</a>.</li>'
          '<li><strong>Děti:</strong> měkký, bez švů, který nedráždí pokožku.</li></ul>'
          '<h2>Kukly a ochrana obličeje</h2>'
          '<p>Kukla se vyplatí v silném mrazu, kdy čepice a nákrčník samy nestačí. Chrání bradu, tváře a uši a nezanechává mezeru mezi čepicí a límcem. Při větru a rychlosti, třeba na běžkách nebo skútru, je rozdíl patrný hned. Obličejový otvor má být dost velký, aby neomezoval výhled, a materiál kolem nosu prodyšný. V extrémně nízkých teplotách hrozí omrzliny, proto sledujte pokožku tváří a nosu a při bělení či ztrátě citlivosti se ukryjte do tepla.</p>'
          '<h2>Co mít v batohu a jak vrstvit</h2>'
          '<p>Vrstvení vychází z jednoduchého pravidla: spodní vrstva odvádí pot, střední hřeje, vnější chrání před větrem. Nákrčník patří do první a druhé vrstvy a snadno se přidá nebo sundá. Na túru či lyže berte jeden tenký a jeden teplý, který lze vyměnit, když zvlhne. Nezapomeňte na <a href="/termopradlo/">termoprádlo</a>, <a href="/sportovni-rukavice/">rukavice</a> a <a href="/cepice-a-celenky/">čepici</a>. Takový komplet váží málo a výrazně zvyšuje komfort, takže se hodí i při krátkých vycházkách v nejistém počasí. Na delší horskou akci se zkombinuje s <a href="/turisticke-batohy/">turistickým batohem</a> a mapou.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce jsou nejčastěji ' + B(('buff', 'Buff'), ('finmark', 'Finmark'), ('viking', 'Viking'), ('barts', 'Barts'), ('rockbros', 'Rockbros'), ('new-era', 'New Era')) + '. Buff je rozšířená značka multifunkčních šátků, Finmark a Viking pokrývají outdoorové zimní doplňky. Rothco a Mil-tec nabízejí armádní styl, ' + B(('rothco', 'Rothco'), ('mil-tec', 'Mil-tec®'), ('mfh', 'Mfh')) + ' mají typické vojenské barvy a materiály. Rockbros je silný v cyklistice. Značka sama o ničem nerozhoduje, kontrolujte materiál a střih konkrétního kusu. Dobré je přečíst si i složení a doporučené použití, protože dva nákrčníky podobného vzhledu se mohou chovat úplně jinak, jeden jako tenká letní ochrana a druhý jako hřejivá zimní vrstva do mrazu.</p>'
          '<h2>Péče a praní</h2>'
          '<p>Nákrčníky z umělých vláken snesou běžné praní, ideálně při nižší teplotě, bez aviváže, která zhoršuje odvádění vlhkosti. Merino perte jemným programem a sušte rozložené, ne na radiátoru. Fleece nežehlete a vyvarujte se vysokých teplot. Pokud si nákrčník nasazujete před obličej, perte ho častěji, protože na něm zůstává pot, dech a kosmetika. U kuklí zkontrolujte, zda je tvar po vyprání stabilní. Při skladování se vyvarujte tlaku, protože některé tenké materiály se vymačkají a ztratí pružnost.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Zvolit bavlněný nákrčník na sport, který namokne a studí.</li>'
          '<li>Kupovat příliš silný nákrčník na běh, ve kterém se člověk přehřeje.</li>'
          '<li>Zapomenout, že nákrčník pod helmou nesmí tvořit záhyby.</li>'
          '<li>Dýchat vlhkým vzduchem do jedné vrstvy a nevyměnit ji na delší výpravě.</li>'
          '<li>Považovat jakýkoli šátek za náhradu zdravotnické roušky nebo ochranného prostředku bez ověření určení.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého kusu vidíte nabídky více obchodů, takže snadno najdete barvu nebo vzor, které jsou právě skladem. Vybírejte podle materiálu a použití, ne jen podle vzoru. Pro další hlavové a krční doplňky pokračujte v kategoriích <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/merino-doplnky/">merino doplňky</a>, <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a>.</p>',
    faq=[('Co je to nákrčník a k čemu slouží?', 'Je to bezešvá trubice z elastické látky, kterou lze nosit jako šálu, čepici, čelenku nebo kuklu. Chrání krk a obličej před chladem, větrem, sluncem a prachem.'),
         ('Jaký materiál nákrčníku vybrat?', 'Na sport merino nebo polyester, na zimu fleece nebo silnější merino, pro volný čas i bavlna. Bavlna při sportu nasákne a chladí, proto se pro aktivity moc nehodí.'),
         ('Čím se liší nákrčník od kukly?', 'Kukla je střižená tak, aby kryla hlavu a krk a ponechala otvor pro obličej. Nákrčník je jednoduchá trubice, kterou lze složit a nosit různě. Pod helmu se lépe hodí kukla.'),
         ('Jak nosit nákrčník pod helmou?', 'Zvolte tenkou variantu bez záhybů. Přetáhněte ji přes hlavu nebo jen přes krk a zkuste helmu nasadit tak, aby nic netlačilo na čelo a uši.'),
         ('Hodí se nákrčník na běh?', 'Ano, pokud je tenký, prodyšný a rychle schnoucí. Při zahřátí ho stáhnete na krk. Silný fleece je na běh většinou zbytečně teplý.'),
         ('Chrání nákrčník před sluncem?', 'Některé modely mají UV ochranu, což výrobce uvádí v popisu. Látka pokožku jen částečně stíní a bez UV filtru před popálením nechrání, proto v silném slunci použijte i opalovací krém.'),
         ('Jak prát nákrčník?', 'Syntetické a fleece perte na nižší teplotu bez aviváže, merino jemným programem a sušte rozložené. Vyhněte se radiátorům, které poškozují elastická vlákna.'),
         ('Zamlžují se mi brýle, když nosím nákrčník. Co s tím?', 'Dech proudí vzhůru kolem nosu. Pomůže nasadit nákrčník pevněji pod nos, zvolit brýle s lepším odvětráním nebo kombinaci s kuklou, která dech odvádí jinam.'),
         ('Jaký nákrčník pro děti?', 'Měkký a bez švů, kratší a z nedráždivého materiálu. Měl by dobře sedět na krku a nesklouzávat, aby dítě nemuselo stále upravovat.'),
         ('Kolik nákrčníků je dobré mít?', 'Pro běžné použití stačí jeden tenký a jeden teplejší. Kdo sportuje v mrazu, vezme si i náhradní, protože zvlhlá látka zábranu proti chladu ztrácí.'),
         ('Kde jinde najdu doplňky pro hlavu a krk?', 'V kategoriích čepice a čelenky, merino doplňky, lyžařské čepice a nákrčníky a sportovní rukavice. V zimní sezóně pomůže i kategorie zimní sporty.')],
)
