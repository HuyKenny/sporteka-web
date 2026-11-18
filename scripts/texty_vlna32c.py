"""sporteka.cz — wave 32c (18. 11. 2026): long texts for brasny-na-kolo, kosiky-na-kolo, cyklisticke-batohy,
nepromokave-ponozky, potitka, suspenzory.
General true facts only, no prices, no product counts. Load limits and mounting systems are quoted only as examples from the
makers' own data and the reader is always sent to the label of the exact model. Suspensories are described as sports
protective gear, not as a medical device; no promise of full protection, a doctor after a hard blow. Back protectors in
backpacks only with the norm name (EN 1621-2, levels 1 and 2) and a pointer to the label of the exact model. Brands linked only
if present in src/texts/znacky.json (or the wave 32 brand list), the rest plain text.

Sources:
- ortlieb.com (about us, quick-lock mounting pages, QL3.1 datasheet): founded 1982 in Nuremberg, HQ in Heilsbronn since 1997,
  bags welded instead of sewn; QL1 / QL2.1 / QL3.1, QL3.1 max. 9 kg per pannier, QL1/QL2/QL2.1 bags fit QL3.1 rails
- topeak.com "QuickTrack": trunk bags slide onto MTX / RX racks; Omni QuickTrack adapter for rack widths 90-120 mm
- klickfix.com and retailer data (Rose, Bike24): handlebar adapters 22-26 mm and 31.8 mm, typically max. 7 kg; combined limit =
  the lower of adapter and basket; Doggy handlebar models about 7 kg, rack baskets 8-10 kg depending on the variant
- Racktime Snapit / Snapit 2.0 adapter plates (rosebikes.com, bike-components.de): max. 12 kg
- basil.com "about": bicycle shop in Silvolde 1934, basket import from 1976, company in Ulft (NL)
- deuter.com: Aircomfort mesh back on a spring-steel frame (Race Air 10, 3 l hydration compatible, rain cover); Attack 20
  recommended body height 170-195 cm; SL = women's fit
- Evoc / Blue Tomato product data: back protectors certified to EN 1621-2 level 1 or level 2 (level 2 = higher absorption)
- sealskinz.com (what is a waterproof sock, product care, FAQ, Hydrostop pages): outer layer, Aquasealz hydrophilic membrane,
  inner wicking layer; wash inside out below 40 °C on hand/wool program, drip dry, no radiator, low tumble dry allowed;
  trim toenails, check shoes for stones and thorns; Hydrostop = silicone-free elastic taping inside the cuff; sizes S-XL
- DexShell retailer data: three layers with the Porelle membrane
- shockdoctor.com "Cup fit guide": waist measured about 1 inch above the hips, size up between sizes, cup snug without
  pinching or shifting, youth cups smaller and shaped differently, hockey cups worn with hockey compression shorts
- Retailer data on Twins GPS1 / Fairtex GC2: Thai metal groin guards, steel cup with a leather cover and laces
- Wimbledon dress code (si.com, redbull.com): headbands and wristbands must be white like the rest of the clothing
- Women's "Jill" hockey shorts with pelvic protector and Velcro sock tabs (Warrior, Bauer, Shock Doctor listings)
Left out (not verifiable): DexShell founding year, IP ratings of Ortlieb panniers, ISO 11243 load classes, Deuter Attack
certification level, exact rules of individual combat-sport federations, potítko fibre blends of individual brands.
"""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ brasny-na-kolo
NEW['brasny-na-kolo'] = dict(long=True,
    title='Brašny na kolo na nosič, rám, řídítka i pod sedlo',
    desc='Brašny na kolo na nosič, rám, řídítka i pod sedlo a sady na bikepacking. Systémy uchycení, objem, vodotěsnost a jak náklad rozložit.',
    intro='<p><strong>Brašna na kolo</strong> přenese náklad ze zad na kolo. Podle místa uchycení se dělí na boční brašny na zadní nebo přední nosič, horní brašny na nosič, rámové brašny, malé brašničky na horní rámovou trubku, podsedlové brašny a brašny na řídítka. Pro bikepacking, tedy cestování bez nosiče, se vyrábějí velké rolovací vaky na sedlovku, rámové brašny přes celý trojúhelník rámu a role na řídítka. Na odpolední vyjížďku stačí brašnička na duši a klíče, na týdenní cestu se balí celá sestava.</p>'
          '<p>Na Sportece jsou vedle sebe nabídky českých obchodů, takže u každé brašny vidíte, kdo ji právě prodává. V kategorii najdete brašny Ortlieb, Topeak, Acepac, Basil, Vaude nebo Woho a také '
          + B(('rockbros', 'Rockbros'), ('deuter', 'Deuter'), ('force', 'Force')) +
          '. Brašny patří do sekce <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>, kde jsou i samotné nosiče.</p>',
    guide='<h2>Typy brašen podle místa na kole</h2>'
          '<p>Nejdřív si ujasněte, kam brašnu chcete dát. Na kolo s nosičem se hodí jiné řešení než na lehké silniční nebo gravelové kolo, které nosič nemá a ani ho namontovat nejde. Rozhoduje i to, jestli brašnu budete sundávat a nosit do kanceláře, nebo zůstane na kole celý den.</p>'
          + T(['Typ', 'Kam se upevňuje', 'K čemu se hodí'], [
              ['Boční brašna (pannier)', 'z boku na zadní nebo přední nosič', 'cestování, nákupy, dojíždění do práce'],
              ['Horní brašna na nosič', 'navrch nosiče, popruhy nebo kolejnice', 'menší náklad, kombinace s bočními brašnami'],
              ['Rámová brašna', 'do trojúhelníku rámu na suché zipy', 'těžší věci blízko těžiště, bikepacking'],
              ['Brašnička na horní trubku', 'na horní rámovou trubku u představce', 'telefon, svačina, doklady po ruce'],
              ['Podsedlová brašna', 'pod sedlo na lišty sedla a sedlovku', 'duše, montpáky, multiklíč'],
              ['Velký vak na sedlovku', 'pod sedlo, přesah za kolo', 'oblečení a spacák na bikepacking'],
              ['Brašna na řídítka', 'na řídítka přes adaptér nebo popruhy', 'mapa, foťák, svačina, lehké věci']]) +
          '<h2>Boční brašny na nosič</h2>'
          '<p>Klasické boční brašny se zavěšují na trubky nosiče háčky a spodní pojistkou. Mají největší objem, typicky se prodávají jednotlivě nebo v páru a na cestách s nimi uvezete stan, spacák i vařič. Těžiště zůstane nízko, záda se nepotí a kolo se dobře ovládá i s plným nákladem. Pro kratší cesty po městě stačí jedna boční brašna, často ve střihu aktovky s popruhem přes rameno nebo s úchytem na notebook.</p>'
          '<p>Na přední nosič, tedy lowrider u přední vidlice, se dávají menší brašny. Rozložení zátěže mezi přední a zadní kolo zlepšuje ovládání na delších expedicích. Na běžné dojíždění to ale potřeba není.</p>'
          '<h2>Systémy uchycení</h2>'
          '<p>Většina výrobců má vlastní systém, kterým brašna drží na nosiči nebo řídítkách. U bočních brašen Ortlieb se používají systémy QL1, QL2.1 a QL3.1. Brašny s QL1, QL2 a QL2.1 lze zavěsit i do kolejnic QL3.1, opačně to nejde. Ortlieb u systému QL3.1 uvádí nosnost nejvýše 9 kg na jednu brašnu. Háčky u novějších systémů se nastavují bez nářadí, takže brašnu snadno přesunete na jiné kolo.</p>'
          '<p>Topeak má pro horní brašny systém QuickTrack. Brašna se zasune do kolejnice na nosičích řady MTX nebo RX a zacvakne, uvolní se tlačítkem. Pro běžné nosiče se prodává adaptér Omni QuickTrack, který výrobce uvádí pro šířku nosiče 90 až 120 mm. Na řídítka se často používají adaptéry KlickFix, u kterých výrobce uvádí nosnost zpravidla 7 kg. Další systémy jsou Racktime Snapit a MIK, se kterými pracuje více výrobců nosičů a košíků.</p>'
          '<p>Před nákupem zjistěte, jaký nosič máte a jestli brašna potřebuje adaptér. Podívejte se i na průměr trubek nosiče: některé háčky mají vložky pro tenké a silnější trubky, jiné se musí dokoupit.</p>'
          '<h2>Bikepacking bez nosiče</h2>'
          '<p>Bikepackingové brašny se připevňují popruhy a suchými zipy přímo na rám, sedlovku a řídítka. Kolo zůstane lehké a úzké, takže projede i po úzkých stezkách. V nabídce jsou třeba rolovací brašny Topeak BackLoader na sedlovku, rámové brašny Topeak MidLoader v několika objemech, sady Acepac s nosnými postroji na řídítka a pod sedlo nebo držáky na vidlici pro lahve a menší vaky.</p>'
          '<p>Velký vak pod sedlo potřebuje mezi sedlem a pláštěm zadního kola dost místa. U menších rámů a celoodpružených kol se vak při propružení může dotknout pláště. Kolik místa vak potřebuje, zjistíte v návodu. Klasický vak nejde použít s teleskopickou sedlovkou, protože by sedlu bránil v pohybu dolů. Pro takové sedlovky existují speciální brašny, Acepac má například model Drop Post Bag. Rámovou brašnu přes celý trojúhelník vybírejte podle rozměrů vnitřku rámu a myslete na to, že zabere místo pro košíky na lahve. Role na řídítka nesmí stlačovat lanka a kabely ani zakrývat přední světlo.</p>'
          '<h2>Vodotěsné, nebo voděodolné</h2>'
          '<p>Brašny se liší tím, jak dobře odolají dešti. Vodotěsné modely jsou ze zátěrové tkaniny nebo laminátu a mají svařované švy místo prošívaných. Firma Ortlieb, založená v roce 1982 v Norimberku, je spojuje vysokofrekvenčním svařováním. Zavírají se rolovacím uzávěrem, který se několikrát přehne a zacvakne přezkou. Voděodolné brašny s prošitými švy a zipem vydrží přeháňku, ale při celodenním dešti do nich voda časem pronikne.</p>'
          '<p>Pokud brašna vodotěsná není, zabalte věci uvnitř do <a href="/nepromokave-vaky/">nepromokavých vaků</a> nebo si kupte pláštěnku na brašnu. Doklady, elektroniku a náhradní oblečení dávejte do vodotěsného obalu vždy, i když předpověď vypadá dobře.</p>'
          '<h2>Objem a nosnost</h2>'
          '<p>Podsedlové brašničky mají objem pod jeden litr až kolem dvou litrů, rámové brašny jednotky litrů a boční brašny se pohybují kolem dvaceti litrů na kus. Velké vaky pod sedlo pojmou zhruba deset až patnáct litrů. Objem je ale jen část pravdy. Nosnost určuje i nosič, na který brašnu dáte. Maximální zatížení bývá vyražené přímo na nosiči nebo uvedené v návodu a je potřeba ho dodržet, včetně limitu brašny a adaptéru. Platí vždy ta nižší hodnota.</p>'
          '<p>Elektrokola mají někdy nosič s baterií nebo s omezenou nosností. U nich si ověřte, jestli brašna nezakrývá zadní světlo a jestli háčky pasují na profil nosiče. Některé brašny výrobci nabízejí přímo ve verzi pro elektrokola.</p>'
          '<h2>Jak brašny naložit</h2>'
          '<ul><li><strong>Těžké věci dolů a dopředu.</strong> Vařič, nářadí a jídlo patří ke dnu bočních brašen a co nejblíž k ose kola.</li>'
          '<li><strong>Zátěž rovnoměrně.</strong> Dvě boční brašny naplňte zhruba stejně, jinak kolo táhne na jednu stranu.</li>'
          '<li><strong>Pata a brašna.</strong> Brašnu posuňte na nosiči dozadu tak, aby o ni pata při šlapání nezavadila.</li>'
          '<li><strong>Řídítka lehce.</strong> Těžká brašna na řídítkách zhoršuje řízení, dávejte do ní hlavně lehké věci.</li>'
          '<li><strong>Nic nevisí.</strong> Volné popruhy zastrčte nebo zkraťte, aby se nenamotaly do výpletu nebo kotouče.</li></ul>'
          '<h2>Ochrana rámu</h2>'
          '<p>Popruhy a suché zipy se při jízdě o rám lehce posouvají a s prachem fungují jako brusný papír. Na místa, kde brašna přiléhá, nalepte ochrannou fólii nebo pásku. Platí to hlavně pro karbonové rámy a lakované rámy, na kterých je odřenina vidět. Při každém zastavení zkontrolujte, jestli se brašna neposunula a nedře o plášť.</p>'
          '<h2>Brašny na řídítka a na horní trubku</h2>'
          '<p>Brašna na řídítka drží buď na adaptéru, ze kterého se jedním pohybem sundá, nebo na popruzích. Adaptérová brašna se hodí na výlety, kdy ji berete s sebou do restaurace nebo do muzea. Často má navrchu průhlednou kapsu na mapu. Brašnička na horní rámovou trubku je malá, ale věci z ní vyndáte za jízdy: tyčinku, gel, klíče nebo powerbanku pro světlo. Některé mají kapsu na telefon s fólií, přes kterou jde ovládat displej. Na silničních kolech se nosí hlavně brašničky těsně za představcem, aby nepřekážely kolenům při stoupání ze sedla.</p>'
'<h2>Jak porovnávat nabídky</h2>'
          '<p>U stejného modelu se v názvu často liší jen barva nebo systém uchycení. Porovnávejte objem v litrech, způsob uchycení a potřebné adaptéry, vodotěsnost a typ uzávěru, hmotnost, reflexní prvky a to, jestli se prodává jedna brašna, nebo pár. U bikepackingových sad zjistěte, jestli je v balení i nosný postroj, nebo jen samotný vak. Přečtěte si i maximální zatížení, které výrobce uvádí.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě bočních brašen na kolo, které nemá nosič ani úchyty pro něj.</li>'
          '<li>Brašna s jiným systémem, než jaký má nosič nebo adaptér na řídítkách.</li>'
          '<li>Velký vak pod sedlo na malém celoodpruženém kole.</li>'
          '<li>Spoléhání na voděodolnou brašnu při několikadenním dešti.</li>'
          '<li>Přetížený nosič a těžké věci nahoře v brašně.</li></ul>'
          '<p>Na kolo se hodí také <a href="/kosiky-na-kolo/">košíky</a>, a kdo raději vozí věci na zádech, najde <a href="/cyklisticke-batohy/">cyklistické batohy</a>. K delším cestám patří <a href="/cyklo-lahve-a-drzaky/">lahve a držáky</a>, <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> a <a href="/cyklo-zamky/">zámky na kolo</a>. Telefon na řídítka upevníte <a href="/drzaky-na-mobil-na-kolo/">držákem na mobil</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi boční a horní brašnou na nosič?', 'Boční brašna visí z boku nosiče, má velký objem a nízké těžiště. Horní brašna leží navrch nosiče, je menší a často se kombinuje s bočními brašnami.'),
        ('Jak poznám, jestli brašna pasuje na můj nosič?', 'Zjistěte systém uchycení brašny a průměr trubek nosiče. U horních brašen se systémem QuickTrack, Snapit nebo MIK potřebujete kompatibilní nosič nebo adaptér.'),
        ('Kolik unese brašna na kolo?', 'Záleží na brašně, adaptéru i nosiči. Ortlieb například u systému QL3.1 uvádí 9 kg na jednu brašnu. Vždy platí nejnižší limit z celé sestavy.'),
        ('Co je bikepacking?', 'Cestování na kole s brašnami připevněnými přímo na rám, sedlovku a řídítka, bez nosiče. Kolo zůstane lehké a projede i úzké stezky.'),
        ('Dá se velká podsedlová brašna použít s teleskopickou sedlovkou?', 'Klasický vak ne, bránil by sedlu sjet dolů. Pro teleskopické sedlovky se vyrábějí speciální brašny, například Acepac Drop Post Bag.'),
        ('Je brašna se zipem nepromokavá?', 'Většinou jen voděodolná. Plně vodotěsné bývají brašny se svařovanými švy a rolovacím uzávěrem, prošívané švy a zip časem vodu propustí.'),
        ('Jak naložit boční brašny?', 'Těžké věci ke dnu a dopředu, obě brašny zhruba stejně plné. Brašnu posuňte dozadu, aby o ni pata při šlapání nezavadila.'),
        ('Poškodí rámová brašna rám?', 'Popruhy mohou lak časem odřít, hlavně s prachem. Místa styku přelepte ochrannou fólií a brašnu pravidelně kontrolujte.'),
        ('Jakou brašnu na kolo do práce?', 'Boční brašnu ve tvaru aktovky s popruhem přes rameno a kapsou na notebook. Na kolo bez nosiče se hodí spíš batoh nebo menší rámová brašna.'),
        ('Kde koupit brašnu na kolo?', 'Sporteka porovná nabídky českých e-shopů u brašen na nosič, rám, řídítka i pod sedlo. Objednávku pak uděláte přímo v obchodě.'),
    ])

