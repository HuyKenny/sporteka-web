"""sporteka.cz — wave 33b (19. 11. 2026): long text for the category posilovaci-kolecka (ab wheels / ab rollers).
General true facts only, no prices, no product counts, no test results. Model names were checked against the local
catalogue copy (Spokey Tween, Power System Twin Core / Phantom / Multi Core / Full Grip, Sedco AB roller Pro,
Insportline AB Roller AR0/AR1/AR4 and Pushabroll 3v1, Merco Giant AB / Multi Roller / AB Roller 2W / 3W, Sportago Ab Roller /
Multitrain, GymBeam Grip-Ring and sets with mat and bands, HMS WA03, Lifefit Exercise Wheel Single / Duo / FAT, Fitforce,
Sharp Shape, Corength AB Wheel Evolutive and 2-mode wheel, Springos and Actiget with knee pad, Yate, 4Fizjo).
Brands linked only if present in src/texts/znacky.json (insportline, merco, gymbeam, hms).

Sources:
- Escamilla et al., Physical Therapy 2006 (PubMed 16649890): roll-out with a wheeled device (Power Wheel) among the
  exercises with the highest rectus abdominis, external/internal oblique and latissimus dorsi EMG activity
- Escamilla et al., JOSPT 2010 (Swiss ball): pike and roll-out the most effective at recruiting core musculature
- Decathlon product pages: Corength "evolving ab wheel" with a removable elastic strap that assists the return and
  a knee mat; Corength "dual mode" wheel, stable or unstable mode, can be taken apart for storage
- insportline.eu: 3-in-1 Ab Roller Pushabroll = ab roller, push-up grips and water-bottle dumbbells in one
Left out (not verifiable): exact wheel diameters of individual models, load limits, which model has an inner spring
(described only as a type), any claim that the exercise treats or prevents back pain.
"""
from texty_vlna1a import T

NEW = {}

