"""Guides wave 5d (2026-11-19): velikost-kola, jak-vybrat-detske-kolo, jak-vybrat-sjezdove-lyze, jak-vybrat-snowboard.

Demand (CZ / month): velikost kola 600, jak vybrat dětské kolo 80, druhy lyží 80, jak vybrat lyže 50,
délka lyží pro děti 50, jak vybrat snowboard 300.

Sources used for the facts:
- Bike frame size: cyclistshub.com "Bike Size Chart" (inseam factors: hybrid/trekking inseam x 0.685 = cm, MTB inseam
  x 0.225 = inches, road inseam x 0.665 = cm; road chart also used for cyclocross and gravel; height/inseam tables for
  MTB XS-2XL, road 48-62 cm, hybrid XS-XL; standover 1-2 inches of clearance; sizing varies by brand; between sizes:
  smaller = agile, larger = stable); other calculators (runbikecalc, bike-size.com, miniwebtool) give MTB 0.66 x inseam
  in cm and road factors between 0.665 and 0.70 - the article says the factors differ by source and are a start only.
- Kids bikes: woom.com "Find the right woom bike" and cyclesprog.co.uk woom guide (GO 1-3 = 12/14/16 inch, 20/24/26
  inch for the 4/5/6 models, woom 1 balance bike from 18 months, EXPLORE 6 26 inch for 140-165 cm, ages 10-14);
  emiliasport.fi / clevercycles kids bike guides (12 in 85-100 cm / inseam 35-42 cm, 14 in 95-110 / 40-48, 16 in
  105-120 / 44-55, 20 in 115-135 / 51-63, 24 in 130-145 / 60-73, 26 in 140+ / 70+); REI kids bike guide (both feet
  on the ground for beginners, inseam decides more than age). ISO 8098:2023 scope (saddle height 435-635 mm).
- Skis: evo "How to choose skis & ski size chart" (length between chin and top of the head, beginners shorter,
  experts longer, heavier skiers and off-piste longer, rocker may be sized up); gorhambike (beginner chin-upper lip,
  intermediate upper lip-eyebrows, advanced eyebrows-top of head); factionskis (start at nose to eyebrow); scheels
  (brands measure length differently); skrblik.cz (rule of thumb 10-15 cm shorter than height for men's piste skis,
  freeride about body height); recenzopedia.cz (kids' skis between chin and nose, beginners shorter); waist width
  bands from Backcountry/REI/evo/Oberson/Salomon via search (carving under ~85 mm, all-mountain ~85-105 mm, freeride
  ~100 mm and wider; cut-offs differ between sources). Bindings: ISO 11088 (replaced DIN 7881 in 1993; release value
  set from weight, height, age, skier type and boot sole length by a ski technician; ANSI blog).
- Snowboard: REI "How to choose a snowboard" (size by height, weight and riding style; camber for groomed and speed,
  hybrid camber/rocker, flat boards); twelveboardstore (weight before height, too short = unstable, too long =
  sluggish); snowandrock (length by height, weight and style); Sun and Ski (US men 10.5+ / women 11.5+ consider
  mid-wide or wide to avoid toe/heel drag); evo Burton charts (board length, waist width, rider weight, boot range;
  Custom Wide 158 = 258 mm waist); K2 / Ride / Salomon buying guides (softer, rocker or flat for beginners, stiffer
  holds more weight).
Left out because not verified: ISO 8098 brake requirements (two brakes / back-pedal), an exact bike-weight-to-child-
weight ratio, fixed turn radii for slalom and GS skis, FIS minimum lengths, a DIN table, exact snowboard waist widths
per boot size for every brand, a fixed mondopoint-to-width rule.
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- velikost-kola
MTB = T(['Výška jezdce', 'Vnitřní délka nohy', 'Velikost rámu MTB'], [
    ['145–155 cm', '69–73 cm', 'XS (asi 13–14″)'],
    ['155–165 cm', '74–78 cm', 'S (asi 15–16″)'],
    ['165–176 cm', '79–83 cm', 'M (asi 17–18″)'],
    ['177–188 cm', '84–89 cm', 'L (asi 19–20″)'],
    ['188–195 cm', '89–91 cm', 'XL (asi 21″)'],
    ['195–203 cm', '91–97 cm', 'XXL (22″ a víc)'],
])
ROAD = T(['Výška jezdce', 'Vnitřní délka nohy', 'Silniční / gravel rám'], [
    ['152–158 cm', '71–75 cm', '48 cm (XXS–XS)'],
    ['158–163 cm', '74–77 cm', '50 cm (XS)'],
    ['163–168 cm', '76–79 cm', '52 cm (S)'],
    ['168–174 cm', '78–82 cm', '54 cm (S–M)'],
    ['174–180 cm', '81–85 cm', '56 cm (M–L)'],
    ['180–185 cm', '84–87 cm', '58 cm (L)'],
    ['185–190 cm', '86–90 cm', '60 cm (XL)'],
    ['190–195 cm', '89–92 cm', '62 cm (XXL)'],
])
TREK = T(['Výška jezdce', 'Vnitřní délka nohy', 'Trekingové a městské kolo'], [
    ['147–155 cm', '69–73 cm', 'XS'],
    ['155–165 cm', '72–78 cm', 'S'],
    ['165–175 cm', '77–83 cm', 'M'],
    ['175–186 cm', '82–88 cm', 'L'],
    ['186–197 cm', '87–93 cm', 'XL'],
])
FORMULAS = T(['Typ kola', 'Výpočet z vnitřní délky nohy', 'Příklad pro nohu 80 cm'], [
    ['Horské kolo (MTB)', 'délka nohy v cm × 0,225 = rám v palcích', '18″, tedy obvykle M'],
    ['Silniční a gravel kolo', 'délka nohy v cm × 0,665 = rám v cm', '53,2 cm, tedy rám 52–54'],
    ['Trekingové, krosové, městské', 'délka nohy v cm × 0,685 = rám v cm', '54,8 cm (asi 21,5″)'],
])

GUIDES['velikost-kola'] = dict(
    name='Velikost kola',
    h1='Velikost kola: tabulka podle výšky a délky nohou',
    seo_title='Velikost kola: tabulka podle výšky a délky nohou (MTB, silnice)',
    seo_desc='Jak zjistit velikost rámu kola: tabulky pro horská, silniční, gravel a trekingová kola podle výšky, výpočet z délky nohou a kontrola rozkroku.',
    intro_html=(
        '<p><strong>Jakou velikost kola potřebujete?</strong> Hrubý odhad dá výška: kdo měří 165–176 cm, jezdí na horském kole většinou velikost M (asi 17–18″), '
        'na silničním kole rám kolem 54 cm. Přesnější je změřit vnitřní délku nohy (od podlahy do rozkroku) a vynásobit ji koeficientem pro daný typ kola. '
        'Pro horské kolo délka nohy v centimetrech × 0,225 dá velikost rámu v palcích, pro silniční kolo × 0,665 v centimetrech, pro trekingové × 0,685.</p>'
        '<p>Tabulky i výpočty jsou jen vodítko. Každý výrobce měří rám trochu jinak a moderní horská kola mají geometrii, u které čísla v palcích skoro nic neříkají. '
        'Proto v článku ukážeme, jak správně změřit nohu, kdy zvolit menší a kdy větší rám, co je standover a jak ověřit velikost na konkrétním kole v obchodě.</p>'
        '<p>Sporteka sama nic neprodává, srovnává nabídky českých e-shopů. Pod jednotlivými částmi proto najdete kola, která se v obchodech právě nabízejí.</p>'
    ),
    sections=[
        dict(h2='Jak změřit vnitřní délku nohy',
             html=(
                 '<p>Vnitřní délka nohy (anglicky inseam) je pro velikost kola užitečnější než výška. Dva lidé se stejnou výškou mohou mít nohy dlouhé o několik centimetrů jinak. Postup:</p>'
                 '<ol><li>Zujte se a postavte se zády ke stěně, chodidla mějte zhruba 15–20 cm od sebe, jako když stojíte nad rámem.</li>'
                 '<li>Vezměte tvrdou knihu nebo vodováhu a vsuňte ji mezi nohy hřbetem nahoru. Zvedněte ji do rozkroku tak, jak by tlačilo sedlo.</li>'
                 '<li>Knihu držte vodorovně a druhá osoba udělá na stěně tužkou značku u horní hrany.</li>'
                 '<li>Svinovacím metrem změřte vzdálenost od podlahy ke značce. To je vaše vnitřní délka nohy.</li>'
                 '<li>Měření zopakujte dvakrát nebo třikrát a vezměte průměr.</li></ol>'
                 '<p>Číslo na kalhotách nepoužívejte, střih a sed se mezi značkami liší. Vnitřní délka nohy se hodí i pro nastavení výšky sedla, takže si ji poznamenejte.</p>'
             )),
        dict(h2='Výpočet velikosti rámu z délky nohy',
             html=(
                 '<p>Z délky nohy se velikost rámu spočítá jednoduchým násobením. Koeficienty se mezi zdroji trochu liší, některé kalkulačky počítají silniční kolo s 0,67 nebo 0,70, horské s 0,66 v centimetrech. '
                 'Rozdíl dělá jednu velikost, proto výsledek berte jako výchozí bod, ne jako konečné číslo.</p>'
                 + FORMULAS +
                 '<p>Výsledek zaokrouhlete na nejbližší velikost, kterou výrobce nabízí. Když vyjde přesně mezi dvěma velikostmi, rozhodne styl jízdy a délka trupu (viz část o volbě mezi velikostmi). '
                 'Velikost rámu v centimetrech nebo palcích je u většiny výrobců délka sedlové trubky. Ta se ale měří od středu osy pedálů k hornímu okraji trubky nebo ke středu horní trubky, podle zvyklosti značky.</p>'
             )),
        dict(h2='Horská kola: tabulka velikostí',
             html=(
                 '<p>Horská kola se dřív značila v palcích, dnes většina výrobců uvádí písmena S, M, L a XL. Následující tabulka je orientační přehled podle výšky a délky nohy:</p>'
                 + MTB +
                 '<p>U moderních trailových a enduro kol rozhoduje víc než sedlová trubka parametr <strong>reach</strong>, tedy vodorovná vzdálenost od středu osy pedálů ke hlavové trubce. '
                 'Dvě kola velikosti L od různých značek mohou mít reach rozdílný i o 2–3 cm. Při porovnání proto otevřete tabulku geometrie výrobce. '
                 'Menší rámy často jezdí na kolech 27,5″, větší na 29″. Některé značky dávají 27,5″ jen do velikostí XS a S.</p>'
                 '<p>Přehled nabídky najdete v kategorii <a href="/horska-kola/">horská kola</a>, plně odpružené modely v kategorii <a href="/celoodpruzena-horska-kola/">celoodpružená horská kola</a>.</p>'
             ), cat='horska-kola', n=4),
        dict(h2='Silniční a gravel kola: tabulka velikostí',
             html=(
                 '<p>Silniční rámy se tradičně udávají v centimetrech. Stejnou tabulku lze použít pro gravel a cyklokros, jejich geometrie vychází ze silničních kol.</p>'
                 + ROAD +
                 '<p>U silničních kol víc záleží na délce trupu a rukou. Výrobci k velikosti uvádějí <strong>stack</strong> (výška řídítek nad osou pedálů) a <strong>reach</strong>. '
                 'Endurance a gravel rámy mají vyšší stack a kratší reach, sedí se na nich vzpřímeněji. Závodní rámy jsou nižší a delší. '
                 'Kdo má ztuhlá záda nebo jezdí dlouhé vyjížďky, bývá spokojenější s vyšším stackem než s menším rámem.</p>'
                 '<p>Nabídku najdete v kategoriích <a href="/silnicni-kola/">silniční kola</a> a <a href="/gravel-kola/">gravel kola</a>.</p>'
             ), cat='silnicni-kola', n=4),
        dict(h2='Trekingová, krosová a městská kola',
             html=(
                 '<p>Trekingová a městská kola mají vzpřímenější posez a často šikmou nebo sníženou horní trubku. Velikosti se značí písmeny, palci i centimetry, podle výrobce.</p>'
                 + TREK +
                 '<p>U kol s nízkým nástupem (dámské rámy, city kola) neřešíte standover, protože horní trubka je nízko. Rozhoduje hlavně vzdálenost k řídítkům a výška sedla. '
                 'Když výrobce udává velikost v centimetrech a vy znáte palce, vydělte centimetry číslem 2,54. Rám 53 cm tedy odpovídá zhruba 21″.</p>'
                 '<p>Trekingová kola najdete v kategorii <a href="/trekingova-kola/">trekingová kola</a>, další modely v kategoriích <a href="/krosova-kola/">krosová kola</a> a <a href="/mestska-kola/">městská kola</a>.</p>'
             ), cat='trekingova-kola', n=4),
        dict(h2='Standover: kontrola nad horní trubkou',
             html=(
                 '<p><strong>Standover</strong> je výška horní trubky nad zemí v místě, kde nad kolem stojíte. Když se postavíte nad rám obkročmo s oběma chodidly na zemi, '
                 'mezi rozkrokem a trubkou by mělo zůstat zhruba 2,5–5 cm místa. U horských kol, kde se často sesedá v terénu, raději víc.</p>'
                 '<p>Když je vaše vnitřní délka nohy kratší než standover kola, je kolo příliš velké. Při prudkém zastavení byste dopadli rozkrokem na trubku. '
                 'Výrobci standover uvádějí v tabulce geometrie, takže ho lze porovnat i bez zkoušení.</p>'
                 '<p>Pozor: dobrý standover ještě neznamená správnou velikost. Moderní rámy mají horní trubku hodně skloněnou, takže se nad ně postaví i menší jezdec, a přesto může být kolo dlouhé.</p>'
             )),
        dict(h2='Mezi dvěma velikostmi: menší, nebo větší rám?',
             html=(
                 '<p>Pokud výpočet vyjde mezi dvěma velikostmi, zvažte:</p>'
                 '<ul><li><strong>Menší rám</strong> je obratnější, snáz se s ním manévruje v technickém terénu a lépe se ovládá na singletracku. Vyhovuje kratšímu trupu a jezdcům, kteří chtějí hravé kolo.</li>'
                 '<li><strong>Větší rám</strong> je stabilnější v rychlosti a na dlouhých tratích, nabízí víc místa v kokpitu. Hodí se pro delší trup a ruce.</li>'
                 '<li><strong>Proporce těla:</strong> kdo má dlouhé nohy a krátký trup, volí spíš menší rám s vyšší sedlovkou. Kdo má krátké nohy a dlouhý trup, spíš větší rám.</li></ul>'
                 '<p>Drobné rozdíly doladíte představcem (o 1–2 cm kratším nebo delším), posunem sedla na sedlovce a výškou řídítek. Rám, který je o dvě velikosti mimo, už ale žádná úprava nezachrání.</p>'
             )),
        dict(h2='Nastavení sedla a zkouška na kole',
             html=(
                 '<p>Po výběru velikosti nastavte výšku sedla. Orientační postup: sedněte na kolo, patu postavte na pedál v dolní poloze. Noha má být téměř propnutá. '
                 'Při běžném šlapání přes přední část chodidla pak zůstane koleno mírně pokrčené. Boky se při šlapání nemají kývat ze strany na stranu.</p>'
                 '<ol><li>Při zkušební jízdě sledujte, jestli dosáhnete pohodlně na řídítka bez propnutých loktů.</li>'
                 '<li>Zkontrolujte, že při zatáčení koleno nenaráží do řídítek.</li>'
                 '<li>Ujeďte aspoň pár set metrů, ideálně i do kopce a ze sedla.</li>'
                 '<li>U kola z e-shopu si uložte tabulku geometrie a porovnejte ji se svým starým kolem, na kterém se vám jezdí dobře.</li></ol>'
                 '<p>Při objednávce online si ověřte podmínky vrácení. Kolo musí zůstat nepoužité, takže zkoušejte jen doma nebo na krátké vzdálenosti. '
                 'Na kolo patří i správně padnoucí přilba, výběr najdete v kategorii <a href="/cyklisticke-helmy/">cyklistické helmy</a>.</p>'
             ), cat='cyklisticke-helmy', n=4),
        dict(h2='Časté chyby při výběru velikosti',
             html=(
                 '<ul><li><strong>Kupovat podle výšky kamaráda.</strong> Stejná výška neznamená stejnou délku nohou a trupu.</li>'
                 '<li><strong>Porovnávat palce u různých značek.</strong> Rám 19″ jedné značky může odpovídat rámu 18″ jiné. Srovnávejte raději reach, stack a standover.</li>'
                 '<li><strong>Brát větší kolo „do zásoby“.</strong> U dospělých to nedává smysl a u dětí je to nebezpečné.</li>'
                 '<li><strong>Řešit velikost jen sedlovkou.</strong> Vysoko vytažená sedlovka s nízkými řídítky znamená přetížená záda a ruce.</li>'
                 '<li><strong>Zapomenout na elektrokolo.</strong> U <a href="/elektrokola/">elektrokol</a> platí stejné tabulky, kolo je ale těžší a hůř se s ním manipuluje, takže na standoveru záleží víc.</li></ul>'
                 '<p>Při srovnání nabídek se vyplatí hledat přesný model a ročník, protože geometrie se mezi ročníky mění.</p>'
             ), cat='elektrokola', n=4),
    ],
    faq=[
        ('Jakou velikost kola potřebuji při výšce 180 cm?',
         '<p>Orientačně na horském kole velikost L (asi 19–20″), na silničním nebo gravel kole rám 56–58 cm, na trekingovém L. Přesnější odhad dá vnitřní délka nohy a tabulka geometrie výrobce.</p>'),
        ('Jakou velikost kola potřebuji při výšce 170 cm?',
         '<p>Nejčastěji velikost M na horském kole (17–18″), rám 54 cm na silničním a M na trekingovém. Při kratších nohách může vyjít o velikost menší.</p>'),
        ('Jak se počítá velikost rámu z délky nohy?',
         '<p>Vnitřní délku nohy v centimetrech vynásobte koeficientem: horské kolo 0,225 (výsledek v palcích), silniční 0,665 (v cm), trekingové 0,685 (v cm). Koeficienty se mezi zdroji liší, berte je jako odhad.</p>'),
        ('Jak převést velikost rámu z centimetrů na palce?',
         '<p>Centimetry vydělte číslem 2,54. Rám 46 cm odpovídá asi 18″, rám 53 cm asi 21″.</p>'),
        ('Co je standover a kolik místa má zůstat?',
         '<p>Standover je výška horní trubky nad zemí. Když stojíte nad rámem, mělo by mezi rozkrokem a trubkou zůstat zhruba 2,5–5 cm, u horských kol raději víc.</p>'),
        ('Je lepší menší, nebo větší rám?',
         '<p>Menší rám je obratnější, větší stabilnější a prostornější. Při délce mezi velikostmi rozhoduje délka trupu, styl jízdy a geometrie konkrétního modelu.</p>'),
        ('Proč se velikosti mezi značkami liší?',
         '<p>Každý výrobce měří sedlovou trubku jinak a má jinou geometrii. Proto je lepší porovnávat reach, stack a standover než číslo v palcích.</p>'),
        ('Platí stejné tabulky pro elektrokola?',
         '<p>Ano, velikost elektrokola se volí podobně jako u běžného kola stejného typu. Kvůli vyšší hmotnosti se vyplatí mít dost místa nad horní trubkou.</p>'),
        ('Jak zjistím velikost kola pro dítě?',
         '<p>U dětí se neřídí velikostí rámu, ale průměrem kol v palcích (12″ až 26″). Postup popisujeme v článku <a href="/jak-vybrat-detske-kolo/">jak vybrat dětské kolo</a>.</p>'),
    ],
    cats=['jizdni-kola', 'horska-kola', 'silnicni-kola', 'gravel-kola', 'trekingova-kola', 'krosova-kola', 'mestska-kola', 'silnicni-a-gravel-kola'],
    updated='2026-11-19')

# ---------------------------------------------------------------- jak-vybrat-detske-kolo
KIDS = T(['Kola', 'Výška dítěte', 'Vnitřní délka nohy', 'Orientační věk'], [
    ['Odrážedlo', 'asi od 80 cm', 'od asi 26–30 cm', 'od 1,5–2 let'],
    ['12″', '85–100 cm', '35–42 cm', '2,5–4 roky'],
    ['14″', '95–110 cm', '40–48 cm', '3–5 let'],
    ['16″', '105–120 cm', '44–55 cm', '4–6 let'],
    ['20″', '115–135 cm', '51–63 cm', '6–9 let'],
    ['24″', '130–145 cm', '60–73 cm', '8–11 let'],
    ['26″', 'od 140 cm', 'od 70 cm', 'od 10 let'],
])

GUIDES['jak-vybrat-detske-kolo'] = dict(
    name='Jak vybrat dětské kolo',
    h1='Jak vybrat dětské kolo: velikost kol podle výšky a věku',
    seo_title='Jak vybrat dětské kolo: velikost podle výšky a věku (tabulka)',
    seo_desc='Dětské kolo 12″ až 26″: tabulka velikostí podle výšky a délky nohy, kdy odrážedlo, jaké brzdy a proč na hmotnosti kola záleží víc než u dospělých.',
    intro_html=(
        '<p><strong>Jak vybrat dětské kolo?</strong> Velikost dětského kola se udává průměrem kol v palcích, od 12″ pro nejmenší až po 26″ pro školáky kolem 140 cm. '
        'Rozhoduje výška dítěte a hlavně vnitřní délka nohy, ne věk. Orientačně: 12″ pro děti 85–100 cm, 14″ pro 95–110 cm, 16″ pro 105–120 cm, '
        '20″ pro 115–135 cm a 24″ pro 130–145 cm. Začínající dítě by mělo ze sedla dosáhnout na zem oběma chodidly.</p>'
        '<p>Druhou věcí, na které záleží, je hmotnost kola. Dítě s 18 kg na těžkém kole kolem 10 kg veze víc než polovinu své váhy. '
        'Dále probereme odrážedla, brzdy, převody, odpružení i nejčastější chybu: kupovat kolo „na vyrůstání“.</p>'
        '<p>Sporteka nic neprodává, srovnává nabídky českých e-shopů. Pod částmi článku najdete dětská kola a odrážedla z nabídky obchodů.</p>'
    ),
    sections=[
        dict(h2='Tabulka velikostí dětských kol',
             html=(
                 '<p>Rozsahy se mezi výrobci liší o několik centimetrů, proto je tabulka jen vodítko. Překrývání je běžné: dítě o výšce 110 cm může jezdit na 14″ i 16″ kole podle délky nohou a zkušenosti.</p>'
                 + KIDS +
                 '<p>Například rakouská značka woom řadí modely tak, že GO 1 až GO 3 mají kola 12″, 14″ a 16″, další modely 20″, 24″ a 26″. Jejich 26″ kolo je určené dětem zhruba od 140 do 165 cm. '
                 'U jiných značek se ale rozsahy posouvají, takže vždy otevřete tabulku konkrétního výrobce.</p>'
                 '<p>Nabídku najdete v kategorii <a href="/detska-kola/">dětská kola</a>, po velikostech v kategoriích <a href="/detska-kola-12-14-palcu/">12–14″</a>, '
                 '<a href="/detska-kola-16-palcu/">16″</a>, <a href="/detska-kola-20-palcu/">20″</a> a <a href="/detska-kola-24-palcu/">24″</a>.</p>'
             ), cat='detska-kola', n=4),
        dict(h2='Jak dítěti změřit nohu a vyzkoušet kolo',
             html=(
                 '<ol><li>Dítě se postaví bosé ke zdi, nohy mírně od sebe.</li>'
                 '<li>Mezi nohy vsuňte knihu hřbetem nahoru a zlehka ji přitlačte do rozkroku.</li>'
                 '<li>Změřte vzdálenost od podlahy k horní hraně knihy.</li>'
                 '<li>Porovnejte ji s minimální a maximální výškou sedla, kterou výrobce u kola uvádí.</li></ol>'
                 '<p>U úplných začátečníků má být nejnižší výška sedla stejná nebo o pár centimetrů nižší než vnitřní délka nohy. Dítě pak stojí na zemi celými chodidly a nebojí se. '
                 'Zkušenější jezdec, který umí rozjíždět a brzdit, může mít sedlo výš a na zem dosáhne jen špičkami.</p>'
                 '<p>Při zkoušce sledujte, jestli dítě dosáhne pohodlně na řídítka, neopírá se koleny o řídítka a zvládne zmáčknout brzdové páky. Na tom posledním padá mnoho levných kol.</p>'
             )),
        dict(h2='Odrážedlo: první krok před šlapáním',
             html=(
                 '<p>Odrážedlo je kolo bez pedálů. Dítě se odráží nohama a učí se rovnováhu, kterou na šlapacím kole potřebuje nejvíc. '
                 'Mnoho dětí, které začínaly na odrážedle, později přejde rovnou na kolo bez přídavných koleček.</p>'
                 '<ul><li><strong>Věk:</strong> zpravidla od 1,5 do 2 let, podle výšky a vnitřní délky nohy. Výrobci uvádějí minimální výšku sedla, u nejmenších modelů kolem 26–30 cm.</li>'
                 '<li><strong>Hmotnost:</strong> čím lehčí, tím lépe, dítě ho musí zvednout a otočit.</li>'
                 '<li><strong>Pneumatiky:</strong> nafukovací lépe tlumí a drží, pěnové (EVA) nepíchnou, ale kloužou na mokru.</li>'
                 '<li><strong>Brzda:</strong> u starších dětí se hodí ruční brzda zadního kola, ať si zvykají brzdit rukou.</li>'
                 '<li><strong>Omezení řízení:</strong> některá odrážedla mají doraz, aby se řídítka nepřetočila. Pro začátek dobré, později spíš překáží.</li></ul>'
                 '<p>Výběr najdete v kategorii <a href="/odrazedla/">odrážedla</a>. Pro nejmenší, kteří ještě nechodí jistě, existují také <a href="/detske-trikolky/">dětské tříkolky</a>.</p>'
             ), cat='odrazedla', n=4),
        dict(h2='Hmotnost kola: proč na ní záleží',
             html=(
                 '<p>Dospělý na kole o 2 kg těžším skoro nic nepozná. Dítě ano, protože kolo tvoří mnohem větší část jeho hmotnosti. Těžké kolo se hůř rozjíždí, hůř se s ním zatáčí, hůř brzdí a dítě ho nevytlačí do kopce.</p>'
                 '<ul><li>Hliníkový rám je obvykle lehčí než ocelový.</li>'
                 '<li>Odpružená vidlice na 16″ nebo 20″ kole přidá váhu a u levných modelů skoro nefunguje, protože dítě je na ni příliš lehké.</li>'
                 '<li>Blatníky, nosič, stojánek a kryt řetězu jsou praktické, ale každý díl něco váží.</li>'
                 '<li>Široké pneumatiky s hrubým vzorkem jsou pomalejší na asfaltu.</li></ul>'
                 '<p>Hmotnost bez pedálů najdete v parametrech u většiny značkových kol. Když ji e-shop neuvádí, hledejte ji na webu výrobce.</p>'
             )),
        dict(h2='Brzdy na dětském kole',
             html=(
                 '<p>Na malých dětských kolech se potkáte se třemi řešeními:</p>'
                 '<ul><li><strong>Brzda v náboji ovládaná šlapáním dozadu</strong> (torpédo). Je jednoduchá, ale dítě nemůže pedál otočit dozadu, aby si ho nastavilo pro rozjezd. Při náhlém zastavení navíc často šlápne špatně.</li>'
                 '<li><strong>Ráfkové brzdy V</strong> ovládané rukou. Lehké a dobře seřiditelné, pokud mají páky s krátkým dosahem pro malou dlaň.</li>'
                 '<li><strong>Kotoučové brzdy</strong> na větších 20″ až 26″ kolech. Mají sílu i na mokru, ale přidávají hmotnost a potřebují jemné dávkování.</li></ul>'
                 '<p>Kontrolujte, jestli dítě dosáhne prsty na páky a zvládne je zmáčknout tak, aby se kolo zastavilo. Většina pák má šroubek pro nastavení vzdálenosti od řídítek. '
                 'Dítě, které přechází z odrážedla s ruční brzdou, obvykle zvládá ruční brzdy rychle.</p>'
             )),
        dict(h2='Převody, odpružení a další výbava',
             html=(
                 '<p>Kola 12″ až 16″ mají obvykle jeden převod. Kola 20″ a větší už většinou nabízejí přehazovačku s několika rychlostmi. '
                 'Pro začátek stačí jeden převodník vpředu a 6–8 rychlostí vzadu, ovládání otočnou rukojetí nebo malou páčkou.</p>'
                 '<p>Odpružení dává smysl až u 24″ a 26″ kol pro děti, které jezdí v terénu, a jen když je vidlice nastavitelná na nízkou hmotnost. Jinak jsou lepší pevná vidlice a širší pneumatika.</p>'
                 '<p>Přídavná kolečka dítě sice udrží, ale nenaučí ho rovnováhu. Pokud dítě jezdilo na odrážedle, většinou je nepotřebuje. '
                 'Na kole nesmí chybět přilba, kterou najdete v kategorii <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</p>'
             ), cat='detske-cyklohelmy', n=4),
        dict(h2='Kolo „na vyrůstání“: proč to nefunguje',
             html=(
                 '<p>Rodiče často kupují kolo o velikost větší, aby vydrželo déle. Dítě pak na zem nedosáhne, nezvládne rozjezd, brzdí špatně a kolo ho nebaví. Hrozí pád a ztráta chuti jezdit.</p>'
                 '<p>Lepší je kolo, které sedí teď a má široký rozsah výšky sedla a řídítek. Dobře udržovaná dětská kola se také dají prodat dál, takže rozdíl v ceně se částečně vrátí. '
                 'Kolo menší velikosti se dá na rok či dva protáhnout delší sedlovkou, pokud ji výrobce dodává.</p>'
             )),
        dict(h2='Rám, geometrie a pneumatiky',
             html=(
                 '<p>Na dětském kole záleží na detailech, které na fotce nejsou vidět. <strong>Nízký nástup</strong> (snížená horní trubka) usnadní nasedání a seskakování, hlavně u 12″ až 20″ kol. '
                 'Dlouhý rozvor a nízko položený střed kola dodají stabilitu, takže se dítě méně kymácí. Úzká řídítka s malými gripy sedí dětské dlani lépe než zkrácená řídítka pro dospělé.</p>'
                 '<p><strong>Kliky</strong> mají být úměrné délce nohou. Na levných kolech se často montují příliš dlouhé, takže dítě šlape s koleny až u brady. '
                 '<strong>Pneumatiky</strong> volte podle terénu: hladší a užší na chodník a asfalt, širší s hrubším vzorkem na lesní cesty. Nafukujte podle tlaku uvedeného na boku pláště, podhuštěná pneumatika kolo zbytečně brzdí.</p>'
                 '<p>Kolo pro dívky a chlapce se liší jen barvou a tvarem rámu, velikost a výbava jsou stejné. Rozhodujte proto podle funkce, dekor je až poslední.</p>'
             )),
        dict(h2='Bezpečnost a údržba dětského kola',
             html=(
                 '<ul><li>Před každou jízdou zkontrolujte brzdy, tlak v pneumatikách a dotažení řídítek a sedla.</li>'
                 '<li>Řetěz čas od času otřete a namažte, u kol s krytem řetězu stačí méně často.</li>'
                 '<li>Výšku sedla upravte zhruba každé půl roku, děti rostou rychleji, než se zdá.</li>'
                 '<li>Na silnici patří světla a odrazky, za šera i reflexní vesta.</li></ul>'
                 '<p>Přilba musí sedět rovně na čele a neposouvat se, když dítě zavrtí hlavou. Podle zákona o silničním provozu musí mít přilbu při jízdě na pozemní komunikaci cyklisté mladší 18 let.</p>'
             )),
        dict(h2='Postup výběru krok za krokem',
             html=(
                 '<ol><li>Změřte dítěti výšku a vnitřní délku nohy.</li>'
                 '<li>Podle tabulky zvolte průměr kol, při hraniční výšce rozhoduje zkušenost dítěte.</li>'
                 '<li>Porovnejte minimální výšku sedla s délkou nohy.</li>'
                 '<li>Zkontrolujte hmotnost kola a typ brzd.</li>'
                 '<li>U větších kol zvažte převody a jen kvalitní odpružení.</li>'
                 '<li>Přidejte přilbu, případně chrániče, zvonek a světla.</li></ol>'
                 '<p>Pro starší děti a pro jízdu po městě se hodí i <a href="/kolobezky/">koloběžky</a>, které jsou lehčí a snáz se přenášejí. '
                 'Kdy už dítě přejde na kolo velikosti pro dospělé, popisuje článek <a href="/velikost-kola/">velikost kola podle výšky</a>.</p>'
             )),
    ],
    faq=[
        ('Jaké kolo pro dítě, které měří 110 cm?',
         '<p>Nejčastěji 16″, u menších nebo začínajících dětí 14″. Rozhoduje vnitřní délka nohy, která by měla odpovídat nejnižší výšce sedla.</p>'),
        ('Jaké kolo pro 6leté dítě?',
         '<p>Šestileté děti jezdí obvykle na 16″ nebo 20″ kole. Věk je ale jen orientační, rozhodují výška a délka nohou.</p>'),
        ('Od kolika let je 20palcové kolo?',
         '<p>Orientačně od 6 let, při výšce od zhruba 115–120 cm a vnitřní délce nohy kolem 51 cm a víc.</p>'),
        ('Od kolika let je 24palcové kolo?',
         '<p>Zhruba od 8 let, pro děti mezi 130 a 145 cm. Některé modely se hodí i pro menší dospělé.</p>'),
        ('Kdy koupit odrážedlo?',
         '<p>Obvykle mezi 1,5 a 2 lety, jakmile dítě jistě chodí a dosáhne na zem ze sedla v nejnižší poloze.</p>'),
        ('Má mít dětské kolo brzdu šlapáním dozadu?',
         '<p>Nemusí. Mnoho lehkých dětských kol má jen dvě ruční brzdy. Důležité je, aby dítě dosáhlo na páky a umělo je zmáčknout.</p>'),
        ('Kolik má dětské kolo vážit?',
         '<p>Co nejméně. Pevné číslo neexistuje, ale lehké hliníkové kolo bez odpružení je pro dítě výrazně snazší než těžký ocelový model.</p>'),
        ('Potřebuje dětské kolo odpruženou vidlici?',
         '<p>Na 12″ až 20″ kolech většinou ne. Levné vidlice jsou na lehké dítě příliš tuhé a jen přidávají váhu.</p>'),
        ('Mám koupit kolo o velikost větší?',
         '<p>Ne. Dítě na velkém kole nedosáhne na zem a hůř brzdí. Lepší je správná velikost s rezervou v nastavení sedla.</p>'),
        ('Potřebuje dítě přídavná kolečka?',
         '<p>Po odrážedle obvykle ne. Kolečka učí opírat se do strany, místo aby dítě udrželo rovnováhu.</p>'),
    ],
    cats=['detska-kola', 'odrazedla', 'detska-kola-12-14-palcu', 'detska-kola-16-palcu', 'detska-kola-20-palcu', 'detska-kola-24-palcu', 'detske-cyklohelmy'],
    updated='2026-11-19')

# ---------------------------------------------------------------- jak-vybrat-sjezdove-lyze
SKI_TYPES = T(['Typ lyží', 'Šířka pod vázáním', 'Kde jezdí', 'Pro koho'], [
    ['Sjezdovkové (on-piste, carving)', 'zhruba do 85 mm', 'upravené sjezdovky', 'začátečníci až pokročilí'],
    ['Slalomky (SL)', 'úzké, kolem 65–70 mm', 'krátké oblouky na tvrdé sjezdovce', 'technicky zdatní'],
    ['Obřačky (GS)', 'úzké', 'dlouhé rychlé oblouky', 'pokročilí a závodníci'],
    ['All-mountain', 'zhruba 85–105 mm', 'sjezdovka i prašan mimo ni', 'všestranní lyžaři'],
    ['Freeride', 'od zhruba 100 mm', 'hluboký sníh, volný terén', 'zkušení, mimo sjezdovky'],
    ['Freestyle (twin tip)', 'různá', 'snowpark, jízda pozadu', 'parkoví jezdci'],
])
SKI_LEN = T(['Úroveň', 'Kam má lyže sahat', 'Příklad pro výšku 175 cm'], [
    ['Začátečník', 'mezi bradu a horní ret', 'asi 150–160 cm'],
    ['Středně pokročilý', 'mezi horní ret a obočí', 'asi 160–170 cm'],
    ['Pokročilý a expert', 'od obočí po temeno hlavy', 'asi 165–175 cm'],
    ['Freeride', 'kolem výšky lyžaře i víc', 'asi 175–185 cm'],
])

GUIDES['jak-vybrat-sjezdove-lyze'] = dict(
    name='Jak vybrat sjezdové lyže',
    h1='Jak vybrat sjezdové lyže: délka, typy a tvrdost',
    seo_title='Jak vybrat sjezdové lyže: délka, druhy lyží a tvrdost',
    seo_desc='Druhy sjezdových lyží, délka podle výšky a úrovně, dětské lyže, rocker a camber, tvrdost a vázání. Tabulky a postup výběru pro začátečníky i pokročilé.',
    intro_html=(
        '<p><strong>Jak vybrat lyže?</strong> Nejdřív podle toho, kde budete jezdit: na upravené sjezdovce stačí užší sjezdovkové (carvingové) lyže, '
        'kdo jezdí i mimo ni, sáhne po all-mountain nebo freeride. Délku pak určuje výška a úroveň. Začátečníkovi mají lyže sahat zhruba mezi bradu a horní ret, '
        'středně pokročilému k nosu až obočí, pokročilému od obočí po temeno. Těžší lyžaři a rychlá jízda posouvají délku nahoru.</p>'
        '<p>V článku projdeme druhy lyží, tabulku délek, dětské lyže, profil (camber a rocker), tvrdost i to, proč se vázání nastavuje v servisu. '
        'Na konci najdete nejčastější chyby při nákupu.</p>'
        '<p>Sporteka nic neprodává, srovnává nabídky českých e-shopů. Pod částmi článku uvidíte lyže, boty a další výbavu, které obchody nabízejí.</p>'
    ),
    sections=[
        dict(h2='Druhy sjezdových lyží',
             html=(
                 '<p>Lyže se dělí podle terénu, pro který jsou stavěné. Nejlepší vodítko je šířka pod vázáním: čím užší, tím rychleji přechází z hrany na hranu na tvrdém sněhu, '
                 'čím širší, tím lépe nese v měkkém a hlubokém sněhu. Hranice mezi kategoriemi se u výrobců liší, takže čísla v tabulce berte zhruba.</p>'
                 + SKI_TYPES +
                 '<p>Většina rekreačních lyžařů v Česku a v Alpách jezdí po upravených sjezdovkách. Pro ně jsou nejvhodnější sjezdovkové lyže nebo užší all-mountain. '
                 'Široké freeridové lyže na tvrdé sjezdovce zbytečně unavují kolena a hůř drží hranu.</p>'
                 '<p>Přehled nabídky najdete v kategorii <a href="/sjezdove-lyze/">sjezdové lyže</a>, vybrané značky třeba na stránkách <a href="/rossignol-lyze/">lyže Rossignol</a> nebo <a href="/head-lyze/">lyže Head</a>.</p>'
             ), cat='sjezdove-lyze', n=4),
        dict(h2='Délka lyží podle výšky a úrovně',
             html=(
                 '<p>Správná délka sjezdových lyží leží obvykle mezi bradou a temenem hlavy. Pro muže na sjezdovku se v Česku často uvádí orientačně o 10–15 cm méně, než měří. Kde přesně v tom rozsahu skončíte, rozhodnou úroveň, hmotnost a styl:</p>'
                 + SKI_LEN +
                 '<ul><li><strong>Kratší lyže</strong> se snáz točí a odpouštějí chyby. Hodí se pro začátečníky, lehčí lyžaře a krátké oblouky.</li>'
                 '<li><strong>Delší lyže</strong> jsou stabilnější v rychlosti a v nerovném sněhu. Vyberte je při vyšší hmotnosti, rychlé jízdě nebo jízdě mimo sjezdovku.</li>'
                 '<li><strong>Lyže s rockerem</strong> mají kratší kontaktní délku, proto se často berou o něco delší.</li></ul>'
                 '<p>Pozor na to, že výrobci měří délku různě, někdo po křivce, někdo rovně. Rozdíl dělá centimetr až dva. Kdo si není jistý, zkusí lyže v půjčovně nebo na testovacím dni.</p>'
             )),
        dict(h2='Délka dětských lyží',
             html=(
                 '<p>U dětí platí jednodušší pravidlo: lyže mají sahat zhruba <strong>mezi bradu a nos</strong>. Malé děti a začátečníci jezdí na kratších, mezi hrudníkem a bradou. '
                 'Pokročilejší děti, které už jezdí oblouky po hranách, mohou mít lyže k nosu.</p>'
                 '<ul><li><strong>Hmotnost dítěte</strong> rozhoduje stejně jako výška. Lehké dítě na dlouhých a tvrdých lyžích je neprotočí.</li>'
                 '<li><strong>Nekupujte lyže „na dva roky“.</strong> Příliš dlouhé lyže brzdí pokrok a zvyšují riziko pádu.</li>'
                 '<li><strong>Dětské lyže</strong> se prodávají obvykle jako komplet s vázáním, které umí servis nastavit na nízké vypínací hodnoty.</li></ul>'
                 '<p>Výběr najdete v kategoriích <a href="/detske-lyze/">dětské lyže</a> a <a href="/lyze-komplety/">lyže s vázáním</a>. Tipy na zimní sporty s dětmi má článek <a href="/zimni-radovanky-s-detmi/">zimní radovánky s dětmi</a>.</p>'
             ), cat='detske-lyze', n=4),
        dict(h2='Profil lyže: camber, rocker a jejich kombinace',
             html=(
                 '<p>Když položíte lyži na rovnou zem, uvidíte její profil:</p>'
                 '<ul><li><strong>Camber (prohnutí)</strong>: střed lyže je nad zemí a lyže se dotýká jen u špičky a patky. Po zatížení se celá hrana opře o sníh. Dává přesný záběr na tvrdém podkladu a energii ve výjezdu z oblouku.</li>'
                 '<li><strong>Rocker (zvednutá špička)</strong>: špička, případně i patka, se zvedá dřív. Lyže se snáz točí a plave v hlubokém sněhu, na ledu ale drží hůř.</li>'
                 '<li><strong>Kombinace</strong>: camber pod vázáním a rocker ve špičce. Je nejrozšířenější u rekreačních a all-mountain lyží, protože spojuje záběr se snadným zahájením oblouku.</li></ul>'
                 '<p>Pro tvrdé české sjezdovky dává smysl lyže s převahou camberu a jen mírným rockerem ve špičce. Výrazný rocker na špičce i patce patří spíš do prašanu a parku.</p>'
             )),
        dict(h2='Tvrdost a poloměr oblouku',
             html=(
                 '<p><strong>Tvrdost (flex)</strong> výrobci obvykle neudávají číslem, poznáte ji podle určení lyže. Měkké lyže jsou pro začátečníky a lehčí lyžaře, '
                 'tvrdé s kovovými vrstvami (titanal) pro rychlou jízdu a těžší jezdce. Tvrdá lyže pod lehkým lyžařem nepracuje a je nepříjemně neposlušná.</p>'
                 '<p><strong>Poloměr oblouku (radius)</strong> je v metrech uvedený na lyži. Vyjadřuje, jaký oblouk lyže sama opíše, když ji položíte na hranu. '
                 'Malý poloměr znamená krátké oblouky a slalomový charakter, větší poloměr dlouhé rychlé oblouky. Rekreační lyže mají střední hodnotu, která zvládne obojí.</p>'
                 '<p>Při porovnání dvou modelů tedy sledujte šířku pod vázáním, délku, poloměr, profil a určení podle výrobce. Samotné „pro pokročilé“ v popisu obchodu nestačí.</p>'
             )),
        dict(h2='Vázání a jeho nastavení',
             html=(
                 '<p>Vázání drží botu na lyži a při pádu ji má uvolnit. Vypínací hodnota (lidově DIN) se nastavuje podle normy ISO 11088 z hmotnosti, výšky, věku, typu lyžaře a délky podrážky boty. '
                 'Tuto práci má dělat proškolený technik v servisu, který zkontroluje i funkci vypínání. Tabulky na internetu dávají jen orientační číslo.</p>'
                 '<ul><li>Hodnotu si sami nezvyšujte, abyste „nevypadávali“. Příliš tvrdé vázání při pádu nevypne.</li>'
                 '<li>Při každé výměně bot nechte vázání znovu nastavit, délka podrážky se mezi botami liší.</li>'
                 '<li>Rozsah vázání musí odpovídat lyžaři. Lehké děti potřebují vázání s nízkým rozsahem.</li></ul>'
                 '<p>Samostatná vázání najdete v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>, boty v kategorii <a href="/lyzarske-boty/">lyžařské boty</a>.</p>'
             ), cat='lyzarske-boty', n=4),
        dict(h2='Postup výběru lyží krok za krokem',
             html=(
                 '<ol><li><strong>Určete terén.</strong> Jen sjezdovka, nebo i mimo ni? Podle toho zvolte typ a šířku.</li>'
                 '<li><strong>Odhadněte poctivě úroveň.</strong> Kdo jezdí převážně smykem, je začátečník nebo středně pokročilý, i když jezdí léta.</li>'
                 '<li><strong>Spočítejte délku</strong> podle výšky a úrovně, pak ji upravte podle hmotnosti a rockeru.</li>'
                 '<li><strong>Vyberte tvrdost</strong> podle hmotnosti a rychlosti jízdy.</li>'
                 '<li><strong>Nejdřív boty.</strong> Dobře padnoucí lyžařské boty mají na ovládání lyží větší vliv než samotné lyže.</li>'
                 '<li><strong>Nechte nastavit vázání</strong> v servisu a lyže namazat, podrobnosti v kategorii <a href="/lyzarske-vosky/">lyžařské vosky</a>.</li></ol>'
                 '<p>K lyžím patří i přilba a brýle. Výběr najdete v kategoriích <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/lyzarske-hole/">lyžařské hole</a>.</p>'
             ), cat='lyzarske-helmy', n=4),
        dict(h2='Nové lyže, bazar, nebo půjčovna?',
             html=(
                 '<p>Kdo jede na hory jednou za sezonu, nemusí lyže hned kupovat. Půjčovna nabízí aktuální modely, servis i nastavení vázání v ceně, a navíc umožní vyzkoušet různé délky. '
                 'Sezonní pronájem se hodí hlavně pro děti, kterým lyže každý rok rostou. Vlastní lyže se vyplatí, když jezdíte víc týdnů ročně nebo chcete stále stejný pocit z jízdy.</p>'
                 '<p>U lyží z bazaru zkontrolujte:</p>'
                 '<ul><li>hrany bez prasklin a výrazné rzi, skluznici bez hlubokých rýh až na jádro,</li>'
                 '<li>že lyže nejsou zkroucené a po položení k sobě mají stejný profil,</li>'
                 '<li>rok výroby a typ vázání; u velmi starého vázání servis odmítne nastavení,</li>'
                 '<li>prasklé nebo oprýskané špičky a patky, kudy se do jádra dostává voda.</li></ul>'
             )),
        dict(h2='Péče o lyže během sezony',
             html=(
                 '<p>Po každém lyžování lyže otřete a nechte oschnout při pokojové teplotě, ne na topení. Hrany po čase otupí kamínky a led, skluznice vysychá. '
                 'Brousit hrany a voskovat se vyplatí několikrát za sezonu, podle toho, kolik jezdíte. Na konci sezony nechte lyže v servisu ošetřit a uložte je s vrstvou vosku v suchu.</p>'
                 '<p>Při přenášení a převozu pomůže vak, nabídku najdete v kategorii <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>.</p>'
             ), cat='lyzarske-vaky-a-tasky', n=4),
        dict(h2='Nejčastější chyby při nákupu lyží',
             html=(
                 '<ul><li><strong>Příliš dlouhé a tvrdé lyže.</strong> Vypadají „pokročile“, ale většina lidí na nich jezdí hůř.</li>'
                 '<li><strong>Freeridové lyže na sjezdovku.</strong> Široká lyže na tvrdém sněhu hůř drží hranu a víc namáhá kolena.</li>'
                 '<li><strong>Úspora na botách.</strong> Lyže nijak nespraví volnou nebo tlačící botu.</li>'
                 '<li><strong>Vázání podle tabulky z internetu.</strong> Bez kontroly v servisu chybí jistota, že vypne.</li>'
                 '<li><strong>Lyže pro děti s rezervou.</strong> Na dlouhých lyžích se dítě nenaučí zatáčet.</li></ul>'
                 '<p>Při srovnání cen se vyplatí sledovat starší ročníky stejného modelu, které se od nových liší často jen grafikou. Podívejte se na nabídku značek <a href="/znacka/atomic/">Atomic</a>, '
                 '<a href="/znacka/salomon/">Salomon</a> nebo <a href="/znacka/fischer/">Fischer</a>.</p>'
             )),
    ],
    faq=[
        ('Jak dlouhé lyže potřebuji?',
         '<p>Obvykle mezi bradou a temenem hlavy. Začátečníci kratší (k bradě až rtu), pokročilí delší (k obočí až temeni), freeride i kolem vlastní výšky.</p>'),
        ('Jaká délka lyží při výšce 170 cm?',
         '<p>Začátečník zhruba 145–155 cm, středně pokročilý 155–165 cm, pokročilý 160–170 cm. Těžší lyžař se posouvá k horní hranici.</p>'),
        ('Jak dlouhé lyže pro dítě?',
         '<p>Dětské lyže mají sahat zhruba mezi bradu a nos. Malé děti a začátečníci na kratších, až k hrudníku.</p>'),
        ('Jaké jsou druhy sjezdových lyží?',
         '<p>Sjezdovkové (carving), slalomky, obřačky, all-mountain, freeride a freestyle. Liší se šířkou, tvrdostí a profilem.</p>'),
        ('Jaké lyže pro začátečníka?',
         '<p>Měkčí sjezdovkové nebo užší all-mountain lyže s mírným rockerem ve špičce, kratší délka mezi bradou a horním rtem.</p>'),
        ('Co znamená rocker a camber?',
         '<p>Camber je prohnutí lyže uprostřed, dává záběr na tvrdém sněhu. Rocker je zvednutá špička nebo patka, usnadňuje točení a plavání v prašanu.</p>'),
        ('Mohu si vázání nastavit sám?',
         '<p>Nedoporučuje se. Vypínací hodnota podle ISO 11088 se nastavuje v servisu podle hmotnosti, výšky, věku, úrovně a délky podrážky a technik ověří funkci.</p>'),
        ('Co je poloměr oblouku lyže?',
         '<p>Údaj v metrech, který říká, jaký oblouk lyže opíše na hraně. Menší poloměr znamená krátké oblouky, větší dlouhé.</p>'),
        ('Jak široké lyže na sjezdovku?',
         '<p>Pro upravené sjezdovky se obvykle volí lyže zhruba do 85 mm pod vázáním, všestranné all-mountain mívají asi 85–105 mm.</p>'),
        ('Mám koupit nejdřív lyže, nebo boty?',
         '<p>Boty. Na jejich padnutí záleží nejvíc a délka podrážky ovlivní i nastavení vázání.</p>'),
    ],
    cats=['sjezdove-lyze', 'detske-lyze', 'lyze-komplety', 'lyzarske-vazani', 'lyzarske-boty', 'skialpove-lyze'],
    updated='2026-11-19')

# ---------------------------------------------------------------- jak-vybrat-snowboard
SB_LEN = T(['Hmotnost jezdce', 'Orientační délka prkna', 'Poznámka'], [
    ['do 45 kg', 'asi 130–145 cm', 'mládež a lehcí dospělí'],
    ['45–55 kg', 'asi 140–150 cm', ''],
    ['55–65 kg', 'asi 145–155 cm', ''],
    ['65–75 kg', 'asi 150–158 cm', 'nejčastější rozsah'],
    ['75–85 kg', 'asi 155–162 cm', ''],
    ['85–95 kg', 'asi 158–165 cm', 'zvažte širší verzi'],
    ['nad 95 kg', 'od asi 162 cm', 'tvrdší nebo širší prkno'],
])
SB_STYLE = T(['Styl', 'Délka vůči výchozí', 'Profil a tvrdost'], [
    ['Začátečník', 'spíš kratší', 'měkké, rocker nebo plochý profil'],
    ['Freestyle, park', 'o 2–5 cm kratší', 'měkčí, twin tip, hybrid'],
    ['All-mountain', 'výchozí délka', 'střední tvrdost, hybrid nebo camber'],
    ['Freeride, prašan', 'o 3–6 cm delší', 'tvrdší, rocker ve špičce, směrový tvar'],
    ['Carving na sjezdovce', 'výchozí až delší', 'tvrdší, převaha camberu'],
])

GUIDES['jak-vybrat-snowboard'] = dict(
    name='Jak vybrat snowboard',
    h1='Jak vybrat snowboard: délka, šířka a profil',
    seo_title='Jak vybrat snowboard: délka podle váhy, šířka a profil prkna',
    seo_desc='Jak vybrat snowboard: délka podle hmotnosti a výšky, šířka podle velikosti bot, camber nebo rocker, tvrdost a vázání. Tabulky a postup pro začátečníky.',
    intro_html=(
        '<p><strong>Jak vybrat snowboard?</strong> Délku prkna určuje hlavně hmotnost jezdce, výška je až druhá. Pro začátek se dá vyjít z pravidla, že prkno postavené na zem sahá zhruba mezi bradu a nos, '
        'a pak délku upravit podle hmotnosti a stylu. Jezdec kolem 70 kg obvykle jezdí na prkně dlouhém asi 150–158 cm. '
        'Šířka prkna musí odpovídat velikosti bot, aby špička a pata nedrhly o sníh. Začátečníci volí měkčí prkno s rockerem nebo plochým profilem.</p>'
        '<p>V článku najdete tabulku délek podle hmotnosti, vysvětlení profilů camber a rocker, tvrdosti, tvaru prkna i kompatibility vázání a bot.</p>'
        '<p>Sporteka nic neprodává, srovnává nabídky českých e-shopů. Pod částmi článku jsou snowboardy, boty a vázání, které obchody nabízejí.</p>'
    ),
    sections=[
        dict(h2='Délka snowboardu podle hmotnosti',
             html=(
                 '<p>Prkno funguje jako pružina, kterou jezdec zatěžuje svou hmotností. Příliš krátké prkno je pod těžkým jezdcem nestabilní, příliš dlouhé se pod lehkým nedá ohnout a těžko se točí. '
                 'Proto výrobci u každé délky uvádějí doporučený rozsah hmotnosti. Ten je spolehlivější než jakákoli obecná tabulka.</p>'
                 + SB_LEN +
                 '<p>Tabulka je orientační, rozsahy se liší podle modelu a tvrdosti. Tvrdší prkno unese při stejné délce víc. '
                 'Když váha ukazuje víc, než by odpovídalo výšce, držte se hmotnostního rozsahu výrobce. Když méně, vyberte kratší délku.</p>'
                 '<p>Přehled nabídky najdete v kategorii <a href="/snowboardy/">snowboardy</a>, vybrané značky třeba na stránkách <a href="/head-snowboard/">snowboardy Head</a> a <a href="/raven-snowboard/">snowboardy Raven</a>.</p>'
             ), cat='snowboardy', n=4),
        dict(h2='Délka podle stylu jízdy',
             html=(
                 '<p>Od výchozí délky podle hmotnosti se dál posunete podle toho, jak a kde jezdíte:</p>'
                 + SB_STYLE +
                 '<p>Kratší prkno se snáz točí, lépe se s ním skáče a rychleji se na něm učí. Delší prkno je stabilnější v rychlosti a v prašanu lépe nese. '
                 'Začátečníkům se vyplatí spíš kratší délka z doporučeného rozsahu. Jak se zlepšují, prkno se jim stejně za pár sezon vymění.</p>'
             )),
        dict(h2='Šířka prkna a velikost bot',
             html=(
                 '<p>Šířka v pase (nejužší místo prkna, waist) se udává v milimetrech. Boty v zapnutém vázání mírně přečnívají přes hranu. Když přečnívají příliš, '
                 'špička nebo pata zadrhne o sníh v náklonu a jezdec spadne. Proto se k velkým botám volí širší prkno.</p>'
                 '<ul><li><strong>Běžná šířka</strong> stačí většině jezdců s menší a střední velikostí bot.</li>'
                 '<li><strong>Mid-wide a wide (W)</strong> verze se doporučují pro velké nohy. Prodejci uvádějí orientačně pánské boty od velikosti US 10,5 až 11, tedy zhruba od EU 44–45.</li>'
                 '<li><strong>Dámská prkna</strong> bývají užší a měkčí, sedí menším botám a nižší hmotnosti.</li></ul>'
                 '<p>Hranice se mezi výrobci liší. Spolehlivější je tabulka konkrétního modelu, kde je u každé délky šířka a rozsah velikosti bot. '
                 'Pomůže i úhel vázání: větší úhel natočení snižuje přesah bot, ale jen do určité míry.</p>'
                 '<p>Boty najdete v kategorii <a href="/snowboardove-boty/">snowboardové boty</a>.</p>'
             ), cat='snowboardove-boty', n=4),
        dict(h2='Profil prkna: camber, rocker, plochý a hybrid',
             html=(
                 '<ul><li><strong>Camber</strong> je klasické prohnutí, střed prkna je nad zemí. Dává přesný záběr hran, dobrou stabilitu v rychlosti a pružnost při výjezdu z oblouku. Chyby ale netoleruje a hrany snadno zaseknou.</li>'
                 '<li><strong>Rocker</strong> je opačné prohnutí, prkno se jako kolébka zvedá ke špičce i patce. Snáz se točí, lépe plave v prašanu a méně zasekává hrany, na ledu ale drží hůř.</li>'
                 '<li><strong>Plochý profil (flat)</strong> leží celou délkou na zemi. Je stabilní a přitom rychle reaguje, oblíbený u začátečníků i ve snowparku.</li>'
                 '<li><strong>Hybrid</strong> kombinuje camber pod nohama a rocker ve špičce a patce, nebo naopak. Spojuje záběr se snadným točením a je dnes nejrozšířenější.</li></ul>'
                 '<p>Pro první sezony se nejvíc hodí rocker, plochý profil nebo hybrid s rockerem uprostřed. Čistý camber ocení jezdci, kteří už jezdí oblouky po hranách.</p>'
             )),
        dict(h2='Tvrdost a tvar prkna',
             html=(
                 '<p><strong>Tvrdost (flex)</strong> výrobci obvykle udávají na stupnici, často 1–10. Měkká prkna (1–4) jsou pro začátečníky a park, střední (5–6) pro all-mountain, '
                 'tvrdá (7–10) pro rychlou jízdu a freeride. Stupnice ale není jednotná a každá značka ji počítá po svém.</p>'
                 '<p><strong>Tvar</strong> prkna:</p>'
                 '<ul><li><strong>True twin</strong>: souměrné prkno, jezdí se stejně dopředu i pozadu. Ideální do parku.</li>'
                 '<li><strong>Directional twin</strong>: tvar souměrný, ale tvrdost nebo postavení vázání mírně směrové. Univerzální volba.</li>'
                 '<li><strong>Directional</strong>: delší a měkčí špička, kratší patka. Pro jízdu dopředu a freeride.</li></ul>'
             )),
        dict(h2='Vázání, boty a kompatibilita',
             html=(
                 '<p>Prkno, vázání a boty tvoří jeden systém. Než nakoupíte, ověřte:</p>'
                 '<ol><li><strong>Velikost vázání</strong> (S, M, L) musí odpovídat velikosti bot. Každý výrobce má vlastní tabulku.</li>'
                 '<li><strong>Uchycení na prkno</strong>: většina vázání sedí na otvory 4×2 i 2×4. Některá prkna Burton mají kolejnici Channel, na kterou potřebujete vázání s kompatibilním diskem.</li>'
                 '<li><strong>Tvrdost</strong> vázání a bot má odpovídat prknu. Tvrdé vázání na měkkém prkně je zbytečné a obráceně.</li>'
                 '<li><strong>Systém zapínání bot</strong>: klasické tkaničky, rychlošněrování nebo otočný kolečkový systém. Vyberte podle pohodlí, ne podle módy.</li></ol>'
                 '<p>Vázání najdete v kategorii <a href="/snowboardova-vazani/">snowboardová vázání</a>. Pro začátek se vyplatí komplet, nabídka v kategorii <a href="/snowboardove-sety/">snowboardové sety</a>. '
                 'Podívejte se také na nabídku značky <a href="/znacka/burton/">Burton</a>.</p>'
             ), cat='snowboardova-vazani', n=4),
        dict(h2='Postup výběru snowboardu',
             html=(
                 '<ol><li>Zvažte, kde budete jezdit: sjezdovka, park, prašan.</li>'
                 '<li>Podle hmotnosti najděte doporučený rozsah délek v tabulce výrobce.</li>'
                 '<li>Délku upravte podle stylu a úrovně, začátečník spíš kratší.</li>'
                 '<li>Zkontrolujte šířku podle velikosti bot.</li>'
                 '<li>Vyberte profil a tvrdost.</li>'
                 '<li>Doplňte vázání a boty kompatibilní s prknem.</li>'
                 '<li>Nezapomeňte na helmu a chrániče zápěstí, kostrče a kolen.</li></ol>'
                 '<p>Chrániče najdete v kategorii <a href="/snowboardove-chranice/">snowboardové chrániče</a>, oblečení v kategoriích <a href="/snowboardove-bundy/">snowboardové bundy</a> a <a href="/snowboardove-kalhoty/">snowboardové kalhoty</a>.</p>'
             ), cat='snowboardove-chranice', n=4),
        dict(h2='Postoj: regular, goofy a nastavení vázání',
             html=(
                 '<p>Než vázání namontujete, zjistěte, kterou nohu máte vpředu. <strong>Regular</strong> jezdí levou nohou vpředu, <strong>goofy</strong> pravou. '
                 'Jednoduchý test: rozběhněte se po hladké podlaze v ponožkách a sklouzněte. Noha, která jde instinktivně dopředu, bude přední. Jinou možností je nechat se zlehka postrčit zezadu a sledovat, kterou nohou vykročíte.</p>'
                 '<p><strong>Šíře postoje</strong> se obvykle začíná zhruba na šířce ramen, většina prken má vyznačené doporučené otvory. '
                 'Běžné výchozí nastavení úhlů bývá přední noha natočená dopředu kolem 15° a zadní kolem 0° nebo mírně do minusu. Postoj „kachna“ s oběma špičkami ven se hodí, když chcete jezdit i pozadu.</p>'
                 '<p>Nastavení si upravte po prvních dnech na svahu. Pokud vás bolí kolena, zkuste menší úhly nebo užší postoj, případně se poraďte v servisu.</p>'
             )),
        dict(h2='Nové prkno, bazar, nebo půjčovna?',
             html=(
                 '<p>Na první dny na svahu se vyplatí půjčovna. Uvidíte, jestli vás snowboard baví, a vyzkoušíte různé délky a profily. '
                 'Vlastní prkno dává smysl, když jezdíte pravidelně a víte, jaký styl vás táhne.</p>'
                 '<p>U prkna z bazaru zkontrolujte skluznici a hrany, zda nejsou prasklé nebo vyrvané, jestli prkno není prohnuté jinak než má být a jestli závity pro vázání drží. '
                 'Delaminace, tedy odlepené vrstvy na špičce nebo podél hran, znamená konec prkna. Boty kupujte raději nové, vnitřní bota se po letech vyšlape.</p>'
             )),
        dict(h2='Péče o snowboard',
             html=(
                 '<p>Prkno po jízdě otřete a nechte oschnout. Hrany brousí a skluznici voskuje servis nebo zkušený jezdec doma, frekvence záleží na tom, kolik jezdíte a jaký je sníh. '
                 'Po sezoně prkno uložte s ochrannou vrstvou vosku, v suchu a mimo zdroj tepla. Při převozu chrání prkno i auto vak, nabídku najdete v kategorii <a href="/lyzarske-vaky-a-tasky/">vaky a tašky</a>.</p>'
                 '<p>Dotažení šroubů vázání zkontrolujte na začátku každého dne, uvolněné vázání se projeví nejistou jízdou a může poškodit závity.</p>'
             ), cat='lyzarske-vaky-a-tasky', n=4),
        dict(h2='Časté chyby při výběru snowboardu',
             html=(
                 '<ul><li><strong>Délka jen podle výšky.</strong> Lehký vysoký jezdec na dlouhém prkně ho neohne.</li>'
                 '<li><strong>Úzké prkno pro velké boty.</strong> Drhnoucí špička způsobí nečekané pády.</li>'
                 '<li><strong>Tvrdé camberové prkno na začátek.</strong> Zasekává hrany a učení zpomaluje.</li>'
                 '<li><strong>Nekompatibilní vázání.</strong> Zkontrolujte uchycení, hlavně u prken s kolejnicí.</li>'
                 '<li><strong>Staré boty z bazaru.</strong> Vyšlapaná vnitřní bota nedrží patu a prkno se hůř ovládá.</li></ul>'
                 '<p>Kdo váhá mezi lyžemi a snowboardem, může si přečíst i článek <a href="/jak-vybrat-sjezdove-lyze/">jak vybrat sjezdové lyže</a>.</p>'
             )),
    ],
    faq=[
        ('Jak dlouhý snowboard potřebuji?',
         '<p>Délku určuje hlavně hmotnost, výrobci u každé délky uvádějí rozsah. Výchozí odhad je prkno mezi bradou a nosem, jezdci kolem 70 kg obvykle 150–158 cm.</p>'),
        ('Je důležitější hmotnost, nebo výška?',
         '<p>Hmotnost. Ta určuje, jak prkno ohnete. Výška a velikost bot slouží k doladění.</p>'),
        ('Jaký snowboard pro začátečníka?',
         '<p>Měkčí prkno s rockerem, plochým profilem nebo hybridem, spíš kratší délka z doporučeného rozsahu, tvar twin nebo directional twin.</p>'),
        ('Kdy potřebuji široký snowboard?',
         '<p>Když boty přečnívají přes hranu tak, že drhnou o sníh. Prodejci to uvádějí orientačně od pánských bot US 10,5–11 (zhruba EU 44–45).</p>'),
        ('Jaký je rozdíl mezi camberem a rockerem?',
         '<p>Camber je prohnutí nahoru uprostřed, dává záběr a stabilitu. Rocker je zvednutá špička i patka, prkno se snáz točí a plave v prašanu.</p>'),
        ('Co znamená tvrdost snowboardu?',
         '<p>Jak moc se prkno ohýbá. Měkké jsou pro začátečníky a park, tvrdé pro rychlou jízdu a freeride. Stupnice se mezi značkami liší.</p>'),
        ('Pasuje každé vázání na každé prkno?',
         '<p>Většina vázání sedí na standardní otvory, prkna s kolejnicí Channel potřebují kompatibilní disk. Vždy to ověřte u výrobce.</p>'),
        ('Mám koupit snowboardový set?',
         '<p>Pro začátečníka je set praktický, vázání je sladěné s prknem. Boty ale vybírejte zvlášť podle nohy.</p>'),
        ('Jak dlouhý snowboard pro dítě?',
         '<p>U dětí rozhoduje hmotnost ještě víc, prkno by mělo sahat zhruba mezi hrudník a bradu. Dětská prkna jsou měkká a kratší.</p>'),
    ],
    cats=['snowboardy', 'snowboardove-boty', 'snowboardova-vazani', 'snowboardove-sety', 'snowboarding'],
    updated='2026-11-19')