# ------------------------------------------------------------------ kosiky-na-kolo
NEW['kosiky-na-kolo'] = dict(long=True,
    title='Košíky na kolo přední i zadní, proutěné i drátěné',
    desc='Přední košíky na řídítka, zadní košíky na nosič, proutěné, drátěné i dětské. Uchycení, nosnost, vození psa a jak se s košíkem jezdí.',
    intro='<p><strong>Košík na kolo</strong> je nejjednodušší způsob, jak vozit nákup, kabelku nebo deku na piknik. Přední košík se upevňuje na řídítka nebo na přední nosič, zadní košík na nosič nad zadním kolem. Vyrábějí se z ocelového drátu, plastu, proutí nebo plastu s proutěným vzhledem a také jako textilní košíky, které se dají po sundání nosit jako taška. Zvláštní skupinu tvoří košíky pro malé psy a dětské košíky s potiskem na dětská kola.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů, takže porovnáte, kde je vybraný košík k mání. V nabídce jsou košíky Basil, KlickFix, Racktime, Topeak, Fastrider nebo Btwin a držáky na řídítka od '
          + B(('force', 'Force'), ('merco', 'Merco')) +
          '. Košíky jsou součástí sekce <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>',
    guide='<h2>Přední, nebo zadní košík</h2>'
          '<p>Přední košík máte stále na očích a věci z něj vyndáte, aniž byste slezli z kola. Náklad na řídítkách ale ovlivňuje řízení: čím je těžší, tím víc se kolo stáčí a tím hůř se jezdí pomalu nebo v zatáčkách. Zadní košík unese víc a řízení neovlivní, potřebuje ovšem nosič. Na městské a trekingové kolo s nosičem se často dávají oba typy, na kolo bez nosiče zbývá jen přední košík.</p>'
          + T(['Typ', 'Uchycení', 'Vhodný náklad'], [
              ['Přední košík na řídítka', 'adaptér na řídítka, často s rychloupínáním', 'lehčí věci, kabelka, svačina'],
              ['Přední košík pevně na vidlici', 'vzpěry k ose kola nebo přední nosič', 'těžší nákup na městském kole'],
              ['Zadní košík na nosič', 'šrouby, svorky nebo systém MIK, Snapit', 'nákup, přepravka, větší taška'],
              ['Textilní košík-taška', 'adaptér na řídítka nebo háčky na nosič', 'nákupy, po sundání slouží jako taška'],
              ['Košík pro psa', 'řídítka nebo nosič podle modelu', 'malý pes do limitu výrobce'],
              ['Dětský košík', 'pásky na řídítka dětského kola', 'hračky a drobnosti']]) +
          '<h2>Uchycení na řídítka</h2>'
          '<p>Přední košíky se k řídítkům připevňují adaptérem. Rozšířený je systém KlickFix, kdy na řídítkách zůstane objímka a košík se do ní zacvakne a jedním stiskem sundá. Výrobce u svých adaptérů na řídítka uvádí nosnost zpravidla 7 kg. Při kombinaci adaptéru a košíku přitom platí nižší z obou limitů. Některé adaptéry mají zámek, aby košík nezmizel, když kolo necháte stát.</p>'
          '<p>Před nákupem změřte průměr řídítek v místě, kde bude objímka. Běžné jsou průměry 22,2 mm, 25,4 mm a 31,8 mm a mnoho držáků má vložky pro více průměrů. U řídítek s velkým množstvím lanek, s displejem elektrokola nebo s předním světlem na řídítkách ověřte, jestli se adaptér vejde. Topeak nabízí přední košík přímo ve verzi pro elektrokola.</p>'
          '<p>Levnější košíky se připevňují háčky nebo pásky přímo na řídítka. Drží méně pevně a při jízdě po kostkách se mohou pootočit. Na nákup jednou týdně stačí, na každodenní jízdu je pohodlnější pevný adaptér.</p>'
          '<h2>Zadní košík na nosič</h2>'
          '<p>Zadní košíky se na nosič připevňují šrouby se svorkami nebo systémem s adaptérovou deskou. Systémy MIK a Racktime Snapit umožňují košík nasadit a sundat jedním pohybem a mají zámek. Racktime u svých adaptérových desek Snapit uvádí nosnost 12 kg. Systémy mezi sebou obvykle kompatibilní nejsou, proto zjistěte, jaký nosič na kole máte. Pokud nosič žádný systém nemá, existují univerzální adaptérové desky.</p>'
          '<p>Nosnost zadního košíku omezuje i nosič. Údaj o maximálním zatížení najdete na nosiči nebo v návodu kola. Zadní košík nesmí zakrývat zadní světlo ani odrazku, jinak je potřeba světlo přesunout.</p>'
          '<h2>Materiály košíků</h2>'
          '<p><strong>Drátěné košíky</strong> z oceli nebo hliníku jsou pevné a vzdušné, voda z nich vyteče a dobře drží. Ocelové bývají povrchově upravené proti rzi, poškozený lak je ale potřeba hlídat. Drobnosti mohou propadnout mřížkou, proto se k nim prodávají vložky. <strong>Plastové košíky</strong> jsou lehké a levné, nerezaví a mají jemnou mřížku.</p>'
          '<p><strong>Proutěné košíky</strong> mají klasický vzhled, hodí se k městským a retro kolům. Proutí ale nemá rádo dlouhodobou vlhkost, a když kolo stojí venku, proutí šedne a časem praská. Proto se vyrábějí i košíky z plastu, který proutí jen napodobuje. Basil je nabízí pod označením Rattan Look. Nizozemská firma Basil začínala v roce 1934 jako obchod s koly a košíky dováží od roku 1976. <strong>Textilní košíky</strong> mají pevný rám a látkové stěny, často s víkem nebo stahovací šňůrkou. Po sundání se nosí jako taška.</p>'
          '<h2>Košík pro psa</h2>'
          '<p>V košíku se dá vozit malý pes, ale jen v košíku, který je k tomu určený, a jen do hmotnosti, kterou uvádí výrobce. Psí košíky mají vyšší stěny, polstrované dno, ochrannou mřížku nebo stříšku a úchyt na krátké vodítko. KlickFix u svých psích košíků na řídítka uvádí limit kolem 7 kg, u košíků na nosič podle varianty o něco víc. Rozhoduje údaj v návodu konkrétního modelu a adaptéru.</p>'
          '<ul><li>Psa připněte krátkým vodítkem k postroji, ne k obojku, aby nemohl vyskočit.</li>'
          '<li>Pes se na kolo musí zvykat postupně, nejdřív na stojícím kole a na krátkých trasách.</li>'
          '<li>Pes v předním košíku mění řízení víc než nákup, protože se hýbe. Jezděte pomalu.</li>'
          '<li>V horku a na slunci dělejte přestávky a myslete na vodu pro psa.</li></ul>'
          '<p>Většího psa v košíku nevozte. Pro něj existují psí vozíky za kolo.</p>'
          '<h2>Dětské košíky</h2>'
          '<p>Malé plastové košíky s motivy z pohádek se připevňují pásky na řídítka dětských kol a odrážedel. Slouží na hračky a drobnosti, ne na těžký náklad. Dbejte, aby košík nebránil dítěti v řízení a nezakrýval zvonek ani brzdové páčky. Pásky po připevnění zkraťte, aby nevisely do předního kola.</p>'
          '<h2>Jízda s plným košíkem</h2>'
          '<p>S nákladem se kolo chová jinak. Brzdná dráha se prodlouží, kolo se v zatáčkách naklání pomaleji a při rozjezdu může přední kolo s těžkým košíkem uhýbat. Těžké věci dávejte radši do zadního košíku, do předního jen lehké. Nákup v igelitce, která vyčnívá přes okraj košíku, zajistěte gumicuky nebo síťkou, aby nevypadl do kola. Při stání na stojanu se kolo s plným předním košíkem snadno převrhne, proto ho opřete nebo držte.</p>'
          '<h2>Údržba</h2>'
          '<p>Šrouby a objímky po prvních jízdách zkontrolujte a dotáhněte, protože se usadí. Drátěný košík, který začne rezavět, očistěte a ošetřete. Proutěný košík neparkujte v dešti a nechte ho uschnout v suchu. Textilní košíky stačí otřít vlhkým hadříkem, odnímatelné vložky jdou často vyprat.</p>'
          '<h2>Jaký košík na jaké kolo</h2>'
          '<p>Košík patří hlavně na <a href="/mestska-kola/">městská</a> a <a href="/trekingova-kola/">treková kola</a> s rovnými nebo zahnutými řídítky a nosičem. Na horské kolo se přední košík dá připevnit také, v terénu ale náklad poskakuje a košík trpí. Na silniční a gravelové kolo s beranem se klasický košík nehodí, pro bikepacking existují lehké košíky na řídítka s popruhy. Elektrokolo unese těžší nákup bez námahy, má ale displej a ovladač na řídítkách, se kterými musí adaptér předního košíku počítat.</p>'
          '<p>Ženská kola s nízkým nástupem mívají nosič i úchyty pro přední košík z výroby. U skládacích kol se používají menší košíky a tašky na speciální úchyty vpředu na rámu. Pokud kolo převážíte autem na nosiči, počítejte s tím, že košík se před naložením sundává. Rychloupínací adaptér tu ušetří práci, protože košík odepnete bez nářadí a objímka zůstane na řídítkách.</p>'
          '<p>Na kolo, které parkujete venku u nádraží nebo ve škole, se hodí košík, který jde snadno sundat a vzít s sebou, nebo naopak pevně přišroubovaný drátěný košík, o který nikdo nestojí. Odnímatelný košík s adaptérem bez zámku se ztrácí snadno.</p>'
'<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte objem nebo rozměry, materiál, způsob uchycení a to, jestli je adaptér v balení, nebo se kupuje zvlášť. U zadních košíků sledujte systém (MIK, Snapit, KlickFix, univerzální), u předních průměr řídítek a nosnost. Košík a adaptér se často prodávají odděleně, a pokud v nabídce chybí jedno z nich, na kolo ho nepřipevníte.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Těžký nákup v předním košíku na řídítkách.</li>'
          '<li>Košík bez adaptéru a zjištění až doma, že se nedá připevnit.</li>'
          '<li>Zadní košík, který zakryje zadní světlo.</li>'
          '<li>Pes v obyčejném nákupním košíku bez vodítka.</li>'
          '<li>Proutěný košík trvale venku na dešti.</li></ul>'
          '<p>Kdo potřebuje vozit víc, najde <a href="/brasny-na-kolo/">brašny na kolo</a>. Na nákupy dobře poslouží <a href="/mestska-kola/">městská kola</a> s nosičem, na kterém může být i <a href="/cyklo-sedacky-a-voziky/">sedačka pro dítě</a>. Kolo před obchodem zajistíte <a href="/cyklo-zamky/">zámkem</a> a na večerní cestu se hodí <a href="/cyklo-svetla/">světla na kolo</a>.</p>',
    faq=[
        ('Je lepší přední, nebo zadní košík na kolo?', 'Přední je stále po ruce, ale ovlivňuje řízení, proto se hodí na lehčí věci. Zadní unese víc a řízení nemění, potřebuje však nosič.'),
        ('Kolik unese košík na řídítka?', 'Záleží na košíku i adaptéru. KlickFix u adaptérů na řídítka uvádí zpravidla 7 kg. Platí vždy nižší limit z košíku a držáku.'),
        ('Jak změřit průměr řídítek?', 'Posuvným měřítkem v místě, kde bude objímka. Běžné průměry jsou 22,2, 25,4 a 31,8 mm a mnoho držáků má vložky pro více z nich.'),
        ('Pasuje každý zadní košík na každý nosič?', 'Ne. Systémy MIK, Racktime Snapit a KlickFix jsou různé a obvykle navzájem nepasují. Zjistěte, jaký systém má váš nosič, nebo použijte univerzální montáž.'),
        ('Můžu v košíku vozit psa?', 'Jen v košíku určeném pro psy a do hmotnosti, kterou výrobce uvádí. Psa připněte krátkým vodítkem k postroji a jezděte pomalu.'),
        ('Vydrží proutěný košík déšť?', 'Občasné zmoknutí ano, dlouhodobou vlhkost proutí nesnáší. Na kolo, které stojí venku, se hodí plastový košík s proutěným vzhledem.'),
        ('Dá se košík sundat a nosit jako taška?', 'U košíků na rychloupínací adaptér ano. Textilní košíky a mnohé proutěné modely mají ucha a slouží po sundání jako nákupní taška.'),
        ('Potřebuji ke košíku adaptér?', 'Většinou ano. Košík a adaptér se často prodávají zvlášť, proto si v nabídce ověřte, co přesně je v balení.'),
        ('Jaký košík na dětské kolo?', 'Malý plastový košík na pásky, který nebrání v řízení a nezakryje zvonek ani brzdové páčky. Slouží na hračky, ne na těžké věci.'),
        ('Kde koupit košík na kolo?', 'Na Sportece porovnáte nabídky českých obchodů u předních, zadních, proutěných i psích košíků a nakoupíte v obchodě, který vám vyhovuje.'),
    ])

