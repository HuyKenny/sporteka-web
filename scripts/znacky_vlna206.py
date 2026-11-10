"""sporteka.cz — brand texts wave 206: rockbros, tommy-hilfiger, columbia, victoria.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ rockbros
NEW['rockbros'] = dict(
    title='Rockbros: cyklistické oblečení, brašny, helmy a brýle',
    desc='Rockbros v katalogu Sporteky: cyklistické oblečení, brašny a nosiče, helmy, brýle, řídítka a pedály. Jak vybrat velikost a porovnat obchody.',
    intro='<p>Rockbros je v katalogu Sporteky značka, která pokrývá téměř celou výbavu cyklisty od hlavy až po pedály. Největší skupinu tvoří <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>, hned za ní následují <a href="/cyklo-tasky-a-nosice/">brašny, nosiče a košíky</a>, <a href="/sportovni-bryle/">sportovní a sluneční brýle</a> a <a href="/cyklisticke-helmy/">cyklistické helmy</a>. Najdete tu dresy, polstrované kraťasy, rukavice, boty, zámky i drobné díly na kolo. '
          'Zboží je z velké části unisex, dětské kousky tvoří znatelnou část a dámských i pánských modelů je méně. Převládá černá barva, což se hodí k jakémukoli kolu. Tato stránka vysvětluje, jak se v takové šíři orientovat: od čeho začít, co kupovat podle typu jízdy, jak vybrat velikost dresu a helmy a kdy se vyplatí sledovat nabídky obchodů. Sporteka nic neprodává, jen porovnává obchody a ukazuje, kde je právě vaše velikost skladem.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Rockbros funguje jako jednotný dodavatel doplňků pro kolo. Místo hledání dresu u jedné firmy, helmy u druhé a brašny u třetí můžete většinu výbavy najít pod jedním jménem. To usnadňuje sladění barev a velikostí, ale znamená to také, že každá kategorie má jiný charakter. Oblečení je spíš praktické než závodní, brašny cílí na každodenní a výletní použití a technické díly jako řídítka či pedály slouží jako dostupná náhrada. Přehled hlavních kategorií uvádí tabulka.</p>'
          + T(['Kategorie', 'Typický kousek v nabídce', 'Kdy se hodí'], [
              ['<a href="/cyklisticke-obleceni/">Cyklistické oblečení</a>', 'dres, triko na kolo, vesta, bunda, polstrované kraťasy', 'pravidelné vyjížďky, dojíždění, víkendové ježdění'],
              ['<a href="/cyklo-tasky-a-nosice/">Brašny, nosiče a košíky</a>', 'zadní nosič, brašna na rám a na nosič', 'dojíždění, cestování s nákladem'],
              ['<a href="/sportovni-bryle/">Sportovní a sluneční brýle</a>', 'brýle na kolo s měnitelnými skly', 'jízda za slunce, prach, hmyz'],
              ['<a href="/cyklisticke-helmy/">Cyklistické helmy</a>', 'silniční, horská a dětská přilba', 'každá jízda; děti zvlášť'],
              ['<a href="/cyklo-riditka/">Řídítka, představce a sedlovky</a>', 'řídítka, představec, sedlovka', 'úprava posedu, výměna dílu'],
              ['<a href="/cyklo-pedaly/">Pedály</a>', 'ploché pedály pro obyčejné boty', 'městské a horské kolo'],
              ['<a href="/cyklo-zamky/">Zámky na kolo</a>', 'zámek na kolo', 'parkování ve městě']]) +
          '<p>Kromě cyklistiky tu uvidíte i obecné sportovní textilie, například <a href="/teplaky/">tepláky</a>, <a href="/sportovni-vesty/">vesty</a>, <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/nakrcniky-a-satky/">nákrčníky a kukly</a>. Ty se hodí na kolo, ale stejně dobře poslouží při běhu nebo túře, takže se nemusíte omezovat jen na cyklistické kategorie.</p>'
          '<h2>Pro koho je zboží určeno</h2>'
          '<p>Filtr podle pohlaví ukazuje, že největší část nabídky nese označení unisex. U brýlí, helem, rukavic, zámků a dílů to dává smysl, protože na pohlaví tolik nezáleží. U oblečení si označení vždy přečtěte pozorně: pánský dres je střižený na širší ramena a delší trup, dámský je užší v pase a kratší. Dětská část je u značky neobvykle velká, což souvisí hlavně s helmami, rukavicemi a oblečením pro malé cyklisty. Mladí jezdci rychle rostou, takže se u dětí vyplatí volit levnější kousky a řešit hlavně správnou velikost přilby.</p>'
          '<h2>Cyklistické oblečení: dres, kraťasy a vrstvení</h2>'
          '<p>V cyklistickém oblečení se opakují prodyšná trička, dresy se zadními kapsami, vesty, dvouvrstvé bundy a polstrované kraťasy. Dres s kapsami na zádech unese telefon, klíče, energetickou tyčinku a pláštěnku, aniž byste je museli mít v batohu. Prodyšné triko na kolo funguje jako základní vrstva v teplých dnech. Při změně počasí pomáhá vesta, která chrání trup před větrem a nezahřívá paže.</p>'
          + T(['Kousek', 'K čemu slouží', 'Na co se zaměřit při výběru'], [
              ['Dres s krátkým rukávem', 'léto, delší výjezdy', 'zip, kapsy, délka zad a zadní díl delší než přední'],
              ['Dres s dlouhým rukávem', 'jaro a podzim', 'střih v zápěstí, zda přiléhá bez přílišného sevření'],
              ['Triko na kolo', 'dojíždění, krátké jízdy', 'prodyšnost, reflexní prvky, volnější střih'],
              ['Vesta', 'vítr a chladné ráno', 'skladnost, zda se vejde do kapsy dresu'],
              ['Dvouvrstvá bunda', 'chladné a mokré dny', 'větruvzdornost, rukávy, zip pod bradou'],
              ['Polstrované kraťasy', 'delší ježdění', 'tvar a tloušťka vložky, šev, šířka gumy na stehnech']]) +
          '<p>Polstrovaná vložka v kraťasech patří k nejdůležitějším částem oblečení. Nenosí se pod ní spodní prádlo, protože švy by třely a vložka by plnila svou funkci hůř. Při krátkých městských cestách stačí volnější model s odnímatelnou vložkou, na dlouhé trasy se vyplatí přiléhavý střih, který vložku udrží na místě. Kdybyste hledali další možnosti, projděte <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a> a <a href="/cyklisticke-dresy/">cyklistické dresy</a> od ostatních značek.</p>'
          '<h2>Helmy a brýle</h2>'
          '<p>Helma je jediný kus výbavy, u kterého nemá smysl šetřit na velikosti. Obvod hlavy změřte měkkým metrem nad obočím a hledejte rozsah, který tuto hodnotu pokrývá. Po nasazení musí helma sedět rovně, zakrývat čelo a zůstat na místě i při předklonu. Popruhy tvoří písmeno V pod ušima a pod bradou se dotahují tak, aby se vešel jeden prst. U dětí je důležitá možnost jemného nastavení a lehká konstrukce; v nabídce najdete i dětskou přilbu s odnímatelným chráničem brady, což je typ určený spíš pro náročnější terén. Další možnosti ukazují <a href="/silnicni-cyklohelmy/">silniční cyklohelmy</a>, <a href="/mestske-cyklohelmy/">městské cyklohelmy</a> a <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</p>'
          '<p>Sportovní brýle chrání oči před větrem, prachem a hmyzem. Pro jízdu za různého počasí se hodí sada s výměnnými skly: tmavé na slunce, čiré do šera a mlhy. Dioptrické oči se obejdou s klipem nebo s kontaktními čočkami. Sledujte také, aby rámeček nezasahoval do zorného pole v předklonu na silničním kole. Rozdíly mezi kategoriemi popisují stránky <a href="/cyklisticke-bryle/">cyklistické brýle</a> a <a href="/sportovni-bryle/">sportovní brýle</a>.</p>'
          '<h2>Brašny, nosiče a zámky</h2>'
          '<p>Brašny a nosiče tvoří druhou největší skupinu značky. Zadní hliníkový nosič se montuje na kola s očky pro upevnění a unese zátěž podle údaje výrobce. Tento údaj vždy ověřte v popisu produktu a nepřekračujte ho. U nosičů dbejte na průměr kol, protože nosič pro 26 palců nemusí sedět na jiné velikosti, a na vzdálenost úchytů. Některé modely mají policku nebo pružinu pro přichycení nákladu. Brašna na nosič se zavěšuje háky a zajišťuje se proti poskakování, brašna na rám slouží na drobnosti, které chcete mít po ruce.</p>'
          '<p>Zámek volte podle toho, kde kolo parkujete. Lanový nebo skládací zámek stačí na krátké zastavení u obchodu, v místech s vyšším rizikem se hodí robustnější typy. Pojistka je vždy pouze kompromis mezi váhou a odolností. Další přehled najdete v kategoriích <a href="/cyklo-zamky/">zámky na kolo</a> a <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>.</p>'
          '<h2>Boty a pedály</h2>'
          '<p>Ve vzorku zboží se často objevují boty na silniční cyklistiku a boty pro ploché pedály. Pro silnici jsou určené tuhé podrážky s uchycením kufru k pedálu, pro ploché pedály stačí podrážka s lepším záběrem a méně tuhou konstrukcí. U karbonových modelů počítejte s tuhou podrážkou, která dobře přenáší sílu, ale není příjemná při delší chůzi. Zkontrolujte, zda se bloky hodí k vašemu systému, protože systémy se liší. Pokud kupujete pedály zvlášť, najdete je v kategorii <a href="/cyklo-pedaly/">pedály</a>, obuv pak v <a href="/cyklisticka-obuv/">cyklistické obuvi</a>.</p>'
          '<h2>Jak zvolit velikost</h2>'
          '<p>Značka pochází z asijského výroby a rozměry se často řídí tabulkou uvedenou u konkrétního kusu. Označení M či L tedy nemusí odpovídat evropským zvyklostem a bývá menší než u evropských značek. Při výběru oblečení proto změřte obvod hrudníku, pasu a boků a porovnejte jej s tabulkou v popisu. Pokud se nacházíte mezi velikostmi, u dresu zvolte větší pro volnější jízdu a menší pro závodní přilnutí. U bot sledujte délku vložky v centimetrech, nikoli jen číslo.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Cyklistické textilie perte na doporučenou teplotu, bez aviváže a bez sušení v sušičce. Avivážní složky zalepují vlákna a zhoršují odvod potu. Polstrovanou vložku vypláchněte po každé jízdě, aby se v ní nedržela vlhkost. Brýle čistěte jen mikrovláknem a vodou, helmu nikdy neodkládejte na slunci za oknem auta. Po pádu nebo silném nárazu helmu vyměňte, i když vypadá celá, protože vnitřní pěna se mohla poškodit.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Cyklistické zboží se nejlevněji nakupuje mimo sezonu: dresy a bundy na podzim a v zimě, brýle a helmy po skončení hlavní sezony. Na jaře se naopak zdražuje a skladem nezůstávají populární velikosti. Pomocí Sporteky porovnejte více obchodů a zohledněte poštovné a lhůtu pro vrácení zboží, protože u oblečení se vám může stát, že velikost nesedí. Cenové grafy produktu ukazují vývoj nabídek a pomáhají poznat, zda je sleva skutečná. Na kvalitní doplňky se vyplatí počkat, základní kusy typu rukavic nebo nákrčníku se doplňují kdykoli.</p>'
          '<h2>Jak značku srovnat s ostatními</h2>'
          '<p>V nabídce Sporteky jde o značku, která spojuje široký sortiment s praktickým střihem. Pokud hledáte závodní oblečení s přesným střihem, podívejte se spíše na ' + B(('giro', 'Giro'), ('rogelli', 'Rogelli'), ('scott', 'Scott')) + '. Pro zámky a přilby se hodí ' + B(('abus', 'Abus')) + ', pro kola a díly ' + B(('cube', 'Cube'), ('shimano', 'Shimano')) + '. Rockbros je dobrá volba, když skládáte výbavu postupně a potřebujete drobnosti ke kolu bez složitého rozhodování.</p>',
    faq=[
        ('Co všechno od značky Rockbros najdu?', 'Největší část tvoří cyklistické oblečení, poté brašny a nosiče, brýle a helmy. Dále jsou v nabídce řídítka, pedály, zámky, rukavice, boty a obecné sportovní textilie jako tepláky či kraťasy.'),
        ('Jsou produkty Rockbros určené mužům nebo ženám?', 'Většina zboží je unisex, hlavně doplňky. Oblečení bývá označené jako pánské nebo dámské, výrazný podíl tvoří i dětské kousky, proto filtr pro koho používejte hned na začátku.'),
        ('Jak vybrat velikost cyklistického dresu?', 'Změřte obvod hrudníku, pasu a boků a porovnejte je s tabulkou u konkrétního produktu. Značky z Asie vycházejí menší, takže při pochybnostech zvolte větší číslo, zvlášť pro volnější jízdu.'),
        ('Musím pod polstrované kraťasy nosit spodní prádlo?', 'Ne. Cyklistické kraťasy s vložkou se nosí přímo na kůži, protože švy spodního prádla by třely. Po jízdě je hned vyperte a nechte uschnout.'),
        ('Jak správně nasadit cyklistickou helmu?', 'Helma sedí rovně, zakrývá čelo a nehýbe se do stran. Popruhy se uzavírají pod bradou tak, aby se pod ně vešel jeden prst, a tvoří písmeno V u uší.'),
        ('Kolik unese zadní nosič?', 'Nosnost uvádí výrobce v popisu produktu a nesmí se překračovat. Před koupí ověřte také, zda nosič sedí na vaši velikost kol a má potřebná očka pro montáž.'),
        ('Je lepší tmavá, nebo čirá skla brýlí?', 'Tmavá skla se hodí za jasného slunce, čirá a světlá do šera, lesa nebo deště. Sada s výměnnými skly pokryje různé podmínky a vyplatí se u pravidelných jezdců.'),
        ('Kdy nakupovat cyklistické oblečení výhodněji?', 'Mimo hlavní sezonu, tedy na podzim a v zimě. Nabídky obchodů porovnejte na Sporteka.cz včetně dopravy a podmínek vrácení a využijte historii nabídek u produktu.'),
        ('Jak pečovat o cyklistické textilie?', 'Perte šetrně při doporučené teplotě, bez aviváže a bez sušičky. Vložku v kraťasech vyplachujte po každé jízdě, aby se v ní nedržela vlhkost a zápach.'),
    ])

# ------------------------------------------------------------------ tommy-hilfiger
NEW['tommy-hilfiger'] = dict(
    title='Tommy Hilfiger: tenisky, trička, mikiny a plavky',
    desc='Tommy Hilfiger v katalogu Sporteky: tenisky, trička, mikiny, plavky, bundy a ponožky pro muže, ženy i děti. Jak vybrat střih a porovnat obchody.',
    intro='<p>Tommy Hilfiger je v katalogu Sporteky především značka volnočasové obuvi a každodenního oblečení se sportovním nádechem. Zdaleka nejpočetnější skupinu tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, za nimi následují <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/mikiny/">mikiny</a> a <a href="/sportovni-ponozky/">ponožky</a>. V nabídce jsou také plavky, košile, jarní bundy, sandály, kalhoty, čepice a polokošile. '
          'Prodává se pánům, ženám i dětem, přičemž dámských a pánských položek je podobně mnoho a dětská část je také velká. Převažují bílé, modré, černé a béžové odstíny. Tato stránka ukazuje, jak mezi tím vybírat: jak se liší nízké kožené tenisky od sportovnějších modelů, jak zvolit velikost, co sledovat u plavek a mikin a jak porovnat obchody. Sporteka nic neprodává, jen srovnává nabídky e-shopů a ukazuje, kde je vaše velikost skladem.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Značka Tommy Hilfiger se v nabídce nechová jako výrobce výkonnostního vybavení. Spíše jde o stylové oblečení a obuv pro každý den, které vypadá sportovně. Kdo hledá boty na maraton nebo funkční bundu do hor, najde lepší možnosti u jiných značek. Pro město, školu, kancelář s uvolněným dress codem, dovolenou a cestování je ale rozsah široký. Hlavní kategorie shrnuje tabulka.</p>'
          + T(['Kategorie', 'Typický kousek', 'Pro koho a kdy'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'nízké kožené tenisky, sportovní tenisky, dětské tenisky s pruhy', 'každodenní nošení, město, cestování'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'tričko s logem, tílko', 'léto, vrstvení pod mikinu'],
              ['<a href="/mikiny/">Mikiny</a>', 'mikina s kapucí i bez ní', 'podzim, jaro, chladné večery'],
              ['<a href="/plavky/">Plavky</a>', 'koupací kraťasy, plavky dámské i pánské', 'dovolená, bazén, pláž'],
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehká bunda přes mikinu', 'přechodné období'],
              ['<a href="/polokosile/">Polokošile</a>', 'klasická polokošile s límečkem', 'smart casual, léto'],
              ['<a href="/sportovni-ponozky/">Sportovní ponožky</a>', 'ponožky v setu', 'doplněk k teniskám']]) +
          '<p>Na okraji nabídky najdete i <a href="/kosile/">košile</a>, <a href="/sandaly/">sandály</a>, <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, <a href="/teplaky/">tepláky</a> a <a href="/cepice-a-celenky/">čepice a kšiltovky</a>. Pokud hledáte konkrétní typ, zkuste rovnou stránku <a href="/teplaky-tommy-hilfiger/">tepláky Tommy Hilfiger</a>.</p>'
          '<h2>Tenisky: jádro nabídky</h2>'
          '<p>Většinu tenisek Tommy Hilfiger tvoří nízké modely z hladké kůže nebo z kombinace kůže a textilu v bílé barvě, často s barevným pruhem na podrážce nebo na patě. Najdete tu pánské, dámské i dětské velikosti a názvy modelů obvykle obsahují označení jako Court nebo Runner, které naznačuje spíše tenisový či běžecký styl než skutečné určení. Tenisky slouží jako každodenní obuv, ne pro výkonnostní sport.</p>'
          '<p>Při výběru rozlišujte tři základní typy:</p>'
          '<ul><li><strong>Kožené nízké tenisky:</strong> elegantní vzhled, kombinace s kalhotami i džínami, vyžadují občasné otírání a impregnaci.</li>'
          '<li><strong>Textilní a kombinované modely:</strong> lehčí a prodyšnější, vhodné pro léto, zato hůře odolávají špíně.</li>'
          '<li><strong>Sportovnější modely s tlumením:</strong> podrážka bývá silnější a pohodlnější na delší chůzi.</li></ul>'
          '<p>Bílá obuv potřebuje péči. Po každém nošení otřete povrch vlhkým hadříkem a skvrny řešte hned. Kožené modely ošetřete krémem nebo sprejem na kůži, textilní vyčistěte kartáčem a jemným mýdlem. Do pračky se obuv s koženými díly nehodí. Více informací o kategorii poskytuje <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Značku znají zákazníci jako střihem spíše klasickou, než přiléhavou. Tričko bývá rovné, mikina běžně volnější, polokošile pravidelná. Pro přesné rozměry je ale vždy lepší použít tabulku konkrétního produktu. U obuvi se opakuje stejné pravidlo jako u většiny značek: změřte chodidlo večer, kdy je největší, a porovnejte s délkou vložky v centimetrech. Dětské velikosti si nechte s rezervou jednoho centimetru, aby dítě mělo místo na růst, ale bota nebyla příliš široká.</p>'
          + T(['Typ zboží', 'Jak velikost zvolit', 'Častá chyba'], [
              ['Tenisky', 'délka chodidla plus malá rezerva, ověřit šířku', 'koupě podle čísla bez změření'],
              ['Trička', 'podle obvodu hrudníku v tabulce', 'výběr příliš těsného střihu'],
              ['Mikiny', 'zvažte vrstvu pod mikinou', 'příliš malá velikost po vyprání'],
              ['Plavky', 'podle obvodu pasu a boků', 'ignorování podšívky a šňůrky'],
              ['Ponožky', 'rozsah čísel na obalu', 'koupě příliš těsného páru']]) +
          '<h2>Trička, mikiny a vrstvení</h2>'
          '<p>V kategoriích <a href="/sportovni-tricka/">trička a tílka</a> a <a href="/mikiny/">mikiny</a> převládají bavlněné nebo bavlněné směsné kousky s výrazným logem nebo s výšivkou. Jsou určené na běžné nošení a méně na intenzivní trénink. Pro posilovnu či běh se hodí funkční syntetika, která odvádí pot, zatímco bavlna zůstává mokrá. Pro cestování, školu a výlet po městě je bavlna příjemná a lépe snáší opakované praní. Mikinu s kapucí zvolte tam, kde potřebujete kapuci jako ochranu, hladkou bez kapuce na kombinaci s bundou.</p>'
          '<p>Pro přechodné období je tu <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bunda</a>. Bývá lehká, často s kapsami na zip a s úpletovým lemem. Neočekávejte však zimní zateplení. Do mrazu přidejte vrstvu pod bundu, nebo se podívejte na <a href="/zimni-bundy/">zimní bundy</a> jiných značek.</p>'
          '<h2>Plavky a letní oblečení</h2>'
          '<p>Plavky značky zahrnují koupací kraťasy pro muže i plavky pro ženy a děti. Pánské koupací kraťasy mají stahovací šňůrku a často vnitřní síťku. Pro plavání na bazéně je ale užitečnější přiléhavý střih, který neklade vodě odpor; k dovolené u moře se volné koupací kraťasy hodí. Plavky po koupání vypláchněte sladkou vodou, aby chlór a sůl nepoškodily vlákna, a sušte je ve stínu. Další varianty najdete v kategoriích <a href="/panske-plavky/">pánské plavky</a>, <a href="/damske-plavky/">dámské plavky</a> a <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h2>Pro koho je zboží určeno</h2>'
          '<p>Filtr podle pohlaví ukazuje na nejpočetnější pánskou nabídku, těsně za ní je dámská a dětská část je rovněž velká. Unisex položky jsou výjimkou, takže u většiny kousků volte podle označení. Dětské tenisky bývají zjednodušené modely s pruhy na boku a suchým zipem nebo se šněrováním. Pro školáky je praktické volit tmavší odstín, který snáší špínu.</p>'
          '<h2>Jak značku odlišit od konkurence</h2>'
          '<p>Na rozdíl od sportovních firem jako ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma')) + ' nenabízí Tommy Hilfiger techniku pro konkrétní sport. Je blíž značkám ' + B(('lacoste', 'Lacoste'), ('calvin-klein', 'Calvin Klein'), ('polo-ralph-lauren', 'Polo Ralph Lauren')) + ' tím, že spojuje preppy styl a sportovní prvky. Při výběru tedy rozhoduje vzhled a pohodlí na každý den, nikoli výkon.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Módní zboží se zlevňuje na konci sezony. Plavky a letní trička se objevují ve slevě koncem léta, mikiny a bundy v zimě a na jaře. Tenisky v bílé barvě patří k nejvíce hledaným a základní velikosti rychle mizí, proto při nabídce se slevou nečekejte dlouho. Využijte porovnání obchodů na Sporteka.cz, sledujte vývoj nabídek a ověřte, že jde o originální zboží s běžnou lhůtou pro vrácení. U módních značek se vyplatí zkontrolovat název modelu a číslo artiklu, aby šlo o stejný kus.</p>',
    faq=[
        ('Co od značky Tommy Hilfiger v katalogu najdu?', 'Převažují tenisky a volnočasové boty, dále trička, mikiny, ponožky, plavky, jarní bundy, košile a polokošile. Zboží je pro muže, ženy i děti.'),
        ('Jsou tenisky Tommy Hilfiger vhodné na sport?', 'Většinou jde o volnočasové boty pro každodenní nošení. Pro běh, fitness nebo hru zvolte obuv určenou přímo pro daný sport, například z kategorie běžecké boty.'),
        ('Jak čistit bílé kožené tenisky?', 'Povrch otřete vlhkým hadříkem hned po nošení, skvrny ošetřete jemným mýdlem a kůži občas natřete krémem. Do pračky tyto boty nedávejte.'),
        ('Jak zvolit velikost tenisek?', 'Změřte chodidlo večer a porovnejte délku s tabulkou u produktu. Pro děti nechte rezervu asi jeden centimetr, aby se botě neztrácel prostor na růst.'),
        ('Jsou mikiny Tommy Hilfiger vhodné na trénink?', 'Bavlněné mikiny jsou určené na běžné nošení. Na intenzivní cvičení se lépe hodí funkční materiály, které odvádějí pot a rychleji schnou.'),
        ('Jak se starat o plavky?', 'Po koupání je vypláchněte sladkou vodou, nemačkejte je a sušte ve stínu. Chlór a sůl vlákna časem poškozují, bez péče barvy blednou.'),
        ('Najdu u značky dětské oblečení a obuv?', 'Ano, dětská část je velká a obsahuje hlavně tenisky, trička, mikiny a plavky. Obuv volte s malou rezervou a v odolnějším odstínu.'),
        ('Kdy bývají slevy na módní sportovní oblečení?', 'Na konci sezony: letní zboží na konci léta, zimní zboží na jaře. Nejpopulárnější velikosti tenisek ale mizí rychle, proto nečekejte příliš dlouho.'),
        ('Jak poznám, že nabídka obchodu je výhodná?', 'Porovnejte celkovou cenu včetně dopravy a podmínek vrácení a sledujte historii nabídek u produktu. Ověřte stejný model a velikost.'),
    ])

# ------------------------------------------------------------------ columbia
NEW['columbia'] = dict(
    title='Columbia: outdoorové bundy, fleece, boty a oblečení',
    desc='Columbia v katalogu Sporteky: bundy, fleecové mikiny, trekové a trailové boty, zimní obuv a oblečení pro muže, ženy i děti. Jak vybrat a kdy hledat slevu.',
    intro='<p>Columbia je v katalogu Sporteky velká outdoorová značka, která pokrývá obuv i oblečení pro celý rok. Nejvíc zboží spadá do kategorie <a href="/tenisky/">tenisky a volnočasové boty</a>, hned za ní jsou <a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, <a href="/trekova-obuv/">trekové boty</a>, <a href="/trailove-boty/">trailové běžecké boty</a> a <a href="/zimni-bundy/">zimní a péřové bundy</a>. '
          'Značka cílí hlavně na muže, významný podíl ale mají ženy, dětská nabídka je menší. V barvách převládá černá, šedá, modrá a zelená s hnědými a béžovými přechody. Stránka vysvětluje, jak v tak široké nabídce vybrat: čím se liší trekové boty od trailových, kdy použít fleece a kdy bundu, jak číst názvy modelů a kdy se vyplatí sledovat slevy. Sporteka nic neprodává, jen porovnává e-shopy a ukazuje, kde je vaše velikost skladem.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Sortiment Columbia se dá rozdělit na tři části: obuv, vrchní vrstvy a základní oblečení. Obuv zahrnuje pohodlné volnočasové modely, trekové boty, trailové boty, zimní obuv a sandály. Vrchní vrstvy tvoří fleece, jarní a podzimní bundy, vesty, zimní a lyžařské bundy. Základ doplňují trička, kraťasy, kalhoty a čepice. Přehled hlavních kategorií je v tabulce.</p>'
          + T(['Kategorie', 'Typický kousek', 'Kdy se hodí'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'volnočasová obuv, zimní boty, nízké outdoorové modely', 'město, procházky, chladné dny'],
              ['<a href="/fleecove-mikiny/">Fleecové mikiny</a>', 'fleece se zipem, polovičním zipem nebo bez', 'střední vrstva na túru, chladný večer'],
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehká nepromokavá nebo větruodolná bunda', 'přechodné období, déšť'],
              ['<a href="/trekova-obuv/">Trekové boty</a>', 'kotníkové a nízké trekové boty', 'túry, nerovný terén'],
              ['<a href="/trailove-boty/">Trailové běžecké boty</a>', 'lehčí boty s dezénem', 'běh v lese, rychlé túry'],
              ['<a href="/zimni-bundy/">Zimní a péřové bundy</a>', 'zateplená bunda, lyžařská bunda', 'mráz, lyžování, zimní procházky'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'sandály s pásky', 'léto, voda, cestování']]) +
          '<p>Dále jsou v nabídce <a href="/mikiny/">mikiny</a>, <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/cepice-a-celenky/">čepice a kšiltovky</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>. Pro rychlý přechod k typu, který hledá hodně lidí, slouží <a href="/lyzarska-bunda-columbia/">lyžařská bunda Columbia</a>.</p>'
          '<h2>Pro koho je zboží určeno</h2>'
          '<p>Filtr podle pohlaví ukazuje, že největší část nabídky tvoří pánské kousky, dámská je o něco menší a dětská nabízí zejména zimní obuv a bundy. Unisex položek je málo. U obuvi používá značka často v názvu písmeno W pro dámskou verzi a slovo Youth nebo Dětská pro děti, takže při hledání pozorně čtěte název. Dámské střihy mají užší pas a kratší délku, u pánských je pohodlnější prostor v ramenou a hrudníku.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Názvy produktů Columbia obsahují řadu zkratek. Označení jako WP nebo Waterproof sdělují, že obuv či bunda má odolávat vodě. V názvech se objevuje OutDry, Insulated, Mid, Low a Fleece. Mid znamená vyšší střih pod kotník či nad něj, Insulated zateplený model. Nezapomeňte, že konkrétní vlastnosti a materiály vždy upřesňuje popis produktu v obchodě. Názvy slouží pro orientaci, nikoli jako záruka. Pokud popis chybí, nespoléhejte jen na zkratku a porovnejte více obchodů.</p>'
          + T(['Označení v názvu', 'Co obvykle naznačuje', 'Co ověřit v popisu'], [
              ['WP, Waterproof', 'ochrana proti vodě', 'zda jde o celý model, nebo jen o část'],
              ['Insulated', 'zateplení', 'typ výplně a vhodnou teplotu'],
              ['Mid', 'vyšší střih obuvi', 'výšku nad kotníkem a tuhost'],
              ['Fleece', 'měkká střední vrstva', 'tloušťku a zda má zip'],
              ['Youth', 'dětská řada', 'tabulku velikostí'],
              ['W nebo Dámská', 'dámský střih', 'číslo velikosti v tabulce']]) +
          '<h2>Trekové a trailové boty: čím se liší</h2>'
          '<p>Trekové boty mají tužší podrážku, pevnější špičku a často vyšší kotník. Hodí se na kamenité a nerovné cesty, delší túry a nošení batohu. Pro ty jsou určené stránky <a href="/trekova-obuv/">trekové boty</a>, <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> a <a href="/nizke-trekove-boty/">nízké trekové boty</a>. Trailové boty jsou lehčí, pružnější a mají agresivní dezén pro záběr na blátě a kořenech. Používají se pro běh i pro rychlé túry bez těžkého batohu. Ve vzorku zboží uvidíte kotníkové modely s membránou i trailové modely, které se hodí na rychlejší pohyb.</p>'
          '<p>Správná velikost obuvi vyžaduje rezervu před prsty, aby při sestupu nenarážely do špičky. Zkoušejte boty odpoledne v ponožkách, které na túře nosíte. Pro delší túry je výhodou víc prostoru, pro běh sedí lépe střih přiléhavější. Při výběru mezi nízkou a vysokou obuví zvažte terén: kotník podpoří vyšší bota, nízká dává větší svobodu pohybu na stezkách bez zátěže. Kdybyste váhali, porovnejte i <a href="/damske-trekove-boty/">dámské trekové boty</a> a <a href="/trekove-boty-panske/">pánské trekové boty</a>.</p>'
          '<h2>Fleece a bundy: vrstvení po celý rok</h2>'
          '<p>Fleecové mikiny tvoří druhou největší část nabídky a patří k typickému kusu značky. Fleece funguje jako střední vrstva: hřeje, i když zvlhne, a je lehký. Model s polovičním zipem se dobře vrství a zip lze rozepnout při námaze, plný zip se snáz nasazuje a umožňuje regulaci teploty. Fleecová mikina však nechrání proti větru a dešti, proto na ni patří vrchní bunda. Pro srovnání navštivte kategorii <a href="/funkcni-mikiny/">funkční mikiny</a>.</p>'
          '<p>Jarní a podzimní bundy v nabídce pokrývají lehčí nepromokavé varianty a větrovky. Pro zimu slouží zateplené bundy a lyžařské modely. Při volbě tloušťky myslete na teplotu, při které se budete pohybovat, a na vrstvení: tenčí bunda s fleecem pod ní se zvládne přizpůsobit víc podmínkám než jedna tlustá bunda. Při lyžování hledejte lyžařský střih s prodlouženými zády, sněhovým pásem a kapsou na skipas. Další varianty: <a href="/nepromokave-bundy/">nepromokavé bundy</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/lyzarske-bundy/">lyžařské bundy</a>.</p>'
          '<h2>Zimní obuv a sandály</h2>'
          '<p>V nabídce je velké množství zimní obuvi pro muže, ženy i děti, od lehkých zateplených bot po sněhule. Při volbě sledujte podrážku s hlubším dezénem pro jízdu na sněhu a ledu, zateplení a výšku svršku. U dětí se vyplatí boty, které se dobře obouvají, protože suchý zip nebo šněrování ušetří čas. V létě značka nabízí sportovní sandály s pásky, vhodné k vodě i cestování.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Nepromokavé oblečení perte podle štítku a bez aviváže. Jejich povrch časem ztrácí odpudivost vody a lze jej obnovit impregnací. Fleece se vypírá při nízké teplotě a nesuší se na topení. Obuv po túře očistěte kartáčem, vyjměte vložky a nechte ji uschnout při pokojové teplotě, ne u kamen. Kůži ošetřete vhodným přípravkem. Bundu skladujte uvolněnou, nestlačenou, aby se zachovala výplň.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Outdoorové zboží je nejlevnější mimo svou sezonu. Zimní bundy a obuv se zlevňují na jaře, fleece a sandály koncem léta. Kolekce se obměňují, takže starší modely často zlevní víc. Pomocí Sporteky porovnejte obchody včetně dopravy a lhůty pro vrácení, protože obuv potřebuje vyzkoušet. Historie nabídek u produktu ukáže, zda je sleva skutečná.</p>'
          '<h2>Jak značku srovnat s konkurencí</h2>'
          '<p>Columbia je pro mnoho lidí vstupní bod do outdooru. V rozsahu konkuruje značkám ' + B(('the-north-face', 'The North Face'), ('jack-wolfskin', 'Jack Wolfskin'), ('salomon', 'Salomon'), ('merrell', 'Merrell')) + '. Pokud hledáte levnější české alternativy, podívejte se na ' + B(('hannah', 'Hannah'), ('alpine-pro', 'Alpine Pro'), ('loap', 'Loap')) + '.</p>',
    faq=[
        ('Co od Columbia najdu v katalogu Sporteky?', 'Hlavně tenisky a volnočasovou obuv, fleecové mikiny, jarní a zimní bundy, trekové a trailové boty, sandály, trička, kraťasy a čepice.'),
        ('Pro koho jsou produkty Columbia určené?', 'Nejvíc je pánského zboží, dámská nabídka je také široká a dětská část je menší, hlavně zimní obuv a bundy. Unisex kousků je málo.'),
        ('Čím se liší trekové boty od trailových?', 'Trekové mají tužší podrážku a často vyšší kotník, hodí se na túry s batohem. Trailové jsou lehčí a pružnější, určené na běh nebo rychlou chůzi.'),
        ('Co znamená WP nebo Waterproof v názvu produktu?', 'Označení naznačuje ochranu před vodou, ale přesné vlastnosti a použité materiály vždy ověřte v popisu produktu u konkrétního obchodu.'),
        ('Je fleecová mikina dostatečně teplá na zimu?', 'Fleece hřeje jako střední vrstva, ale nechrání před větrem a deštěm. V mrazu k ní přidejte vrchní bundu a případně spodní vrstvu.'),
        ('Jak vybrat velikost trekové obuvi?', 'Zkoušejte odpoledne v ponožkách, které na túře nosíte, a nechte rezervu před prsty. Při sestupu pak noha nenarazí do špičky.'),
        ('Jak čistit a udržovat nepromokavou bundu?', 'Perte ji podle štítku bez aviváže a občas obnovte impregnaci. Skladujte ji volně, aby se výplň nestlačila.'),
        ('Najdu dětskou zimní obuv?', 'Ano, v nabídce jsou dětské zimní boty a bundy. Vybírejte boty s dobrým dezénem a snadným obouváním a při volbě velikosti nechte malou rezervu.'),
        ('Kdy nakoupit outdoorové oblečení výhodněji?', 'Mimo sezonu: zimní bundy a obuv na jaře, fleece a sandály koncem léta. Porovnejte obchody a sledujte historii nabídek u produktu.'),
    ])

# ------------------------------------------------------------------ victoria
NEW['victoria'] = dict(
    title='Victoria: barefoot a dětské tenisky, boty pro celý rok',
    desc='Victoria v katalogu Sporteky: dětské a dámské tenisky, barefoot boty a sandály. Jak vybrat velikost, kdy volit barefoot a porovnat obchody.',
    intro='<p>Victoria je v katalogu Sporteky obuvnická značka a skoro celý její sortiment tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>. Doplňují je <a href="/barefoot-obuv/">barefoot boty</a> a několik <a href="/sandaly/">sportovních sandálů</a>. Zboží míří hlavně na ženy a děti, pánský výběr je menší. '
          'V názvech modelů se opakují jména jako Oliver, Olmo, Kai, Bosco nebo Mary Jane a k nim barva: béžová, růžová, modrá, námořnická, bílá nebo hnědá. Tato stránka vysvětluje, jak v takové nabídce vybírat: čím se liší barefoot tenisky od běžných, jak změřit dětskou nohu, kdy zvolit plátěnou obuv a kdy kožený svršek, jak se o boty starat a jak porovnat obchody. Sporteka nic neprodává, jen ukazuje nabídky e-shopů a dostupné velikosti.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Victoria je v nabídce pozoruhodná tím, že se věnuje téměř výhradně obuvi, a to hlavně lehké každodenní. Nenajdete tu textil, bundy ani doplňky. Díky tomu se dají snadno porovnat modely mezi sebou. Většina zboží patří do kategorie tenisek, menší část tvoří barefoot a jen několik kusů jsou sandály. Přehled kategorií shrnuje tabulka.</p>'
          + T(['Kategorie', 'Typický kousek', 'Kdy se hodí'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'plátěné i kožené tenisky, celoroční boty, Mary Jane', 'škola, školka, město, volný čas'],
              ['<a href="/barefoot-obuv/">Barefoot boty</a>', 'tenisky s širokou špičkou a tenkou flexibilní podrážkou', 'děti i dospělí, kteří chtějí volný pohyb nohy'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'sandály s pásky', 'léto, dovolená']]) +
          '<p>Pokud hledáte rychlou cestu, použijte stránky <a href="/barefoot-boty-damske/">dámské barefoot boty</a> a <a href="/barefoot-boty-panske/">pánské barefoot boty</a>. Pro porovnání ostatních obuvnických kategorií navštivte i <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Pro koho je zboží určeno</h2>'
          '<p>Filtr podle pohlaví ukazuje, že největší část tvoří dámská obuv, těsně za ní následují dětské boty a pánských modelů je výrazně méně. Dětská nabídka je velká, protože k mnoha dámským modelům existuje menší sourozenec. U nákupu pro děti proto sledujte, zda je v názvu uvedeno slovo dětské nebo Youth. Dospělé velikosti nabízejí často stejné střihy, což umožňuje sladit boty pro rodiče i dítě. Rodiny to oceňují při cestování, protože si mohou vzít podobné pohodlné boty.</p>'
          '<h2>Barefoot tenisky: co je to a komu se hodí</h2>'
          '<p>Barefoot obuv je typ bot, který napodobuje pohyb naboso: má širokou špičku, v níž se prsty mohou roztáhnout, tenkou a ohebnou podrážku a bývá bez výrazného zvýšení paty. V názvech položek Victoria se slovo barefoot objevuje u dětských tenisek Oliver, Olmo, Kai a Bosco. Takové boty umožňují přirozený pohyb chodidla, nohy je však třeba postupně navyknout, zejména u dospělých.</p>'
          '<p>Před koupí zvažte několik věcí:</p>'
          '<ul><li><strong>Podrážka:</strong> tenká podrážka předává chodidlu víc vjemů z povrchu, ale méně tlumí a na ostrých kamíncích je citelná.</li>'
          '<li><strong>Šířka špičky:</strong> prsty musí mít prostor i při došlapu a nesmí se tlačit k sobě.</li>'
          '<li><strong>Pružnost:</strong> bota se musí dát ohnout rukou, jinak ji noha nepřirozeně vzdoruje.</li>'
          '<li><strong>Zapínání:</strong> suchý zip nebo šněrování, které drží patu na místě.</li>'
          '<li><strong>Postupné zvykání:</strong> začněte kratšími vycházkami a prodlužujte je podle toho, jak se vám noha přizpůsobuje.</li></ul>'
          '<p>Dětem se barefoot obuv často doporučuje, protože noha se vyvíjí, ale u zdravotních potíží, plochonoží nebo vbočených prstů se poraďte s lékařem nebo ortopedem. Žádná obuv nenahradí odborné vyšetření. Další informace jsou v kategorii <a href="/barefoot-obuv/">barefoot boty</a>.</p>'
          '<h2>Jak změřit dětskou nohu</h2>'
          '<p>Správná velikost je u dětí zásadní, protože noha roste rychle a špatná bota ji může tlačit. Postupujte takto:</p>'
          '<ol><li>Postavte dítě bez ponožek na papír a patu opřete o zeď.</li>'
          '<li>Tužkou označte nejdelší prst a změřte vzdálenost od zdi pravítkem.</li>'
          '<li>Stejný postup zopakujte na druhé noze a vezměte větší hodnotu.</li>'
          '<li>Přidejte rezervu zhruba půl až jeden centimetr, podle typu boty a doporučení obchodu.</li>'
          '<li>Výsledek porovnejte s tabulkou velikostí uvedenou u produktu.</li></ol>'
          '<p>Měření opakujte pravidelně, u menších dětí řádově po několika měsících. Po koupi zkontrolujte, zda dítě nemá červená místa po sundání bot. Dítě své problémy často nepoví, protože si na nepohodlí zvykne.</p>'
          '<h2>Materiály a barvy</h2>'
          '<p>Tenisky Victoria jsou plátěné, kožené i kombinované. Plátěné modely jsou lehké a dobře větrají, hodí se na teplejší dny, ale hůř snášejí déšť a rychle se zašpiní. Kožené svršky jsou odolnější a vydrží déle, vyžadují ale péči a při namočení je třeba je pomalu vysušit. Nejčastější barvy jsou bílá, hnědá, béžová a modrá. Bílou nosí rádi ti, kdo ji dokážou udržovat, tmavé a zemité odstíny lépe skryjí špínu a hodí se pro děti ve škole.</p>'
          + T(['Materiál', 'Výhoda', 'Nevýhoda'], [
              ['Plátno', 'lehké, prodyšné', 'špiní se, hůř odolává vodě'],
              ['Kůže', 'odolná, snese delší nošení', 'potřebuje péči a pomalé schnutí'],
              ['Kombinace', 'vyvážené pohodlí', 'záleží na kvalitě zpracování']]) +
          '<h2>Kdy zvolit celoroční boty a sandály</h2>'
          '<p>V nabídce se vyskytují i celoroční boty s vyšším střihem nebo s popruhem. Hodí se na podzim a jaro, kdy je potřeba chránit kotníky před chladem a vlhkem, ale ne zimní zateplení. V mrazu a sněhu potřebujete zimní obuv. Sportovní sandály pomohou v létě a při dovolené, kdy se nohy potí. Dětem však při dlouhé chůzi nebo hře na hřišti zajistí lepší ochranu prstů uzavřená tenisky. Podívejte se i na <a href="/zimni-obuv/">zimní obuv</a>, pokud potřebujete boty pro chladné období.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Boty po nošení vyvětrejte a nechte uschnout při pokojové teplotě, nikdy ne na radiátoru ani na slunci, protože lepené spoje se uvolňují. Vložky občas vyjměte. Plátno čistěte kartáčem a jemným mýdlem, kůži otřete vlhkým hadříkem a ošetřete krémem. Dětem se vyplatí mít dva páry na střídání, protože boty tak vydrží déle a stíhají vyschnout.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Letní plátěné modely zlevňují koncem léta, přechodné a celoroční boty na jaře i na podzim po skončení sezony. Dětské velikosti se ale rozprodávají rychle, takže u nejčastějších čísel nečekejte příliš dlouho. Při porovnávání obchodů na Sporteka.cz sledujte dopravu a možnost výměny velikosti, protože obuv bez vyzkoušení nemusí sednout. Pokud si nejste jistí číslem, vybírejte obchod s jednoduchou výměnou.</p>'
          '<h2>Jak značku srovnat s konkurencí</h2>'
          '<p>Pokud hledáte barefoot obuv od jiných firem, prohlédněte si nabídku v kategorii barefoot a dětské tenisky u značek ' + B(('skechers', 'Skechers'), ('geox', 'Geox'), ('crocs', 'Crocs')) + '. Victoria patří k těm, které se soustředí na lehkou každodenní obuv, nikoli na výkon, a proto se hodí hlavně pro školu, procházky a volný čas.</p>',
    faq=[
        ('Co od značky Victoria v katalogu Sporteky najdu?', 'Téměř výhradně obuv: tenisky a volnočasové boty, barefoot modely a několik sportovních sandálů. Textil ani doplňky tu nejsou.'),
        ('Je obuv Victoria vhodná pro děti?', 'Ano, dětská část je velká. Nabídka obsahuje barefoot tenisky i celoroční boty s různým zapínáním. Důležité je správné změření chodidla.'),
        ('Co je barefoot obuv?', 'Je to obuv s širokou špičkou, tenkou ohebnou podrážkou a malým zvýšením paty, která napodobuje chůzi naboso. Nohy je třeba pomalu navyknout.'),
        ('Jak změřit velikost nohy dítěte?', 'Postavte dítě na papír, označte nejdelší prst a změřte vzdálenost od paty. Přidejte rezervu zhruba půl až jeden centimetr a porovnejte s tabulkou velikostí.'),
        ('Jsou barefoot boty vhodné pro dospělé?', 'Ano, ale vyžadují postupné zvykání. Začněte kratšími vycházkami a při zdravotních potížích s nohama se poraďte s lékařem.'),
        ('Jaký materiál zvolit: plátno, nebo kůži?', 'Plátno je lehké a prodyšné, ale rychle se špiní. Kůže vydrží déle a vyžaduje péči. Podle použití a ročního období vyberte, co vám vyhovuje.'),
        ('Jak čistit bílé a světlé tenisky?', 'Plátno očistěte kartáčem s jemným mýdlem, kůži otřete vlhkým hadříkem a ošetřete krémem. Sušte při pokojové teplotě, ne na radiátoru.'),
        ('Hodí se tenisky Victoria do zimy?', 'Lehčí tenisky nejsou určené do mrazu a sněhu. Na zimu zvolte zateplenou zimní obuv, přechodné období zvládnou celoroční boty.'),
        ('Kdy nakoupit dětské boty výhodněji?', 'Koncem sezony, ale dětské velikosti se rozprodávají rychle. Porovnejte obchody včetně dopravy, vrácení a historie nabídek u produktu.'),
    ])

# ------------------------------------------------------------------ doplnky (vlozene za hlavni text)
NEW['tommy-hilfiger']['guide'] += (
    '<h2>Jak sestavit praktický outfit</h2>'
    '<p>Z nabídky se dá poskládat několik jednoduchých kombinací, které fungují bez složitého přemýšlení. Základem je bílé nebo tmavě modré tričko, k němu mikina přes ramena a nízké bílé tenisky. Na jaro přidejte lehkou bundu, na léto polokošili a koupací kraťasy v kufru. Značka pracuje s omezenou paletou, hlavně s bílou, modrou, červenou a béžovou, takže kusy spolu obvykle ladí a nemusíte řešit, zda se barvy nehádají.</p>'
    '<ul><li><strong>Do města:</strong> tenisky v bílé nebo tmavě modré barvě, rovné kalhoty a tričko s menším logem.</li>'
    '<li><strong>Na cesty:</strong> pohodlné tenisky, mikina na zip a ponožky, které se snadno perou.</li>'
    '<li><strong>K vodě:</strong> plavky, lehké tričko a sandály, které se rychle obují.</li>'
    '<li><strong>Do školy:</strong> odolnější tmavší tenisky a mikina, která snese časté praní.</li></ul>'
    '<h2>Originální zboží a srovnání nabídek</h2>'
    '<p>U módních značek se na internetu objevují padělky, proto kupujte jen u obchodů s jasnými podmínkami a kontakty. Zkontrolujte název modelu a číslo artiklu na štítku, porovnejte fotografie různých obchodů a nevěřte nabídce, která je výrazně pod ostatními. Sporteka ukazuje obchody vedle sebe, takže odchylka v nabídce je dobře vidět. Pokud si nejste jistí, použijte běžné platební metody s ochranou kupujícího a ponechte si doklad o koupi.</p>')
NEW['tommy-hilfiger']['faq'] += [
    ('Jak poznám, že koupím originální zboží?', 'Kupujte u obchodů s jasnými kontakty a podmínkami, porovnejte název modelu, číslo artiklu a fotografie a nevěřte nabídce výrazně pod ostatními.'),
    ('Jak se liší pánské a dámské tenisky?', 'Dámské modely bývají užší a lehčí, pánské širší. Ověřte tabulku velikostí u produktu, protože označení se může mezi řadami mírně lišit.'),
]
NEW['columbia']['guide'] += (
    '<h2>Jak sestavit vrstvy na túru</h2>'
    '<p>Při pohybu v horách funguje osvědčený třívrstvý systém. Spodní vrstva odvádí pot, střední hřeje a vrchní chrání před větrem a deštěm. Z nabídky Columbia se dá poskládat střední a vrchní vrstva: fleecová mikina pod nepromokavou bundu, k tomu trekové boty a čepice. Do batohu patří rezervní tričko a tenká vesta, kterou použijete při odpočinku. Při chůzi se nesmí zapomínat na odvětrávání, protože zpocený člověk rychle prochladne.</p>'
    '<ul><li><strong>Na krátký výlet:</strong> lehká bunda, tričko a nízké trekové boty nebo trailové boty.</li>'
    '<li><strong>Na celodenní túru:</strong> fleece, bunda do deště, kotníkové boty a čepice.</li>'
    '<li><strong>Na zimu:</strong> zateplená bunda, fleece pod ní a zimní obuv s dobrým dezénem.</li></ul>'
    '<h2>Velikosti a střihy</h2>'
    '<p>Značka má uvolněnější střih než závodní sportovní firmy a nechává prostor na vrstvení. Při koupi bundy počítejte s mikinou pod ní, při koupi fleecu zvažte, zda jej budete nosit jako střední vrstvu. Pro přesnou velikost si vždy otevřete tabulku u konkrétního produktu a porovnejte obvod hrudníku. Děti rostou, takže zimní bundu volte s malou rezervou, ale ne příliš velkou, aby neprofukovala.</p>')
NEW['columbia']['faq'] += [
    ('Jak si poskládat vrstvy na celodenní túru?', 'Základ tvoří tričko odvádějící pot, nad ním fleecová mikina a na vrchu nepromokavá bunda. Do batohu přidejte rezervní vrstvu a čepici.'),
]
NEW['victoria']['guide'] += (
    '<h2>Jak zvolit boty do školy a školky</h2>'
    '<p>Pro každodenní nošení v kolektivu je důležité, aby dítě bylo schopné boty obout samo. Suchý zip nebo pružné šněrování to usnadňují a ušetří ráno čas. Pevná špička chrání prsty při hře, flexibilní podrážka dovoluje přirozený krok. Do školy zvolte barvu, která skryje špínu, a nechte si náhradní pár na přezutí. Pamatujte, že dětská noha se v průběhu dne mírně zvětšuje, proto zkoušejte boty odpoledne.</p>'
    '<p>Doplňky pomáhají prodloužit životnost bot: kvalitní <a href="/sportovni-ponozky/">sportovní ponožky</a> brání otěru a pocení a <a href="/doplnky-k-obuvi/">doplňky k obuvi</a> jako vložky, impregnace či tkaničky vyřeší drobné potíže bez nákupu nového páru. Ponožky vybírejte bez tlačících švů a ze směsi, která odvádí vlhkost.</p>'
    '<h2>Velikosti a střihy</h2>'
    '<p>Značka je ve střihu spíše úzká až střední, což se projevuje hlavně u dospělých modelů. Barefoot varianty mají naopak širší špičku. Pokud váháte mezi dvěma čísly, rozhodujte podle délky vložky v centimetrech uvedené u produktu, a ne podle čísla. U dětí je rozumné zvolit větší číslo, pokud je noha tlustší, ale ne příliš velké, aby se bota nepřetáčela.</p>')
NEW['victoria']['faq'] += [
    ('Jak vybrat boty do školy?', 'Zvolte lehké tenisky se snadným zapínáním, pevnou špičkou a pružnou podrážkou. Tmavší barva skryje špínu a druhý pár se hodí na střídání.'),
    ('Jsou boty užší, nebo širší?', 'Běžné modely jsou spíš střední až užší, barefoot varianty mají širší špičku. Rozhodujte podle délky vložky uvedené u produktu.'),
]

NEW['tommy-hilfiger']['guide'] += (
    '<h2>Na co se zaměřit u dětských kusů</h2>'
    '<p>Dětská nabídka je u této značky pozoruhodně široká a obsahuje tenisky, trička, mikiny i plavky. Rodiče by měli nejdřív zvážit praktickou stránku: dítě bude kus oblečení nosit často, a proto má smysl hledat střih, který nesvazuje pohyb, a materiál, který vydrží opakované praní. Světlé tenisky se rychle špiní, tmavší varianty jsou praktičtější pro školu. U plavek pro děti zkontrolujte, zda gumy nezařezávají do kůže a zda podšívka nepuchýřkuje. Rostoucí dítě potřebuje novou velikost častěji, než by se zdálo, takže nákup do zásoby se nevyplácí.</p>'
    '<p>Rodinné nákupy usnadňuje to, že se podobné modely objevují v pánské, dámské i dětské verzi. Porovnáním více obchodů zjistíte, kde je skladem celá sada velikostí najednou, a ušetříte si doplňkové objednávky a dopravu.</p>')
NEW['columbia']['guide'] += (
    '<h2>Co sledovat u dětského zboží</h2>'
    '<p>Dětská část Columbia je menší než pánská a dámská, soustředí se na zimní obuv a bundy. U zimní obuvi pro děti dbejte na snadné obouvání a dobrý dezén, který neklouže na ledu. Bunda má mít kapuci nebo možnost přidat čepici a rukávy dostatečně dlouhé, aby dítě při hře nezmrzlo na zápěstích. Při koupi počítejte s tím, že děti se v zimní vrstvě pohybují hodně, a proto nesmí být oblečení příliš těžké.</p>')
NEW['victoria']['guide'] += (
    '<h2>Barefoot v běžném dni</h2>'
    '<p>Barefoot tenisky nejsou jen pro nadšence, ale také pro rodiny, které chtějí každodenní obuv bez výrazného zvýšení paty. Na procházku po městě, na hřiště, do školky nebo do školy se hodí stejně jako klasické tenisky. Počítejte jen s tím, že tenká podrážka méně tlumí nárazy na tvrdém povrchu, takže při delších trasách po dlažbě volte měkčí tempo. Pro sportovní hry s prudkými změnami směru je lepší pevnější sportovní obuv, například z kategorie <a href="/tenisova-obuv/">tenisová obuv</a> nebo jiné specializované sportovní obuvi.</p>'
    '<p>Při přechodu na barefoot začínejte postupně. První týdny nosíte boty jen na kratší vycházky, abyste dali svalům chodidla čas zesílit. U dětí je přechod snazší, protože jejich chůze není tolik ovlivněna zvyklostmi, přesto sledujte, zda si nestěžují na únavu nebo bolest. V takovém případě se vraťte k běžné obuvi a poraďte se s odborníkem.</p>')
