"""Guides wave 5b (2026-11-19): cviceni-s-posilovaci-gumou, co-je-pilates, kettlebell-cviky, rozcvicka-pred-behem.

Demand (CZ / month): cvičení s posilovací gumou 600, co je pilates 400, kettlebell cviky 250, rozcvička před během 150.

Sources used for the facts:
- Bands: TheraBand / Performance Health catalogue and colour charts (order from lightest: tan, yellow, red, green,
  blue, black, silver, gold; each step yellow-black about 25 % more resistance at 100 % stretch; other brands use
  their own colours); local catalogue copy (HMS GU06 loop bands 2250 mm long, widths 13-29 mm; power band and mini
  band sets from Revity, 4FIZJO, Sveltus, Merco with kg ranges stated by the seller).
- Pilates: Britannica "Pilates" / "Joseph Pilates" (born 9 Dec 1883 Mönchengladbach, to England 1912, interned as an
  enemy alien in WWI in camps in Lancaster and on the Isle of Man, New York 1926, died 9 Oct 1967 New York); Pilates
  Method Alliance "The History of Pilates" (studio with Clara in New York, method called Contrology, Return to Life
  Through Contrology 1945); several sources on the six principles (concentration, control, centre, flow, precision,
  breathing) being codified by Friedman & Eisen, The Pilates Method of Physical and Mental Conditioning (1980), not
  by Joseph Pilates himself.
- Kettlebells: StrongFirst sizing note (16 kg and 24 kg for an average man), Kettlebell Kings "What is a pood"
  (1 pood ≈ 16 kg), several trainer guides (8 kg common start for women, 12-16 kg for men; heavier bell for swing
  than for press); technique standards for swing (hip hinge, hips drive the bell), clean to rack, press, goblet squat
  and Turkish get-up as taught by StrongFirst/RKC style courses.
- Warm-up: Simic, Sarabon, Markovic 2013, Scand J Med Sci Sports, meta-analysis of 104 studies: pre-exercise static
  stretching reduced strength by 5.4 %, power 1.9 %, explosive performance 2.0 %, smallest effects for stretches
  of 45 s or less, static stretching as the only warm-up activity should be avoided; Lauersen, Bertelsen, Andersen
  2014, BJSM 48:871-877, meta-analysis of 25 RCTs: stretching showed no protective effect on sports injuries
  (RR 0.963), strength training reduced injuries to less than a third.
Left out because not verified: Joseph Pilates' cause of death, exact kg values behind band colours of particular
brands (only TheraBand order is given), an official StrongFirst weight for women, any study showing a dynamic
warm-up prevents running injuries, numbers for calories burned, any claim that pilates treats back pain.
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- cviceni-s-posilovaci-gumou
BAND_TYPES = T(['Typ gumy', 'Jak vypadá', 'Na co se hodí'], [
    ['Dlouhá smyčka (loop, power band)', 'Uzavřený pruh latexu, často kolem 2 m dlouhý, šíře udává sílu', 'Přítahy, tlaky, mrtvý tah, dopomoc na hrazdě, protahování'],
    ['Mini band', 'Krátká smyčka kolem 30 cm, latexová nebo textilní', 'Hýždě a kyčle: chůze do stran, mosty, unožování'],
    ['Textilní hip band', 'Krátká smyčka z látky s gumou, nesroluje se', 'Stejné cviky jako mini band, pohodlnější na holou kůži'],
    ['Expandér s úchyty (tube)', 'Hadice s madly, někdy s karabinami a kotvou do dveří', 'Cviky jako na kladce: tlak na prsa, přítahy, biceps, triceps'],
    ['Plochý pás (terapeutický)', 'Tenký plochý pruh bez smyčky, prodává se v metráži nebo na kusy', 'Lehké cviky na ramena, zahřátí, cvičení vsedě'],
])

BAND_PLAN = T(['Den', 'Cviky', 'Série × opakování'], [
    ['A (horní polovina)', 'Přítah ve stoje, tlak nad hlavu, rozpínání před tělem, biceps, triceps', '3 × 12–15'],
    ['B (dolní polovina)', 'Dřep s gumou, rumunský mrtvý tah, most s mini bandem, chůze do stran', '3 × 12–15 (chůze 3 × 10 kroků na stranu)'],
    ['C (celé tělo)', 'Kliky s gumou, přítah vsedě, výpady, Pallofův tlak, mrtvý brouk', '2–3 × 10–12'],
])

GUIDES['cviceni-s-posilovaci-gumou'] = dict(
    name='Cvičení s posilovací gumou',
    h1='Cvičení s posilovací gumou: cviky na celé tělo a jednoduchý plán',
    seo_title='Cvičení s posilovací gumou: 14 cviků na celé tělo a plán',
    seo_desc='Jak cvičit s posilovací gumou: typy gum (loop, mini band, expandér), co znamenají barvy, 14 cviků na celé tělo s popisem techniky a třídenní plán.',
    intro_html=(
        '<p><strong>Jak cvičit s posilovací gumou?</strong> Vyberte si gumu, se kterou zvládnete 12 až 15 pomalých opakování, a posledních pár musí být těžkých. '
        'Gumu ukotvěte pod chodidly, za pevný sloup nebo do dveří, držte napětí po celou dobu pohybu a vracejte se pomalu. '
        'Na celé tělo stačí šest až osm cviků: dřep, mrtvý tah, most, přítah, tlak, kliky a jeden cvik na střed těla. Cvičte dvakrát až třikrát týdně a gumu měňte za silnější, když opakování přestanou být náročná.</p>'
        '<p>V článku vysvětlíme rozdíl mezi dlouhou smyčkou, mini bandem a expandérem, co znamenají barvy, proč se síla gumy v kilogramech nedá porovnat mezi značkami, '
        'a popíšeme 14 cviků s nejčastějšími chybami. Na konci najdete třídenní plán a péči o gumu, aby nepraskla. '
        'Pokud chcete doma víc vybavení, podívejte se i na průvodce <a href="/domaci-posilovna/">domácí posilovnou</a>.</p>'),
    sections=[
        dict(h2='Typy posilovacích gum a k čemu který slouží',
             html=(
                 '<p>Pod názvem posilovací nebo odporová guma se prodává několik dost odlišných pomůcek. Liší se tvarem, délkou a tím, jak se upínají. '
                 'Pro cvičení celého těla je nejuniverzálnější dlouhá smyčka, které se říká loop nebo power band. Mini band je naopak specialista na hýždě a kyčle.</p>'
                 + BAND_TYPES +
                 '<p>Dlouhé smyčky se dají spojovat a zdvojovat, takže s dvěma nebo třemi kusy pokryjete většinu cviků. Expandér s madly je příjemnější do ruky a s kotvou do dveří připomíná kladku v posilovně. '
                 'Mini band se nasazuje nad kolena nebo ke kotníkům a hodí se jako doplněk, ne jako jediná guma. Na plochý terapeutický pás se často cvičí ve fyzioterapii, kde ho vybírá a dávkuje terapeut.</p>'),
             cat='posilovaci-gumy', n=4),
        dict(h2='Barvy a síla gumy: proč nejde srovnávat napříč značkami',
             html=(
                 '<p>Barva gumy označuje její tuhost, ale <strong>každá značka má vlastní stupnici</strong>. Zelená guma jednoho výrobce může být lehčí než červená od jiného. '
                 'Nejznámější je stupnice TheraBand, kde od nejlehčí jdou barvy béžová, žlutá, červená, zelená, modrá, černá, stříbrná a zlatá. Ostatní výrobci ji často nepřebírají.</p>'
                 '<p>U dlouhých smyček se síla obvykle udává v kilogramech jako rozsah, třeba 16–39 kg. Číslo popisuje tah při určitém protažení, jak ho změřil výrobce, a různé obchody měří různě. '
                 'Mnohem spolehlivějším vodítkem je šířka pásu a tloušťka latexu. U jedné řady například platí, že guma široká 13 mm je lehká a 29 mm už výrazně tužší.</p>'
                 '<ul><li><strong>Začátečník:</strong> sada tří až pěti gum stejné značky, abyste měli návaznou stupnici.</li>'
                 '<li><strong>Dolní polovina těla:</strong> nohy a hýždě snesou tužší gumu než ramena a paže.</li>'
                 '<li><strong>Dopomoc na hrazdě:</strong> čím těžší jste, tím tužší guma, nejčastěji ze středu nabídky.</li></ul>'
                 '<p>Při srovnávání nabídek proto koukejte na rozměry (délka × šířka × tloušťka) a materiál, ne jen na barvu. Pro citlivou pokožku nebo alergii na latex hledejte textilní či TPE varianty.</p>')),
        dict(h2='Jak gumu bezpečně ukotvit a správně cvičit',
             html=(
                 '<ol><li><strong>Zkontrolujte gumu</strong> před každým tréninkem. Natržení, bílé praskliny nebo lepkavý povrch znamenají vyřazení.</li>'
                 '<li><strong>Kotvěte pevně.</strong> Pod oběma chodidly, kolem sloupku zábradlí, žebřin nebo pomocí kotvy do dveří na straně pantů. Nikdy ne za kliku ani nábytek, který se může posunout.</li>'
                 '<li><strong>Začněte s napětím.</strong> Guma má být lehce napnutá už ve výchozí poloze, jinak první část pohybu nic nedělá.</li>'
                 '<li><strong>Vracejte se pomalu.</strong> Návrat přes dvě až tři vteřiny je polovina práce. Když gumu pustíte, cvik ztratí smysl a guma může švihnout.</li>'
                 '<li><strong>Držte ji od obličeje.</strong> Při tlacích a přítazích nemiřte gumou k očím a pracujte v suchých dlaních.</li></ol>'
                 '<p>Odpor gumy roste s protažením, takže cvik je nejtěžší na konci pohybu. To je opak činky, kde je těžší spíš začátek. Proto se gumy dobře doplňují s volnými váhami a hodí se i k rozcvičení před posilovnou.</p>')),
        dict(h2='Cviky na nohy a hýždě',
             html=(
                 '<p><strong>1. Dřep s gumou.</strong> Postavte se na dlouhou smyčku na šířku ramen, druhý konec přetáhněte přes ramena za krk nebo držte v rukou u ramen. '
                 'Dřepněte tak hluboko, jak udržíte rovná záda a paty na zemi, a vstaňte. Kolena jdou ve směru špiček.</p>'
                 '<p><strong>2. Rumunský mrtvý tah.</strong> Stůjte na gumě, konce držte v rukou podél stehen. S mírně pokrčenými koleny posílejte zadek dozadu, trup se sklápí s rovnými zády. '
                 'Zastavte, když ucítíte tah v zadní straně stehen, a vraťte se vytlačením pánve dopředu.</p>'
                 '<p><strong>3. Hýžďový most s mini bandem.</strong> Lehněte na záda, mini band nad kolena, chodidla na zemi. Zvedněte pánev, kolena tlačte mírně od sebe proti gumě a nahoře vydržte vteřinu.</p>'
                 '<p><strong>4. Chůze do stran.</strong> Mini band nad kolena nebo ke kotníkům, mírný podřep. Dělejte malé kroky stranou, guma zůstává napnutá a trup se nekomíhá. Deset kroků jedním směrem a zpět.</p>'
                 '<p><strong>5. Výpad s gumou.</strong> Přední noha stojí na gumě, konce v rukou u ramen. Klesněte zadním kolenem k zemi a vytlačte se přes přední patu. Po sérii vyměňte nohy.</p>'),
             cat='posilovaci-gumy', n=4),
        dict(h2='Cviky na záda, hrudník a ramena',
             html=(
                 '<p><strong>6. Přítah ve stoje.</strong> Gumu ukotvěte ve výšce hrudníku, ustupte, až je napnutá. Táhněte lokty podél těla dozadu a stáhněte lopatky k sobě. Ramena nezvedejte k uším.</p>'
                 '<p><strong>7. Přítah vsedě.</strong> Seďte s nataženýma nohama, guma kolem chodidel. Táhněte konce k pupku s rovnými zády, jako na veslařském trenažéru.</p>'
                 '<p><strong>8. Rozpínání před tělem.</strong> Gumu držte nataženýma rukama před hrudníkem na šířku ramen a roztáhněte ji do stran, až se dotkne hrudní kosti. Výborný cvik na držení těla po práci u počítače.</p>'
                 '<p><strong>9. Tlak nad hlavu.</strong> Stůjte na gumě, konce u ramen, a vytlačte je nad hlavu. Bedra neprohýbejte, břicho a hýždě držte zpevněné.</p>'
                 '<p><strong>10. Kliky s gumou.</strong> Gumu veďte přes záda pod lopatkami a konce přidržte dlaněmi na zemi. Guma přidá odpor v horní části kliku. Kdo klik nezvládne, cvičí s koleny na zemi bez gumy.</p>')),
        dict(h2='Cviky na paže a střed těla',
             html=(
                 '<p><strong>11. Bicepsový zdvih.</strong> Stůjte na gumě, lokty u těla, a přitahujte dlaně k ramenům. Lokty se nepohybují dopředu.</p>'
                 '<p><strong>12. Tricepsové propínání.</strong> Gumu ukotvěte vysoko nebo ji přidržte jednou rukou u hrudníku. Druhou rukou propínejte loket dolů, nadloktí zůstává u těla.</p>'
                 '<p><strong>13. Pallofův tlak.</strong> Gumu ukotvěte z boku ve výšce hrudníku. Držte ji oběma rukama u hrudní kosti a vytlačte před sebe. Guma vás táhne do rotace a vaším úkolem je jí odolat. Tři vteřiny výdrž, pak zpět.</p>'
                 '<p><strong>14. Mrtvý brouk s gumou.</strong> Lehněte na záda, gumu ukotvěte za hlavou a držte ji nataženýma rukama nad hrudníkem. Nohy pokrčené ve vzduchu. Střídavě natahujte nohy k zemi, bedra zůstávají přitisknutá k podložce.</p>'
                 '<p>Na zemi cvičte na protiskluzové podložce, šetří lokty, kolena i gumu před ostrými hranami dlažby. Vybírat můžete v kategorii <a href="/joga-a-podlozky/">podložky na jógu a cvičení</a>.</p>'),
             cat='joga-a-podlozky', n=4),
        dict(h2='Třídenní plán pro začátečníky',
             html=(
                 '<p>Plán je stavěný na tři tréninky týdně se dnem pauzy mezi nimi. Každý trénink trvá zhruba 30 minut včetně rozcvičení. Mezi sériemi odpočívejte 45 až 90 vteřin.</p>'
                 + BAND_PLAN +
                 '<p><strong>Jak přidávat:</strong> když zvládnete všechny série s horní hranicí opakování a čistou technikou, přejděte na tužší gumu, gumu zdvojte nebo zkraťte úchop. '
                 'Další možnost je zpomalit návrat na čtyři vteřiny nebo přidat výdrž v nejtěžším bodě. Po šesti až osmi týdnech cviky obměňte.</p>'
                 '<p>Před tréninkem si dejte pět minut lehkého pohybu, třeba chůzi po schodech nebo kroužení pažemi a výkopy. Inspiraci na kardio bez stroje najdete v článku <a href="/kardio-doma/">kardio doma</a>.</p>')),
        dict(h2='Nejčastější chyby',
             html=(
                 '<ul><li><strong>Moc lehká guma.</strong> Když dáte 30 opakování bez únavy, trénujete hlavně vytrvalost a pokrok se zastaví.</li>'
                 '<li><strong>Rychlý návrat.</strong> Guma vás „vystřelí“ zpět a svaly v brzdící fázi nepracují.</li>'
                 '<li><strong>Nekontrolovaná guma.</strong> Praskliny vznikají hlavně po přejetí přes ostrou hranu nebo po letech na slunci.</li>'
                 '<li><strong>Jen jeden cvik.</strong> Samotná chůze s mini bandem nenahradí dřep a přítah. Celé tělo potřebuje tlaky, tahy a cviky pro nohy.</li>'
                 '<li><strong>Kotvení za kliku.</strong> Dveře se mohou otevřít a guma vás udeří. Kotvu dávejte na stranu pantů a dveře zamkněte.</li></ul>'
                 '<p>Cvičení s gumou je šetrné, přesto ho lidé po úrazu, s bolestmi zad, kloubů nebo v těhotenství mají probrat s lékařem či fyzioterapeutem. Guma není zdravotnická pomůcka a tento článek nenahrazuje individuální rehabilitaci.</p>')),
        dict(h2='Péče o gumu a výběr v obchodě',
             html=(
                 '<p>Latex stárne působením slunce, tepla a olejů. Gumu skladujte v suchu a stínu, neodkládejte ji na topení a nečistěte ji ředidly. Stačí otřít vlhkým hadříkem a nechat uschnout. '
                 'Textilní hip bandy jdou obvykle vyprat v ruce, řiďte se štítkem.</p>'
                 '<p>Při nákupu srovnávejte rozměry, materiál a jestli sada obsahuje odstupňované síly. Dlouhé smyčky prodává řada značek, například <a href="/znacka/hms/">HMS</a> nebo <a href="/znacka/merco/">Merco</a>, '
                 'další drobnosti na cvičení jsou ve <a href="/fitness-pomucky/">fitness pomůckách</a>. Když gumy přestanou stačit, dalším krokem bývají <a href="/jednorucni-cinky/">jednoruční činky</a> nebo <a href="/kettlebelly/">kettlebell</a>.</p>'),
             cat='fitness-pomucky', n=4),
    ],
    faq=[
        ('Jakou sílu posilovací gumy si mám koupit jako začátečník?',
         '<p>Nejvýhodnější je sada tří až pěti gum jedné značky. Lehčí použijete na ramena a paže, tužší na nohy a záda. Správná guma je ta, se kterou uděláte 12 až 15 opakování a poslední jsou těžká.</p>'),
        ('Co znamenají barvy posilovacích gum?',
         '<p>Barva značí tuhost, ale stupnice se liší podle výrobce. U TheraBand jde od nejlehčí béžová, žlutá, červená, zelená, modrá, černá, stříbrná a zlatá. U jiných značek se řiďte tabulkou výrobce.</p>'),
        ('Dá se s gumou nabrat svaly?',
         '<p>Ano, pokud gumu postupně měníte za tužší a série vedete blízko únavy. Pro hodně silné cviky na nohy ale guma časem nestačí a hodí se přidat činky nebo kettlebell.</p>'),
        ('Jak často cvičit s posilovací gumou?',
         '<p>Pro celé tělo dvakrát až třikrát týdně se dnem odpočinku mezi tréninky. Lehké cviky na ramena a mini band jako rozcvička můžete zařadit i častěji.</p>'),
        ('Jaký je rozdíl mezi mini bandem a power bandem?',
         '<p>Mini band je krátká smyčka nad kolena nebo kotníky na hýždě a kyčle. Power band je dlouhá smyčka kolem dvou metrů na cviky pro celé tělo a dopomoc na hrazdě.</p>'),
        ('Jak dlouho posilovací guma vydrží?',
         '<p>Záleží na četnosti a péči. Gumu kontrolujte před každým cvičením a při prasklinách, natržení nebo lepkavém povrchu ji vyměňte. Skladování v teple a na slunci její život zkracuje.</p>'),
        ('Můžu gumu uvázat do dveří?',
         '<p>Ano, ale s kotvou do dveří, která se vkládá do škvíry na straně pantů. Dveře zavřete a ideálně zamkněte, aby je nikdo neotevřel během cviku.</p>'),
        ('Mám alergii na latex. Jakou gumu?',
         '<p>Hledejte textilní gumy nebo modely z TPE či jiného materiálu bez latexu. Informaci o materiálu najdete v popisu produktu.</p>'),
        ('Pomůže cvičení s gumou při bolesti zad?',
         '<p>Guma je cvičební pomůcka, ne léčba. Při bolestech zad nebo po úrazu se nejdřív poraďte s lékařem či fyzioterapeutem, který vám cviky vybere a dávkuje.</p>'),
    ],
    cats=['posilovaci-gumy', 'fitness-pomucky', 'joga-a-podlozky'],
    updated='2026-11-19')

# ---------------------------------------------------------------- co-je-pilates
PIL_COMPARE = T(['', 'Pilates na podložce (mat)', 'Pilates na reformeru'], [
    ['Vybavení', 'Podložka, případně míč, kruh, válec', 'Reformer: pojízdný vozík, pružiny, popruhy, opěrka nohou'],
    ['Odpor', 'Vlastní váha těla', 'Pružiny, nastavitelné podle cviku a úrovně'],
    ['Kde cvičit', 'Doma, v lekci, kdekoli', 'Hlavně ve studiu, doma jen s vlastním strojem'],
    ['Pro koho', 'Pro každého, nejlevnější start', 'Pro začátečníky i pokročilé, kdo chce přesné vedení pohybu'],
    ['Nároky na místo', 'Prostor velikosti podložky', 'Stroj dlouhý zhruba jako postel, plus místo kolem'],
])

GUIDES['co-je-pilates'] = dict(
    name='Co je pilates',
    h1='Co je pilates: principy, účinky a jak začít',
    seo_title='Co je pilates: historie, principy, reformer a cviky pro začátek',
    seo_desc='Co je pilates a pro koho je: kdo byl Joseph Pilates, šest principů, rozdíl mezi podložkou a reformerem, cviky pro začátečníky a co potřebujete doma.',
    intro_html=(
        '<p><strong>Pilates je systém cvičení zaměřený na kontrolu pohybu, zpevnění středu těla, dýchání a přesné provedení.</strong> '
        'Cviky se dělají pomalu, s malým počtem opakování a velkým důrazem na techniku, buď na podložce, nebo na strojích, z nichž nejznámější je reformer. '
        'Metodu vymyslel Joseph Pilates na začátku 20. století a sám ji nazýval Contrology. Cvičit může začátečník i pokročilý, protože obtížnost se mění pozicí, pákou a u reformeru pružinami.</p>'
        '<p>V článku najdete stručnou historii, princip metody, srovnání pilatesu na podložce a na reformeru, sedm cviků na začátek a rady k vybavení. '
        'Řekneme i to, co pilates není: není to léčba a lidé se zdravotními potížemi nebo v těhotenství by měli začít po poradě s lékařem.</p>'),
    sections=[
        dict(h2='Kdo byl Joseph Pilates a jak metoda vznikla',
             html=(
                 '<p>Joseph Hubertus Pilates se narodil 9. prosince 1883 v Mönchengladbachu v Německu. V roce 1912 odešel do Anglie a po vypuknutí první světové války byl jako občan nepřátelského státu internován, '
                 'nejprve v Lancasteru a pak na ostrově Man. V táborech začal ostatní vést ke cvičení a rozvíjet svůj systém.</p>'
                 '<p>V roce 1926 se přestěhoval do New Yorku a spolu s Clarou, svou pozdější ženou, otevřel studio. Metodu nazýval Contrology, tedy nauka o kontrole těla myslí. '
                 'Do studia chodili mimo jiné tanečníci, kteří metodu pomohli rozšířit. V roce 1945 vyšla kniha Return to Life Through Contrology s jeho cviky na podložce. Joseph Pilates zemřel v New Yorku 9. října 1967.</p>'
                 '<p>Po jeho smrti metodu dál učili jeho žáci, každý trochu po svém. Proto dnes vedle sebe existuje „klasický“ pilates, který se drží původních sestav, a „moderní“ či „současný“ pilates, který cviky upravuje podle novějších poznatků o pohybu.</p>')),
        dict(h2='Šest principů pilatesu',
             html=(
                 '<p>Šest principů, jak se o nich dnes mluví, sepsali až Philip Friedman a Gail Eisenová v knize z roku 1980 podle toho, co se naučili od Pilatesových žáků. Sám Pilates je takto nečísloval, ale dobře vystihují, jak se cvičí:</p>'
                 '<ol><li><strong>Koncentrace.</strong> Pozornost je u cviku, ne u telefonu nebo počítání opakování.</li>'
                 '<li><strong>Kontrola.</strong> Každý pohyb je řízený, bez švihu a bez „pádu“ do konečné polohy.</li>'
                 '<li><strong>Střed (centrum).</strong> Pohyb vychází ze zpevněného trupu: břicha, zad, pánevního dna a hýždí. Anglicky se mu říká powerhouse.</li>'
                 '<li><strong>Plynulost.</strong> Cviky na sebe navazují a pohyb nemá trhané zastávky.</li>'
                 '<li><strong>Přesnost.</strong> Lépe pět správných opakování než dvacet nepřesných.</li>'
                 '<li><strong>Dýchání.</strong> Dech se sladí s pohybem. Obvykle se nadechuje nosem do hrudníku a do stran žeber a vydechuje při náročnější fázi cviku.</li></ol>'
                 '<p>V praxi to znamená, že hodina pilatesu vypadá klidně, ale svaly středu těla pracují skoro nepřetržitě. Kdo čeká rychlé tempo jako v aerobiku, bývá z první lekce překvapený, kolik úsilí se schovává v pomalém pohybu.</p>')),
        dict(h2='Pilates na podložce a na reformeru',
             html=(
                 '<p>Základní forma je pilates na podložce, anglicky mat pilates. Kromě podložky nepotřebujete nic, odpor tvoří vlastní váha těla. Postupně se dají přidat malé pomůcky: overball, kruh, válec nebo gumy.</p>'
                 + PIL_COMPARE +
                 '<p><strong>Reformer</strong> je rám s pojízdným vozíkem, který se pohybuje proti pružinám. Cvičíte vleže, vsedě, v kleku i ve stoje a odpor se mění počtem a tuhostí pružin. '
                 'Pružiny umí pohyb ztížit, ale i ulehčit a vést, proto je reformer vhodný i pro začátečníky. Ve studiích se setkáte i s dalšími stroji, jako je věž (tower) nebo židle (chair).</p>'
                 '<p>Domácí reformer dává smysl, když víte, že u pilatesu vydržíte, a máte kam ho postavit. Některé modely jsou skládací. Před nákupem zkontrolujte délku, nosnost, počet pružin a jestli jde přikoupit box nebo plošinu.</p>'),
             cat='pilates-reformery', n=4),
        dict(h2='Co pilates dělá a co od něj nečekat',
             html=(
                 '<p>Pilates posiluje hlavně svaly trupu, hýždí a stabilizátory ramen a kyčlí, učí pohybovou kontrolu a pracuje s rozsahem pohybu. Lidé ho často popisují tak, že si lépe uvědomují držení těla a dech. '
                 'Je to nízkonárazové cvičení, takže nezatěžuje klouby doskoky.</p>'
                 '<p>Neslibujeme, že pilates vyléčí bolest zad, zúží pas nebo zhubne. Hubnutí určuje hlavně celkový příjem a výdej energie a pilates má spíš menší energetický výdej než běh nebo kolo. '
                 'Pro vytrvalost je dobré ho kombinovat s kardio aktivitou a pro sílu s posilováním.</p>'
                 '<p><strong>Zdraví:</strong> pilates ani reformer nejsou zdravotnický prostředek ani léčba. Při bolestech zad, po operaci, při osteoporóze, problémech s pánevním dnem nebo v těhotenství začněte až po poradě s lékařem a cvičte s kvalifikovaným lektorem nebo fyzioterapeutem.</p>')),
        dict(h2='Sedm cviků pro začátečníky na podložce',
             html=(
                 '<p>Cvičte na měkké podložce, pomalu, 5 až 10 opakování od každého cviku. Pokud cokoli bolí, cvik vynechte.</p>'
                 '<p><strong>1. Dýchání a neutrální pánev.</strong> Lehněte na záda s pokrčenými koleny. Najděte polohu, kdy bedra nejsou ani přitlačená, ani prohnutá. Nadechujte se do stran žeber, s výdechem lehce vtáhněte podbřišek.</p>'
                 '<p><strong>2. Pánevní náklon a most.</strong> Z téže polohy s výdechem podsaďte pánev a obratel po obratli zvedněte záda do mostu. S nádechem nahoře, s výdechem pomalu zpět dolů.</p>'
                 '<p><strong>3. Stovka (hundred), upravená.</strong> Hlava a ramena nad zemí, nohy pokrčené v pravém úhlu. Paže drobně pumpují u boků, pět dob nádech, pět dob výdech. Začněte třiceti pumpnutími, ne stovkou.</p>'
                 '<p><strong>4. Natažení jedné nohy (single leg stretch).</strong> Hlava zvednutá, jedno koleno k hrudníku, druhá noha natažená šikmo nahoru. Nohy střídejte, bedra drží kontakt s podložkou.</p>'
                 '<p><strong>5. Plavání (swimming), v leže na břiše.</strong> Střídavě zvedejte protilehlou ruku a nohu jen pár centimetrů nad zem. Krk prodloužený, pohled do podložky.</p>'
                 '<p><strong>6. Série v leže na boku.</strong> Leh na boku, spodní ruka pod hlavou. Svrchní nohu zvedejte a veďte dopředu a dozadu, pánev se nehoupe.</p>'
                 '<p><strong>7. Předklon vsedě (spine stretch forward).</strong> Vsedě s nohama od sebe se s výdechem rolujte dopředu obratel po obratli a s nádechem se vracejte do vzpřímeného sedu.</p>'),
             cat='joga-a-podlozky', n=4),
        dict(h2='Jak začít: lekce, online video, nebo sám doma',
             html=(
                 '<ol><li><strong>Úvodní lekce s lektorem.</strong> Pár hodin pod dohledem naučí správné zapojení středu a dýchání. Ve skupině se ptejte na úpravy cviků.</li>'
                 '<li><strong>Pravidelnost.</strong> Dvě až tři kratší cvičení týdně bývají lepší než jedno dlouhé.</li>'
                 '<li><strong>Postup.</strong> Až základní cviky zvládnete bez námahy v krku a bedrech, přidejte těžší varianty nebo pomůcky.</li>'
                 '<li><strong>Reformer později nebo hned?</strong> Pokud máte studio blízko, reformer je skvělý učitel, protože pružiny pohyb vedou. Doma začněte podložkou.</li></ol>'
                 '<p>Pilates se dobře doplňuje s jógou, ale jde o jiné metody. Jóga víc pracuje s výdrží v pozicích a protažením, pilates s kontrolovaným pohybem a stabilitou. Spojené jsou v naší kategorii <a href="/joga-a-pilates/">jóga a pilates</a>.</p>')),
        dict(h2='Jak vypadá lekce a jak vybrat lektora',
             html=(
                 '<p>Typická skupinová lekce na podložce trvá 45 až 60 minut. Začíná dechem a nalezením neutrální polohy pánve a páteře, pokračuje sérií cviků vleže na zádech, na boku a na břiše a končí protažením ve stoji nebo vsedě. '
                 'Lekce na reformeru bývají menší, protože každý cvičenec potřebuje vlastní stroj, a lektor víc chodí mezi lidmi a upravuje nastavení pružin.</p>'
                 '<p>Při výběru lektora se ptejte, jaký výcvik absolvoval a zda učí spíš klasickou sestavu, nebo upravený současný styl. Dobrý lektor se na začátku zeptá na zdravotní omezení, nabídne lehčí variantu a opravuje polohu rukou a pánve. '
                 'Pokud vás po hodině bolí krk nebo bedra, řekněte mu to. Bývá to znak, že cvik je zatím příliš těžký nebo chybí zpevnění středu.</p>'
                 '<p>Online videa jsou dobrý doplněk, když už základ znáte. Vybírejte taková, kde lektor ukazuje i snazší variantu a vysvětluje dech, ne jen tempo a počet opakování.</p>')),
        dict(h2='Vybavení: co potřebujete a co je navíc',
             html=(
                 '<p><strong>Podložka</strong> pro pilates může být o něco silnější než na jógu, protože se hodně cvičí vleže na zádech a rolování přes páteř tlačí na obratle. Dobrá je protiskluzová a dost dlouhá na leh.</p>'
                 '<p><strong>Malé pomůcky</strong> dělají cvičení pestřejší: overball (měkký malý míč), pilates kruh pro odpor mezi stehny nebo v dlaních, válec na rovnováhu, gumy a lehké činky. '
                 'Najdete je v kategorii <a href="/pilates-pomucky/">pilates pomůcky</a>, gumy pak v <a href="/posilovaci-gumy/">posilovacích gumách</a>.</p>'
                 '<p><strong>Reformer</strong> je největší investice. Porovnejte délku vozíku vůči vaší výšce, počet a typ pružin, nosnost, skladnost a příslušenství. Domácí reformery prodává mimo jiné <a href="/znacka/insportline/">inSPORTline</a>.</p>'
                 '<p>Oblečení stačí přiléhavé a pružné, aby lektor viděl polohu pánve a kolen. Cvičí se bosky nebo v protiskluzových ponožkách.</p>'),
             cat='pilates-pomucky', n=4),
    ],
    faq=[
        ('Co je pilates jednoduše?',
         '<p>Cvičení zaměřené na zpevnění středu těla, kontrolu pohybu a dýchání. Cvičí se pomalu a přesně, na podložce nebo na strojích, jako je reformer.</p>'),
        ('Kdo vymyslel pilates?',
         '<p>Joseph Pilates, narozený roku 1883 v Německu. Systém rozvíjel během internace v Anglii za první světové války a od roku 1926 ho učil ve svém studiu v New Yorku. Sám ho nazýval Contrology.</p>'),
        ('Jaký je rozdíl mezi pilatesem a jógou?',
         '<p>Jóga pochází z indické tradice a pracuje víc s pozicemi, výdrží a protažením. Pilates je západní cvičební systém zaměřený na kontrolu pohybu a stabilitu trupu. V praxi se mohou doplňovat.</p>'),
        ('Co je pilates reformer?',
         '<p>Stroj s pojízdným vozíkem, pružinami, popruhy a opěrkou na nohy. Pružiny dávají odpor nebo pohyb ulehčují, a tak se dá cvičit v mnoha polohách a úrovních.</p>'),
        ('Je pilates vhodný pro začátečníky?',
         '<p>Ano. Cviky mají jednodušší varianty a obtížnost se přidává postupně. Nejlepší je začít několika lekcemi s lektorem, který opraví techniku.</p>'),
        ('Jak často cvičit pilates?',
         '<p>Dvakrát až třikrát týdně je běžný rytmus. Krátké domácí cvičení na podložce se dá zařadit i častěji, pokud vás nic nebolí.</p>'),
        ('Pomůže pilates na bolest zad?',
         '<p>Pilates není léčba. Lidé s bolestmi zad by měli cvičení probrat s lékařem nebo fyzioterapeutem, který určí, jaké cviky jsou pro ně vhodné.</p>'),
        ('Můžu cvičit pilates v těhotenství?',
         '<p>Jen po poradě s lékařem a ideálně v lekci určené pro těhotné. Řada cviků vleže na zádech nebo na břiše se v těhotenství upravuje nebo vynechává.</p>'),
        ('Co si vzít na první hodinu pilatesu?',
         '<p>Přiléhavé pružné oblečení, protiskluzové ponožky, pití a ručník. Podložku studia většinou půjčují, pro cvičení doma si pořiďte vlastní.</p>'),
    ],
    cats=['pilates-reformery', 'pilates-pomucky', 'joga-a-pilates', 'joga-a-podlozky'],
    updated='2026-11-19')

# ---------------------------------------------------------------- kettlebell-cviky
KB_WEIGHT = T(['Kdo', 'Swing, dřep, mrtvý tah', 'Tlak nad hlavu, get-up'], [
    ['Žena bez zkušeností se silovým tréninkem', '8–12 kg', '6–8 kg'],
    ['Žena se zkušeností', '12–16 kg', '8–12 kg'],
    ['Muž bez zkušeností se silovým tréninkem', '12–16 kg', '8–12 kg'],
    ['Muž se zkušeností', '16–24 kg', '12–16 kg'],
])

KB_PLAN = T(['Týden', 'Trénink A', 'Trénink B'], [
    ['1–2', 'Mrtvý tah s kettlebellem 3 × 10, goblet dřep 3 × 8, most 3 × 12', 'Nácvik swingu 5 × 10, get-up nácvik s botou na pěsti 3 × 1 na stranu'],
    ['3–4', 'Swing 6 × 10, goblet dřep 3 × 10, přítah v předklonu 3 × 10', 'Clean 4 × 5 na stranu, tlak 4 × 5 na stranu, farmářská chůze 3 × 30 m'],
    ['5–8', 'Swing 10 × 10 (pauza podle potřeby), goblet dřep 4 × 8', 'Get-up 5 × 1 na stranu, clean + tlak 5 × 5, výpady 3 × 8'],
])

GUIDES['kettlebell-cviky'] = dict(
    name='Kettlebell cviky',
    h1='Kettlebell cviky: swing, goblet dřep, clean, tlak a turecké vstávání',
    seo_title='Kettlebell cviky: swing, goblet dřep, get-up a plán pro začátek',
    seo_desc='Kettlebell cviky pro začátečníky: jakou váhu zvolit, technika swingu, goblet dřepu, clean, tlaku a tureckého vstávání, osmitýdenní plán a bezpečnost.',
    intro_html=(
        '<p><strong>Které kettlebell cviky se naučit jako první?</strong> Mrtvý tah, goblet dřep a swing. Mrtvý tah naučí předklon v kyčlích s rovnými zády, goblet dřep správný dřep a swing z nich dělá dynamický cvik, který zapojí hýždě, zadní stranu stehen, záda i úchop. '
        'Potom přidejte clean (nadhoz k rameni), tlak nad hlavu a turecké vstávání. Žena obvykle začíná s 8 až 12 kg, muž s 12 až 16 kg, s tím, že na swing se hodí těžší koule než na tlak nad hlavu.</p>'
        '<p>Níže popisujeme techniku každého cviku krok za krokem, nejčastější chyby, osmitýdenní plán dvakrát týdně a bezpečnostní pravidla. Kettlebell je technický nástroj a pár lekcí s trenérem se vyplatí.</p>'),
    sections=[
        dict(h2='Jakou váhu kettlebellu zvolit',
             html=(
                 '<p>Kettlebell je koule s madlem, které je posunuté mimo těžiště. Proto se s ním dá švihat a přehazovat jinak než s jednoruční činkou. Tradiční ruská jednotka je pud, zhruba 16 kg, a proto se 16kg koule často považuje za standard pro muže.</p>'
                 + KB_WEIGHT +
                 '<p>Tabulka je orientační, vychází z běžných doporučení trenérů. Silnější lidé nebo sportovci začnou výš. Kdo chce mít jen jednu kouli, vezme tu těžší pro swing a dřep, protože tlak nad hlavu se dá nahradit jinými cviky. '
                 'Ideální jsou postupně dvě nebo tři koule s odstupem 4 kg.</p>'
                 '<p><strong>Litina, nebo vinyl?</strong> Litinové koule mají menší rozměry a hladké madlo. Vinylem potažené chrání podlahu, ale jsou objemnější. U soutěžních ocelových kettlebellů je rozměr stejný pro všechny váhy. '
                 'Madlo by mělo být hladké, bez ostrých švů, a dost široké pro obě ruce.</p>'),
             cat='kettlebelly', n=4),
        dict(h2='Než začnete: místo, obuv a rozcvička',
             html=(
                 '<ul><li><strong>Místo:</strong> kolem sebe nechte aspoň dva metry volného prostoru, hlavně před sebou. Nikdo nesmí procházet před vámi, když šviháte.</li>'
                 '<li><strong>Podlaha:</strong> rovná, neklouzavá. Na parkety dejte gumovou podložku, koule může vyklouznout a podlahu poškodit.</li>'
                 '<li><strong>Obuv:</strong> plochá podrážka nebo naboso. Měkká běžecká bota s vysokou patou ztěžuje stabilitu.</li>'
                 '<li><strong>Rozcvička:</strong> pět až osm minut: kroužení v kyčlích a ramenou, mosty, dřepy bez váhy a pár lehkých mrtvých tahů.</li></ul>'
                 '<p>Úchop je u kettlebellu často limitující. Ruce mějte suché, případně použijte magnézium. Rukavice moc nedoporučujeme, madlo v nich klouže.</p>')),
        dict(h2='Mrtvý tah a goblet dřep: základ všeho',
             html=(
                 '<p><strong>Mrtvý tah s kettlebellem.</strong> Postavte se nad kouli, chodidla na šířku boků až ramen, koule mezi nártmi.</p>'
                 '<ol><li>Pošlete zadek dozadu, kolena se mírně pokrčí, záda zůstávají rovná a hrudník míří šikmo dopředu.</li>'
                 '<li>Uchopte madlo oběma rukama, stáhněte ramena od uší a vytvořte napětí v zádech.</li>'
                 '<li>Vstaňte tlakem nohou do země a vytlačením pánve dopředu. Nahoře zpevněte hýždě, ale neprohýbejte se v bedrech.</li>'
                 '<li>Vraťte kouli stejnou cestou: nejdřív kyčle dozadu, pak kolena.</li></ol>'
                 '<p><strong>Goblet dřep.</strong> Kettlebell držte za rohy madla nebo za kouli u hrudníku, lokty dolů. Dřepněte mezi kolena tak hluboko, jak udržíte rovná záda a paty na zemi, a vstaňte. '
                 'Váha vepředu pomáhá udržet trup vzpřímený, proto se goblet dřep učí jako první varianta dřepu.</p>'),
             cat='kettlebelly', n=4),
        dict(h2='Kettlebell swing krok za krokem',
             html=(
                 '<p>Swing je švih koule z kyčlí. Nejde o dřep ani o zvedání paží: ruce jsou jen „lana“, sílu dodávají hýždě a zadní strana stehen. Rozlišuje se ruský swing do výšky hrudníku a americký nad hlavu. Začínejte ruským.</p>'
                 '<ol><li><strong>Výchozí poloha:</strong> koule asi 30 cm před vámi, předklon v kyčlích, ruce na madle, kettlebell nakloněný k vám.</li>'
                 '<li><strong>Nápřah:</strong> přitáhněte kouli dozadu mezi stehna jako přihrávku v americkém fotbale. Předloktí se dotýkají vnitřní strany stehen, madlo je nad koleny.</li>'
                 '<li><strong>Výšvih:</strong> prudce vytlačte pánev dopředu a zpevněte hýždě. Koule vyletí do výšky zhruba hrudníku, paže jsou natažené, ale nezvedají ji.</li>'
                 '<li><strong>Nahoře:</strong> postavení jako v prkně ve stoje, kolena propnutá, žádné zaklánění.</li>'
                 '<li><strong>Návrat:</strong> nechte kouli padat, předkloňte se v kyčlích až ve chvíli, kdy se předloktí blíží k tělu, a plynule navažte další opakování.</li>'
                 '<li><strong>Odložení:</strong> po posledním opakování kouli zpomalte nápřahem dozadu a položte ji zpět před sebe, ne pod sebe.</li></ol>'
                 '<p><strong>Časté chyby:</strong> kulatá záda, dřepování místo předklonu, tahání paží, zaklánění nahoře a koule, která v nápřahu padá pod kolena.</p>')),
        dict(h2='Clean a tlak nad hlavu',
             html=(
                 '<p><strong>Clean</strong> přenese kouli z prostoru mezi nohama do polohy u ramene, které se říká rack. Koule leží na vnější straně předloktí, zápěstí je rovné, loket u těla a palec u klíční kosti.</p>'
                 '<ol><li>Začněte jako u swingu jednou rukou.</li>'
                 '<li>Při výšvihu držte loket blízko těla a veďte kouli krátkou drahou podél trupu, jako byste zapínali bundu na zip.</li>'
                 '<li>V poslední chvíli protáhněte ruku madlem, aby koule „dosedla“ na předloktí, místo aby do něj narazila.</li></ol>'
                 '<p>Když vás koule mlátí do předloktí, vede ji příliš daleko od těla. Zpomalte a zkraťte dráhu.</p>'
                 '<p><strong>Tlak nad hlavu</strong> začíná z racku. Zpevněte hýždě a břicho a vytlačte kouli nahoru, až je paže natažená vedle ucha a zápěstí rovné. Dolů ji spouštějte pod kontrolou zpět do racku. '
                 'Bedra se nesmí prohýbat. Pokud se prohýbají, je koule moc těžká.</p>'),
             cat='kettlebelly', n=4),
        dict(h2='Turecké vstávání (Turkish get-up)',
             html=(
                 '<p>Get-up je pomalý cvik z lehu do stoje s koulí nad hlavou. Trénuje stabilitu ramene, střed těla a koordinaci. Učte se ho nejdřív bez váhy nebo s botou postavenou na pěsti, která nesmí spadnout.</p>'
                 '<ol><li>Leh na zádech, kettlebell v pravé ruce nad hrudníkem, pravá noha pokrčená, levá ruka a noha šikmo od těla.</li>'
                 '<li>Odtlačte se pravou nohou a převalte se na levý loket. Pohled stále na kouli.</li>'
                 '<li>Propněte levou ruku do dlaně.</li>'
                 '<li>Zvedněte pánev do mostu a protáhněte levou nohu pod tělem do kleku na levém koleni.</li>'
                 '<li>Narovnejte trup do kleku, levá ruka se odlepí od země.</li>'
                 '<li>Natočte zadní nohu rovnoběžně, vstaňte z výpadu.</li>'
                 '<li>Stejnou cestou krok po kroku zpět na zem.</li></ol>'
                 '<p>Paže s koulí je po celou dobu kolmo k zemi a zápěstí rovné. Jedno opakování na každou stranu trvá i půl minuty, a to je v pořádku.</p>')),
        dict(h2='Doplňkové cviky: přítah, farmářská chůze a výpady',
             html=(
                 '<p><strong>Přítah v předklonu.</strong> Jednou rukou se opřete o lavici nebo koleno, záda rovně. Kouli táhněte loktem podél těla k boku a pomalu spusťte. Vyvažuje tlaky a swingy, které namáhají spíš přední stranu těla.</p>'
                 '<p><strong>Farmářská chůze.</strong> Vezměte kouli do jedné nebo obou rukou a jděte vzpřímeně 20 až 40 metrů. Ramena dolů, trup se nenaklání. Posiluje úchop, ramena a boční svaly trupu.</p>'
                 '<p><strong>Výpady s kettlebellem.</strong> Kouli držte u hrudníku jako u goblet dřepu nebo v racku. Krok vzad do výpadu je pro kolena šetrnější než krok vpřed a lépe se kontroluje rovnováha.</p>'
                 '<p>Tyto tři cviky nevyžadují tolik techniky jako swing nebo get-up, takže se hodí do dnů, kdy jste unavení, ale chcete se hýbat.</p>')),
        dict(h2='Osmitýdenní plán pro začátečníky',
             html=(
                 '<p>Plán počítá se dvěma tréninky týdně, mezi nimi aspoň dva dny jinou aktivitu nebo odpočinek. Před každým tréninkem rozcvička, mezi sériemi pauza 60 až 90 vteřin.</p>'
                 + KB_PLAN +
                 '<p>Když se technika s rostoucí únavou zhoršuje, sérii ukončete dřív. Až všechny série zvládnete s rezervou, zvyšte váhu o jeden stupeň u swingu a dřepu. U tlaku a get-upu postupujte pomaleji.</p>'
                 '<p>K tréninku s koulí se hodí i <a href="/posilovaci-gumy/">posilovací gumy</a> na rozcvičení ramen a <a href="/jednorucni-cinky/">jednoruční činky</a> pro cviky, kde kettlebell není praktický.</p>')),
        dict(h2='Bezpečnost a péče o kettlebell',
             html=(
                 '<ul><li><strong>Kvalita před počtem.</strong> Většina problémů vzniká na konci série z únavy.</li>'
                 '<li><strong>Kouli nechte padnout, když to nejde.</strong> Pokud ztratíte kontrolu nad swingem, ustupte a nechte ji odletět dopředu, nesnažte se ji chytat.</li>'
                 '<li><strong>Nezačínejte americkým swingem.</strong> Koule nad hlavou vyžaduje rozsah v ramenou, který mnoho lidí nemá.</li>'
                 '<li><strong>Děti a mazlíčci pryč.</strong> Švihající koule kolem sebe potřebuje volný prostor.</li></ul>'
                 '<p>Lidé po úrazech zad, ramen či kolen, s vysokým krevním tlakem nebo v těhotenství by měli trénink probrat s lékařem nebo fyzioterapeutem. Text nenahrazuje lekci s trenérem.</p>'
                 '<p>Litinovou kouli otřete po tréninku do sucha, aby madlo nerezivělo, a skladujte ji na zemi, ne na polici. Další váhy a příslušenství pro domácí cvičení najdete v <a href="/cinky-a-kotouce/">činkách a kotoučích</a>, '
                 'kettlebelly prodávají třeba <a href="/znacka/hms/">HMS</a> nebo <a href="/znacka/insportline/">inSPORTline</a>.</p>'),
             cat='cinky-a-kotouce', n=4),
    ],
    faq=[
        ('Jaký kettlebell si mám koupit jako začátečník?',
         '<p>Ženy obvykle začínají s 8 až 12 kg, muži s 12 až 16 kg. Na swing a dřep se hodí těžší koule než na tlak nad hlavu, takže časem se vyplatí mít dvě váhy.</p>'),
        ('Který kettlebell cvik je nejlepší?',
         '<p>Žádný nevyhrává. Pro začátek dává smysl swing, goblet dřep a mrtvý tah, později clean, tlak a turecké vstávání. Dohromady pokryjí celé tělo.</p>'),
        ('Jaký je rozdíl mezi ruským a americkým swingem?',
         '<p>Ruský swing končí ve výšce hrudníku, americký nad hlavou. Americký vyžaduje dobrou pohyblivost ramen a začátečníkům ho nedoporučujeme.</p>'),
        ('Bolí mě po swingu bedra. Co dělám špatně?',
         '<p>Nejčastěji kulatíte záda, švih táhnete rukama nebo se nahoře zakláníte. Snižte váhu, natočte se na video a nechte techniku zkontrolovat trenérem. Pokud bolest trvá, navštivte lékaře.</p>'),
        ('Kolikrát týdně cvičit s kettlebellem?',
         '<p>Začátečník dvakrát až třikrát týdně s pauzou mezi tréninky. Krátké série swingů se dají přidat i do jiných dnů, pokud se cítíte zotavení.</p>'),
        ('Litinový, nebo vinylový kettlebell?',
         '<p>Litinový je menší a odolnější, vinylový je šetrnější k podlaze, ale objemnější. U soutěžních ocelových koulí je velikost stejná napříč váhami.</p>'),
        ('Mám cvičit s kettlebellem v rukavicích?',
         '<p>Spíš ne, madlo v rukavici klouže. Lepší je suchá ruka, případně magnézium, a hladké madlo bez ostrých švů.</p>'),
        ('Co je turecké vstávání?',
         '<p>Turkish get-up: pomalý přechod z lehu do stoje a zpět s koulí drženou nad hlavou. Učí stabilitu ramene a koordinaci, nacvičuje se nejdřív bez váhy.</p>'),
        ('Je kettlebell vhodný na hubnutí?',
         '<p>Kettlebell je nástroj na silový a kondiční trénink. Váha závisí hlavně na celkové energetické bilanci, trénink s koulí je jedna z cest, jak zvýšit pohyb.</p>'),
    ],
    cats=['kettlebelly', 'cinky-a-kotouce', 'fitness-pomucky'],
    updated='2026-11-19')

# ---------------------------------------------------------------- rozcvicka-pred-behem
WARM_ROUTINE = T(['Minuta', 'Co dělat', 'Jak dlouho / kolikrát'], [
    ['0–4', 'Svižná chůze, pak velmi pomalý klus', '4 minuty'],
    ['4–5', 'Kroužení pažemi a rameny, otáčení trupu', '10× každým směrem'],
    ['5–6', 'Švihy nohou dopředu-dozadu u zdi', '10× každou nohou'],
    ['6–7', 'Švihy nohou do stran', '10× každou nohou'],
    ['7–8', 'Výpady s rotací trupu, chůze', '6× na každou stranu'],
    ['8–9', 'Liftink, zakopávání (běžecká abeceda)', '2 × 20 m'],
    ['9–10', 'Dvě až tři stupňované rovinky', '60–80 m, volně zpět'],
])

COOL_STRETCH = T(['Sval', 'Poloha', 'Výdrž'], [
    ['Lýtko', 'Ruce o zeď, zadní noha natažená, pata na zemi', '20–30 s na nohu, pak s pokrčeným kolenem'],
    ['Přední strana stehna', 'Ve stoje přitáhnout patu k hýždi, kolena u sebe', '20–30 s na nohu'],
    ['Zadní strana stehna', 'Noha na nízkém schodu, předklon v kyčlích s rovnými zády', '20–30 s na nohu'],
    ['Hýždě', 'Vleže kotník přes koleno druhé nohy a přitáhnout', '20–30 s na stranu'],
    ['Flexory kyčle', 'Klek na jednom koleni, pánev posunout dopředu', '20–30 s na stranu'],
])

GUIDES['rozcvicka-pred-behem'] = dict(
    name='Rozcvička před během',
    h1='Rozcvička před během a strečink po něm: desetiminutová sestava',
    seo_title='Rozcvička před během a strečink po něm: 10 minut, co funguje',
    seo_desc='Jak se rozcvičit před během: proč dynamická rozcvička a ne statický strečink, desetiminutová sestava krok za krokem, vyklusání a protažení po běhu.',
    intro_html=(
        '<p><strong>Jak se rozcvičit před během?</strong> Začněte čtyřmi až pěti minutami svižné chůze a pomalého klusu, pak přidejte dynamické cviky v pohybu: švihy nohou, výpady, kroužení pažemi a prvky běžecké abecedy. '
        'Celé to zabere kolem deseti minut. Dlouhé statické protahování s výdrží v jedné poloze si nechte až po běhu nebo na jiný čas. Před tempovým tréninkem nebo závodem přidejte několik stupňovaných rovinek.</p>'
        '<p>V článku vysvětlíme, co o statickém a dynamickém strečinku říkají přehledové studie, ukážeme sestavu na deset minut, vyklusání a krátký strečink po běhu. '
        'Pokud s během začínáte, přečtěte si i <a href="/zaciname-behat-v-zime/">jak začít běhat v zimě</a>.</p>'),
    sections=[
        dict(h2='Proč se rozcvičovat',
             html=(
                 '<p>Rozcvička postupně zvedá tepovou frekvenci a teplotu svalů a připravuje klouby a nervovou soustavu na pohyb, který přijde. První kilometr pak není šok, ale pokračování. '
                 'Hlavně před rychlejším během, intervaly nebo kopci je rozdíl znát: bez rozcvičky se tělo do tempa dostává pomaleji a krok je toporný.</p>'
                 '<p>Před lehkým klidným výběhem může rozcvičkou být i samotných prvních pět až deset minut běhu ve velmi pomalém tempu. Čím rychlejší a náročnější trénink, tím delší a specifičtější má být rozcvička.</p>'
                 '<ul><li><strong>Lehký výběh:</strong> chůze a pomalý klus, pár dynamických cviků.</li>'
                 '<li><strong>Intervaly a tempo:</strong> celá desetiminutová sestava a 3–4 rovinky.</li>'
                 '<li><strong>Závod:</strong> 10–20 minut volného klusu, dynamické cviky, rovinky v závodním tempu, poslední 10–15 minut před startem.</li></ul>'
                 '<p>Rozcvička je také chvíle, kdy zjistíte, jak se dnes cítíte. Když jsou nohy po předchozím dni těžké a tep vyšší než obvykle, je to rozumný důvod plánovaný rychlý trénink odložit nebo zkrátit. '
                 'Obráceně se po pár minutách klusu často ukáže, že počáteční ztuhlost byla jen ranní a tělo se rozběhne. Bez rozcvičky tyto signály snadno přehlédnete.</p>')),
        dict(h2='Statický, nebo dynamický strečink? Co říkají studie',
             html=(
                 '<p><strong>Statický strečink</strong> znamená výdrž v protažené poloze, obvykle 20 až 60 vteřin. <strong>Dynamický strečink</strong> jsou kontrolované pohyby v rozsahu, například švihy nohou nebo výpady v chůzi.</p>'
                 '<p>Metaanalýza Simice a kolegů z roku 2013, která shrnula 104 studií, zjistila, že statický strečink těsně před výkonem v průměru snížil maximální sílu o 5,4 %, výbušnost o zhruba 2 %. '
                 'Nejmenší vliv měly výdrže do 45 vteřin. Autoři doporučili, aby statický strečink nebyl jedinou náplní rozcvičky.</p>'
                 '<p>Přehled Lauersena a kolegů z roku 2014 v British Journal of Sports Medicine porovnal randomizované studie prevence sportovních zranění. U strečinku ochranný účinek nenašel, '
                 'kdežto silový trénink zranění v zahrnutých studiích výrazně snižoval. Pro běžce z toho plyne, že protahování není pojistkou proti zraněním a posilování nohou a středu těla má smysl.</p>'
                 '<p><strong>Co to znamená v praxi:</strong> krátké protažení před během, pokud vám je příjemné, ničemu neublíží. Hlavní část rozcvičky má být ale pohyb: klus a dynamické cviky. Studie nedávají důvod se protahování bát, jen ho nepřeceňovat.</p>')),
        dict(h2='Desetiminutová rozcvička krok za krokem',
             html=(
                 '<p>Sestava je pro venku i doma před pásem. Cviky dělejte v plynulém rytmu, bez švihnutí na doraz.</p>'
                 + WARM_ROUTINE +
                 '<ol><li><strong>Chůze a klus:</strong> začněte opravdu pomalu. Dýchat byste měli tak, abyste mohli mluvit.</li>'
                 '<li><strong>Paže a trup:</strong> velké kruhy pažemi dopředu a dozadu, pak rotace trupu s volnými pažemi.</li>'
                 '<li><strong>Švihy nohou:</strong> přidržte se zdi nebo stromu, noha volně kmitá dopředu a dozadu, rozsah zvětšujte postupně. Pak stranou před tělem.</li>'
                 '<li><strong>Výpady s rotací:</strong> krok vpřed do výpadu, trup se otočí k přední noze, pak krok další nohou.</li>'
                 '<li><strong>Prvky abecedy:</strong> liftink (rychlé krátké kroky s vysokým kolenem) a zakopávání patami k hýždím. Technice se věnuje článek <a href="/bezecka-abeceda/">běžecká abeceda</a>.</li>'
                 '<li><strong>Rovinky:</strong> 60–80 m postupně zrychlujte až k rychlému, ale uvolněnému běhu a pak zpomalte. Zpátky volně klusem nebo chůzí.</li></ol>')),
        dict(h2='Rozcvička v zimě a ráno',
             html=(
                 '<p>V chladu trvá zahřátí déle. Rozcvičku můžete začít doma, kde uděláte kroužení a švihy, a ven vyjít, až budete zahřátí. První kilometr běžte pomaleji než obvykle.</p>'
                 '<p>Ráno po probuzení bývá tělo ztuhlejší. Rozcvičku protáhněte o pár minut a rychlé úseky zařaďte až v druhé polovině tréninku.</p>'
                 '<p>Při rozcvičce venku mějte vrstvu navíc, kterou pak sundáte, nebo běhejte okruh kolem domu. Na zimní obutí a oblečení se podívejte do kategorie <a href="/bezecka-obuv/">běžecká obuv</a> a do článku o tom, '
                 'jak <a href="/zaciname-behat-v-zime/">začít běhat v zimě</a>.</p>'),
             cat='bezecka-obuv', n=4),
        dict(h2='Jak poznat, že jste dost rozcvičení',
             html=(
                 '<p>Neexistuje přesný čas, který platí pro každého. Řiďte se tím, co cítíte. Po dobré rozcvičce je dech zrychlený, ale klidný, cítíte teplo ve svalech, často se objeví lehké pocení a krok je volnější než na začátku.</p>'
                 '<p>Pokud po deseti minutách pořád cítíte ztuhlé lýtko nebo kyčel, pokračujte pomalým klusem o pár minut déle. Když něco ostře bolí, nejde o ztuhlost, ale o signál přestat a nechat to prohlédnout.</p>'
                 '<p><strong>Rozcvička na běžeckém pásu</strong> funguje stejně: pár minut chůze se sklonem, pak pomalý klus. Dynamické cviky udělejte vedle pásu, ne na něm. Rovinky nahraďte třemi až čtyřmi úseky po 20 až 30 vteřinách v rychlejším tempu.</p>'
                 '<p><strong>Před závodem</strong> plánujte rozcvičku tak, aby skončila deset až patnáct minut před startem. V koridoru pak jen přešlapujte a udržujte teplo, třeba ve staré mikině, kterou odložíte. Nic nového, co jste nezkoušeli v tréninku, na závodě nezkoušejte.</p>')),
        dict(h2='Vyklusání po běhu',
             html=(
                 '<p>Po intervalech, tempovém běhu nebo závodu se hodí 5 až 10 minut volného klusu nebo chůze. Tep a dech se postupně zklidní, a hlavně se nezastavíte prudce s nohama ztěžklýma po námaze.</p>'
                 '<p>Po klidném výběhu stačí poslední minuty zpomalit a dojít domů chůzí. Vyklusání nemusí být dlouhé, aby splnilo účel. Důležitější pro regeneraci je spánek, jídlo a rozumný plán tréninků.</p>'
                 '<ul><li><strong>Po závodě:</strong> převlékněte se do suchého, napijte se a pak vyklusejte.</li>'
                 '<li><strong>V zimě:</strong> nevyklusávejte dlouho v propoceném tričku, rychle prochladnete.</li>'
                 '<li><strong>Po dlouhém běhu:</strong> chůze je často příjemnější než další klus.</li></ul>')),
        dict(h2='Strečink po běhu: pět poloh',
             html=(
                 '<p>Po běhu, kdy jsou svaly zahřáté, je vhodný čas na statické protažení. Neslibujeme, že zabrání bolesti svalů nebo zranění, ale pro mnoho lidí je to příjemná součást zklidnění a udržuje rozsah pohybu.</p>'
                 + COOL_STRETCH +
                 '<p>Protahujte do mírného tahu, ne do bolesti. Dýchejte klidně a nehoupejte se. Kdo má zkrácené svaly nebo ztuhlá lýtka, může doma použít <a href="/masazni-valce/">masážní válec</a>.</p>'),
             cat='masazni-valce', n=4),
        dict(h2='Nejčastější chyby',
             html=(
                 '<ul><li><strong>Žádná rozcvička před intervaly.</strong> Nejrychlejší úseky na studené svaly jsou zbytečné riziko.</li>'
                 '<li><strong>Pět minut statického strečinku místo pohybu.</strong> Tělo tím nezahřejete.</li>'
                 '<li><strong>Rozcvička jako trénink.</strong> Dlouhé sady skipů a výskoků vás unaví ještě před během.</li>'
                 '<li><strong>Švihy na doraz.</strong> Rozsah zvyšujte postupně, prudký švih s bolestí nepřináší nic.</li>'
                 '<li><strong>Vynechané posilování.</strong> Podle studií má na zranění větší vliv silový trénink než protahování. Dvakrát týdně dřep, výpady a výpony na lýtka dávají smysl.</li></ul>'
                 '<p>Lidé po zranění, s bolestmi kloubů, srdečními potížemi nebo v těhotenství by měli rozsah a intenzitu běhu i cvičení probrat s lékařem nebo fyzioterapeutem.</p>')),
        dict(h2='Co ještě pomůže: obuv, technika a vybavení',
             html=(
                 '<p>Rozcvička neopraví nevhodnou obuv. Bota má odpovídat povrchu a vaší chůzi. Jestli se vám chodidlo stáčí dovnitř, vysvětlujeme v článku <a href="/pronace-a-supinace/">pronace a supinace</a>, '
                 'obuv pro silnici najdete v <a href="/silnicni-bezecke-boty/">silničních běžeckých botách</a> a do terénu v <a href="/trailove-boty/">trailových botách</a>.</p>'
                 '<p>Pro tempo a rovinky se hodí <a href="/sportovni-hodinky/">sportovní hodinky</a>, které měří čas a tep. Pro posilování doma stačí <a href="/posilovaci-gumy/">posilovací gumy</a>, se kterými zvládnete výpony, mosty i výpady.</p>'),
             cat='silnicni-bezecke-boty', n=4),
    ],
    faq=[
        ('Jak dlouho se rozcvičovat před během?',
         '<p>Před lehkým během stačí pět minut chůze a pomalého klusu. Před intervaly nebo závodem počítejte deset až dvacet minut včetně dynamických cviků a rovinek.</p>'),
        ('Mám se před během protahovat?',
         '<p>Dlouhé statické protahování není potřeba. Studie ukazují, že výdrže před výkonem mohou krátkodobě mírně snížit sílu. Krátké protažení do 45 vteřin má malý vliv, hlavní část rozcvičky má být pohyb.</p>'),
        ('Co je dynamický strečink?',
         '<p>Protahování v pohybu: švihy nohou, výpady s rotací, kroužení pažemi. Svaly a klouby procházejí rozsahem bez dlouhé výdrže a tělo se zahřívá.</p>'),
        ('Předchází strečink zraněním při běhu?',
         '<p>Přehled randomizovaných studií z roku 2014 ochranný účinek strečinku nenašel. Silový trénink naopak počet zranění v zahrnutých studiích snižoval.</p>'),
        ('Mám se protahovat po běhu?',
         '<p>Můžete, pokud je vám to příjemné. Po běhu jsou svaly zahřáté a krátký statický strečink pomáhá zklidnit a udržet rozsah pohybu. Nečekejte ale, že zabrání bolesti svalů.</p>'),
        ('Co jsou stupňované rovinky?',
         '<p>Úseky 60 až 100 metrů, kdy postupně zrychlíte až k rychlému uvolněnému běhu a pak zpomalíte. Zařazují se na konec rozcvičky před rychlým tréninkem.</p>'),
        ('Jak se rozcvičit v zimě?',
         '<p>Začněte uvnitř, protáhněte rozcvičku o pár minut a první kilometr běžte pomaleji. Mějte vrstvu oblečení navíc, kterou po zahřátí sundáte.</p>'),
        ('Musím vyklusávat?',
         '<p>Po intervalech a závodě se vyklusání nebo chůze hodí. Po klidném výběhu stačí poslední minuty zpomalit.</p>'),
        ('Jak se rozcvičit před během do kopce nebo v terénu?',
         '<p>Stejně jako před rychlým během, jen přidejte pár výpadů a výponů na lýtka. První stoupání vyběhněte volněji, v terénu se nohy a kotníky musí přizpůsobit nerovnostem.</p>'),
        ('Je běžecká abeceda rozcvička?',
         '<p>Její prvky se do rozcvičky hodí, třeba liftink a zakopávání. Delší sada abecedy už je spíš samostatný technický trénink.</p>'),
    ],
    cats=['bezecka-obuv', 'silnicni-bezecke-boty', 'masazni-valce'],
    updated='2026-11-19')
