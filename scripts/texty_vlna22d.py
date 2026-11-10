"""sporteka.cz — wave 22d (4. 11. 2026): long texts (>= 1650 words) for kreatin, chladici-boxy, turisticke-stany, sane-a-boby.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ kreatin
NEW['kreatin'] = dict(long=True,
    title='Kreatin: monohydrát, kapsle, Creapure a porovnání',
    desc='Kreatin monohydrát v prášku, kapslích i tabletách: formy, čistota, balení a rozdíly. Jak číst etiketu a porovnat nabídky českých obchodů.',
    intro='<p>Kreatin patří k nejčastěji vyhledávaným doplňkům stravy mezi lidmi, kteří pravidelně posilují nebo trénují rychlostní disciplíny. V kategorii najdete jednoduchý <strong>monohydrát v prášku</strong>, kapsle a tablety, směsi s příchutí i kombinované produkty, které k kreatinu přidávají další látky. Rozdíly mezi nabídkami jsou hlavně v čistotě suroviny, velikosti balení, formě a přídavných složkách.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u značek jako '
          + B(('gymbeam', 'GymBeam'), ('amix', 'Amix'), ('masmusculo', 'Masmusculo'), ('allnutrition', 'AllNutrition'), ('biotech-usa', 'BioTech USA'), ('myprotein', 'MyProtein'), ('weider', 'Weider'), ('optimum-nutrition', 'Optimum Nutrition')) +
          '. Text je obecný popis zboží, nikoli zdravotní rada. Okolní témata najdete ve <a href="/sportovni-vyziva/">sportovní výživě</a>, v <a href="/proteiny/">proteinech</a> a v <a href="/aminokyseliny-bcaa/">aminokyselinách</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Základní nabídku tvoří čistý kreatin monohydrát v prášku, často ve dvou velikostech balení pro vyzkoušení a pro dlouhodobé používání. Vedle něj jsou kapsle a tablety pro ty, kdo nechtějí míchat nápoj, a pak různé kombinované výrobky. Některé obsahují beta-alanin, elektrolyty nebo cukry, jiné dokonce tvoří součást pudinku či jiné hotové potraviny s kreatinem.</p>'
          + T(['Forma', 'Typické balení', 'Co zvážit'], [
              ['Monohydrát v prášku', 'sáček nebo dóza stovky gramů až kilo', 'bez příchutě, snadné dávkování lopatkou'],
              ['Kapsle a tablety', 'plastová dóza s desítkami až stovkami kusů', 'pohodlné na cesty, nižší množství v kusu'],
              ['Příchuťové směsi', 'dóza s práškem k rozmíchání', 'obsahují sladidla a aromata'],
              ['Kombinované produkty', 'prášek nebo kapsle s dalšími látkami', 'čtěte složení, porovnávejte dávky'],
              ['Potraviny s kreatinem', 'pudink, tyčinka, nápoj', 'spíš doplněk než základní zásoba']]) +
          '<p>Nejjednodušší je držet se jedné složky. Čistý monohydrát se snáz porovnává mezi obchody a výrobci, protože každé balení vypadá z hlediska složení stejně. Kombinované produkty mají smysl, když přesně víte, co v nich hledáte.</p>'
          '<h2>Monohydrát a jeho varianty</h2>'
          '<p>Kreatin monohydrát je nejstarší a nejběžnější forma. Na obalech narazíte na označení jako <em>Creapure</em>, což je ochranná známka suroviny vyráběné v Německu, kterou některé značky uvádějí jako zdroj. Setkáte se i s popisem <em>200 mesh</em>, který udává jemnost mletí. Jemnější prášek se obecně snáz rozpouští ve vodě a méně se usazuje na dně šejkru.</p>'
          '<p>Dále existují další chemické formy, například hydrochlorid, ethylester nebo pufrovaná varianta. Prodejci je často prezentují jako alternativu, ale z hlediska srovnání nabídek platí jednoduchá zásada: čtěte, kolik čistého kreatinu je v jedné porci, a ne jen název na přední straně obalu.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<ul><li><strong>Složení:</strong> u čistého výrobku by mělo být na prvním místě jediná položka, kreatin monohydrát.</li>'
          '<li><strong>Velikost porce:</strong> porovnávejte množství na porci a počet porcí v balení, ne celkovou hmotnost dózy.</li>'
          '<li><strong>Doplněk stravy:</strong> označení znamená, že produkt není lék. Nahrazovat pestrou stravu nemá.</li>'
          '<li><strong>Upozornění:</strong> výrobci uvádějí doporučené denní množství, kterého se nemá překračovat, a skupiny osob, pro které výrobek není určen.</li>'
          '<li><strong>Datum minimální trvanlivosti:</strong> u velkých balení ověřte, že stihnete spotřebovat obsah.</li>'
          '<li><strong>Alergeny:</strong> u příchuťových směsí a kombinovaných výrobků bývají uvedené v tučném písmu.</li></ul>'
          '<h2>Prášek, nebo kapsle</h2>'
          '<p>Prášek je ve většině případů cenově výhodnější na jednu porci a dá se přesně dávkovat. Rozmíchá se ve vodě, džusu nebo v shakeru, nejčastěji společně s dalším nápojem. Nevýhodou je, že potřebujete odměrku a čistou nádobu. Kapsle a tablety zase vyřeší cestování, kancelář i situace, kdy nemáte po ruce vodu na míchání, ale jedna porce obvykle vyžaduje několik kusů.</p>'
          '<p>U kapslí pozorně porovnávejte, kolik kreatinu opravdu obsahuje jedna kapsle a kolik jich výrobce doporučuje na porci. Velké číslo na přední straně dózy se může vztahovat na celkový počet kapslí, ne na množství látky.</p>'
          '<h2>Pro koho je kreatin zajímavý</h2>'
          '<p>Nejčastěji ho kupují lidé, kteří se věnují silovému tréninku v <a href="/fitness/">fitness</a>, pracují s <a href="/cinky-a-kotouce/">činkami a kotouči</a> nebo dělají intenzivní intervalový trénink. Zajímá i kolektivní hráče a sprintery. Pro vytrvalostní běh či dlouhé túry je mnohem méně typický. Rozhodnutí, zda doplněk začít užívat, patří k osobním a při zdravotních potížích nebo užívání léků ho konzultujte s lékařem. Ani popis na webu obchodu nenahradí individuální radu.</p>'
          '<h2>Jak se kreatin skládá do jídelníčku</h2>'
          '<p>Obecně se doplněk užívá pravidelně, ne jen v tréninkové dny, a dávkuje se podle pokynů výrobce na obalu. Prášek se nemusí kombinovat s konkrétním nápojem. V praxi lidé míchají kreatin do šejkru spolu s <a href="/proteiny/">proteinem</a>, což šetří nádobí. Dalším navazujícím doplňkem bývají <a href="/predtreninkove-boostery/">předtréninkové boostery</a>, které kreatin někdy obsahují také, takže při kombinaci hlídejte celkové množství ze všech zdrojů.</p>'
          '<p>Pamatujte i na pitný režim. Při jakékoli zvýšené fyzické zátěži se hodí dostatek tekutin, a proto stojí za zvážení i <a href="/iontove-napoje/">iontové nápoje</a> nebo kvalitní <a href="/lahve-a-termosky/">láhev na vodu</a>.</p>'
          '<h2>Kreatin vedle dalších doplňků</h2>'
          + T(['Doplněk', 'Obvyklá role v nabídce', 'Kategorie'], [
              ['Protein', 'zdroj bílkovin ve formě nápoje', '<a href="/proteiny/">proteiny</a>'],
              ['Aminokyseliny', 'rozpustné prášky a kapsle', '<a href="/aminokyseliny-bcaa/">BCAA</a>'],
              ['Vitaminy a minerály', 'doplnění mikroživin', '<a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>'],
              ['Kloubní výživa', 'kolagen, glukosamin', '<a href="/kolagen-a-klouby/">kolagen a klouby</a>'],
              ['Energie při tréninku', 'gely a tyčinky', '<a href="/energeticke-gely-a-tycinky/">gely a tyčinky</a>'],
              ['Ostatní doplňky', 'extrakty a oleje', '<a href="/ostatni-doplnky-stravy/">ostatní doplňky</a>']]) +
          '<p>Žádný z těchto doplňků nenahrazuje zdravé stravování, spánek a trénink. Fungují jako doplněk, a ne jako základ.</p>'
          '<h2>Kde se kreatin nejlépe porovnává</h2>'
          '<p>Z celého katalogu je nejvíc výrobků od značky GymBeam, hned za ní následují Amix, Masmusculo, AllNutrition a BioTech USA. Velké zahraniční značky, třeba MyProtein nebo Optimum Nutrition, nabízejí často větší balení. Menší výrobci se objevují s jedním dvěma produkty. Nejlepší postup je vybrat si nejprve formu, pak velikost balení a teprve potom porovnat obchody.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Porovnávání podle hmotnosti dózy:</strong> důležitý je obsah na porci, ne celkový počet gramů.</li>'
          '<li><strong>Přeplacení za marketing:</strong> komplikované názvy často znamenají jen jinou chemickou formu nebo přidaná aromata.</li>'
          '<li><strong>Příliš velké balení:</strong> pokud si nejste jistí, začněte menším, abyste zjistili, jak vám doplněk vyhovuje.</li>'
          '<li><strong>Ignorování složení:</strong> v kombinovaných směsích mohou být látky, které nechcete, třeba kofein.</li>'
          '<li><strong>Špatné skladování:</strong> prášek je citlivý na vlhkost, dózu zavírejte a nenechávejte ji na parné koupelně.</li>'
          '<li><strong>Čekání na zázrak:</strong> doplněk sám o sobě nic nevyřeší bez tréninku a stravy.</li></ul>'
          '<h2>Skladování a praktické tipy</h2>'
          '<p>Dózu uchovávejte na suchém, chladnějším místě mimo přímé slunce a mimo dosah dětí. Odměrku po každém použití otřete do sucha, ať se prášek nesléhává. Při cestování se hodí malá <a href="/sportovni-tasky/">sportovní taška</a> s přihrádkou na šejkr a dózu, případně <a href="/sportovni-vyziva/">výživové dávkovače</a> na jednu porci. Na letiště raději berte originální obaly s etiketou, ať je zřejmé, o co jde.</p>'
          '<h2>Jak na nákup na Sportece</h2>'
          '<p>Filtrujte podle značky, obchodu a velikosti balení. U každého produktu si otevřete detail a zkontrolujte, zda se nabídky skutečně týkají stejné hmotnosti a příchutě, protože obchody často pod jedním názvem slučují více variant. Sledujte i dostupnost a termín dodání, hlavně u zahraničních značek. Případné akce se mění, proto porovnejte více obchodů, než objednáte.</p>',
    faq=[('Co je kreatin monohydrát?', 'Je to nejběžnější forma kreatinu v doplňcích stravy, obvykle prodávaná jako bílý prášek bez příchutě nebo ve formě kapslí. V kategorii se nejlépe porovnává, protože složení je u všech výrobců v zásadě stejné.'),
         ('Jaký je rozdíl mezi práškem a kapslemi?', 'Prášek se odměřuje a rozmíchává v tekutině, kapsle se polykají. Liší se obsahem látky v jednom kusu, pohodlím a počtem kusů potřebných na porci. Vždy porovnávejte množství na porci.'),
         ('Co znamená Creapure?', 'Je to obchodní název suroviny kreatin monohydrátu z jednoho výrobce v Německu. Značky ho uvádějí na obalu jako zdroj. Je to informace o původu suroviny, ne o jiné chemické formě.'),
         ('Co znamená 200 mesh?', 'Jde o údaj o jemnosti mletí prášku. Jemnější prášek se obecně snáz rozpouští a méně se usazuje v nápoji. Informace o hrubosti se na obalech objevuje u části značek.'),
         ('Je lepší příchuťová směs, nebo neutrální prášek?', 'Neutrální prášek obsahuje jen jednu složku a snadno se míchá do jiných nápojů. Příchuťové směsi chutnají výrazněji, ale obsahují sladidla, aromata a někdy i další látky, takže čtěte složení.'),
         ('Můžu kreatin míchat s proteinem?', 'Praktická kombinace je běžná, často se oba prášky míchají v jednom šejkru. Respektujte doporučení výrobce na obalu a sledujte celkové množství, pokud užíváte i předtréninkový přípravek s kreatinem.'),
         ('Jak dlouho vydrží velké balení?', 'Záleží na velikosti balení a na tom, kolik gramů výrobce doporučuje na porci. Vydělte hmotnost dózy množstvím na porci a dostanete počet porcí. Pak zkontrolujte datum minimální trvanlivosti.'),
         ('Hodí se kreatin pro začátečníky?', 'Rozhodnutí je individuální. Doplněk není nutný, nahradit ho nemůže trénink, strava ani spánek. Pokud si nejste jistí, poraďte se s lékařem nebo kvalifikovaným odborníkem na výživu.'),
         ('Mohu kreatin užívat, když beru léky nebo mám zdravotní potíže?', 'Takovou otázku patří řešit s lékařem, ne podle popisu v e-shopu. Také děti, těhotné a kojící osoby se mají poradit s lékařem před užíváním jakéhokoli doplňku stravy.'),
         ('Proč se cena stejného produktu liší mezi obchody?', 'Každý obchod si stanovuje vlastní marži, poštovné a akce. Sporteka ukazuje nabídky vedle sebe, takže snadno uvidíte rozdíly. Ověřte ale, že porovnáváte stejnou hmotnost, formu a příchuť.'),
         ('Jak kreatin správně skladovat?', 'Na suchém místě, v dobře uzavřené dóze, mimo vlhkost a přímé slunce. Odměrku udržujte suchou. Po otevření dodržte pokyny výrobce o spotřebě v uvedené době.')])

# ------------------------------------------------------------------ chladici-boxy
NEW['chladici-boxy'] = dict(long=True,
    title='Chladicí boxy a tašky: pasivní, elektrické, termo',
    desc='Chladicí boxy, tašky a termotašky na kemp, výlet i rybaření: pasivní, kolečkové a elektrické. Jak vybrat objem a porovnat nabídky obchodů.',
    intro='<p>Chladicí box nebo taška vám udrží jídlo a pití chladné při výletě, na pláži, v kempu i při rybaření. V kategorii najdete <strong>pevné pasivní boxy</strong> s izolovanou stěnou, měkké termotašky, boxy na kolečkách, elektrické modely do auta a také dětské tašky na svačinu. Rozdíly jsou v objemu, tloušťce izolace, těsnění víka a v tom, jak se s nimi nosí.</p>'
          '<p>Sporteka porovnává nabídky obchodů u značek jako '
          + B(('thermos', 'Thermos'), ('merco', 'Merco'), ('quechua', 'Quechua'), ('campingaz', 'Campingaz'), ('outwell', 'Outwell'), ('coleman', 'Coleman'), ('petromax', 'Petromax'), ('curver', 'Curver')) +
          '. K chlazení se hodí také <a href="/lahve-a-termosky/">láhve a termosky</a>, <a href="/kemping/">kempingové vybavení</a> a <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>',
    guide='<h2>Jaké druhy chlazení existují</h2>'
          '<p>Chlazení bez elektřiny funguje tak, že izolovaná stěna zpomaluje přenos tepla dovnitř. Aby uvnitř zůstal chlad, potřebujete chladicí vložky, led nebo předchlazené potraviny. Elektrické boxy naopak aktivně ochlazují nebo udržují teplotu a potřebují zdroj proudu.</p>'
          + T(['Typ', 'Princip', 'Hodí se pro'], [
              ['Pevný pasivní box', 'silná izolace a těsné víko', 'kemp, víkend, delší pobyt'],
              ['Box na kolečkách', 'pasivní s úchytem a koly', 'pláž, velké rodiny, těžký náklad'],
              ['Termotaška', 'měkká izolovaná taška', 'výlet, piknik, oběd do práce'],
              ['Dětská taška', 'malá taška s motivem', 'svačina do školky a školy'],
              ['Elektrický box', '12 V nebo síťové napájení', 'cesta autem, karavan, dlouhé chlazení'],
              ['Rybářská termotaška', 'izolovaná taška pro nástrahy a jídlo', 'kaprařina, <a href="/rybareni/">rybaření</a>']]) +
          '<p>Pevné boxy bývají těžší, ale izolují nejlépe a vydrží i silné používání. Měkké tašky jsou lehké a skladné, hodí se na krátké akce a na ruční přenášení. Elektrické modely se vyplatí hlavně při dlouhých cestách.</p>'
          '<h2>Jak zvolit objem</h2>'
          '<p>Objem se udává v litrech nebo v anglických jednotkách quartech, třeba u modelů označených jako 50QT. Větší není vždy lepší: prázdný prostor v boxu urychluje oteplování a box se hůř nosí. Podle účelu zhruba platí:</p>'
          '<ul><li><strong>Malé tašky:</strong> osobní svačina, nápoj a nějaké ovoce, obvykle jedna osoba.</li>'
          '<li><strong>Střední boxy:</strong> piknik pro dva až čtyři lidi, jeden den na pláži.</li>'
          '<li><strong>Velké boxy:</strong> víkend v kempu, rodina se zásobou, rybářská výprava.</li>'
          '<li><strong>Kolečkové a velkoobjemové:</strong> dlouhodobý pobyt a větší skupiny.</li></ul>'
          '<p>Pamatujte, že uvedený objem nemusí odpovídat použitelnému prostoru. Silná izolace ubírá vnitřní rozměr, takže se vždy podívejte i na vnitřní rozměry, zejména u vysokých lahví.</p>'
          '<h2>Na čem záleží u izolace a víka</h2>'
          '<p>Kvalitní box má plné stěny s pěnou, těsnicí lem kolem víka a robustní zámky nebo západky. Víko by mělo doléhat rovnoměrně, protože každá štěrbina je cesta pro teplo. Dobré boxy mají odtokový ventil, kterým vypustíte vodu z roztátého ledu, a odnímatelné madlo, případně držák na lahve nebo kelímky.</p>'
          '<p>U měkkých tašek hledejte vnitřní fólii bez švů, zpevněné dno a zip s krytím. Taška s tenkou stěnou rychle nahřeje obsah a hodí se opravdu jen na krátký transport. Zkoušejte také popruhy: široký polstrovaný nosník se pohodlně nosí delší dobu.</p>'
          '<h2>Jak chlad udržet co nejdéle</h2>'
          '<ul><li>Box i potraviny předchlaďte v lednici, nikdy neplňte teplý obsah.</li>'
          '<li>Použijte chladicí vložky nebo zmrzlé láhve s vodou, které se při tání nezmění v louži.</li>'
          '<li>Skládejte vrstvy: studené dole, jemné věci nahoře, mezery vyplňte látkou nebo další vložkou.</li>'
          '<li>Box nechte ve stínu, nejlépe přikrytý ručníkem, a víko otevírejte co nejméně.</li>'
          '<li>Pití a jídlo oddělte, protože nápoje se otevírají častěji.</li>'
          '<li>Syrové maso a ryby balte zvlášť, aby neznečistily ostatní potraviny.</li></ul>'
          '<h2>Elektrické a termoelektrické boxy</h2>'
          '<p>Tyto modely se připojují do zásuvky v autě, někdy i do běžné sítě. Termoelektrické boxy chladí zhruba o 15 až 20 °C pod teplotu okolí (přesný údaj najdete u konkrétního modelu), ne na pevnou hodnotu, proto v horkém autě nedosáhnou teploty lednice. Kompresorové modely jsou výkonnější a drahé. Před koupí si ověřte napětí, spotřebu a to, zda box neodebírá proud, když je auto vypnuté. Při delším stání se vybíjí autobaterie, a proto se hodí <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a> nebo přenosný zdroj. Některé modely umějí udržovat i teplo.</p>'
          '<h2>Chladicí boxy a tašky podle aktivity</h2>'
          + T(['Aktivita', 'Co se hodí', 'Související kategorie'], [
              ['Kemp s rodinou', 'velký pasivní box s odtokem', '<a href="/kempingovy-nabytek/">kempingový nábytek</a>'],
              ['Pláž a koupaliště', 'box na kolečkách nebo střední taška', '<a href="/plazove-doplnky/">plážové doplňky</a>'],
              ['Pěší výlet', 'malá termotaška do batohu', '<a href="/turisticke-batohy/">turistické batohy</a>'],
              ['Rybaření', 'termotaška na nástrahy a svačinu', '<a href="/rybarske-tasky/">rybářské tašky</a>'],
              ['Piknik v parku', 'měkká taška se zipem', '<a href="/volny-cas/">volný čas</a>'],
              ['Škola a svačina', 'dětská taška', '<a href="/detske-stany/">dětské vybavení</a>']]) +
          '<h2>Péče a čištění</h2>'
          '<p>Po každém použití box vypláchněte vlažnou vodou s trochou saponátu, otřete a nechte otevřený, aby uvnitř nevznikl zápach. Nepoužívejte drsné houbičky ani silná rozpouštědla, která by poškodila vnitřní vrstvu. Těsnění občas zkontrolujte a utřete od nečistot. Při dlouhodobém uložení nechte víko lehce pootevřené. U měkkých tašek zkontrolujte, zda výrobce nezakazuje praní, protože v pračce se izolace často poničí.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Příliš velký box:</strong> nosí se hůř a potřebuje víc ledu.</li>'
          '<li><strong>Porovnávání jen podle objemu:</strong> důležitější je tloušťka stěny a těsnost víka.</li>'
          '<li><strong>Zapomenuté chladicí vložky:</strong> samotný box nechladí, jen zpomaluje oteplování.</li>'
          '<li><strong>Termotaška místo boxu na víkend:</strong> měkká taška má kratší výdrž chladu.</li>'
          '<li><strong>Elektrický box bez zdroje:</strong> v autě bez nabíjení ztrácí smysl.</li>'
          '<li><strong>Ignorované rozměry:</strong> ověřte, zda se vejde do kufru nebo do stanu.</li></ul>'
          '<h2>Jak na nákup na Sportece</h2>'
          '<p>V katalogu najdete i věci, které s chlazením souvisejí jen okrajově, například tašky na rybářské vybavení nebo dětské svačinové modely. Filtrujte podle značky a podle názvu produktu. Zjistěte, jaký objem a rozměry si vybíráte, a porovnejte dostupnost u více obchodů. Po sezóně bývá výběr užší, takže potřebujete-li konkrétní velikost, hledejte dříve.</p>',
    faq=[('Jak velký chladicí box potřebuji?', 'Pro osobní svačinu stačí malá taška, pro piknik střední box, pro víkend v kempu velký pasivní model. Zohledněte počet lidí, délku výletu a to, kolik místa v autě nebo ve stanu máte.'),
         ('Jaký je rozdíl mezi chladicím boxem a termotaškou?', 'Box má pevné stěny a silnější izolaci, takže drží chlad déle a unese zátěž. Termotaška je měkká, lehká a skladná, ale chlad udrží kratší dobu.'),
         ('Chladí pasivní box sám od sebe?', 'Ne. Pouze zpomaluje oteplování obsahu. Potřebujete předchlazené potraviny a chladicí vložky nebo zmrzlé láhve, jinak se zahřeje stejně jako okolí, jen pomaleji.'),
         ('Co znamená označení QT u amerických boxů?', 'Jde o americké jednotky objemu quart. Zhruba přibližně se dá převést na litry, ale vždy se podívejte na litrový údaj výrobce nebo na vnitřní rozměry, ať víte, co se do boxu vejde.'),
         ('Jak se používají elektrické chladicí boxy?', 'Připojují se do zásuvky v autě nebo do sítě. Termoelektrické modely ochlazují jen o omezený rozdíl pod teplotu okolí, takže v horkém autě nedosáhnou teploty lednice. Hlídejte spotřebu, ať nevybíjíte baterii vozidla při stání.'),
         ('Jak dlouho udrží box chlad?', 'Záleží na kvalitě izolace, teplotě okolí, předchlazení a množství chladicích vložek. Přesný čas výrobci uvádějí orientačně, a proto s ním počítejte jen jako s hrubým vodítkem.'),
         ('Může se do boxu dát i teplé jídlo?', 'Některé izolované boxy a tašky umějí držet i teplo, ale výrobce to musí výslovně uvádět. Jinak používejte termosku nebo speciální termonádobu určenou pro teplé jídlo.'),
         ('Jak chladicí box čistit?', 'Vypláchněte jej vlažnou vodou se saponátem, otřete a nechte oschnout otevřený. Vyhněte se drsným čisticím prostředkům a rozpouštědlům. Těsnění pravidelně zkontrolujte, aby zůstalo celé.'),
         ('Proč jsou boxy od různých značek tak rozdílné?', 'Liší se tloušťkou a materiálem izolace, kvalitou těsnění, odolností plastu a výbavou, třeba kolečky, držáky nebo odtokem. Při porovnání se zaměřte na tyto parametry, ne jen na objem a barvu.'),
         ('Hodí se chladicí taška na rybaření?', 'Ano, v katalogu najdete i rybářské termotašky na nástrahy a svačinu. Hledejte zpevněné dno, zip s krytím a dost místa na menší nádoby a chladicí vložky.')])

# ------------------------------------------------------------------ turisticke-stany
NEW['turisticke-stany'] = dict(long=True,
    title='Turistické a trekové stany: výběr, váha, vodní sloupec',
    desc='Turistické a trekové stany pro 1–3 osoby: tunelové, kopulové, ultralehké. Jak vybrat váhu, vodní sloupec a porovnat nabídky českých obchodů.',
    intro='<p>Turistický stan je domov na jednu až několik nocí v horách, na vodě nebo na kole. V této kategorii jsou <strong>lehké trekové stany</strong> pro jednoho až tři lidi, ultralehké konstrukce, tunelové a kopulové modely i vojenské stany z nabídky outdoorových výrobců. Oproti rodinným stanům se víc řeší váha, rozměr po složení a rychlost stavění než prostor na stolek a židle.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů u značek jako '
          + B(('jurek', 'Jurek'), ('3f-ul-gear', '3F UL GEAR'), ('naturehike', 'Naturehike'), ('husky', 'Husky'), ('trimm', 'Trimm'), ('hannah', 'Hannah'), ('loap', 'Loap'), ('ferrino', 'Ferrino')) +
          '. Podobně užitečné jsou <a href="/stany/">stany</a>, <a href="/spaci-pytle/">spací pytle</a>, <a href="/karimatky-a-matrace/">karimatky a matrace</a> a <a href="/stanove-doplnky/">stanové doplňky</a>.</p>',
    guide='<h2>Jaké stany tu najdete</h2>'
          '<p>Hlavní rozdíl je v konstrukci. Určuje, jak stan drží proti větru, kolik váží a kolik prostoru nabídne. Konstrukce se liší počtem a tvarem tyček, počtem vchodů a tím, zda se vnitřní stan zavěšuje pod vnější plášť, nebo je s ním spojený.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Tunelový stan', 'oblouky paralelně, dobrý poměr prostor a váha', 'trek, delší pobyt, vítr při správném zakotvení'],
              ['Kopulový stan', 'křížené tyčky, samostatně stojí', 'kemp, rychlé stavění, víc směrů větru'],
              ['Ultralehký stan', 'tenké tkaniny, často s trekovými holemi', 'dlouhé túry, bikepacking, minimální váha'],
              ['Samostavěcí stan', 'pružné tyčky, rychlé rozložení', 'víkendy, začátečníci, festivaly'],
              ['Vojenský stan', 'robustní tkanina, často maskáčová', 'těžší zátěž, nenáročný provoz'],
              ['Tipi a lavvu', 'jeden střed, kónický tvar', 'skupiny, <a href="/tipi-a-lavvu/">tipi a lavvu</a>']]) +
          '<p>Typ konstrukce vybírejte podle terénu. V otevřené krajině a v horách vyhrávají tunelové a nízké kopulové modely, které odolají větru. Na loukách a v kempu klidně stačí lehký kopulový stan s vyšší stěnou.</p>'
          '<h2>Váha, rozměr a nosnost</h2>'
          '<p>U pěší turistiky se každý kilogram počítá. U ultralehkých modelů se váha často uvádí bez kolíků a obalu, takže si přečtěte, zda údaj znamená <em>minimální</em> hmotnost (jen stan a tyčky), nebo <em>obchodní</em> hmotnost se vším. Stan s počtem míst dva se v praxi hodí hlavně pro dvě štíhlé osoby bez většího zavazadla, proto si často vyplatí vzít model o jedno místo větší, pokud nevadí vyšší váha.</p>'
          '<ul><li><strong>Jednoosobní stany:</strong> nejlehčí, ale těsné. Vejdou se spací pytel a malý batoh.</li>'
          '<li><strong>Dvouosobní stany:</strong> nejuniverzálnější kompromis pro dvojici i pro jednoho s věcmi.</li>'
          '<li><strong>Tříosobní stany:</strong> rodina s dítětem, pohodlí pro dva a výbavu.</li>'
          '<li><strong>Rozměr po složení:</strong> důležitý pro batoh, kolo nebo motorku. Hledejte údaj o délce a průměru obalu.</li></ul>'
          '<h2>Vodní sloupec a materiály</h2>'
          '<p>Hodnota vodního sloupce vyjadřuje, kolik vody materiál udrží, než začne prosakovat. Podlážka má mít vyšší vodní sloupec než vnější plášť, protože je pod tlakem váhy a stojící vody. Důležitější než samotné číslo je kvalita a utěsnění švů. Svařené nebo přelepené švy zabrání průsaku, bez nich stan i s vysokým číslem propustí vodu.</p>'
          '<p>Nejběžnější materiály jsou polyester a nylon. Polyester méně nasákne a lépe odolává slunci, nylon bývá lehčí a pevnější, ale může se při promočení povolit. Ultralehké stany používají tkaniny s označením denier, například 15D. Čím nižší číslo, tím tenčí vlákno a lehčí tkanina, ale také menší odolnost proti poškrábání a propíchnutí. Stan nestavějte na ostrých kamenech bez podložky.</p>'
          '<h2>Tyčky, kolíky a odolnost proti větru</h2>'
          '<p>Hliníkové tyčky patří k lehkým a pevným. Skelná vlákna se hodí pro levnější modely a sezonní použití, jsou však těžší a při přetížení se mohou lámat. Kolíky nejsou jen příslušenstvím: v pevné zemi se hodí tvrdé hliníkové, v písku nebo ve sněhu širší typy. Vždy si vezměte náhradní kolíky a co nejvíc šňůr pro zesílení.</p>'
          '<p>Při bouři pomáhá správná orientace stanu čelem proti větru, plné napnutí přístřešku a ukotvení všech lanek. Stan nestavějte pod osamělými stromy ani v korytu potoka. Odolnost se řeší spolu s <a href="/stanove-kolky/">stanovými kolíky</a>, náhradními lanky a podložkou pod podlážku.</p>'
          '<h2>Větrání a kondenzace</h2>'
          '<p>Stan s jednou stěnou je lehký, ale v něm často kondenzuje voda. Dvouplášťové stany mají vnitřní stan prodyšný a vnější plášť (tropiko) vodotěsný, mezi nimi proudí vzduch. Při stavění nechte větrací otvory otevřené a ráno stan krátce otřete a vysušte. Vlhký obsah snižuje komfort a zkracuje životnost tkaniny a zipů.</p>'
          '<h2>Výběr podle sezóny a terénu</h2>'
          + T(['Podmínky', 'Na co se zaměřit', 'Související kategorie'], [
              ['Léto a nížiny', 'větrání, moskytiéra, nízká váha', '<a href="/hygiena-a-repelenty/">repelenty</a>'],
              ['Jaro a podzim', 'dvojitý plášť, kvalitní podlážka', '<a href="/dekove-spacaky/">spacáky</a>'],
              ['Hory a vítr', 'aerodynamický tvar, pevné tyčky', '<a href="/trekove-hole/">trekové hole</a>'],
              ['Bikepacking', 'malý obal, nízká váha', '<a href="/cyklo-tasky-a-nosice/">cyklotašky</a>'],
              ['Festivaly a kempy', 'rychlé stavění, prostornější předsíň', '<a href="/kempingovy-nabytek/">kempingový nábytek</a>'],
              ['Rybaření', 'robustní materiál, přístřešek', '<a href="/rybarske-stany/">rybářské stany</a>']]) +
          '<p>Většina stanů v kategorii je určena na tři roční období, tedy jaro až podzim. Skutečně zimní konstrukce s plnou sněhovou zátěží najdete v kategorii <a href="/expedicni-stany/">expedičních stanů</a>.</p>'
          '<h2>Co dalšího se hodí do výbavy</h2>'
          '<ul><li><strong>Podložka pod stan:</strong> chrání podlážku před ostrými kameny a vlhkem.</li>'
          '<li><strong>Karimatka:</strong> izolace od země je důležitější než samotný stan.</li>'
          '<li><strong>Čelovka:</strong> viz <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</li>'
          '<li><strong>Vařič:</strong> ve stanu se nikdy nevaří a v předsíni jen výjimečně a s větráním, kvůli riziku požáru i zplodinám; jinak vařte venku. Vařiče a kartuše najdete v kategorii <a href="/varice-a-kartuse/">vařiče a kartuše</a>.</li>'
          '<li><strong>Batoh:</strong> <a href="/turisticke-batohy/">turistický batoh</a> musí pojmout i stan.</li>'
          '<li><strong>Opravná sada:</strong> záplaty na tkaninu, náhradní spojka na tyčky.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Stan nikdy neskladujte vlhký. Po návratu ho postavte na zahradě nebo rozložte v bytě a nechte úplně oschnout, jinak vzniká plíseň a páchne. Čistěte vlažnou vodou a jemnou houbou, bez pracích prostředků a bez pračky. Zipy občas vyčistěte od písku a podle potřeby promažte speciálním prostředkem. Skladujte volně sbalený nebo v prodyšném pytli, ne v těsně stlačeném obalu po celou zimu. Tkaniny se postupně opotřebují vlivem UV záření, takže stan nenechávejte celé dny bez nutnosti na slunci.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Hmotnost bez kontroly:</strong> zjistěte, co udává výrobce a zda kolíky patří do váhy.</li>'
          '<li><strong>Příliš malá kapacita:</strong> údaj dvě osoby často znamená těsné ubytování.</li>'
          '<li><strong>Jen vodní sloupec:</strong> bez kvalitních švů je číslo k ničemu.</li>'
          '<li><strong>Špatný terén:</strong> lehký stan do bouřlivých hor bez zkušeností a zajištění.</li>'
          '<li><strong>Chybějící podložka:</strong> podlážka se poškodí dříve, než čekáte.</li>'
          '<li><strong>Nezkoušené stavění:</strong> stan poprvé zkuste doma, ne za tmy v dešti.</li></ul>'
          '<h2>Jak na nákup na Sportece</h2>'
          '<p>Vyberte počet osob a typ konstrukce a pak porovnejte váhu a rozměry. Tamtéž si všimněte, že v nabídce jsou i vojenské stany a levnější kopulové modely pro kempy, takže filtrujte podle značky a podle názvu. U zahraničních modelů sledujte dostupnost a dodací lhůtu. Rodinné modely najdete v <a href="/rodinne-stany/">rodinných stanech</a>, dětské hrací stany v <a href="/detske-stany/">dětských stanech</a>.</p>',
    faq=[('Jaký stan zvolit na pěší trek?', 'Lehký tunelový nebo ultralehký model pro jednu až dvě osoby s malým obalem. Zkontrolujte váhu, rozměr po složení, kvalitu švů a odolnost tyček proti větru.'),
         ('Co znamená vodní sloupec?', 'Je to hodnota odolnosti tkaniny proti pronikání vody. Důležitá je i kvalita švů a podlážka. Nejde o jediný ukazatel kvality, ale o orientační údaj pro srovnání.'),
         ('Kolik osob se skutečně vejde do dvouosobního stanu?', 'Dvě osoby, ale většinou bez většího zavazadla v ložnici. Pro pohodlí a uložení batohů si vyplatí zvolit model s předsíní nebo o jednu kapacitu větší.'),
         ('Jaký je rozdíl mezi tunelovým a kopulovým stanem?', 'Tunelový stan má rovnoběžné oblouky a nabízí víc prostoru za nižší váhu, ale vyžaduje správné ukotvení. Kopulový stan stojí samostatně a lépe zvládá změnu směru větru.'),
         ('Co znamená 15D nebo 20D u tkaniny?', 'Údaj denier popisuje tloušťku vlákna. Čím nižší číslo, tím lehčí a tenčí tkanina, ale také citlivější na poškození. Ultralehké stany tak vyžadují opatrnější zacházení.'),
         ('Je potřeba pod stan podložka?', 'Doporučuje se. Chrání podlážku před kameny, šiškami a vlhkostí. Podložka by neměla přesahovat okraj stanu, aby se pod něj nedostávala voda.'),
         ('Může se ve stanu vařit?', 'Ne. Vaření ve stanu představuje riziko požáru a otravy oxidem uhelnatým. Nejbezpečnější je vařit venku s odstupem od látky stanu; v předsíni jen výjimečně, s větráním a podle pokynů výrobce vařiče.'),
         ('Jak stan sušit a čistit?', 'Po návratu ho rozložte a nechte úplně vyschnout. Čistěte jen vlažnou vodou a jemnou houbou, bez pračky a bez agresivních prostředků. Teprve suchý skladujte.'),
         ('Hodí se turistický stan i pro festival nebo kemp?', 'Ano, pokud vám nevadí menší prostor. Pro festivaly se hodí samostavěcí modely s rychlým stavěním, pro delší pobyt v kempu spíš větší rodinný model.'),
         ('Jak poznat, že stan unese vítr?', 'Hledejte pevné tyčky, nízký profil, dostatek kotevních bodů a možnost zajistit všechna lanka. V praxi rozhoduje i správné postavení a kolíky vhodné do daného terénu.')])

# ------------------------------------------------------------------ sane-a-boby
NEW['sane-a-boby'] = dict(long=True,
    title='Sáně a boby: plastové, dřevěné, řiditelné a kluzáky',
    desc='Sáně a boby pro děti i dospělé: plastové, dřevěné, řiditelné, kluzáky a doplňky na sáňkování. Jak vybrat bezpečně a porovnat nabídky obchodů.',
    intro='<p>Sáňkování je jedna z nejjednodušších zimních radostí, ale vybrat správné sáně nebo bob už tak jednoduché není. V kategorii najdete <strong>plastové sáně a boby</strong>, tradiční dřevěné rohačky, řiditelné boby s volantem, kluzáky a doplňky k sáňkování. Konkrétní sortiment se mezi obchody mění. Rozdíly jsou v ovladatelnosti, rychlosti, nosnosti a také v tom, jak se s nimi dá nést do kopce.</p>'
          '<p>Porovnáváme nabídky obchodů u značek jako '
          + B(('sulov', 'Sulov'), ('merco', 'Merco'), ('plastkon', 'Plastkon'), ('gizmo-riders', 'Gizmo Riders'), ('acra-sport', 'ACRA Sport'), ('stiga', 'Stiga'), ('alpengaudi', 'AlpenGaudi'), ('prosperplast', 'Prosperplast')) +
          '. K zimní zábavě patří i <a href="/zimni-sporty/">zimní sporty</a>, <a href="/zimni-bundy/">zimní bundy</a>, <a href="/zimni-obuv/">zimní obuv</a> a <a href="/snezky/">sněžky</a>.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Základ nabídky tvoří sáně a boby, k nim přibývají doplňky a příslušenství. Při hledání proto pozorně čtěte název a popis a rozlišujte, zda kupujete celé sáně, nebo jen příslušenství.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Plastové sáně', 'lehké, tvarované, odolné proti vodě', 'děti, malé svahy, jednoduchá manipulace'],
              ['Dřevěné sáně', 'klasická konstrukce s ližinami', 'tradiční sáňkování, vyšší nosnost'],
              ['Plastové boby', 'tvarovaný korpus, většinou bez řízení', 'děti, rychlé svahy, jízda po sněhu'],
              ['Řiditelné boby', 'volant nebo řídicí tyče, někdy brzda', 'starší děti, dlouhé svahy'],
              ['Kluzáky a kruhy', 'nafukovací nebo pevné plastové', 'zábavné sjíždění, kratší svahy'],
              ['Sedačky a ohrádky', 'sedačka na sáně s opěrkou', 'malé děti podle věku, který uvádí výrobce'],
              ['Doplňky', 'provazy, popruhy, brzdy', 'tahání do kopce, bezpečnější jízda']]) +
          '<p>Název a popis produktu prozradí, zda jde o dětské, nebo dospělé sáně, jaká je nosnost a zda je v balení provaz nebo brzda. Výběr zúžíte zadáním konkrétního typu do hledání, třeba plastový bob nebo dřevěné sáně.</p>'
          '<h2>Sáně, nebo bob</h2>'
          '<p>Sáně mají obvykle sedadlo, ližiny nebo hladké dno a vezou jednoho až dva lidi. Dřevěné sáně se řídí nohama nebo tahem za provaz. Boby jsou tvarované, často s opěrkou zad, a bývají rychlejší. Řiditelné boby mají volant nebo ovládací páky, které zatáčejí lyže pod předkem. Přesto platí, že ovladatelnost bez brzd je omezená a rychlost roste s výškou svahu.</p>'
          '<p>Pro nejmenší děti se vyplatí sedačka s pásem a opěrkou nebo ohrádka, která jim brání z vozítka vypadnout. Starší děti ocení lehký plastový model, který zvládnou samy vytáhnout na kopec. Dospělí a rodiny hledají delší sáně s větší nosností nebo dvojitý bob.</p>'
          '<h2>Materiály a konstrukce</h2>'
          '<ul><li><strong>Polyetylen a polypropylen:</strong> nejčastější plasty u bobů a plastových saní. Jsou lehké, nenasákavé a v mrazu relativně odolné, ale při silném úderu mohou prasknout.</li>'
          '<li><strong>Dřevo:</strong> tradiční sáně s kovovými ližinami, těžší, pevné, vhodné pro delší sáňkování po upravené trati.</li>'
          '<li><strong>Kov:</strong> ližiny, rámy a řídicí mechanismy. Kontrolujte, zda nekorodují.</li>'
          '<li><strong>PVC a nafukovací materiály:</strong> kluzáky a kruhy, lehké a skladné, ale citlivé na ostré předměty.</li>'
          '<li><strong>Textilní prvky:</strong> sedačky, popruhy a polstrování.</li></ul>'
          '<h2>Bezpečnost na svahu</h2>'
          '<p>Sáňkování je zábava, ale svah ji může rychle změnit na úraz. Základem je vybrat vhodné místo bez stromů, kamenů, silnic a vodních ploch. Konec svahu musí být dostatečně dlouhý a volný, aby se dalo zastavit. Při jízdě se hodí lyžařská nebo cyklistická <a href="/detske-cyklohelmy/">dětská helma</a>, případně <a href="/lyzarske-helmy/">lyžařská helma</a>, a také <a href="/sportovni-rukavice/">rukavice</a>, <a href="/lyzarske-kalhoty/">nepromokavé kalhoty</a> a pevná obuv. Brýle jako <a href="/lyzarske-bryle/">lyžařské brýle</a> ochrání oči před sněhem.</p>'
          '<ul><li>Děti jezdí pod dohledem dospělých, malé děti vždy s opěrkou a pásem.</li>'
          '<li>Řiditelné boby zkoušejte nejdřív na mírném svahu.</li>'
          '<li>Na hustě navštívených svazích dávejte pozor na ostatní a jezděte vždy ve stejném směru.</li>'
          '<li>Nikdy nesáňkujte tam, kde končí svah silnicí nebo vodní plochou.</li>'
          '<li>Neberte sáně za autem ani za čtyřkolkou.</li>'
          '<li>Před jízdou zkontrolujte provazy, popruhy a řídicí mechanismus.</li></ul>'
          '<h2>Výběr podle věku a velikosti</h2>'
          + T(['Věk a situace', 'Co zvolit', 'Na co se zaměřit'], [
              ['Batolata', 'sáně se sedačkou a ohrádkou', 'opěrka zad, pás, bezpečný úchop pro rodiče'],
              ['Mladší děti', 'lehké plastové sáně nebo malý bob', 'nízká váha, úchyty, stabilita'],
              ['Starší děti', 'řiditelný bob nebo větší sáně', 'brzda, pevná konstrukce, nosnost'],
              ['Teenageři a dospělí', 'větší bob, dřevěné sáně, kluzák', 'nosnost, délka, ližiny'],
              ['Rodiny', 'dvoumístné sáně nebo bob', 'kapacita, bezpečný provaz, snadné nesení'],
              ['Pro hru na zahradě', 'kluzák, kruh, malé sáně', 'odolnost proti propíchnutí']]) +
          '<p>Nosnost vždy ověřte. Neplatí, že co se vejde, to unese: přetížené plastové boby praskají a dřevěné sáně se ohýbají. Výrobce obvykle uvádí maximální zatížení a doporučený věk uživatele.</p>'
          '<h2>Tahání do kopce a doprava</h2>'
          '<p>Vytáhnout sáně do kopce je polovina zábavy. Dobrá rukojeť a pevný provaz usnadní práci. Lehký plastový bob se dá nést pod paží, těžší dřevěné sáně vozte po sněhu za provaz. Do auta se ploché sáně vejdou přes sklopená sedadla, řiditelné boby zaberou víc místa. Při přepravě mimo auto je zajistěte popruhem, ať neletí.</p>'
          '<h2>Kam sáňkování zapadá</h2>'
          '<p>Vedle sáněk se na sněhu hodí i <a href="/detske-lyze/">dětské lyže</a>, <a href="/snowboarding/">snowboarding</a>, <a href="/brusle/">brusle</a> na zamrzlých plochách a pěší turistika se <a href="/snezky/">sněžnicemi</a>. Pro rodiny je to levnější a nenáročnější vstup do zimní sezóny než lyžování, protože nepotřebují permanentku ani výuku. Sáňkování se hodí i pro místa bez vleků, třeba pro kopec za domem nebo louku v parku.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po sezóně sáně očistěte od bláta, soli a vlhkosti. Plasty umyjte vlažnou vodou, dřevo osušte a občas ošetřete vhodným přípravkem. Ližiny z kovu lehce přetřete olejem, aby nezrezivěly. Nafukovací kluzáky vypusťte, osušte a uložte složené bez ostrých hran. Sáně skladujte v suchu a mimo přímé slunce, protože vlivem UV záření plast křehne. Před další zimou zkontrolujte praskliny a uvolněné šroubky.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Bob bez brzdy na prudký svah:</strong> bez možnosti zastavit se riskuje kolize.</li>'
          '<li><strong>Nesprávná nosnost:</strong> dospělý na dětském modelu poškodí konstrukci.</li>'
          '<li><strong>Chybějící provaz:</strong> pro malé děti je nutný.</li>'
          '<li><strong>Nafukovací kluzák na kamenitý terén:</strong> snadno se prorazí.</li>'
          '<li><strong>Koupě podle barvy:</strong> důležitější je tvar dna a pevnost materiálu.</li>'
          '<li><strong>Podcenění dojezdu:</strong> i pomalé sáně potřebují na konci svahu volný prostor, na kterém se dá zastavit.</li></ul>'
          '<h2>Jak na nákup na Sportece</h2>'
          '<p>Nejdřív si ujasněte, kdo bude sáňkovat a na jakém svahu. Pak vyfiltrujte značku a porovnejte nabídky obchodů. Nejvíce produktů nabízejí značky Sulov, Merco a Plastkon, rozšířené jsou i Gizmo Riders a Acra. Před objednáním si přečtěte popis, rozměry a nosnost. Sezóna začíná brzy, výběr bývá největší na podzim, a proto se vyplatí nenechávat nákup na první sníh.</p>',
    faq=[('Jaký je rozdíl mezi sáněmi a bobem?', 'Sáně mají ližiny nebo hladké dno a vezou vsedě, tradiční jsou dřevěné. Boby jsou tvarované a rychlejší, některé se řídí volantem. Vybírejte podle věku jezdce a sklonu svahu.'),
         ('Jaké sáně jsou vhodné pro nejmenší děti?', 'Sáně nebo sedačka s opěrkou zad, pásem a ohrádkou, aby dítě nevypadlo. Rodič je tahá za pevný provaz a jezdí jen po rovině nebo mírném svahu, vždy s dohledem.'),
         ('Jsou plastové boby bezpečné?', 'Při správném používání ano, ale bez brzdy a řízení záleží na terénu a opatrnosti. Používejte přilbu, vyberte svah bez překážek a s dlouhým volným dojezdem.'),
         ('Co znamená řiditelný bob?', 'Má volant nebo páky, kterými zatáčíte lyže pod předkem. Ovladatelnost je vyšší než u klasického bobu, ale stále vyžaduje zkušenost a zdravý rozum. Hodí se pro starší děti a dospělé.'),
         ('Jak poznat správnou nosnost?', 'Výrobce ji uvádí v popisu. Počítejte se součtem všech osob, které na sáně nasednou. Když je blízko hranice, vyberte větší model, protože plast může při přetížení prasknout.'),
         ('Hodí se nafukovací kluzáky na sníh?', 'Ano, na rovné a čisté plochy bez ostrých předmětů. Jsou lehké a zábavné, ale propíchnutí je snadné. Na kamenitých nebo zledovatělých svazích jsou nevhodné.'),
         ('Jak sáně uložit přes léto?', 'Očistěte je, osušte, kovové části lehce naolejujte a uložte v suchu a mimo přímé slunce. Nafukovací kluzáky vypusťte a složte. Před zimou zkontrolujte praskliny a šrouby.'),
         ('Jak si ve výpisu najdu konkrétní typ?', 'Zadejte do hledání název typu, třeba plastový bob, dřevěné sáně nebo kluzák, a případně vyfiltrujte značku. U každého produktu si pak přečtěte popis, rozměry, nosnost a doporučený věk uvedený výrobcem.'),
         ('Potřebuji helmu na sáňkování?', 'Doporučuje se, zejména pro děti a na svazích s větším sklonem nebo provozem. Lyžařská nebo cyklistická přilba ochrání hlavu při pádu či kolizi. Vždy ověřte, že sedí a je správně zapnutá.'),
         ('Na jakém svahu sáňkovat?', 'Na svahu bez stromů, kamenů, silnic a vodních ploch s dlouhým rovným dojezdem. Svah by měl být dobře přehledný a nepříliš prudký. Raději vybírejte místa určená k sáňkování.')])

# ------------------------------------------------------------------ rozšíření (ručně připojené sekce)
NEW['chladici-boxy']['intro'] = NEW['chladici-boxy']['intro'].replace('Rozdíly jsou v objemu', 'Rozdíly jsou hlavně v objemu')
NEW['chladici-boxy']['intro'] = NEW['chladici-boxy']['intro'].replace('a v tom, jak se s nimi nosí.', 'a v tom, jak se s nimi nosí, ale také v tom, kolik prostoru zabírají v kufru auta.')

NEW['kreatin']['guide'] += (
    '<h2>Příchutě, sladidla a snášenlivost složení</h2>'
    '<p>Neutrální prášek nemá chuť, a proto se bez problému rozpustí v jakémkoli nápoji. U příchuťových směsí výrobci přidávají sladidla, kyseliny, barviva a aromata. Pokud sledujete cukr ve stravě nebo máte potravinovou alergii, přečtěte si složení do detailu a při pochybnostech raději zvolte jednoduchý produkt. U tablet a kapslí se podívejte na obal tobolky: může být želatinová, nebo rostlinná, což je důležité pro vegany a vegetariány.</p>'
    '<h2>Velikost balení a rozumný nákup</h2>'
    '<p>Větší dózy bývají na jednu porci výhodnější, ale mají smysl jen tehdy, když je opravdu spotřebujete. Pokud doplněk zkoušíte poprvé, vezměte raději menší balení a nejprve si ověřte, že vám vyhovuje. Na stránce produktu často najdete více variant hmotnosti pod stejným názvem a obchody je řadí různě. Zkontrolujte, že u každé nabídky porovnáváte stejné balení, jinak vás může překvapit nečekaný rozdíl.</p>'
    '<ul><li>Pro vyzkoušení se hodí malé balení nebo balíček kapslí.</li>'
    '<li>Pro pravidelné užívání vezměte větší dózu, která vydrží několik týdnů.</li>'
    '<li>Do batohu a na cesty se hodí kapsle nebo jednodávkové sáčky.</li>'
    '<li>Do posilovny stačí malá nádobka, kterou doplníte z velkého balení.</li></ul>'
    '<h2>Doplněk stravy a pravidla prodeje</h2>'
    '<p>Doplňky stravy podléhají potravinářským předpisům a před uvedením na trh musí být oznámeny úřadům. Na obalu hledejte jméno a adresu výrobce nebo distributora, číslo šarže a datum trvanlivosti. Nic z toho nezaručuje, že konkrétní produkt vám bude vyhovovat, ale pomáhá to odlišit seriózní prodejce od neznámých dovozců. Sporteka ukazuje jen nabídky obchodů a zdravotní tvrzení nehodnotí.</p>')

NEW['sane-a-boby']['guide'] += (
    '<h2>Zimní oblečení na sáňkování</h2>'
    '<p>Při sáňkování se pohybujete málo, ale sedíte ve sněhu, a proto je důležité, aby oblečení nepropouštělo vlhkost. Vrstvěte podle zásady, kterou znáte z lyžování: <a href="/termopradlo/">termoprádlo</a> na tělo, teplá střední vrstva a nepromokavá svrchní vrstva. Na ruce patří vodotěsné rukavice, protože ty se při tahání provazu a sjezdu namáhají nejvíc. Kalhoty s membránou a zesíleným sedem ocení zejména děti, které se po sněhu válejí celé hodiny. Obuv by měla mít protiskluzovou podrážku a vysokou stulpnu, aby se do ní nenasypal sníh.</p>'
    '<h2>Sáňkování s dětmi krok za krokem</h2>'
    '<ol><li>Vyberte svah, který znáte, a před jízdou ho celý projděte.</li>'
    '<li>Nastavte pravidla: jede jeden, ostatní čekají nahoře, a pak se nejde zpátky přes dráhu.</li>'
    '<li>Zkontrolujte, zda je na sáních provaz a zda jsou všechny úchyty pevné.</li>'
    '<li>První jízdu absolvujte společně a ukažte, jak se brzdí patami nebo brzdou.</li>'
    '<li>Po sjezdu odneste sáně stranou, aby nepřekážely dalším jezdcům.</li></ol>'
    '<h2>Počasí, sníh a stav svahu</h2>'
    '<p>Nejlépe se jezdí po upěchovaném sněhu s pevným podkladem. Čerstvý prašan brzdí a sáně se do něj boří, naopak ledovatý svah je rychlý a nebezpečný. Za mokrého sněhu se plast lepí a jízda se zpomalí. Při velkém mrazu plast tvrdne a může prasknout, proto sáně v mrazu nenechávejte na zemi pod velkou zátěží. Za špatné viditelnosti, v mlze nebo za soumraku sáňkování raději odložte, protože si nevšimnete překážek.</p>')

NEW['turisticke-stany']['guide'] += (
    '<h2>Jak stan postavit správně</h2>'
    '<ol><li>Vyberte rovné místo bez kamenů, kořenů a prohlubní, kde se nehromadí voda.</li>'
    '<li>Rozložte podložku a na ni podlážku stanu. Okraje nesmí přečnívat.</li>'
    '<li>Sestavte tyčky a protáhněte je pouzdry nebo zacvakněte do háčků.</li>'
    '<li>Ukotvte rohy kolíky, nejdřív závětrnou stranu.</li>'
    '<li>Nasaďte vnější plášť, napněte ho a upevněte lanka.</li>'
    '<li>Otevřete větrací otvory a zkontrolujte, zda vnější plášť nedosedá na vnitřní stan.</li></ol>'
    '<h2>Bivak, hamaka, nebo stan</h2>'
    '<p>Stan nabízí nejlepší ochranu před hmyzem a deštěm, ale váží víc než jiné způsoby přespání. Lehčí alternativou je bivakovací pytel nebo plachta, které zaberou málo místa a rychle se staví. Hamaka je pohodlná mezi stromy, ale potřebuje spolehlivé úvazy a spodní izolaci. Přehled najdete v kategoriích <a href="/bivaky-a-kresla/">bivaky a křesla</a> a <a href="/hamaky/">hamaky</a>. Naopak pro delší pobyt a špatné počasí je stan nejspolehlivější, protože poskytuje vyšší soukromí a ochranu.</p>'
    '<h2>Předsíň, vchody a praktické detaily</h2>'
    '<p>Dva vchody dovolují dvěma osobám vystupovat nezávisle a lépe větrat. Předsíň slouží k odložení bot a batohů, ale zvětšuje váhu a rozměr. Vnitřní kapsy pomáhají udržet pořádek, háček pod stropem unese malou lampičku nebo čelovku. Reflexní lanka a barevné značky usnadní orientaci za tmy a snižují riziko zakopnutí. Zipy by měly mít chlopně proti dešti a pevné tahy, které se dají uchopit v rukavicích.</p>')

NEW['chladici-boxy']['guide'] += (
    '<h2>Chladicí vložky, led a jiné způsoby chlazení</h2>'
    '<p>Nejjednodušší je led z mrazničky, ale po rozmrznutí zůstane voda, která může potraviny zamokřit. Plastové chladicí vložky tohle neřeší, protože zůstávají uzavřené a po použití se dají znovu zmrazit. Praktické jsou i zmrzlé láhve s vodou: chladí a později poslouží jako pitná voda. Pokud chcete chlad udržet dlouho, využijte kombinaci: spodní vrstva vložky, uprostřed potraviny, nahoře další vložka. Suchý led se používá jen výjimečně a vyžaduje větrání, protože uvolňuje plyn. Pro běžný výlet není potřeba.</p>'
    '<h2>Bezpečnost potravin při chlazení</h2>'
    '<p>Rychle se kazí maso, ryby, mléčné výrobky a hotová jídla s majonézou. Pro takové potraviny je důležité, aby box zůstal studený po celou dobu. Obecně se doporučuje potraviny nenechávat dlouho při pokojové teplotě, zejména za horkého počasí. Syrové potraviny skladujte odděleně v uzavřených nádobách. Nápoje vložte do samostatné tašky nebo do vrchní části boxu, ať se potraviny nevystavují zbytečnému otevírání. Maso a mléčné výrobky držte pod 5 °C a v horku je nenechávejte venku déle než přibližně dvě hodiny. Při pochybnostech o stavu potraviny ji raději vyhoďte.</p>'
    '<h2>Doplňky a příslušenství</h2>'
    '<ul><li><strong>Chladicí vložky:</strong> opakovaně použitelné, různé tvary a velikosti podle boxu.</li>'
    '<li><strong>Košíky a přepážky:</strong> oddělí křehké potraviny od ledu.</li>'
    '<li><strong>Odnímatelná madla a popruhy:</strong> usnadní přenášení těžkého boxu.</li>'
    '<li><strong>Víko jako sedátko:</strong> některé pevné boxy unesou dospělého, ale ověřte nosnost výrobce.</li>'
    '<li><strong>Držák na pruty a nástrahy:</strong> rybáři oceňují boxy s kapsami na drobnosti, viz <a href="/rybarske-doplnky/">rybářské doplňky</a>.</li>'
    '<li><strong>Kolečka a výsuvné držadlo:</strong> pro cesty po pláži a po zpevněných cestách.</li></ul>'
    '<h2>Jak se box vejde do auta a do stanu</h2>'
    '<p>Před koupí si změřte nejen místo v kufru, ale i výšku pod sklopenou zadní policí. Vysoké boxy s víkem otevíraným nahoru potřebují volný prostor nad sebou. Ve stanu rozhoduje půdorys: rovnoměrný hranatý box se lépe zasune do rohu než kulatý. Pro kempování si prohlédněte i <a href="/kempingovy-nabytek/">kempingový nábytek</a>, protože box se často používá i jako stolek, a také <a href="/stany/">stany</a> s dostatečnou předsíní, kde zůstane chladný stín.</p>'
    '<h2>Sezónní tipy</h2>'
    '<p>V létě se vyplatí box ve stínu zakrýt světlou látkou, která odráží teplo. Na jaře a na podzim stačí menší model a méně chladicích vložek. V zimě se box hodí obráceně: zabrání zmrznutí nápojů nebo potravin, když přenášíte pití k autu. Při dlouhém skladování po sezóně box umyjte, vysušte a uložte s pootevřeným víkem, aby nevznikl zápach. Také se vyplatí zkontrolovat zámky a panty ještě před první akcí v dalším roce.</p>')

NEW['chladici-boxy']['guide'] += (
    '<h2>Ekologie a životnost</h2>'
    '<p>Dobrý pevný box vydrží mnoho sezón, takže se vyplatí investovat do robustnějšího kusu místo opakovaného nákupu levných tašek. Opravitelné jsou západky, madla i těsnění, které výrobci často prodávají jako náhradní díl. Pokud box už neslouží k chlazení, poslouží jako úložný kontejner na nářadí, rybářské vybavení nebo zahradní drobnosti. Měkké tašky po poškození izolace raději vyřaďte, protože už nechladí spolehlivě.</p>'
    '<h2>Jak číst parametry v e-shopu</h2>'
    '<p>Zaměřte se na vnitřní objem v litrech, vnější rozměry, hmotnost prázdného boxu a materiál. Údaje o počtu plechovek, které se vejdou dovnitř, berte jen orientačně, protože závisí na jejich uspořádání. Pokud výrobce uvádí dobu udržení chladu, hledejte i podmínky, za kterých ji měřil, jinak je porovnání mezi značkami zavádějící. Fotografie z různých úhlů napoví, zda má box odtok, kolečka a pevné zámky.</p>')

NEW['turisticke-stany']['guide'] += (
    '<h2>Hlučnost a komfort při spaní</h2>'
    '<p>Tenká tkanina se ve větru třepotá a hlučí, což může rušit spánek. Pomáhá dobře napnutý vnější plášť, pevné ukotvení všech lanek a vhodné místo za přírodní překážkou. Pro pohodlné spaní je důležitá i délka vnitřního stanu: vysoký člověk by se neměl dotýkat hlavou a nohama stěny, jinak do ní kondenzace nakape. U modelů s nízkým stropem se nedá sedět, což ocení spíš minimalisté než ti, kdo tráví ve stanu deštivé dny.</p>'
    '<h2>Ekonomika vlastnictví</h2>'
    '<p>Levnější stan může stačit na pár nocí ročně, ale při častém používání se vyplatí robustnější konstrukce s kvalitními tyčkami a švy. Počítejte i s příslušenstvím, které stan doplňuje: podložka, náhradní kolíky, opravná sada. Dobře ošetřený stan vydrží roky, proto po každé sezóně zkontrolujte švy, zipy a tyčky a drobné vady opravte dřív, než se zhorší.</p>')

NEW['sane-a-boby']['guide'] += (
    '<h2>Sáňkařské akce a závody</h2>'
    '<p>V mnoha horských střediscích existují upravené sáňkařské dráhy, kde se jezdí na půjčených i vlastních sáních. Někde se pořádají veřejné závody pro děti i dospělé, kde se hodí lehké dřevěné sáně s pevnými ližinami. Pokud vyrazíte na takovou dráhu, informujte se předem o pravidlech, povinné výbavě a časech provozu. Na vlastní sáně se někde nesmí, nebo se vyžaduje ochranná helma.</p>'
    '<h2>Praktické doplňky k zakoupení</h2>'
    '<p>K zimnímu vybavení se hodí termoska s teplým čajem, vyhřívané vložky do rukavic a náhradní ponožky. Ve vozítku pomůže měkká podložka pod sedák a pro rodiče píšťalka, kterou se dá na svahu dát dítěti znamení, že má zastavit. Sáně označte jménem nebo pestrou barvou, aby se po ukončení jízdy nepletly s ostatními.</p>')

NEW['turisticke-stany']['guide'] += (
    '<h2>Rodinný trek a stan pro dítě</h2>'
    '<p>S dětmi se vyplatí vzít stan o jednu velikost větší, než udává počet lidí, protože děti se v noci převalují a potřebují místo na hračky a oblečení. Zkraťte denní etapy a zvolte kempy s vodou v blízkosti. Dítěti dejte vlastní čelovku a ukažte mu, kde jsou zipy a jak se vychází ze stanu. Stejně jako dospělí potřebuje i ono izolaci od země, takže se vyplatí vzít si pěnovou nebo nafukovací karimatku.</p>')
