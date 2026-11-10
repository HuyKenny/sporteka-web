"""sporteka.cz — wave 18e (4. 11. 2026): long texts (>= 1650 words) for lyzarske-ponozky, tenis, badminton, boxovaci-pytle.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-ponozky
NEW['lyzarske-ponozky'] = dict(long=True,
    title='Lyžařské ponožky: merino, syntetika, výběr',
    desc='Lyžařské ponožky na sjezdovky, skialpy i běžky. Merino, syntetika, výška, zesílení a péče. Porovnejte nabídku českých obchodů na jednom místě.',
    intro='<p>Mezi vším, co si berete na svah, mají <strong>lyžařské ponožky</strong> nejmenší objem a překvapivě velký vliv na to, jak se vám bude celý den lyžovat. V pevné skořepině boty nemá noha kam uhnout, a tak každý záhyb látky, tlustý šev nebo promočené vlákno okamžitě pocítíte jako tlak, puchýř či studené prsty. '
          'Správný pár naopak odvádí vlhkost, drží tvar a téměř si ho nevšimnete.</p>'
          '<p>Na Sportece vedle sebe porovnáte nabídky českých obchodů a snadno najdete svou velikost i tloušťku. K ponožkám se hodí <a href="/lyzarske-boty/">lyžařské boty</a>, <a href="/lyzarske-termopradlo/">termoprádlo</a> a celé <a href="/lyzarske-obleceni/">lyžařské oblečení</a>. '
          'Níže vysvětlíme materiály, výšku, zesílení i péči a pomůžeme s výběrem podle disciplíny.</p>',
    guide='<h2>Čím se lyžařská ponožka liší od běžné</h2>'
          '<p>Obyčejná sportovní ponožka počítá s volným prostorem v botě a s lehkým pohybem nohy. Lyžařská bota je ale tuhá, vypodložená a utažená přezkami, takže se ponožka musí chovat jinak. Bývá delší, tenčí v místech, kde bota tlačí, a naopak zesílená tam, kde se noha opírá nebo se tře o skořepinu. '
          'Cílem není teplo za každou cenu, ale stabilní mikroklima: suché chodidlo, které se nepohybuje.</p>'
          '<p>Kategorie zahrnuje několik typů, které se hodí do různé obuvi i tempa jízdy.</p>'
          + T(['Typ ponožky', 'Pro koho a kam', 'Na co dát pozor'], [
              ['Tenká sjezdová', 'sportovní jízda, těsné závodní boty', 'minimum švů, přesné zesílení holeně'],
              ['Střední univerzální', 'rekreační lyžování celý den', 'dobrá výška, pružný zvedák kotníku'],
              ['Hřejivější s vyšším podílem vlny', 'nemrznoucí lidé, dlouhé stání ve frontě', 'nesmí tlačit v prstech'],
              ['Skialpová', 'výstup i sjezd v jednom páru', 'rychle schne, snese opakované praní'],
              ['Běžkařská', 'klasika a bruslení, měkčí boty', 'tenčí, bez výrazných zesílení'],
              ['Snowboardová', 'měkčí boty, jiná zátěž holeně', 'střední až vyšší vlněné zesílení']]) +
          '<h2>Materiály a jejich chování</h2>'
          '<p>Základ určuje, jak se ponožka vypořádá s potem. Bavlna se nasákne, dlouho schne a vlhkost ponechává u kůže, proto se na svah nehodí. Z přírodních vláken se používá hlavně <a href="/merino/">merino</a>, ze syntetických polyamid, polyester a elastan. Většina kvalitních modelů je směs, která spojuje výhody obou skupin.</p>'
          + T(['Materiál', 'Výhody', 'Slabší stránky'], [
              ['Merino vlna', 'hřeje i za vlhka, pomaleji začne zapáchat, příjemný dotyk', 'bývá trochu méně odolná při velkém tření'],
              ['Polyamid a polyester', 'odolnost, rychlé schnutí, pevný tvar', 'u levnějších kusů se rychleji projeví pach'],
              ['Elastan a lycra', 'drží ponožku na místě, přizpůsobí se noze', 've směsi jen malý podíl, sám nehřeje'],
              ['Bambusová a celulózová vlákna', 'měkké na dotek', 'kratší životnost při tvrdém lyžování'],
              ['Bavlna', 'běžně dostupná', 'promáčí se a chladí, na lyže nevhodná']]) +
          '<p>Chcete-li si ponožku vybrat podle vlastního stylu, myslete na délku dne. Při několika hodinách na sjezdovce stačí vyvážená směs. Při celodenním výstupu s lyžemi na zádech ocení většina lidí merino s příměsí syntetiky, protože po cestě nahoru se noha zapotí a při sjezdu přijde chlad. Více merino variant najdete také v kategorii <a href="/merino-ponozky/">merino ponožky</a>.</p>'
          '<h2>Výška, zesílení a střih</h2>'
          '<h3>Délka</h3>'
          '<p>Sjezdová ponožka má sahat pod koleno, minimálně ale nad okraj boty. Pokud se jazyk boty dotýká holého místa nebo rozhraní ponožky, vznikne tření, které může vést k odřeninám. Příliš krátká ponožka se navíc rádo svine do kotníku.</p>'
          '<h3>Zesílené zóny</h3>'
          '<p>Výrobci vyztužují přední hranu holeně, patu a někdy i špičku, zatímco nárt a chodidlo nechávají tenčí. Tenčí nárt zabraňuje tlaku pod přezkami. Anatomicky tvarované modely se prodávají jako levá a pravá, což se pozná podle značky L a R.</p>'
          '<h3>Švy a pletení</h3>'
          '<p>Špičkový šev bývá ploše spojený, aby netlačil na prsty. Zkontrolujte ho prstem zevnitř. Pleteniny s vyšší hustotou drží tvar, ale hůř prodýchávají, proto jemnější pletení patří na teplejší lyžování.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<ul>'
          '<li><strong>Sjezdové lyžování:</strong> tenčí až střední ponožky do <a href="/sjezdove-lyze/">sjezdových</a> bot. Klíčová je přesná velikost, aby se nevytvořily záhyby.</li>'
          '<li><strong>Skialpinismus:</strong> lehká a rychleschnoucí směs, která snese dlouhý pobyt na stoupacích a sjezd po něm. Vybavení pro tento obor shrnuje <a href="/skialpinismus/">skialpinismus</a> a boty <a href="/skialpove-boty/">skialpové boty</a>.</li>'
          '<li><strong>Běžecké lyžování:</strong> boty jsou měkčí a těsněji přiléhají. Zvolte tenčí ponožku bez výrazných zesílení, viz <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</li>'
          '<li><strong>Snowboard:</strong> boty jsou vypolstrované a zatěžují nohu jinak, proto se ponožka s mírným zesílením hodí. Navazují <a href="/snowboardove-boty/">snowboardové boty</a> a obecně <a href="/snowboarding/">snowboarding</a>.</li>'
          '<li><strong>Děti:</strong> tenké ponožky stejné konstrukce jako dospělé, jen v menší velikosti. Netlačící gumy a hladké švy jsou důležitější než silná vrstva.</li>'
          '</ul>'
          '<h2>Jak velkou ponožku koupit</h2>'
          '<p>Velikosti se uvádějí v rozsazích, například 39–42. Pokud jste na hranici dvou rozsahů, vezměte menší pro těsně sedící lyžáky a větší pro volnější nebo měkké boty. Ponožka musí přiléhat jako druhá kůže, ale nesmí tlačit v palci. Zkoušejte ji vždy v botě, do které půjde, a postavte se do lyžařského postoje. V takové pozici se záhyby projeví okamžitě.</p>'
          '<p>Nezapomínejte, že ponožka je jen část systému. K teplu přispívá <a href="/lyzarske-termopradlo/">termoprádlo</a>, rukavice, čepice a nákrčník. Pokud se vám přesto hodně potí chodidla, může pomoct sušení bot přes noc a vložky z kategorie <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul>'
          '<li><strong>Dva páry ponožek přes sebe.</strong> Tlustá vrstva zmenší prostor v botě, zhoršuje prokrvení a ruší funkci odvodu vlhkosti. Jeden vhodný pár je lepší.</li>'
          '<li><strong>Bavlněné ponožky z domova.</strong> Zvlhnou a chladí. Teplota klesá hlavně při sjezdu.</li>'
          '<li><strong>Příliš silná ponožka kvůli zimě.</strong> Omezený krevní oběh studí víc než tenká, ale dobře padnoucí.</li>'
          '<li><strong>Záhyby na patě a nártu.</strong> Dobré ponožky po natažení sedí bez vln. Když ne, zvolte jinou velikost.</li>'
          '<li><strong>Jedna ponožka pro vše.</strong> Skialpová ponožka na stoupání se liší od ponožky pro tvrdý závodní sjezd.</li>'
          '<li><strong>Praní s aviváží.</strong> Změkčovadlo se usadí na vláknech a zhorší odvod vlhkosti.</li>'
          '</ul>'
          '<h2>Péče a životnost</h2>'
          '<p>Ponožky perte podle štítku, nejlépe v pračce na šetrný program a obrácené naruby. Aviváž nepoužívejte. Merino nesušte na radiátoru ani v sušičce na vysokou teplotu, hrozí smrštění. Po lyžování je vyvěste, ať se zbaví zbytkové vlhkosti, a před dalším výjezdem zkontrolujte pleteninu na patě. '
          'Prořídlé místo se projeví tenčí látkou proti světlu a je čas na novou dvojici. Pár držte pohromadě a nezaměňujte mezi sebou levé a pravé kusy.</p>'
          '<h2>Řešení typických potíží</h2>'
          '<p>Většina problémů v lyžařské botě se dá pojmenovat a vyřešit právě volbou ponožky. Než začnete měnit boty, projděte si, co vám na noze vadí.</p>'
          + T(['Potíž', 'Pravděpodobná příčina', 'Co zkusit'], [
              ['Puchýře na patě', 'ponožka se pohybuje nebo dělá záhyby', 'užší střih, elastanový podíl, přesnější velikost'],
              ['Zimní prsty při sjezdu', 'tlak přezek, silná ponožka, vlhkost', 'tenčí pár, povolit přezky, suché boty'],
              ['Pálení na holeni', 'tření jazyka boty o ponožku', 'delší ponožka se zesílenou přední hranou'],
              ['Zápach po dni na sněhu', 'syntetika bez ošetření, málo větrání', 'směs s merinem, vyvěšování po sjezdu'],
              ['Ponožka sjíždí do špičky', 'příliš velká velikost nebo slabá guma', 'menší velikost, model s pevným lemem'],
              ['Prodřená pata po pár výjezdech', 'tenká pleteninou bez zesílení', 'zesílená pata, rotace více párů']]) +
          '<p>Pokud se obtíže vracejí i s ideální ponožkou, příčina je spíš v botě. V takovém případě se nechte poradit v prodejně lyžařských bot, kde boty případně roztáhnou nebo upraví. Samotná ponožka vadný tvar skořepiny nevyřeší.</p>'
          '<h2>Jak ponožku vyzkoušet</h2>'
          '<p>Ponožku nasaďte v klidu, vyhlaďte ji od prstů až po koleno a ověřte, že pata sedí přesně v místě zesílení. Poté ji v botě zkuste při předklonu a při zdvihu paty. Pokud cítíte tlak na nártu nebo záhyb u palce, zvolte jiný střih. Před delším výjezdem vyzkoušejte ponožku na půldenní lyžování, nikoli až na týdenním zájezdu. Pokud se po prvním dni objeví červená místa, nechte nohu odpočinout a příště zvolte jinou velikost.</p>'
          '<h2>Rotace párů a cestování</h2>'
          '<p>Na týdenní pobyt se vyplatí vzít tři až pět párů. Střídáním se snižuje opotřebení a každý pár má čas vyschnout. Na cesty je vhodné mít jeden náhradní pár v batohu, aby se dalo převléknout po dlouhém výstupu nebo po pádu do sněhu. Ponožky dobře odvětrávejte, nesušte je přímo u kamen a nevkládejte je do bot, dokud nevychladnou. Při dlouhé cestě autem je zabalte odděleně od mokrého oblečení.</p>'
          '<h2>Zimní túry a jiné použití</h2>'
          '<p>Vyšší lyžařská ponožka se osvědčí i při zimní turistice, sněžnicích, bruslení či práci venku. Pokud budete chodit v turistické obuvi, hledejte spíš modely z kategorie <a href="/sportovni-ponozky/">sportovní ponožky</a>. Pro chladné dny v běžném životě je lyžařská ponožka často zbytečně dlouhá, ale na vysoké zimní boty z kategorie <a href="/zimni-obuv/">zimní obuv</a> se hodí dobře.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>V nabídce obchodů najdete mimo jiné značky ' + B(('lasting', 'Lasting'), ('smartwool', 'Smartwool'), ('icebreaker', 'Icebreaker'), ('relax', 'Relax'), ('rossignol', 'Rossignol'), ('accezzi', 'Accezzi'), ('falke', 'Falke'), ('cep', 'Cep'), ('nordica', 'Nordica'), ('blizzard', 'Blizzard')) + '. '
          'Rozdíly mezi nimi se týkají hlavně střihu, poměru vlny a zesílení, proto neporovnávejte jen jméno, ale i popis materiálu.</p>'
          '<h2>Co dalšího se hodí na svah</h2>'
          '<p>Sestavujete-li komplet, myslete i na <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, <a href="/lyzarske-kalhoty/">kalhoty</a> a <a href="/lyzarske-doplnky/">lyžařské doplňky</a>. Širší rozcestník s výběrem pro sezonu je kategorie <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<h2>Kdy nakupovat a jak porovnat nabídky</h2>'
          '<p>Ponožky se kupují snadno online, protože se nemusejí zkoušet tak důkladně jako boty. Přesto ověřte velikostní tabulku konkrétního výrobce, protože rozsahy se liší. Na Sportece vidíte u stejného produktu více obchodů, jejich dostupnost velikostí i dopravu. Pokud se nehodí první vybraný pár, zjistíte alternativu hned v sousední nabídce.</p>',
    faq=[
        ('Jaké ponožky do lyžařských bot?', 'Vysoké, tenčí až střední, z merina nebo syntetiky se zesílením na holeni. Bavlně se vyhněte, protože zadržuje vlhkost.'),
        ('Je lepší merino, nebo syntetika?', 'Merino hřeje i vlhké a pomaleji zapáchá, syntetika rychleji schne a lépe snáší tření. Nejlepší jsou obvykle směsi obou vláken.'),
        ('Mohu si vzít dvě ponožky přes sebe?', 'Nedoporučuje se. Dvě vrstvy zmenšují prostor v botě, tlačí a zhoršují odvod potu. Chodidlo se pak spíš zapotí a zmrzne.'),
        ('Jak vysoká má být lyžařská ponožka?', 'Musí sahat výrazně nad okraj boty, tedy pod koleno. Díky tomu se jazyk boty nedře o holou kůži.'),
        ('Proč mě v lyžácích studí prsty, i když mám teplou ponožku?', 'Často za to může tlak. Příliš silná ponožka nebo těsné přezky stlačí cévy. Zkuste tenčí pár, povolte přezky a nenoste vlhké boty.'),
        ('Liší se ponožky na skialpy od sjezdových?', 'Ano. Skialpová ponožka bývá lehčí a rychleji schne, protože na stoupání zvlhne víc než při sjezdu. Pro jízdu pouze po sjezdovce není nutná.'),
        ('Jak vybrat velikost?', 'Podle tabulky výrobce. Mezi dvěma rozsahy zvolte menší pro těsný lyžák, větší pro volnější bota. Ponožka nesmí dělat záhyby ani tlačit v palci.'),
        ('Jak prát lyžařské ponožky?', 'Šetrně podle štítku, naruby a bez aviváže. Merino nesušte na topení, aby se nesrazilo. Mezi sezónami je uložte suché.'),
        ('Hodí se lyžařské ponožky i na jiné aktivity?', 'Ano, na zimní túry, sněžnice nebo stání v mrazu. Na běžné nošení jsou naopak zbytečně dlouhé a husté.'),
        ('Kdy měnit ponožky za nové?', 'Když se prodřou na patě či špičce, ztratí pružnost nebo začnou sjíždět. Slabá látka proti světlu je jasným znamením.'),
    ])

# ------------------------------------------------------------------ tenis
NEW['tenis'] = dict(long=True,
    title='Tenis: rakety, míče, obuv a oblečení',
    desc='Tenisové vybavení: rakety, struny, míče, tenisová obuv, tašky a oblečení. Průvodce výběrem podle úrovně a srovnání nabídek českých obchodů.',
    intro='<p><strong>Tenis</strong> je hra, kde se vybavení promítá do každého úderu, a přesto stačí pár správných rozhodnutí, aby se hrálo pohodlně a bez zranění. Základ tvoří raketa, která sedí hráči váhou i velikostí hlavy, míče odpovídající povrchu, obuv s oporou pro boční pohyb a taška na přenos. '
          'Zbytek je na zkušenosti a chuti se zlepšovat. Vybíráte-li poprvé, nespěchejte a porovnávejte parametry a vlastní styl hry, ne jen vzhled.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u stovek produktů. Největší podkategorií jsou <a href="/tenisove-rakety/">tenisové rakety</a>, k nim patří <a href="/tenisova-obuv/">tenisová obuv</a>, <a href="/sportovni-tasky/">sportovní tašky</a> a oblečení. Dále najdete tipy, jak vybírat podle věku, úrovně, povrchu a stylu hry.</p>',
    guide='<h2>Co všechno k tenisu patří</h2>'
          '<p>Tenisové vybavení se na první pohled zdá jednoduché: raketa, míč, kurt. Při bližším pohledu se ukáže řada rozhodnutí. Raketa se liší velikostí hlavy, vyvážením, vzorem strunění a pružností rámu. Míče se dělí podle tlaku a určení. Obuv je navržena podle povrchu a oblečení podle pohybu a počasí.</p>'
          + T(['Část výbavy', 'Co řeší', 'Kde hledat'], [
              ['Raketa', 'výkon, kontrola, komfort ruky', '<a href="/tenisove-rakety/">tenisové rakety</a>'],
              ['Struny a gripy', 'cit, odezva, pohodlné držení', 'doplňky u rakety'],
              ['Míče', 'odskok, životnost, povrch', 'tuby po třech či čtyřech kusech'],
              ['Obuv', 'opora a skluz, tlumení', '<a href="/tenisova-obuv/">tenisová obuv</a>, <a href="/tenisky/">tenisky</a>'],
              ['Tašky a batohy', 'přenos rakety, bot a oblečení', '<a href="/sportovni-tasky/">sportovní tašky</a>'],
              ['Oblečení', 'volnost pohybu, odvod potu', '<a href="/sportovni-obleceni/">sportovní oblečení</a>']]) +
          '<h2>Jak vybrat tenisovou raketu</h2>'
          '<p>Raketa je nejdůležitější nákup. Rozhodují čtyři věci: velikost hlavy, váha, vyvážení a tuhost rámu. Velikost hlavy se udává v čtverečních palcích. Větší hlava odpustí nepřesný zásah a dává lehčí výkon, menší nabízí větší kontrolu, ale vyžaduje čistší techniku.</p>'
          + T(['Parametr', 'Co znamená', 'Komu vyhovuje'], [
              ['Větší hlava (103 a více čtverečních palců)', 'větší sweet spot, víc výkonu', 'začátečníci, rekreační hráči'],
              ['Střední hlava (zhruba 98 až 102)', 'kompromis výkonu a kontroly', 'pokročilí rekreační hráči'],
              ['Menší hlava (do 97)', 'přesnost a cit', 'zkušení hráči s dobrou technikou'],
              ['Lehčí raketa', 'snadná manipulace, méně únavy', 'začátečníci, děti, senioři'],
              ['Těžší raketa', 'stabilita při úderu, lepší absorpce', 'silnější hráči s dobrou technikou'],
              ['Vyvážení do hlavy', 'více výkonu, těžší manévrování', 'hráči odspodu kurtu'],
              ['Vyvážení do rukojeti', 'obratnost, rychlé reakce', 'hráči u sítě, čtyřhra']]) +
          '<p>Pro prvních několik týdnů se hodí lehčí raketa s větší hlavou a pohodlným rámem. Zlepšíte se tak dříve, než poznáte vlastní styl. Rakety značky ' + B(('head', 'Head'), ('wilson', 'Wilson'), ('babolat', 'Babolat'), ('dunlop', 'Dunlop'), ('tecnifibre', 'Tecnifibre'), ('prince', 'Prince')) + ' najdete v nabídce, ale zkoušejte podle parametrů, ne podle jména.</p>'
          '<h3>Velikost gripu</h3>'
          '<p>Správná tloušťka rukojeti se pozná tak, že mezi konečky prstů a dlaní zůstane prostor zhruba na šířku prstu. Příliš tenký grip nutí sevřít ruku silněji, příliš tlustý omezuje pohyb zápěstí. Pokud váháte, zvolte menší a nechte ho ztloustnout obalovou páskou.</p>'
          '<h3>Strunění</h3>'
          '<p>Struny určují cit a životnost úderu. Syntetické struny nabízejí dobrý poměr komfortu a ceny, přírodní jsou pružnější a šetrné k loktu, polyesterové mají dlouhou životnost pro razantní hráče, ale jsou tvrdší. Napnutí se udává v kilogramech, vyšší hodnota znamená větší kontrolu a menší výkon.</p>'
          '<h2>Tenisové míče</h2>'
          '<p>Míče se liší tlakem, určením a obalem plsti. Tlakové míče v tubě drží odskok jen omezenou dobu po otevření, bezpřetlakové jsou trvanlivější, ale tvrdší. Pro tvrdé povrchy se vyrábí míče s odolnější plstí, pro antuku citlivější. Děti začínají s pomalejšími míči a menšími kurty, takže jim odskok neutíká a učí se správné technice.</p>'
          '<h2>Tenisová obuv podle povrchu</h2>'
          '<p>Tenisová bota musí zvládat prudké změny směru. Má rozšířenou podešev, výztuhu v oblasti kotníku a podrážku s vhodným vzorem. Běžecká obuv nic z toho nenabízí. Při bočním pohybu se proto doporučuje použít tenisovou obuv, nebo alespoň <a href="/salova-obuv/">sálovou obuv</a>.</p>'
          + T(['Povrch', 'Vhodná podrážka', 'Poznámka'], [
              ['Antuka', 'hustý vzor „rybí kost“ pro skluz', 'čistí se sama při pohybu'],
              ['Tvrdý povrch', 'odolná guma, vyšší tlumení', 'rychleji opotřebuje špičku'],
              ['Tráva', 'drobné výstupky', 'vzácná, zvláštní obuv'],
              ['Hala (koberec)', 'hladší podrážka', 'dávejte pozor na kluzký kontakt']]) +
          '<p>Obuv vyměňte, když podrážka v místě, kde sjíždíte špičkou, ztratí vzor, nebo když se vnitřní vložka sleze. Opotřebovaná bota vás nechá klouzat tam, kde nemá.</p>'
          '<h2>Tašky, oblečení a doplňky</h2>'
          '<p>Taška na rakety chrání rámy před teplotou, nárazy a prachem. Menší batoh pojme jednu až dvě rakety, větší termobag i více kusů, obuv a oblečení. Hledejte samostatnou kapsu na obuv, aby špína nešla do oblečení. Přehled najdete v kategorii <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/batohy/">batohy</a>.</p>'
          '<p>Oblečení má být lehké a prodyšné. Na kurtu se osvědčí tričko z technického materiálu, šortky nebo sukně s kapsou na míček a v chladnu mikina či <a href="/funkcni-mikiny/">funkční mikina</a>. Pro orientaci v sortimentu jsou k dispozici <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/sportovni-sukne-a-saty/">sukně a šaty</a>. K tenisu patří také <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/bandaze-a-ortezy/">bandáže</a>, pokud si je doporučí fyzioterapeut.</p>'
          '<h2>Výběr podle hráče</h2>'
          '<h3>Děti</h3>'
          '<p>Dětské rakety se vyrábějí podle délky. Rozhoduje výška dítěte, nikoli věk. Příliš dlouhá raketa kazí techniku. Pro nejmenší jsou vhodné menší kurty a měkčí míče, aby se hra neproměnila v honičku za míčem.</p>'
          '<h3>Začátečníci a rekreační hráči</h3>'
          '<p>Lehčí raketa s větší hlavou, vybraná podle pocitu v ruce, pomůže rychleji získat jistotu. Praktické je pořídit zároveň obal a několik tub míčů.</p>'
          '<h3>Pokročilí hráči</h3>'
          '<p>Zkušení hráči často přecházejí na menší hlavu a těžší raketu. Měli by znát váhu, vyvážení i napnutí strun, aby mohli dále ladit styl. Dobrou praxí je mít dvě stejné rakety, případně dvě s mírně odlišným strunením.</p>'
          '<h2>Povrchy a styl hry</h2>'
          '<p>Na pomalé antuce míč vyskakuje výš a výměny jsou delší, takže se vyplatí raketa s větším prostorem pro rotaci a pohodlná obuv na skluz. Na rychlém tvrdém povrchu se míč odráží níž a rychleji, což zvýhodňuje rovné údery a dobrý servis. Hráč z lajny obvykle ocení raketu s větší hlavou a vyvážením do hlavy, zatímco hráč, který rád chodí k síti, zvolí obratnější raketu s vyvážením blíž rukojeti.</p>'
          + T(['Styl hry', 'Vhodná raketa', 'Doplněk'], [
              ['Základní čára, dlouhé výměny', 'větší hlava, vyšší tolerance', 'tlumič vibrací podle pocitu'],
              ['Útočný hráč se silným servisem', 'těžší rám, střední hlava', 'tužší struny'],
              ['Hra u sítě, čtyřhra', 'lehčí a obratná raketa', 'pevný grip'],
              ['Rekreační hra jednou týdně', 'univerzální raketa střední váhy', 'náhradní grip']]) +
          '<h2>Příprava před hrou a prevence</h2>'
          '<p>Tenis zatěžuje rameno, loket, zápěstí i kolena. Před hrou se několik minut rozcvičte, projděte kyčle a ramena a prvních pár míčů hrajte volně. Mnoho potíží s loktem souvisí s příliš těžkou raketou, tuhými strunami nebo s nesprávnou technikou úderu. Pokud bolest přetrvává, nechte si poradit u lékaře či fyzioterapeuta, případně se domluvte s trenérem na úpravě techniky. Bandáže a ortézy z kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> nejsou náhradou za odborné vyšetření.</p>'
          '<p>Kondici a pohyblivost lze podpořit doplňkovým cvičením. Pomůže <a href="/posilovaci-gumy/">cvičení s gumami</a>, posilování a protahování. Pro dobu mimo kurt přijdou vhod i <a href="/svihadla/">švihadla</a>, protože zlepšují práci nohou.</p>'
          '<p>Při prvních hodinách se vyplatí zkusit raketu půjčenou od kamaráda nebo z kurtu. Rozdíl mezi dvěma raketami poznáte po deseti minutách výměn lépe než z tabulky parametrů.</p>'
          '<h2>Co přibalit na kurt</h2>'
          '<ul>'
          '<li>Dvě rakety, pokud hrajete soutěžně, nebo jednu a náhradní grip.</li>'
          '<li>Tubu čerstvých míčů a jednu starší na trénink podání.</li>'
          '<li>Obuv na daný povrch a náhradní ponožky.</li>'
          '<li>Lahev s pitím, případně <a href="/iontove-napoje/">iontový nápoj</a> při delším zápase.</li>'
          '<li>Ručník, čepici či čelenku a krém s UV filtrem při hře venku.</li>'
          '</ul>'
          '<h2>Časté chyby</h2>'
          '<ul>'
          '<li><strong>Příliš těžká raketa.</strong> Namáhá loket a rameno, zvlášť na delších zápasech.</li>'
          '<li><strong>Nesprávná velikost gripu.</strong> Vede k přílišnému tlaku v zápěstí.</li>'
          '<li><strong>Staré struny.</strong> Ztrácí pružnost a zvyšují náraz do ramene a lokte.</li>'
          '<li><strong>Běžecká obuv na kurtu.</strong> Chybí boční opora a hrozí podvrtnutí.</li>'
          '<li><strong>Úplně nové míče na každý trénink.</strong> Pro běžné hraní stačí méně intenzivní obměna.</li>'
          '<li><strong>Raketa ponechaná v horkém autě.</strong> Rám i struny teplo nesnášejí.</li>'
          '</ul>'
          '<h2>Péče o výbavu</h2>'
          '<p>Rakety skladujte v obalu při pokojové teplotě. Po hře osušte rám a rukojeť, grip vyměňte, jakmile se začne lesknout a klouzat. Vyštípaný lak na rámu zkontrolujte, protože praskliny mohou znamenat konec životnosti. Obuv po hře vyvětrejte a vložky občas vyndejte. Míče po otevření tuby uchovávejte v uzavřeném obalu s přetlakem, který prodlouží jejich životnost.</p>'
          '<h2>Nákup a porovnání nabídek</h2>'
          '<p>Rakety se prodávají v různých barvách a ročnících, přičemž starší série bývají dostupnější a hrají podobně. Porovnávejte hlavně technické parametry. U obuvi ověřte velikostní tabulku a u oblečení materiál. Na Sportece vidíte stejný produkt u více prodejců s informací o skladu i dopravě. Další raketové sporty najdete v kategoriích <a href="/badminton/">badminton</a>, <a href="/squash/">squash</a>, <a href="/padel/">padel</a> a <a href="/stolni-tenis/">stolní tenis</a>. Celý obor shrnuje <a href="/micove-sporty/">míčové sporty</a>.</p>',
    faq=[
        ('Jakou tenisovou raketu zvolit pro začátečníka?', 'Lehčí raketu s větší hlavou a vyvážením spíš do hlavy. Takové rakety odpouštějí nepřesný zásah a pomáhají zvládnout základní údery.'),
        ('Podle čeho vybrat velikost gripu?', 'Mezi konečky prstů a dlaní má zbýt prostor zhruba na šířku prstu. Při váhání zvolte menší grip a dolaďte ho obalovou páskou.'),
        ('Jak často měnit struny?', 'Záleží na tom, kolik hrajete. Zhruba tolikrát za rok, kolikrát týdně hrajete, je běžné pravidlo. Mrtvé struny poznáte podle ztráty cítění.'),
        ('Jaký je rozdíl mezi tlakovými a bezpřetlakovými míči?', 'Tlakové míče mají lepší odskok, ale po otevření ho ztrácejí. Bezpřetlakové vydrží déle, bývají ale tvrdší.'),
        ('Mohu hrát tenis v běžecké obuvi?', 'Nedoporučuje se. Chybí boční opora a podrážka nezvládne skluz. Zvolte tenisovou či alespoň sálovou obuv.'),
        ('Jaká obuv na antuku a jaká na tvrdý povrch?', 'Na antuku patří podrážka s hustým vzorem pro řízený skluz, na tvrdý povrch odolnější guma s lepším tlumením.'),
        ('Jak vybrat raketu pro dítě?', 'Podle výšky, ne podle věku. Příliš dlouhá raketa kazí techniku. Pro nejmenší používejte lehké rakety a pomalejší míče.'),
        ('Co je sweet spot?', 'Místo na strunách, kde zásah dává nejlepší odezvu s minimem vibrací. U rakety s větší hlavou bývá větší.'),
        ('Jak pečovat o tenisovou raketu?', 'Skladujte ji v obalu, mimo horké auto a vlhko. Pravidelně vyměňujte grip a kontrolujte rám, zda neobsahuje praskliny.'),
        ('Kolik tub míčů je potřeba na trénink?', 'Pro hru na kurtu stačí jedna tuba na zápas nebo dva tréninky. Pro nácvik servisu se hodí starší míče, které už tolik neodskakují.'),
        ('Kdy poznám, že je čas na novou obuv?', 'Když je podrážka na špičce sjetá, vložka rozdrcená nebo bota po zápase bolí chodidlo. Opotřebená obuv horší oporu i přilnavost.'),
        ('Dá se hrát tenis venku v zimě?', 'Ano, při suchém počasí a nad bodem mrazu, ale míče jsou tužší a hůř odskakují. Hrajte se zahřátým svalstvem a raději v halách.'),
        ('Je lepší raketa starší ročník, nebo nejnovější?', 'Starší série často hrají velmi podobně a bývají dostupnější. Důležitější je, aby raketa odpovídala vaší váze, síle a stylu hry.'),
    ])

# ------------------------------------------------------------------ badminton
NEW['badminton'] = dict(long=True,
    title='Badminton: rakety, košíky, sítě, obuv',
    desc='Badmintonové rakety, košíky, sítě a sálová obuv. Jak vybrat podle váhy, vyvážení a úrovně, plus porovnání nabídek českých obchodů na jednom místě.',
    intro='<p><strong>Badminton</strong> bývá označován za nejrychlejší raketový sport. Košík letí jinak než míč, proto je potřeba lehká raketa, rychlý zápěstní pohyb a obuv, která zvládne prudké zastavení. Rekreačně ho hrají děti, rodiny na zahradě i dospělí v hale, a podle toho se liší i nároky na výbavu. '
          'Pro začátek stačí jednoduchý set, pro soutěžní hru rozhodují parametry rakety. U košíků navíc záleží, zda hrajete v hale, nebo venku na zahradě.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u raket, košíků, sítí, tašek i obuvi. Další raketové sporty najdete v kategoriích <a href="/tenis/">tenis</a>, <a href="/squash/">squash</a> a <a href="/padel/">padel</a>. Dále popisujeme parametry rakety, rozdíly mezi typy košíků, obuv a péči, abyste vybírali s jistotou.</p>',
    guide='<h2>Co se v kategorii prodává</h2>'
          '<p>Nabídka sahá od jednoduchých rodinných sad po rakety pro klubové hráče. Spodní hranici tvoří sety s raketami s ocelovým rámem a sítí, horní jednotlivé rakety z uhlíkových kompozitů. K tomu přibývají košíky, grip pásky, struny, tašky a obuv.</p>'
          + T(['Položka', 'Účel', 'Poznámka'], [
              ['Sety pro rekreaci', 'zahrada, dovolená, děti', 'obvykle dvě rakety, košíky a síť'],
              ['Jednotlivé rakety', 'pravidelná hra v hale', 'rozdíly ve váze a vyvážení'],
              ['Košíky', 'trénink i zápas', 'peří nebo plast'],
              ['Sítě a stojany', 'domácí hřiště, škola, zahrada', 'rozměr a výška podle pravidel'],
              ['Grip pásky a struny', 'ladění pocitu a odezvy', 'výměna po opotřebení'],
              ['Sálová obuv', 'opora při rychlých změnách směru', '<a href="/salova-obuv/">sálová obuv</a>'],
              ['Tašky', 'přenos rakety a oblečení', '<a href="/sportovni-tasky/">sportovní tašky</a>']]) +
          '<h2>Jak vybrat raketu</h2>'
          '<p>Badmintonová raketa je mnohem lehčí než tenisová, váží zhruba osmdesát až devadesát pět gramů. I malý rozdíl je ale na pohybu zápěstí znát. Při výběru sledujte váhu, vyvážení, tuhost násady a materiál rámu.</p>'
          '<h3>Váha</h3>'
          '<p>Označení 2U, 3U, 4U a 5U vyjadřuje váhovou skupinu. Čím vyšší číslo, tím lehčí raketa. Lehčí raketa se snadněji rozkmitá a méně unavuje, těžší dává víc setrvačnosti pro úder. Rekreační hráči obvykle začínají u lehčích kategorií.</p>'
          '<h3>Vyvážení</h3>'
          + T(['Vyvážení', 'Chování', 'Styl hry'], [
              ['Do hlavy', 'silnější smeče, hůře se manévruje', 'útočná hra z dálky'],
              ['Vyvážená', 'univerzální, předvídatelná', 'začátečníci a všestranní hráči'],
              ['Do rukojeti', 'rychlé reakce, rychlá obrana', 'čtyřhra, hra u sítě']]) +
          '<h3>Tuhost násady</h3>'
          '<p>Pružnější násada pomáhá vyrobit sílu při menší rychlosti paže a odpouští chyby. Tužší násada dává přesnost a kontrolu, ale vyžaduje dobrou techniku a rychlý švih. Začátečníci a starší hráči volí spíš pružnější, zkušení tužší.</p>'
          '<h3>Rám a materiál</h3>'
          '<p>Hliníkový nebo ocelový rám najdete v levných rodinných sadách. Je trvanlivý, ale těžší a méně citlivý. Uhlíkové kompozity (grafit) jsou lehké a tuhé, vybírají se do výkonnostních raket, ale jsou náchylnější na náraz do podlahy nebo do soupeřovy rakety. Karbonový rám je křehký, proto jím nenarážejte o zem ani o soupeřovu raketu.</p>'
          '<p>V nabídce jsou rakety značek ' + B(('yonex', 'Yonex'), ('victor', 'Victor'), ('babolat', 'Babolat'), ('carlton', 'Carlton'), ('talbot-torro', 'Talbot Torro'), ('kuikma', 'Kuikma'), ('nils', 'Nils'), ('merco', 'Merco')) + '. Mezi značkami se liší řada parametrů, takže vždy porovnejte údaje u konkrétního modelu.</p>'
          '<h2>Košíky</h2>'
          '<p>Badmintonový košík má korkovou hlavu a letky z peří nebo plastu. Peřové jsou standardem pro soutěže a mají citlivější let a při hře v hale nabízejí správný průběh letu, ale snadno se poškodí a rychle se opotřebují. Plastové (nylonové) jsou odolnější, vydrží opakovaná smeč a hodí se pro děti, školu i venkovní hru. Rychlost létání se označuje číslem, které odpovídá teplotě a nadmořské výšce prostředí. Při tréninku s jedním košíkem se letky časem rozcuchají, tak je dobré je občas přetvarovat prsty.</p>'
          '<h2>Sítě, hřiště a hra venku</h2>'
          '<p>Oficiální hřiště má rozměry odlišné pro dvouhru a čtyřhru, síť visí přibližně do výšky 1,55 metru u kůlů. Pro zahradní hru se rozměry nehlídají, důležitá je pevná síť a rovný povrch. Hrajete-li venku, myslete na vítr. Již slabý závan změní let košíku, proto je hala nebo zástěna lepší pro seriózní trénink. Pokud potřebujete zahradní vybavení, prohlédněte <a href="/hry-na-zahradu/">hry na zahradu</a>.</p>'
          '<h2>Obuv do haly</h2>'
          '<p>Badminton je pohybově náročný, hráč se pohybuje v lunge, skokech a rychlých změnách směru. Běžecká obuv nemá boční oporu, tlumí jen dopředný krok a podrážka může v hale klouzat. Správná sálová obuv má hladkou nebo jemně profilovanou gumovou podrážku a vyztužené boky. Přehled najdete v kategorii <a href="/salova-obuv/">sálová obuv</a>. Pokud chodíte na badminton jen občas, použijte alespoň <a href="/treninkova-obuv/">tréninkovou obuv</a> s boční oporou.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Lehké tričko a šortky ze syntetiky se hodí do haly, kde je teplo a hráč se zapotí. Při tréninku přijdou vhod <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/sportovni-ponozky/">ponožky</a>. Grip pásky vylepší držení, otěrky a potítka chrání zápěstí před potem. Pro přenos poslouží <a href="/sportovni-tasky/">taška</a>, která pojme dvě rakety, obuv a lahev.</p>'
          '<h2>Výběr podle hráče</h2>'
          '<ul>'
          '<li><strong>Děti:</strong> kratší a lehčí rakety, plastové košíky a nižší síť. Důležité je, aby si raketu udržely bez únavy zápěstí.</li>'
          '<li><strong>Rodiny a rekreační hráči:</strong> jednoduchá sada s dvěma raketami stačí, později lze přikoupit lepší kus.</li>'
          '<li><strong>Pravidelní hráči v hale:</strong> jednotlivá raketa s vhodnou váhou a vyvážením, k tomu peřové nebo kvalitnější plastové košíky.</li>'
          '<li><strong>Soutěžící:</strong> dvě stejné rakety, odladěné strunění a obuv s dobrou přilnavostí.</li>'
          '</ul>'
          '<h2>Základy techniky a držení rakety</h2>'
          '<p>Správné držení je polovina úspěchu. Základní „forehand“ držení připomíná podání ruky s raketou: palec a ukazováček tvoří písmeno V na hraně rukojeti, ostatní prsty drží volně. Při úderech z backhandové strany se palec posune na široké plochy rukojeti a zápěstí pracuje rychleji. Pevné sevření se používá jen na okamžik zásahu, mezi údery ruka povolí. Kdo drží raketu celou dobu pevně, rychle ucítí únavu předloktí.</p>'
          + T(['Úder', 'Kdy se používá', 'Na co dbát'], [
              ['Podání', 'zahájení výměny', 'nízký zásah pod úrovní pasu, uvolněné zápěstí'],
              ['Clear (vysoký obloukový)', 'zatlačení soupeře do zadní části', 'zásah nad hlavou, plný švih'],
              ['Smeč', 'ukončení výměny silným úderem dolů', 'předklon těla a dokončení pohybu'],
              ['Drop', 'jemný krátký míček za síť', 'minimální rychlost rakety, cit v prstech'],
              ['Net kill a síťová hra', 'reakce na slabý míč u sítě', 'rychlé zápěstí, raketa před tělem']]) +
          '<h2>Základní pravidla pro začátečníky</h2>'
          '<p>Zápas se hraje na dva vítězné sety a bod získá hráč při každé výměně bez ohledu na to, kdo podával. Podává se diagonálně a košík se u podání zasahuje pod úrovní pasu. Hra končí, když košík dopadne na zem na straně soupeře, nebo když ho soupeř pošle mimo hřiště či do sítě. Přesná pravidla vydává světová federace, pro rekreační hru stačí tato jednoduchá verze. Pokud hrajete s dětmi, domluvte si zjednodušená pravidla a hrajte na kratší sety.</p>'
          '<h2>Strunění a ladění rakety</h2>'
          '<p>Většina levnějších raket se prodává již nastrunená. Pokročilejší hráči si struny vybírají sami, protože tloušťka a napnutí ovlivňují cit i trvanlivost. Tenčí struna dává živější odezvu, ale rychleji se přetrhne. Tlustší vydrží déle. Vyšší napnutí zvyšuje kontrolu, nižší dává více výkonu a odpouští. Při prasknutí struny se raketa nesmí dál používat, nechte ji znovu nastrunit u servisu. Rám se při tom zkontroluje, zda není prasklý.</p>'
          '<p>Pro úplné začátečníky je dobrá zásada hrát nejdřív s lehčím košíkem při zdi nebo s partnerem na krátkou vzdálenost. Teprve když se vám daří udržet výměnu, přidejte rychlost a délku úderů.</p>'
          '<h2>Jak trénovat doma</h2>'
          '<p>Badminton se dá procvičovat i bez partnera. Odbíjení košíku nahoru na místě trénuje cit a rytmus, nácvik výpadů zlepšuje práci nohou a stínové údery bez košíku pomáhají zafixovat pohyb. Kondici podpoří <a href="/svihadla/">švihadla</a> a posilování nohou. Doplňkově se hodí také <a href="/fitness-pomucky/">fitness pomůcky</a> a protahování, protože hráč často sahá do hlubokých pozic.</p>'
          '<h2>Časté chyby</h2>'
          '<ul>'
          '<li><strong>Příliš těžká raketa.</strong> Zatěžuje zápěstí a zpomaluje reakci.</li>'
          '<li><strong>Přílišné napětí strun.</strong> Snižuje odpuštění nepřesného zásahu a zvyšuje riziko přetížení.</li>'
          '<li><strong>Hra v běžecké obuvi.</strong> Hrozí podvrtnutí kotníku při bočních výpadech.</li>'
          '<li><strong>Uložení rakety bez obalu.</strong> Rám je náchylný k poškození nárazem.</li>'
          '<li><strong>Hra bez rozcvičení.</strong> Rychlé změny směru namáhají kotníky, kolena a rameno.</li>'
          '</ul>'
          '<h2>Péče o raketu a košíky</h2>'
          '<p>Raketu skladujte v obalu při pokojové teplotě, mimo vlhko a horké auto. Po hře osušte rukojeť, grip vyměňte, jakmile je kluzký. Struny jsou citlivé na vlhkost, proto raketu nenechávejte ve sklepě. Peřové košíky uchovávejte v původní tubě, aby se letky nezkroutily. Plastové občas omyjte vodou a nechte oschnout.</p>'
          '<h2>Jak číst nabídku v obchodech</h2>'
          '<p>Při porovnání se nenechte zmást grafikou. Zjistěte váhovou kategorii, vyvážení, materiál rámu a zda je raketa prodávána již nastrunená. U sad dívejte se, kolik raket a košíků obsahují. Na Sportece vidíte jednotlivé nabídky u stejného produktu a snadno posoudíte dostupnost i dopravu. Související sporty najdete také v kategoriích <a href="/micove-sporty/">míčové sporty</a> a <a href="/stolni-tenis/">stolní tenis</a>.</p>',
    faq=[
        ('Jakou badmintonovou raketu pro začátečníka?', 'Lehkou raketu s vyvážením na střed a s pružnější násadou. Uhlíkový rám není nutný, důležitější je pohodlné držení.'),
        ('Co znamená označení 3U, 4U a 5U?', 'Jde o váhovou skupinu. Vyšší číslo značí lehčí raketu. Lehčí rakety se snadněji ovládají, těžší dávají více setrvačnosti.'),
        ('Peřové, nebo plastové košíky?', 'Peřové jsou citlivější a používají se v soutěžích, rychle se však opotřebují. Plastové vydrží déle, hodí se pro děti, školu a venkovní hru.'),
        ('Hodí se badminton na zahradu?', 'Ano, s plastovými košíky a pevnou sítí. Vítr ale mění let košíku, takže seriózní trénink je lepší v hale.'),
        ('Jaká obuv je na badminton správná?', 'Sálová obuv s hladkou podrážkou, boční oporou a pevným zakončením pro rychlé výpady. Běžecká obuv nevyhovuje.'),
        ('Jak často měnit struny?', 'Při pravidelné hře zhruba jednou za sezonu, u hráčů rekreačních méně často. Znamením je ztráta napětí nebo prasklá struna.'),
        ('Je lepší raketa pro útok, nebo pro obranu?', 'Raketa s vyvážením do hlavy podpoří silné smeče, raketa s vyvážením do rukojeti rychlejší reakce při obraně a hře u sítě.'),
        ('Jak vybrat raketu pro dítě?', 'Zvolte kratší a lehčí raketu, aby ji dítě udrželo bez bolesti zápěstí. Hodí se plastové košíky a nižší síť.'),
        ('Jak vysoko má viset badmintonová síť?', 'Podle oficiálních rozměrů je asi 1,55 metru u kůlů a o něco méně uprostřed. Při rekreační hře se výška přizpůsobuje dětem.'),
        ('Kolik raket potřebuji do rodiny?', 'Pro dva hráče stačí sada se dvěma raketami. Pro rodinu s dětmi vyberte další kusy v menší velikosti, aby se hráči mohli střídat.'),
        ('Čím se liší rakety pro dvouhru a čtyřhru?', 'Pevná norma neexistuje. Hráči čtyřhry často volí lehčí raketu s vyvážením blíž k rukojeti kvůli rychlým reakcím u sítě.'),
        ('Mám raketu při hře v hale držet pevně?', 'Ne. Sevření uvolněte a zpevněte ho jen v okamžiku zásahu. Trvale pevný stisk unavuje předloktí a zpomaluje zápěstí.'),
        ('Jak dlouho vydrží košík?', 'Peřový jen několik her, plastový mnohem déle. Pokud se letky ohýbají nebo chybí, je čas na nový.'),
        ('Je badminton vhodný pro seniory?', 'Může být, pokud je hra klidná, raketa lehká a obuv vhodná. Při zdravotních potížích se před hrou poraďte s lékařem.'),
    ])

# ------------------------------------------------------------------ boxovaci-pytle
NEW['boxovaci-pytle'] = dict(long=True,
    title='Boxovací pytle a hrušky: výběr a montáž',
    desc='Boxovací pytle, hrušky a stojany: velikosti, plnění, závěsy a montáž. Jak vybrat pro box, kickbox a fitness, srovnání nabídek českých obchodů.',
    intro='<p>Pořádný <strong>boxovací pytel</strong> je jedním z nejvděčnějších kusů vybavení pro domácí trénink. Nevadí mu rána, hodí se pro začátečníka i pokročilého a dá se použít na techniku, rychlost, sílu i kondici. Při nákupu ale rozhoduje několik detailů: velikost a váha, plnění, uchycení, a hlavně to, kam ho zavěsíte. '
          'Špatná volba znamená pytel, který se houpe, tvrdne nebo se dokonce utrhne. Proto níže probíráme typy, váhu, montáž i bezpečnost rukou.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u pytlů, hrušek i příslušenství. Rukavice najdete v kategorii <a href="/boxerske-rukavice/">boxerské rukavice</a>, ochranu v kategorii <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a> a oblečení v <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a>.</p>',
    guide='<h2>Typy pytlů a hrušek</h2>'
          '<p>Pod kategorií se skrývá víc než jeden tvar. Každý typ trénuje něco jiného, a tak se vyplatí vědět, co od něj čekáte.</p>'
          + T(['Typ', 'Na co se hodí', 'Poznámka'], [
              ['Klasický závěsný pytel', 'údery, kopy, kondice', 'nejuniverzálnější volba'],
              ['Dlouhý pytel „banana“', 'nízké kopy, kolena, práce na zemi', 'delší, často sahá téměř k podlaze'],
              ['Stojanový pytel', 'domácí trénink bez stropního závěsu', 'stabilitu určuje podstavec s náplní'],
              ['Rychlostní hruška', 'rytmus, koordinace, reakce', 'malá, pevně vzduchem naplněná'],
              ['Hruška s dvojitým uchycením', 'přesnost a refleks', 'napíná se mezi podlahu a strop'],
              ['Uppercut pytel a pytel pro lokty', 'vyšší technická práce', 'určeno pokročilým'],
              ['Dětské pytle', 'zábava a základy techniky', 'menší a měkčí']]) +
          '<h2>Velikost a hmotnost</h2>'
          '<p>Pro stabilitu platí jednoduché pravidlo: pytel by měl vážit zhruba polovinu hmotnosti hráče, případně o něco méně, má-li být lehčí a rychlejší. Příliš lehký pytel se při každém úderu rozhoupe a přestane trénovat přesnost. Příliš těžký zatěžuje klouby a není příjemný pro začátečníka. Délka se volí podle kopů: běžný pytel míří od hrudi k holeni, dlouhý obsáhne i nízké kopy.</p>'
          '<p>Rozhoduje také průměr. Širší pytel odpouští chyby, užší se více pohybuje a vyžaduje přesnější zásah. Pro děti zvolte kratší pytel, který nezasahuje podlahu a nezpůsobí zranění při pádu.</p>'
          '<h2>Plnění a povrch</h2>'
          '<p>Plnění určuje tvrdost a životnost. Vlastnosti se liší podle použité výplně.</p>'
          + T(['Plnění', 'Vlastnosti', 'Pozor na'], [
              ['Textilní směs (odpad z látek)', 'rovnoměrná, relativně měkká', 'časem se slehne při dolním konci'],
              ['Pěnová vrstva se středovou výplní', 'dobré tlumení, stabilní tvar', 'váha je zpravidla vyšší'],
              ['Písek nebo granulát', 'těžší, velmi tvrdé', 'vyšší zátěž pro ruce a kloub'],
              ['Prázdný obal', 'plníte sami', 'je třeba materiál a trpělivost']]) +
          '<p>Povrch bývá z koženky, PVC nebo pravé kůže. Syntetické materiály jsou cenově dostupné a snadno se čistí, kůže je pružnější a pevnější. Na kvalitu poukazují hlavně švy a úchyty. Hledejte dvojité prošití a zesílené úchyty. Zkontrolujte, zda jsou popruhy přišité přes větší plochu a mají kovové karabiny.</p>'
          '<h2>Kam pytel zavěsit</h2>'
          '<p>Montáž je častý zdroj chyb. Závěs musí unést nejen váhu pytle, ale i dynamické zatížení při úderech a kopech. Strop v bytě bývá často betonový, ale dutý nosník ani sádrokarton nestačí. Použijte nosný trám nebo kotvy dimenzované výrobcem, případně samostatný stojan nebo nástěnný držák. Řetězy by měly mít pružinu nebo tlumič, který snižuje přenos nárazů do konstrukce.</p>'
          '<ul>'
          '<li><strong>Beton:</strong> vhodné chemické nebo mechanické kotvy dle manuálu.</li>'
          '<li><strong>Dřevěný trám:</strong> šrouby s dostatečnou délkou a podložkami.</li>'
          '<li><strong>Nástěnný držák:</strong> řešení do garáže, na zdi s nosnou konstrukcí.</li>'
          '<li><strong>Stojan:</strong> pro nájemní bydlení, ale zabírá více místa.</li>'
          '</ul>'
          '<p>Před prvním tréninkem pytel zkuste zatížit bez úderů, tedy zvednout ho a zatáhnout. Pokud se konstrukce hýbe, montáž je slabá. Po několika týdnech úchyty zkontrolujte. Při pochybnostech nechte montáž udělat odborníka.</p>'
          '<h2>Výběr podle cíle a zkušeností</h2>'
          '<h3>Začátečník</h3>'
          '<p>Hodí se střední pytel s měkčím plněním a pevnými popruhy. K tomu rukavice s bandáží, aby se snížilo riziko zranění ruky. Začněte jednoduchými údery a technikou, nikoli silou. Na prvních trénincích raději krátké a častější série.</p>'
          '<h3>Fitness a kondice</h3>'
          '<p>Pytel se používá jako kardio nástroj: intervaly po třech minutách, pauzy, kombinace úderů a kopů. Pomůže střední nebo lehčí pytel, který se nerozhoupe příliš. Doplňte cvičením s <a href="/svihadla/">švihadly</a>, <a href="/posilovaci-gumy/">posilovacími gumami</a> a <a href="/funkcni-trenink/">funkčním tréninkem</a>.</p>'
          '<h3>Kickbox, thajský box a MMA</h3>'
          '<p>Kopy ocení delší nebo dlouhý pytel s pevnějším plněním a povrch, který snese nárazy holeně. Pomohou chrániče, viz <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>. Celý obor shrnuje kategorie <a href="/bojove-sporty/">bojové sporty</a>.</p>'
          '<h3>Rychlost a koordinace</h3>'
          '<p>Hruška trénuje rytmus a práci s hlavou. Pro správné nastavení musí být v úrovni očí až brady. Zkušení boxeři používají hrušku jako rozcvičení před těžším pytlem.</p>'
          '<h2>Příslušenství, které se hodí</h2>'
          '<p>K pytli patří rukavice a bandáže na ruce, případně chrániče holení a nártu. Základní ochranu zajistí <a href="/boxerske-rukavice/">boxerské rukavice</a>. Při dlouhém tréninku jsou praktické <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/sportovni-tasky/">sportovní taška</a> na vybavení. Při přípravě oblečení a podlahy pomohou doplňky z kategorie <a href="/fitness-pomucky/">fitness pomůcky</a>. Pod pytlem se osvědčí podložka, která tlumí hluk a chrání podlahu. Další vybavení pro domácí tělocvičnu najdete také v kategorii <a href="/fitness/">fitness</a>.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>V nabídce obchodů najdete značky ' + B(('hms', 'HMS'), ('bushido', 'Bushido'), ('insportline', 'Insportline'), ('master', 'Master'), ('kubisport', 'Kubisport'), ('brute', 'Brute'), ('rdx-sports', 'RDX Sports'), ('merco', 'Merco')) + '. Neporovnávejte pouze značku, ale hlavně hmotnost, rozměr, materiál povrchu a typ závěsu.</p>'
          '<h2>Základní trénink na pytli</h2>'
          '<p>Trénink začíná zahřátím: lehké poskoky, kroužení rameny, několik minut švihadla. Pak následují série po dvou až třech minutách s minutovou pauzou. V první sérii pracujte jen s lehkými údery a dívejte se na postoj. Pata zadní nohy se mírně zvedá, brada je skloněná a druhá ruka kryje obličej. Úder vychází z nohy, přes boky a rameno do pěsti, nikoli jen z paže. Silné údery přidejte až ve druhé polovině tréninku.</p>'
          + T(['Cvičení', 'Cíl', 'Poznámka'], [
              ['Jab a kříž v sérii', 'základní technika', 'pomalu a s dokončením pohybu'],
              ['Práce nohou kolem pytle', 'pohyb a vzdálenost', 'nenechte se zastavit u pytle'],
              ['Kombinace s kopy', 'kondice, koordinace', 'pouze s ochranou holeně'],
              ['Intervalová série', 'výdrž', 'střídejte rychlé a pomalé minuty'],
              ['Úder a odskok', 'rytmus a obrana', 'pytel nastaví vlastní rychlost']]) +
          '<h2>Bezpečnost a zdraví rukou</h2>'
          '<p>Většina zranění u začátečníků postihuje zápěstí a záprstní kosti. Příčinou bývá chybné držení pěsti, příliš tvrdý pytel nebo úder bez bandáží. Bandáže zpevní zápěstí a chrání klouby, rukavice tlumí náraz. Vyvarujte se úderů s ohnutým zápěstím a po tréninku ruce uvolněte. Pokud cítíte ostrou bolest, trénink přerušte. Při dlouhodobých obtížích vyhledejte lékaře. Je rozumné domluvit se s trenérem, který zkontroluje techniku a ukáže správné držení.</p>'
          '<h2>Pytel a kondiční trénink v kostce</h2>'
          '<p>Plán na týden může vypadat jednoduše: dva dny technika s lehčími údery, jeden den intervaly a jeden den kopy nebo kombinace podle disciplíny. Mezi dny nechte svaly odpočinout. Po tréninku protáhněte ramena, záda a předloktí. Jakmile technika drží, zvyšujte počet sérií, nikoli sílu jednotlivých úderů, aby zůstala přesnost.</p>'
          '<h2>Domácí prostředí a sousedé</h2>'
          '<p>Pytel v bytě přenáší vibrace do konstrukce a hluk do sousedního bytu. Pomůže tlumicí podložka pod stojan a pružina u závěsu. Trénujte v rozumnou denní dobu. V garáži či suterénu bývá méně omezení, ale ověřte nosnost zdi a stropu. Pamatujte, že těžký pytel potřebuje kolem sebe volný prostor, přibližně kruh o průměru několika kroků, aby se při kopech nehoupal proti nábytku.</p>'
          '<h2>Časté chyby při nákupu a používání</h2>'
          '<ul>'
          '<li><strong>Nesprávná váha.</strong> Příliš lehký pytel se houpe, příliš těžký zatěžuje klouby.</li>'
          '<li><strong>Slabý závěs.</strong> Nejnebezpečnější chyba. Dutý strop nebo malé hmoždinky nemusí vydržet.</li>'
          '<li><strong>Údery bez ochrany rukou.</strong> Samotné rukavice bez bandáže nemusí stačit, hlavně u začátečníků.</li>'
          '<li><strong>Špatná technika.</strong> Silné údery s nesprávným držením zápěstí vedou k bolesti.</li>'
          '<li><strong>Zanedbaná údržba.</strong> Rozedrané švy a uvolněné řetězy je třeba řešit hned.</li>'
          '<li><strong>Trénink bez rozcvičení.</strong> Svaly ramen a zad potřebují zahřátí.</li>'
          '</ul>'
          '<h2>Údržba a skladování</h2>'
          '<p>Povrch pytle otírejte vlhkou utěrkou, po intenzivním tréninku po potu hned. Používejte jemné čisticí prostředky bez rozpouštědel, která poškozují koženku. Pytel nenechávejte dlouhodobě na přímém slunci. Pokud se při dolním konci slehne plnění, občas ho obraťte nebo jemně prohněťte. Při stěhování pytel sundejte a zabalte, aby se nepromáčkl.</p>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>U každého produktu si ověřte rozměr, hmotnost, zda je pytel plný nebo prázdný, a zda jsou v ceně řetězy a karabiny. U stojanů zjistěte, kolik kilogramů zátěže podstavec pojme. Na Sportece vidíte jednotlivé obchody u stejného produktu i jejich dopravu, což se u těžkých kusů hodí. Často dává smysl koupit pytel a rukavice současně, aby výbava seděla k sobě.</p>',
    faq=[
        ('Jak těžký má být boxovací pytel?', 'Zhruba polovina hmotnosti hráče, případně o něco méně pro rychlejší práci. Příliš lehký pytel se houpe, příliš těžký zatěžuje klouby.'),
        ('Plný, nebo prázdný pytel?', 'Plný je připravený k použití. Prázdný vyplníte sami, což je levnější na dopravu, ale vyžaduje čas a vhodný materiál.'),
        ('Kam pytel zavěsit v bytě?', 'Jen na nosný strop nebo trám, ne na sádrokarton. Při pochybnostech zvolte stojan nebo nástěnný držák a nechte montáž zkontrolovat.'),
        ('Potřebuji rukavice a bandáže?', 'Ano. Chrání zápěstí a klouby. Bez nich hrozí odřeniny i zranění, zejména u začátečníků.'),
        ('Jaký je rozdíl mezi pytlem a hruškou?', 'Pytel trénuje sílu, kopy a kondici, hruška rychlost, rytmus a koordinaci. Hruška je menší a lehčí.'),
        ('Který pytel je vhodný na kopy?', 'Delší nebo dlouhý pytel s pevným plněním a povrchem, který snese nárazy holeně. Doporučují se chrániče.'),
        ('Mohu pytel použít jako kardio trénink?', 'Ano, v intervalech po několika minutách s krátkými pauzami. Důležité je zahřátí a správná technika.'),
        ('Jak čistit boxovací pytel?', 'Vlhkou utěrkou a jemným prostředkem bez rozpouštědel. Po potu otřete povrch hned a nenechávejte pytel na slunci.'),
        ('Jak často trénovat na pytli?', 'Pro začátek stačí dva až tři tréninky týdně s dostatečnou pauzou na odpočinek rukou a ramen. Intenzitu zvyšujte postupně.'),
        ('Jaké rukavice ke kterému pytli?', 'Na tvrdší a těžší pytle volte rukavice s dostatečnou výplní. Menší hrušky snesou i lehčí rukavice, ale s bandážemi pod nimi.'),
        ('Proč se pytel houpe?', 'Je příliš lehký vůči síle úderů nebo má volný závěs. Pomůže těžší pytel, pevné uchycení a tlumič v řetězech.'),
        ('Jak daleko od zdi má pytel viset?', 'Tak, aby se při kopu nedotkl zdi ani nábytku. Počítejte s volným prostorem o několik kroků kolem pytle.'),
        ('Co dělat, když se pytel slehne?', 'Obvykle ho stačí zdola prohníst a otočit. Pokud je plnění rozdrcené a tvrdé, pomůže pytel dosypat nebo vyměnit.'),
        ('Můžu pytel nechat v nevytápěné garáži?', 'Ano, ale v mrazu povrch tvrdne a křehne. Před tréninkem ho nechte zahřát a údery začněte lehce.'),
        ('Vyplatí se stojanový pytel?', 'Hodí se tam, kde nelze použít strop. Je přenosný, ale zabírá místo a stabilitu určuje zátěž podstavce.'),
        ('Je boxování do pytle vhodné pro děti?', 'Ano, v menších verzích a pod dohledem trenéra či rodiče. Důležité jsou lehčí pytel, ochrana rukou a správná technika.'),
    ])
