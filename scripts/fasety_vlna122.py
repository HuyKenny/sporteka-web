"""sporteka.cz — facet landing texts wave 122: panske-outdoorove-kalhoty, teplaky-tommy-hilfiger, damske-jizdni-kola, panske-rukavice.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ panske-outdoorove-kalhoty
NEW['panske-outdoorove-kalhoty'] = dict(
    title='Pánské outdoorové kalhoty: střih, materiál a velikost',
    desc='Pánské outdoorové kalhoty na túry, kolem stanu i do města. Jak vybrat střih, délku nohavic a materiál, čím se liší značky a kde porovnat nabídku.',
    intro='<p>Pánské outdoorové kalhoty se od dámských nebo unisex střihů liší hlavně v rozkroku, v pasu a v délce nohavic. Muži mají obvykle užší boky vůči pasu, delší nohy a jiné rozložení svalů na stehnech, takže střih počítá s hlubším rozkrokem, širším kolenem a rovnějším pasem. '
          'Tato stránka shrnuje pánské modely z kategorie <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, od lehkých letních kousků přes tvrdší kalhoty do skal až po zateplené modely na zimní túry. Najdete tu vysvětlení, jak vybrat velikost podle pasu a vnitřní délky nohavice, kdy je lepší pevná tkanina a kdy elastický softshell, a čím se liší severské a české značky. '
          'Pokud chcete také svrchní vrstvu, podívejte se na <a href="/softshellova-bunda-panska/">pánské softshellové bundy</a>. Dostupnost velikostí u jednotlivých obchodů porovnáte přímo v přehledu produktů.</p>',
    guide='<h2>V čem se pánský střih liší</h2>'
          '<p>Pánské outdoorové kalhoty mají rovnější linii pasu, širší stehna a více prostoru v sedu. Na rozdíl od dámských kalhot s tvarovaným bokem neleží na kyčlích, ale v přirozeném pasu, a opasek nebo pevný pás je proto zásadní pro udržení polohy. Kolena bývají předtvarovaná, aby se při zvedání nohy pod batohem látka nenapínala. '
          'Rozkrok je často vyztužený nebo opatřený klínem, který odstraňuje švy z místa, kde se nejvíc tře a namáhá. Důležité je také to, že pánské velikosti u outdoorových značek často udávají délku nohavice zvlášť, což mnoho dámských řad nedělá.</p>'
          + T(['Prvek', 'Pánská úprava', 'Co to znamená v praxi'], [
              ['Pas', 'rovnější, pevný, často s pásky na opasek', 'kalhoty drží i s těžším batohem a vybavením v kapsách'],
              ['Rozkrok', 'klín, méně švů', 'volnost při zvedání nohy na vysoký stupeň a při lezení'],
              ['Kolena', 'předtvarovaná, někdy dvojitá vrstva', 'méně vytahaná látka po delší túře'],
              ['Nohavice', 'delší, různé délky v řadě', 'nenajíždějí na boty ani při dřepu a předklonu'],
              ['Kapsy', 'prostorné, často na zip a v cargo střihu', 'mapa, telefon i rukavice na dosah ruky']]) +
          '<h2>Velikost: pas, vnitřní délka a jak číst značky</h2>'
          '<p>Většina outdoorových značek používá buď číselné velikosti odvozené od obvodu pasu, nebo písmena S až XXL. Skandinávské značky jako ' + B(('fjallraven', 'Fjällräven'), ('haglofs', 'Haglöfs'), ('lundhags', 'Lundhags')) + ' často uvádějí evropské číslo, například 48 nebo 52, které odpovídá kombinaci obvodu hrudníku a pasu. České a britské značky jako ' + B(('loap', 'Loap'), ('kilpi', 'Kilpi'), ('alpine-pro', 'Alpine Pro'), ('regatta', 'Regatta')) + ' bývají označovány písmeny a mají obvykle pohodlnější střih. '
          'Základem je proto vlastní měření a porovnání s tabulkou konkrétní značky.</p>'
          '<ul><li><strong>Pas:</strong> změřte v místě, kde kalhoty skutečně nosíte, ne nad kyčlemi.</li>'
          '<li><strong>Vnitřní délka nohavice:</strong> od rozkroku po kotník, ideálně v botách, které k nim budete obouvat.</li>'
          '<li><strong>Stehna a kolena:</strong> v dřepu nesmí látka zatahovat ani tlačit na kolenní čéšku.</li>'
          '<li><strong>Zimní varianta:</strong> počítejte s termoprádlem pod kalhotami, takže vybírejte spíše o půl velikosti volněji.</li>'
          '<li><strong>Lezecký sed:</strong> pokud používáte úvazek, vyzkoušejte, zda se pas nezařezává pod kyčelní pás.</li></ul>'
          '<p>Při nákupu na dálku mezi dvěma velikostmi zvolte větší, pokud jsou kalhoty z pevné tkaniny bez strečového podílu, a menší, když mají elastickou složku. U kalhot s pásky na opasek vždy ověřte, zda lze pas zúžit o několik centimetrů.</p>'
          '<h2>Materiál: pevná tkanina, softshell nebo lehký nylon</h2>'
          '<p>Rozdíly mezi materiály určují, kdy budou kalhoty nejlepší. Pevné tkaniny ze směsi bavlny a polyesteru, jaké mají na kalhotách například ' + B(('fjallraven', 'Fjällräven')) + ', jsou odolné vůči otěru, snesou větve a skálu a při péči se dají ošetřit voskem. Jsou však těžší, pomaleji schnou a v dešti nasáknou. '
          'Softshell nabízí pružnost, rychlé schnutí a lehkou ochranu před větrem a drobným deštěm, ale na ostré kameny je citlivější. Lehký nylon se skládá na minimum a hodí se na letní horské túry, u nichž jde hlavně o rychlé schnutí.</p>'
          + T(['Materiál', 'Silné stránky', 'Slabé stránky', 'Vhodné pro'], [
              ['Pevná tkanina (směs bavlny a polyesteru)', 'odolnost, kapsy, vzhled', 'váha, pomalé schnutí', 'trek se zátěží, kemping, práce venku'],
              ['Softshell', 'pružnost, větruodolnost', 'nižší odolnost vůči ostré hraně', 'všestranné túry od jara do podzimu'],
              ['Lehký nylon se stretchem', 'nízká váha, rychlé schnutí', 'tenký, méně teplý', 'letní hory, ferraty, běh do kopce'],
              ['Zateplený nebo fleecový', 'teplo bez přídavné vrstvy', 'objem, nutnost větrání', 'zimní chůze, sněžnice, fotografování']]) +
          '<p>Voděodolná úprava na povrchu pomáhá proti krátké přeháňce, ale nenahradí nepromokavé kalhoty. Pokud chodíte častěji do deště, přidejte do batohu skládací membránové kalhoty a základní kalhoty vybírejte podle prodyšnosti.</p>'
          '<h2>Kalhoty podle ročního období</h2>'
          '<p><strong>Léto.</strong> Hodí se lehké kalhoty z rychleschnoucí tkaniny, ideálně s odepínacími nohavicemi nebo možností vyhrnout je nad kolena. Větrání zajišťují zipy na stehnech, které je dobré mít po obou stranách. '
          '<strong>Jaro a podzim.</strong> Nejuniverzálnější jsou softshellové kalhoty střední tloušťky, které zvládnou rozdíl mezi chladným ránem a teplým odpolednem. <strong>Zima.</strong> Potřebujete zateplení, vyšší pas a spodní lem, který se zapíná kolem boty, aby dovnitř netáhl sníh.</p>'
          '<p>Chcete-li chodit celoročně, ušetří vám nákup jednoho lehkého a jednoho teplého páru víc než jedny kalhoty na všechno. Pro sjezdovky a freeride ale hledejte spíš <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>, které mají nepromokavou membránu.</p>'
          '<h2>Značky v nabídce a komu sedí</h2>'
          '<p>Nabídka pánských outdoorových kalhot je široká a každá značka má vlastní charakter. ' + B(('fjallraven', 'Fjällräven'), ('haglofs', 'Haglöfs'), ('lundhags', 'Lundhags')) + ' stojí na severské tradici: pevné tkaniny, dlouhá životnost a střih pro dlouhé túry se zátěží. '
          + B(('viking', 'Viking'), ('northfinder', 'Northfinder'), ('loap', 'Loap'), ('kilpi', 'Kilpi'), ('alpine-pro', 'Alpine Pro'), ('hannah', 'Hannah'), ('husky', 'Husky')) + ' jsou značky ze střední Evropy se střihem pro naše postavy a širokým výběrem pro běžné túry. '
          + B(('regatta', 'Regatta'), ('trespass', 'Trespass'), ('dare2b', 'Dare2b')) + ' nabízejí britský styl lehčích všestranných kalhot. ' + B(('columbia', 'Columbia'), ('the-north-face', 'The North Face')) + ' jsou americké značky se širokým záběrem od městských kalhot po horské. '
          + B(('dynafit', 'Dynafit')) + ' míří na skialpinismus a trail, ' + B(('helikon-tex', 'Helikon-Tex®')) + ' na taktické a bushcraft kalhoty s mnoha kapsami.</p>'
          '<h3>Který střih zvolit</h3>'
          '<ul><li><strong>Úzký (slim):</strong> sportovnější vzhled, vhodný pro lehčí postavy a rychlou chůzi.</li>'
          '<li><strong>Regular:</strong> nejuniverzálnější, dobře drží i s oblečením pod kalhotami.</li>'
          '<li><strong>Volný, cargo:</strong> pro kemping, práci venku a větší objem v kapsách.</li></ul>'
          '<h2>Na co se dívat před nákupem</h2>'
          '<ol><li>Zvolte účel: dlouhý trek, rychlá túra, skály, nebo městské nošení.</li>'
          '<li>Rozhodněte se pro materiál podle převažujícího počasí.</li>'
          '<li>Změřte pas a vnitřní délku a porovnejte s tabulkou značky.</li>'
          '<li>Zkontrolujte kapsy na zip, zesílení kolen a možnost zúžit pas.</li>'
          '<li>Ověřte, zda jsou nohavice dostatečně široké na trekové boty, třeba <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>.</li></ol>'
          '<h2>Jak pečovat o outdoorové kalhoty</h2>'
          '<p>Praní při doporučené teplotě, bez aviváže a s menším množstvím prášku prodlužuje život membrán i impregnace. Aviváž zalepí póry materiálu a snižuje prodyšnost. Pevné tkaniny je dobré občas vyklepat a nechat odvětrat, protože se nemusí prát po každé túře. Softshell vyžaduje jemný program a sušení na vzduchu. '
          'Po vyprání se obnovuje voděodolná úprava teplem nebo impregnačním sprejem. Dírku v koleně nebo roztřepený lem nohavice lze opravit žehlicí nášivkou. Při plánování větší túry se vyplatí podívat i na <a href="/trekove-hole/">trekové hole</a>, které odlehčí kolenům v klesání.</p>'
          '<h2>Pánské kalhoty a sousední výběry</h2>'
          '<p>Pokud hledáte spíše kalhoty na běh, kolo nebo do posilovny, prohlédněte si <a href="/sportovni-kalhoty/">sportovní kalhoty</a>. Pro blízké použití se hodí i <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a> a <a href="/panske-leginy/">pánské legíny</a>, které můžete nosit pod outdoorovými kalhotami jako první vrstvu. Pro ženy je k dispozici výběr <a href="/damske-sportovni-kalhoty/">dámských sportovních kalhot</a> a v kategorii outdoorových kalhot i dámské střihy.</p>',
    faq=[
        ('Čím se pánské outdoorové kalhoty liší od dámských?', 'Mají rovnější linii pasu, širší stehna a více prostoru v rozkroku. Dámské modely bývají tvarované v bocích a na kyčlích. Pánské řady navíc často nabízejí více délek nohavic, takže lépe sedí na vyšší postavy. Pro štíhlé muže ale může být pohodlnější dámský nebo unisex střih.'),
        ('Jak změřit velikost pánských outdoorových kalhot?', 'Změřte obvod pasu v místě, kde kalhoty nosíte, a vnitřní délku nohavice od rozkroku po kotník. Obě hodnoty porovnejte s tabulkou výrobce, protože označení S, M a L se mezi značkami liší. Kalhoty z pevné tkaniny bez strečového podílu vybírejte raději volnější.'),
        ('Jaký materiál je nejlepší na celoroční túry?', 'Nejuniverzálnější je softshell střední tloušťky s elastickou složkou, protože zvládá vítr, drobný déšť i chůzi do kopce. V létě se hodí lehčí nylon s rychlým schnutím, v zimě zateplený nebo fleecový model. Na těžký terén a práci venku je lepší pevná tkanina.'),
        ('Jsou outdoorové kalhoty nepromokavé?', 'Většina z nich má jen voděodolnou úpravu, která zvládne přeháňku a mokrou trávu, ne trvalý déšť. Nepromokavé jsou kalhoty s membránou a zalepenými švy. Pro jistotu mějte v batohu skládací membránové kalhoty a základní pár vybírejte podle prodyšnosti.'),
        ('Mám volit odepínací nohavice?', 'Hodí se na léto, hory s proměnlivým počasím a cesty, kde nechcete nosit druhý pár. Zipy ale mohou tlačit v koleni a zvyšují váhu. Pokud chodíte převážně v chladnějším počasí, jsou pohodlnější celistvé kalhoty bez zipů.'),
        ('Dají se outdoorové kalhoty nosit i do města?', 'Ano, především střihy v tmavých barvách a z pevné tkaniny, které vypadají podobně jako chino nebo cargo kalhoty. Praktické jsou kapsy na zip a rychlé schnutí. Pro kancelář nejsou ideální, na cesty, výlety a volný čas jsou skvělé.'),
        ('Jak často prát outdoorové kalhoty?', 'Pevné tkaniny stačí prát jen při znatelném znečištění a jinak vyvětrat. Softshell a lehké nylonové modely perte podle nošení, ideálně na jemný program bez aviváže. Příliš časté praní zbytečně zkracuje životnost impregnace a pružnost materiálu.'),
        ('Mohou kalhoty na zimní túry nahradit lyžařské kalhoty?', 'Na klidnou chůzi stačí zateplené outdoorové kalhoty, ale pro sjezd, snowboard nebo dlouhé sezení ve sněhu jsou vhodnější lyžařské s membránou. Mají vyšší odolnost vůči vodě, zesílené kotníky a gamaše, takže sníh neprosákne do bot.'),
        ('Kde pánské outdoorové kalhoty koupit výhodně?', 'Sporteka porovnává nabídku více českých a evropských obchodů na jednom místě. Podívejte se na dostupnost vaší velikosti a vnitřní délky, protože některé kombinace bývají skladem jen v několika obchodech. Na konci sezóny se objevují výprodeje starších kolekcí.'),
    ],
)

# ------------------------------------------------------------------ teplaky-tommy-hilfiger
NEW['teplaky-tommy-hilfiger'] = dict(
    title='Tepláky Tommy Hilfiger: pánské, dámské i dětské',
    desc='Tepláky Tommy Hilfiger z bavlny a směsi: pánské, dámské, dětské i kojenecké. Jak vybrat střih, velikost a materiál a kde porovnat nabídku obchodů.',
    intro='<p>Tommy Hilfiger je americká módní značka známá červeno-bílo-modrou vlajkou a námořnickým stylem, která do sportovního a volnočasového oblečení přenáší městský vzhled. Tepláky z této značky nejsou výkonnostní kus na maraton, ale pohodlné kalhoty na doma, do města, na cesty a na lehký pohyb. '
          'Najdete tu pánské, dámské, dětské a kojenecké modely, převážně z bavlny nebo bavlny s elastanem, s úpletem uvnitř nebo froté. Stránka vychází z kategorie <a href="/teplaky/">tepláky</a> a vysvětluje, čím se Tommy Hilfiger liší od sportovních značek jako Nike, Puma nebo Jordan, jak číst velikosti u dětí a jak o bavlněné tepláky pečovat, aby neztrácely tvar.</p>',
    guide='<h2>Co od teplákovin Tommy Hilfiger čekat</h2>'
          '<p>Značka Tommy Hilfiger vznikla v osmdesátých letech v USA a od začátku stavěla na prep stylu, tedy na čistém, sportovně elegantním vzhledu. V nabídce tepláků to znamená decentní nápis nebo malou vlajku, jednobarevné plochy a hladký střih. Sportovní značky vyhrávají na technologiích, Tommy Hilfiger na pohodlí a vzhledu: tepláky se dají nosit i mimo posilovnu, bez pocitu, že jdete v tréninkovém.</p>'
          '<p>V katalogu se opakují typy jako Essential Fleece Sweatpant, Essential Terry Sweatpant nebo jogger s manžetou u kotníku. Název napovídá materiál: fleece je počesaný, teplý a měkký zevnitř, terry je froté s drobnými poutky a lépe prodýchá. Kromě kalhot jsou k mání i teplákové šortky a dětské soupravy, takže si můžete sladit celý outfit.</p>'
          + T(['Typ', 'Materiál a charakter', 'Kdy se nosí'], [
              ['Fleece (počesaný úplet)', 'měkký, hřejivý, mírně objemný', 'podzim, zima, doma a na procházky'],
              ['Terry (froté)', 'lehčí, savější, prodyšnější', 'jaro, léto a chladnější večery'],
              ['Jogger s manžetou', 'zúžená nohavice, sportovnější silueta', 'město, cestování, kombinace s teniskami'],
              ['Rovná nohavice', 'volnější, klasický střih', 'doma, na odpočinek, k mikině'],
              ['Šortky', 'kratší délka, lehká tkanina', 'léto a dovolená']]) +
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p><strong>Pánské tepláky</strong> mají rovnější střih v pasu, volnější stehna a zúžení u kotníku. Barevně převládá černá, šedá a tmavě modrá. Dámské modely bývají kratší v nohavici a často mají jemnější barvy, například bílou nebo béžovou. U obou skupin je dobré sledovat obsah elastanu, který dává pohodlnější sed při sezení a pohybu.</p>'
          '<p><strong>Dětské a kojenecké tepláky</strong> mají měkčí úplet a často pružný pas se šňůrkou. U dětí značka obvykle uvádí velikost podle věku nebo výšky, u kojenců podle měsíců. Dítě se však může rychle vymykat průměru, proto se řiďte výškou v centimetrech a rezervou na růst, ne jen věkem.</p>'
          + T(['Výška dítěte', 'Přibližně věk', 'Poznámka'], [
              ['do cca 68 cm', 'kojenec, první měsíce', 'volíte podle měsíců a pohodlí v plence'],
              ['cca 80 až 92 cm', 'batole', 'hodí se pružný pas a nohavice s manžetou'],
              ['cca 98 až 116 cm', 'předškolák', 'nechte rezervu v délce na rok nošení'],
              ['cca 122 až 140 cm', 'mladší školák', 'výška je spolehlivější než věk'],
              ['cca 146 a výše', 'starší dítě a teenager', 'začíná se překrývat s dámskými a pánskými velikostmi']]) +
          '<p>Hodnoty jsou jen orientační. Tabulky značek se mírně liší, a pokud dítě stojí mezi dvěma velikostmi, vyberte větší, pokud má pas na gumu. Bavlna se při praní mírně srazí, proto se vyplatí dát přednost lehce delší nohavici.</p>'
          '<h2>Střih a velikost: na co si dát pozor</h2>'
          '<p>Módní značky často ušívají prostorněji, než jsou zvyklí zákazníci sportovních značek. Základem je proto změřit obvod pasu a boků, případně rozkrok, a porovnat s tabulkou. U pánských tepláků s úzkou nohavicí sledujte, zda se manžeta dostatečně roztáhne přes kotník a zda tkanina netlačí v lýtku. Nezapomeňte, že úplet je pružný a po vyprání se vrátí do tvaru jen částečně.</p>'
          '<ul><li><strong>Pas:</strong> guma se šňůrkou drží pas na místě, bez šňůrky se pas při nošení zvětší.</li>'
          '<li><strong>Délka:</strong> vnitřní délka by měla končit u kotníku, jogger může být kratší a odhalit botu.</li>'
          '<li><strong>Kapsy:</strong> boční kapsy bez zipu jsou pohodlné, zadní bývají jen dekorativní.</li>'
          '<li><strong>Nápis nebo logo:</strong> malý vyšitý znak je méně náchylný k ošoupání než nažehlený.</li>'
          '<li><strong>Barva:</strong> světlé tepláky jsou citlivé na špínu, tmavé na zbytky chmýří.</li></ul>'
          '<h2>Jak se liší od jiných značek tepláků</h2>'
          '<p>Chcete-li srovnat s klasickými sportovními značkami, otevřete si <a href="/nike-teplaky/">tepláky Nike</a>, <a href="/teplaky-puma/">tepláky Puma</a>, <a href="/jordan-teplaky/">tepláky Jordan</a> nebo <a href="/gymbeam-teplaky/">tepláky GymBeam</a>. Nike a Puma staví na sportovním původu, Jordan na basketbalovém stylu a GymBeam na fitness. Tommy Hilfiger je blíž módě, podobně jako ' + B(('calvin-klein', 'Calvin Klein'), ('lacoste', 'Lacoste'), ('guess', 'Guess'), ('armani-exchange', 'Armani Exchange')) + '.</p>'
          + T(['Přístup', 'Typické zaměření', 'Komu to sedí'], [
              ['Tommy Hilfiger', 'městský, prep, bavlna a froté', 'na každodenní nošení a cesty'],
              ['Sportovní značky', 'trénink, technické úpletové materiály', 'na sport a posilovnu'],
              ['Fitness značky', 'střih na pohyb, často elastické úpravy', 'na pravidelný trénink'],
              ['Módní značky', 'logo, střih a styl na prvním místě', 'do města a na cesty']]) +
          '<h2>Kombinace a styling</h2>'
          '<p>Pánské tepláky v tmavé barvě se hodí k bílým teniskám a jednoduché mikině, šedé k tmavému tričku. Pro sladěný look lze vybrat celou soupravu, kterou nabízí i dětská řada. Dámské tepláky se kombinují s crop topem, delším svetrem nebo oversize bundou. K teplákům se hodí <a href="/mikiny/">mikiny</a> a pro muže výběr <a href="/panska-mikina/">pánské mikiny</a>. Barevně nejbezpečnější je černá a šedá, protože odpustí drobné skvrny a lze ji nosit celoročně.</p>'
          '<h2>Péče o bavlněné tepláky</h2>'
          '<p>Praní na 30 až 40 stupňů obrácené naruby chrání potisk i vyšitý znak. Nepoužívejte horkou sušičku, protože bavlna se srazí a upletený pas ztratí pružnost. Úplet s počesanou vnitřní stranou se po čase zachumlá, proto jej perte odděleně od oděvů se zipy a suchým zipem. Sušte na vzduchu a žehlete na nižší stupeň.</p>'
          '<p>Chmýří z bavlny lze odstranit rolovacím kartáčem nebo strojkem na žmolky, ale s mírou, aby se neprodřel povrch. Dětské tepláky mají často zesílená kolena a při nošení se na nich objevují oděrky; záplata uvnitř nohavice jejich život podstatně prodlouží.</p>'
          '<h2>Kde porovnat a jak sledovat nabídku</h2>'
          '<p>Značky tohoto typu se prodávají ve více obchodech a velikostní řady se rychle vyprodávají. Porovnejte proto dostupnost v jednotlivých obchodech a nenechávejte nákup na poslední chvíli. Sezónní výprodeje bývají na konci zimy u fleecových modelů a na konci léta u lehčích kousků.</p>',
    faq=[
        ('Jsou tepláky Tommy Hilfiger sportovní, nebo módní?', 'Spíše módní, určené na každodenní nošení a volný čas. Mají čistý střih, malé logo a bavlněné materiály. Na intenzivní trénink jsou vhodnější tepláky sportovních značek s technickými úplety, které rychleji schnou a lépe odvádějí pot.'),
        ('Z jakého materiálu jsou tepláky Tommy Hilfiger?', 'Nejčastěji jde o bavlnu nebo bavlnu s příměsí elastanu či polyesteru. Fleece má počesanou vnitřní stranu pro teplo, terry je froté a lépe prodýchá. Konkrétní složení vždy najdete v popisu produktu u obchodu.'),
        ('Jak vybrat velikost pánských tepláků?', 'Změřte obvod pasu a boků a porovnejte s tabulkou značky. Pokud stojíte mezi dvěma velikostmi, vybírejte podle toho, zda chcete volný střih, nebo jogger s úzkou nohavicí. Bavlna se po praní mírně srazí, takže si nechte malou rezervu.'),
        ('Jaká je velikostní řada dětských tepláků?', 'U dětí se velikost obvykle uvádí podle věku nebo výšky, u kojenců podle měsíců. Spolehlivější je výška v centimetrech. Pokud je dítě mezi velikostmi, vyberte větší, hlavně pokud má pas na gumu s možností zúžení.'),
        ('Srazí se bavlněné tepláky při praní?', 'Mírně ano, hlavně při prvním praní a při horké sušičce. Perte je na 30 až 40 stupňů, obrácené naruby, a sušte na vzduchu. Zbytečně neriskujte kombinaci vysoké teploty a bubnové sušičky, která může změnit délku nohavic i velikost pasu.'),
        ('Čím se liší tepláky od joggerů?', 'Tepláky mají obvykle rovnější nohavici a volnější střih, jogger je zúžený a končí manžetou u kotníku. Jogger vypadá sportovněji a lépe se kombinuje s teniskami, rovné tepláky jsou pohodlnější doma a na odpočinek.'),
        ('Dají se Tommy Hilfiger tepláky nosit celoročně?', 'Fleece a hustší úplet se hodí na podzim a zimu, lehké froté na jaro a léto. V chladnějším počasí si pod ně můžete obléct legíny nebo termoprádlo, v létě zvolte teplákové šortky.'),
        ('Jak poznat originální zboží?', 'Kupujte v ověřených obchodech a hlídejte rozumné ceny, protože příliš nízká cena je varováním. Zkontrolujte kvalitu šití, vyšitý znak a štítky s velikostí a složením. Pokud si nejste jisti, zeptejte se obchodu na původ zboží.'),
        ('Mohu tepláky Tommy Hilfiger sladit s mikinou?', 'Ano, značka nabízí i soupravy a mikiny ve stejných barvách. Sladěný komplet dobře vypadá na cestách a při volném čase. Pokud chcete kombinovat různé značky, držte se jednobarevných kusů a stejné barevné škály, třeba šedá s černou.'),
    ],
)

# ------------------------------------------------------------------ damske-jizdni-kola
NEW['damske-jizdni-kola'] = dict(
    title='Dámské jízdní kola: rám, velikost a typ podle jízdy',
    desc='Dámská jízdní kola: městská, horská, silniční i elektrokola. Co je nízký nástup a co dámská geometrie, jak vybrat velikost rámu a kde porovnat nabídku.',
    intro='<p>Dámské kolo může znamenat dvě různé věci. Jednak kolo s nízkým nástupem, kterým se dá snadno projít bez zvedání nohy, a jednak kolo s geometrií upravenou pro ženské tělo: kratší horní trubkou, užším řídítkem a sedlem s širší zadní částí. Nízký nástup je otázka pohodlí při nasedání, ženská geometrie pak otázka dlouhodobého komfortu v sedle. '
          'Tato stránka shrnuje kola z kategorie <a href="/jizdni-kola/">jízdní kola</a> určená ženám, tedy městská, krosová, horská, silniční i elektrická. Průvodce vysvětluje, jak vybrat velikost rámu podle výšky a délky nohou, jaký typ zvolit pro dojíždění, výlety nebo sport a na čem při nákupu opravdu záleží. Dostupnost velikostí porovnáte u jednotlivých obchodů.</p>',
    guide='<h2>Nízký nástup versus ženská geometrie</h2>'
          '<p>Termín dámské kolo se v češtině používá volně. U městských kol znamená rám bez horní trubky, který se snadno přechází, a hodí se do sukně, při nošení tašek a pro starší cyklistky. Na horských a silničních kolech označuje dámský model rám s upravenou geometrií. Ta počítá s tím, že ženy mají v průměru kratší trup a delší nohy vůči výšce než muži. Rám je proto kratší, řídítka užší a sedlo širší v zadní části pro kosti pánve.</p>'
          + T(['Vlastnost', 'Nízký nástup', 'Ženská geometrie'], [
              ['Účel', 'snadné nasedání a sesedání', 'pohodlná poloha při delší jízdě'],
              ['Rám', 'průlezný, bez horní trubky', 'kratší horní trubka, jinak klasický tvar'],
              ['Řídítka', 'široká, vzpřímená', 'užší, přizpůsobená šířce ramen'],
              ['Sedlo', 'široké a měkké', 'tvarované pro sedací kosti'],
              ['Nejčastěji u', 'městských a trekingových kol', 'horských, silničních a gravelových kol']]) +
          '<p>Nízký nástup však nezaručuje lepší pohodlí. Rám bez horní trubky bývá o něco méně tuhý, a pokud chcete sportovní jízdu, je rozumnější zvolit klasický rám v menší velikosti nebo model s ženskou geometrií. Pro dojíždění po městě je ale nízký nástup velkým pomocníkem.</p>'
          '<h2>Jak vybrat velikost rámu</h2>'
          '<p>Velikost rámu se odvíjí od výšky postavy a délky nohou. Výrobci ji uvádějí v palcích nebo písmeny XS až L a v nabídce kol najdete často i doporučenou výšku jezdce v centimetrech. Údaje se u jednotlivých značek liší, proto se vždy řiďte tabulkou konkrétního modelu. Následující tabulka je jen orientační.</p>'
          + T(['Výška postavy', 'Přibližná velikost rámu', 'Označení'], [
              ['135 až 150 cm', 'cca 13 až 14 palců', 'XS'],
              ['150 až 165 cm', 'cca 15 až 16 palců', 'S'],
              ['165 až 175 cm', 'cca 17 až 18 palců', 'M'],
              ['175 až 185 cm', 'cca 19 až 20 palců', 'L']]) +
          '<ul><li><strong>Výška sedla:</strong> při šlápnutí na pedál v nejnižší poloze má být noha lehce pokrčená v kolenu.</li>'
          '<li><strong>Stand-over:</strong> u rámu s horní trubkou musí zůstat několik centimetrů mezi trubkou a rozkrokem.</li>'
          '<li><strong>Délka předloktí:</strong> řídítka nesmí být tak daleko, aby se vám napínala záda a ramena.</li>'
          '<li><strong>Zkušební jízda:</strong> pokud to jde, vyzkoušejte kolo před nákupem alespoň na krátkém úseku.</li>'
          '<li><strong>Kola 26, 27,5 a 28 palců:</strong> menší kola se hodí pro nižší postavy, větší jedou plynuleji po rovině.</li></ul>'
          '<h2>Typ kola podle způsobu jízdy</h2>'
          '<p><strong>Městské kolo</strong> je vzpřímené, s blatníky, nosičem a často s řetězovým krytem, aby sukně a kalhoty zůstaly čisté. V nabídce jsou kola od značek jako ' + B(('canellini', 'Canellini'), ('kellys', 'Kellys'), ('davi', 'Davi'), ('storm', 'Storm')) + '. Podrobnosti hledejte v kategorii <a href="/mestska-kola/">městská kola</a> a <a href="/trekingova-kola/">trekingová a městská kola</a>. '
          '<strong>Krosové kolo</strong> je kompromis mezi městem a lehkým terénem, s užšími plášti a bohatší převodovou řadou, viz <a href="/krosova-kola/">krosová kola</a>.</p>'
          '<p><strong>Horské kolo</strong> je určené pro lesní a polní cesty, s tlumičem vidlice a širšími plášti. Pro začátečnice stačí tuhá vidlice nebo jednodušší tlumič, pro náročnější trasy se hodí celoodpružené modely. Najdete je v kategorii <a href="/horska-kola/">horská kola</a>. <strong>Silniční a gravelová kola</strong> jsou lehká a rychlá, s nižší polohou těla; více v kategoriích <a href="/silnicni-a-gravel-kola/">silniční a gravel kola</a> a <a href="/silnicni-kola/">silniční kola</a>.</p>'
          + T(['Typ kola', 'Povrch', 'Poloha těla', 'Výhoda'], [
              ['Městské', 'asfalt, dlažba', 'vzpřímená', 'komfort, nosič, blatníky'],
              ['Krosové a trekingové', 'asfalt a zpevněné cesty', 'mírně předklonená', 'všestrannost, dobrý převod'],
              ['Horské', 'les, pole, kameny', 'sportovní', 'tlumení a záběr na hrubém povrchu'],
              ['Silniční a gravel', 'silnice, šotolina', 'sportovní, nízká', 'rychlost a nízká váha'],
              ['Elektrokolo', 'město i terén', 'podle typu', 'pomoc do kopce a na delší trase']]) +
          '<h2>Dámská elektrokola</h2>'
          '<p>Elektrokolo je dobrá volba pro dojíždění, jízdu s dětským sedátkem nebo trasy s kopci. U dámských modelů se často kombinuje nízký nástup s motorem uprostřed nebo v zadním kole a s baterií na rámu nebo nosiči. Mějte na paměti, že elektrokolo je podstatně těžší než běžné a musíte ho vynést po schodech nebo naložit do auta. Dojezd uváděný výrobci je odhad za ideálních podmínek, ve skutečnosti ho zkracuje kopcovitý terén, studené počasí a vyšší asistence.</p>'
          '<p>Podrobnější přehled najdete v kategorii <a href="/elektrokola/">elektrokola</a> a ve výběru <a href="/damska-elektrokola/">dámská elektrokola</a>. Elektrokola nabízejí například ' + B(('crussis', 'Crussis'), ('engwe', 'Engwe'), ('olpran', 'Olpran')) + '. Zvláštní kategorií jsou <a href="/skladaci-kola/">skládací kola</a>, praktická do paneláku nebo do vlaku.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Mezi dámskými koly najdete jak české značky, tak evropské. ' + B(('kellys', 'Kellys'), ('author', 'Author'), ('kross', 'Kross')) + ' nabízejí horská, krosová i městská kola. ' + B(('van-rysel', 'VAN Rysel')) + ' staví na silničních kolech, ' + B(('davi', 'Davi'), ('canellini', 'Canellini')) + ' na městských a dámských modelech. ' + B(('sava', 'Sava'), ('storm', 'Storm')) + ' jsou praktické volby pro každodenní jízdu.</p>'
          '<h2>Výbava, kterou nepodcenit</h2>'
          '<ul><li><a href="/cyklisticke-helmy/">Cyklistická helma</a> v dobré velikosti a se správně dotaženými popruhy.</li>'
          '<li><a href="/cyklo-svetla/">Světla</a> přední a zadní, i na krátké městské trasy.</li>'
          '<li><a href="/cyklo-zamky/">Zámek</a>, který kolo spolehlivě zajistí, ideálně s pevnou ocelovou smyčkou.</li>'
          '<li><a href="/cyklo-tasky-a-nosice/">Brašny, nosič a košík</a> na nákup a dojíždění.</li>'
          '<li><a href="/cyklisticke-dresy-damske/">Dámské dresy</a> a kraťasy s vložkou pro delší jízdu.</li></ul>'
          '<h2>Rady před nákupem</h2>'
          '<ol><li>Rozhodněte, kde budete jezdit nejčastěji, a podle toho vyberte typ kola.</li>'
          '<li>Změřte výšku postavy a porovnejte s tabulkou velikostí u modelu.</li>'
          '<li>Zkontrolujte převody, brzdy a materiál rámu. Hliník je lehký a odolný, ocel pružnější a lépe se opravuje.</li>'
          '<li>Ověřte, zda lze kolo doplnit nosičem, blatníky a světly.</li>'
          '<li>Zjistěte, kolik kolo váží, pokud ho budete nosit po schodech.</li></ol>'
          '<p>Chcete-li kolo pro dítě, podívejte se spíš na <a href="/detska-kola/">dětská kola</a> a jízdu na kole pro celou rodinu naplánujte s ohledem na velikosti všech členů.</p>',
    faq=[
        ('Co je dámské kolo?', 'Dámské kolo je buď kolo s nízkým nástupem, tedy rámem bez horní trubky, nebo kolo se ženskou geometrií s kratším rámem, užším řídítkem a širším sedlem. Městská kola jsou častěji dámská ve smyslu nízkého nástupu, horská a silniční spíše ve smyslu geometrie.'),
        ('Jaká velikost rámu mi bude sedět?', 'Řiďte se výškou postavy a délkou nohou podle tabulky u konkrétního modelu. Orientačně se pro výšku okolo 160 cm hodí velikost S kolem 16 palců, pro 170 cm velikost M kolem 18 palců. U různých značek se hodnoty mírně liší.'),
        ('Je lepší kolo s nízkým nástupem, nebo klasický rám?', 'Pro městské dojíždění, nošení tašek a jízdu v sukni je pohodlnější nízký nástup. Pro sportovní jízdu je klasický rám tužší a lehčí. Na horská a silniční kola se dámský střih obvykle řeší geometrií, nikoli nízkým nástupem.'),
        ('Jaké kolo zvolit do města?', 'Městské nebo trekingové kolo se vzpřímenou polohou, blatníky, nosičem a světly. Praktický je řetězový kryt a zámek na rám. Pokud se pohybujete v kopcovitém městě, zvažte elektrokolo.'),
        ('Má smysl kupovat dámské horské kolo?', 'Ano, pokud máte menší postavu nebo kratší trup. Ženská geometrie nabízí kratší reach, užší řídítka a sedlo pro širší pánev. Pro vyšší ženy není rozdíl tak patrný a stejně dobře poslouží unisex model ve správné velikosti.'),
        ('Jak velká kola vybrat, 26, 27,5 nebo 28 palců?', 'Menší kola, tedy 26 a 27,5 palců, se hodí pro nižší postavy a hornatější terén. Kola 28 palců jedou plynuleji po rovině a pohodlněji přejíždějí nerovnosti. U horských kol se dnes běžně používá i 29 palců, ale u malých rámů je lepší výběr menšího průměru.'),
        ('Na co si dát pozor u elektrokola?', 'Sledujte váhu kola, kapacitu baterie, polohu motoru a dostupnost servisu. Dojezd závisí na terénu, váze jezdce a nastavení asistence. Pokud elektrokolo nosíte po schodech, hledejte lehčí model nebo skládací řešení.'),
        ('Kolik převodů je dost?', 'Pro rovinaté město stačí tři až sedm převodů nebo nábojová převodovka. Na kopcovitou jízdu a terén volte víc převodů v kombinaci s širším rozsahem kazety. Podstatná je kvalita přehazovačky, ne jen počet rychlostí.'),
        ('Jak kolo správně seřídit?', 'Nastavte výšku sedla tak, aby noha při šlápnutí byla lehce pokrčená, a sklon sedla na vodorovnou polohu. Řídítka upravte tak, abyste neměla napnutá záda ani paže. Po několika stech kilometrech nechte zkontrolovat výplety a řetěz v servisu.'),
    ],
)

# ------------------------------------------------------------------ panske-rukavice
NEW['panske-rukavice'] = dict(
    title='Pánské rukavice: velikost, materiál a použití',
    desc='Pánské rukavice na zimu, lyže, kolo, běh i práci. Jak změřit velikost ruky, jaký materiál zvolit a čím se liší značky, a kde porovnat nabídku obchodů.',
    intro='<p>Pánské rukavice mají delší prsty, širší dlaň a větší obvod v kloubech než dámské. Střih počítá s větší rukou a silnějším zápěstím, takže muži v dámských rukavicích často cítí, že jim tlačí v kloubech, zatímco ženy v pánských mají prsty příliš dlouhé. '
          'Najdete tu rukavice určené mužům a chlapcům pro zimní chůzi, lyžování, jízdu na kole, běh, práci i outdoor. Stránka vychází z kategorie <a href="/sportovni-rukavice/">rukavice</a> a vysvětluje, jak změřit velikost ruky, kdy zvolit prstové a kdy palčáky, jak se liší materiály a jaké rukavice se hodí na jednotlivé sporty. Dostupnost velikostí porovnáte u více obchodů najednou.</p>',
    guide='<h2>Čím se pánská rukavice liší</h2>'
          '<p>Rozdíl není jen ve velikosti. Pánské rukavice mají delší prsty, širší dlaň, silnější zápěstí a často masivnější konstrukci. Dámské střihy mají užší dlaň a kratší prsty, někdy i jinak umístěné švy. Dětské rukavice jsou naopak úzké a krátké, ale často mají prodloužené manžety, aby chránily před sněhem.</p>'
          + T(['Prvek', 'Pánský střih', 'Co to znamená'], [
              ['Dlaň', 'širší, delší', 'odpovídá většímu obvodu v kloubech'],
              ['Prsty', 'delší, často s tvarovanými špičkami', 'lepší citlivost a držení'],
              ['Zápěstí', 'širší manžeta', 'dobře se obepíná přes rukáv bundy'],
              ['Zesílení', 'větší plochy na dlani a mezi palcem a ukazovákem', 'delší životnost při práci a lyžování'],
              ['Barvy', 'tmavé a tlumené odstíny', 'méně špinavé při práci a venku']]) +
          '<h2>Jak změřit velikost ruky</h2>'
          '<p>Základem je obvod dlaně těsně pod klouby, bez palce, změřený v centimetrech. Číslo se pak porovnává s tabulkou značky a převádí do označení S až XXL nebo do číselných velikostí od sedmi do dvanácti. U většiny mužů vychází obvod mezi dvaceti a třiadvaceti centimetry. Druhým údajem je délka ruky od zápěstí po špičku prostředníčku, která se hodí u kožených a lyžařských modelů s pevnými prsty.</p>'
          '<ul><li><strong>Měřte větší ruku:</strong> obvykle je silnější dominantní ruka.</li>'
          '<li><strong>Nezužujte ruku:</strong> příliš těsná rukavice omezuje prokrvení a v zimě studí.</li>'
          '<li><strong>Prostor na vzduch:</strong> u zimních modelů je malá vzduchová vrstva před prsty výhodou, ne chybou.</li>'
          '<li><strong>Palec:</strong> vyzkoušejte jeho pohyb, protože u levnějších střihů je často krátký.</li>'
          '<li><strong>Převod značek:</strong> malé rozdíly mezi tabulkami jsou běžné, proto nevolte slepě pořád stejné označení.</li></ul>'
          '<h2>Prstové rukavice, palčáky nebo kombinace</h2>'
          '<p>Prstové rukavice dávají nejlepší citlivost a chvat, ale jsou o něco chladnější. Palčáky drží prsty pohromadě, takže se vzájemně zahřívají, a v extrémních mrazech jsou bezkonkurenční, jen se s nimi hůř manipuluje. Existují i kombinované modely, kdy se přes tenké prstové rukavice natáhne palčák, nebo rukavice s odklápěcími konci prstů.</p>'
          + T(['Typ', 'Výhoda', 'Nevýhoda', 'Vhodné pro'], [
              ['Prstové', 'citlivost, práce s telefonem a nářadím', 'o něco chladnější', 'město, kolo, běh, práce'],
              ['Palčáky', 'teplo, jednoduchý střih', 'horší chvat', 'lyže, snowboard, extrémní mráz'],
              ['Kombinované', 'přizpůsobí se podmínkám', 'víc kusů v jednom', 'skialpinismus a dlouhé túry'],
              ['Podrukavice', 'tenká vrstva, citlivost', 'samy nezahřejí', 'pod lyžařské a zimní rukavice']]) +
          '<h2>Materiály a membrány</h2>'
          '<p>Kůže je odolná a časem se přizpůsobí ruce, ale hůř snáší mokro. Syntetické povrchy z polyesteru a nylonu schnou rychleji a jsou lehčí. Fleece hřeje a je levný, ale nehodí se do větru. Softshell chrání před větrem a drobným deštěm. Membrány zvyšují nepromokavost, ale snižují prodyšnost, a proto se hodí hlavně na lyže a na zimní túry. Vlna merino dobře reguluje teplotu a nezapáchá, hodí se jako podrukavice nebo na běh. Silikonové tečky na dlani zlepšují úchop, protože rukavice neklouže po řídítkách a hůlkách.</p>'
          '<p>Plocha na špičkách palce a ukazováku, která umožňuje obsluhovat dotykový displej, je dnes běžnou výbavou u řady modelů. Vedlejším efektem je však o něco nižší izolace těchto prstů, takže v hlubokých mrazech se vyplatí dotykové špičky vynechat.</p>'
          '<h2>Rukavice podle sportu a činnosti</h2>'
          '<p><strong>Lyžování a snowboard.</strong> Potřebujete nepromokavou membránu, prodloužený rukáv, zesílenou dlaň a ideálně popruh na zápěstí. Podrobný přehled je v kategorii <a href="/lyzarske-rukavice/">lyžařské rukavice a palčáky</a> a ve výběru <a href="/lyzarske-rukavice-panske/">pánské lyžařské rukavice</a>. Mezi značkami v nabídce jsou například ' + B(('rossignol', 'Rossignol'), ('reusch', 'Reusch'), ('viking', 'Viking'), ('picture', 'Picture')) + '.</p>'
          '<p><strong>Kolo.</strong> Cyklistické rukavice mají polstrování dlaně a kratší nebo delší prsty podle sezóny; hledejte je v kategorii <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>. V nabídce jsou značky jako ' + B(('silvini', 'Silvini'), ('craft', 'Craft')) + '. <strong>Běh a běžky.</strong> Tenké, lehké rukavice z elastického materiálu nebo merina, které nebrání pohybu. Značka ' + B(('swix', 'Swix')) + ' se zaměřuje na běžky a zimní sporty.</p>'
          '<p><strong>Práce a taktické využití.</strong> Kožené nebo syntetické rukavice se zesílenou dlaní a prsty, například od značek ' + B(('mechanix-wear', 'Mechanix Wear®'), ('mil-tec', 'Mil-tec®'), ('helikon-tex', 'Helikon-Tex®')) + '. Důležitá je přesnost střihu a citlivost špiček prstů. <strong>Box a brankáři.</strong> Pro tyto sporty existují specializované kategorie: <a href="/boxerske-rukavice/">boxerské rukavice</a> a <a href="/brankarske-rukavice/">brankářské rukavice</a>.</p>'
          '<h2>Značky v nabídce a komu sedí</h2>'
          '<p>' + B(('viking', 'Viking')) + ' je česká značka s velkým výběrem zimních a trekových rukavic. ' + B(('reusch', 'Reusch')) + ' se soustředí na lyžování a zimní sporty. ' + B(('under-armour', 'Under Armour'), ('nike', 'Nike'), ('adidas', 'Adidas')) + ' nabízejí sportovní a běžecké střihy s moderním vzhledem. ' + B(('columbia', 'Columbia'), ('the-north-face', 'The North Face'), ('loap', 'Loap'), ('hannah', 'Hannah')) + ' mají všestranné zimní rukavice pro město i hory. ' + B(('icebreaker', 'Icebreaker')) + ' staví na vlně merino, ' + B(('sealskinz', 'Sealskinz')) + ' na vodotěsných konstrukcích.</p>'
          '<h2>Kombinace s dalšími vrstvami</h2>'
          '<p>Rukavice nejsou jen doplněk, ale součást vrstvení. V mrazech se osvědčuje tenká podrukavice, přes ni zateplená rukavice a nad ní nepromokavý palčák. Rukáv bundy by měl přes manžetu rukavice zapadnout a nesmí ji nechat odkrytou. Na lyže a při chůzi po sněhu jsou vhodnější rukavice s dlouhou manžetou přes bundu, na kolo naopak krátká manžeta pod rukávem.</p>'
          '<p>Další zimní doplňky najdete také ve výběru pro ženy: <a href="/damske-rukavice/">dámské rukavice</a>. Pro děti jsou užitečné <a href="/reima-rukavice/">rukavice Reima</a> a <a href="/detske-lyzarske-rukavice/">dětské lyžařské rukavice</a>. A pokud preferujete výrazné barvy, hledejte i specifické výběry, například <a href="/u-zlate-rukavice/">rukavice ve zlaté barvě</a>.</p>'
          '<h2>Péče o rukavice</h2>'
          '<p>Praní se řídí materiálem: syntetické rukavice se perou na nízké teplotě, kožené se jen otírají vlhkým hadříkem a ošetřují krémem. Rukavice s membránou nepoužívejte s aviváží, která ucpává póry. Sušte při pokojové teplotě, nikdy na topení nebo v sušičce, protože kůže i lepené švy tvrdnou a praskají. Mokré rukavice vyndejte na vzduch s prsty otevřenými, aby se vnitřek vysušil celý.</p>'
          '<p>Rukavice se ztrácejí snadno, proto pomáhá malé očko nebo karabina pro spárování dvojice. Při dlouhodobém skladování je uchovávejte v suchu a bez přímého světla.</p>',
    faq=[
        ('Jak změřit velikost pánských rukavic?', 'Změřte obvod dlaně těsně pod klouby, bez palce, a porovnejte hodnotu s tabulkou značky. Mnoho mužů spadá do rozmezí dvaceti až třiadvaceti centimetrů. U kožených a lyžařských rukavic ověřte také délku ruky od zápěstí po špičku prostředníčku.'),
        ('Čím se pánské rukavice liší od dámských?', 'Mají širší dlaň, delší prsty a silnější zápěstí. Dámské střihy jsou užší a kratší. Ženám s větší rukou mohou vyhovovat pánské modely, mužům s menší rukou zase dámské nebo dětské ve větších velikostech.'),
        ('Jsou lepší prstové rukavice, nebo palčáky?', 'Prstové rukavice dávají víc citlivosti a jsou vhodné pro město, kolo a práci. Palčáky jsou teplejší, protože si prsty vzájemně předávají teplo, a hodí se do extrémních mrazů a na lyže. Mezi nimi stojí kombinované modely.'),
        ('Jaký materiál zvolit na zimu?', 'Na každodenní nošení stačí fleece nebo softshell s podšívkou, na lyže a vlhké počasí nepromokavá membrána. Merino je skvělé jako podrukavice, kůže je odolná, ale hůř snáší mokro.'),
        ('Fungují rukavice s dotykovými prsty i v mrazu?', 'Fungují, ale špičky prstů mají tenčí izolaci a v silném mrazu je cítit chlad dříve. V hlubokých mrazech proto raději volte palčáky nebo rukavice bez dotykových špiček a telefon obsluhujte přes podrukavici.'),
        ('Jak vybrat cyklistické rukavice?', 'Hledejte zesílení na dlani s polstrováním, prodyšný hřbet a pružnou manžetu. Pro léto jsou ideální rukavice s kratšími prsty, na jaro a podzim s delšími nebo membránové. Velikost volte tak, aby látka nevytvářela záhyby.'),
        ('Co udělat, když rukavice nesedí?', 'Zvažte tabulku jiné značky nebo model s jiným střihem. Úzká dlaň někdy znamená dámský nebo dětský model, široká naopak pánský nebo outdoorový střih. Rukavice se nejlépe zkouší s prsty zavřenými v pěst.'),
        ('Jak prát zimní a kožené rukavice?', 'Syntetické a membránové rukavice perte na nízké teplotě jemným prostředkem bez aviváže. Kožené otřete vlhkým hadříkem a ošetřete krémem na kůži. Sušte při pokojové teplotě, nikoli na radiátoru.'),
        ('Kde pánské rukavice koupit výhodně?', 'Sporteka porovnává nabídky více obchodů na jednom místě. Podívejte se na dostupnost vaší velikosti, protože střední velikosti se vyprodávají jako první. Výprodeje zimních rukavic bývají na konci sezóny a letních cyklistických rukavic na podzim.'),
    ],
)


# ------------------------------------------------------------------ doplnky
NEW['panske-outdoorove-kalhoty']['guide'] += (
    '<h2>Kapsy, zipy a detaily, které se v terénu projeví</h2>'
    '<p>Dobré outdoorové kalhoty poznáte podle drobností. Kapsa na stehně s ochranným zipem udrží telefon nebo mapu a nehoupe se při chůzi. Zip s větším tahátkem se snadno ovládá v rukavicích. '
    'Zesílení na kolenou a v sedu prodlouží životnost při klečení u ohně nebo na skále, a pokud se objeví možnost vložit kolenní chrániče, vyplatí se to hlavně při práci v terénu. Pásek na zúžení pasu pomůže, když kalhoty používáte celý rok a přibíráte či ubíráte vrstvy pod nimi.</p>')

NEW['teplaky-tommy-hilfiger']['intro'] = NEW['teplaky-tommy-hilfiger']['intro'].replace(
    'aby neztrácely tvar.</p>', 'aby neztrácely tvar. Na konci najdete odkazy na další značky a výběry, pokud se chcete rozhodnout podle střihu, nikoli podle loga.</p>')
NEW['teplaky-tommy-hilfiger']['guide'] += (
    '<h2>Pro koho se tyto tepláky hodí</h2>'
    '<p>Nejlépe pro lidi, kteří chtějí jedny kalhoty na doma, na cesty a do města a nehledají technické vlastnosti. Pro rodiče jsou praktické dětské soupravy a kojenecké modely, protože se snadno perou a bavlna je příjemná na citlivou kůži. Pro dospívající jsou zajímavé jogger střihy s malým logem, které se kombinují s teniskami. '
    'Naopak pro běh, posilovnu a delší trénink jsou vhodnější tepláky z technického úpletu, třeba z řad <a href="/panske-leginy/">pánských legín</a> nebo <a href="/sportovni-kalhoty/">sportovních kalhot</a>, které rychleji schnou.</p>'
    '<h2>Barvy a kombinace podle ročního období</h2>'
    '<p>Na podzim a v zimě se nejčastěji nosí tmavě modrá, šedá melanž a černá, protože hodí k vlněným svetrům a zimním bundám. Na jaře přicházejí světlejší odstíny, zelené a modré tóny s proužkem nebo kontrastním lemem. Pruh po straně nohavice vizuálně prodlužuje nohy, ale u kojeneckých a dětských tepláků je vhodnější bez dekorací, aby nic neškrábalo. '
    'K teplákům se hodí také černá mikina, například z výběru <a href="/cerna-mikina/">černé mikiny</a>, nebo mikina z řady <a href="/nike-mikina/">Nike</a>, pokud chcete kombinovat sportovnější styl s módním.</p>'
    '<h2>Časté chyby při nákupu</h2>'
    '<ul><li>Výběr podle loga bez ohledu na materiál: bavlna a směsi se chovají jinak než technický polyester.</li>'
    '<li>Nepřipočtená srážlivost: bavlněné tepláky se po prvním praní mírně zkrátí.</li>'
    '<li>Příliš těsný jogger: pas i manžeta se po nošení roztáhnou, ale stehna zůstávají těsná.</li>'
    '<li>Ignorování pasu u dětí: děti rostou do délky i do pasu a guma s možností zúžení ušetří koupi o velikost dříve.</li>'
    '<li>Nákup jen jednoho páru: tepláky se obvykle prostřídávají a při každodenním nošení se rychle opotřebují.</li></ul>')

NEW['damske-jizdni-kola']['guide'] += (
    '<h2>Sedlo, řídítka a pozice: co ženám často vadí</h2>'
    '<p>Nejčastější stížností bývá bolest sedacích kostí a otlaky. Ženská pánev je širší a sedlo by proto mělo mít širší zadní část a mírný prostřih nebo měkčí povrch. Výběr sedla je ale osobní a nelze jej odhadnout podle tabulky, proto se vyplatí kolo po týdnu jízdy dolaďovat. '
    'U horských a silničních kol hraje roli i šířka řídítek: příliš široká řídítka zatěžují ramena a krční páteř. Dobrá je šířka přibližně odpovídající šířce ramen. Pákové brzdy bývají nastavitelné na rozteč prstů, takže malá ruka na ně dosáhne bez natahování.</p>'
    '<h2>Údržba a servis</h2>'
    '<p>Před sezónou zkontrolujte tlak v pláštích, opotřebení brzdových destiček a stav řetězu. Řetěz se maže po každé mokré jízdě a po delší době se vyplatí jeho výměna spolu s kazetou, aby se zbytečně neopotřebovaly nové díly. Brzdová lanka a pláště vyměňujte podle stavu. Při koupi v e-shopu počítejte s tím, že kolo bývá dodáno částečně smontované, a základní seřízení brzd a přehazovaček je dobré svěřit servisu.</p>'
    '<h2>Kolo pro různé postavy a potřeby</h2>'
    '<p>Pokud jste nižší než 155 cm, hledejte kola s menším průměrem 26 nebo 27,5 palce a s krátkým představcem, aby řídítka nebyla příliš daleko. Pro vyšší ženy nad 175 cm může být lepší unisex nebo pánský rám, který nabídne delší trubky. Těhotenství a návrat po porodu přinášejí jiné priority, kdy se hodí vzpřímená poloha, nízký nástup a stabilita, a často i sedačka pro dítě.</p>')

NEW['panske-rukavice']['intro'] = NEW['panske-rukavice']['intro'].replace(
    'porovnáte u více obchodů najednou.</p>', 'porovnáte u více obchodů najednou, takže snadno najdete i méně běžné velikosti.</p>')
NEW['panske-rukavice']['guide'] += (
    '<h2>Časté chyby při výběru</h2>'
    '<ul><li>Nákup příliš těsné velikosti: prsty se tlačí na špičky a rukavice nehřeje, protože mezi vrstvami chybí vzduch.</li>'
    '<li>Jedna rukavice na všechno: lyžařská je moc hrubá na řízení auta, tenká běžecká nestačí na lyže.</li>'
    '<li>Ignorování manžety: krátká manžeta pod bundou nechává zápěstí odkryté a vlhké.</li>'
    '<li>Mokré rukavice bez sušení: vlhkost zabírá teplo a rychle se v nich objeví zápach.</li>'
    '<li>Žádná náhrada: pro zimu stojí za to mít dva páry a střídat je.</li></ul>'
    '<h2>Jak rozpoznat kvalitu</h2>'
    '<p>Kvalitní rukavice mají rovné a hustě šité švy bez vyčnívajících nití, pružný a dobře držící zápěstní pásek a dlaň s vyztužením v místech největšího namáhání. U zimních modelů se podívejte na podšívku: měkká a hustá vydrží víc než tenký lesklý materiál, který se brzy vyboulí. Palec by měl mít ohnutý tvar, aby se nemusel při sevření ruky vytahovat ze švu.</p>'
    '<h2>Zima, jaro a podzim</h2>'
    '<p>V mírných dnech na jaře a na podzim se osvědčují tenké softshellové nebo elastické rukavice, které chrání před větrem a neprohřívají ruku při chůzi. Zimní rukavice s membránou jsou výhodné pro dlouhé pobyty na sněhu, ale při normální chůzi po městě se v nich ruka potí. Nejlepší strategií je mít dvě až tři úrovně: tenkou, střední a hřejivou. K rukavicím se hodí i čepice a šál stejné barvy a materiálu, a pokud jezdíte na kole, pomůže chránit prsty před větrem i krátký návlek na rukáv.</p>')
