"""sporteka.cz — winter subcategories: practical sections appended by texty-export.py to texty_vlna7a.py / texty_vlna7b.py."""

EXTRA = {}


def add(slug, intro, guide):
    EXTRA[slug] = dict(intro='<p>' + intro + '</p>', guide=guide)


add('snowboardove-boty', 'Velikost a tuhost si zkuste ideálně před koupí, protože snowboardové boty se po několika dnech rozšlapou.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je koupě bot podle vzhledu a ne podle pohodlí. Další chybou je ignorovat ponožky: zkoušejte boty v těch, které budete nosit. Příliš silná ponožka tlačí a boty uvnitř studí.</p>')
add('snowboardova-vazani', 'Zkontrolujte si před koupí děrování desky a velikost boty, ať vázání při první jízdě sedí.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je koupit vázání bez kontroly desky. Další chybou je příliš utažený pásek přes nárt, který tlačí a vede k brnění. Pásky utahujte pevně, ale tak, aby noha zůstala prokrvená.</p>'
    '<h3>Kdy vázání vyměnit</h3><p>Praskliny v plastu, ohnuté sponky nebo zubatý ráčnový mechanismus jsou důvod k výměně. Před sezónou zkontrolujte šrouby a dotáhněte je, protože se postupně uvolňují.</p>')
add('snowboardove-chranice', 'Vybírejte chránič, který ucítíte až při pádu, a ne při jízdě, protože příliš velký omezuje pohyb.',
    '<h3>Péče o chrániče</h3><p>Po použití je vyvětrejte a nenechávejte mokré v tašce. Pěnové vložky perte podle štítku a ne v pračce při vysokých teplotách, aby neztratily tvar. Zkontrolujte popruhy a suché zipy, protože se po sezóně opotřebují.</p>'
    '<h3>Jak začít</h3><p>Při první sezóně obvykle stačí chrániče zápěstí a ochranné kalhotky. Další vrstvy přidáte, jakmile začnete jezdit v parku nebo v neupravovaném terénu.</p>')
add('bezecke-boty', 'Při zkoušce nezapomeňte na tenkou běžeckou ponožku a rezervu na přehřátí chodidla, protože při jízdě se nohy zahřívají.',
    '<h3>Jak začít s běžkami</h3><p>Pro první sezónu stačí kombinované boty s lyžemi na klasiku. Později můžete přejít na bruslení nebo vyšší výkonnostní boty. Na vyjížďky v mírném terénu nepotřebujete nejdražší model, důležitější je správná velikost a vázání.</p>'
    '<h3>Časté chyby</h3><p>Mnoho začátečníků kupuje botu o číslo větší „na teplo“. Ve volné botě se ale noha posouvá a vznikají puchýře. Vždy si zjistěte i systém vázání, ať se nic nemusí vracet.</p>')
add('bezecke-vazani', 'Při koupi zkontrolujte, jestli ladí bota i lyže, a pokud si nejste jistí, požádejte o radu prodejce.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je koupě vázání jiného systému než mají boty. Dalším problémem bývá špatně zvolená montáž, kdy vázání leží příliš vpředu nebo vzadu a lyže se hůř ovládá. Přesné umístění udává značka na lyži nebo návod výrobce.</p>'
    '<h3>Péče o vázání</h3><p>Po jízdě očistěte vázání od sněhu a nechte je vyschnout. Zamrzlý sníh v mechanismu ztěžuje zacvaknutí. Občas zkontrolujte šrouby a pružinu.</p>')
add('skialpove-lyze', 'Před koupí si ujasněte, jak často chodíte na túry a zda budete lyže využívat i na sjezdovce.',
    '<h3>Časté chyby</h3><p>Začátečníci často kupují lyže určené pro závody nebo naopak příliš široké freeridové, aby zvládly všechno. Nejlepší je začít univerzálními túrovými lyžemi. Poslední chybou je zanedbat servis před sezónou.</p>')
