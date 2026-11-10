"""sporteka.cz — texts of wave 2, part B: football, hockey, scooters (3. 11. 2026). Same rules as texty_vlna1a.py."""
from texty_vlna1a import T

NEW = {}

NEW['kopacky'] = dict(short=True,
    title='Kopačky – lisovky, turfy, halovky | Porovnání cen',
    desc='Kopačky pánské, dámské a dětské: lisovky, turfy, halovky a tenisky na futsal. Porovnejte ceny a velikosti skladem v českých sportovních obchodech.',
    intro='<p><strong>Kopačky</strong> se vybírají podle povrchu, na kterém budete hrát. Na přírodní trávu jsou <strong>lisovky (FG)</strong> s kolíky, na umělou trávu <strong>turfy (TF)</strong> s malými nopy, '
          'na tvrdé či hliněné hřiště <strong>multinopy (MG, AG)</strong> a do haly <strong>halovky</strong> s hladkou gumovou podrážkou. Špatný typ znamená horší trakci a vyšší riziko zranění kolene a kotníku.</p>'
          '<p>Na Sportece porovnáte ceny kopaček z českých obchodů a vidíte, které velikosti jsou skladem. Na trénink ve městě se hodí <a href="/treninkova-obuv/">tréninková obuv</a>, k balonu <a href="/fotbalove-mice/">fotbalové míče</a>.</p>',
    guide='<h2>Jak vybrat kopačky</h2>'
          '<p>Kopačky jsou jediná část výbavy, která přímo ovlivňuje hru. Správně padnoucí pár dá jistotu při driblování, střelbě i zastavení, špatná velikost naopak způsobí puchýře a ztrátu citu pro míč.</p>'
          '<h3>Typ podrážky podle povrchu</h3>'
          + T(['Označení', 'Povrch', 'Podrážka'], [['FG', 'přírodní tráva', 'pevné kolíky'], ['SG', 'měkká, mokrá tráva', 'vyměnitelné kovové kolíky'], ['AG / MG', 'umělá tráva, tvrdší hřiště', 'více krátkých kolíků'], ['TF', 'umělá tráva, škvára, asfalt', 'malé gumové nopy'], ['IC / IN', 'hala, parkety', 'hladká guma']]) +
          '<h3>Materiál svršku</h3>'
          '<ul><li><strong>Přírodní kůže:</strong> pohodlná, roztáhne se po rozhrání, vyžaduje péči.</li>'
          '<li><strong>Syntetika:</strong> lehčí, nenasákne a drží tvar, hodí se do deště.</li>'
          '<li><strong>Pletený svršek:</strong> ponožkový střih, těsně obepíná nohu, pohodlný od prvního zápasu.</li></ul>'
          '<h3>Velikost a střih</h3>'
          '<p>Kopačky mají sedět těsněji než běžná obuv. Palec se nemá dotýkat špičky a pata nesmí vyskakovat. Značky mají různé střihy, proto si u každého páru ověřte šířku a pocit v přední části. U dětí počítejte s rezervou do 1 cm.</p>'
          '<h3>Pozice na hřišti</h3>'
          '<p>Útočníci volí lehké kopačky pro rychlost, záložníci důraz na cit a přihrávky, obránci pevnější materiál. Brankáři potřebují především dobré <a href="/brankarske-rukavice/">brankářské rukavice</a>.</p>'
          '<h3>Péče o kopačky</h3>'
          '<p>Po zápase očistěte kolíky a svršek od bláta, vyndejte vložky a nechte schnout při pokojové teplotě, ne na topení. Kůže se potírá krémem, aby neprasklá. K ochraně holení slouží <a href="/fotbalove-chranice-a-stulpny/">fotbalové chrániče a štulpny</a>.</p>',
    faq=[('Jaké kopačky na umělou trávu?', 'Turfy (TF) s malými nopy nebo multinopy (AG, MG). Lisovky s dlouhými kolíky se na umělé trávě zabodávají a zatěžují koleno.'),
         ('Jaký je rozdíl mezi lisovkami a turfy?', 'Lisovky mají kolíky pro přírodní trávu, turfy malé nopy pro umělý povrch, škváru a tvrdší hřiště.'),
         ('Jak vybrat velikost kopaček?', 'Těsně, ale bez tlaku. Palec se nesmí dotýkat špičky a pata nesmí vyskakovat. Změřte si nohu odpoledne.'),
         ('Hodí se kopačky na halu?', 'Ne, do haly patří halovky s hladkou gumovou podrážkou. Kolíky by poškodily podlahu.'),
         ('Jak vyčistit kopačky?', 'Odstraňte hrubé bláto kartáčem, otřete vlhkým hadrem a sušte při pokojové teplotě. Nikdy ne na radiátoru ani v sušičce.'),
         ('Jaké kopačky pro dítě?', 'Lehké a pohodlné s nízkými kolíky podle povrchu, kde dítě trénuje. Většina dětí začíná s multinopy nebo turfy.')],
)

