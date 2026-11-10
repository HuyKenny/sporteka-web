"""sporteka.cz — wave 12b (4. 11. 2026): long texts for cyklistika, sportovni-bundy, outdoor, mikiny. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklistika
NEW['cyklistika'] = dict(long=True,
    title='Cyklistika: kola, helmy, oblečení a díly | Sporteka',
    desc='Vše pro cyklisty na jednom místě: kola, helmy, oblečení, díly, světla i zámky. Porovnejte nabídku českých obchodů a vyberte podle stylu jízdy.',
    intro='<p><strong>Cyklistika</strong> je široký obor a výbava se liší podle toho, jestli jezdíte do práce po městě, o víkendu po lesních stezkách, nebo trénujete na silnici. Nejdřív proto stojí za to určit, kolik času na kole skutečně trávíte a po jakém povrchu, a teprve pak vybírat konkrétní kousky. Špatně zvolená velikost rámu nebo nevhodné pláště zkazí radost z jízdy víc než o třídu slabší pohon.</p>'
          '<p>Sporteka sdružuje nabídku českých e-shopů v jedné kategorii: od <a href="/jizdni-kola/">jízdních kol</a> a <a href="/cyklisticke-helmy/">helem</a> přes <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a <a href="/cyklo-dily/">díly a pláště</a> až po <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zamky/">zámky</a> a <a href="/cyklo-pumpy-a-naradi/">nářadí</a>. Průvodce níže vysvětluje, jak jednotlivé části výbavy spolu souvisejí, na co se při nákupu dívat a které chyby se opakují nejčastěji.</p>',
    guide='<h2>Jak si vybrat kolo a výbavu podle stylu jízdy</h2>'
          '<p>Kolo je jen základ. K bezpečné a pohodlné jízdě patří helma, viditelnost za šera, oblečení do počasí a nářadí na drobné opravy u cesty. Když začnete od stylu jízdy, snadno poznáte, co potřebujete hned a co může počkat.</p>'
          + T(['Styl jízdy', 'Hlavní priorita', 'Typická výbava'], [
              ['Městské dojíždění', 'viditelnost, zámek, praktičnost', 'světla, zámek, blatníky, brašny nebo nosič, helma'],
              ['Rekreační vyjížďky', 'pohodlí a dosah', 'trekingové kolo, rukavice, láhev, pumpa, zadní světlo'],
              ['Terén a stezky', 'odolnost a ochrana', 'horské kolo, MTB helma, chrániče, hrubší plášť, nářadí'],
              ['Silnice a gravel', 'efektivita a váha', 'silniční nebo gravel kolo, dres, kraťasy se vložkou, cyklopočítač'],
              ['Elektrokolo', 'dojezd a bezpečnost', 'e-kolo, kvalitní zámek, helma, nabíječka a baterie'],
              ['Děti', 'bezpečnost a růst', 'dětské kolo nebo odrážedlo, helma, sedačka či vozík pro nejmenší']]) +
          '<h3>Typy kol</h3>'
          '<p>Základní rozdělení je podle terénu. <a href="/horska-kola/">Horská kola</a> mají odpružení nebo robustní rám a široké pláště s hrubým vzorkem. <a href="/silnicni-a-gravel-kola/">Silniční a gravel kola</a> jsou lehčí, mají beraní řídítka a hladší pláště. <a href="/trekingova-kola/">Trekingová a městská kola</a> nabízejí vzpřímenou polohu, blatníky a nosič, takže se hodí na každodenní použití. <a href="/elektrokola/">Elektrokola</a> přidávají motor a baterii, což oceníte v kopcích i při dojíždění v obleku. Pro cestování vlakem a MHD jsou praktická <a href="/skladaci-kola/">skládací kola</a>, pro triky a skatepark slouží <a href="/bmx-a-dirt-kola/">BMX a dirt kola</a> a nejmenší jezdí na <a href="/detska-kola/">dětských kolech a odrážedlech</a>.</p>'
          '<h3>Velikost rámu je důležitější než značka</h3>'
          '<p>Výrobci udávají velikost rámu v palcích, centimetrech nebo ve stylu S až XL. Pro orientaci se používá výška postavy a délka vnitřní strany nohy, ale konkrétní rozměry rámu se liší podle geometrie. Správně nastavené sedlo má při spodní poloze pedálu mírně pokrčenou nohu, řídítka by se měla dosahovat bez křečovitého předklonu. Bolest zad, krku nebo kolen je častěji důsledkem špatné velikosti než slabé kondice. U dětí volte kolo, na kterém dosáhnou na zem alespoň špičkami, a nekupujte ho s příliš velkou rezervou.</p>'
          '<h2>Helma a ochrana</h2>'
          '<p>Helma je nejdůležitější doplněk, který se nevyplatí šetřit. Pro děti i dospělé platí stejné pravidlo: nasazená helma má sedět rovně na čele, popruhy mají tvořit písmeno V pod ušima a pod bradou mají dovolit jen jeden až dva prsty. Po pádu, při kterém helma narazila, ji vyměňte, protože ochranná pěna se mohla poškodit i bez viditelných trhlin. Podle disciplíny existují různé typy: <a href="/silnicni-cyklohelmy/">silniční a gravel helmy</a> jsou lehké a větrané, <a href="/mtb-a-integralni-helmy/">MTB, enduro a integrální helmy</a> mají nižší týl a často kšilt, <a href="/mestske-cyklohelmy/">městské helmy</a> stavějí na stylu a <a href="/detske-cyklohelmy/">dětské cyklohelmy</a> na lehkosti a snadném nastavení.</p>'
          '<p>Při jízdě v terénu přidávají jistotu <a href="/cyklo-chranice/">chrániče pro cyklisty</a>: kolenní, loketní nebo páteřní. Pro každodenní jízdu se jim ale většina lidí vyhne, a tak je dobré mít aspoň <a href="/cyklisticke-rukavice/">rukavice</a>, které chrání dlaně při pádu a tlumí vibrace řídítek. Pro ochranu očí před větrem, hmyzem a prachem slouží <a href="/cyklisticke-bryle/">cyklistické brýle</a>, v nabídce často s výměnnými skly pro slunečný i zatažený den.</p>'
          '<h2>Oblečení do každého počasí</h2>'
          '<p>Cyklistické oblečení je střižené pro polohu na kole: zadní díl dresu je delší, kalhoty mají vložku a rukávy nepřekáží v předklonu. Funkční materiály odvádějí pot a nenasáknou, takže se tělo během jízdy neprochladí. Přehled je v kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>'
          '<ul><li><a href="/cyklisticke-dresy/">Dresy</a> mají kapsy na zádech a zip, který se dá otevřít za jízdy.</li>'
          '<li><a href="/cyklisticke-kratasy-a-kalhoty/">Kraťasy a kalhoty</a> s vložkou omezují otlaky a tření na delších trasách.</li>'
          '<li><a href="/cyklisticke-bundy-a-vesty/">Bundy a vesty</a> chrání před větrem a deštěm a dají se složit do kapsy.</li>'
          '<li><a href="/cyklisticke-navleky/">Návleky a rukávky</a> upraví oblečení při proměnlivém počasí, například ráno chladno a odpoledne teplo.</li>'
          '<li><a href="/cyklisticke-ponozky/">Ponožky</a> bez švů na prstech snižují riziko puchýřů.</li>'
          '<li><a href="/cyklisticka-obuv/">Cyklistické tretry</a> se zapínají do nášlapných pedálů, což zlepšuje přenos síly.</li></ul>'
          '<p>Platí zásada vrstev. Na jaře a na podzim se hodí tenké spodní prádlo, dres a lehká větrovka, v zimě termo vrstva, teplejší bunda a rukavice, které chrání prsty. Ze všeho nejdřív promrzají ruce a špičky nohou, takže se oplatí věnovat jim pozornost.</p>'
          '<h2>Díly, pláště a údržba</h2>'
          '<p>Hlavní kategorie <a href="/cyklo-dily/">díly a pláště</a> je největší část nabídky. Nejčastěji se vyměňují <a href="/plaste-a-duse/">pláště a duše</a>, protože se opotřebovávají jako první. Při výběru plášťů sledujte rozměr uvedený na boku a rozsah tlaku. Hrubý vzorek je do terénu, hladký a užší na silnici, pro město se hodí odolné pláště s ochranou proti defektům.</p>'
          '<p>Pohon tvoří <a href="/cyklo-pohon/">přehazovačky, řetězy, kazety a kliky</a>. Opotřebovaný řetěz brzy zničí i kazetu, takže se vyplatí měnit ho včas. <a href="/cyklo-brzdy/">Brzdy a brzdové destičky</a> jsou bezpečnostní součást, kterou je dobré kontrolovat nejméně před každou sezónou. K pohodlí patří <a href="/sedla-a-gripy/">sedla, gripy a potahy</a> a <a href="/cyklo-riditka/">řídítka, představce a sedlovky</a>. Náročnější jezdci hledají <a href="/cyklo-kola-a-rafky/">zapletená kola, ráfky a náboje</a>, <a href="/cyklo-pedaly/">pedály</a> a <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>. Při jízdě v dešti ocení uživatelé <a href="/cyklo-blatniky/">blatníky</a>, majitelé e-kol zase <a href="/ebike-baterie/">baterie, motory a nabíječky</a>.</p>'
          '<p>Důležitý je kompatibilní standard. Kazeta musí odpovídat počtu rychlostí, osa kola šířce vidlice a brzdový kotouč upevnění náboje. Před objednávkou si proto ověřte parametry svého kola a nespoléhejte jen na podobný vzhled dílu.</p>'
          '<h3>Pravidelná údržba</h3>'
          '<p>Základ je čistý a promazaný řetěz. Po jízdě v bahně ho očistěte, nanesete mazivo a přebytek otřete, jinak se na něj lepí prach. Tlak v pláštích kontrolujte před jízdou, protože při nižším tlaku se zvyšuje riziko defektu. Potřebné pomůcky najdete v kategoriích <a href="/cyklo-udrzba/">údržba kola: mazadla a čističe</a> a <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. S sebou na trasu patří náhradní duše, montážní páčky, malá pumpa a imbusové klíče.</p>'
          '<h2>Bezpečnost, viditelnost a převoz</h2>'
          '<p>Za šera i ve dne je nutné, aby vás řidiči viděli. <a href="/cyklo-svetla/">Světla na kolo</a> se dělí na přední, která svítí na cestu, a zadní, která se hlavně dává vidět. Blikající režim je dobrý pro viditelnost ve městě, pevné světlo se hodí na tmavé cesty. Odrazky na pedálech, paprscích a rámu se tolerují dobře a nestojí vám žádnou baterii.</p>'
          '<p>Kolo, které zůstává bez dozoru, zabezpečí <a href="/cyklo-zamky/">zámek na kolo</a>. Nejlepší je pevný U-zámek nebo kvalitní řetěz, přičemž se kolo přiváže za rám a pevný objekt. Lankové zámky poslouží jen na krátkou chvíli. Na dálkové výlety se hodí <a href="/cyklo-nosice-na-auto/">nosiče kol na auto a stojany</a>, doma pak stojan do garáže ušetří místo.</p>'
          '<h3>Zavazadla a navigace</h3>'
          '<p>Na trasy s nákladem jsou praktické <a href="/cyklo-tasky-a-nosice/">brašny, nosiče a košíky</a>, které přenesou váhu z ramen na kolo. Na dlouhých výletech se dobře hlídá trasa pomocí <a href="/cyklo-computery/">cyklopočítačů a navigací</a>, které ukazují rychlost, vzdálenost a u pokročilých modelů i mapu. Pití zajistí <a href="/cyklo-lahve-a-drzaky/">láhve, košíky a držáky telefonu</a>, zvonek a zrcátko vyřeší <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>. Rodiny s malými dětmi najdou <a href="/cyklo-sedacky-a-voziky/">dětské sedačky a vozíky za kolo</a>.</p>'
          '<h3>Značky v nabídce</h3>'
          '<p>V katalogu Sportek jsou nejčastěji zastoupené značky ' + B(('rockbros', 'Rockbros'), ('force', 'Force'), ('shimano', 'Shimano'), ('silvini', 'Silvini'), ('topeak', 'Topeak'), ('author', 'Author'), ('alpina', 'Alpina'), ('specialized', 'Specialized'), ('craft', 'Craft'), ('kenda', 'Kenda')) + '. Shimano je známé z pohonů a brzd, Topeak z pump a nářadí, Kenda z plášťů, Alpina z helem a brýlí a Silvini z cyklistického oblečení. Jednotlivé značky mají různé zaměření, takže nehledejte jedinou nejlepší, ale tu, která má silný segment pro váš typ jízdy.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Špatná velikost:</strong> kolo nebo helma se vybírají podle vzhledu a pak nepohodlně sedí.</li>'
          '<li><strong>Nekompatibilní díly:</strong> kazeta, řetěz nebo brzdová destička neodpovídá původnímu standardu.</li>'
          '<li><strong>Podceněný zámek:</strong> drahé kolo jištěné slabým lankem je snadný cíl.</li>'
          '<li><strong>Žádná světla:</strong> večerní návrat z práce bez světel je nebezpečný a může stát pokutu.</li>'
          '<li><strong>Zanedbaná údržba:</strong> suchý řetěz a nízký tlak v pláštích zkracují životnost dílů.</li>'
          '<li><strong>Nevhodné oblečení:</strong> bavlněné triko v dešti rychle nasákne a ochladí.</li></ul>'
          '<h3>Kdy nakupovat</h3>'
          '<p>Nejširší nabídka bývá na jaře, kdy se sezóna rozjíždí. Slevy na loňské modely a oblečení se objevují po skončení sezóny, tedy na podzim a v zimě. Díly a údržbové potřeby, které spotřebováváte pravidelně, se vyplatí kupovat podle potřeby a porovnávat obchody, protože stejný plášť nebo řetěz se v různých e-shopech liší dostupností i cenou.</p>',
    faq=[
        ('Jak poznám správnou velikost kola?', 'Orientačně podle výšky postavy a délky nohy, ale rozhoduje geometrie konkrétního rámu. Výrobci uvádějí tabulky s doporučenou výškou jezdce. Na sedle by měla být noha při spodní poloze pedálu mírně pokrčená a do řídítek nemá být nutné se příliš natahovat.'),
        ('Který typ kola je nejlepší pro začátečníka?', 'Pro většinu lidí je nejuniverzálnější trekingové nebo hybridní kolo. Zvládne asfalt, polní cesty i každodenní dojíždění a má vzpřímenou polohu. Až když víte, že vás baví terén nebo rychlost, má smysl přejít na horské nebo silniční kolo.'),
        ('Musím nosit helmu?', 'Povinnost se v Česku týká dětí do 18 let, ale pro bezpečí ji doporučuje nosit každý. Helma snižuje riziko vážných poranění hlavy při pádu a stojí za to ji mít i na krátkých trasách.'),
        ('Kdy vyměnit pláště a duše?', 'Pláště vyměňte, když je vzorek setřený, boky popraskané nebo se opakují defekty. Duši měníte po proražení, pokud ji nejde spolehlivě zalepit, a vždy ve správné velikosti podle rozměru na plášti.'),
        ('Jak často mazat řetěz?', 'Ideálně po každé větší jízdě v mokru a jinak zhruba jednou za několik výletů. Řetěz nejprve očistěte, naneste mazivo na jednotlivé články a přebytek otřete. Mazivo na suchou nebo mokrou jízdu se liší, tak vybírejte podle podmínek.'),
        ('Jaký zámek je nejbezpečnější?', 'Spolehlivější než lanko jsou U-zámky a články z tvrzené oceli. Kolo přivažte za rám a pevný nepohyblivý předmět, ne jen za kolo. Čím vyšší hodnota kola, tím silnější zámek se vyplatí a lepší je kombinovat dva různé typy.'),
        ('Co dát do tašky na výlet?', 'Náhradní duši, montážní páčky, malou pumpu nebo bombičky, multiklíč, lepení na duše a trochu jídla. K tomu telefon s powerbankou a lehkou bundu do proměnlivého počasí.'),
        ('Jsou pro silnici nutné cyklistické kalhoty s vložkou?', 'Nutné nejsou, ale na vzdálenosti nad hodinu jízdy výrazně zvyšují pohodlí. Vložka tlumí tlak a omezuje tření. Nosí se přímo na kůži, bez spodního prádla, a po každé jízdě se pere.'),
        ('Dá se elektrokolo používat bez motoru?', 'Ano, ale je těžší než běžné kolo, takže bez pomoci motoru se jede hůř. Doporučuje se je pravidelně používat, aby baterie neztrácela kapacitu hlubokým vybitím při dlouhém skladování.'),
        ('Je lepší koupit kolo online, nebo v kamenném obchodě?', 'Online je širší nabídka a snadné porovnání obchodů, v prodejně vám kolo seřídí a nastaví. Pokud kupujete přes internet, ověřte velikost rámu, zda je kolo seřízené, a počítejte s tím, že bude potřeba finální nastavení brzd a řazení.'),
    ])

# ------------------------------------------------------------------ sportovni-bundy
NEW['sportovni-bundy'] = dict(long=True,
    title='Sportovní bundy a vesty: zimní, softshell | Sporteka',
    desc='Sportovní bundy a vesty: zimní, softshellové, nepromokavé i větrovky. Jak vybrat podle sezóny a aktivity a kde porovnat nabídku českých obchodů.',
    intro='<p><strong>Sportovní bunda</strong> je nejdůležitější vrstva oblečení, protože stojí mezi vámi a počasím. Jiná bude fungovat při běhu za chladného rána, jiná na horách v zimě a další při deštivém výletu. Nejčastější chybou je koupit jednu univerzální bundu a pak v ní buď zmoknout, nebo se uvařit. Správný výběr proto začíná otázkou, kdy a při jaké činnosti ji chcete nosit.</p>'
          '<p>Na Sportece najdete <a href="/zimni-bundy/">zimní a péřové bundy</a>, <a href="/softshellove-bundy/">softshelly</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a>, <a href="/vetrovky/">větrovky</a>, <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> i <a href="/sportovni-vesty/">vesty</a> od mnoha obchodů pohromadě. Průvodce níže vysvětluje materiály, vrstvení, střihy a péči, abyste si z nabídky vybrali kus, který opravdu sedí k vašemu způsobu pohybu venku.</p>',
    guide='<h2>Jak vybrat bundu podle počasí a činnosti</h2>'
          '<p>Rozhodující jsou tři věci: jaké počasí čekáte, jak intenzivně se budete hýbat a kolik místa chcete věnovat balení. Při chůzi městem stačí jiná bunda než při běhu do kopce, kde se tělo zahřívá a potřebuje odvádět pot. Z toho vyplývá základní pravidlo: čím víc se hýbete, tím lehčí a prodyšnější bunda se vyplatí.</p>'
          + T(['Typ bundy', 'Chrání před', 'Hodí se na'], [
              ['Větrovka', 'větrem a lehkým deštěm', 'běh, kolo, svižnou chůzi, balení do batohu'],
              ['Softshell', 'větrem a mírným deštěm, drží teplo', 'turistika, podzim, jaro, každodenní nošení'],
              ['Nepromokavá bunda', 'deštěm i silným větrem', 'výlety v dešti, hory, cestování'],
              ['Zimní nebo péřová', 'mrazem', 'zimní procházky, lyžování, zastávky v klidu'],
              ['Jarní a podzimní', 'chladem a změnou počasí', 'město, volný čas, lehčí sport'],
              ['Vesta', 'chladem trupu, ruce zůstávají volné', 'doplněk pod i nad bundu, běh, kolo, práce venku']]) +
          '<h3>Větrovky a šusťákové bundy</h3>'
          '<p>Větrovka je tenká vrstva z hustě tkané látky, která zastaví vítr a pomůže udržet teplo. Většina se dá sbalit do vlastní kapsy a váží velmi málo. Běžně nejsou plně vodotěsné, ale lehký déšť vydrží. Pokud vás zajímá tento typ, projděte si <a href="/vetrovky/">větrovky a šusťákové bundy</a>. Šusťák je pak označení pro sportovní bundu z lesklého lehkého materiálu, často v retro střihu, kterou lidé nosí i jako módní kus.</p>'
          '<h3>Softshellové bundy</h3>'
          '<p>Softshell kombinuje pružný vnější materiál s měkkou, často česanou vnitřní stranou. Prodyšnost je vyšší než u pláštěnek a pružnost dovoluje volný pohyb paží. Většina softshellů má impregnaci, která odolá lehkému dešti, ale při dlouhém lijáku promokne. Hodí se do proměnlivého počasí a při aktivitě. V kategorii <a href="/softshellove-bundy/">softshellové bundy</a> uvidíte rozdíly mezi tenkými verzemi na léto a silnějšími s podšívkou na zimu.</p>'
          '<h3>Nepromokavé a outdoorové bundy</h3>'
          '<p>Nepromokavá bunda má membránu nebo povrchovou úpravu, která zadrží vodu. Dobrá kapuce se dá stáhnout kolem obličeje, zip má krytku a švy bývají zalepené. Proti dešti pomáhá, ale prodyšnost se liší: levnější modely uvnitř kondenzují vlhkost, takže při větší aktivitě promokne oblečení zevnitř. Nabídku najdete v kategorii <a href="/nepromokave-bundy/">nepromokavé a outdoorové bundy</a>. Pokud vás zajímá celá výbava na turistiku, podívejte se i do nadřazené kategorie <a href="/outdoor/">outdoor a turistika</a>.</p>'
          '<h3>Zimní a péřové bundy</h3>'
          '<p>Zimní bundy se plní peřím nebo syntetickým materiálem. Prachové peří je při stejné váze teplejší a lépe se stlačí, ale po namočení ztrácí izolaci a hůř schne. Syntetická výplň drží teplo i za vlhka a snáze se pere. Pro aktivní pohyb v zimě se často volí tenčí bunda a pod ní funkční vrstva, pro stání na zastávce nebo pozorování teplejší kus s kapucí. Přehled je v kategorii <a href="/zimni-bundy/">zimní a péřové bundy</a>.</p>'
          '<h3>Jarní a podzimní bundy</h3>'
          '<p>Je to nejširší kategorie a zahrnuje lehké prošívané bundy, mikinové bundy, parky i sportovní kousky do města. Hodí se na období, kdy ráno mrzne a odpoledne svítí slunce. Řada modelů kombinuje střih sportovní bundy a běžného oblečení, takže se nosí do práce i na procházku. Vybírejte podle <a href="/sportovni-bundy-jaro-podzim/">jarních a podzimních bund</a> a dbejte na to, aby se dala zapnout až ke krku.</p>'
          '<h3>Vesty</h3>'
          '<p>Vesta zahřeje trup, ale nechá volné ruce, takže se nepotíte v rukávech. Lehké péřové a prošívané vesty se nosí jako izolační vrstva pod větrovku, sportovní vesty se používají při běhu a jízdě na kole. Najdete je v kategorii <a href="/sportovni-vesty/">vesty</a>. Pokud se při pohybu často přehříváte, bude vesta dobrou volbou na jaro a podzim.</p>'
          '<h2>Materiály a membrány</h2>'
          '<p>Vrchní látka bývá z polyesteru nebo nylonu. Nylon je pevnější a lehčí, polyester méně nasákavý a lépe drží barvu. Membrána, tedy tenká vrstva uvnitř bundy, propouští vodní páru ven, ale vodu zvenčí nepustí. Přítomnost membrány ale sama o sobě neručí za kvalitu. Rozhoduje i konstrukce švů, kvalita zipů a stav povrchové úpravy, která se časem opotřebovává.</p>'
          '<ul><li><strong>Vodní sloupec</strong> udává, jak velký tlak vody látka vydrží. Vyšší číslo znamená lepší odolnost, ale je to jen orientační údaj.</li>'
          '<li><strong>Prodyšnost</strong> říká, kolik vodní páry projde látkou. Pro sport je důležitá stejně jako nepromokavost.</li>'
          '<li><strong>Zalepené švy</strong> brání vsakování vody dírkami po jehle.</li>'
          '<li><strong>Větrací zipy</strong> pod pažemi umožní odvětrat teplo bez svlékání.</li>'
          '<li><strong>Impregnace DWR</strong> nechá vodu stékat po povrchu a časem se musí obnovit.</li></ul>'
          '<h2>Vrstvení a střih</h2>'
          '<p>Nejjednodušší systém tvoří tři vrstvy. Spodní funkční prádlo odvádí pot, střední vrstva izoluje, například fleece nebo lehká <a href="/mikiny/">mikina</a>, a svrchní vrstva chrání před větrem a vodou. Tělo pracuje nejlépe, když jednotlivé vrstvy lze rychle přidat nebo odebrat. V zimě se vyplatí volnější střih, který pojme střední vrstvu, v létě naopak přiléhavý, aby nic nevlálo.</p>'
          '<h3>Na co se dívat při zkoušení</h3>'
          '<ul><li>Rukávy mají po zvednutí paží zůstat na zápěstí, ne vyjet k loktům.</li>'
          '<li>Délka kolem pasu musí zakrýt záda při předklonu, na kole i při sedu.</li>'
          '<li>Kapuce se musí dát nastavit tak, aby se při otočení hlavy otočila s ní.</li>'
          '<li>Límec chrání krk, aniž by tlačil na bradu.</li>'
          '<li>Kapsy se zapínají zipem a jsou dostupné i s batohem na zádech.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V katalogu jsou zastoupené například ' + B(('regatta', 'Regatta'), ('trespass', 'Trespass'), ('columbia', 'Columbia'), ('dare2b', 'Dare2b'), ('helly-hansen', 'Helly Hansen'), ('haglofs', 'Haglöfs'), ('fjallraven', 'Fjällräven'), ('the-north-face', 'The North Face'), ('dynafit', 'Dynafit'), ('kilpi', 'Kilpi'), ('reima', 'Reima'), ('nike', 'Nike'), ('adidas', 'Adidas')) + '. Outdoorové značky jsou silné v nepromokavých bundách a zimních modelech, sportovní značky ve větrovkách a lehkých bundách na trénink. Dětské kolekce nabízí například Reima.</p>'
          '<h2>Péče o bundy</h2>'
          '<p>Bundy perte podle štítku, nejlépe na nižší teplotu a bez aviváže, která ucpává póry membrány a snižuje její účinnost. Zipy před praním zapněte a suchý zip zacvakněte, aby se nic nezachytilo. Péřové a prošívané kousky se suší pomalu, občas se protřepou, aby se výplň nezlepila. Impregnaci je vhodné po několika sezónách obnovit speciálním přípravkem, jinak se látka začne nasávat vodou. Bundu skladujte volně na ramínku, nestlačenou v batohu, aby neztratila nadnášení.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Příliš teplá bunda na sport:</strong> při pohybu se člověk potí a po zastavení prochladne.</li>'
          '<li><strong>Nepromokavost místo prodyšnosti:</strong> neprodyšný plášť vyrobí v bundě vlastní déšť.</li>'
          '<li><strong>Nevhodná velikost:</strong> příliš těsná bunda brzdí pohyb, příliš volná táhne.</li>'
          '<li><strong>Ignorování kapuce:</strong> pokud ji nepotřebujete, můžete ušetřit váhu, v horách ale chybí.</li>'
          '<li><strong>Zanedbaná impregnace:</strong> stará bunda, která už nepropouští pot ani vodu, nemusí být špatná, jen potřebuje obnovu.</li></ul>'
          '<h3>Pro koho a kdy koupit</h3>'
          '<p>Pro děti volte bundy s reflexními prvky a lehce nastavitelnými rukávy, pro seniory s dlouhým zipem a velkými kapsami. Pánské a dámské střihy se liší šířkou ramen, pasu a boků, takže ženám často sedí dámský střih lépe i při stejné velikosti. Zimní modely se nejlépe hledají na jaře a v létě, kdy je méně poptávky, lehké větrovky zase po skončení sezóny. Na Sportece porovnáte, kde je daná velikost skladem.</p>'
          '<h3>Bunda pro konkrétní sport</h3><p>Pro běh vybírejte nejlehčí větrovku nebo vestu s reflexními prvky a malou kapsou na klíče. Na kolo se hodí delší záda, prodloužené rukávy a výraznější barva, aby vás viděli řidiči. Při lyžování a snowboardu potřebujete zimní bundu se sněžným lemem, zpevněnými rameny a kapsou na skipas. Na turistiku sáhněte po lehké nepromokavé skořápce, která se vejde do víka batohu, a přes zimu doplňte tenkou péřovou bundou na zastávky. Pro děti a mládež při školních aktivitách bude praktická odolná jarní nebo podzimní bunda, která snese pád v bahně a časté praní.</p>'
          '<h3>Cestování a každodenní použití</h3><p>Na cestách ocení lidé bundu, která se dá sbalit do malého objemu a vejde se do příručního zavazadla. V letadle nebo vlaku se hodí tenká izolační vrstva, v dešti nepromokavá skořápka. Ve městě se vyplatí neutrální barvy, které se kombinují s běžným oblečením, a diskrétní reflexní detaily pro bezpečí za tmy.</p>',
    faq=[
        ('Jaký je rozdíl mezi softshellem a nepromokavou bundou?', 'Softshell je pružnější a prodyšnější, ale snese jen lehký déšť. Nepromokavá bunda s membránou ochrání před lijákem, bývá ale méně pohodlná a dražší. Pro proměnlivé počasí a aktivní pohyb je lepší softshell, pro déšť skořápka.'),
        ('Co znamená vodní sloupec a jaká hodnota stačí?', 'Vodní sloupec udává, jak vysoký sloupec vody látka vydrží bez prosáknutí. Pro mírný déšť stačí nižší hodnoty, pro vytrvalý liják a hory se volí vyšší. Údaj je orientační a nezohledňuje kvalitu švů ani zipů.'),
        ('Jaká velikost bundy je správná?', 'Bunda má přiléhat, ale nesmí omezovat pohyb. Zkuste zvednout ruce a udělat předklon. Pokud plánujete pod ni zimní vrstvu, zvolte volnější střih, ale ne takový, aby foukal vítr za záda.'),
        ('Péřová, nebo syntetická výplň?', 'Peří je lehčí a lépe se sbalí, ale nemá rádo vlhko. Syntetika zahřeje i po namočení a je snáze udržovatelná. Pro suchý mráz je lepší peří, pro vlhké zimy a aktivní sporty syntetika.'),
        ('Jak vyprat nepromokavou bundu?', 'Použijte jemný prací prostředek bez aviváže, nižší teplotu a šetrný program. Po vyprání ji opatrně vysušte a případně obnovte impregnaci sprejem nebo prostředkem do pračky. Řiďte se štítkem uvnitř.'),
        ('Dá se bunda nosit i na každý den?', 'Ano. Většina sportovních bund je dnes střižená tak, aby fungovala i ve městě. U každodenního nošení hledejte pohodlné zapínání, praktické kapsy a barvu, která se dobře kombinuje s ostatním oblečením.'),
        ('Kdy se hodí vesta místo bundy?', 'Při aktivitách, kdy se vám rychle přehřívají paže: běh, kolo, svižná chůze nebo práce na zahradě. Vesta také funguje jako střední vrstva pod větrovku v chladnějším počasí.'),
        ('Jak poznám dobrou zimní bundu pro děti?', 'Měla by být teplá, ale lehká, s odolným povrchem, zipem kryjícím bradu a kapucí, která se dá stáhnout. Důležité jsou i reflexní prvky a rukávy se zápěstními manžetami, které nepropustí sníh.'),
        ('Proč mě v nepromokavé bundě bývá vedro?', 'Membrána musí odvádět páru, ale při intenzivním pohybu vyprodukujete víc vlhkosti, než stihne projít. Pomůže otevřít větrací zipy, snížit počet vrstev pod bundou nebo zvolit prodyšnější model.'),
        ('Je lepší koupit bundu na konci sezóny?', 'Obvykle ano. Obchody ve stejnou dobu vyprodávají předchozí kolekci a ceny klesají. Nevýhodou je omezený výběr velikostí a barev, takže je dobré vybírat včas a sledovat dostupnost.'),
    ])

# ------------------------------------------------------------------ outdoor
NEW['outdoor'] = dict(long=True,
    title='Outdoor a turistika: batohy, láhve, čelovky | Sporteka',
    desc='Výbava na turistiku a do přírody: batohy, termosky, čelovky, nože, hole i první pomoc. Porovnejte nabídku českých obchodů a vyberte podle výletu.',
    intro='<p><strong>Outdoorová výbava</strong> se skládá z mnoha drobností, které na první pohled nesouvisí, a přesto rozhodují o tom, jak výlet dopadne. Dobrý batoh, dost vody, světlo do tmy a lékárnička vás stojí málo místa, ale chrání vás před nepříjemnostmi, které se na trase stávají často. Cílem tohoto přehledu je ukázat, co patří do základní sady a co se hodí až při náročnějších výpravách.</p>'
          '<p>Na Sportece najdete <a href="/batohy/">batohy</a>, <a href="/lahve-a-termosky/">láhve a termosky</a>, <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, <a href="/trekove-hole/">trekové hole</a>, <a href="/outdoorove-noze-a-multitoola/">nože a multitoolly</a> a další doplňky z českých obchodů na jednom místě. Níže popisujeme, jak výbavu poskládat podle délky výletu, ročního období a obtížnosti terénu a kde se vyplatí nešetřit.</p>',
    guide='<h2>Jak zvolit výbavu podle typu výletu</h2>'
          '<p>Procházka po značených cestách vyžaduje jiné vybavení než dvoudenní trek s přespáním. Čím je trasa delší a odlehlejší, tím víc záleží na váze, spolehlivosti a samostatnosti. Zásada zní: do batohu patří to, co potřebujete k bezpečnému návratu, a až pak věci pro pohodlí.</p>'
          + T(['Typ výletu', 'Co nesmí chybět', 'Co je volitelné'], [
              ['Krátký výlet do hodiny', 'voda, mobil, malá svačina', 'brýle, hole'],
              ['Celodenní túra', 'batoh, pití, pláštěnka, čelovka, lékárnička', 'termoska, dalekohled, powerbanka'],
              ['Vícedenní trek', 'objemnější batoh, čelovka, hygiena, navigace, strava', 'nůž, hole, filtr na vodu'],
              ['Horolezectví a ferraty', 'sedák, přilba, lana a karabiny, vhodná obuv', 'rukavice, brýle, čelovka'],
              ['Rodinný výlet', 'pití, svačina, pláštěnky, lékárnička', 'repelent, pohodlná sedačka'],
              ['Zimní túra', 'termoska, čelovka, nesmeky, teplé rukavice', 'powerbanka, brýle, hole']]) +
          '<h2>Batohy: velikost a nošení</h2>'
          '<p>Objem batohu se uvádí v litrech. Na půldenní výlet postačí malý batoh, na celodenní o něco větší, na vícedenní trek je třeba několikanásobek. Objem ale není všechno. Důležitá jsou záda: nastavitelná délka zad, bederní pás, který přenese váhu na boky, a ramenní popruhy, které netlačí. Dobře seřízený batoh drží těžiště blízko těla a nenechává ramena zbytečně unavovat.</p>'
          '<p>Podle použití vybírejte z podkategorií. <a href="/turisticke-batohy/">Turistické batohy</a> mají zádový systém a výztuhy pro delší cesty, <a href="/mestske-batohy/">městské a sportovní batohy</a> jsou praktické do práce, na trénink i krátké výlety, <a href="/skolni-batohy/">školní a studentské batohy</a> mají přihrádky pro knihy a ergonomická záda pro děti a <a href="/tasky-pres-rameno/">tašky přes rameno a dokladovky</a> poslouží na doklady, peněženku a drobnosti. Pro malé věci a běh jsou praktické i <a href="/sportovni-tasky/">sportovní tašky a ledvinky</a>.</p>'
          '<h3>Jak batoh zabalit</h3>'
          '<ul><li>Těžké věci dejte nahoru a blízko zad, lehké dolů.</li>'
          '<li>Věci, které potřebujete často, patří do horní kapsy nebo bočních kapes.</li>'
          '<li>Oblečení a spacák zabalte do nepromokavých pytlů.</li>'
          '<li>Pásky a popruhy utáhněte tak, aby se obsah neposouval.</li>'
          '<li>Před odchodem zkuste batoh nasadit a projít se po místnosti.</li></ul>'
          '<h2>Pití, jídlo a energie</h2>'
          '<p>Pitný režim je při turistice důležitější, než se zdá. <a href="/lahve-a-termosky/">Láhve a termosky</a> se liší materiálem i izolací. Plastové jsou lehké, nerezové odolné a dobře drží teplo i chlad, termosky na jídlo se hodí na delší zastávky v zimě. U každé láhve ověřte uzávěr, protože pití v batohu rozlité přes zip dokáže zničit celý den. Na delší túry zvažte vodní vak v batohu, ze kterého se pije hadičkou bez zastavování.</p>'
          '<p>Na vícedenní výpravy se hodí <a href="/outdoorova-strava/">outdoorová a lyofilizovaná strava</a>, která je lehká a stačí jen zalít horkou vodou. Pro čištění vody a hygienu v přírodě slouží <a href="/hygiena-a-repelenty/">hygiena, repelenty a úprava vody</a>. U neznámých zdrojů vodu vždy upravte, protože i čistě vypadající potok může být kontaminovaný.</p>'
          '<h2>Světlo, navigace a elektronika</h2>'
          '<p>Čelovka patří do batohu celoročně, i když plánujete návrat za světla. Zpoždění, špatná orientace nebo zranění vás mohou zastihnout za tmy. Při výběru sledujte dosvit, režimy svícení, způsob napájení a odolnost proti vodě. Širší paprsek se hodí do blízka, soustředěný na dálku. Nabídka je v kategorii <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, kde najdete i kapesní svítilny.</p>'
          '<p>Pro orientaci v terénu poslouží <a href="/dalekohledy-a-kompasy/">dalekohledy, kompasy a navigace</a>. Mapa a kompas fungují bez baterie a každý by měl umět je použít aspoň na základní úrovni. <a href="/sportovni-hodinky/">Sportovní hodinky a elektronika</a> měří tep, krok a stoupání a u pokročilejších kusů i trasu, <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a> pak dobíjejí telefon a další zařízení. Na delší trase počítejte s tím, že se telefon vybije dřív, než čekáte, zvlášť v mrazu.</p>'
          '<h2>Chůze, ochrana a bezpečnost</h2>'
          '<p><a href="/trekove-hole/">Trekové a nordic walking hole</a> odlehčí kolenům při sestupu a pomáhají na stoupání. Při sestupu hole prodlužte, na stoupání je mírně zkraťte. Pro zimní trasy a zledovatělé cesty se hodí <a href="/nesmeky/">nesmeky a protiskluzové návleky</a>, které se natáhnou přes obuv a zlepší přilnavost na ledu a udusaném sněhu. Proti slunci a prachu chrání <a href="/sportovni-bryle/">sportovní a sluneční brýle</a>, na horách se vybírají s dobrou UV ochranou.</p>'
          '<p>Při náhlé změně počasí zachrání den <a href="/plastenky/">pláštěnky a pončo</a>, které se vejdou do kapsy. Zranění vyřeší <a href="/prvni-pomoc/">lékárničky a první pomoc</a>: obvaz, náplasti, dezinfekce, nůžky a izotermická fólie jsou základ. Kontrolujte jejich platnost a po použití je doplňujte.</p>'
          '<h3>Nože, multitoolly a doplňky</h3>'
          '<p>Kvalitní <a href="/outdoorove-noze-a-multitoola/">outdoorový nůž nebo multitool</a> se hodí na krájení jídla, drobné opravy i přípravu podpalu. Pevnou čepel vybírejte pro náročnější práci, skládací pro každodenní nošení. Před koupí se seznamte s právními pravidly nošení nožů v místě, kde se pohybujete. Drobné pomůcky, jako karabiny, lana a organizéry, najdete v kategorii <a href="/outdoor-doplnky/">outdoorové doplňky</a>.</p>'
          '<h2>Horolezectví a ferraty</h2>'
          '<p>Horolezecká výbava je bezpečnostní vybavení, u kterého nemá smysl riskovat na kvalitě. <a href="/lezecke-boty/">Lezečky</a> mají těsný střih a hladkou podrážku, <a href="/lezecke-sedaky-a-pomucky/">sedáky, přilby a pomůcky</a> chrání při pádu a <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a> jsou základem jištění. Celý obor shrnuje kategorie <a href="/horolezectvi/">horolezectví a ferraty</a>. Začátečníci by měli výbavu kupovat až po absolvování kurzu, kde se vysvětlí její správné použití a údržba.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('deuter', 'Deuter'), ('fjallraven', 'Fjällräven'), ('osprey', 'Osprey'), ('laken', 'Laken'), ('victorinox', 'Victorinox'), ('oakley', 'Oakley'), ('alpina', 'Alpina'), ('the-north-face', 'The North Face'), ('levenhuk', 'Levenhuk'), ('baagl', 'Baagl')) + '. Deuter a Osprey jsou silné v turistických batozích, Victorinox v multitoolech a nožích, Oakley a Alpina v brýlích a Levenhuk v optice. Armádní styl nabízejí značky jako Mil-Tec nebo Rothco.</p>'
          '<h2>Sezónnost a péče o výbavu</h2>'
          '<p>Na jaře a na podzim počítejte s rychlými změnami počasí, takže přibalte lehkou nepromokavou vrstvu. V létě dávejte pozor na dehydrataci a UV záření, v zimě na kratší den a mráz. Po výletu batoh vyklepejte a nechte vyschnout, termosku vymyjte a nechte otevřenou, aby nezapáchala. Čelovku vyndejte z batohu, jinak se může v zavazadle náhodně zapnout. Nůž očistěte a lehce naolejujte, hole rozložte a osušte.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li><strong>Příliš těžký batoh:</strong> do batohu se snadno nasype víc, než je nutné. Vážte, co nesete.</li>'
          '<li><strong>Málo vody:</strong> pití se vyplatí nést raději víc, protože při dlouhém výstupu se spotřebuje rychle.</li>'
          '<li><strong>Čelovka bez náhradních baterií:</strong> světlo se vybije v nejhorší chvíli.</li>'
          '<li><strong>Nevyzkoušená výbava:</strong> nové boty a batoh před delším výletem aspoň na kratší trase otestujte.</li>'
          '<li><strong>Žádný plán:</strong> před výletem se podívejte na předpověď a řekněte někomu, kam jdete.</li><li><strong>Neověřená funkčnost:</strong> před výletem zkontrolujte baterie, zipy a uzávěry.</li></ul>'
          '<p>Při porovnávání na Sportece se vyplatí hlídat dostupnost velikosti a barvy, protože u batohů a brýlí se rychle vyprodají oblíbené modely.</p>'
          '<h3>Výbava podle ročního období</h3><p>Na jaře se hodí lehká bunda do deště, čelovka a repelent, protože klíšťata a komáři se probouzejí brzy. V létě je důležitá ochrana před sluncem: brýle, čepice a dostatek vody. Podzim přináší kratší den, mlhy a první mrazy, proto patří do batohu teplá vrstva, rukavice a čelovka. V zimě přidejte termosku, nesmeky a náhradní ponožky. V každé sezóně platí, že lehká výbava šetří síly, ale nesmí být na úkor bezpečí.</p>'
          '<h3>Vybavení pro děti a rodinné výlety</h3><p>Děti se rychle unaví a prochladnou, takže potřebují častější zastávky, teplý čaj, svačinu a oblečení do vrstev. Dětský batoh by měl být lehký a nést jen drobnosti, jako láhev a pláštěnku. Při delším výletu vezměte náhradní tričko a ponožky. Hra s kompasem nebo dalekohledem navíc učí děti orientaci a zvědavost, což z krátké procházky udělá malé dobrodružství.</p>'
          '<h3>Jak vybavení postupně doplňovat</h3><p>Nemusíte kupovat vše najednou. Začněte batohem, pitím, pláštěnkou a lékárničkou, po několika výletech doplňte čelovku, hole nebo termosku podle toho, co vám chybělo. Vlastní zkušenost je lepším rádcem než seznam z internetu. Dobrým zvykem je vést si krátký seznam věcí, které jste na trase opravdu použili, a ten před dalším výletem projít. Tak se výbava časem zpřesní a batoh zůstane lehký. Pokud něco nepoužijete během celé sezóny, příště to nechte doma.</p>',
    faq=[
        ('Jaký objem batohu zvolit na jednodenní túru?', 'Pro jednodenní túru bývá vhodný střední objem, který pojme vodu, svačinu, pláštěnku, lékárničku a teplou vrstvu. Důležitější než objem je pohodlný zádový systém a bederní pás, který přenese část váhy na boky.'),
        ('Kolik vody vzít na výlet?', 'Záleží na délce, teplotě a náročnosti. Lepší je mít rezervu než vodu vypít po půlce cesty. Na delších trasách plánujte doplnění z bezpečných zdrojů a nezapomeňte na prostředek k úpravě vody.'),
        ('Je lepší termoska, nebo láhev?', 'Láhev je lehčí a levnější na běžné pití, termoska udrží čaj horký i chladný a hodí se v zimě a při delších zastávkách. Pro každodenní použití se vyplatí nerez, protože snese pády a nezapáchá.'),
        ('Potřebuji čelovku, i když jdu za světla?', 'Ano. Při zpoždění, ztrátě směru nebo zranění můžete skončit v lese za tmy. Čelovka je lehká a zabírá minimum místa, takže patří do výbavy celoročně.'),
        ('K čemu jsou trekové hole?', 'Odlehčují kloubům při sestupu, zlepšují stabilitu na nerovném terénu a pomáhají při stoupání rozložit námahu do paží. Správně nastavená hůl má loket ohnutý zhruba do pravého úhlu.'),
        ('Co by mělo být v lékárničce na výlet?', 'Obvaz, náplasti, dezinfekce, nůžky, elastické obinadlo, rukavice a izotermická fólie. Doplňte osobní léky a zkontrolujte datum expirace.'),
        ('Jaké brýle zvolit na hory?', 'Brýle s dobrou UV ochranou a širokým zakrytím očí, které sedí pevně a nesklouzávají. Na zasněžených svazích je sluneční záření odražené sněhem silnější, proto je ochrana obzvlášť důležitá.'),
        ('Mohu nosit nůž při turistice?', 'Pravidla se liší podle místa a situace. Skládací nůž s krátkou čepelí je obvykle běžnou součástí výbavy, ale je dobré se seznámit s místními předpisy a nůž nosit zabalený v batohu, ne viditelně u pasu ve městě.'),
        ('Kdy si koupit lezecké vybavení?', 'Až po absolvování kurzu nebo se zkušeným parťákem. Nejdřív se naučte správně vázat, jistit a kontrolovat vybavení. Boty a sedák si pořiďte podle toho, jak budete lézt, a nikdy nekupujte použité lano nebo karabiny s neznámou historií.'),
        ('Jak dlouho vydrží powerbanka v mrazu?', 'V mrazu kapacita baterií klesá, takže počítejte s kratší výdrží. Pomáhá uchovávat powerbanku a telefon blízko těla ve vnitřní kapse a nenechávat je venku v batohu.'),
    ])

# ------------------------------------------------------------------ mikiny
NEW['mikiny'] = dict(long=True,
    title='Mikiny: sportovní, fleecové, funkční | Sporteka',
    desc='Mikiny na sport i volný čas: fleecové, funkční a bavlněné s kapucí nebo bez. Jak vybrat materiál, střih a velikost a kde porovnat české obchody.',
    intro='<p><strong>Mikina</strong> je nejuniverzálnější kus sportovního šatníku. Nosí se na trénink, na výlet, do školy i na procházku, a podle materiálu a střihu se může chovat velmi různě. Bavlněná je pohodlná na sezení, funkční odvádí pot při běhu, fleecová drží teplo v chladném počasí. Při výběru se proto vyplatí rozhodnout, k čemu ji budete nosit nejčastěji.</p>'
          '<p>Na Sportece najdete <a href="/fleecove-mikiny/">fleecové mikiny</a> i <a href="/funkcni-mikiny/">funkční mikiny</a> a také klasické modely s kapucí, na zip i přes hlavu od značek jako Nike, Champion, Adidas nebo Under Armour. Průvodce níže vysvětluje materiály, střihy, vrstvení, péči i nejčastější chyby, abyste si z velké nabídky vybrali kus, který vydrží víc sezón.</p>',
    guide='<h2>Jak vybrat mikinu podle použití</h2>'
          '<p>Slovo mikina pokrývá několik odlišných druhů oblečení. Společné mají jen to, že jde o vrchní vrstvu s dlouhým rukávem. Pro správnou volbu určete nejdřív, jestli bude mikina sloužit jako sportovní vrstva, jako teplá bunda do chladna, nebo jen jako pohodlné oblečení na doma a do města.</p>'
          + T(['Druh mikiny', 'Hlavní přednost', 'Hodí se na'], [
              ['Bavlněná', 'měkkost a pohodlí', 'město, volný čas, doma, lehké cvičení'],
              ['Směs bavlny a polyesteru', 'lepší tvarová stálost a rychlejší schnutí', 'každodenní nošení, trénink'],
              ['Funkční', 'odvod potu a rychlé schnutí', 'běh, fitness, kolo, lehké túry'],
              ['Fleecová', 'tepelná izolace při nízké váze', 'chladné dny, turistika, střední vrstva pod bundu'],
              ['Na zip', 'snadné ventilování a svlékání', 'sport s proměnlivou intenzitou, vrstvení'],
              ['S kapucí', 'ochrana hlavy a krku', 'město, chladné ráno, chůze s batohem']]) +
          '<h3>Bavlna a směsové materiály</h3>'
          '<p>Klasická mikina bývá z česané bavlny, která je příjemná na dotek a dobře izoluje. Nevýhodou je, že nasákne potem a pomalu schne. Při lehkém pohybu ve městě to nevadí, při běhu nebo intenzivním cvičení však mikina ztěžkne a přestane hřát. Směs bavlny s polyesterem se nesráží a po vyprání drží tvar, takže se hodí na každodenní nošení. Pokud chcete mikinu kombinovat se sukní, džínami nebo kalhotami, sáhněte po jednoduchém barevném provedení, které se dobře kombinuje.</p>'
          '<h3>Funkční mikiny</h3>'
          '<p>Funkční mikina používá materiály, které odvádějí vlhkost od kůže a rychle schnou. Mívají ploché švy proti odírání, často i prodyšné panely v místech, kde se tělo potí. Hodí se na běh, fitness, kolo i lehčí túry. V kategorii <a href="/funkcni-mikiny/">funkční mikiny</a> najdete jak tenké modely na chladnější ráno, tak silnější s fleecovou vložkou. Pro maximální prodyšnost vybírejte takové, které se dají otevřít zipem u krku.</p>'
          '<h3>Fleecové mikiny</h3>'
          '<p>Fleece je syntetický materiál, který při malé váze dobře zadrží teplo a nenasákne. Hodí se na výlety, kdy potřebujete teplou střední vrstvu pod nepromokavou bundu. Fleecové mikiny jsou často ve verzi na zip, takže se dají v případě potřeby rychle rozepnout. Vybírejte je podle tloušťky: tenký fleece funguje jako střední vrstva v pohybu, silnější slouží jako teplá bunda na podzim. Celý přehled najdete v kategorii <a href="/fleecove-mikiny/">fleecové mikiny</a>. Pozor na šustění a elektrizaci: levnější materiály se mohou při tření nabíjet.</p>'
          '<h2>Střih, velikost a kapuce</h2>'
          '<p>Střih ovlivňuje pohodlí i použití. Přiléhavá mikina je vhodná pro sport, protože nevlaje a nepřekáží pohybu. Volný střih oversize se nosí ve městě a poskytuje prostor pro vrstvení. Při zkoušení zvedněte ruce nad hlavu a zkontrolujte, zda se spodní lem nezvedá nad pas. Rukávy mají končit na zápěstí a zůstat tam i při pohybu paží.</p>'
          '<ul><li><strong>Kapuce:</strong> hodí se do větru a chladna, ale přes batoh může tlačit. Ověřte, zda se dá stáhnout šňůrkou.</li>'
          '<li><strong>Zip nebo přes hlavu:</strong> zip se snáze svléká a větrá, mikina přes hlavu je jednodušší a těsnější.</li>'
          '<li><strong>Kapsa klokanka:</strong> pohodlná na zahřátí rukou, ale při sportu zbytečně zatěžuje.</li>'
          '<li><strong>Manžety a lem:</strong> elastické manžety drží teplo a nesjíždějí, ale nesmí tlačit.</li>'
          '<li><strong>Stojáček:</strong> chrání krk a ocení ho běžci i cyklisté.</li></ul>'
          '<h3>Pánské, dámské, dětské a unisex</h3>'
          '<p>Dámské mikiny bývají užší v ramenou a pase a často kratší, pánské širší a delší. Unisex modely se nosí volněji. Dětské mikiny volte s rezervou na růst, ale ne příliš velké, aby nepřekážely. Pro školní děti jsou praktické materiály, které snesou časté praní, a pro nejmenší bez šňůrek u krku, které mohou zachytit hračky nebo prvky na hřišti.</p>'
          '<h2>Mikina jako součást vrstvení</h2>'
          '<p>Na sport venku funguje mikina nejlépe jako střední vrstva. Pod ní patří funkční tričko, nad ní větrovka nebo bunda. Takto upravená kombinace nechá pot odcházet a zároveň drží teplo. Nejvhodnější vrchní vrstvu najdete v kategorii <a href="/sportovni-bundy/">sportovní bundy a vesty</a>, například <a href="/softshellove-bundy/">softshelly</a>, <a href="/vetrovky/">větrovky</a> nebo <a href="/nepromokave-bundy/">nepromokavé bundy</a>. Na zimu se hodí kombinace se <a href="/zimni-bundy/">zimní bundou</a>. Pokud potřebujete celý outfit, podívejte se i na <a href="/sportovni-obleceni/">sportovní oblečení</a> nebo na <a href="/outdoor/">outdoor a turistiku</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nabídku tvoří značky ' + B(('nike', 'Nike'), ('champion', 'Champion'), ('adidas', 'Adidas'), ('under-armour', 'Under Armour'), ('puma', 'Puma'), ('fila', 'Fila'), ('new-era', 'New Era'), ('fanatics', 'Fanatics'), ('mitchell-ness', 'Mitchell & Ness'), ('columbia', 'Columbia'), ('regatta', 'Regatta'), ('trespass', 'Trespass'), ('helly-hansen', 'Helly Hansen')) + '. Sportovní značky převažují u tréninkových a každodenních modelů, outdoorové u fleecových a funkčních. Fanouškovské značky nabízejí mikiny s týmovými logy.</p>'
          '<h2>Péče o mikiny</h2>'
          '<p>Před praním mikinu otočte naruby, aby se nepoškodil potisk a vlas. Perte na nižší teplotu, bez aviváže u funkčních a fleecových modelů, protože zanáší vlákna a ruší jejich vlastnosti. Fleece nesušte na vysoké teplotě, může se zdeformovat. Bavlněné mikiny se mohou po praní srazit, proto je sušte opatrně a při koupi zvažte mírnou rezervu. Potisky chraňte před žehličkou, pokud to štítek nedovoluje.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li><strong>Bavlněná mikina na sport:</strong> po zpocení je těžká a studená.</li>'
          '<li><strong>Příliš těsný střih:</strong> omezuje pohyb a při vrstvení tlačí.</li>'
          '<li><strong>Ignorování štítku s praním:</strong> funkční materiály ztrácejí vlastnosti po špatné péči.</li>'
          '<li><strong>Jediná mikina na všechno:</strong> pro běh a chodník do kanceláře se hodí různé typy.</li>'
          '<li><strong>Nesprávná velikost u dětí:</strong> příliš velká mikina překáží při hře.</li></ul>'
          '<h3>Kdy mikiny kupovat</h3>'
          '<p>Nejvíc nabídky bývá na podzim, slevy se objevují na konci zimy a na jaře. Mikiny s týmovými logy a kolekce značek se obměňují, takže oblíbené kusy mizí rychle. Na Sportece porovnáte více obchodů naráz a uvidíte, kde je vaše velikost skladem.</p>'
          '<h3>Jak kombinovat mikiny s dalším oblečením</h3><p>Do města se mikina hodí k džínám, joggerům nebo sukni, k tomu tenisky nebo sportovní obuv. Při sportu ji kombinujte s legínami nebo tréninkovými kraťasy. Barva by měla ladit s ostatními kusy: tmavé odstíny jsou praktické a nezničí je skvrny, světlé působí svěžeji, ale rychleji se špiní. Výrazné potisky a loga dobře fungují s jednoduchými bezvzorovými kalhotami.</p>'
          '<h3>Sportovní disciplíny a mikiny</h3><p>Pro běh vybírejte tenkou, přiléhavou a prodyšnou mikinu, na fitness stačí středně silná s pružným střihem. Na kolo se hodí delší záda, aby nefoukalo, na lyže a snowboard fleecová nebo funkční vrstva pod bundu. Pro kolektivní sporty jsou oblíbené týmové mikiny, ve kterých se chodí k zápasu a po něm. Při turistice nahradí fleecová mikina těžší svetr a při přestávce ji lze obléci přes funkční tričko.</p>'
          '<h3>Udržitelnost a životnost</h3><p>Dobrá mikina vydrží mnoho sezón, pokud ji správně perete. Nepřeplňujte pračku, protože tření poškozuje vlas, a nepoužívejte zbytečně silné prostředky. Žmolky na povrchu můžete opatrně odstranit holicím strojkem nebo hřebínkem na žmolky. Mikiny z recyklovaných materiálů nabízejí některé značky, a pokud na štítku najdete údaj o složení, získáte představu o jejich vlastnostech. Když mikinu přestanete nosit, darujte ji nebo odevzdejte do sběru textilu.</p>'
          '<h3>Mikina jako dárek</h3><p>Při výběru pro někoho jiného držte neutrální barvy a volnější střih, který odpustí chyby ve velikosti. Fanoušci sportovních týmů ocení mikinu s klubovým logem, běžci kousek z funkčního materiálu a děti oblíbenou postavu nebo barvu. Ověřte možnost výměny velikosti u obchodu, ze kterého kupujete. Pokud váháte mezi dvěma velikostmi, bezpečnější je větší, protože výrazně menší mikina tlačí v ramenou a nedá se upravit, zatímco větší jde stáhnout pasem nebo zkrátit rukávy.</p>'
          '<h3>Mikina do školy, do práce a na cesty</h3><p>Ve škole a v kanceláři s uvolněným dress codem se osvědčují mikiny jednobarevné, bez velkých nápisů, z hladkého materiálu, který vypadá upraveně i po celém dni. Na cesty vlakem nebo letadlem se hodí mikina s kapucí a kapsou na zip, do které se vejde jízdenka a sluchátka. Při dlouhé cestě ji lze složit pod hlavu místo polštáře. Pro společné akce, výlety třídy nebo firemní dny volte praktické barvy, které snesou i špinavější prostředí.</p>',
    faq=[
        ('Jaký je rozdíl mezi mikinou a fleecem?', 'Mikina je obvykle z česané bavlny nebo směsi, je měkká, ale pomalu schne. Fleece je syntetický, lehký, teplý a nenasákne. Fleece je lepší do přírody, mikina do města a na každodenní nošení.'),
        ('Je funkční mikina lepší než bavlněná?', 'Na sport ano, protože odvádí pot a rychle schne. Pro klidné nošení je bavlněná pohodlnější a příjemnější na dotek. Záleží na použití, ne na tom, že by jeden materiál byl obecně lepší.'),
        ('Jak vybrat velikost mikiny?', 'Podle tabulky výrobce a podle způsobu nošení. Při sportu volte přiléhavou velikost, ve městě můžete zvolit volnější. Mikina by neměla být v ramenou příliš široká a rukávy mají končit na zápěstí.'),
        ('Má se mikina srazit po praní?', 'Bavlněné mikiny se mohou lehce srazit, zvlášť při vyšší teplotě a sušení v sušičce. Pomůže praní na nižší teplotu a sušení na vzduchu. Funkční a fleecové modely se prakticky nesrážejí.'),
        ('Jak vyprat mikinu s potiskem?', 'Otočte ji naruby, perte na nižší teplotu a nepoužívejte silné bělicí prostředky. Žehlete jen z rubu, nikdy přes potisk, pokud štítek výslovně nedovoluje jinak.'),
        ('Hodí se mikina na běhání?', 'Ano, pokud je funkční a přiléhavá. Tenká mikina na zip se dobře větrá a můžete ji uvázat kolem pasu. Bavlněná mikina na delší běh není vhodná, protože nasákne potem.'),
        ('Jak nosit mikinu v zimě?', 'Jako střední vrstvu pod zimní bundu nebo větrovku. Spodní vrstva by měla být funkční, střední teplá a svrchní chránit před větrem a vlhkem. Mikina sama většinou nestačí.'),
        ('Mikina s kapucí, nebo bez?', 'S kapucí je teplejší a praktičtější v chladu a větru, bez ní pohodlnější s batohem, helmou nebo bundou. Pokud mikinu často nosíte pod bundou, může kapuce tlačit na krk.'),
        ('Dají se fleecové mikiny sušit v sušičce?', 'Ne na vysokou teplotu. Fleece se může zdeformovat nebo se vlákna slepí. Lepší je sušit na vzduchu a na nízký stupeň, případně se řídit štítkem v oděvu.'),
        ('Jaké mikiny jsou vhodné pro děti?', 'Pohodlné, odolné materiály, které se dobře perou, bez dlouhých šňůrek u krku a s dostatečně volným střihem. U menších dětí se hodí zapínání na zip, u školáků mikina přes hlavu.'),
    ])
