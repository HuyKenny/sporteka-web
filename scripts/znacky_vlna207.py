"""sporteka.cz — brand texts wave 207: gap, lotto, crocs, viking.
Only what follows from the live catalogue (categories, filters, product names); no history, prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ gap
NEW['gap'] = dict(
    title='Gap: trička, mikiny a tepláky pro celou rodinu',
    desc='Gap ve sporteka.cz: základní trička, mikiny, tepláky a kraťasy pro muže, ženy i děti. Jak vybrat řadu, velikost a kdy hledat zlevněné kousky.',
    intro='<p>Gap je v našem katalogu především značka každodenního oblečení. Neuvidíte tu technické membrány ani běžecké závodní vybavení, ale základní kousky, které se nosí do školy, do práce, na procházku i do posilovny: bavlněná trička, mikiny s logem, tepláky a kraťasy. Nejvíc zboží patří do kategorie <a href="/sportovni-tricka/">triček a tílek</a>, hned za ní následují <a href="/mikiny/">mikiny</a> a <a href="/teplaky/">tepláky</a>.</p>'
          '<p>Zvláštností je poměr kolekcí. Dětského zboží je tu víc než dámského a pánského dohromady, takže Gap funguje jako zdroj oblečení na celou rodinu, kde se dají vybrat podobné kousky pro rodiče i potomky. Tato stránka vysvětluje, jak se v nabídce orientovat podle řad v názvech produktů, jak volit velikost a střih, jak o oblečení pečovat a kdy má smysl sledovat slevy. Porovnáváme aktuální nabídky obchodů, takže uvidíte, kde je vybraný kus právě nejvýhodnější.</p>',
    guide='<h2>Co Gap v katalogu sporteky nabízí</h2>'
          '<p>Nabídka je zaměřená na pohodlné oblečení z měkkých materiálů. Převažují jednobarevná trička s drobným logem, mikiny s kapucí i bez ní, tepláky z úpletu a letní kraťasy. Doplňují je jarní a podzimní bundy, košile, sukně, šaty a legíny. Pro přehled tu máme rozložení hlavních kategorií, bez čísel, jen s pořadím podle významu.</p>'
          + T(['Kategorie', 'Typické použití', 'Pro koho se nejčastěji hodí'], [
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'každodenní nošení, spodní vrstva, domácí oblečení', 'děti, ženy i muži'],
              ['<a href="/mikiny/">Mikiny</a>', 'chladnější dny, škola, procházky', 'děti a muži, mikiny s logem i bez něj'],
              ['<a href="/teplaky/">Tepláky</a>', 'volný čas, cestování, domov', 'chlapci, děvčata, muži'],
              ['<a href="/sportovni-kratasy/">Kraťasy</a>', 'léto, hřiště, dovolená', 'chlapci a muži'],
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'městské nošení', 'děti i dospělí'],
              ['<a href="/sportovni-sukne-a-saty/">Sukně a šaty</a>', 'léto, škola, oslavy', 'dívky a ženy'],
              ['<a href="/leginy/">Legíny</a>', 'pod sukni, doma, na cvičení v lehčím tempu', 'dívky a ženy']]) +
          '<p>Gap tedy není specializovaný sportovní výrobce. Hodí se tam, kde chcete oblečení vhodné k pohybu, ale především k běžnému dni. Pro náročný výkon, jako je dlouhý běh v dešti nebo lyžování, hledejte spíš značky se sportovní specializací, například <a href="/znacka/nike/">Nike</a> nebo <a href="/znacka/adidas/">adidas</a>.</p>'
          '<h2>Pro koho: děti, ženy, muži</h2>'
          '<p>Podle filtru „pro koho“ jsou největší skupinou dětské kousky. Chlapecké a dívčí oblečení má v názvu velikosti ve stylu 4Y nebo 5Y, což odpovídá věku dítěte. Dámská a pánská nabídka je menší, ale pořád pokrývá všechny hlavní kategorie. Unisexových kusů je minimum, takže nečekejte univerzální střihy.</p>'
          '<ul><li><strong>Děti:</strong> trička, mikiny, tepláky a šortky v klasických barvách. Praktické jsou kusy, které se dají kombinovat mezi sourozenci.</li>'
          '<li><strong>Ženy:</strong> měkká trička, mikiny, tílka, sukně, šaty a legíny. U triček je k dispozici několik výstřihů a délek.</li>'
          '<li><strong>Muži:</strong> klasická trička s kulatým výstřihem, mikiny s velkým logem na hrudi a pohodlné tepláky.</li></ul>'
          '<h2>Jak číst názvy řad</h2>'
          '<p>V názvech produktů se opakují slova jako CLASSIC, HERITAGE, ARCHIVE LOGO, FLEECE, FRENCH TERRY nebo ORGANIC. Nejde o technické označení výkonu, ale o popis stylu nebo materiálu. Podle toho, co si vyberete, získáte jinou strukturu látky i vzhled.</p>'
          + T(['Označení v názvu', 'Co můžete čekat', 'Na co si dát pozor'], [
              ['CLASSIC', 'jednoduchý střih, malé logo, základní barvy', 'střih je spíše rovný, rozměr ověřte u konkrétní nabídky'],
              ['HERITAGE, ARCHIVE LOGO', 'výraznější logo nebo retro vzhled', 'velký potisk je u praní citlivý na teplotu'],
              ['FLEECE', 'hřejivý, na rubu chlupatější úplet', 'mikina je teplejší, na léto zbytečná'],
              ['FRENCH TERRY', 'hladký povrch zvenku, smyčky uvnitř', 'dobře drží tvar, ale dlouho schne'],
              ['ORGANIC', 'trička z bavlny označené jako organická', 'u dětí s citlivou pokožkou je to příjemné, údaje ověřte v popisu obchodu']]) +
          '<p>Přesné složení látky vždy ověřte v popisu na stránce obchodu, protože se mezi sezónami mění. Na sporteka.cz vidíte jen porovnání nabídek, samotný nákup se uzavírá v e-shopu.</p>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Základní trička a mikiny mají většinou uvolněnější, nenápadně rovný střih. Pro běžné nošení vybírejte svou obvyklou velikost. Pokud chcete trochu širší, takzvaně oversize vzhled, vezměte o stupeň větší. Pro výrazně přiléhavé nošení pod košili naopak o stupeň menší, ale jen u triček z čisté bavlny, protože ta se po praní mírně zkracuje.</p>'
          '<p>U dětí počítejte s růstem. Mikina nebo tepláky větší o jednu velikost vydrží jednu sezónu navíc, jenom nesmějí být tak velké, aby překážely při hře. Rukávy je možné podle potřeby jednou přehrnout. U triček a šortek se rezerva moc nevyplatí, protože sedí hůř a děti si je neoblíbí. Při nákupu přes internet změřte aktuální oblečení dítěte, které mu sedí, a porovnejte jeho rozměry s tabulkou obchodu.</p>'
          '<ol><li>Změřte oblečení, které vám dobře sedí, od podpaží k podpaží a od ramene k lemu.</li>'
          '<li>Porovnejte čísla s tabulkou v obchodě, ne jen s označením S, M nebo L.</li>'
          '<li>U bavlněných kusů přidejte malou rezervu na smrštění.</li>'
          '<li>Pro děti raději vybírejte širší střih v pase, který nesvírá a dá se dotáhnout šňůrkou.</li></ol>'
          '<h2>Trička a mikiny jako základ šatníku</h2>'
          '<p>Nejširší výběr najdete mezi tričky. Bílé a černé jsou nejčastější, doplňují je modrá, šedá a růžová. Takto omezená paleta je výhoda: kousky se snadno kombinují a rodinné oblečení se dá skládat k sobě. Pro druhou vrstvu při chladnějším počasí sáhněte po <a href="/mikiny/">mikině</a>. Na chladný den postačí fleece, na přechodné období zase mikina z francouzského froté. K ní se hodí <a href="/teplaky/">tepláky</a> stejné řady, takže vznikne celá souprava.</p>'
          '<p>Chcete-li něco konkrétnějšího, otevřete si výběr <a href="/gap-mikina/">mikin Gap</a>, kde jsou kousky z této značky seskupené podle typu a obchodu. Na tričkách a tílkách můžete porovnat výstřihy, rozdíl mezi kratším a delším střihem a to, zda je u konkrétního kusu potisk nebo jen drobná výšivka.</p>'
          '<h2>Péče o oblečení a životnost</h2>'
          '<p>Bavlněné oblečení vydrží mnoho let, když se pere šetrně. Platí několik jednoduchých zásad, které prodlouží život každému triku i mikině.</p>'
          '<ul><li>Perte při teplotě doporučené na štítku teplotu, obvykle třicet až čtyřicet stupňů.</li>'
          '<li>Potištěné kousky obraťte naruby, potisk tak méně praská.</li>'
          '<li>Mikiny a tepláky s fleecem nesušte při vysoké teplotě, úplet se může sbíhat a tvořit žmolky.</li>'
          '<li>Světlé a tmavé barvy perte zvlášť, bílá trička se jinak snadno zašedí.</li>'
          '<li>Dětské oblečení často skvrnami trpí víc, proto skvrny předpírejte hned po vzniku.</li></ul>'
          '<p>Žmolky vznikají třením u rukávů a v podpaží a nejsou vadou. Dají se odstranit speciálním holicím strojkem na textil. Pokud je naopak materiál prostřihnutý nebo se rozpárá šev po několika nošeních, uplatněte reklamaci v obchodě, kde jste nakupovali.</p>'
          '<h2>Jak se Gap liší od sportovních značek</h2>'
          '<p>Sportovní značky vyvíjejí látky pro odvod potu, rychlé schnutí a zvýšený pohyb. U Gapu je pohodlí postavené na měkkosti a vzhledu. To znamená, že bavlna příjemně hřeje, ale na intenzivní trénink se nehodí, protože ztěžkne a dlouho schne. Pro lehké cvičení, procházky nebo cestování je ale naprosto v pořádku. Pokud chcete oblečení opravdu do posilovny, podívejte se do <a href="/sportovni-tricka/">sportovních triček</a> od jiných značek nebo do kategorie <a href="/leginy/">legín</a>.</p>'
          '<p>Kdo chce celou rodinu oblékat podobně, Gap tento požadavek splní lépe než většina sportovních výrobců, protože dětské i dospělé řady mají stejné logo a barevnou paletu. Konkurencí v tomto segmentu jsou jiné volnočasové značky, třeba <a href="/znacka/champion/">Champion</a> nebo <a href="/znacka/fila/">Fila</a>.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zlevněné jsou nejčastěji kousky z uplynulé sezóny, protože e-shopy uvolňují sklad před příchodem nových barev. U triček je to nejčastěji na jaře po zimní sezóně, u mikin a tepláků zase na konci zimy. Celý rok jsou slevy na barvy a velikosti, které se prodávají hůř.</p>'
          '<ul><li>Hlídejte si méně obvyklé barvy a velikosti, bývají zlevněné jako první.</li>'
          '<li>Porovnávejte stejný kus ve více obchodech, rozdíly se mohou objevit i u základních triček.</li>'
          '<li>Počítejte s dopravou, u levného trika může být doprava významná část celkové částky.</li>'
          '<li>Při nákupu více kousků najednou se dopravě často vyhnete.</li></ul>'
          '<p>Na stránce každého produktu uvidíte, ve kterých obchodech je nabídka a jak se vyvíjí její cena. Rozhodnutí o koupi je pak snazší, protože víte, zda je daná nabídka běžná, nebo výjimečná.</p>',
    faq=[
        ('Je Gap sportovní značka?',
         'V katalogu sporteky je to hlavně značka volnočasového oblečení. Trička, mikiny a tepláky se hodí k pohybu v běžném dni, ale nejsou určené pro náročný výkon.'),
        ('Pro koho Gap v nabídce převažuje?',
         'Největší část nabídky tvoří dětské oblečení, po něm následuje dámské a pánské. Unisex kusů je minimum, takže střih se obvykle liší podle pohlaví.'),
        ('Jak poznám, jestli je mikina teplá?',
         'V názvu hledejte slovo FLEECE nebo údaj o materiálu v popisu. Francouzský froté je hladší a lehčí, fleece je na vnitřní straně chlupatější a hřeje víc.'),
        ('Co znamená označení 4Y nebo 5Y?',
         'U dětského oblečení udává velikost podle věku dítěte v letech. Přesné rozměry ale vždy porovnejte s tabulkou konkrétního obchodu.'),
        ('Srazí se bavlněná trička po praní?',
         'Čistá bavlna se mírně smrští, hlavně při prvním praní nebo při sušení v sušičce. Perte při doporučené teplotě a vybírejte raději volnější střih.'),
        ('Dá se Gap nosit na cvičení?',
         'Na lehké cvičení nebo domácí jógu ano. Na intenzivní trénink je lepší funkční materiál, který odvádí pot a rychle schne.'),
        ('Jak poznám výhodnou nabídku?',
         'Podívejte se na stránku produktu, kde jsou obchody seřazené podle ceny a vidíte vývoj nabídky. Výrazný rozdíl mezi obchody bývá u starších kolekcí.'),
        ('Mám brát dětskou mikinu větší?',
         'O jednu velikost větší je rozumný kompromis, vydrží déle. Větší než o jednu velikost už bývá nepraktické, protože se dítě v oblečení hůř pohybuje.'),
        ('Jak odstranit žmolky z mikiny?',
         'Použijte strojek na žmolky nebo jemný hřeben na textil a postupujte opatrně. Žmolky vznikají třením a nejsou vadou materiálu, další tvorbě zabrání šetrné praní.'),
    ])

# ------------------------------------------------------------------ lotto
NEW['lotto'] = dict(
    title='Lotto: tenisky, tenisová obuv a kopačky pro každého',
    desc='Lotto ve sporteka.cz: dětské i dospělé tenisky, tenisová obuv, kopačky, trička a doplňky. Jak vybrat obuv a velikost a kdy hledat zlevněné kousky.',
    intro='<p>Značka Lotto je v našem katalogu typická obuví. Zhruba polovinu nabídky tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, výrazná je i <a href="/tenisova-obuv/">tenisová obuv</a>, <a href="/kopacky/">kopačky</a> a zimní boty. Doplňují ji trička, kraťasy, polokošile a tepláky, takže se dá oblékat od hlavy k patě, i když obuv zůstává hlavním důvodem návštěvy.</p>'
          '<p>Zajímavé je, že největší skupinou jsou dětské modely a pánské kousky, dámy zůstávají těsně za nimi. Mezi produkty se objeví i dětská obuv na suchý zip a turistické sandály. Zvláštností katalogu je dokonce domácí fitness: najdete tu běžecký pás nebo rotoped. Tato stránka vysvětluje, jak se orientovat v modelech, jak vybrat správnou velikost a kdy má smysl hledat slevu.</p>',
    guide='<h2>Co Lotto nabízí v katalogu</h2>'
          '<p>Základem je obuv pro volný čas a sport. Ve výběru uvidíte dětské tenisky s názvy jako Whizzer, Dasher, Pacer nebo Kobalto, dámskou tenisovou obuv Mirage a boty Lunar. Pánská obuv zahrnuje městské tenisky i trekingové modely. Oblečení je spíše doplněk, ale s trička, kraťasy a polokošile dobře navazují na kopačky a tenisovou obuv.</p>'
          + T(['Kategorie', 'Co v ní najdete', 'Pro koho'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'každodenní boty, dětská sportovní obuv, modely na suchý zip', 'děti, muži, ženy'],
              ['<a href="/tenisova-obuv/">Tenisová obuv</a>', 'boty na antuku i tvrdý povrch, často v bílé barvě', 'ženy, muži, mládež'],
              ['<a href="/kopacky/">Kopačky</a>', 'obuv na fotbal pro trávu i pro umělé povrchy', 'hráči všech věkových skupin'],
              ['<a href="/zimni-obuv/">Zimní boty a sněhule</a>', 'teplejší boty na chladné dny', 'děti i dospělí'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'lehká obuv na léto a výlety', 'děti a ženy'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'oblečení na trénink a do školy', 'všichni'],
              ['<a href="/polokosile/">Polokošile</a>', 'tenisový a sportovně elegantní vzhled', 'muži a ženy']]) +
          '<p>Ve stránce značky proto sledujte hlavně obuv. Pokud hledáte komplexní oblečení na jeden sport, vybírejte oblečení z jiných kategorií a Lotto použijte pro boty. V oblasti běhu najdete víc modelů od značek jako <a href="/znacka/asics/">Asics</a> nebo <a href="/znacka/mizuno/">Mizuno</a>.</p>'
          '<h2>Dětská obuv: velikost, suchý zip a rychlý růst</h2>'
          '<p>Největší část nabídky je dětská. Rodiče tu najdou boty se šněrováním, gumičkami i suchým zipem, který se hodí pro mladší děti a také do školky. Dětská noha roste rychle, proto kontrolujte vnitřní délku stélky alespoň jednou za tři měsíce. Rezerva před špičkou má být zhruba prst, ale nesmí být tak velká, aby dítě v botě klouzalo.</p>'
          '<ul><li><strong>Měřte na stélce:</strong> vyndejte vložku z boty, postavte na ni dítě a zkontrolujte, kde končí palec.</li>'
          '<li><strong>Zvolte zapínání podle věku:</strong> suchý zip pro nejmenší, šněrování pro školáky, kteří už zvládnou uvázat tkaničky.</li>'
          '<li><strong>Zkoušejte odpoledne:</strong> noha je večer mírně větší než ráno.</li>'
          '<li><strong>Dvoje boty:</strong> střídání v týdnu prodlužuje životnost obuvi a nechá boty vyschnout.</li></ul>'
          '<p>Barevná paleta je u dětských modelů veselejší. Dívčí varianty bývají růžové a bílé, chlapecké modré a černé, ale kombinace se rozhodně dají střídat. Podívejte se na <a href="/znacka/skechers/">Skechers</a>, jestli chcete porovnat jiné dětské sportovní tenisky, a ceny hlídejte u obou značek.</p>'
          '<h2>Tenisová obuv: na co se zaměřit</h2>'
          '<p>Tenisová obuv musí zvládat rychlé boční pohyby, náhlé zastavení a sklouznutí. Proto má pevnější bočnice, širší patu a podešev s vytvarovaným vzorem. Modely s označením Mirage nebo Lunar v názvu patří právě sem. Pro hru na antuce se hodí podešev s hustým vzorem do ztracena, pro tvrdý povrch podešev odolnější proti otěru.</p>'
          + T(['Povrch', 'Co hledat v podešvi', 'Na co si dát pozor'], [
              ['Antuka', 'jemnější vzor, který se neucpává', 'tvrdá guma na antuce klouže jinak'],
              ['Tvrdý povrch', 'odolnější guma, vyztužená špička', 'rychleji se opotřebuje při smyku'],
              ['Hala', 'světlá nebo nešpinící podešev', 'mnoho hal přísně vyžaduje obuv, která nezanechává stopy'],
              ['Rekreační hra', 'univerzální podešev', 'pro časté hraní zvolte specializovanou obuv']]) +
          '<p>Pokud hrajete častěji než jednou týdně, má smysl pořídit boty speciálně pro tenis. V jednotlivých obchodech se ve výběru <a href="/tenisova-obuv/">tenisové obuvi</a> objevují modely na různé povrchy. Pro porovnání si prohlédněte i značky <a href="/znacka/babolat/">Babolat</a> nebo <a href="/znacka/head/">Head</a>, pokud jsou v katalogu k dispozici.</p>'
          '<h2>Kopačky Lotto</h2>'
          '<p>Kopačky tvoří menší, ale důležitou část nabídky. Při výběru nejdříve určete povrch, na kterém hrajete. Pro přírodní trávu jsou určeny kolíky, pro umělou trávu a tvrdé povrchy nižší hroty a pro halu hladká podešev. Špatně zvolený typ zvyšuje riziko uklouznutí a bolesti kolen.</p>'
          '<ul><li>Kolíky na přírodní trávu drží v měkkém terénu, ale na tvrdém povrchu se nepříjemně zabodávají.</li>'
          '<li>Nízké hroty na umělé trávě rozloží tlak a zmírní zátěž kloubů.</li>'
          '<li>Dětem vybírejte měkčí, lehčí kopačky, které nenutí k omezování pohybu.</li>'
          '<li>Boty vyzkoušejte se stejnou ponožkou, v jaké budete hrát.</li></ul>'
          '<p>Při dětském fotbale se vyplatí vyměňovat kopačky častěji než ostatní obuv, protože děti vyrostou za jednu sezónu. Ve výběru uvidíte i levnější modely, které jsou pro začátečníky v pořádku.</p>'
          '<h2>Velikost a střih obuvi</h2>'
          '<p>Základem je naměřit délku chodidla. Postavte se na papír, označte patu a špičku a změřte vzdálenost v milimetrech. K naměřenému číslu přidejte rezervu zhruba půl centimetru pro běžné nošení a víc pro dlouhé túry. Konkrétní tabulku pak porovnejte s údajem obchodu, protože se mezi modely liší.</p>'
          '<ol><li>Měřte obě chodidla, často je jedno o něco větší.</li>'
          '<li>Zkoušejte boty odpoledne, kdy je noha nejrozšířenější.</li>'
          '<li>Při zkoušce obuv zašněrujte a projděte se, patu nesmí sklouzávat.</li>'
          '<li>Palec se nesmí opírat o špičku, ale ani se v botě volně pohybovat.</li></ol>'
          '<p>Pokud mezi dvěma velikostmi váháte, vezměte ji o číslo větší u dětí a podle pocitu u dospělých. U tenisové obuvi a kopaček je lepší přesněji padnoucí velikost, protože volná bota zhoršuje stabilitu při pohybu.</p>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Z oblečení najdete trička, kraťasy, <a href="/polokosile/">polokošile</a>, mikiny a tepláky. Polokošile jsou typické pro tenis a golf, trička a kraťasy pro trénink a volný čas. Dámská nabídka zahrnuje i sukně, šaty a legíny. Pro konkrétní sport sledujte materiál: polyester a směsi s elastanem odvádějí pot lépe než čistá bavlna.</p>'
          '<p>Domácí fitness je zajímavý doplněk, který se u značky objevuje: běžecké pásy a rotopedy. Při koupi si ujasněte, kolik místa máte, jakou hmotnost zařízení unese a jak hlučné bude. Takovou věc nevyberete podle designu, ale podle parametrů a podle recenzí v obchodech.</p>'
          '<h2>Péče o obuv a životnost</h2>'
          '<p>Bota vydrží déle, když ji necháte vyschnout a nenosíte každý den. Po dešti vyndejte stélky a vycpěte boty papírem, nikdy je nesušte na topení, protože se lepené spoje uvolní a materiál ztvrdne. Špínu z textilních tenisek odstraňte kartáčkem a vlažnou vodou s mýdlem, kůži otřete vlhkým hadříkem a občas ošetřete impregnací.</p>'
          '<ul><li>Boty nepřipravujte do pračky, pokud to výslovně nedovoluje výrobce.</li>'
          '<li>Tkaničky perte zvlášť, vrátí botě čistý vzhled.</li>'
          '<li>Podešev kontrolujte, zda není nerovnoměrně sešlapaná, a boty včas vyměňte.</li>'
          '<li>Pro sport používejte sportovní obuv, ne tu nejhezčí do města.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Slevy bývají u obuvi dobře předvídatelné. Zimní boty jsou levnější na jaře, letní sandály na konci léta. Tenisky a kopačky mívají nižší ceny před novou sezónou a po ní, tedy při výprodeji starších řad. Hodí se sledovat několik obchodů, protože sklad se rozlišuje podle velikosti a nabídka se mění.</p>'
          '<ul><li>Pro dětské velikosti sledujte nabídku často, nejběžnější velikosti se rychle vyprodají.</li>'
          '<li>Porovnejte kus s podobnou obuví jiné značky, ať víte, jestli je sleva skutečná.</li>'
          '<li>Počítejte s poštovným a se vrácením zboží, pokud boty nesednou.</li></ul>'
          '<p>Na stránce produktu uvidíte všechny obchody a vývoj nabídky, takže si ověříte, zda se vyplatí koupit hned, nebo počkat.</p>',
    faq=[
        ('Jaká je hlavní kategorie značky Lotto?',
         'V katalogu převažují tenisky a volnočasové boty, hlavně dětské. Významné jsou také tenisová obuv, kopačky, zimní boty a sandály.'),
        ('Jak vybrat velikost dětské obuvi?',
         'Změřte stélku a ověřte rezervu zhruba na šířku prstu před špičkou. Chodidlo kontrolujte alespoň jednou za tři měsíce, protože děti rychle rostou.'),
        ('Hodí se suchý zip i pro starší děti?',
         'Ano, hodí se pro děti, které se potřebují rychle obout. Pro školáky bývá praktičtější šněrování, protože lépe drží kotník.'),
        ('Na jaký povrch je tenisová obuv?',
         'Záleží na modelu. Pro antuku je lepší jemnější vzor podešve, pro tvrdé povrchy odolnější guma. Popis obchodu obvykle povrch uvádí.'),
        ('Jaké kopačky zvolit pro děti?',
         'Vyberte podle povrchu hřiště a vybírejte lehčí, měkčí modely. Děti rychle rostou, proto se vyplatí rozumná cena a pravidelná kontrola velikosti.'),
        ('Prodává se u značky i jiné než sportovní zboží?',
         'Ve výběru se objevuje také domácí fitness, například běžecký pás nebo rotoped. Před koupí ověřte rozměry, nosnost a požadavky na místo.'),
        ('Jak sušit mokré boty?',
         'Vyndejte stélky, vycpěte boty papírem a nechte je schnout při pokojové teplotě. Topení a přímé slunce poškozují lepení i materiál.'),
        ('Kdy bývá obuv levnější?',
         'Zimní boty obvykle na jaře, letní modely na konci léta. Sledujte také výprodej starších řad před novou sezónou.'),
        ('Mám brát obuv o číslo větší?',
         'U dětí ano, jen s rozumnou rezervou. U dospělých a u tenisové obuvi či kopaček raději přesněji, aby bota při pohybu nesklouzávala.'),
    ])

# ------------------------------------------------------------------ crocs
NEW['crocs'] = dict(
    title='Crocs: pantofle, sandály a klapky pro děti i dospělé',
    desc='Crocs ve sporteka.cz: nazouváky, pantofle, sandály a holínky. Jak vybrat model, velikost a péči o obuv a kdy hledat zlevněné kousky.',
    intro='<p>Crocs je v našem katalogu skoro čistě obuvnická značka. Převahu mají <a href="/pantofle-a-zabky/">pantofle a žabky</a>, tedy nazouváky z lehkého materiálu s otvory, a po nich <a href="/sandaly/">sportovní sandály</a>. Doplňují je holínky, zimní boty a ojedinělé kousky z jiných oborů, například doplňky na pláž nebo plavecké pomůcky.</p>'
          '<p>Z hlediska zákazníků jsou nejpočetnější dámské varianty, následují pánské, dětské a unisex. Modely jsou známé nazouvacím tvarem, který se dá nosit k dovolené, do zahrady, na pláž i do každodenního provozu. Na této stránce vysvětlujeme, jak se orientovat v řadách s označením Classic, Clog, Crocband nebo Yukon Vista, jak vybrat velikost a jak boty udržovat. Přidáváme tipy, kdy hledat sníženou nabídku v obchodech.</p>',
    guide='<h2>Co Crocs v katalogu sporteky nabízí</h2>'
          '<p>Základem jsou pantofle ve stylu klasického nazouvacího „clogu“ s otvory na vrchu a s řemínkem kolem paty. Vedle nich najdete sandály s přezkami a řemínky, platformové varianty i obuv s kožíškem. Velmi úzká nabídka patří holínkám a kouskům na vodu. Přehled hlavních kategorií:</p>'
          + T(['Kategorie', 'Typický model', 'Použití'], [
              ['<a href="/pantofle-a-zabky/">Pantofle a žabky</a>', 'Classic Clog, Crocband, InMotion, Echo', 'volný čas, zahrada, bazén, cestování'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'Yukon Vista, Getaway Strappy, Baya', 'léto, procházky, dovolená'],
              ['<a href="/holinky/">Holínky</a>', 'nepromokavé kousky', 'déšť, zahrada, blátivé cesty'],
              ['<a href="/zimni-obuv/">Zimní boty a sněhule</a>', 'teplejší modely', 'chladné dny, krátké venčení'],
              ['<a href="/bazeny/">Bazény a nafukovadla</a>', 'doplňky k vodě', 'dovolená a hry'],
              ['<a href="/plavecke-pomucky/">Plavecké pomůcky</a>', 'malá nabídka', 'bazén, hra dětí']]) +
          '<p>Z toho plyne, že jde o značku, jejíž hlavní hodnota je jednoduchost: nazout, vyrazit. Pro delší pěší túry nebo běh nebude obuv s otevřenou patou vhodná. Pro takové potřeby sáhněte po <a href="/znacka/salomon/">Salomon</a> nebo <a href="/znacka/merrell/">Merrell</a>.</p>'
          '<h2>Jak rozumět názvům modelů</h2>'
          '<p>Názvy v katalogu vypadají nesourodě, ale skládají se z několika stále stejných slov. Znalost pár základních pojmů ušetří čas při hledání.</p>'
          + T(['Označení', 'Co obvykle znamená', 'Pro koho'], [
              ['CLASSIC CLOG', 'základní nazouvací tvar s otvory a řemínkem', 'všichni, nejuniverzálnější'],
              ['CROCBAND', 'varianta s pruhem na podešvi, sportovnější vzhled', 'muži, ženy, děti'],
              ['INMOTION', 'řada s důrazem na vnitřní tvar a pohodlí', 'celodenní nošení'],
              ['YUKON VISTA', 'sandály nebo klapky s řemínky', 'letní nošení, procházky'],
              ['PLATFORM', 'vyšší podešev', 'ženy, módní vzhled'],
              ['KID', 'dětská varianta', 'děti, mládež']]) +
          '<p>Slovo „Unisex“ v názvu znamená, že velikost je určená pro obě pohlaví a rozměry se řídí číselnou tabulkou. Pánské a dámské verze používají jiné číslování, proto vždy ověřte, v jaké škále je velikost uvedena.</p>'
          '<h2>Velikost: jak vybrat správnou</h2>'
          '<p>Nazouvací obuv potřebuje trochu jinou velikost než zavazovací. Chodidlo má mít rezervu, ale pata nesmí sklouzávat. Většina modelů má zadní řemínek, který přenese patu dopředu, a pak se bota chová jako pantofle. Při jízdě nebo chůzi po schodech se pak obuv drží lépe.</p>'
          '<ul><li>Změřte délku chodidla a porovnejte ji s tabulkou obchodu. Označení M a W se mohou lišit.</li>'
          '<li>Při váhání mezi velikostmi zvolte tu, v níž prsty nenarážejí na špičku.</li>'
          '<li>Pro děti raději volte přesnou velikost, příliš velká obuv se zachytává na schodech.</li>'
          '<li>Jsou-li boty určené k dlouhé chůzi, vyzkoušejte je v ponožkách.</li>'
          '<li>V létě nosí nohy více opuchlé, odpolední zkoušení je spolehlivější.</li></ul>'
          '<p>U unisex velikostí se doporučuje sledovat tabulku přepočtu. Dámy často využívají pánské číslo o dvě velikosti menší, ale přesné přepočty v popisu ověřte, protože se u modelů mohou lišit.</p>'
          '<h2>Pro koho: ženy, muži, děti</h2>'
          '<p>Nejvíc kousků je dámských, což se projevuje v široké nabídce barev od černé a béžové až po růžovou a fialovou. Pánské modely mají tmavší paletu: černá, šedá, khaki a modrá. Dětské nazouváky jsou veselé a často mají motivy, třeba pohádkové postavy. Pro rodinné dovolené jde o praktickou volbu, protože obuv zvládne vodu i písek.</p>'
          '<p>Rodiče by měli vědět, že dětská obuv musí mít pevný řemínek, a při hře na hřišti se hodí zavřená špička. U nejmenších zvažte, zda je pro ně nazouvací obuv vhodná pro celodenní nošení.</p>'
          '<h2>Pantofle, sandály nebo holínky</h2>'
          '<p>Základní rozhodnutí je, kde budete boty nosit. Pro bazén, sprchy a pláž jsou nejlepší pantofle, které schnou rychle a nenasákne vodou. Pro letní chůzi po městě a lehké výlety volte <a href="/sandaly/">sandály</a> s upínacím řemínkem. Pro déšť a zahradu jsou určeny <a href="/holinky/">holínky</a>, ve kterých se nemáte šanci zmáčet.</p>'
          '<p>Hodí se vám nabídka <a href="/crocs-holinky/">holínek Crocs</a>, pokud chcete porovnat ceny nepromokavé obuvi ve více obchodech. Zimní variantu najdete v kategorii <a href="/zimni-obuv/">zimních bot</a>, ale ta je v nabídce značky poměrně úzká.</p>'
          '<h2>Péče o obuv a životnost</h2>'
          '<p>Lehký materiál se snadno čistí, ale vyžaduje několik pravidel. Po koupání obuv opláchněte, nechte vyschnout ve stínu a nenechávejte v rozpáleném autě, kde se může deformovat.</p>'
          '<ul><li>Perte ručně vlažnou vodou a jemným mýdlem, kartáčkem odstraňte nečistoty z otvorů.</li>'
          '<li>Nesušte na topení ani na přímém slunci, tvar by se mohl změnit.</li>'
          '<li>Boty střídejte, pokud je nosíte celý den, vydrží déle.</li>'
          '<li>Při nošení po ostrém štěrku nebo v lese hlídejte opotřebení podešve.</li>'
          '<li>Skladujte volně, ne pod těžkými předměty.</li></ul>'
          '<p>Pokud na nohách vzniká otlak nebo pálení, vyměňte velikost nebo přidejte tenkou ponožku. Obuv bez zapínání nemá chodidlo stabilizovat tak jako šněrovací bota, proto na delší túry zvolte pevnější model.</p>'
          '<h2>Jak se Crocs liší od jiných značek obuvi na léto</h2>'
          '<p>Většina konkurentů v segmentu pantoflí používá kůži, korek nebo textil. Crocs je spojené s lehkou, tvarovanou podešví a nazouvacím střihem, ve kterém je obuv rychle hotová na cestu. Výhodou je rychlé schnutí a snadná údržba, nevýhodou menší stabilita na nerovném terénu. Pro porovnání se podívejte na <a href="/znacka/skechers/">Skechers</a>, který nabízí odlišný druh pohodlí, nebo na <a href="/znacka/adidas/">adidas</a> s klasickými pantoflemi na bazén.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Léto je sezóna největšího zájmu, proto bývá nabídka nejširší na jaře a nejvýhodnější na konci léta. Zimní kousky jsou levnější v dubnu a v květnu. Zlevněné bývají hlavně neobvyklé barvy a zbytky velikostí.</p>'
          '<ul><li>Porovnávejte více obchodů, jeden model se může v různých e-shopech výrazně lišit.</li>'
          '<li>Zkontrolujte, zda je v nabídce i dětská velikost, kterou potřebujete.</li>'
          '<li>Počítejte s dopravou, u jednoho páru obuvi může být její podíl značný.</li></ul>'
          '<p>Na stránce každého produktu vidíte nabídky obchodů a vývoj nabídky, takže poznáte, zda je právě vhodný čas koupit, nebo počkat.</p>',
    faq=[
        ('Pro koho je nabídka Crocs nejširší?',
         'Podle filtrů je nejvíc dámských modelů, po nich pánské a dětské. Unisex kusy tvoří menší část a řídí se společnou číselnou tabulkou.'),
        ('Jsou pantofle vhodné na dlouhou chůzi?',
         'Na krátké procházky ano, na dlouhé túry spíše ne. Otevřená pata a nízká stabilita jsou omezením, pro túry zvolte uzavřenou obuv.'),
        ('Jak poznám správnou velikost?',
         'Změřte délku chodidla a porovnejte ji s tabulkou obchodu. U nazouvací obuvi nesmí pata sklouzávat a špička nemá narážet na přední okraj.'),
        ('Co znamená Classic Clog?',
         'Je to základní nazouvací tvar s otvory na vrchu a s řemínkem kolem paty. Ostatní modely z něj vycházejí a doplňují ho o jiný vzhled nebo použití.'),
        ('Dají se Crocs nosit v bazénu?',
         'Pantofle se k vodě běžně používají, rychle schnou a snadno se čistí. Před vstupem do konkrétního zařízení si ověřte jeho pravidla.'),
        ('Jak pečovat o obuv?',
         'Perte ručně v mýdlové vodě, kartáčkem vyčistěte otvory a nechte je schnout ve stínu. Nesušte na topení ani v rozpáleném autě.'),
        ('Je ve výběru i obuv do deště?',
         'Ano, malá část nabídky patří do kategorie holínek. Pro porovnání cen využijte stránku s holínkami Crocs.'),
        ('Kdy bývá obuv Crocs levnější?',
         'Letní kousky na konci léta, zimní na jaře. Hlavně neobvyklé barvy a zbytky velikostí bývají zlevněné jako první.'),
        ('Je dětská obuv bezpečná na hřiště?',
         'Pro hru je lepší pevný řemínek na patě a zavřená špička. Příliš velká velikost se může zachytit na schodech nebo na prolézačkách.'),
    ])

# ------------------------------------------------------------------ viking
NEW['viking'] = dict(
    title='Viking: rukavice, termoprádlo a outdoorové oblečení',
    desc='Viking ve sporteka.cz: lyžařské rukavice a palčáky, termoprádlo, outdoorové kalhoty a bundy. Jak vybrat velikost a vrstvení a kdy hledat slevy.',
    intro='<p>Viking je v našem katalogu především značkou na zimní a horské aktivity. Největší kategorií jsou <a href="/sportovni-rukavice/">rukavice</a>, hlavně lyžařské a zimní, následuje <a href="/termopradlo/">funkční a termo prádlo</a>, <a href="/mikiny/">mikiny</a>, <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> a bundy. Doplňují je nákrčníky, kukly, merino prádlo a dokonce posilovací gumy.</p>'
          '<p>Zajímavostí je rozložení zákazníků. Dámské modely tu převažují nad pánskými a dětské tvoří významnou část, takže se dá oblékat celá rodina na hory. V názvech najdete označení jako Hudson GTX, Sherpa 2.0 nebo Expander, které naznačují řadu a použití. Tato stránka popisuje, jak vybrat rukavice, termoprádlo a kalhoty, jak vrstvit a jak o oblečení pečovat. Hodí se každému, kdo na hory jezdí a nechce platit víc, než musí.</p>',
    guide='<h2>Co Viking v katalogu nabízí</h2>'
          '<p>Nabídku lze rozdělit na tři bloky. První tvoří zimní doplňky: rukavice, palčáky, nákrčníky a kukly. Druhý blok je spodní prádlo ve formě setů a samostatných kusů, včetně merina. Třetí blok jsou svrchní vrstvy: fleecové mikiny, jarní a podzimní bundy, nepromokavé bundy a outdoorové kalhoty.</p>'
          + T(['Kategorie', 'K čemu slouží', 'Pro koho'], [
              ['<a href="/sportovni-rukavice/">Rukavice</a>', 'lyžování, zimní túry, chladné dny', 'ženy, muži, děti'],
              ['<a href="/termopradlo/">Funkční a termo prádlo</a>', 'spodní vrstva pod oblečení na hory', 'všichni, sety i samostatné kusy'],
              ['<a href="/merino-pradlo/">Merino prádlo a legíny</a>', 'dlouhé túry, zima, nízká zápachovost', 'ženy a muži'],
              ['<a href="/fleecove-mikiny/">Fleecové mikiny</a>', 'střední vrstva', 'ženy, muži, děti'],
              ['<a href="/outdoorove-kalhoty/">Outdoorové kalhoty</a>', 'túry, vycházky, lehká turistika', 'ženy a muži'],
              ['<a href="/nepromokave-bundy/">Nepromokavé bundy</a>', 'déšť a vítr', 'dospělí'],
              ['<a href="/nakrcniky-a-satky/">Nákrčníky a kukly</a>', 'ochrana krku a obličeje', 'všichni'],
              ['<a href="/posilovaci-gumy/">Posilovací gumy</a>', 'doplňkové cvičení', 'všichni']]) +
          '<p>Uvedená struktura odpovídá třívrstvému systému oblékání. Pot odvádí prádlo u těla, hřeje fleece uprostřed a vítr se zastavuje na povrchu bundy. Viking umožňuje poskládat všechny tři vrstvy ze stejné značky, ale hodí se i kombinovat s jinými výrobci, třeba <a href="/znacka/salomon/">Salomon</a> nebo <a href="/znacka/jack-wolfskin/">Jack Wolfskin</a>.</p>'
          '<h2>Lyžařské rukavice a palčáky: jak vybrat</h2>'
          '<p>Rukavice jsou nejpočetnější kategorie a zaslouží si nejvíc pozornosti. Dělí se na prstové a palčáky. Palčáky jsou teplejší, protože prsty hřejí společně, ale hůř se v nich uchopuje. Prstové rukavice dávají lepší cit, ale chladnou rychleji. Pro děti jsou praktičtější palčáky, které se snadněji obouvají a obecně zahřejí.</p>'
          + T(['Typ', 'Výhoda', 'Nevýhoda', 'Pro koho'], [
              ['Prstové rukavice', 'cit v prstech, snadné ovládání hůlek', 'rychleji chladnou', 'aktivní lyžaři, freeriding'],
              ['Palčáky (Mitten)', 'nejlepší tepelný komfort', 'horší jemná motorika', 'děti, mrzlé ruce, chladné dny'],
              ['S membránou GTX/Gore-Tex', 'nepromokavost při vlhkém sněhu', 'delší schnutí vnitřní vrstvy', 'celodenní pobyt venku'],
              ['Lehké zimní', 'univerzální pro město a procházky', 'na sjezdovku nestačí', 'každodenní nošení']]) +
          '<p>Při výběru velikosti změřte obvod dlaně těsně pod klouby, bez palce, a porovnejte ho s tabulkou obchodu. Označení jako 7 nebo 8 u dámských modelů vychází z tohoto číselného systému. Rukavice mají sedět, ale prsty se nesmí ve špičce opírat o konec. Příliš těsná rukavice omezuje prokrvení a ruce více mrznou.</p>'
          '<ul><li>Na sjezdovku volte prodloužený manžet přes rukáv bundy.</li>'
          '<li>Pro děti vybírejte modely s popruhem nebo šňůrkou, aby se neztrácely.</li>'
          '<li>Palčáky s členěním na dva prsty jsou kompromis mezi teplem a citem.</li>'
          '<li>Při vlhkém počasí zvolte membránovou variantu.</li></ul>'
          '<h2>Termoprádlo a merino</h2>'
          '<p>Spodní vrstva se nosí těsně na těle a odvádí pot do vnější vrstvy. Bavlna tuto roli nezvládá, proto jsou sety označené jako termoprádlo vyrobené z technických vláken, případně z merino vlny. Sety, například pánský Roni nebo dámský Hera, zahrnují tričko s dlouhým rukávem a kalhoty. Dětské sety, jako Riko, se hodí na zimní sporty a školní výlety.</p>'
          + T(['Materiál', 'Silné stránky', 'Slabé stránky'], [
              ['Syntetické vlákno', 'rychle schne, odolné při praní, příznivá cena', 'zápach se drží déle'],
              ['Merino vlna', 'hřeje i vlhká, méně zapáchá, příjemná na dotek', 'vyžaduje šetrnější praní'],
              ['Směs vlákna a merina', 'kompromis mezi trvanlivostí a příjemností', 'vlastnosti závisí na poměru složek']]) +
          '<p>Při výběru velikosti platí, že prádlo musí přiléhat, jinak neodvádí pot. Nemá ale tlačit nebo škrtit. Pro děti vybírejte raději volnější střih, který se dá nosit i při růstu. Více o správném výběru najdete v kategoriích <a href="/termopradlo/">termoprádla</a> a <a href="/merino-pradlo/">merino prádla</a>.</p>'
          '<h2>Outdoorové kalhoty a bundy</h2>'
          '<p>Kalhoty z řady Expander se v nabídce objevují v dámské i pánské verzi, včetně variant s označením Ultralight a šortek. Slouží k túrám, vycházkám i pracovnímu pohybu v přírodě. Materiál bývá strečový a rychleschnoucí, díky čemu nevadí zmáčení při krátkém dešti. Pro chladnější dny jsou určeny zateplené modely, pro léto lehčí.</p>'
          '<ul><li>Zkontrolujte délku nohavice, u kalhot do hor se nesmí zachytávat o boty.</li>'
          '<li>Zapínání na suchý zip nebo zip u kotníku usnadňuje obouvání.</li>'
          '<li>Kapsy na zip jsou praktické, nic z nich nevypadne.</li>'
          '<li>Pro dlouhé túry volte kalhoty se zesílením na kolenou.</li></ul>'
          '<p>U <a href="/nepromokave-bundy/">nepromokavých bund</a> a <a href="/sportovni-bundy-jaro-podzim/">jarních a podzimních bund</a> rozhoduje, kolik času strávíte venku v dešti. Do mrholení stačí lehká větrovka, na celodenní túru za deště je lepší membrána s přelepenými švy. Dostatečná je i kapuce, kterou lze stáhnout, aby nepropouštěla vodu. Podívejte se i na <a href="/holinky-viking/">holínky Viking</a>, pokud potřebujete obuv do deště.</p>'
          '<h2>Jak vrstvit na hory</h2>'
          '<p>Správné vrstvení je důležitější než jedno drahé oblečení. Pomáhá udržet teplo a zároveň zabránit zpocení. Doporučené pořadí je jednoduché.</p>'
          '<ol><li>Spodní vrstva z termoprádla nebo merina, přiléhavá a bez bavlny.</li>'
          '<li>Střední vrstva z <a href="/fleecove-mikiny/">fleecové mikiny</a>, která hřeje a prodyšně odvádí vlhkost.</li>'
          '<li>Svrchní vrstva z bundy, která chrání před větrem, sněhem a deštěm.</li>'
          '<li>Doplňky: rukavice, nákrčník nebo kukla a čepice.</li></ol>'
          '<p>Vždy mějte v batohu náhradní vrstvu. Při zastavení je potřeba rychle přidat, aby tělo nevychladlo. Při výstupu naopak vrstvu sundejte, abyste se nepotili.</p>'
          '<h2>Dětské a dámské oblečení</h2>'
          '<p>Jak ukazuje filtr, dámská nabídka je nejširší, což se projevuje v barevné paletě. Dětské modely jsou praktické a snadno se oblékají. Při nákupu dětských věcí hlídejte velikost podle výšky a počítejte s růstem. Dětské rukavice a palčáky mají často šňůrku, která zabrání ztrátě. U kalhot se vyplatí nastavitelný pas.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Technické oblečení vydrží mnoho sezón, pokud se správně pere a suší. Zásady jsou jednoduché a týkají se většiny kategorií.</p>'
          '<ul><li>Termoprádlo perte na doporučenou teplotu bez aviváže, která snižuje odvod vlhkosti.</li>'
          '<li>Rukavice s membránou sušte při pokojové teplotě, ne na topení.</li>'
          '<li>Merino perte šetrně a nesušte v sušičce.</li>'
          '<li>Bundy s membránou čas od času oživte praním a impregnací.</li>'
          '<li>Uložte všechno suché, aby se neobjevila plíseň.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní zboží je nejlevnější na jaře a na začátku léta, kdy obchody uvolňují sklad. Termoprádlo a rukavice se naopak dobře kupují hned po sezóně, protože nikdo nespěchá. Před sezónou, tedy na podzim, bývá nabídka nejširší, ale ceny nejvyšší.</p>'
          '<ul><li>Pro děti sledujte nabídku o jednu velikost větší, vydrží další sezónu.</li>'
          '<li>Porovnejte nabídky více obchodů, rozdíly bývají u rukavic překvapivě velké.</li>'
          '<li>Sety termoprádla bývají výhodnější než samostatné kusy.</li></ul>'
          '<p>Stránka každého produktu ukazuje obchody a vývoj nabídky, takže poznáte, zda je dobrá doba nakupovat.</p>',
    faq=[
        ('Co dělá Viking nejlépe podle nabídky katalogu?',
         'Největší část tvoří rukavice, hlavně lyžařské a zimní, po nich termoprádlo, mikiny a outdoorové kalhoty.'),
        ('Jaký je rozdíl mezi rukavicemi a palčáky?',
         'Palčáky jsou teplejší, ale hůř se v nich chytá. Rukavice s prsty dávají lepší cit, rychleji ale vychladnou. Pro děti jsou praktičtější palčáky.'),
        ('Co znamená GTX v názvu rukavic?',
         'Označuje model s membránou Gore-Tex, která má chránit před vodou. Přesnou specifikaci najdete v popisu obchodu.'),
        ('Jak vybrat velikost rukavic?',
         'Změřte obvod dlaně těsně pod klouby bez palce a porovnejte ho s tabulkou. Prsty se nesmějí opírat o špičku a rukavice nemá tlačit.'),
        ('Proč není vhodná bavlna jako spodní vrstva?',
         'Bavlna nasákne potem a pomalu schne, takže tělo prochladne. Pro spodní vrstvu volte technické vlákno nebo merino.'),
        ('Jak vrstvit na hory?',
         'Spodní vrstva z termoprádla, střední fleecová mikina a svrchní bunda, k tomu rukavice, nákrčník a čepice. Vždy s sebou noste náhradní vrstvu.'),
        ('Jsou v nabídce i dětské věci?',
         'Ano, tvoří významnou část, hlavně rukavice, palčáky, termoprádlo a mikiny. U dětí počítejte s růstem a vybírejte praktické zapínání.'),
        ('Jak prát termoprádlo?',
         'Perte na doporučenou teplotu bez aviváže a bez sušení při vysoké teplotě. Aviváž snižuje schopnost odvádět vlhkost.'),
        ('Kdy bývá zimní zboží levnější?',
         'Nejčastěji na jaře a na začátku léta, kdy obchody uvolňují sklad. Na podzim je nabídka nejširší, ale často dražší.'),
    ])


NEW['gap']['guide'] += (
    '<h2>Jak sestavit rodinný šatník z kousků Gap</h2>'
    '<p>Protože jsou dětské, dámské i pánské řady stavěné na podobné barvy, dá se z nabídky poskládat sladěný základ pro celou domácnost. Začněte třemi až čtyřmi kusy, které se kombinují se vším: bílé a černé tričko, šedá nebo tmavě modrá mikina a pohodlné tepláky. Teprve pak přidávejte barevnější kousky, například růžové nebo béžové tričko, které oživí jinak střídmou garderobu.</p>'
    '<ul><li><strong>Škola a školka:</strong> dvě až tři trička, jedna mikina a jedny tepláky vystačí na týden, když je perete průběžně.</li>'
    '<li><strong>Dovolená:</strong> kraťasy, tílka a lehké sukně nebo šaty zaberou v kufru málo místa a rychle se perou.</li>'
    '<li><strong>Domácí pohoda:</strong> mikina z měkkého úpletu a tepláky slouží i jako oblečení na spaní v chladnějších dnech.</li>'
    '<li><strong>Přechodná období:</strong> mikina pod <a href="/sportovni-bundy-jaro-podzim/">jarní či podzimní bundu</a> vytvoří vrstvu, kterou lze v případě tepla sundat.</li></ul>'
    '<p>Když si pro děti vyberete několik kusů stejné barvy, ušetříte ráno čas a snáz poskládáte oblečení po praní. Dospělým se hodí totéž, hlavně pokud hodně cestují s příručním zavazadlem.</p>'
    '<h2>Čepice, košile a ostatní doplňky</h2>'
    '<p>Mimo základní trojici najdete menší skupiny zboží, které se hodí k doplnění. Jsou to <a href="/cepice-a-celenky/">čepice, kšiltovky a čelenky</a> s logem, které přidají vzhled, a lehčí <a href="/kosile/">košile</a> z látek vhodných na jarní a letní vycházky. V kategorii <a href="/tilka/">tílek a topů</a> uvidíte kousky, které se dobře nosí samostatně v létě i jako vrstva pod mikinu. Tyto skupiny jsou menší, takže výběr barev a velikostí se může rychleji vyprodat a vyplatí se proto sledovat je častěji.</p>'
)
NEW['gap']['faq'] += [
    ('Jak poznám, který kus je letní a který zimní?',
     'Řiďte se materiálem a typem oblečení. Tílka, kraťasy a lehká trička jsou letní, fleecové mikiny a tepláky s hřejivou vnitřní stranou patří do chladu.'),
]

NEW['lotto']['guide'] += (
    '<h2>Jak Lotto vybírat v rodině</h2>'
    '<p>Značka pokrývá děti, muže i ženy, a proto se dá pořídit celá sada pro rodinu. Pro dospělé je nejčastější volba každodenní tenisky v černé nebo bílé barvě, které jdou do kanceláře i na procházku. Děti často potřebují troje boty: do školy, na tělocvik a na hřiště. Vyplatí se to, protože každý druh obuvi dělá jinou práci a jinak se opotřebovává.</p>'
    '<ul><li><strong>Škola:</strong> lehká bota s pevnou patou, která se snadno obouvá.</li>'
    '<li><strong>Tělocvik:</strong> světlá podešev, která nezanechává stopy v hale.</li>'
    '<li><strong>Venkovní hry:</strong> robustnější bota s hrubším vzorem podešve.</li>'
    '<li><strong>Léto:</strong> <a href="/sandaly/">sportovní sandály</a> s upínáním kolem paty, ve kterých dítě zvládne i výlet.</li></ul>'
    '<h2>Oblečení z kategorií tepláky, mikiny a legíny</h2>'
    '<p>Doplňkové oblečení je užitečné tam, kde chcete mít sladěný celek. <a href="/teplaky/">Tepláky</a> a <a href="/mikiny/">mikiny</a> se hodí na zahřátí před tréninkem a po něm, <a href="/leginy/">legíny</a> zase pro ženy, které cvičí nebo hrají tenis v chladnějším počasí. U dětí jde o praktický doplněk k obuvi, který se dá používat i ve škole.</p>'
    '<p>Při výběru dbejte na materiál. Polyester a směsi s elastanem se hodí do tělocvičny, bavlna je příjemnější na doma. Velikost vybírejte podle výšky, u kraťasů a sukní podle obvodu pasu.</p>'
    '<h2>Jak číst názvy modelů</h2>'
    '<p>Název produktu ve výpisu obvykle obsahuje jméno modelu, kategorii a barvu, například dětská sportovní obuv Whizzer, dámská tenisová obuv Mirage 300 nebo pánská trekingová obuv. Označení za názvem modelu, jako K, W nebo M, bývá zkratkou pro cílovou skupinu: děti, ženy nebo muže. Římská číslice v názvu, například III, ukazuje na novější generaci modelu. Starší generace bývají v obchodech levnější, jen je potřeba ověřit, že je k dispozici vaše velikost.</p>'
)
NEW['lotto']['faq'] += [
    ('Co znamená písmeno K, W nebo M v názvu modelu?',
     'Bývá to zkratka cílové skupiny: K pro děti, W pro ženy a M pro muže. Spolehlivější je však údaj o určení v popisu konkrétního obchodu.'),
]

NEW['crocs']['guide'] += (
    '<h2>Zahrada, bazén a dovolená: kde se Crocs osvědčí</h2>'
    '<p>Hlavní devízou nazouvací obuvi je rychlost. Na zahradě ji nazujete za pár vteřin, na terase ji bez zavazování svlečete a u bazénu ji bez obav namočíte. Při cestování zabírá málo místa v kufru a po zmáčení rychle schne. Pro děti jde o praktický kousek na prázdniny, protože si ji obují samy.</p>'
    '<ul><li><strong>Zahrada:</strong> pantofle snadno opláchnete hadicí, bahno se z podešve odstraní bez námahy.</li>'
    '<li><strong>Bazén a pláž:</strong> hladká podešev nenasákne, ale na mokrém dlaždičkovém povrchu buďte opatrní, zejména u hladkých modelů.</li>'
    '<li><strong>Dovolená:</strong> sandály s řemínky zvládnou procházku po městě a lehký výlet, zatímco pantofle patří spíš k ubytování a pláži.</li>'
    '<li><strong>Práce:</strong> někdo je nosí v kuchyni, ve zdravotnictví nebo ve službách, kde je důležité pohodlí při dlouhém stání. Ověřte si pravidla zaměstnavatele.</li></ul>'
    '<h2>Příslušenství, kupování pro děti a malé kousky z jiných oborů</h2>'
    '<p>Kromě obuvi se v katalogu objeví i drobnosti z jiných kategorií: <a href="/obuv-do-vody/">boty do vody</a>, <a href="/kajaky-a-cluny/">kajaky a čluny</a> nebo <a href="/plazove-doplnky/">plážové doplňky a osušky</a>. Jsou to ojedinělé nabídky, které se objevují podle aktuální nabídky obchodů, a proto na ně nespoléhejte jako na stálý sortiment. Pro výběr vodních bot je vhodnější podívat se i na jiné značky, které se na tuto oblast specializují.</p>'
    '<p>Kupujete-li obuv pro dítě, počítejte s tím, že dětská noha je širší a kratší než dospělá, a vyberte model přímo dětský. Zkontrolujte pevné zapnutí paty, aby se dítě nemohlo při běhu vyzout. Dětské verze často nabízejí ozdobné doplňky, které se dají přidat nebo odebrat. Dbejte na to, aby z nich nic nevyčnívalo a nehrozilo zachycení.</p>'
    '<h2>Barvy a kombinace</h2>'
    '<p>Podle filtru barev převažují černá a béžová, následuje bílá, modrá, růžová a hnědá. Tmavé a neutrální modely se dobře kombinují s oblečením a jsou praktické, protože se na nich nepoznají drobné skvrny. Světlé barvy ukazují každou špínu, ale u pláže a léta vypadají svěže. Výraznější a pastelové varianty jsou určené spíš dětem a ženám, které chtějí boty k určitému outfitu.</p>'
    '<ul><li>Černá se hodí na cesty, do práce a k tmavému oblečení.</li>'
    '<li>Béžová a hnědá působí přirozeně a pasuje k letním barvám.</li>'
    '<li>Bílá je svěží, ale vyžaduje častější čištění.</li>'
    '<li>Barevné kousky jsou ideální pro děti, které si je snadno najdou v šatně.</li></ul>'
)
NEW['crocs']['faq'] += [
    ('Jakou barvu zvolit, aby boty nebyly poznat od špíny?',
     'Nejpraktičtější jsou černá, tmavě šedá a hnědá. Světlé a bílé modely ukazují každou skvrnu a vyžadují častější čištění.'),
]

NEW['viking']['guide'] += (
    '<h2>Příklady použití: lyžování, túry a město</h2>'
    '<p>Podle toho, kam se chystáte, se mění důraz u jednotlivých kousků. Na sjezdovce rozhodují rukavice s dlouhým manžetem, nepromokavé kalhoty a teplá střední vrstva. Na zimní túře je důležitější prodyšnost a nízká váha. V městském provozu stačí lehčí oblečení, které se nepoznáte od běžného, ale hřeje a nepromokne.</p>'
    + T(['Aktivita', 'Co vybrat', 'Na co si dát pozor'], [
        ['Sjezdové lyžování', 'prstové rukavice nebo palčáky s membránou, termoprádlo, bunda', 'dlouhý manžet přes rukáv, přiléhavá spodní vrstva'],
        ['Zimní túra', 'fleecová mikina, merino prádlo, lehčí rukavice', 'prodyšnost, protože se při výstupu hodně potíte'],
        ['Letní a podzimní túra', '<a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, jarní bunda, tričko', 'rychlé schnutí, kapsy na zip'],
        ['Procházka městem v zimě', 'nákrčník, lehčí rukavice, mikina', 'nenosit zbytečně hrubé vrstvy'],
        ['Domácí cvičení', '<a href="/posilovaci-gumy/">posilovací gumy</a>, sportovní spodní prádlo, tričko', 'odpor gumy volte podle cvičení, ne podle vzhledu']]) +
    '<p>Takto rozložené oblečení vám dovolí používat stejné kousky v několika situacích. Spodní prádlo například poslouží na lyžích, na túře i na zimní procházce, zatímco rukavice se dají využít na sjezdovce i na sáňkování s dětmi.</p>'
    '<h2>Sportovní spodní prádlo a doplňky</h2>'
    '<p>Mimo termoprádlo najdete i <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a> a <a href="/sportovni-tricka/">trička</a>, která se nosí na trénink nebo jako spodní vrstva v mírnějším počasí. Pro krk a obličej slouží <a href="/nakrcniky-a-satky/">nákrčníky a kukly</a>. Jsou lehké, zabírají málo místa v kapse a chrání proti větru. Nákrčník lze nosit také jako čelenku nebo čepici, takže se vyplatí mít jeden v každém batohu. Z <a href="/posilovaci-gumy/">posilovacích gum</a> si můžete sestavit sadu pro domácí cvičení, kterou ocení každý, kdo v zimě nechce chodit do posilovny.</p>'
    '<h2>Jak číst názvy v katalogu</h2>'
    '<p>Mezi produkty se objevují názvy v češtině i v polštině, což vychází z podoby, v jaké je obchody uvádějí. Označení Man, Lady nebo Kids ukazuje cílovou skupinu, Set znamená komplet prádla z horní a spodní části, Mitten palčák a Ski rukavici určenou na sjezdovku. Pokud u produktu nenajdete potřebnou informaci, ověřte ji v popisu obchodu před koupí, zejména u materiálu a membrány.</p>'
)
NEW['viking']['faq'] += [
    ('Co znamená Set u termoprádla?',
     'Je to komplet, který obvykle zahrnuje horní a spodní díl. Pořizovat sadu bývá praktičtější než kupovat každou část zvlášť.'),
]