NEW['dresy'] = dict(short=True,
    title='Dresy – fotbalové, hokejové, basketbalové | Sporteka',
    desc='Dresy klubů a reprezentací: fotbal, hokej, basketbal. Originální i tréninkové dresy pánské, dámské a dětské. Porovnejte ceny v českých obchodech.',
    intro='<p><strong>Dresy</strong> patří mezi nejoblíbenější fanouškovské i sportovní oblečení. Najdete tu fotbalové dresy klubů a reprezentací, hokejové dresy, basketbalové a americké dresy NBA nebo NHL. '
          'Originální replika má přesný střih a logo, zatímco volnější fanouškovská verze je levnější a pohodlná pro každodenní nošení.</p>'
          '<p>Na Sportece porovnáte ceny dresů v českých obchodech a vidíte velikosti skladem. K hokeji patří <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>, ke sportovnímu oblečení pak <a href="/sportovni-tricka/">sportovní trička</a> a <a href="/teplaky/">tepláky</a>.</p>',
    guide='<h2>Jak vybrat dres</h2>'
          '<p>Dres se hodí na zápas, trénink i do ulic. Podle toho, k čemu ho chcete, se liší materiál, střih a cena.</p>'
          '<h3>Replika, nebo autentický dres</h3>'
          '<ul><li><strong>Replika (stadium):</strong> volnější střih, odolný materiál, určená pro fanoušky i amatérské hráče.</li>'
          '<li><strong>Autentický (match, authentic):</strong> střih a technologie jako na hřišti, těsnější, lehčí a dražší.</li>'
          '<li><strong>Tréninkový dres:</strong> bez klubových log nebo s nimi, funkční a odolný.</li></ul>'
          '<h3>Velikosti</h3>'
          '<p>Značky velikosti značí různě, proto se řiďte tabulkou výrobce u konkrétního produktu. U autentických dresů často vybírejte o velikost větší, replika sedí volněji.</p>'
          + T(['Obvod hrudníku', 'Velikost'], [['88–96 cm', 'S'], ['96–104 cm', 'M'], ['104–112 cm', 'L'], ['112–120 cm', 'XL']]) +
          '<h3>Materiál a údržba</h3>'
          '<p>Dresy ze syntetiky odvádějí pot a rychle schnou. Perte je naruby ve vlažné vodě, nežehlete potisk a nesuštěte v sušičce, protože znaky se zvlní.</p>'
          '<h3>Potisk jména a čísla</h3>'
          '<p>Potisk dělá dres osobním, ale pozdější zpětný prodej snižuje. Pokud ho chcete, vyberte oficiální provedení, které drží tvar při praní.</p>'
          '<p>Tipy na další kolekce najdete v kategoriích <a href="/fotbal/">fotbal</a> a <a href="/hokej/">hokej</a>.</p>',
    faq=[('Jak vybrat velikost dresu?', 'Podle tabulky výrobce a obvodu hrudníku. Replika sedí volněji, autentický dres je přiléhavý, proto vezměte větší.'),
         ('Jaký je rozdíl mezi replikou a autentickým dresem?', 'Autentický má střih a materiál jako hráči na hřišti, bývá lehčí a dražší. Replika je volnější a odolná.'),
         ('Jak prát fotbalový dres?', 'Naruby, ve vlažné vodě do 30 °C a bez aviváže. Nesušit v sušičce a nežehlit potisk.'),
         ('Lze si nechat vytisknout jméno a číslo?', 'Ano, u většiny obchodů při objednávce, nebo u dresů s oficiálním potiskem hráčů. Stranu potisku volte podle návodu.'),
         ('Kde najdu dres reprezentace?', 'Použijte filtr značky a hledejte název reprezentace v názvu produktu. Porovnání cen ukazuje všechny obchody.'),
         ('Dres pro děti – jakou velikost?', 'Podle výšky dítěte, ne věku. Velikosti 128 až 164 odpovídají výšce v centimetrech.')],
)

