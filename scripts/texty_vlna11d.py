"""sporteka.cz — wave 11d (4. 11. 2026): long texts (>= 1500 words) for cyklo-dily, sportovni-ponozky, vodni-sporty.
General true facts only, no prices; brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklo-dily
NEW['cyklo-dily'] = dict(long=True,
    title='Díly na kolo – pláště, brzdy, pohon, řídítka | Sporteka',
    desc='Náhradní díly na kolo: pláště, brzdy, řetězy, kazety, řídítka, sedla, pedály i vidlice. Porovnejte ceny českých obchodů a vyberte díl, který sedne.',
    intro='<p><strong>Díly na kolo</strong> se nevybírají podle vzhledu, ale podle standardů. Stejně vypadající plášť, brzdový kotouč nebo kazeta se mohou lišit rozměrem, počtem převodů či způsobem uchycení, a pak je nekoupíte do kola, ale do koše. Nejdřív proto zjistěte, co na kole máte, a teprve potom hledejte náhradu nebo upgrade.</p>'
          '<p>Na Sportece najdete tisíce dílů z českých obchodů a každou skupinu máte zvlášť: <a href="/plaste-a-duse/">pláště a duše</a>, <a href="/cyklo-brzdy/">brzdy</a>, <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklo-riditka/">řídítka a sedlovky</a>, <a href="/sedla-a-gripy/">sedla a gripy</a>, <a href="/cyklo-pedaly/">pedály</a>, <a href="/cyklo-blatniky/">blatníky</a>, <a href="/cyklo-kola-a-rafky/">kola a ráfky</a>, <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a> a <a href="/ebike-baterie/">komponenty pro e-kola</a>. Stránka vás provede tím, co se kontroluje u kterého dílu.</p>',
    guide='<h2>Jak na nákup dílů, aby seděly napoprvé</h2>'
          '<p>Nejčastější příčinou špatného nákupu je výběr podle vzhledu místo rozměrů: kupující vycházel z toho, jak kolo vypadá, a ne z toho, jaké má rozměry. Než otevřete obchod, udělejte si zápis. Poznamenejte si průměr kol a šířku pláště, typ brzd, počet rychlostí vzadu, průměr řídítek v místě upnutí a typ osy v zadním kole. Hodí se i fotografie pohonu a brzd zblízka. Většinu údajů najdete vyražených nebo vytištěných přímo na dílech.</p>'
          '<h3>Kontrolní seznam podle skupin</h3>'
          + T(['Skupina', 'Co ověřit před koupí'], [
              ['Pláště a duše', 'průměr ráfku, šířka pláště, typ ventilku, tubeless nebo duše'],
              ['Brzdy', 'kotoučové nebo ráfkové, hydraulické nebo lanové, tvar destiček'],
              ['Kotouče', 'průměr a způsob upnutí na náboj (šest šroubů nebo centrální zámek)'],
              ['Pohon', 'počet rychlostí, kompatibilita přehazovačky, řazení, kazety a řetězu'],
              ['Řídítka a představce', 'průměr upnutí, zvednutí, šířka, délka představce'],
              ['Sedlovka', 'průměr trubky, délka, případně průchod vnitřního vedení'],
              ['Pedály', 'závit osy, plošinové nebo nášlapné, typ nášlapů'],
              ['Vidlice', 'průměr kol, délka zdvihu, osa, průměr krkové trubky']]) +
          '<h3>Pláště a duše</h3>'
          '<p>Rozměr pláště je vyražen na boku v palcích nebo v milimetrech a odpovídá průměru ráfku. Do stejného ráfku se vejdou různě široké pláště, ale ne libovolně. Široký plášť poskytuje větší pohodlí a přilnavost v terénu, úzký se lépe valí po asfaltu. Duše se kupuje podle stejného rozměru a podle ventilku: autoventilek je širší, galusák (francouzský) užší a ráfek musí mít vyvrtaný otvor odpovídající velikosti. Podrobnosti najdete v kategorii <a href="/plaste-a-duse/">pláště a duše</a>.</p>'
          '<p>Z hlediska vzorku platí jednoduché pravidlo. Hladký nebo jemně žíhaný plášť patří na silnici a do města, střední vzorek na gravel a trekingové kolo, hrubé špunty na horské kolo do bláta a kořenů. Směs gumy ovlivňuje přilnavost a životnost, měkčí směs lépe drží, ale rychleji se obrušuje.</p>'
          '<h3>Brzdy a brzdové destičky</h3>'
          '<p>Brzdy patří mezi díly, na nichž se nešetří. Kotoučové brzdy jsou dnes standardem u horských, gravelových i většiny trekingových kol a fungují i za mokra. Ráfkové brzdy najdete hlavně u starších kol a u některých městských modelů. Destičky se liší podle výrobce a modelu brzdy, takže je nelze volně zaměňovat. Rozlišují se také směsi: organické (pryskyřičné) destičky jsou tišší a mají dobrý záběr hned, kovové (sintrované) vydrží déle a hodí se do blátivých a náročných podmínek, ale jsou hlučnější.</p>'
          '<p>Brzdový kotouč se vyměňuje, když je sjetý pod minimální tloušťku vyznačenou na něm, zkroucený nebo opakovaně ztrácí účinnost po znečištění. Výběr najdete v kategorii <a href="/cyklo-brzdy/">brzdy a destičky</a>.</p>'
          '<h3>Pohon: řetěz, kazeta, převodníky, přehazovačka</h3>'
          '<p>Pohon je soustava dílů, které se opotřebovávají společně. Řetěz se prodlužuje, tím obrušuje zuby kazety a převodníků a ty se pak nehodí pro nový řetěz. Proto se vyplatí měnit řetěz včas, ideálně podle měřidla opotřebení. Kazeta, řetěz a řazení musí mít stejný počet rychlostí a stejnou řadu od jednoho výrobce nebo kompatibilní výrobce. Na kole s jedním převodníkem vpředu řešte kapacitu přehazovačky vzhledem k největšímu zubu kazety.</p>'
          '<p>Nejběžnější značky v nabídce jsou Shimano a Sram, podle kterých se orientuje většina kompatibilních dílů. Další součástky najdete v kategorii <a href="/cyklo-pohon/">pohon</a>.</p>'
          '<h3>Řídítka, představce a sedlovky</h3>'
          '<p>Řídítka mají několik rozměrů, které se nesmějí splést: průměr středu, kam se upíná představec, průměr konců pro gripy a řazení, šířku a zvednutí. Představec musí mít stejný průměr upnutí jako řídítka a dosah ovlivňuje, jak daleko od těla máte ruce. Sedlovka se kupuje podle vnitřního průměru sedlové trubky rámu, rozdíl desetiny milimetru už vadí. Najdete je v kategorii <a href="/cyklo-riditka/">řídítka, představce a sedlovky</a>.</p>'
          '<h3>Sedla, gripy a pedály</h3>'
          '<p>Sedlo je osobní věc. Šířka se volí podle vzdálenosti sedacích kostí, nikoli podle toho, jak je sedlo měkké, a příliš měkké sedlo často tlačí víc než pevné. Gripy mohou být gumové, pěnové nebo šroubovací s objímkou, která zabrání protočení. Pedály se dělí na plošinové, na které stačí běžná obuv, a nášlapné, které spojují botu s pedálem. Nášlapy a tretry musí odpovídat systému. Další výběr: <a href="/sedla-a-gripy/">sedla, gripy a potahy</a> a <a href="/cyklo-pedaly/">pedály</a>.</p>'
          '<h3>Kola, ráfky a vidlice</h3>'
          '<p>Zapletené kolo je jeden z dražších dílů a kupuje se podle průměru, šířky ráfku, rozteče nábojů, typu osy a uchycení kotouče nebo brzdové plochy. U vidlic hlídejte zdvih, průměr kol, osu a průměr krkové trubky. Změna zdvihu ovlivňuje geometrii rámu, proto výrazně větší zdvih než určil výrobce nedoporučujeme. Viz <a href="/cyklo-kola-a-rafky/">kola, ráfky a náboje</a> a <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>.</p>'
          '<h3>Blatníky a drobnosti</h3>'
          '<p>Blatníky se kupují podle průměru kol a šířky pláště. Mají mít rezervu kolem pláště, jinak se v nich zasekne bláto a kamínky. K dílům patří i šrouby, kabely, bowdeny, spojky řetězu a jiná drobnost, kterou je dobré mít doma. Najdete je v <a href="/cyklo-blatniky/">blatnících</a> a v <a href="/cyklo-prislusenstvi/">příslušenství</a>.</p>'
          '<h3>Kdy opravit a kdy vyměnit</h3>'
          '<p>Rozhodněte podle bezpečnosti, nikoli podle ceny. Pláště s popraskanými boky, vyhřezlou duší nebo viditelnou kostrou, brzdové destičky bez materiálu a prasklé lanko mají okamžitou výměnu. Řetěz sleduje měřidlo, ložiska se vyměňují, když se náboj nebo středové složení točí drsně. Díly nosné konstrukce, jako jsou řídítka, představec, sedlovka, vidlice nebo kliky, po pádu vždy zkontrolujte. Prasklinu nebo deformaci nezachrání oprava a vyřazený díl nepoužívejte.</p>'
          '<h3>Montáž a nářadí</h3>'
          '<p>Základní práce zvládnete s imbusy, momentovým klíčem, stahovákem kazety, kleštěmi na spojky a sadou montpák. Momentový klíč je důležitý u karbonových dílů a u upnutí řídítek, kde přílišné dotažení praskne materiál. Přehled pomůcek a údržby najdete v kategoriích <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> a <a href="/cyklo-udrzba/">údržba kola</a>. Seřízení brzd a řazení svěřte servisu, pokud to neumíte, protože chyba se projeví právě při náhlé brzdě nebo při přeřazení na kopci.</p>'
          '<h3>Díly na e-kolo</h3>'
          '<p>Elektrokola mají vlastní komponenty. Baterie, motory a nabíječky nejsou univerzální, vybírejte přesně podle výrobce kola a typu systému. Pohon e-kola je namáhanější, proto se na něm používají zesílené řetězy a kazety určené pro elektrokola. Přehled najdete v kategorii <a href="/ebike-baterie/">baterie, motory a nabíječky</a> a v nabídce <a href="/elektrokola/">elektrokol</a>.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Součástky nabízejí například {B(("shimano", "Shimano"), ("sram", "Sram"), ("kenda", "Kenda"), ("maxxis", "Maxxis"), ("ergon", "Ergon"), ("ritchey", "Ritchey"), ("race-face", "Race Face"), ("wtb", "WTB"), ("topeak", "Topeak"), ("force", "Force"), ("rockbros", "RockBros"), ("author", "Author"))}. U všech značek se řiďte popisem produktu a kompatibilitou, ne jménem.</p>'
          '<h3>Sezónní plán údržby</h3>'
          '<p>Na jaře prohlédněte pláště, vyměňte duše s trvalým úbytkem tlaku a zkontrolujte brzdy. V létě sledujte řetěz, protože prach a písek ho obrušují nejrychleji. Na podzim se hodí blatníky a světla, v zimě pláště s hlubším vzorkem a mazivo odolné vodě. Po zimě vyměňte lanka a bowdeny, které zkorodovaly.</p>'
          '<h3>Jak porovnávat nabídky dílů</h3>'
          '<p>U stejného dílu se často nabízí několik variant podle délky, barvy, balení nebo výrobní řady. Porovnávejte kód výrobce a technické parametry, ne jen název. Zkontrolujte, zda je v ceně vše potřebné, například šrouby, ventilky nebo objímky. Sledujte dostupnost jednotlivých velikostí, protože u pláště nebo kotouče bývá skladem jen část rozměrů. Díly s uznávanou normou, jako jsou běžné průměry řídítek nebo závity pedálů, se snadněji nahrazují než proprietární řešení.</p>'
          '<h3>Nářadí a pomůcky, které se vyplatí mít doma</h3>'
          '<p>K výměně dílů se hodí sada imbusových klíčů, kleště na spojky řetězu, měřidlo opotřebení řetězu, montpáky a pumpa s manometrem. Čistič a mazivo na řetěz prodlouží život celému pohonu. Do brašny na kolo patří náhradní duše, záplaty a multiklíč, aby vás defekt nezastavil daleko od domova.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Koupě dílu podle fotografie bez ověření průměru, osy nebo počtu rychlostí.</li>'
          '<li>Nový řetěz na staré, ojeté kazetě, která pak přeskakuje.</li>'
          '<li>Příliš silné dotažení šroubů na karbonu a hliníku.</li>'
          '<li>Míchání brzdových kapalin: minerální olej a DOT se nesmějí zaměnit.</li>'
          '<li>Odkládání výměny pláště, dokud nepřijde první defekt na cestě.</li></ul>',
    faq=[('Jak zjistím, jaký plášť potřebuji na své kolo?', 'Podívejte se na bok stávajícího pláště. Je tam uveden rozměr, například 28 × 1,6 nebo 29 × 2,2. První číslo je průměr, druhé šířka. Při změně šířky ověřte, že se plášť vejde do rámu nebo vidlice a že ráfek má vhodnou vnitřní šířku.'),
         ('Jaký je rozdíl mezi ráfkovou a kotoučovou brzdou?', 'Ráfková brzda tlačí destičky na bok ráfku, kotoučová brzdí o kotouč uprostřed kola. Kotoučová funguje stabilněji za mokra a nezatěžuje ráfek, ale vyžaduje rám a vidlici s uchycením. Jedno nelze snadno přestavět na druhé.'),
         ('Kdy mám vyměnit řetěz?', 'Řetěz se prodlužuje a tím obrušuje kazetu a převodníky. Nejlepší je měřit opotřebení měřidlem a vyměnit řetěz včas. Když to odložíte, vyměníte nakonec celou sadu.'),
         ('Mohu na kolo dát jakákoli řídítka?', 'Ne. Musí odpovídat průměru upnutí představce a typu brzdových a řadicích pák. Důležité je také zvednutí a šířka, které ovlivňují posez a ovladatelnost.'),
         ('Jaké sedlo je nejlepší?', 'Takové, které odpovídá šířce vašich sedacích kostí a stylu jízdy. Na krátké městské cesty stačí pohodlnější sedlo, na delší vyjížďky užší a pevnější s vhodným prostřihem.'),
         ('Co jsou nášlapné a plošinové pedály?', 'Plošinové mají širokou plochu a jezdí se na nich v běžné obuvi. Nášlapné se spojují s tretrou a přenášejí sílu efektivněji, ale vyžadují zvyk při sundávání nohy. Nášlapy musí odpovídat systému pedálu.'),
         ('Je lepší tubeless, nebo klasická duše?', 'Tubeless snižuje počet defektů a umožňuje nižší tlak v terénu, ale vyžaduje kompatibilní ráfek, plášť, ventilky a tmel, který je třeba čas od času doplnit. Klasická duše je jednodušší a levnější na opravu na cestě.'),
         ('Mohu si díly vyměnit sám?', 'Pláště, gripy, pedály, sedlo nebo světla zvládne většina lidí s běžným nářadím. Brzdy a řazení vyžadují zkušenosti a seřízení, ty raději svěřte servisu.'),
         ('Jaké díly se hodí na elektrokolo?', 'Elektrokolo se rozjíždí silněji a tlačí na pohon, proto kupujte řetězy a kazety určené pro e-kola. Baterie, motory a nabíječky vybírejte striktně podle výrobce a typu systému.')],
)

# ------------------------------------------------------------------ sportovni-ponozky
NEW['sportovni-ponozky'] = dict(long=True,
    title='Sportovní ponožky – na běh, turistiku, kolo | Sporteka',
    desc='Sportovní ponožky pro muže, ženy i děti: běžecké, turistické, cyklistické, merino i lyžařské. Porovnejte ceny a vyberte materiál, délku a velikost.',
    intro='<p><strong>Sportovní ponožky</strong> jsou nejlevnější část výbavy, která rozhoduje o tom, zda se na výlet těšíte, nebo zda doma ošetřujete puchýře. Dobrá ponožka odvádí vlhkost, drží na místě, má hladké švy a je zesílená tam, kde noha tlačí. Bavlněná ponožka na dlouhý běh nebo túru tohle nezvládne, protože nasákne potem a začne tlačit. Vyplatí se proto vybírat podle sportu, délky boty a materiálu, a ne podle barvy nebo loga na špičce.</p>'
          '<p>Na Sportece najdete sportovní ponožky od mnoha značek a můžete porovnat nabídky českých obchodů. Samostatné sekce tvoří <a href="/merino-ponozky/">merino ponožky</a>, <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> a <a href="/lyzarske-ponozky/">lyžařské ponožky</a>. K ponožkám patří správná obuv, například <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> nebo <a href="/trailove-boty/">trailové boty</a>.</p>',
    guide='<h2>Jak vybrat sportovní ponožky</h2>'
          '<p>Při výběru si odpovězte na čtyři otázky. Na jaký sport je potřebujete, jak dlouho v nich budete, do jaké boty a v jakém počasí. Podle toho zvolíte tloušťku, délku, materiál a zesílené zóny. Nejlepší ponožka na maraton se liší od nejlepší ponožky na zimní trek, i když je obě označují jako sportovní.</p>'
          '<h3>Podle sportu</h3>'
          + T(['Sport', 'Na co se zaměřit'], [
              ['Silniční běh', 'tenká nebo střední ponožka, bezešvé nebo ploché švy, vzdušné pletení'],
              ['Trail a terén', 'o něco pevnější materiál, vyšší lem proti kamínkům, zesílená pata'],
              ['Turistika', 'střední až silné tlumení, dlouhá životnost, ideálně merino nebo směs'],
              ['Cyklistika', 'lehká, vzdušná, vyšší lem, bez tlačících švů u špičky'],
              ['Fotbal a týmové sporty', 'podkolenky, odolnost v místě chrániče, pevné držení'],
              ['Fitness a posilování', 'kratší ponožka, příjemná v teple, dobře odvádí pot'],
              ['Zimní sporty', 'vyšší, teplejší, bez tlačících švů, specifický tvar na lýtku']]) +
          '<h3>Materiály a jejich vlastnosti</h3>'
          '<p>Materiál ovlivňuje to, jak ponožka odvádí pot, jak rychle schne, jak hřeje a jak dlouho vydrží. Skoro vždy jde o směs, protože jedno vlákno nenabízí všechno.</p>'
          '<ul><li><strong>Polyamid a polyester:</strong> odolné syntetické vlákno, které rychle schne a drží tvar.</li>'
          '<li><strong>Elastan:</strong> přidává pružnost, aby ponožka přilnula k noze a nekrčila se.</li>'
          '<li><strong>Merino vlna:</strong> hřeje i vlhká, pomalu zapáchá a hodí se na delší túry a chladnější počasí.</li>'
          '<li><strong>Bavlna:</strong> příjemná na dotek a prodyšná, ale nasákne a pomalu schne. Na výkon se nehodí.</li>'
          '<li><strong>Bambus a viskóza:</strong> měkké a hladké, vhodné pro citlivou pokožku, ale méně odolné.</li></ul>'
          '<p>Procentuální složení najdete na štítku. Pokud je na prvním místě bavlna s malým podílem syntetiky, jde spíš o volnočasovou ponožku než o výkonnostní. Více o vlně najdete v kategorii <a href="/merino/">merino oblečení</a>.</p>'
          '<h3>Délka ponožky a střih</h3>'
          + T(['Délka', 'Kam se hodí'], [
              ['Neviditelná (nízká)', 'tenisky a lehká obuv, nehodí se do vyšší boty'],
              ['Kotníková', 'běžné běhání a fitness'],
              ['Střední (nad kotník)', 'trailová a turistická obuv, ochrana kotníku'],
              ['Vysoká (crew)', 'trekové boty, chrání před třením okraje boty'],
              ['Podkolenka', 'týmové sporty a lyže, drží u lýtka']]) +
          '<p>Střih ovlivňuje pohodlí. Anatomické ponožky mají označenou pravou a levou nohu, mají prodloužený prostor pro prsty a zesílenou klenbu. Plochý steh na špičce brání otlakům, švy na klenbě a patě tlačí, pokud jsou silné. Vyšší lem u kotníku drží ponožku na místě a nesesouvá se v botě.</p>'
          '<h3>Zesílení a prodyšnost</h3>'
          '<p>Pata a špička bývají zesílené, protože se opotřebovávají nejrychleji. Střední část nohy může mít vzdušnější pletení, tedy síťované pásmo na nártu, kudy proudí vzduch. U turistických ponožek se zesilují chodidlo a lýtko, u běžeckých jen pata a špička, aby nezvyšovaly teplo. Při náročnějším provozu se hodí kompresní zóna kolem klenby, která drží ponožku v správné poloze.</p>'
          '<h3>Velikost: nekupujte „asi tak“</h3>'
          '<p>Velikost je uvedena v rozmezí, například 39 až 42. Na hranici dvou rozměrů zvolte větší, pokud máte širší nohu nebo vysoký nárt, a menší, pokud ponožka u špičky vytahuje. Ponožka se nesmí krčit na patě ani tlačit na špičce. Po vyprání se může trochu srazit, hlavně bavlněné a vlněné modely, proto si nechte rezervu. Při koupi do bot s přesnou velikostí zkoušejte obuv v ponožkách, které použijete na sport.</p>'
          '<h3>Pánské, dámské a dětské ponožky</h3>'
          '<p>Dámské ponožky mají užší patu a nárt, pánské jsou širší. Dětské modely mají měkčí švy a menší rozměry, a protože děti rychle rostou, kupujte raději více kusů ve stejné velikosti, než sahat po příliš velké. Příliš velká ponožka se krčí a je nepohodlná. Rozdíl mezi pohlavími není u všech značek stejný, u neutrálních ponožek rozhoduje rozmezí velikostí.</p>'
          '<h3>Kompresní a regenerační ponožky</h3>'
          '<p>Kompresní ponožky jemně stlačují lýtko a mají podpořit krevní oběh. Hodí se na delší běh, cestování a stání, ale nenahrazují lékařskou radu při žilních potížích. Vyberte správnou velikost podle obvodu lýtka, příliš těsná kompresní ponožka je nepříjemná. Po tréninku ji lze obléct jako regenerační pomůcku.</p>'
          '<h3>Ponožky do zimy a do horka</h3>'
          '<p>V zimě volte vyšší a hustěji pletenou ponožku, nejlépe s merinem, která hřeje i při potu. Příliš tlustá ponožka ale vyplní botu a omezí prokrvení, což vede k prochladnutí, proto k obuvi ladit i tloušťku ponožky. V horku vyberte tenkou vzdušnou ponožku s ventilačními zónami. Na lyže existují samostatné modely, viz <a href="/lyzarske-ponozky/">lyžařské ponožky</a>.</p>'
          '<h3>Péče a životnost</h3>'
          '<p>Ponožky perte naruby při nižší teplotě, bez aviváže, která zalepí vlákna a zhorší odvod potu. Merino nemá rádo vysokou teplotu v sušičce. Páry nepřehazujte, ať se opotřebovávají stejnoměrně. Kupujte ponožky ve stejném provedení a barvě, aby se dalo nahradit ztracený kus. Když se na patě objeví řídká místa nebo ztratí ponožka pružnost, vyměňte je, protože tlumení už nefunguje.</p>'
          '<h3>Ponožky a prevence puchýřů</h3>'
          '<p>Puchýře vznikají třením a vlhkem. Ponožka, která se krčí nebo je promočená, je zhoršuje. Pomáhá správná velikost boty, tenká vnitřní ponožka pod silnou při dlouhých túrách a výměna za suché kusy při delší zastávce. Na dlouhé výlety si bereme náhradní pár.</p>'
          '<h3>Jak ponožky zkoušet a porovnávat v obchodě</h3>'
          '<p>Při porovnávání nabídek sledujte složení, délku a rozmezí velikostí, nejen cenu za pár. Vícekusová balení bývají výhodná na běžné nošení, ale u náročných modelů se často prodávají po páru. Čtěte popis zesílených zón a zjistěte, jestli výrobce uvádí pravou a levou nohu. Pokud si ponožky objednáváte poprvé, vezměte raději jeden pár na zkoušku a po prvním vyprání zkontrolujte, jak drží tvar. Sedí-li dobře, objednejte další kusy ve stejné řadě.</p>'
          '<h3>Ponožky do různé obuvi</h3>'
          '<p>Do nízkých tenisek stačí kotníková nebo neviditelná ponožka, do trailových bot střední délka s vyšším lemem a do pevných treků delší model s tlumením. Do lyžáků patří vyšší ponožka bez švů a bez záhybů, která nesmí být příliš silná, jinak bota tlačí. Boty vybírejte společně s ponožkami, protože tloušťka mění objem v botě. Při koupi si prohlédněte i kategorie <a href="/sportovni-obuv/">sportovní obuv</a> a <a href="/bezecke-boty/">běžecké boty</a>.</p>'
          '<h3>Ponožky pro každodenní trénink a pro závod</h3>'
          '<p>Na trénink si pořiďte více stejných párů, které snesou častější praní. Na závod použijte ponožku, kterou jste už několikrát vyzkoušeli, a nikdy neběhejte nebo nejezděte v nových ponožkách bez předchozího testu. Dlouhé výkony zvládne lépe ponožka s mírným tlumením a hladkými švy než úplně tenká, která se na kilometrech opotřebuje.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V kategorii najdete {B(("adidas", "Adidas"), ("nike", "Nike"), ("smartwool", "Smartwool"), ("lasting", "Lasting"), ("under-armour", "Under Armour"), ("puma", "Puma"), ("fila", "Fila"), ("on", "On"), ("dynafit", "Dynafit"), ("errea", "Errea"), ("force", "Force"), ("tommy-hilfiger", "Tommy Hilfiger"))}. Značky si porovnejte podle složení a střihu, ne jen podle jména.</p>'
          '<h3>Kdy se vyplatí platit víc</h3>'
          '<p>Za kvalitnější ponožky se platí hlavně u dlouhých výkonů a náročné obuvi. Lepší materiál, přesnější střih a pevnější zesílení se projeví po desítkách kilometrů, kdežto na krátkou procházku nebo hodinu fitness stačí jednoduchý model. Rozumný postup je vzít jeden kvalitní pár na nejdůležitější sport a ostatní doplnit podle potřeby. Při opotřebení nejdřív vyměňte ty, které nosíte nejčastěji.</p>'
          '<h3>Ponožky při sportu v chladnu a vlhku</h3>'
          '<p>Za deště a v blátě nasákne i dobrá ponožka, takže rozhoduje, jak rychle vyschne a jestli hřeje i mokrá. Merino a tenká syntetika si s tím poradí lépe než bavlna. Na dlouhý den v terénu vezměte druhý pár do batohu a převlečte se při první delší pauze. Boty po výletu vysušte zvlášť a vložky vyndejte, aby ponožky neměly příště vlhké prostředí.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Bavlněná ponožka na dlouhý výkon nebo mokrý terén.</li>'
          '<li>Nová obuv bez vyzkoušení s ponožkou, ve které se bude sportovat.</li>'
          '<li>Příliš tlustá ponožka v těsné botě.</li>'
          '<li>Praní s aviváží nebo sušení na topení.</li>'
          '<li>Používání ponožky, která už nemá tlumení nebo na patě prosvítá.</li></ul>',
    faq=[('Jaké ponožky se hodí na běhání?', 'Tenké až střední, s plochými švy a vzdušnými zónami. Nejlépe ze syntetické směsi, která rychle schne, případně z tenkého merina. Pata může být lehce zesílená.'),
         ('Jaké ponožky se vybírají na turistiku?', 'Střední nebo silnější s tlumením na chodidle, kotníku a patě. Merino nebo směs s merinem vydrží delší nošení a méně zapáchá. Vyšší lem chrání před třením boty.'),
         ('Proč bavlněné ponožky nejsou dobré na sport?', 'Bavlna nasákne potem a pomalu schne. Vlhká ponožka tře a zvyšuje riziko puchýřů. Na krátké pohodlné chození ale stačí.'),
         ('Kolik párů ponožek mít na delší výlet?', 'Alespoň jeden náhradní pár navíc a při vícedenní túře střídat. Vlhké ponožky vysušte na batohu nebo přes noc, pokud je počasí příznivé.'),
         ('Jak poznám správnou velikost?', 'Ponožka má těsně přiléhat, ale netlačit. Nesmí se krčit na patě ani vytahovat na špičce. Na hranici rozmezí velikostí vyberte podle šířky nohy a podle materiálu, protože bavlna se může srazit.'),
         ('Jsou kompresní ponožky pro každého?', 'Hodí se na delší výkony, cestování a regeneraci, ale nejsou náhradou lékařské péče. Při žilních potížích se poraďte s lékařem a velikost vyberte podle obvodu lýtka.'),
         ('Jak často ponožky vyměňovat?', 'Když zeslábne tlumení na patě, objeví se řídké místo, díra nebo ponožka ztratí pružnost. Pravidelně nošené ponožky vydrží obvykle jednu až dvě sezóny.'),
         ('Mohu ponožky sušit v sušičce?', 'Syntetické obvykle ano na nižší teplotě, merino a bavlnu raději sušte volně, aby se nesrazily. Řiďte se štítkem na výrobku.'),
         ('Jaký je rozdíl mezi pánskými a dámskými ponožkami?', 'Dámské mají užší patu a nárt, pánské jsou širší. U neutrálních ponožek rozhoduje rozmezí velikostí, proto zkontrolujte tabulku u výrobce.')],
)

# ------------------------------------------------------------------ vodni-sporty
NEW['vodni-sporty'] = dict(long=True,
    title='Vodní sporty a plavání – výbava, brýle, neopreny | Sporteka',
    desc='Výbava pro vodní sporty: plavecké brýle, neopreny, paddleboardy, šnorchly, bazény i UV trička. Porovnejte ceny českých obchodů a vyberte podle aktivity.',
    intro='<p><strong>Vodní sporty</strong> zahrnují vše od rekreačního plavání po paddleboarding, šnorchlování a potápění. Výbava se liší podle toho, kde a jak dlouho ve vodě trávíte čas: v bazénu potřebujete brýle, čepici a plavky, na řece plavidlo s vestou, v moři masku a šnorchl. Základem každé volby je bezpečnost, protože voda odpustí méně chyb než souš. Proto stránka začíná otázkou, co děláte, kde a s kým, a teprve potom řeší značky a typy.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů v těchto skupinách: <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-cepice/">plavecké čepice</a>, <a href="/plavecke-pomucky/">plavecké pomůcky</a>, <a href="/neopreny/">neopreny</a>, <a href="/paddleboardy/">paddleboardy a kajaky</a>, <a href="/snorchlovani/">šnorchlování a potápění</a>, <a href="/plazove-doplnky/">plážové doplňky</a>, <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> a <a href="/bazeny/">bazény a nafukovadla</a>.</p>',
    guide='<h2>Jak si vybrat výbavu podle toho, co děláte na vodě</h2>'
          '<p>Nejdřív určete aktivitu a prostředí. Bazén má stabilní teplotu a čistou vodu, rybník nebo řeka mají proměnlivou teplotu, proud a překážky, moře přidává slanou vodu, vlny a slunce. Každé prostředí vyžaduje jinou výbavu a jiný stupeň opatrnosti. Nekupujte vše najednou. Začněte tím, co potřebujete k bezpečnému provozu, a doplňujte postupně.</p>'
          '<h3>Základní výbava podle aktivity</h3>'
          + T(['Aktivita', 'Co nesmí chybět'], [
              ['Plavání v bazénu', '<a href="/plavky/">plavky</a>, plavecké brýle, čepice, případně pomůcky na trénink'],
              ['Plavání v otevřené vodě', 'plavky nebo neopren, brýle, výrazná čepice, bójka viditelnosti'],
              ['Paddleboarding', 'prkno, pádlo, leash, pumpa, vesta, vodotěsný vak'],
              ['Kajak a kánoe', 'plavidlo, pádlo, vesta, odvodňovací pomůcky, vodotěsné vaky'],
              ['Šnorchlování', 'maska, šnorchl, ploutve, případně neopren nebo lycra'],
              ['Rodinný den u vody', 'bazén nebo nafukovadla, UV oblečení, osuška, obuv do vody']]) +
          '<h3>Plavání: brýle, čepice a pomůcky</h3>'
          '<p>Plavecké brýle musí sedět kolem očí bez tlaku a bez prosakování. Zkuste je tak, že je přitisknete k obličeji bez pásku, a pokud chvíli drží podtlakem, těsní. Čočky se liší tónováním: čiré do haly, tónované nebo zrcadlové na slunce, polarizované do otevřené vody. Čepice chrání vlasy před chlórem, snižuje odpor a zlepšuje viditelnost, silikonová vydrží déle a nesmeká, latexová je tenká a levná, textilní hřeje a hodí se spíš pro rekreační plavání. Pomůcky jako plováky, žabky, pádla a ploutve slouží k nácviku techniky a posílení konkrétních svalů. Najdete je v kategoriích <a href="/plavecke-bryle/">brýle</a>, <a href="/plavecke-cepice/">čepice</a> a <a href="/plavecke-pomucky/">pomůcky</a>.</p>'
          '<h3>Plavky pro sport a rekreaci</h3>'
          '<p>Na pravidelný trénink v bazénu vybírejte plavky z materiálu odolného chlóru, který drží tvar a netvoří žmolky. Pánské slipy a jammery se liší krytím stehen, dámské jednodílné plavky sedí na těle pevněji než dvoudílné. Pro dovolenou stačí pohodlný střih a rychle schnoucí materiál. Výběr najdete v kategoriích <a href="/panske-plavky/">pánské plavky</a>, <a href="/damske-plavky/">dámské plavky</a> a <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h3>Neopreny a teplota vody</h3>'
          '<p>Neopren je pěnová látka, která zadržuje tenkou vrstvu vody mezi tělem a oblekem, kde se ohřeje. Proto musí obleku těsně sedět, ale nesmí omezovat pohyb ramen a nedusit dýchání. Silnější neopren hřeje víc, tenčí je pohyblivější. Rozlišují se dlouhé obleky, krátké obleky na jaro a léto, vesty a doplňky jako boty a rukavice. Plavecké neopreny pro triatlon a otevřenou vodu jsou na rozdíl od surfových hladší a pružnější v ramenou. Po použití oplachujte sladkou vodou a sušte ve stínu naruby. Výběr najdete v kategorii <a href="/neopreny/">neopreny</a>.</p>'
          '<h3>Paddleboardy a kajaky</h3>'
          '<p>Paddleboard se vybírá podle váhy jezdce, nosnosti, délky a šířky. Nafukovací prkna se vejdou do batohu a hodí se pro většinu rekreačních jezdců, pevná se pohodlněji ovládají při závodění a surfování. Kajaky a kánoe potřebují více místa a plovací vesta je jejich nezbytnou součástí (povinnost se řídí předpisy a trasou). Při rozhodování pomáhá, jestli se chcete věnovat klidným túrám na rybníce, nebo rychlejší jízdě po řece. Podrobnosti a typy najdete v kategorii <a href="/paddleboardy/">paddleboardy a kajaky</a> a v samostatných sekcích <a href="/kajaky-a-cluny/">kajaky a čluny</a> a <a href="/plovaci-vesty/">plovací vesty</a>.</p>'
          '<h3>Šnorchlování a potápění</h3>'
          '<p>Základní sada se skládá z masky, šnorchlu a ploutví. Maska se zkouší tak, že ji přitisknete k obličeji bez pásku, nadechnete se nosem a pokud drží, těsní. Silikonová sukně je měkká a pohodlná, tvrzené sklo odolává poškrábání. Šnorchl může mít ventil proti vniknutí vody, ale je to otázka pohodlí, ne bezpečnosti. Ploutve s otevřenou patou se nosí s botou, s uzavřenou patou boso. Potápění s přístrojem vyžaduje certifikovaný výcvik, výbava jako regulátory a vesty se musí pravidelně servisovat. Vše najdete v kategorii <a href="/snorchlovani/">šnorchlování a potápění</a>.</p>'
          '<h3>Ochrana před sluncem u vody</h3>'
          '<p>Hladina odráží světlo a na vodě se spálíte rychleji než na souši. UV tričko nebo lycra s dlouhým rukávem chrání ramena a záda, která jsou na paddleboardu nebo při šnorchlování nejvíce exponovaná. Doplňte ho kloboukem a brýlemi s polarizací. Voděodolný krém obnovujte podle návodu výrobce, ne podle toho, jak se cítíte. Viz <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> a <a href="/plazove-doplnky/">plážové doplňky</a>.</p>'
          '<h3>Bazény, nafukovadla a hry na vodě</h3>'
          '<p>Nafukovací a rámové bazény se vybírají podle velikosti zahrady, počtu lidí a toho, zda chcete bazén stavět jednou na celé léto. Bazén vyžaduje rovný základ, filtraci nebo alespoň pravidelnou výměnu vody a úpravu chemií. Menší dětské bazény se vyprazdňují po každém dni. U nafukovadel kontrolujte maximální nosnost a doporučený věk. Nafukovadlo není záchranná pomůcka a dítě u něj nesmí zůstat bez dozoru. Přehled najdete v kategorii <a href="/bazeny/">bazény a nafukovadla</a>.</p>'
          '<h3>Bezpečnost před volbou vybavení</h3>'
          '<p>Ptejte se, co se stane, když spadnete do vody. Plovací vesta by měla odpovídat váze a mít dobrý uzávěr, vesta pro dítě navíc poutko mezi nohama. Na řece sledujte proud, jezy a spadlé stromy, na moři vítr a odliv. V neznámém prostředí plavte s bójkou, která vás zviditelní. Nikdy nepodceňujte studenou vodu, šok z ní dokáže ochromit i zdatného plavce během vteřin. Vybavení nenahradí zdravý rozum, ale pomáhá ho uplatnit.</p>'
          '<h3>Péče o vybavení</h3>'
          '<p>Po koupání v chlóru nebo moři všechno opláchněte sladkou vodou. Brýle neotírejte hadrem uvnitř čoček, nechte uschnout na vzduchu a uložte v pouzdře. Neopren neskládejte do ostrých záhybů, věšte ho na široké ramínko. Nafukovací věci sušte, lehce vypusťte a skladujte mimo slunce a mimo hlodavce. Kovové části, třeba zip nebo ventily, mažte podle doporučení výrobce.</p>'
          '<h3>Vodní sporty s dětmi a začátečníky</h3>'
          '<p>Děti se učí nejlépe v mělké a teplé vodě pod dohledem dospělého. Dětská vesta musí odpovídat váze a držet hlavu nad hladinou, rukávky a nafukovací kruhy ji nenahradí. Začátečníci v dospělosti by měli vyzkoušet základy v bazénu, než sáhnou po prkně nebo kajaku. Lekce plavání nebo paddleboardingu s instruktorem ušetří spoustu přepracování špatných návyků.</p>'
          '<h3>Přeprava a skladování</h3>'
          '<p>Nafukovací plavidla se vejdou do auta bez střešního nosiče a zabírají v bytě málo místa. Pevná prkna a kajaky potřebují nosič a bezpečné upevnění popruhy. Mokrý neopren a plavky přepravujte v oddělené tašce a doma je hned rozviňte. Drobnosti jako telefon a klíče uložte do vodotěsného vaku, který zároveň plave.</p>'
          '<h3>Plavání v přírodní vodě krok za krokem</h3>'
          '<p>Před prvním plaváním v rybníce nebo přehradě si zjistěte, zda je koupání povolené a jaká je kvalita vody. Vstupujte postupně, aby si tělo zvyklo na teplotu, a zůstaňte blízko břehu. Výrazná čepice a bójka s popruhem k pasu vás zviditelní pro lodě i rybáře. Plavte s kamarádem nebo tak, aby o vás někdo věděl. Po koupání se rychle převlečte do suchého a teplého oblečení, protože tělo se po výstupu z vody ochlazuje nejvíc. V chladnější vodě začněte krátkými úseky a délku postupně prodlužujte, neopren i čepice z neoprenu pomáhají zadržet teplo.</p>'
          '<h3>Jak vybrat pádlo a doplňky k plavidlu</h3>'
          '<p>Pádlo se volí podle výšky a stylu jízdy. Lehčí pádlo méně unavuje při delší túře, nastavitelná délka se hodí, když pádluje víc lidí. Součástí výbavy je vodotěsný vak, pumpa s manometrem, opravná sada a lano na přivázání plavidla. Na delší trasy přidejte píšťalku, svítilnu a základní lékárničku. Všechno se vejde do jednoho vodotěsného vaku, který plave na hladině.</p>'
          '<h3>Sezónnost a plánování nákupů</h3>'
          '<p>Vybavení na léto se nejrychleji vyprodává na jaře. Plavecké pomůcky a brýle jsou naopak celoroční, protože bazény fungují i v zimě. Neopreny se prodávají hlavně před sezónou. Nafukovadla a bazény kupujte s předstihem, ať máte čas vyzkoušet a opravit případnou vadu. Na podzim se vyplatí sledovat výprodeje, hlavně u prken a plavidel.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce najdete {B(("speedo", "Speedo"), ("arena", "Arena"), ("finis", "Finis"), ("mad-wave", "Mad Wave"), ("aqua-speed", "Aqua Speed"), ("aqualung", "Aqualung"), ("mares", "Mares"), ("o-neill", "O\'Neill"), ("intex", "Intex"), ("bestway", "Bestway"), ("aqua-marina", "Aqua Marina"), ("nils", "Nils"), ("agama", "Agama"))}. Výběr si zpřesněte podle konkrétní skupiny, protože každá značka je silná v jiné oblasti.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Nákup brýlí podle vzhledu, nikoli podle toho, jak těsní.</li>'
          '<li>Neopren o číslo větší, ve kterém se hromadí voda a tělo vychládá.</li>'
          '<li>Prkno nebo plavidlo s malou nosností vzhledem k váze a vybavení.</li>'
          '<li>Podcenění slunce a studené vody.</li>'
          '<li>Skladování mokrého vybavení v tašce, které zplesniví.</li></ul>',
    faq=[('Co si vzít na první paddleboarding?', 'Plovací vestu a leash (na řece s rychlým uvolněním), prkno s dostatečnou nosností a pádlo ve správné délce. Hodí se také UV tričko, klobouk, vodotěsný vak a při chladné vodě neopren.'),
         ('Jak poznám, že plavecké brýle těsní?', 'Přitiskněte čočky k očím bez nasazeného pásku. Pokud se na chvíli drží podtlakem, těsní. Poté nastavte pásek tak, aby nebyl příliš utažený.'),
         ('Jaký neopren si vybrat?', 'Podle teploty vody a aktivity. Krátký obleček stačí na teplejší vodu, dlouhý na jaro a podzim. Musí těsně sedět a nesmí omezovat ramena.'),
         ('Jaký je rozdíl mezi plaveckým a surfovým neoprenem?', 'Plavecký neopren je tenčí a pružnější v oblasti ramen, aby nebránil záběru. Surfový je tlustší a robustnější a hřeje víc, ale omezuje pohyb při dlouhém plavání.'),
         ('Je nafukovací bazén bezpečný pro děti?', 'Jen pod stálým dohledem. I malá hloubka je riziko, proto vodu vypouštějte po koupání a bazén zabezpečte, když ho nepoužíváte.'),
         ('Jaká maska se hodí na šnorchlování?', 'Taková, která těsní bez pásku a pohodlně sedí v oblasti nosu. Silikonová sukně je měkká a tvrzené sklo je odolné. Před nákupem ověřte velikost obličeje.'),
         ('Potřebuji vestu i pro plavce?', 'Na řece, na otevřené vodě a při jízdě na plavidle ji doporučujeme každému. I dobrý plavec může být zraněn nebo vyčerpán.'),
         ('Jak se starat o plavecké brýle?', 'Po použití opláchněte sladkou vodou, nechte uschnout a uložte v pouzdře. Čočky neotírejte, protože antifogová vrstva se snadno poškodí.'),
         ('Jak chránit kůži na vodě?', 'UV oblečením, kloboukem, brýlemi a voděodolným krémem, který obnovujete podle návodu. Voda odráží světlo, takže se spálíte rychleji než na souši.')],
)
