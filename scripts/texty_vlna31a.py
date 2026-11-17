"""sporteka.cz — wave 31a (17. 11. 2026): long texts for akupresurni-podlozky, chodici-pasy, airtracky-a-zinenky, otuzovaci-kade.
General true facts only, no prices, no product counts. Acupressure mats and cold-water tubs are described without health
promises: they are not medical devices, the research on mats is small and mostly about subjective relaxation, and people
with health problems are sent to a doctor. Cold-water immersion with explicit safety rules (never alone, short exposure,
afterdrop, heart and blood pressure, no alcohol, no driving until warm). Walking pad and airtrack figures are quoted only as
examples taken from the maker's own data sheet. Brands linked only if present in src/texts/znacky.json, the rest plain text.

Sources:
- inSPORTline AKU-1000 manual (CZ, PDF on insportline.cz): ABS spike plates, 100% cotton cover, soft foam filling, size 125x50x2 cm
- ShaktiMat help centre "contraindications" (blood thinners, pregnancy, skin) and reviews of mat studies (2011 exploratory study:
  subjective relaxation, no change in salivary cortisol; no systematic review specific to mats)
- Virtufit WP50 data (fitnessbenelux.nl, direct-running.com, CZ manual): 0.8-8 km/h, 1 HP continuous / 1.5 HP peak, belt 100x40 cm;
  Virtufit Walkingpad 100: max user 100 kg
- inSPORTline Airstunt 500x100x10 (insportline.eu): PVC drop-stitch, 1.5-2 PSI (0.1-0.14 bar) with a hand/foot pump,
  electric pump included, EN 12503-1 / EN 14960-1 / EN 15649-1, usable on water
- inSPORTline FrostZen Pro II (insportline.eu): 375 l, cover, thermometer; separate thermoregulation unit 0-55 °C
- UNSW / ScienceAlert / PsyPost articles on ice-bath risks (cold shock, heart attack or stroke risk with undiagnosed conditions,
  never alone, afterdrop, no driving until rewarmed)
Left out (not verifiable): exact afterdrop duration, a recommended number of minutes in the tub, typical airtrack pressure
for 20 cm models, spike counts of individual mats, noise levels in dB.
"""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ akupresurni-podlozky
NEW['akupresurni-podlozky'] = dict(long=True,
    title='Akupresurní podložky a sady s polštářem',
    desc='Akupresurní podložky s plastovými hroty, sady s polštářem i podložky na chodidla. Rozměry, materiály, praní potahu a kdy se poradit s lékařem.',
    intro='<p><strong>Akupresurní podložka</strong> je pěnová matrace potažená látkou, na které jsou našité stovky malých plastových destiček. Každá destička má tvar květu a nese desítky tupých hrotů. Když si na podložku lehnete, váha těla se rozloží do tisíců bodů a kůže cítí silné píchání, které po chvíli přejde v teplo. Lidé ji používají hlavně k odpočinku po práci, k ležení před spaním nebo jako doplněk k protahování. Často se jí říká „Shakti“ podle obchodního názvu jedné ze značek.</p>'
          '<p>Na Sportece jsou vedle sebe nabídky českých obchodů, takže u každé podložky nebo sady uvidíte, který e-shop ji právě prodává. Najdete tu samostatné podložky, sady s polštářem, menší podložky na chodidla i rozšíření s náplní z pohanky nebo kokosu, mimo jiné od '
          + B(('insportline', 'Insportline'), ('hms', 'HMS'), ('merco', 'Merco')) +
          ' nebo Bodhi. Podložky patří mezi <a href="/masazni-pomucky/">masážní pomůcky</a>. Nejde o zdravotnický prostředek a léčbu nenahrazují.</p>',
    guide='<h2>Jak je akupresurní podložka postavená</h2>'
          '<p>Základ tvoří pěnová výplň silná zhruba dva až tři centimetry. Kolem ní je potah, obvykle z bavlny nebo lnu, a na něm řady plastových destiček. Destičky bývají z ABS nebo podobného tvrdého plastu a mají tvar lotosového květu s hroty. Hroty jsou tupé, kůži nepropíchnou, ale při ležení je cítit každý z nich. Výrobce Insportline například u modelu AKU-1000 uvádí rozměr 125 × 50 × 2 cm, bavlněný potah a destičky z ABS.</p>'
          '<p>Hustota destiček rozhoduje o tom, jak ostře podložka působí. Čím víc hrotů na stejné ploše, tím víc se váha těla rozloží a tím je pocit mírnější. Řidší rozmístění znamená méně bodů a ostřejší vjem. Kdo podložku zkouší poprvé, bývá překvapený, jak intenzivní prvních pár minut je. Proto se začíná přes tenké tričko nebo na kratší dobu.</p>'
          + T(['Typ', 'Jak vypadá', 'K čemu se hodí'], [
              ['Samostatná podložka', 'obdélník kolem 65–75 × 40–45 cm', 'ležení na zádech, sezení, stání'],
              ['Dlouhá podložka', 'délka přes 120 cm', 'ležení celými zády i s nohama'],
              ['Sada s polštářem', 'podložka a válec nebo polštář s hroty', 'podložení šíje, ležení na boku'],
              ['Podložka na chodidla', 'menší čtverec, někdy s kamínky nebo kolíky', 'stání a přešlapování na místě'],
              ['Balanční dráha s hroty', 'díly k poskládání do cesty', 'hry a chůze naboso pro děti']]) +
          '<h2>Jak se podložka používá</h2>'
          '<p>Nejběžnější je ležení na zádech. Podložku položte na koberec nebo na postel, ne na tvrdou dlažbu, a lehněte si pomalu, aby se váha rozložila rovnoměrně. Prvních pár minut bývá nepříjemných, pak se většině lidí uleví. Začátečníci leží kratší dobu a postupně ji prodlužují podle toho, jak to snášejí. Po vstání je kůže zarudlá a jsou na ní otisky hrotů, které obvykle za chvíli zmizí.</p>'
          '<p>Další možností je sezení na podložce opřené o opěradlo židle nebo stání naboso. Při stání je tlak na chodidla velký, takže se většinou začíná vsedě s nohama položenýma na podložce. Polštář ze sady se podkládá pod krk nebo se na něj pokládají lýtka. Někdo si podložku dává pod záda při poslechu hudby nebo při dechovém cvičení, jiný ji používá po <a href="/joga-a-pilates/">józe a pilates</a> jako klidovou část.</p>'
          '<h2>Co říká výzkum</h2>'
          '<p>Prodejci často uvádějí dlouhý seznam účinků, od lepšího spánku po úlevu od bolesti. Studií přímo o akupresurních podložkách je ale málo a jsou malé. Ve větší míře popisují, že se lidé na podložce cítí uvolněněji. Objektivně měřené ukazatele, například hladina stresového hormonu ve slinách, se v nich výrazně neměnily. Výzkum klasické akupresury, kterou provádí terapeut prsty na konkrétních bodech, se na podložku nedá jednoduše přenést.</p>'
          '<p>Rozumné je brát podložku jako pomůcku pro odpočinek, jako by šlo o teplou koupel nebo masáž. Pokud vám ležení na ní dělá dobře, je to v pořádku. Při bolestech zad, nespavosti nebo jiných potížích, které trvají delší dobu, ale nemá smysl spoléhat jen na podložku. V takové situaci je na místě návštěva lékaře nebo fyzioterapeuta.</p>'
          '<h2>Kdo by měl být opatrný</h2>'
          '<p>Hroty tlačí na kůži a zvyšují v daném místě prokrvení. Výrobci proto sami uvádějí skupiny lidí, kterým podložku bez porady s lékařem nedoporučují. Sepsali jsme nejčastější z nich:</p>'
          '<ul><li><strong>Těhotenství:</strong> o používání se poraďte s lékařem nebo porodní asistentkou.</li>'
          '<li><strong>Léky na ředění krve:</strong> při užívání antikoagulancií se snáz tvoří modřiny, výrobci podložku v takovém případě nedoporučují.</li>'
          '<li><strong>Kožní potíže:</strong> rány, ekzém, popáleniny, záněty nebo citlivá pokožka na místě, kde má podložka působit.</li>'
          '<li><strong>Snížená citlivost:</strong> například při poškození nervů u cukrovky, kdy člověk necítí, že je tlak už příliš silný.</li>'
          '<li><strong>Srdeční a cévní onemocnění, epilepsie, onkologická léčba:</strong> vždy až po souhlasu lékaře.</li></ul>'
          '<p>U dětí je dobré používání hlídat a omezit ho na hravé formy, například chůzi po balanční dráze. Malé děti by na podložce neměly usínat bez dozoru.</p>'
          '<h2>Rozměr a výplň</h2>'
          '<p>Menší podložky kolem 70 × 40 cm pokryjí záda od lopatek po kříž. Na celé tělo, nebo pokud jste vysocí, je pohodlnější delší model přes 120 cm. Sada s polštářem dává víc možností, polštář ale zabere místo ve skříni. Tloušťka pěny ovlivňuje, jak moc se podložka na posteli prohýbá. Tenká pěna na tvrdé podlaze působí ostřeji, silnější výplň tlak trochu změkčí.</p>'
          '<p>Kromě pěny se prodávají i podložky a polštáře s náplní z pohankových slupek nebo kokosových vláken. Lépe se přizpůsobí tvaru těla a pohanka trochu šustí. Náplň se dá u některých modelů vysypat, aby se potah mohl vyprat zvlášť.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Potah je v kontaktu s kůží a časem nasákne pot. U většiny sad jde pěnová vložka vyjmout a potah s destičkami vyprat ručně ve vlažné vodě. Pračka a sušička hroty i lepení destiček poškodí, pokud to výrobce výslovně nedovoluje. Po vyprání nechte potah volně uschnout a teprve pak do něj vraťte pěnu. Uložte podložku naplocho nebo srolovanou hroty dovnitř, aby se destičky neodlamovaly.</p>'
          '<p>Když se destička uvolní nebo praskne, může mít ostrou hranu. Takovou podložku je lepší přestat používat na holé tělo. Pokud podložka nepříjemně páchne po plastu, nechte ji před prvním použitím několik dní vyvětrat.</p>'
          '<h2>Akupresurní podložka a cvičení</h2>'
          '<p>Podložka s hroty není náhrada podložky na cvičení. Na hrotech se nedá dělat prkno ani kliky, a pokud na ní budete chodit v botách, destičky se rychle ulomí. Hodí se na konec tréninku, kdy si lehnete a necháte tělo vydýchat. Někteří lidé ji střídají s protahováním na válci nebo s ležením na rovné zemi. Pokud po cvičení podložku používáte na zpocené tělo, dejte si mezi kůži a hroty tenké bavlněné tričko. Potah pak zůstane déle čistý a nemusíte ho prát tak často.</p>'
          '<p>Na cesty se hodí menší podložka, která se srolovaná vejde do tašky. Velkou sadu s polštářem si nechte doma. Podložku na chodidla je možné mít pod pracovním stolem a během dne na ni občas položit bosé nohy. Při stání se tlak soustředí do malé plochy, takže s tím začínejte opatrně a raději vsedě.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejná podložka se často prodává v několika barvách a pod mírně odlišným názvem. Porovnávejte hlavně rozměr, materiál potahu a destiček, odnímatelnost potahu a to, zda je v balení polštář nebo taška. Pozor na rozdíl mezi podložkou a rozšířením: „rozšíření“ s náplní z pohanky je jen doplněk, ne kompletní podložka. Dětské balanční dráhy s akupresurním povrchem jsou spíš hračka na pohyb než pomůcka na ležení.</p>'
          '<p>Před nákupem si přečtěte i návod a upozornění výrobce. Najdete tam, jak podložku prát, a seznam situací, kdy ji nepoužívat. Pokud návod v nabídce chybí, můžete si ho vyžádat od obchodu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Ležení na podložce poprvé hned dlouhou dobu a bez trička.</li>'
          '<li>Podložka položená na studenou dlažbu, kde hroty tlačí nejvíc.</li>'
          '<li>Praní celé podložky v pračce i s pěnovou výplní.</li>'
          '<li>Používání na podrážděné kůži nebo čerstvých odřeninách.</li>'
          '<li>Spoléhání na podložku při dlouhodobé bolesti místo vyšetření.</li></ul>'
          '<p>K uvolnění po cvičení se hodí i <a href="/masazni-valce/">masážní válce</a> a <a href="/masazni-pistole/">masážní pistole</a>. Kdo hledá podložku na cvičení, ne na ležení s hroty, najde ji v kategorii <a href="/joga-a-podlozky/">jóga a podložky</a>. Na klidné ležení po dechovém cvičení se hodí také pomůcky pro <a href="/meditace/">meditaci</a>.</p>',
    faq=[
        ('Jak dlouho ležet na akupresurní podložce?', 'Začněte několika minutami přes tenké tričko a dobu prodlužujte podle toho, jak to snášíte. Když je pocit nepříjemný i po chvíli, z podložky slezte.'),
        ('Je akupresurní podložka zdravotnický prostředek?', 'Ne. Je to pomůcka pro odpočinek a uvolnění. Studie o podložkách jsou malé a léčbu ani vyšetření nenahrazují.'),
        ('Kdo by akupresurní podložku neměl používat?', 'Bez porady s lékařem ji nepoužívejte v těhotenství, při užívání léků na ředění krve, při kožních potížích, snížené citlivosti nebo vážných onemocněních srdce a cév.'),
        ('Proč mám po podložce červená záda?', 'Hroty tlačí na kůži a místo se prokrví. Zarudnutí a otisky obvykle brzy zmizí. Pokud zůstávají modřiny nebo kůže pálí, podložku vynechte.'),
        ('Dá se akupresurní podložka prát?', 'Potah s destičkami se většinou pere ručně ve vlažné vodě po vyjmutí pěny. Pračku a sušičku používejte jen tehdy, když to výrobce povoluje.'),
        ('Jakou velikost podložky vybrat?', 'Na záda stačí podložka kolem 70 × 40 cm. Pro vysoké lidi nebo ležení s nohama je pohodlnější délka přes 120 cm.'),
        ('Na čem podložku používat?', 'Na koberci, karimatce nebo posteli. Na tvrdé dlažbě působí hroty ostřeji, na měkké matraci naopak mírněji.'),
        ('Má smysl sada s polštářem?', 'Pokud chcete podložit krk nebo ležet na boku, ano. Kdo podložku používá hlavně na záda a vsedě, vystačí si se samotnou podložkou.'),
        ('Mohou akupresurní podložku používat děti?', 'Spíš v podobě her, například chůze naboso po balanční dráze s výstupky. Ležení na podložce je u dětí lepší hlídat a nenechat je na ní usnout.'),
        ('Kde koupit akupresurní podložku?', 'Sporteka u každé podložky a sady ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ chodici-pasy
NEW['chodici-pasy'] = dict(long=True,
    title='Chodicí pásy a walking pady pod stůl i do bytu',
    desc='Chodicí pásy (walking pady) na chůzi doma i pod pracovním stolem. Rozsah rychlosti, nosnost, motor, rozměr pásu, hlučnost a bezpečnost.',
    intro='<p><strong>Chodicí pás</strong>, často nazývaný anglicky <strong>walking pad</strong>, je nízký a lehký trenažér na chůzi. Na rozdíl od běžeckého pásu nemá vysoký rám s madly a ovládacím panelem, takže se vejde pod postel, za skříň nebo pod zvýšený pracovní stůl. Jezdí pomaleji, většinou do zhruba šesti až osmi kilometrů za hodinu, a ovládá se dálkovým ovladačem nebo aplikací v telefonu. Hodí se pro lidi, kteří chtějí víc chodit, ale venku na to nemají čas nebo počasí.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů, takže u konkrétního pásu uvidíte, kde je k mání. Objednávku pak dokončíte v obchodě, který si zvolíte. V nabídce jsou modely značek '
          + B(('insportline', 'Insportline'), ('hms', 'HMS')) +
          ', Virtufit, Vifito nebo Hop-sport. Chodicí pásy jsou součástí kategorie <a href="/kardio-trenazery/">kardio trenažéry</a>, na rychlou chůzi do kopce a běh jsou určené klasické <a href="/behaci-pasy/">běžecké pásy</a>.</p>',
    guide='<h2>Chodicí pás, nebo běžecký pás</h2>'
          '<p>Oba stroje mají motor, který točí nekonečný pás, ale každý je stavěný na jiné tempo. Běžecký pás má delší a širší běžeckou plochu, silnější motor, vyšší rychlosti a obvykle i nastavitelný sklon. Má pevná madla a panel, ze kterého se ovládá rychlost a kde je bezpečnostní klíček. Je těžký a zabere v místnosti stálé místo.</p>'
          '<p>Chodicí pás je naopak plochá deska vysoká jen několik centimetrů. Plocha pro chůzi je kratší, u modelu Virtufit WP50 například 100 × 40 cm. To na klidnou chůzi stačí, na běh ne. Rychlost končí u většiny modelů mezi šesti a osmi kilometry za hodinu. Existují i kombinované typy 2 v 1, které po vyklopení madla zvládnou pomalý běh. Na pravidelné běhání je ale pořád lepší plnohodnotný běžecký pás.</p>'
          + T(['Parametr', 'Chodicí pás', 'Běžecký pás'], [
              ['Rychlost', 'obvykle do 6–8 km/h', 'běžně přes 12 km/h'],
              ['Madlo', 'žádné, nízké nebo sklopné', 'pevná madla a panel'],
              ['Plocha pásu', 'kratší a užší', 'delší a širší'],
              ['Sklon', 'většinou bez sklonu, výjimečně ruční nebo nízký', 'často elektricky nastavitelný'],
              ['Uložení', 'pod postel, za skříň, někdy se skládá napůl', 'stálé místo, některé jdou sklopit']]) +
          '<h2>Chůze pod stolem</h2>'
          '<p>Hodně lidí si walking pad kupuje k výškově nastavitelnému stolu. Při práci jdou pomalým tempem, třeba při telefonátech nebo čtení, a na soustředěnou práci se zastaví nebo si sednou. Psaní na klávesnici při chůzi chce cvik a pomalou rychlost. Stůl by měl být v takové výšce, aby lokty byly zhruba v pravém úhlu a ramena volná. Monitor ve výšce očí šetří krk.</p>'
          '<p>Před nákupem změřte prostor pod stolem. Pás musí vyčnívat dopředu i dozadu tak, abyste nenaráželi koleny do desky a měli za sebou volné místo. Hlídejte nohy stolu a kabely, které nesmějí vést přes pás ani pod ním. Kdo počítá s chůzí pod stolem celý den, měl by si zvyknout postupně a střídat chůzi se sezením a stáním.</p>'
          '<h2>Motor, nosnost a plocha</h2>'
          '<p>U motoru výrobci uvádějí výkon v koňských silách, často zvlášť trvalý a špičkový. Trvalý výkon je pro srovnání důležitější, protože ho motor zvládne dlouhodobě. Například Virtufit WP50 má podle prodejců trvalý výkon 1 HP a špičkový 1,5 HP. Slabší motor u těžšího uživatele víc hřeje, hlučí a rychleji se opotřebí.</p>'
          '<p>Maximální nosnost bývá u menších modelů okolo 100 kg, odolnější pásy unesou víc. Údaj berte vážně a nechte si rezervu, protože se vztahuje i k životnosti motoru a desky. Šířka pásu ovlivňuje, jak snadno z něj sešlápnete, když se zadíváte do monitoru. Delší plocha dává volnější krok vysokým lidem. Pokud měříte přes 185 cm, vyplatí se hledat model s delším pásem.</p>'
          '<h2>Ovládání a bezpečnost</h2>'
          '<p>Chodicí pásy se ovládají malým dálkovým ovladačem, tlačítky na desce nebo aplikací v telefonu. Některé modely mají automatický režim, kdy pás mění rychlost podle toho, kde na něm stojíte. Kolem stroje ale nikdy není madlo, kterého byste se chytili při zakopnutí. Proto začínejte na nízké rychlosti a zvyšujte ji až po pár minutách.</p>'
          '<ul><li><strong>Zastavení:</strong> zjistěte, jak pás rychle zastavit. Některé modely mají bezpečnostní klíček s magnetem, jiné spoléhají jen na ovladač.</li>'
          '<li><strong>Děti a zvířata:</strong> pás má za sebou mezeru, kde může něco skřípnout. Po skončení ho vypněte ze zásuvky a ovladač uschovejte.</li>'
          '<li><strong>Obuv:</strong> choďte v pevných sportovních botách, ne v ponožkách. V ponožkách noha na pásu klouže a není ničím chráněná.</li>'
          '<li><strong>Kabel:</strong> zapojte pás přímo do zásuvky, ne přes dlouhý prodlužovací kabel vedený pod nohama.</li></ul>'
          '<h2>Hluk a podlaha</h2>'
          '<p>Motor i dopady kroků přenáší deska do podlahy. V paneláku nebo v podkroví to sousedé pod vámi uslyší víc než vy. Pomůže pevná pryžová podložka pod trenažér, která tlumí vibrace a chrání podlahu před poškrábáním. Plovoucí podlaha a koberec s vysokým vlasem nejsou ideální podklad. Koberec může ucpat větrání motoru a pod pás se táhne prach.</p>'
          '<p>Hluk motoru stoupá s rychlostí a s hmotností uživatele. Pokud chcete chodit při videohovorech, vyzkoušejte, jak zní pás v nejpomalejším tempu, a čtěte recenze právě s ohledem na hlučnost.</p>'
          '<h2>Skládání a přenášení</h2>'
          '<p>Chodicí pásy jsou lehčí než běžecké, ale pořád váží kolem dvaceti kilogramů a víc. Většina má vpředu kolečka, takže se dají postavit na hranu a odvézt. Skládací modely se přeloží napůl a vejdou se do skříně. Výhodou je méně místa, slabinou kloub uprostřed, který při chůzi nesmí cvakat.</p>'
          '<h2>Údržba</h2>'
          '<p>Pás a deska potřebují mazání silikonem podle návodu výrobce. Bez něj se zvyšuje tření a motor se víc namáhá. Občas je třeba pás vystředit a dopnout šroubky na konci rámu, když se posouvá do strany. Pod pásem a kolem motoru vysávejte prach, zvlášť pokud máte domácí zvířata. Po delším používání zkontrolujte, jestli pás při došlapu neprokluzuje.</p>'
          '<h2>Kolik a jak chodit</h2>'
          '<p>Běžná chůze venku má tempo kolem čtyř až pěti kilometrů za hodinu. Na pásu se většině lidí zdá stejná rychlost náročnější, protože se nemění terén a krok je pořád stejný. Začněte pomaleji a rychlost přidávejte, až když jdete jistě a nemusíte se dívat pod nohy. Při chůzi pod stolem stačí klidné tempo, u kterého se dá mluvit i psát. Kdo chce na pásu trénovat svižnou chůzi, ať si nechá na konec pár minut zpomalení.</p>'
          '<p>Krokoměr v pásu nebo v aplikaci počítá kroky podle otáček pásu a délky kroku, kterou si zadáte. Výsledek proto nemusí přesně odpovídat hodinkám. Pro srovnání dní je důležitější, abyste měřili pořád stejným způsobem. Některé aplikace ukládají historii a dají se propojit s dalšími sportovními službami, ale bez telefonu by měl pás jít ovládat i tak.</p>'
          '<p>Pás nezvládne všechno. Chůze po rovině bez sklonu zatěžuje svaly jinak než chůze do kopce nebo po lesní cestě. Pokud máte bolesti kloubů nebo zad, nechte si chůzi na pásu odsouhlasit lékařem nebo fyzioterapeutem.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte rozsah rychlosti, trvalý výkon motoru, nosnost, rozměr chodicí plochy, výšku desky a hmotnost. Ověřte, jestli je v balení ovladač, zda pás funguje i bez aplikace a jak se zastavuje. Pod podobnými názvy se prodávají i bezmotorové pásy, které se pohánějí jen krokem. Ty fungují úplně jinak a pod stůl se nehodí.</p>'
          '<p>Před nákupem si ujasněte, kde bude pás stát a kdo na něm bude chodit. Pro jednoho člověka pod stolem stačí kompaktní model. Když ho bude používat víc lidí v domácnosti s různou hmotností a délkou kroku, vyplatí se delší plocha, vyšší nosnost a silnější trvalý výkon motoru. Zjistěte také, jak dlouhá je záruka na motor a desku a jestli obchod zajišťuje servis v Česku. Náhradní díly jako ovladač nebo pás se u neznámých značek shánějí obtížně.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nákup chodicího pásu na běhání.</li>'
          '<li>Nosnost na hraně hmotnosti uživatele.</li>'
          '<li>Pás pod stolem bez změřeného prostoru pro kolena.</li>'
          '<li>Chůze v ponožkách nebo naboso.</li>'
          '<li>Pás ponechaný v zásuvce, když jsou doma malé děti.</li></ul>'
          '<p>Na jinou formu pohybu doma se hodí <a href="/steppery/">steppery</a>, <a href="/rotopedy/">rotopedy</a> nebo <a href="/elipticke-trenazery/">eliptické trenažéry</a>. Počet kroků vám spočítají <a href="/chytre-hodinky/">chytré hodinky</a>, k chůzi se hodí pohodlná <a href="/treninkova-obuv/">tréninková obuv</a>. Celou nabídku strojů najdete v sekci <a href="/fitness/">fitness</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi chodicím a běžeckým pásem?', 'Chodicí pás je nízký, bez pevných madel a jezdí obvykle do šesti až osmi kilometrů za hodinu. Běžecký pás má delší plochu, silnější motor, madla a vyšší rychlosti.'),
        ('Dá se na walking padu běhat?', 'Na většině modelů ne, plocha je krátká a rychlost nízká. Kombinované pásy 2 v 1 po vyklopení madla zvládnou pomalý běh, na pravidelné běhání je lepší běžecký pás.'),
        ('Hodí se chodicí pás pod pracovní stůl?', 'Ano, k tomu se kupuje nejčastěji. Potřebujete výškově nastavitelný stůl a dost místa pro kolena a krok za sebou.'),
        ('Jakou nosnost by měl chodicí pás mít?', 'S rezervou nad vaší hmotností. U menších modelů bývá kolem 100 kg, odolnější pásy unesou víc.'),
        ('Jsou chodicí pásy hlučné?', 'Ozývá se hlavně motor a kroky, které se přenášejí do podlahy. Pryžová podložka pod trenažér hluk a vibrace utlumí.'),
        ('Jak chodicí pás zastavit v nouzi?', 'Ovladačem nebo bezpečnostním klíčkem, pokud ho model má. Před první chůzí si vyzkoušejte, jak rychle se pás zastaví.'),
        ('Je chodicí pás bezpečný, když jsou doma děti?', 'Jen pod dohledem. Po použití ho vypojte ze zásuvky a ovladač schovejte, mezera u konce pásu může skřípnout prsty.'),
        ('Jak se chodicí pás udržuje?', 'Podle návodu se maže silikonem, občas vystředí a dopne. Pod pásem pravidelně vysávejte prach.'),
        ('Dá se chodicí pás uložit pod postel?', 'Většinou ano, deska je nízká. Změřte výšku pod postelí a počítejte s hmotností kolem dvaceti kilogramů a víc.'),
        ('Kde koupit chodicí pás?', 'Na Sportece porovnáte nabídky českých obchodů u každého modelu. Nákup proběhne v e-shopu, který si vyberete.'),
    ])

# ------------------------------------------------------------------ airtracky-a-zinenky
NEW['airtracky-a-zinenky'] = dict(long=True,
    title='Airtracky a žíněnky: nafukovací i skládací',
    desc='Nafukovací airtracky a skládací gymnastické žíněnky pro domácí gymnastiku, parkour i školní cvičení. Rozměry, tloušťka, tlak, materiály a bezpečnost.',
    intro='<p><strong>Airtrack</strong> je nafukovací gymnastická dráha z pevné PVC tkaniny. Uvnitř drží tvar tisíce vláken, takže po nafouknutí je deska rovná, pružná a odpouští dopady. Hodí se na kotouly, přemety, salta i parkourové prvky. <strong>Žíněnka</strong> je pěnová podložka v omyvatelném potahu, skládací na dva až čtyři díly nebo vcelku. Obojí slouží jako bezpečnější povrch pro cvičení na zemi a dopady.</p>'
          '<p>Na Sportece jsou u každé dráhy a žíněnky vidět nabídky českých e-shopů, nákup pak proběhne v obchodě, který si vyberete. Najdete tu airtracky Airtrack Master a '
          + B(('insportline', 'Insportline')) +
          ' Airstunt v délkách od dvou do šesti metrů, příslušenství jako odrazové válce a spojky i klasické školní a skládací žíněnky. Kategorie patří pod <a href="/funkcni-trenink/">funkční trénink</a>, další vybavení pro cvičení najdete v sekci <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>',
    guide='<h2>Airtrack: jak funguje</h2>'
          '<p>Většina airtracků je postavená technologií drop-stitch. Horní a spodní vrstvu tkaniny spojují tisíce tenkých vláken, která po nafouknutí drží obě plochy rovnoběžně. Díky nim deska nemá tvar polštáře, ale zůstává plochá jako žíněnka. Stejnou technologii používají nafukovací paddleboardy. Povrch bývá protiskluzový a odolný proti oděru.</p>'
          '<p>Tvrdost airtracku nastavíte tlakem. Víc vzduchu znamená tvrdší a rychlejší dráhu, méně vzduchu měkčí dopad a víc pružení. Insportline u svého modelu Airstunt 500 × 100 × 10 cm uvádí doporučený tlak 1,5 až 2 PSI, tedy zhruba 0,1 až 0,14 baru. Jiné modely a tloušťky mohou mít jinou hodnotu, vždy se řiďte návodem. Tenká dráha nesmí být podhuštěná, jinak se při dopadu prorazí až na podlahu.</p>'
          + T(['Typ', 'Rozměry a stavba', 'Kam se hodí'], [
              ['Airtrack 10 cm', 'délka 2–6 m, šířka kolem 1 m', 'domácí gymnastika, akrobacie, parkour'],
              ['Airtrack 15–20 cm', 'silnější a často širší deska', 'vyšší skoky, dopady, oddíly'],
              ['Airfloor', 'tenká nafukovací plocha', 'podlaha na cvičení, rozcvičení'],
              ['Skládací žíněnka', 'pěna 4–5 cm, 2–4 díly', 'cvičení doma, kotouly, strečink'],
              ['Školní a dopadová žíněnka', 'silná pěna, až 20 cm i víc', 'dopady z nářadí, tělocvična']]) +
          '<h2>Rozměry: délka, šířka a tloušťka</h2>'
          '<p>Rozměry se u airtracků i žíněnek uvádějí v pořadí délka × šířka × tloušťka. Pro děti, které doma dělají kotouly a stoj na rukou, stačí dráha dlouhá dva až tři metry. Na přemety a sestavy s rozběhem je lepší čtyři až šest metrů, pokud se to vejde do místnosti nebo na zahradu. Šířka kolem jednoho metru stačí na většinu prvků, širší plochy jsou bezpečnější na salta a dopady do strany.</p>'
          '<p>Tloušťka 10 cm je nejrozšířenější. Na domácí cvičení a výuku základů je dostatečná. Silnější dráhy 15 až 20 cm lépe tlumí a víc pruží, jsou ale těžší a déle se nafukují. U žíněnek je běžná tloušťka 4 až 5 cm na cvičení na zemi. Dopadové žíněnky pod hrazdu nebo kruhy bývají mnohem silnější.</p>'
          '<h2>Pumpa a nafukování</h2>'
          '<p>Airtrack se nafukuje elektrickou pumpou, která bývá v balení nebo se kupuje zvlášť. Velkou dráhu nafoukne za pár minut i rychleji. Ruční nebo nožní pumpa funguje taky, ale u dlouhých drah to trvá. Pro přesné nastavení tlaku se hodí pumpa s manometrem. Pozor na adaptéry: ventil airtracku nemusí pasovat na každou pumpu, a proto výrobci přibalují sadu koncovek.</p>'
          '<p>Před cvičením zkontrolujte, že je dráha nafouknutá rovnoměrně a ventil je zavřený a zakrytý. Během delšího tréninku tlak mírně klesá, zvlášť když se dráha přesune ze studené místnosti do teplé nebo naopak. Doplňte vzduch, jakmile dopady začnou být cítit až na podlaze.</p>'
          '<h2>Žíněnky: pěna a potah</h2>'
          '<p>Skládací žíněnky mají pěnovou výplň a potah z omyvatelné koženky nebo PVC tkaniny. Díly jsou spojené pružnou částí potahu, takže se žíněnka složí do kvádru a dá se nosit za držadla. Některé mají na koncích suchý zip a dají se spojit do delší dráhy. Hustota pěny ovlivňuje, jak moc se žíněnka promáčkne. Měkká pěna je příjemná na strečink, na dopady je lepší tužší.</p>'
          '<p>Školní žíněnky vcelku jsou těžké a hodí se tam, kde zůstávají na místě. Doma jsou praktičtější skládací. Na jógu nebo pilates je žíněnka zbytečně silná, na to se lépe hodí tenké <a href="/joga-a-podlozky/">podložky na jógu</a>.</p>'
          '<h2>Gymnastika s dětmi doma</h2>'
          '<p>Airtrack a žíněnky jsou oblíbené u rodin, kde děti chodí do gymnastiky, akrobacie nebo parkouru a chtějí trénovat i doma. Povrch zmírní náraz, ale neochrání před špatně provedeným prvkem. Nové prvky, hlavně salta a přemety, se děti mají učit s trenérem. Doma je bezpečnější opakovat to, co už umějí.</p>'
          '<ul><li>Při cvičení dětí buďte u toho a hlídejte, aby se na dráze střídaly, ne skákaly naráz.</li>'
          '<li>Kolem dráhy nechte volný prostor bez nábytku, radiátorů a ostrých hran.</li>'
          '<li>Na airtrack se chodí bez bot a bez šperků, zipy a přezky mohou tkaninu poškodit.</li>'
          '<li>Pod dráhu nedávejte kameny ani štěrk, na trávě zkontrolujte, že tam nejsou větve.</li>'
          '<li>Airtrack není trampolína. Opakované skákání na místě vysoko do vzduchu na něj nepatří.</li></ul>'
          '<h2>Venku a na vodě</h2>'
          '<p>Na zahradě je airtrack v létě velká atrakce. Pod něj dejte celtu nebo podložku, aby se tkanina nedřela o trávu a hlínu. Na přímém slunci se povrch ohřívá a tlak uvnitř stoupá, proto po delším pobytu na slunci zkontrolujte tlak. Některé modely výrobce povoluje použít i na vodě, třeba v bazénu nebo na jezeře, s nižší nosností. Takové použití ověřte v návodu.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po cvičení otřete povrch vlhkým hadříkem a jemným čisticím prostředkem bez rozpouštědel. Před složením musí být dráha suchá, jinak začne plesnivět. Skladujte ji vyfouknutou, srolovanou volně a mimo mráz a přímé slunce. U balení bývá záplatovací sada, s níž se drobná díra opraví jako u nafukovacího člunu. Žíněnky stačí otírat a nechat vyschnout ve skládaném stavu na boku, aby se pěna neprohnula.</p>'
          '<h2>Příslušenství k airtracku</h2>'
          '<p>K dráhám se prodávají doplňky, které rozšiřují možnosti cvičení. Odrazové válce a kulaté nafukovací „spoty“ slouží jako odrazový můstek nebo jako pomůcka pro učení kotoulů a přemetů přes překážku. Spojovací díly s klínem umožní spojit dvě dráhy nebo udělat plynulý nájezd z podlahy na desku. Nafukovací klíny pomáhají dětem naučit se kotoul vzad, protože se po nich tělo převalí samo. Taška a náhradní ventil se hodí pro oddíly, které dráhu často převážejí.</p>'
          '<p>Před nákupem doplňků zkontrolujte, že pasují k vaší dráze. Spojovací díly a klíny bývají navržené pro konkrétní šířku a tloušťku. Doplňky od jiného výrobce nemusejí mít stejné rozměry ani typ ventilu.</p>'
          '<h2>Kolik místa potřebujete</h2>'
          '<p>K délce dráhy připočítejte volný prostor pro rozběh na jednom konci a pro dopad na druhém. Do stran nechte rezervu, protože děti často dopadnou mimo střed. V obývacím pokoji je proto dvoumetrová dráha často rozumnější než čtyřmetrová. Hlídejte také výšku stropu a lustr, zvlášť u sestav se skoky. Na hladké podlaze podložte dráhu protiskluzovou podložkou nebo kobercem, aby při rozběhu neujížděla.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U airtracků porovnávejte délku, šířku a tloušťku, materiál a údaj o drop-stitch konstrukci, typ pumpy v balení a hmotnost. U některých modelů výrobce uvádí shodu s normou EN 12503-1, která se týká gymnastických žíněnek. Nabídky s označením „2. jakost“ mívají kosmetické vady, které nemají vliv na funkci, popis ale vždy čtěte. U žíněnek srovnávejte rozměr po rozložení, počet dílů, tloušťku a materiál potahu.</p>'
          '<p>U oddílů a škol rozhoduje kromě rozměrů i hmotnost a doba, za kterou se dráha připraví. Pětimetrový airtrack v tašce unese jeden dospělý, silná dopadová žíněnka vyžaduje dva lidi. Doma zase ocení, že se dráha po vyfouknutí vejde do skříně nebo pod postel. Barva nemá vliv na funkci, na světlém povrchu je ale víc vidět špína.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Podhuštěná dráha, kde dopad dojde až na podlahu.</li>'
          '<li>Dráha delší, než kolik místa je v pokoji, a cvičení u zdi.</li>'
          '<li>Skládání mokrého airtracku po zahradním cvičení.</li>'
          '<li>Učení salt doma bez trenéra.</li>'
          '<li>Silná žíněnka koupená na jógu místo tenké podložky.</li></ul>'
          '<p>K domácímu cvičení se hodí <a href="/balancni-pomucky/">balanční pomůcky</a> a <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>. Kdo hledá skákání na zahradě, najde <a href="/trampoliny/">trampolíny</a>. Další vybavení pro dívky i kluky z oddílů je v sekci <a href="/tanec-a-gymnastika/">tanec a gymnastika</a>.</p>',
    faq=[
        ('Co je airtrack?', 'Nafukovací gymnastická dráha z PVC tkaniny s vnitřními vlákny, která drží rovný tvar. Používá se na akrobacii, gymnastiku a parkour.'),
        ('Jak dlouhý airtrack vybrat?', 'Na kotouly a stoj na rukou stačí dva až tři metry. Na přemety a sestavy s rozběhem je lepší čtyři až šest metrů, pokud na to máte místo.'),
        ('Jaká tloušťka airtracku je nejlepší?', 'Tloušťka 10 cm je nejběžnější a na domácí cvičení stačí. Silnější dráhy víc pruží a lépe tlumí dopady, ale víc váží.'),
        ('Jak moc airtrack nafouknout?', 'Podle návodu výrobce. Například Insportline u modelu Airstunt 10 cm uvádí 1,5 až 2 PSI. Dráha nesmí být podhuštěná, aby se dopad neprorazil na podlahu.'),
        ('Potřebuji k airtracku elektrickou pumpu?', 'Není nutná, ale u dlouhých drah ušetří hodně času. Často bývá v balení, jinak se kupuje zvlášť.'),
        ('Dá se airtrack použít venku?', 'Ano, na rovné ploše bez kamenů a větví a ideálně s podložkou. Na slunci kontrolujte tlak a před uložením dráhu vysušte.'),
        ('Jaký je rozdíl mezi airtrackem a žíněnkou?', 'Airtrack je nafukovací a pružný, dá se vyfouknout a srolovat. Žíněnka je pěnová, nepruží a je připravená k použití hned po rozložení.'),
        ('Jak opravit propíchnutý airtrack?', 'Záplatovací sadou podle návodu, podobně jako nafukovací člun. Větší poškození nebo trhlinu u švu řešte s prodejcem.'),
        ('Je airtrack bezpečný pro děti?', 'Zmírní pády, ale nenahradí dohled a trenéra. Nové prvky se děti mají učit v oddíle, doma je lepší opakovat zvládnuté cviky.'),
        ('Kde koupit airtrack nebo žíněnku?', 'Sporteka u každé dráhy a žíněnky ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě podle svého výběru.'),
    ])

# ------------------------------------------------------------------ otuzovaci-kade
NEW['otuzovaci-kade'] = dict(long=True,
    title='Otužovací kádě a vany na ledovou koupel',
    desc='Otužovací kádě, skládací vany, sudy i kádě s chladicí jednotkou. Typy, objem, izolace, víko, hygiena vody a bezpečná pravidla ledové koupele.',
    intro='<p><strong>Otužovací káď</strong> je nádoba na studenou koupel, do které se sedá až po ramena. Existují nafukovací a skládací vany z vícevrstvé tkaniny, pevné kádě tvaru sudu nebo oválu i vany s chladicí jednotkou, která drží teplotu vody bez ledu. Kupují je otužilci, kteří nemají po ruce řeku nebo rybník, a sportovci, kteří se chtějí po tréninku ponořit do studené vody. Káď není zdravotnický prostředek a o vhodnosti studené koupele se poraďte s lékařem.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých obchodů, takže u každé kádě uvidíte, kde ji prodávají. Nákup proběhne v obchodě, jehož nabídku si zvolíte. V nabídce jsou kádě a vany '
          + B(('insportline', 'Insportline'), ('gymbeam', 'GymBeam')) +
          ', Lifefit, Virtufit, Sharp Shape Lumi nebo Tunturi a také samostatné termoregulační jednotky. Kategorie patří pod <a href="/outdoor-doplnky/">outdoor doplňky</a>.</p>',
    guide='<h2>Typy otužovacích kádí</h2>'
          '<p>Nejlevnější a nejsnáze uložitelné jsou nafukovací a skládací vany. Stěny tvoří několik vrstev tkaniny s pěnou nebo nafukovací komory z PVC, někdy s konstrukcí drop-stitch. Po sezóně se vypustí, složí a uloží do tašky. Pevnost jim dává napuštěná voda, prázdné se snadno přenášejí.</p>'
          '<p>Pevné kádě mají tvar sudu, oválu nebo hranaté vany. Bývají z plastu, akrylátu nebo kompozitu, někdy s povrchem imitujícím dřevo. Lépe drží teplotu, mají pevný okraj a déle vydrží venku. Nejvyšší třídu tvoří kádě s chladicí jednotkou, které vodu samy ochladí na nastavenou teplotu a často ji i filtrují.</p>'
          + T(['Typ', 'Výhody', 'Na co myslet'], [
              ['Skládací vana', 'malá hmotnost, rychlá instalace, snadné uložení', 'méně izolace, voda se ohřívá rychleji'],
              ['Nafukovací káď', 'tuhé stěny, lepší izolace vzduchem', 'kontrola tlaku, ochrana proti propíchnutí'],
              ['Pevný sud nebo ovál', 'stálý tvar, delší životnost venku', 'větší hmotnost, místo na celý rok'],
              ['Káď s chladicí jednotkou', 'stálá teplota bez ledu, filtrace', 'elektřina, hluk, umístění jednotky'],
              ['Samostatná termoregulace', 'dá se připojit k vhodné kádi', 'kompatibilita přípojek a výkon']]) +
          '<h2>Objem a rozměry</h2>'
          '<p>Kádě se prodávají v objemech od zhruba dvou set do několika set litrů. Insportline například uvádí u modelu FrostZen Pro II objem 375 litrů. Větší objem znamená víc místa a stabilnější teplotu, ale také víc vody k napuštění a víc ledu nebo energie na chlazení. Pro jednoho dospělého sedícího s pokrčenýma nohama stačí menší káď. Vysokým lidem a těm, kdo si chtějí natáhnout nohy, se hodí oválná nebo podlouhlá vana.</p>'
          '<p>Rozhoduje hlavně výška a průměr. Při sezení byste měli mít ramena pod hladinou, přitom voda nesmí přetékat. Rozměr porovnejte se svou výškou a změřte i místo, kam káď postavíte.</p>'
          '<h2>Izolace a víko</h2>'
          '<p>Studená voda se v teplém prostředí rychle ohřívá. Silné izolované stěny a dobře těsnicí víko prodlužují dobu, po kterou voda vydrží studená, a omezují množství ledu. Víko navíc chrání vodu před listím, hmyzem a prachem, brání nehodám dětí a zvířat a v zimě omezuje zamrzání hladiny. U skládacích van bývá víko izolované a zapíná se na zip, u pevných kádí je někdy pevné nebo z izolační fólie.</p>'
          '<h2>Led, nebo chladicí jednotka</h2>'
          '<p>Bez jednotky se voda chladí ledem. V zimě stačí venkovní teplota a studená voda z kohoutku, v létě je potřeba led ve velkém množství. Některé kádě mají přihrádku na led nebo sáčky s chladicí náplní. Je to levné řešení na začátek, ale náročné na plánování.</p>'
          '<p>Chladicí jednotka funguje podobně jako malá lednice s čerpadlem. Vodu nasává, ochladí a vrací zpět. Některé jednotky umějí vodu i ohřát, Insportline například uvádí u své termoregulace rozsah od 0 do 55 °C. Jednotka potřebuje místo s přívodem vzduchu, pravidelné čištění filtru a zásuvku. Venku ji zapojte do zásuvky chráněné proudovým chráničem a kabel veďte mimo vodu. Při výběru porovnávejte příkon, chladicí výkon a to, zda jednotka pasuje ke konkrétní kádi.</p>'
          '<h2>Hygiena vody</h2>'
          '<p>Stojatá voda s teplotou kolem deseti stupňů není sterilní. Po každém ponoru do ní přejde pot, kožní maz a nečistoty z nohou. Bez péče se voda kalí, začne zapáchat a na stěnách se tvoří povlak.</p>'
          '<ul><li>Před koupelí se osprchujte a nevstupujte do vody s krémem nebo make-upem.</li>'
          '<li>Káď zakrývejte víkem, aby do vody nepadalo listí a nečistoty.</li>'
          '<li>U kádí bez filtrace vodu měňte často a stěny při výměně umyjte.</li>'
          '<li>Pokud používáte přípravky na úpravu vody, vybírejte ty, které výrobce kádě nebo jednotky povoluje.</li>'
          '<li>Filtr chladicí jednotky čistěte a měňte podle návodu.</li></ul>'
          '<h2>Kam káď postavit</h2>'
          '<p>Napuštěná káď je těžká. Litr vody váží zhruba kilogram, takže káď s 375 litry vody a člověkem uvnitř může vážit kolem půl tuny. Na balkón nebo terasu nad místností ji dávejte jen tehdy, když víte, kolik konstrukce unese. Podklad má být rovný a pevný, nejlépe dlažba nebo betonová plocha. Na trávě se káď časem nakloní.</p>'
          '<p>Myslete i na vypouštění. Voda by měla odtékat tam, kde nic nezaplaví, a pokud v ní byly chemické přípravky, nepatří na záhon. V zimě hrozí, že voda zamrzne v hadicích a v jednotce. Pokud výrobce nepovoluje provoz v mrazu, káď vypusťte a jednotku uložte do suchého prostoru.</p>'
          '<h2>Bezpečnost ledové koupele</h2>'
          '<p>Ponoření do studené vody vyvolá chladový šok. Dech se zrychlí a je těžké ho ovládat, stoupne tep i krevní tlak. U lidí s neodhaleným onemocněním srdce, cév nebo mozku může takový šok vést k vážným komplikacím. Otužování proto začíná postupně a s rozumem.</p>'
          '<ul><li><strong>Nikdy sami.</strong> U kádě má být další člověk, zvlášť když s ledovou koupelí začínáte.</li>'
          '<li><strong>Krátce.</strong> Začněte velmi krátkými ponory v ne úplně ledové vodě a dobu prodlužujte jen pozvolna. Při třesu, brnění nebo necitlivosti prstů vylezte.</li>'
          '<li><strong>Lékař napřed.</strong> Při onemocnění srdce, vysokém krevním tlaku, poruchách rytmu, sklonu k mdlobám, v těhotenství nebo při jiných zdravotních potížích se poraďte s lékařem.</li>'
          '<li><strong>Bez alkoholu.</strong> Alkohol do otužování nepatří, zhoršuje úsudek a reakci těla na chlad.</li>'
          '<li><strong>Hlava nad vodou.</strong> Neponořujte se pod hladinu a do vody vstupujte pomalu.</li></ul>'
          '<p>Po výstupu tělo ještě nějakou dobu chladne, i když už jste z vody venku. Rychle se osušte, oblékněte do suchých a teplých vrstev a zahřejte se pohybem a teplým nápojem. Za volant nebo k práci s nářadím si sedněte, až když jste úplně zahřátí. Horká sprcha hned po ledové koupeli může u citlivých lidí vyvolat závrať.</p>'
          '<h2>Kdy otužovací káď dává smysl</h2>'
          '<p>Otužilci se v Česku tradičně koupou v řekách, rybnících a lomech. Káď je pohodlnější tam, kde přírodní voda není blízko, nebo pro lidi, kteří se chtějí ponořit každý den doma. V zimě je venku voda studená sama a káď slouží hlavně jako soukromé místo. V létě je bez chladicí jednotky potřeba hodně ledu. Sezóna kádí proto začíná na podzim, kdy noci ochladí vodu samy.</p>'
          '<p>Pokud chcete studenou koupel spojit se saunou, počítejte s tím, že rozpálené tělo reaguje na studenou vodu prudčeji. Mezi saunou a kádí si dopřejte chvíli na vychladnutí na vzduchu a do vody vstupujte pomalu. Po skončení se zahřejte v klidu, ne další rychlou změnou teploty.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte typ kádě, objem, vnitřní rozměry, tloušťku stěn, víko, výpustný ventil a hmotnost prázdné kádě. U kádí s chlazením sledujte nejnižší dosažitelnou teplotu, filtraci, hlučnost a nároky na umístění jednotky. Termoregulační jednotky se prodávají i samostatně, ověřte proto, co přesně je v balení.</p>'
          '<p>Při výběru zvažte také, kolik lidí bude káď používat a jak často. Pro jednoho člověka, který se ponoří párkrát týdně, stačí skládací vana s víkem. Pro rodinu nebo každodenní používání je praktičtější pevná káď s filtrací, ve které voda vydrží čistá déle. Ověřte také, jak se káď vypouští a jestli má výpustný ventil s přípojkou na hadici.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Ledová koupel bez dozoru a bez zkušeností.</li>'
          '<li>Káď na balkoně bez ověření nosnosti.</li>'
          '<li>Voda měněná jednou za sezónu.</li>'
          '<li>Jednotka v mrazu, když to výrobce nepovoluje.</li>'
          '<li>Prodlužování času ve vodě ze soutěživosti.</li></ul>'
          '<p>Po koupeli se hodí velký <a href="/rucniky/">ručník</a>, <a href="/neoprenove-boty-a-ponozky/">neoprenové boty a ponožky</a> na cestu ke kádi a <a href="/termohrnky/">termohrnek</a> s teplým čajem. Kdo se chce otužovat i v přírodě, najde <a href="/neopreny/">neopreny</a> a <a href="/plavky/">plavky</a>. Na letní koupání je určená kategorie <a href="/bazeny/">bazény</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi skládací a pevnou otužovací kádí?', 'Skládací je lehká a po sezóně se uloží do tašky, ale hůř drží teplotu. Pevná káď má lepší izolaci a pevný okraj, potřebuje ale stálé místo.'),
        ('Jak velkou otužovací káď vybrat?', 'Takovou, abyste vsedě měli ramena pod hladinou. Porovnejte výšku a průměr kádě se svou postavou a změřte místo, kam ji postavíte.'),
        ('Potřebuji ke kádi chladicí jednotku?', 'Není nutná. V zimě stačí studená voda a venkovní teplota, v létě led. Jednotka udrží stálou teplotu bez ledu, ale potřebuje elektřinu a údržbu.'),
        ('Jak dlouho zůstat v ledové vodě?', 'Na začátku jen krátce a v ne úplně ledové vodě. Dobu prodlužujte pozvolna a vylezte hned, když se objeví třes nebo necitlivost prstů.'),
        ('Kdo by se neměl otužovat v kádi?', 'Lidé s onemocněním srdce, vysokým tlakem, poruchami rytmu, sklonem k mdlobám nebo v těhotenství by se měli nejdřív poradit s lékařem.'),
        ('Jak často měnit vodu v otužovací kádi?', 'Záleží na počtu lidí a filtraci. Bez filtru vodu měňte často, káď zakrývejte víkem a před koupelí se osprchujte.'),
        ('Může káď stát na balkoně?', 'Jen pokud víte, že balkon unese její váhu. Napuštěná káď s člověkem může vážit kolem půl tuny.'),
        ('Co dělat po ledové koupeli?', 'Rychle se osušit, obléknout do teplého a zahřát pohybem a teplým nápojem. Řídit až po úplném zahřátí.'),
        ('Je otužovací káď zdravotnický prostředek?', 'Ne. Slouží ke studené koupeli a výrobci ani prodejci nemohou slibovat léčebné účinky.'),
        ('Kde koupit otužovací káď?', 'Sporteka u každé kádě a vany ukáže nabídky českých e-shopů. Objednávku dokončíte v obchodě, který si zvolíte.'),
    ])
