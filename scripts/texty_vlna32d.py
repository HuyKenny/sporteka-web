"""sporteka.cz — wave 32d (18. 11. 2026): long texts for posilovaci-kladky, pilates-reformery, vibracni-plosiny,
zavesne-systemy-trx, petanque. General true facts only, no prices, no product counts. Pilates reformers and vibration plates
are described without health promises (not medical devices; people with health problems are sent to a doctor or
physiotherapist; instruction recommended). Load limits are always "per manufacturer"; the few figures quoted are examples
from a maker's or seller's data sheet. Pétanque figures come only from the FIPJP rulebook and Decathlon product pages.
Brands linked only if present in src/texts/znacky.json (hms, insportline, gymbeam, decathlon, merco), the rest plain text.
Product types checked by name in the local catalogue copy (kladky HMS/Marbo/Insportline/Vifito/Revity, reformers
Insportline Comfolder/Oquiler/Auraler/Driftaler/Trancer, Sharp Shape, Myga; plates HMS SVP, Insportline, Tunturi, Fluxa;
suspension trainers Insportline MultiTrainer, HMS RXT, Sportago Variotrainer, Sedco EP514; pétanque Master, Geologic, Obut).

Sources:
- Cable ratios 1:1 vs 2:1 (repfitness.com, musclesquad.com, fringesport.com guides): 2:1 = half the stack at the handle,
  twice the cable travel; compare working weight, not stack size
- MARBO MH-W108 wall pulley (seller listings goodio.be, e-katalog): max load 120 kg, wall/ceiling mounting
- inSPORTline Comfolder reformer (insportline.eu/79208): 248.5 x 92 x 28 cm, max load 150 kg, weight 68 kg, user height
  max 200 cm, foot bar 10 positions, springs red up to 20 kg / green 12 kg / yellow 7.5 kg, EN 20957 class S, folds and
  rolls on wheels; replacement set of 6 springs sold separately (insportline.eu/81538)
- Pilates Method Alliance history page: Joseph Pilates interned on the Isle of Man in WWI, emigrated to the USA in 1926;
  "Universal Reformer"; method originally called Contrology
- Whole-body vibration: side-alternating ~5-35 Hz with larger amplitude, vertical ~20-50 Hz with smaller amplitude;
  amplitude grows with foot distance from the axis; less transmission to the head with bent knees (MDPI Vibration 2022,
  Cumbria/Bone 2021 comparison of three platforms); fat-mass reviews (PubMed 31749405, The Conversation): small studies,
  modest effect mainly together with diet/exercise, vibration alone no meaningful weight loss
- inSPORTline vibration machine manuals (Katrina TO-600 / SE TO-650, Masay IN 2085): contraindications pregnancy, acute
  thrombosis, cardiovascular disease, fresh surgical scars, hip/knee replacement, pacemaker, epilepsy, tumour, hernia,
  disc problems, diabetes, severe migraine, metal screws; consult a doctor before use
- TRX: trxtraining.com Randy Hetrick page (ex-Navy SEAL, first prototype from a jiu-jitsu belt and parachute webbing),
  Wikipedia "TRX System"; trxtraining.eu setup blog (door anchor over a solid door closed on it, XMount to a load-bearing
  beam, suspension anchor around poles/trees for anchor heights of 7-9 ft); GoFit/X-Over door anchor sheets (solid door,
  close and lock it)
- FIPJP "Règlement de jeu officiel" (fipjp.org/images/pdf/reglementFIPJP.pdf): teams 3/2/1 players, 2 or 3 boules,
  boules metal 70.5-80 mm, 650-800 g, maker label and weight engraved, no lead/sand, under-12 competitions 600 g/65 mm;
  jack wood or synthetic 30 mm +-1 mm, painted jack must not be magnetic; terrain min 15 x 4 m (national/international),
  otherwise min 12 x 3 m; games to 13 points; circle 35-50 cm drawn or rigid 50 cm; jack 6-10 m; feet inside the circle
  until the boule lands; 1 minute per throw
- Wikipedia / Provence tourism: La Ciotat, 1907 (some sources 1910), Jules Lenoir, Provençal "pès tancats"
- Decathlon/Geologic pages: hardness hard / semi-soft / soft, harder = less damage but more bounce; heavier for pointers,
  lighter for shooters, diameter by hand size; leisure set 70 mm / 550 g for sand or grass; wipe and oil boules
Left out (not verifiable): TRX strap load ratings and the founding year of the company in the text, exact years of the
first pilates studio, frequency/amplitude of individual plates, the Czech federation's founding year, folded size of
reformers, typical rack upright profiles, any claims on calories, bone density or "lymphatic drainage".
"""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ posilovaci-kladky
NEW['posilovaci-kladky'] = dict(long=True,
    title='Posilovací kladky na zeď, strop i k power racku',
    desc='Horní a spodní kladky na zeď, protisměrné kladky, nástavce k rackům a madla. Převod 1:1 a 2:1, nosnost podle výrobce a bezpečná montáž.',
    intro='<p><strong>Posilovací kladka</strong> je jednoduché zařízení: ocelové lanko vedené přes kladky s ložisky přenáší odpor závaží nebo kotoučů na madlo. Díky tomu se dá táhnout shora, zdola i ze strany a odpor působí ve směru lanka po celé dráze pohybu. Typické cviky jsou stahování horní kladky k hrudníku, přitahování spodní kladky vsedě, tricepsové tlaky s lanem nebo upažování jednou rukou. Doma se kladka nejčastěji šroubuje na zeď, na strop nebo jako nástavec na stojan na dřepy.</p>'
          '<p>Na Sportece jsou vedle sebe nabídky českých e-shopů na samostatné horní a spodní kladky, protisměrné kladky, nástavce k power rackům, kladky k lavicím i madla a lana. Najdete tu mimo jiné výrobky značek '
          + B(('hms', 'HMS'), ('insportline', 'Insportline')) +
          ', Marbo, Vifito nebo Revity. Kladky patří mezi <a href="/posilovaci-stroje/">posilovací stroje</a> a dobře se doplňují s nabídkou <a href="/posilovaci-veze/">posilovacích věží</a> a <a href="/kotouce-na-cinky/">kotoučů na činky</a>.</p>',
    guide='<h2>Jak kladka funguje</h2>'
          '<p>Každá kladka má tři části: zdroj odporu, lanko s kladkami a madlo. Zdrojem odporu je buď blok závaží, ve kterém se hmotnost volí zastrčením kolíku, nebo trn, na který se nakládají kotouče. Lanko běží přes jednu či více kladek s ložisky a na konci má oko, do kterého se karabinou připne madlo. Když za madlo zatáhnete, zvedá se závaží a po celou dobu cítíte jeho odpor.</p>'
          '<p>Proti volným činkám má kladka jednu velkou výhodu. Činka vždy tíhne svisle dolů, kdežto lanko táhne tím směrem, kterým vede. Dá se tak posilovat v úhlech, které s jednoručkou nejdou, například táhnout zepředu dozadu nebo zdola nahoru přes tělo. Proti stroji s pevnou dráhou si zase tělo volí postavení samo, takže se zapojují i svaly, které drží trup a ramena ve stabilní poloze.</p>'
          '<p>Blok závaží je pohodlný, protože se hmotnost mění během pár vteřin. Stroj s ním je ale větší, těžší a dražší. Nakládací trn je jednodušší a zabere méně místa, potřebujete k němu však kotouče se správným otvorem. Hobby kotouče mívají otvor kolem 30 mm, olympijské kolem 50 mm. Než kladku objednáte, ověřte průměr trnu a porovnejte ho s kotouči, které doma máte.</p>'
          '<h2>Typy kladek</h2>'
          + T(['Typ', 'Jak vypadá', 'Typické cviky'], [
              ['Horní kladka na zeď nebo strop', 'rameno s kladkou nad hlavou, lat tyč', 'stahování k hrudníku, tricepsové tlaky'],
              ['Horní a spodní kladka', 'kladka nahoře i dole, někdy jedno společné lanko', 'stahování, přitahování vsedě, bicepsové zdvihy'],
              ['Nástavec k power racku', 'kladky šroubované na sloupky stojanu', 'stejné cviky bez dalšího místa v místnosti'],
              ['Kladka k posilovací lavici', 'spodní kladka na konci lavice', 'bicepsové zdvihy, předkopávání, zakopávání'],
              ['Protisměrné kladky', 'dvě věže s výškově stavitelnými kladkami', 'rozpažování, rotace trupu, cviky jednou rukou'],
              ['Závěsná kladka s trnem', 'kladka zavěšená na hrazdě nebo racku', 'jednoduchá varianta na tricepsy a stahování']]) +
          '<p>Protisměrné kladky se v obchodech objevují i pod anglickým názvem cable crossover. Jde o dvojici sloupů, na kterých se dá vozík s kladkou posunout do libovolné výšky. Patří k nejvšestrannějším strojům v posilovně, ale potřebují hodně místa do šířky. Kompaktnější variantou jsou kombinované stroje, v nichž je kladka součástí multipressu nebo věže.</p>'
          '<h2>Převod 1:1 a 2:1</h2>'
          '<p>U kladek se často uvádí převod. Při převodu 1:1 cítíte na madle stejnou hmotnost, jakou máte nastavenou nebo naloženou. Lanko přitom ujede stejnou vzdálenost jako závaží. Takový převod se hodí na těžší cviky, jako je stahování horní kladky nebo přitahování vsedě.</p>'
          '<p>Při převodu 2:1 cítíte zhruba polovinu hmotnosti a lanko se dá vytáhnout dvakrát dál. Proto ho mají hlavně protisměrné kladky a funkční trenažéry, na kterých se dělají dlouhé pohyby přes celé tělo. Když srovnáváte dva stroje, nedívejte se jen na hmotnost bloku závaží. Blok o stejné hmotnosti dá na stroji s převodem 2:1 poloviční odpor než na stroji s převodem 1:1. Pokud převod v parametrech nenajdete, zeptejte se prodejce.</p>'
          '<h2>Nosnost a montáž na zeď nebo strop</h2>'
          '<p>Každý výrobce uvádí maximální zatížení. Je to hmotnost závaží nebo kotoučů, kterou konstrukce, lanko a kladky podle něj snesou. Prodejci například u nástěnné horní kladky Marbo MH-W108 uvádějí 120 kg. Číslo platí jen pro konkrétní model a za správné montáže, proto ho vždy hledejte v parametrech toho výrobku, který kupujete. Limit nepřekračujte, ani když se konstrukce zdá pevná.</p>'
          '<p>Nástěnná a stropní kladka drží jen tak dobře, jak dobře je ukotvená. Při tahu působí na kotvy větší síla než samotná hmotnost závaží, hlavně když se cvičí švihem nebo se závaží nechá spadnout. Výrobce v návodu uvádí, do jaké zdi se kladka smí montovat a jaké kotvy použít. Obecně se počítá s nosnou zdí nebo stropem z betonu či plných cihel. Sádrokarton a duté příčky bez ověření a speciálního kotvení nevyhoví. Pokud si nejste jistí, svěřte montáž někomu, kdo se v kotvení vyzná.</p>'
          '<p>Nástavce k power rackům se vyrábějí pro konkrétní profil sloupků a rozteč otvorů. Nejjistější je koupit nástavec od stejného výrobce jako stojan. U cizího nástavce porovnejte rozměry profilu a otvorů, jinak nemusí jít nasadit nebo bude na sloupku viklat.</p>'
          '<h2>Madla a příslušenství</h2>'
          '<p>K většině kladek se dodává jedna lat tyč, ostatní madla se dokupují. Rozmanitost cviků přitom záleží hlavně na nich. Nejčastěji se používají tyto:</p>'
          '<ul><li>Rovná nebo lomená lat tyč na stahování k hrudníku a za hlavu.</li>'
          '<li>Trojúhelníkové madlo (V madlo) na přitahování vsedě a úzké stahování.</li>'
          '<li>Tricepsové lano s koncovkami na tlaky dolů a nad hlavou.</li>'
          '<li>Jednoruční madlo s otočným okem na cviky jednou rukou.</li>'
          '<li>Krátká rovná nebo lomená tyč na bicepsové zdvihy u spodní kladky.</li>'
          '<li>Popruh na kotník na zanožování a unožování.</li></ul>'
          '<p>Madlo se k lanku připíná karabinou. Používejte tu, kterou dodal výrobce kladky, nebo spojku určenou pro posilovací stroje. Malé ozdobné karabinky na klíče se pod zatížením mohou rozevřít. Při nákupu madla od jiného výrobce ověřte, že oko madla projde karabinou a že se madlo při tahu nekroutí.</p>'
          '<h2>Kolik místa kladka potřebuje</h2>'
          '<p>Na horní kladku je potřeba dostatečná výška místnosti. Při stahování obvykle sedíte pod kladkou na lavici nebo sedáku a před sebou potřebujete místo na kolena. Spodní kladka vyžaduje prostor na dlouhý krok vzad nebo na nohy natažené vsedě. Protisměrné kladky potřebují šířku obou věží a ještě volný prostor vpředu, kam při cviku vykročíte. Před nákupem si místo změřte a připočtěte rezervu pro pohyb paží do stran.</p>'
          '<h2>Údržba a bezpečnost</h2>'
          '<p>Lanko je nejvíc namáhaná část. Před tréninkem zkontrolujte, jestli nemá roztřepená vlákna, zlomy nebo prodřený plastový obal. Poškozené lanko vyměňte hned, ne až po sezóně. Kontrolujte také, jestli se kladky otáčejí volně a bez drhnutí a jestli karabiny dobře zavírají. Šrouby a kotvy po prvních trénincích dotáhněte a pak je kontrolujte pravidelně podle návodu.</p>'
          '<p>Závaží pouštějte zpět řízeně, nenechte ho padat. Nárazy ničí lanko i kotvy a hluk se nese po celém domě. Kolík v bloku závaží a mezery mezi kotouči umí skřípnout prsty, proto u stroje nenechávejte malé děti bez dozoru. Při cvičení noste pevnou obuv a madla držte suchou rukou nebo v <a href="/sportovni-rukavice/">rukavicích</a>.</p>'
          '<h2>Jaké cviky se na kladce dají dělat</h2>'
          '<p>Na horní kladce se nejčastěji stahuje lat tyč k hrudníku širokým i úzkým úchopem, dělají se tricepsové tlaky dolů s lanem nebo rovnou tyčí a z kleku přítahy lana k obličeji na zadní část ramen. Na spodní kladce se přitahuje V madlo k břichu vsedě, cvičí se bicepsové zdvihy, předpažování a s popruhem na kotníku zanožování nebo unožování. Protisměrné kladky přidávají rozpažování ve stoje, rotace trupu s lanem vedeným zboku a tlaky jednou rukou.</p>'
          '<p>Kladka se hodí i pro začátečníky, protože hmotnost se dá přidávat po malých krocích a pohyb se snadno zastaví. Techniku si ale nechte ukázat trenérem nebo zkušeným cvičencem. Nejčastější chybou je tah švihem, při kterém se záda zaklánějí a práci místo svalů dělá setrvačnost závaží.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U každé kladky sledujte způsob montáže, maximální zatížení, převod, průměr trnu nebo rozsah bloku závaží a délku dráhy lanka. Důležité je také, co je v balení: lat tyč, další madla, kotvy, karabiny. Kotvy bývají určené jen pro určitý materiál zdi, ověřte proto, jestli se k vaší stěně hodí. U nástavců k rackům ověřte kompatibilitu se stojanem a u protisměrných kladek počet výškových poloh a rozměry půdorysu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kladka přišroubovaná do sádrokartonu nebo duté příčky.</li>'
          '<li>Kotouče, které na trn nepasují, přidělané provizorně.</li>'
          '<li>Srovnávání strojů podle bloku závaží bez ohledu na převod.</li>'
          '<li>Cvičení s poškozeným nebo roztřepeným lankem.</li>'
          '<li>Švihové tahy, při kterých závaží naráží do dorazu.</li></ul>'
          '<p>Ke kladce se hodí <a href="/posilovaci-lavice/">posilovací lavice</a>, na kotouče <a href="/stojany-na-cinky/">stojany</a> a pro cviky s vlastní vahou <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>. Kdo nemá kam kladku přišroubovat, může začít s <a href="/posilovaci-gumy/">posilovacími gumami</a> nebo se <a href="/zavesne-systemy-trx/">závěsným systémem</a>.</p>',
    faq=[
        ('Co je lepší, horní kladka na zeď, nebo posilovací věž?', 'Kladka na zeď zabere méně místa a je jednodušší. Věž nemusí kotvit do zdi a obvykle nabízí víc cviků, ale potřebuje větší půdorys.'),
        ('Jaký je rozdíl mezi převodem 1:1 a 2:1?', 'Při 1:1 cítíte na madle celou nastavenou hmotnost. Při 2:1 zhruba polovinu, zato lanko ujede dvakrát delší dráhu.'),
        ('Kolik kilogramů kladka unese?', 'Záleží na modelu. Maximální zatížení uvádí výrobce v parametrech a platí jen při montáži podle návodu.'),
        ('Můžu kladku přišroubovat do sádrokartonu?', 'Bez ověření a speciálního kotvení ne. Výrobci počítají s nosnou zdí nebo stropem, typ zdi a kotev uvádí návod.'),
        ('Jaké kotouče potřebuji na nakládací kladku?', 'Takové, jejichž otvor odpovídá průměru trnu. Hobby kotouče mívají otvor kolem 30 mm, olympijské kolem 50 mm.'),
        ('Dá se kladka přidat k power racku?', 'Ano, prodávají se nástavce s horní a spodní kladkou. Musí ale sedět na profil sloupků a rozteč otvorů vašeho stojanu.'),
        ('Jaká madla ke kladce koupit?', 'Kromě lat tyče se nejvíc hodí V madlo, tricepsové lano, jednoruční madlo a popruh na kotník.'),
        ('Jak často měnit lanko?', 'Kdykoli je poškozené: roztřepená vlákna, zlom nebo prodřený obal jsou důvod k okamžité výměně.'),
        ('Kde porovnat ceny posilovacích kladek?', 'Na Sportece u každé kladky a madla vidíte nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ pilates-reformery
NEW['pilates-reformery'] = dict(long=True,
    title='Pilates reformery: domácí, skládací i s věží',
    desc='Domácí a skládací pilates reformery, modely s věží, pružiny, boxy a náhradní díly. Kolik místa potřebujete, co porovnat a proč začít s lektorem.',
    intro='<p><strong>Pilates reformer</strong> je cvičební lehátko na kolejnicích. Na rámu jezdí pojízdný vozík s čalouněním, který je k jednomu konci připojený pružinami. Na druhém konci je opěrka nohou a z rámu vedou lana s poutky na ruce nebo chodidla. Cvičí se vleže, vsedě, vkleče i ve stoje a pružiny při tom jednou kladou odpor, jindy pohyb podpírají. Reformer vymyslel Joseph Pilates a cvičení na něm se dnes učí ve studiích i doma.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů na domácí a skládací reformery, modely s věží, dřevěné i hliníkové rámy a náhradní díly, jako jsou pružiny, boxy nebo odrazové plochy. Nejvíc modelů má v nabídce '
          + B(('insportline', 'Insportline')) +
          ', dále tu najdete například Sharp Shape, Myga nebo Yesoul. Reformery patří mezi <a href="/pilates-pomucky/">pilates pomůcky</a>. Nejde o zdravotnický prostředek a cvičení na něm nenahrazuje léčbu ani rehabilitaci.</p>',
    guide='<h2>Odkud reformer pochází</h2>'
          '<p>Joseph Pilates se narodil v Německu. Za první světové války byl v Británii internován jako německý státní příslušník na ostrově Man a už tam podle dochovaných vzpomínek cvičil s ostatními internovanými. V roce 1926 odešel do Spojených států a v New Yorku vyučoval svou metodu, kterou původně nazýval Contrology. Stroj, kterému dnes říkáme reformer, se tehdy jmenoval Universal Reformer. Současné reformery se od původního liší materiály a detaily, princip vozíku a pružin ale zůstal stejný.</p>'
          '<h2>Z čeho se reformer skládá</h2>'
          + T(['Část', 'K čemu slouží'], [
              ['Rám a kolejnice', 'nesou vozík, bývají ze dřeva, hliníku nebo oceli'],
              ['Vozík (carriage)', 'čalouněná plocha, na které ležíte nebo klečíte'],
              ['Pružiny', 'odpor a podpora pohybu, zapínají se jednotlivě'],
              ['Opěrka nohou (footbar)', 'tyč pro chodidla nebo ruce, nastavuje se do několika poloh'],
              ['Lana a poutka', 'tah rukama nebo nohama, délka se dá upravit'],
              ['Opěrka hlavy a ramen', 'drží hlavu a brání sklouznutí z vozíku'],
              ['Pilates box', 'podložka na vozík pro cviky vsedě a vleže na břiše'],
              ['Odrazová plocha', 'deska na konec rámu pro odrazy vleže'],
              ['Věž (tower)', 'rám nad reformerem s tyčí a pružinami pro další cviky']]) +
          '<p>U levnějších domácích modelů bývá část příslušenství jen za příplatek. Výrobci prodávají samostatně věže, boxy, odrazové plochy, vyplňující plošiny, které zakryjí prostor mezi vozíkem a koncem rámu, nebo náhradní opěrky ramen. Než si reformer vyberete, podívejte se, co je v balení a co se dá dokoupit později.</p>'
          '<h2>Pružiny a odpor</h2>'
          '<p>Pružiny jsou srdcem reformeru. Zapínají se jednotlivě a jejich kombinací se nastavuje odpor. Barevné značení není mezi výrobci jednotné, a proto ho vždy čtěte v návodu ke konkrétnímu stroji. Například Insportline u modelu Comfolder uvádí červenou pružinu do 20 kg, zelenou do 12 kg a žlutou do 7,5 kg.</p>'
          '<p>Vyšší odpor neznamená vždy těžší cvik. U některých pohybů pružina pomáhá, a když jí uberete, trup musí víc pracovat, aby vozík nejel nekontrolovaně. Začátečníci proto nemají cvičit „co nejtěžší“, ale s takovým nastavením, při kterém udrží pohyb pomalý a plynulý.</p>'
          '<p>Pružiny časem ochabují. Kontrolujte, jestli nemají mezery mezi závity, rez nebo ohnuté háky. Mění se obvykle celá sada najednou, aby měly stejné vlastnosti. Náhradní sady se prodávají pro konkrétní model, třeba Insportline nabízí šestici pružin právě ke Comfolderu.</p>'
          '<h2>Typy reformerů</h2>'
          '<p><strong>Skládací domácí reformer</strong> se po cvičení složí a odveze na kolečkách ke zdi. Rám bývá hliníkový nebo dřevěný a celý stroj je lehčí než studiový. <strong>Pevný reformer</strong> se nepřenáší, má masivnější rám a obvykle tišší chod vozíku. <strong>Reformer s věží</strong> přidává nad koncem rámu konstrukci s tyčí a dalšími pružinami. Rozšíří počet cviků, ale zvětší výšku stroje a s ní i nároky na místo.</p>'
          '<p>Kromě toho se prodávají přenosné „reformerové“ desky s gumovými lany. Jsou malé a lehké, ale nemají vozík na kolejnicích ani pružiny, takže skutečný reformer nenahradí. Hodí se spíš jako doplněk k cvičení na podložce.</p>'
          '<h2>Kolik místa reformer potřebuje</h2>'
          '<p>Reformer je dlouhý stroj. Například Insportline Comfolder má v rozloženém stavu podle výrobce 248,5 × 92 cm a výšku 28 cm a váží 68 kg. K rozměru stroje připočtěte volné místo kolem, kam při cvicích sahají ruce a nohy, a prostor pro nástup z boku. U modelu s věží změřte i výšku stropu.</p>'
          '<p>Skládací modely ušetří místo jen tehdy, když je opravdu budete skládat. Zkontrolujte, jak se stroj složí, kam se postaví a jestli zvládnete jeho hmotnost přesunout sami. Pod reformer se hodí podložka, která chrání podlahu a tlumí hluk. Výrobci také uvádějí maximální nosnost a doporučenou výšku cvičence, u Comfolderu je to 150 kg a 200 cm. Vysocí lidé by měli ověřit délku vozíku a počet poloh opěrky nohou.</p>'
          '<h2>Materiál rámu a chod vozíku</h2>'
          '<p>Dřevěné rámy z javoru, dubu nebo kaučukovníku vypadají jako nábytek a jsou tuhé, bývají ale těžší. Hliník je lehčí a hodí se pro skládací konstrukce. Ocel se objevuje hlavně v kloubech a dílech, které nesou zatížení. Pro pohodlí cvičení je důležitější chod vozíku: měl by jezdit plynule, bez cukání a s co nejmenším hlukem. Rozhodují o tom kolečka, ložiska a přesnost kolejnic.</p>'
          '<p>Některé modely uvádějí třídu podle normy EN ISO 20957. Třída H je určená pro domácí používání, třída S pro komerční provoz, například ve studiu. Stroj s třídou S snese častější používání, doma ji ale nutně nepotřebujete.</p>'
          '<h2>Jak začít cvičit</h2>'
          '<p>Pilates na reformeru vypadá jednoduše, ale vyžaduje správnou techniku. Doporučujeme začít několika lekcemi s lektorem, který ukáže nastavení pružin, polohu těla a bezpečný nástup na vozík. Základem je pomalý a řízený pohyb, plynulé dýchání a kontrola trupu. Doma pak můžete pokračovat podle naučených sestav nebo podle videí, ke kterým už máte základ.</p>'
          '<p>Kdo má potíže se zády, klouby nebo srdcem, je těhotná, po operaci či úrazu, měl by se před začátkem poradit s lékařem nebo fyzioterapeutem. Reformer se ve fyzioterapii používá, ale to neznamená, že domácí cvičení samo cokoli vyléčí. Při bolesti cvičení přerušte.</p>'
          '<h2>Bezpečnost a údržba</h2>'
          '<p>Pružiny přepínejte jen tehdy, když vozík stojí v klidu na dorazu. Nesestupujte z vozíku, dokud jsou pružiny napnuté, vozík by se prudce vrátil. Děti a zvířata držte během cvičení mimo dosah kolejnic. Cvičí se bosky nebo v ponožkách s protiskluzovou úpravou. Čalounění otírejte vlhkým hadříkem a vhodným čisticím prostředkem podle návodu, kolejnice udržujte bez prachu a pravidelně kontrolujte lana, poutka a šrouby.</p>'
          '<h2>Reformer, nebo cvičení na podložce</h2>'
          '<p>Pilates se dá cvičit i na obyčejné podložce bez jakéhokoli stroje. Podložka je levná, nezabírá místo a pro mnoho lidí je to dobrý začátek. Reformer přidává odpor pružin a pojízdný vozík, takže se stejný princip dá procvičit v mnoha dalších polohách. Pružiny také umožní některé cviky usnadnit, což ocení lidé, kterým jsou cviky na podložce zatím příliš těžké.</p>'
          '<p>Reformer je ale velký a dražší stroj. Než si ho domů koupíte, vyzkoušejte několik lekcí ve studiu. Zjistíte, jestli vás cvičení baví, jak často budete reformer používat a jaký typ vám vyhovuje. Teprve potom má smysl řešit model, rozměry a příslušenství.</p>'
          '<h2>Náhradní díly a doplňky</h2>'
          '<p>K reformerům se prodávají náhradní pružiny, lana, poutka, opěrky ramen, čalouněné potahy i podložky na vozík. Výrobci obvykle prodávají díly ke konkrétnímu modelu, proto při objednávce uvádějte přesný název stroje. Univerzální díly od jiného výrobce nemusí pasovat na úchyty ani mít stejnou sílu.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte rozměry v rozloženém i složeném stavu, hmotnost stroje, maximální nosnost, doporučenou výšku cvičence, počet a sílu pružin, počet poloh opěrky nohou a délku lan. Zjistěte, jestli je v balení box, odrazová plocha nebo věž a jestli jdou dokoupit. U skládacích modelů se zeptejte na způsob skládání a kolečka. Ověřte také dostupnost náhradních pružin a dílů, reformer slouží roky.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nákup bez změření místa včetně prostoru kolem stroje.</li>'
          '<li>Cvičení s co nejtěžšími pružinami místo s řízeným pohybem.</li>'
          '<li>Přepínání pružin, když je vozík vytažený.</li>'
          '<li>Začátek bez jediné lekce s lektorem.</li>'
          '<li>Opotřebované pružiny vyměněné jen po jedné.</li></ul>'
          '<p>K reformeru se hodí <a href="/joga-a-podlozky/">podložka</a> na cvičení vedle stroje, <a href="/joga-bloky/">jógové bloky</a>, <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/masazni-valce/">masážní válce</a> na protažení. Oblečení na cvičení najdete v kategoriích <a href="/leginy/">legíny</a> a <a href="/sportovni-podprsenky/">sportovní podprsenky</a>, další vybavení v sekci <a href="/joga-a-pilates/">jóga a pilates</a>.</p>',
    faq=[
        ('Co je pilates reformer?', 'Cvičební stroj s pojízdným vozíkem na kolejnicích, pružinami, opěrkou nohou a lany. Pružiny při cvičení kladou odpor nebo pohyb podpírají.'),
        ('Vejde se reformer do bytu?', 'Rozložený má přes dva metry na délku, například Comfolder 248,5 × 92 cm. Skládací modely se po cvičení odklidí ke zdi.'),
        ('Jaký je rozdíl mezi reformerem s věží a bez ní?', 'Věž je rám nad koncem reformeru s tyčí a pružinami, který rozšíří počet cviků. Stroj je pak vyšší a těžší.'),
        ('Co znamenají barvy pružin?', 'Sílu pružiny, ale značení není mezi výrobci jednotné. Vždy se řiďte návodem ke konkrétnímu reformeru.'),
        ('Můžu na reformeru cvičit bez lektora?', 'Jde to, ale na začátek doporučujeme několik lekcí s lektorem. Naučíte se nastavit pružiny a bezpečně nastupovat na vozík.'),
        ('Je reformer vhodný při bolestech zad?', 'Nejdřív se poraďte s lékařem nebo fyzioterapeutem. Reformer není zdravotnický prostředek a léčbu nenahrazuje.'),
        ('Jak často měnit pružiny?', 'Podle opotřebení a doporučení výrobce. Mezery mezi závity, rez nebo ohnuté háky jsou důvod k výměně celé sady.'),
        ('Je lepší dřevěný, nebo hliníkový reformer?', 'Dřevo je tuhé a vypadá jako nábytek, ale je těžší. Hliník je lehčí a hodí se pro skládací modely. Důležitý je hlavně plynulý chod vozíku.'),
        ('Kolik váží domácí reformer?', 'Záleží na modelu a materiálu. Například skládací Insportline Comfolder váží podle výrobce 68 kg.'),
        ('Kde porovnat ceny pilates reformerů?', 'Na Sportece u každého reformeru a náhradního dílu vidíte nabídky českých e-shopů a vyberete obchod, kde nakoupíte.'),
    ])

# ------------------------------------------------------------------ vibracni-plosiny
NEW['vibracni-plosiny'] = dict(long=True,
    title='Vibrační plošiny oscilační i vertikální',
    desc='Oscilační, vertikální a kombinované vibrační plošiny na domácí cvičení. Co je a co není prokázané, nosnost, programy a kdy se poradit s lékařem.',
    intro='<p><strong>Vibrační plošina</strong> je deska s elektromotorem, který ji rozkmitá. Na plošině se stojí, dělají se na ní podřepy, výpady nebo výdrže a vibrace se přenášejí do nohou a dál do těla. Doma se používá jako doplněk k běžnému cvičení, často spolu s gumami, které bývají v balení. Reklamy jí připisují kdeco od hubnutí po zpevnění postavy. Výzkum je ale mnohem opatrnější, a proto o něm níže píšeme otevřeně.</p>'
          '<p>Na Sportece jsou vedle sebe nabídky českých e-shopů na oscilační, vertikální i kombinované plošiny, menší desky bez držadla i modely se sloupkem a displejem. Najdete tu výrobky značek '
          + B(('hms', 'HMS'), ('insportline', 'Insportline'), ('merco', 'Merco')) +
          ', Tunturi, Fluxa nebo 4FIZJO. Plošiny patří mezi <a href="/masazni-pomucky/">masážní pomůcky</a>. Nejsou zdravotnickým prostředkem, nic neléčí a lidé se zdravotními potížemi by se měli před použitím poradit s lékařem.</p>',
    guide='<h2>Jak vibrační plošina funguje</h2>'
          '<p>Pod deskou je motor s nevyváženou hmotou nebo jiným mechanismem, který desku rozkmitá. Rychlost kmitání se udává jako frekvence v hertzích, tedy počet kmitů za sekundu. Rozkmit, tedy jak daleko se deska pohne, se nazývá amplituda a udává se v milimetrech. Obě hodnoty spolu určují, jak silně vibrace na těle cítíte. Domácí plošiny se ovládají tlačítky nebo dálkovým ovladačem a mají několik desítek až stovek stupňů intenzity a přednastavené programy.</p>'
          '<p>Stupně intenzity na displeji nejsou mezi výrobci srovnatelné. „Stupeň 50“ u jedné plošiny neříká nic o tom, jak silně kmitá jiná. Pokud výrobce uvádí rozsah frekvence a amplitudy, je to užitečnější údaj než počet stupňů.</p>'
          '<h2>Oscilační, vertikální a kombinované plošiny</h2>'
          + T(['Typ', 'Jak se deska pohybuje', 'Co uvádí odborná literatura'], [
              ['Oscilační (střídavá)', 'kolébá se jako houpačka kolem středové osy, chodidla se střídají', 'nižší frekvence, zhruba 5–35 Hz, větší rozkmit'],
              ['Vertikální (lineární)', 'celá deska se zvedá a klesá, obě chodidla najednou', 'vyšší frekvence, zhruba 20–50 Hz, menší rozkmit'],
              ['Kombinovaná', 'umí oba režimy, případně jejich střídání', 'záleží na konkrétním modelu']]) +
          '<p>U oscilační plošiny se rozkmit mění podle toho, jak široce stojíte. Čím dál od středu jsou chodidla, tím víc se deska pod nimi pohybuje. Užší postoj tedy znamená mírnější vibrace, širší silnější. Vertikální plošina kmitá pod oběma chodidly stejně a pocit bývá „bzučivější“.</p>'
          '<p>Na krabicích se objevují označení 3D, 4D nebo 5D. Nejde o normu, ale o obchodní pojmenování, které popisuje kombinaci směrů kmitání. U každého modelu proto čtěte, jaké pohyby deska skutečně dělá, a neporovnávejte plošiny podle počtu „D“.</p>'
          '<h2>Co je prokázané a co ne</h2>'
          '<p>Vibrační trénink se zkoumá desítky let, ale většina studií je malá, krátká a dělaná na konkrétním přístroji s konkrétním nastavením. Výsledky se proto špatně přenášejí na domácí plošinu. Přehledové práce o tukové hmotě u lidí s nadváhou zaznamenaly mírný účinek hlavně tam, kde se vibrace kombinovaly s úpravou jídelníčku nebo s cvičením. Samotné stání na plošině k výraznému hubnutí podle dostupných dat nevede.</p>'
          '<p>Výzkumy se týkají také svalové síly, rovnováhy nebo kostí u různých skupin lidí, například starších osob. Výsledky nejsou jednotné a nedá se z nich vyvodit, co plošina udělá právě vám. Proto ji berte jako doplněk, na kterém se dají dělat cviky s vlastní vahou, ne jako náhradu chůze, posilování nebo léčby. Tvrzení jako „vyplavuje toxiny“ nebo „hubnete bez námahy“ nemají oporu ve výzkumu.</p>'
          '<p>Vibrace se přenášejí i do hlavy. Měření ukázala, že ve stoje s mírně pokrčenými koleny se jich k hlavě dostane méně než s propnutými nohama a že u oscilačních plošin je přenos do hlavy nižší než u vertikálních. Na plošině proto nestůjte s natlačenými koleny.</p>'
          '<h2>Kdy se nejdřív poradit s lékařem</h2>'
          '<p>Výrobci uvádějí v návodech seznam stavů, při kterých se plošina nemá používat, nebo jen po souhlasu lékaře. Návody k vibračním strojům značky Insportline mezi nimi jmenují například těhotenství, akutní trombózu, onemocnění srdce a cév, kardiostimulátor, čerstvé pooperační jizvy, náhradu kyčelního nebo kolenního kloubu, kovové šrouby v těle, epilepsii, nádorové onemocnění, kýlu, potíže s ploténkami, cukrovku a těžkou migrénu. Seznam se liší model od modelu, vždy si ho přečtěte v návodu k vašemu stroji.</p>'
          '<p>Kdo si není jistý, ať se zeptá lékaře ještě před nákupem. Při bolesti na hrudi, závrati, nevolnosti nebo bušení srdce cvičení hned ukončete. Děti by měly plošinu používat jen pod dohledem a podle pokynů výrobce.</p>'
          '<h2>Jak se na plošině cvičí</h2>'
          '<p>Začněte s nízkou intenzitou a krátkou dobou a přidávejte postupně. Délku jednoho cvičení a celkový čas za den uvádí výrobce v návodu, držte se ho. Základní cviky jsou podřep, výdrž v podřepu, výpad s jednou nohou na plošině, prkno s rukama nebo předloktím na desce a protahování lýtek. S gumami připnutými k plošině se dají přidat přítahy a tlaky rukama.</p>'
          '<p>Plošina sama za vás necvičí. Když na ní jen stojíte, svaly pracují málo. Kdo chce posilovat, musí se hýbat stejně jako na zemi, jen na kmitající desce. Pokud se vám po cvičení točí hlava nebo vám je nepříjemně, snižte intenzitu nebo zkraťte čas.</p>'
          '<h2>Na co se dívat při výběru</h2>'
          '<ul><li><strong>Typ kmitání.</strong> Oscilační, vertikální nebo kombinovaná. Oscilační se hodí na nastavení síly šířkou postoje.</li>'
          '<li><strong>Maximální nosnost.</strong> Uvádí ji výrobce, počítejte s rezervou nad vlastní hmotností.</li>'
          '<li><strong>Frekvence a amplituda.</strong> Pokud je výrobce uvádí, dávají lepší představu než počet stupňů.</li>'
          '<li><strong>Velikost desky.</strong> Na širší desce se pohodlněji dělají výpady a cviky v kleku.</li>'
          '<li><strong>Držadlo.</strong> Plošina se sloupkem dává oporu, nízká deska bez sloupku je skladnější.</li>'
          '<li><strong>Ovládání a programy.</strong> Dálkový ovladač, časovač, případně aplikace v telefonu.</li>'
          '<li><strong>Příslušenství.</strong> Gumy, podložka pod plošinu, protiskluzový povrch.</li></ul>'
          '<h2>Umístění a údržba</h2>'
          '<p>Plošinu postavte na rovnou a pevnou podlahu, ideálně na gumovou podložku, která tlumí hluk a chrání podlahu. V bytovém domě počítejte s tím, že se vibrace a hluk mohou nést ke spodním sousedům. Kolem plošiny nechte volné místo pro případ, že ztratíte rovnováhu. Po cvičení desku otřete, přívodní kabel kontrolujte a před čištěním plošinu odpojte ze zásuvky. Děti si s plošinou nemají hrát bez dozoru.</p>'
          '<h2>Plošina se sloupkem, nebo nízká deska</h2>'
          '<p>Nízká deska bez držadla je lehká a po cvičení se dá zasunout pod postel nebo do skříně. Hodí se na podřepy, výpady, prkno a cviky v kleku. Chybí jí ale opora, takže na ní nemusí cvičit každý jistě. Plošina se sloupkem má držadlo s ovládáním a displejem. Můžete se jí přidržet, a proto ji častěji volí lidé, kteří si na kmitající desce nevěří. Je však větší a těžší a místo, kde stojí, se tím stává trvalým.</p>'
          '<p>Pokud plošinu budete po každém cvičení uklízet, zjistěte si její hmotnost a jestli má kolečka nebo madlo na přenášení. Těžkou plošinu bez koleček po čase přestanete vytahovat a skončí v rohu nepoužitá.</p>'
          '<h2>Pro koho plošina dává smysl</h2>'
          '<p>Plošinu ocení lidé, kteří doma rádi cvičí s vlastní vahou a chtějí ke cvikům přidat jiný podnět. Také tomu, kdo má doma málo místa a nechce velký trenažér. Naopak nemá smysl ji kupovat jako zkratku k hubnutí nebo jako náhradu procházek a pohybu venku. Pokud jste dosud necvičili vůbec, začněte s jednoduchými cviky na zemi a plošinu přidejte až později.</p>'
          '<p>Před nákupem si také ujasněte, kdo bude plošinu používat. Pokud ji chce sdílet více členů rodiny, ověřte nosnost pro toho nejtěžšího a zjistěte, jestli si každý může uložit vlastní nastavení. Pro starší lidi nebo pro ty, kdo si nejsou jistí rovnováhou, je bezpečnější model s držadlem. Zvažte i hlučnost motoru, pokud budete cvičit večer, když ostatní v bytě odpočívají.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U každé plošiny srovnejte typ kmitání, nosnost, rozměry a hmotnost desky, rozsah frekvence, příkon motoru, počet programů a obsah balení. Zkontrolujte, jestli má plošina časovač s automatickým vypnutím a v jakém jazyce je návod. Tvrzení o spálených kaloriích nebo o léčebných účincích při porovnávání ignorujte, nedají se ověřit.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Stání na plošině s propnutými koleny.</li>'
          '<li>Začátek na nejvyšší intenzitě a příliš dlouho.</li>'
          '<li>Spoléhání na plošinu místo pohybu a jídelníčku.</li>'
          '<li>Přehlédnutý seznam kontraindikací v návodu.</li>'
          '<li>Porovnávání modelů podle počtu stupňů nebo „D“.</li></ul>'
          '<p>Kdo hledá pohyb navíc doma, najde také <a href="/chodici-pasy/">chodicí pásy</a>, <a href="/steppery/">steppery</a> a <a href="/rotopedy/">rotopedy</a>. Na protažení a uvolnění slouží <a href="/masazni-valce/">masážní válce</a> a <a href="/masazni-pistole/">masážní pistole</a>, na rovnováhu <a href="/balancni-podlozky-bosu/">balanční podložky</a> a k posilování <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi oscilační a vertikální plošinou?', 'Oscilační deska se kolébá kolem středu a chodidla se střídají. Vertikální se zvedá a klesá celá. Oscilační obvykle kmitá pomaleji a s větším rozkmitem.'),
        ('Zhubnu na vibrační plošině?', 'Samotné stání na plošině podle dostupných studií k výraznému hubnutí nevede. Mírný účinek se ukázal spíš ve spojení s cvičením a úpravou jídelníčku.'),
        ('Je vibrační plošina zdravotnický prostředek?', 'Domácí plošiny ne. Slouží jako doplněk ke cvičení a nemohou slibovat léčebné účinky.'),
        ('Kdo by neměl používat vibrační plošinu?', 'Návody uvádějí například těhotenství, trombózu, kardiostimulátor, kloubní náhrady, epilepsii nebo čerstvé operace. Při zdravotních potížích se poraďte s lékařem.'),
        ('Jak dlouho cvičit na vibrační plošině?', 'Začněte krátce a s nízkou intenzitou. Délku cvičení a denní limit uvádí výrobce v návodu.'),
        ('Co znamená 3D nebo 4D plošina?', 'Obchodní označení kombinace směrů kmitání, ne norma. Čtěte, jaké pohyby deska skutečně dělá.'),
        ('Cvičit na plošině bosky, nebo v botách?', 'Řiďte se návodem k vašemu modelu. Bota tlumí část vibrací, naboso je cítíte silněji.'),
        ('Proč stát na plošině s pokrčenými koleny?', 'Pokrčená kolena tlumí vibrace, které by se jinak víc přenášely do hlavy a páteře.'),
        ('Může plošina stát v bytě v patře?', 'Ano, ale na gumové podložce. Vibrace a hluk se mohou přenášet ke spodním sousedům.'),
        ('Kde porovnat ceny vibračních plošin?', 'Sporteka u každé plošiny ukáže nabídky českých obchodů. Objednávku dokončíte v e-shopu, který si zvolíte.'),
    ])

# ------------------------------------------------------------------ zavesne-systemy-trx
NEW['zavesne-systemy-trx'] = dict(long=True,
    title='Závěsné systémy TRX a posilovací popruhy',
    desc='Závěsné posilovací systémy do dveří, na strop, hrazdu i ven. Jak se liší od TRX, jak je bezpečně ukotvit a nastavit a čím trénink doplnit.',
    intro='<p><strong>Závěsný systém</strong> tvoří dva nastavitelné popruhy s madly a poutky na nohy, které visí z jednoho kotevního bodu. Cvičí se jen s vlastní vahou: tělo se zaklání nebo předklání proti popruhům a odpor se mění úhlem a postavením nohou. Na jedné sadě se dají dělat přítahy, kliky, dřepy, výpady i cviky na břicho a celou výbavu unese běžný batoh. V Česku se všem závěsným systémům často říká TRX, i když jde o název jedné konkrétní značky.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů na závěsné posilovací systémy, kotvy do dveří a na strop, prodlužovací popruhy i varianty s pružným dílem. Najdete tu například výrobky '
          + B(('insportline', 'Insportline'), ('hms', 'HMS'), ('gymbeam', 'GymBeam')) +
          ', Sportago, Acra nebo Sedco. Kategorie patří do sekce <a href="/funkcni-trenink/">funkční trénink</a>. Na trénink s vlastní vahou se hodí také <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</p>',
    guide='<h2>Co je závěsný trénink</h2>'
          '<p>Princip je jednoduchý. Popruhy jsou ukotvené nad vámi a vy se o ně opíráte nebo za ně taháte. Čím víc se tělo blíží vodorovné poloze, tím větší část jeho hmotnosti zvedáte. Když stojíte skoro rovně, cvik je lehký. Když se zakloníte níž, je těžší. Stejný přítah tak zvládne začátečník i trénovaný sportovec, jen každý v jiném úhlu.</p>'
          '<p>Popruhy se při cvičení mírně houpou, a tak musí tělo samo držet rovnováhu. Do práce se zapojují svaly trupu i drobné svaly kolem ramen a kyčlí. Proto se závěsný trénink řadí k funkčnímu tréninku. Neznamená to, že nahradí těžké posilování s činkami. Je to jiný nástroj, který se dá vzít kamkoli.</p>'
          '<h2>TRX jako značka</h2>'
          '<p>TRX je obchodní značka americké firmy, kterou založil Randy Hetrick, bývalý příslušník jednotek Navy SEAL. Podle vyprávění firmy vznikl první prototyp během vojenského nasazení z pásku na jiu-jitsu a z padákových popruhů. Z vojenského prostředí se závěsný trénink rozšířil do posiloven a fitness studií a označení TRX se ujalo pro celý typ pomůcky.</p>'
          '<p>Závěsné systémy dnes vyrábí řada dalších firem. V katalogu najdete třeba Insportline MultiTrainer, HMS RXT, Sportago Variotrainer nebo sady značky Acra. Liší se materiálem popruhů, přezkami, madly, délkou a příslušenstvím. Principem fungují stejně.</p>'
          '<h2>Z čeho se závěsný systém skládá</h2>'
          '<ul><li><strong>Kotevní smyčka nebo popruh</strong>, který se obtočí kolem trámu, hrazdy či stromu nebo se připne ke kotvě.</li>'
          '<li><strong>Hlavní popruhy</strong>, buď dva samostatné, nebo jeden rozdělený do tvaru Y.</li>'
          '<li><strong>Přezky</strong> na rychlé zkracování a prodlužování popruhů.</li>'
          '<li><strong>Madla</strong> s pěnovým nebo gumovým potahem.</li>'
          '<li><strong>Poutka na nohy</strong> pro kliky, prkna a cviky na břicho s nohama v popruzích.</li>'
          '<li><strong>Kotva do dveří</strong>, obvykle silný pěnový válec na popruhu, který se zasune nad horní hranu dveří.</li></ul>'
          '<p>Některé sady mají v popruhu pružný díl, výrobci jim říkají bungee. Popruh se při zatížení trochu natáhne, takže pohyb je měkčí a víc pruží. Klasické popruhy jsou pevné a dávají přesnější odpor. Která varianta vám sedne, je věc vkusu. Pro začátek se lépe učí na pevných popruzích.</p>'
          '<h2>Kam závěsný systém ukotvit</h2>'
          + T(['Kotevní bod', 'Jak se používá', 'Na co dát pozor'], [
              ['Dveře', 'kotva přes horní hranu, dveře se zavřou', 'jen pevné dveře, zavřené a nejlépe zamčené'],
              ['Strop nebo trám', 'stropní úchyt přišroubovaný do nosné konstrukce', 'nosnost stropu a kotev podle návodu'],
              ['Hrazda nebo stojan', 'smyčka obtočená kolem tyče', 'hrazda musí být pevně ukotvená'],
              ['Venku', 'popruh kolem silné větve, sloupu nebo prolézačky', 'zdravý strom, popruh nesmí sklouznout'],
              ['Zeď', 'nástěnný úchyt přišroubovaný do nosné zdi', 'typ zdi a kotev podle výrobce']]) +
          '<p>TRX u svého přenosného úchytu počítá s kotvením ve výšce zhruba 2,1 až 2,7 metru (7 až 9 stop). Obecně platí, že kotevní bod má být nad hlavou, aby popruhy visely volně a dalo se v nich cvičit vleže i ve stoje.</p>'
          '<p>Kotva do dveří je nejpohodlnější, ale také nejvíc podceňovaná. Dveře musí být plné a pevné, lehké duté dveře mohou pod tahem povolit. Kotvu zasuňte nad horní hranu, dveře zavřete a pokud to jde, zamkněte, aby je během cvičení nikdo neotevřel. Cvičte na té straně, od které se dveře otvírají směrem pryč. Tah pak tlačí křídlo do zárubně a nespoléhá jen na zámek.</p>'
          '<p>Nikdy nekotvěte k věcem, které na to nejsou stavěné. Radiátor, garnýž, klika, háček na lustr nebo tenká větev mohou pod tahem povolit. Stropní úchyt patří do nosného stropu nebo trámu a montuje se podle návodu výrobce. Venku chraňte kůru stromu širokým popruhem a kontrolujte, jestli smyčka po stromě nesjíždí.</p>'
          '<h2>Nastavení délky a obtížnosti</h2>'
          '<p>Délka popruhů se nastavuje přezkami podle cviku. Na přítahy a cviky stojící čelem ke kotvě se popruhy obvykle prodlužují, na kliky s nohama v poutkách zkracují tak, aby poutka visela kousek nad zemí. Obtížnost pak měníte hlavně úhlem těla: krokem blíž ke kotevnímu bodu nebo dál od něj. Další možností je užší postoj, cvičení na jedné noze nebo pomalejší tempo.</p>'
          '<p>Při přítazích a klicích držte tělo rovně jako prkno, nenechte boky propadnout. Popruhy by se během cviku neměly odírat o paže a měly by být stále napnuté. Když povolí a pak se prudce napnou, zatěžuje to kotvu i klouby.</p>'
          '<h2>Bezpečnost a kontrola</h2>'
          '<p>Před každým tréninkem zkontrolujte švy, přezky a karabinu. Roztřepený popruh, prasklý šev nebo karabina, která nedovírá, jsou důvod sadu nepoužívat, dokud díl nevyměníte. Po ukotvení popruhy nejdřív postupně zatěžujte a teprve potom začněte cvičit naplno. Maximální zatížení uvádí výrobce a vztahuje se jen ke správnému ukotvení.</p>'
          '<p>Na závěsném systému se dá cvičit v každém věku, ale kdo začíná, ocení pár lekcí s trenérem nebo kvalitní video s výkladem techniky. Lidé s potížemi se zády, rameny nebo srdcem by se měli před začátkem poradit s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Péče o popruhy</h2>'
          '<p>Popruhy po cvičení venku nechte uschnout a neskladujte je vlhké. Dlouhé vystavení slunci popruhům škodí, proto je venku nenechávejte viset celé léto. Madla otírejte od potu. Pokud chcete popruhy prát, řiďte se návodem výrobce, ne každá sada snese pračku.</p>'
          '<h2>Základní cviky</h2>'
          '<ul><li><strong>Přítah ve vzporu ležmo vzad.</strong> Stojíte čelem ke kotvě, držíte madla, zakloníte se a přitahujete hrudník k rukám.</li>'
          '<li><strong>Tlak na hrudník.</strong> Stojíte zády ke kotvě, předkloníte se do popruhů a děláte klik ve stoje.</li>'
          '<li><strong>Dřep s oporou.</strong> Popruhy držíte před sebou a pomáhají vám udržet rovnováhu v hlubokém dřepu.</li>'
          '<li><strong>Výpad s nohou v poutku.</strong> Zadní noha visí v poutku a přední pracuje jako při bulharském dřepu.</li>'
          '<li><strong>Prkno s nohama v poutkách.</strong> Opíráte se o ruce nebo předloktí na zemi a nohy visí v popruzích.</li>'
          '<li><strong>Přitahování kolen k hrudníku.</strong> Ze vzporu s nohama v poutkách přitahujete kolena pod tělo.</li></ul>'
          '<p>Tyto cviky pokryjí celé tělo a dají se poskládat do krátkého kruhového tréninku. Začněte menším počtem opakování ve snadném úhlu a obtížnost zvyšujte, až když udržíte rovné tělo po celou dobu série.</p>'
          '<h2>Závěsný systém na cesty</h2>'
          '<p>Velkou výhodou závěsného systému je, že se vejde do malého vaku a váží málo. Na dovolené nebo služební cestě ho stačí uchytit do dveří hotelového pokoje nebo kolem stromu v parku. Než ho na cestách použijete, prohlédněte dveře i kotevní místo stejně pečlivě jako doma. Hotelové dveře bývají pevné, vestavěné skříně a lehké vnitřní dveře v pronajatých bytech ale nemusí tah vydržet.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte délku popruhů a rozsah nastavení, typ přezek, materiál madel, poutka na nohy a obsah balení. Zásadní je, jaké kotvy jsou součástí sady: kotva do dveří, smyčka na trám nebo strom, případně prodlužovací popruh. Stropní úchyty a nástěnné kotvy se často prodávají zvlášť. Sledujte také maximální zatížení, pokud ho výrobce uvádí, a záruku.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kotva v lehkých dutých dveřích nebo na straně, kam se dveře otvírají.</li>'
          '<li>Úchyt pověšený na radiátor, kliku nebo háček od lustru.</li>'
          '<li>Popruhy, které se během cviku povolí a prudce napnou.</li>'
          '<li>Cvičení s roztřepeným popruhem nebo vadnou karabinou.</li>'
          '<li>Propadlé boky při přítazích a klicích.</li></ul>'
          '<p>Závěsný trénink se dobře doplňuje s <a href="/kettlebelly/">kettlebelly</a>, <a href="/svihadla/">švihadly</a> a <a href="/posilovaci-gumy/">posilovacími gumami</a>. Na cviky na zemi se hodí <a href="/joga-a-podlozky/">podložka</a>, na přidání zátěže <a href="/zatezove-vesty/">zátěžové vesty</a>. Kdo má doma místo na pevnou konstrukci, může zvážit <a href="/posilovaci-kladky/">posilovací kladky</a>.</p>',
    faq=[
        ('Je TRX totéž co závěsný systém?', 'TRX je obchodní značka jedné americké firmy. Závěsné systémy dalších výrobců fungují na stejném principu a v Česku se jim často také říká TRX.'),
        ('Dá se závěsný systém ukotvit do dveří?', 'Ano, pomocí kotvy přes horní hranu. Dveře musí být pevné, zavřené a nejlépe zamčené a cvičí se na straně, od které se otvírají pryč.'),
        ('V jaké výšce má být kotevní bod?', 'Nad hlavou, aby popruhy visely volně. TRX u svého přenosného úchytu počítá s výškou zhruba 2,1 až 2,7 m.'),
        ('Jak změnit obtížnost cviku?', 'Hlavně úhlem těla: čím víc se blížíte vodorovné poloze, tím je cvik těžší. Pomůže i užší postoj nebo cvik na jedné noze.'),
        ('Je závěsný trénink vhodný pro začátečníky?', 'Ano, protože obtížnost se dá snížit stojem skoro vzpřímeně. Na začátek se vyplatí naučit techniku s trenérem nebo podle videa.'),
        ('Kolik závěsný systém unese?', 'Maximální zatížení uvádí výrobce a platí jen při správném ukotvení. Kotevní bod musí unést víc než popruhy samotné.'),
        ('Můžu závěsný systém pověsit na strom?', 'Ano, na silnou zdravou větev nebo kmen. Použijte široký popruh, který chrání kůru a nesjíždí.'),
        ('Jaký je rozdíl mezi pevnými popruhy a bungee?', 'Bungee má v popruhu pružný díl, takže pohyb víc pruží. Pevné popruhy dávají přesnější odpor a lépe se na nich učí technika.'),
        ('Jak se o popruhy starat?', 'Nechte je po použití uschnout, nenechávejte je dlouho na slunci a před tréninkem kontrolujte švy, přezky a karabinu.'),
        ('Kde porovnat ceny závěsných systémů?', 'Na Sportece u každé sady a kotvy vidíte nabídky českých e-shopů. Koupi dokončíte v obchodě podle vlastního výběru.'),
    ])

# ------------------------------------------------------------------ petanque
NEW['petanque'] = dict(long=True,
    title='Pétanque: sady koulí, turnajové koule a doplňky',
    desc='Rekreační sady i turnajové koule na pétanque, košonky, magnety a kruhy. Hmotnost a průměr podle pravidel FIPJP, tvrdost koulí a základní pravidla.',
    intro='<p><strong>Pétanque</strong> je francouzská hra s kovovými koulemi, ve které se hráči snaží dostat své koule co nejblíž k malé dřevěné kuličce zvané košonek. Hází se z kruhu, ve kterém hráč stojí oběma nohama na zemi, a hraje se na štěrku, udusané hlíně, písku i trávě. Hrát mohou jednotlivci, dvojice i trojice, děti i senioři. U nás se jí někdy říká i koulená.</p>'
          '<p>Na Sportece jsou vedle sebe nabídky českých e-shopů na rekreační sady v pouzdře či kufříku, turnajové koule po třech kusech, plastové sady pro děti, košonky, magnety na zvedání koulí, kruhy na házení i počítadla skóre. Mezi výrobci najdete například '
          + B(('decathlon', 'Decathlon')) +
          ' s řadou Geologic, Master nebo Obut. Pétanque patří mezi <a href="/hry-na-zahradu/">hry na zahradu</a>, ale stejně dobře se hraje v parku nebo na pláži.</p>',
    guide='<h2>Odkud pétanque pochází</h2>'
          '<p>Hra vznikla v Provence na jihu Francie jako odnož starší hry jeu provençal, při které se před hodem nabíhá. Tradice uvádí městečko La Ciotat a rok 1907, některé zdroje 1910. Podle vyprávění si hráč Jules Lenoir kvůli revmatu nemohl rozbíhat, a tak se začalo hrát z místa. Název pochází z provensálského výrazu pès tancats, tedy zhruba „nohy pevně na zemi“. Mezinárodní pravidla dnes vydává federace FIPJP, v Česku působí národní federace ČAPEK a kluby hrají vlastní soutěže.</p>'
          '<h2>Základní pravidla</h2>'
          '<p>Hrají proti sobě dva týmy. Podle pravidel FIPJP jsou to trojice, dvojice nebo jednotlivci. Ve trojicích má každý hráč dvě koule, ve dvojicích a jednotlivcích tři. Los určí, kdo začíná. Hráč začínajícího týmu nakreslí na zemi kruh o průměru 35 až 50 cm, nebo položí pevný kruh o vnitřním průměru 50 cm. Z kruhu hodí košonek do vzdálenosti 6 až 10 metrů.</p>'
          '<p>Potom tentýž tým hodí první kouli co nejblíž ke košonku. Další hází vždy ten tým, který „nemá bod“, tedy jehož nejbližší koule je od košonku dál než nejbližší koule soupeře. Hraje, dokud se mu nepodaří dostat blíž, nebo dokud mu nedojdou koule. Při hodu musí mít hráč obě nohy celé v kruhu a nesmí je zvednout, dokud koule nedopadne. Na hod má podle pravidel nejvýš jednu minutu.</p>'
          '<p>Když oba týmy dohrají všechny koule, kolo skončí. Body získá jen tým, jehož koule je nejblíž košonku, a to jeden bod za každou svou kouli, která je blíž než nejlepší koule soupeře. Další kolo začíná z kruhu nakresleného kolem místa, kde ležel košonek. Hraje se do 13 bodů.</p>'
          '<p>Hráči rozlišují dva způsoby hodu. <strong>Nahrávka</strong> (pointování) je hod, při kterém se koule snaží zastavit co nejblíž košonku. <strong>Střela</strong> je hod, kterým hráč vyrazí soupeřovu kouli nebo košonek z výhodné pozice. V týmech se role obvykle dělí podle toho, kdo co umí lépe.</p>'
          '<h2>Rekreační a turnajové koule</h2>'
          + T(['', 'Rekreační koule', 'Turnajové koule'], [
              ['Použití', 'zahrada, park, pláž, dovolená', 'oficiální soutěže a klubová hra'],
              ['Prodej', 'sady po 6 nebo 8 kusech s košonkem', 'obvykle sady po 3 kusech pro jednoho hráče'],
              ['Rozměry', 'často jeden průměr a hmotnost pro celou sadu', 'průměr 70,5–80 mm, hmotnost 650–800 g'],
              ['Značení', 'bez povinného značení', 'vyrytá značka výrobce a hmotnost'],
              ['Volba', 'stačí jedna sada pro celou partu', 'průměr, hmotnost a tvrdost podle hráče']]) +
          '<p>Turnajové koule musí podle pravidel FIPJP být kovové, mít průměr 70,5 až 80 mm a hmotnost 650 až 800 g. Na kouli musí být vyrytá značka výrobce a hmotnost a musí jít o model schválený federací. Koule se nesmí zatěžovat olovem ani plnit pískem. Děti do 11 let mohou v soutěžích pro svou kategorii hrát se schválenými koulemi o hmotnosti 600 g a průměru 65 mm.</p>'
          '<p>Rekreační koule takové podmínky splňovat nemusí. Bývají lehčí a menší, například rekreační sada Geologic od Decathlonu má koule o průměru 70 mm a hmotnosti 550 g a výrobce ji doporučuje na měkčí povrch, jako je písek nebo tráva. Na hru s rodinou úplně stačí. Kdo chce hrát v klubu nebo na turnajích, potřebuje schválené koule. Plastové a dřevěné sady jsou určené hlavně pro malé děti nebo na pláž.</p>'
          '<h2>Jak vybrat turnajové koule</h2>'
          '<p><strong>Průměr</strong> se volí podle velikosti ruky. Koule má v dlani sedět tak, aby ji prsty pohodlně obemkly a při hodu nevyklouzla. Menší ruce si obvykle volí menší průměr. Nejlepší je koule potěžkat v obchodě nebo si půjčit sadu od spoluhráčů v klubu.</p>'
          '<p><strong>Hmotnost</strong> souvisí s rolí ve hře. Decathlon doporučuje těžší koule hráčům, kteří hlavně nahrávají, a lehčí koule střelcům. Hmotnost ale musí především sedět vaší ruce, příliš těžká koule při delší hře unaví zápěstí.</p>'
          '<p><strong>Tvrdost</strong> se rozlišuje na tvrdé, polotvrdé a měkké koule. Tvrdší koule méně trpí poškozením a vydrží déle, zato víc odskakují. Měkčí koule po dopadu tolik neodskočí a lépe zůstanou ležet, ale rychleji se na nich dělají šrámy. Polotvrdé jsou kompromis, se kterým začíná mnoho hráčů.</p>'
          '<p><strong>Rýhování</strong> je vzor vyrytý na povrchu koule. Pomáhá rozlišit koule jednotlivých hráčů, takže se při měření nespletou. Hladké i rýhované koule jsou v soutěžích povolené, volba je otázkou zvyku a toho, co vám sedí v ruce.</p>'
          '<h2>Košonek</h2>'
          '<p>Košonek, francouzsky cochonnet, je malá kulička, ke které se hraje. Podle pravidel FIPJP je ze dřeva nebo ze schváleného syntetického materiálu a má průměr 30 mm s tolerancí jeden milimetr. Smí být natřený barvou, ale nesmí se dát zvednout magnetem. Barevný košonek je na štěrku lépe vidět. Vyplatí se mít v tašce jeden náhradní, protože se snadno ztratí v trávě.</p>'
          '<h2>Užitečné doplňky</h2>'
          '<ul><li><strong>Magnet na šňůrce</strong> na zvedání koulí ze země bez ohýbání.</li>'
          '<li><strong>Měřidlo nebo svinovací metr</strong> na rozhodnutí, čí koule je blíž.</li>'
          '<li><strong>Kruh na házení</strong>, pevný nebo skládací, aby se nemusel kreslit.</li>'
          '<li><strong>Počítadlo skóre</strong> na opasek nebo do kapsy.</li>'
          '<li><strong>Pouzdro nebo taška</strong> na tři koule, případně kufřík na celou sadu.</li>'
          '<li><strong>Hadřík</strong> na otření koulí od prachu a vlhkosti.</li></ul>'
          '<h2>Kde hrát</h2>'
          '<p>Nejlepší povrch je udusaná hlína s jemným štěrkem, jaký mají hřiště v parcích a klubech. Koule na něm dopadne a kutálí se předvídatelně. Na trávě nebo písku se hraje také, koule se ale zastaví dřív a hra je víc o štěstí. Pravidla FIPJP pro národní a mezinárodní soutěže vyžadují vymezený terén nejméně 15 × 4 metry, pro ostatní soutěže lze připustit menší, ale ne pod 12 × 3 metry. Na zahradě si vystačíte s menším prostorem, jen počítejte s tím, že koule letí i několik metrů za košonek.</p>'
          '<p>Při hře dbejte na bezpečnost. Kovová koule váží obvykle přes půl kila a může zranit, proto nikdo nesmí stát v dráze hodu a děti by měly hrát pod dohledem dospělých. Koule nikdy neházejte směrem k lidem, autům nebo oknům.</p>'
          '<h2>Péče o koule</h2>'
          '<p>Po hře koule otřete od prachu a vlhkosti a nechte je doma vyschnout. Decathlon doporučuje koule po každé hře otřít a zhruba jednou za měsíc lehce naolejovat, aby nerezavěly. Koule z nerezové oceli odolávají korozi lépe, koule z uhlíkové oceli bez péče rezivějí rychleji. Koule skladujte v suchu v pouzdře, ne v mokré tašce v garáži.</p>'
          '<h2>Pétanque s dětmi</h2>'
          '<p>Pro malé děti jsou turnajové koule příliš těžké. Začněte s plastovými nebo lehčími rekreačními koulemi a s kratší vzdáleností ke košonku. Děti si tak osvojí hod spodním obloukem a počítání bodů bez rizika, že si kouli pustí na nohu. Starší děti, které chtějí hrát v klubu, mohou v soutěžích své kategorie použít lehčí schválené koule.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U rekreační sady sledujte počet koulí, jejich průměr a hmotnost, materiál a povrch, obsah balení (košonek, metr, pouzdro) a to, zda jsou koule barevně odlišené pro dva týmy. U turnajových koulí ověřte schválení FIPJP, průměr, hmotnost, tvrdost a rýhování. Pro dva hráče, kteří chtějí hrát proti sobě, potřebujete dvě rozlišitelné trojice.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Turnajové koule vybrané jen podle vzhledu, bez ohledu na ruku.</li>'
          '<li>Rekreační sada koupená pro hru v soutěži.</li>'
          '<li>Koule uložené mokré, které pak zrezivějí.</li>'
          '<li>Hráč nebo dítě stojící v dráze hodu.</li>'
          '<li>Dvě sady stejného vzhledu, které se při měření nedají rozlišit.</li></ul>'
          '<p>K pétanque se na výlet hodí <a href="/piknikove-deky/">piknikové deky</a>, <a href="/kempingove-zidle/">kempingové židle</a> a <a href="/chladici-tasky/">chladicí tašky</a>. Další hry na venku najdete v kategoriích <a href="/discgolf/">discgolf</a> a <a href="/sipky/">šipky</a>.</p>',
    faq=[
        ('Kolik koulí má hráč v pétanque?', 'Podle pravidel FIPJP má hráč ve trojicích dvě koule, ve dvojicích a hře jednotlivců tři.'),
        ('Kolik váží koule na pétanque?', 'Turnajové koule váží 650 až 800 g a mají průměr 70,5 až 80 mm. Rekreační koule bývají lehčí.'),
        ('Jaký je rozdíl mezi rekreačními a turnajovými koulemi?', 'Turnajové jsou schválené federací FIPJP a mají vyrytou značku a hmotnost. Rekreační sady jsou na volnou hru a v soutěžích se používat nesmějí.'),
        ('Do kolika bodů se hraje pétanque?', 'Podle pravidel FIPJP do 13 bodů. Skupinové zápasy se mohou hrát do 11 bodů.'),
        ('Jak daleko se hází košonek?', 'Z kruhu do vzdálenosti 6 až 10 metrů. Pro nejmladší děti mohou soutěže určit kratší vzdálenost.'),
        ('Jaké koule zvolit, tvrdé, nebo měkké?', 'Tvrdé vydrží víc, ale víc odskakují. Měkké lépe zůstanou ležet, ale rychleji se poškrábou. Polotvrdé jsou kompromis.'),
        ('Jak se počítají body?', 'Po dohrání všech koulí boduje jen tým s koulí nejblíž košonku, jeden bod za každou kouli bližší než nejlepší koule soupeře.'),
        ('Na jakém povrchu se pétanque hraje?', 'Nejlépe na udusané hlíně s jemným štěrkem. Hrát se dá i na trávě nebo písku, koule se tam ale zastaví dřív.'),
        ('Jak se starat o koule na pétanque?', 'Po hře je otřít, nechat vyschnout a podle doporučení výrobce občas lehce naolejovat, aby nerezavěly.'),
        ('Kde koupit sadu na pétanque?', 'Sporteka u každé sady a koule ukáže nabídky českých obchodů. Nákup dokončíte v e-shopu, který si vyberete.'),
    ])
