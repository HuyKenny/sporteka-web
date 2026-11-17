"""Guides wave 3a: size chart for shoes and clothing (EU / UK / US / cm, kids by height, Mondopoint, helmets, gloves).

Demand (Ahrefs CZ / month): tabulka velikostí 2 100, dětské velikosti 2 000, velikost bot 1 400,
tabulka velikostí bot 700, velikost bot v cm 700, velikostní tabulka děti 250.

How the numbers were built (all values are approximate on purpose and the page says so):
- Foot length column: ISO/TS 19407 relation EUR = 0.15 x L(mm) + 2, i.e. L = (EU - 2) x 20/3 mm
  (Paris point = 2/3 cm, last = foot + 2 Paris points). Source: Wikipedia "Shoe size" (sections Continental
  European system, ISO/TS 19407 shoe sizing; adult and children's equivalence tables).
- Adult UK / US men / US women columns: ranges spanning the brand charts of Nike (nike.com/size-fit/mens-footwear,
  womens-footwear: e.g. EU 42 = UK 7.5 = US M 8.5 = 26.5 cm/JP) and adidas (UK 8 = EU 42 = US M 8.5, US M = UK + 0.5,
  US W = UK + 1.5; runrepeat.com/uk/size-charts/adidas, adidas US 9 = 270 mm). Wikipedia: US men = UK + 1 in the
  customary system; ISO/TS 19407 theoretical table gives UK/US about half to one size higher than brand labels.
- Children's UK / US columns: Wikipedia children's table after ISO/TS 19407 (EU 20 = 120 mm = UK 4 = US 4.5;
  EU 24 = UK 7.5; EU 28 = UK 10.5; EU 31 = UK 13), US kids = UK + 0.5 (same as adidas kids).
- Adults: last is 13-25 mm longer than the foot (Wikipedia, ISO/TS 19407 section). Children: inside length at least
  12 mm and up to about 17 mm over foot length (Apotheken Umschau, Spektrum.de, wunschkind-community.de).
- Mondopoint: ISO 9407:2019, foot length and width in mm (e.g. 280/110) - Wikipedia "Shoe size". Ski boots: mondo = foot
  length in cm; 26.0 and 26.5 often share a shell (jans.com, getcarv.com, peterglenn.com Mondopoint guides).
- Measuring the foot at home: heel to wall, mark the longest toe, evening, larger foot (several measuring guides,
  e.g. blitzresults.com, deichmann.com kids guide).
- Adult clothing chest/waist: adidas men (sport-conrad.com / absolute-snow.co.uk Terrex: M chest 93-100, waist 81-88),
  adidas EU guide (M chest 95-102), Nike men tops (hibbett.com: M 37.5-41 in = 95-104 cm), Nike women tops
  (nike.com/size-fit/womens-tops-alpha, inches converted). Table rounds across these.
- Children's clothing: European size = body height in cm, 6 cm steps, ages only indicative
  (rechner-portal.de Kindergrößenrechner, familie.de, wunschkind-community.de); EN 13402: height is the primary
  dimension for children (Wikipedia "EN 13402").
- Helmets: head circumference just above ears and eyebrows; S 51-55, M 55-59, L 59-63 cm at Smith and Atomic
  (skatepro charts); HEAD and Salomon measuring guides.
- Gloves: circumference of the palm below the knuckles without the thumb; EN ISO 21420 sizes 6-11 =
  152/178/203/229/254/279 mm (Ejendals TEGERA size guide, Wenaas EN ISO 21420 page).
- Bikes: frame size from height and inseam per manufacturer; kids' bikes by wheel size (Schwinn, Trek kids guides).
Left out because sources disagree or could not be verified: a single "correct" UK/US value per EU size, shoe sizes by
child's age, a fixed shell-check gap for ski boots, inseam x coefficient formulas for bike frames, numeric glove size
per cm for sports brands.
"""
from texty_vlna1a import T

GUIDES = {}

