"""sporteka.cz — wave 21b (4. 11. 2026): long texts (>= 1650 words) for energeticke-gely-a-tycinky, basketbalove-mice, bezecke-lyze, obuv-do-vody.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ energeticke-gely-a-tycinky
NEW['energeticke-gely-a-tycinky'] = dict(long=True,
    title='Energetické gely, tyčinky a ovesné kaše pro sportovce',
    desc='Energetické gely, tyčinky a ovesné kaše na běh, kolo i túry. Jak vybrat formu, chuť a balení a porovnat nabídky českých e-shopů na jednom místě.',
    intro='<p>Kdo se pohybuje déle než hodinu, často narazí na praktický problém: jak si vzít jídlo, které se vejde do kapsy, nerozpadne se v batohu a dá se spolknout za běhu. '
          'Právě na to jsou určené gely v sáčku, tuhé tyčinky, kaše do kelímku nebo vločky, které se zalijí vodou. Každá forma funguje jinak, liší se konzistencí, množstvím vody k zapití i tím, jak dobře se snáší při pohybu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u produktů značek GymBeam, Nutrend, Isostar, Powerbar, Enervit, Bombus nebo Penco. '
          'K tématu se hodí také <a href="/iontove-napoje/">iontové nápoje</a>, <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>, <a href="/outdoorova-strava/">outdoorová strava</a> a <a href="/sportovni-vyziva/">sportovní výživa</a>. '
          'Níže najdete přehled forem, rady pro výběr podle sportu a tipy, jak si nové produkty vyzkoušet dřív než na závodě.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Název kategorie slibuje gely a tyčinky, ale nabídka je širší. Vedle klasických gelových sáčků tu jsou tyčinky z ovesných vloček, datlí a ořechů, měkké žvýkací kostky, instantní ovesné kaše v kelímku i vločky na přípravu s horkou či studenou vodou. '
          'Společné mají to, že jsou určeny pro rychlé doplnění sacharidů a kalorií během pohybu nebo před ním. Kolik jich opravdu potřebujete, záleží na délce, intenzitě a vaší zkušenosti, proto u každého výrobce sledujte údaje na obalu.</p>'
          + T(['Forma', 'Konzistence', 'Hodí se hlavně'], [
              ['Gel v sáčku', 'hustá nebo tekutá pasta, rychle se polyká', 'běh, kolo, závody, kde není čas žvýkat'],
              ['Tyčinka', 'pevná nebo měkká, nutné žvýkat', 'turistika, cyklistika, delší výlety'],
              ['Žvýkací kostky', 'gumová konzistence v malých kusech', 'kdo nechce lepkavý gel'],
              ['Ovesná kaše', 'instantní směs, zalévá se vodou', 'snídaně před výkonem, kemping, outdoor'],
              ['Vločky a směsi', 'sypký základ k domácí úpravě', 'příprava doma, vlastní kombinace'],
          ]) +
          '<h2>Gely, tyčinky nebo kaše: čím se liší</h2>'
          '<h3>Gely</h3>'
          '<p>Gel je nejkompaktnější způsob, jak s sebou vzít energii. Sáček váží několik desítek gramů, vejde se do kapsy dresu a po otevření ho spolknete během pár sekund. '
          'Některé gely jsou hustší a vyžadují zapít vodou, jiné jsou řidší a snesou se i bez ní. Výrobci často nabízejí variantu s kofeinem nebo s elektrolyty, která je jasně označená na obalu. '
          'Pokud gel nikdy nezkusíte předem, může vás na trati zaskočit chuť nebo konzistence, kterou nezvládnete.</p>'
          '<h3>Tyčinky</h3>'
          '<p>Tyčinka se žvýká, a proto se hodí tam, kde máte klidnější tempo. Na túře nebo při vyjížďce na kole zvládnete ukousnout po kouscích a zapít vodou. '
          'Složení se liší: jedny jsou ovocné s datlemi, jiné ovesné, další s ořechy nebo čokoládou. Rozdílné je i to, zda jsou měkké, nebo tvrdé; v zimě se tvrdé tyčinky stávají téměř nepoživatelné a v létě může čokoláda v kapse změknout.</p>'
          '<h3>Ovesné kaše a vločky</h3>'
          '<p>Instantní kaše je spíš jídlo než svačina na trasu. V kategorii jsou kaše příchutí kakao, kokos, jahoda nebo borůvky a objemná balení vloček. '
          'Hodí se na snídani před náročným dnem, na výlety s vařičem nebo na kemping, kde chcete teplé jídlo s minimem přípravy. Zalijí se horkou vodou, některé varianty i studenou, a po pár minutách jsou hotové.</p>'
          '<h2>Jak vybrat podle sportu</h2>'
          '<p>Při běhu chcete něco, co se nezadrhne v krku a nenarušuje rytmus dechu. Běžci proto sahají po gelech nebo měkkých žvýkacích kostkách, které se dají spolknout bez zastavení. '
          'U silničního běhu a maratonu se obvykle počítá s doplňováním podle času, proto se hodí zkoušet různé značky v tréninku. Na stezkách v horách je praktičtější mít kombinaci tyčinky a gelu, protože tempo se mění podle sklonu.</p>'
          '<p>Cyklisté mají výhodu, že jim na kole hodně věcí vydrží v kapsách dresu i v rámové brašně. Dlouhé vyjížďky snesou i objemnější tyčinky a ovesné kaše se hodí na večer před výjezdem. '
          'K ruce se vyplatí mít také <a href="/cyklo-lahve-a-drzaky/">cyklistické lahve a držáky</a> a při plánování nezapomeňte, že energii je třeba zapít, ne jen pozřít.</p>'
          '<p>Turistům a lidem v přírodě vyhovují tyčinky a kaše, které se nerozpadají v batohu a nepotřebují chlazení. U vícedenních túr je důležitá i hmotnost, takže srovnávejte gramáž s počtem porcí. '
          'Na výlety s vařením se vyplatí zahrnout i položky z <a href="/vareni-v-prirode/">vaření v přírodě</a> a z kategorie <a href="/outdoorova-strava/">outdoorová strava</a>.</p>'
          '<h2>Na co se dívat na obalu</h2>'
          '<p>Obal vám řekne víc než reklama. Vždy zkontrolujte hmotnost porce, počet kusů v balení a doporučený způsob použití. Pokud jde o balení po šesti nebo dvaceti kusech, přepočtěte si cenu na porci a porovnejte ji u různých obchodů. '
          'Dále sledujte, zda je produkt vegetariánský nebo veganský, pokud to pro vás něco znamená, a zda neobsahuje alergeny jako ořechy, mléko nebo lepek. Výrobci je na obalu zvýrazňují.</p>'
          '<ul><li><strong>Hmotnost a počet porcí:</strong> porovnávejte gramy a kusy, ne jen velikost balení.</li>'
          '<li><strong>Příchuť:</strong> sladké varianty se po hodině mohou zprotivit, proto se vyplatí mít i neutrálnější nebo kyselejší chuť.</li>'
          '<li><strong>Alergeny:</strong> čtěte tučně vyznačené složky, zejména u tyčinek s ořechy.</li>'
          '<li><strong>Trvanlivost:</strong> u zásob pro celou sezónu ověřte datum minimální trvanlivosti.</li>'
          '<li><strong>Obal:</strong> sáček s odtrhovacím okrajem se otevírá snáz než obal, který potřebuje nůžky.</li></ul>'
          '<h2>Jak si produkty vyzkoušet</h2>'
          '<p>Základní pravidlo zní: na závod nebo důležitý výlet nebrat nic, co jste nikdy nejedli. Žaludek reaguje na pohyb jinak než v klidu a zkoušení nové značky na trati je zbytečné riziko. '
          'Koupit si proto několik kusů od různých značek, vyzkoušet je na tréninku a až pak objednat větší balení, se vyplatí. Kdo nechce utratit hodně, může začít menšími balíčky nebo mix sadami, které nabízí řada výrobců.</p>'
          '<p>Při testování si poznamenejte, jak dlouho po pozření vám bylo dobře, jestli jste museli hned zapít a jestli vám chuť nezačala vadit. '
          'Po delší době se u řady lidí objeví odpor ke sladkému a pak se hodí slanější tyčinky nebo ovesné kaše se solí. Žádná z těchto poznámek není lékařská rada, jde o zkušenosti sportovců, které lze ověřit na vlastním těle.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Kupování velkého balení jedné příchuti bez zkoušky.</li>'
          '<li>Nepočítání s tím, že gel potřebuje vodu, a nebrat si ji.</li>'
          '<li>Nošení tyčinek s čokoládou v horku, kde se v kapse rozpustí.</li>'
          '<li>Srovnávání jen podle celkové ceny balení bez přepočtu na porci.</li>'
          '<li>Zapomenutí na odpadky: prázdné sáčky patří zpět do kapsy, ne do přírody.</li></ul>'
          '<h2>Jak plánovat energii na dlouhou trasu</h2>'
          '<p>Praktický plán začíná tím, že si rozdělíte trasu na úseky. Gel nebo kousek tyčinky si naplánujte například na místa, kde stoupáte pomaleji nebo kde víte, že budete mít po ruce vodu. Díky tomu nebudete uprostřed prudkého kopce hledat sáček v zadní kapse. '
          'Na dlouhých závodech organizátoři často rozmísťují občerstvovací stanice a je dobré vědět, jaké produkty tam mají, abyste si nemuseli vozit všechno s sebou.</p>'
          '<p>Při kratších trasách do hodiny většinou žádné doplňování neřešíte, a pokud ano, stačí malá tyčinka nebo pár soust. Důležité je umět rozlišit hlad od krátkodobé únavy; vlastní zkušenost vás naučí nejvíc, proto si po každé trase poznamenávejte, co jste jedli a jak jste se cítili.</p>'
          '<h2>Značky v kategorii</h2>'
          f'<p>Největší výběr mají na Sportece značky {B(("gymbeam", "GymBeam"), ("decathlon", "Decathlon"), ("penco", "Penco"), ("nutrend", "Nutrend"), ("bombus", "Bombus"), ("isostar", "Isostar"), ("powerbar", "Powerbar"), ("enervit", "Enervit"))}. '
          'Najdete také menší značky jako LYOfood, Food Force, Mixit nebo Extrifit. Každý výrobce má vlastní chutě, texturu i velikost porcí, takže porovnání jedné značky nestačí k určení nejlepší volby pro vás.</p>'
          '<h2>Doplňkové kategorie</h2>'
          '<p>Energie je jen část příprav. Pokud plánujete delší trasu, zvažte i <a href="/iontove-napoje/">iontové nápoje</a> na pití, <a href="/lahve-a-termosky/">lahve a termosky</a> na nošení vody, '
          '<a href="/bezecke-opasky/">běžecké opasky</a> nebo <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a> na uložení gelů. Pro regeneraci po výkonu se hodí <a href="/proteiny/">proteiny</a> a <a href="/kreatin/">kreatin</a>, ale ty patří do jiného okruhu a řeší se zvlášť.</p>'
          '<h2>Pro koho se hodí které produkty</h2>'
          + T(['Typ sportovce', 'Praktická volba', 'Poznámka'], [
              ['Začínající běžec', 'jedna tyčinka nebo gel na zkoušku', 'nejdřív v tréninku, až pak na závodě'],
              ['Maratonec', 'gely ve více příchutích, měkké kostky', 'plánujte podle času, ne podle hladu'],
              ['Cyklista na dlouhé trasy', 'tyčinky a gely střídavě', 'zapíjejte hned po pozření'],
              ['Turista na víkend', 'tyčinky, ovesná kaše na snídani', 'sledujte gramáž a obal'],
              ['Horolezec nebo horský běžec', 'lehké a pevné obaly, snadné otevírání', 'v mrazu tvrdnou tyčinky, vezměte měkčí'],
              ['Pro snídani před výkonem', 'instantní ovesná kaše', 'zalít vodou, připravit s předstihem'],
          ]) +
          '<h2>Skladování a přeprava</h2>'
          '<p>Sáčky a tyčinky skladujte na suchém místě bez přímého slunce. Gely v kapse na slunci se zahřejí a někdy se stanou řidšími a lepivějšími. V létě proto vybírejte tyčinky bez čokoládové polevy nebo je ukládejte do vnitřní kapsy batohu. '
          'Ovesné kaše v kelímku jsou objemnější, takže se hodí do auta nebo na kemp, ne do kapes dresu.</p>'
          '<p>Při cestování letadlem platí běžná pravidla pro tekutiny v příručním zavazadle. Gely ve větších balení jsou formálně tekutina, takže si ověřte aktuální limity letecké společnosti, než je zabalíte. Tuhé tyčinky a sypké směsi problémy většinou nedělají.</p>'
          '<h2>Jak na Sportece nakupovat</h2>'
          '<p>U každého produktu vidíte nabídky více českých obchodů najednou, včetně aktuální dostupnosti a přibližné ceny za kus. Přepněte řazení podle ceny nebo slev a porovnejte, jak se liší balení po jednom kusu a po větších množstvích. '
          'Pokud si nejste jistí, otevřete detail a podívejte se na fotku obalu s tabulkou složení; většina obchodů ji u produktu uvádí. Doprava a podmínky se liší obchod od obchodu, proto je ověřte až v košíku vybraného obchodu.</p>',
    faq=[
        ('Kdy sáhnout po energetickém gelu a kdy po tyčince?', 'Gel se hodí tam, kde nemáte čas ani chuť žvýkat, tedy při běhu a závodech. Tyčinka je pohodlnější při klidnějším tempu, třeba na túře nebo při vyjížďce na kole.'),
        ('Musím gel zapít vodou?', 'U hustších gelů je zapití vodou obvykle doporučené výrobcem, řidší varianty se snesou i bez něj. Postup najdete na obalu konkrétního produktu a vyzkoušejte si ho předem v tréninku.'),
        ('Co znamená gel s kofeinem na obalu?', 'Je to varianta, kterou výrobce označuje obsahem kofeinu. Pokud kofein nechcete nebo ho nesnášíte, vybírejte gely bez něj a obal čtěte pozorně.'),
        ('Jsou tyčinky vhodné pro vegany?', 'Část tyčinek je rostlinná a výrobce to uvádí na obalu. Vždy zkontrolujte složení, protože ani jedna značka nemá všechny produkty ve stejné variantě.'),
        ('Dá se ovesná kaše připravit v horách?', 'Ano, instantní kaše se obvykle zalévá horkou vodou a po několika minutách je hotová. Stačí vařič nebo termoska s vodou a lžíce, takže se hodí na chaty i do stanu.'),
        ('Jak dlouho vydrží gely a tyčinky?', 'Na obalu je vytištěné datum minimální trvanlivosti. Při skladování v suchu a chladu vydrží do tohoto data; po otevření je lepší sníst celý kus hned.'),
        ('Může gel vyvolat žaludeční potíže?', 'Reakce na jídlo za pohybu je individuální a u některých lidí se objeví nepříjemné pocity. Proto se doporučuje novinky zkoušet v tréninku, ne na závodě, a při opakovaných potížích poradit se s lékařem.'),
        ('Mohu si tyčinky vozit v letadle?', 'Pevné tyčinky bývají v příručním zavazadle bez problémů. U gelů v bublinách nebo větších sáčcích si ověřte aktuální pravidla pro tekutiny u letecké společnosti.'),
        ('Čím se liší tyčinka od proteinové tyčinky?', 'Energetická tyčinka má sloužit jako zdroj sacharidů při pohybu, proteinová se tradičně vybírá po tréninku nebo jako svačina. Rozdíl poznáte podle složení na obalu a také podle toho, do které kategorie je produkt zařazen.'),
        ('Jak poznám, že jsou ceny v obchodech srovnatelné?', 'Ověřte hmotnost jedné porce a počet kusů v balení, pak si cenu přepočtěte na porci. Sporteka u produktu ukazuje nabídky více obchodů vedle sebe, takže rozdíl vidíte hned.'),
        ('Je lepší koupit jedno velké balení, nebo více příchutí?', 'Pro první nákup se vyplatí menší sada s různými příchutěmi. Velké balení dává smysl, až když víte, která chuť a konzistence vám vyhovuje.'),
    ])

# ------------------------------------------------------------------ basketbalove-mice
NEW['basketbalove-mice'] = dict(long=True,
    title='Basketbalové míče a koše: velikosti, povrch, montáž',
    desc='Basketbalové míče, koše, desky a síťky. Jak vybrat velikost, povrch, indoor nebo outdoor a porovnat nabídky českých obchodů na jednom místě.',
    intro='<p>Dobrý basketbalový míč poznáte po první hodině hry: drží v prstech, odráží se předvídatelně a po dopadu na asfalt se nerozpadne. Špatný vás naopak naučí mrštit zbytečně silně a trefovat jen náhodně. '
          'Kategorie spojuje míče pro halu i venkovní hřiště, mini míčky pro děti, koše na stěnu či stojan, desky, obruče a náhradní síťky, takže na jednom místě pokryje celou výbavu pro hru doma i v klubu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Spalding, Nike, Wilson, Molten, Kipsta, Jordan, Master nebo Insportline. '
          'K výběru se hodí také <a href="/basketbalova-obuv/">basketbalová obuv</a>, <a href="/basketbal/">basketbal</a>, <a href="/micove-sporty/">míčové sporty</a>, <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/hry-na-zahradu/">hry na zahradu</a>. '
          'Níže najdete přehled velikostí, povrchů a typů košů i rady pro montáž a péči.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Základem jsou míče, ale kategorie nekončí u nich. Najdete tu míče různých velikostí, mini míčky na sběratelské a dětské hraní, koše na zeď i mobilní stojany, samostatné obruče a desky, '
          'závěsné držáky, síťky ze šňůry nebo řetězu a pumpičky s jehlami. Sezónu otevírá většinou nákup míče, a pokud hrajete na zahradě, přidá se koš s deskou.</p>'
          + T(['Produkt', 'K čemu slouží', 'Na co se zaměřit'], [
              ['Míč', 'hra, trénink, driblink', 'velikost, povrch, indoor nebo outdoor'],
              ['Mini míč', 'dětské hraní, sběratelství, dárky', 'velikost, motiv, pevnost'],
              ['Koš se stojanem', 'zahrada, dvůr, garáž', 'nastavitelná výška, stabilita, základna'],
              ['Obruč a deska', 'montáž na zeď nebo konstrukci', 'rozměr, uchycení, materiál'],
              ['Síťka', 'výměna po opotřebení', 'délka, počet ok, šňůra nebo řetěz'],
              ['Pumpička a jehly', 'dofukování, údržba tlaku', 'kompatibilita s ventilem, přenosnost'],
          ]) +
          '<h2>Velikosti míčů</h2>'
          '<p>Basketbalové míče se vyrábějí ve velikostech 3, 5, 6 a 7. Velikost 7 má obvod kolem 75 centimetrů a hraje se s ní v mužských soutěžích, velikost 6 je určená pro ženy a starší dívky, velikost 5 je pro mladší děti a mini míčky ve velikosti 3 slouží spíš jako hračka nebo suvenýr. '
          'Přesné rozměry a věkové hranice se mohou lišit podle organizace, takže si před nákupem pro klub nebo školu ověřte pravidla soutěže.</p>'
          '<p>Nejčastější chybou rodičů je koupit dítěti míč „na vyrůstání“. Příliš velký míč se špatně drží, nutí hráče házet silou paží místo celým tělem a zbytečně zhoršuje techniku. Správný míč pro věk je ten, který dítě udrží jednou rukou a zvládne s ním driblovat bez únavy.</p>'
          '<h2>Povrch: kůže, kompozit a guma</h2>'
          '<p>Povrch rozhoduje, kde míč vydrží. Kožený nebo kompozitní míč je určen do haly: má lepší úchop a citlivější odskok, ale na hrubém betonu se rychle obrušuje. '
          'Gumový míč se hodí na asfalt a beton, protože snáší drsný povrch a nebojí se vlhka. Mezi nimi stojí kompozitní míče označené jako indoor/outdoor, které slibují kompromis a pro rekreační hru mají nejlepší poměr univerzálnosti a odolnosti.</p>'
          + T(['Povrch', 'Hlavní prostředí', 'Výhody', 'Omezení'], [
              ['Přírodní kůže', 'hala', 'výborný úchop, citlivý odskok', 'rychlé opotřebení venku'],
              ['Kompozit', 'hala, někdy i venku', 'dobrý úchop, nižší nároky na péči', 'na hrubém povrchu se obrušuje'],
              ['Guma', 'venkovní hřiště', 'odolnost, nižší nároky', 'méně citlivý odskok, tvrdší dotyk'],
          ]) +
          '<h2>Indoor, outdoor nebo univerzální</h2>'
          '<p>Hraje-li se většinou v hale, je rozumné pořídit samostatný halový míč a venku používat jiný. Hráči, kteří hrají ve škole i na hřišti, často skončí u univerzálního modelu, který nic nedělá dokonale, ale vyhoví všude. '
          'Jedno pravidlo ovšem platí napříč: na prašném a vlhkém hřišti se každý míč zhoršuje rychleji než v hale, takže je dobré míč občas otřít vlhkým hadříkem.</p>'
          '<h2>Koše, desky a obruče</h2>'
          '<p>Pro hru na zahradě se prodávají koše na stojanu s nastavitelnou výškou, které dobře poslouží dětem i dospělým. Výška obruče v soutěžním basketbalu je 3,05 metru a průměr obruče je 45 centimetrů; nastavitelné koše umožňují začít níž a pomalu růst. '
          'U stojanů zkontrolujte, jak se zajišťuje stabilita: základna se plní vodou nebo pískem, jiné modely se kotví do země. Lehký koš bez dostatečné zátěže se při opření nebo úderu snadno převrhne.</p>'
          '<h3>Montáž na zeď</h3>'
          '<p>Chcete-li koš na zeď nebo garáž, počítejte s pevným podkladem, ne s lehkým obkladem. Obruč s deskou má váhu a při namáhání (zavěšení hráče) působí velké síly. '
          'Používejte kotvy vhodné pro materiál stěny a vždy dodržujte pokyny výrobce. Pokud si nejste jistí, požádejte o pomoc odborníka, protože chyba při montáži může skončit zraněním.</p>'
          '<h3>Pružné a pevné obruče</h3>'
          '<p>Pevná obruč je jednodušší a levnější na údržbu, pružná obruč (s pérem) snese víc úderů a méně namáhá desku při zakončení po dunku. Výrobci často nabízejí obě verze, takže při výběru zvažte, zda budete skákat k obruči, nebo střílet z místa.</p>'
          '<h2>Síťky a doplňky</h2>'
          '<p>Síťka je spotřební zboží, které se na venkovním hřišti ničí nejrychleji. Nylonová šňůra je lehká a tichá, řetězová síť vydrží roky, ale při zásahu zazvoní a těžší řetízky mohou namáhat obruč. '
          'Před nákupem si zjistěte, kolik oček má vaše obruč (obvykle 12) a jak se síť zavěšuje. Pumpa s jehlou je další nezbytnost, protože míč s nízkým tlakem se špatně odráží a snadněji se poškodí.</p>'
          '<h2>Jak hustit a jak pečovat</h2>'
          '<ul><li><strong>Tlak:</strong> správnou hodnotu najdete na míči u ventilku nebo v návodu. Přehuštěný míč se nadměrně odráží a může popraskat, podhuštěný ztrácí odskok.</li>'
          '<li><strong>Ventilek:</strong> před hustěním jehlu navlhčete vodou nebo glycerinem, aby snadno vklouzla a nepoškodila ventilek.</li>'
          '<li><strong>Čištění:</strong> otřete vlhkým hadříkem bez agresivní chemie, nevhazujte do pračky.</li>'
          '<li><strong>Skladování:</strong> mimo radiátory, mráz a přímé slunce, kde se povrch zhoršuje.</li>'
          '<li><strong>Zahřátí:</strong> v zimě nechte míč před hrou chvíli v teple, ztuhlá guma se odráží hůř.</li></ul>'
          '<h2>Jak vybrat podle věku a úrovně</h2>'
          + T(['Hráč', 'Velikost a typ', 'Doplněk'], [
              ['Předškolní dítě', 'velikost 3 nebo malý koš', 'nízký stojan, měkká síťka'],
              ['Školák 6 až 11 let', 'velikost 5', 'nastavitelný koš, pumpa'],
              ['Starší žákyně', 'velikost 6', 'indoor/outdoor míč podle prostředí'],
              ['Dospívající a dospělí muži', 'velikost 7', 'kvalitnější povrch, pevná obruč'],
              ['Hráč v klubu', 'halový míč dle pravidel soutěže', 'sada míčů, taška na míče'],
              ['Majitel zahrady', 'gumový nebo indoor/outdoor míč', 'koš se stojanem, zátěž na základnu'],
          ]) +
          '<h2>Co pro začátek</h2>'
          '<p>Začínáte-li na hřišti za domem, stačí pevný gumový míč velikosti 5 nebo 7 podle věku a pumpa. Pokud hrajete každý týden v tělocvičně, vyplatí se investovat do kvalitnějšího povrchu a nepoužívat ho venku. '
          'Pro rodinu s dětmi dává smysl koš s nastavitelnou výškou, aby si s ním užili malí i velcí. Malé děti ocení měkčí míče a nízký koš, aby jim hra přinesla úspěch hned a nezačali ji považovat za obtížnou.</p>'
          '<h2>Basketbalová výbava kolem míče</h2>'
          '<p>Míč je jen začátek. Dobře padnoucí <a href="/basketbalova-obuv/">basketbalová obuv</a> chrání kotníky při doskocích, <a href="/sportovni-ponozky/">sportovní ponožky</a> snižují riziko puchýřů, a <a href="/sportovni-kratasy/">sportovní kraťasy</a> s <a href="/sportovni-tricka/">sportovními tričky</a> usnadní pohyb. '
          'Do tašky patří i <a href="/lahve-a-termosky/">láhev na vodu</a> a pro tréninky v zimě <a href="/mikiny/">mikina</a>. Pokud trénujete s dětmi, přidejte <a href="/chranice-a-helmy/">chrániče</a> na kolena a zápěstí, které nejsou povinné, ale zmírní následky pádů.</p>'
          '<h2>Kdy míč vyměnit</h2>'
          '<p>Míč je pro výměnu zralý, když je povrch hladký jako dlaň a rýhy (drážky) zmizí. Jakmile povrch vypadá obroušeně, míč neudrží prsty a každý dribling je nejistý. '
          'Dalším signálem je trvale nízký tlak i po dohuštění: znamená to netěsný ventilek nebo prasklou vnitřní komoru. Málokdy se vyplatí opravovat míče domácími prostředky, protože výsledek většinou nevydrží.</p>'
          '<p>Pro školní nebo klubové použití se hodí mít v zásobě několik míčů a střídat je, aby se opotřebení rozložilo. Sady míčů v tašce usnadňují i trénink, kdy hráči používají míče současně a nemusí čekat.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší zastoupení mají {B(("spalding", "Spalding"), ("nike", "Nike"), ("wilson", "Wilson"), ("kipsta", "Kipsta"), ("molten", "Molten"), ("master", "Master"), ("powershot", "Powershot"), ("insportline", "Insportline"), ("nils", "Nils"), ("hudora", "Hudora"), ("jordan", "Jordan"))}. '
          'Spalding a Wilson jsou spojeny s oficiálními ligovými míči, Molten patří mezi tradiční značky halových míčů, Kipsta je vlastní sportovní značka Decathlonu a Powershot, Nils nebo Insportline se zaměřují na koše a doplňky. '
          'Rozdíly mezi značkami jsou hlavně v povrchu, vnitřní konstrukci a v tom, jak se míč chová po několika měsících používání.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupit halový míč na asfalt a divit se, že po měsíci vypadá jako po válce.</li>'
          '<li>Vybrat příliš velký míč pro dítě „na vyrůstání“.</li>'
          '<li>Podcenit zátěž stojanu a nechat koš stát prázdný na větru.</li>'
          '<li>Zapomenout na jehlu a pumpu, bez nichž se míč po týdnu přestane odrážet.</li>'
          '<li>Montovat obruč na slabou stěnu bez ověření kotvení.</li></ul>'
          '<h2>Jak vám pomůže Sporteka</h2>'
          '<p>U každého míče nebo koše vidíte nabídky více českých obchodů a aktuální dostupnost. Filtrujte podle značky a řaďte podle ceny nebo slevy. '
          'Při srovnávání se dívejte na úplný název produktu, protože se u stejné řady míčů liší velikosti a povrchy. Před objednávkou si ověřte velikost 5, 6 nebo 7, protože změna po doručení bývá zdlouhavá.</p>',
    faq=[
        ('Jakou velikost basketbalového míče potřebuji?', 'Muži a starší chlapci hrají s velikostí 7, ženy a starší dívky s velikostí 6, mladší děti s velikostí 5. Velikost 3 je spíš pro nejmenší a sběratele. U soutěží ověřte pravidla organizace.'),
        ('Rozdíl mezi indoor a outdoor míčem?', 'Indoor míč je určen do haly, má citlivější povrch, ale rychle se obrušuje na betonu. Outdoor míč má odolnější povrch, který snáší asfalt, vlhko i nečistoty.'),
        ('Dá se halový míč použít venku?', 'Dá, ale povrch se výrazně rychleji opotřebuje a míč ztratí úchop. Pokud hrajete na obou místech, vyplatí se mít dva míče nebo vybrat univerzální model.'),
        ('Na kolik huštit basketbalový míč?', 'Doporučený tlak je obvykle vytištěný na míči poblíž ventilku. Pokud ho nenajdete, hledejte údaj v návodu nebo na stránkách výrobce a nepřehušťujte, aby míč nepraskl.'),
        ('Jak vysoko se věší basketbalový koš?', 'V oficiálním basketbalu je obruč ve výšce 3,05 metru a má průměr 45 centimetrů. Pro děti se hodí nižší nastavení, které se postupně zvyšuje.'),
        ('Je lepší koš na stojan, nebo na zeď?', 'Stojan se dá přemístit a nastavit výšku, zeď poskytuje stabilnější základ pro obruč. Záleží na tom, zda máte vhodnou pevnou stěnu a kolik místa chcete obětovat.'),
        ('Jak vyčistit basketbalový míč?', 'Otřete ho vlhkým hadříkem a případně jemným mýdlovým roztokem. Nenamáčejte ho a nesušte na radiátoru, jinak se povrch zdeformuje.'),
        ('Kolik oček má síťka na koš?', 'Standardní síťka má obvykle 12 oček, ale ověřte, kolik háčků má vaše obruč. Při nákupu si poznamenejte typ materiálu a délku, aby se k vám hodila.'),
        ('Mám koupit kožený, nebo kompozitní míč?', 'Kožený míč je určen pro pokročilé hráče v hale a vyžaduje péči. Kompozit je odolnější a hodí se rekreačním hráčům i školám, které míče používají často.'),
        ('Proč se míč špatně odráží?', 'Nejčastější příčinou je nízký tlak, často následek úniku vzduchu přes ventilek. Dohustěte ho a pokud problém trvá, zkontrolujte ventilek a povrch na trhliny.'),
        ('Kde Sporteka bere ceny míčů?', 'Sporteka ukazuje nabídky českých obchodů u stejného produktu, takže vidíte víc cen vedle sebe. Objednávku dokončíte přímo v obchodě, který vyberete.'),
    ])

# ------------------------------------------------------------------ bezecke-lyze
NEW['bezecke-lyze'] = dict(long=True,
    title='Běžecké lyže: klasika, bruslení, skin a kolečkové',
    desc='Běžecké lyže na klasiku, bruslení i skin, dětské a kolečkové. Jak zvolit délku, tuhost, skluznici a vázání a porovnat nabídky českých obchodů.',
    intro='<p>Běžecké lyže jsou výrazně užší a lehčí než sjezdovky a jejich výběr má víc proměnných, než by se zdálo. Rozhoduje styl, tedy klasika nebo bruslení, dále délka a tuhost podle váhy lyžaře, typ skluznice a vázání, které musí odpovídat botám. '
          'Pro rekreační jezdce navíc existují šupinaté lyže bez nutnosti mazat, pro sportovce skinové a vosky, a pro letní trénink kolečkové lyže.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Fischer, Madshus, Rossignol, Acra, Peltonen, Kästle, Salomon, Sporten nebo Inovik. '
          'K lyžím patří <a href="/bezecke-boty/">běžecké boty</a>, <a href="/bezecke-vazani/">běžecká vázání</a>, <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-vosky/">lyžařské vosky</a> a <a href="/bezecke-lyzovani/">běžecké lyžování</a>. '
          'Níže najdete vysvětlení stylů, rad pro délku a tuhost a tipy na péči o skluznici.</p>',
    guide='<h2>Jaké běžecké lyže existují</h2>'
          '<p>Běžecké lyže se dělí především podle stylu jízdy a způsobu, jak vytvářejí záběr. Klasické lyže jsou delší, měkčí a mají v prostřední části záběrovou zónu, bruslařské lyže jsou kratší, tužší a mají celou skluznici hladkou. '
          'Kombinované lyže (combi) slibují obojí, ale u kvalitních tréninkových modelů se většinou vybírá jedna disciplína. Rekreační jezdec na upravených stopách se cítí dobře na klasických lyžích a bruslení si zkouší až později.</p>'
          + T(['Typ lyží', 'Styl', 'Záběr', 'Pro koho'], [
              ['Klasické s mazáním', 'klasika ve stopě', 'vosk v záběrové zóně', 'zkušení jezdci, závodníci'],
              ['Šupinaté (nomazací)', 'klasika ve stopě', 'šupiny nebo struktura ve skluznici', 'rekreační a začínající'],
              ['Skinové', 'klasika ve stopě', 'pás z umělého kožíšku v záběru', 'pohodlná volba bez vosků'],
              ['Bruslařské', 'bruslení na upravené trati', 'hladká skluznice, vosk na skluz', 'sportovní jezdci'],
              ['Combi', 'klasika i bruslení', 'kompromis, často šupiny', 'ti, kdo chtějí jedny lyže'],
              ['Kolečkové lyže', 'letní trénink', 'kolečka a brzda', 'trénink mimo sezónu'],
              ['Dětské a juniorské', 'klasika, často šupiny', 'jednodušší konstrukce', 'školáci, začátečníci'],
          ]) +
          '<h2>Klasika, nebo bruslení</h2>'
          '<h3>Klasika</h3>'
          '<p>Klasika znamená jízdu v připravené stopě, kde nohy kluzou rovnoběžně vedle sebe. Je to snazší na začátek, protože stopa vede lyže a střed váhy zůstává stabilní. '
          'Výběr zahrnuje mazací lyže s vosky, šupinaté lyže, nebo lyže se skinem. Lyže s mazáním vyžadují, aby se vosk vybíral podle teploty a typu sněhu; šupinaté a skinové modely tento krok vynechávají a výrobci je proto doporučují zejména začínajícím a rekreačním jezdcům.</p>'
          '<h3>Bruslení</h3>'
          '<p>Bruslení vyžaduje širší upravenou plochu a více síly v odrazu. Lyže jsou kratší, mají tužší konstrukci a hladkou skluznici. Je to dynamičtější a rychlejší styl, ale vyžaduje naučit se techniku i odrazy. '
          'Pokud plánujete bruslit, doporučuje se pořídit zvlášť bruslařské lyže, hole a boty; kompromisní combi vybavení se chová jako dobrý začátek, nikoliv jako ideál pro závodní nasazení.</p>'
          '<h2>Délka lyží</h2>'
          '<p>Hrubým pravidlem je, že klasické lyže mají být přibližně o 10 až 20 centimetrů delší než výška lyžaře, bruslařské o 10 až 15 centimetrů kratší. Tato pravidla jsou jen vodítkem: výrobci mají vlastní tabulky podle váhy a tělesného typu, protože pro tuhost lyže je vedle výšky podstatná zejména hmotnost. '
          'Příliš dlouhé lyže se hůř ovládají, příliš krátké se bez dostatečného odrazu bortí. U dětí se často vybírají lyže o něco kratší, aby je zvládly ovládat.</p>'
          '<h2>Tuhost a prohnutí</h2>'
          '<p>Správná tuhost zajišťuje, že lyže při zatížení na jedné noze dosedne záběrovou zónou na sníh a při přenesení váhy na druhou nohu se zase odlehčí. Příliš měkké lyže drhnou skluznicí o sníh, příliš tuhé neprovedou záběr a prokluzují. '
          'Výrobci to řeší označením jako soft, medium a stiff, které se vybírají podle váhy. U rekreačních lyží často stačí jedna univerzální tuhost, u závodních modelů se vyplatí zkoušet.</p>'
          '<h2>Skluznice a péče</h2>'
          '<p>Skluznice, tedy spodní plocha, určuje, jak lyže klouže. Sportovní lyže mají kvalitnější materiál a vyplatí se je pravidelně voskovat. Rekreační lyže se mají aspoň čistit a hlídat, zda na skluznici nepřibyly škrábance nebo tmavé skvrny, které značí vyschnutí. '
          'Před sezónou zkontrolujte poškození a doplňte vosk; po ní je očistěte a uložte na suchém místě bez přímého slunce. Mazání vyžaduje <a href="/lyzarske-vosky/">lyžařské vosky</a> a některé produkty pro čištění, které najdete ve vedlejší kategorii.</p>'
          '<h2>Vázání a boty</h2>'
          '<p>Vázání se musí hodit k botě: dva nejběžnější systémy jsou NNN a Prolink, které jsou vzájemně kompatibilní, zatímco starší SNS je dožívající a nelze jej s nimi kombinovat. Mnoho lyží se prodává už s vázáním, jiné jen s montážní plochou, takže při nákupu zkontrolujte popis. '
          'Boty vybírejte podle stylu, tedy nižší a pružnější na klasiku, vyšší s pevnou podrážkou na bruslení. Kombinované boty slouží oběma. Podrobný přehled najdete v kategoriích <a href="/bezecke-boty/">běžecké boty</a> a <a href="/bezecke-vazani/">běžecká vázání</a>.</p>'
          '<h2>Hole a doplňky</h2>'
          '<p>Běžecké hole jsou delší než sjezdové: pro klasiku sahají přibližně k podpaží, pro bruslení kolem brady až k nosu. Materiál bývá karbon nebo kompozit, pro začátečníky stačí odolnější a levnější varianty. Najdete je v kategorii <a href="/lyzarske-hole/">lyžařské hole</a>. '
          'K výbavě patří také <a href="/lyzarske-rukavice/">lyžařské rukavice</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>. '
          'Vždy myslete na vrstvení oblečení, protože při běžkování se zahřejete rychle a pot rychle chladne.</p>'
          '<h2>Kolečkové lyže a suchý trénink</h2>'
          '<p>Kolečkové lyže se používají k tréninku mimo sezónu. Mají podvozek s koly a brzdami a jezdí se na asfaltu. Existují varianty klasické i bruslařské; kupují je obvykle závodníci, ale baví i rekreační sportovce, kteří chtějí zlepšit techniku. '
          'V kategorii najdete například modely značky Drlik. Při jízdě na asfaltu vždy používejte přilbu a chrániče, protože pád je zde nepříjemnější než ve sněhu.</p>'
          '<h2>Na co si dát pozor při nákupu</h2>'
          '<ul><li><strong>Styl:</strong> klasické a bruslařské lyže se liší tvarem i délkou, nemíchejte je.</li>'
          '<li><strong>Váha:</strong> tuhost se vybírá podle hmotnosti jezdce, ne jen podle výšky.</li>'
          '<li><strong>Vázání:</strong> NNN a Prolink jsou kompatibilní, starší SNS ne, boty a vázání musí být stejného systému.</li>'
          '<li><strong>Sezóna:</strong> modely z minulého ročníku bývají stejné, jen v jiné grafice.</li>'
          '<li><strong>Vosk:</strong> bez mazání zvolte šupiny nebo skin, jinak počítejte s časem na přípravu.</li></ul>'
          '<h2>Jak se připravit na první výjezd</h2>'
          '<p>Před první cestou na stopu si lyže vyzkoušejte doma: obujte boty, zapněte vázání a ověřte, že se bota po nášlapu ozve cvaknutím. Zkontrolujte, zda jsou hole správně dlouhé a poutka nejsou příliš volná. '
          'V terénu hledejte nejprve rovné upravené trasy a nechte si pár kilometrů na zvyk, než zkusíte kopce. Vzpomeňte si, že běžkování je dlouhodobější pohyb, který se vyplatí rozložit; nepřeceňte síly a vezměte si teplou vrstvu na přestávky.</p>'
          '<p>Při prvním mazání se řiďte tabulkou výrobce vosku: každý typ je označen rozsahem teplot, ve kterém funguje. Pokud si nejste jistí, požádejte o radu v servisu nebo na půjčovně. Správně namazané lyže poznáte tak, že při zatížení jedné nohy drží a při klouzání nebrzdí.</p>'
          '<p>Dětem a mírně pokročilým jezdcům se vyplatí nechat si lyže zkontrolovat i před koupí použitých kusů, protože rovnost skluznice a stav hran se z fotky nepozná.</p>'
          '<h2>Servis a uskladnění</h2>'
          '<p>Skluznici je dobré nechat jednou za sezónu prohlédnout v servisu, kde ji zbrousí, opraví škrábance a nanesou kvalitní vosk. Mezi sezónami lyže skladujte ve vaku nebo na stojanu v suché místnosti, pokud možno s lehkým podložením středu tak, aby se neztrácelo prohnutí. '
          'Neukládejte je u topení ani na půdě, kde se v létě silně zahřívají. Vázání a šrouby po sezóně zkontrolujte, protože drobné uvolnění je na stopě nepříjemné.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší výběr mají {B(("fischer", "Fischer"), ("madshus", "Madshus"), ("rossignol", "Rossignol"), ("acra-sport", "ACRA Sport"), ("peltonen", "Peltonen"), ("sporten", "Sporten"), ("acra", "Acra"), ("kastle", "Kästle"), ("inovik", "Inovik"), ("salomon", "Salomon"))}. '
          'Fischer, Madshus a Rossignol patří mezi tradiční výrobce závodních lyží, Peltonen se profiluje ve finské klasice, Acra a Sporten nabízejí cenově dostupné rekreační sady a Kästle přináší prémiové modely. '
          'Značka sama o sobě nic neříká o vhodnosti pro vás, vždy se dívejte na styl, délku a tuhost konkrétního modelu.</p>'
          '<h2>Pro koho které lyže</h2>'
          + T(['Jezdec', 'Doporučení', 'Poznámka'], [
              ['Začátečník', 'šupinaté nebo skinové lyže s vázáním', 'jednoduchost, žádné mazání'],
              ['Rodina s dětmi', 'dětské šupinaté sety', 'kratší lyže, lehké hole'],
              ['Rekreační sportovec', 'skin nebo kvalitní šupiny', 'pohodlná volba pro každý víkend'],
              ['Pokročilý klasik', 'lyže s mazáním', 'čas na vosky, lepší záběr'],
              ['Bruslař', 'bruslařské lyže a boty', 'upravené tratě, tužší konstrukce'],
              ['Letní trénink', 'kolečkové lyže', 'asfalt, přilba a chrániče'],
          ]) +
          '<h2>Kdy a kde nakupovat</h2>'
          '<p>Na začátku sezóny je největší výběr velikostí, ale také největší poptávka. Pozdě v sezóně a po jejím skončení bývá výhodnější hledat slevy, přičemž riziko je, že vaše velikost bude vyprodaná. '
          'Pokud se nechcete zdržovat měřením, sledujte u konkrétního produktu doporučené rozmezí hmotnosti a výšky. Na Sportece vidíte nabídky více obchodů vedle sebe a dostupnost podle délky, takže rychle zjistíte, kdo má vaši velikost skladem.</p>'
          '<h2>Příbuzné kategorie</h2>'
          '<p>Kdo hledá lyže na sjezdovku, najde ve výběru <a href="/sjezdove-lyze/">sjezdové lyže</a>, pro stoupání do kopce <a href="/skialpove-lyze/">skialpové lyže</a> a pro děti <a href="/detske-lyze/">dětské lyže</a>. '
          'Při přepravě pomohou <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>. Širší přehled zimní výbavy a teplého oblečení najdete v kategorii <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[
        ('Jak dlouhé běžecké lyže potřebuji?', 'Klasické lyže mají být přibližně o 10 až 20 cm delší než vaše výška, bruslařské o 10 až 15 cm kratší. Výrobci ale uvádějí vlastní tabulky podle hmotnosti, ty mají přednost.'),
        ('Jaký je rozdíl mezi šupinatými a skinovými lyžemi?', 'Šupinaté mají záběr tvořený šupinami nebo strukturou ve skluznici, skinové mají pás z umělého kožíšku. Obě varianty nevyžadují mazání vosky, liší se chováním při jízdě.'),
        ('Mohu jezdit klasiku na bruslařských lyžích?', 'Nedoporučuje se. Bruslařské lyže mají hladkou skluznici a nemají záběrovou zónu, takže ve stopě prokluzují.'),
        ('Co znamená NNN a SNS?', 'Jde o dva různé systémy vázání pro běžecké boty. Nejsou zaměnitelné, proto musí boty a vázání patřit do stejného systému.'),
        ('Je nutné běžecké lyže voskovat?', 'U sportovních lyží se vosk pravidelně doplňuje, protože zlepšuje skluz. U rekreačních lyží stačí občas skluznici ošetřit, pokud je suchá nebo vybledlá.'),
        ('Jak poznám správnou tuhost lyží?', 'Podle hmotnosti, kterou výrobce uvádí. Jednoduchá zkouška je postavit se na lyže a pod střed vsunout list papíru; při zatížení jednou nohou má list uvíznout.'),
        ('Dají se použít kolečkové lyže v zimě?', 'Ne, jsou určeny na asfalt a suché povrchy. V zimě se pro trénink používají klasické nebo bruslařské lyže na sněhu.'),
        ('Jaké hole vybrat k běžkám?', 'Pro klasiku sahají hole přibližně k podpaží, pro bruslení blíž k bradě. Vybírejte podle stylu a nezaměňujte je se sjezdovými holemi.'),
        ('Můžu koupit lyže bez vázání?', 'Ano, některé modely se prodávají jen s montážní plochou. U nich si musíte vybrat vázání zvlášť a nechat ho namontovat.'),
        ('Jaké lyže pro děti?', 'Nejčastěji šupinaté juniorské sety s vázáním, které se snadno obouvají. Lyže mají být o něco kratší než dítě, aby je zvládlo ovládat.'),
        ('Kdy je nejlepší doba na nákup?', 'Největší výběr bývá před sezónou, slevy po jejím skončení. Pokud hledáte konkrétní velikost, je bezpečnější koupit dřív.'),
    ])

# ------------------------------------------------------------------ obuv-do-vody
NEW['obuv-do-vody'] = dict(long=True,
    title='Boty do vody: neoprenové, síťové, dětské a ponožky',
    desc='Boty do vody pánské, dámské i dětské: neoprenové, síťové, plavecké ponožky a modely na brodění. Jak vybrat podrážku a velikost, srovnání obchodů.',
    intro='<p>Kamenité dno, mušle, ostré škeble nebo rozpálený písek: u vody se noha namáhá jinak než na chodníku. Boty do vody ji chrání, přidávají přilnavost na kluzkých kamenech a po namočení rychle schnou. '
          'Dělí se na neoprenové, síťové, otevřené a minimalistické ponožky a hodí se do moře, k jezeru, na potok i na kajak nebo paddleboard.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Speedo, Springos, Merco, Aqualung, Aquos, Aqua Speed, Reima, O\'Neill nebo Loap. '
          'K výběru se hodí také <a href="/sandaly/">sandály</a>, <a href="/pantofle-a-zabky/">pantofle a žabky</a>, <a href="/plavky/">plavky</a>, <a href="/vodni-sporty/">vodní sporty</a> a <a href="/plazove-doplnky/">plážové doplňky</a>. '
          'Níže najdete přehled typů, rady pro velikost a podrážku a tipy na péči po koupání.</p>',
    guide='<h2>K čemu se boty do vody hodí</h2>'
          '<p>Hlavní roli hraje ochrana. Dno moří a jezer často skrývá ostré kameny, střepy, mušle, v tropech i ježky nebo korály. Boty do vody pomáhají předejít říznutí, zmírňují tlak kamenů a dávají jistotu při vstupu do vody. '
          'Druhým benefitem je přilnavost na mokrých kamenech, třetím teplo: neoprén zmírňuje chlad v chladnější vodě. Bohužel žádné boty nenahradí opatrnost, takže ježky či korály je třeba stále obcházet.</p>'
          + T(['Typ', 'Materiál', 'Hodí se hlavně'], [
              ['Neoprenové boty', 'neopren, protiskluzová podrážka', 'chladnější voda, potápění, kajak'],
              ['Sítové boty', 'textilní síťka a pryžová podrážka', 'brodění, treky u vody, rychlé schnutí'],
              ['Plavecké ponožky', 'tenký neopren nebo elastický textil', 'pláž, bazén, malé nároky na ochranu'],
              ['Sandálový typ', 'pásky a pěnová nebo gumová podrážka', 'horké dny, rodinné koupání'],
              ['Dětské boty do vody', 'pružná pryž, snadné uchycení', 'moře, aquaparky, rodinné dovolené'],
              ['Potápěčské boty', 'tlustší neopren, pevná podrážka', 'potápění, ploutve, skalnaté pobřeží'],
          ]) +
          '<h2>Neoprenové a síťové boty</h2>'
          '<h3>Neopren</h3>'
          '<p>Neoprenové boty uzavřou nohu do pružného materiálu, který zadrží tenkou vrstvu vody a ohřeje ji. Hodí se pro chladnější vody, třeba severské moře nebo horské jezero, a pro vodní sporty, kde jsou nohy delší dobu mokré. '
          'Tloušťka neoprenu určuje tepelný komfort: tenčí je pohodlnější v létě, silnější patří do studené vody nebo k potápění. Výrobci tloušťku uvádějí v milimetrech.</p>'
          '<h3>Sítě a textil</h3>'
          '<p>Sítové boty mají horní díl z odvětrávané tkaniny, která propouští vodu ven i dovnitř a rychle schne. Jsou lehčí než neopren, vyhoví na túry kolem vody, kaňony a potoky a nedělají z nohy saunu. '
          'Typickým příkladem jsou modely značky Merrell pro brodění; v nabídce jsou i variace od Loap, Aquos nebo Springos. Mezi sítě se dostane písek, takže je třeba boty po koupání vypláchnout.</p>'
          '<h3>Ponožky do vody</h3>'
          '<p>Plavecké ponožky jsou nejminimalističtější řešení. Jsou tenké, často z neoprenu, a stačí na písčité pláže, bazén a lehčí bahno. Neposkytují dostatečnou ochranu proti ostrým kamenům, ale zlepšují komfort při chůzi po horkém písku a chrání před mozoly z plavacích ploutví.</p>'
          '<h2>Podrážka a přilnavost</h2>'
          '<p>Podrážka rozhoduje o bezpečnosti. Měla by být pružná, aby noha cítila terén, ale zároveň dostatečně pevná, aby chránila před hrotem kamene. '
          'Vzorek protiskluzové podrážky pomáhá na vlhkých kamenech, hluboký vzorek lépe drží v bahně a mezi oblázky. Pokud se budete pohybovat po ostrém dně, vybírejte tužší podrážku; pro dětské brouzdání stačí měkčí.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Neoprenové boty mají sedět těsně, bez záhybů a bez tlaku na prsty. Při příliš velké velikosti se pod botu dostává voda, která se při pohybu přelévá a boty vyvádí z rovnováhy. Naopak příliš malé tlačí a rychle mohou způsobit odřeniny. '
          'Sítové a sandálové modely mohou být o půl čísla větší, zvlášť pokud je budete nosit s ponožkami. Dětem se hodí boty s upevněním na suchý zip nebo gumou, které si zvládnou nazout samy.</p>'
          '<ul><li><strong>Měření:</strong> změřte délku chodidla ve stoje a porovnejte s tabulkou výrobce.</li>'
          '<li><strong>Chodidlo:</strong> široká noha uvítá širší střih, úzká těsnější neopren.</li>'
          '<li><strong>Dospělé a dětské:</strong> dětské velikosti se u různých značek liší víc než dospělé, proto vždy ověřte údaj v cm.</li>'
          '<li><strong>Zimní ponožky:</strong> pokud do bot obujete ponožky, počítejte s mírně větší velikostí.</li></ul>'
          '<h2>Jak vybrat podle aktivity</h2>'
          + T(['Aktivita', 'Vhodná volba', 'Důvod'], [
              ['Moře a skalnaté pobřeží', 'neopren s pevnou podrážkou', 'ochrana proti kamenům a mušlím'],
              ['Pláž a bazén', 'plavecké ponožky nebo lehké sandály', 'jednoduchost, rychlé schnutí'],
              ['Brodění potoků', 'síťové boty s protiskluzem', 'rychlé schnutí, přilnavost'],
              ['Kajak a paddleboard', 'neopren nebo sítě s uzavřenou špičkou', 'teplo a ochrana při nastupování'],
              ['Potápění', 'potápěčské boty s tlustším neoprenem', 'kompatibilita s ploutvemi'],
              ['Rodinná dovolená', 'dětské sandálové boty', 'snadné nazutí, odolnost'],
          ]) +
          '<h2>Boty do vody pro děti</h2>'
          '<p>Děti se u vody pohybují bez obav a tím se snadno zraní. Dětské boty mají být lehké, snadno obuvatelné a s pevnou podrážkou. Pružná guma na patě zajistí, že boty nesjedou, a protiskluzová sada se osvědčí na mokrém molu a kamenech. '
          'Na dovolené s rodinou se vyplatí vzít si pro každé dítě dva páry, aby po koupání mohly mít druhý pár suchý. Děti rychle rostou, takže kupujte velikost, která sedí aspoň na jednu sezónu, ale ne větší.</p>'
          '<h2>Péče po koupání</h2>'
          '<p>Boty do vody se po slané vodě vypláchnou pitnou vodou, aby sůl nepoškodila materiál. Poté se nechají uschnout na vzduchu, mimo přímé slunce a radiátor, které deformují neopren a lepené spoje. '
          'Pokud se v botách drží zápach, pomůže jemné mýdlo nebo speciální prostředek na neopren a důkladné proschnutí. Sítě občas vykartáčujte, aby se z nich vybral písek.</p>'
          '<ul><li>Po každém použití vypláchněte pitnou vodou.</li>'
          '<li>Sušte ve stínu, nikoliv na topení.</li>'
          '<li>Neskladujte vlhké v uzavřeném batohu.</li>'
          '<li>Při dlouhodobém uložení je zbavte písku a nechte vyvětrat.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kupovat příliš velké boty a mít v nich vodu, která se přeliévá.</li>'
          '<li>Spoléhat na ponožky v kamenitém terénu, kde potřebujete tužší podrážku.</li>'
          '<li>Vzít na túru u vody neoprén, v němž se v létě noha přehřívá.</li>'
          '<li>Sušit boty na slunci a nechat lepené spoje prasknout.</li>'
          '<li>Zapomenout na dětské velikosti a koupit „aspoň o dvě čísla víc“.</li></ul>'
          '<h2>Boty do vody na cestách</h2>'
          '<p>Při cestování do zahraničí se hodí boty, které se vejdou do kapsy batohu a rychle schnou. Plavecké ponožky a lehké sítě zaberou málo místa, těžší neoprenové boty se vyplatí jen tehdy, pokud skutečně budete chodit po ostrém dně nebo potápět. '
          'Před odjezdem zkontrolujte pravidla na plážích: na některých chráněných místech je chůze po korálech zakázána a boty tu nepomohou. Pokud plánujete trek v kaňonu, zvolte obuv se zavřenou špičkou, která chrání prsty před nárazy do kamenů.</p>'
          '<h2>Rozdíl oproti sandálům a teniskám</h2>'
          '<p>Sportovní <a href="/sandaly/">sandály</a> mají podobné určení, ale nejsou stavěny na dlouhý pobyt ve vodě. Pásky se po namočení mohou roztahovat a podrážka z pěny nasákne. '
          'Naopak <a href="/tenisky/">tenisky</a> do vody nepatří, protože nasákou, těžknou a schnou hodiny. Boty do vody jsou kompromisem mezi ochranou a odvodem vody, a proto se hodí všude tam, kde se střídá chůze se sednutím do vody.</p>'
          '<p>Při prvním koupání v nových botách si jejich chování vyzkoušejte v mělké vodě, než se vydáte do hlubší nebo proudící vody. Ověříte tak, zda pata drží a zda se pod chodidlem nehromadí písek.</p>'
          '<p>Pokud boty používáte i na lodi nebo molu, ověřte, že podrážka neklouže po mokrém dřevě a plastu. Právě tam se nejčastěji uklouznete, i když pod vodou máte dobrou přilnavost.</p>'
          '<h2>Jak poznat kvalitní boty</h2>'
          '<p>Kvalitní boty poznáte podle čistých švů bez vyčuhujících nití, rovnoměrně nalepené podrážky a pevných pásků nebo suchého zipu. Zkuste ohnout botu v místě prstů: pokud se ohýbá přirozeně a vrací se do původního tvaru, je to dobrá známka. '
          'Neopren má být pružný, ne křehký, a nemá se na ohybech trhat. Kontrolujte také, zda má otvory pro odtok vody, aby z boty voda rychle odtékala. Jestli je u produktu popis materiálu, přečtěte si ho; výrobci tam obvykle uvádějí tloušťku neoprenu a typ podrážky.</p>'
          '<h2>Značky v nabídce</h2>'
          f'<p>Největší zastoupení mají {B(("speedo", "Speedo"), ("springos", "Springos"), ("merco", "Merco"), ("aqualung", "Aqualung"), ("aquos", "Aquos"), ("aqua-speed", "Aqua Speed"), ("reima", "Reima"), ("o-neill", "O\'Neill"), ("aquastic", "Aquastic"), ("hiko", "Hiko"), ("loap", "Loap"), ("scubapro", "Scubapro"), ("merrell", "Merrell"))}. '
          'Speedo a Aqua Speed jsou spojeny s plaváním, Aqualung a Scubapro s potápěním, Reima a Konges Sløjd nabízejí dětské modely a Merrell a Loap jsou outdoorové značky se sítovými botami. '
          'Nabídka se mění podle sezóny, proto sledujte dostupnost velikostí u konkrétních modelů.</p>'
          '<h2>Jak boty zapadají do dalšího vybavení</h2>'
          '<p>Při vodních sportech počítejte s kompletní výbavou: <a href="/neopreny/">neopreny</a> na tělo, <a href="/plovaci-vesty/">plovací vesty</a> na bezpečnost, <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/ploutve/">ploutve</a> na pohyb pod vodou. '
          'Pro volné dny u vody se hodí <a href="/lycra-a-uv-tricka/">UV trička</a> a <a href="/paddleboardy/">paddleboardy</a>, pro kempování <a href="/kemping/">kempingové vybavení</a>. Pro přeměnu pláže v odpočinkové místo se podívejte na <a href="/pop-up-a-plazove-stany/">plážové stany</a>.</p>'
          '<h2>Jak porovnat nabídky na Sportece</h2>'
          '<p>Při hledání konkrétního modelu otevřete jeho detail a porovnejte nabídky více obchodů. Dívejte se na dostupné velikosti, protože u bot do vody se rychle vyprodávají prostřední čísla. '
          'Pokud si nejste jistí, kterou variantu zvolit, začněte filtrem podle značky nebo materiálu v názvu produktu (neopren, sítě, ponožky). Objednávku dokončíte přímo v obchodě, který zvolíte.</p>',
    faq=[
        ('K čemu jsou boty do vody?', 'Chrání chodidla před ostrými kameny, mušlemi a střepy, zlepšují přilnavost a v případě neoprenu zahřívají nohu. Hodí se do moře, k jezeru i na potok.'),
        ('Čím se liší neoprenové a síťové boty?', 'Neoprenové jsou těsné a zahřívají, síťové jsou lehčí a rychle schnou. Neopren se hodí do chladnější vody, sítě do tepla a pro brodění.'),
        ('Jakou velikost vybrat?', 'Neoprenové boty mají sedět těsně bez záhybů, síťové a sandálové mohou být o půl čísla větší. Vždy porovnejte délku chodidla s tabulkou výrobce.'),
        ('Hodí se boty do vody i na brodění potoků?', 'Ano, zejména síťové modely s protiskluzovou podrážkou. U potoků s ostrými kameny dejte přednost pevnější podrážce.'),
        ('Pro děti stačí plavecké ponožky?', 'Na písčitou pláž a bazén ano. Na kamenité dno nebo molo je lepší pevnější obuv se zpevněnou podrážkou.'),
        ('Jak boty vyprat a usušit?', 'Po koupání je vypláchněte pitnou vodou, případně jemným mýdlem. Sušte ve stínu na vzduchu, ne na radiátoru ani na přímém slunci.'),
        ('Chrání boty do vody před mořskými ježky?', 'Silnější podrážka sníží riziko poranění, ale žádná obuv nezaručuje plnou ochranu. Ježkům se vyhýbejte i v botách.'),
        ('Můžu v botách do vody plavat?', 'Neoprenové boty se k plavání s ploutvemi občas používají, ale některé modely nejsou určeny k dlouhému plavání. Ověřte použití v popisu produktu.'),
        ('Jak zabránit zápachu?', 'Po každém použití boty vypláchněte, nechte důkladně vyschnout a neskladujte vlhké v batohu. Pomůže jemný čisticí prostředek na neopren.'),
        ('Jsou boty do vody vhodné i na pláž?', 'Ano, chrání před horkým pískem i ostrými předměty a snadno se zouvají. Pro suchou pláž stačí lehčí sandálové varianty nebo ponožky.'),
        ('Najdu na Sportece i pánské, dámské a dětské modely?', 'Ano, v kategorii jsou modely pro všechny skupiny. Rozlišení vidíte v názvu produktu a ve velikostní tabulce obchodu.'),
    ])