add('skialpove-boty', 'Při zkoušce si vezměte vlastní ponožky a nechte si čas, bota se nesmí otírat ani tlačit.',
    '<h3>Péče a údržba</h3><p>Po túře boty vyndejte z přepravy, vyjměte vložky a nechte je zcela vyschnout při pokojové teplotě. Mokré boty zamrzají a tvrdnou. Zkontrolujte přezky a podrážku, protože se na túrách opotřebují rychleji než u sjezdových bot.</p>'
    '<h3>Časté chyby</h3><p>Nejčastěji se kupuje příliš velká bota. V ní se pata zvedá a noha se při sjezdu pohybuje. Drobně menší bota se po rozchození uvolní.</p>')
add('skialpove-vazani', 'Zkontrolujte kompatibilitu bot, a pokud nemáte jistotu, požádejte o radu prodejce.',
    '<h3>Seřízení a kontrola</h3><p>Před sezónou nechte vázání zkontrolovat a seřídit. U pinových vázání zkontrolujte pružiny a stav kolíků. Při jakémkoli poškození je třeba vázání vyměnit.</p>'
    '<h3>Časté chyby</h3><p>Nejčastěji se zapomíná na to, že vázání se musí hodit k botám a lyžím. Dalším problémem je nastavení uvolnění podle odhadu, bez ověření v servisu.</p>')
add('skialpove-pasy', 'Pásy vyberte podle šířky lyží a mějte je vždy vyzkoušené na lyžích před túrou.',
    '<h3>Jak pásy skladovat</h3><p>Po vysušení pásy slepte k ochranné fólii nebo k sobě a uložte do pouzdra. Chraňte je před horkem a před prachem. Při dlouhém skladování uložte v suchu, ne v autě v létě.</p>'
    '<h3>Časté chyby</h3><p>Nejčastěji se pásy koupí na lyže, které později vyměníte. Pásy z role se přizpůsobí, hotové jsou rychlé na nasazení. Ořezávejte pásy vždy tak, aby zůstaly volné hrany.</p>')
add('lyzarske-vosky', 'Před sezónou si vyzkoušejte jeden vosk, ať víte, jak lyže na sněhu reagují.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je nanášet vosk na špinavou skluznici nebo příliš silnou vrstvu. Další chybou je zapomenout odstranit přebytek škrabkou. Před voskováním skluznici očistěte, vosk nechte vychladnout a pak teprve škrabte.</p>'
    '<h3>Jak začít</h3><p>Pro první voskování stačí univerzální vosk, žehlička a škrabka. Později můžete přidat vosky podle teploty a sprej na doplnění během dne.</p>')
add('lyzarske-vaky-a-tasky', 'Na cestách ocení kvalitní vak zvlášť ti, kdo létají nebo jezdí vlakem s dětmi a mnoha zavazadly.',
    '<h3>Co dalšího se hodí</h3><p>Pro ochranu lyží před poškrábáním se hodí vnitřní přepážka nebo polstrování. Zip by měl mít pevný jezdec a popruhy musí unést váhu lyží včetně hůlek. Pro častou cestu stojí za zvážení kolečka.</p>'
    '<h3>Časté chyby</h3><p>Nejčastěji se kupuje vak příliš krátký, takže se lyže nevejdou nebo se zip nezavře. Změřte lyže předem. Dalším omylem je dlouhodobé skladování mokrých lyží ve vaku.</p>')
add('lyze-komplety', 'Komplet je výhodný hlavně pro rekreační jezdce, kteří nechtějí studovat kompatibilitu vázání.',
    '<h3>Časté chyby</h3><p>Nejčastěji se vybírají lyže, které jsou příliš dlouhé nebo příliš tuhé, aby „vydržely“. Pro rekreační jízdu je lepší lyže, které se dobře ovládají. Druhou chybou je koupit komplet bez ověření, že vázání vyhovuje vašim botám.</p>'
    '<h3>Kdy kupovat</h3><p>Výběr velikostí bývá nejširší na podzim, ceny se v průběhu sezóny mění. Starší sezónní kolekce bývají v průběhu sezóny často zlevněné.</p>')
add('detske-lyze', 'Při výběru zapojte i dítě, ať si lyže vyzkouší v obchodě a ať mu sedí boty.',
    '<h3>Časté chyby</h3><p>Rodiče často kupují příliš dlouhé lyže, aby vydržely víc sezón. Dítě pak nezvládá zatáčet a ztrácí zájem. Dalším omylem je zapomenout na helmu a brýle, které jsou stejně důležité jako lyže.</p>'
    '<h3>Jak začít</h3><p>Nejmenší děti začínají na kratších lyžích s jednoduchým vázáním a pomocí pásky nebo lana pro vedení. S postupem věku přecházejí na vyšší lyže s lepším ovládáním.</p>')