# ------------------------------------------------------------------ cyklisticke-batohy
NEW['cyklisticke-batohy'] = dict(long=True,
    title='Cyklistické batohy s větráním, hydrovakem a chráničem',
    desc='Cyklistické batohy od malých na vyjížďku po velké na přejezd hor. Objem, větraná záda, hydratace, chránič páteře a jak batoh správně seřídit.',
    intro='<p><strong>Cyklistický batoh</strong> se od běžného batohu liší hlavně zády a popruhy. Má větraný zádový systém, užší střih, který nepřekáží v předklonu, bederní a hrudní pás, aby se batoh na sjezdu nehoupal, a uvnitř kapsy na nářadí a duši. Většina modelů má místo na vak s vodou a výstup pro hadičku, mnohé také držák na helmu a pláštěnku. Některé batohy na enduro a sjezd mají vestavěný chránič páteře.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů, takže u každého batohu vidíte, kde ho právě prodávají. Najdete tu cyklistické batohy '
          + B(('deuter', 'Deuter'), ('kilpi', 'Kilpi'), ('husky', 'Husky'), ('klimatex', 'Klimatex')) +
          ', Evoc, Camelbak nebo Kellys. Batohy patří do sekce <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</p>',
    guide='<h2>Batoh, nebo brašna</h2>'
          '<p>Batoh se hodí tam, kde kolo nosič nemá nebo mít nemá: na horském kole, při jízdě v terénu a na vyjížďky, kde chcete mít vodu a nářadí vždy u sebe. Batoh přejde s vámi z kola do obchodu nebo na vrchol kopce. Na druhou stranu zahřívá záda, zvedá těžiště a při delší cestě s velkým nákladem tlačí do ramen. Na trekingové a městské kolo s nosičem jsou na těžší náklad pohodlnější <a href="/brasny-na-kolo/">brašny na kolo</a>.</p>'
          '<h2>Objem podle typu jízdy</h2>'
          + T(['Objem', 'Typ jízdy', 'Co se vejde'], [
              ['do 8 l', 'krátké vyjížďky, závody, trail', 'vak s vodou, duše, pumpička, klíč'],
              ['10–14 l', 'odpolední a celodenní vyjížďka', 'navíc bunda, svačina, lékárnička'],
              ['16–22 l', 'enduro, celodenní túra v horách', 'chrániče, teplá vrstva, víc jídla'],
              ['24–32 l', 'přejezd hor, vícedenní túra s nocováním pod střechou', 'oblečení na několik dní, toaletní taška'],
              ['20–30 l městský', 'dojíždění do práce', 'notebook, oblečení na převlečení, oběd']]) +
          '<p>Větší batoh pro jistotu kupovat nemá smysl. Prázdné místo se při jízdě přelévá a batoh se houpe. Lepší je vybrat objem, který odpovídá většině vašich vyjížděk, a na výjimečné akce si půjčit nebo dokoupit větší. Deuter například nabízí batohy Race od 8 litrů a řadu Trans Alpine kolem 22 až 32 litrů, na přejezd hor.</p>'
          '<h2>Záda a větrání</h2>'
          '<p>Při šlapání se záda potí víc než při chůzi, protože jste v předklonu a batoh na nich leží celou plochou. Cyklistické batohy proto mají větraný zádový systém. Jedním typem jsou pěnové polštáře s kanálky, kudy proudí vzduch. Druhým je napnutá síťovina, která batoh od zad oddálí. Deuter u řady Race Air používá systém Aircomfort se síťovinou napnutou na rámu z pružinové oceli, mezi zády a batohem tak vzniká mezera pro proudění vzduchu.</p>'
          '<p>Síťová záda větrají lépe, batoh má ale těžiště o kousek dál od těla. Na technické sjezdy proto mnoho jezdců volí batoh, který přiléhá těsně, a se zpocenými zády počítá. Na dlouhé vyjížďky po silnici a v létě je naopak pohodlnější síťovina.</p>'
          '<h2>Popruhy a seřízení</h2>'
          '<p>Batoh má sedět vysoko a blízko u těla. Ramenní popruhy dotáhněte tak, aby batoh neležel na bedrech, hrudní pás zapněte zhruba v polovině hrudníku a bederní pás tak, aby batoh při naklonění kola neujížděl do strany. U malých batohů bývá bederní pás jen úzký pásek, u větších má polstrovaná křídla s kapsami. Popruhy, které zbývají, zastrčte nebo stáhněte gumičkou, aby nepleskaly.</p>'
          '<p>Batohy se liší i délkou zad. Výrobci uvádějí, pro jakou výšku postavy je model určený. Deuter u modelu Attack 20 uvádí výšku 170 až 195 cm. Modely s označením SL mají dámský střih s kratšími zády a jinak tvarovanými ramenními popruhy. Pro děti existují menší batohy, například Deuter Attack 8 JR.</p>'
          '<h2>Pití na cestu</h2>'
          '<p>Většina cyklistických batohů má uvnitř kapsu na <a href="/hydrovaky/">hydrovak</a>, tedy měkký vak s hadičkou a náustkem. Pít se dá za jízdy bez sahání po lahvi, což ocení hlavně jezdci v terénu, kde na lahev na rámu není čas. Batohy jsou obvykle stavěné na vak o objemu dva až tři litry, Deuter například u modelu Race Air 10 uvádí kompatibilitu s třílitrovým vakem. Vak se často kupuje zvlášť, ověřte si, co je v balení. Plný vak váží tolik, kolik je v něm vody, a do batohu patří co nejblíž k zádům.</p>'
          '<p>Camelbak, výrobce hydratačních vaků, nabízí batohy přímo postavené kolem vaku, například řadu M.U.L.E. Kdo vak nechce, vystačí si s lahvemi v <a href="/cyklo-lahve-a-drzaky/">košících na rámu</a> a batoh použije jen na věci.</p>'
          '<h2>Batohy s chráničem páteře</h2>'
          '<p>Batohy na enduro a sjezd mají v zádech chránič, který při pádu na záda tlumí náraz. Pro chrániče zad platí evropská norma EN 1621-2 se dvěma úrovněmi: úroveň 2 tlumí náraz víc než úroveň 1. Některé batohy mají chránič certifikovaný podle této normy a na štítku uvádějí úroveň, jiné mají jen pěnovou vložku bez certifikace. Pokud vám o ochranu jde, hledejte v popisu konkrétní normu a úroveň. Chránič v batohu kryje jen část zad a nenahrazuje helmu ani další <a href="/cyklo-chranice/">cyklistické chrániče</a>.</p>'
          '<h2>Kapsy a výbava</h2>'
          '<ul><li><strong>Kapsa na nářadí</strong> s přihrádkami, aby klíč a montpáky nedřely o vak s vodou.</li>'
          '<li><strong>Držák na helmu</strong> v podobě síťky nebo háčků, když jdete pěšky nebo na kafe.</li>'
          '<li><strong>Pláštěnka</strong> uložená ve spodní kapse. Deuter ji u modelu Race Air 10 dodává odnímatelnou.</li>'
          '<li><strong>Reflexní prvky a poutko na světlo</strong> pro jízdu za šera.</li>'
          '<li><strong>Kapsy na bederním pásu</strong> pro telefon, tyčinku nebo gel.</li>'
          '<li><strong>Poutka na chrániče</strong> kolen, aby se daly nést na stoupání.</li></ul>'
          '<h2>Do města a do práce</h2>'
          '<p>Na dojíždění se hodí batoh s polstrovanou kapsou na notebook, organizérem a uzávěrem, který při dešti nepropustí vodu. Velké reflexní plochy zlepší viditelnost v provozu. Městské batohy na kolo bývají jednodušší, bez kapsy na vak, zato s více přihrádkami. Výběr dalších městských modelů je v kategorii <a href="/mestske-batohy/">městské batohy</a>.</p>'
          '<h2>Péče o batoh</h2>'
          '<p>Batoh po jízdě v blátě nechte proschnout a pak ho vykartáčujte. Pokud výrobce dovoluje praní, perte ho ručně ve vlažné vodě s jemným prostředkem, vyndejte předtím chránič a výztuhy. Pračka a sušička mohou poškodit pěnu, zátěr i přezky. Vak na vodu po každém použití vypláchněte a nechte vyschnout otevřený, aby v něm nezačaly růst plísně.</p>'
          '<h2>Co do batohu zabalit</h2>'
          '<p>Na každou vyjížďku patří do batohu náhradní duše nebo lepení, montpáky, pumpička a multiklíč. Přidejte tenkou bundu proti větru, něco k jídlu, telefon a peníze. Na delší výlety se hodí malá lékárnička, čelovka a nabitá powerbanka. Těžké věci, jako je nářadí a vak s vodou, dávejte co nejblíž k zádům a dolů, lehké oblečení nahoru a ven. Věci, které potřebujete za jízdy, nechte v kapsách bederního pásu.</p>'
          '<h2>Batoh v zimě a v dešti</h2>'
          '<p>V zimě voda v hadičce hydrovaku zamrzá. Pomáhá izolovaný obal hadičky a vyfouknutí vody zpět do vaku po každém napití. Batoh přes bundu musí mít dost dlouhé popruhy, ověřte to před první zimní vyjížďkou. V dešti se hodí pláštěnka na batoh v reflexní barvě. Doklady a elektroniku zabalte uvnitř do vodotěsného sáčku, protože látka batohu a zipy promoknou dřív, než si toho všimnete. Mokrý batoh po návratu vyprázdněte, rozepněte kapsy a nechte ho uschnout v teple, ale ne na topení.</p>'
          '<p>Za tmy a v mlze pomůže blikačka připnutá na poutko batohu. Je výš než světlo na sedlovce a řidiči ji vidí i přes náklad v brašnách nebo když zadní světlo zakryje bunda.</p>'
'<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte objem, hmotnost, délku zad nebo doporučenou výšku postavy, typ zádového systému, kapsu na hydrovak a to, jestli je vak v balení. U batohů s chráničem hledejte normu a úroveň. Stejný model se prodává v několika barvách a také v dámské verzi.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Velký batoh na krátké vyjížďky, ve kterém se věci přelévají.</li>'
          '<li>Batoh nízko na bedrech s povolenými popruhy.</li>'
          '<li>Nezapnutý hrudní a bederní pás na sjezdu.</li>'
          '<li>Spoléhání na pěnovou vložku bez certifikace jako na chránič.</li>'
          '<li>Vak na vodu nechaný v batohu s vodou do další vyjížďky.</li></ul>'
          '<p>K batohu se hodí <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/cyklisticke-bryle/">cyklistické brýle</a> a <a href="/cyklisticke-rukavice/">rukavice</a>. Běžci najdou lehké batohy a vesty v kategorii <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, turisté v kategorii <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    faq=[
        ('Jak velký cyklistický batoh vybrat?', 'Na krátké vyjížďky stačí do 8 litrů, na celodenní kolem 10 až 14 litrů. Enduro a túry v horách potřebují 16 až 22 litrů, přejezd hor kolem 30 litrů.'),
        ('Čím se cyklistický batoh liší od turistického?', 'Má užší střih, větraná záda, kapsu na nářadí a vak s vodou a pevnější bederní a hrudní pás. Je stavěný na předklon a pohyb na kole.'),
        ('Má smysl batoh se síťovanými zády?', 'Na dlouhé vyjížďky a v létě ano, záda se méně potí. Na technické sjezdy někteří jezdci volí batoh, který přiléhá těsněji.'),
        ('Jak velký vak na vodu se vejde do cyklistického batohu?', 'Většina batohů počítá se dvěma až třemi litry. Konkrétní objem uvádí výrobce, a pokud vak v balení není, kupuje se zvlášť.'),
        ('Co znamená EN 1621-2 u batohu s chráničem?', 'Evropskou normu pro chrániče zad. Úroveň 2 tlumí náraz víc než úroveň 1. Hledejte ji na štítku konkrétního batohu nebo chrániče.'),
        ('Nahradí batoh s chráničem chráničovou vestu?', 'Ne úplně. Chránič v batohu kryje jen část zad a batoh se při pádu může posunout. Helmu ani další chrániče nenahrazuje.'),
        ('Jak správně seřídit cyklistický batoh?', 'Batoh má sedět vysoko a blízko těla. Dotáhněte ramenní popruhy, zapněte hrudní pás a bederní pás tak, aby se batoh při naklonění nehoupal.'),
        ('Existují dámské cyklistické batohy?', 'Ano. Mají kratší záda a jinak tvarované popruhy. U Deuteru je poznáte podle označení SL v názvu modelu.'),
        ('Jak vyčistit vak na vodu?', 'Po každém použití ho vypláchněte a nechte vyschnout otevřený. Hadičku a náustek čistěte podle návodu výrobce, aby v nich nerostly plísně.'),
        ('Kde koupit cyklistický batoh?', 'Sporteka u každého batohu ukáže nabídky českých e-shopů. Porovnáte, kde je vybraný model a barva, a koupíte v obchodě podle sebe.'),
    ])

