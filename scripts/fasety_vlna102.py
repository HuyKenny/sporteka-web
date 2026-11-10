"""sporteka.cz — facet landings wave 102: panska-mikina, vuch-batoh, osprey-batoh, nike-kratasy.
General facts only, no prices or product counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ panska-mikina
NEW['panska-mikina'] = dict(
    title='Pánská mikina: střih, materiál, kapuce a zip – průvodce',
    desc='Pánská mikina pro sport i volný čas. Jak se liší střih a velikosti, kdy zvolit kapuci, zip, bavlnu nebo fleece, a jak ji prát, aby vydržela.',
    intro='<p>Pánská mikina je kousek, který se nosí na trénink, na výlet i v kanceláři s uvolněným dress codem. Přesto se dvě mikiny stejné velikosti mohou obléknout zcela odlišně. Rozhodují ramena, délka rukávů a těla, hustota úpletu a to, zda jde o klasický střih, nebo o záměrně volný oversize. Tato stránka vybírá z kategorie <a href="/mikiny/">mikiny</a> jen modely určené pro muže, takže se nemusíte probírat dámskými a dětskými kusy.</p>'
          '<p>V textu rozebíráme rozdíly pánského střihu, materiály, typy zapínání a kapuce, velikosti i praktickou péči. Hledáte-li konkrétní značku, podívejte se na <a href="/nike-mikina/">Nike mikiny</a> nebo <a href="/gap-mikina/">Gap mikiny</a>, pro nenápadný kousek na každý den pak na <a href="/cerna-mikina/">černé mikiny</a>.</p>',
    guide='<h2>V čem se pánský střih liší od dámského a unisex</h2>'
          '<p>Pánské mikiny se šijí na širší ramena, rovnější linii boků a delší trup i rukávy. Dámský střih bývá užší v pase, kratší a s přiléhavějším výstřihem. Unisex modely se střihem blíží pánským, ale velikostní řada často začíná níž, takže je nosí i menší muži a ženy. Pokud jste štíhlejší postavy se širokými rameny, sedne vám klasický pánský střih; pokud máte spíš objemnější trup, zvažte o číslo větší a sledujte délku rukávu.</p>'
          '<p>U sportovní mikiny je podstatné, jak se chová při pohybu. Rukávy, které se při zvednutí paží vyhrnou nad zápěstí, nebo spodní lem, který vyjede nad pás, signalizují, že velikost není ideální. Dobrá mikina zůstává na svém místě i při předklonu a rukávy po zdvižení rukou neodhalí celé předloktí.</p>'
          '<h2>Typy pánských mikin podle konstrukce</h2>'
          + T(['Typ', 'Charakter', 'Kdy se hodí'], [
              ['Přes hlavu s kapucí (hoodie)', 'kapsa na břiše, stahovací šňůrka, nejuniverzálnější volba', 'volný čas, chladnější večery, cestování'],
              ['Přes hlavu bez kapuce (crewneck)', 'čistá linie u krku, snadno se vrství pod bundu', 'město, kancelář s volným oblékáním, trénink v hale'],
              ['Na zip přes celou délku', 'rychle se odepíná, reguluje teplo', 'turistika, cestování, doprava na kole'],
              ['Polozip (quarter zip)', 'krátký zip pod krkem, stojáček', 'běh za chladu, golf, sportovně elegantní styl'],
              ['Fleecová a funkční', 'hřejivá, lehká, rychleschnoucí', 'hory, výlety, podzimní a zimní aktivity']]) +
          '<p>Kapuce pomáhá u krku a při větru, ale rušívě působí pod batohem a v bundě s vlastní kapucí. Mikina bez kapuce se proto lépe vrství. Zip je praktický při potu a vrstvení, jen se zkontrolujte, zda má zip pod bradou ochrannou záložku, jinak může škrábat. Pokud potřebujete techničtější kus na turistiku, přejděte do kategorií <a href="/fleecove-mikiny/">fleecové mikiny</a> a <a href="/funkcni-mikiny/">funkční mikiny</a>.</p>'
          '<h2>Materiály: bavlna, polyester a směsi</h2>'
          '<p>Klasická mikina je z bavlněného úpletu s počesanou vnitřní stranou, díky níž je na dotek měkká a hřejivá. Bavlna dobře dýchá, ale pomalu schne a po zmoknutí je těžká. Polyester a jeho směsi se zmenšují méně, rychleji schnou a drží tvar, ale na kůži mohou působit chladněji a po opakovaném praní se snáz zachytí zápach. Směs bavlny s polyesterem je kompromis, který najdete u většiny sportovních značek.</p>'
          '<ul><li><strong>Bavlna:</strong> příjemná na denní nošení, hůř zvládá intenzivní pocení.</li>'
          '<li><strong>Směs bavlna a polyester:</strong> méně se mačká a zmenšuje, rychleji schne.</li>'
          '<li><strong>Polyesterový fleece nebo mikroflís:</strong> lehké teplo bez váhy, hodí se do hor a pod bundu.</li>'
          '<li><strong>Merino:</strong> přirozeně reguluje teplotu a méně zapáchá, ale vyžaduje šetrnou péči; vyzkoušíte ji v kategorii <a href="/merino-mikiny/">merino mikiny</a>.</li></ul>'
          '<h2>Gramáž a tloušťka: lehká nebo hřejivá</h2>'
          '<p>Hustota úpletu určuje, jak mikina hřeje. Tenká mikina z lehčího úpletu se nosí na jaro a podzim nebo do vytopené místnosti, silná počesaná slouží místo bundy na zimní procházky. Jedna mikina na všechna roční období obvykle nevyhovuje. Vhodnější je mít jednu tenčí vrstvu pod bundu a jednu silnější na doma nebo na večerní chlad.</p>'
          '<p>Při výběru si pomůžete i vzhledem úpletu. Francouzský frotír s drobnými smyčkami uvnitř dobře hřeje a působí sportovně, hladký jersey je elegantnější a méně objemný, plyšový fleece nejlépe izoluje, ale vypadá spíš outdoorově.</p>'
          '<h2>Velikosti a jak je zvolit</h2>'
          '<p>Pánské velikosti se obvykle značí od S do XXL, u některých značek i dál. Orientační velikost podle obvodu hrudníku najdete v tabulkách výrobce, ale nespoléhejte jen na ni. Americké a sportovní značky střihají volněji než evropské módní, a tak se může M u jedné značky obléknout jako L u jiné. Rozhodující je obvod hrudníku a délka rukávu změřené na dobře padnoucí mikině, kterou už máte.</p>'
          + T(['Požadovaný vzhled', 'Doporučení k velikosti'], [
              ['Přiléhavý sportovní střih', 'vaše běžná velikost, případně o číslo menší u volných značek'],
              ['Klasický střih', 'vaše běžná velikost; rukáv končí u zápěstí'],
              ['Volný streetwear (oversize)', 'o jedno až dvě čísla větší; ramena padají níž']]) +
          '<p>Mikina se po prvním praní může mírně srazit, hlavně bavlněná. Rozdíl mezi velikostmi snáz poznáte z tabulky než z fotky, takže ji před objednávkou vždy otevřete.</p>'
          '<h2>Co nosit s pánskou mikinou</h2>'
          '<p>Mikina funguje jako střední vrstva. Pod ni patří funkční nebo bavlněné <a href="/sportovni-tricka/">sportovní tričko</a>, na ni lehká bunda z kategorie <a href="/sportovni-bundy/">sportovní bundy</a>. Dole ladí s <a href="/teplaky/">tepláky</a>, sportovními kalhotami i džíny. Dvojice mikiny a kalhot ze stejného materiálu vytváří klasickou soupravu, ale i kus z odlišného úpletu působí upraveně, když sedí barva.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Pánské mikiny dodávají zejména sportovní, streetwearové a outdoorové značky: ' + B(('nike', 'Nike'), ('champion', 'Champion'), ('adidas', 'Adidas'), ('gap', 'Gap'), ('under-armour', 'Under Armour'), ('puma', 'Puma'), ('columbia', 'Columbia'), ('fjallraven', 'Fjällräven'), ('the-north-face', 'The North Face'), ('helly-hansen', 'Helly Hansen'), ('fila', 'Fila'), ('tommy-hilfiger', 'Tommy Hilfiger')) + '. Sportovní značky sázejí na logo a materiál pro pohyb, módní na střih a barvy, outdoorové na funkci a odolnost. Fanouškovské mikiny týmů a lig tvoří zvláštní skupinu: mají výrazný potisk, ale střih je pohodlný a rozměry volné.</p>'
          '<h2>Péče o pánskou mikinu</h2>'
          '<ul><li>Perte naruby, aby se potisk a vnější úplet méně otíral. Výšivky a gumové potisky tak vydrží déle.</li>'
          '<li>Volte nižší teplotu a jemnější program, tmavé barvy perte zvlášť, aby neodbarvovaly.</li>'
          '<li>Aviváž u funkčních materiálů vynechte, snižuje jejich schopnost odvádět vlhkost.</li>'
          '<li>Sušte volně, bez radiátoru. Vysoké teploty srážejí bavlnu a poškozují potisk.</li>'
          '<li>Při žmolkování pomůže odžmolkovač; vyvarujte se tření o hrubé povrchy, třeba popruhy batohu.</li></ul>'
          '<h2>Jak výběr zúžit</h2>'
          '<p>Ujasněte si nejdřív účel: trénink, město nebo hory. Pak zvolte typ zapínání, materiál a teprve potom značku a barvu. Po výběru se vyplatí porovnat dostupnost jednotlivých velikostí, protože oblíbené barvy se v nejběžnějších číslech vyprodávají jako první. Chcete-li zjistit, jak vypadá celá nabídka bez omezení na pohlaví, otevřete základní kategorii <a href="/mikiny/">mikiny</a>.</p>',
    faq=[
        ('Jak poznám, že jde opravdu o pánskou mikinu?', 'Pánské modely mají širší ramena, rovnější boky a delší rukávy a v názvu nebo popisu bývá označení pánská, men nebo male. Při nejasnostech si ověřte velikostní tabulku výrobce. Unisex kusy jsou určeny oběma pohlavím.'),
        ('Jakou velikost vybrat, když jsem mezi dvěma?', 'Pokud preferujete volnější nošení nebo budete mikinu vrstvit přes tričko a pod bundu, berte větší. Pro přiléhavý sportovní vzhled a vyšší štíhlost se hodí menší velikost. Orientujte se hlavně podle obvodu hrudníku a délky rukávu.'),
        ('Je lepší mikina s kapucí, nebo bez?', 'S kapucí je univerzální a hřeje u krku, bez kapuce se lépe vrství pod bundu a pod batoh. Pro běh a trénink v hale vyhovuje spíš bez kapuce, pro volný čas a chladné večery s kapucí.'),
        ('Hodí se mikina jako vrstva do hor?', 'Bavlněná mikina je na hory vhodná jen na krátké procházky, protože pomalu schne. Pro delší túru zvolte fleecovou nebo funkční mikinu z polyesteru či merina, která odvádí pot a dá se pod bundou nosit celý den.'),
        ('Srazí se mikina po praní?', 'Bavlněné mikiny se mohou po prvních praních mírně srazit, hlavně při vysoké teplotě a sušení v sušičce. Perte při nízké teplotě, sušte volně a velikost volte s ohledem na tuto drobnou změnu.'),
        ('Jak vyprat potištěnou mikinu, aby potisk vydržel?', 'Obraťte ji naruby, použijte nižší teplotu a jemnější program a nepoužívejte aviváž. Neždímejte na vysoké otáčky a nežehlete přímo přes potisk, nýbrž z rubu.'),
        ('Co je to oversize mikina a jak ji nosit?', 'Oversize je záměrně volný střih s nízkými rameny a delším trupem. Obvykle se kupuje o jedno až dvě čísla větší než klasická velikost. Dobře se nosí s užšími kalhotami, aby celek nepůsobil příliš objemně.'),
        ('Jaký je rozdíl mezi mikinou a fleecem?', 'Mikina je z úpletu, nejčastěji bavlněného, s hladkým povrchem a počesaným vnitřkem. Fleece je syntetický materiál s rouškem s chlupatým povrchem, lehčí, rychleji schne a lépe izoluje při stejné váze, ale nevypadá tak neutrálně do města.'),
        ('Kam se dostanu, když chci pánskou mikinu určité značky?', 'Použijte stránky značek, například Nike mikiny nebo Gap mikiny, případně filtry v základní kategorii. Ceny a dostupnost se u jednotlivých obchodů mění, proto se srovnání vyplatí před nákupem znovu otevřít.'),
        ('Jak dlouho vydrží kvalitní pánská mikina?', 'Při šetrné péči, nižším praní a bez sušičky vydrží i několik sezon. Nejrychleji se obnošují manžety a lem, hustší úplet drží tvar déle. Kvalitu poznáte podle pevných švů a rovnoměrně počesaného vnitřku.')
    ])

# ------------------------------------------------------------------ vuch-batoh
NEW['vuch-batoh'] = dict(
    title='Vuch batoh: městské a módní batohy, jak vybrat model',
    desc='Vuch batohy: městské módní modely, jak se liší velikostí a střihem, na co se hodí, kdy zvolit turistický batoh a kde se vyplatí porovnat nabídky.',
    intro='<p>Vuch je česká značka, která se zaměřuje na městské batohy, tašky a drobnou módní galanterii. Její batohy jsou určené do školy, do práce, na nákup a na každodenní nošení, nikoli na vícedenní túry. Nabídka je rozsáhlá a v mnoha modelech se opakují podobné názvy v různých barvách, takže se v ní snadno ztratíte. Tato stránka pomáhá vybrat správný tvar, velikost a barvu a ukazuje, kdy má smysl sáhnout po jiné značce.</p>'
          '<p>Pokud hledáte batoh na hory, začněte u <a href="/turisticke-batohy/">turistických batohů</a>. Pro školu jsou tu <a href="/skolni-batohy/">školní batohy</a>, pro každodenní nošení <a href="/mestske-batohy/">městské batohy</a>. Hledáte-li širší srovnání, otevřete <a href="/batohy/">kategorii batohy</a>.</p>',
    guide='<h2>Pro koho je Vuch batoh určený</h2>'
          '<p>Většina modelů Vuch míří na ženy a dívky, ale najdete i neutrální kusy v černé, šedé nebo béžové, které nosí všichni. V nabídce se objevují menší batůžky, běžné denní batohy a nákupní tašky ve tvaru batohu. Společné mají městský charakter: elegantní design, jednoduché kapsy a materiály, které nejsou stavěné na deštný prales, ale na každodenní cestování MHD.</p>'
          '<p>Značku volí lidé, kteří chtějí batoh jako módní doplněk. Pokud potřebujete nosný systém s bederním pásem, nastavitelnou délku zad nebo velký objem na stan a spacák, bude lepší technická značka. Vuch je přesně opačný přístup: lehký, jednoduchý a stylový.</p>'
          '<h2>Jak se liší jednotlivé řady</h2>'
          '<p>Značka pojmenovává modely křestními jmény, třeba Mellora, Linton, Glenn, Corbin, Joanna, Eloa nebo Lien, a každý má několik barevných variant. Názvy se v obchodech někdy zkracují nebo píší různě, a tak se stává, že stejný batoh je uveden pod dvěma podobami názvu. Při porovnání proto sledujte konkrétní barvu a obrázek, ne jen jméno.</p>'
          + T(['Typ modelu', 'Charakter', 'Hodí se na'], [
              ['Malý městský batůžek', 'kompaktní tvar, málo kapes, lehký', 'doklady, telefon, drobnosti na večer'],
              ['Denní batoh střední velikosti', 'hlavní komora, přední kapsa, popruhy', 'práce, škola, nákup, výlet'],
              ['Batoh s ozdobným potiskem', 'puntíky, květiny, výrazné vzory', 'módní doplněk ke každodennímu oblečení'],
              ['Nákupní taška s batohovým nošením', 'prostorná komora, jednoduché zapínání', 'nákupy a lehké přenášení']]) +
          '<p>Přesné rozměry si vždy ověřte v popisu u obchodu; výrobci uvádějí objem a rozměry pro jednotlivé modely a barvy se v tomto ohledu nemění.</p>'
          '<h2>Kolik se do městského batohu vejde</h2>'
          '<p>Městský batoh na každodenní nošení má obvykle menší objem než turistický. Do menšího se vejde peněženka, klíče, láhev, drobné kosmetické a hygienické věci a svačina. Střední denní batoh pojme navíc sešity, tenčí notebook nebo tablet a lehkou mikinu. Když potřebujete přenést notebook, zkontrolujte, zda má batoh vyztuženou přihrádku nebo aspoň dostatečně široký hlavní prostor.</p>'
          '<ul><li><strong>Dokumenty a formát A4:</strong> hlavní komora musí být dost vysoká, aby se desky nepřehýbaly.</li>'
          '<li><strong>Láhev:</strong> boční kapsa je pohodlnější než nošení uvnitř, kde láhev při úniku zmáčí vše ostatní.</li>'
          '<li><strong>Cennosti:</strong> skrytá kapsa na zádech nebo uvnitř víka je bezpečnější než vnější zip.</li>'
          '<li><strong>Zavírání:</strong> zip je spolehlivější než patent, přezka s klopou vypadá elegantněji, ale otvírá se pomaleji.</li></ul>'
          '<h2>Pohodlí a nošení</h2>'
          '<p>Městský batoh nemá bederní pás a zátěž nese celou na ramenou, proto nedoporučujeme plnit ho těžkými věcmi. Popruhy by měly být alespoň částečně polstrované a nastavitelné, aby batoh sedl na záda, ne se houpal v pasu. Pokud nosíte batoh dlouho, vyplatí se zadní stěna s lehkou výplní, která tlumí tlak předmětů uvnitř.</p>'
          '<p>Příliš plný batoh na zádech působí nevzhledně a namáhá švy a zipy. Nechte uvnitř trochu místa a vyndejte věci, které nepotřebujete. Těžké předměty ukládejte co nejblíž k zádům, lehké dopředu.</p>'
          '<h2>Barvy a materiály</h2>'
          '<p>Nejčastěji se nabízí černá, šedá, béžová, vínová, hnědá a zelená. Tmavé barvy skryjí otěry a nečistoty, světlé a béžové jsou elegantní, ale rychleji se špiní, zvlášť u dna. Šedá je praktický kompromis. U světlých batohů se vyplatí impregnační sprej, který odpuzuje vodu a drobné skvrny; vyzkoušejte ho nejdřív na skrytém místě. Pokud hledáte nenápadný kus, podívejte se na <a href="/cerny-batoh/">černé batohy</a>.</p>'
          '<h2>Kdy zvolit jinou značku</h2>'
          '<p>Vuch není určen pro náročný terén, pro vícedenní trasy ani pro sportovní využití s bederním pásem. Pro tyto účely se hodí batohy ostatních značek. Zvažte například ' + B(('osprey', 'Osprey'), ('deuter', 'Deuter'), ('the-north-face', 'The North Face'), ('husky', 'Husky'), ('baagl', 'Baagl')) + '. Podrobněji o jednotlivých značkách pojednávají stránky <a href="/osprey-batoh/">Osprey batoh</a>, <a href="/deuter-batohy/">Deuter batohy</a>, <a href="/the-north-face-batoh/">The North Face batoh</a>, <a href="/batoh-husky/">Batoh Husky</a> a <a href="/baagl-batoh/">Baagl batoh</a>. Pro školáky s ortopedickým systémem se hodí spíše <a href="/skolni-batohy/">školní batohy</a>.</p>'
          '<h2>Dámský, pánský nebo unisex</h2>'
          '<p>Mnoho modelů je označeno jako dámský batoh, ale značení se týká hlavně vzhledu, ne konstrukce. Městské batohy nemají tak výrazný rozdíl v nosném systému jako turistické. Podívejte se i na <a href="/damsky-batoh/">dámské batohy</a> a <a href="/pansky-batoh/">pánské batohy</a>, kde najdete další značky.</p>'
          '<h2>Péče o městský batoh</h2>'
          '<ul><li>Vyprázdněte všechny kapsy a vysajte nebo vyklepejte drobky a písek.</li>'
          '<li>Skvrny odstraňte vlhkým hadříkem s jemným mýdlem, nepoužívejte ostré čisticí prostředky.</li>'
          '<li>Do pračky ho dávejte jen tehdy, když to výrobce dovoluje; jinak hrozí odlepení podšívky a výztuh.</li>'
          '<li>Sušte ho otevřený a ve stínu, ne na radiátoru.</li>'
          '<li>Zipy občas očistěte kartáčkem a dle potřeby je ošetřete voskem nebo mýdlem.</li></ul>'
          '<h2>Na co se před koupí podívat</h2>'
          '<p>Porovnejte objem, rozměry a materiál. Zkontrolujte, zda je v ceně i příslušenství, jako je pouzdro nebo vnitřní organizér. Vyplatí se projít recenze, protože se u městských módních batohů nejčastěji řeší tvrdost popruhů a kvalita zipů. Pokud si nejste jistí, jaký objem vybrat, porovnejte ho s batohem, který už používáte.</p>',
    faq=[
        ('Jaké batohy značka Vuch vyrábí?', 'Zaměřuje se na městské a módní batohy, tašky a drobnou galanterii. Najdete malé batůžky, denní batohy i nákupní tašky, často v černé, šedé, béžové či v dalších barvách s ozdobným potiskem.'),
        ('Je batoh Vuch vhodný do školy?', 'Pro studenty a starší žáky ano, pokud nenosí příliš těžké učebnice. Pro menší děti zvolte školní batoh s ortopedickou zádovou částí a pevnějším dnem, který se hledá v kategorii školní batohy.'),
        ('Vejde se do batohu Vuch notebook?', 'Záleží na modelu. Větší denní batohy zpravidla pojmou tenký notebook nebo tablet, malé městské batůžky ne. Před koupí si ověřte vnitřní rozměry v popisu obchodu a porovnejte je s notebookem.'),
        ('Hodí se Vuch na turistiku?', 'Na krátkou procházku po městě nebo v parku ano, na vícedenní túru ne. Chybí mu bederní pás, větraná záda a nosná konstrukce. Pro hory použijte turistický batoh.'),
        ('Je batoh Vuch pro ženy, nebo pro muže?', 'Většina modelů míří spíš na ženy, ale neutrální barvy a jednoduché tvary nosí i muži. Rozdíly ve stavbě nejsou tak výrazné jako u turistických batohů, proto rozhoduje hlavně vzhled a velikost.'),
        ('Jak poznám, že dva různé názvy jsou stejný batoh?', 'Obchody názvy zkracují, přepisují a přidávají slova jako backpack nebo dámský batoh. Porovnávejte podle jména modelu, barvy a obrázku, případně podle rozměrů a objemu.'),
        ('Jak vyčistit světlý batoh?', 'Vlhkým hadříkem s jemným mýdlem a šetrně na skvrnách. Neperte ho v pračce, pokud to výrobce výslovně nedovoluje, a suste volně. Před nošením můžete povrch ošetřit impregnací.'),
        ('Jaký objem batohu je vhodný pro každodenní nošení?', 'Pro nejnutnější věci stačí malý batůžek, na dokumenty, láhev a svačinu střední denní batoh. Pro notebook a více vrstev oblečení zvolte větší, ale vyhněte se zbytečně velkému, který lákne k přeplnění.'),
        ('Čím se liší městský batoh od turistického?', 'Městský je lehčí, jednodušší a vzhledově cílený, bez bederního pásu a větrání. Turistický má nosný systém, který přenáší váhu na boky, nastavitelnou délku zad a objem do desítek litrů. Určuje se tedy podle zátěže a délky nošení.')
    ])

# ------------------------------------------------------------------ osprey-batoh
NEW['osprey-batoh'] = dict(
    title='Osprey batoh: turistické, městské a cestovní modely',
    desc='Osprey batohy pro hory, město i cesty: řady a velikosti, rozdíl mezi pánskými a dámskými modely, délka zad a bederní pás, na co si dát pozor při výběru.',
    intro='<p>Osprey je americká značka specializovaná na batohy, od malých denních modelů po velké expediční kusy, které se prodávají po celém světě. Pověst si udělala dobře padnoucími nosnými systémy, promyšlenými kapsami a širokou nabídkou velikostí. V katalogu najdete turistické batohy, lehké denní batohy, městské modely, cestovní tašky i příslušenství jako pouzdra na notebook nebo vak na boty.</p>'
          '<p>Značka často nabízí pánskou a dámskou verzi stejného typu, takže má smysl vědět, čím se liší. V další části vysvětlujeme, jak číst názvy řad, jak změřit délku zad, kdy volit větší objem a kdy stačí lehký batůžek. Související kategorie: <a href="/batohy/">batohy</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    guide='<h2>Jak číst názvy řad Osprey</h2>'
          '<p>Osprey pojmenovává řady a za názvem uvádí číslo, nejčastěji objem v litrech. Například model s číslem 58 znamená objem kolem 58 litrů. K tomu se přidává označení velikosti, třeba S/M nebo L/XL, které se týká délky zad. Dvě stejně pojmenované řady se můžou lišit generací, proto sledujte i označení II nebo podobné.</p>'
          + T(['Skupina', 'Příklady řad', 'Hodí se na'], [
              ['Velké trekové batohy', 'Aether, Ariel, Kestrel, Kyte, Renn, Rook, Porter', 'vícedenní túry, cestování s ubytováním ve stanu či horské chatě'],
              ['Denní turistické batohy', 'Talon, Tempest, Hikelite, Sportlite, Stratos, Eja, Sirrus', 'jednodenní výlety, via ferrata, lehká turistika'],
              ['Lehké a běžecké batohy', 'Duro, Dyna, Katari, Syncro, Skarab, Raven', 'běh v terénu, kolo, rychlé a lehké túry'],
              ['Městské a lifestylové batohy', 'Arcane, Aoede, Daylite, Metron, Glade', 'práce, škola, každodenní nošení'],
              ['Cestovní tašky a kufry', 'Transporter, Airporter, Ozone', 'letecká přeprava a cestování mezi městy']]) +
          '<p>Seznam shrnuje typické zaměření; konkrétní dostupnost řad se v čase mění, takže si vždy zkontrolujte aktuální nabídku. Název modelu pak řekne víc než kategorie obchodu.</p>'
          '<h2>Pánský a dámský střih</h2>'
          '<p>Osprey dlouhodobě vyrábí oddělené pánské a dámské verze. Dámské mají užší a kratší nosný systém, tvarovaná ramenní popruhy, aby netlačily na hrudník, a bederní pás přizpůsobený širším bokům. Dvojice jako Kestrel a Kyte, Talon a Tempest nebo Aether a Ariel jsou klasické příklady: stejná konstrukce, odlišný střih. Muži s menší postavou a ženy s vyšší postavou ale mohou zvolit opačný typ, pokud jim lépe sedí. Rozhoduje délka zad a obvod boků, ne jen pohlaví.</p>'
          '<h2>Délka zad a bederní pás</h2>'
          '<p>Správná velikost batohu se nezjišťuje podle výšky těla, nýbrž podle délky zad. Měří se od sedmého krčního obratle, který vyčnívá při předklonu hlavy, k hřebenům pánevních kostí. Hodnotu porovnejte s tabulkou výrobce a vyberte velikost. U řady modelů lze bederní pás a ramenní popruhy vyměnit nebo upravit, což pomůže, pokud jste mezi velikostmi.</p>'
          '<ul><li><strong>Bederní pás:</strong> by měl obepínat boky, ne pas. Většina váhy má jít na boky.</li>'
          '<li><strong>Ramenní popruhy:</strong> mají objímat rameno bez mezery a nevykazovat tlak.</li>'
          '<li><strong>Stabilizační popruhy nad rameny:</strong> přitahují batoh k zádům a omezují houpání.</li>'
          '<li><strong>Hrudní popruh:</strong> zabraňuje sjíždění ramenních popruhů.</li></ul>'
          '<h2>Větrání zad</h2>'
          '<p>U turistických batohů se setkáte se dvěma základními konstrukcemi zad. Napnutá síťovina vytváří vzduchovou mezeru mezi zády a batohem a dobře odvádí pot, zato batoh stojí o něco dál od těla. Přiléhavá záda s polstrováním drží váhu blíž, což se hodí pro lyžování, kolo a zimní túry, kde je pot menší problém než stabilita. Zvolte podle sezony a typu aktivity.</p>'
          '<h2>Jaký objem zvolit</h2>'
          '<p>Objem se odvíjí od délky výletu a vybavení. Velké batohy lákají k přebalování, ale prázdný velký batoh se hůř stahuje a je zbytečně těžký.</p>'
          + T(['Objem', 'Použití'], [
              ['do 15 litrů', 'běh, kolo, krátké výlety, městské nošení'],
              ['15 až 30 litrů', 'jednodenní túry, ferraty, škola, cestování s lehkým zavazadlem'],
              ['30 až 45 litrů', 'víkend s přespáním v chatě, lehká výbava, zimní túra na den'],
              ['45 až 65 litrů', 'vícedenní trek s přespáním ve stanu'],
              ['nad 65 litrů', 'expedice, zimní výpravy, nošení dětí a nákladu']]) +
          '<p>Chystáte-li výpravu se stanem, k batohu se hodí <a href="/stany/">stan</a> i <a href="/spaci-pytle/">spací pytel</a>, které se upevňují do spodní komory nebo pod víko. Pro běh a rychlé trasy zkoumejte i kategorii <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>.</p>'
          '<h2>Městské a cestovní řady</h2>'
          '<p>Osprey nabízí i městské batohy s přihrádkou na notebook, organizéry a diskrétním vzhledem. Řady jako Arcane se hodí do práce nebo do školy, Daylite na lehké denní výlety a na doplněk do většího batohu. Cestovní tašky Transporter a Airporter se nosí jako batoh nebo taška, vydrží náročné zacházení a pomáhají při přepravě v letadle. K dispozici jsou také pouzdra a tašky na boty. Další městské typy najdete v kategorii <a href="/mestske-batohy/">městské batohy</a>.</p>'
          '<h2>Osprey ve srovnání s dalšími značkami</h2>'
          '<p>Hlavními konkurenty jsou ' + B(('deuter', 'Deuter'), ('the-north-face', 'The North Face'), ('salewa', 'Salewa'), ('lowe-alpine', 'Lowe Alpine'), ('fjallraven', 'Fjällräven')) + '. Deuter patří k evropským značkám s důrazem na větrání zad, Fjällräven je známý městským a módním designem, Salewa a Lowe Alpine sázejí na alpské využití. Osprey je v nabídce uznávaný zejména pro velikostní řady a nastavitelnost. Podrobnější náhled vám dají stránky <a href="/deuter-batohy/">Deuter batohy</a> a <a href="/the-north-face-batoh/">The North Face batoh</a>.</p>'
          '<h2>Co se hodí k batohu</h2>'
          '<p>Zbytek výbavy dokončí nepromokavý obal, hydratační vak, popruhy na hole a organizéry. Před sezonou zkontrolujte švy, zipy a přezky. Po výletech batoh vyprázdněte, vytřepejte a nechte uschnout; stlačené vlhké oblečení uvnitř způsobuje zápach i plísně.</p>',
    faq=[
        ('Jaká je nejlepší řada Osprey pro jednodenní túry?', 'Záleží na objemu a stylu. Pro běžné výlety se hodí lehké denní řady kolem dvaceti až třiceti litrů s větranými zády, například Talon a Tempest nebo Hikelite. Vybírejte podle délky zad a typu kapes.'),
        ('Jak změřit délku zad pro Osprey?', 'Najděte sedmý krční obratel, který při předklonu vyčnívá, a změřte vzdálenost k hřebenům pánevních kostí. Výsledek porovnejte s tabulkou výrobce a vyberte velikost batohu.'),
        ('Čím se liší pánské a dámské batohy Osprey?', 'Dámské verze mají kratší a užší nosný systém, tvarovaná ramenní popruhy a přizpůsobený bederní pás. Konstrukce je jinak obdobná. Rozhodujte podle toho, co vám sedí, ne jen podle označení.'),
        ('Jaký objem potřebuji na vícedenní trek?', 'Pro trek s přespáním ve stanu se obvykle hodí batoh kolem padesáti až šedesáti litrů, podle množství jídla a výbavy. Na chatovou túru s lehkým zavazadlem stačí méně.'),
        ('Je Osprey vhodný i do města?', 'Ano, značka vyrábí městské a cestovní řady s přihrádkou na notebook a organizéry. Pro dojíždění vyberte menší model s odolným materiálem a pevnými popruhy.'),
        ('Jak poznám, že mi batoh sedí?', 'Bederní pás má spočívat na kostech pánve, ramenní popruhy mají objímat rameno bez mezery a po zatížení nesmí batoh sjíždět. Vyzkoušejte ho naplněný váhou, kterou budete nosit.'),
        ('Jak pečovat o turistický batoh?', 'Po výletu vyprázdněte kapsy, vytřepejte nečistoty a nechte batoh uschnout na vzduchu. Skvrny odstraňte vlhkým hadříkem, neperte jej agresivně ani v pračce, pokud to výrobce výslovně nedovoluje.'),
        ('Na co se vyplatí podívat u levnějších starších kolekcí?', 'Ověřte, že máte k dispozici potřebnou velikost záda a že se nejedná o nekompletní model bez příslušenství. Starší řady mohou mít jiný systém nastavení, ale základní funkce zůstává stejná.'),
        ('Mohu s batohem Osprey cestovat letadlem?', 'Cestovní řady jsou na přepravu přizpůsobeny, ale pravidla pro příruční zavazadla určují dopravci. Ověřte rozměry kabinového zavazadla u své aerolinky a porovnejte je s rozměry batohu.')
    ])

# ------------------------------------------------------------------ nike-kratasy
NEW['nike-kratasy'] = dict(
    title='Nike kraťasy: běh, trénink, fotbal i volný čas – průvodce',
    desc='Nike kraťasy pro běh, trénink, fotbal, basketbal i každodenní nošení. Jak se liší délka nohavic, podšívka, střih a velikosti a jak vybrat správný pár.',
    intro='<p>Nike nabízí kraťasy pro většinu sportů a také pro volný čas, a názvy modelů proto stojí za rozluštění. Označení jako Challenger, Stride, Club, Pro, Flex nebo Academy naznačují zaměření, a délka nohavic v palcích určuje, jak kraťasy vypadají a jak se v nich pohybujete. Stránka porovnává nabídky obchodů u kraťasů a šortek Nike pro muže, ženy i děti a pomáhá rozlišit, který model se hodí na běh, který do posilovny a který na každodenní nošení.</p>'
          '<p>V textu vysvětlujeme rozdíly mezi řadami, nohavice, podšívky a materiály a ukazujeme, jak vybrat velikost. Pokud porovnáváte víc značek, najdete další možnosti v těchto sekcích: otevřete kategorii <a href="/sportovni-kratasy/">sportovní kraťasy</a> nebo stránky <a href="/gymbeam-kratasy/">GymBeam kraťasy</a> a <a href="/jordan-kratasy/">Jordan kraťasy</a>.</p>',
    guide='<h2>Co znamenají názvy řad Nike</h2>'
          '<p>Nike dělí kraťasy podle použití, a pokud rozumíte názvům, vyberete správně rychleji. V katalogu se opakují řady, které se liší účelem, materiálem a střihem.</p>'
          + T(['Řada', 'Zaměření', 'Typické vlastnosti'], [
              ['Challenger, Stride, Tempo, Swift', 'běh', 'lehký materiál, odvádění potu, často vnitřní slipy'],
              ['Pro', 'přiléhavé a kompresní', 'elastické, těsné k tělu, jako spodní vrstva i samostatně'],
              ['Club, Sportswear', 'volný čas', 'bavlněný nebo flísový úplet, kapsy, pohodlný pas'],
              ['Form, Flex, Multi', 'trénink a posilovna', 'strečový nebo tkaný materiál, volný střih'],
              ['Academy, Strike, Park', 'fotbal a týmové sporty', 'lehký polyester, větraný střih'],
              ['DNA, Icon', 'basketbal', 'delší nohavice, široký střih'],
              ['Court', 'tenis a raketové sporty', 'lehký tkaný materiál s kapsami na míčky']]) +
          '<p>Rozdělení je orientační, protože se řady mění po sezonách. Přesné určení vždy najdete v popisu u konkrétního obchodu.</p>'
          '<h2>Délka nohavic a jak se nosí</h2>'
          '<p>U Nike se délka nohavic obvykle uvádí v palcích a týká se vnitřního švu. Krátká nohavice kolem tří palců je závodní a odhalí většinu stehna. Průměrná kolem pěti až sedmi palců je běžná na běh a trénink. Delší, osm až devět palců, pokrývá koleno a hodí se na basketbal, posilovnu a volnější nošení.</p>'
          '<ul><li><strong>Krátké:</strong> maximální volnost, ale při sezení a na kole se vyhrnují.</li>'
          '<li><strong>Střední:</strong> univerzální volba pro běh a trénink; nepřekáží a nevypadají příliš sportovně.</li>'
          '<li><strong>Dlouhé:</strong> pohodlné na hřiště a pro ty, kdo nechtějí odhalovat stehna.</li></ul>'
          '<h2>Vnitřní slip, podšívka a 2v1</h2>'
          '<p>Běžecké kraťasy Nike mívají zabudovaný vnitřní slip z lehkého síťovaného materiálu, který nahrazuje spodní prádlo a omezuje tření. Verze bez podšívky, v názvu často označené unlined, jsou určeny pro ty, kdo nosí vlastní spodní vrstvu nebo kompresní šortky. Model 2v1 spojuje volný vnější díl s přiléhavým vnitřním spodním dílem a hodí se na trénink, kde se kraťasy nesmějí vyhrnovat.</p>'
          '<p>Pokud trpíte otěry mezi stehny, zvolte přiléhavou nebo vnitřně podšitou verzi a vyhněte se bavlněným, které se po zmoknutí lepí. Zkontrolujte také švy; ploché švy minimalizují tření při opakovaném pohybu.</p>'
          '<h2>Materiály: Dri-FIT, bavlna, flís</h2>'
          '<p>Vlastní technologie Dri-FIT je označení Nike pro syntetický materiál, který odvádí pot od těla. Najdete ho u běžeckých, tréninkových i fotbalových kraťasů. Volnočasové kraťasy Club bývají z bavlny nebo bavlněného flísu, příjemného na dotek, ale hůř schnoucího. Tkané šortky jsou lehké, rychle schnou a mají hladký povrch; úpletové jsou pružnější, měkčí a hodí se na každodenní nošení.</p>'
          '<p>Pro vodní sporty ani plavání nejsou běžné kraťasy ideální; počítejte s <a href="/plavky/">plavkami</a> a <a href="/panske-plavky/">pánskými plavkami</a>. Pro zimní trénink si pořiďte <a href="/leginy/">legíny</a> nebo dlouhé sportovní kalhoty.</p>'
          '<h2>Pánské, dámské a dětské kraťasy</h2>'
          '<p>Pánské kraťasy Nike mají volnější střih a obvykle delší nohavice. Dámské, často v řadách One, Pro nebo Tempo, bývají přiléhavější s vyšším pasem a vnitřním slipem. Dětské modely jsou označeny Big Kids nebo Big Kid a velikosti se uvádějí v XS až XL podle výšky a věku. Pro dospívající chlapce se hodí pánské modely ve velikosti XS nebo S. Podívejte se i na stránku <a href="/damske-kratasy/">dámské kraťasy</a>, kde najdete další značky.</p>'
          '<h2>Velikosti Nike</h2>'
          '<p>Nike střihá podle amerického systému, takže se velikost značená S obvykle shoduje s evropským S nebo menším. Porovnejte obvod pasu a boků s tabulkou. Elastický pas s tkaničkou umožňuje drobné doladění, ale pokud mezi velikostmi váháte, vyberte přiléhavější u běžeckých a volnější u volnočasových kusů. Tkaný materiál se nenatáhne tolik jako úplet, takže ho kupte spíše volněji.</p>'
          '<h2>Výběr podle sportu</h2>'
          '<ul><li><strong>Běh:</strong> lehký tkaný materiál, vnitřní slip, kapsa na klíč nebo telefon, reflexní prvky. Nohavice střední délky. K nim obuv z kategorie <a href="/bezecka-obuv/">běžecká obuv</a>.</li>'
          '<li><strong>Posilovna a crossfit:</strong> strečový materiál bez vnitřního slipu, aby se nezachytával při dřepech, střední délka.</li>'
          '<li><strong>Fotbal:</strong> lehký polyester s větráním; pro týmové sporty více v kategorii <a href="/fotbal/">fotbal</a>.</li>'
          '<li><strong>Basketbal:</strong> delší nohavice, širší střih, vyztužený pas.</li>'
          '<li><strong>Každodenní nošení:</strong> řady Club a Sportswear, bavlněný úplet a kapsy na zip nebo patent.</li></ul>'
          '<h2>S čím kraťasy nosit</h2>'
          '<p>K běžeckým kraťasům patří funkční tričko, ať už z kategorie <a href="/funkcni-tricka/">funkční trika</a>, nebo ze <a href="/sportovni-tricka/">sportovních triček</a>. Volnočasové kraťasy ladí s mikinou či tričkem. V chladnějším počasí se hodí přiléhavé spodky pod ně, v dešti nepromokavá bunda.</p>'
          '<h2>Značky a alternativy</h2>'
          '<p>Nike se v kategorii setkává s ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('gymbeam', 'GymBeam'), ('champion', 'Champion'), ('umbro', 'Umbro'), ('hummel', 'Hummel')) + '. Adidas a Puma nabízejí podobné spektrum, Under Armour sází na přiléhavé kompresní střihy, GymBeam je zaměřen na posilovnu a fitness a Champion na volný čas. Jordan, sesterská značka Nike, má basketbalový styl.</p>'
          '<h2>Péče o kraťasy</h2>'
          '<ul><li>Perte při nízké teplotě naruby, ať se nepoškodí potisk ani síťovina.</li>'
          '<li>Nepoužívejte aviváž, snižuje schopnost odvádět vlhkost.</li>'
          '<li>Sušte na vzduchu; sušička ničí pružnost vnitřního slipu a gumy v pasu.</li>'
          '<li>Zip kapsy zavřete před praním, aby se nepoškodil materiál.</li></ul>',
    faq=[
        ('Jaká délka nohavic se hodí na běh?', 'Pro běžný běh vyhovují střední délky kolem pěti až sedmi palců. Krátké kolem tří palců jsou určeny závodníkům a pro volnost pohybu, delší se hodí na trénink a basketbal.'),
        ('Co je vnitřní slip v kraťasech?', 'Je to lehká síťovaná podšívka sešitá s vnější vrstvou, která nahrazuje spodní prádlo a omezuje tření. Verze označené unlined ji nemají, takže je lze nosit s vlastním spodním dílem.'),
        ('Jaký je rozdíl mezi řadou Club a Challenger?', 'Club je volnočasová řada z bavlny či bavlněného flísu na každodenní nošení. Challenger je běžecká řada z lehkého syntetického materiálu, který odvádí pot a rychle schne.'),
        ('Pro koho jsou řady Pro a One?', 'Jde o přiléhavé střihy, často se zvýšeným pasem, které slouží jako samostatný kus i jako spodní vrstva. Hodí se pro trénink, jógu, běh a fitness.'),
        ('Jak vybrat velikost dětských kraťasů Nike?', 'Orientujte se podle výšky a věku uvedených v tabulce výrobce, ne podle zvyklosti. Dětské velikosti se označují XS až XL a mívají nastavitelný pas, takže drobný rozdíl lze doladit.'),
        ('Mohu kraťasy Nike používat na posilovnu?', 'Ano. Nejlepší volbou jsou strečové tréninkové modely bez vnitřního slipu, které se nevyhrnují a nepřekážejí při dřepech. Hodí se i řada Flex nebo Form.'),
        ('Jak prát kraťasy s technologií Dri-FIT?', 'Při nízké teplotě naruby, bez aviváže a bez sušičky. Aviváž zanáší vlákna a snižuje schopnost odvádět vlhkost.'),
        ('Čím se liší pánské a dámské kraťasy Nike?', 'Pánské mívají volnější střih a delší nohavice, dámské jsou přiléhavější, s vyšším pasem a často s vnitřním slipem. Střihy se u jednotlivých řad liší, proto se řiďte tabulkou.'),
        ('Jak poznám, že kraťasy nejsou vhodné na plavání?', 'Běžné kraťasy se ve vodě ztěžknou, schnou pomalu a vnitřní slip se nemusí hodit. Pro vodu zvolte plavky; kraťasy Nike jsou určeny hlavně na souš.')
    ])


# ---- extensions (word-count top-ups)
NEW['panska-mikina']['guide'] += (
    '<h2>Barva a vzhled pánské mikiny</h2>'
    '<p>Barva rozhoduje o tom, kolik outfitů mikina zvládne. Černá, tmavě modrá a šedá melír se hodí na všechno a skryjí drobné otěry. Světlé odstíny, například smetanová nebo pískově béžová, působí moderně, ale vyžadují častější praní. Výrazné barvy a potisky se hodí spíš jako doplněk. Černé kusy najdete na stránce <a href="/cerna-mikina/">černá mikina</a>, kde lze porovnat i střihy.</p>'
    '<h2>Mikina jako dárek a pro aktivní využití</h2>'
    '<p>Pokud mikinu vybíráte pro někoho jiného, zvolte neutrální barvu a klasický střih, nejlépe unisex s mírně volným tvarem, který odpustí i drobnou nepřesnost ve velikosti. Pro sportovce pak dává smysl funkční materiál, který se hned po tréninku nepromění v mokrý těžký kus. Fanouškovské mikiny sportovních klubů jsou oblíbeným dárkem, ale potisk vyžaduje opatrnější praní.</p>'
    '<h2>Časté chyby při výběru</h2>'
    '<ul><li><strong>Kupování podle fotky bez tabulky:</strong> sportovní a módní značky střihají odlišně, a proto má smysl porovnat obvod hrudníku.</li>'
    '<li><strong>Příliš silná mikina na vrstvení:</strong> pod bundu patří tenčí úplet, jinak se přehřejete.</li>'
    '<li><strong>Ignorování složení:</strong> čistá bavlna a polyesterový fleece se chovají zcela jinak při potu a dešti.</li>'
    '<li><strong>Zapomenutá délka rukávů:</strong> vyšší postavy by měly sledovat nejen šířku, ale i délku rukávu a trupu.</li></ul>')

NEW['vuch-batoh']['guide'] += (
    '<h2>Kapsy a organizace obsahu</h2>'
    '<p>U městského batohu rozhoduje o pohodlí méně celkový objem než uspořádání kapes. Přední kapsa na zip drží věci, které potřebujete rychle, jako klíče, kartu na dopravu nebo sluchátka. Vnitřní kapsy a přihrádky oddělí drobnosti od dokumentů a zabrání hledání na dně. Boční otevřená kapsa pojme malý deštník nebo láhev. Čím víc přihrádek, tím víc šití a tím vyšší hmotnost prázdného batohu, takže modely s jednoduchou stavbou jsou lehčí a někomu vyhovují víc.</p>'
    '<h2>Batoh pro každodenní dojíždění</h2>'
    '<p>Při dojíždění MHD nebo vlakem si ověřte, jestli se batoh dá sundat a držet v ruce nebo přehodit dopředu. Měkký tvar bez pevné konstrukce se v davu snáz stlačí. Důležité jsou i popruhy: tenké se zařezávají a široké drží váhu rovnoměrněji. Madlo nahoře pomáhá při zavěšení na hák nebo opěradlo. Pro každodenní používání je vhodný materiál, který snese otěr o sedačky i drobný deštík, a zip s dobrým chodem.</p>'
    '<h2>Barvy a styl k oblečení</h2>'
    '<p>Neutrální černý nebo šedý batoh se hodí ke všemu, ale výraznější barva z něj udělá módní doplněk. Béžová a hnědá ladí s přírodními tóny a svetry, vínová s tmavším oblečením, zelená se džínovinou. Potisky v podobě puntíků nebo květin zvolte, pokud batoh chcete používat jako výrazný prvek, a ne jen jako nosič věcí. Klasické jednobarevné modely se lépe kombinují i po delší době.</p>'
    '<h2>Dárek a výběr pro dospívající</h2>'
    '<p>Pro teenagery a studenty je rozhodující vzhled a také kapacita na sešity. Vyplatí se zjistit, jestli bude batoh nosit notebook, a zvolit podle toho velikost komory. Pro mladší děti se hodí spíše specializované školní batohy se zpevněnými zády a reflexními prvky. Batoh jako dárek je bezpečná volba, pokud vyberete neutrální barvu a jednoduchý tvar. Rozdíl mezi dvěma barvami téhož modelu bývá jen v povrchu, proto stačí porovnat obrázky u obchodu.</p>')

NEW['osprey-batoh']['guide'] += (
    '<h2>Jak batoh správně zabalit</h2>'
    '<p>Rozložení váhy rozhoduje o pohodlí víc než samotný model. Nejtěžší věci patří doprostřed zad a blízko těla, lehké a objemné dolů a nahoru, věci potřebné během dne do víka a bočních kapes. Spací pytel vložte do spodní komory, stan připevněte pod víko nebo na boky. Hydratační vak s hadičkou se zasouvá do zadní přihrádky, která je u většiny řad připravena. Při nošení po rovině stačí těžiště ve střední výšce, ve svahu trochu níž.</p>'
    '<h2>Kdy má smysl lehký batoh</h2>'
    '<p>Pokud chodíte rychle a lehce, hledejte batoh s minimem kapes, tenčím materiálem a jednoduchou konstrukcí. Takové modely váží méně, ale nenesou těžkou zátěž. Pro dennodenní výlety do dvaceti litrů jsou lehké batohy dostačující, nad třicet litrů a při těžším nákladu ocení záda vyztuženou konstrukci. Lehká a skladná varianta do tašky pomůže jako rezerva pro nákup suvenýrů nebo mokré oblečení.</p>'
    '<h2>Rodiny s dětmi a mladí turisté</h2>'
    '<p>Značka vyrábí i menší dětské a mládežnické batohy, často s označením Jr nebo Youth. Mají kratší záda a menší objem, aby dítě nepřetěžovaly. Dítě nemá nosit víc, než zvládne bez bolesti zad, a obvyklé pravidlo říká, že zátěž má být malou částí tělesné hmotnosti. Pro školní povinnosti se hodí i <a href="/skolni-batohy/">školní batohy</a>, které mají jiné priority než turistické.</p>'
    '<h2>Zimní a lyžařské využití</h2>'
    '<p>V zimě potřebuje batoh další úchyty a odolnější materiál. Hodí se poutka na lyže, hole nebo cepín a kapsa na lavinové vybavení. Přiléhavá záda bez vzduchové mezery drží stabilněji a netlačí na zápěstí. Rukavice se při nastavování popruhů stále obtížně ovládají, takže zvolte velké a dobře uchopitelné přezky. Pro lyžování zvažte i vaky a tašky z kategorie <a href="/lyzarske-vaky-a-tasky/">lyžařské vaky a tašky</a>.</p>')

NEW['osprey-batoh']['intro'] = NEW['osprey-batoh']['intro'].replace('Značka často nabízí','Značka dlouhodobě nabízí').replace('V další části vysvětlujeme','V dalších částech vysvětlujeme')
NEW['osprey-batoh']['intro'] = NEW['osprey-batoh']['intro'].replace('Související kategorie:','K porovnání nabídek se hodí také související kategorie, a to')

NEW['nike-kratasy']['guide'] += (
    '<h2>Tkaný, úpletový nebo flísový: co zvolit</h2>'
    '<p>Tkané kraťasy mají hladký povrch, nesrážejí se a rychle schnou. Hodí se na běh, fotbal a letní trénink. Úpletové jsou měkčí a pružnější, ale pomaleji schnou, takže se víc hodí do posilovny a na odpočinek. Flísové z bavlněné směsi jsou nejteplejší a nejpohodlnější na doma, ale na horké dny jsou příliš silné. Podle sezony a účelu se vyplatí mít dva různé páry, jeden na pohyb a druhý na každodenní nošení.</p>'
    '<h2>Kapsy a praktické detaily</h2>'
    '<p>U běžeckých modelů hledejte zapínací kapsu na klíč nebo menší telefon, aby se nepohupovala. U tréninkových kapsy na zip nebo s patentem zamezí vypadávání drobností při dřepech. Reflexní prvky pomáhají večerním běžcům. Stahovací šňůrka v pase doladí velikost a gumička s vnitřním lemem zabrání sjíždění. Pro každodenní nošení se hodí boční kapsy bez zipu, protože se do nich rychle sahá.</p>'
    '<h2>Kraťasy pro týmové sporty a děti</h2>'
    '<p>Fotbalové a týmové kraťasy bývají součástí klubových souprav, a proto se nabízejí v barvách známých týmů. Pro děti volte pružný pas a nenápadné švy, aby nedřely. Rostoucí dítě potřebuje větší velikost každou sezonu, takže se vyplatí o číslo větší model s nastavitelným pasem. Při výběru je užitečné sledovat zdroje velikostí, protože americké označení Big Kids neodpovídá přesně evropským věkovým údajům.</p>'
    '<h2>Kdy kraťasy nestačí</h2>'
    '<p>Při teplotách kolem deseti stupňů a níže zvažte dlouhé legíny nebo sportovní kalhoty z kategorií <a href="/leginy/">legíny</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>. Na kolo patří cyklistické kraťasy s vložkou, které najdete v kategorii <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a>. Běžné sportovní kraťasy na delší jízdu nestačí, protože nemají vložku a švy otírají.</p>')

# ---- second top-up
NEW['vuch-batoh']['guide'] += (
    '<h2>Jak batoh vyzkoušet před koupí</h2>'
    '<p>Při osobním nákupu naplňte batoh obvyklým obsahem a projděte se s ním. Popruhy mají sedět bez zarývání, dno nemá viset nízko pod pasem a zip se musí zavírat bez tlaku. Při online nákupu porovnejte uvedené rozměry s věcmi, které nosíte denně, a ověřte, zda lze popruhy zkrátit. Rozhodnutí usnadní také možnost vrácení zboží do několika dní od převzetí, kterou obchody většinou nabízejí.</p>'
    '<p>Pokud nosíte věci, které mají pevný tvar, například obědový box nebo tablet, zvolte batoh s tvarově stálejší zadní částí. Měkké modely se hodí pro lehké a pružné náklady.</p>')

NEW['osprey-batoh']['guide'] += (
    '<h2>Záruka, opravy a výdrž</h2>'
    '<p>Turistický batoh je investice na mnoho sezon, a proto má smysl všímat si, jak se dá opravit. Oprava popruhu, přezky nebo zipu bývá často jednodušší než výměna celého kusu, a mnozí výrobci nabízejí náhradní díly. Před koupí zkontrolujte, že máte k dispozici všechny části, které k modelu patří, například ochranný obal proti dešti nebo odnímatelné víko. Starší kolekce v nabídce obchodů bývají plnohodnotné, jen mají jiné barvy nebo drobně odlišný systém seřízení.</p>'
    '<h2>Vybavení v batohu: co nezapomenout</h2>'
    '<ul><li><strong>Nepromokavý obal:</strong> chrání obsah při dešti, protože síťovina a zipy vodu propouštějí.</li>'
    '<li><strong>Hydratace:</strong> láhev v boční kapse nebo vak s hadičkou, aby se pilo za chůze.</li>'
    '<li><strong>Lékárnička a čelovka:</strong> malé, ale nezbytné pro delší túry.</li>'
    '<li><strong>Vrstva navíc:</strong> lehká bunda nebo fleece, i když je ráno slunečno.</li></ul>')

NEW['nike-kratasy']['guide'] += (
    '<h2>Jak poznat správně padnoucí kraťasy</h2>'
    '<p>Dobře padnoucí kraťasy nezačnou při běhu sjíždět ani se nezařezávají do pasu. Nohavice nemají tlačit do stehen a vnitřní slip se nemá vyhrnovat. Zkuste se předklonit, dřepnout a zvednout koleno; pokud se materiál napíná nebo se vyhrnuje, zvolte jinou velikost nebo střih. Před objednávkou si porovnejte obvod pasu a boků s tabulkou a zjistěte, zda je pas elastický a zda má šňůrku.</p>'
    '<p>Při opakovaném nošení vyhodnoťte i švy, zda nedrhnou, a gumu, zda nesjíždí. Kvalitnější kraťasy zachovají tvar i po desítkách praní.</p>'
    '<h2>Sezona a porovnání obchodů</h2>'
    '<p>Kraťasy se nejvíc prodávají na jaře a v létě, a proto se starší kolekce často vyprodávají na podzim a v zimě. Neznamená to horší kvalitu, jen posun modelových řad. Při porovnání mezi obchody sledujte barvu, velikost a přesný název řady, protože stejný název může mít několik materiálových variant.</p>')