ADULT_SHOES = T(['EU', 'Délka chodidla (cm, cca)', 'UK', 'US pánské', 'US dámské'], [
    ['35', '22,0', '2–3', '3–3,5', '4–4,5'],
    ['36', '22,7', '3–3,5', '4', '5–5,5'],
    ['37', '23,3', '4–4,5', '4,5–5', '5,5–6,5'],
    ['38', '24,0', '5', '5,5', '6,5–7'],
    ['39', '24,7', '5,5–6', '6–6,5', '7–8'],
    ['40', '25,3', '6–6,5', '7', '8–8,5'],
    ['41', '26,0', '7–7,5', '7,5–8', '8,5–9,5'],
    ['42', '26,7', '7,5–8', '8,5', '9,5–10'],
    ['43', '27,3', '8,5–9', '9–9,5', '10–11'],
    ['44', '28,0', '9–9,5', '10', '11–11,5'],
    ['45', '28,7', '10–10,5', '10,5–11', '11,5–12,5'],
    ['46', '29,3', '11', '11,5–12', '12,5–13,5'],
    ['47', '30,0', '11,5–12', '12–12,5', '13–14'],
])

KIDS_SHOES = T(['EU', 'Délka chodidla (cm, cca)', 'UK (dětské)', 'US (dětské)'], [
    ['18', '10,7', '2,5', '3'],
    ['19', '11,3', '3', '3,5'],
    ['20', '12,0', '4', '4,5'],
    ['21', '12,7', '5', '5,5'],
    ['22', '13,3', '5,5', '6'],
    ['23', '14,0', '6,5', '7'],
    ['24', '14,7', '7,5', '8'],
    ['25', '15,3', '8', '8,5'],
    ['26', '16,0', '9', '9,5'],
    ['27', '16,7', '9,5', '10'],
    ['28', '17,3', '10,5', '11'],
    ['29', '18,0', '11,5', '12'],
    ['30', '18,7', '12', '12,5'],
    ['31', '19,3', '13', '13,5'],
    ['32', '20,0', '13,5', '1'],
    ['33', '20,7', '1–1,5', '1,5–2'],
    ['34', '21,3', '2–2,5', '2,5–3'],
    ['35', '22,0', '2,5–3', '3–3,5'],
])

MEN_CLOTHES = T(['Velikost', 'Obvod hrudníku (cm)', 'Obvod pasu (cm)'], [
    ['XS', '82–88', '70–75'],
    ['S', '88–94', '75–81'],
    ['M', '94–102', '81–88'],
    ['L', '102–110', '88–96'],
    ['XL', '110–120', '96–106'],
    ['XXL', '120–130', '106–118'],
])

WOMEN_CLOTHES = T(['Velikost', 'Obvod hrudníku (cm)', 'Obvod pasu (cm)', 'Obvod boků (cm)'], [
    ['XS', '76–83', '60–66', '84–90'],
    ['S', '83–90', '66–74', '90–98'],
    ['M', '90–97', '74–80', '98–104'],
    ['L', '97–104', '80–88', '104–112'],
    ['XL', '104–113', '88–98', '112–119'],
    ['XXL', '113–123', '98–108', '119–127'],
])

KIDS_CLOTHES = T(['Velikost', 'Výška dítěte (cm)', 'Orientační věk'], [
    ['50', 'do 50', 'novorozenec'],
    ['56', '51–56', '1–2 měsíce'],
    ['62', '57–62', '2–4 měsíce'],
    ['68', '63–68', '4–6 měsíců'],
    ['74', '69–74', '6–9 měsíců'],
    ['80', '75–80', '9–12 měsíců'],
    ['86', '81–86', '1–1,5 roku'],
    ['92', '87–92', '2 roky'],
    ['98', '93–98', '3 roky'],
    ['104', '99–104', '4 roky'],
    ['110', '105–110', '5 let'],
    ['116', '111–116', '6 let'],
    ['122', '117–122', '7 let'],
    ['128', '123–128', '8 let'],
    ['134', '129–134', '9 let'],
    ['140', '135–140', '10 let'],
    ['146', '141–146', '11 let'],
    ['152', '147–152', '12 let'],
    ['158', '153–158', '13 let'],
    ['164', '159–164', '14 let'],
    ['170', '165–170', '15 let'],
    ['176', '171–176', '16 let'],
])

GLOVES = T(['Velikost', 'Obvod dlaně (mm)', 'Písmenné označení'], [
    ['6', '152', 'XS'],
    ['7', '178', 'S'],
    ['8', '203', 'M'],
    ['9', '229', 'L'],
    ['10', '254', 'XL'],
    ['11', '279', 'XXL'],
])

HELMETS = T(['Velikost', 'Obvod hlavy (cm)'], [
    ['S', '51–55'],
    ['M', '55–59'],
    ['L', '59–63'],
    ['XL', 'od 63'],
])