add('lyzarske-vazani', 'Před koupí si ověřte šířku lyží a normu boty, ať se vázání při montáži nemusí vracet.',
    '<h3>Časté chyby</h3><p>Největší chybou je nechat seřídit vázání na odhad nebo podle kamaráda. Další chybou je používat vázání po několik sezón bez kontroly. Kontrola před sezónou je levná a zabrání poškození zdraví.</p>'
    '<h3>Péče</h3><p>Po jízdě vázání očistěte od sněhu a soli, osušte a při dlouhém skladování nenechávejte tlak v pružinách nastavený na maximum.</p>')
add('lyzarske-kombinezy', 'Při zkoušce nechte dítě se pohybovat, ať ověříte, že ho kombinéza nikde neškrtí.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je koupit příliš velkou kombinézu, ve které se dítě špatně pohybuje a hromadí se sníh v ohybech. Další chybou je kupovat podle věku na štítku a ne podle výšky. Zkontrolujte také, jestli je zip chráněný proti sněhu.</p>'
    '<h3>Péče</h3><p>Perte podle štítku, bez aviváže, která zhoršuje voděodolnost. Po praní obnovte impregnaci sprejem.</p>')
add('lyzarske-termopradlo', 'Při zkoušce zdvihněte ruce a předkloňte se, ať ověříte, že se tričko nezvedá nad kalhoty.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je oblékat bavlněné tričko pod lyžařskou bundu nebo se vrstvit příliš silně, takže se pot hromadí. Další chybou je kupovat termoprádlo velké, protože volné prádlo nepřenáší vlhkost.</p>'
    '<h3>Jak začít</h3><p>Pro první sezónu stačí jeden set syntetického termoprádla a pár ponožek. Merino přidejte, jakmile víte, že vám lyžování vyhovuje.</p>')
add('lyzarske-cepice-a-nakrcniky', 'Při zkoušce nasaďte i helmu, abyste ověřili, že čepice nebo čelenka nepřekáží.',
    '<h3>Časté chyby</h3><p>Nejčastěji lidé obléknou tlustou čepici pod helmu, takže helma nesedí a neochrání. Další chybou je bavlněný nákrčník, který se promáčí a studí. Sáhněte po tenkém merinu nebo syntetice.</p>'
    '<h3>Péče</h3><p>Perte podle štítku na šetrný program. Merino a fleece neperte s avivážemi, protože ztrácejí schopnost odvádět pot.</p>')
add('krasobruslarske-brusle', 'Při zkoušce vyzkoušejte předklon a dřep a ověřte, že pata zůstává v botě pevně.',
    '<h3>Časté chyby</h3><p>Nejčastější chybou je koupit brusle o číslo větší, aby vydržely déle. Pata se pak pohybuje a nůž se nedá ovládat. Další chybou je nechat nůž vlhký po bruslení, takže rezaví.</p>'
    '<h3>Jak začít</h3><p>Pro první sezónu stačí rekreační model. Pokud dítě začne trénovat pravidelně, trenér poradí s výběrem tužší boty a nože.</p>')
add('rekreacni-brusle', 'Zkoušejte brusle odpoledne, kdy je noha mírně oteklá, abyste se vyhnuli příliš těsné velikosti.',
    '<h3>Časté chyby</h3><p>Nejčastěji se kupují brusle příliš měkké nebo příliš volné, v nichž kotník nemá oporu. Další chybou je vynechat obal na nůž. Brusle by měly být v taštičce, ne po sobě tlučené v batohu.</p>'
    '<h3>Jak začít</h3><p>Při prvním vstupu na led se držte mantinelu a učte se pomalu. Přilba a chrániče kolen pomáhají hlavně dětem.</p>')
