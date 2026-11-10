"""sporteka.cz — wave 23f (4. 11. 2026): long texts (>= 1650 words) for mestske-cyklohelmy, hazena, trekingova-a-mestska-elektrokola, lukostrelba.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ mestske-cyklohelmy
NEW['mestske-cyklohelmy'] = dict(long=True,
    title='Městské cyklohelmy: dojíždění, světlo, velikost, péče',
    desc='Městské cyklohelmy na dojíždění i volné jízdy. Jak vybrat velikost, větrání, zadní světlo a zapínání a porovnat nabídky českých obchodů.',
    intro='<p>Městská cyklistická helma je určená pro každodenní jízdu po silnici, cyklostezce a v dopravní zácpě, kde se jezdí klidněji než na závodním kole. Od silniční přilby se liší hlubším týlem, odolnější skořepinou a často i integrovaným zadním světlem nebo odrazkou. Sporteka porovnává nabídky českých obchodů u helem pro dospělé, a to na klasických kolech i na elektrokolech.</p>'
          '<p>V nabídce převažují značky ' + B(('abus', 'Abus'), ('alpina', 'Alpina'), ('uvex', 'Uvex'), ('urge', 'Urge'), ('prophete', 'Prophete'), ('lazer', 'Lazer'), ('kask', 'Kask')) +
          '. Širší přehled najdete v nadřazené kategorii <a href="/cyklisticke-helmy/">cyklistické helmy</a>, kde jsou i <a href="/silnicni-cyklohelmy/">silniční</a> a <a href="/mtb-a-integralni-helmy/">MTB helmy</a>.</p>',
    guide='<h2>Čím se městská helma liší od ostatních</h2>'
          '<p>Silniční přilba maximalizuje větrání a nízkou hmotnost, horská počítá s kšiltem a pádem v terénu. Městský model řeší jiný problém: musí vydržet každodenní manipulaci, pověšení na řídítka, odložení do tašky a pobyt v dešti. Proto má pevnější vnější skořepinu, méně průduchů a často tlumenější vzhled, který se nebije s oblekem ani s bundou.</p>'
          + T(['Vlastnost', 'Městská helma', 'Silniční helma'], [
              ['Skořepina', 'pevnější, odolná proti škrábancům', 'tenká, lehká, více otvorů'],
              ['Větrání', 'střední, kompromis pro chladnější dny', 'maximální, kvůli vysoké zátěži'],
              ['Příslušenství', 'světlo, odrazky, někdy vizor', 'zpravidla jen síťka proti hmyzu'],
              ['Vzhled', 'nenápadný, jednobarevný nebo matný', 'sportovní, výrazné barvy'],
              ['Hmotnost', 'o něco vyšší', 'co nejnižší']]) +
          '<p>Nejde o dvě oddělené bezpečnostní třídy. Cílem obou je tlumit náraz hlavy do tvrdé překážky, rozdíl je v pohodlí a ve vybavení pro konkrétní styl jízdy.</p>'
          '<h2>Typy městských helem</h2>'
          '<ul><li><strong>Klasická městská přilba:</strong> kulatý tvar, uzavřenější skořepina, několik větracích otvorů. Základ pro dojíždění.</li>'
          '<li><strong>Helma s LED světlem vzadu:</strong> dobíjecí nebo bateriové světlo je zasazené do skořepiny a zvyšuje viditelnost za šera. Modely značek Abus Urban-I nebo Uvex City I-Vo patří k typickým.</li>'
          '<li><strong>Helma pro elektrokola:</strong> protažený týl a zesílená skořepina pro vyšší rychlosti. Hodí se k běžným <a href="/elektrokola/">elektrokolům</a> s asistencí do 25 km/h; rychlé modely (speed pedelec) vyžadují helmu s certifikací NTA 8776.</li>'
          '<li><strong>Helma ve skate stylu:</strong> hlubší a oblejší tvar, vhodná pro rekreační jízdu, kolobežky a občasné triky.</li>'
          '<li><strong>Helma s vizorem nebo kšiltem:</strong> chrání oči před sluncem a drobným deštěm, ale může omezit výhled při předklonu.</li></ul>'
          '<h2>Správná velikost a nastavení</h2>'
          '<p>Velikost se určuje obvodem hlavy měřeným pásmem těsně nad obočím a ušima. Výrobce uvádí rozsah v centimetrech, například 52 až 58 nebo 56 až 61, a v něm helmu doladíte kolečkem v týlu. Při vybírání nepodléhejte iluzi, že vyšší rozsah je pohodlnější. Hlava musí uvnitř přiléhat bez tlaku a helma se při zatřesení nesmí kývat.</p>'
          '<ol><li>Nasaďte helmu rovně, přední hrana je zhruba dva prsty nad obočím.</li>'
          '<li>Seřiďte popruhy tak, aby se pod ušima sbíhaly do písmene V.</li>'
          '<li>Zapněte spínací přezku a utáhněte popruh pod bradou tak, aby se vešel jen jeden prst.</li>'
          '<li>Otočte kolečko v týlu, dokud nesedí pevně, ale bez bolesti.</li>'
          '<li>Zavrťte hlavou a zkuste helmu posunout prstem dopředu a dozadu. Nemá se pohnout o víc než o centimetr.</li></ol>'
          '<p>Vlasy a zimní čepice mění potřebnou velikost. Dlouhé vlasy se vejdou lépe do modelu s otevřeným týlem, pro zimu hledejte helmu s prostorem na tenkou čepici pod ní, nikdy ne na tlustou pletenou.</p>'
          '<h2>Bezpečnostní technologie, kterých si všimnout</h2>'
          '<p>Základní konstrukcí je tvrdá vnější skořepina nalepená na expandovaný polystyren, který se při nárazu rozdrtí a pohltí energii. Moderní helmy přidávají další prvky, které se objevují i v katalogu městských modelů:</p>'
          + T(['Prvek', 'K čemu slouží', 'Poznámka'], [
              ['Klouzavá vrstva (typ MIPS)', 'snižuje rotační síly při šikmém nárazu', 'u některých modelů Abus a Uvex označená jinak, ale princip je podobný'],
              ['In-mold skořepina', 'vnější plast je spojený s pěnou při lisování', 'lehčí a pevnější než slepené díly'],
              ['Kolečko v týlu', 'jemné nastavení obvodu', 'lépe dolaďuje než pevné pásky'],
              ['Odrazky a světlo', 'viditelnost za šera', 'viz sekce o bezpečném dojíždění'],
              ['Magnetická přezka', 'rychlé zapínání jednou rukou', 'ověřte zámek, aby se sám neotevřel']]) +
          '<p>Žádná technologie nenahradí správné nasazení. Helma posunutá do týlu neochrání čelo, uvolněný popruh nezabrání jejímu sesmeknutí.</p>'
          '<h2>Viditelnost a světla pro městský provoz</h2>'
          '<p>Dobrá viditelnost snižuje riziko, že vás řidič přehlédne. Reflexní prvky a zadní světlo na helmě pracují ve výšce očí řidičů, což je výhoda proti světlu připevněnému nízko na sedlovce. Helmové světlo však nenahrazuje povinné vybavení kola. Dobrý základ tvoří <a href="/cyklo-svetla/">cyklistická světla</a> na řídítkách i sedlovce a odrazky na pedálech a v paprscích.</p>'
          '<p>U modelů s dobíjecí baterií zkontrolujte typ nabíjení. Standardní mikro USB nebo USB-C se hledá snadno, speciální dokovací kontakt se při ztrátě kabelu shání obtížně. Světlo si nabíjejte pravidelně, ideálně týdně při každodenním dojíždění.</p>'
          '<h2>Kam s ní v zimě a v dešti</h2>'
          '<p>Ve vlhkém počasí pomáhá helma s menšími otvory a s pevnějším týlem. V zimě se mnoho jezdců neobejde bez tenké čepice pod helmu a krytu helmy proti dešti a větru. Kombinace <a href="/cyklisticke-rukavice/">cyklistických rukavic</a> s <a href="/cyklisticke-bundy-a-vesty/">bundou nebo vestou</a> doplní výbavu, aby vás jízda neunavila zbytečně. Při proměnlivém počasí se hodí i <a href="/cyklisticke-navleky/">návleky na nohy</a>.</p>'
          '<h2>Péče a životnost helmy</h2>'
          '<ul><li><strong>Čištění:</strong> vlažná voda a jemné mýdlo, bez rozpouštědel, která polystyren poškozují.</li>'
          '<li><strong>Sušení:</strong> volně na vzduchu, ne na topení ani v autě za oknem. Teplo mění vlastnosti pěny.</li>'
          '<li><strong>Skladování:</strong> mimo přímé slunce a mimo hlučné tašky s ostrými předměty.</li>'
          '<li><strong>Po pádu:</strong> helmu vyměňte, pokud narazila hlavou nebo jí cokoli viditelně praskla. Poškození pěny zvenčí často není vidět.</li>'
          '<li><strong>Stárnutí:</strong> po několika letech provozu pěna a plast stárnou. Výrobce zpravidla doporučuje helmu vyměnit po určité době, uvedené v návodu.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<p>První chybou je výběr podle vzhledu bez zkoušení velikosti. Druhou je koupě staršího modelu bez zkontrolování data výroby, třetí zapomenuté nastavení po přechodu na zimní čepici. Další pokušení: helma je příliš velká, protože se hodí i pro partnera. Sdílená přilba neposkytuje ochranu ani jednomu z vás.</p>'
          '<p>Dobré je také nedoplňovat do helmy cizí součásti. Zadní světlo, které výrobce nezamýšlel, může změnit rozložení nárazu. Chcete-li svítit víc, přidejte světlo na tašku nebo zádový batoh, například z kategorie <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>'
          '<h2>Pro koho se městská helma hodí</h2>'
          + T(['Uživatel', 'Co hledat', 'Doplňky'], [
              ['Dojíždějící do práce', 'světlo, nenápadný vzhled, rychlé nastavení', 'brašna, <a href="/cyklo-zamky/">zámek</a>, zvonek'],
              ['Uživatelé elektrokol', 'pevný týl a delší skořepina', '<a href="/trekingova-a-mestska-elektrokola/">městské a trekingové e-kolo</a>'],
              ['Studenti a jezdci na sdílených kolech', 'skládací nebo lehká helma na přenášení', 'batoh, ochrana proti dešti'],
              ['Rekreační jezdci na cyklostezkách', 'větrání a pohodlí na delší vyjížďky', 'láhev, <a href="/cyklisticke-bryle/">brýle</a>'],
              ['Rodiče s dětskou sedačkou', 'vlastní helma pro dospělého a samostatná dětská', '<a href="/detske-cyklohelmy/">dětské cyklohelmy</a>, <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>']]) +
          '<h2>Jak porovnat nabídky na Sportece</h2>'
          '<p>Při porovnávání pracujte s konkrétním modelem a jeho barvou. Stejná helma se liší podle velikosti, barvy a roku výroby, proto je dobré porovnat celý název produktu. Sledujte dostupnost vybrané velikosti, poštovné a lhůtu pro výměnu, protože u helmy je zkouška doma často nutná. Hledáte-li kompletní městskou výbavu, pomůže kategorie <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>, <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a> a <a href="/mestska-kola/">městská kola</a>.</p>',
    faq=[
      ('Musím nosit helmu v městském provozu?', 'Platné povinnosti se liší podle věku a státu. V České republice se helma u dětí do určitého věku vyžaduje, u dospělých se doporučuje. Z hlediska bezpečnosti ale platí totéž pro obě skupiny: helma snižuje riziko poranění hlavy při pádu.'),
      ('Jak poznám, že mi městská helma padne?', 'Nasazená helma sedí rovně, přední hrana je dva prsty nad obočím, popruhy se sbíhají pod ušima a pod bradou se vejde jeden prst. Zakývání hlavou nesmí helmu posunout o víc než o centimetr.'),
      ('Je městská helma bezpečnější než silniční?', 'Neplatí to jako pravidlo. Obě mají stejný účel, tlumit náraz, ale městská je přizpůsobená denní jízdě a odolnosti, silniční nízké hmotnosti a větrání. Důležitější než typ je velikost, nasazení a stav helmy.'),
      ('K čemu je světlo na helmě?', 'Zvyšuje viditelnost za šera a v dešti, protože svítí ve výšce očí řidičů. Nenahrazuje povinné světlo na kole, ale doplňuje ho. Pravidelně kontrolujte baterii.'),
      ('Co znamená systém MIPS nebo podobný?', 'Jde o vrstvu, která umožňuje malý pohyb skořepiny vůči hlavě při šikmém nárazu a tím snižuje rotační zatížení. Je to doplňková technologie a nenahrazuje správné nasazení.'),
      ('Jak často helmu měnit?', 'Po pádu, při kterém narazila, a po uplynutí doby, kterou doporučuje výrobce v návodu. Pokud je viditelně poškozená, rozbitá, má uvolněné popruhy nebo zdeformovanou pěnu, vyměňte ji ihned.'),
      ('Hodí se městská helma pro elektrokolo?', 'Ano, pokud jezdíte běžnou rychlostí asistence. Jezdíte-li rychleji než 25 km/h, vyberte helmu určenou pro rychlá e-kola.'),
      ('Jak helmu v zimě nosit?', 'Pod helmu patří tenká čepice nebo bandana z funkčního materiálu. Silná pletená čepice zmenšuje prostor a helma sedí jinak. Při chladu pomůže i kryt na helmu nebo pláštěnka proti větru.'),
      ('Lze helmu vyprat nebo vyčistit rozpouštědlem?', 'Čistěte ji vlažnou vodou a jemným mýdlem, vnitřní polstrování se dá vyjmout a vyprat. Rozpouštědla, benzín ani agresivní čističe nepoužívejte, protože poškozují pěnu i plast.'),
      ('Může helmu nosit víc členů rodiny?', 'Není to dobrý nápad. Každá hlava má jiný obvod a helma se časem přizpůsobí jedné osobě. Pro děti je nutné vybírat samostatnou velikost, viz <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.')])

# ------------------------------------------------------------------ hazena
NEW['hazena'] = dict(long=True,
    title='Házená: míče, obuv, dresy, branky a doplňky pro hráče',
    desc='Házenkářské míče, obuv, dresy, chrániče, pryskyřice a branky. Jak vybrat velikost míče a obuv do haly a porovnat nabídky českých obchodů.',
    intro='<p>Házená je kontaktní halový sport, který se hraje i venku jako plážová házená, a rozhodují v ní míč s dobrým úchopem, obuv se spolehlivou přilnavostí a oblečení, které nebrání pohybu. Sporteka sbírá nabídky českých obchodů na házenkářské míče všech velikostí, halovou obuv, dresy, kraťasy, brankářské vybavení, branky a tréninkové pomůcky, aby se daly srovnat na jednom místě.</p>'
          '<p>V nabídce jsou značky ' + B(('select', 'Select'), ('kipsta', 'Kipsta'), ('hummel', 'Hummel'), ('powershot', 'Powershot'), ('puma', 'Puma'), ('molten', 'Molten'), ('kempa', 'Kempa')) +
          '. Kategorie spadá pod <a href="/micove-sporty/">míčové a raketové sporty</a> a sousedí s <a href="/florbal/">florbalem</a>, <a href="/volejbal/">volejbalem</a> a <a href="/basketbal/">basketbalem</a>.</p>',
    guide='<h2>Co všechno k házené patří</h2>'
          '<p>Základem je míč a halová obuv, ale pro pravidelný trénink se hodí i další věci. Hráči oceňují kolenní chrániče a neoprenové návleky, brankáři speciální výstroj, týmy sítě, branky a brašny na míče. Na rozdíl od jiných míčových sportů se v házené používá pryskyřice na prsty, která zlepšuje úchop, a proto se v nabídce objevuje i tato specialita.</p>'
          + T(['Skupina zboží', 'Co obsahuje', 'Komu je určena'], [
              ['Házenkářské míče', 'velikosti 0 až 3, tréninkové, zápasové, replika', 'děti, ženy, muži, kluby'],
              ['Halová obuv', 'tenisky s gumovou podešví pro házenou a halové sporty', 'hráči a hráčky v hale'],
              ['Dresy a kraťasy', 'dětské, dámské a pánské sady', 'týmy a jednotlivci'],
              ['Chrániče a návleky', 'kolenní chrániče, neoprenové návleky, výztuhy', 'hráči s pohybovými potížemi i prevence'],
              ['Pryskyřice', 'lepivá pasta na prsty, někdy v balení pro tým', 'pokročilí hráči a kluby'],
              ['Branky a sítě', 'hliníkové branky, redukce velikosti, tréninkové sítě', 'kluby, školy, domácí trénink'],
              ['Tašky a doplňky', 'pytle na míče, tréninkové pomůcky', 'trenéři a organizátoři']]) +
          '<h2>Velikost házenkářského míče</h2>'
          '<p>Míč se vybírá podle věku a kategorie. Nejmenší míč číslo 0 slouží minikategoriím, číslo 1 je obvyklý pro mladší děti a starší žákyně, číslo 2 pro ženy a starší žáky, číslo 3 je největší a je zápasovým míčem mužských kategorií. Přesný obvod a hmotnost uvádí výrobce u každého modelu. Použití míče, který je pro dítě příliš velký, zhoršuje techniku hodu a zvyšuje riziko přetížení ramene.</p>'
          '<ul><li><strong>Číslo 0:</strong> mini míč pro nejmladší hráče a první seznámení s hrou.</li>'
          '<li><strong>Číslo 1:</strong> dětská a mládežnická kategorie, například míče Hummel Classic Bounce.</li>'
          '<li><strong>Číslo 2:</strong> ženy, dorostenky a starší žáci. Většina klubů ho používá při tréninku.</li>'
          '<li><strong>Číslo 3:</strong> muži a nejstarší věkové kategorie.</li></ul>'
          '<p>Při nákupu pro školní tělocvik se vyplatí ptát učitele, který míč je pro dané ročníky předepsaný, a při tréninku v klubu respektovat požadavky soutěže. Na stejném principu se vybírají míče pro <a href="/fotbalove-mice/">fotbal</a> nebo <a href="/volejbalove-mice/">volejbal</a>.</p>'
          '<h2>Pryskyřice, wax a bezpryskyřicové míče</h2>'
          '<p>Tradiční házenkářský míč se hraje s pryskyřicí. Hráč si lepivou hmotu nanese na prsty a míč se mu snáze drží i při rychlém přihrávání. Nevýhodou je, že pryskyřice zůstává na míči, na podlaze i na oblečení a hala ji nemusí povolit. Proto se objevily míče označené jako „wax free“, které mají speciální povrch a pryskyřici nevyžadují.</p>'
          '<p>Před nákupem zjistěte, co povoluje hala, kde trénujete. Mnohé tělocvičny pryskyřici nedovolují a trénink s ní by vás vyloučil z pronájmu. Na pryskyřici se používají odstraňovače, tekuté čističe, nebo se čistí hala po zápase mopem. Míče bez pryskyřice dnes využívá i řada škol a amatérských týmů.</p>'
          '<h2>Typy míčů podle použití</h2>'
          + T(['Typ', 'Vlastnosti', 'Použití'], [
              ['Tréninkový míč', 'odolný povrch, rozumná životnost', 'běžné tréninky, tělocvik'],
              ['Zápasový míč', 'přesná velikost a tvar, vyšší kvalita povrchu', 'soutěže a přátelské zápasy'],
              ['Replika oficiálního míče', 'vzhledově shodná s ligovými míči', 'fanoušci a trénink s motivací'],
              ['Wax free míč', 'speciální povrch bez pryskyřice', 'haly, kde se lepidlo nesmí používat'],
              ['Dětský měkký míč', 'lehčí a měkčí, pro první kontakt', 'minihráči a školy']]) +
          '<p>U drahých zápasových modelů je rozdíl hlavně v povrchu a vyvážení. Pro školní tělocvik nebo rekreační házenou postačí tréninkový míč, protože rozdíl oproti zápasovému modelu je hlavně v povrchu a vyvážení, které rekreační hráč tolik nevyužije. Údržba míče je jednoduchá: otřít vlhkým hadříkem, nenechávat na slunci a udržovat tlak, který výrobce doporučuje.</p>'
          '<h2>Obuv do haly: přilnavost a ochrana kotníků</h2>'
          '<p>Házená znamená rychlé starty, zastavení a změny směru. Obuv by proto měla mít podešev z gumové směsi, která se drží parket nebo umělého povrchu, a pevné svrchní díly, které podrží nohu při úkrocích. Běžné běžecké boty se do haly nehodí, protože mají vysoký, ale nestabilní tlumicí systém a při bočním pohybu hrozí vyvrtnutí. V nabídce najdete halové boty, například od značek Puma nebo Hummel, a podobné modely z kategorie <a href="/salova-obuv/">sálová obuv</a>.</p>'
          '<ul><li><strong>Podešev:</strong> světlá nebo bezešvá guma, která nezanechává stopy na podlaze.</li>'
          '<li><strong>Stabilita:</strong> pevná pata, zpevněné boky a nízko položené těžiště.</li>'
          '<li><strong>Velikost:</strong> palec by měl mít rezervu zhruba šířky prstu. Při bočním pohybu noha nesmí klouzat.</li>'
          '<li><strong>Odlišení od venkovní obuvi:</strong> boty do haly se nenosí venku, jinak se zanesou a ztratí přilnavost.</li>'
          '<li><strong>Doplňky:</strong> vložky, <a href="/sportovni-ponozky/">sportovní ponožky</a> bez švů a ortézy pro náchylné kotníky.</li></ul>'
          '<h2>Dresy, kraťasy a oblečení do haly</h2>'
          '<p>Házenkářský dres je sportovní tričko z funkčního materiálu, který odvádí pot a zůstává příjemný při opakovaných kontaktech. Střih je pro hráče volnější v ramenou, aby nebránil hodu. V nabídce jsou samostatné dětské, dámské a pánské velikosti, takže u sady pro tým stačí zvolit velikost podle výšky a postavy. Doplňují je kraťasy, někdy se zesíleným pasem a kapsou na míč nebo ručník.</p>'
          '<p>Na trénink se hodí vrstvy: pod dres tenké funkční spodní prádlo, po tréninku mikina nebo bunda, aby se zahřáté svaly nezchladily. Pro oblečení do teplejších dnů funguje princip podobný jako u <a href="/sportovni-tricka/">sportovních triček</a> a <a href="/funkcni-tricka/">funkčních triček</a>. U týmů je praktické objednávat jednotnou sadu, protože barvy a odstíny se mezi dávkami mírně liší.</p>'
          '<h2>Chrániče, návleky a prevence zranění</h2>'
          '<p>Házená je náročná na kolena, kotníky a prsty. Kolenní chrániče s výztuhou, jaké najdete v dětské i dospělé podobě, tlumí nárazy při pádech na podlahu a chrání před odřením. Neoprenové návleky udržují kloub v teple, ale nenahrazují lékařské doporučení při potížích. Pokud máte zdravotní omezení, poraďte se s lékařem nebo fyzioterapeutem, než zvolíte ortézu.</p>'
          '<p>Prevence začíná u kondice. Správné zahřátí, posilování stabilizačních svalů a protažení po zátěži snižují riziko zranění víc než jakýkoli doplněk. K doplňkovému tréninku mimo halu se hodí <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
          '<h2>Brankářské vybavení a branky</h2>'
          '<p>Brankář nosí volnější oblečení, často kalhoty a dres, které umožňují roznožku, a obuv s dobrým vedením při skluzu. Brankářská výstroj v házené je jednodušší než v jiných míčových sportech, protože brankář brání hlavně tělem, a proto se rukavice používají jen výjimečně. Branka standardní velikosti má rozměr 3 × 2 metry. Hliníkové konstrukce se skládají a přenášejí, redukce umožňuje zmenšit otvor pro děti.</p>'
          '<p>Pro trénink doma nebo ve škole existují tréninkové sítě a zástěny, které zachytí míč a omezí běhání pro jeho sbírání. Při každém použití ověřte stabilitu branky a pojistěte ji proti převrhnutí, protože převrácená branka je častou příčinou úrazů.</p>'
          '<h2>Jak začít, pokud jste noví</h2>'
          '<p>Začátečníkovi stačí míč vhodné velikosti, halová obuv a pohodlné oblečení. Chrániče a pryskyřici můžete přidat později, až poznáte potřeby oddílu. Dobré je zeptat se trenéra na požadavky klubu na barvy dresů a velikosti míčů. Děti mohou začít na <a href="/micove-sporty/">míčových sportech</a> obecně a hru střídat s <a href="/florbalove-hole/">florbalem</a> nebo <a href="/ragby-a-americky-fotbal/">ragby</a>, aby si vybudovaly všestrannost.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě míče o jednu velikost většího „na růst“. Dětská ruka míč neudrží a technika trpí.</li>'
          '<li>Použití venkovní obuvi v hale, která ničí podlahu a neposkytuje oporu.</li>'
          '<li>Nákup pryskyřice bez ověření, zda ji hala povoluje.</li>'
          '<li>Nedostatečné nahuštění míče nebo opačně přepumpování, které zkracuje životnost povrchu.</li>'
          '<li>Podcenění ponožek. Špatné ponožky způsobují puchýře dřív než špatné boty.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Na Sportece porovnáte u každého modelu více obchodů. Sledujte barvu a velikost, protože u míčů a obuvi se stejným názvem často skrývá více variant. Hledáte-li kombinaci pro tým, zvažte nákup většího množství najednou, aby vám sety ladily. Ostatní halové sporty najdete v kategoriích <a href="/basketbalova-obuv/">basketbalová obuv</a> a <a href="/basketbalove-mice/">basketbalové míče</a>.</p>',
    faq=[
      ('Jaký míč na házenou vybrat pro dítě?', 'Podle věku a kategorie. Nejmenším stačí číslo 0 nebo 1, starším dětem číslo 1 nebo 2. Zápasovou velikost 3 používají muži. Míč pro dítě nikdy neberte větší, než odpovídá věku.'),
      ('Jaký je rozdíl mezi míčem s pryskyřicí a wax free?', 'Klasický míč se hraje s pryskyřicí na prstech, která zvyšuje přilnavost. Wax free míče mají speciální povrch, který pryskyřici nevyžaduje a hodí se do hal, kde se lepidlo nepovoluje.'),
      ('Můžu hrát házenou v běžecké obuvi?', 'Nedoporučuje se. Běžecká obuv je určená pro přímý pohyb, nemá oporu pro boky a při změnách směru hrozí vyvrtnutí kotníku. Použijte halovou obuv s gumovou podešví.'),
      ('Jak se pečuje o házenkářský míč?', 'Otírejte ho vlhkým hadříkem, nenechávejte na slunci nebo topení a udržujte doporučený tlak. U míčů s pryskyřicí se používají čisticí prostředky, aby se povrch nelepil.'),
      ('Jak vybrat velikost dresu pro dítě?', 'Podle výšky a obvodu hrudníku v tabulce výrobce. Dres má být volný v ramenou a nesmí škrtit při zvednutí rukou. Mírná rezerva je v pořádku, ale dres nemá být příliš velký.'),
      ('Potřebuji kolenní chrániče?', 'Nejsou povinné, ale při častých pádech na podlahu jsou užitečné, hlavně u dětí a u hráčů s citlivými koleny. Při zdravotních potížích se poraďte s lékařem, nepoužívejte chrániče jako náhradu léčby.'),
      ('Co obsahuje základní výbava pro začátečníka?', 'Míč odpovídající velikosti, halovou obuv, ponožky a pohodlné oblečení. Chrániče, pryskyřice a brašnu na míče přidáte, až budete znát požadavky klubu.'),
      ('Jak velká je házenkářská branka?', 'Standardní rozměr je 3 metry na šířku a 2 metry na výšku. Pro děti a školní trénink se prodávají redukce, které otvor zmenšují.'),
      ('Kam si míč nejlépe uložit?', 'Do pytle nebo tašky na míče, v suchu a mimo přímé slunce. Nenechávejte ho v autě za horka ani v mrazu, mění se tlak i povrch.'),
      ('Dá se házená hrát i na venkovním hřišti?', 'Ano, existuje venkovní varianta, ale povrch se liší od haly. Pro hrubší povrch volte robustnější míč a obuv s odolnou podrážkou a halovou obuv s čistou podešví nechte jen pro halu.')])

# ------------------------------------------------------------------ trekingova-a-mestska-elektrokola
NEW['trekingova-a-mestska-elektrokola'] = dict(long=True,
    title='Trekingová a městská elektrokola: dojíždění a výlety',
    desc='Trekingová a městská elektrokola s motorem a baterií. Jak vybrat dojezd, motor, rám a výbavu a porovnat nabídky českých obchodů.',
    intro='<p>Trekingová a městská elektrokola jsou určená pro každodenní dojíždění, nákupy a výlety po cyklostezkách i po lesních a polních cestách. Mají vzpřímenou polohu, široké pláště, blatníky, nosič a světla, takže se hodí pro většinu uživatelů bez zkušeností s horským kolem. Sporteka porovnává nabídky českých obchodů u modelů s motorem v zadním kole, středovým motorem i vyjímatelnou baterií.</p>'
          '<p>V nabídce převažují značky ' + B(('specialized', 'Specialized'), ('trek', 'Trek'), ('hitway', 'Hitway'), ('devron', 'Devron'), ('dyu', 'DYU'), ('samebike', 'Samebike'), ('corwin', 'Corwin'), ('ttgo', 'Ttgo')) +
          '. Pohled můžete zúžit na <a href="/mestska-elektrokola/">městská elektrokola</a> nebo <a href="/trekingova-elektrokola/">trekingová elektrokola</a>, nadřazená kategorie je <a href="/elektrokola/">elektrokola</a>.</p>',
    guide='<h2>Městské a trekingové e-kolo: rozdíl v praxi</h2>'
          '<p>Obě skupiny mají hodně společného, liší se hlavně zaměřením. Městské elektrokolo je určeno pro dojíždění po asfaltu a dlažbě, často se snadným nástupem a plným výbavou pro každodenní provoz. Trekingové e-kolo je odolnější, má větší pláště a často lepší odpružení, takže zvládne i štěrk a polní cesty. V praxi se obě kategorie překrývají.</p>'
          + T(['Vlastnost', 'Městské e-kolo', 'Trekingové e-kolo'], [
              ['Rám', 'často nízký nástup, nižší hmotnost', 'robustnější rám, často i s nízkým nástupem (dámský)'],
              ['Pláště', 'užší a hladší', 'širší, s jemným vzorkem'],
              ['Terén', 'asfalt, dlažba, cyklostezky', 'cesty, polní trasy, štěrk'],
              ['Výbava', 'blatníky, nosič, světla, zámek rámu', 'totéž plus odpružená vidlice nebo sedlovka'],
              ['Použití', 'dojíždění a nákupy', 'dlouhé výlety a víkendové trasy']]) +
          '<p>Chcete-li srovnat s jinými druhy, podívejte se na <a href="/horska-elektrokola/">horská elektrokola</a>, <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel e-kola</a> a <a href="/skladaci-elektrokola/">skládací elektrokola</a>. Pro převoz nákladu a dětí existují <a href="/nakladni-elektrokola/">nákladní elektrokola</a>.</p>'
          '<h2>Motor: kde je a co to znamená</h2>'
          '<p>Motor v zadním náboji je jednodušší a levnější na výrobu, jízda je podobná klasickému kolu a stačí na rovinu a mírné stoupání. Středový motor sedí u pedálů, využívá převodovku kola a lépe zvládá strmé kopce. Přední motor se používá nejméně, protože zhoršuje stabilitu na kluzkém povrchu. V nabídce se objevují i modely se středovým motorem Bosch nebo Shimano.</p>'
          '<ul><li><strong>Zadní motor:</strong> přirozený pocit, nízká údržba, vhodné pro rovinu a méně náročné trasy.</li>'
          '<li><strong>Středový motor:</strong> lepší rozložení hmotnosti, vyšší točivý moment, přesnější reakce při šlapání.</li>'
          '<li><strong>Snímač točivého momentu:</strong> motor reaguje na sílu šlapání, jízda je přirozenější než u prostého snímače otáček.</li>'
          '<li><strong>Snímač otáček:</strong> motor se zapne při šlapání bez ohledu na sílu, jednodušší a levnější princip.</li></ul>'
          '<p>V Evropské unii platí, že pedelec s asistencí do 25 km/h a výkonem motoru do 250 W se považuje za kolo. Výkonnější stroje a modely s plynovou rukojetí mohou spadat do jiné kategorie vozidel. Při nákupu proto kontrolujte, zda je uvedený maximální výkon i rychlost, ať se vyhnete problémům s předpisy.</p>'
          '<h2>Baterie, kapacita a dojezd</h2>'
          '<p>Kapacita baterie se uvádí ve wattodinách (Wh). Čím vyšší hodnota, tím delší potenciální dojezd, ale také vyšší hmotnost. V nabídce se objevují kapacity kolem 400 až 750 Wh a více. Skutečný dojezd závisí na hmotnosti jezdce a nákladu, profilu trasy, tlaku v pláštích, počasí a zvolené úrovni asistence. Údaje výrobce berte jako orientační.</p>'
          + T(['Faktor', 'Vliv na dojezd', 'Co s tím'], [
              ['Silná asistence', 'výrazně zkracuje dojezd', 'volte nižší režim na rovině'],
              ['Kopce a protivítr', 'zvyšují spotřebu', 'přeřazujte na lehčí převod'],
              ['Nízká teplota', 'snižuje využitelnou kapacitu baterie', 'držte baterii v teple před jízdou'],
              ['Nižší tlak v pláštích', 'zvyšuje valivý odpor', 'kontrolujte tlak každý týden'],
              ['Náklad a hmotnost', 'zvyšují spotřebu', 'nenoste zbytečně těžké věci']]) +
          '<p>Vyjímatelná baterie se dá nabíjet doma i v kanceláři a v případě závady vyměnit samostatně. Integrovaná v rámu vypadá čistěji, ale nabíjení vyžaduje přístup k elektřině u kola. Nabíjejte ji zhruba mezi 20 a 80 procenty, pokud to jde, a nenechávejte úplně vybitou po dlouhou dobu. Při delším skladování, například přes zimu, ji ponechte zhruba v polovině kapacity.</p>'
          '<h2>Rám, velikost a geometrie</h2>'
          '<p>Správná velikost rámu určuje pohodlí. Výrobce uvádí tabulku podle výšky postavy. U elektrokol se kvůli hmotnosti oplatí vyzkoušet i nástup: nízký rám pomáhá při nakládání a v hustém provozu, vyšší je tužší a stabilnější. Kola 28 palců jsou rychlejší a pohodlnější na rovině, kola 26 a 27,5 palce jsou menší, manévrovatelnější a vhodná pro nižší jezdce. Dámský a nižší rám nabízí řada výrobců i v kategorii <a href="/damska-elektrokola/">dámská elektrokola</a>.</p>'
          '<p>Hmotnost elektrokola je vyšší než u běžného kola, proto je důležité promyslet, jak ho budete přepravovat. Při nošení do schodů, do sklepa nebo na vlak se každý kilogram počítá. Pokud potřebujete lehčí stroj, zvažte <a href="/skladaci-elektrokola/">skládací modely</a>.</p>'
          '<h2>Převody, brzdy a pláště</h2>'
          '<ul><li><strong>Převody:</strong> řazení na zadním kole, například osmirychlostní, stačí pro rovinu a mírné stoupání. Pro kopce hledejte širší rozsah.</li>'
          '<li><strong>Brzdy:</strong> kotoučové brzdy brzdí spolehlivě i za mokra a při vyšší hmotnosti. Při koupi sledujte, zda jsou hydraulické nebo mechanické.</li>'
          '<li><strong>Pláště:</strong> širší s ochranou proti defektům se hodí do města. Při jízdě po štěrku volte jemný vzorek a nižší tlak. Více viz <a href="/plaste-a-duse/">pláště a duše</a>.</li>'
          '<li><strong>Odpružení:</strong> odpružená vidlice a sedlovka tlumí rázy, ale přidávají hmotnost a vyžadují údržbu.</li></ul>'
          '<p>Pokud musíte vyměnit díly, vyplatí se zkontrolovat <a href="/cyklo-brzdy/">brzdy a destičky</a>, <a href="/cyklo-pohon/">řetěz a kazetu</a> a hlavně pláště. Elektrokola opotřebovávají pohon rychleji než klasická kola, proto je kontrola častější.</p>'
          '<h2>Výbava pro každodenní provoz</h2>'
          '<p>Většina trekingových a městských e-kol je prodávána s kompletní výbavou, ale ne vždy. Zkontrolujte, zda máte světla, blatníky, nosič, stojánek a zvonek. Chybějící prvky lze doplnit.</p>'
          '<ul><li><a href="/cyklo-svetla/">Světla</a> napájená z baterie kola jsou praktická a vždy nabitá.</li>'
          '<li><a href="/cyklo-blatniky/">Blatníky</a> chrání oblečení v dešti a umožňují jízdu v běžném oděvu.</li>'
          '<li><a href="/cyklo-tasky-a-nosice/">Brašny a nosiče</a> se hodí na nákupy a dojíždění. U elektrokola ověřte nosnost nosiče.</li>'
          '<li><a href="/cyklo-zamky/">Zámek</a> s dostatečnou pevností je nutný, protože e-kolo je lákavou kořistí.</li>'
          '<li><a href="/cyklo-zvonky-a-zrcatka/">Zvonek a zrcátko</a> zlepšují bezpečnost v provozu.</li></ul>'
          '<h2>Bezpečnost jezdce</h2>'
          '<p>Elektrokolo zrychluje rychleji než běžné kolo a lidé na něm často jezdí rychleji, než by se odvážili sami. Základem je helma: <a href="/mestske-cyklohelmy/">městské cyklohelmy</a> nabízejí pevnou skořepinu a světlo. Doplňte <a href="/cyklisticke-rukavice/">rukavice</a>, <a href="/cyklisticke-bryle/">brýle</a> a viditelné oblečení. Před první jízdou si zvykněte na brzdění v bezpečném prostoru.</p>'
          '<h2>Údržba a péče</h2>'
          '<ol><li>Pravidelně kontrolujte tlak v pláštích.</li>'
          '<li>Čistěte kolo vlhkým hadrem, nikdy je nestříkejte tlakovou vodou do motoru a baterie.</li>'
          '<li>Mažte řetěz a kontrolujte jeho opotřebení.</li>'
          '<li>Baterii skladujte v suchu, při pokojové teplotě, nenabíjejte ji nonstop.</li>'
          '<li>Před sezónou nechte prověřit brzdy a světla v servisu.</li></ol>'
          '<p>Základní nářadí a ošetřovací pomůcky najdete v kategoriích <a href="/cyklo-udrzba/">údržba kol</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Pro koho je které e-kolo</h2>'
          + T(['Uživatel', 'Co hledat', 'Poznámka'], [
              ['Dojíždějící do práce', 'městský model s blatníky, světly a nosičem', 'zkontrolujte, zda se baterie dobíjí v kanceláři'],
              ['Rekreační cyklisté', 'trekingový model se středovým motorem', 'ověřte dojezd pro vaše výlety'],
              ['Senioři a méně zdatní jezdci', 'nízký nástup, jednoduché ovládání', 'zkoušejte před koupí'],
              ['Pendleři s vlakem', 'lehké nebo skládací kolo', 'hmotnost je klíčová'],
              ['Rodiny', 'e-kolo se silným nosičem', 'zvažte <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>']]) +
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je volba podle dojezdu uvedeného v inzerátu bez ohledu na vlastní trasu. Druhou je zanedbání servisu: pokud nevíte, kdo kolo bude opravovat, zeptejte se prodejce na servis a dostupnost náhradních dílů. Třetí je zanedbání velikosti rámu, čtvrtou zanedbání zámku. Levné modely bez známého servisu bývají problematické, když se objeví závada baterie nebo řídicí jednotky.</p>'
          '<h2>Jak porovnat nabídky na Sportece</h2>'
          '<p>Porovnávejte celý název produktu včetně velikosti rámu, barvy, kapacity baterie a velikosti kol. Stejný model se může lišit v motoru a výbavě podle roku výroby. Sledujte dostupnost, dopravu, záruku a to, zda prodejce nabízí sestavení a servis. Z příbuzných kategorií stojí za pohled <a href="/jizdni-kola/">jízdní kola</a>, <a href="/trekingova-kola/">trekingová kola</a> a <a href="/mestska-kola/">městská kola</a>.</p>',
    faq=[
      ('Jaký je rozdíl mezi trekingovým a městským elektrokolem?', 'Městské je určené pro asfalt a dojíždění, trekingové má robustnější konstrukci a širší pláště pro cyklostezky, štěrk a delší výlety. Obě kategorie mají podobnou výbavu a vzpřímenou polohu.'),
      ('Kolik wattodin baterie potřebuji?', 'Záleží na délce trasy, terénu, hmotnosti a použité asistenci. Pro krátké dojíždění stačí menší kapacita, na delší výlety nebo kopce vyberte větší. Údaje výrobce berte jen orientačně.'),
      ('Je lepší středový, nebo zadní motor?', 'Středový motor lépe rozkládá hmotnost a zvládá strmé kopce, zadní je jednodušší a hodí se na rovinu. Pro hornatější okolí zvažte střed, pro město s mírným profilem postačí zadní motor.'),
      ('Potřebuji na e-kolo řidičský průkaz nebo registraci?', 'Pedelec s asistencí do 25 km/h a motorem do 250 W se v EU považuje za kolo a bez průkazu se řídí. Výkonnější modely mohou spadat do jiné kategorie, ověřte si údaje u prodejce.'),
      ('Jak daleko dojedu na jedno nabití?', 'Skutečný dojezd závisí na hmotnosti, terénu, počasí, tlaku v pláštích a úrovni asistence. Údaje výrobce jsou laboratorní. Počítejte raději s rezervou.'),
      ('Jak nabíjet baterii, aby vydržela?', 'Nabíjejte při pokojové teplotě, ideálně mezi zhruba 20 a 80 procenty, a nenechávejte ji dlouho zcela vybitou. Při zimním skladování ji uchovejte zhruba v polovině kapacity a v suchu.'),
      ('Co dělat v zimě?', 'Baterii před jízdou držte v teple, protože chlad snižuje využitelnou kapacitu. Zkontrolujte pláště a zvolte vhodné oblečení a světla. Po jízdě v soli kolo otřete.'),
      ('Dá se elektrokolo přepravovat vlakem nebo autem?', 'Ano, ale je těžší než klasické kolo. Pro auto použijte nosič s dostatečnou nosností, viz <a href="/cyklo-nosice-na-auto/">nosiče kol na auto</a>. U vlaku zjistěte podmínky dopravce a zvažte skládací model.'),
      ('Jak vybrat velikost rámu?', 'Podle výšky postavy a tabulky výrobce. Při zkoušce byste měli dosáhnout na zem špičkami nebo celou plochou chodidla podle komfortu a sedlo nastavit tak, aby noha ve spodní poloze byla mírně pokrčená.'),
      ('Stojí za to kupovat levné e-kolo bez značky?', 'Může se hodit, ale ověřte servis, dostupnost baterie a náhradních dílů a záruku. U neznámých modelů bývá problém se servisem, a to může cenový rozdíl smazat.')])

# ------------------------------------------------------------------ lukostrelba
NEW['lukostrelba'] = dict(long=True,
    title='Lukostřelba: luky, šípy, terče a ochranné doplňky',
    desc='Luky, šípy, terče, chrániče předloktí a toulce pro děti i dospělé. Jak vybrat luk, délku šípu a bezpečný terč a porovnat nabídky obchodů.',
    intro='<p>Lukostřelba spojuje soustředění, techniku a pohyb na čerstvém vzduchu. Může být zábavou pro děti na zahradě, volnočasovým sportem pro dospělé i cestou k pravidelnému tréninku v klubu. Sporteka porovnává nabídky českých obchodů u luků, kuší, šípů, terčů, chráničů předloktí, toulců a doplňků pro začátečníky i zkušenější střelce.</p>'
          '<p>V nabídce jsou značky ' + B(('insportline', 'Insportline'), ('geologic', 'Geologic'), ('yate', 'Yate'), ('marksman', 'Marksman'), ('jack-pyke', 'Jack Pyke'), ('avalon', 'Avalon')) +
          '. Kategorie patří do přehledu <a href="/volny-cas/">hry a volný čas</a>, příbuzné jsou <a href="/sipky/">šipky</a>, <a href="/hry-na-zahradu/">hry na zahradu</a> a <a href="/lov-a-priroda/">lov a příroda</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Nabídka je různorodá. Vedle skutečných sportovních luků jsou tu dětské sety s jednoduchými šípy a přísavkami, karbonové šípy pro zkušené střelce, terče na zahradu i příslušenství pro bezpečné držení a střelbu. Část nabídky tvoří i kuše, u nichž je dobré ověřit platné předpisy a podmínky použití. Zboží je dobré vybírat podle toho, zda půjde o hru, rekreaci nebo trénink.</p>'
          + T(['Skupina', 'Typické zboží', 'Komu se hodí'], [
              ['Dětské sety', 'luk s lehčími šípy, přísavky, jednoduchý terč', 'děti od základních let pod dohledem dospělého'],
              ['Rekreační luky', 'luky pro pravoráké a leváky, sety s toulcem', 'zahrada a rekreační střelba'],
              ['Šípy', 'dřevěné, skleněné, karbonové, náhradní sady', 'každý střelec s vlastním lukem'],
              ['Terče a zástěny', 'slámové, pěnové a textilní terče', 'trénink a bezpečné zachycení šípů'],
              ['Chrániče a rukavice', 'chrániče předloktí, prstové chrániče', 'všichni, aby tětiva neotloukala ruku'],
              ['Toulce a pouzdra', 'pasové, zádové a boční toulce', 'pohodlné nošení šípů'],
              ['Kuše', 'sportovní a rekreační modely', 'zájemci o jiný druh střelby']]) +
          '<h2>Druhy luků</h2>'
          '<ul><li><strong>Rekurzivní luk:</strong> klasický olympijský tvar s ohnutými konci ramen. Dobře přenáší sílu a je nejčastější v klubech.</li>'
          '<li><strong>Dlouhý luk:</strong> tradiční tvar bez složitých prvků, jednoduchý a odolný. Vyžaduje cit pro střelbu a dobrou techniku.</li>'
          '<li><strong>Kladkový luk:</strong> pokročilý model s kladkami, obvykle pro zkušené střelce, vyžaduje seřízení a odbornou údržbu.</li>'
          '<li><strong>Jednoduchý rekreační luk:</strong> levnější luk z kompozitu nebo dřeva, často dodávaný v sadě pro začátečníky a děti.</li>'
          '<li><strong>Dětský luk:</strong> lehký, s malou silou tahu a bezpečnostními šípy s gumovými nebo přísavkovými hroty.</li></ul>'
          '<p>Při výběru dbejte na to, zda je luk pro pravorukého nebo levorukého střelce. Označení „pro pravoráky“ a „pro leváky“ najdete v názvech modelů, například u řady Viper. Podle dominantního oka, ne podle dominantní ruky, určíte nejpřirozenější stranu. Pokud si nejste jistí, otestujte na střelnici nebo se poraďte s instruktorem.</p>'
          '<h2>Síla luku a délka tahu</h2>'
          '<p>Síla luku se udává v librách (lbs) a vyjadřuje sílu, kterou je třeba vynaložit při dosažení plné délky tahu. Začátečník nemá volit příliš silný luk. Příliš velká síla znamená špatnou techniku, rychlou únavu a riziko přetížení ramene. Děti začínají s malou silou, dospělí s mírnou silou, kterou zvládnou udržet bez třesu.</p>'
          + T(['Skupina', 'Přibližná volba síly', 'Poznámka'], [
              ['Malé děti', 'velmi nízká síla, plastové a pěnové luky', 'vždy pod dohledem dospělého'],
              ['Starší děti a mládež', 'nízká až střední síla', 'zvětšuje se s fyzickým vývojem'],
              ['Dospělí začátečníci', 'nízká až střední síla', 'raději nižší a čistá technika'],
              ['Pokročilí střelci', 'vyšší síla podle zkušeností', 'doporučuje se konzultace s trenérem']]) +
          '<p>Délka tahu se měří od nástřelu po maximální natažení tětivy a je daná rozpětím paží. Rozpětí paží, tedy vzdálenost mezi konečky prstů při rozpažení, dělená přibližně 2,5 dává orientační délku tahu. Podle ní se vybírá délka šípu.</p>'
          '<h2>Šípy: materiál, délka a tuhost</h2>'
          '<p>Šíp musí odpovídat luku. Příliš krátký šíp je nebezpečný, protože se při tahu může dostat za okno luku. Příliš dlouhý šíp zhoršuje přesnost. Tuhost (spine) vyjadřuje, jak moc se šíp prohýbá při výstřelu. Při nákupu proto kontrolujte označení na šípu a doporučení výrobce luku. V nabídce se objevují karbonové šípy s označením například 32/1100, 32/1200 nebo 32/1500 a jejich sady pro výměnu.</p>'
          '<ul><li><strong>Dřevěné šípy:</strong> tradiční, vhodné pro dlouhé luky a nenáročnou střelbu. Mohou prasknout a vyžadují kontrolu.</li>'
          '<li><strong>Skleněné šípy:</strong> levnější a pružnější, vhodné pro děti a rekreaci.</li>'
          '<li><strong>Karbonové šípy:</strong> lehké, rovné a pevné. Oblíbené u zkušenějších střelců, ale po poškození je nutné je vyřadit.</li>'
          '<li><strong>Hroty:</strong> pro terč bodové, pro děti bezpečnostní. Nikdy nepoužívejte lovecké hroty na terč ze slámy.</li>'
          '<li><strong>Brk a vedení:</strong> pěnová nebo plastová brka se dají vyměnit, pokud se opotřebují.</li></ul>'
          '<p>Před každou střelbou zkontrolujte šípy: praskliny, odštípnuté hroty, uvolněné nástavce. Poškozený šíp nikdy nepoužívejte, protože se při výstřelu může roztříštit.</p>'
          '<h2>Terče a bezpečné místo střelby</h2>'
          '<p>Bezpečnost je u lukostřelby klíčová. Střílet se smí jen na místě, kde nikdo nemůže vstoupit do dráhy šípu, za terčem je záchytný val nebo stěna a v okolí nejsou lidé, zvířata ani cesty. Šíp, který terč mine, může letět velmi daleko. Na zahradě proto používejte zástěnu nebo alespoň záchytnou síť a zvolte směr, kde neleží soused.</p>'
          + T(['Typ terče', 'Vlastnosti', 'Poznámka'], [
              ['Slámový', 'tradiční, dobře zachytí šípy', 'je těžší a v dešti nasákne'],
              ['Pěnový', 'lehký a odolný proti vlhku', 'životnost závisí na hustotě pěny'],
              ['Textilní s výplní', 'skladný, pro děti', 'nehodí se pro silné luky'],
              ['Zástěna a síť', 'zachytí zbloudilé šípy', 'doplněk, ne náhrada terče']]) +
          '<p>Terč pověste nebo postavte tak, aby se nepřevrátil. Střed terče se doporučuje umístit zhruba do výšky ramen střelce. Pro začátečníky se hodí krátká vzdálenost, kterou můžete postupně zvětšovat, jak roste jistota.</p>'
          '<h2>Chrániče, toulce a další doplňky</h2>'
          '<p>Chránič předloktí, který najdete i v běžné nabídce, chrání ruku před úderem tětivy. Bez něj se objevují modřiny a odřeniny a střelec se začne bát výstřelu. Prstová rukavice nebo chránič prstů zase ulehčují tah tětivy. Toulec drží šípy po ruce a chrání hroty, existuje v provedení na pas, na záda nebo k luku.</p>'
          '<ul><li><strong>Chránič předloktí:</strong> základ pro každého začátečníka.</li>'
          '<li><strong>Chránič prstů nebo rukavice:</strong> zabraňuje puchýřům při delší střelbě.</li>'
          '<li><strong>Toulec:</strong> pasový je praktický při pohybu, zádový při terénní střelbě.</li>'
          '<li><strong>Pouzdro na luk:</strong> chrání luk při převozu a zabraňuje poškození ramen.</li>'
          '<li><strong>Náhradní tětiva:</strong> tětivy se opotřebují a při přetržení je nutné je vyměnit.</li></ul>'
          '<p>Oblečení při střelbě má být upnuté a bez volných cípů, které by se mohly zachytit o tětivu. Terénní střelci využívají <a href="/lovecke-obleceni/">lovecké oblečení</a> nebo <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>. Pro střelbu při vycházce přijde vhod <a href="/batohy/">batoh</a>.</p>'
          '<h2>Jak začít</h2>'
          '<ol><li>Zvolte místo, kde máte dostatek bezpečného prostoru a záchytný val.</li>'
          '<li>Vyberte luk podle věku, síly a dominantního oka.</li>'
          '<li>Doplňte šípy odpovídající délky a ochranu předloktí.</li>'
          '<li>Naučte se základní postoj, nasazení šípu, tah a uvolnění od zkušeného střelce nebo trenéra.</li>'
          '<li>Střílejte nejdřív na krátkou vzdálenost a pozvolna ji zvětšujte.</li></ol>'
          '<p>Většina měst nabízí lukostřelecké kluby, kde zapůjčí základní vybavení a ukážou techniku. Je to nejlepší způsob, jak zjistit, zda vás sport baví, než investujete do vlastního luku.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Luk skladujte uvolněný, bez napnuté tětivy, v suchu a mimo mráz i horko.</li>'
          '<li>Tětivu kontrolujte, zda se neprodřela, a pravidelně ji voskujte.</li>'
          '<li>Šípy skladujte svisle nebo v tubě, aby se nezkroutily.</li>'
          '<li>Dřevěné části ošetřete olejem nebo voskem proti vlhkosti.</li>'
          '<li>Po mokré střelbě vše osušte, než uložíte do pouzdra.</li></ul>'
          '<h2>Lukostřelba pro děti</h2>'
          '<p>Dětské sady, jako je Hood nebo jednoduchý luk s přísavkovými šípy, jsou určené k zábavě a nácviku. Dítě by mělo střílet pouze pod dozorem dospělého, v prostoru bez dalších osob a jen na terč. Nikdy nemiřte na lidi, zvířata ani na předměty, které se mohou odrazit. Pravidla bezpečnosti si projděte spolu a trvejte na nich. Pro menší děti jsou v oddíle <a href="/hry-na-zahradu/">hry na zahradu</a> vhodné alternativy, například <a href="/sipky/">šipky</a> s bezpečnými hroty.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Častá chyba je koupě luku s příliš velkou silou, který střelci znemožní správnou techniku. Další je koupě šípů bez ohledu na délku tahu a zanedbání ochrany předloktí. Častým omylem je i nedostatečný terč: slabá zástěna dovolí šípu proletět a ohrozit okolí. Zkontrolujte také, zda je luk určen pro praváka, nebo leváka, a neodkládejte výměnu poškozených šípů.</p>'
          '<h2>Jak porovnat nabídky na Sportece</h2>'
          '<p>Porovnávejte celé sady, ne jen cenu jednotlivých dílů. Zkontrolujte, co všechno sada obsahuje: počet šípů, terč, chránič, toulec. Pokud potřebujete jednotlivé doplňky, porovnejte kompatibilitu. U šípů sledujte délku a tuhost, u luků stranu a sílu. Pro širší výběr volnočasových her nahlédněte také do kategorií <a href="/sipkove-terce/">šipkové terče</a>, <a href="/sipkove-doplnky/">šipkové doplňky</a> a <a href="/outdoor-doplnky/">outdoor doplňky</a>.</p>',
    faq=[
      ('Jaký luk vybrat pro začátečníka?', 'Rekreační nebo rekurzivní luk s nižší silou tahu. Důležitější než výkon je správná technika. Začátečník by měl zvolit luk, který udrží bez třesu a se kterým se nebude zbytečně unavovat.'),
      ('Jak poznám délku šípu?', 'Měří se podle délky tahu, která vychází z rozpětí paží. Šíp má být o něco delší než vaše plná délka tahu, aby se nikdy nedostal za okno luku. Při pochybnostech se poraďte s instruktorem.'),
      ('Jaký je rozdíl mezi luk pro pravoráky a levoráky?', 'Okno luku je vyříznuté pro jednu stranu, takže šíp prochází správně jen při držení ve správné ruce. Správnou stranu určuje dominantní oko, nejen ruka.'),
      ('Kde mohu střílet z luku?', 'Na střelnici, v klubu nebo na vlastním pozemku s bezpečným záchytným valem a bez osob v dráze šípu. Ověřte si pravidla obce a majitele pozemku. Na veřejných místech nestřílejte.'),
      ('Je lukostřelba vhodná pro děti?', 'Ano, pokud mají vhodné dětské vybavení a střílí pod dohledem dospělého. Dítě musí znát pravidla, mít bezpečné šípy a střílet pouze na terč.'),
      ('Proč potřebuji chránič předloktí?', 'Tětiva po výstřelu může udeřit do vnitřní strany předloktí, což bolí a dělá modřiny. Chránič tomu zabrání a pomáhá střelci udržet klid při výstřelu.'),
      ('Jak se starat o tětivu?', 'Pravidelně ji voskujte, kontrolujte, zda se neprodírá, a při viditelném poškození vyměňte. Tětivu nenechávejte dlouho napnutou, pokud luk neslouží.'),
      ('Jaký terč je nejlepší?', 'Záleží na luku a místu střelby. Slámový terč dobře drží šípy, pěnový je lehčí a odolnější proti vlhku. Pro silnější luky volte hustší materiál a vždy za něj přidejte záchytnou zástěnu.'),
      ('Můžu použít šípy z jiného luku?', 'Jen pokud odpovídají délce tahu a tuhosti, které váš luk potřebuje. Nesprávné šípy létají nepřesně a mohou být nebezpečné. Ověřte údaje výrobce.'),
      ('Je kuše stejná jako luk?', 'Ne. Kuše se drží a střílí jinak a pro její nákup a používání mohou platit odlišná pravidla. Před koupí si ověřte aktuální předpisy a používejte ji jen na bezpečném místě.')])

# ------------------------------------------------------------------ extensions (intro and guide sections)
NEW['mestske-cyklohelmy']['intro'] += ('<p>Nákup začíná změřením obvodu hlavy a rozhodnutím, zda potřebujete světlo, vizor nebo model pro e-kolo. Níže najdete přehled typů, nastavení, péče a pravidel, která vám pomohou vybrat helmu bez zbytečných kompromisů.</p>')
NEW['mestske-cyklohelmy']['guide'] += (
    '<h2>Materiály a konstrukce skořepiny</h2>'
    '<p>Většina městských přileb používá lehkou polystyrenovou pěnu pod vnějším polykarbonátovým pláštěm. Metoda in-mold spojuje obě vrstvy při lisování, takže helma je lehčí a odolnější vůči rozlepení. Hard-shell konstrukce s pevnější vnější slupkou je těžší, ale lépe snáší odřený povrch, kterému se v batohu nevyhnete. U dražších modelů se objevuje i zpevnění v týlu a pod čelem, které rozkládá náraz na větší plochu.</p>'
    '<p>Vnitřní polstrování je vyměnitelné a omyvatelné. Mnoho značek, například Alpina nebo Uvex, dodává náhradní sady. Prostor pro uši a brýle bývá řešen zářezy v popruzích, takže <a href="/cyklisticke-bryle/">brýle</a> nedrhnou o rámeček.</p>'
    '<h2>Barva, vzhled a viditelnost</h2>'
    '<p>Světlé a výrazné barvy, například bílá, žlutá nebo oranžová, se v šeru a mlze zpozorují dříve než černá. Matné povrchy vypadají decentně, ale ztrácejí viditelnost. Pokud preferujete tmavou helmu, doplňte ji reflexní samolepkou nebo světlem. Reflexní pruhy na popruzích a v zadní části zvýší šanci, že vás řidič zpozoruje včas.</p>'
    '<h2>Hluk, vítr a komfort během jízdy</h2>'
    '<p>Při rychlejší jízdě může vítr proudící okolo uší hučet. Tvar helmy, popruhy a poloha přezky ovlivňují hluk víc, než se zdá. Zkuste helmu na kole, nejen v obchodě, a rozhodněte, zda vám její tvar při větru nevadí. V létě se vyplatí větší otvory, v zimě menší a vložka proti studenému větru.</p>')
NEW['hazena']['guide'] += (
    '<h2>Trénink doma a ve škole</h2>'
    '<p>Pro domácí rozvoj dovedností se hodí odrazová stěna, malá síť na přihrávku a lehčí míč, který se nesnaží přetížit zápěstí. Žáci si mohou procvičovat vedení míče, střelbu na branku se zmenšenou redukcí a postřeh. Škola zvládne základní trénink s několika míči, kužely a jednou brankou. Pro doplňkovou kondici se hodí <a href="/posilovaci-stroje/">posilovací stroje</a>, ale i jednoduché cviky s vlastní vahou. Kdo chce jiný týmový sport, podívá se do kategorií <a href="/hokej/">hokej</a> nebo <a href="/fotbal/">fotbal</a>.</p>')
NEW['trekingova-a-mestska-elektrokola']['intro'] += ('<p>Pomáháme si údaji o motoru, kapacitě baterie, velikosti kol a výbavě, abyste rychle poznali, který model odpovídá vaší trase.</p>')
NEW['trekingova-a-mestska-elektrokola']['guide'] += (
    '<h2>Pořízení, převzetí a první jízda</h2>'
    '<p>Po doručení zkontrolujte rám, pláště a světla, nabijte baterii podle návodu a nastavte sedlo a řídítka. Elektrokola se zpravidla dodávají částečně smontovaná, proto zkontrolujte dotažení pedálů, kol a brzd. První jízdu věnujte seznámení s režimy asistence a brzdami na klidném místě, než vyrazíte do provozu. Zapište si sériové číslo rámu pro případ krádeže nebo reklamace.</p>'
    '<h2>Ochrana před krádeží</h2>'
    '<p>Elektrokolo je cenný předmět, proto používejte kvalitní zámek a kolo zamykejte za rám ke stabilnímu předmětu. Vyjímatelnou baterii a displej berte s sebou. Doma si ponechte fotografie kola a sériové číslo a zvažte pojištění. V kategorii <a href="/cyklo-zamky/">zámky na kola</a> najdete řetězy, pancéřové zámky i skládací modely.</p>')

NEW['hazena']['intro'] += ('<p>Text níže vysvětluje velikosti míčů, pryskyřici, volbu obuvi a péči o výbavu.</p>')
NEW['lukostrelba']['intro'] += ('<p>Průvodce shrnuje druhy luků, volbu síly a šípů, bezpečnost střelby i péči o vybavení.</p>')
NEW['lukostrelba']['guide'] += (
    '<h2>Technika a postoj ve zkratce</h2>'
    '<p>Základem je stabilní postoj na šířku ramen, uvolněná ramena a rovná záda. Šíp se nasazuje na polici luku, šíp se nasazuje zářezem na tětivu pod nasazovací bod a prsty se pokládají za šíp. Tah vychází ze zad, ne jen z paže, a uvolnění tětivy má být plynulé. Většina začátečníků trpí tím, že zvedá rameno nebo trhá prsty. Pomůže krátká série výstřelů s pauzami a návštěva klubu, kde trenér opraví drobnosti dřív, než se stanou zlozvyky.</p>')
NEW['trekingova-a-mestska-elektrokola']['guide'] += (
    '<p>Pro delší výlety si předem naplánujte trasu s nabíjecími body a vezměte nářadí na opravu defektu, viz <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>')

NEW['hazena']['intro'] += ('<p>Najdete zde i radu pro rodiče a trenéry, kteří vybavují celý tým.</p>')
NEW['lukostrelba']['intro'] += ('<p>Připojili jsme rady pro rodiče.</p>')
