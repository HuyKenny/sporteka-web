"""Guides wave 1a: home gym and home cardio (January buying guides)."""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- domaci-posilovna
GUIDES['domaci-posilovna'] = dict(
    name='Domácí posilovna',
    h1='Domácí posilovna: jak ji vybavit podle prostoru a rozpočtu',
    seo_title='Domácí posilovna: jak ji vybavit podle prostoru a rozpočtu',
    seo_desc='Domácí posilovna krok za krokem: činky, kettlebelly, lavice, hrazda, gumy a podlaha. Co koupit nejdřív, co počká a na co si dát pozor u bezpečnosti.',
    intro_html=(
        '<p>V lednu vznikají domácí posilovny hromadně a stejně hromadně se z nich stávají věšáky na prádlo. Obvykle za to nemůže nedostatek vůle, ale špatný nákup: velký stroj, který se nevejde do pokoje, '
        'nebo sada činek, ze které se po dvou týdnech používají jen dva nejlehčí kotouče, protože ostatní jsou moc těžké. Cvičení doma funguje, když vybavení odpovídá prostoru, rozpočtu a tomu, co vás opravdu bude bavit.</p>'
        '<p>Průvodce postupuje v pořadí, v jakém se domácí kout obvykle skládá: nejdřív prostor a podlaha, pak základ (činky, kettlebelly, gumy), potom to, co přidáte, když vám základ přestane stačit (lavice, hrazda, věž, vesta). '
        'Pod každou částí najdete aktuální nabídky z kategorie. Sporteka srovnává nabídky českých e-shopů a nic neprodává, takže si vybrané kousky objednáte přímo v obchodě, který vám nabídne nejlepší cenu a dopravu.</p>'
        '<p>Nic v tomto textu není zdravotní rada. Pokud máte potíže se zády, klouby nebo srdcem, nebo se po delší pauze vracíte k pohybu, začněte zvolna a poraďte se s lékařem.</p>'
    ),
    sections=[
        dict(h2='Nejdřív prostor: kout v bytě, pokoj, nebo garáž',
             html=(
                 '<p>Než otevřete první e-shop, změřte místo. Pro většinu cviků potřebujete víc místa, než čekáte. Člověk s rozpaženýma rukama zabere zhruba dva metry na šířku, a když připočtete kotouč, který může spadnout vedle, '
                 'je jasné, proč s činkami necvičit mezi gaučem a skříní.</p>'
                 '<h3>Kout v bytě</h3>'
                 '<p>Stačí plocha na jednu podložku a metr volného místa kolem ní. Tady vyhrává vybavení, které se dá uklidit za dveře nebo pod postel: <a href="/posilovaci-gumy/">posilovací gumy</a>, jedna až dvě kettlebelly, nastavitelné činky. '
                 'Hrazda do rámu dveří nezabere skoro žádné místo. Rozumná hranice je vybavení, které do pěti minut uklidíte – co překáží, to se přestane používat.</p>'
                 '<h3>Samostatný pokoj</h3>'
                 '<p>Počítejte s plochou zhruba 2 × 3 m a s výškou stropu, pod kterou zvednete činku v natažených rukou nad hlavu. Vejde se lavice, stojánek na činky, hrazda na zeď a místo na podložku. '
                 'V panelovém bytě pamatujte na sousedy pod sebou: položená činka nebo spadlý kotouč je slyšet přes celý strop, takže se vyplatí tlumicí podlaha, o které píšeme níže.</p>'
                 '<h3>Garáž nebo sklep</h3>'
                 '<p>Nejvíc místa a nejméně starostí s hlukem, zato chlad a vlhkost. Železo na vlhku rezaví, proto kotouče a tyče s lakem nebo chromem obvykle vydrží lépe než holý materiál. '
                 'V zimě se v nevytápěné garáži špatně rozcvičuje, takže si naplánujte delší zahřátí. Sem se hodí lavice, věž nebo stojan, které by v bytě překážely.</p>'
             )),
        dict(h2='Činky a kotouče: základ, který se hodí vždycky',
             html=(
                 '<p>Činky jsou nejuniverzálnější nákup. Dají se s nimi dělat dřepy, přítahy, tlaky, výpady i cviky na ramena a paže. Základní volba je mezi dvěma variantami: pevné činky o jedné hmotnosti, '
                 'nebo nakládací činky s tyčí a kotouči, kde si zátěž měníte.</p>'
                 '<ul><li><strong>Nakládací sada</strong> je levnější v přepočtu na kilogram a poroste s vámi. Nevýhodou je přendávání kotoučů a to, že musíte kontrolovat zámky, aby se nic nepohnulo.</li>'
                 '<li><strong>Pevné činky</strong> máte hned po ruce, což ocení ten, kdo cvičí po práci a nechce nic skládat. Pořídit jich ale musíte několik párů.</li>'
                 '<li><strong>Průměr tyče a závit</strong> hlídejte, pokud kupujete kotouče zvlášť: tyč 25 či 30 mm a tyč 50 mm nejsou zaměnitelné a obvykle se nedají kombinovat s kotouči jiného průměru otvoru.</li></ul>'
                 '<p>Při výběru kotoučů se podívejte na materiál. Litinové jsou tvrdé a pevné, pogumované jsou tišší a šetrnější k podlaze. Do bytu jsou skoro vždy lepší ty pogumované. '
                 'Nabídku značek jako <a href="/znacka/hms/">HMS</a> nebo <a href="/znacka/insportline/">Insportline</a> najdete v kategorii <a href="/cinky-a-kotouce/">činky a kotouče</a>, kde se dá řadit podle ceny i hmotnosti.</p>'
             ), cat='cinky-a-kotouce', n=4),
        dict(h2='Kettlebelly: jedna kulatá váha místo půlky sklepa',
             html=(
                 '<p>Kettlebell je koule s držadlem; na rozdíl od jednoruční činky má těžiště mimo dlaň. Proto se hodí na švihy, zdvihy z podřepu i nošení, tedy na cviky, které zapojí celé tělo a zvednou tep. '
                 'Do bytu se hodí výborně, protože zabere jen kousek podlahy.</p>'
                 '<p>Začátečník potřebuje jednu kettlebell střední váhy. Kdo dosud se zátěží necvičil, ať sáhne spíš po lehčí, protože švih stojí na technice, ne na síle. '
                 'Později můžete přikoupit těžší kus a lehčí na tlaky nad hlavu.</p>'
                 '<ul><li>Držadlo musí být hladké, ale ne klouzavé. Ostrý šev (otřep) na rukojeti odírá kůži na dlaních.</li>'
                 '<li>Litinová bez povrchové úpravy je nejlevnější, vinylová nebo potažená šetří podlahu.</li>'
                 '<li>Nastavitelné kettlebelly existují, ale bývají hranatější a hůř se s nimi švihá. Na učení základů zvolte raději pevnou.</li></ul>'
                 '<p>Švih se nejlépe naučíte podle videa zkušeného trenéra nebo na lekci, ne podle popisku u zboží. Aktuální nabídku máte v kategorii <a href="/kettlebelly/">kettlebelly</a>.</p>'
             ), cat='kettlebelly', n=4),
        dict(h2='Posilovací lavice: kdy se vyplatí a na co se dívat',
             html=(
                 '<p>Lavice rozšíří cvičení o tlaky vleže, přítahy s oporou, dřepy na jedné noze se zadní nohou opřenou o lavici a spoustu cviků na ruce. Bez ní se obejdete, pokud máte jen gumy a jednu kettlebell. '
                 'Jakmile ale kupujete činky těžší než pár kilogramů, lavice se hodí.</p>'
                 '<h3>Nastavitelná, nebo rovná</h3>'
                 '<p>Rovná lavice je pevnější a levnější. U nastavitelné lze opěradlo postavit šikmo nebo svisle, takže přibude tlak na šikmé lavici a tlak vsedě. Pro domácí použití je většinou lepší nastavitelná, jen ověřte, '
                 'že se mechanismus zajišťuje čepem nebo západkou, ne jen třením.</p>'
                 '<h3>Co kontrolovat</h3>'
                 '<ul><li><strong>Nosnost</strong> vždy počítejte s rezervou: váha cvičence plus zátěž, kterou položíte na hrudník nebo si přehodíte přes nohy.</li>'
                 '<li><strong>Stabilita:</strong> rám by se při zatížení neměl kývat, nohy mají mít široký rozchod a gumové patky.</li>'
                 '<li><strong>Potah:</strong> pevný, protiskluzový, dobře držící tvar. Příliš měkká výplň působí pohodlně, při těžších sériích z ní ale bolí záda.</li></ul>'
                 '<p>V kategorii <a href="/posilovaci-lavice/">posilovací lavice</a> porovnáte nabídky obchodů. Rozměry a hmotnost lavice si před koupí porovnejte s místem v pokoji.</p>'
             ), cat='posilovaci-lavice', n=4),
        dict(h2='Posilovací věže a multistanice: celý stroj na jednom místě',
             html=(
                 '<p>Věž nebo multistanice je rám s kladkami, lany a opěrkami, na kterém zvládnete desítky cviků bez nakládání kotoučů. Je to pohodlné řešení pro domácnost, kde cvičí víc lidí s různou silou, '
                 'protože se zátěž přepíná jedním čepem.</p>'
                 '<p>Je ovšem třeba střízlivě počítat s místem. Věž má větší půdorys než lavice a činky dohromady a není jednoduché ji později přestěhovat. Stroje také nenahradí volné váhy tam, kde jde o stabilitu a rovnováhu, '
                 'takže pro většinu lidí jsou doplňkem, ne náhradou.</p>'
                 '<ul><li>Zjistěte, kolik závaží věž obsahuje a zda ho lze rozšířit.</li>'
                 '<li>Lana a kladky jsou součást, která se opotřebuje první. Dobrý obchod u nich uvede, jak se vyměňují.</li>'
                 '<li>Sestavení trvá obvykle několik hodin a bývá k němu potřeba druhý člověk. Počítejte s tím při dodání.</li></ul>'
                 '<p>Stroje najdete v kategorii <a href="/posilovaci-veze/">posilovací věže</a>, širší výběr v <a href="/posilovaci-stroje/">posilovacích strojích</a>.</p>'
             ), cat='posilovaci-veze', n=4),
        dict(h2='Hrazda a bradla: levný základ pro silná záda',
             html=(
                 '<p>Shyby a přítahy patří k nejúčinnějším cvikům na záda a paže a hrazda je pro ně nejjednodušší pomůcka. Existují tři hlavní typy a každý se hodí do jiného bytu.</p>'
                 '<ul><li><strong>Hrazda do rámu dveří:</strong> nejlevnější a skladná, ale omezená šířkou a kvalitou zárubně. Rozhoduje materiál rámu a to, jak pevně ho zárubeň drží.</li>'
                 '<li><strong>Hrazda na zeď:</strong> pevná, pro těžší cvičence nejlepší, musí se ale přivrtat do zdi z vhodného materiálu.</li>'
                 '<li><strong>Samostatný stojan nebo bradla:</strong> nemusíte vrtat, zaberou ale místo na podlaze. Bradla k tomu přidají kliky a dipy.</li></ul>'
                 '<p>Platí jednoduché pravidlo: dveřní hrazdu nedávejte do zárubně, která neunese vaši váhu, a před první sérií se na ni jen opatrně pověste a sledujte, jestli se rám nehýbe. '
                 'Úplný začátečník, který zatím shyb nezvládne, začne negativními shyby nebo přítahy v předklonu s gumou či s činkou. Výběr najdete v kategorii <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</p>'
             ), cat='hrazdy-a-bradla', n=4),
        dict(h2='Posilovací gumy: nejmenší nákup s největším využitím',
             html=(
                 '<p>Odporová guma je nejlevnější součást domácí posilovny a pro začátek nejrozumnější. Vejde se do zásuvky, vezmete ji i na dovolenou a dají se s ní posilovat záda, ramena, nohy i hýždě.</p>'
                 '<h3>Druhy gum</h3>'
                 '<ul><li><strong>Smyčky (mini bands)</strong> se natahují kolem kolen nebo kotníků a hodí se na hýždě a boky.</li>'
                 '<li><strong>Dlouhé uzavřené gumy</strong> se používají na pomoc při shybech i jako odpor při dřepech a tlacích.</li>'
                 '<li><strong>Gumy s madly</strong> připomínají činky na lanech a dají se uchytit ve dveřích.</li></ul>'
                 '<p>Gumy se vyrábějí v několika stupních odporu a na začátek je lepší koupit sadu než jednu gumu, protože na záda potřebujete větší odpor než na ramena. '
                 'Před každým cvičením gumu zkontrolujte, zda na ní nejsou praskliny. Natržená guma praskne ve chvíli největšího napětí. Nabídku najdete v kategorii <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
             ), cat='posilovaci-gumy', n=4),
        dict(h2='Zátěžové vesty: když vlastní váha přestane stačit',
             html=(
                 '<p>Vesta přidá kilogramy k vlastní váze a hodí se na kliky, shyby, dřepy a výpady. Ocení ji ti, kdo už cviky s vlastní vahou zvládají bez potíží a nechtějí kupovat další činky. '
                 'Pro začátečníka je to spíš nadstavba: nejdřív se naučte pohyb bez zátěže.</p>'
                 '<ul><li>Vesta má sedět těsně k tělu, aby se při pohybu nehoupala. Dobré modely mají nastavitelné popruhy.</li>'
                 '<li>Zátěž je buď pevná, nebo ve vyjímatelných váčcích, které se dají přidávat po malých krocích.</li>'
                 '<li>Při běhu a skocích zvyšujte zátěž opatrně, vesta zatěžuje klouby víc, než se zdá.</li></ul>'
                 '<p>Nabídku najdete v kategorii <a href="/zatezove-vesty/">zátěžové vesty</a>.</p>'
             ), cat='zatezove-vesty', n=4),
        dict(h2='Podložka a podlaha: ochrana domova i kloubů',
             html=(
                 '<p>Podlaha je nejpodceňovanější část domácí posilovny. Neslouží jen ke komfortu, ale chrání parkety, dlažbu, vaše kolena a sousedy dole. Podle toho, co cvičíte, se hodí různá řešení.</p>'
                 '<ul><li><strong>Tenká podložka</strong> na jógu, protahování a cviky vleže. Nechrání před dopadem činky.</li>'
                 '<li><strong>Silnější pěnová podložka nebo puzzle dlaždice</strong> pod vybavení a při cvičení vstoje. Dlaždice se dají poskládat na míru.</li>'
                 '<li><strong>Gumová nebo pryžová podlaha</strong> pod těžké činky a lavici: nejlépe tlumí a nejméně klouže.</li></ul>'
                 '<p>Pod stroj a lavici dejte plochu větší než jejich půdorys, aby se zátěž rozložila. Při dřepu a mrtvém tahu stojte na pevném, rovném základu, měkká pěna pod nohama zhoršuje stabilitu. '
                 'Výběr podložek najdete v kategorii <a href="/joga-a-podlozky/">jóga a podložky</a>.</p>'
             ), cat='joga-a-podlozky', n=4),
        dict(h2='Základní sada a rozšířená sada',
             html=(
                 '<p>Rozdíl mezi startovní a rozšířenou sadou není jen v penězích, ale v tom, co chcete dělat. Vyplatí se kupovat postupně a po měsíci zhodnotit, co vám chybí.</p>'
                 + T(['', 'Základní sada', 'Rozšířená sada'], [
                     ['Prostor', 'kout v bytě, 2 × 2 m', 'pokoj nebo garáž, 2 × 3 m a víc'],
                     ['Zátěž', 'gumy, jedna kettlebell, nastavitelné činky', 'sada činek a kotoučů, více kettlebellů'],
                     ['Další', 'podložka, dveřní hrazda', 'nastavitelná lavice, hrazda na zeď, vesta'],
                     ['Nejvíc se hodí', 'začátečníkům a bytům', 'těm, kdo cvičí třikrát týdně a víc'],
                     ['Úroveň ceny', 'nižší', 'střední až vyšší'],
                 ]) +
                 '<p>Silové vybavení se opotřebovává pomalu, takže kvalitní kousek vydrží roky. U nákupu sady dbejte spíš na nosnost a pevnost než na to, kolik kusů příslušenství je v balení. '
                 'Širší přehled najdete v kategorii <a href="/fitness/">fitness</a>.</p>'
             )),
        dict(h2='Bezpečnost: nosnost, ukotvení a podlaha',
             html=(
                 '<p>Doma vás při cvičení nikdo nesleduje. Je to příjemné, ale znamená to, že si sami musíte hlídat věci, které by jinak pohlídal trenér.</p>'
                 '<h3>Nosnost</h3>'
                 '<p>Sčítejte: vaše hmotnost plus zátěž. U lavice, hrazdy i věže uvádí výrobce limit a ten je hranice, ne doporučení. Při dynamickém pohybu (švih, kip, skok z hrazdy) působí síla vyšší než jen váha těla.</p>'
                 '<h3>Ukotvení</h3>'
                 '<p>Hrazdu na zeď přivrtejte jen do zdi, která to vydrží. Plné cihly nebo beton jsou něco jiného než sádrokarton. Pokud si nejste jisti, svěřte montáž odborníkovi. Dveřní hrazdu zkoušejte nejdřív jen s částí váhy a sledujte, jestli se rám nehýbe.</p>'
                 '<h3>Podlaha a okolí</h3>'
                 '<p>Zajistěte volný prostor kolem sebe, nepoužívejte vybavení s uvolněným šroubem a pravidelně kontrolujte zámky na činkách. Při těžších sériích potřebujete druhého člověka nebo stojan s pojistkami, aby vám tyč nepřistála na hrudi.</p>'
             )),
        dict(h2='První měsíc: jednoduchý plán',
             html=(
                 '<p>Jediný správný plán neexistuje, začátečníkovi ale stačí jednoduchý rámec: tři tréninky týdně po zhruba čtyřiceti minutách se dnem odpočinku mezi nimi.</p>'
                 '<ol><li><strong>První týden:</strong> naučte se základní pohyby bez zátěže nebo s malou zátěží: dřep, předklon, tlak, přítah, plank. Důležitá je technika, ne počet opakování.</li>'
                 '<li><strong>Druhý týden:</strong> přidejte zátěž tak, aby poslední opakování bylo namáhavé, ale pořád čisté.</li>'
                 '<li><strong>Třetí týden:</strong> zvyšte buď opakování, nebo váhu, ne obojí najednou.</li>'
                 '<li><strong>Čtvrtý týden:</strong> udělejte lehčí týden a zhodnoťte, co vás bavilo, co bolelo a co vám chybí.</li></ol>'
                 '<p>Před každým tréninkem se zahřejte pár minut lehkým pohybem. Pokud cítíte jinou bolest než běžnou únavu svalů, přestaňte. '
                 'Při zdravotních potížích se poraďte s lékařem. Silový trénink můžete doplnit kardiem, třeba podle <a href="/kardio-doma/">průvodce kardiem doma</a>. Nutriční základy najdete v textu o <a href="/vyziva-pro-zacatecniky/">výživě pro začátečníky</a>.</p>'
             )),
    ],
    faq=[
        ('Co koupit do domácí posilovny jako první?',
         '<p>Podložku, sadu posilovacích gum a jednu kettlebell nebo nastavitelné činky. Za málo peněz s tím procvičíte celé tělo a po měsíci víte, jestli vás cvičení doma baví. Teprve potom má smysl pořizovat lavici nebo hrazdu.</p>'),
        ('Vejde se domácí posilovna do panelákového bytu?',
         '<p>Ano, když zvolíte skladné vybavení a podložku. Gumy, kettlebell a dveřní hrazda se vejdou do skříně. Počítejte s tím, že cvičení s činkami je slyšet, takže pomůže tlumicí podlaha.</p>'),
        ('Je lepší nakládací sada, nebo pevné činky?',
         '<p>Nakládací sada je levnější na kilogram a lze ji postupně rozšiřovat. Pevné činky máte rychleji připravené, musíte jich ale mít víc párů. Pro začátečníka bývá rozumná sada s tyčí a několika kotouči.</p>'),
        ('Můžu hrazdu zavěsit do dveří?',
         '<p>Záleží na zárubni a na výrobci. Dveřní hrazdy mají omezenou nosnost a nehodí se do každé zárubně. Pokud si nejste jisti, zvolte hrazdu na zeď nebo samostatný stojan.</p>'),
        ('Jak často cvičit doma na začátku?',
         '<p>Dvakrát až třikrát týdně se dnem pauzy mezi tréninky. Začněte zvolna a při zdravotních potížích se poraďte s lékařem.</p>'),
        ('Jak poznám, že je nabídka na Sportece výhodná?',
         '<p>Sporteka porovnává nabídky českých e-shopů u téhož produktu, takže vidíte rozdíly v ceně a dopravě. Objednáváte vždy přímo v obchodě, my nic neprodáváme. Před objednávkou si ověřte dodací lhůtu a podmínky vrácení.</p>'),
    ],
    cats=['fitness', 'posilovaci-stroje'],
    updated='2026-11-16')