add('sane-a-boby', 'Při koupi sáně vyzkoušejte, zda unesou dítě i dospělého, který ho bude tahat nebo vozit.',
    '<h3>Časté chyby</h3><p>Nejčastěji se kupují sáně příliš malé, na kterých dítě rychle vyroste, nebo příliš lehké pro rychlý svah. Další chybou je zapomenout na brzdu u bobu. Zkontrolujte také šňůru a madla, protože se nejdřív trhají.</p>'
    '<h3>Jak začít</h3><p>Pro první zimu stačí jednoduché plastové nebo dřevěné sáně a šňůra. Později můžete přejít na řiditelný bob.</p>')

_MORE = {
    'bezecke-boty': '<h3>Kdy kupovat</h3><p>Nabídka velikostí je nejširší na podzim, v sezóně se rychle vyprodají oblíbené modely. Pokud boty kupujete pro dítě, prověřte možnost půjčení nebo bazaru, protože děti z nich rychle vyrostou.</p>',
    'bezecke-vazani': '<h3>Kdy kupovat</h3><p>Vázání se kupuje obvykle spolu s lyžemi nebo botami, pokud se mění systém. Při výměně opotřebovaného vázání zkontrolujte rozteč šroubů, aby nové vázání sedělo do stejných otvorů.</p>',
    'skialpove-lyze': '<h3>Kdy kupovat</h3><p>Skialpový trh je užší než sjezdový, proto se vyplatí sledovat nabídku během podzimu. Pokud si nejste jistí, zkuste si lyže nejdřív půjčit na jednu túru a teprve pak se rozhodněte.</p>',
    'skialpove-boty': '<h3>Kdy kupovat</h3><p>Při koupi počítejte s dobou, kdy se boty rozchodí. Ideální je zkusit je doma několik hodin před první túrou a zjistit, jestli netlačí.</p>',
    'skialpove-vazani': '<h3>Kdy kupovat</h3><p>Vázání se kupuje spolu s lyžemi nebo při výměně. Pokud se rozhodujete mezi pinovým a rámovým, zvažte, kolik času strávíte stoupáním a kolik sjezdem. Převaha stoupání mluví pro lehčí pinové vázání.</p><p>Nezapomeňte na brzdy nebo pojistné řemínky, které brání ztrátě lyže.</p>',
    'skialpove-pasy': '<h3>Kdy kupovat</h3><p>Pásy se kupují spolu s lyžemi nebo při opotřebení. Při výběru zvažte délku túr a drsnost terénu. Syntetika zvládne častější a náročnější použití, mohair ocení ti, kdo cení klouzavost.</p>',
    'lyze-komplety': '<h3>Pro koho je komplet</h3><p>Komplet vyhovuje začátečníkům, rodinám s dětmi a lidem, kteří jezdí několik dní v roce. Pokud jezdíte často a máte oblíbenou značku vázání, může se vyplatit koupit lyže a vázání zvlášť.</p>',
    'lyzarske-vazani': '<h3>Kdy kupovat</h3><p>Vázání se obvykle kupuje společně s lyžemi nebo při výměně starého. Pokud kupujete používané, zkontrolujte stáří a stav plastů, protože vázání má omezenou životnost. Starší kusy někteří servisy odmítají nastavit.</p>',
    'lyzarske-kombinezy': '<h3>Kdy kupovat</h3><p>Dětské velikosti se rychle vyprodají na začátku sezóny. Ceny se během zimy mění a po sezóně bývají kombinézy zlevněné, ale výběr velikostí je užší.</p>',
    'lyzarske-cepice-a-nakrcniky': '<h3>Kdy kupovat</h3><p>Na podzim je nejširší výběr barev a velikostí. Nákrčník nebo čepici se vyplatí pořídit v několika kusech, protože se při jízdě zamoří potem a je dobré mít náhradu.</p>',
    'krasobruslarske-brusle': '<h3>Kdy kupovat</h3><p>Brusle kupujte před začátkem sezóny, kdy je největší výběr velikostí. Pro rostoucí děti hledejte možnost výměny nebo prodeje použitých bruslí, ale nikdy nesnižujte kvalitu nože.</p>',
    'sane-a-boby': '<h3>Kdy kupovat</h3><p>Sáně se prodávají nejvíc před prvním sněhem a po sněžení se vyprodávají. Pokud víte, že je budete potřebovat, nakupujte s předstihem a zkontrolujte rozměry vzhledem k autu nebo úložišti.</p>',
}
for _k, _v in _MORE.items():
    EXTRA[_k]['guide'] += _v
