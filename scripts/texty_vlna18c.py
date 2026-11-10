"""sporteka.cz — wave 18c (4. 11. 2026): long texts (>= 1650 words) for posilovaci-gumy, sjezdove-lyze, detske-cyklohelmy, damske-plavky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ posilovaci-gumy
NEW['posilovaci-gumy'] = dict(long=True,
    title='Posilovací gumy a expandery: smyčky, pásy, trubice',
    desc='Posilovací gumy, odporové smyčky, pásy a expandery s madly. Jak zvolit odpor, délku a materiál pro cvičení doma, na cestách i v posilovně.',
    intro='<p>Odporová guma váží pár desítek gramů a vejde se do kapsy, přesto s ní protáhnete celé tělo. V kategorii <strong>posilovací gumy a expandery</strong> '
          'najdete uzavřené smyčky, dlouhé pásy bez konce, trubice s madly, tkané textilní gumy na zadek i dveřní kotvy a úchyty. Liší se šířkou, délkou, '
          'materiálem a hlavně odporem, který kladou při natažení, a právě podle toho se rozhoduje, jestli vám bude sloužit při rozcvičce, nebo při náročném silovém tréninku.</p>'
          '<p>Sporteka srovnává nabídku českých obchodů u stejného zboží vedle sebe, takže snadno uvidíte, kdo má skladem celou sadu odporů. Další vybavení na cvičení doma '
          'je v nadřazené kategorii <a href="/fitness-pomucky/">fitness pomůcky</a> a v celém oboru <a href="/fitness/">fitness a posilování</a>. '
          'Níže vysvětlíme, jak se jednotlivé typy liší, jak volit odpor a jak gumy chránit před předčasným prasknutím.</p>',
    guide='<h2>Typy odporových gum</h2>'
          '<p>Slovem guma se označuje několik odlišných výrobků a každý se hodí na trochu jinou práci. Než začnete porovnávat jednotlivé kusy, ujasněte si, kterou skupinu vlastně potřebujete.</p>'
          + T(['Typ', 'Jak vypadá', 'K čemu se hodí nejvíc'], [
              ['Minismyčka (mini band)', 'krátký uzavřený kruh, obvykle okolo třiceti centimetrů', 'aktivace hýždí, cviky kolem kolen a kotníků, rozcvičení před během'],
              ['Dlouhá smyčka (power band)', 'velký uzavřený pás, často přes metr', 'přítahy, asistované shyby, dřepy s odporem, protahování'],
              ['Textilní guma', 'tkaný potah s latexovým jádrem, neroluje se', 'cviky pro zadek a stehna, kde guma sedí na kůži nebo legínách'],
              ['Pásy s různou šířkou', 'plochý otevřený pás bez uzavřených konců', 'rehabilitační cvičení, jóga, pilates, jemné posilování ramen'],
              ['Trubice s madly', 'duté trubkové lano s úchyty na koncích', 'imitace kladkových cviků, bicepsy, tricepsy, tlaky a přítahy'],
              ['Sada s dveřní kotvou', 'trubice nebo pásy, madla, popruh na kotníky', 'kompletní trénink horních i dolních partií v malé místnosti']]) +
          '<p>Nejuniverzálnější volbou pro začátek bývá sada několika smyček různé tuhosti. Trubice s madly zase nejvíc připomínají cvičení s kabely v posilovně, protože úchop je pohodlný a lano se dá upevnit ve dveřích.</p>'
          '<h2>Odpor: jak ho poznáte a zvolíte</h2>'
          '<p>Většina výrobců označuje odpor barvou nebo slovy jako lehká, střední, silná. Barevné kódy se ale nesjednotily. Žlutá guma jedné značky může být jemnější než žlutá guma jiné, proto se spoléhejte na text v popisu a na údaje o šířce a tloušťce. '
          'Čím je pás širší a silnější, tím víc práce při natažení vyžaduje. Odpor se také mění podle toho, jak daleko guma natáhnete, takže stejný kus je u kolen lehčí než nad hlavou.</p>'
          '<p>Praktické pravidlo zní, že správná guma dovolí odcvičit zvolený počet opakování s kontrolovaným pohybem a poslední dvě až tři opakování jsou znatelně náročná. '
          'Pokud se tělo při cvičení kroutí, zadržujete dech nebo zkracujete rozsah, je odpor příliš velký. Když naopak zvládnete dvacet opakování bez zaváhání, přejděte na silnější kus. '
          'Proto se vyplatí kupovat sady, kde jsou alespoň tři stupně, nebo kombinovat jednu lehčí a jednu tužší gumu, protože malé svaly ramen potřebují jiný odpor než velké svaly nohou.</p>'
          '<h3>Orientační volba podle partie</h3>'
          + T(['Partie', 'Doporučený směr odporu', 'Poznámka'], [
              ['Ramena a rotátory', 'lehký', 'malé svaly se unaví dřív, pomalý pohyb je důležitější než síla'],
              ['Záda a přítahy', 'střední až silný', 'trubice s madly nebo dlouhá smyčka okolo pevného bodu'],
              ['Hýždě a boky', 'střední až silný', 'minismyčka nad kolena nebo kolem kotníků, textilní provedení neujíždí'],
              ['Předloktí a paže', 'lehký až střední', 'madla s vyšším tahem, aby se nezkracoval rozsah'],
              ['Celé tělo, rozcvička', 'lehký', 'cílem je zahřátí a probuzení pohybu, ne únava']]) +
          '<h2>Materiál: latex, textil a latexová alternativa</h2>'
          '<p>Klasická guma je z přírodního latexu, který se dobře natahuje a vrací do původního tvaru. Latex ale některým lidem vadí a při alergii na něj se hledají bezlatexové varianty z termoplastických materiálů, které bývají o něco méně pružné. '
          'Textilní potah zase řeší dva typické problémy tenké gumy, totiž že se ve cviku svinuje a že se lepí k pokožce. Za příplatek ve váze a tuhosti dostanete příjemnější použití pod koleny a na stehnech. '
          'Latex trpí slunečním zářením, teplem i potem, takže po použití je dobré gumu otřít a uložit stranou od topení.</p>'
          '<h2>Délka a šířka</h2>'
          '<p>Dlouhé smyčky jsou praktické pro vysokého člověka i pro cviky, kde se guma vede kolem sloupku nebo hrazdy. Krátké minismyčky se obvykle používají přímo na těle, a proto stačí menší rozměr. '
          'Šířka ovlivňuje pohodlí. Široká guma se méně zařezává, tenká pásová se lépe zasouvá pod chodidlo či kolem dlaně. Pokud chcete cvičit s koleny pod gumou, vezměte širší pás z textilu.</p>'
          '<h2>Kdy gumy nahradí činky a kdy je doplní</h2>'
          '<p>Gumy zaberou málo místa a nemají omezený rozsah nastavitelný po kilogramech. Hodí se pro cestování, rehabilitaci pod dohledem odborníka, dlouhou zimu bez posilovny a jako doplněk, který zpestří trénink s <a href="/cinky-a-kotouce/">činkami a kotouči</a>. '
          'Mají specifický průběh odporu, který u klasické váhy chybí, protože nejtěžší je v koncové poloze pohybu. Pro velká základní cvičení se stejně vyplatí kombinace s <a href="/kettlebelly/">kettlebelly</a>. '
          'Kdo chce stavět na ještě větším zatížení, najde v kategorii <a href="/posilovaci-stroje/">posilovací stroje a lavice</a> zařízení, která zatížení řídí přesněji.</p>'
          '<h2>Jak s gumou cvičit bezpečně</h2>'
          '<ul><li>Před každým tréninkem gumu prohlédněte. Drobné trhlinky, ztenčená místa nebo lepkavý povrch jsou důvodem k výměně, protože natažená guma se může přetrhnout a zasáhnout vás.</li>'
          '<li>Pevně ji ukotvěte. Dveřní kotva patří do dveří, které se zavírají směrem od vás, a pásy se nesmějí protahovat přes ostré hrany.</li>'
          '<li>Natahujte do rozumné délky. Podle návodu výrobce guma snese pouze určité natažení násobkem původní délky, překročení výrazně zkracuje životnost.</li>'
          '<li>Držte kontrolu při návratu. Pomalé vracení do výchozí polohy je stejně důležité jako samotný tah, protože guma nepovolí sama jako činka.</li>'
          '<li>Při cvičení v brýlích nebo s ozdobami na prstech dbejte opatrnosti, ostré předměty mohou materiál naříznout.</li></ul>'
          '<h2>Co cvičit: rozvržení tréninku</h2>'
          '<p>Základní týdenní plán může mít dvě až tři jednotky po čtyřiceti minutách. V první dominují nohy a hýždě, například dřepy s minismyčkou nad koleny, mosty, boční kroky a odvody v lehu. Druhá se věnuje zádům a ramenům, třeba přítahy k pasu, '
          'rozpažování, face pulls s lanem upevněným ve výšce hlavy. Třetí spojí celé tělo v kruhu cviků po třiceti až čtyřiceti vteřinách. Cvik stačí vybrat jeden na partii, ale pečlivě. '
          'Při pokroku nehledejte hned silnější gumu. Můžete zpomalit pohyb, přidat pauzu v koncové poloze, zvýšit počet sérií nebo zkrátit odpočinek.</p>'
          '<h2>Rozcvička a protažení</h2>'
          '<p>Dlouhý pás bez uzavřených konců se hodí k pasivnímu i aktivnímu protahování. Přehozený přes chodidlo pomáhá při předklonech a dosažení zadní strany stehen, ve dvojici s <a href="/joga-a-podlozky/">jógovou podložkou</a> '
          'ho ocení lidé, kteří cvičí jógu nebo <a href="/pilates-pomucky/">pilates</a>. Pro cvičení rovnováhy lze gumu zkombinovat s <a href="/balancni-pomucky/">balančními pomůckami</a>. '
          'Kdo se po tréninku chce uvolnit, prozkoumá <a href="/masazni-pomucky/">masážní pomůcky</a>, u nichž je vždy potřeba držet se návodu výrobce.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší výběr pod jednou střechou nabízí {B(("viking", "Viking"), ("hms", "HMS"), ("merco", "Merco"), ("sportago", "Sportago"), ("insportline", "Insportline"))}, '
          f'zdravotnickou a fyzioterapeutickou tradici mají pásy značky {B(("theraband", "Theraband"))}. Z dalších nabídek stojí za pohled {B(("sedco", "Sedco"), ("gymbeam", "GymBeam"), ("domyos", "Domyos"), ("lifefit", "Lifefit"), ("4fizjo", "4FIZJO"), ("spokey", "Spokey"))}. '
          'Rozdíly se týkají hlavně rozsahu sad, přibaleného návodu a kvality upevnění madel, a ne tolik samotného latexu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš silná guma hned na začátku. Technika se pak kazí a ramena či zápěstí přebírají práci svalů.</li>'
          '<li>Cvičení bez pevného bodu. Nestabilní úchyt způsobí, že guma vystřelí.</li>'
          '<li>Skladování na slunci nebo v autě. Latex křehne a po několika týdnech se začne drolit.</li>'
          '<li>Ignorování drobných trhlinek. Malé poškození se při natažení rychle rozšíří.</li>'
          '<li>Jen jeden stupeň odporu. Jedna guma nevystačí na malé i velké svaly a trénink se brzy zastaví.</li></ul>'
          '<h2>Pro koho jsou gumy vhodné</h2>'
          '<p>Začátečník ocení lehké pásy, protože učí správný pohyb bez velké zátěže. Běžec je používá na posílení boků a kolenních stabilizátorů, lezec na ramena a lopatky, cyklista na uvolnění těla po dlouhé jízdě. '
          'Kdo cvičí s dětmi, použije lehkou gumu pro zábavné cvičení, pod dohledem dospělého. Při rehabilitaci po zranění se vždy držte pokynů lékaře nebo fyzioterapeuta a gumu zvolte podle jeho doporučení. '
          'Pokud po tréninku potřebujete chránit klouby, podívejte se do kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, a na tělocvik si pořiďte vhodnou <a href="/treninkova-obuv/">tréninkovou obuv</a>. '
          'Ženy ocení pohodlnou <a href="/sportovni-podprsenky/">sportovní podprsenku</a> při dynamických sériích a společníky pro kondiční cvičení představují <a href="/svihadla/">švihadla</a> a <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Po tréninku gumu otřete vlhkým hadříkem a nechte oschnout. Neperte ji ve stroji, nedávejte do sušičky a nepoužívejte agresivní čisticí prostředky. Pokud guma lepí, lehce ji poprašte talkem a pokud lepí trvale nebo je povrch popraskaný, gumu vyměňte; tuky a oleje latex poškozují. '
          'Ukládejte ji volně nebo v látkovém pouzdře, aby se nepřekládala stále na stejném místě. Při pravidelném používání vyměňujte gumy zhruba po několika měsících a vždy, když se objeví povrchové poškození. '
          'Přenosné gumy se skvěle hodí i do tašky z kategorie <a href="/sportovni-tasky/">sportovní tašky a ledvinky</a>.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Při nákupu sledujte hlavně počet kusů v sadě, rozsah odporů, délku a šířku a hmotnost, kterou výrobce deklaruje jako maximální zátěž. U trubic zkontrolujte, zda je karabina a madlo kovové či plastové a zda je lano chráněno textilním pláštěm proti přetržení. '
          'Pokud nakupujete přes Sporteku, porovnejte, jestli obchod uvádí návod k použití a zda nabízí výměnu. U sady o třech stupních odporu se vyplatí využít všechny tři, u dvou používaných stupňů stačí menší balení. Naopak u dvojice s různým odporem se vyplatí mít zálohu.</p>',
    faq=[
        ('Jakou gumu zvolit na začátek?', 'Nejlépe sadu tří smyček s lehkým, středním a silným odporem. Na malé svaly ramen vezmete lehkou, na nohy střední až silnou.'),
        ('Čím se liší minismyčka od dlouhé smyčky?', 'Minismyčka je krátká a používá se na těle kolem kolen či kotníků. Dlouhá smyčka se vede kolem pevného bodu a hodí se na přítahy, dřepy i protahování.'),
        ('Dá se s gumou nahradit posilovna?', 'Pro udržení kondice a lehčí silový trénink ano. Chcete-li zvyšovat zatížení po malých krocích, přidejte k gumám činky nebo kettlebelly.'),
        ('Proč se mi guma při cviku svinuje?', 'Tenká latexová guma se na kůži nebo látce svinuje. Pomůže široká textilní guma, která drží na místě a nejde tolik do kůže.'),
        ('Jak poznám, že je guma opotřebovaná?', 'Sledujte drobné praskliny, ztenčená místa, lepkavý povrch nebo trvalé prodloužení. Při jakémkoli viditelném poškození ji raději vyměňte, hrozí přetržení.'),
        ('Mohu cvičit s gumou při alergii na latex?', 'Existují bezlatexové varianty z jiných pružných materiálů. Zkontrolujte v popisu produktu složení a v případě pochybností se poraďte s lékařem.'),
        ('Jak často s gumami cvičit?', 'Dvě až tři jednotky týdně s odstupem aspoň jednoho dne mezi stejnými partiemi stačí. Lehkou rozcvičku s gumou můžete zařadit i častěji.'),
        ('Jak gumu ukotvit ve dveřích?', 'Použijte kotvu určenou k tomuto účelu a zavřete dveře směrem od sebe tak, aby kotva zůstala na druhé straně. Před cvikem pevně zatáhněte, zda drží.'),
        ('Jak gumy čistit?', 'Otřete je vlhkým hadříkem, nechte oschnout a uložte mimo slunce a topení. Nepoužívejte pračku, sušičku ani rozpouštědla, latex by ztvrdl a popraskal.'),
        ('Hodí se gumy pro děti?', 'Lehkou gumu lze použít pro hravé cvičení pod dohledem dospělého. Dítě by nemělo cvičit s příliš silným odporem ani s upevněním, které by mohlo vystřelit.'),
        ('Co znamená, že guma je určena na rehabilitaci?', 'Obvykle jde o pásy s jemnějším odporem a delší nepřerušenou délkou. Postup cvičení ale má řídit odborník, ne popis v e-shopu.'),
    ])


# ------------------------------------------------------------------ sjezdove-lyze
NEW['sjezdove-lyze'] = dict(long=True,
    title='Sjezdové lyže: carvingové, freeride, dětské i komplety',
    desc='Sjezdové lyže pro začátečníky i pokročilé: carving, all-mountain, freeride, dětské lyže, komplety s vázáním. Jak zvolit délku, profil a tuhost.',
    intro='<p>Dobře zvolené <strong>sjezdové lyže</strong> rozhodují o tom, jestli vás bude lyžování bavit, nebo večer přijdete domů vyčerpaní z boje s technikou, která na vás nesedí. '
          'V nabídce jsou lyže carvingové na upravené sjezdovky, univerzální all-mountain, široké freeridové do neupraveného terénu i závodní modely, a také '
          '<a href="/lyze-komplety/">komplety lyží s vázáním</a> pro pohodlný nákup na jeden zátah. Děti hledají v samostatné kategorii <a href="/detske-lyze/">dětských lyží</a>.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného modelu, takže zjistíte, kde je skladem vámi hledaná délka. Samostatně lze dokoupit '
          '<a href="/lyzarske-vazani/">lyžařské vázání</a>, k lyžím patří také <a href="/lyzarske-boty/">lyžařské boty</a> a <a href="/lyzarske-hole/">hole</a>. '
          'V dalším textu vysvětlíme typy lyží, délku, rádius, tuhost, vázání i péči o skluznici.</p>',
    guide='<h2>Typy sjezdových lyží</h2>'
          '<p>Základní dělení vychází z toho, kde a jak chcete lyžovat. Než začnete porovnávat konkrétní modely, rozhodněte se, který styl ve skutečnosti dělá většinu vašich dnů na svahu.</p>'
          + T(['Typ lyže', 'Terén', 'Pro koho'], [
              ['Carvingové', 'upravená sjezdovka', 'rekreační lyžaři, začátečníci a středně pokročilí, kteří chtějí snadné zatáčení'],
              ['All-mountain', 'sjezdovka i sníh mimo ni', 'univerzální volba pro většinu dospělých lyžařů'],
              ['Freeride', 'prašan, neupravený terén', 'zkušení lyžaři, kteří jezdí mimo značené trasy'],
              ['Závodní (slalom, obří slalom)', 'tvrdá, upravená trať', 'závodníci a velmi dobří lyžaři s agresivním stylem'],
              ['Freestyle a twin-tip', 'snowpark, skoky', 'lyžaři, kteří jezdí i pozpátku a skáčou'],
              ['Dětské lyže', 'upravené svahy', 'děti podle hmotnosti a úrovně']]) +
          '<p>Skialpové lyže jsou lehčí a staví se na stoupání, takže na klasické sjezdovky se nehodí. Pro ně máme samostatnou kategorii <a href="/skialpove-lyze/">skialpové lyže</a>. '
          'Na běžecké trasy patří <a href="/bezecke-lyze/">běžecké lyže</a>, což je úplně jiný sport s úzkým profilem a upevněním jen v přední části boty.</p>'
          '<h2>Délka lyží</h2>'
          '<p>Správná délka závisí na výšce, hmotnosti, zkušenostech a typu lyže. Jako hrubý orientační vodítko se používá výška těla, přičemž začátečníkům se doporučují kratší lyže a pokročilým delší. '
          'Kratší lyže se snadněji zatáčejí a odpouštějí chyby, delší jsou stabilnější v rychlosti a lépe plují ve sněhu. U ženských a lehčích lyžařů má výrobce často měkčí konstrukci, takže stejná délka sedí jinak než u pánského modelu.</p>'
          + T(['Úroveň', 'Orientační délka vzhledem k tělu', 'Důvod'], [
              ['Začátečník', 'zhruba k bradě až k nosu', 'snadné otáčení, jistota při pomalé jízdě'],
              ['Středně pokročilý', 'zhruba k nosu až k čelu', 'kompromis mezi obratností a stabilitou'],
              ['Pokročilý a rychlejší jízda', 'zhruba k čelu až k výšce hlavy', 'klid při vyšší rychlosti'],
              ['Freeride', 'může být i delší než hlava', 'větší plocha pro nadnášení v prašanu']]) +
          '<p>Přesnou délku konkrétního modelu uvádí tabulka výrobce, která zohledňuje i hmotnost lyžaře. Pokud váháte mezi dvěma velikostmi, vyberte kratší, jste-li spíš opatrní, a delší, pokud jezdíte rychle.</p>'
          '<h2>Rádius, šířka a tuhost</h2>'
          '<p>Tři parametry rozhodují o chování lyže. Rádius udává oblouk, který lyže zatáčí při stranovém náklonu. Krátký rádius znamená ostrou a hravou zatáčku, dlouhý jistou a rychlou. '
          'Šířka pod nohou ovlivňuje chování na sněhu. Užší lyže jsou rychlé z hrany na hranu a na tvrdém podkladu přesné, širší nadnášejí v hlubokém sněhu, ale na ledovaté sjezdovce jsou těžkopádnější. '
          'Tuhost lyže stoupá s výkonností a váhou. Měkčí lyže jsou odpouštějící, tuhé držejí stabilitu při vyšších rychlostech, ale začátečníka unavují a nesedí mu.</p>'
          '<h3>Rocker a camber</h3>'
          '<p>Klasický prohnutý profil, nazývaný camber, dává lyži pružnost a přesný záběr na hranách. Rocker je opačný zdvih špičky a paty a zlepšuje plování a snadné zatáčení. Mnoho moderních lyží kombinuje oba prvky, '
          'takže se hodí do různého terénu. Freeridové modely mívají rockeru víc, carvingové camber převažuje. U začátečnických lyží proto často najdete mírný rocker na špičce, který usnadňuje zahájení oblouku.</p>'
          '<h2>Komplety a samostatné vázání</h2>'
          '<p>Komplet má vázání namontované a seřízené pro daný typ lyže, takže odpadá skládání dílů. Kompatibilitu s botou (normu podrážky) je ale třeba ověřit i tak. Je to výhodné hlavně pro začátečníky a pro děti, které rychle rostou. '
          'Samostatně prodávané lyže bez vázání si můžete osadit podle potřeby a zvolit vázání s vyšší nastavitelnou silou uvolnění. Vázání musí odpovídat typu a normě podrážky vašich bot a musí být seřízeno servisem. '
          'Hodnota uvolnění se nastavuje podle hmotnosti, výšky, věku a úrovně a nikdy ji neupravujte od oka. Přehled najdete v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>.</p>'
          '<h2>Pánské, dámské, dětské a juniorské</h2>'
          '<p>Dámské lyže mají často měkčí konstrukci, lehčí jádro a posunuté montážní místo, protože lyžařky mívají nižší hmotnost a jiné rozložení váhy. Pánské lyže bývají tužší a delší. Unisex modely se prodávají v širokém rozsahu délek. '
          'Dětské lyže se vyrábějí od velmi krátkých délek a růst dítěte vyžaduje kontrolu každou sezónu. Raději volte lyže, které sahají k bradě až k nosu, ne ty příliš dlouhé s předpokladem, že dítě doroste. '
          'Dobře seřízená menší lyže se ovládá snáz a dítě si udrží radost z lyžování.</p>'
          '<h2>Co ještě k lyžím patří</h2>'
          '<p>Lyže je jen část výbavy. Bezpečnost začíná u dobré <a href="/lyzarske-helmy/">lyžařské helmy</a> a lyžařských <a href="/lyzarske-bryle/">brýlí</a>. Pohodlí a teplo zajistí <a href="/lyzarske-obleceni/">lyžařské oblečení</a>, '
          'funkční <a href="/lyzarske-termopradlo/">termoprádlo</a>, teplé <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/lyzarske-rukavice/">rukavice</a>. '
          'Pro přepravu se hodí <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a>. Kdo lyžuje rychleji nebo v parku, může přidat <a href="/snowboardove-chranice/">chrániče páteře a boků</a>. '
          'Celý obor shrnuje rozcestník <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Velký výběr lyží mají značky {B(("rossignol", "Rossignol"), ("elan", "Elan"), ("fischer", "Fischer"), ("atomic", "Atomic"), ("head", "Head"), ("blizzard", "Blizzard"))}. '
          f'Doplňují je {B(("dynafit", "Dynafit"), ("stockli", "Stöckli"), ("salomon", "Salomon"), ("ride", "Ride"), ("wedze", "Wedze"), ("nordica", "Nordica"))}. '
          'Každý výrobce má vlastní označení řad, takže při porovnávání dívejte spíš na typ, rádius, šířku a deklarovaný styl jízdy než na marketingové jméno.</p>'
          '<h2>Sjezdovka, hloubka a park: jak se liší chování lyže</h2>'
          '<p>Na upravené sjezdovce záleží na hraně. Tam, kde je podklad tvrdý, lyže s užším středem a krátkým rádiusem přeskočí z jedné zatáčky do druhé s minimem snahy a držení hrany je spolehlivé. '
          'V hlubokém sněhu se naopak široká lyže nepropadá, protože plocha rozkládá váhu. Kdo jezdí převážně v zimních střediscích s upravenými svahy, nic na tom nezmění ani drahá freeridová lyže, spíš ho bude zdržovat. '
          'Naopak lyžař, který chce zkoušet zasněžené lesy nebo okraje tratí, brzy narazí na limit úzké carvingové lyže. Odpověď je často kompromis v podobě all-mountain modelu střední šířky. '
          'Parkové lyže mají symetrický tvar a zvednutou patu, aby se snadno jelo pozpátku a přistávalo po skoku. Na tvrdé sjezdovce jsou o něco méně přesné.</p>'
          '<h3>Zapůjčit, nebo koupit</h3>'
          '<p>Pokud lyžujete jeden týden v roce nebo se teprve učíte, má půjčovna smysl. Dostanete lyže s boty a seřízením a nemusíte řešit převoz a uskladnění. '
          'Jakmile jezdíte víc dní v sezóně, vlastní lyže se zpravidla vyplatí. Vlastní boty a vázání jsou seřízené na vaši nohu, takže ušetříte čas u půjčovny a zbavíte se náhodných rozdílů v kvalitě. '
          'Pro děti se osvědčují sezónní půjčovny, které lyže každý rok vymění za větší velikost.</p>'
          '<h3>Typ jízdy a váha lyžaře</h3>'
          '<p>Silný a těžký lyžař potřebuje tužší lyži, jinak se prohýbá a ztrácí stabilitu. Lehká osoba na tuhé závodní lyži ji nedokáže prohnout, zatáčky vázne a nohy se unaví. '
          'Výrobci to řeší různými řadami podle hmotnosti a úrovně, takže se při výběru nevyplatí jen přemýšlet o značce, ale i o tom, jak je lyže skutečně konstruovaná. Nejlepší je přiznat si, jakou rychlost opravdu jezdíte, a ne tu, kterou byste chtěli.</p>'
          '<h2>Jak vybírat krok za krokem</h2>'
          '<ol><li>Určete, kde jezdíte nejčastěji: sjezdovka, mimo ni, nebo od všeho trochu.</li>'
          '<li>Zhodnoťte úroveň ke skutečnosti. Dvakrát týdně na svahu je jiná zkušenost než jeden týden v roce.</li>'
          '<li>Vyberte typ lyže a přibližnou šířku pod nohou.</li>'
          '<li>Zjistěte hmotnost a výšku a porovnejte s tabulkou délek výrobce.</li>'
          '<li>Rozhodněte, zda hledáte komplet, nebo lyže samostatně s vázáním.</li>'
          '<li>Zkontrolujte, zda vázání odpovídá vašim botám, a nechte jej seřídit v servisu.</li></ol>'
          '<h2>Péče o lyže</h2>'
          '<p>Skluznice je nejcitlivější část lyže. Po sezóně nebo po každých několika dnech na svahu by měla být vyčištěna a navoskována. Pokud se do ní dostane kámen a vznikne škrábanec, opraví se plnidlem. Hrany se brousí, aby držely na tvrdém sněhu. '
          'Základní vosky najdete v kategorii <a href="/lyzarske-vosky/">vosky a mazání na lyže a snowboardy</a>. Po lyžování lyže otřete od vlhkosti, aby hrany nezrezivěly, a ukládejte je na suchém místě, ne na zahřátém topení a nepřepínejte je dlouho zapnuté ve stahovacích popruzích. '
          'Před novou sezónou nechte servis zkontrolovat vázání, hrany a skluznici.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš dlouhé a tuhé lyže pro začátečníka. Zatáčení pak stojí víc síly a zvyšuje se únava.</li>'
          '<li>Nákup podle designu bez ohledu na typ. Freeridová lyže na sjezdovce se chová jinak než carvingová.</li>'
          '<li>Vázání podle starých bot. Nová obuv může mít jinou normu podrážky a potřebuje kontrolu.</li>'
          '<li>Nepodcenit seřízení. Nastavení vázání ať provede servis, nikdy ho neodhadujte.</li>'
          '<li>Odkládání servisu na poslední chvíli. Před sezónou bývají dílny plné a lyže se vrací pozdě.</li></ul>'
          '<h2>Kdy kupovat</h2>'
          '<p>Nové kolekce vstupují do prodeje koncem léta a na podzim, výprodej starších modelů přichází v průběhu zimy a na jaře. Lyže z loňské kolekce se obvykle technicky neliší od novinek, mění se hlavně grafika. '
          'Zato nejžádanější délky mizí první, takže při výběru z velké škály je lepší nakupovat včas. Bazarové lyže mohou být zajímavé, ale jejich skluznici i hrany je vhodné nechat zkontrolovat a vázání prověřit v servisu. '
          'Při porovnávání nabídek na Sportece sledujte také, zda je u zboží uveden ročník kolekce a zda cena zahrnuje vázání.</p>',
    faq=[
        ('Jakou délku lyží zvolit?', 'Začátečník volí lyže zhruba k bradě až nosu, pokročilý až k čelu. Rozhoduje i hmotnost, proto zkontrolujte tabulku výrobce konkrétního modelu.'),
        ('Je lepší koupit komplet, nebo lyže bez vázání?', 'Komplet je pohodlný pro začátečníky a děti, protože vázání je už namontované. Samostatný nákup dává více volnosti při výběru vázání.'),
        ('Čím se liší carvingové a all-mountain lyže?', 'Carvingové jsou užší a určené pro upravené sjezdovky. All-mountain jsou o něco širší a zvládnou i sníh mimo trať, na tvrdém podkladu jsou ale méně hravé.'),
        ('Na co dát pozor u dámských lyží?', 'Bývají měkčí a lehčí. Hlavní je ale hmotnost a úroveň, ne jen označení pohlaví, a někdy sedí lépe unisex model.'),
        ('Kolik lyží potřebuje dítě?', 'Stačí jedny lyže na sezónu, které sedí velikostí a úrovní. Dětské lyže se často prodávají ve výměnných bazarech a půjčují, protože dítě rychle roste.'),
        ('Jak poznám, že lyže potřebují servis?', 'Viditelné škrábance na skluznici, ztupené nebo zrezivělé hrany a suchý bílý povrch skluznice jsou jasné signály. Vázání má kontrolovat servis každou sezónu.'),
        ('Mohu si vázání nastavit sám?', 'Nastavení uvolnění je bezpečnostní prvek a mělo by ho provádět servis podle hmotnosti a úrovně lyžaře. Nikdy ho neodhadujte.'),
        ('Co znamená rocker a camber?', 'Camber je klasické prohnutí lyže pod nohou pro přesný záběr hran. Rocker je zdvih špičky nebo paty, který zlepšuje plování a snadné zatáčení.'),
        ('Hodí se sjezdové lyže na skialpinismus?', 'Ne, jsou těžké a vázání nedovoluje zvednout patu. Na výstupy se používají skialpové lyže, pásy a vázání, jak ukazuje samostatná kategorie.'),
        ('Jak lyže převážet?', 'V tašce nebo vaku, který chrání hrany a skluznici, nebo na střešním boxu či nosiči. Lyže stáhněte tak, aby se nedřely o sebe a vázání nevyčnívalo.'),
        ('Kdy je dobré lyže navoskovat?', 'Před sezónou a pak podle používání. Když se skluznice zdá suchá a lyže se po sněhu méně rozjíždí, je čas na vosk.'),
    ])


# ------------------------------------------------------------------ detske-cyklohelmy
NEW['detske-cyklohelmy'] = dict(long=True,
    title='Dětské cyklohelmy: velikost, nastavení, výběr',
    desc='Dětské cyklistické helmy pro odrážedla, kola, koloběžky i brusle. Jak změřit hlavu, správně nastavit pásky a kdy helmu vyměnit.',
    intro='<p>Helma je pro dítě na kole, odrážedle nebo koloběžce nejdůležitější kus výbavy a zároveň ten, který se nejčastěji vybírá špatně. Příliš velká sklouzne do očí, příliš malá tlačí a dítě ji sundá. '
          'Kategorie <strong>dětské cyklohelmy</strong> sdružuje modely od nejmenších velikostí pro batolata až po juniorské helmy pro školáky. Liší se tvarem, hmotností, množstvím větracích otvorů, '
          'systémem nastavení obvodu a motivy, které dětem pomáhají přijmout, že ji nosit musí.</p>'
          '<p>Sporteka porovnává nabídku českých obchodů u stejného modelu, takže snadno ověříte, kde je skladem požadovaná velikost a barva. Nadřazená kategorie <a href="/cyklisticke-helmy/">cyklistické helmy</a> '
          'nabízí i modely pro dospělé, k dětské helmě pak vybírejte <a href="/detska-kola/">dětská kola a odrážedla</a>. V následujícím textu vysvětlíme měření hlavy, nastavení, typy konstrukce i péči o helmu.</p>',
    guide='<h2>Jak změřit hlavu a vybrat velikost</h2>'
          '<p>Základem je obvod hlavy, který změříte krejčovským metrem nebo provázkem asi dva prsty nad obočím a nad ušima, v místě, kde bude helma sedět. Hodnotu porovnejte s tabulkou výrobce u konkrétního modelu. '
          'Velikosti se u různých značek liší, takže stejné číslo u dvou helem neznamená stejné padnutí. Dětem se také při nákupu nevyplácí kupovat větší helmu na vyrůstání. Pokud helma plave, neochrání, jak má.</p>'
          + T(['Věkové označení', 'Typické použití', 'Co sledovat'], [
              ['Batolata (nejmenší velikosti)', 'odrážedla, sedačky na kole, tříkolky', 'nízká hmotnost, jemné popruhy, krytá týlová část'],
              ['Předškoláci', 'dětská kola s pomocnými kolečky a první kola bez nich', 'snadné nastavení jednou rukou, výrazné barvy'],
              ['Školáci', 'kolo, koloběžka, inline brusle', 'větrání, nastavitelný obvod, stabilní sedlo na hlavě'],
              ['Starší děti a junioři', 'silniční, horské i městské jízdy', 'střih podobný helmám dospělých, kšilt proti slunci']]) +
          '<p>Helma by měla sedět vodorovně na hlavě, tedy zhruba dva prsty nad obočím, a nesmí se naklánět dozadu ani dopředu. Po zapnutí podbradního pásku se při pohybu hlavou nesmí kývat. '
          'Zkuste dítěti helmu nasadit, zapnout a lehce zatřást hlavou nahoru a dolů. Pokud se pohne víc než o pár milimetrů, je třeba ji dotáhnout nebo zvolit menší velikost.</p>'
          '<h2>Správné nastavení krok za krokem</h2>'
          '<ol><li>Nasaďte helmu rovně na hlavu tak, aby chránila čelo. Přední hrana má být zhruba dva prsty nad obočím.</li>'
          '<li>Nastavte kolečko nebo systém obvodu v týlu, aby helma pevně obepínala hlavu, ale netlačila.</li>'
          '<li>Seřiďte popruhy tak, aby se spojily pod ušima ve tvaru písmene V a nikdy je nenechávejte zkroucené.</li>'
          '<li>Zapněte podbradní pásek. Mezi bradou a páskem by měl být prostor zhruba na jeden prst.</li>'
          '<li>Zkontrolujte pohyb. Otevřete ústa. Měli byste pocítit lehký tah za helmu. Zatřeste hlavou. Helma musí zůstat na místě.</li></ol>'
          '<p>Nastavení opakujte, když dítě změní účes, nasadí čepici pod helmu, nebo když povyroste. Silné vlasy a culíky mají být upraveny tak, aby nebránily přilnutí helmy, a zadní otvor mnohé modely na culík počítají.</p>'
          '<h2>Konstrukce: skořepina, pěna a větrání</h2>'
          '<p>Většina dětských helem má vnější plastovou skořepinu spojenou s vnitřní tlumící pěnou. Při nárazu se pěna deformuje a pohlcuje část energie, proto je helma jednorázová a po větším nárazu se vyměňuje, i když není vidět poškození. '
          'Tvrdá skořepina chrání lépe před otěrem a odolává běžnému zacházení, což u dětí oceníte, protože helmy často padají nebo se odhazují. Modely s in-mold technologií mají skořepinu nalisovanou přímo na pěnu a bývají lehčí a vzdušnější.</p>'
          '<p>Větrací otvory ovlivňují komfort v horku, ale také bezpečnostní vlastnosti, protože příliš velké otvory oslabují skořepinu. Moderní modely proto mají otvory vedené kanálky, které pomáhají proudění vzduchu. '
          'Vnitřní síťka proti hmyzu je užitečná na louce a u vody. Vnitřní vycpávky by měly jít vyjmout a vyprat. Reflexní prvky a možnost připevnit světlo zvyšují viditelnost za šera.</p>'
          '<h2>Typ helmy podle jízdy</h2>'
          + T(['Druh jízdy', 'Vhodná helma', 'Poznámka'], [
              ['Odrážedlo a tříkolka', 'lehká helma s krytým týlem', 'dítě padá častěji dozadu, proto chcete dobré krytí týlu'],
              ['Rodinný výlet na kole', 'univerzální helma s větráním a kšiltem', 'nejčastější volba, snadno se nastavuje'],
              ['Koloběžka a inline brusle', 'helma s hlubším týlem', 'u některých sportů pomůže i vhodné chrániče kolen a loktů'],
              ['Silniční jízda s rodiči', 'lehká aerodynamičtější helma', 'najdete ji v <a href="/silnicni-cyklohelmy/">silničních a gravel helmách</a>'],
              ['Bike park a trail', 'helma s delším zadním krytím a kšiltem', 'více v kategorii <a href="/mtb-a-integralni-helmy/">MTB, enduro a integrální helmy</a>'],
              ['Městská jízda do školy', 'helma s reflexními prvky', 'srovnejte i <a href="/mestske-cyklohelmy/">městské cyklohelmy</a>']]) +
          '<h2>Certifikace a označení</h2>'
          '<p>Helmy na evropském trhu musí splňovat příslušnou bezpečnostní normu a mít na sobě označení, které to prokazuje: pro cyklistické helmy jde o normu EN 1078 a značku CE. Značka by měla být uvedena uvnitř helmy a v návodu. '
          'U samostatně dovážených modelů z neověřených zdrojů si označení raději zkontrolujte, protože nepřesné údaje v e-shopu se občas objeví. Helma se nekupuje podle ceny, ale podle toho, že má potřebné označení, správně sedí a že ji dítě bude nosit.</p>'
          '<h2>Motivy, barvy a motivace dítěte</h2>'
          '<p>Nejlepší helma je ta, kterou dítě nosí. Proto se vyplatí nechat dítě vybrat barvu nebo motiv z několika bezpečných kandidátů. Postavičky a filmové hrdinové bývají u nejmenších oblíbené. '
          'Starší děti raději vypadají jako rodiče, takže ocení střih helmy dospělých ve zmenšené velikosti. Světlé a výrazné barvy zlepšují viditelnost v provozu. '
          'Důležité je také jít dítěti příkladem. Pokud helmu nosí rodiče, nosí ji obvykle i děti, a stává se normou rodinné jízdy.</p>'
          '<h2>Co s helmou po pádu a kdy ji vyměnit</h2>'
          '<p>Pokud dítě po pádu s helmou narazilo hlavou, helmu vyřaďte, i když na povrchu není vidět poškození. Pěna uvnitř mohla ztratit schopnost pohltit další náraz. Vyměňte ji také v případě prasklin skořepiny, poškozených popruhů nebo rozbité spony. '
          'Bez nehody se helma obvykle mění po několika letech, jak doporučuje výrobce, nebo když dítě povyroste. Pěna, plast i popruhy stárnou vlivem slunce, potu a teplot, takže i nepoužívaná helma má omezenou životnost.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Helmu čistěte vlažnou vodou a jemným mýdlem, nikdy rozpouštědly nebo benzínem, které mohou poškodit pěnu a plast. Vnitřní vycpávky se dají u většiny modelů vyjmout a vyprat. '
          'Nenechávejte helmu v zavazadlovém prostoru auta na slunci, kde se přehřívá, a neodkládejte na ni těžké věci. Nelepte na ni samolepky, které by mohly obsahovat chemikálie narušující materiál, pokud výrobce nepovolí jinak. '
          'Nepoužívejte ji k jiným účelům než ke sportu, na který je určena, a děti učte nezavěšovat ji na řídítka za pásek.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Dětské helmy v nabídce vyrábějí například {B(("rockbros", "Rockbros"), ("ked", "KED"), ("alpina", "Alpina"), ("abus", "Abus"), ("uvex", "Uvex"), ("crazy-safety", "Crazy Safety"))}. '
          f'S oblíbenými motivy se potkáte u značky {B(("disney", "Disney"))}, doplňují je {B(("etape", "Etape"), ("fox", "Fox"), ("cairn", "Cairn"), ("haven", "Haven"), ("force", "Force"))}. '
          'Střihy a systémy nastavení se liší, proto je dobré zkoušet na konkrétním dítěti, případně objednávat s možností výměny.</p>'
          '<h2>Roční období a počasí</h2>'
          '<p>V létě rozhoduje větrání a světlá barva, která se na slunci méně ohřívá. Dítě s přehřátou hlavou jízdu rychle vzdává a helmu sundává. Na jaře a na podzim se hodí menší větrání nebo tenká čepice určená pod helmu, '
          'pokud se ještě vejde bez změny obvodu. Za deště pomůže kšilt, ale jízda po mokrých cestách vyžaduje pomalejší tempo a opatrnější brzdění, což by měli děti znát. '
          'Při jízdě za šera nebo večer pořiďte reflexní nálepky či světlo na helmu, pokud model upevnění nabízí.</p>'
          '<h2>Rodinné pravidlo helmy</h2>'
          '<p>Nastavte si před výletem krátký rituál: helma na hlavu, kontrola popruhů, teprve pak nasednout. Dítě se naučí kontrolovat sebe i mladší sourozence a vy máte jistotu, že na to nezapomene. '
          'Zvlášť u dětí, které si chtějí hrát na dvoře, platí, že helma je součástí kola či odrážedla, ne něco navíc pro dlouhé jízdy. Při opakovaných výletech helmu vyzkoušejte po každé větší změně účesu nebo oblečení.</p>'
          '<h2>Co k helmě pořídit</h2>'
          '<p>Helma je začátek. K dětskému kolu patří odpovídající velikost podle průměru kol, tedy <a href="/detska-kola-12-14-palcu/">12 a 14 palců</a>, <a href="/detska-kola-16-palcu/">16 palců</a>, '
          '<a href="/detska-kola-20-palcu/">20 palců</a> nebo <a href="/detska-kola-24-palcu/">24 palců</a>. Nejmenší začínají na <a href="/odrazedla/">odrážedlech</a> nebo <a href="/detske-trikolky/">tříkolkách</a>, '
          'na kolečkových sportech používají děti také <a href="/kolobezky/">koloběžky</a> a <a href="/inline-brusle/">inline brusle</a>. '
          'Při jízdě za rodičem oceníte <a href="/cyklo-sedacky-a-voziky/">dětské sedačky a vozíky za kolo</a>, kde je helma pro dítě rovněž nutná, pokud to doporučuje výrobce. '
          'K aktivním jízdám se hodí <a href="/cyklo-chranice/">chrániče pro cyklisty</a>, <a href="/cyklisticke-rukavice/">cyklistické rukavice</a> a při soumraku <a href="/cyklo-svetla/">světla na kolo</a>. '
          'Sluneční záře a hmyz odstíní <a href="/cyklisticke-bryle/">cyklistické brýle</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kupování helmy na vyrůstání. Příliš velká helma sedí špatně a při pádu sklouzne.</li>'
          '<li>Vyvázané nebo zkroucené popruhy. Pásek má ležet rovně a pevně.</li>'
          '<li>Nošení čepice nebo kapuce pod helmou, která mění sedlo helmy. Tenká čepice na cyklistiku je výjimka.</li>'
          '<li>Použití helmy po pádu. Pěna je určena k jednomu nárazu.</li>'
          '<li>Půjčování helmy mezi sourozenci bez ověření velikosti. Každé dítě potřebuje helmu, která mu sedí.</li>'
          '<li>Helma na hlavě jen na delších jízdách. Úrazy se dějí i při pomalé jízdě před domem.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Nejlepší postup je změřit hlavu, porovnat s tabulkou, vybrat dva až tři modely a ověřit na dítěti. U e-shopů sledujte lhůtu na výměnu a zda je uvedena velikost v centimetrech. '
          'Při nákupu na Sportece porovnejte i tvary helem a to, zda jsou uvedené informace o hmotnosti. Lehčí helma bývá pro dítě příjemnější, protože ho netíží na krku.</p>',
    faq=[
        ('Jak poznám, že helma dítěti sedí?', 'Sedí vodorovně dva prsty nad obočím, po zapnutí popruhů se nekývá a při zatřesení hlavou se pohne jen o pár milimetrů. Mezi bradou a páskem je asi prst místa.'),
        ('Mám koupit větší helmu na vyrůstání?', 'Ne. Příliš velká helma sklouzne, nechrání čelo a při pádu ztrácí smysl. Kupujte aktuální velikost a po růstu ji vyměňte.'),
        ('Od kdy má dítě nosit helmu?', 'Od prvních jízd na odrážedle, tříkolce nebo v sedačce na kole, pokud to doporučuje výrobce sedačky. Čím dřív si na ni zvykne, tím menší bude odpor.'),
        ('Kdy helmu vyměnit?', 'Po jakémkoli větším nárazu, při poškozené skořepině nebo popruzích, anebo když dítě povyrostlo. Podle doporučení výrobce se mění i po několika letech používání.'),
        ('Můžu helmu předat mladšímu sourozenci?', 'Jen pokud je bez nárazu, v dobrém stavu a sedí. Každé dítě má jiný obvod hlavy a pěna se věkem opotřebovává.'),
        ('Jak helmu čistit?', 'Vlažnou vodou a jemným mýdlem, vycpávky se dají u většiny modelů vyprat. Nepoužívejte rozpouštědla, mohla by poškodit pěnu.'),
        ('Jaká helma se hodí na koloběžku a brusle?', 'Cyklistická helma se používá i na koloběžku, hlavně s dobrým krytím týlu. Pro náročné jízdy zvažte i chrániče kolen, loktů a zápěstí.'),
        ('Co znamená in-mold?', 'Vnější skořepina je spojena s pěnou při výrobě. Helma je lehčí a vzdušnější, ale povrch může být náchylnější k poškrábání, proto ji nepouštějte na zem.'),
        ('Dítě helmu nechce nosit. Co dělat?', 'Nechte ho vybrat barvu nebo motiv a noste helmu i vy. Neustupujte, jízda bez helmy se nekoná, rutina se brzy ustálí.'),
        ('Je třeba helma s kšiltem?', 'Kšilt chrání před sluncem a deštěm a pro volnočasové jízdy je vhodný. Při jízdě v lese nebo bike parku pomáhá i proti větvičkám.'),
        ('Dá se helma nosit i při jízdě v dětské sedačce?', 'Ano, pokud to výrobce sedačky doporučuje. Helma s plochým týlem je pohodlnější, protože dítě opírá hlavu o opěrku.'),
    ])


# ------------------------------------------------------------------ damske-plavky
NEW['damske-plavky'] = dict(long=True,
    title='Dámské plavky: sportovní, jednodílné, dvoudílné',
    desc='Dámské plavky na plavání, pláž i vodní sporty: jednodílné, dvoudílné, sportovní se zády do tvaru X. Materiál, střih, velikost a péče.',
    intro='<p>Dámské plavky se dělí do dvou světů. Jedny jsou určeny pro pravidelné plavání v bazénu, kde musí vydržet chlór a nesmí překážet při tempu. Druhé patří na pláž, k vodě a na dovolenou, '
          'kde se klade důraz na střih, barvy a pohodlí při opalování. V kategorii <strong>dámské plavky</strong> najdete jednodílné, dvoudílné, sportovní, závodní i módní kousky, '
          'včetně modelů s podporou prsou, sníženým výstřihem a různými typy zad.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného zboží, takže snadno zjistíte, kde je skladem vaše velikost. Nadřazená kategorie <a href="/plavky/">plavky</a> '
          'zahrnuje také <a href="/panske-plavky/">pánské plavky</a> a <a href="/detske-plavky/">dětské plavky</a>. V následujícím textu rozebereme střihy, materiály, velikosti, péči i doplňky.</p>',
    guide='<h2>Druhy dámských plavek</h2>'
          '<p>Než začnete porovnávat jednotlivé kusy, ujasněte si, k čemu plavky použijete. Rozdíl mezi sportovním a plážovým modelem je výrazný a špatná volba se projeví hned po prvním plavání.</p>'
          + T(['Střih', 'Hodí se na', 'Na co dát pozor'], [
              ['Sportovní jednodílné s nízkým výstřihem na zádech', 'pravidelné plavání, kondiční trénink', 'ramínka musí sedět a nesmí sklouzávat při obrátce'],
              ['Závodní plavky (kneeskin, jammer)', 'soutěže a velmi intenzivní trénink', 'obtížnější oblékání, zpravidla těsné střihy'],
              ['Módní jednodílné', 'pláž, koupaliště, dovolená', 'podšívka a výztuž jsou pohodlné, ale hůř odolávají chlóru'],
              ['Dvoudílné', 'opalování, rekreační plavání, pláž', 'horní díl podle objemu prsou, kalhotky podle sedu'],
              ['Tankiny a plavky se sukénkou', 'rodinné koupání, pohodlí', 'delší střih zakrývá břicho'],
              ['Plavky pro surf a vodní sporty', 'surf, paddleboard, aktivní dovolená', 'pevné držení, často zip nebo šněrování'],
              ['Plavky s UV ochranou', 'delší pobyt na slunci', 'oblečení se zakrytými zády a rameny']]) +
          '<p>Podle teploty vody a času strávenému v ní doplňte výbavu o <a href="/lycra-a-uv-tricka/">lycru a UV trička</a>, <a href="/neopreny/">neopreny</a> nebo <a href="/plavecke-pomucky/">plavecké pomůcky</a>.</p>'
          '<h2>Materiál: polyester, elastan a chlór</h2>'
          '<p>Většina plavek je směsí polyamidu nebo polyesteru s elastanem, který dodává pružnost. Pro bazén je zásadní odolnost proti chlóru. Polyesterové plavky a jejich varianty, které se označují jako chlorine resistant, vydrží více sezón než ty, které mají vysoký podíl elastanu. '
          'Elastan je citlivý na chlór, olej na opalování i na teplo. Módní plavky s vyšším podílem elastanu jsou na moře a k rybníku v pořádku, v chlorované vodě se ale opotřebují výrazně dřív. '
          'Podšívka a vyjímatelné vycpávky zvyšují komfort, ale pomaleji schnou. Lehčí tkaniny a sítě naopak schnou rychle a nepijí vodu.</p>'
          + T(['Vlastnost', 'Sportovní plavky', 'Plážové a módní plavky'], [
              ['Typický materiál', 'polyester s menším podílem elastanu', 'polyamid s elastanem, často s podšívkou'],
              ['Odolnost vůči chlóru', 'vysoká', 'nižší, vyžaduje opatrné používání'],
              ['Podpora prsou', 'zpevněný střih, někdy vnitřní podpora', 'vycpávky, kosticky, vyjímatelné kapsy'],
              ['Rychlost schnutí', 'rychlá, tenká tkanina', 'záleží na podšívce'],
              ['Střih zad', 'úzká ramínka, závodní záda', 'široká škála, od šněrování po otevřená záda']]) +
          '<h2>Jak vybrat velikost</h2>'
          '<p>Plavky se kupují pevně, ale ne nepříjemně. Po namočení se tkanina trochu uvolní, proto má sedět těsně, nesmí ale tlačit v podpaží a v rozkroku. Změřte obvod hrudníku pod prsy, přes prsa a boky a porovnejte s tabulkou konkrétní značky. '
          'Střih Speedo se může lišit od střihu Arena nebo od módní značky, a proto velikost nikdy nepředpokládejte. Při pochybnostech porovnejte tabulku výrobce a prohlédněte si recenze, zda modely vycházejí větší, nebo menší.</p>'
          '<h3>Co zkontrolovat při zkoušení</h3>'
          '<ul><li>Ramínka nemají klouzat ani se zařezávat. Při předklonu nesmí vypadnout prsa.</li>'
          '<li>Zadní část má pokrývat sedací partie a při dřepu nemá sjíždět.</li>'
          '<li>Švy mají být ploché, aby netřely při plavání.</li>'
          '<li>Podšívka musí být neprůsvitná, i když je mokrá.</li>'
          '<li>Plavky zkoušejte přes spodní prádlo a hygienickou vložku v kalhotkách neodstraňujte; mnoho prodejen jinak zkoušené zboží nevrací.</li></ul>'
          '<h2>Střihy zad a ramínek</h2>'
          '<p>Při pravidelném plavání jsou praktická záda ve tvaru X nebo úzká racerback, která drží ramínka na místě a dávají volnost lopatkám. Široká ramínka jsou pohodlná při pobytu na pláži, ale při kraulu se mohou sesouvat. '
          'Zavazování za krkem lépe vyhovuje při opalování a méně při plavání. Plavky s kroužky nebo kovovými komponenty oceníte na pláži, ale chlór je rychle poškodí. U modelů s kapsami na vložky zkontrolujte, zda je lze vyjmout.</p>'
          '<h2>Plavání, pláž nebo vodní sporty</h2>'
          '<h3>Bazén a trénink</h3>'
          '<p>Vybírejte sportovní plavky s odolným materiálem a bez ozdob. Hodí se i delší kalhotky, které se nezařezávají. K plavání patří <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plavecké čepice</a>, '
          'a pro lepší techniku <a href="/plavecke-pomucky/">plavecké pomůcky</a>. Do šatny se hodí <a href="/pantofle-a-zabky/">pantofle a žabky</a> a <a href="/sportovni-tasky/">sportovní taška</a>.</p>'
          '<h3>Moře a jezero</h3>'
          '<p>Slaná voda a slunce poškozují barvy i pružnost, takže po koupání plavky opláchněte čistou vodou. Dvoudílné plavky nebo tankiny se dobře přizpůsobí různým aktivitám. '
          'V kamenitém terénu dno chrání <a href="/obuv-do-vody/">boty do vody</a>, a pro další výbavu si prohlédněte <a href="/plazove-doplnky/">plážové doplňky a osušky</a> a <a href="/nafukovaci-hracky/">nafukovací hračky a lehátka do vody</a>.</p>'
          '<h3>Aktivní dovolená a surf</h3>'
          '<p>Při paddleboardingu, surfování nebo šnorchlování se nehodí volné a vyztužené střihy. Hledejte plavky se pevným upevněním, případně lycru s dlouhým rukávem. '
          'Pro chladnější vody pomůže neopren, kterému se věnuje kategorie <a href="/neopreny/">neopreny</a>. Pro prohlížení podmořského světa využijete <a href="/snorchlovani/">šnorchlování a potápění</a>. '
          'Celý obor shrnuje <a href="/vodni-sporty/">vodní sporty a plavání</a>.</p>'
          '<h2>Podpora prsou a pohodlí</h2>'
          '<p>Při plavání nebo vodním sportu záleží na držení. Sportovní plavky mají vnitřní podporu nebo zpevněný střih, módní kousky vycpávky a kosticky. Pokud potřebujete větší podporu, hledejte plavky s širokými ramínky a pevným spodním pásem. '
          'Pro cvičení na suchu je k dispozici <a href="/sportovni-podprsenky/">sportovní podprsenka</a>, ale do vody nepatří. Při výběru zvažte, zda budete skákat nebo se potápět. Pokud ano, dbejte na to, aby plavky držely i při nárazu vody.</p>'
          '<h2>Barvy, vzory a střih podle postavy</h2>'
          '<p>Tmavé a jednobarevné plavky nejméně prosvítají a nejlépe drží tvar, proto se hodí na plavání. Vzory a světlé odstíny jsou veselé, ale po sezóně v chlóru nebo na slunci bledne hlavně červená a fialová. '
          'Svislé pruhy a tmavé panely po stranách opticky protahují postavu, vysoký pas zakrývá břicho a kalhotky s vyšším střihem na boku zvýrazňují nohy. Při větším objemu prsou se osvědčují široká ramínka a zpevněný spodní pás, '
          'u menšího objemu pomáhají lehké vycpávky nebo volánky. Přesto neexistuje jediný správný střih, rozhoduje pohodlí a to, jak se v plavkách cítíte.</p>'
          '<h3>Plavky při těhotenství a po porodu</h3>'
          '<p>V těhotenství se mění objem a plavky potřebují pružnější střih. Hledejte modely s nastavitelnými ramínky, širokým pasem a podporou prsou. Konkrétní doporučení, zda a jak plavat, ale patří lékaři nebo porodní asistentce, ne e-shopu.</p>'
          '<h2>Doplňky k plavkám</h2>'
          '<p>Na pláž se hodí osuška nebo plážové pončo a lehká taška, které popisuje kategorie <a href="/plazove-doplnky/">plážové doplňky a osušky</a>. Pro děti, které chodí s vámi, zvolte <a href="/detske-plavky/">dětské plavky</a> se stejnou péčí o materiál. '
          'Při plavání ve volné vodě nebo na dovolené je dobré mít plovací vestu, jak ukazuje kategorie <a href="/plovaci-vesty/">plovací a záchranné vesty</a>. Samostatně pak vybírejte sluneční brýle ze sekce <a href="/sportovni-bryle/">sportovní a sluneční brýle</a>.</p>'
          '<h2>Plavky na cesty</h2>'
          '<p>Na dovolenou si vezměte alespoň dvoje plavky, abyste mohli střídat mokré a suché. Skládací taška na mokré věci chrání ostatní prádlo. Plavky balte až po úplném vyschnutí, jinak zaplesniví. '
          'Pokud letíte, obléknete je pod oblečení, což ušetří místo a hodí se při zpoždění zavazadla. V hotelových bazénech často platí pravidla o hygieně a sprše před vstupem, tak je dodržujte.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší výběr sportovních plavek mají značky {B(("speedo", "Speedo"), ("arena", "Arena"), ("tyr", "Tyr"), ("finis", "Finis"), ("funkita", "Funkita"))}. '
          f'Plážové a módní kousky nabízejí {B(("roxy", "Roxy"), ("trendyol", "Trendyol"), ("4f", "4F"), ("calvin-klein", "Calvin Klein"), ("koton", "Koton"), ("edoti", "Edoti"), ("decathlon", "Decathlon"))}. '
          'Střihy se liší, proto vždy porovnejte velikostní tabulky.</p>'
          '<h2>Péče o plavky</h2>'
          '<p>Po každém koupání je opláchněte ve studené nebo vlažné čisté vodě, aby se odstranil chlór, sůl a krém. Nevyždímávejte je silou ani nekruťte. Perte ručně šetrným prostředkem, nikdy v pračce na vysokou teplotu a nesušte v sušičce. '
          'Suste je rozložené ve stínu, ne na radiátoru a ne na přímém slunci, které vybledne barvy a poškodí elastan. Nesedejte v mokrých plavkách na drsný povrch, třeba na kamenné okraje bazénu. '
          'Při pravidelném plavání střídejte dva až tři kusy, aby měla tkanina čas na zotavení. Opotřebení poznáte podle průsvitnosti, ztráty pružnosti nebo vytahaného střihu.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Módní plavky do bazénu. Rychle se opotřebují a ztratí tvar.</li>'
          '<li>Příliš velké plavky. Při plavání se nafouknou a tahají vodu.</li>'
          '<li>Sušení na slunci a topení. Elastan a barvy trpí.</li>'
          '<li>Nákup přes sezónu bez zkoušky. Střih se liší podle značky a může vám sedět jinak, než čekáte.</li>'
          '<li>Zapomenutí opláchnout po moři. Sůl a písek tkaninu opotřebují.</li></ul>'
          '<h2>Kdy plavky kupovat</h2>'
          '<p>Nové kolekce přicházejí na jaře, ale nejlepší výběr velikostí bývá na začátku sezóny. Výprodeje se objevují v létě a na podzim, kdy zůstávají především mimosezónní velikosti. '
          'Sportovní modely se mění méně než módní, takže starší kolekce jsou zpravidla použitelné. Při koupi na Sportece porovnejte i více obchodů a ověřte, zda lze zboží vrátit, protože zkoušení plavek je u internetových nákupů omezené.</p>',
    faq=[
        ('Jaké plavky zvolit na pravidelné plavání?', 'Sportovní jednodílné z polyesteru odolného vůči chlóru, s úzkými ramínky a neklouzavým střihem. Módní plavky se v chlorované vodě rychle opotřebují.'),
        ('Jak vybrat velikost dámských plavek?', 'Změřte hrudník pod prsy, přes prsa a boky a porovnejte s tabulkou výrobce. Plavky mají sedět těsně, ale netlačit v podpaží.'),
        ('Co znamená chlorine resistant?', 'Materiál je navržen tak, aby odolával chlóru v bazénu. Plavky vydrží déle než klasické elastanové, ale i ty je třeba po plavání opláchnout.'),
        ('Je lepší jednodílné, nebo dvoudílné?', 'Na plavání jednodílné, protože drží na místě. Na pláž a opalování je to otázka pohodlí a střihu, dvoudílné se hodí i k pohybu.'),
        ('Jak plavky prát?', 'Ručně v čisté vlažné vodě s jemným prostředkem, bez ždímání. Pračka a sušička poškozují elastan.'),
        ('Proč jsou plavky po namočení průsvitné?', 'Může jít o příliš tenkou tkaninu nebo opotřebení. Hledejte modely s podšívkou nebo tmavší barvy, a plavky po sezóně vyměňte.'),
        ('Mohu v plavkách cvičit?', 'Pro vodní sporty ano, pro jiné pohybové aktivity se hodí oblečení určené pro daný sport. Plavky nejsou určeny na dlouhé sezení na tvrdém povrchu.'),
        ('Jak dlouho plavky vydrží?', 'Záleží na materiálu a používání. Sportovní plavky při pravidelném tréninku vydrží několik měsíců až let, módní plavky v chlóru kratší dobu.'),
        ('Pomůže UV oblečení k ochraně kůže?', 'Zakrytá kůže je méně vystavena slunci, což pomáhá. Neznamená to, že se není třeba chránit krémem a stínem.'),
        ('Co si vzít do bazénu navíc?', 'Plavecké brýle, čepici, osušku, pantofle a tašku na mokré věci. Podle cíle se hodí i plavecké pomůcky a láhev na pití.'),
        ('Dají se plavky vrátit?', 'Záleží na podmínkách obchodu. Při online nákupu zkontrolujte zásady vrácení zboží, hygienické štítky nesundávejte před zkoušením.'),
    ])
