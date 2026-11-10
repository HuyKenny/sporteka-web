"""sporteka.cz — wave 24k (5. 11. 2026): long texts for nizke-trekove-boty, pristresky-a-party-stany, skialpove-vazani, bezecke-opasky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ nizke-trekove-boty
NEW['nizke-trekove-boty'] = dict(long=True,
    title='Nízké trekové boty: výběr, membrána, podrážka, péče',
    desc='Nízké trekové boty a outdoorová obuv pod kotník. Jak vybrat podle terénu, membrány, podrážky a velikosti a porovnat nabídky českých obchodů.',
    intro='<p>Nízké trekové boty sahají pod kotník, váží méně než vysoké modely a hodí se na výlety, kde nenesete těžký batoh a stezka je udržovaná. Jsou lehké, dobře větrají a mají dost přilnavou podrážku na kořeny, štěrk i mokrou trávu. Na Sportece porovnáváme nabídky českých obchodů u pánských, dámských i dětských modelů, od odvětrávané sportovní obuvi po boty s membránou do deště.</p>'
          '<p>V kategorii najdete značky ' + B(('columbia', 'Columbia'), ('head', 'Head'), ('regatta', 'Regatta'), ('salomon', 'Salomon'), ('adidas', 'Adidas'), ('merrell', 'Merrell'), ('helly-hansen', 'Helly Hansen'), ('kilpi', 'Kilpi')) +
          '. Pro náročnější terén se podívejte na <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>, pro rychlý pohyb na <a href="/trailove-boty/">trailové boty</a> a pro obecný přehled do <a href="/trekova-obuv/">trekové obuvi</a>.</p>',
    guide='<h2>Pro koho jsou nízké trekové boty</h2>'
          '<p>Nízký střih vyhovuje lidem, kteří chodí po značených cestách, po horských loukách, po lesních cestách a po městě s přesahem do přírody. Kotník zůstává volný, takže se pohybuje přirozeněji a noha se tolik nepotí. Kdo nosí těžký batoh nebo chodí po kamenitých hřebenech, ocení spíš vyšší kotník, protože ten pomáhá při šlápnutí vedle a drží nohu při sestupu s nákladem.</p>'
          '<p>Nízké boty si oblíbí také rodiny s dětmi. Děti rychle vyrostou, takže se nevyplatí sahat po nejtužších modelech, ale po lehké obuvi s protiskluzovou podrážkou a pohodlným zapínáním. V kategorii jsou dětské modely například od značek Salomon a Adidas.</p>'
          '<h2>Typy obuvi v kategorii</h2>'
          '<p>Pod pojmem nízké trekové boty se skrývá několik poměrně odlišných druhů. Než začnete porovnávat jednotlivé kusy, ujasněte si, ke kterému z nich se přikláníte.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Odvětrávané outdoorové tenisky', 'síťovina, lehká konstrukce, rychle schnou', 'léto, suché stezky, cestování'],
              ['Boty s membránou', 'voděodolná vložka, plnější svršek', 'proměnlivé počasí, deštivé dny'],
              ['Vycházkové outdoorové boty', 'měkčí střih, kůže nebo textil, jednoduché šněrování', 'procházky, město, lehké výlety'],
              ['Přístupové boty', 'lepivá podrážka, zpevněná špička', 'skalnaté pěšinky, ferraty a krátké přístupy'],
              ['Vodní a drenážní boty', 'otvory pro odtok vody, drží na mokrém', 'brody, kaňony, potoky'],
              ['Dětské trekové boty', 'zesílená špička, suchý zip nebo gumičky', 'rodinné výlety a školní akce']]) +
          '<p>Modely Columbia Vapor Vent patří do první skupiny, tedy odvětrávaných bot. Řada Peakfreak naopak míří k členitějšímu terénu a Drainmaker XTR je určena pro vodu. Regatta nabízí v kategorii lehké pohodlné boty i verze s membránou, značka Head spíš městské a vycházkové provedení.</p>'
          '<h2>Svršek: kůže, nubuk, textil</h2>'
          '<p>Materiál svršku ovlivňuje váhu, trvanlivost i nároky na péči. Textilní a síťované boty jsou nejlehčí a rychle schnou, ale odírají se o ostrý kámen. Kůže a nubuk vydrží víc, hřejí a lépe odolávají vlhkosti, ovšem po zmoknutí schnou pomalu a vyžadují impregnaci a vosk nebo sprej. U kombinací kůže s textilem získáte kompromis, při němž kůže chrání exponovaná místa a síťovina odvětrává zbytek.</p>'
          '<p>Pozor na tvrzení, že je bota „nepromokavá“. Voděodolná úprava svršku zpomalí promáčení, kdežto membrána tvoří souvislou vrstvu uvnitř. Žádná bota ale nezůstane suchá, když voda nateče shora přes nízký nártový otvor. Proto se při brodění nebo v hlubokém mokrém porostu hodí spíš boty, které rychle schnou, než membrána, v níž se voda zachytí.</p>'
          '<h2>Membrána, nebo bez ní</h2>'
          '<p>Membrána propouští vodní páru zevnitř ven a bránit by měla průniku kapek zvenčí. Pomáhá v dešti, v mokré trávě a při chůzi po tajícím sněhu. Za to platíte menší prodyšností, takže v horku bývá noha teplejší a vlhčí. Boty bez membrány jsou vzdušnější a po zmoknutí rychleji schnou. Pro letní výlety a cestování po suchých oblastech jsou často lepší volbou, pro podzim a jaro na nich oceníte spíš membránu.</p>'
          + T(['Kritérium', 'S membránou', 'Bez membrány'], [
              ['Déšť a mokrá tráva', 'lepší ochrana', 'noha promokne dříve'],
              ['Teplo a prodyšnost', 'méně vzdušné', 'vzdušné'],
              ['Schnutí po promočení', 'pomalejší', 'rychlé'],
              ['Vhodná sezóna', 'jaro, podzim, proměnlivo', 'léto, suchá krajina'],
              ['Váha', 'o něco vyšší', 'nižší']]) +
          '<h2>Podrážka a protiskluz</h2>'
          '<p>Podrážka rozhoduje o jistotě na mokrém kamenu a zemi. Hluboký vzorek s ostrými hranami drží v blátě a trávě, ale rychleji se obrušuje na asfaltu. Hladší vzorek s měkčí směsí lépe přilne na skále a v městském provozu. Podrážka se má ohýbat v místě prstů; v nerovném terénu ale potřebuje větší tuhost uprostřed. Pro terén se hodí podrážka, která se prohýbá ve správném místě, ale nepřekládá se na hraně.</p>'
          '<p>Důležité je i odpružení. Tlumicí mezipodešev z pěny zlepšuje komfort při delších túrách po tvrdých cestách. Příliš měkká mezipodešev ovšem na nerovném povrchu nestabilizuje nohu. Při výběru si proto boty vyzkoušejte na šikmé ploše, kterou obvykle mívá obchod, nebo je poctivě otestujte doma na schodech.</p>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Boty zkoušejte odpoledne, kdy je noha mírně oteklá, a v ponožkách, které na túrách nosíte. Prsty se nesmí dotýkat špičky ani při sestupu, před palcem by měl zůstat zhruba šířka palce prostoru. Pata nemá při došlapu vyskakovat a šněrování musí jít dotáhnout bez bolesti na nártu. Šířku nohy nelze „rozchodit“ donekonečna, takže jestli bota tlačí do stran už v obchodě, vyberte jiný střih nebo značku.</p>'
          '<p>Velikostní řady se mezi výrobci liší a dámské modely mívají užší patu a nižší objem. Pánské a dámské varianty jsou v kategorii označeny v názvu produktu, u dětských se držte délky chodidla a nechte rezervu na růst, ale ne více než pár milimetrů, aby dítě nezakopávalo.</p>'
          '<h2>Co obout k botám</h2>'
          '<p>Správné ponožky ovlivní komfort víc než další přeplatek za botu. Tenká, bezešvá ponožka z umělého vlákna nebo vlny zabrání puchýřům. Bavlna nasákne potem a zůstává mokrá, proto se na túry nehodí. Podívejte se do <a href="/sportovni-ponozky/">sportovních ponožek</a> a <a href="/merino-ponozky/">merino ponožek</a>, které lépe regulují teplotu a nezapáchají.</p>'
          '<p>K nízké obuvi doplňte lehké <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, při dešti <a href="/nepromokave-bundy/">nepromokavou bundu</a> a na delší túry <a href="/turisticke-batohy/">turistický batoh</a>. Po strmých cestách pomohou <a href="/trekove-hole/">trekové hole</a>, protože odlehčí kolenům a stabilizují krok.</p>'
          '<h2>Péče o boty</h2>'
          '<p>Po túře vyndejte vložky a boty nechte schnout při pokojové teplotě. Radiátor, kamna ani auto na slunci nepoužívejte, protože lepidla ztvrdnou a kůže popraská. Vyčistěte hrubé bláto kartáčem a vlažnou vodou, bez agresivních čisticích prostředků. Nubuk a kůži pak ošetřete vhodným přípravkem, textilní svršek obnoví impregnační sprej. Boty s membránou perte jen podle návodu výrobce, aby se nezanesly póry membrány.</p>'
          '<p>Vyměňujte tkaničky, když jsou rozedrané, a kontrolujte spojení podrážky a svršku. Pokud se podrážka odlepuje, nechte ji spravit dřív, než se z ní stane problém uprostřed túry. Vložky se opotřebují dřív než zbytek boty, a je-li noha unavená už po krátké chůzi, vyplatí se je vyměnit. Výběr najdete v <a href="/doplnky-k-obuvi/">doplňcích k obuvi</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě boty o půl čísla menší „aby držela“. Při sestupu pak naráží prsty do špičky.</li>'
          '<li>Výběr membrány do horka a opačně: lehkou síťovinu na podzimní blátivé stezky.</li>'
          '<li>Ignorování hmotnosti batohu. Nízká bota nemusí stačit při nákladu, který zatěžuje kotníky.</li>'
          '<li>Zkoušení bot jen na hladké podlaze. Zkuste sejít z rampy nebo schodů.</li>'
          '<li>Nošení nových bot rovnou na dlouhou túru. Rozchoďte je na krátkých vycházkách.</li>'
          '<li>Zanedbání impregnace. Nová kůže i textil se po čase vlhkosti poddají.</li></ul>'
          '<h2>Kdy zvolit něco jiného</h2>'
          '<p>Chodíte-li často po kamenitých stezkách s větším batohem, zvažte <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>. Při rychlých túrách a běhu v přírodě sáhněte po <a href="/trailove-boty/">trailových botách</a>, které jsou lehčí a mají agresivnější vzorek. Kdo hledá přirozený krok a minimální tlumení, projde si <a href="/barefoot-obuv/">barefoot obuv</a>, ale přechod na ni musí být pozvolný. Pro vodní aktivity máte k dispozici <a href="/obuv-do-vody/">obuv do vody</a> a v zimě <a href="/nesmeky/">nesmeky</a>, které se navlékají na boty při chůzi po ledu.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Sporteka sama neprodává. Ukazuje, které obchody mají konkrétní model a velikost, a vede vás na jejich stránky. Filtrujte podle značky, velikosti a barvy a zkontrolujte dostupnost přímo u prodejce. U bot se vyplatí obchod s pohodlným vrácením nebo výměnou, protože jistotu o tvaru nohy a střihu získáte až doma. Stejný model může existovat v několika barvách a mírně se lišit materiálem, proto si před objednáním přečtěte popis a rozměry.</p>',
    faq=[('Jaký je rozdíl mezi nízkými a vysokými trekovými botami?', 'Nízké končí pod kotníkem, jsou lehčí a vzdušnější. Vysoké kotník obepínají, lépe jej chrání a hodí se pro těžší batoh a kamenitý terén.'),
         ('Hodí se nízké trekové boty do deště?', 'Zvládnou běžný déšť, pokud mají membránu nebo voděodolný svršek. Při brodění nebo hlubokém mokrém porostu ale voda přeteče přes nártový otvor.'),
         ('Mám volit boty s membránou?', 'Na jaro, podzim a proměnlivé počasí ano. V létě a na suchých stezkách jsou vzdušnější boty bez membrány pohodlnější a rychle schnou.'),
         ('Jak poznám správnou velikost?', 'Zkoušejte odpoledne v ponožkách, které na túry nosíte. Před palcem má zůstat prostor, pata nesmí vyskakovat a nárt nesmí tlačit.'),
         ('Dají se nízké boty používat i ve městě?', 'Ano, mnoho modelů je vycházkových a v městském provozu je podrážka pohodlná. Hrubý vzorek se ale rychleji obrušuje na asfaltu.'),
         ('Jak často boty impregnovat?', 'Podle používání a materiálu, obvykle při první ztrátě perlení vody. Textil a kůži ošetřete přípravkem určeným pro daný materiál.'),
         ('Jak sušit zmoklé boty?', 'Vyndejte vložky, uvolněte tkaničky a nechte boty schnout při pokojové teplotě. Vyhněte se radiátoru a přímému slunci, aby nepopraskala kůže a nezměkla lepidla.'),
         ('Hodí se tyto boty pro děti?', 'Ano. Dětské modely mají zesílenou špičku a snadné zapínání. Vybírejte podle délky chodidla s malou rezervou a kontrolujte velikost každou sezónu.'),
         ('Mohu v nich jít na hřebenovou túru?', 'Na udržovaných hřebenech ano, pokud nenesete těžký náklad. U kamenitých a exponovaných úseků je jistější vyšší bota s tužší podrážkou.'),
         ('Co s botami po sezóně?', 'Očistěte je, nechte vyschnout, vložte do nich papír, aby držely tvar, a uložte na suché větrané místo mimo topení.'),
         ('Kde zjistím nabídku konkrétní značky?', 'V kategorii použijte filtr značky. Sporteka ukáže, které obchody mají vybraný model a velikost a odkáže vás na jejich stránky.')],
)

# ------------------------------------------------------------------ pristresky-a-party-stany
NEW['pristresky-a-party-stany'] = dict(long=True,
    title='Přístřešky a párty stany: velikost, stěny, kotvení',
    desc='Párty stany, zahradní altány, přístřešky ke stanu a plážové stíny. Jak vybrat velikost, stěny, konstrukci a kotvení a porovnat obchody.',
    intro='<p>Přístřešek nebo párty stan nahrazuje střechu tam, kde není: na zahradní oslavě, na trhu, u chaty, na pláži nebo před vchodem do stanu v kempu. Nejde o lehký turistický stan na spaní, ale o konstrukci, která poskytuje stín a závětří pro stůl, kuchyňku nebo jen pro rodinu s židlemi. Sporteka porovnává nabídky českých obchodů u skládacích pavilonů s nůžkovou konstrukcí, párty stanů se stěnami, přístřešků ke stanům i plážových stínidel.</p>'
          '<p>V kategorii najdete značky ' + B(('springos', 'Springos'), ('king-camp', 'King Camp'), ('trimm', 'Trimm'), ('coleman', 'Coleman'), ('husky', 'Husky'), ('skandika', 'Skandika'), ('high-peak', 'High Peak'), ('quechua', 'Quechua')) +
          '. Na spaní se hodí <a href="/stany/">stany</a>, na pláž <a href="/pop-up-a-plazove-stany/">pop-up a plážové stany</a> a na rodinný kemp <a href="/rodinne-stany/">rodinné stany</a>.</p>',
    guide='<h2>Co se pod pojmem přístřešek skrývá</h2>'
          '<p>Kategorie sdružuje výrobky se společnou funkcí, ale různou konstrukcí. Než začnete porovnávat rozměry, rozhodněte se, zda potřebujete konstrukci na jednu akci, na celou sezónu, nebo doplněk k už vlastněnému stanu.</p>'
          + T(['Druh', 'Popis', 'Typické použití'], [
              ['Skládací párty stan (nůžkový)', 'ocelová nebo hliníková konstrukce, rychlé postavení', 'trhy, oslavy, firemní akce'],
              ['Párty stan se stěnami', 'střecha plus boční plachty s okny nebo dveřmi', 'zahradní party, svatby, zázemí na celý den'],
              ['Pavilon s pevnou střechou a rámem', 'stabilnější, těžší, často s větrací nástavbou', 'trvalejší využití na zahradě'],
              ['Přístřešek ke stanu', 'plachta navazující na tunelový stan', 'předsíň, kuchyně, stín před stanem'],
              ['Přístřešek na pláž nebo sluneční clona', 'lehké tyče, textilie s UV úpravou', 'pláž, hřiště, rodinný výlet'],
              ['Ložnice k párty stanu', 'vnitřní stan, který se vkládá pod střechu', 'přespání pod velkým stanem']]) +
          '<p>V nabídce jsou například párty stany Springos o půdorysu 3×3 m i 3×6 m, pavilony High Peak, modely Coleman Event Shelter nebo přístřešky Trimm a Husky, které slouží jako zastřešení před vchodem do stanu. Přístřešky pro tunelové stany jsou výrazně specifické: musí odpovídat šířce a výšce stanu, jinak voda stéká do mezery mezi nimi.</p>'
          '<h2>Rozměr a kapacita</h2>'
          '<p>Nejběžnější půdorys je 3×3 m, který zakryje stůl se šesti až osmi židlemi nebo malou skupinu stojících hostů. Typ 3×6 m pojme dvě řady stolů nebo bufet. Pro větší akce se spojují dva stany vedle sebe. Při plánování počítejte s tím, že se pod střechou nesmí tísnit a že boční stěny zmenšují použitelný prostor uvnitř.</p>'
          '<p>Důležitá je také výška boků a středu. Nízké vchody omezují vysoké hosty a při vstupu s tácem je nepohodlná, zatímco příliš vysoký střed nabízí vítr hodně plochy. Zjistěte si výšku okapové hrany, nejen výšku vrcholu. Při přepravě ověřte i rozměr složené konstrukce: dlouhé zavazadlo se do menšího auta nemusí vejít.</p>'
          '<h2>Konstrukce a materiál rámu</h2>'
          '<p>Rám bývá z lakované oceli, hliníku nebo kombinace. Ocel je pevná a levnější, ale těžší a při poškrábání lakování rezne. Hliník je lehčí, nekoroduje, ale snáz se ohne. Zajímejte se o průřez trubek a počet nohou. Čtyři nohy stačí na 3×3 m, ale u 3×6 m je třeba šest nebo více a rozumná je i výztuha uprostřed. Pevnější a tlustší profil snese vítr lépe než elegantní tenké trubky.</p>'
          '<p>Nůžkové konstrukce se rozkládají jednoduše a postaví je dvě osoby. Musí mít pojistky, které drží rám v rozloženém stavu. Kolíky na spojích si prohlédněte: tenké plastové díly jsou nejčastějším místem selhání. Pevné pavilony se skládají z jednotlivých dílů a stavba trvá déle, ale vydrží silnější zátěž.</p>'
          '<h2>Střecha: plachta, voděodolnost a UV</h2>'
          '<p>Většina střech je z polyesteru s polyuretanovou nebo PVC vrstvou. Označení vodního sloupce u levnějších modelů je spíš orientační. Střecha by měla mít zatavené švy nebo je přelepené páskou, jinak průsak nastává právě v nich. UV úprava chrání textilii před vyblednutím a zabraňuje propouštění slunečního záření, ale po několika sezónách se účinnost snižuje.</p>'
          '<p>Důležité jsou také okapy a sklon. Plochá střecha zadržuje vodu, na které se tvoří kapsy. Zdvižený střed a sklon do stran umožňují odtok. Po dešti plachtu vždy vytřepejte, jinak se zkrátí její životnost. Přítomnost větracích otvorů na vrcholu snižuje nárazy větru pod střechou a zlepšuje cirkulaci vzduchu v horkých dnech.</p>'
          '<h2>Stěny, okna a vchody</h2>'
          '<p>Boční plachty mění otevřený stín v uzavřený prostor. Mají různé varianty: plné, s okny, s dveřmi na zip nebo se síťkou proti hmyzu. Plné stěny chrání před deštěm a větrem, ale zvyšují zátěž při poryvech, protože se z altánu stane plachta. Při bouřce a silném větru je vhodné je spustit nebo odepnout. Síťové stěny jsou praktické večer, kdy se pod stanem rozsvítí světla a lákají hmyz.</p>'
          '<h2>Kotvení a bezpečnost při větru</h2>'
          '<p>Párty stany jsou při větru riziko, proto je vždy ukotvěte. I lehký poryv může nadzvednout konstrukci, pokud není ukotvená. Na trávě a hlíně použijte pevné kolíky a lana přes každý roh. Na dlážděném povrchu a betonu je třeba závaží, které se připevní na každou nohu. Kolíky a závaží tvoří samostatnou položku, takže si je pročtěte v nabídce a zvolte z kategorie <a href="/stanove-kolky/">stanové kolíky</a> a <a href="/stanove-doplnky/">stanové doplňky</a>.</p>'
          '<p>Platí jednoduché pravidlo: jakmile vítr sílí, stan se sklopí nebo sundá střecha. Nikdy nenechávejte stan postavený a bez dozoru při předpovědi bouře. Volné párty stany bez ukotvení mohou ublížit lidem, proto výrobci uvádějí maximální odolnost jen při dodržení kotvicího návodu. Neupínejte lana přes volný prostor, o který lidé zakopnou, a označte je například barevnou páskou.</p>'
          '<h2>Přístřešky ke stanům: na co dát pozor</h2>'
          '<p>Přístřešek pro tunelový stan, například typu Gotland, se připíná k obloukům a ke vchodu stanu. Funguje jako zastřešená předsíň, kde se vaří, odkládají boty a chrání zavazadla. Musí sedět na stan určitého typu, proto se nenakupuje podle obrázku, ale podle rozměrů vchodu. Spoj mezi stanem a přístřeškem utěsněte přeložením plachty, jinak se déšť protlačí dovnitř.</p>'
          '<p>Vaření pod uzavřenou střechou má svá pravidla. Plynový ani jiný vařič nepoužívejte uvnitř stanu s uzavřenými stěnami, protože hrozí otrava oxidem uhelnatým a požár. Pro větraný přístřešek, otevřený alespoň z jedné strany, platí obezřetnost a bezpečná vzdálenost od plachty. Vybavení najdete v kategorii <a href="/kemping/">kemping</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>.</p>'
          '<h2>Plážové a sluneční přístřešky</h2>'
          '<p>Plážové modely jsou lehké a skladné, často s UV filtrem. Nemají jen chránit před sluncem, ale také před větrem, k čemuž slouží boční klapky a vak na písek. Písek drží stan lépe než kolíky, které v něm snadno povolí. Husky, Mckinley nebo Caperlan nabízejí takové modely a vedle nich existují i větší sluneční clony pro rodiny. Další možnosti najdete v <a href="/pop-up-a-plazove-stany/">pop-up a plážových stanech</a> a v <a href="/plazove-doplnky/">plážových doplňcích</a>.</p>'
          '<h2>Příslušenství a vybavení pod střechou</h2>'
          '<p>Pod přístřeškem se obvykle sedí a jí. Připravte <a href="/kempingovy-nabytek/">kempingový nábytek</a>, <a href="/bivaky-a-kresla/">skládací křesla</a> a <a href="/chladici-boxy/">chladicí box</a> na nápoje. Do stínu patří i <a href="/hamaky/">hamak</a>, pokud je prostor dost velký, ale zavěšujte ho jen na pevné stromy nebo sloupky, nikdy na rám party stanu. Pro děti připravte <a href="/hry-na-zahradu/">hry na zahradu</a> mimo hlavní provoz. Na spaní pod velkým stanem se vkládají <a href="/karimatky-a-matrace/">karimatky a matrace</a>.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po akci stan důkladně vysušte, jinak se objeví plíseň, a očistěte rám od hlíny. Nesušte jej složený, rozložte plachty a nechte je odvětrat. Zkontrolujte pružiny, kloubové spoje a konec trubek, a lehce je promažte silikonovým sprejem. Střechu skladujte vcelku a ne smotanou na ostrém ohybu, aby se nelámala vrstva. Uchovávejte v původním obalu na suchém místě mimo slunce.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Podcenění větru: přístřešek bez ukotvení a závaží je nebezpečný.</li>'
          '<li>Koupě podle plochy bez ověření výšky a váhy složeného balení.</li>'
          '<li>Spoléhání na označení vodního sloupce u levných střech, které nezahrnuje švy.</li>'
          '<li>Použití zahradního altánu na kemp, i když není určen k častému skládání.</li>'
          '<li>Nákup přístřešku ke stanu bez kontroly, zda je kompatibilní s tvarem a šířkou stanu.</li>'
          '<li>Uložení mokré plachty do vaku, kde se za týden ujme plíseň.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Sporteka nabídky shromažďuje, ale nic neprodává. U každého modelu zkontrolujte rozměr, rám, materiál střechy a to, zda jsou stěny součástí balení nebo se kupují zvlášť. Mezi cenovými nabídkami se často vyskytují zboží s označením druhé jakosti, které může mít drobné vady na obalu nebo plachtě, takže si přečtěte popis. Před koupí zvažte, jak často stan postavíte: na jednu akci ročně stačí lehčí konstrukce, pro častější použití se vyplatí pevnější rám.</p>',
    faq=[('Jaký rozměr párty stanu zvolit?', 'Pro menší zahradní akci stačí 3×3 m. Pro dvě řady stolů nebo bufet se hodí 3×6 m. Počítejte s volným místem pro pohyb hostů.'),
         ('Unese párty stan vítr?', 'Jen s pevným ukotvením. Na trávě použijte kolíky a lana, na dlažbě závaží u každé nohy. Při silném větru stan sklopte nebo sundejte střechu.'),
         ('Je střecha opravdu nepromokavá?', 'Záleží na textilii a švech. Hledejte zatavené nebo přelepené švy a po dešti plachtu vytřepejte, ať se nevytvářejí kapsy s vodou.'),
         ('K čemu slouží boční stěny?', 'Chrání před deštěm, větrem a pohledy a s okny a síťkami vytvoří uzavřený prostor. Při silném větru je spusťte nebo odepněte.'),
         ('Hodí se párty stan na kemp?', 'Dá se použít jako společný stín, ale je těžší a rozměrnější než turistické stany. Pro cesty autem je to možné, pro přenášení ne.'),
         ('Jak zvolit přístřešek ke stanu?', 'Podle typu a šířky stanu. Tunelový přístřešek se připíná k obloukům a musí mít odpovídající rozměry vchodu, jinak teče voda do mezery.'),
         ('Smím vařit pod přístřeškem?', 'Pouze v dobře větraném prostoru bez uzavřených stěn a v bezpečné vzdálenosti od plachty. Uvnitř uzavřeného stanu vařit nelze kvůli otravě oxidem uhelnatým a požáru.'),
         ('Jak údržbu provádět po akci?', 'Stan vysušte rozložený, očistěte rám a promažte klouby silikonovým sprejem. Skladujte suché a mimo slunce, plachtu neskládejte na ostrý ohyb.'),
         ('Rozdíl mezi přístřeškem a plážovým stanem?', 'Plážový stan má lehké tyče a UV textilii, často s vakem na písek. Přístřešek a párty stan jsou větší a robustnější, s kovovým rámem.'),
         ('Může stan zůstat celé léto venku?', 'Doporučeno není. UV záření, déšť a vítr zkracují životnost plachty i rámu. Při trvalém použití zvolte pevnější pavilon a v bouřkách jej sklopte.'),
         ('Co znamená druhá jakost u přístřešku?', 'Zboží může mít drobné vady, například poškozený obal. Zkontrolujte popis obchodu a vyzkoušejte stan po doručení, abyste mohli včas reklamovat.')],
)

# ------------------------------------------------------------------ skialpove-vazani
NEW['skialpove-vazani'] = dict(long=True,
    title='Skialpová vázání: pinová, rámová, uvolnění, montáž',
    desc='Skialpová vázání Dynafit a další: pinová (tech) i rámová. Jak vybrat podle bot, hmotnosti, uvolnění a stylu túry a porovnat obchody.',
    intro='<p>Skialpové vázání drží botu při sjezdu jako sjezdové vázání, ale při výstupu uvolní patu, takže noha kráčí jako při chůzi. Tahle dvojí funkce určuje všechno: váhu, způsob zapínání, nastavení uvolnění i kompatibilitu s botami. Sporteka porovnává nabídky českých obchodů u pinových vázání (tech), závodních i všestranných typů a rámových modelů a vypisuje, co ke každému patří.</p>'
          '<p>V kategorii převažuje značka ' + B(('dynafit', 'Dynafit')) + ', dále jsou zastoupeny ' + B(('wedze', 'Wedze'), ('marker', 'Marker'), ('salomon', 'Salomon'), ('fischer', 'Fischer')) +
          '. Ke vázání patří <a href="/skialpove-lyze/">skialpové lyže</a>, <a href="/skialpove-boty/">skialpové boty</a> a <a href="/skialpove-pasy/">stoupací pásy</a>. Přehled celého sportu najdete v kategorii <a href="/skialpinismus/">skialpinismus</a>.</p>',
    guide='<h2>Jak skialpové vázání funguje</h2>'
          '<p>Při stoupání je špička boty uchycena v otočném bodě a pata se volně zvedá. Pro stoupání lze zvednout takzvaný stoupací pomocník, který paty podepře ve dvou výškách a šetří lýtka na prudkých úsecích. Při sjezdu se pata zajistí a vázání se chová jako pevný celek, který při pádu může uvolnit botu. Přepínání mezi režimy se dělá obvykle holí, bez sundání lyží, a trvá pár vteřin.</p>'
          '<p>Nejdůležitější je pochopit, že vázání není izolovaný díl. Skládá se z jednoho systému s botou, lyží a pásem. Vše musí na sebe navazovat, a proto se výběr vázání vždy začíná botou.</p>'
          '<h2>Pinové (tech) a rámové vázání</h2>'
          + T(['Typ', 'Princip', 'Výhody', 'Nevýhody'], [
              ['Pinové (tech)', 'špička boty se zachytí kolíky v předním dílu, vzadu se zajistí v kolíkové patě', 'nízká váha, efektivní stoupání', 'bota musí mít tech vložky, citlivější na správné zacvaknutí'],
              ['Rámové', 'bota je pevně v rámu, který se v patě zvedá', 'blízké sjezdovému pocitu, tolerantní k botám', 'vyšší hmotnost, tužší chůze'],
              ['Hybridní', 'pinová špička s pevnější patou nebo opačně', 'kompromis mezi komfortem a váhou', 'složitější mechanika'],
              ['Závodní', 'minimalistická konstrukce', 'nejnižší hmotnost', 'omezený sjezdový komfort a jistota při pádu']]) +
          '<p>Pinová vázání jsou dnes na túrách nejběžnější, protože nesou nejmenší váhu na každém kroku. Rámová zůstávají u těch, kdo jezdí hodně na sjezdovkách nebo chtějí univerzální vybavení pro túry i resort. V nabídce jsou typické pinové modely řad Dynafit TLT Superlite, Speed Turn, Radical, Low Tech Race a DNA nebo ST Rotation s větším důrazem na sjezd. Značka Wedze nabízí vázání pro rekreační túry.</p>'
          '<h2>Co vlastně znamenají názvy řad</h2>'
          '<p>Názvy modelů označují především účel. TLT Superlite a Low Tech Race míří na minimální váhu, závody a dlouhé výstupy. Speed Turn a Speed Radical jsou kompromisy pro dobrý stoupací komfort a mírnou odezvu při sjezdu. ST Rotation obsahuje otočný přední díl, který se při pádu může vychýlit do strany a snižuje namáhání nohy. Řada Blacklight nebo Seven Summits cílí na lehké, ale funkční vázání pro náročnější túry. U všech modelů je třeba ověřit konkrétní stav, tedy typ brzdy, šířku a rozsah nastavení.</p>'
          '<h2>Kompatibilita s botami</h2>'
          '<p>Před nákupem zkontrolujte, zda vaše boty mají na špičce a patě vložky pro pinové vázání. Pokud je nemají, nelze na ně tech vázání použít a zbývá rámové. Podívejte se také na rozdíl mezi botami z různých značek: délka podrážky, tvar patního výřezu a poloha vložek se mohou lišit a některé vázání vyžaduje přesné nastavení po nasazení. Pokud si nejste jistí, nechte kombinaci zkontrolovat v servisu.</p>'
          '<p>Boty a vázání se vzájemně ovlivňují i jinak. Tužší bota přenáší sjezdové síly na vázání silněji, což u nejlehčích konstrukcí může vést k jejich přetížení. Pro hlubší pohled projděte <a href="/skialpove-boty/">skialpové boty</a>.</p>'
          '<h2>Hmotnost versus bezpečnost</h2>'
          '<p>Rozdíl několika desítek gramů na lyži se při dlouhém výstupu sčítá, ale mizí v celkové váze výbavy. Proto je rozumné ptát se, co za úsporu platíte. Nejlehčí vázání mají menší rozsah nastavení, jednodušší patu a při pádu se často neuvolní tak, jak sjezdové vázání. Pro lidi, kteří lyžují hlavně po neupraveném terénu a občas padají, se vyplatí pevnější konstrukce. Naopak závodník nebo zkušený turista na dlouhých výstupech ocení každý gram.</p>'
          '<h2>Uvolnění a nastavení</h2>'
          '<p>Hodnota uvolnění se nastavuje podle hmotnosti, výšky, věku, délky chodidla a stylu jízdy. Obvykle se pracuje s číselnou stupnicí na vázání. Příliš nízké nastavení vede k nechtěnému uvolnění lyže při jízdě, příliš vysoké zvyšuje riziko zranění při pádu. Hodnotu vždy stanoví servis podle návodu výrobce, ne odhadem. Zkušenost jezdce a terén jsou také podstatné: začátečník volí nižší hodnoty, zkušený a agresivní jezdec vyšší.</p>'
          '<p>Kromě hodnoty se kontroluje také funkce špičky a paty, čistota mechanismu a správné nasazení boty. Při nastavování se nic nehádá a nejde se podle zkušeností kamaráda, protože každý má jinou váhu a obuv.</p>'
          '<h2>Brzdy, řemínky a lyžařské nože</h2>'
          '<p>Na túře je ztráta lyže nebezpečná, protože se může sjet do údolí. Proto mají vázání buď brzdu, která lyži po uvolnění zastaví, nebo se používá bezpečnostní řemínek. Brzda se vybírá podle šířky lyže. Jiná je zapotřebí pro úzkou závodní lyži a jiná pro široké freerideové lyže, takže si ověřte rozmezí šířek brzdy u vybraného modelu. Při jízdě v lavinovém terénu se řemínek často nahrazuje brzdou, ale rozhodnutí závisí na terénu a zkušenostech.</p>'
          '<p>Lyžařské nože, nebo též stoupací železa, se nasazují na zmrzlý a tvrdý sníh, kde pásy neudrží. Jsou dodávány jako doplněk ke konkrétním modelům a vybírají se podle modelu vázání a šířky lyže. Zkontrolujte, zda se k vybranému kusu dají dokoupit.</p>'
          '<h2>Montáž</h2>'
          '<p>Vázání se montuje šrouby do lyže, často s použitím šablony. Montáž musí mít přesné rozteče, správné vrtáky a vhodné lepidlo, jinak se šrouby ve hmotě lyže vytrhnou. U skialpových lyží s tenkou stavbou nebo karbonovou konstrukcí je chyba v montáži obzvlášť riskantní. Proto montáž svěřte servisu, který zná konkrétní lyži a vázání. Nastavení délky podle boty se provádí po montáži a při každé změně boty se kontroluje znovu.</p>'
          '<p>Některé lyže mají předpřipravené vložky, takzvané inserty, do kterých se vázání šroubuje bez vrtání. V nabídce jsou i vázání s označením insert, určená pro takové lyže. Taková kombinace usnadňuje výměnu vázání mezi páry lyží, ale musí odpovídat systému výrobce lyže.</p>'
          '<h2>Pro jaký styl túry zvolit které vázání</h2>'
          + T(['Styl', 'Co zvolit', 'Na co dbát'], [
              ['Závody a rychlé túry', 'nejlehčí pinové vázání', 'omezená odolnost při pádu'],
              ['Univerzální túry', 'pinové s brzdou a větší rezervou', 'poměr váhy a odezvy'],
              ['Freeride a prudké sjezdy', 'robustní pinové nebo rámové', 'hmotnost, pevná pata, tužší bota'],
              ['Začátečníci', 'jednodušší ovládání, nižší nároky na techniku', 'kompatibilita s botou a správné uvolnění'],
              ['Sjezdovky a túry střídavě', 'rámové nebo hybridní vázání', 'komfort při sjezdu']]) +
          '<h2>Péče a kontrola</h2>'
          '<p>Po túře vázání otřete od sněhu a vlhkosti a nenechávejte ho zamrzat v otevřené poloze. Zkontrolujte kolíky, pružiny, brzdu a nástavce, a odstraňte písek nebo zmrzlý sníh z pinů. Před sezónou nechte vázání prohlédnout a nastavit v servisu. Poškrábané plasty, deformované kolíky a prasklé části znamenají výměnu, ne improvizaci. Při přepravě v autě chraňte lyže před nárazy, aby se nepoškodila přední část.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě vázání bez ověření, že boty mají odpovídající vložky.</li>'
          '<li>Výběr nejlehčího modelu bez ohledu na styl jízdy a odolnost.</li>'
          '<li>Nastavení uvolnění „od oka“ nebo podle kamaráda.</li>'
          '<li>Montáž bez šablony a bez servisu.</li>'
          '<li>Zanedbání brzdy nebo řemínku v terénu, kde lyže snadno sjede dolů.</li>'
          '<li>Nepoužití správné šířky brzdy a ztráta lyže při pádu.</li></ul>'
          '<h2>Co dalšího se hodí</h2>'
          '<p>Kromě lyží, bot a pásů se do výbavy počítají <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a>, <a href="/lyzarske-bundy/">lyžařské bundy</a> a <a href="/lyzarske-rukavice/">rukavice</a>. Pro přepravu pomůže <a href="/lyzarske-vaky-a-tasky/">lyžařský vak</a>, na údržbu skluznice <a href="/lyzarske-vosky/">lyžařské vosky</a>. Při túrách mimo značené trasy je nutné znát lavinovou bezpečnost, mít odpovídající vybavení a nechodit sám, přičemž základem je kurz. Doplňte <a href="/prvni-pomoc/">lékárničku</a>.</p>'
          '<p>Mezi podobné kategorie patří <a href="/lyzarske-vazani/">lyžařské vázání</a> na sjezdovky, <a href="/snowboardova-vazani/">snowboardová vázání</a> a <a href="/bezecke-vazani/">běžecké vázání</a>. Ty se ale na skialpové lyže nehodí a nejsou zaměnitelné, protože mají jiné uchycení boty.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Katalog zahrnuje i položky, které vázáním jen sousedí, například držáky a vložky pro lyže nebo vázání jiného sportu. Při výběru čtěte název a popis a nespoléhejte na to, že kategorie obsahuje jen skialpové modely. Sporteka porovnává nabídky obchodů a odkazuje na jejich stránky. Zkontrolujte dostupnost, délku brzdy a to, zda je u vybraného modelu součástí balení i stoupací pomocník, nože a šrouby.</p>',
    faq=[('Jaké skialpové vázání zvolit?', 'Nejprve podle bot a stylu túry. Pro rychlé a dlouhé túry pinové a lehké, pro prudší sjezd robustnější pinové nebo rámové.'),
         ('Co je tech vázání?', 'Pinové vázání, v němž se špička boty zachytí kolíky a pata zajistí v kolíkové patě. Je lehké a efektivní při stoupání, ale boty musí mít tech vložky.'),
         ('Pasují všechny boty na pinové vázání?', 'Ne. Bota musí mít vložky na špičce a patě. Bez nich zvolte rámové vázání nebo jiné boty.'),
         ('Jak se nastavuje uvolnění?', 'Podle hmotnosti, výšky, věku, délky chodidla a stylu jízdy, ideálně v servisu a podle návodu výrobce.'),
         ('Potřebuji brzdu nebo řemínek?', 'Ano, aby lyže po uvolnění nesjela do údolí. Brzdu vybírejte podle šířky lyže, řemínek je doplněk nebo alternativa.'),
         ('Mohu si vázání namontovat sám?', 'Nedoporučuje se. Špatná montáž může způsobit vytržení šroubů a ohrozit bezpečnost, proto ji svěřte servisu se šablonou.'),
         ('K čemu slouží stoupací pomocník?', 'Podpírá patu při stoupání ve dvou výškách, takže šetří lýtka a šlachy na prudkém svahu.'),
         ('Hodí se skialpové vázání na sjezdovku?', 'Funguje, ale u pinových modelů je sjezd méně tolerantní. Pro častý pohyb na sjezdovkách vyberte robustnější nebo rámové vázání.'),
         ('Co jsou lyžařské nože?', 'Stoupací železa, která se nasazují na vázání při stoupání po tvrdém nebo zmrzlém sněhu, kde pásy neudrží.'),
         ('Jak často vázání kontrolovat?', 'Před každou sezónou a po nárazu nebo pádu, který mohl poškodit kolíky nebo pružiny. Opotřebené díly vyměňte.'),
         ('Rozdíl mezi skialpovým a sjezdovým vázáním?', 'Skialpové uvolňuje patu pro chůzi a je lehčí, sjezdové je pevné a robustní. Nejsou zaměnitelné.')],
)

# ------------------------------------------------------------------ bezecke-opasky
NEW['bezecke-opasky'] = dict(long=True,
    title='Běžecké opasky a pouzdra: telefon, láhev, výběr',
    desc='Běžecké opasky, ledvinky a pouzdra na telefon či láhev. Jak vybrat velikost, uchycení a objem a porovnat nabídky českých obchodů.',
    intro='<p>Běžecký opasek unese telefon, klíče, gely a malou láhev a nechá ruce volné. Na rozdíl od vesty se nevěší na ramena, takže se hodí na kratší a střední tratě, na městský běh i na horké dny, kdy by vesta nepříjemně hřála. Sporteka porovnává nabídky českých obchodů u plochých pásek na telefon, trailových ledvinek, opasků s lahvemi i reflexních pásků, které zvyšují viditelnost.</p>'
          '<p>V kategorii se objevují značky ' + B(('compressport', 'Compressport'), ('dynafit', 'Dynafit'), ('kiprun', 'Kiprun'), ('salomon', 'Salomon'), ('bodycross', 'Bodycross'), ('nathan', 'Nathan'), ('silva', 'Silva')) +
          '. Pro větší objem se podívejte na <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, pro běh v přírodě na <a href="/trailove-boty/">trailové boty</a> a pro celkový přehled na <a href="/beh/">běh</a>.</p>',
    guide='<h2>Druhy běžeckých opasků</h2>'
          '<p>Opasek není jen opasek. Pod tímto názvem se prodávají velmi různé tvary a každý se hodí na jinou situaci. Než porovnáte konkrétní kusy, ujasněte si, co potřebujete nést a jak dlouho poběžíte.</p>'
          + T(['Druh', 'Popis', 'Na co se hodí'], [
              ['Plochá páska na telefon', 'úzký elastický pás s kapsou', 'krátké běhy, telefon a klíče'],
              ['Ledvinka na zip', 'širší pás s jednou až dvěma kapsami', 'běh a vycházky s malým nákladem'],
              ['Opasek s lahví', 'držák na jednu nebo dvě láhve', 'střední tratě, horké dny'],
              ['Trailový opasek', 'objemnější, často s popruhem proti houpání', 'terén, závody v přírodě'],
              ['Závodní opasek na čísla a gely', 'pružná páska s očky pro gely a číslo', 'závody, maratony'],
              ['Reflexní nebo svítící pás', 'zvyšuje viditelnost, někdy se světlem', 'běh za tmy a ve městě']]) +
          '<p>Řada Compressport Free Belt je pružná páska pro telefon a drobnosti. Race Belt je zacílen na závodní použití. Dynafit a Salomon nabízejí opasky pro trail s držáky na láhve. Kiprun míří na běžné silniční běhání, Bodycross na trailové ledvinky a Eleven a Silva na lehké varianty. U všech si prohlédněte popis, protože stejný název modelu může skrývat odlišné velikosti nebo kapacity.</p>'
          '<h2>Objem a to, co do opasku patří</h2>'
          '<p>Kapacita se uvádí v litrech nebo v počtu kapes. Pro krátký běh stačí telefon, klíč a kartu, kam se vejde jen pár set mililitrů. Na dvouhodinový běh přidejte gel, malou láhev a lehkou bundu do kapsy. Čím víc obsah váží, tím víc opasek poskakuje, takže je rozumné nosit jen to, co potřebujete. Těžký náklad patří spíš do <a href="/bezecke-vesty-a-batohy/">běžecké vesty</a>, která váhu rozloží na ramena a hrudník.</p>'
          '<p>Praktické předměty na běh: telefon, klíč, platební karta nebo drobné peníze, kapesník, průkaz s kontakty a u delších tratí gel nebo tyčinka. Na delší běh přibalte <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a zvolte vhodný <a href="/iontove-napoje/">iontový nápoj</a>; množství a složení vždy řešte podle pokynů výrobce.</p>'
          '<h2>Jak vybrat velikost a uchycení</h2>'
          '<p>Opasek se nosí na bocích nebo v pase, těsně, ale tak, aby nebránil dýchání. Změřte obvod pasu v místě, kde budete pás nosit, a porovnejte jej s tabulkou výrobce. Pružné pásy mívají široký rozsah a sedí bez nastavení. Ledvinky s přezkou je třeba doladit, aby se nehoupaly. Zkoušejte i s plným obsahem, protože prázdný opasek sedí jinak než nacpaný telefonem a lahví.</p>'
          '<p>Pozor na rozdíly mezi mužskou a ženskou postavou. Úzký pas a širší boky mohou způsobit, že se opasek posouvá nahoru nebo dolů. Řešením je nižší poloha na kyčlích nebo širší pružný pás. Pomůže i protiskluzová vnitřní strana, kterou některé modely mají. Zvažte i to, zda je opasek určen pro nošení na zádech, nebo vpředu: vpředu je telefon snadněji dostupný, vzadu překáží méně.</p>'
          '<h2>Telefon: pouzdro, voděodolnost a dotyk</h2>'
          '<p>Telefon je hlavní důvod, proč lidé opasek kupují. Ověřte rozměry vašeho telefonu, včetně krytu, a porovnejte je s kapsou. Moderní velké telefony se do menších opasků nevejdou, nebo napnou látku tak, že opasek sjíždí. Kapsa s okénkem umožňuje ovládat dotykový displej bez vyndání, ale snižuje ochranu před vodou. Voděodolná kapsa se zipem a zatavenými švy odolá lehkému dešti, nikoli ponoření. Platí to i pro označení „vodotěsný“, které bývá optimistické, takže citlivé předměty chraňte v sáčku.</p>'
          '<p>Pokud používáte telefon na běhu pro sledování trasy, zvažte spotřebu baterie v zimě, protože chlad ji zkracuje. Pomůže držet telefon blízko těla a doplnit <a href="/powerbanky-a-nabijeni/">powerbanku</a> na delší výlety. Pro měření tepu a tempa se hodí <a href="/sportovni-hodinky/">sportovní hodinky</a>, díky nimž telefon vůbec nemusíte mít na očích.</p>'
          '<h2>Láhve a hydratace</h2>'
          '<p>Opasky s lahví nesou jednu nebo dvě menší láhve nebo měkké láhve. Tvrdé láhve se snadněji vytahují, ale houpou se. Měkké se při vypití sbalí a méně vyrušují. Zkuste vytáhnout a zasunout láhev za pohybu, nejlépe jednou rukou, protože na tratích se to dělá bez zastavení. Pro delší běh bez občerstvovacích stanic potřebujete větší zásobu a tam je lepší vesta. Základem jsou <a href="/lahve-a-termosky/">láhve a termosky</a> a při dlouhých trasách i <a href="/iontove-napoje/">iontové nápoje</a>.</p>'
          '<h2>Silnice, trail a závod</h2>'
          '<p>Na silnici stačí lehká páska nebo ledvinka s telefonem. V terénu se zvyšují nároky: větší pohyb těla, nerovnosti a delší trvání. Trailové opasky mají stabilnější uchycení, často popruh přes stehno nebo další pásek a pevnější materiál. Při závodech se používají úzké pásky pro číslo a gely, protože startovní číslo se nemusí přišívat ani připínat na tričko. Při maratonu je výhoda, že gely visí na očkách a jsou po ruce.</p>'
          '<h2>Bezpečnost za tmy</h2>'
          '<p>Reflexní prvky na opasku zlepšují viditelnost pro řidiče a cyklisty. Nejlépe fungují v pohybu, tedy na nohách a pažích, proto je dobré doplnit opasek reflexními prvky na obuvi nebo oblečení. K běhu za tmy se hodí také <a href="/celovky-a-svitilny/">čelovky a svítilny</a>. Nikdy nespoléhejte jen na reflexní materiál, který ztrácí účinnost po několika desítkách praní, a běhejte raději po osvětlených trasách. Vybavení pro lepší viditelnost najdete také v <a href="/funkcni-tricka/">funkčních tričkách</a> s reflexními prvky.</p>'
          '<h2>Materiály a nošení</h2>'
          '<p>Opasky se šijí z elastického polyamidu a elastanu, někdy se síťovinou pro odvětrání. Měkká tkanina nedře, a když nasákne potem, může se roztahovat a klouzat. Proto je dobrá pružná vnitřní strana s protiskluzovým prvkem. Švy nesmějí tlačit na kyčle. Zipy by měly mít jezdce, který se dá ovládnout i v rukavicích. Pokud trpíte otlaky z lemování, vyzkoušejte opasek s plochými švy nebo nižším profilem. V zimě se opasek často nosí pod bundou, což ochrání telefon před chladem, ale ztíží přístup.</p>'
          '<h2>Péče</h2>'
          '<p>Po použití opasek vyvěste, aby vyschl, a vytáhněte všechny předměty, protože pot se usazuje i v kapsách. Perte jej ručně nebo v pračce na jemný program ve vlažné vodě a v ochranném sáčku, aby se nezachytily zipy. Nepoužívejte aviváž, která zhoršuje odvod vlhkosti, a nesušte v sušičce. Pokud je pružný pás po sezóně povolený, vyměňte jej, protože již neudrží polohu. Kapsy s okénkem čistěte jemným hadříkem, aby se nepoškrábalo.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Výběr podle vzhledu bez kontroly rozměru telefonu.</li>'
          '<li>Koupě příliš malého opasku, který se po naplnění nedá zapnout.</li>'
          '<li>Přetížení kapes, kvůli čemuž opasek poskakuje.</li>'
          '<li>Spoléhání na to, že je kapsa nepromokavá, a nechránění telefonu.</li>'
          '<li>Opasek s lahví na dlouhý běh, kde je potřeba větší zásoba.</li>'
          '<li>Ignorace pocitu v pase: tlak na žaludek a dýchání se při delším běhu zhoršuje.</li></ul>'
          '<h2>Co dalšího se hodí k běhu</h2>'
          '<p>K opasku patří pohodlná <a href="/bezecka-obuv/">běžecká obuv</a> a v terénu <a href="/trailove-boty/">trailové boty</a>, dále <a href="/sportovni-ponozky/">sportovní ponožky</a>, lehké <a href="/sportovni-kratasy/">kraťasy</a> nebo <a href="/leginy/">legíny</a> a <a href="/sportovni-bryle/">sportovní brýle</a>. Při bolesti kloubů se poraďte s lékařem; <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> jsou jen podpůrná pomůcka. Pro delší výlety v přírodě je užitečná <a href="/prvni-pomoc/">lékárnička</a>. Závodníci v triatlonu se podívají do kategorie <a href="/triatlon/">triatlon</a>, kde se opasky na číslo používají také.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Sporteka sbírá nabídky obchodů a vede vás na jejich stránky. V kategorii najdete jak opasky na telefon, tak lahve a pouzdra, která se do ní dostala jako příbuzné doplňky, proto vždy zkontrolujte název a popis. Pokud váháte mezi opaskem a vestou, vezměte v úvahu délku tratě, počet věcí a to, zda potřebujete pít za pochodu. Obchody s jednoduchou výměnou jsou výhodnější, protože sedění pásu se ukáže až na běhu.</p>',
    faq=[('Jaký opasek vybrat na běh?', 'Podle toho, co nesete. Na telefon a klíče stačí plochá páska, pro láhev a gely zvolte opasek s držákem nebo trailový model.'),
         ('Je lepší opasek, nebo vesta?', 'Opasek je lehčí a chladnější na krátké a střední běhy. Pro větší zásobu vody a oblečení je vhodnější vesta, která váhu rozloží na ramena.'),
         ('Vejde se do opasku velký telefon?', 'Ne vždy. Porovnejte rozměry telefonu i s krytem s rozměrem kapsy. Příliš napnutá kapsa způsobuje sjíždění opasku.'),
         ('Jak zabránit houpání opasku?', 'Opasek nasaďte těsně na boky, nepřetěžujte kapsy a vybírejte modely s protiskluzovou vnitřní stranou nebo stehenním popruhem.'),
         ('Je kapsa na telefon nepromokavá?', 'Voděodolná kapsa odolá lehkému dešti, ale ne ponoření. Citlivé věci chraňte v sáčku, zvlášť při dlouhých a deštivých bězích.'),
         ('Jak určit velikost?', 'Změřte obvod pasu v místě nošení a porovnejte s tabulkou výrobce. Pružné pásy mají široký rozsah, ledvinky s přezkou se nastavují.'),
         ('Hodí se opasek na maraton?', 'Ano, závodní modely mají očka pro gely a číslo. Zvolte lehký opasek a vyzkoušejte jej při tréninku se stejným obsahem.'),
         ('Mohu opasek prát?', 'Ano, ručně nebo na jemný program ve vlažné vodě, bez aviváže a bez sušičky. Předtím vyprázdněte kapsy a zapněte zipy.'),
         ('Hodí se opasek na běh za tmy?', 'Reflexní prvky pomáhají, ale nespoléhejte jen na ně. Doplňte čelovku a oblečení s reflexními prvky a běhejte po osvětlených trasách.'),
         ('Kolik lahví unese opasek?', 'Podle modelu jednu nebo dvě menší láhve. Na delší běh bez občerstvení potřebujete větší zásobu, tedy vestu nebo batoh.'),
         ('Neškrtí opasek při dýchání?', 'Nemá. Pokud tlačí na žaludek nebo omezuje dech, uvolněte jej, posuňte níže na boky nebo zvolte širší a měkčí pás.')],
)

# ---------------------------------------------------------------- doplňky (rozšíření)
NEW['nizke-trekove-boty']['guide'] += (
    '<h2>Příprava na první túru v nových botách</h2>'
    '<p>Nové boty rozchoďte předem: několik dní je noste doma a na krátkých procházkách, aby se vložka přizpůsobila noze a objevily se případné tlakové body. Zjistíte tak, zda se pata nezvedá, a můžete upravit šněrování. Zkuste přeskakující šněrování nebo dodatečný uzel nad nártem, který patu zafixuje při sestupu. Na túru si vezměte náplast na puchýře a při prvním pálení zastavte a ošetřete místo dřív, než se rozjitří.</p>'
    '<p>Při několikadenních výletech mějte s sebou i náhradní suché ponožky. Střídání ponožek během dne výrazně snižuje riziko otlaků a pomáhá i při mokrém počasí. Večer boty vyvětrejte a vložky rozložte, ať se do rána aspoň částečně vysuší.</p>')
NEW['pristresky-a-party-stany']['guide'] += (
    '<h2>Kde stan postavit</h2>'
    '<p>Místo vyberte rovné, mimo svah, ze kterého stéká voda, a mimo dosah padajících větví. Pod střechu nesmí zasahovat elektrické vedení a u akce na veřejném prostranství je třeba ověřit povolení pořadatele nebo majitele pozemku. Prohlédněte zem: kameny a kořeny poškodí podlahu i nohy konstrukce. Před stavbou rozložte součásti, spočítejte kolíky a lana a rozdělte role, protože stavba ve dvou nebo čtyřech lidech trvá výrazně kratší dobu a je bezpečnější.</p>'
    '<p>Při večerním provozu pomohou řetězy světel nebo lampy připevněné na rám, nikoli volně položené svíčky u plachty. Plachta by neměla mít kontakt s horkými zdroji, grily ani ohřívače nepatří pod střechu.</p>')
NEW['skialpove-vazani']['intro'] = NEW['skialpove-vazani']['intro'].replace(
    '<p>V kategorii převažuje', '<p>Kategorie se mění i podle sezóny, proto vždy ověřte, jaké boty a lyže k vázání přiřazujete. V kategorii převažuje')
NEW['skialpove-vazani']['guide'] += (
    '<h2>Postup před koupí</h2>'
    '<p>Praktický postup je jednoduchý. Zjistěte, zda mají vaše boty tech vložky, změřte šířku lyží ve střední části, odhadněte, kolik času budete trávit stoupáním a kolik sjezdem, a stanovte maximální hmotnost, kterou jste ochotni nést. Teprve poté porovnávejte konkrétní modely, jejich brzdy a rozsah nastavení délky. Pokud kupujete vázání pro jiného člena rodiny, zeptejte se na jeho zkušenosti a rozsah hmotnosti, protože nastavení je u každého jiné.</p>')
NEW['bezecke-opasky']['guide'] += (
    '<h2>Zkouška před delším během</h2>'
    '<p>Nový opasek vyzkoušejte na krátkém tréninku se všemi věcmi, které chcete nést. Zjistíte, zda se neposouvá, jestli telefon nebouchá o pás a jak se vytahuje láhev. Pokud opasek dře, zkuste jej nasadit pod tričko, ale ověřte, zda se vám pak snadno dostanete ke kapsám. Pro delší trasy nechte opasek vyprat a vyvětrat, ať se nevytvoří zápach, který se špatně odstraňuje. Pamatujte, že po delší době se pružnost pásu ztrácí, takže se vyplatí vyměnit opasek, který už nedrží.</p>')
NEW['nizke-trekove-boty']['faq'].append(('Jak zabránit puchýřům?', 'Noste dobře padnoucí boty, bezešvé ponožky z umělého vlákna nebo vlny, boty rozchoďte předem a při prvním pálení zastavte a ošetřete místo.'))
NEW['pristresky-a-party-stany']['faq'].append(('Kde stan postavit?', 'Na rovné místo mimo svah, ze kterého stéká voda, mimo větve a elektrické vedení. Na cizím pozemku si ověřte souhlas majitele.'))
NEW['skialpove-vazani']['faq'].append(('Jak zjistím, zda moje boty mají tech vložky?', 'Podívejte se na špičku a patu boty. Kovové vložky v prohlubních jsou na pohled zřetelné, nebo se zeptejte v servisu či zkontrolujte parametry výrobce.'))
NEW['bezecke-opasky']['faq'].append(('Kdy opasek vyměnit?', 'Když se pružný pás povolí a opasek sjíždí, nebo když zipy a švy přestanou držet. Opotřebovaný opasek už neudrží polohu.'))
NEW['skialpove-vazani']['guide'] += (
    '<p>Na závěr zvažte i budoucnost vybavení. Vázání vydrží několik sezón, ale boty a lyže se mohou změnit. Kdo plánuje přejít na jiné boty nebo širší lyže, zvolí model s větším rozsahem nastavení a výměnnými díly, takže jej nebude muset hned nahrazovat novým kusem.</p>')
NEW['bezecke-opasky']['guide'] += (
    '<p>Při výběru barvy zvažte provoz: tmavý opasek je nenápadný, výrazný nebo reflexní je lépe vidět na silnici a v lese při závodech, kde se hledá odložená věc. Stojí také za to ověřit, zda se pás dá nosit i přes bundu, což v zimě bývá užitečné, když potřebujete rychlý přístup k telefonu bez rozepínání vrstev.</p>')
