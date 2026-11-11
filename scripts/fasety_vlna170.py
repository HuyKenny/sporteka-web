"""sporteka.cz — facet landing texts wave 170: bezky-fischer, batoh-tommy-hilfiger, adidas-kalhoty, puma-ponozky.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bezky-fischer
NEW['bezky-fischer'] = dict(
    title='Běžky Fischer: řady, skluznice a výběr podle stylu',
    desc='Běžky Fischer v nabídce českých obchodů: klasika, bruslení, šupinaté i skinové lyže, juniorské sady. Jak číst názvy řad, délku a tuhost před nákupem.',
    intro='<p>Rakouský výrobce Fischer patří k nejznámějším jmenovkám v běžeckém lyžování a jeho lyže potkáte od rodinných stop po závodní tratě. Pro nákup je užitečné vědět, že názvy řad nejsou marketingová ozdoba, ale hrubé třídění: Crown znamená šupinatou skluznici bez mazání, Twin Skin pás se skinovým záběrem, Skate lyži na bruslení a čísla či slova jako Sport, Pro a Race určují míru výkonu. '
          'Tato stránka shrnuje sortiment značky v kategorii <a href="/bezecke-lyze/">běžecké lyže</a>, vysvětluje, jak se řady liší, a radí s délkou, tuhostí a vázáním. Samostatně se vyplatí srovnat i <a href="/bezky-rossignol/">běžky Rossignol</a>, pokud váháte mezi dvěma výrobci. Přehled všech modelů značky je také na stránce <a href="/znacka/fischer/">Fischer</a>.</p>',
    guide='<h2>Jak číst názvy lyží Fischer</h2>'
          '<p>Katalog značky působí chaoticky, protože jedno jméno se opakuje v několika kombinacích. Základ je jednoduchý: první slovo určuje řadu nebo skluznici, další popisuje tuhost, a nakonec se uvádí vázání, se kterým je lyže prodávána. Například označení typu Twin Skin Medium s vázáním Control Step říká, že jde o klasickou lyži se skinovým pásem, střední tuhosti a s vázáním pro rekreační až sportovní jízdu.</p>'
          + T(['Část názvu', 'Co obvykle znamená', 'Na co si dát pozor'], [
              ['Crown', 'šupinatá skluznice, záběr zajišťuje struktura, mazání odpadá', 'v hlubším sněhu nebo při mrazu klouže méně spolehlivě než vosk'],
              ['Twin Skin', 'pás ve stopě s mohérovým nebo syntetickým vlasem, bez vosku', 'pásy je třeba čistit a chránit před nečistotami a zbytky vosku'],
              ['Skate', 'bruslařská lyže, skluznice po celé délce', 'potřebuje upravenou bruslařskou dráhu a jiné boty než klasika'],
              ['Combi', 'kompromis pro klasiku i bruslení', 'v obou stylech výkonově zaostává za specializovanou lyží'],
              ['EF', 'varianta určená pro rekreační jízdu s vázáním v sadě', 'ověřte, zda jsou boty ve stejném vázacím systému'],
              ['Junior, JR', 'dětské a mládežnické délky', 'vybírejte podle výšky a síly dítěte, ne podle věku']]) +
          '<p>Rozlišujte také model a sezónu. Řady se tu a tam přeznačují a starší ročník bývá zcela srovnatelný s novým, protože se mění hlavně grafika. Rozdíl dělají vzácněji tvar špičky nebo materiál jádra, což výrobce uvádí v popisu.</p>'
          '<h2>Šupinaté lyže Crown a pásy Twin Skin</h2>'
          '<p>Většina lidí, kteří si koupí lyže na víkendové běhání, nechce řešit vosky. Pro ně jsou řady Crown logickou volbou. Skluznice v záběrové zóně nese šupiny, které se při došlápnutí zachytí o sníh, a při skluzu hladce kloužou. Výhodou je, že lyže stačí přijet ze sklepa a vyrazit. Nevýhodou je, že při teplotách kolem nuly a mokrém sněhu mohou šupiny namrzat a v nadšení z přímého výkonu zaostávají za mazanou lyží.</p>'
          '<p>Pás Twin Skin jde o krok dál. Záběr tu vytváří vlas ve stopě, který se v jednom směru položí a ve druhém zachytí. Jízda je tišší a lyže stoupá do kopce s menší námahou než šupinatá. Musíte ale s lyží zacházet jemněji: neodkládejte ji mokrou na topení, neškrábejte pásy ostrými předměty a po sezóně je očistěte. Pokud se vám pás opotřebí, lze ho často vyměnit a nemusíte kupovat nové lyže, ověřte si to ale u konkrétního modelu.</p>'
          '<h3>Kdy zvolit mazanou lyži</h3>'
          '<p>Závodní modely, například odvozené od řad RC nebo Speedmax, bývají určené k mazání. Vosk vám dá lepší záběr v proměnlivých podmínkách a lepší skluz, ale vyžaduje zkušenost, správně zvolený vosk a čas na přípravu. Začátečníkovi dává smysl mazaná lyže až ve chvíli, kdy ho bavení pravidelných tréninků a zajímají ho minuty na trati. Doplňky najdete v kategorii <a href="/lyzarske-vosky/">lyžařské vosky</a>.</p>'
          '<h2>Klasika, nebo bruslení</h2>'
          '<p>Klasický styl se jezdí v zapuštěných stopách a je pro většinu rekreačních jezdců přirozenější, připomíná zrychlenou chůzi. Bruslení probíhá po široké upravené ploše a připomíná bruslení na ledě. Je rychlejší, ale technicky náročnější a vyžaduje trasu s bruslařskou dráhou, což nemají všechny běžecké okruhy. Lyže pro oba styly se liší délkou, tuhostí i skluznicí, proto je nelze zaměňovat.</p>'
          + T(['Kritérium', 'Klasické lyže', 'Bruslařské lyže'], [
              ['Délka', 'delší, přibližně do výšky zvednuté ruky', 'kratší, zhruba do výšky očí až čela'],
              ['Skluznice', 'střed s záběrovou zónou', 'hladká po celé délce'],
              ['Tuhost', 'dvojí prohnutí, měkčí', 'tužší, rovnější'],
              ['Hole', 'kratší, do výše podpaží', 'delší, kolem úrovně brady'],
              ['Terén', 'stopa i neupravený sníh', 'upravená široká plocha']]) +
          '<p>Značka nabízí v obou stylech modely pro všechny úrovně, od hobby sad po lehké závodní skate lyže s uhlíkovým jádrem. Pokud chcete začít, jsou praktické sady s vázáním, protože ušetří čas s kompatibilitou. Více o stylech a technice najdete v průvodci <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</p>'
          '<h2>Délka a tuhost: tabulka a pravidla</h2>'
          '<p>Při výběru délky se dívejte na výšku lyžaře a na jeho váhu. Tuhost se zapisuje slovy jako Soft, Medium nebo Stiff a podle jednoho slova se nikdy nerozhoduje. Tuhá lyže vyžaduje silnější odraz a těžšího lyžaře, jinak se nedotkne záběrovou zónou sněhu a nedrží. Příliš měkká lyže naopak nese záběr trvale ve sněhu a brzdí. Výrobce uvádí rozsah hmotnosti u každé délky a tabulku vždy raději ověřte, než si vyberete podle kolegy.</p>'
          '<ul><li><strong>Přesně podle váhy:</strong> hmotnost lyžaře s oblečením a batohem určuje tuhost silněji než výška.</li>'
          '<li><strong>Test na papír:</strong> postavte se na lyže a zkuste podsunout list papíru pod záběrovou zónu; má se uvolnit při stání na obou lyžích a zachytit při stání na jedné.</li>'
          '<li><strong>Nižší tuhost pro začátek:</strong> měkčí lyže odpustí chyby v odrazu a lépe drží, i když jsou o kus pomalejší.</li>'
          '<li><strong>Sportovní ambice:</strong> Medium a Stiff mají smysl pro lidi, kteří se odrážejí s plnou silou.</li></ul>'
          '<h2>Vázání a boty: kompatibilita rozhoduje</h2>'
          '<p>U lyží z nabídky často nacházíte označení jako Tour Step, Control Step nebo Race Classic. Jde o vázání a systém jeho připojení na lyži. Dnes se v rekreační oblasti používají především systémy NNN a podobné, ale boty a vázání musí ladit. Než objednáte, ověřte, jakou botu máte nebo kupujete, a zda vázání odpovídá. Výběr navazujících kusů najdete v kategoriích <a href="/bezecke-boty/">běžecké boty</a> a <a href="/bezecke-vazani/">běžecká vázání</a>. Pro klasiku kupujte boty s vyšší a měkčí podrážkou, pro bruslení boty s pevnou vyšší kotníkovou částí.</p>'
          '<h2>Juniorské a dámské modely</h2>'
          '<p>V sortimentu se objevují juniorské lyže, často prodávané jako kompletní sady, a dámské řady označené například jako Inspire. Dětské lyže bývají kratší a velmi měkké, aby se dítě zvládlo odrazit. Kupujte s malou rezervou délky, ne s velkou: příliš dlouhá lyže se hůř ovládá a odrazí ji jen těžší dítě. Mladší děti se naučí rychleji na šupinaté lyži, protože nemusí řešit mazání ani údržbu pásů. Další výběr dětských lyží najdete v kategorii <a href="/detske-lyze/">dětské lyže</a>.</p>'
          '<h2>Skluznice, servis a skladování</h2>'
          '<p>Skluznice je nejcitlivější část lyže. Nejde jen o vzhled: nasekané rýhy a oděrky zpomalují skluz a odřený nebo vyschlý plast nasává vosk hůř. Před sezónou lyže prohlédněte, případně nechte zaservisovat a opatřit základním voskem. Mezi výlety lyže otřete, uložte je v chladné suché místnosti a nikdy neodkládejte mokré na zdroj tepla. Zafixujte je k sobě pružným popruhem, aby se předpětí nesnižovalo. Pásy Twin Skin není vhodné mazat skluzovým voskem, protože ztrácejí záběr.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejný model se nabízí v několika délkách a s různým vázáním, proto při srovnání cen porovnávejte celé označení včetně délky, tuhosti a sezóny. Pokud je označení zkrácené, vyhledejte katalogové číslo na webu výrobce. U sad zkontrolujte, zda jsou součástí hole, a pokud ne, doplňte je z kategorie <a href="/lyzarske-hole/">lyžařské hole</a>. K lyžím se hodí také <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, aby se v botě noha netřela. Slevy se objevují hlavně na konci zimy a při přechodu na nový ročník, kdy se výprodejem uvolňují starší grafiky.</p>',
    faq=[
        ('Jaký je rozdíl mezi řadami Crown a Twin Skin?', 'Crown má v záběrové zóně šupiny, které se při došlápnutí zachytí o sníh. Twin Skin používá pás s vlasem, který se v jednom směru položí a v opačném zachytí. Pás bývá tišší a tlumeněji klouže do kopce, šupiny jsou odolnější a nevyžadují zvláštní péči.'),
        ('Musím lyže Fischer mazat?', 'Šupinaté Crown a pásové Twin Skin lyže mazat nemusíte, jsou na to navržené. Mazat se obvykle dávají závodní klasické modely a bruslařské lyže, kterým se na skluznici nanáší skluzný vosk. Na záběrovou část pásů se vosk nikdy nenanáší.'),
        ('Jak zvolit délku klasických lyží?', 'Klasické lyže mají být přibližně tak dlouhé, jak dosáhnete zvednutou rukou, ale důležitější je váha. Každá délka má v tabulce výrobce rozsah hmotnosti, ve kterém lyže správně pracuje. Zvolte model, do jehož rozsahu se vejdete i s oblečením.'),
        ('Je lepší klasika, nebo bruslení pro začátečníka?', 'Většině začátečníků vyhovuje klasika, protože se jede v připravené stopě a pohyb se učí intuitivně. Bruslení je rychlejší, ale náročnější na techniku a rovnováhu. Pokud vaše trasa nemá upravenou bruslařskou plochu, bruslařské lyže nevyužijete.'),
        ('Pasují boty jiné značky na vázání Fischer?', 'Záleží na systému, ne na značce. Boty a vázání musí patřit do stejného systému, například NNN nebo jeho variant. Před nákupem zkontrolujte označení u vázání i u bot, protože sady jsou prodávány s konkrétním typem. Pokud si nejste jistí, porovnejte popisy v kategoriích bot a vázání.'),
        ('Jak vybrat lyže pro dítě?', 'Dětské lyže jsou kratší a měkčí, aby se je dítě naučilo ovládat. Vybírejte podle výšky a síly, ne podle věku, a nechte jen drobnou rezervu, protože příliš dlouhá lyže komplikuje učení. Sady s vázáním šetří čas a odpadá nutnost řešit kompatibilitu.'),
        ('Dá se vyměnit opotřebovaný pás Twin Skin?', 'U některých modelů ano, výrobce nebo servis pás vymění a lyže se tak oživí. Nejde o univerzální pravidlo, proto se před koupí ptejte na dostupnost náhrady konkrétního modelu. Pás prodlouží život hlavně šetrné zacházení a čištění po každé sezóně.'),
        ('Jak uložit běžky přes léto?', 'Otřete skluznici, zbavte lyže nečistot a uložte je v suché a chladné místnosti, ne na slunci a ne u topení. Svažte je k sobě tak, aby se mezi nimi zachoval prostor pod vázáním. Skluznici lze před uložením ošetřit základním voskem, který ji ochrání před vyschnutím.'),
        ('Kdy se běžky nejvýhodněji kupují?', 'Nejširší výběr velikostí bývá na začátku sezóny, výprodeje starších ročníků obvykle probíhají od konce zimy. Při slevě rychle mizí hlavně nejběžnější délky, proto si předem zjistěte svou velikost a tuhost. Starší ročník je vedle nového často shodný, liší se většinou jen grafikou.'),
    ])

# ------------------------------------------------------------------ batoh-tommy-hilfiger
NEW['batoh-tommy-hilfiger'] = dict(
    title='Batoh Tommy Hilfiger: městské, školní a Tommy Jeans',
    desc='Batoh Tommy Hilfiger: městské modely Essential a Established, dětské a dámské, pánské. Jak vybrat objem, materiál a kapsu na notebook, ověřit pravost.',
    intro='<p>Tommy Hilfiger je americká módní značka a jeho batohy jsou především městské: ladí s oblečením, jsou z technických tkanin či imitace kůže a nesou výrazné logo v červenomodrobílé kombinaci. Nejsou určené k vícedenním trekům, ale k dojíždění, škole, kanceláři a víkendu. '
          'V nabídce převládají tmavě modré a černé odstíny, vedle toho se objevují dětské, dámské a pánské verze a řada Tommy Jeans s Essential a Hybrid. Tato stránka pomůže vybrat objem a materiál, rozlišit řady a ověřit pravost. Obecné rady k výběru najdete v kategorii <a href="/batohy/">batohy</a> a v podkategorii <a href="/mestske-batohy/">městské a sportovní batohy</a>. Pokud hledáte podobné módní modely od sportovních značek, porovnejte stránky <a href="/nike-batoh/">Nike</a> nebo <a href="/adidas-batoh/">Adidas</a>.</p>',
    guide='<h2>Co od batohu Tommy Hilfiger čekat</h2>'
          '<p>Značka vychází z klasického amerického stylu a batohy zdědily jeho jednoduchost: čistý tvar, minimum zbytečných popruhů, kontrastní lemování a logo na čelní straně. Nenajdete tu nosné systémy s bederním pásem ani ventilační rámy. Najdete praktické, lehké a snadno čistitelné batohy, které se dobře nosí denně v tramvaji, do školy nebo do práce.</p>'
          + T(['Řada nebo typ', 'Charakter', 'Pro koho'], [
              ['Essential, Dome', 'nylonový nebo polyesterový městský batoh, zaoblený tvar', 'každodenní dojíždění a škola'],
              ['Hybrid, Established', 'strukturovanější vzhled, jemné materiály', 'kancelář a reprezentativnější příležitosti'],
              ['Tommy Jeans', 'sportovnější a mladší vzhled, výraznější nápis', 'studenti a volný čas'],
              ['Dámské, z imitace kůže', 'menší, tvarované, lesklý nebo měkký povrch', 'město, společenské akce'],
              ['Dětské a školní', 'menší objem, jednodušší vnitřek', 'mladší žáci, výlety']]) +
          '<p>Názvy v nabídkách nejsou vždy jednotné. Prodejci tentýž model označují jako Backpack, batoh nebo městský batoh a barvu uvádějí v názvu. Při srovnání proto spoléhejte na kód modelu a rozměry, ne na slovo v titulku.</p>'
          '<h2>Materiály a péče</h2>'
          '<p>Většina batohů je z polyesteru nebo nylonu s polyuretanovou vrstvou, která odpuzuje drobný déšť. Plnohodnotně voděodolné nejsou, takže při dlouhém lijáku může zatéct švy a zipem, a notebook proto patří do vnitřní polstrované kapsy, ne do přední. Modely z imitace kůže vypadají reprezentativně, ale vyžadují jinou péči: otírají se vlhkým hadříkem, nesnášejí ostré hrany a horko a při dlouhém tření v místě popruhů se povrch může odlupovat.</p>'
          '<ul><li><strong>Textilní batoh:</strong> očistěte vlhkým hadříkem a jemným mýdlem, pračku používejte jen při výslovném povolení výrobce.</li>'
          '<li><strong>Imitace kůže:</strong> otřete a nechte oschnout vzdušně, nepoužívejte rozpouštědla.</li>'
          '<li><strong>Zip:</strong> občas jej očistěte kartáčkem, aby nevázl.</li>'
          '<li><strong>Logo:</strong> potištěné nebo vyšité logo žehlete jen na rubu.</li></ul>'
          '<h2>Jaký objem zvolit</h2>'
          '<p>Městské batohy se pohybují v rozmezí zhruba od deseti do třiceti litrů, ale značka většinou neuvádí přesný objem, jen rozměry. Proto je užitečné domýšlet si, co do batohu dáte. Malý model pojme peněženku, telefon, láhev a svačinu, střední notebook a sešity, větší přibalí i oblečení na převlečení. Pokud nosíte notebook, změřte jeho úhlopříčku a porovnejte ji s popisem vnitřní kapsy, protože patnáctipalcový stroj do menšího městského batohu často nevejde.</p>'
          + T(['Co nosíte', 'Co hledat v popisu'], [
              ['Telefon, peněženka, láhev', 'malé rozměry, jedna hlavní komora, přední kapsa na zip'],
              ['Notebook a dokumenty', 'polstrovaná kapsa na notebook, vyztužená záda'],
              ['Sportovní oblečení do posilovny', 'větší hlavní komora, oddělená kapsa na mokré věci'],
              ['Školní pomůcky', 'pevné dno, penálová kapsa, široké popruhy'],
              ['Víkend a krátký výlet', 'větší objem, boční kapsy, madlo nahoře']]) +
          '<h2>Pánský, dámský a dětský batoh</h2>'
          '<p>Rozdíl mezi pohlavími je u městských batohů menší než u turistických. Pánské modely bývají širší a pravoúhlejší, dámské užší a zaoblenější, často v jemnějších barvách nebo s lesklým povrchem. Střihem se liší spíš ramenní popruhy: u dámských bývají užší a kratší, aby nesklouzávaly. Dětský batoh se pozná podle menších rozměrů a jednodušší výbavy; u školáků dbejte, aby plný batoh nebyl příliš těžký a aby měl pevnější záda. Další výběr najdete v kategoriích <a href="/skolni-batohy/">školní batohy</a> a ve výběrech <a href="/damsky-batoh/">dámský batoh</a> a <a href="/pansky-batoh/">pánský batoh</a> a <a href="/detsky-batoh/">dětský batoh</a>.</p>'
          '<h2>Barvy: tmavě modrá, černá a ostatní</h2>'
          '<p>V katalogu značky vede tmavě modrá a černá. Tmavě modrá je spojená s identitou značky a hodí se ke džínům i k saku, černá skrývá otěr a skvrny a je univerzální. Světlejší nebo sytější barvy, třeba oranžová nebo khaki, se nosí hlavně jako módní doplněk a rychle ukážou zašpinění, zejména u dna. Nechcete-li řešit údržbu, vyberte tmavý model. Podobný výběr černých kusů je v kategorii <a href="/cerny-batoh/">černý batoh</a>.</p>'
          '<h2>Jak poznat pravý batoh</h2>'
          '<p>Značkové batohy bývají často napodobované. Pomoci může několik jednoduchých kontrol, které ale neplatí absolutně a nenahrazují nákup u ověřeného prodejce.</p>'
          '<ul><li><strong>Šití:</strong> rovné, husté stehy bez uvolněných nitek, zejména u popruhů a v rozích.</li>'
          '<li><strong>Logo:</strong> písmo je symetrické, barvy čisté a okraje přesné.</li>'
          '<li><strong>Zipy a kování:</strong> těžší kov, hladký chod, často s rytým názvem výrobce.</li>'
          '<li><strong>Štítek uvnitř:</strong> čitelný štítek s kódem a zemí původu, bez překlepů.</li>'
          '<li><strong>Prodejce:</strong> ověřený obchod s jasnou reklamační politikou, ne anonymní inzerát.</li></ul>'
          '<p>Nepřiměřeně nízká nabídka u novinky bývá varování. V přehledu proto sledujte, zda se nabídka pohybuje v běžné hladině u více obchodů. Nejistý prodejce je horší než rozdíl pár korun.</p>'
          '<h2>Srovnání se sportovními značkami</h2>'
          '<p>Batohy módní značky stavějí na vzhledu a značce, sportovní firmy více na funkci. Značky jako <a href="/nike-batoh/">Nike</a>, <a href="/adidas-batoh/">Adidas</a> nebo <a href="/under-armour-batoh/">Under Armour</a> nabízejí obvykle lépe vyztužená záda, prodyšný polstr a oddělené kapsy na boty nebo láhev, zatímco módní řada klade důraz na tvar a barvu. Pokud se do batohu chystáte vtěsnat posilovnu, vyplatí se sportovní model. Pokud batoh nosíte do kanceláře a na něj potřebujete elegantní vzhled, má Tommy Hilfiger smysl. Pro vícedenní túry zvolte raději <a href="/turisticke-batohy/">turistický batoh</a>.</p>'
          '<h2>Jak batoh správně nosit</h2>'
          '<p>Městský batoh bez bederního pásu zatěžuje ramena, proto těžké věci dávejte blízko zad a popruhy utáhněte tak, aby batoh seděl v oblasti lopatek. Nošení na jednom rameni vypadá přirozeně, ale při pravidelné zátěži unavuje jednu stranu těla. Pokud nosíte notebook, vložte ho do vnitřní kapsy k zádům. Hrudní popruh městské modely většinou nemají, takže se vyplatí nenosit těžké věci.</p>',
    faq=[
        ('Je batoh Tommy Hilfiger vhodný na túru?', 'Ne, je to městský a módní batoh bez bederního pásu a ventilovaných zad. Hodí se na dojíždění, do školy, kanceláře či na výlet po městě. Na delší pěší túry zvolte turistický batoh s nosným systémem, který přenese váhu na kyčle.'),
        ('Jak velký objem batohy Tommy Hilfiger mají?', 'Výrobce a obchody často uvádějí spíš rozměry než litry. Modely se pohybují od malých batůžků po velikost běžného školního nebo kancelářského batohu. Před koupí porovnejte rozměry s věcmi, které chcete nosit, zejména s úhlopříčkou notebooku.'),
        ('Vejde se do něj notebook?', 'Řada městských modelů má vnitřní polstrovanou kapsu, ale ne všechny, a velikost se liší. Ověřte údaj o maximální úhlopříčce v popisu. Notebook patří k zádům a do vnitřní kapsy, aby ho při dešti a nárazech chránila hlavní komora.'),
        ('Je batoh voděodolný?', 'Většina modelů má materiál s úpravou odpuzující lehký déšť, ale švy a zipy nejsou těsněné. Při dlouhém lijáku může voda proniknout. Citlivé věci chraňte pláštěnkou nebo vnitřním sáčkem a notebook nenoste v přední kapse.'),
        ('Jak poznám originál?', 'Zkontrolujte rovnost šití, přesnost loga, kvalitu zipů a štítek uvnitř. Nejspolehlivější je koupit u ověřeného prodejce s jasnou reklamací. Výrazně nižší nabídka než u ostatních obchodů je varovný signál.'),
        ('Čím se liší pánský a dámský batoh?', 'Dámské modely bývají užší, zaoblenější a s užšími popruhy, pánské širší a pravoúhlejší. U městských batohů je rozdíl menší než u turistických, takže vybírejte podle pohodlí a velikosti. Mnoho modelů je prakticky unisex.'),
        ('Jak vyčistit batoh Tommy Hilfiger?', 'Textilní materiál očistěte vlhkým hadříkem a jemným mýdlem, pak nechte vyschnout rozevřený. Imitaci kůže stačí otřít vlhkým hadříkem a nepoužívat rozpouštědla. Pračka často poškodí výztuže, lepené části i potisk.'),
        ('Hodí se do školy i pro děti?', 'Dětské a školní modely jsou menší a lehčí, ale zkontrolujte vyztužení zad a šířku popruhů. Plný batoh by neměl být příliš těžký. Pro starší školáky se hodí i městský model s kapsou na notebook.'),
        ('Jaká barva je nejpraktičtější?', 'Tmavě modrá a černá skryjí otěr a drobné skvrny a hodí se ke všemu. Světlé nebo syté barvy jsou módní, ale rychle ukážou zašpinění zejména u dna. Barva nijak neovlivňuje funkci ani nosnost.'),
    ])

# ------------------------------------------------------------------ adidas-kalhoty
NEW['adidas-kalhoty'] = dict(
    title='Adidas kalhoty: tepláky, tréninkové a Terrex',
    desc='Adidas kalhoty: tepláky Essentials, tréninkové Tiro a Entrada, běžecké a outdoorové Terrex. Rozdíly střihů, materiálů a velikostí pro muže, ženy a děti.',
    intro='<p>Pod hlavičkou Adidas se skrývají čtyři různé světy: pohodlné bavlněné tepláky na doma, tréninkové kalhoty pro fotbal a kolektivní sporty, běžecké a fitness střihy a outdoorové kalhoty Terrex na hory. Každý svět má jiný materiál, střih a technické vlastnosti, proto se vyplatí rozlišit je, než kliknete na nabídku. '
          'Tato stránka vysvětluje, co znamenají řady Essentials, Tiro, Entrada, Squadra a Terrex, jak se liší pánské, dámské a dětské střihy a podle čeho vybírat velikost. Základní průvodce najdete v kategorii <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, specializované výběry pak u <a href="/teplaky/">tepláků</a> a <a href="/outdoorove-kalhoty/">outdoorových kalhot</a>. Pro srovnání se podívejte na <a href="/nike-kalhoty/">kalhoty Nike</a> a <a href="/puma-kalhoty/">kalhoty Puma</a>.</p>',
    guide='<h2>Čtyři skupiny kalhot Adidas</h2>'
          '<p>Katalog značky je rozsáhlý a v názvech se opakují slova, která jsou ve skutečnosti kódem pro použití. Pomůže tabulka, ze které poznáte, kam model patří, ještě než otevřete fotografii.</p>'
          + T(['Řada nebo slovo v názvu', 'Typ kalhot', 'Typické použití'], [
              ['Essentials, French Terry, Feel Cozy', 'měkké úplety s vnitřním žíháním', 'volný čas, doma, lehký trénink'],
              ['Tiro, Squadra, Entrada', 'tréninkové kalhoty z polyesteru, často se zipy na nohavicích', 'fotbal, tréninky, rozcvičky'],
              ['Woven, Stadium, Train', 'tenké tkané kalhoty, rychle schnou', 'fitness, venkovní trénink, vrstvení'],
              ['Own The Run, adi365', 'běžecké a lehké sportovní střihy', 'běh a svižná chůze'],
              ['Terrex', 'outdoorové kalhoty, často pružné nebo s ochranou proti dešti', 'túry, cestování, hory'],
              ['Joggers, Cuffed', 'zúžená nohavice s náplety', 'město, tréninky, děti']]) +
          '<p>Slovo Pants označuje všechny kalhoty bez rozlišení. Název Joggers znamená zúžený střih, pro který je typický elastický lem. Ke kalhotám se často prodává i souprava, takže ověřte, zda cena a velikost patří k samotným kalhotám, nebo k setu.</p>'
          '<h2>Tepláky z řady Essentials</h2>'
          '<p>Nejčastější adidasky v nabídce jsou tepláky s tříproužkem nebo malým logem. Materiál bývá směs bavlny a polyesteru, uvnitř žíhaný nebo hladký. Bavlna je měkká a příjemná na kůži, polyester přidává tvarovou stálost a menší sráživost. Tepláky z French Terry mají hladký vnější povrch a smyčkový rub, zatímco fleecové varianty jsou teplejší a nadýchané. Hodí se doma, do města i na lehký trénink, ale při intenzivním potu bavlněné směsi pomaleji schnou.</p>'
          '<p>Pokud je cílem cvičení, ptejte se, zda je materiál určený pro sport, nebo pro volný čas. Na tréninkových kalhotách bývá poznámka o odvádění vlhkosti, u teplákových modelů ji nenajdete. Více o rozdílech mezi typy tepláků je v kategorii <a href="/teplaky/">tepláky</a>.</p>'
          '<h2>Tréninkové kalhoty pro fotbal a týmové sporty</h2>'
          '<p>Řady Tiro, Squadra a Entrada vychází z fotbalového prostředí, kde se trénuje venku většinu roku. Kalhoty jsou z lehkého polyesteru, mívají užší nohavice, zip u kotníku, aby se daly obléct přes kopačky, a kapsy na zip na uložení klíčů. Zúžení u kotníku drží kalhoty u nohy, takže nepřekáží při běhu. Pod ně se v zimě obléká termoprádlo, přes ně nepromokavé bundy. Pokud hledáte i související oblečení, sledujte <a href="/damske-sportovni-kalhoty/">dámské sportovní kalhoty</a> a <a href="/panske-sportovni-kalhoty/">pánské sportovní kalhoty</a>.</p>'
          '<ul><li><strong>Zip na nohavici:</strong> usnadní oblékání přes obuv, ale může při sedu tlačit.</li>'
          '<li><strong>Kapsy na zip:</strong> drží klíče při běhu a neztrácejí se věci.</li>'
          '<li><strong>Pružný pas se šňůrkou:</strong> dovolí přizpůsobit kalhoty při pohybu.</li>'
          '<li><strong>Úzká nohavice:</strong> nezaklesne se do kotníku, ale omezuje při širokých pohybech.</li></ul>'
          '<h2>Terrex: outdoorové kalhoty</h2>'
          '<p>Terrex je venkovní řada značky. Kalhoty z ní jsou obvykle z pružných tkanin, snáší otěr a rychle schnou. Modely s označením Climaproof nebo Rain jsou určené k ochraně před deštěm a hodí se jako vrchní vrstva při dlouhém pochodu, zatímco Multi je univerzálnější typ pro túry a cestování. Pružnost Liteflex přidává volnost kroku při lezení přes kameny. Jde o skutečné outdoorové kalhoty, proto neočekávejte měkkost teplákové bavlny. Pro delší výlety srovnejte i s kategorií <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, kde jsou i další značky, například <a href="/hannah-kalhoty/">Hannah</a> nebo <a href="/kilpi-kalhoty/">Kilpi</a>.</p>'
          '<h2>Pánské, dámské a dětské střihy</h2>'
          '<p>Pánské kalhoty mají rovnější a širší střih v bocích, dámské jsou užší v pase a přizpůsobené šířce boků a délce nohy. Dámské a pánské velikosti se neshodují a převodem se mnohdy nedostanete tam, kam byste chtěli. Dětské kalhoty jsou označeny věkem nebo výškou, a protože děti rostou rychle, bývá lepší jít podle výšky. Zúžené dětské joggery zůstávají na dítěti i při hře. Na růst se vyplatí kupovat o číslo větší, nohavici lze v případě potřeby jednou přehrnout. Další rodiny najdete u <a href="/detske-sportovni-kalhoty/">dětských sportovních kalhot</a>.</p>'
          + T(['Skupina', 'Střih', 'Co ověřit'], [
              ['Pánské', 'rovnější bok, širší stehno', 'délka nohavice podle výšky a rozdíl mezi úzkým a volným střihem'],
              ['Dámské', 'užší pas, přizpůsobený bok', 'výška pasu a obvod boků v tabulce'],
              ['Dětské', 'volnější, s pružným pasem', 'výška dítěte místo věku'],
              ['Unisex', 'volný, bez výrazného tvarování', 'rozdíl mezi dámskými a pánskými velikostmi']]) +
          '<h2>Jak vybrat velikost u Adidas</h2>'
          '<p>Velikostní tabulka značky uvádí obvod pasu, boků a délku nohavice. Vybírejte ji podle míry, ne podle zvyku z jiné značky. Rozdíl mezi úzkým a volným střihem je u značky na první pohled znatelný, ale při nákupu je třeba hledat slova jako Slim, Regular nebo Loose, protože ne všechny prodejny je uvádějí. Pokud váháte mezi dvěma velikostmi, vezměte větší u bavlněných tepláků, které se po praní mohou smrštit, a stávající u polyesterových tréninkových kalhot.</p>'
          '<h2>Péče o sportovní kalhoty</h2>'
          '<ul><li>Perte na rubu při doporučené teplotě, aby se neodřel potisk a lícní strana.</li>'
          '<li>Nepoužívejte aviváž u technických materiálů, snižuje schopnost odvádět vlhkost.</li>'
          '<li>Zip před praním zapněte, aby neodíral okolní látky.</li>'
          '<li>Terrex kalhoty s impregnací občas obnovte impregnačním prostředkem.</li>'
          '<li>Nesušte na topení; žár deformuje pružné tkaniny a nálepky.</li></ul>'
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>Adidas je v kalhotách výraznější v týmových sportech a ve volném čase, kde stojí především na středním střihu a logu s třemi pruhy. <a href="/nike-kalhoty/">Nike</a> se přiklání k lehčím sportovním materiálům, <a href="/puma-kalhoty/">Puma</a> k módnímu volnému času. Outdoorově silnější jsou specializované značky jako <a href="/fjallraven-kalhoty/">Fjällräven</a> nebo <a href="/dynafit-kalhoty/">Dynafit</a>. Pokud chcete jediné univerzální kalhoty, zvolte černý rovný střih; hledáte-li volnější styl, hodí se <a href="/cerne-siroke-kalhoty/">černé široké kalhoty</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi teplákovými a tréninkovými kalhotami Adidas?', 'Tepláky z řady Essentials jsou měkké, z bavlněných směsí a určené pro volný čas. Tréninkové kalhoty Tiro nebo Entrada jsou z lehkého polyesteru, rychle schnou a mají úzké nohavice se zipem. Na sport je lepší technický materiál, na doma bavlna.'),
        ('Co znamená Terrex v názvu kalhot?', 'Terrex je outdoorová řada značky určená na túry, cestování a hory. Kalhoty jsou z pružných nebo voděodolných tkanin, bývají odolnější než běžné tepláky. Neočekávejte vnitřní fleecový povrch, jde o venkovní oblečení.'),
        ('Jak vybrat velikost Adidas kalhot?', 'Podívejte se do tabulky výrobce a porovnejte svůj obvod pasu, boků a délku nohy. Velikosti neodvozujte od jiné značky ani od dámského nebo pánského označení. U bavlněných směsí volte raději větší velikost, protože se mohou po praní mírně smrštit.'),
        ('Jsou kalhoty Adidas pro muže a ženy jiné?', 'Ano, dámské kalhoty mají užší pas a přizpůsobený bok, pánské rovnější střih. Existují i unisex modely, které se řídí spíš volným střihem. Při nákupu zkontrolujte tabulku konkrétní řady, protože se mohou lišit.'),
        ('Hodí se tepláky Adidas na běh?', 'Bavlněné tepláky na běh nejsou nejlepší, protože pomalu schnou a při potu těžknou. Pro běh vybírejte modely z řad pro běžce nebo tkané lehké kalhoty. Pro rozcvičku nebo zimní běh pod bundou ale poslouží i tréninkové polyesterové kalhoty.'),
        ('Dají se Terrex kalhoty nosit do města?', 'Ano, mnohé modely mají nenápadný střih a hodí se na cestování i denní chůzi. Mají ale technický povrch, který šustí a nemusí působit tak měkce jako tepláky. Pro každodenní komfort stačí běžná řada Essentials.'),
        ('Jak vybrat dětské kalhoty Adidas?', 'Rozhodujte se podle výšky dítěte, ne podle věku. Nechte malou rezervu v nohavicích a zvolte pružný pas, ať kalhoty vydrží i růst. Zúžený střih joggers zůstává u kotníku, takže dítě nezakopává.'),
        ('Jak prát sportovní kalhoty?', 'Perte na rubu při doporučené teplotě, zapněte zipy a nepoužívejte aviváž u technických materiálů. Sušte volně, ne na topení ani v horké sušičce. Impregnované kalhoty občas ošetřete obnovovacím prostředkem.'),
        ('Mohu kalhoty Adidas vrstvit se zimním oblečením?', 'Ano, tréninkové kalhoty se zimou nosí přes termoprádlo a pod nepromokavé kalhoty při dešti. Úzké nohavice usnadňují vrstvení, jen si dejte pozor, aby kalhoty nesvíraly. Pro mráz hledejte fleecové varianty nebo teplejší spodní vrstvu.'),
    ])

# ------------------------------------------------------------------ puma-ponozky
NEW['puma-ponozky'] = dict(
    title='Puma ponožky: balení, délky a výběr podle sportu',
    desc='Puma ponožky v balení po 2, 3 i 5 párech: nízké sneaker, quarter, crew a fotbalové štulpny. Jak vybrat délku, materiál a velikost a porovnat obchody.',
    intro='<p>Ponožky Puma se prodávají hlavně v multibalení po dvou, třech nebo pěti párech, a to v několika délkách: neviditelné sneaker, kotníkové quarter, vyšší crew a dlouhé fotbalové štulpny. Pod jednou značkou tak najdete věci pro tenisky, běh, trénink i každodenní nošení. '
          'Tato stránka vysvětluje rozdíly mezi délkami nízkých i vysokých střihů, k čemu se jednotlivé řady hodí, jak číst označení typu 3P a jak vybrat správnou velikost. Obecný průvodce materiály, švy a zesílenými zónami najdete v kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a>, tady se soustředíme na to, co je pro Pumu typické. Pokud chcete srovnat značky, otevřete si <a href="/nike-ponozky/">ponožky Nike</a> a <a href="/adidas-ponozky/">ponožky Adidas</a>, případně přehled ponožek značky <a href="/znacka/puma/">Puma</a>.</p>',
    guide='<h2>Jak číst názvy Puma ponožek</h2>'
          '<p>Většina názvů obsahuje tři informace: typ střihu, počet kusů v balení a barvu. Označení 3P nebo 3PACK znamená tři páry, 2P dva, 5 párů pět. Slovo unisex říká, že balení není určené jen pro muže nebo ženy a velikosti jsou společné. Slovo Elements označuje základní řadu, Cushioned polstrované chodidlo a Mesh prodyšný vzor na nártu. Kódy typu 701231277 jsou katalogová čísla, podle kterých poznáte shodný model u jiného prodejce.</p>'
          + T(['Délka', 'Jak vysoko sahá', 'Nejlepší použití'], [
              ['Invisible, nízká', 'pod kotník, nevidíte ji v botě', 'nízké tenisky, plátěnky, léto'],
              ['Sneaker', 'těsně nad okrajem boty', 'každodenní tenisky, lehký trénink'],
              ['Quarter', 'nad kotník', 'běžecké boty, ochrana kotníku proti otěru'],
              ['Crew', 'do půlky lýtka', 'volný čas, tenis, posilovna, školní tělocvik'],
              ['Fotbalové štulpny', 'pod kolena, s přidržením lýtkového chrániče', 'fotbal a trénink s chrániči']]) +
          '<p>Při srovnání obchodů ověřte, zda srovnáváte stejný počet párů. Balení po dvou a po třech může mít podobnou fotografii, ale zcela jinou cenu za pár. Spočítejte si proto cenu za pár, ne za balení.</p>'
          '<h2>Nízké a neviditelné ponožky</h2>'
          '<p>Nejčastější typ v nabídce jsou nízké ponožky v bílé, černé a šedé v balení po třech. Hodí se do nízkých tenisek, a když se nosí s plátěnými botami, nesmí z boty vykukovat. Nízká ponožka s protiskluzovým pásem nad patou se nezačne sunout dolů, bez něj se po chvíli chůze často sveze pod patu. Pokud máte při chůzi problém s odíráním paty, zkuste raději délku sneaker. V letním horku pomůže vzdušné pletení na nártu, v zimě naopak nízká ponožka nehřeje.</p>'
          '<h2>Crew a quarter: každodenní komfort</h2>'
          '<p>Crew ponožky chrání lýtko před třením a v tenisu, posilovně nebo v hale se osvědčují. Silnější chodidlo u modelů s polstrováním tlumí nárazy a zlepšuje pohodlí při delší chůzi. Quarter drží kotník, ale neobtěžuje. Použijete je v běžeckých botách: ochrání kůži před otěrem o okraj boty. Pokud chodíte po městě celý den, vyberte měkčí bavlněné směsi, při sportu raději směs s polyesterem, který odvádí vlhkost.</p>'
          '<ul><li><strong>Bavlna:</strong> příjemná, ale nasákne potem a pomalu schne.</li>'
          '<li><strong>Polyester a polyamid:</strong> rychle schnou a drží tvar.</li>'
          '<li><strong>Elastan:</strong> dodává pružnost a zabraňuje sbalování v botě.</li>'
          '<li><strong>Frotté chodidlo:</strong> tlumí nárazy, ale hřeje.</li>'
          '<li><strong>Bezešvá špička:</strong> omezuje tlak a možnost puchýře.</li></ul>'
          '<p>Většina ponožek je směs. Poměr najdete na štítku a ten rozhoduje víc než slogan. Pokud je podíl bavlny vysoký, počítejte s pomalejším schnutím.</p>'
          '<h2>Fotbalové ponožky a štulpny</h2>'
          '<p>Fotbalové ponožky Puma, například z řad Teamliga a Teamfinal, jsou dlouhé, přetahují se přes chrániče a drží je na místě. Obvykle mají zesílené chodidlo a pružnou manžetu pod kolenem. Pro týmové dresy se kupují v barvách týmu a stejná barva může být v ligových kolekcích dostupná v celé řadě velikostí. Pokud hrajete v kopačkách, vybírejte ponožku, která není příliš silná, protože tlustá vrstva zmenšuje prostor v obuvi. Související výběr naleznete v kategorii <a href="/kopacky/">kopačky</a>.</p>'
          '<h2>Velikost: jak nesáhnout vedle</h2>'
          '<p>Velikosti se uvádějí v rozsazích, například 39–42 nebo 43–46. Pokud jste na hraně, zvolte větší rozsah u měkkých ponožek a menší u silně elastických. Příliš malá ponožka se napíná, tlačí a rychleji se protře na patě, příliš velká tvoří v botě záhyby a způsobuje puchýře. Dětské ponožky se kupují o něco větší, protože noha roste, ale ne o celé číslo, jinak se v botě přeskupují.</p>'
          + T(['Situace', 'Doporučená volba'], [
              ['Nové nízké tenisky na každý den', 'sneaker nebo invisible s protiskluzovým pásem'],
              ['Běh po silnici', 'quarter, tenká až střední, bez tlustých švů'],
              ['Tenis, squash, hala', 'crew s polstrovaným chodidlem'],
              ['Fotbal s chrániči', 'fotbalové štulpny v barvě týmu'],
              ['Škola a tělocvik', 'bílé nebo šedé crew v balení po pěti párech'],
              ['Pro ženy', 'užší střih, často s žebrováním nebo jemným vzorem']]) +
          '<h2>Pro koho jsou ponožky Puma</h2>'
          '<p>Značka je silná v kategorii základních, lehce sportovních ponožek pro denní nošení a pro mladší nositele. Pokud hledáte vysoce technickou ponožku na delší trail, horskou túru nebo mráz, vybírejte u specialistů jako <a href="/merino-ponozky/">merino ponožky</a> nebo <a href="/lyzarske-ponozky/">lyžařské ponožky</a>. Pro cyklistiku jsou k dispozici <a href="/cyklisticke-ponozky/">cyklistické ponožky</a> s vyšším lemem a lepším přidržením. Puma je tu dobrou volbou na trénink, školní sport a každodenní tenisky.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Ponožky perte na rubu při doporučené teplotě a nepoužívejte aviváž, která zpomaluje odvod vlhkosti. Při párování používejte pytlík na prádlo, aby se kusy neztrácely. Nejrychleji se obvykle opotřebí pata a špička, kde vzniká otěr. Protřená vlákna jsou i signálem, že je čas na novou sadu. Balení po třech párech se proto vyplatí střídat, aby se opotřebení rozložilo rovnoměrně. Výběr pro starší stránky najdete také v nabídkách značek <a href="/ponozky-fila/">Fila</a> a <a href="/under-armour-ponozky/">Under Armour</a>.</p>',
    faq=[
        ('Co znamená 3P nebo 3PACK v názvu ponožek?', 'Označuje balení se třemi páry stejného střihu. Podobně 2P je balení po dvou párech. Při srovnání cen sledujte cenu za pár, protože balení po třech a po dvou se na obrázku často neliší.'),
        ('Jak poznám správnou délku ponožky?', 'Do nízkých tenisek zvolte sneaker nebo invisible, do běžeckých bot quarter a do vysokých bot nebo na tenis crew. Pro fotbal s chrániči slouží dlouhé štulpny. Délka rozhoduje o tom, zda ponožku v botě vidíte a zda chrání kotník.'),
        ('Z jakého materiálu jsou ponožky Puma?', 'Většinou jde o směs bavlny, polyesteru nebo polyamidu a elastanu. Poměr uvádí štítek. Čím víc bavlny, tím je ponožka měkčí, ale pomaleji schne, čím víc syntetiky, tím lépe odvádí vlhkost.'),
        ('Jsou ponožky unisex pro muže i ženy?', 'Ano, většina balení je unisex a řídí se velikostními rozsahy, například 35–38 nebo 39–42. Pro ženy existují i užší modely se žebrováním. Při výběru se řiďte rozsahem velikosti, ne označením pohlaví.'),
        ('Hodí se ponožky Puma na běh?', 'Na kratší běhy a rekreační použití ano, nejlépe ve střihu quarter z tenčího materiálu. Pro dlouhé vzdálenosti nebo trail zvažte specializované běžecké ponožky s plochými švy a zónami pro odvod potu. Bavlněné směsi se při potu rychle promáčejí.'),
        ('Proč se mi ponožka sune dolů pod patu?', 'Nízké ponožky bez protiskluzového pásu nad patou mají tendenci se svézt. Zkuste střih sneaker nebo model s pružnou lemovkou. Pokud je ponožka příliš velká, při chůzi se také hromadí, proto zvolte správný rozsah velikosti.'),
        ('Jak vybrat dětské ponožky?', 'Zvolte rozsah velikosti, který odpovídá noze, ne o celé číslo větší. Dětské ponožky bývají v balení po třech až pěti párech. Zkontrolujte, zda nemají tlačící švy na špičce a že pružný lem neškrtí lýtko.'),
        ('Jak dlouho ponožky vydrží?', 'Záleží na četnosti nošení a pracovním zatížení. Nejdřív se obvykle protře pata nebo špička. Střídání více párů a praní na rubu životnost prodlouží. Jakmile je látka průsvitná, ponožka přestává chránit.'),
        ('Mohu ponožky kombinovat s ponožkami jiné značky?', 'Samozřejmě, ponožky nejsou vázané na boty ani na značku. Důležité je, aby střih odpovídal délce boty a aby materiál odpovídal sportu. Pokud sbíráte sady do práce, vyplatí se koupit jedno balení stejného střihu, aby se páry snadno párovaly.'),
    ])

NEW['batoh-tommy-hilfiger']['guide'] += (
    '<h2>Detaily, které rozhodují při výběru</h2>'
    '<p>Dva batohy podobné na fotografii se v praxi liší hlavně vnitřkem a zády. Podívejte se, zda je hlavní komora otevíratelná dostatečně dokořán, abyste se dostali ke dnu bez vyndavání půlky věcí. Přední kapsa na zip se hodí na klíče a doklady, boční síťovaná kapsa na láhev ušetří místo uvnitř, ale u úzkých modelů chybí. Madlo nahoře uvítáte v šatně a v autobuse, kde batoh zavěšujete. Polstrování zad rozhoduje o komfortu v létě: pěnová záda s dírkami lépe větrají než hladký plochý panel.</p>'
    '<ul><li><strong>Popruhy:</strong> šířka kolem čtyř centimetrů už netlačí na rameno ani při plném batohu.</li>'
    '<li><strong>Dno:</strong> zpevněné nebo pogumované dno nenasákne vodu z mokrého chodníku.</li>'
    '<li><strong>Kapsa na doklady:</strong> skrytá uvnitř je bezpečnější v davu než vnější.</li>'
    '<li><strong>Odnímatelné prvky:</strong> poutko pro klíče nebo kapsa na kartu se hodí při dojíždění.</li></ul>'
    '<h2>Kdy se nákup vyplatí</h2>'
    '<p>Módní batohy se obměňují po sezónách a starší barvy se rozprodávají s rozdílnou nabídkou mezi obchody. Je proto užitečné srovnat tentýž kód modelu u více prodejců a všímat si, zda se nabídka mění v čase. Pokud potřebujete batoh na začátek školního roku, rozhodněte se dříve, protože oblíbené barvy a velikosti mizí jako první. Při koupi nezapomeňte na možnost vrácení, protože batoh je nejlepší zkusit naložený doma.</p>')

NEW['adidas-kalhoty']['guide'] += (
    '<h2>Kalhoty na různé sporty</h2>'
    '<p>Značka pokrývá víc než fotbal. Pro posilovnu se hodí pružné tkané kalhoty nebo lehké tepláky, které nepřekážejí v dřepu. Při běhu pomáhá užší nohavice s lehkým materiálem a kapsou na klíč, protože klíče v klasické kapse poskakují. Na tenis nebo badminton se používají volnější střihy, které nesvazují při výpadech. Při jízdě na kole se nohavice zúžené u kotníku nezachytí do řetězu, ale pro delší jízdu je vhodnější specializované oblečení z kategorie <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a>.</p>'
    '<h2>Častá nedorozumění při nákupu</h2>'
    '<ul><li><strong>Souprava není jen kalhoty:</strong> v názvu se objevuje Tracksuit nebo Souprava a nabídka může zahrnovat i mikinu.</li>'
    '<li><strong>Dětské a dospělé velikosti:</strong> mladiství často přecházejí na dámské XS nebo pánské XS, tabulku porovnejte předem.</li>'
    '<li><strong>Zimní kalhoty:</strong> tréninkové kalhoty nejsou zateplené, v mrazu je kombinujte s vrstvou pod nimi.</li>'
    '<li><strong>Imitace:</strong> nezvykle levná nabídka u novinky může být padělek, ověřte prodejce.</li></ul>'
    '<p>Při srovnání nabídek porovnávejte celý název včetně barvy a velikosti, protože tentýž model se prodává v několika barevných variantách a ne všechny jsou ve všech velikostech skladem.</p>')

NEW['puma-ponozky']['guide'] += (
    '<h2>Kolik párů potřebuji</h2>'
    '<p>Ponožky se opotřebovávají nerovnoměrně a jedna ztracená z páru pokazí celé balení. Pro každodenní nošení se vyplatí mít aspoň sedm párů, aby se dalo prát jednou týdně bez nouze. Sportovec, který trénuje třikrát týdně, si vystačí s menší zásobou, ale měl by mít po ruce dva až tři páry určené pouze na trénink, protože pot a opakované praní urychlují opotřebení. Pokud ponožky kupujete celé balení najednou, vyberte stejnou barvu a střih, aby se páry nemusely hledat.</p>'
    '<h2>Barvy a praktika</h2>'
    '<p>Bílé ponožky vypadají sportovně a hodí se k bílým teniskám, ale rychle ukážou zašpinění chodidla. Černé a tmavé skryjí špínu, ale u světlých bot vypadají kontrastně. Šedé jsou kompromisem. Barevné nebo s logem se nosí hlavně ve volném čase. Pro hodiny tělocviku a týmové sporty bývá důležitější sjednocení: zvolte stejné ponožky pro všechny páry, aby se kusy daly volně zaměňovat.</p>'
    '<h2>Tipy, jak snížit riziko puchýřů</h2>'
    '<ul><li>Nové boty zkoušejte vždy v ponožkách, které k nim budete nosit.</li>'
    '<li>Při delší aktivitě vyměňte promočenou ponožku za suchou.</li>'
    '<li>Zkontrolujte, zda ponožka nemá tlustý šev v oblasti prstů.</li>'
    '<li>Volte ponožku odpovídající tvaru nohy: tvarovaná na levou a pravou nohu sedí přesněji.</li>'
    '<li>Při potížích s otlaky zkuste vrstvení s tenkou vnitřní ponožkou.</li></ul>'
    '<p>Pokud problémy přetrvávají i při správné velikosti ponožky, zkontrolujte především obuv. Špatně padnoucí bota nespraví žádná ponožka, ale dobrá ponožka často odstraní poslední nepohodlí.</p>')

NEW['batoh-tommy-hilfiger']['guide'] += (
    '<h2>Dárek nebo vlastní nákup</h2>'
    '<p>Značkový batoh je častý dárek k začátku školy, maturitě nebo prvnímu zaměstnání. Při výběru pro někoho jiného sázejte na tmavou jednobarevnou variantu s nenápadným logem, která se nezkazí vkusem. Dejte pozor na velikost: příliš malý batoh vadí víc než příliš velký. Pokud si nejste jistí, vyberte obchod s možností výměny a přiložte doklad, aby případná výměna proběhla bez komplikací.</p>')

NEW['adidas-kalhoty']['guide'] += (
    '<h2>Co dělat, když kalhoty nesedí</h2>'
    '<p>Po koupi kalhoty vyzkoušejte doma v pohybu: dřep, předklon a zvednutí kolene ukážou, zda pas nesjíždí a zda nohavice netlačí. Tepláky s pružným pasem bez šňůrky se často sunou dolů, proto hledejte provlečenou šňůrku nebo gumu širší. Pokud jsou kalhoty dlouhé, využijte náplet na kotníku: jde přehrnout a dětem pomůže, že se nohavice nenavlékají pod botu. Při výměně sledujte podmínky vrácení u konkrétního obchodu, někde se kalhoty bez štítku nevracejí.</p>')

NEW['puma-ponozky']['guide'] += (
    '<h2>Ponožky do různých bot</h2>'
    '<p>Do kožených a plátěných tenisek se hodí nízké ponožky, které se při chůzi nepohybují. Do vysokých bot a zimních kousků vezměte crew, aby okraj boty netřel lýtko. Do halové obuvi s měkkým jazykem mnozí upřednostňují lehce polstrované chodidlo, které tlumí nárazy při doskocích. V letním horku zvolte tenčí pletení s větrací strukturou na nártu, v chladném počasí silnější bavlněnou směs. Pokud střídáte boty, mějte několik střihů a nepoužívejte jednu délku do všeho.</p>')
