"""sporteka.cz - facet landing texts wave 196: lyzaky-tecnica, lyzaky-rossignol, rossignol-bunda, trimm-bunda.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzaky-tecnica
NEW['lyzaky-tecnica'] = dict(
    title='Lyžáky Tecnica: řady Mach a Mach1, flex a objem',
    desc='Lyžáky Tecnica pro muže, ženy i děti: jak číst názvy Mach Sport, Mach1 a BOA, který objem LV, MV a HV zvolit a jaký flex odpovídá vaší technice.',
    intro='<p>Lyžáky Tecnica vyrábí italská firma z okolí Trevisa, která patří do skupiny s dalšími značkami lyžařských bot a zimní obuvi. V nabídce převažují řady Mach Sport, Mach BOA a Mach1 pro rekreační až sportovně laděné lyžaře, k tomu juniorské modely JT a JTR a starší Firebird. '
          'Tecnica staví na pohodlném tvaru vnitřní boty a nabízí tutéž řadu v několika objemech, takže najdete verzi pro štíhlou i širokou nohu. Tato stránka vám pomůže rozluštit čísla a zkratky v názvech, jako jsou 85, 120, MV, HV nebo GW, a vybrat podle vlastní nohy, ne podle barvy skořepiny. '
          'Obecný postup od měření chodidla po péči o boty je v kategorii <a href="/lyzarske-boty/">lyžařské boty</a>.</p>',
    guide='<h2>Jak číst názvy modelů Tecnica</h2>'
          '<p>Značka pojmenovává boty skládačkou, ve které je skryto víc informací, než se zdá. Jakmile se naučíte rozklíčovat název, rychle poznáte, jestli je bota určená vám, nebo třeba špičkovému lyžaři s úzkou nohou.</p>'
          + T(['Část názvu', 'Co znamená', 'Příklad'], [
              ['Mach Sport, Mach1, Mach BOA', 'rodina modelů; liší se výbavou a zaměřením', 'Mach Sport 85, Mach1 120'],
              ['Číslo (65–130)', 'flex, tedy tuhost manžety', 'vyšší číslo = tužší bota'],
              ['LV, MV, HV', 'nízký, střední a vysoký objem vnitřního prostoru', 'Mach1 105 LV, Mach Sport 90 HV'],
              ['W', 'dámský model s upraveným tvarem manžety', 'Mach Sport 75 MV W'],
              ['GW', 'podrážka určená i k chůzi (Grip Walk)', 'Mach Sport 100 MV GW'],
              ['BOA', 'zapínání kolečkem a ocelovým lankem místo části přezek', 'Mach BOA HV 100 GW'],
              ['JT, JTR, Firebird', 'juniorské a dětské boty', 'JT 3, JTR 3, Firebird 90']]) +
          '<p>Označení objemu nepřehlížejte. Právě ono rozhoduje o tom, jestli bota sedí po celém chodidle, nebo tlačí na nártu a ve špičce, zatímco jinde je volno. Dvě boty se stejným číslem flexu a velikostí mohou mít kvůli objemu naprosto odlišný pocit.</p>'
          '<h2>Mach Sport, Mach1 a Mach BOA: kdo je pro koho</h2>'
          '<h3>Mach Sport</h3>'
          '<p>Základní a nejpočetnější řada. Je určená lyžařům, kteří jezdí pro radost, na rodinnou dovolenou i dvakrát týdně, a potřebují teplo, snadné nazouvání a odpouštějící flex. Najdete tu dámské verze s nízkým číslem kolem sedmdesáti i pánské ke stovce. Pro většinu rekreačních lyžařů je to rozumný začátek hledání.</p>'
          '<h3>Mach1</h3>'
          '<p>Vyšší řada zaměřená na přesnější přenos pohybu a přizpůsobení tvaru nohy. U zařazených modelů často uvidíte čísla ke stotřiceti a označení TD. Pokud chcete botu, kterou jde tvarovat v servisu, ptejte se prodejce na konkrétní model, protože možnosti úpravy skořepiny a vnitřní boty se mezi sériemi liší.</p>'
          '<h3>Mach BOA</h3>'
          '<p>Kolečko BOA zapíná botu rovnoměrně a jednou rukou, i v rukavici. Hodí se pro lyžaře, kterým přezky tlačí na holeň, nebo pro ty, kdo chtějí doladit utažení bez shýbání. Nevýhodou je dražší oprava, pokud se lanko poškodí; většina výrobců dodává náhradní díly samostatně, takže se informujte předem.</p>'
          '<h2>Objem LV, MV a HV: jak poznat svůj</h2>'
          '<p>Objem popisuje vnitřní prostor boty, nikoli délku. Do spodní tabulky se dívejte, až budete mít změřenou délku chodidla, protože objem se pak vybírá už jen mezi botami správné velikosti.</p>'
          + T(['Typ nohy', 'Typický příznak', 'Doporučený objem'], [
              ['Štíhlá noha, nízký nárt', 'pata uvnitř klouže, špička se pohybuje', 'LV (nízký)'],
              ['Běžná noha', 'střední šířka metatarzu, normální nárt', 'MV (střední)'],
              ['Široká noha, vyšší nárt', 'tlak na malíku, bolest nártu po hodině', 'HV (vysoký)'],
              ['Silné lýtko', 'manžeta se hůř zapíná u kolen', 'HV a širší zapínání manžety']]) +
          '<p>Při zkoušce platí jednoduché pravidlo: bota se po zapnutí musí cítit těsně, ale nemá bolet. Pata ukotvená vzadu a prsty, které se při předklonu odtáhnou od špičky, jsou správný signál. Nárt, kde cítíte hrany přezek, nebo palec, který ztrácí cit, signalizuje špatný objem.</p>'
          '<h2>Flex a jeho čísla u dámských a pánských bot</h2>'
          '<p>U Tecnicy odpovídá číslo v názvu tuhosti a pánské a dámské hodnoty se nedají přímo porovnávat. Dámské boty mají při stejném čísle obvykle měkčí průběh a nižší, užší manžetu, protože ženské lýtko sedí níž. Žena, která jezdí sportovněji, může klidně sáhnout po pánské botě, pokud jí sedí tvar, a naopak štíhlý muž ocení dámskou. Písmeno W tedy popisuje typ postavy, nikoli pohlaví majitele.</p>'
          + T(['Tvoje jízda', 'Orientační číslo', 'Poznámka'], [
              ['Začátečník, občasný lyžař', '65–85', 'měkký průběh odpouští chyby'],
              ['Rekreační, jezdí s jistotou', '85–100', 'nejčastější volba rodinných lyžařů'],
              ['Pokročilý, rychlejší oblouky', '100–120', 'tuhost vyžaduje aktivní postoj'],
              ['Sportovní jízda, těžší lyžař', '120–130', 'nižší komfort, užší tvar']]) +
          '<p>Hmotnost i výška mění, co je pro vás tuhé. Těžší lyžař prohne bota měkčí a výsledkem je klesající přesnost, lehká lyžařka v příliš tuhé botě se naopak nedostane do předklonu. Raději volte botu o stupeň měkčí, která ještě reaguje, než ukázkově tvrdou.</p>'
          '<h2>Juniorské JT, JTR a Firebird</h2>'
          '<p>U dětí se boty vybírají s ohledem na růst, ale ne příliš velké. Nechte dítě stoupnout do boty se zapnutými přezkami: prsty se mají lehce dotýkat špičky, a po předklonu se odtáhnout. Zhruba o jednu velikost mondopointu za rok roste noha mezi osmi a čtrnácti lety, ale u dětí je to individuální. Starší modely Firebird, které občas v nabídce zůstávají z dřívějších sezón, mají stejnou stavbu, ale starší pěnu a plast; podívejte se na ročník uvedený v názvu. Vyhledávání dětských modelů i od jiných značek je v části <a href="/detske-lyzarske-boty/">dětské lyžařské boty</a>.</p>'
          '<h2>Starší ročníky: na co dát pozor</h2>'
          '<p>V názvu se objevují údaje jako 18/19 nebo 25/26. Značí sezónu, ve které model vyšel. U starších ročníků neměňte velikost podle pocitu z fotky: plast, vnitřní bota i přezky stárnou i v krabici. Nová barva většinou znamená jen vzhled, mechanika a tvar zůstávají stejné, takže starší ročník může být výhodný, pokud nemá viditelné praskliny a přezky drží. Přehled zlevněných modelů nabízí kategorie <a href="/lyzarske-boty-vyprodej/">lyžařské boty výprodej</a>.</p>'
          '<h2>Srovnání s jinými značkami v nabídce</h2>'
          '<p>Rozdíl mezi značkami bývá menší než rozdíl mezi tvary nohou. Proto zkoušejte alespoň dvě až tři značky. Tecnica sdílí skupinu s Nordicou, jejíž modely najdete v části <a href="/lyzarske-boty-nordica/">lyžařské boty Nordica</a>. Pokud hledáte alternativu s francouzským původem, podívejte se na <a href="/lyzaky-rossignol/">lyžáky Rossignol</a>, z rakouských značek na <a href="/lyzarske-boty-atomic/">lyžařské boty Atomic</a> a <a href="/lyzarske-boty-head/">Head</a>. Závodněji naladěné modely jsou v části <a href="/lyzarske-boty-lange/">Lange</a> a <a href="/lyzarske-boty-dalbello/">Dalbello</a>, pohodlné rekreační modely má francouzský <a href="/salomon-lyzarske-boty/">Salomon</a>.</p>'
          '<h2>Nákup na dálku a první zkouška doma</h2>'
          '<p>Boty objednané online vyzkoušejte doma na koberci, v ponožkách, které budete mít na svahu, a nejméně dvacet minut. Zapněte všechny přezky na střední sílu, předkloňte se do postoje a hlídejte tři věci: pata nesmí zvedat, holeň nesmí tlačit na jazyk a prsty nesmí necitlivět. Bota, kterou jste neobuli ani v sedě, by do obchodu měla zpět v původním stavu, proto ji nenoste venku ani po špinavé podlaze. Pokud sedí napoprvé skoro dokonale, bude po prvních dnech na sněhu volná, protože se vnitřní bota ulehne.</p>'
          '<h2>Co ještě patří k výbavě</h2>'
          '<ul><li><strong>Ponožky:</strong> tenké lyžařské ponožky bez švu na holeni, viz <a href="/lyzarske-ponozky/">lyžařské ponožky</a>.</li>'
          '<li><strong>Vázání:</strong> délku podrážky ověřte podle údaje na patě boty; nastavení provádí servis, viz <a href="/lyzarske-vazani/">lyžařské vázání</a>.</li>'
          '<li><strong>Lyže:</strong> sjezdové lyže vybírejte až po botách, viz <a href="/sjezdove-lyze/">sjezdové lyže</a>.</li>'
          '<li><strong>Tour:</strong> chcete-li stoupat s pásy, patří vám spíš <a href="/skialpove-boty/">skialpové boty</a>.</li></ul>'
          '<h2>Péče po sezóně</h2>'
          '<p>Vyndejte vnitřní botu a nechte ji uschnout při pokojové teplotě, ne na topení. Skořepinu zapněte na nejmírnější nastavení a skladujte na suchém místě, ne na půdě, kde teplota kolísá. Podrážku před uložením očistěte od soli a kamínků a před další sezónou ověřte stav přezek. U modelů s kolečkem BOA zkontrolujte lanko, zda se nepoškodilo o hranu, a před dopravou v kufru boty zapněte, aby se přezky nezlomily. V botách nechoďte dlouho po asfaltu, ničí podrážku i patky.</p>',
    faq=[
        ('Jsou lyžáky Tecnica vhodné pro začátečníky?', 'Ano, vyplatí se řada Mach Sport s nízkým číslem flexu, která je pohodlná a odpouští chyby. Začátečník nepotřebuje tuhou botu, spíš dobře sedící a teplou.'),
        ('Jaký je rozdíl mezi Mach Sport a Mach1?', 'Mach Sport cílí na komfort a rekreační lyžování, Mach1 na přesnější přenos pohybu a vyšší tuhost. Mach1 bývá užší a často nabízí možnost úprav tvaru v servisu.'),
        ('Který objem vybrat: LV, MV nebo HV?', 'Podle šířky a výšky nohy. LV je pro štíhlou nohu, MV pro běžnou a HV pro širokou s vyšším nártem. Při pochybnostech zkuste MV a podle pocitu přejděte na další objem.'),
        ('Co znamená GW v názvu?', 'GW značí podrážku s protiskluzovým povrchem, která zlepšuje chůzi. Před koupí si ověřte, že vaše vázání s touto normou pracuje, u běžných sjezdových vázání to obvykle platí.'),
        ('Má smysl dávat přednost botám s BOA?', 'BOA nabízí rychlé a rovnoměrné utažení, a to i v rukavicích. Je to otázka komfortu, ne kvality; pokud vám klasické přezky sedí, přeplácet nemusíte.'),
        ('Jaký flex zvolit u dámských Tecnica?', 'Pro začátečnice zhruba 65–75, pro rekreační lyžařky 75–90, pro sportovní jízdu výš. Rozhoduje i váha: těžší lyžařka potřebuje o něco tužší botu.'),
        ('Jakou velikost vybrat dítěti do JT nebo JTR?', 'Změřte chodidlo v centimetrech a vyberte odpovídající mondopoint. Prsty se mají lehce dotýkat špičky, po předklonu se odtáhnou. Příliš velké boty dítěti sklouznou a zhorší ovládání lyží.'),
        ('Dá se lyžařská bota roztáhnout, když tlačí?', 'V servisu lze skořepinu místně rozšířit nebo upravit vnitřní botu, ale pomáhá to jen v řádu několika milimetrů. Když bota tlačí na celém chodidle, zvolte jiný objem nebo velikost.'),
        ('Jak poznám ročník modelu?', 'Ročník bývá v názvu jako dvojčíslí, například 25/26, nebo v popisu produktu. Bez údaje se ptejte obchodu. Starší ročník je v pořádku, pokud je plast celý a přezky drží.'),
        ('Mohu Tecnica kombinovat s libovolným vázáním?', 'Pro klasické sjezdové vázání potřebujete normovanou podrážku. Boty s režimem chůze a hybridní modely mají jiné patky, proto před koupí ověřte typ podrážky a nechte vázání nastavit v servisu.'),
    ],
)

# ------------------------------------------------------------------ lyzaky-rossignol
NEW['lyzaky-rossignol'] = dict(
    title='Lyžáky Rossignol: Alltrack, Vizion, Pure a dětské',
    desc='Lyžáky Rossignol pro muže, ženy a děti: čím se liší řady Alltrack, Vizion 4B, Pure a Speed, kdy sáhnout po BOA a jak vybrat flex, objem i velikost.',
    intro='<p>Rossignol je francouzská značka z Voironu, která začínala na lyžích a dnes dělá i boty, vázání a oblečení. V nabídce lyžáků Rossignol se potkávají čtyři větší sjezdové řady: všestranné Alltrack, sportovnější Vizion 4B, dámské Pure a rychlé Speed a Hi-Speed. Přidávají se dětské Comp J a Hero J a pár běžkařských modelů X-6 a X-11. '
          'Většina bot nese v názvu číslo tuhosti a objem MV nebo HV, takže se v nich snadno ztratíte. Průvodce níže vysvětluje, kterou řadu zvolit podle stylu jízdy, čím se liší verze s BOA a jak pracovat s objemem, aby bota po hodině na svahu neškrtila. Základ o měření a stavbě bot je v kategorii <a href="/lyzarske-boty/">lyžařské boty</a>.</p>',
    guide='<h2>Řady Rossignol a komu se hodí</h2>'
          '<p>Rossignol nepoužívá jedno jméno pro všechno, jednotlivé série mají jasný charakter. Když víte, co od ní čekáte, vypadne vám z výběru polovina nabídky.</p>'
          + T(['Řada', 'Charakter', 'Hodí se pro'], [
              ['Alltrack', 'všestranná, pohodlná, často s kolečkem BOA nebo režimem chůze', 'lyžaře v areálu i mimo upravené tratě'],
              ['Vizion 4B', 'přesnější a užší, vyšší tuhost, verze Pro a Elite', 'pokročilé a sportovně jedoucí lyžaře'],
              ['Pure', 'dámská řada s upraveným tvarem lýtka', 'ženy, jejichž lýtko sedí níž a užší'],
              ['Speed a Hi-Speed', 'plnohodnotná jízdní bota pro rychlé oblouky', 'lyžaře, kteří chtějí rychlou reakci'],
              ['Comp J a Hero J', 'dětské a juniorské boty, od měkkých po tužší', 'děti od prvních lyží po závodní tréninky'],
              ['X-6, X-11', 'běžkařské boty klasické a pro bruslení', 'lyžování v běžecké stopě']]) +
          '<p>Nespoléhejte na hrubé dělení na pánské a dámské. Řada Pure má sice ženský střih, ale Alltrack i Vizion nabízejí také modely s písmenem W, a naopak štíhlý muž se může cítit lépe v modelu bez označení pro ženy. Řídí se především tvar nohy a technika jízdy.</p>'
          '<h2>Alltrack: všestranná volba</h2>'
          '<p>Alltrack je nejrozšířenější řada. V názvech najdete čísla od sedmdesáti po sto třicet, takže pokrývá začátečnici na výletě i zkušeného lyžaře s tvrdším postojem. Řada klade důraz na pohodlí při chůzi a při sezení na lanovce. Modely s kolečkem BOA zapnete jednou rukou, i když se vám v rukavici nedaří přezkám. Verze Pro jsou o něco užší a sportovnější. Alltrack je dobrá volba, pokud jezdíte celý den a odpoledne nechcete mít otlačenou holeň.</p>'
          '<h2>Vizion 4B a Pure: přesnost nebo ženský střih</h2>'
          '<p>Vizion 4B stojí o schod výš: bota je přesnější a tužší, takže se do ní vyplatí investovat, jakmile už dobře ovládáte oblouky a chcete víc vnímat hranu. Ženy najdou stejný charakter u modelů s písmenem W v názvu. Řada Pure je přímo dámská. Nabízí nižší manžetu a obvykle také teplejší vnitřní botu, v názvech se objevuje i slovo Heat nebo Comfort. Při jízdě pomáhá užší lýtko, bota nepřitlačí v kolenou. Naopak ženy se silným lýtkem často raději sáhnou po pánské verzi s větší manžetou.</p>'
          '<h2>Speed a Hi-Speed</h2>'
          '<p>Speed míří na lyžaře, kteří chtějí reagovat přímo a bez prodlevy. Typické jsou nižší objemy a vyšší čísla tuhosti, u kterých už nejde o pohodlí, ale o přenos pohybu. Hi-Speed přidává do téže řady modely s kolečkem BOA. Před koupí si uvědomte, že tuhá bota nemusí vylepšit jízdu, pokud ještě nemáte tělo na dostatečně aktivní postoj. Zhodnoťte to upřímně a raději začněte o stupeň měkčí.</p>'
          '<h2>Objem MV a HV a jak ho vybrat</h2>'
          '<p>Rossignol označuje objem zkratkami MV a HV, tedy střední a vysoký. Jde o rozdíl ve vnitřním prostoru, nikoli ve velikosti. Většina lidí s běžnou nohou si poradí s MV, vyšší nárt a širší přední část chodidla ocení HV. Pokud je bota po zapnutí všude těsná, ale pata se zvedá, je pravděpodobně malá nebo příliš tuhá. Pokud se tlačí jen malík a boky chodidla, jde o šířku, ne délku, a pomůže jiný objem nebo servisní úprava.</p>'
          + T(['Problém v botě', 'Pravděpodobná příčina', 'Řešení'], [
              ['Pata se zvedá', 'bota je příliš velká nebo málo objemná u kotníku', 'menší velikost nebo užší objem'],
              ['Tlak na nártu', 'malý objem nebo příliš pevně dotažená přezka', 'HV, měkčí jazyk, povolit přezku'],
              ['Bolest malíku', 'úzký skelet', 'servisní roztažení nebo širší model'],
              ['Studené prsty', 'těsná špička, špatné ponožky', 'o půl čísla větší, tenká ponožka'],
              ['Obtlačená holeň', 'špatně nastavený postoj nebo příliš tuhá manžeta', 'měkčí flex, kontrola nastavení']]) +
          '<h2>Dětské boty Comp J a Hero J</h2>'
          '<p>Dětské modely mají měkčí průběh a přezky, které zvládne ovládat dítě samo. Označení J a číslo za ním řadí boty podle úrovně: nižší pro nejmenší, vyšší pro pokročilejší, s užším tvarem a větší tuhostí. Dětská noha roste skokově, proto zkoušejte, zda se palec jen lehce dotýká špičky, a nekupujte boty o dvě čísla větší. Starší ročníky z výprodeje jsou v pořádku, pokud je plast celý a přezky drží. Přehled dětských modelů všech značek je v části <a href="/detske-lyzarske-boty/">dětské lyžařské boty</a>.</p>'
          '<h2>Rossignol a běžecké lyžování</h2>'
          '<p>Pod stejným jménem najdete i boty X-6 pro klasickou stopu a X-11 pro bruslení. Klasická bota je nižší a ohebnější, aby se při odrazu uvolnila pata. Bruslařská má vyšší manžetu, která podepírá kotník. Musí navíc pasovat do vašeho vázání, protože systémy NNN a SNS se liší. Podrobnosti k tomu najdete v kategoriích <a href="/bezecke-boty/">boty na běžky</a> a <a href="/bezecke-lyze/">běžecké lyže</a>, nabídku značky k běžkám shrnuje <a href="/bezky-rossignol/">běžky Rossignol</a>.</p>'
          '<h2>Jak zjistit velikost podle chodidla</h2>'
          '<p>Postavte se bosou patou ke zdi na list papíru, označte nejdelší prst a změřte vzdálenost od zdi. Výsledek v centimetrech je výchozí mondopoint a při nákupu ho porovnejte s tabulkou výrobce. Měřte večer, kdy je noha nejširší, a obě nohy zvlášť; lyžařská bota se vybírá podle větší z nich. Pokud jste mezi velikostmi, zvolte menší: vnitřní bota se rozlehá a prostor v ní pak odpovídá, kdežto příliš velkou botu už nezmenšíte. Nezapomeňte na lyžařskou ponožku, protože silná froté ponožka velikost nezvýší, jen zhorší cirkulaci krve.</p>'
          '<h2>Teplo, zapínání a dlouhý den na svahu</h2>'
          '<p>Studené nohy bývají důsledkem těsné boty, ne slabé izolace. Přezky zapínejte od špičky k holeni a nad nártem je utáhněte slaběji než u kotníku. Při přejezdu lanovkou a na oběd je klidně povolte, noha se pak lépe prokrví. Nezapomeňte, že se při chůzi bota ohýbá jinak než při jízdě, proto s uvolněnými přezkami jděte pomalu. Model s tepelnou úpravou nebo vyhříváním má smysl pro lidi, kteří mrznou opravdu často; ostatním obvykle stačí dobře sedící bota a vlněná ponožka.</p>'
          '<h2>Rossignol vedle konkurence</h2>'
          '<p>Víc než logo rozhoduje vaše noha, a proto stojí za to vyzkoušet vedle sebe dvě značky. Italský protějšek najdete v části <a href="/lyzaky-tecnica/">lyžáky Tecnica</a>, další francouzskou volbou je <a href="/salomon-lyzarske-boty/">Salomon</a>. Z rakouských firem jsou k dispozici <a href="/lyzarske-boty-head/">Head</a> i <a href="/lyzarske-boty-atomic/">Atomic</a>. Máte-li zájem o sladěnou výbavu, na stejné značce lze stavět i při výběru lyží, viz <a href="/rossignol-lyze/">lyže Rossignol</a>. Na úplném začátku si ujasněte rozdělení podle pohlaví v částech <a href="/panske-lyzarske-boty/">pánské lyžařské boty</a> a <a href="/damske-lyzarske-boty/">dámské lyžařské boty</a>.</p>'
          '<h2>Dámské a pánské modely v jedné řadě</h2>'
          '<p>U Rossignolu často najdete stejný model ve dvou verzích, třeba Alltrack 90 pro muže a Alltrack 90 W pro ženy. Liší se výškou a tvarem manžety, často barvou, někdy i vnitřní botou. Dámská varianta bývá o kousek měkčí při stejném čísle a pánská má vyšší manžetu. Pokud vám na jedné z nich vadí lýtko, zkuste druhou. Mezi ženami i muži existují lyžaři, kterým sedí opačná varianta, a nic tomu nebrání.</p>'
          '<h2>Na co se zeptat před objednávkou</h2>'
          '<ul><li><strong>Délka podrážky:</strong> údaj v milimetrech slouží servisu pro nastavení vázání.</li>'
          '<li><strong>Typ podrážky:</strong> klasická, nebo s protiskluzovou vložkou pro chůzi.</li>'
          '<li><strong>Možnosti úprav:</strong> zda lze skořepinu rozšířit a vnitřní botu tvarovat.</li>'
          '<li><strong>Ročník:</strong> v názvu bývá sezóna, starší kusy posuzujte podle stavu plastu.</li>'
          '<li><strong>Doplňky:</strong> <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/lyzarske-vazani/">vázání</a> dokončí výbavu.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi Alltrack a Vizion 4B?', 'Alltrack je všestrannější a pohodlnější, pokrývá široké rozpětí tuhosti. Vizion 4B je přesnější, užší a míří na lyžaře, kteří chtějí vnímat hranu a umějí si s tužší botou poradit.'),
        ('Pro koho je řada Pure?', 'Pure je dámská řada s upraveným tvarem manžety a vnitřní boty. Hodí se ženám s užším lýtkem, ale rozhoduje, jak vám bota sedí, ne jen označení.'),
        ('Co znamená MV a HV u Rossignolu?', 'MV je střední objem a HV vysoký. Objem určuje prostor kolem nártu a přední části chodidla. Při stejné délce chodidla zvolte HV, pokud boty tlačí na nártu nebo na malíku.'),
        ('Má smysl kupovat boty s BOA?', 'BOA se hodí, pokud chcete rychle a rovnoměrně dotáhnout botu jednou rukou. Nepřidává přesnost jízdy, takže jde o komfort a pohodlí zapínání, nikoli o výkon.'),
        ('Jaký flex vybrat pro pokročilého lyžaře?', 'Zhruba 100–120 u pánských a 90–105 u dámských bot. Při větší hmotnosti nebo agresivní jízdě výš. Měkčí bota je vždy lepší než příliš tuhá, kterou nedokážete prohnout.'),
        ('Jakou velikost vybrat dítěti do Comp J nebo Hero J?', 'Změřte chodidlo v centimetrech a vyberte odpovídající mondopoint, bez velké rezervy. Prsty se mají mírně dotýkat špičky, po předklonu se odtáhnou. Příliš velká bota zhoršuje ovládání lyží.'),
        ('Jsou boty Rossignol vhodné na chůzi?', 'Záleží na podrážce. Modely se vložkou nebo režimem chůze jsou pohodlnější při přesunech po areálu, klasické jsou určené hlavně do vázání.'),
        ('Dají se Rossignol boty upravit v servisu?', 'Ano, servis umí skořepinu v některých místech rozšířit a vnitřní botu přizpůsobit. Nejlépe to funguje na úrovni milimetrů; špatná velikost se opravit nedá.'),
        ('Kdy se vyplatí kupovat lyžařské boty?', 'Nejširší výběr velikostí bývá na začátku sezóny, zatímco ke konci zimy zůstávají hlavně okrajová čísla. Pokud máte běžnou velikost, najdete výhodnější kusy v průběhu sezóny, u neobvyklé velikosti je lepší nečekat. Boty si doma vyzkoušejte hned po doručení.'),
        ('Na jaké vázání pasují běžecké boty X-6 a X-11?', 'Záleží na systému vázání, nejčastěji NNN nebo SNS. Boty a vázání musí být ze stejného systému, jinak se neuchytí. Údaj najdete v popisu produktu.'),
    ],
)

# ------------------------------------------------------------------ rossignol-bunda
NEW['rossignol-bunda'] = dict(
    title='Rossignol bunda: softshell, péřové a hybridní modely',
    desc='Rossignol bundy a vesty: softshell Genetys, hybridní Classique, péřové Opside i běžecké kousky. Jak vybrat střih, vrstvy a velikost podle použití.',
    intro='<p>Rossignol je ve světě lyží známý dávno, ale jeho oblečení nosí lidé už i mimo svah. Bundy této značky vznikly z lyžařských potřeb, proto se v nabídce střídají softshell Genetys, hybridní Classique, péřové a izolační Opside, tenké střední vrstvy Thin Midlayer, běžecké bundy Poursuite a lifestylové kousky jako Shiny Bomber. '
          'Společné mají sportovní střih, nízkou váhu a důraz na pohyblivost paží. Průvodce vysvětluje, co která řada nabízí, kdy bunda spíš zateplí a kdy chrání před větrem a jak určit velikost, aby se vešla vrstva pod ní. Širší přehled typů je v kategorii <a href="/sportovni-bundy/">sportovní bundy a vesty</a>, nabídku značky najdete i v <a href="/znacka/rossignol/">katalogu značky</a>.</p>',
    guide='<h2>Co Rossignol vyrábí v bundách</h2>'
          '<p>Katalog obsahuje několik řad, které na první pohled vypadají podobně, ale slouží k odlišným věcem. Než porovnáte dva kusy, zjistěte, do které skupiny patří.</p>'
          + T(['Řada nebo typ', 'Co to je', 'Hodí se na'], [
              ['Genetys', 'softshellová bunda, pružná, odolá větru a lehkému dešti', 'podzimní a jarní túry, každodenní nošení'],
              ['Classique Hybrid', 'kombinace materiálů na trupu a na bocích', 'chladné dny při pohybu'],
              ['Opside', 'péřová a outdoorová bunda nebo vesta', 'zimní procházky, lyžařská izolační vrstva'],
              ['Thin Midlayer', 'tenká střední vrstva s kapucí', 'pod větrovku, jako samostatná bunda v mírnějším počasí'],
              ['Poursuite, Sidelhorn', 'lehké běžecké bundy', 'běh, běžky, rychlá aktivita'],
              ['Shiny Bomber, Joseray', 'módní a volnočasové střihy', 'město a každodenní oblékání'],
              ['Wispile a dětské kousky', 'dětské zimní a přechodné bundy', 'děti na svahu i ve škole']]) +
          '<p>Slova v názvu dávají jen přibližnou představu. Vždy si přečtěte, z čeho je bunda ušita a jak je tlustá, protože i bunda označená jako sportovní může být do mrazu příliš slabá.</p>'
          '<h2>Genetys: softshell, který se hýbe s vámi</h2>'
          '<p>Softshell je pružná tkanina s hladkým povrchem a měkčí vnitřní stranou. Nezastaví vodu stejně jako pláštěnka, ale vítr zadrží a lehký déšť nechá steče. U Genetys obvykle poznáte, že je bunda střižená tak, aby se paže zvedala bez zadrhávání. Je to dobrý kus pro lidi, kteří chodí svižně a nechtějí se zpotit pod neprodyšnou membránou. Do vytrvalého lijáku ale vezměte raději nepromokavou vrstvu, viz <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/nepromokave-bundy/">nepromokavé bundy</a>.</p>'
          '<h2>Classique Hybrid: dva materiály v jednom</h2>'
          '<p>Hybridní bunda spojuje na jednom kuse dvě konstrukce. Na hrudi a zádech bývá izolace, která drží teplo, na bocích a pod pažemi pružný materiál, který dovolí pohyb. Takový střih vám vyhoví, pokud potřebujete zahřát trup, ale nechcete se pod rukávy zapařit. Při koupi zjistěte, jakou výplň bunda má a zda je izolace syntetická nebo prachová, protože se podle toho liší péče i chování za vlhka.</p>'
          '<h2>Opside a péřové modely</h2>'
          '<p>Pod jménem Opside se v nabídce objevují péřové bundy, outdoorové bundy a vesty pro muže i ženy. Péřová izolace nabízí vysoké teplo při nízké hmotnosti a bunda se dobře sbalí. Naopak když péří zvlhne, izolace slábne a schne pomalu. Proto se péřová bunda hodí do suchého mrazu, kdežto na mokrý sníh je lepší syntetika. Dámské péřové modely s názvy jako Aretu nebo Chavanette zapadají do kategorie <a href="/zimni-bundy/">zimní a péřové bundy</a>. Chcete-li zahřát jen trup, zvolte vestu z kategorie <a href="/sportovni-vesty/">vesty</a>.</p>'
          '<h2>Tenká střední vrstva Thin Midlayer</h2>'
          '<p>Thin Midlayer je lehká bunda s kapucí, kterou lze nosit samostatně i pod větrovkou. Dá se tak sestavit tříkomponentní systém: funkční triko, tenká bunda a svrchní vrstva proti větru. V chladném suchém dnu stačí sama. Při vyšší aktivitě si zapínáním zipu nastavíte teplotu bez svlékání. Ze všech kusů v nabídce se nejlépe skládá s ostatními, proto je dobrým prvním nákupem pro lidi, kteří teprve skládají vrstvy.</p>'
          '<h2>Lyžařská izolace a bundy pro svah</h2>'
          '<p>Na sjezdovce se nosí kombinace tří vrstev: spodní prádlo, střední vrstva a svrchní lyžařská bunda s membránou. Kusy Rossignol z této nabídky jsou často vhodné jako teplé střední vrstvy pod lyžařskou bundu nebo na lanovku. Plnohodnotné lyžařské bundy se zalepenými švy a sněhovou sukní najdete v části <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>. Další užší výběr značky nabízí stránka <a href="/rossignol-lyzarska-bunda/">Rossignol lyžařská bunda</a>. Podle pohlaví se rozdělují <a href="/panska-lyzarska-bunda/">pánské lyžařské bundy</a> a <a href="/damska-lyzarska-bunda/">dámské lyžařské bundy</a>.</p>'
          '<h2>Vrstvení v zimě: co kam patří</h2>'
          '<p>Při chůzi na zimní procházce se tělo zahřívá, a proto bunda, která vás ve stoji zahřeje, při chůzi zapaří. Nejlepší je vrstvit a upravovat. Základ tvoří prádlo, které odvádí pot, další vrstva zadržuje vzduch a svrchní kus chrání před větrem. U značky Rossignol můžete sestavit takový systém z jednoho katalogu, ale funguje to i smíšeně s jiným oblečením.</p>'
          + T(['Činnost', 'Střední vrstva', 'Vnější vrstva'], [
              ['Rychlá chůze, běh', 'jen funkční triko', 'lehká běžecká nebo softshellová bunda'],
              ['Pomalá procházka v mrazu', 'tenká mikina nebo Thin Midlayer', 'péřová nebo hybridní bunda'],
              ['Lyžování', 'střední izolační vrstva nebo vesta', 'lyžařská bunda s membránou'],
              ['Čekání, fotografování', 'teplejší vrstva', 'péřová bunda s kapucí']]) +
          '<p>Při přechodu z tepla do chladu si zapamatujte jednoduché pravidlo: začněte lehce oblečeni a vrstvu přidejte, jakmile se zastavíte. Vesta a bunda se zipem až ke krku dovolují regulovat teplotu bez svlékání.</p>'
          '<h2>Jak určit velikost bundy</h2>'
          '<p>Změřte obvod hrudníku v nejširším místě, pas a délku rukávu od ramenního švu k zápěstí. Hodnoty porovnejte s tabulkou značky, protože velikost M není u všech výrobců stejná. Sportovní střih bývá přiléhavější než městský, takže rozhodněte, zda pod bundu oblékáte jen triko, nebo i mikinu či péřovou vestu.</p>'
          + T(['Co pod bundou', 'Doporučení', 'Poznámka'], [
              ['Jen funkční triko', 'vaše běžná velikost', 'přiléhavá, nic nevlaje'],
              ['Fleece nebo tenká mikina', 'běžná velikost nebo volnější střih', 'rukávy nesmí šponovat'],
              ['Péřová vesta nebo svetr', 'o velikost větší', 'ověřte šířku ramen'],
              ['Lyžařská vrstva pod lyžařskou bundou', 'střední vrstva ve vaší velikosti', 'nesmí se mačkat pod pažemi']]) +
          '<p>U dámských modelů sledujte délku trupu: ženy s kratším torzem často raději volí kratší střih, delší zakryje boky při sezení. U mužů vyšší postavy stojí za to ověřit délku rukávů, protože u sportovního střihu jsou o něco kratší.</p>'
          '<h2>Pánský a dámský střih</h2>'
          '<p>Dámské bundy mají užší ramena, tvarovaný pas a kratší trup, pánské rovnější střih a širší ramena. V nabídce se pánské modely jako Thin Midlayer vyskytují v několika barvách a velikostech, dámské jako Genetys v odstínech, které se liší od mužských. U obou platí, že rozhoduje pohodlí v ramenou a délka rukávů, a ne označení. Pokud se vám dámská bunda zdá příliš přiléhavá, zvažte pánskou, a naopak.</p>'
          '<h2>Dětské kusy a ochranná vesta</h2>'
          '<p>Dětské bundy Rossignol, například řada Wispile, jsou střihem blízké dospělým, jen s upravenou délkou. Pozor ale na produkt Flexvent Vest Kid: je to ochranná vesta s chráničem zad pro děti na lyžích, nikoli zateplená vesta. Nosí se pod bundou a doplňuje helmu, nenahrazuje ji. Dětskou bundu vybírejte s rezervou v rukávech, ale ne příliš velkou, aby se neplétla do lyží.</p>'
          '<h2>Jak hledat modely v obchodech</h2>'
          '<p>Obchody pojmenovávají stejné zboží různě. Setkáte se s názvy jako „Bunda Rossigno“ nebo „Rossignol Bunda“ bez modelu, proto si vždy ověřte typ a popis. Barva i střih se u téhož jména mění podle sezóny. Vyplatí se zadat model, a ne jen značku, a porovnat několik obchodů.</p>'
          '<h2>Značka v porovnání s dalšími</h2>'
          '<p>Rossignol vychází z lyžařské tradice, takže bundy mívají štíhlejší sportovní střih. Pokud hledáte spíš turistickou odolnost, podívejte se na <a href="/the-north-face-bunda/">The North Face</a>, pro větší výběr cenových hladin na <a href="/kilpi-bunda/">Kilpi</a>, <a href="/hannah-bunda/">Hannah</a> nebo <a href="/alpine-pro-bunda/">Alpine Pro</a>. Český výrobce sportovního oblečení najdete u <a href="/trimm-bunda/">bund Trimm</a>. Jarní a podzimní kousky jsou v části <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, lehké kousky v části <a href="/vetrovky/">větrovky</a>.</p>'
          '<h2>Péče a impregnace</h2>'
          '<p>Perte podle štítku, s jemným prostředkem bez aviváže, protože aviváž ničí prodyšnost a impregnaci. Péřové bundy se suší s tenisovými míčky v sušičce, aby se peří nepolepilo. Když voda přestane stékat a rozlévá se po tkanině, obnovte impregnaci sprejem nebo prostředkem do pračky. Zip občas ošetřete a bundu skladujte zavěšenou, ne stlačenou na dně batohu.</p>',
    faq=[
        ('Je bunda Rossignol vhodná i mimo lyžování?', 'Ano. Softshell Genetys, bundy Opside i tenké Thin Midlayer se nosí na turistiku a do města. Plnohodnotné lyžování vyžaduje bundu s membránou a sněhovou sukní.'),
        ('Co je softshellová bunda Genetys?', 'Je to pružná bunda s větruodolným povrchem a měkkým vnitřkem. Hodí se na svižnou chůzi a chladnější dny, ne na vytrvalý déšť.'),
        ('Jak se liší hybridní bunda od normální?', 'Hybridní bunda kombinuje na jednom kuse materiály s izolací a pružné panely pro pohyb. Zahřeje trup, ale nezapaří pod rukávy.'),
        ('Je péřová bunda lepší než syntetická?', 'Péří je při stejném teple lehčí a lépe se sbalí, ale slabě snáší vlhko. Syntetická výplň drží teplo i za vlhka a snadněji se pere.'),
        ('Do jaké teploty bunda Opside hřeje?', 'Výrobci se liší, proto se řiďte popisem konkrétního modelu a tím, jak se hýbete. Při chůzi stačí tenčí kus a pod něj funkční triko, při stání se hodí tlustší.'),
        ('Jakou velikost vybrat, když pod bundu nosím mikinu?', 'Zvolte stejnou velikost, pokud je střih volný, nebo o jednu větší u přiléhavého. Rukávy se po zvednutí paží nesmí zvedat k loktům a ramena nesmí tlačit.'),
        ('Jak poznám, jestli je bunda dámská?', 'V názvu bývá slovo dámská nebo písmeno W. Dámské střihy mají užší ramena, tvarovaný pas a kratší trup než pánské.'),
        ('Nahradí ochranná vesta Flexvent zimní bundu?', 'Ne. Flexvent Vest Kid je ochranná vesta s chráničem zad. Zahřívat bundou musíte dál a vesta se nosí pod ni.'),
        ('Jak bundu pereme a kdy obnovit impregnaci?', 'Perte na doporučenou teplotu bez aviváže. Jakmile se voda přestane srážet do kapek a vsakuje do tkaniny, obnovte impregnaci prostředkem do pračky nebo sprejem.'),
        ('Proč jsou některé nabídky označeny „Rossigno“?', 'Jde o zkrácený název v nabídce obchodu. Podle popisu a fotografie zjistíte, o jaký model se jedná, a pomůže i hledání podle názvu řady.'),
    ],
)

# ------------------------------------------------------------------ trimm-bunda
NEW['trimm-bunda'] = dict(
    title='Trimm bunda: softshell a sportovní bundy pro muže i ženy',
    desc='Bundy Trimm pro muže, ženy i děti: jak číst názvy Lady a JR a barevné kombinace, kdy zvolit softshell, větrovku či zimní bundu a jak určit velikost.',
    intro='<p>Trimm je česká značka sportovního oblečení, která je známá hlavně cyklistickými a outdoorovými kousky. V nabídce bund se opakují jména jako Erwi, Roche, Honor, Mark, Zenon, Vario nebo Exped a mnohá z nich existují ve dvou verzích: pánské a dámské s dovětkem Lady, dětské s JR. '
          'Názvy modelů toho o použití prozradí málo, takže se ve výběru snadno ztratíte. Tento průvodce vás provede tím, jak ze jména, popisu a barevné kombinace poznat typ bundy, kdy zvolit softshell a kdy větrovku nebo zimní kus a jak vybrat velikost. Všeobecný rozcestník je v kategorii <a href="/sportovni-bundy/">sportovní bundy a vesty</a>, nabídku značky najdete i v <a href="/znacka/trimm/">katalogu Trimm</a>.</p>',
    guide='<h2>Jak číst názvy Trimm</h2>'
          '<p>Obchody uvádějí Trimm bundy podle jednotného vzoru: značka, model, případně přípona pohlaví či věku a pak barvy oddělené lomítkem. Pokud znáte schéma, zorientujete se během vteřiny.</p>'
          + T(['Část názvu', 'Význam', 'Příklad'], [
              ['Jméno modelu', 'řada nebo střih, často jedno slovo', 'Zenon, Roche, Honor, Mark'],
              ['Lady', 'dámská verze se střihem pro ženy', 'Roche Lady, Honor Lady'],
              ['Koncovka -a', 'někdy označuje dámský protějšek modelu', 'Zenon a Zenona, Foxter a Foxtera'],
              ['JR', 'junior, dětská velikostní řada', 'Erwi Hard JR'],
              ['Barvy za lomítkem', 'hlavní a doplňková barva panelů či vložek', 'orange / grafit black'],
              ['Označení Pánská, Dámská', 'doplňuje obchod, ne výrobce', 'Trimm Mark Pánská bunda']]) +
          '<p>Nechte se vést popisem v nabídce a ne jen jménem. Stejný model se může v různých sezónách objevit v jiném provedení, takže ověřte materiál, výplň a zda se jedná o bundu, nebo kus na zip s kapucí.</p>'
          '<h2>Sportovní odkaz značky: kolo a pohyb venku</h2>'
          '<p>Trimm vychází z cyklistického prostředí, což se promítá do střihu. Cyklistické bundy bývají vzadu delší, aby zakryly záda v předklonu, a rukávy mají dost dlouhé pro natažené ruce na řídítkách. Výrazné barvy se hodí do silničního provozu, kde záleží na viditelnosti. Pokud tyto prvky nepotřebujete, hodí se stejné kusy i na výlet nebo do města, jen rukávy a záda nemusí být tak výrazně prodloužené. Zkuste zvedat ruce nad hlavu a předklonit se, ať vidíte, kde bunda uhýbá.</p>'
          '<h2>Softshell: nejčastější typ v nabídce</h2>'
          '<p>Mnoho Trimm bund, od Erwi po Honor, patří do skupiny softshellů. Softshell je pružný, větruodolný a příjemně hřeje, ale není to plnohodnotná pláštěnka. V zimě se hodí jako střední vrstva, na jaře a na podzim jako svrchní. Jakmile hrozí vytrvalý déšť, vezměte nepromokavou vrstvu. Širší výběr typů najdete v částech <a href="/softshellove-bundy/">softshellové bundy</a>, <a href="/softshellova-bunda-panska/">pánská softshellová bunda</a>, <a href="/damska-softshellova-bunda/">dámská softshellová bunda</a> a <a href="/detska-softshellova-bunda/">dětská softshellová bunda</a>.</p>'
          '<h2>Větrovky a lehčí bundy</h2>'
          '<p>Pro rychlý pohyb se hodí lehčí bunda z hustě tkaného materiálu, která zastaví vítr a vejde se do kapsy nebo do batohu. Tenký kus potřebujete při jízdě z kopce na kole, při chladném ránu nebo při přechodu hřebene. Hledejte ty, které mají zip až ke krku, manžety, které se neroztahují, a stahování v pase. Další možnosti jsou v kategoriích <a href="/vetrovky/">větrovky a šusťákové bundy</a> a <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>.</p>'
          '<h2>Zimní varianty</h2>'
          '<p>Pokud je mráz, softshell nestačí a pod něj nebo místo něj potřebujete izolaci. V nabídce Trimm najdete spíš bundy pro pohyb než těžké zimní kabáty, takže počítejte s vrstvením: funkční triko, flísová nebo prošívaná vrstva a svrchní bunda proti větru. Čistě zimní modely porovnáte v části <a href="/zimni-bundy/">zimní a péřové bundy</a>, podle pohlaví v částech <a href="/panska-zimni-bunda/">pánská zimní bunda</a> a <a href="/damska-zimni-bunda/">dámská zimní bunda</a>.</p>'
          '<h2>Detaily, které rozhodují při používání</h2>'
          '<p>Bundu tvoří i drobnosti, které na obrázku nevidíte. Na kole se vyplatí kapsa na zádech, do které sáhnete i s rukavicemi na řídítkách. Při chůzi vám víc posloužily kapsy na zip v bocích, přístupné i s popruhy batohu. Kapuce se při jízdě pod přilbou zvedá, proto ji zvolte stahovací, nebo vůbec žádnou. Zip s krytkou chrání před vlhkostí, ale zhoršuje prodyšnost. Manžety na suchý zip nebo gumičku pomáhají utěsnit rukáv pod rukavicí.</p>'
          '<ul><li><strong>Reflexní prvky:</strong> hodí se, pokud se pohybujete za šera mezi auty.</li>'
          '<li><strong>Větrací otvory:</strong> zip pod paží umožní odvětrat teplo bez svlékání.</li>'
          '<li><strong>Límec:</strong> vyšší chrání krk, ale u kapuce se při otáčení hlavy může tlačit.</li>'
          '<li><strong>Délka u pasu:</strong> delší záda zakryjí ledviny při předklonu.</li></ul>'
          '<h2>Vrstvení podle ročního období</h2>'
          + T(['Období', 'Pod bundou', 'Typ bundy'], [
              ['Jaro a podzim, 8–15 °C', 'tričko s dlouhým rukávem', 'softshell nebo lehká bunda'],
              ['Studené ráno, kolem nuly', 'funkční triko a flís', 'softshell s podšívkou'],
              ['Mráz při pohybu', 'funkční prádlo a tenká izolace', 'zateplená bunda s kapucí'],
              ['Deštivý den', 'lehká vrstva', 'nepromokavá bunda']]) +
          '<p>Teploty v tabulce berte orientačně, protože každý člověk vnímá chlad jinak a záleží na tempu. Dobrým pravidlem je, že na začátku cesty vám má být lehce chladno, zahřejete se během několika minut.</p>'
          '<h2>Výběr podle činnosti</h2>'
          '<p>Stejnou bundu nejde vždy použít na všechno, ale u univerzálních modelů je kompromis rozumný. Podívejte se, co hlavně děláte, a podle toho si určete priority.</p>'
          + T(['Činnost', 'Na co dbát', 'Typ bundy'], [
              ['Silniční a horské kolo', 'delší záda, větruodolnost, reflexní detaily', 'lehký softshell nebo větrovka'],
              ['Túra a procházky', 'kapsy dostupné pod batohem, kapuce', 'softshell s kapucí'],
              ['Každodenní nošení', 'střih, barva, prodyšnost', 'softshell, jarní a podzimní kus'],
              ['Pozdní podzim a zima', 'izolace a odolnost větru', 'zateplená bunda s vrstvou pod ní'],
              ['Děti ve škole a na hřišti', 'odolnost, pračka, volnost pohybu', 'JR softshell']]) +
          '<p>Chcete-li víc kusů do roka, kupujte nejprve univerzální softshell a teprve potom doplňujte lehkou větrovku a zimní vrstvu. Bunda, která se používá často, se vyplatí víc než specializovaná, která zůstává ve skříni.</p>'
          '<h2>Pánský a dámský střih</h2>'
          '<p>Dámská varianta Lady je užší v ramenou, tvarovaná v pase a kratší v trupu. Pánská má rovnější střih. Rozdíl pocítíte nejvíc na ramenou a v délce rukávů. Pokud se vám žádné označení nehodí, zkuste opačné pohlaví, protože na štíhlé muže mohou lépe padnout dámské kousky a na vyšší ženy pánské. U cyklistiky je užitečné prověřit délku zad, u túry spíš šířku ramen.</p>'
          '<h2>Jak určit velikost</h2>'
          '<p>Změřte obvod hrudníku, pasu a boků a porovnejte s tabulkou výrobce. Je-li mezi dvěma velikostmi, zvolte větší, pokud nosíte pod bundou vrstvu, a menší, pokud jde o přiléhavý kus. Zvedněte ruce nad hlavu: když se spodní okraj zvedne nad pas, je bunda krátká.</p>'
          + T(['Zkouška', 'Správně', 'Špatně'], [
              ['Zvednuté ruce', 'rukávy zůstanou u zápěstí', 'rukávy vyjedou k loktům'],
              ['Předklon', 'záda jsou zakrytá', 'ledviny odkryté'],
              ['Zapnutý zip až ke krku', 'límec nedrásá bradu', 'škrtí a tlačí'],
              ['Překřížení rukou', 'ramena se nezadrhávají', 'bunda tlačí v podpaží']]) +
          '<h2>Dětské bundy JR</h2>'
          '<p>U modelů označených JR, třeba Erwi Hard JR, je střih upravený pro děti: kratší rukávy, užší ramena a barvy bez výrazné stylizace. Děti rostou, ale bunda s velkým předstihem jim padá z ramen a ruce vyčnívají z rukávů. Vybírejte velikost, která se nosí letos, s malou rezervou v rukávech, a v případě potřeby ji doplňte teplou vrstvou.</p>'
          '<h2>Barvy a viditelnost</h2>'
          '<p>Trimm používá dvoubarevné kombinace, které vypadají sportovně a jsou dobře vidět. Červená, oranžová a žlutá zaujmou řidiče a turisty, zatímco tmavě modrá, černá a khaki působí nenápadněji a méně se špiní. V městském provozu a za šera se hodí jasné barvy, při procházce lesem tlumené.</p>'
          '<h2>Jak Trimm vychází vedle dalších značek</h2>'
          '<p>Trimm je rozumná volba pro ty, kdo chtějí českou značku zaměřenou na pohyb. Na turistiku a horskou turistiku se podívejte také na <a href="/hannah-bunda/">bundy Hannah</a>, <a href="/kilpi-bunda/">Kilpi</a> či <a href="/alpine-pro-bunda/">Alpine Pro</a>, pro sportovní a cyklistický styl na <a href="/silvini-bunda/">Silvini</a>, pro snow sporty na <a href="/rossignol-bunda/">Rossignol</a>. Chcete-li prémiové outdoorové značky, srovnejte s <a href="/the-north-face-bunda/">The North Face</a>.</p>'
          '<h2>Péče o bundu</h2>'
          '<p>Perte na doporučenou teplotu a bez aviváže, protože ta ucpává póry látky. Zapněte všechny zipy, aby se nepoškodily. Sušte na vzduchu, ne na radiátoru. Pokud voda přestává perlit, obnovte impregnaci prostředkem do pračky.</p>',
    faq=[
        ('Co znamená Lady v názvu bundy Trimm?', 'Je to dámská verze modelu se střihem upraveným pro ženy: užší ramena, tvarovaný pas a kratší trup. Funguje jako dámský protějšek pánského modelu.'),
        ('Co znamená JR u dětských bund?', 'JR je zkratka pro junior. Bundy s tímto označením mají střih a velikosti pro děti a mládež, tedy kratší rukávy a užší ramena.'),
        ('Je bunda Trimm vhodná na kolo?', 'Značka vychází z cyklistického prostředí, takže řada modelů má prodloužená záda a delší rukávy. Konkrétní vlastnosti ověřte v popisu každého kusu.'),
        ('Je softshell dostatečně nepromokavý?', 'Zadrží vítr a lehký déšť, ale při vytrvalém lijáku promokne. Pro takové počasí vezměte nepromokavou bundu s membránou nebo ji dejte přes softshell.'),
        ('Stačí Trimm bunda do zimy?', 'Samotný softshell ne. Do mrazu k němu přidejte funkční prádlo a teplou střední vrstvu nebo zvolte zateplený model.'),
        ('Jakou velikost zvolit, pokud jsem mezi dvěma?', 'Při přiléhavém střihu větší, pokud se pod bundou nosí vrstva. Pokud je střih volný, vyberte menší, jinak bude vlát a ztratí tvar.'),
        ('Jak poznám dámský a pánský model u stejného jména?', 'Dámská verze nese slovo Lady nebo často koncovku -a (například Zenon a Zenona). Pánská verze bývá bez dovětku, ale obchod může doplnit slovo pánská.'),
        ('Jak se starat o softshell?', 'Perte jemně a na nižší teplotu, bez aviváže. Bundu sušte na vzduchu. Pokud voda přestane stékat, obnovte impregnaci sprejem nebo přípravkem do pračky.'),
        ('Jakou barvu vybrat do města a jakou do přírody?', 'Do dopravy, na kolo a za šera jasné barvy: červená, oranžová nebo žlutá. Na lesní stezky a do práce tmavé tóny, které se méně špiní.'),
        ('Do jaké teploty se hodí softshell?', 'Záleží na podšívce a tempu. Tenký kus funguje od jara do podzimu, hrubší s podšívkou i kolem nuly při pohybu. Při stání se vrstvěte více.'),
    ],
)
