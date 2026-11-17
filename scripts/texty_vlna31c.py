"""sporteka.cz — wave 31c (17. 11. 2026): long texts for navleky-na-boty, fotbalove-branky, moskytiery, chladici-tasky, via-ferrata.
General true facts only, no prices, no product counts. Brands linked only if present in src/texts/znacky.json or in the wave 31
brand list (salewa), the rest are named as plain text. Products named in the texts exist in the local catalogue copy.

Facts checked (17. 11. 2026):
- Via ferrata: EN 958:2017 was superseded by EN 958:2024 (CEN approval 19. 5. 2024, valid from 1. 7. 2024; evs.ee, iteh.ai,
  DIN); UIAA 128 v4 (2025) follows EN 958:2024. Sets are designed for users of 40–120 kg (Petzl "Via ferrata with a child",
  Edelrid via ferrata shop, Stubai manual, Climbing Technology manual); lighter persons must be belayed with a dynamic rope.
  EN 12275 type K carabiners = self-closing gate for via ferrata (Edelrid/biwak EN 12275 summaries, Singing Rock datasheet).
  Grades: Schall scale A–E (rarely F), Hüsler scale K1–K6; the scales are only roughly comparable (Vaude, Bergfreunde,
  OSM wiki key:via_ferrata_scale, SAC 2020 grade scale PDF). EN 12492 = mountaineering helmets.
- Football goals: full size 7,32 × 2,44 m (Laws of the Game); futsal 3 × 2 m; Czech small-format youth football uses 5 × 2 m goals
  (FAČR "Pravidla fotbalu malých forem" 2016, Pohár mládeže 2025/26 rules: goals must be secured against falling).
  EN 748 and EN 16579 deal with goal stability (NSAI, DIN, FA goalpost safety guidelines). Fatal accidents of children under
  falling goals in CZ (ČT24, Novinky, iPrima — Břeclav, Blansko, Plzeň).
- Mosquito nets: 156 holes per square inch (≈ 24 holes/cm²) is the long-standing minimum for polyester netting
  (WHO prequalification documents, Vestergaard PermaNet spec). Permethrin-treated nets mentioned only as a general fact.
- Food: SZÚ guidance — chilled food at 5 °C or less; ÚVZ SR recommends cooling bags with ice packs for transport;
  a parked car can exceed 50 °C (ČTK report on parcel boxes).
Left out (not verified): exact youth goal sizes for every age group, technical changes between EN 958:2017 and :2024,
hold times of cooling bags, mesh specs of individual products, any health effect of impregnated nets."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ navleky-na-boty
NEW['navleky-na-boty'] = dict(long=True,
    title='Návleky na boty a gamaše: na túry, do sněhu i na kolo',
    desc='Turistické gamaše, návleky do sněhu a nepromokavé návleky na tretry. Jak vybrat výšku, materiál, pásek pod podrážku a velikost a kde je porovnat.',
    intro='<p><strong>Návleky na boty</strong> chrání obuv a spodní část nohy před sněhem, vodou, blátem a kamínky. Pod jedním názvem se skrývají dost rozdílné věci. Turistické gamaše se nosí přes trekové boty a sahají ke kotníku nebo pod koleno. Cyklistické návleky na tretry obepínají celou botu, mají otvor pro zarážku a chrání nohy před větrem a deštěm. Městské nepromokavé návleky se natahují přes běžné boty, když prší cestou do práce.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u vybraného modelu vidíte, kdo ho prodává a v jakých velikostech. Nákup pak proběhne v obchodě, který si zvolíte. Najdete tu například návleky '
          + B(('viking', 'Viking'), ('salewa', 'Salewa'), ('silvini', 'Silvini'), ('shimano', 'Shimano')) +
          ', dále Ferrino, Sea to Summit nebo Rossignol. Kategorie patří pod <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>, návleky na lýtka a kolena pro cyklisty jsou zvlášť mezi <a href="/cyklisticke-navleky/">cyklistickými návleky</a>.</p>',
    guide='<h2>Gamaše, návleky a návleky na tretry: co je co</h2>'
          '<p>Slovo gamaše se v češtině používá hlavně pro turistické a lyžařské návleky, které kryjí horní část boty a holeň. Spodní okraj leží na botě a pod podrážkou je drží pásek nebo lanko. Cyklistické návleky na tretry fungují jinak: obalí celou botu včetně špičky a paty a nechají volné jen místo pro zarážku a patní kolík. Třetí skupinou jsou ochranné návleky do deště pro chodce a městské cyklisty, které připomínají krátkou holínku z tenkého materiálu.</p>'
          + T(['Typ', 'Jak vypadá', 'Kdy se hodí'], [
              ['Nízké turistické gamaše', 'kryjí kotník a horní část boty, často elastický materiál', 'běh v terénu, letní túry, štěrk a jehličí'],
              ['Vysoké gamaše', 'sahají pod koleno, pevná tkanina, zip nebo suchý zip vpředu', 'sníh, rosa ve vysoké trávě, bláto, sněžnice'],
              ['Gamaše s membránou', 'nepromokavý materiál, který pouští vlhkost ven', 'vícedenní túry v mokru a na horách'],
              ['Návleky na tretry', 'obepnou celou botu, otvor pro zarážku, zip vzadu', 'silniční kolo a MTB v chladu a dešti'],
              ['Návleky na špičku', 'kryjí jen přední část tretry', 'chladná rána, kdy celé návleky nejsou potřeba'],
              ['Městské návleky do deště', 'tenký nepromokavý materiál přes běžnou obuv', 'cesta do práce na kole nebo pěšky']]) +
          '<h2>Turistické gamaše: nízké, nebo vysoké</h2>'
          '<p>Nízké gamaše váží málo a hodí se tam, kde nejde o vodu, ale o drobné kamínky, písek a jehličí, které by jinak padaly do bot. Oblíbené jsou u trailových běžců a turistů v nízké obuvi. Neudrží ale hluboký sníh a v mokré trávě promoknou nohavice nad nimi.</p>'
          '<p>Vysoké gamaše jsou zimní a horská klasika. Kryjí celé lýtko, takže sníh nenapadá do bot ani při brodění závějí a kalhoty zůstanou suché i v rosné trávě. Nahoře je stahuje gumička nebo přezka, vpředu se zapínají zipem, suchým zipem nebo kombinací obojího. Zapínání vpředu je pohodlnější, protože se gamaše dají nasadit bez zouvání bot. Ke sněžnicím nebo zimním výstupům se hodí spolu s <a href="/vysoke-trekove-boty/">vysokými trekovými botami</a>, nízké gamaše dávají smysl s <a href="/trekova-obuv/">trekovou obuví</a> do kotníku i pod něj.</p>'
          '<h2>Materiály a nepromokavost</h2>'
          '<ul><li><strong>Odolná nylonová tkanina</strong>, často Cordura nebo podobná, vydrží tření o kameny, kleč a hroty maček. Bývá ve spodní, nejvíc namáhané části.</li>'
          '<li><strong>Membrána</strong>, například Gore-Tex nebo eVent, propouští vodní páru ven a vodu dovnitř nepustí. Hodí se na dlouhé dny v mokru, kdy se noha pod gamaší jinak zapaří.</li>'
          '<li><strong>Softshell a elastické tkaniny</strong> jsou lehké a dobře sedí, ale do vody a mokrého sněhu nestačí.</li>'
          '<li><strong>Neopren</strong> se používá hlavně u cyklistických návleků. Hřeje i ve vlhku, ale nedýchá, takže při delší jízdě v teple se noha potí.</li>'
          '<li><strong>Lycra a tenké aero materiály</strong> jsou na časovky a závody. Snižují odpor vzduchu, proti zimě a dešti pomáhají jen málo.</li></ul>'
          '<p>Žádná gamaše nevydrží celý den v rozbředlém sněhu bez kapky vody uvnitř. Voda proniká přes horní okraj, zip a kolem pásku pod podrážkou. Velký rozdíl dělá, jestli mají kalhoty přes gamaše, nebo jsou zastrčené pod nimi. Na sníh se osvědčuje nechat nohavici přes gamaši, aby voda stékala ven.</p>'
          '<h2>Pásek pod podrážkou a další upevnění</h2>'
          '<p>Turistické gamaše drží na botě třemi prvky. Vpředu je háček, který se zachytí za tkaničky. Dole vede pod podrážkou pásek, lanko nebo řetízek, které brání vyjíždění gamaše nahoru. Nahoře je stahovací gumička nebo přezka. Pásek pod podrážkou se při chůzi po skalách a štěrku opotřebovává nejrychleji, proto se vyplatí model s vyměnitelným páskem. Lanko je tenčí a méně překáží, gumový pásek drží lépe na měkkém sněhu. U bot s výrazným vzorkem zkontrolujte, jestli pásek sedne do prohlubně pod klenbou a nebude se třít o hroty maček.</p>'
          '<h2>Návleky na tretry pro cyklisty</h2>'
          '<p>Silniční tretry jsou plné větracích otvorů a v chladném počasí se nohy rychle podchladí. Návleky na tretry ten problém řeší: přetáhnou se přes botu, dole mají otvor pro zarážku a patu a vzadu se zapínají zipem nebo suchým zipem. Na podzim a v zimě se používají neoprenové modely, na mírný chlad a vítr stačí tenčí softshell nebo zateplená lycra. Do deště existují návleky z nepromokavého materiálu, které ale při dlouhém lijáku také promoknou, protože voda teče po noze shora.</p>'
          '<p>U horských kol se návleky prodřou rychleji, protože podrážka chodí po kamenech a v blátě. Pro MTB proto vybírejte modely s otevřenější spodní částí nebo zesílenou podrážkou. Pokud jezdíte s tretrami SPD, ověřte, že otvor pro zarážku je dost velký. Ke kompletnímu oblečení na kolo patří <a href="/cyklisticka-obuv/">cyklistická obuv</a> a návleky na nohy z kategorie <a href="/cyklisticke-navleky/">cyklistické návleky</a>.</p>'
          '<h2>Návleky do sněhu na lyžování a městské návleky</h2>'
          '<p>Pro přesuny po horském středisku nebo pro rodiče stojící u svahu se prodávají zateplené návleky přes obyčejnou obuv, třeba typu overboot. Nejsou to plnohodnotné zimní boty, ale na krátké přesuny a stání v mrazu pomohou. Městské nepromokavé návleky z tenkého materiálu se složí do batohu a na cestu deštěm přes běžné boty stačí. Pozor na chůzi po mokré dlažbě: hladká podrážka návleku klouže víc než podešev bot.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Turistické gamaše se prodávají ve velikostech S až XL podle čísla bot a někdy i podle obvodu lýtka. Pokud nosíte objemné zimní boty, sáhněte spíš po větší velikosti, aby se gamaše dala dopnout i přes jazyk a tkaničky. Návleky na tretry se vybírají přímo podle čísla tretry, protože musí sedět těsně. Volný návlek se třepí, plandá a při šlapání se posouvá. Úzké nohavice a silná lýtka zase prověří horní okraj, který nesmí škrtit.</p>'
          '<h2>Péče a životnost</h2>'
          '<ul><li>Po túře gamaše opláchněte od bláta a nechte uschnout při pokojové teplotě, ne na topení.</li>'
          '<li>Zip a suchý zip vyčistěte od písku a jehličí, jinak přestanou dobře držet.</li>'
          '<li>Neopren perte ručně ve vlažné vodě a nežehlete.</li>'
          '<li>Když přestane voda perlit, pomůže <a href="/impregnace/">impregnace</a> ve spreji určená pro technické tkaniny.</li>'
          '<li>Opotřebovaný pásek pod podrážkou vyměňte dřív, než praskne v půlce túry.</li></ul>'
          '<h2>Jak gamaše nasadit</h2><p>Nejdřív si obujte a zavažte boty. Gamaši otočte zipem dopředu, háček zachyťte za spodní tkaničku nebo očko a pásek protáhněte pod podrážkou v místě klenby. Pak zapněte zip nebo suchý zip odspodu nahoru a nakonec stáhněte horní okraj, aby nepropouštěl sníh, ale neškrtil lýtko. Pásek pod podrážkou utáhněte jen tolik, aby gamaše nevyjížděla nahoru. Příliš utažený pásek se rychleji prodře a tlačí na botu.</p><p>Gamaše nejsou potřeba na každou túru. Na suché a udržované cesty v létě je zbytečné je nosit, noha se pod nimi víc potí. Vyplatí se v zimě, na jaře při tání, v rosné trávě, v kleči a všude, kde je hodně štěrku nebo písku.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Lehké elastické gamaše na hluboký mokrý sníh.</li>'
          '<li>Nohavice zastrčená pod gamaší, takže voda stéká přímo do boty.</li>'
          '<li>Návleky na tretry o dvě čísla větší, které se při jízdě shrnou ke kotníku.</li>'
          '<li>Neoprenové návleky na teplé jarní ráno, kdy se noha během hodiny zapotí.</li>'
          '<li>Pásek pod podrážkou natažený přes hroty maček.</li></ul>'
          '<p>K návlekům se hodí <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> a do deště <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>. Pro zimní výpravy mrkněte i na <a href="/snezky/">sněžnice</a> a další <a href="/outdoor-doplnky/">outdoorové doplňky</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi gamašemi a návleky na boty?', 'Gamaše kryjí horní část boty a holeň a nosí se hlavně na túry a do sněhu. Návleky na tretry obalí celou botu a slouží cyklistům proti chladu a dešti.'),
        ('Jsou gamaše nepromokavé?', 'Modely s membránou nebo nepromokavou tkaninou ano, elastické běžecké gamaše ne. Voda může stejně proniknout přes horní okraj nebo zip, když jdete dlouho v mokrém sněhu.'),
        ('Nosí se kalhoty přes gamaše, nebo pod ně?', 'Na sníh a do deště je lepší nechat nohavici přes gamaši, aby voda stékala ven. Úzké kalhoty se někdy zastrkují pod gamaši, ale pak hlídejte, ať voda neteče dovnitř.'),
        ('Jak vybrat velikost gamaší?', 'Podle čísla bot a tabulky výrobce, u vysokých gamaší i podle obvodu lýtka. K objemným zimním botám berte spíš větší velikost.'),
        ('Co dělat, když se prodře pásek pod podrážkou?', 'U mnoha gamaší se pásek dá vyměnit za náhradní. Pokud výrobce náhradu nenabízí, poslouží i lanko protažené stejnými očky.'),
        ('Které návleky na tretry na zimu?', 'Neoprenové, které hřejí i ve vlhku. Do deště jsou vhodné nepromokavé modely, na mírný chlad stačí softshell nebo zateplená lycra.'),
        ('Hodí se návleky na tretry na horské kolo?', 'Ano, ale vybírejte model se zesílenou nebo otevřenější spodní částí. Při chůzi po kamenech se běžný návlek rychle prodře.'),
        ('Jak prát neoprenové návleky?', 'Ručně ve vlažné vodě s jemným prostředkem a sušit volně, ne na topení. Před uložením je nechte úplně proschnout.'),
        ('Jsou gamaše potřeba ke sněžnicím?', 'Velmi se hodí, protože v prašanu jinak sníh padá do bot. Na sněžnice volte vysoké gamaše z odolné tkaniny.'),
        ('Kde koupit návleky na boty?', 'Sporteka u každého modelu ukáže nabídky českých e-shopů a velikosti, které mají. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])

# ------------------------------------------------------------------ fotbalove-branky
NEW['fotbalove-branky'] = dict(long=True,
    title='Fotbalové branky: na zahradu, trénink i futsal',
    desc='Pop-up, skládací, hliníkové i ocelové fotbalové branky na zahradu a trénink. Rozměry, síť, ukotvení proti převrácení a nabídky českých e-shopů.',
    intro='<p><strong>Fotbalová branka</strong> se kupuje na zahradu pro děti, na trénink do klubu, na hřiště u školy i na futsal. Výběr sahá od lehkých pop-up branek, které se rozloží za pár vteřin, přes skládací hliníkové rámy až po těžké ocelové branky ve velikostech pro mládežnický fotbal. Liší se rozměrem, materiálem, sítí a hlavně způsobem ukotvení. U každé branky, kterou postavíte, platí jedno pravidlo: musí být zajištěná proti převrácení.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u vybrané branky vidíte, kdo ji prodává a za jakých podmínek. Nákup proběhne v obchodě, který si vyberete. V nabídce jsou mimo jiné branky '
          + B(('merco', 'Merco')) +
          ', Stiga, Hudora, Kensis, Quickplay nebo Oneteam. Kategorie patří do sekce <a href="/fotbal/">fotbal</a>, kde najdete i <a href="/fotbalove-mice/">fotbalové míče</a> a <a href="/brankarske-rukavice/">brankářské rukavice</a>.</p>',
    guide='<h2>Druhy fotbalových branek</h2>'
          + T(['Typ', 'Konstrukce', 'Pro koho'], [
              ['Pop-up branka', 'pružné tyče a síť, sbalí se do kruhu', 'děti na zahradě, rychlá hra v parku, rozcvička'],
              ['Skládací branka', 'tyče z plastu, sklolaminátu nebo hliníku na zacvaknutí', 'zahrada, trénink, přenos v tašce'],
              ['Plastová (PVC) branka', 'trubky spojené kolínky, lehké', 'menší děti, občasná hra'],
              ['Hliníková branka', 'lehký rám, nerezaví, často skládací', 'tréninky, kluby, častější přenášení'],
              ['Ocelová branka', 'těžší rám, lakovaný nebo pozinkovaný', 'pevné umístění na zahradě nebo hřišti'],
              ['Rebounder a střelecká stěna', 'odrazová síť nebo plachta s otvory', 'trénink přihrávek a míření bez spoluhráče']]) +
          '<h2>Rozměry branek</h2>'
          '<p>Velká branka pro dospělý fotbal má podle pravidel vnitřní rozměr 7,32 × 2,44 m. Tak velký rám na běžnou zahradu většinou nepatří a do rukou dětí už vůbec ne. Mládežnický fotbal malých forem hraje v Česku podle pravidel FAČR na branky 5 × 2 m. Futsal se hraje na branky 3 × 2 m a stejný rozměr se často prodává i na zahradu pro větší děti a dospělé hráče.</p>'
          '<p>Na menší zahradu a pro menší děti se nabízejí branky kolem 1,2 až 1,8 m na šířku. Ty jsou lehké a dají se přenášet, ale právě proto potřebují kolíky nebo závaží. Při výběru myslete i na hloubku branky, tedy jak daleko od čáry je zadní rám se sítí. Mělká branka zabere méně místa, hluboká lépe drží míč v síti a je stabilnější.</p>'
          '<h2>Bezpečnost: branku vždy ukotvěte</h2>'
          '<p>Převrácená fotbalová branka může dítě vážně zranit. V Česku i na Slovensku zemřelo pod padající brankou už několik dětí, typicky když se na ni věšely, šplhaly na břevno nebo ji nesly ve skupině. Ocelový rám je těžký a padá dopředu, směrem do hřiště. Proto platí několik pravidel bez výjimky.</p>'
          '<ul><li>Každou branku ukotvěte: zemními kolíky do trávníku, závažím nebo pytli s pískem na zadním rámu, na hřišti pevnými kotvami.</li>'
          '<li>Nikdo se nesmí věšet na břevno ani lézt po rámu, a to ani u malé zahradní branky.</li>'
          '<li>Branku přenášejte jen v dostatečném počtu dospělých a bez dětí v blízkosti.</li>'
          '<li>Pravidelně kontrolujte šrouby, spoje, kolíky a stav rámu. Prasklý plast nebo zkorodovaný svar je důvod branku vyřadit.</li>'
          '<li>Nepoužívanou branku položte na zem nebo ji složte a uklidte.</li></ul>'
          '<p>Stabilitou branek proti převržení se zabývají evropské normy EN 748 a EN 16579. Uvedená norma u výrobku je dobrý signál, ale ukotvení nenahradí. U levných zahradních branek norma často uvedená není, a tím víc záleží na kolících a dohledu dospělého.</p>'
          '<h2>Materiál rámu</h2>'
          '<p>Hliník je lehký a nerezaví, proto se z něj dělají přenosné tréninkové branky pro kluby, které je stěhují po hřišti. Ocel je těžší a tužší, branka díky tomu méně cuká při zásahu míčem a na zahradě vydrží roky. Lakovaný ocelový rám je třeba hlídat: kde se barva odloupne, začne kov rezavět. Pozinkovaná ocel odolává lépe. Plastové a PVC branky jsou nejlehčí a nejlevnější na výrobu, ale na slunci a mrazu stárnou a spoje se časem uvolní. Na jednu sezónu pro malé děti stačí, na tvrdé střely starších hráčů ne.</p>'
          '<p>Pop-up branky mají pružné obruče, které se samy rozevřou. Postavíte je za pár vteřin, ale sbalení vyžaduje trochu cviku. Vítr je snadno odnese, takže kolíky jsou nutnost i u nich.</p>'
          '<h2>Síť a její upevnění</h2>'
          '<p>Síť bývá z polypropylenu nebo polyetylenu. Silnější vlákno vydrží víc zásahů a déle odolává slunci, tenká síť z levných sad se po sezóně venku může začít trhat. Důležitý je i způsob uchycení k rámu. Háčky nebo klipy na rámu drží síť pevně a dovolují ji sundat na zimu, provázky a pásky se snadno povolí. Náhradní sítě se prodávají podle rozměru branky, takže si poznamenejte šířku, výšku i hloubku horní a dolní části.</p>'
          '<h2>Branka na zahradu</h2>'
          '<p>Na zahradu vybírejte branku podle věku dětí a velikosti trávníku. Do branky 3 × 2 m už hrají i dospělí, pro předškoláky je zbytečně velká. Počítejte s tím, že tráva pod brankou a v brankovišti trpí, takže je dobré branku čas od času posunout. Na zimu sundejte síť, ocelový rám ošetřete a plastové díly uložte pod střechu. Na zahradu se dobře hodí i další <a href="/hry-na-zahradu/">hry na zahradu</a>, pro skákání pak <a href="/trampoliny/">trampolíny</a> se sítí.</p>'
          '<h2>Rebounder a střelecká stěna</h2>'
          '<p>Rebounder je napnutá síť v rámu, která vrací míč zpět. Hráč si na něm trénuje přihrávky, převzetí a volleje bez spoluhráče. Střelecká stěna je plachta zavěšená do branky s otvory v rozích a hodí se k tréninku přesné střelby. Obojí funguje na zahradě i na tréninku, rebounder ale potřebuje rovnou plochu a pevné postavení, jinak po silné přihrávce odskočí.</p>'
          '<h2>Na co se dívat při porovnání nabídek</h2>'
          '<ul><li>Vnitřní rozměr a hloubku branky, ne jen název velikosti.</li>'
          '<li>Materiál a tloušťku trubek, u oceli povrchovou úpravu.</li>'
          '<li>Součást balení: síť, kolíky, taška na přenášení, střelecká stěna.</li>'
          '<li>Způsob ukotvení a jestli se dají dokoupit kotvy nebo závaží.</li>'
          '<li>Dostupnost náhradní sítě a dílů.</li>'
          '<li>Zda jde o jednu branku, nebo sadu dvou kusů.</li></ul>'
          '<h2>Jak branku postavit</h2><ul><li>Vyberte rovné místo bez kamenů, s dostatkem prostoru za brankou i po stranách.</li><li>Rám složte podle návodu a dotáhněte všechny spoje. Volný spoj se při zásahu míčem dál uvolňuje.</li><li>Natáhněte síť a upevněte ji po celém obvodu, aby míč neproklouzl spodem.</li><li>Zatlučte kolíky nebo položte závaží na zadní rám. Pak branku zkuste opatrně zatlačit dopředu a ověřte, že se ani nenadzvedne.</li><li>Dětem vysvětlete, že se na branku nevěší a nešplhá po ní.</li></ul><h2>Branka v hale a na umělé trávě</h2><p>Na tvrdém povrchu a na umělém trávníku kolíky nepoužijete. Branky se tam zajišťují závažím, kotvami zabudovanými v podlaze nebo pytli se zátěží. Při nákupu pro halu nebo umělku se proto ptejte, jaké ukotvení výrobce nabízí a zda se dá dokoupit. Lehké přenosné branky pro trénink na umělé trávě bývají hliníkové a mají široký zadní rám, na který se závaží pokládá.</p><h2>Branky pro kluby a školy</h2><p>Kde branky používá hodně dětí a dospělých, nestačí kontrola od oka jednou za rok. Vyplatí se pravidelně procházet stav rámů, sítí a kotev, zapisovat si, kdy byla kontrola provedená, a poškozené branky okamžitě stáhnout z hřiště. Pro hry malých forem se hodí lehké hliníkové branky 5 × 2 m, které se přenášejí podle potřeby tréninku. Přenášet je mají vždy dospělí.</p>'
          '<h2>Branka a trénink brankáře</h2><p>Malý brankář na zahradě potřebuje hlavně měkký dopad a branku, která se nehne, když do tyče narazí. Na pádové nácviky je lepší trávník než udusaná hlína pod brankou. Na tréninku chytání se hodí i střelecká stěna, která zakryje střed branky a nutí střelce mířit do rohů. Brankář si tak zvyká na střely, které letí k tyči. Rukavice vybírejte podle velikosti dlaně, na umělou trávu a tvrdé hřiště s odolnější dlaní.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Branka postavená bez kolíků, protože jsou děti „malé a branka lehká“.</li>'
          '<li>Velká ocelová branka na zahradu pro předškoláky.</li>'
          '<li>Síť ponechaná venku přes zimu i léto bez kontroly.</li>'
          '<li>Pop-up branka na otevřeném prostranství ve větru.</li>'
          '<li>Rozměr branky vybraný bez ohledu na velikost hrací plochy.</li></ul>'
          '<p>K brance doplňte <a href="/fotbalove-mice/">míč</a> v odpovídající velikosti, <a href="/kopacky/">kopačky</a> a pro brankáře <a href="/brankarske-rukavice/">rukavice</a> a <a href="/fotbalove-chranice-a-stulpny/">chrániče</a>. Branky na hokej a florbal jsou v kategorii <a href="/hokejove-puky-a-branky/">puky a branky</a>.</p>',
    faq=[
        ('Jaký rozměr má fotbalová branka?', 'Velká branka pro dospělé má vnitřní rozměr 7,32 × 2,44 m. Mládež v malých formách hraje na branky 5 × 2 m, futsal na 3 × 2 m.'),
        ('Jakou branku koupit na zahradu?', 'Pro menší děti lehkou skládací nebo pop-up branku do šířky kolem 1,8 m. Větší děti a dospělí ocení branku 3 × 2 m, ta ale potřebuje víc místa a pevné ukotvení.'),
        ('Proč se branka musí ukotvit?', 'Neukotvená branka se může převrátit, když se na ni někdo zavěsí nebo do ní narazí. V Česku kvůli tomu zemřelo už několik dětí, proto kotvy a závaží patří ke každé brance.'),
        ('Čím branku ukotvit na trávníku?', 'Zemními kolíky do rámu nebo závažím či pytli s pískem na zadní části. Kolíky po dešti a před hrou zkontrolujte, jestli drží.'),
        ('Je lepší hliníková, nebo ocelová branka?', 'Hliníková je lehčí, nerezaví a snadno se přenáší. Ocelová je těžší a tužší a na zahradě vydrží dlouho, lakovaný rám ale hlídejte proti korozi.'),
        ('Jaká branka na futsal?', 'Futsalová branka má rozměr 3 × 2 m. Na tvrdý povrch v hale se branky zajišťují závažím nebo kotvami určenými pro halu.'),
        ('Co je rebounder?', 'Napnutá síť v rámu, která vrací míč zpět. Slouží k tréninku přihrávek a převzetí míče bez spoluhráče.'),
        ('Kdy vyměnit síť?', 'Když se trhají oka nebo síť ztvrdla a praská na slunci. Náhradní síť vybírejte podle šířky, výšky i hloubky branky.'),
        ('Jak branku uložit přes zimu?', 'Sundejte síť a uložte ji v suchu, plastové díly dejte pod střechu. Ocelový rám zkontrolujte a místa s odloupnutou barvou ošetřete.'),
        ('Kde koupit fotbalovou branku?', 'Sporteka u každé branky ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])

# ------------------------------------------------------------------ moskytiery
NEW['moskytiery'] = dict(long=True,
    title='Moskytiéry na postel, na hlavu, do kempu i na kočárek',
    desc='Cestovní moskytiéry na postel, sítě na hlavu, klobouky s moskytiérou i sítě na kočárek. Tvary, hustota oka, impregnace a nabídky českých e-shopů.',
    intro='<p><strong>Moskytiéra</strong> je jemná síť, která vytvoří fyzickou překážku mezi vámi a komáry, pakomárci a dalším hmyzem. Používá se nad postelí v tropech i na chatě, v kempu kolem spacáku nebo hamaky, přes hlavu na rybách a v bažinách a přes kočárek nebo autosedačku. Funguje jen tehdy, když nemá díry, je správně napnutá a okraje leží pod matrací nebo na zemi.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u vybrané moskytiéry vidíte, kdo ji prodává a v jakém provedení. Nákup proběhne v obchodě, který si vyberete. Najdete tu cestovní sítě značek TravelSafe, Cocoon, Sea to Summit, LifeSystems nebo Brettschneider, sítě na hlavu od Coghlan\'s i levné moskytiéry na postel. Kategorie patří k výpisu <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>, kde jsou i přípravky proti hmyzu.</p>',
    guide='<h2>Tvary moskytiér na postel</h2>'
          '<p>Moskytiéry na spaní se liší hlavně tvarem a počtem bodů, za které se zavěšují. Tvar určuje, kolik je uvnitř místa a jak snadno ji pověsíte v hotelu, na chatě nebo pod stromem.</p>'
          + T(['Tvar', 'Zavěšení', 'Výhody a nevýhody'], [
              ['Krabicová (box)', 'čtyři rohy, někdy šest bodů', 'nejvíc místa uvnitř, potřebuje víc úchytů'],
              ['Zvonová (bell)', 'jeden bod nad středem postele', 'pověsíte ji téměř všude, uvnitř je méně prostoru'],
              ['Klínová a pyramidová', 'jeden nebo dva body, spodní okraj se vypne', 'lehká, pro jednoho, vhodná i ven'],
              ['Samostojná (dome)', 'vlastní tyčky, bez zavěšení', 'postavíte ji kdekoli, je objemnější'],
              ['Síť na hamaku', 'šňůra nad hamakou nebo všitá síť', 'ochrana při spaní venku mezi stromy']]) +
          '<p>Na cesty se nejvíc osvědčuje krabicový tvar, pokud máte kam uchytit čtyři šňůry. Pro jednoho cestovatele s batohem je praktičtější lehká klínová nebo pyramidová síť, kterou lze napnout i mezi dvěma body. Zvonová moskytiéra se hodí tam, kde je jen jeden háček ve stropě. Na doma a na chatu se prodávají velké moskytiéry na postel i s nebesy, které jsou zároveň ozdobou pokoje.</p>'
          '<h2>Hustota oka</h2>'
          '<p>Rozhodující vlastností sítě je velikost ok. U polyesterových moskytiér se dlouho uvádí jako minimum 156 ok na čtvereční palec, přibližně 24 ok na čtvereční centimetr. Taková síť zastaví komáry a zároveň pustí dost vzduchu. Na drobné pakomárce, kteří se protáhnou i hustší sítí, jsou určené jemnější sítě označované jako midge. Čím hustší síť, tím hůř se pod ní ale dýchá v horku, takže do tropů není ideální volit nejjemnější materiál, pokud tam pakomárci nejsou problém.</p>'
          '<p>Materiálem bývá polyester nebo nylon. Nylon je lehčí a sbalí se do menšího objemu, což ocení cestovatelé s malým batohem. Polyester je odolný a levnější. Bavlněné moskytiéry jsou příjemné na dotek, ale těžší a déle schnou.</p>'
          '<h2>Impregnované moskytiéry</h2>'
          '<p>Část moskytiér se prodává napuštěná insekticidem, nejčastěji permetrinem. Účinná látka působí na hmyz, který na síť usedne. Impregnace postupně slábne praním a časem, výrobce proto uvádí, kolik praní a jak dlouhé používání síť snese. S impregnovanou sítí zacházejte podle návodu a po manipulaci se sítí si umyjte ruce. Neimpregnovaná síť funguje jen jako fyzická bariéra, takže hmyz, který dosedne zvenčí, kousne přes síť do kůže, která se jí dotýká.</p>'
          '<h2>Cesty do tropů</h2>'
          '<p>Při cestách do oblastí, kde se vyskytuje malárie, horečka dengue nebo jiné nemoci přenášené komáry, je moskytiéra jen jedním z opatření. Doporučení pro konkrétní zemi, očkování a případnou léčbu dá lékař nebo centrum cestovní medicíny. Navštivte je s předstihem před odjezdem. Moskytiéru s sebou berte i do ubytování, kde ji slibují, protože síť na místě může být děravá nebo krátká.</p>'
          '<h2>Sítě na hlavu a klobouky s moskytiérou</h2>'
          '<p>Síť na hlavu se natáhne přes čepici nebo klobouk a dole se stáhne gumičkou kolem krku. Váží pár desítek gramů a do kapsy se vejde kdykoli. Hodí se rybářům, houbařům, na túry kolem jezer, na Sever nebo do bažin. Klobouk se všitou moskytiérou je pohodlnější, protože síť se nedotýká obličeje. Při výběru sledujte barvu: tmavá síť se lépe prohlíží než bílá, která v protisvětle oslňuje.</p>'
          '<h2>Moskytiéry na kočárek a autosedačku</h2>'
          '<p>Síť na kočárek se natahuje přes celou korbu nebo sportovní sedačku a dole se upevní gumou. Musí sedět tak, aby ji dítě nemohlo stáhnout k sobě a aby mezi sítí a obličejem zůstal prostor. Na univerzální modely se podívejte, jestli jsou určené pro váš typ kočárku. Moskytiéry se prodávají i na přívěsné vozíky za kolo, ty najdete u <a href="/cyklo-sedacky-a-voziky/">cyklosedaček a vozíků</a>. Pod síť dítě nenechávejte bez dozoru a v horku hlídejte, aby se pod ní nepřehřálo.</p>'
          '<h2>Moskytiéry do kempu</h2>'
          '<p>Moderní <a href="/turisticke-stany/">turistické stany</a> mají moskytiéru ve vchodu vestavěnou. Samostatná síť se hodí pro spaní pod širákem, pod plachtou nebo na verandě chaty. Pro spaní v lese existují hamaky se všitou moskytiérou nebo samostatné sítě, které se natáhnou přes <a href="/hamaky/">hamaku</a>. Pod síť se do teplých nocí hodí lehký <a href="/spaci-pytle/">spacák</a> nebo jen <a href="/vlozky-do-spacaku/">vložka do spacáku</a>.</p>'
          '<h2>Jak moskytiéru pověsit</h2>'
          '<ul><li>Do cestovní sady patří šňůry, háčky a někdy lepicí úchyty nebo hřebíčky. Ověřte, co balení obsahuje.</li>'
          '<li>Spodní okraj zastrčte pod matraci, ne jen na ni položte.</li>'
          '<li>Síť nesmí ležet na těle, jinak komár kousne skrz.</li>'
          '<li>Před spaním zkontrolujte, jestli uvnitř nezůstal komár, a vchod vždy zavřete.</li>'
          '<li>Na otevřený oheň a svíčky pozor: síť z umělých vláken snadno chytne.</li></ul>'
          '<h2>Péče a opravy</h2>'
          '<p>Moskytiéru perte šetrně ručně a sušte ve stínu, protože UV záření syntetická vlákna časem oslabuje. Malé díry spravíte záplatou nebo lepicí páskou na sítě, větší trhliny sešijte. I jedna díra o velikosti nehtu stačí, aby komár našel cestu dovnitř. Do batohu síť balte do obalu, aby se nezachytila o přezky a zipy.</p>'
          '<h2>Velikost moskytiéry podle postele</h2><p>Moskytiéra musí být větší než postel, aby se okraje daly zastrčit pod matraci. Krabicová síť pro jednoho bývá užší, pro dva lidi vybírejte dvojitou velikost s rozměrem podle šířky manželské postele. U zvonové moskytiéry rozhoduje obvod spodního okraje a výška zavěšení. Když ji pověsíte příliš nízko, nedosáhne dolů, když příliš vysoko, okraje se nedají zastrčit. Do hamaky a pod širák se dělají sítě pro jednoho v protáhlém tvaru, které se zavěšují za šňůru nad hlavou a nohama.</p><h2>Hmotnost a balení</h2><p>Cestovní moskytiéry z tenkého nylonu váží jen pár set gramů a sbalí se do obalu velikosti láhve. Větší krabicové sítě pro dva a moskytiéry na postel na chatu jsou těžší, ale do batohu se na cesty stále vejdou. Pokud často měníte ubytování, vyplatí se síť, kterou zvládnete pověsit za pár minut a ráno rychle sbalit. Šňůry, háčky a záplaty držte přímo v obalu sítě, aby se neztratily.</p><h2>Sítě do oken a dveří</h2><p>Na chatu nebo do obytného auta se prodávají i síťové závěsy do dveří, které se uprostřed spojují magnety. Projdete jimi bez rukou a po průchodu se samy zavřou. Okenní sítě se lepí suchým zipem do rámu. Ty ale patří spíš do domácnosti než na cesty a výběr je v obchodech s bytovými doplňky.</p>'
          '<h2>Moskytiéra a repelent</h2><p>Moskytiéra chrání ve chvíli, kdy pod ní ležíte nebo sedíte. Večer u ohně, při procházce za šera nebo na rybách mimo síť pomáhá vhodné oblečení s dlouhým rukávem a nohavicemi a repelent. Repelenty se liší účinnou látkou, dobou působení a vhodností pro děti. Vždy si přečtěte etiketu a řiďte se pokyny výrobce, u malých dětí a v těhotenství se poraďte s lékařem nebo lékárníkem. Oblečení v barvách khaki a olivové se v přírodě hodí, světlé oblečení zase usnadní všimnout si klíšťat.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Zvonová moskytiéra na dvojlůžko, pod kterou se dva lidé nevejdou.</li>'
          '<li>Krátká síť, která nedosáhne pod matraci.</li>'
          '<li>Jemná síť proti pakomárcům do tropického horka bez větru.</li>'
          '<li>Spoléhání jen na moskytiéru při cestě do oblasti s malárií bez porady s lékařem.</li>'
          '<li>Cestovní síť bez šňůr a háčků, které pak na místě chybí.</li></ul>'
          '<p>Doplňkem moskytiéry jsou repelenty ve výpisu <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>. Na cesty se hodí <a href="/cestovni-tasky/">cestovní tašky</a> a drobnosti z kategorie <a href="/kempingove-doplnky/">kempingové doplňky</a>.</p>',
    faq=[
        ('Jakou moskytiéru na cesty?', 'Pro jednoho lehkou klínovou nebo krabicovou síť z nylonu, která se sbalí do malého obalu. Ověřte, že balení obsahuje šňůry a háčky.'),
        ('Jaký je rozdíl mezi krabicovou a zvonovou moskytiérou?', 'Krabicová se věší za čtyři rohy a uvnitř je víc místa. Zvonová potřebuje jen jeden bod nad postelí, ale prostor uvnitř je menší.'),
        ('Jak hustá má síť být?', 'Na komáry se jako minimum uvádí kolem 156 ok na čtvereční palec. Na drobné pakomárce jsou určené jemnější sítě, pod kterými se ale v horku hůř dýchá.'),
        ('Co je impregnovaná moskytiéra?', 'Síť napuštěná insekticidem, nejčastěji permetrinem, který působí na hmyz při dosednutí. Impregnace slábne praním a časem, řiďte se návodem výrobce.'),
        ('Stačí moskytiéra při cestě do tropů?', 'Je to jen jedno z opatření. Doporučení pro danou zemi, očkování a další ochranu vám před odjezdem řekne lékař nebo centrum cestovní medicíny.'),
        ('Jak pověsit moskytiéru v hotelu bez háčku?', 'Pomohou lepicí úchyty, šňůra natažená mezi skříní a oknem nebo samostojná moskytiéra s vlastními tyčkami.'),
        ('Jakou síť na kočárek?', 'Takovou, která pasuje na váš typ kočárku, dole se pevně stáhne a nedotýká se obličeje dítěte. V horku hlídejte, aby se dítě pod sítí nepřehřálo.'),
        ('Je lepší síť na hlavu, nebo klobouk s moskytiérou?', 'Síť na hlavu je lehčí a vejde se do kapsy. Klobouk s moskytiérou drží síť dál od obličeje, takže se v něm lépe vidí a dýchá.'),
        ('Jak opravit díru v moskytiéře?', 'Malou díru přelepte záplatou nebo páskou na sítě, větší trhlinu sešijte. Komárovi stačí i malý otvor.'),
        ('Kde koupit moskytiéru?', 'Sporteka u každé moskytiéry ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])

# ------------------------------------------------------------------ chladici-tasky
NEW['chladici-tasky'] = dict(long=True,
    title='Chladicí tašky a termotašky na piknik, výlet i oběd',
    desc='Chladicí tašky, termotašky, chladicí batohy a obědové tašky na jídlo. Jak vybrat objem a izolaci, jak používat chladicí vložky a kde porovnat nabídky.',
    intro='<p><strong>Chladicí taška</strong> je měkká izolovaná taška, ve které vydrží jídlo a pití déle studené. Na rozdíl od pevného chladicího boxu je lehčí, po vyprázdnění se dá složit a nosí se přes rameno nebo na zádech. Prodává se ve velikostech od malé obědové termotašky do práce a do školy přes tašky na piknik a na pláž až po velké rodinné tašky na dovolenou autem. Sama taška nechladí, jen zpomaluje ohřívání. Chlad dodají chladicí vložky nebo zmražené nápoje.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u vybrané tašky vidíte, kdo ji prodává a za jakých podmínek. Nákup proběhne v obchodě, který si vyberete. Najdete tu tašky '
          + B(('merco', 'Merco')) +
          ', Thermos, Outwell, Campingaz, Nils, Spokey, Tatonka nebo Reisenthel. Pevné boxy a elektrické chladničky jsou ve vedlejší kategorii <a href="/chladici-boxy/">chladicí boxy</a>.</p>',
    guide='<h2>Druhy chladicích tašek</h2>'
          + T(['Typ', 'Jak vypadá', 'Kdy se hodí'], [
              ['Obědová termotaška', 'malá taška na jeden až dva boxy s jídlem', 'do práce, do školy, na výlet s dětmi'],
              ['Chladicí taška přes rameno', 'měkká taška se zipem a popruhem', 'piknik, pláž, nákup v létě'],
              ['Chladicí batoh', 'izolovaná komora, ramenní popruhy', 'pěší výlet, kolo, festival'],
              ['Skládací taška', 'po vyprázdnění se složí naplocho', 'nákupy, cesta autem, malý byt'],
              ['Taška na kolečkách', 'velký objem, výsuvná rukojeť', 'dovolená autem, kemp, rodinný piknik'],
              ['Pevný chladicí box', 'tvrdá skořepina, silnější izolace', 'několik dní v kempu, rybaření']]) +
          '<h2>Jak velkou tašku vybrat</h2>'
          '<p>Objem se uvádí v litrech. Na oběd do práce stačí malá taška na jeden nebo dva boxy. Na piknik pro dva se hodí střední velikost, rodina na celý den u vody ocení větší tašku. Při výběru počítejte s tím, že chladicí vložky zaberou část místa. Lépe chladí taška plná než poloprázdná, protože vzduch uvnitř se ohřívá rychleji než studené potraviny. Pokud tašku nosíte pěšky, myslete na váhu: velká naplněná taška přes rameno se po kilometru pěkně pronese a lepší je pak chladicí batoh.</p>'
          '<h2>Izolace a konstrukce</h2>'
          '<p>Chladicí tašky mají mezi vnějším a vnitřním materiálem vrstvu pěny. Silnější izolace udrží chlad déle, ale taška je objemnější a těžší. Vnitřek bývá z omyvatelné fólie nebo plastu. Svařené švy uvnitř nepropustí vodu z tajícího ledu, prošívané švy mohou časem prosakovat. Důležitý je zip: čím těsněji víko doléhá, tím méně teplého vzduchu se dostane dovnitř. Někdy je víko zateplené zvlášť, protože teplo přichází hlavně shora od slunce.</p>'
          '<ul><li>Malá vnější kapsa se hodí na příbory, ubrousky a klíče, aby se nemusela otevírat hlavní komora.</li>'
          '<li>Pevné dno udrží tvar a taška se nepřevrátí s lahvemi uvnitř.</li>'
          '<li>Světlá vnější barva se na slunci ohřívá méně než tmavá.</li>'
          '<li>Vyjímatelná vnitřní vložka se snadno umyje.</li></ul>'
          '<h2>Jak dlouho chladicí taška chladí</h2>'
          '<p>Na tuto otázku neexistuje jedno číslo. Výsledek závisí na izolaci, venkovní teplotě, slunci, množství chladicích vložek a tom, jak často tašku otevíráte. Měkká taška chladí kratší dobu než pevný box se silnými stěnami, je tedy určená spíš na den než na několik dní. Výrobci někdy dobu chlazení uvádějí, berte ji ale jako údaj z jejich vlastních podmínek.</p>'
          '<p>Hodně pomůže pár jednoduchých kroků. Tašku nechte před cestou chvíli vychladit s vložkou uvnitř. Do tašky dávejte už vychlazené potraviny a nápoje, nikdy teplé. Vložky rozmístěte nahoru i dolů, protože studený vzduch klesá. Tašku stavte do stínu a v autě ji nenechávejte na slunci, kde může být uvnitř přes 50 °C. Otevírejte ji co nejméně.</p>'
          '<h2>Chladicí vložky</h2>'
          '<p>Chladicí vložky jsou plastové nádobky s gelem nebo kapalinou, které se předem zmrazí v mrazáku. Kolik hodin mají v mrazáku být, uvádí výrobce, obvykle je nejjistější nechat je tam přes noc. Ploché vložky se dobře zasunou mezi potraviny, větší kostky vydrží déle. Místo vložky lze použít i zmraženou lahev s vodou, která po roztátí poslouží jako pití. Led v sáčku chladí dobře, ale tající voda pak stojí na dně tašky.</p>'
          '<h2>Termotaška na teplé jídlo</h2>'
          '<p>Izolace funguje oběma směry, takže termotaška udrží chvíli teplé i teplé jídlo. Hodí se na oběd do práce nebo pro výlet s dětmi. Na delší dobu je lepší dát teplé jídlo do termoboxu nebo termosky, protože taška teplo udrží jen krátce. Termosky a jídelní termoboxy najdete mezi <a href="/lahve-a-termosky/">lahvemi a termoskami</a>, kávu na cestu udrží <a href="/termohrnky/">termohrnky</a>. Teplé a studené jídlo nedávejte do jedné tašky, navzájem se ohřejí a ochladí.</p>'
          '<h2>Bezpečnost potravin v létě</h2>'
          '<p>Chlazené potraviny se v ledničce skladují při teplotě do 5 °C, jak doporučuje Státní zdravotní ústav. V chladicí tašce se k tomu dostanete jen se dostatkem vložek a s vychlazeným obsahem. Nejvíc pozornosti zaslouží rychle se kazící potraviny: maso, ryby, uzeniny, mléčné výrobky, majonézové saláty a vajíčka. Syrové maso na gril balte zvlášť do uzavřené nádoby, aby šťáva nekapala na ostatní jídlo. Pokud se jídlo v tašce za horkého dne ohřálo, nevracejte ho večer do ledničky a raději ho vyhoďte.</p>'
          '<h2>Čištění a uložení</h2>'
          '<ul><li>Po každém použití tašku vytřete vlhkým hadříkem s trochou saponátu a vypláchněte čistou vodou.</li>'
          '<li>Nechte ji schnout otevřenou, jinak začne zapáchat a plesnivět.</li>'
          '<li>Do pračky ji dávejte jen tehdy, když to výrobce výslovně povoluje.</li>'
          '<li>Pach od ryb nebo mléka zmírní vytření roztokem jedlé sody.</li>'
          '<li>Uložte ji v suchu a nemačkejte ji pod těžkými věcmi, aby se izolace nedeformovala.</li></ul>'
          '<h2>Chladicí taška na kolo a k vodě</h2><p>Na kolo se hodí chladicí batoh nebo malá taška, kterou připnete na nosič. Velká taška přes rameno na kole houpe a přetěžuje jedno rameno. Pro vodu a pláž jsou dobré tašky s vodotěsným dnem a omyvatelným povrchem, ze kterého jde snadno setřít písek. Na lodi nebo na pádlování je chladicí taška zranitelná, protože do ní může natéct voda zipem. Proto ji dejte do lodního vaku nebo k jídlu použijte lodní barel.</p><h2>Chladicí tašky pro rybáře</h2><p>Rybářské chladicí tašky se používají na návnady i na jídlo pro celodenní a noční výpravy. Mají často odolnější vnější materiál, víc kapes a tmavou barvu, ve které nejsou vidět skvrny. Návnady a jídlo uchovávejte v oddělených nádobách nebo rovnou v různých taškách. Vnitřek po každé výpravě vymyjte, rybí pach se jinak do pěny nasaje.</p><h2>Taška na jídlo pro děti</h2><p>Dětská termotaška do školy a školky bývá malá, lehká a s veselým potiskem. Vybírejte takovou, kterou dítě samo otevře, a vnitřek, který jde rychle vytřít. Svačinu s jogurtem nebo sýrem doplňte malou chladicí vložkou, zvlášť v teplých měsících. Na tašku napište jméno, ve třídě jich bývá několik stejných.</p><h2>Na co se dívat při porovnání nabídek</h2><ul><li>Objem v litrech a vnější rozměry, aby se taška vešla do auta nebo kufru kola.</li><li>Tloušťka izolace a jestli má zateplené i víko.</li><li>Svařené, nebo prošívané vnitřní švy.</li><li>Způsob nošení: popruh přes rameno, batoh, rukojeť a kolečka.</li><li>Zda jsou v balení chladicí vložky, nebo je musíte dokoupit.</li></ul>'
          '<h2>Jak chladicí tašku sbalit</h2><p>Na dno položte jednu chladicí vložku a na ni nejvíc zkazitelné potraviny, tedy maso, sýr a jogurty. Nad ně dejte nápoje a ovoce a navrch druhou vložku. Křehké věci jako pečivo a zeleninu ukládejte nahoru, aby je nezmačkaly lahve. Volná místa vyplňte, ať se obsah nepřelévá. Věci, které budete potřebovat jako první, dejte co nejvýš, abyste nemuseli tašku dlouho prohrabávat s otevřeným víkem.</p><h2>Chladicí taška na nákup</h2><p>V létě se skládací chladicí taška hodí i na nákup, zvlášť když cesta z obchodu domů trvá déle nebo nakupujete před dalším vyřizováním. Mražené a chlazené zboží dávejte do tašky až na konci nákupu a doma ho ukládejte jako první. Skládací tašku si nechte v autě nebo v kufru kola, ať ji máte po ruce.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Teplé potraviny v chladicí tašce s jednou malou vložkou.</li>'
          '<li>Taška ponechaná v autě na slunci během koupání.</li>'
          '<li>Poloprázdná taška, ve které je víc vzduchu než jídla.</li>'
          '<li>Neustálé otevírání kvůli jednomu nápoji.</li>'
          '<li>Měkká taška na několikadenní pobyt v kempu, kam patří spíš pevný box.</li></ul>'
          '<p>Na piknik doplňte <a href="/piknikove-deky/">piknikovou deku</a>, k vodě <a href="/plazove-doplnky/">plážové doplňky</a> a do kempu <a href="/kempingove-nadobi/">kempingové nádobí</a> a výbavu na <a href="/vareni-v-prirode/">vaření v přírodě</a>. Další vybavení je v sekci <a href="/kemping/">kemping</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi chladicí taškou a chladicím boxem?', 'Taška je měkká, lehká a dá se složit, chladí ale kratší dobu. Pevný box má silnější izolaci a hodí se na delší pobyty.'),
        ('Jak dlouho vydrží jídlo v chladicí tašce studené?', 'Záleží na izolaci, teplotě venku, slunci a počtu chladicích vložek. Měkká taška je určená spíš na jeden den, údaj výrobce berte jako orientační.'),
        ('Kolik chladicích vložek potřebuji?', 'Tolik, aby byly nahoře i dole a obklopily potraviny. Do větší tašky na celý den se vyplatí dvě a víc.'),
        ('Jak dlouho mrazit chladicí vložky?', 'Podle návodu výrobce, nejjistější je nechat je v mrazáku přes noc. Částečně zmražená vložka chladí krátce.'),
        ('Udrží termotaška jídlo teplé?', 'Krátce ano, izolace funguje oběma směry. Na delší dobu je lepší termobox nebo termoska na jídlo.'),
        ('Jakou tašku na oběd do práce?', 'Malou obědovou termotašku na jeden až dva boxy s plochou chladicí vložkou. Vnitřek by měl jít snadno umýt.'),
        ('Co nedávat do chladicí tašky?', 'Teplé jídlo spolu se studeným a syrové maso bez uzavřené nádoby. Rychle se kazící potraviny držte co nejblíž u vložek.'),
        ('Jak vyčistit chladicí tašku?', 'Vytřete ji hadříkem se saponátem, vypláchněte a nechte schnout otevřenou. Na pach pomůže roztok jedlé sody.'),
        ('Je chladicí batoh lepší než taška přes rameno?', 'Na pěší výlet a kolo ano, protože váha je rozložená na obě ramena. Na krátký přesun z auta na pláž stačí taška.'),
        ('Kde koupit chladicí tašku?', 'Sporteka u každé tašky ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])

# ------------------------------------------------------------------ via-ferrata
NEW['via-ferrata'] = dict(long=True,
    title='Via ferrata: ferratové sety, tlumiče pádu a rukavice',
    desc='Ferratové sety s tlumičem pádu, karabiny, sedáky a rukavice na via ferraty. Co říká norma EN 958, jak set kontrolovat a kdy ho vyřadit.',
    intro='<p><strong>Via ferrata</strong>, česky ferrata nebo zajištěná cesta, je horská trasa jištěná ocelovým lanem, kramlemi a žebříky. Lezec se k lanu cvaká ferratovým setem, tedy dvěma rameny s karabinami a tlumičem pádu. Tlumič je nutný, protože pád na ferratě končí až na nejbližší kotvě lana a síla rázu bez tlumení by byla obrovská. K setu patří sedák, přilba a rukavice, na ferraty se chodí v pevné obuvi s dobrou podrážkou.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů, takže u vybraného setu nebo rukavic vidíte, kdo je prodává. Nákup proběhne v obchodě, který si vyberete. Ferratové vybavení tu mají značky '
          + B(('salewa', 'Salewa')) +
          ', Edelrid, Camp, Ocún, Petzl nebo Black Diamond. Kategorie patří do sekce <a href="/horolezectvi/">horolezectví</a>. Sedáky jsou ve výpisu <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky a pomůcky</a>, samostatné karabiny a lana mezi <a href="/lezecka-lana-a-karabiny/">lezeckými lany a karabinami</a>.</p>',
    guide='<h2>Co na ferratu potřebujete</h2>'
          + T(['Vybavení', 'K čemu slouží', 'Na co se dívat'], [
              ['Ferratový set', 'spojuje sedák s lanem a tlumí pád', 'norma EN 958, hmotnostní rozsah, otočná spojka'],
              ['Sedák', 'nese set a rozloží sílu při pádu', 'lezecký nebo ferratový sedák, správná velikost'],
              ['Přilba', 'chrání hlavu před kameny a při pádu', 'horolezecká přilba podle EN 12492'],
              ['Rukavice', 'chrání dlaně před ocelovým lanem', 'kůže na dlani, dobrý úchop'],
              ['Obuv', 'drží na skále a stupech', 'pevná podrážka s dobrým třením'],
              ['Batoh', 'nese vodu, vrstvu proti dešti a svačinu', 'malý objem, nic nevisí ven']]) +
          '<h2>Jak funguje ferratový set</h2>'
          '<p>Set má dvě ramena zakončená karabinami. Při postupu je vždy aspoň jedna karabina zacvaknutá v laně, při přecvakávání na kotvě se nejdřív přepne jedna karabina a pak druhá. Ramena bývají elastická, aby se nepletla pod nohama. Obě ramena vedou do tlumiče pádu, který se připíná k sedáku. Většina současných setů používá textilní tlumič: popruh je složený a prošitý tak, že se při pádu postupně párá a pohltí energii. Na trhu jsou i tlumiče s kovovou brzdnou destičkou, kterou prokluzuje lano.</p>'
          '<p>Mnoho setů má otočnou spojku, takzvaný swivel. Ten brání tomu, aby se ramena při přecvakávání a otáčení zamotala. Pohodlí to zvyšuje hodně, zvlášť na dlouhých trasách s mnoha kotvami.</p>'
          '<h2>Karabiny typu K</h2>'
          '<p>Karabiny ferratového setu odpovídají normě EN 12275 jako typ K. Mají zámek, který se po zacvaknutí sám zavře a zajistí, a velké rozevření, aby obemkly lano i kotvy. Ovládají se jednou rukou. U některých modelů se zámek odjišťuje stiskem v dlani, jiné mají tlačítko nebo otočnou objímku. Před nákupem si zámek vyzkoušejte v rukavici, pokud to jde, protože tisíckrát opakovaný pohyb musí jít snadno.</p>'
          '<h2>Norma EN 958 a hmotnost uživatele</h2>'
          '<p>Ferratové sety se vyrábějí podle evropské normy EN 958. Vydání z roku 2017 bylo v roce 2024 nahrazeno novým vydáním. Set vyrobený podle starší verze kvůli tomu není automaticky nutné měnit, rozhoduje návod výrobce a stav setu. Sety jsou podle výrobců určené pro uživatele s hmotností zhruba od 40 do 120 kg. Jak přesně se hmotnost počítá a zda zahrnuje výbavu, uvádí návod ke konkrétnímu setu.</p>'
          '<p>Děti a lehčí lidé pod 40 kg nemají dost váhy, aby tlumič při pádu fungoval správně. Výrobci jako Petzl a Edelrid proto uvádějí, že je musí navíc jistit dospělý dynamickým lanem shora. Lano má zachytit případný pád dřív než set. Pokud jdete na ferratu s dítětem bez zkušenosti s jištěním lanem, je rozumné vzít horského vůdce nebo instruktora.</p>'
          '<h2>Kontrola setu a kdy ho vyřadit</h2>'
          '<ul><li>Po pádu, při kterém se tlumič roztrhl nebo aktivoval, set vyřaďte. Tlumič je na jedno použití.</li>'
          '<li>Před každou túrou zkontrolujte, že obal tlumiče je celý a švy nejsou natržené.</li>'
          '<li>Karabiny se musí samy zavřít a zajistit. Pomalý nebo drhnoucí zámek je důvod k výměně.</li>'
          '<li>Ramena prohlédněte, zda nejsou prodřená, natavená nebo jinak poškozená.</li>'
          '<li>Maximální životnost a podmínky skladování určuje výrobce v návodu.</li>'
          '<li>U staršího nebo bazarového setu ověřte, zda se na model nevztahuje svolávací akce.</li></ul>'
          '<p>Set skladujte v suchu, mimo slunce a daleko od chemikálií, zejména kyselin z autobaterií. Mokrý set nechte uschnout volně, ne na topení.</p>'
          '<h2>Sedák, přilba a obuv</h2>'
          '<p>Ke ferratovému setu je nutný sedák. Postačí běžný lezecký sedák, existují i lehké sedáky stavěné přímo pro ferraty. Velikost musí sedět přes oblečení, které budete mít na sobě. Přilba je na ferratě povinná výbava: z výšky padají kameny shozené lezci nad vámi a hlava může narazit do skály i při malém zakopnutí. Vybírejte horolezeckou přilbu podle normy EN 12492, cyklistická helma na to určená není. Na nohy se hodí <a href="/nizke-trekove-boty/">nízké trekové boty</a> s tužší podrážkou nebo přístupové boty. Na lehké lezecké pasáže si někteří berou <a href="/lezecke-boty/">lezečky</a>, na ferraty je ale většina lidí nepotřebuje.</p>'
          '<h2>Rukavice na ferraty</h2>'
          '<p>Ocelové lano se při celodenním držení zarývá do dlaní a jeho vlákna mohou kůži poškrábat. Ferratové rukavice mají dlaň z kůže nebo odolné syntetiky a hřbet z prodyšného materiálu. Rukavice s odstřiženými prsty dovolí lépe cítit stupy a ovládat karabiny, celoprsté chrání víc a hodí se do chladu. Rukavice by měly mít poutko nebo karabinku na připnutí k sedáku. Obecnější výběr je mezi <a href="/sportovni-rukavice/">sportovními rukavicemi</a>.</p>'
          '<h2>Obtížnost ferrat</h2>'
          '<p>V Alpách se obtížnost ferrat nejčastěji značí podle dvou stupnic. Schallova stupnice používá písmena od A (lehká) do E (extrémně obtížná), výjimečně se uvádí i F. Hüslerova stupnice, rozšířená ve Švýcarsku a Německu, má stupně K1 až K6. Obě stupnice se dají porovnat jen přibližně a každý průvodce je může vykládat trochu jinak. Začátečníci by měli začít na cestách stupně A až B, kde jsou dobré stupy a málo převislých míst.</p>'
          '<h2>Bezpečnost na ferratě</h2>'
          '<ul><li>Začátečníci by měli první ferraty absolvovat s horským vůdcem, v kurzu nebo se zkušeným kamarádem.</li>'
          '<li>Mezi dvěma kotvami lana má být vždy jen jeden člověk, aby při pádu nestrhl dalšího.</li>'
          '<li>Při hrozící bouřce na ferratu nevstupujte. Ocelové lano a žebříky vedou blesk.</li>'
          '<li>Počítejte s časem na sestup a únavou, na dlouhých cestách nemusí být úniková možnost.</li>'
          '<li>Sledujte, kdo leze nad vámi, a nestůjte pod nimi v linii padajících kamenů.</li></ul>'
          '<h2>Jak se na ferratě postupuje</h2><p>Na ferratě se nahoru dostáváte hlavně nohama, lano a kramle slouží rukám k udržení rovnováhy. Kdo celou cestu táhne rukama, brzy unaví předloktí. Na každé kotvě přepněte nejprve jednu karabinu za kotvu, teprve potom druhou, a nikdy neodepínejte obě najednou. Na žebřících a strmých úsecích držte tělo blízko skály. Odpočívat můžete na místech s dobrým stupem, nikoli zavěšení za set, který k tomu není určený. Pro odpočinek se používá samostatná odsedávací smyčka, kterou některé sety obsahují.</p><h2>Půjčit, nebo koupit</h2><p>Ve vyhledávaných alpských oblastech se ferratové vybavení dá půjčit v půjčovnách a horských školách. Na první zkušenost to stačí. Kdo chodí na ferraty pravidelně, ocení vlastní set, protože zná jeho historii a ví, že nikdy nezachytil pád. U půjčeného setu se o tom můžete jen spolehnout na půjčovnu. Vlastní sedák a rukavice padnou lépe než půjčené.</p><h2>Na co se dívat při porovnání nabídek</h2><ul><li>Norma EN 958 a hmotnostní rozsah uvedený výrobcem.</li><li>Typ tlumiče a jestli má set otočnou spojku.</li><li>Ovládání karabin jednou rukou v rukavici.</li><li>Hmotnost a délka ramen vzhledem k vaší výšce.</li><li>Zda jde jen o set, nebo o komplet se sedákem a přilbou.</li></ul>'
          '<h2>Oblečení na ferratu</h2><p>Na ferraty se oblékejte jako na horskou túru: funkční triko, pružné kalhoty, které neomezují krok, a v batohu větrovka nebo nepromokavá bunda. Ve skále bývá v létě horko, ve stínu a na hřebeni ale rychle zima. Volné oblečení a dlouhé popruhy batohu se mohou zachytit o kramle, proto je stáhněte. Dlouhé vlasy mějte pod přilbou nebo svázané.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Půjčení dítěti do 40 kg setu bez jištění lanem.</li>'
          '<li>Další používání setu po pádu, při kterém se tlumič roztrhl.</li>'
          '<li>Samostatná lonž nebo smyčka bez tlumiče místo ferratového setu.</li>'
          '<li>Výstup bez přilby, protože jde „jen o lehkou ferratu“.</li>'
          '<li>Volba cesty podle fotky, ne podle obtížnosti a délky.</li></ul>'
          '<p>Na celodenní túru vezměte malý <a href="/turisticke-batohy/">turistický batoh</a> s vodou a bundou. Další horolezecké vybavení najdete v sekci <a href="/horolezectvi/">horolezectví</a>.</p>',
    faq=[
        ('Co je ferratový set?', 'Dvě ramena s karabinami a tlumič pádu, který se připíná k sedáku. Spojuje lezce s ocelovým lanem a při pádu tlumí ráz.'),
        ('Podle jaké normy se ferratové sety vyrábějí?', 'Podle evropské normy EN 958. Vydání z roku 2017 bylo v roce 2024 nahrazeno novým, o použitelnosti konkrétního setu rozhoduje návod a jeho stav.'),
        ('Pro jakou hmotnost jsou ferratové sety?', 'Výrobci je určují zhruba pro uživatele od 40 do 120 kg. Přesný rozsah a to, zda zahrnuje výbavu, najdete v návodu.'),
        ('Může dítě na ferratu s běžným setem?', 'Dítě pod 40 kg musí dospělý navíc jistit dynamickým lanem shora. Samotný set by jeho pád nezatlumil správně.'),
        ('Kdy ferratový set vyřadit?', 'Po pádu, při kterém se tlumič roztrhl, při poškození ramen nebo když se karabiny samy nezavírají. Maximální životnost uvádí výrobce.'),
        ('K čemu je otočná spojka na setu?', 'Brání zamotání ramen při přecvakávání a otáčení. Na dlouhých cestách výrazně zvyšuje pohodlí.'),
        ('Potřebuji na ferratu přilbu?', 'Ano. Hrozí padající kameny i náraz hlavou do skály, vybírejte horolezeckou přilbu podle normy EN 12492.'),
        ('Jaké rukavice na ferratu?', 'S dlaní z kůže nebo odolné syntetiky, která vydrží tření o ocelové lano. Bez prstů pro lepší cit, celoprsté do chladu.'),
        ('Jak se značí obtížnost ferrat?', 'Nejčastěji Schallovou stupnicí A až E (výjimečně F) nebo Hüslerovou stupnicí K1 až K6. Začátečníci by měli začít na cestách A až B.'),
        ('Kde koupit ferratový set?', 'Sporteka u každého setu ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])
