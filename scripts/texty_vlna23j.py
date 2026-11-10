"""sporteka.cz — wave 23j (5. 11. 2026): long texts (>= 1650 words) for detska-kola-20-palcu, detske-spacaky, cyklo-lahve-a-drzaky, florbalove-hole.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detska-kola-20-palcu
NEW['detska-kola-20-palcu'] = dict(long=True,
    title='Dětská kola 20 palců: výška, převody, brzdy, výběr',
    desc='Dětská kola s 20palcovými koly pro školáky. Jak vybrat velikost podle výšky, převody, brzdy, odpružení a váhu, a porovnat nabídky obchodů.',
    intro='<p>Dvacetipalcové kolo je typická volba pro dítě, které už jezdí bez pomocných kolečků a chce se vydat na delší vyjížďky se spolužáky nebo rodinou. Obvykle sedí zhruba školákům na prvním stupni, ale rozhoduje výška, délka nohou a zkušenost, ne přesně dané datum narození. Sporteka porovnává nabídky českých obchodů u modelů s jedním převodem, s přehazovačkou i s odpružením a ukazuje, co se v popisu vyplatí hlídat: váhu, typ brzd, velikost rámu a výbavu.</p>'
          '<p>V kategorii najdete značky ' + B(('dino-bikes', 'Dino Bikes'), ('olpran', 'Olpran'), ('dhs', 'Dhs'), ('author', 'Author'), ('canellini', 'Canellini'), ('attabo', 'Attabo'), ('btwin', 'Btwin'), ('early-rider', 'Early Rider'), ('rockrider', 'Rockrider')) +
          '. Při růstu dítěte se hodí i sousední velikosti, <a href="/detska-kola-16-palcu/">16 palců</a> a <a href="/detska-kola-24-palcu/">24 palců</a>, a k novému kolu patří <a href="/detske-cyklohelmy/">dětská helma</a>.</p>',
    guide='<h2>Pro koho je 20palcové kolo</h2>'
          '<p>Velikost kol se u dětských kol uvádí v palcích a odpovídá průměru ráfku s pláštěm. Dvacítka bývá určená dětem, které překročily hranici šestnáctek, ale ještě se nevejdou na kolo s většími koly. Orientační tabulka pomáhá zúžit výběr, finální rozhodnutí ale udělá zkouška na sedle.</p>'
          + T(['Výška dítěte (orientačně)', 'Velikost kol', 'Poznámka'], [
              ['do zhruba 115 cm', '<a href="/detska-kola-16-palcu/">16 palců</a>', 'dvacítka by byla příliš velká a těžko ovladatelná'],
              ['zhruba 115 až 135 cm', '20 palců', 'nejčastější rozsah, rozhoduje délka nohou'],
              ['nad zhruba 135 cm', '<a href="/detska-kola-24-palcu/">24 palců</a>', 'dítě už by na dvacítce sedělo skrčeně']]) +
          '<p>Hodnoty berte jako vodítko, protože dvě děti stejné výšky mohou mít různě dlouhé nohy. Kolo je správně velké, pokud se dítě na sedle špičkami dotkne země a při jízdě má lehce pokrčené koleno v nejnižší poloze pedálu. Řídítka by měla být v dosahu bez nuceného předklonu. Příliš velké kolo děti odradí, protože se bojí rozjezdu a zastavení, příliš malé zase brzy přestane stačit.</p>'
          '<h2>Typy dětských kol v této velikosti</h2>'
          '<p>Nabídka se dělí podle toho, kde chce dítě jezdit. Část modelů vychází z horských kol, část z městských, další jsou stylizované podle oblíbených postaviček a mají košík, zvonek nebo blatníky v základní výbavě.</p>'
          '<ul><li><strong>Jednorychlostní kola:</strong> jednoduchá, lehká a nenáročná na seřízení. Hodí se na rovinu, dvůr a cesty kolem domu.</li>'
          '<li><strong>Kola s přehazovačkou:</strong> mají obvykle šest nebo sedm převodů a dítě se naučí řadit. Hodí se tam, kde se jezdí do kopců.</li>'
          '<li><strong>Odpružená kola:</strong> přední vidlice s pružinou vypadá jako u dospělého horského kola. U levných kusů ale může zvýšit váhu a poskytovat jen symbolický zdvih.</li>'
          '<li><strong>Městská a trekingová provedení:</strong> mají blatníky, nosič a světla, takže se hodí na dojíždění do školy nebo kroužků.</li></ul>'
          '<p>Ke starším dětem, které chtějí terén, se hodí širší pohled do kategorie <a href="/horska-kola/">horských kol</a>, i když dospělé velikosti už 20palcové dítě neunese. Pro mladší sourozence jsou tu <a href="/detska-kola-12-14-palcu/">kola 12 a 14 palců</a>, <a href="/odrazedla/">odrážedla</a> a <a href="/detske-trikolky/">tříkolky</a>.</p>'
          '<h2>Váha je důležitější, než se zdá</h2>'
          '<p>Dítě s dvacítkou váží často méně než třicet kilogramů a kolo, které váží devět nebo deset kilogramů, je pro něj proporčně stejně těžké, jako by dospělý nesl kolo o váze dvaceti kilo. Lehké kolo se snáze rozjíždí, zatáčí i zvedá přes obrubník a dítě ho zvládne samo opřít nebo vynést do schodů. Hliníkový rám bývá lehčí než ocelový a nerezaví. Ocel je zase odolnější vůči pádům, ale váha stoupá. Při porovnání nabídek proto vždy hledejte údaj o hmotnosti, ne jen o velikosti rámu.</p>'
          '<h2>Brzdy a bezpečnost</h2>'
          '<p>Dětské ruce mají menší sílu, takže brzdové páčky s nastavitelným dosahem jsou velká výhoda. Na dvacítkách najdete tyto systémy:</p>'
          + T(['Brzda', 'Jak funguje', 'Na co dát pozor'], [
              ['Zpětlapková (torpédo)', 'brzdí se šlápnutím pedálů dozadu', 'dítě zvládne brzdit i s rukama na řídítkách, ale účinek bývá slabší'],
              ['V-brake', 'čelisti tlačí na ráfek', 'nejběžnější, vyžaduje seřízení a čisté ráfky'],
              ['Kotoučová', 'třmen stlačuje kotouč na náboji', 'silnější brzdění za mokra, potřebuje pravidelnou kontrolu']]) +
          '<p>Mnoho modelů kombinuje zpětlapkovou brzdu vzadu a ruční vpředu. Naučte dítě používat obě a brzdit nejdřív lehce, ne prudce přední brzdou. Kolo má mít zvonek, odrazky vpředu i vzadu a v provozu na silnici i světla, viz <a href="/cyklo-svetla/">světla na kolo</a> a <a href="/cyklo-zvonky-a-zrcatka/">zvonky</a>.</p>'
          '<h2>Výbava, která se vyplatí</h2>'
          '<p>K základní výbavě patří přilba, kterou stanoví zákon pro děti do osmnácti let, tedy vyberte správně velkou <a href="/detske-cyklohelmy/">dětskou cyklohelmu</a>. Dále přijdou vhod <a href="/cyklisticke-rukavice/">rukavice</a> proti odřeným dlaním, <a href="/cyklo-chranice/">chrániče kolen a loktů</a> pro začátečníky v terénu, malá <a href="/cyklo-lahve-a-drzaky/">láhev s držákem</a> a <a href="/cyklo-zamky/">zámek</a>, pokud dítě odkládá kolo před školou.</p>'
          '<h2>Jak kolo seřídit</h2>'
          '<ol><li>Výška sedla: špičky se dotýkají země, v dolní poloze pedálu zůstává koleno mírně pokrčené.</li>'
          '<li>Sklon sedla: vodorovně, aby dítě nesklouzávalo dopředu.</li>'
          '<li>Řídítka: v takové výšce, aby záda nebyla příliš skloněná a dítě mělo hlavu zvednutou.</li>'
          '<li>Páčky brzd: dosah nastavte tak, aby dítě bez problému obemklo páčku celou dlaní.</li>'
          '<li>Tlak v pláštích: podle údaje na boku pláště, nižší tlak kolo zpomaluje.</li></ol>'
          '<h2>Rámy, pláště a zapomenuté detaily</h2>'
          '<p>Rám dětského kola bývá z oceli nebo hliníku. U dětských kol se často nevyplatí řešit jemné rozdíly v kvalitě hliníkové slitiny, důležitější je, aby rám neměl ostré hrany, aby kryty řetězu skutečně chránily nohavici a aby vodiče lanek nebyly přehnutě ostré. Pláště s mírným vzorkem dobře fungují na asfaltu i na polňačce, příliš hrubý terénní běhoun naopak zbytečně brzdí. Pokud kolo stojí často venku, ocení se nerezové šrouby a ochrana proti korozi.</p>'
          '<p>Stranou se často zapomíná na pedály. Plastové jsou lehké a nebolí při pádu, kovové s ostrými hranami mohou zranit lýtko. Pružné rukojeti by měly mít zátky na koncích, aby se řídítko nezabodlo do dlaně.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li><strong>Kolo na vyrůstání:</strong> příliš velké kolo je nebezpečné. Zvolte maximálně o malou rezervu více, ne o celou velikost.</li>'
          '<li><strong>Nejnižší cena bez čtení popisu:</strong> levné kolo bývá nejtěžší a bývá bez základních prvků, třeba odrazek nebo krytu řetězu.</li>'
          '<li><strong>Zbytečné odpružení:</strong> pružná vidlice u nejlevnějších kol nepomáhá a zvyšuje váhu.</li>'
          '<li><strong>Chybějící seřízení:</strong> kolo z balíku vyžaduje dotažení šroubů a seřízení brzd. Ověřte to před první jízdou.</li>'
          '<li><strong>Zapomenutá přilba:</strong> bezpečnostní výbava patří do rozpočtu hned na začátku.</li></ul>'
          '<h2>Péče a údržba</h2>'
          '<p>Po jízdě v blátě kolo otřete vlhkým hadrem a řetěz lehce promažte. Jednou za několik týdnů zkontrolujte tlak v pláštích a dotažení šroubů na sedle a řídítkách. Pláště, které začínají praskat, nebo brzdové špalky opotřebené až na kov, vyměňte. Základní nářadí a pumpa se vejdou do <a href="/cyklo-pumpy-a-naradi/">sady pro opravu</a>, kterou zvládne s dospělým i dítě. Na zimu kolo uložte do sucha, nejlépe tak, aby nestálo celou váhou na jedné pneumatice.</p>'
          '<h2>Co dělat, když dítě vyroste</h2>'
          '<p>Dvacítka vydrží zhruba dva až čtyři roky, podle toho, jak rychle dítě roste. Sedlovku a řídítka lze zvednout, ale limit je dán délkou rámu. Až dítě sedí skrčeně a kolena se zvedají k hrudníku, je čas přejít na <a href="/detska-kola-24-palcu/">24 palců</a> nebo na <a href="/detska-elektrokola/">dětské elektrokolo</a>, pokud rodina plánuje delší trasy. Staré kolo lze předat mladšímu sourozenci, proto se vyplatí neutrální barva a pravidelná údržba.</p>'
          '<h2>Jak na Sportece vybrat</h2>'
          '<p>U každého modelu vidíte nabídky více obchodů a rozdíly v dostupnosti i dopravě. Filtrujte podle značky, porovnejte parametry v popisu a ověřte, zda je kolo dodáváno smontované, nebo ve stavebnici. Pokud váháte mezi velikostmi, změřte dítěti délku nohy a zkuste kolo v obchodě nebo u kamaráda. Pro širší přehled otevřete <a href="/detska-kola/">všechna dětská kola</a>.</p>',
    faq=[
        ('Pro jak staré dítě je kolo s 20palcovými koly?', 'Nejčastěji pro děti zhruba od šesti do devíti let, ale věk je jen vodítko. Rozhoduje výška, délka nohou a zkušenost s ježděním. Správná velikost je taková, kde dítě na sedle dosáhne špičkami na zem a může bezpečně brzdit.'),
        ('Jak poznám, že dítě z 16palcového kola vyrostlo?', 'Kolena se při šlapání zvedají k hrudníku, sedlo je vytažené na maximum a dítě sedí skrčeně. Vyzkoušejte také, jestli se řídítka dostanou do pohodlného úchopu. Pokud ano a nohy jsou dlouhé, je čas na dvacítku.'),
        ('Je lepší jednorychlostní kolo, nebo kolo s přehazovačkou?', 'Jedna rychlost je lehčí a jednodušší, takže se hodí do rovinatého terénu. Přehazovačka pomůže v kopcích a naučí dítě řadit, ale vyžaduje seřízení a občasnou údržbu. Pro dítě, které zatím jezdí jen po dvoře, stačí jeden převod.'),
        ('Má smysl kolo s odpružením?', 'U dětí na lesních cestách a v terénu může pomoci, pokud je vidlice kvalitní a nastavitelná. U levných kol má odpružení často jen symbolický zdvih a zvyšuje váhu. Pro jízdu po silnici a po zpevněných cestách je pevná vidlice praktičtější.'),
        ('Jaké brzdy jsou pro dítě nejvhodnější?', 'Dobře fungují kombinace zpětlapkové brzdy a jedné ruční brzdy. Důležitý je nastavitelný dosah páčky, aby ji dítě pohodlně obemklo. Kotoučové brzdy mají větší sílu, ale jejich seřízení je náročnější a bývají jen u dražších modelů.'),
        ('Jak těžké má dětské kolo být?', 'Čím lehčí, tím lépe. Dítě, které váží kolem dvaceti pěti kilo, těžko ovládá kolo o hmotnosti desítek procent své váhy. Při porovnání nabídek proto hledejte údaj o váze a upřednostněte hliníkový rám před ocelovým, pokud rozpočet dovolí.'),
        ('Jakou helmu k dvacítce koupit?', 'Helma musí sedět těsně, nesmí se kývat a má zakrývat čelo. Změřte obvod hlavy a vyberte velikost podle tabulky výrobce. V kategorii dětských helem najdete modely s nastavitelným kolečkem na týlu, které se dají upravit při růstu.'),
        ('Koupit kolo ve stavebnici, nebo smontované?', 'Pokud nemáte zkušenosti, volte smontované nebo nechte kolo seřídit v servisu. Špatně dotažená řídítka nebo nenastavené brzdy jsou častou příčinou pádů. V popisu u nabídky obchodu obvykle stojí, v jakém stavu se kolo dodává.'),
        ('Jak dlouho dvacítka vydrží?', 'Obvykle dva až čtyři roky, podle toho, jak rychle dítě roste a jak moc jezdí. Sedlo a řídítka lze zvyšovat jen do určité míry. Když kolo dobře udržujete, vydrží i pro mladšího sourozence nebo se dá předat dál.'),
        ('Mohu na dvacítku přidat zadní nosič nebo sedačku?', 'Nosič pro malou brašnu je možný, pokud rám má závity pro jeho upevnění. Sedačku pro dalšího pasažéra nepoužívejte, dětské kolo na to není stavěné. Pro přepravu věcí je lepší batoh nebo menší brašna přímo na rámu.')
    ])

# ------------------------------------------------------------------ detske-spacaky
NEW['detske-spacaky'] = dict(long=True,
    title='Dětské spacáky: teplota, délka, výplň, rostoucí modely',
    desc='Dětské spacáky na stan, chatu i přespávání u kamarádů. Jak vybrat teplotu, délku, výplň a tvar, a porovnat nabídky českých obchodů.',
    intro='<p>Dětský spacák má stejný úkol jako dospělý: udržet teplo těla během spánku. Je ale menší, lehčí a často rostoucí, takže se hodí na několik sezón. Na Sportece porovnáte nabídky českých obchodů u modelů pro přespávání ve stanu, na chatě, na táboře i u babičky na gauči. Najdete tu spacáky dekové, mumiové, s nastavitelnou délkou i hedvábné vložky, které slouží jako lehká přikrývka v létě.</p>'
          '<p>V kategorii jsou zastoupeny značky ' + B(('husky', 'Husky'), ('highlander', 'Highlander'), ('skandika', 'Skandika'), ('nils-camp', 'NILS Camp'), ('deuter', 'Deuter'), ('crossroad', 'Crossroad'), ('loap', 'Loap'), ('easy-camp', 'Easy Camp'), ('outwell', 'Outwell'), ('cocoon', 'Cocoon'), ('quechua', 'Quechua')) +
          '. Spacák se nejlépe doplňuje s <a href="/karimatky-a-matrace/">karimatkou nebo matrací</a>, protože nejvíc tepla se ztrácí směrem do země.</p>',
    guide='<h2>Jak se dětský spacák liší od dospělého</h2>'
          '<p>Dětské tělo vychládá rychleji než dospělé, protože má menší hmotnost a poměrně velký povrch. Spacák proto musí těsněji obepínat a zároveň neomezovat pohyb, protože děti se ve spánku často převalují. Správně zvolená délka je pro teplo důležitější než pár stupňů navíc: příliš dlouhý pytel nechává prázdné místo, které dítě musí vyhřát, a konec se navíc může zamotat kolem nohou.</p>'
          '<p>Rozdíl je i v zapínání. Zipy mají mít jezdec, který dítě zvládne ovládat, a ochrannou lištu proti zachytávání látky. Kapuce se stahuje šňůrkou, která by neměla být dlouhá, aby se nedostala kolem krku.</p>'
          '<h2>Typy dětských spacáků</h2>'
          + T(['Typ', 'Vlastnosti', 'Hodí se pro'], [
              ['Dekový', 'obdélníkový tvar, dá se rozepnout na přikrývku', 'léto, chata, přespání uvnitř, rodinné kempování, viz <a href="/dekove-spacaky/">dekové spacáky</a>'],
              ['Mumiový', 'zužuje se k nohám, kapuce kolem hlavy', 'chladnější noci a ve stanu, kde záleží na teple'],
              ['Rostoucí', 'zip nebo vložka na konci prodlužuje délku', 'děti, které rychle rostou'],
              ['Spací vložka', 'tenká látka bez izolace', 'horké noci a ochrana před špínou, viz <a href="/vlozky-do-spacaku/">vložky do spacáků</a>']]) +
          '<p>Pro vyšší nároky, tedy zimní tábory nebo horské túry, existují i <a href="/perove-spacaky/">péřové spacáky</a>. Pro děti jsou ale méně praktické, protože péří nesmí zmoknout a údržba je náročnější. Hlavní nabídku tak tvoří syntetika, která snese i vlhčí prostředí.</p>'
          '<h2>Teplotní rozsah: jak ho číst</h2>'
          '<p>Výrobci uvádějí několik teplot: komfortní, limitní a extrémní. Komfortní je ta, při které by se průměrná osoba měla v pytli pohodlně vyspat. Limitní je hranice pro skrčenou polohu a už není moc příjemná. Extrémní teplota je nouzový údaj, ne cíl nákupu. Dětem doporučujeme řídit se komfortní teplotou a přidat pár stupňů rezervy, protože se v noci hůř zahřívají.</p>'
          '<p>Ve skutečnosti rozhodují i podložka, oblečení a vlhkost. Pokud dítě spí v zimním oblečení, spacák ho může sevřít a izolace se zhutní, takže zahřeje hůř. Dítěti postačí lehké termoprádlo, například z kategorie <a href="/termopradlo/">termoprádlo</a>, a čepice na hlavu.</p>'
          '<h2>Výplň a materiál</h2>'
          '<p>Syntetická výplň z dutých vláken se pere snadněji, rychle schne a izoluje i vlhká. Dětem se hodí proto, že se spacák občas zašpiní, zmokne nebo se na něm někdo svezne po blátě. Vnější látka bývá z polyesteru a lehce odpuzuje vodu, ale dešti nevydrží. Vnitřní strana je často bavlněná nebo flísová. Bavlna je příjemná na kůži, ale pomaleji schne, fleece je hřejivý a lehčí, ale hůř odvádí vlhkost.</p>'
          '<p>Některé spacáky mají pevnější látku, která snese kontakt s dřevem v chatě. Hedvábné vložky od značky Cocoon se hodí na horkých nocích a na ochranu před cizí postelí.</p>'
          '<h2>Velikost a délka</h2>'
          '<p>Při výběru dejte přednost délce, která odpovídá výšce dítěte plus malé rezervě na hlavu. Spacák o dvacet centimetrů delší je v pořádku, o padesát už nikoli. Rostoucí modely mají vyztužený konec, který se prodlouží zipem, a hodí se pro děti, které rostou po spurtech. Při zmenšení se konec složí a zajistí. U mumiových pytlů zkontrolujte šířku v ramenou, aby dítě nebylo sevřené, a obvod u kolen.</p>'
          '<h2>Kam spacák vybírat</h2>'
          '<ul><li><strong>Přespávání u kamarádů:</strong> lehký deka spacák se zapínáním a nenáročnou údržbou.</li>'
          '<li><strong>Dětský tábor:</strong> střední teplotní rozsah, odolná látka, popruh na přenášení.</li>'
          '<li><strong>Stanování s rodinou:</strong> teplejší mumie nebo rostoucí model a vhodná podložka.</li>'
          '<li><strong>Chata nebo pokoj:</strong> léto na dece, v zimě spacák s kapucí, protože dům může být vychladlý.</li>'
          '<li><strong>Zahrádka a hamak:</strong> lehká přikrývka nebo spací vložka.</li></ul>'
          '<h2>Co přibalit kolem spacáku</h2>'
          '<p>Spacák není celý spací systém. Důležitá je <a href="/karimatky-a-matrace/">karimatka</a> s dostatečnou izolací, která odděluje dítě od země. U stanu pomůže <a href="/detske-stany/">dětský stan</a> na zahradu nebo <a href="/rodinne-stany/">rodinný stan</a> na delší pobyt. Přes noc se může hodit <a href="/celovky-a-svitilny/">čelovka</a>, aby dítě našlo cestu na toaletu, a malý polštářek nebo nafukovací podhlavník. Do batohu se spacák vejde v kompresním obalu, ale nenechávejte ho v něm dlouhodobě, výplň by ztratila nadnos.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po akci spacák vyvětrejte, vytřepejte a nechte úplně vyschnout, než ho uložíte. Pere se podle štítku, obvykle v pračce na šetrný program a s jemným prostředkem bez aviváže. Skladujte ho volně, ve velkém pytli nebo zavěšený, ne stlačený. Zip občas přejeďte svíčkou nebo voskem, pokud drhne, a vyhněte se silnému tahu. Drobné díry v látce zalepte záplatou, aby z nich nevytékala výplň.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Příliš velký spacák:</strong> dítě v něm trpí zimou, protože prázdný prostor nezahřeje.</li>'
          '<li><strong>Pouze spacák bez podložky:</strong> zem odvádí teplo i v létě.</li>'
          '<li><strong>Vlhký spacák po víkendu:</strong> bez sušení vzniká zápach a plíseň.</li>'
          '<li><strong>Oblékání do silné bundy:</strong> stlačená izolace nehřeje a zip se zasekává.</li>'
          '<li><strong>Zamlčená velikost:</strong> u dětí se vyplatí zkusit spacák doma před akcí, ověřit zip a tvar kapuce.</li></ul>'
          '<h2>Jak vybírat na Sportece</h2>'
          '<p>Zvolte typ podle plánovaného využití, pak porovnejte teplotní údaje a délku. U každého produktu vidíte nabídky více obchodů a rozdíly v dopravě i dostupnosti barev. Pokud je kategorie příliš široká, vyjděte z nadřazené <a href="/spaci-pytle/">kategorie spacích pytlů</a> a z outdoorového vybavení, například <a href="/kemping/">kempingu</a>, <a href="/turisticke-batohy/">turistických batohů</a> a <a href="/hamaky/">hamaků</a>. Nezapomeňte, že děti potřebují teplo, ne rekordní lehkost, proto raději vybírejte o stupeň hřejivější spacák.</p>',
    faq=[
        ('Jakou teplotu má dětský spacák zvládnout?', 'Řiďte se komfortní teplotou, ne extrémní. Pro letní přespávání ve stanu stačí spacák s komfortním rozsahem kolem deseti stupňů, na jaro a podzim volte teplejší. Dětem přidejte rezervu pár stupňů, protože se v noci zahřívají hůř než dospělí.'),
        ('Je lepší dekový, nebo mumiový spacák?', 'Dekový je pohodlnější a hodí se do tepla nebo na chatu, protože se dá rozepnout jako přikrývka. Mumiový lépe drží teplo díky úzkému tvaru a kapuci. Pro dítě, které se hodně vrtí, je volnější deka příjemnější, ve stanu za chladu se ale hodí mumie.'),
        ('Má smysl rostoucí dětský spacák?', 'Ano, pokud dítě rychle roste. Prodloužení konce zipem nebo vložkou přidá deset až dvacet centimetrů, takže spacák vydrží více sezón. Nevýhodou může být vyšší hmotnost a složitější konstrukce, ale praktický rozdíl je malý.'),
        ('Jak dlouhý spacák vybrat?', 'Délka by měla odpovídat výšce dítěte plus malé rezervě, nejvýše dvacet centimetrů. Příliš dlouhý pytel nechává prázdný prostor, který se nezahřeje. U rostoucího modelu zvolte základní délku a využijte prodloužení až při růstu.'),
        ('Z čeho je výplň dětských spacáků?', 'Nejčastěji ze syntetických dutých vláken, která se dobře perou a rychle schnou. Péřové spacáky jsou lehčí a teplejší, ale po zmoknutí ztrácejí izolaci a vyžadují šetrnější péči. Pro děti se většinou hodí syntetika.'),
        ('Může dítě spát ve spacáku v zimním oblečení?', 'Nedoporučuje se. Silné oblečení stlačí výplň a spacák pak hřeje hůř, navíc dítěti brání v pohybu. Lepší je lehké termoprádlo, ponožky a čepice. Pokud je zima, zvolte spacák s nižší komfortní teplotou.'),
        ('Jak spacák vyprat?', 'Podívejte se na štítek. Většina syntetických spacáků jde prát v pračce na šetrný program s jemným prostředkem, bez aviváže. Důkladně vymáchejte a nechte úplně vyschnout, případně v sušičce na nízkou teplotu s tenisovými míčky pro rozdýchání výplně.'),
        ('Potřebuji k dětskému spacáku i karimatku?', 'Ano. Zem odvádí teplo podstatně víc než vzduch a spodní část spacáku se pod váhou těla stlačí. Karimatka nebo nafukovací matrace tak patří k základu. Vybírejte podle roční doby a hodnoty izolace uvedené u produktu.'),
        ('K čemu je spací vložka z hedvábí?', 'Hedvábná nebo bavlněná vložka funguje jako lehká přikrývka v létě a chrání spacák před potem a špínou. Vložku lze prát častěji než samotný spacák. Přidá také pár stupňů tepla, ale netvoří náhradu za izolaci.'),
        ('Jak dlouho spacák vydrží?', 'Při správné péči i několik sezón. Důležité je sušení, skladování bez stlačení a včasná oprava zipu a prošívání. Rostoucí modely se dají předat mladšímu sourozenci, takže se investice vrací.')
    ])

# ------------------------------------------------------------------ cyklo-lahve-a-drzaky
NEW['cyklo-lahve-a-drzaky'] = dict(long=True,
    title='Cyklo lahve, košíky a držáky telefonu na kolo',
    desc='Cyklistické lahve, košíky na bidon a držáky telefonu na řídítka. Jak vybrat objem, materiál, uchycení a porovnat nabídky českých obchodů.',
    intro='<p>Pití na kole se musí dát vzít jednou rukou, za jízdy a bez zastavení. Právě proto existují bidony se sportovním víčkem a košíky, které je drží na rámu i při nárazech. Druhým pomocníkem je držák telefonu, který udrží navigaci na očích a chrání přístroj před otřesy. Sporteka porovnává nabídky českých obchodů u lahví, košíků, držáků a příbuzných drobností, abyste našli kus pro silnici, terén i městské dojíždění.</p>'
          '<p>V kategorii najdete značky ' + B(('rockbros', 'Rockbros'), ('kellys', 'Kellys'), ('lifefit', 'Lifefit'), ('sp-connect', 'SP Connect'), ('quechua', 'Quechua'), ('max1', 'Max1'), ('fidlock', 'Fidlock'), ('fixed', 'Fixed'), ('nite-ize', 'Nite IZE')) +
          '. K tomu se hodí <a href="/cyklo-tasky-a-nosice/">brašny a nosiče</a>, <a href="/cyklo-computery/">cyklocomputery</a> a <a href="/cyklo-riditka/">řídítka</a>.</p>',
    guide='<h2>Co všechno kategorie obsahuje</h2>'
          '<p>Kategorie spojuje dvě odlišné skupiny: nádoby na pití a upevnění pro telefon. Mají společné to, že se připevňují na rám nebo řídítka a že rozhodují o pohodlí delších jízd. Kromě lahví a košíků tu najdete i nerezové termolahve a zvláštní nádoby, které se hodí na výlety s dětmi.</p>'
          + T(['Produkt', 'Role', 'Na co dát pozor'], [
              ['Cyklistická láhev', 'pití s ventilkem nebo sportovním víčkem', 'objem, měkkost stěny, snadné čištění'],
              ['Košík na láhev', 'drží láhev v rámu', 'průměr, držení při nárazech, materiál'],
              ['Držák telefonu', 'upevní mobil na řídítka nebo představec', 'sevření, velikost displeje, odolnost vůči vibracím'],
              ['Termoláhev', 'udrží teplotu nápoje', 'rozměr vzhledem k košíku, hmotnost']]) +
          '<h2>Jak vybrat láhev</h2>'
          '<p>Láhev na kolo má pružnou stěnu, aby se dalo zmáčknout a nápoj vystříknout bez sundání víčka. Nejčastější objem bývá pět set až osm set mililitrů. Menší láhve se vejdou do košíku na menším rámu, větší se hodí na dlouhé trasy, kde nejsou obchody nebo studánky. Víčko s ventilkem se otevírá zuby nebo prstem a nepropouští při převrácení, zároveň se dá snadno rozebrat a vymýt.</p>'
          '<p>Materiál je většinou plast bez bisfenolu, který nepřebírá chuť. Nerezové láhve udrží déle teplotu, ale nejsou stlačitelné a váží víc, proto je používejte jako doplněk, ne jako hlavní bidon. Pokud vozíte iontový nápoj, hodí se široký otvor, který se dá důkladně vyčistit. Různé nápoje najdete v kategoriích <a href="/iontove-napoje/">iontové nápoje</a>, <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>'
          '<h2>Košík: sedí, nebo vypadne</h2>'
          '<p>Košík musí držet láhev i na hrbolech, ale nesmí se zasekávat při vytahování. Hliníkové a kompozitní modely bývají lehké, plastové levnější a flexibilnější. Šrouby se upevňují do závitů v rámu, nejčastěji ve dvojici. Pokud rám závity nemá, existují úchyty s objímkou nebo s páskem. Boční přístup se hodí na malých rámech, kde by se láhev nevešla zepředu. Zkontrolujte rozteč závitů a průměr lahve, ať se obě části k sobě hodí.</p>'
          '<p>Někteří cyklisté používají magnetické systémy, které láhev vytáhnou a vrátí jednou rukou. Tyto uchycení jsou praktické pro silniční jízdu, ale vyžadují kompatibilní láhev.</p>'
          '<h2>Držáky telefonu</h2>'
          '<p>Telefon na řídítkách slouží jako navigace i záznam trasy. Držáky se liší způsobem sevření, uchycením a ochranou. Pružné silikonové držáky se přizpůsobí různým rozměrům, ale při velkých vibracích mohou povolit. Čelisti s pružinou drží pevněji, ale hůře zvládají různé tloušťky pouzdra. Systémy s bajonetem nebo magnetem, třeba od SP Connect nebo Fidlock, vyžadují pouzdro nebo adaptér, ale sundají a nasadí telefon během vteřiny.</p>'
          '<p>Při výběru zkontrolujte, zda se do držáku vejde váš telefon včetně pouzdra, a zda zůstává dostupné tlačítko vypínače a hlasitosti. Silné vibrace, zejména u motocyklů, mohou poškodit stabilizaci fotoaparátu v moderních telefonech. Při běžné jízdě na kole je riziko menší, přesto výrobci telefonů doporučují u silně vibrujících strojů tlumič vibrací a na kole upevnění na rám nebo představec.</p>'
          '<h2>Kam držák umístit</h2>'
          '<ul><li><strong>Na řídítka:</strong> klasika, telefon je na očích. Zkontrolujte, aby nebránil lanům a brzdovým páčkám.</li>'
          '<li><strong>Na představec:</strong> telefon je blíž ose kola a vypadá čistěji, ale může bránit cyklocomputeru.</li>'
          '<li><strong>Na trubku rámu:</strong> hodí se u kol s nízkými řídítky, kde by telefon vadil.</li></ul>'
          '<p>Pokud chcete jen navigaci, zvažte <a href="/cyklo-computery/">cyklocomputer</a>, který má lepší výdrž baterie a čitelný displej na slunci. Telefon pak zůstane v kapse jako záloha. K napájení pomůže <a href="/powerbanky-a-nabijeni/">powerbanka</a>.</p>'
          '<h2>Výběr podle typu jízdy</h2>'
          + T(['Jízda', 'Doporučené řešení', 'Poznámka'], [
              ['Silnice', 'dvě láhve v košících, malý držák telefonu', 'hmotnost a aerodynamika, viz <a href="/silnicni-kola/">silniční kola</a>'],
              ['MTB a terén', 'robustní košík, nižší láhev, pevné sevření', 'nárazy, viz <a href="/horska-kola/">horská kola</a>'],
              ['Gravel a bikepacking', 'košíky na vidlici i rámu, vyšší objem', 'viz <a href="/gravel-kola/">gravel kola</a>'],
              ['Městská jízda', 'nerezová láhev, držák na telefon pro navigaci', 'viz <a href="/mestska-kola/">městská kola</a>'],
              ['Elektrokolo', 'stejné jako u běžných kol, ale vyšší váha', 'viz <a href="/elektrokola/">elektrokola</a>']]) +
          '<h2>Hygiena a péče</h2>'
          '<p>Láhve na kole se rychle zašpiní, protože se na ně dostává prach a potůčky z cesty. Po každé jízdě je vypláchněte, jednou za týden důkladně vyčistěte kartáčkem a nechte uschnout rozebrané. Do myčky patří jen modely, které to výrobce výslovně dovoluje. Gumové těsnění se může časem uvolnit, proto ho zkontrolujte. Zápach se dá odstranit roztokem jedlé sody. Sladké nápoje a proteinové směsi nenechávejte v lahvi přes noc.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Příliš tuhá láhev:</strong> nedá se zmáčknout a pití za jízdy je obtížné.</li>'
          '<li><strong>Nesprávný průměr:</strong> láhev vypadne z košíku nebo se nedá vytáhnout.</li>'
          '<li><strong>Telefon bez zajištění:</strong> při vibracích se držák uvolní a přístroj spadne.</li>'
          '<li><strong>Zakrytý displej bez ochrany:</strong> slunce a déšť omezují čitelnost, pomůže clona nebo pouzdro.</li>'
          '<li><strong>Nezkontrolované šrouby:</strong> košík se časem uvolní a při jízdě klape.</li></ul>'
          '<h2>Příslušenství navíc</h2>'
          '<p>K láhvím se hodí <a href="/cyklo-pumpy-a-naradi/">pumpa a nářadí</a>, <a href="/cyklo-zamky/">zámek</a> a <a href="/cyklo-svetla/">světla</a>, které se montují na stejné části kola. Pokud svůj telefon používáte v dešti, dají se pořídit voděodolná pouzdra. Pro děti vybírejte menší lahve a <a href="/detska-kola/">dětská kola</a> mají často speciální držák.</p>'
          '<h2>Jak vybírat na Sportece</h2>'
          '<p>Nejdříve určete, co potřebujete: bidon, košík, držák, nebo celou sadu. Pak porovnejte objem, upevnění a kompatibilitu s vaším telefonem či rámem. U každého produktu vidíte nabídky více obchodů a rozdíly v ceně a dopravě, takže snadno zjistíte, kde je kus skladem. Větší přehled najdete v nadřazené kategorii <a href="/cyklo-prislusenstvi/">příslušenství pro cyklisty</a> a v <a href="/cyklistika/">cyklistice</a>.</p>',
    faq=[
        ('Jaký objem cyklistické láhve zvolit?', 'Pro krátké jízdy stačí zhruba pět set mililitrů, na delší trasy volte sedm set až osm set. Pokud jedete dlouho bez možnosti doplnit zásoby, vezměte dvě láhve nebo kombinujte s hydrovakem v batohu. Velikost košíku musí odpovídat průměru láhve.'),
        ('Je lepší plastová, nebo nerezová láhev?', 'Plastová je lehčí, stlačitelná a levná, takže se hodí na sport. Nerezová udrží déle teplotu a vydrží nárazy, ale váží víc a nedá se zmáčknout. Na kolo volte primárně plast, nerez si nechte na výlety, kde nezáleží na každém gramu.'),
        ('Jak poznám, že láhev pasuje do košíku?', 'Zkontrolujte průměr láhve a světlost košíku. Standardní bidon má průměr kolem sedmi centimetrů a do většiny košíků zapadne. Pokud kupujete nerezovou nebo širší láhev, ověřte kompatibilitu v popisu produktu nebo u obchodu.'),
        ('Co dělat, když láhev při jízdě vypadává?', 'Zkontrolujte, zda košík nemá uvolněné šrouby a zda není roztažený. Pomůže košík s pevnějšími rameny nebo magnetickým systémem. U terénních jízd se vyplatí košík s bočním přístupem a láhev s drsnějším povrchem.'),
        ('Jaký držák telefonu vybrat?', 'Rozhodněte podle velikosti telefonu a typu jízdy. Silikonové pásky jsou univerzální, čelisti drží pevněji, bajonetové a magnetické systémy se nasazují nejrychleji, ale vyžadují pouzdro. Ověřte, zda nezakrývá tlačítka a zda je kompatibilní s vaším průměrem řídítek.'),
        ('Může vibrace poškodit telefon na kole?', 'Dlouhodobé silné vibrace mohou ovlivnit stabilizaci objektivu fotoaparátu, proto se doporučuje tlumič nebo držák na rám. Pro běžnou jízdu po asfaltu a normální cestě to nebývá problém, u terénních tras se vyplatí volit držák s tlumením.'),
        ('Hodí se držák telefonu i na elektrokolo?', 'Ano, funguje stejně jako na běžném kole. U elektrokol se často využívá napájení telefonu z baterie kola přes USB, pokud ho model nabízí. Pozor na to, aby kabely nebránily řízení a brzdění.'),
        ('Jak láhev vyčistit od zápachu?', 'Vypláchněte ji teplou vodou s jedlou sodou nebo octovým roztokem a nechte rozebranou uschnout. Použijte kartáček na ventil a víčko, kde se zbytky nápoje drží nejdéle. Pokud zápach zůstane, vyměňte víčko, plast může zápach vstřebat.'),
        ('Můžu láhev pro kolo dát do myčky?', 'Záleží na výrobci. Některé modely jsou označené jako vhodné do myčky na nižší teplotu, jiné se deformují. Víčko a ventil je lepší mýt ručně. Řiďte se pokyny uvedenými u produktu a vyhněte se vysokým teplotám.'),
        ('Jak připevnit košík, když rám nemá závity?', 'Pořiďte objímky nebo pásky, které se upevní na trubky rámu bez vrtání. Mohou mírně poškrábat lak, proto použijte pryžovou podložku. Alternativou je brašna na rám nebo láhev v zadní kapse dresu, viz cyklistické dresy.')
    ])

# ------------------------------------------------------------------ florbalove-hole
NEW['florbalove-hole'] = dict(long=True,
    title='Florbalové hole: délka, tuhost, čepel, junior i senior',
    desc='Florbalové hole pro děti, juniory i dospělé. Jak vybrat délku, tuhost, tvar čepele a materiál, a porovnat nabídky českých obchodů.',
    intro='<p>Florbalová hůl je nejdůležitější část výbavy hráče, protože rozhoduje o ovládání míčku, přesnosti přihrávky i síle střely. Skládá se z násady a čepele, přičemž každá část má jiné parametry: délku, tuhost, zahnutí a úchop. Správná volba šetří záda, zlepšuje techniku a u dětí brání špatným návykům. Sporteka porovnává nabídky českých obchodů u holí pro začátečníky, dorostence i pokročilé hráče, včetně levých a pravých provedení a samostatných čepelí.</p>'
          '<p>V kategorii jsou zastoupeny značky ' + B(('fat-pipe', 'Fat Pipe'), ('salming', 'Salming'), ('kubisport', 'Kubisport'), ('unihoc', 'Unihoc'), ('tempish', 'Tempish'), ('oxdog', 'Oxdog'), ('arex', 'Arex'), ('freez', 'Freez'), ('zone', 'Zone')) +
          '. Do kompletní výbavy patří <a href="/salova-obuv/">sálová obuv</a>, <a href="/sportovni-bryle/">sportovní brýle</a> a <a href="/sportovni-tasky/">sportovní taška</a>; celý sport najdete v kategorii <a href="/florbal/">florbal</a>.</p>',
    guide='<h2>Z čeho se florbalová hůl skládá</h2>'
          '<p>Hůl tvoří dlouhá trubice, kterou nazýváme násada, a výměnná čepel. Násada bývá z kompozitu na bázi uhlíkových nebo skleněných vláken, u nejlevnějších kusů z lehčích plastů. Čepel se zasouvá do konce násady a zajišťuje se zahřátím nebo lepidlem. Díky tomu lze měnit tvar čepele a opravit opotřebovanou hůl bez nákupu nové. Na konec násady se navléká omotávka, tedy lepicí páska, která zlepšuje úchop.</p>'
          '<h2>Délka hole</h2>'
          '<p>Správná délka patří k nejčastějším nastavením, která začátečníci podcení. Hůl se při postoji opře o tělo a její horní konec by měl sahat zhruba k pupku až k pasu. Delší hůl umožňuje dosáhnout dál a lépe střílet, ale hůře se s ní driblinkuje. Kratší hůl má lepší ovládání míčku a rychlejší pohyb, ale nutí hráče se hrbit. Délku lze zkrátit, protože násada se řeže pilkou, proto lze zakoupit delší hůl a upravit ji na míru.</p>'
          + T(['Hráč', 'Přibližná délka hole', 'Poznámka'], [
              ['Malé děti', 'kolem osmdesáti centimetrů', 'lehká násada, nízká tuhost, viz modely s označením Mini nebo Kids'],
              ['Junioři', 'zhruba 87 až 95 cm', 'rostoucí hráč potřebuje hůl o něco delší, ale lehkou'],
              ['Dospělí', 'zhruba 95 až 105 cm', 'podle výšky a stylu hry'],
              ['Vysocí hráči', 'nad 105 cm', 'ověřte, že hůl splňuje pravidla soutěže']]) +
          '<p>Čísla jsou orientační a závisí na výšce a stylu hry. Obránci často volí delší hole, útočníci kratší, protože potřebují lepší manipulaci s míčkem.</p>'
          '<h2>Tuhost násady</h2>'
          '<p>Tuhost se označuje číslem, které odpovídá ohybu násady při standardním zatížení. Nižší číslo, například 26 nebo 27, znamená tužší hůl, vyšší číslo, třeba 32 nebo 34, měkčí. Tuhá hůl přenáší energii přímo do míčku a vyžaduje silnější hráče s dobrou technikou. Měkčí hůl se při střele prohne a vrátí energii, hodí se začátečníkům a dětem, protože odpouští chyby. Pro dorostence a lehčí hráče proto vybírejte měkčí hole a postupně přecházejte k tužším.</p>'
          '<p>Při výběru dbejte také na váhu, protože lehká hůl se rychleji otáčí v rukou, ale přenáší méně energie z těla do střely. Pokročilí hráči často volí kompozit s výrazně nižší hmotností a pevnějším jádrem, začátečníci spíše levnější konstrukci.</p>'
          '<h2>Čepel a zahnutí</h2>'
          '<p>Čepel se liší tvarem, zahnutím a tuhostí. Mírně zahnutá čepel dobře drží míček při vedení a hodí se pro obránce a univerzální hráče. Výraznější zahnutí usnadňuje zvedání míčku a střelbu bekhendem, ale hůře se s ním přihrává naplocho. Tvrdší čepel přesněji střílí, měkčí lépe přijímá míček. Pokud hráč trénuje trik s míčkem na hůl, ocení měkčí čepel s nižším zahnutím, která je odpouští.</p>'
          '<p>Důležité je také to, zda je čepel pravá, nebo levá. Označení vychází z toho, na které straně je zahnutí. Ověřte vždy v popisu produktu a vyzkoušejte, která ruka vám dole na holi sedí lépe, protože dominantní ruka nemusí odpovídat straně, kterou hrajete. Kdo je na pochybách, vyzkouší hůl s kamarádem na tréninku. V nabídce najdete i hole pro leváky.</p>'
          '<h2>Schválení IFF</h2>'
          '<p>Mezinárodní florbalová federace schvaluje hole a čepele pro oficiální zápasy. Takové výrobky mají na násadě značku, a pokud hrajete soutěže, jsou povinné. Pro rekreační hru, školní tělocvik nebo trénink doma není schválení nutné, ale hráč si zvykne na stejné parametry jako v soutěžích. V popisu produktu proto sledujte, zda je schválení uvedeno.</p>'
          '<h2>Jak vybrat podle věku a úrovně</h2>'
          '<ul><li><strong>Malé děti a začátečníci:</strong> lehká, krátká a měkká hůl s jednoduchou čepelí. Důležitá je radost z hry, ne technické parametry.</li>'
          '<li><strong>Školáci a mladší žáci:</strong> střední tuhost, rozumná cena a možnost zkrátit hůl podle růstu.</li>'
          '<li><strong>Dorost a dospělí amatéři:</strong> střední až vyšší tuhost, kompozit a výměnná čepel.</li>'
          '<li><strong>Ligoví a pokročilí hráči:</strong> lehká uhlíková násada, přesné zahnutí čepele a schválení IFF.</li></ul>'
          '<h2>Co dalšího patří k výbavě</h2>'
          '<p>Hůl sama nestačí. Hráč potřebuje <a href="/salova-obuv/">sálovou obuv</a> s protiskluzovou podrážkou, <a href="/sportovni-ponozky/">sportovní ponožky</a>, <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/dresy/">dres</a>. Brankáři nosí vlastní ochranu, rukavice najdete v kategorii <a href="/brankarske-rukavice/">brankářské rukavice</a>. Ochranné <a href="/sportovni-bryle/">brýle</a> jsou volitelné a doporučují se hlavně dětem a hráčům po úrazu oka. K přenášení holí a míčků se hodí <a href="/sportovni-tasky/">taška</a>. Míčky patří do <a href="/micove-sporty/">míčových sportů</a>.</p>'
          '<h2>Omotávka a úchop</h2>'
          '<p>Omotávka je tenká páska, kterou se obtáčí horní konec hole. Zvyšuje přilnavost a zabraňuje sklouzávání rukou po potu. Měnit by se měla, jakmile je ohmataná nebo se odlepuje. Silnější pásky tlumí vibrace, tenčí dávají lepší cit. Mnoho hráčů volí barvu podle týmu. Při výměně pásku začněte u konce násady a obtáčejte s přesahem dva až tři milimetry, aby se nevytvořily mezery.</p>'
          '<h2>Péče a životnost hole</h2>'
          '<ul><li>Hůl neponechávejte v autě na slunci, kompozit i lepidlo čepele trpí vysokou teplotou.</li>'
          '<li>Po tréninku ji otřete a dejte do obalu nebo tašky, aby se nepoškrábala.</li>'
          '<li>Čepel kontrolujte, jestli se nezačíná odlupovat nebo praskat, a včas ji vyměňte.</li>'
          '<li>Neopírejte se o hůl jako o hůl na chůzi a nesedejte na ni, násada se může zlomit.</li>'
          '<li>Trhlinu v násadě neopravujte lepidlem, hůl může při střele prasknout a zranit hráče.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Příliš tuhá hůl pro dítě:</strong> hůl se neprohne, střela je slabší a dítě ztrácí chuť trénovat.</li>'
          '<li><strong>Příliš dlouhá hůl:</strong> děti si hůl nechávají delší na růst, ale zhoršují si techniku. Raději hůl upravte.</li>'
          '<li><strong>Špatná strana:</strong> hůl s opačným zahnutím nedrží míček a hráč se musí učit nový pohyb.</li>'
          '<li><strong>Zapomenuté schválení:</strong> v soutěžích se může stát, že hůl nesplňuje pravidla.</li>'
          '<li><strong>Nákup podle barvy:</strong> parametry jsou důležitější než design.</li></ul>'
          '<h2>Podobné sporty a hole</h2>'
          '<p>Florbalová hůl je odlišná od <a href="/hokejky/">hokejky</a> a od hole na <a href="/pozemni-hokej/">pozemní hokej</a>. Nepoužívejte je zaměnitelně, protože tvar, váha i pravidla jsou jiné. Pokud váháte, jaký sport dítě bude hrát, začněte sálovou hrou s lehčí holí a teprve později řešte specializaci. Dobrou průpravou jsou i <a href="/funkcni-trenink/">funkční trénink</a> a doplňky pro <a href="/hokej/">hokej</a>.</p>'
          '<h2>Jak vybírat na Sportece</h2>'
          '<p>Nejprve určete délku a tuhost, pak zvolte značku a tvar čepele. U každé hole vidíte nabídky více obchodů a rozdíly v dostupnosti i dopravě. Při porovnání se zaměřte na údaje o délce, tuhosti a straně, protože se u jedné značky mohou lišit varianty stejného modelu. Pokud nakupujete pro dítě, zvolte lehčí hůl a pamatujte, že se délka dá snadno zkrátit.</p>',
    faq=[
        ('Jak dlouhou florbalovou hůl vybrat?', 'Postavte hůl před sebe, horní konec by měl sahat zhruba k pupku až k pasu. Pro děti volte kratší hůl, pro dospělé přibližně do výšky pasu. Delší hůl lze zkrátit pilkou, takže při pochybách kupujte spíše delší model.'),
        ('Co znamená číslo tuhosti, například 29?', 'Udává ohyb násady při standardním zatížení. Nižší číslo znamená tužší hůl, vyšší měkčí. Začátečníci a děti obvykle volí hole s vyšším číslem, protože odpouštějí chyby. Silní hráči s dobrou technikou sahají po nižších číslech.'),
        ('Jakou tuhost zvolit pro dítě?', 'Raději měkčí. Dítě nemá sílu hůl prohnout a tuhá násada pak slabě střílí. Zkuste hole s tuhostí kolem třiceti a víc a dívejte se na hmotnost, protože lehká hůl se snáze ovládá.'),
        ('Jak poznám, jestli je hůl levá, nebo pravá?', 'Rozhoduje, na kterou stranu je zahnutá čepel. V popisu produktu bývá uvedeno označení, někdy jen písmeno L nebo R. Vyzkoušejte, která ruka vám dole na holi vyhovuje, protože volba nemusí odpovídat dominantní ruce.'),
        ('Co je schválení IFF?', 'Je to označení, že hůl nebo čepel splňuje pravidla mezinárodní florbalové federace pro oficiální zápasy. Pro rekreační hru není nutné, v soutěžích ano. Značku najdete na násadě nebo v popisu produktu.'),
        ('Dá se měnit čepel na holi?', 'Ano, většina kompozitních holí má výměnnou čepel, která se zasouvá do násady a zahřátím nebo lepidlem fixuje. Čepel se mění při opotřebení nebo při změně stylu hry. Při výměně dbejte na správnou orientaci a pokyny výrobce.'),
        ('Jak často vyměnit omotávku?', 'Jakmile se ohmatá, odlepuje nebo ztrácí přilnavost. Aktivní hráči ji mění několikrát za sezónu. Omotávka je levná a rychle se vymění, dává hráči lepší úchop a chrání dlaň před puchýři.'),
        ('Mohu hůl zkrátit sám?', 'Ano, násada se zkracuje pilkou na kov nebo řezačkou na trubky. Odměřte délku podle hráče, odřízněte rovně a hranu zabruste. Nezkracujte víc, než je nutné, protože se tím mění tuhost a hůl bude tužší.'),
        ('Jak dlouho florbalová hůl vydrží?', 'Při pravidelné hře několik měsíců až sezónu, kompozit se unavuje a po čase ztrácí odezvu. Životnost zkracuje hrubé zacházení, sluneční žár a údery o podlahu. Trhlinu nebo ohyb nelze opravit, hůl pak vyměňte.'),
        ('Je florbalová hůl stejná jako hokejka?', 'Ne. Je lehčí, dutá a s plastovou čepelí, určená pro hru s plastovým míčkem v hale. Hokejka na led je pevnější a těžší. Pro děti ve škole nebo kroužku je vhodná lehká florbalová hůl.')
    ])


# ------------------------------------------------------------------ doplnění sekcí (guide)
NEW['detska-kola-20-palcu']['guide'] += (
    '<h2>První vyjížďky a bezpečné trasy</h2>'
    '<p>Dítě na dvacítce už zvládá delší trasy, ale zkušenost s provozem mu ještě chybí. Začněte na cyklostezkách, v parku nebo na nezpevněných cestách mimo auta a postupně přidávejte úseky s přechody a zatáčkami. Procvičte společně rozjezd do kopce, zastavení na značku, pohled přes rameno a signalizaci rukou. Dospělý jede vzadu nebo těsně za dítětem, aby viděl jeho reakce, a vybírá trasu s dohledem na překážky. Krátká zastávka po půl hodině dětem pomůže, protože se unaví dřív než dospělí.</p>'
    '<h2>Oblečení a doplňky do různého počasí</h2>'
    '<p>Dítě na kole chladne na rukou a uších dřív, než by čekal rodič. Na jaro a podzim se hodí tenké <a href="/cyklisticke-rukavice/">rukavice</a> a <a href="/cepice-a-celenky/">čelenka pod helmu</a>, v létě lehké tričko z funkčního materiálu a kraťasy bez švů na vnitřní straně stehen. Při dešti pomůže <a href="/nepromokave-bundy/">nepromokavá bunda</a>, která dítě neomezuje v pohybu. Reflexní prvky na batohu a na oblečení zvyšují viditelnost za soumraku, kdy se děti vracejí z kroužků.</p>')
NEW['detske-spacaky']['guide'] += (
    '<h2>Jak spacák zvolit podle sezóny</h2>'
    '<p>Spacák na léto má lehkou výplň a hodí se na noci, kdy teplota klesá jen mírně. Na jaro a podzim potřebujete hustší izolaci a kapuci. V zimě se spacák na dětské akce téměř nevyužívá, protože děti spí v prohřátých objektech. Pokud rodina chodí stanovat celoročně, volí se vícevrstvý systém: spacák, vložka a teplé oblečení. Dětem se vyplatí zkusit systém doma na zahradě, aby se ověřilo, že jim nebude zima a že zvládnou zip.</p>'
    '<h2>Bezpečnost při spaní venku</h2>'
    '<p>Spací pytel musí mít zip, který nejde zavřít přes obličej, a otvor pro hlavu, který zůstává odkrytý. Šňůrky u kapuce zkraťte, aby se neomotaly kolem krku. Dítě by mělo znát cestu k východu ze stanu a mít po ruce <a href="/celovky-a-svitilny/">svítilnu</a>. Věci k vaření a ohni nepatří do stanu. Při dešti zkontrolujte, zda se voda nedostává pod podlážku, protože mokrý spacák ztrácí izolační schopnost a dítě rychle vychladne. Základní vybavení pro drobná zranění najdete v oddílu <a href="/prvni-pomoc/">první pomoc</a>.</p>'
    '<h2>Balení a přenášení</h2>'
    '<p>Spacák se do obalu nacpe ze spodní strany, bez skládání, aby se výplň nezlomila na stejném místě. Obal s kompresními popruhy dítě odnese samo, lehčí modely se vejdou do malého batohu. Pro dálkovější túry si prohlédněte <a href="/turisticke-batohy/">turistické batohy</a> s připevněním na spodku. Pokud cestujete vlakem, praktické jsou kompaktní kusy s malým objemem po složení. V balení nezapomeňte na čistou vložku nebo prostěradlo, které se dá vyprat po táboře a které chrání vnitřek spacáku před špínou.</p>'
    '<h2>Dětské spacáky podle značek</h2>'
    '<p>Značky v kategorii se liší zaměřením. Husky a Highlander nabízejí mnoho dekových a mumiových modelů s dětským vzorem, Skandika a Easy Camp se zaměřují na rodinné kempování, Deuter a Pinguin vyrábějí lehčí rostoucí kusy pro turistiku s dětmi. NILS Camp a Crossroad mají cenově dostupné řady a Cocoon se specializuje na vložky a lehké přikrývky. Porovnání značek je užitečné hlavně u teplotních údajů a hmotnosti, protože se mezi řadami liší více než samotná barva nebo potisk.</p>')
NEW['cyklo-lahve-a-drzaky']['guide'] += (
    '<h2>Hydratace na delších trasách</h2>'
    '<p>Na kole se pocení často nepozná, protože vítr pot odpařuje, takže se pít má pravidelně po menších doušcích, ne až při žízni. Při delší jízdě se vyplatí jedna láhev čisté vody a jedna s iontovým nápojem. Druhou láhev označte lihovou fixou nebo barevnou páskou, aby se při jízdě nezaměnily. V horku a v kopcích dochází k vyššímu úbytku tekutin, proto plánujte zastávky u pramenů a obchodů. Neexistuje jednotné pravidlo na objem, ten závisí na teplotě, váze a tempu, a při zdravotních omezeních je rozumné poradit se s lékařem.</p>'
    '<h2>Kompatibilita s kolem a rámem</h2>'
    '<p>Než košík koupíte, zkontrolujte, kolik má rám závitů a kde. Malé rámy často mají závity jen pro jednu láhev, dětská kola žádné. Odpružená kola mají rám s tlumičem, který bere část prostoru, a tak se vejde jen nižší láhev. Elektrokola s baterií v rámu mají vlastní rozložení. Vždy porovnejte vzdálenost závitů s rozměry košíku a při pochybnostech si vzdálenost změřte svinovacím metrem.</p>'
    '<h2>Držák telefonu a bezpečnost jízdy</h2>'
    '<p>Telefon na řídítkách může rozptylovat, proto se na něj dívejte jen krátce a před jízdou si trasu naplánujte. Vypněte upozornění, která zbytečně svítí, a nastavte displej tak, aby byl čitelný na slunci. Při jízdě v dešti zvolte voděodolné pouzdro nebo držák s krytem. Hlasitý zvuk z reproduktoru by neměl přehlušit okolní provoz. Telefon spojený se sluchátky v obou uších je nebezpečný, zvuk ze sluchátka jen v jednom uchu nebo z řídítek ponechává prostor pro slyšení okolí.</p>'
    '<h2>Doplňky a drobnosti</h2>'
    '<p>Mezi doplňky patří silikonové pásky na zajištění lahve, přídavné držáky pod sedlem pro dvě lahve, brašny na rám s okénkem na mobil a tlumiče vibrací. Pro kempování a výlety s rodinou se hodí také nerezové láhve a termosky, které najdete v kategorii <a href="/lahve-a-termosky/">láhve a termosky</a>. K drobnému příslušenství pro každou výpravu patří <a href="/cyklo-zvonky-a-zrcatka/">zvonek a zrcátko</a> a <a href="/cyklo-udrzba/">údržba kola</a>.</p>')
NEW['florbalove-hole']['guide'] += (
    '<h2>Trénink techniky podle typu hole</h2>'
    '<p>Hůl se mění s tím, jak hráč zraje. Začátečník potřebuje lehkou a měkkou násadu, na které se naučí vedení míčku a základní střelu. Po prvních sezónách přichází vhodný čas přejít na hůl s tužší násadou a přesnější čepelí, protože střela získá sílu. Dobře to zkusit při tréninku se spoluhráči, kteří mají jiné modely. Trénink s hůlí vyžaduje i přípravu těla: protažení zápěstí, předloktí a ramen a posilování středu těla, které stabilizuje střelu. Pomůže i vybavení pro <a href="/fitness-pomucky/">fitness</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
    '<h2>Hole podle značek v nabídce</h2>'
    '<p>Fat Pipe a Salming patří k nejrozšířenějším značkám a mají široký sortiment od dětských po soutěžní modely. Unihoc a Tempish nabízejí řady pro školy a kluby, Kubisport a Sport 2020 se zaměřují na cenově dostupné hole pro rekreační hráče. Oxdog, Arex, Freez a další značky doplňují nabídku o specializované tvary a levé varianty. Při porovnání se nezaměřujte na jméno, ale na délku, tuhost, hmotnost a schválení.</p>'
    '<h2>Bezpečnost ve hře</h2>'
    '<p>Pravidla florbalu zakazují zvedat hůl nad úroveň kolen při hře a při střele, aby nedošlo ke zranění ostatních. Děti musí znát toto pravidlo od začátku. Hůl nepoužívejte mimo hru jako zbraň ani hračku. V hale je důležitá vhodná obuv, protože uklouznutí na hladké podlaze je častější než zranění holí. Pokud se po pádu zdá násada poškozená, vyměňte ji, než se hráč znovu postaví na hřiště. K ochraně kloubů pomáhají <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>')

NEW['detske-spacaky']['guide'] += (
    '<h2>Kontrola před sezónou</h2>'
    '<p>Na začátku sezóny spacák rozbalte, prohlédněte švy a zip a zkuste, zda dítě v pytli pohodlně vleže otočí. Zjistíte tak, jestli vyrostlo, a včas objednáte větší kus. Zkontrolujte i obal, popruhy a šňůrku kapuce, které se rády poškodí při skladování.</p>')
NEW['cyklo-lahve-a-drzaky']['guide'] += (
    '<h2>Před první jízdou</h2>'
    '<p>Nový košík i držák vyzkoušejte nejdřív na krátké trase poblíž domova. Trhněte lahví, zatřeste telefonem, zkontrolujte dotažení šroubů a ověřte, že nic nebrání řízení ani brzdění. Teprve poté vyražte na delší výlet, kde případná závada znamená potíž.</p>')
