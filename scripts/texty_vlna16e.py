"""sporteka.cz — wave 16e (4. 11. 2026): long texts (>= 1650 words) for funkcni-trenink, kardio-trenazery, doplnky-k-obuvi, rybarske-tasky.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ funkcni-trenink
NEW['funkcni-trenink'] = dict(long=True,
    title='Funkční trénink a hrazdy: medicinbaly, bradla | Sporteka',
    desc='Hrazdy, bradla, medicinbaly, slam bally a závěsné popruhy z českých obchodů. Jak vybrat podle místa, nosnosti a cíle tréninku a kde je nejlevněji.',
    intro='<p>Funkční trénink stojí na pohybech, které zapojují celé tělo najednou: tahy, tlaky, dřepy, výpady, rotace a nošení zátěže. Proto se k němu nehodí jeden velký stroj, ale sada menších pomůcek, které se vejdou do bytu, garáže nebo na zahradu. V této kategorii najdete <strong>hrazdy, bradla, medicinbaly, slam bally, závěsné popruhy a kruhy</strong> a u každé položky porovnáte nabídky českých obchodů vedle sebe.</p>'
          '<p>Největší podskupinou jsou <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>. Na ně navazují <a href="/fitness-pomucky/">fitness pomůcky</a>, <a href="/cinky-a-kotouce/">činky a kotouče</a> a <a href="/fitness/">fitness</a> jako celek. Správnou volbu určuje hlavně místo, kde budete cvičit, tělesná hmotnost cvičícího a styl tréninku, nikoli značka.</p>',
    guide='<h2>Co do funkčního tréninku patří</h2>'
          '<p>Pojem je široký, a proto se pod něj ve vybavení vejde hodně věcí. Společné mají to, že zátěží je často vlastní tělo nebo lehká pomůcka a že se cviky dají řetězit do kruhů a sérií. Přehled hlavních skupin zboží:</p>'
          + T(['Pomůcka', 'K čemu slouží', 'Na co dát pozor při výběru'], [
              ['Hrazda dveřní nebo nástěnná', 'shyby, zavěšené zdvihy nohou, visy', 'způsob uchycení, nosnost, šířka úchopu'],
              ['Bradla a stojany', 'kliky na bradlech, dipy, zdvihy nohou', 'stabilita, výška, rozteč madel'],
              ['Medicinbal', 'hody, přihrávky, rotace, dřepy se zátěží', 'povrch, odrazivost, hmotnost míče'],
              ['Slam ball', 'prudké hody o zem, intervaly', 'bezodrazový plášť, pevnost švů'],
              ['Závěsné popruhy a kruhy', 'veslování, kliky, tahy na nestabilním závěsu', 'karabina, délka popruhu, bod zavěšení'],
              ['Plyo box a plošiny', 'výskoky, nášlapy, zvyšování pohybu', 'materiál, protiskluz, výška'],
              ['Sandbag a váčky', 'nošení, přehazování, dřepy', 'úchopy, výplň, šití']]) +
          '<h2>Hrazdy a bradla: základ domácího tréninku</h2>'
          '<p>Hrazda je pomůcka, která za málo místa nabídne nejvíc. Dveřní model se opírá o zárubeň nebo se zaklesne za rám a lze jej po cvičení sundat. Nástěnná hrazda se šroubuje přímo do zdi a unese výrazně víc, ale vyžaduje vhodný podklad, tedy zdivo nebo beton, a ne sádrokartonovou příčku. Samostatně stojící konstrukce zabere podlahu, nemusíte však nic vrtat a hodí se do garáže či na terasu.</p>'
          '<p>Ve výběru sledujte uvedenou nosnost a počítejte s dynamickým zatížením. Při švihových cvicích na hrazdě působí na úchyty víc než jen klidná hmotnost těla. Rozteč úchopů ovlivňuje, které svaly pracují: úzký úchop zatěžuje víc biceps, široký záda. Hrazda s několika polohami madel, takzvaná víceúchopová, dovolí všechny varianty a je pro začátečníka praktičtější než jednoduchá tyč.</p>'
          '<p>Bradla se používají na kliky, dipy a zdvihy nohou. Parallettes neboli nízká paralelní madla jsou menší varianta, kterou si odložíte do skříně. Dobrá bradla nemají vrávorat při přenesení váhy na jednu stranu a mají madla s protiskluzovým povrchem. Obojí najdete v podkategorii <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</p>'
          '<h2>Medicinbaly a slam bally</h2>'
          '<p>Medicinbal je těžký míč, který se zvedá, přihrává a hází. Gumový nebo koženkový povrch mívá lepší úchop než hladký plast. Variantu s odrazem můžete házet o zeď, tvrdou podlahu poškodí méně než pevná koule. Slam ball se naopak do země buší a od země se neodráží, protože uvnitř je písek nebo podobná výplň. Slouží ke krátkým výbušným sériím a k odreagování po práci.</p>'
          '<p>Hmotnost volte podle cviku. Na rotace a přihrávky ve dvojici se používají lehčí míče, na dřepy a přenášení těžší. Začátečník si často vybere příliš těžký kus a pak ztrácí techniku, proto je rozumné začít nižší hmotností a přidávat podle toho, jak se pohyb zlepšuje. Pro doplnění sestavy se hodí i <a href="/posilovaci-stroje/">posilovací stroje</a> a <a href="/masazni-pomucky/">masážní pomůcky</a> na regeneraci.</p>'
          '<h2>Závěsné popruhy, kruhy a další závěsné systémy</h2>'
          '<p>Popruhy typu TRX využívají zavěšení u dveří, hrazdy nebo stropního háku a zátěží je úhel těla vůči zemi. Čím víc se naklopíte, tím je cvik těžší, a tak lze intenzitu měnit bez výměny vybavení. Při nákupu se podívejte na pevnost karabiny, šití a nastavení délky. Kruhy, známé z gymnastiky, vyžadují zavěšení do pevného bodu a trénují stabilizaci ramen víc než pevná tyč. Jsou vhodné pro zkušenější cvičence.</p>'
          '<h2>Vybírejte podle místa a cíle</h2>'
          + T(['Situace', 'Rozumná sestava'], [
              ['Malý byt bez možnosti vrtat', 'dveřní hrazda, závěsné popruhy, malý medicinbal'],
              ['Vlastní dům nebo garáž', 'nástěnná hrazda, bradla, slam ball, plyo box'],
              ['Terasa nebo zahrada', 'stojanová konstrukce, sandbag, kruhy'],
              ['Společný trénink ve dvojici', 'medicinbal s odrazem, závěsný systém, lehčí míče']]) +
          '<p>Před nákupem si změřte dveře, výšku stropu a volnou plochu kolem sebe. Pro shyby potřebujete místo nad hlavou, které bývá v bytě menší, než čekáte. U dveřních hrazd ověřte rozsah zárubně, která není všude stejná.</p>'
          '<h2>Pro koho se funkční trénink hodí</h2>'
          '<p>Začátečník potřebuje vybavení, které se používá k jednoduchým cvikům a nic ho nezahltí: hrazdu, popruhy a jeden míč. Pokročilý cvičenec přidá bradla, kruhy a těžší slam bally. Sportovci z míčových nebo bojových disciplín ocení výbušné cviky na doplnění kondice. Při sparingu a bojových sportech se hodí vybavení z kategorie <a href="/bojove-sporty/">bojové sporty</a>, při běhu zase výbava z oddílu <a href="/beh/">běh</a>, protože silové cvičení doplňuje vytrvalost.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Podcenění nosnosti: u hrazdy počítejte s rezervou, nejen s klidovou hmotností.</li>'
          '<li>Vrtání do nevhodné zdi: nástěnná hrazda potřebuje pevné zdivo a správné hmoždinky.</li>'
          '<li>Příliš těžký medicinbal na začátku, který zhorší techniku.</li>'
          '<li>Koupě celé sady najednou, i když budete využívat jen dva kusy.</li>'
          '<li>Zanedbání podložky: výskoky a hody vyžadují protiskluzový povrch a tlumení.</li></ul>'
          '<h2>Péče a bezpečnost</h2>'
          '<p>Před každým cvičením zkontrolujte upevnění hrazdy a stav popruhů. Praskající švy, trhliny v plášti míče nebo vůle v šroubech jsou důvody k okamžité výměně. Kovové části otřete vlhkým hadrem, aby nekorodovaly, popruhy nechte uschnout a neskladujte je na slunci. Míče z koženky se čistí vlažnou vodou, nepoužívejte agresivní rozpouštědla.</p>'
          '<p>Při cvičení bez dozoru volte jen pohyby, které dobře ovládáte, a objem zvyšujte postupně. Trpíte-li bolestmi zad, kloubů nebo ramen, poraďte se před začátkem s lékařem či fyzioterapeutem.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>Nejširší nabídku tvoří české a evropské značky: ' + B(('hms','HMS'),('insportline','Insportline'),('master','Master'),('sedco','Sedco'),('rinagym','Rinagym'),('marbo','Marbo'),('merco','Merco'),('fitforce','Fitforce'),('domyos','Domyos'),('gorilla-sports','Gorilla Sports')) + '. Rozdíly jsou hlavně v zpracování, v nosnosti a v tom, zda je přiložený montážní materiál. Porovnejte proto parametry a recenze, ne jen vzhled.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého produktu uvidíte nabídky více obchodů vedle sebe a hned zjistíte, kde je zboží skladem, jaké je poštovné a jak se liší dodací lhůta. Rozhodnutí ulehčí filtr podle značky a řazení podle oblíbenosti. Těžké zboží jako bradla a stojany se často rozváží přepravní službou, takže se vyplatí zkontrolovat dopravu. Příbuzné skupiny pro další výbavu najdete v kategoriích <a href="/sportovni-obleceni/">sportovní oblečení</a> a <a href="/sportovni-obuv/">sportovní obuv</a>.</p>',
    faq=[
      ('Jaká hrazda se hodí do bytu?', 'Pokud nechcete vrtat, vybírejte dveřní hrazdu, která se zaklesne za zárubeň nebo se vzepře o rám. Zkontrolujte, zda se vejde do vašich dveří, a dávejte pozor na nosnost. Pro pravidelný těžší trénink je vhodnější nástěnná hrazda na pevném zdivu.'),
      ('Jak poznám, že hrazda unese mou hmotnost?', 'Řiďte se uvedenou nosností od výrobce a počítejte s rezervou, protože při dynamických cvicích působí větší síly než při klidném visu. Zkontrolujte také materiál stěny či zárubně, protože nosnost konstrukce je jen tak dobrá, jako její uchycení.'),
      ('Čím se liší medicinbal od slam ballu?', 'Medicinbal se odráží nebo se přihrává a má pevnější pláště. Slam ball je plněný tak, aby se při dopadu neodrazil, a hodí se na výbušné hody o zem. Do obou lze zapojit celé tělo, ale slam ball je odolnější vůči tvrdému dopadu.'),
      ('Jak těžký medicinbal vybrat pro začátek?', 'Začněte lehčí variantou, u které udržíte správnou techniku v celé sérii. Těžší míč přidejte, až cvik zvládnete bez kompenzací. Pro rotace a přihrávky ve dvojici stačí lehčí míč, pro dřepy se hodí těžší.'),
      ('K čemu jsou závěsné popruhy?', 'Slouží ke cvikům, kde zátěží je vaše tělo a intenzitu měníte úhlem vůči zemi. Používají se na kliky, veslování, výpady a cviky na střed těla. Zavěšují se do dveří, na hrazdu nebo do stropního háku a vejdou se do batohu.'),
      ('Potřebuji k funkčnímu tréninku podložku?', 'Ano, podložka tlumí dopad, chrání podlahu a zlepšuje protiskluz. Při výskocích a hodech o zem je důležitá i tloušťka, protože tenká podložka tlumí málo. Podložky pro cvičení najdete v sekci jóga a podložky.'),
      ('Dá se funkčním tréninkem nahradit posilovna?', 'Pro základní sílu a kondici ano, pokud postupně zvyšujete obtížnost cviků a zátěž. Pro maximální sílu nebo cílenou práci na jedné svalové skupině jsou činky a stroje obvykle přesnější. Záleží na cíli a na tom, kolik prostoru a času máte.'),
      ('Jak často cvičit s touto výbavou?', 'Frekvence se řídí zkušeností, regenerací a dalšími sporty. Začátečníkovi obvykle stačí dvě až tři jednotky týdně s odpočinkem mezi nimi. Trvalá bolest nebo únava jsou signálem ke zvolnění a případně k poradě s trenérem.'),
      ('Jak pečovat o vybavení?', 'Kovové části otírejte a udržujte suché, popruhy sušte mimo přímé slunce a míče čistěte vlažnou vodou. Pravidelně kontrolujte šrouby, švy a karabiny a poškozený kus vyměňte. Hrazdu před cvičením vždy zatáhněte a ověřte její pevnost.'),
      ('Kde najdu nejvýhodnější nabídku?', 'Na stránce produktu srovnejte obchody podle dostupnosti, dopravy a doby dodání. U těžkých kusů dopravní náklady mohou výrazně změnit celkový rozdíl. Odkazy vedou do obchodů, kde nákup dokončíte.')])

# ------------------------------------------------------------------ kardio-trenazery
NEW['kardio-trenazery'] = dict(long=True,
    title='Rotopedy a trenažéry: běžecké pásy, eliptické | Sporteka',
    desc='Rotopedy, běžecké pásy, eliptické trenažéry, veslovací stroje i steppery. Jak vybrat kardio stroj do bytu a porovnat nabídky obchodů na jednom místě.',
    intro='<p>Kardio stroje umožňují trénovat vytrvalost bez ohledu na počasí, tmu nebo čas v kalendáři. Na Sportece sem patří <strong>rotopedy, běžecké pásy, eliptické trenažéry, veslovací stroje, steppery</strong> a cyklotrenažéry pro kola. Každý typ zatěžuje tělo trochu jinak a zabírá jiné množství místa, proto se vyplatí rozhodnout nejdřív, co a kde budete cvičit.</p>'
          '<p>U každého produktu porovnáte nabídky českých obchodů na jedné stránce. Související výbavu najdete v kategoriích <a href="/fitness/">fitness</a>, <a href="/posilovaci-stroje/">posilovací stroje</a>, <a href="/cyklistika/">cyklistika</a> a <a href="/sportovni-obleceni/">sportovní oblečení</a>. Před zahájením pravidelného tréninku je rozumné poradit se s lékařem, zejména při zdravotních potížích.</p>',
    guide='<h2>Jaké kardio stroje existují</h2>'
          '<p>Každý typ stroje napodobuje jinou činnost. Rotoped simuluje jízdu na kole, pás chůzi a běh, eliptický trenažér pohyb po stopě bez dopadu a veslovací stroj tah s oporou nohou. Stepper vyžaduje opakované šlapání do schodů. Rozdíly se promítají do toho, které svaly zapojíte, jak zatížíte klouby a kolik hluku stroj vydává.</p>'
          + T(['Typ stroje', 'Zapojené svaly', 'Hlavní výhoda', 'Na co dát pozor'], [
              ['Rotoped', 'nohy, hýždě', 'šetrný k kloubům, tichý', 'pohodlí sedla, plynulost záběru'],
              ['Běžecký pás', 'nohy, střed těla', 'přirozená chůze a běh', 'rozměr, hluk, délka plochy'],
              ['Eliptický trenažér', 'nohy, paže', 'plynulý pohyb bez dopadů', 'délka kroku, stabilita'],
              ['Veslovací stroj', 'záda, nohy, paže', 'zapojí většinu těla', 'délka kolejnice, odpor'],
              ['Stepper', 'nohy, hýždě', 'malé rozměry', 'plynulost chodu, výška schodu'],
              ['Cyklotrenažér', 'nohy', 'trénink na vlastním kole', 'kompatibilita kazety, hlučnost']]) +
          '<h2>Rotopedy: magnetické, spinningové, vzpřímené</h2>'
          '<p>Mezi nejběžnější patří rotopedy s magnetickým odporem, které jsou tiché, nevyžadují údržbu řemene a odpor se nastavuje knoflíkem nebo elektronicky. Spinningová kola mají těžký setrvačník a přímý řetězový nebo řemenový pohon, jízda na nich připomíná silniční kolo. Vzpřímené rotopedy mají sedlo podobné klasickému kolu, kdežto polohovací varianty umožňují opřít záda, což ocení lidé s citlivou páteří. Pod kategorií najdete i stolní minibike pro kancelář nebo seniory.</p>'
          '<p>Při výběru sledujte hmotnost setrvačníku, nastavitelnost sedla a řídítek a nosnost. Vyšší setrvačník obvykle zajistí plynulejší záběr. Pedály s třmeny nebo kompatibilní s kolářskými botami se hodí ke spinningu, ale ověřte, jaký systém stroj používá.</p>'
          '<h2>Běžecké pásy</h2>'
          '<p>Pás nabízí tréninkovou jistotu, protože tempo a sklon nastavíte přesně. Důležitá je délka a šířka plochy: kdo chce běhat, potřebuje delší plochu než ten, kdo jen svižně chodí. Motor se udává jako trvalý a špičkový výkon a rozumné je dívat se na ten trvalý. Skládací pásy se po cvičení vyklopí a zasunou ke zdi, nezapomeňte však změřit prostor, který zabírají v rozloženém stavu. Mnozí lidé používají úzký chodecký pás pod stolem, který nenahradí plnohodnotný běžecký stroj, ale k pohybu v práci stačí.</p>'
          '<p>Pro začátek je rozumné zvolit pás s tlumením pásu, které snižuje dopad na klouby. Pokud plánujete trénovat venku, najdete výbavu v kategorii <a href="/bezecka-obuv/">běžecká obuv</a> a v sekci <a href="/beh/">běh</a>.</p>'
          '<h2>Eliptické trenažéry</h2>'
          '<p>Eliptik se hodí tomu, kdo chce zapojit horní i dolní část těla bez rázů. Zásadní je délka kroku: vyšší lidé potřebují delší, aby pohyb nebyl sevřený. Setrvačník vpředu nebo vzadu určuje, jak stroj působí; zadní bývá stabilnější a tišší. Kontrolujte také, zda se madla při pohybu hýbou, nebo jsou pevná, což usnadňuje měření tepové frekvence.</p>'
          '<h2>Veslovací stroje a steppery</h2>'
          '<p>Veslovací trenažér využívá odpor vzduchu, magnetů nebo vody. Vzduchový odpor roste s tempem a zní hlasitěji, magnetický je tichý a vhodný do bytu. Správná technika vychází z nohou, ne z paží, a tomu odpovídá celá kolejnice a sedátko. Stepper je levnější a kompaktní, ale tlačí hlavně na stehna a hýždě. Jeho hydraulické válce ztrácejí s časem odpor a jejich životnost závisí na kvalitě těsnění.</p>'
          '<h2>Cyklotrenažéry pro vlastní kolo</h2>'
          '<p>Cyklotrenažér umožní zimní trénink na vlastním kole. Válcový model nabízí přirozený pocit, vyžaduje však cit pro rovnováhu. Stojánek s přímým pohonem nahradí zadní kolo a bývá tišší a přesnější. Ověřte kompatibilitu s kazetou a upínáním osy vašeho kola. Pokud ještě kolo hledáte, přejděte do sekce <a href="/jizdni-kola/">jízdní kola</a>.</p>'
          '<h2>Vyberte podle bytu a cílů</h2>'
          + T(['Situace', 'Rozumná volba'], [
              ['Malý byt, tichý provoz', 'magnetický rotoped, skládací stepper, minibike'],
              ['Chcete běhat doma', 'skládací běžecký pás s tlumením'],
              ['Citlivé klouby', 'eliptický trenažér nebo polohovací rotoped'],
              ['Chcete trénink celého těla', 'veslovací stroj'],
              ['Máte kolo a trénujete v zimě', 'cyklotrenažér s přímým pohonem']]) +
          '<h2>Počítače a měření</h2>'
          '<p>Většina strojů má displej s časem, vzdáleností, rychlostí a odhadem spálených kalorií. Údaj o energii je orientační a nelze jej brát jako přesné číslo. Tepovou frekvenci měří snímače na madlech, které bývají méně přesné než hrudní pás přes Bluetooth. Některé modely se propojí s aplikací, ale ověřte, zda nevyžadují předplatné pro plné funkce.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Nezměření prostoru v rozloženém i složeném stavu a nad hlavou.</li>'
          '<li>Podcenění hlučnosti, zejména ve panelovém domě.</li>'
          '<li>Výběr podle počtu programů místo podle kvality chodu a nosnosti.</li>'
          '<li>Očekávání, že samotný stroj udělá práci bez pravidelnosti.</li>'
          '<li>Opomenutí podložky pod stroj, která tlumí vibrace a chrání podlahu.</li></ul>'
          '<h2>Údržba</h2>'
          '<p>Běžecký pás vyžaduje občasné mazání pásu podle návodu a čištění prachu pod ním. U rotopedu se kontroluje utažení pedálů, sedla a řídítek. Veslovací kolejnici otírejte a po delší době promažte. Stroj nestavte do vlhké místnosti, kde korodují šrouby a elektronika.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Najdete zde ' + B(('hms','HMS'),('insportline','Insportline'),('skandika','Skandika'),('hop-sport','Hop-sport'),('kubisport','Kubisport'),('zipro','Zipro'),('master','Master'),('citysports','Citysports'),('domyos','Domyos'),('merach','Merach')) + ' a další. Značky se liší zpracováním rámu, kvalitou ložisek a servisem, proto čtěte parametry a podmínky záruky.</p>'
          '<h2>Pro koho se které zařízení hodí</h2>'
          '<p>Začátečníkovi poslouží jednoduchý rotoped nebo chodecký pás, který motivuje k pravidelnosti. Rodina, kde cvičí více lidí, ocení nastavitelné řídítko a sedlo. Pokročilý vytrvalostní sportovec sáhne po spinningovém kole, veslařském stroji nebo cyklotrenažéru. Pro seniory jsou vhodné stabilní polohovací modely s nízkým nástupem.</p>'
          '<p>Při srovnání nabídek na Sportece sledujte nejen cenu, ale i dopravu těžkého zboží a dobu dodání. Doplňky jako rukavice, ponožky a ručník najdete v kategoriích <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-rukavice/">sportovní rukavice</a>.</p>',
    faq=[
      ('Jaký kardio stroj je nejlepší do bytu?', 'Nejlepší je ten, který zvládnete používat pravidelně a který se vejde do prostoru. Do bytu se obvykle hodí tichý magnetický rotoped, skládací stepper nebo minibike. Běžecký pás zabere víc místa a vydává víc hluku, ale pro běh doma je nezastupitelný.'),
      ('Je lepší rotoped, nebo eliptický trenažér?', 'Oba jsou šetrné ke kloubům. Rotoped zapojuje hlavně nohy a je tišší a menší, eliptik přidává pohyb paží a zabírá víc místa. Pokud máte citlivá kolena nebo kyčle, poraďte se s lékařem, který stroj bude vhodný.'),
      ('Na co se dívat u běžeckého pásu?', 'Na délku a šířku plochy, trvalý výkon motoru, tlumení, nosnost a rozměry po složení. Chodcům stačí kratší plocha, běžci potřebují delší. Zkontrolujte také maximální rychlost a sklon, zvláště pokud chcete trénovat intervaly.'),
      ('Co znamená magnetický odpor?', 'Brzdný efekt vytvářejí magnety poblíž setrvačníku a odpor se mění jejich přiblížením. Nedochází k tření, takže je stroj tichý a prakticky bezúdržbový. Odpor lze nastavit mechanicky nebo elektronicky.'),
      ('Jak velký setrvačník je dostačující?', 'Těžší setrvačník dává plynulejší a přirozenější záběr, lehčí může působit trhaně. Pro rekreační použití stačí střední hmotnost, náročnější cvičenci ocení těžší. Hmotnost uvedenou výrobcem porovnávejte u stejného typu stroje.'),
      ('Dá se cvičit na kardio stroji každý den?', 'Záleží na intenzitě, kondici a regeneraci. Kratší a lehčí sezení lze zařazovat často, vysoké intenzity vyžadují odpočinek. Při bolesti, závratích nebo nezvyklé únavě trénink přerušte a poraďte se s lékařem.'),
      ('Kolik místa potřebuji kolem stroje?', 'Počítejte s rozměrem stroje plus volným okolím pro nástup a sestup, u pásu navíc s prostorem za ním pro případ, že byste ze stroje sestoupili za chodu. Jednotná pravidla neexistují, vždy se řiďte pokyny výrobce v návodu.'),
      ('Je údaj o spálených kaloriích přesný?', 'Ne, jde o odhad podle zadaných údajů a zvoleného odporu. Slouží ke srovnání tréninků mezi sebou, ne jako přesné měření. Přesnější je sledování času, vzdálenosti a tepové frekvence.'),
      ('Jak snížit hluk a vibrace stroje?', 'Postavte jej na protiskluzovou podložku, aby se zmenšil přenos do podlahy. Zkontrolujte utažení šroubů a vyvážení nohou. U pásů hlučnost snižuje správné promazání a čistý pás.'),
      ('Jaký trenažér pro vlastní kolo?', 'Záleží na tom, jak často trénujete a kolik jste ochotni investovat. Válce jsou přirozené, přímý pohon je tichý a přesný, stojánek s třecím kolečkem je nejjednodušší. Před nákupem ověřte kompatibilitu s kazetou a upínáním osy.')])

# ------------------------------------------------------------------ doplnky-k-obuvi
NEW['doplnky-k-obuvi'] = dict(long=True,
    title='Tkaničky, vložky a péče o boty: impregnace | Sporteka',
    desc='Tkaničky, vložky, stélky, impregnace, vosky a potřeby k bruslím. Jak vybrat doplňky podle typu bot a materiálu a porovnat nabídky obchodů na jednom místě.',
    intro='<p>Dobré boty z poloviny dělají doplňky: správně zašněrovaná bota drží nohu, vložka mění pohodlí a impregnace prodlužuje život svršku. V této kategorii najdete <strong>tkaničky, vložky a stélky, impregnace, vosky, čističe, deodoranty do bot a potřeby k bruslím</strong> a u každého zboží porovnáte nabídky českých obchodů na jedné stránce.</p>'
          '<p>Doplňky jsou záměrně levnější než samotné boty, přesto rozhodují o tom, jak dlouho obuv vydrží a jak se v ní bude chodit. Hledáte-li samotnou obuv, podívejte se do kategorií <a href="/sportovni-obuv/">sportovní obuv</a>, <a href="/trekova-obuv/">trekové boty</a>, <a href="/bezecka-obuv/">běžecké boty</a> nebo <a href="/zimni-obuv/">zimní obuv</a>. Při bolestech nohou se před koupí ortopedické vložky poraďte s odborníkem.</p>',
    guide='<h2>Co do kategorie patří</h2>'
          '<p>Doplňky k obuvi tvoří tři větší skupiny: výbava, která se vyměňuje uvnitř boty, péče o svršek a drobné součásti pro konkrétní sport. Tabulka ukazuje, co kde hledat.</p>'
          + T(['Skupina', 'Typické zboží', 'Proč se vyplatí'], [
              ['Tkaničky a šněrování', 'ploché, kulaté, elastické, reflexní, rychlošněrování', 'lepší držení nohy, rychlé obouvání'],
              ['Vložky a stélky', 'tlumicí, gelové, sportovní, ortopedické, zateplené', 'pohodlí, tlumení, zvýšení stability'],
              ['Impregnace a spreje', 'na textil, kůži, semiš, membránu', 'odpuzování vody a špíny'],
              ['Vosky a krémy', 'včelí vosk, krém na hladkou kůži', 'výživa a ochrana kůže'],
              ['Čistění a pachy', 'kartáče, čističe, deodoranty, pohlcovače', 'čistota a svěží boty'],
              ['Potřeby k bruslím', 'ostření, chrániče ostří, šněrovadla', 'bezpečná jízda a delší životnost']]) +
          '<h2>Tkaničky a způsoby šněrování</h2>'
          '<p>Tkaničky se liší průřezem, délkou a materiálem. Plochá tkanička drží uzel lépe než kulatá, kulatá zase hezky klouže v očkách. Elastické a rychlošněrovací systémy se hodí do triatlonu, na běh a pro děti, které se neumějí zavazovat. Délka se určuje podle počtu párů oček: při šesti párech vystačíte s kratší, při devíti už potřebujete výrazně delší. Reflexní provedení zlepší viditelnost za šera.</p>'
          '<p>Způsob šněrování se dá přizpůsobit anatomii nohy. Při úzké patě pomůže přidaný uzel u kotníku, při vysokém nártu přeskočení jednoho páru oček. Při tlaku na prsty se uvolní šněrování ve špičce. Tyto úpravy nic nestojí a často vyřeší problém, kvůli kterému lidé kupují jinou velikost.</p>'
          '<h2>Vložky, stélky a ortopedické doplňky</h2>'
          '<p>Vkládací stélka je vrstva, která určuje, jak bota pod chodidlem působí. Pěnová nebo gelová tlumí, tvarovaná podpírá klenbu a tenká sportovní zlepšuje cit. Vložky na ortopedickou korekci se vyrábějí na míru nebo jako sériová varianta, ale při bolesti nebo vadách je správné nejprve navštívit lékaře či ortopeda. Pro zvýšení pohodlí slouží také podpatěnky, gelové polštářky na paty a samolepicí podložky pod přední část nohy.</p>'
          '<p>Před koupí vyjměte originální stélku a přiložte novou, aby seděla do tvaru boty. Silná vložka v těsné botě zmenší vnitřní prostor a způsobí tlak, takže může být lepší sáhnout po tenčí variantě. Stélky do zimní obuvi mají reflexní fólii nebo vlněnou vrstvu, která pomáhá udržet teplo. Zimní boty najdete v sekci <a href="/zimni-obuv/">zimní obuv</a> a navazují na ně <a href="/nesmeky/">nesmeky</a>.</p>'
          '<h2>Impregnace a péče o materiály</h2>'
          '<p>Každý materiál potřebuje jiný postup. Hladká kůže se čistí, vyživí krémem nebo voskem a nakonec se nalešti. Semiš a nubuk se čistí suchým kartáčem a gumou a impregnují se spreji, které nezanechají mastné skvrny. Textilní svršky s membránou ošetřujte prostředky určenými pro membrány, protože nevhodná impregnace póry ucpe a zhorší prodyšnost.</p>'
          + T(['Materiál boty', 'Čištění', 'Ochrana'], [
              ['Hladká kůže', 'vlhký hadřík, jemný kartáč', 'krém nebo vosk, leštění'],
              ['Semiš a nubuk', 'suchý kartáč, speciální guma', 'sprej na semiš'],
              ['Textil a síťovina', 'měkký kartáč, jemné mýdlo', 'sprej na textil'],
              ['Membrána (např. Gore-Tex typ)', 'vlažná voda, šetrný prostředek', 'prací nebo sprejová impregnace pro membrány'],
              ['Guma a plast', 'vlhký hadr', 'bez zvláštní ochrany']]) +
          '<p>Impregnaci obnovujte, jakmile voda přestane po povrchu stékat a začne se vsakovat. Sprej stříkejte na čistý a suchý svršek z odstupu, aby byla vrstva rovnoměrná, a boty nechte uschnout při pokojové teplotě. Do zimy se hodí i vosky a krémy, které ochrání před solí, ale nenahradí membránu. Pro delší túry navazují <a href="/trekova-obuv/">trekové boty</a> a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>.</p>'
          '<h2>Čištění a boj se zápachem</h2>'
          '<p>Zápach vzniká z potu, který zůstává ve vložce a podšívce. Pomáhá boty po každém použití vyvětrat, vyndat stélky a střídat dva páry. Deodoranty ve spreji nebo prášku potlačují pach, ale odstranit příčinu zvládnou jen čistota a vysušení. Kartáč s měkkými štětinami zbaví podrážku bláta, čistič na boty se hodí na tvrdohlavé skvrny. Boty nesušte u topení ani na slunci, deformuje se lepení a zasychá kůže.</p>'
          '<h2>Brusle a hokejové doplňky</h2>'
          '<p>K bruslím patří ostření, chrániče ostří, šněrovadla a vosk na tkaničky. Ostří se brousí podle způsobu hry a hmotnosti hráče, protože hloubka drážky ovlivňuje záběr i klouzání. Chrániče ostří používejte při chůzi mimo led a po jízdě brusle vytřete suchým hadrem, aby ocel nerezavěla. Celá výbava je součástí kategorie <a href="/brusle/">brusle</a> a <a href="/hokej/">hokej</a>.</p>'
          '<h2>Vyberte podle sportu</h2>'
          + T(['Sport nebo využití', 'Co se hodí'], [
              ['Běh', 'tenké sportovní vložky, elastické tkaničky'],
              ['Turistika', 'impregnace, vyživující vosk, pevné tkaničky'],
              ['Zimní provoz', 'zateplené stélky, impregnace proti soli'],
              ['Míčové sporty a hala', 'tlumicí vložky, pevné ploché tkaničky'],
              ['Každodenní nošení', 'pohodlné stélky, deodorant, čistič']]) +
          '<h2>Časté chyby</h2>'
          '<ul><li>Vložení silné vložky do těsné boty bez ověření prostoru.</li>'
          '<li>Použití nevhodné impregnace na membránu, která zhorší prodyšnost.</li>'
          '<li>Sušení mokrých bot na radiátoru.</li>'
          '<li>Pořizování ortopedické vložky na vlastní pěst při bolestech.</li>'
          '<li>Příliš dlouhé tkaničky, o které se při chůzi zakopává.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Najdete zde ' + B(('proma','Proma'),('svorto','Svorto'),('nikwax','Nikwax'),('vtr','VTR'),('oxford','Oxford'),('pedag','Pedag'),('toko','Toko'),('sidas','Sidas'),('collonil','Collonil'),('bauer','Bauer'),('footgel','Footgel'),('boot-doc','Boot Doc')) + '. Značky se specializují: některé na impregnace, jiné na vložky, další na brusle. Pro srovnání čtěte popis použití u konkrétního zboží, ne jen název.</p>'
          '<h2>Ponožky a další vrstva komfortu</h2>'
          '<p>Pohodlí uvnitř boty ovlivňují i ponožky. Funkční vlákna a merino odvádějí vlhkost a snižují třecí body. Příbuzné kategorie jsou <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/merino-ponozky/">merino ponožky</a>. Dobrá ponožka spolu s vložkou často vyřeší puchýře, které byste jinak připisovali samotné botě.</p>',
    faq=[
      ('Kdy vyměnit vložky v botách?', 'Když se pěna zmáčkne a nevrací do tvaru, když se objeví zápach, který nezmizí po vyprání, nebo když bota přestane dobře držet nohu. U sportovní obuvi to bývá dřív než u běžných bot. Orientační doba závisí na používání a hmotnosti.'),
      ('Jak vybrat správné tkaničky?', 'Změřte stávající tkaničku nebo spočítejte páry oček. Plochá drží uzel lépe, kulatá je hladší. Pro rychlé obouvání zvolte elastické nebo rychlošněrovací, za šera se hodí reflexní.'),
      ('Dá se impregnovat membránová obuv?', 'Ano, ale používejte prostředky určené pro membrány, které nezalepí póry. Čisté a suché boty ošetřete rovnoměrně z odstupu a nechte uschnout. Pokud se voda po povrchu přestane perlit, impregnaci obnovte.'),
      ('Jak čistit semišové boty?', 'Suchým kartáčem odstraňte prach a gumou skvrny. Mokrý postup zkoušejte opatrně, protože semiš tmavne a tuhne. Pak použijte sprej na semiš, který materiál zbytečně nezamastí.'),
      ('Pomůže vložka od bolesti nohou?', 'Vložka může zlepšit tlumení nebo oporu klenby, ale bolest může mít různé příčiny. Při dlouhodobých potížích navštivte lékaře nebo ortopeda a nespoléhejte jen na sériovou vložku.'),
      ('Jak se zbavit zápachu z bot?', 'Boty po použití vyvětrejte, vyndejte vložky a střídejte dva páry. Deodorant pomůže, ale nenahradí sušení. Vložky lze často vyprat, pokud to dovolí výrobce.'),
      ('Co obnáší ostření bruslí?', 'Ostrá hrana ostří je nutná pro záběr na ledě. Ostření provádí servis podle zvoleného profilu drážky. Po jízdě brusle otřete, ostří chraňte chrániči a nenoste je bez nich po tvrdém podkladu.'),
      ('Je lepší vosk, nebo sprej?', 'Vosk a krém jsou vhodné na hladkou kůži, kde ji vyživují a chrání. Sprej se hodí na textil, semiš a nubuk, kde vosk nechce zanechat mastné skvrny. U kombinovaných bot ošetřete každý materiál zvlášť.'),
      ('Jaké vložky do zimních bot?', 'Zateplené s vrstvou vlny nebo reflexní fólií pomáhají udržet teplo od země. Pozor na tloušťku, aby nebyla bota těsná, protože těsná obuv zhoršuje prokrvení a zima se dostane dovnitř rychleji.'),
      ('Kde porovnám nabídky?', 'Na stránce zboží uvidíte nabídky více obchodů vedle sebe, skladovost a dopravu. Doplňky jsou drobné, takže se vyplatí zkontrolovat poštovné a případně nakoupit víc kusů najednou.')])

# ------------------------------------------------------------------ rybarske-tasky
NEW['rybarske-tasky'] = dict(long=True,
    title='Rybářské tašky, pouzdra a krabičky | Sporteka',
    desc='Rybářské tašky, batohy, pouzdra na pruty, krabičky a boxy na nástrahy. Jak vybrat podle způsobu lovu a porovnat nabídky českých obchodů.',
    intro='<p>Dobře zvolené úložné vybavení šetří rybáři čas, nervy i peníze. Návazce se nezamotají, háčky nerezavějí na dně batohu a pruty vydrží přepravu bez poškození. V kategorii najdete <strong>rybářské tašky, batohy, pouzdra a obaly na pruty, krabičky na nástrahy a boxy</strong> a u každého zboží uvidíte nabídky českých obchodů vedle sebe.</p>'
          '<p>Tašky se liší podle způsobu lovu: kapraři potřebují velké kufry a přepravní tašky, přívlačáři lehké brašny a muškaři malé hrudní. Související výbavu najdete v kategoriích <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/rybarske-navijaky/">navijáky</a>, <a href="/vlasce-a-snury/">vlasce a šňůry</a>, <a href="/nastrahy-a-navnady/">nástrahy a návnady</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>.</p>',
    guide='<h2>Jaké druhy úložného vybavení existují</h2>'
          '<p>Společným jmenovatelem je ochrana vybavení před vodou, nárazy a zapomenutím. Typy se však liší velikostí, tuhostí a organizací vnitřku.</p>'
          + T(['Typ', 'Hlavní použití', 'Na co dát pozor'], [
              ['Pouzdro nebo obal na pruty', 'přeprava hotových sestav i rozložených prutů', 'délka, vycpání, počet přihrádek'],
              ['Přepravní taška na vybavení', 'celodenní lov, bivak, kaprařina', 'dno odolné vodě, pevné švy, rozměr'],
              ['Batoh', 'přívlač a pěší přesuny po břehu', 'nosný systém, přihrádky, odolnost vůči vodě'],
              ['Krabička na nástrahy', 'woblery, gumy, třpytky, háčky', 'těsné zavírání, přihrádky nastavitelné'],
              ['Box a kufřík', 'hrubé vybavení, drobnosti', 'zámky, tuhost, vodotěsnost'],
              ['Pouzdro na doplňky', 'nůžky, kleště, vyprošťovák', 'rychlý přístup, upevnění na opasek']]) +
          '<h2>Pouzdra a obaly na pruty</h2>'
          '<p>Nejčastější kus výbavy je pouzdro na pruty. Přepravuje více prutů najednou, často již se sestavenými navijáky, takže na břehu rychle lovíte. Zvolte délku podle nejdelšího prutu a dvoudílné modely, aby se vešly do auta. Tvrdé pouzdro nabízí lepší ochranu proti nárazu, měkké je lehčí a skladnější. U vícedílných pouzder zkontrolujte, zda jsou přihrádky vyztužené, aby se špičky nepoškodily. Zip a popruhy musí vydržet větší zatížení, protože se s nimi manipuluje v blátě.</p>'
          '<p>Špičky prutů jsou nejzranitelnější část. Dbejte, aby měly samostatnou ochranu nebo vycpání. Pro nákup prutů navštivte sekci <a href="/rybarske-pruty/">rybářské pruty</a> a pro kombinaci s navijáky <a href="/rybarske-navijaky/">rybářské navijáky</a>.</p>'
          '<h2>Tašky na vybavení pro kapraře</h2>'
          '<p>Kaprařina je disciplína, kde se vozí hodně věcí: podložka, váha, sak, signalizátory, návazce, nádobí. Přepravní taška na vybavení rozdělí obsah do oddílů a ochrání jej před vlhkem. Chladicí tašky udrží návnadu čerstvou v létě, vložky z termoizolace slouží i na nápoje. Na bivak se hodí tašky s pevným dnem, které nepromoknou, když je položíte na rosu. Pro delší pobyty navazují <a href="/bivaky-a-kresla/">bivaky a křesla</a> a <a href="/rybarske-spacaky/">rybářské spacáky</a>.</p>'
          '<h2>Batohy pro přívlač a pěší lov</h2>'
          '<p>Při přívlači se rybář pohybuje podél břehu, proto upřednostní batoh nebo brašnu, které neomezují pohyb. Hodí se hrudní popruh, který stabilizuje zátěž, a boční přihrádka na lahev. Praktické jsou panely pro krabičky, které se dají vyndat a použít i bez batohu. Pokud lovíte v dešti nebo při brodění, vyberte model s voděodolným materiálem a pláštěnkou na zip. Šaty a doplňky přívlačáře najdete v sekci <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>'
          '<h2>Krabičky na nástrahy a háčky</h2>'
          '<p>Krabička chrání nástrahy před poškozením a roztřídí je podle druhu. Wobler krabičky mají vyjímatelné přepážky, aby každý kus měl své místo, a háčky se tak nezachytí o sousední. Gumové nástrahy se neukládají k jiným materiálům, protože některé plasty se vzájemně rozpouštějí, takže měkké gumy patří do vlastního oddílu. Háčky a malé třpytky se ukládají do těsné krabičky s pěnovou vložkou, která drží háčky na místě; po lovu je nechte vyschnout. Pro naplnění krabiček se podívejte na kategorii <a href="/nastrahy-a-navnady/">nástrahy a návnady</a>.</p>'
          '<h2>Muškařské a mořské vybavení</h2>'
          '<p>Muškaři nosí malé hrudní tašky a krabičky s pěnovým povrchem, do kterého se zapichují umělé mušky. Tašky mají přihrádky na vyprošťovák, nůžky a vazelínu na šňůru. Pro tuto disciplínu najdete rozšířenou nabídku v sekci <a href="/muskareni/">muškaření</a>. Pro lov z lodi se používají větší nepromokavé tašky a boxy, které odolávají slané vodě a slunci. Sekce <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a> pokrývá doplňky pro vodu.</p>'
          '<h2>Materiály a zpracování</h2>'
          + T(['Materiál', 'Výhoda', 'Nevýhoda'], [
              ['Polyester s PU vrstvou', 'lehký, dobře odpuzuje vodu', 'otěr na hranách'],
              ['PVC plachtovina', 'velmi odolná vůči vodě', 'těžší a méně pružná'],
              ['EVA (tvrdá pěna)', 'tuhá, lehce omyvatelná', 'méně prostorná'],
              ['Nylon', 'pevný a lehký', 'bez impregnace propouští vlhko'],
              ['Neopren', 'tlumí nárazy', 'pomalu schne']]) +
          '<p>Rozhoduje kvalita zipů, švů a popruhů. Zip s velkým jezdcem se lépe ovládá v rukavicích. Dvojité šití u madel snižuje riziko utržení. Vodotěsnost zkontrolujte u popisu: voděodolný materiál odolá dešti, ale ne ponoření.</p>'
          '<h2>Vyberte podle způsobu lovu</h2>'
          + T(['Způsob lovu', 'Hlavní výbava'], [
              ['Kaprařina a bivak', 'velká přepravní taška, pouzdro na pruty, chladicí taška'],
              ['Přívlač', 'lehký batoh, krabičky na nástrahy, pouzdro na kleště'],
              ['Feeder a položená', 'organizér na krmítka a návazce, pouzdro na pruty'],
              ['Muškaření', 'hrudní taška, krabička na mušky'],
              ['Rodinný lov u rybníka', 'jedna středně velká taška a pár krabiček']]) +
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě příliš malé tašky, do které se po roce nevejde nová výbava.</li>'
          '<li>Opomenutí ochrany špiček prutů při přepravě v pouzdře.</li>'
          '<li>Společné uložení gumových nástrah s jinými plasty.</li>'
          '<li>Uložení vlhké výbavy do uzavřené tašky bez vysušení.</li>'
          '<li>Volba podle vzhledu místo podle zipů a švů.</li></ul>'
          '<h2>Péče a uložení</h2>'
          '<p>Po výpravě tašku vyprázdněte, vytřepte písek a nechte uschnout. Plesnivění způsobuje zápach a poškozuje vybavení. Zipy občas ošetřete silikonovým sprejem. Krabičky na háčky otevřete a nechte vyschnout, aby nekorodovaly. Pouzdro na pruty skladujte vodorovně nebo ve svislé poloze s oporou, aby se špičky neohýbaly.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>Nabídka zahrnuje ' + B(('mikado','Mikado'),('fox','Fox'),('westin','Westin'),('korda','Korda'),('zfish','Zfish'),('delphin','Delphin'),('mivardi','Mivardi'),('versus','Versus'),('meiho','Meiho'),('suretti','Suretti'),('wychwood','Wychwood'),('daiwa','Daiwa')) + '. Meiho je známé pevnými boxy, Fox a Korda se zaměřují na kapraře a Wychwood na muškaře. Výběr se opírá o popis použití, ne jen o značku.</p>'
          '<h2>Nakupujte na Sportece</h2>'
          '<p>U každého zboží porovnáte obchody podle skladovosti, dopravy a doby dodání. Rozměrné pouzdro na pruty se někdy posílá jako nadměrný balík, což mění celkovou cenu zásilky. Sladit lze i ostatní nákup, například <a href="/bivaky-a-kresla/">bivaky a křesla</a> nebo <a href="/rybareni/">rybářské vybavení</a> pohromadě.</p>',
    faq=[
      ('Jakou tašku vybrat pro kaprařinu?', 'Velkou přepravní tašku s pevným dnem, oddíly a odolným zipem, spolu s pouzdrem na pruty a chladicí taškou na návnady. Rozměr volte podle počtu věcí, které vozíte na jedno sezení. Příliš malá taška vás bude nutit nosit vybavení ve více kusech.'),
      ('Jak vybrat pouzdro na pruty?', 'Podle délky nejdelšího prutu v transportní velikosti a počtu prutů, které vozíte. Vyztužené oddíly chrání špičky, tuhé pouzdro lépe odolává nárazům. Pokud vozíte pruty se sestavenými navijáky, zkontrolujte šířku přihrádek.'),
      ('Čím se liší batoh od tašky pro přívlač?', 'Batoh se nosí na zádech a nechává ruce volné, což je výhodné při pěším přesunu podél břehu. Taška se většinou nosí přes rameno nebo v ruce a hodí se na kratší vzdálenosti. Batoh má obvykle lepší rozložení váhy.'),
      ('Kde uložit gumové nástrahy?', 'Do samostatného oddílu nebo vlastní krabičky. Některé měkké plasty se při dlouhém kontaktu rozpouštějí a slepují s tvrdými nástrahami, proto je neukládejte společně. Gumy ze zimního uložení před použitím prohlédněte.'),
      ('Jak zabránit korozi háčků?', 'Po lovu háčky a třpytky nechte vyschnout v otevřené krabičce, teprve pak ji zavřete. Pěnová vložka nasává vlhkost, proto ji občas vyměňte. Těsná krabička s ventilací je lepší než dokonale uzavřená.'),
      ('Je voděodolná taška totéž co vodotěsná?', 'Ne. Voděodolný materiál odolá dešti a stříkající vodě, vodotěsný se svařovanými švy snese i krátké ponoření. Pro lov z lodi nebo při brodění zvolte vodotěsnější provedení a sledujte popis výrobce.'),
      ('Dá se taška prát?', 'Nejlépe ji vymýt vlažnou vodou s jemným mýdlem a nechat uschnout. Pračka a vysoká teplota mohou poškodit impregnaci a lepené spoje. Před uschováním vždy vysušte i vnitřní přihrádky.'),
      ('Jaká výbava patří do tašky muškaře?', 'Krabičky s mouchami, vyprošťovák, nůžky, vazelína na šňůru, předvazce a náhradní návazce. Hodí se malá hrudní taška nebo vesta, která drží věci v dosahu. Jednotlivé kusy záleží na vodě a způsobu lovu.'),
      ('Na co se zaměřit u zipů a švů?', 'Zip by měl mít velký jezdec, který se ovládá v rukavicích, a krytí proti dešti. Švy u madel a popruhů mají být zesílené dvojitým šitím. Mnoho tašek selže právě v těchto místech, ne v látce.'),
      ('Kde porovnám nabídky tašek a krabiček?', 'Na stránce konkrétního zboží uvidíte nabídky více obchodů, skladovost a dopravu. U objemných pouzder dávejte pozor na poštovné, které se může lišit.')])


# ------------------------------------------------------------------ extensions (appended sections)
NEW['funkcni-trenink']['intro'] += '<p>Většina vybavení se po cvičení uklidí, takže se hodí i tam, kde žádná posilovna nevznikne.</p>'
NEW['funkcni-trenink']['guide'] += (
    '<h2>Jak sestavit první týden tréninku</h2>'
    '<p>Rozumný plán nepotřebuje desítky cviků. Základ tvoří pět pohybových vzorů: tah, tlak, dřep, předklon a nošení nebo rotace. Pro tah poslouží hrazda nebo závěsné popruhy, pro tlak kliky na bradlech či na zemi, pro dřep medicinbal držený u hrudi, pro předklon sandbag a pro rotace hod slam ballem. Každý vzor stačí zařadit dvakrát týdně v krátkých sériích a mezi sérií odpočívat dost dlouho na to, abyste udrželi techniku.</p>'
    '<p>Kruhový trénink zkracuje čas, ale nesmí z něj vzniknout hon za počtem opakování. Lepší je zvolit čtyři až šest stanovišť, na každém zůstat třicet až čtyřicet sekund a mezi koly si dopřát pauzu. Intenzitu měňte postupně a zapisujte si ji, protože právě záznam ukáže pokrok líp než pocit. Pokud bolest po cvičení trvá několik dní, ubrat objem je rozumnější než zatnout zuby.</p>'
    '<h2>Progrese bez kupování nového vybavení</h2>'
    '<p>Jedna pomůcka vydrží roky, pokud umíte měnit obtížnost. U hrazdy začněte negativními shyby, tedy pomalým spouštěním z horní polohy, pokračujte shyby s pomocí gumy a teprve potom plnými opakováními. U kliků na bradlech se zvětšuje rozsah pohybu, zpomaluje sestup nebo přidává pauza dole. U závěsných popruhů stačí přisunout nohy blíž ke kotvě a cvik je těžší. U medicinbalu se mění vzdálenost hodu, rychlost i druh pohybu.</p>'
    '<p>Takto vystavěný trénink nevyžaduje stálé přikupování, a proto je vhodné pořídit si méně kusů, ale kvalitnějších. Doplňující výbavu na posílení izolovaných svalů najdete v sekci <a href="/cinky-a-kotouce/">činky a kotouče</a>, kdežto <a href="/posilovaci-stroje/">posilovací stroje</a> řeší cílenou práci na jednu partii.</p>'
    '<h2>Rozcvička a navazující protažení</h2>'
    '<p>Před výbušnými cviky se tělo rozehřeje kroužením v kloubech, lehkým skákáním a několika pomalými opakováními stejného cviku s nižší zátěží. Ramena, zápěstí a kyčle potřebují zvláštní pozornost, protože při visech a výskocích nesou největší zátěž. Po tréninku pomůže klidné protažení a případně práce s <a href="/masazni-pomucky/">masážními pomůckami</a>. Delší pauzu zařaďte, jakmile se objeví netypická bolest.</p>'
    '<h2>Kam dál</h2>'
    '<p>Pokud vás baví spíš výdrž než síla, přejděte ke strojům v <a href="/kardio-trenazery/">kardio trenažérech</a>. Chcete-li vybavit celý domácí prostor, začněte přehledem <a href="/fitness/">fitness</a>.</p>')

NEW['kardio-trenazery']['intro'] += '<p>Ať vyberete cokoli, nejdůležitější je pohodlí a pravidelnost.</p>'
NEW['kardio-trenazery']['guide'] += (
    '<h2>Jak nastavit stroj, aby sedl vašemu tělu</h2>'
    '<p>Špatně nastavený stroj zhorší pohodlí rychleji než slabý motor. U rotopedu nastavte výšku sedla tak, aby se při spodní poloze pedálu koleno mírně neukládalo do úplného napřímení. Řídítka mají být v takové výšce, aby záda zůstala přirozeně zakřivená a ramena uvolněná. U veslovacího stroje upravte popruhy na chodidla tak, aby pata mohla jemně zvedat. U eliptiku se dívejte dopředu a nedržte se madel křečovitě, jinak se vyhýbáte práci svalů trupu.</p>'
    '<h2>Intervaly, vytrvalost nebo chůze</h2>'
    '<p>Kardio stroj podporuje více stylů tréninku. Dlouhé klidné sezení rozvíjí vytrvalost a hodí se při návratu k pohybu. Intervaly střídají krátký vyšší odpor s regenerací a jsou kratší, ale náročnější. Chůze do kopce na pásu zatíží stehna a hýždě a mnohým lidem vyhovuje víc než běh. Žádný styl není nadřazený; záleží na cíli, kondici a zdravotním stavu. Před náročnější zátěží se doporučuje konzultace s lékařem.</p>'
    '<h2>Doplňky ke kardio strojům</h2>'
    '<p>Praktické jsou podložka pod stroj, držák na tablet nebo telefon, ručník a láhev na pití. Hrudní pás pro měření tepu bývá přesnější než dotykové snímače. U rotopedu se hodí pohodlnější sedlo nebo gelový potah a pedály s třmeny. Oblečení vybírejte lehké a prodyšné z kategorie <a href="/sportovni-tricka/">sportovní trička</a> a <a href="/sportovni-kratasy/">sportovní kraťasy</a>, obuv pro pás nebo rotoped z kategorie <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
    '<h2>Kam stroj postavit</h2>'
    '<p>Rovná podlaha, odstup od zdí a pevný podklad jsou základ. Na koberci se stroj může bortit a naklánět, proto pod něj patří tvrdá podložka. Dávejte pozor na zásuvku, pokud stroj potřebuje elektřinu, a nikdy nepoužívejte přetížené prodlužovačky. Místnost by měla být větratelná, protože při vytrvalostním tréninku se rychle oteplí. Přemístění těžkého stroje zjednoduší transportní kolečka, která většina pásů a eliptiků má.</p>'
    '<h2>Kdy vyměnit nebo opravit</h2>'
    '<p>Pokud stroj skřípe, drhne nebo se zasekává, zkontrolujte nejprve šrouby a mazání. Zvuk z ložisek se často po promazání uklidní. Odpor, který se neřídí tlačítky, i vypadávání displeje bývají důvodem k reklamaci v záruce, proto si uschovejte doklad o nákupu. Opravy jsou u levnějších strojů někdy dražší než nový kus, a tak se vyplatí zvážit i náhradu za kvalitnější model.</p>')

NEW['doplnky-k-obuvi']['intro'] += '<p>Většinu z toho vyřešíte za malou část ceny nových bot.</p>'
NEW['doplnky-k-obuvi']['guide'] += (
    '<h2>Jak změřit a zvolit velikost vložky</h2>'
    '<p>Vložky se prodávají buď v číselných velikostech, nebo ve stříhatelné podobě. Číselné odpovídají velikosti boty, ale rozdíly mezi výrobci jsou zřejmé, takže vložku vždy porovnejte s originální stélkou. Stříhatelné se přiloží k vyjmuté stélce, obtáhne se obrys a opatrně se ořízne o něco větší, protože větší vložku lze dále zkrátit, menší už ne. Po vložení zkontrolujte, zda se vložka nezvedá ve špičce nebo u paty. Pokud bota po přidání vložky tlačí na nárt, zvolte tenčí variantu.</p>'
    '<h2>Doplňky pro konkrétní problémy</h2>'
    + T(['Problém', 'Co zkusit'], [
        ['Bota drhne patu', 'samolepicí gelová podložka, ponožka bez silných švů'],
        ['Bota je o půl čísla větší', 'tenká vložka nebo podložka do špičky'],
        ['Tkanička se rozvazuje', 'dvojitý uzel, plochá tkanička s hrubším povrchem'],
        ['Jazyk bota uhýbá', 'tkanička provlečená ušicí na jazyku'],
        ['Mokrá obuv nechce schnout', 'vyndat stélku, vycpat papírem, sušit při pokojové teplotě'],
        ['Rychle se otírá podrážka', 'opravná vrstva nebo kontrola došlapu u odborníka']]) +
    '<p>Žádný doplněk nenahradí správnou velikost. Pokud je bota zásadně malá, nepomůže vložka ani tkaničky. V takovém případě vyberte jiný pár v kategoriích <a href="/tenisky/">tenisky</a>, <a href="/treninkova-obuv/">tréninková obuv</a> nebo <a href="/barefoot-obuv/">barefoot obuv</a>.</p>'
    '<h2>Děti a rychlý růst</h2>'
    '<p>Dětská noha roste rychle a vložky se mění častěji než u dospělých. Na dětské botě se hodí elastické tkaničky, které děti ovládnou samy, a jednoduché vložky bez zbytečné tuhé podpory. U potíží s držením nohy nebo chůzí je lepší vyhledat lékaře, ne experimentovat se sériovými pomůckami.</p>'
    '<h2>Sezónní údržba bot</h2>'
    '<p>Před sezónou zkontrolujte tkaničky, stav stélek a podrážek a obnovte impregnaci. Na konci sezóny boty vyčistěte, vysušte a uložte na vzdušné místo, ne do plastového pytle. Kožené boty před uložením ošetřete krémem, textilní vyperte podle pokynů výrobce. Zimní boty si zaslouží omytí od soli, která kůži vysušuje a bělá. Při dlouhodobém skladování vložte do boty papír nebo napínač, který udrží tvar.</p>')

NEW['rybarske-tasky']['intro'] += '<p>Dobrá taška snese blato, déšť i každodenní přepravu v autě.</p>'
NEW['rybarske-tasky']['guide'] += (
    '<h2>Jak zorganizovat vybavení uvnitř tašky</h2>'
    '<p>Praktické pravidlo zní: co potřebujete často, patří nahoru a ven, co jen občas, patří dolů. Do vnější kapsy dejte nůžky, kleště, vyprošťovák a hadřík na ruce. Střední oddíl využijte pro krabičky, které označte podle obsahu. Dno si nechte pro těžší věci, jako jsou olůvka, váha nebo nádobí. Návazce ukládejte na cívky nebo do speciálních pouzder, aby se nezamotaly. Při každém lovu si zapište, co jste použili, a doplňte zásoby ještě před další výpravou.</p>'
    '<h2>Bezpečnost a ohleduplnost k přírodě</h2>'
    '<p>Ostré háčky patří do uzavřené krabičky, ne volně do kapsy. Použité vlasce, ostré konce a obaly nenechávejte u vody, protože ohrožují zvířata. Praktická je malá odpadková kapsa na tašce, která zajistí, že po sobě nic nezůstane. Těžší tašky nenoste přes jedno rameno po dlouhé vzdálenosti, jinak se zbytečně zatěžují záda.</p>'
    '<h2>Doprava a uložení v autě</h2>'
    '<p>Pouzdra na pruty ukládejte rovně a zabezpečte je proti sklouznutí při brzdění. Těžké tašky patří dolů a blíže středu vozu, lehčí nahoru. Mokré vybavení vozte odděleně od suchého v nepromokavém pytli nebo boxu, aby se voda nedostala k návnadám a oblečení. Na kolo nebo na krátké výlety po břehu se hodí skládací vozíky nebo batohy, které nosíte na zádech.</p>'
    '<h2>Kolik tašek je dost</h2>'
    '<p>Většině rybářů stačí tři věci: pouzdro na pruty, jedna prostorná taška na vybavení a krabičky na drobnosti. Další tašky přidávejte, až poznáte, co vám chybí. Lidé, kteří loví několika způsoby, ocení jednu univerzální sestavu s přihrádkami, kterou přizpůsobí podle cíle. Pokud do výbavy patří i křeslo, bivak nebo chladicí box, počítejte s vozíkem. Ostatní kategorie, které na tašky navazují, jsou <a href="/outdoor-doplnky/">outdoor doplňky</a>, <a href="/batohy/">batohy</a> a <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>')

NEW['kardio-trenazery']['intro'] += '<p>Před nákupem si změřte volné místo v bytě a zjistěte maximální uživatelskou hmotnost stroje.</p>'
NEW['rybarske-tasky']['guide'] += '<p>Před každou sezónou prohlédněte všechny zipy, popruhy a přezky a vadné kusy včas vyměňte, aby vás nezaskočily na břehu.</p>'

NEW['doplnky-k-obuvi']['guide'] += (
    '<h2>Jak nakupovat doplňky chytře</h2>'
    '<p>U drobného zboží rozhodují detaily, které se z názvu nepoznají. Přečtěte si, pro jaký typ boty je vložka určená, zda je impregnace vhodná pro membránu a zda tkaničky odpovídají délce, kterou potřebujete. Doplňky se často prodávají v balení po jednom páru, jindy po více kusech, proto si ověřte počet. Při větším nákupu se vyplatí sloučit objednávku v jednom obchodě, protože poštovné se tak nezaplatí vícekrát. Zásoba několika párů náhradních tkaniček a jedné impregnace pokryje většinu situací během sezóny a ušetří cestu do obchodu těsně před výletem, závodem nebo prvním sněhem.</p>')
NEW['rybarske-tasky']['guide'] += (
    '<h2>Na co myslet před koupí</h2>'
    '<p>Nejprve si spočítejte, co chcete vozit, a teprve potom hledejte tašku. Rozložte vybavení na podlahu, odhadněte objem a přidejte rezervu pro nové kusy. Změřte nejdelší položku, obvykle pruty, a zkontrolujte, zda se vejde do kufru auta nebo na kolo. Dále zvažte, jak daleko budete věci nosit: na vzdálenost několika metrů k autu stačí jakákoli taška, ale při pochodu podél řeky záleží na nosném systému a hmotnosti prázdné tašky. Z popisu zboží vyčtěte materiál, počet přihrádek a rozměry a porovnejte je u více obchodů.</p>')
