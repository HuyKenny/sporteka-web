"""sporteka.cz — brand texts wave 210: bauer, peak-mountain, helly-hansen, palladium.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bauer
NEW['bauer'] = dict(
    title='Bauer: hokejové brusle, hokejky a výstroj pro děti i dospělé',
    desc='Bauer v katalogu Sporteky: hokejové brusle, hokejky, chrániče, brankářská výstroj a florbal. Jak vybrat řadu, velikost a kdy hledat slevy.',
    intro='<p>Bauer je v katalogu Sporteky především hokejová značka. Největší skupinou jsou <a href="/hokejky/">hokejky</a>, hned za nimi <a href="/brusle/">zimní brusle</a>, <a href="/hokejove-chranice/">hokejové chrániče</a> a <a href="/hokejove-brankarske-vybaveni/">brankářská výstroj</a>. K tomu přibývá florbal, inline brusle a část sportovního oblečení, tedy trička, mikiny a čepice se značkovým logem.</p>'
          '<p>Podle filtrů míří většina zboží na děti a mládež, dospělé modely tvoří menší část a výrazně převažuje černá barva. Ve výpisu se opakují řady s označením Vapor, Supreme, X, Prodigy nebo Rookie a zkratky SR, INT, JR a YTH, které říkají, pro jakou věkovou a výkonnostní skupinu je kus určen. Stránka vysvětluje, jak se v nich vyznat, čím se brusle liší od hokejky z hlediska výběru, jak sladit velikosti a kdy se vyplatí porovnávat nabídky obchodů, aby nákup vyšel levněji.</p>',
    guide='<h2>Co Bauer v katalogu nabízí</h2>'
          '<p>Nabídku značky nejlépe popíše pohled na kategorie, ve kterých se její produkty objevují. Žádná jiná oblast nemá takovou váhu jako hokej, ale dole se ukazují i položky mimo led.</p>'
          + T(['Oblast', 'Co v ní najdete', 'Pro koho je vhodná'], [
              ['<a href="/hokejky/">Hokejky</a>', 'kompozitní a dřevěné hole, komplety pro nejmenší, brankářské hole', 'od začátečníků po aktivní hráče'],
              ['<a href="/brusle/">Zimní brusle</a>', 'hokejové brusle, rekreační modely, náhradní nože, nastavitelné brusle', 'děti, mládež, dospělí'],
              ['<a href="/hokejove-chranice/">Hokejové chrániče</a>', 'kalhoty, rukavice, kolenní a loketní chrániče, vesty', 'všechny věkové kategorie'],
              ['<a href="/hokejove-brankarske-vybaveni/">Brankářská výstroj</a>', 'brankářské brusle, hole, lapačky a vyrážečky', 'brankáři v týmech i na tréninku'],
              ['<a href="/florbal/">Florbal</a>', 'florbalové hole, boty a doplňky', 'školní a klubový florbal'],
              ['<a href="/inline-brusle/">Inline brusle</a>', 'letní brusle pro hokejový styl bruslení', 'hráči i rekreační jezdci'],
              ['Oblečení a čepice', 'trička, mikiny, kalhoty, kšiltovky a zimní čepice', 'fanoušci a volný čas']]) +
          '<p>Kdo hledá jen jednu věc, třeba bruslařský nůž nebo vyrážečku, může do vyhledávání přímo název modelu, protože prodejci obvykle uvádějí celé označení včetně velikostní kategorie a ročníku. Ročník bývá součástí názvu, například S24 nebo S26, a starší ročníky bývají levnější. Podrobnější nabídku značky v hokejkách shrnuje stránka <a href="/bauer-hokejky/">Bauer hokejky</a> a v inline bruslích stránka <a href="/inline-brusle-bauer/">inline brusle Bauer</a>.</p>'
          '<h2>Jak číst označení SR, INT, JR a YTH</h2>'
          '<p>Hokejová výstroj se na rozdíl od běžných bot a oblečení dělí nejen podle velikosti, ale hlavně podle věkové a výkonnostní kategorie. Přesné rozměry každé řady stanovuje výrobce, proto se vždy dívejte do tabulky u konkrétního produktu.</p>'
          + T(['Zkratka', 'Význam', 'Komu obvykle sedí'], [
              ['SR (Senior)', 'dospělí', 'dospívající a dospělí hráči'],
              ['INT (Intermediate)', 'mezistupeň mezi mládeží a dospělými', 'starší dorost, menší dospělí'],
              ['JR (Junior)', 'mládež', 'školní děti zhruba od ukončení první třídy'],
              ['YTH (Youth)', 'nejmladší hráči', 'děti, které se učí bruslit a hrát'],
              ['Rec / Rookie / Lil', 'rekreační nebo nejlehčí řady', 'začátečníci a hobby bruslení']]) +
          '<p>Věkové hranice nejsou přísné. Rozhodující je výška, váha a síla hráče. Dítě, které rychle roste, nepotřebuje mnohem větší hokejku, ale lepší je trefit správnou délku. U chráničů naopak hledáme tvar, který kryje klouby, aniž by omezoval pohyb.</p>'
          '<h2>Brusle: tvar, šířka a výběr řady</h2>'
          '<p>Bruslařská bota je nejdůležitější a nejnáročnější část výbavy. Brusle musí držet patu, aby noha nepřetáčela, ale nesmí tlačit v palci nebo v nártu. Většina výrobců používá pro hokejové brusle užší tvar paty a pro volnější styl dává na výběr širší střih. Podívejte se do popisu produktu, zda je označena šířka, třeba D (běžná) a EE (širší), a porovnejte ji s tím, co jste nosili dosud.</p>'
          '<ul><li><strong>Velikost bruslí bývá o jednu až dvě čísla menší</strong> než velikost běžné obuvi. Změřte nohu v centimetrech a použijte tabulku výrobce.</li>'
          '<li><strong>Vyšší řady</strong> mají tužší skořepinu, přesnější podporu kotníku a lehčí jazyk. Hodí se pro ty, kdo hrají pravidelně a potřebují rychlý přenos síly.</li>'
          '<li><strong>Nižší řady</strong> bývají měkčí, snesou hodiny volného bruslení a jsou lepší pro děti, které rychle vyrostou.</li>'
          '<li><strong>Nastavitelné brusle pro nejmenší</strong> (označené zkratkou ADJ) se prodlouží o několik velikostí a přežijí tak víc sezón. Hodí se tam, kde cílem je radost z ledu, nikoli výkon.</li>'
          '<li><strong>Náhradní nože a držáky</strong> se prodávají zvlášť. Pokud hráč na ledě drhne nožem o zábradlí, je často levnější vyměnit nůž než celou brusli.</li></ul>'
          '<p>Brankářské brusle jsou zvláštní kategorie. Mají nižší a pevnější nůž, který chrání před zraněním od puku a umožňuje boční posuny. Nepoužívejte je pro hru v poli ani naopak. Nabídku dětských modelů najdete v přehledu <a href="/detske-zimni-brusle/">dětské zimní brusle</a>, zatímco dospělým pomůže stránka <a href="/panske-zimni-brusle/">pánské zimní brusle</a>. Společně s tím je dobré projít i <a href="/hokejove-brusle/">hokejové brusle</a> jako celek.</p>'
          '<h2>Hokejky: flex, délka a zakřivení</h2>'
          '<p>U hokejky rozhodují tři parametry. Prvním je délka, kterou měříme tak, aby hokejka při stoji na bruslích sahala mezi bradu a nos. Druhým je flex, tedy tuhost, která se udává číslem a velmi hrubě odpovídá polovině tělesné váhy hráče. Třetím je zahnutí čepele, které ovlivňuje, jak se puk nabírá a střílí. Pro začátek volte běžný průměrný tvar, zkušenější hráči si sami zvolí podle stylu hry.</p>'
          + T(['Parametr', 'Co určuje', 'Praktická rada'], [
              ['Délka', 'ovladatelnost puku a držení těla', 'u dětí raději kratší, ať se nenaučí hrbit'],
              ['Flex', 'jak se hůl prohne při střele', 'příliš tuhá hůl dítěti nepomůže, spíš ho zbrzdí'],
              ['Čepel', 'zakřivení a směr (levá, pravá)', 'drží-li hráč levou rukou dole, volí levou čepel'],
              ['Materiál', 'dřevo, kompozit', 'dřevo je levné a odolné, kompozit lehčí a přesnější'],
              ['Komplet', 'hůl a čepel v jednom kuse', 'u začátečníků praktické, u pokročilých se vyměňuje čepel zvlášť']]) +
          '<p>Hokejka pro brankáře má jiný tvar: širší dolní část, rovnější čepel a větší úhel zlomu. Nezaměňujte ji s hůlkou do pole. Pokud shánite náhradu pouze za čepel nebo násadu, existují samostatné kategorie <a href="/hokejove-cepele-a-nasady/">hokejové čepele a násady</a>. Další značky hokejek najdete na stránkách <a href="/znacka/ccm/">CCM</a> a <a href="/znacka/warrior/">Warrior</a>.</p>'
          '<h2>Chrániče a ochranné vybavení</h2>'
          '<p>Základem je celá sada, která chrání hlavu, ramena, lokty, rukavice, kyčle, kolena a holeně. Při nákupu respektujte pravidlo, že chránič má na těle ležet pevně a nesmí se pohybovat při bruslení. Příliš velký se při pádu posune a odhalí kloub, příliš malý omezuje pohyb. Kategorie <a href="/chranice-a-helmy/">chrániče a helmy</a> shrnuje obecný přehled, zatímco <a href="/hokejove-chranice/">hokejové chrániče</a> nabízí konkrétní kusy.</p>'
          '<ul><li><strong>Helma:</strong> musí sedět rovně na čele a nesmí se kývat. Vnitřní pěna se po nárazu poškodí, takže vybírejte novou přilbu nebo prověřenou, nepoškozenou.</li>'
          '<li><strong>Rukavice:</strong> prsty mají mít mírnou vůli, dlaň nesmí škrtit, zápěstí kryje delší manžeta.</li>'
          '<li><strong>Kalhoty:</strong> kryjí boky a stehna a mají sedět tak, aby chránič sahal ke kolenní ochraně.</li>'
          '<li><strong>Chrániče holení:</strong> měří se od středu kolene po botu, kratší kus nechá odkrytý kloub.</li></ul>'
          '<h2>Brankářská výstroj</h2>'
          '<p>Brankář nosí těžší a robustnější vybavení než hráč v poli. Mezi produkty se objevují brankářské brusle, hokejky, lapačky, vyrážečky a části výstroje, které se kupují zvlášť. Velikost a tuhost chráničů musí odpovídat věku i hmotnosti, protože příliš velký kus se špatně pohybuje, zatímco příliš malý nechává otevřená místa. Pokud kupujete brankářskou výstroj pro dítě, počítejte s tím, že rychle vyroste, a zvažte i bazarové nebo starší série. Ostatní hokejové zboží je součástí kategorie <a href="/hokej/">hokej</a>.</p>'
          '<h2>Oblečení a čepice se značkou</h2>'
          '<p>Menší část nabídky tvoří běžné oblečení: <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/mikiny/">mikiny</a>, <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/cepice-a-celenky/">čepice a kšiltovky</a>. Hodí se na trénink, do šatny i do běžného dne. Barevně převažuje černá, doplněná červenou, bílou a modrou. U triček dávejte pozor, zda jde o střih unisex nebo dětský, protože stejné číslo velikosti sedí odlišně.</p>'
          '<h2>Péče, životnost a údržba</h2>'
          '<ol><li>Po tréninku brusle utřete a nechte vyschnout mimo pouzdro, vlhkost zkracuje život nožů i bot.</li>'
          '<li>Nože hlídejte ostřením po určitém počtu hodin na ledě, tupé nože zhoršují stabilitu.</li>'
          '<li>Chrániče a rukavice sušte rozložené, ne na topení, a vyvětrejte vnitřek.</li>'
          '<li>Hokejku kontrolujte u spojení násady a čepele, kde vznikají první praskliny.</li>'
          '<li>Prasklou kompozitní hůl nevyměňujte tejpem, lom může při střele selhat.</li></ol>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Největší nabídky se objevují na konci sezóny, tedy na jaře, kdy obchody uvolňují sklad, a v létě před začátkem příprav. Výhodné bývají předchozí ročníky, které se od nových liší spíš označením než funkcí. Naopak před zahájením soutěží a o Vánocích poptávka roste a slevy bývají nižší. Porovnejte alespoň tři obchody včetně poštovného, zkontrolujte velikost a variantu hole (levá, pravá) a sledujte, zda je zboží skladem, protože u těchto kombinací se nabídka rychle mění.</p>',
    faq=[
        ('Jaké zboží Bauer v katalogu převažuje?', 'Převažují hokejky a hokejové brusle, následují chrániče, brankářská výstroj a florbal. Menší část tvoří oblečení a čepice.'),
        ('Pro koho je zboží Bauer určené?', 'Většina nabídky míří na děti a mládež, dospělé modely tvoří menší část. Vždy proto zkontrolujte označení SR, INT, JR nebo YTH.'),
        ('Co znamená zkratka SR u hokejových bruslí?', 'SR je Senior, tedy velikost určená dospělým. Mládež se označuje JR, mezistupeň INT a nejmladší hráči YTH.'),
        ('Jakou velikost brusle vybrat?', 'Změřte délku chodidla a porovnejte ji s tabulkou výrobce. Brusle bývají o jedno až dvě čísla menší než běžná obuv a patu musí držet pevně.'),
        ('Kdy se hodí nastavitelné brusle?', 'U nejmenších dětí, které teprve zkouší led. Dají se prodloužit o několik velikostí, takže vydrží déle než pevná bota.'),
        ('Jak dlouhá má být hokejka?', 'Při stoji na bruslích by měla sahat zhruba mezi nos a bradu. Pro děti je lepší o něco kratší než delší.'),
        ('Mohu brankářské brusle používat v poli?', 'Nedoporučuje se. Mají jiný nůž a konstrukci pro boční pohyb, zatímco hráči v poli potřebují rychlé odrazy.'),
        ('Jak poznám správnou velikost chráničů?', 'Chránič musí sedět pevně na místě kloubu a nesmí se při pohybu posouvat. Příliš velký kus se při pádu odsune a odhalí tělo.'),
        ('Kdy bývají hokejové věci nejlevnější?', 'Obvykle na konci sezóny a v létě, kdy obchody vyprodávají starší ročníky. Před soutěžemi a o Vánocích slevy mizí.'),
        ('Jak se starat o brusle po tréninku?', 'Utřete nože, vyjměte brusle z pouzdra a nechte je vyschnout. Mokré brusle v tašce rychle rezaví a zapáchají.'),
    ],
)

# ------------------------------------------------------------------ peak-mountain
NEW['peak-mountain'] = dict(
    title='Peak Mountain: lyžařské a softshellové bundy a soupravy',
    desc='Peak Mountain v katalogu Sporteky: bundy, kalhoty a soupravy pro děti, ženy i muže. Jak vybrat lyžařské oblečení, softshell a fleece a porovnat obchody.',
    intro='<p>Peak Mountain je v katalogu Sporteky značka horského a zimního oblečení, která se vyplatí hledat především kvůli dětským a dámským kouskům. Výrazně největší skupinou jsou <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, za nimi jdou <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, <a href="/kabaty-a-parky/">kabáty a parky</a>, <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/soupravy/">soupravy a komplety</a>. Menší zastoupení mají <a href="/lyzarske-bundy/">lyžařské bundy</a>, rukavice, mikiny a fleece.</p>'
          '<p>V nabídce se rozdělují dámské, dětské a pánské kusy téměř vyrovnaně, unisex je výjimkou. Mezi barvami vedou černá, modrá a zelená, ale často se objevuje také růžová, oranžová a červená. Průvodce níže vysvětluje, jak vybrat vrstvy podle počasí, co znamená softshell proti lyžařské bundě, jak řešit velikost u rostoucího dítěte a jak porovnat nabídky obchodů, aby se zimní oblečení nekupovalo v sezónní špičce.</p>',
    guide='<h2>Z čeho se nabídka značky skládá</h2>'
          '<p>Skladba kategorií napovídá, že Peak Mountain je hlavně značka pro svrchní vrstvy. Základ tvoří bundy, doplňují je kalhoty a soupravy, zatímco tenké spodní vrstvy a doplňky hrají vedlejší roli. Díky tomu je snadné poskládat komplet na zimní víkend, ale na dlouhé túry v létě tu pestrý výběr nenajdete.</p>'
          + T(['Kategorie', 'Typické kusy podle názvů', 'Kdy je dává smysl hledat'], [
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'softshellové a větrovkové bundy, bundy s kapucí a kožešinou', 'přechodná období, chladné dny ve městě i na procházku'],
              ['<a href="/lyzarske-bundy/">Lyžařské bundy</a>', 'dětské a dívčí lyžařské bundy', 'sjezdovka, sáňkování, zimní hry venku'],
              ['<a href="/lyzarske-kalhoty/">Lyžařské kalhoty</a>', 'dětské a dámské kalhoty, často v kompletu s bundou', 'lyžařský týden, školy v přírodě'],
              ['<a href="/kabaty-a-parky/">Kabáty a parky</a>', 'delší zimní svrchníky', 'každodenní zimní nošení'],
              ['<a href="/soupravy/">Soupravy a komplety</a>', 'souprava bundy a kalhot pro dívky a chlapce', 'dítě, které potřebuje jednotný zimní set'],
              ['<a href="/fleecove-mikiny/">Fleecové mikiny</a>', 'fleece bundy a polopuly', 'střední vrstva pod bundu'],
              ['<a href="/sportovni-rukavice/">Rukavice</a>', 'lyžařské rukavice a palčáky', 'doplněk k zimnímu kompletu']]) +
          '<p>Nabídka je ve velké míře dětská, proto se hodí rodičům, kteří hledají praktické kusy s pevným střihem a výraznými barvami. Pro dámy platí něco podobného a pánská část je menší, ale kompletní. Pokud chcete znát nabídku jinou, podívejte se na stránku <a href="/jarni-a-podzimni-bundy-damske/">jarní a podzimní bundy dámské</a>.</p>'
          '<h2>Softshell, lyžařská bunda a parka: v čem se liší</h2>'
          '<p>Slova v názvu často klamou, takže je dobré znát základní rozdíl mezi typy bund. Mezi produkty Peak Mountain se objevují všechny tři, a každá má jiný účel.</p>'
          + T(['Typ bundy', 'K čemu slouží', 'Čeho si všímat'], [
              ['Softshell', 'větrná a lehce vodoodolná vrstva pro pohyb v chladu', 'prodyšnost, pružnost materiálu, zda má vnitřní fleece'],
              ['Lyžařská bunda', 'zateplená bunda s kapucí, sněhovou sukní a kapsou na skipas', 'vodní sloupec a prodyšnost, zip s chlopní, nastavitelné manžety'],
              ['Parka', 'delší, hřejivá bunda na městské zimní dny', 'délka vzadu, kapuce, zateplení, kožešina'],
              ['Fleece', 'střední izolační vrstva bez ochrany před větrem', 'hustota, zda je potřeba pod větrovku']]) +
          '<p>Softshell hřeje díky přilehlé fleecové vložce a dobře se pohybuje, ale v dešti nebo hlubokém sněhu navlhne. Lyžařská bunda je naopak určena do mokra a mrazu, proto má utěsněné švy a delší střih. Kdo hledá jedno univerzální oblečení pro školu, procházky i lyže, může přemýšlet o souboru, který kombinuje lyžařskou bundu a kalhoty. Pro dospělé vybírejte podle teploty: při pohybu v mrazu se člověk zahřeje, a tak může být výhodnější lehčí bunda s vrstvou fleece než těžká bunda s hustou výplní.</p>'
          '<h2>Vrstvení: jak se obléct do zimy a na jaro</h2>'
          '<p>Správné oblečení nespočívá v jedné silné bundě, ale ve vrstvách. Spodní vrstva odvádí pot, střední zahřívá a vnější chrání před větrem a mokrem. Vrstvy můžete kombinovat podle toho, kolik se pohybujete.</p>'
          '<ul><li><strong>Spodní vrstva:</strong> funkční nebo merino triko, které se nedrží na kůži mokré. Bavlna nasákne potem a po zastavení studí.</li>'
          '<li><strong>Střední vrstva:</strong> fleecová mikina nebo tenká zateplená vesta. V nabídce jsou <a href="/fleecove-mikiny/">fleecové mikiny</a> i běžné <a href="/mikiny/">mikiny</a>.</li>'
          '<li><strong>Vnější vrstva:</strong> softshell na suché dny, lyžařská bunda na mokro a mráz.</li>'
          '<li><strong>Kalhoty:</strong> lyžařské do sněhu, softshellové na turistiku, lehké sportovní na jaro.</li>'
          '<li><strong>Doplňky:</strong> rukavice, čepice a nákrčník pomáhají víc než silnější bunda.</li></ul>'
          '<p>Další inspiraci hledejte v kategorii <a href="/lyzarske-obleceni/">lyžařské oblečení</a>, která shrnuje všechny vrstvy pro zimní sporty, a v přehledu <a href="/termopradlo/">termoprádlo</a> pro spodní vrstvu.</p>'
          '<h2>Dětské oblečení: velikosti a růst</h2>'
          '<p>Více než polovina nabídky je určena dětem a mládeži. Dětské velikosti se u zimního oblečení obvykle uvádějí ve výšce postavy, nikoli v letech, takže si změřte dítě bez bot a porovnejte údaj s tabulkou konkrétního produktu. Pro rostoucí dítě je lepší zvolit mírně volnější střih, aby se pod bundu vešla mikina, ale ne tak velký, aby překážel při pohybu na lyžích nebo sáňkách.</p>'
          '<ol><li>Změřte výšku dítěte a obvod hrudníku a porovnejte s tabulkou prodejce.</li>'
          '<li>U bundy zkontrolujte délku rukávů v předklonu, nesmí odhalit zápěstí.</li>'
          '<li>U kalhot s laclem nebo šlemi se ujistěte, že délka zad vydrží alespoň sezónu.</li>'
          '<li>Rukavice vybírejte raději o trochu větší, ale se zpevněním na zápěstí.</li>'
          '<li>Zvažte komplet ze stejné řady, aby se barvy i funkce doplňovaly.</li></ol>'
          '<p>Při koupi souprav a kompletů pro dívky i chlapce vyplatí se porovnat obchody, protože stejný set se nabízí s různým poštovným. Pokud lyžujete jen příležitostně, zvažte i nákup o velikost větší s úpravou nohavic nebo rukávů, což prodlouží životnost o další sezónu.</p>'
          '<h2>Dámské a pánské oblečení</h2>'
          '<p>Dámské kusy bývají přiléhavější v pase a delší v zádech, pánské mají rovnější střih a širší ramena. Pokud mezi velikostmi váháte, zvažte, zda pod bundou budete nosit silnější mikinu, a vyberte tu větší. Dámská nabídka Peak Mountain je velmi barevná: kromě černé a modré najdete zelené, růžové a oranžové kousky. Pro dospělé kalhoty je dobré zkontrolovat obvod pasu a délku nohavice, protože se liší podle střihu. Pokud potřebujete kalhoty na pohyb v přírodě, prozkoumejte <a href="/damske-sportovni-kalhoty/">dámské sportovní kalhoty</a>, zatímco sporty v kratším rukávu nabídne kategorie <a href="/sportovni-podprsenky/">sportovní podprsenky</a> a <a href="/sportovni-kratasy/">kraťasy</a>.</p>'
          '<h2>Jak číst technické údaje u bundy</h2>'
          '<p>Prodejci často uvádějí vodní sloupec a prodyšnost. Vyšší vodní sloupec znamená lepší ochranu před vodou, ale zpravidla i nižší prodyšnost. Pro děti, které hodně lyžují, je rozumný kompromis střední hodnota, protože se dítě při pohybu zahřívá. U lyžařských bund také sledujte detaily: sněhovou sukni, která brání vniknutí sněhu, zipy s chlopní, kapuci pro helmu a kapsy na ruce i na skipas. Nepromokavost totiž nemá jen materiál, ale i zpracování švů. Pokud nejste ochotni investovat, vyberte bundu s dostatečným zateplením a nepromokavostí doplňte vrstvou pláštěnky při dešti.</p>'
          '<h2>Jaro, podzim a léto: nejen zimní kusy</h2>'
          '<p>Přestože se značka spojuje se sněhem, největší skupinou jsou bundy do přechodných období. Lehký softshell nebo větrovka se hodí na kolo, na školní výlet i do města, kdy je ráno chladno a odpoledne teplo. Takovou bundu snadno sbalíte do batohu, a proto je dobré dávat pozor na hmotnost a kapuci, která se dá stáhnout nebo odepnout. Pro teplejší dny jsou tu <a href="/sportovni-kratasy/">sportovní kraťasy</a>, tenké ponožky a děti ocení tričko s dlouhým rukávem. Podle názvů produktů se objevují i kusy pro vodáky, například v kategorii <a href="/kajaky-a-cluny/">kajaky a čluny</a>, ale jde o okrajovou část sortimentu.</p>'
          '<h2>Jak vybrat mezi stejně vypadajícími kusy</h2>'
          '<p>Pojmenování modelů je v nabídce různorodé a dívčí, chlapecké i dámské varianty se často liší jen barvou nebo jménem. Neřiďte se proto jménem, ale několika praktickými body. Zjistěte, zda je bunda zateplená, nebo jen s tenkou podšívkou. Podívejte se, zda má kapuci pevnou, nebo odnímatelnou, zda je uvnitř fleece a jak vypadá zip. Porovnejte délku bundy a nohavic s dosavadním oblečením a použijte tabulku konkrétního prodejce, protože velikosti se mohou lišit mezi obchody. A nakonec sledujte, jestli je u produktu uvedena barva, kterou opravdu chcete, protože tatáž řada bývá k dispozici v několika odstínech.</p>'
          '<h2>Péče, praní a životnost</h2>'
          '<p>Zimní oblečení vydrží déle, pokud se pere podle štítku, obvykle při nižší teplotě a bez aviváže, která zalepuje póry membrány. Zapněte zipy a suchý zip, aby se nepoškodily. Bundu sušte při pokojové teplotě, ne přímo na topení. Na konci sezóny oblečení vyperte a uložte volně v suchu, ne stlačené v tašce. Pokud po několika sezónách přestane materiál odpuzovat vodu, můžete obnovit impregnaci speciálním sprejem nebo přísadou do pračky.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Zimní oblečení bývá nejdražší v listopadu a prosinci, kdy je poptávka největší. Slevy se obvykle objeví na přelomu ledna a února, často však s omezeným výběrem velikostí. Jarní softshelly a kalhoty jsou naopak výhodnější koncem léta, kdy obchody uvolňují sklady. Sledujte více obchodů, porovnávejte včetně dopravy a zkoušejte, zda stejná bunda není v jiné barvě levnější. Starší barevné varianty bývají stejně kvalitní jako nejnovější.</p>',
    faq=[
        ('Jaké oblečení Peak Mountain v katalogu převažuje?', 'Převažují jarní a podzimní bundy, následují sportovní kalhoty, kabáty, kraťasy a soupravy. Lyžařské oblečení tvoří menší část.'),
        ('Je Peak Mountain spíš pro děti, nebo pro dospělé?', 'Zastoupeny jsou obě skupiny. Dětské i dámské kusy tvoří největší díl nabídky, pánské jsou o něco méně časté.'),
        ('Čím se softshell liší od lyžařské bundy?', 'Softshell chrání před větrem a lehkým deštěm a dobře dýchá. Lyžařská bunda je zateplená a utěsněná pro sníh a mráz.'),
        ('Jak vybrat velikost dětské lyžařské bundy?', 'Změřte výšku dítěte a porovnejte ji s tabulkou. Rukávy by v předklonu neměly odkrýt zápěstí a pod bundu se má vejít mikina.'),
        ('Hodí se souprava bundy a kalhot pro lyžování?', 'Ano, kus ze stejné řady se barevně i funkčně doplňuje. Pro děti je to praktické a často levnější než nákup dvou samostatných kusů.'),
        ('Jak vrstvit oblečení v zimě?', 'Spodní vrstva odvádí pot, střední zahřívá a vnější chrání před větrem a mokrem. Bavlnu na kůži raději vynechte.'),
        ('Jak prát zimní bundu?', 'Podle štítku, při nižší teplotě a bez aviváže. Zapněte zipy a sušte při pokojové teplotě, ne na topení.'),
        ('Co znamená vodní sloupec?', 'Udává odolnost látky proti vodě. Vyšší hodnota chrání víc, ale často snižuje prodyšnost, proto je dobré hledat rozumný kompromis.'),
        ('Kdy bývají zimní bundy nejlevnější?', 'Slevy se obvykle objevují koncem zimy, na přelomu ledna a února. V listopadu a prosinci ceny většinou neklesají.'),
        ('Najdu i kraťasy a rukavice?', 'Ano, v menším rozsahu. Jsou tu kraťasy, lyžařské rukavice, sportovní podprsenky, ponožky a fleecové mikiny.'),
    ],
)

# ------------------------------------------------------------------ helly-hansen
NEW['helly-hansen'] = dict(
    title='Helly Hansen: bundy, lyžařské oblečení, fleece a obuv',
    desc='Helly Hansen v katalogu Sporteky: bundy do deště, lyžařské oblečení, fleece, merino a obuv. Jak vybrat vrstvy a velikost a kdy hledat slevy.',
    intro='<p>Helly Hansen je v katalogu Sporteky široká outdoorová a lyžařská značka. Největší skupinu tvoří <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, těsně za nimi jsou <a href="/tenisky/">tenisky a volnočasové boty</a>, <a href="/fleecove-mikiny/">fleecové mikiny</a> a <a href="/lyzarske-bundy/">lyžařské bundy</a>. K tomu přibývají <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/mikiny/">mikiny</a>, <a href="/merino-tricka/">merino trička</a>, <a href="/polokosile/">polokošile</a> a <a href="/zimni-bundy/">zimní bundy</a>.</p>'
          '<p>Více než polovinu zboží tvoří pánská řada, dámská je druhá a dětská tvoří menší část. Z barev vede černá a modrá, následuje bílá a zelená. Stránka dále ukazuje, jak z názvů poznat účel bundy, jak spojit vrstvy pro zimu a déšť, jak řešit velikosti a jak porovnat obchody a sezónní slevy. Pomáhá tak vybrat mezi bundou do deště, zimní parkou a lyžařským komplet oblečením a vyhnout se zbytečně tlustému nebo naopak tenkému kusu.</p>',
    guide='<h2>Co v nabídce Helly Hansen převažuje</h2>'
          '<p>Z kategorií je vidět, že značka pokrývá téměř celý rok. V létě a na jaře jsou to bundy do deště a polokošile, na podzim fleece a mikiny, v zimě lyžařské a péřové bundy. Zvláštností je i obuv, která v katalogu zabírá více než deset procent nabídky.</p>'
          + T(['Kategorie', 'Co podle názvů najdete', 'Kdy dává smysl'], [
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehčí zateplené bundy a větrovky', 'přechodná období a každodenní nošení'],
              ['<a href="/nepromokave-bundy/">Nepromokavé bundy</a>', 'bundy do deště pro muže a ženy', 'chladný déšť, výlet, město'],
              ['<a href="/lyzarske-bundy/">Lyžařské bundy</a> a <a href="/lyzarske-kalhoty/">kalhoty</a>', 'sjezdové a snowboardové oblečení včetně dětských overalů', 'sezóna na sjezdovce'],
              ['<a href="/zimni-bundy/">Zimní a péřové bundy</a>', 'zateplené bundy na mráz', 'zima ve městě i v přírodě'],
              ['<a href="/fleecove-mikiny/">Fleecové mikiny</a>', 'fleece mikiny a bundy', 'střední vrstva'],
              ['<a href="/merino-tricka/">Merino trička</a>', 'spodní vrstva z jemné vlny', 'chladno, delší aktivity'],
              ['<a href="/tenisky/">Tenisky a boty</a>', 'tenisky, zimní boty, treková obuv, dětské boty', 'město, výlet, zimní procházky'],
              ['<a href="/cepice-a-celenky/">Čepice a čelenky</a>', 'zimní čepice a čelenky', 'doplněk k bundě']]) +
          '<p>Kromě toho se v nabídce objevují batohy a trička s potiskem. Pro rychlé shrnutí zaměřené na jednu kategorii použijte stránku <a href="/helly-hansen-lyzarska-bunda/">Helly Hansen lyžařská bunda</a>. Nabídka je poměrně široká a názvy nejsou standardizované, proto si vždy přečtěte popis a údaje o zateplení.</p>'
          '<h2>Jak vybrat správný typ bundy</h2>'
          '<p>Značka nabízí bundy, které na první pohled vypadají podobně, ale slouží různým účelům. Pomůže mít jasno v tom, jak se používají.</p>'
          + T(['Typ', 'Pro co je navržen', 'Na co si dát pozor'], [
              ['Bunda do deště', 'ochrana před deštěm a větrem, nejlépe lehká a sbalitelná', 'utěsněné švy, kapuce, prodyšnost'],
              ['Zateplená přechodová bunda', 'chladné dny bez deště', 'síla zateplení, délka, střih'],
              ['Lyžařská bunda', 'sníh, vítr a pohyb na svahu', 'sněhová sukně, kapsa na skipas, kapuce na helmu'],
              ['Péřová nebo zimní bunda', 'mráz a stání venku', 'zateplení, délka, odolnost proti vlhku'],
              ['Fleece', 'střední vrstva a oblečení na chlad bez větru', 'hustota, přilnavost, zip až ke krku']]) +
          '<p>Pokud chcete jednu bundu na celý rok, je rozumné pořídit nepromokavou skořepinu, pod kterou se v zimě oblékne fleece a termoprádlo. V létě pak stačí samotná skořepina. Zateplená bunda funguje tam, kde nechcete skládat vrstvy a jde vám o jednoduchost, ale v dešti může být těžká a pomalu schne. Při sjezdovém lyžování je lepší vybrat speciální lyžařský kus, který zvládne sníh, vítr i sezení na lanovce. Dalším tipem je kategorie <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>'
          '<h2>Lyžování a snowboarding</h2>'
          '<p>Lyžařský komplet tvoří bunda, kalhoty a vrstvy pod nimi. V nabídce jsou kusy pro dospělé i děti, včetně zimních overalů pro nejmenší. Na svahu rozhoduje kombinace ochrany před mokrem a prodyšnosti, protože při jízdě se hodně potíte a při stání na lanovce rychle ochladnete. Pomáhají větrací zipy na bocích nebo pod paží, které umožní regulovat teplotu bez svlékání. Kalhoty mají mít zpevněný spodní okraj, aby nasákl co nejméně vody a nepoškodil se od hran lyží. Podrobněji pomůže stránka <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a> a <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a>, a pro doplnění i <a href="/lyzarske-rukavice/">lyžařské rukavice</a>.</p>'
          '<ul><li><strong>Střih:</strong> lyžaři vyžadují volnější, snowboardisté ještě volnější a delší střih, který kryje při pádech zadek.</li>'
          '<li><strong>Zateplení:</strong> čím aktivnější jste, tím méně zateplení potřebujete. Chladnější lidé a děti oceňují víc.</li>'
          '<li><strong>Kapuce:</strong> musí jít nasadit přes helmu, nikoli pod ni.</li>'
          '<li><strong>Zip a manžety:</strong> chlopeň přes zip a stahovací manžety brání pronikání sněhu.</li>'
          '<li><strong>Vnitřní kapsy:</strong> na telefon, aby se v mrazu nevybíjel.</li></ul>'
          '<h2>Spodní a střední vrstvy: merino a fleece</h2>'
          '<p>Merino trička z katalogu slouží jako spodní vrstva, která zadržuje teplo i při zvlhnutí a pomaleji absorbuje pach. Hodí se k aktivitám v chladném počasí a mnoho lidí je nosí i při cestování, protože se nemusí prát po každém použití. Fleecové mikiny a bundy tvoří střední vrstvu. Jejich síla se pozná podle hustoty a hmotnosti, zatímco tenký fleece slouží i jako samostatná horní vrstva v mírném počasí. Samotný fleece ale vítr propouští, proto jej doplňte větrovkou nebo bundou.</p>'
          '<p>Hledáte-li něco pod bundu, nabízí se i prodlouženější skupina <a href="/termopradlo/">termoprádlo</a>. Pro volnější použití jsou k dispozici <a href="/mikiny/">mikiny</a>, <a href="/polokosile/">polokošile</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, které se hodí do přírody i do města.</p>'
          '<h2>Obuv: tenisky, zimní a treková</h2>'
          '<p>Obuv je v nabídce výrazná. Najdete tu volnočasové tenisky, kožené a zimní boty, trekovou obuv i dětské modely. Při výběru začněte účelem: tenisky do města nemusí mít membránu ani agresivní podrážku, zimní boty potřebují pevnější a protiskluzovou podešev a vnitřní zateplení, treková obuv musí podržet kotník na nerovném terénu. Velikost ověřte u konkrétního výrobce a před nákupem změřte nohu odpoledne, kdy je největší. Zimní boty vybírejte s malou rezervou kvůli silnější ponožce, ale ne větší, aby noha neklouzala. Další možnosti poskytují <a href="/zimni-obuv/">zimní obuv</a> a <a href="/trekova-obuv/">trekové boty</a>.</p>'
          '<h2>Batohy, čepice a drobnosti</h2>'
          '<p>Mimo oblečení a obuv najdete v katalogu také sportovní batohy a čepice. Čepice a čelenky se hodí k zimnímu kompletu a váží málo, takže je snadné je mít v kapse. U batohů vždy zkontrolujte objem a zda má vyztužená záda a popruhy, které se dají upravit. Menší batoh pomůže při denním výletě, zatímco na delší cestu potřebujete nosný systém s bederním pásem. Rukavice a nákrčníky kupujte spolu s bundou, protože barvy a zateplení se pak ladí. Další výběr nabízí kategorie <a href="/batohy/">batohy</a> a <a href="/cepice-a-celenky/">čepice, kšiltovky a čelenky</a>.</p>'
          '<h2>Pro koho a na co: tři příklady složení</h2>'
          '<p>Městský dojíždějící: nepromokavá bunda, fleecová mikina a tenisky nebo kožené boty. Taková sestava zvládne chladné ráno i déšť a nevypadá příliš sportovně. Rodina na sjezdovce: dětský zimní overal nebo bunda s kalhotami, termoprádlo a rukavice, pro dospělé lyžařský komplet s větracími zipy. Víkendový výletník: merino triko, fleece, lehká skořepina a pohodlná obuv, doplněné čepicí a malým batohem. Sestavy se dají snadno upravit podle ročního období a to, co z nich pořídíte jako první, určuje počasí, ve kterém trávíte nejvíc času.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Oblečení se prodává ve standardních velikostech od XS po XXL a pánské kusy bývají většinou volnější v těle než dámské. Při koupi přes internet ověřte údaje o délce a šířce a porovnejte je s kusem, který vám sedí. Pokud jste mezi dvěma velikostmi, volte větší u zimních bund, aby se pod ně vešly vrstvy, a menší u fleece nebo merino, které mají přiléhat. V dětské části se využívá výška postavy a bývá vhodné počítat s růstem o jednu velikost. Při vrácení zboží si vyžádejte jasné podmínky, aby zkušební oblékání nebylo omezeno.</p>'
          '<h2>Péče a životnost</h2>'
          '<ol><li>Vodoodpudivé bundy perte podle štítku a bez aviváže, která zalepuje póry.</li>'
          '<li>Po několika sezónách obnovte impregnaci speciálním sprejem nebo přísadou do pračky.</li>'
          '<li>Merino perte šetrně a sušte položené naplocho, aby se nevytáhlo.</li>'
          '<li>Fleece nežehlete a nesušte na topení, materiál se může zdeformovat.</li>'
          '<li>Obuv po použití vysušte při pokojové teplotě a zbavte špíny.</li></ol>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Lyžařské oblečení a zimní bundy bývají levnější od ledna do března, kdy se sezóna chýlí ke konci. Bundy do deště a jarní kusy lze výhodně nakoupit na přelomu léta a podzimu. Opačně se vyplatí nespěchat u novinek, které jsou zpočátku nejdražší. Při porovnávání berte v úvahu i poštovné, dostupnost vaší velikosti a barvu, protože tatáž bunda může mít v jiném odstínu jinou cenu. Starší ročník bývá po funkční stránce velmi podobný nejnovějšímu.</p>',
    faq=[
        ('Co v nabídce Helly Hansen převažuje?', 'Největší skupinou jsou jarní a podzimní bundy. Následují tenisky a volnočasové boty, fleecové mikiny, lyžařské bundy a kalhoty.'),
        ('Pro koho je zboží Helly Hansen určeno?', 'Nejvíce je pánských kusů, dámská řada je druhá největší a dětská tvoří menší část včetně zimních overalů a bot.'),
        ('Jakou bundu vybrat na déšť?', 'Zvolte nepromokavou bundu s utěsněnými švy, stažitelnou kapucí a dostatečnou prodyšností. Sbalitelný kus se vejde do batohu.'),
        ('Stačí jedna bunda na celý rok?', 'Nepromokavá skořepina funguje celoročně, pokud pod ni v zimě přidáte fleece a termoprádlo. Pro lyžování je ale lepší speciální lyžařská bunda.'),
        ('K čemu je merino triko?', 'Jako spodní vrstva zahřívá i při zvlhnutí a pomaleji absorbuje pach. Hodí se při pohybu v chladu a na cesty.'),
        ('Čím se fleece liší od zimní bundy?', 'Fleece zahřívá, ale vítr propouští. Zimní bunda chrání před větrem a zimou, proto se kombinuje fleece jako střední vrstva pod bundou.'),
        ('Jak vybrat velikost zimní bundy?', 'Volte raději větší, aby se pod ni vešel fleece nebo mikina. Zkontrolujte délku rukávů a zad v tabulce prodejce.'),
        ('Jak obnovit nepromokavost bundy?', 'Bundu vyperte bez aviváže a použijte impregnaci ve spreji nebo přísadu do pračky. Poté ji sušte při doporučené teplotě.'),
        ('Nabízí značka i boty?', 'Ano. Najdete tenisky, kožené a zimní boty, trekovou obuv i dětské modely. Velikost ověřte u konkrétního modelu.'),
        ('Kdy bývají bundy Helly Hansen nejlevnější?', 'Zimní kusy se obvykle zlevňují od ledna do března, bundy do deště a přechodové kusy koncem léta. Novinky bývají nejdražší.'),
    ],
)

# ------------------------------------------------------------------ palladium
NEW['palladium'] = dict(
    title='Palladium: kotníkové tenisky, boty Pampa a outdoorová obuv',
    desc='Palladium v katalogu Sporteky: kotníkové tenisky, Pampa, Palla Ace, trekové boty a holínky. Jak vybrat model a velikost a kdy hledat slevy.',
    intro='<p>Palladium je v katalogu Sporteky téměř výhradně obuvnická značka. Drtivou většinu zboží tvoří <a href="/tenisky/">tenisky a volnočasové boty</a>, zbytek je rozdělený mezi <a href="/tenisova-obuv/">tenisovou obuv</a>, <a href="/sandaly/">sportovní sandály</a>, <a href="/trekova-obuv/">trekové boty</a>, <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> a <a href="/holinky/">holínky</a>. Ve výpisu se opakují řady Pampa, Palla Ace, Dunelite a Baggy v nízkém i kotníkovém provedení.</p>'
          '<p>Většina nabídky je dámská, pánská tvoří menší část a dětské boty jsou spíše výjimkou. Barvy jsou přírodní: černá, béžová, hnědá, bílá a šedá, doplněné zelenou. Další text popisuje, jak se jednotlivé řady liší, jak vybrat mezi plátěnou a nepromokavou verzí, jak řešit velikost a péči a kdy se vyplatí porovnat obchody. Pomůže vám rozhodnout, zda je to bota do města, nebo spíš lehčí obuv do počasí a po lese.</p>',
    guide='<h2>Co z nabídky Palladium vyčnívá</h2>'
          '<p>Pro značku je typická silná podešev a vyšší kotníkový střih, který připomíná lehkou pracovní nebo armádní botu a zároveň vypadá městsky. V katalogu se taková obuv objevuje v několika provedeních, od plátěných až po voděodolná.</p>'
          + T(['Skupina', 'Co zahrnuje podle názvů', 'Komu se hodí'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'řady Pampa, Palla Ace, Dunelite a Baggy', 'město, škola, cesty, volný čas'],
              ['<a href="/tenisova-obuv/">Tenisová obuv</a>', 'nízká obuv pro sportovnější použití', 'ti, kdo chtějí lehčí botu'],
              ['<a href="/trekova-obuv/">Treková obuv</a> a <a href="/vysoke-trekove-boty/">vysoké boty</a>', 'kotníkové a vyšší boty s označením WP', 'procházky v mokru, nenáročné stezky'],
              ['<a href="/holinky/">Holínky</a>', 'obuv do mokra a bláta', 'zahrada, déšť, hřiště'],
              ['<a href="/sandaly/">Sportovní sandály</a>', 'otevřená letní obuv', 'léto, voda, cesty'],
              ['<a href="/merino-tricka/">Merino trička</a> a <a href="/cepice-a-celenky/">čepice</a>', 'okrajová část sortimentu', 'doplňky k obuvi']]) +
          '<p>Ostatní kategorie jsou jen doplňkem. Pokud vás zajímají podobné boty od jiných značek, projděte kategorie <a href="/sportovni-obuv/">sportovní obuv</a> nebo <a href="/zimni-obuv/">zimní obuv</a>, případně značky <a href="/znacka/timberland/">Timberland</a> a <a href="/znacka/merrell/">Merrell</a>, které se zaměřují na venkovní boty.</p>'
          '<h2>Řady a modely: jak se v nich zorientovat</h2>'
          '<p>Názvy v katalogu se opakují v různých materiálech a barvách. Celé označení se skládá z řady a doplňku, který říká, jaká bota to je. Označení vždy ověřte v popisu produktu, protože prodejci je zapisují různě.</p>'
          + T(['Označení', 'Co obvykle znamená', 'Na co dát pozor'], [
              ['Pampa Hi', 'kotníková bota s vyšší nártem a šněrováním', 'sedí pevněji, ale potřebuje rozšlapat'],
              ['Pampa Cuff nebo Zip', 'varianta s manžetou nebo zipem', 'zip usnadňuje obouvání, ale hůř těsní'],
              ['WP nebo WP+', 'vodovzdorné provedení', 'v dešti ochrání, ale v teple méně dýchá'],
              ['Palla Ace', 'nižší nebo chukka střih', 'městská bota bez vysoké šněrovací části'],
              ['Dunelite OX', 'nízká sportovnější bota', 'lehčí a vhodná i na delší chůzi po městě'],
              ['Troppercuff, Troopetlit', 'robustnější kotníkové boty', 'těžší, hodí se do náročnějšího počasí']]) +
          '<p>Plátěný svršek je lehký, prodyšný a v létě příjemný, ale snáší vodu hůře. Kožené a voděodolné kusy odolávají lépe, jsou však těžší a méně prodyšné. Pokud chodíte po městě v mírném počasí, plátěná Pampa stačí, pro podzimní procházky lesem bývá lepší verze s membránou. V obchodech najdete i barevné nebo zdobené varianty, které se hodí jako módní doplněk.</p>'
          '<h2>Dámské, pánské a dětské boty</h2>'
          '<p>Dámské velikosti tvoří většinu nabídky, a proto se na této stránce vyplatí hledat dámské kotníkové tenisky, nižší boty chukka i zimnější provedení. Pánská nabídka je užší, ale zahrnuje nízké sportovní i vysoké modely. Dětské boty se objevují jen ojediněle, spíše v řadě Pampa. Stejné číslo velikosti může v unisex modelu sedět jinak, takže vždy sledujte, jestli výrobce uvádí velikost podle EU, UK nebo cm. Podobné pohlaví řazené přehledy najdete v kategoriích <a href="/damska-sportovni-obuv/">dámská sportovní obuv</a> a <a href="/panska-sportovni-obuv/">pánská sportovní obuv</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<ol><li>Změřte chodidlo večer, kdy je největší, a přidejte rezervu přibližně jednoho centimetru před špičkou.</li>'
          '<li>Porovnejte délku s tabulkou výrobce nebo prodejce a ověřte, zda je uvedena v centimetrech.</li>'
          '<li>Kotníkové boty zkoušejte s ponožkou, kterou budete nosit, tlustší do zimy, tenkou na léto.</li>'
          '<li>Dívejte se na šířku nártu. Pevná plátěná bota se po několika dnech rozchodí, ale kůže tlačí déle.</li>'
          '<li>Při koupi na dálku si ověřte podmínky vrácení.</li></ol>'
          '<p>Tvar a velikost se mohou lišit podle modelu, takže se nespoléhejte na zkušenost z jiného páru. Pokud jste mezi dvěma čísly, zkuste menší s tenkou ponožkou a větší, pokud chcete nosit teplou.</p>'
          '<h2>Plátěná, kožená nebo nepromokavá: co zvolit</h2>'
          '<ul><li><strong>Plátno:</strong> lehké a levnější na údržbu, vhodné pro léto a suché dny. Špínu snadno setřete, ale prosáknout může.</li>'
          '<li><strong>Kůže a semiš:</strong> působí kvalitněji a lépe drží tvar, ale potřebují impregnaci a opatrnost při mokru.</li>'
          '<li><strong>Voděodolné provedení (WP):</strong> do deště a sněhu. Pamatujte, že není určeno k delšímu brodění.</li>'
          '<li><strong>Podšívka:</strong> teplá podšívka hřeje v zimě, v létě je zbytečná.</li>'
          '<li><strong>Podešev:</strong> hrubý vzorek zlepšuje přilnavost v blátě, hladký se hodí do města.</li></ul>'
          '<h2>Do města, na výlet nebo do lesa</h2>'
          '<p>Městská bota potřebuje pohodlí a tvar, který se hodí ke kalhotám i k šatům. V nabídce je to především řada Pampa a Palla Ace. Pro lehké výlety po cestách ve volné krajině se hodí kotníkové boty s vodovzdorným svrškem. Pro skutečnou turistiku v horách ale vybírejte raději specializovanou <a href="/trekova-obuv/">trekovou obuv</a>, protože pevnější podešev a stabilita kotníku se při nesení batohu liší. Nakonec zvažte holínky na zahradu nebo děti, které rády šlapou v kalužích. Stejně tak boty s nižším střihem patří spíš do suchého počasí.</p>'
          '<h2>Jak nosit kotníkové tenisky</h2>'
          '<p>Kotníková bota je při správné volbě univerzální. K džínám a kalhotám s úzkou nohavicí vypadá nejlépe, když se nohavice jen lehce opře o svršek nebo se vyhrne nad kotník. K šatům a sukním působí kontrastně a zároveň praktičtěji než lodičky. U šněrovacích modelů nechte horní dva otvory volnější, pokud kotník tlačí, a naopak dotáhněte, pokud pata klouže. Šněrování se dá měnit podle činnosti: pevnější při chůzi z kopce, volnější na delším sezení.</p>'
          '<h2>Cestování a každodenní nošení</h2>'
          '<p>Boty z katalogu se často vybírají jako univerzální pár na cesty, protože se dají nosit ve městě i při procházkách mimo něj. Pro dlouhé dny na nohou je důležitá vložka. Standardní vložka bývá tenká, proto lidé s problémy s klenbou zvažují vložení vlastní ortopedické vložky. Při dlouhé chůzi na tvrdém povrchu pomáhá i střídání bot a ponožky z přírodních vláken, které odvádějí vlhkost. Pro letní cestování se hodí plátěná varianta, pro podzim voděodolná, a pokud jedete na chlad, vezměte raději s sebou druhý pár.</p>'
          '<h2>Co dělat, když boty tlačí</h2>'
          '<p>Nové boty z plátna se obvykle rozchodí během několika dní, kůže potřebuje delší dobu. Začněte krátkými vycházkami a doma je noste s tlustší ponožkou, aby se materiál přizpůsobil. Pokud tlačí na jednom místě, pomůže u kůže roztažení speciálním sprejem nebo napínákem u obuvníka. Bolí-li patu, zkontrolujte, zda je bota správně zašněrovaná a zda nejde o příliš velkou velikost. Pokud nic nepomáhá, využijte právo vrátit zboží v zákonné lhůtě. Do té doby je zkoušejte jen doma na čistém povrchu, aby šly vrátit.</p>'
          '<h2>Co hledat u konkrétního produktu</h2>'
          '<ul><li><strong>Popis svršku:</strong> plátno, kůže nebo kombinace určí, jak bota snáší vodu.</li>'
          '<li><strong>Označení WP:</strong> signalizuje vodovzdorný svršek, ale podrobnosti ověřte u prodejce.</li>'
          '<li><strong>Typ zapínání:</strong> šněrování, zip nebo kombinace mění pohodlí při obouvání.</li>'
          '<li><strong>Výška kotníku:</strong> nízká bota je lehká, kotníková drží nohu pevněji.</li>'
          '<li><strong>Dostupné velikosti:</strong> u oblíbených řad se rychle vyprodají střední čísla.</li></ul>'
          '<h2>Sandály, holínky a tenisová obuv</h2>'
          '<p>Menší skupiny mají své přednosti. Sportovní sandály se hodí k vodě a na letní cesty, kde potřebujete obuv, která rychle schne a drží na noze. Holínky patří k deštivým dnům a práci na zahradě, přičemž u dětí je důležitá snadná obouvací část a nepromokavá podešev. Tenisová obuv v katalogu je spíše nižší sportovní bota, kterou lze nosit na kurt, ale i při běžném pohybu. Každou z těchto skupin vybírejte podle účelu a velikost ověřte zvlášť, protože tvar kopyta se liší.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Obuv vydrží déle, pokud ji po mokru vysušíte při pokojové teplotě a vycpete papírem, ne přímo na topení. Plátno čistěte kartáčem a jemným mýdlovým roztokem, kůži a semiš kartáčem a vhodným impregnačním sprejem. Před pračkou raději dejte přednost ručnímu čištění, protože lepidlo a tvar podešve to nemusí vydržet. Šněrovadla se dají prát zvlášť a vyměnit. Střídání dvou párů prodlužuje životnost a umožňuje obuvi vyschnout.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Značková obuv se zlevňuje při změně sezón. Plátěné kusy bývají výhodnější na konci léta, vyšší zimní boty počátkem jara. Hledejte také předchozí barevné varianty, které bývají levnější než aktuální kolekce, a sledujte více obchodů najednou, protože dostupnost velikostí se rychle mění. Nezapomeňte započítat poštovné a možnost výměny velikosti. U módní obuvi se ceny mění podle barvy, takže stojí za to zkusit jiný odstín.</p>',
    faq=[
        ('Co v nabídce Palladium převažuje?', 'Naprostou většinu tvoří tenisky a volnočasové boty, zejména kotníkové modely. Zbytek tvoří treková obuv, sandály, holínky a doplňky.'),
        ('Pro koho je Palladium určeno?', 'Většina nabídky je dámská, pánská část je menší a dětské boty se objevují jen výjimečně.'),
        ('Co znamená označení WP u bot?', 'Obvykle vodovzdorné provedení svršku. Boty snesou déšť a mokrý sníh, ale nejsou určené k brodění ve vodě.'),
        ('Jak velikost bot sedí?', 'Záleží na modelu, proto vždy porovnejte délku chodidla s tabulkou. Zvolte rezervu asi centimetru před špičkou.'),
        ('Hodí se kotníkové boty do zimy?', 'Ano, zejména s voděodolným svrškem nebo podšívkou. Pro mráz a sníh ověřte zateplení a protiskluzovou podešev.'),
        ('Plátěné nebo kožené boty?', 'Plátno je lehčí a vhodné pro léto, kůže drží tvar a lépe odolává chladu. Obě varianty vyžadují péči a impregnaci.'),
        ('Dají se boty prát v pračce?', 'Raději ne. Čistěte je kartáčem a jemným roztokem, aby se nepoškodilo lepení podešve ani tvar.'),
        ('Hodí se tyto boty na turistiku?', 'Na lehké výlety ano. Pro dlouhé túry s batohem je lepší specializovaná treková obuv s tužší podešví.'),
        ('Nabízí značka i holínky a sandály?', 'Ano, v malém množství. Najdete holínky, sportovní sandály, trekové boty a tenisovou obuv.'),
        ('Kdy bývají boty Palladium nejlevnější?', 'Při změně sezón: plátěné modely koncem léta, vyšší boty na jaře. Starší barevné varianty bývají levnější než nové kolekce.'),
    ],
)

