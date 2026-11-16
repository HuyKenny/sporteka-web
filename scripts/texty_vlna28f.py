"""sporteka.cz — wave 28f (16. 11. 2026): long texts for steppery, balancni-desky, drzaky-na-mobil-na-kolo.
General true facts only, no prices, no product counts, no medical promises. Phone mounts: vibration caution kept general.
Brands with an indexed page (znacky.json): hms, insportline, merco, rockbros; other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ steppery
NEW['steppery'] = dict(long=True,
    title='Steppery: mini, twister i stepper s madlem a gumami',
    desc='Mini steppery, rotační twistery, steppery s madlem i s expandéry. Jak vybrat podle odporu, nosnosti a hluku a čím se liší od aerobní bedýnky.',
    intro='<p>Stepper je jeden z nejmenších kardio trenažérů, které se dají postavit doma. Napodobuje chůzi do schodů: stojíte na dvou pedálech, střídavě je sešlapujete a odpor kladou hydraulické válce. Mini stepper zabere plochu menší než rohožka u dveří, po cvičení ho zasunete pod postel a nepotřebuje zásuvku. Vedle klasických modelů se prodávají rotační steppery, kterým se říká twistery, steppery s pevným madlem pro lepší rovnováhu a modely s gumovými expandéry na procvičení paží. Všechny spojuje to, že se dají používat kdykoli během dne, bez převlékání a cesty do posilovny.</p>'
          '<p>Sporteka shromažďuje nabídky českých obchodů ke stejnému stepperu na jednu stránku a nákup dokončíte u prodejce, kterého si vyberete. V kategorii najdete steppery ' + B(('hms', 'HMS'), ('insportline', 'inSPORTline')) + ', Maxxiva a dalších značek. Patří do skupiny <a href="/kardio-trenazery/">kardio trenažéry</a>, kde jsou i <a href="/rotopedy/">rotopedy</a> a <a href="/elipticke-trenazery/">eliptické trenažéry</a>.</p>',
    guide='<h2>Typy stepperů</h2>'
          '<p>Všechny steppery v této kategorii fungují na stejném principu, liší se ale dráhou pedálů a výbavou. Podle toho se mění, které partie se zapojí a jak stabilně se na stroji stojí.</p>'
          + T(['Typ', 'Jak se pohybuje', 'Pro koho'], [
              ['Mini stepper', 'pedály se pohybují nahoru a dolů', 'začátečníci, malý byt, krátké tréninky'],
              ['Rotační stepper (twister)', 'pedály opisují oblouk do stran, boky se natáčejí', 'ti, kdo chtějí zapojit i boky a střed těla'],
              ['Stepper s expandéry', 'k pedálům nebo rámu jsou připnuté gumy s držadly', 'kdo chce současně procvičit paže a ramena'],
              ['Stepper s madlem', 'pevné držadlo před tělem nebo po stranách', 'senioři, lidé s horší rovnováhou, začátečníci'],
              ['Schodišťový trenažér', 'velký stroj s točícími se schody nebo dlouhými pedály', 'fitness centra, vyšší nosnost a zátěž']]) +
          '<p>Velké schodišťové trenažéry z posiloven jsou úplně jiná kategorie strojů: váží desítky kilogramů, potřebují elektřinu a mají vyšší nosnost. Do běžného bytu se většinou nevejdou a v této kategorii jde především o kompaktní steppery.</p>'
          '<h2>Stepper není aerobní bedýnka</h2>'
          '<p>Slovem step se označuje i plastová aerobní bedýnka, na kterou se při step aerobiku střídavě vystupuje a sestupuje. Ta nemá žádné pohyblivé díly a odpor jí dává jen vaše tělesná hmotnost. Hodí se na skupinové lekce, kruhový trénink nebo výpady a najdete ji mezi <a href="/fitness-pomucky/">fitness pomůckami</a>. Pokud hledáte bedýnku, v kategorii stepperů ji nehledejte; a naopak stepper s pedály na lekci step aerobiku nepoužijete.</p>'
          '<h2>Odpor: hydraulické válce</h2>'
          '<p>Většina domácích stepperů používá dva hydraulické válce, které fungují podobně jako tlumiče. Při sešlápnutí pedálu se v nich olej protlačuje malým otvorem a tím vzniká odpor. U některých modelů lze odpor nastavit otočným kolečkem přímo na válci, u jiných je pevný. Nastavení odporu bývá jednoduché a jeho rozsah menší než u rotopedu nebo eliptického trenažéru.</p>'
          '<p>Hydraulika má jednu vlastnost, se kterou je dobré počítat: při dlouhém nepřerušeném cvičení se olej ve válcích zahřívá, řídne a odpor postupně klesá. Výrobci proto obvykle uvádějí maximální délku jednoho cvičení nebo doporučují přestávky. Řiďte se návodem; přehřátý válec se rychleji opotřebí a může začít prosakovat. Pro dlouhé souvislé tréninky je vhodnější eliptický trenažér nebo rotoped s magnetickou brzdou.</p>'
          '<h3>Propojené, nebo nezávislé pedály</h3>'
          '<p>U levnějších stepperů bývají pedály nezávislé: každý má svůj válec a pohybuje se sám, takže je na vás, jak hluboko sešlápnete. U propojených pedálů vede jeden pedál nahoru, když druhý jde dolů, například přes lanko nebo kladku. Pohyb je plynulejší a rytmičtější a pedál vás „nese“ zpět nahoru. Nezávislé pedály zase umožní měnit hloubku kroku podle sebe.</p>'
          '<h2>Nosnost a stabilita</h2>'
          '<p>U mini stepperů výrobci obvykle uvádějí maximální hmotnost uživatele kolem 100 až 120 kg, robustní modely snesou víc. Údaj berte vážně, protože se týká pedálů, válců i kloubů rámu. Pokud se blížíte horní hranici, vyberte model s rezervou a širší základnou. Spodní strana by měla mít gumové patky, které nekloužou po podlaze a nepoškrábou ji.</p>'
          '<p>Na stepperu bez madla stojíte na dvou malých pohyblivých plochách a rovnováhu si držíte sami. Začátečníkům a starším lidem se hodí model s pevným madlem nebo postavit stepper vedle stěny, opěradla židle nebo stolu, o které se dá v případě potřeby opřít. Madlo ale slouží k jistění, ne k zavěšení celou vahou; když se o něj opíráte, nohy pracují méně.</p>'
          '<h2>Hluk a sousedé</h2>'
          '<p>Stepper je jeden z nejtišších trenažérů. Nemá motor ani setrvačník a pohyb nevytváří údery jako běh. Přesto se mohou ozývat drobné zvuky: vrzání kloubů, cvakání dorazu pedálů nebo šum hydrauliky. Pomůže podložka pod trenažér, která utlumí přenos vibrací do podlahy a zároveň chrání parkety. Vrzající klouby obvykle stačí očistit a ošetřit podle návodu výrobce. V bytovém domě je stepper vhodnější volbou na večerní trénink než švihadlo nebo poskoky.</p>'
          '<h2>Displej a expandéry</h2>'
          '<p>Malý displej na stepperu obvykle počítá kroky, čas a odhad spálených kalorií. Kalorie berte jen orientačně, protože displej nezná vaši hmotnost, tep ani to, jak hluboko pedály sešlapujete. Užitečnější je sledovat počet kroků a čas a porovnávat tréninky mezi sebou. Displej běží na baterii, kterou je občas potřeba vyměnit.</p>'
          '<p>Gumové expandéry připnuté ke stepperu umožní během kroku přitahovat a tlačit paže. Jejich odpor bývá nízký, což stačí na zahřátí ramen a koordinaci, ne na posilování. Kdo chce paže posilovat víc, pořídí si samostatné <a href="/posilovaci-gumy/">posilovací gumy</a> s vyšším odporem.</p>'
          '<h2>Jak na stepperu cvičit</h2>'
          '<ul><li>Stůjte vzpřímeně, s mírně pokrčenými koleny a pohledem dopředu.</li>'
          '<li>Pokládejte na pedál celé chodidlo, ne jen špičku.</li>'
          '<li>Začněte kratšími úseky a postupně je prodlužujte; svaly i válce si zvyknou.</li>'
          '<li>Nehrbte se nad madlem a nepřenášejte na něj váhu.</li>'
          '<li>Cvičte ve sportovní obuvi, ne naboso nebo v pantoflích.</li>'
          '<li>Při bolesti kloubů přestaňte a poraďte se s lékařem nebo fyzioterapeutem.</li></ul>'
          '<h2>Stepper, rotoped, nebo eliptický trenažér?</h2>'
          '<p>Stepper vyhraje rozměrem, cenou za kus a tichým chodem. Rotoped je pohodlnější na dlouhé tréninky a vsedě šetří klouby nohou při nesení hmotnosti. <a href="/elipticke-trenazery/">Eliptický trenažér</a> zapojí ruce i nohy a má plynulý pohyb, zabírá ale víc místa. <a href="/behaci-pasy/">Běžecký pás</a> umožní chůzi i běh, je však největší a nejhlučnější. Pokud máte místo jen na jeden menší stroj a cvičíte krátce a pravidelně, je stepper rozumný začátek.</p>'
          '<h2>Údržba</h2>'
          '<p>Po cvičení otřete pedály a rám od potu, který časem narušuje povrch. Občas zkontrolujte šrouby a dotáhněte ty, které povolily. Klouby a osy ošetřete mazivem, které doporučuje výrobce, a hlídejte, zda z válců neprosakuje olej. Stepper skladujte v suchu; ve vlhkém sklepě rezaví ocelový rám i pružiny pedálů.</p>'
          '<h2>Kam stepper postavit</h2>'
          '<p>Stepper potřebuje rovnou a pevnou podlahu. Na měkkém koberci se může naklánět a na hladké dlažbě klouzat, proto se vyplatí protiskluzová podložka. Nad hlavou nechte dost místa: na pedálu stojíte o několik centimetrů výš a vyšší lidé si v podkrovním pokoji mohou cvičení nepříjemně zkomplikovat. Vedle stepperu mějte stěnu, skříň nebo opěradlo, kterého se chytíte, když ztratíte rovnováhu. Pokud cvičíte u televize nebo u okna, postavte stepper tak, abyste se nemuseli otáčet a krk zůstal v neutrální poloze.</p>'
          '<h2>Pravidelnost místo maratonů</h2>'
          '<p>Největší výhodou stepperu je, že je pořád po ruce. Nemusíte se oblékat na ven, jet do posilovny ani čekat na volný stroj. Proto se hodí na krátké a časté tréninky: deset až patnáct minut ráno, při oblíbeném seriálu nebo mezi dvěma pracovními hovory. Takový režim je pro hydraulické válce šetrnější než jeden dlouhý trénink a zároveň se snáz udrží jako zvyk. Když chcete trénink zpestřit, střídejte rychlejší a pomalejší úseky, nebo přidejte cviky s expandéry.</p>'
          '<h2>Steppery pod stůl</h2>'
          '<p>Některé malé steppery a šlapací pomůcky jsou určené k používání vsedě pod pracovním stolem. Mají menší odpor a krátký zdvih pedálů a slouží spíš k rozhýbání nohou při dlouhém sezení než k tréninku. Pokud chcete stepper používat vestoje i vsedě, zkontrolujte v popisu, zda to výrobce u konkrétního modelu umožňuje.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Záměna stepperu s aerobní bedýnkou.</li>'
          '<li>Model bez madla pro člověka s horší rovnováhou.</li>'
          '<li>Přehlédnutá maximální nosnost.</li>'
          '<li>Hodinový trénink bez přestávky, při kterém se hydraulika přehřeje.</li>'
          '<li>Očekávání, že displej změří kalorie přesně.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Karta stepperu ukazuje nabídky více obchodů, jejich dostupnost a dopravu, objednávku pak dokončíte v e-shopu. Rozhodujte se nejprve podle typu pohybu a nosnosti, potom podle výbavy jako madlo, expandéry nebo nastavitelný odpor. Další stroje do domácí posilovny najdete v kategoriích <a href="/veslovaci-trenazery/">veslovací trenažéry</a> a <a href="/rotopedy/">rotopedy</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi stepperem a aerobní bedýnkou?', 'Stepper má dva pohyblivé pedály s hydraulickým odporem. Aerobní bedýnka je pevný plastový stupínek, na který se vystupuje při step aerobiku. Bedýnky najdete mezi fitness pomůckami.'),
        ('Proč stepper po čase cvičení povolí?', 'Olej v hydraulických válcích se při dlouhém cvičení zahřívá a odpor klesá. Výrobci proto doporučují přestávky nebo omezenou délku jednoho cvičení. Řiďte se návodem.'),
        ('Kolik vydrží stepper kilogramů?', 'U mini stepperů výrobci obvykle uvádějí kolem 100 až 120 kg, robustní modely víc. Nosnost najdete v parametrech každého výrobku a je dobré mít rezervu.'),
        ('Je stepper hlučný?', 'Patří k nejtišším trenažérům. Může vrzat nebo cvakat, pomůže ale podložka pod trenažér a údržba kloubů podle návodu.'),
        ('Co je rotační stepper?', 'Stepper, jehož pedály se pohybují po oblouku do stran, takže se při kroku natáčejí boky. Říká se mu také twister.'),
        ('Je stepper vhodný pro seniory?', 'Model s pevným madlem ano, protože usnadní udržení rovnováhy. Začínejte krátce a při potížích s klouby se nejdřív poraďte s lékařem nebo fyzioterapeutem.'),
        ('Potřebuje stepper elektřinu?', 'Ne. Odpor vytvářejí hydraulické válce a displej běží na malou baterii. Stepper tak můžete postavit kamkoli, kde je rovná a pevná podlaha.'),
        ('Jsou kalorie na displeji přesné?', 'Ne, jde jen o odhad. Displej nezná vaši hmotnost ani tep. Spolehlivější je sledovat počet kroků a čas a porovnávat tréninky mezi sebou.'),
    ])

# ------------------------------------------------------------------ balancni-desky
NEW['balancni-desky'] = dict(long=True,
    title='Balanční deska: wobble, rocker, Rola Bola i pro děti',
    desc='Balanční desky wobble a rocker, roller boardy na trénink surfu a skate, dřevěné houpací desky a labyrinty pro děti. Typy, bezpečnost a výběr.',
    intro='<p>Balanční deska je plocha, která pod nohama nestojí pevně, ale kolébá se, naklání nebo jezdí. Tělo musí neustále drobně vyrovnávat polohu, a tak se trénuje rovnováha, souhra svalů a postřeh. Desky používají sportovci při přípravě na lyže, snowboard, surf nebo skateboard, lidé cvičící doma pro zpestření a děti jako hračku, na které se dá houpat i stavět. Podle tvaru spodní části se dělí na několik typů s velmi rozdílnou obtížností. Správná volba proto začíná otázkou, kdo na desce bude stát a co chce trénovat.</p>'
          '<p>Na Sportece najdete nabídky českých obchodů k jednotlivým deskám, koupi pak dokončíte přímo v e-shopu. Zastoupené jsou značky Epicstar, Sedco, ' + B(('merco', 'Merco')) + ', Sharp Shape a další. Balanční desky patří do kategorie <a href="/balancni-pomucky/">balanční pomůcky</a>, kde jsou i <a href="/balancni-podlozky-bosu/">balanční podložky a BOSU</a>.</p>',
    guide='<h2>Typy balančních desek</h2>'
          '<p>Obtížnost desky určuje hlavně to, kolem kolika os se může naklánět a zda se celá plocha může posouvat. Začátečník by měl začít u jednodušších typů a teprve s jistotou přejít k těm, které jezdí.</p>'
          + T(['Typ', 'Pohyb', 'Obtížnost a použití'], [
              ['Wobble board (kruhová deska)', 'naklání se do všech stran na polokouli', 'střední, posilovna, rehabilitace kotníku pod dohledem odborníka'],
              ['Rocker board (kolébka)', 'naklání se jen v jedné ose, dopředu a dozadu nebo do stran', 'nejjednodušší, vhodná na začátek'],
              ['Roller board (deska na válci)', 'deska jezdí po válci, který se kutálí po zemi', 'vysoká, trénink surfu, skate a snowboardu'],
              ['Deska s nafukovacím polštářem', 'deska leží na nafukovacím disku a naklání se i otáčí', 'mírnější varianta roller boardu'],
              ['Dřevěná houpací deska pro děti', 'prohnutá deska se houpá jako kolébka', 'hračka, houpačka, můstek či skluzavka'],
              ['Deska s labyrintem', 'naklání se a kulička se vede bludištěm', 'hra pro děti, trénink koordinace']]) +
          '<h2>Wobble board a rocker board</h2>'
          '<p>Kruhová deska na polokouli, které se anglicky říká wobble board, je nejrozšířenější typ. Naklání se do všech směrů, a tak se musí stabilizovat kotníky, kolena i kyčle současně. Obtížnost určuje výška a tvar polokoule: nižší polokoule znamená menší náklon a snazší ovládání. Některé desky mají výměnné polokoule různých výšek, takže obtížnost roste s vámi.</p>'
          '<p>Rocker board má místo polokoule půlválec nebo dvě lišty, takže se kolébá jen v jedné rovině. Když ji otočíte o devadesát stupňů, změníte směr náklonu z předozadního na boční. Pro začátek je to nejpřívětivější typ. Fyzioterapeuti obě desky využívají při cvičení po zranění kotníku, cviky by vám ale měl sestavit odborník, ne video na internetu.</p>'
          '<h2>Roller boardy: Rola Bola a Indo Board</h2>'
          '<p>Roller board je prkno položené na válci, který se volně kutálí po podlaze. Deska se tak naklání i posouvá a jezdec musí neustále hlídat, aby z ní nesjel. Princip je známý z cirkusového čísla Rola Bola, ze kterého se název ujal. Indo Board a podobné desky mají tvar malého surfu a pod nimi oválný válec, se kterým se dá provádět i natáčení a prudší přesuny. Surfaři, skateboardisté, snowboardisté a kiteři na nich trénují postoj a reakce mimo vodu i mimo sníh.</p>'
          '<p>Pro začátečníky se prodávají měkčí podložky nebo nafukovací polštáře, které se dávají pod desku místo válce. Deska se na nich jen naklání a nemůže ujet, takže si zvyknete na postoj bez rizika pádu. Válce mají často na koncích desky zarážky, které brání tomu, aby deska z válce sklouzla úplně. Kdo s roller boardem začíná, ať si válec postaví na koberec nebo cvičební podložku, která pohyb zpomalí.</p>'
          '<h2>Bezpečnost na prvním místě</h2>'
          '<ul><li><strong>Volný prostor:</strong> kolem desky nesmí být nábytek s ostrými rohy, sklo ani schody.</li>'
          '<li><strong>Měkký podklad:</strong> začínejte na koberci nebo na podložce, ne na kluzké dlažbě.</li>'
          '<li><strong>Opora:</strong> první pokusy dělejte u stěny, u opěradla židle nebo s partnerem, který vás jistí.</li>'
          '<li><strong>Obuv:</strong> v ponožkách na hladké desce snadno sklouznete; noste sportovní boty nebo cvičte naboso na protiskluzovém povrchu.</li>'
          '<li><strong>Postupnost:</strong> rocker a wobble board nejdřív, roller board až po získání jistoty.</li>'
          '<li><strong>Ochrana:</strong> u roller boardu zvažte chrániče zápěstí a kolen, podobně jako při jízdě na skateboardu.</li></ul>'
          '<p>Na desku nastupujte vždy tak, že nejdřív postavíte jednu nohu na stranu, která je u země, a pak přenesete váhu. Seskakujte dopředu nebo do strany od válce, nikdy dozadu, kam deska ujíždí.</p>'
          '<h2>Balanční desky pro děti</h2>'
          '<p>Dětské dřevěné houpací desky ve tvaru prohnutého oblouku jsou oblíbené v rodinách, které vyhledávají otevřené hračky bez pevně daného použití. Dítě se na nich houpe vestoje, vleže i vsedě, otočená deska slouží jako můstek pro autíčka nebo jako tunel. Pro mladší děti se prodávají také senzorické desky a chodníčky s různými povrchy a desky s labyrintem, ve kterém se naklápěním vede kulička k cíli.</p>'
          '<p>U dětských desek kontrolujte doporučený věk a maximální nosnost, kvalitu povrchové úpravy a zaoblení hran. Lakované dřevo by mělo být určeno pro dětské hračky. Malé děti nechávejte na desce jen pod dohledem a dbejte, aby nestála u schodů nebo u stolu s ostrými rohy. Roller boardy na válci pro malé děti vhodné nejsou.</p>'
          '<h2>Materiál a povrch</h2>'
          '<p>Většina desek pro dospělé je z vrstvené překližky, která je pevná, pružná a nepraská. Levnější wobble boardy bývají z plastu, jsou lehké a odolné vůči vlhkosti, ale méně tuhé. Horní plocha by měla mít protiskluzovou úpravu: brusný papír podobný gripu na skateboardu, gumu nebo vlnitý plast. Válec u roller boardu bývá z plastu nebo dřeva, gumový potah snižuje hluk a chrání podlahu.</p>'
          '<p>Rozměr desky volte podle velikosti chodidel a postoje. Na wobble boardu by se měla vejít obě chodidla na šířku ramen. Roller boardy mají délku podobnou skateboardu, aby šel zaujmout boční postoj surfaře.</p>'
          '<h2>Jak s deskou trénovat</h2>'
          '<p>Začněte se stojem na obou nohou a snahou udržet okraj desky nad zemí deset až dvacet vteřin. Pak přidejte pomalé podřepy, přenášení váhy z nohy na nohu a stoj na jedné noze. Pokročilí zkoušejí chytat míč, otáčet se nebo kombinovat desku s kliky, kdy se o ni opírají rukama. Cvičte krátce a soustředěně: balanční trénink je náročný na pozornost a s únavou rychle klesá kvalita pohybu i bezpečnost.</p>'
          '<p>Na přípravu na lyžařskou nebo snowboardovou sezonu se hodí zařadit desku jako součást rozcvičky několikrát týdně. Pro trénink na prkně se nejvíc blíží roller board; pro obecnou stabilitu stačí wobble board.</p>'
          '<h2>Balanční deska u stojícího stolu</h2>'
          '<p>Kdo pracuje u stojícího stolu, používá někdy nízkou balanční desku nebo rocker board jako podložku pod nohy. Drobné kolébání nutí měnit postoj a stání tolik neunavuje. Pro tento účel se hodí desky s malým náklonem a širokou plochou, ne roller boardy. Počítejte s tím, že soustředění na práci a na rovnováhu najednou chvíli trvá, a začněte kratšími úseky.</p>'
          '<h2>S čím desku kombinovat</h2>'
          '<p>Balanční deska je jen jedna z pomůcek na stabilitu. Polokoule typu BOSU dovolí širší škálu cviků včetně kliků a výpadů, vzduchová čočka se hodí na stoj na jedné noze a pěnová podložka na první krůčky po zranění. Mnoho lidí kombinuje desku s cvičením jógy nebo pilates, kde se stabilita trénuje bez pomůcek. Pro doplnění se podívejte na <a href="/jogove-pomucky/">jógové pomůcky</a>, kde najdete bloky a podložky, které se hodí i pod desku.</p>'
          '<h2>Péče o desku</h2>'
          '<p>Dřevěnou desku skladujte v suchu, protože vlhko překližku kroutí a odlepuje vrstvy. Protiskluzový povrch po čase ztrácí drsnost a lze ho vyměnit za nový grip. U roller boardu kontrolujte zarážky na koncích desky a povrch válce; prasklý válec nebo uvolněná zarážka jsou důvodem k opravě před dalším cvičením. Dětské desky občas přetřete přípravkem, který výrobce doporučuje.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Roller board jako první deska pro úplného začátečníka.</li>'
          '<li>Cvičení na hladké dlažbě bez opory v dosahu.</li>'
          '<li>Dětská deska postavená u schodů nebo u nábytku s ostrými rohy.</li>'
          '<li>Deska bez protiskluzového povrchu, na které se cvičí v ponožkách.</li>'
          '<li>Rehabilitační cviky po zranění bez porady s fyzioterapeutem.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě desky vidíte nabídky různých obchodů i dopravu, objednávka pak proběhne u prodejce. Nejprve si vyberte typ podle toho, co chcete trénovat, a teprve potom materiál a vzhled. Pro trénink na prkno se podívejte i na <a href="/skateboardy/">skateboardy</a> a <a href="/paddleboardy/">paddleboardy</a>, k domácímu cvičení na <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>',
    faq=[
        ('Jakou balanční desku zvolit na začátek?', 'Nejjednodušší je rocker board, která se kolébá jen v jedné ose. Pak můžete přejít na kruhový wobble board. Roller board na válci je až pro pokročilé.'),
        ('Co je Rola Bola?', 'Prkno položené na válci, který se kutálí po zemi. Deska se naklání i posouvá. Název pochází z cirkusového čísla a podobné desky slouží k tréninku surfu, skateboardingu a snowboardingu.'),
        ('Je roller board nebezpečný?', 'Při neopatrném použití ano. Začínejte na koberci nebo podložce, s oporou u stěny nebo s partnerem, ve volném prostoru a případně s chrániči zápěstí a kolen.'),
        ('Od kolika let je balanční deska vhodná pro děti?', 'Řiďte se doporučeným věkem a nosností od výrobce. Dřevěné houpací desky jsou určené už pro malé děti, vždy ale pod dohledem. Roller boardy na válci pro malé děti vhodné nejsou.'),
        ('Pomůže balanční deska po zranění kotníku?', 'Fyzioterapeuti desky při cvičení po zranění kotníku používají, cviky by ale měl sestavit odborník podle vašeho stavu. Bez porady s ním s rehabilitací na desce nezačínejte.'),
        ('Jak dlouho na desce cvičit?', 'Krátce a soustředěně, například několik minut jako součást rozcvičky. S únavou klesá kvalita pohybu i bezpečnost.'),
        ('Hodí se balanční deska ke stojícímu stolu?', 'Ano, nízká deska s malým náklonem nebo rocker board poslouží jako podložka pod nohy. Roller board na válci se k práci nehodí.'),
        ('Mohu na desce cvičit naboso?', 'Ano, pokud má deska protiskluzový povrch. V ponožkách na hladké desce snadno sklouznete, proto zvolte bosou nohu nebo sportovní obuv.'),
    ])

# ------------------------------------------------------------------ drzaky-na-mobil-na-kolo
NEW['drzaky-na-mobil-na-kolo'] = dict(long=True,
    title='Držák na mobil na kolo: na řídítka, představec i brašna',
    desc='Držáky na mobil na kolo: na řídítka a představec, systémové s pouzdrem, vodotěsná pouzdra i brašny s okénkem. Kompatibilita, vibrace a déšť.',
    intro='<p>Držák na mobil na kolo udělá z telefonu navigaci a cyklocomputer. Mapa je na očích, nemusíte zastavovat a lovit telefon z kapsy a s aplikací vidíte i rychlost, převýšení nebo trasu, kterou jste si naplánovali. Nabídka se ale hodně liší: od univerzálních silikonových úchytů přes pérové čelisti na řídítka až po systémové držáky, u kterých se telefon v pouzdře zacvakne pootočením. Do kategorie patří také vodotěsná pouzdra a brašny na rám s průhledným okénkem. Výběr začíná u telefonu a řídítek, které máte, ne u vzhledu držáku.</p>'
          '<p>Nabídky českých e-shopů k jednotlivým držákům najdete na Sportece pohromadě a objednáte v tom obchodě, který vám vyhovuje. V kategorii jsou výrobky SP Connect, Quad Lock, Fidlock, Topeak, Swissten, ' + B(('rockbros', 'Rockbros')) + ' a dalších značek. Patří do skupiny <a href="/cyklo-lahve-a-drzaky/">cyklo lahve a držáky</a>, souvisejí s ní <a href="/cyklo-computery/">cyklocomputery</a> a <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>',
    guide='<h2>Typy držáků</h2>'
          + T(['Typ', 'Jak drží telefon', 'Výhody a nevýhody'], [
              ['Silikonový úchyt', 'pružná pryž se natáhne přes rohy telefonu', 'univerzální a lehký, na hrubém terénu méně jistý'],
              ['Pérové čelisti', 'kovové nebo plastové čelisti sevřou telefon z boků', 'pasuje na většinu telefonů, kontrolujte rozsah šířky'],
              ['Systémový držák s pouzdrem', 'telefon v pouzdře se zacvakne pootočením', 'pevný a rychlý, potřebuje pouzdro na konkrétní model'],
              ['Magnetický a podtlakový držák', 'magnet a přísavná plocha drží telefon nebo pouzdro', 'rychlé nasazení, u některých chybí mechanická pojistka'],
              ['Vodotěsné pouzdro', 'telefon je uzavřený v obalu s průhlednou fólií', 'chrání před deštěm, ovládání přes fólii je méně přesné'],
              ['Brašna s okénkem', 'telefon leží v kapse brašny na rámu nebo na řídítkách', 'úložný prostor navíc, telefon je níž a hůř čitelný']]) +
          '<h2>Univerzální držáky</h2>'
          '<p>Silikonové úchyty a držáky s pérovými čelistmi, jaké prodávají například Swissten nebo Rockbros, se hodí pro většinu telefonů bez ohledu na značku. Stačí zkontrolovat rozsah šířky nebo úhlopříčky, který výrobce uvádí, a počítat s tím, že pouzdro telefon zvětší. Jsou dobrou volbou pro město, výlety po cyklostezkách a pro ty, kdo telefon často mění. Na rozbitých lesních cestách ale mohou povolit, a proto je dobré mít telefon ještě zajištěný poutkem nebo gumou, kterou část držáků obsahuje.</p>'
          '<h2>Systémové držáky: Quad Lock, SP Connect, Topeak</h2>'
          '<p>Systémové držáky fungují jako bajonet. Na telefon nasadíte pouzdro nebo nalepíte adaptér, který zapadne do protikusu na kole a pootočením se zajistí. Telefon pak drží pevně i na hrubém terénu a nasadíte ho jednou rukou. Výhodou je, že stejné pouzdro pasuje i do držáku v autě, na kočárku nebo na běžecké rameno stejného výrobce. Nevýhodou je, že potřebujete pouzdro pro svůj konkrétní model telefonu, a když telefon vyměníte, kupujete pouzdro nové. Topeak nabízí podobný systém s pouzdry RideCase.</p>'
          '<p>Fidlock Vacuum spojuje magnet s přísavnou plochou: telefon se k základně přicvakne magneticky a podtlak ho drží na místě, sundá se otočením. Výrobce k němu nabízí pouzdra i univerzální podložku na telefon. U magnetických držáků obecně si všímejte, zda mají kromě magnetu i mechanickou pojistku. Samotný magnet nemusí při tvrdém nárazu na hrubém terénu stačit.</p>'
          '<h2>Kam držák připevnit</h2>'
          '<ul><li><strong>Na řídítka:</strong> nejběžnější umístění, telefon je ve výšce očí jezdce.</li>'
          '<li><strong>Na představec:</strong> telefon je uprostřed, blíž k ose kola a méně vibruje.</li>'
          '<li><strong>Na víčko hlavového složení:</strong> nízký a kompaktní držák místo horní krytky představce.</li>'
          '<li><strong>Před řídítka (out-front):</strong> telefon vystrčený před řídítka, podobně jako cyklocomputer na silničce.</li>'
          '<li><strong>Do brašny na rámu nebo na řídítka:</strong> telefon je chráněný a pod ním je místo na doklady a svačinu.</li></ul>'
          '<h2>Průměr řídítek a kompatibilita</h2>'
          '<p>Řídítka nemají všude stejný průměr. U gripů měří obvykle 22,2 mm, v místě objímky představce bývá 31,8 mm, u starších a městských kol 25,4 mm a u moderních horských kol 35 mm. Držák na řídítka proto zkontrolujte, pro jaký průměr je určený a zda má v balení vymezovací gumičky. Místo na řídítkách je navíc omezené světlem, zvonkem, řadicími páčkami a u elektrokol i ovladačem motoru. Než držák objednáte, prohlédněte si svá <a href="/cyklo-riditka/">řídítka</a> a představte si, kam se vejde.</p>'
          '<p>U <a href="/elektrokola/">elektrokol</a> je to ještě složitější, protože uprostřed řídítek bývá displej. Část výrobců proto nabízí držáky na představec nebo kombinované držáky, které nesou telefon nad displejem.</p>'
          '<h2>Vibrace a fotoaparát telefonu</h2>'
          '<p>Moderní telefony mají fotoaparáty s optickou stabilizací a pohyblivými součástkami. Někteří výrobci telefonů upozorňují, že silné vibrace o určitých frekvencích, typicky od motorů výkonných motocyklů, mohou tyto součástky poškodit, a doporučují držáky s tlumením vibrací. Kolo takové vibrace běžně nevytváří, na hrubém terénu, na kostkách a u elektrokol ale může být rozumné zvolit držák s tlumičem, jaký nabízejí výrobci systémových držáků. Pokud telefon používáte i na motorce nebo skútru, řiďte se doporučením výrobce telefonu.</p>'
          '<h2>Déšť, slunce a mráz</h2>'
          '<p>Mnoho telefonů má krytí proti vodě, déšť jim ale stejně nedělá dobře: mokrý displej reaguje nepřesně a do nabíjecího konektoru se dostane voda. Na delší jízdy v nejistém počasí se hodí vodotěsné pouzdro nebo pláštěnka na držák, kterou nabízí část výrobců. V létě se telefon v přímém slunci s rozsvíceným displejem a zapnutou navigací přehřívá a může ztlumit jas nebo vypnout aplikaci. V zimě zase baterie v mrazu rychle ubývá. Na dlouhé jízdy proto počítejte s nabíjením.</p>'
          '<h2>Nabíjení za jízdy</h2>'
          '<p>Navigace s rozsvíceným displejem spotřebuje hodně energie. Na celodenní výlet se hodí <a href="/powerbanky-a-nabijeni/">powerbanka</a> v brašně na rámu, propojená krátkým kabelem s telefonem. Některá elektrokola mají na displeji USB port a cestovatelé na dlouhé trasy používají dynamo v náboji s USB nabíječkou. Kabel veďte tak, aby se nezachytil o kolena ani o řídítka při zatáčení.</p>'
          '<h2>Bezpečnost za jízdy</h2>'
          '<p>Telefon za jízdy nedržte v ruce. Pravidla silničního provozu to zakazují řidičům a cyklista je také řidič. Displej sledujte jen krátkým pohledem, podobně jako tachometr, a trasu si nastavte před odjezdem. Hlasová navigace ve sluchátku na jednom uchu nebo zvukové pokyny z reproduktoru vám pomohou mít oči na silnici. Když odcházíte od kola, telefon z držáku vezměte, jinak ho můžete snadno ztratit. Na skupinových vyjížďkách se vyplatí mít telefon v držáku i kvůli tomu, že v případě nehody nebo defektu rychle zavoláte pomoc a pošlete ostatním svou polohu.</p>'
          '<h2>Montáž držáku</h2>'
          '<p>Většina držáků se připevní objímkou se šroubem nebo gumovým páskem, bez speciálního nářadí. Šrouby dotahujte s citem; u karbonových řídítek a představců dodržte utahovací moment, který uvádí výrobce dílu, a ověřte, zda je držák pro karbon vhodný. Přílišná síla může karbonový díl poškodit, aniž by to bylo hned vidět. Po první jízdě zkontrolujte, zda se držák neotočil, a podle potřeby ho dotáhněte. Telefon nastavte tak, aby displej nestál proti slunci a nezakrýval světlo ani zvonek.</p>'
          '<h2>Aplikace a nastavení telefonu</h2>'
          '<p>Před výletem si stáhněte mapy offline, protože v lese a na horách často chybí signál a stahování map za jízdy vybíjí baterii. Prodlužte dobu, po které se displej zhasne, nebo naopak nastavte rozsvícení jen při navigačním pokynu, podle toho, zda šetříte baterii, nebo chcete mapu stále na očích. Kdo jezdí hlavně trénink a nepotřebuje velkou mapu, může zvážit samostatný <a href="/cyklo-computery/">cyklocomputer</a>, který vydrží déle na baterii a telefon zůstane v kapse.</p>'
          '<h2>Koloběžka, kočárek a druhé kolo</h2>'
          '<p>Univerzální držáky na řídítka se dají použít i na koloběžkách a elektrokoloběžkách, pokud sedí průměr tyče. Systémové držáky mají výhodu u více kol v rodině: na každé kolo připevníte jen levný protikus a telefon v pouzdře přecvaknete podle toho, na čem zrovna jedete. U <a href="/kolobezky/">koloběžek</a> a elektrokoloběžek platí stejná pravidla jako na kole, včetně opatrnosti kvůli vibracím z malých kol.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Držák pro telefon bez pouzdra, který se s pouzdrem nevejde.</li>'
          '<li>Nesprávný průměr řídítek a chybějící vymezovací gumičky.</li>'
          '<li>Magnetický držák bez pojistky na hrubý terén.</li>'
          '<li>Navigace celý den bez powerbanky.</li>'
          '<li>Telefon ponechaný v držáku na zaparkovaném kole.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě držáku vidíte nabídky různých obchodů a podmínky dopravy, objednávka pak proběhne přímo v e-shopu. Nejprve si ověřte velikost telefonu s pouzdrem a průměr řídítek, pak si vyberte typ uchycení. K jízdě za šera se hodí <a href="/cyklo-svetla/">cyklo světla</a> a další drobnosti najdete v kategorii <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>.</p>',
    faq=[
        ('Jaký držák na mobil na kolo je nejpevnější?', 'Na hrubý terén jsou nejjistější systémové držáky, u kterých se telefon v pouzdře zacvakne pootočením. Univerzální čelisti a silikonové úchyty stačí do města a na cyklostezky.'),
        ('Pasuje držák na každá řídítka?', 'Ne vždy. Řídítka mají průměr 22,2, 25,4, 31,8 nebo 35 mm. Zkontrolujte, pro jaký průměr je držák určený a zda obsahuje vymezovací gumičky.'),
        ('Mohou vibrace poškodit telefon?', 'Někteří výrobci telefonů upozorňují, že silné vibrace, například od výkonných motocyklů, mohou poškodit stabilizaci fotoaparátu. Na kole je riziko menší, na hrubém terénu a elektrokole ale zvažte držák s tlumením.'),
        ('Co dělat, když prší?', 'Použijte vodotěsné pouzdro nebo pláštěnku na držák. I telefon s krytím proti vodě v dešti reaguje nepřesně a do konektoru se může dostat voda.'),
        ('Proč se telefon v držáku vypíná?', 'V přímém slunci se s navigací a rozsvíceným displejem přehřívá, v mrazu zase rychle ubývá baterie. Na delší jízdy počítejte s powerbankou a s ochranou před sluncem.'),
        ('Je lepší držák, nebo brašna s okénkem?', 'Držák drží telefon výš a lépe čitelný. Brašna s okénkem ho chrání před deštěm a nabídne místo pro powerbanku a drobnosti, displej je ale níž a ovládání přes fólii je méně přesné.'),
        ('Hodí se držák i na karbonová řídítka?', 'Záleží na modelu. Ověřte, zda je držák pro karbon vhodný, a šrouby dotahujte s citem podle momentu, který uvádí výrobce řídítek nebo představce.'),
        ('Mohu za jízdy telefon ovládat?', 'Telefon v ruce za jízdy držet nesmíte. Na displej se dívejte jen krátce a trasu si nastavte před odjezdem; pomohou hlasové pokyny.'),
    ])
