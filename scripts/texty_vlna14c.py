"""sporteka.cz — wave 14c (4. 11. 2026): long texts (>= 1650 words) for lyzarske-kalhoty, turisticke-batohy, polokosile, termopradlo.
General true facts only, no prices. Brands and links verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-kalhoty
NEW['lyzarske-kalhoty'] = dict(long=True,
    title='Lyžařské a snowboardové kalhoty: průvodce výběrem | Sporteka',
    desc='Lyžařské a snowboardové kalhoty pánské, dámské i dětské: membrána, izolace, střih, kalhoty s laclem. Průvodce výběrem a nabídky e-shopů vedle sebe.',
    intro='<p><strong>Lyžařské a snowboardové kalhoty</strong> jsou část výbavy, kterou lyžař oceňuje nejvíc ve chvíli, kdy ji nemá: po pádu do sněhu, na nástupu vleku ve větru nebo při sezení na mokré lavici. Chrání před vlhkem zvenku, odvádějí pot zevnitř a nesmějí bránit v pohybu v kolenou a v bocích. Právě tahle kombinace odlišuje skutečné lyžařské kalhoty od zimních kalhot na procházky.</p>'
          '<p>Na Sportece porovnáte kalhoty od desítek značek a v desítkách e-shopů. Vybírat můžete podle pohlaví, velikosti, barvy, materiálu i slevy. Pokud ladíte celou sestavu, podívejte se také na <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a> a <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>. Následující průvodce vysvětluje, na co se při nákupu dívat a čeho se vyvarovat.</p>',
    guide='<h2>Jak lyžařské kalhoty fungují</h2>'
          '<p>Kalhoty na sjezdovku musí splnit tři úkoly najednou. Za prvé zastavit vodu a vítr. Za druhé udržet teplo kolem nohou, které při sjezdu stojí v pokrčené poloze a jsou vystavené proudu vzduchu. Za třetí pustit ven vlhkost z těla, protože při jízdě se dobře potí i ten, komu je při nástupu zima. Konstrukce kalhot proto obvykle obsahuje vnější tkaninu s úpravou proti smáčení, membránu nebo nepromokavý povlak a vnitřní vrstvu, případně izolaci.</p>'
          '<p>Důležité je pochopit, že žádné kalhoty nevyřeší všechno samy. Zvládají to jen ve spolupráci s vrstvami pod sebou. Bavlněné spodní kalhoty nasáknou potem a ochladí nohy, i když jsou svrchní kalhoty špičkové. Proto k tématu patří také <a href="/termopradlo/">funkční a termo prádlo</a>.</p>'
          '<h2>Typy kalhot podle konstrukce</h2>'
          + T(['Typ', 'Pro koho', 'Na co si dát pozor'], [
              ['Kalhoty bez izolace (shell)', 'aktivní lyžaři a snowboardisté, kdo se rád přizpůsobuje teplotě vrstvením', 'v mrazu je nutné pod ně obléknout teplé spodní vrstvy'],
              ['Kalhoty s lehkou izolací', 'rekreační lyžování na sjezdovkách, běžné zimní dny', 'při jarním lyžování mohou být příliš teplé'],
              ['Kalhoty s laclem', 'začátečníci, děti, snowboardisté v hlubokém sněhu', 'složitější při návštěvě toalety, lacl musí mít praktické zipy'],
              ['Volný střih (freestyle)', 'snowboard, snowpark, pohodlí a vrstvení', 'dlouhé nohavice se vlečou, pokud se správně neupraví'],
              ['Úzký sportovní střih', 'sjezdové lyžování, rychlá jízda', 'pod kalhotami je méně místa na silné vrstvy'],
              ['Kalhoty na skialpinismus', 'výstupy i sjezd, důraz na prodyšnost a nízkou váhu', 'bývají tenčí a v zimě na vleku chladnější']]) +
          '<h2>Membrána, vodní sloupec a prodyšnost</h2>'
          '<p>U lyžařských kalhot se nejčastěji setkáte s údajem o vodním sloupci v milimetrech a s údajem o prodyšnosti. Vodní sloupec říká, jaký tlak vody materiál vydrží, než začne propouštět. Čím je číslo vyšší, tím déle kalhoty odolávají vlhku, ale u zimního sportu hrají roli i zalepené švy a kvalitní zipy. Prodyšnost určuje, kolik vodní páry projde látkou ven. Kdo lyžuje svižně a hodně se potí, měl by sledovat obě hodnoty společně a nespoléhat jen na jednu z nich.</p>'
          '<p>Dobré kalhoty bývají doplněné o <strong>větrací zipy</strong> na vnitřní straně stehen. Otevřené zipy zrychlí odvod tepla při výstupu, při čekání na lanovce je zase zavřete. Důležité jsou také <strong>sněhové manžety</strong> uvnitř nohavic, které přiléhají k lyžařské botě a nedovolí sněhu vniknout dovnitř, a <strong>zesílené spodní okraje</strong> odolné proti poškrábání hranami lyží.</p>'
          '<h2>Izolace a teplo</h2>'
          '<p>Teplo kalhot nezávisí jen na tloušťce. Rozhoduje, kolik vzduchu se mezi vlákny uvězní, jak dobře kalhoty přiléhají a co máte pod nimi. Syntetická izolace drží teplo i po navlhnutí a snese běžné praní, proto se v lyžařských kalhotách používá nejčastěji. Péřové vycpávky se u kalhot vyskytují zřídka, protože u kolen a zadku je namáhání a vlhkost největší. Pokud jezdíte většinou za jasných dnů a na jaře, vybírejte kalhoty bez izolace nebo s lehkou a teplo řešte spodním prádlem. Kdo lyžuje v mrazu nebo hodně sedí na lanovkách, ocení hřejivější typ.</p>'
          '<h2>Pánské, dámské a dětské kalhoty</h2>'
          '<p>Pánské a dámské střihy se liší v délce nohavic, šířce v pase a v bocích a v ohnutí kolene. Dámské kalhoty bývají v bocích zaoblenější a kratší, pánské rovnější a delší. Rozdíl pocítíte až při pohybu, proto zkoušejte ohyb kolen: do hlubokého podřepu i do naklonu vpřed by kalhoty neměly drhnout ani se stahovat. Dětské kalhoty mívají prodloužitelné nohavice nebo nastavitelný pas, takže vydrží i růstový skok. Pro nejmenší děti jsou vhodné kalhoty s laclíkem, které hřejí kolem pasu a nikdy se nesesunou.</p>'
          '<p>Pro nejmenší sjezdaře navazuje na tuto kategorii nabídka <a href="/detske-lyze/">dětských lyží</a> a <a href="/lyzarske-helmy/">lyžařských helem</a>. Dětská helma i kalhoty by měly být vždy v kombinaci s dobře padnoucím <a href="/lyzarske-obleceni/">lyžařským oblečením</a>, aby dítě nenasáklo sněhem a nezmrzlo.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Správná velikost se pozná při pohybu. Posaďte se na bobek, zvedněte koleno k hrudi a protáhněte se do stran, jako byste hledali stabilitu na lyžích. Pokud kalhoty tlačí v rozkroku nebo se v kolenou napínají, jsou malé. Pokud nohavice sjíždějí přes botu a lemují sníh, jsou naopak příliš dlouhé. Pro začátečníky je pohodlnější mírně volnější střih, protože pády jsou častější a potřebují prostor pro chrániče nebo silnější podšívku.</p>'
          '<ul><li><strong>Pas:</strong> nastavitelný pas s gumou nebo popruhy se přizpůsobí oblečení pod kalhotami.</li>'
          '<li><strong>Kapsy:</strong> alespoň jedna zipová kapsa pro skipas a jedna pro drobnosti.</li>'
          '<li><strong>Kolena a zadek:</strong> zesílení z odolnější látky prodlužuje životnost při pádech.</li>'
          '<li><strong>Nohavice:</strong> musí jít navléct přes lyžařskou botu bez boje a pevně se přichytit.</li>'
          '<li><strong>Šle:</strong> odnímatelné šle pomáhají u lyžařů, kterým se kalhoty sesouvají v pase.</li></ul>'
          '<h2>Snowboard versus sjezdové lyžování</h2>'
          '<p>Snowboardisté tráví víc času sezením ve sněhu a opřeni o ruce, proto vyhledávají kalhoty s vyšší odolností zadní části a delším lemem. Lyžaři zase uvítají užší střih a lepší pohyblivost v bocích. Rozdíl ale není pevně daný. Mnoho značek vyrábí unisexové střihy a o výběru nakonec rozhoduje pohodlí. Snowboard má vlastní kategorii <a href="/snowboarding/">snowboardingu</a> s doplňky jako <a href="/snowboardove-chranice/">chrániče</a> nebo <a href="/snowboardove-boty/">snowboardové boty</a>, které s kalhotami úzce souvisejí, protože tvar boty ovlivňuje, jak nohavice dosednou.</p>'
          '<h2>Sjezdovka, skialpinismus nebo běžky</h2>'
          '<p>Pro lanovku a sjezdovku jsou nejvhodnější vyloženě zimní kalhoty. Při výstupech na skialpech se tělo zahřívá, proto se hodí tenčí materiály, kratší manžety a dlouhé větrací zipy. Detaily najdete v kategorii <a href="/skialpinismus/">skialpinismus</a>. Na běžky a lehké zimní túry stačí obvykle <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> s membránou nebo softshellové materiály, které jsou pružnější a prodyšnější, ale hůř odolávají dlouhému sezení ve sněhu. Při nočním chladu a větru jim sluší vrstva termoprádla pod nimi.</p>'
          '<h2>Co mít pod kalhotami a na nich</h2>'
          '<p>Základem je spodní vrstva, která odvádí pot od kůže. U lyžování se osvědčily funkční legíny z umělých vláken nebo z <a href="/merino-pradlo/">merino prádla</a>. Na ně se v mrazu přidá lehký fleecový kus. Důležitá jsou také <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, které sahají nad lýtko a nesmějí se krčit v botě, a <a href="/lyzarske-rukavice/">rukavice</a>, které dotvoří celou sestavu. Mnoho lyžařů si koupí kalhoty a zapomene na to, že špatná ponožka nebo bavlněné spodky zničí komfort stejně jako promoklé kalhoty.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší sortiment lyžařských a snowboardových kalhot na Sportece nabízejí značky ' + B(('rossignol', 'Rossignol'), ('kilpi', 'Kilpi'), ('dare2b', 'Dare2b'), ('helly-hansen', 'Helly Hansen'), ('northfinder', 'Northfinder'), ('o-neill', "O'Neill"), ('silvini', 'Silvini'), ('cmp', 'Cmp'), ('protest', 'Protest'), ('loap', 'Loap'), ('picture', 'Picture'), ('scott', 'Scott'), ('alpine-pro', 'Alpine Pro'), ('columbia', 'Columbia'), ('hannah', 'Hannah')) + '. Nabídka se liší stylem. Některé značky se zaměřují na rekreační lyžaře a jednoduchý střih, jiné na freeride a snowboard s dlouhým volným střihem, další na technické kalhoty s membránou. Při srovnání proto neporovnávejte jen cenu, ale zejména konstrukci a určení.</p>'
          '<h2>Péče a praní</h2>'
          '<p>Lyžařské kalhoty vydrží mnoho sezón, pokud je správně ošetříte. Po každém dni na sněhu je nechte vyschnout rozvěšené, nejlépe na vzdušném místě bez přímého topení. Příliš žár poškodí lepené švy a membránu. Perte je podle štítku, obvykle při nižší teplotě bez aviváže a s čisticím prostředkem určeným pro funkční textil. Aviváž ucpe póry membrány a sníží prodyšnost. Po několika praních se úprava proti smáčení vyčerpá a látka začne nasávat vodu. Pomůže impregnační sprej nebo prací přípravek s impregnací a krátké ohřátí v sušičce na mírný program, pokud to výrobce dovolí.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Kupovat kalhoty podle módní barvy a ignorovat membránu i střih.</li>'
          '<li>Volit příliš teplé kalhoty na jarní lyžování, kde se pak člověk uvaří.</li>'
          '<li>Zkoušet kalhoty jen vestoje, ne v podřepu a při pohybu kolen.</li>'
          '<li>Podcenit sněhové manžety a nechat nohavice sjíždět přes botu.</li>'
          '<li>Spoléhat se na kalhoty a nepřipravit si vrstvy pod nimi.</li>'
          '<li>Prát bez ohledu na štítek a ničit impregnaci aviváží.</li></ul>'
          '<h2>Kdy kalhoty koupit a jak porovnat nabídky</h2>'
          '<p>Nejvíc modelů, velikostí a barev je k dispozici na začátku sezóny, kdy e-shopy doplňují sklady. Slevy přicházejí obvykle ke konci zimy, ale pak často zbývají jen okrajové velikosti. Pokud znáte svou velikost a styl, může se vyplatit nakoupit dřív. Ve srovnání na Sportece sledujte nejen nabídku, ale i dostupnost velikosti, doručení a podmínky vrácení. U oblečení je výměna běžná a dobře si ověřte, zda ji obchod bez potíží zajistí. Stejnou pozornost věnujte i detailům jako barva, odstín nebo dostupnost v dámském a pánském střihu.</p>',
    faq=[
        ('Jaký vodní sloupec mají mít lyžařské kalhoty?', 'Pro běžné sjezdové lyžování stačí zhruba 10 000 mm, kalhoty ale musí mít zalepené švy a kvalitní zipy. Vyšší hodnota se vyplatí pro snowboard, kde sedíte ve sněhu, a pro lyžování za mokrého počasí. Kromě čísla sledujte i prodyšnost, aby se nohy nepotily.'),
        ('Mají být lyžařské kalhoty izolované, nebo bez izolace?', 'Záleží na tom, jak se rád oblékáte. Kalhoty bez izolace jsou univerzálnější, protože teplo regulujete spodními vrstvami. Izolované jsou jednodušší na chladné dny a lanovky, ale na jaře se v nich zahřejete. Začátečníkům a zimomřivým stačí lehká izolace.'),
        ('Je lepší lacl, nebo klasické kalhoty?', 'Kalhoty s laclem lépe chrání proti sněhu v zádech a nesklouznou, proto je volí děti, začátečníci a snowboardisté v hlubokém sněhu. Klasické kalhoty se snáz oblékají a řeší se v nich toaleta. Ujistěte se, že lacl má dobře vedené zipy.'),
        ('Jak poznám správnou velikost lyžařských kalhot?', 'Zkuste podřep a zvednuté koleno, v obou polohách kalhoty nesmí tlačit ani se stahovat. Nohavice mají zakrýt vršek boty, ale nesmí se pod ní hromadit. V pase by měly sedět s oblečením pod nimi, které na sjezdovce skutečně nosíte.'),
        ('Mohou se lyžařské kalhoty použít i na snowboard?', 'Ano, funkce jsou stejné. Snowboardisté však častěji preferují volnější střih, vyšší odolnost na zadku a delší nohavice. Pokud si vyberete lyžařský střih, ověřte, že vám nic nebrání v hlubokém podřepu a při sezení ve sněhu.'),
        ('Jak pereme lyžařské kalhoty s membránou?', 'Perte je při nižší teplotě s prostředkem určeným pro funkční textil a bez aviváže. Aviváž zalepí membránu a sníží prodyšnost. Po opakovaných praních obnovte impregnaci sprejem nebo přípravkem do pračky, aby látka opět odpuzovala vodu.'),
        ('Co nosit pod lyžařské kalhoty?', 'Nejlépe funkční legíny z umělých vláken nebo z merina, které odvádějí pot od těla. Bavlna nasákne a ochladí nohy, proto se jí vyhněte. V mrazu přidejte tenčí fleecovou vrstvu a ponožky, které sahají nad lýtko a netlačí v botě.'),
        ('Proč mají kalhoty větrací zipy?', 'Větrací zipy na stehnech umožní rychle odvést teplo a vlhkost, když jdete do kopce nebo se potíte při jízdě. V klidu je zavřete a teplo zůstane. U skialpinismu a jarního lyžování jsou téměř nezbytné, na mrazivé dny je nepoužijete.'),
        ('Čím se liší dámské a pánské lyžařské kalhoty?', 'Dámské kalhoty mají zpravidla užší pas a širší boky, kratší nohavice a jinak tvarované koleno. Pánské jsou rovnější a delší. Unisexové střihy najdete hlavně u freestylových a snowboardových kalhot, vyplatí se zkusit obojí a vybrat podle pohodlí.'),
        ('Kdy je nejlepší doba na nákup lyžařských kalhot?', 'Nejširší výběr velikostí a barev je před sezónou, na podzim a začátkem zimy. Slevy se objeví na konci zimy, ale často zůstanou jen krajní velikosti. Pokud potřebujete konkrétní střih, kupujte včas a sledujte nabídky více obchodů vedle sebe.'),
        ('Jak dlouho lyžařské kalhoty vydrží?', 'Při správné péči i několik sezón. Nejdřív se opotřebuje úprava proti smáčení a spodní okraj nohavic od hran lyží. Zesílená kolena a zadek prodlužují životnost. Opravu drobných škod zvládne obyčejná záplata a nová impregnace.'),
    ])

# ------------------------------------------------------------------ turisticke-batohy
NEW['turisticke-batohy'] = dict(long=True,
    title='Turistické batohy: objem a zádový systém | Sporteka',
    desc='Turistické batohy od denních výletů po týdenní treky: objem, nosný systém, velikost zad a péče. Průvodce výběrem a nabídky e-shopů vedle sebe.',
    intro='<p><strong>Turistický batoh</strong> nese všechno, co potřebujete na cestě, a zároveň rozhoduje o tom, zda si túru užijete, nebo ji budete jen přežívat. Dobře padnoucí batoh přenese váhu na boky, nechá záda dýchat a dá se otevřít tam, kde ho potřebujete. Špatný batoh bolí ramena, ať je jakkoli drahý nebo moderní.</p>'
          '<p>Na Sportece najdete turistické batohy od lehkých denních modelů po velké kousky na trek na více dní. Vedle nich se vyplatí zvážit <a href="/batohy/">další typy batohů</a>, například <a href="/mestske-batohy/">městské</a>, <a href="/skolni-batohy/">školní</a> nebo <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>. Průvodce níže vysvětluje, jak zvolit objem, zádový systém a velikost a jak se o batoh starat.</p>',
    guide='<h2>Začněte objemem</h2>'
          '<p>Objem batohu se udává v litrech a lidé ho často volí podle pocitu. Praktičtější je opačný postup: nejdřív si rozložte věci, které na cestu skutečně vezmete, a teprve pak pořiďte batoh, který je pojme s malou rezervou. Příliš velký batoh svádí přibalit zbytečnosti, příliš malý nutí věci přivazovat zvenčí a zhoršuje těžiště.</p>'
          + T(['Typ túry', 'Orientační objem', 'Co se vejde'], [
              ['Krátký výlet na půl dne', 'do 20 litrů', 'láhev, svačina, bunda do deště, mapa, lékárnička'],
              ['Celodenní túra', '20 až 35 litrů', 'navíc vrstva na zahřátí, jídlo na celý den, čelovka'],
              ['Víkend s přespáním v chatě', '30 až 45 litrů', 'náhradní oblečení, hygiena, lehký spací vak'],
              ['Několikadenní trek se stanem', '50 až 70 litrů', 'stan, spacák, karimatka, vařič, jídlo na několik dní'],
              ['Expedice a dlouhé putování', 'více než 70 litrů', 'zimní vybavení, zásoby, technické vybavení']]) +
          '<p>Hodnoty jsou jen orientační. Objem ovlivňuje také zimní vs. letní výbava a to, zda je zbytek vybavení lehký. Zimní spacák nebo péřová bunda zabírají víc místa než letní verze. Kdo nosí vše lehké a skladné, vystačí s menším batohem než ten, kdo má klasickou výbavu.</p>'
          '<h2>Záda, popruhy a bederní pás</h2>'
          '<p>Nejdůležitější částí batohu je <strong>nosný systém</strong>. Skládá se z polstrovaných ramenních popruhů, bederního pásu, hrudního pásku a zádové části. U menších batohů se nosnost opírá hlavně o ramena. U velkých batohů má nést většinu váhy bederní pás, který se opírá o kyčelní kosti. Ramena jen stabilizují. Pokud pás dosedá na měkké břicho nebo je příliš široký, přenos váhy nefunguje a ramena bolí.</p>'
          '<ul><li><strong>Velikost zádové části:</strong> měří se od sedmého krčního obratle k úrovni kyčelních kostí. Mnoho batohů nabízí velikosti S, M a L nebo nastavitelná záda.</li>'
          '<li><strong>Dámské střihy:</strong> mají kratší záda, užší ramenní popruhy a tvarovaný bederní pás.</li>'
          '<li><strong>Odvětrávaná záda:</strong> prostor mezi zády a batohem zlepšuje cirkulaci vzduchu, ale odsune těžiště od těla.</li>'
          '<li><strong>Přiléhající záda:</strong> drží zátěž blíž k tělu a hodí se na technický terén a těžší náklad.</li>'
          '<li><strong>Hrudní pásek:</strong> stahuje popruhy k sobě a zabraňuje jejich sklouzávání z ramen.</li></ul>'
          '<h2>Jak se batoh měří a nastavuje</h2>'
          '<p>Při zkoušce vždy dejte do batohu zátěž. Prázdný batoh se chová úplně jinak než naložený. Postavte se rovně, utáhněte bederní pás tak, aby střed pásu ležel na kyčelních kostech, a pak postupně dotahujte ramenní popruhy. Mezi popruhy a rameny nemá být mezera, ale nic nesmí tlačit. Nakonec zapněte hrudní pásek a seřiďte stahovací pásky u horní části batohu. Horní okraj batohu má být zhruba v úrovni uší a stahovací popruhy z horní části mají vést k ramenům mírně vzhůru, ne vodorovně.</p>'
          '<h2>Typy batohů podle použití</h2>'
          + T(['Typ', 'Vhodný pro', 'Zvláštnost'], [
              ['Denní batoh', 'výlety, hory, město', 'lehká konstrukce, často vak na pití'],
              ['Trekový batoh', 'několikadenní putování', 'pevný nosný systém, bederní pás, dolní komora na spacák'],
              ['Batoh na cestování', 'letiště, ubytovny, města', 'otvírání jako kufr, ochrana proti krádeži'],
              ['Lezecký batoh', 'skály, ferraty, lyžařské túry', 'štíhlý tvar, úchyty na lano a cepín'],
              ['Fotografický batoh', 'foto túry', 'vnitřní přepážky, boční přístup k technice'],
              ['Dětský batoh', 'děti na výletech', 'malé záda, lehká konstrukce, reflexní prvky']]) +
          '<p>Pro delší pobyt venku se hodí kombinace s <a href="/stany/">stanem</a>, <a href="/spaci-pytle/">spacákem</a> a <a href="/karimatky-a-matrace/">karimatkou</a>. Pokud vybíráte celou výbavu, věnujte pozornost <a href="/kemping/">kempingu</a> a <a href="/outdoor/">outdooru</a> jako celku. Vedle batohu bude potřeba také <a href="/trekova-obuv/">trekové obuv</a>, <a href="/trekove-hole/">trekové hole</a> a <a href="/celovky-a-svitilny/">čelovka</a>, bez které se noční příchod na chatu nebo odchod ve tmě neobejde.</p>'
          '<h2>Konstrukce a funkce, které stojí za pozornost</h2>'
          '<p>Rozdíl mezi dobrým a průměrným batohem často tkví v detailech. Zipy musí být hladké a odolné, švy zesílené v místech zátěže. Boční kapsy by měly dosáhnout na láhev i za chůze. Pokud nesete dlouhé věci, uvítáte úchyty na hole. Spodní zip nebo oddělená spodní komora usnadní přístup ke spacáku bez vykládání celého obsahu. Horní kapsa na drobnosti se hodí na mapu, doklady a svačinu.</p>'
          '<ul><li><strong>Pláštěnka na batoh:</strong> mnoho modelů ji mívá ve spodní kapse. Ochrání obsah, pokud začne pršet.</li>'
          '<li><strong>Vnitřní kapsa na vak na pití:</strong> umožňuje pít bez zastavení.</li>'
          '<li><strong>Kompresní popruhy:</strong> stáhnou obsah blíž k tělu a stabilizují těžiště.</li>'
          '<li><strong>Úchyty na výbavu:</strong> smyčky a poutka pro cepín, hole nebo karimatku.</li>'
          '<li><strong>Přední přístup:</strong> zip na přední straně umožní otevřít batoh jako kufr.</li></ul>'
          '<h2>Jak batoh sbalit</h2>'
          '<p>Správné balení šetří záda stejně jako dobrý batoh. Nejlehčí a nejměkčí věci, například spacák, patří dolů. Nejtěžší věci se ukládají blízko zádům a do úrovně lopatek, aby těžiště zůstalo nad boky. Věci, které budete potřebovat za chůze, patří nahoru nebo do kapes: pláštěnka, svačina, čepice, rukavice. Dutiny vyplňte oblečením, aby se obsah nepřesouval. Při balení vždy myslete na to, že se budete batoh pokaždé snažit dostat na záda s nejmenším úsilím, proto pečlivé a symetrické rozložení šetří sílu.</p>'
          '<h2>Pro koho a na co</h2>'
          '<p>Rodinné výlety se obejdou s malým denním batohem, který pojme pití, svačiny a náhradní trička. Pro děti vybírejte batohy se zádovou částí odpovídající jejich výšce a bez zbytečného zatížení. Turista, který chodí po českých horách a spí na chatách, vystačí s batohem do čtyřiceti litrů. Pro trekaře a vodáky s přespáváním ve stanu je vhodné vybrat nosný systém s dobrým bederním pásem. Při zimních túrách počítejte s větším objemem kvůli teplému oblečení, zatímco v létě vám zbude místo. Pro vodní sporty se hodí vodotěsné pytle, které chrání vybavení před vlhkem.</p>'
          '<p>Do města a na cesty po letištích existují <a href="/mestske-batohy/">městské batohy</a> s jednodušším střihem a laptopovou kapsou. Běžci milují <a href="/bezecke-vesty-a-batohy/">vesty</a>, které se přimknou k tělu. A kdo potřebuje přenášet sportovní vybavení nebo oblečení do tělocvičny, najde řešení mezi <a href="/sportovni-tasky/">sportovními taškami</a>.</p>'
          '<h2>Materiály a hmotnost batohu</h2>'
          '<p>Většina turistických batohů se šije z nylonu nebo polyesteru. Tkaniny se liší hustotou vlákna, která se označuje číslem denier, a povrchovou úpravou. Hrubší tkanina lépe snáší otěr o skálu a větve, jemnější je lehčí a skladnější. Lehké batohy šetří záda, jenže bývají méně odolné a mají jednodušší nosný systém. Pokud nosíte těžký náklad nebo chodíte skalnatým terénem, nehoňte se za nejnižší hmotností. Kdo cestuje nalehko a s nízkou zátěží, ocení lehký model bez zbytečných řemínků.</p>'
          '<p>Hmotnost batohu je jedna věc, hmotnost pohodlí druhá. Pevný rám nebo výztuha v zádech váží víc, ale rozloží náklad na boky a u těžších nákladů se vyplatí. U lehkého batohu bez rámu vám zátěž spočine na ramenou, takže ho zaplňte pouze do rozumné míry a těžké věci uložte blízko zad.</p>'
          '<h2>Co dělat s batohem před koupí</h2>'
          '<p>Nejjistější cesta je batoh vyzkoušet s reálnou zátěží. V obchodě si vyžádejte pytlíky s pískem nebo ho naplňte vlastním oblečením. Projděte se, předkloňte se, otočte se a posaďte se. Sledujte, zda se bederní pás neposouvá, zda ramenní popruhy neškrtí podpaží a zda batoh při pohybu nepřevažuje na jednu stranu. Při nákupu online si předem změřte délku zad a ověřte, že model nabízí odpovídající velikost nebo nastavitelný systém. Zeptejte se také na podmínky vrácení, protože batoh se skutečně pozná až při zátěži.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší sortiment turistických batohů mají značky ' + B(('deuter', 'Deuter'), ('osprey', 'Osprey'), ('fjallraven', 'Fjällräven'), ('regatta', 'Regatta'), ('husky', 'Husky'), ('highlander', 'Highlander'), ('ferrino', 'Ferrino'), ('loap', 'Loap'), ('columbia', 'Columbia'), ('cabinzero', 'CabinZero'), ('pacsafe', 'Pacsafe'), ('hannah', 'Hannah'), ('quechua', 'Quechua'), ('the-north-face', 'The North Face'), ('mammut', 'Mammut'), ('eagle-creek', 'Eagle Creek'), ('naturehike', 'Naturehike')) + '. Některé jsou zaměřené na klasické turistické a trekové batohy, jiné na cestování nebo městské použití. Při porovnání se držte svého použití, ne jména značky.</p>'
          '<h2>Péče o batoh</h2>'
          '<p>Batoh po túře vyprázdněte, vytřepejte a nechte uschnout. V mokrém stavu plesniví a materiál ztrácí vodoodpudivou úpravu. Skvrny odstraňujte vlažnou vodou a jemnou houbičkou, pračce se raději vyhněte. Mechanické namáhání v pračce poškodí pěnové výplně a lepené části. Zipy občas očistěte od písku a potřete je vhodným mazivem. Před uskladněním povolte všechny popruhy a batoh uložte volně, ne pod těžkými předměty, aby si zachoval tvar.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Vybírat batoh jen podle objemu a ignorovat velikost zad.</li>'
          '<li>Zkoušet prázdný batoh a nezatížit ho přibližnou váhou výbavy.</li>'
          '<li>Kupovat velký batoh pro jistotu a pak ho zbytečně plnit.</li>'
          '<li>Podcenit bederní pás a přenášet všechnu váhu na ramena.</li>'
          '<li>Spoléhat na to, že batoh je nepromokavý, i když výrobce uvádí jen odolnost vůči vodě.</li>'
          '<li>Ukládat batoh vlhký a pak se divit zápachu a plísni.</li></ul>',
    faq=[
        ('Jak velký turistický batoh potřebuji?', 'Na celodenní výlet stačí obvykle objem kolem dvaceti až pětatřiceti litrů, na víkend s přespáním v chatě třicet až pětačtyřicet. Na trek se stanem se používají objemy od padesáti litrů výš. Vždy záleží na tom, jak lehkou výbavu máte.'),
        ('Podle čeho vybrat velikost zádové části?', 'Měří se délka zad od sedmého krčního obratle po úroveň kyčelních kostí. Podle ní vyberete velikost batohu nebo nastavíte nastavitelná záda. Správně nastavený batoh má bederní pás na kyčlích a ramenní popruhy bez mezery.'),
        ('Má cenu kupovat dámský batoh?', 'Dámské modely mají kratší záda, užší ramenní popruhy a tvarovaný pás, který lépe sedí na ženských bocích. Pro ženy s kratším trupem jsou pohodlnější. Pokud vám padne unisexový model, není důvod volit jiný.'),
        ('Kolik váhy má nést bederní pás?', 'U větších batohů má nést většinu zátěže, ramena ji jen stabilizují. Aby to fungovalo, musí pás sedět na kyčelních kostech a pevně obepínat boky. U malých denních batohů je pás jen pomocný a nese minimum.'),
        ('Je lepší batoh s odvětranými zády?', 'Odvětrávaná záda zlepšují cirkulaci vzduchu a v teple se méně potíte. Za to se těžiště posune dál od těla, takže batoh je při těžším nákladu méně stabilní. Pro těžkou zátěž je lepší přiléhavé záda, pro teplé dny lehčí odvětrané.'),
        ('Je turistický batoh nepromokavý?', 'Většina batohů je vyrobena z látek s vodoodpudivou úpravou, která odolá lehkému dešti, ale ne dlouhému lijáku. Pro jistotu používejte pláštěnku na batoh, případně vodotěsné pytle uvnitř. Citlivé věci, třeba spacák nebo elektroniku, zabalte zvlášť.'),
        ('Jak správně sbalit batoh?', 'Nejlehčí a nejměkčí věci, například spacák, dejte dolů. Těžké věci uložte co nejblíž zádům a do výšky lopatek. Věci, které budete potřebovat na cestě, mějte nahoře nebo v kapsách. Prázdná místa vyplňte oblečením, aby obsah nepadal.'),
        ('Jak batoh vyčistit?', 'Vyprázdněte ho, vytřepejte písek a nečistoty a skvrny omyjte vlažnou vodou s jemným mýdlem. Pračce se raději vyhněte, může poškodit výplně i povrchovou úpravu. Nechte ho dokonale uschnout mimo přímé slunce a topení.'),
        ('Který batoh se hodí na cestování letadlem?', 'Na cestování se hodí batohy s otevíráním podobným kufru, s pevným zadním panelem a se skrytými popruhy, které nezavadí o dopravník. Dbejte na rozměry pro příruční zavazadlo podle konkrétní letecké společnosti, protože se liší. Cestovní batohy najdete také v nabídce značek.'),
        ('Mohu turistický batoh používat i do města?', 'Ano, menší denní batoh se hodí i do města. Větší trekové batohy se v městské dopravě nosí hůře, jsou objemné a zavazí. Pro každodenní dojíždění je praktičtější městský model s kapsou na notebook a jednoduchým střihem.'),
        ('Kdy turistický batoh vyměnit?', 'Když se trhají švy, zip nezavírá nebo se rozpadá pěnová výplň zádové části a popruhů. Opotřebovaný nosný systém přestane přenášet váhu a bolí záda. Drobné škody lze opravit u krejčího nebo v servisu, ale nosný systém se opravuje obtížně.'),
    ])

# ------------------------------------------------------------------ polokosile
NEW['polokosile'] = dict(long=True,
    title='Polokošile: pánské a dámské sportovní polo trička | Sporteka',
    desc='Sportovní i módní polokošile pánské, dámské a dětské: materiál, střih, velikost, údržba. Průvodce výběrem a nabídky e-shopů vedle sebe.',
    intro='<p><strong>Polokošile</strong> je zvláštní oděv, který se vyvinul na tenisových kurtech a dnes ho nosí golfisté, fotbalisté, lidé v kanceláři i na výletě. Má límeček, krátký knoflíkový rozparek a pohodlný pletený materiál. Kombinuje pohodlí trička s úpravnějším vzhledem košile, a proto se vejde do míst, kam by tričko bylo málo a košile moc.</p>'
          '<p>Na Sportece porovnáte polokošile od značek sportovních i módních a vedle sebe uvidíte nabídky obchodů. Příbuzné kategorie jsou <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/funkcni-tricka/">funkční trička</a>, <a href="/kosile/">košile</a> a <a href="/golfove-obleceni-a-obuv/">golfové oblečení</a>. Průvodce níže vysvětluje materiály, střihy, velikosti a údržbu, aby vaše polokošile vydržela v dobrém stavu co nejdéle. Vybírat můžete podle pohlaví, velikosti, barvy i materiálu a porovnat dostupnost v několika obchodech najednou.</p>',
    guide='<h2>Odkud polokošile pochází a proč se nosí</h2>'
          '<p>Polokošile vznikla jako praktický oděv pro hráče, kterým bylo v dlouhé košili těžko. Krátký rukáv, pletený materiál a límeček, který chrání krk před sluncem, se osvědčily natolik, že se oděv rozšířil z kurtů na ulici. Dnes je to nejuniverzálnější kus mezi tričkem a košilí. Hodí se k džínám, k kalhotám a při slavnostnější příležitosti stačí přidat sako. Díky tomu je nákup polokošile jedním z nejlepších poměrů užitku k počtu nošení.</p>'
          '<h2>Materiál rozhoduje o komfortu</h2>'
          + T(['Materiál', 'Vlastnosti', 'Kdy se hodí'], [
              ['Piké z bavlny', 'klasická struktura s drobnou texturou, prodyšná, příjemná na dotek', 'denní nošení, město, volný čas'],
              ['Bavlněný žerzej', 'hladký a měkký, lehčí než piké', 'teplé dny, volnější vzhled'],
              ['Polyester a funkční směsi', 'rychle schne, odvádí pot, nemačká se', 'golf, tenis, běh, aktivní sport'],
              ['Směs bavlny a elastanu', 'pružnější, drží tvar, lépe sedí na těle', 'úzké střihy, každodenní nošení'],
              ['Merino a přírodní směsi', 'neztrácí svěžest ani po delším nošení', 'cestování, kancelář, nenáročná údržba']]) +
          '<p>Bavlna je pohodlná a prodyšná, ale v potu těžkne a pomalu schne. Syntetika je lehká a po praní schne rychle, ovšem při dlouhém nošení může víc držet zápach. U sportu proto zvažujte funkční materiál, u denního nošení klasické piké. Hustota a kvalita pleteniny se pozná na omak. Kvalitní látka po vytažení do stran vrací tvar a nevykazuje rozedranou strukturu.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Správně padnoucí polokošile nezvedá límec a ramenní švy leží na ramenou, ne na paži. Rukávy končí uprostřed paží, podle střihu volněji nebo těsněji. Délka pokrývá pas, ale nesahá dolů přes boky, pokud ji nosíte přes kalhoty. Volný střih (regular) je pohodlný pro každodenní nošení, přiléhavý (slim) vynikne u štíhlé postavy a u sportovců, kdo chtějí volnost pohybu bez vlajícího materiálu.</p>'
          '<ul><li><strong>Regular fit:</strong> klasika pro volný čas a kancelář, ponechává prostor v hrudi i v pase.</li>'
          '<li><strong>Slim fit:</strong> užší střih ke tělu, často s příměsí elastanu.</li>'
          '<li><strong>Athletic fit:</strong> širší hrudník a užší pas pro sportovní postavy.</li>'
          '<li><strong>Oversize:</strong> volný módní střih s delším rukávem a širším tělem.</li>'
          '<li><strong>Dámský střih:</strong> zpravidla kratší, s užším pasem a tvarovaným výstřihem.</li></ul>'
          '<p>Při měření se orientujte podle tabulky výrobce. Různé značky mají jiné rozměry a stejná velikost M se může lišit o několik centimetrů. Změřte hruď v nejširším místě, ne přes oblečení, a porovnejte ji s tabulkou. Pokud jste mezi velikostmi, vybírejte podle střihu: u přiléhavých modelů větší, u volných menší.</p>'
          '<h2>Límeček, rozparek a detaily</h2>'
          '<p>Kvalitu poznáte podle límečku. Dobrý límeček drží tvar i po opakovaném praní a nezvlňuje se. Mnohé polokošile mají zesílené vložky nebo pevnější úplet, jiné používají měkký límeček, který lépe hladí na krku. Rozparek má dva až tři knoflíky, u sportovních modelů se vyskytuje i zip. Boční rozparky na spodním lemu dávají volnost při pohybu a zabraňují vytahování. Výšivka znaku na hrudi je jen dekorace, kvalitu určuje šití, ne logo.</p>'
          '<h2>Polokošile pro sport</h2>'
          '<p>Na golfu, tenisu, padelu nebo squashi vybírejte funkční polokošile z lehkých materiálů, které odvádějí pot a nelepí se na tělo. Podrobnosti najdete v kategoriích <a href="/golf/">golf</a>, <a href="/tenis/">tenis</a>, <a href="/padel/">padel</a> a <a href="/squash/">squash</a>. Pro týmové sporty existují <a href="/dresy/">dresy</a> a týmové polokošile, které se objevují hlavně u trenérů a fanoušků. Děti ocení měkké materiály, které nedrhnou, a pevné švy. Při slunečném počasí zvažte i UV filtr a světlé barvy, které se méně zahřívají. Oblečení, které lépe chrání před sluncem, najdete u <a href="/lycra-a-uv-tricka/">lycra a UV triček</a>.</p>'
          '<h2>Polokošile ve městě a v kanceláři</h2>'
          '<p>V městském prostředí se polokošile nosí zasunutá i přes kalhoty, s džínami, chino kalhotami nebo se sakem. Tmavé jednobarevné kusy působí formálněji, pruhované a sytě barevné uvolněněji. Do kanceláře se hodí klasické piké v tlumených odstínech, do volného času cokoli, co vám sedí. Při kombinaci si hlídejte, aby límeček zůstal rovný a nesvíral krk. Na chladnější dny se polokošile hodí pod <a href="/mikiny/">mikinu</a> nebo <a href="/fleecove-mikiny/">fleece</a>, jelikož se nezkrabatí a límec vykoukne.</p>'
          '<h2>Barvy, vzory a kombinace</h2>'
          '<p>Barva polokošile rozhoduje o tom, kolik outfitů s ní vytvoříte. Bílá, tmavě modrá, černá a šedá patří k základním odstínům, které se hodí téměř ke všemu. Sytější tóny, jako zelená, červená nebo hořčičná, fungují jako akcent a nejlépe se kombinují s neutrálními kalhotami. Proužky působí sportovněji a vizuálně rozšiřují postavu, jednobarevné kusy jsou elegantnější. Pokud vám záleží na tom, aby oblečení vydrželo, vybírejte barvy, které nevyblednou po několika praních a nežloutnou v podpaží.</p>'
          '<p>Ve větším horku jsou světlé barvy pohodlnější, protože odráží slunce. Tmavé zase lépe skryjí pot a drobné skvrny. U sportovních modelů nezapomínejte na rozdíl mezi povrchem a vnitřkem: tmavý povrch s prodyšným vnitřkem může být ve stínu dokonale pohodlný, na prudkém slunci však hřeje.</p>'
          '<h2>Pro koho se polokošile hodí</h2>'
          '<p>Ve volném čase je polokošile volbou pro muže i ženy, kteří chtějí vypadat upraveně bez námahy. Pro sportovce je pohodlnou alternativou k tričku při hře i po ní. Studenti a zaměstnanci ocení, že nevyžaduje žehlení tak důkladně jako košile. Trenéři a rozhodčí ji nosí kvůli límečku a firemnímu vzhledu. Děti ji použijí jako školní nebo sváteční tričko. Při cestování zabere málo místa a rychle se vyvětrá, takže zvládne několik dní bez praní.</p>'
          '<h2>Jak poznat kvalitní polokošili v obchodě</h2>'
          '<p>Při online nákupu se kvalita těžko zjišťuje, proto si všímejte několika drobností. Fotografie má ukázat límeček zblízka a detail pleteniny. Složení materiálu musí být jasně uvedeno a nesmí se krýt s popisem, například „bavlna“ u produktu, který je ze syntetiky. Zkontrolujte tabulku velikostí a recenze, které se zmiňují o tom, zda model odpovídá velikosti. Pokud výrobce uvádí gramáž materiálu, vyšší hodnota znamená hustší a trvanlivější látku, nižší lehčí a vzdušnější. Důležité jsou i podmínky vrácení, u oblečení se výměna velikosti stává běžně.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku polokošil mají značky ' + B(('us-polo-assn', 'US Polo Assn'), ('celio', 'Celio'), ('under-armour', 'Under Armour'), ('polo-ralph-lauren', 'Polo Ralph Lauren'), ('lotto', 'Lotto'), ('helly-hansen', 'Helly Hansen'), ('lacoste', 'Lacoste'), ('adidas', 'Adidas'), ('tommy-hilfiger', 'Tommy Hilfiger'), ('nike', 'Nike'), ('kappa', 'Kappa'), ('fila', 'Fila'), ('puma', 'Puma'), ('calvin-klein', 'Calvin Klein'), ('fred-perry', 'Fred Perry'), ('asics', 'Asics')) + '. Některé jsou původem sportovní, jiné módní. U sportovních značek najdete častěji funkční materiály, u módních klasické piké a výrazné detaily. Na výběr tedy nemá vliv jen jméno, ale účel, ke kterému polokošili použijete.</p>'
          '<h2>Praní a údržba</h2>'
          '<p>Většina polokošil se pere v pračce při nízké teplotě. Otočte je naruby, zapněte horní knoflíky a nepoužívejte silné bělicí prostředky. Bavlněné piké se po prvním praní někdy mírně smrští, proto zvažte zakoupení o chlup větší velikosti, pokud nosíte volnější střih. Funkční materiály neperte s aviváží, která zalepí vlákna a zhorší odvod potu. Sušit je nejlépe na vzduchu, protože sušička urychluje opotřebení límečku a vytahuje materiál. Žehlete na nižší teplotu a z rubu, aby se nepoškodila výšivka.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Vybírat jen podle značky a nezkontrolovat tabulku velikostí.</li>'
          '<li>Kupovat bavlnu na sport, kde se pot dlouho drží v látce.</li>'
          '<li>Podcenit límeček a pak se divit, že se po několika praních zvlní.</li>'
          '<li>Ignorovat střih a brát vždy stejnou velikost u všech značek.</li>'
          '<li>Prát v horké vodě a sušit v sušičce na vysoký stupeň.</li></ul>',
    faq=[
        ('Z jakého materiálu má být polokošile?', 'Pro každodenní nošení se osvědčila bavlna typu piké, která je prodyšná a příjemná. Na sport se hodí funkční polyester, který rychle schne a odvádí pot. Směsi s elastanem drží tvar a pohodlně sedí. Vždy sledujte hustotu a kvalitu pleteniny.'),
        ('Jak poznám správnou velikost polokošile?', 'Změřte obvod hrudi v nejširším místě a porovnejte ho s tabulkou výrobce. Ramenní švy mají ležet na ramenou a rukávy končit uprostřed paže. Pokud jste mezi velikostmi, u přiléhavého střihu volte větší, u volného menší.'),
        ('Smrskne se polokošile při praní?', 'Bavlněné modely se mohou po prvním praní lehce smrštit, zejména při vysoké teplotě a v sušičce. Perte při nízké teplotě a sušte na vzduchu. Funkční syntetické materiály se obvykle nesrážejí, ale mohou se zhoršit při horké vodě.'),
        ('Nosí se polokošile zasunutá, nebo přes kalhoty?', 'Klasická polokošile má delší zadní díl a nosí se obojím způsobem. Do kalhot ji zasouvejte při formálnějších příležitostech a s opaskem, přes kalhoty ve volném čase. Rozhodující je délka: pokud sahá hluboko přes boky, raději ji zasuňte.'),
        ('Čím se liší sportovní polokošile od módní?', 'Sportovní kusy jsou z lehkých funkčních materiálů, které odvádějí pot, a mívají ergonomický střih pro volný pohyb. Módní se vyrábějí hlavně z bavlněného piké a pracují s barvou, detaily a značkou. Obojí můžete nosit v běžném životě.'),
        ('Hodí se polokošile do kanceláře?', 'V neformálním prostředí ano. Vybírejte tlumené odstíny, pevné piké a čistý límeček, který drží tvar. Kombinujte s chino kalhotami nebo sakem. U přísného dress codu je vhodnější klasická košile.'),
        ('Jak nejlépe polokošili prát?', 'Otočte ji naruby, zapněte horní knoflíky a perte při nízké teplotě s jemným prostředkem. U funkčních materiálů nepoužívejte aviváž. Sušte na vzduchu a žehlete z rubu na mírný stupeň, aby se nepoškodila výšivka ani límec.'),
        ('Proč se mi límeček zvlňuje?', 'Příčinou bývá nekvalitní úplet, horká voda, sušička nebo nevhodné věšení za límec. Pomáhá praní při nízké teplotě, sušení naležato a žehlení do tvaru. U velmi poškozených kusů už se tvar obnovit nedá.'),
        ('Jaká polokošile je vhodná na golf nebo tenis?', 'Lehká, pružná a rychleschnoucí z funkčního materiálu, ideálně s prodyšnými panely a UV ochranou. Střih má dovolit plný švih a zvednutí rukou. Světlé barvy se méně zahřívají na slunci. Sledujte také, zda límeček drží tvar a nedrhne.'),
        ('Mohou polokošile nosit i děti?', 'Ano, existují dětské modely z měkké bavlny nebo funkčních materiálů. Zkontrolujte švy, aby nedrhly, a pořiďte raději o něco větší velikost, ale ne tolik, aby překážela při hře. Pro školu a sport jsou praktické tmavší nebo týmové barvy.'),
        ('Dá se polokošile nosit celoročně?', 'V létě samostatně, na jaře a na podzim pod bundou nebo svetrem. V zimě se hodí pod mikinu nebo fleece, kde zůstane límec úhledně vidět. Při výběru zohledněte tloušťku materiálu, silnější piké lépe zahřeje.'),
    ])

# ------------------------------------------------------------------ termopradlo
NEW['termopradlo'] = dict(long=True,
    title='Funkční a termo prádlo: jak vybrat vrstvu k tělu | Sporteka',
    desc='Funkční a termo prádlo pánské, dámské a dětské: syntetika, merino, tloušťka, střih a praní. Průvodce výběrem a nabídky e-shopů vedle sebe.',
    intro='<p><strong>Funkční a termo prádlo</strong> je první vrstva oblečení, kterou máte na kůži. Úkol má jednoduchý, ale zásadní: odvést pot od těla, aby vás nechladil, a pomoci udržet stabilní teplotu při pohybu i při odpočinku. Dobře zvolená spodní vrstva rozhoduje o komfortu při lyžování, běhu, túře i každodenní zimě venku.</p>'
          '<p>Na Sportece porovnáte funkční prádlo od značek pro sport i outdoor a uvidíte nabídky e-shopů vedle sebe. Ve stejném světě vás zajímají i <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>, <a href="/merino-pradlo/">merino prádlo</a>, <a href="/funkcni-tricka/">funkční trička</a> a <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>. Průvodce níže vysvětluje, jaký materiál vybrat, jak prádlo vrstvit a jak ho prát. Pomůže také sestavit celou zimní výbavu, od spodní vrstvy až po bundu.</p>',
    guide='<h2>Proč funkční prádlo existuje</h2>'
          '<p>Bavlněné tričko pod bundou při pohybu nasákne potem a ten se pomalu odpařuje. Mokrá látka přenáší teplo od těla mnohem rychleji než suchá, a tak se člověk po zastavení rychle ochladí. Funkční prádlo je vyrobeno z vláken, která vlhkost od kůže odvádějí a pouštějí ji dál do další vrstvy, kde se odpaří (merino ji část pohltí a přesto zůstává teplé). Díky tomu zůstává pokožka suchá a tělo si drží teplo.</p>'
          '<h2>Syntetika, merino a směsi</h2>'
          + T(['Materiál', 'Výhody', 'Nevýhody'], [
              ['Polyester a polypropylen', 'rychle schnou, jsou lehké, odolné a snášejí časté praní', 'mohou déle držet zápach'],
              ['Polyamid', 'hladký, pevný, příjemný na dotek, dobře se barví', 'při horkém praní se může deformovat'],
              ['Merino vlna', 'zahřeje i vlhká, dlouho nepáchne, příjemná na kůži', 'schne pomaleji, citlivější na praní a opotřebení'],
              ['Směsi merina a syntetiky', 'spojují pohodlí vlny a odolnost syntetiky', 'vlastnosti závisejí na poměru složek'],
              ['Bezešvé pleteniny', 'minimum švů, nedrhnou, přiléhají k tělu', 'vyžadují přesnou velikost']]) +
          '<p>Bavlna se do spodní vrstvy pro aktivní sport nehodí, zato se dá použít na klidný den. Syntetika vítězí při intenzivním pohybu a při častém praní. Merino se osvědčilo na vícedenní túry, při cestování a pro lidi, kteří hůř snášejí zápach nebo chlad po zastavení. Podrobnosti o vlně najdete v kategorii <a href="/merino/">merino</a>.</p>'
          '<h2>Tloušťka a určení</h2>'
          '<p>Funkční prádlo se vyrábí v různých tloušťkách. Lehčí varianty se používají za tepla nebo při velké námaze, středně silné jako univerzální volba na podzim a jaro, silné pro zimu a klidné aktivity. Důležité je i to, jak se prádlo používá. Pro pohyb s vysokou intenzitou, třeba běh nebo běžky, stačí tenčí vrstva, protože se tělo samo zahřeje. Pro sedavé aktivity venku, třeba rybaření nebo čekání na zvěř, se hodí silnější.</p>'
          + T(['Aktivita', 'Doporučená spodní vrstva', 'Poznámka'], [
              ['Běh a rychlá chůze', 'tenké syntetické nebo bezešvé prádlo', 'prodyšnost je důležitější než teplo'],
              ['Sjezdové lyžování', 'středně silné prádlo, případně merino', 'pomáhá vrstvit s teplými kalhotami'],
              ['Běžky a skialpinismus', 'tenčí, vysoce prodyšné', 'při výstupu se tělo hodně potí'],
              ['Turistika na podzim a v zimě', 'středně silné, merino nebo směs', 'volte i ponožky a čepici'],
              ['Rybaření, lov, pozorování', 'silné termoprádlo', 'dlouhé sezení vyžaduje víc izolace'],
              ['Každodenní zima ve městě', 'tenké až středně silné', 'bavlna je možná, ale hůř odvádí vlhkost']]) +
          '<h2>Typy kousků</h2>'
          '<ul><li><strong>Tričko s dlouhým rukávem:</strong> základní kus pro horní část těla, často s krkem nebo zipem.</li>'
          '<li><strong>Tričko s krátkým rukávem:</strong> univerzální vrstva na jaro a léto nebo pod bundu.</li>'
          '<li><strong>Legíny a dlouhé spodky:</strong> chrání nohy před chladem a větrem pod kalhotami.</li>'
          '<li><strong>Kompletní set:</strong> sladěné horní a spodní díly, které se doplňují střihem.</li>'
          '<li><strong>Kombinéza:</strong> jednodílné prádlo pro děti a skutečné zimní podmínky.</li>'
          '<li><strong>Boxerky a spodní prádlo:</strong> funkční spodní prádlo vhodné pro dlouhé výlety.</li>'
          '<li><strong>Ponožky, nákrčníky, čepice:</strong> doplňky z funkčních materiálů, viz <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a>.</li></ul>'
          '<h2>Jak vrstvit</h2>'
          '<p>Vrstvení funguje na jednoduchém principu: spodní vrstva odvádí pot, střední hřeje, vnější chrání před větrem a deštěm. Spodní vrstva by měla přiléhat k tělu, jinak se vlhkost nepřenáší. Střední vrstvou bývá <a href="/fleecove-mikiny/">fleecová mikina</a> nebo lehká <a href="/funkcni-mikiny/">funkční mikina</a>. Vnější vrstvou je <a href="/nepromokave-bundy/">nepromokavá bunda</a>, <a href="/softshellove-bundy/">softshellová bunda</a> nebo <a href="/zimni-bundy/">zimní bunda</a>. Na nohy se přidá ještě jedna vrstva v podobě <a href="/outdoorove-kalhoty/">outdoorových kalhot</a> nebo <a href="/lyzarske-kalhoty/">lyžařských kalhot</a>. Pokud se začnete potit, odepněte nebo svlékněte střední vrstvu dřív, než propotíte spodní.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Funkční prádlo má přiléhat, ale nesmí tlačit. Příliš volné nepřenese pot, příliš těsné omezuje pohyb a může dráždit. Při zkoušce se předkloňte, zvedněte ruce nad hlavu a posaďte se. Rukávy nesmějí vyjíždět nahoru, kalhoty se nemají svinovat v pase. Pozor na švy: ploché a plošně lepené pleteniny omezují otlaky při dlouhém pohybu s batohem. Pokud nosíte těžký batoh, ověřte, že švy neleží na ramenou a lopatkách.</p>'
          '<h2>Pánské, dámské a dětské prádlo</h2>'
          '<p>Dámské střihy respektují tvar těla, mívají užší ramena, delší záda a jinak tvarovaný pas. Pánské mají širší hruď a ramena. Dětské funkční prádlo musí být především měkké a bezešvé, protože děti rychle poznají každý nepohodlný šev. Děti také rychle vyrůstají, proto se vyplatí kupovat spíše jednu vrstvu dobré kvality než několik nekvalitních. Pro lyžařské děti navazuje nabídka <a href="/detske-lyze/">dětských lyží</a> a <a href="/lyzarske-obleceni/">lyžařského oblečení</a>.</p>'
          '<h2>Švy, lemy a detaily, které rozhodují</h2>'
          '<p>U prádla, které nosíte celý den těsně na kůži, rozhodují maličkosti. Ploché švy a bezešvé konstrukce zabraňují otlakům pod popruhy batohu nebo pod lyžařskou botou. Zvýšený límec chrání krk před studeným vzduchem, zip u krku umožní rychlou regulaci. Palcové otvory na rukávech drží rukáv na místě a chrání zápěstí. Pasový lem s gumou nesmí řezat, nohavice mají končit nad kotníkem nebo pod ním podle střihu. Zónová pletenina, která má na zádech a v podpaží prodyšnější plochy, pomáhá rychleji odvádět pot z míst, kde se tvoří nejvíc.</p>'
          '<h2>Pro koho je funkční prádlo</h2>'
          '<p>Nejvíc ho využijí lyžaři, snowboardisté, běžci a turisté. Bez něj se neobejdou lidé pracující venku, rybáři, myslivci a fotografové, kteří stojí dlouho na místě. Praktické je také pro děti na zimním hřišti a pro seniory, kteří snadno prochladnou. Ve městě se hodí cyklistům, kteří dojíždějí v zimě do práce, a každému, kdo čeká na zastávce. Pro zimní sporty doplňte prádlo o <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, <a href="/cepice-a-celenky/">čepice a čelenky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a>, které tvoří stejně důležitou část výbavy.</p>'
          '<h2>Jak pečovat o prádlo při cestování</h2>'
          '<p>Na vícedenní túře nebo cestě se funkční prádlo hodí i proto, že rychle schne. Večer ho vyperte v umyvadle, pověste a ráno je suché. Merino se dá často jen vyvětrat. Vezměte si alespoň dvě sady, jednu na sobě a jednu na výměnu. Pro spaní se osvědčí suché prádlo, které jste nenosili po celý den, protože jeho teplo vás ochrání před nočním chladem. Při balení ho nestlačujte příliš a vyhněte se ostrým předmětům v batohu, které by mohly rozdrásat jemnou pleteninu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší sortiment funkčního a termo prádla na Sportece mají značky ' + B(('viking', 'Viking'), ('merrell', 'Merrell'), ('craft', 'Craft'), ('klimatex', 'Klimatex'), ('sensor', 'Sensor'), ('progress', 'Progress'), ('the-north-face', 'The North Face'), ('husky', 'Husky'), ('4f', '4F'), ('kari-traa', 'Kari Traa'), ('kilpi', 'Kilpi'), ('arcore', 'Arcore'), ('dare2b', 'Dare2b'), ('swix', 'Swix'), ('meatfly', 'Meatfly'), ('alpine-pro', 'Alpine Pro'), ('devold', 'Devold')) + '. Některé značky se specializují na vlnu, jiné na syntetické pleteniny a bezešvé technologie, další na lyžařský nebo běžecký trh. Při porovnání vždy sledujte složení a určení, ne jen jméno.</p>'
          '<h2>Praní a údržba</h2>'
          '<p>Funkční prádlo perte při nízké teplotě, nejlépe podle štítku. Nepoužívejte aviváž ani silné bělicí prostředky, které ucpávají vlákna a snižují schopnost odvádět vlhkost. Syntetiku můžete prát častěji, merino šetrněji a s jemným prostředkem, ideálně na vlnu. Sušte na vzduchu, mimo přímé slunce a topení. Příliš vysoká teplota poškodí elastická vlákna i přilnavost. Po sezóně prádlo vyperte, zcela vysušte a uložte na suchém místě. Pokud je prádlo z merina, chraňte ho před moly.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Kupovat prádlo o velikost větší, aby se lépe oblékalo, a tím ztratit funkci.</li>'
          '<li>Volit bavlnu pro aktivní sport kvůli příjemnému pocitu při oblékání.</li>'
          '<li>Podcenit tloušťku a pořídit zimní prádlo na intenzivní běh.</li>'
          '<li>Prát s aviváží, která zničí odvod potu.</li>'
          '<li>Spoléhat se jen na jednu vrstvu a zapomenout na větrovku nebo bundu.</li>'
          '<li>Neověřit švy a pak řešit otlaky pod popruhy batohu.</li></ul>'
          '<h2>Kdy a kde kupovat</h2>'
          '<p>Největší výběr je na začátku podzimu, kdy e-shopy doplňují zimní sortiment. Slevy se objevují na konci zimy, ale chybí některé velikosti. Funkční prádlo se vyplatí kupovat ve více kusech, protože jedno bývá v praní a druhé na těle. Při výběru porovnávejte složení, hmotnost látky, střih i podmínky vrácení. Kromě sportu využijete prádlo také při zimních výletech, na rybách, při práci venku a při každodenních cestách v mrazu.</p>',
    faq=[
        ('Co je funkční prádlo a čím se liší od běžného?', 'Je to spodní vrstva z vláken, která odvádějí pot od těla, místo aby ho nasákla (merino pot částečně pohltí, ale i tak hřeje). Bavlněné prádlo vlhkost drží a ochlazuje, funkční ji přenáší dál a rychleji schne. Proto se hodí na sport, výlety a každý pohyb ve chladu.'),
        ('Je lepší merino, nebo syntetika?', 'Merino zahřeje i vlhké a dlouho nepáchne, hodí se na cestování a vícedenní túry. Syntetika rychleji schne, je odolnější a snáší časté praní. Pro intenzivní sport je často praktičtější syntetika, pro delší nošení merino.'),
        ('Jakou tloušťku funkčního prádla zvolit?', 'Řiďte se intenzitou pohybu a teplotou. Při běhu a běžkách stačí tenčí vrstva, při jízdě na lyžích středně silná, při sedavých činnostech venku silnější. Kdo se rychle potí, ať raději vrství více tenčích kusů než jeden silný.'),
        ('Má funkční prádlo přiléhat k tělu?', 'Ano, přiléhavý střih zajišťuje, že vlhkost přechází z kůže do materiálu. Prádlo však nesmí tlačit ani omezovat pohyb. Při zkoušce se předkloňte, zvedněte ruce a posaďte se, abyste zjistili, kde napíná nebo se svinuje.'),
        ('Jak prát funkční prádlo?', 'Při nízké teplotě, bez aviváže a bez silných bělidel. Syntetiku můžete prát častěji, merino šetrněji s prostředkem na vlnu. Sušte na vzduchu mimo přímé slunce a topení, aby se vlákna nepoškodila.'),
        ('Proč funkční prádlo nesmí být prané s aviváží?', 'Aviváž pokryje vlákna tenkým filmem, který zhoršuje odvod potu. Prádlo pak vlhkost drží a začne více zapáchat. Funkce se může zhoršit a obnovuje se obtížně. Použijte specializovaný prací prostředek nebo jen obyčejný jemný prášek.'),
        ('Mohou funkční prádlo nosit děti?', 'Ano, existují dětské varianty, které jsou měkké a bez drsných švů. Vyplatí se zvolit vrstvu odpovídající aktivitě: tenčí pod lyžařské oblečení, silnější na dlouhý pobyt venku. Dbejte na správnou velikost a kontrolujte, zda neškrtí.'),
        ('Jak funkční prádlo vrstvit s dalším oblečením?', 'Spodní vrstva odvádí pot, střední hřeje (fleece, mikina) a vnější chrání před větrem a deštěm. Při pohybu odepněte nebo svlékněte střední vrstvu dříve, než propotíte spodní. Všechny vrstvy musí na sebe navazovat a nesmí se tlačit.'),
        ('Hodí se funkční prádlo i na každodenní nošení?', 'Ano, v zimě pod běžné oblečení při cestě do práce nebo na procházku. Vyberte tenčí variantu, aby se pod oblečením nepotilo. V kanceláři se hodí merino, které nezapáchá, i když ho nosíte celý den.'),
        ('Kdy je potřeba funkční prádlo vyměnit?', 'Když se materiál vydře, ztratí pružnost, začnou se dělat žmolky nebo prádlo i po vyprání zapáchá. U merina se objevují malé dírky po molech. Funkční vlastnosti slábnou postupně, proto sledujte, zda stále odvádí pot.'),
        ('Dá se funkční prádlo kombinovat s bavlněnými tričky?', 'Přímo na kůži má být funkční prádlo, bavlněné tričko až nad ním. Bavlna na kůži pot nasákne a ochladí vás. Pokud ale nosíte bavlnu jako střední vrstvu, sníží se odvod vlhkosti dál od těla. Pro aktivní pohyb se proto drží syntetika nebo vlna.'),
    ])