NEW['hokej'] = dict(short=True,
    title='Hokejové vybavení – hokejky, brusle, chrániče | Sporteka',
    desc='Hokejové vybavení: hokejky, brusle, chrániče, helmy, rukavice a dresy. Porovnejte ceny a dostupnost v českých sportovních obchodech.',
    intro='<p><strong>Hokejové vybavení</strong> musí sedět a chránit, protože hokej je kontaktní sport s vysokou rychlostí. Základ tvoří <a href="/hokejove-brusle/">brusle</a>, <a href="/hokejky/">hokejka</a>, '
          '<a href="/hokejove-helmy-a-mrizky/">helma s mřížkou</a> a <a href="/hokejove-chranice/">chrániče</a>. Brankáři mají samostatnou výbavu v kategorii <a href="/hokejove-brankarske-vybaveni/">hokejové brankářské vybavení</a>.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů. Vidíte ceny, slevy a velikosti, které jsou skladem. Pro rekreační hráče je lepší nižší řada, pro ligové hráče vyšší.</p>',
    guide='<h2>Jak sestavit hokejovou výbavu</h2>'
          '<p>Hokejové vybavení se kupuje po částech. Nejdřív brusle a helma, na kterých šetřit nemá smysl, potom hokejka, rukavice a chrániče. Nejdřív se ujistěte, jestli hrajete ledový, nebo inline hokej, výbava se liší.</p>'
          '<h3>Brusle</h3>'
          '<p>Hokejové brusle se kupují o půl až celou velikost menší než běžná obuv. Patu mají držet pevně, prsty se jen lehce dotýkat špičky. Při výběru zkontrolujte šířku (D standardní, EE široká) a tuhost boty.</p>'
          '<h3>Hokejka</h3>'
          '<p>Správná délka sahá po nasazení bruslí k bradě, bez bruslí do úrovně nosu. Důležitý je flex, tedy ohebnost. Přibližně se řídí vzorcem hmotnost hráče děleno dvěma. Kompozitové hokejky jsou lehčí a dražší, dřevěné odolnější a vhodné pro začátky. Více o nich v kategorii <a href="/hokejky/">hokejky</a> a <a href="/hokejove-cepele-a-nasady/">hokejové čepele a nástavce</a>.</p>'
          '<h3>Chrániče a helma</h3>'
          '<ul><li><strong>Helma s mřížkou:</strong> základ ochrany, hledejte certifikaci HECC.</li>'
          '<li><strong>Chrániče loktů a ramen:</strong> sedí těsně, nesmí omezovat pohyb.</li>'
          '<li><strong>Rukavice a kalhoty:</strong> chrání prsty a boky, kontrolujte délku podle výšky.</li>'
          '<li><strong>Chrániče holení a suspenzor:</strong> doplňují výbavu, pravidla se liší podle soutěže a věku.</li></ul>'
          '<h3>Oblečení a brašna</h3>'
          '<p>Pod chrániče patří funkční spodní prádlo a dres. Výbavu pohodlně převezete v <a href="/hokejove-tasky/">hokejové tašce</a> s kolečky a ventilací. Fanoušci najdou dresy v kategorii <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>.</p>'
          '<h3>Děti a růst</h3>'
          '<p>Dětské brusle s nastavitelnou velikostí vydrží i několik sezón. U chráničů a helmy je lepší nešetřit a kupovat podle velikosti, ne s rezervou, protože volné chrániče neochrání.</p>',
    faq=[('Co potřebuji na začátek s hokejem?', 'Brusle, helmu s mřížkou, rukavice, chrániče loktů a ramen, hokejové kalhoty a hokejku. Většinu nabízí začátečnické sady.'),
         ('Jak vybrat velikost hokejových bruslí?', 'O půl až celou velikost menší než běžné boty. Pata drží pevně, prsty se jen lehce dotýkají špičky.'),
         ('Jak dlouhá má být hokejka?', 'S bruslemi po bradu, bez nich k nosu. Při váhání raději kratší, usnadní vedení pukem.'),
         ('Jaký flex hokejky zvolit?', 'Přibližně polovina tělesné hmotnosti hráče. Děti volí nižší flex, dospělí podle síly a stylu hry.'),
         ('Jaké chrániče jsou povinné?', 'Pravidla se liší podle soutěže a věku hráče. Helma s mřížkou je základ všude, ostatní chrániče určuje řád soutěže, doporučují se i na trénincích.'),
         ('Kde sehnat hokejovou výbavu pro děti?', 'V kategorii najdete juniorské a dětské velikosti. Filtr značky a velikosti zúží výběr, porovnání cen vám ukáže obchod s nejnižší nabídkou.')],
)

