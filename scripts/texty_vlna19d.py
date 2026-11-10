"""sporteka.cz — wave 19d (4. 11. 2026): long texts (>= 1650 words) for hokejove-brusle, lovecke-obleceni, posilovaci-stroje, ostatni-micove-sporty.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ hokejove-brusle
NEW['hokejove-brusle'] = dict(long=True,
    title='Hokejové brusle: velikost, šířka, tuhost, ostření',
    desc='Hokejové brusle pro děti, juniory, dospělé i brankáře. Jak vybrat velikost a šířku, tuhost boty, držák s ostřím a kde porovnat nabídky obchodů.',
    intro='<p>Hokejová brusle má zvláštní postavení v celé výbavě: nechrání jako helma, ale rozhoduje o tom, jak jistě se na ledě pohybujete, jak rychle se rozjedete a jak dlouho vydržíte bez bolavých nohou. '
          'Špatně zvolená velikost nebo příliš tuhá bota dokážou zkazit radost z hokeje dřív než jakákoli chyba v technice. Naopak dobře padnoucí pár se po krátkém zajetí chová jako prodloužení nohy.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u dětských, juniorských i seniorských modelů, najdete tu rekreační pár pro veřejné bruslení i závodní špičku. Zastoupené jsou hlavně značky Bauer, CCM, Daoust a Winnwell. '
          'Pro skládání celé výbavy navštivte také <a href="/hokejky/">hokejky</a>, <a href="/hokejove-chranice/">hokejové chrániče</a> a <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>. Níže vysvětlujeme, jak si brusle změřit, vybrat a udržovat.</p>',
    guide='<h2>Z čeho se hokejová brusle skládá</h2>'
          '<p>Brusle tvoří čtyři hlavní celky: bota (kopyto), jazyk, držák a ostří. Skořepina bývá z kompozitu nebo z kombinace plastu a syntetické tkaniny, uvnitř je tvarovatelná výstelka. '
          'Držák, tedy plastová nebo kompozitní konstrukce pod botou, nese ocelové ostří a u většiny značek jde vyměnit, takže po poškození nemusíte kupovat celou brusli. '
          'Právě tato modularita je důvod, proč se vyplatí rozumět jednotlivým dílům před nákupem.</p>'
          + T(['Díl', 'K čemu slouží', 'Na co se zaměřit'], [
              ['Bota', 'drží kotník a chodidlo, přenáší sílu', 'tuhost, tvar špičky, šířka a objem'],
              ['Jazyk', 'chrání nárt před tlakem hůlky a puku', 'pružný nebo tužší, případně s vložkou'],
              ['Výstelka', 'tvoří styk s nohou', 'termotvarovatelný materiál, odvětrání'],
              ['Držák', 'spojuje botu s ostřím', 'výška, možnost výměny, uchycení ostří'],
              ['Ostří', 'vede brusli po ledě', 'ocel, radius broušení, stav hran']]) +
          '<h2>Velikost: o číslo menší než běžná obuv</h2>'
          '<p>Hokejové brusle se kupují menší než civilní boty, obvykle o jedno až půldruhého čísla. Důvod je jednoduchý: noha v brusli musí sedět pevně, aby se při záběru neposouvala. '
          'Pro orientaci změřte délku chodidla od paty k nejdelšímu prstu a porovnejte ji s tabulkou konkrétního výrobce. Tabulky mezi značkami nejsou stejné, takže stejné číslo u dvou výrobců nemusí sedět stejně.</p>'
          '<p>Při zkoušce brusli pevně utáhněte, předkloňte se a ověřte, že pata zůstává vzadu a špičky se jen lehce dotýkají přední části. Prsty nemají být ohnuté ani přitisknuté. Pokud pata zvedá při předklonu, je bota příliš velká nebo má špatný objem.</p>'
          '<h2>Šířka a objem chodidla</h2>'
          '<p>V severoamerickém značení se používá šířka D pro standardní chodidlo, EE pro širší a někdy se objevují i další varianty. Jednotlivé řady jednoho výrobce mají navíc odlišný tvar kopyta: některé jsou štíhlé a přiléhavé, jiné prostornější. '
          'Značky Bauer a CCM tradičně rozlišují různé profily nohy a v popisu produktu je lze dohledat. Pokud při první zkoušce tlačí boky chodidla, nehledejte větší číslo, ale širší model.</p>'
          + T(['Typ chodidla', 'Příznak v brusli', 'Co zvolit'], [
              ['Úzké a štíhlé', 'noha se kývá, pata zvedá', 'užší kopyto, pevnější utažení'],
              ['Standardní', 'sedí bez tlaku po stranách', 'běžná šířka D'],
              ['Široké', 'tlak na malíku a kloubech', 'širší kopyto nebo varianta EE'],
              ['Vysoký nárt', 'tlak pod šněrováním', 'prostornější model s měkčím jazykem']]) +
          '<h2>Tuhost boty podle úrovně hráče</h2>'
          '<p>Tuhost boty určuje, kolik síly se z kotníku přenese na led a jak dlouho se hráč v brusli udrží bez únavy. Tvrdší bota je reaktivnější, ale vyžaduje silné nohy a dobrou techniku, jinak působí jako svěrák. '
          'Měkčí modely jsou komfortnější a odpouštějí chyby, takže se hodí pro začátečníky, rekreační hráče i děti, které rychle rostou. Výrobci tuhost označují vlastními stupnicemi a názvy řad, proto se nesrovnává číslo mezi značkami, ale úroveň v rámci jedné řady.</p>'
          '<ul><li><strong>Začátečníci a děti:</strong> pohodlí, měkčí kopyto, výstelka bez tlakových míst.</li>'
          '<li><strong>Pokročilí amatéři:</strong> střední tuhost, tvarovatelná bota, vyměnitelný držák.</li>'
          '<li><strong>Soutěžní hráči:</strong> tuhé kompozitní boty, nízký držák, přesný tvar nohy.</li></ul>'
          '<h2>Velikostní řady: dětské, juniorské, seniorské</h2>'
          '<p>Kategorie se dělí na mladší děti (Youth), junioři a seniory (Senior). Mezi nimi se někdy objevuje i střední velikost Intermediate. U nejmenších existují posuvné modely s nastavitelnou délkou, které vydrží více sezón, protože se dají prodloužit o několik čísel. '
          'Zkoušejte ale vždy s hokejovou ponožkou, ne s tlustou zimní, jinak koupíte nevhodný pár. Seniorské velikosti začínají tam, kde končí juniorské, a platí pro dospělé i vyšší mladistvé.</p>'
          '<h2>Držák a ostří</h2>'
          '<p>Ostří je z oceli a jeho výška i radius broušení ovlivňují chování na ledě. Výraznější zakřivení ostří dává větší obratnost při zatáčení, plošší profil stabilitu v přímém směru. '
          'Základní vodítko: čím větší radius, tím delší kontakt s ledem a tím stabilnější jízda. Běžně se brousí na hodnoty v rozmezí několika stop a každý hráč si časem najde vlastní preferenci. Brusiči v hokejových obchodech i na zimních stadionech nabízejí různé profily a lze je střídat podle potřeby.</p>'
          '<p>Po každém tréninku ostří otřete suchým hadrem, aby nezačalo rezivět. Neprocházejte v bruslích po betonu nebo gumové podlaze bez chráničů ostří a po zápase nenechávejte brusle zavřené v mokré tašce.</p>'
          '<h2>Rekreační versus závodní řady</h2>'
          '<p>Nabídka obsahuje i levnější modely pro veřejné bruslení. Mají měkčí skořepinu, jednodušší držák a často trvanlivější syntetickou výstelku, ale pro tvrdší trénink a zápasy je nevyužijete naplno. '
          'Pokud jezdíte jen zřídka, oceníte komfort a odolnost proti vlhkosti. Chcete-li hrát pravidelně v lize, potřebujete tvar kopyta a tuhost, která drží kotník při změně směru.</p>'
          '<p>Rekreační bruslení jiného typu najdete v kategoriích <a href="/rekreacni-brusle/">rekreační brusle</a> a <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a>. Vše dohromady zastřešuje <a href="/brusle/">hlavní přehled bruslí</a>.</p>'
          '<h2>Brankářské brusle</h2>'
          '<p>Brankář nepotřebuje rychlý záběr, ale boční posun, kryt a stabilitu. Brankářská brusle má proto plošší a níže posazené ostří, vyztužené boky boty a menší flexibilitu v přední části. '
          'Na Sportece se vyskytují i brankářské modely, například řada GSX od značky Bauer. Kompletní brankářská sada, tedy chrániče, lapačka i vyrážečka, je v kategorii <a href="/hokejove-brankarske-vybaveni/">hokejové brankářské vybavení</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(('bauer', 'Bauer'), ('ccm', 'CCM'), ('daoust', 'Daoust'), ('winnwell', 'Winnwell'), ('sherwood', 'Sherwood')) + '. '
          'Bauer a CCM jsou dvě hlavní hokejové značky, u nichž najdete celé řady od dětských po špičkové. Daoust a Winnwell nabízejí cenově dostupnější páry pro začátečníky a mládež. '
          'Rozdíly mezi značkami se většinou týkají tvaru kopyta, takže není vhodné kupovat podle jména, ale podle toho, jak model sedí na vaší noze.</p>'
          '<h2>Tvarování a první zajetí</h2>'
          '<p>Většina vyšších modelů má tepelně tvarovatelné díly. V hokejovém servisu se bota zahřeje v pícce a nasazená se přizpůsobí obrysu kotníků a paty. Po tvarování stojte chvíli ve stoji s lehce pokrčenými koleny, aby se materiál usadil podle vašeho postoje. '
          'První dvě až tři jízdy bývají nepohodlné, protože výstelka i skořepina se teprve uleží. Pokud ale bolest trvá déle než týden, jde o chybnou velikost nebo tvar, ne o zajíždění.</p>'
          '<h2>Šněrování, ponožky a doplňky</h2>'
          '<p>Šněrování se utahuje postupně od špičky ke kotníkům. Špičku utáhněte jen lehce, přes nárt pevněji a kolem kotníku nejsilněji. Příliš utažený nárt může omezit prokrvení. '
          'Používejte tenké ponožky z technického materiálu a nepřidávejte druhou vrstvu, protože zhorší cit. Vhodné jsou <a href="/sportovni-ponozky/">sportovní ponožky</a> a pro chlad i termo varianty. '
          'K brusli se hodí také chrániče ostří, brousek a sušicí návleky. Pásky, zesilovače a další drobnosti najdete v <a href="/hokejove-pasky-a-doplnky/">hokejových páskách a doplňcích</a>.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po zápase vytáhněte vložky, povolte šněrování a nechte brusle vyschnout při pokojové teplotě. Neumisťujte je k topení ani do auta na slunci, protože teplo poškozuje lepené spoje a výstelku. '
          'Do tašky patří suché brusle s chrániči ostří. Cvičební tašku vybírejte s odvětráním, například z kategorie <a href="/hokejove-tasky/">hokejové tašky</a>. Ostří nechte pravidelně brousit podle frekvence hraní, ne podle kalendáře: hokejista na ledě několikrát týdně potřebuje broušení častěji než veřejný bruslař.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě „na vyrůstání“: o velikost větší brusle znamenají nejistý krok a horší techniku.</li>'
          '<li>Hodnocení podle vzhledu a značky bez zkoušky tvaru.</li>'
          '<li>Použití silných ponožek při zkoušce.</li>'
          '<li>Zapomenutí na ostření nových bruslí, které z výroby nemusí být připravené na hru.</li>'
          '<li>Ukládání mokrých bruslí do uzavřené tašky.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého páru vidíte nabídky více obchodů, velikosti, které jsou skladem, a přímý odkaz do e-shopu. Použijte filtr podle značky a velikosti, abyste nevybírali z modelů, které nesedí. '
          'Pokud nakupujete pro dítě, ověřte možnost vrácení, protože růst chodidla je rychlý a velikost je vhodné zkontrolovat po doručení. Výběr ostatní výbavy najdete v hlavní kategorii <a href="/hokej/">hokej</a>, kde jsou i <a href="/hokejove-puky-a-branky/">puky a branky</a> a <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>.</p>',
    faq=[
        ('O kolik menší brusle mám koupit než běžné boty?', 'Většinou o jedno až půldruhého čísla menší, ale přesnou velikost vždy ověřte v tabulce výrobce a zkuste v tenké hokejové ponožce. Nohu v brusli drží pevné sevření, proto nemá být prostorná.'),
        ('Jaký je rozdíl mezi šířkou D a EE?', 'D označuje standardní šířku chodidla, EE širší kopyto. Pokud brusle tlačí po stranách a prsty mají místo, je správným řešením širší model, ne větší číslo. Tvar kopyta se ale liší i mezi řadami jedné značky.'),
        ('Mám brusle po koupi nechat vytvarovat?', 'U modelů s termotvarovatelnou skořepinou je to dobrý nápad. V servisu se bota ohřeje a přizpůsobí kotníku a patě. Pokud brusle nijak netlačí, můžete zkusit jen zajet; k tvarování se vyplatí vrátit, když máte tlakové body.'),
        ('Jak často nechat brusle brousit?', 'Podle frekvence hraní a stavu ledu. Aktivní hráč musí brousit častěji než rekreační bruslař. Pokud brusle při zatáčení podkluzují nebo nedrží hranu, je čas na ostření, i kdyby uběhlo málo týdnů.'),
        ('Dají se použít hokejové brusle na veřejné bruslení?', 'Ano, hokejová brusle je bezpečná i při běžném bruslení. Pro občasné využití však pohodlnější bývá rekreační model s měkčí botou. Oba typy se liší tuhostí a tvarem ostří, nikoli principem jízdy.'),
        ('Čím se liší brusle brankáře od hráčské?', 'Brankářská brusle má plošší ostří, vyztuženou botu na bocích a menší flexibilitu v kotníku. Slouží pro boční posun a kryt branky, nikoli pro dlouhý záběr. Hráčské brusle se v brance nehodí a naopak.'),
        ('Jakou velikost zvolit pro rostoucí dítě?', 'Takovou, která sedí teď. Příliš velká bota je nebezpečná, protože se noha v ní pohybuje a dítě ztrácí kontrolu. U nejmenších můžete zvolit nastavitelné brusle, které se prodlužují s rostoucím chodidlem.'),
        ('Jak poznám, že je brusle příliš tuhá?', 'Pokud se po několika jízdách kotník neohýbá, vzniká tlak na přední části holeně a nohy brzy znavíte, je bota pro vaši úroveň příliš tuhá. Začátečníkovi a rekreačnímu hráči ve většině případů stačí střední nebo měkčí řada.'),
        ('Jak vysušit brusle po tréninku?', 'Vyndejte vložky, povolte šněrování, roztáhněte jazyk a nechte brusle vyschnout při pokojové teplotě mimo zdroj tepla. Ostří otřete suchým hadrem a pro přepravu použijte chrániče, které nezadržují vlhkost.'),
        ('Je lepší koupit brusle s vyměnitelným držákem?', 'Pro aktivní hráče ano. Při poškození ostří nebo držáku vyměníte jen díl, nikoli celou brusli. U rekreačních modelů je držák často pevný a není potřeba řešit úpravy, proto na tento znak tolik nehleďte.'),
    ])

# ------------------------------------------------------------------ lovecke-obleceni
NEW['lovecke-obleceni'] = dict(long=True,
    title='Lovecké oblečení a obuv: maskování, vrstvy, ticho',
    desc='Lovecké bundy, kalhoty, trička, vesty a obuv. Jak vybrat maskování, tichý materiál, vrstvení do počasí a velikost a kde porovnat nabídky obchodů.',
    intro='<p>Myslivec tráví na stanovišti nebo při šoulání často několik hodin v klidu a v každém počasí. Oblečení pro tuto činnost musí být tiché, nenápadné barvou a vzorem a zároveň tepelně i vlhkostně promyšlené, protože pohyb se střídá s dlouhým sezením. '
          'Právě kombinace těchto požadavků odlišuje lovecký oděv od běžné outdoorové konfekce.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u bund, kalhot, triček, košilí, svetrů, vest i obuvi. Zastoupené jsou značky Solognac, Tagart, MFH, Camo Systems, Mil-Tec nebo Jack Pyke. '
          'K tématu patří také <a href="/lovecke-vybaveni/">lovecké vybavení</a>, <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a> a <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>. Níže projdeme materiály, vrstvení, vzory maskování, obuv a péči.</p>',
    guide='<h2>Co lovecké oblečení řeší</h2>'
          '<p>Zvěř reaguje na pohyb, tvar a ostrý zvuk víc než na samotnou barvu, takže prvním požadavkem je tichá tkanina. Látky, které při pohybu šustí, na stanovišti prozradí i drobné posunutí paže. '
          'Druhým požadavkem je povrch, který neodráží světlo, třetím tepelná pohoda při dlouhém klidu a čtvrtým odolnost proti trní, větvím a dešti. Dobrý oděv se hodnotí podle toho, jak se v něm lze skrýt, zahřát a nepřemýšlet o něm.</p>'
          + T(['Požadavek', 'Řešení v oděvu', 'Typické použití'], [
              ['Ticho', 'měkké tkaniny, fleece, bavlna, tiché membrány', 'čekaná, šoulání, posed'],
              ['Maskování', 'vzory přizpůsobené prostředí, matná barva', 'les, pole, bažiny'],
              ['Teplo při klidu', 'vrstvení, izolace, vyšší límec', 'podzim a zima na posedu'],
              ['Odolnost', 'zpevněné kolena a lokty, ripstop', 'prodírání křovím'],
              ['Nepromokavost', 'membrána nebo impregnace', 'déšť, mokrá tráva']]) +
          '<h2>Vrstvení: tři vrstvy místo jedné tlusté</h2>'
          '<p>Při lovu se tělo střídavě zahřívá chůzí a ochlazuje klidem, proto jedna silná bunda nestačí. Základní vrstva odvádí pot od kůže, střední vrstva drží teplo a svrchní chrání před větrem a deštěm. '
          'Základem jsou termoprádlo a merino, na tělo se hodí <a href="/termopradlo/">termoprádlo</a> nebo <a href="/merino-pradlo/">merino prádlo</a>. Bavlna pohlcuje pot a pomalu schne, takže u kůže je méně vhodná při větším pohybu, zatímco při klidném sezení v teple stačí.</p>'
          '<p>Střední vrstvu tvoří <a href="/fleecove-mikiny/">fleecové mikiny</a>, vlněné svetry nebo lehká izolace. Svrchní vrstvu volte podle sezóny: <a href="/softshellove-bundy/">softshellová bunda</a> pro suché chladné dny a <a href="/nepromokave-bundy/">nepromokavá bunda</a> pro déšť. Zimní doplnění najdete v kategorii <a href="/kabaty-a-parky/">kabáty a parky</a>.</p>'
          '<h2>Maskovací vzory</h2>'
          '<p>Nejrozšířenější jsou vzory podle typu prostředí. Listnatý les s opadem zná pestrou hnědozelenou kresbu, jehličnatý les zase tmavší odstíny, pole a okraje lesa se hodí k světlejším tónům. Některé vzory napodobují kůru, listí nebo trávu přímo a vytvářejí plasticitu. '
          'Pro příklad Woodland používají velké skvrny zelené, hnědé a černé, zatímco vzory typu Treemetic od značky Solognac napodobují stromové struktury a řeší i potlačení šustění. U každého modelu zkontrolujte, jaké roční období a prostředí výrobce uvádí, protože zelený kus je v zimě nápadný.</p>'
          '<p>Dobrá volba je neutrální dvoubarevná kombinace. Jednobarevná zelená nebo hnědá často maskuje lépe než nevhodně zvolený vzor, hlavně na stanovišti u pole. Důležitá je i matná úprava: lesklé zipy, nášivky a reflexní prvky vypadají v zorném poli zvěře jako světelný bod.</p>'
          '<h2>Bundy a kalhoty</h2>'
          '<p>Lovecká bunda by měla mít tiché zipy nebo suchý zip s krytím, kapsy v dosahu paží při držení zbraně a rukávy, které při namíření neklouzají. Lehčí bundy se nosí na jaře a v létě, zimní s izolací vyžadují prostornější střih, aby nebránily pohybu ramen. '
          'Kalhoty jsou z odolného materiálu, často z ripstopu, a mají zpevněná kolena. Zvlášť oceníte vyšší pas a nastavitelný opasek, protože při sezení se klasické kalhoty zbytečně stahují. Více nabídky univerzálních modelů najdete v <a href="/outdoorove-kalhoty/">outdoorových kalhotách</a>.</p>'
          + T(['Kus oděvu', 'Na co si dát pozor', 'Sezóna'], [
              ['Tričko a košile', 'prodyšnost, tichý materiál, dlouhý rukáv proti hmyzu', 'jaro až podzim'],
              ['Mikina a svetr', 'hustota úpletu, nešustění', 'chladné dny'],
              ['Bunda', 'zipy, kapsy, kapuce, nepromokavost', 'celoročně dle typu'],
              ['Kalhoty', 'kolena, nastavení pasu, odolnost', 'celoročně'],
              ['Vesta', 'pohyblivost paží, kapsy', 'přechodná období']]) +
          '<h2>Vesty, čepice a doplňky</h2>'
          '<p>Vesta nahradí rukávy tam, kde stačí zahřát trup, a nechává paže volné. Hodí se při šoulání, na čekané ji doplníte pod bundu. Čepice, kukly a nákrčníky řeší obličej a krk, které zvěř vidí nejlépe, a chrání před chladem. '
          'Podívejte se na <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a> a <a href="/sportovni-rukavice/">rukavice</a>, ideálně tenké, které nebrání citlivému zacházení se spouští.</p>'
          '<p>Maskovací převleky, takzvané ghillie, jsou určeny hlavně pro přírodní vegetaci. Zvlášť v této nabídce je velké množství kamuflážních sítí a převleků od značek Camo Systems a Jack Pyke. Převlek se nenosí jako běžný oděv, ale přes něj, při zachování hlavní vrstvy pod ním.</p>'
          '<h2>Obuv pro lov</h2>'
          '<p>Obuv volíte podle terénu a ročního období. V suchém lese se hodí vysoké kožené nebo textilní boty s dobrým vzorkem podrážky a pevným podpětím kotníku. Do mokrých luk a rákosí pomáhají <a href="/holinky/">holínky</a>, do zimy izolované boty. '
          'Obecně dobře fungují <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>, protože chrání kotník a nesou zátěž. Podrážka by měla být tichá a ne příliš hrubá, jinak se na kamenech ozývá. Tichou chůzi podporuje i měkčí materiál svršku.</p>'
          '<p>K obuvi patří vhodné ponožky. Pro zimu a delší čekání zvolte vlněné, třeba <a href="/merino-ponozky/">merino ponožky</a>, protože zůstávají teplé i při vlhkosti. Vždy mějte pár na výměnu a obuv nechte přirozeně vyschnout.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Lovecký oděv má sedět volněji než sportovní, aby se pod ním vešly vrstvy a aby nebránil při míření. Přílišná volnost ale vytváří záhyby, které šustí a zachytávají větve. Zkoušejte s vrstvami, které budete nosit, a prověřte pohyb paží nad hlavu i předklon. '
          'U dámských modelů hledejte kratší rukáv a tvar v pase, zvlášť pokud je na webu dámská varianta, protože pánský střih bývá delší. Dětské a mládežnické velikosti se objevují zřídka, takže se vyplatí porovnat tabulku výrobce.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Z katalogu vybíráme ' + B(('solognac', 'Solognac'), ('tagart', 'Tagart'), ('mfh', 'MFH'), ('camo-systems', 'Camo Systems'), ('mil-tec', 'Mil-Tec'), ('jack-pyke', 'Jack Pyke'), ('percussion', 'Percussion')) + '. '
          'Solognac a Percussion jsou specializované lovecké značky, Tagart se zaměřuje na maskovací kolekce, Jack Pyke nabízí britský venkovský styl. Mil-Tec a MFH dodávají hlavně vojenské a outdoorové kousky, které myslivci často používají jako odolný základ.</p>'
          '<h2>Péče o lovecký oděv</h2>'
          '<p>Maskovací oděv perte šetrně, nejlépe bez parfemovaných pracích prostředků a aviváže. Vůně a optické zjasňovače mohou změnit odraz světla i pach, který zvěř zaznamená. Membránové bundy občas oživte impregnací a podle návodu je vyperte, jinak se zanesou nečistotami a přestanou odvádět vlhkost. '
          'Odění sušte mimo přímé slunce a uložte volně, aby se nepomačkalo. Vlněné kousky chraňte před moly.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě podle vzoru, ne podle materiálu: nejhezčí kamufláž nepomůže, pokud tkanina šustí.</li>'
          '<li>Jedna tlustá bunda místo vrstvení, která způsobí pocení při chůzi a promrznutí při čekání.</li>'
          '<li>Lesklé zipy a doplňky bez krytí.</li>'
          '<li>Příliš těsné kalhoty, které při sezení tlačí a ruší pohyb.</li>'
          '<li>Praní s běžnou aviváží, které mění vůni oděvu.</li></ul>'
          '<h2>Sezónní výběr: podzimní hon, zima a jaro</h2>'
          '<p>Na podzim se střídá mokro, mlha a ranní chlad, proto se vyplatí kombinace tišší tkaniny, prodyšné spodní vrstvy a nepromokavé bundy pro případ deště. V zimě rozhoduje izolace, hlavně u nohou, rukou a hlavy, protože při dlouhém sezení na posedu se nehýbáte a rychle prochladnete. '
          'Jarní oblečení má být lehčí, rychle schnoucí a odolné proti vlhké trávě, ale stále maskovací. Praktické je mít dvě tenčí vrstvy navíc, které lze podle počasí přidat nebo sundat, místo jedné objemné bundy.</p>'
          '<h2>Pro koho je lovecký oděv vhodný</h2>'
          '<p>Kromě myslivců jej využívají fotografové přírody, pozorovatelé zvěře, rybáři a lidé, kteří chtějí pevné kalhoty a bundu do lesa nebo na zahradu. Důležité je ale respektovat pravidla místa: v době společných honů je potřeba, aby vás ostatní viděli, a proto se doplňuje výrazná oranžová vesta nebo čepice. '
          'Při nákupu pro dospívající a ženy sledujte střih, protože některé řady jsou vyráběny hlavně pro mužskou postavu a dámské varianty mají jiné proporce.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Každý produkt ukazuje nabídky více obchodů, takže snadno ověříte dostupnost velikosti. Filtrujte podle značky, typu oděvu a velikosti. Při výběru zkontrolujte popis materiálu a sezónu určení. '
          'Doplňte výbavu o <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoola</a>, <a href="/turisticke-batohy/">turistické batohy</a> a ostatní z kategorie <a href="/lov-a-priroda/">lov a příroda</a>. Pro vodu a rybaření pak slouží <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>',
    faq=[
        ('Jaký materiál je pro lov nejtišší?', 'Měkké tkaniny jako fleece, vlna nebo hustě tkaná bavlna při pohybu šustí nejméně. Tvrdé nylonové povrchy a hrubé membrány bývají hlučnější. Hlučnost si ověřte při pohybu paže ve zkoušce, než model koupíte.'),
        ('Jaký maskovací vzor zvolit?', 'Podle prostředí. Do listnatého lesa se hodí pestřejší hnědozelené vzory, do jehličnatého tmavší, na pole a okraje lesa světlejší tóny. Neutrální matná barva bývá lepší než nevhodný vzor, zejména v zimě a na stanovišti u pole.'),
        ('Kolik vrstev na podzimní čekanou?', 'Obvykle tři: spodní prádlo odvádějící pot, střední vrstva z fleecu nebo vlny a svrchní větruodolná či nepromokavá vrstva. Při klidném sezení doplníte teplou vestu, čepici a rukavice, které se při chůzi sundají.'),
        ('Je lepší nepromokavá bunda s membránou, nebo softshell?', 'Softshell je pružný, tichý a prodyšný, dobře funguje při suchém a chladném počasí. Membránová bunda chrání lépe v dešti, ale bývá hlasitější a méně prodyšná. Mnozí myslivci mají obě a střídají je podle počasí.'),
        ('Jak vybrat velikost lovecké bundy?', 'Zvolte tak, aby se pod ní vešly vrstvy, a přitom neměla záhyby. Při zkoušce zvedněte paže, předkloňte se a namiřte. Pokud rukávy nebo záda povolují pohyb bez tahu, jde o dobrou velikost. Tabulky výrobců se mohou lišit.'),
        ('Mohu používat vojenské oblečení?', 'Ano, outdoorové a vojenské kousky se pro lov běžně používají, hlavně kalhoty, košile a doplňky. Ověřte maskovací vzor vzhledem k prostředí a to, zda tkanina nešustí. Vojenský střih někdy neřeší pohodlí při míření.'),
        ('Proč se nemá lovecký oděv prát s aviváží?', 'Avivážní a parfemované přísady zanechávají vůni a mohou měnit odraz světla. Zvěř vnímá pachy lépe než člověk, proto se doporučuje neparfemovaný prací prostředek a sušení venku. Funkční membrány také trpí zbytky aviváže.'),
        ('Jaká obuv se hodí na lov?', 'Záleží na terénu: vysoké boty s dobrou podrážkou do lesa, holínky do mokra, izolovaná obuv do zimy. Důležitá je tichá chůze, oporu kotníku a vodotěsnost zajistíte materiálem svršku. Ponožky volte vlněné a mějte náhradní pár.'),
        ('Je kamufláž potřeba u všech kusů?', 'Ne vždy. Základem je neutrální matná barva a maskování tváře a rukou. Vzor je nejdůležitější u svrchních dílů, které zvěř vidí. Spodní vrstvy a ponožky mohou být bez vzoru, pokud nejsou viditelné.'),
        ('Mohu lovecké oblečení nosit i na túry?', 'Ano, kalhoty, mikiny a bundy slouží také v lese při běžných výletech. Výrazný maskovací vzor ale nemusí být vhodný všude, třeba v době honu, kdy ostatní osoby v lese potřebují vás vidět.'),
    ])

# ------------------------------------------------------------------ posilovaci-stroje
NEW['posilovaci-stroje'] = dict(long=True,
    title='Posilovací stroje a lavice: věže, stojany, kladky',
    desc='Posilovací lavice, stojany, věže, kladky a žebřiny pro domácí posilovnu. Jak vybrat nosnost, rozměry a konstrukci a kde porovnat nabídky obchodů.',
    intro='<p>Domácí posilovna se většinou začíná lavicí a párem činek, jenže po pár měsících přijde chvíle, kdy chcete zátěž zvyšovat bezpečně a bez kamarádů, kteří by vás jistili. Právě tady nastupují stojany, věže s kladkami a speciální lavice. '
          'Dobře zvolený kus vybavení vydrží roky, špatně zvolený zabere půlku obýváku a po týdnu se stane věšákem na ručníky.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u posilovacích lavic, power racků, multifunkčních věží, protisměrných kladek, žebřin a doplňků od značek Insportline, HMS, Marbo, Benchk, Gorilla Sports nebo Tunturi. '
          'K tomu se hodí <a href="/cinky-a-kotouce/">činky a kotouče</a>, <a href="/kardio-trenazery/">kardio trenažéry</a> a celý přehled <a href="/fitness/">fitness a posilování</a>. Níže vysvětlujeme, jak si vybrat podle prostoru, cíle a rozpočtu bez zbytečných kompromisů.</p>',
    guide='<h2>Jaké typy vybavení tu najdete</h2>'
          '<p>Posilovací technika se dělí na dvě skupiny. První tvoří volné závaží s oporou, tedy lavice a stojany, u nichž zátěž skládáte z kotoučů. Druhou skupinou jsou stroje s vlastní zátěží nebo kladkovým systémem, kde činnost vede pevná dráha. '
          'Volné závaží vyžaduje víc techniky a prostoru, ale nabízí široký výběr cviků. Stroje jsou přehlednější, zabírají méně času na přípravu a dobře se hodí pro cvičení bez parťáka.</p>'
          + T(['Typ vybavení', 'K čemu slouží', 'Pro koho'], [
              ['Rovná lavice', 'tlaky vleže, přítahy jednoruč, opora při cvicích', 'začátečníci, minimalisté'],
              ['Variabilní lavice', 'nastavitelný sklon opěradla i sedáku', 'většina domácích posiloven'],
              ['Power rack a stojan', 'dřep, tlaky, shyby, jištění zátěže', 'pokročilí a silově zaměření'],
              ['Multifunkční věž', 'kladky, tlaky a přítahy na jednom místě', 'rodiny, malý prostor'],
              ['Protisměrné kladky', 'přítahy, tricepsové stahování, kabelové cviky', 'doplněk ke stojanu nebo zdi'],
              ['Žebřiny a hrazdy', 'visy, shyby, zdvihání nohou', 'cvičení s vlastní vahou']]) +
          '<h2>Posilovací lavice: rovná, variabilní, specializovaná</h2>'
          '<p>Rovná lavice je nejjednodušší a také nejstabilnější. Pokud chcete jen tlačit činky a provádět základní cviky, může stačit. Variabilní lavice nabízí několik poloh opěradla od mírného sklonu po téměř svislou, což rozšíří nabídku o tlaky na ramena v sedě nebo o šikmé tlaky s činkami. '
          'U všech lavic ověřujte nosnost, kterou výrobce uvádí jako celkovou hodnotu včetně hmotnosti cvičícího, a také šířku sedáku. Úzká lavice je pohyblivější, ale méně stabilní při těžkých sériích.</p>'
          '<p>Specializované lavice mají konkrétní účel. Scottova lavice podepírá paže při bicepsových zdvizích a dobře eliminuje švihání, římská lavice (hyperextenze) posiluje záda a hýždě a lavice na břicho má šikmé opěradlo s fixací nohou. '
          'Marbo a Insportline se v nabídce vyskytují u všech uvedených typů, HMS a Benchk zase u silnějších variant s ocelovou konstrukcí.</p>'
          '<h3>Na co se u lavice dívat</h3>'
          '<ul><li><strong>Konstrukce rámu:</strong> hrubší ocelová trubka a svary bez ostrých hran, pevné stavění bez viklání.</li>'
          '<li><strong>Čalounění:</strong> pevná pěna, která při sednutí nepropadá, a potah odolný proti potu.</li>'
          '<li><strong>Nastavení sklonu:</strong> západky nebo kolík, které drží pevně a nepřeskakují.</li>'
          '<li><strong>Hmotnost a podložky:</strong> těžší lavice se hůř posouvá, gumové patky chrání podlahu.</li>'
          '<li><strong>Možnost skládání:</strong> důležitá, pokud posilovna sdílí místnost s jinou činností.</li></ul>'
          '<h2>Stojany a power racky</h2>'
          '<p>Stojan na dřepy nebo celý power rack tvoří rám se čtyřmi sloupy, který drží osu ve zvolené výšce a pod ní jistící tyče. Díky nim se tyč při selhání nezřítí na hrudník. Jistící tyče nebo ramena jsou základní bezpečnostní prvek každého silového cvičení bez parťáka, a proto je při nákupu nepodceňujte. '
          'Rámy se liší hloubkou, výškou a profilem sloupů. Nižší stojany se vejdou do garáže nebo sklepa se standardním stropem, vyšší dovolují shyby a plný rozsah tlaků nad hlavou. Před objednávkou si změřte nejen půdorys, ale i výšku místnosti a zohledněte, že osa se při zvedání může nad hlavou dostat výš než samotný rám.</p>'
          + T(['Parametr', 'Co znamená', 'Jak ho zvolit'], [
              ['Nosnost', 'maximální zátěž rámu', 'výrazně nad vaší plánovanou zátěží'],
              ['Profil sloupů', 'tloušťka a průřez trubky', 'silnější pro těžší trénink'],
              ['Rozteč otvorů', 'jak jemně jde měnit výšku', 'menší rozteč znamená přesnější nastavení'],
              ['Hloubka rámu', 'prostor pro dřepy a výpady', 'víc místa pro vyšší lidi'],
              ['Kotvení', 'stabilita rámu', 'do podlahy nebo zatížený na základně']]) +
          '<h2>Multifunkční věže a kladkové stroje</h2>'
          '<p>Posilovací věž sdružuje několik cviků do jedné konstrukce: kladky pro přítahy a stahování, tlaky vleže, motýlek, nohy a někdy i hrazdu. Zátěž tvoří pevné závaží nebo plechové kotouče. Výhodou je kompaktnost a bezpečný průběh pohybu, nevýhodou menší možnost rozšíření a omezená výška nastavení. '
          'Pro rodiny, kde cvičí několik lidí s různou výškou i silou, jde často o praktičtější volbu než volné závaží. Značky Insportline, Body Craft nebo Finnlo mají širokou paletu, od jednoduchých stanic po složité sestavy s několika zásobníky.</p>'
          '<p>Při srovnání věží kontrolujte váhu zásobníku, počet a typ kladek, průměr lan a to, zda kloubový mechanismus nemá vůli. Zásobník v rozsahu desítek kilogramů stačí rekreačnímu cvičenci, silněji trénující jej brzy přeroste. Zásadní je i prostor: věž potřebuje kolem sebe volnou plochu, aby se pohodlně nastoupilo a chodilo okolo.</p>'
          '<h2>Protisměrné kladky a přídavné moduly</h2>'
          '<p>Pokud máte stojan nebo lavici a chcete rozšířit repertoár o přítahy a stahování, často stačí kladka s kabelem. Lze ji upevnit na zeď, ke stropu nebo na rám racku. Protisměrné kladky mají dva kotouče s opačným směrem tahu, takže při tahu jednou rukou jde druhé madlo nahoru, protože zátěž je vedena přes dvě kladky. '
          'Moduly je dobré vybírat s ohledem na průměr kotoučů, protože nepasují vždy. Vedle kladek najdete i madla, trojúhelníkové držáky, trojitý hmat nebo adaptér na přítahy. Jednotlivé madlo se vyplatí zkoušet, zda dobře sedí v ruce.</p>'
          '<h2>Žebřiny, hrazdy a cvičení s vlastní vahou</h2>'
          '<p>Žebřina na stěně nabízí visy, zdvihání kolen, protahování a bezpečný start pro cviky na hrazdě. Benchk a Insportline nabízejí dřevěné i kovové varianty, které se instalují do hmoždinek. Zeď musí unést váhu cvičícího, takže před montáží prověřte, z čeho je vyrobená. '
          'Podrobněji se cvičení s vlastní vahou věnujeme v kategorii <a href="/hrazdy-a-bradla/">hrazdy a bradla</a> a pro funkční trénink nabízí rozšíření <a href="/funkcni-trenink/">funkční trénink</a>.</p>'
          '<h2>Jak vybrat podle cíle</h2>'
          '<ul><li><strong>Nárůst svalů a síly:</strong> stojan, variabilní lavice a sada činek nebo osa s kotouči. Později doplňte kladky.</li>'
          '<li><strong>Tvarování a kondice:</strong> multifunkční věž nebo lavice s kettlebelly, gumami a kardio trenažérem.</li>'
          '<li><strong>Rehabilitace a opatrný start:</strong> stroje s vedenou drahou, malá zátěž a konzultace s fyzioterapeutem.</li>'
          '<li><strong>Cvičení rodiny:</strong> kompaktní věž, která umožní rychlou změnu zátěže bez skládání kotoučů.</li></ul>'
          '<p>Souvisí s tím i doplňky jako <a href="/kettlebelly/">kettlebelly</a>, <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/sportovni-rukavice/">sportovní rukavice</a> a <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>. Lavice a stojan bez zátěže je totiž jen konstrukce.</p>'
          '<h2>Místnost, podlaha a hluk</h2>'
          '<p>Před nákupem zjistěte, kde bude vybavení stát. V paneláku je podstatné snížit přenos nárazů do stropu níže položeného bytu, proto použijte silnou gumovou podložku nebo desku z OSB pokrytou gumovými dlaždicemi. V garáži hlídejte vlhkost, protože ocel na nechráněném betonu rychle koroduje a čalounění může plesnivět. '
          'Ověřte také šířku dveří, protože rozměrný rám se nemusí dostat do suterénu nebo do podkroví. Rozměry balení uvádí obchod u produktu, ověřte si je kvůli dopravě a manipulaci.</p>'
          '<h2>Montáž a bezpečnost</h2>'
          '<p>Většina vybavení se dodává rozebraná a montáž trvá hodiny. Použijte originální šrouby a po prvním týdnu dotáhněte všechny spoje, protože se mohou uvolnit. Zatěžujte postupně a zkontrolujte, že se rám neviklá. '
          'Kotouče na ose zajistěte zámky, a pokud trénujete sami, použijte jistící tyče nebo ramena. Lavice nikdy nepoužívejte nad deklarovanou nosnost. Netrénujte unavení na těžkých sériích bez jištění.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce modelů mají ' + B(('insportline', 'Insportline'), ('hms', 'HMS'), ('marbo', 'Marbo'), ('benchk', 'Benchk'), ('gorilla-sports', 'Gorilla Sports'), ('vifito', 'Vifito'), ('hop-sport', 'Hop-sport'), ('tunturi', 'Tunturi')) + '. '
          'Insportline a HMS pokrývají celý rozsah od jednoduchých lavic po stojany, Marbo je zaměřeno na modulární sestavy a doplňky, Benchk na žebřiny a kompaktní řešení. '
          'Značka sama o sobě nezaručuje kvalitu každého kusu, proto čtěte parametry konstrukce a nosnosti.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Kovové díly občas otřete suchým hadrem, čalounění vlhkým a jemným čisticím prostředkem. Šrouby a svary kontrolujte po několika týdnech a pak jednou za čas. Kladky a vodicí tyče lehce promažte silikonovým olejem, protože při suchém chodu opotřebují lanka. '
          'Lano s viditelným třepením vyměňte, než praskne. Barevný lak se v místech kontaktu s kotouči časem odře, proto na těchto místech chraňte povrch gumovými návleky.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupovat podle počtu cviků v popisu, ne podle stability konstrukce.</li>'
          '<li>Měřit jen půdorys a zapomenout na výšku stropu.</li>'
          '<li>Podcenit nosnost a nekoupit jistící tyče.</li>'
          '<li>Pořídit rozsáhlý stroj, který nahradí jeden cvik a ostatní se nevyužijí.</li>'
          '<li>Ignorovat podlahu a hluk ve vícepodlažním domě.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého výrobku srovnáte nabídky několika obchodů, rozměry i hmotnost zásilky. Využijte filtr podle značky a podívejte se na parametry v popisu. U velkých kusů zjistěte náklady na dopravu a možnost vrácení zboží, které je těžké a nepoddajné. '
          'Před koupí zvažte také, zda se vybavení vejde do dopravního prostoru auta nebo zda bude doručeno na adresu. Pro doplnění programu můžete projít kategorii <a href="/fitness-pomucky/">fitness pomůcky</a> nebo <a href="/sportovni-vyziva/">sportovní výživu</a>.</p>',
    faq=[
        ('Jakou lavici zvolit pro začátek?', 'Nejlépe variabilní s nastavitelným opěradlem a pevnou ocelovou konstrukcí. Nabídne tlaky na rovině i ve sklonu a zůstane užitečná i po přechodu na těžší zátěž. Rovná lavice je levnější varianta, ale omezuje výběr cviků.'),
        ('Jak poznám dostatečnou nosnost lavice?', 'Výrobce uvádí maximální zatížení zpravidla včetně váhy cvičícího. Připočtěte tedy své kilogramy k hmotnosti tyče a kotoučů a nechte rezervu, protože dynamický pohyb zatěžuje konstrukci víc než statická zátěž.'),
        ('Potřebuji power rack, nebo stačí stojany na osu?', 'Pokud pravidelně děláte dřepy a tlaky v těžších sériích sami, power rack s jistícími tyčemi je bezpečnější. Samostatné stojany jsou kompaktnější, ale jištění je omezené a hodí se spíš pro lehčí zátěž nebo cvičení s parťákem.'),
        ('Vejde se posilovací věž do malého pokoje?', 'Záleží na rozměrech. Věže zabírají obvykle plochu několika čtverečních metrů a potřebují volný okraj kolem sebe pro nástup. Rozměry jsou uvedeny u produktu; porovnejte je s půdorysem místnosti i s výškou stropu.'),
        ('Je lepší volné závaží, nebo stroj?', 'Obojí má své místo. Volné závaží rozvíjí koordinaci a nabízí široký výběr cviků, stroje jsou přehlednější a bezpečnější pro samotného cvičence. Pro rodinu a začátečníky bývá vhodnější stroj, pro silový trénink stojan s osou.'),
        ('Jak ochránit podlahu a snížit hluk?', 'Použijte silnou gumovou podložku nebo desku s gumovými dlaždicemi pod celou stojící plochou. Zátěž pokládejte, ne pouštějte, a pod nohy lavic dejte gumové patky. U vícepodlažních domů je dobré myslet i na zvukovou izolaci.'),
        ('Co znamená protisměrná kladka?', 'Jde o systém dvou kladek, kde pohyb jedné ruky zvedá druhou, nebo kladky s opačným směrem tahu. Rozšiřuje možnosti o stahování, přítahy a tricepsové cviky, přičemž se montuje na zeď, strop nebo rám.'),
        ('Jak často kontrolovat šrouby a lana?', 'Po prvním týdnu provozu a pak pravidelně jednou za čas. Při práci s kladkami sledujte i stav lan. Pokud vidíte třepení, lano vyměňte dřív, než praskne.'),
        ('Dá se kombinovat vybavení různých značek?', 'Často ano, ale kontrolujte průměr osy, rozměry sloupů a typ uchycení. Čepy, kotouče a adaptéry nemusí být kompatibilní, proto se před koupí podívejte do technických údajů obou výrobků.'),
        ('Mám se před silovým tréninkem poradit s lékařem?', 'Pokud máte zdravotní potíže, bolesti zad či kloubů, nebo se vracíte po úrazu, poraďte se s lékařem nebo fyzioterapeutem. Obecně platí začínat s menší zátěží a učit se techniku pod dohledem zkušeného cvičence.'),
    ])

# ------------------------------------------------------------------ ostatni-micove-sporty
NEW['ostatni-micove-sporty'] = dict(long=True,
    title='Další míčové sporty: míče, velikosti, povrchy',
    desc='Míče na házenou, ragby, americký fotbal, nohejbal, baseball i dětské a plážové míče. Jak vybrat velikost, povrch a kde porovnat nabídky obchodů.',
    intro='<p>Fotbal, basketbal a volejbal mají své vlastní kategorie, ale školní tělocvična, kemp i zahrada ukrývají mnohem víc míčových her. Házená, nohejbal, ragby, americký fotbal, softbal, dětské skákací míče nebo plážové hry mají svá pravidla, velikosti i materiály. '
          'Tady se hodí rozcestník, který pomůže vybrat správný míč pro konkrétní hru a věk.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u míčů od značek Mondo, Adidas, Merco, Puma, Gala, Kubisport, Kipsta nebo Select, a to včetně pump, sítí a drobného příslušenství. '
          'Hlavní kategorie najdete v přehledech <a href="/micove-sporty/">míčové a raketové sporty</a>, <a href="/fotbalove-mice/">fotbalové míče</a>, <a href="/basketbalove-mice/">basketbalové míče</a> a <a href="/volejbalove-mice/">volejbalové míče</a>. Níže vysvětlujeme, jak rozlišit jednotlivé míče a nekoupit nevhodný.</p>',
    guide='<h2>Jaké míče sem patří</h2>'
          '<p>Kategorie sdružuje míče a vybavení, které nemají vlastní kategorii vedle hlavních míčových her; najdete tu i sálovou kopanou, futsal a licencované míče. Najdete tu míče na házenou, nohejbal, ragby, americký fotbal, baseballové a softbalové míčky, plážové a nafukovací míče, dětské skákací míče, pěnové varianty pro hru v bytě i medicinbaly pro posilování. '
          'Každá hra má jiný tvar, povrch a tlak, takže stejný míč nelze použít všude. Vhodnou volbu usnadní následující přehled.</p>'
          + T(['Hra', 'Tvar míče', 'Na co se zaměřit'], [
              ['Házená', 'kulatý, menší než fotbalový', 'velikost podle věku a pohlaví, lepivý povrch'],
              ['Nohejbal', 'kulatý, podobný fotbalovému', 'mírně měkký povrch, odolnost proti betonu'],
              ['Ragby', 'oválný', 'kroucení při přihrávce, protiskluzový povrch'],
              ['Americký fotbal', 'protáhlý s vyrážkami', 'velikost podle věku, šněrování'],
              ['Baseball a softbal', 'tvrdá koule', 'velikost podle ligy, šití'],
              ['Dětské hry', 'různé, často pěnové', 'bezpečný materiál a velikost k dlaním']]) +
          '<h2>Házená: velikost podle věku a pohlaví</h2>'
          '<p>Házenkářský míč je menší než fotbalový a hráči jej drží jednou rukou. Používají se čtyři základní velikosti 0 až 3: nejmenší (mini) pro nejmladší děti, velikost 1 pro mladší děti, velikost 2 pro ženy a starší žáky a velikost 3 pro muže; podrobnosti najdete v kategorii <a href="/hazena/">házená</a>. Zjednodušeně: děti začínají na menších a lehčích míčích, ženy a starší dívky používají střední velikost a muži největší. '
          'Přesné rozměry a hmotnost uvádí pravidla federace a produktový popis. Povrch bývá kožený nebo syntetický, někdy s pryskyřicí. Pryskyřice dobře drží v dlani, ale vyžaduje úklid hřiště, protože ulpívá na podlaze. Pro školní tělocvik a rekreaci se dobře hodí míče bez pryskyřice, které jsou tolerantnější.</p>'
          '<p>Navazuje <a href="/hazena/">házená</a> jako samostatná kategorie, kde se věnujeme i brankářské výbavě a obuvi.</p>'
          '<h2>Nohejbal a podobné hry bez rukou</h2>'
          '<p>Nohejbalový míč se vzhledem blíží fotbalovému, ale má jiný povrch a konstrukci a snáší hru na tvrdém podkladu. Hraje se přes síť a míč se odráží ne rukou, ale nohou, hlavou či tělem. Při volbě se hledí na povrch, vnitřní komoru a odolnost šití. '
          'Pro volný čas a pro hry na písku stačí odolnější syntetický míč, soutěžní hráči si vyberou schválený model. Sedco a Select mají v nabídce míče s označením nohejbal, které můžete porovnat podle parametrů.</p>'
          '<h2>Ragby a americký fotbal</h2>'
          '<p>Oválný míč má dvě hlavní skupiny. Ragbyový míč je kratší a obvykle silnější v profilu a drží se oběma rukama, míč pro americký fotbal je užší, zašpičatělejší a opatřený vyvýšenými body a šněrováním pro lepší úchop při házení. '
          'Obě varianty se vyrábějí v několika velikostech od dětských po standardní. Kupujte podle věku a ligy, protože příliš velký míč se špatně chytá. Pro tréninky rozdílné techniky se hodí tvrdší kožený povrch, pro děti a hru venku syntetika.</p>'
          '<p>Hry mají i vlastní kategorii, v níž najdete příslušnou výbavu: <a href="/ragby-a-americky-fotbal/">ragby a americký fotbal</a>. Najdete tam také chrániče a dresy, které sem nepatří.</p>'
          '<h2>Baseball, softbal a související hry</h2>'
          '<p>Baseballový míček je pevná koule s jádrem z korku nebo pryže, obtočená nití a potažená kůží. Softbalový je větší a měkčí, ale stále tvrdší než běžný míč. Při nákupu rozlišujte velikost míčku, protože hra softbal se hraje se zvětšeným průměrem. '
          'Další výbavu popisuje kategorie <a href="/baseball-a-softball/">baseball a softbal</a>. Při tréninku s dětmi používejte měkčí gumové míčky, které snižují riziko zranění.</p>'
          '<h2>Plážové, nafukovací a dětské míče</h2>'
          '<p>Plážové míče bývají z lehké PVC fólie, jsou barevné a hodí se k vodě. K volejbalu na pláži se ale nehodí: potřebujete pevnější míč, který snese tlak a písek. Nafukovací míče a míče s ušima nebo madlem slouží jako hračka pro nejmenší. '
          'Pěnové míče jsou měkké a tiché, hodí se do bytu a do skupin s menšími dětmi. Při výběru sledujte označení bezpečnosti a materiál, aby neobsahoval škodlivé látky a při kousání nepraskal. Rozšíření pro letní sezónu najdete v kategoriích <a href="/plazove-doplnky/">plážové doplňky</a> a <a href="/nafukovaci-hracky/">nafukovací hračky</a>.</p>'
          '<h2>Medicinbaly a těžké míče</h2>'
          '<p>Medicinbal je těžký míč na posilování, rotace a vrhy. Existují odrazové varianty z gumy a měkké z pevného textilu s náplní, které se neodrážejí a hodí se pro cvičení s partnerem nebo o zeď. Hmotnost zvolte tak, aby technika zůstala čistá, tedy spíš lehčí než těžší. '
          'Cvičení s míčem dobře doplňuje <a href="/funkcni-trenink/">funkční trénink</a>, <a href="/balancni-pomucky/">balanční pomůcky</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>.</p>'
          '<h2>Materiály povrchu a konstrukce</h2>'
          '<ul><li><strong>Přírodní kůže:</strong> příjemný úchop, ale vyšší nároky na péči a citlivost na vlhkost.</li>'
          '<li><strong>Syntetika (PU a PVC):</strong> odolná, snáší venku i písek, často levnější než kůže.</li>'
          '<li><strong>Guma:</strong> běžná u míčů pro venek a školní tělocvik, vydrží i beton.</li>'
          '<li><strong>Pěna:</strong> měkká, bezpečná, vhodná pro malé děti a hru v interiéru.</li>'
          '<li><strong>Lepený nebo šitý povrch:</strong> šití bývá odolnější, lepené spoje nabízejí hladší chování ve vzduchu.</li></ul>'
          '<h2>Vnitřní komora, ventilek a tlak</h2>'
          '<p>Většina míčů má vnitřní komoru z butylu nebo latexu. Butyl drží vzduch déle, latex má lepší odezvu, ale vyžaduje častější dofukování. Ventilek se zapíchne jehlou, kterou je třeba před použitím navlhčit, aby se nepoškodil. '
          'Tlak má výrobce vyznačený u ventilku nebo v popisu a jeho dodržování je podstatné: přefouknutý míč se odráží příliš a hůř se ovládá, podfouknutý je těžký a nepřesný. Pumpičku a jehly najdete v příslušenství, kterým se zabýváme níže.</p>'
          '<h2>Příslušenství: pumpy, sítě a tašky</h2>'
          '<p>K míčům se hodí pumpa s tlakoměrem, sada jehel a síť nebo vak na přenášení. Pumpa s tlakoměrem pomáhá držet tlak v doporučeném rozmezí, síť přemístí několik míčů najednou. '
          'Pro kluby a školy jsou vhodné tašky s kapacitou na desítky míčů, pro individuální použití stačí vak na jeden až dva. Přepravní řešení najdete v kategorii <a href="/sportovni-tasky/">sportovní tašky</a>. '
          'Pokud se vám míč poškodí, někdy lze vyměnit vnitřní komoru nebo zalepit povrch, ale u levnějších kusů se oprava nevyplatí.</p>'
          '<h2>Povrch hřiště a obuv</h2>'
          '<p>Pro tvrdý povrch, jako je asfalt nebo beton, vybírejte míč z odolné gumy nebo syntetiky, na trávě vyniknou kvalitnější materiály a v hale kůže nebo kompozit. Velký vliv má i obuv: tělocvična vyžaduje halovou podrážku, venku se hodí kopačky nebo tenisky s dobrým záběrem. '
          'Příklady obuvi najdete v kategoriích <a href="/salova-obuv/">sálová obuv</a>, <a href="/kopacky/">kopačky</a> a <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
          '<h2>Jak vybrat podle věku</h2>'
          '<ul><li><strong>Batolata a předškoláci:</strong> měkké pěnové nebo nafukovací míče, které nebolí a nejsou těžké.</li>'
          '<li><strong>Školáci:</strong> menší a lehčí varianta oficiálního míče, aby se učili správnou techniku.</li>'
          '<li><strong>Mládež:</strong> míč o velikosti odpovídající soutěži, kterou hrají.</li>'
          '<li><strong>Dospělí:</strong> standardní velikost podle pravidel hry, případně levnější trénink a oficiální soutěžní model pro zápasy.</li></ul>'
          '<h2>Péče o míče a skladování</h2>'
          '<p>Míče po hře otřete vlhkým hadříkem, ne rozpouštědlem. Kůži občas ošetřete přípravkem určeným na kůži. Míče neskladujte na slunci a u topení, protože se mění tlak a materiál stárne. '
          'Při delším skladování mírně snižte tlak, aby se šití nenamáhalo. Mokrý míč nechte vyschnout při pokojové teplotě. Písek a bláto odstraňte, než zaschnou, protože drobné částice drhnou povrch.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nabídku tvoří zejména ' + B(('mondo', 'Mondo'), ('adidas', 'Adidas'), ('merco', 'Merco'), ('puma', 'Puma'), ('gala', 'Gala'), ('kubisport', 'Kubisport'), ('kipsta', 'Kipsta'), ('select', 'Select'), ('nike', 'Nike')) + '. '
          'Mondo a Gala jsou časté u dětských a školních míčů, Select se objevuje u házené a fotbalové ligy, Adidas, Puma a Nike u fotbalových a trénování. Kipsta a Merco nabízejí cenově dostupné míče pro volný čas. '
          'V katalogu se objevují také licencované míče, například sběratelské a replikové míče, které slouží spíš jako suvenýr než jako zápasový výrobek.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Kupovat míč podle obrázku a ne podle velikosti, kterou hra předepisuje.</li>'
          '<li>Považovat replikový míč za zápasový: liší se materiálem i odezvou.</li>'
          '<li>Použít plážový PVC míč na tvrdé hřiště.</li>'
          '<li>Zapomenout na pumpu a jehly, takže míč nelze správně nahustit.</li>'
          '<li>Skladovat míč napuštěný na maximum u topení.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého míče vidíte nabídky více obchodů, popis a parametry. Využijte filtr podle značky a sledujte označení velikosti, které bývá v názvu. Pokud nakupujete do školy nebo klubu, zjistěte možnost množstevního nákupu u obchodu a zvažte i tašky na míče. '
          'Další hry najdete v kategoriích <a href="/padel/">padel</a>, <a href="/squash/">squash</a>, <a href="/badminton/">badminton</a> a <a href="/stolni-tenis/">stolní tenis</a>.</p>',
    faq=[
        ('Jakou velikost míče na házenou zvolit pro dítě?', 'Pro nejmladší děti se používají nejmenší a nejlehčí míče, pro starší žactvo střední velikost a pro dospělé muže největší. Přesné rozměry podle věkové kategorie uvádí pravidla federace a popis produktu.'),
        ('Čím se liší ragbyový míč od míče na americký fotbal?', 'Ragbyový míč je kratší a boubelatější, americký je užší a špičatější a má vyvýšené body pro úchop. Obě varianty mají oválný tvar, ale jejich konstrukce odpovídá odlišnému stylu hry.'),
        ('Dá se nohejbal hrát s fotbalovým míčem?', 'Rekreačně ano. Zápasový nohejbalový míč má ale odlišnou konstrukci a povrch, který lépe snáší hru na tvrdém podkladu. Pokud hrajete pravidelně, vyplatí se pořídit míč určený pro nohejbal.'),
        ('Proč se házenkářské míče lepí?', 'Některé soutěžní míče mají povrch ošetřený pryskyřicí pro jistější úchop. Ta se ale lepí na podlahu a vyžaduje čištění. Pro školu a rekreaci se hodí míče bez pryskyřice.'),
        ('Jaký tlak mám v míči udržovat?', 'Doporučené rozmezí uvádí výrobce na míči nebo v popisu. Nižší tlak dělá míč těžký a nepřesný, vyšší tvrdý a nezvladatelný. Pro kontrolu je vhodná pumpa s tlakoměrem.'),
        ('Je plážový míč vhodný na volejbal?', 'Ne. Plážový míč z tenké fólie je určený na hru u vody. Na volejbal potřebujete pevný míč určený pro hru na písku nebo v hale, který snese údery a písek.'),
        ('Jak vybrat míč pro malé dítě?', 'Hledejte měkký pěnový nebo nafukovací míč v rozměru, který dítěti sedí v dlaních. Zkontrolujte označení bezpečnosti a materiál. Nejmenším dětem raději nedávejte tvrdé míče, které mohou bolet.'),
        ('Jak dlouho míč vydrží?', 'Záleží na materiálu, četnosti hraní a povrchu. Syntetický míč používaný na asfaltu se opotřebuje dřív než kožený v hale. Pravidelná kontrola tlaku, čištění a správné skladování životnost prodlužují.'),
        ('Mohu míč opravit, když přestane držet vzduch?', 'Pokud uniká vzduch ventilkem, někdy pomůže vyměnit ventil nebo vnitřní komoru. Prasklinu v povrchu zpravidla nelze opravit spolehlivě. U levných kusů se oprava často nevyplatí.'),
        ('K čemu slouží medicinbal?', 'Je to těžký míč na posilování, rotace, hody a cvičení s partnerem. Hmotnost se volí tak, aby zůstala správná technika. Při zdravotních potížích se před cvičením poraďte s lékařem nebo fyzioterapeutem.'),
    ])
