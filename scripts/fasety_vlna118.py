"""sporteka.cz — facet landing texts wave 118: batoh-husky, new-balance-kopacky, ocun-lezecky, brankarske-rukavice-detske.
General true facts only, no prices or counts. Brands and models verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ batoh-husky
NEW['batoh-husky'] = dict(
    title='Batoh Husky: řady, objemy a výběr podle použití',
    desc='Batohy české outdoorové značky Husky: městské Nery a Shater, turistické Campus a Curly, expediční Cruiser, dětské Jikko a Jibby. Jak vybrat objem.',
    intro='<p>Husky je česká outdoorová značka a její batohy se v nabídce dělí do několika zřetelných řad. Menší modely jako Nery, Peten nebo Shater slouží ve městě, v kanceláři a na kratší procházky. Campus a Curly nesou věci na víkendové výlety, Cruiser je velký expediční batoh a řady Jadju, Jikko, Jibby a Jolly jsou určené dětem. '
          'Stránka sbírá batohy této značky z kategorie <a href="/batohy/">batohy</a> a pomáhá poznat, která řada odpovídá vašemu plánu. Průvodce porovnává objemy podle názvů modelů, vysvětluje rozdíl mezi městskou a expediční konstrukcí, radí s velikostí dětských batůžků a ukazuje, jak Husky obstojí vedle značek Osprey nebo Deuter, a poradí také s péčí o batoh po sezóně.</p>',
    guide='<h2>Jak jsou řady Husky rozdělené</h2>'
          '<p>Husky používá v názvech modelů objem v litrech, takže už z popisku poznáte, do jaké velikostní třídy batoh patří. Číslo za názvem (například Nery 20L nebo Curly 40L) je orientační objem hlavní komory a kapes. Podle určení se nabídka dá rozdělit do pěti skupin.</p>'
          + T(['Skupina', 'Modely v nabídce', 'Typické použití'], [
              ['Městské a kancelářské', 'Nery, Nory, Truvel, Shater, Sofer, Moper', 'dojíždění, škola, notebook, lehký víkend'],
              ['Turistika a cyklistika', 'Peten, Campus', 'půldenní až celodenní výlet, kolo'],
              ['Expedice a trek', 'Capture, Curly, Cruiser', 'vícedenní túra, cestování s větším nákladem'],
              ['Dětské', 'Jadju, Jikko, Jibby, Jolly', 'školka, první třída, výlety dětí'],
              ['Speciální', 'Chladicí Cooler', 'jídlo a pití, které má zůstat chladné']]) +
          '<p>Z tohoto členění plyne první praktická rada: nehledejte „nejlepší batoh Husky“, hledejte řadu, která odpovídá vašemu plánu. Městský Shater nebude pohodlný pod patnácti kilogramy trekového nákladu a Cruiser je zbytečně velký na cestu do kanceláře.</p>'
          '<h2>Městské modely: Nery, Shater, Sofer, Moper</h2>'
          '<p>Nery patří k nejznámějším lehkým batohům značky a v nabídce se objevuje v mnoha barvách, od černé přes béžovou po pastelové tóny. Dvacet litrů stačí na svačinu, mikinu, láhev a menší tablet. Řady Shater (23 l), Moper (28 l) a Sofer (30 l) jsou označené jako office, tedy s větším důrazem na organizaci, na kapsu pro notebook a úhlednější vzhled. Truvel s pětadvaceti litry míří spíše na krátké cestování a víkendové pobyty.</p>'
          '<p>Při výběru městského batohu srovnejte tři věci. Za prvé rozměr notebooku: kapsa musí odpovídat úhlopříčce vašeho přístroje, jinak se zařezává nebo se v ní pohybuje. Za druhé záda: u delšího dojíždění oceníte polstr a ventilační kanálky. Za třetí barvu. Černá nebo tmavě modrá vydrží roky bez viditelných stop, světlé odstíny jako béžová nebo faded pink vypadají čerstvěji, ale rychleji zachytí špínu z kolejnic a zábradlí. Pokud hledáte nenápadný kousek, podívejte se i do výběru <a href="/cerny-batoh/">černý batoh</a>, který porovnává různé značky.</p>'
          '<h2>Turistika a cyklistika: Peten a Campus</h2>'
          '<p>Peten existuje v několika velikostech od deseti do dvaceti litrů a je určený lidem, kteří nepotřebují mnoho místa, ale chtějí, aby batoh seděl těsně a nehoupal se. To je důležité na kole, kde volný batoh na zádech vadí víc než na chůzi. Campus ve třiceti litrech zvládne celodenní výlet s pláštěnkou, teplou vrstvou, jídlem a vodou.</p>'
          '<ul><li><strong>Pro kolo:</strong> menší objem, hrudní popruh a těsné přilnutí, aby se batoh nekýval ze strany na stranu.</li>'
          '<li><strong>Pro pěší výlet:</strong> batoh na dvacet až třicet litrů s bočním místem na láhev.</li>'
          '<li><strong>Pro výlet s dětmi:</strong> větší objem, protože rodič nese i věci navíc, proto spíš Campus než Peten.</li></ul>'
          '<p>Podrobnější rady k nosným systémům, bederním pásům a ventilaci zad najdete v kategorii <a href="/turisticke-batohy/">turistické batohy</a>. Pokud chcete Husky vedle jiných značek, porovnejte ho s modely <a href="/osprey-batoh/">Osprey</a> a <a href="/deuter-batohy/">Deuter</a>.</p>'
          '<h2>Expediční řady Curly, Capture a Cruiser</h2>'
          '<p>Curly a Capture mají čtyřicet litrů, Cruiser padesát pět. Čtyřicítka stačí na víkend se spacákem a karimatkou připevněnou zvenku, případně na krátké cestování s příručním zavazadlem v batohu. Padesát pět litrů je už horní hranice pro vícedenní trek bez podpory, kde nosíte stan, vaření a jídlo. U takových batohů je rozhodující nosný systém, tedy nastavení zad a bederní pás, který přenáší váhu na kyčle.</p>'
          + T(['Model', 'Objem', 'Pro koho'], [
              ['Capture', '40 l', 'víkendová túra, lehké cestování'],
              ['Curly', '40 l', 'víkend s přespáním, nejčastěji nabízená řada v několika barvách'],
              ['Cruiser', '55 l', 'vícedenní trek, expedice, větší výbava']]) +
          '<p>Barvy expedičních řad bývají tlumené: tmavě zelená, černá, bordó nebo žlutozelená. Pro krajinu je praktická zelená, na stezce s více turisty zase pomůže výraznější odstín, protože batoh v lese nezmizí při odpočinku. Bez ohledu na barvu zkoušejte batoh naložený alespoň několika kilogramy, protože prázdný nosný systém nic neprozradí. Vybavení pro tento účel najdete i ve výběrech <a href="/vuch-batoh/">Vuch</a> a <a href="/the-north-face-batoh/">The North Face</a>.</p>'
          '<h2>Dětské batohy Husky: Jadju, Jikko, Jibby a Jolly</h2>'
          '<p>Dětské batohy se liší objemem i konstrukcí zad. Jadju s deseti litry je určený nejmenším, tedy ke školce a na krátké výlety. Jikko a Jolly (15 l) dosahují na první třídu, kde dítě potřebuje pouzdro, svačinu a pár sešitů. Jibby se dvaceti litry už zvládne školní den s učebnicemi. Pro větší děti a studenty zvažte spíše <a href="/skolni-batohy/">školní batohy</a> s pevnějším zadním dílem.</p>'
          '<ul><li><strong>Hmotnost:</strong> plně naložený dětský batoh by neměl být těžší než zhruba desetina váhy dítěte.</li>'
          '<li><strong>Velikost:</strong> horní okraj batohu nemá překračovat ramena a spodek nemá sahat pod pás.</li>'
          '<li><strong>Popruhy:</strong> nastavitelné, polstrované, s hrudním popruhem, aby neklouzaly dolů.</li>'
          '<li><strong>Reflexní prvky:</strong> viditelnost večer je při cestě ze školy a kroužků důležitá.</li></ul>'
          '<h2>Husky ve srovnání s dalšími značkami</h2>'
          '<p>Husky je česká značka zaměřená na dostupnou outdoorovou výbavu pro široké spektrum uživatelů. Osprey a Deuter jsou specializované batohové firmy s rozsáhlými řadami technických trekových batohů a bohatší nabídkou velikostí zad. Pro každodenní nošení, školu a občasné výlety Husky vyhovuje a nabízí zřetelné členění. Pokud plánujete týdenní treky nebo expedice s těžkým nákladem, má smysl porovnat nosný systém s <a href="/osprey-batoh/">Osprey</a> nebo <a href="/deuter-batohy/">Deuter</a> a podle zad vybrat nejlépe sedící model. V ženském střihu se podívejte do výběru <a href="/damsky-batoh/">dámský batoh</a>, pro muže je tu <a href="/pansky-batoh/">pánský batoh</a>.</p>'
          '<h2>Jak batoh zabalit, aby seděl</h2>'
          '<p>I dobře vybraný batoh se špatně nosí, pokud je nesprávně zabalený. Nejtěžší věci patří ke zádům a do výšky lopatek, lehké a objemné (spacák, oblečení) dospodu a nahoru pak to, co potřebujete rychle: pláštěnka, svačina, čelovka. Boční kapsy jsou pro lahve a drobnosti, ne pro těžké kusy, které by batoh stahovaly na jednu stranu. U menších městských batohů platí totéž v malém: notebook k zádům, kabel a pouzdro dopředu.</p>'
          '<p>Před odchodem utáhněte kompresní popruhy, aby se obsah nepřesouval. Při chůzi z kopce se prázdná místa v batohu projeví jako houpání a po hodině už tlačí na ramena. Pokud věci nenaplní celý objem, je to jasný signál, že jste zvolili příliš velký model a příště by stačila nižší řada, například Campus místo Curly.</p>'
          '<h2>Péče a údržba batohu</h2>'
          '<ol><li>Po výletu batoh vyprázdněte, otevřete všechny kapsy a nechte vyschnout ve stínu.</li>'
          '<li>Špínu odstraňte vlhkým hadříkem a jemným mýdlem, pračku používejte jen výjimečně.</li>'
          '<li>Nikdy nesušte na topení ani na přímém slunci, hrozí deformace a poškození laminace.</li>'
          '<li>Zipy občas očistěte kartáčkem a nenatahujte přeplněné zavazadlo násilím.</li>'
          '<li>Uložte volně, ne stlačený pod těžkými věcmi, aby si zachoval tvar zad.</li></ol>'
          '<p>V kategorii <a href="/batohy/">batohy</a> pak můžete modely Husky porovnat podle ceny a dostupnosti v českých obchodech, včetně různých barevných variant téhož modelu.</p>',
    faq=[
        ('Jaký objem má batoh Husky Nery?',
         'Model Nery má podle názvu dvacet litrů, což stačí do města, na lehkou procházku nebo do kanceláře s menším notebookem. Pro víc věcí zvolte větší řady Shater, Moper nebo Sofer.'),
        ('Který batoh Husky vybrat na víkendovou túru?',
         'Na víkend s přespáním se hodí čtyřicetilitrové Curly nebo Capture. Na jednodenní výlet bez spaní stačí Campus s třiceti litry. Pro delší trek s vařením je vhodnější padesátipětilitrový Cruiser.'),
        ('Je Husky vhodný pro školáky?',
         'Pro mladší děti existují řady Jadju, Jikko, Jolly a Jibby od deseti do dvaceti litrů. U starších žáků s objemnými učebnicemi zvažte i modely Office nebo specializované školní batohy s pevnými zády.'),
        ('Jak poznám správný objem batohu?',
         'Podle plánu a podle toho, kolik věcí skutečně nesete. Na den ve městě stačí dvacet litrů, na jednodenní výlet třicet, na víkend čtyřicet a na týden bez podpory kolem padesáti pěti. Větší batoh bývá zbytečně těžký.'),
        ('Má Husky batoh s kapsou na notebook?',
         'Řady označené Office, tedy Shater, Sofer a Moper, jsou určené pro práci a notebook. Přesnou úhlopříčku kapsy ověřte v popisu konkrétního modelu, protože se u jednotlivých kusů liší.'),
        ('Hodí se Peten na kolo?',
         'Ano, malé objemy Peten od deseti do dvaceti litrů patří do kategorie turistika a cyklistika. Nízký objem znamená, že batoh na zádech nepřekáží a při jízdě se nehoupe.'),
        ('Jak vybrat velikost dětského batohu?',
         'Podívejte se na záda dítěte. Batoh nemá sahat nad ramena ani pod pas a plně naložený by neměl vážit víc než zhruba desetinu hmotnosti dítěte. Popruhy se musí dát utáhnout tak, aby batoh neklouzal.'),
        ('Mohu batoh Husky prát v pračce?',
         'Raději ne. Vhodnější je mytí ručně vlažnou vodou s jemným mýdlem, protože pračka a odstřeďování mohou poškodit výztuhy, pěnu v zádech a zipy. Sušte vždy na vzduchu, mimo topení.'),
        ('Čím se Husky liší od Osprey nebo Deuter?',
         'Husky je česká outdoorová značka s širokou nabídkou pro každodenní nošení i výlety. Osprey a Deuter jsou specializované na batohy a nabízejí rozsáhlejší technické řady a velikosti zad pro náročný trek.'),
        ('Je lepší batoh s jedním velkým prostorem, nebo s více kapsami?',
         'Pro město a školu se hodí členěný batoh s kapsou na notebook, penál a drobnosti. Na trek je lepší jedna velká komora s kompresními popruhy a několik vnějších kapes na věci, které potřebujete za chůze.'),
        ('Kdy je dobré batoh vyměnit?',
         'Když se začnou trhat švy u popruhů, zadní polstr ztratí tvar nebo zip přestane držet. Menší vada se dá opravit v krejčovství, ale poškozený nosný pás u těžkého batohu raději neriskujte.'),
        ('Kde porovnám ceny a dostupnost batohů Husky?',
         'Na této stránce vidíte nabídky z českých obchodů. U každého modelu porovnejte barvu, objem a dostupnost velikostí, protože stejný model bývá dostupný v několika variantách.'),
    ],
)

# ------------------------------------------------------------------ new-balance-kopacky
NEW['new-balance-kopacky'] = dict(
    title='New Balance kopačky: Furon, Tekela a 442 podle hráče',
    desc='New Balance kopačky: rychlé Furon, ovládací Tekela a klasické 442. Rozdíly v řadách, povrchy FG, SG, TF a IN, střih a výběr podle postu na hřišti.',
    intro='<p>New Balance v kopačkách stojí na třech jménech. Furon je řada pro rychlé hráče, kteří potřebují zrychlení a lehkou botu. Tekela je určená těm, kdo hrají hlavně s míčem na noze a oceňují jemný dotek. Řada 442 je klasika pro širší okruh hráčů. '
          'Stránka sbírá kopačky této značky z kategorie <a href="/kopacky/">kopačky</a> a ukazuje, jak se jednotlivé řady liší, co znamenají přívlastky Pro, Team, Dispatch, Destroy nebo Elite a jak zvolit podrážku FG, SG, TF či IN a kdy sáhnout po klasickém modelu. Průvodce pomůže i s velikostí, s porovnáním vůči kopačkám Nike, Adidas a Puma a s údržbou, aby vám pár vydržel celou sezónu.</p>',
    guide='<h2>Tři řady, tři způsoby hry</h2>'
          '<p>Na rozdíl od značek, které mají v nabídce desítky názvů, drží New Balance jednoduché členění. Pomůže vám vybrat, ještě než se začnete věnovat povrchu nebo velikosti.</p>'
          + T(['Řada', 'Hlavní myšlenka', 'Komu sedí'], [
              ['Furon', 'rychlost, lehká a přiléhavá bota', 'křídla, útočníci, hráči se zrychlením do prostoru'],
              ['Tekela', 'kontakt s míčem a kontrola', 'středopolaři, tvůrci hry, hráči s přihrávkami po zemi'],
              ['442', 'klasický střih a univerzálnost', 'rekreační hráči, mládež, tréninky a zápasy bez nároků na špičku']]) +
          '<p>Podobné dělení najdete i jinde, ale nejde o pravidlo. Rychlá kopačka může být vhodná i pro obránce, který potřebuje dohnat soupeře, a ovládací pro útočníka, který hraje zády k bráně. Raději proto vybírejte podle pocitu v noze než podle postu.</p>'
          '<h2>Furon: lehká a rychlá</h2>'
          '<p>Furon je v nabídce nejpočetnější. Setkáte se s verzemi V7+ a novější V8, přičemž číslo značí generaci modelu. U starších generací bývá výhodou, že se rozprodávají a dají se najít v širší nabídce barev. Novější verze přináší jemné změny v materiálu a střihu, ale základ zůstává podobný: lehká bota s tenčím svrškem a dobrou stabilitou při změně směru.</p>'
          '<p>Přívlastky za názvem označují úroveň vybavení. Pro je vyšší řada, Team a Dispatch jsou dostupnější a cílí na tréninky i rekreační fotbal, Destroy je zase vizuálně výraznější varianta téhož typu. Přesný popis materiálů vždy zkontrolujte v kartě produktu, protože u jednotlivých ročníků se mění. Obecné pravidlo ale platí: čím vyšší řada, tím tenčí a lehčí svršek a tím méně odolná bota vůči hrubému zacházení na škváře nebo betonu.</p>'
          '<h2>Tekela: kontrola míče</h2>'
          '<p>V katalogu se objevují Tekela Magia, Tekela Magique, Tekela Team a Tekela Elite v provedení Low Laced. Kopačky jsou zaměřené na dotek a čistý kontakt s míčem při přihrávce, zpracování a střele. Ve srovnání s Furon mají zpravidla klidnější charakter: méně agresivní vzhled a důraz na pohodlí. Tvůrčím hráčům, kteří přihrávají vnitřním nártem a vedou míč blízko nohy, sedí tento přístup nejlíp.</p>'
          '<ul><li><strong>Magia, Magique:</strong> názvy variant řady, v nabídce s označením generace V4 nebo V4+.</li>'
          '<li><strong>Team:</strong> dostupnější verze určená na pravidelný trénink a nižší soutěže.</li>'
          '<li><strong>Elite Low Laced:</strong> nižší střih s klasickým šněrováním, bez vysokého nártu.</li></ul>'
          '<h2>Povrchy: FG, SG, TF a IN u New Balance</h2>'
          '<p>New Balance používá stejné zkratky jako ostatní výrobci. V nabídce vidíte pro trávu FG, pro měkký terén SG, pro umělku a škváru TF a pro halu IN. Nově se objevuje i AG pro umělou trávu. Rozhodnutí je jednoduché: kupujte podle hřiště, na kterém trávíte nejvíc času. Pokud hrajete většinu zápasů na rozbředlé trávě, volba SG má smysl, jinak je FG univerzálnější. Turfy s nízkými noppy jsou skvělé na trénink, ale na dobré trávě nedrží při prudkém zatočení.</p>'
          + T(['Označení v názvu', 'Typ podrážky', 'Vhodné použití'], [
              ['FG', 'pevné kolíky', 'zápasy na přírodní trávě'],
              ['SG', 'delší kolíky, často kovové koncovky', 'těžký terén, déšť, blátivé hřiště'],
              ['TF', 'gumové nopy', 'trénink na umělce a tvrdé podložce'],
              ['IN', 'hladká guma', 'hala a sál (podrobněji v kategorii sálové obuvi)']]) +
          '<p>Pokud hledáte kopačky pro celou rodinu, mrkněte i na výběr <a href="/detske-kopacky/">dětské kopačky</a>, protože některé řady New Balance existují i v juniorském provedení.</p>'
          '<h2>Střih a velikost: na co si dát pozor</h2>'
          '<p>New Balance je v běžné obuvi známý nabídkou různých šířek, ale u kopaček se dostupnost šířek omezuje a výsledek závisí na konkrétním modelu. Proto platí obecné pravidlo: zkoušejte s fotbalovými ponožkami, ve stejné hodnotě jako při zápase a v odpoledních hodinách, kdy je noha nejširší. Špička by měla být zhruba o palec od konce boty, aby se prsty při sprintu nepřetlačovaly.</p>'
          '<ul><li><strong>Čtěte popis střihu:</strong> pokud výrobce píše o užším střihu, vezměte raději půl čísla navíc.</li>'
          '<li><strong>Syntetika se přizpůsobí málo:</strong> kopačky s tenkým svrškem se po rozšlapání uvolní jen mírně, proto nekupujte příliš těsné.</li>'
          '<li><strong>Kůže povolí:</strong> přírodní kůže se přizpůsobuje, takže se jí vyplatí volit těsnější velikost.</li>'
          '<li><strong>Šněrování:</strong> klasické šněrování drží nárt pevně, bez něj se hodí kopačky spíše na dotek než na tvrdé zákroky.</li></ul>'
          '<h2>New Balance a ostatní značky</h2>'
          '<p>Pokud se rozhodujete mezi značkami, srovnejte nejen vzhled, ale i střih. <a href="/kopacky-nike/">Nike</a> nabízí užší a lehčí modely pro rychlé hráče, <a href="/kopacky-adidas/">Adidas</a> široký sortiment od klasických až po moderní konstrukce, <a href="/kopacky-puma/">Puma</a> mívá pohodlný přední díl a <a href="/mizuno-kopacky/">Mizuno</a> klade důraz na jemnější kůži. <a href="/joma-kopacky/">Joma</a> a <a href="/kopacky-under-armour/">Under Armour</a> jsou další možnosti pro ty, kdo hledají jiný střih. New Balance se v tomto srovnání zařazuje mezi značky, které nemají tolik modelů, ale každá řada má jasný záměr. Podívejte se i na vybavení kolem hřiště, jako jsou <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a> nebo <a href="/fotbalove-mice/">fotbalové míče</a>.</p>'
          '<h2>Výběr podle postu a stylu hry</h2>'
          '<p>Kopačky nejsou jen otázka povrchu, ale i toho, co děláte s míčem nejčastěji. Brankář kopačky řeší jen okrajově, takže se zaměřte na hráče v poli. Útočník a křídlo ocení lehkost a pevný záběr při prvních krocích, proto vedle sebe srovnejte Furon Pro a Furon Dispatch. Středopolař, který přihrává a řídí hru, bude spokojenější s Tekela, kde jde o kontakt s míčem a pohodlí při dlouhých minutách. Obránce potřebuje hlavně odolnost: přední část boty snáší tvrdé souboje, takže stojí za zvážení dostupnější řada Team místo nejlehčí verze.</p>'
          '<p>Rekreační hráč, který kopaní střídá s tréninkem v hale a na umělce, by měl začít nejuniverzálnější podrážkou a teprve potom řešit design. Zkušenost ukazuje, že boty koupené podle barvy bez ohledu na povrch se často nosí hůř než o třídu nižší model, který sedí na hřiště a na nohu.</p>'
          '<h2>Kdy a jak nakupovat</h2>'
          '<p>Kopačky se obměňují v ročních vlnách. Když vyjde nová generace (například V8 po V7+), starší modely zlevňují a dá se najít stejný střih v širší nabídce barev. Pokud nepotřebujete nejnovější technologii, bývá starší generace rozumná volba. Pozor na úplně poslední velikosti: rozprodávají se obvykle krajní čísla, takže stejný model v běžné velikosti často zbývá jen v jiné barvě nebo povrchu. Nikdy neobětujte povrch podrážky kvůli slevě.</p>'
          '<p>Před koupí ověřte také, zda jde o dospělou nebo juniorskou verzi, protože se liší nejen velikostí, ale i tuhostí podrážky. Dospělé kopačky na dětské noze přidají zbytečnou váhu, juniorské na dospělé noze naopak nevydrží tvrdé zatížení. Chybí-li vám sportovní obuv na trénink mimo hřiště, prohlédněte si i <a href="/treninkova-obuv/">tréninkovou obuv</a>.</p>'
          '<h2>Jak o kopačky pečovat</h2>'
          '<ol><li>Po zápase vyndejte vložky a nechte boty vyschnout při pokojové teplotě, ne na topení.</li>'
          '<li>Hrubé bláto smyjte vlažnou vodou a měkkým kartáčem, nikdy ne v pračce.</li>'
          '<li>Do mokré boty vložte zmuchlané noviny, které vysají vlhkost a drží tvar.</li>'
          '<li>Při tréninku na tvrdé umělce střídejte kopačky s turfy, aby se jemná podrážka neopotřebovala dřív.</li>'
          '<li>Kolíky kontrolujte před každým zápasem, opotřebené a ulomené neodkládejte.</li></ol>'
          '<p>Víc o výběru podle povrchu a o dalších značkách najdete v nadřazené kategorii <a href="/kopacky/">kopačky</a> a v přehledu sportu <a href="/fotbal/">fotbal</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi New Balance Furon a Tekela?',
         'Furon je určený rychlým hráčům, kteří chtějí lehkou přiléhavou botu. Tekela je zaměřená na kontrolu míče a pohodlí. Obě řady se liší charakterem, takže vybírejte podle stylu hry, ne jen podle vzhledu.'),
        ('Co znamená FG, SG, TF a IN u kopaček New Balance?',
         'FG je pevná podrážka pro přírodní trávu, SG pro měkký a rozmoklý terén, TF pro umělku a tvrdý povrch a IN pro halu. U některých modelů najdete i AG, určené pro umělou trávu.'),
        ('Co znamenají přívlastky Pro, Team, Dispatch a Destroy?',
         'Označují úroveň a zaměření modelu v rámci jedné řady. Pro bývá vyšší a lehčí, Team a Dispatch dostupnější pro trénink a rekreační hru, Destroy je jiná varianta téhož základu. Přesný popis materiálů ověřte u produktu.'),
        ('Jsou kopačky New Balance vhodné pro děti?',
         'Některé řady existují i v juniorském provedení. Pro rostoucí nohu zvolte raději levnější a pohodlnou kopačku a ne špičkový model, protože dítě z velikosti brzy vyroste. Podívejte se do výběru dětských kopaček.'),
        ('Jakou velikost kopaček New Balance vybrat?',
         'Podle konkrétní velikostní tabulky výrobce a s fotbalovými ponožkami. Před koncem boty nechte zhruba šířku palce. Syntetika se příliš nerozšlapává, proto nekupujte příliš těsné kopačky.'),
        ('Je lepší kůže, nebo syntetika?',
         'Kůže se přizpůsobí noze a bývá pohodlnější, ale po namočení těžkne a vyžaduje péči. Syntetický svršek je lehčí, odolnější proti vodě a nemění tvar. Volte podle toho, na čem hrajete a jak často.'),
        ('Pro jaký post jsou Furon vhodné?',
         'Typicky pro útočníky a křídla, tedy hráče s rychlými sprinty. Ale hodí se i pro obránce, kteří potřebují zrychlení. Nejde o pravidlo, rozhoduje pohodlí v noze a styl hry.'),
        ('Mohu kopačky TF používat na trávě?',
         'Dá se to, ale není to ideální. Gumové nopy na přírodní trávě málo drží a při prudkém obratu hrozí uklouznutí. TF jsou určené na umělku, škváru a tvrdé podložky, zejména na trénink.'),
        ('Jak dlouho kopačky vydrží?',
         'Záleží na četnosti hry, povrchu a péči. Při pravidelných zápasech a tréninku většinou jednu až dvě sezóny. Střídání dvou párů a správné sušení životnost prodlužují.'),
        ('Čím se New Balance liší od Nike a Adidas?',
         'New Balance má menší sortiment s jasným členěním do tří řad. Nike a Adidas mají širší nabídku modelů a více designových řad. Střih a pocit v noze se liší, proto kopačky vždy zkoušejte.'),
    ],
)

# ------------------------------------------------------------------ ocun-lezecky
NEW['ocun-lezecky'] = dict(
    title='Ocún lezečky: Jett, Striker, Ozone a dětské Ribbit',
    desc='Ocún lezečky a lezecké vybavení: Jett, Striker, Ozone, Havoc, dětské Ribbit a úvazky Flit či Doppler. Střih, šněrování, velikost a výběr podle úrovně.',
    intro='<p>Ocún je česká lezecká značka a její lezečky patří k nejznámějším na tuzemských stěnách. V nabídce se střídají modely Jett a Striker pro stěnu a boulder, Ozone a Havoc pro náročnější lezení a dětské Ribbit pro první kroky. Vedle bot tu najdete také sedací úvazky, dětské úvazky a drobnosti jako gumové náplasti nebo úchyty. '
          'Stránka vybírá zboží této značky z kategorie <a href="/lezecke-boty/">lezečky</a> a vysvětluje, jak poznat správný střih, proč se u lezeček řeší šněrování nebo suchý zip, jak vybrat velikost a co potřebujete kromě bot. Průvodce je psaný pro začátečníky i pro lezce, kteří hledají druhý pár na jiný styl lezení.</p>',
    guide='<h2>Co všechno nese značka Ocún</h2>'
          '<p>Ocún nevyrábí jen lezecké boty. Nabídka značky zahrnuje i sedací a dětské úvazky, hrudní úvazky, startovní sety a příslušenství. Díky tomu se dá celá výbava pro stěnu poskládat z jednoho zdroje, což zjednodušuje výběr velikostí a doplňků.</p>'
          + T(['Druh zboží', 'Příklady z nabídky', 'Kdo ho potřebuje'], [
              ['Lezečky', 'Jett, Striker, Ozone, Havoc, Fury, Renta', 'začátečníci i pokročilí, stěna a skála'],
              ['Dětské lezečky', 'Ribbit', 'děti, které začínají na stěně'],
              ['Sedací úvazky', 'Flit, Mojo, Doppler, Bodyguard', 'sportovní lezení, výcvik, stěna'],
              ['Dětské úvazky', 'Doppler dětský', 'malé děti pod dohledem dospělého'],
              ['Startovní sety', 'Climbing Twist Set', 'nováčci, kteří chtějí kompletní základ'],
              ['Drobnosti', 'Ozone Patch, úchyty a pomůcky', 'údržba boty a domácí stěna']]) +
          '<p>Takto široká nabídka je užitečná hlavně pro začínající lezce. Na první stěně obvykle stačí půjčená výbava, ale po několika návštěvách se vyplatí vlastní boty a sedák. Úvazky a lana najdete také v kategoriích <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky a pomůcky</a> a <a href="/lezecka-lana-a-karabiny/">lana a karabiny</a>.</p>'
          '<h2>Jak číst názvy modelů Jett, Striker, Ozone a Havoc</h2>'
          '<p>Názvy vypadají zdánlivě náhodně, ale mají logiku. Přívlastek na konci často označuje způsob zapínání. LU značí šněrované provedení (lace-up), zatímco QC je varianta s rychlejším zapínáním. Šněrování umožní jemně dotáhnout botu na celé noze, rychlé zapínání ušetří čas mezi lezením, například na stěně nebo při boulderu, kde boty často sundáváte. Jaká verze je u konkrétního kusu, vždy ověřte v popisu produktu.</p>'
          '<ul><li><strong>Jett:</strong> v nabídce ve verzích LU i QC, určený pro lezení na stěně a na skále.</li>'
          '<li><strong>Striker:</strong> šněrovaná lezečka, kterou lze brát jako všestrannou volbu.</li>'
          '<li><strong>Ozone a Havoc:</strong> pokročilejší modely, u kterých stojí za to prostudovat popis střihu a gumy.</li>'
          '<li><strong>Fury:</strong> pánské lezečky pro pokročilé, zaměřené na výkonnější lezení.</li>'
          '<li><strong>Ribbit:</strong> dětské lezečky, v nabídce v několika barvách.</li></ul>'
          '<h2>Střih: neutrální, mírně zahnutý, zahnutý</h2>'
          '<p>Střih ovlivňuje, jak noha v botě stojí na malých stupech. Neutrální bota drží prsty skoro rovně a dovolí delší nošení, proto se doporučuje začátečníkům a na vícedélkové cesty. Mírně zahnutá bota tlačí špičku dolů a hodí se na strmější terén. Silně zahnutá, agresivní bota vyžaduje zkušenost a je určená na převisy a malé chyty. Pro začátek vyberte pohodlnější typ a zkraťte čas, který v botách strávíte tlačením prstů.</p>'
          '<p>Pokud lezete poprvé, dejte přednost botě, která drží nohu pohromadě, ale necítíte v ní bolest. Strmé převisy a malé stupy jsou až později. Čím agresivnější bota, tím víc zatíží prsty a tím rychleji se projeví chyby v technice. Srovnání s dalšími značkami najdete na stránce <a href="/la-sportiva-lezecky/">La Sportiva lezečky</a>.</p>'
          '<h2>Velikost: lezečky se nekupují jako běžné boty</h2>'
          '<p>Lezecká bota má sedět těsně, ale bez bolesti. Prsty jsou lehce pokrčené nebo dosahují na špičku, pata nemá mít vůli a vzadu nesmí vznikat záhyby. Pro začátečníky platí pravidlo, že boty mají být o něco větší než pro pokročilého. Pokud je první pár příliš těsný, lezení se stane nepříjemnou zkouškou a ne zábavou.</p>'
          '<ol><li>Měřte nohu odpoledne, kdy je největší, a zkoušejte s tenkou ponožkou nebo naboso.</li>'
          '<li>Stoupněte si na špičky, ověřte, že pata nevyskakuje.</li>'
          '<li>Zkontrolujte, zda se prsty nepřekrývají tak, že brání krevnímu oběhu.</li>'
          '<li>Počítejte s mírným roztažením: kožené modely povolí víc než syntetické.</li>'
          '<li>Pokud boty koupíte přes internet, ověřte vrácení a vyzkoušejte je v interiéru.</li></ol>'
          '<h2>Pro koho jsou Ocún lezečky</h2>'
          '<p>Ocún má dobré postavení mezi tuzemskými lezci a dětmi, které začínají v lezeckých oddílech. Díky širokému rozsahu zboží je snadné poskládat základ: boty, sedák a základní pomůcky. Zkušený lezec může použít Ocún jako druhý pár na trénink na stěně a lepší boty si nechat na skálu. Pro děti je důležité zvolit malé a lehké boty s měkčím střihem, protože noha dítěte roste rychle a není důvod platit za výkonnostní konstrukci.</p>'
          '<h2>Úvazky Ocún: Flit, Mojo, Doppler, Bodyguard</h2>'
          '<p>Sedací úvazky Flit, Mojo, Doppler a Bodyguard slouží pro sportovní lezení, na stěně a při základním výcviku. Základem je sedací úvazek s nastavitelnými stehenními smyčkami, takže jedna velikost obstojí v různých vrstvách oblečení. Dámský lezecký sedací úvazek má obvykle užší pas a delší smyčky pro boky. Dětské úvazky Doppler a celotělové úvazky jsou určené těm nejmenším, jejichž boky ještě nedrží sedací úvazek.</p>'
          '<ul><li><strong>Nastavitelnost:</strong> stehenní smyčky se mají dát upravit na tenké i silné oblečení.</li>'
          '<li><strong>Uzavírání:</strong> pás musí být zajištěný podle návodu a vždy zkontrolovaný druhou osobou.</li>'
          '<li><strong>Dětský úvazek:</strong> u malých dětí se používá celotělový nebo hrudní úvazek a vždy pod dohledem dospělého.</li>'
          '<li><strong>Životnost:</strong> po pádu nebo po několika letech používání vyměňte úvazek podle pokynů výrobce.</li></ul>'
          '<p>Výběr úvazků napříč značkami je v samostatném přehledu <a href="/lezecky-sedak/">lezecký sedák</a>. Další vybavení, například přilby a lana, najdete v kategorii <a href="/horolezectvi/">horolezectví a ferraty</a>.</p>'
          '<h2>Stěna, boulder, skála: jak se styl lezení promítá do výbavy</h2>'
          '<p>Na boulderu lezete krátké a těžké cesty nad žíněnkou, bez lana a úvazku, takže potřebujete jen boty a pytlík na magnézium. Boty jsou hodně namáhané a často se sundávají, proto se tu hodí rychlé zapínání a těsnější střih. Při lezení s lanem na umělé stěně si naopak pohodlí ceníte víc, protože cesty jsou delší a bota zůstává na noze po dobu celého výstupu včetně jištění. Venku na skále potřebujete botu, která zvládne drsnější povrch a přetrvá nárazy o hranu, a často druhý pár, který nelitujete.</p>'
          '<p>Rozdělit si boty podle stylu je typický krok po prvním roce lezení. Jeden pár slouží na trénink, druhý na projekt. Pokud nechcete investovat do dvou, zvolte všestrannější model a doplňte ho doplňky na péči o botu, jako je Ozone Patch, který chrání opotřebovaná místa.</p>'
          '<h2>Trénink mimo stěnu</h2>'
          '<p>Síla prstů a předloktí je u lezení omezujícím faktorem, proto lezci doplňují stěnu cvičením doma nebo v posilovně. Pomůže hrazda, kruhy a posilovací pomůcky z kategorie <a href="/funkcni-trenink/">funkční trénink a hrazdy</a>. Pro cvičení mimo lezeckou stěnu potřebujete obyčejnou obuv a ne lezečky, vhodnou volbou je <a href="/treninkova-obuv/">tréninková obuv</a>. Pokud trénujete doma, buďte opatrní se zátěží prstů a zvyšujte ji pomalu, šlachy se přizpůsobují déle než svaly.</p>'
          '<h2>Péče o lezečky</h2>'
          '<p>Lezečky jsou citlivé na teplo a vlhkost, takže je nenechávejte v autě na slunci ani v mokrém batohu. Po lezení je vysušte při pokojové teplotě, vyluxujte prach z gumy a před lezením gumu očistěte hadříkem nebo kartáčkem. Čistá guma lépe lne, proto se vyhněte tomu, abyste na ni šlapali po špinavém povrchu před cestou. Když je guma sjetá, můžete botu nechat přezout, což je levnější než nový pár. Nošení v pohodlných botách mezi cestami šetří nejen gumu, ale i nohu.</p>',
    faq=[
        ('Jsou Ocún lezečky vhodné pro začátečníky?',
         'Ano, v nabídce jsou modely pro začátečníky i pro pokročilé. Pro první pár vybírejte neutrálnější střih, který nebolí, a nechte si poradit na stěně, kde mají půjčovnu a vyzkoušíte si několik velikostí.'),
        ('Co znamená LU a QC u lezeček Ocún?',
         'LU označuje šněrovanou verzi a QC variantu s rychlejším zapínáním. Šněrování umožní jemnější utažení, rychlé zapínání šetří čas při častém sundávání bot, například při boulderu.'),
        ('Jak vybrat velikost lezeček?',
         'Zkoušejte odpoledne, boty mají sedět těsně bez bolesti, pata bez vůle a prsty jen lehce pokrčené. Kůže se mírně roztáhne, syntetika méně. Začátečníci volí volnější velikost než pokročilí.'),
        ('Jak poznám správný střih lezeček?',
         'Neutrální střih je nejpohodlnější a hodí se na stěnu a delší lezení. Mírně zahnutý se hodí na strmější terén a silně zahnutý na převisy a pokročilé lezce. Na začátku zvolte pohodlnější typ.'),
        ('Lezou děti v Ribbit?',
         'Ribbit jsou dětské lezečky z nabídky Ocúnu. U dětí je nejdůležitější dobrý tvar a pohodlí, ne agresivní konstrukce, a velikost kontrolovat každou sezónu, protože noha rychle roste.'),
        ('Potřebuji kromě bot také úvazek?',
         'Pro lezení s lanem ano. Na boulderu a základním lezení na stěně u nižších cest se úvazek nepoužívá. Pro lezení s jištěním potřebujete úvazek, jisticí pomůcku a karabinu a naučit se správné jištění.'),
        ('Jak dlouho lezečky vydrží?',
         'Podle četnosti lezení, terénu a péče. Guma se opotřebovává nejvíc na špičce. Pokud je ještě zbytek boty v pořádku, dá se nechat přezout u servisu, což prodlouží život páru.'),
        ('Mohu lezečky prát?',
         'Doporučuje se spíše ruční čištění vlažnou vodou a kartáčkem, bez agresivních čisticích prostředků. Pračka může poškodit lepidlo a tvar boty. Sušte při pokojové teplotě, nikdy na topení.'),
        ('Je dětský úvazek totéž co sedací?',
         'Ne. Malé děti mají užší boky a při pádu by mohly z klasického sedacího úvazku vyklouznout, proto se používají celotělové nebo hrudní úvazky. Používejte je vždy s dohledem zkušeného dospělého.'),
        ('Stačí na boulder jedny lezečky?',
         'Ano, na boulder potřebujete boty, magnézium a ideálně kartáček na chyty. Úvazek ani lano se nepoužívají. Při častém sundávání bot ocení lezec rychlejší zapínání a pohodlně nasazovatelný střih.'),
        ('Kdy dát lezečky přezout?',
         'Když se guma na špičce sjede skoro až k podešvi, ale zbytek boty drží tvar. Přezutí v servisu bývá levnější než nový pár. Pokud je svršek roztržený nebo bota deformovaná, vyplatí se koupit nový model.'),
        ('Čím se liší Ocún od La Sportiva?',
         'Ocún je česká značka s širokou nabídkou pro začátečníky a děti, La Sportiva se zaměřuje na výkonnostní lezení. Rozdíl uvidíte i ve střihu, proto je nejlepší vyzkoušet oboje.'),
    ],
)

# ------------------------------------------------------------------ brankarske-rukavice-detske
NEW['brankarske-rukavice-detske'] = dict(
    title='Brankářské rukavice dětské: velikost, střih a věk',
    desc='Dětské brankářské rukavice: jak změřit ruku, velikosti 4 až 8, rovný nebo rolovaný střih, ochrana prstů, trénink a zápas a značky Reusch, BU1, Adidas.',
    intro='<p>Dětská brankářská rukavice se od dospělé liší víc než jen velikostí. Dlaň je menší, prsty kratší, latex tenčí a lehčí a zápěstní pásek se musí snadno utáhnout malýma rukama. Pro malého brankáře je to rozdíl mezi jistým chytáním a rukavicemi, které padají z ruky. '
          'Tato stránka sbírá modely označené Junior, JR nebo Kids z kategorie <a href="/brankarske-rukavice/">brankářské rukavice</a>. Průvodce vysvětluje, jak změřit ruku dítěte, jak se velikosti vážou k věku, kdy zvolit tréninkový a kdy zápasový pár, zda dětem pomáhá ochrana prstů, a jak o rukavice pečovat, aby vydržely celou sezónu a dítě v nich chytalo s jistotou i radostí.</p>',
    guide='<h2>Jak změřit ruku dítěte</h2>'
          '<p>Velikost rukavic se řídí délkou dlaně, ne věkem. Změřte ji od zápěstí po špičku nejdelšího prstu a obvod dlaně kolem kloubů bez palce. U většiny výrobců odpovídá číslo rukavice přibližně délce ruky v centimetrech zaokrouhlené nahoru, ale přepočet se mezi značkami mírně liší, proto vždy zkontrolujte tabulku konkrétního výrobce. Některé modely, například Blindsave Vault JR, uvádějí velikost rovnou v rozsahu věku, třeba 7 až 9 let nebo 10 až 12 let.</p>'
          + T(['Věk dítěte', 'Orientační velikost', 'Poznámka'], [
              ['5–6 let', '4–5', 'nejmenší děti, hlavně hra a zvyk na rukavice'],
              ['7–8 let', '5–6', 'první tréninky v přípravce'],
              ['9–10 let', '6–7', 'mladší žáci, přechod na pevnější latex'],
              ['11–12 let', '7–8', 'starší žáci, ruka rychle roste'],
              ['13–14 let', '8–9', 'přechod na dospělou řadu, kontrola tabulky']]) +
          '<p>Tabulka je jen orientační. Dvě děti stejného věku mají někdy o dvě čísla jinou dlaň, takže vždy měřte a porovnávejte s tabulkou výrobce. Pokud je dítě mezi velikostmi, zvolte větší jen o půl čísla, ne víc, a vždy vyzkoušejte oba kusy: příliš velká rukavice se na konci prstů ohýbá a míč se ztrácí.</p>'
          '<h2>Proč nekupovat rukavice do zásoby</h2>'
          '<p>U dětí je lákavé koupit o číslo víc, aby rukavice vydržely dvě sezóny. U brankářských rukavic to nefunguje. Prázdný konec prstu bere úchop, rukavice se otáčí na ruce a při zákroku hrozí vyvrknutí prstu. Lepší je koupit levnější pár v přesné velikosti a po sezóně přejít na další. Rozumnější je zvážit, co dítě skutečně potřebuje, a rukavice vybrat podle toho.</p>'
          '<h2>Tréninkové a zápasové dětské rukavice</h2>'
          '<p>Menší děti se v přípravce teprve učí postavení a chytání, proto nepotřebují nejměkčí latex pro nejlepší záběr. Pro ně stačí odolnější tréninkový model, například řady Reusch Attrakt Solid nebo Starter Solid, Adidas Predator Training, Nike Match JR nebo BU1 Light. Starší děti, které hrají soutěže, ocení zápasový pár s měkčí dlaní, jaký nabízejí řady Pure Contact, Predator Match, Copa Match nebo Puma Ultra a King.</p>'
          '<ul><li><strong>Trénink:</strong> odolnější latex, který snese tvrdý povrch a časté chytání, bez ohledu na vzhled.</li>'
          '<li><strong>Zápas:</strong> měkčí dlaň s lepším záběrem, ale rychlejším opotřebením, proto ji nenoste na škváře.</li>'
          '<li><strong>Umělka a škvára:</strong> tvrdý povrch drhne dlaň, takže pro ni mějte samostatný starší pár.</li>'
          '<li><strong>Hala:</strong> na hladké podlaze je latex suchý a čistý, ale pásek musí držet i při šmycích po zemi.</li></ul>'
          '<h2>Střih dlaně pro děti</h2>'
          '<p>Rovný střih má dlaň ze dvou rovných panelů a prsty jsou oddělené bočními vložkami. Dává prostor mezi prsty a je volnější. Rolovaný střih obepíná prsty kolem dlaně a zvyšuje kontakt s míčem, ale vyžaduje přesné velikosti. Negativní střih má švy uvnitř a drží těsněji. Pro nejmenší děti je vhodnější volnější rovný střih, který odpouští chyby. Starší děti, které už vědí, jaký pocit mají rády, si mohou vyzkoušet rolovaný nebo hybridní.</p>'
          '<h2>Ochrana prstů: ano, nebo ne?</h2>'
          '<p>V nabídce se objevují modely označené Fingersave, tedy s výztuhami na hřbetu prstů. Chrání před přepnutím prstu dozadu, což se u brankářů stává. U malých dětí ale prsty rostou a výztuha mění pohyblivost ruky, takže ji vybírejte po dohodě s trenérem. U začátečníků v přípravce většinou stačí obyčejná rukavice, u starších žáků s tvrdšími střelami může pomoci. Žádná výztuž nenahradí správnou techniku a zahřátí prstů před tréninkem.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Dětské rukavice nabízí široká škála značek. Reusch, <a href="/znacka/uhlsport/">Uhlsport</a> a <a href="/znacka/select/">Select</a> patří mezi specialisty na brankářské vybavení. <a href="/znacka/adidas/">Adidas</a>, <a href="/znacka/nike/">Nike</a> a <a href="/znacka/puma/">Puma</a> mají junior řady odvozené od hráčských modelů. Dále najdete <a href="/znacka/bu1/">BU1</a>, <a href="/znacka/rinat/">Rinat</a>, <a href="/znacka/kensis/">Kensis</a>, <a href="/znacka/freez/">Freez</a> a Blindsave. Přehled jednotlivých značek najdete na stránkách <a href="/brankarske-rukavice-adidas/">brankářské rukavice Adidas</a> a <a href="/brankarske-rukavice-bu1/">brankářské rukavice BU1</a>.</p>'
          '<h2>Jak zkontrolovat, že rukavice sedí</h2>'
          '<p>Správně sedící dětská rukavice obepíná ruku bez tlaku a prsty končí těsně u špičky rukavice, nejvýš s mezerou široké jako nehet. Zkuste s dítětem několik jednoduchých zkoušek: zavřít pěst, rozevřít prsty, chytit míč oběma rukama a pustit ho na zem. Pokud se látka na hřbetu nabírá do záhybů, je rukavice velká. Pokud dítěti zbělají konečky prstů nebo se mu nedaří dlaň vystrčit, je malá.</p>'
          '<ul><li><strong>Zápěstí:</strong> pásek se zapíná bez velké síly a rukavice při zvednutí paže neklouže dolů.</li>'
          '<li><strong>Palec:</strong> volně se ohýbá a nenarazí na šev uvnitř.</li>'
          '<li><strong>Dlaň:</strong> latex je čistý a pružný, ne tvrdý, popraskaný ani vyleštěný.</li>'
          '<li><strong>Váha:</strong> dětská ruka se unaví rychle, proto je lehká konstrukce důležitější než množství výztuh.</li></ul>'
          '<h2>Časté chyby rodičů při nákupu</h2>'
          '<p>První chybou bývá velikost do zásoby, kterou jsme zmínili výše. Druhou je výběr podle motivu: rukavice s oblíbenou barvou nebo klubovým znakem vypadají skvěle, ale pokud mají tvrdý latex a nepohodlný pásek, dítě je nebude chtít nosit. Třetí chyba je koupě dospělého modelu v nejmenší velikosti. Dospělé řady mívají širší prsty a tužší dlaň, a ačkoliv číslo souhlasí, střih na dětskou ruku nepasuje. Čtvrtá je zanedbání péče: rukavice zapomenuté mokré v tašce po jednom tréninku ztvrdnou a ztratí záběr.</p>'
          '<h2>Kdy přejít na dospělé rukavice</h2>'
          '<p>Přechod nenastává podle věku, ale podle velikosti ruky. Když dítě dosáhne velikosti osmičky nebo devítky a prsty dětského modelu už jsou krátké, je čas zkusit dospělou řadu, ideálně v užším střihu. Mladší výběry mezi 12 a 14 lety často střídají dětské a dospělé velikosti. Vyplatí se vyzkoušet oba typy, protože střih a tuhost dlaně se liší. Dospělou řadu najdete v nadřazené kategorii <a href="/brankarske-rukavice/">brankářské rukavice</a>.</p>'
          '<h2>Jak rukavice navlékat, prát a sušit</h2>'
          '<ol><li>Před tréninkem rukavice navlhčete, aby latex ožil, a pak nasaďte a utáhněte pásek.</li>'
          '<li>Po tréninku je opláchněte vlažnou vodou a jemně promněte dlaně, žádné drhnutí kartáčem.</li>'
          '<li>Nechte je schnout volně na vzduchu, mimo topení a slunce.</li>'
          '<li>Nikdy nepoužívejte pračku ani aviváž, ničí latex a lepidlo.</li>'
          '<li>Skladujte je volně, ne stlačené v tašce s kopačkami.</li></ol>'
          '<p>Hned na začátku si ověřte, že dítě opravdu rukavice dokáže samo obléct a upnout. Pokud mu s tím musí pomáhat dospělý, volte jednodušší pásek na suchý zip.</p>'
          '<h2>Co ještě patří do výbavy malého gólmana</h2>'
          '<p>Vedle rukavic potřebuje dítě pohodlné <a href="/detske-kopacky/">dětské kopačky</a> podle povrchu, chrániče z kategorie <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a> a míč odpovídající věku, který najdete mezi <a href="/fotbalove-mice/">fotbalovými míči</a>. Mladším hráčům obvykle sedí lehčí míč velikosti 4, starším velikosti 5. Pokud je dítě zapálené do fotbalu a chce vyzkoušet i hru v poli, může si rukavice střídat s běžnou výbavou, přehled najdete v kategorii <a href="/fotbal/">fotbal</a> a v kategorii <a href="/kopacky/">kopačky</a>.</p>',
    faq=[
        ('Jakou velikost dětských brankářských rukavic vybrat?',
         'Změřte délku dlaně od zápěstí po špičku nejdelšího prstu a porovnejte ji s tabulkou výrobce. Číslo rukavice odpovídá přibližně délce ruky v centimetrech. Věk je jen orientační, nekupujte rukavice do zásoby.'),
        ('Od kolika let mohou děti chytat v rukavicích?',
         'Rukavice se hodí již pro děti v přípravce, kolem pěti až šesti let. Pro tuto věkovou skupinu jsou nejlepší lehké a odolné rukavice se snadným suchým zipem a bez výztuh prstů.'),
        ('Mají mít děti rukavice s ochranou prstů?',
         'Není to nutné. Ochrana prstů může pomoci starším žákům s tvrdšími střelami, u malých dětí ale omezuje pohyblivost. Zeptejte se trenéra, který zná styl hry a zátěž konkrétního dítěte.'),
        ('Jaký je rozdíl mezi tréninkovými a zápasovými rukavicemi?',
         'Tréninkový pár má odolnější latex, zápasový měkčí a lepivější. Měkká dlaň se rychleji opotřebuje, proto ji používejte jen na zápasy na trávě a pro trénink mějte starší nebo levnější pár.'),
        ('Mohu rukavice prát v pračce?',
         'Ne. Pračka a aviváž ničí latex i lepidlo. Opláchněte je vlažnou vodou, jemně vymačkejte a nechte volně schnout na vzduchu mimo topení.'),
        ('Proč dítěti rukavice klouzou?',
         'Příčinou bývá velká velikost nebo opotřebený latex. Rukavice před tréninkem lehce navlhčete, zkontrolujte pásek a velikost. Pokud je dlaň hladká a tvrdá, je čas na nový pár.'),
        ('Jak dlouho rukavice vydrží?',
         'Podle četnosti tréninku a povrchu. Na tvrdé umělce se latex ztrácí za několik týdnů, na trávě vydrží sezónu. Pokud dítě stále roste, hlídejte spíš velikost než opotřebení.'),
        ('Jsou drahé rukavice pro děti nutné?',
         'Pro začátečníky ne. Dítě poznáte podle toho, že se rukavice učí používat a chytá míč jistě. Teprve při soutěžích má smysl koupit zápasový pár a trénink si nechat na odolnější.'),
        ('Mohou děti chytat v rukavicích na škváře nebo na betonu?',
         'Dá se to, ale dlaň se rychle ničí. Pro tvrdý povrch mějte starší pár a zápasový si nechte na trávu a na hlídaný povrch, aby latex vydržel co nejdéle.'),
        ('Jak rukavice vyzkoušet před sezónou?',
         'Nechte dítě zavřít pěst, rozevřít prsty a chytit míč. Prsty mají končit těsně u špičky, pásek se má zapnout bez námahy. Pokud se na hřbetu tvoří záhyby, zkuste menší velikost.'),
        ('Kdy ztratí rukavice záběr?',
         'Latex ztvrdne a vyleští se po vyschnutí bez oplachu nebo po tvrdém povrchu. Opláchnutí vlažnou vodou po tréninku záběr udrží déle. Pokud je dlaň hladká a popraskaná, vyměňte pár.'),
        ('Čím se dětské rukavice liší od dospělých?',
         'Mají menší dlaň, kratší prsty, lehčí konstrukci a snadnější uzavírání. Přechod na dospělou řadu vychází na dospívání, kdy ruka dosáhne velikosti zhruba osmičky až devítky.'),
    ],
)
