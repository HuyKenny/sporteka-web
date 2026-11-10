"""sporteka.cz — facet landing texts wave 131: elektrokolobezka-levne, kopacky-under-armour, gymbeam-leginy, detske-lyzarske-helmy.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ elektrokolobezka-levne
NEW['elektrokolobezka-levne'] = dict(
    title='Elektrokoloběžka levně: jak vybrat model ve slevě',
    desc='Slevněné elektrokoloběžky: jak poznat skutečnou slevu, co číst z baterie, brzd a pneumatik a na čem se u levnějšího modelu šetřit nesmí.',
    intro='<p>Slevněná elektrokoloběžka může být výhodný nákup, ale také past, protože u stroje s baterií, motorem a brzdami se nedá šetřit na všem. Rozdíl mezi dobrým kouskem v akci a modelem, který zlevnil, protože jeho slabou baterii nikdo nechtěl, je potřeba umět přečíst z parametrů. '
          'Tato stránka ukazuje modely z kategorie <a href="/elektrokolobezky/">elektrokoloběžky</a>, u kterých obchody uvádějí snížení ceny. Průvodce vás naučí hodnotit věci, které se v reklamě objevují nejméně: skutečný dojezd, kapacitu v watthodinách, typ brzd a pneumatik, hmotnost a dostupnost servisu. '
          'Najdete tu tabulku toho, co se u levnějšího modelu dá oželet a co ne, postup, jak poznat opravdovou slevu, i rady pro dojíždění, výlety a rodiny s dětmi. Pro mladší jezdce slouží samostatný výběr <a href="/detska-elektrokolobezka/">dětská elektrokoloběžka</a>.</p>',
    guide='<h2>Levná neznamená špatná, ale něco vždy chybí</h2>'
          '<p>Elektrokoloběžka je souhrn několika dílů, které stojí peníze: baterie, motor s řídicí jednotkou, brzdy, rám a pneumatiky. Když výrobce nebo obchod cenu sníží, pokrývá to buď marži, nebo starší generaci modelu, nebo zásoby, které se špatně prodávají. První dvě varianty jsou výhodné pro zákazníka, třetí vyžaduje opatrnost. Důležité je proto zjistit, <strong>kde přesně se úspora skrývá</strong>. U kvalitnějších značek bývá nejčastěji v tom, že na trh přišel nový ročník a starý se vyprodává za nižší cenu. U neznámých dovozců bývá úspora často v menší baterii, slabších brzdách nebo pneumatikách, které se rychle propíchnou.</p>'
          '<p>Pomůže jednoduchá úvaha: nejdřív si určete, jak daleko a po jakém povrchu budete jezdit, a teprve potom hledejte nejlevnější model, který tyto požadavky splní. Levná koloběžka, která vás na půlce cesty nechá bez šťávy nebo se při brzdění třese, je dražší než model, který stál o něco víc a funguje.</p>'
          '<h2>Baterie: watthodiny řeknou víc než inzerovaný dojezd</h2>'
          '<p>Dojezd uvedený v popisu se měří za ideálních podmínek: lehký jezdec, rovina, mírné tempo, zapnutý nejúspornější režim. V praxi s přibývající hmotností, kopci, větrem a chladem klesá. Spolehlivější než kilometry je <strong>kapacita baterie v watthodinách (Wh)</strong>. Spočítáte ji tak, že vynásobíte napětí ve voltech kapacitou v ampérhodinách. Baterie 36 V s 10 Ah má tedy 360 Wh, baterie 48 V s 15 Ah má 720 Wh. Čím vyšší číslo, tím víc energie, a tím i větší hmotnost a delší nabíjení.</p>'
          + T(['Parametr', 'Co znamená', 'Na co si dát pozor'], [
              ['Napětí (V)', 'úroveň, na které baterie pracuje', 'vyšší napětí obvykle znamená svižnější zrychlení do kopce'],
              ['Kapacita (Ah)', 'kolik proudu baterie dodá za hodinu', 'sama o sobě nic neříká, dokud ji nepřevedete na Wh'],
              ['Kapacita (Wh)', 'celková zásoba energie', 'nejlepší číslo pro srovnání modelů mezi sebou'],
              ['Výkon motoru (W)', 'jmenovitý nebo špičkový výkon', 'špičkový údaj bývá výrazně vyšší než trvalý, ptejte se na jmenovitý'],
              ['Dojezd (km)', 'orientační vzdálenost za ideálních podmínek', 'počítejte spíš s polovinou až dvěma třetinami uvedené hodnoty'],
              ['Doba nabíjení', 'čas od prázdné po plnou baterii', 'u velké baterie s malou nabíječkou i několik hodin']]) +
          '<p>Chcete-li dojíždět do práce pár kilometrů v jednom směru, stačí menší baterie a lehčí model. Chcete-li ujet delší trasu bez možnosti nabít, hledejte víc watthodin, i kdyby to znamenalo vyšší hmotnost. Výměnná baterie je pro dojíždění ještě praktičtější, protože ji lze nabít doma nebo v kanceláři, a také ji lze časem obnovit, aniž byste vyměňovali celý stroj.</p>'
          '<h2>Co se u levnější koloběžky dá oželet a co ne</h2>'
          '<p>Ne všechny kompromisy jsou stejně nebezpečné. Některé jen ubírají na komfortu, jiné ohrožují bezpečnost. Následující přehled pomůže rozlišit, kde je rozumné ušetřit.</p>'
          + T(['Součást', 'Dá se ušetřit', 'Raději ne'], [
              ['Brzdy', 'jeden kotoučový nebo bubnový plus elektronická brzda pro jízdu po městě', 'jen elektronická brzda bez mechanické'],
              ['Pneumatiky', 'plné pneumatiky pro hladký asfalt a nízkou údržbu', 'tvrdé plné pneumatiky na dlažbě a kočičích hlavách'],
              ['Odpružení', 'bez odpružení na rovinu a kratší trasy', 'bez odpružení při denní jízdě po rozbitých cestách'],
              ['Displej a aplikace', 'jednoduchý displej, bez aplikace', 'nečitelný displej na přímém slunci'],
              ['Osvětlení', 'základní přední a zadní světlo', 'žádné nebo slabé světlo, pokud jezdíte za šera'],
              ['Rám a kolo', 'menší kola u skládacího modelu', 'slabý zamykací mechanismus u skládacího rámu'],
              ['Odolnost proti vodě', 'nižší krytí pro jezdce, kteří nejezdí v dešti', 'žádné údaje o krytí, pokud jedete i za mokra']]) +
          '<p>Základní pravidlo zní: <strong>na brzdách, rámu a baterii se neušetří</strong>, na displeji, aplikaci a vzhledu ano. Kvalitní brzda je ten díl, který vás zastaví před autem. Rám, který se po roce rozviklá v kloubu, je zase důvod ke stížnosti, u které se servisu nikdo nechce ujmout.</p>'
          '<h2>Pneumatiky, brzdy a odpružení v praxi</h2>'
          '<p>Vzduchové pneumatiky tlumí nárazy a lépe drží v mokru, ale vyžadují občasné dofouknutí a opravu defektu. Plné pneumatiky se nepropíchnou, jenže jsou tvrdší, takže ruce a záda dostávají víc. Pro denní dojíždění po městě je rozumný kompromis větší kolo se vzduchovou pneumatikou. Pro malé rodinné koloběžky nebo kratší jízdu na hladkém povrchu stačí plné pneumatiky.</p>'
          '<p>Brzdy jsou u elektrokoloběžek ve třech provedeních: kotoučová brzda, bubnová brzda a elektronická brzda motoru. Kotoučová je citlivější a lépe zabírá, bubnová je méně náročná na seřízení, elektronická slouží spíš jako doplněk. Nechtějte model, který má jen elektronickou brzdu. Zkontrolujte, zda má také nášlapnou nebo ruční mechanickou brzdu a zda jde seřídit.</p>'
          '<p>Odpružení má smysl, pokud jezdíte po nerovném povrchu. U levných modelů bývá odpružení jen pružinový prvek v předním kole a jeho užitná hodnota je malá. Lepší než špatné odpružení je často větší kolo a pneumatika s nižším tlakem.</p>'
          '<h2>Jak poznat skutečnou slevu</h2>'
          '<p>Přeškrtnutá cena u elektrokoloběžky neříká, kolik by model stál jinde. Zkontrolujte tři věci. Za prvé <strong>historii ceny</strong>: porovnejte, za kolik se tentýž model prodával v posledních týdnech, nejen jaká je doporučená cena výrobce. Za druhé <strong>ročník a verzi</strong>: stejný název modelu může mít jinou baterii nebo displej než minulý rok. Za třetí <strong>obchod a záruku</strong>: sleva v obchodě, který nemá českou podporu, vás může stát víc než ušetříte, pokud se baterie nebo řídicí jednotka porouchají.</p>'
          '<ul><li><strong>Zkontrolujte přesný název modelu</strong> včetně písmen za číslem, často označují jinou verzi.</li>'
          '<li><strong>Ověřte kapacitu baterie</strong> v Wh, ne jen slova „dlouhý dojezd“.</li>'
          '<li><strong>Zjistěte, kdo dělá servis</strong> a zda jsou skladem náhradní díly, hlavně pneumatiky a duše.</li>'
          '<li><strong>Zeptejte se na záruku na baterii</strong>, bývá kratší než záruka na stroj.</li>'
          '<li><strong>Ověřte hmotnost</strong>, protože těžká koloběžka se špatně nosí do schodů a výtahu.</li></ul>'
          '<p>Slevy se obvykle objevují při příchodu nového ročníku, na konci sezóny a v době výprodejů, ne uprostřed jara, kdy po koloběžkách roste poptávka. Chcete-li ušetřit, plánujte nákup mimo hlavní sezónu.</p>'
          '<h2>Pro koho se levná elektrokoloběžka hodí</h2>'
          '<p><strong>Dojíždění po městě.</strong> Důležitá je nízká hmotnost, skládací konstrukce a rozumný dojezd. Nesmí být příliš těžká, pokud ji potřebujete nosit do schodů, a měla by mít dobré světlo i brzdy. Menší výkon vás nezabrzdí, pokud jezdíte po rovině.</p>'
          '<p><strong>Víkendové vyjížďky a stezky.</strong> Tady rozhoduje baterie a pneumatiky. Větší kola se vzduchovým plněním a výkonnější motor poradí s kopcem a štěrkem. Takové modely bývají těžší a dražší, a proto je dobré hledat u nich zlevněnou starší generaci, ne nejlevnější kus s neznámým původem. Nabídku podobných strojů najdete i v kategorii <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a> a v souvisejících <a href="/kolobezky/">koloběžkách</a>; pro jízdu s trikovými prvky slouží <a href="/freestyle-kolobezky/">freestyle koloběžky</a>.</p>'
          '<p><strong>Děti a mladiství.</strong> Menší dětské modely mají omezenou rychlost a nižší hmotnost, což je pro děti důležité. Hledejte pevný stojan, ochranu rukou, dobré brzdy a možnost omezit rychlost. Na samostatný výběr se podívejte do <a href="/detska-elektrokolobezka/">dětských elektrokoloběžek</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Mezi zlevněnými modely se objevují značky, které prodávají koloběžky ve více kategoriích. Mezi zavedená jména patří ' + B(('xiaomi', 'Xiaomi'), ('segway', 'Segway'), ('navee', 'Navee')) + ', které prodávají hlavně městské modely s aplikací. České a slovenské značky jako ' + B(('eljet', 'Eljet'), ('bluetouch', 'Bluetouch'), ('city-boss', 'City Boss'), ('todimart', 'Todimart')) + ' nabízejí široký výběr od jednoduchých po výkonné kusy. Pro skladné modely se podívejte také na ' + B(('joyor', 'Joyor'), ('kukirin', 'Kukirin'), ('motus', 'Motus'), ('iscooter', 'Iscooter')) + '. Který model sedí, neříká značka, ale parametry: Wh, brzdy, hmotnost a servis.</p>'
          '<h2>Bezpečnost a nabíjení</h2>'
          '<p>Na elektrokoloběžce jezdíte rychleji než na běžné, takže se vyplatí helma, rukavice a odrazky. Helmu nevybírejte podle ceny, ale podle velikosti a komfortu, aby ji dítě i dospělý skutečně nosili. Nabídku najdete v kategoriích <a href="/chranice-a-helmy/">chrániče a helmy</a> a <a href="/cyklisticke-helmy/">cyklistické helmy</a>. Před jízdou zkontrolujte tlak v pneumatikách a funkci brzd.</p>'
          '<p>Baterii nabíjejte originální nabíječkou, nikdy ne na hořlavém povrchu a ne bez dozoru. Poškozenou nebo nafouklou baterii nepoužívejte. Přes zimu ji uchovávejte částečně nabitou v suché místnosti. Koloběžka se hodí nejen k přepravě, ale i jako alternativa k <a href="/elektrokola/">elektrokolům</a>; než se rozhodnete, zvažte, kde ji budete skladovat a jak často budete jezdit.</p>'
          '<h2>Kontrolní seznam před objednávkou</h2>'
          '<ol><li>Spočítejte kapacitu baterie v Wh a porovnejte ji s požadovanou trasou.</li>'
          '<li>Zkontrolujte, zda má koloběžka mechanickou brzdu, nejen elektronickou.</li>'
          '<li>Podívejte se na hmotnost a rozměry po složení.</li>'
          '<li>Ověřte, kdo poskytuje záruční servis a kde seženete pneumatiky a duše.</li>'
          '<li>Porovnejte aktuální nabídku ve více obchodech a sledujte, jak se model prodával dřív.</li></ol>',
    faq=[
        ('Proč se některé elektrokoloběžky prodávají tak levně?', 'Důvodů je několik. Může jít o starší ročník, který se vyprodává, o menší baterii a slabší motor nebo o jednodušší brzdy a pneumatiky. Levnější neznamená automaticky horší, ale cenu je třeba číst společně s parametry, hlavně s kapacitou baterie a typem brzd.'),
        ('Jak spočítám reálný dojezd elektrokoloběžky?', 'Vynásobte napětí baterie ve voltech kapacitou v ampérhodinách a získáte kapacitu ve watthodinách. Zjednodušeně dojezd závisí na tomto čísle, hmotnosti jezdce, rychlosti, terénu a teplotě. Počítejte s tím, že skutečný dojezd bude pod hodnotou uvedenou výrobcem.'),
        ('Na čem se u levné elektrokoloběžky nesmí šetřit?', 'Na brzdách, rámu a baterii. Mechanická brzda je nutnost, rám se skládacím kloubem musí držet bez vůle a baterie by měla pocházet od ověřeného výrobce s jasně uvedenou kapacitou a zárukou.'),
        ('Je lepší vzduchová nebo plná pneumatika?', 'Vzduchová tlumí nárazy a lépe drží v mokru, ale může se propíchnout. Plná se nepropíchne, jenže je tvrdší a méně příjemná na nerovném povrchu. Pro denní dojíždění po městě je vhodnější vzduchová, pro krátké jízdy po rovině vyhoví plná.'),
        ('Kdy se elektrokoloběžky nejvíce zlevňují?', 'Typicky při uvedení nového ročníku, na konci sezóny a v době velkých výprodejů. Uprostřed jara a léta, kdy je poptávka největší, bývají slevy menší. Pokud nespěcháte, sledujte ceny ve více obchodech.'),
        ('Co znamená krytí IP u elektrokoloběžky?', 'Označení udává odolnost proti prachu a vodě. Vyšší druhé číslo znamená lepší ochranu proti vodě. Krytí neznamená, že se s koloběžkou dá jezdit v silném dešti nebo ji čistit proudem vody, vždy se řiďte pokyny výrobce.'),
        ('Hodí se levná elektrokoloběžka pro děti?', 'Pro děti je lepší vybírat z dětských modelů s omezenou rychlostí, nižší hmotností a dobrými brzdami. Dospělý model s vysokým výkonem je pro dítě nevhodný, i když je ve slevě. Podrobnosti najdete u dětských elektrokoloběžek.'),
        ('Jak dlouho vydrží baterie elektrokoloběžky?', 'Záleží na kvalitě článků, počtu nabití a způsobu uložení. Baterii šetří nabíjení originální nabíječkou, vyhýbání se úplnému vybití a skladování přes zimu částečně nabité v suchu. Po několika letech kapacita znatelně klesá, proto se ptejte na dostupnost náhradní baterie.'),
        ('Na co se zeptat obchodu před nákupem ve slevě?', 'Zeptejte se na verzi modelu, kapacitu baterie, záruku na stroj i baterii a dostupnost náhradních dílů. Ověřte také, kdo dělá servis a zda lze objednat pneumatiky, duše nebo brzdové destičky bez čekání na dovoz.'),
        ('Je lepší skládací nebo pevná elektrokoloběžka?', 'Skládací se lépe vozí ve vlaku nebo ve výtahu a ukládá do bytu, má však pohyblivý kloub, který musí pevně držet. Pevný rám je odolnější a tišší na nerovnostech, ale zabere víc místa. Rozhodněte podle toho, jak často budete koloběžku nosit.'),
    ])

# ------------------------------------------------------------------ kopacky-under-armour
NEW['kopacky-under-armour'] = dict(
    title='Kopačky Under Armour: řady, povrchy a velikosti',
    desc='Kopačky Under Armour: jak se orientovat v řadách Magnetico a Shadow, kdy zvolit FG nebo turf a jak je porovnat s Nike, Adidas a Pumou.',
    intro='<p>Under Armour je americká značka, která se proslavila přiléhavým sportovním oblečením, a kopačky u ní tvoří užší, ale zajímavou nabídku. Hodí se těm, kdo chtějí jiný tvar a design, než nabízejí největší fotbalové firmy. '
          'Na této stránce jsou kopačky Under Armour z kategorie <a href="/kopacky/">kopačky</a>, od dětských modelů po pánské a unisex provedení. Průvodce vysvětluje, co znamenají názvy řad Magnetico a Shadow a označení Club, Select, Pro a Elite, jak se liší obuv na přírodní trávu od turfů, jak vybrat velikost a jak značku srovnat s <a href="/kopacky-nike/">Nike</a>, <a href="/kopacky-adidas/">Adidasem</a> nebo <a href="/kopacky-puma/">Pumou</a>. Přehled najdete i v tabulce zkratek podložek a poznáte, které kopačky se hodí pro trénink na umělce a které na zápas na tvrdé trávě.</p>',
    guide='<h2>Sortiment Under Armour mezi kopačkami</h2>'
          '<p>Under Armour vznikla jako značka sportovního prádla a později rozšířila nabídku na obuv a výbavu pro běh, trénink a další sporty. Mezi kopačkami není tak široká jako Nike, Adidas nebo Puma, a proto se její modely snáze přehlédnou. Dobře se však hodí pro hráče, kteří chtějí vybrat obuv mimo hlavní proud a nechtějí se omezovat jen na nejčastěji vídané tvary. V aktuální nabídce se opakují dvě hlavní řady: <strong>Magnetico</strong> a <strong>Shadow</strong>. Každá se prodává ve více úrovních a provedeních pro dospělé i pro děti.</p>'
          '<p>Při výběru není třeba pamatovat si technické popisy. Důležité je pochopit, kdo hraje, na jakém povrchu a jak často. Zbytek rozhodne pocit v noze a vaše zkušenost s předchozími kopačkami.</p>'
          '<h2>Řady Magnetico a Shadow</h2>'
          '<p>Názvy řad se napříč sezónami opakují s číslem generace, třeba Magnetico Select 4 nebo 6, Shadow Select 4. Číslo označuje pořadí modelu, vyšší tedy obvykle znamená novější vydání. Staršího ročníku se vyplatí hledat, pokud vám nevadí, že nemá nejnovější vzhled; funkční rozdíly mezi sousedními generacemi bývají menší než rozdíl mezi úrovněmi řady. Dobrý přehled dává tabulka.</p>'
          + T(['Označení', 'Co obvykle znamená', 'Pro koho'], [
              ['Club', 'základní úroveň řady, odolný svršek', 'začátečníci, děti a pravidelný trénink'],
              ['Select', 'střední úroveň, vyvážená cena a provedení', 'rekreační a amatérští hráči na pravidelné zápasy'],
              ['Pro', 'vyšší úroveň, lehčí a přiléhavější provedení', 'ambiciózní hráči, kteří hrají každý týden'],
              ['Elite', 'nejvyšší úroveň řady', 'ti, kdo chtějí nejlepší provedení a nejlehčí váhu'],
              ['JR', 'junior, dětská velikost', 'děti a mladiství, kteří rostou'],
              ['AMP, RCS', 'doplňkové označení konkrétní edice', 'podle popisu prodejce']]) +
          '<p>Přesný popis každé edice si vždy přečtěte na stránce konkrétního modelu. Značka u každé generace mění materiál svršku a tvar kopaček, a proto se doporučení „vezměte Pro, je lepší“ nedá brát doslova. Pro většinu amatérských hráčů je střední úroveň praktičtější než nejdražší kus, protože se při tréninku nezničí tak rychle.</p>'
          '<h2>Podrážky: FG, turf a další povrchy</h2>'
          '<p>Nejčastější chybou při nákupu kopaček je špatná podrážka na špatném povrchu. Značka Under Armour nabízí především dvě provedení: <strong>FG</strong> pro přírodní trávu a <strong>turf</strong> pro umělou trávu s krátkým vlasem a pro tvrdé hřiště.</p>'
          + T(['Zkratka', 'Povrch', 'Poznámka'], [
              ['FG', 'pevná přírodní tráva', 'kolíky se zaboří, nejběžnější zápasová podrážka'],
              ['AG', 'umělá tráva', 'kratší a hustší kolíky, méně namáhají kloub'],
              ['SG', 'měkká a rozmoklá tráva', 'delší vyměnitelné kolíky, pro blátivý terén'],
              ['MG', 'kombinovaný povrch', 'kompromis pro trávu i umělku'],
              ['Turf (TF)', 'umělka, tvrdá zem, asfalt', 'mnoho malých hlaviček, nejlepší na trénink'],
              ['IN', 'hala, parkety', 'hladká podrážka bez kolíků']]) +
          '<p>Pokud hrajete většinu zápasů na přírodní trávě, zvolte FG. Pokud trénujete na umělce nebo na školním hřišti, jsou turfy lepší a levnější na opotřebení. Kopačky FG na tvrdém povrchu rychle ztrácejí podrážku a zvyšují zátěž na kolena a kotníky. Naopak turf na měkké trávě málo drží, což zhoršuje změny směru.</p>'
          '<h2>Jak vybrat velikost kopaček Under Armour</h2>'
          '<p>Kopačka musí sedět těsněji než běžná sportovní obuv, ale nesmí tlačit. Prsty se mají v klidu lehce dotýkat špičky nebo mít jen malou rezervu. Příliš velké kopačky způsobují, že noha klouže, takže puchýře jsou častější než u malých. Nejlepší je změřit délku chodidla a porovnat ji s tabulkou konkrétního obchodu. Velikosti různých značek se mohou lišit, a proto nepřebírejte číslo z jiných kopaček bez kontroly.</p>'
          '<ul><li><strong>Změřte chodidlo večer</strong>, kdy je mírně zduřené.</li>'
          '<li><strong>Porovnejte délku stélky v centimetrech</strong> mezi značkami, ne jen číslo na krabici.</li>'
          '<li><strong>Vezměte ponožky, ve kterých hrajete</strong>, ne tenké ponožky z obchodu.</li>'
          '<li><strong>Zkuste obě nohy</strong>, protože každé chodidlo je trochu jiné.</li>'
          '<li><strong>Nekupujte děti o dvě čísla větší</strong>, zbytečně se jim v nich klouže a roste riziko podvrtnutí.</li></ul>'
          '<p>Kožené nebo kožené imitace svršky se po několika hodinách rozšlapou, syntetické materiály drží tvar více. Pokud váháte mezi dvěma velikostmi, bývá bezpečnější vzít menší u měkkého svršku a větší u tuhého.</p>'
          '<h2>Pro koho jsou kopačky Under Armour</h2>'
          '<p><strong>Dospělí amatéři.</strong> Střední úroveň řady vám v rekreační lize poskytne všechno, co potřebujete. Teprve pokud hrajete soutěžně a chcete lehčí model, má smysl uvažovat o vyšší úrovni.</p>'
          '<p><strong>Děti a mladiství.</strong> Dětské modely označené Jr mají menší velikosti a obvykle pevnější konstrukci. Děti rychle rostou, a proto se vyplatí vybrat model s rozumným poměrem ceny a kvality. Širší výběr dětské obuvi je na stránce <a href="/detske-kopacky/">dětské kopačky</a>.</p>'
          '<p><strong>Trénink na umělce.</strong> Turfy Under Armour se hodí jako druhý pár pro tréninky. Chrání zápasové kopačky před zbytečným opotřebením a umožňují hrát na tvrdém povrchu bez rizika vyvrtnutí na dlouhých kolících.</p>'
          '<h2>Srovnání s ostatními značkami</h2>'
          '<p>Největší nabídku najdete u značek <a href="/kopacky-nike/">Nike</a>, <a href="/kopacky-adidas/">Adidas</a> a <a href="/kopacky-puma/">Puma</a>, které mají i nejvíc dětských a juniorských modelů. Menší výrobci jako <a href="/mizuno-kopacky/">Mizuno</a>, <a href="/joma-kopacky/">Joma</a> a <a href="/new-balance-kopacky/">New Balance</a> sázejí na odlišný tvar nebo praktický poměr ceny a výbavy. Under Armour patří do skupiny značek, které se hodí těm, kdo neřeší, jestli mají logo stejné jako spoluhráč, a hledají odlišný střih i design. Pokud chcete barevnou variantu, prohlédněte si třeba <a href="/ruzove-kopacky-nike/">růžové kopačky Nike</a> jako příklad, jak výrazná barva ovlivňuje celkový dojem.</p>'
          '<p>Při srovnávání nejsou rozhodující loga, ale tvar špičky, šířka v přední části chodidla, výška v oblasti kotníku a typ podrážky. Kopačky, které sedí jednomu hráči, mohou druhému tlačit. Proto se vyplatí zkoušet, nebo vybírat v obchodě, který přijímá vrácení.</p>'
          '<h2>Kolik párů kopaček potřebujete</h2>'
          '<p>Hráč, který chodí na trénink dvakrát týdně a o víkendu na zápas, snadno zničí jeden pár dřív, než by musel. Praktické je mít dva páry: <strong>zápasové kopačky</strong> na přírodní trávu a <strong>turfy</strong> na trénink na umělce nebo tvrdém hřišti. Zápasové pak vydrží déle a zůstanou tvarově vyladěné, zatímco tréninkový pár snáší ztráty, které zápasovému nesvědčí. Pokud hrajete výhradně na umělce, vystačíte si s turfy nebo s modelem pro umělou trávu a druhý pár nepotřebujete.</p>'
          '<p>Při výběru druhého páru nemusíte brát stejnou úroveň řady. Na trénink je často rozumnější jednodušší model označený Club nebo Select, který nevadí zničit. Pokud chcete mít oba páry stejného tvaru, vezměte stejnou řadu v obou provedeních podrážky, a vaše noha si zvykne na jeden tvar.</p>'
          '<h2>Jak kopačky rozchodit</h2>'
          '<p>Nové kopačky nikdy neberte rovnou na důležitý zápas. První dvě tři hodiny je noste doma nebo na lehkém tréninku, aby se svršek přizpůsobil tvaru chodidla. Pokud tlačí v konkrétním místě, zkuste je na chvíli navléknout s tlustší ponožkou a nechat při chůzi změknout. Hodí se i nalepit náplast na místa, kde hrozí puchýř, třeba na patu. Obuv, která po několika hodinách stále tlačí, je pravděpodobně špatná velikost nebo špatný tvar a vrátit ji je rozumnější než ji trpělivě rozchodit.</p>'
          '<h2>Péče o kopačky</h2>'
          '<p>Po zápase očistěte podrážku od hlíny a trávy kartáčem a svršek otřete vlhkým hadrem. Mokré kopačky sušte při pokojové teplotě, nikoli u radiátoru, protože teplo deformuje lepené spoje. Vycpěte je novinami, které vsáknou vlhkost. Kopačky nenoste v autě ani na batohu zabalené v mokrém, rychle by zapáchaly. Pokud potřebujete kvalitní tréninkovou obuv na jiné sporty, najdete ji v kategorii <a href="/treninkova-obuv/">fitness a tréninková obuv</a>.</p>'
          '<p>K výbavě patří i chrániče, štulpny a míč. Nabídku najdete v kategoriích <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>, <a href="/fotbalove-mice/">fotbalové míče</a> a v přehledu <a href="/fotbal/">fotbal</a>. Značku si můžete prohlédnout na stránce <a href="/znacka/under-armour/">Under Armour</a>, kde najdete i oblečení.</p>',
    faq=[
        ('Jsou kopačky Under Armour kvalitní?', 'Under Armour je zavedená sportovní značka a její kopačky patří do běžné nabídky pro amatérské i soutěžní hráče. Kvalita se liší podle úrovně řady, proto se orientujte podle označení Club, Select, Pro a Elite a podle použití.'),
        ('Čím se liší řady Magnetico a Shadow?', 'Obě řady se prodávají v několika úrovních a generacích. Konkrétní rozdíly ve tvaru, svršku a pocitu v noze popisuje prodejce u každého modelu. Nejlepší je porovnat popisy a při zkoušení sledovat tvar špičky a šířku v přední části.'),
        ('Co znamená FG u kopaček?', 'Zkratka FG znamená firm ground, tedy pevnou přírodní trávu. Podrážka s kolíky se zaboří do povrchu a zajistí oporu při změně směru. Na tvrdé umělce se FG hodí hůř, kde je lepší turf nebo AG.'),
        ('Kdy zvolit turfy místo kopaček na trávu?', 'Turfy jsou určeny pro umělou trávu s krátkým vlasem, hřiště s tvrdým povrchem a trénink. Mají mnoho krátkých hlaviček místo kolíků, takže méně zatěžují kloub a nejsou tak náchylné k opotřebení.'),
        ('Jakou velikost kopaček Under Armour koupit?', 'Změřte délku chodidla a porovnejte ji s tabulkou prodejce. Kopačka má sedět těsně, ale bez tlaku, s malou rezervou u prstů. Jednotlivé značky nemají shodné velikosti, takže číslo z jiných kopaček nepřebírejte automaticky.'),
        ('Hodí se kopačky Under Armour pro děti?', 'Ano, v nabídce jsou modely označené Jr s dětskými velikostmi. Pro děti volte pevnou konstrukci a správnou podrážku podle hřiště. Dítě nemá nosit o dvě čísla větší kopačky, hrozí mu podvrtnutí.'),
        ('Jak dlouho vydrží kopačky?', 'Záleží na povrchu, četnosti hraní a péči. Na tvrdém povrchu se podrážka opotřebuje mnohem rychleji než na trávě. Pravidelné čištění a správné sušení životnost výrazně prodlouží.'),
        ('Mohu hrát v kopačkách FG na umělce?', 'Dá se to, ale není to ideální. Dlouhé kolíky se v umělé trávě zasekávají a zatěžují kolena a kotníky. Lepší jsou kopačky s označením AG nebo turfy, zvlášť pokud na umělce trénujete pravidelně.'),
        ('Jak vyčistit a vysušit kopačky?', 'Seškrábněte hlínu z podrážky, svršek otřete vlhkým hadříkem a vysušte při pokojové teplotě. Nesušte je u radiátoru ani na slunci, protože teplo poškozuje lepení a materiál. Pomůže vycpání novinovým papírem.'),
        ('Čím se Under Armour liší od Nike nebo Adidasu?', 'Největší rozdíl je v sortimentu a tvaru. Nike, Adidas a Puma mají širší nabídku a víc dětských modelů, Under Armour nabízí užší výběr a odlišný design. Rozhoduje spíš pohodlí v noze než logo.'),
    ])

# ------------------------------------------------------------------ gymbeam-leginy
NEW['gymbeam-leginy'] = dict(
    title='GymBeam leginy: střihy, materiály a výběr do posilovny',
    desc='GymBeam leginy: bezešvé, kompresní i běžecké modely, jak vybrat velikost a materiál, jak otestovat nepropustnost a jak je srovnat s Nike a Under Armour.',
    intro='<p>GymBeam je slovenská značka a internetový obchod zaměřený na fitness, takže leginy dělá především pro posilování, cvičení a běh. V nabídce najdete dámské i pánské střihy, bezešvé a kompresní materiály a modely se šňůrkou nebo kapsou. '
          'Na této stránce jsou leginy GymBeam z kategorie <a href="/leginy/">legíny</a>. Průvodce vysvětluje, jak se liší bezešvé a šité modely, co znamená vysoký pas a komprese, jak vybrat velikost a materiál, jak poznat, že legíny nejsou průsvitné při dřepu, a jak o ně pečovat. Najdete zde i srovnání s dalšími sportovními značkami a odkazy na barevné a pánské varianty, takže si můžete snadno vybrat to, co vám bude vyhovovat při tréninku.</p>',
    guide='<h2>Co GymBeam v legínách nabízí</h2>'
          '<p>GymBeam vyrostl z prodeje sportovní výživy a doplňků a postupně přidal vlastní oblečení. Leginy patří k jeho nejviditelnějšímu zboží, protože se hodí na všechno od posilování po jógu. V nabídce se opakují názvy řad jako <strong>Limitless, Fierce, BEAT, Pulse, Core a FIT</strong>. Každá řada má trochu jiný střih, šířku pasu a materiál, proto se při výběru vyplatí číst popis konkrétního modelu a neřídit se jen názvem.</p>'
          '<p>Pro orientaci pomůže třídění podle použití. Posilování a cvičení v hale vyžaduje pružný materiál, který se při dřepu neprosvítá. Běh vyžaduje lehkou tkaninu se šňůrkou nebo kapsou na klíč. Pro jógu a jemnější cvičení se hodí měkký materiál bez švů, který neškrtí. Pánské modely bývají kompresní nebo volnější, aby se daly nosit pod kraťasy.</p>'
          '<h2>Bezešvé, kompresní a klasické střihy</h2>'
          + T(['Typ', 'Charakteristika', 'Hodí se na'], [
              ['Bezešvé', 'pleteno v jednom kuse, hladký povrch bez tlustých švů', 'posilování, jóga, celodenní nošení'],
              ['Kompresní', 'pevnější materiál, stahuje svaly', 'těžký trénink, běh, pánské modely'],
              ['S vysokým pasem', 'sahá nad pupík, drží břicho', 'dřepy, cvičení, ženy, které nechtějí neustále upravovat pas'],
              ['Běžecké', 'lehký materiál, šňůrka a kapsa', 'běh, rychlá chůze, venkovní trénink'],
              ['Flare', 'rozšířená nohavice od kolen', 'jóga, pilates, volnočasové nošení'],
              ['Se zpevněným pasem', 'širší pas, který neroluje', 'intenzivní cvičení, skoky']]) +
          '<p>Bezešvé leginy se vyrábějí pletením a materiál se přizpůsobuje tělu bez výrazných švů, takže nedrásají pokožku při dlouhém tréninku. Nevýhodou může být menší rozsah velikostí a méně pevný materiál. Kompresní modely drží svaly pevněji, ale mohou být dlouhé na oblékání. Klasické šité leginy bývají univerzálnější a lépe se přizpůsobí různým postavám.</p>'
          '<h2>Materiál a nepropustnost</h2>'
          '<p>Většina sportovních legín je z polyamidu (nylonu) nebo polyesteru s příměsí elastanu. Polyamid je měkčí a příjemnější na dotek, polyester rychle schne a snáší praní. Příměs elastanu zajišťuje pružnost, ale po letech se materiál unaví. Čím vyšší podíl elastanu, tím větší stažení a pružnost. Bavlněné legíny jsou pohodlné na doma, ale v posilovně nasáknou potem a hůře schnou.</p>'
          '<p>Nejčastější starost při koupi je, zda se materiál při dřepu neprosvítá. Zkoušku je potřeba provést doma při denním světle:</p>'
          '<ol><li>Obléknout si leginy a stoupnout si před zrcadlo.</li>'
          '<li>Udělat hluboký dřep s koleny mírně do stran.</li>'
          '<li>Podívat se zezadu na materiál nad stehny a na zadnici, zda neprosvítá barva spodního prádla.</li>'
          '<li>Zkontrolovat, zda se pas neroluje a legíny nesjíždějí.</li>'
          '<li>Pokud něco nevyhovuje, vyměnit nebo vrátit model, dokud jsou nenošené.</li></ol>'
          '<p>Tmavé barvy, jako černá nebo šedá, prosvítají méně než světlé tóny. Pro víc informací o barevné variantě se podívejte na stránku <a href="/cerne-leginy/">černé legíny</a>, která pomáhá s výběrem nejuniverzálnějšího odstínu, nebo na <a href="/hnede-leginy/">hnědé legíny</a> pro jemnější barvy.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Legíny mají sedět přiléhavě, ale nesmí tlačit v pase ani se zařezávat do stehen. Základem je změřit obvod pasu a boků a porovnat je s tabulkou. Pokud jste mezi velikostmi, u bezešvých materiálů volte menší, protože se vytahují, a u pevných kompresních volte větší. Vysoký pas se musí dobře opřít o tělo, aby se při pohybu nesvinoval.</p>'
          '<ul><li><strong>Změřte obvod pasu a boků</strong> a porovnejte jej s tabulkou konkrétního modelu.</li>'
          '<li><strong>Zkontrolujte délku nohavic</strong>, protože zkrácené 7/8 nebo 3/4 modely sedí jinak u vysokých a nízkých postav.</li>'
          '<li><strong>Zohledněte typ cvičení</strong>: na dřepy a skoky potřebujete pevnější úchop než na jógu.</li>'
          '<li><strong>Zkuste pohyb</strong> – dřep, výpad, předklon. Legíny, které se při něm posouvají, vám při tréninku budou překážet.</li></ul>'
          '<h2>Pánské a dámské leginy</h2>'
          '<p>Dámské modely mají tvarovanější pas a boky, často vysoký pas a zdobení v pase nebo na zádech, jako střih V-back. Pánské modely jsou rovnější, často kompresní a mívají kapsu na telefon nebo klíč. Pánské legíny se nosí samostatně nebo pod kraťasy při tréninku a běhu. Širší výběr najdete na stránce <a href="/panske-leginy/">pánské legíny</a>. Stejně jako u oblečení obecně není rozdělení striktní, a pokud vám sedí model z druhé skupiny, můžete ho klidně nosit.</p>'
          '<h2>Do jakého tréninku se které leginy hodí</h2>'
          '<ul><li><strong>Dřepy a mrtvý tah:</strong> potřebujete pevný, neprůsvitný materiál a vysoký pas, který se neroluje. Bezešvé a kompresní modely tady obvykle fungují nejlépe.</li>'
          '<li><strong>Kardio a skupinové lekce:</strong> hodí se lehký a prodyšný materiál, který rychle schne, protože se při skocích a rychlém tempu hodně potíte.</li>'
          '<li><strong>Jóga a pilates:</strong> dává smysl měkký materiál bez tlustých švů a širší pas, který netlačí na břicho při předklonu.</li>'
          '<li><strong>Běh venku:</strong> praktická je šňůrka v pase, kapsa na klíč a materiál, který nechytá vodu. V chladu se leginy nosí s další vrstvou.</li>'
          '<li><strong>Chladné dny:</strong> pod volné kalhoty nebo přes ně se obléká druhá vrstva, takže sportovní leginy fungují jako základ a ne jako jediná ochrana.</li></ul>'
          '<h2>Kombinace s topem a podprsenkou</h2>'
          '<p>Vysoký pas se nejlépe kombinuje s kratším topem nebo sportovní podprsenkou, protože hranice pasu zůstane viditelná a oblečení nepřeskakuje. Delší tričko zakryje boky, hodí se pro ty, kdo preferují volnější siluetu. U jednobarevných legín se dobře nosí vzorované svršky a naopak. Pro jednotný styl můžete zvolit stejnou barvu legín a topu, což funguje obzvlášť u bezešvých setů. Nabídku podprsenek najdete v kategorii <a href="/sportovni-podprsenky/">sportovní podprsenky</a>.</p>'
          '<h2>Barvy a vzory</h2>'
          '<p>Černé a tmavé odstíny jsou praktické, protože maskují pot, otěry a prosvítání. Světlé a pastelové tóny vypadají svěže, ale jsou náročnější na údržbu a vyžadují pevnější materiál. Barevné modely se hodí do skupinových lekcí, kde chcete vyniknout. Mějte na paměti, že tmavé materiály na slunci hřejí víc, takže na letní běh je lepší vybrat světlejší odstín.</p>'
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>Pokud chcete porovnat nabídku s velkými sportovními firmami, podívejte se na <a href="/nike-leginy/">legíny Nike</a> a <a href="/under-armour-leginy/">legíny Under Armour</a>. Velké značky nabízejí širší výběr běžeckých modelů a modelů pro týmové sporty. GymBeam se soustředí na fitness a posilování, proto má bohatší nabídku bezešvých a kompresních materiálů. Značku si můžete prohlédnout i na stránce <a href="/znacka/gymbeam/">GymBeam</a>, kde najdete další oblečení, a pro doplnění tréninku nabídku <a href="/sportovni-podprsenky/">sportovních podprsenek</a> a <a href="/fitness/">fitness</a>.</p>'
          '<h2>Sety, kapsy a drobné detaily</h2>'
          '<p>Praktickou drobností je kapsa v pasu nebo na boku nohavice, do které se vejde telefon, karta nebo klíč. U legín bez kapes se hodí pouzdro na paži nebo pásek. Nezapomínejte na reflexní prvky, pokud běháte za šera. Kdo chce sladěný vzhled, najde v nabídce také sety, kde top a leginy mají stejný materiál a odstín, což u bezešvých modelů vypadá nejlépe. Při nákupu setu zkontrolujte, zda lze obě části koupit i samostatně v jiné velikosti, protože horní a dolní polovina těla nemusí mít stejné míry.</p>'
          '<h2>Péče o sportovní leginy</h2>'
          '<p>Materiál vydrží déle, pokud se pere naruby při nízké teplotě, nejlépe v praní na šetrný program. Nepoužívejte aviváž, která ucpává vlákna a snižuje schopnost odvádět pot. Také se nehodí do sušičky, kde elastan stárne. Sušte je volně rozložené, mimo přímé slunce. Nenoste je při aktivitách, při kterých se otírají o hrubý povrch, třeba při lezení po betonu nebo při cvičení na drsné podložce, protože se vytahují oka.</p>'
          '<p>Po tréninku legíny nenechávejte dlouho ve vlhké tašce. Pot a vlhkost v kombinaci s teplem způsobují zápach, který se obtížně odstraňuje. Dobře se osvědčilo aspoň krátké vyvětrání a praní hned po cvičení.</p>'
          '<h2>Kontrolní seznam před nákupem</h2>'
          '<ol><li>Rozhodněte, zda hledáte posilování, běh, nebo jógu.</li>'
          '<li>Zvolte materiál podle použití: bezešvý, kompresní, nebo klasický.</li>'
          '<li>Porovnejte velikost s tabulkou, ne jen číslem z jiných značek.</li>'
          '<li>Doma proveďte zkoušku dřepu proti světlu.</li>'
          '<li>Porovnejte stejný model ve více obchodech a sledujte dostupnost velikostí.</li></ol>',
    faq=[
        ('Jsou leginy GymBeam vhodné do posilovny?', 'Ano, značka se na fitness zaměřuje. V nabídce jsou bezešvé a kompresní modely s vysokým pasem, které se hodí na dřepy a těžší cvičení. Rozhodující je materiál a střih konkrétního modelu, proto si přečtěte popis.'),
        ('Prosvítají leginy při dřepu?', 'Může se to stát hlavně u světlých barev a tenkých materiálů. Doma si udělejte dřep před zrcadlem při denním světle a podívejte se zezadu. Tmavé odstíny a pevnější pleteniny prosvítají méně.'),
        ('Jak vybrat velikost legín GymBeam?', 'Změřte obvod pasu a boků a porovnejte je s tabulkou u modelu. Legíny mají sedět přiléhavě, ale netlačit. Mezi velikostmi volte menší u elastických bezešvých modelů a větší u pevných kompresních.'),
        ('Čím se liší bezešvé leginy od klasických?', 'Bezešvé se pletou v jednom kuse a nemají tlusté švy, takže nedrásají pokožku. Klasické šité modely jsou univerzálnější a lépe se přizpůsobí různým postavám, mají však výraznější švy.'),
        ('K čemu je vysoký pas?', 'Vysoký pas drží břicho a stabilizuje legíny při pohybu, takže se neroluje a nesjíždí. Hodí se na dřepy, jógu a cvičení v posilovně, kde často měníte pozice.'),
        ('Mohu leginy GymBeam použít na běhání?', 'Ano, pokud zvolíte lehčí model, nejlépe se šňůrkou v pase a kapsou na klíč nebo telefon. Pro delší běh se vyplatí materiál, který rychle schne a nemá drsné švy v místech tření.'),
        ('Jak prát sportovní leginy?', 'Perte je naruby při nízké teplotě, na šetrný program a bez aviváže. Aviváž ucpává vlákna a zhoršuje odvod potu. Sušte volně rozložené mimo přímé slunce, sušička zkracuje životnost elastanu.'),
        ('Jsou pánské leginy jen pro běh?', 'Ne. Pánské leginy se nosí na běh, trénink v posilovně, pod kraťasy i v chladnu. Kompresní modely pevněji drží svaly, volnější střih se hodí na vyjížďky nebo volný čas.'),
        ('Jak se GymBeam liší od Nike a Under Armour?', 'Nike a Under Armour nabízejí širší sortiment pro týmové sporty a běh. GymBeam se soustředí na fitness a posilování a má bohatší výběr bezešvých a kompresních legín. Který je lepší, rozhodne střih a pocit při pohybu.'),
    ])

# ------------------------------------------------------------------ detske-lyzarske-helmy
NEW['detske-lyzarske-helmy'] = dict(
    title='Dětské lyžařské helmy: velikost, bezpečnost a výběr',
    desc='Dětské lyžařské helmy: jak změřit obvod hlavy, jak helmu nastavit a vyzkoušet, co znamená MIPS a norma EN 1077 a které značky nabízejí dětské modely.',
    intro='<p>Dětská lyžařská helma musí v první řadě sedět. Dítě v příliš velké helmě má falešný pocit bezpečí, protože se při pádu posune a nechrání to, co má. Tato stránka zobrazuje dětské a juniorské modely z kategorie <a href="/lyzarske-helmy/">lyžařské helmy</a>. '
          'Průvodce vysvětluje, jak změřit obvod hlavy, kterou velikost zvolit, jak helmu nastavit a zkontrolovat, co znamená norma EN 1077, systém MIPS a typ ventilace a jak spojit helmu s brýlemi. Dozvíte se také, jak poznat, že je čas helmu vyměnit, co dělat po pádu, a které značky nabízejí dětské modely. Pokud vybavujete dítě na celou zimu, navazují odkazy na <a href="/detske-lyzarske-bryle/">dětské lyžařské brýle</a>, boty a rukavice.</p>',
    guide='<h2>Proč dítě potřebuje vlastní dětskou helmu</h2>'
          '<p>Dětská helma není zmenšená dospělá. Má jiné proporce, nižší hmotnost, hlubší nasazení a často i měkčí vnitřní výstelku, aby seděla na menší hlavě. Hlava dítěte je vzhledem k tělu relativně větší a těžší, a proto je hmotnost helmy pro krk důležitá. Lehká helma s dobrým nastavením se při dlouhém dni na sjezdovce nestane zátěží, kterou děti sundávají.</p>'
          '<p>Z toho plyne i druhé pravidlo: nekupujte velkou helmu, do které dítě „doroste“. Rostoucí hlava se sice za rok zvětší, ale helma, která nyní viklá, nechrání. Příjemnější a bezpečnější je koupit helmu na jednu až dvě sezóny a pak ji vyměnit.</p>'
          '<h2>Jak změřit obvod hlavy a vybrat velikost</h2>'
          '<p>Velikosti dětských helem se uvádějí v rozsahu obvodu hlavy v centimetrech, například 48–52 nebo 52–56. Označení S, M a L se mezi značkami liší, a proto je číslo v centimetrech spolehlivější. Obvod změřte krejčovským metrem vodorovně kolem hlavy asi dva prsty nad obočím a nad ušima, v nejširším místě. Výsledek porovnejte s tabulkou konkrétního výrobce.</p>'
          + T(['Zkouška', 'Jak ji provést', 'Co má být výsledkem'], [
              ['Posun', 'helmu nasadit a zatřást hlavou do stran a dopředu', 'helma se nehýbe nezávisle na hlavě'],
              ['Výška na čele', 'zkontrolovat, kde končí přední hrana', 'asi dva prsty nad obočím, ne na čele'],
              ['Podbradní pásek', 'zapnout a vsunout prst pod bradu', 'prst se vejde, ale pásek netlačí na krk'],
              ['Nastavení', 'dotočit kolečko nebo systém úpravy', 'helma přiléhá po celém obvodu'],
              ['Brýle', 'nasadit brýle k helmě', 'pásek brýlí sedí a mezi hranou a brýlemi není velká mezera'],
              ['Pohodlí', 'ponechat helmu 15 minut', 'žádné tlakové body na čele a spáncích']]) +
          '<p>Většina dětských helem má vnitřní nastavení obvodu, obvykle kolečko vzadu nebo pásek. Díky němu se dá helma upravit o několik centimetrů a využít i s čepicí. Vnitřek helmy dítě nemá mít pocit, že ho tlačí, a zároveň se helma nesmí kývat. Pokud musí kolečko dotáhnout do krajní polohy, helma je velká.</p>'
          '<h2>Norma EN 1077, MIPS a ventilace</h2>'
          '<p>Lyžařské helmy se v Evropě zkoušejí podle normy <strong>EN 1077</strong>, která má dvě třídy: A a B. Třída A zahrnuje požadavky na větší krytí, třída B se hodí pro lehčí provedení s větším odvětráním. Značení najdete uvnitř helmy nebo v popisu produktu. Pro děti volte model s jasně uvedenou normou, ne bezejmennou helmu bez označení. Helma pro cyklistiku je jiná kategorie a lyžařskou nenahradí.</p>'
          '<p>Některé modely mají <strong>MIPS</strong>, což je vnitřní vrstva, která se při šikmém nárazu může mírně pootočit vůči hlavě. Tento systém je dnes v nabídce běžný, třeba u Alpiny, Uvexu nebo Smithu. MIPS může přidat další vrstvu ochrany, ale správná velikost a nastavení jsou důležitější. Helma s MIPS, která viklá, je horší než helma bez ní, která sedí dokonale.</p>'
          '<p>Ventilace se u dětských helem často řeší otvory, které se dají zavřít. Dítě se na lyžích zahřeje stejně jako dospělý, a proto jsou otvory užitečné. Lehká čepice pod helmou je obvykle zbytečná, pokud není opravdu zima; tenká kukla nebo nákrčník ale pomůže. Teplejší doplňky najdete v kategorii <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>.</p>'
          '<h2>Helma a brýle musí ladit</h2>'
          '<p>Brýle a helma tvoří systém. Pásek brýlí má sedět na helmě a hrana helmy nemá tlačit na rám. Mezera mezi helmou a brýlemi může být zdrojem zimy na čele a omrzlin. Některé helmy mají hledí nebo štít, který nahrazuje brýle; pro menší děti jsou praktické, protože se nemusí řešit nasazování brýlí. Dobře fungují i tam, kde dítě brýle odmítá. Ostatní modely se kombinují s <a href="/detske-lyzarske-bryle/">dětskými lyžařskými brýlemi</a> nebo s obecnou nabídkou <a href="/lyzarske-bryle/">lyžařských brýlí</a>.</p>'
          '<h2>Značky dětských helem v nabídce</h2>'
          '<p>Největší výběr dětských modelů mají ' + B(('alpina', 'Alpina'), ('uvex', 'Uvex')) + ', které se zaměřují na helmy i brýle pro děti. Velké lyžařské značky jako ' + B(('head', 'Head'), ('rossignol', 'Rossignol'), ('atomic', 'Atomic'), ('salomon', 'Salomon'), ('blizzard', 'Blizzard')) + ' nabízejí juniorské modely pro děti, které už jezdí samostatně. Další možnosti pak představují ' + B(('smith', 'Smith'), ('poc', 'Poc'), ('scott', 'Scott'), ('cairn', 'Cairn'), ('bolle', 'Bollé')) + '. Praktické a cenově dostupné řady mají také ' + B(('etape', 'Etape'), ('relax', 'Relax'), ('laceto', 'Laceto'), ('arcore', 'Arcore')) + '. U všech značek rozhoduje velikost, nastavení a norma, nikoli logo.</p>'
          '<h2>První dny na sjezdovce a lyžařská škola</h2>'
          '<p>Pro děti ve školce nebo v lyžařské škole je helma nejdůležitější v prvních dnech, kdy padají nejčastěji a nejméně předvídatelně. Instruktoři helmu u malých lyžařů zpravidla požadují. Připravte dítě tak, že si doma helmu vyzkouší, nasadí s brýlemi a zvykne si na pásek pod bradou. Dítě, které zná její pocit z domova, ji na svahu neodmítne. Označte vnitřek helmy jménem nebo kontaktem, protože v šatně se rychle zamění.</p>'
          '<h2>Pokročilejší děti: park, závody a freeride</h2>'
          '<p>Děti, které jezdí rychleji nebo v parku, ocení helmu s lepším krytím uší a pevnějším uchycením. Závodní tréninky mívají vlastní požadavky na helmy, proto se řiďte pokyny oddílu. Pro mladé freeridery je dobré zvolit model s vyšším krytím týlu. V parku a při skocích se na lyžích hodí hlubší tvar, který chrání i spánky. Taková helma bývá těžší, a proto je dobré ji nejdřív zkusit v klidu doma.</p>'
          '<h2>Postup nasazení krok za krokem</h2>'
          '<ol><li>Povolte nastavení obvodu a nasaďte helmu rovně na hlavu, ne nahoru nebo dozadu.</li>'
          '<li>Zapněte podbradní pásek tak, aby pod bradou zůstal prostor na jeden prst.</li>'
          '<li>Dotáhněte kolečko vzadu, dokud helma nepřiléhá po celém obvodu.</li>'
          '<li>Zatřeste hlavou a zkontrolujte, že se helma nehýbe nezávisle na ní.</li>'
          '<li>Nasaďte brýle a zkontrolujte, že pásek sedí na helmě.</li></ol>'
          '<h2>Kdy helmu vyměnit</h2>'
          '<ul><li><strong>Po silném nárazu:</strong> vnitřní pěnová vrstva se mohla zničit, i když vnější skořepina vypadá celá.</li>'
          '<li><strong>Po několika sezónách:</strong> materiál stárne, stejně jako výstelka a pásek.</li>'
          '<li><strong>Když dítě vyrostlo:</strong> helma už nesedí a nastavení je na hranici rozsahu.</li>'
          '<li><strong>Při viditelném poškození:</strong> praskliny, odlupující se výstelka nebo poškozený pásek jsou důvodem k výměně.</li>'
          '<li><strong>U použité helmy z druhé ruky:</strong> neznáte její historii, takže riziko skrytého poškození je vyšší.</li></ul>'
          '<p>Helmu skladujte v suchu, nepřikrývejte ji těžkými věcmi a nepřevážejte ji v kufru pod zavazadly. Čistěte ji vlažnou vodou a jemným mýdlem, bez rozpouštědel, která mohou poškodit materiál.</p>'
          '<h2>Jak dítě přesvědčit, aby helmu nosilo</h2>'
          '<p>Nejčastější problém není výběr, ale přesvědčení dítěte, aby helmu nosilo. Pomáhá, když si dítě barvu a vzor vybere samo, helma dobře sedí a je pohodlná. Pro menší děti fungují veselé vzory se zvířátky, starší děti ocení decentní provedení. Ukažte příklad: když helmu nosí rodiče, děti ji berou jako samozřejmost. Dítě by mělo helmu nasazovat před každým výjezdem, i v lyžařské školce.</p>'
          '<h2>Kompletní výbava pro malého lyžaře</h2>'
          '<p>Helma je jen jedna část. Děti potřebují teplou vrstvu pod oblečením, rukavice a pevné boty. Nabídku najdete v kategoriích <a href="/detske-lyzarske-boty/">dětské lyžařské boty</a>, <a href="/detske-lyzarske-rukavice/">dětské lyžařské rukavice</a>, <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a> a <a href="/lyzarske-kombinezy/">lyžařské kombinézy a overaly</a>. Širší přehled je ve stránce <a href="/lyzarske-obleceni/">lyžařské a snowboardové oblečení</a>. Pokud dítě používá helmu i na kole, mějte na paměti, že jde o jinou kategorii a pro cyklistiku slouží <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</p>',
    faq=[
        ('Jak vybrat velikost dětské lyžařské helmy?', 'Změřte obvod hlavy dva prsty nad obočím a nad ušima a porovnejte s tabulkou výrobce. Helma má přiléhat po celém obvodu, nehýbat se při zatřesení hlavou a podbradní pásek nesmí tlačit. Velikosti S, M a L se mezi značkami liší, spolehněte se na centimetry.'),
        ('Může si dítě koupit helmu větší, aby mu vydržela déle?', 'Nedoporučuje se. Příliš velká helma se při pádu posune a nechrání. Vyplatí se koupit helmu, která sedí teď, a po jedné až dvou sezónách ji vyměnit za větší.'),
        ('Co znamená norma EN 1077?', 'Je to evropská norma pro lyžařské a snowboardové helmy s třídami A a B. Informace najdete uvnitř helmy nebo v popisu produktu. Pro děti volte helmu s jasným označením normy.'),
        ('Je MIPS u dětských helem nutný?', 'Nutný není, je to doplňková vrstva proti rotačním nárazům. Důležitější než MIPS je správná velikost, nastavení a pevně zapnutý pásek. Pokud model s MIPS sedí a vyhovuje, je to dobrý doplněk.'),
        ('Jak poznám, že helma dobře sedí?', 'Po nasazení a zapnutí pásku zatřeste hlavou do stran a dopředu. Helma se nesmí posouvat, přední hrana má být asi dva prsty nad obočím a pod bradou se vejde prst. Nic nemá tlačit na čelo ani spánky.'),
        ('Mohu používat cyklistickou helmu na lyžování?', 'Nedoporučuje se. Cyklistická helma má jiné provedení, ventilaci i kryt uší. Pro lyže volte helmu určenou na lyžování a snowboard, ideálně s označením normy.'),
        ('Kdy dětskou lyžařskou helmu vyměnit?', 'Po silném nárazu, při viditelném poškození, když dítěti přestane sedět a po několika sezónách, kdy materiál stárne. Použitá helma z druhé ruky může mít skrytá poškození.'),
        ('Jak spojit helmu a lyžařské brýle?', 'Pásek brýlí má sedět na helmě a mezi hranou helmy a rámem nemá být velká mezera. Nejlepší je zkusit obojí společně. U menších dětí se hodí i helma s integrovaným hledím.'),
        ('Má dítě pod helmou nosit čepici?', 'Obvykle ne, helma zajišťuje teplo a čepice by změnila nastavení. V mrazu pomůže tenká kukla nebo nákrčník. Helmu vždy zkoušejte s doplňky, které dítě skutečně nosí.'),
        ('Jak helmu čistit a skladovat?', 'Čistěte ji vlažnou vodou a jemným mýdlem, bez rozpouštědel. Skladujte v suchu a nepřikrývejte ji těžkými věcmi. Při přepravě ji dejte do batohu nebo tašky, ne pod zavazadla.'),
    ])
