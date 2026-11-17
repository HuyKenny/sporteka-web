"""sporteka.cz — wave 29c (16. 11. 2026): long texts for ortezy-na-koleno, ortezy-na-kotnik, fotbalove-dresy.
General true facts only, no prices, no product counts. Orthoses: no medical promises — a sport brace is support,
not treatment; after an injury or with pain see a doctor or physiotherapist; sizing by the manufacturer's chart.
Brands with an indexed page (znacky.json): merco, asics, adidas, nike, puma, joma, lotto; other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ ortezy-na-koleno
NEW['ortezy-na-koleno'] = dict(long=True,
    title='Ortéza na koleno a chrániče na kolena pro sport',
    desc='Ortézy na koleno od elastických návleků po kloubové a chrániče kolen na volejbal, florbal, skate i kolo. Jak změřit obvod a co od ortézy čekat.',
    intro='<p>Ortéza na koleno je pomůcka, která koleno při sportu obepne, zahřeje a podle typu i zpevní ze stran. Nejjednodušší je elastický návlek, o stupeň dál je bandáž s otvorem pro čéšku a nejvíc opory dávají ortézy s bočními klouby. Vedle nich v kategorii najdete chrániče na kolena, které neslouží k opoře, ale k ochraně před nárazem: pěnové pro volejbal a florbal, tvrdé pro skateboard, kolečkové brusle a sjezd na kole. Sportovní ortéza je opora, ne léčba. Když koleno bolí, otéká nebo jste si ho zranili, nejdřív ho ukažte lékaři nebo fyzioterapeutovi.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých obchodů a nákup dokončíte na webu prodejce. Porovnáte tu ortézy a chrániče značek McDavid, Mueller, Thuasne, ' + B(('merco', 'Merco'), ('asics', 'Asics')) + ', Leatt, Fox nebo Tempish. Další pomůcky na klouby jsou v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>',
    guide='<h2>Ortéza, bandáž a chránič nejsou totéž</h2>'
          '<p>V obchodech i v hovoru se tyto názvy často míchají, každá z těch věcí ale dělá něco jiného. Bandáž nebo návlek je pružná trubice z pleteniny či neoprenu, která koleno stlačí a udrží v teple. Ortéza má navíc pevné prvky, tedy boční výztuhy, pásky nebo kovové klouby, a omezuje pohyb do stran. Chránič na koleno pohyb téměř neovlivňuje, jen tlumí náraz při pádu nebo kleku. Než začnete vybírat, ujasněte si, jestli potřebujete pocit opory, zpevnění, nebo ochranu kůže a čéšky.</p>'
          '<h2>Typy ortéz a chráničů na koleno</h2>'
          + T(['Typ', 'Jak je postavený', 'Kdy se nosí'], [
              ['elastický návlek', 'pružná pletenina nebo neopren bez výztuh', 'pocit opory a tepla při běhu, v posilovně, na túře'],
              ['bandáž s otvorem pro čéšku', 'návlek s otvorem a často silikonovým prstencem kolem čéšky', 'sporty s doskoky a rychlými změnami směru'],
              ['bandáž s bočními výztuhami', 'spirálové nebo plastové pruty po stranách kolena', 'když chcete víc stability do stran'],
              ['kloubová ortéza', 'boční klouby z kovu nebo plastu, pásky přes stehno a lýtko', 'nejvyšší opora, často na doporučení odborníka'],
              ['pásek pod čéšku', 'úzký pásek obepínající nohu pod kolenem', 'běh a skoky, kde chcete jen lehký tlak pod čéškou'],
              ['měkký chránič', 'pěnový polštář přes čéšku v pružném návleku', 'volejbal, florbal, házená, tanec, práce na zemi'],
              ['tvrdý chránič', 'plastová skořepina s polstrováním a pásky', 'skateboard, brusle, koloběžka, MTB a sjezd']]) +
          '<p>Kloubové ortézy na trhu najdete také, ale u nich platí zvlášť, že by měl výběr probrat odborník. Zdravotnické ortézy po operaci nebo úrazu může předepsat lékař a nastavení kloubu pak řeší specialista. Sportovní ortéza z obchodu takovou pomůcku nenahradí.</p>'
          '<h2>Materiály: neopren, nebo pletenina</h2>'
          '<p>Neopren dobře hřeje a pevně drží, pod ním se ale noha víc potí a v létě může být nepříjemný. Hodí se na chladné tréninky, na vodu a pro ty, kdo mají rádi pocit pevného sevření. Pletené návleky z nylonu, polyesteru a elastanu jsou tenčí a prodyšnější, lépe se schovají pod legíny a dají se nosit déle. Pro citlivou kůži se vyplatí hledat model s plochými švy a bez latexu, pokud na něj máte alergii. U chráničů rozhoduje pěna: měkká je pohodlná na volejbal, tužší a silnější lépe snese tvrdý pád na beton.</p>'
          '<h2>Jak vybrat správnou velikost</h2>'
          '<p>Ortéza, která je příliš volná, sjíždí ke kotníku a nedrží. Příliš těsná zase škrtí a omezuje krevní oběh. Velikost se proto neodhaduje podle oblečení, ale měří krejčovským metrem. Výrobci obvykle chtějí obvod stehna několik centimetrů nad čéškou, obvod přes střed kolena nebo obvod lýtka pod kolenem. Kde přesně měřit a jestli má být noha natažená, nebo mírně pokrčená, je vždy napsané v tabulce konkrétního výrobce. Tabulky se mezi značkami liší, takže velikost M jedné firmy nemusí sedět jako M u druhé.</p>'
          '<p>Pokud vám vychází hodnota na hranici dvou velikostí, podívejte se, co doporučuje výrobce. Obecně platí, že návlek se má dát natáhnout bez velkého přemáhání a po nasazení nesmí tlačit v podkolenní jamce. U chráničů zkontrolujte, že polštář kryje celou čéšku i při pokrčení, kdy se koleno posune dopředu.</p>'
          '<h2>Chrániče na kolena podle sportu</h2>'
          '<h3>Volejbal, florbal a házená</h3>'
          '<p>Ve <a href="/volejbal/">volejbale</a> hráči padají a kloužou po palubovce, a proto mají chrániče s pěnovým polštářem přes čéšku a pružný návlek, který neomezuje dřep. Florbaloví brankáři klečí většinu zápasu a potřebují chrániče s větší a tužší výplní. Pro hráče v poli se hodí tenčí modely, které nebrání v běhu. Vybavení pro tento sport je v kategorii <a href="/florbal/">florbal</a>.</p>'
          '<h3>Skateboard, brusle a koloběžka</h3>'
          '<p>Na asfaltu a betonu chrání koleno tvrdá plastová skořepina. Ta při pádu sklouzne po povrchu místo toho, aby se o něj zasekla, a rozloží náraz. Dětské sady obsahují chrániče kolen, loktů a zápěstí; přilbu k nim najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h3>Horské kolo</h3>'
          '<p>Chrániče na MTB se dělí na lehké, ve kterých se dá šlapat celý den, a robustní pro sjezd a bikepark. Lehké mívají návlek z prodyšného úpletu a vložku z materiálu, který je při pohybu měkký a při nárazu ztuhne. Sjezdové modely mají tvrdou skořepinu a často kryjí i holeň. Značky Leatt a Fox se na cyklistické chrániče specializují, další modely jsou v kategorii <a href="/cyklo-chranice/">cyklo chrániče</a>.</p>'
          '<h2>Ortéza na běh, lyže a do posilovny</h2>'
          '<p>Běžci obvykle sahají po tenkých pletených návlecích nebo po pásku pod čéšku, protože nesmí dřít v podkolení a musí vydržet hodiny pocení. Na lyžích a na skialpech se nosí bandáže s bočními výztuhami pod lyžařské kalhoty; tady se hodí spíš tenčí materiál, který nezvětší objem v botě ani pod kalhotami. Ve vzpírání a při dřepech s velkou vahou se používají silné neoprenové návleky, které koleno drží v teple a dodají pocit pevnosti v dolní poloze dřepu. Pro turistiku a dlouhé sestupy stačí lehký návlek, k němuž si mnoho lidí přibírá <a href="/trekove-hole/">trekové hole</a>, které kolena při klesání odlehčí.</p>'
          '<h2>Chrániče kolen pro děti</h2>'
          '<p>Děti padají na kolena častěji než dospělí, ať se učí jezdit na bruslích, na skateboardu, nebo hrají míčové hry v tělocvičně. Dětské chrániče se prodávají v sadách a měly by mít pružné pásky, které si dítě zapne samo, a skořepinu, která kryje celou čéšku. Velikost se určuje podle obvodu nohy nebo podle věku a výšky, opět podle tabulky výrobce. Chránič, který po pár minutách sjede na holeň, nechrání, a proto se vyplatí nechat dítě v chráničích chvíli běhat a klekat si ještě doma.</p>'
          '<h2>Co od ortézy čekat a co ne</h2>'
          '<p>Sportovní ortéza zvenku přidá pocit stability, koleno zahřeje a připomene vám, abyste ho nepřetěžovali. Svaly ale nahradit neumí a sama o sobě koleno nespraví. Když se bolest vrací, koleno praská a otéká nebo pod vámi uhýbá, je to důvod k návštěvě lékaře, ne k nákupu pevnější ortézy. Fyzioterapeut také poradí, jaký typ ortézy a na jak dlouho má smysl nosit, a ukáže cviky, které koleno posílí. U dětí a dospívajících platí totéž ještě důrazněji.</p>'
          '<h2>Ortéza, nebo kineziologický tejp</h2>'
          '<p>Na koleno se kromě ortéz lepí i pružné tejpy, které pohyb neomezují a vydrží na kůži několik dní. Ortéza je pohodlnější v tom, že ji ráno nasadíte a po tréninku sundáte, a dá se používat opakovaně. Tejp zase nezabere žádné místo pod oblečením a nehřeje. Oboje je doplněk, ne náhrada cvičení, a o vhodnější variantě pro vaši situaci se poraďte s fyzioterapeutem, který vám tejp případně i ukáže nalepit.</p>'
          '<h2>Nošení a péče</h2>'
          '<ul><li>Ortézu nasazujte na suchou kůži a srovnejte ji tak, aby otvor ležel přesně nad čéškou.</li>'
          '<li>Když prsty brní, noha mění barvu nebo chladne, ortézu povolte nebo sundejte.</li>'
          '<li>Pásky na suchý zip utahujte postupně, nejdřív spodní, potom horní.</li>'
          '<li>Perte podle štítku, většinou ručně ve vlažné vodě, a sušte na vzduchu mimo topení.</li>'
          '<li>Opotřebovaný návlek, který už nedrží tvar, vyměňte za nový.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Velikost odhadnutá podle velikosti kalhot místo změřeného obvodu.</li>'
          '<li>Neoprenová ortéza na celý letní den, pod kterou se kůže zapaří.</li>'
          '<li>Chránič na skate bez tvrdé skořepiny, který se při pádu na beton zasekne.</li>'
          '<li>Nošení ortézy místo vyšetření dlouhodobé bolesti.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>U každého modelu uvidíte nabídky více obchodů a velikosti, které mají skladem; objednávka pak proběhne u prodejce. Nejdřív zvolte typ podle toho, jestli chcete oporu, nebo ochranu před nárazem, potom si změřte obvod a vyberte velikost podle tabulky výrobce. Na kotník se podívejte do kategorie <a href="/ortezy-na-kotnik/">ortézy na kotník</a>, na lepení kloubů na <a href="/tejpy/">tejpy</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi ortézou a bandáží na koleno?', 'Bandáž je pružný návlek, který koleno stlačí a zahřeje. Ortéza má navíc pevné prvky, třeba boční výztuhy nebo klouby, a omezuje pohyb do stran.'),
        ('Pomůže ortéza na bolavé koleno?', 'Sportovní ortéza je opora, ne léčba. Bolest kolena může mít mnoho příčin, od přetížení po poranění vazů nebo menisku, proto ji nejdřív ukažte lékaři nebo fyzioterapeutovi. Ten poradí, jestli ortézu nosit, jaký typ a při jakých činnostech.'),
        ('Jak změřit velikost ortézy na koleno?', 'Krejčovským metrem změřte obvod na místě, které uvádí výrobce, obvykle nad čéškou, přes střed kolena nebo pod kolenem. Hodnotu porovnejte s tabulkou konkrétní značky.'),
        ('Proč má bandáž otvor pro čéšku?', 'Otvor a často i silikonový prstenec kolem něj drží čéšku v místě a nevytváří na ni tlak. Bandáž tak lépe sedí při dřepu a doskoku.'),
        ('Jaké chrániče na kolena na volejbal?', 'Měkké chrániče s pěnovým polštářem přes čéšku a pružným návlekem. Chrání při pádech a skluzech po palubovce a nebrání v hlubokém postoji. Vyzkoušejte, že polštář zůstane na čéšce i v dřepu.'),
        ('Jaké chrániče na kolena na skateboard?', 'Tvrdé chrániče s plastovou skořepinou, která při pádu po betonu sklouzne. K nim patří chrániče loktů, zápěstí a přilba.'),
        ('Můžu ortézu nosit celý den?', 'Sportovní ortézy jsou určené hlavně na dobu tréninku a zápasu. Dlouhodobé nošení proberte s lékařem nebo fyzioterapeutem, protože bez zátěže svaly kolem kolena ochabují. Když noha brní, chladne nebo otéká, ortézu hned povolte.'),
    ])

# ------------------------------------------------------------------ ortezy-na-kotnik
NEW['ortezy-na-kotnik'] = dict(long=True,
    title='Ortéza na kotník: elastické, šněrovací i s výztuhami',
    desc='Ortézy a bandáže na kotník pro volejbal, basketbal, florbal i běh: elastické, šněrovací, s pásky do osmičky a výztuhami. Velikost a nošení v botě.',
    intro='<p>Ortéza na kotník obepíná hlezno a zčásti i chodidlo a při sportu přidává kloubu oporu. Nejjednodušší jsou elastické bandáže, které kotník jen stlačí a zahřejí. Šněrovací ortézy připomínají nízkou botu bez podrážky a dají se utáhnout přesně podle nohy. Modely s pásky vedenými do osmičky nebo s bočními výztuhami omezují vytočení chodidla do strany, při kterém dochází k typickému podvrtnutí. Sahají po nich hlavně volejbalisté, basketbalisté, florbalisté a tenisté, tedy všichni, kdo často doskakují a mění směr. Sportovní ortéza ale není léčba: po podvrtnutí, při otoku nebo bolesti nejdřív navštivte lékaře nebo fyzioterapeuta.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů, a to včetně dostupných velikostí, a objednávku dokončíte v e-shopu, který si vyberete. Najdete tu ortézy McDavid, Mueller, Select, Spokey, LiveUp a dalších výrobců. Patří do kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>',
    guide='<h2>Proč sportovci kotník zpevňují</h2>'
          '<p>Kotník je při sportu namáhaný hlavně při doskoku a prudké změně směru. Stačí dopadnout na nohu spoluhráče nebo zavadit o nerovnost a chodidlo se vytočí dovnitř. Někteří hráči proto nosí ortézu preventivně na každý trénink, jiní se k ní vracejí po dřívějším zranění, když už mají kotník ošetřený a rehabilitovaný. Ortéza zvenku omezí krajní pohyb a dodá pocit jistoty. Posílení svalů a nácvik rovnováhy ale nenahradí, a právě o ty se fyzioterapeuti při návratu ke sportu opírají nejvíc.</p>'
          '<h2>Typy ortéz na kotník</h2>'
          + T(['Typ', 'Konstrukce', 'Míra opory'], [
              ['elastická bandáž', 'pružný návlek z pleteniny nebo neoprenu', 'nízká, hlavně teplo a mírný tlak'],
              ['bandáž s páskem', 'návlek a pásek na suchý zip vedený kolem kotníku', 'nízká až střední'],
              ['šněrovací ortéza', 'tuhá textilie se šněrováním přes nárt, často s jazykem', 'střední, dá se přesně dotáhnout'],
              ['ortéza s pásky do osmičky', 'šněrování a pásky překřížené přes nárt a kolem paty', 'střední až vyšší, podobně jako tejp'],
              ['ortéza s bočními výztuhami', 'plastové nebo kovové pruty po stranách kotníku', 'vyšší, omezí vytočení chodidla'],
              ['pevná ortéza se skořepinou', 'dvě boční dlahy spojené pod patou', 'nejvyšší, obvykle po úrazu na doporučení lékaře']]) +
          '<p>Pevné ortézy se skořepinou patří spíš do zdravotnictví a lékař je může předepsat po úrazu. Pro běžný sport se nejčastěji používají šněrovací modely a modely s pásky, protože se vejdou do sportovní obuvi a nebrání v běhu.</p>'
          '<h2>Elastická bandáž, nebo šněrovací ortéza</h2>'
          '<p>Elastickou bandáž natáhnete jako ponožku a skoro ji necítíte. Hodí se na běh, túry a posilovnu, kde chcete kotník spíš zahřát a mít ho pod lehkým tlakem. Proti vytočení chodidla toho ale udělá málo. Šněrovací ortéza drží pevněji a dá se utáhnout podle toho, jak se kotník během zápasu zahřeje. Nasazení trvá déle a v botě zabere víc místa. Ortézy s pásky do osmičky napodobují způsob, jakým fyzioterapeuti lepí <a href="/tejpy/">tejpy</a>, a mají výhodu, že je nemusíte pokaždé znovu lepit.</p>'
          '<h2>Ortéza podle sportu</h2>'
          '<ul><li><strong>Volejbal a basketbal:</strong> mnoho doskoků, často u sítě nebo pod košem na nohu soupeře. Hráči volí šněrovací ortézy s pásky nebo výztuhami a k nim pevnou halovou obuv, třeba <a href="/basketbalova-obuv/">basketbalovou obuv</a>.</li>'
          '<li><strong>Florbal, házená a fotbal:</strong> rychlé změny směru. Hodí se nízké a tenké ortézy, které se vejdou do sálovky nebo kopačky.</li>'
          '<li><strong>Tenis a squash:</strong> boční pohyby po kurtu; ortéza by neměla omezovat došlap na špičku.</li>'
          '<li><strong>Běh v terénu a turistika:</strong> spíš elastická bandáž, pevnější oporu dá vyšší treková bota.</li>'
          '<li><strong>Lyže a snowboard:</strong> kotník drží skelet lyžařské nebo snowboardové boty, a tak se ortéza do ní obvykle nedává; o výjimce po zranění rozhodne odborník.</li></ul>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Výrobci určují velikost dvojím způsobem. Někteří podle velikosti bot, jiní podle obvodu kotníku nebo obvodu kolem paty a nártu. Vždy se řiďte tabulkou konkrétní značky a měřte krejčovským metrem na místě, které výrobce uvádí. Některé ortézy jsou levé a pravé, jiné univerzální. Pokud máte nohu na pomezí dvou velikostí, přečtěte si, kterou výrobce doporučuje, protože u šněrovacích modelů bývá rozumnější menší a u elastických naopak záleží na tom, aby návlek neškrtil.</p>'
          '<h2>Ortéza a bota</h2>'
          '<p>I tenká ortéza zabere v botě místo, a tak ji vyzkoušejte se sportovní obuví, ve které hrajete. Někomu stačí povolit tkaničky, jiný potřebuje botu o půl čísla větší. Pod ortézu se nosí tenká <a href="/sportovni-ponozky/">sportovní ponožka</a> bez silných švů, které by se pod pevnou látkou otlačovaly. Ortézu nasazujte vsedě, s chodidlem v pravém úhlu k bérci, a pásky dotahujte postupně. Po nazutí se projděte a udělejte pár výponů; když ortéza tlačí na kotníkovou kost nebo na nárt, upravte šněrování. Pokud otlak nezmizí ani po úpravě, zkuste jinou velikost nebo jiný model, protože tvar kotníku má každý trochu jiný.</p>'
          '<h2>Jak ortézu nasadit</h2>'
          '<ol><li>Posaďte se a nohu opřete tak, aby chodidlo svíralo s bércem pravý úhel.</li>'
          '<li>Natáhněte ortézu přes ponožku a zkontrolujte, že pata sedí v připraveném otvoru nebo kapse.</li>'
          '<li>Šněrování dotahujte odspodu nahoru, rovnoměrně a ne nadoraz.</li>'
          '<li>Pásky veďte podle návodu, obvykle přes nárt, kolem paty a zpět na vnější stranu kotníku.</li>'
          '<li>Nazujte botu, projděte se a podle pocitu šněrování nebo pásky ještě upravte.</li></ol>'
          '<p>Postup se u různých modelů liší, a tak si před prvním použitím přečtěte návod. Při hře ortézu po rozehřátí zkontrolujte, protože materiál se zahřeje a pásky mohou povolit.</p>'
          '<h2>Materiály a pohodlí</h2>'
          '<p>Šněrovací ortézy se šijí z pevného nylonu nebo polyesteru, který se netahá, a často mají vnitřní stranu z měkčí síťoviny, aby se pod nimi noha tolik nepotila. Elastické bandáže bývají pletené, případně z neoprenu, který víc hřeje. Na halové sporty, kde se hraje dlouho a v teple, se vyplatí prodyšnější model s tenkým jazykem. Pokud máte citlivou kůži, hledejte ortézu s měkkým lemováním okrajů a bez hrubých švů na vnitřní straně kotníku, kde se pásky nejvíc dotýkají kůže.</p>'
          '<h2>Ortéza pro děti a juniory</h2>'
          '<p>Dětské a juniorské velikosti mají šněrovací i elastické ortézy většiny výrobců. U dětí, které hrají volejbal, basketbal nebo florbal v klubu, by měl o ortéze rozhodnout trenér spolu s lékařem nebo fyzioterapeutem, hlavně po zranění. Dítě roste a kotník mu během sezony zesílí, takže velikost kontrolujte častěji než u dospělých. Ortéza, ze které noha vyrostla, tlačí a místo opory způsobuje otlaky.</p>'
          '<h2>Kdy k lékaři</h2>'
          '<p>Podvrtnutý kotník lidé často podceňují a vracejí se na hřiště dřív, než je kloub připravený. Pokud po zranění kotník výrazně otekl, objevila se modřina, nemůžete na nohu došlápnout nebo bolest neustupuje, nechte ho vyšetřit. Lékař nebo fyzioterapeut rozhodne, jestli a jakou ortézu nosit a jak dlouho. Sportovní ortéza z obchodu je pomůcka pro trénink, ne náhrada péče po úrazu. Návrat ke sportu po zranění je dobré naplánovat s odborníkem postupně, od chůze přes běh po skoky a změny směru.</p>'
          '<h2>Co dělat kromě ortézy</h2>'
          '<p>Ortéza je jen jeden díl skládačky. Stejně důležitá je rozcvička před tréninkem, obuv určená pro daný povrch a sport a pravidelné posilování lýtek a chodidel. Fyzioterapeuti po zranění kotníku často zařazují cviky na rovnováhu, třeba stoj na jedné noze, později na nestabilní podložce. Pro domácí cvičení se hodí <a href="/balancni-podlozky-bosu/">balanční podložky</a>, konkrétní cviky a jejich postup ale nechte na odborníkovi. Unavený hráč dopadá hůř, a tak k prevenci patří i rozumná délka tréninku a odpočinek mezi zápasy.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Ortéza nasaje pot, a proto ji po tréninku vyndejte z tašky a nechte vyschnout na vzduchu. Prát ji můžete podle štítku, většinou ručně ve vlažné vodě s jemným pracím prostředkem a se zapnutými suchými zipy, aby nezachytávaly látku. Plastové výztuhy před praním vyndejte, pokud to výrobce umožňuje. Když se šněrování vytrhává nebo pásky přestávají držet, ortéza už neposkytuje oporu, se kterou počítáte.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Ortéza vyzkoušená bez boty, ve které se pak hraje.</li>'
          '<li>Silná ponožka se švem přes nárt pod šněrovací ortézou.</li>'
          '<li>Návrat na hřiště po podvrtnutí jen s ortézou, bez rehabilitace.</li>'
          '<li>Volné pásky, které se po pár minutách hry povolí.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu uvidíte nabídky různých obchodů a dostupné velikosti, nákup pak dokončíte u prodejce. Vyberte typ podle sportu a míry opory, změřte si nohu a velikost porovnejte s tabulkou výrobce. Pro koleno slouží kategorie <a href="/ortezy-na-koleno/">ortézy na koleno</a>, pro regeneraci po tréninku <a href="/kompresni-ponozky/">kompresní ponožky</a>.</p>',
    faq=[
        ('Jakou ortézu na kotník na volejbal?', 'Volejbalisté nejčastěji nosí šněrovací ortézy s pásky do osmičky nebo s bočními výztuhami. Vejdou se do halové obuvi, nebrání ve výskoku a omezí vytočení chodidla při doskoku na nohu spoluhráče nebo soupeře u sítě.'),
        ('Je lepší ortéza, nebo tejp?', 'Tejp je tenčí a lépe sedí v botě, musí se ale pokaždé znovu lepit a jeho nalepení chce cvik. Ortézu nasadíte rychle a můžete ji používat opakovaně. Co je pro vás vhodnější, poradí fyzioterapeut.'),
        ('Jak zvolit velikost ortézy na kotník?', 'Podle tabulky výrobce. Některé značky určují velikost podle čísla boty, jiné podle obvodu kotníku. Měřte krejčovským metrem na místě, které výrobce uvádí.'),
        ('Pomůže ortéza po podvrtnutí kotníku?', 'Po podvrtnutí nejdřív nechte kotník vyšetřit, zvlášť když je oteklý nebo na nohu nemůžete došlápnout. Lékař nebo fyzioterapeut rozhodne, jakou oporu kloub potřebuje, jak dlouho ji nosit a kdy se můžete vrátit ke sportu.'),
        ('Vejde se ortéza do boty?', 'Tenké šněrovací a elastické ortézy ano, jen je občas potřeba povolit tkaničky nebo zvolit botu o půl čísla větší. Vždy je zkoušejte s obuví a ponožkami, ve kterých hrajete, a projděte se v nich.'),
        ('Je ortéza na kotník levá a pravá?', 'Záleží na modelu. Elastické bandáže a mnoho šněrovacích ortéz je univerzálních, modely s výztuhami a pásky se často vyrábějí zvlášť pro levou a pravou nohu. Informaci najdete v popisu produktu nebo na obalu.'),
        ('Jak ortézu na kotník prát?', 'Většinou ručně ve vlažné vodě s jemným prostředkem, se zapnutými suchými zipy a bez vyjímatelných výztuh. Sušte ji na vzduchu, ne na topení, kde by se mohla zdeformovat. Vždy se řiďte štítkem.'),
    ])

# ------------------------------------------------------------------ fotbalove-dresy
NEW['fotbalove-dresy'] = dict(long=True,
    title='Fotbalové dresy: klubové, reprezentační i týmové',
    desc='Fotbalové dresy klubů a reprezentací v replice i hráčské verzi, týmové sady pro kluby a dětské dresy. Rozdíly, velikosti, potisk a péče o dres.',
    intro='<p>Fotbalový dres nosí hráči na zápasy a tréninky, fanoušci na stadion a děti na hřiště v barvách svého oblíbeného klubu. Pod jedním názvem se ale skrývá několik různých věcí. Klubové a reprezentační dresy se prodávají ve verzi pro fanoušky, které se říká replika, a v hráčské verzi, kterou výrobci označují jako autentickou nebo zápasovou. Kluby a školy zase kupují týmové dresy z katalogových řad, které se dají potisknout čísly a doobjednat i po několika sezonách. Každá skupina se jinak střihá a jinak se u ní vybírá velikost, a tak se vyplatí vědět, co přesně hledáte, ještě než začnete porovnávat.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů a nákup dokončíte na webu prodejce. Najdete tu dresy ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('joma', 'Joma'), ('lotto', 'Lotto')) + ' a dalších značek. Nadřazená kategorie jsou <a href="/dresy/">dresy</a>, ostatní fotbalové vybavení je v kategorii <a href="/fotbal/">fotbal</a>.</p>',
    guide='<h2>Replika a hráčská verze</h2>'
          '<p>Velké značky šijí klubové a reprezentační dresy ve dvou provedeních. Replika je určená fanouškům: má volnější střih, odolnější a o něco těžší materiál a znak klubu i logo výrobce bývají vyšité nebo nažehlené. Nosí se pohodlně na stadionu i na běžné nošení a vydrží časté praní. Hráčská verze se šije stejně jako dresy, ve kterých nastupují profesionálové. Je lehčí, užší a z prodyšnější úpletové látky s větracími zónami, znaky jsou tepelně nalisované, aby nic nedřelo. U Adidasu se jí říká autentický dres, Nike rozlišuje verzi Match pro hráče a Stadium pro fanoušky.</p>'
          + T(['', 'Replika pro fanoušky', 'Hráčská verze'], [
              ['střih', 'volnější, klasický', 'přiléhavý, sportovní'],
              ['materiál', 'odolnější úplet', 'lehčí a prodyšnější, se síťovanými zónami'],
              ['znak a logo', 'vyšité nebo nažehlené', 'tepelně nalisované, ploché'],
              ['pro koho', 'fanoušci, běžné nošení, děti', 'hráči, sběratelé, kdo chce dres jako na hřišti'],
              ['velikost', 'obvykle podle běžného oblečení', 'často o číslo větší, podle tabulky výrobce']]) +
          '<p>Kluby mají obvykle tři sady: domácí, venkovní a třetí, kterou hrají, když se barvy obou týmů tlučou. Brankář má vlastní dres v odlišné barvě, často s dlouhým rukávem a polstrováním na loktech. Nové dresy kluby představují zpravidla před začátkem sezony a reprezentace před velkými turnaji.</p>'
          '<h2>Týmové dresy pro kluby a školy</h2>'
          '<p>Amatérský klub, školní tým nebo parta na malou kopanou nepotřebuje replikové dresy, ale jednoduché a odolné týmové sady. Výrobci pro ně mají katalogové řady, třeba Entrada u Adidasu, Park u Nike nebo týmové kolekce Joma a Lotto. Jejich výhodou je, že se v nabídce drží několik sezon, a tak se dá doplnit dres pro nového hráče ve stejné barvě a střihu. Řady mívají více barev, ladící <a href="/sportovni-kratasy/">trenky</a> a <a href="/fotbalove-chranice-a-stulpny/">štulpny</a> a k tomu tréninková trička, bundy a soupravy.</p>'
          '<p>Při objednávání pro celý tým se vyplatí nejdřív sepsat velikosti všech hráčů a jednu sadu nechat zkusit. Dospělí a děti často hrají ve stejném modelu, juniorské velikosti jsou ale uvedené jinak. Počítejte i s rezervou pro hráče, kteří přijdou během sezony. Pro nejmenší hráče se prodávají i dětské sady, kde je dres, trenky a štulpny v jednom balení, což usnadní nákup pro rodiče i trenéry přípravek.</p>'
          '<h2>Velikosti: dětské a dospělé</h2>'
          '<p>Dětské a juniorské dresy se značí podle výšky postavy v centimetrech nebo podle věku, dospělé písmeny od XS po XXL. Výrobci mají vlastní tabulky s obvodem hrudníku a výškou, a právě podle nich se vyplatí vybírat. U dětí, které rychle rostou, je rozumné vzít dres s malou rezervou, ne o dvě velikosti větší; příliš dlouhý dres plandá a překáží při běhu. Hráčské verze bývají střižené úzce, a kdo nechce dres těsně na tělo, obvykle bere o číslo víc. Dámské a dívčí dresy mají kratší rukáv a užší pas a velikostní řadu odlišnou od pánské.</p>'
          '<h2>Jména a čísla</h2>'
          '<p>Na dres si můžete nechat natisknout jméno a číslo hráče. U klubových dresů se používá oficiální písmo dané soutěže, které nabízejí jen někteří prodejci, u týmových sad volíte písmo a barvu sami. Nejčastější technikou je nažehlovací fólie nebo flock se sametovým povrchem, týmové dresy se celé potiskují také sublimací, kdy barva přejde přímo do vlákna. Před objednáním potisku zkontrolujte pravopis jmen a čísla, protože dres upravený na přání zákazníka bývá z možnosti vrácení vyloučený. Podmínky si přečtěte u konkrétního obchodu.</p>'
          '<h2>Materiál a pohodlí při hře</h2>'
          '<p>Dnešní fotbalové dresy se šijí převážně z polyesteru, často i z recyklovaného. Úplet odvádí pot od těla a rychle schne, takže se dres po přestávce nepřilepí na záda. Bavlněné dresy se dnes skoro nevyrábějí, protože pot drží a těžknou. V chladu se pod dres nosí funkční vrstva, třeba termoprádlo s dlouhým rukávem, místo trička z bavlny. Brankáři ocení dres s polstrováním na loktech a s delším rukávem, který chrání při pádech na tvrdém trávníku.</p>'
          '<h2>Jak dres prát, aby vydržel</h2>'
          '<ul><li>Před praním dres otočte naruby, aby se potisk a znaky nedřely o buben.</li>'
          '<li>Perte na nízkou teplotu podle štítku, obvykle kolem 30 °C, s jemným prostředkem a bez aviváže.</li>'
          '<li>Nedávejte ho do sušičky, teplo odlupuje nalisované znaky a čísla.</li>'
          '<li>Nežehlete přes potisk; pokud je to nutné, žehlete naruby na nízkou teplotu.</li>'
          '<li>Sušte na ramínku ve stínu, ne na topení.</li></ul>'
          '<h2>Pravé dresy a padělky</h2>'
          '<p>Klubové dresy patří k často padělanému zboží. Podezřelé jsou nabídky z neznámých webů za cenu hluboko pod obvyklou úrovní, křivě umístěné znaky, nekvalitní výšivky a chybějící visačky. Nakupujte u obchodů, které uvádějí sídlo, kontakt a obchodní podmínky. Sporteka zobrazuje nabídky českých e-shopů, u kterých si podmínky můžete ověřit dřív, než objednáte.</p>'
          '<h2>Dresy na malou kopanou a futsal</h2>'
          '<p>Malá kopaná a futsal se hrají v menších týmech, často na umělé trávě nebo v hale, a dresy se tu vybírají hlavně podle ceny za celou sadu a podle odolnosti. Výhodou jsou katalogové řady se širokou paletou barev, protože soutěže obvykle chtějí, aby se dresy obou týmů jasně lišily. Brankář musí mít barvu odlišnou od spoluhráčů i soupeře. V hale se hodí lehčí dres s krátkým rukávem, venku v zimě pod něj hráči přidávají funkční vrstvu.</p>'
          '<h2>Fandění v zimě</h2>'
          '<p>Na podzimní a zimní zápasy si fanoušci berou dres přes mikinu nebo bundu, a proto volí o číslo větší repliku. Kdo chce mít dres pod bundou, ocení repliku s dlouhým rukávem, kterou některé kluby nabízejí. Hráčská verze je na stadion v chladu příliš tenká a těsná.</p>'
          '<h2>Retro dresy</h2>'
          '<p>Vedle aktuálních sad se prodávají i retro dresy, tedy kopie slavných dresů z minulých desetiletí. Mají jednodušší střih, často límeček a bavlněný nebo bavlnu připomínající materiál a nosí se hlavně jako módní kousek nebo dárek pro pamětníka. Některé kluby a výrobci je vydávají jako oficiální reedice k výročím. Na zápas na umělce se příliš nehodí, protože jsou těžší a hůř odvádějí pot, na fandění ale fungují skvěle.</p>'
          '<h2>Tréninkové oblečení v klubových barvách</h2>'
          '<p>Klubové kolekce nekončí u zápasového dresu. Prodávají se i tréninková trička, předzápasové dresy, ve kterých se hráči rozcvičují, mikiny, bundy a soupravy. Tréninková trička bývají jednodušší a bez reklamy sponzora, takže je fanoušci nosí i do posilovny. Pro amatérské týmy mají výrobci k týmovým dresům sladěné <a href="/teplakove-soupravy/">teplákové soupravy</a> a bundy, aby celý tým vypadal jednotně i na lavičce.</p>'
          '<h2>Dres jako dárek</h2>'
          '<p>Dres oblíbeného klubu nebo reprezentace patří k častým dárkům pro malé i velké fanoušky. Když velikost neznáte, vezměte repliku, která se střihem blíží běžnému tričku, a ověřte si u obchodu možnost výměny. U dětí pomůže zjistit výšku, protože podle ní se juniorské dresy značí. S potiskem jména a čísla počkejte, až budete mít velikost jistou, protože upravený dres se už nedá jen tak vyměnit. Hodí se také zjistit, jestli obdarovaný chce domácí, nebo venkovní sadu.</p>'
          '<h2>Co k dresu přikoupit</h2>'
          '<p>Kompletní fotbalový úbor tvoří dres, trenky, štulpny a chrániče holení. Na hřiště k tomu patří <a href="/kopacky/">kopačky</a> na trávu nebo <a href="/turfy/">turfy</a> na umělý povrch a na trénink vlastní <a href="/fotbalove-mice/">fotbalový míč</a>. Fanoušci často kombinují dres se šálou nebo kšiltovkou v klubových barvách.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>U každého dresu uvidíte nabídky více obchodů a velikosti, které jsou právě skladem, objednávku pak dokončíte u prodejce. Nejdřív si ujasněte, jestli chcete repliku, hráčskou verzi, nebo týmový dres, potom podle tabulky výrobce vyberte velikost. U týmových objednávek porovnejte, které obchody mají skladem celou velikostní řadu a nabízejí i potisk.</p>',
    faq=[
        ('Jaký je rozdíl mezi replikou a autentickým dresem?', 'Replika je pro fanoušky, má volnější střih, odolnější materiál a vyšité znaky. Autentický neboli hráčský dres je lehčí, přiléhavější a se znaky nalisovanými teplem, stejně jako dresy profesionálů.'),
        ('Jakou velikost fotbalového dresu vybrat?', 'Podle tabulky výrobce s obvodem hrudníku a výškou. Repliky velikostí odpovídají běžnému oblečení, hráčské verze jsou užší a mnoho lidí bere o číslo větší. Kdo chce dres nosit přes mikinu, volí také větší velikost.'),
        ('Jak se značí dětské fotbalové dresy?', 'Obvykle podle výšky dítěte v centimetrech nebo podle věku, přesné hodnoty má každý výrobce ve své tabulce. Dres vybírejte s malou rezervou, protože příliš velký plandá a překáží při hře.'),
        ('Lze na dres natisknout jméno a číslo?', 'Ano, potisk nabízí řada obchodů. U klubových dresů se používá oficiální písmo soutěže. Dres upravený na přání bývá z vrácení vyloučený, proto jména a čísla před objednáním zkontrolujte.'),
        ('Jaké dresy koupit pro amatérský tým?', 'Týmové katalogové řady, třeba Adidas Entrada, Nike Park nebo kolekce Joma a Lotto. Drží se v nabídce několik sezon, takže dres pro nového hráče doplníte ve stejné barvě.'),
        ('Jak prát fotbalový dres?', 'Naruby, na nízkou teplotu podle štítku, s jemným prostředkem a bez aviváže. Nesušte ho v sušičce a nežehlete přes potisk.'),
        ('Jak poznám padělaný dres?', 'Varovné znaky jsou podezřele nízká cena, neznámý obchod bez kontaktu a sídla, nekvalitní výšivky, křivě umístěné znaky a chybějící visačky. Nakupujte u obchodů s jasnými obchodními podmínkami a možností reklamace.'),
    ])