NEW['hokejky'] = dict(short=True,
    title='Hokejky – kompozitové, dřevěné, dětské | Porovnání cen',
    desc='Hokejky kompozitové i dřevěné pro dospělé, juniory a děti. Porovnejte ceny, flex a zahnutí čepele v českých sportovních obchodech.',
    intro='<p><strong>Hokejka</strong> je osobní nástroj hráče, proto se vybírá podle délky, ohebnosti (flexu) a zahnutí čepele. Kompozitová hokejka je lehká a odpružená, dřevěná levnější a odolná. '
          'Pro děti a začátečníky stačí dřevěná nebo základní kompozit, ambiciózní hráči sahají po vyšších řadách.</p>'
          '<p>Na Sportece porovnáte ceny hokejek z českých obchodů a vyberete podle značky, levé nebo pravé ruky a velikosti. K hokejce patří <a href="/hokejove-cepele-a-nasady/">čepele a nástavce</a>, <a href="/hokejove-pasky-a-doplnky/">pásky a doplňky</a> a '
          '<a href="/hokejove-puky-a-branky/">puky a branky</a>. Další vybavení najdete v hlavní kategorii <a href="/hokej/">hokej</a>.</p>',
    guide='<h2>Jak vybrat hokejku</h2>'
          '<p>Správná hokejka vám usnadní střelbu i vedení pukem. Špatná délka nebo tuhost naopak zhorší techniku a unaví ruce. Při výběru sledujte čtyři věci.</p>'
          '<h3>Délka</h3>'
          '<p>S nasazenými bruslemi má hůl končit někde mezi bradou a rty, bez bruslí u nosu. Kratší hokejka lépe vede puk, delší dává dosah a páku při střelbě. Dětem nikdy neberte hokejku „na vyrůstání“.</p>'
          '<h3>Flex (tuhost)</h3>'
          '<p>Flex udává, kolik kilogramů je potřeba k ohnutí hole o 1 palec. Obecně se volí zhruba polovina vlastní váhy. Nižší flex je pro děti a lehčí hráče, vyšší pro silnější střelce.</p>'
          + T(['Kategorie', 'Orientační flex'], [['Děti (Youth)', '20–40'], ['Junior', '40–60'], ['Intermediate', '55–70'], ['Senior', '70–110']]) +
          '<h3>Zahnutí čepele (patterns)</h3>'
          '<p>Zahnutí čepele ovlivňuje, jak puk vedete a střílíte. Běžné jsou P92, P28 a P88. Pro začátečníky je nejlepší střední zahnutí, které se hodí do všech situací. Čepel je levá nebo pravá podle toho, kterou rukou držíte hůl níže.</p>'
          '<h3>Materiál a hmotnost</h3>'
          '<ul><li><strong>Dřevo:</strong> levné a odolné, těžší, hodí se do začátků a na trénink.</li>'
          '<li><strong>Kompozit (karbon):</strong> lehký a reaktivní, dražší a citlivější na zlomení.</li>'
          '<li><strong>Jednodílný, nebo dvoudílný:</strong> u dvoudílné se čepel dá vyměnit.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Hokejku po tréninku osušte a ošetřete páskou na čepeli. Kompozit neponechávejte v mrazivém autě ani na slunci, extrémní teploty ho oslabují.</p>',
    faq=[('Jak dlouhá má být hokejka?', 'S bruslemi po bradu, bez nich k nosu. Kratší hůl lépe vede puk, delší dává dosah.'),
         ('Co znamená flex hokejky?', 'Tuhost, tedy síla v kilogramech potřebná k ohnutí hole o jeden palec. Volí se zhruba polovina tělesné hmotnosti.'),
         ('Levá, nebo pravá hokejka?', 'Podle toho, kterou rukou držíte hůl níže. Levák vede hokejku levou rukou dole, to je levá hokejka.'),
         ('Dřevěná, nebo kompozitová hokejka?', 'Dřevěná je levnější a odolnější, kompozit lehčí a výbušnější při střelbě. Začátečníkům stačí dřevo nebo základní kompozit.'),
         ('Jak často měnit čepel?', 'Podle opotřebení, u dvoudílných hokejek stačí vyměnit čepel, nástavec zůstane. Ošetřujte ji páskou.'),
         ('Jaká hokejka pro dítě?', 'Dětská hokejka s nízkým flexem a správnou délkou. Dřevěné modely jsou levné a odolné proti pádům.')],
)

