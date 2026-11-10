"""sporteka.cz — wave 23i (5. 11. 2026): long texts (>= 1650 words) for silnicni-cyklohelmy, atletika, perove-spacaky, ebike-baterie.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ silnicni-cyklohelmy
NEW['silnicni-cyklohelmy'] = dict(long=True,
    title='Silniční a gravel cyklohelmy: výběr, velikost, MIPS',
    desc='Silniční a gravel cyklistické helmy: jak vybrat velikost, větrání, MIPS a aerodynamický tvar. Porovnejte nabídky českých obchodů.',
    intro='<p>Silniční a gravelová helma je lehká, dobře větraná přilba pro rychlou jízdu na asfaltu, štěrku a dlouhých výjezdech do kopce. Má menší profil než horská přilba, užší kšilt nebo žádný a větší počet větracích otvorů, takže drží hlavu v chladu i při dlouhém výkonu. Sporteka porovnává nabídky českých obchodů u silničních, aerodynamických i gravelových modelů a pomáhá vám najít správnou velikost, tvar i ochranné technologie.</p>'
          '<p>Mezi výsledky jsou zastoupeny značky ' + B(('abus', 'Abus'), ('limar', 'Limar'), ('alpina', 'Alpina'), ('rockbros', 'Rockbros'), ('lazer', 'Lazer'), ('uvex', 'Uvex'), ('giro', 'Giro'), ('kask', 'Kask')) +
          '. K helmě se hodí <a href="/cyklisticke-bryle/">cyklistické brýle</a>, <a href="/cyklisticke-dresy/">dresy</a> a <a href="/cyklisticke-rukavice/">rukavice</a>. Širší přehled najdete v nadřazené kategorii <a href="/cyklisticke-helmy/">cyklistické helmy</a>.</p>',
    guide='<h2>Čím se silniční helma liší od ostatních</h2>'
          '<p>Silniční helma se konstruuje s ohledem na nízkou hmotnost, větrání a aerodynamiku. Skořepina je tenká a často spojená s pěnou ve formě, takže přilba je štíhlá a pevná. Vzadu sahá nízko na týl, v předu nemá výrazný kšilt a popruhy jsou úzké, aby netlačily při předklonu na řídítkách. Horská helma má naopak větší krytí zátylku a spánků a pevný kšilt proti větvím a slunci.</p>'
          + T(['Typ helmy', 'Typické vlastnosti', 'Hodí se pro'], [
              ['Klasická silniční', 'lehká, hodně větracích otvorů, krátký nebo žádný kšilt', 'vyjížďky, kopce, závody, léto'],
              ['Aerodynamická', 'méně otvorů, protažený zadní tvar, hladký povrch', 'rychlé skupinové jízdy, časovky, rovina'],
              ['Gravelová', 'o něco větší krytí hlavy, malý kšilt, často sklopný', 'štěrkové cesty, bikepacking, smíšený terén'],
              ['Trekingová a městská', 'pevnější konstrukce, často s osvětlením', 'dojíždění, výlety, pomalejší tempo']]) +
          '<p>Hranice mezi typy není ostrá. Řada gravelových helem vypadá jako silniční, ale přidává pár centimetrů krytí vzadu, a některé aerodynamické modely mají zadní otvory, které se dají přelepit. Chcete-li kombinovat silnici s lesními cestami, přečtěte si i kategorii <a href="/mtb-a-integralni-helmy/">MTB a integrální helmy</a>, kde je krytí výraznější.</p>'
          '<h2>Jak zjistit správnou velikost</h2>'
          '<p>Velikost helmy se určuje podle obvodu hlavy v centimetrech. Změřte krejčovským metrem obvod hlavy zhruba centimetr nad obočím a ušima a porovnejte ho s rozpětím, které uvádí výrobce. Velikosti S, M a L nejsou mezi značkami totožné, a proto spoléhejte na číselné rozmezí, ne na písmeno.</p>'
          '<h3>Zkouška po nasazení</h3>'
          '<ul><li><strong>Poloha:</strong> helma sedí vodorovně, okraj je dva prsty nad obočím. Nesmí se sklápět dozadu, aby nezůstalo čelo nechráněné.</li>'
          '<li><strong>Popruhy:</strong> tvoří písmeno V pod uchem a pod bradou se dají provléknout jeden nebo dva prsty. Při otevření úst cítíte jemné potažení.</li>'
          '<li><strong>Kolečko:</strong> systém utažení vzadu doladí obvod bez tlaku na čelo. Po utažení se helma při zakývání hlavou nehýbe.</li>'
          '<li><strong>Tvar hlavy:</strong> někdo má hlavu spíš kulatou, jiný protáhlou. Různé značky mají různý vnitřní tvar a vyplatí se je střídat.</li></ul>'
          '<p>Pokud se pohybujete mezi dvěma velikostmi, zkuste menší s doladěným kolečkem. Příliš velká přilba při pádu sklouzne a chrání hůř. Dětem a mládeži patří <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>, protože hlava roste a tvar je jiný.</p>'
          '<h2>Větrání, hmotnost a aerodynamika</h2>'
          '<p>Počet a velikost větracích otvorů ovlivňuje, kolik vzduchu proudí kolem hlavy. Uvnitř helmy jsou kanálky, které odvádí teplý vzduch dozadu. V letním horku a při výjezdech je větrání nejdůležitější vlastnost a hmotnost se projeví zejména na dlouhých trasách. Aerodynamické přilby při vysoké rychlosti kladou menší odpor vzduchu, ale v pomalém tempu hřejí.</p>'
          '<ul><li><strong>Léto a kopce:</strong> vyberte helmu s velkým počtem otvorů a nízkou hmotností.</li>'
          '<li><strong>Rychlé skupiny a rovina:</strong> aerodynamický tvar s hladkým povrchem ušetří energii.</li>'
          '<li><strong>Chladné dny:</strong> pod helmu se hodí tenká čepice nebo čelenka. Při koupi nechte v obvodu malou rezervu.</li>'
          '<li><strong>Hmotnost:</strong> na sportovní jízdu rozhoduje o pocitu z helmy a únavě krčních svalů.</li></ul>'
          '<h2>Ochranné technologie a konstrukce</h2>'
          '<p>Základem je pěnová výplň z expandovaného polystyrenu, která při nárazu pohlcuje energii. Technologie in-mold slučuje tenkou vnější skořepinu s pěnou, a tím vzniká lehká a pevná přilba. Hybridní konstrukce přidávají vyztužení nebo kostru, která drží tvar. Pro EU se kontroluje shoda s normou EN 1078, kterou najdete na štítku uvnitř helmy.</p>'
          '<h3>MIPS a podobné systémy</h3>'
          '<p>Při šikmém nárazu může helma s hlavou rotovat. Systémy typu MIPS přidávají uvnitř kluznou vrstvu, která umožní mírný pohyb přilby vůči hlavě a snižuje rotační sílu přenášenou na mozek. Konstrukcí podobného typu existuje několik a výrobci je různě pojmenovávají. Neznamenají, že se helma stane nezničitelnou, ale doplňují základní ochranu. Při výběru věnujte pozornost i tomu, jak pohodlně přilba sedí, protože i nejlepší technologie nepomůže, když se vám helma při jízdě posouvá.</p>'
          '<h3>Další prvky</h3>'
          '<ul><li><strong>Hmyzí síťka:</strong> chrání otvory na přední části před vosami a mouchami.</li>'
          '<li><strong>Odnímatelné vložky:</strong> dají se prát a nahradit, když se opotřebují.</li>'
          '<li><strong>Zadní světlo a odrazky:</strong> některé modely mají integrované LED světlo. Zvyšují viditelnost, ale nenahrazují <a href="/cyklo-svetla/">světla na kole</a>.</li>'
          '<li><strong>Magnetická přezka:</strong> usnadňuje zapnutí v rukavicích.</li></ul>'
          '<h2>Gravelová helma: na co si dát pozor</h2>'
          '<p>Gravel spojuje silniční rychlost s volnějším terénem. Kromě větrání ocení jezdec malý nebo sklopný kšilt proti slunci, mírně hlubší krytí spánků a týlu a nastavitelnou polohu popruhů. Pokud po štěrku jezdíte i s brýlemi, ověřte, že se obě součásti k sobě hodí a popruhy nekolidují se stranicemi. Na technické sjezdy je lepší sáhnout po horské přilbě, přehled najdete u <a href="/horska-kola/">horských kol</a> a jejich výbavy.</p>'
          '<h2>Pro koho je která helma</h2>'
          + T(['Jezdec', 'Doporučení', 'Čemu se vyhnout'], [
              ['Začátečník, rekreační jízda', 'střední větrání, pohodlné popruhy, jednoduché kolečko', 'příliš aerodynamických modelů s malými otvory'],
              ['Pravidelný silničář', 'lehká helma s dobrým větráním, výměnné vložky', 'těžké modely s masivním kšiltem'],
              ['Závodník a rychlé skupiny', 'aerodynamický tvar, hladký povrch, nízká hmotnost', 'horké letní jízdy bez možnosti odkrýt otvory'],
              ['Gravel a bikepacking', 'kšilt, větší krytí, odolnost proti otěru', 'křehké ultra lehké modely'],
              ['Dojíždění', 'viditelnost, světlo, praktická přezka', 'zbytečná technika na úkor pohodlí']]) +
          '<h2>Péče o helmu a kdy ji vyměnit</h2>'
          '<p>Helmu čistěte vlažnou vodou s jemným mýdlem a nepoužívejte rozpouštědla, která poškozují pěnu a plast. Vložky vyperte podle návodu a nechte uschnout na vzduchu. Skladujte ji na suchém místě, ne ve vyhřátém autě, kde teplo zkracuje životnost materiálu.</p>'
          '<ul><li><strong>Po pádu:</strong> pokud helma utrpěla nárazem, vyměňte ji, i když navenek vypadá v pořádku. Pěna se mohla zdeformovat.</li>'
          '<li><strong>Stáří:</strong> výrobci obvykle doporučují obměnu po několika letech, protože se materiály vlivem slunce, potu a prachu unavují.</li>'
          '<li><strong>Nálepky a barvy:</strong> lepidla a barvy s rozpouštědly mohou skořepinu narušit.</li>'
          '<li><strong>Převoz:</strong> nenoste helmu zavěšenou na řídítkách, kde se otlouká.</li></ul>'
          '<h2>Co k helmě pořídit</h2>'
          '<p>Helma nechrání sama. Kompletní výbava zahrnuje <a href="/cyklisticke-bryle/">brýle</a>, které chrání oči před vzduchem a hmyzem, <a href="/cyklisticke-rukavice/">rukavice</a> s vycpávkou na dlaních a <a href="/cyklisticka-obuv/">tretry nebo boty</a> pro efektivní šlapání. Pro delší trasy pomůže <a href="/cyklo-computery/">cyklocomputer</a> a <a href="/cyklo-lahve-a-drzaky/">láhev s držákem</a>. Pokud zvažujete i nové kolo, projděte si <a href="/silnicni-a-gravel-kola/">silniční a gravel kola</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupovat podle vzhledu a barvy, bez ověření obvodu hlavy.</li>'
          '<li>Nedotahovat popruhy, takže helma při pádu sklouzne z hlavy.</li>'
          '<li>Používat starou helmu po nárazu nebo po mnoha letech.</li>'
          '<li>Vybírat aerodynamickou přilbu na horský výjezd v horku.</li>'
          '<li>Nosit helmu nakloněnou dozadu a nechat čelo odkryté.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>U každého modelu vidíte nabídky více českých obchodů, takže porovnáte cenu, dostupnost velikostí i dodání. Filtrujte podle značky, barvy a velikosti a otevřete detail pro popis technologií. Vybíráte-li pro sebe a partnera, ověřte velikosti zvlášť, protože tvar hlavy se liší.</p>',
    faq=[
        ('Jak poznám správnou velikost silniční helmy?', 'Změřte obvod hlavy metrem asi centimetr nad obočím a ušima a porovnejte ho s rozpětím centimetrů u daného modelu. Helma má sedět vodorovně a po utažení kolečka se nesmí hýbat.'),
        ('Je MIPS nutný?', 'Není povinný, ale přidává ochranu při šikmých nárazech, při kterých se hlava otáčí. Pokud vám model s MIPS sedí a odpovídá rozpočtu, je rozumnou volbou. Rozhodující je ale především správná velikost a nasazení.'),
        ('Čím se liší gravelová helma od silniční?', 'Gravelová má obvykle větší krytí hlavy, malý kšilt a odolnější konstrukci pro smíšený terén. Silniční je lehčí a více větraná, určená hlavně pro asfalt.'),
        ('Kdy vyměnit cyklistickou helmu?', 'Po každém pádu a nárazu, i když vypadá celá. Výrobci také doporučují obměnu po několika letech používání, protože pěna a plast stárnou vlivem slunce, potu a času.'),
        ('Jsou aerodynamické helmy horké?', 'Mají méně větracích otvorů, a proto v pomalém tempu a v horku hřejí víc než klasické silniční modely. Hodí se hlavně do rychlé jízdy.'),
        ('Jak helmu čistit?', 'Vlažnou vodou s jemným mýdlem, bez rozpouštědel a agresivní chemie. Vnitřní vložky se dají vyprat a nechají se uschnout při pokojové teplotě.'),
        ('Mohu nosit pod helmou čepici?', 'Ano, tenká cyklistická čepice nebo čelenka se pod helmu vejde. Při koupi počítejte s malou rezervou v obvodu, aby helma po nasazení čepice netlačila.'),
        ('Musím nosit helmu s integrovaným světlem?', 'Ne. Světlo v helmě zvyšuje viditelnost, ale nenahrazuje přední a zadní světla na kole, která mají předpisy a spolehlivě osvětlí cestu.'),
        ('Jaká helma je vhodná pro dojíždění?', 'Pohodlná, s dobrým sezením, viditelnou barvou a případně světlem. Pro město jsou k dispozici i městské cyklohelmy s odolnější konstrukcí.'),
        ('Může stejnou helmu používat více lidí?', 'Nedoporučuje se. Pěna a vložky se přizpůsobují konkrétní hlavě a hygiena i správné sezení se tím zhorší. Každý jezdec by měl mít vlastní helmu.'),
    ],
)

# ------------------------------------------------------------------ atletika
NEW['atletika'] = dict(long=True,
    title='Atletika: hroty, oštěpy, překážky, startovací bloky',
    desc='Atletické vybavení: hroty, oštěpy, koule, překážky, startovní bloky a oblečení. Jak vybrat podle disciplíny a věku a porovnat obchody.',
    intro='<p>Atletika zahrnuje běh, skoky a vrhy a každá disciplína má vlastní vybavení. V kategorii najdete atletické hroty, oštěpy včetně pěnových, koule, kriketové míčky, překážky, startovací bloky, značky a oblečení pro trénink i závody. Sporteka porovnává nabídky českých obchodů a pomáhá vybrat vhodnou výbavu pro děti, školy, kluby i dospělé sportovce.</p>'
          '<p>Hlavní zastoupení mají značky ' + B(('merco', 'Merco'), ('powershot', 'Powershot'), ('mizuno', 'Mizuno'), ('sedco', 'Sedco'), ('jipast', 'Jipast'), ('puma', 'Puma'), ('kiprun', 'Kiprun'), ('joma', 'Joma')) +
          '. K atletice patří i <a href="/bezecka-obuv/">běžecká obuv</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a> a širší nabídka v kategorii <a href="/beh/">běh, triatlon a atletika</a>.</p>',
    guide='<h2>Co všechno spadá do atletické výbavy</h2>'
          '<p>Atletika se dělí na běžecké, skokanské a vrhačské disciplíny. Každá potřebuje jiné pomůcky a jiný typ obuvi. Níže najdete přehled toho, co se v kategorii hledá nejčastěji, a k čemu to slouží.</p>'
          + T(['Vybavení', 'K čemu slouží', 'Poznámka'], [
              ['Atletické hroty', 'sprinty, střední tratě, skoky, vrhy', 'liší se podle disciplíny a tvaru podrážky'],
              ['Startovací bloky', 'start ze sprintu', 'nastavitelné pro různé délky nohou'],
              ['Překážky', 'běh přes překážky a trénink techniky', 'nastavitelná výška, stabilní základna'],
              ['Oštěpy', 'hod oštěpem a nácvik techniky', 'dřevěné, plastové, pěnové pro děti'],
              ['Koule', 'vrh koulí', 'litinové a plastové, podle věku a síly'],
              ['Kriketové míčky', 'hod míčkem ve školách a přípravkách', 'různé hmotnosti'],
              ['Značky a metry', 'vyznačení tratí a odrazu', 'barevné kužele a pásky']]) +
          '<p>Vybavení je určeno hlavně pro oddíly, školy a trenéry, ale velkou část využijí i rodiče, kteří chtějí dětem doma vyzkoušet základy techniky. Pokud je pro vás atletika novinka, začněte jednoduchými pomůckami a obuví, která zvládne i běžný trénink.</p>'
          '<h2>Atletické hroty: výběr podle disciplíny</h2>'
          '<p>Hroty jsou tretry s kovovými trny v přední části podrážky, které zvyšují přilnavost na umělém povrchu dráhy. Pro každou disciplínu existuje jiný typ, protože se liší sklon, tuhost a pozice trnů. Obecně platí, že sprinterské hroty jsou velmi tuhé a mají trny po celé přední části chodidla, zatímco hroty pro delší tratě mají víc tlumení.</p>'
          '<h3>Typy hrotů</h3>'
          '<ul><li><strong>Sprinterské:</strong> pro 60 až 400 metrů, tuhá deska, prostor pro prsty, minimální tlumení.</li>'
          '<li><strong>Střední tratě:</strong> lehčí než sprinterské, s více pružnosti a komfortu pro delší úsilí.</li>'
          '<li><strong>Dlouhé tratě:</strong> s lepším tlumením a menším počtem trnů.</li>'
          '<li><strong>Skokanské:</strong> zesílená přední část a v patě pěna pro dopad.</li>'
          '<li><strong>Víceúčelové:</strong> pro děti a začátečníky, kteří zkoušejí více disciplín najednou.</li></ul>'
          '<p>Délka trnů se volí podle povrchu dráhy a pravidel stadionu. Zjistěte si, jaká délka je povolená, protože některé stadiony používají omezení. V balení bývá klíč a sada náhradních trnů. Pro dětské vybavení postačí méně specializovaný model, který zvládne i běžný trénink. Širší nabídku boty najdete v kategorii <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> a <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
          '<h3>Velikost hrotů</h3>'
          '<p>Hroty mají sedět těsně, ale nesmí tlačit. Při sprintu chodidlo vyvíjí tlak na špičku, a tak je potřeba, aby se prsty mohly mírně roztáhnout. U značek se velikostní tabulky liší, takže před koupí ověřte délku chodidla v centimetrech. Děti rostou a často volí o půl čísla větší, ale ne víc, jinak se noha v botě posouvá.</p>'
          '<h2>Vrhy: koule, oštěpy, kriketové míčky</h2>'
          '<p>Vrhačské disciplíny vyžadují správnou techniku a hmotnost náčiní odpovídající věku. Pro děti existují lehčí koule a oštěpy, které dovolují naučit pohyb bez zátěže pro klouby. Dospělí a závodníci používají náčiní podle pravidel své kategorie.</p>'
          '<ul><li><strong>Koule:</strong> litinové koule jsou klasika pro školy i kluby, plastové s plnicí hmotou se hodí pro trénink v hale a děti.</li>'
          '<li><strong>Oštěpy:</strong> pro závodní kategorie se liší hmotnost a délka. Děti začínají s pěnovými nebo plastovými oštěpy, které bezpečně létají a nepoškodí zem.</li>'
          '<li><strong>Kriketové míčky:</strong> používají se pro školní hod míčkem a atletickou přípravku. Nabízejí se v různých hmotnostech.</li>'
          '<li><strong>Vrhací pomůcky:</strong> vířivé oštěpy a vrhače míčků pomáhají procvičit pohyb ramene bez složité techniky.</li></ul>'
          '<p>Při práci s oštěpem platí bezpečnostní pravidla. Vymezte prostor, kde nikdo nestojí, házejte jen na pokyn trenéra a oštěpy po tréninku sbírejte najednou. Pěnové oštěpy jsou vhodné pro začátečníky a školní hodiny, protože jsou měkké a pomalejší.</p>'
          '<h2>Startovací bloky a překážky</h2>'
          '<p>Startovací bloky mají dvě opěrky pro nohy, které se posouvají po kolejnici a nastavují se podle délky nohou a stylu startu. Důležitá je stabilita na dráze: kolíky nebo trny drží blok při odrazu a základna nesmí klouzat. Pro školy a kluby volte pevnou konstrukci z oceli, doma stačí lehčí variantu.</p>'
          '<p>Překážky mají nastavitelnou výšku. Překážka je konstruována tak, aby se při nárazu převrátila ve směru běhu a běžce nezranila. Pro děti jsou nízké překážky z plastu nebo pěny, které umožní nacvičit rytmus a techniku přeběhu. Pro vyšší kategorie jsou překážky z kovu s nastavením v celém rozsahu. Při výběru ověřte, zda se dají výškově nastavit a jak jsou stabilní.</p>'
          + T(['Pomůcka', 'Pro koho', 'Na co se dívat'], [
              ['Startovací bloky', 'sprinterské oddíly, školy', 'stabilita, nastavení úhlu, kolíky'],
              ['Překážky nastavitelné', 'kluby, trenéři', 'výškový rozsah, váha, základna'],
              ['Dětské překážky', 'přípravka a školní tělocvična', 'měkký materiál, bezpečný pád'],
              ['Značky a kužely', 'každý trénink', 'viditelnost, stohování, hmotnost']]) +
          '<h2>Oblečení a doplňky pro atletiku</h2>'
          '<p>Atletické oblečení je lehké, přiléhavé a odvádí pot. Sprinteři a skokani volí krátké kraťasy a tílka, vrhači pohodlné volnější střihy. V chladu se hodí <a href="/leginy/">legíny</a>, <a href="/funkcni-mikiny/">funkční mikiny</a> a <a href="/funkcni-tricka/">funkční trička</a>. Nezapomeňte na <a href="/sportovni-ponozky/">sportovní ponožky</a>, které při dlouhém tréninku zabrání puchýřům.</p>'
          '<ul><li><strong>Sprint:</strong> přiléhavé kraťasy nebo kalhoty, které neomezují krok.</li>'
          '<li><strong>Skoky:</strong> lehké tílko, aby nepřekáželo při odrazu.</li>'
          '<li><strong>Vrhy:</strong> pohodlné oblečení s volností pro ramena.</li>'
          '<li><strong>Zima:</strong> vrstvení s termo prádlem a větruvzdornou vrstvou.</li></ul>'
          '<h2>Atletika pro děti a školy</h2>'
          '<p>Atletická přípravka potřebuje bezpečné a zábavné náčiní. Pěnové oštěpy, měkké překážky, lehké koule a barevné kužele umožní učit základní pohyby hrou. Soupravy pro přípravku obvykle kombinují několik pomůcek pro nácvik běhu, skoku a hodu. Při výběru pro školu zohledněte úložný prostor a odolnost proti vlhku. Doplňte je o <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/funkcni-trenink/">pomůcky pro funkční trénink</a>, kterými si děti posílí tělo.</p>'
          '<p>Rodiče, kteří chtějí dětem koupit první atletické hroty, nemusí sahat po špičkových modelech. Dětské hroty bývají lehké, s měkčí podrážkou a trny kratšími než u dospělých. Důležitější než značka je, aby bota seděla a dítě se v ní cítilo jistě.</p>'
          '<h2>Péče o vybavení</h2>'
          '<ul><li><strong>Hroty:</strong> po tréninku vyčistěte trny od zbytků drahy a vysušte je při pokojové teplotě. Trny občas vyměňte a kontrolujte utažení.</li>'
          '<li><strong>Oštěpy a koule:</strong> otřete od hlíny a uložte na suchém místě. Dřevěné nebo kovové části chraňte před vlhkem.</li>'
          '<li><strong>Bloky a překážky:</strong> po použití odstraňte z kolejnic písek a prach a v zimě je neskladujte ve vlhku.</li>'
          '<li><strong>Oblečení:</strong> perte podle štítku, bez aviváže, která zhoršuje odvod vlhkosti.</li></ul>'
          '<h2>Co se v kategorii ještě objeví</h2>'
          '<p>Kategorie je nejednoznačná, a proto se mezi výsledky občas vyskytnou i věci, které s atletikou souvisejí jen vzdáleně, například tréninkové stepy, atletické draky nebo rybářské vrhací tyče. U takových položek ověřte popis a použití. Pro míčové hry se podívejte do kategorie <a href="/micove-sporty/">míčové sporty</a> a pro běžecké závody do kategorie <a href="/beh/">běh, triatlon a atletika</a>.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na Sportece porovnáte nabídky více českých obchodů, vyfiltrujete značku a otevřete detail produktu s popisem. U hrotů porovnejte tabulky velikostí, u oštěpů a koulí ověřte hmotnost a určení pro kategorii a věk. Pro sady a hromadné objednávky pro oddíly sledujte balení po několika kusech.</p>',
    faq=[
        ('Jaké atletické hroty vybrat pro začátečníka?', 'Víceúčelové nebo dětské hroty s měkčí podrážkou a kratšími trny. Špičkové sprinterské modely jsou tuhé a vyžadují techniku a zesílené lýtkové svaly.'),
        ('Mohu v hrotech běhat po asfaltu?', 'Nedoporučuje se. Kovové trny jsou určeny pro umělý povrch dráhy, na asfaltu se rychle opotřebují a ztrácejí přilnavost. Pro silnici zvolte běžeckou obuv.'),
        ('Jakou hmotnost oštěpu zvolit pro děti?', 'Pro děti se používají pěnové nebo plastové oštěpy, které jsou lehčí než závodní. Konkrétní hmotnost určuje věk a pravidla soutěže, proto se poraďte s trenérem.'),
        ('K čemu je kriketový míček?', 'Používá se pro hod míčkem v atletické přípravce a ve školách. Je pevný a snadno se drží, hodí se na nácvik pohybu ramene a odhadu vzdálenosti.'),
        ('Jak nastavit startovací bloky?', 'Vzdálenost opěrek se nastavuje podle délky nohou a stylu startu. Přední opěrka bývá blíž ke startovní čáře, zadní o něco dál. Nejlépe s trenérem, který posoudí postavení.'),
        ('Je atletická překážka bezpečná pro děti?', 'Dětské překážky bývají lehké a měkké nebo se při nárazu převrací. Při tréninku je důležité, aby děti začínaly z nízké výšky a pod dohledem dospělého.'),
        ('Jaká obuv se hodí na atletiku ve škole?', 'Pro tělocvik a běžný trénink stačí lehká sportovní nebo běžecká obuv s pevným uchycením nohy. Hroty jsou určeny pro dráhu a oddílový trénink.'),
        ('Jak často vyměňovat trny v hrotech?', 'Podle opotřebení. Pokud jsou zaoblené nebo zkrácené, vyměňte je. Trny se šroubují klíčem a mají se utáhnout, ale ne násilím, aby nepoškodily závit.'),
        ('Jak skladovat atletické náčiní?', 'Na suchém místě mimo přímé slunce. Oštěpy ukládejte ve svislé nebo vodorovné poloze, koule v pevné bedně a překážky stohujte tak, aby se nedeformovaly.'),
        ('Pomůže mi atletika při jiných sportech?', 'Ano, základy běhu, skoku a hodu rozvíjejí rychlost, koordinaci a sílu, kterou využijete v míčových i individuálních sportech. Proto atletiku zařazují mnohé kluby jako přípravu.'),
    ],
)

# ---- additions: silnicni-cyklohelmy
NEW['silnicni-cyklohelmy']['guide'] += (
    '<h2>Sezóna a podmínky jízdy</h2>'
    '<p>V létě rozhodují větrací kanály, světlé barvy a odnímatelné vložky, které se po ježdění v horku dají vyprat. Na jaře a na podzim občas zaprší, a proto se hodí helma s popruhy z rychleschnoucího materiálu a s vložkami, které nenasáknou. V zimě se přilba obvykle nosí s tenkou čepicí a tvar helmy se při výběru porovnává i s ní. Při jízdě za soumraku zvyšují viditelnost reflexní prvky a světlé barvy, které vynikají mezi stromy i na silnici.</p>'
    '<h2>Nastavení popruhů krok za krokem</h2>'
    '<ol><li>Nasaďte helmu na hlavu a zajistěte, aby okraj ležel dva prsty nad obočím.</li>'
    '<li>Upravte rozdělovače popruhů tak, aby tvořily V přímo pod ušním lalůčkem.</li>'
    '<li>Zapněte přezku a zkraťte popruh, aby se pod bradou vešel prst nebo dva.</li>'
    '<li>Utáhněte kolečko vzadu, dokud helma nesedí pevně, ale bez bolesti.</li>'
    '<li>Zatřeste hlavou a zkontrolujte, zda se helma nepřesouvá dopředu ani dozadu.</li></ol>'
    '<p>Kontrolu opakujte po každé změně účesu nebo čepice. Většina špatně sedících helem není vadná, jen nemá správně seřízené popruhy.</p>'
    '<h2>Jak poznáte kvalitní zpracování</h2>'
    '<p>Při prohlídce v ruce zkontrolujte, zda vnější skořepina přesahuje přes okraje pěny a chrání ji proti odření. Švy popruhů mají být pevné a konce zajištěné, přezka cvakne bez vůle a nastavení kolečka se nehýbe samo. Vnitřní pěna nemá mít trhliny a všechny vložky mají sedět na svých místech. Zadní část by měla pokrýt týl a dovolit pohodlný předklon, aniž se opře o límec dresu nebo o batoh.</p>'
)

# ---- additions: atletika
NEW['atletika']['intro'] = (
    '<p>Atletika zahrnuje běh, skoky a vrhy a každá disciplína má vlastní vybavení. V kategorii najdete atletické hroty, oštěpy včetně pěnových, koule, kriketové míčky, překážky, startovací bloky, značky a oblečení pro trénink i závody. Sporteka porovnává nabídky českých obchodů a pomáhá vybrat vhodnou výbavu pro děti, školy, kluby i dospělé sportovce, od prvních pokusů v přípravce po výkonnostní trénink na dráze. Nabídka obsahuje jak závodní, tak pomocné a tréninkové kusy.</p>'
    + NEW['atletika']['intro'].split('</p>', 1)[1])
NEW['atletika']['guide'] += (
    '<h2>Jak vybrat podle věku a úrovně</h2>'
    '<p>Pro nejmenší je důležitější radost z pohybu než specializovaná technika, proto se u nich uplatní měkké pomůcky a hravé soutěže. Mladší žáci už zkouší jednotlivé disciplíny a potřebují lehčí náčiní odpovídající jejich síle. Dorost a dospělí se specializují, a tak si pořizují vlastní hroty, osobní náčiní a technické oblečení. Vybavení má růst s dítětem postupně, bez zbytečných výdajů na model, který ho nebude bavit.</p>'
    '<h2>Bezpečnost na tréninku</h2>'
    '<ul><li>Před každým tréninkem zkontrolujte trny hrotů, upevnění bloků a stav překážek.</li>'
    '<li>Při hodech i vrzích koulí vymezte sektor a nikdy nestůjte před házejícím.</li>'
    '<li>Zahřejte se, zvláště před sprintem a skoky, aby se předešlo natažení svalů.</li>'
    '<li>Používejte náčiní určené pro danou kategorii a věk a nepřeceňujte síly dítěte.</li>'
    '<li>Na mokré dráze zpomalte, trny přilnou, ale svaly reagují hůř v chladu.</li></ul>'
    '<h2>Doplňky pro dlouhé tréninky</h2>'
    '<p>Na delší bloky se hodí <a href="/lahve-a-termosky/">láhev na pití</a> a <a href="/iontove-napoje/">iontový nápoj</a>, v hale i venku pak <a href="/sportovni-tasky/">sportovní taška</a> na hroty, ponožky a náhradní oblečení. Hodinky s měřením času pomůžou sledovat výkonnost, přehled najdete v kategorii <a href="/sportovni-hodinky/">sportovní hodinky</a>. Nezapomeňte na regeneraci a protažení po tréninku.</p>'
)

# ------------------------------------------------------------------ perove-spacaky
NEW['perove-spacaky'] = dict(long=True,
    title='Péřové spacáky: teplota, plnění, mumie, péče o péří',
    desc='Péřové spacáky a spací pytle: jak vybrat komfortní teplotu, nadouvání, tvar a velikost. Péče o péří a porovnání nabídek českých obchodů.',
    intro='<p>Péřový spacák nabízí nejlepší poměr tepla, hmotnosti a objemu po sbalení, proto ho volí trekaři, horolezci a bikepackeři, kteří všechno nesou na zádech. Jemné pírko zachytává vzduch a vytváří izolační vrstvu, která při stejném teple váží méně než syntetika. Sporteka porovnává péřové spacáky z českých obchodů a pomáhá zvolit teplotní třídu, tvar, velikost a péči, která prodlouží životnost na mnoho let.</p>'
          '<p>V nabídce převažují značky ' + B(('sir-joseph', 'Sir Joseph'), ('ferrino', 'Ferrino'), ('warmpeace', 'Warmpeace'), ('patizon', 'Patizon'), ('hannah', 'Hannah'), ('sea-to-summit', 'Sea to Summit'), ('husky', 'Husky'), ('deuter', 'Deuter')) +
          '. Obecný přehled je v kategorii <a href="/spaci-pytle/">spací pytle</a>, pod spacák se hodí <a href="/karimatky-a-matrace/">karimatka nebo matrace</a>.</p>',
    guide='<h2>Proč péří a kdy ho zvolit</h2>'
          '<p>Péří je přírodní izolant, který se po stlačení rychle vrací do původního objemu. Spacák z péří je při stejné teplotní třídě lehčí a po sbalení menší než syntetický, což se projeví hlavně na vícedenním treku. Naopak vlhkost péří oslabuje: slepené chomáče izolují hůř a schnou pomalu. Péřový spacák se proto hodí do suchého a chladného prostředí a tam, kde nosíte všechno sami.</p>'
          + T(['Výplň', 'Silné stránky', 'Slabé stránky'], [
              ['Péří', 'nízká hmotnost, malý sbalený objem, dlouhá životnost', 'citlivé na vlhko, pomalejší schnutí, náročnější péče'],
              ['Syntetika', 'izoluje i vlhká, snadno se pere', 'těžší a objemnější'],
              ['Peří s příměsí syntetiky', 'kompromis mezi cenou a odolností proti vlhku', 'hmotnost se pohybuje mezi oběma extrémy']]) +
          '<p>Pokud kempujete v autě nebo na chatě, stačí vám <a href="/dekove-spacaky/">dekový spacák</a>. Pro děti je praktičtější <a href="/detske-spacaky/">dětský model</a>, který se lépe pere a lépe odpouští vlhko.</p>'
          '<h2>Jak číst teplotní údaje</h2>'
          '<p>Seriózní výrobci uvádějí údaje podle testovací normy pro spací pytle, kterou je evropská EN 13537, od roku 2022 nahrazovaná mezinárodní ISO 23537. Zjistíte z ní tři hodnoty, které se pro spacák uvádějí.</p>'
          '<ul><li><strong>Komfortní teplota:</strong> při ní se vyspí průměrná žena ve volné poloze bez prochladnutí.</li>'
          '<li><strong>Limitní teplota:</strong> při ní se vyspí průměrný muž stočený do klubíčka.</li>'
          '<li><strong>Extrémní teplota:</strong> hranice, při které hrozí prochladnutí. Nikdy se s ní neplánuje.</li></ul>'
          '<p>Pokud výrobce uvádí jen jedno číslo bez metody, bývá optimistické. Spacák vybírejte podle komfortní teploty a nechte si rezervu. Na zimní túru zvolte spacák s komfortní teplotou o několik stupňů nižší, než jaká se očekává, protože pocit tepla ovlivní únava, hlad a vlhkost.</p>'
          + T(['Sezóna', 'Komfortní teplota', 'Typ použití'], [
              ['Léto', 'zhruba 10 °C a více', 'nížiny, chaty, lehký bikepacking'],
              ['Třísezónní', 'zhruba 0 až 5 °C', 'jaro, podzim, hory v létě'],
              ['Zima', 'okolo −5 °C a níže', 'zimní túry, nízké hory'],
              ['Expedice', 'výrazně pod −10 °C', 'vysoké hory, polární oblasti']]) +
          '<h2>Nadouvání, hmotnost výplně a konstrukce</h2>'
          '<p>Kvalita peří se vyjadřuje nadouváním, které se uvádí v kubických palcích. Vyšší hodnota znamená, že stejné množství peří vytvoří větší izolační objem a spacák vyjde při stejném teple lehčí. Dalším údajem je poměr prachového peří a obyčejných pírek. Čím více prachu, tím měkčí a teplejší je výplň, ale tím vyšší nároky má na ošetření.</p>'
          '<h3>Komorové konstrukce</h3>'
          '<p>Výplň se rozděluje do komor, aby se peří neshlukovalo na jednom místě. Přepážky mohou být sešité, nebo se používá konstrukce s kosými přepážkami, které omezují studené mosty. Dvouvrstvé uspořádání se u zimních modelů přidává pro eliminaci míst, kde by se švy dotýkaly vnější látky.</p>'
          '<h3>Tvar a doplňky</h3>'
          '<ul><li><strong>Kapuce:</strong> stažitelná kapuce zadrží teplo u hlavy, odkud uniká nejvíc.</li>'
          '<li><strong>Zimní límec:</strong> měkká rolka kolem ramen brání úniku teplého vzduchu.</li>'
          '<li><strong>Zip s lištou:</strong> překrytí zipu zabraňuje prosvítání chladu a zachytávání látky.</li>'
          '<li><strong>Nožní prostor:</strong> tvarovaný prostor pro chodidla zajišťuje pohodlí a teplo.</li>'
          '<li><strong>Obal a kompresní pytel:</strong> přepravní sáček malé velikosti usnadní balení do batohu.</li></ul>'
          '<h2>Tvar, velikost a strana zipu</h2>'
          '<p>Mumie přiléhá k tělu a nejlépe udrží teplo, protože zbytečně nehřeje volný vzduch. Poloviční mumie nabízí o něco víc prostoru pro ramena. Prostornější tvar se hodí pro ty, kdo spí neklidně. Délka se uvádí pro tělo určité výšky; příliš dlouhý spacák vyplní studený vzduch, příliš krátký tlačí na peří a izolace slábne.</p>'
          '<ul><li><strong>Dámský střih:</strong> bývá kratší a v oblasti kyčlí a chodidel teplejší, protože ženy v průměru častěji mrznou.</li>'
          '<li><strong>Pánský střih:</strong> širší v ramenou a delší.</li>'
          '<li><strong>Levý nebo pravý zip:</strong> pokud chcete dva spacáky spojit, musí se zipy hodit k sobě.</li></ul>'
          '<h2>Spacák, karimatka a stan jako jeden systém</h2>'
          '<p>Péří pod tělem se stlačí a izolace od země nefunguje. O teplo pod zády se proto stará <a href="/karimatky-a-matrace/">karimatka nebo matrace</a> s dostatečnou tepelnou odolností. Do chladu přidejte <a href="/vlozky-do-spacaku/">vložku do spacáku</a>, která přidá několik stupňů a chrání spacák před potem. Samotný pytel se uplatní pod střechou <a href="/stany/">stanu</a> nebo <a href="/turisticke-stany/">turistického stanu</a>; v zimě se k tomu hodí i <a href="/expedicni-stany/">expediční stany</a>.</p>'
          '<h2>Péče o péřový spacák</h2>'
          '<ul><li><strong>Skladování:</strong> volně, v prostorném bavlněném pytli nebo zavěšený. Dlouhé stlačení poškozuje strukturu peří.</li>'
          '<li><strong>Větrání:</strong> po noci spacák rozložte, aby vyschl z potu.</li>'
          '<li><strong>Praní:</strong> jen speciálním přípravkem na péří, v bubnu s dostatkem prostoru a při nízké teplotě. Pere se výjimečně, aby péří neztratilo přirozené tuky.</li>'
          '<li><strong>Sušení:</strong> pomalu a opatrně, s pomocí čistých tenisových míčků nebo sušicích kuliček. Nesmí zůstat žádné vlhké místo.</li>'
          '<li><strong>Ochrana:</strong> v mokru pomáhá nepromokavý obal nebo vodotěsný vak uvnitř batohu.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Orientovat se podle limitní nebo extrémní teploty místo komfortní.</li>'
          '<li>Koupit příliš velký spacák, který se hůř vyhřeje.</li>'
          '<li>Spát na tenké podložce a divit se, že spacák nehřeje zespodu.</li>'
          '<li>Skladovat péřový spacák stlačený v obalu celé léto.</li>'
          '<li>Neověřit, zda kapuce a límec opravdu sedí k tělu.</li></ul>'
          '<h2>Pro koho je péřový spacák</h2>'
          '<p>Hodí se pro trekaře, kteří nesou výbavu na delší vzdálenost a počítají gramy, pro horolezce a skialpinisty, kteří spí na horských chatách i ve stanech, i pro bikepackery s omezeným místem na kole. Příležitostným kempařům, rodinám s dětmi a lidem, kteří často spí ve vlhku, stačí syntetika. Pro chladné měsíce se vyplatí zvážit i <a href="/termopradlo/">termoprádlo</a> a <a href="/cepice-a-celenky/">čepici na spaní</a>.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na Sportece vidíte nabídky více obchodů u jednoho spacáku. U každého si ověřte teplotní údaje, délku, tvar a stranu zipu. Pokud vybíráte pár spacáků, sledujte, zda se zipy hodí k sobě. Při srovnání rozlišujte spacáky určené pro léto a zimu a nenechte se zmást vzhledem, který o teple nevypovídá.</p>'
          '<h2>Spacák na cesty a do hor</h2>'
          '<p>Na vícedenní treky v horách zvolte třísezónní model s rezervou, protože počasí se mění rychleji než předpověď. Pro zimní túry dává smysl zimní spacák s límcem a kapucí. Při cestě letadlem počítejte s tím, že komprimovaný spacák zabere málo místa, ale po rozbalení potřebuje čas, aby se péří nadýchalo. Na noc ve vyhřáté chatě stačí lehký letní model nebo vložka.</p>',
    faq=[
        ('Jak vybrat správnou teplotu péřového spacáku?', 'Řiďte se komfortní teplotou, ne extrémní. Vybírejte model o několik stupňů teplejší, než jaká bude nejnižší teplota na výletě, protože pocit tepla ovlivní únava a vlhkost.'),
        ('Co znamená nadouvání péří?', 'Je to míra, jak velký objem zaujme jedna unce peří po nadýchání, a udává se v kubických palcích. Vyšší číslo znamená lepší izolaci při stejné hmotnosti a menší sbalený objem.'),
        ('Je péřový spacák vhodný do vlhka?', 'Hůř než syntetický. Mokré péří ztrácí izolaci a pomalu schne. Pomůže nepromokavý obal, ošetřené hydrofobní péří a péče o sušení.'),
        ('Jak často prát péřový spacák?', 'Co nejméně. Stačí ho pravidelně větrat a občas vyprat speciálním prostředkem na péří, aby se zachovaly přirozené tuky a izolace.'),
        ('Jak skladovat spacák přes léto?', 'Volně, v prostorném bavlněném pytli nebo zavěšený v suché místnosti. Nestlačujte ho v kompresním obalu, protože se péří při dlouhém stlačení lámou.'),
        ('Potřebuji k péřovému spacáku vložku?', 'Není to nutné, ale vložka přidá několik stupňů, chrání spacák před potem a snadno se pere. Hodí se do chladu i při cestování po ubytovnách.'),
        ('Jaký tvar zvolit, mumie, nebo prostornější?', 'Mumie nejlépe drží teplo a vyniká na treku. Prostornější tvar vyhovuje lidem, kteří spí neklidně nebo potřebují víc místa pro nohy.'),
        ('Jaký je rozdíl mezi dámským a pánským spacákem?', 'Dámský bývá kratší, užší v ramenou a více izolovaný v oblasti nohou a boků. Pánský je delší a širší. Důležité je, aby spacák seděl k vaší postavě.'),
        ('Jak se péřový spacák suší?', 'Pomalu, při nízké teplotě a s opatrným protřepáváním. V sušičce pomáhají čisté tenisové míčky, které rozbijí chomáče peří. Spacák musí být úplně suchý, než ho uložíte.'),
        ('Mohu péřový spacák používat v zimě?', 'Ano, pokud má dostatečnou teplotní třídu a spíte na izolační podložce. Do silného mrazu zvolte zimní model s límcem a kapucí.'),
    ],
)

# ------------------------------------------------------------------ ebike-baterie
NEW['ebike-baterie'] = dict(long=True,
    title='Baterie, motory a nabíječky pro e-kola a koloběžky',
    desc='Baterie, nabíječky, kryty motorů a díly pro elektrokola a elektrokoloběžky. Jak vybrat kapacitu, napětí a bezpečně nabíjet. Porovnání obchodů.',
    intro='<p>Kategorie sdružuje baterie, nabíječky, kryty motorů, držáky a další díly pro elektrokola, elektrokoloběžky a skútry. Elektrická výbava není univerzální, takže se vybírá podle výrobce a typu pohonu, nikoli podle vzhledu. Sporteka porovnává nabídky českých obchodů a pomáhá zorientovat se v napětí, kapacitě, konektorech a bezpečném nabíjení.</p>'
          '<p>V nabídce najdete značky ' + B(('bosch', 'Bosch'), ('specialized', 'Specialized'), ('racceway', 'Racceway'), ('joyor', 'Joyor'), ('bluetouch', 'Bluetouch'), ('city-boss', 'City Boss'), ('todimart', 'Todimart'), ('kukirin', 'Kukirin')) +
          '. Pro kompletní stroj se podívejte do <a href="/elektrokola/">elektrokol</a> nebo <a href="/elektrokolobezky/">elektrokoloběžek</a>, běžné součástky najdete v kategorii <a href="/cyklo-dily/">díly a pláště</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Nabídka je smíšená, a proto před koupí zkontrolujte popis. Kromě náhradních baterií se tu objevují nabíječky, přídavné baterie pro prodloužení dojezdu, neoprenové obaly, kryty motorů a držáky. Mezi výsledky bývají i hotové elektrokoloběžky a baterie ke skútrům. Naopak nemusí jít o součást kola, například u akumulátorových sekaček se základní baterie podobá, ale není kompatibilní.</p>'
          + T(['Položka', 'K čemu slouží', 'Na co se dívat'], [
              ['Baterie pro e-kolo', 'napájí motor a displej', 'napětí, kapacita Wh, konektor a držák'],
              ['Přídavná baterie', 'zvyšuje dojezd', 'kompatibilita se systémem a upevnění'],
              ['Nabíječka', 'dobíjí baterii', 'napětí, proud, typ konektoru, certifikace'],
              ['Kryt motoru', 'chrání motor a zadní část rámu', 'model motoru a rámu'],
              ['Obal na baterii', 'chrání před chladem a špínou', 'rozměr baterie'],
              ['Baterie ke skútru a koloběžce', 'napájí elektrické vozidlo', 'napětí, kapacita Ah, technologie článků']]) +
          '<h2>Napětí, kapacita a výpočet energie</h2>'
          '<p>Energie baterie se udává ve watthodinách (Wh) a spočítá se jako napětí ve voltech krát kapacita v ampérhodinách. Například baterie 36 V s kapacitou 10 Ah má 360 Wh. Vyšší hodnota znamená větší dojezd, ale také vyšší hmotnost. U elektrokol se údaj Wh uvádí přímo, u koloběžek se častěji píše volty a Ah, takže si ho snadno přepočítáte.</p>'
          '<ul><li><strong>Napětí:</strong> musí odpovídat systému kola. Baterii s jiným napětím nelze použít.</li>'
          '<li><strong>Kapacita:</strong> ovlivňuje dojezd, který se mění podle terénu, váhy jezdce, větru a úrovně asistence.</li>'
          '<li><strong>Typ článků:</strong> lithium-iontové baterie jsou standard; olověné se používají u levnějších strojů a jsou těžší.</li>'
          '<li><strong>Rozhraní a komunikace:</strong> chytré baterie komunikují s motorem a displejem a bývají vázané na výrobce.</li></ul>'
          '<h2>Jak vybrat správnou baterii</h2>'
          '<p>Nejdůležitější je kompatibilita. Baterie musí mít stejný systém, konektor a držák jako původní. U značkových pohonů hledejte přesný model, často je uveden v typovém štítku. Zkontrolujte, zda je baterie určena pro rám, nebo pro nosič, a zda se hodí do držáku.</p>'
          '<h3>Postup výběru</h3>'
          '<ol><li>Zjistěte označení pohonu, například značku motoru a model baterie.</li>'
          '<li>Porovnejte napětí a rozměry se stávající baterií.</li>'
          '<li>Zvolte kapacitu podle délky tras, které jezdíte.</li>'
          '<li>Ověřte, zda je zahrnut držák, klíč a nabíječka.</li>'
          '<li>Prověřte záruku a dostupnost servisu.</li></ol>'
          '<p>Pokud kolo ještě nemáte, projděte si <a href="/horska-elektrokola/">horská elektrokola</a>, <a href="/trekingova-elektrokola/">trekingová elektrokola</a>, <a href="/mestska-elektrokola/">městská elektrokola</a> nebo <a href="/skladaci-elektrokola/">skládací elektrokola</a>. Pro terén a zimu jsou k dispozici <a href="/fatbike-elektrokola/">fatbike elektrokola</a>.</p>'
          '<h2>Nabíječky a bezpečné nabíjení</h2>'
          '<p>Nabíječka musí odpovídat napětí a typu baterie. Použití jiné nabíječky než určené výrobcem je rizikové: baterie se může přebít, přehřát nebo poškodit. Ověřte i konektor a polaritu a nabíječku nekupujte bez označení výrobce.</p>'
          '<ul><li>Nabíjejte na rovném, suchém a nehořlavém povrchu mimo dosah dětí.</li>'
          '<li>Nenechávejte baterii nabíjet bez dohledu přes noc, zvlášť pokud je levná nebo poškozená.</li>'
          '<li>Baterii nenabíjejte těsně po jízdě; nechte ji vychladnout.</li>'
          '<li>Při zimním nabíjení baterii nejprve vyhřejte na pokojovou teplotu.</li>'
          '<li>Poškozená baterie, nafouklá nebo cítící chemii, patří do sběrného místa, ne do popelnice.</li></ul>'
          '<h2>Péče o baterii a životnost</h2>'
          '<p>Lithium-iontová baterie ztrácí kapacitu s počtem cyklů a s časem. Zpomalit stárnutí pomáhá střídmé používání a správné skladování. Nevybíjejte ji do nuly a nenechávejte dlouho plně nabitou. Při odstavení na zimu ji uložte přibližně do poloviny kapacity na suchém, chladném místě a občas ji zkontrolujte.</p>'
          '<ul><li><strong>Teplota:</strong> mráz snižuje dojezd, horko urychluje stárnutí. Neponechávejte baterii v autě na slunci.</li>'
          '<li><strong>Voda:</strong> baterie je odolná proti dešti, ale ne proti ponoření. Nemyjte ji tlakovou vodou.</li>'
          '<li><strong>Kontakty:</strong> čistěte suchým hadříkem a sledujte, zda nejsou zoxidované.</li>'
          '<li><strong>Převoz:</strong> baterii vyndejte při dopravě na nosiči a chraňte před nárazy.</li></ul>'
          '<h2>Kryty motorů, držáky a doplňky</h2>'
          '<p>Kryty motorů chrání mechanickou část před nárazy kamenů a otěrem. Při nákupu zkontrolujte model motoru a stranu, protože levý a pravý kryt se liší, a pro některé rámy bývá potřeba i spodní kryt. Držák baterie musí sedět na rámu a zajišťovat dobrý kontakt. Pro studené měsíce se hodí neoprenový obal, který baterii izoluje a chrání před špínou. K bezpečné jízdě patří <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zamky/">zámky</a> a <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>, které unesou vyšší hmotnost elektrokola.</p>'
          '<h2>Elektrokoloběžky a skútry</h2>'
          '<p>V kategorii je i řada baterií a nabíječek pro elektrokoloběžky a elektrické skútry. U nich se baterie liší typem článků, kapacitou a konektorem, často bývá konkrétní pro model. Před nákupem zkontrolujte napětí, kapacitu v Ah a typ připojení. Širší nabídku strojů nabízí kategorie <a href="/kolobezky/">koloběžky</a> a <a href="/elektrokolobezky/">elektrokoloběžky</a>. Pro mobilní nabíjení drobné elektroniky se hodí <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a>, ale na pohonnou baterii je nepoužívejte.</p>'
          '<h2>Servis a údržba</h2>'
          '<p>Pohon elektrokola je složitý systém. Chyby displeje, prudký pokles dojezdu nebo vypínání motoru nemusí znamenat vadnou baterii. Může jít o konektor, snímač nebo software. Před výměnou nechte stav prověřit v servisu. Pravidelná údržba kola, včetně <a href="/cyklo-pohon/">pohonu</a> a <a href="/cyklo-brzdy/">brzd</a>, snižuje zatížení motoru a zvyšuje bezpečnost. Přehled prostředků na péči najdete v kategorii <a href="/cyklo-udrzba/">údržba kol</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupit baterii podle vzhledu bez ověření napětí a konektoru.</li>'
          '<li>Používat nabíječku jiné značky bez ověření parametrů.</li>'
          '<li>Skladovat baterii vybitou celou zimu.</li>'
          '<li>Odstranit kryt motoru a jezdit bez ochrany.</li>'
          '<li>Spoléhat na dojezd uvedený výrobcem v ideálních podmínkách.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na Sportece porovnáte nabídky více obchodů a ověříte dostupnost. U každého výrobku čtěte popis kompatibility a stav záruky. Pro hledání použijte název modelu motoru nebo kola, protože univerzální baterie neexistují.</p>',
    faq=[
        ('Jak poznám, jaká baterie se hodí na moje e-kolo?', 'Podívejte se na typový štítek baterie a motoru a porovnejte označení, napětí a konektor. Baterie od jiného systému zpravidla nefunguje, i když vypadá podobně.'),
        ('Co znamená Wh u baterie?', 'Jsou to watthodiny, tedy energie uložená v baterii. Vypočítají se jako napětí krát kapacita v ampérhodinách. Vyšší číslo znamená větší dojezd.'),
        ('Mohu použít jinou nabíječku?', 'Ne bez ověření. Nabíječka musí mít správné napětí, proud, konektor a polaritu, jinak hrozí poškození baterie nebo požár. Nejbezpečnější je originální nebo doporučená nabíječka.'),
        ('Jak dlouho baterie vydrží?', 'Záleží na kvalitě článků, počtu cyklů, teplotě a způsobu používání. Správné skladování a střídmé nabíjení životnost prodlužuje, ale kapacita postupně klesá.'),
        ('Jak skladovat baterii přes zimu?', 'Na suchém a chladném místě při asi poloviční kapacitě. Nenechávejte ji úplně vybitou ani plně nabitou a jednou za pár týdnů zkontrolujte stav.'),
        ('Je přídavná baterie vhodná pro každé kolo?', 'Ne, musí být kompatibilní se systémem pohonu a mít způsob upevnění. Některé přídavné baterie se připojují k hlavnímu systému, jiné jen doplňují dojezd.'),
        ('Mohu baterii nabíjet přes noc?', 'Nedoporučuje se bez dohledu, zvláště u levnějších nebo starších baterií. Nabíjejte na bezpečném povrchu a po ukončení nabíjení nabíječku odpojte.'),
        ('Jak vyčistit baterii a kontakty?', 'Suchým nebo mírně vlhkým hadříkem. Nepoužívejte tlakovou vodu a nenechávejte kontakty vlhké. Zoxidované kontakty prověří servis.'),
        ('Proč se v kategorii objevují i koloběžky?', 'Protože se v nich používají podobné baterie a nabíječky a obchody je zařazují společně. Kategorie je smíšená, proto se vždy řiďte popisem konkrétního produktu.'),
        ('Co dělat s poškozenou baterií?', 'Přestaňte ji používat a nabíjet. Nafouklá, horká nebo zapáchající baterie je nebezpečná a patří do sběrného místa pro elektroodpad, ne do běžného odpadu.'),
    ],
)

# ---- additions round 2
NEW['atletika']['guide'] += (
    '<p>Při výběru začněte disciplínou, kterou dítě nebo sportovec skutečně provozuje, a teprve pak řešte značku. Pomůže i konzultace s trenérem oddílu, který ví, jaké náčiní se na tréninku používá a jaké vybavení klub už má.</p>')

NEW['perove-spacaky']['guide'] += (
    '<h2>Hmotnost, sbalení a transport</h2>'
    '<p>Péřový spacák se na treku nese v kompresním vaku nebo v nepromokavém obalu na dně batohu. Čím je výplň kvalitnější, tím menší a lehčí balení vznikne, ale stlačený spacák se po rozbalení nejlépe nadýchá, pokud ho chvíli protřepete. Do batohu ho neutahujte násilím a nenoste ho v cestovní tašce přes celé léto. Hmotnost spacáku se vyplatí porovnat s ostatním vybavením, například s <a href="/turisticke-batohy/">turistickým batohem</a>, protože úspora gramů na jedné věci se může rozplynout u jiné.</p>'
    '<h2>Hygiena a pocení</h2>'
    '<p>Spacák se při spaní zahřívá a vyplňuje se potem a vlhkostí z těla. Proto se vyplatí spát v čistém spodním prádle nebo v <a href="/merino/">merino</a> vrstvě, která pot odvádí. Tělesné oleje a prach snižují schopnost peří zadržet vzduch, a tak vložka nebo tenká spodní vrstva prodlouží životnost spacáku. Po každé výpravě spacák vyvětrejte a před uložením zkontrolujte švy a zip.</p>'
    '<h2>Co dělat při promoknutí</h2>'
    '<p>Pokud se spacák namočí, nejdříve z něj jemně vytlačte vodu bez kroucení a ždímání a rozložte na suchém větraném místě. Peří suší jen pomalu, a tak ho občas protřepte, aby se chomáče rozpadly. Při potřebě rychle vysušit spacák na treku se hodí slunce a vítr, ne přímý oheň. Do mokrého prostředí si vezměte <a href="/hamaky/">hamak</a> s podložkou nebo <a href="/karimatky-a-matrace/">matraci</a>, která drží mimo vlhkou zem.</p>')

NEW['ebike-baterie']['intro'] = (
    '<p>Kategorie sdružuje baterie, nabíječky, kryty motorů, držáky a další díly pro elektrokola, elektrokoloběžky a skútry. Elektrická výbava není univerzální, takže se vybírá podle výrobce a typu pohonu, nikoli podle vzhledu. Sporteka porovnává nabídky českých obchodů a pomáhá zorientovat se v napětí, kapacitě, konektorech a bezpečném nabíjení, ale také v tom, co v tak smíšené kategorii skutečně najdete.</p>'
    + NEW['ebike-baterie']['intro'].split('</p>', 1)[1])
NEW['ebike-baterie']['guide'] += (
    '<h2>Dojezd a co ho ovlivňuje</h2>'
    '<p>Dojezd uváděný výrobcem vychází z ideálních podmínek, tedy z rovného povrchu, mírné rychlosti a nízké hmotnosti jezdce. Ve skutečnosti ho zkracuje kopcovitý terén, protivítr, nízká teplota, vyšší úroveň asistence, nahuštěné měkké pláště a časté rozjezdy ve městě. Nižší tlak v pláštích a špatně namazaný řetěz zvyšují odpor a baterie se vybíjí rychleji. Hospodárnější jízdu podpoří správně nahuštěné <a href="/plaste-a-duse/">pláště a duše</a> a pravidelné mazání pohonu.</p>'
    '<ul><li><strong>Nižší stupeň asistence:</strong> v rovině a z kopce snižte podporu, ušetříte energii.</li>'
    '<li><strong>Řazení:</strong> motor pracuje efektivněji při plynulém šlapání ve vhodném převodu.</li>'
    '<li><strong>Hmotnost nákladu:</strong> zavazadla a děti na nosiči zkracují dojezd.</li>'
    '<li><strong>Teplota:</strong> v zimě baterii před jízdou ponechte v teple a nasaďte ji těsně před odjezdem.</li></ul>'
    '<h2>Kdy baterii vyměnit</h2>'
    '<p>Známkou opotřebení je výrazný pokles dojezdu při stejné jízdě, náhlé vypnutí podpory při zátěži nebo rychlé zahřívání při nabíjení. Před koupí nové baterie vždy ověřte, zda problém nezpůsobuje nabíječka, konektor nebo nastavení. Opotřebovanou baterii můžete odevzdat k recyklaci a mnohé obchody ji převezmou. Po výměně si ověřte, že držák a zámek baterie drží pevně a nic nechrastí.</p>'
    '<h2>Doplňkové vybavení pro elektrokolo</h2>'
    '<p>Elektrokolo je těžší než běžné kolo, proto se vyplatí kvalitní brzdy, odolné pláště a pevný zámek. Pro delší výlety se hodí rezervní baterie nebo plánování tras s možností dobití. Výbavu doplňte o helmu a zdroj světla, aby jízda byla bezpečná. Při přepravě kola na auto používejte <a href="/cyklo-nosice-na-auto/">nosiče na auto</a> určené pro vyšší hmotnost a baterii vždy sundejte.</p>'
    '<h2>Pro koho je která volba</h2>'
    + T(['Uživatel', 'Typické potřeby', 'Doporučení'], [
        ['Dojíždějící do práce', 'pravidelné krátké trasy, nabíjení doma nebo v práci', 'baterie střední kapacity, spolehlivá nabíječka'],
        ['Turista a cyklista na víkend', 'delší trasy, kopce', 'vyšší kapacita, případně přídavná baterie'],
        ['Jezdec v terénu', 'náročné stoupání, nárazy', 'chráněná baterie a pevné kryty motoru'],
        ['Majitel koloběžky nebo skútru', 'krátké městské trasy', 'baterie přesně podle modelu a nabíječka od výrobce']]))

# ---- additions round 3
NEW['perove-spacaky']['guide'] += (
    '<h2>Péřový spacák pro děti a pro dva</h2>'
    '<p>Děti rychle rostou a spí neklidně, takže pro ně bývá výhodnější levnější syntetický model, který se snadno pere. Starší děti na túrách ale ocení lehký péřový spacák, jehož nesení je menší zátěží. Pro páry existují široké spacáky nebo dva spojitelné pytle se zipy na opačných stranách. Společné spaní hřeje víc, ale vyžaduje dostatečně širokou karimatku, ať se nikdo nepřevaluje na studenou zem.</p>'
    '<p>Při výběru počítejte i s tím, že péřový spacák se obvykle kupuje na dlouhá léta, takže se vyplatí nešetřit na teplotní třídě ani na zpracování zipu.</p>')
NEW['ebike-baterie']['intro'] = NEW['ebike-baterie']['intro'].replace('skutečně najdete.</p>', 'skutečně najdete, a čemu se při nákupu vyhnout.</p>')
NEW['ebike-baterie']['guide'] += (
    '<h2>Prověřený nákup a záruka</h2>'
    '<p>U baterií a nabíječek se vyplatí vybírat obchod s jasnou záruční dobou a možností reklamace. Levné neznačkové kusy z neověřených zdrojů mohou mít nepřesně uvedenou kapacitu nebo slabší ochranné obvody, které hlídají přebití, zkrat a přehřátí. Zkontrolujte, zda popis uvádí napětí, kapacitu, typ článků a rozměry, a dávejte přednost kusům s jasně uvedeným výrobcem a kompatibilními modely. Po doručení baterii prohlédněte, zda není poškozená, a před prvním použitím ji nabijte podle návodu.</p>'
    '<p>Při přepravě a posílání baterie se vztahují zvláštní pravidla pro lithiové zboží, proto se u dopravce předem informujte o podmínkách. Totéž platí pro cestování letadlem, kde se větší baterie do zavazadel nepřijímají.</p>')

# ---- additions round 4
NEW['perove-spacaky']['guide'] += (
    '<p>Spacák si před první nocí venku rozbalte doma. Zjistíte, zda vám sedí délka, zda se dá pohodlně zapnout zip a zda kapuce nesklouzává. Ráno ho nechte rozložený, aby se vlhkost z těla odpařila, a teprve potom ho sbalte do obalu.</p>')
NEW['ebike-baterie']['guide'] += (
    '<p>Před výměnou si vyfotografujte původní zapojení a typový štítek a poznamenejte si sériové číslo baterie. Při reklamaci nebo hledání shodného dílu vám usnadní práci a zkrátí čekání na správnou součástku. Pokud si nejste jistí montáží krytů nebo držáku, svěřte práci servisu.</p>')
