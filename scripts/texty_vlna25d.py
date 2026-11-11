"""sporteka.cz — wave 25d: long texts for chytre-hodinky, kimona, cyklo-stojany-a-drzaky.
General true facts only, no prices. Brands verified in the catalogue sample."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ chytre-hodinky
NEW['chytre-hodinky'] = dict(long=True,
    title='Chytré hodinky a fitness náramky: jak vybrat a porovnat',
    desc='Chytré hodinky a fitness náramky na sport: GPS, měření tepu, výdrž baterie a kompatibilita. Jak vybrat a porovnat nabídky českých obchodů.',
    intro='<p>Chytré hodinky už dávno nejsou jen prodloužená ruka telefonu. Počítají kroky, měří tep, zaznamenají trasu běhu i spánek a upozorní na příchozí hovor, takže se hodí běžci, cyklistovi, plavci stejně jako člověku, který chce mít přehled o svém denním pohybu. Sporteka porovnává nabídky českých obchodů u chytrých hodinek, fitness náramků, dětských hodinek i náhradních řemínků a nabíjecích kabelů.</p>'
          '<p>V katalogu najdete značky ' + B(('garmin', 'Garmin'), ('huawei', 'Huawei'), ('samsung', 'Samsung'), ('apple', 'Apple'), ('xiaomi', 'Xiaomi'), ('watchmark', 'Watchmark'), ('forever', 'Forever'), ('insportline', 'Insportline'), ('carneo', 'Carneo'), ('maxcom', 'Maxcom')) +
          '. Nadřazená kategorie je <a href="/sportovni-hodinky/">sportovní hodinky a elektronika</a>; pokud hledáte spíše přístroje na kolo, mrkněte i na <a href="/cyklo-computery/">cyklopočítače a navigace</a>.</p>',
    guide='<h2>Chytré hodinky, sportovní hodinky a fitness náramek: v čem je rozdíl</h2>'
          '<p>Názvy se v obchodech míchají, ale za nimi stojí tři různé typy zařízení. Chytré hodinky (anglicky smartwatch) mají obvykle barevný dotykový displej, operační systém a možnost instalovat aplikace. Sportovní hodinky se zaměřují na trénink: podrobné metriky, přesnou GPS a dlouhou výdrž. Fitness náramek je nejjednodušší varianta, malý úzký pásek s displejem, který se soustředí na kroky, tep a spánek.</p>'
          + T(['Typ', 'Co umí nejlépe', 'Pro koho'], [
              ['Chytré hodinky s displejem AMOLED', 'oznámení, platby, aplikace, svižné ovládání', 'každodenní nošení, kancelář i lehký sport'],
              ['Multisportovní hodinky s GPS', 'záznam tras, tréninkové metriky, odolnost', 'běžci, cyklisté, triatlonisté, turisté'],
              ['Fitness náramek', 'kroky, tep, spánek, nízká hmotnost', 'začátečníci a lidé, kterým vadí velké hodinky'],
              ['Dětské chytré hodinky', 'volání, poloha, jednoduché ovládání', 'rodiče školáků a menších dětí'],
              ['Náhradní řemínky a kabely', 'výměna opotřebovaných dílů', 'majitelé stávajících hodinek']]) +
          '<h2>Jak vybrat chytré hodinky podle toho, co s nimi budete dělat</h2>'
          '<p>Než porovnáte konkrétní modely, ujasněte si hlavní účel. Hodinky, které skvěle fungují jako doplněk k telefonu, nemusí být nejlepší volbou pro maraton, a naopak outdoorové kousky bývají hrubší a pomalejší při práci s aplikacemi. Zeptejte se sami sebe na čtyři věci: kde je budete nosit, jaký sport provozujete, jak často jste ochotni dobíjet a jaký telefon používáte.</p>'
          '<ul><li><strong>Běh a chůze:</strong> důležitá je přesná GPS, měření tepu a přehled tempa. Zajímavé jsou i tréninkové plány a doporučená doba odpočinku.</li>'
          '<li><strong>Cyklistika:</strong> hodí se připojení čidel (výkonoměr, snímač kadence) a záznam výškových metrů, případně ukazování trasy.</li>'
          '<li><strong>Plavání:</strong> hledejte vodotěsnost uváděnou v atmosférách nebo metrech a režim plavání v bazénu i na otevřené vodě.</li>'
          '<li><strong>Posilovna a fitness:</strong> důležitý je spolehlivý snímač tepu a možnost zvolit si typ cvičení.</li>'
          '<li><strong>Každodenní nošení:</strong> řešíte hlavně vzhled, pohodlí, výdrž a oznámení z telefonu.</li></ul>'
          '<h2>Na jaké parametry se při výběru dívat</h2>'
          '<h3>Displej</h3>'
          '<p>Displej typu AMOLED má sytější barvy a hluboké černé, ale spotřebuje více energie než displej, který je viditelný na slunci bez podsvícení. Starší a levnější hodinky používají displej LCD. Na slunci se čitelnost liší model od modelu, proto stojí za to přečíst si recenze, kde to někdo vyzkoušel venku. U sportovních hodinek je užitečná možnost nastavit stálé zobrazení času, ovšem za cenu kratší výdrže.</p>'
          '<h3>GPS a navigace</h3>'
          '<p>Pokud chcete mít záznam trasy bez telefonu, hodinky musí mít vlastní GPS. Mnoho modelů podporuje i další družicové systémy, což zlepšuje přesnost v lese nebo mezi vysokými budovami. Levné modely mohou využívat GPS z telefonu, což je pohodlné, ale nutí vás mít telefon u sebe. U trailových a horských hodinek se hodí mapy nebo možnost nahrát trasu a následovat ji.</p>'
          '<h3>Měření tepu a další senzory</h3>'
          '<p>Optický snímač na spodní straně hodinek měří tep přes kůži. Funguje dobře při klidné činnosti, ale při intervalovém tréninku, silném pohybu zápěstí nebo studeném počasí může být méně přesný. Pro seriózní trénink proto sportovci používají hrudní pás, který se spáruje s hodinkami. Mezi další senzory patří měření okysličení krve, barometr, kompas, teploměr a elektrokardiogram. Údaje z nich berte jako orientační ukazatele, nikoli jako lékařské měření; při zdravotních obavách se vždy obraťte na lékaře.</p>'
          '<h3>Výdrž baterie</h3>'
          '<p>Hodinky s pestrým displejem a stálým zapnutím se často dobíjejí každý den nebo po několika dnech. Sportovní modely s úspornějším režimem vydrží i několik týdnů, ale při zapnuté GPS spotřeba prudce stoupne. Výrobci uvádějí hodnoty pro různé režimy, takže porovnávejte stejný režim: běžné nošení, záznam GPS, a případně režim s úsporou. Pamatujte, že baterie časem stárne a výdrž se po letech používání zkracuje.</p>'
          '<h3>Vodotěsnost</h3>'
          '<p>Označení 5 ATM odpovídá odolnosti proti stříkající vodě a plavání v bazénu, vyšší hodnoty snesou náročnější vodní aktivity. U potápění je ovšem potřeba speciální režim a výrobcem uvedená hloubka. Mořskou vodu, sprchy s horkou vodou a sauny hodinky obvykle nemají rády, i když jsou vodotěsné, protože teplo a mýdlo zhoršují těsnění.</p>'
          '<h2>Kompatibilita s telefonem</h2>'
          '<p>Chytré hodinky se spárují s telefonem přes Bluetooth a výrobcovu aplikaci. Hodinky Apple Watch spolupracují jen s iPhonem. Modely se systémem Wear OS od Googlu a Samsungu pracují s telefony s Androidem. Garmin, Huawei, Xiaomi či Polar mají vlastní aplikaci a obvykle fungují s Androidem i iPhonem, ale některé funkce, například odpovědi na zprávy, se mohou lišit podle systému. Před nákupem ověřte, zda váš telefon požadované verzi systému odpovídá.</p>'
          '<h2>Značky v katalogu</h2>'
          '<p>Značka ' + B(('garmin', 'Garmin')) + ' je známá hlavně sportovními a outdoorovými hodinkami s dlouhou výdrží. ' + B(('huawei', 'Huawei')) + ' a ' + B(('xiaomi', 'Xiaomi')) + ' nabízejí pestrý výběr hodinek i náramků pro každodenní nošení. ' + B(('samsung', 'Samsung')) + ' a ' + B(('apple', 'Apple')) + ' míří na uživatele svých telefonů a chytrých ekosystémů. Domácí a regionální značky jako ' + B(('watchmark', 'Watchmark'), ('forever', 'Forever'), ('carneo', 'Carneo'), ('maxcom', 'Maxcom'), ('hama', 'Hama')) + ' se objevují u jednodušších modelů a dětských hodinek, ' + B(('insportline', 'Insportline')) + ' doplňuje nabídku o sportovní modely a náhradní příslušenství a ' + B(('liu-jo', 'Liu Jo')) + ' patří spíše do módní kategorie.</p>'
          '<h2>Dětské chytré hodinky</h2>'
          '<p>Dětské modely se liší od dospělých. Mívají jednoduché ovládání, odolnější tělo a funkce pro rodiče, například volání vybraným kontaktům nebo zobrazení polohy. Mnohé vyžadují vlastní SIM kartu s datovým připojením, takže počítejte s tarifem. Před koupí zkontrolujte, jak výrobce nakládá s daty dítěte, a promluvte si s dítětem o tom, k čemu hodinky slouží. Alternativou jsou hodinky bez volání, které jen měří pohyb a čas.</p>'
          '<h2>Řemínky, kabely a další příslušenství</h2>'
          '<p>Řemínek je nejvíce namáhanou částí. Silikonový je pohodlný při sportu, ale může dráždit kůži při dlouhém nošení v teple. Nylonový je lehký a dobře se pere, kožený působí elegantně, ale nehodí se do vody. Při výměně dbejte na šířku úchytu v milimetrech a na typ uchycení, protože zdaleka ne každý řemínek sedne každému modelu. Stejně tak nabíjecí kabely bývají specifické pro konkrétní řadu hodinek a nelze je zaměňovat bez ověření v návodu.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Kupovat podle počtu funkcí, které nikdy nepoužijete, a ne podle toho, co potřebujete na sport.</li>'
          '<li>Podcenit velikost pouzdra: hodinky s velkým průměrem na tenkém zápěstí vadí při spánku a při cvičení.</li>'
          '<li>Neověřit, zda jsou funkce, které chcete (platby, volání, mapy), dostupné v České republice.</li>'
          '<li>Spoléhat na měření tepu na zápěstí při intervalech bez ověření hrudním pásem.</li>'
          '<li>Zapomenout na cenu příslušenství, jako je řemínek navíc nebo sklo na displej.</li></ul>'
          '<h2>Péče o hodinky a životnost</h2>'
          '<p>Po sportu osušte spodní stranu a očistěte senzor jemným hadříkem, protože pot a krém na ruce zhoršují měření tepu. Řemínek občas umyjte vodou a nechte oschnout. Aktualizujte software, protože výrobci tak opravují chyby a zlepšují přesnost. Baterii nenechávejte dlouho zcela vybitou a nenabíjejte ji na horkém místě. S péčí vydrží hodinky několik let, ale po nějaké době se přestanou aktualizovat a některé funkce vypadnou.</p>'
          '<h2>Jak ušetřit při nákupu chytrých hodinek</h2>'
          '<p>Sporteka sleduje nabídky českých obchodů, takže u každého modelu uvidíte, kde je dostupný a za kolik. Starší generace oblíbených hodinek bývají po uvedení nástupce mnohem výhodnější a pro většinu lidí jsou stále dostatečné. Sledujte sezónní výprodeje, sady s příslušenstvím a rozdíly mezi variantami stejného modelu: základní verze často chybí jen drobnost, například safírové sklo nebo paměť na hudbu. Nezapomeňte na dopravu a lhůtu na vrácení, protože hodinky je dobré několik dní vyzkoušet.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Hodinky doplňte <a href="/behaci-pasy/">běžeckými pásy</a> na domácí trénink, <a href="/rotopedy/">rotopedy</a>, <a href="/celovky-a-svitilny/">čelovkami</a> na večerní běhání a <a href="/batohy/">batohy</a> na trasu. Pro sledování cyklistických výletů vám pomůže také <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>.</p>',
    faq=[
        ('Jaké chytré hodinky vybrat na běhání?',
         'Hledejte hodinky s vlastní GPS, spolehlivým měřením tepu a přehledným zobrazením tempa a vzdálenosti. Pro delší tratě je důležitá i výdrž baterie při zapnuté GPS. Sportovní modely mají obvykle více tréninkových metrik než hodinky zaměřené na každodenní nošení.'),
        ('Jak přesné je měření tepu na zápěstí?',
         'Při klidné činnosti je optické měření obvykle dostatečně přesné pro orientaci. Při intervalovém tréninku, studeném počasí nebo volně nasazeném řemínku se výsledek může lišit. Pro přesnější data použijte hrudní pás, který hodinky podporují.'),
        ('Funguje chytrá hodinka bez telefonu?',
         'Základní funkce jako čas, měření tepu, počítání kroků a u modelů s GPS i záznam tras fungují samostatně. Oznámení, aplikace a synchronizace dat ale vyžadují spárovaný telefon. Hodinky s eSIM nebo SIM kartou mohou volat i bez telefonu.'),
        ('Jaký je rozdíl mezi chytrými hodinkami a fitness náramkem?',
         'Fitness náramek je menší, lehčí a jednodušší, soustředí se na kroky, tep a spánek. Chytré hodinky mají větší displej, více senzorů, často vlastní GPS a možnost instalovat aplikace. Náramek vydrží obvykle déle na jedno nabití.'),
        ('Dají se s chytrými hodinkami plavat?',
         'Mnoho modelů je vodotěsných a má režim plavání, ale je třeba zkontrolovat deklarovanou vodotěsnost a doporučení výrobce. Po plavání v chlóru nebo moři je vhodné hodinky opláchnout čistou vodou. Horké sprchy a sauna jim nesvědčí.'),
        ('Kolik dní vydrží baterie chytrých hodinek?',
         'Záleží na typu displeje, zapnuté GPS a počtu senzorů. Hodinky s displejem AMOLED se dobíjejí častěji, často po několika dnech, sportovní modely s úsporným režimem vydrží i déle. Porovnávejte údaje výrobce vždy pro stejný režim používání.'),
        ('Jak vybrat chytré hodinky pro dítě?',
         'Zvolte model s jednoduchým ovládáním, odolným tělem a funkcemi, které opravdu potřebujete, například voláním nebo polohou. Zjistěte, zda je nutná SIM karta, a přečtěte si zásady ochrany osobních údajů. Dětem je vhodné vysvětlit, k čemu hodinky slouží.'),
        ('Jak vyměnit řemínek na chytrých hodinkách?',
         'Většina hodinek má rychloupínací čepy, takže se řemínek vymění bez nářadí. Při výběru zkontrolujte šířku úchytu v milimetrech a typ uchycení, protože řemínky nejsou zaměnitelné mezi všemi modely. U hodinek bez rychloupínání potřebujete malý šroubovák nebo páčidlo.'),
        ('Zobrazí hodinky oznámení z iPhonu i Androidu?',
         'Většina značek podporuje oba systémy, ale rozsah funkcí se může lišit. Apple Watch spolupracují jen s iPhonem a modely s Wear OS cílí především na telefony s Androidem. Před koupí si ověřte kompatibilitu u konkrétního modelu.'),
    ])

# ------------------------------------------------------------------ kimona
NEW['kimona'] = dict(long=True,
    title='Kimona na judo, karate, jiu-jitsu a taekwondo: výběr',
    desc='Kimona na judo, karate, BJJ a taekwondo pro děti i dospělé. Jak vybrat gramáž, střih, velikost a porovnat nabídky českých obchodů.',
    intro='<p>Kimono je tréninkový oděv bojových umění, který má vydržet tahání, škrcení i časté praní. Judo, karate, brazilské jiu-jitsu a taekwondo mají každé svůj střih a svou tkaninu, takže kimono na judo se na karate nehodí a naopak. Pro dítě, které začíná chodit do kroužku, stačí lehčí a levnější varianta, pro soutěžícího dospělého bývá důležitá pevnost a schválení svazem. Sporteka porovnává nabídky českých obchodů u kimon pro všechna tato umění.</p>'
          '<p>V katalogu najdete značky ' + B(('mizuno', 'Mizuno'), ('bushido-dbx', 'Bushido DBX'), ('kwon', 'Kwon'), ('adidas', 'Adidas'), ('outshock', 'Outshock'), ('danrho', 'Danrho'), ('fighter', 'Fighter'), ('merco', 'Merco'), ('decathlon', 'Decathlon')) +
          '. Nadřazená kategorie je <a href="/obleceni-bojove-sporty/">kimona a oblečení pro bojové sporty</a>, doplnit můžete <a href="/chranice-bojove-sporty/">chrániči</a>.</p>',
    guide='<h2>Jaké kimono vybrat podle bojového umění</h2>'
          '<p>Slovo kimono se v češtině používá obecně pro tréninkový oděv, ačkoli v každém umění má jiný název: judogi, karategi, gi pro jiu-jitsu nebo dobok v taekwondu. Liší se stříhem kabátku, délkou rukávů a kalhot, pevností tkaniny i barvou. Pro vás to znamená jediné pravidlo: koupit kimono určené přesně pro vaše umění a pro to, jak ho trénujete.</p>'
          + T(['Umění', 'Typické vlastnosti kimona', 'Na co se dívat'], [
              ['Judo', 'pevný kabátek, který vydrží tahání za klopy; bílá nebo modrá barva', 'gramáž, výztuha na límci, povolení pro soutěže'],
              ['Brazilské jiu-jitsu (BJJ)', 'přiléhavý střih, pevná tkanina, často vyztužený límec', 'pletení tkaniny, velikost po praní, barva podle pravidel soutěže'],
              ['Karate', 'lehčí a volnější kimono, dlouhé a široké rukávy', 'střih pro volný pohyb, kvalita švů, nižší gramáž'],
              ['Taekwondo (dobok)', 'lehký, volný střih, často s výstřihem do V', 'hladká látka, barva výstřihu podle stupně'],
              ['Aikido a ostatní umění', 'podobné kimonu na judo a karate', 'gramáž a střih podle klubu']]) +
          '<h2>Kimono na judo</h2>'
          '<p>Kimono na judo je určeno pro techniky s chycením soupeře za oděv, takže musí být pevné, aby se nepotrhalo. Kabátek má silný límec a pevně tkané klopy, kalhoty mají zesílená kolena. Pro děti existují lehčí modely, které se snadněji perou a neomezují pohyb. Pokud plánujete závody, ověřte si, zda kimono splňuje pravidla svazu, protože soutěže mohou vyžadovat určitou šířku rukávu a délku kabátku. Barva bývá bílá, často je v nabídce i modrá pro druhého zápasníka.</p>'
          '<h2>Kimono na brazilské jiu-jitsu</h2>'
          '<p>Kimono na brazilské jiu-jitsu (BJJ) má přiléhavější střih než judo, aby se soupeř neměl za co chytit. Kvalita pletení látky a vyztužený límec rozhodují o tom, jak dlouho vydrží. Lehčí tkaniny jsou příjemné v horku a rychle schnou, těžší jsou odolnější, ale tvrdší a teplejší. V obchodech se objevují i uniformy pro děti, které bývají lehčí, aby se v nich dítě pohodlně pohybovalo.</p>'
          '<h2>Kimono na karate</h2>'
          '<p>Karate není zápasem o držení, a proto je kimono lehčí a pohyblivější. Důležitá je volnost v ramenou a v rozkroku a dostatečná délka rukávů, aby se nebortily při úderech. Kimono na karate pro začátečníky má obvykle nižší gramáž, zatímco soutěžní varianty mívají hladší a výraznější materiál. Specifickým stylem je kyokushin, jehož kimono je ze silnější látky s kratším rukávem; pokud trénujete tento styl, hledejte ho v nabídce výslovně.</p>'
          '<h2>Taekwondo kimono (dobok)</h2>'
          '<p>Dobok je lehký oděv s výstřihem do V, širokými kalhotami a hladkou látkou, která umožňuje vysoké kopy. Barva výstřihu a pásku se odvíjí od technického stupně a federace. U doboku si pohlídejte délku kalhot, protože při kopech nesmí překážet. Při soutěži se řídí pravidly federace, takže se před nákupem zeptejte trenéra, jaký model je povolen.</p>'
          '<h2>Gramáž a materiál</h2>'
          '<p>Gramáž se udává v gramech na metr čtvereční a vypovídá o hustotě látky. Čím je vyšší, tím je kimono pevnější a těžší, ale také teplejší a dražší na výrobu. Lehčí kimona okolo 200 až 350 g/m² se hodí pro děti, začátečníky a horká léta. Střední a těžší gramáže v rozmezí kolem 450 až 550 g/m² volí dospělí zápasníci, kteří potřebují pevnost při chycení. Většina kimon je z bavlny nebo směsi s polyesterem; čistá bavlna příjemně savě dýchá, ale při praní se může srazit.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Velikosti kimon se obvykle uvádějí číslem, které odpovídá tělesné výšce v centimetrech. Kimono se po praní často srazí, proto lidé kupují o něco větší, ale zase ne tak velké, aby překáželo. Rukávy by měly končit u zápěstí nebo těsně za ním a kalhoty u kotníku, dokud je nová látka čerstvá. U dětí, které rychle rostou, se vyplatí vybrat jednu velikost navíc a rukávy podvinout, ovšem ne u soutěžních modelů.</p>'
          '<ul><li>Změřte výšku, hmotnost a případně délku rukávu.</li>'
          '<li>Porovnejte údaje s tabulkou konkrétního výrobce, protože se liší.</li>'
          '<li>Počítejte s kratšími kalhotami a rukávy po praní u bavlněných modelů.</li>'
          '<li>U dívek se hodí tričko pod kimono, které si koupíte zvlášť.</li></ul>'
          '<h2>Dětská kimona</h2>'
          '<p>Dětská kimono jsou lehčí a levnější než dospělá, ale pořád musí vydržet časté praní. Při výběru první uniformy se poraďte s trenérem klubu: některé kluby vyžadují bílou barvu nebo nášivku. Děti rychle rostou, proto nevolte předraženou soutěžní variantu, dokud nevíte, že u sportu zůstanou. Pokud dítě trénuje dvakrát týdně, bude kimono potřebovat prát po každém tréninku, takže se hodí mít dvě sady.</p>'
          '<h2>Pásky, doplňky a ochranné pomůcky</h2>'
          '<p>Barevný pásek se kupuje zvlášť a jeho barvu určuje stupeň techniky. Vážete ho podle návodu klubu a při praní ho nenechávejte smotaný v mokré tašce. K tréninku bojových umění patří také <a href="/chranice-bojove-sporty/">chrániče</a>, <a href="/boxerske-rukavice/">rukavice</a> a <a href="/boxovaci-pytle/">boxovací pytle</a> pro doma. Pro dopravu na trénink se hodí <a href="/sportovni-tasky/">sportovní taška</a>, ve které kimono vyschne bez zápachu.</p>'
          '<h2>Značky v katalogu</h2>'
          '<p>Značka ' + B(('mizuno', 'Mizuno')) + ' nabízí kimona na judo a jiu-jitsu pro děti i dospělé. ' + B(('bushido-dbx', 'Bushido DBX'), ('bushido', 'Bushido')) + ' pokrývá judo, jiu-jitsu a karate kyokushin. ' + B(('kwon', 'Kwon')) + ' se zaměřuje na taekwondo a další orientální umění. ' + B(('outshock', 'Outshock'), ('decathlon', 'Decathlon')) + ' cílí na začátečníky a děti, ' + B(('fighter', 'Fighter'), ('merco', 'Merco'), ('danrho', 'Danrho')) + ' nabízejí bojový sortiment a ' + B(('adidas', 'Adidas')) + ' se objevuje u oblečení pro bojové sporty. Při výběru porovnávejte tabulky velikostí a gramáž, protože značky se liší.</p>'
          '<h2>Péče o kimono</h2>'
          '<ul><li>Perte po každém tréninku, aby se nezapařilo a nezačalo zapáchat.</li>'
          '<li>Perte na doporučenou teplotu, protože horká voda urychluje srážení bavlny.</li>'
          '<li>Nepoužívejte aviváž ani bělidla s chlorem, která poškozují vlákna.</li>'
          '<li>Sušte na vzduchu mimo přímé slunce, sušička látku zbytečně smršťuje.</li>'
          '<li>Skvrny a krev ošetřete co nejdříve studenou vodou.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit kimono na špatné umění, například karate místo judo.</li>'
          '<li>Neověřit, zda klub nebo soutěž požaduje konkrétní barvu a střih.</li>'
          '<li>Vybrat příliš velké kimono, které při zápase překáží.</li>'
          '<li>Počítat s tím, že se bavlna nesrazí.</li>'
          '<li>Nechat vlhké kimono v tašce, kde se množí bakterie.</li></ul>'
          '<h2>Jak ušetřit</h2>'
          '<p>Sporteka sleduje nabídky českých obchodů, takže uvidíte, kde je vámi vybrané kimono dostupné. Pro začátečníka je rozumné začít lehčím modelem a teprve po půl roce přejít na těžší. Rodiče dětí mohou využít bazary klubu a výměnu mezi členy. Sledujte také velikosti, které se vyprodávají, protože právě ty bývají zlevněné.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Pokračujte v nadřazené kategorii <a href="/obleceni-bojove-sporty/">kimona a oblečení</a>, v hlavní sekci <a href="/bojove-sporty/">bojové sporty</a>, a také v kategoriích <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/fitness/">fitness a posilování</a>, které se hodí na doplňkový trénink.</p>',
    faq=[
        ('Jaké kimono vybrat na judo pro začátečníka?',
         'Pro začátečníka stačí lehčí až střední gramáž v bílé barvě, která se dobře pere a nebrání pohybu. Poraďte se s trenérem klubu o požadavcích na střih a barvu. Soutěžní modely s vyšší pevností si pořiďte, až budete na zápasy opravdu chodit.'),
        ('Jak se liší kimono na judo a na karate?',
         'Kimono na judo je pevnější a těžší, protože musí vydržet tahání a zápas. Kimono na karate je lehčí a volnější, aby nebránilo úderům a kopům. Střih rukávů a kalhot se v obou případech liší.'),
        ('Co znamená gramáž kimona a jakou zvolit?',
         'Gramáž je hmotnost látky na metr čtvereční. Lehčí kimona do zhruba 350 g/m² se hodí pro děti, začátečníky a horko, těžší kolem 450 až 550 g/m² volí dospělí zápasníci. Čím vyšší gramáž, tím větší pevnost, ale i teplo a hmotnost.'),
        ('Jakou velikost kimona koupit pro dítě?',
         'Velikost se obvykle odvozuje od tělesné výšky v centimetrech. Protože se bavlněná kimona po praní srážejí a děti rostou, volí se mírná rezerva, ale ne příliš velké kimono. Vždy porovnejte údaje s tabulkou výrobce.'),
        ('Srazí se kimono po vyprání?',
         'Bavlněná kimona se mohou srazit, zvláště při vysoké teplotě praní a v sušičce. Dodržujte pokyny výrobce, perte na doporučenou teplotu a sušte na vzduchu. Počítejte s tím, že nové kimono může být po prvním praní o něco kratší.'),
        ('Jaké kimono se hodí na brazilské jiu-jitsu?',
         'Hodí se přiléhavé kimono s pevnou tkaninou a vyztuženým límcem, které se soupeř nesnadno chytí. Lehčí tkanina je příjemná v teple, těžší je odolnější. Pro soutěže zkontrolujte pravidla federace o barvě a střihu.'),
        ('Jak často prát kimono?',
         'Nejlépe po každém tréninku, aby se nezapařilo a nezačalo zapáchat. Hodí se mít druhou sadu na střídání. Používejte vhodný prací prostředek bez chloru a sušte na vzduchu.'),
        ('Mohu na taekwondo použít kimono na judo?',
         'Nedoporučuje se. Dobok na taekwondo je lehčí a volnější, aby umožnil vysoké kopy, kdežto kimono na judo je těžší a pevnější. Klub nebo federace navíc obvykle požadují konkrétní typ oděvu.'),
    ])

# ------------------------------------------------------------------ cyklo-stojany-a-drzaky
NEW['cyklo-stojany-a-drzaky'] = dict(long=True,
    title='Stojany a držáky na kola: nástěnné, zadní, montážní',
    desc='Stojany a držáky na kolo: nástěnné držáky, boční a zadní stojánky, montážní stojany a čelisti. Jak vybrat podle kola, a porovnat obchody.',
    intro='<p>Kolo opřené o zeď brzy skončí na zemi, a navíc zabere víc místa, než byste čekali. Správný stojan nebo držák vyřeší oboje: udrží kolo ve svislé poloze, ochrání lak a pomůže při údržbě. Jsou tu jednoduché stojánky pod zadní kolo, nástěnné držáky do garáže či bytu, montážní stojany pro seřízení a také pomůcky na vyvažování kol. Sporteka porovnává nabídky českých obchodů u všech těchto typů.</p>'
          '<p>V katalogu najdete značky ' + B(('force', 'Force'), ('max1', 'Max1'), ('m-wave', 'M-Wave'), ('rockbros', 'Rockbros'), ('author', 'Author'), ('topeak', 'Topeak'), ('stasdock', 'Stasdock'), ('pedalsport', 'Pedalsport'), ('insportline', 'Insportline'), ('btwin', 'Btwin')) +
          '. Nadřazená kategorie je <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>; na auto kola upevníte <a href="/cyklo-nosice-na-auto/">nosiči kol na auto</a>.</p>',
    guide='<h2>Jaké typy stojanů a držáků na kolo existují</h2>'
          '<p>Pod pojmem stojan na kolo se skrývá několik odlišných pomůcek. Liší se tím, kde kolo drží, jak ho nesou a kolik místa zabírají. Před výběrem proto určete, kde bude kolo stát a co s ním potřebujete dělat: parkovat, vystavit, opravovat nebo uskladnit přes zimu.</p>'
          + T(['Typ', 'Jak funguje', 'Hodí se pro'], [
              ['Nástěnný držák', 'kolo visí za rám, kolo nebo pedál na zdi', 'garáž, byt, chodba, malé prostory'],
              ['Stojánek pod zadní kolo', 'zadní kolo se zasune do držáku na zemi', 'parkování doma, ve sklepě, na zahradě'],
              ['Stojan pod rám nebo dvojitý', 'podpírá spodní část rámu, často s protikusem', 'dětská a menší kola, výstavy'],
              ['Boční stojánek', 'montuje se na kolo a drží ho při zaparkování', 'městská a trekingová kola'],
              ['Montážní stojan', 'zvedne kolo do pohodlné výšky na opravy', 'domácí dílna, servis, seřizování'],
              ['Čelist do svěráku', 'nástěnná nebo stolní fixace rámu nebo sedlovky', 'servisní stolek, dílna'],
              ['Stojan na vyvažování kol', 'ráfek se upne a točí, aby se dal vycentrovat', 'servis kol a opravy ráfků'],
              ['Patrový a vícemístný stojan', 'více kol nad sebou nebo vedle sebe', 'rodina, sklep, firemní parkoviště']]) +
          '<h2>Nástěnné držáky na kolo</h2>'
          '<p>Nástěnný držák šetří podlahu a hodí se všude tam, kde se kola mačkají. Existují varianty, kde kolo visí za přední kolo, za rám nebo za pedál, a sklopné modely, které po sundání kola nepřekážejí. Zeď musí držák unést: do cihly nebo betonu použijte hmoždinky odpovídající váze, do sádrokartonu raději najděte nosný profil. Dávejte pozor na váhu kola, zvláště u e-kol, která jsou výrazně těžší a vyžadují pevnější držák a vždy dva lidi na zavěšení.</p>'
          '<p>Při umístění počítejte s šířkou řídítek a pedálů, aby se kola nedotýkala a nepoškrábala. Několik kol vedle sebe se hodí věšet na střídačku v různých výškách. Patrový držák využije výšku místnosti, ale vyžaduje pevné upevnění.</p>'
          '<h2>Stojánky pod zadní kolo a pod rám</h2>'
          '<p>Tento typ je nejjednodušší a nevyžaduje žádné vrtání. Zadní kolo se zasune do kovové zarážky nebo do vidlice, která ho vede a drží. Pozor na rozsah: stojánky se vyrábějí pro různé průměry kol v palcích, od dětských po 29 palců, a často mají nastavitelné ramena. Při koupi si ověřte i šířku pláště, protože tlustší plášť nemusí do zarážky zapadnout. Pro e-kola jsou k dispozici zesílené verze s označením nosnosti.</p>'
          '<p>Stojan pod rám podpírá kolo za spodní část a bývá doplněn protikusem, který kolo vyvažuje. Je to dobré řešení pro dětská kola nebo pro vystavení v obchodě. U modelů, které se skládají, ušetříte místo při uskladnění.</p>'
          '<h2>Montážní stojany a čelisti pro údržbu</h2>'
          '<p>Pokud si kolo seřizujete sami, ocení se montážní stojan. Kolo se v něm upne za sedlovku nebo rám a zvedne do výšky pasu, takže při práci nemusíte sedat na zem. Skládací varianty se vejdou do auta nebo do skříně. Dbejte na maximální nosnost, kompatibilitu s tvarem rámu (karbonový rám nesnese silné sevření čelisti) a stabilitu při práci. Čelisti určené do svěráku nebo na stůl nabízejí podobnou funkci s menším zástavbovým prostorem.</p>'
          '<p>Další servisní pomůckou je stojan na vyvažování kol, tedy upnutí ráfku pro kontrolu bočního a výškového házení. Hodí se pro ty, kdo si sami zaplétají nebo seřizují kola. Pro základní údržbu využijte kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> a <a href="/cyklo-udrzba/">údržba kola</a>.</p>'
          '<h2>Boční stojánky na městská a trekingová kola</h2>'
          '<p>Boční stojánek se připevňuje k zadní vidlici a zvedne se vedle kola. Hodí se na městská a trekingová kola, kde je kolo často zaparkované u zdi nebo u sloupu. Při výběru dbejte na délku, která odpovídá velikosti kol od 24 do 29 palců. Příliš dlouhý stojánek kolo naklání dopředu, krátký zase dozadu. Nezapomeňte na rozteč děr na vidlici a na uchycení u karbonových rámů, které nesnášejí upínání bez příslušné podložky.</p>'
          '<h2>Držáky, které s kolem nesouvisejí zcela přímo</h2>'
          '<p>V kategorii se objevují i předměty, které na kole jen pomáhají: držáky na hodinky, držáky řídítek ke stojanu nebo stojany na vybavení. Pro telefon a láhve se podívejte do kategorie <a href="/cyklo-lahve-a-drzaky/">lahve, košíky a držáky telefonu</a>. Pokud potřebujete zajistit kolo proti krádeži, vyberte <a href="/cyklo-zamky/">zámek na kolo</a>.</p>'
          '<h2>Jak vybrat stojan podle kola</h2>'
          '<ul><li><strong>Velikost kol:</strong> zkontrolujte rozsah v palcích a šířku pláště.</li>'
          '<li><strong>Typ kola:</strong> horské, silniční, městské a e-kolo mají různé nároky na nosnost a upnutí.</li>'
          '<li><strong>Váha:</strong> u e-kol vybírejte jen modely s udanou vyšší nosností.</li>'
          '<li><strong>Prostor:</strong> změřte šířku a výšku místa, kde bude kolo stát.</li>'
          '<li><strong>Materiál:</strong> hliník je lehký a nerezne, ocel je pevná a levná, ale potřebuje ochranný nátěr.</li>'
          '<li><strong>Využití:</strong> jiné stojany se hodí na parkování, jiné na opravy.</li></ul>'
          '<h2>Značky v katalogu</h2>'
          '<p>Značka ' + B(('force', 'Force')) + ' má nejširší výběr od stojánků a nástěnných držáků po montážní stojany. ' + B(('topeak', 'Topeak'), ('rockbros', 'Rockbros'), ('m-wave', 'M-Wave')) + ' nabízejí kvalitní příslušenství pro cyklisty. ' + B(('author', 'Author'), ('max1', 'Max1'), ('pedalsport', 'Pedalsport')) + ' obsluhují české trhy s dostupnými stojánky a držáky. ' + B(('stasdock', 'Stasdock'), ('nexelo', 'Nexelo'), ('insportline', 'Insportline'), ('btwin', 'Btwin'), ('decathlon', 'Decathlon')) + ' doplňují nabídku o skladné držáky, boční stojánky a modely pro rodiny.</p>'
          '<h2>Montáž a bezpečnost</h2>'
          '<p>U nástěnných držáků používejte vždy hmoždinky vhodné pro daný materiál zdi a nikdy nezavěšujte kolo na držák, který jste nezkontrolovali. Při zavěšování těžkých kol si nechte pomoci. Montážní stojan postavte na rovný a pevný povrch, a těžká kola zabezpečte, aby se nepřevrátila. U dětí dbejte na to, aby si nehrály pod zavěšeným kolem, a pokud kolo skladujete dlouho, vypusťte trochu vzduchu z pláště, aby se předešlo deformacím.</p>'
          '<h2>Skladování kola přes zimu</h2>'
          '<p>Pokud kolo na zimu odložíte, zavěste je na držák nebo postavte na stojan, aby pláště nestály pořád na jednom místě. Předtím kolo omyjte, promažte řetěz a zkontrolujte brzdy. Uložte na suchém místě bez prudkých výkyvů teploty. E-kolo skladujte i s částečně nabitou baterií podle pokynů výrobce, ne prázdnou a ne zcela plnou.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit stojánek, který nesedí na velikost kol nebo šířku pláště.</li>'
          '<li>Zapomenout na nosnost při koupi pro e-kolo.</li>'
          '<li>Nástěnný držák upevnit do slabé zdi bez správné hmoždinky.</li>'
          '<li>Upnout karbonový rám do čelisti bez ochrany.</li>'
          '<li>Podcenit prostor kolem kola, kvůli čemuž se řídítka a pedály o sebe škrábou.</li></ul>'
          '<h2>Jak ušetřit</h2>'
          '<p>Sporteka sleduje nabídky českých obchodů, takže u každého stojanu a držáku uvidíte, kde je dostupný. Jednoduchý stojánek často stačí, a pokud si kolo seřizujete jen občas, nemusíte kupovat profesionální montážní stojan. Sledujte výprodeje na konci sezony a kombinované sady, které ušetří dopravu při nákupu více kusů.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Další příslušenství najdete v kategoriích <a href="/cyklisticke-bryle/">cyklistické brýle</a>, <a href="/cyklo-chranice/">chrániče pro cyklisty</a>, <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>, <a href="/cyklo-svetla/">světla na kolo</a> a <a href="/cyklistika/">cyklistika</a>.</p>',
    faq=[
        ('Jaký stojan na kolo vybrat do bytu nebo garáže?',
         'Do malého prostoru se hodí nástěnný držák, který kolo zvedne ze země. Pokud nechcete vrtat, zvolte stojánek pod zadní kolo. Zkontrolujte rozměry kola, šířku pláště a nosnost.'),
        ('Unese nástěnný držák e-kolo?',
         'Jen pokud má výrobce uvedenou dostatečnou nosnost. E-kola jsou výrazně těžší než běžná kola, proto zvolte zesílený držák s pevným upevněním a zavěšení provádějte ve dvou. Hmoždinky přizpůsobte materiálu zdi.'),
        ('Na jaká kola jsou zadní stojánky?',
         'Zadní stojánky se vyrábějí pro různé velikosti kol, obvykle od dětských po 29 palců, často s nastavitelným ramenem. Ověřte rozsah v palcích a šířku pláště. Pro e-kola vybírejte modely s vyšší nosností.'),
        ('K čemu je montážní stojan na kolo?',
         'Montážní stojan zvedne kolo do pohodlné výšky a pevně ho drží při seřizování, čištění a opravách. Kolo se upne za sedlovku nebo rám. Dbejte na nosnost a opatrnost u karbonových rámů.'),
        ('Dá se kolo upnout do čelisti i s karbonovým rámem?',
         'Karbonový rám je citlivý na silné sevření, proto se upíná raději za sedlovku nebo se používá ochranná podložka. Řiďte se pokyny výrobce rámu i stojanu. Při pochybnostech konzultujte servis.'),
        ('Jaký je rozdíl mezi stojánkem pod rám a pod zadní kolo?',
         'Stojan pod rám podpírá spodní část rámu, často doplněný protikusem pro rovnováhu. Stojánek pod zadní kolo drží zadní kolo v zarážce. Druhý typ je běžnější u dospělých kol, první se hodí i pro dětská kola.'),
        ('Jak vybrat boční stojánek na městské kolo?',
         'Určující je velikost kol v palcích, délka stojánku a rozteč děr na vidlici. Příliš dlouhý kolo nakloní dopředu, krátký dozadu. U karbonových rámů se používají jen schválená uchycení.'),
        ('Jak uložit kolo přes zimu?',
         'Kolo omyjte, promažte řetěz a zavěste ho nebo postavte na stojan na suchém místě. Pláště tak nestojí stále na jednom bodě. U e-kol dodržujte doporučení výrobce ohledně nabití baterie.'),
    ])

NEW['kimona']['guide'] += ('<h2>Jak kimono poznat kvalitní</h2>'
    '<p>Kvalitní kimono poznáte podle rovných a hustých švů, zesílených míst na loktech, kolenou a v rozkroku a pevného límce, který se nepoddává při tahu. Zkontrolujte, zda látka nepropouští světlo a zda se šněrování kalhot nebo pas nepřetáčí. U levných modelů se nejčastěji trhají švy v podpaží, proto si je prohlédněte hned po vybalení. Pokud je kimono určeno pro soutěže, ověřte i štítek s potvrzením od svazu a vyzkoušejte si pohyb v plné šíři, než odstřihnete cedulky.</p>'
    '<p>Dobré je také zeptat se spolucvičících, jak jim vydrželo jejich kimono po roce pravidelného tréninku. Zkušenost z klubu je často cennější než popis výrobce.</p>')
NEW['cyklo-stojany-a-drzaky']['guide'] += ('<h2>Stojany pro více kol a rodiny</h2>'
    '<p>Pokud v domácnosti jezdí více lidí, vyplatí se přemýšlet o vícemístném řešení. Patrový držák ušetří šířku, ale vyžaduje, aby měl někdo sílu zvednout kolo do horního patra. Podlahový stojan na více kol zabere víc půdorysu, ale kola se vyjímají snadno. Dětská kola mohou stát v nízkých stojáncích, aby si je děti odkládaly samy. Před nákupem si rozmyslete pořadí kol, hlavně u dlouhých řídítek, a nechte mezi nimi aspoň ruku volného místa, aby se nepoškrábaly pedály ani lak.</p>')
NEW['kimona']['faq'].append(('Jak poznat kvalitní kimono?',
    'Všímejte si hustých a rovných švů, zesílených míst na kolenou a loktech a pevného límce. Látka by neměla být průsvitná. Informace o zkušenostech s trvanlivostí vám může dát i trenér nebo spolucvičící v klubu.'))
NEW['cyklo-stojany-a-drzaky']['faq'].append(('Jak postavit stojan pro více kol v domácnosti?',
    'Zvolte patrový nebo podlahový stojan podle prostoru a ověřte nosnost každého místa. Mezi koly nechte rezervu, aby se nepoškrábaly řídítka a pedály. Pro děti se hodí nižší stojánky, do kterých kolo odloží samy.'))
