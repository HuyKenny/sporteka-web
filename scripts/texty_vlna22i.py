"""sporteka.cz — wave 22i (4. 11. 2026): long texts for sportovni-hodinky, prvni-pomoc, trekingova-kola, squash.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ sportovni-hodinky
NEW['sportovni-hodinky'] = dict(long=True,
    title='Sportovní hodinky: GPS, chytré, dětské i příslušenství',
    desc='Sportovní a chytré hodinky s GPS, pulzem a AMOLED displejem, hrudní pásy, řemínky a nabíječky. Jak vybrat a porovnat nabídky českých obchodů.',
    intro='<p>Kategorie sportovních hodinek je ve skutečnosti směs několika světů. Najdete tu běžecké a multisportovní GPS hodinky pro trénink, chytré hodinky pro každodenní nošení, dětské modely s volaním a polohou, ale také hrudní pásy, přijímače tepu, náhradní řemínky a nabíjecí kabely. Společné mají to, že mají na zápěstí pomáhat s pohybem, spánkem, navigací nebo oznámeními z telefonu.</p>'
          '<p>Sporteka porovnává nabídky sportovních e-shopů u značek jako '
          + B(('garmin', 'Garmin'), ('huawei', 'Huawei'), ('suunto', 'Suunto'), ('samsung', 'Samsung'), ('apple', 'Apple'), ('amazfit', 'Amazfit'), ('polar', 'Polar'), ('insportline', 'Insportline'), ('watchmark', 'Watchmark')) +
          '. Hodinky se často kupují společně s vybavením pro <a href="/beh/">běh</a>, <a href="/cyklistika/">cyklistiku</a>, <a href="/triatlon/">triatlon</a> nebo <a href="/fitness/">fitness</a>, proto vás dole navedeme na související kategorie. Text vás provede typy zařízení, funkcemi, které se opravdu využijí, i chybami, kvůli kterým se hodinky po měsíci vrací do šuplíku.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Než začnete porovnávat konkrétní modely, ujasněte si, jaký druh zařízení vlastně hledáte. Nabídka se dá rozdělit do několika skupin, které se liší účelem, výdrží baterie i způsobem ovládání.</p>'
          + T(['Skupina', 'K čemu slouží', 'Typický uživatel'], [
              ['Běžecké GPS hodinky', 'záznam tempa, vzdálenosti, tréninkové plány', 'běžec od začátečníka po závodníka'],
              ['Multisportovní a outdoorové hodinky', 'navigace, výškoměr, dlouhá výdrž, odolné tělo', 'turista, horolezec, ultratrailový běžec'],
              ['Chytré hodinky', 'oznámení, platby, hovory, základní sport', 'člověk, který chce jedno zařízení na všechno'],
              ['Dětské chytré hodinky', 'volání rodičům, poloha, jednoduché funkce', 'školák a rodič, který chce mít přehled'],
              ['Hrudní pásy a přijímače', 'přesnější měření tepu při zátěži', 'trénink podle tepových zón'],
              ['Příslušenství', 'řemínky, nabíjecí kabely, kryty', 'majitel hodinek, který řeší údržbu']]) +
          '<p>Rozdělení je důležité hlavně proto, že cena nabídky nic neříká o vhodnosti. Špičkový outdoorový model je pro někoho zbytečně složitý, zatímco jednoduché chytré hodinky se nemusejí hodit k dlouhým výletům, protože je budete nabíjet každý den či dva.</p>'
          '<h2>GPS a přesnost záznamu</h2>'
          '<p>GPS je základ pro každého, kdo chce znát skutečnou trasu a tempo. Hodinky bez vlastního přijímače se spoléhají na telefon v kapse, což funguje, dokud ho neodložíte. Vestavěná GPS umožní vyběhnout jen s hodinkami a trasu pak najdete v aplikaci. Novější modely umějí víc družicových systémů současně a lépe si poradí v hustém lese nebo mezi vysokými budovami.</p>'
          '<p>Záznam polohy se vždy trochu odchyluje, zvlášť v kaňonech ulic a pod stromy. Pro běžný trénink to nevadí, pro závodní měření vzdáleností počítejte s tím, že každý přístroj může ukázat jiný výsledek. Pokud chcete stabilnější data, počkejte po zapnutí na zachycení signálu a teprve pak vyrazte.</p>'
          '<h2>Měření tepu na zápěstí a hrudní pás</h2>'
          '<p>Optický snímač na zadní straně hodinek svítí do kůže a z odrazu světla odhaduje tep. Pro chůzi, klidový tep a pravidelný běh je dostačující. U intervalů, silového tréninku a při chladném počasí může být nepřesný, protože za rychlými změnami tepu zaostává. Hrudní pás, například <a href="/znacka/garmin/">Garmin</a> HRM, měří elektrickou aktivitu srdce a bývá při intenzivním cvičení spolehlivější.</p>'
          '<p>Hrudní pás potřebuje kompatibilní hodinky nebo cyklopočítač, takže před nákupem ověřte, zda používá Bluetooth nebo ANT+. K pásu patří i správná péče: navlhčit elektrody, po použití omýt a nenechávat ho zmačkaný v tašce. Při zdravotních potížích se srdcem rozhoduje lékař, hodinky nejsou zdravotnický prostředek.</p>'
          '<h2>Displej: AMOLED, nebo paměťový</h2>'
          '<p>AMOLED displej je jasný, barevný a výborně čitelný uvnitř, na slunci ale spotřebuje víc energie. Paměťový displej (MIP) je méně efektní, zato při přímém světle čitelný a velmi úsporný. Nové hodinky pro každodenní nošení volí většinou AMOLED, outdoorové modely nabízejí obě varianty a dlouhodobě sázejí na výdrž. Při výběru zkuste představit, kde budete na hodinky koukat nejčastěji: v posilovně, při běhu v poledne, nebo v noci s čelovkou.</p>'
          '<h2>Výdrž baterie a nabíjení</h2>'
          '<p>Výdrž se zásadně liší podle režimu. Chytrý režim s oznámeními vydrží jiný počet dní než nepřetržité GPS a hudba. Výrobci uvádějí několik scénářů, proto porovnávejte stejný režim u obou kandidátů. Pro víkendové túry a vícedenní akce hledejte režimy s úsporným GPS a solární dobíjení, pro městské nošení stačí nabíjení každé dva tři dny.</p>'
          '<p>Nabíjecí kabely bývají pro každou značku jiné, často magnetické nebo na kontakty. Pokud kabel ztratíte, univerzální nabíječka nepomůže, proto mějte v zásobě originální nebo kompatibilní kabel. Na delší cesty se hodí <a href="/powerbanky-a-nabijeni/">powerbanka</a> s dostatečným výkonem.</p>'
          '<h2>Výběr podle sportu</h2>'
          '<p>Každý sport klade jiné nároky na funkce. Následující přehled pomáhá odfiltrovat zbytečné.</p>'
          '<ul><li><strong>Běh:</strong> tempo, intervalové tréninky, měření kadence, tréninkové plány a odhad zotavení. Hodí se lehké tělo a pohodlný silikonový řemínek.</li>'
          '<li><strong>Cyklistika:</strong> propojení se senzory výkonu a rychlosti, ale pro dlouhé jízdy a navigaci je lepší samostatný <a href="/cyklo-computery/">cyklopočítač</a>.</li>'
          '<li><strong>Plavání:</strong> vodotěsnost, počítání délek a záběrů. Ověřte, že hodinky umějí režim bazénu i otevřené vody. Související sortiment najdete v <a href="/plavecke-pomucky/">plaveckých pomůckách</a>.</li>'
          '<li><strong>Turistika a horolezectví:</strong> kompas, barometr, výškoměr, záznam tras a odolné sklo. Návazné vybavení je v kategorii <a href="/outdoor/">outdoor</a> a <a href="/horolezectvi/">horolezectví</a>.</li>'
          '<li><strong>Triatlon:</strong> multisportovní profil s přepínáním disciplín a přechodovými zónami, viz <a href="/triatlon/">triatlon</a>.</li>'
          '<li><strong>Fitness a posilovna:</strong> počítání sérií, tep, spalování a doba zotavení. Pro domácí cvičení se hodí i <a href="/kardio-trenazery/">kardio trenažery</a>.</li>'
          '<li><strong>Golf a lyže:</strong> specializované profily jsou na vybraných modelech, takže je potřeba ověřit popis. Viz <a href="/golf/">golf</a> a <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</li></ul>'
          '<h2>Chytré hodinky versus sportovní hodinky</h2>'
          '<p>Hranice se stírá, přesto rozdíly existují. Chytré hodinky od <a href="/znacka/apple/">Applu</a>, <a href="/znacka/samsung/">Samsungu</a> či <a href="/znacka/huawei/">Huawei</a> staví na aplikacích, platbách, odpovídání na zprávy a zdravotních funkcích. Sportovní řady <a href="/znacka/garmin/">Garminu</a>, <a href="/znacka/suunto/">Suunta</a> nebo <a href="/znacka/polar/">Polaru</a> se soustředí na trénink, regeneraci a výdrž, a naopak nabízejí méně aplikací třetích stran.</p>'
          '<p>Důležitá je i kompatibilita s telefonem. Některé funkce, například odpovědi na zprávy nebo platby, fungují jinak na iPhonu a na Androidu. Před koupí si ověřte, jaký telefon máte, a přečtěte si popis, který operační systém hodinky podporují. Pokud sdílíte zařízení v rodině, zvažte, zda jeden telefon obslouží i dvoje hodinky.</p>'
          '<h2>Dětské hodinky</h2>'
          '<p>Dětské chytré hodinky, například řady Cubbio nebo Bounce, spojují volání, zprávy a polohu. Obvykle potřebují SIM kartu s datovým tarifem, někdy i aplikaci v telefonu rodiče. Dobře se ovládají, mají odolné pouzdro a barevný řemínek. Ověřte si výdrž baterie, kvalitu výrobce a zabezpečení údajů dítěte. Pro mladší děti bývá užitečnější jednoduchý model, u starších se hodí sledování pohybu a spánku.</p>'
          '<h2>Řemínky, folie a další příslušenství</h2>'
          '<p>Řemínek je nejsnadněji vyměnitelná součást a zároveň ta, která se nejvíc opotřebí. Silikon vydrží pot i vodu, nylonové a textilní provedení jsou prodyšné, kožené a kovové řemínky se hodí do kanceláře. Při koupi sledujte šířku v milimetrech a způsob uchycení, například rychlozámek, klasický kolík nebo systém konkrétní značky. Insportline a další výrobci nabízejí náhradní řemínky pro konkrétní modely; ověřte, že souhlasí název vašich hodinek.</p>'
          '<p>Mezi doplňky patří ochranné fólie, kryty, stolní nabíječky a přijímače k hrudnímu pásu. Nezapomeňte, že čisté zadní sklíčko a kůže bez krému zlepšují měření tepu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ol><li>Kupovat nejvybavenější model, přestože se použije jen malá část funkcí.</li>'
          '<li>Ignorovat velikost pouzdra. Příliš velké hodinky na tenké zápěstí se při běhu kývají a kazí měření tepu.</li>'
          '<li>Neověřit kompatibilitu s telefonem a aplikacemi, které už používáte.</li>'
          '<li>Porovnávat výdrž v různých režimech, takže se zdá, že dva modely se liší, i když jsou stejné.</li>'
          '<li>Spoléhat se na hodinky jako na lékařský přístroj a vyvozovat z nich diagnózy.</li>'
          '<li>Zapomenout na řemínek. Nepohodlný pásek rozhodne víc než funkce.</li></ol>'
          '<h2>Jak číst nabídky a kdy nakupovat</h2>'
          '<p>Stejný model se v obchodech liší barvou, velikostí pouzdra a edicí. Garmin například vydává jednu řadu ve 42 a 47 milimetrech, s hudbou a bez ní, takže jen podle názvu poznáte rozdíl špatně. Zkontrolujte celý popis, zda v ceně je nabíjecí kabel a zda je verze určená pro český trh. Na stránce každého produktu na Sportece vidíte nabídky více obchodů a vývoj ceny, což usnadní rozhodnutí, zda čekat na slevu.</p>'
          '<p>Po příchodu nové generace starší řada obvykle zlevní. Starší model často nabídne téměř stejné funkce, a přitom je znatelně dostupnější. Pokud nehledáte nejnovější senzor, stojí za to porovnat i loňskou verzi.</p>'
          '<h2>Péče o hodinky</h2>'
          '<p>Po sportu hodinky opláchněte čistou vodou, zejména po plavání v chlorované nebo slané vodě, a osušte. Nečistěte je agresivními chemikáliemi. Řemínek občas sundejte, aby kůže pod ním dýchala. Aktualizujte software, protože výrobci tím zlepšují přesnost a stabilitu. Před dlouhým skladováním nabijte baterii zhruba na polovinu a ukládejte na suchém místě.</p>'
          '<h2>Pro koho jsou hodinky nejvhodnější</h2>'
          '<p>Začátečníkovi stačí jednoduché GPS hodinky s tepem a přehlednou aplikací. Ambiciózní běžec ocení tréninkové plány a regeneraci. Turista a horolezec potřebuje výdrž a odolné tělo. Člověk, který chce hlavně oznámení a platby, zvolí chytré hodinky. Rodiče malých dětí zvažují dětský model. Kdo hodinky už má, často potřebuje jen řemínek, kabel nebo hrudní pás.</p>'
          '<p>Jestli sháníte celkový set pro sezónu, projděte i <a href="/sportovni-vyziva/">sportovní výživu</a>, <a href="/bezecke-opasky/">běžecké opasky</a> a <a href="/bezecke-vesty-a-batohy/">běžecké vesty</a>, které s hodinkami tvoří běžnou výbavu na delší trasy.</p>',
    faq=[
        ('Potřebuji GPS, když běhám jen po parku?', 'Pokud nosíte telefon, nemusíte. Vlastní GPS ale dává přesnější tempo a trasu bez telefonu v ruce či v kapse, což se při pravidelném běhání rychle oceňuje.'),
        ('Je rozdíl mezi chytrými a sportovními hodinkami?', 'Ano. Chytré hodinky staví na aplikacích, oznámeních a platbách. Sportovní se soustředí na trénink, navigaci a výdrž. Řada modelů obě oblasti kombinuje, takže záleží na tom, co používáte nejčastěji.'),
        ('Jak dlouho vydrží baterie?', 'Podle režimu od jednoho dne po několik týdnů. Rozhoduje displej, GPS, hudba a počet oznámení. Porovnávejte údaje výrobců ve stejném režimu a počítejte s tím, že skutečná výdrž bývá kratší.'),
        ('Je měření tepu na zápěstí přesné?', 'Pro klidový stav a stabilní tempo obvykle postačuje. Při intervalech, silovém tréninku nebo v zimě může zaostávat, a proto se pro přesnější data používá hrudní pás.'),
        ('Dají se s hodinkami plavat?', 'Jen s těmi, které mají odpovídající vodotěsnost a plavecký režim. Informaci hledejte v technické specifikaci. Po koupání v moři nebo v bazénu hodinky opláchněte sladkou vodou.'),
        ('Jak poznám správný řemínek?', 'Podle šířky v milimetrech a typu uchycení. U původních řemínků pomůže název modelu, u univerzálních je potřeba změřit vzdálenost mezi výstupky pouzdra.'),
        ('Fungují hodinky s iPhonem i s Androidem?', 'Většina ano, ale některé funkce se liší. Hodinky Apple Watch jsou určené k iPhonu, Galaxy Watch se nejlépe chovají s Androidem. U jiných značek si ověřte kompatibilitu v popisu.'),
        ('Jsou dětské hodinky bezpečné?', 'Záleží na výrobci, zabezpečení a nastavení rodičovské aplikace. Doporučujeme zvolit známější značku, nastavit silné heslo a vysvětlit dítěti, jak s hodinkami zacházet.'),
        ('Mohu s hodinkami diagnostikovat zdravotní problémy?', 'Ne. Údaje o tepu, spánku nebo kyslíku jsou orientační. Při obtížích se vždy poraďte s lékařem, hodinky ho nenahradí.'),
        ('Kdy se vyplatí starší generace?', 'Pokud nepotřebujete nejnovější senzor ani displej. Předchozí řada nabízí podobné funkce a po uvedení nástupce se často objeví v obchodech za výhodnějších podmínek.'),
    ])

# ------------------------------------------------------------------ prvni-pomoc
NEW['prvni-pomoc'] = dict(long=True,
    title='Lékárničky a první pomoc na výlet, kolo i do batohu',
    desc='Outdoorové lékárničky, pouzdra IFAK, izotermické fólie a doplňky první pomoci. Jak vybrat velikost, obsah a obal a porovnat nabídky obchodů.',
    intro='<p>Do této kategorie patří hlavně cestovní a outdoorové lékárničky, tedy kompaktní sady v nepromokavém obalu, které se vejdou do batohu, na kolo nebo do auta. Vedle hotových sad tu najdete prázdná pouzdra na lékárničku, modulární vložky s úchyty MOLLE, náplně se spotřebním materiálem, izotermické fólie a drobné doplňky. Kategorie je tedy hodně praktická: kdo chodí do hor, kempuje nebo jezdí s dětmi, dřív nebo později něco z toho potřebuje.</p>'
          '<p>Sporteka porovnává nabídky obchodů u značek jako '
          + B(('lifesystems', 'Lifesystems'), ('tatonka', 'Tatonka'), ('deuter', 'Deuter'), ('tasmanian-tiger', 'Tasmanian Tiger'), ('helikon-tex', 'Helikon-Tex'), ('mil-tec', 'Mil-tec'), ('rothco', 'Rothco'), ('ortovox', 'Ortovox')) +
          '. Následující text je obecný přehled, nenahrazuje školení první pomoci ani radu lékaře a neuvádí žádná zdravotní doporučení k léčbě. Pomůže vám ale vybrat správnou velikost sady, rozumně ji doplnit a nezapomenout na údržbu.</p>',
    guide='<h2>Jaké druhy lékárniček a doplňků se nabízejí</h2>'
          '<p>Při pohledu na nabídku se zdá, že lékárnička je jen červená taška s křížem. Ve skutečnosti se jednotlivé typy liší velikostí, způsobem nošení i tím, na koho jsou zaměřené.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se na'], [
              ['Mini a kapesní sady', 'několik náplastí a základní materiál, hmotnost pár desítek gramů', 'běh, krátký výlet, kolo'],
              ['Lékárničky do batohu', 'nepromokavý obal, přihrádky, střední kapacita', 'celodenní túry, víkend'],
              ['Rodinné a kempingové sady', 'větší kapacita, pro více osob', 'stan, karavan, dovolená'],
              ['Expediční a leader sady', 'rozsáhlé vybavení pro skupiny', 'vedoucí kurzů, horské akce'],
              ['Pouzdra IFAK a MOLLE', 'prázdný obal s úchyty na výstroj', 'taktické vybavení, airsoft, outdoor'],
              ['Izotermické fólie a doplňky', 'lehká fólie, náplně, jednotlivé položky', 'doplnění sady, nouzové zakrytí']]) +
          '<p>V nabídce uvidíte i hotové sady řady Lifesystems, například Mountain, Trek, Camping nebo Bike, které rozlišují účel v názvu. Název je dobré brát jen jako hrubé vodítko. Obsah vždy porovnejte s tím, co budete při akci opravdu dělat.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Správná velikost vychází z délky akce, počtu lidí a vzdálenosti od pomoci. Na hodinový výlet po okolí stačí kapesní sada, na vícedenní expedici nebo skupinu už ne. Příliš velká lékárnička se naopak zbytečně nosí a často zůstane doma.</p>'
          '<ul><li><strong>Počet osob:</strong> sady jsou obvykle určené pro jednoho, dva nebo rodinu. Rodinné modely, například Tatonka First Aid Family, počítají s víc lidmi.</li>'
          '<li><strong>Délka akce:</strong> víkend vyžaduje víc materiálu než dvouhodinová procházka.</li>'
          '<li><strong>Dostupnost pomoci:</strong> v horách a mimo signál je užitečnější větší výbava.</li>'
          '<li><strong>Hmotnost a objem:</strong> u lehkého balení, třeba na běh nebo trek, dává smysl řadit mikro varianty.</li>'
          '<li><strong>Zkušenosti:</strong> jen to, co umíte použít, dává smysl nosit.</li></ul>'
          '<h2>Co obvykle obsahuje základní sada</h2>'
          '<p>Obsah se liší podle výrobce, ale v typické outdoorové sadě najdete náplasti různých velikostí, sterilní krytí, obinadlo, fixační pásku, rukavice, nůžky, pinzetu, trojcípý šátek nebo jeho náhradu a stručný návod. Některé sady obsahují i dezinfekci, izotermickou fólii a píšťalku. Přesný seznam položek vždy zkontrolujte u produktu, protože hotové sady se v různých obchodech mohou lišit.</p>'
          '<p>Žádná výbava nenahradí znalosti. Kurz první pomoci, který pořádá například zdravotnická organizace, naučí zacházet s materiálem a rozhodnout, kdy volat záchrannou službu. U léků a zdravotních potřeb vždy respektujte pokyny na obalu a poraďte se s lékařem nebo lékárníkem, zvlášť pokud užíváte pravidelnou léčbu nebo máte alergie.</p>'
          '<h2>Obal: nepromokavý, textilní, nebo pouzdro s úchyty</h2>'
          '<p>Obal je na lékárničce stejně důležitý jako obsah. Vlhkost, prach a otřesy dokážou zničit sterilitu balení, a pokud má obal špatný zip, nic nepomůže. Nepromokavé obaly se svařenými švy nebo ventilem uzavřou obsah před deštěm a potem. Textilní pouzdra bývají lehká a přehledná. Pouzdra na úchyty MOLLE se upevňují na batoh nebo vestu a mají rychlé otevírání.</p>'
          + T(['Obal', 'Výhoda', 'Pozor na'], [
              ['Nepromokavý (dry bag styl)', 'chrání proti vodě a vlhku', 'obvykle méně přihrádek'],
              ['Textilní s přihrádkami', 'přehledný, lehký', 'u vlhkého prostředí potřebuje sáček'],
              ['Pouzdro MOLLE / IFAK', 'upevnění na batoh nebo opasek', 'bývá prázdné, obsah doplníte sami'],
              ['Rolovací organizér', 'dobře se rozloží a vidíte vše', 'zabírá víc prostoru v batohu'],
              ['Pevný box', 'chrání proti rozdrcení', 'vyšší hmotnost']]) +
          '<p>Při výběru z nabídek značek <a href="/znacka/tasmanian-tiger/">Tasmanian Tiger</a>, <a href="/znacka/helikon-tex/">Helikon-Tex</a> nebo <a href="/znacka/direct-action/">Direct Action</a> si všimněte, že mnohé produkty jsou jen pouzdra. Název „lékárnička“ nemusí znamenat, že je uvnitř materiál. Čtěte popis a podívejte se na fotografii.</p>'
          '<h2>IFAK a taktická pouzdra: co to je</h2>'
          '<p>Zkratka IFAK označuje individuální lékárničku, kterou voják nebo outdoorista nosí přímo na výstroji. V nabídce jsou především prázdná pouzdra a sady s minimálním obsahem. Používají je airsoftoví hráči, lovci, bushcrafteři i lidé, kteří chtějí mít materiál na dosah ruky. Mají dobré uchycení, rychlé otevření a trhací panel. Pokud hledáte běžnou rodinnou lékárničku, tyto modely nejsou tím správným výchozím bodem.</p>'
          '<h2>Výběr podle aktivity</h2>'
          '<p>Různé sporty vyžadují různou výbavu a jiný způsob nošení. Uvedené tipy jsou obecné a nejsou lékařskou radou.</p>'
          '<ul><li><strong>Turistika:</strong> kompaktní sada v batohu, viz <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/outdoor/">outdoor</a>. Sada by měla mít odolný obal a dobře čitelný seznam.</li>'
          '<li><strong>Kolo:</strong> malá sada do brašny nebo kapsy, doplněná o pár dalších drobností. Související kategorie: <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>, <a href="/cyklistika/">cyklistika</a>.</li>'
          '<li><strong>Kempování:</strong> větší sada pro rodinu v autě nebo ve stanu, viz <a href="/kemping/">kemping</a> a <a href="/stany/">stany</a>.</li>'
          '<li><strong>Horolezectví a skialpinismus:</strong> kompaktní, odolná výbava s izotermickou fólií, viz <a href="/horolezectvi/">horolezectví</a> a <a href="/skialpinismus/">skialpinismus</a>. Značka Ortovox nabízí rolovací sady Doc, které se hodí k lavinovému vybavení.</li>'
          '<li><strong>Cestování s dětmi:</strong> samostatná sada, ve které jsou drobnosti pro děti. Dětské sady, například Little Life a Tatonka School, jsou barevné a přehledné.</li>'
          '<li><strong>Běh a trail:</strong> miniaturní balení do vesty, viz <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>.</li></ul>'
          '<h2>Izotermická fólie a další pomocné prostředky</h2>'
          '<p>Izotermická fólie je tenká metalizovaná plachta, která se při nouzi používá k zakrytí osoby proti větru, dešti a ztrátě tepla. Váží minimum a v batohu zabere málo místa, proto je součástí mnoha sad. Existují jednorázové varianty i silnější, vícekrát použitelné modely. Fólie se nehodí jako náhrada spacáku, ale v nouzi pomůže překlenout čas, než přijde pomoc.</p>'
          '<p>Do kategorie patří také doplňkové materiály a prostředky pro péči o drobná zranění, například náplasti na puchýře, přírodní náplasti či obvazy. U kosmetických a přírodních produktů vždy zkontrolujte, k čemu jsou výrobcem určené. Pro péči o nohy a ochranu před sluncem a hmyzem se podívejte do kategorie <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>. Při poranění kloubů se informujte v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, případně u lékaře.</p>'
          '<h2>Skladování a uložení v praxi</h2>'
          '<p>I dobře vybavená sada selže, když leží na špatném místě. V batohu ji dejte do horní kapsy nebo hned pod víko, aby byla po ruce bez vyndávání všeho ostatního. Na kole se osvědčila brašna pod sedlem nebo rámová taška, kde se obsah netluče. V autě patří lékárnička k místu, které je dostupné i po nehodě, nikoli pod zavazadla. Velké teplotní výkyvy poškozují lepidlo náplastí i plastové obaly, takže v létě nenechávejte sadu přes den na přímém slunci.</p>'
          '<p>Vyplatí se také označit sadu viditelnou barvou nebo reflexním prvkem a říct ostatním členům výpravy, kde leží. V nouzi nemá smysl, aby jen jeden člověk věděl, kde je lékárnička. Kdo vede děti nebo skupinu, může k sadě přiložit kartičku s důležitými telefonními čísly a údaji o alergiích a pravidelné léčbě členů skupiny.</p>'
          '<h2>Jak lékárničku udržovat</h2>'
          '<p>Lékárnička není předmět, který se koupí a zapomene. Spotřební materiál má datum použitelnosti a obaly časem vysychají. Dvakrát ročně, například před jarní a před podzimní sezónou, sadu otevřete, zkontrolujte kompletnost a vyměňte, co expiruje. Zkontrolujte také baterie v případné svítilně a čitelnost návodu.</p>'
          '<ol><li>Vyndejte obsah a zkontrolujte data použitelnosti.</li>'
          '<li>Doplňte spotřebované kousky, hlavně náplasti a rukavice.</li>'
          '<li>Prohlédněte obal, zipy a švy.</li>'
          '<li>Vložte osobní věci, například léky pro členy rodiny, které užívají pravidelně, po konzultaci s lékařem.</li>'
          '<li>Sadu uložte tam, kde ji najdete: na stejném místě v batohu, v autě nebo na kole.</li></ol>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je koupě sady podle vzhledu a ceny, aniž by si člověk přečetl obsah. Další problém nastává u přeplněných lékárniček, kde se nic nedá najít, a u příliš malých, které nestačí. Často se zapomíná na individuální potřeby: alergici, diabetici a lidé s chronickými potížemi musí svoji výbavu řešit s lékařem. Také se podceňuje nepromokavost. V dešti vlhne papír, náplasti a sterilní krytí.</p>'
          '<p>Časté je i zakoupení pouzdra bez obsahu v domnění, že je kompletní. U kategorie jako je tato pomáhá srovnání: ve stránce produktu na Sportece uvidíte nabídky více obchodů, takže snadno zjistíte, který prodejce nabízí kompletní sadu a který jen obal.</p>'
          '<h2>Pro koho se sady hodí a kde ještě hledat</h2>'
          '<p>Základní sadu potřebuje každý, kdo tráví čas v přírodě, na kole nebo s dětmi. Skupiny a vedoucí kurzů volí větší sady a pravidelně je doplňují. Fanoušci taktického vybavení hledají pouzdra a vložky. Pokud sestavujete výbavu na delší cestu, vyplatí se podívat také na <a href="/outdoor-doplnky/">outdoorové doplňky</a>, <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoola</a> a <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>',
    faq=[
        ('Jakou lékárničku vzít na jednodenní výlet?', 'Obvykle stačí kompaktní sada s náplastmi, sterilním krytím a základním materiálem. Důležité je zvolit nepromokavý obal a vědět, co v něm máte.'),
        ('Je lepší koupit hotovou sadu, nebo si ji poskládat?', 'Hotová sada šetří čas a bývá přehledná. Vlastní skladba umožní přizpůsobit obsah akci, ale vyžaduje znalosti. Pro začátek volí většina lidí hotovou sadu a časem ji doplní.'),
        ('Jak často kontrolovat obsah?', 'Alespoň dvakrát ročně a vždy před delší cestou. Zkontrolujte data použitelnosti, kompletnost a stav obalu.'),
        ('Co znamená zkratka IFAK?', 'Označuje individuální lékárničku nošenou na výstroji. V nabídce jde často o pouzdra s uchycením MOLLE, která mohou být prázdná.'),
        ('Je izotermická fólie nutná?', 'Není povinná, ale je lehká a levná a nepromokavě chrání před větrem a chladem. Proto ji mnoho outdoorových sad obsahuje.'),
        ('Mohu do lékárničky přidat léky?', 'Ano, ale vždy podle doporučení lékaře nebo lékárníka a s ohledem na expiraci a podmínky skladování. Tento text žádné léky nedoporučuje.'),
        ('Hodí se rodinná lékárnička na kolo nebo do batohu?', 'Spíše ne. Rodinné modely jsou větší a těžší. Na kolo a krátké túry se hodí menší sady, které se vejdou do brašny nebo kapsy.'),
        ('Jak poznám, že je pouzdro prázdné?', 'Podle popisu produktu a fotografie. Názvy jako pouzdro, obal, carrier nebo pouch obvykle označují prázdný obal, kdežto kit nebo set znamená, že obsahuje materiál.'),
        ('Nahradí sada kurz první pomoci?', 'Ne. Materiál je užitečný, jen když víte, jak ho použít. Absolvujte kurz u zdravotnické organizace a v nouzi volejte záchrannou službu.'),
        ('Kam ukládat lékárničku v autě nebo doma?', 'Na suché, dostupné místo mimo extrémní teploty a mimo dosah malých dětí. Při přímém slunci a v horkém autě se materiál a léky mohou zhoršit.'),
    ])

# ------------------------------------------------------------------ trekingova-kola
NEW['trekingova-kola'] = dict(long=True,
    title='Trekingová a městská kola: krosová, dámská, do města',
    desc='Trekingová, krosová, městská a dámská kola s 28 koly a přehazovačkou. Jak vybrat rám, velikost, převody a výbavu a porovnat nabídky obchodů.',
    intro='<p>Trekingová a městská kola jsou univerzální dopravní prostředek pro dojíždění, víkendové výlety i cykloturistiku po cyklostezkách. Mají pohodlnější posez než horské nebo silniční kolo, kola velikosti 28 palců, často blatníky, nosič a osvětlení. Nabídka na Sportece zahrnuje tři podkategorie: <a href="/mestska-kola/">městská kola</a>, <a href="/krosova-kola/">krosová kola</a> a <a href="/damska-kola/">dámská kola</a>. Najdete tu také skládací kola, koloběžky pro dospělé a drobné doplňky, které sem prodejci řadí.</p>'
          '<p>Porovnáváme nabídky obchodů u značek '
          + B(('davi', 'Davi'), ('storm', 'Storm'), ('author', 'Author'), ('kellys', 'Kellys'), ('prophete', 'Prophete'), ('kross', 'Kross'), ('btwin', 'Btwin'), ('specialized', 'Specialized'), ('canellini', 'Canellini')) +
          '. Dále vás provedeme rozdíly mezi typy kol, výběrem velikosti rámu, převodů a materiálu, běžnými chybami při nákupu a údržbou. Pokud váháte nad pohonem, podívejte se i na <a href="/trekingova-elektrokola/">trekingová elektrokola</a> a <a href="/mestska-elektrokola/">městská elektrokola</a>.</p>',
    guide='<h2>Typy kol v této kategorii</h2>'
          '<p>Název „trekingové“ se používá volně, a proto je dobré vědět, co za ním prodejce myslí. Rozdíly mezi typy jsou zejména v poloze těla, výbavě a odolnosti rámu.</p>'
          + T(['Typ', 'Charakter', 'Pro koho'], [
              ['Městské kolo', 'vzpřímený posez, nízký nášlap, často blatníky a košík', 'dojíždění, nákupy, krátké vzdálenosti'],
              ['Trekingové kolo', 'robustní rám, nosič, osvětlení, širší pláště', 'delší výlety, cykloturistika, zavazadla'],
              ['Krosové (crossové) kolo', 'sportovnější geometrie, lehčí rám, užší pláště', 'rychlá jízda po asfaltu a zpevněných cestách'],
              ['Dámské kolo', 'nižší nášlap a rám přizpůsobený postavě', 'komfortní nasedání, dojíždění'],
              ['Skládací kolo', 'malá kola a sklopný rám', 'kombinace s MHD, malý byt'],
              ['Koloběžka pro dospělé', 'bez pedálů, složitelné', 'městské přesuny na krátké vzdálenosti']]) +
          '<p>Městské kolo, třeba modely značky Davi, klade důraz na pohodlí a praktičnost. Trekingové kolo nabídne víc výbavy na dlouhé trasy. Krosové kolo (cross) se sportovnějším sedem jede rychleji a hodí se, když budete jezdit hodně po silnici a zpevněných cestách. Hranice se stírá, takže se spoléhejte na popis konkrétního modelu.</p>'
          '<h2>Rám a materiál</h2>'
          '<p>Rám určuje hmotnost, tuhost i cenu. Ocel je pevná a dobře tlumí nerovnosti, ale bývá těžší. Hliník je lehčí a odolný proti korozi, proto je nejběžnější u trekingových a krosových kol. Karbon je spíš výsadou sportovních modelů. Pokud kolo často stojí venku, ceňte lakování a ochranu proti korozi.</p>'
          '<p>Rámy se liší tvarem. Klasický pánský rám s horní trubkou je tuhý, dámský a unisex rám s nízkým nášlapem usnadňuje nasedání i s nákladem. Pro starší lidi, nákupy nebo oblečení, které brání zvedání nohy, je nízký nášlap pohodlný. Pro sportovnější jízdu je výhodnější klasický rám. Tvar nemá s pohlavím cyklisty nic společného, rozhoduje pohodlí.</p>'
          '<h2>Jak vybrat velikost rámu</h2>'
          '<p>Správná velikost rámu je důležitější než značka. Výrobci uvádějí velikosti v palcích nebo písmeny (S, M, L) a doporučují rozsah výšky postavy. V nabídce se často objevují údaje jako 18 palců a 160 až 185 cm. Zároveň si všimněte délky kroku, protože podle ní se určuje výška sedla.</p>'
          + T(['Výška postavy', 'Orientační velikost rámu'], [
              ['do 165 cm', 'S, přibližně 16 až 17 palců'],
              ['165 až 175 cm', 'M, přibližně 17 až 18 palců'],
              ['175 až 185 cm', 'L, přibližně 19 až 20 palců'],
              ['nad 185 cm', 'XL, přibližně 21 palců a víc']]) +
          '<p>Tabulka je jen orientační, protože každý výrobce má jinou geometrii. Při stání nad horní trubkou by mezi rámem a tělem měla zůstat rezerva a při nejnižší poloze pedálu má být noha téměř natažená. Pokud váháte mezi dvěma velikostmi, zkuste kolo vyzkoušet nebo se poraďte s prodejcem.</p>'
          '<h2>Velikost kol: 26, 27,5 a 28 palců</h2>'
          '<p>Většina trekingových a městských kol má kola velikosti 28 palců, které lépe překonávají nerovnosti a udržují rychlost. Menší kola 26 palců se používají u menších rámů, dámských modelů a pro nižší postavy. Skládací kola mají kola ještě menší. Při výběru ověřte, že velikost plášťů a ráfků odpovídá a že na kolo lze koupit náhradní pláště, viz <a href="/plaste-a-duse/">pláště a duše</a>.</p>'
          '<h2>Převody a brzdy</h2>'
          '<p>Většina kol v této kategorii používá vnější přehazovačku a kazetu se sedmi až dvaceti čtyřmi převody. Značka Shimano je nejčastější. Pro rovinu a město bohatě stačí méně převodů, pro kopcovitou trasu je výhodné víc. Jednoduché městské kolo může mít i jediný převod, což snižuje údržbu, ale omezuje kopce. Existují také převody v nábojích, které jsou chráněné před blátem, ale bývají dražší.</p>'
          '<p>Brzdy bývají ráfkové (V-brake) nebo kotoučové. Kotoučové, hlavně hydraulické, brzdí spolehlivěji za mokra a vyžadují méně síly, ale jsou složitější na údržbu. Ráfkové brzdy jsou jednoduché a levně opravitelné. Podrobnosti najdete v kategoriích <a href="/cyklo-brzdy/">brzdy</a> a <a href="/cyklo-pohon/">pohon</a>.</p>'
          '<h2>Výbava: co je v ceně a co přikoupit</h2>'
          '<p>Trekingová a městská kola často přicházejí s blatníky, nosičem a osvětlením, ale ne vždy. Zkontrolujte popis, zda je výbava součástí. Co chybí, lze doplnit.</p>'
          '<ul><li><a href="/cyklo-svetla/">Světla</a>: bílé vpředu a červené vzadu, bez nich se nejezdí za šera.</li>'
          '<li><a href="/cyklo-blatniky/">Blatníky</a> chrání před špínou při dešti.</li>'
          '<li><a href="/cyklo-tasky-a-nosice/">Tašky a nosiče</a> usnadní dojíždění a nákup.</li>'
          '<li><a href="/cyklo-zamky/">Zámky</a> jsou nezbytné pro parkování ve městě.</li>'
          '<li><a href="/cyklisticke-helmy/">Helma</a> chrání hlavu, a u dětí je v mnoha případech povinná.</li>'
          '<li><a href="/cyklo-zvonky-a-zrcatka/">Zvonek a zrcátko</a> zvyšují bezpečnost provozu.</li>'
          '<li><a href="/sedla-a-gripy/">Sedlo a gripy</a> se často mění kvůli pohodlí.</li>'
          '<li><a href="/cyklo-pumpy-a-naradi/">Pumpa a nářadí</a> pro opravy na cestě.</li></ul>'
          '<h2>Výběr podle použití</h2>'
          '<p>Použití je nejlepší vodítko. Pokud jezdíte hlavně do práce a na nákup, zvolte městské kolo s nízkým nášlapem, blatníky a košíkem. Pro víkendové výlety po cyklostezkách se hodí trekingové kolo s nosičem. Když chcete jet svižněji po asfaltu, vybírejte krosový model. Pokud bydlíte v bytě nebo kombinujete kolo s vlakem, zvažte skládací provedení.</p>'
          '<p>Na kopcovitém terénu, při dlouhých trasách nebo s nákladem zvažte elektrokolo. Podrobně se jimi zabývají kategorie <a href="/elektrokola/">elektrokola</a> a <a href="/skladaci-elektrokola/">skládací elektrokola</a>. Pokud hledáte kolo pro dítě, patří sem <a href="/detska-kola/">dětská kola</a>. Jestli plánujete i lesní cesty, srovnejte s <a href="/horska-kola/">horskými koly</a>, pro rychlou jízdu pak s <a href="/silnicni-a-gravel-kola/">silničními a gravel koly</a>.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ol><li>Koupit podle designu bez kontroly velikosti rámu. Špatně sedící kolo bolí záda i zápěstí.</li>'
          '<li>Podcenit hmotnost. Rozdíl mezi 15 a 20 kg je znát při tahání do schodů.</li>'
          '<li>Nezkontrolovat výbavu a po koupi zjistit, že chybí osvětlení nebo blatníky.</li>'
          '<li>Spoléhat na univerzální popis. „Trekingové“ nemusí znamenat vhodné pro terén.</li>'
          '<li>Nechat kolo bez servisu. Řetěz, brzdy a plášť potřebují pravidelnou kontrolu.</li>'
          '<li>Zapomenout na zámek a pojištění při parkování ve městě.</li></ol>'
          '<h2>Pohodlí: sedlo, řídítka a posez</h2>'
          '<p>Pohodlí rozhoduje, zda budete kolo používat každý den. Široké sedlo s mírným prohnutím obvykle vyhovuje vzpřímenému posezu, užší sedlo se hodí pro sportovnější jízdu. Řídítka jsou u městských kol zahnutá k tělu, u trekingových rovná nebo s rohy pro více poloh rukou. Ergonomické gripy zmenšují tlak na dlaně při delších trasách. Výšku sedla nastavte tak, aby noha při spodní poloze pedálu zůstala lehce pokrčená, a řídítka zvedněte, pokud vás bolí záda nebo zápěstí. Pro většinu lidí je lepší začít vzpřímeněji a posez časem upravit.</p>'
          '<h2>Tlumení a pláště</h2>'
          '<p>Některá trekingová kola mají odpruženou vidlici nebo odpruženou sedlovku, které zmírňují otřesy na nerovném povrchu. Vidlice přidávají hmotnost a potřebují údržbu, proto se vyplatí hlavně u častých jízd po štěrku. Pláště s ochranou proti defektu prodlužují nerušenou jízdu, širší pláště tlumí nárazy. Správný tlak najdete na boku pláště a bývá uveden v rozmezí. Příliš nízký tlak zvyšuje riziko defektu a zpomaluje jízdu, příliš vysoký zhoršuje pohodlí.</p>'
          '<h2>Zavazadla, děti a náklad</h2>'
          '<p>Pokud kolo budete používat k vození nákupu, zvolte robustní nosič a ověřte jeho nosnost. Zavazadla rozložte rovnoměrně, aby kolo nebylo labilní. Pro převoz dítěte existují sedačky a vozíky, viz <a href="/cyklo-sedacky-a-voziky/">cyklo sedačky a vozíky</a>, ale ověřte, že rám a nosič s nimi počítají. Na kolech s nízkým nášlapem bývají omezení pro montáž, proto čtěte pokyny výrobce. Pro vlastní pohodlí a oděv se hodí také <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a <a href="/cyklisticke-rukavice/">rukavice</a>.</p>'
          '<h2>Montáž a první seřízení</h2>'
          '<p>Kola z e-shopu přicházejí často částečně smontovaná. Po rozbalení dotáhněte řídítka, pedály a kola, seřiďte sedlo a zkontrolujte brzdy i řazení. Nejste-li zruční, nechte první seřízení v servisu. Dobře seřízené kolo vydrží déle a jízda je bezpečnější. Pro pravidelnou péči se hodí <a href="/cyklo-udrzba/">cyklo údržba</a> a <a href="/cyklo-dily/">cyklo díly</a>.</p>'
          '<h2>Údržba po celý rok</h2>'
          '<p>Základ je čistý a promazaný řetěz, správný tlak v pláštích a kontrola brzd. Před zimou kolo umyjte, osušte a uložte v suchu. Po dešti ho otřete, aby kolo netrpělo korozí. Jednou za rok nechte zkontrolovat ložiska, lanka a obruče. Při přepravě autem využijte <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>.</p>'
          '<h2>Jak číst nabídky na Sportece</h2>'
          '<p>Na stránce každého kola uvidíte ceny více obchodů, dostupné velikosti a historii ceny. Stejné kolo se prodává v několika velikostech i barvách, často pod jedním názvem. Ujistěte se, že porovnáváte shodnou velikost rámu a velikost kol. U nabídek s označením modelu 2026 počítejte s tím, že se starší ročníky prodávají za jiných podmínek, často s nižším rozdílem ve výbavě. Doprava velkých balíků se mezi obchody liší, proto zkontrolujte, zda jde o doručení smontovaného kola, nebo částečně rozloženého balíku.</p>',
    faq=[
        ('Jaký je rozdíl mezi trekingovým a městským kolem?', 'Městské kolo je pohodlnější pro krátké vzdálenosti a často má košík a nízký nášlap. Trekingové je robustnější a vybavenější pro delší výlety s nákladem.'),
        ('Co je krosové kolo?', 'Sportovnější kolo s užšími plášti a lehčím rámem, vhodné pro rychlejší jízdu po asfaltu a zpevněných cestách. Označuje se také crossové.'),
        ('Jakou velikost rámu zvolit?', 'Podle výšky postavy a délky kroku. Tabulky výrobců jsou orientační, proto při váhání zkuste kolo vyzkoušet nebo se zeptejte prodejce.'),
        ('Stačí sedm převodů?', 'Pro město a rovinu ano. Na kopcovité trasy a delší výlety se hodí víc převodů, případně elektrokolo.'),
        ('Jsou lepší kotoučové, nebo ráfkové brzdy?', 'Kotoučové brzdí silněji a spolehlivěji za mokra. Ráfkové jsou jednodušší a levněji opravitelné. Záleží na terénu a tom, kolik údržby zvládnete.'),
        ('Je potřeba helma?', 'Doporučuje se vždy. U dětí a mladistvých ji ukládá zákon, takže si ověřte aktuální pravidla.'),
        ('Co dělat s nákupem kola přes internet?', 'Po rozbalení zkontrolujte stav, dotáhněte šrouby a nechte provést základní seřízení. Při nejistotě zajděte do servisu.'),
        ('Hodí se městské kolo i na lehčí terén?', 'Na zpevněné cesty a cyklostezky ano, na hrubý terén ne. Pro lesní stezky je vhodnější trekingové nebo horské kolo.'),
        ('Jak dlouho vydrží řetěz?', 'Záleží na jízdě a údržbě. Čistý, promazaný a včas vyměněný řetěz chrání ozubená kola a zvyšuje životnost celého pohonu.'),
        ('Dá se kolo vozit ve vlaku?', 'Záleží na dopravci a typu spoje. Skládací kolo se obvykle bere snáz než klasické, ale podmínky přepravy si vždy ověřte u dopravce před cestou.'),
        ('Kdy zvolit elektrokolo?', 'Když dojíždíte do kopce, vozíte náklad nebo chcete jezdit na delší vzdálenosti s menší námahou. Rozdíl v hmotnosti a údržbě je ale znát.'),
    ])

# ------------------------------------------------------------------ squash
NEW['squash'] = dict(long=True,
    title='Squash: rakety, míčky, brýle a obuv do haly',
    desc='Squashové rakety, míčky, ochranné brýle, halová obuv a oblečení. Jak vybrat váhu rakety, míček a výbavu a porovnat nabídky obchodů.',
    intro='<p>Squash je rychlá hra v uzavřeném kurtu, kde se každá sekunda počítá a vybavení musí odpovídat tempu. Kategorie obsahuje hlavně squashové rakety, míčky různé rychlosti, ochranné brýle, sálovou obuv a doplňky, jako jsou omotávky, tašky, kšiltovky a sportovní oblečení. Pokud s hrou začínáte, získáte tu základní sadu, pokud hrajete roky, najdete modely pro zlepšení rychlosti, pocitu nebo ochrany očí.</p>'
          '<p>Sporteka porovnává nabídky obchodů u značek '
          + B(('dunlop', 'Dunlop'), ('head', 'Head'), ('tecnifibre', 'Tecnifibre'), ('perfly', 'Perfly'), ('harrow', 'Harrow'), ('salming', 'Salming'), ('mizuno', 'Mizuno'), ('victor', 'Victor'), ('wilson', 'Wilson')) +
          '. Následující průvodce vysvětlí, čím se rakety liší, jak vybrat míček a jak chránit oči. Pokud ještě váháte mezi sporty, srovnejte squash s <a href="/badminton/">badmintonem</a>, <a href="/tenis/">tenisem</a> nebo <a href="/padel/">padelem</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Hlavní součástí jsou rakety, ale zdaleka ne jedinou. Bezpečná a pohodlná hra potřebuje celou sadu, protože míček a stěny jsou nemilosrdné vůči nesprávné obuvi nebo špatné ochraně očí.</p>'
          + T(['Položka', 'Co řešit', 'Pro koho'], [
              ['Squashová raketa', 'váha, vyvážení, rám, struny', 'všechny úrovně'],
              ['Squashový míček', 'rychlost a odskok, značení tečkou', 'začátečník až závodník'],
              ['Ochranné brýle', 'pevné čočky, upevnění, velikost obličeje', 'každý hráč, hlavně debl'],
              ['Halová obuv', 'neoznačující podrážka, boční opora', 'celoroční hra'],
              ['Oblečení', 'prodyšné tričko a kraťasy či sukně', 'každý, kdo se potí'],
              ['Omotávky a tašky', 'přilnavost, přeprava rakety', 'pravidelně hrající']]) +
          '<p>Nabídka obsahuje i produkty, které se squashem souvisí volně, například tenisové sukně, trička nebo volnočasové tenisky inspirované squashem. Při nákupu rozlišujte, zda jde o skutečné halové vybavení, nebo o módní doplněk.</p>'
          '<h2>Squashová raketa: váha a vyvážení</h2>'
          '<p>Squashové rakety jsou lehčí než tenisové. Typická váha se pohybuje zhruba od 110 do 180 gramů a názvy modelů ji často uvádějí. Lehčí raketa, například kolem 120 až 140 gramů, se snadno manipuluje a rychle reaguje, ale předá míčku méně síly. Těžší model dodá víc razance, ovšem unaví zápěstí. Začátečníci a mladší hráči se často přiklánějí k lehčímu rozmezí.</p>'
          '<p>Vyvážení rozhoduje, kde leží těžiště. Raketa vyvážená k hlavě přidává sílu úderu, raketa vyvážená k rukojeti zlepšuje obratnost a kontrolu. Pro rychlé výměny v kurtu platí, že obratnost bývá užitečnější než síla, zatímco pro delší výměny a razantní úder se hodí těžiště blíž k hlavě.</p>'
          + T(['Vlastnost', 'Lehká raketa', 'Těžší raketa'], [
              ['Ovladatelnost', 'vysoká', 'nižší'],
              ['Síla úderu', 'nižší', 'vyšší'],
              ['Namáhání zápěstí', 'menší', 'větší'],
              ['Vhodnost pro začátečníky', 'velmi dobrá', 'spíše pokročilí'],
              ['Typický rozsah', 'kolem 110 až 140 g', 'kolem 145 g a výš']]) +
          '<h2>Rám, materiál a struny</h2>'
          '<p>Rámy se vyrábějí z hliníku, grafitu, karbonu a kompozitních směsí. Hliníkové modely, které se hodí na rekreační hru a pro mladší děti, jsou odolné a dostupné. Grafit a karbon nabízejí lepší odezvu a nižší hmotnost při stejné tuhosti. Rám se vždy trochu opotřebuje nárazy o stěnu, proto nebuďte překvapeni škrábanci. Tvar hlavy ovlivňuje „sweet spot“, tedy plochu, na které se míček odráží nejlépe. Větší hlava odpouští chyby, menší dává pocit kontroly.</p>'
          '<p>Struny jsou důležité. Tenčí struny dodávají víc citu a rotace, ale rychle se trhají, silnější vydrží déle. Hustota úpletu a napnutí ovlivňují tvrdost úderu. Řada raket se prodává už nastrunených. Pokud hrajete často, počítejte s přestrunováním a s tím, že samostatné struny nabízejí například <a href="/znacka/tecnifibre/">Tecnifibre</a> nebo <a href="/znacka/dunlop/">Dunlop</a>.</p>'
          '<h2>Míčky: tečky a rychlost</h2>'
          '<p>Squashový míček je z kaučuku a při hře se postupně zahřívá a odskakuje víc. Míčky se rozlišují tečkami. Modrá tečka nebo dvě žluté tečky označují různé rychlosti. Obecně platí, že čím pomalejší míček (například se dvěma žlutými tečkami), tím nižší odskok a vyšší nároky na techniku, takže je vhodnější pro pokročilé a soutěžní hráče. Začátečníci volí živější míčky s vyšším odskokem, například modré nebo červené. Konkrétní značení se mezi výrobci mírně liší, proto sledujte popis balení.</p>'
          '<ul><li><strong>Začátečníci:</strong> pomalejší, výraznější míčky s vysokým odskokem usnadňují výměny. Hodí se i barevné modely pro nácvik.</li>'
          '<li><strong>Pokročilí a soutěžící:</strong> rychlejší míček s nízkým odskokem, který vyžaduje přesnost a dobrou techniku.</li>'
          '<li><strong>Chladný kurt:</strong> studený míček odskakuje méně, proto se před hrou rozehřívá několika výměnami.</li></ul>'
          '<p>Tenisové míčky do squashového kurtu nepatří, mají jiné chování i odskok. Squashové míčky se časem opotřebují a ztrácejí odskok, takže je vyměňte.</p>'
          '<h2>Ochranné brýle</h2>'
          '<p>Oči jsou ve squashi nejzranitelnější. Míček dosahuje vysoké rychlosti a může se odrazit od stěny nečekaným směrem, stejně jako raketa soupeře. Proto se používají brýle s pevnými čočkami a bezpečným upevněním. V nabídce jsou modely značky Dunlop, a to pro dospělé, dětské i pro široký obličej. Při výběru zkontrolujte pohodlné nasazení, šířku, zorné pole a možnost nosit brýle spolu s dioptrickými. Poškozené nebo popraskané brýle vyměňte.</p>'
          '<p>Použití ochrany doporučují provozovatelé kurtů a mnoho z nich ji vyžaduje, především u deblu a dětí. Pro více informací se informujte přímo v halách. Brýle se hodí také pro <a href="/sportovni-bryle/">sport obecně</a>.</p>'
          '<h2>Obuv a oblečení</h2>'
          '<p>Obuv na squash se liší od běžecké obuvi. Potřebujete pevnou boční oporu, dobrou přilnavost a podrážku, která nezanechává stopy. Běžecké boty mají vysokou podrážku a nestabilní bok, takže při prudkém zastavování hrozí podvrtnutí. Hledejte značky <a href="/znacka/mizuno/">Mizuno</a>, <a href="/znacka/salming/">Salming</a>, <a href="/znacka/victor/">Victor</a> nebo <a href="/znacka/head/">Head</a>. Související kategorie jsou <a href="/tenisova-obuv/">tenisová obuv</a> a <a href="/treninkova-obuv/">tréninková obuv</a>. Pro více informací o obecných typech se podívejte na <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<p>Oblečení má být prodyšné a nesmí omezovat pohyb. Kraťasy a sukně musí dovolit hluboký výpad, tričko by se mělo rychle sušit. Pro doplnění můžete zvolit <a href="/sportovni-tricka/">sportovní trička</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-sukne-a-saty/">sukně a šaty</a>.</p>'
          '<h2>Výběr podle úrovně a věku</h2>'
          '<p>Pro začátečníka je rozumné zvolit lehčí raketu s větší hlavou, pomalejší míček a základní brýle. Dospívající hráči používají lehčí rakety s kratší rukojetí. Děti volí menší, hliníkové modely a míčky s vysokým odskokem. Pokročilý hráč pak hledá raketu podle stylu: útočný hráč těžší hlavu, technický hráč lehčí vyvážení. Pravidelně hrající ocení druhou raketu pro případ přetržených strun.</p>'
          '<p>Pokud chcete zkusit hru, kurty a vybavení nabízí řada sportovních center, kde si lze raketu půjčit. Pro začátek stačí jedna raketa, brýle a sálová obuv.</p>'
          '<h2>Základy hry pro nováčky</h2>'
          '<p>Squash se hraje ve čtyřstěnném kurtu, kde se míček odráží od přední i bočních stěn a zadní stěny. Hráči se střídají u míčku a musí soupeři uvolnit prostor. Pro začátek stačí naučit se držení rakety, základní forhend a bekhend a návrat na střed kurtu, takzvané T. Teprve potom přidáváte délku úderů, krátké míče podél stěny a práci s rotací. Dobrý trenér ukáže, jak se vyhýbat zbytečným kolizím, a vysvětlí pravidla uvolnění cesty.</p>'
          '<p>Před hrou se vždy rozcvičte, protože prudké starty a výpady zatěžují kotníky, kolena a třísla. Při hře dbejte na pitný režim, protože kurt bývá teplý a dusný. Hráčům s kloubními potížemi může pomoci konzultace s lékařem či fyzioterapeutem a případně bandáže z kategorie <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>'
          '<h2>Rakety pro různé styly hry</h2>'
          '<p>Značky řadí rakety do řad, které naznačují styl. Útočná řada má těžiště u hlavy, pevný rám a mírně těžší váhu, takže nabízí razantní údery z půlky kurtu. Technické řady jsou lehčí a vyvážené k rukojeti, což vyhovuje hráčům, kteří spoléhají na přesné krátké míče a rychlé reakce. Univerzální řady, hlavně u rekreačních hráčů, vyvažují obojí. Při výběru z nabídky Dunlop, Head nebo Tecnifibre sledujte vlastnosti v popisu: váhu, vyvážení, materiál rámu a velikost hlavy. Názvy řad se mění s modelovými roky, takže při srovnání spoléhejte spíše na technické údaje než na název.</p>'
          '<h2>Půjčit, nebo koupit</h2>'
          '<p>Většina hal půjčuje rakety i míčky, což je dobrá cesta, jak si hru vyzkoušet. Po několika návštěvách ale zjistíte, jaká váha vám sedí, a vlastní raketa ušetří čas i zlepší pocit z hry. Brýle a obuv se vyplatí pořídit hned, protože jsou osobní věc a špatně padnoucí půjčený kus nechrání dobře. Nabídka na Sportece vám ukáže, kolik obchodů daný model prodává a jaké velikosti zrovna zbývají.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Raketu po hře otřete, nenechávejte ji v horkém autě a skladujte v ochranném obalu nebo tašce. Teplo a vlhkost poškozují struny i rám. Omotávku vyměňte, když ztratí přilnavost. Brýle omyjte vlažnou vodou a uložte do pouzdra. Obuv po hře vyvětrejte. Při vlhkém počasí uložte raketu do obalu a vlhké oblečení do samostatné tašky. Pomoci může také kategorie <a href="/sportovni-tasky/">sportovní tašky</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ol><li>Volba příliš těžké rakety kvůli představě, že síla je klíč. Squash je hlavně o technice a rychlosti.</li>'
          '<li>Použití běžecké obuvi, která nemají boční oporu.</li>'
          '<li>Podcenění brýlí. Ochrana očí je nezbytná.</li>'
          '<li>Kupování tenisového míčku nebo rakety místo squashových.</li>'
          '<li>Nevyměňování strun a omotávky, takže raketa působí „mrtvě“.</li>'
          '<li>Ignorování pravidel haly, kde je například povinná čistá podrážka.</li></ol>'
          '<h2>Jak použít Sportecu při nákupu</h2>'
          '<p>Na stránce každého produktu uvidíte nabídky více obchodů a vývoj ceny, což pomáhá při výběru. U rakety ověřte váhu a značku, u míčků značení rychlosti a počet kusů v balení, u obuvi velikost a šířku. Stejný model může být ve dvou obchodech v jiném provedení, takže sledujte popis a obrázky.</p>'
          '<p>Pokud rozšiřujete výbavu pro další sporty, podívejte se na <a href="/micove-sporty/">míčové sporty</a> a <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, případně na <a href="/iontove-napoje/">iontové nápoje</a> a <a href="/lahve-a-termosky/">láhve</a> pro hydrataci během tréninku.</p>',
    faq=[
        ('Jakou váhu rakety zvolit?', 'Začátečníkům obvykle vyhovuje lehčí raketa kolem 120 až 140 gramů, protože se lépe ovládá. Pokročilí volí podle stylu a síly zápěstí.'),
        ('Jak se liší squashová raketa od tenisové?', 'Je výrazně lehčí, má menší hlavu a užší rám. Je to dáno hrou v malém kurtu a potřebou rychlé reakce.'),
        ('Jaký míček si koupit na začátek?', 'Pomalejší míček s větším odskokem a výraznějším značením, který se snáze hraje. Modely označené jako intro nebo pro začátečníky jsou vhodné.'),
        ('Co znamenají tečky na míčku?', 'Označují rychlost a odskok. Obecně více teček znamená pomalejší míček s nižším odskokem, který je určený pro pokročilé, ale značení se u výrobců liší, proto čtěte popis.'),
        ('Jsou brýle povinné?', 'O povinnosti rozhoduje provozovatel haly a pravidla. Ochranu očí doporučujeme vždy, protože míček i raketa mohou způsobit vážný úraz.'),
        ('Mohu hrát v běžeckých botách?', 'Nedoporučuje se. Chybí boční opora a podrážka může ve hale kluzet nebo zanechávat stopy. Lepší je halová obuv.'),
        ('Jak často přestrunovat raketu?', 'Podle intenzity hry. Při častém hraní je potřeba struny kontrolovat a po přetržení nebo ztrátě napnutí vyměnit.'),
        ('Hodí se dětem dospělá raketa?', 'Spíše ne. Děti potřebují lehčí a kratší raketu přizpůsobenou postavě, aby se naučily správnou techniku.'),
        ('Jak pečovat o raketu?', 'Nenechávejte ji v horku ani v mokru, po hře ji otřete a ukládejte do obalu. Opotřebovanou omotávku vyměňte.'),
        ('Je squash vhodný pro začátečníky bez zkušeností?', 'Ano, základní výměny se naučíte rychle. V hale se vyplatí zeptat se na kurz nebo trenéra a nejdřív se zahřát. Při zdravotních potížích se poraďte s lékařem.'),
    ])
