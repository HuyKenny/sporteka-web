"""sporteka.cz — wave 31b (17. 11. 2026): long texts for prosivane-bundy, nepromokave-kalhoty, snowboardove-bundy,
snowboardove-kalhoty. General true facts only, no prices, no product counts, no norms.

Facts checked against:
- water column (mm) and breathability (g/m2/24 h), 10K/20K meaning, seam taping:
  uk.oneill.com/blogs/all/water-columns-breathability-ski-jackets-pants-explained, jans.com waterproof ratings guide,
  ridestore.com/mag/waterproof-ratings-and-breathability-explained (breathability figure is for the membrane only)
- 2L / 2.5L / 3L construction: rei.com/learn/expert-advice/rainwear-how-it-works, evo.com outerwear construction guide,
  absolute-snow.co.uk 2/2.5/3-layer guide
- care and DWR reactivation (warm tumble or warm iron through a cloth, spray or wash-in re-proofing):
  gore-tex.com/support/care/outerwear, evo.com Gore-Tex care guide
- down fill power (volume of one ounce of down after lofting), sewn-through vs box-baffle cold spots:
  alpineascents.com Down 101, mountainwarehouse.com down jacket guide
- down washing (front loader, down wash, low heat drying with balls): gearjunkie.com, fieldmag.com, nike.com guides
- RECCO (passive reflector, detector carried by rescue teams, no replacement for a transceiver):
  burton.com RECCO blog, marmot.com/ReccoTechnology.html, jack-wolfskin.com/recco
RECCO named only for models whose catalogue names state it (Siroko W5, O'Neill Gtx Recco).
Left out (not verified or not generalisable): exact EU vs US fill-power conversion, EN 343 classes, which brands
offer jacket-to-pant powder-skirt interfaces or growth systems in kids' pants (described generically).
Brands linked only if present in src/texts/znacky.json or the wave 31 brand list, the rest are plain text."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ prosivane-bundy
NEW['prosivane-bundy'] = dict(long=True,
    title='Prošívané bundy dámské, pánské i dětské: péřové i syntetické',
    desc='Prošívané bundy s péřovou nebo syntetickou výplní pro dámy, pány i děti. Jak vybrat výplň, prošití, střih a velikost a jak bundu správně prát.',
    intro='<p><strong>Prošívaná bunda</strong> drží výplň v komorách, které vznikají prošitím vnější a vnitřní látky. Péří ani syntetická vata se tak nesesype do spodní části a bunda hřeje rovnoměrně po celé ploše. Anglicky se jí říká puffer, česky často „péřovka“, i když spousta prošívaných bund žádné peří nemá. Najdete mezi nimi tenké přechodové modely, které se sbalí do vlastní kapsy, sportovní bundy do hor i dlouhé zimní kabáty s kapucí do města.</p>'
          '<p>Sporteka řadí nabídky českých e-shopů vedle sebe, takže u vybraného modelu hned vidíte, který obchod ho má a v jakých velikostech. Nákup dokončíte přímo u prodejce. Hodně prošívaných bund mají '
          + B(('trespass', 'Trespass'), ('regatta', 'Regatta'), ('dare2b', 'Dare2b'), ('helly-hansen', 'Helly Hansen'), ('columbia', 'Columbia'), ('the-north-face', 'The North Face')) +
          '. Kategorie patří pod <a href="/zimni-bundy/">zimní bundy</a>, výběr pro ženy shrnuje stránka <a href="/damska-prosivana-bunda/">dámská prošívaná bunda</a> a čistě péřové modely najdete mezi <a href="/perove-bundy/">péřovými bundami</a>.</p>',
    guide='<h2>Péří, nebo syntetická výplň</h2>'
          '<p>O tom, jak bunda hřeje, rozhoduje hlavně výplň. Přírodní peří (kachní nebo husí) má nejlepší poměr tepla a hmotnosti. Dá se silně stlačit, a když se bunda rozbalí, zase nabere objem. Jeho slabinou je voda: mokré peří se slepí do chuchvalců, ztratí objem a s ním i většinu izolační schopnosti. Schne navíc pomalu.</p>'
          '<p>Syntetická výplň je z polyesterových vláken. V názvech bund se objevují obchodní označení jako PrimaLoft, mnoho výrobců ale používá vlastní nebo nepojmenovanou vatu. Syntetika si udrží část hřejivosti i ve vlhku, rychleji schne a snáz se pere. Na stejné teplo je ale o něco těžší a objemnější a po letech nošení a praní postupně ztrácí pružnost. Hybridní bundy kombinují obojí: peří na trupu, kde hřeje nejvíc, a syntetiku na ramenou, v podpaží nebo na manžetách, kde se bunda nejčastěji namočí nebo zapotí.</p>'
          + T(['Výplň', 'Silné stránky', 'Slabší stránky', 'Kam se hodí'], [
              ['Péří (prachové peří s podílem per)', 'nejvíc tepla na gram, dobře se sbalí, dlouhá životnost při dobré péči', 've vlhku ztrácí objem, pomalu schne, náročnější praní', 'suchý mráz, město, přestávky na horách pod nepromokavou vrstvou'],
              ['Syntetická vata', 'hřeje i mírně vlhká, rychle schne, snadná údržba', 'těžší a objemnější na stejné teplo, časem se slehne', 'mokrá zima, děti, aktivní pohyb, časté praní'],
              ['Hybridní bunda', 'peří tam, kde hřeje, syntetika tam, kde se bunda namáhá', 'složitější výrobek, péči určuje štítek', 'turistika, skialpové přestávky, proměnlivé počasí'],
              ['Tenká přechodová prošívaná bunda', 'lehká, sbalitelná, nosí se i jako mezivrstva', 'na tuhý mráz sama nestačí', 'jaro, podzim, vrstva pod bundu do deště']]) +
          '<h2>Plnivost a poměr peří: co znamenají čísla</h2>'
          '<p>U péřových bund se často uvádějí dva údaje. Prvním je poměr prachového peří a per, například 90/10 nebo 80/20. První číslo udává podíl jemného prachového peří, které hřeje nejvíc, druhé podíl drobných per, která výplni dodávají pružnost. Čím vyšší podíl prachového peří, tím je výplň lehčí a objemnější.</p>'
          '<p>Druhým údajem je plnivost (fill power), uváděná v jednotkách cuin. Říká, jaký objem zaujme jedna unce peří poté, co se ve zkušebním válci nadýchá. Vyšší číslo znamená, že stejné množství peří vytvoří víc izolující vzduchové vrstvy. Pozor ale na zjednodušení: o teple bundy rozhoduje i to, kolik peří v ní celkem je. Bunda s menším množstvím kvalitnějšího peří může hřát méně než bunda s větším množstvím peří o nižší plnivosti, jen bude lehčí. Výsledky se navíc liší podle metody měření, proto čísla srovnávejte spíš v rámci jedné značky. Někteří výrobci uvádějí i certifikaci původu peří, například RDS (Responsible Down Standard), která se týká zacházení se zvířaty.</p>'
          '<h2>Prošití: průchozí šev, nebo komory s přepážkami</h2>'
          '<p>Nejběžnější je takzvané průchozí prošití (sewn-through). Šev spojí vnější a vnitřní látku napřímo, takže v linii švu není žádná výplň. Na těchto místech bunda hřeje méně a v silném větru jimi může táhnout chlad. Výroba je jednodušší a bunda vychází lehčí, proto tuto konstrukci mají skoro všechny městské a přechodové modely.</p>'
          '<p>Teplejší bundy na velký mráz bývají šité do komor s přepážkami (box wall nebo box baffle). Mezi vnější a vnitřní látkou je proužek tkaniny, který vytvoří trojrozměrnou komoru, a výplň v ní má plnou výšku i v místě švu. Bunda je o něco těžší a dražší na výrobu, ale chladná místa na švech odpadají. Některé moderní bundy mají komory místo šití svařené nebo lepené; tím ubude dírek po jehle, kterými může prolézat peří.</p>'
          '<p>Na vzhled má vliv i šířka komor. Úzké vodorovné pruhy působí sportovně a bunda je tenčí, široké komory dávají výplni víc prostoru a bunda vypadá i hřeje „nafouknutěji“. Svislé nebo kosočtvercové prošití je spíš otázka střihu a módy.</p>'
          '<h2>Teplo versus hmotnost</h2>'
          '<p>Nejteplejší bunda není vždy ta nejlepší. Když se hodně hýbete, třeba při rychlé chůzi do kopce nebo běhu na autobus, silná péřovka vás přehřeje a pod ní se zapotíte. Vlhkost pak zevnitř zhoršuje izolaci. Na aktivní pohyb proto volte tenčí bundu a teplou vrstvu přidejte, až zastavíte. Lehká sbalitelná prošívaná bunda se v batohu skoro neprojeví a na vrcholu nebo při přestávce ji oceníte víc než cokoli jiného.</p>'
          '<p>Na stání venku, čekání na zastávce nebo procházku s kočárkem při mrazu je naopak správná volba objemná bunda s vysokým límcem a kapucí. K vrstvení se hodí i <a href="/sportovni-vesty/">sportovní vesty</a> s prošívanou výplní, které zahřejí trup a nechají volné ruce, a <a href="/fleecove-mikiny/">fleecové mikiny</a> pod bundu.</p>'
          '<h2>Do města, nebo na hory</h2>'
          '<p>Většina prošívaných bund má vnější látku jen s vodoodpudivou úpravou. Krátký déšť nebo sníh vydrží, při delším dešti ale voda proteče švy, kterými je prošitá výplň. Pokud bunda nemá výslovně uvedenou nepromokavou membránu a podlepené švy, nepočítejte s ní do lijáku. Na hory se prošívaná bunda nosí hlavně jako teplá vrstva pod nepromokavou <a href="/nepromokave-bundy/">bundu do deště</a> nebo přes ni na přestávkách. Na sjezdovku je lepší sáhnout po <a href="/lyzarske-bundy/">lyžařské bundě</a>, která má sněžný pás, kapsu na skipas a odolnější látku.</p>'
          '<p>Do města rozhoduje délka a střih. Bunda do pasu je praktická na kolo a do auta, delší model zakryje bedra a sedá se v něm na studenou lavičku. Dlouhé prošívané kabáty mají často zip i zespodu, aby se v nich dalo pohodlně chodit a sedat.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Prošívaná bunda má sedět tak, aby se pod ní vešla mikina nebo svetr a výplň přitom nebyla stlačená. Příliš těsná bunda hřeje méně, protože stlačené peří nemá objem. Zkuste zvednout ruce nad hlavu: rukávy by neměly vyjet nad zápěstí a lem se nemá vytáhnout až nad pas. Kapuce má jít stáhnout tak, aby se při otočení hlavy neotáčela s vámi a nezakrývala výhled.</p>'
          '<p>Velikosti se mezi značkami liší a některé modely jsou šité úžeji, jiné vyloženě oversize. Vždy se podívejte do tabulky velikostí konkrétního výrobce a porovnejte obvod hrudníku a délku rukávu se svými mírami. Dětskou bundu kupte s rezervou na vrstvu pod ní, ale ne o několik čísel větší. Volnými rukávy a lemem pak dovnitř proudí studený vzduch. U dětí se vyplatí reflexní prvky a kapuce, která jde odepnout.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Postup vždy určuje štítek. U péřové bundy obecně platí: zapnout zipy, prát v pračce s předním plněním na šetrný program a nízkou teplotu, s pracím prostředkem určeným pro peří a bez aviváže. Prášek a aviváž zanechávají v peří zbytky, po kterých se slepuje. Pomůže extra máchání.</p>'
          '<p>Nejdůležitější je sušení. Pokud štítek sušičku dovoluje, sušte na nízkou teplotu a přidejte do bubnu dvě tři sušicí nebo tenisové míčky, které rozbíjejí shluky peří. Sušení trvá dlouho a bunda musí proschnout úplně, jinak může zatuchnout. Bez sušičky ji nechte rozloženou a během dne ji opakovaně protřepte a prohněťte chuchvalce. Syntetické bundy jsou méně choulostivé, i u nich ale aviváž škodí. Po praní lze vnější látce obnovit vodoodpudivost přípravkem z kategorie <a href="/impregnace/">impregnace</a>.</p>'
          '<p>Přes léto bundu neskladujte dlouho stlačenou v obalu. Pověste ji na ramínko nebo uložte volně, ať si výplň udrží objem. Když z látky vyleze pírko, nevytahujte ho, ale zkuste ho z druhé strany vtáhnout zpět. Vytažením se otvor jen zvětší.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Spoléhat na prošívanou bundu bez membrány jako na ochranu před deštěm.</li>'
          '<li>Kupovat co nejteplejší model na aktivní pohyb, ve kterém se pak potíte.</li>'
          '<li>Srovnávat jen plnivost bez ohledu na množství výplně a konstrukci prošití.</li>'
          '<li>Vybrat těsnou velikost, ve které je výplň pod svetrem stlačená.</li>'
          '<li>Prát péřovou bundu s aviváží a sušit ji jen napůl.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Stejný model se v obchodech často liší barvou, kódem varianty nebo rokem kolekce. Než se rozhodnete, zkontrolujte u nabídky typ výplně, poměr peří, délku bundy a materiál vnější látky. Pokud si nejste jistí velikostí, vybírejte obchod, u kterého je vrácení zboží jednoduché. K prošívané bundě se hodí <a href="/termopradlo/">termoprádlo</a> na chladné dny a pro děti stránka <a href="/detska-zimni-bunda/">dětská zimní bunda</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi prošívanou a péřovou bundou?', 'Prošívaná bunda je pojem pro konstrukci, kdy je výplň zašitá do komor. Péřová bunda je prošívaná bunda s výplní z peří. Prošívaná bunda může mít i syntetickou výplň.'),
        ('Je lepší péří, nebo syntetika?', 'Péří hřeje víc na stejnou hmotnost a dobře se sbalí. Syntetika lépe snáší vlhko, rychleji schne a snáz se pere. Do suchého mrazu je silnější peří, do mokré zimy a pro děti syntetika.'),
        ('Co znamená plnivost 600 nebo 800 cuin?', 'Je to objem, který zaujme jedna unce peří po nadýchání. Vyšší číslo znamená lehčí a objemnější izolaci. Teplo bundy ale určuje i celkové množství výplně.'),
        ('Je prošívaná bunda nepromokavá?', 'Většinou ne. Má vodoodpudivou úpravu, která vydrží krátký déšť nebo sníh, ale švy vodu propustí. Nepromokavá je jen bunda s membránou a podlepenými švy.'),
        ('Co je box wall konstrukce?', 'Komory oddělené proužkem tkaniny, takže výplň má plnou výšku i v místě švu. Bunda tak nemá chladná místa na prošití. Bývá teplejší, ale těžší a dražší.'),
        ('Jak vyprat péřovou bundu?', 'Podle štítku, obvykle na šetrný program s prostředkem na peří a bez aviváže. Pak ji důkladně usušte, ideálně v sušičce na nízkou teplotu se sušicími míčky.'),
        ('Jakou velikost prošívané bundy zvolit?', 'Takovou, pod kterou se vejde mikina, aniž by se výplň stlačila. Zkontrolujte tabulku výrobce a délku rukávů se zvednutými pažemi.'),
        ('Hodí se prošívaná bunda na lyže?', 'Na krátké lyžování v suchém mrazu ano, ale lyžařská bunda má sněžný pás, kapsu na skipas a odolnější nepromokavou látku. Prošívaná bunda se dá nosit jako teplá vrstva pod skořepinu.'),
        ('Proč z bundy lezou pírka?', 'Drobná pírka prostupují látkou nebo dírkami po jehle, hlavně u nových bund. Nevytahujte je, zkuste je vtáhnout zpět z vnitřní strany.'),
        ('Kde koupit prošívanou bundu?', 'Sporteka u každé bundy ukáže nabídky českých e-shopů včetně velikostí. Nákup dokončíte v obchodě, jehož nabídku si vyberete.'),
    ])

# ------------------------------------------------------------------ nepromokave-kalhoty
NEW['nepromokave-kalhoty'] = dict(long=True,
    title='Nepromokavé kalhoty do deště: dámské, pánské i dětské',
    desc='Nepromokavé kalhoty s membránou, svrchní kalhoty do deště i dětské kalhoty do bláta. Vodní sloupec, prodyšnost, podlepené švy a boční zipy.',
    intro='<p><strong>Nepromokavé kalhoty</strong> chrání nohy před deštěm, mokrou trávou, sněhem i blátem. Patří do nich technické kalhoty s membránou na turistiku a skialpinismus, lehké svrchní kalhoty, které se natáhnou přes běžné kalhoty, když začne pršet, i dětské kalhoty do deště na hřiště a do školky. Každý typ funguje jinak: membránové kalhoty propouštějí část vodní páry ven, pogumované nepropustí vodu ani páru.</p>'
          '<p>Na Sportece porovnáte nabídky nepromokavých kalhot z českých obchodů a u každého modelu vidíte, kdo ho prodává a v jakých velikostech. Nakupuje se pak přímo v e-shopu. Mezi značkami jsou '
          + B(('regatta', 'Regatta'), ('trespass', 'Trespass'), ('dynafit', 'Dynafit'), ('fjallraven', 'Fjällräven'), ('helly-hansen', 'Helly Hansen'), ('northfinder', 'Northfinder'), ('kilpi', 'Kilpi'), ('reima', 'Reima')) +
          ', dále Vaude, Didriksons nebo <a href="/znacka/salewa/">Salewa</a>. K nim se hodí <a href="/nepromokave-bundy/">nepromokavé bundy</a>, širší výběr do terénu nabízejí <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>.</p>',
    guide='<h2>Typy nepromokavých kalhot</h2>'
          '<p>Nejdřív si ujasněte, k čemu kalhoty potřebujete. Turista, který chodí v horách celý den, chce jiné kalhoty než rodič, který na podzim stojí s dětmi na hřišti, nebo rybář, který sedí na mokrém břehu.</p>'
          + T(['Typ', 'Jak jsou postavené', 'Pro koho'], [
              ['Membránové kalhoty (hardshell)', 'vnější látka, membrána a vnitřní vrstva, podlepené švy, často zipy na nohavicích', 'turistika, vysokohorská turistika, skialpinismus'],
              ['Svrchní kalhoty do deště', 'lehké, sbalitelné, natahují se přes jiné kalhoty, boční zipy', 'turistika s nejistým počasím, cyklisté, cesta do práce'],
              ['Zateplené nepromokavé kalhoty', 'membrána nebo zátěr plus podšívka či výplň', 'zimní stání venku, rybaření, práce na zahradě'],
              ['Kalhoty s laclem do deště', 'vysoký předek i záda, kšandy, často zesílená kolena', 'rybáři, práce venku, děti'],
              ['Dětské kalhoty do deště a bláta', 'pogumovaná nebo PU látka, svařené švy, pásek pod chodidlo', 'školka, hřiště, louže']]) +
          '<p>Membránové modely typicky nesou zkratku GTX nebo Gore-Tex, případně vlastní membránu výrobce. Membrána je tenká vrstva, která nepropustí kapky vody, ale molekuly vodní páry ano. Pogumované a PU kalhoty bez membrány jsou naopak úplně uzavřené, takže pod nimi se při pohybu člověk zpotí. Na hraní v blátě a krátké stání to ale nevadí.</p>'
          '<h2>Vodní sloupec: co číslo v milimetrech znamená</h2>'
          '<p>Nepromokavost se vyjadřuje vodním sloupcem v milimetrech. Při zkoušce se na látku tlačí sloupec vody a měří se výška, při které začne voda prosakovat. Údaj 10 000 mm (často zkráceně 10K) znamená, že látka vydrží tlak deseti metrů vody. U kalhot je to důležitější než u bundy. Při klečení, sezení na mokrém kameni nebo pod popruhy batohu působí na látku mnohem vyšší tlak než padající déšť, a kde nestačí bundě nižší číslo, tam kalhoty na kolenou proteknou.</p>'
          '<p>Hodnota platí pro samotnou látku. Výsledná nepromokavost kalhot záleží i na švech, zipech a střihu. Kalhoty s vysokým číslem a nepodlepenými švy propustí vodu dřív než model s nižším číslem a pečlivě podlepenými švy. Ve specifikacích se vyplatí hledat obojí.</p>'
          '<h2>Prodyšnost: proč se pod membránou přesto potíte</h2>'
          '<p>Prodyšnost se obvykle udává v gramech vodní páry, které projdou čtverečním metrem látky za 24 hodin (g/m²/24 h). Vyšší číslo je lepší. Někteří výrobci uvádějí hodnotu RET, u které platí opak: čím nižší číslo, tím lépe látka dýchá. Obě čísla se měří na membráně nebo látce v laboratoři, ne na hotových kalhotách při výstupu do kopce.</p>'
          '<p>V praxi prodyšnost klesá, když vnější látka nasákne vodou. Proto mají membránové kalhoty na povrchu vodoodpudivou úpravu (DWR), díky které voda tvoří kapky a stéká. Při velké zátěži v teplém dešti nestačí žádná membrána a trochu vlhkosti pod kalhotami zůstane. Pomůže otevřít větrací zipy na stehnech a pod kalhoty vzít funkční vrstvu místo bavlny.</p>'
          '<h2>2L, 2,5L a 3L: z kolika vrstev je látka</h2>'
          '<ul><li><strong>Dvouvrstvá (2L)</strong> látka má membránu spojenou s vnější tkaninou a uvnitř volně visící podšívku, často síťovinu. Je příjemná na kůži, ale objemnější a těžší.</li>'
          '<li><strong>Dvouapůlvrstvá (2,5L)</strong> má místo podšívky na membráně jen tenký ochranný nástřik nebo potisk. Je nejlehčí a nejlépe se sbalí, proto ji mají lehké svrchní kalhoty do deště. Obvykle hůř dýchá a je méně odolná vůči oděru.</li>'
          '<li><strong>Třívrstvá (3L)</strong> látka má membránu zalaminovanou mezi vnější a vnitřní tkaninu. Je nejodolnější a nic se v ní neposouvá, proto ji mají kalhoty do vysokých hor a na skialpy. Bývá tužší a dražší.</li></ul>'
          '<h2>Švy, zipy a nohavice</h2>'
          '<p>Každý šev je místo, kde jehla propíchne membránu. Nepromokavé kalhoty proto mají švy zevnitř přelepené páskou, případně svařené. U levnějších modelů bývají podlepené jen ty nejexponovanější švy, u kvalitnějších všechny. Zipy jsou buď s vodoodpudivým nánosem, nebo kryté légou.</p>'
          '<p>U svrchních kalhot do deště hraje velkou roli boční zip. Krátký zip u kotníku pomůže při oblékání, zip po celé délce nohavice umožní natáhnout kalhoty přes pohorky bez zouvání a kalhoty se dají rozepnout i jako větrání. Spodní lem má jít zúžit suchým zipem nebo patentkou, aby nepřekážel a nenabíral bláto. Na trekové modely lze připnout i <a href="/navleky-na-boty/">návleky na boty</a>, které uzavřou mezeru mezi kalhotami a botou.</p>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Svrchní kalhoty se nosí přes jiné kalhoty, takže potřebují víc místa v sedu a na stehnech. Vyzkoušejte je s tím, co pod nimi budete nosit, a udělejte dřep a vysoký krok jako do schodu. Kalhoty nesmí v klíně táhnout a nohavice mají zakrýt horní okraj boty i při ohnutém koleni. Tvarovaná kolena a klínek v rozkroku usnadní chůzi do kopce.</p>'
          '<p>U membránových kalhot, které se nosí samostatně, rozhoduje pas. Pružný pas s poutky na opasek nebo stahováním sedí na různé postavy, kšandy a lacl udrží kalhoty na místě i pod batohem. Délku volte podle bot, se kterými budete chodit: u vysokých trekových bot můžou být nohavice o kousek kratší než u nízké obuvi.</p>'
          '<h2>Dětské kalhoty do deště</h2>'
          '<p>Děti potřebují kalhoty, které vydrží klečení v kalužích a klouzání po mokré skluzavce. Nejčastější jsou kalhoty z PU nebo pogumované tkaniny se svařenými švy, které jsou úplně nepromokavé. Kšandy zabrání tomu, aby se kalhoty při hraní stahovaly, a pásek pod chodidlem drží nohavici přes holínku. Pro chladné dny jsou modely s fleecovou podšívkou, v teple je lepší tenká verze a pod ní běžné oblečení.</p>'
          '<p>Kupujte velikost s malou rezervou, aby se dala obléct přes tepláky a obout <a href="/holinky/">holínky</a>. Reflexní prvky ocení každý, kdo chodí s dětmi v listopadu za šera. Kalhoty po bahnitém dni stačí opláchnout vodou a nechat uschnout, praní v pračce snášejí podle štítku.</p>'
          '<h2>Péče a obnova impregnace</h2>'
          '<p>Membránu nejvíc poškozuje špína, pot a opalovací krémy, které ucpávají póry a ničí vodoodpudivou úpravu. Kalhoty proto občas vyperte podle štítku: zapnout zipy, tekutý prací prostředek, žádná aviváž ani bělidlo a důkladné máchání. Výrobci membrán obvykle doporučují po usušení obnovit úpravu teplem, tedy krátce v sušičce na mírnou teplotu nebo vyžehlit na nízký stupeň přes látku, pokud to štítek dovoluje.</p>'
          '<p>Když voda na povrchu přestane tvořit kapky ani po vyprání a prohřátí, přichází na řadu nová úprava. Použijte sprej nebo přípravek do pračky z kategorie <a href="/impregnace/">impregnace</a> a postupujte podle návodu. Nasáklá vnější látka ještě neznamená, že membrána teče. Kalhoty jsou ale pak studené a těžké a hůř odvádějí páru.</p>'
          '<h2>Na kolo, běh a k vodě</h2>'
          '<p>Běžci a cyklisté potřebují kalhoty co nejlehčí a s užší nohavicí, aby nezachytávala o řetěz nebo o druhou nohu. Běžecké nepromokavé kalhoty bývají z tenké 2,5vrstvé látky a sbalí se do malé kapsy. Na kolo se hodí reflexní prvky a vyšší zadní díl, který kryje bedra v předklonu. Více střihů na kolo najdete mezi <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistickými kalhotami</a>.</p>'
          '<p>Rybáři a lidé, kteří dlouho stojí nebo sedí venku, sahají po zateplených kalhotách nebo po modelech s laclem, které kryjí i ledviny. Tam není prodyšnost tak důležitá jako teplo a odolnost látky. Další výbavu k vodě nabízí kategorie <a href="/rybarske-obleceni/">rybářské oblečení</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Svrchní kalhoty bez bočních zipů pro někoho, kdo je chce oblékat v pohorkách.</li>'
          '<li>Spoléhat na vodní sloupec a nezkontrolovat podlepení švů.</li>'
          '<li>Prát membránu s aviváží nebo práškem.</li>'
          '<li>Nosit pod kalhoty do deště bavlněné tepláky, které nasáknou potem.</li>'
          '<li>Koupit dětem kalhoty bez kšand nebo pásku pod chodidlo.</li></ul>'
          '<p>Na suché dny a mírný déšť vystačí <a href="/softshellove-kalhoty/">softshellové kalhoty</a>, na sníh a sjezdovku <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a> a na kolo nebo dlouhé čekání v dešti i <a href="/plastenky/">pláštěnky</a>.</p>',
    faq=[
        ('Jaký vodní sloupec mají mít nepromokavé kalhoty?', 'Na turistiku je rozumné hledat kalhoty s membránou a podlepenými švy, číslo kolem 10 000 mm a víc. Kolena a sed se při klečení a sezení namáhají víc než bunda, proto se vyšší hodnota u kalhot vyplatí.'),
        ('Co znamená 10K/10K?', 'První číslo je vodní sloupec v milimetrech, druhé prodyšnost v gramech páry na metr čtvereční za 24 hodin. Obě hodnoty platí pro látku, ne pro hotové kalhoty.'),
        ('Jaký je rozdíl mezi 2L, 2,5L a 3L?', '2L má volnou podšívku, 2,5L tenký nástřik místo podšívky a je nejlehčí, 3L má membránu zalaminovanou mezi dvě tkaniny a je nejodolnější.'),
        ('Proč jsou důležité boční zipy?', 'Umožní natáhnout svrchní kalhoty přes boty bez zouvání a slouží i k větrání. Zip po celé délce nohavice je nejpraktičtější.'),
        ('Jakou velikost svrchních kalhot do deště vzít?', 'Takovou, která se pohodlně vejde přes kalhoty, které pod nimi nosíte. Zkuste dřep a vysoký krok, nic nesmí táhnout.'),
        ('Dýchají dětské kalhoty do deště?', 'Pogumované a PU kalhoty nedýchají, zato jsou úplně nepromokavé. Na hřiště a do louží to nevadí, na delší pochody jsou lepší membránové.'),
        ('Proč mi kalhoty promokají na kolenou?', 'Klečení a tlak batohu nebo sedačky vytlačí vodu i přes látku s nižším vodním sloupcem. Promočení může způsobit i opotřebovaná membrána nebo poškozený šev.'),
        ('Jak obnovit nepromokavost kalhot?', 'Vyperte je tekutým prostředkem bez aviváže, usušte a prohřejte podle štítku. Když voda dál nesteká v kapkách, naneste novou impregnaci sprejem nebo v pračce.'),
        ('Můžu nepromokavé kalhoty prát v pračce?', 'Většinou ano, podle štítku. Zapněte zipy, použijte tekutý prostředek a vynechte aviváž a bělidlo.'),
        ('Kde koupit nepromokavé kalhoty?', 'Sporteka ukáže nabídky českých e-shopů u každého modelu. Nákup proběhne v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ snowboardove-bundy
NEW['snowboardove-bundy'] = dict(long=True,
    title='Snowboardové bundy: dámské, pánské i dětské bundy na prkno',
    desc='Snowboardové bundy volnějšího střihu se sněžným pásem a kapucí přes helmu. Co znamená 10K a 20K, zateplení, větrání a kapsa na skipas.',
    intro='<p><strong>Snowboardová bunda</strong> je zimní bunda na prkno, která musí vydržet pády do sněhu, sezení na svahu i celý den v mrazu a větru. Od běžné zimní bundy se liší nepromokavou látkou s podlepenými švy, sněžným pásem a kapucí, která se vejde přes helmu. Hledáte-li bundu na snowboard, uvidíte, že střih bývá volnější a delší než u lyžařských bund. Mnoho modelů výrobci označují jako lyžařské i snowboardové zároveň.</p>'
          '<p>Sporteka sbírá nabídky českých obchodů, takže u každé bundy vidíte, kde je k dispozici a ve kterých velikostech, a nakoupíte přímo v e-shopu. Nejvíc modelů mají '
          + B(('roxy', 'Roxy'), ('o-neill', "O'Neill"), ('siroko', 'Siroko'), ('horsefeathers', 'Horsefeathers'), ('salomon', 'Salomon'), ('rossignol', 'Rossignol')) +
          ', dále Protest, Quiksilver nebo Fundango. Ke kompletní výbavě patří <a href="/snowboardove-kalhoty/">snowboardové kalhoty</a>, celou sekci najdete pod <a href="/snowboarding/">snowboarding</a>.</p>',
    guide='<h2>Čím se snowboardová bunda liší od lyžařské</h2>'
          '<p>Zásadní rozdíl je ve střihu. Snowboardista stojí bokem, často si sedá do sněhu, aby si zapnul vázání, a při jízdě rotuje trupem. Bunda proto bývá volnější a delší, aby zakryla bedra i při předklonu a sezení. Lyžařské bundy jsou obvykle přiléhavější a kratší, protože lyžař stojí čelem ke svahu a chce, aby oblečení nevlálo ve vyšší rychlosti. Snowboardové bundy mají také častěji volnější vzhled s velkou kapucí a výraznými barvami.</p>'
          + T(['Vlastnost', 'Snowboardová bunda', 'Lyžařská bunda'], [
              ['Střih', 'volnější, prostor pro vrstvy a chrániče', 'přiléhavější, užší v pase'],
              ['Délka', 'delší, kryje bedra i při sezení', 'kratší, do pasu nebo lehce pod něj'],
              ['Kapuce', 'velká, přes helmu', 'často menší nebo odepínací'],
              ['Vzhled', 'volnější styl, výrazné barvy a vzory', 'sportovní střih, užší linie'],
              ['Výbava', 'sněžný pás, kapsa na skipas, větrání', 'obdobná výbava, často i zateplení']]) +
          '<p>Rozdíl není dogma. Bunda s označením lyžařská/snowboardová poslouží na obojí a na lyže se klidně dá jet i ve volnější bundě. Rozhoduje, aby se v ní dobře hýbalo a nikde netáhla. Pro srovnání se podívejte i do kategorie <a href="/lyzarske-bundy/">lyžařské bundy</a>.</p>'
          '<h2>Co znamenají údaje 10K, 15K a 20K</h2>'
          '<p>U snowboardových bund se nepromokavost a prodyšnost často zapisují zkratkou, například 10K/10K nebo 10K/7K. První číslo je vodní sloupec v milimetrech, tedy tlak vody, který látka vydrží, než začne prosakovat. 10K znamená 10 000 mm. Druhé číslo je prodyšnost v gramech vodní páry na metr čtvereční za 24 hodin. Čím vyšší, tím víc potu látka odvede.</p>'
          '<ul><li><strong>Kolem 5K</strong> stačí na občasné lyžování za suchého a mrazivého počasí.</li>'
          '<li><strong>10K</strong> je běžný standard na sjezdovku v typické zimě.</li>'
          '<li><strong>15K–20K a víc</strong> se vyplatí do mokrého sněhu, na jarní firn a pro ty, kdo jezdí hodně dní nebo mimo upravené tratě.</li></ul>'
          '<p>Čísla nejsou všechno. Údaj platí pro látku, ne pro hotovou bundu, a bunda s vyšším číslem a nepodlepenými švy může protéct dřív než model s nižším číslem a celoplošně podlepenými švy. U dražších modelů se setkáte s membránou Gore-Tex nebo vlastní membránou výrobce.</p>'
          '<h2>Zateplená bunda, nebo skořepina</h2>'
          '<p>Zateplená snowboardová bunda má mezi vnější látkou a podšívkou syntetickou výplň. Výrobci někdy uvádějí její gramáž. Je to nejjednodušší volba pro začátečníky a rodiny: oblečete termoprádlo, mikinu a bundu a jste připravení. V teplejších dnech se v ní ale snadno zapotíte.</p>'
          '<p>Skořepina (shell) je jen nepromokavá vrstva bez izolace. Teplo dodáte vrstvami pod ní: <a href="/lyzarske-termopradlo/">termoprádlo</a>, <a href="/fleecove-mikiny/">fleecová mikina</a> a v mrazu tenká <a href="/prosivane-bundy/">prošívaná bunda</a>. Skořepina se přizpůsobí jarnímu slunci i lednovému mrazu a využijete ji i na skialpy nebo do hor. Vyžaduje ale víc přemýšlení nad tím, co pod ni obléct.</p>'
          '<h2>Výbava, kterou se vyplatí kontrolovat</h2>'
          '<ul><li><strong>Sněžný pás</strong> je pružný lem uvnitř bundy, který se zapne kolem pasu a nepustí sníh pod bundu při pádu. U některých bund ho lze připnout ke kalhotám.</li>'
          '<li><strong>Kapuce přes helmu</strong> se má dát stáhnout, aby nepadala do očí a otáčela se s hlavou.</li>'
          '<li><strong>Větrací zipy</strong> v podpaží nebo na boku pustí ven teplo, když jedete z kopce na slunci nebo šlapete k vleku.</li>'
          '<li><strong>Kapsa na skipas</strong> bývá na rukávu, takže kartu přiložíte ke čtečce bez rozepínání.</li>'
          '<li><strong>Vnitřní kapsy</strong> pro telefon, který v mrazu rychleji vybíjí baterii, a síťová kapsa na brýle.</li>'
          '<li><strong>Vnitřní manžety s otvorem pro palec</strong> brání sněhu vniknout do rukávu a drží rukáv nad rukavicí.</li></ul>'
          '<h2>RECCO reflektor</h2>'
          '<p>Část bund má v sobě všitý reflektor RECCO. V katalogu je uveden přímo v názvu například u modelů Siroko řady W5 nebo u některých bund O\'Neill s membránou Gore-Tex. Reflektor je pasivní: nepotřebuje baterii ani zapnutí a odráží signál detektoru, který používají záchranné týmy na mnoha střediscích. Může jim usnadnit hledání zasypaného člověka.</p>'
          '<p>RECCO ale nenahrazuje lavinový vyhledávač, sondu a lopatu. Lavinový vyhledávač jeho signál nezachytí a funguje jen tam, kde má záchranka detektor k dispozici. Pokud jezdíte mimo sjezdovky, kde hrozí laviny, potřebujete vlastní lavinovou výbavu, výcvik a parťáka, který ji umí používat.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Bundu zkoušejte s vrstvami, které pod ní budete nosit, ideálně i s chrániči páteře, pokud je používáte. Zvedněte ruce nad hlavu a předkloňte se jako při zapínání vázání: rukávy by měly zůstat přes rukavice a lem nemá vyjet nad pas. Volný střih neznamená kupovat o dvě čísla větší, protože příliš velkou bundou proudí chladný vzduch a sněžný pás pak nedoléhá.</p>'
          '<p>Dámské bundy mají užší ramena a víc prostoru v bocích. Roxy je dámská a dívčí značka, takže střihy jsou zaměřené výhradně na ženy a dívky. U dětských bund vybírejte výraznou barvu, která je na svahu dobře vidět, a reflexní prvky. Dítě roste rychle, rezerva na jednu sezónu je rozumná, ale ne na tři.</p>'
          '<h2>Vrstvy podle počasí</h2>'
          + T(['Podmínky', 'Pod skořepinu', 'Pod zateplenou bundu'], [
              ['Silný mráz, vítr', 'termoprádlo, fleece a tenká prošívaná bunda', 'termoprádlo a fleecová mikina'],
              ['Běžný zimní den', 'termoprádlo a fleecová mikina', 'termoprádlo, případně tenká mikina'],
              ['Jarní slunce, firn', 'jen funkční triko', 'funkční triko a otevřené větrání'],
              ['Mokrý sníh, déšť', 'termoprádlo a tenká syntetická vrstva', 'termoprádlo, bunda s podlepenými švy']]) +
          '<p>Vrstvy volte z funkčních materiálů nebo merino vlny. Bavlněné tričko nasákne potem a na lanovce pak studí. Na krk se hodí nákrčník a pod helmu tenká čepice, obojí najdete mezi <a href="/lyzarske-cepice-a-nakrcniky/">čepicemi a nákrčníky</a>.</p>'
          '<h2>Bunda a kalhoty jako souprava</h2>'
          '<p>Bundu a kalhoty není nutné kupovat od jedné značky, ale má to výhody. Délka bundy a výška pasu kalhot do sebe zapadají, barvy ladí a u některých výrobců lze sněžný pás bundy připnout k poutkům kalhot. Kdo bundu i kalhoty kupuje zvlášť, ať zkontroluje, že bunda přesahuje pas kalhot alespoň o dlaň i v předklonu. Jinak se mezi nimi při pádu dostane sníh.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Roxy nabízí dámské a dívčí bundy v mnoha barvách a střizích, často s označením vodního sloupce v názvu. O\'Neill má pánské, dámské i dětské bundy a u části modelů membránu Gore-Tex. Siroko označuje bundy řadami jako W1, W3 nebo W5, Horsefeathers a Protest vsadily na volnější snowboardový styl. Salomon a Rossignol mají spíš univerzální bundy na lyže i prkno. Mezi dětskými modely najdete také Fundango nebo Trollkids.</p>'
          '<h2>Péče o snowboardovou bundu</h2>'
          '<p>Nepromokavá látka potřebuje čas od času vyprat, protože pot a nečistoty zhoršují její funkci. Řiďte se štítkem: zapnuté zipy, tekutý prací prostředek bez aviváže a důkladné máchání. Vodoodpudivou úpravu povrchu často obnoví krátké prohřátí v sušičce na mírnou teplotu, pokud ho štítek dovoluje. Když voda na látce netvoří kapky ani potom, použijte přípravek z kategorie <a href="/impregnace/">impregnace</a>. Po každém dni na horách bundu vyvětrejte a vysušte, než ji uložíte do skříně.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kupovat bundu bez sněžného pásu, když se při učení často padá.</li>'
          '<li>Sledovat jen číslo 10K/20K a přehlédnout, jestli jsou švy podlepené.</li>'
          '<li>Volit silně zateplenou bundu na jaro, kdy se v ní člověk vaří.</li>'
          '<li>Spoléhat na RECCO jako na náhradu lavinové výbavy.</li>'
          '<li>Zkoušet bundu bez vrstev a pak zjistit, že pod ni nic nevejde.</li></ul>'
          '<p>Ke snowboardové bundě přidejte <a href="/lyzarske-helmy/">helmu</a>, <a href="/lyzarske-bryle/">brýle</a> a <a href="/lyzarske-rukavice/">rukavice</a>. Pokud teprve skládáte výbavu, podívejte se i na <a href="/snowboardy/">snowboardy</a>, <a href="/snowboardove-boty/">boty</a> a <a href="/snowboardove-chranice/">chrániče</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi snowboardovou a lyžařskou bundou?', 'Snowboardová bunda bývá volnější a delší, aby kryla bedra při sezení ve sněhu a nebránila rotaci trupu. Lyžařská je přiléhavější a kratší. Mnoho bund je určeno pro oba sporty.'),
        ('Stačí na snowboard 10K?', 'Na běžné ježdění na sjezdovce v typické zimě ano. Do mokrého sněhu, na jaro nebo na hodně dní na horách je lepší 15K a víc a celoplošně podlepené švy.'),
        ('Co znamená 10K/7K?', 'První číslo je vodní sloupec 10 000 mm, druhé prodyšnost 7 000 g vodní páry na metr čtvereční za 24 hodin. Platí pro látku, ne pro celou bundu.'),
        ('Zateplená bunda, nebo skořepina?', 'Zateplená je jednodušší pro začátečníky a rodiny. Skořepina s vrstvami pod ní se lépe přizpůsobí počasí a hodí se i na skialpy a do hor.'),
        ('Co je sněžný pás?', 'Pružný lem uvnitř bundy, který se zapne kolem pasu a zabrání sněhu dostat se pod bundu při pádu. U některých bund ho lze připnout ke kalhotám.'),
        ('Nahradí RECCO lavinový vyhledávač?', 'Ne. RECCO je pasivní reflektor, který najde jen záchranný tým se speciálním detektorem. Mimo sjezdovky potřebujete lavinový vyhledávač, sondu, lopatu a výcvik.'),
        ('Jakou velikost snowboardové bundy vybrat?', 'Zkoušejte ji s vrstvami, které pod ní budete nosit. Rukávy mají zůstat přes rukavice i se zvednutými pažemi. Volný střih neznamená o dvě čísla větší.'),
        ('Je Roxy jen dámská značka?', 'Ano, Roxy dělá oblečení pro ženy a dívky. V nabídce jsou dámské i dívčí snowboardové bundy.'),
        ('Jak prát snowboardovou bundu?', 'Podle štítku, tekutým prostředkem bez aviváže a se zapnutými zipy. Vodoodpudivou úpravu obnovíte prohřátím nebo novou impregnací.'),
        ('Kde koupit snowboardovou bundu?', 'Sporteka u každé bundy zobrazí nabídky českých e-shopů. Nákup dokončíte u prodejce, jehož nabídku si vyberete.'),
    ])

# ------------------------------------------------------------------ snowboardove-kalhoty
NEW['snowboardove-kalhoty'] = dict(long=True,
    title='Snowboardové kalhoty: volný střih, kšandy i dětské modely',
    desc='Snowboardové kalhoty volného střihu, s kšandami nebo laclem, zateplené i skořepinové. Jak číst 10K/10K, vybrat velikost a co nosit pod nimi.',
    intro='<p><strong>Snowboardové kalhoty</strong> jsou nepromokavé kalhoty volnějšího střihu, ve kterých se dá sedět ve sněhu, klečet na svahu a jezdit v širokém postoji. Mají zesílený spodní lem, vnitřní návleky přes boty a často kšandy nebo vysoký lacl, který nepustí sníh k tělu ani při pádu. Na trhu jsou zateplené modely na mráz i tenké skořepinové kalhoty, pod které si teplo přidáte vrstvami.</p>'
          '<p>Sporteka porovná nabídky českých e-shopů, takže u každých kalhot vidíte, kdo je má a v jakých velikostech, a nakoupíte přímo u prodejce. Velký výběr mají '
          + B(('roxy', 'Roxy'), ('o-neill', "O'Neill"), ('siroko', 'Siroko'), ('horsefeathers', 'Horsefeathers'), ('salomon', 'Salomon'), ('4f', '4F')) +
          ', dále Quiksilver nebo Ziener. K nim patří <a href="/snowboardove-bundy/">snowboardové bundy</a>, srovnání s lyžařskými modely najdete v kategorii <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>',
    guide='<h2>Proč mají snowboardové kalhoty volný střih</h2>'
          '<p>Snowboardista stojí na prkně v širokém postoji s pokrčenými koleny a každé zapínání vázání znamená sednout si nebo kleknout do sněhu. Úzké kalhoty by v klíně táhly a na kolenou se napínaly. Volnější střih dává prostor pro pohyb i pro vrstvy pod kalhotami, například termoprádlo nebo chrániče kostrče a kyčlí, které začátečníci často nosí. Volný střih je zároveň typický styl snowboardového oblečení.</p>'
          '<p>Kalhoty se prodávají ve střizích od mírně volného (regular) po výrazně volné (loose, baggy). Lyžařské kalhoty bývají užší, hlavně v lýtkách. Mnoho modelů je ale určeno pro oba sporty a označení lyžařské/snowboardové kalhoty je běžné.</p>'
          '<h2>Kalhoty, kšandy, nebo lacl</h2>'
          + T(['Typ', 'Výhody', 'Nevýhody'], [
              ['Kalhoty do pasu', 'snadno se oblékají, stahování pasu, poutka na opasek', 'při pádu se do pasu dostane sníh, sjíždějí'],
              ['Kalhoty s kšandami', 'drží na místě, kšandy jdou často odepnout', 'kšandy mohou pod bundou tlačit'],
              ['Lacl (bib)', 'vysoký předek i záda, sníh nepronikne k tělu, teplejší trup', 'těžší, pomalejší převlékání, toaleta']]) +
          '<p>Kalhoty s laclem (bib) se mezi snowboardisty rozšířily hlavně díky ježdění v hlubokém sněhu, kde ochrání záda při pádu i sezení. Ocení je i děti, které se ve sněhu válejí. Nevýhodou je složitější cesta na toaletu. Některé modely to řeší dlouhými bočními zipy nebo odepínacím zadním dílem, podrobnosti uvádí popis výrobce. V katalogu najdete kalhoty s kšandami například v řadě B1 od značky Siroko, v dětských verzích pak modely KB1.</p>'
          '<h2>Spodní lem a vnitřní návleky</h2>'
          '<p>Nohavice snowboardových kalhot končí přes botu. Uvnitř mají pružný návlek, často s protiskluzovým lemem nebo háčkem na tkaničky, který se natáhne přes snowboardovou botu a nepustí sníh dovnitř. Vnější nohavice zakryje vršek boty a spoj s vázáním. Spodní okraj bývá zevnitř zesílený odolnou tkaninou, protože o něj tře hrana prkna, druhá bota a přezky vázání.</p>'
          '<p>Délka je důležitá: kalhoty mají zakrýt horní část boty i v pokrčených kolenou, ale nesmí se táhnout po zemi, kde nasáknou vodou a roztrhá je hrana. Pokud máte <a href="/snowboardove-boty/">snowboardové boty</a> s objemnějším límcem, zkuste kalhoty s nimi.</p>'
          '<h2>Nepromokavost a prodyšnost</h2>'
          '<p>Kalhoty jsou při snowboardingu namáhané víc než bunda. Sezení ve sněhu a klečení na svahu vytvoří velký tlak, který vodu protlačí i přes látku s nízkým vodním sloupcem. Údaj ve formátu 10K/10K znamená vodní sloupec 10 000 mm a prodyšnost 10 000 g/m² za 24 hodin. Hodnoty kolem 5K vystačí na pár dní za suchého mrazu, 10K je běžný standard a 15K–20K se vyplatí do mokrého sněhu a pro ty, kdo jezdí hodně.</p>'
          '<p>Začátečník sedí ve sněhu častěji než zkušený jezdec, proto mu vyšší nepromokavost pomůže víc, než by se mohlo zdát. Stejně důležité jako číslo jsou podlepené švy, hlavně v sedu a na kolenou, kde je tlak největší.</p>'
          '<h2>Zateplení a vrstvy</h2>'
          '<p>Zateplené kalhoty mají tenkou syntetickou výplň a stačí pod ně funkční spodky. Jsou pohodlné pro rekreační ježdění a pro ty, kterým bývá zima. Skořepinové kalhoty bez výplně jsou lehčí a víc univerzální: v mrazu pod ně oblečete teplé <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a> nebo fleecové spodky, na jaře jen tenkou vrstvu.</p>'
          '<p>Pod kalhoty nepatří džíny ani bavlněné tepláky, které nasáknou potem a sněhem a chladí. Větrací zipy na vnitřní nebo vnější straně stehen se hodí při šlapání k vleku a v teplých dnech. Kapsy by měly mít zip nebo patentku, aby se z nich při pádu nic neztratilo.</p>'
          + T(['Teplota a počasí', 'Skořepinové kalhoty', 'Zateplené kalhoty'], [
              ['Pod −10 °C, vítr', 'teplé termoprádlo a fleecové spodky', 'teplejší funkční spodky'],
              ['Kolem −5 °C', 'funkční spodky střední tloušťky', 'tenké funkční spodky'],
              ['Kolem nuly a jaro', 'tenké spodky nebo nic, otevřené větrání', 'tenké spodky, větrání, hrozí přehřátí']]) +
          '<h2>Kapsy a další detaily</h2>'
          '<p>Na kalhotách se hodí jedna stehenní kapsa na zip nebo s klopou na drobnosti, které se nevejdou do bundy. Velké nákladní kapsy vypadají dobře, ale těžký telefon nebo klíče v nich při jízdě poskakují a při pádu tlačí do stehna. Poutka na opasek a stahování pasu oceníte, pokud kalhoty nemají kšandy. Pruh odolnější tkaniny na sedu a kolenou prodlouží život kalhot, které se často dostávají do kontaktu s ledem a hranou.</p>'
          '<p>Na kalhotách s laclem zkontrolujte, jak se nastavují ramenní popruhy a jestli se dají rozepnout bez sundání bundy. Pro jízdu v hlubokém sněhu je praktický vysoký zadní díl, který při sezení v prašanu zabrání tomu, aby se vám sníh dostal do kalhot.</p>'
          '<h2>Kalhoty a chrániče</h2>'
          '<p>Začátečníci často padají na kostrč a kolena. Chránicí šortky s výstelkou na bocích a kostrči se nosí pod kalhoty, chrániče kolen také. Kalhoty proto musí mít dost místa, aby výstelka zůstala na svém místě a netlačila. Zkuste dřep v kalhotách i s chrániči a zkontrolujte, že látka nikde nenapíná. Výběr najdete v kategorii <a href="/snowboardove-chranice/">snowboardové chrániče</a>.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Vyzkoušejte kalhoty s tím, co pod nimi budete nosit, včetně chráničů. Udělejte hluboký dřep a vysoký krok: kalhoty nesmí táhnout v sedu ani na kolenou. Pas bývá nastavitelný suchým zipem nebo pružnými pásky uvnitř, takže lze dorovnat mezi velikostmi. Délku kontrolujte v botách.</p>'
          '<p>Dámské střihy mají víc místa v bocích a užší pas. Roxy šije kalhoty jen pro ženy a dívky, takže výběr dámských modelů je široký. Velikostní tabulky se mezi značkami liší, proto vždy porovnejte obvod pasu, boků a vnitřní délku nohavice se svými mírami.</p>'
          '<h2>Dětské snowboardové kalhoty</h2>'
          '<p>Děti se na prkně učí hlavně padáním a sezením ve sněhu. Vyplatí se jim kalhoty s kšandami nebo laclem, zesíleným sedem a koleny a dostatečným vodním sloupcem. Pestrá barva a reflexní prvky pomohou, abyste dítě na svahu snadno našli. Některé dětské modely mají možnost prodloužení nohavic, díky kterému vydrží o sezónu déle; zda ji konkrétní kalhoty mají, uvádí popis výrobce. Pro nejmenší lyžaře a snowboardisty se nabízí i <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a>.</p>'
          '<h2>Péče</h2>'
          '<p>Po dni na horách kalhoty vysušte při pokojové teplotě, ne přímo na topení. Perou se podle štítku tekutým prostředkem bez aviváže, se zapnutými zipy a zapnutými kšandami. Obnovu vodoodpudivé úpravy zajistí krátké prohřátí podle návodu nebo přípravek z kategorie <a href="/impregnace/">impregnace</a>. Prodřený spodní lem lze nechat podšít, než se díra rozšíří až k návleku.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Kupovat kalhoty bez kšand pro dítě nebo začátečníka, který často padá.</li>'
          '<li>Volit nohavice tak dlouhé, že se táhnou po sněhu a ničí je hrana.</li>'
          '<li>Nosit pod kalhotami bavlnu místo funkční vrstvy.</li>'
          '<li>Sledovat jen vodní sloupec a nezkontrolovat podlepení švů v sedu.</li>'
          '<li>Nezkusit kalhoty s chrániči, se kterými pak nejdou zapnout.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Stejné kalhoty se v obchodech objevují v různých barvách a s kódy variant, někdy i z předchozí sezóny. Při srovnání se dívejte hlavně na vodní sloupec, typ zateplení, střih (regular, nebo loose) a na to, jestli mají kšandy. Velikosti mizí ze skladů rychle, hlavně na začátku zimy, takže pokud vám sedí konkrétní model, ověřte si dostupnost své velikosti u více prodejců. Užitečné je i snadné vrácení zboží, protože střih kalhot se mezi značkami liší víc než u bund.</p>'
          '<p>V mokrém počasí mimo svah poslouží i obyčejné <a href="/nepromokave-kalhoty/">nepromokavé kalhoty</a>. Bunda, kalhoty a <a href="/lyzarske-rukavice/">rukavice</a> tvoří základ, který ochrání před sněhem. Celou výbavu doplníte v kategoriích <a href="/snowboardy/">snowboardy</a> a <a href="/snowboardova-vazani/">vázání</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi snowboardovými a lyžařskými kalhotami?', 'Snowboardové kalhoty mají volnější střih, prostor pro chrániče a zesílený spodní lem, protože se v nich hodně sedí a klečí. Lyžařské jsou užší. Mnoho modelů je určeno pro oba sporty.'),
        ('Kalhoty s kšandami, nebo lacl?', 'Kšandy udrží kalhoty na místě a dají se odepnout. Lacl má vysoký předek i záda, takže nepustí sníh k tělu ani při pádu. Je ale těžší a složitější na převlékání.'),
        ('Jaký vodní sloupec mají mít snowboardové kalhoty?', 'Běžný standard je 10K. Začátečníkům, kteří často sedí ve sněhu, a na mokrý sníh se vyplatí 15K a víc a podlepené švy.'),
        ('Co jsou vnitřní návleky?', 'Pružné manžety uvnitř nohavic, které se natáhnou přes botu a nepustí sníh dovnitř. Často mají protiskluzový lem nebo háček na tkaničky.'),
        ('Jak dlouhé mají snowboardové kalhoty být?', 'Mají zakrýt horní část boty i s pokrčenými koleny, ale nesmí se táhnout po zemi. Délku zkoušejte v botách.'),
        ('Co nosit pod snowboardové kalhoty?', 'Funkční spodky, v mrazu teplejší termoprádlo nebo fleecové spodky. Bavlna nasákne potem a chladí.'),
        ('Zateplené, nebo skořepinové kalhoty?', 'Zateplené jsou jednodušší pro rekreační ježdění. Skořepinové s vrstvami pod nimi se lépe přizpůsobí teplotě a počasí.'),
        ('Jaké snowboardové kalhoty pro dítě?', 'S kšandami nebo laclem, zesíleným sedem a koleny, dobrou nepromokavostí a výraznou barvou s reflexními prvky.'),
        ('Jak prát snowboardové kalhoty?', 'Podle štítku tekutým prostředkem bez aviváže. Vodoodpudivou úpravu obnoví prohřátí nebo nová impregnace.'),
        ('Kde koupit snowboardové kalhoty?', 'Sporteka zobrazí nabídky českých e-shopů u každého modelu včetně velikostí. Nakoupíte přímo v obchodě, který si vyberete.'),
    ])
