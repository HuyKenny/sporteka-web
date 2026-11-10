"""sporteka.cz — wave 22h (4. 11. 2026): long texts (>= 1650 words) for powerbanky-a-nabijeni, cyklisticke-ponozky, obleceni-bojove-sporty, iontove-napoje.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ powerbanky-a-nabijeni
NEW['powerbanky-a-nabijeni'] = dict(long=True,
    title='Powerbanky a nabíjení: kapacita, výkon, solár, stanice',
    desc='Powerbanky, solární nabíječky a nabíjecí stanice pro výlety, kolo i kemp. Jak číst mAh a watty a porovnat nabídky českých obchodů.',
    intro='<p>Powerbanka je dnes stejně samozřejmá součást výbavy jako lahev s pitím. Telefon s mapou, hodinky, čelovka i světlo na kolo jedou na baterie, a pokud se vybijí uprostřed trasy, výlet se rázem komplikuje. V téhle kategorii proto nenajdete jen klasické externí baterie do kapsy, ale i solární nabíječky, nabíjecí stanice na kemp, nabíjecí AA a AAA baterie a překvapivě také svítilny nebo světla na kolo, které umějí nabíjet jiná zařízení.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u značek jako '
          + B(('baseus', 'Baseus'), ('viking', 'Viking'), ('vayox', 'Vayox'), ('bluetti', 'Bluetti'), ('rockbros', 'Rockbros'), ('nitecore', 'Nitecore'), ('anker', 'Anker'), ('xiaomi', 'Xiaomi')) +
          '. K nabíjení se vážou i <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, <a href="/cyklo-svetla/">cyklosvětla</a>, <a href="/sportovni-hodinky/">sportovní hodinky</a> a <a href="/kemping/">kempingové</a> vybavení.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Název „powerbanky a nabíjení“ zahrnuje několik zařízení, která řeší stejný problém jiným způsobem. Než začnete porovnávat nabídky, určete si, co budete nabíjet, kde a jak dlouho bez zásuvky vydržíte.</p>'
          + T(['Typ', 'Pro koho', 'Na co si dát pozor'], [
              ['Kapesní powerbanka', 'telefon, hodinky, sluchátka na denní výlet', 'kapacita, váha a typ konektoru'],
              ['Powerbanka s vyšším výkonem', 'tablet, notebook, několik zařízení najednou', 'podpora rychlého nabíjení a výstupní watty'],
              ['Outdoorová odolná powerbanka', 'túry, kolo, déšť a prach', 'krytí proti vodě a nárazům, odolný povrch'],
              ['Solární nabíječka', 'vícedenní trek bez zásuvky', 'rozměr panelu a závislost na slunci'],
              ['Nabíjecí stanice', 'kemp, karavan, chata, výpadek proudu', 'váha, výstupy do zásuvky a možnost solárního dobíjení'],
              ['Nabíjecí AA a AAA články', 'čelovky, GPS, bezdrátové doplňky', 'kompatibilita nabíječky a typ článku'],
              ['Svítilna nebo světlo s funkcí powerbanky', 'kolo, kemp, nouzové osvětlení', 'dvojí využití, ale menší kapacita než samostatná baterie']]) +
          '<p>V kategorii najdete i příslušenství. Patří sem brašny na rám kola určené pro powerbanku, ochranná pouzdra a nabíječky pro speciální nabíjecí baterie. U těchto produktů hlídejte, jestli jsou určené pro váš konkrétní typ baterie.</p>'
          '<h2>Jak číst mAh, Wh a watty</h2>'
          '<p>Na obalu bývá hlavní číslo kapacita v miliampérhodinách (mAh). Je to hrubá informace o tom, kolik náboje baterie uchová. Skutečně využitelná energie je vždy nižší, protože se část ztratí při převodu napětí a v elektronice. Počítejte proto s tím, že dostanete znatelně méně, než naznačuje číslo na obalu. Přesná ztráta se u různých modelů liší.</p>'
          '<p>Pro srovnání většího zařízení se hodí údaj ve watthodinách (Wh), protože zohledňuje i napětí. U nabíjecích stanic je to hlavní údaj. Wh získáte přibližně vynásobením mAh a jmenovitého napětí článku a vydělením tisícem. Výrobce často uvede obě hodnoty.</p>'
          '<p>Druhým důležitým číslem je <strong>výstupní výkon ve wattech</strong>. Telefonu stačí desítky wattů, tablet nebo notebook potřebuje víc. Powerbanka s nízkým výkonem sice dobije telefon, ale notebook nabíjet nebude, případně jen velmi pomalu. Zkontrolujte také, co zvládá <em>vstup</em>: baterie, která se dlouho dobíjí, vás na cestě zdrží.</p>'
          '<h2>Konektory a rychlé nabíjení</h2>'
          '<p>Dnes převládá USB-C, který slouží jako vstup i výstup. Starší typy mají USB-A a micro USB. Pro nabíjení moderních telefonů se hodí powerbanka s USB-C a podporou standardu Power Delivery nebo podobného rychlého protokolu. Telefon i kabel musí dané nabíjení podporovat, jinak se zařízení domluví na pomalejším režimu.</p>'
          '<ul><li><strong>Kabel:</strong> tenký a levný kabel může limitovat výkon. Pro vyšší watty použijte kabel určený pro vyšší proud.</li>'
          '<li><strong>Více portů:</strong> při současném nabíjení se výkon mezi porty obvykle dělí.</li>'
          '<li><strong>Průchozí nabíjení:</strong> některé modely umějí nabíjet zařízení, zatímco se samy dobíjejí. Funkce není u všech stejně spolehlivá.</li>'
          '<li><strong>Zabudovaný kabel:</strong> pohodlný, ale když se poškodí, může být celá powerbanka k ničemu.</li></ul>'
          '<h2>Jakou kapacitu zvolit podle aktivity</h2>'
          '<p>Nekupujte největší baterii jen proto, že je největší. Váží víc, déle se nabíjí a při cestování letadlem platí limity pro přepravu lithiových baterií. Aktuální pravidla si vždy ověřte u dopravce.</p>'
          '<ul><li><strong>Denní výlet a běh:</strong> malá powerbanka stačí na jedno nebo dvě dobití telefonu. Pokud používáte <a href="/sportovni-hodinky/">sportovní hodinky</a>, dobijete je s ní také.</li>'
          '<li><strong>Víkend na túře:</strong> střední kapacita, ideálně odolné provedení. K navigaci, fotkám a čelovce se hodí rezerva. Čelovky vybírejte v sekci <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</li>'
          '<li><strong>Cyklistika:</strong> baterie do brašny na rám nebo světla s funkcí powerbanky. Světlo, <a href="/cyklo-computery/">cyklocomputer</a> i telefon mohou čerpat z jednoho zdroje.</li>'
          '<li><strong>Kemp nebo karavan:</strong> nabíjecí stanice pokryje notebook, ventilátor i menší spotřebiče. Přehled vybavení najdete v kategorii <a href="/kemping/">kemping</a>.</li></ul>'
          '<h2>Solární nabíječky: realistická očekávání</h2>'
          '<p>Solární panel dobíjí jen při dostatku přímého světla. V zataženém počasí, v lese nebo u malého panelu bývá výkon velmi nízký. Rozkládací panel proto ocení hlavně ten, kdo je několik dní venku a mimo sítě, a nejlépe ho kombinuje s powerbankou. Panel nabíjí baterii přes den a telefon se nabíjí z ní večer, ne přímo ze slunce. Na batohu viset může, ale v pohybu často zakrývá část panelu, takže výkon kolísá.</p>'
          '<p>Větší stanice mívají solární vstup, ale stejně platí, že kapacita se doplní pomalu. Použijte je jako doplněk, ne jako jediný zdroj energie na delší cestu.</p>'
          '<h2>Nabíjecí stanice pro kemp a nouzové situace</h2>'
          '<p>Přenosné stanice se podobají velké powerbance se zásuvkou na 230 V. Zvládnou běžný notebook, ventilátor, malý ohřívač vody nebo světla, ale topidla, varné konvice a jiné výkonné spotřebiče jsou limitované maximálním výkonem měniče. Před koupí sečtěte příkon zařízení, která chcete připojit, a nechte si rezervu. Doba provozu závisí na kapacitě ve Wh a na tom, kolik zařízení současně připojíte.</p>'
          '<p>Stanice jsou těžké a pro přenos pěšky nevhodné. Hodí se do auta, k chatě a do stanu u kempu, kde nejsou přípojky. Ke kempování se hodí i <a href="/chladici-boxy/">chladicí boxy</a> a <a href="/stany/">stany</a>. Značky jako Bluetti a Anker mají v nabídce Sporteky právě stanice a jejich kity se solárním panelem.</p>'
          '<h2>Nabíjecí AA a AAA baterie</h2>'
          '<p>Nabíjecí články v USB-C provedení, které se dobíjejí přímo kabelem, jsou praktické pro čelovky, GPS a bezdrátové doplňky. Ověřte, že baterie odpovídá přístroji. Některé články mají jiné napětí než jednorázové alkalické, a ne každé zařízení to snese. Informace najdete v návodu k přístroji.</p>'
          '<h2>Péče o baterii a bezpečnost</h2>'
          '<p>Lithiové články nemají rády extrémy. Nenechávejte powerbanku v rozpáleném autě na slunci a v mrazu ji noste blízko těla, aby zůstala v teple. V zimě kapacita klesá, protože chemická reakce v článku zpomaluje. Pokud baterii delší dobu nepoužíváte, uložte ji částečně nabitou a občas ji zkontrolujte.</p>'
          '<ul><li>Poškozenou, nafouklou nebo opravovanou powerbanku přestaňte používat.</li>'
          '<li>Při nabíjení ji nepřikrývejte a nenechávejte bez dozoru na hořlavém povrchu.</li>'
          '<li>Používejte kvalitní kabely a nabíječky, které odpovídají parametrům zařízení.</li>'
          '<li>Vysloužilé baterie odevzdejte do sběrného místa, nepatří do běžného odpadu.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Porovnávání jen podle mAh bez ohledu na výstupní výkon a podporu rychlého nabíjení.</li>'
          '<li>Očekávání, že 10 000 mAh dobije telefon s baterií 5 000 mAh přesně dvakrát.</li>'
          '<li>Koupě malého solárního panelu s přesvědčením, že nahradí zásuvku.</li>'
          '<li>Ignorování krytí: pro kolo a túry se vyplatí odolnější provedení.</li>'
          '<li>Nakupování podle ceny bez ověření, že baterie nese označení shody a pochází od ověřeného výrobce.</li></ul>'
          '<h2>Powerbanka na kolo a na běh</h2>'
          '<p>Na kole je největší problém uložení. Powerbanka v zadní kapse dresu je pohodlná, ale při pádu nebo v dešti ji nic nechrání. Brašna na rám kola s oddělenou kapsou, kterou najdete mezi <a href="/cyklo-tasky-a-nosice/">brašnami a nosiči</a>, drží baterii blízko těžiště a kabel vede k přednímu světlu nebo cyklocomputeru. Pokud jezdíte dlouhé etapy, zkontrolujte, že konektor v brašně nepřekáží stehnu ani kolenu.</p>'
          '<p>Běžci mají nejraději malé a ploché baterie do opasku nebo vesty. Hodí se pro ně <a href="/bezecke-opasky/">běžecké opasky</a> a <a href="/bezecke-vesty-a-batohy/">běžecké vesty</a>, kam se vejde i telefon. Na kratší tréninky powerbanku většinou vůbec nebrat, vyplatí se až na ultra tratích a při dlouhém používání navigace.</p>'
          '<h2>Nabíjení v terénu: praktické tipy</h2>'
          '<ul><li>Zapněte v telefonu úsporný režim a vypněte nepotřebné služby, jako je neustálé hledání sítě, a baterie vydrží výrazně déle.</li>'
          '<li>Zimní navigaci na hodinkách nebo telefonu si zkuste předem a ověřte, jak dlouho vám baterie vydrží při nízké teplotě.</li>'
          '<li>Před vícedenní cestou plně nabijte powerbanku i všechna zařízení. Teprve po vyčerpání prvního zdroje sáhněte po druhém.</li>'
          '<li>Kabely uložte do malého pouzdra, aby se nezamotaly a konektory nenasbíraly prach a vlhkost.</li>'
          '<li>Na společných túrách se dohodněte, kdo veze společnou baterii, ať se zbytečně nenosí několik stejných.</li></ul>'
          '<h2>Pro koho jednotlivé typy jsou</h2>'
          '<p>Začátečník na víkendových výletech spokojeně vystačí s jednou střední powerbankou a dobrým kabelem. Kolo a bikepacking vyžadují odolnější provedení, případně světlo s vestavěnou baterií. Rodina v kempu ocení nabíjecí stanici, kterou nabíjí tablety dětem, čelovky i malý ventilátor. Fotograf a kameraman s dronem nebo kamerou potřebuje baterii s vyšším výkonem a více porty. A kdo se bojí výpadku proudu doma, může stanici držet jako nouzovou zálohu pro světlo a router.</p>'
          '<h2>Jak porovnávat na Sportece</h2>'
          '<p>Stejný model bývá v různých obchodech za různé ceny a s různým termínem dodání. U každého produktu vidíte nabídky a dostupnost, takže snadno najdete obchod, který má baterii skladem. Dívejte se na kapacitu, konektory a údaj o výkonu v popisu produktu, ne jen na název. U <a href="/outdoor/">outdoorových</a> doplňků je důležité i krytí a materiál. Pokud shánite komplet na delší výlet, pokračujte do <a href="/batohy/">batohů</a>, <a href="/outdoor-doplnky/">outdoorových doplňků</a> a <a href="/celovky-a-svitilny/">svítilen</a>.</p>',
    faq=[
        ('Jakou kapacitu powerbanky potřebuji na telefon?', 'Pro jedno až dvě dobití běžného telefonu na denní výlet stačí střední kapacita. Pamatujte, že využitelná energie je kvůli ztrátám nižší než číslo na obalu. Pokud máte starší telefon se slabší baterií, vystačíte i s menší powerbankou.'),
        ('Je lepší USB-C, nebo starší USB-A?', 'USB-C je univerzálnější, protože slouží jako vstup i výstup a podporuje rychlé nabíjení. USB-A se hodí pro starší kabely a doplňky. Praktická powerbanka má obojí.'),
        ('Mohu powerbanku vzít do letadla?', 'Obvykle ano, ale do příručního zavazadla, ne do odbaveného. Limity kapacity určují dopravci a předpisy, proto si je před cestou ověřte u své letecké společnosti.'),
        ('Proč se powerbanka v zimě rychleji vybíjí?', 'V chladu zpomaluje chemická reakce v lithiovém článku, a baterie proto dodá méně energie. Pomůže uložit ji do vnitřní kapsy blízko těla a používat ji až po zahřátí.'),
        ('Pomůže mi solární nabíječka na vícedenní túře?', 'Může pomoct, pokud je dost přímého slunce a panel je dostatečně velký. V lese, za mraků a při chůzi bývá výkon nízký. Rozumná kombinace je panel plus powerbanka, která se nabíjí přes den.'),
        ('Co je to nabíjecí stanice a komu se hodí?', 'Je to velká přenosná baterie se zásuvkou na 230 V. Hodí se do kempu, na chatu, do karavanu nebo jako záloha při výpadku proudu. Pro pěší trek je příliš těžká.'),
        ('Jak poznám, že kabel zvládne rychlé nabíjení?', 'Podívejte se do popisu kabelu, kde výrobce uvádí podporovaný výkon. Tenké kabely bez označení bývají omezené. Pokud nabíjení trvá nečekaně dlouho, vyměňte kabel jako první.'),
        ('Dá se svítilna nebo světlo na kolo použít jako powerbanka?', 'Některé modely tuto funkci mají a mohou nouzově dobít telefon. Jejich kapacita ale bývá menší než u samostatné powerbanky, takže je berte jako doplněk.'),
        ('Jak dlouho powerbanka vydrží?', 'Záleží na kvalitě článků a způsobu používání. Hluboké vybíjení, horko a časté nabíjení vysokým výkonem životnost zkracují. Šetrné zacházení ji prodlouží, ale po letech používání kapacita přirozeně klesne.'),
        ('Můžu nabíjet notebook powerbankou?', 'Ano, pokud powerbanka dodá dostatečný výstupní výkon přes USB-C a notebook tento způsob nabíjení podporuje. Pro slabší modely poběží notebook spíš pomalu nebo se jen udrží. Ověřte si výkon v návodu obou zařízení.'),
    ])

# ------------------------------------------------------------------ cyklisticke-ponozky
NEW['cyklisticke-ponozky'] = dict(long=True,
    title='Cyklistické ponožky: letní, zimní, merino, MTB a silnice',
    desc='Cyklistické ponožky pro silnici, MTB i zimu: délka, materiál, merino a velikosti. Jak vybrat a porovnat nabídky českých obchodů.',
    intro='<p>Ponožky patří k věcem, kterých si cyklista všimne až ve chvíli, kdy nesedí. Pár hodin na kole znamená tisíce otáček pedálů, a pokud ponožka sklouzává, vlhne nebo tlačí ve švu, vzniknou puchýře a pocit nepohodlí, který vám zkazí jízdu. Správný pár přitom stojí jen zlomek vybavení a rozdíl poznáte hned při první delší vyjížďce. Cyklistické ponožky proto bývají tenčí, pružnější a lépe odvádějí pot než běžné bavlněné.</p>'
          '<p>Na Sportece najdete letní, zimní, merino i kompresní modely pro silnici, MTB a gravel, od značek '
          + B(('r2', 'R2'), ('siroko', 'Siroko'), ('eleven', 'Eleven'), ('rockbros', 'Rockbros'), ('silvini', 'Silvini'), ('ale-cycling', 'Alé Cycling'), ('northwave', 'Northwave'), ('van-rysel', 'VAN Rysel')) +
          '. Doplňují je <a href="/cyklisticka-obuv/">cyklistická obuv</a>, <a href="/cyklisticke-navleky/">návleky</a>, <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy</a> a <a href="/cyklisticke-dresy/">dresy</a>.</p>',
    guide='<h2>Proč speciální ponožky na kolo</h2>'
          '<p>Chodidlo v cyklistické botě je během jízdy stlačené a pracuje jen ve velmi omezeném rozsahu. Nepotřebuje tlumení jako při běhu, ale bezvadné odvádění vlhkosti, hladké švy a stabilní přilnutí k noze. Silnější froté ponožka, která se hodí do turistických bot, se v tuhé cyklistické botě stává problémem, protože zvětšuje objem uvnitř a tlačí na nárt.</p>'
          '<p>Cyklistické modely se proto vyrábějí ze syntetických vláken, merina nebo jejich směsi, mají zesílení tam, kde ho potřebujete, a prodyšnou síťku nad nártem. Často nabízejí i podporu klenby a pružné pásky, které drží ponožku na místě.</p>'
          '<h2>Délka ponožky</h2>'
          + T(['Délka', 'Výška', 'Hodí se pro'], [
              ['Nízká a kotníková', 'těsně nad kotník', 'horké dny, krátké vyjížďky, módní preference'],
              ['Střední', 'zhruba do poloviny lýtka', 'klasika pro silnici a MTB'],
              ['Vysoká', 'nad střed lýtka', 'chlad, ochrana před trním, aerodynamický look'],
              ['Zimní', 'vysoká s nadstandardní izolací', 'jízda při nízkých teplotách']]) +
          '<p>Pravidlo o výšce ponožky se ve světě silničářů a MTB bikerů často liší. Silničáři preferují vyšší vzhled, bikeři zase střední nebo delší, které chrání před větvemi a blátem. Nejdůležitější je komfort, ne tradice.</p>'
          '<h2>Materiál: merino, syntetika, bambus</h2>'
          '<p>Materiál rozhoduje o pocení, zápachu a rychlosti schnutí. Žádný není univerzálně nejlepší.</p>'
          '<ul><li><strong>Syntetika (polyamid, polyester, elastan):</strong> rychle schne, je odolná a levnější. Dobře drží tvar. Při dlouhém používání se může hůř vypořádat se zápachem.</li>'
          '<li><strong>Merino vlna:</strong> reguluje teplotu, v chladu hřeje i když je vlhká a méně zapáchá. Bývá dražší a při intenzivním používání ve vysokém počtu pracích cyklů se může dříve prodřít v místech tření. Vlnu můžete prát podle návodu na etiketě. Další modely najdete také v kategorii <a href="/merino-ponozky/">merino ponožky</a>.</li>'
          '<li><strong>Bambusová a směsová vlákna:</strong> měkká na dotyk, často se míchají se syntetikou. U delších jízd v horku mohou vlhnout déle než čistá syntetika.</li>'
          '<li><strong>Bavlna:</strong> na kolo se nehodí, protože nasákne potem a dlouho zůstává mokrá.</li></ul>'
          '<h2>Letní, přechodové a zimní ponožky</h2>'
          '<p>V létě chcete co nejtenčí model s prodyšnou síťkou. Na jaře a na podzim se hodí o něco silnější materiál, případně kombinace s <a href="/cyklisticke-navleky/">návleky na nohy</a>. V zimě jde o dvě věci současně: izolaci a prostor. Příliš silná ponožka ve stejné botě stlačí chodidlo, zhorší prokrvení a nohy budou paradoxně studit víc. Raději zvolte vyšší velikost boty nebo kombinujte tenčí zimní ponožku s <a href="/cyklisticka-obuv/">návleky na boty</a> či zimní botou.</p>'
          '<p>Při mokrém počasí pomáhají ponožky s membránou, ale zároveň se hůř prodýchávají. Nejspolehlivější je při pauze vyměnit mokrý pár za suchý.</p>'
          '<h2>Kompresní a aerodynamické modely</h2>'
          '<p>Kompresní ponožky stahují lýtko a výrobci je často doporučují pro delší jízdy a cestování. Vliv na výkon a regeneraci je individuální a nemá smysl jim přisuzovat zázraky. Pokud vám pocit sevření vyhovuje, mohou být příjemnou volbou, jinak je vynechte. Aero ponožky se jemným texturovaným povrchem používají zejména v závodech a časovkách. Pro rekreační jízdu rozhodně nejsou nutností.</p>'
          '<h2>MTB, gravel a silnice</h2>'
          '<ul><li><strong>Silnice:</strong> tenká, lehká ponožka s dobrou ventilací, často střední až vyšší délky. Jízda v tuhých botách s karbonovou podrážkou vyžaduje hladký střih bez tlakových míst.</li>'
          '<li><strong>MTB:</strong> o něco odolnější materiál, zesílená pata a špička a delší manžeta. Nohy tu bývají víc vystavené blátu, vodě a drobným nárazům.</li>'
          '<li><strong>Gravel a trekking:</strong> univerzální střední ponožka s kombinací odolnosti a prodyšnosti. Na dlouhé cesty se osvědčuje merino.</li>'
          '<li><strong>Městská jízda a e-bike:</strong> v obyčejných botách stačí kterákoli sportovní ponožka. Specializace tu nehraje velkou roli.</li></ul>'
          '<h2>Velikost a střih</h2>'
          '<p>Výrobci uvádějí velikosti většinou v rozmezích, například 39–42. Pokud jste na hranici dvou velikostí, zvolte podle toho, jak sedí v botě. Ponožka, která je příliš velká, vytváří záhyby a tlak, příliš malá se naopak stahuje a sklouzává. U dětí a dospívajících počítejte s rychlým růstem nohy.</p>'
          '<p>Kvalitní ponožka sedí bez záhybů a prstní špička není natažená. Švy u palce mají být ploché. Při koupi online se řiďte velikostní tabulkou konkrétního výrobce, protože se mezi značkami mohou lišit.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Perte je naruby při teplotě, kterou doporučuje výrobce, a bez aviváže, která zhoršuje odvod potu.</li>'
          '<li>Nesušte na topení, tepelné namáhání zničí elastan.</li>'
          '<li>Při sušení v sušičce zvolte nízkou teplotu nebo šetrný program.</li>'
          '<li>Opotřebená špička a pata znamená, že se blíží konec. Průhledná síťka a uvolněné pletení nad nártem jsou také varováním.</li>'
          '<li>Párujte je, aby se opotřebovávaly rovnoměrně.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Bavlněná ponožka na dlouhou jízdu. Mokrá látka dře a chladí.</li>'
          '<li>Příliš silná zimní ponožka v těsné botě bez navýšení velikosti obuvi.</li>'
          '<li>Neodpovídající velikost, zvlášť u vícebarevných balení, kde se v balení míchají rozměry.</li>'
          '<li>Podcenění pravidelné výměny. Ponožky jsou spotřební zboží a každý rok jízdy je znatelně opotřebuje.</li>'
          '<li>Nezvážení stylu a barev. Bílé a světlé ponožky se při blátivých jízdách rychle zašpiní.</li></ul>'
          '<h2>Ponožky a cyklistická obuv: spolupráce, na které záleží</h2>'
          '<p>Ponožka je jen jedna vrstva systému, který tvoří také stélka a bota. Silničářské boty mají úzký střih a karbonovou podešev, takže tam patří nejtenčí ponožky. Do MTB bot s volnějším prostorem se vejde i silnější model. Pokud vás při jízdě tlačí prsty, nejprve zkontrolujte velikost boty, teprve potom ponožku. Dlouhodobě tlačící švy a drobné záhyby se nejčastěji řeší výměnou za bezešvý střih. Kategorii <a href="/cyklisticka-obuv/">cyklistické obuvi</a> proto probírejte společně s ponožkami.</p>'
          '<h2>Barvy, vzory a viditelnost</h2>'
          '<p>Ponožky jsou jedním z mála míst, kde se cyklista může předvést. Výrazné vzory a neonové barvy jsou na silnici vidět, protože se při šlapání nohy pohybují a řidiči si jich lépe všimnou. Na druhou stranu bílé ponožky se po prvním blátivém výjezdu změní na hnědé. Pokud jezdíte hlavně v terénu, jsou praktičtější tmavé nebo vzorované. Odrazné prvky a reflexní potisk najdete spíše u modelů do městského provozu.</p>'
          '<h2>Na co dávat pozor při výběru podle sezóny</h2>'
          '<ul><li><strong>Jaro a podzim:</strong> měňte vrstvy podle ranní a odpolední teploty. Tenké ponožky a návleky na lýtka dovolí obejít se bez celé zimní sady.</li>'
          '<li><strong>Léto:</strong> dbejte na prodyšnou síťku nad nártem a světlé barvy, které se v slunci méně prohřívají.</li>'
          '<li><strong>Zima:</strong> volte dlouhé modely z vlny nebo termo vlákna, případně dvě tenké vrstvy místo jedné silné. Pokud jezdíte pravidelně v mrazu, vyplatí se zkusit obuv, která ponožce nechá víc místa.</li>'
          '<li><strong>Dlouhé výlety:</strong> vezměte si náhradní pár. Suchá ponožka na polovině trasy dokáže zachránit celý den.</li></ul>'
          '<h2>Pro koho jsou které modely</h2>'
          '<p>Příležitostný cyklista si vystačí s několika páry univerzálních ponožek ve střední délce. Pravidelný závodník ocení tenké a lehké modely s dobře navrženým střihem. Bikepacker a dojíždějící do práce zvažují merino, protože i po několika dnech nošení méně zapáchá. Děti a mládež potřebují levnější páry, které rychle vyrostou. Jezdci s úzkou nebo širokou nohou často zjistí, že střih různých značek sedí rozdílně, takže zkoušení několika výrobců se vyplatí.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Ponožky se prodávají jednotlivě i ve vícekusových baleních. Porovnávejte proto cenu za pár, nikoli cenu balení, a u každé nabídky zkontrolujte velikost a barvu. V nabídkách se mohou lišit dostupnost a dodací doba, takže vám přehled ušetří čas. Pokud skládáte celou výbavu, pokračujte do kategorií <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>, <a href="/cyklisticke-helmy/">helmy</a> a <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>',
    faq=[
        ('Jak vysoké cyklistické ponožky zvolit?', 'Rozhoduje hlavně komfort a počasí. Nízké se hodí do horka, střední jsou univerzální a vysoké pomáhají v chladu nebo při jízdě v křoví. Estetika silničářů a bikerů se liší, ale žádné pravidlo není povinné.'),
        ('Je merino na kolo lepší než syntetika?', 'Merino lépe reguluje teplotu a méně zapáchá, syntetika rychleji schne a je odolnější. Na dlouhé jízdy a studenější dny se hodí merino, na horko a intenzivní trénink spíš syntetika nebo směs.'),
        ('Mohu jezdit v běžných sportovních ponožkách?', 'Na krátké vyjížďky ano, ale cyklistické jsou tenčí, pružnější a lépe odvádějí pot. Tlustá froté ponožka může v tuhé cyklistické botě tlačit na nárt.'),
        ('Pomůžou mi silnější ponožky proti zimě v botách?', 'Ne vždy. Příliš silná ponožka sníží prostor v botě a zhorší prokrvení, takže nohy mohou studit víc. Lepší je tenčí zimní ponožka a návlek nebo zimní obuv s větším vnitřním objemem.'),
        ('Co jsou kompresní cyklistické ponožky?', 'Jsou to pletené ponožky, které mírně stahují lýtko. Někomu vyhovuje pocit podpory při delších jízdách. Účinek je individuální a vždy záleží na střihu. Při zdravotních potížích s cévami se poraďte s lékařem.'),
        ('Jak často cyklistické ponožky měnit?', 'Podle opotřebení. Když zeslábne špička, pata nebo pletení nad nártem a ponožka sklouzává nebo tlačí, je čas na nový pár. Intenzivním jezdcům vydrží ponožky kratší dobu než příležitostným.'),
        ('Dají se cyklistické ponožky nosit i na běh nebo turistiku?', 'Mnohé ano, protože jsou lehké a prodyšné. Pro delší túry je vhodnější ponožka se zesílením pod chodidlem a na patě. Cyklistické modely na to nejsou stavěné.'),
        ('Jak vybrat velikost, když jsem mezi dvěma?', 'Zkuste větší, pokud bota sedí volněji, a menší, pokud je bota úzká. Důležité je, aby ponožka netvořila záhyby a netahala se na špičce. U online nákupu se držte tabulky výrobce.'),
        ('Prát ponožky s aviváží?', 'Nedoporučuje se. Aviváž zanechává na vláknech film, který zhoršuje odvod vlhkosti, a u merina i měkké vlny může zbytečně poškozovat strukturu. Použijte šetrný prací prostředek a řiďte se etiketou.'),
        ('Kolik párů ponožek mít do začátku?', 'Pro pravidelnou jízdu se hodí aspoň tři až pět párů, aby bylo co střídat při praní a na vícedenní výlety. Jeden pár navíc patří do batohu nebo brašny pro případ mokré trasy.'),
        ('Proč mi při jízdě ponožky sklouzávají dolů?', 'Nejčastěji je příliš velká nebo má unavenou manžetu, případně ji vytahuje voda či pot. Zkuste menší velikost nebo model s pevnějším lemem. Pomoct může i jiný střih, který lépe sedí na lýtku.'),
        ('Jsou drahé značkové ponožky o tolik lepší?', 'Rozdíl bývá ve střihu, kvalitě pletení a odolnosti. Střední třída často stačí. Zaplatit víc se vyplatí tomu, kdo jezdí hodně nebo má problémy s puchýři, jinak lze vybírat podle materiálu a velikosti.'),
    ])

# ------------------------------------------------------------------ obleceni-bojove-sporty
NEW['obleceni-bojove-sporty'] = dict(long=True,
    title='Kimona a oblečení na bojové sporty: judo, karate, BJJ',
    desc='Kimona na judo, karate, jiu-jitsu a taekwondo, pásy a tréninkové oblečení. Jak vybrat střih, gramáž a velikost a porovnat nabídky obchodů.',
    intro='<p>Kimono je pro bojové umění víc než oblečení. Musí snést tahání, házení i opakované praní, a přitom vás nesmí omezovat. Každý styl má vlastní střih: judo a jiu-jitsu počítají s pevným úchopem za látku, karate vyžaduje lehkou a volnou kutnu, taekwondo zase pohyblivý a lehký dobok. Proto se při výběru vyplatí vědět, co se v kategorii skutečně nabízí.</p>'
          '<p>Najdete tu kimona pro děti i dospělé, pásy a tréninkové oblečení od značek '
          + B(('mizuno', 'Mizuno'), ('dbx-bushido', 'DBX Bushido'), ('bushido', 'Bushido'), ('kwon', 'Kwon'), ('danrho', 'Danrho'), ('adidas', 'Adidas'), ('outshock', 'Outshock')) +
          '. Při výběru sledujte, pro který styl je kimono určené, protože střih a gramáž se mezi styly liší. Kategorii doplní <a href="/boxerske-rukavice/">boxerské rukavice</a>, <a href="/chranice-bojove-sporty/">chrániče</a> a <a href="/boxovaci-pytle/">boxovací pytle</a>.</p>',
    guide='<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Jádrem kategorie jsou bojová kimona a pásy pro judo, karate, BJJ a taekwondo, doplněná tréninkovým oblečením pro kontaktní sporty. Aby se vám nabídka četla snadněji, rozdělme ji do tří částí.</p>'
          + T(['Skupina', 'Příklady', 'Poznámka'], [
              ['Kimona a pásy', 'judo, karate, BJJ, taekwondo, dětská kimona, pásy ke kimonu', 'jádro kategorie'],
              ['Tréninkové oblečení', 'trika, kalhoty, kraťasy a rashguardy pro kontaktní sporty', 'pro nácvik a lehčí sparing'],
              ['Dětská kimona', 'lehčí a odolné modely pro začátečníky a rostoucí děti', 'důležitá je tabulka výrobce a rezerva v délce']]) +
          '<p>Pokud hledáte opravdu kimono, filtrujte podle názvu stylu, například judo, karate nebo BJJ. Ochranné pomůcky a rukavice najdete v kategoriích <a href="/boxerske-rukavice/">boxerské rukavice</a> a <a href="/chranice-bojove-sporty/">chrániče</a>.</p>'
          '<h2>Judo, karate, BJJ a taekwondo: čím se kimona liší</h2>'
          '<p>Na pohled vypadají kimona podobně, ale rozdíl poznáte při tréninku. Každý styl klade jiné nároky na pevnost látky a střih.</p>'
          '<ul><li><strong>Judo:</strong> pevná, silnější bavlna s vyztuženou kutnou a límcem, protože soupeř se kimona chytá a tahá. Rukávy a kalhoty jsou obvykle delší a střih volnější.</li>'
          '<li><strong>Jiu-jitsu (BJJ):</strong> přiléhavější střih, zpevněný límec a menší rukávy, aby soupeř těžko našel úchop. Často se prodávají v bílé, modré a černé barvě.</li>'
          '<li><strong>Karate:</strong> lehčí a volné kimono, které nebrání rychlým kopům a úderům. Tkanina bývá méně hrubá, protože se za látku tolik netahá.</li>'
          '<li><strong>Taekwondo:</strong> dobok s volnou kutnou a pohodlnými kalhotami, často s V-výstřihem. Je lehčí než judo a vhodný pro výskoky a vysoké kopy.</li>'
          '<li><strong>Kickbox a thajský box:</strong> většinou se necvičí v kimonu, ale v kraťasech a tričku. Hledejte v kategoriích <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/sportovni-tricka/">trička</a>.</li></ul>'
          '<h2>Gramáž, materiál a střih</h2>'
          '<p>Hustota tkaniny se u kimon uvádí v gramech na metr čtvereční. Čím vyšší číslo, tím silnější a odolnější látka, ale i těžší a teplejší. Lehčí modely se hodí pro začátečníky, děti a cvičení v teplejší hale, těžší pro zápas, kde se kimono tahá a trhá.</p>'
          '<ul><li><strong>Bavlna:</strong> klasika, příjemná na dotek, ale po praní se smršťuje. Nové kimono se po prvním praní může mírně srazit, proto se řiďte tabulkou výrobce.</li>'
          '<li><strong>Směsové materiály:</strong> lehčí, rychleji schnou a méně se srazí. Mohou být o něco tužší nebo méně prodyšné.</li>'
          '<li><strong>Zesílená místa:</strong> kolena, límec a švy. Pevné prošití zvyšuje životnost.</li>'
          '<li><strong>Střih:</strong> pohodlný, ne příliš volný, protože soupeř se pak snadněji chytí. Ani příliš těsný, který omezí pohyb.</li></ul>'
          '<h2>Velikost kimona</h2>'
          '<p>Výrobci uvádějí velikost podle výšky postavy, někdy i s rozměrem pro váhu. Nejčastěji najdete číselné velikosti, třeba 140, 160 nebo 180 cm, případně označení A1–A5 u zápasnických kimon. Jednotná tabulka neexistuje, takže si vždy pročtěte tu, kterou dodává výrobce konkrétního modelu.</p>'
          '<p>Kutna by měla po zavázání pásu překrývat bedra a rukávy sahat zhruba k zápěstí, případně lehce přes. Kalhoty končí kousek nad kotníkem. U dětí je lákavé koupit větší, aby kimono vydrželo déle. Příliš velké ale překáží v technice a dítě se v něm trápí, proto raději zvolte model na míru, případně s malou rezervou po praní.</p>'
          '<h2>Pásy a jejich význam</h2>'
          '<p>Pás ke kimonu nejen drží kutnu, ale ukazuje i stupeň. Systém barev se mezi styly liší a o povýšení rozhoduje trenér nebo zkouška, ne obchod. V kategorii najdete pásy v běžných barvách, jednobarevné i s proužky. Při výběru zkontrolujte délku a šířku. Pás pro dospělého má být dost dlouhý na dvojité omotání a uzel, dětský kratší.</p>'
          '<p>Nový pás bývá tuhý a uzel se snadno rozváže. Po několika trénincích změkne a drží lépe. Pás se zpravidla nepere příliš často, protože podle tradice jeho vzhled odráží roky cvičení.</p>'
          '<h2>Jak o kimono pečovat</h2>'
          '<ul><li>Perte po každém tréninku, ať se nehromadí pot a bakterie, které způsobují zápach.</li>'
          '<li>Použijte teplotu doporučenou na etiketě. Příliš vysoká teplota zvyšuje srážlivost bavlny.</li>'
          '<li>Sušte rozvěšené na ramínku nebo v prostoru s dobrým prouděním, ne na radiátoru.</li>'
          '<li>Bílá kimona skvrnu po bláti nebo trávě vyžadují rychlé ošetření. Barevný pás perte zvlášť.</li>'
          '<li>Při ukládání je nenechávejte vlhké v tašce, hrozí plíseň a zápach.</li></ul>'
          '<h2>Tréninkové oblečení bez kimona</h2>'
          '<p>Ne každý bojový sport se cvičí v kimonu. Při boxu, kickboxu, MMA nebo thajském boxu se nosí lehké kraťasy s pružným pasem a tričko, které pot odvádí od těla. Pro cvičení na zemi se hodí rashguard, těsné tričko, které chrání kůži před odřením o žíněnku a drží na těle. Pod ním mívají zápasníci kompresní <a href="/leginy/">legíny</a> nebo spodní kalhoty, protože se při kontaktu neroztrhnou ani nezachytí. Další tipy jsou v kategoriích <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a> a <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<p>Při výběru dávejte pozor na zip, kapsy a tvrdé aplikace. Při kontaktním tréninku mohou zranit partnera nebo se zachytit. Hladký střih bez kovových prvků je bezpečnější. Pokud trénujete venku, zvažte i <a href="/sportovni-bundy/">bundu</a> na cestu mezi šatnou a halou.</p>'
          '<h2>Jak poznat kvalitní kimono v obchodě</h2>'
          '<ul><li><strong>Prošití:</strong> hustý steh na ramenou, v rozkroku a u kolen. Prasklé nitě po týdnu používání jsou špatné znamení.</li>'
          '<li><strong>Límec:</strong> u judo a BJJ vyztužený, aby se při tahu nedeformoval.</li>'
          '<li><strong>Kalhoty:</strong> pružný nebo stahovací pas a prostor v kolenou.</li>'
          '<li><strong>Informace o materiálu:</strong> poctivý prodejce uvádí gramáž, složení a velikostní tabulku. Pokud údaje chybí, vyhledejte je u výrobce.</li>'
          '<li><strong>Schválení pro soutěže:</strong> u závodních modelů výrobce uvádí, pro jaký svaz je vhodné.</li></ul>'
          '<h2>Hygiena a zdravá kůže</h2>'
          '<p>Kimono a tréninkové oblečení je v těsném kontaktu s ostatními, takže hygiena není jen otázka zápachu. Čisté kimono a pás, krátké nehty a pantofle v šatně snižují riziko přenosu kožních potíží. Při podráždění kůže, vyrážce nebo ránách se poraďte s lékařem a trénink raději vynechte. Po tréninku se osprchujte a mokré oblečení hned vyndejte z tašky.</p>'
          '<h2>Kimono pro děti: na co myslet</h2>'
          '<p>Dětské kimono musí být především pohodlné. Dítě v něm skáče, padá a učí se pády, takže pevnější látka vydrží víc, ale příliš tuhá bude překážet. Mnoho oddílů začíná lehčím modelem s elastickým pasem, který se snadno obléká. Dětské sady často obsahují kutnu, kalhoty a pás, takže se vyplatí zkontrolovat, co přesně nabídka zahrnuje. Podle věku a postavy počítejte s výměnou po jednom až dvou letech, a pokud sourozenci cvičí stejný styl, vyplatí se dobře udržované kimono předat dál. K tréninku dále patří <a href="/sportovni-tasky/">taška</a> a láhev, takže se podívejte i do kategorie <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>'
          '<h2>Co dalšího se k tréninku hodí</h2>'
          '<p>Na obuv do haly a na žíněnky většinou stačí zůstat bosky nebo si vzít nazouvací pantofle, aby se předešlo infekcím nohou. Venku a v šatnách se hodí <a href="/pantofle-a-zabky/">pantofle</a>. U kontaktních sportů je důležitá ochrana: ústní chránič, chrániče holení a rukavice najdete v kategorii <a href="/chranice-bojove-sporty/">chrániče</a>. Pod kimono nosí ženy často <a href="/sportovni-podprsenky/">sportovní podprsenku</a> a tričko, muži trička nebo rashguardy z kategorie <a href="/sportovni-obleceni/">sportovního oblečení</a>. Pro přepravu se hodí <a href="/sportovni-tasky/">sportovní taška</a>.</p>'
          '<h2>Pro koho je která volba</h2>'
          '<p>Začátečník nemusí kupovat nejdražší kimono. Lehčí a pohodlný model z kvalitní bavlny mu postačí na první rok. Dětem se vyplatí levnější sada s pásem, protože rychle rostou. Soutěžící oceňují pevné kimono schválené pro turnaje, u kterého ověřují požadavky svazu, protože pravidla pro střih a barvu se liší. Dojíždějící trenér potřebuje druhé kimono na střídání. A kdo cvičí jen občas v kroužku, vystačí s univerzálním střihem, který se hodí pro více stylů.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě kimona podle jiného stylu, než který cvičíte. Judogi do karate nebo BJJ gi do taekwondo obvykle sedí špatně.</li>'
          '<li>Ignorování smrštění. Po prvním praní bývá kimono kratší.</li>'
          '<li>Výběr podle vzhledu místo gramáže a střihu.</li>'
          '<li>Zaměňování střihu pro judo a BJJ, i když se kimona na pohled podobají.</li>'
          '<li>Zapomenutí na požadavky soutěže nebo oddílu, například barvu a nášivky.</li></ul>'
          '<h2>Jak porovnávat na Sportece</h2>'
          '<p>U stejného modelu vidíte nabídky více obchodů, včetně dostupnosti jednotlivých velikostí. Sledujte název stylu, popis materiálu a tabulku velikostí. Pokud vás zajímá celkové vybavení pro kontaktní sporty, procházejte <a href="/bojove-sporty/">bojové sporty</a>, <a href="/treninkova-obuv/">tréninkovou obuv</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>',
    faq=[
        ('Jaké kimono vybrat na začátek?', 'Pro začátečníka stačí lehčí nebo střední kimono z bavlny ve správném stylu. Nejprve zjistěte, jaké kimono váš oddíl vyžaduje. Dražší model má smysl, až když víte, že u sportu zůstanete.'),
        ('Jak moc se kimono smrští?', 'Bavlněné kimono se po praní obvykle znatelně zmenší, hlavně na délku. Výrobci často doporučují koupit o něco větší, než je potřeba, nebo respektovat jejich tabulku. Přesné údaje najdete u konkrétního modelu.'),
        ('Je rozdíl mezi judo a BJJ kimonem?', 'Ano. Judo má volnější střih a pevnější kutnu, BJJ přiléhavější střih a užší rukávy. Pro soutěž v daném sportu si ověřte pravidla svazu, protože se u střihu a barev liší.'),
        ('Do kolika stupňů mohu kimono prát?', 'Řiďte se etiketou. Obecně se doporučuje mírnější teplota, která omezuje srážlivost bavlny. Vysoké teploty látku zbytečně namáhají a mohou zkrátit její životnost.'),
        ('Čím se liší cena kimon?', 'Rozdíl dělá gramáž látky, zpevnění límce a švů, střih a značka. Pro začátečníka stačí střední gramáž; dražší model má smysl, až když víte, že u sportu zůstanete.'),
        ('Jakou velikost kimona zvolit pro dítě?', 'Podle výšky dítěte a tabulky výrobce. Příliš velké kimono překáží v technice a může vést k úrazu. Pokud dítě rychle roste, počítejte s tím, že po roce bude potřeba větší.'),
        ('Co znamená barva pásu?', 'Barva obvykle vyjadřuje stupeň v daném sportu a systém se liší podle stylu a svazu. O povýšení rozhoduje trenér nebo zkouška. Při koupi pásu hledejte správnou délku a šířku.'),
        ('Dá se cvičit v obyčejném tričku a kalhotách?', 'U sportů bez úchopů, jako je kickbox nebo thajský box, ano. U judo, BJJ a podobných stylů je kimono podstatné. Oddíly často požadují oficiální kimono po prvních trénincích.'),
        ('Jak se zbavit zápachu z kimona?', 'Perte po každém tréninku, dobře vysušte a neukládejte vlhké. Pomoct může i delší máchání nebo prostředek na sportovní textil. Hlavní příčinou zápachu je zbylý pot a vlhko, ne špatný materiál.'),
        ('Mohu používat kimono pro více stylů?', 'Záleží na stylu a oddílu. Karate a taekwondo kimona jsou si podobná, judo a BJJ se liší střihem a pevností. Pokud trénujete víc sportů, poraďte se s trenérem.'),
    ])

# ------------------------------------------------------------------ iontove-napoje
NEW['iontove-napoje'] = dict(long=True,
    title='Iontové nápoje a hydratace: prášky, tablety, elektrolyty',
    desc='Iontové nápoje, izotonické prášky, šumivé tablety a elektrolyty pro sport. Jak číst složení a porovnat nabídky českých obchodů a značek.',
    intro='<p>Při delším pohybu pijeme víc než jen vodu a tělo mimo tekutiny ztrácí také minerály, které s potem odcházejí. Právě pro tuto situaci vznikly iontové nápoje: prášky k rozmíchání, šumivé tablety, tekuté koncentráty i kapsle s elektrolyty. Kategorie je široká a názvy matou, proto se vyplatí vědět, čím se jednotlivé formy liší a kdy dává smysl sáhnout po něčem víc než po čisté vodě.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek '
          + B(('gymbeam', 'GymBeam'), ('isostar', 'Isostar'), ('penco', 'Penco'), ('activlab', 'ActivLab'), ('extrifit', 'Extrifit'), ('enervit', 'Enervit'), ('chimpanzee', 'Chimpanzee'), ('flow-nutrition', 'Flow Nutrition')) +
          '. Související přehledy najdete v kategoriích <a href="/sportovni-vyziva/">sportovní výživa</a>, <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>, <a href="/lahve-a-termosky/">lahve a termosky</a> a <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>',
    guide='<h2>Jaké druhy produktů v kategorii najdete</h2>'
          '<p>Slovo „iontový“ se používá volně. Pod stejným názvem se prodává prášek s cukrem, bezcukerná varianta se sladidly, šumivá tableta nebo samotné soli bez energie. Rozdíl poznáte ze složení a údajů na etiketě.</p>'
          + T(['Forma', 'Typické použití', 'Poznámka'], [
              ['Prášek k rozmíchání', 'trénink, závod, každodenní pití při sportu', 'nejvíc variant, výhodný na litr nápoje'],
              ['Šumivé tablety', 'kolo, turistika, cestování', 'lehké a pohodlné, malá dávka na tabletu'],
              ['Tekutý koncentrát', 'ředění do lahve', 'praktický, ale těžší a objemnější'],
              ['Kapsle s elektrolyty', 'doplnění solí bez sladké chuti', 'neobsahují energii, pijete vodu zvlášť'],
              ['Sacharidové nápoje s vyšším obsahem energie', 'dlouhé vytrvalostní výkony', 'cukrů je výrazně víc než v klasickém ionťáku'],
              ['Hotové nápoje', 'spěch, cesta', 'bývají objemné a méně výhodné']]) +
          '<p>V nabídce Sporteky najdete převážně prášky v dózách nebo sáčcích, ale i šumivé tablety, tekuté koncentráty a samostatné soli v kapslích. U každého produktu se podívejte na údaje o dávkování, protože stejná dóza vystačí na různý počet porcí.</p>'
          '<h2>Izotonický, hypotonický a hypertonický nápoj</h2>'
          '<p>Tyto pojmy popisují koncentraci rozpuštěných látek v nápoji vzhledem k tělním tekutinám. Izotonický nápoj má koncentraci podobnou, hypotonický nižší a hypertonický vyšší. Výrobci tyto výrazy používají k tomu, aby naznačili, na co je nápoj určený: hypotonické jsou lehčí na žaludek, hypertonické bohatší na energii. Přesná hodnota se liší produkt od produktu, a proto se řiďte údaji na obalu a doporučením výrobce, ne názvem.</p>'
          '<h2>Jak číst složení</h2>'
          '<ul><li><strong>Sacharidy:</strong> glukóza, fruktóza, maltodextrin nebo sacharóza dodávají energii. Jejich množství rozhoduje, zda je nápoj spíš na hydrataci, nebo na energii při dlouhém výkonu.</li>'
          '<li><strong>Elektrolyty:</strong> sodík, draslík, hořčík, vápník a chloridy. Různé produkty je kombinují v různém poměru a množství.</li>'
          '<li><strong>Sladidla:</strong> bezcukerné varianty používají umělá nebo přírodní sladidla. Chuť je odlišná, někomu vadí.</li>'
          '<li><strong>Kyseliny a aromata:</strong> dodávají chuť a stabilitu. Pokud máte citlivý žaludek nebo alergie, čtěte i drobný text.</li>'
          '<li><strong>Doplňky navíc:</strong> vitamíny, aminokyseliny, kofein nebo kreatin. Takové nápoje jsou hybridy s dalšími účinky a při kombinaci s jinými doplňky snadno překročíte doporučené dávky.</li></ul>'
          '<p>Na obalu hledejte doporučené dávkování a množství vody na jednu porci. Silnější roztok neznamená lepší účinek, naopak může vést k žaludečním potížím.</p>'
          '<h2>Kdy se vyplatí iontový nápoj a kdy stačí voda</h2>'
          '<p>Při krátkém a mírném pohybu zpravidla stačí obyčejná voda. Iontový nápoj dává smysl zejména při delší a intenzivnější zátěži, v horku nebo pokud se hodně potíte. Pomáhá i tím, že chutná a motivuje k pití. To, kolik pít, je individuální a závisí na teplotě, intenzitě a vaší konstituci. Obecným vodítkem je pít pravidelně po menších množstvích a řídit se žízní. U zdravotních potíží nebo při dietě s omezením soli se předem poraďte s lékařem.</p>'
          '<p>Tento text nemá nahradit rady odborníka. Výživové doplňky neslouží k léčbě žádných onemocnění, a pokud máte potíže se srdcem, ledvinami nebo krevním tlakem, zeptejte se před užíváním lékaře.</p>'
          '<h2>Podle sportu</h2>'
          '<ul><li><strong>Běh:</strong> do lahve na pásek nebo do <a href="/bezecke-vesty-a-batohy/">běžecké vesty</a> se hodí lehký roztok. Na delší tratě jej doplní <a href="/energeticke-gely-a-tycinky/">gely</a>. Podívejte se i do kategorie <a href="/beh/">běh</a>.</li>'
          '<li><strong>Cyklistika:</strong> bidon s nápojem se vejde do košíku. Praktické jsou <a href="/cyklo-lahve-a-drzaky/">cyklistické lahve a držáky</a> a v létě se osvědčuje nápoj s elektrolyty.</li>'
          '<li><strong>Fitness a posilovna:</strong> při běžném tréninku často stačí voda. Pro delší a intenzivní jednotky zvažte slabší roztok. Další doplňky jsou v kategoriích <a href="/proteiny/">proteiny</a>, <a href="/kreatin/">kreatin</a> a <a href="/predtreninkove-boostery/">předtréninkové boostery</a>.</li>'
          '<li><strong>Míčové sporty:</strong> přestávky a poločasy mají omezený čas, takže se hodí lahev připravená předem. Více v kategoriích <a href="/fotbal/">fotbal</a> a <a href="/florbal/">florbal</a>.</li>'
          '<li><strong>Turistika a kemp:</strong> lehké tablety a prášek v sáčcích zabírají málo místa. K tomu patří <a href="/outdoorova-strava/">outdoorová strava</a> a <a href="/lahve-a-termosky/">lahve</a>.</li></ul>'
          '<h2>Jak nápoj správně připravit</h2>'
          '<p>Základem je přesné dávkování. Dózy mívají odměrku, ale její velikost se mezi značkami liší. Prášek rozmíchejte v části vody a pak dolijte. V lahvi se šejkrem se rozpustí lépe než v hrnku. Pokud nápoj připravíte předem, uchovejte ho v chladu a spotřebujte v době uvedené výrobcem, protože sladké roztoky v horku rychle kazí chuť.</p>'
          '<ul><li>Nepřidávejte víc prášku „pro jistotu“. Silný roztok žaludek zatěžuje.</li>'
          '<li>Lahev po použití vypláchněte a občas důkladněji vyčistěte, protože sladký film podporuje plísně.</li>'
          '<li>Do nápoje nepřidávejte horkou vodu u produktů, které to nedoporučují. Některé složky mohou ztratit stabilitu.</li>'
          '<li>V mrazu používejte termosku. Jinak může nápoj v lahvi zamrznout.</li></ul>'
          '<h2>Chuť, žaludek a snášenlivost</h2>'
          '<p>Chuť je u ionťáku překvapivě důležitá. Příliš sladký nápoj po hodině unavuje a nechce se do něj pít, naopak slabší a méně sladký nápoj lze pít déle. Zkoušejte nové produkty při tréninku, ne při závodě. Citlivější žaludek může na některá sladidla nebo koncentrovanější roztoky reagovat nepříjemně. Pokud máte alergie, pozorně čtěte složení a upozornění, a při pochybnostech vyhledejte lékaře.</p>'
          '<h2>Načasování: před, během a po výkonu</h2>'
          '<p>Většina lidí pije ionťák během zátěže, ale někdo ho používá i před startem a po závodě. Před výkonem dává smysl dopít vodu s mírnou dávkou solí, pokud víte, že vás čeká dlouhý den v horku. Během výkonu se pije po malých doušcích v pravidelných intervalech, ne celá lahev najednou. Po výkonu je důležitější běžné jídlo a pití než specializovaný doplněk. Přesný postup se mezi sportovci liší, takže si vyzkoušejte, co vám sedí, a u vážnějších cílů se obraťte na trenéra nebo výživového poradce.</p>'
          '<h2>Pocení, počasí a nadmořská výška</h2>'
          '<p>Potřeba tekutin není stálá. Horko, vlhkost, silné oblečení a vyšší tempo zvyšují pocení, v zimě je pocit žízně slabší, ale tělo tekutiny stejně ztrácí. Proto se vyplatí pít podle plánu a neočekávat, že vás žízeň vždy včas upozorní. Ve vyšších nadmořských výškách je vzduch suchý, takže se dýcháním ztrácí víc tekutiny. Na túrách v kombinaci s <a href="/batohy/">batohem</a> se hodí hydratační vak nebo lahve na boku batohu, abyste nemuseli zastavovat při každém loku.</p>'
          '<h2>Jak porovnat dvě dózy mezi sebou</h2>'
          '<p>Dózy mají různou váhu a různou porci, takže cena za dózu nic neříká. Vezměte hmotnost balení, vydělte ji hmotností jedné porce, a zjistíte počet nápojů. Potom srovnejte množství sacharidů a sodíku na porci. Podívejte se, jestli je v porci započtena rozpuštěná voda, kolik mililitrů výrobce doporučuje na jednu porci a zda obal zmiňuje alergeny. Rozdíl může být výrazný, i když dvě dózy vypadají stejně.</p>'
          '<h2>Cestování a skladování</h2>'
          '<ul><li>Sáčky a tablety se hodí do kapsy batohu nebo vesty. Prášek v dóze je těžký, přesypte ho do menší nádoby.</li>'
          '<li>Prášek uchovávejte na suchém místě bez přímého slunce, jinak ztvrdne a ztratí chuť.</li>'
          '<li>Na cestách do zahraničí si ověřte pravidla pro dovoz sportovních doplňků do cílové země.</li>'
          '<li>Mezi nápoje v příručním zavazadle letadla se tekuté koncentráty počítají, takže řešte limit kapalin.</li>'
          '<li>Hotový nápoj nenechávejte na slunci. Ve vyhřátém autě se rychle kazí a ztrácí chuť.</li></ul>'
          '<h2>Pro koho které řešení</h2>'
          '<p>Rekreační běžec a cyklista si spokojeně vystačí s lehkým práškem nebo tabletami ve vodě. Maratonec a vytrvalec zvažují energeticky bohatší roztok doplněný gely. Hráč míčových sportů ocení nápoj, který se dobře pije v krátké pauze a nezatěžuje žaludek. Turista na vícedenní cestě sáhne po lehkých tabletách nebo sáčcích. A ten, kdo nemá rád sladkou chuť, může zkusit samotné elektrolyty v kapslích.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Pití sladkého ionťáku místo vody během celého dne, ne jen při sportu.</li>'
          '<li>Příliš koncentrovaná příprava a následné žaludeční potíže.</li>'
          '<li>Porovnávání jen podle ceny dózy místo ceny za porci.</li>'
          '<li>Zkoušení nového nápoje až při závodě.</li>'
          '<li>Opomenutí, že kapsle s elektrolyty nenahrazují pití vody.</li>'
          '<li>Spoléhání na doplněk místo dostatku pestré stravy.</li></ul>'
          '<h2>Jak nakupovat a porovnávat</h2>'
          '<p>Stejný produkt bývá v různých obchodech v různé velikosti balení a s různou dobou dodání. Sporteka u každé nabídky ukazuje dostupnost, takže snadno najdete obchod, který ho má skladem. Porovnávejte cenu za porci, nikoli za balení. Zkontrolujte datum minimální trvanlivosti, zejména u akčních nabídek. Pokud vybíráte celkovou sportovní výživu, pokračujte do kategorií <a href="/aminokyseliny-bcaa/">aminokyseliny</a>, <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky</a> a <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>.</p>',
    faq=[
        ('Potřebuji iontový nápoj, nebo stačí voda?', 'Při krátkém a mírném cvičení většinou stačí voda. Iontový nápoj dává smysl při delším a intenzivnějším výkonu, v horku nebo při silném pocení. Individuální potřeby se liší, a při zdravotních omezeních se poraďte s lékařem.'),
        ('Čím se liší izotonický nápoj od hypotonického?', 'Liší se koncentrací rozpuštěných látek. Hypotonický je zředěnější, izotonický střední a hypertonický koncentrovanější. Výrobci takto naznačují zaměření nápoje, ale přesné složení se liší podle produktu.'),
        ('Je lepší prášek, nebo šumivá tableta?', 'Prášek bývá výhodnější na litr nápoje a nabízí víc variant. Tablety jsou lehké a pohodlné na cesty, ale často obsahují méně složek. Vyberte podle způsobu použití a chuti.'),
        ('Mohu iontový nápoj pít celý den?', 'Obvykle je určený k pití při sportu a krátce kolem něj. Sladké varianty obsahují cukry, a pokud je pijete celý den, bez pohybu nemusí být výhodné. Řiďte se doporučením výrobce na obalu.'),
        ('Jak připravit nápoj, aby nebyl příliš sladký?', 'Dodržte doporučené dávkování a v případě potřeby použijte víc vody. Bezcukerné varianty se sladidly mají odlišnou chuť. Můžete také zkusit slabší roztok, než odpovídá návodu, pokud ho výrobce dovoluje.'),
        ('K čemu jsou kapsle s elektrolyty?', 'Obsahují minerály bez cukru a chuti. Hodí se pro ty, kdo nechtějí sladký nápoj. Je potřeba pít dostatek vody zvlášť a dodržet dávkování. Při zdravotních potížích se poraďte s lékařem.'),
        ('Hodí se iontové nápoje pro děti?', 'Děti obvykle stačí voda, případně běžná strava. Pokud zvažujete doplněk pro dítě, ověřte si vhodnost u lékaře nebo pediatra a řiďte se pokyny na obalu.'),
        ('Můžu iontový nápoj nosit v termosce?', 'Ano, v chladu je termoska praktická. Po použití ji důkladně vypláchněte, protože sladký roztok může zanechávat zápach a plísně. Vybírejte nádoby určené pro nápoje s příměsemi.'),
        ('Jak dlouho vydrží otevřená dóza prášku?', 'Řiďte se údaji na obalu. Dózu uchovávejte suchou a dobře uzavřenou, protože vlhkost způsobuje hrudky. Hotový roztok je lepší spotřebovat do několika hodin, nejlépe v chladu.'),
        ('Na co si dát pozor u nápojů s kofeinem nebo jinými přísadami?', 'Takové nápoje kombinují více účinných látek. Ověřte množství kofeinu a jiných přísad, abyste jich s dalšími doplňky nepřekročili příliš. Citlivé osoby, těhotné ženy a lidé s chronickými potížemi by měli předem konzultovat lékaře.'),
    ])