# ------------------------------------------------------------------ nepromokave-ponozky
NEW['nepromokave-ponozky'] = dict(long=True,
    title='Nepromokavé ponožky s membránou na kolo, běh i túry',
    desc='Nepromokavé ponožky s membránou DexShell, Sealskinz a dalších značek. Jak fungují, kde se hodí, jak vybrat velikost a jak je prát.',
    intro='<p><strong>Nepromokavé ponožky</strong> mají mezi vnější a vnitřní pleteninou vloženou membránu, která nepustí vodu dovnitř a přitom propouští vodní páru z nohy ven. Noha tak zůstane suchá i v promočené botě. Hodí se na kolo v dešti, na běh v terénu, na túry v lehkých botách bez membrány i na podzimní a zimní procházky po rozbředlém sněhu. Na pohled vypadají jako silnější sportovní ponožky, při oblékání ale méně pruží.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů, takže u každého páru vidíte, kde ho prodávají. V nabídce jsou ponožky DexShell, Sealskinz a Bridgedale StormSock a také ponožky '
          + B(('insportline', 'Insportline')) +
          ' s bambusovou nebo merino vnitřní vrstvou. Kategorie patří pod <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>',
    guide='<h2>Jak jsou nepromokavé ponožky postavené</h2>'
          '<p>Nepromokavá ponožka má tři vrstvy. Vnější pletenina bývá z nylonu nebo jiného odolného vlákna a chrání membránu před oděrem o botu. Uprostřed je membrána. Vnitřní vrstva, která se dotýká kůže, bývá z merina, bambusové viskózy nebo syntetických vláken a odvádí pot od nohy k membráně.</p>'
          '<p>Membrána je hydrofilní, to znamená, že vodu v kapalné podobě nepropustí, ale vodní páru postupně převádí ven. DexShell používá membránu Porelle, Sealskinz vlastní membránu Aquasealz. Prodyšnost má ale své meze. Při intenzivním výkonu a v teplé botě se noha v nepromokavé ponožce potí víc než v obyčejné. Vlhkost pak zůstane uvnitř, i když déšť zvenku neprošel.</p>'
          + T(['Vrstva', 'Materiál', 'Úkol'], [
              ['Vnější', 'nylon, polyamid, směsi', 'odolnost proti oděru, tvar ponožky'],
              ['Membrána', 'hydrofilní fólie (Porelle, Aquasealz a další)', 'nepustí vodu, propouští páru'],
              ['Vnitřní', 'merino, bambus, syntetika', 'komfort na kůži, odvod potu']]) +
          '<h2>Kde se hodí</h2>'
          '<p><strong>Cyklistika.</strong> Tretry a silniční boty mají větrací otvory a v dešti promoknou rychle. Nepromokavé ponožky udrží nohy suché, i když bota je mokrá. Na podzim a v zimě se kombinují s <a href="/navleky-na-boty/">návleky na boty</a>, které zastaví vodu a vítr zvenku.</p>'
          '<p><strong>Běh v terénu.</strong> Trailové boty bez membrány dobře větrají a rychle schnou, ale v mokré trávě a kalužích promoknou za pár minut. Nepromokavá ponožka v nich funguje jako membrána, kterou si obléknete jen ve dnech, kdy je potřeba. DexShell má pro běh lehčí modely, například Running Lite.</p>'
          '<p><strong>Turistika.</strong> V letních botách bez membrány nebo v sandálech na brodění se nepromokavá ponožka hodí jako záloha. Na cestách se dají nosit i do botou, které už membránu mají, ale přestaly těsnit.</p>'
          '<p><strong>Zima.</strong> Zimní modely mají silnější vnitřní vrstvu, často z merina, a delší lem. Sealskinz je rozlišuje podle počasí na teplé, celoroční a chladné. Bridgedale prodává řadu StormSock v různých tloušťkách včetně podkolenek.</p>'
          '<h2>Voda shora</h2>'
          '<p>Nepromokavá ponožka je vodotěsná jen po lem. Pokud vstoupíte do vody hlouběji, než sahá ponožka, voda nateče dovnitř shora. Totéž se stane v dešti, když voda stéká po holé noze nebo po mokrých kalhotách do ponožky. Sealskinz má proto u některých modelů na vnitřní straně lemu pružný pásek Hydrostop bez silikonu, který stékání vody do ponožky omezuje. Někteří prodejci ale upozorňují, že těsný pásek může při dlouhém nošení dřít.</p>'
          '<p>Proti vodě shora pomáhají také dlouhé nepromokavé kalhoty přes kotník, návleky nebo vyšší ponožky. Na brodění potoků je lepší počítat s mokrou nohou a vzít si <a href="/neoprenove-boty-a-ponozky/">neoprenové boty nebo ponožky</a>.</p>'
          '<h2>Ponožky s membránou, nebo boty s membránou</h2>'
          '<p>Boty s membránou jsou nepromokavé samy, ale pomaleji schnou, a když do nich jednou nateče voda shora, zůstane uvnitř. V létě v nich bývá horko. Nepromokavé ponožky v lehké botě bez membrány fungují obráceně: bota zvenku promokne a rychle zase vyschne, noha uvnitř zůstane suchá. Ponožky navíc můžete nosit jen tehdy, když je potřeba, a ve zbytku roku chodit ve vzdušných botách. Nevýhodou je silnější vrstva na noze a menší prodyšnost.</p>'
          '<p>Pro trvalé chození v mokru, třeba na vícedenní túře v horách, je pohodlnější kvalitní bota s membránou. Na kolo, krátké běhy v dešti a jako záloha do batohu dává smysl ponožka. Někteří turisté obě řešení kombinují, když jim membrána v botách přestane těsnit.</p>'
          '<h2>Vnitřní vrstva: merino, bambus, nebo syntetika</h2>'
          '<p>Merinová vlna hřeje i ve vlhku a méně zapáchá, proto se používá u zimních modelů a na vícedenní cesty. Schne ale pomaleji. Bambusová viskóza je jemná na kůži a hodí se do teplejšího počasí. Syntetická vlákna jsou nejodolnější a schnou nejrychleji, takže se objevují u lehkých běžeckých a cyklistických ponožek. Insportline prodává nepromokavé ponožky s bambusovou i merino vnitřní vrstvou, Sealskinz a DexShell mají modely s různými směsmi. Složení najdete v popisu výrobku.</p>'
'<h2>Ponožky vyzkoušejte předem</h2>'
          '<p>Nepromokavé ponožky se nosí jinak než běžné. Jsou tužší, na noze je cítit švy membrány a v botě zaberou víc místa. Než s nimi vyrazíte na celodenní túru nebo na dlouhou vyjížďku, vyzkoušejte je na kratší trase ve stejných botách. Zjistíte, jestli netlačí na prstech nebo na patě a jestli se do boty vejde i vložka. Pokud bota tlačí, pomůže tenčí model nebo povolení tkaniček.</p>'
          '<p>DexShell i Sealskinz vyrábějí kromě ponožek také nepromokavé rukavice a čepice se stejným principem membrány. Na kolo v dešti se tak dá sestavit celá výbava, která udrží suché ruce i nohy.</p>'
          '<p>Nepromokavé ponožky se hodí i mimo sport, třeba na ryby, na práci na zahradě v rose nebo na procházky se psem po mokré louce. Platí ale stejné pravidlo jako jinde: voda nesmí natéct přes lem.</p>'
'<h2>Délka a tloušťka</h2>'
          '<p>Kotníkové ponožky jsou lehké a hodí se do nízkých bot na kolo a na běh. Ponožky do půli lýtka kryjí kotník a jsou nejuniverzálnější. Podkolenky se nosí do vysokých bot a v zimě. Tloušťka ovlivňuje, jak ponožka hřeje a jak se vejde do boty. Silná zimní ponožka zabere v botě víc místa. Pokud máte boty na tělo, zkuste je s nepromokavými ponožkami ještě před výletem.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Membrána nepruží jako běžná pletenina, proto na velikosti záleží víc než u obyčejných ponožek. Ponožky se prodávají v rozmezí S až XL a každá velikost pokrývá několik čísel obuvi podle tabulky výrobce. Příliš malá ponožka tlačí na prsty a membrána je na ní více napnutá. Příliš velká dělá na chodidle a na patě záhyby, které mohou dřít. Řiďte se tabulkou konkrétní značky, protože se mezi výrobci liší.</p>'
          '<p>Při oblékání ponožku nenatahujte silou za lem. Shrňte ji, nasaďte na špičku a postupně ji rozviňte přes patu. Membránu tak zbytečně nenapínáte.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Sealskinz doporučuje prát ponožky naruby na programu pro ruční praní nebo vlnu do 40 °C. Sušit je nechte volně, nejdřív naruby a pak na líc. Nedávejte je na topení ani k jinému přímému zdroji tepla, který může membránu poškodit. Sušička je u Sealskinz povolená jen na nízkou teplotu. Membrána se podle výrobce nemusí znovu impregnovat. Vnitřní merino vrstva schne pomaleji než nylon zvenku, proto ponožky před dalším použitím nechte proschnout celé.</p>'
          '<p>U ostatních značek se řiďte štítkem uvnitř lemu. Obecně membránám škodí vysoká teplota, ostré předměty a silné ždímání.</p>'
          '<h2>Jak dlouho vydrží</h2>'
          '<p>Nejčastější příčinou, proč ponožka začne propouštět vodu, je propíchnutá membrána. Výrobci proto radí mít krátce zastřižené nehty na nohou a před obutím vysypat z bot kamínky, trny a jiné ostré věci. Membránu poškodí i dlouhé dření o rozbitou vložku boty. Jestli ponožka těsní, zjistíte, když ji obléknete a na chvíli vstoupíte do kbelíku s vodou, nebo ji naplníte vodou a podíváte se, zda neprosakuje.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte délku ponožky, materiál vnitřní vrstvy, určení podle počasí, tloušťku a velikostní tabulku. U Sealskinz sledujte, jestli má model pásek Hydrostop. Stejná ponožka se často prodává v několika barvách a velikostech, a ne každý obchod má skladem všechny velikosti.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Brodění hlouběji, než sahá lem ponožky.</li>'
          '<li>Menší velikost, protože běžné ponožky nosíte těsné.</li>'
          '<li>Sušení na topení nebo na kamnech.</li>'
          '<li>Dlouhé nehty a kamínek v botě, který membránu propíchne.</li>'
          '<li>Silná zimní ponožka nacpaná do těsné letní boty.</li></ul>'
          '<p>Do deště se hodí také <a href="/nepromokave-bundy/">nepromokavé bundy</a> a <a href="/nepromokave-kalhoty/">kalhoty</a>. Kdo hledá obyčejné teplé ponožky, najde <a href="/merino-ponozky/">merino ponožky</a>, <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> a <a href="/lyzarske-ponozky/">lyžařské ponožky</a>. Do mokrého terénu jsou určené také <a href="/trailove-boty/">trailové boty</a>.</p>',
    faq=[
        ('Jak fungují nepromokavé ponožky?', 'Mezi vnější a vnitřní pleteninou mají membránu, která nepustí vodu dovnitř a propouští vodní páru ven. Noha zůstane suchá i v mokré botě.'),
        ('Jsou nepromokavé ponožky opravdu vodotěsné?', 'Membrána ano, ale jen po lem ponožky. Voda, která steče po noze nebo nateče shora při brodění, se dovnitř dostane.'),
        ('Potí se noha v nepromokavých ponožkách?', 'Při velké zátěži a v teplé botě víc než v obyčejné ponožce. Membrána páru propouští, ale ne tak rychle jako běžná pletenina.'),
        ('Jakou velikost nepromokavých ponožek vybrat?', 'Podle tabulky konkrétní značky, protože membrána nepruží. Malá ponožka tlačí, velká dělá záhyby, které mohou dřít.'),
        ('Jak prát nepromokavé ponožky?', 'Sealskinz radí prát naruby na ruční nebo vlněný program do 40 °C a sušit volně, ne na topení. U jiných značek se řiďte štítkem.'),
        ('Proč nepromokavé ponožky začnou propouštět vodu?', 'Nejčastěji kvůli propíchnuté membráně, třeba dlouhým nehtem nebo kamínkem v botě. Pomáhá krátce zastřihnout nehty a botu před obutím vysypat.'),
        ('Co je Hydrostop u ponožek Sealskinz?', 'Pružný pásek bez silikonu na vnitřní straně lemu, který omezuje stékání vody po noze do ponožky. Při dlouhém nošení může dřít.'),
        ('Hodí se nepromokavé ponožky na kolo?', 'Ano, v dešti udrží nohy suché i v mokrých tretrách. V zimě je dobré kombinovat je s návleky na boty proti větru a vodě zvenku.'),
        ('Jaký je rozdíl mezi DexShell a Sealskinz?', 'Obě značky staví ponožky ze tří vrstev s membránou. DexShell používá membránu Porelle, Sealskinz vlastní Aquasealz. Liší se modely, střihy a tabulky velikostí.'),
        ('Kde koupit nepromokavé ponožky?', 'Sporteka porovná nabídky českých e-shopů u ponožek DexShell, Sealskinz a dalších značek. Vyberete velikost a koupíte v obchodě, který ji má.'),
    ])