NEW['kolobezky'] = dict(short=True,
    title='Koloběžky – dětské, městské, freestyle | Porovnání cen',
    desc='Koloběžky pro děti i dospělé: městské, skládací, freestyle a elektrické. Porovnejte ceny, velikosti kol a nosnost v českých obchodech.',
    intro='<p><strong>Koloběžka</strong> je jednoduchý dopravní prostředek pro děti i dospělé. Dětské modely mají tři kola a nízkou plošinu, městské modely velká kola a brzdu a '
          '<a href="/freestyle-kolobezky/">freestyle koloběžky</a> jsou stavěné na triky v parku. Pokud chcete jezdit bez odrážení, podívejte se na <a href="/elektrokolobezky/">elektrokoloběžky</a>.</p>'
          '<p>Na Sportece porovnáte ceny koloběžek z českých obchodů a vyberete podle velikosti kol, nosnosti a značky. K bezpečné jízdě patří <a href="/chranice-a-helmy/">chrániče a helmy</a>, pro dopravu na delší vzdálenost zase <a href="/inline-brusle/">inline brusle</a>.</p>',
    guide='<h2>Jak vybrat koloběžku</h2>'
          '<p>Koloběžka se vybírá podle věku, výšky jezdce a místa, kde se bude jezdit. Zeptejte se tedy, kdo na ní bude jezdit a po jakém povrchu.</p>'
          '<h3>Typy koloběžek</h3>'
          '<ul><li><strong>Dětské tříkolky:</strong> od zhruba 2 let, stabilní a s nízkou plošinou.</li>'
          '<li><strong>Dvoukolky pro děti:</strong> od 4–5 let, s brzdou na zadním blatníku.</li>'
          '<li><strong>Městské a skládací:</strong> velká kola 200 mm a více, hodí se do města a do MHD.</li>'
          '<li><strong>Freestyle:</strong> pevná ocel nebo hliník, malá kola, bez skládání.</li>'
          '<li><strong>Terénní:</strong> nafukovací kola, vhodná pro lesní a polní cesty.</li></ul>'
          '<h3>Velikost kol</h3>'
          '<p>Větší kola překonají nerovnosti snáz. Pro město jsou ideální kola 200 mm, pro delší trasy a hrubší povrch 230 mm a víc. Malá kola 100–125 mm jsou na hladký povrch a triky.</p>'
          '<h3>Řídítka a nosnost</h3>'
          '<p>Výška řídítek se nastavuje tak, aby se jezdec mohl pohodlně držet bez hrbení. Zkontrolujte maximální nosnost v popisu, běžně 100 až 120 kg u dospělých modelů.</p>'
          '<h3>Brzdy a bezpečnost</h3>'
          '<p>Základem je zadní brzda na blatník, lepší koloběžky mají kotoučovou nebo ráfkovou. Pro děti vždy používejte helmu, chrániče kolen a loktů. Pro večerní jízdu přidejte světlo a odrazky.</p>'
          '<h3>Skládání a převoz</h3>'
          '<p>Skládací model se vejde do kufru i do kanceláře. Kontrolujte hmotnost, 6 až 8 kg se ještě dobře nese. Pevný zámek konstrukce při skládání je důležitý pro bezpečnost.</p>',
    faq=[('Jakou koloběžku pro dítě ve 3 letech?', 'Tříkolku s nízkou plošinou a širokým postojem. Pro stabilitu volte model s naklápěcím řízením.'),
         ('Jak velká kola má mít městská koloběžka?', 'Nejlépe 200 mm a víc. Větší kola lépe zvládají obrubníky a nerovný povrch.'),
         ('Hodí se koloběžka do MHD?', 'Ano, skládací modely s hmotností do 8 kg se vejdou do tramvaje i metra. Zkontrolujte pravidla dopravce.'),
         ('Jakou nosnost má mít koloběžka pro dospělého?', 'Alespoň 100 kg, lepší 120 kg. Zahrňte i váhu batohu.'),
         ('Je potřeba helma na koloběžku?', 'Ano, pro děti je povinná, pro dospělé silně doporučená. Doplňte ji chrániči kolen a loktů.'),
         ('Čím se liší freestyle koloběžka?', 'Má pevnou konstrukci, malá kola a ocelovou nebo hliníkovou konstrukci, bez skládání. Je určená na skatepark a triky.')],
)

