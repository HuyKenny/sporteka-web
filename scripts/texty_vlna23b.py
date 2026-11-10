"""sporteka.cz — wave 23b (4. 11. 2026): long texts (>= 1650 words) for cyklisticke-bryle, stanove-doplnky, vlozky-do-spacaku, lyzarske-vazani.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklisticke-bryle
NEW['cyklisticke-bryle'] = dict(long=True,
    title='Cyklistické brýle: zorníky, polarizace, rámy, péče',
    desc='Cyklistické brýle na silnici, MTB i gravel. Jak vybrat zorník, fotochrom, polarizaci a rám, a porovnat nabídky českých obchodů na jednom místě.',
    intro='<p>Cyklistické brýle chrání oči před větrem, prachem, hmyzem, drobnými kamínky od předního kola a v lese také před větvemi. Správně zvolený zorník navíc upraví kontrast podle světla, takže lépe vidíte výmol, kořen nebo kluzký šotolinový úsek. Sporteka porovnává nabídky českých obchodů u brýlí na silnici, do terénu, na gravel i pro děti, od jednoduchých modelů po sady s výměnnými zorníky.</p>'
          '<p>Zvolit je třeba tvar rámu, barvu a vlastnosti skla, větrání a velikost. V přehledu najdete značky ' + B(('force', 'Force'), ('author', 'Author'), ('uvex', 'Uvex'), ('siroko', 'Siroko'), ('rockbros', 'Rockbros'), ('julbo', 'Julbo')) +
          '. K brýlím se hodí <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/cyklisticke-rukavice/">rukavice</a> a další <a href="/cyklo-prislusenstvi/">cyklistické příslušenství</a>.</p>',
    guide='<h2>Proč nejezdit bez brýlí</h2>'
          '<p>Při rychlosti kolem třiceti kilometrů v hodině se i drobná mouška v oku stává problémem, a to nejen nepříjemným, ale i bezpečnostním. Oko zareaguje slzením, víčka se zavřou a krátce nevidíte. Brýle tuhle chvíli odstraní. Chrání také před výtryskem bláta při jízdě za někým, před kapkami deště a před studeným vzduchem, který v zimě pálí v očích a vyvolává slzení.</p>'
          '<p>Druhý důvod je světelný komfort. Dlouhé jízdy na ostrém slunci unavují oči i při obyčejném mhouření. Tmavší sklo nebo polarizační filtr tuto zátěž snižuje. Naopak do hustého lesa, kde se střídá stín a sluneční skvrny, se hodí zorník, který přechody vyrovná a nechá vás přehlédnout terén bez zbytečného oslnění.</p>'
          '<h2>Jaké zorníky se v nabídce objevují</h2>'
          '<p>Základem brýlí je zorník, tedy čočka, nebo jednodílný štít. Bývá z polykarbonátu, který je lehký a odolný proti rozbití. Rozdíly se dělají povrchovou úpravou a zbarvením. Podrobnější přehled shrnuje tabulka.</p>'
          + T(['Zorník', 'Jak se chová', 'Kdy se hodí'], [
              ['Tmavý (šedý, hnědý)', 'výrazně tlumí světlo', 'plné slunce, pláž u jezera, rovinatá silnice'],
              ['Zrcadlový', 'odráží část světla tenkou vrstvou', 'ostré světlo, vysokohorské trasy, voda'],
              ['Polarizační', 'filtruje odlesky od vodorovných ploch', 'mokrý asfalt, jízda proti slunci, lesklé povrchy'],
              ['Fotochromatický', 'ztmavuje se podle intenzity UV záření', 'dlouhé trasy s proměnlivým počasím a tunely'],
              ['Čirý', 'bez filtru, jen mechanická ochrana', 'noc, déšť, mlha, tunely a dojíždění za tmy'],
              ['Žlutý, oranžový, růžový', 'zvyšuje kontrast, tlumí modrou část spektra', 'šero, les, zataženo, úsvit']]) +
          '<p>Ke každé barvě patří i obecná zásada: světlý zorník pustí více světla do oka, tmavý méně. Barevné odlišnosti rozhodují hlavně o tom, jak výrazně uvidíte nerovnosti. Pokud nemáte jistotu, vyberte model s výměnnými zorníky a vezměte si do kapsy čirý, abyste nezůstali bez ochrany po západu slunce.</p>'
          '<h2>Polarizace a fotochrom: co si od nich slibovat</h2>'
          '<p>Polarizační vrstva potlačuje odlesky z vody a lesklého povrchu. V praxi to pomáhá například při jízdě podél řeky nebo po mokré silnici. Má ale i nevýhodu: některé displeje cyklocomputerů nebo telefonů se přes polarizační sklo zdají tmavší nebo se mění jejich viditelnost při naklonění hlavy. Proto polarizaci před koupí vyzkoušejte, nebo si přečtěte, jak ji uvádí výrobce.</p>'
          '<p>Fotochromatické sklo mění tmavost podle světla. Nezačíná ale ztmavovat okamžitě a v chladu reaguje pomaleji než v létě, což oceníte při jízdě tunelem nebo úsekem v lese, kde se světlo střídá po sekundách. Hodí se spíš na delší výlety s proměnlivými podmínkami než na krátké hodinové vyjížďky, kde si můžete zorník zvolit předem.</p>'
          '<h2>Rám, tvar a zakřivení</h2>'
          '<p>Brýle mají být dostatečně velké, aby kryly oči i okolí, a přitom nesmějí tlačit na tváře ani sklouzávat. Tvarů je několik: jednodílný štít ohýbaný kolem hlavy dobře chrání před větrem a poskytuje široký výhled, brýle se dvěma čočkami mají klasičtější vzhled a lépe se čistí. Rámečky bývají plastové, často z nylonu, a lehké. Bezrámové a poloobrubové varianty ubírají na hmotnosti, ale u pádu jsou citlivější.</p>'
          '<ul><li><strong>Nosní opěrka:</strong> nastavitelná nebo gumová, nesmí tlačit a při pocení musí držet. Někteří lidé uvítají možnost opěrku vyměnit.</li>'
          '<li><strong>Stonky:</strong> zahnuté konce s gumovým povrchem drží pod helmou, rovné pasují spíš do běžného života. Tenké stonky se lépe skrývají pod popruhem helmy.</li>'
          '<li><strong>Zakřivení:</strong> výraznější zakřivení chrání z boku, ale může zkreslit obraz u levnějších zorníků. Zkuste si brýle prohlédnout v obchodě nebo si pozorně přečtěte recenze.</li>'
          '<li><strong>Hmotnost:</strong> rozhodují gramy, protože brýle nosíte celé hodiny. Těžké brýle se při jízdě po hrbolech posouvají a zanechávají otlaky.</li></ul>'
          '<h2>Větrání a mlžení</h2>'
          '<p>Pokud se brýle zamlžují, je problém buď v nedostatečné ventilaci, nebo v nevhodném sedu. Dobré modely mají otvory nad zorníkem a prostor mezi sklem a obličejem, kudy proudí vzduch. U brýlí těsně přilehlých ke tváři, které jsou určené pro zimu, bývá odvětrání horší. Na mlžení pomáhá povrchová úprava zorníku proti zamlžení, případně speciální odmlžovací sprej či ubrousek, s nímž se obvykle setkáte přímo v nabídce kategorie.</p>'
          '<p>Při rozjezdu a v prudkém kopci, kde se těžce dýchá, brýle mlží nejvíc. Zkuste je posunout trochu níž, aby vzduch proudil nad nimi, a nasadit je až po zahřátí. Když stojíte na semaforu, je lepší si brýle nechat na nose a nevytahovat je ze zakryté kapsy, kde se sráží voda.</p>'
          '<h2>Sed pod helmou a velikost</h2>'
          '<p>Brýle a helma tvoří jeden systém. Pokud helma nese kšilt, musí být hrana brýlí pod ním a nesmí se dotýkat horních řad větracích otvorů. Zkoušejte brýle vždy s helmou, kterou používáte, jinak se může stát, že stonky drhnou o popruhy. Model z kategorie <a href="/cyklisticke-helmy/">cyklistické helmy</a> často doporučuje výrobce přímo v popisu.</p>'
          '<p>Velikost brýlí udává výrobce slovy S, M a L, nebo šířkou mezi stonky. Úzký obličej potřebuje menší rám, aby brýle nepadaly, široký obličej zase větší, aby nesvíraly spánky. Dětské brýle mají menší tvar a bývají označeny junior. Děti by měly nosit brýle také, protože riziko drobných zranění od kamínků je u nich stejné jako u dospělých.</p>'
          '<h2>Dioptrické brýle a clip-in</h2>'
          '<p>Lidé s dioptriemi mají tři možnosti. První jsou kontaktní čočky pod běžné brýle, druhá je vložka, která se nasazuje dovnitř rámu a nese dioptrické čočky, třetí jsou dioptrické čočky přímo ve sportovním rámu od optika. Vložka bývá nejlevnější, ale zmenšuje zorné pole. Dioptrické zorníky u zakřivených štítů vyžadují odborníka, proto se vyplatí zajít k optikovi s vybraným rámem v ruce.</p>'
          '<h2>Co všechno v kategorii najdete</h2>'
          '<p>Většinu nabídky tvoří sportovní brýle pro cyklisty, ale mezi výsledky narazíte i na další zboží. Objevují se sady s výměnnými zorníky, odmlžovací sady, ochranné pracovní brýle vhodné i na kolo při práci v dílně a občas lyžařské nebo sjezdové brýle, které jsou kvůli popisu zařazeny blízko. Pokud hledáte lyžařské modely, podívejte se do kategorie <a href="/lyzarske-bryle/">lyžařské brýle</a>, pro běh a obecný sport do <a href="/sportovni-bryle/">sportovních brýlí</a> a pro náhradu poškozeného skla do <a href="/nahradni-zorniky/">náhradních zorníků</a>.</p>'
          '<p>Nabídka obsahuje značky ' + B(('force', 'Force'), ('author', 'Author'), ('uvex', 'Uvex'), ('siroko', 'Siroko'), ('max1', 'Max1'), ('rockbros', 'Rockbros'), ('vif', 'Vif'), ('decathlon', 'Decathlon'), ('real-shades', 'Real Shades'), ('tsg', 'TSG'), ('shot-race-gear', 'Shot Race Gear'), ('julbo', 'Julbo')) +
          '. Každá se profiluje trochu jinak: Force a Author nabízejí široký výběr tvarů a barev pro silnici i terén, Uvex se zaměřuje na pevné rámy a výměnné zorníky, Siroko a Rockbros dávají důraz na dostupné sady, Julbo a TSG se zaměřují na ochranu a horské sporty.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<ul><li><strong>Silnice:</strong> aerodynamický štít nebo velké dvě čočky, světlé i tmavé zorníky v sadě. Pokud vozíte jen jeden pár, vyberte fotochromatický nebo polarizační.</li>'
          '<li><strong>MTB a enduro:</strong> pevnější rám, výměnný zorník, dobrá ventilace a odolnost proti nárazu. Ve spleti stromů se hodí žlutá nebo oranžová čočka.</li>'
          '<li><strong>Gravel:</strong> univerzální pár s fotochromatickým sklem. Dlouhé dny na šotolině mají šero i silné slunce, takže se světlo mění.</li>'
          '<li><strong>Dojíždění:</strong> čirý zorník na každý den, k němuž přidáte tmavý pár na slunečné dny. Brýle se mohou hodit i na pěší cestu.</li>'
          '<li><strong>Děti:</strong> menší rám, měkké konce stonků a pružný materiál. Vybírejte raději polykarbonát než sklo.</li></ul>'
          '<h2>Péče o brýle</h2>'
          '<p>Brýle neotírejte suchým hadrem, protože písek zanechá škrábance. Nejdřív oplachujte vodou a pak jemně otřete mikrovláknem. Pokud na skle ulpěla mastnota, použijte kapku jemného saponátu a utřete do sucha. Uchovávejte je v pouzdře, nikoliv v kapse dresu s klíči. Zrcadlové a polarizační vrstvy jsou citlivé na teplo, takže brýle nenechávejte na palubní desce auta na slunci.</p>'
          '<p>Odřený zorník je bezpečnostní problém, ne jen estetický. Při jízdě proti slunci se každý škrábanec rozzáří a oslepí. V takovém případě sáhněte po náhradním zorníku, pokud ho výrobce nabízí, nebo koupi nový pár. Povolené šroubky je dobré dotáhnout miniaturním šroubovákem, jinak se zorník časem vyvrtá z rámu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Příliš tmavý zorník na jízdu pod stromy nebo za soumraku. Ztrátu kontrastu pocítíte při přejíždění kořenů.</li>'
          '<li>Výběr jen podle vzhledu bez zkoušky sedu. Brýle, které při předklonu sklouznou na špičku nosu, budete stále posouvat.</li>'
          '<li>Levné brýle bez označení UV ochrany. Tmavé sklo bez filtru rozšíří zornici a pustí do oka více škodlivého záření, než když nenosíte nic.</li>'
          '<li>Zapomenutý čirý zorník na večerní jízdu domů.</li>'
          '<li>Čištění utěrkou z trička. Mikrovlákno je rychlé, levné a nepoškrábe povrch.</li></ul>'
          '<h2>Jak nakupovat chytře</h2>'
          '<p>Na Sportece jednoduše porovnáte nabídky obchodů a zúžíte výběr podle značky, zorníku nebo určení. Pozorujte, zda je v ceně pouzdro, mikrovláknový sáček a náhradní zorníky, protože u některých sad jsou zahrnuty, u jiných se kupují zvlášť. Brýle jsou nákup, u kterého se vyplatí trocha trpělivosti, protože sezónní kolekce se obměňují a starší barevné varianty se prodávají s odstupem.</p>'
          '<p>Chcete-li dokončit výbavu, projděte i <a href="/cyklisticke-dresy/">cyklistické dresy</a>, <a href="/cyklisticka-obuv/">cyklistickou obuv</a> a <a href="/cyklo-svetla/">světla na kolo</a>. Pro jízdu v nerovném terénu přidejte <a href="/cyklo-chranice/">chrániče</a>, pro výlet po kopcích zkontrolujte <a href="/cyklo-lahve-a-drzaky/">láhve a držáky</a>. Na kvalitní kolo se podívejte do kategorií <a href="/horska-kola/">horská kola</a> nebo <a href="/silnicni-kola/">silniční kola</a>.</p>',
    faq=[('Jaké cyklistické brýle vybrat do začátku?', 'Brýle s polykarbonátovým zorníkem a UV ochranou, ideálně s výměnnými skly. Čirý zorník na šero a tmavý na slunce vám pokryjí většinu situací bez dalšího nákupu.'),
         ('Jaký je rozdíl mezi polarizačními a fotochromatickými brýlemi?', 'Polarizační filtr potlačuje odlesky, fotochromatické sklo mění tmavost podle UV záření. Každé řeší jiný problém a dají se kombinovat jen u některých modelů.'),
         ('Mohu jezdit na kole v obyčejných slunečních brýlích?', 'Lze, ale sportovní brýle drží lépe, mají vyšší odolnost proti nárazu, lépe větrají a nesklouzávají při předklonu. Běžné módní brýle nemusejí vydržet zásah kamínku.'),
         ('Jak zabránit mlžení brýlí?', 'Vybírejte modely s větracími otvory a antifog úpravou, pomáhá odmlžovací sprej. V pomalém kopci brýle posuňte níž a nasazujte je až po zahřátí.'),
         ('Jaký zorník je na jízdu v lese?', 'Žlutý, oranžový nebo světle hnědý. Zvýšený kontrast usnadní vidění kořenů a výmolů ve stínu stromů. Pro mix slunce a stínu vyzkoušejte fotochrom.'),
         ('Jak poznat, že mi brýle sedí?', 'Nesmějí tlačit na spánky, sjíždět při předklonu a nesmějí se dotýkat řas. Zkuste je s helmou, kterou nosíte, a zkontrolujte, zda stonky nedrhnou o popruhy.'),
         ('Mohou cyklistické brýle nosit děti?', 'Ano, existují dětské modely s menším rámem a měkkými stonky. Ochrana před kamínky a hmyzem je pro děti stejně důležitá jako pro dospělé.'),
         ('Co dělat s dioptriemi?', 'Použijte kontaktní čočky, clip-in vložku do sportovního rámu, nebo nechte vyrobit dioptrické čočky u optika. Rám s výraznou křivkou potřebuje odborné zpracování.'),
         ('Jak čistit brýle, aby se nepoškrábaly?', 'Nejprve opláchněte vodou, abyste smyli písek, a pak očistěte mikrovláknem, případně s kapkou jemného mycího prostředku. Utěrka z trička a suché otírání zanechávají škrábance.'),
         ('Kdy vyměnit zorník nebo celé brýle?', 'Když je zorník hluboce poškrábaný, má odprýsknutou povrchovou vrstvu nebo se rám deformoval. Škrábance zhoršují vidění při jízdě proti slunci.'),
         ('Jsou ochranné pracovní brýle vhodné na kolo?', 'Slouží jako mechanická ochrana očí, ale nemívají větrání ani sed pro sport. Na delší jízdu je lepší skutečný sportovní model.')],
)

# ------------------------------------------------------------------ stanove-doplnky
NEW['stanove-doplnky'] = dict(long=True,
    title='Plachty, podlážky a opravy stanů: tarpy, předstany',
    desc='Tarpy, plachty, předstany, podlážky, tyče a opravné sady ke stanům. Jak vybrat doplňky, uchytit je a porovnat nabídky českých obchodů.',
    intro='<p>Stan sám o sobě nevyřeší všechno. Z deště vás ochrání plachta, před vlhkou zemí podlážka, pro společenský večer předstan nebo přístřešek a při prasklé tyčce se hodí opravná sada. Sporteka v této kategorii přehledně porovnává nabídky českých obchodů: tarpy a bivakovací plachty, předstany, podlážky, stanové tyče, koberce, závětří pro vařiče i drobné opravné díly a spojky.</p>'
          '<p>Správná volba závisí na tom, ke kterému stanu doplněk bude, v jaké sezóně a jak často ho budete používat. V nabídce převažují značky ' + B(('outwell', 'Outwell'), ('mfh', 'Mfh'), ('eurotrail', 'Eurotrail'), ('skandika', 'Skandika'), ('sea-to-summit', 'Sea to Summit'), ('robens', 'Robens')) +
          '. Stan samotný najdete v kategorii <a href="/stany/">stany</a>, další vybavení v <a href="/kemping/">kempingu</a>.</p>',
    guide='<h2>Co všechno patří mezi stanové doplňky</h2>'
          '<p>Kategorie sdružuje poměrně různorodé věci, které mají společné jedno: rozšiřují nebo zachraňují stan. Najdete tu plachty na zastřešení, předstany, které se připojují ke stanům, podlážky pod dno, náhradní tyče a oblouky, opravné sady a výplňky, závětří pro vařiče i koberce. Dělí se podle toho, k čemu slouží.</p>'
          + T(['Doplněk', 'K čemu slouží', 'Poznámka'], [
              ['Tarp, bivakovací plachta', 'rychlý přístřešek nad spacím místem nebo kuchyní', 'lehký, vyžaduje lanka, tyče nebo stromy'],
              ['Předstan', 'zastřešený prostor před vchodem do stanu', 'musí odpovídat modelu, rodině nebo systému uchycení'],
              ['Podlážka (footprint)', 'chrání dno stanu před oděrem a vlhkem', 'ušitá na míru nebo univerzální fólie'],
              ['Tyče a oblouky', 'náhrada za zlomenou nebo ohnutou tyč', 'průměr a délka musí souhlasit'],
              ['Opravná sada', 'záplaty, tmel, náhradní manžety', 'vždy do výbavy na delší cestu'],
              ['Koberec do stanu', 'izolace a pohodlí na podlaze předstanu', 'prodyšný, lze skládat'],
              ['Závětří', 'chrání plamen vařiče před větrem', 'nepatří do stanu']]) +
          '<p>Než cokoli koupíte, ujasněte si, zda hledáte doplněk právě k vašemu stanu. U značkových kempingových stanů často existují doplňky přesně navržené pro jeden model, zatímco u univerzálních se řídíte rozměry. Doporučujeme přečíst si i text kategorie <a href="/stany/">stany</a>, kde najdete výběr podle počtu osob.</p>'
          '<h2>Tarpy a bivakovací plachty</h2>'
          '<p>Tarp je jednoduchá plachta s očky a uchycením na rozích a po obvodu. Používá se jako přístřešek nad hamakem, bivakem nebo kuchyní. Vyrábí se z nylonu, polyesteru, někdy z bavlněných směsí nebo moderních laminátů pro ultralehké turisty. Nylon je lehký a rychle schne, polyester méně nasákne a lépe odolává UV záření, bavlna se hodí do kempu, kde nezáleží na hmotnosti.</p>'
          '<ul><li><strong>Velikost:</strong> pro jednoho člověka stačí malý tarp, pro dva a kuchyň vybírejte větší. Platí, že větší plocha poskytuje více místa, ale také zachytává vítr.</li>'
          '<li><strong>Vodní sloupec:</strong> údaj v milimetrech říká, jak odolává tlaku vody. Pro tarp stačí nižší vodní sloupec než pro dno stanu, protože ho netlačí voda ani váha těla zespodu.</li>'
          '<li><strong>Uchycení:</strong> důležité jsou pevné rohy, smyčky na okrajích a body ve středu pro napnutí do tvaru. Slabý okraj se při větru protrhne jako první.</li>'
          '<li><strong>Doplňky:</strong> teleskopické tyče, lanka a kolíky se často prodávají zvlášť. Zkontrolujte, zda jsou v balení.</li></ul>'
          '<p>Při stavbě tarpu je důležitý sklon. Vodorovně napnutá plachta zadržuje vodu a prohýbá se, takže jednu stranu vždy nastavte níž, aby voda stékala. Do větru směřujte nízkou stranu. Rozpětí lan nastavujte tak, aby nikde nevisela volně, protože tam by se dutiny plnily deštěm.</p>'
          '<h2>Předstany a přístřešky</h2>'
          '<p>Předstan je nejpraktičtější rozšíření rodinného stanu. Poskytuje zastřešený prostor na jídlo, boty a zavazadla a v dešti nabízí místo, kde se děti mohou hrát. Bývá napojen na stanovou plachtu pomocí popruhů, tunýlku nebo lišty. Právě uchycení je to, na čem záleží: stan musí mít odpovídající systém, jinak předstan neprojde a prostor mezi nimi zateče.</p>'
          '<p>V nabídce najdete předstany větší, určené pro kempování s karavanem nebo velkým stanem, i menší přístřešky. Značky jako Outwell a Eurotrail nabízejí řady, které se kombinují s jejich vlastními stany, další výrobci vyrábějí univerzálnější verze. Jako ochranu proti vlhku se hodí vodotěsné spoje a vyšší vodní sloupec střechy, pro letní horko prodyšné boky a síťová okna.</p>'
          '<ul><li>Změřte šířku a výšku vchodu stanu i předstanu.</li>'
          '<li>Pozor na hmotnost. Předstany se skládají dlouho a zabírají místo v kufru.</li>'
          '<li>Při větru ho vždy zajistěte kolíky a odtahy. Velká plocha působí jako plachta.</li>'
          '<li>Při dešti odvádějte vodu přes okap, který spojí dva přístřešky nebo přístřešek a stan.</li></ul>'
          '<h2>Podlážky a ochrana dna</h2>'
          '<p>Dno stanu je nejnamáhanější část. Přichází do styku s kameny, kořeny a vlhkem, proto se vyplatí nasadit pod něj vrstvu navíc. Značková podlážka je ušitá přesně na tvar a má očka pro tyče, univerzální podlážka bývá fólie nebo odolná plachta, kterou si zastřihnete. Musí být o něco menší než dno stanu, jinak voda stékající po plášti zateče pod ni a vytvoří kaluž.</p>'
          '<p>Podlážka pod stanem chrání dno před kameny a šiškami zespodu, a tak prodlužuje jeho životnost, zejména na hrubém nebo odřeném podkladu. Izolaci od chladné země ale řeší až <a href="/karimatky-a-matrace/">karimatka nebo matrace</a> uvnitř stanu. Podlážku po použití opláchněte, osušte a skládejte volně.</p>'
          '<h2>Tyče, oblouky a drobné díly</h2>'
          '<p>Stanové tyče bývají hliníkové nebo ze skelného vlákna. Hliník je pevnější a lehčí, sklolaminát levnější a pružnější. Při výběru náhrady měřte průměr, délku a typ spojek. Kovová manžeta opravuje prasklou tyč dočasně, pokud nemáte po ruce celou náhradu. Pro velké stany existují středové tyče a teleskopické konstrukce, u kterých ověřte nosnost.</p>'
          '<p>Do kategorie spadají také kolíky, odtahová lanka, větrné kroužky, napínáky a stahovací poutka a další drobnosti, které se hodí při každém stavění. Kolíky vyberte podle půdy: do tvrdé země ocelové, do písku a sněhu dlouhé a široké.</p>'
          '<h2>Opravy stanu a plachet</h2>'
          '<p>Opravná sada se vejde do kapsy a zachrání víkend. Obvykle obsahuje samolepicí záplaty, tmel na švy, náhradní manžetu na tyč, jehlu a nit. Díra v plášti se zalepí z obou stran, předtím se okolí očistí a odmastí. Prasklý šev se zatmelí a nechá zaschnout, než stan sbalíte. Oprava není neomezeně trvanlivá, ale na pár nocí obvykle postačí.</p>'
          '<ul><li>Záplaty vždy zaoblete v rozích, nelepí se pak od okraje.</li>'
          '<li>Při tmelení švů pracujte v suchu a při pokojové teplotě.</li>'
          '<li>Neskladujte stan vlhký, plíseň ničí povrchovou úpravu.</li>'
          '<li>Při rozkládání doma zkontrolujte zipy, popruhy a oblouky a včas je vyměňte.</li></ul>'
          '<h2>Zázemí pro vaření a bivak</h2>'
          '<p>V kategorii se objevují i závětří pro kempingové vařiče a tarpy na bivakování. Závětří z hliníkových lamel se rozloží kolem hořáku a chrání plamen. Vařiče nikdy nepoužívejte ve stanu ani v uzavřeném předstanu, protože hrozí požár a otrava oxidem uhelnatým. Pro přípravu jídla vyberte otevřený prostor s dostatečnou vzdáleností od látky. Další vybavení hledejte v kategorii <a href="/varice-a-kartuse/">vařiče a kartuše</a> a <a href="/vareni-v-prirode/">vaření v přírodě</a>.</p>'
          '<p>Pro zajištění výbavy použijte i <a href="/kempingove-doplnky/">kempingové doplňky</a>. Bez kvalitní podložky se neobejdou ani <a href="/karimatky-a-matrace/">karimatky a matrace</a> a spacák se uplatní v kategorii <a href="/spaci-pytle/">spací pytle</a>, kde najdete i <a href="/vlozky-do-spacaku/">vložky do spacáku</a>.</p>'
          '<h2>Výběr podle způsobu kempování</h2>'
          '<ul><li><strong>Víkendový kemp s autem:</strong> předstan, koberec a robustní kolíky. Hmotnost je vedlejší.</li>'
          '<li><strong>Trek a bikepacking:</strong> lehký tarp, lehké kolíky a malá opravná sada. Každý gram se počítá.</li>'
          '<li><strong>Rybaření:</strong> větší plachta a závětří, ideálně v nenápadné barvě. Pro delší pobyty se podívejte i do <a href="/rybarske-stany/">rybářských stanů</a>.</li>'
          '<li><strong>Rodina s dětmi:</strong> prostorný přístřešek, který vás ochrání před deštěm i sluncem. Dětské stany jsou v kategorii <a href="/detske-stany/">dětské stany</a>.</li>'
          '<li><strong>Festival:</strong> pevné lanko, náhradní kolíky a podlážka proti rozbahněné louce.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nákup předstanu bez kontroly kompatibility s konkrétním stanem.</li>'
          '<li>Podlážka větší než půdorys. Voda se pod ní hromadí.</li>'
          '<li>Napnutí tarpu naplocho, bez spádu pro odtok vody.</li>'
          '<li>Podcenění větru. Velké plochy je třeba odtahovat více body.</li>'
          '<li>Vaření ve stanu nebo těsně u látky.</li>'
          '<li>Absence záložní tyče na vícedenní výlet v horách.</li></ul>'
          '<h2>Sezónnost a skladování doplňků</h2>'
          '<p>Stanové doplňky se prodávají celý rok, ale největší výběr bývá na jaře před sezónou. Podlážky, tarpy a opravné sady skladujte suché a volně složené, nejlépe v látkovém pytli. Hliníkové tyče nenechávejte spojené, jinak elastická šňůra uvnitř ztrácí pružnost. Před každou výpravou projděte výbavu, ať se při prvním dešti nezjistí chybějící kolík nebo odtržený popruh.</p>'
          '<h2>Materiály a povrchové úpravy</h2>'
          '<p>Nylon a polyester bývají opatřeny silikonovým nebo polyuretanovým nátěrem, který zvyšuje vodotěsnost. Silikon je lehký a pevný, ale špatně se lepí, polyuretan se lépe lepí, ale časem stárne a může zapáchat. Bavlněná plachta se po namočení zatáhne a vodu pak odpuzuje, je však těžká. Při výběru sledujte také odolnost proti UV záření, protože slunce plachty časem zkřehčí.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Porovnejte popisy a rozměry v několika obchodech. Pozor na stejně vypadající nabídky, které se liší materiálem nebo hmotností. Pokud bude doplněk jeden z mála, který budete brát na delší cestu, vybírejte lehčí a pevnější variantu. Koupě na konci sezóny bývá výhodná, ale některé předstany a plachty se vyprodávají bez možnosti doobjednat díly, proto raději vybírejte doplněk dlouhodobě podporovaný výrobcem.</p>',
    faq=[('Co to je tarp a k čemu je dobrý?', 'Tarp je lehká plachta natažená mezi stromy nebo tyčemi. Slouží jako přístřešek nad bivakem, hamakem nebo kuchyní, kde nepotřebujete plný stan.'),
         ('Hodí se každý předstan ke každému stanu?', 'Ne. Záleží na šířce a výšce vchodu a na způsobu uchycení. U značkových stanů volte předstan ze stejné řady, u univerzálních porovnejte rozměry.'),
         ('Potřebuji podlážku pod stan?', 'Není povinná, ale chrání dno před oděrem a vlhkem. Musí být o něco menší než dno, jinak se pod ni dostane voda.'),
         ('Jak opravit díru ve stanu?', 'Plochu očistěte a odmastěte a nalepte samolepicí záplatu z obou stran. Lze také použít tmel. Před sbalením nechte vše zaschnout.'),
         ('Z čeho jsou stanové tyče?', 'Nejčastěji z hliníku nebo ze sklolaminátu. Hliník je lehčí a pevnější, sklolaminát levnější a pružnější. Náhradu vybírejte podle průměru a délky.'),
         ('Jak postavit tarp, aby nezatékalo?', 'Jednu stranu postavte níž, aby voda stékala, a nízkou stranu otočte proti větru. Plachtu napněte do spádu a zajistěte odtahy.'),
         ('Mohu vařit pod tarpem nebo v předstanu?', 'Pod otevřeným tarpem s odstupem od látky ano. V předstanu a ve stanu vařič nepoužívejte, hrozí požár a otrava oxidem uhelnatým.'),
         ('Jaké kolíky ke stanu vybrat?', 'Záleží na půdě. Do tvrdé země se hodí ocelové, do písku nebo sněhu dlouhé a široké. Univerzální sada se hodí do auta, ne na trek.'),
         ('Jak o plachty a předstany pečovat?', 'Po použití je vysušte, opláchněte od bláta a skladujte volně v suchu. Mokré složené plachty plesnivějí a ztrácejí povrchovou úpravu.'),
         ('Jak vybrat velikost tarpu?', 'Pro jednoho člověka stačí menší plachta, pro dva s batohy nebo vařením zvolte větší. Příliš velká plocha ovšem víc zachytává vítr a hůř se napíná.'),
         ('Kdy je lepší koupit předstan a kdy tarp?', 'Předstan se hodí k rodinnému stanu, který stojí na jednom místě několik dní. Tarp je lehčí a rychlejší, vhodný pro trek, hamak a krátké pobyty.'),
         ('Co patří do základní opravné sady na stan?', 'Samolepicí záplaty, tmel na švy, manžeta na tyč, jehla s nití a kus lanka. Sada se vejde do kapsy batohu.')],
)

# ------------------------------------------------------------------ vlozky-do-spacaku
NEW['vlozky-do-spacaku'] = dict(long=True,
    title='Vložky do spacáku: hedvábí, bavlna, fleece, obaly',
    desc='Vložky do spacího pytle z hedvábí, bavlny, mikrovlákna a fleecu, cestovní přikrývky a obaly. Jak vybrat tvar, materiál a velikost a porovnat obchody.',
    intro='<p>Vložka do spacáku je tenký vnitřní pytel, který chrání výplň před potem, kožním mazem a špínou a při cestování nahrazuje cizí povlečení. Některé materiály přidají pár stupňů tepla, jiné jsou téměř bez váhy a vejdou se do dlaně. Sporteka porovnává nabídky českých obchodů u vložek z hedvábí, bavlny, mikrovlákna a fleecu, u cestovních přikrývek i u kompresních obalů.</p>'
          '<p>Při výběru pomůže tvar mumie nebo obdélníku, správná délka, materiál a také to, zda vložku koupíte na trek, do hostelu, nebo k chladnému spacáku. Mezi značkami najdete ' + B(('cocoon', 'Cocoon'), ('sea-to-summit', 'Sea to Summit'), ('ferrino', 'Ferrino'), ('lifeventure', 'LifeVenture'), ('naturehike', 'Naturehike'), ('warmpeace', 'Warmpeace')) +
          '. K vložce patří vhodný <a href="/spaci-pytle/">spací pytel</a>, třeba <a href="/perove-spacaky/">péřový</a> nebo <a href="/dekove-spacaky/">dekový</a>, a také <a href="/karimatky-a-matrace/">karimatka</a>.</p>',
    guide='<h2>Proč vložku používat</h2>'
          '<p>Spacák se pere nepříjemně: péřová výplň vyžaduje opatrnost a speciální prostředek, syntetická se po několika pracích časem sesedá a každé praní zkracuje životnost. Vložka tento problém řeší tím, že se špína zachytí v ní. Vložku vyperete po každé cestě v běžné pračce a spacák zůstane čistý po několik sezón. Druhý důvod je hygiena na cestách: v hostelu, chatě nebo vlaku s lůžkem se hodí mít vlastní povlak.</p>'
          '<p>Třetí důvod je teplota. Tenká vrstva vzduchu a látky přidá několik stupňů, hedvábí méně, fleece více. Nejde o náhradu teplejšího spacáku, ale o doladění: v teplé noci vložka slouží místo spacáku samostatně, v chladné ho doplní. Hodnoty uvádějí výrobci jen orientačně, protože reálný efekt závisí na oblečení a na tom, jak dobře spacák těsní.</p>'
          '<h2>Materiály, které v kategorii najdete</h2>'
          + T(['Materiál', 'Vlastnosti', 'Hodí se na'], [
              ['Hedvábí', 'velmi lehká, hebká, po sbalení malá', 'trek, minimalismus, horké noci'],
              ['Bavlna', 'příjemná na dotek, dobře se pere, těžší', 'chaty, hostely, kempy autem'],
              ['Mikrovlákno, polyester', 'lehká, rychle schne, nenáročná', 'univerzální použití, tábor'],
              ['Fleece, Polartec', 'hřeje, měkká, objemnější', 'chladné noci, zimní spaní'],
              ['Směsi (hedvábí a bavlna)', 'kompromis mezi vahou a komfortem', 'dlouhé cesty'],
              ['Neprodyšná fólie (vapor barrier)', 'zadržuje vlhkost a teplo, nedýchá', 'extrémní chlad, expedice']]) +
          '<p>Bavlna je levná a prodyšná, ale po zvlhnutí se pomalu suší a po praní zabírá hodně místa v batohu. Hedvábí stojí víc, ale je nejlehčí a nejmenší. Mikrovlákno je rozumný kompromis a odolá víc než hedvábí. Fleece se hodí hlavně do zimy, v létě by se v ní spalo příliš teple. Neprodyšná vložka je speciální nástroj pro expedice, pro běžné spaní se nehodí, protože se v ní vlhkost hromadí a spaní není příjemné.</p>'
          '<h2>Tvar: mumie, obdélník a dvojitá vložka</h2>'
          '<p>Tvar vložky má odpovídat tvaru spacáku. Mumie je úzká u nohou a má kapuci, takže přesně pasuje do mumiového spacáku, obdélníková vložka je prostorná a hodí se do dekového spacáku nebo na samostatné použití. Lidé, kteří se pohybují hodně ve spánku, ocení širší tvar, někdy i s dodatečnými zipy. Dvojitá vložka vznikne spojením dvou zipů a je určena pro dva, což se hodí do manželského spacáku nebo na samostatnou postel.</p>'
          '<ul><li><strong>Délka:</strong> vložka má být o pár centimetrů delší než tělo, jinak se vám při spaní zvedne při nohou. Pro vysoké osoby existují prodloužené varianty.</li>'
          '<li><strong>Zip:</strong> zip podél celé délky usnadňuje větrání. Zip jen do poloviny je lehčí, ale hůř se nasazuje.</li>'
          '<li><strong>Kapuce:</strong> mumiové vložky mívají stahovací kapuci, která zahřeje hlavu a přitom drží polohu.</li>'
          '<li><strong>Kapsa:</strong> vestavěný polštářek na kapsu na hlavě se hodí v hostelu, kde chcete mít čistý polštář.</li></ul>'
          '<h2>Cestovní spacáková přikrývka</h2>'
          '<p>Přikrývka, kterou některé značky označují jako travel blanket, bývá z tenkého textilu a tvarem připomíná prodlouženou obálku. Používá se do tepla, na lehátko ve vlaku nebo na slunnou chatu. V nabídce převažují přikrývky mumie a obdélníkové, často v barevném provedení. Značka Cocoon je v kategorii nejčastější a dělá všechny hlavní materiály včetně hedvábí, bavlny a mikrovlákna.</p>'
          '<h2>Obaly a kompresní vaky</h2>'
          '<p>Mezi vložkami najdete i obaly na spací pytel. Kompresní vak má popruhy, kterými spacák stlačíte na zlomek objemu a vejdete se do batohu. Voděodolný obal chrání výplň před deštěm, pro péřové modely je nezbytný. Pozor ale: spacák doma nenechávejte v kompresi, protože výplň ztrácí vzdušnost. Stlačení využijte při přepravě a doma ho volně uložte do větší bavlněné tašky.</p>'
          '<ul><li>Velikost obalu volte podle objemu spacáku, ne podle délky.</li>'
          '<li>Péřový spacák vždy vložte nejdřív do vnitřního voděodolného pytle.</li>'
          '<li>Neskladujte obal na hřejícím místě, třeba v autě na slunci.</li></ul>'
          '<h2>Jak vybrat podle použití</h2>'
          '<ul><li><strong>Dálkový trek:</strong> hedvábná mumie bez zbytečných doplňků. Zajímá vás hmotnost a velikost po sbalení.</li>'
          '<li><strong>Hostely a cestování po městech:</strong> bavlněná obdélníková vložka s polštářkem, dobře se pere a příjemně se v ní spí.</li>'
          '<li><strong>Chladné noci ve stanu:</strong> fleecová vložka nebo kombinace tenké vložky a teplejšího spacáku.</li>'
          '<li><strong>Dovolená v teple:</strong> lehká přikrývka, v níž se nepřehřejete.</li>'
          '<li><strong>Rodina s dětmi:</strong> bavlněné vložky, které se dají pravidelně prát. U dětských spacáků vás zajímají <a href="/detske-spacaky/">dětské spací pytle</a>.</li>'
          '<li><strong>Rybáři:</strong> teplejší vložka do <a href="/rybarske-spacaky/">rybářského spacáku</a> při nočním čekání na rybu.</li></ul>'
          '<h2>Jak o vložku pečovat</h2>'
          '<p>Bavlnu a mikrovlákno perte v pračce na teplotu uvedenou na štítku, hedvábí šetrněji, nejlépe v ruce nebo programem pro jemné prádlo. Sušte volně, mimo přímé slunce a bez radiátoru. Hedvábí po dlouhodobém působení slunce křehne. Po praní se materiály sesednou o nepatrnou délku, takže u kratších vložek je potřeba brát v úvahu přídavek. Pokud vložka získala zápach, pomůže ji rozložit na vzduchu před praním.</p>'
          '<p>Při sbalení udělejte z vložky roličku a dejte ji do sáčku, ve kterém ji kupujete. Nejlépe se hodí uchovávat ji ve stejném pytlíku jako spacák, abyste ji měli vždy po ruce. Pokud ji máte pověsit, použijte šňůru pro prádlo a neponechávejte ji na kovovém háku, kde může ve vlhku zrezivět.</p>'
          '<h2>Co v kategorii najdete navíc</h2>'
          '<p>Vedle klasických vložek se v nabídce objevují vojenské obaly na spacák, sady s kompresním vakem, ale i výrobky pro speciální použití, například zateplovací vložky Polartec. Dále jsou tu přehozy a zimní návleky na spacák, které rozšiřují komfortní rozsah o další stupně. Oproti koupi nového spacáku jsou levnějším způsobem, jak doladit chladné noci. U označení teploty pamatujte na to, že komfortní a extrémní teplota u spacáku se liší a přírůstek teploty od vložky je jen orientační.</p>'
          '<p>Kompletní spaní doplňte o <a href="/stany/">stan</a>, <a href="/turisticke-stany/">turistický stan</a> a o <a href="/stanove-doplnky/">stanové doplňky</a>. Hodí se i <a href="/hamaky/">hamak</a>, <a href="/kemping/">kempingové vybavení</a> a <a href="/kempingove-doplnky/">kempingové drobnosti</a>.</p>'
          '<h2>Vložka a hygiena na cestách</h2>'
          '<p>Na cestách po horských chatách, v hostelech nebo na kolejích se vlastní povlak hodí jako ochrana před cizími alergeny. Některé vložky mají protipotní úpravu s ionty stříbra, která brání zápachu, ale úprava časem slábne a nenahradí praní. Pokud cestujete do tropů, zvolte hedvábí nebo tenkou bavlnu, v nichž nebudete mít pocit horka, a přidejte repelent. Lehká vložka s moskytiérou není tentýž výrobek, mezi vložkami ji nehledejte.</p>'
          '<p>Praktické je mít dvě vložky, jednu v použití a druhou čistou na výměnu, protože po několika nocích v jednom kuse se vložka vyplatí vyprat. Hedvábná se uschne za pár hodin, takže stačí praní večer a ráno je opět připravena. Pro delší cestu si sbalte vložku do vodotěsného sáčku, aby se nezamočila s ostatními věcmi. Vlhká vložka se nesmí zabalit natrvalo, protože v ní vznikne plíseň. V dešti tak ochráníte nejen vložku, ale i spacák, ke kterému patří.</p>'
          '<h2>Jak číst parametry v popisu</h2>'
          '<ul><li><strong>Rozměry:</strong> délka a šířka v centimetrech. Porovnejte je s vlastní výškou a obvodem ramen.</li>'
          '<li><strong>Hmotnost:</strong> hedvábné modely mívají okolo stovek gramů, těžší bavlněné výrazně víc. Rozdíl se na treku snadno pozná.</li>'
          '<li><strong>Rozměr po sbalení:</strong> údaj v popisu rozhodne, zda se vejde do postranní kapsy batohu.</li>'
          '<li><strong>Zip a kapuce:</strong> určují, jak se vložka obléká a zda ji lze používat rozevřenou jako přikrývku.</li>'
          '<li><strong>Péče:</strong> štítek říká teplotu praní a zda je vhodná sušička. Hedvábí a technické textilie se často mají sušit volně.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě vložky o stejné velikosti jako spacák. Příliš těsná vložka se při otáčení zkroutí a spacák vytlačí.</li>'
          '<li>Očekávání, že vložka nahradí teplý spacák v mrazu.</li>'
          '<li>Použití bavlny na dlouhý trek, kde na gramech záleží.</li>'
          '<li>Skladování spacáku v kompresním vaku celé měsíce.</li>'
          '<li>Praní hedvábí na vysoké teplotě.</li>'
          '<li>Koupě neprodyšné vložky pro běžné spaní.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Při porovnávání v obchodech sledujte materiál, rozměry, hmotnost a také to, zda je zahrnut obal. Barevné varianty stejného modelu se liší jen vzorem, ale ne vždy je dostupná každá velikost. Většina modelů se prodává dlouhodobě, takže stačí počkat na vhodnou nabídku. Vyplatí se zvážit vložku i při koupi nového spacáku, protože prodlouží jeho životnost a ušetří čas při praní.</p>',
    faq=[('K čemu je vložka do spacího pytle?', 'Chrání výplň před potem a špínou, dá se snadno vyprat a v ubytování nahrazuje cizí povlečení. Mírně také přidává teplo.'),
         ('Jaký materiál vložky zvolit?', 'Hedvábí je nejlehčí a nejmenší, bavlna nejpříjemnější a nejlevnější, mikrovlákno univerzální a fleece nejteplejší. Vybírejte podle toho, kam jedete.'),
         ('O kolik stupňů vložka přihřeje?', 'Záleží na materiálu. Hedvábí přidá málo, fleece víc. Výrobci uvádějí orientační hodnoty, které se mohou lišit podle oblečení a spacáku.'),
         ('Jak velkou vložku koupit?', 'Tvar volte stejný jako u spacáku a délku o něco větší než výšku postavy. Pro vysoké existují prodloužené modely.'),
         ('Mohu vložku použít místo spacáku?', 'V teplých nocích ano, hlavně hedvábnou nebo bavlněnou. V chladu ji kombinujte se spacákem, samotná by nestačila.'),
         ('Jak prát hedvábnou vložku?', 'Šetrně, v ruce nebo programem pro jemné prádlo, při nízké teplotě. Sušte volně mimo přímé slunce.'),
         ('K čemu slouží kompresní vak?', 'Stlačí spacák na menší objem pro přepravu v batohu. Doma ho nenechávejte v kompresi, výplň by ztrácela vzdušnost.'),
         ('Co je neprodyšná vložka (vapor barrier)?', 'Speciální vložka zadržující vlhkost a teplo pro extrémní chlad. Pro běžný kemp se nehodí, protože v ní spíte v potu.'),
         ('Je vložka vhodná pro děti?', 'Ano, pokud je dostatečně malá, aby se v ní neplácaly. Bavlna je nenáročná a dá se často prát. Dětské spacáky najdete ve vlastní kategorii.'),
         ('Jak poznám, že vložka není vhodná pro mě?', 'Pokud se v ní zamotáváte nebo vám zůstávají prostory u nohou, je buď příliš velká, nebo má špatný tvar. Správná vložka sedí podobně jako spacák.'),
         ('Stačí vložka v zimě?', 'Ne. V zimě slouží jako doplněk, ne náhrada teplého spacáku. Pomůže fleecová nebo dvouvrstvá varianta, ale základ musí tvořit spacák na danou teplotu.'),
         ('Jak vložku skladovat?', 'Suchou a čistou, volně složenou v sáčku. Neponechávejte ji vlhkou, aby nezačala zapáchat.'),
         ('Hodí se vložka i do hostelu?', 'Ano, to je jedno z hlavních použití. Máte vlastní čisté povlečení a vložka zabere v zavazadle málo místa.')],
)

# ------------------------------------------------------------------ lyzarske-vazani
NEW['lyzarske-vazani'] = dict(long=True,
    title='Lyžařské vázání: sjezd, skialp, snowboard, DIN',
    desc='Lyžařská vázání: sjezdová, skialpová a snowboardová. Jak vybrat podle bot, brzdy, DIN a šířky lyží a porovnat nabídky českých obchodů.',
    intro='<p>Vázání spojuje botu s lyží a při pádu se má včas uvolnit, aby chránilo kotník a koleno. Proto se vybírá pečlivěji než jakýkoli jiný doplněk: musí odpovídat botě, šířce lyže i vaší váze a zkušenostem. Sporteka porovnává nabídky českých obchodů u sjezdových, skialpových, běžeckých a snowboardových vázání včetně dětských modelů a náhradních dílů.</p>'
          '<p>Před koupí si zapište typ a normu podrážky boty a šířku lyže. Váhu a zkušenost zadá servis při seřízení. V nabídce převažují značky ' + B(('dynafit', 'Dynafit'), ('ride', 'Ride'), ('nitro', 'Nitro'), ('salomon', 'Salomon'), ('k2', 'K2'), ('stockli', 'Stöckli')) +
          '. K vázání patří <a href="/sjezdove-lyze/">sjezdové lyže</a> a <a href="/lyzarske-boty/">lyžařské boty</a>, pro prkna <a href="/snowboardova-vazani/">snowboardová vázání</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Slovo vázání se používá pro několik odlišných výrobků, které se vzájemně nezastoupí. Podle disciplíny se mění konstrukce, váha i způsob uvolnění. Kategorie je proto širší než sjezdové vázání a před koupí si ověřte, pro co konkrétní model je.</p>'
          + T(['Typ', 'Princip', 'Použití'], [
              ['Sjezdové vázání', 'pevné předek i pata, uvolnění v obou směrech', 'sjezdovky, freeride s liftem'],
              ['Skialpové (pinové) vázání', 'špičkové piny, odpojitelná pata, režim chůze', 'výstupy a sjezdy mimo trať'],
              ['Běžecké vázání', 'upevnění jen špičky boty', 'klasika a bruslení na stopách'],
              ['Snowboardové vázání', 'popruhy nebo zadní nástup, bez uvolnění', 'snowboard, splitboard'],
              ['Dětské vázání', 'nižší hodnoty uvolnění, nastavitelná velikost', 'děti na lyžích'],
              ['Díly a doplňky', 'brzdy, popruhy, šrouby, podložky', 'servis a výměna']]) +
          '<p>Z výsledku vidíte, že se tu setkává několik světů. Pokud hledáte vázání na lyže, snowboardová ve výpisu přeskočte. Pokud potřebujete vázání na skialp, hledejte také v kategorii <a href="/skialpove-vazani/">skialpová vázání</a>, běžkaři zase v kategorii <a href="/bezecke-vazani/">běžecká vázání</a> a snowboardisté v kategorii <a href="/snowboardova-vazani/">snowboardová vázání</a>. Pomocí těchto odkazů se vyhnete záměně.</p>'
          '<h2>Sjezdové vázání: základní principy</h2>'
          '<p>Sjezdové vázání má přední část nad špičkou boty a patní část, která drží botu za patu. Při pádu se obě strany, nebo jedna z nich, uvolní, když síla překročí nastavenou hodnotu. Přední díl reaguje na boční a rotační zatížení, patní na přední náklon a svislé síly. Pro správnou funkci musí být bota čistá, bez sněhu a ledu mezi podrážkou a vázáním, a zároveň její podrážka nesmí být opotřebovaná.</p>'
          '<p>Základní údaje se odvíjejí od lyží. Většina lyží pro rekreační použití se prodává s integrovanou montážní plochou nebo s lištou, na kterou se vázání nasadí. Některé lyže jsou prodávány jako komplet s vázáním, jiné jen s plochou. Pokud kupujete samostatné vázání, ověřte, zda ho lze namontovat, a nechte to provést v servisu.</p>'
          '<h2>Hodnota DIN a nastavení</h2>'
          '<p>DIN, česky někdy uvolňovací hodnota, vyjadřuje sílu, při které se vázání otevře. Určuje se podle váhy, výšky, věku a zkušeností lyžaře a nastavuje se s přesnými měřidly. Příliš nízká hodnota způsobí nechtěné vystřelení lyže při jízdě, příliš vysoká zhorší ochranu při pádu. Proto nastavení svěřte servisu a nikdy je neodhadujte podle pocitu. Při změně hmotnosti, bot nebo úrovně hodnotu znovu zkontrolujte.</p>'
          '<ul><li><strong>Rozsah hodnot:</strong> každé vázání má horní hranici, kterou nepřekročíte. Pokročilý a těžší lyžař potřebuje model s vyšším rozsahem.</li>'
          '<li><strong>Dětská vázání:</strong> mají nižší rozsah, který je u dětí důležitý, protože jejich síla je menší.</li>'
          '<li><strong>Kontrola:</strong> před sezónou a po výrazném pádu nechte vázání zkontrolovat, podle stáří také vyměnit.</li></ul>'
          '<h2>Kompatibilita s botou a šířkou lyže</h2>'
          '<p>Nejčastější chyba je koupě vázání, které nepasuje na botu. Alpské boty se řídí starší normou s hladkou podrážkou, novější konstrukce s protiskluzovou podrážkou umožňují pohodlnější chůzi a vyžadují vázání s příslušným označením. Skialpové boty mají vlastní vložky pro pinový systém a nehodí se do každého vázání. Pokud si nejste jistí, zeptejte se obchodníka nebo se podívejte do popisu výrobce.</p>'
          '<p>Druhým faktorem je šířka lyže. Brzda vázání musí odpovídat šířce lyže pod nohou, jinak se nemůže otevřít nebo se vleče po sněhu. Výrobci nabízejí brzdy ve více šířkách a lze je vyměnit. Při koupi si poznamenejte šířku lyže uvedenou ve specifikaci a porovnejte ji s údajem brzdy. Přečtěte si také popis výrobce o rozsahu hodnoty DIN, aby vázání nebylo předimenzované nebo poddimenzované.</p>'
          '<h2>Skialpové vázání</h2>'
          '<p>Skialpová vázání se dělí na pinová a rámová. Pinová, v nabídce hojně zastoupená značkou Dynafit, drží botu kovovými špičkami zasunutými do pouzdra na špici boty. Jsou lehká a umožňují volný pohyb paty při stoupání. Rámová vázání jsou těžší a bližší sjezdovým, proto se hodí pro lyžaře, kteří chtějí stejné pocity jako na sjezdovce a sem tam si vyjdou nahoru.</p>'
          '<ul><li><strong>Hmotnost:</strong> při dlouhém výstupu se nese každý gram, lehká vázání výrazně šetří energii.</li>'
          '<li><strong>Zvedáky paty:</strong> usnadňují výstup do strmých svahů a pomáhají udržet pohodlnou polohu chodidla.</li>'
          '<li><strong>Brzdy:</strong> brzdy nebo popruhy proti ztrátě lyže. V terénu se lyže nesmí rozjet dolů.</li>'
          '<li><strong>Bezpečnost:</strong> do terénu patří lavinové vybavení a znalosti, o kterých se poraďte s odborníkem nebo kurzem.</li></ul>'
          '<h2>Snowboardová vázání</h2>'
          '<p>Snowboardová vázání se skládají z podstavce, popruhů nebo zadního nástupu a vysokého zadního opěráku. Neuvolňují se při pádu jako lyžařská, držíte se jich pevně pro kontrolu prkna. Vybírejte podle velikosti boty, stylu jízdy a typu prkna. Jízda freestyle potřebuje měkčí vázání, freeride a carving tužší. Pozor na to, aby se šrouby shodovaly s rozmístěním děr na prkně. V nabídce najdete značky Ride, Nitro, Union, Jones i další, často s barevnými provedeními pro dámy i muže.</p>'
          '<h2>Výběr podle úrovně</h2>'
          '<ul><li><strong>Začátečník a rekreační lyžař:</strong> střední rozsah DIN, jednoduchá konstrukce, vázání ve stejné řadě jako lyže.</li>'
          '<li><strong>Pokročilý:</strong> vyšší rozsah DIN, tužší konstrukce a přesnější přenos síly.</li>'
          '<li><strong>Závodník:</strong> závodní vázání s vysokými hodnotami a pevným spojením lyže.</li>'
          '<li><strong>Freerider:</strong> rámová nebo hybridní vázání, kde jde o kombinaci výstupu a sjezdu.</li>'
          '<li><strong>Děti:</strong> specializovaná vázání s nižšími hodnotami a možností úprav délky.</li></ul>'
          '<h2>Pohodlí, chůze a režim přepravy</h2>'
          '<p>Moderní vázání řeší i to, co se děje mimo sjíždění. Některá mají speciální pozici pro nasedání do boty, patu, kterou jednoduše zvednete nohou, nebo zarážku, která drží lyži u boty při chůzi. Pro skialpinismus je důležitá možnost přepnout mezi výstupem a sjezdem v rukavicích, bez sundávání lyží. Pro lyžaře, kteří často nastupují na lanovku, je výhodou snadné nasazování a viditelné značení stavu zavření.</p>'
          '<p>Pohodlí ovlivňují také podložky pod vázáním. Přidávají výšku a lepší přenos síly na hranu, ale zvyšují polohu boty nad lyží. Pro začátečníky se hodí nižší stavba, pro agresivní carving vyšší. Výška nad lyží se u jednotlivých modelů liší, proto ji porovnejte s doporučením výrobce lyží.</p>'
          '<h2>Montáž a servis</h2>'
          '<p>Namontované vázání musí být vyrovnané vůči lyži, a to přesně na pozici podle značky pro střed boty na lyži. Chybná montáž, o pár milimetrů, mění jízdní vlastnosti i bezpečnost. Servis proto použije šablonu nebo měřidlo, nastaví délku podle boty a zkontroluje uvolnění. Doma neprovádějte opravy ani výměnu pružin. Po sezóně vázání očistěte vlhkým hadříkem, osušte a skladujte v suchu. Brzdy a pohyblivé části lehce promažte přípravkem určeným pro lyžařské vázání, nikdy ne univerzálním olejem.</p>'
          '<p>Pokud kupujete použitý set, nechte vázání prohlédnout a vyzkoušet. Staré vázání ztrácí pružnost pružin, plastové části křehnou. Některé modely výrobce přestane podporovat a nebudou k nim náhradní díly.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Mezi výsledky najdete ' + B(('dynafit', 'Dynafit'), ('ride', 'Ride'), ('nitro', 'Nitro'), ('salomon', 'Salomon'), ('k2', 'K2'), ('stockli', 'Stöckli'), ('hagan', 'Hagan'), ('sp-bindings', 'SP Bindings'), ('union', 'Union'), ('atk', 'ATK'), ('jones', 'Jones')) +
          '. Dynafit představuje skialpová vázání, Ride, Nitro, Union a Jones snowboardová, Salomon se objevuje u lyžařských vázání a K2 u snowboardových. ATK a Hagan jsou zastoupeny skialpovými modely, Stöckli lyžařským příslušenstvím.</p>'
          '<h2>Související výbava</h2>'
          '<p>Ke správnému vázání patří i správně zvolené vybavení. Zvolte <a href="/lyzarske-helmy/">lyžařskou helmu</a>, <a href="/lyzarske-bryle/">brýle</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-rukavice/">rukavice</a>. Dětem pomůže <a href="/detske-lyze/">dětská lyže</a>, <a href="/lyze-komplety/">komplety lyží s vázáním</a> usnadní rozhodování. Pro péči o lyže se hodí <a href="/lyzarske-vosky/">lyžařské vosky</a> a pro přepravu <a href="/lyzarske-vaky-a-tasky/">vaky a tašky</a>. Na dlouhé túry myslete na <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nákup vázání bez kontroly kompatibility s botou.</li>'
          '<li>Nastavení DIN od oka, bez servisu.</li>'
          '<li>Použití starého vázání bez kontroly po několika sezónách.</li>'
          '<li>Záměna snowboardového a lyžařského vázání při hledání v obchodech.</li>'
          '<li>Brzda, která neodpovídá šířce lyže.</li>'
          '<li>Montáž vlastními silami bez šablony.</li></ul>'
          '<h2>Skladování a přeprava</h2>'
          '<p>Lyže s vázáním skladujte na suchém místě, ne v přetopené místnosti ani na slunci. Hodnotu uvolnění na konci sezóny neměňte, pokud to výrobce výslovně nepožaduje, a před další zimou ji nechte ověřit v servisu. Při přepravě v autě je chraňte před otlučením, nejlépe v obalu nebo ve vaku. Sníh a led z podrážek boty i vázání před nastupem do auta odstraňte, ať se zbytečně netaje na pružinách.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Na Sportece porovnáte nabídky obchodů u vázání podle značky a použití. Před koupí si zapište šířku lyží a normu podrážky boty, protože tyto údaje rozhodují o kompatibilitě. Váhu a zkušenost zadá servis při seřízení. Pokud nákup plánujete na sezónu, sledujte ukončení kolekcí. Zvlášť u skialpových modelů se vyplatí počkat na srovnání několika obchodů, protože rozdíly mezi shodnými kusy mohou být značné.</p>',
    faq=[('Jak vybrat lyžařské vázání?', 'Podle typu disciplíny, normy boty, šířky lyží a váhy a zkušeností lyžaře. Vždy ověřte kompatibilitu v popisu výrobce.'),
         ('Co znamená hodnota DIN?', 'Je to síla, při které se vázání uvolní. Nastavuje se podle váhy, výšky, věku a úrovně lyžaře.'),
         ('Mohu si vázání nastavit sám?', 'Doporučuje se servis s měřidly. Chybné nastavení může být nebezpečné v obou směrech, tedy při nechtěném uvolnění i při neuvolnění.'),
         ('Hodí se každé vázání na každou botu?', 'Ne. Záleží na podrážce boty a konstrukci vázání. Alpské, s protiskluzovou podrážkou a skialpové boty nejsou vždy zaměnitelné.'),
         ('Jaký je rozdíl mezi sjezdovým a skialpovým vázáním?', 'Skialpové má režim chůze s volnou patou a bývá lehčí, často s pinovým uchycením špičky. Sjezdové je robustnější a stavěné jen na sjíždění.'),
         ('Hodí se snowboardové vázání na lyže?', 'Ne. Snowboardová vázání se při pádu neuvolňují a mají jiný princip. Pro lyže musíte vybrat lyžařské vázání.'),
         ('Na co dát pozor u dětského vázání?', 'Na nižší rozsah uvolnění a nastavitelnou velikost. Dětem se mění váha i velikost bot, proto nechávejte nastavení kontrolovat před každou sezónou.'),
         ('Jak poznám, že brzda sedí k lyži?', 'Šířka brzdy v milimetrech musí odpovídat šířce lyže pod nohou. Příliš úzká se neotevře, příliš široká se vleče po sněhu.'),
         ('Jak často kontrolovat vázání?', 'Před každou sezónou a po silném pádu. Stará vázání ztrácejí pružnost pružin a plasty křehnou.'),
         ('Kupovat vázání samostatně nebo s lyžemi?', 'Pro rekreační lyžování se hodí komplet, protože lyže a vázání spolu ladí. Samostatné vázání je volba pro zkušené a pro výměnu.'),
         ('Kam patří vázání na běžky?', 'Do kategorie běžeckých vázání, která drží pouze špičku boty. Nejsou kompatibilní se sjezdovými ani skialpovými.')],
)
