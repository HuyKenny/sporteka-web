"""sporteka.cz — wave 12e (4. 11. 2026): long texts for kopacky, sportovni-vyziva, trekova-obuv, pantofle-a-zabky. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ kopacky
NEW['kopacky'] = dict(long=True,
    title='Kopačky: lisovky, turfy, halovky pro každý povrch',
    desc='Kopačky na trávu, umělku i do haly: lisovky, turfy, multinopy a halovky. Jak vybrat typ, velikost a materiál. Porovnejte nabídky českých obchodů.',
    intro='<p><strong>Kopačky</strong> jsou specializovaná obuv a o jejich vhodnosti rozhoduje hlavně povrch, na kterém se hraje. Stejný pár, který drží na přírodní trávě, se na umělce zasekává a na parketách kloužou i ty nejlepší. Proto se při nákupu vyplatí začít otázkou, kde budete hrát nejčastěji, a teprve potom řešit střih, materiál svršku nebo značku.</p>'
          '<p>Na Sportece najdete kopačky pánské, dámské i dětské od většiny značek na českém trhu a vedle nich <a href="/salova-obuv/">sálovou a halovou obuv</a> pro futsal. Pro trénink mimo trávník poslouží <a href="/treninkova-obuv/">fitness a tréninková obuv</a>, k ní patří <a href="/fotbalove-mice/">fotbalové míče</a> a <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>. Níže je průvodce, který vás provede povrchy, střihy, materiály i péčí, aby pár vydržel déle než jednu sezónu.</p>',
    guide='<h2>Jak vybrat kopačky podle povrchu</h2>'
          '<p>Kopačky se od sebe liší především spodní částí. Výrobce označuje podrážku zkratkou, která říká, pro jaký povrch je určená. Označení se u různých značek drobně liší, ale základní logika je společná. Pokud si zkratku nejste jistí, hledejte ji v popisu produktu nebo na štítku v jazyku boty.</p>'
          + T(['Zkratka', 'Povrch', 'Co je na podrážce', 'Poznámka'], [
              ['FG', 'přirozená tráva se zdravým drnem', 'pevné kolíky, často kónické nebo čepelkové', 'nejběžnější typ, kopačky pro většinu zápasů na trávě'],
              ['SG', 'rozbředlá nebo hluboká tráva', 'méně kolíků, delších, někdy vyměnitelných', 'používají hlavně hráči na rozmoklých hřištích'],
              ['AG', 'umělá tráva nové generace', 'více kratších kolíků rozložených po podrážce', 'rozděluje zatížení a šetří klouby'],
              ['MG', 'různé povrchy včetně smíšených', 'kompromis mezi FG a AG', 'univerzální volba pro začátečníky a rekreační hráče'],
              ['TF', 'starší umělka, škvára, tvrdý povrch', 'drobné gumové nopy', 'lehké a pohodlné, vhodné pro trénink'],
              ['IC / IN', 'hala, parkety, sportovní podlaha', 'hladká nebo drobně rýhovaná guma', 'bez kolíků, bezpečné pro podlahu']]) +
          '<p>Praktické pravidlo zní: jedny kopačky nikdy nepokryjí všechny povrchy stejně dobře. Hrajete-li pravidelně na dvou různých hřištích, vyplatí se mít dva páry a střídat je. Střídání prodlužuje životnost obou, protože se každý pár po zápase stihne vysušit.</p>'
          '<h3>Co se stane, když zvolíte špatnou podrážku</h3>'
          '<p>Dlouhé kolíky na tvrdé umělé trávě se zakusují do povrchu a při otočení se noha nemusí uvolnit. Naopak malé nopy na rozmoklé trávě nemají dostatek záběru, hráč uklouzává a ztrácí jistotu při zrychlení. V hale mohou kolíky poškodit podlahu a v mnoha halách jsou kvůli tomu zakázané. Právě proto jsou halovky samostatná kategorie, kterou najdete v sekci <a href="/salova-obuv/">sálová a halová obuv</a>.</p>'
          '<h2>Svršek: kůže, syntetika, pletený materiál</h2>'
          '<p>Materiál svršku ovlivňuje cit pro míč, hmotnost i péči. Přírodní kůže se po rozehrání přizpůsobí noze a dobře sedí, ale po namočení se víc natahuje. Syntetické materiály jsou lehčí, méně nasákavé a obvykle stabilnější z hlediska tvaru. Pletený svršek tvoří pohodlný ponožkový střih, který nohu pevně obepíná od prvního zápasu.</p>'
          '<ul><li><strong>Kůže:</strong> příjemná a tvárná, vyžaduje impregnaci a pravidelné krémování.</li>'
          '<li><strong>Syntetika:</strong> méně nasákne, schne rychleji a drží tvar i po deštivých zápasech.</li>'
          '<li><strong>Pletený svršek:</strong> pružný a elastický, bez hrubých švů, často s límcem kolem kotníku.</li>'
          '<li><strong>Textilní podšívka:</strong> odvádí pot a zabraňuje otěrům, důležitá hlavně u dětských modelů.</li></ul>'
          '<h2>Střih, šířka a velikost</h2>'
          '<p>Kopačky mají sedět těsněji než běžná obuv, ale nesmí tlačit. Prsty se mají dotýkat špičky jen lehce, pata nesmí vyskakovat a v nártu nemá být žádný tlak. Příliš volná bota způsobuje otlaky a znejistí hru, příliš těsná vede k bolesti a poškození nehtů. Chodidlo měřte odpoledne, kdy je lehce oteklé, a zkoušejte v ponožkách, v jakých hrajete. Nejlepší jsou <a href="/sportovni-ponozky/">sportovní ponožky</a>, které nesklouzávají a neodírají.</p>'
          '<p>Značky mají různé střihy. Některé jsou ve špičce užší a vhodné pro užší nohu, jiné nabízejí širší nárt a pohodlnější zakončení. Jestliže vám pár nesedí, je rozumnější zkusit jiný model než kompenzovat nepohodlí vložkami nebo silnými ponožkami. Případné drobné úpravy obstarají doplňky z kategorie <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>'
          '<h3>Děti a dorost</h3>'
          '<p>U dětí se obvykle řeší dvě věci: rychle rostoucí noha a bezpečnost. Rozumná rezerva ve špičce je v pořádku, ale kopačky o dvě čísla větší způsobují klopýtání a ztrátu citu pro míč. Dětské modely mají mít nižší kolíky a pevnější podpatěnku, aby noha stabilně seděla. Pro děti hrající převážně na školním hřišti nebo na umělce je rozumný turf nebo multinop. Velikost přeměřujte alespoň jednou za sezónu, protože noha může narůst během několika měsíců.</p>'
          '<h2>Pozice na hřišti a styl hry</h2>'
          '<p>Rozdíly mezi modely se vyplatí zohlednit podle toho, co po obuvi chcete. Útočníci a křídla ocení nižší hmotnost a těsné padnutí, záložníci cit pro míč a konstrukci přední části s dobrým kontaktem, obránci pevnější materiál a oporu ve středu boty. Specifický případ tvoří brankáři, kteří kopačky nepotřebují tolik jako ostatní, ale zato potřebují kvalitní <a href="/brankarske-rukavice/">brankářské rukavice</a>.</p>'
          + T(['Hráč', 'Na co se zaměřit', 'Typický povrch'], [
              ['Útočník', 'nízká hmotnost, těsný střih, dobrý záběr při startu', 'tráva, umělka'],
              ['Záložník', 'cit pro míč, pohodlí během celého zápasu', 'tráva, umělka'],
              ['Obránce', 'pevnější materiál, opora paty, odolnost', 'tráva, tvrdší hřiště'],
              ['Futsalista', 'hladká podrážka, dobrá přilnavost na podlaze', 'hala, sportovní podlaha'],
              ['Rekreační hráč', 'pohodlí, univerzální podrážka MG nebo TF', 'různé povrchy']]) +
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece jsou nejvíc zastoupené značky ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('joma', 'Joma'), ('nike', 'Nike'), ('mizuno', 'Mizuno'), ('lotto', 'Lotto'), ('kipsta', 'Kipsta'), ('new-balance', 'New Balance'), ('munich', 'Munich'), ('umbro', 'Umbro')) + '. Velké světové značky mají celé řady od základních modelů pro začátečníky po špičkové pro profesionály. Joma, Lotto a Kipsta jsou oblíbené u amatérských klubů a mládeže, Mizuno je oblíbené u hráčů, kteří hledají lehčí obuv s citem pro míč, a Munich se zaměřuje na halovou a futsalovou obuv. Značka sama o sobě nic nezaručuje, důležitější je padnutí a správný povrch.</p>'
          '<h2>Další výbava k fotbalu</h2>'
          '<p>Kopačky tvoří jen část výbavy. Při zápase i tréninku se hodí <a href="/fotbalove-chranice-a-stulpny/">chrániče holení a štulpny</a>, které chrání před údery a drží chrániče na místě. Pro trénink doma nebo s kamarády se hodí <a href="/fotbalove-mice/">fotbalové míče</a> v různých velikostech. Širší sortiment najdete v kategorii <a href="/fotbal/">fotbal</a> a pro hru s oválným míčem v sekci <a href="/ragby-a-americky-fotbal/">ragby a americký fotbal</a>.</p>'
          '<p>Na zahřátí nebo regeneraci stačí lehká <a href="/sportovni-obuv/">sportovní obuv</a> nebo pohodlné <a href="/tenisky/">tenisky</a>. Nikdy nechoďte v kopačkách po tvrdém betonu nebo asfaltu, kolíky se rychle obrousí a bota ztratí záběr.</p>'
          '<h2>Péče o kopačky krok za krokem</h2>'
          '<ol><li>Po zápase sejměte hrubé bláto kartáčem, ještě než zaschne.</li>'
          '<li>Svršek otřete vlhkým hadrem, kolíky vyčistěte například starším kartáčkem.</li>'
          '<li>Vyndejte vložky a povolte tkaničky, aby vzduch mohl proudit dovnitř.</li>'
          '<li>Sušte při pokojové teplotě, nejlépe v průvanu, nikoli na topení.</li>'
          '<li>Kůži občas ošetřete krémem, syntetiku stačí otřít a vyvětrat.</li>'
          '<li>Do tašky ukládejte suché, pokud možno v oddělené kapse.</li></ol>'
          '<p>Vlhké kopačky zavřené v tašce začnou zapáchat a rychleji se rozpadají. Pokud boty promoknou, vycpěte je papírem a papír po pár hodinách vyměňte. Podrážku kontrolujte před každou sezónou, zda nejsou kolíky rozlámané nebo zalomené.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Špatný povrch:</strong> lisovky na umělou trávu nebo turfy na rozmoklou trávu.</li>'
          '<li><strong>Nákup podle hvězdy:</strong> model, který nosí oblíbený hráč, nemusí sedět vašemu chodidlu.</li>'
          '<li><strong>Velikost na vyrůstání:</strong> příliš velká bota u dítěte znamená klopýtání a horší cit.</li>'
          '<li><strong>Nezkoušení se správnými ponožkami:</strong> tenká ponožka zmenší dojem těsnosti, tlustá ho naopak přeplní.</li>'
          '<li><strong>Špatné sušení:</strong> topení deformuje kůži a poškozuje lepení podrážky.</li></ul>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>Začněte filtrem povrchu a velikosti, potom si zúžte výběr podle značky a pohlaví. U vybraného páru porovnejte nabídky obchodů vedle sebe, uvidíte rozdíl ve dostupnosti velikostí i v dodací době. Starší modely předchozích sezón mají obvykle stejné vlastnosti jako novinky a vyplatí se je zvážit, pokud vám nejde o poslední barevnou kombinaci. Před nákupem vždy zkontrolujte, zda je v popisu uvedený povrch a zda je velikost opravdu skladem.</p>',
    faq=[('Jaké kopačky koupit na umělou trávu?', 'Podle typu umělky. Na novější povrchy s delším vláknem jsou určené kopačky AG s více kratšími kolíky, na starší nebo tvrdší povrchy turfy TF s drobnými nopy. Lisovky FG se zde nedoporučují.'),
         ('Jaký je rozdíl mezi lisovkami a turfy?', 'Lisovky mají delší kolíky pro záběr v přírodní trávě. Turfy mají malé gumové nopy a hodí se na umělý povrch, škváru nebo tvrdé hřiště, kde dlouhé kolíky nedávají smysl.'),
         ('Mohu v kopačkách hrát na hale?', 'Ne. Do haly patří halovky s hladkou podrážkou. Kolíky nebo nopy poškozují podlahu, často jsou v halách zakázané a bota na nich klouže.'),
         ('Jak poznám správnou velikost kopaček?', 'Chodidlo změřte odpoledne a zkoušejte v ponožkách, ve kterých hrajete. Prsty se mají jen lehce dotýkat špičky, pata nesmí vyskakovat a nárt nesmí tlačit.'),
         ('Jsou lepší kožené, nebo syntetické kopačky?', 'Záleží na preferencích. Kůže se přizpůsobí noze a je pohodlná, ale vyžaduje péči. Syntetika je lehčí, méně nasákne a rychleji schne, proto se hodí do deště.'),
         ('Jaké kopačky pro dítě na první trénink?', 'Lehké, pohodlné a s nižšími kolíky nebo nopy podle povrchu, kde se bude trénovat. Pro školní hřiště a umělku bývá rozumná volba turf nebo multinop. Velikost přeměřujte každou sezónu.'),
         ('Jak často je potřeba kopačky měnit?', 'Záleží na četnosti hraní a povrchu. Vyměňte je, když se kolíky sjedou, podrážka se odlepuje nebo svršek přestane držet nohu. Střídání dvou párů výrazně prodlužuje životnost.'),
         ('Jak kopačky vyčistit a vysušit?', 'Hrubé bláto sejměte kartáčem, svršek otřete vlhkým hadrem, vyjměte vložky a sušte při pokojové teplotě. Nesušte je na topení, kůže se deformuje a lepidlo povoluje.'),
         ('Proč mi kopačky tlačí v prstech?', 'Nejčastěji jsou malé nebo mají úzký střih špičky. Zkuste větší velikost nebo jiný model s širší přední částí. Ke zlepšení nepomůže jen silná ponožka, boty vyměňte.'),
         ('Hodí se kopačky i na jiné sporty?', 'Pro ragby, americký fotbal nebo baseball existují specializované boty s vlastním uspořádáním kolíků. Fotbalové kopačky jsou laděné na zrychlení a cit pro míč, proto je nepoužívejte jinde než na fotbal.')],
)

# ------------------------------------------------------------------ sportovni-vyziva
NEW['sportovni-vyziva'] = dict(long=True,
    title='Sportovní výživa: proteiny, kreatin, vitamíny',
    desc='Sportovní výživa a doplňky stravy: proteiny, kreatin, BCAA, vitamíny, gely a iontové nápoje. Jak vybrat a porovnat nabídky českých obchodů.',
    intro='<p><strong>Sportovní výživa</strong> je široká skupina potravin a doplňků, které mají pomáhat s pohodlným doplněním energie, bílkovin a minerálů kolem tréninku. Žádný prášek ani tyčinka nenahradí pestrou stravu a dostatek spánku, ale ve správné chvíli ušetří čas a práci. Proto je rozumné nejdřív vědět, co od výživy chcete, a teprve pak vybírat produkt.</p>'
          '<p>Na Sportece najdete <a href="/proteiny/">proteiny</a>, <a href="/kreatin/">kreatin</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny</a>, <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>, <a href="/iontove-napoje/">iontové nápoje</a> nebo <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a> z českých e-shopů vedle sebe. Průvodce níže vysvětluje, kdy se která skupina hodí, jak číst složení, jak výživu skladovat a na co si dát při nákupu opravdu pozor.</p>',
    guide='<h2>Co sportovní výživa dělá a co ne</h2>'
          '<p>Základem každé sportovní přípravy je běžná strava, tedy dost energie, bílkovin, sacharidů, tuků a tekutin. Doplňky přicházejí na řadu, když něco z toho jen těžko pokryjete jídlem, například proto, že je málo času, jíte na cestách nebo potřebujete rychle doplnit energii při vytrvalostním výkonu. Nejde o zázračný přípravek. Kdo má jídelníček v nepořádku, nenapraví to žádným kelímkem prášku.</p>'
          '<p>Před nákupem si zodpovězte tři otázky: jaký sport děláte a jak často, co vám v jídelníčku konkrétně chybí a kolik jste ochotni řešit. Pokud trénujete dvakrát týdně rekreačně, většinou si vystačíte s dobrou stravou a občasnou tyčinkou. Při těžších trénincích, soutěžích nebo vegetariánské stravě už se doplňky vyplatí zvážit.</p>'
          '<h2>Přehled skupin a k čemu slouží</h2>'
          + T(['Skupina', 'K čemu se používá', 'Kdy dává smysl'], [
              ['<a href="/proteiny/">Proteiny</a>', 'pohodlný zdroj bílkovin v nápoji nebo jídle', 'když je těžké pokrýt bílkoviny jídlem'],
              ['<a href="/kreatin/">Kreatin</a>', 'doplněk pro silové a rychlostní sporty', 'při pravidelném posilování'],
              ['<a href="/aminokyseliny-bcaa/">Aminokyseliny a BCAA</a>', 'stavební látky bílkovin ve formě prášku nebo kapslí', 'nejčastěji při tréninku nalačno nebo při diétě'],
              ['<a href="/gainery/">Gainery</a>', 'kombinace bílkovin a sacharidů pro příjem energie', 'pro hubené a velmi aktivní lidi'],
              ['<a href="/predtreninkove-boostery/">Předtréninkové boostery</a>', 'směsi s kofeinem a dalšími látkami před tréninkem', 'když potřebujete povzbudit před tréninkem'],
              ['<a href="/spalovace-tuku/">Spalovače tuků</a>', 'přípravky prodávané jako spalovače tuků; jejich účinek není spolehlivě prokázán', 'jen jako doplněk dobrého režimu, ne náhrada']]) +
          '<h2>Proteiny: typy a výběr</h2>'
          '<p>Proteinový prášek se vyrábí z mléčných nebo rostlinných zdrojů. Syrovátkový protein se rychle rozpouští a je nejrozšířenější, kaseinový se tráví pomaleji a hodí se spíš na večer, rostlinné směsi z hrachu, rýže nebo sóji jsou volbou pro vegany a lidi s intolerancí laktózy. Koncentrát bývá obsahem bílkovin nižší, izolát je čistší a méně obsahuje laktózy. Na etiketě sledujte obsah bílkovin v dávce, aminokyselinový profil a seznam sladidel a aromat.</p>'
          '<p>Hledáte-li něco k zakousnutí, podívejte se na <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>. Ty jsou praktické do tašky, ale od čokoládové tyčinky se někdy liší jen v obsahu bílkovin, takže stojí za to číst tabulku nutričních hodnot.</p>'
          '<h2>Kreatin a aminokyseliny</h2>'
          '<p>Kreatin je jedním z nejlépe prozkoumaných doplňků pro silové sporty. Nejčastěji se používá kreatin monohydrát, který se dávkuje pravidelně a nemusí se kombinovat s ničím dalším. Drobné rozdíly ve formách dělají hlavně marketing. Pozor na pitný režim, při užívání kreatinu je rozumné pít dostatek tekutin. U zdravotních potíží, zejména ledvin, se před užíváním poraďte s lékařem.</p>'
          '<p>Aminokyseliny a BCAA nabízejí stavební látky ve formě prášku, tablet nebo nápoje. Pokud denně jíte dostatek kvalitních bílkovin, přidané aminokyseliny většinou nepotřebujete. Jejich smysl je spíše v pohodlí, například při dlouhém tréninku nebo při dietě.</p>'
          '<h2>Energie při vytrvalostním sportu</h2>'
          '<p>Při běhu, cyklistice nebo turistice trvající déle než hodinu už tělo potřebuje doplňovat sacharidy. Pomáhají <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a>, které se rychle tráví a vejdou se do kapsy. Gely se zapíjejí vodou, protože koncentrovaný cukr jinak dráždí žaludek. Na delších trasách je rozumné vyzkoušet vše dopředu na tréninku, nikdy ne poprvé na závodě.</p>'
          '<p>K tomu patří <a href="/iontove-napoje/">iontové nápoje a hydratace</a>. Při větším pocení se ztrácí sodík a další minerály a čistá voda je už nedoplní. Iontový nápoj se dá namíchat v láhvi, kterou vyberete mezi <a href="/lahve-a-termosky/">lahvemi a termoskami</a>. Pro dlouhé túry může být zajímavá i <a href="/outdoorova-strava/">outdoorová a lyofilizovaná strava</a>, která je lehká a nezabere místo v <a href="/batohy/">batohu</a>.</p>'
          '<h2>Vitamíny, minerály a klouby</h2>'
          '<p>Běžný jídelníček obvykle pokryje většinu potřeb a vitamíny nejsou povinnou součástí sportu. Smysl mohou mít při omezené stravě, v zimě nebo při zvýšené zátěži. <a href="/vitaminy-a-mineraly/">Vitamíny, minerály a omega-3</a> se prodávají jako jednotlivé látky i komplexy. Nepřekračujte doporučené dávky uvedené na obalu, vyšší příjem neznamená lepší výsledek.</p>'
          '<p>Pro namáhané klouby existují přípravky v kategorii <a href="/kolagen-a-klouby/">kolagen a kloubní výživa</a>. Obsahují kolagen, glukosamin nebo kyselinu hyaluronovou. Jejich účinnost u kloubů není jednoznačně prokázána, účinky se u různých lidí liší a nenahradí rozcvičení, správnou techniku ani odpočinek. Další přípravky, které se nevejdou do jiných skupin, najdete v sekci <a href="/ostatni-doplnky-stravy/">další doplňky stravy</a>.</p>'
          '<h2>Jak číst etiketu</h2>'
          '<ul><li><strong>Dávka a gramáž:</strong> porovnávejte cenu za porci bílkovin nebo účinné látky, ne za balení.</li>'
          '<li><strong>Složení:</strong> čím kratší seznam, tím snazší je poznat, co kupujete.</li>'
          '<li><strong>Alergeny:</strong> mléko, sója, lepek nebo ořechy musí být na obalu vyznačeny.</li>'
          '<li><strong>Sladidla a barviva:</strong> citlivý žaludek reaguje na některá z nich nepříjemně.</li>'
          '<li><strong>Datum minimální trvanlivosti:</strong> u prášků je dlouhé, u gelů a nápojů kontrolujte.</li>'
          '<li><strong>Původ a certifikace:</strong> pro soutěžní sportovce je užitečné ověřit, zda je výrobek testován na zakázané látky.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(('gymbeam', 'GymBeam'), ('amix', 'Amix'), ('nutrend', 'Nutrend'), ('extrifit', 'Extrifit'), ('ostrovit', 'OstroVit'), ('biotech-usa', 'BioTech USA'), ('myprotein', 'MyProtein'), ('greenfood-nutrition', 'GreenFood Nutrition'), ('weider', 'Weider')) + '. Některé jsou silné v prášcích a tyčinkách, jiné ve vitamínech nebo přírodních doplňcích. Hodnoťte složení a obsah, ne jen vzhled obalu nebo reklamu.</p>'
          '<h2>Pro koho které doplňky a jak začít</h2>'
          + T(['Typ sportovce', 'Co obvykle dává smysl', 'Co raději vynechat'], [
              ['Začátečník v posilovně', 'dobrý jídelníček, případně protein', 'kombinace mnoha doplňků najednou'],
              ['Běžec a cyklista', 'gely, tyčinky, iontový nápoj', 'velké množství bílkovin navíc'],
              ['Turista na delších trasách', 'tyčinky, outdoorová strava, hydratace', 'nezkoušené novinky na trase'],
              ['Vegan', 'rostlinný protein, vitamíny podle jídelníčku', 'výrobky s mléčným základem'],
              ['Sportovec v soutěži', 'ověřené produkty od důvěryhodných výrobců', 'nejasné směsi bez uvedeného složení']]) +
          '<p>Začínejte vždy jedním produktem a sledujte, jak vám vyhovuje. Teprve potom přidávejte další. Více kusů najednou zkomplikuje zjištění, co skutečně pomáhá a co případně dráždí.</p>'
          '<h2>Skladování a bezpečné používání</h2>'
          '<p>Prášky skladujte v suchu a chladu, otevřené balení pevně zavřete. Vlhkost způsobuje hrudky, proto používejte suchou odměrku a nenechávejte ji uvnitř. Vitamíny a kapsle chraňte před světlem a teplem. Děti, těhotné a kojící ženy, lidé s chronickým onemocněním a lidé užívající léky by měli užívání doplňků konzultovat s lékařem. Doplněk stravy není lék a nemá se používat jako náhrada pestré stravy.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Nákup podle reklamy:</strong> sliby na obalu neříkají nic o složení.</li>'
          '<li><strong>Příliš mnoho doplňků:</strong> většina lidí potřebuje jen jeden nebo dva.</li>'
          '<li><strong>Ignorování alergií:</strong> některé směsi obsahují mléko, sóju nebo lepek.</li>'
          '<li><strong>Porovnávání jen podle hmotnosti balení:</strong> důležité je množství účinné látky v dávce.</li>'
          '<li><strong>Zkoušení nového před soutěží:</strong> žaludek reaguje různě, vyzkoušejte předem.</li></ul>'
          '<p>Na Sportece snadno porovnáte nabídky několika obchodů najednou. Sledujte cenu za dávku, nikoli za balení, a před nákupem se podívejte na datum trvanlivosti i na složení v popisu produktu.</p>',
    faq=[('Je nutné užívat sportovní výživu, když sportuji rekreačně?', 'Není. Pestrá strava, dostatek tekutin a spánek jsou základ. Doplňky jsou pohodlí, ne povinnost, a rekreační sportovec si často vystačí bez nich.'),
         ('Jaký protein je nejvhodnější pro začátečníka?', 'Většinou syrovátkový koncentrát nebo izolát, který se dobře rozpouští. Při intoleranci laktózy nebo veganské stravě zvolte rostlinnou směs z hrachu, rýže nebo sóji.'),
         ('Jak se užívá kreatin?', 'Obvykle se užívá pravidelně v doporučené dávce uvedené na obalu, nejčastěji monohydrát. Pijte dostatek tekutin a při zdravotních potížích, zejména s ledvinami, se poraďte s lékařem.'),
         ('Potřebuji BCAA, když jím dost bílkovin?', 'Pravděpodobně ne. Plnohodnotná strava obsahuje aminokyseliny včetně BCAA. Přidané se hodí spíše pro pohodlí při dlouhém tréninku nebo dietě.'),
         ('Kdy použít energetický gel?', 'Při výkonu delším než zhruba hodinu, kdy tělo potřebuje doplnit sacharidy. Zapíjejte vodou a vyzkoušejte jej nejdříve na tréninku, ne na závodě.'),
         ('Stačí na pití voda, nebo potřebuji iontový nápoj?', 'Při krátkém tréninku stačí voda. Při dlouhém výkonu nebo ve vedru, kdy se hodně potíte, pomůže iontový nápoj, který doplní i minerály.'),
         ('Jsou vitamíny pro sportovce nutné?', 'Obvykle ne, pokud jíte pestře. Mohou se hodit při omezené stravě, v zimě nebo při zvýšené zátěži. Nepřekračujte dávku na obalu.'),
         ('Jak poznám kvalitní doplněk?', 'Podle čitelného složení, uvedeného obsahu účinné látky v dávce a důvěryhodného výrobce. Vyhněte se směsím, které neuvádějí množství jednotlivých složek.'),
         ('Mohou děti a mladiství užívat sportovní výživu?', 'Většinou ji nepotřebují a pestrá strava stačí. Pokud o doplňku uvažujete, poraďte se s lékařem nebo dětským lékařem. Některé směsi s kofeinem nejsou pro děti vhodné.'),
         ('Jak dlouho vydrží otevřený prášek?', 'Podle výrobce, obvykle do data minimální trvanlivosti na obalu při správném skladování. Držte jej v suchu a chladu a po použití pevně uzavřete.')],
)

# ------------------------------------------------------------------ trekova-obuv
NEW['trekova-obuv'] = dict(long=True,
    title='Trekové boty: nízké, vysoké, s membránou | Sporteka',
    desc='Trekové boty pánské, dámské i dětské: nízké a vysoké, s membránou i bez. Jak vybrat podle trasy, batohu a sezóny. Porovnejte nabídky obchodů.',
    intro='<p><strong>Trekové boty</strong> jsou obuv pro chůzi v přírodě, kde potřebujete stabilitu, přilnavost a ochranu chodidla. Od běžných tenisek se liší pevnější podrážkou, zesílenou špičkou a patou a většinou i konstrukcí, která chrání před kameny, vodou a nerovným terénem. Výběr ale není otázka značky: rozhoduje trasa, zátěž v batohu a roční doba.</p>'
          '<p>Na Sportece najdete <a href="/nizke-trekove-boty/">nízké trekové boty</a> pro lehčí výlety a <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> pro náročnější terén. Vedle toho se hodí podívat se na <a href="/outdoor/">outdoor a turistiku</a>, na <a href="/trailove-boty/">trailové běžecké boty</a> pro rychlé túry nebo na <a href="/sandaly/">sportovní sandály</a> pro léto. Průvodce vysvětluje rozdíly mezi typy, materiály i péči o boty.</p>',
    guide='<h2>Nízké, polovysoké, nebo vysoké boty</h2>'
          '<p>Výška svršku určuje, jak moc bota drží kotník a jak ochrání před kamením, vodou a trávou. Vyšší bota dává větší pocit jistoty, ale je těžší a v horku méně příjemná. Nižší bota je lehčí a ohebnější, ale nechrání před zvrtnutím a vniknutím drobných kamínků.</p>'
          + T(['Typ', 'Výhody', 'Nevýhody', 'Hodí se na'], [
              ['<a href="/nizke-trekove-boty/">Nízké</a>', 'lehké, ohebné, rychle schnou', 'menší opora kotníku, méně ochrany', 'kratší výlety, lehký batoh, suché cesty'],
              ['Polovysoké', 'kompromis opory a hmotnosti', 'těžší než nízké', 'celodenní túry, střední zátěž'],
              ['<a href="/vysoke-trekove-boty/">Vysoké</a>', 'opora kotníku, ochrana před kamením a vodou', 'těžší, v horku teplejší', 'hory, vícedenní treky, těžší batoh']]) +
          '<p>Často se opakuje mýtus, že vysoká obuv zabrání zvrtnutí. Pomáhá, ale pevné držení paty a silná podrážka jsou stejně důležité. Zkušený turista s dobrou technikou a lehkým batohem zvládne i náročnější terén v nízké botě. Začátečník s těžším batohem se ve vysoké botě cítí jistěji.</p>'
          '<h2>Podrážka, tuhost a hmotnost</h2>'
          '<p>Podrážka určuje, jak bota přilne na kamenech a mokré trávě a jak chrání chodidlo před ostrými předměty. Hrubý vzorek s hlubšími drážkami se lépe drží v blátě a na sněhu, mělčí vzorek je lepší na chodníku a suché skále. Tuhost se vybírá podle zátěže: tuhá bota pomáhá při dlouhém nošení těžkého batohu a prudkých úsecích, ohebnější je pohodlnější při obvyklé chůzi. Lehčí obuv méně unavuje nohy, ale při těžké zátěži poskytuje menší oporu.</p>'
          '<h3>Svršek a membrána</h3>'
          '<ul><li><strong>Kůže:</strong> odolná a trvanlivá, vyžaduje péči a delší rozchození.</li>'
          '<li><strong>Textil a syntetika:</strong> lehčí, rychleji schnou a nevyžadují tolik péče.</li>'
          '<li><strong>Membrána:</strong> brání vniknutí vody, ale zhoršuje větrání při horku.</li>'
          '<li><strong>Bez membrány:</strong> dýchá lépe a schne rychleji, ale rychleji promoká.</li></ul>'
          '<p>Membrána není všelék. Pokud voda přeteče přes okraj boty, uvnitř zůstane a vysychá pomalu. Na vlhké trasy s brody dává někdy větší smysl prodyšná bota, která rychle vyschne, než boty s membránou. Pro sníh a podzimní chlad je membrána praktická, pro léto je obvykle zbytečná.</p>'
          '<h2>Výběr podle sezóny a terénu</h2>'
          + T(['Podmínky', 'Na co se zaměřit'], [
              ['Léto, suché cesty', 'lehká prodyšná bota, nízká nebo polovysoká'],
              ['Jaro a podzim, vlhko', 'membrána nebo rychleschnoucí svršek, hrubší vzorek'],
              ['Zima, sníh', 'zateplení, vyšší svršek, hrubá podrážka, vhodná ponožka; viz <a href="/zimni-obuv/">zimní boty a sněhule</a>'],
              ['Skalnatý terén', 'pevná špička, tužší podrážka, dobrá opora'],
              ['Lesní cesty a louky', 'ohebnější podrážka a lehká váha'],
              ['Vícedenní trek', 'vyšší bota, tužší konstrukce, přizpůsobená batohu']]) +
          '<h2>Velikost a zkoušení</h2>'
          '<p>Boty zkoušejte odpoledne, kdy je noha mírně oteklá, a s ponožkami, v jakých budete chodit. Při chůzi z kopce nesmí prsty narážet do špičky, proto je potřeba rezerva přibližně v šíři palce. Pata musí držet a nesmí sjíždět nahoru a dolů, jinak vznikají puchýře. Pokud tlačí šířka nártu, nepomůže jen delší bota. Zkuste jiný střih nebo značku, protože každý výrobce používá trochu jiné kopyto.</p>'
          '<p>Nové boty rozchoďte na kratších trasách, než se vydáte na dlouhou túru. Kůže potřebuje čas, aby se přizpůsobila noze. Zacházení s tkaničkami také ovlivní komfort: pevnější utažení v patě a volnější v prstech brání sunutí nohy dopředu.</p>'
          '<h3>Ponožky a vložky</h3>'
          '<p>Ponožky jsou polovina pohodlí. Bavlna nasákne potem a drhne, naopak <a href="/merino-ponozky/">merino ponožky</a> nebo syntetické <a href="/sportovni-ponozky/">sportovní ponožky</a> odvádějí vlhkost a snižují riziko puchýřů. Pokud vám původní vložka nevyhovuje, vyberte vložku v kategorii <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>. U dlouhých tras se ponožky vyplatí vyměnit v polovině dne.</p>'
          '<h2>Dámské, pánské a dětské trekové boty</h2>'
          '<p>Dámské modely mají obvykle užší patu a lehčí konstrukci, pánské jsou širší. Neznamená to, že každá žena potřebuje dámský střih, důležité je padnutí. Dětské trekové boty musí být lehké, ohebné a s pevným držením paty. Děti rostou rychle, proto nohu měřte alespoň jednou za sezónu. Pro děti hrající si v blátě a na loukách jsou praktické boty, které se dají očistit a rychle vysuší.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší výběr trekových bot mají ' + B(('merrell', 'Merrell'), ('regatta', 'Regatta'), ('adidas', 'Adidas'), ('la-sportiva', 'La Sportiva'), ('cmp', 'CMP'), ('columbia', 'Columbia'), ('trespass', 'Trespass'), ('salomon', 'Salomon'), ('keen', 'Keen'), ('tecnica', 'Tecnica')) + '. Salomon, La Sportiva a Tecnica jsou spojené s horským prostředím, Merrell a Keen s pohodlným střihem pro každodenní turistiku a Regatta a Trespass nabízejí cenově dostupnější modely. Střih bývá důležitější než logo, proto vždy ověřte pocit v přední části.</p>'
          '<h2>Co dalšího se hodí na túru</h2>'
          '<p>Správná obuv bez dobrého vybavení nestačí. Na delší trasy se vyplatí <a href="/turisticke-batohy/">turistický batoh</a> se správně nastaveným nosným systémem, <a href="/trekove-hole/">trekové hole</a>, které odlehčí kolenům při sestupu, a <a href="/lahve-a-termosky/">láhev nebo termoska</a>. Přehled dalšího vybavení najdete v kategorii <a href="/outdoor/">outdoor a turistika</a>. Na lehké výlety v teple stačí <a href="/sandaly/">sportovní sandály</a> a pro přírodní styl chůze zkuste <a href="/barefoot-obuv/">barefoot boty</a>, které vyžadují postupné zvykání.</p>'
          '<h2>Péče o trekové boty</h2>'
          '<ol><li>Po túře vyndejte vložky a povolte tkaničky.</li>'
          '<li>Očistěte bláto kartáčem a vlhkým hadrem, bez agresivních čisticích prostředků.</li>'
          '<li>Sušte při pokojové teplotě, ne na topení ani u kamen.</li>'
          '<li>Kůži ošetřete vhodným přípravkem, textil impregnujte podle návodu.</li>'
          '<li>Membránu udržujte čistou, protože špína omezuje prodyšnost.</li>'
          '<li>Skladujte v suchu, ne zabalené ve vlhku.</li></ol>'
          '<p>Impregnace časem slábne, proto ji obnovujte, když voda přestane perlit. Opotřebovanou podrážku nebo odlepené místo nenechte být, protože při zatížení může selhat v nevhodnou chvíli.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Malé boty:</strong> prsty při klesání naráží do špičky a po hodinách bolí.</li>'
          '<li><strong>Membrána za každou cenu:</strong> v létě způsobí zbytečné přehřátí.</li>'
          '<li><strong>Nezkoušení s ponožkami:</strong> tenká ponožka v obchodě, silná na trase.</li>'
          '<li><strong>Nerozchozené boty na dlouhou túru:</strong> základ puchýřů.</li>'
          '<li><strong>Špatné sušení:</strong> topení deformuje podrážku a lepidlo.</li></ul>'
          '<p>Na Sportece porovnáte nabídky obchodů u konkrétního páru, zkontrolujete velikosti skladem a můžete se vrátit ke starším modelům, které mají stejné vlastnosti za příznivější podmínky.</p>',
    faq=[('Jak vybrat trekové boty?', 'Podle trasy, hmotnosti batohu a sezóny. Pro kratší túry stačí nízké nebo polovysoké, na hory s těžším batohem vysoké. Na podzim a zimu zvažte membránu.'),
         ('Jaký je rozdíl mezi nízkými a vysokými trekovými botami?', 'Nízké jsou lehčí a ohebnější, vysoké lépe drží kotník a chrání před kamením a vodou. Vybírejte podle terénu a zátěže, ne podle módy.'),
         ('Musí mít trekové boty membránu?', 'Nemusí. Membrána drží vodu venku, ale v horku zhoršuje větrání. Na léto stačí prodyšná bota, membrána se vyplatí v chladu a vlhku.'),
         ('Jak poznám správnou velikost?', 'Zkoušejte odpoledne s turistickými ponožkami. Prsty mají mít při klesání rezervu, pata nesmí sjíždět. Pokud prsty narážejí do špičky, je bota malá.'),
         ('Jak rozchodit nové boty?', 'Několikrát je obujte doma a vyražte na kratší trasy. Kůže se přizpůsobí noze postupně. Na vícedenní túru nikdy nevyrážejte v zcela nových botách.'),
         ('Čím se liší pánské a dámské trekové boty?', 'Dámské mívají užší patu a lehčí konstrukci, pánské jsou širší. Rozhoduje však padnutí, takže zkuste oba střihy.'),
         ('Mohu v trekových botách chodit po městě?', 'Ano, ale podrážka se rychle sjede a bota je tvrdší než běžné tenisky. Na denní nošení je pohodlnější nižší model nebo <a href="/tenisky/">tenisky</a>.'),
         ('Jak často měnit trekové boty?', 'Záleží na používání. Vyměňte je, když se podrážka sjede nebo odlepuje, svršek praská nebo bota propouští vodu. Dobrá péče životnost prodlužuje.'),
         ('Jak vyčistit a vysušit boty po dešti?', 'Očistěte kartáčem a vlhkým hadrem, vyjměte vložky a sušte při pokojové teplotě. Do mokrých bot dejte papír, který nasaje vlhkost, a po pár hodinách ho vyměňte.'),
         ('Jaké boty na zimní túry?', 'Zateplené s membránou, hrubou podrážkou a dostatečným prostorem na silnější ponožku. Vyšší svršek chrání před sněhem. Pro hlubší sníh zvažte specializované <a href="/zimni-obuv/">zimní boty a sněhule</a>.')],
)

# ------------------------------------------------------------------ pantofle-a-zabky
NEW['pantofle-a-zabky'] = dict(long=True,
    title='Pantofle a žabky: Crocs, nazouváky, domácí',
    desc='Pantofle, nazouváky, žabky a domácí obuv pánské, dámské i dětské. Jak vybrat materiál, velikost a typ podle účelu. Porovnejte nabídky obchodů.',
    intro='<p><strong>Pantofle a žabky</strong> patří k obuvi, kterou si lidé kupují rychle a často bez většího rozmyšlení. Přitom se velmi liší: žabky na horké dny, nazouváky do šatny a ke sprše, lehké klapky z pěny k vodě i teplé domácí pantofle na zimu. Nejlepší volba stojí na jednoduché otázce, kde je budete skutečně nosit.</p>'
          '<p>Na Sportece najdete pantofle vedle <a href="/sandaly/">sportovních sandálů</a>, <a href="/obuv-do-vody/">bot do vody</a> a <a href="/tenisky/">tenisek</a>, takže snadno porovnáte, co se na daný účel hodí nejlépe. Níže je průvodce typy, materiály, velikostmi a péčí, který pomůže vybrat pár, který vám nebude rozdírat prsty a nerozpadne se po jednom létě.</p>',
    guide='<h2>Typy pantoflí a k čemu slouží</h2>'
          '<p>Slovo pantofle zahrnuje velmi různé druhy obuvi. Rozdíl mezi nimi není jen ve vzhledu, ale především v tom, jak drží chodidlo a jaký materiál snese vodu, horko nebo studenou podlahu. Před nákupem proto zvažte, zda bude obuv sloužit hlavně venku, v interiéru, u vody nebo v šatně.</p>'
          + T(['Typ', 'Hodí se', 'Pozor na'], [
              ['Žabky', 'pláž, horké dny, rychlé nazutí', 'řemínek mezi prsty, nižší stabilita'],
              ['Nazouváky', 'bazén, šatna, volný čas', 'chodidlo drží jen horní pás'],
              ['Klapky z pěny', 'voda, zahrada, procházky po pláži', 'rozdílné střihy, vyberte šířku'],
              ['Kožené a korkové', 'volný čas, cesty, kancelář bez dress codu', 'voda jim škodí'],
              ['Domácí textilní', 'interiér, zima, chladné podlahy', 'nejsou do vody ani na ven'],
              ['Zimní s kožíškem', 'chladný interiér, zahrada', 'rychle se přehřejí v teple']]) +
          '<p>Chcete-li obuv, která pevněji drží, zvažte spíše <a href="/sandaly/">sportovní sandály</a> se zapínáním. Pro vodu s kameny nebo mořské dno je lepší <a href="/obuv-do-vody/">obuv do vody</a>, protože chrání před poraněním.</p>'
          '<h2>Materiál a komfort</h2>'
          '<p>Materiál určuje, jak dlouho pantofle vydrží a jak se noší. Pěna EVA je lehká a nepromokavá, guma pevnější a odolnější, kůže a korek se časem přizpůsobí noze, ale nesnášejí vodu. Textil a flís hřejí a hodí se do interiéru. Ovčí kůže poskytuje teplo i v chladu, ale vyžaduje opatrné čištění.</p>'
          '<ul><li><strong>EVA a pryž:</strong> lehké, rychle schnou, snadno se myjí.</li>'
          '<li><strong>Kůže a korek:</strong> tvarují se podle chodidla a mají anatomickou stélku.</li>'
          '<li><strong>Textil a flís:</strong> měkké, teplé a prané podle štítku.</li>'
          '<li><strong>Ovčí kůže nebo imitace:</strong> teplé, dobré na zimu a chladné dlažby.</li>'
          '<li><strong>Protiskluzová podrážka:</strong> důležitá u vody, na mokré dlažbě a u dětských modelů.</li></ul>'
          '<h2>Velikost a střih</h2>'
          '<p>Pantofle mají mít chodidlo uložené tak, aby pata nepřesahovala podrážku a prsty nezasahovaly přes přední okraj. Příliš velká obuv způsobuje šourání a zvyšuje riziko zakopnutí, příliš malá tlačí a obtiskuje se. U žabek hlídejte řemínek mezi palcem a druhým prstem. Pokud tře, zkuste jiný tvar nebo materiál.</p>'
          '<p>Různé značky používají různé střihy. Některé nabízejí užší a širší varianty, jiné mají volnější střih, který se přizpůsobí i širšímu chodidlu. Zkoušet se dá jen v prodejně, ale při nákupu online ověřte rozměr stélky, kterou výrobce často uvádí v centimetrech. Nechte si rezervu u modelů z pěny, které se mírně přizpůsobují teplem nohy.</p>'
          '<h3>Pantofle pro děti</h3>'
          '<p>Dětské pantofle potřebují zadní pásek nebo pevnější špičku, aby je dítě neztrácelo při běhu. U menších dětí je rozumná protiskluzová podrážka a výrazná barva, která je v písku vidět. Rodiče by měli sledovat, zda obuv nedrhne, a velikost kontrolovat přibližně každé tři měsíce. Pro delší procházky nebo hru na hřišti jsou lepší <a href="/sandaly/">sandály</a> nebo <a href="/tenisky/">tenisky</a>, pantofle jsou jen pro krátké chvíle.</p>'
          '<h2>Kdy pantofle nenosit</h2>'
          '<p>Pantofle a zejména žabky nejsou obuv na dlouhé procházky ani na zátěž. Nedrží patu a při chůzi je nutné je mírně přidržovat prsty, což zatěžuje chodidlo a lýtka. Nehodí se na kolo, za volant (hrozí sklouznutí z pedálu), do lesa ani do hor, kde patří <a href="/trekova-obuv/">trekové boty</a>. Při práci, kde hrozí pád předmětů, je potřeba uzavřená obuv. Při běhu a sportu volte <a href="/bezecka-obuv/">běžecké boty</a> nebo <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<p>Pokud máte problémy s nohama, například plochou nohu nebo bolest paty, dlouhé nošení pantoflí může potíže zhoršovat. Poraďte se s lékařem nebo ortopedem a zvažte obuv s anatomickou stélkou.</p>'
          '<h2>Pantofle k vodě a na dovolenou</h2>'
          '<p>U moře nebo bazénu se hodí obuv, která rychle schne a nekluže. Pěnové klapky jsou praktické, ale u hlubší vody nebo kamenitého dna je lepší <a href="/obuv-do-vody/">obuv do vody</a>. Při sbalení na dovolenou se vyplatí lehké žabky a jedny pohodlnější sandály. K pláži patří i <a href="/plavky/">plavky</a> a <a href="/plazove-doplnky/">plážové doplňky a osušky</a>. Na bazénu a v šatně pomáhají pantofle chránit před plísněmi a kluzkou podlahou.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Největší nabídku mají ' + B(('crocs', 'Crocs'), ('birkenstock', 'Birkenstock'), ('adidas', 'Adidas'), ('ugg', 'Ugg'), ('ipanema', 'Ipanema'), ('coqui', 'Coqui'), ('aquos', 'Aquos'), ('havaianas', 'Havaianas'), ('nike', 'Nike'), ('puma', 'Puma')) + '. Crocs jsou nejznámější díky lehkým klapkám z pěny, Birkenstock díky anatomické stélce, Havaianas a Ipanema díky žabkám, Ugg díky teplým domácím modelům a Adidas, Nike a Puma díky sportovním nazouvákům. Coqui a Aquos nabízejí cenově dostupnější modely pro děti i dospělé.</p>'
          '<h2>Péče a hygiena</h2>'
          '<ol><li>Gumové a pěnové pantofle opláchněte vodou s jemným mýdlem.</li>'
          '<li>Sušte je ve stínu, slunce a topení způsobují deformaci.</li>'
          '<li>Kožené a korkové otřete vlhkým hadrem a ošetřete impregnací.</li>'
          '<li>Textilní domácí perte podle štítku, vlněné spíše ručně.</li>'
          '<li>Vyjímatelnou stélku občas vyndejte a vyvětrejte.</li>'
          '<li>Nošené bez ponožek je pravidelně dezinfikujte nebo myjte.</li></ol>'
          '<p>Pantofle nošené bez ponožek se rychleji propotí. Pravidelná hygiena zabraňuje zápachu a snižuje riziko plísní. Doplňky na péči najdete v kategorii <a href="/doplnky-k-obuvi/">tkaničky, vložky a péče o boty</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Žabky na dlouhé procházky:</strong> nemají oporu klenby ani držení paty.</li>'
          '<li><strong>Domácí pantofle k vodě:</strong> textil nasákne a hůř schne.</li>'
          '<li><strong>Příliš velká velikost:</strong> noha klouže a zvyšuje se riziko zakopnutí.</li>'
          '<li><strong>Ignorování materiálu:</strong> kůže u bazénu nebo pěna u kamen nevydrží dlouho.</li>'
          '<li><strong>Nákup podle vzhledu:</strong> estetika není záruka pohodlí.</li></ul>'
          '<p>Na Sportece porovnáte nabídky obchodů u každého páru, zjistíte, které velikosti jsou skladem, a můžete se vrátit ke starším barvám, které mají stejné vlastnosti. Pro zimní měsíce s předstihem zvažte <a href="/zimni-obuv/">zimní boty a sněhule</a>, pro léto doplňte pantofle o <a href="/sandaly/">sandály</a>.</p>',
    faq=[('Jaký je rozdíl mezi žabkami a nazouváky?', 'Žabky mají řemínek mezi prsty a jsou lehké, nazouváky mají široký pás přes nárt a drží pevněji. Na vodu a v šatně se hodí oboje, na delší chůzi spíše nazouváky.'),
         ('Jaké pantofle vybrat k bazénu?', 'Lehké z pěny nebo gumy s protiskluzovou podrážkou, které rychle schnou. Kožené a textilní nejsou vhodné, protože vodu nesnáší.'),
         ('Jak vybrat správnou velikost pantoflí?', 'Pata nesmí přesahovat podrážku a prsty se nesmí dotýkat okraje. Ověřte rozměr stélky v centimetrech a respektujte střih výrobce.'),
         ('Hodí se žabky na dlouhé procházky?', 'Ne. Nemají oporu klenby ani pevné držení paty, takže zatěžují chodidlo i lýtka. Na delší chůzi zvolte sandály nebo tenisky.'),
         ('Jaké pantofle pro děti?', 'S protiskluzovou podrážkou a zadním páskem nebo pevnější špičkou, aby je dítě neztrácelo. Velikost kontrolujte přibližně každé tři měsíce.'),
         ('Jak čistit gumové a pěnové pantofle?', 'Opláchněte vlažnou vodou s mýdlem, případně jemným kartáčkem, a nechte vyschnout ve stínu. Na slunci nebo topení se deformují.'),
         ('Jak se starat o kožené pantofle?', 'Otřete vlhkým hadříkem a ošetřete impregnací nebo krémem na kůži. Chraňte je před vodou a sušte při pokojové teplotě.'),
         ('Mohu v pantoflích řídit auto?', 'Nedoporučuje se. Pantofle a žabky mohou při sešlápnutí pedálu sklouznout nebo se zaklínit, bezpečnější je uzavřená obuv s pevným držením paty.'),
         ('Jak poznat kvalitní domácí pantofle?', 'Podle stélky, protiskluzové podrážky a materiálu. Textil a flís hřejí, ovčí kůže je velmi teplá. Dobrá podrážka brání uklouznutí na dlažbě.'),
         ('Čím se liší pantofle Crocs od jiných klapek?', 'Crocs jsou vyrobené z lehké pěny, snadno se myjí a rychle schnou. Různé střihy mají různou šířku, proto sledujte popis modelu a tabulku velikostí.')],
)


# ---- extra sections appended to the guides (kept separate so the first drafts stay readable)
NEW['kopacky']['guide'] += (
    '<h2>Konstrukce kopaček: na co se dívat kromě podrážky</h2>'
    '<p>Za cenou a barvou se skrývá několik prvků, které se na hřišti projeví víc, než by se zdálo. Přední část svršku určuje cit při driblinku a střelbě: tenčí materiál přenáší dotek míče věrněji, silnější vrstva nebo texturovaný povrch zlepšuje kontakt při vlhku. Jazyk boty a límec kolem kotníku ovlivňují, zda noha drží stabilně. Stélka bývá vyměnitelná a dá se nahradit vlastní vložkou, což ocení hráči s plochou nohou nebo citlivou patou.</p>'
    '<p>Zapínání je dalším detailem. Klasické tkaničky dovolují jemné nastavení a jsou nejspolehlivější, zakrytá šněrovací část zlepšuje plochu pro kontakt s míčem. Pletené modely bez tkaniček nebo se skrytou šněrovací částí vypadají čistě, ale vyžadují přesně sedící velikost, protože se nedají pořádně dotáhnout.</p>'
    '<h2>Zima, déšť a rozmoklá hřiště</h2>'
    '<p>Na podzim a na jaře se hraje na mokrém terénu, který zkouší oboje: záběr i udržení tepla. Na rozmoklou trávu se hodí kopačky s delšími kolíky nebo SG podrážka, na tvrdě promrzlý povrch naopak raději multinopy nebo turfy, protože dlouhé kolíky se do zmrzlé země nezasunou rovnoměrně a zatěžují klouby. V zimě pomůže teplejší funkční ponožka a ochrana před promočením, ale nikdy nenavlékejte tak tlusté ponožky, aby kopačky tlačily. Po každém mokrém zápase boty důkladně vysušte.</p>'
    '<h2>Kdy je čas na nový pár</h2>'
    '<p>Kopačky se neopotřebují jen na podrážce. Zkontrolujte, zda nejsou kolíky sjeté nebo prasklé, zda se podrážka nedělí od svršku, zda se v patě neprotlačila vložka a zda svršek stále drží nohu. Dětem se mění velikost dřív, než se boty opotřebují, proto nevyhazujte pár, který je ještě v pořádku, a nabídněte jej mladším sourozencům nebo klubu. Starší modely z předchozích sezón mají obvykle stejné vlastnosti jako novinky.</p>'
    '<p>Rekreační hráč, který hraje jednou týdně, vystačí s jedním párem řadu let. Hráč s několika tréninky a zápasy týdně by měl počítat s výměnou po jedné až dvou sezónách, podle povrchu. Nejrychleji se ničí podrážka na umělé trávě a tvrdých hřištích.</p>')

NEW['sportovni-vyziva']['guide'] += (
    '<h2>Načasování: před, během a po tréninku</h2>'
    '<p>Doplňky se dají rozdělit podle toho, kdy je používáte. Před tréninkem má smysl lehká porce sacharidů, případně předtréninkový nápoj, pokud kofein snášíte. Během výkonu, hlavně u vytrvalostních sportů, se doplňují voda, minerály a rychlé sacharidy. Po tréninku se vyplatí kombinace bílkovin a sacharidů, ať už ve formě jídla, nebo koktejlu. Nejdůležitější je ale celodenní příjem, ne přesná minuta, ve které jste prášek vypili.</p>'
    '<h2>Vegetariáni, vegani a alergici</h2>'
    '<p>Při rostlinné stravě bývá obtížnější pokrýt bílkoviny a některé mikroživiny, proto je rostlinný protein praktický. Hledejte směsi, které kombinují více zdrojů, například hrách a rýži, protože se jejich aminokyselinové profily doplňují. Vegani by měli řešit také vitamín B12, který se v rostlinné stravě přirozeně nevyskytuje, a případně vitamín D a omega-3. Alergici si musí číst etiketu pozorně: výrobky mohou obsahovat stopy mléka, lepku, sóji nebo ořechů i tam, kde to nečekáte.</p>'
    '<h2>Hubnutí a redukce</h2>'
    '<p>Při snižování hmotnosti pomáhá hlavně mírný kalorický deficit, dostatek bílkovin a pohyb. Proteinové koktejly a tyčinky mohou usnadnit dodržení plánu, protože zasytí, ale nejsou nutností. Spalovače tuků jsou často směsi se stimulanty a nepracují zázračně. Pokud je zvažujete, přečtěte si složení, sledujte obsah kofeinu a při zdravotních potížích nebo užívání léků se poraďte s lékařem.</p>')

NEW['trekova-obuv']['guide'] += (
    '<h2>Šněrování a nastavení boty na trase</h2>'
    '<p>I dobrá bota může být nepohodlná, když je špatně zašněrovaná. Při stoupání povolte tkaničky v oblasti prstů a nártu, aby se noha mohla roztáhnout, a pevně držte patu. Při sestupu naopak utáhněte v horní části, aby chodidlo neklouzalo dopředu a prsty nenarážely do špičky. Pokud vám tlačí nárt, přeskočte jedno oko šněrování nebo zkuste jiné vedení tkaničky. Při dlouhých trasách se vyplatí zastavit a boty upravit, než vznikne puchýř.</p>'
    '<h2>Puchýře a péče o nohy</h2>'
    '<p>Puchýře vznikají třením, vlhkem a tlakem. Pomáhá správná velikost, suchá ponožka bez záhybů a včasná reakce: jakmile ucítíte horké místo, zastavte se a ošetřete jej náplastí nebo páskou. Nehty držte krátce zastřižené, protože dlouhé nehty při sestupu bolí. Při delší túře dopřejte nohám pauzu a nenechávejte je dlouho v mokré obuvi. Mokré ponožky vyměňte.</p>'
    '<h2>Kam vyrazit v jakých botách</h2>'
    '<p>Pro procházky po lesních cestách, hřebenovky v Beskydech nebo Krkonoších a výlety na pár hodin stačí lehčí nízká nebo polovysoká bota. Skalnaté trasy, strmé sestupy nebo vícedenní přechody s těžším batohem ocení vyšší tužší konstrukci. Zimní túry vyžadují obuv s hrubší podrážkou a ochranou před sněhem. Rozhoduje vždy konkrétní trasa, počasí a zátěž, ne obecné označení.</p>'
    '<h2>Trekové boty, trailové boty a sandály</h2>'
    '<p>Trekové boty nejsou jedinou obuví na túru. <a href="/trailove-boty/">Trailové běžecké boty</a> jsou lehké a rychlé, ale chrání méně a nesou menší zátěž. Sportovní sandály se hodí na mírné teplé trasy a přechody vody. Trekové boty jsou nejpevnější volbou pro kombinaci terénu, váhy batohu a dlouhých dní. Neexistuje obuv na všechno, proto stojí za to uvažovat podle trasy.</p>'
    '<h2>Lyžařský a zimní styl chůze</h2>'
    '<p>Na zimní túry po upravených stezkách stačí zateplená trekovka, v hlubokém sněhu pomáhají návleky, které brání sněhu vniknout shora. Zimní obuv se musí vejít na silnější ponožku, ale pořád nesmí být příliš velká. Vložka s hliníkovou fólií nebo zateplená stélka může pomoci při chladné zemi.</p>')

NEW['pantofle-a-zabky']['guide'] += (
    '<h2>Anatomická stélka a zdraví nohou</h2>'
    '<p>Plochá podrážka bez profilu zatěžuje chodidlo jinak než tvarovaná. Anatomická stélka podpírá klenbu a rozkládá tlak po celé ploše, což ocení lidé, kteří stojí nebo chodí v pantoflích delší dobu. Žabky bez opory jsou v tomto ohledu nejméně vhodné. Při nošení se prsty v řemínku napínají, aby obuv držela, a to zatěžuje svaly chodidla a při delším nošení může vést k únavě. Chodidlo si zaslouží občasný odpočinek na bosou nohu nebo v pohodlné obuvi s pevnou patou.</p>'
    '<h2>Pantofle do sprch a na veřejná místa</h2>'
    '<p>V bazénu, ve fitness centru nebo v hotelové sprše jsou pantofle praktickou ochranou před kluzkou podlahou a kožními infekcemi, například plísněmi nohou. Pro takové účely se hodí lehké nazouváky z pěny nebo gumy, které se dají umýt a vydezinfikovat. Textilní pantofle nebo kožené se pro veřejné sprchy nehodí, protože nasáknou a špatně schnou.</p>'
    '<h2>Zima, doma a chladné podlahy</h2>'
    '<p>Doma záleží především na tom, jaká je podlaha. Na dlažbě a laminátu jsou potřeba pantofle s pevnější podrážkou, která izoluje od chladu, na koberci stačí měkký textil. Pantofle s kožíškem nebo flísem hřejí, ale chodidlo v nich v teplé místnosti snadno zpotí. Protiskluzová podrážka je u starších lidí a dětí důležitá, protože hladká zadní část může na dlažbě sklouznout.</p>'
    '<h2>Jak dlouho vydrží a kdy je vyměnit</h2>'
    '<p>Pantofle se opotřebují hlavně na podrážce a v místě, kde se sjíždí pata. Vyměňte je, když je podrážka hladká a nedrží, když stélka ztratila tvar, nebo když se řemínek protrhl či povolil. U žabek je poškozený řemínek častým důvodem k výměně, protože už se nedá bezpečně nosit. Pěnové a gumové pantofle se časem zbarví a ztvrdnou, zejména po delším pobytu na slunci.</p>'
    '<h2>Dárek a obuv pro celou rodinu</h2>'
    '<p>Při nákupu pro rodinu se vyplatí kupovat podle věku. Dospělí dávají přednost pohodlí a anatomické stélce, děti lehkému materiálu a bezpečnému držení, senioři protiskluzové podrážce a stabilitě. Kupujete-li pantofle jako dárek, zvolte neutrální barvu a ověřte velikost, nebo dárek doplňte možností výměny. Pro celou rodinu se hodí podobné modely v různých velikostech, které se dají snadno rozlišit podle barev.</p>')

NEW['sportovni-vyziva']['guide'] += (
    '<h2>Hydratace jako základ</h2>'
    '<p>Nejlevnějším a často nejdůležitějším doplňkem zůstává voda. Už mírná dehydratace snižuje výkon a koncentraci, proto pijte průběžně během dne, ne jen při tréninku. Množství závisí na teplotě, intenzitě a individuálním pocení. Jako vodítko poslouží barva moči a pocit žízně. Při krátkém cvičení nepotřebujete žádné ionty, při několikahodinové zátěži už ano.</p>'
    '<h2>Jak porovnávat nabídky obchodů</h2>'
    '<p>Stejný produkt prodává více obchodů a rozdíly bývají v balení, dostupnosti příchutí a datu trvanlivosti. Porovnávejte vždy stejnou gramáž a příchuť a zkontrolujte, kolik dávek balení obsahuje. U produktů s krátkou trvanlivostí, jako jsou nápoje nebo gely, se podívejte, zda obchod uvádí datum. Při opakovaném nákupu se vyplatí sledovat cenu za dávku v čase.</p>')

NEW['trekova-obuv']['guide'] += (
    '<h2>Jak zkoušet boty doma i v obchodě</h2>'
    '<p>Při online nákupu ověřte délku stélky v centimetrech a porovnejte ji se svou nohou. Postavte se na papír, obkreslete chodidlo a změřte vzdálenost od paty k nejdelšímu prstu. Doma boty vyzkoušejte na koberci, projděte se po schodech nahoru i dolů a ověřte, zda pata nesjíždí a prsty nenarážejí. Pokud boty nesedí, vraťte je dříve, než se ušpiní, protože použité boty obchody nemusejí přijmout.</p>'
    '<h2>Hmotnost boty a únava</h2>'
    '<p>Každých sto gramů navíc na každé noze se při tisících krocích promítne do únavy. Proto těžká tuhá bota není automaticky lepší. Pro rychlé a lehké túry je lepší lehčí konstrukce, pro těžký batoh a náročný terén pevnější. Rozumný kompromis volí většina turistů, kteří chodí celodenní výlety s lehkým batohem.</p>')

NEW['pantofle-a-zabky']['guide'] += (
    '<h2>Jak porovnávat nabídky na Sportece</h2>'
    '<p>Pantofle se prodávají ve velkém množství barev a velikostí, a proto se dostupnost mezi obchody liší. U vybraného modelu porovnejte, zda obchod nabízí vaši velikost, jak dlouho trvá dodání a zda lze zboží vrátit. U značek, které mají několik střihů, ověřte přesně označení modelu, protože podobně vypadající pár může mít jinou šířku nebo stélku.</p>'
    '<h2>Sezónní nákup</h2>'
    '<p>Letní žabky a klapky se nejlépe kupují na jaře, kdy je výběr barev a velikostí největší. Domácí a zimní pantofle jsou v nabídce nejširší na podzim. Mimo sezónu bývá výběr užší, ale starší kolekce mívají stejné vlastnosti za příznivější podmínky. Nenechávejte nákup na poslední chvíli před dovolenou, protože oblíbené velikosti se vyprodají nejdřív.</p>')