NEW['elektrokolobezky'] = dict(short=True,
    title='Elektrokoloběžky – výkon, dojezd, ceny | Sporteka',
    desc='Elektrokoloběžky pro město: výkon motoru, dojezd, nosnost a brzdy. Porovnejte ceny a dostupnost modelů v českých obchodech.',
    intro='<p><strong>Elektrokoloběžka</strong> nahrazuje auto i MHD na krátkých trasách po městě. Rozhodují tři parametry: <strong>dojezd na baterii</strong>, výkon motoru a hmotnost. '
          'Lehčí modely do 15 kg se dobře nosí, výkonnější s větší baterií zvládnou stoupání i delší cesty. U nás se elektrokoloběžka s výkonem do 1000 W a rychlostí do 25 km/h řadí mezi malé elektrické dopravní prostředky podobně jako kolo.</p>'
          '<p>Na Sportece porovnáte ceny a vybavení z českých obchodů a přehled zúžíte podle značky a ceny. Chcete-li jet bez baterie, vyberte klasickou <a href="/kolobezky/">koloběžku</a>, pro bezpečí patří ke každé jízdě <a href="/chranice-a-helmy/">chrániče a helma</a>.</p>',
    guide='<h2>Jak vybrat elektrokoloběžku</h2>'
          '<p>Při výběru netlačte jen na cenu. Slabá baterie nebo malé kolo se projeví až po několika týdnech používání, a to není příjemné.</p>'
          '<h3>Dojezd a baterie</h3>'
          '<p>Deklarovaný dojezd výrobce měří za ideálních podmínek. V praxi počítejte zhruba o třetinu méně, hlavně při jízdě do kopce, v zimě a s těžším jezdcem. Pro denní dojíždění zvolte baterii s rezervou.</p>'
          + T(['Trasa za den', 'Doporučený dojezd podle výrobce'], [['do 10 km', '20–25 km'], ['10–20 km', '35–45 km'], ['více než 20 km', '50 km a víc']]) +
          '<h3>Výkon motoru a stoupání</h3>'
          '<p>Motory 250–350 W stačí do rovinatého města. Do kopců potřebujete 500 W a víc. Vyšší výkon znamená větší spotřebu a vyšší cenu.</p>'
          '<h3>Kola a odpružení</h3>'
          '<ul><li><strong>Pevné pneumatiky:</strong> bez defektů, ale tvrdší jízda.</li>'
          '<li><strong>Nafukovací pneumatiky:</strong> pohodlné, ale mohou se píchnout.</li>'
          '<li><strong>Odpružení:</strong> tlumí nerovnosti, hodí se na dlážděné ulice.</li></ul>'
          '<h3>Brzdy a bezpečnost</h3>'
          '<p>Kotoučové brzdy brzdí spolehlivěji než elektronická brzda sama. Zkontrolujte světla vpředu a vzadu a stupnici osvětlení, bez nich jezdit po setmění nelze. K výbavě patří helma a při rychlé jízdě i chrániče.</p>'
          '<h3>Zákon a pojištění</h3>'
          '<p>Elektrokoloběžka s maximální rychlostí 25 km/h a výkonem do 1000 W jezdí podle pravidel pro cyklisty, na chodníku se pouze tlačí. Aktuální pravidla ověřte u dopravního úřadu, mění se. Pojištění odpovědnosti se vyplatí.</p>'
          '<h3>Údržba</h3>'
          '<p>Baterii nenechávejte vybitou ani zcela nabitou po dlouhou dobu, ideálně držte mezi 20 a 80 %. V zimě ji skladujte v teple a pneumatiky kontrolujte před každou jízdou.</p>',
    faq=[('Jaký dojezd má mít elektrokoloběžka?', 'Pro město 25 až 40 km podle výrobce. V praxi počítejte zhruba s dvěma třetinami uvedeného dojezdu.'),
         ('Jaký výkon motoru zvolit?', 'Na rovinu 250–350 W, do kopců 500 W a víc. Pamatujte, že vyšší výkon znamená rychlejší vybíjení baterie.'),
         ('Smí se na elektrokoloběžce jezdit po chodníku?', 'Ne, po chodníku se pouze tlačí. Jezdí se po silnici nebo cyklostezce, rychlost do 25 km/h.'),
         ('Potřebuji helmu na elektrokoloběžku?', 'Pro děti je povinná, pro dospělé silně doporučená. Doplňte ji světly a odrazkami.'),
         ('Jak pečovat o baterii?', 'Nabíjejte před kompletním vybitím, skladujte v suchu a v teple. Při dlouhodobém skladování držte nabití zhruba na 50 %.'),
         ('Je lepší pevná, nebo nafukovací pneumatika?', 'Pevná se nepropíchne, ale tlumí hůř. Nafukovací je pohodlnější, vyžaduje kontrolu tlaku a opravu při defektu.')],
)
