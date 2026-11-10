"""sporteka.cz — brand texts wave 219: sensor, cmp, gola, husky.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ sensor
NEW['sensor'] = dict(
    title='Sensor: merino prádlo, trička a ponožky ve srovnání',
    desc='Sensor v katalogu Sporteky: merino trička, spodní prádlo, mikiny a ponožky pro muže, ženy i děti. Jak vybrat řadu, velikost a kdy hledat slevy.',
    intro='<p>Sensor je v katalogu Sporteky především značkou merino oblečení. Většinu nabídky tvoří <a href="/merino-tricka/">merino trička a tílka</a>, hned za nimi stojí <a href="/merino-pradlo/">merino spodní prádlo a legíny</a> a <a href="/merino-mikiny/">merino mikiny a svetry</a>. Menší část pokrývají funkční termoprádlo, merino doplňky, ponožky a pár kousků pro cyklistiku. '
          'Zboží je rozdělené pro muže, ženy i děti, takže si tu najde své celá rodina. Stránka vysvětluje, jak se orientovat v názvech řad jako Active, Air, DF, Upper nebo Bold, kdy zvolit triko s dlouhým rukávem a kdy s krátkým, jak vybírat ponožky a jak pečovat o vlnu, aby vydržela. Sporteka sama nic neprodává, jen porovnává nabídky obchodů a ukazuje, kde je vaše velikost a barva skladem.</p>',
    guide='<h2>Co Sensor v katalogu nabízí</h2>'
          '<p>Značka se v naší nabídce drží jednoho materiálu a jednoho způsobu použití: vrstvení oblečení pro pohyb a chladné počasí. Kdo hledá Sensor, obvykle hledá spodní vrstvu, která se nosí přímo na těle. Rozložení kategorií to dobře ukazuje.</p>'
          + T(['Skupina', 'Kategorie značky', 'Na co se hodí'], [
              ['Trička', '<a href="/merino-tricka/">merino trička a tílka</a>, <a href="/sportovni-tricka/">sportovní trička</a>', 'spodní vrstva na túru, běh, každodenní nošení'],
              ['Spodní prádlo', '<a href="/merino-pradlo/">merino prádlo a legíny</a>, <a href="/termopradlo/">termoprádlo</a>', 'zima, lyže, dlouhé dny venku'],
              ['Střední vrstva', '<a href="/merino-mikiny/">merino mikiny a svetry</a>', 'teplo nad spodním tričkem'],
              ['Doplňky', '<a href="/merino-doplnky/">čepice, nákrčníky a rukavice</a>', 'chladné ráno, ochrana krku a hlavy'],
              ['Ponožky', '<a href="/merino-ponozky/">merino ponožky</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a>', 'hory, běžky, delší chůze'],
              ['Kolo', '<a href="/cyklisticke-obleceni/">cyklistické oblečení</a>, <a href="/cyklo-prislusenstvi/">příslušenství</a>', 'jízda v sezoně i mimo ni']]) +
          '<p>Z toho plyne praktický závěr: Sensor v katalogu není značka pro „všechno“, ale specialista na vlněné vrstvy. Pokud potřebujete bundu nebo boty, hledejte jinde; pokud chcete něco pod bundu, tady je výběr velký.</p>'
          '<h2>Proč právě merino a čím se liší od syntetiky</h2>'
          '<p>Merino je jemná ovčí vlna, která na kůži neškrábe tak jako hrubý svetr. Vlákno umí pojmout vlhkost, aniž by se na omak okamžitě zdálo mokré, a proto se v něm při chůzi do kopce nemrzne tak rychle jako v promočené bavlně. Další známá přednost je, že pach z potu se v něm drží méně než v běžném syntetickém triku, takže je můžete nosit několik dní po sobě na výletě bez praní. Nevýhodou bývá pomalejší schnutí než u čistého polyesteru a vyšší citlivost na hrubé zacházení.</p>'
          '<p>Proto se ve výrobě často mísí: do vlny se přidává syntetické vlákno pro pevnost a pružnost. Přesné složení najdete v popisu u každého produktu u obchodu, a právě na něj se vyplatí dívat. Vyšší podíl vlny je příjemnější a teplejší, vyšší podíl syntetiky odolnější a rychleji schne. Žádné číslo není správné pro všechny, záleží na tom, co s oblečením budete dělat.</p>'
          '<h2>Jak číst názvy řad</h2>'
          '<p>V názvech produktů se opakují slova psaná velkými písmeny. Značka je používá jako označení řady nebo střihu a pomáhá vám rychle odhadnout, co kupujete. Přesné parametry řady vždy ověřte v popisu, tady uvádíme jen to, co plyne ze samotných názvů.</p>'
          + T(['Označení v názvu', 'Co z názvu vyplývá', 'Kdy dává smysl'], [
              ['Merino Active', 'běžné sportovní triko, spodky a další kusy', 'denní nošení, běh, túra'],
              ['Merino Air', 'řada triček i dětských setů', 'teplejší dny, cestování, lehká vrstva'],
              ['Merino DF', 'trička, mikiny s kapucí, termo spodky', 'chladnější počasí, volnější vrstva'],
              ['Merino Upper', 'mikiny a svetry', 'střední vrstva nad tričkem'],
              ['Merino Bold', 'trička s rolákem a funkční spodky', 'zima, vyšší límec na krk'],
              ['Traveller', 'dámské mikiny a trička', 'cestování, kombinace s běžným oděvem'],
              ['Zero, Hiking', 'ponožky', 'lyže, turistika, chladné nohy']]) +
          '<p>Slovo „set“ u dětských kousků znamená, že v balení je triko i spodky, což bývá výhodnější než koupit každý díl zvlášť. Naopak, pokud chcete jen jeden kus, pečlivě zkontrolujte, zda neobjednáváte celý set.</p>'
          '<h2>Pro koho je zboží určené</h2>'
          '<p>Nabídka je rozdělena mezi pánské a dámské kousky téměř vyrovnaně, k tomu přibývá znatelný díl dětského oblečení a malé množství unisex modelů. Dámská trička bývají užší v pase a delší v zádech, pánská volnější přes hrudník. U vlněného prádla se nevyplatí kupovat větší velikost „pro jistotu“, protože spodní vrstva má přiléhat k tělu. Jen tak totiž odvádí vlhkost a hřeje.</p>'
          '<ul><li><strong>Muži:</strong> volte podle obvodu hrudníku a délky těla; vysoká postava si pozorně přečte tabulku délky trupu.</li>'
          '<li><strong>Ženy:</strong> pozor na rozdíl mezi střihy; sportovní trička jsou přiléhavější než ta nošená do města.</li>'
          '<li><strong>Děti:</strong> kupujte spíš na sezonu a počítejte s růstem; vlna se při správném praní nesráží, ale vyrostlé dítě je rychlejší než oblečení.</li>'
          '<li><strong>Unisex:</strong> menší část nabídky, vhodná pro doplňky a volnější střihy.</li></ul>'
          '<p>Odpovídající výběr najdete také ve filtrech, například <a href="/merino-ponozky-damske/">dámské merino ponožky</a>, <a href="/merino-ponozky-panske/">pánské merino ponožky</a> a <a href="/detske-merino-ponozky/">dětské merino ponožky</a>.</p>'
          '<h2>Triko s dlouhým a krátkým rukávem</h2>'
          '<p>Častá otázka zní, který rukáv zvolit. Dlouhý rukáv je univerzálnější: v zimě hřeje, na jaře a na podzim chrání před větrem a v horku ochrání ruce před sluncem a komáry. Krátký rukáv se hodí do tepla a jako spodní vrstva pod bundu, když nechcete mít zbytečné vrstvy na pažích. Kdo si chce koupit jen jedno triko, vezme dlouhý rukáv; kdo chodí pravidelně a vrství, pořídí obě délky.</p>'
          '<p>Další rozhodnutí je mezi tenčí a hustší pleteninou. Lehčí materiál je určený na pohyb, hustší na klidnější chůzi a chlad. Podle názvu to nepoznáte vždy, proto čtěte gramáž v popisu a porovnávejte ji mezi obchody. Většinou ji najdete v technických parametrech.</p>'
          '<h2>Merino ponožky, spodky a doplňky</h2>'
          '<p>Ponožky jsou kus oblečení, u kterého se chyby ve výběru projeví okamžitě puchýřem. Vlněná ponožka by měla sedět bez záhybů, mít vyztužené místo na patě a špičce a nesmí být ani příliš široká, ani stažená. Lyžařské modely se vyznačují delším lýtkem a tenčím materiálem na přední straně holeně, aby bota netlačila. Turistické jsou silnější v chodidle. Kategorie <a href="/merino-ponozky/">merino ponožky</a> i <a href="/sportovni-ponozky/">sportovní ponožky</a> proto procházejte s ohledem na činnost.</p>'
          '<p>Spodky a legíny z merina se nosí jako spodní vrstva pod kalhoty. V kategorii <a href="/merino-pradlo/">merino prádlo</a> hledejte střih podle toho, zda potřebujete krátké, dlouhé nebo sportovní. Pro nejchladnější dny se kombinuje s <a href="/termopradlo/">funkčním termoprádlem</a> na dalších vrstvách. Doplňky, tedy čepice, nákrčníky a rukavice, jsou lehké, ale ochrání nejvíc zranitelná místa.</p>'
          '<h2>Jak vrstvit a jak se liší od konkurence</h2>'
          '<p>Základní pravidlo vrstvení: nejblíž k tělu spodní vrstva, nad ní izolační, navrch ochrana před větrem a deštěm. Sensor zde pokrývá první dvě. Z konkurentů, kteří dělají podobné merino oblečení, v katalogu najdete například <a href="/znacka/icebreaker/">Icebreaker</a>; mimo čisté merino nabízejí vrstvy také <a href="/znacka/hannah/">Hannah</a>, <a href="/znacka/alpine-pro/">Alpine Pro</a> a <a href="/znacka/loap/">Loap</a>. Rozdíl nehledejte ve slibech, ale v konkrétním složení, střihu a rozsahu velikostí u daného produktu.</p>'
          '<p>Při srovnání se vyplatí sledovat tři věci: kolik procent vlny materiál obsahuje, jak je triko dlouhé a zda má plochou švy, které netlačí pod popruhem batohu. Pokud nosíte těžký batoh, ploché švy jsou důležitější než barva.</p>'
          '<h2>Péče a životnost vlněného oblečení</h2>'
          '<p>Vlna snese víc, než se myslí, ale nelíbí se jí horká voda a bubnová sušička. Běžná doporučení platí pro většinu výrobků, vždy ale zkontrolujte štítek.</p>'
          '<ul><li><strong>Praní:</strong> šetrný program na nízkou teplotu, prací prostředek bez enzymů a bez bělidla.</li>'
          '<li><strong>Avivážní přípravky:</strong> vynechejte, zalepují vlákno a zhoršují schopnost odvádět vlhkost.</li>'
          '<li><strong>Sušení:</strong> pověste na vzduchu ve stínu; vlna na radiátoru tuhne.</li>'
          '<li><strong>Větrání:</strong> často stačí přes noc pověsit ven, pach se vyvětrá.</li>'
          '<li><strong>Molice:</strong> při skladování přes léto čisté kusy uzavřete do plátěného obalu nebo látkového pytle.</li>'
          '<li><strong>Drobné díry:</strong> zašijte hned, než se rozšíří.</li></ul>'
          '<p>Dobře ošetřené triko vydrží řadu sezon, což je argument pro vyšší pořizovací cenu. Pokud vás zajímá celý obor, podívejte se i na kategorii <a href="/trailove-boty/">trailových bot</a> a obuv, protože vrstvy mají smysl jen tehdy, když zbytek výbavy odpovídá.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Vlněné oblečení je sezonní zboží. Nejvíc se prodává na podzim, nejvíc zlevňuje na konci zimy a v létě, kdy obchody uvolňují sklad. Slevy na konkrétní barvy a velikosti se objevují celoročně, protože prodejci vyprodávají odstíny, které se prodávají hůř. Proto se vyplatí přijmout méně oblíbenou barvu a ušetřit. Sledujte také změny názvů řad, protože při příchodu nové kolekce klesá cena té předchozí.</p>'
          '<p>Využijte možnosti filtrovat podle velikosti a barvy a porovnat nabídky mezi obchody. Dívejte se na celkovou cenu včetně dopravy, na dostupnost vaší velikosti a podmínky vrácení. Poslední velikosti v sadě bývají nejlevnější, ale vrácení bývá stejně důležité jako sleva, pokud se střih ukáže jako nevhodný.</p>',
    faq=[
        ('Pro co je značka Sensor v katalogu nejvhodnější?', 'Hlavně pro spodní a střední vrstvy z merino vlny: trička, spodní prádlo, mikiny, ponožky a doplňky. Bundy ani boty tu nehledejte, těžiště nabídky je v oblečení, které se nosí blízko těla.'),
        ('Je merino lepší než syntetické prádlo?', 'Není lepší obecně, je jiné. Merino méně zapáchá, příjemně hřeje i vlhké a nedrhne, syntetika rychleji schne a lépe snáší hrubé zacházení. Mnoho lidí kombinuje obojí podle činnosti.'),
        ('Jakou velikost mám zvolit?', 'Spodní vrstva má přiléhat, ale netlačit. Změřte hrudník nebo boky, porovnejte s tabulkou v obchodě a při váhání se vyhněte velikosti navíc, protože volné prádlo špatně odvádí vlhkost.'),
        ('Co znamenají názvy Active, Air, DF nebo Upper?', 'Jsou to označení řad a střihů. Z názvů produktů plyne například to, že Upper označuje mikiny a svetry, kdežto Active a Air trička. Přesné parametry si ověřte v popisu u daného obchodu.'),
        ('Mám koupit triko s dlouhým, nebo krátkým rukávem?', 'Pokud chcete jedno univerzální, vezměte dlouhý rukáv. Krátký se hodí do tepla a pod bundu. Kdo chodí do hor pravidelně, časem stejně pořídí obě délky.'),
        ('Jak prát merino oblečení, aby se nesrazilo?', 'Šetrný program na nízké teplotě, bez aviváže a bez sušičky. Sušte rozložené na vzduchu. Přesný postup vždy hledejte na štítku, protože směsi vlny se syntetikou snášejí praní různě.'),
        ('Dá se merino nosit celý rok?', 'Ano, lehčí trička se nosí v teple a hustší vrstvy v zimě. Rozhodující je gramáž a střih, nikoli roční období. Pro léto vybírejte tenčí kusy, pro zimu hustší nebo v kombinaci s termoprádlem.'),
        ('Jsou v nabídce i dětské kusy?', 'Ano, dětské oblečení tvoří znatelnou část nabídky, včetně setů s tričkem a spodky a dětských ponožek. U dětí počítejte s růstem a kupujte primárně na jednu sezonu.'),
        ('Kdy bývají slevy na merino oblečení nejvyšší?', 'Největší slevy bývají na konci zimy a v létě, kdy prodejci uvolňují sklad. Celoročně se zlevňují méně oblíbené barvy a poslední velikosti, takže stačí porovnat obchody a nespěchat.'),
    ])

# ------------------------------------------------------------------ cmp
NEW['cmp'] = dict(
    title='CMP: trekové boty, sandály a lyžařské oblečení',
    desc='CMP v katalogu Sporteky: trailové a trekové boty, sandály, sněhule, lyžařské kalhoty a bundy. Jak vybrat model, velikost a kdy hledat slevy.',
    intro='<p>CMP je v katalogu Sporteky značkou outdoorové obuvi a zimního oblečení. Největší skupinu tvoří <a href="/trailove-boty/">trailové běžecké boty</a>, za nimi jsou <a href="/trekova-obuv/">trekové boty</a>, <a href="/tenisky/">tenisky a volnočasové boty</a> a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>. K tomu přibývají sandály, sněhule a lyžařské kalhoty a bundy. '
          'Nabídka míří na pány i dámy a dětská obuv tvoří třetinu zboží, což je pro outdoorovou značku neobvyklé a pro rodiny praktické. Na této stránce rozebíráme rozdíl mezi nízkou, polovysokou a vysokou botou, ukazujeme, jak číst názvy typu Rige, Rigel Mid nebo Hamal, jak vybírat zimní obuv pro děti a kdy se vyplatí membrána. Sporteka sama neprodává, jen porovnává obchody podle ceny, dostupnosti velikostí a podmínek vrácení.</p>',
    guide='<h2>Co CMP v katalogu nabízí</h2>'
          '<p>Pohled na kategorie ukazuje značku, která se opírá o obuv do terénu a doplňuje ji oblečením na sníh. Textil je v menšině, ale pro lyžařské dny pokrývá základní kusy.</p>'
          + T(['Oblast', 'Kategorie značky', 'Pro koho a na co'], [
              ['Terénní běh a chůze', '<a href="/trailove-boty/">trailové boty</a>, <a href="/trekova-obuv/">trekové boty</a>', 'stezky, výlety, delší chůze'],
              ['Členkové boty', '<a href="/vysoke-trekove-boty/">vysoké trekové boty</a>', 'nerovný terén, těžší batoh'],
              ['Město a volný čas', '<a href="/tenisky/">tenisky a volnočasové boty</a>', 'každodenní obuv, lehké výlety'],
              ['Léto', '<a href="/sandaly/">sportovní sandály</a>, <a href="/pantofle-a-zabky/">pantofle a žabky</a>', 'vodní turistika, kemp, teplé dny'],
              ['Zima', '<a href="/zimni-obuv/">zimní boty a sněhule</a>, <a href="/zimni-bundy/">zimní bundy</a>', 'sníh, mráz, dětské zimní hry'],
              ['Lyže a snowboard', '<a href="/lyzarske-kalhoty/">kalhoty</a>, <a href="/lyzarske-bundy/">bundy</a>', 'sjezdovka, zimní sporty'],
              ['Mezisezóna', '<a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, <a href="/mikiny/">mikiny</a>', 'chladnější dny, vrstvení']]) +
          '<p>Z kategorií je vidět, že značka je dobrá volba, když potřebujete obuv pro víc situací najednou: od krátké procházky po nerovném povrchu po sezónní boty pro děti.</p>'
          '<h2>Nízká, polovysoká nebo vysoká bota</h2>'
          '<p>Nejčastější otázka u trekové obuvi je výška svršku. Nízká bota je lehká, ventiluje a hodí se na pěšiny a výlety bez těžkého batohu. Polovysoká, v názvech často označená slovem Mid, chrání kotník a drží nohu při sestupu. Vysoká bota je určená pro nerovný terén, kamení a delší výlety s nákladem. Výška svršku ale kotník nezafixuje sama o sobě; pevnost závisí na podrážce a šněrování.</p>'
          + T(['Typ', 'Výhody', 'Nevýhody'], [
              ['Nízká', 'nízká váha, prodyšnost, svoboda pohybu', 'menší ochrana kotníku, do bláta a sněhu proniká voda'],
              ['Polovysoká (Mid)', 'kompromis, chrání před úderem a kamínky', 'o něco teplejší a těžší'],
              ['Vysoká', 'podpora kotníku, ochrana před vlhkem a trním', 'horší prodyšnost, vyšší váha'],
              ['Sandál', 'vzdušnost, schnutí, pohodlí v teple', 'chrání jen chodidlo, ne kotník']]) +
          '<p>Chcete-li vidět konkrétní filtry, otevřete si výběr <a href="/damske-trekove-boty/">dámské trekové boty</a>, <a href="/trekove-boty-panske/">pánské trekové boty</a> a <a href="/detske-trekove-boty/">dětské trekové boty</a>, kde najdete i další značky pro porovnání.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>V katalogu se opakují pojmenování jako Rige, Rigel Mid, Vertyx, Mintaka, Dhenieb, Almaak nebo Hamal. Jde o názvy modelů, jejichž význam si výrobce určuje sám, ale pomáhají v orientaci. Důležitější než samotné jméno jsou přívlastky v názvu produktu, protože ukazují parametry.</p>'
          '<ul><li><strong>„Nepromokavé“ nebo „s membránou“:</strong> boty mají vnitřní vrstvu proti vodě, což se hodí do deště, méně do horka.</li>'
          '<li><strong>„Voděodolné“:</strong> odolává stříkající vodě, ne dlouhému stání v louži.</li>'
          '<li><strong>„Kožené“:</strong> pevnější svršek, vyžaduje ošetření, hůř schne.</li>'
          '<li><strong>„Nízké“, „Mid“, „vysoké“:</strong> výška svršku, viz tabulka výše.</li>'
          '<li><strong>„Wp“:</strong> v názvu zkratka, která v kontextu odkazuje na odolnost vůči vodě; podrobnosti ověřte v popisu.</li></ul>'
          '<p>Rozdíl mezi „voděodolné“ a „nepromokavé“ je důležitý. Pokud jdete na delší túru v dešti, volte nepromokavý model a ponožky, které odvádějí vlhkost. Při suchém počasí a v létě je membrána spíš na škodu, protože noha se potí.</p>'
          '<h2>Trailové boty versus trekové</h2>'
          '<p>Trailová bota je určená pro běh po cestách a stezkách, má tlumenou střední podešev a výraznější vzorek. Trekové boty jsou tužší a těžší, určené na pomalejší chůzi a těžší zátěž. V katalogu CMP je trailových modelů nejvíc, což ukazuje na obuv pro aktivní výlety, nikoli jen pro těžký trek. Pro delší túru s batohem a na ostrém kamení je bezpečnější tužší podešev, pro svižnou chůzi a běh lepší tlumení trailovky. Obě kategorie najdete v přehledu <a href="/trailove-boty/">trailové boty</a> a <a href="/trekova-obuv/">trekové boty</a>.</p>'
          '<p>Pokud jedete do hor, ale nejste si jistí, zvolte polovysokou botu s vyšším vzorkem podrážky. Ukázkou praktického kompromisu jsou nízké modely s membránou: lehké, ale v dešti suché. Zejména pro cesty do Alp a Tater si vyberte botu s pevným špičkovým lemem, který chrání prsty při nárazu o kámen.</p>'
          '<h2>Velikost, šířka a vložky</h2>'
          '<p>Outdoorová obuv se kupuje větší než běžná. Při chůzi z kopce noha sjíždí dopředu a při dlouhé túře otéká, takže potřebujete prostor asi na šířku palce před prsty. Změřte nohu navečer, kdy je největší, a berte ponožky, ve kterých budete chodit. Pokud si nejste jistí, objednejte dvě velikosti a jednu vraťte; Sporteka vám ukáže obchody, které vrácení usnadňují.</p>'
          '<ul><li>Při šněrování nejprve utáhněte v prstech volněji a v nártu pevněji, jinak se pata zvedá.</li>'
          '<li>Při obtížném terénu použijte různé uzly na horní a spodní části šněrování.</li>'
          '<li>Vložku vyměňte, pokud potřebujete vyšší podporu klenby; originální bývá tenká.</li>'
          '<li>U dětí nekupujte o dvě čísla větší, bota pak ztrácí oporu.</li></ul>'
          '<h2>Dětská obuv a sněhule</h2>'
          '<p>Dětské zboží tvoří v nabídce značné procento, a to jak boty, tak zimní oblečení. Zimní dětské boty jsou ve výběru označené slovy jako „vysoké“, „zateplené“ a „nepromokavé“. Právě tyto tři přívlastky hledejte společně: bez zateplení dítě zmrzne, bez nepromokavosti zmokne a bez vysokého svršku mu napadá sníh do boty. V kategorii <a href="/zimni-obuv/">zimní boty a sněhule</a> proto kontrolujte všechny tři parametry zároveň a nezapomeňte na pevné zapínání na suchý zip nebo šněrování, které zvládne i dítě samo.</p>'
          '<p>Dětské noze se vyplatí odlehčit: příliš těžká bota unavuje, takže dítě rychleji odmítne jít. Při růstu počítejte s tím, že obuv vydrží zhruba jednu sezonu, a pokud ji nosí sourozenec, nechte ji vyschnout a vyčistěte.</p>'
          '<h2>Lyžařské kalhoty a bundy</h2>'
          '<p>Z oblečení v nabídce převažují lyžařské kalhoty a bundy, doplněné o zimní a jarní bundy. Pro sjezdovku jsou důležité tři věci: voděodolnost materiálu, zateplení a střih umožňující vrstvení. Kalhoty mají mít zesílené spodní lemy a sněhový límec, který se přiloží k botě. Bundy se vyplatí zvolit s kapucí přes helmu, pokud ji nosíte, a s kapsou na skipas. Přehled najdete v kategoriích <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a> a <a href="/lyzarske-bundy/">lyžařské bundy</a>.</p>'
          '<p>V horách je lepší vrstvit než oblékat jednu silnou bundu: spodní termoprádlo, střední vrstvu a vrchní ochranu. Doporučení, jak spodní vrstvy vybrat, najdete u značky <a href="/znacka/sensor/">Sensor</a>, jejíž merino prádlo se pod lyžařské oblečení často nosí. Podobnou bundovou nabídku mají i <a href="/znacka/hannah/">Hannah</a> a <a href="/znacka/alpine-pro/">Alpine Pro</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Obuv po túře vyndejte vložky, vyklepejte bláto a nechte ji vyschnout při pokojové teplotě. Žádný radiátor, žádné vařiče, protože lepidlo se může oddělit. Kožené modely ošetřete vosky nebo impregnací, membránové dle pokynů výrobce. Lyžařské oblečení perte podle štítku a pravidelně obnovujte impregnaci, aby voda dál stékala. Sandály opláchněte a nechte vyschnout ve stínu, aby popruhy neztvrdly.</p>'
          '<h2>Jak sestavit výbavu na výlet</h2>'
          '<p>Pokud si skládáte výbavu od nuly, začněte u obuvi, protože ta rozhoduje o tom, zda vás výlet bude bavit. Teprve potom doplňte ponožky, které se k botě hodí, a pak oblečení. Na jednodenní výlet za mírného počasí stačí nízká trailová nebo treková bota, lehká bunda z kategorie <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> a ponožky bez švů v místě palce. Na víkendovou túru s batohem přidejte polovysokou botu a rezervní ponožky. Pro zimní výlet vyberte zimní obuv s hrubším vzorkem a nepromokavé kalhoty.</p>'
          '<p>Nepodceňujte ponožky. I nejlepší bota způsobí puchýře, když do ní oblečete bavlněnou ponožku, která drží vlhkost. Kategorie <a href="/sportovni-ponozky/">sportovní ponožky</a> nabízí tenčí i silnější provedení a v katalogu najdete i ponožky v názvu s označením Ultralight. Dobrá ponožka se k botě nemusí hodit barvou, ale tloušťkou musí.</p>'
          '<h2>Sandály, žabky a pantofle</h2>'
          '<p>Turistické sandály jsou praktické na vodní výlety, do kempu a do horka. Měly by mít pevné zapínání, podrážku s vyšším vzorkem a popruhy, které nedrhnou. V sandálech se nedoporučuje chodit po ostré skále ani nosit těžký batoh, protože nechrání prsty. Žabky a pantofle slouží k odpočinku po túře a na pláž. V horkých dnech se hodí i do města, ale na delší chůzi nejsou určeny.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní zboží zlevňuje na konci sezony, v únoru a březnu, letní boty a sandály ke konci léta. Trekové boty jsou celoročně rozprodávané po řadách: když se objeví nová barva modelu, předchozí zlevní. V nabídce sledujte více obchodů najednou, protože velikosti se rozbíhají a ty nejběžnější zmizí první. Vždy porovnejte celkovou cenu včetně dopravy a zjistěte, jak funguje vrácení; u obuvi je to stejně důležité jako sleva.</p>',
    faq=[
        ('Pro koho je značka CMP v katalogu vhodná?', 'Pro muže, ženy i děti. Pánské a dámské zboží je zastoupeno téměř stejně a dětská obuv i oblečení tvoří znatelnou část, takže si rodina může vybrat u jedné značky.'),
        ('Jaká je hlavní kategorie CMP?', 'Obuv do terénu. Nejvíc je trailových běžeckých bot, následují trekové boty, tenisky, vysoké trekové boty a sandály. Oblečení se soustřeďuje na lyžařské kalhoty a bundy.'),
        ('Jak vybrat mezi nízkou a vysokou trekovou botou?', 'Podle terénu a zátěže. Nízká je lehká a prodyšná pro stezky bez těžkého batohu, vysoká chrání kotník na kamení a s nákladem. Polovysoká (Mid) je kompromis pro většinu výletů.'),
        ('Co znamená, že je bota nepromokavá nebo voděodolná?', 'Nepromokavá má obvykle vnitřní membránu a zvládne déšť. Voděodolná vydrží stříkající vodu, ale ne dlouhé stání v louži. V horku se membránová obuv hůř větrá.'),
        ('Jakou velikost trekové obuvi mám koupit?', 'Zhruba o půl až celé číslo větší než běžnou obuv, protože noha při chůzi z kopce klouže a otéká. Měřte navečer, v ponožkách, ve kterých půjdete, a ponechte před prsty prostor.'),
        ('Jak vybrat zimní boty pro děti?', 'Hledejte kombinaci zateplení, nepromokavosti a vyššího svršku, aby sníh nenapadal dovnitř. Pro malé děti je praktický suchý zip nebo rychlé zapínání, které zvládnou samy.'),
        ('Jak pečovat o trekové boty?', 'Po túře vyjměte vložky, vyklepejte bláto a sušte při pokojové teplotě. Kůži ošetřete vosky, membránu impregnací dle štítku. Nikdy nesušte na radiátoru ani v blízkosti ohně.'),
        ('Co si představit pod názvy jako Rige nebo Rigel Mid?', 'Jsou to názvy modelů. Význam určuje výrobce, takže se řiďte přívlastky v názvu produktu, například výškou svršku, membránou nebo zateplením, a podrobnostmi v popisu.'),
        ('Kdy hledat slevy na obuv CMP?', 'Zimní obuv a oblečení bývají levnější koncem zimy, sandály a letní boty koncem léta. Celoročně zlevňují starší barvy modelů, takže srovnání více obchodů zpravidla ušetří nejvíc.'),
    ])

# ------------------------------------------------------------------ gola
NEW['gola'] = dict(
    title='Gola: tenisky pro ženy, muže a děti ve srovnání cen',
    desc='Gola v katalogu Sporteky: retro tenisky Elan, Tornado, Harrier a další pro ženy, muže i děti. Jak vybrat model, velikost a kdy hledat slevy.',
    intro='<p>Gola je v katalogu Sporteky téměř výhradně značkou tenisek. Drtivá většina nabídky patří do kategorie <a href="/tenisky/">tenisky a volnočasové boty</a>, k tomu přibývá pár kousků pro badminton, trénink a pantofle. Jsou to modely každodenní obuvi s retro vzhledem, určené pro ženy, pány i děti, v pestré škále barev od bílé po zelenou. '
          'Najdete tu opakující se názvy jako Elan, Tornado, Harrier, Daytona, Firefly nebo Bullet, často v několika materiálech a barvách. Na této stránce vysvětlujeme, jak mezi nimi vybírat, v čem se liší semišové a nylonové provedení, jak zvolit velikost a jak o tenisky pečovat. Sporteka sama neprodává, jen porovnává nabídky obchodů: uvidíte, kde je vaše číslo skladem a jak vypadají podmínky vrácení.</p>',
    guide='<h2>Co Gola v katalogu nabízí</h2>'
          '<p>Rozložení nabídky je u této značky velmi jednoznačné. Skoro všechno jsou tenisky, a proto se dá celá nabídka procházet jedním pohledem. Menší kategorie slouží jen jako doplněk.</p>'
          + T(['Kategorie značky', 'Role v nabídce', 'Typické použití'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'naprostá většina modelů', 'město, škola, cestování, volný čas'],
              ['<a href="/badminton/">Badminton</a>', 'jednotky kusů', 'občasná hala, rekreační hra'],
              ['<a href="/treninkova-obuv/">Fitness a tréninková obuv</a>', 'jednotky kusů', 'lehký trénink'],
              ['<a href="/pantofle-a-zabky/">Pantofle a žabky</a>', 'jednotlivé kusy', 'doma, bazén, léto']]) +
          '<p>Značku proto vnímejte jako módní a každodenní obuv, nikoli jako specialistu na výkon. Kdo hledá boty na dlouhý běh nebo túru, najde lepší výběr v kategoriích <a href="/trailove-boty/">trailové boty</a> a <a href="/trekova-obuv/">trekové boty</a>, kde nabízejí více modelů například <a href="/znacka/salomon/">Salomon</a> nebo <a href="/znacka/cmp/">CMP</a>.</p>'
          '<h2>Pro koho jsou boty určené</h2>'
          '<p>Největší část nabídky tvoří dámské tenisky, o něco menší pánské a značné množství dětských. Dámské modely bývají užší a lehčí, pánské širší a výraznější, dětské často kopírují vzhled dospělých, ale mají dětský střih. Značka tedy dává smysl pro rodiny, které chtějí podobný vzhled obuvi pro celou domácnost. Barevně převažuje bílá, modrá, zelená a béžová, černá je spíš vzácnější, než by se čekalo.</p>'
          '<ul><li><strong>Ženy:</strong> nejširší výběr střihů, včetně semišových a nazouvacích modelů.</li>'
          '<li><strong>Muži:</strong> klasické šněrovací tenisky a modely označené jako univerzální obuv.</li>'
          '<li><strong>Děti:</strong> dětské verze oblíbených modelů v menších velikostech, často na šněrování.</li>'
          '<li><strong>Barvy:</strong> bílá se hodí k čemukoli, ale rychle se špiní, tmavé odstíny odpustí víc.</li></ul>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Názvy v katalogu se opakují s doplněním materiálu, typu nebo pohlaví. Pomáhá tomu řadit zboží: stejný model se může objevit jako dámský, pánský i dětský a v několika barvách. Tabulka shrnuje, co se z názvů dá odvodit.</p>'
          + T(['Označení', 'Co vyplývá z názvů v katalogu', 'Na co si dát pozor'], [
              ['Elan', 'dostupný jako Elan, Elan Trainer, Elan Leder, Elan Islington', 'liší se materiálem a podrážkou'],
              ['Tornado', 'nylonové šněrovací tenisky', 'lehčí, méně odolné vůči oděru'],
              ['Harrier', 'tenisky, dětská varianta Classics Harrier', 'ověřte střih a velikostní tabulku'],
              ['Daytona', 'varianta s označením Chute', 'různé provedení svršku'],
              ['Firefly, Bullet', 'dámské modely', 'porovnejte materiál a barvu'],
              ['Cleora Summit Mule', 'semišová nazouvací varianta', 'bez šněrování, pohodlná na doma i do města'],
              ['Made in England', 'v názvu u pánské univerzální obuvi', 'jde o část názvu produktu, ověřte popis obchodu']]) +
          '<p>Slova „Trainer“ nebo „Classics“ odkazují na styl tenisky, ne na výkon. Všechny tyto modely berte jako módní obuv se sportovním střihem.</p>'
          '<h2>Semiš, nylon a kůže: jak se liší</h2>'
          '<p>Materiál svršku rozhoduje o vzhledu, péči i počasí, ve kterém se bota nosí. Semišové tenisky mají měkký povrch a příjemný vzhled, ale bojí se vody a skvrn. Nylonové jsou lehké a rychle schnou, hůř však chrání před větrem a při dlouhé chůzi mohou víc prostoupit potem. Kožené snesou nejvíc a dají se čistit, jen potřebují pravidelnou péči a delší zaběhnutí.</p>'
          '<ul><li><strong>Semiš:</strong> impregnujte před první nošením a zbavujte skvrn speciální gumou nebo kartáčem.</li>'
          '<li><strong>Nylon:</strong> utřete vlhkým hadříkem, v pračce jen na šetrný program a v ochranném sáčku.</li>'
          '<li><strong>Kůže:</strong> otřete vlhkým hadříkem a občas ošetřete krémem.</li>'
          '<li><strong>Podrážka:</strong> gumová drží na mokrém i suchém, tenká plochá se na kluzkém povrchu rychleji smekne.</li></ul>'
          '<p>Pokud tenisky nosíte každý den, zvolte jednodušší materiál. Semišové se hodí spíš do suchého počasí a jako doplněk k oděvu na večer. Podobné rady najdete v průvodci kategorií <a href="/tenisky/">tenisky</a>, kde je i srovnání s dalšími značkami.</p>'
          '<h2>Retro tenisky a každodenní pohodlí</h2>'
          '<p>Retro tenisky mívají tenkou podešev a méně tlumení než moderní běžecká obuv. Při procházce po městě to nevadí, při celodenním stání nebo delší chůzi po tvrdém povrchu však vítáte pevnější vložku. Pokud vás bolí chodidla, zvažte výměnu originální vložky za anatomickou. Pro chůzi s batohem nebo delší výlet se hodí jiná kategorie, zatímco pro kancelář a město je retro bota stylová a nenápadná. Zaměřte se na pružnou špičku, měkký jazyk a kvalitní šněrování, které drží.</p>'
          '<p>Pro letní měsíce hledejte prodyšnější svršky a světlejší barvy. Na podzim se hodí tmavší semiš nebo kůže a výraznější podrážka. Do zimy raději zvolte zimní obuv ze sekce <a href="/zimni-obuv/">zimní boty a sněhule</a>, protože tenisky na sníh nejsou stavěné.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Velikostní tabulky se liší podle výrobce, takže vždy změřte délku chodidla v centimetrech a porovnejte s tabulkou v obchodě. Britské značky často používají britské číslování, které se od evropského liší, proto zkontrolujte, v jaké velikosti je produkt uveden. Tenisky s užším střihem mohou sedět hůř na široké noze; v takovém případě hledejte model s měkkým svrškem, který se přizpůsobí. U dětí nekupujte příliš velké boty, v těch se noha neudrží a hrozí otlaky. Dětský model vybírejte spíš s pevným zadním dílem a rychlým uzavíráním.</p>'
          '<ol><li>Změřte chodidlo večer, kdy je největší.</li>'
          '<li>Přičtěte asi centimetr na prostor před palcem.</li>'
          '<li>Porovnejte s tabulkou konkrétního obchodu.</li>'
          '<li>Vyzkoušejte doma na koberci, abyste mohli v případě potřeby vrátit.</li></ol>'
          '<h2>Čím se Gola liší od jiných značek tenisek</h2>'
          '<p>Zatímco značky jako <a href="/znacka/nike/">Nike</a> nebo <a href="/znacka/adidas/">Adidas</a> pokrývají celou škálu od běhu po fotbal, Gola se v katalogu soustředí na jediný typ obuvi. Díky tomu je nabídka přehlednější, ale chybí vám výkonové modely. Kdo chce tenisku hlavně do města, ocení pestrost barev a opakující se klasické tvary. Kdo potřebuje obuv na pravidelný sport, měl by vybrat specializovanou kategorii. Pomůže také porovnání s dalšími tenisky ve výběru <a href="/tenisky/">tenisky</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Tenisky nevolejte do pračky bez rozmyslu. Lepené spoje a lehké materiály nesnášejí vysokou teplotu a odstřeďování. Odstraňte tkaničky a vložky, očistěte kartáčem a vlhkým hadříkem, nechte uschnout při pokojové teplotě. Vložte do bot papír nebo noviny, aby udržely tvar a nasákly vlhkost. Při střídání dvou párů vydrží každý déle, protože materiál stihne vyschnout.</p>'
          '<h2>Jak tenisky kombinovat s oblečením</h2>'
          '<p>Bílá nebo béžová tenisky se hodí ke džínám, šortkám, lehkým šatům i kalhotám s užším střihem. Modré a zelené odstíny působí výrazněji a snesou jednoduché oblečení v neutrálních barvách. Semišové nazouvací modely ladí s mikinou a volnějšími kalhotami z kategorie <a href="/mikiny/">mikiny</a>, zatímco šněrovací nylonové se hodí ke sportovnějšímu stylu. Pokud chcete jedny boty na všechno, zvolte jednobarevné, bez velkého loga, a vyhněte se příliš zářivým barvám, které se rychle okoukají.</p>'
          '<p>Chcete-li si sestavit sportovnější obleček, podívejte se na <a href="/teplaky/">tepláky</a> nebo <a href="/leginy/">legíny</a>, které s tenisky vytvoří pohodlnou městskou kombinaci. Pro chladnější dny dobře poslouží <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>.</p>'
          '<h2>Pohodlí při celodenní chůzi</h2>'
          '<p>Plochá podrážka bez tlumení je lehká a stylová, ale při celodenním pobytu na tvrdém povrchu může unavit chodidla. Pokud trávíte den na nohou, ocení se měkčí vložka, širší špička a kvalitní ponožky. Ponožky vybírejte kratší, které se do nízké tenisky schovají, a z materiálu, který neklouže. Při prvních nošeních noste boty hodinu nebo dvě, aby se materiál přizpůsobil. Pokud tlačí, nepokračujte, protože otlaky ruší radost z nošení. Vložka se dá vyměnit za silnější, pokud pomáhá s oporou klenby.</p>'
          '<h2>Rodinný nákup a dětské velikosti</h2>'
          '<p>Značka nabízí podobné modely pro ženy, muže i děti, takže se hodí pro rodinný nákup. Dětská noha roste rychle, a proto kupujte malou rezervu, ale ne více než půl čísla navíc. Změřte dítěti nohu doma a porovnejte s tabulkou. Pokud dítě na prvním pokusu jde špatně nebo se zakopává, bota je pravděpodobně velká. Dětské tenisky snášejí hodně, proto kontrolujte pevné šití na špičce a vzorek podrážky, který neklouže po mokré dlažbě.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Módní tenisky zlevňují během sezónních výprodejů, na jaře a koncem léta, i při příchodu nové barevné kolekce. Protože se model opakuje v mnoha barvách, vyplatí se přijmout trochu méně oblíbenou barvu. Bílé modely bývají dražší, odstíny s menší poptávkou levnější. Porovnávejte více obchodů, sledujte celkovou cenu včetně dopravy a ověřte, jak funguje vrácení, protože u obuvi se často vrací kvůli velikosti.</p>',
    faq=[
        ('Co Gola v katalogu Sporteky nabízí?', 'Téměř výhradně tenisky a volnočasovou obuv pro ženy, muže a děti. Jen minimum je mimo tuto kategorii, například pár kousků pro badminton, trénink a pantofle.'),
        ('Je Gola vhodná na sport?', 'Spíš ne. Jde o módní každodenní obuv s retro vzhledem. Pro běh, túry nebo halové sporty je lepší vybírat ve specializovaných kategoriích s tlumením a oporou.'),
        ('Čím se liší modely Elan, Tornado nebo Harrier?', 'Jsou to různé tvary a materiály, například semišové, kožené nebo nylonové. Rozdíl poznáte z přívlastků v názvu a z popisu u obchodu, který uvádí svršek, podrážku a střih.'),
        ('Jak vybrat velikost tenisek?', 'Změřte chodidlo večer, přidejte přibližně centimetr a porovnejte s tabulkou obchodu. U britských značek ověřte, zda je číslo uvedeno v britské nebo evropské velikosti.'),
        ('Jak čistit semišové tenisky?', 'Pravidelně je kartáčujte suchým kartáčem, skvrny odstraňte semišovou gumou a před nošením impregnujte. Vodě se vyhněte, semiš po namočení tvrdne a mění barvu.'),
        ('Lze tenisky prát v pračce?', 'U nylonových a látkových někdy ano, na šetrný program a v sáčku, ale vždy zkontrolujte štítek. Semiš a kůži raději čistěte ručně, protože voda a odstřeďování poškozují materiál.'),
        ('Které barvy jsou nejčastější?', 'Nejvíc je bílých, modrých, zelených a béžových, doplňují je hnědé a růžové. Bílá se rychle špiní, tmavší odstíny odpouštějí víc a hodí se na každodenní nošení.'),
        ('Jsou v nabídce i dětské tenisky?', 'Ano, dětské verze populárních modelů tvoří znatelnou část. Při výběru dbejte na pevnou patu a snadné zapínání, a nekupujte o hodně větší velikost, noha v nich ztrácí oporu.'),
        ('Kdy bývají tenisky Gola ve slevě?', 'Nejčastěji při sezónních výprodejích a při příchodu nových barev. Celoročně bývají levnější méně žádané odstíny a poslední velikosti, takže se vyplatí porovnat obchody a nechat si čas.'),
    ])

# ------------------------------------------------------------------ husky
NEW['husky'] = dict(
    title='Husky: outdoorové oblečení, stany a spacáky ve srovnání',
    desc='Husky v katalogu Sporteky: outdoor kalhoty, bundy, spací pytle, stany, batohy a termoprádlo. Jak vybrat kus a kdy hledat slevy mezi obchody.',
    intro='<p>Husky je v katalogu Sporteky široká outdoorová značka: oblečení, spaní pod stanem i nošení výbavy. Největší část nabídky tvoří <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, hned za nimi <a href="/spaci-pytle/">spací pytle</a>, <a href="/stany/">stany</a>, kraťasy, trička a mikiny. Menší, ale důležitou skupinou jsou <a href="/turisticke-batohy/">turistické batohy</a>, ponožky, <a href="/termopradlo/">termoprádlo</a> a karimatky. '
          'Nabídka míří na ženy i muže téměř vyrovnaně a přidává unisex a dětské kousky. Stránka vysvětluje, jak se zorientovat v názvech Thermopro, Neoni, Nomi nebo Kippe, jak vybírat spacák podle teplotního údaje, jak velký stan potřebujete a jak vrstvit oblečení. Sporteka neprodává, jen porovnává obchody podle ceny, dostupnosti velikostí a vracení.</p>',
    guide='<h2>Co Husky v katalogu nabízí</h2>'
          '<p>Značka pokrývá celý outdoorový cyklus: co si obléknout, kde spát a co nést. To je u jediné značky ve srovnávači vzácné a hodí se pro ty, kdo chtějí vybavit celou výpravu stejnou řadou.</p>'
          + T(['Oblast', 'Kategorie značky', 'Typické použití'], [
              ['Kalhoty a kraťasy', '<a href="/sportovni-kalhoty/">sportovní kalhoty</a>, <a href="/sportovni-kratasy/">kraťasy</a>', 'túry, výlety, kempování, zima na lyžích'],
              ['Bundy', '<a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, <a href="/lyzarske-bundy/">lyžařské bundy</a>', 'vítr, déšť, chladnější dny'],
              ['Spaní', '<a href="/spaci-pytle/">spací pytle</a>, <a href="/stany/">stany</a>, <a href="/karimatky-a-matrace/">karimatky a matrace</a>', 'kemp, víkendová túra, výlet'],
              ['Nošení', '<a href="/turisticke-batohy/">turistické batohy</a>', 'jednodenní i vícedenní túry'],
              ['Spodní vrstvy', '<a href="/termopradlo/">termoprádlo</a>, <a href="/merino-pradlo/">merino prádlo</a>, <a href="/sportovni-ponozky/">ponožky</a>', 'zima, vrstvení, delší chůze'],
              ['Volný čas', '<a href="/sportovni-tricka/">trička</a>, <a href="/mikiny/">mikiny</a>', 'výlet, město, odpočinek']]) +
          '<p>Z přehledu je vidět, že oblečení je v počtu výrazně silnější než nocleh a nošení, ale právě stany a spacáky dělají z Husky komplexnější outdoorovou značku než čistě textilní. Pro srovnání s dalšími výrobci outdoorového oblečení se podívejte na <a href="/znacka/hannah/">Hannah</a>, <a href="/znacka/alpine-pro/">Alpine Pro</a>, <a href="/znacka/loap/">Loap</a> nebo <a href="/znacka/jack-wolfskin/">Jack Wolfskin</a>.</p>'
          '<h2>Jak číst názvy oblečení</h2>'
          '<p>Oblečení má v katalogu jednotný vzorec: značka, pohlaví, typ, jméno modelu, velikostní označení a barva. Jména modelů jako Nomi, Neoni, Kamela, Kilia, Kinel, Silvo nebo Grati jsou volně zvolená označení. Z názvu poznáte i materiál: „softshell“, „hardshell“ nebo „péřová“.</p>'
          + T(['Typ v názvu', 'Co to znamená', 'Kdy zvolit'], [
              ['Softshell bunda', 'pružný materiál odolný větru a lehkému dešti', 'aktivní pohyb, jaro a podzim'],
              ['Hardshell bunda', 'pevnější plášť proti dešti a větru', 'nepříznivé počasí, hory'],
              ['Outdoor bunda', 'univerzálnější vrchní vrstva', 'výlety, kempování'],
              ['Péřová vesta', 'izolace na trup bez rukávů', 'přidání vrstvy ve stanu, pauza'],
              ['Outdoor kalhoty', 'lehčí odolný materiál', 'túry po celý rok'],
              ['Lyžařské kalhoty a bundy', 'zateplené, odolné vůči sněhu', 'sjezdovka, zimní sporty']]) +
          '<p>Písmeno za jménem, například M nebo L, ukazuje velikost, nikoliv pohlaví. Pohlaví je uvedeno slovy „Pánské“ nebo „Dámské“. Před nákupem vždy prověřte velikostní tabulku konkrétní řady.</p>'
          '<h2>Spacák: jak číst teploty a zvolit typ</h2>'
          '<p>Spací pytle jsou v nabídce označeny jako letní, třísezónní a zimní, doplněné teplotním údajem v názvu, například −5, −10 nebo −20 °C. Takový údaj bývá uváděn jako hraniční nebo extrémní, ne jako teplota, při které bude spaní pohodlné. Zkontrolujte popis, zda výrobce uvádí komfortní, limitní a extrémní hodnotu, a vyberte spacák podle té komfortní. Pokud často mrzne, přidejte si rezervu, protože zima ve stanu bývá jiná než číslo na štítku.</p>'
          + T(['Typ', 'Pro jaké podmínky', 'Poznámka'], [
              ['Letní', 'teplé noci, kemp, chata', 'nejlehčí, snadno se vejde do batohu'],
              ['Třísezónní', 'jaro, léto, podzim', 'nejuniverzálnější volba'],
              ['Zimní', 'mrazy, horské noci', 'těžší, větší objem po zabalení'],
              ['Mumie', 'tvar těla, méně prostoru', 'teplejší na stejnou váhu'],
              ['Deka', 'více prostoru, rovný tvar', 'pohodlnější, ale chladnější']]) +
          '<p>Důležitou roli hraje izolace pod tělem. Spacák se pod vámi stlačí a přestává hřát, proto potřebujete kvalitní podložku. V kategorii <a href="/karimatky-a-matrace/">karimatky a matrace</a> vybírejte podle tepelného odporu, nikoli podle tloušťky. Zimní spaní na zmrzlé zemi bez izolace je téměř vždy chyba.</p>'
          '<h2>Stan: velikost, počet osob a použití</h2>'
          '<p>Označení „pro 2 osoby“ znamená, že se vejdou dva lidé těsně vedle sebe, bez místa na výbavu. Pokud chcete i zavazadla ve stanu, počítejte o osobu víc. U trekových stanů hraje roli váha a rozměr po složení, u kempových hlavně prostor a vstup. Kategorie <a href="/stany/">stany</a> a výběr <a href="/husky-stany/">stany Husky</a> vám umožní srovnat parametry mezi obchody. Důležitá je i vodní odolnost podlahy a přístřešku, kterou výrobce uvádí v milimetrech vodního sloupce; vyšší číslo znamená lepší ochranu, ale i těžší materiál.</p>'
          '<ul><li><strong>Předsíň:</strong> prostor pro boty a batohy, který zůstává pod střechou stanu.</li>'
          '<li><strong>Počet vchodů:</strong> dva vchody ulehčují vstup a ventilaci pro dva lidi.</li>'
          '<li><strong>Stavba:</strong> jednodušší kostra se staví rychleji, klíčové je mít stan vyzkoušený doma.</li>'
          '<li><strong>Zakotvení:</strong> kolíky a šňůry vždy kontrolujte, hodí se i náhradní.</li></ul>'
          '<h2>Batoh a nošení výbavy</h2>'
          '<p>Turistické batohy volte podle objemu a velikosti zad, nikoli podle vzhledu. Pro jednodenní výlet postačí dvacet až třicet litrů, pro víkend s nocováním výrazně víc. Nastavte nosný systém tak, aby váha spočívala na kyčlích, a vyzkoušejte batoh naložený. Podrobnější výběr nabízí kategorie <a href="/turisticke-batohy/">turistické batohy</a> a landing <a href="/batoh-husky/">batohy Husky</a>. Obecně platí, že těžké věci patří blízko zad a nahoru, lehké dolů a ven.</p>'
          '<h2>Vrstvení oblečení pro všechna roční období</h2>'
          '<p>Outdoorové oblečení funguje jako systém. Nejblíž k tělu patří spodní vrstva z <a href="/termopradlo/">termoprádla</a> nebo merina, nad ní fleece nebo mikina, navrch ochrana před větrem a deštěm. Ponožky vybírejte podle činnosti, ne podle barvy. Pokud plánujete delší túru, mějte s sebou rezervní suchou vrstvu v nepromokavém obalu. V létě stačí tričko a lehké kalhoty, přibalte však tenkou bundu, protože na hřebeni se počasí mění rychle. V zimě vrstvěte spíš více tenčích kusů než jeden těžký.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Outdoorové oblečení se obecně šije s větším volným prostorem než městské, protože se pod ním nosí další vrstvy. Pokud si chcete bundu navléci přes silnou mikinu, vezměte raději větší velikost. Kalhoty mají mít pružnější pas a zesílená kolena. Dámský střih bývá užší v pase a širší v bocích, pánský rovnější. U dětských kousků počítejte s růstem a vybírejte spíš prostornější střih, který vydrží celou sezonu. Pokud váháte mezi dvěma velikostmi, porovnejte obvod hrudníku a pasu v tabulce konkrétního obchodu.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li><strong>Membránové a softshellové kusy:</strong> perte šetrně, bez aviváže, a občas obnovte impregnaci.</li>'
          '<li><strong>Spacák:</strong> skladujte volně uložený ve velkém pytli, ne stlačený celoročně v sáčku.</li>'
          '<li><strong>Stan:</strong> po výletě důkladně vysušte, jinak vznikne plíseň.</li>'
          '<li><strong>Batoh:</strong> vyprázdněte kapsy, vyklepejte a vydrhněte vlhkým hadříkem.</li>'
          '<li><strong>Karimatky:</strong> zbavte písku a skladujte rozbalené, pokud je to možné.</li></ul>'
          '<p>Správně ošetřené kusy slouží řadu sezon, což vyvažuje vyšší pořizovací cenu. Pokud hledáte jemnější spodní vrstvu, prohlédněte si také značku <a href="/znacka/sensor/">Sensor</a> s merino prádlem.</p>'
          '<h2>Lyžařské a zimní oblečení</h2>'
          '<p>V nabídce se objevují i dámské lyžařské kalhoty a bundy, v několika barvách a velikostech. Zimní oblečení volte s ohledem na činnost: na sjezdovku zateplené s kapucí a sněhovým lemem, na běžky tenčí a prodyšnější. Kategorie <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a> a <a href="/lyzarske-bundy/">lyžařské bundy</a> ukazují srovnání dalších značek, mezi nimi i <a href="/znacka/cmp/">CMP</a>. Pod lyžařské oblečení patří termoprádlo a ponožky, které nestlačí lýtko. Dívejte se i na zimní nabídku <a href="/zimni-bundy/">zimních a péřových bund</a>.</p>'
          '<h2>Jak spolu spacák, karimatka a stan fungují</h2>'
          '<p>Při nocování venku platí, že teplo vzniká z kombinace tří věcí. Stan chrání před větrem a deštěm, karimatka izoluje od země a spacák zadržuje teplo těla. Pokud jeden z článků chybí nebo je slabší, celek selže. Proto nekupujte zimní spacák a tenkou karimatku, je to zbytečná investice. Naopak solidní karimatka a třísezónní spacák zvládnou víc, než se zdá. Navíc pomáhá jíst před spaním teplé jídlo, obléct suché spodní vrstvy a nechat si u hlavy čepici.</p>'
          + T(['Část výbavy', 'Hlavní úkol', 'Kde se šetřit nevyplatí'], [
              ['Stan', 'ochrana před deštěm a větrem', 'podlaha, švy, kvalita tyček'],
              ['Karimatka', 'izolace od země', 'tepelný odpor při chladu'],
              ['Spacák', 'zadržení tepla', 'komfortní teplota, ne jen hraniční'],
              ['Spodní vrstva', 'odvod potu, suchá kůže', 'materiál, který neudržuje vlhkost']]) +
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Outdoorové zboží je sezonní: spacáky, stany a letní oblečení zlevňují na podzim, zimní kousky na jaře. V průběhu roku se uvolňují starší barvy modelů, což se ve srovnávači pozná podle toho, že stejný produkt je v jedné barvě výrazně levnější. Pro velké nákupy, například stan a spacák společně, porovnejte celkové ceny i dopravu, protože stan je objemná zásilka. Sledujte, kdy zboží přijde zpět do skladu, a nenechte se zlákat ke koupi příliš malé velikosti jen kvůli akci.</p>',
    faq=[
        ('Co Husky v katalogu Sporteky nabízí?', 'Outdoorové oblečení, spací pytle, stany, karimatky, batohy, termoprádlo a ponožky. Nejvíc je kalhot a bund, ale značka pokrývá i spaní a nošení výbavy.'),
        ('Pro koho je zboží určené?', 'Pro ženy i muže téměř ve stejné míře, k tomu přibývají unisex modely a dětské kousky. Pohlaví poznáte z názvu produktu, velikost z písmen u jména modelu.'),
        ('Jak číst teplotu u spacáku?', 'Číslo v názvu, například −10 °C, bývá hraniční či extrémní údaj, ne pohodlná teplota. Hledejte v popisu komfortní hodnotu a při pochybnostech si přidejte rezervu.'),
        ('Který spacák je nejuniverzálnější?', 'Třísezónní. Pokryje jaro, léto i podzim, v chladnějším období doplníte vložkou nebo teplejšími vrstvami. Letní se hodí do kempu, zimní jen pokud opravdu mrzne.'),
        ('Jak velký stan koupit?', 'Počet osob v názvu znamená těsné spaní vedle sebe. Pokud chcete místo na výbavu nebo pohodlí, vyberte stan o osobu větší a zkontrolujte, zda má předsíň.'),
        ('Čím se liší softshell od hardshellu?', 'Softshell je pružnější a prodyšnější, odolá větru a lehkému dešti. Hardshell je pevnější a lépe chrání při silném dešti, bývá ale méně prodyšný. Volte podle počasí a činnosti.'),
        ('Jak vybrat velikost bundy nebo kalhot?', 'Porovnejte obvody v tabulce obchodu. Pokud pod bundu oblékáte silnou vrstvu, vezměte raději větší velikost. Kalhoty mají mít volnost v kolenou a pružný pas.'),
        ('Jak pečovat o spacák a stan?', 'Spacák skladujte volně, stan po výletě vysušte, aby nezplesnivěl. Oblečení perte šetrně, bez aviváže, a občas obnovte impregnaci, aby voda dál stékala.'),
        ('Kdy bývají slevy na outdoorové vybavení?', 'Letní vybavení zlevňuje na podzim, zimní na jaře. Celoročně se zlevňují starší barvy a poslední velikosti, takže stačí porovnat obchody a sledovat změny v nabídce.'),
    ])
