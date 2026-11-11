"""sporteka.cz — facet landing texts wave 176: salomon-lyze, husky-bunda, lacoste-tenisky, nike-sportovni-boty.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ salomon-lyze
NEW['salomon-lyze'] = dict(
    title='Salomon lyže: řady S/MAX, Stance, QST a závodní modely',
    desc='Salomon lyže pro carving, all-mountain i freeride. Rozdíly mezi řadami S/MAX, Stance a QST, výběr délky a vázání a porovnání nabídky obchodů.',
    intro='<p>Salomon patří k největším jménům v lyžování a v nabídce českých obchodů ho najdete jak u sjezdových lyží s vázáním, tak u kompletů pro běžecké lyžování. Značka staví řady podle stylu jízdy: S/MAX míří na rekreační carving, Stance a Addict na univerzální jízdu, QST na volnější terén a Equipe a S/Race na sportovně naladěné lyžaře a juniory. '
          'Tato stránka shrnuje lyže Salomon z kategorie <a href="/sjezdove-lyze/">sjezdové lyže</a> a ukazuje, kde se ve vybraném modelu a délce vyplatí hledat skladem. '
          'Průvodce níže vysvětluje, jak se řady liší, jak poznat model pro začátečníka a pro pokročilého, co znamenají zkratky v názvu a proč se vyplatí hlídat, jestli lyže přicházejí s vázáním nebo bez něj. Na konci najdete odkazy na další značky, na lyžařské boty a na doplňky, které k lyžím patří.</p>',
    guide='<h2>Jak je Salomon uspořádaný v nabídce lyží</h2>'
          '<p>Salomon je francouzská značka z lyžařského prostředí Alp a dnes patří do skupiny, která stojí i za dalšími sportovními značkami. Vyrábí sjezdové a běžecké lyže, lyžařské boty, vázání, helmy a outdoorovou obuv. U sjezdových lyží se orientace v katalogu opírá o názvy řad, protože právě ty říkají, na jaký terén je lyže stavěná. Zkratky a čísla jsou součástí názvu a obvykle ukazují na úroveň v rámci řady.</p>'
          + T(['Řada', 'Zaměření', 'Pro koho'], [
              ['S/MAX', 'carving na upravené sjezdovce', 'rekreační lyžaři od začátečníků po dobré střední pokročilé'],
              ['Stance', 'univerzální all-mountain', 'ti, kdo jezdí sjezdovku, ale občas odbočí na nezpracovaný sníh'],
              ['Addict', 'sportovnější all-mountain', 'zkušenější lyžaři, kteří chtějí živější a rychlejší lyži'],
              ['QST', 'širší lyže do volnějšího terénu', 'lyžaři, kteří rádi vyrazí mimo sjezdovku'],
              ['Equipe a S/Race', 'závodně laděné modely, slalom a obří slalom', 'pokročilí lyžaři a mladí závodníci'],
              ['Juniorské modely', 'zmenšené verze s mírnější konstrukcí', 'děti a dorost, viz <a href="/detske-lyze/">dětské lyže</a>']]) +
          '<p>Salomon v nabídce označuje také ženské modely, ať už zvláštním názvem, nebo slovem dámské v popisu. Mají obvykle lehčí a měkčí konstrukci a vázání je nastavené na nižší hmotnost a menší chodidla. Pro rychlejší srovnání použijte i výběry <a href="/damske-sjezdove-lyze/">dámské sjezdové lyže</a> a <a href="/sjezdove-lyze-panske/">pánské sjezdové lyže</a>.</p>'
          '<h2>S/MAX: lyže pro většinu rekreačních lyžařů</h2>'
          '<p>Kdo jezdí o víkendech a na dovolené, většinou skončí u carvingových lyží. Řada S/MAX je určená právě jim. Tělo lyže je užší, boční zaoblení umožňuje zatáčet na hraně a vyšší čísla v názvu zpravidla značí tužší a výkonnější verzi. Nižší číslo se hodí pro začátečníky a pro lyžaře, kteří preferují klidnou jízdu. Vyšší patří lidem, kteří jezdí rychleji a chtějí, aby lyže držela stopu i na tvrdém, ojeděném sněhu.</p>'
          '<p>U modelů s označením XT nebo Ti se objevuje vyztužená konstrukce. Neznamená to automaticky lepší lyži pro každého: tužší lyže potřebuje silnější tlak a lepší techniku, jinak působí unaveně a nedělá radost. Pokud si nejste jistí, vyberte spíše o stupeň měkčí a přívětivější. Rozdíl pocítíte hned v prvním dni na svahu.</p>'
          '<h2>Stance, Addict a QST: když sjezdovka nestačí</h2>'
          '<p>All-mountain lyže jsou širší než carvingové, takže líp plují v čerstvém sněhu a lépe snášejí rozbité svahy po poledni. Stance je kompromisní volba pro lyžaře, který chce jednu lyži na všechno. Addict je živější a vhodnější pro ty, kdo jezdí svižně a rádi se naklánějí do oblouků. QST míří ještě víc do volného terénu a hodí se tam, kde chcete mít při pohybu mimo upravenou trať víc stability.</p>'
          '<p>Širší lyže má nevýhodu na tvrdé sjezdovce, kde se z hrany na hranu překlápí pomaleji. Pokud jezdíte převážně na upravených tratích v Česku, je užší carvingový model často praktičtější. Pro skutečné freeridové lyžování existuje i užší nabídka z kategorie <a href="/skialpove-lyze/">skialpové lyže</a>, ale ty se staví na stoupání a pro klasickou sjezdovku se příliš nehodí.</p>'
          '<h2>Jak číst názvy a zkratky v nabídce</h2>'
          '<p>Salomon uvádí v názvu často i vázání a obchody k tomu přidávají vlastní popis. Pomůže tento přehled.</p>'
          '<ul><li><strong>Číslo za názvem řady</strong> (například 8, 10, 12) obvykle označuje úroveň výkonu. Vyšší číslo bývá tužší lyže pro lepší lyžaře.</li>'
          '<li><strong>Označení M10, M11, MI12 a podobně</strong> patří vázání. Číslo souvisí s nastavitelnou hodnotou vypínání, takže určuje, pro jak těžkého a rychlého lyžaře je vázání vhodné.</li>'
          '<li><strong>GW</strong> znamená, že vázání je kompatibilní s podrážkami GripWalk, které mají mírně zakulacenou patu a kroky v nich jsou pohodlnější.</li>'
          '<li><strong>Brzda s číslem</strong> (například 80) odpovídá šířce brzdy a ta musí sedět k šířce lyže pod vázáním, jinak se při pádu nesprávně otevře.</li>'
          '<li><strong>Ročník</strong> jako 2026/2027 ukazuje sezonu. Starší ročník je často levnější a pro rekreační použití stejně dobrý, ale může mít jiné barvy nebo drobné konstrukční změny.</li></ul>'
          '<h2>Lyže s vázáním, nebo samostatně</h2>'
          '<p>Salomon lyže přicházejí v nabídce často jako komplet s vázáním. To je pohodlné, protože výrobce spáruje lyži s vázáním, které má správnou brzdu a technické parametry. Dostupnost najdete v kategorii <a href="/lyze-komplety/">lyže s vázáním (komplety)</a>. Samostatné lyže mají smysl u pokročilých, kteří chtějí zvolit vázání podle hmotnosti a stylu, a u závodních modelů, kde se vázání většinou prodává zvlášť. Vázání vybírejte v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a> a nastavte ho vždy v servisu, protože špatně seřízené vázání je nejčastější skrytá chyba při výbavě.</p>'
          '<p>Kompatibilita s botou není samozřejmost. Klasická alpská podrážka a GripWalk mají jiný tvar a vázání musí obě podrážky podporovat. Pokud boty nemáte, koupi řešte společně a zkontrolujte popis. Nabídku najdete v kategorii <a href="/lyzarske-boty/">lyžařské boty</a>.</p>'
          '<h2>Délka lyží Salomon a rady pro výběr</h2>'
          '<p>Délka se mezi řadami mírně liší, protože rockerové a zaoblené špičky na sněhu fungují jako delší oblouk, než ukazuje číslo v centimetrech. Proto lyže pro volný terén bývají delší a carvingové kratší. Obecné pravidlo je stejné: začátečníci kratší, pokročilí delší. Podrobnou tabulku najdete v textu kategorie <a href="/sjezdove-lyze/">sjezdové lyže</a>. Zde jen několik poznámek ke značce:</p>'
          '<ul><li>U lyží s větším zaoblením a mírným rockerem stačí kratší délka než u klasického tvaru.</li>'
          '<li>Pokud váháte mezi dvěma délkami, vybírejte podle hmotnosti a zkušeností, ne podle výšky.</li>'
          '<li>Pro děti a rostoucí dorost kupujte raději novou lyži menší, než lyži o dvě velikosti větší, kterou nezvládnou.</li>'
          '<li>Lehčí dospělí lyžaři se často lépe cítí na měkčích ženských nebo juniorských řadách.</li></ul>'
          '<h2>Salomon a ostatní značky lyží</h2>'
          '<p>Lyže vyrábí mnoho značek a každá má trochu jiný charakter. Pokud chcete porovnat, otevřete nabídky <a href="/head-lyze/">Head</a>, <a href="/rossignol-lyze/">Rossignol</a>, <a href="/fischer-lyze/">Fischer</a> nebo <a href="/sjezdove-lyze-atomic/">Atomic</a>. Rozdíly nejsou tak velké, aby jedna značka byla pro každého lepší. Důležitější je typ lyže, délka a úroveň výkonu. Salomon bývá oblíbený u lyžařů, kteří chtějí lyži s přívětivým chováním a široký výběr v řadách pro rekreační jízdu. Rozhodnutí by neměla stát na logu, ale na tom, zda lyže odpovídá vašemu stylu.</p>'
          '<h2>Salomon i mimo sjezdové lyže</h2>'
          '<p>Salomon je silný i v běžeckém lyžování. V nabídce se proto vedle sjezdových lyží objevují také komplety běžek s vázáním, jak klasických, tak bruslařských, včetně juniorských. Bruslařská technika vyžaduje delší a tužší lyže a hůlky, klasická styl používá stopu a podklad s vosky nebo šupinami. Pro takové lyže otevřete kategorii <a href="/bezecke-lyze/">běžecké lyže</a>, protože mají jinou délku, vázání i upevnění boty. Souhrn značky najdete také na stránce <a href="/znacka/salomon/">Salomon</a>, kde jsou lyže, obuv a další zboží pohromadě.</p>'
          '<h2>Na co nezapomenout při nákupu</h2>'
          '<p>Kromě lyží potřebujete boty, hole a helmu. Hole vyberete podle výšky a stylu jízdy v kategorii <a href="/lyzarske-hole/">lyžařské hole</a>, helmu v kategorii <a href="/lyzarske-helmy/">lyžařské helmy</a>. U všech částí platí stejné pravidlo: zkontrolujte velikost, ročník a to, zda je zboží skladem. Sporteka porovnává nabídky českých obchodů a ukáže vám, kde je vámi hledaná délka dostupná, takže nemusíte objíždět jednotlivé e-shopy ručně. Po sezóně lyže očistěte, vosk a hrany ošetřete a uložte je na suchém místě mimo přímé teplo. Tak vydrží dlouho a na svahu se budou chovat předvídatelně.</p>',
    faq=[
        ('Pro koho je řada Salomon S/MAX?', 'Pro rekreační lyžaře, kteří jezdí hlavně po upravených sjezdovkách. Nižší čísla v názvu jsou měkčí a odpustí chyby, vyšší jsou tužší a pro lepší lyžaře. Pokud začínáte, zvolte spíš nižší stupeň a krátkou až střední délku.'),
        ('Čím se liší Salomon Stance od carvingových lyží?', 'Stance je širší, takže lépe snáší rozbitý sníh a výlety mimo sjezdovku. Na tvrdé upravené trati se ale překlápí z hrany na hranu pomaleji než užší carvingová lyže. Je to dobrá volba pro univerzální použití.'),
        ('Je lepší koupit Salomon lyže s vázáním, nebo bez?', 'Pro většinu rekreačních lyžařů je jednodušší komplet, protože vázání už je spárované s lyží. Samostatné lyže se hodí tomu, kdo chce vázání přizpůsobit hmotnosti a stylu jízdy. V obou případech nechte vázání seřídit v servisu.'),
        ('Co znamená označení GW u vázání Salomon?', 'GW je zkratka pro kompatibilitu s podrážkami GripWalk. Takové boty mají mírně zaoblenou podrážku, v níž se pohodlněji chodí. Vázání označené GW pasuje i na klasické alpské podrážky, ale vždy ověřte popis konkrétního modelu.'),
        ('Jakou délku lyží Salomon zvolit?', 'Začátečníci obvykle kratší, přibližně k bradě až nosu, pokročilí delší. Záleží i na typu lyže: carvingové bývají kratší, freeridové delší. Pokud váháte mezi dvěma délkami, rozhodněte podle hmotnosti a zkušeností, ne jen podle výšky.'),
        ('Najdu u Salomonu i lyže pro děti?', 'Ano, značka nabízí juniorské sjezdové lyže i dětské a juniorské komplety pro běžecké lyžování. Kupujte podle výšky a hmotnosti dítěte, ne s velkou rezervou, protože lyže, která je příliš dlouhá, brání v zatáčení. Další modely najdete v kategorii dětské lyže.'),
        ('Hodí se Salomon i na běžky?', 'Ano. Salomon vyrábí běžecké lyže pro klasický styl i pro bruslení, v nabídce jsou i komplety s vázáním. Mají jiný tvar i délku než sjezdové lyže, proto je vybírejte v samostatné kategorii běžecké lyže a ne podle sjezdových tabulek.'),
        ('Mám kupovat starší ročník lyží?', 'Pro rekreační lyžování je starší ročník často rozumná volba, protože konstrukce se mezi sezónami mění jen mírně. Zkontrolujte, zda je lyže nepoužitá a zda je k dispozici potřebná délka a vázání. Rozdíl bývá hlavně v grafice.'),
        ('Jak pečovat o lyže Salomon po sezóně?', 'Očistěte skluznici, nechte lyže vyschnout a v servisu nechte opravit hrany a navoskovat. Uložte je na suchém místě bez přímého tepla a s uvolněnou brzdou nebo s mírně povoleným vázáním. Před novou sezónou nechte vázání zkontrolovat.'),
    ],
)

# ------------------------------------------------------------------ husky-bunda
NEW['husky-bunda'] = dict(
    title='Husky bunda: hardshell, softshell a zimní modely',
    desc='Husky bundy pánské i dámské: hardshell, softshell, outdoorové a plněné zimní modely. Jak poznat typ podle názvu, vybrat velikost a porovnat nabídky.',
    intro='<p>Husky je česká outdoorová značka a její bundy se v obchodech snadno poznají podle názvů, které začínají na N nebo S a hned prozradí typ. Neoni, Nickin nebo Nicker jsou hardshelly do deště, Salfa, Silvo a Sonny softshelly na proměnlivé počasí, Nomi a Nakama outdoorové bundy pro běžné nošení, Nitri lehká plněná bunda a Norel zimní model. '
          'Na této stránce je výběr bund Husky z kategorie <a href="/sportovni-bundy/">sportovní bundy a vesty</a> pro muže i ženy. '
          'Průvodce vysvětluje, jak se jednotlivé typy liší, co rozhoduje o prodyšnosti a nepromokavosti, jak vybrat velikost a vrstvení pod bundu a jak se Husky řadí vedle ostatních značek. Pomůže vám rozhodnout se mezi tenkou skořepinou do deště a teplejším softshellem na podzim a zimu.</p>',
    guide='<h2>Jak číst názvy modelů Husky</h2>'
          '<p>Husky dává modelům jména, která se opakují napříč sezónami a barvami. Vedle jména je v obchodech uveden i typ: hardshell, softshell, outdoor nebo plněná bunda. Pánské a dámské verze mají často stejný název a liší se střihem, takže ve výsledcích uvidíte například Neoni pro muže i pro ženy. Pro rychlou orientaci slouží tento přehled.</p>'
          + T(['Typ', 'Příklady z nabídky', 'K čemu se hodí'], [
              ['Hardshell', 'Neoni, Nickin, Nicker, Nanola', 'déšť, vítr, výlety v horách, cestování'],
              ['Softshell', 'Salfa, Silvo, Sonny', 'jaro a podzim, aktivní chůze, běžné nošení'],
              ['Outdoorová bunda', 'Nomi, Nakama', 'město a lehká turistika, univerzální vrstva'],
              ['Plněná ultralehká', 'Nitri', 'chladné dny, balení do batohu'],
              ['Zimní plněná', 'Norel', 'mrazy, procházky, delší zastavení'],
              ['Hardshell s výplní', 'Nesebi', 'zima s deštěm nebo mokrým sněhem'],
              ['Péřová vesta', 'Dresles', 'doplněk pod bundu nebo samostatně na chladnější dny']]) +
          '<p>Přesné parametry membrány a výplně si vždy přečtěte v popisu konkrétní barvy a ročníku. Model se může mezi sezónami změnit, i když název zůstane stejný.</p>'
          '<h2>Hardshell: bunda, která zastaví déšť</h2>'
          '<p>Hardshell je tenká vnější vrstva s membránou, která nepouští vodu. Hodí se tam, kde potřebujete skutečnou ochranu před lijákem a ostrým větrem. Vedle membrány záleží na zalepených švech, zipu s krytkou a kapuci, kterou lze stáhnout kolem obličeje a zvednout přes helmu nebo čepici. Husky hardshelly jsou spíš lehké a skladné, proto je lidé nosí v batohu pro případ, že se počasí zlomí. Pokud hledáte specializovanější výběr, podívejte se do kategorie <a href="/nepromokave-bundy/">nepromokavé a outdoorové bundy</a>.</p>'
          '<p>Prodyšnost není u žádné membrány neomezená. Při rychlé chůzi do kopce se může uvnitř srážet pot, zejména pod batohem. Pomáhají větrací zipy v podpaží a spodní vrstva, která pot odvádí. Nejlevnější vrstva pod bundu je tenké funkční tričko, ne bavlna.</p>'
          '<h2>Softshell: pohodlí a pružnost</h2>'
          '<p>Softshell je měkčí, pružnější a prodyšnější než hardshell. Vnější tkanina je často napuštěná impregnací proti lehkému dešti, vnitřní strana bývá česaná. Lidé ho nosí od jara do podzimu a v zimě jako střední vrstvu. Pro pohyb ve větru a při aktivitě je to často nejpříjemnější volba, protože se v ní nepotíte tak jako v neprodyšné pláštěnce. Při delším dešti ale promokne. Další výběr najdete v kategorii <a href="/softshellove-bundy/">softshellové bundy</a>.</p>'
          '<p>Kdo hledá jednu bundu na většinu dní, často zvolí softshell, který lze doplnit lehkou pláštěnkou do deště. Opačné řešení je hardshell s teplým flísem pod ním. Obě varianty fungují, rozdíl je v tom, zda chcete jedno oblečení, nebo dvě samostatné vrstvy.</p>'
          '<h2>Plněné a zimní bundy</h2>'
          '<p>Plněné bundy drží teplo díky vzduchu zachycenému ve výplni. Ultralehké modely typu Nitri jsou určené na chladné dny a na vrstvení, ne na mráz bez pohybu. Zimní Norel a hardshellové plněné modely mají silnější izolaci a hodí se na delší pobyt venku. Pokud chcete plnohodnotnou zimní výbavu, projděte i <a href="/zimni-bundy/">zimní a péřové bundy</a>. Péřové vesty typu Dresles se osvědčily jako doplněk: drží jádro těla v teple a nechávají ruce volné, takže se dají nosit i pod hardshell.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Značka rozlišuje pánské a dámské střihy, v nabídce jsou označené M a L podle obvyklé velikosti. Pánské bundy mají přímější střih a širší ramena, dámské jsou užší v pase a mívají delší záda. Při výběru vezměte v úvahu, co budete pod bundou nosit. Pokud ji chcete používat i v zimě přes mikinu, volte volnější velikost. Pro aktivní sporty se hodí přiléhavější střih, který se neobléká do větru.</p>'
          '<ul><li><strong>Délka rukávů:</strong> při zvednutých pažích nemá odhalit zápěstí.</li>'
          '<li><strong>Délka těla:</strong> zadní část má krýt bederní oblast při předklonu.</li>'
          '<li><strong>Kapuce:</strong> musí jít nastavit bez zakrývání výhledu.</li>'
          '<li><strong>Kapsy:</strong> na zip, aby nic nevypadlo; zkuste, zda jsou dostupné i s batohem.</li>'
          '<li><strong>Manžety a lem:</strong> nastavitelné suchým zipem nebo šňůrkou omezí průvan.</li></ul>'
          '<h2>Vrstvení pod bundu Husky</h2>'
          '<p>Bunda je jen vnější vrstva. V mírném počasí stačí tričko a tenká mikina, ve chladu přidejte flís nebo lehký izolační kus. Pro zimu dobře funguje funkční prádlo, střední teplá vrstva a vnější ochrana. Bavlna se nasákne potem a hřeje špatně, proto se jí při pohybu v chladu vyhněte. Další oblečení na turistiku najdete v kategorii <a href="/outdoor/">outdoor</a>. U cestování je praktické, když bunda jde sbalit do vlastní kapsy a nezabere víc místa než láhev.</p>'
          '<h2>Která bunda Husky na jakou činnost</h2>'
          '<p>Stejný model se nehodí na všechno. Před nákupem si ujasněte, kde bunda stráví nejvíc času, a podle toho zvolte typ.</p>'
          + T(['Činnost', 'Vhodnější typ', 'Poznámka'], [
              ['Víkendová turistika v Česku', 'softshell nebo lehký hardshell v batohu', 'počasí se mění, proto se vyplatí vrstvení'],
              ['Pobyt v horách za deště', 'hardshell s pevnou kapucí', 'zkontrolujte zalepené švy a krytku zipu'],
              ['Dojíždění a město', 'outdoorová bunda nebo softshell', 'důležité je pohodlí, kapsy a nenápadná barva'],
              ['Chladné ráno, svižný pohyb', 'lehká plněná bunda nebo vesta', 'při pohybu se rychle přehřejete, vrstvu lze sundat'],
              ['Zimní procházky', 'plněná zimní bunda', 'pod ni stačí tenčí vrstva, nabalený svetr zbytečně svazuje'],
              ['Cestování letadlem', 'sbalitelná bunda', 'vejde se do příručního zavazadla a nahradí deštník']]) +
          '<p>Při rozhodování pomáhá jednoduché pravidlo: pro suchý chlad zvolte teplo a prodyšnost, pro vlhko membránu. Pokud bydlíte v místě, kde často fouká, myslete také na to, že vítr odebírá teplo rychleji než teplota vzduchu. Proto i tenká vrstva, která ho zastaví, často pomůže víc než silnější svetr pod ní.</p>'
          '<h2>Barvy a viditelnost</h2>'
          '<p>Husky nabízí modely v široké paletě, od černé a antracitové přes modré a zelené odstíny až po hořčicovou, růžovou nebo fialovou. Černá a šedá se dobře kombinují a méně ukazují špínu, ale v šeru jsou hůř vidět. Žlutá, oranžová nebo světle zelená jsou výraznější pro pohyb po silnici i v mlze a při hledání člena skupiny v terénu. Světlé barvy, například béžová nebo pastelová, vypadají na procházce dobře, ale rychleji zašpiní lem a manžety. Pokud bundu používáte i v zimě, myslete na to, že tmavá se na slunci nahřeje rychleji než světlá, což může být výhoda ve stínu, ale na horách v létě nepříjemnost.</p>'
          '<h2>Husky vedle ostatních značek</h2>'
          '<p>Husky je zaměřené hlavně na turistiku a volný čas a patří k českým značkám s širokým výběrem barev. Pro porovnání se můžete podívat na <a href="/hannah-bunda/">Hannah</a>, <a href="/kilpi-bunda/">Kilpi</a>, <a href="/alpine-pro-bunda/">Alpine Pro</a> nebo <a href="/northfinder-bunda/">Northfinder</a>, které cílí na podobné zákazníky. Mezi zahraničními značkami stojí za pozornost <a href="/columbia-bunda/">Columbia</a> a <a href="/the-north-face-bunda/">The North Face</a>. Nejde o to, která značka je nejlepší, ale kterou bundu potřebujete a zda vám střih sedí. Hlavní souhrn zboží této značky je také na stránce ' + B(('husky', 'Husky')) + '.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Membrána a impregnace mají kratší životnost, když se bunda nepere. Naopak pravidelné praní při nízké teplotě a šetrným prostředkem bez aviváže obnovuje prodyšnost a po usušení ji lze krátce vložit do sušičky, pokud to štítek dovolí. Impregnaci pak obnovíte sprejem nebo prostředkem do pračky. Péřové a plněné bundy sušte s tenisovými míčky, aby se výplň nespojila do hrudek. Odkládejte je volně pověšené, ne stlačené v pytli.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejný model Husky se prodává ve více barvách a velikostech a některé obchody mají skladem jen část z nich. Sporteka ukazuje stejné zboží u více obchodů vedle sebe, takže uvidíte, kde je dostupná vaše velikost a barva. Pokud hledáte i vesty, otevřete <a href="/sportovni-vesty/">sportovní vesty</a>, pro lehčí věc na jaro a podzim <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> a pro větrné dny <a href="/vetrovky/">větrovky a šusťákové bundy</a>.</p>',
    faq=[
        ('Co znamenají jména Neoni, Salfa a Nomi u bund Husky?', 'Husky používá jména modelů, která se opakují v sezónách. Neoni, Nickin a Nicker jsou hardshelly, Salfa, Silvo a Sonny softshelly, Nomi a Nakama outdoorové bundy. Typ je vždy uveden v názvu položky.'),
        ('Je hardshell Husky vhodný do deště?', 'Hardshell má membránu a je určen na déšť a vítr. Zkontrolujte popis konkrétního modelu a pamatujte, že prodyšnost má své meze. Při intenzivní aktivitě otevřete větrací zipy a pod bundu oblékněte vrstvu, která odvádí pot.'),
        ('Jaký je rozdíl mezi softshellem a hardshellem?', 'Softshell je pružnější a prodyšnější a snese lehký déšť, hardshell chrání před silnějším deštěm a větrem. Pro aktivní pohyb v chladu je pohodlnější softshell, pro lijáky potřebujete hardshell.'),
        ('Do jaké zimy se hodí bunda Husky?', 'Záleží na modelu a výplni. Ultralehké plněné bundy slouží do chladnějších dnů a na vrstvení, zimní plněné kusy zvládnou mráz při chůzi. Pro dlouhé zastavení v mrazu je potřeba silnější izolace a teplé vrstvy pod bundou.'),
        ('Jak vybrat velikost Husky bundy?', 'Změřte hrudník, v případě žen i boky, a porovnejte s tabulkou výrobce. Pokud chcete bundu přes mikinu, zvolte volnější velikost. Vyzkoušejte, zda rukávy při zvednutých pažích nezkrátí a zda bunda kryje bederní oblast.'),
        ('Jsou Husky bundy pánské i dámské?', 'Ano, většina modelů je k dispozici v obou verzích. Dámské mají užší střih v pase a delší záda, pánské přímější linii a širší ramena. Ve výsledcích proto kontrolujte označení M nebo L v názvu a pohlaví v popisu.'),
        ('Jak prát bundu s membránou?', 'Použijte šetrný prací prostředek bez aviváže, nízkou teplotu a štítek výrobce. Po usušení se prodyšnost a hydrofobní úprava často zlepší. Povrchovou impregnaci lze obnovit prostředkem určeným pro membrány.'),
        ('Hodí se Husky bunda i na každodenní nošení?', 'Ano, outdoorové a softshellové modely se nosí v městském provozu stejně dobře jako na výletě. Při volbě barvy zvažte praktičnost: tmavé odstíny jsou nenápadné, světlé a výrazné lépe vidět v horském terénu nebo za šera.'),
        ('Kde porovnat nabídky bund Husky?', 'Na této stránce vidíte více obchodů u stejného modelu. Zkontrolujte dostupnost velikosti a barvy, protože u oblíbených modelů mají obchody často skladem jen část řady. Srovnání nabídek šetří čas a ukáže, kde je právě dostupná vaše varianta.'),
    ],
)

# ------------------------------------------------------------------ lacoste-tenisky
NEW['lacoste-tenisky'] = dict(
    title='Lacoste tenisky: Carnaby, L003, Ziane a další modely',
    desc='Lacoste tenisky pánské, dámské i dětské. Rozdíl mezi modely Carnaby, L003, T-Clip a Ziane, výběr velikosti, údržba kůže a porovnání nabídek obchodů.',
    intro='<p>Lacoste je francouzská značka spojená s tenisem, krokodýlem na hrudi a polo košilí, a její tenisky nesou stejnou čistou, zdrženlivou estetiku. Většina modelů vychází z kurtové obuvi: nízký střih, hladká kůže nebo textil, bílý základ a drobný krokodýl na boku. '
          'Na této stránce najdete Lacoste z kategorie <a href="/tenisky/">tenisky a volnočasové boty</a>, od klasických Carnaby přes objemnější L003 až po lehčí sportovní kousky typu Powercourt nebo Lineshot. '
          'Průvodce vysvětluje, v čem se modely liší, jak je kombinovat s oblečením, jak čistit kůži a bílou podrážku a jak zvolit velikost. Nechybí srovnání s dalšími značkami a rady pro dámské i dětské varianty.</p>',
    guide='<h2>Odkud Lacoste tenisky pocházejí</h2>'
          '<p>Značku založil francouzský tenista René Lacoste a první kousky oblečení vznikly pro kurt. Z tenisových kořenů vychází i obuv: dnešní tenisky Lacoste jsou převážně nízké, s plochou nebo mírně profilovanou podrážkou, a nosí se spíš jako módní, ale praktická městská obuv než jako sportovní vybavení. Některé modely s označením Power Serve, Lineshot nebo Baseshot se k tenisu vztahují i funkčně, většina nabídky je ale určená na každodenní chůzi.</p>'
          '<h2>Hlavní modely v nabídce</h2>'
          '<p>Katalog je rozsáhlý a modely se opakují v mnoha barvách a ročnících. Několik názvů se ale vrací pravidelně a pomáhá se v nich zorientovat.</p>'
          + T(['Model', 'Charakter', 'Pro koho'], [
              ['Carnaby (Set, Cup, Evo)', 'klasické nízké tenisky s kurtovým vzhledem, často kůže', 'ti, kdo chtějí nadčasovou bílou botu do města'],
              ['L003 (Neo, 2K24)', 'objemnější podešev, moderní, někdy textilní svršek', 'streetwear, pohodlná celodenní chůze'],
              ['T-Clip', 'jednoduchý střih, minimalistický vzhled', 'kancelář s volnějším dress codem'],
              ['Ziane, Ziane Platform', 'lehčí střih, dámské i pánské verze, platforma u dámských', 'každodenní nošení, kombinace se šaty i kalhotami'],
              ['Powercourt, Lerond, Elite Active', 'sportovnější, kurtový základ', 'volný čas a sportovní styl'],
              ['Graduate, Sideline, Cherre', 'klasické kurtové střihy z dřívějších kolekcí', 'retro vzhled'],
              ['Lineshot, Baseshot, Spinor, L-Guard Breaker', 'výrazné podrážky a moderní tvary', 'moderní městský styl']]) +
          '<p>Sortiment se mění podle sezón, a proto při porovnání vždy kontrolujte ročník a materiál, ne jen jméno. Bílý Carnaby z kůže a plátěný Carnaby jsou dvě rozdílné boty s rozdílným komfortem i péčí.</p>'
          '<h2>Kůže, textil a syntetika</h2>'
          '<p>Lacoste tenisky se vyrábějí z kůže, textilu i kombinace materiálů. Kůže vypadá reprezentativně, dobře se čistí vlhkým hadříkem a časem se přizpůsobí noze, ale v létě je méně prodyšná a po namočení potřebuje opatrné sušení. Textilní a syntetické modely jsou lehčí a prodyšnější, hodí se na teplejší dny a na cesty, ale snáz se zašpiní a hůře snášejí deštivé počasí. Pokud chcete jednu botu na většinu roku, zvolte kůži s kvalitní impregnací. Na léto a cestování sáhněte po textilu.</p>'
          '<h2>Bílé tenisky a údržba</h2>'
          '<p>Bílá je pro Lacoste základní barva a pozná se podle ní celá značka. Nevýhodou je, že ukazuje každou skvrnu. Pomůže několik pravidel.</p>'
          '<ul><li><strong>Čistěte hned:</strong> čerstvá skvrna z bláta nebo kávy zmizí snadno, zaschlá se vpíjí do pórů.</li>'
          '<li><strong>Měkký kartáč a vlažná voda:</strong> u kůže stačí jemný čisticí prostředek na boty, agresivní chemie ji vysušuje.</li>'
          '<li><strong>Podrážka:</strong> gumovou stranu lze čistit zubním kartáčkem a jemným čisticím prostředkem.</li>'
          '<li><strong>Sušení:</strong> nikdy na topení, kůže by se zkroutila a prasknula. Vycpěte papírem a nechte vyschnout při pokojové teplotě.</li>'
          '<li><strong>Impregnace:</strong> sprej před prvním nošením snižuje vsakování vody a špíny.</li></ul>'
          '<p>Pokud nechcete denně řešit bílou, vyberte tmavší odstíny, které jsou praktičtější v zimě a po dešti. Černé tenisky a další barvy najdete v nabídce i u ostatních značek, například ve výběru <a href="/cerne-tenisky-nike/">černé tenisky Nike</a>.</p>'
          '<h2>Velikost a pohodlí</h2>'
          '<p>Lacoste střihy bývají spíš přiléhavější a nižší, takže u modelů se špičatější špičkou nebo tuhou kůží se vyplatí počítat s mírnou rezervou. Změřte chodidlo večer, kdy je nejširší, a porovnejte s tabulkou výrobce. Na krabici je u některých modelů uvedena i britská velikost, ale rozhodující je vždy délka vnitřní stélky v centimetrech. Pokud máte široké chodidlo, hledejte textilní svršek, který se přizpůsobí, nebo zvolte o půl čísla větší, pokud to střih dovolí. Pro dlouhou chůzi pomůže měkčí mezipodešev a vložka, kterou lze vyměnit za ortopedickou.</p>'
          '<h2>Pánské, dámské a dětské Lacoste</h2>'
          '<p>Dámské modely mají užší patu a středový díl, dostupné jsou i varianty na platformě, které prodlužují siluetu. Pánské jsou širší a mají pevnější stavbu. U dětí se objevují zmenšené verze oblíbených kousků, často se suchým zipem nebo se šněrováním. Dětské tenisky kupujte s rezervou zhruba centimetr a velikost kontrolujte po několika měsících, protože noha roste rychle. Pro dívky a ženy je užitečný také výběr <a href="/damske-tenisky/">dámské tenisky</a>, kde můžete porovnat Lacoste s dalšími značkami.</p>'
          '<h2>Jak Lacoste nosit</h2>'
          '<p>Bílé nebo světlé tenisky se hodí k džínám, chino kalhotám, šortkám i letním šatům. Značka je ceněná pro to, že vypadají upraveně a přitom nejsou formální. K obleku vybírejte hladkou kůži bez výrazné podrážky. Do města se hodí polstrované verze s měkkou stélkou, na procházku ocení lidé lehčí textil. Pokud chcete vzhled odlišit, zvolte barevný detail, například zelený nebo modrý prvek, který podtrhne polo košili ze stejné značky.</p>'
          '<h2>Jaký model zvolit podle situace</h2>'
          '<p>Stejná značka nabízí boty s odlišným charakterem. Před nákupem se zeptejte, kolik kroků za den nachodíte a jak formální má být vaše okolí.</p>'
          + T(['Situace', 'Doporučený směr', 'Na co dát pozor'], [
              ['Kancelář s uvolněným oblékáním', 'hladká kožená bílá nebo tmavá bota nízkého střihu', 'tenká podešev méně tlumí, při dlouhé chůzi unavuje'],
              ['Celodenní pobyt ve městě', 'model s objemnější mezipodešví a měkkou vložkou', 'hmotnější bota, v létě teplejší'],
              ['Léto a dovolená', 'textilní nebo perforovaný svršek', 'snáz se špiní a hůř odolává dešti'],
              ['Škola a mladší děti', 'zmenšená verze se suchým zipem nebo gumičkami', 'rychle se vyroste, hlídejte rezervu'],
              ['Společenské příležitosti', 'jednobarevná hladká kůže bez výrazných prvků', 'bílá vyžaduje čerstvě vyčištěnou podrážku']]) +
          '<p>Při pochybnostech sáhněte po klasickém střihu, který se nejlépe kombinuje a nezestárne s módou. Výrazná podrážka nebo hodně barev vypadá skvěle sezónu, ale hůř se skloubí s tím, co už máte ve skříni.</p>'
          '<p>Pokud chcete bílé boty udržet dlouho, střídejte dva páry a nenoste jedny každý den. Kůže potřebuje čas, aby po nošení vyschla a vrátila se do tvaru. Boty ukládejte s vycpávkou nebo napínačem a mimo přímé slunce, které bílou barvu žloutne.</p>'
          '<h2>Starší kolekce a výprodeje</h2>'
          '<p>Lacoste mění kolekce dvakrát ročně a obchody pak vyprodávají zbylé velikosti starších modelů. Tyto boty bývají stejně kvalitní jako nové, jen mají jiný ročník v kódu. Vyplatí se kontrolovat, zda zbytek velikostní řady skutečně odpovídá vaší noze a zda bota nebyla dlouho uložená. U kůže se po letech v krabici může objevit zaschlé lepidlo nebo drobné praskliny na ohybech. Při nákupu na dálku proto sledujte popis stavu a podmínky vrácení.</p>'
          '<h2>Lacoste a ostatní značky tenisek</h2>'
          '<p>Na trhu je mnoho značek s podobným stylem. Pokud hledáte sportovnější vzhled, podívejte se na <a href="/nike-tenisky/">Nike</a>, <a href="/adidas-tenisky/">Adidas</a>, <a href="/new-balance-tenisky/">New Balance</a> nebo <a href="/puma-tenisky/">Puma</a>. Pro módnější nebo pohodlnější linii zkuste <a href="/tenisky-tommy-hilfiger/">Tommy Hilfiger</a>, <a href="/fila-tenisky/">Fila</a> nebo <a href="/tenisky-vans/">Vans</a>. Lacoste se z nich odlišuje především klasickým kurtovým vzhledem, nižší siluetou a čistými liniemi. Pro dlouhou chůzi v terénu nebo na sport je lepší specializovaná obuv, třeba <a href="/tenisova-obuv/">tenisová obuv</a> nebo <a href="/bezecka-obuv/">běžecké boty</a>. Přehled všech modelů značky je i na stránce ' + B(('lacoste', 'Lacoste')) + '.</p>'
          '<h2>Jak porovnat nabídky Lacoste</h2>'
          '<p>Jeden model je často v obchodech pod trochu jiným názvem, takže stojí za to hledat podle kódu uvedeného v popisu. Sporteka u stejného páru porovnává více obchodů a ukáže, kde je dostupná vaše velikost a barva. Pozor na zboží z minulých kolekcí, které může mít jiné rozměry i materiály než aktuální verze. Pokud kupujete na dálku, ověřte lhůtu pro vrácení zboží a sledujte, zda je boty možné vyzkoušet.</p>',
    faq=[
        ('Jaký je nejznámější model Lacoste tenisek?', 'Nejznámější je Carnaby, nízká tenisová bota v klasickém bílém provedení. Ve variantách Set, Cup nebo Evo se objevuje v kůži i textilu. Pokud chcete moderněji vypadající silnější podrážku, podívejte se na řadu L003.'),
        ('Jsou Lacoste tenisky vhodné na sport?', 'Většina modelů je určena na každodenní nošení, nikoli na trénink. Některé tenisově laděné kousky, například Power Serve, se ke kurtu vztahují víc, ale pro kvalitní odpružení a stabilitu při sportu je lepší specializovaná obuv.'),
        ('Jak čistit bílé kožené tenisky Lacoste?', 'Použijte měkký kartáč, vlažnou vodu a jemný čisticí prostředek. Skvrny odstraňujte co nejdříve a boty sušte při pokojové teplotě s papírem uvnitř. Před nošením pomůže impregnace, která omezí vsakování špíny.'),
        ('Padnou Lacoste větší, nebo menší?', 'Střihy bývají spíš přiléhavější, a u tuhé kůže proto stojí za to počítat s mírnou rezervou. Změřte chodidlo večer a porovnejte s tabulkou výrobce. Rozhoduje délka vnitřní stélky, ne číslo na krabici.'),
        ('Nabízí Lacoste i dětské tenisky?', 'Ano, v nabídce jsou dětské modely vycházející z populárních dospělých kousků. Kupujte s rezervou asi centimetr, hlídejte pevnou patu a měkký jazyk a velikost kontrolujte po několika měsících nošení.'),
        ('Jak poznat originální Lacoste?', 'Kupujte u prověřených obchodů, kde je uveden úplný název modelu a kód. Pozorně sledujte kvalitu šití, tvar krokodýla a konzistentní označení na vložce. Příliš nízká cena u neznámého prodejce je varovný signál.'),
        ('Hodí se Lacoste tenisky k obleku?', 'Hladké kožené modely v tmavé nebo bílé barvě se hodí k méně formálnímu obleku a k chino kalhotám. Vyhněte se výrazné podrážce a barevným detailům. Při striktním dress codu zůstaňte u klasických polobotek.'),
        ('Vydrží Lacoste tenisky celoroční nošení?', 'Kožené modely při pravidelné péči zvládnou i vlhčí období, ale potřebují impregnaci a sušení. Textilní jsou lehčí a hodí se hlavně na teplejší část roku. Pro zimu a sníh jsou vhodnější boty s odolnější podrážkou.'),
        ('Kde porovnat nabídky Lacoste?', 'Na této stránce vidíte stejný model u více obchodů a můžete porovnat dostupnost velikostí a barev. Hledejte podle názvu a kódu modelu, protože obchody používají mírně odlišné popisy. Sledujte také ročník kolekce.'),
    ],
)

# ------------------------------------------------------------------ nike-sportovni-boty
NEW['nike-sportovni-boty'] = dict(
    title='Nike sportovní boty: běh, kopačky, trénink i basketbal',
    desc='Nike sportovní boty pro běh, fotbal, fitness, basketbal i volný čas. Jak se orientovat v řadách, vybrat velikost, povrch a porovnat nabídky obchodů.',
    intro='<p>Nike nevyrábí jednu sportovní botu, ale celou paletu určenou pro různé disciplíny. V nabídce najdete běžecké boty Pegasus a Quest, trailové Juniper, kopačky Mercurial, Phantom a Tiempo, basketbalové Precision, tréninkové Metcon a také pantofle Victori a tenisky Court Vision. '
          'Tato stránka shrnuje boty Nike z kategorie <a href="/sportovni-obuv/">sportovní obuv</a> a pomáhá vám rozhodnout, která řada patří k vašemu sportu. Průvodce vysvětluje, jak číst názvy a zkratky, jak vybrat velikost a povrch a čím se liší běžecké, fotbalové a tréninkové boty. Pomůže vám také porovnat nabídky českých obchodů a vybrat správný pár pro dospělé i děti, ať už hledáte první běžecké boty, kopačky do klubu nebo obuv do tělocvičny.</p>',
    guide='<h2>Jak se v nabídce Nike zorientovat</h2>'
          '<p>Nike se v e-shopech objevuje ve velkém množství. Nejrychleji se v ní zorientujete podle jména modelu a sportu. Každé jméno patří do jedné disciplíny a ta určuje stavbu, tlumení i podrážku. Ve výsledcích proto vždy sledujte, k čemu je bota určená, ne jen jak vypadá.</p>'
          + T(['Sport', 'Příklady modelů z nabídky', 'Co je typické'], [
              ['Běh po silnici', 'Quest, Downshifter, Revolution, Structure, Run Defy, Zoom Fly', 'tlumená mezipodešev a prodyšný svršek'],
              ['Běh v terénu', 'Juniper Trail', 'výraznější vzorek podrážky a pevnější špička'],
              ['Fotbal', 'Mercurial Vapor, Phantom, Tiempo', 'kolíky nebo výstupky pro daný povrch'],
              ['Basketbal', 'Precision', 'vyšší opora kotníku a pevná podrážka'],
              ['Fitness a trénink', 'Metcon, Air Monarch, Alpha Trainer', 'stabilní podrážka pro zvedání a skupinové cvičení'],
              ['Volný čas', 'Court Vision, Full Force, V5 RNR', 'městský vzhled, každodenní nošení'],
              ['Pantofle a žabky', 'Victori One, Kawa, Sunray Protect, Marina', 'šatna, bazén, léto']]) +
          '<p>Nabídka se mění podle sezón, takže nové ročníky nahrazují starší a stejný název se může u dalšího ročníku lišit konstrukcí. Při porovnání sledujte popis a číslo verze.</p>'
          '<h2>Nike běžecké boty</h2>'
          '<p>Běžecké modely se dělí podle používání. Pro rekreační běh po silnici slouží kategorie jako <a href="/bezecka-obuv/">běžecké boty</a> a z modelů Nike tam patří například Quest, Downshifter nebo Revolution. Jsou lehké, s měkkým odpružením a prodyšným svrškem. Pro svižnější tempo se používají modely s tužší a odrazivější mezipodešví. Trailový Juniper má pevnější špičku a agresivnější vzorek pro hlínu, kořeny a kamení, proto se hodí na lesní cesty. Při běhu po asfaltu ale rychleji ztrácí výstupky a je tvrdší.</p>'
          '<p>Velikost běžecké boty by měla mít před prsty přibližně šířku palce místo. Při doběhu se noha mírně roztáhne a prsty narážejí na špičku. Pokud bota tlačí v délce, u dlouhých běhů se objeví puchýře a černající nehty. Pro lepší srovnání si změřte chodidlo večer a nechte rezervu přibližně centimetr.</p>'
          '<h2>Nike kopačky: povrch rozhoduje</h2>'
          '<p>Kopačky patří k nejznámějším produktům značky. Mercurial je lehká a rychlá, Phantom zaměřený na kontrolu míče a Tiempo klasika z kůže pro pohodlný dotek. Na jiné povrchy se používají jiné podrážky, a to je důležitější než samotný model.</p>'
          '<ul><li><strong>FG:</strong> pevný přírodní trávník, delší kolíky.</li>'
          '<li><strong>MG:</strong> multipovrch, kratší kolíky pro přírodní i umělou trávu.</li>'
          '<li><strong>AG:</strong> umělá tráva, kratší a početnější kolíky.</li>'
          '<li><strong>TF:</strong> umělý povrch typu turf, malé gumové výstupky.</li>'
          '<li><strong>IC:</strong> hala, plochá guma bez kolíků.</li></ul>'
          '<p>Verze Academy a Club jsou určené pro rekreační hráče a mládež, mají odolnější materiál a vyšší tuhost. Elitní verze bývají lehčí a doladěné pro dobré hráče. Rozdíl pro amatérskou hru nebývá zásadní. Důležitější je správné sedření a povrch. Pro děti zvolte Jr. verzi, která je užší a lehčí. Podrobnější nabídky najdete v kategorii <a href="/kopacky/">kopačky</a> a pro hrací halu v <a href="/salova-obuv/">sálové obuvi</a>.</p>'
          '<h2>Trénink, fitness a basketbal</h2>'
          '<p>Trénink v posilovně vyžaduje plochou a stabilní podrážku, aby se váha přenášela rovnoměrně. Metcon je stavěný právě na takové zatížení a hodí se také na skupinová cvičení nebo cross-trénink. Měkká běžecká mezipodešev se při těžkém dřepu propadá a stabilitu zhoršuje. Do posilovny se tak běžecká obuv nehodí. Další tréninkové boty najdete v kategorii <a href="/treninkova-obuv/">fitness a tréninková obuv</a>. Basketbalová řada Precision má vyšší oporu kotníku a pevnou podrážku pro prudké změny směru a doskoky. U kurtů s hladkou podlahou zkontrolujte, zda podrážka nezanechává stopy.</p>'
          '<h2>Pantofle, žabky a tenisky Nike</h2>'
          '<p>Victori One je pantofle do šatny, bazénu i na pláž, lehká a rychle schnoucí. Nejde o botu na dlouhou chůzi. Pro vycházky se hodí tenisky Court Vision a Full Force, které vychází z kurtové obuvi. Více volnočasových modelů najdete v kategoriích <a href="/pantofle-a-zabky/">pantofle a žabky</a> a <a href="/tenisky/">tenisky</a>. U dětí volte podle velikosti, ne podle módy, a hlídejte pevnou patu.</p>'
          '<h2>Velikost a střih Nike</h2>'
          '<p>Velikostní tabulka se může lišit podle řady a ročníku. Měřte tedy délku chodidla a hledejte údaj o délce vnitřní stélky v centimetrech. Při kopání jsou vhodnější přiléhavější boty, u běhu s rezervou. Basketbalové a tréninkové modely mají pevnější střih kolem střední části chodidla. Široké chodidlo oceňuje svršek z pleteniny nebo textilu, tuhá syntetika méně povolí. Pokud nakupujete bez zkoušení, zvažte rozumné vrácení zboží u obchodu.</p>'
          '<h2>Pánské, dámské a dětské boty</h2>'
          '<p>Pánské a dámské verze se liší hlavně šířkou paty a objemem v přední části. Dámské modely jsou užší a mají často nižší tuhost. Označení W v názvu znamená dámskou verzi, Jr nebo GS dětskou. Pro ucelený přehled si otevřete <a href="/panska-sportovni-obuv/">pánskou sportovní obuv</a>, <a href="/damska-sportovni-obuv/">dámskou sportovní obuv</a> a <a href="/detska-sportovni-obuv/">dětskou sportovní obuv</a>, kde je Nike k dispozici vedle dalších značek.</p>'
          '<h2>Boty pro školu, tělocvik a první sport</h2>'
          '<p>Pro děti není nutné pořizovat odborně laděný model hned, ale hlavně správně velkou a pevnou botu. Na školní tělocvik stačí lehká sálová nebo tréninková obuv se světlou podrážkou, která nezanechává stopy na podlaze. Pro dětský fotbal volte Jr. kopačky podle povrchu hřiště, nejčastěji MG nebo AG, a tenisky s tvrdou podrážkou nechte na procházky. Dítě, které běhá pravidelně, ocení pružnější běžeckou botu, ale pro příležitostnou hru stačí obyčejná tréninková. Jedny boty na všechno nedoporučujeme: ve špatném typu klouže, rychle se ničí a může způsobit bolest chodidel.</p>'
          '<ul><li><strong>Pata:</strong> musí držet a nesmí sjíždět, jinak vzniknou puchýře.</li>'
          '<li><strong>Špička:</strong> prsty se mají volně hýbat, ale noha v botě neklouže dopředu.</li>'
          '<li><strong>Šněrování:</strong> suchý zip nebo gumičky usnadní samostatné obouvání u menších dětí.</li>'
          '<li><strong>Pravidelná kontrola:</strong> změřte nohu každé tři až čtyři měsíce, protože dětské chodidlo roste rychle.</li></ul>'
          '<h2>Nike a konkurence</h2>'
          '<p>Pokud chcete porovnat značky, zkuste <a href="/sportovni-boty-adidas/">sportovní boty Adidas</a> nebo <a href="/sportovni-boty-puma/">sportovní boty Puma</a>. Každá značka má jiný střih a jiný charakter podrážky. Nike bývá spojována s odrazivým tlumením a dynamickým vzhledem, Adidas s tradiční sportovní linií a Puma s módnějším vzhledem. Výběr nemá rozhodovat jméno, ale vaše noha a sport. Kompletní přehled výrobků značky je i na stránce ' + B(('nike', 'Nike')) + '.</p>'
          '<h2>Péče o sportovní boty</h2>'
          '<p>Boty po tréninku vyndejte z tašky a nechte vyschnout při pokojové teplotě. Nesušte je na radiátoru, lepidlo i pěna by se poškodily. Vložky občas vyjměte a vyperte, svršek očistěte kartáčem a vlažnou vodou. Běžecké boty střídejte alespoň po dvou párech a po několika stovkách kilometrů sledujte tlumení, které slábne dřív než samotný svršek. Kopačky po zápase očistěte od trávy a bláta a neukládejte je zablácené.</p>'
          '<p>Při výběru počítejte i s ponožkami. Tenká sportovní ponožka a silná zimní mění objem boty natolik, že se rezerva před prsty změní o půl čísla. Na zkoušku si proto vezměte ty, které budete opravdu nosit, a stejné číslo hledejte i při nákupu na dálku. Totéž platí pro vložky: pokud nosíte ortopedické, vyjměte originální a zkuste botu s nimi.</p>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Stejný model je u různých obchodů v různých velikostech. Sporteka vedle sebe ukáže dostupnost a pomůže najít obchod, kde je vaše číslo skladem. Při výběru zkontrolujte popis povrchu u kopaček a sport u ostatních modelů, ať se nespletete s podobně vypadající botou jiné disciplíny.</p>',
    faq=[
        ('Jaké Nike boty zvolit na běhání?', 'Pro běh po silnici se hodí lehké modely s odpružením, třeba Quest, Downshifter nebo Revolution. Pro terén je lepší Juniper Trail s hrubším vzorkem. Vždy kontrolujte rezervu před prsty a velikost podle délky chodidla.'),
        ('Co znamenají FG, MG, AG a TF u kopaček Nike?', 'Je to povrch, pro který je podrážka určená. FG je přírodní tráva, MG multipovrch, AG umělá tráva, TF turf a IC hala. Na špatném povrchu bota klouže nebo přetěžuje klouby, proto značení vždy ověřte.'),
        ('Liší se kopačky Academy a Club od elitních?', 'Ano, Academy a Club jsou odolnější a určené pro rekreační hráče a mládež, elitní verze bývají lehčí a doladěné pro náročné hráče. Pro amatérskou hru je rozdíl menší než správný povrch a velikost.'),
        ('Hodí se běžecké boty do posilovny?', 'Moc ne. Měkká mezipodešev se při zátěži propadá a zhoršuje stabilitu. Do posilovny vyberte tréninkovou obuv s plochou podrážkou, například Metcon, která lépe přenáší váhu při dřepech a zvedání.'),
        ('Jak vybrat správnou velikost Nike bot?', 'Změřte chodidlo večer, porovnejte s tabulkou výrobce a počítejte s rezervou před prsty u běhu. Kopačky bývají přiléhavější. Rozhoduje délka vnitřní stélky v centimetrech, ne číslo, protože tabulky se u řad liší.'),
        ('Je Nike Victori One vhodná na delší chůzi?', 'Ne, je to pantofle do šatny, k bazénu nebo na pláž. Pro delší chůzi je lepší pevná obuv s pevnou patou. Pantofle jsou lehké a rychle schnou, ale chodidlu nedávají oporu.'),
        ('Jak poznám dětskou nebo dámskou verzi?', 'V názvu bývá W pro dámskou, Jr nebo GS pro dětskou verzi. Dámské jsou užší, dětské menší a lehčí. U dětí kupujte s rezervou asi centimetr a velikost kontrolujte častěji, protože noha rychle roste.'),
        ('Jak dlouho vydrží běžecké boty?', 'Záleží na váze, stylu běhu, povrchu a péči. Tlumení slábne dřív než svršek, proto sledujte pocit při došlapu a bolest kloubů. Střídání dvou párů a sušení při pokojové teplotě životnost prodlužuje.'),
        ('Jak porovnat Nike s Adidasem nebo Pumou?', 'Střihy a podrážky se liší, takže stejná velikost může sedět jinak. Podívejte se na tabulku výrobce a recenze k modelu. Důležitější než značka je určení boty pro váš sport a to, jak vám sedí.'),
    ],
)
