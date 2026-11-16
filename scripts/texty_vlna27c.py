"""sporteka.cz — wave 27c (16. 11. 2026): long texts for balancni-podlozky-bosu, medicinbaly, zebriny, stojany-na-cinky.
General true facts only, no prices. Brands linked only where they exist in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ balancni-podlozky-bosu
NEW['balancni-podlozky-bosu'] = dict(long=True,
    title='BOSU a balanční podložky: typy, velikosti a použití',
    desc='Balanční polokoule typu BOSU, vzduchové čočky, pěnové podložky a ježci. Jak vybrat podle cviku a porovnat nabídky českých obchodů.',
    intro='<p>Balanční podložky mění pevnou podlahu v povrch, na kterém se tělo musí pořád vyrovnávat. Nejznámější je polokoule typu BOSU s plochou plošinou a nafukovací kopulí. Vedle ní se prodávají vzduchové balanční čočky, pěnové podložky a malé polokoule s výstupky, kterým se říká ježci. Používají se ve fitness, při přípravě na lyžování nebo míčové sporty i ve fyzioterapii. Sporteka porovnává nabídky českých obchodů; samotný nákup proběhne u obchodu, jehož nabídku si vyberete.</p>'
          '<p>Nejvíc modelů v katalogu má Sedco, dále ' + B(('insportline', 'Insportline'), ('merco', 'Merco'), ('hms', 'HMS'), ('gymbeam', 'GymBeam')) + ', Sportago, Trinfit, Lifefit nebo Pure2Improve. BOSU je ochranná známka jednoho výrobce, ostatní značky prodávají stejný princip pod názvem balance trainer nebo balanční polokoule. Balanční desky, čočky na stání a další pomůcky na stabilitu najdete v nadřazené kategorii <a href="/balancni-pomucky/">balanční pomůcky</a>.</p>',
    guide='<h2>Jaké balanční podložky existují</h2>'
          '<p>Všechny pomůcky v této kategorii dělají totéž: zmenšují nebo rozhýbávají opěrnou plochu. Liší se ale tím, jak moc a jakým způsobem. Pro první nákup se vyplatí vědět, co který typ umí.</p>'
          + T(['Typ', 'Typický rozměr', 'Na co se hodí'], [
              ['Balanční polokoule (typ BOSU)', 'průměr zhruba 55–65 cm, kopule vysoká kolem 20–25 cm', 'dřepy, výpady, kliky, plank, poskoky, celotělový trénink'],
              ['Vzduchová balanční čočka', 'průměr zhruba 30–36 cm', 'stoj na jedné noze, cvičení kotníku, aktivní sezení na židli'],
              ['Pěnová balanční podložka', 'obdélník kolem 40 × 33 cm až 50 × 40 cm, tloušťka 5–7 cm', 'začátečníci, rehabilitace kotníku a kolene, klečení'],
              ['Ježci (malé polokoule s výstupky)', 'průměr zhruba 16–20 cm, často v páru', 'stoj na dvou bodech, opora rukou při klicích, stimulace chodidel']]) +
          '<p>Kdo s balančním tréninkem začíná, má nejvíc z pěnové podložky nebo čočky: jsou levnější, malé a dají se schovat do šuplíku. Polokoule je univerzálnější, ale zabírá víc místa a vyžaduje trochu zkušenosti.</p>'
          '<h2>Balanční polokoule typu BOSU</h2>'
          '<p>Polokoule má dvě strany. Spodní tvoří tuhá plastová plošina s protiskluzovou úpravou, horní nafukovací kopule z pryže nebo PVC. Když stojí kopulí nahoru, je to nejběžnější poloha pro dřepy, výpady, poskoky a stoj na jedné noze. Obrácená plošinou nahoru se chová mnohem nestabilněji a používá se hlavně na kliky, podpory a plank, kde se o okraje plošiny opírají ruce. Stát na obrácené polokouli je cvik pro zkušené a v domácích podmínkách k němu není důvod.</p>'
          '<p>Některé modely mají na plošině úchyty, jiné se prodávají s gumovými expandery s držadly, které se připnou k okraji. V nabídce je to vidět na sériích Balance Trainer od Sedco nebo na modelech Dome od Insportline. Expandery rozšiřují počet cviků o přítahy a tlaky, jejich odpor ale bývá nízký.</p>'
          '<p>Kopule se nafukuje pumpičkou, která bývá v balení. Výrobce obvykle uvádí, do jaké výšky se má nafouknout. Tvrdší kopule víc pruží, měkčí se pod chodidlem víc boří. Vzduch časem trochu uniká, proto výšku občas změřte a dohustěte. Při výběru se dívejte na průměr, nosnost uvedenou výrobcem, materiál kopule a na to, zda je spodní strana plošiny pogumovaná, aby po podlaze nejezdila.</p>'
          '<h2>Vzduchové balanční čočky</h2>'
          '<p>Čočka je plochý nafukovací polštář s ventilem. Jedna strana bývá hladká, druhá pokrytá drobnými výstupky, které masírují chodidlo nebo zlepšují přilnavost. Míru nestability lze měnit množstvím vzduchu, takže si obtížnost doladíte sami; doporučené nafouknutí obvykle uvádí výrobce. Výhodou je malý rozměr a hmotnost, takže čočku vezmete s sebou na chatu nebo na hřiště.</p>'
          '<p>Kromě cvičení se čočka používá jako sedák na kancelářskou židli, kde nutí pánev k drobným pohybům. Takové sezení je fajn jako zpestření, ale neočekávejte od něj zázraky a celý den na čočce neseďte. V katalogu se objevují čočky Sedco, Fitforce Balance Cushion, Sportago FitSit nebo masážní podložky Durian.</p>'
          '<h2>Pěnové balanční podložky</h2>'
          '<p>Pěnová podložka je kvádr z měkké pružné pěny, například z TPE nebo PVC. Nic se nefoukne, nic nepraskne a podložka nedělá hluk, takže se hodí do bytu. Stoj na ní je méně náročný než na polokouli, a proto je ideální pro začátek, pro seniory a pro cviky doporučené fyzioterapeutem po zranění kotníku nebo kolene. V nabídce jsou například Merco Balance Pad TPE, Sportago Skim o rozměru 40 × 33 × 5 cm nebo podložky Theraband a Pure2Improve.</p>'
          '<p>Tloušťka rozhoduje o obtížnosti. Tenčí podložka kolem pěti centimetrů je stabilnější, silnější se víc boří. Pěna časem měkne a na místech, kde se stojí nejčastěji, se může trvale promáčknout. Skladujte ji naplocho a mimo přímé slunce.</p>'
          '<h2>Ježci a malé polokoule</h2>'
          '<p>Ježek je malá polokoule s výstupky, obvykle o průměru 16 až 20 cm. Prodává se jednotlivě i v páru. Položí se plochou stranou na zem a staví se na něj jednou nohou, případně oběma nohama na dva kusy. Obrácený výstupky dolů slouží jako nestabilní opora pro ruce při klicích. V nabídce najdete ježky Jakobs Senso Balance Igel nebo Lifefit Erizo. Děti je používají i jako součást překážkové dráhy, vždy ale pod dohledem dospělého.</p>'
          '<h2>Jak vybrat podle cíle</h2>'
          '<ul><li><b>Začínám s tréninkem rovnováhy:</b> pěnová podložka nebo čočka. Přidají nestabilitu, ale pády z nich nehrozí.</li>'
          '<li><b>Chci celotělový trénink doma:</b> polokoule typu BOSU, ideálně s pevnou plošinou a deklarovanou nosností.</li>'
          '<li><b>Připravuji se na lyže, snowboard nebo míčové sporty:</b> polokoule a ježci, na kterých se dají cvičit dřepy, výpady a doskoky.</li>'
          '<li><b>Mám doporučení od fyzioterapeuta:</b> řiďte se jeho radou. Obvykle začíná pěnová podložka a čočka.</li>'
          '<li><b>Hledám něco na sezení u stolu:</b> vzduchová čočka nebo <a href="/gymnasticke-mice/">gymnastický míč</a>.</li></ul>'
          '<h2>Kde cvičit a kolik místa potřebujete</h2>'
          '<p>Balanční podložka sama mnoho místa nezabere, ale kolem ní musí být volno. Počítejte aspoň s metrem a půl na každou stranu, protože při ztrátě rovnováhy se sestupuje do strany nebo dozadu. V blízkosti nesmí být ostré hrany nábytku, skleněné dveře ani radiátor. Na začátku se vyplatí cvičit vedle zdi, opěradla židle nebo kuchyňské linky, kde se dá rychle chytit.</p>'
          '<p>Podklad má být rovný a neklouzavý. Polokoule položená na volném koberečku může i s cvičencem ujet. Na hladkou dlažbu nebo parkety dejte pod ni gumovou nebo jógovou podložku. Cvičit se dá naboso i v obuvi; naboso chodidlo lépe cítí povrch, v obuvi s pevnou podrážkou jsou zase některé cviky stabilnější. Pantofle a ponožky na hladké kopuli kloužou.</p>'
          '<h2>Časté chyby a bezpečnost</h2>'
          '<ul><li><b>Příliš těžký začátek.</b> Stoj na jedné noze na pěnové podložce je pro mnoho lidí výzva sám o sobě. Skoky na polokouli patří až na konec postupu.</li>'
          '<li><b>Cvičení v únavě.</b> Rovnováha se s únavou zhoršuje rychle, proto balanční cviky zařazujte na začátek tréninku.</li>'
          '<li><b>Zavřené oči bez jistoty.</b> Stoj se zavřenýma očima obtížnost výrazně zvyšuje. Zkoušejte ho jen vedle opory.</li>'
          '<li><b>Ignorovaná nosnost.</b> U polokoulí výrobci uvádějí maximální zatížení. Při poskocích působí na kopuli větší síla než při klidném stoji.</li>'
          '<li><b>Ostré předměty.</b> Nafukovací kopule i čočka se mohou propíchnout o hrany nábytku, třísky nebo kamínky.</li>'
          '<li><b>Rehabilitace bez rady.</b> Po úrazu kotníku, kolene nebo po operaci postupujte podle fyzioterapeuta, který určí, kdy a na čem začít.</li></ul>'
          '<h2>Jak trénink postupně ztěžovat</h2>'
          '<p>Kdo s balancí začíná v lednu jako součástí nového tréninkového plánu, může postupovat jednoduše. Nejdřív stoj na obou nohou na pěnové podložce, dokud nebude klidný aspoň půl minuty. Potom stoj na jedné noze, následně stejný stoj s pomalými pohyby paží, s otáčením hlavy nebo s chytáním míčku. Teprve potom přicházejí dřepy a výpady, nejdřív na podložce, pak na polokouli. Na každý krok si klidně dejte týden nebo dva. Stačí deset až patnáct minut dvakrát až třikrát týdně, ideálně jako součást rozcvičky.</p>'
          '<p>Na polokouli se dá cvičit i posilování trupu: sed s nohama ve vzduchu, plank s předloktími na kopuli nebo most s chodidly na kopuli. Tyto cviky jsou bezpečnější, protože se při nich nepadá z výšky, a hodí se i pro ty, kdo stoj na kopuli zatím nezvládají.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Nafukovací podložky čistěte vlhkým hadříkem s trochou jemného mýdla, rozpouštědla materiál poškozují. Nenechávejte je na slunci, u topení ani v mrazu na balkoně, protože PVC i pryž stárnou a praskají. Ventil uzavírejte zátkou a zátku neztraťte, náhradní se shání obtížně. Pěnové podložky ukládejte naplocho, aby se nezkroutily, a jednou za čas je opláchněte vodou.</p>'
          '<p>K balančním podložkám se hodí <a href="/joga-a-podlozky/">podložka na cvičení</a> jako protiskluzový podklad. Další pomůcky na trénink trupu najdete mezi <a href="/pilates-pomucky/">pilates pomůckami</a> a ve <a href="/funkcni-trenink/">funkčním tréninku</a>. Než se rozhodnete, porovnejte u konkrétní nabídky rozměry, nosnost, obsah balení (pumpička, expandery) a podmínky vrácení; tyto údaje se mezi obchody liší i u stejného modelu.</p>',
    faq=[
        ('Co je BOSU?', 'Balanční polokoule s pevnou plastovou plošinou a nafukovací kopulí. BOSU je obchodní značka, jiní výrobci stejný typ pomůcky prodávají jako balance trainer nebo balanční polokouli.'),
        ('Jaký je rozdíl mezi balanční čočkou a pěnovou podložkou?', 'Čočka je nafukovací a nestabilitu u ní měníte množstvím vzduchu. Pěnová podložka se nefukuje, je tichá a stabilnější, a proto se hodí na úplný začátek a pro rehabilitaci.'),
        ('Na kterou stranu polokoule se má stoupat?', 'Pro stoj, dřepy a výpady kopulí nahoru. Plošinou nahoru se polokoule používá hlavně na kliky a podpory, protože stoj na ní je velmi nestabilní.'),
        ('Jak moc nafouknout polokouli typu BOSU?', 'Podle návodu výrobce, který obvykle uvádí výšku kopule. Tvrdší kopule víc pruží, měkčí se víc boří. Výšku občas zkontrolujte, protože vzduch pomalu uniká.'),
        ('Hodí se balanční podložka pro seniory?', 'Ano, ale nejlépe pěnová podložka a cvičení vedle pevné opory. Při potížích s rovnováhou, závratích nebo po úrazu je dobré cvičení probrat s lékařem nebo fyzioterapeutem.'),
        ('Cvičit naboso, nebo v botách?', 'Obojí jde. Naboso chodidlo lépe vnímá povrch, pevná obuv dává víc jistoty při dřepech a poskocích. Nevhodné jsou ponožky a pantofle, které kloužou.'),
        ('Dá se balanční čočka použít na sezení?', 'Ano, na židli se dá sedět i na ní. Berte to ale jako zpestření, ne jako náhradu pravidelného pohybu, a sezení na čočce střídejte s běžným.'),
        ('Kolik místa potřebuji?', 'Samotná podložka je malá, ale kolem ní nechte zhruba metr a půl volna. Na začátku cvičte u zdi nebo u opěradla židle, abyste se mohli zachytit.')])

# ------------------------------------------------------------------ medicinbaly
NEW['medicinbaly'] = dict(long=True,
    title='Medicinbaly a slam bally: typy, hmotnost a výběr',
    desc='Medicinbaly, slam bally a wall bally od 1 do 25 kg. Jak vybrat typ, hmotnost a materiál podle cviku; porovnání nabídek českých obchodů.',
    intro='<p>Medicinbal je plný míč se zátěží, se kterým se hází, chytá, nosí nebo tluče o zem. Patří k nejstarším tréninkovým pomůckám a dnes se prodává ve třech hlavních podobách: klasický medicinbal, měkký wall ball na házení proti zdi a neodskakující slam ball na údery o podlahu. Kategorie zahrnuje hmotnosti od jednoho kilogramu pro rehabilitaci až po pětadvacetikilové slam bally. Sporteka porovnává nabídky českých obchodů a nakupujete přímo u obchodu podle svého výběru.</p>'
          '<p>Velkou část nabídky tvoří řady značky ' + B(('hms', 'HMS')) + ' (medicinbaly NK a NKU, wall bally WLB a slam bally PSB a PST), dále ' + B(('insportline', 'Insportline'), ('merco', 'Merco')) + ', Sedco, Fitforce, Merc sport, Master nebo Power System. Míče jsou součástí širší kategorie <a href="/funkcni-trenink/">funkční trénink</a>, kde najdete i další pomůcky pro cvičení celého těla.</p>',
    guide='<h2>Tři druhy míčů a jak se liší</h2>'
          '<p>V e-shopech se názvy často míchají a slam ball se klidně prodává jako „lékařský míč“. Pro výběr je ale podstatné, jak se míč chová při dopadu a jak se drží v rukou.</p>'
          + T(['Typ', 'Povrch a výplň', 'Odskok', 'Běžné hmotnosti', 'Hlavní použití'], [
              ['Klasický medicinbal', 'pryž, syntetická nebo pravá kůže', 'pryžový odskakuje, kožený málo', '1–10 kg', 'hody s partnerem, rotace, cviky na břicho, rehabilitace'],
              ['Medicinbal s úchyty', 'pryž, dvě pevné rukojeti', 'odskakuje', '3–10 kg', 'rotace, výpady, dřepy, tlaky nad hlavu'],
              ['Wall ball', 'měkký šitý obal ze syntetické kůže, uvnitř výplň', 'téměř žádný', '2–15 kg', 'dřep s výhozem na terč na zdi'],
              ['Slam ball', 'silná pryžová skořepina, uvnitř písek nebo granulát', 'žádný, míč „padne“', '2–25 kg i víc', 'údery o zem, nošení, přehazování přes rameno']]) +
          '<p>Rozměr nemá s hmotností pevný vztah. Wall bally bývají velké, kolem 35 cm v průměru, i když váží jen pár kilogramů. Klasické pryžové medicinbaly jsou menší a tvrdší. Slam bally rostou s hmotností, ty nejtěžší už se drží obtížně.</p>'
          '<h2>Klasický medicinbal</h2>'
          '<p>Pryžový medicinbal je pevný, často s vroubkovaným povrchem, a při dopadu odskakuje. Hodí se na hody do zdi s chytáním, přihrávky s partnerem, rotace trupu, sedy-lehy s míčem nebo kliky s rukou na míči. Kožené a syntetické medicinbaly jsou měkčí, mají šitý obal a odskakují méně; jsou příjemnější při chytání. Varianty s úchyty, které má v nabídce například HMS, se snáz drží při rotacích a cvicích nad hlavou.</p>'
          '<p>U pryžového míče pozor na odskok. Když s ním mrštíte o zem, může vyskočit zpátky do obličeje. Na údery o podlahu proto patří slam ball, ne klasický medicinbal.</p>'
          '<h2>Wall ball</h2>'
          '<p>Wall ball je měkký míč, se kterým se dělá cvik stejného jména: hluboký dřep a z něj plynulý výhoz na terč vysoko na zdi, chycení a návrat do dřepu. V CrossFitu je standardem míč 20 liber (asi 9 kg) pro muže a 14 liber (asi 6 kg) pro ženy a terč ve výšce 10, respektive 9 stop, tedy zhruba 3 m a 2,7 m. Pro začátek doma je ale rozumné vzít lehčí míč.</p>'
          '<p>Na wall ball potřebujete pevnou zeď bez oken, svítidel a obrazů a dostatečnou výšku stropu. V běžném bytě se proto cvik dělá obtížně, vhodnější je garáž, tělocvična nebo venkovní zeď. Měkký obal míče tlumí náraz, ale zeď i tak trpí, a sousedé za tenkou příčkou rány uslyší. Kontrolujte švy: jakmile se začnou párat, výplň se sype a míč ztrácí tvar.</p>'
          '<h2>Slam ball</h2>'
          '<p>Slam ball se zvedne nad hlavu a celou silou hodí o zem. Díky výplni z písku nebo granulátu po dopadu zůstane ležet, takže ho cvičenec musí zvednout ze země. Je to dobrý trénink výbušnosti, ale i důvod hlídat techniku zvedání: záda rovná, pohyb z kyčlí a kolen. Silná pryžová skořepina vydrží venku i na betonu a mnoho modelů je voděodolných; někteří výrobci, například HMS, to uvádějí přímo v názvu.</p>'
          '<p>Podlaha musí ránu vydržet. Ideální je beton nebo pryžová podlaha v garáži či posilovně. Dlažba může prasknout, plovoucí podlaha se poškodí a v paneláku rány přenesou zvuk do celého domu. Doma pomůže silná pryžová deska nebo puzzle podložka, ani ta ale zvuk zcela neutlumí.</p>'
          '<h2>Jakou hmotnost zvolit</h2>'
          '<p>Při práci s míčem jde hlavně o rychlost. Když je míč moc těžký, pohyb se zpomalí a z výbušného cviku se stane pomalé zvedání. Proto se vyplatí začít lehčím kusem a zvýšit zátěž, až technika sedí. Následující hodnoty jsou jen orientační:</p>'
          '<ul><li><b>Rehabilitace a cvičení seniorů:</b> 1–2 kg, u nejlehčích často měkké míče, které se dobře chytají.</li>'
          '<li><b>Hody s partnerem a rotace trupu:</b> 2–5 kg. Míč musí letět rychle a dát se bezpečně chytit.</li>'
          '<li><b>Wall ball na začátek:</b> zhruba 4–6 kg pro ženy, 6–9 kg pro muže.</li>'
          '<li><b>Slam ball na začátek:</b> zhruba 6–10 kg. Těžší kusy přes 15 kg slouží spíš k nošení a přehazování.</li></ul>'
          '<p>Pokud trénujete v domácnosti víc lidí nebo chcete různé cviky, dávají smysl dva míče: lehčí na hody a rotace a těžší na slam nebo nošení. Jeden univerzální kus bývá kompromis, se kterým se nepracuje dobře ani při jednom.</p>'
          '<h2>Materiál a zpracování</h2>'
          '<p>Nový pryžový míč může zpočátku vonět gumou, pach se obvykle vyvětrá. U slam ballů hledejte texturovaný povrch, protože hladká pryž po zpocení klouže. Ventil nebo plnicí otvor by měl být zapuštěný a pevně uzavřený. U wall ballů se dívejte na dvojité švy a na to, jak je obal vyztužený v místech, kde se míč dotýká zdi. U kožených medicinbalů počítejte s tím, že venku na vlhku stárnou rychleji než pryžové.</p>'
          '<h2>Kde a jak cvičit</h2>'
          '<p>Kolem sebe potřebujete prostor, ve kterém míč nikoho a nic nezasáhne. Pro rotační hody do zdi stačí pár metrů a pevná stěna, pro hody s partnerem volné místo mezi vámi a za vámi. Slam ball potřebuje pevnou podlahu a volný prostor kolem nohou, protože míč po dopadu může mírně odkulit. Venku na trávě nebo na hřišti je s míčem nejvíc svobody, jen ho potom nechte uschnout.</p>'
          '<p>Typický domácí trénink s míčem může vypadat takto: dřep s míčem u hrudníku, rotační hody do zdi na každou stranu, slam nebo hod nad hlavou, výpady s míčem a na závěr cvik na břicho s míčem v rukou. Tři kola po deseti opakováních dvakrát až třikrát týdně je solidní start pro ty, kdo začínají s pohybem po Novém roce. Mezi tréninky nechte den volna.</p>'
          '<h2>Bezpečnost a časté chyby</h2>'
          '<ul><li>Pryžový medicinbal nemlaťte o zem. Odskočí nepředvídatelně a může zasáhnout obličej.</li>'
          '<li>Slam ball nehazujte těsně před špičky nohou. Dopad mírně před tělem je bezpečnější pro kotníky i záda.</li>'
          '<li>Míč neberte z podlahy s kulatými zády. Dřepněte si k němu, zvlášť u těžších kusů.</li>'
          '<li>Hody s partnerem dělejte v klidu a domluvte se na signálu. Míč, který letí na nepřipraveného člověka, umí zranit prsty.</li>'
          '<li>Vysoké výhozy nedělejte pod lustrem a u oken.</li>'
          '<li>Zátěž nezvyšujte jen proto, že nový míč vypadá lehce. Rozhodující je rychlost a čistota pohybu.</li></ul>'
          '<h2>Medicinbal v rehabilitaci</h2>'
          '<p>Lehké medicinbaly mají místo i ve fyzioterapii, například při nácviku úchopu, koordinace nebo stability trupu. Zvolený cvik i hmotnost by ale měl určit fyzioterapeut, který zná váš zdravotní stav. Po úrazu ramene, zápěstí nebo zad nezačínejte hody na vlastní pěst.</p>'
          '<h2>Co porovnávat v nabídce</h2>'
          '<p>U míčů se stejnou hmotností se nabídky liší víc, než se zdá. Podívejte se na průměr, protože ten určuje, jak se míč drží a chytá. U slam ballů zjistěte, zda je povrch hladký, nebo vroubkovaný, a zda výrobce uvádí odolnost proti vodě. U wall ballů je důležitý materiál obalu a provedení švů. Hmotnost těžších kusů se může od deklarované mírně lišit, což u domácího tréninku obvykle nevadí. Těžké míče se posílají jako samostatné balíky, takže se vyplatí porovnat i dopravu. Pokud nevíte, jakou hmotnost zvolit, kupte nejdřív lehčí kus a těžší přidejte později.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Pryžové míče stačí otřít vlhkým hadříkem, kožené a syntetické obaly jen lehce navlhčeným, aby se do švů nedostala voda. Ukládejte je na zem nebo do nízkého regálu, ne do výšky, odkud by mohly spadnout. Na slunci a v mrazu pryž tvrdne a praská. U slam ballu, ze kterého se začíná sypat písek, je čas na výměnu.</p>'
          '<p>Míč dobře doplní <a href="/kettlebelly/">kettlebelly</a>, <a href="/zatezove-vesty/">zátěžová vesta</a> nebo <a href="/posilovaci-gumy/">posilovací gumy</a>. Pozor na záměnu s nafukovacím <a href="/gymnasticke-mice/">gymnastickým míčem</a>, který se někdy prodává pod podobným názvem. Při porovnávání nabídek kontrolujte skutečnou hmotnost, průměr a typ míče; samotná cena za kus bez těchto údajů mnoho neřekne.</p>',
    faq=[
        ('Jaký je rozdíl mezi medicinbalem a slam ballem?', 'Klasický pryžový medicinbal při dopadu odskakuje a hodí se na hody a chytání. Slam ball má silnou pryžovou skořepinu s pískem uvnitř, neodskakuje a je určený na údery o zem.'),
        ('Co je wall ball?', 'Velký měkký míč se šitým obalem, se kterým se z dřepu hází na terč na zdi. Téměř neodskakuje a dobře se chytá.'),
        ('Jak těžký medicinbal koupit na začátek?', 'Na hody a rotace stačí 2–5 kg, na wall ball zhruba 4–6 kg pro ženy a 6–9 kg pro muže, na slam ball 6–10 kg. Hodnoty jsou orientační; míč musí jít hodit rychle a technicky čistě.'),
        ('Můžu slam ball používat v bytě?', 'Jde to jen omezeně. Rány se přenášejí do konstrukce domu a dlažba nebo plovoucí podlaha se může poškodit. Vhodnější je garáž, sklep s betonem nebo venkovní plocha, v bytě aspoň silná pryžová deska.'),
        ('Proč slam ball neodskakuje?', 'Uvnitř je volná výplň z písku nebo granulátu, která pohltí energii dopadu. Míč proto zůstane ležet a je potřeba ho zvednout.'),
        ('Je medicinbal vhodný pro rehabilitaci?', 'Lehké medicinbaly kolem jednoho až dvou kilogramů se při rehabilitaci používají. Cviky a hmotnost ale určí fyzioterapeut, zvlášť po úrazu nebo operaci.'),
        ('Jak velký je wall ball?', 'Obvykle kolem 35 cm v průměru, a to i u lehčích hmotností. Velký objem usnadňuje chytání. Přesný průměr najdete v popisu konkrétního míče.'),
        ('Jak medicinbal čistit?', 'Pryžový otřete vlhkým hadříkem, kožený nebo syntetický jen lehce navlhčeným. Nenechávejte ho na slunci ani v mrazu.')])

# ------------------------------------------------------------------ zebriny
NEW['zebriny'] = dict(long=True,
    title='Žebřiny (ribstole): montáž na zeď, rozměry a výběr',
    desc='Žebřiny a ribstole ze dřeva i kovu, s hrazdou, rozpěrné i dětské sestavy. Jak je ukotvit do zdi a porovnat nabídky českých obchodů.',
    intro='<p>Žebřiny, kterým se často říká také ribstole, jsou rám s vodorovnými příčkami připevněný ke zdi. Známe je z tělocvičen, doma ale fungují stejně dobře: na protahování, visy, zvedání nohou, shyby na přidané hrazdě i jako prolézačka pro děti. Zaberou jen pár desítek centimetrů od zdi a vydrží roky. Sporteka porovnává nabídky českých obchodů, žebřiny si pak objednáte přímo u obchodu, který vám vyhovuje.</p>'
          '<p>V nabídce jsou žebřiny značky ' + B(('insportline', 'Insportline')) + ' (řady Directline, Shapemar, Dualmar nebo Steadyline), dále Benchk, Master, Marbo, Physionics, Kometa a Evergym. Objevují se i dětské sestavy se skluzavkou a doplňky jako lavice nebo bradla na žebřiny. Hrazdy a samostatná bradla najdete v nadřazené kategorii <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</p>',
    guide='<h2>Typy žebřin</h2>'
          '<p>Základní konstrukce se léta nemění, liší se hlavně uchycení a výbava. Podle toho, kde budou žebřiny stát a kdo na nich bude cvičit, se dá výběr rychle zúžit.</p>'
          + T(['Typ', 'Uchycení', 'Pro koho a kam'], [
              ['Nástěnné žebřiny', 'kotví se do zdi několika držáky nahoře a dole', 'domácí posilovna, dětský pokoj, nejčastější volba'],
              ['Žebřiny s hrazdou', 'nástěnné, nahoře vysunutá nebo zavěšená hrazda', 'shyby, visy, zvedání nohou'],
              ['Rozpěrné žebřiny', 'rozepřené mezi podlahou a stropem, bez vrtání do zdi', 'byty, kde nejde nebo nesmí vrtat do stěny'],
              ['Venkovní žebřiny', 'zapuštěné do země nebo na vlastní základně', 'zahrada, dětské hřiště'],
              ['Dětské sestavy', 'žebřina se skluzavkou, kruhy, lanem nebo žebříkem', 'pohybové hry dětí doma']]) +
          '<h2>Rozměry a co si změřit</h2>'
          '<p>Běžné domácí žebřiny jsou vysoké zhruba 2 až 2,5 metru a široké 60 až 90 cm. Příčky bývají od sebe zhruba patnáct centimetrů, přesnou rozteč uvádí výrobce. Výrobci uvádějí rozměry v názvu, například 240 × 80 cm. Při výběru změřte světlou výšku místnosti: nad horní příčkou a hlavně nad hrazdou musí zůstat místo na hlavu při shybu. Zkontrolujte i to, kudy vedou okna, dveře a radiátor, protože žebřiny potřebují rovnou plochu zdi celou svou šířkou.</p>'
          '<p>Rám stojí několik centimetrů od zdi, aby se mezi příčky a stěnu vešla špička nohy a prsty při úchopu. Před žebřinami nechte volný prostor aspoň na délku těla, protože při visu nebo zvedání nohou se cvičí čelem od stěny.</p>'
          '<h2>Dřevo, nebo kov</h2>'
          '<p>Klasické žebřiny jsou dřevěné. Boční nosníky bývají z borovice nebo smrku, příčky z tvrdšího dřeva, často z buku nebo jasanu, protože musí vydržet zatížení i tření rukou. Lakované dřevo je příjemné na dotek a v dětském pokoji působí přirozeně. Kovové žebřiny z ocelových profilů s práškovou barvou jsou tenčí, v nabídce se objevují i v bílé nebo grafitové barvě a někdy kombinují kovový rám s bukovými příčkami. Pro venkovní použití se hodí jen modely k tomu určené, s impregnovaným dřevem nebo pozinkovanou či ošetřenou ocelí.</p>'
          '<h2>Montáž na zeď</h2>'
          '<p>Montáž je nejdůležitější část celého nákupu. Žebřiny drží na několika kotvách a při visu nebo shybech na ně působí síly, které výrazně přesahují samotnou hmotnost cvičence. Hrazda vysunutá od zdi navíc funguje jako páka: horní kotvy se snaží ze zdi vytrhnout, dolní naopak tlačí do stěny. Proto záleží na tom, z čeho je zeď.</p>'
          '<ul><li><b>Beton a plná cihla.</b> Nejlepší podklad. Stačí kvalitní hmoždinky dostatečné délky a odpovídající vruty nebo kotevní šrouby.</li>'
          '<li><b>Děrované cihelné bloky.</b> Běžné v novostavbách. Potřebují hmoždinky pro duté materiály s dlouhou rozpěrnou částí nebo chemickou kotvu se sítkem. Vrtá se bez příklepu, aby se nerozbily tenké stěny dutin.</li>'
          '<li><b>Pórobeton.</b> Měkký materiál, ve kterém běžné hmoždinky snadno povolí. Použijte hmoždinky určené pro pórobeton nebo chemickou kotvu.</li>'
          '<li><b>Sádrokarton.</b> Sám o sobě žebřiny neunese. Kotvit se musí do nosné zdi za ním nebo do zesílené konstrukce připravené při stavbě.</li>'
          '<li><b>Dřevostavba.</b> Kotví se do nosných sloupků nebo do zesílení ve stěně, ne jen do desky opláštění.</li></ul>'
          '<p>Hmoždinky přibalené k žebřinám nemusí odpovídat vaší zdi. Zkontrolujte, pro jaký materiál jsou určené, a případně je nahraďte vhodnými podle doporučení výrobce kotevní techniky. Před vrtáním si detektorem ověřte, že ve zdi nevedou elektrické kabely ani trubky, a rám srovnejte vodováhou. Pokud si nejste jistí materiálem zdi nebo kotvením, svěřte montáž odborníkovi; vypadlé žebřiny jsou vážné riziko úrazu. Nosnost uvedená výrobcem platí pro správně ukotvený rám, ne pro jakoukoli zeď.</p>'
          '<h2>Montáž krok za krokem</h2>'
          '<ol><li>Zjistěte materiál zdi, nejlépe zkušebním vývrtem na skrytém místě nebo podle projektu domu.</li>'
          '<li>Detektorem zkontrolujte, kudy vedou kabely a trubky, a označte si je tužkou.</li>'
          '<li>Přiložte rám, vyrovnejte ho vodováhou a označte otvory pro všechny držáky.</li>'
          '<li>Vrtejte vrtákem o průměru podle hmoždinky, otvory vyfoukejte nebo vysajte od prachu.</li>'
          '<li>Osaďte hmoždinky nebo chemickou kotvu a u chemie dodržte dobu vytvrzení.</li>'
          '<li>Rám přišroubujte, dotáhněte a před prvním cvičením zkuste opatrný vis, zda se nic nehýbe.</li></ol>'
          '<h2>Rozpěrné žebřiny bez vrtání</h2>'
          '<p>Rozpěrné žebřiny se upnou mezi podlahu a strop pomocí nastavitelného rozpěrného mechanismu, podobně jako některé dětské prolézačky. Hodí se do pronájmů, kde majitel nepovolí vrtání do zdi. Strop ale musí být pevný, ideálně betonový. Pod podhledem ze sádrokartonu nebo pod podkrovím s tenkým obkladem rozpěrné žebřiny spolehlivě nedrží. Zkontrolujte rozsah výšek, pro který je rám určený, a dotažení pravidelně kontrolujte, protože při cvičení a změnách teploty mechanismus povoluje.</p>'
          '<h2>Příslušenství</h2>'
          '<p>Žebřiny se dají rozšířit o řadu doplňků. Nejčastější je hrazda, buď pevná součást rámu, nebo zavěšovací, která se nasadí na libovolnou příčku. Bradla na žebřiny umožňují dipy a zvedání nohou ve vzporu. Lavice na žebřiny se jedním koncem zavěsí na příčku a slouží na šikmé sedy-lehy nebo jako skluzavka pro děti. Některé řady, například Insportline Directline, nabízejí i stůl nebo lavici, které se k žebřinám připojí. Dětské sestavy mívají kruhy, šplhací lano, provazový žebřík nebo skluzavku. Pod žebřiny se vyplatí dopadová žíněnka nebo aspoň silná podložka.</p>'
          '<h2>Co se na žebřinách cvičí</h2>'
          '<ul><li>volný vis a vis s pokrčenými koleny, které protahují záda a posilují úchop,</li>'
          '<li>zvedání kolen a nohou ve visu na posílení břicha,</li>'
          '<li>shyby na hrazdě a australské shyby s nohama na zemi,</li>'
          '<li>protahování zadní strany stehen, lýtek a hrudníku s oporou o příčku,</li>'
          '<li>kliky s rukama na příčce, které jsou lehčí než kliky na zemi,</li>'
          '<li>cviky s <a href="/posilovaci-gumy/">posilovacími gumami</a> zavěšenými na příčku v různé výšce.</li></ul>'
          '<p>Žebřiny se tradičně používají i ve fyzioterapii. Pokud je chcete využít po úrazu nebo kvůli bolestem zad, poraďte se s fyzioterapeutem, které cviky a v jakém rozsahu jsou pro vás vhodné. Vis zatěžuje ramena a není vhodný pro každého.</p>'
          '<h2>Žebřiny pro děti</h2>'
          '<p>Pro děti jsou žebřiny jedna z nejlepších věcí do pokoje: lezou, visí, houpou se a přirozeně posilují. Bezpečnost ale stojí na dospělých. Rám musí být ukotvený stejně pečlivě jako u dospělých, protože děti se houpou a skáčou. Pod žebřiny patří měkká dopadová plocha, kolem nesmí být ostré hrany nábytku a doplňky jako kruhy a lano by měly mít bezpečné uchycení. Malé děti by měly lézt pod dohledem a jen do výšky, ze které pád nehrozí vážným zraněním. Dětské sestavy, například od Kometa, Evergym nebo dalších výrobců, mají často zaoblené hrany a pestré barvy.</p>'
          '<h2>Bezpečnost a údržba</h2>'
          '<ul><li>Po prvních týdnech používání kotvy a šrouby znovu dotáhněte, potom je kontrolujte zhruba jednou za čtvrt roku.</li>'
          '<li>Dřevěné příčky prohlížejte, zda nejsou prasklé nebo naštípnuté. Poškozenou příčku vyměňte.</li>'
          '<li>Nepřekračujte nosnost uvedenou výrobcem a počítejte s tím, že švihové pohyby zatěžují rám víc.</li>'
          '<li>Lakované dřevo čistěte vlhkým hadříkem, kovové díly otírejte od potu, aby nekorodovaly.</li>'
          '<li>Venkovní žebřiny pravidelně ošetřujte podle návodu, dřevo na slunci a v dešti šedne a praská.</li></ul>'
          '<h2>Jak vybrat</h2>'
          '<p>Nejdřív si ujasněte, kde budou žebřiny stát a z čeho je zeď; tím se často vyřadí polovina nabídky. Pak zvolte výšku podle stropu, šířku podle místa a materiál podle vzhledu a použití. Pokud plánujete shyby, hledejte model s pevnou hrazdou nebo počítejte s dokoupením zavěšovací. Pro celé tělo doplní žebřiny <a href="/posilovaci-veze/">posilovací věž</a> nebo <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a> jako kruhy. U nabídek porovnávejte rozměry, nosnost, materiál příček, obsah balení včetně kotev a dobu dodání. Žebřiny přicházejí v dlouhém a těžkém balíku, proto si zjistěte i to, jak je obchod doručuje.</p>'
          '<p>Pro start v novém roce se žebřiny hodí právě tím, že nevyžadují žádné nastavování. Stačí si každý den na pár minut zavěsit, protáhnout se a postupně přidávat cviky. Výsledky závisí na pravidelnosti víc než na vybavení.</p>',
    faq=[
        ('Jaký je rozdíl mezi žebřinami a ribstolemi?', 'Žádný. Ribstole je starší označení převzaté ze švédštiny, obchody používají oba názvy pro stejný výrobek.'),
        ('Do jaké zdi se dají žebřiny připevnit?', 'Nejlépe do betonu nebo plné cihly. Děrované cihly a pórobeton vyžadují speciální hmoždinky nebo chemickou kotvu. Do samotného sádrokartonu žebřiny nepatří, kotví se do nosné zdi za ním.'),
        ('Kolik váhy žebřiny unesou?', 'Záleží na modelu a hlavně na ukotvení. Řiďte se nosností uvedenou výrobcem a myslete na to, že hrazda a švihové cviky zatěžují kotvy víc než klidný vis.'),
        ('Dají se žebřiny namontovat bez vrtání?', 'Ano, existují rozpěrné žebřiny, které se upnou mezi podlahu a strop. Strop ale musí být pevný a rozpěrný mechanismus je potřeba pravidelně dotahovat.'),
        ('Jak vysoké žebřiny zvolit?', 'Podle výšky stropu. Běžné modely měří zhruba 2 až 2,5 metru. Nad hrazdou nechte místo na hlavu při shybu.'),
        ('Jsou lepší dřevěné, nebo kovové žebřiny?', 'Dřevěné s příčkami z tvrdého dřeva, například buku, jsou klasika, příjemné na úchop. Kovové jsou subtilnější a odolnější proti poškození. Na zahradu patří jen modely určené pro venkovní použití.'),
        ('Od kolika let mohou děti na žebřiny?', 'Pevný věk se uvést nedá. Batolata a malé děti by měly lézt jen pod dohledem dospělého a nad měkkou dopadovou plochou. Řiďte se doporučením výrobce sestavy.'),
        ('Pomáhají žebřiny na bolest zad?', 'Vis a protahování mohou být součástí cvičení pro záda, nejsou ale vhodné pro každého. Při bolestech zad se nejdřív poraďte s lékařem nebo fyzioterapeutem.')])

# ------------------------------------------------------------------ stojany-na-cinky
NEW['stojany-na-cinky'] = dict(long=True,
    title='Stojany na činky a kotouče: typy, nosnost a výběr',
    desc='Stojany na jednoručky, stromy na kotouče, nástěnné držáky os i stojany na velkou činku. Nosnost a průměr trnů; porovnání nabídek českých obchodů.',
    intro='<p>Stojan na činky drží domácí posilovnu v pořádku a chrání podlahu, prsty i kotníky. Kotouče rozházené po zemi jsou nejčastější příčinou zakopnutí a poškozené podlahy. Kategorie zahrnuje stojany na jednoručky, stromy na kotouče, pojízdné vozíky, nástěnné držáky na osy a kotouče i dvojice stojanů, do kterých se odkládá velká činka při dřepu nebo benchpressu. Sporteka porovnává nabídky českých obchodů a objednávka proběhne přímo u vybraného obchodu.</p>'
          '<p>V nabídce jsou stojany ' + B(('hms', 'HMS'), ('insportline', 'Insportline'), ('gymbeam', 'GymBeam'), ('merco', 'Merco')) + ', dále Marbo, Virtufit, Trinfit, Hop-sport, Sedco, Gorilla Sports nebo 4FIZJO. Samotné činky, osy a kotouče najdete v nadřazené kategorii <a href="/cinky-a-kotouce/">činky a kotouče</a>. Pod výpisem popisujeme, jak vybrat stojan podle typu kotoučů, místa a podlahy.</p>',
    guide='<h2>Přehled typů</h2>'
          '<p>Než začnete vybírat, sepište si, co přesně chcete uložit: kolik párů jednoruček, kolik kotoučů a jakého průměru otvoru, kolik os a jak dlouhých. Teprve podle toho dává smysl srovnávat stojany.</p>'
          + T(['Typ', 'K čemu slouží', 'Na co se dívat'], [
              ['Stojan na jednoručky', 'páry jednoruček v řadách na jedné až třech policích', 'počet párů, šířka polic, nosnost'],
              ['Věžový stojan (stacker)', 'jednoručky uložené svisle nad sebou', 'malý půdorys, vhodné hlavně pro šestihranné činky'],
              ['Strom na kotouče', 'kotouče na trnech kolem středového sloupku', 'průměr a délka trnů, stabilita'],
              ['Pojízdný stojan na kotouče', 'kotouče na vozíku s kolečky', 'brzdy, nosnost, rovná podlaha'],
              ['Nástěnné držáky', 'kotouče nebo osy pověšené na zdi', 'typ zdi, nosnost držáku, kotvy'],
              ['Držák na osy', 'olympijské osy vodorovně na zdi nebo svisle ve stojanu', 'počet míst, délka os'],
              ['Stojany na velkou činku', 'opora osy při dřepu a benchpressu', 'rozsah výšek, nosnost, šířka základny']]) +
          '<h2>Průměr trnů: 30, nebo 50 mm</h2>'
          '<p>Kotouče se vyrábějí ve dvou hlavních systémech. Takzvané standardní kotouče mají otvor kolem 30 mm (někteří výrobci uvádějí 25 nebo 31 mm) a patří k lehčím domácím činkám. Olympijské kotouče mají otvor 50 až 51 mm a nasazují se na olympijské osy dlouhé obvykle 220 cm. Stojan na kotouče musí mít trny odpovídající vašim kotoučům. Kotouč s velkým otvorem na tenkém trnu sice drží, ale volně se houpe a škrábe; malý otvor se na silný trn nevejde vůbec.</p>'
          '<p>Některé stojany řeší obojí. Například model Insportline PR50 je podle popisu určený pro kotouče s otvorem 30 i 50 mm. Zkontrolujte také délku trnů. Bumper kotouče z pryže jsou mnohem silnější než litinové, takže se jich na stejný trn vejde méně. Pokud máte doma kotouče obou typů, změřte si jejich tloušťku a sečtěte ji.</p>'
          '<h2>Stojany na jednoručky</h2>'
          '<p>Klasický stojan na jednoručky má dvě nebo tři šikmé police, na kterých leží činky v párech vedle sebe. Šikmé uložení usnadňuje odebírání a police s prolisy nebo pryžovými vložkami brání odkutálení. Výrobci uvádějí počet párů a celkovou nosnost, například desítky až stovky kilogramů. Spočítejte si skutečnou hmotnost všech činek, které chcete uložit, a nechte rezervu na další nákupy. Rozhodující je i délka polic: činky s velkými kulatými kotouči zaberou víc místa než kompaktní šestihranné.</p>'
          '<p>Věžové stojany, jako je GymBeam Stacker nebo stojany Virtufit, ukládají činky nad sebou a hodí se do malých místností. Nastavitelné jednoručky se šroubovacími nebo zacvakávacími závažími mají obvykle vlastní kolébku a do běžného stojanu se nehodí. Dvojité stojany na jednoručky, třeba Insportline Ratus s dvaceti pozicemi, se hodí pro větší sady.</p>'
          '<h2>Stromy a organizéry na kotouče</h2>'
          '<p>Strom na kotouče je svislý sloupek s několika trny po stranách. Zabere málo místa a kotouče jsou po ruce. Je ale potřeba hlídat stabilitu. Těžké kotouče patří na spodní trny, lehčí nahoru, a stojan nakládejte rovnoměrně z obou stran. Pokud z jedné strany sundáte všechny kotouče a druhou necháte plnou, může se lehčí konstrukce převrhnout.</p>'
          '<p>Kombinované organizéry, například HMS Premium nebo stojany Marbo řady MH-S, nesou kotouče i osy a někdy háčky na doplňky. Hodí se, když chcete mít celou výbavu na jednom místě. Pojízdné stojany s kolečky, jako HMS STR32, se dají přesunout k místu cvičení, zato potřebují rovnou podlahu a brzdy nebo aretaci.</p>'
          '<h2>Nástěnné držáky</h2>'
          '<p>Držáky na zeď šetří podlahu. Na kotouče se používají trny přišroubované ke zdi, na osy vodorovné hřebenové držáky s několika místy nebo svislé stojany, do kterých se osa zasune koncem. V nabídce jsou například vodorovné držáky na šest os s nosností do 180 kg nebo sady nástěnných držáků HMS na kotouče a osy.</p>'
          '<p>Na montáž platí totéž co u žebřin. Do betonu a plné cihly stačí kvalitní hmoždinky, děrované cihly a pórobeton potřebují kotvy pro tyto materiály a sádrokarton sám o sobě kotouče neunese. Držáky na kotouče se montují nízko nad podlahu, aby se těžké kotouče nemusely zvedat do výšky. Pro vodorovné uložení olympijské osy počítejte s volnou zdí širší, než je délka osy, aby šla bezpečně vyndat.</p>'
          '<h2>Stojany na velkou činku</h2>'
          '<p>Samostatné stojany na činku (squat stands) jsou dva nezávislé sloupky nebo jeden spojený rám s nastavitelnými držáky. Odkládá se do nich osa před dřepem a po něm, v kombinaci s lavicí také při benchpressu. V katalogu se objevují například Trinfit Rack HX2 a HX3, stojany 4FIZJO, Gorilla Sports nebo Thunder. Výšku nastavíte čepem po krocích, nosnost uvádí výrobce.</p>'
          '<p>Samostatné stojany nejsou klec. Ne všechny mají bezpečnostní ramena, která by zachytila činku při nepovedeném opakování, a dva oddělené stojany se při nárazu osy mohou posunout. Těžké dřepy a tlaky proto cvičte s dopomocí, s pojistkami, pokud je konstrukce nabízí, a s rozumnou zátěží. Pro samostatné cvičení s velkou zátěží je bezpečnější silová klec mezi <a href="/posilovaci-stroje/">posilovacími stroji</a>. K tlakům vleže budete potřebovat <a href="/posilovaci-lavice/">posilovací lavici</a>.</p>'
          '<h2>Podlaha a umístění</h2>'
          '<p>Plně naložený stojan soustředí na malou plochu velkou hmotnost. Strom s kotouči může vážit přes sto kilogramů a plný stojan na jednoručky i víc. Na dřevěné nebo plovoucí podlaze proto pod stojan dejte pryžovou desku, která tlak rozloží a zachytí kotouč, kdyby vyklouzl. Ve starších domech s trámovými stropy se vyplatí stavět těžké vybavení blíž k nosné zdi.</p>'
          '<p>Kolem stojanu nechte prostor na odebírání. U stromu na kotouče aspoň krok na každou stranu, u stojanu na jednoručky místo na dřep před ním. Pokud doma bývají děti, stojan umístěte tak, aby na něj nemohly lézt, a těžké kusy dávejte vždy dolů. Na nejvyšší polici patří nejlehčí činky.</p>'
          '<h2>Jak naplánovat úložný prostor</h2>'
          '<p>Domácí posilovna obvykle začíná jedním párem jednoruček a pár kotouči, po roce ale výbava naroste. Při plánování si nakreslete půdorys místnosti a vyznačte, kde se bude cvičit a kde ukládat. Stojany patří ke zdi mimo prostor, kde se pracuje s velkou činkou, aby se o ně osa při dřepu nebo mrtvém tahu nezachytila. Jednoručky mějte blízko lavice, ať je nemusíte nosit přes celou místnost. Kotouče ukládejte co nejblíž místu, kde se nakládají na osu. Pokud je místa málo, kombinujte svislé řešení: strom na kotouče, věžový stojan na jednoručky a držák na osy na zeď. Na podlaze tak zůstane prostor na samotné cvičení.</p>'
          '<p>Před nákupem si sepište, kolik kusů jakého druhu máte a kolik plánujete dokoupit. Stojan, který je plný hned první den, brzy přestane stačit a kotouče skončí znovu na zemi.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Stojan s trny na 30 mm pro olympijské kotouče, nebo naopak.</li>'
          '<li>Nerovnoměrné zatížení stromu na kotouče, po kterém se konstrukce převrhne.</li>'
          '<li>Nástěnný držák v pórobetonu na běžných hmoždinkách.</li>'
          '<li>Stojan na jednoručky s krátkými policemi, kam se celá sada nevejde.</li>'
          '<li>Spoléhání na samostatné stojany na činku při těžkém dřepu bez pojistek a bez dopomoci.</li>'
          '<li>Těžké kotouče v úrovni hlavy nebo na horních trnech.</li></ul>'
          '<h2>Údržba</h2>'
          '<p>Šrouby a spoje po sestavení dotáhněte a po několika týdnech je zkontrolujte znovu. Lakovaný kov stačí otírat od prachu a potu, odřená místa přetřete, aby nezačala korodovat. Pryžové vložky a krytky na trnech se časem opotřebují; když chybějí, kov škrábe kotouče. V nevytápěné garáži nebo sklepě hlídejte vlhkost, protože rezaví stojan i nechromované kotouče.</p>'
          '<p>Pokud domácí posilovnu teprve zařizujete, začněte jedním typem stojanu podle toho, čeho máte nejvíc, a ostatní dokupujte s rozšiřováním výbavy. K činkám se hodí také <a href="/kettlebelly/">kettlebelly</a>, které se ukládají na podlahu nebo do nízkého regálu. U nabídek porovnávejte nosnost, rozměry, průměr trnů, obsah balení a hmotnost zásilky; stojany přicházejí ve velkých a těžkých krabicích.</p>',
    faq=[
        ('Jaký průměr trnů má mít stojan na kotouče?', 'Podle vašich kotoučů. Standardní mají otvor kolem 30 mm, olympijské 50–51 mm. Některé stojany mají trny nebo adaptéry pro oba systémy.'),
        ('Kolik unese stojan na činky?', 'Nosnost uvádí výrobce a u domácích stojanů se pohybuje od desítek po stovky kilogramů. Sečtěte hmotnost všeho, co chcete uložit, a nechte si rezervu.'),
        ('Je lepší stojan na zem, nebo držák na zeď?', 'Nástěnný držák šetří podlahu, ale potřebuje pevnou zeď a správné kotvy. Stojan na zem lze přesunout a nevyžaduje vrtání, zabere však místo.'),
        ('Proč se strom na kotouče převrací?', 'Nejčastěji kvůli nerovnoměrnému zatížení nebo těžkým kotoučům nahoře. Těžké kusy dávejte dolů a nakládejte i vykládejte z obou stran rovnoměrně.'),
        ('Nahradí stojany na činku silovou klec?', 'Ne úplně. Samostatné stojany nemusí mít bezpečnostní ramena, takže těžké dřepy a benchpress na nich cvičte s dopomocí. Klec nebo stojany s pojistkami jsou bezpečnější.'),
        ('Vejdou se nastavitelné jednoručky do běžného stojanu?', 'Obvykle ne. Nastavitelné jednoručky mají vlastní kolébku nebo stojan od výrobce. Běžné stojany jsou dělané pro pevné činky.'),
        ('Kam umístit stojan v bytě?', 'Na pevnou rovnou podlahu, ideálně na pryžovou desku a blíž k nosné zdi. Nechte kolem místo na odebírání a těžké kusy ukládejte dolů, zvlášť pokud doma bývají děti.'),
        ('Jak dlouhou zeď potřebuji na držák olympijských os?', 'Pánská olympijská osa měří 220 cm, dámská 201 cm. Pro vodorovné uložení počítejte s volnou zdí o něco delší, aby se osa dala bezpečně vyndat.')])
