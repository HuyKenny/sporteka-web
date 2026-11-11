"""sporteka.cz — wave 25b2: long texts for masazni-pistole, omega-3, horcik.
General true facts only, no prices. Brands verified in the catalogue sample."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ masazni-pistole
NEW['masazni-pistole'] = dict(long=True,
    title='Masážní pistole: jak vybrat, amplituda, nástavce, baterie',
    desc='Masážní pistole od mini po profi modely. Jak vybrat amplitudu, otáčky, baterii a nástavce a porovnat nabídky českých obchodů vedle sebe.',
    intro='<p>Masážní pistole je ruční přístroj s kmitající hlavicí, která v rychlém rytmu naráží do měkkých tkání. Používá se před tréninkem v rámci rozcvičky, po výkonu jako příjemné dotažení a také při sezení u počítače, když člověka tlačí šíje a bedra. Přístroj nic neléčí, jen poskytuje mechanickou stimulaci, která řadě lidí přijde příjemná. Sporteka porovnává nabídky českých obchodů u kompaktních mini pistolí, plnohodnotných modelů i přístrojů s vyhřívanou nebo chladivou hlavicí.</p>'
          '<p>V přehledu najdete značky ' + B(('beurer', 'Beurer'), ('kica', 'Kica'), ('tunturi', 'Tunturi'), ('lifefit', 'Lifefit'), ('insportline', 'Insportline'), ('4fizjo', '4FIZJO'), ('gymbeam', 'GymBeam'), ('xtrexo', 'Xtrexo'), ('hms', 'HMS'), ('eljet', 'Eljet')) +
          '. Pokud váháte, zda vám víc sedne klasická pomůcka, projděte nadřazenou kategorii <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>',
    guide='<h2>Jak masážní pistole funguje</h2>'
          '<p>Uvnitř je malý motor, který přes klikový mechanismus posouvá hlavici dopředu a dozadu. Hlavice tak tluče do kůže a svalu krátkými, rychlými údery. Odborně se tomu říká perkusní masáž. Důležité jsou dvě veličiny: kolik milimetrů hlavice vykoná při jednom úderu a kolikrát za minutu to zopakuje. První údaj se nazývá amplituda nebo zdvih, druhý otáčky či frekvence a výrobci ho uvádějí v úderech nebo otáčkách za minutu.</p>'
          '<p>Přístroj nahrazuje ruce terapeuta jen částečně. Neumí vycítit napětí, nepřizpůsobí tlak a nepozná, kdy je lepší přestat. Berte ho proto jako pomůcku pro domácí použití, nikoli jako náhradu fyzioterapie.</p>'
          '<h2>Parametry, které se vyplatí porovnat</h2>'
          + T(['Parametr', 'Co znamená', 'Na co se dívat'], [
              ['Amplituda (zdvih)', 'délka jednoho úderu v milimetrech', 'menší hodnota je jemnější, větší pronikne hlouběji do velkých svalů'],
              ['Otáčky za minutu', 'rychlost úderů', 'více rychlostních stupňů dovolí začít zlehka a postupně přitvrdit'],
              ['Síla motoru', 'schopnost držet rytmus při přitlačení', 'slabší motor se při tlaku zastaví nebo zpomalí'],
              ['Kapacita baterie', 'údaj v mAh a doba provozu', 'záleží na tom, zda přístroj vezmete na cesty nebo ho nabíjíte doma'],
              ['Hlučnost', 'zvuk při provozu', 'pro večerní použití doma je tišší model příjemnější'],
              ['Hmotnost a tvar rukojeti', 'pohodlí při držení', 'těžší přístroj unaví ruku, ale lépe drží tlak'],
              ['Počet nástavců', 'sada výměnných hlavic', 'více tvarů pokryje více partií těla'],
              ['Příslušenství', 'pouzdro, nabíječka, vyhřívaná hlavice', 'praktické pro přepravu a delší životnost']]) +
          '<p>Údaje výrobců nejsou měřené stejně, takže slepě porovnávat jedno číslo mezi dvěma značkami nemá smysl. Mnohem užitečnější je dívat se na celek: popis, recenze zákazníků a to, zda obchod uvádí všechny hlavní parametry.</p>'
          '<h2>Amplituda a otáčky: jak je číst</h2>'
          '<p>Kratší zdvih zhruba v rozmezí několika milimetrů působí povrchově a jemně. Dlouhý zdvih kolem dvou centimetrů už je výrazně hlubší, hodí se na velké svaly, ale může být nepříjemný na začátku. Pro člověka, který pistoli zkouší poprvé, bývá rozumná střední cesta, nebo přístroj s více stupni, na kterém začne tou nejjemnější úrovní. Při vyšších otáčkách je vibrace silnější, ale ne vždy příjemnější. Hlubší efekt zajistí hlavně amplituda, ne samotná rychlost.</p>'
          '<h2>Mini, standardní a profesionální pistole</h2>'
          '<p>V nabídce se potkávají tři velikostní skupiny. Mini modely, jako jsou ty, které v názvu mají slovo Mini, se vejdou do kapsy sportovní bundy nebo do menší tašky. Mají slabší motor, kratší zdvih a menší baterii, ale na lýtka, předloktí a šíji bohatě stačí. Standardní pistole mají plnohodnotný zdvih, několik stupňů a sadu nástavců. Profesionální přístroje bývají větší, těžší a vybavené silnější baterií a pouzdrem, určené pro trenéry a ty, kdo je používají denně.</p>'
          + T(['Skupina', 'Výhody', 'Nevýhody'], [
              ['Mini', 'malé rozměry, nízká hmotnost, snadné balení', 'menší síla, kratší výdrž baterie'],
              ['Standardní', 'vyvážený poměr síly a velikosti, sada hlavic', 'větší než kapesní modely'],
              ['Profesionální', 'silný motor, velká baterie, pouzdro', 'vyšší hmotnost, objemnější balení'],
              ['S vyhřívanou nebo chladivou hlavicí', 'kombinace perkuse s teplem či chladem', 'složitější konstrukce, větší nároky na péči']]) +
          '<h2>Nástavce a jejich použití</h2>'
          '<p>Výměnné hlavice jsou jednou z hlavních věcí, kterými se pistole liší. Většina sad obsahuje kulatou, plochou, kuželovou a vidlicovou hlavici. Každá se hodí na jiné místo a mění pocit z masáže.</p>'
          + T(['Nástavec', 'Tvar', 'Typické použití'], [
              ['Kulatá hlavice', 'koule nebo půlkoule', 'velké svaly, jako stehna a hýždě'],
              ['Plochá hlavice', 'rovný disk', 'plošné partie, záda, hrudník'],
              ['Kuželová hlavice', 'špička', 'úzké partie, chodidlo, dlaň'],
              ['Vidlicová hlavice', 'dvě větve', 'okolo páteře a Achillovy šlachy, nikdy přímo na ni'],
              ['Měkká pěnová hlavice', 'tlumený povrch', 'citlivější místa, začátečníci'],
              ['Vyhřívaná či chladivá hlavice', 'kovová plocha s ohřevem nebo chladem', 'příjemný doplněk po výkonu nebo při ztuhlosti']]) +
          '<p>V katalogu najdete i samostatné hlavice, třeba nahřívací a chladicí nástavce pro pistole určitých značek. Před koupí ověřte, zda závit nebo uchycení odpovídá vašemu přístroji, protože univerzální standard neexistuje.</p>'
          '<h2>Pro koho je masážní pistole vhodná</h2>'
          '<ul><li><strong>Běžci a cyklisté:</strong> po delším tréninku lze přejet přes lýtka, stehna a hýždě. U cyklistů a běžců je to jedna z nejčastějších pomůcek.</li>'
          '<li><strong>Silový trénink:</strong> před cvičením zahřeje velké svaly a po něm zklidní namáhané partie. Pro rozcvičku ji můžete kombinovat s <a href="/posilovaci-gumy/">posilovacími gumami</a>.</li>'
          '<li><strong>Kancelářská práce:</strong> šíje, ramena a bedra. Tady se hodí tišší a lehčí model s měkkou hlavicí.</li>'
          '<li><strong>Cvičení jógy a pilates:</strong> po lekci je příjemné rozmasírovat ztuhlé partie, ať už jde o <a href="/joga-a-podlozky/">jógu</a>, nebo <a href="/pilates-pomucky/">pilates</a>.</li>'
          '<li><strong>Trenéři a masérky:</strong> profesionální model s odolnou baterií a pouzdrem.</li></ul>'
          '<h2>Pistole, válec, nebo míček</h2>'
          '<p>Každá pomůcka řeší trochu jiný problém. Pěnový válec působí plošně a vyžaduje vlastní hmotnost těla a koordinaci. Míček je přesnější, ale hůř se vyrovná se zadní stranou stehen. Pistole je pohodlná, protože při ní můžete zůstat v klidu na gauči a pouze vedete ruku. Nevýhodou je cena, nutnost nabíjení a hluk. Mnoho sportovců používá kombinaci, a proto stojí za to projít i sousední kategorie <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/funkcni-trenink/">funkční trénink</a>.</p>'
          '<h2>Jak masážní pistoli používat</h2>'
          '<ol><li>Začněte nejnižším stupněm a hlavici jen položte na sval. Tlak nahrazuje vlastní váha přístroje.</li>'
          '<li>Pohybujte pomalu, přibližně rychlostí několika centimetrů za vteřinu, po svalu, ne po kosti.</li>'
          '<li>Na jednom místě se zdržujte krátce, obecně nejvýše jednu až dvě minuty, a řiďte se pokyny výrobce.</li>'
          '<li>Hlavici veďte ve směru svalových vláken a nikdy nenatlačujte do bolesti.</li>'
          '<li>Po použití si dopřejte klidné protažení nebo pití vody, pokud vám to pomáhá.</li></ol>'
          '<p>Vynechte klouby, kosti, přední stranu krku, hlavu, tříslo a místa s podrážděnou kůží. Přístroj nepoužívejte při akutním zranění, otoku, zánětu, křečových žilách, těhotenství, při užívání léků na ředění krve ani s kardiostimulátorem. Pokud se necítíte jistě, poraďte se s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Časté chyby při nákupu a používání</h2>'
          '<ul><li>Volba podle jediného čísla, třeba podle počtu otáček, bez zohlednění zdvihu a hlučnosti.</li>'
          '<li>Příliš silný přítlak, který vyvolá bolest místo uvolnění.</li>'
          '<li>Dlouhé masírování jednoho místa v domnění, že víc znamená lépe.</li>'
          '<li>Nákup minipistole pro velké svaly a následné zklamání z malé síly.</li>'
          '<li>Opomenutí nástavců: sada o dvou hlavicích může být pro vaše potřeby málo.</li>'
          '<li>Ignorování nabíjení: baterie zcela vybitá po dlouhou dobu ztrácí kapacitu.</li></ul>'
          '<h2>Péče, nabíjení a životnost</h2>'
          '<p>Přístroj otřete suchým nebo lehce vlhkým hadříkem, nikdy ho neponořujte do vody. Hlavice se dají umýt jemným mýdlem a musí se nechat uschnout. Uložte ho do pouzdra nebo krabice, mimo přímé slunce a vlhko. Lithiové baterie mají rády střední stav nabití a nesnášejí dlouhé uložení úplně vybité. Jednou za čas si zkontrolujte, zda se nepovolilo uchycení hlavice. Pokud se při chodu objeví zvláštní zvuky nebo zápach spáleniny, přístroj vypněte a nepoužívejte ho.</p>'
          '<h2>Na co si dát pozor při koupi</h2>'
          '<ul><li><strong>Záruka a servis:</strong> přístroj s motorem a baterií je spotřební zboží, a proto sledujte délku záruky a dostupnost náhradních dílů.</li>'
          '<li><strong>Kompletní příslušenství:</strong> nabíječka, pouzdro a hlavice by měly být součástí balení.</li>'
          '<li><strong>Typ nabíjení:</strong> USB-C je praktické, protože kabel už pravděpodobně doma máte.</li>'
          '<li><strong>Hlučnost:</strong> recenze zákazníků jsou užitečnější než údaj výrobce v decibelech.</li>'
          '<li><strong>Bezpečnostní značení:</strong> hledejte označení shody CE a návod v češtině.</li>'
          '<li><strong>Nadsazené sliby:</strong> přístroj je pomůcka, ne zdravotnický zázrak, a texty slibující vyléčení jsou varováním.</li></ul>'
          '<h2>Značky v katalogu</h2>'
          '<p>V nabídce Sportek jsou různé značky se zaměřením na domácnost, wellness i sport. ' + B(('beurer', 'Beurer')) + ' je známý hlavně z domácích zdravotních a wellness přístrojů a nabízí modely i s tepelnou hlavicí. ' + B(('kica', 'Kica')) + ' a ' + B(('xtrexo', 'Xtrexo')) + ' se zaměřují na kompaktní pistole od mini po plné modely. ' + B(('tunturi', 'Tunturi')) + ' a ' + B(('insportline', 'Insportline')) + ' jsou typické pro fitness vybavení a obvykle nabízejí zřetelné parametry. ' + B(('lifefit', 'Lifefit')) + ', ' + B(('4fizjo', '4FIZJO')) + ', ' + B(('hms', 'HMS')) + ', ' + B(('gymbeam', 'GymBeam')) + ' a ' + B(('eljet', 'Eljet')) + ' doplňují nabídku o další modely. Vždy si ověřte konkrétní parametry u každého kusu, protože značka sama o výkonu nerozhoduje.</p>'
          '<h2>Jak ušetřit při nákupu masážní pistole</h2>'
          '<p>Sporteka zobrazuje nabídky obchodů vedle sebe, takže poznáte, kde je stejný model dostupný za nižší cenu. Při porovnání myslete na celkové náklady: poštovné, sadu hlavic v balení a délku záruky. Starší generace téhož modelu bývá často levnější a rozdíl ve výkonu se v domácím použití nemusí projevit. Sezónní slevy a akce kolem svátků jsou obvyklé, takže cenu sledujte před nákupem. Nepořizujte nejsilnější přístroj jen proto, že je nejsilnější: kdo ho použije dvakrát týdně na lýtka, vystačí s jednodušším modelem. A pokud jde o první kontakt s masážní technikou, může úplně stačit <a href="/masazni-pomucky/">pěnový válec nebo míček</a>.</p>'
          '<h2>Pistole a související doplňky</h2>'
          '<p>K regeneraci patří i další věci, které si můžete projít: kompresní a stabilizační pomůcky v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, doplňky pro sportovce v <a href="/sportovni-vyziva/">sportovní výživě</a> nebo lehká kardio zátěž na <a href="/kardio-trenazery/">kardio trenažérech</a>. Žádný přístroj ale nenahradí dostatek spánku, pitný režim a rozumné zatěžování.</p>',
    faq=[
        ('K čemu je masážní pistole dobrá?', 'Slouží jako pomůcka při rozcvičce a po tréninku nebo při ztuhlosti od sezení. Působí mechanicky na měkké tkáně a řadě lidí přijde příjemná. Léčebné účinky nemá a při potížích je potřeba se poradit s lékařem.'),
        ('Jak vybrat masážní pistoli?', 'Sledujte amplitudu, počet rychlostních stupňů, výdrž baterie, hlučnost a sadu nástavců. Pro cestování zvažte mini model, pro doma plnohodnotný. Porovnejte také záruku a dostupnost servisu.'),
        ('Co je to amplituda u masážní pistole?', 'Je to délka jednoho úderu hlavice v milimetrech. Menší zdvih je jemnější, větší pronikne hlouběji do velkých svalů. Údaj je užitečnější než samotné otáčky za minutu.'),
        ('Kolik stupňů rychlosti je dost?', 'Pro domácí použití stačí tři až pět stupňů. Důležité je, aby nejnižší byl opravdu jemný, protože při prvním použití je lepší začít zlehka. Více stupňů nabízí jemnější nastavení.'),
        ('Na jaká místa se pistole nepoužívá?', 'Vynechejte kosti, klouby, přední stranu krku, hlavu, tříslo a podrážděnou kůži. Neprocházejte přes zranění, otok a zánět. Při zdravotním omezení se nejprve poraďte s lékařem.'),
        ('Jak dlouho masírovat jedno místo?', 'Obecně se doporučuje krátká doba, nejvýše několik desítek vteřin až dvě minuty na jeden sval. Přesný pokyn najdete v návodu výrobce. Při nepříjemném pocitu přestaňte.'),
        ('Je lepší masážní pistole, nebo pěnový válec?', 'Každá pomůcka má jiné silné stránky. Válec je levnější a působí plošně, pistole je pohodlná a dobře se dostane na zadní stranu nohou. Mnoho sportovců používá obě.'),
        ('Mohu pistoli používat před tréninkem?', 'Ano, krátké použití na velké svaly bývá součástí rozcvičky. Neměla by ji nahradit pohybová příprava. Používejte nižší stupeň a krátkou dobu.'),
        ('Jak dlouho vydrží baterie masážní pistole?', 'Závisí na kapacitě, zvoleném stupni a stáří baterie. Výrobci uvádějí dobu provozu v hodinách, reálná výdrž při vyšších stupních bývá kratší. Baterii nenechávejte dlouho úplně vybitou.'),
        ('Jak masážní pistoli čistit a skladovat?', 'Otírejte ji suchým nebo mírně vlhkým hadříkem a nepoužívejte agresivní čističe. Hlavice se dají umýt jemným mýdlem. Skladujte ji v pouzdře na suchém místě mimo přímé slunce.'),
        ('Hodí se vyhřívaná hlavice?', 'Je to příjemný doplněk, pokud preferujete kombinaci perkuse s teplem nebo chladem. Pro základní použití není nutná. Dbejte na pokyny výrobce a nepřikládejte horkou hlavici dlouho na jedno místo.'),
    ])

# ------------------------------------------------------------------ omega-3
NEW['omega-3'] = dict(long=True,
    title='Omega-3 a rybí olej: jak vybrat, EPA a DHA, formy',
    desc='Omega-3 a rybí olej v kapslích i tekuté formě. Jak číst EPA a DHA, rozlišit rybí, krillový a řasový olej a porovnat nabídky obchodů.',
    intro='<p>Omega-3 mastné kyseliny patří k tukům, které si lidské tělo neumí samo vytvořit v dostatečné míře, a proto je přijímáme stravou. Hlavními zdroji jsou tučné mořské ryby, ale také lněné semínko nebo vlašské ořechy. Doplňky stravy s rybím, krillovým nebo řasovým olejem nabízejí pohodlnou alternativu pro ty, kdo ryby jedí málo. Jde o doplněk stravy, nikoli o lék, a rozhodnutí o jeho užívání patří ke konzultaci s lékařem nebo lékárníkem.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů a najdete tu značky ' + B(('gymbeam', 'GymBeam'), ('nfo', 'NFO'), ('arctic-blue', 'Arctic Blue'), ('amix', 'Amix'), ('ostrovit', 'OstroVit'), ('masmusculo', 'Masmusculo'), ('vitaharmony', 'VitaHarmony'), ('moller-s', 'Möller´s'), ('czech-virus', 'Czech Virus'), ('nordbo', 'Nordbo')) +
          '. Další látky najdete v nadřazené kategorii <a href="/vitaminy-a-mineraly/">vitamíny, minerály a omega-3</a>.</p>',
    guide='<h2>Co je omega-3 a z čeho se skládá</h2>'
          '<p>Pod názvem omega-3 se skrývá skupina nenasycených mastných kyselin. V doplňcích stravy se nejčastěji setkáte se třemi. Kyselina eikosapentaenová (EPA) a kyselina dokosahexaenová (DHA) pocházejí hlavně z mořských zdrojů. Kyselina alfa-linolenová (ALA) se vyskytuje v rostlinných olejích, například lněném. Tělo umí ALA částečně přeměnit na EPA a DHA, ale účinnost přeměny je omezená, a proto se u mořských olejů dívá na obsah EPA a DHA přímo.</p>'
          '<p>Výživová doporučení pro omega-3 se liší podle země a věku, takže tento text neuvádí konkrétní denní dávky. Řiďte se údaji na obalu a radou lékaře nebo lékárníka.</p>'
          '<h2>Rybí, krillový a řasový olej</h2>'
          + T(['Zdroj', 'Co to je', 'Zvláštnosti'], [
              ['Rybí olej', 'olej z tělní tkáně tučných ryb, často z ančoviček, sardinek nebo makrel', 'nejběžnější a nejširší nabídka, různé koncentrace EPA a DHA'],
              ['Olej z tresčích jater', 'olej z jater tresky', 'kromě omega-3 obsahuje přirozeně vitaminy A a D, proto se čte i jejich obsah'],
              ['Krillový olej', 'olej z drobných korýšů krillu', 'omega-3 je vázaná ve fosfolipidech, kapsle bývají menší'],
              ['Řasový olej', 'olej z mořských řas', 'rostlinný zdroj, vhodný pro vegany a vegetariány'],
              ['Lněný olej a směsi 3-6-9', 'rostlinný olej s ALA, někdy s omega-6 a omega-9', 'neobsahuje přímo EPA a DHA, jiné složení než rybí olej']]) +
          '<p>Rozdíl mezi omega-3, omega-6 a omega-9 je v poloze dvojné vazby v molekule. Směsi označované jako omega 3-6-9 nejsou totéž co čistý rybí olej. U nich se tedy podívejte, kolik v jedné dávce je skutečně omega-3, a jakého druhu.</p>'
          '<h2>Jak číst etiketu rybího oleje</h2>'
          '<p>Slogan „1000 mg rybího oleje“ říká jen, kolik oleje kapsle obsahuje, nikoli kolik z něj tvoří prospěšné EPA a DHA. Právě tyto dvě látky určují, co vlastně kupujete. Správný postup při čtení etikety je tento:</p>'
          '<ol><li>Najděte údaj o EPA a DHA zvlášť a vypočtěte jejich součet v jedné dávce.</li>'
          '<li>Zjistěte, kolik kapslí tvoří jednu dávku, protože výrobci někdy počítají se dvěma nebo třemi.</li>'
          '<li>Vydělte cenu balení počtem dávek, abyste porovnali přípravky se stejným množstvím EPA a DHA.</li>'
          '<li>Sledujte formu: triglyceridová nebo ethylesterová. Ta první je přirozenější, druhá je častá u levnějších koncentrátů.</li>'
          '<li>Podívejte se na přidané látky, třeba vitamin D, K2, E nebo ADEK, a na antioxidant, který olej chrání.</li></ol>'
          + T(['Údaj na obalu', 'Co znamená', 'Proč ho sledovat'], [
              ['EPA a DHA v mg', 'obsah dvou hlavních mořských omega-3', 'rozhoduje o skutečné hodnotě přípravku'],
              ['Forma (TG, EE, fosfolipidy)', 'chemická vazba mastných kyselin', 'liší se způsob vstřebávání a cena'],
              ['Původ oleje', 'druh ryby nebo krill', 'důležité při alergii na ryby nebo korýše'],
              ['Čerstvost a oxidace', 'označení dosažené kvality, certifikáty třetích stran', 'zoxidovaný olej páchne a nemá smysl'],
              ['Obal', 'tmavá lahvička, blistr, měkká kapsle', 'světlo a vzduch olej kazí'],
              ['Pomocné látky', 'želatina, glycerol, aromata', 'u vegetariánů a vegetariánek, u alergiků']]) +
          '<h2>Formy: kapsle, tobolky, tekuté oleje a žvýkací varianty</h2>'
          '<p>Nejrozšířenější jsou měkké želatinové kapsle. Jsou pohodlné, nechutnají a olej v nich chrání před vzduchem. Rostlinné tobolky se hodí pro ty, kdo se vyhýbají želatině. Tekutý olej se dávkuje lžičkou nebo mililitry, bývá výhodnější z hlediska množství v balení, ale musí se skladovat v chladu a rychle spotřebovat. Pro děti jsou určeny žvýkací či ovocné varianty, například s příchutí pomeranče nebo ovoce. Takové produkty se vybírají podle věku a konkrétního návodu výrobce.</p>'
          '<h2>Pro koho se omega-3 doplňky nabízejí</h2>'
          '<ul><li><strong>Lidé, kteří jedí málo mořských ryb:</strong> v běžné stravě jich je málo a doplněk může být pohodlnou cestou.</li>'
          '<li><strong>Vegani a vegetariáni:</strong> hledají řasový olej s EPA a DHA.</li>'
          '<li><strong>Sportovci:</strong> doplněk jako součást pestré stravy najdete vedle <a href="/sportovni-vyziva/">sportovní výživy</a>, <a href="/aminokyseliny-bcaa/">aminokyselin</a> nebo <a href="/kreatin/">kreatinu</a>.</li>'
          '<li><strong>Děti a těhotné ženy:</strong> mají vlastní pravidla a před užíváním je zásadní poradit se s lékařem nebo pediatrem.</li></ul>'
          '<p>Žádný doplněk nepřekoná pestrou stravu, dostatek pohybu a spánek. Pokud užíváte léky, hlavně ty ovlivňující srážlivost krve, poraďte se s lékařem před zahájením užívání, protože omega-3 mohou s některými léčivy interagovat.</p>'
          '<h2>Kombinované přípravky s vitaminy</h2>'
          '<p>Mnoho výrobců přidává do rybího oleje vitamin D3, K2, E nebo celou skupinu ADEK. Kombinace šetří počet tablet, ale komplikuje dávkování: příliš velká dávka vitaminu rozpustného v tucích se nedoporučuje bez dohledu odborníka. Pokud už užíváte samostatný multivitamin nebo vitamin D, porovnejte celkový příjem. Pro přehled vitaminových přípravků se podívejte do kategorie <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>'
          '<h2>Jak užívat a skladovat</h2>'
          '<p>Etikety zpravidla radí užívat omega-3 s jídlem, které obsahuje tuk, protože tělo tuky lépe vstřebává. Dávku nepřekračujte a dodržujte pokyny výrobce. Kapsle skladujte v původním obalu na chladném a tmavém místě. Tekutý olej po otevření uchovávejte v lednici a spotřebujte ho do doby uvedené na etiketě. Pokud olej silně páchne po žluklém tuku, nepoužívejte ho.</p>'
          '<h2>Možné nežádoucí projevy</h2>'
          '<p>Někteří lidé po rybím oleji zažívají říhání s rybí příchutí, žaludeční nevolnost nebo řidší stolici. Pomáhá užívat kapsli s jídlem, rozdělit dávku nebo zkusit jinou formu. Alergici na ryby a korýše musí číst složení a vyhnout se příslušnému zdroji. V případě jakýchkoli potíží užívání přerušte a poraďte se s lékařem.</p>'
          '<h2>Omega-3 ve stravě: ryby a rostlinné zdroje</h2>'
          '<p>Přirozeným zdrojem EPA a DHA jsou tučné mořské ryby, třeba makrela, sardinky, sleď a losos. Rostlinné zdroje, jako je lněné a chia semínko, vlašské ořechy nebo řepkový olej, nabízejí ALA. Každý zdroj má jiné složení, takže se vzájemně nenahrazují jedna ku jedné. Pestrý jídelníček s rybou jednou až dvakrát týdně patří k obecným výživovým doporučením. Doplněk stravy má smysl zvážit tehdy, když ryby jíte málo nebo vůbec, ale pořád je to doplněk, který nenahradí pestrou stravu.</p>'
          '<h2>Jak poznat kvalitní přípravek</h2>'
          '<p>Kvalitu nelze posoudit podle obalu. Užitečné je hledat podrobnou etiketu s rozepsaným EPA a DHA, údajem o původu oleje a jasným uvedením formy. Někteří výrobci zveřejňují výsledky nezávislých testů čerstvosti a čistoty, což je příjemný bonus. Zdravá nedůvěra patří k velkým slibům typu „nejčistší na trhu“. Při nejistotě porovnejte více obchodů na Sportece a přečtěte si recenze zákazníků, hlavně o chuti a dochuti po užití.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Porovnávání podle celkového množství oleje, nikoli podle EPA a DHA.</li>'
          '<li>Nákup lněného oleje v domnění, že obsahuje totéž co rybí olej.</li>'
          '<li>Zanedbání počtu kapslí v jedné dávce při výpočtu ceny.</li>'
          '<li>Ukládání lahvičky na okně nebo do horka.</li>'
          '<li>Souběžné užívání několika přípravků se stejnými vitaminy.</li>'
          '<li>Očekávání rychlého zázraku od doplňku stravy.</li></ul>'
          '<h2>Značky v katalogu</h2>'
          '<p>Nabídku tvoří české i zahraniční značky. ' + B(('gymbeam', 'GymBeam')) + ' má v kategorii nejširší sortiment včetně veganské varianty a směsí 3-6-9. ' + B(('nfo', 'NFO')) + ' a ' + B(('arctic-blue', 'Arctic Blue')) + ' jsou zastoupeny desítkami kusů. ' + B(('amix', 'Amix')) + ' a ' + B(('ostrovit', 'OstroVit')) + ' jsou sportovní značky s koncentrovanějšími kapslemi. ' + B(('masmusculo', 'Masmusculo')) + ', ' + B(('vitaharmony', 'VitaHarmony')) + ', ' + B(('moller-s', 'Möller´s')) + ', ' + B(('czech-virus', 'Czech Virus')) + ', ' + B(('nordbo', 'Nordbo')) + ' a ' + B(('movit-energy', 'Movit Energy')) + ' doplňují výběr. Každou položku posuzujte podle etikety, ne podle jména výrobce.</p>'
          '<h2>Jak ušetřit u omega-3</h2>'
          '<p>Základem je porovnat cenu za dávku s odpovídajícím obsahem EPA a DHA, ne cenu za krabičku. Velká balení bývají na dávku výhodnější, ale jen když je stihnete spotřebovat před koncem trvanlivosti. Sporteka ukazuje nabídky více obchodů u stejného produktu vedle sebe, takže nepřeplatíte. Sledujte i akce kolem sezonních slev a kombinované přípravky, kde zaplatíte za vitamin D a K2 v jednom, pokud ho opravdu potřebujete. Pokud chcete s hořčíkem a omega-3 dostat i další minerály, projděte sourozeneckou kategorii <a href="/horcik/">hořčík</a>.</p>'
          '<h2>Omega-3 mezi ostatními doplňky</h2>'
          '<p>Pro orientaci v širší nabídce se hodí kategorie <a href="/kolagen-a-klouby/">kolagen a kloubní výživa</a>, <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a> nebo <a href="/proteiny/">proteiny</a>. Doplněk stravy má doplnit stravu, nikoli ji nahradit, a při jakékoli nejistotě je nejlepší kontakt s lékárníkem.</p>',
    faq=[
        ('Co je omega-3 a k čemu se používá?', 'Jde o skupinu nenasycených mastných kyselin, které tělo přijímá stravou. Doplňky stravy s omega-3 mají doplnit stravu u lidí, kteří jedí málo mořských ryb. Nejde o lék a o užívání se poraďte s lékařem.'),
        ('Čím se liší EPA a DHA?', 'Jsou to dvě hlavní omega-3 mastné kyseliny z mořských zdrojů. Na etiketě sledujte jejich součet v jedné dávce, protože to je skutečný obsah. Celkové množství oleje v kapsli o tom nevypovídá.'),
        ('Jaký je rozdíl mezi rybím a krillovým olejem?', 'Rybí olej pochází z ryb, krillový z drobných korýšů. Liší se formou vazby omega-3 a velikostí kapslí. Při alergii na ryby nebo korýše čtěte složení a konzultujte s lékařem.'),
        ('Pro vegany existuje omega-3?', 'Ano, řasový olej obsahuje EPA a DHA a je rostlinného původu. Lněný olej obsahuje ALA, kterou tělo přeměňuje jen částečně. Vždy čtěte údaje o EPA a DHA.'),
        ('Je lněný olej to samé co rybí olej?', 'Ne. Lněný olej obsahuje kyselinu alfa-linolenovou, nikoli přímo EPA a DHA. Jeho složení a využití se liší, takže ho nezaměňujte za rybí olej.'),
        ('Co znamená omega 3-6-9?', 'Jde o směs tří typů mastných kyselin. Neobsahuje obvykle tolik omega-3 jako čistý rybí olej. Při výběru sledujte množství omega-3 a způsob, jak je uvedeno na etiketě.'),
        ('Kdy a jak omega-3 užívat?', 'Obvykle s jídlem, které obsahuje tuk, protože se tak lépe vstřebává. Dávku a dobu užívání řiďte pokyny výrobce nebo radou lékárníka. Nepřekračujte doporučenou dávku.'),
        ('Mohu omega-3 užívat s léky?', 'Omega-3 mohou ovlivňovat některé léky, zejména ty na srážlivost krve. Před užíváním se vždy poraďte s lékařem nebo lékárníkem a řiďte se příbalovým textem.'),
        ('Proč kapsle páchne po rybách?', 'Silný nebo žluklý zápach může znamenat, že se olej zkazil oxidací. Neužívejte ho. Kapsle skladujte v chladu a tmě, ideálně v původním obalu, a hlídejte datum trvanlivosti.'),
        ('Jaká forma je lepší: kapsle, nebo tekutý olej?', 'Kapsle jsou pohodlné a bez chuti. Tekutý olej se snáze dávkuje po menších množstvích, ale vyžaduje chladné skladování. Záleží na tom, co vám vyhovuje.'),
        ('Mohou omega-3 užívat děti?', 'Pro děti existují přípravky s vhodnou příchutí a dávkováním, ale před užíváním je nutné poradit se s pediatrem. Dospělé přípravky dětem nedávejte.'),
    ])

# ------------------------------------------------------------------ horcik
NEW['horcik'] = dict(long=True,
    title='Hořčík (magnesium): formy, dávka v tabletě, jak vybrat',
    desc='Hořčík v tabletách, kapslích i prášku. Jak porovnat bisglycinát, citrát a malát, číst obsah prvku a vybrat doplněk. Nabídky českých obchodů.',
    intro='<p>Hořčík je minerál, který tělo potřebuje pro řadu běžných procesů, třeba pro činnost svalů a nervové soustavy. Přijímáme ho z listové zeleniny, ořechů, luštěnin, celozrnných výrobků a minerální vody. Doplňky stravy s hořčíkem se v obchodech objevují jako tablety, kapsle, šumivé tablety, prášky na rozpuštění a také jako gumoví medvídci. Jde o doplněk stravy, ne o lék, a před užíváním se vyplatí poradit se s lékařem nebo lékárníkem.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů a najdete tu značky ' + B(('gymbeam', 'GymBeam'), ('viridian', 'Viridian'), ('greenfood-nutrition', 'GreenFood Nutrition'), ('maxi-vita', 'Maxi Vita'), ('pillar-performance', 'Pillar Performance'), ('movit-energy', 'Movit Energy'), ('medpharma', 'MedPharma'), ('nordbo', 'Nordbo'), ('atp', 'ATP'), ('fitsport', 'Fitsport')) +
          '. Příbuzné látky najdete v kategorii <a href="/vitaminy-a-mineraly/">vitamíny, minerály a omega-3</a>.</p>',
    guide='<h2>K čemu hořčík v těle slouží</h2>'
          '<p>Hořčík se podílí na činnosti svalů a nervové soustavy, na tvorbě energie a na udržení normálního stavu kostí a zubů. Evropský úřad pro bezpečnost potravin schválil pro hořčík několik obecných tvrzení tohoto typu. Neznamená to, že doplněk řeší konkrétní potíže. Pokud trpíte častými křečemi, únavou nebo poruchami spánku, jde o příznaky s mnoha možnými příčinami a správný postup je návštěva lékaře, ne samoléčba.</p>'
          '<h2>Jak číst etiketu: sloučenina a obsah samotného hořčíku</h2>'
          '<p>Nejčastější past při výběru je rozdíl mezi hmotností sloučeniny a množstvím čistého hořčíku. Údaj „1000 mg citrátu hořečnatého“ neznamená 1000 mg hořčíku. Hořčík je vždy navázaný na jinou molekulu, například kyselinu citronovou nebo aminokyselinu glycin, a samotný prvek tvoří jen část hmotnosti. Hledejte proto řádek „hořčík“ nebo „elementární hořčík“ s množstvím v jedné dávce a v procentech referenční hodnoty příjmu.</p>'
          '<p>Druhý údaj, který si zaslouží pozornost, je počet kapslí nebo tablet v jedné dávce. Výrobce často uvede obsah na dvě až čtyři kapsle, zatímco jediná kapsle obsahuje zlomek. Pro férové porovnání vypočtěte cenu za dávku se stejným množstvím čistého hořčíku.</p>'
          '<h2>Formy hořčíku a jejich rozdíly</h2>'
          + T(['Forma', 'Typické vlastnosti', 'Poznámka při výběru'], [
              ['Bisglycinát (chelát)', 'hořčík navázaný na glycin, často označovaný jako šetrný k žaludku', 'častá volba pro večerní užívání a citlivý trávicí trakt'],
              ['Citrát', 'dobře rozpustný, běžný v šumivých tabletách a prášcích', 'u větších dávek může působit projímavě'],
              ['Malát', 'hořčík s kyselinou jablečnou', 'oblíbený u sportovců, často v kapslích'],
              ['Oxid hořečnatý', 'vysoký podíl prvku v hmotnosti, nižší rozpustnost', 'nejlevnější forma, u citlivých lidí může dráždit trávení'],
              ['Taurát', 'hořčík s taurinem', 'méně běžná specializovaná forma'],
              ['Triple komplex', 'směs více forem v jednom přípravku', 'přehledná etiketa je zde důležitá'],
              ['Mořský hořčík', 'hořčík z mořského zdroje', 'pro děti existují speciální varianty, čtěte dávkování']]) +
          '<p>Které formy se vstřebávají nejlépe, nelze jednoznačně říci. Studie se liší a výsledky závisí na dávce, stravě i jedinci. Kdo hledá šetrnější přípravek, často volí organické soli, kdo chce nízkou cenu, volí oxid. Konečnou volbu můžete konzultovat s lékárníkem.</p>'
          '<h2>Tablety, kapsle, šumivé tablety a prášek</h2>'
          '<ul><li><strong>Tablety a kapsle:</strong> pohodlné, snadno se berou s sebou a nemají chuť. Kapsle jsou obvykle šetrnější k čistotě složení.</li>'
          '<li><strong>Šumivé tablety:</strong> rozpustí se ve sklenici vody, často obsahují vitamin B6. Zkontrolujte sladidla a kyselinu citronovou.</li>'
          '<li><strong>Prášek a instantní nápoj:</strong> rychle se dávkuje po lžičkách, hodí se pro větší dávky a přidání do nápoje. Chuť bývá výrazná, někdy kyselá.</li>'
          '<li><strong>Shoty a tekuté formy:</strong> jednorázová dávka na cesty, často s příchutí.</li>'
          '<li><strong>Gumoví medvídci:</strong> příjemná chuť, ale obvykle obsahují cukr nebo sladidlo, což je pro některé lidi důležité.</li></ul>'
          '<h2>Hořčík s vitaminem B6, vápníkem a zinkem</h2>'
          '<p>Kombinované přípravky se prodávají pod názvy jako hořčík plus B6, vápník plus hořčík a zinek, nebo s meduňkou či šafránem. Výhodou je pohodlí: jedna tableta místo dvou. Nevýhodou je, že pevné složení nemusí odpovídat tomu, co potřebujete, a dávky jednotlivých látek se sčítají s jinými přípravky. Pokud už užíváte multivitamin, sečtěte obsah vitaminu B6 a dalších složek, protože u některých látek existují horní bezpečné limity. Přehled doplňků s dalšími minerály najdete v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a> a doplňky s mikroživinami také v <a href="/ostatni-doplnky-stravy/">ostatních doplňcích stravy</a>.</p>'
          '<h2>Pro koho se hořčík nabízí</h2>'
          '<ul><li><strong>Sportovci:</strong> při vydatném pocení se ztrácí část minerálů, a proto se hořčík objevuje spolu s <a href="/iontove-napoje/">iontovými nápoji</a> a v doplňcích pro regeneraci.</li>'
          '<li><strong>Lidé s jednostrannou stravou:</strong> kdo málo jí listovou zeleninu, ořechy a luštěniny, může doplněk zvažovat.</li>'
          '<li><strong>Ti, kdo mají velkou zátěž:</strong> stres a nedostatek spánku patří k situacím, kdy lidé po doplňcích sahají, ale doplněk sám problém neřeší.</li>'
          '<li><strong>Vegani a vegetariáni:</strong> mohou si stravu doplnit podle doporučení lékaře nebo nutričního terapeuta.</li>'
          '<li><strong>Děti a senioři:</strong> mají jiné potřeby a bezpečné dávky, takže se vždy poraďte s odborníkem.</li></ul>'
          '<h2>Kdy hořčík neužívat bez porady</h2>'
          '<p>Přebytečný hořčík vylučují ledviny, a proto lidé s onemocněním ledvin musí postupovat zvlášť opatrně a užívání konzultovat s lékařem. Hořčík může ovlivnit vstřebávání některých léků, například některých antibiotik a léků na štítnou žlázu, a proto se doporučuje dodržet časový odstup a poradit se s lékárníkem. U gravidity a kojení platí totéž. Příliš velká dávka může způsobit průjem, nevolnost nebo bolest břicha, a v takovém případě užívání omezte nebo ho přerušte.</p>'
          '<h2>Jak a kdy hořčík užívat</h2>'
          '<p>Postupujte podle pokynů na obalu. Mnoho lidí užívá hořčík večer nebo s jídlem, protože se tak snižuje riziko žaludečních potíží, ale pevné pravidlo neexistuje. Dávku lze rozdělit na více menších. Nepřekračujte doporučené množství v naději na rychlejší výsledek. Při užívání s vápníkem ve stejné dávce se obě látky vstřebávají v téže části střeva, proto některé návody doporučují je brát odděleně.</p>'
          '<h2>Hořčík ve stravě: kde ho najdete</h2>'
          '<p>Než sáhnete po doplňku, projděte si jídelníček. Hořčík obsahují dýňová a slunečnicová semínka, mandle a kešu, ovesné vločky, černé fazole, špenát a mangold, ale také tmavá čokoláda s vysokým podílem kakaa a některé minerální vody. Při vaření část minerálů přechází do vody, takže se vyplatí zeleninu spíše dusit nebo využít i vývar. Pestrý jídelníček obvykle pokrývá většinu potřeby a doplněk je jen jednou z možností, nikoli povinností. Pokud si nejste jistí, požádejte lékaře o vyšetření a řiďte se jeho radou.</p>'
          '<h2>Hořčík a sportovní doplňky v jednom plánu</h2>'
          '<p>Kdo skládá doplňky do jednoho režimu, měl by vést jednoduchý seznam: co užívá, v jaké dávce a kdy. Přehled pomůže odhalit zdvojení, třeba když hořčík obsahuje multivitamin, předtréninkový přípravek i večerní kapsle. Zdvojení nemusí být nebezpečné, ale zbytečně zvyšuje náklady a zátěž pro trávení. Při změně dávky nebo přípravku počkejte několik dní a sledujte, jak vám vyhovuje.</p>'
          '<h2>Časté chyby při výběru hořčíku</h2>'
          '<ul><li>Porovnávání podle hmotnosti sloučeniny místo podle čistého hořčíku.</li>'
          '<li>Zapomenutí na počet tablet v jedné dávce.</li>'
          '<li>Nákup nejlevnější formy a následné trávicí potíže.</li>'
          '<li>Kombinace několika přípravků s vitaminem B6, kde se dávky sčítají.</li>'
          '<li>Spoléhání na hořčík jako na řešení únavy a stresu bez úpravy režimu.</li>'
          '<li>Opomenutí, že šumivé a gumové formy mohou obsahovat cukr a sladidla.</li></ul>'
          '<h2>Značky v katalogu</h2>'
          '<p>Největší výběr nabízí ' + B(('gymbeam', 'GymBeam')) + ' s bisglycinátem, malátem, šumivými tabletami a shoty. ' + B(('viridian', 'Viridian')) + ' a ' + B(('greenfood-nutrition', 'GreenFood Nutrition')) + ' se zaměřují na čisté složení a organické formy. ' + B(('maxi-vita', 'Maxi Vita')) + ', ' + B(('pillar-performance', 'Pillar Performance')) + ' a ' + B(('pillar', 'Pillar')) + ' mají širší sortiment minerálů. ' + B(('movit-energy', 'Movit Energy')) + ', ' + B(('medpharma', 'MedPharma')) + ', ' + B(('nordbo', 'Nordbo')) + ', ' + B(('atp', 'ATP')) + ', ' + B(('fitsport', 'Fitsport')) + ' a ' + B(('ostrovit', 'OstroVit')) + ' doplňují nabídku o další tablety, kapsle a prášky. U každého přípravku čtěte konkrétní etiketu.</p>'
          '<h2>Jak ušetřit při nákupu hořčíku</h2>'
          '<p>Porovnávejte cenu za dávku se stejným obsahem čistého hořčíku, ne cenu za balení. Velká balení bývají hospodárnější, ale jen pokud je stihnete spotřebovat. Sporteka zobrazuje nabídky více obchodů vedle sebe u stejného produktu, takže snadno uvidíte rozdíly. Přípravky s příchutí, extrakty a doplňkem navíc bývají dražší a nemusí být užitečnější než jednoduchá kapsle. Pokud už užíváte multivitamin, ověřte, zda hořčík neobsahuje a zda přidávat další opravdu potřebujete. Ostatní doplňky ke zvážení najdete v sourozenecké kategorii <a href="/omega-3/">omega-3 a rybí olej</a>.</p>'
          '<h2>Hořčík mezi dalšími doplňky a sportovní výživou</h2>'
          '<p>K regeneraci patří spánek, pitný režim a vyvážená strava. Pro další inspiraci projděte <a href="/sportovni-vyziva/">sportovní výživu</a>, <a href="/kolagen-a-klouby/">kolagen a kloubní výživu</a>, <a href="/ashwagandha/">ashwagandhu</a> nebo <a href="/aminokyseliny-bcaa/">aminokyseliny</a>. Doplněk má stravu doplnit, ne nahradit. Při nejasnostech se obraťte na lékaře, lékárníka nebo nutričního terapeuta.</p>',
    faq=[
        ('K čemu je hořčík dobrý?', 'Hořčík se podílí na činnosti svalů a nervové soustavy a na tvorbě energie. Doplňky stravy slouží k doplnění stravy, ne k léčbě. Při potížích, jako jsou časté křeče, vyhledejte lékaře.'),
        ('Jaká forma hořčíku je nejlepší?', 'Jednoznačná odpověď neexistuje. Bisglycinát bývá považován za šetrný k žaludku, citrát je dobře rozpustný, oxid je levný, ale může dráždit trávení. Rozhodněte podle snášenlivosti a po poradě s lékárníkem.'),
        ('Jak poznám skutečný obsah hořčíku?', 'Hledejte na etiketě řádek s množstvím čistého hořčíku v jedné dávce. Údaj o hmotnosti sloučeniny, třeba citrátu, je jiný. Sledujte také, kolik tablet tvoří jednu dávku.'),
        ('Kdy hořčík užívat, ráno, nebo večer?', 'Pevné pravidlo není. Řada lidí volí večer nebo užívání s jídlem, aby předešla žaludečním potížím. Řiďte se pokyny výrobce a radou lékárníka.'),
        ('Může hořčík způsobit průjem?', 'Ano, u vyšších dávek a u některých forem, například citrátu a oxidu, může působit projímavě. Pomůže snížit dávku, rozdělit ji nebo zvolit šetrnější formu. Při přetrvávání potíží přestaňte a poraďte se s lékařem.'),
        ('Mohu užívat hořčík s vitaminem B6?', 'Kombinované přípravky existují a jsou běžné. Pozor na součet vitaminu B6 z více přípravků, protože u něj platí horní bezpečné limity. Dávky si zkontrolujte na etiketách.'),
        ('Je hořčík vhodný pro sportovce?', 'Sportovci hořčík často užívají, protože při pocení část minerálů ztrácejí. Pestrá strava a pitný režim jsou základ. O doplnění rozhodněte po poradě s lékařem nebo nutričním terapeutem.'),
        ('Kdo by měl být s hořčíkem opatrný?', 'Opatrnost platí u lidí s onemocněním ledvin, u těhotných a kojících žen, u dětí a u těch, kdo užívají léky. Vždy se předem poraďte s lékařem nebo lékárníkem.'),
        ('Vstřebává se lépe prášek, nebo tableta?', 'Záleží hlavně na formě hořčíku a na tom, jak ho snášíte, ne na tvaru přípravku. Prášek se dobře dávkuje, tablety a kapsle jsou praktické na cesty. Vyberte, co vám vyhovuje.'),
        ('Mohu hořčík kombinovat s vápníkem a zinkem?', 'Kombinované přípravky existují. Některé návody doporučují brát minerály s odstupem, protože si mohou konkurovat při vstřebávání. Pokyny najdete na obalu, případně se zeptejte lékárníka.'),
        ('Jak hořčík skladovat?', 'Na suchém, chladném místě v původním uzavřeném obalu mimo dosah dětí. Prášky a šumivé tablety chraňte před vlhkostí. Sledujte datum minimální trvanlivosti.'),
    ])
