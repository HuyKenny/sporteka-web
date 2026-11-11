"""sporteka.cz — wave 25c (11. 11. 2026): long texts for ashwagandha, ponozkoboty, posilovaci-lavice.
General true facts only, no prices. Brands verified in the live catalogue sample."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ ashwagandha
NEW['ashwagandha'] = dict(long=True,
    title='Ashwagandha: kapsle, extrakt KSM-66 a prášek v přehledu',
    desc='Ashwagandha v kapslích, prášku i gumících. Jak číst etiketu, rozlišit KSM-66 a Shoden, kdy být opatrný a jak porovnat nabídky českých obchodů.',
    intro='<p>Ashwagandha, česky též vitánie snodárná nebo indický ženšen, je keřovitá rostlina z čeledi lilkovitých, jejíž kořen se v ájurvédě používá po staletí. Dnes ji najdete jako doplněk stravy v kapslích, tabletách, prášku, kapkách i žvýkacích gumících. Sporteka porovnává nabídky českých obchodů, takže vedle sebe uvidíte standardizované extrakty, čisté kořenové prášky i kombinované přípravky.</p>'
          '<p>Tahle stránka vám pomůže zorientovat se v označeních, jako jsou KSM-66, Shoden nebo procento withanolidů, a v rozdílech mezi formami. Nenajdete tu slibované zázraky: doplněk stravy nenahrazuje pestrou stravu, spánek ani péči lékaře. V nabídce jsou značky ' + B(('gymbeam', 'GymBeam'), ('blendea', 'Blendea'), ('olaola', 'OlaOla'), ('ostrovit', 'OstroVit'), ('atp-nutrition', 'ATP Nutrition'), ('nutriworks', 'NutriWorks')) + '. Širší výběr najdete v nadřazené kategorii <a href="/ostatni-doplnky-stravy/">další doplňky stravy</a>.</p>',
    guide='<h2>Co je ashwagandha a z čeho se vyrábí</h2>'
          '<p>Latinsky se rostlina jmenuje Withania somnifera. V doplňcích se využívá hlavně kořen, někdy také list. Kořen se suší a mele na prášek, nebo se z něj vyrábí extrakt, tedy koncentrovanější látka získaná rozpouštědlem a následně vysušená. Aktivními složkami se obvykle míní withanolidy, skupina přírodních sloučenin, podle jejichž podílu se extrakty odlišují.</p>'
          '<p>Slovo adaptogen se v marketingu používá pro rostliny, které se tradičně spojují s odolností vůči zátěži. Jde o obecné označení, ne o schválené zdravotní tvrzení. Výrobci u doplňků stravy nesmějí slibovat léčbu nebo prevenci nemocí a při čtení popisů je dobré si tohle pravidlo pamatovat.</p>'
          '<h2>Ashwagandha KSM-66, Shoden a další názvy</h2>'
          '<p>Na obalech se často objevují zkratky a ochranné známky. Nejde o odlišné rostliny, ale o označení konkrétního způsobu zpracování. Chcete-li přípravky srovnávat, je třeba vědět, co která značka znamená.</p>'
          + T(['Označení', 'Co to obvykle znamená', 'Na co se zaměřit'], [
              ['KSM-66', 'patentovaný extrakt z kořene, vyráběný bez alkoholu', 'obsah extraktu v jedné kapsli, nikoli jen celkové množství kořene'],
              ['Shoden', 'extrakt standardizovaný na vyšší podíl withanolidů', 'uvedené procento a dávka na porci'],
              ['Extrakt 10:1', 'poměr, kolik rostlinné suroviny padlo na jednotku extraktu', 'poměr sám o obsahu aktivních látek nic neříká'],
              ['10 % withanolidů', 'standardizace na podíl účinných látek', 'zda výrobce uvádí metodu a dávku na kapsli'],
              ['Kořenový prášek', 'pouze usušený a rozemletý kořen', 'čistota, původ a případné bio osvědčení'],
              ['Bio', 'surovina z ekologického zemědělství', 'logo kontrolní organizace na obalu']]) +
          '<p>Platí, že větší číslo neznamená automaticky lepší produkt. Srovnávejte dávku jedné porce, počet porcí v balení a to, zda je uvedeno, jaká část z celkové hmotnosti kapsle je skutečně extrakt.</p>'
          '<h2>Kapsle, prášek, gummies a kapky</h2>'
          '<p>Forma určuje, jak se doplněk dávkuje, jak chutná a jak se skladuje. Pro většinu lidí je nejpohodlnější kapsle, ale ostatní formy mají své místo.</p>'
          '<ul><li><strong>Kapsle a tobolky:</strong> přesná dávka, bez chuti, snadno se berou na cesty. Rostlinné kapsle jsou vhodné pro vegany.</li>'
          '<li><strong>Tablety:</strong> bývají levnější na výrobu, ale obsahují více pomocných látek.</li>'
          '<li><strong>Prášek:</strong> dá se míchat do smoothie, ovesné kaše nebo teplého nápoje. Chuť je výrazně hořká až zemitá, proto ji řada lidí zamaskuje ovocem či kakaem.</li>'
          '<li><strong>Gummies:</strong> žvýkací bonbony s příchutí, snadné na užívání, ale často obsahují cukr nebo sladidla a nižší dávku účinné složky.</li>'
          '<li><strong>Kapky a tinktury:</strong> tekutý výtažek, dávkuje se pipetou. Bývá v něm alkohol nebo glycerin.</li>'
          '<li><strong>Kombinované přípravky:</strong> ashwagandha spolu s vitamíny, tryptofanem, šilajitem nebo kakaem. Při srovnání zkontrolujte, kolik ashwagandhy v nich skutečně je.</li></ul>'
          '<h2>Jak číst etiketu</h2>'
          '<p>Na zadní straně obalu hledejte tabulku s dávkou na porci. Dobrý výrobce uvede, kolik miligramů kořene nebo extraktu obsahuje jedna kapsle, kolik kapslí tvoří doporučenou denní porci a z jakého druhu extraktu pochází. Podezřelé jsou obecné formulace bez čísel, například pouhé slovo „komplex“.</p>'
          '<ul><li>Doporučená denní dávka je stanovena výrobcem a nemá se překračovat.</li>'
          '<li>Seznam složek řadí látky od největšího podílu k nejmenšímu. Pokud jsou na začátku plnidla, extraktu je málo.</li>'
          '<li>Upozornění pro těhotné, kojící a lidi se zdravotními potížemi je povinnou součástí etikety.</li>'
          '<li>Číslo šarže a datum minimální trvanlivosti usnadní případnou reklamaci.</li></ul>'
          '<h2>Pro koho je ashwagandha a pro koho není</h2>'
          '<p>Doplněk si pořizují lidé, kteří se zajímají o rostlinné přípravky v rámci aktivního životního stylu, sportovci, kteří zařazují adaptogeny k pestré výživě, i ti, kdo si chtějí zpestřit večerní rutinu. Žádný přípravek ale není nutný a rozhodně nenahrazuje dostatek spánku, pravidelný pohyb a odpočinek.</p>'
          '<p>Opatrnost je na místě u těhotných a kojících žen, dětí, lidí se štítnou žlázou, autoimunitním onemocněním nebo při užívání léků, zejména na uklidnění, snížení tlaku či cukru. U ashwagandhy se také opakovaně upozorňuje na poruchy jater. Před zahájením užívání proto konzultujte s lékařem nebo lékárníkem, nejlépe ještě před objednávkou.</p>'
          '<h2>Jak začít a jak dlouho užívat</h2>'
          '<p>Rozumný postup je začít nejnižší dávkou doporučenou výrobcem a sledovat, jak tělo reaguje. Nové přípravky nezačínejte kombinovat všechny najednou, jinak nepoznáte, který z nich způsobil případné potíže, třeba žaludeční nevolnost. Mnoho výrobců doporučuje užívat po jídle, aby se omezilo podráždění trávicího traktu, a rozdělit dávku na dopoledne a večer.</p>'
          '<p>Délku užívání určete podle pokynů na obalu, případně podle poradenství lékaře. Dlouhodobé nepřetržité užívání bez přestávky se u rostlinných doplňků obvykle nedoporučuje a řada výrobců nabízí cyklování, tedy střídání období užívání a pauzy. Přípravek, po kterém se objeví vyrážka, silná únava, bolest břicha nebo jiné neobvyklé příznaky, přestaňte brát a vyhledejte lékaře.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Porovnávání jen podle ceny za balení:</strong> kapsle mají různou dávku, takže se vyplatí srovnat cenu za jednu porci obsahující účinnou složku.</li>'
          '<li><strong>Slepé spoléhání na ochrannou známku:</strong> název KSM-66 sám o sobě nezaručí kvalitu celého produktu, rozhoduje i dávka a čistota.</li>'
          '<li><strong>Kombinace s dalšími rostlinami bez ověření:</strong> směsi adaptogenů mohou obsahovat látky, které si s vašimi léky nerozumí.</li>'
          '<li><strong>Nákup z neověřených zdrojů:</strong> doplněk bez českých údajů na obalu nebo bez kontaktu na distributora je rizikový.</li>'
          '<li><strong>Očekávání rychlého efektu:</strong> rostlinné přípravky nejsou léky a výrobci jejich účinek popisují jako dlouhodobější, bez záruky.</li></ul>'
          '<h2>Čistota, původ a ověření</h2>'
          '<p>Kořeny rostou převážně v Indii, takže se doplněk dováží. U rostlinných surovin se může objevit problém s kovy nebo pesticidy, proto je dobré dát přednost produktům, jejichž výrobce uvádí zkoušky čistoty nebo osvědčení bio. Bio logo na obalu znamená, že surovina pochází z kontrolovaného ekologického zemědělství, ale samo o sobě nepotvrzuje vyšší obsah účinných látek. Doplňky prodávané v Evropské unii musí splňovat pravidla pro potraviny a být oznámené příslušnému úřadu, kontakt na výrobce proto na obalu nechybí.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Kapsle i prášek uchovávejte v původním uzavřeném obalu na suchém a chladném místě, mimo dosah dětí a přímého slunce. Vlhkost je největším nepřítelem prášku, protože ho slepí a urychlí kažení. Po otevření dóz s práškem se vyplatí spotřebovat obsah v rozumné lhůtě, kterou udává výrobce. Gummies teplo tají a lepí se, takže je nenechávejte v autě. Kapky s alkoholem dobře těsněte a lahvičku po otevření uchovávejte podle pokynů na štítku.</p>'
          '<h2>Značky ashwagandhy na Sportece</h2>'
          '<p>V nabídce najdete sportovní značky s širokým portfoliem, například ' + B(('gymbeam', 'GymBeam'), ('ostrovit', 'OstroVit'), ('atp-nutrition', 'ATP Nutrition'), ('nutriworks', 'NutriWorks')) + ', ale také specializované výrobce bylinných doplňků jako ' + B(('blendea', 'Blendea'), ('olaola', 'OlaOla'), ('movit', 'MOVit')) + '. Sportovní značky obvykle nabízejí standardizované extrakty v kapslích, bylinní výrobci spíše bio kořenový prášek nebo čisté kapsle. Žádný z typů není automaticky lepší, záleží na vašem záměru a na čitelné etiketě.</p>'
          '<h2>Jak ashwagandha zapadá do výživy sportovce</h2>'
          '<p>Základem výkonu zůstává dostatek energie, bílkovin, tekutin a spánku. Doplňky jsou až poslední doplněk skládačky. Pokud řešíte konkrétní nedostatek, projděte nejdřív přehled <a href="/vitaminy-a-mineraly/">vitamínů a minerálů</a>, třeba <a href="/horcik/">hořčík</a> nebo <a href="/omega-3/">omega-3</a>. Svalový růst podporují spíše ověřené základy jako <a href="/proteiny/">proteiny</a> a <a href="/kreatin/">kreatin</a>. Kloubům se věnuje kategorie <a href="/kolagen-a-klouby/">kolagen a kloubní výživa</a>.</p>'
          '<p>Pozor na kombinace se stimulanty z <a href="/predtreninkove-boostery/">předtréninkových boosterů</a>. Pokud máte pochybnosti o vzájemném působení látek, zeptejte se lékaře nebo lékárníka, než přípravky spojíte. Obecně platí pravidlo nepřidávat několik nových doplňků současně.</p>'
          '<h2>Jak porovnat ashwagandhu na Sportece</h2>'
          '<p>Sporteka nevyrábí ani neprodává vlastní zboží, jen sbírá nabídky českých obchodů. Postupujte takto: vyberte formu, která vám vyhovuje, porovnejte dávku extraktu na jednu porci a počet porcí v balení, přečtěte si složení a upozornění, a teprve potom srovnejte cenu u různých prodejců. Zohledněte také dopravu a možnost vrácení. Při opakovaných nákupech se vyplatí větší balení, pokud ho stihnete spotřebovat před koncem trvanlivosti. Další přípravky z oblasti zdraví hledejte v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>.</p>',
    faq=[
        ('Co je ashwagandha?', 'Je to rostlina Withania somnifera, také zvaná vitánie snodárná nebo indický ženšen. V doplňcích stravy se využívá hlavně její kořen ve formě prášku nebo extraktu.'),
        ('Co znamená KSM-66 u ashwagandhy?', 'Je to ochranná známka patentovaného extraktu z kořene. Označuje způsob zpracování, ale kvalitu celého výrobku určuje také dávka, čistota a složení.'),
        ('Jaký je rozdíl mezi práškem a kapslemi?', 'Kapsle mají přesnou dávku a bez chuti, prášek je hořký, ale umožňuje volné dávkování a míchání do jídla nebo nápojů. Zvolte podle toho, co vám vyhovuje v každodenním režimu.'),
        ('Kolik withanolidů má doplněk obsahovat?', 'Podíl se liší podle extraktu, často se uvádí kolem pěti až deseti procent. Důležitější než samotné číslo je dávka na porci a transparentní informace výrobce.'),
        ('Kdy ashwagandhu užívat?', 'Řiďte se pokyny na obalu. Mnoho výrobců doporučuje užívat po jídle, aby se zmírnilo podráždění žaludku, a dávku případně rozdělit na dvě části během dne.'),
        ('Kdo by ashwagandhu užívat neměl?', 'Těhotné a kojící ženy, děti a lidé s onemocněním štítné žlázy, jater nebo autoimunitními potížemi. Opatrnost platí i při užívání léků. Vždy se předem poraďte s lékařem nebo lékárníkem.'),
        ('Jaké nežádoucí účinky se mohou objevit?', 'Mohou se objevit žaludeční nevolnost, průjem nebo ospalost. Při jakékoli neobvyklé reakci užívání ukončete a vyhledejte lékaře.'),
        ('Dá se ashwagandha kombinovat s jinými doplňky?', 'Obecně ano, ale nepřidávejte několik novinek najednou a hlídejte celkovou dávku podobných rostlin. Při užívání léků se nejdřív poraďte s odborníkem.'),
        ('Jak dlouho ashwagandhu užívat?', 'Délku určuje výrobce na obalu. Dlouhodobé nepřetržité užívání se u rostlinných přípravků obvykle nedoporučuje, proto se v praxi střídá užívání s pauzou.'),
        ('Je ashwagandha doping?', 'Rostlina sama není zařazena mezi zakázané látky, ale u kombinovaných přípravků se mohou objevit jiné složky. Soutěžní sportovci by měli kontrolovat složení a řídit se pravidly své federace.'),
        ('Jak poznat kvalitní ashwagandhu?', 'Hledejte uvedenou dávku extraktu, typ extraktu, původ, českou etiketu s kontaktem na distributora a případně bio osvědčení nebo výsledky laboratorních zkoušek.'),
    ])

# ------------------------------------------------------------------ ponozkoboty
NEW['ponozkoboty'] = dict(long=True,
    title='Ponožkoboty: barefoot obuv do vody, na běh i na doma',
    desc='Ponožkoboty jsou ohebné barefoot boty s tenkou podrážkou. Jak vybrat velikost, materiál a použití pro dospělé i děti a porovnat nabídky obchodů.',
    intro='<p>Ponožkoboty jsou lehká obuv, která se přimyká k noze jako silnější ponožka, ale má pevnější podrážku a chrání chodidlo před zemí. Nohu nestahují a nezvedají patu, takže se v nich chodí podobně jako naboso. Jsou oblíbené na cvičení, na procházky, do města v létě, na vodu i jako přezuvky na cestování, protože se dají sbalit do malé kapsy.</p>'
          '<p>Sporteka sleduje nabídky českých obchodů, kde dominuje česká značka Skinners, a doplňuje ji prstová obuv značky Vibram. Na této stránce se dozvíte, čím se ponožkoboty liší od klasických barefoot bot, jak vybrat správnou velikost a kdy se hodí dětské provedení. Další modely hledejte v nadřazené kategorii <a href="/barefoot-obuv/">barefoot boty</a>. Značky: ' + B(('skinners', 'Skinners'), ('vibram', 'Vibram')) + '.</p>',
    guide='<h2>Co jsou ponožkoboty</h2>'
          '<p>Slovo ponožkoboty označuje obuv, jejíž svršek je z pružné elastické pleteniny, připomínající ponožku. Na rozdíl od běžné boty nemá pevnou špičku, tvrdou patu ani tuhou stélku. Podrážka je tenká, ohebná a bez rozdílu výšky mezi patou a špičkou. Díky tomu se chodidlo může přirozeně ohýbat, roztahovat prsty a vnímat povrch pod sebou.</p>'
          '<p>Z hlediska zařazení patří ponožkoboty mezi barefoot obuv, ale představují její nejminimalističtější variantu. Klasické barefoot tenisky, které v nabídce rovněž uvidíte, mají pevnější svršek a více vrstev, zatímco ponožkoboty vsázejí na nízkou váhu a skladnost.</p>'
          '<h2>Jak se liší od barefoot tenisek a bot</h2>'
          + T(['Vlastnost', 'Ponožkoboty', 'Barefoot tenisky a boty'], [
              ['Svršek', 'elastická pletenina', 'textil, kůže nebo syntetika s pevnější konstrukcí'],
              ['Podrážka', 'velmi tenká, ohebná', 'tenká, ale často s výraznějším vzorkem'],
              ['Váha a skladnost', 'nízká váha, sbalí se do malé kapsy', 'těžší, objemnější'],
              ['Ochrana nohy', 'základní, před drobnými nerovnostmi', 'vyšší, hodí se i do chladu a na špinavý terén'],
              ['Použití', 'léto, cvičení, voda, cestování, domov', 'městská chůze, celoroční nošení'],
              ['Přizpůsobení tvaru nohy', 'pletenina se přizpůsobí tvaru chodidla', 'záleží na střihu a šířce špičky']]) +
          '<h2>Pro koho jsou ponožkoboty vhodné</h2>'
          '<p>Hodí se lidem, kteří chtějí vyzkoušet barefoot styl bez velké investice do plné zimní boty, a těm, kdo hledají letní obuv do horka. Používají je cvičenci v posilovně nebo na jógu, rodiny na dovolené, děti ve školce i ve škole a lidé, kteří potřebují lehkou obuv do batohu. Hodí se také jako druhý pár na cesty, kdy nechcete nosit těžké boty.</p>'
          '<p>Naopak pro dlouhé túry v kamenitém terénu, pro zimu nebo do deště nejsou ideální, protože podrážka je tenká a svršek bývá prodyšný, ne nepromokavý. Takové situace řeší spíš <a href="/trekova-obuv/">trekové boty</a> nebo <a href="/zimni-obuv/">zimní boty</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Správná velikost je u této obuvi klíčová. Elastický materiál zdánlivě odpouští chyby, ale příliš krátká bota tlačí na prsty a příliš velká se při chůzi sune. Postup je jednoduchý.</p>'
          '<ol><li>Postavte se bosou nohou na papír a obkreslete ji nebo označte nejdelší bod prstů a patu.</li>'
          '<li>Změřte vzdálenost v milimetrech a porovnejte ji s tabulkou výrobce, ne s číslem, které nosíte u jiných značek.</li>'
          '<li>K naměřené délce připočtěte několik milimetrů volného místa před prsty, aby se mohly roztáhnout.</li>'
          '<li>Měřte večer, kdy je noha mírně oteklá, a lépe obě nohy, protože se často liší.</li></ol>'
          '<p>U dětí počítejte s růstem, ale příliš velká bota znamená klopýtání. Velikosti se u jednotlivých řad Skinners liší podle střihu, proto vždy otevřete tabulku u konkrétního modelu. Ponožkoboty s vyšším elastickým svrškem snesou o něco větší toleranci, u prstových modelů Vibram ovšem musí každý prst sedět ve své kapse.</p>'
          '<h2>Skinners Comfort, Compression a Kids line</h2>'
          '<p>V nabídce se opakují tři řady. Označení se mohou zdát podobná, proto je shrnuji v jednom místě.</p>'
          '<ul><li><strong>Comfort:</strong> základní model pro každodenní nošení, jemný vnitřek a ohebná podrážka.</li>'
          '<li><strong>Compression:</strong> pevnější střih s větším přilnutím k noze, vhodný pro ty, kteří preferují sevřenější pocit.</li>'
          '<li><strong>Kids line:</strong> dětská řada v menších velikostech, často v barevných variantách.</li></ul>'
          '<p>Přesné vlastnosti a rozdíly mezi řadami vždy ověřte v popisu u daného obchodu, protože výrobce je upravuje mezi generacemi, například označením 2.0.</p>'
          '<h2>Prstové boty Vibram</h2>'
          '<p>Vibram vyrábí obuv se samostatnou přihrádkou pro každý prst. Podrážku z gumy Vibram znají turisté z horských bot, v prstovém provedení slouží hlavně k cvičení, na vodu a pro rychlé procházky. Prstová obuv má pocit podobný chůzi naboso a prsty se nemohou o sebe třít, ale navlékání chvíli trvá a nemusí vyhovovat každému tvaru nohy. Dospělým se doporučuje začít krátkými úseky.</p>'
          '<h2>Přechod na ponožkoboty</h2>'
          '<p>Pokud jste nosili klasickou tlumenou obuv, svaly chodidla a lýtek jsou zvyklé na oporu. Při náhlém přechodu na minimalistickou botu se mohou objevit bolesti chodidel, pat nebo lýtek. Postupujte pomalu: začněte hodinou denně, na rovném povrchu, a dobu postupně prodlužujte. Při cvičení je střídejte s dosavadní obuví postupně, ne celou rutinu najednou. Přečtěte si i rady v kategorii barefoot obuv a při jakýchkoli zdravotních potížích nohou, plochonoží nebo po úrazu se poraďte s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Na co používat: cvičení, voda, město</h2>'
          '<ul><li><strong>Fitness a jóga:</strong> nízká podrážka a ohebnost dávají dobrý kontakt s podlahou. Na těžké mrtvé tahy je stabilní plochá obuv žádaná, ale zkontrolujte, zda se podrážka nepropíná. Pro silové boty se podívejte i do kategorie <a href="/treninkova-obuv/">fitness a tréninková obuv</a>.</li>'
          '<li><strong>Voda:</strong> pletenina schne rychle, ale nenahrazuje obuv se speciálním odvodem vody. Pokud chodíte po kamenitém břehu, zvažte <a href="/obuv-do-vody/">boty do vody</a>.</li>'
          '<li><strong>Chůze a město:</strong> v teple dobře vzdušné, v chladu a dešti ne. Výběr na každý den najdete mezi <a href="/tenisky/">teniskami a volnočasovou obuví</a>.</li>'
          '<li><strong>Běh:</strong> mnoho lidí bosou techniku zkouší, ale začátečníci by měli zvyšovat vzdálenost velmi pozvolna. Běžecké modely najdete v kategorii <a href="/bezecka-obuv/">běžecké boty</a>.</li>'
          '<li><strong>Cestování:</strong> váha je minimální, dvojice se vejde do příručního zavazadla.</li></ul>'
          '<h2>Materiály a konstrukce</h2>'
          '<p>Svršek bývá z umělých vláken, nejčastěji z polyesteru a elastanu, které jsou pružné a rychle schnou. Podrážka je pryžová, často s jednoduchým vzorem pro přilnavost. Některé modely mají textilní vnitřek bez švů, který je příjemný na kůži i bez ponožky. U každého výrobce se mění složení, takže si přečtěte tabulku parametrů.</p>'
          '<p>Důležitá je prodyšnost a stejně tak ochrana před drobnými kameny. Tenká podrážka nechrání před ostrými předměty, proto si při chůzi po štěrku dávejte pozor. Stélka je buď vlepená, nebo vyjímatelná, a u některých modelů ji lze nahradit tenkou vložkou, pokud potřebujete větší komfort. Doplňky najdete v kategorii <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Většinu ponožkobot lze prát ručně v lehce teplé vodě s jemným prostředkem, u některých výrobců i v pračce na šetrný program. Řiďte se štítkem. Sušte je volně na vzduchu, nikdy na topení ani na přímém slunci, protože teplo poškozuje lepení podrážky. Po vodě nebo potu je dobře vysušte a vyvětrejte, jinak vzniká zápach. Životnost závisí na terénu: tenká podrážka se na asfaltu obrušuje rychleji než tlustá, takže nepočítejte s tím, že vydrží stejně dlouho jako klasická běžecká bota.</p>'
          '<h2>Dětské ponožkoboty</h2>'
          '<p>Dětské nohy se vyvíjejí a volná, ohebná obuv jim umožňuje přirozený pohyb. Dětská řada se hodí do školky, na hřiště i na přezutí ve škole. Dbejte na to, aby bota nebyla příliš velká, a kontrolujte velikost každých několik měsíců. Ve vlhku a v zimě dítě potřebuje ochranu, kterou ponožkoboty neposkytují. Se zdravotními otázkami nohou dětí se obraťte na dětského lékaře nebo ortopeda.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Objednání podle běžné velikosti místo změření chodidla.</li>'
          '<li>Očekávání, že tenká podrážka vydrží lámání ostrých povrchů.</li>'
          '<li>Nošení v dešti nebo mrazu, kde bota není určena.</li>'
          '<li>Příliš rychlý přechod z tlumených bot a následné bolesti.</li>'
          '<li>Pořízení extrémně barevných nebo módních variant bez ohledu na střih.</li></ul>'
          '<h2>Jak ušetřit při nákupu</h2>'
          '<p>Ponožkoboty vycházejí v mnoha barvách, jejichž střih je shodný. Barva se při srovnání cen často liší více než model, takže projděte několik variant stejné řady. Sledujte také, zda obchod nabízí výměnu velikosti a dopravu zdarma, protože při nejistotě s velikostí se vám nákup vyplatí jen tehdy, když ho lze snadno vrátit. Na Sportece uvidíte nabídky vedle sebe a můžete přeskočit na stránku obchodu až při rozhodnutí. Další tipy k obuvi najdete v nadřazené kategorii <a href="/sportovni-obuv/">sportovní obuv</a> a v přehledu barefoot bot.</p>',
    faq=[
        ('Co jsou ponožkoboty?', 'Je to lehká barefoot obuv s elastickým svrškem podobným ponožce a tenkou ohebnou podrážkou. Chodidlo si v ní zachovává přirozený pohyb a boty se dají sbalit do malé kapsy.'),
        ('Jsou ponožkoboty to samé co barefoot boty?', 'Patří mezi barefoot obuv, ale jsou její nejminimalističtější formou. Klasické barefoot boty a tenisky mívají pevnější svršek a větší ochranu.'),
        ('Jak vybrat správnou velikost ponožkobot?', 'Změřte délku chodidla večer a porovnejte ji s tabulkou výrobce. Nechte několik milimetrů volného místa před prsty a vždy se řiďte konkrétním modelem.'),
        ('Dají se ponožkoboty prát?', 'Většinu lze prát ručně v lehce teplé vodě, někdy v pračce na šetrný program. Sušte je volně na vzduchu mimo topení a vždy se řiďte štítkem od výrobce.'),
        ('Hodí se ponožkoboty do vody?', 'Pletenina rychle schne, takže se hodí do mělké vody a na pláž. Na kamenité dno nebo do proudu je lepší obuv určená přímo do vody.'),
        ('Můžu v ponožkobotách běhat?', 'Lze, ale na bosý styl je třeba zvykat postupně, s kratšími úseky a rovným povrchem. Při potížích se poraďte s trenérem nebo fyzioterapeutem.'),
        ('Jsou ponožkoboty vhodné pro děti?', 'Dětská řada je pro volný pohyb nohy vhodná do školky a na hřiště. Boty nesmí být příliš velké a pro chlad nebo vlhko nejsou dostatečnou ochranou.'),
        ('Nosí se v nich ponožky?', 'Mnoho modelů je určeno pro nošení naboso, protože má hladký vnitřek. V chladnějších dnech lze zkusit tenkou ponožku, pokud se noha v botě stále vejde bez tlaku.'),
        ('Jak dlouho ponožkoboty vydrží?', 'Záleží na povrchu a četnosti nošení. Tenká podrážka se brousí rychleji než silná, proto je to obuv spíše na lehčí použití než na denní chůzi po drsném asfaltu.'),
        ('Čím se liší prstová obuv Vibram od ponožkobot?', 'Prstová obuv má pro každý prst zvláštní kapsu, ponožkoboty mají společný prostor. Prstové boty potřebují správné sladění tvaru nohy a delší zvykání.'),
    ])

# ------------------------------------------------------------------ posilovaci-lavice
NEW['posilovaci-lavice'] = dict(long=True,
    title='Posilovací lavice: rovná, variabilní, na bench press',
    desc='Posilovací lavice do domácí posilovny: rovné, variabilní a specializované. Jak vybrat nosnost, polohování a stabilitu a porovnat nabídky obchodů.',
    intro='<p>Posilovací lavice je základ domácí posilovny. Umožňuje tlaky na prsa s jednoručními činkami nebo s velkou činkou, přítahy, cvičení ramen i břicha a díky různým úhlům oporu pro mnoho dalších cviků. Správně zvolená lavice vydrží roky, špatná se viklá nebo se chvěje pod zátěží. Sporteka porovnává nabídky českých obchodů, kde najdete rovné, variabilní, skládací i specializované modely.</p>'
          '<p>Tahle stránka vysvětluje rozdíl mezi jednotlivými typy, nosnost, polohování opěrky, rozměry a materiály čalounění. V nabídce jsou značky ' + B(('hms', 'HMS'), ('marbo', 'Marbo'), ('insportline', 'Insportline'), ('gorilla-sports', 'Gorilla Sports'), ('hop-sport', 'Hop-sport'), ('sedco', 'Sedco'), ('tunturi', 'Tunturi'), ('domyos', 'Domyos'), ('zipro', 'Zipro'), ('vifito', 'Vifito')) + '. Širší výběr vybavení najdete v kategorii <a href="/posilovaci-stroje/">posilovací stroje a lavice</a>.</p>',
    guide='<h2>Typy posilovacích laviček</h2>'
          '<p>Slovo lavice nebo bench se v nabídce používá pro několik odlišných výrobků. Než začnete porovnávat parametry, rozhodněte se, co s lavicí chcete dělat.</p>'
          + T(['Typ lavice', 'K čemu slouží', 'Hodí se pro'], [
              ['Rovná lavice', 'tlaky vleže, přítahy, cviky pro triceps', 'jednoduchou a stabilní základnu'],
              ['Variabilní lavice', 'nastavitelné sklopné opěradlo od ležaté po svislou polohu', 'většinu domácích cvičenců'],
              ['Šikmá lavice', 'pevný sklon pro horní část prsou', 'cílené zaměření, pokud máte málo místa'],
              ['Lavice s úpravou sedáku', 'nastavitelný sedák, často sklopitelný', 'tlaky s velkou činkou i pro pokročilé'],
              ['Scottova lavice', 'opora paží při bicepsových zdvizích', 'izolaci bicepsů'],
              ['Římská lavice a hyperextenze', 'cvičení spodních zad a hýždí', 'doplňkové posilování zad'],
              ['Sit up bench', 'šikmá lavice na zdvihy trupu s fixací nohou', 'cvičení břicha'],
              ['Multifunkční lavice', 'kombinace několika funkcí v jednom rámu', 'malý prostor, začátečníky'],
              ['Příslušenství', 'návleky, opěrky a držáky', 'doplnění existující lavice']]) +
          '<h2>Rovná lavice, nebo variabilní</h2>'
          '<p>Rovná lavice je nejjednodušší a nejtužší. Má málo pohyblivých částí, takže se nemá co rozbít, a bývá levnější na výrobu. Variabilní lavice nabízí víc cviků, ale složitější mechanismus a více míst, kde se může objevit vůle. Pro většinu lidí, kteří chtějí cvičit celé tělo, je variabilní varianta rozumnější volba. Pokud trénujete především těžké tlaky s činkou a chcete maximální stabilitu, vybírejte robustní rovný model nebo lavici určenou k použití se stojanem.</p>'
          '<h2>Nosnost a stabilita</h2>'
          '<p>Nosnost uvádí výrobce jako maximální zátěž, kterou lavice snese. Ověřte, zda údaj zahrnuje jen hmotnost cvičence, nebo i činku. Počítejte součet: vaše váha plus nejtěžší činky, které chcete zvedat, plus rezerva. Nosnost uvedená na levných modelech je často optimistická, takže vybírejte s odstupem.</p>'
          '<ul><li><strong>Rám:</strong> ocelové profily s větším průřezem a svařované spoje jsou stabilnější než tenké trubky šroubované do tvaru U.</li>'
          '<li><strong>Stopa:</strong> širší nohy a více bodů opory zabraňují klopení při tlacích s činkami.</li>'
          '<li><strong>Protiskluzové zakončení:</strong> pryžové patky chrání podlahu a brání pohybu lavice.</li>'
          '<li><strong>Sedlo a opěradlo:</strong> musí být pevně uchyceny, ne se kývat při zatížení.</li></ul>'
          '<h2>Polohování opěradla a sedáku</h2>'
          '<p>Variabilní lavice mají opěradlo nastavitelné ve více polohách, obvykle od záporného sklonu přes rovinu až po téměř svislou polohu. Důležité je, jak se poloha zajišťuje. Nejlepší je čepový zámek s pevnými otvory, méně spolehlivé jsou pružinové kolíky nebo klasické západky. Zkontrolujte, zda se zámek ovládá bez nářadí a zda vyhovuje i při těžké zátěži. Sedák, který lze také naklonit, pomáhá držet se při tlaku s činkou a zabraňuje sklouznutí.</p>'
          '<h2>Rozměry a čalounění</h2>'
          '<p>Šířka sedacího a opěrného dílu určuje komfort i stabilitu. Pro cviky s velkou činkou potřebujete dostatečně širokou plochu pro lopatky, jinak se vám při tlaku vychyluje záda. Příliš široká lavice zase omezuje pohyb paží při přítazích. Výška sedáku by měla umožnit pevné opření nohou o zem. Čalounění bývá z kůže a syntetické kůže nebo z textilu, vnitřek je z pěny. Příliš měkká pěna se propadá a destabilizuje cvičení, příliš tvrdá tlačí. Dobrou volbou je střední tuhost s protiskluzovým povrchem.</p>'
          '<h2>Skládací a přenosné lavice</h2>'
          '<p>Pokud cvičíte v obývacím pokoji nebo v garáži sdílené s autem, ocení se skládací provedení. Rám se sklopí a lavice se opře o zeď. Kompromis je nižší tuhost a menší nosnost. Zkontrolujte pevnost závěsů, protože právě tam se při opakovaném skládání objevuje vůle. Pro nejtěžší cviky ponechte lavici pevně rozloženou.</p>'
          '<h2>Lavice pro konkrétní cvičení</h2>'
          '<ul><li><strong>Tlak s jednoručkami:</strong> pomůže variabilní lavice s dostatečně širokým opěradlem. Sety najdete v kategorii <a href="/cinky-a-kotouce/">činky a kotouče</a>.</li>'
          '<li><strong>Tlak s velkou činkou:</strong> potřebuje robustní rám, ideálně s opěrnými stojany, a rezervu v nosnosti.</li>'
          '<li><strong>Přítahy jednoruč:</strong> opřete koleno a ruku o rovnou lavici, proto je dobrá užší a delší plocha.</li>'
          '<li><strong>Břicho:</strong> sit up lavice nebo sklonitelná lavice s fixací nohou.</li>'
          '<li><strong>Záda:</strong> římská lavice nebo hyperextenze pro spodní část zad a hýždě.</li>'
          '<li><strong>Biceps:</strong> Scottova lavice s opěrkou pro paže.</li></ul>'
          '<h2>Kam lavici postavit</h2>'
          '<p>Měřte celkový prostor, ne jen délku samotné lavice. Při tlaku s činkou potřebujete místo po stranách a za hlavou pro bezpečné vstání. Podlaha musí být rovná a nosná. Na tvrdé podlaze pomůže protiskluzová podložka, která chrání dlažbu, snižuje hluk a stabilizuje rám. V bytě počítejte se zvukem dopadajících kotoučů a zvažte gumové desky. Ucelené sety pro doma se hodí, když doplníte další vybavení, například z kategorie <a href="/funkcni-trenink/">funkční trénink a hrazdy</a>.</p>'
          '<h2>Bezpečnost při cvičení</h2>'
          '<p>Nejčastější zranění nevzniká poruchou lavice, ale špatným odhadem síly. Při těžkých tlacích vleže používejte stojany s pojistkou nebo spolucvičence. Před každým tréninkem zkontrolujte šrouby, zámky a stav čalounění. Začněte s lehčí zátěží a ověřte, zda lavice při pohybu nekmitá. Pokud máte zdravotní potíže se zády, rameny nebo srdcem, poraďte se s lékařem nebo kvalifikovaným trenérem.</p>'
          '<h2>Montáž a údržba</h2>'
          '<p>Většina laviček se dodává rozložená a sestavení trvá obvykle jednu hodinu, bez speciálního nářadí. Šrouby dotahujte postupně, nejdřív volně všechny, až poté pevně, aby se rám nepřepjal. Po prvních týdnech používání kontrolu zopakujte, protože se matice nejčastěji uvolňují právě zpočátku. Čalounění otírejte vlhkým hadrem a mýdlovým roztokem a pohyblivé spoje občas promažte. Pot a vlhkost rez a plíseň urychlují, proto lavici po tréninku osušte.</p>'
          '<h2>Lavice a návaznost na další vybavení</h2>'
          '<p>Lavice málokdy stojí sama. Většinou ji doplníte sadou jednoručních činek, později stojanem nebo kladkou. Při plánování domácí posilovny proto myslete na to, jaký cvičební styl chcete v následujících letech provozovat. Kdo počítá s postupným přidáváním zátěže, ušetří, když hned koupí lavici s rezervou nosnosti a širokým opěradlem, protože výměna za pevnější model znamená druhý nákup. Kdo se zaměřuje hlavně na tělesnou hmotnost a lehčí činky, vystačí s úspornější lavicí. Důležitá je také pohodlná výška, která odpovídá vašemu vzrůstu: u vyšších cvičenců se vyplatí delší opěradlo, u menších zase nižší sedák, aby chodidla pevně stála na podlaze. Před nákupem si proto přečtěte rozměry a porovnejte je s tím, co máte doma.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete široké spektrum výrobců. Domácí posilovny obsluhují hlavně ' + B(('insportline', 'Insportline'), ('marbo', 'Marbo'), ('hms', 'HMS'), ('sedco', 'Sedco'), ('hop-sport', 'Hop-sport'), ('vifito', 'Vifito'), ('zipro', 'Zipro')) + ' a ' + B(('gorilla-sports', 'Gorilla Sports')) + '. Pokročilejší a komerčněji zaměřené konstrukce mívá například ' + B(('tunturi', 'Tunturi')) + ' a levnější lavice na začátek ' + B(('domyos', 'Domyos')) + '. V nabídce se mohou objevit i zboží se slovem bench v názvu, například oblečení nebo tašky. Pozornost věnujte názvu a kategorii.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Podcenění nosnosti a nákup lavice na hraně zatížení.</li>'
          '<li>Ignorování šířky opěradla, na kterém se pak lopatky nedrží stabilně.</li>'
          '<li>Výběr lavice jen podle počtu poloh, ne podle kvality zámku.</li>'
          '<li>Nákup velké multifunkční konstrukce, která se do místnosti nevejde.</li>'
          '<li>Opomenutí příslušenství, třeba stojanů, pojistek nebo podložky.</li></ul>'
          '<h2>Jak ušetřit při nákupu</h2>'
          '<p>Rozdíl v nabídkách bývá největší u příslušenství a dopravy. Lavice je objemná, proto porovnávejte poštovné a možnost osobního odběru. Sledujte, zda je v ceně montážní materiál a zda dodavatel nabízí náhradní díly, protože u levnějších konstrukcí se opotřebují nejdřív čalounění a zámek. Pokud trénujete doma, zvažte, zda místo samostatné lavice nestačí kombinace lehčí lavice a <a href="/posilovaci-gumy/">posilovacích gum</a>. Další cvičební vybavení najdete v kategorii <a href="/fitness/">fitness</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>.</p>',
    faq=[
        ('Jakou posilovací lavici vybrat do domácí posilovny?', 'Pro většinu lidí je nejuniverzálnější variabilní lavice s dostatečnou nosností a pevným zámkem opěradla. Pro těžké tlaky s velkou činkou zvolte robustní rám.'),
        ('Jaká nosnost lavice stačí?', 'Sečtěte svou hmotnost a nejtěžší činky, které budete zvedat, a přidejte rezervu. Nosnost uvedenou na levných modelech berte spíše jako horní hranici.'),
        ('Čím se liší rovná a variabilní lavice?', 'Rovná lavice je tužší a jednodušší, variabilní má nastavitelné opěradlo a tím víc cviků. Složitější mechanismus ale znamená více míst, kde se může objevit vůle.'),
        ('Dá se na lavici cvičit s jednoručními činkami i s velkou činkou?', 'Ano, pokud je dostatečně stabilní a široká. Pro velkou činku zvlášť zkontrolujte nosnost, rozměry a zda se lavice při tlaku nekýve.'),
        ('Je vhodná skládací lavice?', 'Pro malé prostory ano, ale mívá nižší tuhost a menší nosnost. Zkontrolujte pevnost kloubů, kde se při opakovaném skládání objevuje vůle.'),
        ('Co je Scottova lavice?', 'Je to lavice s nakloněnou opěrkou pro paže, která slouží k izolovaným zdvihům na biceps. Samostatně se prodává, nebo bývá součástí multifunkční lavice.'),
        ('K čemu je římská lavice?', 'Slouží k hyperextenzím a cvičení spodních zad, hýždí a zadní strany stehen. Nohy se fixují pod válečky a trup se pohybuje nahoru a dolů.'),
        ('Jak poznat kvalitní zámek polohování?', 'Čepový zámek s pevnými otvory, který zapadne bez vůle a lze ho ovládat jednou rukou, je spolehlivější než pružinový kolík nebo plastová západka.'),
        ('Jak velký prostor lavice potřebuje?', 'Počítejte nejen s její délkou, ale i s místem po stranách a za hlavou. Při tlaku s činkou musíte mít bezpečný prostor pro nastavení i odložení zátěže.'),
        ('Jak pečovat o čalounění?', 'Otírejte ho vlhkým hadrem a jemným mýdlovým roztokem, nepoužívejte agresivní chemii a po cvičení lavici osušte, aby pot neničil povrch.'),
        ('Je lavice vhodná i pro začátečníky?', 'Ano. Začněte s lehčí zátěží, zvládněte techniku a u těžkých tlaků cvičte se spolucvičencem nebo se stojany. Při zdravotních potížích se poraďte s lékařem nebo trenérem.'),
    ])