# ------------------------------------------------------------------ posilovaci-kolecka
NEW['posilovaci-kolecka'] = dict(long=True,
    title='Posilovací kolečka – ab wheel na břicho a střed těla',
    desc='Posilovací kolečka (ab wheel): jednoduchá, dvojitá, s pružinou i 3v1. Jak cvičit rollout bezpečně a jak vybrat. Porovnejte nabídky obchodů.',
    intro='<p><strong>Posilovací kolečko</strong>, anglicky ab wheel nebo ab roller, je jedno nebo dvě kola na ose se dvěma rukojeťmi. Cvičí se s ním hlavně rollout: z kleku nebo ze stoje kolečko odvalujete před sebe a zase přitahujete zpět. Práci odvedou břišní svaly, které drží pánev a bederní páteř v klidu, a k tomu ramena, široký sval zádový a paže. Pomůcka zabere v šuplíku méně místa než činka a dá se s ní cvičit na kousku podlahy.</p>'
          '<p>V kategorii najdete jednoduchá i dvojitá kolečka, široká kola s více koly vedle sebe, modely s gumovým popruhem nebo pružinou, která pomáhá při návratu, a sady 3v1 s rukojeťmi na kliky. Nabízejí je značky jako Spokey, Power System, Sedco, <a href="/znacka/insportline/">Insportline</a>, <a href="/znacka/merco/">Merco</a>, Sportago, <a href="/znacka/gymbeam/">GymBeam</a> nebo Lifefit. Ke každému kolečku uvidíte nabídky českých e-shopů. Další drobné vybavení na cvičení doma je v kategorii <a href="/fitness-pomucky/">fitness pomůcky</a>.</p>',
    guide='<h2>Co kolečko posiluje</h2>'
          '<p>Rollout patří mezi cviky, při kterých se trup nemá hýbat. Úkolem břicha je zabránit tomu, aby se při vzdalování rukou od těla bedra prohnula k zemi. Čím dál kolečko dojede, tím delší je páka a tím víc práce musí střed těla udělat. Pracuje přímý sval břišní, šikmé svaly, ramena a široký sval zádový, který kolečko přitahuje zpátky. Elektromyografická studie Escamilly a kolegů z roku 2006 řadila rollout na kolečkovém nářadí mezi cviky s nejvyšší aktivitou břišních svalů, srovnatelně s visem a přednožováním.</p>'
          '<p>Výsledek na postavě ale nezávisí na jednom cviku. Kolečko vám nespálí tuk z břicha, viditelnost svalů určuje hlavně celkové množství podkožního tuku. Berte ho jako jeden z cviků na sílu a stabilitu trupu, který se dobře kombinuje s prkny, visy na hrazdě nebo cviky s gumou.</p>'
          '<h2>Typy posilovacích koleček</h2>'
          + T(['Typ', 'Jak se chová', 'Pro koho'], [
              ['Jednoduché kolečko', 'úzké kolo, při jízdě se může naklánět do stran', 'pokročilejší, kdo chce víc zapojit šikmé svaly'],
              ['Dvojité kolečko', 'dvě kola vedle sebe, jede rovněji', 'začátečníci i většina rekreačních cvičenců'],
              ['Široké a vícekolové', 'tři nebo čtyři kola, široká stopa', 'kdo chce co nejstabilnější jízdu'],
              ['S pružinou nebo popruhem', 'mechanismus brzdí odjezd a pomáhá při návratu', 'začátečníci, kdo se rollout teprve učí'],
              ['Sady 3v1 a víc', 'kolečko, rukojeti na kliky, případně další doplňky', 'kdo chce víc cviků z jedné krabice']]) +
          '<p>Jednoduché kolečko s úzkou stopou je nejlevnější a nejméně stabilní. Při jízdě se kroutí, takže trup musí kromě prohnutí hlídat i rotaci. Dvojitá kolečka, například Spokey Tween, Power System Twin Core, Merco AB Double Wheel nebo HMS WA03, mají dvě kola na společné ose a jedou rovněji. Pro první měsíce jsou rozumnější volbou.</p>'
          '<p>Široká kolečka se třemi nebo čtyřmi koly, jako Merco AB Roller 3W, Sharp Shape AB Four Wheel nebo Lifefit FAT, mají ještě širší dosedací plochu. Na nerovné podlaze a na koberci se chovají klidněji, za to jsou objemnější.</p>'
          '<p>Kolečka s pomocným mechanismem mají buď pružinu uvnitř kola, nebo gumový popruh, který se zahákne a drží kolečko na uzdě. Decathlon prodává pod značkou Corength kolečko s odnímatelným elastickým popruhem a podložkou pod kolena. Popruh brzdí pohyb vpřed a pomáhá při cestě zpět, a když cvik zvládnete, sundáte ho. Stejná značka má i kolečko se dvěma režimy, stabilním a nestabilním, které se dá rozložit.</p>'
          '<p>Multifunkční sady kombinují kolečko s dalším nářadím. Insportline Pushabroll je podle výrobce kolečko, rukojeti na kliky a lahve, které poslouží jako lehké činky, v jednom. Některé sady GymBeam obsahují kolečko spolu s podložkou na cvičení a odporovými gumami. Taková sada dává smysl, když začínáte a nemáte doma nic.</p>'
          '<h2>Technika rolloutu z kleku</h2>'
          '<p>Všichni začínají z kleku. Rollout ze stoje je cvik pro velmi silné a zkušené cvičence a většina lidí ho nikdy nepotřebuje.</p>'
          '<ol><li>Klekněte si na podložku, kolena na šířku pánve. Kolečko položte na zem pod ramena a uchopte rukojeti.</li>'
          '<li>Zatněte hýždě a lehce podsaďte pánev, jako byste chtěli přitáhnout stydkou kost k pupíku. Bedra mají být rovná nebo mírně zakulacená, nikdy prohnutá.</li>'
          '<li>S výdechem nebo zadrženým dechem pomalu odvalujte kolečko vpřed. Boky jdou dopředu spolu s rameny, paže zůstávají propnuté.</li>'
          '<li>Jeďte jen tak daleko, dokud udržíte bedra v neutrální poloze. Jakmile cítíte, že se záda začínají propadat, zastavte.</li>'
          '<li>Přitáhněte kolečko zpět do výchozí polohy silou břicha a zad, ne vystrčením zadku dozadu.</li></ol>'
          '<p>Tempo volte pomalé, zhruba dvě až tři sekundy tam a stejně zpět. Rychlá jízda zvenku vypadá působivě, ale břicho při ní nestihne převzít práci a zátěž jde do beder a ramen. Hlavu držte v prodloužení páteře, pohled směřuje k zemi kousek před kolečko.</p>'
          '<h2>Progrese od začátečníka po rollout ze stoje</h2>'
          '<p>Postupujte po krocích. Další stupeň má smysl až tehdy, když předchozí zvládnete s čistou technikou na několik opakování v několika sériích.</p>'
          '<ol><li><strong>Prkno na předloktích a na dlaních.</strong> Naučí vás držet pánev podsazenou. Kdo nevydrží půl minuty v rovném prknu, ať s kolečkem ještě počká.</li>'
          '<li><strong>Krátký rollout z kleku ke zdi.</strong> Klekněte čelem ke zdi tak daleko, aby kolečko narazilo dřív, než ztratíte kontrolu. Zeď vás zastaví a postupně se od ní odsouváte.</li>'
          '<li><strong>Rollout z kleku s pomocí.</strong> Gumový popruh nebo pružina vás brzdí a pomůže zpět. Odporová guma připevněná ke kolečku a k pevnému bodu za vámi funguje podobně.</li>'
          '<li><strong>Plný rollout z kleku.</strong> Až do polohy, kdy jsou paže nad hlavou a tělo téměř u země, s rovnými bedry.</li>'
          '<li><strong>Rollout z kleku s pomalou fází zpět, se zastavením v krajní poloze, případně šikmo do stran.</strong></li>'
          '<li><strong>Rollout ze stoje.</strong> Začíná se ze stoje rozkročmo s kolečkem u nohou a zpočátku opět ke zdi nebo jen na krátkou vzdálenost.</li></ol>'
          '<p>Na začátek stačí dvě až tři série po několika opakováních dvakrát až třikrát týdně. Počet opakování přidávejte, teprve když technika zůstává čistá do posledního opakování. Břicho potřebuje odpočinek jako jiné svaly, každodenní série „do selhání“ jsou zbytečné.</p>'
          '<h2>Záda a bezpečnost</h2>'
          '<p>Nejčastější chybou je propadnutí beder v dlouhé poloze. Páteř se pak prohne a místo břicha drží tělo vazy a kloubní struktury bederní části. Pokud po cvičení cítíte bedra, a ne břicho, jeli jste moc daleko nebo moc rychle. Zkraťte rozsah a vraťte se o krok zpátky v progresi.</p>'
          '<p>Rollout výrazně zatěžuje také ramena, protože paže se dostávají nad hlavu. Kdo má omezený pohyb v ramenou nebo bolest při zvedání paží, ať začne s krátkým rozsahem. Zápěstí udržujte rovná, nezalamujte je dozadu.</p>'
          '<p>Kolečko není rehabilitační pomůcka a nikdo neslibuje, že bolest zad vyřeší. Kdo má bolesti zad, výhřez ploténky, je po operaci břicha, po porodu, těhotná nebo má diastázu břišních svalů, má se před cvičením poradit s lékařem nebo fyzioterapeutem. Ten nejlépe posoudí, zda je cvik vhodný a v jakém rozsahu. Při ostré nebo vystřelující bolesti cvičení hned ukončete.</p>'
          '<h2>Jak vybrat posilovací kolečko</h2>'
          '<p><strong>Šířka a počet kol.</strong> Čím širší stopa, tím stabilnější jízda. Na začátek doporučujeme dvojité nebo vícekolové kolečko, jednoduché úzké si nechte na později nebo jako druhou pomůcku.</p>'
          '<p><strong>Povrch kola.</strong> Kolo by mělo mít gumový nebo pryžový běhoun, který na podlaze tiše jede a neklouže. Tvrdý plast bez potahu na dlažbě hlučí a na plovoucí podlaze může zanechat stopy.</p>'
          '<p><strong>Rukojeti.</strong> Pěnové návleky jsou měkké, ale časem se mohou protočit nebo potrhat. Gumové rukojeti s drážkami drží v ruce pevněji. Dobré je, když osa nepruží a rukojeti se nevrtí. Vyzkoušejte, zda se do úchopu vejde celá dlaň.</p>'
          '<p><strong>Podložka pod kolena.</strong> Řada koleček se prodává s malou pěnovou podložkou, například Springos, Actiget nebo Corength. Pokud ji balení nemá, použijte složenou karimatku nebo podložku na cvičení. Kolena na tvrdé podlaze bolí a rozptýlí vás od techniky. Podložky najdete v kategorii <a href="/joga-a-podlozky/">jóga a podložky</a>.</p>'
          '<p><strong>Skladnost.</strong> Kolečka se zpravidla dají rozebrat na osu a rukojeti. Pokud cvičíte na cestách, hledejte model, který jde rozložit bez nářadí.</p>'
          '<p><strong>Pomocný mechanismus.</strong> Pružina nebo popruh má smysl hlavně na začátku. Až se rollout naučíte, kolečko bez pomoci dává víc práce, proto je lepší, když popruh jde sundat.</p>'
          '<h2>Na jaké podlaze cvičit</h2>'
          '<p>Nejlépe se jezdí po rovné a hladké podlaze: lino, parkety, vinyl nebo pevná gumová podlaha v posilovně. Na hustém koberci kolečko brzdí a jede trhaně. Na dlažbě s hlubokými spárami se kola zadrhávají. Pod kolena patří podložka, pod kolečko ne, měkká podložka by pohyb utlumila.</p>'
          '<h2>Další cviky s kolečkem</h2>'
          '<ul><li><strong>Rollout šikmo.</strong> Kolečko jede diagonálně vlevo a vpravo, víc pracují šikmé svaly.</li>'
          '<li><strong>Přitahování kolen v opoře.</strong> Nohy v kolečku s opěrkami pro chodidla nebo nárty, ruce na zemi. Hodí se jen kolečko, které na nohy výrobce určuje.</li>'
          '<li><strong>Pike.</strong> Ze stejné polohy zvedáte boky nahoru. Náročný cvik pro zkušené.</li>'
          '<li><strong>Kliky na kolečku.</strong> U sad 3v1 se rukojeti sundají a použijí jako opory na kliky.</li></ul>'
          '<p>Pokud chcete trénovat střed těla pestřeji, kombinujte kolečko s visem na <a href="/hrazdy-a-bradla/">hrazdě</a>, závěsným systémem <a href="/zavesne-systemy-trx/">TRX</a> nebo s <a href="/posilovaci-gumy/">posilovacími gumami</a>. Inspiraci, jak si doma sestavit trénink, najdete v článku <a href="/domaci-posilovna/">domácí posilovna</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Kolečko je jednoduchá pomůcka a údržbu skoro nepotřebuje. Běhoun občas otřete vlhkým hadříkem, prach a vlasy z podlahy se nabalují na gumu a kolečko pak hůř drží. Zkontrolujte, zda se osa neviklá a rukojeti pevně sedí. Pokud začne kolo drhnout nebo pískat, rozeberte ho a vyčistěte vnitřek. Prasklé nebo naštípnuté kolo nepoužívejte, při plné zátěži by mohlo povolit.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejné kolečko se v obchodech často prodává pod různými názvy, třeba jen jako „posilovací kolečko dvojité“ bez značky. Porovnávejte proto fotky, počet kol, materiál rukojetí a to, zda je v balení podložka. U sad zkontrolujte, co přesně obsahují. Na detailu produktu uvidíte nabídky jednotlivých e-shopů, nákup pak dokončíte přímo v obchodě.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Začít rolloutem ze stoje nebo hned plným rozsahem z kleku.</li>'
          '<li>Prohnutá bedra v krajní poloze. Rozsah určuje kontrola beder, ne ambice.</li>'
          '<li>Návrat vystrčením zadku dozadu místo přitažení břichem.</li>'
          '<li>Rychlé tempo, při kterém pracuje setrvačnost.</li>'
          '<li>Cvičení na holých kolenou na dlažbě.</li>'
          '<li>Přehlížení bolesti v zádech nebo ramenou. Bolest je signál přestat a poradit se s odborníkem.</li></ul>',
    faq=[
        ('Jaké posilovací kolečko vybrat pro začátečníka?', 'Dvojité nebo vícekolové s širokou stopou, ideálně s podložkou pod kolena. Pomůže i popruh nebo pružina, které brzdí jízdu vpřed.'),
        ('Je lepší jednoduché, nebo dvojité kolečko?', 'Dvojité jede rovněji a je stabilnější. Jednoduché se naklání do stran, víc zapojí šikmé svaly a hodí se pro pokročilé.'),
        ('Jak daleko mám kolečko odvalovat?', 'Jen tak daleko, dokud udržíte bedra rovná. Jakmile se začnou prohýbat k zemi, zastavte a vraťte se.'),
        ('Kolik opakování s kolečkem dělat?', 'Na začátek dvě až tři série po několika opakováních dvakrát až třikrát týdně. Přidávejte, až když technika vydrží.'),
        ('Bolí mě po kolečku záda, co dělám špatně?', 'Nejspíš jedete moc daleko nebo rychle a bedra se propadají. Zkraťte rozsah, a pokud bolest trvá, poraďte se s lékařem.'),
        ('Pomůže kolečko na bolavá záda?', 'Kolečko není rehabilitační pomůcka. S bolestmi zad nejprve navštivte lékaře nebo fyzioterapeuta, který cvičení doporučí.'),
        ('Spálím s kolečkem tuk na břiše?', 'Ne cíleně. Kolečko posiluje střed těla, ale viditelnost břišních svalů závisí na celkovém množství tuku v těle.'),
        ('K čemu je kolečko s pružinou nebo popruhem?', 'Mechanismus brzdí jízdu vpřed a pomáhá při návratu. Usnadní učení rolloutu, později se dá sundat.'),
        ('Můžu s kolečkem cvičit v těhotenství nebo po porodu?', 'Rollout silně zatěžuje břišní stěnu. V těhotenství, po porodu a při diastáze se vždy předem poraďte s lékařem.'),
        ('Na jaké podlaze se s kolečkem cvičí nejlépe?', 'Na rovné hladké podlaze, jako je lino, parkety nebo vinyl. Na hustém koberci kolečko brzdí, pod kolena dejte podložku.'),
    ])