# ---------------------------------------------------------------- tabulka-velikosti
GUIDES['tabulka-velikosti'] = dict(
    name='Tabulka velikostí',
    h1='Tabulka velikostí bot a oblečení: EU, UK, US a centimetry',
    seo_title='Tabulka velikostí bot a oblečení: EU, UK, US a cm',
    seo_desc='Velikost bot v cm i převod EU, UK a US pro dospělé a děti, dětské velikosti podle výšky, oblečení XS–XXL, lyžáky, helmy a rukavice. Jak se správně měřit.',
    intro_html=(
        '<p>Na krabici od tenisek bývají tři až čtyři čísla: evropská velikost, britská, americká a centimetry. V e-shopu pak stačí jedno kliknutí vedle a bota je malá. '
        'Tento průvodce vysvětluje, co jednotlivá čísla znamenají, jak si doma změřit chodidlo a jak převést <strong>velikost bot v cm</strong> na EU, UK a US. '
        'Najdete tu i tabulku velikostí oblečení pro dospělé, <strong>dětské velikosti podle výšky</strong>, velikosti lyžařských bot v systému Mondopoint, helem a rukavic.</p>'
        '<p>Všechny tabulky na této stránce jsou orientační. Každá značka šije a lisuje podle vlastních kopyt a střihů, a proto má vlastní tabulku. '
        'Nike, Adidas nebo Salomon se mezi sebou klidně liší o půl až celé číslo. Naše tabulka vám pomůže odhadnout, kde hledat. '
        'Před objednávkou vždy porovnejte svou naměřenou délku chodidla s tabulkou výrobce u konkrétního modelu.</p>'
        '<p>Sporteka nic neprodává. Srovnává nabídky českých e-shopů, takže pod každou částí vidíte boty a oblečení z příslušné kategorie a objednáváte přímo v obchodě.</p>'
    ),
    sections=[
        dict(h2='Jak si doma změřit délku chodidla v centimetrech',
             html=(
                 '<p>Nejspolehlivější základ je délka chodidla v centimetrech. Číslo z bot, které právě nosíte, je jen odhad, protože ty mohly být od jiné značky nebo už povolily.</p>'
                 '<ol><li><strong>Připravte si</strong> list papíru, tužku, pravítko nebo svinovací metr. Papír položte na tvrdou podlahu ke zdi.</li>'
                 '<li><strong>Postavte se</strong> na papír bosí nebo v ponožkách, které budete do bot nosit. Patu opřete o zeď a váhu rozložte na obě nohy.</li>'
                 '<li><strong>Označte</strong> konec nejdelšího prstu. Nejdelší nemusí být palec, u části lidí přečnívá druhý prst. Tužku držte svisle.</li>'
                 '<li><strong>Změřte</strong> vzdálenost od zdi ke značce v milimetrech. Totéž zopakujte u druhé nohy.</li></ol>'
                 '<p>Rozhoduje delší noha, protože levá a pravá se u většiny lidí trochu liší. Měřte navečer, kdy je chodidlo po celém dni na nohou nejdelší. '
                 'U dětí měřte vestoje, ne vsedě, protože dítě při stání chodidlo zatíží a roztáhne. Malé děti rády krčí prsty, takže měření raději zopakujte.</p>'
                 '<p>Naměřené číslo je délka nohy, ne délka boty. Uvnitř boty musí zbýt místo na pohyb prstů. U dospělých bývá kopyto, podle kterého se bota vyrábí, '
                 'zhruba o 1,3 až 2,5 cm delší než chodidlo. U dětských bot doporučují dětští odborníci vnitřní délku nejméně o 12 mm delší, než je noha, s rezervou na růst až o 17 mm.</p>'
             )),
        dict(h2='EU, UK, US a Mondopoint: čtyři systémy na jedné krabici',
             html=(
                 '<p>Každý systém měří jinou věc a začíná od jiné nuly. Proto se čísla nedají převádět jedním jednoduchým vzorcem bez odchylek.</p>'
                 '<h3>Evropská velikost (EU)</h3>'
                 '<p>Evropské číslo udává délku kopyta v takzvaných pařížských bodech. Jeden bod má 2/3 cm, tedy asi 6,7 mm. O tolik se liší dvě sousední celá čísla, polovina čísla je asi 3,3 mm. '
                 'Kopyto je delší než noha zhruba o dva body. Z toho plyne orientační převod: <strong>délka chodidla v cm ≈ (EU − 2) × 2/3</strong>. Velikosti 42 tak odpovídá chodidlo dlouhé asi 26,7 cm.</p>'
                 '<h3>Britská velikost (UK)</h3>'
                 '<p>Britský systém počítá v třetinách palce, jeden krok je asi 8,5 mm. Dětská řada jde od 0 do 13,5 a pak začíná dospělá řada znovu od jedničky. '
                 'Proto je dětská bota UK 13 menší než dospělá UK 1, i když číslo vypadá větší.</p>'
                 '<h3>Americká velikost (US)</h3>'
                 '<p>Americká čísla vycházejí z britských, ale pánská řada je posunutá zhruba o jedno číslo nahoru a dámská ještě o něco víc. '
                 'Značky ten posun nepoužívají stejně: u Nike bývá dámské US o 1,5 čísla vyšší než pánské, u Adidas o jedno. Proto má smysl u unisex bot vždy zkontrolovat, zda je uvedené číslo pánské (M), nebo dámské (W).</p>'
                 '<h3>Mondopoint a centimetry</h3>'
                 '<p>Mondopoint popisuje mezinárodní norma ISO 9407. Udává délku a šířku chodidla v milimetrech, například 280/110 znamená nohu dlouhou 280 mm a širokou 110 mm. '
                 'Je to jediný systém, který vychází přímo z nohy, a ne z kopyta. Používají ho lyžařské a běžkařské boty a japonské velikosti. '
                 'Pozor na údaj „cm“ nebo „JP“ na krabicích sportovních značek: někdy jde o délku nohy, jindy o velikost boty. Nike u své tabulky výslovně uvádí, že sloupec CM/JP se od délky chodidla liší.</p>'
             )),
        dict(h2='Tabulka velikostí bot pro dospělé (EU 35–47)',
             html=(
                 '<p>Tabulka převádí evropskou velikost na přibližnou délku chodidla a na britská a americká čísla. Délka chodidla je vypočtená z mezinárodního převodu podle ISO/TS 19407. '
                 'Sloupce UK a US ukazují rozpětí, ve kterém se pohybují tabulky velkých sportovních značek. Kde je uveden rozsah, liší se výrobci mezi sebou.</p>'
                 + ADULT_SHOES +
                 '<p>Jak tabulku použít: najděte řádek s délkou chodidla, která je stejná nebo o něco větší než vaše naměřená hodnota. Pokud vám vyšlo 26,4 cm, začněte u EU 42. '
                 'Pak otevřete tabulku značky, kterou kupujete, a ověřte číslo tam. Teoretické převody podle norem dávají UK a US obvykle o půl až celé číslo výš, než píšou značky na krabice. '
                 'Proto se při nákupu řiďte tím, co uvádí výrobce, ne obecnou tabulkou z internetu.</p>'
                 '<p>Pánské a dámské boty mají v evropském systému stejná čísla, liší se však šířkou a tvarem kopyta. Dámská bota velikosti 40 bývá užší než pánská 40. '
                 'Široké chodidlo často potřebuje o půl čísla větší botu nebo model ve verzi „wide“. Nabídku pro každý den najdete v kategorii <a href="/tenisky/">tenisky</a>, '
                 'zúžit ji můžete na <a href="/nike-sportovni-boty/">boty Nike</a> nebo <a href="/sportovni-boty-adidas/">boty Adidas</a>.</p>'
             ), cat='tenisky', n=4),
        dict(h2='Proč má každá značka vlastní tabulku',
             html=(
                 '<p>Dvě boty se stejným číslem od dvou výrobců mívají různou vnitřní délku. Důvodů je několik a žádný z nich není chyba obchodu.</p>'
                 '<ul><li><strong>Kopyto:</strong> každá značka má vlastní tvarové kopyto, podle kterého boty vyrábí. Liší se délkou, šířkou ve špičce, výškou nártu i tvarem paty.</li>'
                 '<li><strong>Přídavek na pohyb:</strong> běžecká bota potřebuje víc místa před prsty než kopačka nebo lezečka, takže i u jednoho výrobce se velikosti napříč kategoriemi chovají jinak.</li>'
                 '<li><strong>Výchozí bod:</strong> americký a britský systém mají různé nuly pro děti, muže a ženy a výrobci je nepřevádějí stejně.</li>'
                 '<li><strong>Zaokrouhlení:</strong> evropské číslo se někdy uvádí na třetiny (42 2/3), jindy na poloviny (42,5). Adidas používá třetiny, Nike poloviny.</li></ul>'
                 '<p>Prakticky to znamená, že bota od <a href="/znacka/salomon/">Salomonu</a> může v čísle 42 sedět jinak než bota od <a href="/znacka/nike/">Nike</a> nebo <a href="/znacka/adidas/">Adidasu</a>. '
                 'Pokud už máte model, který vám dobře padne, vyhledejte jeho tabulku a zjistěte, jaká délka v centimetrech u něj odpovídá vaší velikosti. To číslo pak porovnávejte s ostatními značkami. '
                 'U běžeckých bot se často doporučuje mít před nejdelším prstem asi palec místa, protože noha při delším běhu oteče. Na výběr se hodí <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a> '
                 'nebo <a href="/trailove-boty/">trailové boty</a>, pro muže a ženy zvlášť pak <a href="/panske-bezecke-boty/">pánské běžecké boty</a> a <a href="/bezecke-boty-damske/">dámské běžecké boty</a>.</p>'
             ), cat='silnicni-bezecke-boty', n=4),
        dict(h2='Dětské velikosti bot (EU 18–35) a velikost bot v cm',
             html=(
                 '<p>U dětí je měření ještě důležitější než u dospělých, protože malé dítě neřekne, že ho bota tlačí. Noha batolete roste až o 1,5 mm měsíčně, u školáků obvykle méně než o milimetr, takže u malých dětí měřte každých pár měsíců. '
                 'Tabulka ukazuje přibližnou délku chodidla, britská a americká dětská čísla.</p>'
                 + KIDS_SHOES +
                 '<p>Velikost zvolte tak, aby vnitřní délka boty byla nejméně o 12 mm delší než naměřená noha. U zimních bot počítejte i s tlustší ponožkou. '
                 'Rezerva navíc by neměla přesáhnout zhruba 17 mm, jinak dítě v botě klouže, zakopává a nohu si v ní pere. Kupovat boty o dvě čísla větší „na příští rok“ se nevyplatí.</p>'
                 '<p>Některé dětské tabulky výrobců už přídavek na růst obsahují, jiné ne. Proto je u dětských bot nejlepší vytáhnout vložku, postavit na ni dítě a zkontrolovat, kolik místa zůstává před prsty. '
                 'Kdo vybírá zimní obuv, může začít u <a href="/detske-zimni-boty/">dětských zimních bot</a>, na sport se hodí <a href="/detske-bezecke-boty/">dětské běžecké boty</a> '
                 'a pro volný pohyb <a href="/detske-barefoot-boty/">dětské barefoot boty</a>. Celou nabídku zimních bot najdete v kategorii <a href="/zimni-obuv/">zimní obuv</a>.</p>'
             ), cat='zimni-obuv', n=4),
        dict(h2='Tabulka velikostí oblečení pro dospělé (XS–XXL)',
             html=(
                 '<p>Písmena XS až XXL nemají u všech značek stejný význam. Evropská norma EN 13402 popisuje značení podle tělesných rozměrů v centimetrech, rozsahy písmen si ale výrobci stanovují po svém. '
                 'U triček a bund je hlavní míra obvod hrudníku, u kalhot obvod pasu. Tabulky jsou zaokrouhlené z tabulek velkých sportovních značek.</p>'
                 '<h3>Pánské velikosti</h3>'
                 + MEN_CLOTHES +
                 '<h3>Dámské velikosti</h3>'
                 + WOMEN_CLOTHES +
                 '<h3>Jak se změřit</h3>'
                 '<ul><li><strong>Hrudník:</strong> krejčovský metr veďte vodorovně přes nejširší místo hrudníku a pod pažemi. Nadechněte se normálně, ne zhluboka.</li>'
                 '<li><strong>Pas:</strong> v nejužším místě trupu, obvykle kousek nad pupíkem.</li>'
                 '<li><strong>Boky:</strong> v nejširším místě přes hýždě, chodidla u sebe.</li></ul>'
                 '<p>Když vám hrudník vychází na jednu velikost a pas na jinou, řiďte se u triček a bund hrudníkem, u kalhot pasem. '
                 'Sportovní střihy se navíc liší podle účelu: kompresní a běžecká trička jsou úzká, outdoorové bundy počítají s vrstvou pod sebou. '
                 'U lyžařské bundy proto zkuste velikost s mikinou nebo <a href="/termopradlo/">termoprádlem</a>. Výběr najdete mezi <a href="/sportovni-tricka/">sportovními tričky</a>, <a href="/mikiny/">mikinami</a> a <a href="/zimni-bundy/">zimními bundami</a>.</p>'
             ), cat='sportovni-tricka', n=4),
        dict(h2='Dětské velikosti oblečení podle výšky (50–176 cm)',
             html=(
                 '<p>Evropské dětské velikosti jsou jednoduché: číslo odpovídá výšce dítěte v centimetrech. Velikost 110 je pro dítě vysoké přibližně 105 až 110 cm. '
                 'Řada postupuje po šesti centimetrech, od 50 pro novorozence po 176 pro dospívající. Norma EN 13402 také počítá u dětí s výškou jako hlavním rozměrem.</p>'
                 + KIDS_CLOTHES +
                 '<p>Věk je jen hrubé vodítko. Tříletí sourozenci nebo spolužáci se klidně liší o deset centimetrů, takže vždy měřte výšku. '
                 'Když dítě stojí na hranici dvou velikostí, vezměte vyšší. Výrobci často spojují dvě velikosti do jedné (například 122/128) a pak platí horní hodnota.</p>'
                 '<p>U zimního oblečení, kombinéz a lyžařských kalhot počítejte s vrstvou pod nimi a s tím, že děti v pohybu potřebují volnost v kolenou a ramenou. '
                 'Rukávy a nohavice mohou být o něco delší, ale bunda by neměla být tak velká, že dovnitř profukuje. '
                 'Projděte si <a href="/detske-sportovni-obleceni/">dětské sportovní oblečení</a>, <a href="/detska-zimni-bunda/">dětské zimní bundy</a>, '
                 '<a href="/detske-lyzarske-kalhoty/">dětské lyžařské kalhoty</a> a <a href="/detske-termopradlo/">dětské termoprádlo</a>. Tipy na zimní výlety s dětmi najdete v průvodci <a href="/zimni-radovanky-s-detmi/">zimní radovánky s dětmi</a>.</p>'
             ), cat='zimni-bundy', n=4),
        dict(h2='Velikost lyžařských bot: Mondopoint v praxi',
             html=(
                 '<p>Lyžařské boty se značí v Mondopointu, tedy podle délky chodidla v centimetrech. Když vám doma vyjde 26,4 cm, hledáte velikost 26 nebo 26,5. '
                 'Na botě bývá vedle Mondopointu i číslo EU nebo UK, ale u lyžáků je rozhodující právě údaj v centimetrech.</p>'
                 '<ul><li><strong>Skelet po celých číslech:</strong> u mnoha modelů mají velikosti 26 a 26,5 stejný plastový skelet a liší se jen vnitřní botičkou. Pokud jste mezi dvěma velikostmi, prodavači často doporučují tu menší, protože botička se časem slehne.</li>'
                 '<li><strong>Šířka kopyta:</strong> lyžařské boty mají uvedenou šířku v přední části v milimetrech. Užší kopyto drží nohu přesněji, širší je pohodlnější pro rekreační lyžování.</li>'
                 '<li><strong>Zkušení lyžaři</strong> volí boty těsnější, i o půl až celé číslo menší. Rekreační lyžař má zůstat u své délky chodidla.</li></ul>'
                 '<p>Zkoušejte boty v lyžařských ponožkách, ne v bavlněných, a nechte je na noze aspoň deset minut. Ve vzpřímeném stoji se prsty smějí lehce dotknout špičky, po předklonu v kotnících se od ní mají trochu odtáhnout. Pata se nesmí zvedat. '
                 'Dětem nekupujte lyžáky o velikost či dvě větší s výhledem na další sezónu: v příliš velké botě dítě lyže neovládá. '
                 'Nabídku najdete v kategorii <a href="/lyzarske-boty/">lyžařské boty</a>, rozdělenou na <a href="/panske-lyzarske-boty/">pánské</a>, <a href="/damske-lyzarske-boty/">dámské</a> '
                 'a <a href="/detske-lyzarske-boty/">dětské lyžařské boty</a>. Výběr běžkařského vybavení popisuje průvodce <a href="/bezky-pro-zacatecniky/">běžky pro začátečníky</a>.</p>'
             ), cat='lyzarske-boty', n=4),
        dict(h2='Helmy: velikost podle obvodu hlavy',
             html=(
                 '<p>Velikost lyžařské, cyklistické i jezdecké helmy se určuje podle obvodu hlavy v centimetrech. Měkký krejčovský metr veďte vodorovně kolem hlavy těsně nad obočím a nad ušima, vzadu přes nejvystouplejší místo týla. '
                 'Měřte dvakrát a použijte větší hodnotu.</p>'
                 + HELMETS +
                 '<p>Tato rozpětí používají například značky Smith a Atomic. Jiní výrobci mají rozsahy posunuté nebo přidávají mezivelikosti, a co je u jedné značky S, může být u jiné M. '
                 'Když jste přesně na hranici, zkuste obě velikosti a jemné doladění nechte na kolečku vzadu nebo na výměnných vložkách. '
                 'Správně nasazená helma se při zatřesení hlavou nehýbe, nezakrývá oči a netlačí na čele. Lyžařská helma má navíc navazovat na brýle bez mezery.</p>'
                 '<p>Helmu po silném nárazu vyměňte, i když na ní není vidět poškození. U dětí nekupujte helmu „na vyrůstání“, protože volná helma nechrání. '
                 'Výběr najdete v kategoriích <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/cyklisticke-helmy/">cyklistické helmy</a>, pro děti pak <a href="/detske-lyzarske-helmy/">dětské lyžařské helmy</a> '
                 'a <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</p>'
             ), cat='lyzarske-helmy', n=4),
        dict(h2='Rukavice: obvod dlaně a čísla 6 až 11',
             html=(
                 '<p>U rukavic se měří obvod dlaně. Metr oviňte kolem nejširšího místa dlaně těsně pod klouby prstů, bez palce. Měřte dominantní ruku, která bývá o něco větší. '
                 'Pracovní a ochranné rukavice se značí čísly podle normy EN ISO 21420, sportovní značky většinou písmeny a vlastními rozsahy.</p>'
                 + GLOVES +
                 '<p>Číselná řada odpovídá zhruba obvodu dlaně v palcích. Sportovní výrobci ji používají jen orientačně, takže u lyžařských nebo cyklistických rukavic se podívejte na tabulku konkrétní značky. '
                 'Zimní rukavice mají ve špičkách prstů nechat trochu volného místa, protože vrstva vzduchu kolem prstů hřeje. Příliš těsná rukavice studí, příliš volná se špatně ovládá. '
                 'U palčáků velikost tolik nerozhoduje, kontrolujte hlavně délku a manžetu.</p>'
                 '<p>Nabídku najdete v kategoriích <a href="/lyzarske-rukavice/">lyžařské rukavice</a>, <a href="/sportovni-rukavice/">sportovní rukavice</a> a <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>, '
                 'dětské modely pak mezi <a href="/detske-lyzarske-rukavice/">dětskými lyžařskými rukavicemi</a>.</p>'
             ), cat='lyzarske-rukavice', n=4),
        dict(h2='Velikost rámu kola jen krátce',
             html=(
                 '<p>Kolo se neměří obvodem ani délkou chodidla, ale výškou jezdce a vnitřní délkou nohy (od rozkroku k podlaze, naboso). Velikost rámu se uvádí v palcích, centimetrech nebo písmeny S až XL '
                 'a každý výrobce k ní má vlastní tabulku podle výšky. Porovnávejte proto tabulku konkrétního modelu, ne písmeno.</p>'
                 '<p>U dětských kol rozhoduje průměr kola v palcích. Menší děti začínají na 12 až 16 palcích, školáci jezdí na 20 a 24 palcích. Mezi rozkrokem dítěte a horní trubkou rámu má zůstat volné místo a výrobce u modelu uvádí doporučenou výšku dítěte. '
                 'Podrobnější výběr najdete v kategoriích <a href="/detska-kola-16-palcu/">dětská kola 16"</a>, <a href="/detska-kola-20-palcu/">20"</a> a <a href="/detska-kola-24-palcu/">24"</a>, '
                 'pro dospělé v kategorii <a href="/jizdni-kola/">jízdní kola</a>.</p>'
             ), cat='detska-kola', n=4),
        dict(h2='Časté chyby při výběru velikosti online',
             html=(
                 '<ul><li><strong>Číslo podle starých bot:</strong> boty se vyšlapou a značky se liší. Vždy vycházejte z naměřené délky chodidla.</li>'
                 '<li><strong>Záměna pánské a dámské US velikosti:</strong> u unisex modelů je na štítku často obojí. Přečtěte si, zda jde o M, nebo W.</li>'
                 '<li><strong>Délka boty místo délky nohy:</strong> když tabulka uvádí „cm“, ověřte, zda jde o nohu, nebo o stélku. Délka stélky je vždy delší.</li>'
                 '<li><strong>Měření ráno:</strong> chodidlo je přes den delší a širší. Měřte odpoledne nebo večer.</li>'
                 '<li><strong>Velká rezerva u dětí:</strong> přílišná rezerva ve špičce škodí stejně jako malá bota.</li>'
                 '<li><strong>Zapomenutá ponožka:</strong> do zimních a lyžařských bot se nosí tlustší ponožky. Mějte je na sobě při měření i zkoušení. Vhodné najdete mezi <a href="/sportovni-ponozky/">sportovními ponožkami</a>.</li></ul>'
                 '<p>Při nákupu přes internet se podívejte i na podmínky vrácení zboží. Spotřebitel má při nákupu na dálku obvykle 14 dní na odstoupení od smlouvy, '
                 'za botu nošenou venku vám ale obchod může vrácenou částku snížit. Boty proto zkoušejte doma na koberci. Na Sporteka porovnáte stejný model u více obchodů; '
                 'podrobněji popisujeme postup na stránce <a href="/jak-srovnavame/">jak srovnáváme</a>. Velikost bruslí řeší samostatný průvodce <a href="/brusle-na-led/">brusle na led</a>.</p>'
             )),
    ],
    faq=[
        ('Jak převést velikost bot v cm na evropskou velikost?',
         '<p>Orientačně platí: EU ≈ délka chodidla v cm × 1,5 + 2. Chodidlo dlouhé 26 cm tak odpovídá zhruba velikosti 41. Je to jen odhad, každá značka má vlastní tabulku, a proto si číslo ověřte u výrobce konkrétního modelu.</p>'),
        ('Jaká velikost bot je 27 cm?',
         '<p>Chodidlo dlouhé 27 cm odpovídá přibližně evropské velikosti 42,5 až 43, britské 8 až 9 a pánské americké 9 až 9,5. U některých značek budete potřebovat o třetinu až půl čísla víc, záleží na kopytě a typu boty.</p>'),
        ('Je velikost UK stejná jako US?',
         '<p>Není. Pánská americká velikost bývá o půl až jedno číslo vyšší než britská, dámská americká o jedno a půl až dvě a půl čísla. Přesný posun se liší podle značky.</p>'),
        ('Jak zjistit velikost bot dítěte?',
         '<p>Postavte dítě na papír patou ke zdi, označte konec nejdelšího prstu a změřte vzdálenost. K naměřené délce přičtěte 12 až 17 mm a hledejte botu s takovou vnitřní délkou. Měřte obě nohy a řiďte se delší.</p>'),
        ('Co znamenají dětské velikosti 98, 110 nebo 128?',
         '<p>Jsou to centimetry výšky dítěte. Velikost 110 je pro dítě vysoké zhruba 105 až 110 cm, 128 pro dítě do 128 cm. Řada jde po šesti centimetrech a věk je jen orientační.</p>'),
        ('Co je Mondopoint?',
         '<p>Systém podle normy ISO 9407, který udává délku a šířku chodidla v milimetrech. U lyžařských bot se uvádí délka v centimetrech, například 26,5. Je to nejpřesnější způsob značení, protože vychází z nohy, ne z boty.</p>'),
        ('Mám si koupit lyžáky o číslo větší?',
         '<p>Ne. Lyžařská bota má držet nohu, ve volné botě lyže špatně ovládáte a nohy prochladnou. Vyberte velikost podle délky chodidla a když jste mezi dvěma velikostmi, zkuste obě.</p>'),
        ('Jak si změřit hlavu kvůli velikosti helmy?',
         '<p>Krejčovský metr veďte vodorovně kolem hlavy těsně nad obočím a nad ušima. U mnoha značek odpovídá obvod 55 až 59 cm velikosti M, rozsahy se ale u výrobců liší.</p>'),
        ('Jakou velikost rukavic potřebuji?',
         '<p>Změřte obvod dlaně pod klouby prstů bez palce. Obvod kolem 20 cm odpovídá u pracovních rukavic velikosti 8 (M). Sportovní značky mají vlastní tabulky, proto zkontrolujte tu u konkrétního modelu.</p>'),
        ('Proč mi sedí 42 u jedné značky a 43 u jiné?',
         '<p>Výrobci používají různá kopyta, jinak zaokrouhlují a jinak převádějí čísla mezi systémy. Spolehlivější než číslo je délka v centimetrech z tabulky výrobce, kterou porovnáte se svou naměřenou délkou chodidla.</p>'),
    ],
    cats=['sportovni-obuv', 'tenisky', 'zimni-obuv', 'lyzarske-boty', 'lyzarske-helmy', 'lyzarske-rukavice', 'sportovni-tricka'],
    updated='2026-11-17')