# ---------------------------------------------------------------- kardio-doma
GUIDES['kardio-doma'] = dict(
    name='Kardio doma',
    h1='Rotoped, běžecký pás, nebo eliptický trenažér? Kardio doma',
    seo_title='Kardio doma: rotoped, běžecký pás, eliptický trenažér',
    seo_desc='Rotoped, běžecký pás, eliptický trenažér, nebo veslo? Srovnání do bytu: prostor, hluk, zátěž kloubů a na co si dát při koupi pozor.',
    intro_html=(
        '<p>Kardio trenažér se v lednu kupuje s nejlepšími úmysly a v únoru z něj bývá odkládací plocha. Důvod je téměř vždy stejný: koupil se stroj, který nesedí k bytu nebo k člověku. Pás hlučí v paneláku, '
        'eliptický trenažér zabere půl pokoje a rotoped je pro někoho příliš nudný. Výběr proto začněte otázkou, kde bude stroj stát a jak dlouho vás na něm cvičení vydrží bavit.</p>'
        '<p>Průvodce porovnává čtyři základní typy: rotoped, běžecký pás, eliptický trenažér a veslovací trenažér. U každého najdete, komu se hodí, co kontrolovat a na co si dát pozor. '
        'Pod každou částí najdete aktuální nabídky. Sporteka porovnává nabídky českých e-shopů a nic neprodává, objednáváte tedy přímo v obchodě.</p>'
        '<p>Tohle není zdravotní poradna. Pokud máte potíže se srdcem, klouby nebo se po delší pauze vracíte k pohybu, začněte zvolna a poraďte se s lékařem.</p>'
    ),
    sections=[
        dict(h2='Porovnání: který trenažér se hodí k vašemu bytu',
             html=(
                 '<p>Tabulka ukazuje jen hrubý obrázek. Konkrétní modely se liší, základní vlastnosti každého typu ale platí.</p>'
                 + T(['', 'Rotoped', 'Běžecký pás', 'Eliptický trenažér', 'Veslovací trenažér'], [
                     ['Prostor', 'malý, často skladný', 'velký, složený menší', 'střední až velký', 'dlouhý, na výšku se dá postavit'],
                     ['Hluk', 'nízký', 'vyšší, dopady kroků', 'nízký až střední', 'střední, šum vzduchu či vody'],
                     ['Zátěž kloubů', 'nízká', 'vyšší, dopad při běhu', 'nízká', 'nízká'],
                     ['Zapojené svaly', 'nohy, hýždě', 'nohy, hýždě, trup', 'nohy, hýždě, ruce', 'záda, nohy, ruce, trup'],
                     ['Úroveň ceny', 'nižší až střední', 'střední až vyšší', 'střední až vyšší', 'střední až vyšší'],
                 ]) +
                 '<p>Zjednodušeně: do malého bytu a paneláku se nejlíp hodí rotoped, do většího prostoru a pro ty, kdo chtějí chodit nebo běhat, pás. Eliptický trenažér potěší ty, kdo se chtějí vyhnout dopadům, a veslo ocení ti, kdo chtějí zapojit záda a paže.</p>'
                 '<p>Širší výběr najdete v kategorii <a href="/fitness/">fitness</a>, ke kardiu se hodí i náš <a href="/domaci-posilovna/">průvodce domácí posilovnou</a>, který cvičení doplní o sílu.</p>'
             )),
        dict(h2='Pro koho se co hodí',
             html=(
                 '<p>Tabulka je přehledná, jenže každý člověk je jiný. Tady je pár typických situací z praxe.</p>'
                 '<h3>Malý byt v paneláku</h3>'
                 '<p>Rotoped, nejlépe skládací, s magnetickým odporem. Postavíte ho do kouta a večer jezdíte u seriálu, aniž byste rušili sousedy. Pokud chcete posilovat i záda a paže, po čase přidejte gumy nebo jednu kettlebell.</p>'
                 '<h3>Chcete se vrátit k běhání, ale nechcete ven do tmy a mrazu</h3>'
                 '<p>Na pásu si udržíte návyk i v zimě. Počítejte s hlukem a s tím, že kroky zatěžují klouby stejně jako venku. Na začátek stačí svižná chůze se sklonem, běh přidávejte po krátkých úsecích.</p>'
                 '<h3>Bolí vás kolena nebo kotníky při dopadu</h3>'
                 '<p>Rotoped nebo eliptický trenažér. Pohyb je plynulý a bez nárazů. Pokud bolest přetrvává, poraďte se s lékařem, trenažér ji nevyřeší.</p>'
                 '<h3>Cvičíte rádi celým tělem a nudí vás šlapání</h3>'
                 '<p>Veslo. Dají se na něm jezdit krátké intervaly a zapojíte při tom záda, nohy i paže. Vyžaduje ale techniku a trochu trpělivosti, než pohyb zautomatizujete.</p>'
                 '<h3>Cvičí víc lidí v domácnosti</h3>'
                 '<p>Nejdůležitější je nastavitelnost: sedlo a řídítka u rotopedu, délka kroku u elipsy, popruhy na chodidla u vesla. Stroj, který se dá rychle přenastavit, se používá víc než ten, který sedí jen jednomu.</p>'
                 '<p>Pokud váháte mezi dvěma typy, zeptejte se sami sebe, který z nich byste byli ochotni zapnout v deštivý čtvrtek večer. Právě ten je pro vás správný, i když na papíře vypadá hůř.</p>'
             )),
        dict(h2='Rotopedy: nejklidnější volba do bytu',
             html=(
                 '<p>Rotoped zabere nejméně místa a je nejtišší. Můžete na něm jezdit u televize a nevzbudíte děti. Existují dva základní typy: klasický vzpřímený, na kterém se sedí podobně jako na kole, '
                 'a ležatý (recumbent) s opěradlem a polohou v pololehu, který je šetrnější k zádům.</p>'
                 '<ul><li><strong>Setrvačník:</strong> těžší setrvačník dává plynulejší záběr a působí přirozeněji. U lehkého je šlapání trhané.</li>'
                 '<li><strong>Odpor:</strong> magnetický je tichý a bezúdržbový, řemenový nebo třecí může drhnout. Nastavení odporu otočným knoflíkem je jednodušší než přes počítač.</li>'
                 '<li><strong>Sedlo a řídítka:</strong> nastavitelná do výšky i vzdálenosti. Pokud nejsou, bolí jízda i po krátké době.</li>'
                 '<li><strong>Pedály:</strong> s řemínky, nebo nášlapné pro tretry – podle toho, jak chcete jezdit.</li></ul>'
                 '<p>Mnoho rotopedů jde složit, což v malém bytě oceníte. V kategorii <a href="/rotopedy/">rotopedy</a> najdete modely značek jako <a href="/znacka/hms/">HMS</a> nebo <a href="/znacka/insportline/">Insportline</a>.</p>'
             ), cat='rotopedy', n=4),
        dict(h2='Běžecké pásy: pro ty, kdo chtějí chodit a běhat doma',
             html=(
                 '<p>Pás je jediný trenažér, na kterém opravdu běžíte nebo svižně chodíte. Je to největší výhoda i největší nevýhoda: dopad kroků zatěžuje klouby podobně jako běh venku a v paneláku se přenáší do stropu pod vámi.</p>'
                 '<h3>Na co se dívat</h3>'
                 '<ul><li><strong>Délka a šířka pásu:</strong> pro chůzi stačí kratší pás, pro běh potřebujete delší a širší, abyste měli jistý krok. Vyšší lidé potřebují delší běžeckou plochu.</li>'
                 '<li><strong>Výkon motoru:</strong> při pomalé chůzi stačí slabší, pro běh potřebujete rezervu. Sledujte trvalý výkon motoru, ne špičkový.</li>'
                 '<li><strong>Nosnost:</strong> počítejte s rezervou nad vlastní váhou, běh zvyšuje zatížení.</li>'
                 '<li><strong>Odpružení pásu:</strong> tlumí dopady a šetří kolena.</li>'
                 '<li><strong>Sklon a programy:</strong> sklonem zvýšíte zátěž, aniž byste museli zrychlit.</li></ul>'
                 '<p>Při posuzování hlučnosti nespoléhejte jen na číslo v popisku, zvlášť do bytu. Pomůže tlumicí podložka pod pásem. Pokud jde o začátek běhání obecně, přečtěte si průvodce <a href="/zaciname-behat-v-zime/">začínáme běhat v zimě</a>. '
                 'Nabídku najdete v kategorii <a href="/behaci-pasy/">běžecké pásy</a>.</p>'
             ), cat='behaci-pasy', n=4),
        dict(h2='Eliptické trenažéry: plynulý pohyb bez dopadů',
             html=(
                 '<p>Elipsa kombinuje pohyb nohou a paží a nezatěžuje klouby dopady. Je to rozumná volba pro ty, kdo se vracejí k pohybu a chtějí šetřit kolena a kotníky. '
                 'Pohyb připomíná chůzi do schodů se zapojením paží a chvíli trvá, než si na něj zvyknete.</p>'
                 '<ul><li><strong>Délka kroku:</strong> delší krok je přirozenější, pro vyšší postavy je to důležité.</li>'
                 '<li><strong>Setrvačník a plynulost:</strong> těžší setrvačník dává plynulejší chod, u levnějších modelů bývá chod trhaný.</li>'
                 '<li><strong>Madla:</strong> pohyblivá madla zapojí horní polovinu těla, pevná slouží jen jako opora.</li>'
                 '<li><strong>Stabilita:</strong> stroj se nesmí při šlapání kývat.</li></ul>'
                 '<p>Eliptický trenažér zabere víc místa než rotoped, proto předem změřte, kam se vejde a kolik místa kolem něj potřebujete pro bezpečný nástup. Nabídku najdete v kategorii <a href="/elipticke-trenazery/">eliptické trenažéry</a>.</p>'
             ), cat='elipticke-trenazery', n=4),
        dict(h2='Veslovací trenažéry: kardio a záda v jednom',
             html=(
                 '<p>Veslování zapojí nohy, záda, trup i paže a při správném provedení klouby nepřetěžuje. Technika je tu ale důležitější než u ostatních strojů. Pohyb začíná odrazem nohou, potom se zakloní trup a nakonec se přitáhnou paže. Častou chybou je opak: táhnout nejdřív rukama a nohy zapojit až na konci.</p>'
                 '<ul><li><strong>Typ odporu:</strong> vzduchový dává pocit podobný skutečnému veslování a odpor roste s tempem, ale je slyšet. Magnetický je tišší, vodní má typický šplouchavý zvuk a plynulý chod.</li>'
                 '<li><strong>Sedadlo a kolejnice:</strong> pohodlné sedadlo a dostatečně dlouhá kolejnice pro vaši výšku.</li>'
                 '<li><strong>Skládání:</strong> mnoho modelů se dá postavit na výšku, což v bytě oceníte.</li></ul>'
                 '<p>Při slabších zádech začínejte krátkými úseky a hlídejte techniku. Porovnáte je v kategorii <a href="/veslovaci-trenazery/">veslovací trenažéry</a>.</p>'
             ), cat='veslovaci-trenazery', n=4),
        dict(h2='Co zkontrolovat před koupí',
             html=(
                 '<p>Většina chyb se dá odhalit v popisu a v parametrech, ještě než zboží objednáte.</p>'
                 '<ul><li><strong>Nosnost:</strong> musí pokrýt vaši váhu s rezervou. To platí zejména u pásu a vesla, kde síla při pohybu převyšuje klidovou hmotnost.</li>'
                 '<li><strong>Setrvačník:</strong> těžší se vyplatí u rotopedu, elipsy a vesla. Plynulý záběr je pro pohodlí důležitější než počet programů.</li>'
                 '<li><strong>Odpor:</strong> plynulá regulace a rozsah, který stačí na rozjetí i na těžší práci.</li>'
                 '<li><strong>Hlučnost pro panelák:</strong> nejtišší jsou rotopedy a magnetické stroje, nejhlasitější běžecký pás. Podložka a rozumná doba cvičení pomáhají sousedům i vám.</li>'
                 '<li><strong>Skládání:</strong> pokud nebude stroj stát trvale, dívejte se na rozměry po složení a na to, jestli se dá snadno přesunout (kolečka).</li>'
                 '<li><strong>Rozměry:</strong> změřte místo a nezapomeňte na dveře, kterými stroj projde, a na výšku stropu u pásu se sklonem.</li></ul>'
                 '<p>Počítač s programy je příjemný doplněk, nikoliv důvod, proč stroj koupit. Pro začátek stačí displej s časem, vzdáleností a tepem.</p>'
             )),
        dict(h2='Umístění a ochrana podlahy',
             html=(
                 '<p>I nejlepší stroj zlobí, když stojí na nerovné nebo měkké podlaze. Pod trenažér patří pevná podložka z gumy nebo pryže, ne koberec, do kterého se stroj boří.</p>'
                 '<ul><li><strong>Rovinu</strong> ověřte vodováhou. Nerovnost se projeví vrzáním a rychlým opotřebením.</li>'
                 '<li><strong>Podložku</strong> volte větší než půdorys stroje. Zachytí pot, olej a drobné nečistoty a ochrání parkety.</li>'
                 '<li><strong>Volný prostor:</strong> za pásem a elipsou nechte aspoň metr volného místa a dost prostoru i po stranách, aby se dalo bezpečně nastoupit.</li>'
                 '<li><strong>Sousedé:</strong> v bytě stroj postavte ke zdi, ne doprostřed pokoje, a necvičte brzy ráno ani pozdě večer.</li></ul>'
                 '<p>Podložky pod trenažéry najdete mezi <a href="/joga-a-podlozky/">podložkami</a>. Při cvičení doma v zimě se hodí i vyvětraná místnost a voda po ruce.</p>'
             )),
        dict(h2='Jak začít: jednoduchý plán pro první týdny',
             html=(
                 '<p>Na začátku platí jedno: kratší tréninky častěji jsou lepší než jeden dlouhý. Dvacet minut třikrát týdně pomalým tempem je dobrý základ, ze kterého se dá stavět.</p>'
                 '<ol><li><strong>První dva týdny:</strong> dvacet minut v tempu, při kterém můžete mluvit celými větami. Nehoňte výkon.</li>'
                 '<li><strong>Třetí a čtvrtý týden:</strong> prodlužujte dobu po pěti minutách, ne rychlost.</li>'
                 '<li><strong>Později:</strong> jednou týdně zkuste střídat rychlejší a pomalejší úseky.</li></ol>'
                 '<p>Tep nemusíte přesně měřit přístrojem. Orientačně poslouží test řečí: když při cvičení zvládnete říct celou větu a neztrácíte dech, tempo je pro začátek správné. Zahřejte se a po cvičení se protáhněte. Pokud se objeví bolest na hrudi, závrať nebo neobvyklá dušnost, přestaňte a vyhledejte lékaře. '
                 'Kardio dobře doplní silový trénink – viz průvodce <a href="/domaci-posilovna/">domácí posilovna</a>. Pokud vás láká venkovní pohyb, podívejte se na <a href="/zaciname-behat-v-zime/">běh v zimě</a>.</p>'
             )),
    ],
    faq=[
        ('Který kardio trenažér je nejtišší do paneláku?',
         '<p>Rotoped, zvlášť s magnetickým odporem. Nejhlasitější bývá běžecký pás, protože kroky dopadají na pás a přenášejí se do podlahy. Pomůže tlumicí podložka a rozumně zvolená doba cvičení.</p>'),
        ('Je lepší rotoped, nebo eliptický trenažér?',
         '<p>Rotoped je menší, tišší a zpravidla levnější. Elipsa zapojí i paže a nabízí pohyb podobný chůzi, ale zabere víc místa. Pokud máte málo prostoru, vyberte rotoped.</p>'),
        ('Zatěžuje běžecký pás klouby?',
         '<p>Ano, běh na pásu zatěžuje klouby podobně jako běh venku, i když odpružení pásu dopad zmírní. Pokud chcete šetřit kolena, zvažte rotoped nebo eliptický trenažér, případně začněte svižnou chůzí.</p>'),
        ('Na co dát pozor u vesla?',
         '<p>Na typ odporu, délku kolejnice a možnost složení. Hlavně se naučte správnou techniku: nejdřív nohy, pak trup a nakonec paže. Začněte krátkými úseky.</p>'),
        ('Jak dlouho cvičit na začátku?',
         '<p>Stačí dvacet minut třikrát týdně v klidném tempu. Začněte zvolna a při zdravotních potížích se poraďte s lékařem.</p>'),
        ('Prodává Sporteka trenažéry?',
         '<p>Ne. Sporteka porovnává nabídky českých e-shopů. Objednáváte přímo v obchodě a ten řeší dopravu, montáž i reklamaci.</p>'),
    ],
    cats=['fitness'],
    updated='2026-11-16')
