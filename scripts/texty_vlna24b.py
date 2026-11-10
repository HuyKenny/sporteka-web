"""sporteka.cz — wave 24b (5. 11. 2026): long texts for detske-lyze, jezdecke-obleceni, snowboardova-vazani, predtreninkove-boostery.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detske-lyze
NEW['detske-lyze'] = dict(long=True,
    title='Dětské lyže: délka, komplety s vázáním, výběr',
    desc='Dětské sjezdové lyže i komplety s vázáním. Jak zvolit délku podle výšky, tvar, tuhost, seřízení vázání a péči a porovnat nabídky českých obchodů.',
    intro='<p>První lyže určují, jestli dítě na svahu zůstane nadšené, nebo bude po týdnu vzdychat u svačiny. Dětské modely jsou kratší, lehčí a měkčí než dospělé, mají jednodušší hrany a často přicházejí rovnou s vázáním, které se dá nastavit podle velikosti boty. Sporteka porovnává nabídky českých obchodů u malých plastových lyží pro nejmenší, juniorských sjezdovek, závodních modelů i příslušenství, jako jsou vaky na lyže.</p>'
          '<p>V kategorii najdete značky ' + B(('rossignol', 'Rossignol'), ('fischer', 'Fischer'), ('blizzard', 'Blizzard'), ('atomic', 'Atomic'), ('head', 'Head'), ('elan', 'Elan'), ('sulov', 'Sulov'), ('wedze', 'Wedze')) +
          '. K lyžím patří <a href="/lyzarske-boty/">lyžařské boty</a>, <a href="/lyzarske-helmy/">helma</a>, <a href="/lyzarske-bryle/">brýle</a> a <a href="/lyzarske-hole/">hole</a>, dospělí si vyberou ve <a href="/sjezdove-lyze/">sjezdových lyžích</a>.</p>',
    guide='<h2>Jaké dětské lyže se v nabídce objevují</h2>'
          '<p>Pod pojmem dětské lyže se skrývá několik odlišných věcí. Nejmenší dítě na prvním kroku potřebuje něco jiného než školák, který už zvládá modré a červené sjezdovky, a mladý závodník zase sáhne po modelu s pevnějším jádrem. Při procházení nabídky si proto nejdřív ujasněte, do které skupiny vaše dítě patří.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Plastové lyže pro nejmenší', 'velmi krátké, jednoduché pásky nebo univerzální úchyt na botu', 'první krůčky na sněhu v zahradě nebo na kopečku'],
              ['Komplet lyže s vázáním', 'lyže už mají namontované vázání, často nastavitelné podle bot', 'rekreační lyžování a první sezóny'],
              ['Juniorské lyže bez vázání', 'vázání se vybírá zvlášť', 'zkušenější děti a kluby'],
              ['Dívčí a chlapecké řady', 'rozdíl hlavně v grafice a občas v tuhosti', 'běžné rodinné lyžování'],
              ['Závodní juniorky', 'užší, tužší, s ostřejšími hranami', 'oddíly a děti, které zrychlují'],
              ['Lyže s licenčními motivy', 'lehká konstrukce a postavičky z oblíbených seriálů', 'nejmenší děti, pro které je hlavní radost z lyží']]) +
          '<p>Kromě samotných lyží kategorie obsahuje i drobnosti, třeba úložné vaky na lyže pro děti. Pokud je potřebujete, zkontrolujte, pro jakou délku lyží jsou vak i hole určeny.</p>'
          '<h2>Délka lyží podle výšky a zkušeností</h2>'
          '<p>U dětí platí jednoduché pravidlo: délka vychází z výšky, váhy a umu. Nejkratší lyže, zhruba po hrudník, se otáčejí snadno a odpouštějí chyby. Pokročilejší jezdec může sáhnout po lyžích po bradu až po nos, protože ocení stabilitu při rychlosti. Nekupujte lyže „na vyrůstání“, protože příliš dlouhé lyže se špatně otáčejí a dítě na nich bojuje místo aby se učilo.</p>'
          + T(['Výška dítěte', 'Orientační délka lyží', 'Poznámka'], [
              ['do 100 cm', '70–90 cm', 'nejmenší děti, často i kratší plastové modely'],
              ['100–120 cm', '90–110 cm', 'první sjezdovky a školy lyžování'],
              ['120–140 cm', '110–130 cm', 'samostatná jízda po modrých a červených'],
              ['140–160 cm', '130–150 cm', 'přechod k juniorským a závodním modelům']]) +
          '<p>Označení v názvu produktu často udává rozsah délky, například řada ve velikostech 100–140 cm, kde se vybírá konkrétní kus. Najděte v popisu obchodu, jakou délku ten který odkaz skutečně nabízí, protože u stejného modelu se často prodává více velikostí.</p>'
          '<h2>Tvar, tuhost a konstrukce</h2>'
          '<p>Dětské lyže jsou většinou širší v lopatce a patě a užší uprostřed, aby se snadno zatáčely. Čím větší je rozdíl mezi nimi, tím snáze lyže zatáčí a tím líp odpouští první chyby. Závodnější modely mají menší boční zakřivení a delší poloměr, takže drží stopu při větší rychlosti, ale vyžadují techničtější jízdu.</p>'
          '<ul><li><strong>Měkký prohyb:</strong> pro menší a lehčí děti, které by tužší lyži neprohnuly.</li>'
          '<li><strong>Střední tuhost:</strong> univerzální volba pro školáky na upravených sjezdovkách.</li>'
          '<li><strong>Tužší jádro:</strong> pro lyžaře s oddílovou přípravou. Neznamená, že jsou lyže pro každé dítě lepší.</li>'
          '<li><strong>Dřevěné a kompozitní jádro:</strong> kvalitnější modely jsou stabilnější a déle drží tvar než levné plastové provedení.</li>'
          '<li><strong>Rocker v lopatce:</strong> mírně zvednutá špička usnadňuje vjezd do oblouku a zlepšuje chování v hlubším sněhu.</li></ul>'
          '<h2>Vázání: co se dá nastavit a kdo to dělá</h2>'
          '<p>Vázání je nejdůležitější bezpečnostní prvek celé sestavy. Dětské vázání se nastavuje podle váhy dítěte, zkušeností a délky podrážky boty. Kdo se rozhodne pro komplet, ušetří si výběr kompatibilního vázání, protože výrobce už lyže a vázání spojil. U lyží bez vázání dohlédněte, aby zvolené vázání odpovídalo normě podrážky dětských bot a mělo správnou délku brzdy pro šířku lyže.</p>'
          '<p>Značné rozdíly najdete v nastavitelnosti. Některé komplety mají vázání, které se posouvá podle velikosti boty a dá se použít několik sezón, jiné jsou pevně dané. Seřízení by mělo provádět servis s přístrojem, který ověří uvolňovací sílu. Nedělejte ho jen odhadem doma, protože špatně seřízené vázání zvyšuje riziko zranění, ať se při pádu neuvolní, nebo uvolní příliš brzy. Příbuzný výběr vázání pro dospělé najdete v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>.</p>'
          '<h2>Boty, helma a další výbava</h2>'
          '<p>Dítě stojí na botách, ne na lyžích, takže jim věnujte víc času než lyžím. <a href="/lyzarske-boty/">Lyžařské boty</a> musí držet patu. Ve stoje se prsty lehce dotýkají špičky, v předklonu se noha stáhne dozadu a prsty dostanou volnost. Sem se hodí i teplé <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, protože jedna silná vrstva drží lépe než dvě tenké. Pro bezpečnost je nutná <a href="/lyzarske-helmy/">helma</a> a doporučuje se i <a href="/lyzarske-bryle/">brýle</a>. Dětské oblečení najdete v <a href="/lyzarske-obleceni/">lyžařském oblečení</a>, nebo v samostatných <a href="/lyzarske-kombinezy/">kombinézách</a>. Teplou vrstvu pod nimi dodá <a href="/lyzarske-termopradlo/">termoprádlo</a>.</p>'
          '<ul><li>Délku hole ověřte tak, že ji obrátíte, uchopíte pod talířkem a loket má svírat pravý úhel.</li>'
          '<li>Rukavice kupujte s prodlouženou manžetou, která se dá zasunout pod rukáv.</li>'
          '<li>Malé děti hole ještě neumějí využít a často jim spíš překážejí. Pro začátek je klidně vynechte, dokud dítě nezíská jistotu v rovnováze.</li></ul>'
          '<h2>Koupit, půjčit, nebo vyzkoušet bazar</h2>'
          '<p>Děti rostou rychle a lyže jim většinou slouží jednu až dvě sezóny. Proto přichází v úvahu několik cest. Půjčovna dává smysl pro první týden, protože dítě vyzkouší lyžování bez investice. Bazar je dobrá volba u sourozenců nebo při koupi druhých lyží, ale pozorně zkontrolujte hrany, skluznici a vázání. Nové lyže se vyplatí, pokud jezdíte pravidelně, nebo když počítáte s předáním dalšímu dítěti. Sporteka srovnává jen nové zboží českých obchodů a ukazuje, kde je zrovna dostupná správná délka.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Dětské lyže nepotřebují náročnou údržbu, ale několik návyků prodlouží jejich život. Po lyžování je otřete od sněhu, hlavně na hranách, a nechte vyschnout při pokojové teplotě, nikoli u radiátoru. Před zimou zkontrolujte hrany a nechte lyže namazat. Vosky pro domácí použití najdete v kategorii <a href="/lyzarske-vosky/">lyžařské vosky</a>. Na konci sezóny lyže očistěte, lehce promažte a uložte v suchu a chladu, ideálně ve vaku z kategorie <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>. Hodnotu uvolnění sami neměňte a řiďte se návodem výrobce vázání. Nastavení před sezónou nechte ověřit v servisu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Příliš dlouhé lyže:</strong> dítě se bojí zatáčet a rychle se unaví.</li>'
          '<li><strong>Boty o číslo větší:</strong> patu neudrží a dítě má pocit, že lyže neovládá.</li>'
          '<li><strong>Nepřizpůsobené vázání:</strong> seřízené na váhu, kterou dítě už vyrostlo.</li>'
          '<li><strong>Pozdní nákup:</strong> během sezóny chybí oblíbené délky, proto se vyplatí koupit v listopadu nebo začátkem prosince.</li>'
          '<li><strong>Podceněná výbava:</strong> bez helmy a vhodného oblečení dítě nevydrží na svahu ani hodinu.</li></ul>'
          '<h2>Rodinný nákup krok za krokem</h2>'
          '<p>Nejdřív změřte dítě a zapište si výšku a velikost nohy, pak vyberte boty a až potom lyže s vázáním. Hledejte komplet, který odpovídá výšce, a vedle nabídky si prohlédněte i <a href="/lyze-komplety/">lyžařské sety</a>, kde se někdy najde sjezdový komplet i s doplňky. Pokud si rodina chce vyzkoušet i jiný styl, zajímavým doplňkem pro starší děti je <a href="/bezecke-lyzovani/">běžecké lyžování</a> nebo <a href="/snowboarding/">snowboarding</a>. Širší přehled zimních aktivit najdete v kategorii <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[('Jak dlouhé lyže pro dítě vybrat?', 'Podle výšky, váhy a zkušeností. Začátečník potřebuje lyže zhruba po hrudník až bradu, zkušenější jezdec po bradu až nos. Příliš dlouhé lyže se hůř otáčejí a dítě na nich ztrácí jistotu.'),
         ('Má smysl koupit lyže o něco delší, aby je dítě vyrostlo?', 'Ne. Nevhodná délka zhorší ovládání, takže se dítě učí pomaleji. Raději koupte správnou velikost a po sezóně ji předejte dál nebo prodejte.'),
         ('Je lepší komplet s vázáním, nebo lyže zvlášť?', 'Pro rekreační lyžování je komplet pohodlný, protože vázání je už sladěné s lyží. Lyže zvlášť volí zkušení lyžaři a kluby, které chtějí vázání vybrat podle bot a stylu jízdy.'),
         ('Kdo má seřídit vázání na dětských lyžích?', 'Servis nebo prodejna s přístrojem na měření uvolňovací síly. Nastavení závisí na váze dítěte, zkušenostech a velikosti boty, takže odhad doma není bezpečný.'),
         ('Jak často se mění dětské lyže?', 'Nejčastěji po jedné až dvou sezónách, podle toho, jak dítě roste a jak často jezdí. Kvalitnější lyže se dají předat mladšímu sourozenci, pokud jsou hrany a skluznice v pořádku.'),
         ('Od kolika let může dítě začít lyžovat?', 'Záleží na zvládání chůze, rovnováze a zájmu dítěte. Mnoho rodin začíná kolem tří až čtyř let na krátkých plastových lyžích a pomalu přechází k pevnějšímu modelu.'),
         ('Potřebuje dítě hole hned od začátku?', 'Ne. Mladším dětem hole často překážejí, protože se musí soustředit na rovnováhu. Hole se přidávají, až když dítě zvládá základní oblouky.'),
         ('Jaké boty se hodí k dětským lyžím?', 'Dětské lyžařské boty se zapínacími přezkami, které drží patu a mají vhodnou tuhost pro váhu dítěte. Boty by měly sedět pevně a mít jen malou rezervu před prsty, ne rezervu na růst.'),
         ('Jak o dětské lyže pečovat po sezóně?', 'Otřete je, nechte vyschnout při pokojové teplotě, zkontrolujte hrany, promažte skluznici a uložte v chladu a suchu. Hodnotu uvolnění sami neměňte a řiďte se návodem výrobce; nastavení před sezónou nechte ověřit v servisu.'),
         ('Jak poznám, že už dítěti lyže nesedí?', 'Když lyže sahají nad nos, dítě se v nich cítí nejistě nebo je dítě tak těžké, že se lyže prohýbají nad míru. Dalším znakem je opotřebovaná skluznice a hrany, které už nelze opravit.')],
)

# ------------------------------------------------------------------ jezdecke-obleceni
NEW['jezdecke-obleceni'] = dict(long=True,
    title='Jezdecké oblečení: trička, bundy, vesty, rukavice',
    desc='Jezdecké polo trička, mikiny, bundy, vesty a rukavice pro dospělé i děti. Jak vybrat podle sezóny a disciplíny a porovnat nabídky českých obchodů.',
    intro='<p>Jezdecké oblečení se liší od běžného sportovního tím, že musí vydržet sedlo, otěže, plot i stáj. Triko nesmí vylézat z kalhot, bunda se nesmí zadrhnout o sedlo a rukavice musí dovolit cit v prstech. Sporteka porovnává nabídky českých obchodů u jezdeckých polo triček, mikin, bund, vest, rukavic i ochranných airbagových vest pro dospělé a děti.</p>'
          '<p>V kategorii převládají značky ' + B(('fouganza', 'Fouganza'), ('progress', 'Progress'), ('galop-wear', 'Galop Wear'), ('equestrian-queen', 'Equestrian Queen'), ('elt', 'ELT'), ('roeckl', 'Roeckl'), ('hv-polo', 'HV Polo'), ('vestrum', 'Vestrum')) +
          '. Doplněním jsou <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a>, <a href="/jezdecka-obuv/">jezdecká obuv</a>, <a href="/jezdecke-helmy/">jezdecké helmy</a> a <a href="/jezdecke-doplnky/">jezdecké doplňky</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Jezdecké oblečení pro horní část těla se dělí podle použití. Na trénink do stáje a na vyjížďky stačí funkční triko a mikina, závodní disciplíny vyžadují společenské polo, sako nebo košili, a v zimě přibývají prošívané a nepromokavé bundy. Zvláštní skupinou je ochranná vesta s airbagem a rukavice, které jsou součástí celé výbavy.</p>'
          + T(['Typ', 'K čemu slouží', 'Na co dát pozor'], [
              ['Polo tričko s krátkým rukávem', 'letní tréninky a lehké závody', 'prodyšný materiál a delší záda'],
              ['Polo s dlouhým rukávem', 'závody a chladnější dny', 'stojatý límec a pevná manžeta'],
              ['Mikina a fleece', 'stáj, ježdění v přechodných obdobích', 'pružný střih bez ohrnujících se lemů'],
              ['Prošívaná bunda', 'podzimní a zimní vyjížďky', 'pohyblivost v ramenou a délka za sedlo'],
              ['Nepromokavá bunda s kapucí', 'déšť a práce kolem koní', 'ventilace a zakryté zipy'],
              ['Vesta', 'teplá vrstva, která nebrání pohybu rukou', 'zip bez zadrhávání a šev nad pasem'],
              ['Rukavice', 'ochrana dlaní a lepší držení otěží', 'velikost prstů a materiál dlaně'],
              ['Airbagová vesta', 'doplňková ochrana při pádech', 'správná velikost a servis podle výrobce']]) +
          '<p>Jezdecké oblečení se často překrývá s běžnou sportovní módou, takže kromě specializovaných kousků najdete i klasické mikiny s koňským motivem. Pokud je potřebujete jen na stáj, nemusí splňovat pravidla závodů, ale i tam se vyplatí vybírat střih, který nepřekáží v sedle.</p>'
          '<h2>Polo trička a košile pro tréninky a závody</h2>'
          '<p>Jezdecké polo je základ letní garderoby. Má pevný límec, který na sobě udrží tvar, delší záda, aby při předklonu nevylezlo z kalhot, a tenký prodyšný materiál. Závodní verze v bílé nebo tmavé barvě bývají úzké a pružné, tréninkové jsou volnější a lépe odvádějí pot. Rukávy se liší: krátké jsou na horké dny, dlouhé chrání před slunkem a hmyzem a vypadají společensky na turnajích. Pro děti se prodávají dívčí i chlapecké střihy a nezřídka se zdobí malými logy nebo drobnou výšivkou.</p>'
          '<ul><li>Zvolte materiál s elastanem, aby se triko přizpůsobilo při předklonu a zvedání paží.</li>'
          '<li>Světlé odstíny odrážejí slunce, ale po koni a sedle se špiní víc, takže počítejte s častějším praním.</li>'
          '<li>Pro závody si předem přečtěte řád disciplíny, protože barvy a typy oděvu se mohou lišit.</li></ul>'
          '<h2>Mikiny, fleece a vesty do stáje</h2>'
          '<p>Stáj je místo, kde se jezdecké oblečení nejvíc zašpiní, takže na práci kolem koní se hodí robustnější mikina nebo vesta. Fleece a pletené mikiny drží teplo a dobře se nosí, jen se do nich zachytávají chlupy z koňské srsti a špatně se čistí. Prošívaná vesta nechává volné ruce a chrání trup před chladem. Oblíbené jsou i hřejivé modely s beránkem, které si ale zasluhují šetrné praní, aby se vlákno nezhrubilo.</p>'
          '<h2>Bundy: prošívané, nepromokavé a zimní</h2>'
          '<p>Bunda do sedla má jiné nároky než běžná zimní. Musí být dost dlouhá, aby zakryla ledviny a sedací část, ale nesmí se zachytávat o sedlo. Nepromokavé bundy mívají zatěsněné švy a kapuci, která se vejde pod helmu nebo se dá stáhnout. Prošívané bundy jsou lehké a teplé, ale ve vlhku se rychle prosáknou. U dětí se osvědčily modely s odepínací kapucí, které se hodí do stáje i na vyjížďku. Pokud chcete jezdit i v mrazu, zvolte vrstvení: funkční prádlo, mikina a lehká bunda.</p>'
          '<ul><li>Boční rozparky usnadní pohyb v sedle a nezadrhnou se o zadní část sedla.</li>'
          '<li>Reflexní prvky pomáhají při vyjížďkách za šera. Pokud jezdíte po veřejných cestách, přidejte i reflexní vestu z kategorie <a href="/vybaveni-pro-kone/">vybavení pro koně</a>.</li>'
          '<li>Kapsy by měly mít zip nebo klopu, aby z nich při klusu nevypadly klíče.</li></ul>'
          '<h2>Jezdecké rukavice</h2>'
          '<p>Rukavice jsou nejčastěji kupovaným doplňkem a největším důvodem k opotřebení. Otěže odírají dlaň, zvlášť při dlouhých vyjížďkách nebo při práci s hříbětem. Dobrá rukavice má tenkou kůži nebo syntetickou dlaň s protiskluzem, elastický hřbet, který sleduje pohyb prstů, a suchý zip na zápěstí. Zimní verze mají podšívku a vyšší manžetu, letní bývají perforované a lehké.</p>'
          + T(['Materiál dlaně', 'Výhody', 'Nevýhody'], [
              ['Kůže', 'dobrý cit, pevné držení', 'po namočení tvrdne'],
              ['Syntetická kůže', 'snadná údržba, stálý tvar', 'méně prodyšná'],
              ['Textil s protiskluzem', 'lehká, levná na výměnu', 'rychleji se obrušuje'],
              ['Zimní kombinace', 'teplá, odolná proti větru', 'menší cit v prstech']]) +
          '<p>Při zkoušení rukavic sevřete pěst a napněte prsty. Pokud látka zhoustne nebo se zkroutí, rukavice je malá. Příliš velké rukavice naopak tvoří záhyby, které tisknou prsty otěžemi.</p>'
          '<h2>Ochranné vesty a airbagy</h2>'
          '<p>Ochranná jezdecká vesta se obléká přes tričko nebo pod bundu a zmírňuje dopad při pádu. Airbagová varianta se při pádu nafoukne a chrání trup a páteř. Funguje jen správně nasazená a zapojená do popruhu v sedle, proto se při koupi nejdřív podívejte na velikostní tabulku výrobce a na způsob připojení. Po každé aktivaci je nutné vyměnit patronu nebo dát vestu do servisu podle návodu. Je to doplňková ochrana, ne náhrada helmy: <a href="/jezdecke-helmy/">jezdecká helma</a> zůstává základem.</p>'
          '<h2>Oblečení pro děti</h2>'
          '<p>Dětské jezdecké oblečení je v poměru k dospělému malá nabídka, ale pokrývá nejdůležitější kusy: polo trička, mikiny, zimní bundy a rukavice. U dětí dávejte přednost pružným materiálům, které dovolují volný pohyb, a švům, které neškrábou na kůži. Pokud dítě jezdí v oddíle, zeptejte se trenéra na barvu a střih, než koupíte první závodní kousky. Kalhoty a boty pro děti jsou zvlášť v <a href="/jezdecke-kalhoty/">jezdeckých kalhotách</a> a <a href="/jezdecka-obuv/">jezdecké obuvi</a>.</p>'
          '<h2>Materiály a péče</h2>'
          '<p>Většina jezdeckých triček je z polyesteru s elastanem, který rychle schne a nemačká se. Mikiny jsou obvykle směs bavlny a polyesteru. Perte při doporučené teplotě, bez aviváže, která zhoršuje odvod potu. Prošívané a nepromokavé bundy perte šetrně a občas oživte impregnací. Rukavice po namočení nesušte na radiátoru, aby se kůže nezkroutila, ale nechte je vyschnout v pokojové teplotě. Odznaky a nášivky obracejte naruby, aby se v pračce neodřely.</p>'
          '<h2>Jak vybrat podle jezdecké činnosti</h2>'
          '<ul><li><strong>Rekreační vyjížďky:</strong> funkční polo nebo triko, vesta a nepromokavá bunda v tašce.</li>'
          '<li><strong>Drezura a parkur:</strong> společenské polo, sako a rukavice, které se hodí k barvě oblečení.</li>'
          '<li><strong>Stáj a péče o koně:</strong> odolná mikina a zimní vesta, která se nebojí špíny.</li>'
          '<li><strong>Zimní jízdy:</strong> vrstvení s funkčním prádlem a teplou bundou.</li>'
          '<li><strong>Začátečníci:</strong> začněte jedním polo trikem, rukavicemi a nepromokavou bundou, dalších kusů si dokupujte podle zájmu.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Srovnáváme nabídky českých obchodů u stejného kusu a upozorňujeme, kde jsou ještě dostupné vaše velikosti. Velikosti jezdeckého oblečení se mezi značkami liší, takže před koupí přečtěte tabulku výrobce a změřte hrudník, pas a délku paže. Vedle kategorie najdete i ostatní jezdeckou výbavu v <a href="/jezdectvi/">jezdectví</a>.</p>',
    faq=[('Jaké oblečení je vhodné pro začínajícího jezdce?', 'Pohodlné pružné triko nebo polo, rukavice, helma a pevné boty s podpatkem. Další kusy si pořiďte až podle disciplíny a sezóny.'),
         ('Čím se jezdecké polo liší od běžného trička?', 'Má pevnější límec, delší záda, aby nevylezlo z kalhot při předklonu, a pružný materiál. Závodní verze bývají přesně střižené, tréninkové volnější.'),
         ('Jak vybrat jezdecké rukavice?', 'Podle velikosti ruky a použití. Sevřete pěst a zkontrolujte, že látka netlačí na prsty. Tenké rukavice dávají cit, zimní modely teplo.'),
         ('Mám si koupit bundu delší, nebo kratší?', 'Raději delší, aby zakryla spodní část zad a sedací část. Nesmí se však zachytávat o sedlo, proto se hodí rozparky.'),
         ('Hodí se jezdecká mikina i mimo stáj?', 'Ano, většina mikin má běžný střih a dá se nosit i každodenně. Pružný střih pomáhá v sedle a motiv koně nemusí vadit.'),
         ('Nahradí airbagová vesta jezdeckou helmu?', 'Ne. Vesta chrání trup, ale helma chrání hlavu. Obě součásti se doplňují a vesta musí být správně připojena k sedlu.'),
         ('Jak prát jezdecké oblečení?', 'Při doporučené teplotě, naruby, bez aviváže. Bundy občas oživte impregnací a rukavice sušte při pokojové teplotě.'),
         ('Jaká výbava je potřeba na závody?', 'Řídí se pravidly pořadatele. Obvykle se vyžaduje společenské polo nebo košile, sako, rukavice a vhodné barvy. Zkontrolujte propozice předem.'),
         ('Jak vybrat oblečení pro dítě?', 'Dbejte na pružný materiál, měkké švy a vhodnou velikost, která nebude překážet v sedle. Trenér dětí může poradit s barvami pro závody.'),
         ('Co si obléci na vyjížďku v zimě?', 'Vrstvy: funkční prádlo, mikinu nebo fleece a lehčí bundu. Rukavice by měly mít podšívku, ale nesmí omezovat cit v prstech.')],
)

# ------------------------------------------------------------------ snowboardova-vazani
NEW['snowboardova-vazani'] = dict(long=True,
    title='Snowboardová vázání: typy, velikost, kompatibilita',
    desc='Snowboardová vázání pánská, dámská i dětská. Jak zvolit tuhost, velikost, zapínání a montáž na desku a porovnat nabídky českých obchodů.',
    intro='<p>Vázání je spojnice mezi botou a deskou a přenáší každý pohyb nohy na hranu. Kvalitní vázání zrychlí reakce, drží nohu v pohodlné poloze a ulehčí dlouhý den na svahu, špatně zvolené způsobí otlaky, ztrátu citu nebo nechtěné uvolnění. Sporteka porovnává nabídky českých obchodů u klasických vázání s pásky, rychloupínacích systémů, dětských modelů i náhradních pásků.</p>'
          '<p>V kategorii najdete značky ' + B(('nitro', 'Nitro'), ('head', 'Head'), ('union', 'Union'), ('bataleon', 'Bataleon'), ('burton', 'Burton'), ('dreamscape', 'Dreamscape'), ('nidecker', 'Nidecker'), ('drake', 'Drake')) +
          '. Vázání vybírejte společně s <a href="/snowboardy/">deskou</a> a <a href="/snowboardove-boty/">botami</a>, případně hledejte hotové <a href="/snowboardove-sety/">snowboardové sety</a>.</p>',
    guide='<h2>Typy snowboardových vázání</h2>'
          '<p>Vázání se liší tím, jak se do něj nastupuje, jak je tuhé a pro jaký styl je navržené. Většina modelů je klasická s dvěma pásky, ale přibývá rychloupínacích a hybridních systémů. Typ určuje komfort při nasazování na svahu a také přesnost jízdy.</p>'
          + T(['Typ', 'Princip', 'Hodí se pro'], [
              ['Klasické s dvěma pásky', 'pásek přes špičku a pásek přes nárt, úchyt na pátku', 'univerzální, nejběžnější volba'],
              ['Rychloupínací zadní vstup', 'sklopná zadní opěrka, noha se zasune a zapne', 'rychlé nasazování na vleku'],
              ['Rychlý vstup bez pásků (např. Step On)', 'bota se zacvakne přímo do vázání, vyžaduje kompatibilní boty', 'časté sedání a vstávání, začátečníci'],
              ['Dětská vázání', 'menší a měkčí, nastavitelná na růst', 'děti a nejmenší jezdci'],
              ['Dámské modely', 'užší patní míska, často měkčí', 'jezdkyně s menší nohou'],
              ['Freeridové a tvrdé', 'větší opěrka a tužší základna', 'rychlá jízda, strmý terén']]) +
          '<p>V kategorii najdete i drobné součásti, například sady předních pásků nebo náhradní úchyty. Hodí se, když se pásek zlomí nebo opotřebuje, a není nutné kupovat celé vázání.</p>'
          '<h2>Tuhost: od měkkého po tvrdé</h2>'
          '<p>Tuhost vázání určuje, jak rychle se pohyb nohy projeví na desce. Měkké vázání odpouští chyby, hodí se do snowparku a na triky, protože se dá využít flex. Střední tuhost je univerzální a vyhovuje většině jezdců na upravených svazích. Tvrdé vázání přenáší sílu přesně a bez zpoždění, což ocení rychlí a freeridoví jezdci, ale způsobí méně citu pro drobné nerovnosti.</p>'
          '<ul><li><strong>Začátečníci:</strong> měkčí až střední tuhost, která se lépe ovládá a odpouští chyby.</li>'
          '<li><strong>Freestyle:</strong> měkčí a odpružená vázání pro skoky a přistání.</li>'
          '<li><strong>All-mountain:</strong> střední tuhost jako kompromis mezi pohodlím a přesností.</li>'
          '<li><strong>Freeride a carving:</strong> tužší vázání s vyšší zadní opěrkou, která pomáhá při zatáčení na hranách.</li></ul>'
          '<p>Tuhost vázání by měla odpovídat tuhosti desky a bot. Příliš tvrdé vázání na měkké desce ji přetíží a nepřináší žádný užitek, příliš měkké vázání na tvrdé desce nedokáže přenášet sílu.</p>'
          '<h2>Velikost podle bot</h2>'
          '<p>Vázání se vyrábí ve velikostech S, M a L podle délky podrážky boty, a výrobci uvádějí tabulky, které se mohou lišit. Bota by měla ve vázání sedět pevně, špička ani pata by neměla přesahovat okraj víc, než doporučuje výrobce, a pásky musí dosednout na správná místa. Pokud je vázání příliš velké, noha se v něm pohybuje, pokud je malé, tlačí na prsty.</p>'
          + T(['Velikost vázání', 'Orientační velikost boty (EU)', 'Poznámka'], [
              ['S', 'zhruba 36–40', 'mohou se lišit podle značky'],
              ['M', 'zhruba 39–44', 'nejběžnější velikost'],
              ['L', 'zhruba 43–48', 'větší chodidla a široké boty'],
              ['Dětské', 'zhruba do 38', 'často nastavitelné na růst']]) +
          '<p>Tabulky berte jako orientační. Každý výrobce má vlastní rozměry, takže vždy porovnejte údaje v popisu u konkrétního modelu a zkuste vázání s botami, než ho namontujete. Pokud nosíte hraniční velikost, zeptejte se prodejce nebo ověřte rozměry podrážky boty.</p>'
          '<h2>Kompatibilita s deskou: disky a šrouby</h2>'
          '<p>Vázání se k desce připevňuje pomocí disku, který se zašroubuje do otvorů v desce. Většina desek má klasický čtyřbodový nebo trojbodový vzor, ale některé značky používají vlastní systém, například kanálový systém desky. Před koupí proto ověřte, jak je deska vybavena a jaký disk vázání potřebuje. Vázání a deska mohou být od různých výrobců, ale kompatibilita musí sedět na šrouby a rozteče.</p>'
          '<ul><li><strong>Stance:</strong> šířka postoje se nastavuje podle výšky jezdce a podle zvyklostí.</li>'
          '<li><strong>Úhly nohou:</strong> kladné úhly vpředu a mírně záporné vzadu patří k běžnému nastavení pro freestyle, carvingoví jezdci volí větší úhly.</li>'
          '<li><strong>Šrouby:</strong> používejte šrouby, které jsou součástí balení, a utahujte je podle návodu.</li></ul>'
          '<h2>Nastavení: pásky, highback a forward lean</h2>'
          '<p>Po montáži vázání čeká ještě jemné doladění. Pásky se utahují tak, aby bota držela, ale nezastavovala krevní oběh. Highback je zadní opěrka lýtka a jeho úhel a otočení se nastavuje, aby kopíroval boty. Forward lean, tedy předklon, zvyšuje reakce na hranu, ale zatěžuje stehna, proto ho začátečníci obvykle nechávají nižší. Zkuste si nastavení doma na koberci a před sezónou ho zkontrolujte, protože šrouby se po čase uvolňují.</p>'
          '<h2>Pro koho se které vázání hodí</h2>'
          '<ul><li><strong>Dítě a začátečník:</strong> měkčí vázání, jednoduché zapínání a nastavitelná velikost. U dětí zkontrolujte, jestli se dá vázání posunout s růstem boty.</li>'
          '<li><strong>Dámy:</strong> dámské vázání s užší pátkou a obvykle měkčím flexem, které sedí na menší boty.</li>'
          '<li><strong>Muži a pokročilí:</strong> modely s různou tuhostí podle stylu, od odpružených freestyle po tužší pro carving.</li>'
          '<li><strong>Splitboard a skialpové snowboardy:</strong> mají vlastní vázání, která se mění mezi stoupáním a sjezdem. Se skialpinismem souvisí kategorie <a href="/skialpinismus/">skialpinismus</a>.</li>'
          '<li><strong>Cestování se snowboardem:</strong> pásky se dají odepnout, aby vázání zabralo méně místa v tašce.</li></ul>'
          '<h2>Péče a údržba</h2>'
          '<p>Vázání ocení krátkou péči po každé sezóně. Opláchněte od soli a sněhu, osušte a zkontrolujte pásky, přezky a šrouby. Pokud se objeví trhlinky v plastu, vázání vyměňte, protože jejich praskání na svahu může být nebezpečné. Kovové součásti lehce promažte a uložte vázání v suchu mimo přímé slunce, kterým plasty časem křehnou. Při převozu ho zabalte, aby se pásky nezkroutily.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě vázání bez kontroly kompatibility s deskou.</li>'
          '<li>Velikost vázání zvolená podle sebe, ne podle bot.</li>'
          '<li>Příliš tvrdé vázání pro začátečníka, které unavuje nohy.</li>'
          '<li>Uvolněné šrouby po první sezóně, protože je nikdo nedotáhl.</li>'
          '<li>Zanedbané pásky, které zůstanou vlhké v tašce a zkroutí se.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu a upozorňujeme na výprodejové velikosti. U vázání vždy ověřte velikost a typ disku. Pokud vybíráte celou sestavu, podívejte se i na <a href="/snowboardove-chranice/">snowboardové chrániče</a> a širší přehled v kategorii <a href="/snowboarding/">snowboarding</a>. Pro zimní den se hodí i <a href="/lyzarske-bryle/">brýle</a> a <a href="/lyzarske-helmy/">helma</a>.</p>',
    faq=[('Jak poznám správnou velikost snowboardového vázání?', 'Podle velikosti boty a tabulky výrobce. Bota má ve vázání sedět pevně, špička a pata nesmějí přesahovat víc, než doporučuje výrobce.'),
         ('Jak tuhé vázání zvolit?', 'Začátečníci a freestyle jezdci volí měkčí až střední, rychlí a freeridoví jezdci tužší. Tuhost by měla odpovídat desce i botám.'),
         ('Hodí se každé vázání na každou desku?', 'Ne. Záleží na rozteči otvorů a systému montáže. Před koupí ověřte, jaký disk vázání potřebuje a jaké otvory má deska.'),
         ('Co znamená highback a forward lean?', 'Highback je zadní opěrka lýtka, forward lean je jeho předklon. Vyšší předklon zrychluje reakci na hranu, ale víc zatěžuje stehna.'),
         ('Mohu koupit dětské vázání na vyrůstání?', 'Dětská vázání mívají nastavitelný rozsah velikosti, ale nesmí být příliš velká. Bota musí sedět pevně, jinak vázání nepřenese pohyb.'),
         ('Jak nastavit úhly nohou?', 'Běžné je kladný úhel vpředu a mírně záporný nebo nulový vzadu. Přesné hodnoty záleží na stylu a pohodlí, zkoušejte po malých krocích.'),
         ('Jak často kontrolovat šrouby na vázání?', 'Před sezónou a během ní občas. Vibrace je mohou povolit, proto je dotáhněte podle návodu výrobce.'),
         ('Jsou rychloupínací vázání pro začátečníky?', 'Ano, usnadní nasazení a snižují námahu při opakovaném sedání. Zvažte jejich tuhost a kompatibilitu s botami.'),
         ('Jak péče prodlouží život vázání?', 'Opláchnout, osušit, zkontrolovat pásky a šrouby a skladovat na suchu mimo slunce. Prasklé plastové díly vyměňte.'),
         ('Mohu vázání použít na splitboard?', 'Klasické vázání se na splitboard zpravidla nehodí, protože potřebuje systém pro stoupání. Hledejte speciální splitboardová vázání.')],
)

# ------------------------------------------------------------------ predtreninkove-boostery
NEW['predtreninkove-boostery'] = dict(long=True,
    title='Předtréninkové boostery: typy, složení, výběr',
    desc='Předtréninkové boostery a pre-workout prášky i kapsle. Jak číst složení, volit příchuť a balení a porovnat nabídky českých obchodů. Bez zdravotních slibů.',
    intro='<p>Předtréninkové boostery, anglicky pre-workout, jsou doplňky stravy v podobě prášku, kapslí nebo nápoje, které se užívají před cvičením. Jejich složení se mezi výrobci výrazně liší, od jednoduchých směsí po bohaté formule s mnoha látkami. Sporteka porovnává nabídky českých obchodů a pomáhá se zorientovat v balení, příchutích a složení. Nejde o lék ani o zdravotní radu, před užíváním doplňků se poraďte s lékařem.</p>'
          '<p>V kategorii najdete značky ' + B(('gymbeam', 'GymBeam'), ('myprotein', 'MyProtein'), ('amix', 'Amix'), ('atp', 'ATP'), ('nutrend', 'Nutrend'), ('optimum-nutrition', 'Optimum Nutrition'), ('nutriversum', 'Nutriversum'), ('maxxwin', 'Maxxwin')) +
          '. Související výběr: <a href="/kreatin/">kreatin</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny BCAA</a>, <a href="/iontove-napoje/">iontové nápoje</a> a <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>',
    guide='<h2>Co jsou předtréninkové boostery</h2>'
          '<p>Pre-workout je pojem pro širokou skupinu doplňků, které se pijí nebo polykají krátce před tréninkem. Obsahují směs látek, které výrobci kombinují podle zaměření: některé míří na soustředění, jiné na pocit pumpy, další na vytrvalost. Tvrzení o účincích se u jednotlivých produktů liší a v tomto textu je nehodnotíme. Berte je jako přehled toho, co se na etiketách objevuje a jak se v nabídce orientovat.</p>'
          '<p>Důležité je pochopit, že booster není náhrada spánku, jídla ani tréninkového plánu. Je to jen doplněk a mnoho sportovců bez něj funguje dobře.</p>'
          '<h2>Formy: prášek, kapsle, nápoj a tyčinka</h2>'
          + T(['Forma', 'Výhody', 'Na co dát pozor'], [
              ['Prášek k rozmíchání', 'nejčastější, volba příchutí, přesné dávkování měrkou', 'nutnost shaker nebo láhve, usazování'],
              ['Kapsle a tablety', 'snadno přenosné, bez chuti', 'nižší obsah v jedné dávce, víc kapslí najednou'],
              ['Hotový nápoj', 'okamžitě připravený', 'těžší balení a menší výběr příchutí'],
              ['Gely a šoty', 'jedna dávka v jednom sáčku', 'menší objem, často pro vytrvalostní sporty']]) +
          '<p>V kategorii převládají prášky ve velkých dózách a pytlích, ale najdete i kapsle a hotové nápoje. U prášků se obsah uvádí v gramech, u kapslí v počtu kusů, takže porovnání mezi formami vyžaduje čtení etikety.</p>'
          '<h2>Jak číst složení</h2>'
          '<p>Etiketa popisuje obsah na jednu porci, která bývá jedna odměrka. Podívejte se na několik věcí. Kolik gramů má porce, jaké látky jsou uvedené a zda je jejich množství vypsané, nebo skryté v „proprietární směsi“, kde se konkrétní dávky neuvádějí. Transparentní etiketa umožňuje porovnat výrobky mezi sebou a ověřit si, zda dostanete, co čekáte.</p>'
          '<ul><li><strong>Kofein:</strong> nejčastější složka. Množství na porci se liší, takže ho sečtěte s ostatními zdroji, třeba kávou.</li>'
          '<li><strong>Citrulin, arginin a beta-alanin:</strong> aminokyseliny, které se v boosterech objevují často. Beta-alanin může vyvolat mravenčení kůže, které je u něj známé.</li>'
          '<li><strong>Kreatin a taurin:</strong> některé směsi je obsahují, jiné ne. Kreatin se prodává i samostatně v kategorii <a href="/kreatin/">kreatin</a>.</li>'
          '<li><strong>Sladidla a barviva:</strong> určují chuť a barvu. Sledujte, pokud na některé reagujete.</li>'
          '<li><strong>Vitaminy a minerály:</strong> v některých směsích jsou doplněny, jejich přehled najdete v <a href="/vitaminy-a-mineraly/">vitaminech a minerálech</a>.</li></ul>'
          '<h2>Stimulantní a bezstimulantní varianty</h2>'
          '<p>Nabídka se dělí na dvě velké skupiny. Stimulantní boostery obsahují kofein nebo podobné látky a jejich užívání večer může narušit spánek. Bezstimulantní se prodávají pro ty, kdo trénují pozdě, kofein nesnášejí nebo ho nechtějí. Označení „stim-free“ obvykle znamená, že produkt kofein neobsahuje. Ověřte si to na etiketě, protože formulace se liší.</p>'
          '<h2>Pro koho a pro koho ne</h2>'
          '<p>Výrobci obvykle upozorňují, že boostery nejsou určené pro děti, těhotné ani kojící ženy a lidi s onemocněním srdce nebo krevního tlaku. Pokud užíváte léky nebo máte zdravotní problém, poraďte se s lékařem. To platí i pro zdravé dospělé, kteří začínají. Doporučuje se začít polovinou porce a sledovat reakci těla. Při zrychleném tepu, nespavosti nebo nevolnosti užívání přerušte. Tento text je obecná informace, ne zdravotní doporučení.</p>'
          '<h2>Příchutě, rozpustnost a praktické věci</h2>'
          '<p>Ovocné příchutě jako ananas, mango, citron, červený pomeranč nebo kola bývají běžné, ale najdete i neutrální varianty bez sladidel, které se míchají do šťávy. Prášky s vysokým obsahem látek se hůře rozpouštějí, proto doporučujeme shaker s kuličkou nebo pěnu v láhvi. Některé směsi po rozmíchání mírně hustnou a mají sušší dochuť. Pokud kupujete poprvé, vezměte menší balení, abyste nelitovali, když vám příchuť nebude vyhovovat. Pro pití během tréninku se hodí <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>'
          '<h2>Kdy booster užívat</h2>'
          '<p>Doporučení výrobců bývá užít porci zhruba půl hodiny před tréninkem, často rozmíchanou ve vodě. Nepřekračujte doporučenou dávku a nesčítejte více produktů s kofeinem. Vyhněte se užití pozdě večer, pokud ho trénink končí krátce před spaním. Vedle boosteru nezapomínejte na pitný režim, který lze doplnit <a href="/iontove-napoje/">iontovými nápoji</a>, a na jídlo, které dodá energii.</p>'
          '<h2>Boostery a související doplňky</h2>'
          '<p>Pre-workout nelze zaměňovat s dalšími doplňky. Po tréninku se pije <a href="/proteiny/">protein</a>, během vytrvalostních aktivit se sahá po <a href="/energeticke-gely-a-tycinky/">energetických gelech a tyčinkách</a>, a na regeneraci se používají <a href="/aminokyseliny-bcaa/">aminokyseliny</a>. Pro různé aktivity existují i jiné cesty, třeba <a href="/spalovace-tuku/">spalovače tuku</a>, které jsou zvláštní kategorií. Pro každý z nich platí obecné pravidlo: doplněk má jen doplnit pestrou stravu.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Prášky uchovávejte v dobře uzavřené dóze na suchém a chladném místě, nejlépe mimo vlhkost kuchyně. Po otevření spotřebujte do doby uvedené na obalu a vždy používejte měrku, která je součástí balení. Zhrudkovatění je znamení vlhkosti. Kapsle uchovávejte v původním obalu s vysoušedlem. Zkontrolujte datum minimální trvanlivosti a nekupujte velké balení, které nestihnete spotřebovat.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Výběr podle příchutě a marketingu místo čtení složení.</li>'
          '<li>Dvojnásobná dávka „pro silnější účinek“.</li>'
          '<li>Kombinace s dalšími zdroji kofeinu, například energy drinky.</li>'
          '<li>Užívání večer, které narušuje spánek.</li>'
          '<li>Očekávání zázračných výsledků: základem zůstává trénink, strava a odpočinek.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Srovnáváme nabídky českých obchodů u stejného produktu a sledujeme dostupné příchutě a velikosti balení. Při porovnání dívejte na cenu za porci, ne za balení, a na obsah látek v jedné porci. Širší nabídku najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>, na zdravý životní styl se zaměřuje také <a href="/fitness/">fitness</a>.</p>',
    faq=[('Co jsou předtréninkové boostery?', 'Doplňky stravy ve formě prášku, kapslí nebo nápoje, které se užívají před cvičením. Složení se mezi značkami liší.'),
         ('Kdy se booster užívá?', 'Výrobci obvykle doporučují užít porci zhruba půl hodiny před tréninkem. Přesný návod je na etiketě konkrétního produktu.'),
         ('Co znamená stim-free?', 'Označení pro produkty bez kofeinu a dalších stimulantů. Vždy zkontrolujte složení na etiketě.'),
         ('Jak číst etiketu boosteru?', 'Podívejte se na velikost porce, seznam látek a jejich množství. Pozor na proprietární směsi, kde se jednotlivé dávky neuvádějí.'),
         ('Pro koho booster není vhodný?', 'Výrobci uvádějí, že nejsou určené pro děti, těhotné a kojící ženy ani lidi se zdravotními potížemi. Při pochybnostech se poraďte s lékařem.'),
         ('Mohu užívat booster večer?', 'Pokud obsahuje kofein, může narušit spánek, proto se večer raději volí bezstimulantní varianta nebo se booster vynechá.'),
         ('Jak se booster rozmíchává?', 'Obvykle odměrka prášku s vodou ve shakeru. Pro lepší rozpuštění použijte shaker s kuličkou a dodržte množství vody z návodu.'),
         ('Co je to proprietární směs?', 'Směs látek, u které výrobce neuvádí jednotlivá množství. Porovnání s jinými produkty je pak složitější.'),
         ('Mám začít plnou dávkou?', 'Doporučuje se začít menší porcí a sledovat reakci. Nikdy nepřekračujte dávku uvedenou na obalu.'),
         ('Jak boostery skladovat?', 'V uzavřené dóze na suchém a chladném místě. Po otevření spotřebujte v termínu z obalu a vždy použijte přiloženou měrku.')],
)


# ------------------------------------------------------------------ rozšíření sekcí (stejná vlna)
NEW['detske-lyze']['guide'] += (
    '<h2>Jak probíhá první den na sněhu</h2>'
    '<p>Nejlepší start je krátký a hravý. Dopoledne stačí dvě až tři hodiny, pak teplé jídlo a odpočinek. Děti se rychle unaví a zmrznou, takže po obědě už často nemají sílu na další jízdy. Zvolte plochý svah s kouzelným kobercem nebo malým vlekem, kde se dítě naučí stát na lyžích, brzdit pluhem a zvedat spadlou lyži. Až poté přichází na řadu první oblouky. Ve škole lyžování se dítě učí v partě, což je často lepší než rodičovská výuka, protože ho motivují vrstevníci.</p>'
    '<p>Při prvním dni vynechejte vleky, které dítě neovládá, a vyhněte se přeplněným svahům o víkendech. Nechte děti, ať si samy nasadí lyže: čím dřív poznají, jak se zapínají a otevírají, tím méně pomoci později potřebují. Do kapsy dejte svačinu, náhradní rukavice, krém s vysokým UV filtrem na obličej a balzám na rty, protože slunce na sněhu rychle spálí tváře.</p>'
    '<h2>Nastavení lyží pro různé věkové skupiny</h2>'
    '<ul><li><strong>Předškoláci:</strong> nejkratší lyže, měkký prohyb, jednoduché vázání. Hlavním cílem je rovnováha a radost z klouzání.</li>'
    '<li><strong>Mladší školáci:</strong> lyže po bradu, střední tuhost, dobře nastavené vázání. Začínají se učit řízené oblouky.</li>'
    '<li><strong>Starší školáci:</strong> lyže po nos a tužší jádro, pokud už jezdí rychleji a na strmějších svazích.</li>'
    '<li><strong>Závodní dorost:</strong> specializované modely podle pokynů klubu, často s deskou nebo plotnou pod vázáním.</li></ul>'
    '<p>Každé dítě roste jinak, proto se řiďte spíše jeho schopnostmi a váhou než věkem. Zkušený trenér ve škole nebo v půjčovně rád poradí, kdy je čas na výměnu za delší model.</p>')

NEW['jezdecke-obleceni']['intro'] = NEW['jezdecke-obleceni']['intro'].replace(
    'pro dospělé a děti.</p>', 'pro dospělé a děti. Vybrat se dá podle sezóny, jezdecké činnosti i toho, jestli oblečení použijete jen ve stáji, nebo i na závodech.</p>', 1)
NEW['jezdecke-obleceni']['guide'] += (
    '<h2>Vrstvení během roku</h2>'
    '<p>V jezdectví se počasí pozná nejdřív na rukou a krku. Na jaře a na podzim se osvědčuje třívrstvé oblékání: tenké funkční triko, mikina nebo fleece a lehká bunda, kterou lze sundat, když se kůň rozjede. V létě stačí lehké polo s UV ochranou a ve vedru se vyplatí zvolit světlou barvu. V zimě zvolte vrstvy místo jednoho tlustého kusu, protože v sedle se hýbete a potíte se, a zároveň vám při pomalé chůzi rychle vychladnou ruce a záda. Funkční spodní vrstvu najdete v kategoriích <a href="/termopradlo/">termoprádlo</a> a <a href="/merino/">merino</a>, které se hodí i pod jezdecké oblečení.</p>'
    '<h2>Barvy, nášivky a viditelnost</h2>'
    '<p>Při výběru barvy myslete na praktické věci. Tmavé odstíny skryjí zašpinění z ošetřování, světlé se hodí na závody a odrážejí slunce. Nášivky a výšivky s koňským motivem jsou oblíbené u dětí, ale na závodech mohou být omezené. Na vyjížďkách po silnici nebo za šera pomáhá reflexní prvek, a to na bundě i na rukávech. Viditelnost je v provozu bezpečnostní otázka, ne jen móda, proto se vyplatí mít reflexní prvky na jezdci i na koni.</p>'
    '<h2>Velikosti a střihy</h2>'
    '<p>Jezdecké střihy jsou obvykle užší v pase a delší v zádech než běžná sportovní trička. Dámské modely mají jiný střih v hrudi a ramenou, pánské jsou rovnější. Dětské velikosti se označují věkem nebo výškou, a ty se mezi značkami liší, proto se řiďte tabulkou u produktu. Kupujete-li bundu, zkuste si v ní zvednout ruce nad hlavu a předklonit se. Pokud se záda zvedají nad pas nebo manžety vyjíždějí z rukávů, je střih příliš malý.</p>')

NEW['snowboardova-vazani']['intro'] = NEW['snowboardova-vazani']['intro'].replace(
    'náhradních pásků.</p>', 'náhradních pásků. Vázání nejde vybrat izolovaně, protože musí ladit s botou, deskou i stylem jízdy, a proto je výběr jedním z nejdůležitějších kroků při skládání výbavy.</p>', 1)
NEW['snowboardova-vazani']['guide'] += (
    '<h2>Snowpark, svahy a freeride v praxi</h2>'
    '<p>Styl jízdy ovlivňuje, jaké vázání se hodí. Ve snowparku jezdec skáče a přistává, takže ocení měkčí vázání, které pohlcuje nárazy, a lehkou konstrukci. Na upravených svazích a při carvingu hrají roli přesnost a rychlá reakce, proto se hodí tužší základna a vyšší highback. Freerideoví jezdci kombinují oboje: potřebují pevnou oporu při rychlé jízdě a dostatečný komfort na dlouhých sjezdech v prašanu. Pokud se nemůžete rozhodnout, zvolte univerzální all-mountain model.</p>'
    '<h2>Pásky, přezky a ratchety</h2>'
    '<p>Pásky jsou první, co se opotřebuje. Přední pásek se obvykle nosí přes nárt nebo přes špičku, zadní pevně drží patu a kotník. Ratchet, tedy ozubená přezka, umožňuje utáhnout pásek jedním pohybem, ale může zamrznout nebo se zanést sněhem. Kvalitnější modely mají přezky, které se dají ovládat v rukavicích a které se nezachytí na oděvu. Některé pásky mají polstrování, které rozloží tlak na nárt a snižuje riziko zatlačení. Pokud se pásek roztrhne, vyměňte ho za stejný typ, ne za univerzální.</p>'
    '<h2>Základna a tlumení</h2>'
    '<p>Základna neboli baseplate je podložka, na které stojí bota. Může být z plastu, kompozitu nebo hliníku. Plastová je levnější a lehčí, kompozitní nabízí lepší poměr tuhosti a hmotnosti, hliníková drží tvar i při velkém namáhání. Pod botou bývá také tlumicí vložka, která snižuje vibrace a nárazy na tvrdé podložce. Pro jezdce, kteří často skáčou, je dobré zkontrolovat velikost a materiál tlumení. Zajímavým příkladem jsou modely se zvýšenou základnou, které zlepšují přenos energie na hranu.</p>'
    '<h2>Skladování a doprava</h2>'
    '<p>Při cestě na hory nebo při přepravě po sezóně vázání zabalte tak, aby pásky nebyly zkroucené a základna se nedeformovala. Do tašky na desku je vhodné zabalit i šrouby a disky, aby se neztratily. Pokud snowboard vozíte na střeše auta, zkontrolujte, že vázání není vystaveno přímému slunci a mrazu po celou dobu cesty, protože plasty mohou zkřehnout. V létě skladujte vázání v suchu a při pokojové teplotě. Na vázání se také dá nasadit pěnový chránič, který zabraňuje poškrábání jiných věcí v tašce.</p>')

NEW['predtreninkove-boostery']['intro'] = NEW['predtreninkove-boostery']['intro'].replace(
    'Nejde o lék', 'Hodí se pro ty, kdo chtějí porovnat nabídku podle formy, příchutě a obsahu látek v jedné porci. Nejde o lék', 1)
NEW['predtreninkove-boostery']['guide'] += (
    '<h2>Jak porovnat dva produkty</h2>'
    '<p>Při srovnání dvou boosterů se vyplatí postupovat podle stejného postupu. Nejdřív zjistěte velikost porce a počet porcí v balení, pak vydělte cenu balení počtem porcí, nikoli hmotností. Poté porovnejte, které látky obsahují a v jakém množství. Dva produkty se stejným názvem formule mohou mít zcela odlišné složení. Nakonec zkontrolujte, zda jsou uvedené obsahy jednotlivých látek a zda výrobce zveřejňuje certifikace nebo testy kvality třetí stranou.</p>'
    '<ol><li>Velikost porce a počet porcí v balení.</li>'
    '<li>Obsah kofeinu a dalších stimulantů na jednu porci.</li>'
    '<li>Přehled ostatních látek a jejich množství.</li>'
    '<li>Typ sladidla a případná alergenní upozornění.</li>'
    '<li>Datum minimální trvanlivosti a způsob skladování.</li></ol>'
    '<h2>Boostery pro různé sporty</h2>'
    '<p>Silový trénink, kardio, crossfit i bojové sporty mají odlišné nároky a výrobci proto nabízejí odlišné formule. Pro silové disciplíny se hojně používají směsi s citrulinem a beta-alaninem, pro vytrvalostní sporty bývají vhodnější lehčí nápoje s elektrolyty a sacharidy. Je však důležité nehledat zázrak ve směsi: kdo trénuje několikrát týdně, získá víc z pravidelného spánku a pestré stravy než z jakéhokoli prášku. Jako obecný pomocník pro tělo slouží i <a href="/fitness-pomucky/">fitness pomůcky</a>.</p>'
    '<h2>Etika a pravidla sportu</h2>'
    '<p>Pokud soutěžíte, ověřte si pravidla své federace. Některé látky se mohou objevit na seznamu zakázaných látek a kontaminace doplňků se nedá vyloučit. Soutěžní sportovci by proto měli doplňky zvažovat velmi opatrně a vybírat jen produkty s testy třetí strany. Tato informace je obecná, přesné podmínky najdete u antidopingové organizace ve vaší zemi.</p>'
    '<h2>Běžné otázky při prvním nákupu</h2>'
    '<p>Nováčci se často ptají, zda booster pít každý den. Odpověď záleží na produktu a na doporučení výrobce, ale obvykle se doporučují přestávky a nepřekračování dávky. Další častá otázka se týká tolerance: tělo si na kofein zvyká a po čase vnímá menší efekt. Řešením není zvyšování dávky, ale pravidelné vynechávání a návrat ke kávě nebo čaji. Pokud se objeví nepříjemné příznaky, poraďte se s lékařem. Pro lepší představu si před nákupem přečtěte hodnocení v obchodě, ale mějte na paměti, že chuť i reakce těla jsou individuální.</p>')

NEW['jezdecke-obleceni']['guide'] += (
    '<h2>Co si vzít do stáje navíc</h2>'
    '<p>Kromě samotného oblečení se vyplatí mít ve stáji náhradní triko a suché ponožky, protože i dobrý trénink skončí promoknutým oblečením. Do tašky patří lehká bunda do deště, náhradní rukavice a gumička do vlasů, která se pod helmou nepromáčkne. Dlouhé vlasy je lepší stáhnout do culíku nebo copu, aby nelétaly do obličeje. Podrobnější přehled doplňků najdete v kategorii <a href="/jezdecke-doplnky/">jezdecké doplňky</a>, pro péči o koně slouží <a href="/vybaveni-pro-kone/">vybavení pro koně</a>. Pokud si chcete oblečení a výbavu uložit přehledně, hodí se <a href="/sportovni-tasky/">sportovní taška</a>.</p>')

NEW['snowboardova-vazani']['guide'] += (
    '<h2>Vázání a bota jako jeden celek</h2>'
    '<p>Nejpohodlnější je vybírat boty a vázání ve stejnou chvíli. Měkká bota potřebuje spíše střední vázání, tvrdá bota snese tužší základnu. Pokud boty používají zapínání Boa, zkontrolujte, jestli se pásky vázání netlačí na lanka a tlačítka. Při zkoušce v obchodě si stoupněte do vázání v botách, předkloňte se a ověřte, že pata zůstává dole. Tipy na boty najdete v kategorii <a href="/snowboardove-boty/">snowboardové boty</a>, informace o deskách v <a href="/snowboardy/">snowboardech</a>.</p>'
    '<p>Pokud na svahu často padáte, vedle vázání zvažte i chrániče zápěstí, kolen a zadku, které najdete ve <a href="/snowboardove-chranice/">snowboardových chráničích</a>. Díky nim se první dny na desce zvládnou s menším počtem modřin. Zimní den na hoře navíc vyžaduje teplé <a href="/lyzarske-rukavice/">rukavice</a> a <a href="/lyzarske-kalhoty/">kalhoty</a>, které se hodí i na snowboard.</p>')

NEW['predtreninkove-boostery']['guide'] += (
    '<h2>Jaké sporty a jaké typy tréninku boostery obvykle doprovázejí</h2>'
    '<p>Nejčastěji se boostery objevují v posilovnách, kde se trénuje se závažími, ale používají se i v bojových sportech, při kruhových trénincích a na skupinových lekcích. Každý sport má vlastní tempo: krátký silový trénink trvá hodinu, zatímco vytrvalostní výkon může trvat několik hodin, a proto se na dlouhé výkony hodí jiné doplňky než na krátké a intenzivní. Mnoho lidí si vystačí s vodou, jídlem a dobrým spánkem. Pokud o boosteru uvažujete, položte si otázku, co od něj čekáte, a zda to nezíská jednodušeji jinak.</p>'
    '<p>Vedle boosterů se v obchodech objevují i tyčinky, gely a nápoje pro vytrvalce, které nabízejí rychlé sacharidy. Rozdíl je v tom, že energetická tyčinka dodá hlavně kalorie, zatímco booster míří spíš na složky jako kofein nebo aminokyseliny. Rozhodnutí závisí na délce tréninku, na tom, kdy naposledy jedli, a na osobní toleranci. Podrobnosti o výživě během sportu najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>'
    '<h2>Jak předejít nepříjemnostem</h2>'
    '<ul><li>Nikdy nezačínejte novým boosterem před důležitým závodem nebo testem, vyzkoušejte ho nejdřív na běžném tréninku.</li>'
    '<li>Rozmíchejte prášek v dostatečném množství vody, aby se snížila koncentrace v žaludku.</li>'
    '<li>Nezapomeňte na jídlo, protože booster nenahradí energii z potravy.</li>'
    '<li>Při dlouhodobém užívání dělejte pauzy, aby se tělo nenaučilo spoléhat na stimulant.</li>'
    '<li>Při pochybnostech o složení se obraťte na výrobce nebo lékaře.</li></ul>')
