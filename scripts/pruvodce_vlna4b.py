"""Guides wave 4b (Kenny 18. 11. 2026): pronation and supination, running drills, water column and breathability,
compass vs. baseplate compass (buzola).

Demand (CZ / month): supinace 600, pronace, běžecká abeceda 300, vodní sloupec, buzola vs kompas 350,
jak používat kompas.

Sources used for the facts:
- Pronation: Nielsen R. O. et al., Foot pronation is not associated with increased injury risk in novice runners
  wearing a neutral shoe, Br J Sports Med 2014;48(6):440-7 (927 novice runners, Foot Posture Index, neutral shoe,
  1 year; moderate pronators no higher injury risk; highly pronated feet and experienced runners not answered).
  Knapik J. J. et al., Injury reduction effectiveness of selecting running shoes based on plantar shape,
  J Strength Cond Res 2009 (Army basic training; risk ratio men 1.01, women 1.07) plus the Air Force and
  Marine Corps trials. Nigg B. M. et al., Running shoes and running injuries: mythbusting and a proposal for two
  new paradigms ('preferred movement path', 'comfort filter'), Br J Sports Med 2015.
  Wet test is static and shows arch shape only (Runner's World wet test, runresearchjunkie.com, runblogger.com).
  Stability shoes: medial post vs. guide rails / wide base (marathonhandbook.com, solereview.com). Model lines:
  Asics Gel-Kayano (stability) vs Gel-Nimbus (neutral), Saucony Guide (stability) vs Ride (neutral).
- Running drills (Czech terminology): Charles University bachelor thesis BPTX_2012_1_11410_0_319763 (dspace.cuni.cz:
  liftink = vázaný klus with full ankle work, skipink = thigh at least horizontal, low/half/high variants,
  zakopávání = heels to buttocks with thighs vertical, předkopávání in two definitions (Růžička 1992: skipink with
  lower-leg kick; Jeřábek 2008: running on almost straight legs, slang "prkénka"), "koleso", odpichy, odrazy
  s náponem; section length 20-40 m, walk back); Czech orienteering federation methodology letter (zimní příprava
  OB: liftink = kotníkový běh, each drill 3-5 times, then 3 technical rovinky); Seznam Zprávy interview with
  coach Eva Vrabcová Nývltová (about 10 minutes, 30 m beginners / 50 m advanced, light jog between drills,
  in winter inside the run, more reps on longer sections = strength-dynamic training).
- Water column: ISO 811 / EN ISO 811:2018 hydrostatic pressure test (pressure rising at 10 or 60 cm H2O/min until
  water penetrates in three places; the two rates may give different results). 1 mm H2O = 9.81 Pa (physics).
  Breathability: Wikipedia "Breathability" (MVTR in g/m2/24 h, JIS L 1099 A-1/B-1, ASTM E96, results of
  different methods do not correlate; RET by ISO 11092 sweating guarded hotplate, bands 0-6, 6-13, 13-20, 20-30,
  30+), T3 and Decathlon breathability explainers. Gore ePE membrane in GORE-TEX products from fall/winter 2022,
  made without intentionally added PFAS (gore-tex.com blog, ellis-brigham.com).
- Compass: cs.wikipedia "Buzola" (compass + rotating protractor to measure azimuth, baseplate with mirror,
  orienteering thumb compasses without azimuth scale, military 6400 mils in NATO). Suunto "Understanding balancing
  zones" (northern/southern hemisphere balanced needles, global needle). Magnetic declination: NOAA/BGS World
  Magnetic Model 2025 calculator, 18. 11. 2026: Cheb 4.7° E, Praha 5.2° E, České Budějovice 5.1° E,
  Brno 5.6° E, Ostrava 6.0° E, annual change about +0.11 to +0.13°/year. tan(5°) x 1000 m = 87 m.
Left out because sources disagree or could not be verified: EN 343 class thresholds (sources give different Pa
values), a "kneeling pressure" figure in mm, a fixed water column that a tent or jacket "must" have, exact drill
counts per training plan, a degree value of "normal" pronation, which coordinate grid particular Czech tourist maps
print, behaviour of air bubbles in compass capsules.
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------------------------------------------------------
GUIDES['pronace-a-supinace'] = dict(
    name='Pronace a supinace',
    h1='Pronace a supinace: jak je poznat a jaké běžecké boty vybrat',
    seo_title='Pronace a supinace: jak je poznat a jaké boty vybrat',
    seo_desc='Co je pronace, přepronace a supinace, jak je orientačně poznat podle mokré stopy a ošlapané podrážky a kdy sáhnout po neutrální, nebo stabilní botě.',
    intro_html=(
        '<p><strong>Pronace</strong> je přirozené vtočení chodidla dovnitř poté, co noha dopadne na zem. Pomáhá tlumit náraz a dělá ji každý běžec. '
        'O <strong>přepronaci</strong> se mluví, když se chodidlo stáčí dovnitř výrazně víc a klenba se hodně propadá. '
        'Opakem je <strong>supinace</strong> (přesněji podpronace): chodidlo se dovnitř stáčí málo a běžec zůstává na vnější hraně nohy. '
        'Orientačně to poznáte podle ošlapané podrážky starých bot, podle mokré stopy a nejlépe podle videa nohou zezadu při běhu.</p>'
        '<p>Pro výběr bot z toho plyne jednoduché pravidlo. Neutrální běžecká bota sedne většině lidí včetně těch se supinací. '
        'Stabilní bota má smysl hlavně při výrazné přepronaci, a i tehdy by vám v ní mělo být pohodlně. '
        'Domácí testy nejsou diagnóza. Když vás při běhu bolí kolena, paty, holeně nebo Achillovy šlachy, objednejte se k lékaři nebo fyzioterapeutovi, '
        'protože bota bolest sama nevyřeší.</p>'
    ),
    sections=[
        dict(h2='Co přesně znamená pronace a supinace',
             html=(
                 '<p>Oba pojmy pocházejí z anatomie a popisují pohyb, ne vadu. Při běžném běhu dopadá většina lidí nejdřív na vnější část paty nebo středu chodidla. '
                 'Pak se noha během zlomku vteřiny převalí dovnitř, klenba se mírně sníží a chodidlo se přizpůsobí povrchu. To je pronace. '
                 'Ve chvíli odrazu se pohyb obrací: chodidlo se zpevní, mírně vytočí ven a z nohy se stane pevná páka. To je supinace. '
                 'Obojí tedy proběhne v každém kroku u každého běžce.</p>'
                 '<p>Když běžecký prodavač řekne, že jste „pronátor“ nebo „supinátor“, myslí tím rozsah prvního pohybu. '
                 'Přepronace znamená, že se kotník po dopadu stáčí dovnitř víc, než je obvyklé. Podpronace, kterou běžci hovorově nazývají supinace, znamená, že se stáčí málo a náraz se rozkládá hlavně na vnější hranu. '
                 'Neutrální došlap leží mezi tím. Hranice mezi „normální“ a „přílišnou“ pronací není ostrá a odborníci se neshodnou na jednom čísle ve stupních, proto ho tu neuvádíme.</p>'
                 '<p>Na pronaci má vliv tvar klenby, síla svalů chodidla a lýtek, pohyblivost kotníku, postavení kolen a kyčlí, rychlost běhu i únava. '
                 'Stejný člověk tak může na konci dlouhého běhu pronovat víc než na začátku a na rovném asfaltu jinak než na lesní pěšině.</p>'
             )),
        dict(h2='Tři typy došlapu v přehledu',
             html=(
                 '<p>Následující tabulka shrnuje, co se u jednotlivých typů běžně uvádí. Ber ji jako vodítko, ne jako diagnostickou tabulku.</p>'
                 + T(['Typ došlapu', 'Co se děje', 'Kde bývá podrážka ošlapaná', 'Obvyklá volba bot'], [
                     ['Neutrální', 'chodidlo se po dopadu mírně stočí dovnitř a odrazí se přes prostředek přední části', 'vnější okraj paty, střed pod bříškem prstů', 'neutrální bota'],
                     ['Přepronace', 'kotník se výrazně stáčí dovnitř, klenba se hodně propadá', 'vnitřní strana přední části, oblast pod palcem', 'stabilní bota, případně neutrální se širší a pevnější patou'],
                     ['Supinace (podpronace)', 'chodidlo zůstává na vnější hraně, méně tlumí náraz', 'vnější okraj po celé délce podrážky', 'neutrální bota s dobrým tlumením, spíš ohebná'],
                 ])
                 + '<p>V praxi patří velká část běžců do neutrální skupiny nebo do mírné pronace, která se stále považuje za přirozenou. '
                 'Výrazná supinace je méně častá a často jde ruku v ruce s vysokou a tuhou klenbou.</p>'
             )),
        dict(h2='Test mokré stopy: co ukáže a co ne',
             html=(
                 '<p>Mokrý test je nejrychlejší domácí pokus. Potřebujete misku s vodou a tmavý papír, karton nebo suchou dlažbu.</p>'
                 '<ol><li>Namočte si bosé chodidlo, krátce ho otřete, aby z něj nekapalo.</li>'
                 '<li>Postavte se normálně na papír celou vahou, jako když stojíte ve frontě. Nepředklánějte se a neopírejte se o špičky.</li>'
                 '<li>Opatrně sestupte a stopu si vyfoťte dřív, než zaschne. Totéž udělejte s druhou nohou.</li>'
                 '<li>Podívejte se na střední část stopy pod klenbou.</li></ol>'
                 '<p>Pokud je vidět zhruba polovina klenby, máte středně vysokou klenbu. Když je stopa skoro celá vyplněná, klenba je nízká nebo plochá. '
                 'Úzký proužek mezi patou a přední částí, případně úplně přerušená stopa, znamená vysokou klenbu.</p>'
                 '<p>Háček je v tom, že test zachycuje chodidlo v klidu. Neukáže, jak se noha chová během běhu, kdy na ni působí několikanásobek tělesné hmotnosti. '
                 'Plochá stopa tak nemusí znamenat přepronaci a „normální“ stopa ji nevylučuje. Mokrý test proto berte jako první nápovědu, nikoli jako verdikt, podle kterého automaticky koupíte stabilní botu.</p>'
             )),
        dict(h2='Test ošlapané podrážky starých bot',
             html=(
                 '<p>Spolehlivější stopu nechává samotný běh. Vezměte běžecké boty, ve kterých máte naběháno aspoň několik set kilometrů, a postavte je na stůl patou k sobě.</p>'
                 '<ol><li><strong>Pohled zezadu:</strong> nakloní se pata dovnitř, ven, nebo stojí rovně? Zborcená vnitřní strana paty ukazuje na pronaci, vyšlapaná vnější strana na supinaci.</li>'
                 '<li><strong>Podrážka:</strong> obraťte botu a hledejte místa, kde zmizel vzorek. Mírné obroušení vnější hrany paty je u většiny běžců normální.</li>'
                 '<li><strong>Přední část:</strong> silně ošlapaná oblast pod palcem a vnitřní hrana svědčí o odrazu přes vnitřní stranu. Opotřebení podél celé vnější hrany až k malíčku ukazuje spíš na supinaci.</li>'
                 '<li><strong>Svršek:</strong> vytlačená vnitřní strana nad podrážkou nebo naopak vyboulená vnější strana doplní obrázek.</li></ol>'
                 '<p>Pozor na zkreslení. Boty, ve kterých chodíte i do práce, prozradí spíš styl chůze než běhu. Ošlapání ovlivní i povrch, po kterém běháte, a délka nohou. '
                 'Pokud se levá a pravá bota liší, nejde o nic neobvyklého, obě nohy se mohou chovat různě.</p>'
             )),
        dict(h2='Video z mobilu a běžecká analýza',
             html=(
                 '<p>Nejvíc řekne záznam běhu. Požádejte někoho, ať vás natočí zezadu ve výšce kotníků, ideálně zpomaleným videem. '
                 'Běžte svým obvyklým tempem po rovném povrchu nebo na běžeckém pásu, v botách i bez nich. Na záznamu sledujte, jak se pata a Achillova šlacha stáčí po dopadu a jestli se kolena vtáčejí dovnitř.</p>'
                 '<p>Řada běžeckých obchodů nabízí analýzu běhu na pásu s kamerou. Je to dobrý způsob, jak si vyzkoušet několik párů bot a vidět rozdíl. '
                 'Myslete ale na to, že prodejce vám chce prodat boty. Důkladnější vyšetření nabízí fyzioterapeut nebo sportovní lékař, který se kromě chodidla podívá i na kyčle, '
                 'sílu svalů a pohyblivost a zeptá se na vaše potíže.</p>'
             )),
        dict(h2='Neutrální, nebo stabilní běžecké boty',
             html=(
                 '<p><strong>Neutrální bota</strong> nechává chodidlo pohybovat se po svém. Mezipodešev má stejnou tuhost na vnitřní i vnější straně a výrobci se soustředí na tlumení, odraz a hmotnost. '
                 'Je to výchozí volba pro většinu běžců i pro lidi se supinací.</p>'
                 '<p><strong>Stabilní bota</strong> má prvky, které omezují nadměrné stáčení dovnitř. Klasickým řešením je tvrdší pěna na vnitřní straně mezipodešve, takzvaný mediální klín. '
                 'Novější modely místo něj používají zvýšené boční hrany pěny, které nohu vedou jako mantinely, širší základnu nebo pevnější patní díl. Taková bota bývá o něco těžší a tužší.</p>'
                 '<p>Většina velkých výrobců vede obě řady vedle sebe. Například <a href="/znacka/asics/">Asics</a> má stabilní Gel-Kayano a neutrální Gel-Nimbus, '
                 '<a href="/znacka/saucony/">Saucony</a> stabilní Guide a neutrální Ride. Stabilní modely najdete i u <a href="/znacka/hoka/">Hoka</a>. '
                 'Kategorie „motion control“, tedy velmi tuhé boty pro silnou přepronaci, se dnes vyrábí už jen výjimečně.</p>'
                 '<p>Při výběru projděte <a href="/bezecka-obuv/">běžecké boty</a>, pro asfalt <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, '
                 'a podle toho, pro koho kupujete, rovnou <a href="/panske-bezecke-boty/">pánské běžecké boty</a> nebo <a href="/bezecke-boty-damske/">dámské běžecké boty</a>.</p>'
             ), cat='bezecka-obuv', n=4),
        dict(h2='Co o pronaci a botách říká výzkum',
             html=(
                 '<p>Představa, že každá přepronace vede ke zranění a stabilní bota jí předejde, se v posledních letech hodně zpochybňuje. '
                 'Dánská studie Nielsena a kolegů z roku 2014 sledovala 927 začínajících běžců, kteří rok běhali v neutrální botě. '
                 'Lidé s mírnou pronací neměli vyšší riziko zranění než ti s neutrálním chodidlem. Autoři ale upozorňují, že studie nedává odpověď pro silnou pronaci ani pro zkušené běžce.</p>'
                 '<p>Americká armáda v několika studiích přidělovala rekrutům boty podle tvaru stopy, tedy podobně jako mokrý test. Ve srovnání se skupinou, která dostala jednotnou botu, se počet zranění prakticky nelišil. '
                 'Biomechanik Benno Nigg z univerzity v Calgary s kolegy proto v roce 2015 navrhl jiný přístup: běžec si má vybrat botu, která je mu pohodlná, protože tělo samo pozná, co mu sedí.</p>'
                 '<p>Neznamená to, že je typ došlapu úplně jedno. Spíš to ukazuje, že jedno číslo z mokrého testu nestačí. '
                 'Pro prevenci potíží má velký význam pozvolné přidávání kilometrů, posilování a odpočinek, ne jen správná kategorie bot.</p>'
             )),
        dict(h2='Supinace: jaké boty a na co si dát pozor',
             html=(
                 '<p>Pro výraznou supinaci se žádná speciální „antisupinační“ bota nevyrábí. Doporučuje se neutrální model s dobrým tlumením a ohebnou přední částí, '
                 'protože chodidlo s vysokou klenbou samo tlumí méně. Stabilní bota s tvrdým vnitřním klínem by naopak mohla tlačit nohu ještě víc ven.</p>'
                 '<p>Supinátoři často sjíždějí podrážku na vnější hraně rychleji, takže je dobré boty kontrolovat a měnit včas. '
                 'V terénu se hodí <a href="/trailove-boty/">trailové boty</a> s nižší patou a širší podrážkou, které na nerovném povrchu méně klopí kotník ven. '
                 'Pokud jste si v minulosti opakovaně podvrtli kotník, probírejte výběr bot raději s fyzioterapeutem.</p>'
             ), cat='trailove-boty', n=4),
        dict(h2='Vložky do bot: sportovní, nebo na míru',
             html=(
                 '<p>Běžné sportovní vložky z obchodu vyměňují původní stélku za tvarovanou, s výraznější patní miskou nebo podporou klenby. '
                 'Mohou zlepšit pohodlí, ale nejsou zdravotnický prostředek a nic neléčí. '
                 'Individuální ortopedické vložky vyrábí podle vyšetření ortoped nebo specializovaná dílna a jejich použití má doporučit lékař.</p>'
                 '<p>Když vložku vkládáte do běžecké boty, vyjměte původní stélku, jinak se zmenší prostor pro prsty. Do stabilní boty s vložkou s výraznou oporou klenby přidáte podporu dvakrát, '
                 'což nemusí být dobře. Nabídku najdete v kategorii <a href="/vlozky-do-bot/">vložky do bot</a>.</p>'
             ), cat='vlozky-do-bot', n=4),
        dict(h2='Kdy jít k lékaři nebo fyzioterapeutovi',
             html=(
                 '<p>Tento článek popisuje, jak se orientovat při nákupu bot. Nenahrazuje vyšetření. Odborníka vyhledejte, pokud:</p>'
                 '<ul><li>bolest při běhu nebo po něm trvá déle než pár dní nebo se vrací,</li>'
                 '<li>máte otok, brnění, necitlivost nebo bolest při chůzi,</li>'
                 '<li>bolí vás pata ráno po probuzení, holeně nebo Achillova šlacha,</li>'
                 '<li>máte za sebou úraz kotníku, kolena či kyčle nebo operaci,</li>'
                 '<li>vaše chodidla vypadají každé jinak nebo se tvar nohy v poslední době změnil.</li></ul>'
                 '<p>Lékař nebo fyzioterapeut zjistí, odkud bolest pochází. Často to není pronace samotná, ale přetížení, slabé svaly nebo příliš rychle přidaný objem tréninku.</p>'
             )),
        dict(h2='Jak boty vyzkoušet a porovnat nabídky',
             html=(
                 '<ol><li><strong>Zkoušejte odpoledne</strong>, kdy jsou nohy po dni trochu oteklé, a v ponožkách, ve kterých běháte.</li>'
                 '<li><strong>Nechte si rezervu</strong> zhruba na šířku palce mezi nejdelším prstem a špičkou boty.</li>'
                 '<li><strong>Proběhněte se</strong> po obchodě nebo na pásu. Pata nesmí klouzat a bota nesmí nikde tlačit.</li>'
                 '<li><strong>Porovnejte dvě kategorie</strong>: pokud váháte, zkuste neutrální i stabilní model stejné značky a vyberte ten, ve kterém je krok přirozenější.</li>'
                 '<li><strong>Měňte postupně</strong>: přechod na jiný typ bot rozložte do několika týdnů a začněte kratšími běhy.</li></ol>'
                 '<p>Až víte, který model chcete, porovnejte na Sportece nabídky českých obchodů. U běžeckých bot se vyplatí hledat i předchozí generaci téhož modelu, '
                 'která se od nové často liší jen v detailech. Velikosti se mezi značkami liší, proto se podívejte i do naší <a href="/tabulka-velikosti/">tabulky velikostí</a>.</p>'
             )),
    ],
    faq=[
        ('Co je pronace nohy?', '<p>Pronace je přirozené stočení chodidla dovnitř po dopadu na zem. Klenba se přitom mírně sníží a chodidlo tlumí náraz. Dělá ji každý běžec, otázkou je jen její rozsah.</p>'),
        ('Co je supinace a podpronace?', '<p>Běžci tak označují došlap, při kterém se chodidlo po dopadu stáčí dovnitř málo a náraz nese hlavně vnější hrana nohy. V anatomii znamená supinace opačný pohyb k pronaci, který při odrazu dělá každé chodidlo.</p>'),
        ('Jak doma poznám, jestli pronuji?', '<p>Orientačně podle ošlapaných podrážek starých běžeckých bot a podle videa nohou zezadu při běhu. Mokrý test stopy ukáže tvar klenby, ne pohyb při běhu. Jistotu dá až vyšetření u odborníka.</p>'),
        ('Potřebuji při ploché noze stabilní boty?', '<p>Ne nutně. Plochá stopa a přepronace nejsou totéž a studie ukazují, že výběr bot jen podle tvaru stopy počet zranění nesnížil. Vyzkoušejte neutrální i stabilní model a rozhodněte se podle pohodlí.</p>'),
        ('Jaké boty jsou vhodné při supinaci?', '<p>Neutrální běžecké boty s dobrým tlumením a ohebnou přední částí. Stabilní boty s tvrdým vnitřním klínem se při supinaci obvykle nedoporučují.</p>'),
        ('Mohu běhat ve stabilních botách, když mám neutrální došlap?', '<p>Pokud je vám v nich pohodlně a nic vás nebolí, není to zakázané. Stabilní boty jsou ale obvykle těžší a tužší, takže řada neutrálních běžců dává přednost lehčí neutrální botě.</p>'),
        ('Pomohou vložky proti přepronaci?', '<p>Sportovní vložky mohou zlepšit pohodlí, ale nejsou léčba. Individuální ortopedické vložky by měl doporučit lékař po vyšetření. Do stabilní boty vkládejte vložku s oporou klenby jen po poradě.</p>'),
        ('Je přepronace příčinou bolesti kolen?', '<p>Může k ní přispívat, ale příčin bývá víc: přetížení, slabé svaly, rychlý nárůst kilometrů nebo dřívější úraz. Při bolesti trvající déle než několik dní jděte k lékaři nebo fyzioterapeutovi.</p>'),
        ('Mění se pronace s únavou nebo věkem?', '<p>Ano, na konci dlouhého běhu svaly ochabují a chodidlo se často stáčí víc. Tvar klenby se může měnit i během let, například po úrazu nebo v těhotenství. Proto má smysl boty občas znovu vyzkoušet.</p>'),
    ],
    cats=['bezecka-obuv', 'silnicni-bezecke-boty', 'trailove-boty', 'vlozky-do-bot'],
    updated='2026-11-18',
)

# ---------------------------------------------------------------------------------------------------------------
GUIDES['bezecka-abeceda'] = dict(
    name='Běžecká abeceda',
    h1='Běžecká abeceda: cviky, správné provedení a jak ji zařadit do tréninku',
    seo_title='Běžecká abeceda: cviky, technika a kdy ji zařadit',
    seo_desc='Liftink, skipink, zakopávání, předkopávání a odpichy: jak cviky běžecké abecedy provádět, kolik metrů a opakování dělat a kdy je v tréninku zařadit.',
    intro_html=(
        '<p><strong>Běžecká abeceda</strong> je soubor technických cviků, které rozkládají běžecký krok na jednotlivé části a každou procvičují zvlášť. '
        'Základ tvoří <strong>liftink</strong> (kotníkový běh), <strong>skipink</strong> (běh s vysokým zvedáním kolen), <strong>zakopávání</strong>, <strong>předkopávání</strong> a <strong>odpichy</strong>. '
        'Cvičí se po rozklusu, zhruba deset minut, na rovném úseku dlouhém 20 až 50 metrů. Každý cvik se opakuje dvakrát až pětkrát a zpátky se jde chůzí nebo lehkým klusem. '
        'Na konec patří několik volných rovinek, při kterých se nová koordinace přenese do běžného běhu.</p>'
        '<p>Abecedu používají atleti, orientační běžci i rekreační běžci. Pomáhá s koordinací nohou a paží, držením těla a prací kotníku. '
        'Níže najdete popis každého cviku, nejčastější chyby, ukázkovou sestavu a rady, kdy ji v týdnu zařadit. '
        'Pokud se zotavujete ze zranění nebo vás něco bolí, poraďte se s fyzioterapeutem, které cviky jsou pro vás vhodné.</p>'
    ),
    sections=[
        dict(h2='K čemu běžecká abeceda slouží',
             html=(
                 '<p>Běžný klus je pohyb, který člověk opakuje tisíckrát za trénink, a chyby v něm se snadno zafixují. Cviky abecedy vytáhnou jednu fázi kroku a zvětší ji. '
                 'Při liftinku se soustředíte jen na kotník, při skipinku na zvedání stehna, při zakopávání na pohyb bérce za tělem. '
                 'Česká atletická literatura uvádí, že cviky zlepšují koordinaci dolních a horních končetin a držení těla, posilují svaly důležité pro běh a zvětšují rozsah pohybu v kloubech.</p>'
                 '<p>Abeceda zároveň slouží jako rozcvička. Po ní se tělo lépe připraví na rychlejší úseky, intervaly nebo závod. '
                 'Žádné zázračné zrychlení ani ochranu před zraněním ale neslibujte sami sobě. Jde o doplněk tréninku, ne náhradu běhání, posilování a odpočinku.</p>'
             )),
        dict(h2='Kdy abecedu zařadit do tréninku',
             html=(
                 '<p>Nejčastější místo je mezi rozklusem a hlavní částí tréninku. Svaly by měly být zahřáté, ale ještě ne unavené, protože cviky stojí na přesnosti.</p>'
                 '<ul><li><strong>Před intervaly a rychlejšími úseky:</strong> rozklus 10 až 15 minut, krátké rozhýbání, abeceda, rovinky a teprve pak hlavní část.</li>'
                 '<li><strong>Při volném běhu:</strong> stačí dva nebo tři cviky jednou či dvakrát týdně, třeba uprostřed vyběhání na rovném úseku cesty.</li>'
                 '<li><strong>V zimě:</strong> trenérka Eva Vrabcová Nývltová doporučuje vložit abecedu přímo do běhu, abyste nevychladli při stání na místě.</li>'
                 '<li><strong>Jako hlavní náplň:</strong> s větším počtem opakování na delších úsecích se z abecedy stává silově dynamický trénink. Ten už berte jako náročnější jednotku, ne jako rozcvičku.</li></ul>'
                 '<p>Po dlouhém nebo velmi náročném běhu abecedu nezařazujte. Unavené nohy ji neprovedou přesně a cvičení ztrácí smysl.</p>'
             )),
        dict(h2='Liftink: kotníkový běh',
             html=(
                 '<p>Liftink se v metodických materiálech označuje také jako vázaný klus. Pracuje hlavně kotník a chodidlo.</p>'
                 '<ol><li>Postavte se rovně, chodidla u sebe. Zvedněte patu jedné nohy, špičku nechte na zemi a koleno vysuňte co nejvíc dopředu.</li>'
                 '<li>Druhá noha je přitom v koleni propnutá. Pak nohy vyměňte.</li>'
                 '<li>Začněte pomalu na místě, potom postupujte drobnými krůčky vpřed. Špičky se od země zvedají jen nepatrně.</li>'
                 '<li>Paže nejdřív nechte volně viset, později je ohněte do pravého úhlu a pohybujte jimi jako při běhu. Frekvenci postupně zvyšujte.</li></ol>'
                 '<p><strong>Časté chyby:</strong> malý rozsah odvíjení chodidla, zvedání celého chodidla od země a pokrčená oporová noha. '
                 'Pomůže zpomalit, cvičit nejdřív jen jednou nohou nebo se opřít o zeď a vydržet v poloze se zvednutou patou.</p>'
             )),
        dict(h2='Skipink: běh s vysokým zvedáním kolen',
             html=(
                 '<p>Skipink navazuje na liftink, ale stehno švihové nohy se zvedá nejméně do vodorovné polohy. Trup zůstává v mírném běžeckém náklonu vpřed, oporová noha se při odrazu propíná.</p>'
                 '<ul><li><strong>Nízký skipink</strong> je rychlý a krátký, kolena jdou jen kousek nahoru. Hodí se pro začátečníky a na frekvenci.</li>'
                 '<li><strong>Polovysoký skipink</strong> zvedá stehno zhruba do poloviny.</li>'
                 '<li><strong>Vysoký skipink</strong> vede koleno až do výše kyčlí. Je nejnáročnější na sílu i koordinaci.</li></ul>'
                 '<p>Pokyn trenérů zní: zvedejte kolena, vytáhněte se z boků, zůstaňte na špičkách a ohnutými pažemi energicky pracujte ve směru běhu. '
                 '<strong>Časté chyby:</strong> záklon trupu, „sezení“ s pokrčenou oporovou nohou, nízko zvedaná kolena a násilné přitahování paty k hýždím. '
                 'Bérec má z kolene volně viset, nemá se skládat pod stehno.</p>'
             )),
        dict(h2='Zakopávání',
             html=(
                 '<p>Při zakopávání stehna směřují stále kolmo k zemi a pracuje jen bérec, který se dynamicky švihne dozadu tak, aby se pata dotkla hýždě. '
                 'Došlap i odraz jsou ze špičky, trup je vzpřímený, paže se pohybují jako při běhu. '
                 'Cvik posiluje zadní stranu stehna a protahuje přední.</p>'
                 '<p><strong>Časté chyby:</strong> kolena utíkají dopředu, takže se pata složí pod tělo místo za něj, a přílišný předklon. '
                 'Pomůže stát bokem ke zdi a hlídat, aby stehno zůstalo v prodloužení trupu. Hlavu držte zpříma a dívejte se zhruba dvacet metrů před sebe.</p>'
             )),
        dict(h2='Předkopávání: dvě podoby jednoho názvu',
             html=(
                 '<p>U předkopávání se česká literatura neshodne a trenéři jím myslí dvě různé věci. Než se začnete učit, zeptejte se trenéra, kterou variantu chce.</p>'
                 '<h3>Skipink s vykopnutím bérce</h3>'
                 '<p>Koleno se zvedne jako při skipinku, zhruba do výše boků. Pak bérec aktivně vykývne vpřed a noha rychle dokročí na špičku pod tělo. '
                 'Trup je vzpřímený, nanejvýš mírně zakloněný. Nejdřív vede pohyb koleno, potom bérec.</p>'
                 '<h3>Běh na natažených nohách</h3>'
                 '<p>Ve druhé podobě, které se v oddílech říká třeba „prkénka“ nebo „rovné předkopy“, běžíte na téměř propnutých nohách. '
                 'Špička je před došlapem přitažená k holeni a odraz přichází z rychlého propnutí kotníku, jako byste zemi „hrabali“ pod sebe. '
                 'Cvik klade velké nároky na lýtka. Když na něj síla nestačí, běžec dopadá na celé chodidlo nebo na patu a zaklání se. '
                 'V takovém případě nejdřív posilujte lýtka, například přeskoky přes <a href="/svihadla/">švihadlo</a> nebo chůzí po špičkách.</p>'
                 '<p>Někdy se jako předkopávání chybně označuje i „koleso“, koordinačně náročné spojení skipinku a zakopávání, při kterém noha opisuje velký kruh.</p>'
             )),
        dict(h2='Odpichy, odrazy a cval stranou',
             html=(
                 '<p><strong>Odpichy</strong> jsou krátké odrazy s maximálním rozsahem pohybu v kotníku. Odrazová noha je v koleni uvolněně natažená, '
                 'švihová se zvedá do mírného skrčení vpřed. Odrážíte se hlavně lýtkem a paže pracují ve větším rozsahu než při běhu. Odpichy se dělají nízké, vysoké nebo se stupňovanou rychlostí.</p>'
                 '<p><strong>Odrazy s náponem</strong> vypadají jako prodloužený běžecký krok. Odraz se dokončí v plném rozsahu v kyčli, koleni i kotníku a švihová noha jde „ostrým kolenem“ vpřed do vodorovné polohy. '
                 'Patří k náročnějším cvikům, proto je zařazujte až po zvládnutí základních.</p>'
                 '<p><strong>Cval stranou</strong> (klus přísunný) se dělá bokem k směru pohybu: jedna noha vykročí do strany, druhá ji v letu dohoní. '
                 'Rozhýbe kyčle a procvičí pohyb do strany, který při běhu rovně chybí. Hodí se hlavně do rozcvičky a v orientačním nebo trailovém běhu.</p>'
             )),
        dict(h2='Ukázková sestava na deset minut',
             html=(
                 '<p>Sestava je jen příklad pro zdravého rekreačního běžce. Délky úseků upravte podle místa a kondice. '
                 'Začátečníkům stačí kolem 30 metrů, zdatnější běžci mohou cvičit na 50 metrech. Mezi cviky se vracejte chůzí nebo lehkým klusem.</p>'
                 + T(['Pořadí', 'Cvik', 'Úsek', 'Opakování'], [
                     ['1', 'rozklus a krátké rozhýbání', '10–15 min', '1×'],
                     ['2', 'liftink', '20–30 m', '2×'],
                     ['3', 'nízký skipink', '20–30 m', '2×'],
                     ['4', 'zakopávání', '20–30 m', '2×'],
                     ['5', 'předkopávání (varianta podle trenéra)', '20–30 m', '2×'],
                     ['6', 'odpichy', '20–30 m', '2×'],
                     ['7', 'cval stranou, každou stranou jednou', '20–30 m', '2×'],
                     ['8', 'volné stupňované rovinky', '60–100 m', '3×'],
                 ])
                 + '<p>Až budete cviky ovládat, můžete přidat vysoký skipink, kombinace (například tři kroky skipinku a přechod do běhu) nebo cvičení jen jednou nohou. '
                 'Přidávejte postupně a sledujte, jak se nohy cítí další den.</p>'
             )),
        dict(h2='Nejčastější chyby a jak se jim vyhnout',
             html=(
                 '<ul><li><strong>Rychlost místo kvality:</strong> abeceda není závod. Raději kratší úsek, ale přesně.</li>'
                 '<li><strong>Pohled do země:</strong> sklopená hlava táhne trup do předklonu. Dívejte se před sebe.</li>'
                 '<li><strong>Ztuhlé paže:</strong> ruce patří k běžeckému kroku. Lokty ohnuté, ramena volná, pohyb vpřed a vzad, ne přes tělo.</li>'
                 '<li><strong>Dopad na paty:</strong> většina cviků se dělá na přední části chodidla. Když se paty „lepí“ k zemi, zpomalte.</li>'
                 '<li><strong>Cvičení na únavu:</strong> po dlouhém běhu nebo silovém tréninku cviky ztrácí tvar.</li>'
                 '<li><strong>Nevhodný povrch:</strong> kluzká tráva, štěrk nebo nerovný chodník zvyšují riziko podvrtnutí. Ideální je atletická dráha, pevná cesta nebo hřiště.</li></ul>'
                 '<p>Pomáhá natočit se na mobil zboku a porovnat záznam s popisem cviku. Ještě lepší je navštívit trénink běžeckého nebo atletického oddílu, kde vás trenér opraví na místě.</p>'
             )),
        dict(h2='Obuv a vybavení na běžeckou abecedu',
             html=(
                 '<p>Speciální vybavení nepotřebujete. Stačí běžecké boty, ve kterých normálně běháte, a rovná plocha. '
                 'Velmi měkké boty s vysokou mezipodešví mohou při liftinku a odpiších zastřít práci kotníku, takže někteří běžci volí na technické cviky lehčí a nižší obuv. '
                 'Do lehčích bot ale přecházejte pozvolna.</p>'
                 '<p>Vhodné modely najdete mezi <a href="/silnicni-bezecke-boty/">silničními běžeckými botami</a> a v celé kategorii <a href="/bezecka-obuv/">běžecké obuvi</a>. '
                 'Kdo chce sledovat tempo rovinek a délku úseků, využije <a href="/sportovni-hodinky/">sportovní hodinky</a>. '
                 'Na zimní cvičení venku se hodí přiléhavé <a href="/leginy/">legíny</a> a <a href="/funkcni-tricka/">funkční trička</a>, ve kterých se nic nezachytí o kolena.</p>'
             ), cat='silnicni-bezecke-boty', n=4),
        dict(h2='Abeceda u dětí a začínajících běžců',
             html=(
                 '<p>Děti se cviky učí nejlépe hrou a v malých skupinkách, kde trenér každého vidí. V atletických přípravkách se běžně cvičí ve vlnách po pěti až osmi dětech, '
                 'které vybíhají postupně, a zpátky se jde chůzí.</p>'
                 '<p>Začátečník by měl nejdřív zvládnout liftink, nízký skipink a zakopávání. Předkopávání a odrazy s náponem přidejte, až budou základní cviky vypadat čistě. '
                 'Pokud máte zdravotní potíže, například s koleny, kotníky nebo zády, domluvte se s lékařem nebo fyzioterapeutem, které cviky vynechat.</p>'
             )),
    ],
    faq=[
        ('Co je běžecká abeceda?', '<p>Soubor technických cviků, které procvičují jednotlivé části běžeckého kroku: liftink, skipink, zakopávání, předkopávání, odpichy a další. Slouží ke zlepšení koordinace a jako rozcvička.</p>'),
        ('Jaké cviky patří do běžecké abecedy?', '<p>Základ tvoří liftink (kotníkový běh), skipink (vysoká kolena), zakopávání, předkopávání a odpichy. Často se přidávají odrazy s náponem, cval stranou, koleso a stupňované rovinky.</p>'),
        ('Jaký je rozdíl mezi liftinkem a skipinkem?', '<p>Při liftinku pracuje hlavně kotník a špičky zůstávají skoro u země. Při skipinku se zvedá celé stehno nejméně do vodorovné polohy.</p>'),
        ('Kolik metrů a opakování dělat?', '<p>Obvykle úseky 20 až 50 metrů a každý cvik dvakrát až pětkrát. Začátečníkům stačí kratší úsek kolem 30 metrů a méně opakování.</p>'),
        ('Mám abecedu dělat před, nebo po běhu?', '<p>Před hlavní částí tréninku, po rozklusu. Po dlouhém nebo náročném běhu už nohy cviky neprovedou přesně.</p>'),
        ('Jak často běžeckou abecedu zařazovat?', '<p>Rekreačním běžcům stačí jednou až dvakrát týdně, typicky před rychlejším tréninkem. Krátké základní cviky se dají zařadit téměř kdykoliv jako součást rozcvičky.</p>'),
        ('Co je předkopávání a jak ho dělat?', '<p>Pod názvem se skrývají dvě varianty: skipink s vykopnutím bérce vpřed a běh na téměř natažených nohách s odrazem z kotníku. Zeptejte se trenéra, kterou má na mysli.</p>'),
        ('Mohu dělat běžeckou abecedu doma?', '<p>Liftink nebo nízký skipink na místě ano, pokud máte pevnou podlahu a neruší to sousedy. Plnohodnotné cviky s pohybem vpřed potřebují aspoň 20 metrů rovné plochy.</p>'),
        ('Je běžecká abeceda vhodná i pro starší běžce?', '<p>Ano, s menšími úseky a pomalejším tempem. Kdo má potíže s klouby nebo zády, měl by se nejdřív poradit s lékařem nebo fyzioterapeutem.</p>'),
    ],
    cats=['bezecka-obuv', 'silnicni-bezecke-boty', 'sportovni-hodinky', 'svihadla'],
    updated='2026-11-18',
)

# ---------------------------------------------------------------------------------------------------------------
GUIDES['vodni-sloupec'] = dict(
    name='Vodní sloupec a prodyšnost',
    h1='Vodní sloupec a prodyšnost: co znamenají čísla u bund, kalhot a stanů',
    seo_title='Vodní sloupec a prodyšnost: co znamenají čísla u bund',
    seo_desc='Co udává vodní sloupec v mm, jak se měří, kolik ho potřebujete a jak číst prodyšnost v g/m²/24 h a RET. Rozdíl mezi membránou a zátěrem u bund a stanů.',
    intro_html=(
        '<p><strong>Vodní sloupec</strong> udává, jaký tlak vody materiál vydrží, než jím voda pronikne. Uvádí se v milimetrech: '
        'údaj 10 000 mm znamená, že by tkanina v laboratoři odolala tlaku sloupce vody vysokého 10 metrů. Čím vyšší číslo, tím vyšší odolnost proti dešti, tlaku popruhů batohu nebo klečení na mokré zemi. '
        'U běžné turistiky se jako solidní základ považuje kolem 10 000 mm, do dlouhého deště a na hory se vybírá vyšší hodnota.</p>'
        '<p><strong>Prodyšnost</strong> říká, kolik vodní páry od těla dokáže materiál propustit ven. Najdete ji ve dvou podobách: v gramech na metr čtvereční za 24 hodin (čím víc, tím lépe) '
        'nebo jako hodnotu RET (čím méně, tím lépe). Čísla se dají porovnávat jen tehdy, když byla měřena stejnou metodou. '
        'V článku vysvětlujeme, jak se oba údaje měří, co znamenají v praxi a na co se dívat u <a href="/nepromokave-bundy/">nepromokavých bund</a>, kalhot i stanů.</p>'
    ),
    sections=[
        dict(h2='Co je vodní sloupec',
             html=(
                 '<p>Vodní sloupec je starší jednotka tlaku, která se v textilu udržela, protože je názorná. Představte si trubku postavenou na kus látky a postupně ji plňte vodou. '
                 'Výška hladiny ve chvíli, kdy voda začne pronikat na druhou stranu, je vodní sloupec. Jeden milimetr vodního sloupce odpovídá tlaku asi 9,8 pascalu, '
                 '10 000 mm je tedy zhruba 98 kilopascalů.</p>'
                 '<p>Déšť sám o sobě velký tlak nevytváří. Problém nastává tam, kde se k vodě přidá síla: ramenní popruhy batohu tlačí mokrou bundu na tělo, '
                 'kolena se opírají o mokrou trávu, při sezení na kameni působí na kalhoty váha těla, u stanu na podlahu tlačí člověk ležící na mokré zemi. '
                 'Proto má smysl hledat vyšší čísla tam, kde je materiál namáhaný.</p>'
             )),
        dict(h2='Jak se vodní sloupec měří',
             html=(
                 '<p>Postup popisuje norma <strong>ISO 811</strong> (v Evropě EN ISO 811), hydrostatická zkouška textilií. Vzorek látky se upne do přístroje a zespodu se na něj tlačí voda, '
                 'jejíž tlak plynule roste. Norma připouští dvě rychlosti nárůstu, 10 nebo 60 cm vodního sloupce za minutu, a obě mohou dát odlišný výsledek, proto se zvolená rychlost uvádí v protokolu. '
                 'Zkouška končí ve chvíli, kdy voda prosákne na třech místech vzorku. Tlak v tu chvíli je výsledná hodnota.</p>'
                 '<p>Z toho plyne několik praktických důsledků:</p>'
                 '<ul><li>Měří se samotná látka, ne švy, zipy ani hotová bunda. Nepromokavost oblečení proto závisí i na podlepení švů a konstrukci.</li>'
                 '<li>Výrobce často uvádí hodnotu nového materiálu. Po praní, odření a ohýbání může odolnost klesat.</li>'
                 '<li>Ne každý výrobce zveřejňuje, jakou metodou měřil. Čísla z různých zkušeben a norem nemusí být přímo srovnatelná.</li></ul>'
             )),
        dict(h2='Kolik milimetrů potřebujete',
             html=(
                 '<p>Pevné hranice, od kdy je bunda „nepromokavá“, žádná norma pro sportovní oblečení nestanoví. Výrobci a prodejci se ale drží podobných pásem, která slouží jako dobré vodítko:</p>'
                 + T(['Vodní sloupec', 'Co od materiálu čekat', 'Typické použití'], [
                     ['do 5 000 mm', 'odolá krátké přeháňce, při delším dešti může prosáknout', 'větrovky, lehké bundy do města, softshell'],
                     ['5 000–10 000 mm', 'zvládne běžný déšť a krátké vystavení tlaku', 'turistické bundy, levnější nepromokavé kalhoty'],
                     ['10 000–20 000 mm', 'snese vytrvalý déšť a tlak batohu', 'turistika, lyžování, cyklistika v dešti'],
                     ['nad 20 000 mm', 'určeno pro dlouhý pobyt v dešti a mokrém sněhu', 'horské bundy, expedice, náročný skialpinismus'],
                 ])
                 + '<p>Vyšší číslo není samo o sobě lepší. Vysoce odolné materiály bývají tužší a dražší a ve městě jejich výhodu nevyužijete. '
                 'U lyžařského oblečení navíc hraje roli, jestli se často válíte ve sněhu nebo sedíte na mokré sedačce lanovky.</p>'
             )),
        dict(h2='Prodyšnost v g/m²/24 h',
             html=(
                 '<p>Údaj v gramech na metr čtvereční za 24 hodin (anglicky MVTR) vyjadřuje, kolik vodní páry projde metrem čtverečním látky za den. '
                 'Vyšší číslo znamená prodyšnější materiál. Běžně se setkáte s hodnotami od jednotek tisíc po desítky tisíc.</p>'
                 '<p>Komplikace je v metodě. Japonská norma JIS L 1099 má několik variant: v metodě A-1 je pod vzorkem vysoušedlo, v metodě B-1 je látka obrácená a membrána je v přímém styku s vodou. '
                 'Používá se i americká norma ASTM E96. Výsledky jednotlivých metod spolu nekorelují, takže materiál A s hodnotou 20 000 g podle jedné metody nemusí být prodyšnější než materiál B s 15 000 g podle jiné. '
                 'Když výrobce metodu neuvede, berte číslo jen jako hrubé vodítko.</p>'
             )),
        dict(h2='RET: odpor proti prostupu páry',
             html=(
                 '<p>Druhý způsob vyjádření prodyšnosti je <strong>RET</strong> (resistance to evaporative heat transfer). Měří se podle normy ISO 11092 na vyhřívané „potící se“ desce, '
                 'která napodobuje kůži. Hodnota udává, jak velký odpor klade látka odpařování potu, proto platí opak: <strong>čím nižší RET, tím prodyšnější materiál</strong>.</p>'
                 + T(['RET', 'Prodyšnost', 'Kdy vyhovuje'], [
                     ['0–6', 'velmi vysoká', 'běh, skialpy, intenzivní pohyb'],
                     ['6–13', 'dobrá', 'turistika svižným tempem, kolo'],
                     ['13–20', 'střední', 'chůze, mírná zátěž'],
                     ['nad 20', 'nízká', 'krátké nošení a malá aktivita'],
                 ])
                 + '<p>RET je o něco srovnatelnější než gramy, protože metoda je jedna. I tak záleží na tom, kolik se potíte, jak je venku teplo a jak vlhko. '
                 'Za studeného suchého dne odchází pára z bundy snáz než v teplém dusném dešti.</p>'
             )),
        dict(h2='Membrána, laminát a zátěr',
             html=(
                 '<p>Nepromokavost a prodyšnost zajišťuje buď membrána, nebo zátěr. Vrchní látka sama o sobě vodu nezastaví.</p>'
                 '<ul><li><strong>Mikroporézní membrána</strong> má drobné póry, kterými projdou molekuly páry, ale ne kapky vody. Typicky se vyrábí z expandovaného PTFE. '
                 'Gore od podzimu 2022 nasazuje v řadě výrobků i membránu ePE z expandovaného polyetylenu, vyráběnou bez záměrně přidaných PFAS.</li>'
                 '<li><strong>Neporézní (hydrofilní) membrána</strong> póry nemá a páru propouští chemicky, molekulu po molekule. Bývá polyuretanová nebo polyesterová a funguje lépe, když je uvnitř bundy teplo a vlhko.</li>'
                 '<li><strong>Zátěr</strong> (coating) je vrstva, obvykle polyuretanová, nanesená z rubu látky. Je levnější, ale obvykle méně prodyšný a časem se může odírat.</li></ul>'
                 '<p>Podle toho, jak je membrána spojená s látkami, se mluví o <strong>2vrstvém</strong> laminátu (membrána je přilepená k vrchní látce a uvnitř visí volná podšívka), '
                 '<strong>2,5vrstvém</strong> (místo podšívky je na membráně tenký ochranný potisk, bunda je lehká a sbalitelná) a <strong>3vrstvém</strong> (membrána je sevřená mezi vrchní a vnitřní látkou, nejodolnější varianta pro hory).</p>'
             ), cat='nepromokave-bundy', n=4),
        dict(h2='Impregnace DWR: proč „nepromokavá“ bunda vypadá promočeně',
             html=(
                 '<p>Vrchní látka je ošetřená vodoodpudivou úpravou (DWR), na které voda perlí a stéká. Když úprava zeslábne, látka nasákne. '
                 'Membrána pod ní pořád nepropouští vodu, ale mokrá vrchní vrstva přestane dýchat, pára se uvnitř sráží a člověk má pocit, že bunda promokla.</p>'
                 '<p>Řešení je pravidelné praní technickým pracím prostředkem a obnovení impregnace sprejem nebo prostředkem do pračky. '
                 'Některé úpravy se podle výrobce oživí teplem, například sušením v sušičce na nízkou teplotu, pokud to štítek dovoluje. '
                 'Prostředky najdete v kategorii <a href="/impregnace/">impregnace</a>. Mnoho značek přešlo na úpravy bez fluorovaných látek. Sledujte, jestli voda na látce ještě perlí, a impregnaci obnovte, jakmile přestane.</p>'
             ), cat='impregnace', n=4),
        dict(h2='Švy, zipy a střih rozhodují stejně jako čísla',
             html=(
                 '<p>I látka s vysokým vodním sloupcem promokne, když voda najde cestu švem. U nepromokavého oblečení hledejte <strong>podlepené švy</strong>, tedy páskou přelepené vpichy jehly. '
                 'Levnější bundy mívají podlepené jen nejvíc namáhané švy na ramenou a kapuci.</p>'
                 '<ul><li><strong>Zipy:</strong> vodoodpudivé zipy nebo zipy kryté légou. Hlavní zip by měl mít vnitřní lištu proti zatékání.</li>'
                 '<li><strong>Kapuce:</strong> nastavitelná ve dvou nebo třech směrech, s pevným kšiltem, aby nepadala do očí.</li>'
                 '<li><strong>Větrání:</strong> zipy v podpaží pomohou víc než sebelepší membrána, když jdete do kopce.</li>'
                 '<li><strong>Délka a střih:</strong> delší záda kryjí kalhoty při sezení a pod batohem, manžety se stahují suchým zipem.</li></ul>'
                 '<p>Pro výběr podle střihu se podívejte na <a href="/damska-nepromokava-bunda/">dámské nepromokavé bundy</a> nebo na lehčí <a href="/softshellove-bundy/">softshellové bundy</a>, které mají obvykle nižší vodní sloupec, ale lépe dýchají.</p>'
             )),
        dict(h2='Nepromokavé kalhoty, ponožky a obuv',
             html=(
                 '<p>U kalhot je tlak vody na kolenou a sedu vyšší než na bundě, proto se vyplatí hledat podobnou nebo vyšší hodnotu vodního sloupce. '
                 'Praktické jsou boční zipy po celé délce nohavice, díky kterým kalhoty natáhnete i přes boty. Nabídku najdete v kategorii <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>.</p>'
                 '<p>U obuvi se vodní sloupec obvykle neuvádí. Výrobci píšou název membrány a výsledky vlastních testů, například v ponoření ve vodě nebo na flexním stroji. '
                 'Doplňkem jsou <a href="/nepromokave-ponozky/">nepromokavé ponožky</a> s membránou, které se nosí třeba do běžeckých bot na trail nebo na kolo. '
                 'Věci v batohu ochrání <a href="/nepromokave-vaky/">nepromokavé vaky</a>.</p>'
             ), cat='nepromokave-kalhoty', n=4),
        dict(h2='Vodní sloupec u stanů',
             html=(
                 '<p>U stanů se uvádí zvlášť hodnota pro tropiko (vnější plachtu) a pro podlahu. Podlaha mívá vyšší číslo, protože na ni tlačí váha těla a vybavení na mokré zemi. '
                 'Rozumné je kombinovat odolnou podlahu s podložkou pod stan, která chrání před kameny i oděrem.</p>'
                 '<p>U tropika záleží i na materiálu. Polyesterové tkaniny se ve vlhku méně prověšují, nylonové se silikonovým zátěrem bývají lehčí a pevnější v tahu, ale za deště povolí a je potřeba je dopnout. '
                 'Švy tropika by měly být podlepené nebo utěsněné. Velký rozdíl dělá i postavení stanu: napnuté tropiko, které se nedotýká vnitřní ložnice, zatéká méně.</p>'
                 '<p>Vybírejte podle počtu osob a terénu mezi <a href="/turisticke-stany/">turistickými stany</a>, <a href="/rodinne-stany/">rodinnými stany</a> a v celé kategorii <a href="/stany/">stany</a>. '
                 'Jako lehký přístřešek poslouží i <a href="/tarpy/">tarp</a>.</p>'
             ), cat='stany', n=4),
        dict(h2='Jak číst parametry a porovnávat nabídky',
             html=(
                 '<ol><li><strong>Vodní sloupec:</strong> hledejte číslo v mm a, pokud je uvedeno, normu (ISO 811). Bez čísla je slovo „voděodolný“ jen popis.</li>'
                 '<li><strong>Prodyšnost:</strong> porovnávejte g/m²/24 h jen u stejné metody, RET mezi sebou. Gramy a RET navzájem nepřevádějte.</li>'
                 '<li><strong>Konstrukce:</strong> membrána, nebo zátěr, kolik vrstev, podlepené švy.</li>'
                 '<li><strong>Detaily:</strong> větrání, kapuce, hmotnost, sbalitelnost.</li>'
                 '<li><strong>Péče:</strong> dovolené praní a sušení na štítku.</li></ol>'
                 '<p>Na Sportece pak porovnáte, kolik stojí stejný model v různých českých obchodech a v jakých velikostech je skladem. '
                 'U bund s membránou se vyplatí sledovat i předchozí kolekce, protože materiál se mezi ročníky často nemění.</p>'
             )),
    ],
    faq=[
        ('Co znamená vodní sloupec 10 000 mm?', '<p>Že materiál v laboratoři vydržel tlak vody odpovídající sloupci vysokému 10 metrů, než jím voda prosákla na třech místech. Pro běžnou turistiku je to solidní hodnota.</p>'),
        ('Kolik vodního sloupce má mít nepromokavá bunda?', '<p>Na město a krátké přeháňky stačí kolem 5 000 mm, na turistiku 10 000 mm a víc, do hor a dlouhého deště 20 000 mm a víc. Jde o zvyklosti trhu, ne o normu.</p>'),
        ('Je vyšší prodyšnost v g/m²/24 h lepší?', '<p>Ano, vyšší číslo znamená, že materiál propustí víc páry. Porovnávat se ale dají jen údaje měřené stejnou metodou.</p>'),
        ('Co znamená RET?', '<p>RET vyjadřuje odpor materiálu proti odpařování potu podle normy ISO 11092. Čím nižší číslo, tím prodyšnější látka. Hodnota do 6 se považuje za velmi prodyšnou.</p>'),
        ('Proč bunda s membránou promokla?', '<p>Nejčastěji vyprchala impregnace a vrchní látka nasákla, takže se uvnitř sráží pára. Jindy teče voda švem, zipem nebo kolem kapuce. Skutečně poškozená membrána je méně častá.</p>'),
        ('Jaký je rozdíl mezi membránou a zátěrem?', '<p>Membrána je samostatná tenká vrstva nalaminovaná na látku, zátěr je vrstva nanesená přímo na rub tkaniny. Zátěr bývá levnější, ale obvykle méně prodyšný.</p>'),
        ('Co znamená 2,5vrstvý materiál?', '<p>Membrána je nalaminovaná na vrchní látku a zevnitř ji místo podšívky chrání tenký potisk. Bunda je lehká a dobře se sbalí, ale méně odolná než 3vrstvá.</p>'),
        ('Jaký vodní sloupec má mít stan?', '<p>Podlaha by měla mít vyšší hodnotu než tropiko, protože na ni tlačí váha těla. Stejně důležité jsou podlepené švy a správné vypnutí stanu.</p>'),
        ('Ztrácí bunda časem nepromokavost?', '<p>Odolnost může klesat odíráním, ohýbáním a nevhodným praním. Pravidelné praní technickým prostředkem a obnova impregnace prodlouží funkčnost.</p>'),
    ],
    cats=['nepromokave-bundy', 'nepromokave-kalhoty', 'stany', 'impregnace', 'turisticke-stany'],
    updated='2026-11-18',
)

# ---------------------------------------------------------------------------------------------------------------
GUIDES['buzola-a-kompas'] = dict(
    name='Buzola a kompas',
    h1='Buzola a kompas: jaký je rozdíl a jak je používat s mapou',
    seo_title='Buzola a kompas: rozdíl a jak je používat v terénu',
    seo_desc='Jaký je rozdíl mezi buzolou a kompasem, z čeho se buzola skládá, jak zorientovat mapu, určit azimut a jak započítat magnetickou deklinaci v Česku.',
    intro_html=(
        '<p><strong>Kompas</strong> je přístroj s magnetickou střelkou, která ukazuje k magnetickému severu. Nic víc. '
        '<strong>Buzola</strong> je kompas doplněný otočným úhloměrem se stupnicí, obvykle na průhledné destičce s pravítkem, takže s ní změříte azimut na mapě a přenesete ho do terénu. '
        'V běžné řeči i v e-shopech se oba názvy zaměňují a pod slovem „kompas“ se často prodávají buzoly. Pokud chcete navigovat s mapou, potřebujete buzolu.</p>'
        '<p>Základní použití se dá naučit za odpoledne: přiložíte hranu buzoly na mapu mezi místo, kde stojíte, a cíl, otočíte kruhem tak, aby jeho čáry mířily k severu mapy, '
        'a pak se v terénu natočíte, až střelka zapadne do vyznačené branky. Směrová šipka ukazuje, kudy jít. '
        'V Česku je potřeba pamatovat na magnetickou deklinaci, která je dnes zhruba 5 až 6 stupňů východně.</p>'
    ),
    sections=[
        dict(h2='Rozdíl mezi kompasem a buzolou',
             html=(
                 '<p>Kompas určí světové strany. Když víte, kde je sever, odvodíte jih, východ, západ i jakýkoli úhel. Pro hrubou orientaci, třeba „vrátit se na sever k silnici“, stačí. '
                 'Buzola k tomu přidává možnost měřit úhly přesně a pracovat s mapou. Česká Wikipedie ji popisuje jako kompas doplněný otočným úhloměrem k měření azimutu.</p>'
                 + T(['', 'Kompas', 'Buzola'], [
                     ['Ukazuje sever', 'ano', 'ano'],
                     ['Měří azimut ve stupních', 'jen přibližně, pokud má stupnici na pouzdře', 'ano, na otočném kruhu'],
                     ['Práce s mapou', 'omezená', 'pravítko, měřítka, orientační čáry'],
                     ['Typické použití', 'klíčenka, auto, hrubá orientace', 'turistika, orientační běh, horské túry'],
                 ])
                 + '<p>Azimut je úhel mezi směrem k severu a směrem k cíli měřený ve směru hodinových ručiček. Sever má 0°, východ 90°, jih 180° a západ 270°.</p>'
             )),
        dict(h2='Z čeho se skládá buzola',
             html=(
                 '<p>Názvy dílů se mezi výrobci trochu liší, ale princip je u všech destičkových buzol stejný:</p>'
                 '<ul><li><strong>Průhledná destička</strong> s rovnou hranou, pravítkem a často i měřítky map, například 1 : 25 000 a 1 : 50 000.</li>'
                 '<li><strong>Směrová šipka</strong> vyrytá na destičce ukazuje směr pochodu.</li>'
                 '<li><strong>Otočné pouzdro</strong> s kapalinou, ve kterém se pohybuje střelka. Kapalina tlumí kmitání.</li>'
                 '<li><strong>Stupnice na otočném kruhu</strong> (limbus) se dělením po jednom nebo dvou stupních.</li>'
                 '<li><strong>Orientační šipka a čáry</strong> na dně pouzdra. Šipce se říká také branka, střelka do ní při měření „zapadne“.</li>'
                 '<li><strong>Magnetická střelka</strong>, jejíž severní konec bývá červený nebo svítící.</li>'
                 '<li><strong>Index</strong>, ryska u kruhu, na které se odečítá azimut.</li>'
                 '<li>Podle modelu také <strong>lupa</strong>, <strong>stupnice nebo šroubek pro korekci deklinace</strong>, <strong>sklonoměr</strong> (klinometr) a <strong>zrcátko s průzorem</strong> pro přesné zaměření.</li></ul>'
             )),
        dict(h2='Typy buzol a kompasů',
             html=(
                 '<ul><li><strong>Destičková buzola:</strong> nejuniverzálnější typ pro turistiku. Lehká, levná, dobře se s ní pracuje na mapě.</li>'
                 '<li><strong>Zrcadlová buzola:</strong> má výklopné víčko se zrcátkem a ryskou. Při zaměřování vidíte současně cíl i střelku, takže měření je přesnější. Víčko zároveň chrání pouzdro.</li>'
                 '<li><strong>Palcová buzola pro orientační běh:</strong> nasazuje se na palec a drží se s mapou v jedné ruce. Některé modely nemají azimutovou stupnici, protože se směr přenáší přímo z mapy. Vyrábí se pro levou i pravou ruku.</li>'
                 '<li><strong>Vojenská buzola:</strong> často dělí kruh na dílce místo stupňů. V armádách NATO má kruh 6 400 dílců.</li>'
                 '<li><strong>Kapesní kompas a kompas na klíčenku:</strong> ukáže sever, na navigaci podle mapy nestačí.</li>'
                 '<li><strong>Kompasy pro kolo, kajak a potápění:</strong> upevňují se na řídítka, palubu nebo zápěstí a mají velkou čitelnou stupnici.</li></ul>'
                 '<p>Výběr najdete v kategorii <a href="/buzoly-a-kompasy/">buzoly a kompasy</a>, širší nabídku optiky v kategorii <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>.</p>'
             ), cat='buzoly-a-kompasy', n=4),
        dict(h2='Jak zorientovat mapu podle buzoly',
             html=(
                 '<p>Zorientovaná mapa leží tak, že sever na mapě míří k severu ve skutečnosti. Cesty a potoky pak vedou stejným směrem jako v terénu a mnohem snáz poznáte, kde jste.</p>'
                 '<ol><li>Položte mapu na rovnou plochu nebo ji držte vodorovně.</li>'
                 '<li>Otočte kruhem buzoly na 0° (sever na indexu).</li>'
                 '<li>Přiložte hranu buzoly podél svislé čáry mapy tak, aby směrová šipka mířila k hornímu okraji mapy.</li>'
                 '<li>Otáčejte celou mapou i s buzolou, dokud se severní konec střelky nekryje s orientační šipkou.</li></ol>'
                 '<p>Pro běžnou turistiku tak mapu zorientujete dostatečně přesně. Na delší vzdálenost a při navigaci mimo cesty je potřeba započítat deklinaci, o které píšeme níže.</p>'
             )),
        dict(h2='Jak určit azimut z mapy a jít podle něj',
             html=(
                 '<p>Tento postup se hodí, když víte, kde jste, a chcete dojít k bodu, ke kterému nevede značená cesta. Mapu přitom nemusíte orientovat.</p>'
                 '<ol><li><strong>Spojte start a cíl:</strong> přiložte delší hranu buzoly na mapu tak, aby spojovala vaše stanoviště s cílem. Směrová šipka musí mířit k cíli, ne opačně.</li>'
                 '<li><strong>Nastavte kruh:</strong> otáčejte kruhem, dokud orientační čáry v pouzdře nejsou rovnoběžné se svislými čarami mapy a orientační šipka nemíří k severnímu okraji mapy. Střelky si teď nevšímejte.</li>'
                 '<li><strong>Odečtěte azimut</strong> na indexu a případně ho opravte o deklinaci.</li>'
                 '<li><strong>Natočte se v terénu:</strong> držte buzolu vodorovně před tělem, směrovou šipkou od sebe, a otáčejte se celým tělem, dokud severní konec střelky nezapadne do orientační šipky.</li>'
                 '<li><strong>Vyberte si cíl v dálce:</strong> zaměřte strom, skálu nebo sloup ve směru šipky a dojděte k němu. Pak zaměřte další bod. Je to přesnější než jít se zrakem upřeným na buzolu.</li></ol>'
                 '<p>Když vám v cestě stojí překážka, obejděte ji v pravých úhlech a počítejte kroky, abyste se vrátili na původní linii.</p>'
             )),
        dict(h2='Jak zaměřit azimut v terénu a najít svou polohu',
             html=(
                 '<p>Opačný postup použijete, když vidíte výrazný bod, například rozhlednu nebo vrchol, a chcete zjistit, kde na mapě stojíte.</p>'
                 '<ol><li>Namiřte směrovou šipku na vybraný bod. U zrcadlové buzoly se dívejte průzorem a v zrcátku sledujte střelku.</li>'
                 '<li>Otáčejte kruhem, až orientační šipka obklopí severní konec střelky. Na indexu přečtete azimut k bodu.</li>'
                 '<li>Opravte azimut o deklinaci, tentokrát opačným směrem než při přenosu z mapy.</li>'
                 '<li>Přiložte buzolu na mapu tak, aby hrana procházela zaměřeným bodem a orientační čáry byly rovnoběžné se svislými čarami mapy. Podél hrany narýsujte čáru.</li>'
                 '<li>Totéž zopakujte s druhým bodem, ideálně zhruba v pravém úhlu k prvnímu. Kde se čáry protnou, tam stojíte.</li></ol>'
                 '<p>Přesnost závisí na tom, jak pečlivě zaměříte, a na úhlu mezi oběma body. Když se čáry protínají pod velmi ostrým úhlem, chyba roste.</p>'
             )),
        dict(h2='Magnetická deklinace v Česku',
             html=(
                 '<p>Střelka neukazuje k zeměpisnému severnímu pólu, ale k magnetickému. Úhel mezi oběma směry se jmenuje magnetická deklinace a mění se podle místa i v čase. '
                 'Podle světového magnetického modelu WMM 2025 je na podzim 2026 v Česku deklinace východní: kolem 4,7° na Chebsku, asi 5,2° v Praze, 5,6° v Brně a 6,0° v Ostravě. '
                 'Každý rok se zvětšuje zhruba o desetinu stupně.</p>'
                 '<p>Při východní deklinaci platí:</p>'
                 '<ul><li><strong>z mapy do terénu</strong> deklinaci od azimutu odečtěte (mapový azimut 90° v Praze znamená na buzole asi 85°),</li>'
                 '<li><strong>z terénu do mapy</strong> deklinaci k azimutu přičtěte.</li></ul>'
                 '<p>Proč na tom záleží: chyba 5 stupňů vás na kilometr cesty odchýlí zhruba o 87 metrů. Při chůzi po značené cestě to nevadí, při hledání chaty v mlze nebo v lese mimo cesty už ano. '
                 'Pohodlnější je buzola se šroubkem nebo stupnicí pro korekci deklinace, kterou nastavíte jednou a dál pracujete bez počítání.</p>'
                 '<p>Pozor také na čáry v mapě. Svislé čáry souřadnicové sítě nemusejí přesně mířit k zeměpisnému severu. Když je potřeba velká přesnost, podívejte se do legendy mapy, '
                 'co čáry znamenají a jakou odchylku vydavatel uvádí.</p>'
             )),
        dict(h2='Co buzolu ruší a jak se vyhnout chybám',
             html=(
                 '<ul><li><strong>Kov a magnety v blízkosti:</strong> mobil, magnetické zapínání pouzdra, kapsa s klíči, nůž, kovová přezka batohu. Při měření je dejte stranou.</li>'
                 '<li><strong>Elektrická vedení, auta, železné zábradlí a koleje:</strong> měřte několik metrů od nich.</li>'
                 '<li><strong>Nakloněná buzola:</strong> střelka se dře o pouzdro. Držte buzolu vodorovně.</li>'
                 '<li><strong>Otočená šipka:</strong> když směrová šipka míří od cíle, půjdete opačným směrem. Před vyrážením si vždy ověřte, že severní konec střelky je v orientační šipce.</li>'
                 '<li><strong>Vyvážení střelky:</strong> střelka je vyvážená pro magnetické pole určité části světa. Buzola koupená v Evropě funguje v celé severní polokouli, na cesty na jižní polokouli zvolte model s globální střelkou.</li></ul>'
                 '<p>Buzolu skladujte mimo reproduktory, magnety a elektroniku. Přepólovaná střelka, která ukazuje na jih, se vyskytne vzácně, ale stojí za to buzolu občas porovnat se známým směrem.</p>'
             )),
        dict(h2='Buzola, mobil, nebo hodinky',
             html=(
                 '<p>Mapy v mobilu a GPS v hodinkách navigaci velmi usnadnily a na značených trasách je většina lidí používá. '
                 'Elektronika ale potřebuje baterii, v zimě se rychleji vybíjí a digitální kompas je nutné kalibrovat. Buzola funguje bez energie a v jakémkoli počasí.</p>'
                 '<p>Rozumná kombinace na horské túry je papírová mapa, buzola a k tomu mobil nebo <a href="/sportovni-hodinky/">sportovní hodinky</a> s GPS. '
                 'Kdo chodí do terénu za tmy, přibalí <a href="/celovky-a-svitilny/">čelovku</a>, protože buzola se svítícími prvky čtení mapy nenahradí. '
                 'Vše se vejde do bočních kapes <a href="/turisticke-batohy/">turistického batohu</a>.</p>'
             ), cat='sportovni-hodinky', n=4),
        dict(h2='Jak vybrat buzolu',
             html=(
                 '<ol><li><strong>Účel:</strong> na turistiku a výlety s dětmi stačí jednoduchá destičková buzola. Na hory a do mlhy se hodí zrcadlová s korekcí deklinace. Na orientační běh palcová.</li>'
                 '<li><strong>Pouzdro s kapalinou:</strong> střelka se rychle ustálí a méně kmitá při chůzi.</li>'
                 '<li><strong>Měřítka:</strong> ověřte, že odpovídají mapám, které používáte. Turistické mapy v Česku vycházejí nejčastěji v měřítku 1 : 50 000.</li>'
                 '<li><strong>Dělení stupnice:</strong> po dvou stupních stačí na turistiku, jemnější dělení se hodí na přesnou práci.</li>'
                 '<li><strong>Doplňky:</strong> lupa na drobné popisky, svítící body pro šero, šňůrka na krk a sklonoměr pro odhad sklonu svahu.</li></ol>'
                 '<p>V nabídce českých obchodů najdete buzoly značek jako Silva, Suunto nebo Highlander i levné kapesní kompasy. Na Sportece porovnáte ceny jednoho modelu napříč obchody.</p>'
             )),
        dict(h2='Jak se navigaci naučit',
             html=(
                 '<p>Buzolu si nejdřív vyzkoušejte v terénu, který znáte, třeba v lese za domem. Zaměřte si azimut na známé místo a ověřte, kam vás dovede. '
                 'Dobrou školou jsou oddíly orientačního běhu a turistické kroužky, kde se navigace učí i děti hrou.</p>'
                 '<p>Na hory a do neznámého terénu vyrážejte s rezervou času a s plánem, kudy se vrátit. Buzola a mapa pomohou, ale nenahradí zkušenost ani ohled na počasí.</p>'
             )),
    ],
    faq=[
        ('Jaký je rozdíl mezi buzolou a kompasem?', '<p>Kompas ukazuje jen sever. Buzola je kompas s otočným úhloměrem a průhlednou destičkou, takže s ní změříte azimut na mapě a přenesete ho do terénu.</p>'),
        ('Proč se buzoly prodávají jako kompasy?', '<p>V angličtině se pro obojí používá slovo compass a čeština oba výrazy běžně zaměňuje. Podle popisu poznáte buzolu tak, že má otočný kruh se stupnicí a pravítko.</p>'),
        ('Jak se používá kompas?', '<p>Držte ho vodorovně, dál od kovů a elektroniky, a počkejte, až se střelka ustálí. Její severní konec, obvykle červený, ukazuje k magnetickému severu.</p>'),
        ('Co je azimut?', '<p>Úhel mezi severem a směrem k cíli, měřený ve směru hodinových ručiček od 0° do 360°. Východ má 90°, jih 180° a západ 270°.</p>'),
        ('Jaká je magnetická deklinace v Česku?', '<p>Podle modelu WMM 2025 je v roce 2026 východní, zhruba 4,7° na západě republiky a 6° na východě. Ročně roste přibližně o desetinu stupně.</p>'),
        ('Musím deklinaci při turistice počítat?', '<p>Na značených cestách ne. Při navigaci mimo cesty, v mlze nebo na delší vzdálenosti ano, protože 5° znamená odchylku asi 87 metrů na kilometr.</p>'),
        ('Funguje česká buzola i v zahraničí?', '<p>V celé severní polokouli ano. Na jižní polokouli může střelka drhnout, proto se tam hodí buzola s globální střelkou.</p>'),
        ('Proč buzola ukazuje špatně?', '<p>Nejčastěji ji ruší kov nebo magnet v blízkosti, například mobil, klíče nebo magnetické zapínání. Chybu způsobí i nakloněná buzola nebo blízkost elektrického vedení.</p>'),
        ('Jakou buzolu koupit pro děti?', '<p>Jednoduchou destičkovou buzolu s čitelnou stupnicí a pravítkem. Dětem se hodí šňůrka na krk a výrazná barva, aby se v trávě neztratila.</p>'),
    ],
    cats=['buzoly-a-kompasy', 'dalekohledy-a-kompasy', 'sportovni-hodinky', 'turisticke-batohy'],
    updated='2026-11-18',
)
