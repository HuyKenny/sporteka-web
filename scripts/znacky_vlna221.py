"""sporteka.cz — brand page texts wave 221: munich, insportline, kappa, alpina.
Facts only from the live catalogue (categories, audiences, product names); no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ munich
NEW['munich'] = dict(
    title='Munich: tenisky, kopačky, plavky a padelová obuv',
    desc='Munich ve sporteka.cz: převážně tenisky, k tomu plavky, kopačky, tenisová a padelová obuv. Jak vybrat model, velikost a kdy hledat slevy.',
    intro='<p>Sortiment značky Munich je v katalogu postavený na jedné silné kategorii: volnočasových teniskách. Tvoří drtivou většinu nabídky a zahrnuje jak jednoduché městské kousky, tak výraznější modely s vysokou podrážkou. Vedle nich najdete plavky, kopačky, obuv na tenis a padel, pár treků a lehké sandály. Značka tedy nepokrývá jeden sport, ale spíš způsob oblékání, kde se sportovní střih mísí s běžným nošením.</p>'
          '<p>Na této stránce porovnáváme nabídku Munich napříč obchody. Průvodce vysvětluje, jak se orientovat v číselných kódech modelů, jak vybrat tenisky pro muže, ženy a děti, proč se hodí zkoušet boty odpoledne a jak poznat, kdy je kopačka opravdu určená pro váš povrch. Najdete tu také praktické rady k péči o semišové a textilní svršky a k tomu, kdy se vyplatí sledovat slevy.</p>',
    guide='<h2>Co Munich v katalogu nabízí</h2>'
          '<p>Při prohlížení nabídky je zřejmé, že Munich je především obuvnická značka. Většina produktů spadá do kategorie <a href="/tenisky/">tenisky a volnočasové boty</a>. Druhou skupinu tvoří plavky, třetí kopačky, a pak následuje několik úzce zaměřených kategorií. Pro lepší představu slouží přehled.</p>'
          + T(['Skupina', 'Kategorie na sporteka.cz', 'Pro koho a k čemu'], [
              ['Hlavní sortiment', '<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'každodenní nošení, město, škola, cestování'],
              ['Voda', '<a href="/plavky/">Plavky</a> a <a href="/detske-plavky/">dětské plavky</a>', 'bazén, moře, dovolená'],
              ['Fotbal', '<a href="/kopacky/">Kopačky</a>', 'trénink a zápasy podle povrchu'],
              ['Raketové sporty', '<a href="/tenisova-obuv/">Tenisová obuv</a>, <a href="/padel/">padel</a>', 'kurty, lehké a stabilní boty'],
              ['Turistika', '<a href="/trekova-obuv/">Trekové boty</a>, sportovní sandály', 'výlety, lehčí terén, léto'],
              ['Doplňky a oblečení', '<a href="/mestske-batohy/">městské batohy</a>, kraťasy, trička', 'doplnění outfitu']]) +
          '<p>Z hlediska cílové skupiny převažují pánské modely, dámských je zhruba polovina a dětské tvoří samostatnou a dobře zastoupenou řadu. Unisex kousky jsou výjimkou, proto je při výběru nutné dívat se vždy na označení velikostí. Také barevná paleta je poměrně klidná: bílá, modrá a černá, k nim zelená, hnědá a šedá, a jen v menší míře výraznější odstíny.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Munich v obchodech často pojmenovává produkty kombinací slovního názvu a čísla, například Wave, Speed, Stilo, Next nebo Dash s číslem na konci. Jiné modely mají jen dlouhý číselný kód. Slovní název obvykle označuje řadu, tedy tvar podrážky a styl svršku, číslo pak často barevné provedení nebo konkrétní verzi. Jistotu ale dává jen popis konkrétního obchodu, proto neodhadujte shodu jen podle jména.</p>'
          '<ul><li><strong>Stejný model, jiná barva:</strong> v katalogu se jeden model objevuje v několika barvách a každá má vlastní kód. Při porovnávání obchodů proto hledejte přesně stejný kód a barvu.</li>'
          '<li><strong>Španělské popisy:</strong> u některých položek zůstaly v názvu slova jako Hombre nebo Azul, což znamená pánské a modré. Nejde o chybu, jen o neupravený popis dodavatele.</li>'
          '<li><strong>Verze Premium nebo Classic:</strong> označují zpravidla jiný materiál svršku nebo jinou úpravu, ne nutně jiný sport.</li>'
          '<li><strong>Dámské a pánské označení:</strong> hledejte slova Wmn, Man nebo Woman, ale ověřte i tabulku velikostí.</li></ul>'
          '<h2>Tenisky Munich: kdy jsou ta správná volba</h2>'
          '<p>Volnočasové tenisky této značky jsou určené na chůzi po městě, do školy, do práce v uvolněném prostředí a na cestování. Nejsou to běžecké boty, i když některé modely mají tlumicí podrážku. Pokud chcete běhat pravidelně, vyberte raději z kategorie <a href="/silnicni-bezecke-boty/">silničních běžeckých bot</a>. Pro každodenní použití je důležitý spíš pohodlný střih a pevná podrážka než technické prvky.</p>'
          '<p>Při výběru si ujasněte tři věci. Za prvé, jaký povrch budete nejčastěji šlapat: hladký chodník nebo dlažba snese plochou podrážku, na mokrém povrchu se však vyplatí hrubší vzorek. Za druhé, jak často je budete nosit. Když je obujete denně, hodí se tmavší barva, která skryje stopy. Za třetí, jaké oblečení k nim budete kombinovat. Bílá a béžová jsou univerzální k džínám a lněným kalhotám, modrá a zelená dodají outfitu barvu.</p>'
          + T(['Typ modelu', 'Charakter', 'Hodí se na'], [
              ['Nízká plochá podrážka', 'klidný vzhled, lehká', 'město, léto, dojíždění'],
              ['Vyšší podrážka s tvarem', 'výraznější silueta, stabilní stopa', 'dlouhé procházky, cestování'],
              ['Semišový nebo kožený svršek', 'reprezentativnější, vyžaduje péči', 'práce, večerní program'],
              ['Textilní svršek', 'prodyšný, lehčí', 'horké dny, volný čas'],
              ['Vysoký střih ke kotníku', 'víc opory, chladnější období', 'podzim, jaro']]) +
          '<p>Pro srovnání se podívejte i na modely z <a href="/znacka/nike/">Nike</a>, <a href="/znacka/adidas/">Adidas</a> nebo <a href="/znacka/puma/">Puma</a>. Ty jsou častěji založené na sportovním designu a technologiích výrobce. Munich v tomto srovnání působí jako obuv bližší módě, kde rozhoduje střih a kombinace barev.</p>'
          '<h2>Velikosti a střih</h2>'
          '<p>U jakékoli značky platí, že velikost je jen přibližné číslo. Nejspolehlivější je změřit chodidlo na konci dne, protože odpoledne bývá o něco větší. Postavte se bosá na papír, obkreslete nohu a změřte vzdálenost od paty k nejdelšímu prstu. K naměřené délce přičtěte asi centimetr, aby se prsty mohly při chůzi pohybovat. Pak porovnejte výsledek s velikostní tabulkou konkrétního obchodu.</p>'
          '<ul><li><strong>Evropské a španělské označení:</strong> španělské obchody používají stejné evropské číslování, rozdíly se objevují hlavně v šířce střihu.</li>'
          '<li><strong>Široké chodidlo:</strong> vyberte spíš textilní svršek, který povolí, než tuhou kůži.</li>'
          '<li><strong>Ponožky:</strong> zkoušejte s ponožkami, v nichž budete boty skutečně nosit.</li>'
          '<li><strong>Pravá a levá noha:</strong> pokud je jedna noha delší, řiďte se větší.</li></ul>'
          '<h2>Kopačky Munich</h2>'
          '<p>Značka nabízí také fotbalovou obuv. V kategorii <a href="/kopacky/">kopačky</a> je důležité dívat se na zkratky, které označují povrch. Obuv s vyměnitelnými nebo pevnými kolíky je určená pro trávu, kopačky s nízkými nopy a halová obuv s plochou podrážkou pro tvrdý povrch a sály. Špatná volba nejen zhoršuje souhru s míčem, ale zvyšuje riziko vyvrtnutí. Dětem vybírejte takovou kopačku, která nebude příliš těžká a s pevnou patou.</p>'
          '<p>Před nákupem zkontrolujte, zda se rozměry chodidla hodí k užšímu nebo širšímu střihu, a kopačky vždy zkoušejte s fotbalovými stulpnami. Pokud trénujete častěji než jednou týdně na různých površích, vyplatí se mít dva páry, protože střídání prodlužuje životnost a snižuje zátěž kloubů.</p>'
          '<h2>Plavky, tenis a padel</h2>'
          '<p>V kategorii <a href="/plavky/">plavky</a> se vedle pánských kousků objevují i dámské a samostatná řada <a href="/detske-plavky/">dětských plavek</a>. Pro bazén vybírejte pevnější materiál, který snese chlór, pro dovolenou stačí lehčí a rychleschnoucí střih. Zkontrolujte, zda je v pase vázání nebo guma a zda je vnitřní podšívka vhodná pro vás.</p>'
          '<p>U <a href="/tenisova-obuv/">tenisové obuvi</a> a obuvi na <a href="/padel/">padel</a> je rozhodující zpevněný střed a stabilní podrážka proti bočnímu klouzání. Padel se hraje na umělém povrchu a vyžaduje vzorek, který dobře drží při rychlých změnách směru. Pro běžný volnočasový tenis se hodí i lehčí model, pro pravidelné hraní pevnější. Nikdy nenoste kurtovou obuv na dlouhé procházky, podrážka se opotřebuje nerovnoměrně.</p>'
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p>Pánská řada je v katalogu nejširší a zahrnuje jak tradiční nízké tenisky, tak masivnější podrážky. Dámské modely bývají lehčí a častěji se objevují ve světlých a pastelových barvách, od bílé po růžovou a béžovou. Dětské boty mají obvykle pevnější špičku a snadné zapínání, což ocení rodiče při každodenním spěchu do školy. Při výběru pro školáka myslete také na to, že tělocvična vyžaduje čistou světlou podrážku, která nezanechává stopy.</p>'
          '<h2>Péče o obuv</h2>'
          '<ol><li>Po použití vyndejte vložky a nechte boty vyschnout při pokojové teplotě, nikoli na radiátoru.</li>'
          '<li>Semiš čistěte suchým kartáčkem a gumou, textil jemným kartáčem a vlažnou vodou s malým množstvím mýdla.</li>'
          '<li>Před prvním nošením použijte impregnační sprej odpovídající materiálu.</li>'
          '<li>Boty střídejte, ideálně každý den jiný pár.</li>'
          '<li>Při praní v pračce dodržujte údaj výrobce, mnohé modely praní nesnesou.</li></ol>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Volnočasové tenisky se přeceňují na konci sezóny a při obměně kolekce. Letní textilní modely bývají zlevněné na podzim, zimnější vyšší střihy na jaře. Pomůže sledovat jeden konkrétní model v několika obchodech a porovnat rozdíl po započtení dopravy. Velikosti ve středu řady se vyprodávají dříve než okrajové, proto počítejte s tím, že nejlepší nabídka se může týkat právě těch méně obvyklých čísel.</p>'
          '<p>Při srovnávání obchodů nesledujte jen cenu samotných bot, ale i podmínky vrácení. U obuvi, kterou nelze vyzkoušet, je možnost výměny velikosti důležitější než drobný rozdíl v ceně, protože doma zjistíte, zda střih vyhovuje chodidlu.</p>'
          '<p>Další rady k výběru najdete v kategoriích <a href="/trekova-obuv/">trekové boty</a> a <a href="/mestske-batohy/">městské batohy</a>, které ke značce také patří.</p>',
    faq=[
        ('Jaký sortiment má Munich ve sporteka.cz?', 'Převažují volnočasové tenisky, dále plavky, kopačky, tenisová a padelová obuv, několik trekových bot, sandálů a městských batohů. Pánské, dámské i dětské modely jsou zastoupeny.'),
        ('Jsou tenisky Munich vhodné na běhání?', 'Ne, jde o volnočasovou obuv určenou na chůzi. Pro pravidelný běh zvolte speciální běžecké boty, které mají jinak tlumenou a profilovanou podrážku.'),
        ('Jak poznám stejný model v různých obchodech?', 'Podle kódu nebo slovního názvu a barvy v popisu. Stejný model se prodává v několika barvách a každá má vlastní číslo, takže hledejte přesnou shodu.'),
        ('Proč jsou některé názvy ve španělštině?', 'Dodavatelé občas převezmou původní popis výrobce. Slova jako Hombre a Azul znamenají pánské a modré. Údaje o velikosti jsou přesto evropské.'),
        ('Jakou velikost zvolit, pokud váhám mezi dvěma?', 'Změřte chodidlo odpoledne a přidejte asi centimetr délky. Pokud máte široké chodidlo nebo nosíte silnější ponožky, zvolte větší číslo nebo měkčí textilní provedení.'),
        ('Jak vybrat kopačky podle povrchu?', 'Na trávu použijte kopačky s kolíky, na umělou trávu s nízkými nopy, do haly obuv s plochou podrážkou. Označení povrchu je v popisu produktu.'),
        ('Jak čistit semišové tenisky?', 'Použijte suchý kartáček a speciální gumu, skvrny nenamáčejte. Před nošením nanesete impregnaci pro semiš a boty sušíte mimo zdroj tepla.'),
        ('Dají se Munich tenisky použít na padel?', 'Kategorie padel má vlastní obuv se vzorkem vhodným pro umělý povrch. Běžné městské tenisky tuto stabilitu nemají, takže je na kurt nenoste.'),
        ('Kdy bývají tenisky nejlevnější?', 'Zpravidla na konci sezóny a při obměně kolekce. Letní modely na podzim, vyšší střihy na jaře. Sledujte vývoj nabídky u více obchodů a porovnejte i dopravu.'),
        ('Jsou dětské tenisky Munich nutné kupovat s rezervou?', 'Rezerva kolem jednoho centimetru stačí, větší boty dítě zpomalují a způsobují klopýtání. Velikost kontrolujte každé tři až čtyři měsíce, protože chodidlo roste rychle.'),
    ],
)

# ------------------------------------------------------------------ insportline
NEW['insportline'] = dict(
    title='Insportline: posilovací vybavení, trampolíny a pomůcky',
    desc='Insportline ve sporteka.cz: činky, posilovací lavice, rotopedy, hrazdy, trampolíny, pilates a masážní pomůcky. Jak vybrat vybavení domů a kam hledat slevy.',
    intro='<p>Insportline se v katalogu liší od většiny značek tím, že neprodává především oblečení nebo obuv, ale vybavení. Největší skupiny tvoří fitness pomůcky, činky a kotouče, masážní pomůcky a posilovací stroje s lavicemi. Dále sem patří rotopedy, hrazdy, trampolíny, pilates doplňky a překvapivě také lukostřelba, outdoorové doplňky či ortézy. Na jednom místě tak vidíte vybavení pro domácí posilovnu i drobnosti na cvičení.</p>'
          '<p>Značka nemá rozdělení podle pohlaví, protože vybavení se obvykle nevybírá podle něj. Důležitější je prostor, hmotnost uživatele, způsob použití a rozpočet. Průvodce níže vysvětluje, jak si naplánovat domácí posilovnu, co sledovat u činek, lavic a trenažérů, jak vybrat trampolínu a pilates pomůcky a kdy se vyplatí čekat na slevu. Žádné ceny ani počty neuvádíme, protože se mění týdně.</p>',
    guide='<h2>Co Insportline v katalogu nabízí</h2>'
          '<p>Nabídka je široká, ale dá se přehledně rozdělit do několika oblastí. Základ domácí posilovny tvoří <a href="/cinky-a-kotouce/">činky a kotouče</a> a <a href="/posilovaci-stroje/">posilovací stroje a lavice</a>. Pro kondici slouží <a href="/kardio-trenazery/">rotopedy a trenažéry</a>. Pro cvičení vlastní vahou jsou tu <a href="/hrazdy-a-bradla/">hrazdy a bradla</a> a řada <a href="/funkcni-trenink/">funkčního tréninku</a>.</p>'
          + T(['Oblast', 'Kategorie', 'K čemu slouží'], [
              ['Síla', '<a href="/cinky-a-kotouce/">Činky a kotouče</a>, <a href="/posilovaci-stroje/">stroje a lavice</a>', 'budování svalů, doma i v garáži'],
              ['Kondice', '<a href="/kardio-trenazery/">Rotopedy a trenažéry</a>', 'kardio bez ohledu na počasí'],
              ['Vlastní váha', '<a href="/hrazdy-a-bradla/">Hrazdy a bradla</a>, <a href="/funkcni-trenink/">funkční trénink</a>', 'shyby, dipy, cvičení s gumami'],
              ['Pohyblivost', '<a href="/pilates-pomucky/">Pilates pomůcky</a>, <a href="/fitness-pomucky/">fitness pomůcky</a>', 'jóga, protažení, rehabilitace'],
              ['Regenerace', '<a href="/masazni-pomucky/">Masážní pomůcky</a>, <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>', 'uvolnění svalů, podpora kloubů'],
              ['Zábava', '<a href="/trampoliny/">Trampolíny</a>, <a href="/lukostrelba/">lukostřelba</a>, <a href="/outdoor-doplnky/">outdoor</a>', 'zahrada, děti, volný čas']]) +
          '<p>Z barev dominuje černá, což u fitness vybavení odpovídá potahům, rámům a kovovým částem. Modrá, zelená, červená a růžová se objevují hlavně u malých pomůcek, jako jsou gumy, podložky nebo míče, a u dětských produktů.</p>'
          '<h2>Jak naplánovat domácí posilovnu</h2>'
          '<p>Nejčastější chybou je nákup stroje bez ohledu na prostor a zvyk cvičit. Před výběrem změřte místnost včetně výšky stropu, protože hrazda nebo činky při tlaku nad hlavu vyžadují rezervu. Také zvažte podlahu: těžké vybavení patří na pevný podklad s ochrannou podložkou, v bytě na patře ocení sousedé tlumení nárazů. Teprve poté vybírejte konkrétní kusy.</p>'
          '<ol><li><strong>Začněte základem:</strong> dvojice jednoručních činek nebo nastavitelná činka, podložka a gumy stačí na většinu cviků.</li>'
          '<li><strong>Přidejte lavici:</strong> pevná polohovatelná lavice rozšíří počet cviků víc než další drobné pomůcky.</li>'
          '<li><strong>Doplňte hrazdu:</strong> shyby a visy patří mezi nejúčinnější cviky pro záda a ramena.</li>'
          '<li><strong>Kardio až potom:</strong> rotoped nebo trenažér se vyplatí tomu, kdo ho skutečně použije, ne tomu, kdo ho koupil z dobrého úmyslu.</li>'
          '<li><strong>Regenerace a ochrana:</strong> válce, míčky a bandáže prodlouží dobu, po kterou můžete cvičit bez bolesti.</li></ol>'
          '<h2>Činky a kotouče</h2>'
          '<p>V kategorii <a href="/cinky-a-kotouce/">činky a kotouče</a> je důležité rozlišit průměr tyče a typ uchycení. Kotouče se na tyč nasazují podle průměru otvoru, takže je nelze zaměnit mezi systémy. Před nákupem tedy ověřte, zda se vám kotouče vejdou na tyč, kterou už máte, nebo zda kupujete celou sadu. U nastavitelných činek sledujte způsob zajištění závaží a rozsah hmotností, aby vám po půl roce přestaly stačit.</p>'
          '<p>Povrch činek má také význam. Gumový nebo potažený povrch chrání podlahu a hlučí méně, litinový je odolnější, ale na dlažbě dělá hluk i škody. Pro začátečníky se hodí menší skokové zvyšování zátěže, aby se postupně navyšovalo bez rizika přetížení.</p>'
          '<h2>Lavice a posilovací stroje</h2>'
          '<p>U kategorie <a href="/posilovaci-stroje/">posilovací stroje a lavice</a> rozhoduje stabilita. Pevný rám, širší nohy a polstrování, které nepropadá, jsou důležitější než počet funkcí. Polohovatelné opěradlo se hodí na tlaky šikmo i vsedě, ale každé další nastavení je místo, kde se může objevit vůle. Zkontrolujte nosnost uvedenou v popisu a počítejte s rezervou, protože pohyb s činkou zatěžuje lavici dynamicky.</p>'
          '<p>Víceúčelové stroje s kladkami šetří místo, ale vyžadují dostatečný prostor kolem. Neobejdete se bez návodu k sestavení a bez vhodného nářadí, plánujte proto na montáž dostatek času.</p>'
          '<h2>Rotopedy, trenažéry a hrazdy</h2>'
          '<p>Rotoped je klidnější varianta kardia pro ty, kdo nechtějí běhat venku. V kategorii <a href="/kardio-trenazery/">rotopedy a trenažéry</a> sledujte sedlo, nastavení výšky a plynulost chodu. Tichý a pevný stroj v bytě neruší sousedy ani domácnost. Zásadní je i zátěžový systém, který by měl umožňovat jemné doladění odporu.</p>'
          '<p>Hrazdy se dělí na dveřní, stropní a samostatné. <a href="/hrazdy-a-bradla/">Hrazdy a bradla</a> vyberte podle nosnosti a způsobu montáže. Dveřní model je nejlevnější na prostor, ale závisí na pevnosti zárubně, samostatná konstrukce potřebuje místo a stabilní podlahu. Před prvním shybem vždy zkontrolujte upevnění a odzkoušejte je pomalým zavěšením.</p>'
          '<h2>Pilates, masáž a bandáže</h2>'
          '<p>Z menších věcí se v nabídce objevují válce, míčky, masážní pomůcky a podložky. <a href="/pilates-pomucky/">Pilates pomůcky</a> vybírejte podle tloušťky a materiálu, aby se vám při cvičení neprohýbaly kolena a nesklouzávaly ruce. <a href="/masazni-pomucky/">Masážní pomůcky</a> jsou určené k uvolnění svalů po tréninku, ale při akutní bolesti nebo zranění se poraďte s lékařem či fyzioterapeutem.</p>'
          '<p>Kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> obsahuje podpůrné pomůcky pro klouby. Neslouží jako náhrada léčby, ale jako dočasná opora při zátěži. Správnou velikost zvolte podle obvodu příslušné části těla a postupujte podle tabulky výrobce.</p>'
          '<h2>Trampolíny, lukostřelba a oblečení</h2>'
          '<p>Trampolíny patří mezi největší položky. Zahradní model potřebuje rovný povrch, dostatečnou vzdálenost od stromů a plotů a ochrannou síť. Ověřte nosnost a velikost podle počtu dětí, které budou skákat zároveň. Lukostřelba v katalogu zahrnuje luky a terče, vhodné je používat je jen v místech, kde je bezpečný odstřel. Vedle toho značka nabízí také tepláky, mikiny, trička, šortky, ponožky či brusle, takže skladba je skutečně široká.</p>'
          '<p>U dětských produktů myslete na dohled dospělého a na věk, pro který je výrobek určený. Trampolínu je dobré zasadit do rovného terénu a pravidelně kontrolovat pružiny a spoje. Pokud přemýšlíte o vybavení pro celou rodinu, vyplatí se zvolit několik víceúčelových kousků místo mnoha jednoúčelových, které zabírají místo a rychle se omrzí.</p>'
          '<h2>Jak číst parametry v popisu</h2>'
          '<p>U vybavení nestačí věřit fotografii. V popisu hledejte nosnost, rozměry po složení i za provozu, hmotnost, materiál rámu a způsob montáže. Nosnost uvádí nejvyšší povolenou hmotnost uživatele nebo zátěže, ale reálně by neměla být využita naplno. Rozměry se vztahují často jen ke stroji, nikoli k prostoru potřebnému k cvičení, proto přidejte alespoň půl metru kolem. Pokud popis některý údaj nemá, požádejte obchod o doplnění, ještě než zboží objednáte.</p>'
          '<ul><li><strong>Nosnost:</strong> vybírejte s rezervou vůči vlastní hmotnosti a použité zátěži.</li>'
          '<li><strong>Rozměry:</strong> porovnejte s prostorem včetně výšky stropu a šířky dveří, kterými se bude vybavení nosit.</li>'
          '<li><strong>Hmotnost:</strong> těžší stroj bývá stabilnější, ale hůře se přemisťuje.</li>'
          '<li><strong>Kompletnost:</strong> ověřte, zda cena zahrnuje potah, závaží nebo madla, a co se musí dokoupit.</li>'
          '<li><strong>Záruka a servis:</strong> u pohyblivých dílů se vyplatí vědět, kdo opravuje a jak dlouho se čeká na náhradní díl.</li></ul>'
          '<h2>Bezpečnost a údržba</h2>'
          '<p>Domácí cvičení je bezpečné jen tehdy, když je vybavení v pořádku. Před každým tréninkem zběžně zkontrolujte šrouby, pojistky, kladky a lana. Činky ukládejte tak, aby se neskulily, a kotouče nevršte nad úroveň, kterou dosáhnete bez rizika pádu. U cviků s velkou zátěží nikdy necvičte bez pojistných dorazů nebo bez spolucvičence, který vám v případě selhání pomůže. Pohyblivé části občas promažte podle návodu a čistěte potahy mírně vlhkým hadříkem, nikoliv agresivními přípravky, které je vysušují.</p>'
          '<h2>Jak sestavit týdenní plán</h2>'
          '<p>Vybavení samo o sobě nic nezmění, rozhodují pravidelnost a plán. Začátečník vystačí se třemi tréninky týdně po čtyřiceti až šedesáti minutách. První rozdělte na cviky s činkami na horní polovinu těla, druhý na nohy a třetí na celé tělo nebo kondici. Mezi tréninky nechte aspoň jeden den volna na regeneraci. Pokud vás zajímá pilates nebo protažení, přidejte krátké sezení z kategorie <a href="/fitness-pomucky/">fitness pomůcky</a> po tréninku nebo večer. Po několika týdnech postupně zvyšujte zátěž, nikoli všechny parametry najednou.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Fitness vybavení se nejčastěji zlevňuje v lednu, kdy lidé plánují nové návyky, a na jaře před sezónou na zahradě. Trampolíny jsou nejlevnější na podzim, zimní vybavení na konci zimy. Nejlépe fungují porovnání dodacích podmínek a poplatků za dopravu, protože u objemných kusů mohou tvořit podstatnou část výdaje. Pokud potřebujete vybavení hned, zkontrolujte dostupnost skladem, termíny doručení se mezi obchody liší.</p>'
          '<p>Hledáte-li alternativy, podívejte se i na značky <a href="/znacka/nike/">Nike</a>, <a href="/znacka/adidas/">Adidas</a> a <a href="/znacka/puma/">Puma</a> u oblečení, nebo <a href="/znacka/head/">Head</a> a <a href="/znacka/reebok/">Reebok</a>.</p>',
    faq=[
        ('Co Insportline ve sporteka.cz nabízí?', 'Hlavně fitness vybavení: činky, kotouče, lavice, stroje, rotopedy, hrazdy, pilates a masážní pomůcky. K tomu trampolíny, lukostřelbu, outdoorové doplňky a část oblečení.'),
        ('Jak začít s domácí posilovnou?', 'Začněte jednoruční činkou nebo nastavitelnou sadou, podložkou a gumami. Teprve po několika týdnech přidejte lavici nebo hrazdu podle toho, co cvičíte nejčastěji.'),
        ('Jak zjistím, jestli kotouče pasují na tyč?', 'Porovnejte průměr otvoru kotouče a průměr tyče. Existují různé standardy a nejsou zaměnitelné, proto kupujte kotouče podle údaje v popisu.'),
        ('Je dveřní hrazda bezpečná?', 'Záleží na zárubni a nosnosti hrazdy. Před použitím ověřte upevnění, začněte pomalým zavěšením a nikdy nepřekračujte uvedenou nosnost.'),
        ('Jak vybrat rotoped do bytu?', 'Zaměřte se na tichý chod, stabilitu rámu, nastavitelné sedlo a plynulé zatěžování. Zvažte rozměry po složení a rozmístění ve vaší místnosti.'),
        ('Jakou velikost trampolíny zvolit?', 'Podle prostoru na zahradě a počtu dětí. Okolo trampolíny nechte volný prostor bez stromů, plotů a stěn a vždy použijte ochrannou síť.'),
        ('K čemu jsou masážní pomůcky?', 'K uvolnění svalů po tréninku a protažení tkání. Při akutní bolesti nebo po zranění se nejprve poraďte s lékařem či fyzioterapeutem.'),
        ('Nahradí ortéza léčbu?', 'Ne. Ortéza nebo bandáž poskytuje oporu při zátěži, ale nenahrazuje vyšetření a léčbu. Velikost volte podle obvodu příslušné části těla.'),
        ('Kdy se vyplatí čekat na slevu?', 'U fitness vybavení v lednu a na jaře, u trampolín na podzim. Porovnávejte celkovou cenu včetně dopravy, u objemných kusů je podstatná.'),
        ('Má Insportline pánské a dámské varianty?', 'Většina vybavení je univerzální. Pohlaví se řeší jen u části oblečení, kde se objevují pánské a dámské střihy a velikosti.'),
    ],
)

# ------------------------------------------------------------------ kappa
NEW['kappa'] = dict(
    title='Kappa: mikiny, tepláky, čepice a tenisky v nabídce',
    desc='Kappa ve sporteka.cz: tenisky, čepice, mikiny, trička, polokošile, tepláky a bundy pro muže, děti i ženy. Řady Kappa4Soccer a Kappa4Training, výběr a péče.',
    intro='<p>Kappa je v katalogu především značka sportovního stylu pro každý den. Největší skupinu tvoří tenisky, hned za nimi čepice a kšiltovky, mikiny, trička, polokošile, kraťasy a tepláky. Na rozdíl od specializovaných značek tu nenajdete jeden hlavní sport, ale ucelený šatník od hlavy po paty. Zajímavou součástí jsou i jarní a podzimní bundy, ponožky a několik kusů lyžařských a snowboardových kalhot.</p>'
          '<p>Vzorek zboží ukazuje, že názvy modelů se skládají z řady a jména, například Kappa4Soccer, Kappa4Training nebo Logo. Nabídka cílí hlavně na muže a děti, dámské i unisex kousky doplňují sortiment. Průvodce níže vysvětluje, jak se v řadách orientovat, jak vybrat mikinu, tepláky či bundu, jak poznat funkční oblečení od volnočasového a jak o oděvy pečovat. Najdete tu také tipy, kdy se vyplatí hledat zlevněné kousky.</p>',
    guide='<h2>Co Kappa v katalogu nabízí</h2>'
          '<p>Skladba kategorií ukazuje, že Kappa pokrývá především oblečení a doplňky, které se nosí ve volném čase i při lehkém sportu. Nejvíc zastoupená je obuv v kategorii <a href="/tenisky/">tenisky a volnočasové boty</a>. Následuje velká skupina <a href="/cepice-a-celenky/">čepic, kšiltovek a čelenek</a>, což je u jedné značky neobvyklé a hodí se pro doplnění outfitu. Pak přicházejí <a href="/mikiny/">mikiny</a>, <a href="/sportovni-tricka/">trička a tílka</a> a <a href="/polokosile/">polokošile</a>.</p>'
          + T(['Skupina', 'Kategorie', 'Typické použití'], [
              ['Obuv', '<a href="/tenisky/">Tenisky</a>', 'město, škola, volný čas'],
              ['Doplňky', '<a href="/cepice-a-celenky/">Čepice a kšiltovky</a>, <a href="/sportovni-ponozky/">ponožky</a>', 'každodenní outfit, ochrana hlavy'],
              ['Horní díly', '<a href="/mikiny/">Mikiny</a>, <a href="/sportovni-tricka/">trička</a>, <a href="/polokosile/">polokošile</a>', 'volný čas, fotbalový styl, trénink'],
              ['Spodní díly', '<a href="/teplaky/">Tepláky</a>, <a href="/sportovni-kalhoty/">kalhoty</a>, <a href="/sportovni-kratasy/">kraťasy</a>', 'domov, trénink, léto'],
              ['Bundy', '<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'přechodná období'],
              ['Funkce', '<a href="/funkcni-tricka/">Funkční trička</a>, <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>', 'sport, zima']]) +
          '<p>Z hlediska cílové skupiny jasně převažují pánské modely, hned za nimi jsou dětské, dámské tvoří menší část a unisex jen několik kusů. Pro ženy je tedy nabídka užší, ale u mikin a triček se často vyplatí sáhnout po unisex či pánském střihu o velikost menším. Barevně dominuje černá, doplněná bílou, modrou a šedou. Výraznější červená, vícebarevné kousky či zelená jsou spíš výjimkou.</p>'
          '<h2>Řady Kappa4Soccer, Kappa4Training a Logo</h2>'
          '<p>Při prohlížení nabídky narazíte na názvy začínající Kappa4Soccer nebo Kappa4Training. Podle názvu jde o oblečení inspirované fotbalem a o tréninkové řady. Označení Logo naznačuje, že hlavním motivem oděvu je výrazné logo značky na hrudi nebo rukávu. Jednotlivé modely mají jména, například Dacciozi, Gassolo, Bali nebo Giullio, a mohou se vyskytovat v několika barevných verzích. U každé z nich se dívejte na popis konkrétního obchodu, protože údaje o materiálu a střihu se mohou lišit.</p>'
          '<ul><li><strong>Volnočasová řada:</strong> mikiny a tepláky s logem, určené pro každodenní nošení a pohodlí.</li>'
          '<li><strong>Tréninková řada:</strong> lehčí kalhoty, šortky a trička, která je lepší použít při cvičení nebo hře.</li>'
          '<li><strong>Fotbalový styl:</strong> střihy, které připomínají týmové soupravy, vhodné na trénink i do města.</li>'
          '<li><strong>Dětské varianty:</strong> stejná jména modelů v menších velikostech umožňují sladit oblečení rodičů a dětí.</li></ul>'
          '<h2>Mikiny a tepláky</h2>'
          '<p>Mikina je nejčastěji hledaný kus značky. Vybírejte podle toho, zda ji chcete jako vrstvu pod bundu, nebo jako samostatný svrchní díl. Mikina s kapucí hřeje u krku a dobře vypadá k džínám, bez kapuce působí upraveněji. Zip do poloviny nebo celý zip usnadňuje oblékání, ale víc propouští vítr. Materiál s větším podílem bavlny je příjemný a savý, s přídavkem syntetických vláken rychleji schne a méně se mačká.</p>'
          '<p>Tepláky a <a href="/sportovni-kalhoty/">sportovní kalhoty</a> se liší střihem nohavic. Zúžené s manžetou drží tvar a hodí se k teniskám, rovné jsou volnější a lépe se kombinují s kecky. Pro trénink vybírejte kalhoty s lehčím materiálem a zipy na kapsách, aby věci nevypadávaly při pohybu. Šňůrka v pase je praktická, protože umožňuje doladit sedlost.</p>'
          '<h2>Trička, polokošile a funkční trička</h2>'
          '<p>Pro běžné nošení postačí bavlněné <a href="/sportovni-tricka/">tričko</a>. Při pohybu a pocení ocení člověk spíš <a href="/funkcni-tricka/">funkční triko</a>, které odvádí vlhkost od těla a rychleji schne. Poznáte je podle popisu syntetických vláken a lehčího, hladšího materiálu. Bavlna při větší námaze nasákne a ochlazuje, proto ji na delší sport nevolte. <a href="/polokosile/">Polokošile</a> poslouží jako elegantnější sportovní volba do práce, na golf nebo na turnaj.</p>'
          + T(['Potřeba', 'Zvolte', 'Pozor na'], [
              ['Každodenní pohodlí', 'bavlněné tričko nebo mikinu', 'srážení při praní'],
              ['Trénink a pot', 'funkční tričko, lehké šortky', 'příliš těsný střih'],
              ['Poloformální styl', 'polokošili', 'límec při sušení'],
              ['Chladné dny', 'mikinu s kapucí, tepláky', 'vítr bez větrné vrstvy'],
              ['Mezi sezónami', 'jarní nebo podzimní bundu', 'prodyšnost při chůzi']]) +
          '<h2>Bundy a zimní kousky</h2>'
          '<p>V kategorii <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> se objevují lehké vrstvy a prošívané modely. Prošívaná bunda hřeje díky vzduchové vrstvě, ale hůř prodýchává a není na delší pohyb. Pro dojíždění je dobrá volba, na pěší výlet raději lehčí a větruodolnou vrstvu. Pokud potřebujete skutečně zimní vybavení, najdete v nabídce i <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>. Při výběru kontrolujte zdvojení v koleni, manžety na kotnících a pásek pro regulaci.</p>'
          '<h2>Tenisky a čepice</h2>'
          '<p>Tenisky Kappa jsou určené do města a na volný čas. Nenahradí běžeckou ani halovou obuv, proto je nenoste na intenzivní trénink. Při výběru se řiďte pohodlným střihem a stabilní podrážkou. Dětem kupujte obuv s rezervou kolem jednoho centimetru a se zapínáním na suchý zip, pokud ještě nezvládají tkaničky.</p>'
          '<p>Čepice a kšiltovky jsou druhou největší skupinou. U kšiltovky zkontrolujte nastavitelný pásek vzadu, protože obvod hlavy se mezi lidmi liší. Zimní čepice vybírejte z hladkého materiálu bez škrábání a čelenky z elastického úpletu. Doplněk se stejným logem jako mikina vytvoří sladěný outfit.</p>'
          '<h2>Ponožky a drobnosti</h2>'
          '<p>V kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a> jsou balení několika párů, která vyřeší každodenní zásobu. Vybírejte podle délky: nízké k teniskám, střední k tréninku, vyšší do chladna. Příměs elastanu drží tvar, bavlna je příjemná, ale pomaleji schne. Ponožky střídejte a perte je s ostatním prádlem při stejné teplotě, aby se zbytečně nezmenšily. Drobné kousky jsou také dobrý dárek, protože u nich nehrozí chybná velikost.</p>'
          '<h2>Pánské, dětské a dámské oblečení</h2>'
          '<p>Pánská nabídka je nejširší a zahrnuje všechny hlavní kategorie, od obuvi přes mikiny a tepláky až po bundy. Dětské oblečení je druhou největší skupinou a pro rodiče je praktické, že stejné řady jsou k dispozici v menších velikostech. U dětí počítejte s růstem: mikiny a bundy kupujte o půl velikosti větší, ale ne tolik, aby rukávy zakrývaly dlaně. Dámský výběr je užší, takže ženy často sahají po unisex střihu nebo po dětských největších velikostech u menších kousků. Při takové volbě vždy porovnejte rozměry v tabulce.</p>'
          '<h2>Jak sladit outfit</h2>'
          '<p>Základem sportovního stylu je jednoduchost. Pokud zvolíte černou mikinu, doplňte ji bílými teniskami a tmavými teplákami, a čepice nebo kšiltovka dodá výraznou barvu. Modrou lze kombinovat s bílou a šedou, červenou se spíš nepřehánějte více než jedním kusem. Logo na hrudi je výrazné, takže ostatní kusy držte hladší. Pro chladné dny vrstvěte: funkční tričko, mikina a lehká bunda, každá vrstva se dá podle teploty sundat.</p>'
          '<h2>Velikosti a střih</h2>'
          '<p>Velikosti Kappa bývají standardní konfekční. U sportovního oblečení platí, že tělocvik nebo trénink vyžaduje volnější střih, zatímco do města může být oděv přiléhavější. Pokud váháte mezi dvěma velikostmi, zvolte větší u mikin a bund, které se nosí přes další vrstvu, a menší u triček s elastickou složkou. Porovnejte rozměry z tabulky obchodu s oblečením, které již máte, a přeměřte šířku v ramenou a délku rukávu.</p>'
          '<h2>Péče a životnost</h2>'
          '<ol><li>Mikiny a trička perte naruby, aby se nepoškodily potisky.</li>'
          '<li>Dodržujte teplotu uvedenou na štítku, obvykle třicet až čtyřicet stupňů.</li>'
          '<li>Nepoužívejte aviváž u funkčního prádla, zhoršuje odvod potu.</li>'
          '<li>Sušte na šňůře nebo v mírné sušičce, vysoká teplota zkracuje životnost vláken.</li>'
          '<li>Při žehlení potisků použijte žehličku z rubové strany.</li></ol>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Mikiny a bundy bývají nejlevnější na konci zimy, trička a kraťasy po létě. Čepice a ponožky se zlevňují během celého roku, protože jde o drobné kusy. Porovnávejte více obchodů, protože stejný model se může objevit v jiné barvě za jinou cenu. Hlídejte i dopravu a vrácení zboží: u oblečení se vyplatí možnost výměny velikosti.</p>'
          '<p>Pokud chcete porovnat styl s jinými značkami sportovní módy, podívejte se na <a href="/znacka/umbro/">Umbro</a>, <a href="/znacka/hummel/">Hummel</a>, <a href="/znacka/puma/">Puma</a> nebo <a href="/znacka/adidas/">Adidas</a>.</p>',
    faq=[
        ('Jaké zboží Kappa ve sporteka.cz nabízí?', 'Tenisky, čepice a kšiltovky, mikiny, trička, polokošile, kraťasy, tepláky, funkční trička, jarní a podzimní bundy, ponožky a lyžařské kalhoty. Převažují pánské a dětské modely.'),
        ('Co znamenají názvy Kappa4Soccer a Kappa4Training?', 'Jde o označení řad v názvech produktů. Soccer odkazuje na fotbalový styl, Training na tréninkové oblečení. Konkrétní materiál a střih zjistíte z popisu obchodu.'),
        ('Mají dámské modely dostatečný výběr?', 'Dámských kusů je méně než pánských. Unisex a pánské mikiny či trička proto zkuste o velikost menší, než byste volili normálně.'),
        ('Je Kappa vhodná na trénink?', 'Lehčí tréninkové kalhoty, šortky a funkční trička ano. Volnočasové mikiny s logem a tenisky jsou určené spíš na každodenní nošení.'),
        ('Jak vybrat velikost mikiny?', 'Porovnejte rozměry s oblečením, které vám sedí. Pokud ji budete nosit přes další vrstvu, zvolte větší, pro přiléhavý styl menší.'),
        ('Čím se liší funkční trička od bavlněných?', 'Funkční jsou ze syntetických vláken, odvádějí pot a rychleji schnou. Bavlna je příjemná na denní nošení, ale při námaze nasákne.'),
        ('Jak prát mikiny s potiskem?', 'Naruby při teplotě uvedené na štítku, bez aviváže a bez vysoké teploty v sušičce. Tak potisk vydrží déle a nepopraská.'),
        ('Jak zvolit kšiltovku správné velikosti?', 'Podívejte se na nastavitelný pásek vzadu a změřte obvod hlavy těsně nad obočím. Rozdíl mezi nastavitelným a pevným obvodem zjistíte v popisu.'),
        ('Najdu v nabídce lyžařské oblečení?', 'Ano, jsou tu lyžařské a snowboardové kalhoty. Zaměřte se na zdvojení v koleni, manžety a možnost regulace pasu.'),
        ('Kdy se vyplatí kupovat Kappa se slevou?', 'Zimní kousky na konci zimy, letní po létě. Drobnosti jako čepice nebo ponožky bývají zlevněné průběžně, proto porovnávejte obchody.'),
    ],
)

# ------------------------------------------------------------------ alpina
NEW['alpina'] = dict(
    title='Alpina: cyklistické a lyžařské helmy, brýle a boty',
    desc='Alpina ve sporteka.cz: cyklistické a lyžařské helmy, sportovní a lyžařské brýle, běžecké lyžování a boty. Jak vybrat velikost a kdy hlídat slevy.',
    intro='<p>Alpina je v katalogu značka ochranných pomůcek hlavy a očí. Dvě největší kategorie jsou cyklistické a lyžařské helmy, hned za nimi sportovní a sluneční brýle a lyžařské brýle. Vedle toho nabídka zahrnuje běžecké lyžování, silniční běžecké boty, lyžařské boty a hole, sjezdové lyže, chrániče, zimní obuv a drobnou skupinu příslušenství pro e-kola. Silný důraz na helmy a brýle je z katalogu jasně patrný a určuje, jak se v nabídce orientovat.</p>'
          '<p>Značka cílí na všechny věkové skupiny. Dětské modely tvoří významnou část, pánské a unisex jsou vyrovnané a dámské výběr doplňují. Průvodce níže vysvětluje, jak změřit hlavu, jak vybrat helmu pro kolo či lyže, na co se zaměřit u brýlí a jak se starat o ochranné vybavení. Najdete tu i rady k běžeckému lyžování a ke správnému načasování nákupu.</p>',
    guide='<h2>Co Alpina v katalogu nabízí</h2>'
          '<p>Skladba kategorií ukazuje čtyři hlavní proudy: ochrana hlavy, ochrana očí, běžecké lyžování a menší skupina obuvi s příslušenstvím. Největší část nabídky tvoří helmy a brýle, proto se jim věnuje většina průvodce.</p>'
          + T(['Oblast', 'Kategorie', 'Pro koho a k čemu'], [
              ['Helmy', '<a href="/cyklisticke-helmy/">Cyklistické helmy</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a>', 'děti i dospělí, kolo a lyže'],
              ['Brýle', '<a href="/sportovni-bryle/">Sportovní a sluneční brýle</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a>', 'ochrana očí před sluncem a větrem'],
              ['Lyžování', '<a href="/bezecke-lyzovani/">Běžecké lyžování</a>, <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyzarske-hole/">hole</a>', 'zimní sporty'],
              ['Obuv', '<a href="/lyzarske-boty/">Lyžařské boty</a>, <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, <a href="/zimni-obuv/">zimní obuv</a>', 'sezónní použití'],
              ['Ochrana a doplňky', '<a href="/chranice-a-helmy/">Chrániče a helmy</a>, <a href="/ebike-baterie/">e-kola</a>', 'bezpečnost a příslušenství']]) +
          '<p>Z hlediska barev jasně vede černá, následuje bílá, šedá a modrá. Zelená, růžová či oranžová se objevují hlavně u dětských modelů a u brýlí. Neutrální tmavé odstíny jsou praktické, protože nevypadají vedle různých dresů a bund nevhodně, výraznější barva je naopak lépe vidět v dopravě a na sjezdovce.</p>'
          '<h2>Jak vybrat cyklistickou helmu</h2>'
          '<p>Helma je jediná část výbavy, kterou se nevyplatí šetřit na nepohodlí: pokud tlačí nebo vrže, nasazujete ji neochotně. Základem je správná velikost podle obvodu hlavy. Změřte měkkým metrem obvod těsně nad obočím a uši a porovnejte s tabulkou v popisu. Helma má sedět pevně, ale bez bolestivého tlaku, nesmí se hýbat, když zakroutíte hlavou. Zapínací pásek se utahuje pod bradou tak, aby se pod ním vešel jen prst.</p>'
          '<ol><li>Postavte helmu rovně na čelo, přední okraj má být zhruba dva prsty nad obočím.</li>'
          '<li>Boční pásky tvoří písmeno V pod ušima, ne přes ně.</li>'
          '<li>Dotáhněte kolečko nebo systém na zátylku, aby helma nepadala dopředu.</li>'
          '<li>Pásek pod bradou dotáhněte tak, aby se při otevření úst mírně napnul.</li>'
          '<li>Po silném nárazu nebo pádu helmu vyměňte, i když nevidíte poškození.</li></ol>'
          '<p>V <a href="/cyklisticke-helmy/">cyklistických helmách</a> se liší určení: silniční, horské, městské a dětské. Silniční jsou lehké a prodyšné, horské mívají delší kšilt a hlubší zadní část, městské jsou praktické a často mají světlo nebo odnímatelný kryt. Dětské helmy se prodávají v menších velikostech s pohodlným zapínáním a jasnými barvami pro lepší viditelnost. Další tipy najdete také u srovnání s helmami z <a href="/znacka/giro/">Giro</a> nebo <a href="/znacka/bell/">Bell</a>, které nabízejí podobné kategorie.</p>'
          '<h2>Lyžařské helmy</h2>'
          '<p>V kategorii <a href="/lyzarske-helmy/">lyžařské helmy</a> je důležité, aby helma seděla i s čepicí nebo čelenkou, kterou pod ní nosíte, a aby se k ní hodily lyžařské brýle. Mezera mezi okrajem helmy a brýlemi má být co nejmenší, jinak vás bude táhnout na čelo. Větrání se často dá regulovat otvíráním průduchů. Pro děti vybírejte takovou helmu, která dosedne pevně, a raději ji kupujte na jednu sezónu s mírnou rezervou než o dvě velikosti větší.</p>'
          '<p>Používání helmy při lyžování a snowboardingu je rozumná prevence, a to u dětí i dospělých. Helma pomáhá chránit hlavu před nárazy a pády, ale nezaručí, že se nic nestane. Před sezónou zkontrolujte popruhy, upevnění a stav skořepiny.</p>'
          '<h2>Sportovní a sluneční brýle</h2>'
          '<p>Kategorie <a href="/sportovni-bryle/">sportovní a sluneční brýle</a> je třetí nejpočetnější. V názvech modelů uvidíte slova jako Rift, Bonfire, Sonic, Turbo, Ram nebo Swift a označení typu Q-LITE či HR. Slovní jméno určuje model, zkratky pak souvisejí s provedením skla nebo řadou. Přesný význam vždy najdete v popisu obchodu, nehádejte jej. Vedle sportovních modelů jsou zde také městské sluneční brýle s jednoduchým tvarem.</p>'
          '<ul><li><strong>Tvar rámu:</strong> sportovní brýle obepínají obličej a chrání proti větru a prachu, městské jsou užší a módnější.</li>'
          '<li><strong>Zorné pole:</strong> větší skla ochrání více, ale mohou na malé obličeje působit nepohodlně.</li>'
          '<li><strong>Sklo:</strong> zkontrolujte kategorii ochrany před sluncem a zda sklo odpovídá vašim potřebám, například řízení či jízdě na kole.</li>'
          '<li><strong>Nosní opěrky:</strong> pohodlné a protiskluzové opěrky zabraňují sklouzávání při potu.</li>'
          '<li><strong>Výměna skel:</strong> u některých modelů lze měnit skla podle světla, ověřte to v popisu.</li></ul>'
          '<h2>Lyžařské brýle</h2>'
          '<p>Nabídka <a href="/lyzarske-bryle/">lyžařských brýlí</a> je menší než u sluneční řady, ale pro sjezdovku nepostradatelná. Brýle musí těsnit v okolí obličeje, zároveň nesmí tlačit na nos a čelo. Zkontrolujte kompatibilitu s lyžařskou helmou, pásek a jeho nastavení. Při proměnlivém počasí se hodí brýle s výměnnými skly nebo skla určená pro různé podmínky. Před sezónou vyčistěte vnitřní stranu jen jemným hadříkem, protože antifog vrstva se snadno poškrábe.</p>'
          '<h2>Běžecké lyžování a boty</h2>'
          '<p>Kategorie <a href="/bezecke-lyzovani/">běžecké lyžování</a> zahrnuje výbavu pro klasický i bruslící styl. Rozdíl v nich je jasný: klasika používá stopu a vosk nebo šupinový skluz, brusle volnější povrch. Před koupí ověřte, jaké vázání a boty se k sobě hodí, protože systémy nejsou kompatibilní. Délku lyží a holí zvolte podle výšky a stylu, tabulku najdete u výrobce.</p>'
          '<p>Do nabídky patří také <a href="/lyzarske-boty/">lyžařské boty</a>, <a href="/lyzarske-hole/">hole</a>, <a href="/sjezdove-lyze/">sjezdové lyže</a> a <a href="/zimni-obuv/">zimní obuv</a>. U lyžařských bot rozhoduje délka chodidla v milimetrech a šířka, u hole délka podle výšky. <a href="/silnicni-bezecke-boty/">Silniční běžecké boty</a> jsou menší součástí nabídky, takže na běhání je lépe porovnat i specializované značky jako <a href="/znacka/asics/">Asics</a>.</p>'
          '<h2>Dětské helmy a brýle</h2>'
          '<p>Dětské modely tvoří výraznou část nabídky, což dává smysl: děti rostou rychle a ochranu hlavy potřebují při jízdě na kole, na koloběžce i na lyžích. Vybírejte pohodlné zapínání, které zvládne i dítě samo, a nastavitelný systém na zátylku, protože s dobou se hlava mění. Věnujte pozornost také viditelnosti: světlé a výrazné barvy zvyšují šanci, že dítě řidiči včas zaznamená. Před sezónou pokaždé helmu znovu změřte a zkontrolujte, zda stále sedí.</p>'
          '<p>Dětské lyžařské brýle musí dosednout na menší obličej bez mezer a sluneční brýle by měly mít vhodné sklo pro silné světlo. Nekupujte levné napodobeniny bez označení, protože sklo bez řádné ochrany může oči poškodit víc než jejich nenošení. Při pochybnostech se řiďte údaji obchodu o kategorii skla a radou odborníka.</p>'
          '<h2>Chrániče a příslušenství</h2>'
          '<p>Kategorie <a href="/chranice-a-helmy/">chrániče a helmy</a> doplňuje ochranu hlavy o další části. Při jízdě na kole nebo koloběžce se k helmě hodí chrániče kolen a loktů, hlavně u dětí. Nabídka obsahuje také drobnou skupinu pro <a href="/ebike-baterie/">e-kola</a>, tedy baterie, motory a nabíječky. U takového příslušenství vždy ověřte kompatibilitu s konkrétním kolem a výrobcem, protože různé systémy nejsou zaměnitelné.</p>'
          '<h2>Jak se připravit na sezónu</h2>'
          '<p>Před zimou projděte vybavení: helmu, brýle, boty, hole i lyže. Zkontrolujte popruhy, zapínání, čistotu skel a stav těsnění. U dětí vyzkoušejte, zda stále sedí velikost, protože za rok vyrostou. Podobně postupujte před cyklistickou sezónou. Nový nákup naplánujte s předstihem, ideálně o několik týdnů dřív, než vybavení opravdu potřebujete, aby zbyl čas na výměnu velikosti a nejlepší slevy.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Helmu uchovávejte mimo přímé slunce a horko, nenechávejte ji v rozpáleném autě.</li>'
          '<li>Čistěte ji vlažnou vodou a jemným mýdlem, rozpouštědla poškozují materiál.</li>'
          '<li>Brýle otírejte mikrovláknem po opláchnutí, suchou látkou by se sklo škrábalo.</li>'
          '<li>Skladujte brýle v pouzdře, ne v kapse s klíči.</li>'
          '<li>Po několika sezónách zkontrolujte popruhy a polstrování a pamatujte, že materiál stárne i bez nárazů.</li></ul>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Lyžařské helmy a brýle jsou nejlevnější na jaře a v létě, cyklistické naopak na podzim po sezóně. Sluneční brýle se zlevňují po létě. Různé barevné provedení stejného modelu mají často rozdílné ceny, proto porovnávejte všechny verze. Při nákupu helmy se řiďte hlavně velikostí a vrácením zboží, ne jen rozdílem v ceně.</p>',
    faq=[
        ('Co Alpina ve sporteka.cz nabízí?', 'Hlavně cyklistické a lyžařské helmy, sportovní a lyžařské brýle. K tomu běžecké lyžování, lyžařské boty a hole, sjezdové lyže, zimní obuv a menší doplňky.'),
        ('Jak změřit hlavu na helmu?', 'Měkkým metrem těsně nad obočím a ušima. Naměřený obvod porovnejte s tabulkou velikostí v popisu a vyberte helmu, která pevně sedí bez bolestivého tlaku.'),
        ('Kdy vyměnit helmu?', 'Po silném nárazu nebo pádu vždy, i bez viditelného poškození. Také ji vyměňte, když je poškozená skořepina, popruhy nebo polstrování.'),
        ('Mohu používat cyklistickou helmu na lyže?', 'Ne. Každý typ je navržen pro jiný druh nárazu a jinou ventilaci. Pro lyže použijte lyžařskou helmu a naopak.'),
        ('Co znamenají označení Q-LITE a HR u brýlí?', 'Jde o označení řady nebo provedení skla v názvu produktu. Přesný význam je v popisu u obchodu, takže jej bez ověření neodvozujte.'),
        ('Jak zkontrolovat kompatibilitu brýlí a helmy?', 'Nasaďte obojí společně a podívejte se, zda mezi helmou a rámem brýlí není velká mezera. Pásek brýlí musí sedět na helmě a nesmí klouzat.'),
        ('Jak čistit lyžařské brýle?', 'Opláchněte je vodou a osušte jemným hadříkem. Vnitřní stranu nedrhněte, jinak poškodíte protimlžnou vrstvu.'),
        ('Najdu v nabídce dětské helmy?', 'Ano, dětské modely tvoří významnou část sortimentu. Vybírejte podle obvodu hlavy a kontrolujte velikost každý rok, dítě roste rychle.'),
        ('Jak poznám správný styl běžeckého lyžování?', 'Klasický styl jde ve stopě, bruslení na hladké ploše. Vázání a boty musí odpovídat stejnému systému, ověřte to před nákupem.'),
        ('Kdy bývají helmy a brýle nejlevnější?', 'Lyžařské na jaře a v létě, cyklistické po sezóně na podzim, sluneční brýle po létě. Porovnávejte barevné verze i dopravu.'),
    ],
)
