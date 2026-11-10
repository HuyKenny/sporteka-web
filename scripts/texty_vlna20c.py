"""sporteka.cz — wave 20c (4. 11. 2026): long texts (>= 1650 words) for fotbalove-mice, freestyle-kolobezky, hokejove-puky-a-branky, beh.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ fotbalove-mice
NEW['fotbalove-mice'] = dict(long=True,
    title='Fotbalové míče: velikost, povrch a konstrukce',
    desc='Fotbalové míče velikosti 3, 4 a 5, futsalové, mini i fanouškovské. Jak vybrat podle věku, povrchu a konstrukce a porovnat nabídky obchodů.',
    intro='<p>Fotbalový míč vypadá jako jednoduchý předmět, ale na jeho vlastnostech závisí, jak se hra cítí: jak přesně se přihrává, jak se míč chová na mokré trávě a kolik zápasů nebo tréninků vydrží, než se povrch vyčerpá. '
          'Rozhoduje velikost podle věku hráče, způsob výroby panelů, vnitřní měchýř a také to, kde se bude hrát, zda na trávě, na umělé trávě, v hale nebo na asfaltu. '
          'Samostatnou skupinu tvoří míče fanouškovské, mini míčky pro sběratele a futsalové míče s nižším odskokem.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u míčů značek Puma, Adidas, Select, Kipsta, Nike, Umbro nebo Joma a vidíte, kde je právě skladem ten váš. '
          'K míči se hodí <a href="/kopacky/">kopačky</a>, <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a> a <a href="/brankarske-rukavice/">brankářské rukavice</a>, '
          'celý sport shrnuje kategorie <a href="/fotbal/">fotbal</a>. Níže najdete přehled velikostí, konstrukcí a péče.</p>',
    guide='<h2>Na čem záleží u fotbalového míče</h2>'
          '<p>Každý míč tvoří tři vrstvy: vnější povrch z polyuretanu nebo PVC, mezivrstva z textilu, která určuje tvar a pevnost, a vnitřní měchýř, který drží vzduch. '
          'Kvalitní míč drží kulatý tvar i po stovkách dopadů, vrací se do původního tvaru po kopnutí a nenasákne vodou. Levnější míč je tvrdší, hůř reaguje na jemné dotyky a na vlhku těžkne. '
          'Při výběru proto zvažte nejen vzhled a značku, ale hlavně to, k čemu míč poslouží: pro děti na hřišti za domem stačí odolná klasika, pro ligový zápas se hodí míč s přesným odskokem a tvarem.</p>'
          '<h2>Velikost podle věku</h2>'
          '<p>Velikost se označuje číslem od 1 do 5 a stanovuje ji obvod i hmotnost. Největší chyba při nákupu pro děti je koupit míč o číslo větší, aby „vydržel“. Těžší míč mění techniku, dítě kopá hůř a může ho bolet noha.</p>'
          + T(['Velikost', 'Obvyklé použití', 'Poznámka'], [
              ['1', 'suvenýry, mini míčky a podpisové repliky', 'nehodí se ke hře, slouží jako sběratelský předmět'],
              ['3', 'nejmladší děti, přípravky', 'lehký míč pro první kroky ve hře'],
              ['4', 'starší žáci, futsal a menší hřiště', 'u futsalu má míč navíc nižší odskok'],
              ['5', 'dospělí a dorost, oficiální zápasy', 'standardní velikost velkého fotbalu']]) +
          '<p>Přechod mezi velikostmi určuje klub nebo trenér, který zná sílu a techniku dítěte. Pokud nevíte, zeptejte se na tréninku. V obchodech uvidíte u míče velikost většinou přímo v názvu, například jako „vel. 5“.</p>'
          '<h2>Konstrukce a typy míčů</h2>'
          '<h3>Šité panely</h3>'
          '<p>Šité míče mají panely spojené nití a pevně sevřené vrstvy uvnitř. Jsou odolné vůči nárazům o beton a zeď, proto se hodí na tréninky, školní hřiště a časté používání. '
          'Nevýhodou bývá vyšší hmotnost při navlhnutí a méně pravidelný odskok než u dražších míčů.</p>'
          '<h3>Lepené a termálně spojené panely</h3>'
          '<p>Termálně spojené panely nemají švy, takže míč nasává méně vody a pohybuje se předvídatelněji. Využívají se u zápasových míčů, které mají velké kluby i reprezentace. '
          'Míč je vzhledem k vyšší přesnosti citlivější na hrubé zacházení, proto na štěrku a tvrdých površích dlouho nevydrží.</p>'
          '<h3>Tréninkové míče</h3>'
          '<p>Tréninkový míč je kompromis mezi cenou a výdrží. Má tužší povrch, silnější měchýř a často výraznou barvu, která je vidět na zasněžené nebo večerní trávě. Hodí se pro tréninky klubů i pro rodiny, které chtějí míč používat denně.</p>'
          '<h3>Futsalové míče</h3>'
          '<p>Futsalový míč je menší a má sníženou odrazivost, aby neskákal po tvrdé podlaze. Při hře v hale ho používejte a nepleťte si ho s klasickým míčem, který by od zdi i podlahy odskakoval příliš. Další sálové míče a vybavení jsou v oblasti <a href="/micove-sporty/">míčové sporty</a> a ve <a href="/florbal/">florbalu</a>.</p>'
          '<h3>Fanouškovské a mini míče</h3>'
          '<p>Mezi nabídkou najdete také míče s logem klubů a turnajů. Plnohodnotné repliky zápasových míčů jsou skutečně hratelné, mini míčky určené jako suvenýr a pro děti na zahradě jsou naproti tomu příliš malé pro hru ve velikosti dospělých. Před koupí zkontrolujte, jestli popis uvádí „velikost 1“ nebo „mini“. Zápasové míče bývají označené certifikací FIFA Quality; u dětských a tréninkových míčů dbejte hlavně na velikost, která odpovídá věku hráče.</p>'
          '<h2>Povrch hřiště a materiál</h2>'
          + T(['Hřiště', 'Co zvolit', 'Na co si dát pozor'], [
              ['Přírodní tráva', 'zápasový nebo kvalitní tréninkový míč', 'po dešti míč těžkne, proto vyberte materiál s minimální nasákavostí'],
              ['Umělá tráva', 'míč s odolnějším povrchem', 'povrch se rychleji obrušuje'],
              ['Hala nebo sál', 'futsalový míč', 'klasický míč odskakuje příliš'],
              ['Asfalt, beton, ulice', 'tuhý míč nebo streetový model', 'kvalitní zápasový míč se na tvrdém povrchu rychle ničí'],
              ['Písek a pláž', 'lehčí měkký míč', 'písek poškozuje švy a měchýř']]) +
          '<p>Pokud hrajete na více površích, pořiďte si dva míče. Jeden vždy zůstane na zápasy a druhý bude „na všechno“. Ušetříte tak hlavně ten dražší, který se na asfaltu opotřebí několikanásobně rychleji.</p>'
          '<h2>Pro koho který míč</h2>'
          '<ul><li><strong>Děti a přípravky:</strong> lehčí velikost 3 nebo 4, odolný povrch, živá barva pro lepší viditelnost.</li>'
          '<li><strong>Školy a kroužky:</strong> tréninkové míče s pevnou konstrukcí, balení po více kusech pro tělocvik.</li>'
          '<li><strong>Amatérské ligy:</strong> kvalitní zápasový nebo tréninkový míč velikosti 5 s lepeným nebo termálním spojením panelů.</li>'
          '<li><strong>Fanoušci a sběratelé:</strong> licencované míče klubů a turnajů a mini míčky na polici nebo do auta.</li>'
          '<li><strong>Halové týmy a futsal:</strong> míč s označením futsal, který je určen na hladkou podlahu.</li>'
          '<li><strong>Brankáři:</strong> na tréninky stejný míč jako ostatní, ke chytání přidejte vhodné <a href="/brankarske-rukavice/">brankářské rukavice</a> s dobrým úchopem.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíc nabídek mají ' + B(("puma", "Puma"), ("adidas", "Adidas"), ("select", "Select"), ("kipsta", "Kipsta"), ("nike", "Nike"), ("umbro", "Umbro")) +
          '. Další modely nabízejí ' + B(("sportteam", "SportTeam"), ("gala", "Gala"), ("kensis", "Kensis"), ("joma", "Joma"), ("powershot", "Powershot"), ("spokey", "Spokey"), ("merco", "Merco"), ("errea", "Errea")) + '. '
          'Velké značky nabízejí licencované míče klubů a reprezentací, Select se dlouhodobě spojuje s tréninkovými a zápasovými míči pro české ligy a Kipsta je oblíbená u rodin, které hledají odolný míč pro každodenní hru. '
          'Rozdíl mezi levnějším a dražším míčem pozná hráč hlavně v kvalitě vrstev uvnitř, takže se vyplatí číst popis konstrukce.</p>'
          '<h2>Péče o míč</h2>'
          '<p>Správně nahuštěný míč hraje nejlépe. Při příliš nízkém tlaku ztrácí odraz a hráč musí kopat silněji, při přehuštění tvrdne a bolí do nohy. Pro huštění používejte ventilkovou jehlu navlhčenou vodou, aby se nepoškodil ventil. '
          'Po vlhkém zápase míč otřete suchým hadrem a nechte ho doschnout v pokoji. Nikdy ho nesušte na topení ani na přímém slunci, protože se může deformovat. Vozíte-li ho v autě, nenechávejte ho v zimě ani v létě v zavazadlovém prostoru, kde jsou extrémní teploty. '
          'Na umělé trávě a na asfaltu písek a drobné kamínky míč opotřebovávají, tvrdé hřiště si žádá starší míč.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš velký míč pro dítě. Dítě pak kope hůř a ztrácí chuť do hry.</li>'
          '<li>Zápasový míč na asfalt. Povrch se obrousí během několika tréninků.</li>'
          '<li>Míč s nesprávnou velikostí u futsalu. U haly vždy hledejte označení futsal.</li>'
          '<li>Koupě podle logu bez ohledu na konstrukci. Replika může vypadat stejně jako zápasový míč, ale hrát se jinak.</li>'
          '<li>Zanedbaný tlak. Míč, který není správně nahuštěný, se rychle opotřebuje a nehraje podle očekávání.</li></ul>'
          '<h2>Kdy a jak nakupovat</h2>'
          '<p>Největší nabídka přichází před jarní sezónou a po velkých turnajích, kdy se trh plní míči s motivy. Po sezóně obchody často uvolňují starší série, jejichž hrací vlastnosti se mezi ročníky mění jen málo. '
          'Na Sportece vidíte vedle sebe nabídky několika obchodů a můžete sledovat vývoj ceny u konkrétního míče. Při nákupu pro tým porovnejte vícebalení a zkontrolujte dopravu. '
          'Doplnit můžete <a href="/treninkova-obuv/">tréninkovou obuv</a> pro halu nebo <a href="/funkcni-trenink/">funkční trénink</a>, který zlepší sílu a výbušnost.</p>',
    faq=[
        ('Jakou velikost míče koupit pro dítě?', 'Nejmladším dětem se hodí velikost 3, starším žákům 4 a od dorostu 5. Neberte větší míč „do zásoby“, těžší míč zhoršuje techniku. Vhodnou velikost potvrdí také trenér.'),
        ('Jaký je rozdíl mezi zápasovým a tréninkovým míčem?', 'Zápasový míč má přesnější tvar, citlivější odskok a méně nasákavý povrch, ale na tvrdém hřišti dlouho nevydrží. Tréninkový míč je tužší a odolnější, proto se hodí na každodenní používání.'),
        ('Můžu hrát futsalovým míčem venku?', 'Ano, ale povrch se na asfaltu rychle obrousí a míč je menší a těžší než klasický. Futsalový míč je určený pro hladkou podlahu a vyniká nižším odskokem.'),
        ('Jak často mám míč huštit?', 'Tlak se mění s teplotou a sám také pomalu klesá, proto ho kontrolujte před každým tréninkem. Správný tlak najdete u ventilku nebo v popisu výrobce.'),
        ('Jak vyčistit zablácený míč?', 'Otřete ho vlhkým hadříkem s trochou jemného mýdla a pak dosucha. Nepoužívejte rozpouštědla ani drsné kartáče, které by poškodily povrch.'),
        ('Proč se míč po čase deformuje?', 'Příčinou bývá dlouhé skladování s nízkým tlakem, teplo nebo úder o ostrý předmět. Poškozený měchýř se často už nenapraví, proto míč raději vyměňte.'),
        ('Co znamená termálně spojené panely?', 'Panely nejsou sešité, ale slepené teplem. Povrch je hladší, do švů nevniká voda a míč letí předvídatelněji. Takové míče používají zápasy vyšších soutěží.'),
        ('Jak poznám plnohodnotnou repliku zápasového míče?', 'Popis uvádí velikost 5 a typ konstrukce, kdežto sběratelské míče mají často označení mini nebo velikost 1. Pokud informace chybí, ověřte ji u prodejce nebo na stránce výrobce.'),
        ('Hodí se míč s logem klubu na trénink?', 'Většinou ano, pokud jde o velikost 5 nebo 4 s odolným povrchem. Licencované míče si však často kupují fanoušci jako dárek, a proto se hodí i jako vitrína.'),
        ('Který míč je nejlepší na umělou trávu?', 'Pomůže odolnější povrch a spíše tréninková konstrukce. Umělá tráva míč obrušuje rychleji než přírodní, proto na ni nedávejte nejlepší zápasový kus.'),
    ])

# ------------------------------------------------------------------ freestyle-kolobezky
NEW['freestyle-kolobezky'] = dict(long=True,
    title='Freestyle koloběžky: komplety, kolečka a díly',
    desc='Freestyle koloběžky pro skatepark a triky, kolečka, gripy a díly. Jak vybrat velikost, kolečka a konstrukci a porovnat nabídky českých obchodů.',
    intro='<p>Freestyle koloběžka je pevná a lehká koloběžka postavená na skokánky, rampy a triky v parku nebo na ulici. Na rozdíl od běžných městských modelů nemá sklopné řídítka, jede se na malých kolečkách z tvrdého polyuretanu a všechny díly jsou dimenzované na tvrdé dopady. '
          'Kategorie zahrnuje hotové komplety pro začátečníky i pokročilé jezdce a také samostatná kolečka, gripy, pegy a další náhradní díly, ze kterých si koloběžku postavíte a opravíte sami.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Core, Divine, Striker, Slamm, Chilli, Panda, Ethic, AO nebo Street Surfing. '
          'Pro běžné projížďky se hodí <a href="/kolobezky/">koloběžky</a> a <a href="/elektrokolobezky/">elektrokoloběžky</a>, pro bezpečnost <a href="/chranice-a-helmy/">chrániče a helmy</a>. '
          'Níže najdete přehled konstrukce, velikosti a údržby.</p>',
    guide='<h2>Z čeho se freestyle koloběžka skládá</h2>'
          '<p>Základem je deska (deck), na které stojíte, a k ní se připojují vidlice, řídítka, kolečka a brzda. Většina komplety má pevné jednodílné řídítka a bezzávitovou hlavovou sadu, která snese tvrdá přistání. '
          'Na desce najdete grip pásku, která drží nohu na místě, a zpravidla krátký zadní blatník, který funguje jako brzda. Rozdíl mezi levnější a dražší koloběžkou je hlavně v materiálu desky a v přesnosti zpracování, což určuje životnost a hmotnost.</p>'
          '<h2>Velikost podle výšky a stylu</h2>'
          '<p>Velikost neurčuje věk, ale výška jezdce, délka desky a výška řídítek. Řídítka by měla končit zhruba u pasu až hrudníku, aby jezdec při odrazu nemusel neohrabaně předklánět záda. '
          'Menší koloběžky jsou obratnější a lépe se s nimi dělají vzdušné triky, větší stabilnější při rychlých sjezdech. Menší děti mají k dispozici modely s označením mini nebo junior.</p>'
          + T(['Označení', 'Pro koho', 'Charakter'], [
              ['Mini / Junior', 'menší děti a začátečníci', 'nízká řídítka, lehká konstrukce'],
              ['Standard', 'většina teenagerů a dospělých', 'univerzální výška a délka desky'],
              ['Large / XL', 'vyšší jezdci', 'delší deska a vyšší řídítka, vyšší stabilita'],
              ['Pro komplet', 'zkušení jezdci', 'kvalitní díly, nižší hmotnost, vyšší odolnost']]) +
          '<p>Pokud váháte mezi dvěma velikostmi, vezměte tu, která umožní pohodlný postoj s lehce pokrčenými koleny. U rostoucích dětí se vyplatí kupovat koloběžku s možností výměny řídítek, aby vydržela déle.</p>'
          '<h2>Komplet, nebo skládání z dílů</h2>'
          '<p>Hotová koloběžka je nejrychlejší cesta, jak začít. Obsahuje sladěné díly a obvykle je i nejlevnější z hlediska poměru ceny a výbavy. Sestavení z dílů dává smysl pro pokročilé jezdce, kteří vědí, jaké kolečka, řídítka a vidlici chtějí, a také tehdy, když se rozbije jen jedna část. '
          'Základní nářadí, imbusový klíč a nástroj na hlavovou sadu, často stačí. Při skládání dávejte pozor na kompatibilitu průměru řídítek, šířky vidlice a typu hlavové sady, jinak díly spolu nepasují.</p>'
          '<h2>Kolečka</h2>'
          '<p>Kolečka patří k nejčastěji měněným dílům. Skládají se z plastového nebo hliníkového jádra a polyuretanového pláště. Hliníkové jádro je pevnější a lépe drží tvar, plastové je lehčí a levnější. '
          'Běžný průměr je 110 mm, menší kolečka zrychlují reakce a zlehčují koloběžku, větší lépe udrží rychlost. Tvrdost PU určuje, jak rychle se kolečko obrušuje a jak se chová na hladkém betonu nebo hrubším asfaltu.</p>'
          '<h3>Jak poznat opotřebené kolečko</h3>'
          '<p>Kolečko je třeba vyměnit, když se plášť od jádra odděluje, když vznikne plochá hrana nebo když se neotáčí hladce. Změna obvykle vzniká postupně, proto se vyplatí občas přejet prstem po obvodu a zkontrolovat, zda je kolečko rovné. Pro rychlejší jízdu lze přidat kvalitní ložiska, která snižují odpor.</p>'
          '<h2>Gripy, pegy a doplňky</h2>'
          '<p>Grip páska se časem obrousí a ztrácí přilnavost. Výměna je jednoduchá, stačí starou odlepit a novou nalepit rovně na čistou desku. Pegy jsou kovové nebo plastové nástavce na osách, které umožňují grindy, tedy klouzání po hranách a zábradlích. '
          'Nasazují se jen tehdy, pokud je deska a osa na to uzpůsobena. Z doplňků se hodí také návleky na řídítka, ochranné prvky a sady nářadí.</p>'
          '<h2>Výběr podle stylu jízdy</h2>'
          '<ul><li><strong>Skatepark a rampy:</strong> lehká deska, tvrdé kolečko a pevné řídítka, hlavní je odolnost při dopadech a odezva při skoku.</li>'
          '<li><strong>Street a schody:</strong> silnější deska, pegy pro grindy a kolečka, která se snadno drží na hranách.</li>'
          '<li><strong>Začátečník:</strong> hotový komplet s přijatelnou hmotností. Nejdřív se naučte základní odrazy, a teprve pak investujte do dražších dílů.</li>'
          '<li><strong>Dítě:</strong> modely v menších velikostech a lehčí konstrukce, aby je dítě zvládlo zvednout při skoku.</li>'
          '<li><strong>Dospělí jezdci:</strong> kvalitnější materiály a vyšší nosnost, aby vydržely častější používání.</li></ul>'
          '<h2>Ochrana a bezpečnost</h2>'
          '<p>Freestyle jízda znamená pády, takže helma je základ. Zvolte lehkou přilbu s tvrdou skořepinou, která pokrývá spánky a zadní část hlavy. Další ochranu tvoří chrániče loktů, kolenou a zápěstí. '
          'U dětí kontrolujte, aby chrániče seděly bez posouvání. Výbavu najdete v kategoriích <a href="/chranice-a-helmy/">chrániče a helmy</a> a <a href="/cyklo-chranice/">chrániče pro cyklisty</a>. '
          'Další jízdu po prkně nebo kolečkách nabízejí <a href="/skateboardy/">skateboardy a longboardy</a>, <a href="/inline-brusle/">inline brusle</a> a skupina <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("core", "Core"), ("divine", "Divine"), ("striker", "Striker"), ("slamm", "Slamm"), ("chilli", "Chilli"), ("panda", "Panda"), ("ethic", "Ethic")) +
          '. Další nabídku mají ' + B(("ao", "AO"), ("street-surfing", "Street Surfing"), ("crisp", "Crisp"), ("proto", "Proto"), ("root-industries", "Root Industries"), ("d-young", "D-Young"), ("north", "North")) + '. '
          'Některé značky se zaměřují na kompletní koloběžky pro různé úrovně, jiné, například Core nebo Proto, na kolečka, desky a další díly. Vždy si ověřte, zda je produkt komplet, nebo jen jeden díl, protože se v nabídce mísí.</p>'
          '<h2>Údržba</h2>'
          '<p>Před jízdou zkontrolujte šrouby na vidlici, řídítkách a osách, protože se při dopadech uvolňují. Kolečka občas přeprohoďte nebo vyměňte, aby se obrušovala rovnoměrně. Ložiska čistěte od písku a lehce mažte, ale ne příliš, aby nenasávala prach. '
          'Po jízdě v dešti koloběžku osušte a mírně namažte kovové části, aby nekorodovaly. Pokud se při jízdě objeví vůle v hlavové sadě, dotáhněte ji ihned, protože hrozí poškození vidlice.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě městské nebo skládací koloběžky na triky. Neodolá nárazům a řídítka se mohou ulomit.</li>'
          '<li>Příliš těžký komplet pro dítě, které nedokáže koloběžku zvednout.</li>'
          '<li>Nesprávně vybrané kolečko nebo díl, který neodpovídá průměru osy.</li>'
          '<li>Podcenění helmy a chráničů. Úrazy při prvních pokusech o skok jsou časté.</li>'
          '<li>Nákup kompletu bez ověření, zda jde o koloběžku, nebo jen o desku či díl.</li></ul>'
          '<h2>Kdy kupovat</h2>'
          '<p>Nabídka roste od jara, kdy se otevírají skateparky, a před Vánoci. Po sezóně obchody uvolňují starší série, které se funkčně příliš nemění. Na Sportece sledujete u dílů i kompletů ceny z více obchodů najednou a snáz poznáte, kde je potřebná velikost skladem.</p>',
    faq=[
        ('Čím se freestyle koloběžka liší od běžné?', 'Má pevnější konstrukci, nesklápí se, jede na malých kolečkách z tvrdého polyuretanu a všechny díly jsou dimenzované na skoky a dopady. Běžná městská koloběžka by tvrdé triky nevydržela.'),
        ('Jakou velikost vybrat pro dítě?', 'Podívejte se na výšku řídítek, měla by končit zhruba u pasu až hrudníku. Pro menší děti jsou modely označené mini nebo junior a důležitá je i nízká hmotnost, aby dítě koloběžku zvedlo.'),
        ('Jak často se mění kolečka?', 'Záleží na stylu jízdy a povrchu. Vyměňte je ve chvíli, kdy je plášť poškozený, kolečko se kymácí nebo se špatně otáčí. Na hrubém asfaltu se obrušují rychleji než ve skateparku.'),
        ('Kolik mm mají obvykle kolečka?', 'Běžná velikost je 110 mm. Menší kolečka jsou obratnější, větší lépe drží rychlost. Při výměně vždy ověřte, zda průměr a šířka pasují do vidlice a pod desku.'),
        ('K čemu slouží pegy?', 'Jsou to nástavce na osách kol, které umožňují klouzat po hranách a zábradlích. Hodí se pro street jízdu, ale ne každá koloběžka je pro ně uzpůsobená.'),
        ('Dá se koloběžka na triky použít i na dojíždění?', 'Dá, ale není to její silná stránka. Malá kolečka a pevná řídítka dávají méně komfortu na nerovném povrchu a koloběžka se nesklápí, takže se hůř přenáší.'),
        ('Jak vyměnit grip pásku?', 'Starou pásku odlepte, desku očistěte od lepidla a prachu, novou nalepte od jednoho konce a vyhlaďte bublinky. Přebytečnou páku oříznete nožem podél hrany desky.'),
        ('Co udělat, když se řídítka uvolní?', 'Zkontrolujte upínací šrouby a hlavovou sadu, dotáhněte je imbusovým klíčem. Pokud vůle zůstává, díl vyměňte, protože jízda s vůlí poškozuje vidlici i desku.'),
        ('Je nutné nosit chrániče a helmu?', 'Pro začátečníky i pokročilé se důrazně doporučují. Úrazy při freestyle jízdě vznikají při pádech na tvrdý povrch. Nejdůležitější je helma, dále chrániče kolen, loktů a zápěstí.'),
        ('Jak poznám, jestli je produkt komplet, nebo jen díl?', 'Podívejte se do názvu a popisu. U kompletu je výraz freestyle koloběžka a název modelu, u dílu je uvedeno kolečko, grip, pegy nebo deska. V nejasných případech ověřte obsah balení u prodejce.'),
    ])

# ------------------------------------------------------------------ hokejove-puky-a-branky
NEW['hokejove-puky-a-branky'] = dict(long=True,
    title='Hokejové puky, branky a tréninkové pomůcky',
    desc='Hokejové puky, branky, střelecké pomůcky a fanouškovské repliky. Jak vybrat puk a branku na trénink doma i na led a porovnat nabídky obchodů.',
    intro='<p>Puk je nejmenší část hokejové výbavy, ale právě on určuje, jak se hraje. Tréninkové puky mají jinou hmotnost a tvrdost než zápasové, lehké modely se hodí pro děti a pro hru na asfaltu, a fanouškovské puky s logy klubů a hráčů slouží spíš jako sběratelský předmět. '
          'Kategorie zahrnuje také hokejové branky, střelecké plochy, sítě a další pomůcky pro trénink na zahradě, na parkovišti nebo ve sklepě.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u puků a branek značek FansArena, Winnwell, Inglasco, Merco, Green Biscuit, Mustang, Bauer nebo CCM. '
          'Ke střelbě se hodí <a href="/hokejky/">hokejky</a> a <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>, pro bezpečí <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>. '
          'Celý sport shrnuje skupina <a href="/hokej/">hokej</a>. Níže najdete přehled typů, rozdílů a rad pro nákup.</p>',
    guide='<h2>Co všechno kategorie obsahuje</h2>'
          '<p>Většinu nabídky tvoří puky, a to jak klasické černé tréninkové, tak fanouškovské s logy klubů z NHL a evropských lig nebo reprezentací. Druhou skupinou jsou hokejové branky, od malých dětských po velké, které odpovídají rozměrům pro mládež. '
          'Doplňují je střelecké pomůcky, sítě a dílčí součásti. Přehled usnadní uvedený rozdíl, protože se v jedné kategorii setká hra i sbírka.</p>'
          + T(['Typ', 'K čemu slouží', 'Co sledovat'], [
              ['Tréninkový puk', 'střelba, přihrávky, cvičení', 'hmotnost a tvrdost, vhodnost pro led nebo asfalt'],
              ['Lehký puk', 'děti a začátečníci', 'menší nárazy a menší nebezpečí úrazu'],
              ['Puk pro hru mimo led', 'asfalt, kluziště z plastu, parkoviště', 'materiál, který nehoří od tření'],
              ['Fanouškovský puk', 'sbírka, dárek, vitrína', 'uvedený klub, hráč a edice'],
              ['Podpisová replika', 'dárek pro fanouška', 'zda jde o potisk, nebo originální podpis'],
              ['Hokejová branka', 'trénink doma, zahrada, sklep', 'rozměr, rám, síť, stabilita'],
              ['Střelecká deska a terče', 'zlepšení přesnosti střelby', 'velikost a odolnost vůči nárazům']]) +
          '<h2>Hmotnost a tvrdost puku</h2>'
          '<p>Oficiální zápasový puk je z vulkanizované pryže a má stanovenou velikost i hmotnost. Tréninkové a dětské puky bývají lehčí, někdy barevné, aby byly vidět na sněhu i na trávě. '
          'Pro děti volte lehčí puk, který se snáze nahazuje a při chybě nezpůsobí bolestivý zásah. Hráči, kteří střílí na led, mají použít standardní puk, aby si zvykli na reálnou hmotnost. '
          'Při hře mimo led se používají ve vhodném provedení plastové nebo speciální puky, které snášejí tření o asfalt.</p>'
          '<h2>Branky pro trénink</h2>'
          '<p>Hokejová branka je rám s pevnou síťí. Při výběru sledujte rozměr, hmotnost a stabilitu, protože lehká branka při střelách odlétá. Na zahradě se hodí lehčí kovová nebo plastová konstrukce, která se dá rozložit a uložit. '
          'Branky pro děti mají menší rozměr, aby se do nich dalo střílet přesně. Plnohodnotné branky jsou větší, těžší a často je potřeba je zatížit pytlem s pískem nebo ukotvit. Důležité je i kvalitní síť, která zadrží střelu a nepropouští puk skrz oka.</p>'
          '<h3>Montáž a skladování</h3>'
          '<p>Branka se obvykle skládá z kovových trubek se spojkami. Před první hrou zkontrolujte, zda jsou spoje pevné, a po hře ji nenechávejte venku celý rok. Sníh a déšť poškozují síť i barvu rámu. '
          'Sundejte síť, pokud jedete na delší dobu pryč, a branku uložte do garáže nebo do sklepa.</p>'
          '<h2>Trénink mimo led</h2>'
          '<p>Hokejista, který trénuje celoročně, potřebuje i vybavení pro suchý trénink. Dobře se hodí střelecká plocha z plastu, na které puk klouže téměř jako po ledě, nebo tvrdý povrch, na kterém funguje plastový puk. '
          'Při tréninku na asfaltu mění materiál čepel, takže se vyplatí starší hůl nebo plastová čepel, aby se nezničil drahý kus. K tomu přidejte <a href="/hokejove-pasky-a-doplnky/">pásky, tkaničky a doplňky</a>, které se mezi tréninky rychle opotřebují.</p>'
          '<h2>Výběr podle věku a úrovně</h2>'
          '<ul><li><strong>Nejmenší děti:</strong> lehký puk a malá branka, hlavním cílem je zábava a základní návyky.</li>'
          '<li><strong>Mládež:</strong> standardní tréninkový puk, branka odpovídající rozměrům pro věkovou kategorii a střelecké terče.</li>'
          '<li><strong>Dospělí rekreační hráči:</strong> větší branky a puky pro hru v hale i venku.</li>'
          '<li><strong>Brankáři:</strong> branka s kvalitní sítí a tréninkové puky, které snesou stovky střel. Pro ochranu viz <a href="/hokejove-brankarske-vybaveni/">brankářská výstroj</a>.</li>'
          '<li><strong>Fanoušci a sběratelé:</strong> repliky a edice klubů, ke kterým se hodí <a href="/hokejove-suveniry-a-karty/">hokejové karty a suvenýry</a>.</li></ul>'
          '<h2>Fanouškovské a sběratelské puky</h2>'
          '<p>Značná část nabídky jsou puky s logy klubů NHL, reprezentačních týmů a s motivy konkrétních hráčů. Slouží jako dárek, sbírka nebo dekorace v pokoji a na hru se obvykle nehodí. '
          'Při koupi rozlišujte, zda jde o oficiální zápasový puk, replikou, nebo o fanouškovskou verzi s potiskem, a zda je podpis jen vytištěný. Pokud puk míříte darovat, zvažte vitrínu nebo držák, který ho chrání před poškrábáním. '
          'Dresy a fanouškovské oblečení najdete v kategorii <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("fansarena", "FansArena"), ("winnwell", "Winnwell"), ("inglasco", "Inglasco"), ("merco", "Merco"), ("green-biscuit", "Green Biscuit"), ("mustang", "Mustang")) +
          '. Další nabídku mají ' + B(("hock", "Hock"), ("bauer", "Bauer"), ("gufex", "Gufex"), ("potent-hockey", "Potent Hockey"), ("ccm", "Ccm"), ("strida-sport", "Střída Sport"), ("wincraft", "Wincraft"), ("tempish", "Tempish")) + '. '
          'Značka FansArena je zaměřena hlavně na fanouškovské edice, Winnwell a Inglasco nabízejí tréninkové puky a vybavení pro klubovou i rekreační hru a Bauer či CCM jsou obecně spojené s hokejovou výstrojí. Výrobce vždy porovnejte s popisem konkrétního produktu.</p>'
          '<h2>Péče a bezpečnost</h2>'
          '<p>Puky skladujte na suchém místě a před zimní sezónou je zchlaďte, protože studený puk po dopadu méně odskakuje. Při tréninku na zahradě dbejte na bezpečnost okolí: zaměřte branku tak, aby střely nelétaly na sousední pozemek, a použijte zábranu. '
          'Při hře dětí kontrolujte jejich <a href="/hokejove-helmy-a-mrizky/">helmu s mřížkou</a> a další chrániče. Po sezóně puky zkontrolujte a poškrábané vyřaďte, protože praskliny zvyšují riziko roztříštění.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Fanouškovský puk koupený na trénink. Potisk se rychle obrousí.</li>'
          '<li>Příliš velká branka pro malou zahradu nebo pro dítě.</li>'
          '<li>Lehká branka bez zatížení, která se při střelbě převrací.</li>'
          '<li>Použití tvrdého puku na hru mimo led bez vhodného povrchu.</li>'
          '<li>Podcenění ochrany. K tréninku patří helma a rukavice i doma na zahradě.</li></ul>'
          '<h2>Kdy kupovat</h2>'
          '<p>Nejvíc se prodává před zahájením sezóny a před Vánoci. Fanouškovské edice se objevují při velkých turnajích a draftu. Na Sportece sledujete vývoj nabídek v obchodech a vidíte, kde je konkrétní kus skladem. '
          'Pokud pořizujete výbavu celého týmu, porovnejte i <a href="/hokejove-tasky/">hokejové tašky a batohy</a> a <a href="/hokejove-brusle/">hokejové brusle</a>. Pro hru bez ledu hledejte i <a href="/florbal/">florbal</a> nebo <a href="/inline-brusle/">inline brusle</a>.</p>',
    faq=[
        ('Jaký puk je vhodný pro děti?', 'Pro nejmenší se hodí lehčí puk, který se snáze ovládá a při zásahu méně bolí. Starší mládež již trénuje se standardním pukem, aby si zvykla na reálnou hmotnost.'),
        ('Dá se hrát s puky mimo led?', 'Ano, pokud je puk určený pro tvrdý povrch nebo klouzavou plochu. Klasický gumový puk se na asfaltu rychle obrousí a je těžký, proto se pro dryland používají specializované modely.'),
        ('Jak velká má být branka pro zahradu?', 'Zvolte ji podle věku střelců a místa, které máte k dispozici. Menší branky jsou lepší pro děti a do malého prostoru, plnohodnotná branka je velká a těžká, a vyžaduje větší pozemek.'),
        ('Jak zabránit převrácení branky?', 'Zatížte ji pytlem s pískem nebo ji ukotvěte kolíky. Lehké branky z trubek se při tvrdých střelách pohybují a lze je převrátit i při bouřce nebo větru.'),
        ('Je fanouškovský puk vhodný ke hře?', 'Obvykle ne. Jde o dárkový nebo sběratelský předmět s potiskem, který se při střelbě obrousí. Ke hře kupujte tréninkový puk.'),
        ('Čím se liší replika od originálního puku?', 'Originál se používá v oficiálních zápasech nebo je jako takový označen. Replika vypadá stejně, ale může mít jinou hmotnost a materiál a slouží jako suvenýr.'),
        ('Jak skladovat puky?', 'Na suchém místě a mimo přímé slunce. Před tréninkem na led je dobré je ochladit, protože studený puk nepodskakuje. Praskliny a hluboké škrábance znamenají vyřazení.'),
        ('Co obsahuje střelecká plocha?', 'Je to hladká tvrdá deska, na které puk dobře klouže. Používá se doma i na zahradě k nácviku střelby a přihrávek bez ledu. Rozměr se volí podle prostoru.'),
        ('Je nutné nosit chrániče při tréninku na zahradě?', 'Doporučuje se aspoň helma s mřížkou a rukavice. Puk i hokejka zraní při chybném zásahu stejně jako v hale. Děti by měly trénovat pod dohledem dospělých.'),
        ('Jaké značky mají největší nabídku?', 'V kategorii je nejvíce FansArena, Winnwell a Inglasco, dále Merco, Green Biscuit, Mustang a Bauer. Nabídka se mění podle skladových zásob a sezóny.'),
    ])

# ------------------------------------------------------------------ beh
NEW['beh'] = dict(long=True,
    title='Běh, triatlon a atletika: vesty, opasky, tretry',
    desc='Běžecké vesty a batohy, opasky, atletické tretry, triatlonové obleky a pomůcky. Jak vybrat výbavu pro běh a porovnat nabídky českých obchodů.',
    intro='<p>Běh potřebuje málo, ale dobře zvolené vybavení znamená rozdíl mezi příjemným výběhem a trápením. Kategorie spojuje tři oblasti: dlouhé běhy v terénu, kde potřebujete vodu, jídlo a vrstvy v běžecké vestě, atletiku s tretrami, překážkami a vrhacími pomůckami a triatlon s obleky a doplňky pro plavání, kolo a běh.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Silva, Dynafit, Salomon, Merco, Deuter, Camelbak, Kiprun, Compressport nebo Mizuno. '
          'Hlavní podskupiny jsou <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>, <a href="/bezecke-opasky/">běžecké opasky a pouzdra</a>, <a href="/atletika/">atletika</a> a <a href="/triatlon/">triatlon</a>. '
          'K běhu patří také <a href="/bezecke-boty/">běžecké boty</a>, <a href="/trailove-boty/">trailové boty</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>. Níže najdete přehled, jak si vybrat.</p>',
    guide='<h2>Co kategorie obsahuje</h2>'
          '<p>Největší část nabídky tvoří běžecké vesty a batohy, které se při terénním běhu nosí těsně na těle, a druhou tvoří běžecké opasky na láhev, telefon a drobnosti. '
          'Dále najdete atletické tretry, hroty, překážky, pěnové oštěpy pro děti a další pomůcky z atletiky a také triatlonové obleky, neopreny, pásy na startovní čísla a doplňky. '
          'V nabídce se objeví i pár položek, které jen sousedí s během, například vrhací tyče nebo oštěpy z jiných sportů, takže se vždy držte popisu produktu.</p>'
          + T(['Podkategorie', 'Co obsahuje', 'Pro koho'], [
              ['Běžecké vesty a batohy', 'vesty s kapsami, vaky na vodu, batohy na trail', 'trailoví běžci, ultra a horské závody'],
              ['Běžecké opasky a pouzdra', 'opasky na láhev, telefon, klíče a gely', 'běh po městě, kratší tratě'],
              ['Atletika', 'tretry, hroty, překážky, pomůcky pro skoky a vrhy', 'dětské oddíly a atleti'],
              ['Triatlon', 'neopreny, kombinézy, pásy na číslo, čepice', 'triatlonisté a plavci v otevřené vodě']]) +
          '<h2>Běžecká vesta, batoh, nebo opasek</h2>'
          '<p>Rozhodnutí závisí na délce běhu a na tom, co musíte vzít. Při krátkém výběhu stačí klíče a telefon, které pojme opasek nebo malá kapsa. Na půldenní trail už potřebujete vodu, jídlo, bundu a mobil v dosahu ruky, což zvládne vesta s přední kapsou. '
          'Při horských závodech s povinnou výbavou se hodí větší vesta s objemem několika litrů.</p>'
          + T(['Typ', 'Kapacita', 'Výhoda', 'Nevýhoda'], [
              ['Opasek', 'telefon, klíče, malá láhev', 'nehřeje na zádech, lehký', 'při větší zátěži poskakuje'],
              ['Malá vesta (kolem 5 litrů)', 'voda, gely, bunda', 'sedí těsně, rychlý přístup', 'omezený prostor'],
              ['Větší vesta (8 a více litrů)', 'povinná výbava, vrstvy, jídlo', 'vhodná na ultra a hory', 'víc hřeje, je těžší'],
              ['Batoh s vakem na vodu', 'dlouhé běhy a túry', 'velký objem a pití bez zastavení', 'méně přiléhavý, odřený hlavně na zádech']]) +
          '<h3>Velikost a nastavení vesty</h3>'
          '<p>Vesta se vybírá podle obvodu hrudníku a výrobce uvádí rozsah pro každou velikost. Správně sedí těsně, aniž by bránila dýchání, a při běhu se nehoupe. Nastavte popruhy na prsou tak, aby se nepohyboval ani plný objem, a přední kapsy pomocí gumiček. '
          'Vyzkoušejte vestu s plnými lahvemi nebo vakem, protože prázdná sedí jinak. Dámské modely mají užší střih a přizpůsobené popruhy.</p>'
          '<h3>Pití a jídlo</h3>'
          '<p>Většina vest má přední kapsy na měkké láhve a dovoluje zasunout i vak na vodu. Měkké láhve se zmenšují s množstvím vody, takže nebouchají. Gely a tyčinky patří do kapes u ramen, aby je šlo vytáhnout za běhu. Na rovinky a po městě vám stačí menší láhev na opasku, delší běhy v horách vyžadují větší zásobu a znalost trasy s možností doplnění vody.</p>'
          '<h2>Atletika</h2>'
          '<p>Atletika zahrnuje sprinty, skoky, vrhy a překážky. Základem jsou atletické tretry, jejichž konstrukce se liší podle disciplíny. Sprinterské hroty mají tuhou podrážku a plochu pro hroty pod přední částí chodidla, dálkařské jsou více odpružené a vytrvalostní mají lehčí a pohodlnější podrážku. '
          'Tretry se nehodí na asfalt, kde se hroty opotřebují. Děti mohou začít s lehkými překážkami a pěnovými oštěpy, které jsou bezpečné a učí techniku bez rizika zranění. Pro trénink doma pomůže <a href="/funkcni-trenink/">funkční trénink</a> a pro zotavení <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>'
          '<h2>Triatlon</h2>'
          '<p>Triatlon spojuje plavání, kolo a běh, takže výbava je trojí. Základ tvoří triatlonová kombinéza, která se nosí po celou dobu závodu, a při plavání v chladnější vodě triatlonový neopren, který je tenčí a pružnější v ramenou než surfařský. '
          'Dalším doplňkem je pás na startovní číslo, který se otáčí z cyklistické pozice na běžeckou, a silikonová čepice. K plavání patří i <a href="/plavecke-bryle/">plavecké brýle</a>. Triatlon zahrnuje i cyklistiku, viz kategorie <a href="/cyklistika/">cyklistika</a>. '
          'Při první účasti si před závodem vyzkoušejte přechody mezi disciplínami, protože při převlékání se ztrácí nejvíc času.</p>'
          '<h2>Výběr podle terénu</h2>'
          '<ul><li><strong>Městský běh:</strong> opasek nebo malé pouzdro na telefon, reflexní prvky pro večerní běhy.</li>'
          '<li><strong>Trail a hory:</strong> vesta s přední kapsou na vodu, na bundu a na povinnou výbavu, vhodné <a href="/trailove-boty/">trailové boty</a>.</li>'
          '<li><strong>Dráha a stadion:</strong> atletické tretry podle disciplíny, na delší tratě lehké a pohodlné.</li>'
          '<li><strong>Triatlon:</strong> kombinéza, neopren, pás na číslo a čepice. Zkontrolujte pravidla závodu.</li>'
          '<li><strong>Děti a mládež:</strong> lehké překážky, pěnové oštěpy a bezpečné pomůcky, které se rychle učí.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("silva", "Silva"), ("dynafit", "Dynafit"), ("salomon", "Salomon"), ("merco", "Merco"), ("deuter", "Deuter"), ("camelbak", "Camelbak"), ("kiprun", "Kiprun")) +
          '. Další nabídku mají ' + B(("compressport", "Compressport"), ("powershot", "Powershot"), ("van-rysel", "VAN Rysel"), ("mizuno", "Mizuno"), ("sedco", "Sedco"), ("jipast", "Jipast"), ("swix", "Swix")) + '. '
          'Salomon a Dynafit patří k významným výrobcům trailových vest, Camelbak a Deuter jsou známé vaky a batohy na pití, Compressport nabízí opasky a kompresní doplňky a Mizuno atletické tretry. Porovnejte objem, střih a materiál u konkrétního modelu.</p>'
          '<h2>Péče o vybavení</h2>'
          '<p>Vestu po běhu vyvěste, aby proschla, a občas ji ručně vyperte ve vlažné vodě s jemným čisticím prostředkem. Vaky na vodu čistěte vodou s jedlou sodou nebo speciálním přípravkem a skladujte je v lednici nebo nechte dobře vysušit, jinak se v nich vytvoří plíseň. '
          'Tretry vysušte při pokojové teplotě a pravidelně kontrolujte hroty. Neopren po triatlonu opláchněte sladkou vodou a sušte ve stínu. Další poznatky o neoprenu najdete u kategorie <a href="/neopreny/">neopreny</a> a jejich údržbě.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš velká vesta, která se při běhu houpe a odírá.</li>'
          '<li>Nákup podle objemu bez vyzkoušení s plnými lahvemi.</li>'
          '<li>Tretry na asfalt a nevhodná disciplína, hroty se opotřebují.</li>'
          '<li>Opasek přetížený telefonem a lahví, který tlačí na žaludek.</li>'
          '<li>Použití neoprenu poprvé až na závodě, bez vyzkoušení v otevřené vodě.</li></ul>'
          '<h2>Kdy a jak nakupovat</h2>'
          '<p>Největší nabídka je na jaře před závodní sezónou. Po sezóně se objevují starší modely vest a tretry. Na Sportece sledujete u konkrétních kusů ceny v několika obchodech a vidíte skladovost velikostí. '
          'Při výběru vesty přidejte i hodinky z kategorie <a href="/sportovni-hodinky/">sportovní hodinky</a>, pro horské běhy další výbavu z oblasti <a href="/outdoor/">outdoor</a>.</p>',
    faq=[
        ('Jak velkou běžeckou vestu zvolit?', 'Pro běh na dvě až tři hodiny stačí kolem pěti litrů, na delší horské závody je lepší větší vesta s místem na vrstvy. Důležitější než objem je správně sedící střih bez houpání.'),
        ('Čím se liší vesta od běžeckého batohu?', 'Vesta sedí těsně a má kapsy vpředu, takže se k pití dostanete za běhu. Batoh má větší objem na zádech a bývá volnější. Pro rychlejší běh se obvykle volí vesta.'),
        ('Kdy stačí opasek?', 'Na kratší trasy, kdy potřebujete telefon, klíče a malou láhev. Opasek nezahřívá záda, ale při větším nákladu poskakuje, proto se nehodí na delší trailové běhy.'),
        ('Jak poznám správnou velikost vesty?', 'Změřte obvod hrudníku a srovnejte s tabulkou výrobce. Vesta musí těsně obepínat tělo bez tlaku na dýchání. Vyzkoušejte ji s naplněnými lahvemi nebo vakem.'),
        ('Jak vyčistit vak na vodu?', 'Po použití ho vypláchněte čistou vodou a nechte úplně vyschnout, nejlépe rozevřený. Občas použijte jedlou sodu nebo čisticí tablety, jinak se v hadičce usazuje plíseň.'),
        ('Jsou atletické tretry vhodné i na asfalt?', 'Ne, hroty se rychle opotřebují. Tretry používejte na dráze nebo na tvrdém umělém povrchu a na silnici běhejte v běžeckých botách.'),
        ('Jak začít s atletikou u dětí?', 'S lehkými překážkami a pěnovými oštěpy, které nevyžadují zkušenosti a snižují riziko zranění. Technika a zábava mají přednost před výkonem a oddíl pomůže s výběrem disciplíny.'),
        ('Co potřebuji na první triatlon?', 'Plavky nebo kombinézu, brýle, čepici, kolo s přilbou a běžecké boty. Neopren se hodí v chladnější vodě a pás na číslo usnadní přechod. Vždy ověřte pravidla konkrétního závodu.'),
        ('Mám pro trail kupovat trailové boty?', 'Doporučují se, protože mají agresivnější podrážku a lepší přilnavost na blátě a kamení. Ve vyšších horách pomůže i stabilní střih a ochrana špičky.'),
        ('Jak dlouho vydrží běžecká vesta?', 'Při správné péči mnoho sezón. Nejdřív se opotřebují gumičky, zipy a popruhy, ty lze někdy vyměnit. Neperte ji v pračce s aviváží a nesušte ji na topení.'),
    ])

# ------------------------------------------------------------------ doplnění sekcí
NEW['fotbalove-mice']['guide'] += (
    '<h2>Jak míč testovat před nákupem</h2>'
    '<p>Pokud máte možnost míč vzít do ruky, udělejte tři jednoduché zkoušky. Zmáčkněte ho palcem: kvalitní míč se vrací do tvaru a nepůsobí jako prázdná skořápka. '
    'Pusťte ho z výšky přibližně do pasu a sledujte, zda odskočí přímo nahoru a ne šikmo, protože šikmý odskok prozrazuje nepravidelný měchýř. Položte ho na rovnou plochu a roztočte, kulatý míč se točí bez kymácení. '
    'Při nákupu online tyto zkoušky nahradí recenze a popis konstrukce. Zaměřte se na počet panelů, typ spojení a materiál vnějšího obalu.</p>'
    '<h2>Míč jako součást tréninku</h2>'
    '<p>Dobře zvolený míč zlepšuje techniku už od základů. Děti se učí žonglovat s lehčím míčem, který se nevyhýbá kolenům ani chodidlům, a dospělí si na menší míč, například velikosti 4, procvičují cit pro dotek. '
    'Při tréninku přihrávek pomáhá míč s výraznými panely, protože je vidět rotace. Sady více míčů ocení trenéři, kteří potřebují rychle střídat cvičení. '
    'Brankáři se chytání učí na míčích stejné hmotnosti, jaké budou chytat v zápase. Souvisí s tím obuv i ochrana, proto zvažte i <a href="/kopacky/">kopačky</a> podle povrchu a <a href="/fotbalove-chranice-a-stulpny/">chrániče</a>.</p>'
    '<h2>Míče pro jiné sporty s nohou</h2>'
    '<p>Fotbalový míč se někdy používá i v příbuzných hrách, ale ne vždy je to dobrý nápad. Pro hru v tělocvičně volte futsalový nebo měkký školní míč, pro ragby a americký fotbal potřebujete úplně jiný, vejčitý tvar, který najdete v oblasti <a href="/ragby-a-americky-fotbal/">ragby a americký fotbal</a>. '
    'Plážové míče a míče na streetball mají lehčí povrch a jinou odrazivost. Pokud kupujete dárek, ověřte, zda dárek obdarovaný skutečně potřebuje míč pro hru, nebo spíš sběratelský kousek.</p>')
NEW['fotbalove-mice']['faq'] += [
    ('Jak poznám, že je míč kulatý?', 'Roztočte ho na rovné ploše a sledujte, zda se kymácí. Při pádu z výšky pasu musí odskočit přímo nahoru. Šikmý odskok svědčí o nepravidelném měchýři nebo deformaci.'),
]
NEW['freestyle-kolobezky']['guide'] += (
    '<h2>První pokusy a postup učení</h2>'
    '<p>Začátečník se nejdřív učí stabilně stát na desce, odrážet se oběma nohama a bezpečně brzdit. Teprve potom přijdou na řadu malé hopy, ollie a otáčky o 180 stupňů. Většina úrazů vznikne tím, že jezdec přeskočí základní krok a jde rovnou na rampu. '
    'Procvičujte na rovném hladkém povrchu mimo provoz, ideálně na hřišti nebo v prázdném skateparku. Videa a zkušení jezdci ve skateparku dají spoustu rad zdarma. Pomůže i trpělivost, protože první čisté triky se obvykle objeví až po týdnech pravidelného tréninku.</p>'
    '<h2>Materiály desky a vidlice</h2>'
    '<p>Nejčastěji se používá hliník, který je lehký a dobře snáší nárazy, a u některých modelů ocel pro vyšší odolnost. Hliník je pro většinu jezdců nejlepší kompromis mezi hmotností a pevností. '
    'Vidlice a řídítka z oceli jsou těžší, ale houževnatější, takže se hodí pro hrubší jízdu. Při výběru se řiďte tím, zda je produkt určený pro začátečníky, nebo pro zkušené jezdce, a nehonťte se zbytečně za nejlehčí konstrukcí, pokud děláte spíš rovné skoky než složité triky.</p>'
    '<h2>Jiné způsoby jízdy na kolečkách</h2>'
    '<p>Pokud freestyle koloběžka nevyhovuje, vyzkoušejte příbuzné sporty. Skateboard nabízí podobnou kulturu triků, ale vyžaduje jiný balanc, inline brusle jsou vhodnější na dlouhé jízdy a elektrokoloběžky na dojíždění. '
    'Mnoho jezdců nakonec střídá více vybavení podle nálady a počasí, a proto se rozcestník <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a> vyplatí projít celý.</p>')
NEW['freestyle-kolobezky']['faq'] += [
    ('Jak se naučit první triky?', 'Začněte jízdou, odrazem a brzděním na rovném povrchu, pak malými hopy a otočkou o 180 stupňů. Skákání do rampy s nedostatečným základem končí většinou zraněním.'),
]
NEW['hokejove-puky-a-branky']['guide'] += (
    '<h2>Střelba a přesnost</h2>'
    '<p>Základem dobré střelby je opakování a kontrola techniky, nikoli výkon. Střelecká plocha s terči nebo vyříznutými otvory v síti pomáhá trefit konkrétní místo v brance a odhalit, zda střílíte stále na stejnou stranu. '
    'Zkuste postupně měnit vzdálenost od branky a typ střely, od přihrávkové po prudkou. Zapisujte si počet zásahů z deseti pokusů a po týdnu uvidíte, jestli se trefujete přesněji. '
    'Trénink brankářů vyžaduje střelce s kvalitním puky a bezpečné prostředí, jinak se z tréninku stane riziko.</p>'
    '<h2>Hra v hale, na kluzišti a venku</h2>'
    '<p>Na ledě platí oficiální pravidla, ale pro hru mimo led si zvolte vybavení podle povrchu. Na kluzišti z umělé hmoty se hodí plastový puk, na asfaltu a betonu tvrdší plastové kolečko, které se při hře neroztříští. '
    'Na sněhu a v zimě mohou venku fungovat i běžné tréninkové puky, ale po dešti rychle nasáknou. Pro dětské hry v tělocvičně existuje také <a href="/florbal/">florbal</a> s míčkem a <a href="/florbalove-hole/">florbalové hole</a>, který je bezpečnější než hokej s tvrdým pukem.</p>'
    '<h2>Pozemní hokej a příbuzné sporty</h2>'
    '<p>Podobné hry používají jiné vybavení a jiné míčky nebo puky. Pozemní hokej má vlastní kategorii <a href="/pozemni-hokej/">pozemní hokej</a> a tvrdý míček, florbal plastový dutý míček. Nezaměňujte tyto pomůcky, protože odlišné rozměry znamenají nevhodný trénink a při hře hrozí zranění.</p>')
NEW['hokejove-puky-a-branky']['faq'] += [
    ('Jak se zlepšit ve střelbě?', 'Opakujte střelbu na terče nebo konkrétní místa v brance a zapisujte počet zásahů. Střídejte vzdálenost a typ střely a kontrolujte techniku na videu.'),
]
NEW['beh']['guide'] += (
    '<h2>Příprava na první závod</h2>'
    '<p>Pro první závod v terénu si nejdřív přečtěte pravidla a povinnou výbavu, kterou pořadatel uvádí na stránkách. Většinou jde o vodu, mobil, základní lékárničku, fólii a čelovku, případně také nepromokavou bundu. '
    'Vybavení pak naskládejte do vesty doma a vyzkoušejte s ním delší výběh, abyste věděli, kam co patří a nic vám neskřípe. Při závodě je zbytečné objevovat nové věci, takže vše vyzkoušejte předem v podobných podmínkách. '
    'Zvlášť důležité jsou ponožky a boty, kde se nejčastěji tvoří puchýře, proto se vyplatí podívat se i na <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>'
    '<h2>Doplňky pro bezpečný běh</h2>'
    '<p>Reflexní prvky a čelovka jsou základ pro běh za šera. Reflexní vesta nebo pásky na rukou a kotnících zvyšují viditelnost, na stezkách bez osvětlení je nutná čelovka s dostatečným svitem. '
    'Pomáhají také hodinky nebo telefon s navigací, které vás vrátí na trasu. Při horkém počasí chraňte hlavu čepicí a na slunci použijte opalovací krém. Při chladném počasí se obléká po vrstvách, takže vesta nebo batoh musí pojmout i rukavice a tenkou bundu.</p>'
    '<h2>Regenerace po běhu</h2>'
    '<p>Po delším běhu se vyplatí protáhnout lýtka, stehna a zadní stranu nohou a doplnit tekutiny. Odlehčení svalům poskytnou <a href="/masazni-pomucky/">masážní pomůcky</a>, například válec nebo míček, a na nohy příjemně působí lehké kompresní návleky nebo ponožky. '
    'Při opakovaných bolestech se poraďte s fyzioterapeutem, protože nesprávná technika nebo nevhodné boty se časem projeví na kloubech.</p>')
NEW['beh']['faq'] += [
    ('Co s sebou na první terénní závod?', 'Vždy vodu, mobil, fólii, lékárničku a bundu podle povinné výbavy pořadatele. Vše doma naskládejte do vesty a vyzkoušejte při tréninku.'),
]

NEW['freestyle-kolobezky']['guide'] += (
    '<h2>Kam jezdit</h2>'
    '<p>Nejlepším místem na učení je skatepark s hladkým betonem a rampami různých výšek, kde se jezdci vzájemně sledují a radí. Veřejná prostranství, schody a zábradlí jsou lákavé, ale často je tam zakázáno jezdit, nebo hrozí střet s chodci. '
    'Před jízdou si zjistěte pravidla parku, někde platí povinná helma a časová omezení pro různé typy sportovního náčiní. Do parku si vezměte vodu, náhradní imbusový klíč a v zimě rukavice, protože tvrdé kovové řídítka v mrazu bolí.</p>')
NEW['hokejove-puky-a-branky']['guide'] += (
    '<h2>Doplňky k brance</h2>'
    '<p>K brance se vyplatí přidat několik drobností: pytel s pískem na zatížení, náhradní síť, kolíky na ukotvení a ochrannou plachtu za brankou, aby puky nelétaly mimo. Pro děti pomůže také označení hrací plochy páskou, aby věděly, odkud střílet. '
    'Pokud trénujete s kamarády, připravte si několik puků najednou, protože sbírání po každé střele zdržuje a trénink ztrácí tempo. Seznam rozumné výbavy najdete v kategorii <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>.</p>')

NEW['freestyle-kolobezky']['guide'] += (
    '<h2>Pro koho se freestyle hodí</h2>'
    '<p>Freestyle jízda přitahuje děti od školního věku po dospělé, kteří chtějí aktivní koníček. Ve srovnání se skateboardem se dá rychleji naučit základní stabilita, proto je koloběžka častým prvním krokem k sportům na kolečkách. '
    'Na dojíždění a rekreační jízdu po městě však spíš zvolte <a href="/kolobezky/">klasické koloběžky</a> a pro delší trasy <a href="/elektrokolobezky/">elektrokoloběžky</a>. Pokud se vám při pádech nechce spoléhat jen na helmu, doplňte ji o <a href="/cyklo-chranice/">chrániče</a> na kolena a lokty.</p>')
NEW['freestyle-kolobezky']['faq'] += [
    ('Dá se freestyle koloběžka půjčit nebo vyzkoušet?', 'Mnoho skateparků a jezdeckých skupin nabízí vyzkoušení, ale půjčovny jsou spíš výjimkou. Zeptejte se zkušených jezdců, kteří vám dovolí projet se na jejich koloběžce a poradí s velikostí.'),
]
NEW['hokejove-puky-a-branky']['faq'] += [
    ('Kolik puků mít na trénink?', 'Pro samostatný trénink stačí kolem deseti kusů, pro skupinu více. Čím víc puků máte po ruce, tím méně času ztrácíte sbíráním a tím víc střel stihnete.'),
    ('Jak vybrat dárek pro hokejového fanouška?', 'Podívejte se na oblíbený klub nebo hráče a vyberte puk či repliku s jeho motivem. Dárek doplňte vitrínou, držákem nebo hokejovou kartou, aby se puk dal bezpečně vystavit.'),
]
NEW['beh']['faq'] += [
    ('Jak si vybrat opasek na telefon?', 'Zkontrolujte, zda se do kapsy vejde váš telefon i s pouzdrem, a vyzkoušejte, jak opasek drží při běhu. Dobrý opasek neposkakuje, netlačí na břicho a dá se rychle otevřít.'),
    ('Potřebuji čelovku na běh?', 'Při běhu za šera nebo v lese ano, kdežto na osvětlených trasách stačí reflexní prvky. Čelovka s dostatečným svitem a náhradními bateriemi je často součástí povinné výbavy závodu.'),
]
NEW['beh']['guide'] += (
    '<h2>Trénink a plán</h2>'
    '<p>Výbava sama výkon nezlepší. Nejdůležitější je pravidelnost a postupné zvyšování zátěže, aby se tělo přizpůsobilo. Začátečníci střídají chůzi a běh, mírně prodlužují úseky a nechávají si dny na odpočinek. '
    'Pokud trénujete na závod, přidejte i běh v terénu a na nerovném povrchu, aby se posílily kotníky a stabilizační svaly.</p>')
