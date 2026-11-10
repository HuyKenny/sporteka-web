"""sporteka.cz — wave 21a (4. 11. 2026): long texts (>= 1650 words) for hrazdy-a-bradla, varice-a-kartuse, lovecke-vybaveni, brusle.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ hrazdy-a-bradla
NEW['hrazdy-a-bradla'] = dict(long=True,
    title='Hrazdy a bradla: do dveří, na zeď, žebřiny i rybářské',
    desc='Hrazdy a bradla na shyby, kliky a dipy: dveřní, nástěnné, stropní, žebřiny i rybářské. Jak vybrat, namontovat a porovnat nabídky obchodů.',
    intro='<p>Hrazda a bradla patří k nejefektivnějšímu vybavení pro cvičení s vlastní vahou. Stačí pár čtverečních metrů, a naučíte se shyby, výdrže, dipy, zdvihy nohou i základy kalistheniky. Zároveň je to kategorie s překvapivě širokou nabídkou: od dveřní tyče, kterou během minuty vyndáte, přes nástěnné modely a žebřiny až po samostatně stojící stanice s bradly.</p>'
          '<p>Najdete tu také dětské sestavy do bytu a překvapivě i <em>rybářské hrazdy</em> na pruty, které s posilováním nemají nic společného, ale nesou stejný název. Sporteka porovnává nabídky českých obchodů u značek jako '
          + B(('insportline', 'Insportline'), ('hms', 'HMS'), ('ma-piszon', 'Małpiszon'), ('benchk', 'Benchk'), ('marbo', 'Marbo'), ('rinagym', 'Rinagym'), ('hop-sport', 'Hop-sport'), ('gymbeam', 'GymBeam')) +
          '. Pro skladbu domácího tréninku se hodí také <a href="/funkcni-trenink/">funkční trénink</a>, <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>',
    guide='<h2>Jaké druhy hrazdy a bradel existují</h2>'
          '<p>Základní rozdíl je ve způsobu upevnění. Každé řešení mívá jiné omezení pro dveře, zeď nebo podlahu, takže nejdřív zvažte, kde a jak často budete cvičit. Teprve potom řešte materiál a šířku úchopu.</p>'
          + T(['Typ', 'Upevnění', 'Hodí se pro'], [
              ['Dveřní hrazda', 'zaklesnutí do zárubně nebo vzpěra mezi rámy', 'byt, nájem, příležitostné shyby'],
              ['Nástěnná hrazda', 'šrouby do zdi nebo stropu', 'trvalé domácí cvičení, pevný úchop'],
              ['Žebřiny s hrazdou', 'opřené o zeď, často i se šrouby', 'děti, rodiny, rozcvičky a protahování'],
              ['Samostatně stojící stanice', 'vlastní stabilní rám', 'shyby, dipy, zdvihy nohou bez vrtání'],
              ['Bradla a parallettes', 'stojan nebo malá madla na podlaze', 'kliky, dipy, L-sit, kalistenika'],
              ['Rybářské hrazdy', 'stojan nebo podstavec k prutům', 'kaprařina, nesouvisí s posilováním']]) +
          '<p>Samostatná kategorie jsou <strong>žebřiny</strong>, často kombinované s hrazdou na shyby a někdy i s bradly. Mají oporu o stěnu, ale hodí se i do dětského pokoje, kde se děti přirozeně učí šplhat a viset. U modelů typu Benchk nebo HMS ověřte maximální zatížení a výšku, kterou strop ještě dovolí.</p>'
          '<h2>Dveřní hrazda: co musíte zkontrolovat</h2>'
          '<p>Dveřní hrazdy jsou nejoblíbenější volba, protože nevyžadují vrtání. Existují tři konstrukce: zaklesnutí za horní rám zárubně, teleskopická vzpěra mezi dvěma rámy a model s opěrami na zeď. Každá se hodí do jiných dveří a nelze je zaměnit.</p>'
          '<ul><li><strong>Šířka zárubně:</strong> hrazda musí odpovídat rozměrům otvoru. Změřte ji včetně obložení.</li>'
          '<li><strong>Materiál zárubně:</strong> tenké sádrokartonové a lehké dřevěné rámy neunesou prudké kývání. U starších panelových domů a masivních zárubní bývá situace lepší.</li>'
          '<li><strong>Ochrana povrchu:</strong> gumové koncovky a měkké podložky zabrání odření omítky a laku.</li>'
          '<li><strong>Pevnost:</strong> zatěžujte ji postupně a pohyby dělejte plynule, bez švihu a trhnutí.</li></ul>'
          '<p>Pokud hrazdu používáte denně nebo cvičíte výbušné prvky, vyplatí se přejít na nástěnnou variantu nebo na samostatně stojící konstrukci.</p>'
          '<h2>Nástěnné a stropní hrazdy a montáž</h2>'
          '<p>Pevná montáž je nejbezpečnější, pokud stěnu předem zkontrolujete. Cihlová nebo betonová zeď unese víc než sádrokarton, ale i tam musíte použít hmoždinky vhodné pro daný materiál. Vrtáním do panelových nebo bytových stěn zvažte souhlas majitele a vyhněte se trasám elektřiny a vody.</p>'
          '<p>Zkuste si před montáží určit potřebný prostor. Nad hlavou potřebujete rezervu pro vytažení brady nad tyč, po stranách místo pro pohyb loktů a před hrazdou volný prostor pro švih nohou. Označte si výšku tak, aby se při visu chodidla nedotýkala podlahy, a zároveň nehrozil kontakt hlavy se stropem.</p>'
          '<h2>Šířka úchopu a průměr tyče</h2>'
          '<p>Rovná tyč umožňuje široký, užší i střídavý úchop, ale rameno a zápěstí zatěžuje v jedné poloze. Hrazdy s vícenásobnými madly nabízejí neutrální úchop dlaněmi proti sobě, který bývá šetrnější ke kloubům. Pro začátečníky je to praktická volba, protože dovolí postupně přecházet mezi variantami.</p>'
          + T(['Úchop', 'Co zatěžuje víc', 'Poznámka'], [
              ['Nadhmat (dlaně od sebe)', 'široký sval zádový, ramena', 'klasický shyb, náročnější pro začátečníky'],
              ['Podhmat (dlaně k tělu)', 'bicepsy, horní záda', 'chin-up, o něco snazší pro mnoho cvičenců'],
              ['Neutrální úchop', 'záda i ruce vyváženě', 'šetrnější k zápěstí a loktům'],
              ['Úzký úchop', 'ruce a střed zad', 'pro doplňkové varianty']]) +
          '<p>Průměr tyče ovlivňuje sílu úchopu. Tenčí tyč se drží lépe, silnější se hůř svírá a trénuje předloktí. Pokud vás při cvičení pálí dlaně, pomohou magnézium, rukavice bez prstů nebo hrazda s pěnovým potahem.</p>'
          '<h2>Bradla a parallettes</h2>'
          '<p>Bradla slouží hlavně ke dipům a zdvihům nohou. Stanice se dvěma ramenem v pevné výšce zvládne i těžší cvičence, nastavitelné modely se přizpůsobí výšce postavy a lze je složit. Ve Sportece najdete značky jako Marbo, Rinagym nebo GymBeam, případně sety bradel s hrazdou.</p>'
          '<p><strong>Parallettes</strong> jsou nízká madla, která pokládáte na podlahu. Vhodná jsou na kliky s větším rozsahem pohybu, L-sit, výdrže v podporu i stoje na rukou. Potřebují protiskluzovou podložku, ideálně z kategorie <a href="/joga-a-podlozky/">jóga a podložky</a>. Menší rozměr a nízká váha z nich dělají praktickou volbu do bytu.</p>'
          '<h2>Výběr podle cíle</h2>'
          '<ul><li><strong>Začátečník:</strong> dveřní hrazda a odporová guma, která zmírní váhu těla při prvních shybech. Doplňte ji sadou <a href="/posilovaci-gumy/">posilovacích gum</a>.</li>'
          '<li><strong>Pokročilý domácí cvičenec:</strong> nástěnná hrazda a bradla, případně <a href="/kettlebelly/">kettlebelly</a> k doplňkovému tréninku.</li>'
          '<li><strong>Kalistenika:</strong> samostatně stojící konstrukce s bradly, parallettes a závěsné kruhy.</li>'
          '<li><strong>Rodina s dětmi:</strong> žebřiny s hrazdou, měkká podlaha a bezpečný odstup od nábytku. Další pomůcky najdete v <a href="/gymnasticke-pomucky/">gymnastických pomůckách</a>.</li>'
          '<li><strong>Kombinace s posilovnou:</strong> hrazda jako doplněk k <a href="/cinky-a-kotouce/">činkám a kotoučům</a> a <a href="/posilovaci-stroje/">posilovacím strojům</a>.</li></ul>'
          '<h2>Rybářské hrazdy: pozor na záměnu názvu</h2>'
          '<p>Mezi výsledky se objeví také <em>hrazdy na pruty</em>, tedy lehké stojany s hlavicemi pro kapří pruty a signalizátory záběru. Nejčastěji je dělá Korda, Korum, Carp Spirit nebo Giants Fishing, vyrobené z nerezu nebo hliníku, s nastavitelnou šířkou a počtem prutů. Pokud hledáte rybářskou verzi, pokračujte v kategorii <a href="/rybarske-doplnky/">rybářské doplňky</a> nebo <a href="/rybarske-pruty/">rybářské pruty</a>. K nim patří také pouzdra na hrazdy a příslušenství, které kategorie obsahuje.</p>'
          '<h2>Technika a bezpečnost</h2>'
          '<p>Před zatížením vždy zkontrolujte pevnost uchycení, šrouby a utažení vzpěr. Na začátku cvičení se zahřejte, protože studená ramena a lokty jsou nejčastějším místem přetížení. Dbejte na plný rozsah pohybu a pomalý sestup, nehoupejte se a nepoužívejte švih, pokud ho nevyžaduje konkrétní cvik.</p>'
          '<p>Pokud trpíte bolestmi ramen nebo zad, poraďte se s fyzioterapeutem, než začnete s tréninkem na hrazdě. Hrazda totiž zatěžuje úchop, lokty i ramena víc, než by se na první pohled zdálo.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Kovové části otřete od potu, aby nekorodovaly. Potahy na madlech se čistí vlhkým hadříkem, pěnu nenamáčejte. Pravidelně kontrolujte šrouby, hmoždinky a gumové patky, zejména u dveřních konstrukcí, které se při každém použití malinko posouvají. Poškozený díl vyměňte, než se pokazí celek.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě dveřní hrazdy bez změření zárubně.</li>'
          '<li>Podcenění prostoru nad hlavou a před hrazdou.</li>'
          '<li>Ignorování maximálního zatížení uvedeného výrobcem.</li>'
          '<li>Přeskočení zahřátí a prudký start s výbušnými prvky.</li>'
          '<li>Záměna sportovní a rybářské hrazdy.</li></ul>'
          '<h2>Jednoduchý plán pro první měsíce</h2>'
          '<p>Nejčastější důvod, proč hrazda skončí jako věšák na ručníky, je chybějící plán. Pomůže jednoduchý rytmus: dvakrát až třikrát týdně krátká série, vždy s pauzou mezi sériemi, a postupné zvyšování. V prvních týdnech se soustřeďte na kvalitu pohybu, ne na počet opakování. Do plánu zařaďte tři druhy cviků: vis na rovných pažích pro zpevnění úchopu, tahy k tyči pro záda a výdrže v horní poloze pro sílu.</p>'
          '<ul><li><strong>Vis a výdrže:</strong> učí tělo unést vlastní váhu a posilují předloktí. Prodlužujte je po vteřinách.</li>'
          '<li><strong>Negativní shyby:</strong> vyskočíte nahoru a pomalu klesáte. Je to nejrychlejší cesta k prvnímu samostatnému shybu.</li>'
          '<li><strong>Zdvihy kolen a nohou:</strong> posilují břicho a stabilizují trup, takže se při shybech méně houpete.</li>'
          '<li><strong>Doplňkové cviky:</strong> kliky, veslování s gumou a cviky na lopatky, které chrání ramena.</li></ul>'
          '<p>Až zvládnete několik čistých opakování, přidejte zátěž, například <a href="/cinky-a-kotouce/">kotouč</a> v batohu nebo pásek se závažím. Pokrok je pomalejší než v posilovně, ale hrazda ho odmění stabilní silou horní poloviny těla.</p>'
          '<h2>Prostor, podlaha a hluk</h2>'
          '<p>Při cvičení doma myslete na sousedy i na podlahu. Dopady z výskoků hlučí, proto pod hrazdu položte tlumicí podložku. U nástěnných modelů zkontrolujte, zda se nad hrazdou nenachází lustr nebo police. Samostatně stojící konstrukce vyžadují rovnou plochu a rezervu kolem sebe, aby nehrozil pád na nábytek. Pro cvičení venku si hledejte modely z lakovaného nebo pozinkovaného kovu, které snesou vlhko, a po dešti je otřete.</p>'
          '<p>Pro společné cvičení a skupiny se hodí vyšší hrazda s více úchopy. Děti naopak potřebují nižší výšku a pod hrazdou měkkou podložku, kterou najdete v kategorii <a href="/fitness/">fitness</a>. Dopad na tvrdou podlahu patří k nejčastějším příčinám úrazů.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého produktu vidíte nabídky obchodů vedle sebe, takže snadno zjistíte, kdo má hrazdu skladem a s jakým doručením. Filtrujte podle značky a hledejte přesný název modelu. Před nákupem zkontrolujte rozměry, maximální zatížení a materiál, a pokud nevíte, kam hrazdu připevnit, vyberte radši samostatně stojící konstrukci.</p>',
    faq=[
        ('Unese dveřní hrazda shyby každý den?', 'Záleží na zárubni a konstrukci. Pevné zárubně a kvalitní uchycení zvládnou pravidelné cvičení, ale každá dveřní hrazda je kompromis. Při denním tréninku nebo výbušných prvcích je bezpečnější nástěnná nebo samostatně stojící varianta.'),
        ('Poškodí hrazda dveře nebo zárubeň?', 'Může, pokud ji nainstalujete na slabý rám nebo bez ochranných podložek. Měkké koncovky a rovnoměrné rozložení tlaku riziko snižují, ale nikdy ho zcela neodstraní. U pronajatého bytu je rozumné počítat s možným otlakem.'),
        ('Kam namontovat nástěnnou hrazdu?', 'Na pevnou cihlovou nebo betonovou zeď, případně do nosné konstrukce. Použijte hmoždinky pro daný materiál a nevrtejte do míst, kde vedou kabely nebo trubky. Při pochybnostech požádejte odborníka.'),
        ('Jaký úchop je nejlepší pro začátečníky?', 'Většině lidí vyhovuje podhmat nebo neutrální úchop, protože do pohybu zapojí víc svalů. Nadhmat je náročnější, ale pro záda a ramena velmi účinný, proto se do tréninku přidává postupně.'),
        ('Co dělat, když ještě nezvládnu jediný shyb?', 'Začněte negativními shyby, visy, shyby s gumou nebo cviky s nízkou hrazdou. Postupně se zvyšuje počet opakování i délka výdrže.'),
        ('Jsou žebřiny vhodné i pro dospělé?', 'Ano, pokud mají dost pevnou konstrukci a uvedené maximální zatížení. Hodí se pro protahování, zdvihy nohou i shyby na přídavné hrazdě. Pro dospělé hledejte vyšší a široké modely.'),
        ('Jaký je rozdíl mezi bradly a parallettes?', 'Bradla jsou vyšší a stojí na podlaze nebo ve stojanu, parallettes jsou nízká madla pro cvičení v blízkosti podlahy. Bradla se hodí na dipy, parallettes na kliky s větším rozsahem a výdrže.'),
        ('Proč mezi hrazdami najdu rybářské vybavení?', 'Protože se obě věci jmenují hrazda. Rybářská hrazda je stojan pro pruty a signalizátory záběru, s posilováním nemá nic společného. Rybářské verze poznáte podle zmínky o prutech nebo značek jako Korda a Giants Fishing.'),
        ('Jak často mohu cvičit na hrazdě?', 'Většina rekreačních cvičenců cvičí dva až čtyřikrát týdně a mezitím nechává svalům čas na regeneraci. Pokud vás bolí lokty nebo ramena, trénink zkraťte a poraďte se s odborníkem.'),
        ('Jak zjistím, jestli hrazda unese moji váhu?', 'Vždy se řiďte údajem o maximálním zatížení od výrobce. Počítejte s rezervou, protože při dynamických pohybech působí na uchycení větší síla než samotná váha těla.'),
    ])

# ------------------------------------------------------------------ varice-a-kartuse
NEW['varice-a-kartuse'] = dict(long=True,
    title='Vařiče a kartuše: plynové, lihové, tuhé palivo',
    desc='Turistické vařiče a plynové kartuše: Jetboil, Primus, Fire-Maple, Campingaz, Meva. Jak vybrat typ vařiče, kartuši a porovnat nabídky obchodů.',
    intro='<p>Teplé jídlo nebo čaj na vrcholu, u stanu nebo v lese po náročném dni dokážou změnit celý výlet. Aby se to povedlo, musí vařič odpovídat typu túry: na lehký víkend stačí kompaktní plynový hořák, pro zimu se hodí systém s regulací a lepším odolným palivem, pro dvoučlennou rodinu v kempu pohodlný dvouplotýnkový model.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u vařičů a kartuší od značek '
          + B(('jetboil', 'Jetboil'), ('primus', 'Primus'), ('fire-maple', 'Fire-maple'), ('campingaz', 'Campingaz'), ('meva', 'Meva'), ('pinguin', 'Pinguin'), ('optimus', 'Optimus'), ('esbit', 'Esbit'), ('coleman', 'Coleman')) +
          '. K vaření v přírodě patří i <a href="/vareni-v-prirode/">celkový přehled vaření v přírodě</a>, <a href="/kempingove-nadobi/">kempingové nádobí</a>, <a href="/outdoorova-strava/">outdoorová strava</a> a <a href="/kemping/">kempingové vybavení</a>. Níže najdete rozdělení typů, rady k palivu a bezpečnému používání.</p>',
    guide='<h2>Jaké druhy vařičů existují</h2>'
          '<p>Hlavní rozdíl je v palivu a ve způsobu použití. Plynové vařiče jsou nejpohodlnější, lihové a tuhé palivo zase nejjednodušší a nejtišší, a každý typ má jiný poměr váhy, výkonu a ceny provozu.</p>'
          + T(['Typ', 'Palivo', 'Hodí se pro'], [
              ['Hořák na kartuši', 'směs plynů ve šroubovací nebo ventilové kartuši', 'turistika, trek, rychlý ohřev vody'],
              ['Integrovaný systém (Jetboil, Fire-Maple)', 'kartuše se speciální nádobou', 'velmi rychlý ohřev vody a instantní jídla'],
              ['Kempingový vařič s 1 až 2 hořáky', 'kartuše nebo větší lahev', 'auto, stan, rodinný kemp'],
              ['Lihový vařič', 'denaturovaný líh', 'minimalistické túry, tichý provoz'],
              ['Tuhé palivo (Esbit)', 'tablety', 'nouzové a ultralehké vaření'],
              ['Vojenské a bushcraft sady', 'kombinované', 'přežití, outdoorový styl']]) +
          '<h2>Plynové vařiče na kartuši</h2>'
          '<p>Nejvíc uživatelů volí právě tento typ. Zapalování je rychlé, plamen se dá regulovat a vařič se vejde i do malého kotlíku. Hořáky se liší hmotností, konstrukcí ramen, stabilitou a odolností proti větru. Menší a lehčí modely jsou vhodné pro ohřev vody, širší hořák se hodí i pro vaření v hrnci.</p>'
          '<p>Při výběru sledujte stabilní podstavec nebo plochu, kvalitu piezo zapalování a jemnost regulace. Piezo selhává při vlhkosti nebo mrazu, takže si vždy vezměte i zapalovač nebo sirky.</p>'
          '<h2>Integrované systémy typu Jetboil</h2>'
          '<p>Tyto sestavy spojují hořák, hrnec s výměníkem tepla a izolační obal. Vodu ohřejí rychle a spotřebují méně paliva, což oceníte u tras s omezenou zásobou kartuší. Hodí se na čaj, kávu a lyofilizované jídlo. Na přípravu složitějších pokrmů, smažení nebo vaření těstovin jsou méně praktické a rozměrově i hmotnostně se vyplatí hlavně u delších túr.</p>'
          '<p>K systémům Jetboil si často přikoupíte doplňky, jako jsou podpěry hrnce, lžíce nebo sada pro pánev. Ty najdete v kategorii mezi samostatnými položkami a nabídky obchodů srovnáte stejně jako u samotných vařičů.</p>'
          '<h2>Kartuše: závit, ventil a směs plynů</h2>'
          '<p>Nejčastější chyba je koupě kartuše, která se na vařič nehodí. Existují závitové kartuše, které se našroubují přímo, a ventilové, které se zasouvají do držáku. Zkontrolujte tedy typ připojení u vařiče a kartuše, případně použijte adaptér. Adaptéry se prodávají jako samostatné příslušenství, ale používejte je pouze podle návodu výrobce.</p>'
          '<p>Směsi plynů se liší. Butan je levnější, ale při nízkých teplotách se hůře odpařuje. Propan a isobutan si s chladem poradí lépe, proto se kartuše pro zimu a hory prodávají jako směsi s vyšším podílem těchto složek. Složení směsi vždy čtěte na obalu kartuše.</p>'
          + T(['Situace', 'Doporučení pro kartuši', 'Proč'], [
              ['Léto, nižší nadmořská výška', 'běžná směs', 'plyn se odpařuje spolehlivě'],
              ['Jaro, podzim, noční mrazíky', 'směs s isobutanem a propanem', 'lepší výkon v chladu'],
              ['Zima, vyšší hory', 'zimní směs, kartuši držet v teple', 'zabrání poklesu tlaku'],
              ['Dlouhá výprava', 'větší kartuše nebo zásoba', 'méně výměn a větší jistota']]) +
          '<h2>Kolik paliva vzít</h2>'
          '<p>Spotřeba závisí na tom, kolik vody ohříváte, jak je venku zima a jak moc fouká. Pro orientaci si přibližně spočítejte počet jídel, přidejte ranní nápoje a pro jistotu nechte rezervu. Při zkoušce doma zapište, kolik paliva spotřebujete na litr vody, a na túru vezměte víc, než vám vychází. Lehčí kartuše jsou praktické na víkend, větší se hodí pro skupinu.</p>'
          '<h2>Lihové vařiče a tuhé palivo</h2>'
          '<p>Lihový vařič je jednoduchý, tichý a bez pohyblivých částí. Na druhé straně potřebuje déle na ohřev, hůř se reguluje a plamen je při bezvětří téměř neviditelný, takže s ním zacházejte opatrně. Skládá se z hořáku, stojánku a větrné clony. Pro nenáročné vaření a pro ty, kdo upřednostňují nízkou váhu, je výborná volba.</p>'
          '<p>Tuhé palivo Esbit je lehké a nenáročné na skladování, hodí se jako záloha. Za sebou však zanechává zbytky a zápach, nehodí se pro kuchyň uvnitř stanu a vaření trvá relativně dlouho.</p>'
          '<h2>Kempingové a rodinné vařiče</h2>'
          '<p>Pokud jedete autem, vyplatí se větší vařič s jedním nebo dvěma hořáky. Je stabilnější, výkonnější a přizpůsobí se většímu hrnci i pánvi. Dvouhořákové modely se hodí pro čtyřčlennou rodinu nebo pro vaření více jídel najednou. Vezměte v úvahu stabilitu stojanu, odolnost větrným clonám a hmotnost při přenášení.</p>'
          '<p>Přenosná plynová topidla na kartuši patří také do nabídky, ale slouží k vytápění, nikoliv k vaření. Používejte je podle návodu výrobce jen tam, kde je to výslovně dovoleno, a nikdy uvnitř stanu.</p>'
          '<h2>Výběr podle typu túry</h2>'
          '<ul><li><strong>Víkendový turista:</strong> kompaktní hořák, malý hrnek a jedna kartuše. Doplňte o <a href="/turisticke-batohy/">turistický batoh</a> a <a href="/lahve-a-termosky/">láhev nebo termosku</a>.</li>'
          '<li><strong>Trekař na více dní:</strong> integrovaný systém nebo hořák s účinným větrným štítem. Přidejte <a href="/outdoorova-strava/">outdoorovou stravu</a>.</li>'
          '<li><strong>Zimní výlety:</strong> kartuše se zimní směsí, vařič s dobrou regulací a ochrana před větrem. Chraňte kartuši před mrazem v bundě nebo ve <a href="/spaci-pytle/">spacáku</a>.</li>'
          '<li><strong>Rodinný kemp:</strong> dvouplotýnkový vařič a sada <a href="/kempingove-nadobi/">kempingového nádobí</a>.</li>'
          '<li><strong>Bushcraft a vojenský styl:</strong> lihový nebo skládací vařič a sady značky Mil-Tec.</li></ul>'
          '<h2>Bezpečnost při vaření</h2>'
          '<ul><li>Nikdy nevařte uvnitř stanu ani uzavřeného přístřešku. Hrozí požár i otrava oxidem uhelnatým.</li>'
          '<li>Vařič postavte na rovný a stabilní podklad, mimo hořlavé předměty.</li>'
          '<li>Kartuši nepřehřívejte a nezahřívejte přímým ohněm.</li>'
          '<li>Po použití zavřete ventil a před výměnou kartuše se ujistěte, že plamen zhasl.</li>'
          '<li>Při přepravě sledujte předpisy dopravce, zejména u letecké a kombinované dopravy. Plynové kartuše se do zavazadel většinou nesmějí.</li></ul>'
          '<h2>Péče a údržba</h2>'
          '<p>Po výletu hořák očistěte od zbytků jídla a zkontrolujte těsnění u závitu. Poškozené těsnění se musí vyměnit, jinak hrozí únik plynu. Kartuše skladujte na suchém místě, mimo zdroje tepla, a prázdné odevzdejte podle místních pravidel k recyklaci kovu. Pokud se vařič zanáší, použijte čisticí jehlu určenou pro daný model.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě kartuše s jiným připojením, než má vařič.</li>'
          '<li>Podcenění větru, který spotřebu výrazně zvýší, proto používejte clonu.</li>'
          '<li>Použití příliš velkého hrnce na malém hořáku.</li>'
          '<li>Vaření bez zkoušky doma. Ověřte si vařič před odjezdem.</li>'
          '<li>Skladování plynu v horkém autě.</li></ul>'
          '<h2>Co patří k vařiči</h2>'
          '<p>Samotný hořák nestačí. Spolu s ním potřebujete hrnec nebo hrnek vhodné velikosti, zapalovač, větrnou clonu a podložku pro stabilní postavení. Při vaření pro dva stačí menší hrnec do jednoho litru, pro skupinu větší kotlík nebo sada z kategorie <a href="/kempingove-nadobi/">kempingové nádobí</a>. Hrnce s tepelným výměníkem šetří palivo, ale jsou dražší a objemnější.</p>'
          '<ul><li><strong>Větrná clona:</strong> snižuje spotřebu a zrychluje vaření, ale nesmí se přibližovat ke kartuši, aby se nepřehřála.</li>'
          '<li><strong>Podložka pod kartuši:</strong> zlepší stabilitu na měkké půdě a sněhu.</li>'
          '<li><strong>Lžíce a příbory:</strong> dlouhá lžíce dosáhne na dno sáčku s jídlem a nemusíte si špinit ruce.</li>'
          '<li><strong>Pouzdro a obal:</strong> chrání batoh před zbytky a sazemi.</li>'
          '<li><strong>Zapalovač a sirky:</strong> vždy dvě varianty, kdyby piezo zapalování selhalo.</li></ul>'
          '<h2>Jak vařit rychle a hospodárně</h2>'
          '<p>Voda se ohřívá rychleji s víkem a v závětří. Hrnec nevařte nasucho a po uvaření plamen ihned zhasněte, ať šetříte plyn. Pro těstoviny a rýži se vyplatí nechat jídlo po krátkém uvaření dojít v izolovaném obalu. Taková úsporná metoda se hodí hlavně na delších túrách. Lyofilizovaná jídla z kategorie <a href="/outdoorova-strava/">outdoorová strava</a> vyžadují jen horkou vodu, takže se hodí i do integrovaných systémů.</p>'
          '<p>Při přípravě doma si zkuste vařič v zahradě nebo na balkoně, než s ním vyrazíte do hor. Poznáte jeho výkon, hlučnost i to, jak snadno se zapaluje. Zkouška ukáže také, jestli vám nechybí adaptér, podpěra pro menší hrnce nebo pevnější obal pro přepravu.</p>'
          '<h2>Tipy k přepravě a skladování</h2>'
          '<p>Vařič přenášejte v pevném pouzdru, aby se nepoškodil hořák ani zapalování. Kartuši vždy oddělte od vařiče, nenechávejte ji připojenou v batohu a nedávejte ji do blízkosti zdrojů tepla. Doma kartuše skladujte ve větrané místnosti, nejlépe ve stoje, a občas zkontrolujte, zda nejsou promáčknuté nebo zrezivělé. Zbylé palivo si poznamenejte, ať na další výlet nevyrazíte s téměř prázdnou kartuší.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého produktu uvidíte nabídky více obchodů a dostupnost. Pro vařiče a kartuše si ověřte zejména typ závitu, objem plynu a doporučené teploty. Doplňky, jako jsou adaptéry, podpěry hrnce nebo lžíce, najdete ve stejné kategorii, takže celou výbavu složíte na jednom místě.</p>',
    faq=[
        ('Jaký vařič je nejlepší na první túru?', 'Pro začátečníka je nejjednodušší kompaktní plynový hořák na kartuši. Rychle se zapálí, reguluje a je lehký. Pokud chcete hlavně ohřívat vodu na čaj a instantní jídlo, zvažte integrovaný systém.'),
        ('Pasuje každá kartuše na každý vařič?', 'Ne. Liší se závit a ventilové provedení. Před koupí zkontrolujte typ připojení u vařiče i kartuše, případně použijte adaptér a řiďte se návodem výrobce.'),
        ('Jaká kartuše je vhodná do zimy?', 'Zimní směsi s vyšším podílem propanu a isobutanu fungují lépe v chladu než čistý butan. Kartuši přes noc uchovejte v teple a před použitím ji ohřejte v rukou nebo kapse.'),
        ('Může se vařit uvnitř stanu?', 'Ne. Vařič v uzavřeném prostoru představuje riziko požáru i otravy oxidem uhelnatým. Vařte venku, v dostatečné vzdálenosti od látky stanu, na rovném a stabilním podkladu.'),
        ('Co je lepší, líh, nebo plyn?', 'Plyn je rychlejší a lépe regulovatelný, líh je lehčí, tišší a jednodušší. Pro víkend a rodinnou turistiku většinou vyhrává plyn, pro minimalisty a dlouhé túry bez náhrady vybavení někdy líh.'),
        ('Jak dlouho vydrží jedna kartuše?', 'Záleží na velikosti kartuše, počasí a množství vody. Doma si změřte spotřebu na litr vody a podle toho naplánujte zásobu. Vždy vezměte rezervu.'),
        ('Dají se kartuše vozit v letadle?', 'Obvykle ne. Dopravci i bezpečnostní předpisy jejich přepravu většinou zakazují. Informace si ověřte u konkrétního dopravce a kartuši koupíte až na místě.'),
        ('Co dělat s prázdnou kartuší?', 'Úplně prázdnou kartuši odevzdejte do sběru kovového odpadu podle místních pravidel. Nikdy ji neprorážejte ani nespalujte a nenechávejte částečně plnou v přírodě.'),
        ('Proč vařič špatně hoří ve větru?', 'Vítr odvádí teplo od hrnce a rozfukuje plamen. Pomůže větrná clona, hrnec s výměníkem tepla nebo vaření v závětří. Bez clony se spotřeba paliva zvyšuje.'),
        ('Je vhodné používat plynové topení ve stanu?', 'Ne. Plynová topidla ve stanu nepoužívejte, hrozí otrava oxidem uhelnatým i požár. Spalování uvnitř uzavřeného prostoru je nebezpečné i při větrání, proto topidlo ve stanu ani v přístřešku nezapínejte.'),
    ])

# ------------------------------------------------------------------ lovecke-vybaveni
NEW['lovecke-vybaveni'] = dict(long=True,
    title='Lovecké vybavení: optika, fotopasti, brašny, psi',
    desc='Lovecké vybavení bez zbraní: fotopasti, dalekohledy, batohy, pouzdra, nože, výcvik psů a doplňky Solognac a Jack Pyke. Srovnání obchodů.',
    intro='<p>Dobrý myslivec nebo lovec stráví v terénu hodiny v tichu a chladu, takže drobnosti rozhodují o pohodlí i bezpečnosti. Lovecké vybavení zahrnuje mnohem víc než zbraň: brašny na náboje, pouzdra, dalekohledy, fotopasti, nože, výbavu pro psa, ochranné brýle, nešustivé oblečení a pomůcky pro čekání na posedu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek '
          + B(('solognac', 'Solognac'), ('jack-pyke', 'Jack Pyke'), ('spypoint', 'Spypoint'), ('num-axes', "Num'axes"), ('steiner', 'Steiner'), ('mikov', 'Mikov'), ('bergans', 'Bergans'), ('mil-tec', 'Mil-Tec')) +
          '. Samotné zbraně a střelivo tu neřešíme, pouze příslušenství a výbavu. Pro kompletní sadu se hodí <a href="/lovecke-obleceni/">lovecké oblečení</a>, <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>, <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitooly</a> a <a href="/lov-a-priroda/">lov a příroda</a>.</p>',
    guide='<h2>Co všechno spadá do lovecké výbavy</h2>'
          '<p>Kategorie je pestrá, protože každý typ lovu, od posedu přes šoulání po naháňku, vyžaduje jinou výbavu. Hodí se rozdělit ji do několika skupin.</p>'
          + T(['Skupina', 'Příklady', 'K čemu slouží'], [
              ['Optika a pozorování', 'dalekohledy, fotopasti', 'sledování zvěře, přehled o revíru'],
              ['Nošení a přeprava', 'batohy, brašny, pouzdra', 'bezpečný převoz a organizace výbavy'],
              ['Ochrana a komfort', 'střelecké brýle, rukávníky, sedáky', 'ochrana při střelbě a dlouhém čekání'],
              ['Nože a nástroje', 'dýky, nože, multitooly', 'práce se zvěří a v terénu'],
              ['Pes a výcvik', 'obojky, píšťalky, vodítka', 'práce a výcvik loveckých psů'],
              ['Údržba a doplňky', 'oleje, hadříky, nádoby s dehtem', 'péče o výstroj, lákání zvěře']]) +
          '<p>Tato nabídka stojí na legálním příslušenství. Nákup a držení zbraní podléhá zákonu a požaduje příslušné oprávnění, proto se držte pravidel a obracejte se na oprávněné prodejce.</p>'
          '<h2>Fotopasti a pozorování revíru</h2>'
          '<p>Fotopast je kamera s čidlem pohybu, která zvěř zachytí bez rušení člověkem. Pomáhá poznat, kde se zvěř zdržuje, v jakou dobu a kolik kusů tam je. Při výběru sledujte rozlišení fotografií a videa, rychlost spouště, dosah detekce, noční režim a způsob napájení. Důležitá je i odolnost proti vlhkosti a možnost přenosu dat. Modely značky Spypoint nabízejí mobilní připojení, ale vyžadují datový tarif.</p>'
          '<p>Fotopast upevněte na pevný kmen ve výšce, která odpovídá zvěři, a nasměrujte ji mírně dolů. Odstraňte větve, které by se vlivem větru pohybovaly a spouštěly záznam. Při umísťování na cizí pozemek vždy dodržujte pravidla a respektujte soukromí osob.</p>'
          '<h2>Dalekohledy a optika</h2>'
          '<p>Dalekohled je jedna z nejdůležitějších věcí na posedu. Zvětšení a průměr přední čočky určují, jak daleko a za jakého světla uvidíte. Vyšší zvětšení zvětšuje i chvění ruky, takže se těžko drží. Pro lov za šera se hodí větší objektiv, ale rostou rozměry i hmotnost. Ověřte si odolnost proti vodě a mlžení a možnost nošení na popruhu nebo v postroji. Hledejte také v kategorii <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>.</p>'
          '<h2>Batohy, brašny a pouzdra</h2>'
          '<p>Lovecký batoh má být tichý, pohodlný a uspořádaný. Dobře fungují modely s integrovaným sedátkem nebo oporou, zejména při dlouhém čekání na posedu. Brašny na náboje, například značky Jack Pyke, ukládají střelivo a drobnosti tak, aby se nepřehrabovaly v tmavé kapse.</p>'
          '<p>Pouzdra na zbraně slouží k bezpečné přepravě. Vybírejte podle délky, tuhosti a vnitřního polstrování. Měkká pouzdra se lépe nosí, tvrdá více chrání. Přepravní povinnosti stanoví zákon a liší se podle situace, proto se řiďte aktuálními pravidly. Nosit sebou si můžete také <a href="/turisticke-batohy/">turistický batoh</a>, pokud vám nevyhovuje specializovaná varianta.</p>'
          '<h2>Oblečení, které se hodí na posed</h2>'
          '<p>Nešustivá tkanina je základ. Vlna a speciální měkké materiály tlumí zvuk a zahřejí i za mrazu, ale na mokrý den se hodí membrána. Důležité jsou i barvy, které splynou s prostředím. Solognac a Jack Pyke patří mezi značky, které nabízejí kabáty, vesty a doplňky určené pro lov. Pro větší výběr si prohlédněte <a href="/lovecke-obleceni/">lovecké oblečení a obuv</a>, <a href="/zimni-bundy/">zimní bundy</a> a <a href="/termopradlo/">termoprádlo</a>.</p>'
          '<p>K dlouhému čekání se hodí rukávníky a hřejivé doplňky, které udrží ruce v teple bez omezení pohybu. Na zimu sáhněte po vrstvách a <a href="/sportovni-ponozky/">teplých ponožkách</a>.</p>'
          '<h2>Ochrana zraku a sluchu</h2>'
          '<p>Střelecké brýle chrání před úlomky a částicemi, proto je používejte při střelbě i při práci se zbraní. Sady s výměnnými skly se přizpůsobí světlu, od jasného slunce po šero. Ochrana sluchu je také nezbytná, protože střelba může sluch trvale poškodit.</p>'
          '<h2>Nože a nástroje</h2>'
          '<p>Lovecký nůž musí být ostrý a spolehlivý, s pevným držadlem, které se nesmekne ani při mokrých rukou. Pevné nože jsou jednodušší, skládací se hodí do kapsy. Nože značky Mikov patří mezi tradiční české výrobky. Při nošení a přepravě dodržujte místní předpisy. Další varianty najdete v kategorii <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitooly</a>.</p>'
          '<h2>Pes při lovu</h2>'
          '<p>Lovecký pes vyžaduje vyvážený výcvik a správnou výbavu. Mezi základní věci patří píšťalka, stopovací vodítko, reflexní vesta nebo obojek a pomůcky pro výcvik. Výcvik musí psovi působit co nejméně stresu a nesmí mu způsobovat bolest, proto volte šetrné metody založené na odměně. Elektrošokové obojky zákon na ochranu zvířat proti týrání v České republice zakazuje, proto je nepoužívejte. Pokud si nejste jistí, zeptejte se kynologa.</p>'
          '<h2>Další příslušenství</h2>'
          '<p>K lovu patří i položky, které nejsou na první pohled vidět: bezpečnostní skříň na zbraně (zbraně musí být uloženy podle platných předpisů), bipod pro stabilní oporu, vlek nebo nosič na zvěřinu, vábničky a granule či krmivo pro lovecké psy. Při výběru sledujte nosnost, materiál a odolnost proti vlhku a vždy si ověřte, zda se pro daný účel nevyžaduje povolení nebo osvědčení.</p>'
          '<h2>Výběr podle typu lovu</h2>'
          '<ul><li><strong>Posed a čekaná:</strong> teplé oblečení, sedák, dalekohled a tichý batoh.</li>'
          '<li><strong>Šoulání a pochůzky:</strong> lehké, nešustivé oblečení a pevná <a href="/trekova-obuv/">treková obuv</a>.</li>'
          '<li><strong>Společné lovy:</strong> výstražné prvky, pouzdro na zbraň, vesta a výbava pro psa.</li>'
          '<li><strong>Pozorování revíru:</strong> fotopasti, dalekohled a kompas z kategorie <a href="/dalekohledy-a-kompasy/">dalekohledy a kompasy</a>.</li>'
          '<li><strong>Dlouhý pobyt v přírodě:</strong> doplňte <a href="/celovky-a-svitilny/">čelovky</a> a <a href="/prvni-pomoc/">lékárničku</a>.</li></ul>'
          '<h2>Údržba a péče o výstroj</h2>'
          '<p>Po každém použití výbavu vysušte a očistěte. Oblečení s membránou perte podle štítku, aby nepřišlo o funkci. Kožené a textilní pouzdra větrejte a skladujte mimo vlhko, protože vlhkost zbraním škodí. Olejničky a hadříky na údržbu patří do sady každého střelce. Dbejte, aby oleje nepřišly do kontaktu s oblečením, které potom zapáchá a při dalším použití zvěř odpuzuje.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš hlučné oblečení a batoh, které při pohybu šustí.</li>'
          '<li>Nedostatek teplých vrstev při dlouhém čekání.</li>'
          '<li>Nevhodná ochrana očí a sluchu, nebo žádná.</li>'
          '<li>Špatné umístění fotopasti, kterou při větru spouštějí větve.</li>'
          '<li>Použití výcvikového obojku bez zkušeností.</li></ul>'
          '<h2>Příslušenství pro vyšší pohodlí na čekané</h2>'
          '<p>Dlouhé hodiny bez pohybu jsou hlavně o teple a pohodlí. Sedák nebo skládací stolička s opěrkou zabrání prochladnutí zad, rukávník s kapsami zahřeje ruce a termoska s teplým nápojem pomůže udržet pozornost. Další pomůcky najdete v kategoriích <a href="/lahve-a-termosky/">láhve a termosky</a> a <a href="/bivaky-a-kresla/">bivaky a křesla</a>. Přidejte tichou svítilnu s červeným světlem, která zvěř neplaší, a čelovku z kategorie <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</p>'
          '<ul><li><strong>Sedák a stolička:</strong> izoluje od studené země a odlehčí zádům.</li>'
          '<li><strong>Rukavice s citlivým prstem:</strong> umožní pohyb bez sundání celé rukavice.</li>'
          '<li><strong>Pláštěnka nebo ochrana proti dešti:</strong> měla by být tichá a lehká. Další typy najdete mezi <a href="/nepromokave-bundy/">nepromokavými bundami</a>.</li>'
          '<li><strong>Maskovací prvky:</strong> sítě, čepice a nákrčníky, které rozbijí obrys postavy.</li></ul>'
          '<h2>Orientace a bezpečnost v revíru</h2>'
          '<p>Kompas a mapa jsou nezbytné i v dobře známém lese, protože v mlze a ve tmě se snadno ztratíte. Mobil je užitečný, ale baterie v mrazu rychle slábne, proto vezměte i powerbanku z kategorie <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a>. Základem bezpečnosti je také lékárnička, signální píšťalka a vždy informovaný kolega o místě pobytu.</p>'
          '<p>Při společných honech se dodržují pravidla pro výstražné prvky a bezpečné směry střelby. Tyto věci řeší organizátor, ale vy si zajistěte viditelnou vestu nebo čepici a vybavení pro psa. Používejte také vždy bezpečné způsoby přepravy a nikdy nenechávejte vybavení bez dozoru.</p>'
          '<h2>Přírodní prostředí a ohleduplnost</h2>'
          '<p>Lov a pobyt v přírodě znamená odpovědnost k zvěři i k ostatním lidem. Odpadky odneste, ohně rozdělávejte jen tam, kde je to dovoleno, a respektujte pravidla honitby. Dobře ošetřená výbava vydrží několik sezón a snižuje množství odpadu. Pokud kupujete vybavení pro menší část sezóny, vyberte univerzální kusy, které využijete i na túrách nebo fotografování zvířat.</p>'
          '<h2>Výbava pro úplné začátečníky</h2>'
          '<p>Pokud s myslivostí teprve začínáte, nekupujte všechno najednou. Pořiďte nejprve to, co odpovídá vašim zkušenostem a revíru: spolehlivou obuv, tiché oblečení, dalekohled a základní pouzdro či brašnu. Fotopast, výcvikové pomůcky a speciální doplňky přidávejte postupně, až poznáte, co skutečně využijete. Poraďte se s členy místního sdružení, protože zkušení lidé vědí, co se v daném terénu osvědčilo. Sporteka vám pomůže najít nabídky českých obchodů a porovnat varianty podle dostupnosti.</p>'
          '<p>Při výběru kvalitní výstroje nemusíte kupovat nejdražší kusy. Důležité je, aby výbava seděla, nerušila a vydržela náročné počasí. Raději volte menší počet osvědčených věcí než plný batoh nevyzkoušených novinek.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka srovnává nabídky několika obchodů, takže vidíte, kdo má produkt skladem a za jakých podmínek ho doručí. Zbraně a střelivo zde nehledejte. Kategorie sdružuje příslušenství a výbavu, u každého produktu si ověřte popis, rozměry a materiál.</p>',
    faq=[
        ('Prodává Sporteka zbraně a střelivo?', 'Ne. Kategorie obsahuje příslušenství, oblečení a vybavení. Zbraně a střelivo podléhají zákonu a nákup vyžaduje příslušná oprávnění, takže se obracejte na oprávněné prodejce.'),
        ('Jak vybrat fotopast?', 'Sledujte rozlišení, rychlost spouště, dosah čidla, noční režim a napájení. Pokud chcete data přímo v mobilu, hledejte model s připojením, ale počítejte s datovým tarifem.'),
        ('Jaký dalekohled je vhodný na posed?', 'Záleží na světle a vzdálenosti. Větší průměr objektivu pomáhá za šera, vyšší zvětšení hůře drží v ruce. Dobrý kompromis je střední zvětšení s větší čočkou a odolností proti vlhkosti.'),
        ('Proč je důležité nešustivé oblečení?', 'Zvěř reaguje na zvuk a šustění látky prozradí váš pohyb. Vlna a měkké tkaniny hluk tlumí a při chladném čekání i lépe hřejí.'),
        ('Jaké pouzdro zvolit na převoz zbraně?', 'Vyberte podle délky a polstrování. Měkké pouzdro je lehčí, tvrdé nabízí větší ochranu. Přepravní pravidla stanoví zákon, proto se vždy informujte u příslušného úřadu nebo prodejce.'),
        ('K čemu slouží stopovací vodítko?', 'Je dlouhé, pevné a umožňuje psovi pracovat na stopě. Hodí se při dohledávce zvěře. Správné použití a výcvik s vodítkem si osvojte u zkušeného kynologa.'),
        ('Je bezpečné používat elektronický výcvikový obojek?', 'Jen s dobrou znalostí a ve správném nastavení. Nevhodné použití může psovi škodit, proto raději nejdřív konzultujte zkušeného výcvikáře a řiďte se návodem.'),
        ('Jak pečovat o lovecké oblečení?', 'Čistěte ho podle štítku, nepoužívejte aviváž u membrán a sušte mimo přímé teplo. Skladujte větrané a suché, aby nezplesnivělo.'),
        ('Proč mi na fotopasti nahrává prázdné záběry?', 'Nejčastěji ji spouštějí větve nebo tráva v dosahu čidla. Upravte okolí, snižte citlivost a změňte sklon kamery.'),
        ('Potřebuji střelecké brýle?', 'Ano, při střelbě chrání oči před úlomky a částicemi. Vyberte sadu s výměnnými skly a ověřte, že dobře sedí a nezamlžují se.'),
        ('Jak dlouho vydrží baterie ve fotopasti?', 'Záleží na počtu spuštění, teplotě a typu baterií. V mrazu kapacita klesá, proto vložte kvalitní baterie vhodné do nízkých teplot a sledujte jejich stav při každé kontrole revíru. Řada fotopastí umí také externí napájení.'),
        ('Čím začít, když s lovem začínám?', 'Pořiďte spolehlivou obuv, tiché teplé oblečení, dalekohled a základní pouzdro nebo brašnu. Další pomůcky přidávejte postupně podle revíru a rad zkušených členů sdružení.'),
    ])

# ------------------------------------------------------------------ brusle
NEW['brusle'] = dict(long=True,
    title='Zimní brusle: rekreační, krasobruslařské, hokejové',
    desc='Zimní brusle na led: rekreační, krasobruslařské i hokejové pro děti a dospělé. Velikost, tuhost, nože a péče. Porovnejte nabídky obchodů.',
    intro='<p>Dobře sedící brusle rozhodují o tom, jestli si zimu na ledě užijete, nebo skončíte po půl hodině s obtlačenými kotníky. Zimní brusle zahrnují rekreační modely na veřejné kluziště, krasobruslařské s vyšší patou a zoubky, hokejové brusle a dětské kluzáky s nastavitelnou velikostí. Každá skupina má jinou stavbu boty, nůž i tuhost.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek '
          + B(('tempish', 'Tempish'), ('fila', 'Fila'), ('winnwell', 'Winnwell'), ('bauer', 'Bauer'), ('sulov', 'Sulov'), ('roces', 'Roces'), ('arcore', 'Arcore'), ('k2', 'K2'), ('riedell', 'Riedell')) +
          '. Pomocí podkategorií <a href="/rekreacni-brusle/">rekreační brusle na led</a> a <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a> zúžíte výběr a v sekci <a href="/hokejove-brusle/">hokejové brusle</a> najdete další modely. Dále se vám hodí <a href="/zimni-sporty/">zimní sporty</a>, <a href="/hokej/">hokej</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>',
    guide='<h2>Druhy zimních bruslí</h2>'
          '<p>Hlavní rozdíl je v účelu: některé brusle se hodí na hru a hokej, jiné na kroužky a pomalou jízdu po kluzišti. Při výběru se nejdříve rozhodněte, k čemu je budete používat.</p>'
          + T(['Typ', 'Charakteristika', 'Pro koho'], [
              ['Rekreační brusle', 'měkčí bota, často s nastavitelnou velikostí', 'veřejná kluziště a rybníky'],
              ['Krasobruslařské brusle', 'vyšší pata, zoubky na noži, pevný kotník', 'pohyb po ledě, piruety, kroužky a tréninky'],
              ['Hokejové brusle', 'tuhá bota, kratší zahnutý nůž, ochrana nártu', 'hokej, zápasy, rychlá jízda'],
              ['Dětské kluzáky', 'nastavitelná velikost, dvojitý nůž nebo upevnění', 'malé děti, první pokusy'],
              ['Půjčovní a dětské modely', 'odolná bota, snadné zavazování', 'rodiny, kurzy']]) +
          '<p>Hokejové modely, například značek Bauer nebo Winnwell, jsou stavěné na prudké změny směru a ochranu chodidla před puky. Na pomalé bruslení po kluzišti jsou zbytečně tuhé, rekreační brusle naopak nepodrží kotník při hře.</p>'
          '<h2>Rekreační brusle na led</h2>'
          '<p>Rekreační brusle jsou nejčastější volbou. Bota bývá z měkčího syntetického materiálu s vložkou, která zahřeje chodidlo. Šněrování nebo kombinace přezek a šněrování drží nohu bezpečně. Značky jako Tempish, Fila, Roces nebo Arcore nabízejí pánské, dámské i dětské modely, často s nastavitelnou velikostí.</p>'
          '<p>Pro nepravidelné bruslení stačí jednodušší model, ale vždy hledejte pevnou podporu kotníku. Příliš měkká bota se prohýbá a unaví nohy. Praktická je také možnost vyjmout vložku a bota rychle uschne po použití.</p>'
          '<h2>Krasobruslařské brusle</h2>'
          '<p>Krasobruslařské brusle mají vyšší patu, pevnější kotník a nůž se zoubky na přední části, které slouží k odrazům a skokům. Pro začátečníky existují lehčí modely z umělé kůže, pro pokročilé tužší bota z kůže nebo kompozitu. Pozor, tuhá bota nevyhovuje každému a špatně volená tuhost zpomalí pokrok.</p>'
          '<p>Věnujte pozornost nožům. Některé modely jsou prodávány s nožem, jiné bez něj a nůž se kupuje zvlášť. Značka Riedell je známá specializovanými modely. Při koupi se ptejte, co je v ceně a zda je nůž přišroubovaný.</p>'
          '<h2>Hokejové brusle v kategorii</h2>'
          '<p>V nabídce najdete také řady jako Vapor či Supreme od Baueru v juniorských, intermediate a senior velikostech. Označení FIT 1 nebo EE se vztahuje k šířce a tvaru boty. Hokejové brusle zvolte podle šířky chodidla a podle úrovně hry. Rozdíl mezi levnějšími a dražšími modely spočívá v materiálu, tuhosti a tepelné tvarovatelnosti. Další výběr najdete v kategorii <a href="/hokejove-brusle/">hokejové brusle</a>, navazuje <a href="/hokejove-chranice/">hokejová chránice</a> a <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Velikost je nejčastější zdroj problémů. Brusle sedí jinak než boty, protože noha musí být fixovaná. Prsty se mají lehce dotýkat špičky a pata nesmí zvedat. V příliš velkých bruslích se noha pohybuje a vznikají puchýře. U dětí se nesmí kupovat „na dorost“ s velkou rezervou. Pokud chcete výběr usnadnit, použijte modely s nastavitelnou velikostí.</p>'
          + T(['Zkouška', 'Co sledovat', 'Chyba'], [
              ['Zasunutí nohy', 'pata dosedne do zadní části', 'volný prostor za patou'],
              ['Zašněrování', 'pevné, bez tlaku na nárt', 'příliš utažené nebo uvolněné'],
              ['Postoj', 'kotník stabilní, prsty bez tlaku', 'prsty ohnuté nebo kotník vybočuje'],
              ['Krok a stání', 'noha se nepohybuje', 'pata zvedá nebo bota tlačí']]) +
          '<p>Při koupi používejte tenké sportovní ponožky. Silné zimní ponožky zmenšují prostor a snižují cit pro kontakt s ledem. Vhodné tenké modely najdete mezi <a href="/sportovni-ponozky/">sportovními ponožkami</a>.</p>'
          '<h2>Tuhost boty a podpora kotníku</h2>'
          '<p>Tuhá bota poskytuje oporu a přenos síly, ale začátečníkům může být nepohodlná. Příliš měkká bota se při zatížení prohýbá a kotníky zbytečně pracují. Rekreační jezdec má volit střední tuhost, hokejista a pokročilý bruslař vyšší. Zkuste si v bruslích stoupnout, mírně pokrčit kolena a ověřit, že kotník nevybočuje dovnitř.</p>'
          '<h2>Nože, ostření a ochrana</h2>'
          '<p>Nůž brusle určuje kluz a ovladatelnost. Tupý nůž klouže špatně, ostrý lépe drží hranu. Naostřit je třeba po několika bruslích nebo když ztrácí záběr, ale vždy ve specializovaném servisu, který dodržuje správný profil. Na ledě se nepoužívají chrániče, mimo led je nasaďte, aby se nůž nepoškodil o beton a kameny. Praktické jsou chrániče, jako je Rollergard, a náhradní gumy.</p>'
          '<h2>Děti a první brusle</h2>'
          '<p>Malé děti často začínají s nastavitelnými kluzáky nebo dvojitými noži, které se připevní na boty. Postupně přecházejí na klasické brusle s pevnou botou. Dětské modely mají měkké zapínání a vyšší stabilitu. Vždy věnujte pozornost helmě a chráničům, protože pády jsou běžné. K tomu se hodí <a href="/chranice-a-helmy/">chrániče a helmy</a> a rukavice z kategorie <a href="/sportovni-rukavice/">sportovní rukavice</a>.</p>'
          '<p>U dětských bruslí je důležité, aby šly dobře obout a zašněrovat. Špatně padnoucí brusle, které se obtížně obouvají, děti od bruslení často odradí.</p>'
          '<h2>Výběr podle účelu</h2>'
          '<ul><li><strong>Veřejné kluziště a rybník:</strong> rekreační brusle s měkčí vložkou. Přidejte <a href="/zimni-obuv/">zimní obuv</a> na cestu na led.</li>'
          '<li><strong>Kurzy krasobruslení:</strong> krasobruslařské brusle a doplňky, jako jsou <a href="/leginy/">legíny</a> a <a href="/sportovni-rukavice/">rukavice</a>.</li>'
          '<li><strong>Hokej a florbal na ledě:</strong> hokejové brusle, <a href="/hokejky/">hokejky</a> a chránice.</li>'
          '<li><strong>Rodinné bruslení:</strong> nastavitelné brusle, helma a teplé vrstvy. Další oblečení najdete v <a href="/zimni-bundy/">zimních bundách</a>.</li>'
          '<li><strong>Celoroční trénink:</strong> v létě navazují <a href="/inline-brusle/">inline brusle</a> a <a href="/kolobezky-a-brusle/">kolečkové brusle</a>.</li></ul>'
          '<h2>Péče o brusle</h2>'
          '<p>Po bruslení nože osušte měkkým hadříkem, aby nezrezivěly. Brusle nenechávejte v chráničích, ve kterých se drží vlhkost. Vyjměte vložky a nechte boty uschnout při pokojové teplotě, mimo topení. Boty skladujte v suchu a nože zatím chraňte látkovými návleky. Pokud na noži najdete rez, nechte ji odstranit odborníkem.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš velké brusle pro děti, které se v nich špatně drží.</li>'
          '<li>Hrubé zimní ponožky, které nohu sevřou a zhorší cit.</li>'
          '<li>Chůze po betonu v nožích bez chráničů.</li>'
          '<li>Zanedbaná údržba a ostření.</li>'
          '<li>Volba hokejových bruslí pro pomalou rekreační jízdu a naopak.</li></ul>'
          '<h2>Jak vypadá správné obutí a zašněrování</h2>'
          '<p>Zašněrování rozhoduje o komfortu stejně jako velikost. Začněte u špičky mírně volněji, aby se prsty mohly pohybovat, nad nártem utáhněte pevněji a v oblasti kotníku opět tak, aby se pata nezvedala. Jazyk boty by měl ležet rovně a nesmí tlačit. Při bruslení se šněrování časem uvolní, proto ho po prvním kole zkontrolujte. U modelů se západkami a přezkami ověřte, zda drží, a při zapínání se nepřetahujte, aby se nepřiškrtila krev v noze.</p>'
          '<ol><li>Vložte nohu až na doraz, aby pata přiléhala k zadní části boty.</li>'
          '<li>Poklepejte patou o zem, aby se noha posadila.</li>'
          '<li>Zašněrujte od špičky k nártu a rovnoměrně utáhněte.</li>'
          '<li>Zkontrolujte kotník: noha má držet, ale krev nesmí škrtit.</li>'
          '<li>Po několika minutách na ledě šněrování dotáhněte.</li></ol>'
          '<h2>Technika a první kroky na ledě</h2>'
          '<p>Základem je postoj s mírně pokrčenými koleny a váhou nad středem chodidla. Při prvních krocích se držte mantinelu, pohybujte se malými kroky a dívejte se před sebe, ne na špičky. Padat se učte tak, že se skrčíte a dopadnete na bok nebo na kolena, ruce stáhnete do pěstí, aby vám je nepřejely nože, a chráníte hlavu. Ruce nikdy nedržte v kapsách, hodí se rukavice, které chrání před odřením.</p>'
          '<p>Brzdění pluhem nebo otočením boty se učí hned na začátku. Děti se rychle učí na kurzech, dospělí potřebují více trpělivosti. Dobrý začátek s kvalitní obuví a vhodnou velikostí ušetří spoustu frustrace a rozhoduje o tom, zda bruslení zůstane koníčkem.</p>'
          '<h2>Oblečení na led</h2>'
          '<p>Na ledě je chladnější než se zdá, ale při pohybu se zahřejete. Oblékejte se do vrstev: funkční spodní vrstva, fleecová nebo softshellová střední a lehká bunda. Z kategorie <a href="/funkcni-mikiny/">funkční mikiny</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/cepice-a-celenky/">čepice a čelenky</a> si složíte teplou sestavu bez zbytečné váhy. Rukavice zamezí odřeninám při pádu a ruce zahřejí.</p>'
          '<h2>Údržba bruslí během sezóny</h2>'
          '<p>Při pravidelném bruslení si zvyknete na jednoduchý rituál: po každé jízdě osušit nože, vyjmout vložky, nechat boty vyvětrat a před dalším použitím zkontrolovat šněrovadla. Prasklé tkaničky měňte hned, protože při bruslení se prudce namáhají. Pokud se bota viditelně deformuje nebo se kotník začne propadat, je čas na novou. Děti vyrůstají rychle, proto je rozumné brusle po sezóně zkusit a případně předat mladšímu sourozenci nebo bazaru.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého páru porovnáte nabídky několika obchodů a uvidíte, které velikosti jsou skladem. Před objednávkou si změřte délku chodidla a porovnejte ji s tabulkou výrobce. Pokud váháte mezi dvěma velikostmi, raději si ověřte možnost výměny. Filtrujte podle značky a pohlaví a použijte podkategorie.</p>',
    faq=[
        ('Jaké brusle vybrat na veřejné kluziště?', 'Nejlépe rekreační brusle se střední tuhostí a pevným šněrováním. Mají měkčí vložku a podrží kotník. Hokejové a krasobruslařské modely jsou pro tento účel zbytečně specializované.'),
        ('Jak poznám správnou velikost brusle?', 'Prsty se mají lehce dotýkat špičky, pata musí sedět v zadní části a noha se nesmí pohybovat. Porovnejte délku chodidla s tabulkou výrobce a zkoušejte s tenkými ponožkami.'),
        ('Mohou mít děti brusle na dorost?', 'Příliš velké brusle nejsou bezpečné, noha v nich neudrží stabilitu. Lepší volbou jsou nastavitelné modely, které se přizpůsobí růstu o několik čísel.'),
        ('Jaký je rozdíl mezi hokejovými a rekreačními bruslemi?', 'Hokejové mají tužší botu, kratší zahnutý nůž a ochranu nártu, vhodné jsou pro rychlou hru. Rekreační jsou měkčí a pohodlnější na pomalé bruslení.'),
        ('Proč mají krasobruslařské brusle zoubky?', 'Zoubky na přední části nože slouží k odrazům a skokům. Pro základní bruslení nejsou nutné, ale v krasobruslení jsou důležitou součástí techniky.'),
        ('Jak často brusle brousit?', 'Když nůž ztrácí záběr nebo kluz, nejpozději po několika bruslích. Broušení nechte provést v servisu, který dodrží správný profil nože.'),
        ('Mám brusle uschovávat v chráničích?', 'Ne, vlhkost v nich zůstane a nůž může rezivět. Chrániče používejte při chůzi mimo led a pro uložení použijte savý návlek nebo hadřík.'),
        ('Jaké ponožky na brusle?', 'Tenké, funkční a bez švů. Silné zimní ponožky zmenšují prostor v botě a snižují cit pro kontakt s ledem.'),
        ('Dají se brusle použít na venkovním ledě?', 'Ano, ale led na rybníku nebo řece nemusí být bezpečný. Pohybujte se pouze na ověřených a kontrolovaných plochách a nikdy nechoďte na led sami.'),
        ('Potřebuji helmu při rekreačním bruslení?', 'Pro děti a začátečníky je helma velmi vhodná, protože pády na tvrdý led jsou časté. Doplňte ji chrániči loktů, kolen a zápěstí.'),
        ('Jak poznám, že je čas na novou obuv?', 'Když se bota deformuje, kotník se propadá dovnitř nebo noha v botě hýbe, ztratila oporu. U dětí je čas také ve chvíli, kdy palce tlačí na špičku, i když šněrování vypadá v pořádku.'),
        ('Mohu si brusle půjčit, než koupím vlastní?', 'Ano, většina kluzišť půjčuje. Půjčovní kusy jsou ale často opotřebené, takže pro pravidelné bruslení se vlastní pár vyplatí. Půjčení se hodí k vyzkoušení, jakou tuhost a velikost zvolit.'),
    ])