# ------------------------------------------------------------------ potitka
NEW['potitka'] = dict(long=True,
    title='Potítka na zápěstí a čelenky proti pocení',
    desc='Potítka na zápěstí a na hlavu pro tenis, badminton, basketbal, běh i fitness. Materiály, šířka, velikost, praní a jak potítko nosit.',
    intro='<p><strong>Potítko</strong> je pruh savé látky, který zachytí pot dřív, než doteče tam, kde překáží. Potítko na zápěstí nedovolí potu stékat do dlaně a na grip rakety, potítko na hlavu, tedy čelenka, ho zastaví nad obočím, aby nepálil v očích. Nosí ho tenisté, badmintonisté, hráči squashe, basketbalisté, běžci i lidé, kteří cvičí ve fitku. Nejčastěji je z bavlněného froté s pružnou příměsí, takže drží bez gumičky a dá se vyprat s ostatním sportovním oblečením.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů, takže potítka různých značek porovnáte na jednom místě. V nabídce jsou potítka '
          + B(('head', 'Head'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('under-armour', 'Under Armour')) +
          ', Yonex, Wilson, Dunlop nebo Stiga. Potítka najdete v sekci <a href="/cepice-a-celenky/">čepice a čelenky</a>.</p>',
    guide='<h2>Potítko na zápěstí, nebo na hlavu</h2>'
          '<p>Oba typy dělají stejnou práci na jiném místě. Potítko na zápěstí se hodí do sportů s raketou nebo míčem, kde mokrá dlaň znamená horší úchop. Zároveň slouží jako ručník: hráči si jím mezi výměnami otírají čelo. Čelenka na hlavu drží pot mimo oči a vlasy mimo obličej a nosí se tam, kde ruce potřebujete na něco jiného.</p>'
          + T(['Typ', 'Kde se nosí', 'Typické sporty'], [
              ['Krátké potítko na zápěstí', 'těsně nad dlaní', 'tenis, badminton, squash, stolní tenis'],
              ['Dlouhé potítko na zápěstí', 'zápěstí a část předloktí', 'tenis, basketbal, volejbal'],
              ['Froté čelenka', 'přes čelo, nad obočím', 'tenis, basketbal, fitness'],
              ['Tenká funkční čelenka', 'přes čelo, i pod helmu', 'běh, cyklistika, kruhové tréninky'],
              ['Sada čelenka a dvě potítka', 'hlava a obě zápěstí', 'zápasy v horku, dlouhé tréninky']]) +
          '<h2>Kde se potítka používají</h2>'
          '<p>V <a href="/tenis/">tenise</a> nosí potítko na zápěstí většina hráčů rekreační i závodní úrovně. Pot ze zápěstí a předloktí by jinak stékal do dlaně a grip by klouzal. Mnoho hráčů ho má na ruce s raketou, aby dlaň zůstala suchá, a další na druhé ruce na otírání čela. Podobně se potítka používají v <a href="/badminton/">badmintonu</a>, <a href="/squash/">squashi</a> a <a href="/stolni-tenis/">stolním tenise</a>, kde je hra rychlá a na ručník není čas.</p>'
          '<p>V <a href="/basketbal/">basketbalu</a> a <a href="/volejbal/">volejbale</a> se nosí širší potítka na zápěstí i čelenky. Chrání míč a ruce před potem a k dresu patří i vzhledově. Při <a href="/beh/">běhu</a> a ve <a href="/fitness/">fitness</a> převládají čelenky, protože pot stéká hlavně z čela. Cyklisté nosí tenké čelenky pod helmou, kde by froté bylo příliš silné.</p>'
          '<h2>Materiály</h2>'
          '<p><strong>Bavlněné froté</strong> je nejrozšířenější. Smyčky na povrchu dobře sají a na kůži jsou měkké. Pružnost dodává příměs elastanu nebo jiných syntetických vláken, které drží potítko na místě. Nevýhodou je, že nasáklé froté schne pomalu a v horku je po čase těžké.</p>'
          '<p><strong>Funkční syntetické materiály</strong> pot nesají do sebe, ale odvádějí ho a rychle schnou. Hodí se na tenké čelenky na běh a pod helmu, které se nosí dlouho a nesmí tlačit. Některé čelenky mají na vnitřní straně proužek, který brání sjíždění.</p>'
          '<h2>Šířka a velikost</h2>'
          '<p>Krátká potítka na zápěstí jsou úzká a kryjí jen samotné zápěstí. Dlouhá potítka sahají až do půli předloktí a pojmou víc potu. U tenisových potítek se prodávají i velikosti XL pro širší zápěstí. Dětská potítka jsou užší a menší v obvodu.</p>'
          '<p>Potítko má sedět pevně, ale nesmí škrtit. Pokud po sundání zůstane na kůži hluboký otlak, je příliš malé. Čelenka na hlavu má držet i při skocích a otáčení hlavy, a přitom nesmí tlačit na spánky. Mnoho čelenek se prodává v jedné univerzální velikosti, ověřte si ale obvod, pokud máte menší nebo větší hlavu.</p>'
          '<h2>Jak potítko nosit</h2>'
          '<p>Potítko na zápěstí nasaďte těsně nad dlaň, aby nebránilo ohnutí zápěstí, ale zachytilo pot dřív, než doteče do dlaně. Pokud nosíte hodinky nebo sporttester, dejte potítko pod ně nebo nad ně podle toho, kde vám to při hře nevadí. Čelenku si nasaďte nad obočí, ne přes oči, a vlasy pod ní nechte volně. Při zápase se vyplatí mít náhradní pár v tašce. Mokré potítko už pot nepojme a ztrácí smysl.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Potítko je v kontaktu s potem po celou dobu tréninku a bez praní začne brzy zapáchat. Perte ho po každém použití, ideálně s ostatním sportovním oblečením podobných barev. Teplotu najdete na štítku. Bílé froté potítko bez potisku obvykle snese vyšší teplotu než barevné nebo s logem. Aviváž zanechává na vláknech film, po kterém froté hůř saje, proto ji raději vynechte. Sušte volně na vzduchu, na topení se může gumička ve vláknech poškodit.</p>'
          '<p>Potítka se časem vytahají a přestanou držet. Jakmile sjíždějí ze zápěstí nebo z hlavy, je čas na nový pár. Protože jde o drobnost, která se snadno ztratí v tašce, mnoho hráčů kupuje balení po dvou nebo třech kusech.</p>'
          '<h2>Potítko, grip a omotávka</h2>'
          '<p>Na rukojeti tenisové, badmintonové nebo squashové rakety je grip, přes který si hráči často dávají tenkou omotávku. Omotávka saje pot z dlaně a postupně se opotřebuje, takže se mění. Potítko na zápěstí jí pomáhá tím, že do dlaně nestéká pot z předloktí. Omotávka pak vydrží suchá déle a raketa méně klouže. Potítko ale nenahradí omotávku, protože dlaň se potí sama. Kdo se hodně potí, kombinuje savou omotávku, potítko a ručník na lavičce.</p>'
          '<h2>Barvy a pravidla oblékání</h2>'
          '<p>Potítka se prodávají v mnoha barvách, často sladěná s oblečením značky. Na většině rekreačních kurtů a v halách na barvě nezáleží. Některé kluby a turnaje ale mají pravidla oblékání. Nejznámější je Wimbledon, kde musí být oblečení hráčů bílé, a to se týká i čelenek a potítek. Před turnajem si proto pravidla přečtěte. Pro trénink stačí potítko jakékoli barvy, bílé je ale nejlépe vidět, kdy už je potřeba ho vyprat.</p>'
          '<h2>Potítka pro děti a začátečníky</h2>'
          '<p>Dětem na tréninku tenisu nebo basketbalu potítko pomůže hlavně v létě a v hale, kde je teplo. Vybírejte menší velikost, která nesjíždí, a raději balení s více kusy, protože se potítka v šatně snadno ztrácejí. Začínající hráči nemusí kupovat sady s čelenkou. Stačí jeden pár na zápěstí a podle potřeby čelenka, pokud pot stéká do očí.</p>'
'<h2>Jak poznat dobré potítko</h2>'
          '<p>Dobré potítko má husté a měkké smyčky froté, které na sebe pot rychle natáhnou. Řídké froté sice vypadá stejně, ale nasákne za pár minut a pak už jen klouže po kůži. Pružnost má být rovnoměrná po celém obvodu, bez tvrdého švu, který by tlačil na šlachy zápěstí. Po prvním praní by potítko nemělo výrazně srazit ani pustit barvu. Logo bývá vyšité nebo natištěné, vyšívané vydrží déle, natištěné časem popraská.</p>'
          '<h2>Potítko v horku</h2>'
          '<p>Při letním turnaji na antuce nebo v nevětrané hale nasákne potítko rychleji, než stihne vyschnout. Hráči proto potítka během zápasu střídají a mokrá si věší na tašku nebo opěradlo lavičky. Čelenku je dobré mít v horku i tehdy, když ji jinak nenosíte, protože pot v očích při podání nebo smeči rozhoduje o výměně. Kšiltovka chrání před sluncem, pot ale zachytí jen částečně. Mezi výměnami pijte a v přestávkách si potítka vyždímejte, ať jim vrátíte aspoň část savosti.</p>'
          '<p>Po zápase potítka nenechávejte smotaná v kapse tašky. Rozložte je, nechte proschnout a doma je hned vyperte. Froté, které zůstane vlhké celou noc, začne zapáchat a zápach se z něj při běžném praní špatně dostává.</p>'
'<h2>Potítko a hygiena</h2>'
          '<p>Potítko je osobní věc, stejně jako ručník. Nepůjčujte ho a nepoužívejte cizí. Kdo trénuje víckrát týdně, má mít aspoň dva páry, aby jeden mohl schnout. Potítko nechané přes noc ve sportovní tašce zapáchá a zapáchá pak i taška.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte typ (zápěstí, hlava, sada), šířku, materiál a počet kusů v balení. Potítka se prodávají po jednom kuse, v páru i v sadách s čelenkou, a cena za kus se tak mezi nabídkami liší. U dlouhých potítek a čelenek sledujte i velikost, u dětí obvod zápěstí a hlavy.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Jedno potítko na celý dlouhý zápas v horku.</li>'
          '<li>Silná froté čelenka pod cyklistickou helmou.</li>'
          '<li>Potítko nasazené vysoko na předloktí, odkud pot do dlaně stejně steče.</li>'
          '<li>Praní s aviváží a sušení na topení.</li>'
          '<li>Potítko nechané mokré v tašce do příštího tréninku.</li></ul>'
          '<p>Do tenisové tašky se kromě potítek hodí <a href="/tenisove-rakety/">tenisové rakety</a> a <a href="/tenisova-obuv/">tenisová obuv</a>. Proti slunci na kurtu pomůže <a href="/ksiltovky/">kšiltovka</a> a na trénink <a href="/funkcni-tricka/">funkční trička</a>.</p>',
    faq=[
        ('K čemu je potítko na zápěstí?', 'Zachytí pot, který stéká z předloktí do dlaně, takže raketa nebo míč neklouže. Hráči si jím také otírají čelo mezi výměnami.'),
        ('Na kterou ruku se nosí potítko?', 'Většina hráčů ho má na ruce, kterou drží raketu, aby dlaň zůstala suchá. Druhé potítko na volné ruce slouží k otírání čela.'),
        ('Z čeho jsou potítka?', 'Nejčastěji z bavlněného froté s příměsí elastanu nebo syntetických vláken. Tenké čelenky na běh a pod helmu bývají z funkčních materiálů.'),
        ('Jak prát potítka?', 'Po každém použití podle teploty na štítku, s podobnými barvami a bez aviváže, po které froté hůř saje. Sušte volně na vzduchu.'),
        ('Jak široké potítko vybrat?', 'Krátké potítko kryje jen samotné zápěstí. Dlouhé sahá do půli předloktí a pojme víc potu, hodí se do horka a na dlouhé zápasy.'),
        ('Jaká čelenka se hodí pod cyklistickou helmu?', 'Tenká čelenka z funkčního materiálu, která netlačí a rychle schne. Silné froté je pod helmou nepohodlné.'),
        ('Jak poznám, že potítko je příliš malé?', 'Po sundání zůstane na kůži hluboký otlak nebo potítko škrtí. Správné potítko drží pevně, ale netlačí.'),
        ('Kdy potítko vyměnit?', 'Když se vytahá a sjíždí ze zápěstí nebo hlavy, nebo když po praní přestane sát. Potítka jsou levná a vyplatí se mít víc párů.'),
        ('Hodí se potítka i pro děti?', 'Ano, prodávají se menší dětská potítka a čelenky. Vybírejte podle obvodu zápěstí a hlavy, aby nesjížděla.'),
        ('Kde koupit potítka?', 'Sporteka porovná nabídky českých obchodů u potítek a čelenek značek Head, Nike, Yonex a dalších. Vyberete balení a nakoupíte v obchodě.'),
    ])

# ------------------------------------------------------------------ suspenzory
NEW['suspenzory'] = dict(long=True,
    title='Suspenzory pro hokej, bojové sporty i brankáře',
    desc='Sportovní suspenzory s pevnou mušlí: klasické, kraťasy a kalhoty se suspenzorem, dámské i dětské. Velikosti, materiály a péče.',
    intro='<p><strong>Sportovní suspenzor</strong> je chránič rozkroku. Tvoří ho pevná tvarovaná mušle, obvykle z plastu s měkkým lemem, a textilní držák, který ji udrží na místě. Držákem může být klasický suspenzor s pásem a pružnými pásky, slipy nebo kompresní kraťasy s kapsou na mušli nebo hokejové kraťasy a kalhoty se suchými zipy na štulpny. Nosí se při hokeji, v bojových sportech, v brankovišti míčových sportů a všude, kde hrozí zásah pukem, míčem, holí, kolenem nebo kopem.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů u suspenzorů '
          + B(('winnwell', 'Winnwell'), ('bauer', 'Bauer'), ('ccm', 'CCM'), ('insportline', 'Insportline')) +
          ', RDX, DBX Bushido, Venum, Ringhorns nebo Opus. Suspenzory patří do sekce <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>. Jde o sportovní ochranné vybavení, ne o zdravotnickou pomůcku.</p>',
    guide='<h2>Z čeho se suspenzor skládá</h2>'
          '<p>Hlavní částí je mušle. Je z tvrdého plastu, který při úderu rozloží sílu do větší plochy a přenese ji na pánev. Okraj mušle bývá obšitý nebo obložený pěnou či gelem, aby netlačil do třísel. Mnoho mušlí má větrací otvory. Druhou částí je držák. Ten musí mušli udržet přesně na místě, protože posunutá mušle chrání méně a navíc dře.</p>'
          '<p>Pozor na název. Slovem suspenzor se někdy označuje také podpůrné prádlo bez mušle, které nic nechrání. V této kategorii jsou sportovní chrániče s mušlí a k nim několik držáků bez mušle, které se kupují na výměnu.</p>'
          '<h2>Typy suspenzorů</h2>'
          + T(['Typ', 'Jak vypadá', 'Kde se nosí'], [
              ['Klasický suspenzor', 'pružný pás a pásky přes hýždě, kapsa s mušlí', 'bojové sporty, trénink, starší výstroj'],
              ['Slipy nebo boxerky s kapsou', 'přiléhavé spodní prádlo s vyjímatelnou mušlí', 'bojové sporty, míčové hry'],
              ['Hokejové kraťasy se suspenzorem', 'kompresní nebo síťované kraťasy se suchými zipy', 'hokej, in-line hokej'],
              ['Hokejové kalhoty se suspenzorem', 'dlouhé kompresní kalhoty s mušlí a suchými zipy', 'hokej, chladnější haly'],
              ['Brankářský suspenzor', 'větší mušle s ochranou podbřišku a stehen', 'brankáři v hokeji a házené'],
              ['Thajský kovový suspenzor', 'ocelová mušle v koženém potahu se šněrováním', 'thajský box'],
              ['Dámský chránič pánve', 'plošší tvar, kraťasy Jill nebo slip', 'hokej, bojové sporty, brankářky']]) +
          '<h2>Hokej</h2>'
          '<p>Hokejisté nosí suspenzor zabudovaný do kraťasů nebo kalhot. Na přední a zadní straně nohavic mají suché zipy, na které se přichytí štulpny, takže pod chrániči nic nesjíždí. Kompresní kraťasy drží mušli nejpevněji. Síťované kraťasy jsou volnější a lépe větrají. Shock Doctor doporučuje nosit hokejovou mušli s kompresními kraťasy určenými pro hokej, aby se při bruslení neposouvala. Winnwell nabízí řadu Jock pro chlapce a muže a řadu Jill pro dívky a ženy, obě ve verzi kraťasů i dlouhých kalhot.</p>'
          '<p>Brankáři mají vlastní suspenzory. Jejich mušle je větší, kryje i podbřišek a vnitřní stranu stehen a počítá se střelami z bezprostřední blízkosti. Brankářské suspenzory má v nabídce například Bauer. Vlastní brankářské suspenzory se vyrábějí i pro házenkářské brankáře. Další hokejovou výstroj najdete v kategoriích <a href="/hokejove-chranice/">hokejové chrániče</a> a <a href="/hokejove-brankarske-vybaveni/">brankářské vybavení</a>.</p>'
          '<h2>Bojové sporty</h2>'
          '<p>V kickboxu, karate, MMA nebo thajském boxu hrozí zásah kolenem nebo kopem do rozkroku i při sparingu. Většina bojovníků nosí tvrdou mušli s přiléhavými kompresními kraťasy nebo klasickým suspenzorem. Suspenzory pro bojové sporty bývají obšité textilem nebo koženkou a mají široký pás, který se při pohybu neroluje. V thajském boxu se tradičně používají kovové mušle v koženém potahu, které se zavazují šňůrkami, například od výrobců Twins nebo Fairtex.</p>'
          '<p>Při závodech a turnajích se řiďte pravidly konkrétního svazu a soutěže. V mnoha bojových sportech je chránič rozkroku pro muže povinný a pravidla někdy určují i jeho typ. Pro ženy existují chrániče pánve s plošším tvarem. Další ochranné vybavení, jako jsou <a href="/chranice-zubu/">chrániče zubů</a> nebo rukavice, je v sekci <a href="/bojove-sporty/">bojové sporty</a>.</p>'
          '<h2>Další sporty</h2>'
          '<p>Chránič rozkroku se nosí i v míčových sportech s tvrdým míčem. Pálkaři v kriketu ho mají pod kalhotami, v baseballu a softballu ho používají hlavně chytači a hráči blízko pálkaře. Brankáři ve florbale, házené a pozemním hokeji jsou vystaveni střelám z malé vzdálenosti a mušli nosí běžně. Pro tyto sporty se hodí kompresní slipy nebo kraťasy s kapsou, které nepřekážejí v běhu. Na fotbal a ragby se suspenzor nosí výjimečně, mnoha hráčům v běhu vadí.</p>'
          '<p>Kdo s mušlí začíná, potřebuje si zvyknout. První tréninky může mušle tlačit a omezovat v širokých krocích. Vyzkoušejte ji doma při dřepech a výpadech, a pokud tlačí i po několika trénincích, zkuste jinou velikost nebo tvar. Pomoci může i jiný držák, protože kompresní kraťasy drží mušli jinak než klasický suspenzor s pásky.</p>'
          '<p>Na trénink si suspenzor oblékejte vždy, nejen na zápasy a sparingy. Zásah přichází nečekaně, často při obyčejném cvičení ve dvojicích nebo při střelbě na brankáře před tréninkem.</p>'
'<h2>Jak vybrat velikost</h2>'
          '<p>Suspenzory se prodávají ve velikostech podle obvodu pasu nebo v hokejovém značení YTH, JR a SR, tedy dětská, juniorská a dospělá velikost. Shock Doctor radí změřit obvod pasu měkkým krejčovským metrem zhruba 2,5 cm nad kyčlemi a při hodnotě mezi dvěma velikostmi zvolit větší. Dětské mušle jsou nejen menší, ale mají i jiný tvar než mušle pro dospělé, proto dítěti nekupujte malou dospělou velikost.</p>'
          '<p>Správná mušle sedí pevně u těla, netlačí, neposouvá se a nezůstává pod ní volné místo. Při dřepu, výpadu nebo bruslení se nesmí přesunout do strany. Pokud tlačí lem do třísel, je mušle příliš velká nebo má nevhodný tvar. Pokud se při běhu hýbe, je držák příliš volný. Děti rostou rychle, velikost je potřeba kontrolovat před každou sezónou.</p>'
          '<h2>Mušle a větrání</h2>'
          '<p>Mušle se liší tvarem, tuhostí okraje a větráním. Některé mají pevný plastový skelet s pružnějším lemem, který se přizpůsobí tělu. Jiné kombinují tvrdou vnější vrstvu s pěnou uvnitř. Větrací otvory pomáhají při dlouhých trénincích, mušle bez otvorů bývá tužší. Kovová mušle chrání před tvrdým úderem, ale je těžší a méně pohodlná na běhání.</p>'
          '<p>Mušle je často vyjímatelná a dá se koupit i samostatně. Hodí se to, když se kraťasy roztrhnou nebo vytahají a mušle je stále v pořádku, nebo když potřebujete jinou velikost mušle do stejných kraťasů. Ověřte si, že náhradní mušle pasuje do kapsy vašeho držáku.</p>'
          '<h2>Dívky a ženy</h2>'
          '<p>Ženské chrániče pánve mají plošší a širší tvar, který odpovídá ženské anatomii. V hokeji se nosí v kraťasech nebo kalhotách označovaných Jill, které mají stejné suché zipy na štulpny jako pánské. Pro bojové sporty se prodávají dámské suspenzory se širokým pasem, například od Ringhorns. Mužský suspenzor ženám nesedí a mušle se v něm posouvá.</p>'
          '<h2>Péče a hygiena</h2>'
          '<p>Suspenzor se při tréninku propotí víc než jakákoli jiná část výstroje. Po každém tréninku ho vyndejte z tašky a nechte vyschnout na vzduchu, nejlépe s vyjmutou mušlí. Textilní část perte podle štítku, kompresní kraťasy obvykle na šetrný program bez aviváže. Mušli umyjte vlažnou vodou s mýdlem a nechte oschnout. Na topení ani do sušičky ji nedávejte, plast se teplem může zdeformovat.</p>'
          '<p>Mušli vyměňte, když je prasklá, má ostrou hranu nebo se zdeformovala. Kraťasy vyměňte, když se vytahají a mušle v nich přestane držet. Suspenzor je osobní věc a půjčovat se nemá.</p>'
          '<h2>Bezpečnost</h2>'
          '<p>Suspenzor riziko zranění snižuje, ale úplnou ochranu nezaručí. Při silném úderu může bolest přijít i přes mušli. Pokud bolest po zásahu neustupuje, objeví se otok, změna barvy nebo krev v moči, vyhledejte lékaře a nečekejte, až to přejde. Suspenzor není zdravotnický prostředek a nepoužívá se k léčbě.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte typ držáku, velikost, materiál a tvar mušle, větrání a to, jestli je mušle vyjímatelná. U hokejových kraťasů sledujte suché zipy na štulpny a střih (kompresní, nebo síťovaný). Stejný model se často prodává v dětské, juniorské i dospělé velikosti a v pánské a dámské verzi, proto si název nabídky přečtěte celý.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Dítě v malé dospělé velikosti místo dětské mušle.</li>'
          '<li>Volný držák, ve kterém se mušle při pohybu posouvá.</li>'
          '<li>Pánský suspenzor pro hráčku nebo bojovnici.</li>'
          '<li>Mokrý suspenzor nechaný v tašce do dalšího tréninku.</li>'
          '<li>Prasklá mušle používaná další sezónu.</li></ul>'
          '<p>Pod hokejovou výstroj se hodí <a href="/hokejove-dresy-a-obleceni/">hokejové oblečení</a>, na bojové sporty <a href="/obleceni-bojove-sporty/">oblečení pro bojové sporty</a>, <a href="/boxerske-rukavice/">boxerské rukavice</a> a <a href="/mma-rukavice/">MMA rukavice</a>. Brankáři v házené najdou další vybavení v kategorii <a href="/hazena/">házená</a>.</p>',
    faq=[
        ('K čemu slouží sportovní suspenzor?', 'Chrání rozkrok před zásahem pukem, míčem, holí, kolenem nebo kopem. Tvrdá mušle rozloží úder do větší plochy. Nejde o zdravotnickou pomůcku.'),
        ('Jak vybrat velikost suspenzoru?', 'Podle obvodu pasu a tabulky výrobce, v hokeji podle značení YTH, JR a SR. Shock Doctor radí měřit asi 2,5 cm nad kyčlemi a mezi velikostmi zvolit větší.'),
        ('Jak má suspenzor sedět?', 'Mušle má přiléhat pevně k tělu, nesmí tlačit lemem do třísel ani se posouvat při dřepu, běhu nebo bruslení.'),
        ('Jaký suspenzor na hokej?', 'Hokejové kraťasy nebo kalhoty se suspenzorem a suchými zipy na štulpny. Kompresní drží mušli nejpevněji, síťované lépe větrají.'),
        ('Potřebují brankáři jiný suspenzor?', 'Ano. Brankářské suspenzory mají větší mušli, která kryje i podbřišek a vnitřní stranu stehen. Vyrábějí se pro hokej i házenou.'),
        ('Existují suspenzory pro ženy?', 'Ano, jako chrániče pánve s plošším tvarem. V hokeji se nosí v kraťasech nebo kalhotách Jill, v bojových sportech jako dámské suspenzory.'),
        ('Je suspenzor povinný v bojových sportech?', 'Na mnoha soutěžích pro muže ano, pravidla ale určuje konkrétní svaz a soutěž. Před turnajem si je přečtěte.'),
        ('Jak prát suspenzor?', 'Textilní část podle štítku, obvykle na šetrný program. Mušli umyjte vlažnou vodou s mýdlem a nechte oschnout mimo topení.'),
        ('Kdy suspenzor vyměnit?', 'Když mušle praskne, zdeformuje se nebo má ostrou hranu, nebo když se držák vytahá a mušle se v něm hýbe. U dětí kontrolujte velikost každou sezónu.'),
        ('Co dělat po silném úderu do rozkroku?', 'Pokud bolest neustupuje nebo se objeví otok, změna barvy či krev v moči, vyhledejte lékaře. Suspenzor riziko snižuje, ale úplnou ochranu nezaručí.'),
    ])
