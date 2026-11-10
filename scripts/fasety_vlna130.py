"""sporteka.cz — facet landing texts wave 130: teplaky-puma, damske-plavky-roxy, detske-inline-brusle, kilpi-lyzarska-bunda.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ teplaky-puma
NEW['teplaky-puma'] = dict(
    title='Tepláky Puma: řady Essentials, střihy a velikosti',
    desc='Tepláky Puma pánské, dámské i dětské: rozdíl mezi řadami Essentials, fleece a tricot, střihy, velikosti a praní. Porovnejte nabídky českých obchodů.',
    intro='<p>Tepláky Puma jsou jedním z nejsnáze rozpoznatelných kousků značky, a přitom se pod stejným logem skrývá několik odlišných věcí. Základ tvoří řada Essentials z měkké teplákoviny na každý den, vedle ní stojí hladší tricotové kalhoty z tréninkové linie, klubové modely fotbalových týmů a dětské kolekce s licencovanými motivy. '
          'Na této stránce jsou jen tepláky Puma z kategorie <a href="/teplaky/">tepláky</a>, takže je nemusíte vyhledávat mezi kalhotami jiných výrobců. Průvodce vysvětluje, jak číst názvy modelů, čím se liší fleece od tricotu, jak sedí otevřený a manžetový konec nohavice a jak vybrat velikost. Najdete tu také srovnání s dalšími značkami a rady pro dámské, pánské i dětské střihy. '
          'Nabídky českých obchodů vidíte vedle sebe, takže poznáte, kde je vaše velikost ještě skladem.</p>',
    guide='<h2>Jak číst názvy modelů Puma</h2>'
          '<p>Názvy tepláků Puma vypadají jako zkratkový kód, ale řídí se pravidly, která se dají naučit za minutu. Slovo <strong>Sweatpants</strong> znamená klasické tepláky, <strong>Pant</strong> či <strong>Track Pant</strong> bývá sportovnější kalhota z hladšího materiálu. Za názvem řady následuje zkratka materiálu a konce nohavice. Značení se může mezi sezonami drobně měnit, proto ho berte jako vodítko a ověřte si složení v popisu zboží.</p>'
          + T(['Zkratka nebo slovo v názvu', 'Co obvykle znamená', 'Jak se to nosí'], [
              ['ESS, Essentials', 'základní celoroční řada s logem', 'každodenní kalhoty do města i domů'],
              ['FL', 'teplákovina s počesanou nebo froté rubovou stranou', 'teplejší a měkčí, na podzim a zimu'],
              ['TR', 'hladká tricotová pletenina bez huňatého vnitřku', 'lehčí, rychleji schne, vhodná na trénink'],
              ['cl', 'zakončení nohavice manžetou', 'zúžený vzhled, drží u kotníku'],
              ['op', 'otevřený konec nohavice', 'rovnější linie, přes boty nebo naboso do bot'],
              ['No. 1 Logo', 'výrazné logo na stehně nebo boku', 'čistě stylová záležitost'],
              ['Team, klubové kalhoty', 'tréninkové kalhoty fotbalových týmů', 'na zápasové rozcvičení a trénink']]) +
          '<p>Nejdůležitější je dvojice FL a TR. Kdo chce především pohodlné kalhoty na gauč a na procházku, vybere FL. Kdo chce kalhoty na běh, do posilovny nebo na tréninkové hřiště, dá přednost TR. Pokud v názvu žádná zkratka není, rozhodne složení: vyšší podíl bavlny znamená měkkost, vyšší podíl polyesteru rychlejší schnutí.</p>'
          '<h2>Řady, které v nabídce poznáte</h2>'
          '<p>Značka Puma je sportovní firma s tradicí v kopané, běhu a streetwearu, a podle toho vypadají i její tepláky. V nabídce se opakuje několik typických okruhů.</p>'
          '<ul><li><strong>Essentials:</strong> nejširší řada v mnoha barvách. Najdete v ní variantu s malým logem na hrudi nebo stehně, variantu s velkým nápisem a dvoubarevné provedení. Pro většinu lidí je to nejrozumnější volba na každý den.</li>'
          '<li><strong>Classics:</strong> retro vzhled s lemováním a kontrastním pruhem po straně. Sedí lidem, kterým se líbí sportovní styl starších let.</li>'
          '<li><strong>Dámské modely s vysokým pasem:</strong> v názvu často ležérní slovo Comfort nebo označení High-Waist, kalhoty s širším a vyšším pásem, které drží tvar.</li>'
          '<li><strong>Kovové a zdobené varianty:</strong> modely s metalickým potiskem nebo grafikou, určené do města a ne na pot.</li>'
          '<li><strong>Klubové kalhoty:</strong> modely fotbalových týmů, například se znakem a barvami klubu, jsou tréninkového střihu.</li>'
          '<li><strong>Dětské kolekce:</strong> kromě jednobarevných kalhot nabízí značka i licenční motivy z filmů a her, takže se v nabídce objeví kalhoty pro děti s postavami z oblíbených příběhů.</li></ul>'
          '<h2>Střih, který Puma šije</h2>'
          '<p>Většina tepláků Puma sedí rovněji než přiléhavě. Pánské modely mají obvykle klasický regular střih, někdy označený jako slim nebo tapered, který se k nohavici mírně zužuje. Hodí se ke sportovním botám a nepůsobí ani příliš objemně, ani příliš těsně. Dámské kalhoty ve stejné řadě se liší užším pasem, mírně vyšším sedem a rozdílnou délkou nohavice. Označení Comfort naznačuje volnější sed, označení Slim přiléhavější. Přesný rozměr ale nepoznáte z názvu, jen z tabulky.</p>'
          '<p>Pokud kalhoty nosíte do posilovny, vybírejte tricotové zúžené kusy. Pro každodenní nošení s tenisky je nejuniverzálnější rovná nohavice s manžetou, která se dá vyhrnout nebo nechat spadnout na botu. Klubové modely často mají zip u kotníku, kterým se kalhoty navlečou přes kopačky nebo chrániče.</p>'
          '<h2>Velikosti: co je u Pumy jinak</h2>'
          '<p>Velikost S, M a L nic neříká o skutečném obvodu pasu. Puma uvádí rozměry v tabulce u každého modelu a my doporučujeme postup, který funguje u všech značek: změřit kalhoty, které vám sedí, a porovnat je s rozměry produktu. Tepláky s pružným pasem a šňůrkou odpustí chybu o jednu velikost, ale délka nohavice se upravit nedá.</p>'
          + T(['Rozměr', 'Jak ho změřit', 'Proč na něm záleží'], [
              ['Pas', 'položte kalhoty naplocho a změřte pás napříč, výsledek násobte dvěma', 'pružný pas toleruje malé rozdíly'],
              ['Boky', 'nejširší místo kalhot pod pasem napříč', 'rozhoduje u přiléhavých dámských střihů'],
              ['Vnitřní šev', 'od rozkroku po konec nohavice', 'určuje, kde nohavice skončí nad botou'],
              ['Obvod nohavice', 'konec nohavice napříč', 'rozhoduje, zda půjdou přes boty bez zipu']]) +
          '<p>Nakupujete-li přes internet, jednoduše se vyplatí vybrat model, který lze snadno vrátit, a vyzkoušet jej s ponožkami a botami, které k němu budete nosit.</p>'
          '<h2>Dámské, pánské a dětské tepláky Puma</h2>'
          '<p><strong>Pánské</strong> kalhoty mají delší nohavici a rovnější linii od pasu k boku. <strong>Dámské</strong> mají užší pas, o něco širší bok a často vyšší sed, aby kalhoty nesklouzávaly. Pokud vám střih jednoho druhu nesedí, zkuste druhý: unisex se Puma neprodává výslovně, ale mnoho žen nosí rovnější pánské kalhoty a muži zase volnější dámské.</p>'
          '<p>U <strong>dětí</strong> platí, že rostou rychleji, než se kalhoty obnosí. Vybírejte pružný pas se šňůrkou a manžetu u kotníku, kterou lze o rok později vyhrnout. Kolena bývají u hravých dětí nejzatíženější místo, proto se hodí hustší teplákovina. Dětská velikost se uvádí ve výšce dítěte, ne ve věku, takže ji změřte doma u zdi.</p>'
          + T(['Výška dítěte', 'Odhadovaný věk', 'Poznámka'], [
              ['104 cm', 'zhruba 3–4 roky', 'předškolní velikost'],
              ['116 cm', 'zhruba 5–6 let', 'začátek školní docházky'],
              ['128 cm', 'zhruba 7–8 let', 'běžná velikost prvního stupně'],
              ['140 cm', 'zhruba 9–10 let', 'kalhoty se prodlužují rychle'],
              ['152 cm', 'zhruba 11–12 let', 'přechod k pánské a dámské velikosti'],
              ['164 cm', 'zhruba 13–14 let', 'často už dospělá XS nebo S']]) +
          '<p>Věk je pouze orientační, každé dítě roste jinak. Rozhodující je tedy skutečná výška a obvod pasu. Starším dětem často sedí už dospělá velikost XS.</p>'
          '<h2>Puma ve srovnání s dalšími značkami</h2>'
          '<p>Při srovnávání se nabízí několik dalších značek, které v kategorii najdete: ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('under-armour', 'Under Armour'), ('champion', 'Champion'), ('fila', 'Fila'), ('lacoste', 'Lacoste')) + '. '
          'Adidas a Nike jsou nejbližší soupeři Pumy ve sportovním pojetí. Under Armour sází spíš na funkční a přiléhavé kalhoty pro trénink. Champion, Fila a Lacoste táhnou módní a streetwearovou linkou, kde záleží víc na vzhledu než na funkci. Puma stojí uprostřed: kalhoty jsou dostatečně sportovní na hřiště a zároveň dobře vypadají ve městě. Mezi modely jednotlivých firem je rozdíl hlavně ve střihu a v logu, ne tolik v tom, jak se v nich cvičí.</p>'
          '<p>Máte-li oblíbenou značku, prohlédněte si i sousední výběry: <a href="/nike-teplaky/">Nike tepláky</a>, <a href="/jordan-teplaky/">Jordan tepláky</a>, <a href="/teplaky-tommy-hilfiger/">Tepláky Tommy Hilfiger</a> a pro fitness <a href="/gymbeam-teplaky/">GymBeam tepláky</a>.</p>'
          '<h2>Co nosit s teplákami Puma</h2>'
          '<p>Logo Pumy bývá velké a výrazné, takže se kalhoty dobře kombinují s jednoduchým vrškem. K sytým barvám sáhněte po neutrálním tričku, ke černým teplákům s logem se hodí <a href="/mikiny/">mikina</a> v jiném odstínu. Chcete-li celý outfit sladit, hledejte <a href="/soupravy/">soupravu</a> stejné řady. Pro trénink vyberte <a href="/sportovni-tricka/">sportovní tričko</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>, v teplejším počasí zvažte <a href="/sportovni-kratasy/">sportovní kraťasy</a> nebo <a href="/leginy/">legíny</a>. Základní přehled všeho, co k tomu patří, je v kategorii <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>'
          '<h2>Praní a péče o potisk</h2>'
          '<p>Na tepláky Puma se vztahují stejná pravidla jako na každou teplákovinu s potiskem. Perte je naruby, nejlépe při 30 až 40 °C, a nepoužívejte aviváž, která nanáší vrstvu na vlákna a u funkčních materiálů zhoršuje odvod potu. Logo z gumového nebo plastového potisku se nesmí žehlit a nesuší se v sušičce při vysoké teplotě, protože by popraskalo. Tmavé a světlé kusy perte zvlášť. Žmolky na stehnech odstraňte strojkem na textil. Vlhké kalhoty vytáhněte do tvaru a sušte volně.</p>'
          '<h2>Jak poznat dobrou nabídku</h2>'
          '<ul><li>Porovnejte přesný název modelu včetně zkratky, ne jen obrázek. Dvoje na pohled stejné kalhoty se mohou lišit materiálem.</li>'
          '<li>Zjistěte, zda jde o aktuální kolekci, nebo starší řadu. Starší kusy bývají levnější, ale velikostní řada bývá neúplná.</li>'
          '<li>Dívejte se na to, kdo je prodejcem a jaké jsou podmínky vrácení zboží.</li>'
          '<li>Pozor na nápadně nízké ceny u neznámých obchodů. Napodobeniny značky se vyskytují u všech velkých sportovních firem.</li>'
          '<li>Pokud nakupujete víc kusů, využijte obchod, kde se doprava spojí do jedné zásilky.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi tepláky Puma FL a TR?',
         'FL označuje teplákovinu s měkkým počesaným nebo froté rubem, která zahřeje a hodí se na podzim a zimu. TR je hladší tricotová pletenina bez huňatého vnitřku. Je lehčí, rychleji schne a lépe se hodí na trénink.'),
        ('Jak vybrat velikost tepláků Puma?',
         'Změřte pas, boky a vnitřní šev kalhot, které vám sedí, a porovnejte je s rozměry v tabulce u konkrétního modelu. Samotné označení S, M nebo L nestačí, protože rozměry se mohou mezi řadami lišit.'),
        ('Co znamená v názvu cl a op?',
         'Zkratka cl obvykle označuje nohavici s manžetou u kotníku, op nohavici s otevřeným koncem. Manžeta drží u nohy a zužuje siluetu, otevřená nohavice je rovnější a lépe se obléká přes boty.'),
        ('Jsou tepláky Puma vhodné na trénink?',
         'Ano, ale vybírejte správnou řadu. Na běh a posilovnu se hodí tricotové kalhoty TR nebo tréninkové klubové modely se zipem u kotníku. Silnější teplákovina je pohodlná, ale při pocení těžkne.'),
        ('Srazí se tepláky Puma při praní?',
         'Bavlněné modely se mohou při prvním praní mírně srazit, hlavně při vysoké teplotě nebo v sušičce. Perte je naruby na doporučených 30 až 40 °C a sušte na vzduchu, pak si drží tvar i velikost.'),
        ('Jak vybrat dětské tepláky Puma?',
         'Podle výšky dítěte, ne podle věku. Vezměte pružný pas se šňůrkou, manžetu u kotníku, kterou lze vyhrnout, a hustší materiál na kolena. Věkové údaje v tabulce jsou jen orientační.'),
        ('Jak se starat o potisk loga na teplákách?',
         'Perte kalhoty naruby, vyhněte se aviváži a nesušte je při vysoké teplotě. Potisk se nesmí žehlit, protože by se roztavil nebo popraskal. Při sušení kalhoty vytáhněte do tvaru.'),
        ('Čím se liší dámské a pánské tepláky Puma?',
         'Dámské mají užší pas, širší bok, často vyšší sed a kratší nohavici. Pánské mají rovnější linii a delší nohavici. Pokud vám střih jedné skupiny nesedí, zkuste druhý, rozdíl je především v proporcích.'),
        ('Čím se Puma liší od Adidas a Nike?',
         'Všechny tři značky nabízejí podobné sportovní tepláky, liší se hlavně logem, střihem a řadami. Puma bývá o něco volnější a každodennější, Adidas a Nike mají širší nabídku tréninkových materiálů. Jistotu dá až tabulka velikostí.'),
        ('Mohu tepláky Puma nosit každý den?',
         'Ano, řada Essentials je určená právě na každodenní nošení. Pro běžný provoz zvolte střední gramáž a rovnou nohavici, v zimě zateplenou variantu FL a v létě lehčí tricot.'),
        ('Jak poznám napodobeninu tepláků Puma?',
         'Podezřelé jsou nápadně nízké ceny, nejasný prodejce a nekvalitní fotografie bez štítku. Kontrolujte štítek s materiálem a velikostí, kvalitu švů a logo. Nakupujte u prodejců s jasnými podmínkami vrácení.')
    ])

# ------------------------------------------------------------------ damske-plavky-roxy
NEW['damske-plavky-roxy'] = dict(
    title='Dámské plavky Roxy: vrchní a spodní díly na surf a pláž',
    desc='Dámské plavky Roxy: bikiny, bralette, trojúhelníky, cheeky i boardshortky. Střihy pro surf, pláž a vodu, velikosti a údržba. Porovnejte obchody.',
    intro='<p>Dámské plavky Roxy se od klasických plaveckých kostýmů liší už tím, že jsou to většinou dvoudílné modely, u kterých si vrchní a spodní díl kombinujete zvlášť. Značka vychází ze surfingu a plážového stylu, takže v nabídce najdete bralette, trojúhelníkové podprsenky, spodní díly se zavazováním po stranách, vysoké střihy i dámské boardshortky. '
          'Tato stránka ukazuje jen plavky Roxy z kategorie <a href="/damske-plavky/">dámské plavky</a>. Průvodce vysvětluje rozdíl mezi střihy, jak poznat plavky určené na surf, jak správně zvolit velikost zvlášť pro horní a dolní díl a jak o materiál pečovat, aby nevybledl. '
          'Řešíte-li spíš plavání v bazénu, přečtěte si také srovnání v kapitole o závodních kostýmech. Nabídky českých obchodů vidíte vedle sebe, takže poznáte, kde je kombinace ve vaší velikosti.</p>',
    guide='<h2>Co dělá plavky Roxy jiné než bazénový kostým</h2>'
          '<p>Velkou část dámských plavek na trhu tvoří jednodílné závodní kostýmy z odolné pleteniny, které vydrží chlór a hodiny plavání. Roxy míří jinam: na pláž, k vodě, na surfovací prkno a na prázdniny. Proto jsou to hlavně dvoudílné sestavy, kde se vrchní a spodní díl prodávají samostatně. Díky tomu si můžete každý kus vybrat ve vlastní velikosti a vzájemně kombinovat barvy a vzory.</p>'
          + T(['Vlastnost', 'Plavky Roxy', 'Bazénový závodní kostým'], [
              ['Typický střih', 'dvoudílný, bralette, trojúhelník, cheeky', 'jednodílný, s úzkými ramínky, často otevřená záda'],
              ['Účel', 'pláž, surf, dovolená, opalování', 'plavecký trénink a závody'],
              ['Hlavní materiál', 'pružná elastická pletenina s polyamidem nebo polyesterem', 'chlorovzdorný polyester nebo speciální tkanina'],
              ['Vzory', 'květiny, tropické motivy, barevné potisky', 'jednobarevné nebo jednoduché dekory'],
              ['Sezónní nasazení', 'léto, moře, jezero', 'celý rok, bazén']]) +
          '<p>Z toho plyne praktické pravidlo: Roxy volte na moře, jezero, dovolenou a surfování, ne na každodenní plavecký trénink v chlorované vodě. Ten patří do kategorií jako <a href="/speedo-plavky/">Speedo plavky</a> nebo <a href="/arena-plavky/">Arena plavky</a>. Rozdíl uvidíte i na střihu: plavky na plavání drží tělo pevně, plážové modely tolik nestahují.</p>'
          '<h2>Vrchní díly: bralette, trojúhelník, bandeau a další</h2>'
          '<p>U horního dílu rozhoduje, kolik opory potřebujete a k čemu plavky použijete. Nejčastější tvary v nabídce vidíte v přehledu.</p>'
          + T(['Střih', 'Jak vypadá', 'Pro koho a k čemu'], [
              ['Bralette', 'krátký top bez kostic, tvarem připomíná sportovní podprsenku', 'surf, volejbal, aktivní den na pláži; drží lépe než trojúhelník'],
              ['Trojúhelník', 'dvě trojúhelníkové košíčky stahované tkanicemi', 'opalování a lehký pohyb; velikost se upravuje zavázáním'],
              ['Brassière', 'širší pás pod prsy, pevnější tvar', 'více opory, delší pobyt ve vodě'],
              ['Bandeau', 'pás bez ramínek', 'opalování bez pruhů, ne na vlny'],
              ['Střih s kosticemi nebo vyjímatelnými vycpávkami', 'podprsenkový střih', 'větší poprsí, více tvaru a opory']]) +
          '<p>Pro surfování a aktivní sporty vybírejte top, který se zavazuje na zádech nebo má pevný pás pod prsy a ramínka vedená přes lopatky. Vlna dokáže strhnout volný trojúhelník, zatímco bralette zůstane na místě. Pro opalování je lepší trojúhelník, který se dá libovolně upravit.</p>'
          '<h2>Spodní díly: cheeky, high leg, tie side a boardshortky</h2>'
          '<p>Spodní díl ovlivňuje, jak se v plavkách cítíte, i jak dobře drží ve vlnách. V názvech modelů se opakují označení, která se vyplatí znát.</p>'
          '<ul><li><strong>Cheeky:</strong> kratší pokrytí zadní části, oblíbený střih na pláž.</li>'
          '<li><strong>High leg:</strong> vyšší vykrojení na bocích, které opticky prodlužuje nohy. V kombinaci s vyšším pasem vypadá retro.</li>'
          '<li><strong>Tie side:</strong> zavazování po stranách, kterým se dá nastavit velikost i výška kalhotek na boku.</li>'
          '<li><strong>Mini:</strong> menší pokrytí, určené především do slunce a k vodě.</li>'
          '<li><strong>Střih se zřasením:</strong> jemné nabrání vzadu, které zdůrazní tvar a skryje lehké nedokonalosti.</li>'
          '<li><strong>Boardshortky:</strong> dámské kraťasy do vody, delší než klasické spodní díly, určené na surf a paddleboard. Pro plavání a pro pohyb ve vlnách jsou nejpraktičtější, protože se nesesmeknou ani při pádu z prkna.</li></ul>'
          '<p>Chcete-li si koupit boardshortky na běžné chození, podívejte se i do kategorie <a href="/plavky/">plavky</a> a k nim doplňky v <a href="/plazove-doplnky/">plážových doplňcích</a>.</p>'
          '<h2>Velikost: horní a spodní díl se vybírají odděleně</h2>'
          '<p>Největší výhodou dvoudílných plavek je to, že každý díl můžete koupit v jiné velikosti. U horního dílu rozhoduje obvod pod prsy a velikost košíčku, u dolního obvod boků a případně pasu. Plavky se při smáčení lehce roztáhnou, proto se vybírají přiléhavě, ale nikoli těsně. Pokud top vyjede z vody uvolněný, byl od začátku velký.</p>'
          + T(['Měření', 'Kde měřit', 'Na co dát pozor'], [
              ['Obvod hrudníku', 'v nejširším místě přes prsa', 'vybírejte podle tabulky značky'],
              ['Obvod pod prsy', 'těsně pod prsy, vodorovně', 'rozhoduje u střihů s pásem'],
              ['Obvod pasu', 'v nejužším místě trupu', 'důležité u vysokých spodních dílů'],
              ['Obvod boků', 'v nejširším místě', 'hlavní rozměr pro spodní díl']]) +
          '<p>Při váhání mezi dvěma velikostmi se u zavazovaných modelů vyplatí větší, protože tkanice velikost upraví. U modelů s pevným pasem vyberte raději menší, plavky se ve vodě trochu roztáhnou. Při online nákupu ověřte, zda vám obchod prodá každý díl zvlášť, a podívejte se na podmínky vrácení.</p>'
          '<h2>Jak vybrat podle toho, co budete dělat</h2>'
          '<ul><li><strong>Surf a paddleboard:</strong> bralette nebo brassière s úzkým pásem a spodní díl s pevnějším střihem nebo boardshortky.</li>'
          '<li><strong>Plážový volejbal a hry ve vodě:</strong> přiléhavý top a spodek, který se při skoku neposouvá.</li>'
          '<li><strong>Opalování a odpočinek:</strong> trojúhelníkový top a cheeky nebo tie side, které lze upravit podle potřeby.</li>'
          '<li><strong>Dovolená s dětmi:</strong> spodní díl s pevnějším střihem a top s ramínky, které nesklouzávají při hrách. Pro děti jsou v nabídce <a href="/detske-plavky/">dětské plavky</a>.</li>'
          '<li><strong>Cesta na kajak a vodní sporty:</strong> top zavazovaný vzadu a boardshortky, které chrání stehna před třením.</li></ul>'
          '<h2>Materiál a péče, aby plavky vydržely</h2>'
          '<p>Plážové plavky bývají z elastické pleteniny, nejčastěji polyamidu nebo polyesteru s podílem elastanu. Takový materiál je pružný a rychle schne, ale citlivý na tři věci: slunce, chlór a tření. Po koupání ho opláchněte sladkou vodou, aby se z látky vypláchla sůl a písek. Perte ručně ve vlažné vodě, bez aviváže a bez bělicích prostředků. Plavky nemačkejte ani nekruťte, jen jemně vymáčkněte a nechte schnout ve stínu.</p>'
          '<ul><li>Nesušte plavky na přímém slunci, barvy bledou a elastan rychle stárne.</li>'
          '<li>Nesedejte v mokrých plavkách na drsný povrch, pletenina se zadírá.</li>'
          '<li>Tmavé a světlé plavky perte zvlášť, ať se barvy nepřenesou.</li>'
          '<li>Vyměňte vložky, pokud se zdeformovaly, nebo je vyndejte při praní.</li>'
          '<li>Neskladujte vlhké plavky v pytlíku, vznikají skvrny a zápach.</li></ul>'
          '<h2>Roxy ve srovnání s dalšími značkami plavek</h2>'
          '<p>V kategorii dámských plavek najdete také ' + B(('speedo', 'Speedo'), ('arena', 'Arena'), ('calvin-klein', 'Calvin Klein')) + '. '
          'Speedo a Arena jsou značky se silným zázemím v plavání a nabízejí hlavně kostýmy na trénink a závody. Calvin Klein se zaměřuje na módní a minimalistický styl. Roxy leží mezi nimi: sportovní aktivita u vody ano, ale ne závodní plavání. Další výběry najdete v landingu <a href="/damske-plavky-calvin-klein/">Dámské plavky Calvin Klein</a>, <a href="/decathlon-damske-plavky/">Decathlon dámské plavky</a> a v přehledu <a href="/roxy-plavky/">Roxy plavky</a>, kde jsou i další pláže a surf produkty značky. Hledáte-li jednodušší nabídku bez dalších značek, otevřete kategorii <a href="/plavky/">plavky</a>.</p>'
          '<h2>Jak plavky zkombinovat</h2>'
          '<p>Dvoudílné plavky mají tu výhodu, že barvy a vzory můžete míchat. Jednobarevný spodní díl se hodí k potištěnému topu a naopak. Tmavé kusy hubnou a jsou univerzální, světlé se rychleji špiní od krému na opalování. K plavkám se na pláži hodí lehké šaty nebo kraťasy, na surf pak lycrové triko proti spálení. Vhodné doplňky jsou ve výběru <a href="/plazove-doplnky/">plážové doplňky</a>.</p>'
          '<h2>Na co se zaměřit při koupi</h2>'
          '<ul><li>Zkontrolujte složení v popisu, nejen název. Elastan zajišťuje pružnost, podšívka komfort.</li>'
          '<li>Ověřte, zda je v modelu vyndavací vycpávka, nebo je přišitá. Přišité se hůř suší.</li>'
          '<li>Podívejte se na zapínání. Zavazování na zádech se dá upravit, zip nebo spona drží pevně.</li>'
          '<li>U barevných a potištěných modelů se ptejte, jak se chovají při dlouhém slunění.</li>'
          '<li>Při koupi jednoho dílu zjistěte, zda je druhý díl ve stejném odstínu k dispozici.</li></ul>',
    faq=[
        ('Jsou plavky Roxy vhodné na plavání v bazénu?',
         'Pro pravidelné plavání v chlorované vodě jsou lepší závodní kostýmy z chlorovzdorného materiálu. Roxy je určena hlavně na pláž, surf, jezero a moře. Občasné koupání v bazénu zvládnou, ale materiál se chlórem rychleji opotřebuje.'),
        ('Jaký střih plavek Roxy vybrat na surf?',
         'Vyberte bralette nebo brassière s pevným pásem pod prsy a spodní díl se střihem, který nesklouzává. Dobře se osvědčují také dámské boardshortky, protože při pádu z prkna nezmění polohu a chrání stehna.'),
        ('Mohu koupit vrchní a spodní díl v různých velikostech?',
         'Ano, u dvoudílných plavek se oba díly prodávají zvlášť. Horní díl vybírejte podle obvodu hrudníku nebo pod prsy, spodní podle boků. Před koupí ověřte, že obchod prodává každý díl samostatně.'),
        ('Co znamená cheeky a high leg?',
         'Cheeky je spodní díl s menším pokrytím zadní části. High leg má vysoké vykrojení po stranách, které opticky prodlužuje nohy, často v kombinaci s vyšším pasem.'),
        ('Jak vybrat velikost plavek, aby nesklouzávaly?',
         'Plavky mají přiléhat, ale netlačit. Ve vodě se pletenina lehce roztáhne, proto raději volte pevnější sedu. U zavazovaných střihů dobře pomůže nastavení tkanicemi, u pevných horních dílů rozhoduje obvod pod prsy.'),
        ('Jak plavky Roxy prát?',
         'Po koupání je opláchněte sladkou vodou, perte ručně ve vlažné vodě bez aviváže a bělidel a jemně vymáčkněte. Neždímejte je a neperte v pračce při vysoké teplotě, jinak ztratí pružnost.'),
        ('Proč plavky po sezóně blednou?',
         'Barvivo trpí sluncem, solí a chlórem. Zpomalíte to oplachem po každém koupání a sušením ve stínu. Úplně se tomu vyhnout nedá, plavky jsou materiál vystavený náročnému prostředí.'),
        ('Jaký je rozdíl mezi bralette a trojúhelníkem?',
         'Bralette je krátký top bez kostic a tvarem připomíná sportovní podprsenku, drží pevně a hodí se na aktivity. Trojúhelník se stahuje tkanicemi, nabízí upravitelnost, ale menší oporu při pohybu.'),
        ('Co jsou dámské boardshortky?',
         'Jsou to delší plavecké kraťasy určené na surf a vodní sporty. Mají pevný pas a nohavice po stehna nebo nad kolena, takže se ve vlnách nesesmeknou a chrání kůži před třením o prkno.'),
        ('Jak dlouho plavky vydrží?',
         'Při péči a rozumném používání vydrží několik sezón. Jakmile se pletenina začne třepit, ztratí pružnost nebo prosvítá, vyměňte je. Každodenní použití v bazénu životnost zkracuje.')
    ])

# ------------------------------------------------------------------ detske-inline-brusle
NEW['detske-inline-brusle'] = dict(
    title='Dětské inline brusle: nastavitelné, velikosti a bezpečnost',
    desc='Dětské inline brusle: nastavitelné velikosti, 2v1 a 4v1, kolečka, brzda a chrániče. Jak vybrat bruslení pro začátečníky i větší děti. Porovnejte nabídky.',
    intro='<p>Dětské inline brusle se vybírají jinak než dospělé, protože dítě z nich vyroste rychleji, než se opotřebují. Proto je v nabídce tolik nastavitelných modelů, u kterých se délka boty posouvá o několik velikostí, a proto dává smysl dívat se hlavně na stabilitu, brzdu a pohodlí, ne na rychlost. '
          'Na této stránce jsou brusle pro děti z kategorie <a href="/inline-brusle/">inline brusle</a>, od jednoduchých modelů pro první kroky přes kolečkové brusle 2v1 a 4v1 až po větší modely s vyššími kolečky pro školáky. Průvodce vysvětluje, jak změřit nohu, kolik místa nechat na růst, jak vybrat kolečka a ložiska a které chrániče jsou nezbytné. '
          'Nabídky českých obchodů vidíte vedle sebe, takže snadno najdete velikost, která je právě skladem.</p>',
    guide='<h2>Čím se dětské brusle liší od dospělých</h2>'
          '<p>U dětí se mění nejen velikost nohy, ale i způsob, jakým jezdí. Začátečník hodně stojí na místě, drží se zábradlí a snaží se vyvážit těžiště. Brusle proto mají nižší podvozek, měkčí botu a snadno dosažitelnou brzdu. Dětské modely bývají i lehčí, protože malá noha nemá sílu zvedat těžkou botu. Rozdíly vidíte v přehledu.</p>'
          + T(['Vlastnost', 'Dětské brusle', 'Dospělé brusle'], [
              ['Velikost', 'často nastavitelná přes tři až čtyři čísla', 'pevná velikost'],
              ['Podvozek', 'nižší, stabilnější', 'delší rám, vyšší kola'],
              ['Kolečka', 'menší, často kolem 64 až 80 mm', 'větší, 80 až 110 mm'],
              ['Brzda', 'u začátečnických modelů vždy', 'volitelná nebo vyměnitelná'],
              ['Bota', 'měkká, s vyztuženou patou', 'tuhá nebo polotuhá, podle sportu'],
              ['Zapínání', 'přezky a tkanice, u větších dětí rychlé šněrování', 'přezky, šněrování, systém BOA']]) +
          '<p>Brusle pro dospělé jsou určeny pro hmotnější uživatele a vyšší rychlosti. Pokud dítě už vyrostlo z dětských velikostí, vyplatí se projít kategorii <a href="/inline-brusle-damske/">dámské inline brusle</a> nebo <a href="/inline-brusle-panske/">pánské inline brusle</a>.</p>'
          '<h2>Nastavitelné brusle a jak správně změřit nohu</h2>'
          '<p>Nastavitelná bota má posuvnou část, kterou přesunete o několik velikostí, takže brusle vydrží dvě až tři sezóny. Jeden model tak typicky pokrývá rozmezí jako 29–32, 33–36 nebo 37–40, přesné rozsahy ale určuje výrobce a je nutné je ověřit u konkrétního kusu. Při nastavení se mění délka boty i vnitřní bota, pata ale zůstává ukotvená.</p>'
          '<ol><li>Postavte dítě bez bot na list papíru a obkreslete chodidlo tužkou svislě drženou u paty.</li>'
          '<li>Změřte vzdálenost od paty po nejdelší prst. Měřte u obou nohou a použijte delší.</li>'
          '<li>Přičtěte přibližně půl centimetru na rezervu, ale ne víc, aby v botě noha neklouzala.</li>'
          '<li>Porovnejte výsledek s tabulkou značky. Označení S, M a L nemá jednotný význam.</li>'
          '<li>Zkoušejte s tenkými sportovními ponožkami, v nichž bude dítě jezdit.</li></ol>'
          '<p>Rezerva na růst nemá být velká. Příliš volná bota způsobí, že se noha při prvním pádu zkroutí, a dítě se bude bát dalšího pokusu. Proto je lepší vybrat nastavitelné brusle, které se dají zmenšit, než kupovat o tři čísla větší model.</p>'
          '<h2>Typy dětských kolečkových bruslí</h2>'
          '<p>V nabídce uvidíte několik označení, která vypadají podobně, ale znamenají něco jiného.</p>'
          '<ul><li><strong>Inline brusle:</strong> kolečka v řadě za sebou, rychlejší a pohyblivější, ale vyžadují vyváženost. Nejlepší pro dítě, které už zvládá základy.</li>'
          '<li><strong>Quad (čtyřkolky):</strong> dvě kolečka vedle sebe vpředu a dvě vzadu, stabilnější při stání, vhodné pro nejmenší.</li>'
          '<li><strong>Modely 2v1 a 4v1:</strong> brusle, které se přestavují mezi dvěma nebo čtyřmi konfiguracemi, například z čtyřkolek na inline, někdy s přidáním ledových nožů. Praktické, pokud dítě nevíte, co se mu bude líbit.</li>'
          '<li><strong>Svítící kolečka:</strong> kolečka s LED diodami, které při otáčení svítí. Zábavné pro děti, ale pro bezpečnost není světlo rozhodující.</li>'
          '<li><strong>Freestylové a fitness modely:</strong> pro starší děti, které chtějí jezdit rychleji, slalomovat nebo se učit triky.</li></ul>'
          '<p>Pro první kroky je vhodné začít na stabilnějším modelu a po půl roce přejít na klasický inline podvozek. Pro bruslení na ledě mají děti vlastní kategorie: <a href="/detske-zimni-brusle/">dětské zimní brusle</a>, <a href="/hokejove-brusle/">hokejové brusle</a> nebo <a href="/rekreacni-brusle/">rekreační brusle na led</a>.</p>'
          '<h2>Kolečka, ložiska a podvozek</h2>'
          '<p>Průměr koleček se uvádí v milimetrech a spolu s tvrdostí určuje chování bruslí. Menší kolečka jsou stabilnější a lépe se rozjíždějí, větší jedou rychleji a plynuleji, ale vyžadují větší jistotu. Tvrdost se uvádí číslem s písmenem A: čím vyšší číslo, tím tvrdší a rychlejší kolečko, ale tím méně přilnavé na hrubém povrchu. Pro děti, které jezdí hlavně po chodníku a cyklostezce, jsou vhodná středně tvrdá kolečka.</p>'
          + T(['Součást', 'Co dělá', 'Co hlídat u dětských modelů'], [
              ['Kolečka', 'určují rychlost a přilnavost', 'menší průměr pro začátečníky, nepoškozený povrch'],
              ['Ložiska', 'umožňují plynulé otáčení', 'číslo ABEC je jen orientační, důležitější je čistota a mazání'],
              ['Podvozek (rám)', 'drží kolečka a přenáší sílu', 'pevný, nízký rám, který se nekroutí'],
              ['Brzda', 'zastavení patou', 'snadno dostupná, vyměnitelná pryžová botka'],
              ['Přezky a tkaničky', 'fixace nohy', 'nezadrhávat, mít pojistku proti samovolnému uvolnění']]) +
          '<p>Ložiska jsou častý předmět marketingu, přestože u dětí je jejich třída podružná. Dítě jezdí pomalu a krátce, takže rozdíl mezi levnějšími a dražšími ložisky nepozná. Důležité je naopak udržovat je čistá. Po jízdě v mokru nebo písku brusle vysušte a ložiska občas očistěte a namažte.</p>'
          '<h2>Brzda a bezpečnost</h2>'
          '<p>Základní brzdou je pryžová botka na zadním kole jedné nohy, kterou dítě přitlačí vyklopením špičky nahoru. Na začátku se musí naučit brzdit dřív než rozjíždět. Procvičte to na trávníku nebo rovné ploše bez provozu. Pokud brzda vzadu chybí, dítě se bude zastavovat nárazem do něčeho nebo pádem. Pro menší děti proto platí: brzda vždy.</p>'
          '<p>Druhým pilířem bezpečnosti jsou chrániče. Základní sada obsahuje čtyři části: helmu, chrániče kolen, loktů a zápěstí. Zápěstí je zranitelné proto, že se při pádu dopředu instinktivně opřeme rukama. Chránič se zpevněnou dlaní tyto zlomeniny a odřeniny omezí. Sady dostupné v obchodech se označují například jako sady po třech nebo více kusech.</p>'
          '<ul><li><strong>Helma:</strong> musí sedět rovně na čele a nesmí se vychylovat. Pokud ji dítě používá i na kole nebo koloběžce, podívejte se na <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</li>'
          '<li><strong>Kolena a lokty:</strong> tvrdá skořepina vpředu a polstrování uvnitř. Velikost musí odpovídat nohám a rukám, aby chránič nesjel.</li>'
          '<li><strong>Zápěstí:</strong> opora s pevnou dlaňovou destičkou, kterou nahradí rukavice jen částečně.</li>'
          '<li><strong>Oblečení:</strong> dlouhé kalhoty a mikina ochrání před odřením lépe než kraťasy.</li></ul>'
          '<p>Kompletní přehled chráničů je v kategoriích <a href="/detske-chranice/">dětské chrániče</a> a <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Značky v nabídce a pro koho jsou</h2>'
          '<p>V dětských inline bruslích vidíte široké spektrum výrobců: ' + B(('powerslide', 'Powerslide'), ('raven', 'Raven'), ('fila', 'Fila'), ('k2', 'K2'), ('rollerblade', 'Rollerblade'), ('tempish', 'Tempish'), ('oxelo', 'Oxelo'), ('roces', 'Roces')) + '. '
          'Powerslide, K2 a Rollerblade patří k tradičním značkám, které mají v sortimentu i nastavitelné dětské modely a řady pro pokročilejší děti. Raven a Tempish jsou české značky se zaměřením na rodinné a rekreační bruslení a nabízejí i kombinace 2v1 a 4v1. Fila vyrábí barevné dětské modely, často v sadách s chrániči. Oxelo je privátní značka sportovního řetězce a míří na jednoduché a cenově dostupné modely pro začátečníky. Roces má dlouhou tradici v kolečkových bruslích a čtyřkolkách.</p>'
          '<p>Pokud hledáte konkrétní výrobce, otevřete <a href="/inline-brusle-k2/">Inline brusle K2</a> nebo <a href="/inline-brusle-bauer/">Inline brusle Bauer</a>. Pro porovnání s modely pro dospělé je tu i kategorie <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a> a pro děti, které dávají přednost jiné aktivitě, <a href="/kolobezky/">koloběžky</a> nebo <a href="/freestyle-kolobezky/">freestyle koloběžky</a>.</p>'
          '<h2>Jak naučit dítě jezdit</h2>'
          '<ol><li>Nasaďte všechny chrániče a helmu, i když jde jen o pár minut jízdy.</li>'
          '<li>Začněte na trávníku nebo koberci. Dítě má stát v mírném předklonu s pokrčenými koleny.</li>'
          '<li>Pak přejděte na hladký povrch a učte chůzi jako kachna: špičky ven, malé krůčky.</li>'
          '<li>Další krok je odraz a klouzání na jedné noze. Vyvarujte se strmých kopců.</li>'
          '<li>Zastavení trénujte jako první dovednost. Až pak zrychlujte.</li></ol>'
          '<p>Většina dětí se naučí základy za několik odpolední. Nejde o rychlost, ale o jistotu. Pokud se dítě bojí, dejte mu čas a nechte ho zvyknout si na brusle doma, třeba na koberci.</p>'
          '<h2>Údržba a skladování</h2>'
          '<p>Po jízdě vysušte vnitřní botu a brusle uložte v suchu. Kolečka se opotřebovávají nerovnoměrně, proto je zhruba po několika týdnech jízdy prohoďte mezi pozicemi, aby se sjížděla rovnoměrně. Brzdu vyměňte, jakmile se pryž sjede téměř ke kovovému držáku. Šrouby u koleček a rámu čas od času dotáhněte. Zbytky písku z ložisek vyčistíte jemným kartáčkem. Před zimou brusle uložte do chladnější a suché místnosti, nikoli na topení.</p>'
          '<h2>Na co se zaměřit při koupi</h2>'
          '<ul><li>Zkontrolujte rozsah velikostí a porovnejte ho s naměřenou délkou nohy.</li>'
          '<li>Vyberte model s brzdou, pokud dítě jezdí poprvé.</li>'
          '<li>Zeptejte se, zda lze vnitřní botu vyjmout a vyprat nebo vysušit.</li>'
          '<li>Pokud dítě roste, zvolte nastavitelné brusle místo větší pevné velikosti.</li>'
          '<li>Při koupi sady s chrániči ověřte jejich velikosti, aby nebyly příliš velké.</li></ul>',
    faq=[
        ('Kolik místa nechat na růst u dětských inline bruslí?',
         'Přibližně půl centimetru za nejdelším prstem, ne víc. Příliš velká bota způsobuje, že noha klouže, dítě se hůř vyvažuje a hrozí pády. Na růst proto raději vybírejte nastavitelné brusle, které se dají zmenšit.'),
        ('Jak fungují nastavitelné dětské brusle?',
         'Mají posuvnou část boty, kterou přesunete o několik velikostí, takže brusle vydrží dvě i tři sezóny. Rozsah velikostí je uvedený u každého modelu a vždy se vyplatí ověřit, zda pokrývá aktuální délku nohy dítěte.'),
        ('Čím se liší inline brusle od čtyřkolek?',
         'Inline mají kolečka v řadě za sebou, jsou rychlejší a pohyblivější. Čtyřkolky mají kolečka ve dvojicích a stojí stabilněji, proto se hodí pro nejmenší děti a úplné začátečníky.'),
        ('Co znamená označení 2v1 a 4v1?',
         'Jde o brusle s přestavitelným podvozkem. Typicky se přepínají mezi uspořádáním čtyřkolek a inline, někdy je k nim i varianta s ledovým nožem. Hodí se, pokud dítě ještě nevíte, jaký styl mu vyhovuje.'),
        ('Jaké chrániče dítě na brusle potřebuje?',
         'Helmu a chrániče kolen, loktů a zápěstí. Zápěstí se při pádu zraňuje nejčastěji, protože se dítě instinktivně opře o ruce. Chrániče musí sedět přiléhavě, jinak při pádu sjedou.'),
        ('Od kolika let mohou děti jezdit na inline bruslích?',
         'Záleží na dítěti. Většina dětí zvládá první kroky ve věku předškoláka až začátku školní docházky. Rozhodující je rovnováha a ochota nosit chrániče, ne věk. Pro nejmenší jsou vhodnější stabilnější čtyřkolky.'),
        ('Jak velká mají být kolečka u dětských bruslí?',
         'Pro začátečníky jsou vhodnější menší kolečka, která jsou stabilnější a lépe se rozjíždějí. Větší děti přecházejí na větší průměr kvůli plynulejší a rychlejší jízdě. Přesný rozměr je vždy uveden u konkrétního modelu.'),
        ('Je číslo ABEC u ložisek důležité?',
         'U dětských bruslí příliš ne. Dítě jezdí pomaleji a krátce, takže rozdíl mezi třídami nepozná. Mnohem víc na plynulost působí čistota a mazání ložisek, proto po jízdě v písku nebo mokru brusle očistěte.'),
        ('Jak dítě naučit brzdit?',
         'Začněte na trávníku nebo koberci. Dítě nastaví jednu nohu dopředu a zvedne špičku, čímž brzdu na zadním kole přitlačí k zemi. Brzdění procvičte dřív než rozjezd a jezděte na rovné ploše bez provozu.'),
        ('Jak pečovat o dětské inline brusle?',
         'Po jízdě vysušte vnitřní botu a uložte brusle v suchu. Pravidelně prohazujte kolečka mezi pozicemi, aby se sjížděla rovnoměrně, vyměňte opotřebenou brzdu a dotáhněte šrouby. Před zimou brusle nenechávejte u topení.')
    ])

# ------------------------------------------------------------------ kilpi-lyzarska-bunda
NEW['kilpi-lyzarska-bunda'] = dict(
    title='Kilpi lyžařská bunda: dámské, pánské i vyhřívané modely',
    desc='Kilpi lyžařská bunda: dámské a pánské střihy, vyhřívané a hybridní modely, izolace a membrána. Jak vybrat velikost a porovnat obchody.',
    intro='<p>Kilpi je česká outdoorová značka a její lyžařské bundy patří k nejčastějším volbám lidí, kteří chtějí na svah praktickou a dobře vypadající bundu bez zbytečného přemýšlení. Sortiment je široký: dámské modely v pastelových i sytých barvách, pánské bundy v klasických odstínech, hybridní kousky s izolací a také bundy s vestavěným vyhříváním. '
          'Na této stránce vidíte jen lyžařské bundy Kilpi z kategorie <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>. Průvodce vysvětluje, jak číst názvy modelů, čím se liší klasická zateplená bunda od hybridní a vyhřívané, jak vybrat velikost na vrstvení a jak bundu praním a impregnací udržet funkční. '
          'Porovnáte také Kilpi s dalšími značkami, a to i při výběru kalhot a doplňků. Nabídky českých obchodů vidíte vedle sebe, takže snadno poznáte, kde je vaše velikost skladem.</p>',
    guide='<h2>Jak číst názvy a řady Kilpi</h2>'
          '<p>Názvy modelů Kilpi jsou osobní jména nebo krátká slova, například Lin, Dalila, Flip, Turnau nebo Hyder. Rozlišovat se dají hlavně podle koncovky. Dámské modely často končí písmenem W (dámská verze, například Flip-w nebo Lorien-w), pánské mají M, případně žádnou koncovku. Pro jistotu ale vždy sledujte, zda popis uvádí dámský, pánský nebo dětský střih, a čtěte tabulku velikostí.</p>'
          + T(['Typ bundy', 'Jak funguje', 'Pro koho'], [
              ['Zateplená lyžařská bunda', 'syntetická izolace mezi svrchní látkou a podšívkou', 'běžné lyžování od podzimu do jara, nejčastější volba'],
              ['Hybridní bunda (například s izolací Primaloft)', 'izolace jen v hlavních zónách, lehčí konstrukce a často pružné boky', 'aktivní lyžaři, kteří se zahřívají pohybem'],
              ['Bunda s vestavěným vyhříváním', 'topné prvky napájené baterií, ovládané tlačítkem', 'lidé, kteří rychle mrznou, nebo dlouhé dny na lanovce'],
              ['Lehká bunda bez izolace', 'slouží jako ochrana proti větru a vodě, teplo řeší vrstvy pod ní', 'skialpinismus, jaro, vrstvení'],
              ['Dětské modely', 'zkrácené střihy se zesílenými rukávy a kolenními ochranami', 'děti, které se učí lyžovat']]) +
          '<p>Kilpi tedy nenabízí jen jednu bundu, ale rodinu modelů. Pro rekreační lyžování na sjezdovkách stačí zateplená bunda se členěním, pro delší dny s častým stáním ve frontách pomůže vyhřívání. Aktivním lyžařům s vysokou výměnou tepla se hodí hybridní model.</p>'
          '<h2>Izolace, membrána a voděodolnost</h2>'
          '<p>Lyžařská bunda musí zvládnout dvě věci zároveň: udržet teplo a odvádět vlhkost. Většina modelů používá kombinaci vodoodpudivého povrchu, membrány a syntetické izolace. Hodnoty uvádí výrobce jako číslo v milimetrech vodního sloupce pro odolnost proti vodě a v gramech na metr čtvereční za den pro prodyšnost. Čím vyšší číslo, tím lepší parametr, ale rozhodující je poměr obou hodnot a skutečné podmínky.</p>'
          + T(['Parametr', 'Co ukazuje', 'Jak ho číst'], [
              ['Vodní sloupec (mm)', 'odolnost proti pronikání vody', 'nižší hodnoty stačí na suchý sníh, vyšší na mokrý a déšť'],
              ['Prodyšnost (g/m²/24 h)', 'kolik vlhkosti materiál propustí ven', 'důležitá při aktivním lyžování a potu'],
              ['Izolace (gramáž)', 'tloušťka tepelné vrstvy', 'vyšší hodnota znamená teplejší, ale objemnější bundu'],
              ['Zalepené švy', 'zabraňují pronikání vody švem', 'důležité u bund pro mokrý sníh'],
              ['Sněhová zástěra', 'pružná lemovka uvnitř bundy', 'drží sníh venku při pádu']]) +
          '<p>Pro běžné sjezdové lyžování v Evropě je důležitější prodyšnost než extrémní voděodolnost. Sníh na lyžařských střediscích obvykle není tak mokrý jako déšť, ale pot se uvnitř hromadí hned. Jestli se budete spíš potit, vyberte model s lepší prodyšností a větráním pod pažemi. Pokud často stojíte a čekáte, ocení se silnější izolace.</p>'
          '<h2>Vyhřívané bundy Kilpi: jak fungují a co čekat</h2>'
          '<p>Značka nabízí i bundy s integrovaným vyhříváním. Jde o tenké topné prvky v zádech, na hrudi nebo v kapsách, které napájí malá přenosná baterie, takzvaný powerbank. Zapínají se tlačítkem a často mají několik stupňů ohřevu. Teplo se vytváří okamžitě a udržuje se po dobu, kterou udává výrobce u konkrétního modelu a stupně.</p>'
          '<ul><li><strong>Kdy se vyplatí:</strong> při dlouhém stání na lanovce, při fotografování, u lidí, kteří rychle mrznou, nebo na horských túrách s častými zastávkami.</li>'
          '<li><strong>Co si ověřit:</strong> zda je baterie součástí balení, jaká je její kapacita a jak dlouho vydrží na kterém stupni.</li>'
          '<li><strong>Péče:</strong> před praním baterii vždy vyjměte a postupujte podle štítku. Topné prvky nikdy neperte při vysoké teplotě.</li>'
          '<li><strong>Omezení:</strong> baterie se v mrazu vybíjí rychleji, takže ji nenoste venku odhalenou a zálohu držte u těla.</li>'
          '<li><strong>Nezapomínejte na vrstvy:</strong> vyhřívání doplňuje vrstvení, nenahrazuje termoprádlo.</li></ul>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Lyžařská bunda má sedět tak, aby pod ní bylo místo na funkční prádlo a mikinu nebo flís, ale aby nebyla tak velká, že fouká dovnitř. Měřte obvod hrudníku, pasu a délku paží a porovnejte s tabulkou. Při váhání mezi dvěma velikostmi se vyplatí vybrat podle toho, kolik vrstev budete nosit. Při pohybu paží nad hlavou nesmí bunda povyjet nad pas a rukávy mají zakrývat zápěstí.</p>'
          + T(['Kontrola', 'Jak ji provést', 'Co by mělo platit'], [
              ['Ramena', 'zvedněte obě ruce nad hlavu', 'bunda nestahuje a nepovyjede nad boky'],
              ['Rukávy', 'natáhněte paže dopředu', 'rukávy zakrývají zápěstí a překrývají rukavice'],
              ['Délka', 'předkloňte se', 'zadní díl zakrývá bedra'],
              ['Obvod hrudníku', 'zapněte zip a nadechněte se', 'bunda netlačí a ještě se dá vrstvit'],
              ['Kapuce', 'nasaďte helmu', 'kapuce se přes ni dá natáhnout']]) +
          '<p>Dámské střihy Kilpi bývají přiléhavější v pase a delší na zádech. Pánské jsou rovnější a objemnější v hrudníku. Pokud vám střih jednoho druhu nesedí, zkuste druhý nebo se podívejte na model označený jako unisex.</p>'
          '<h2>Funkční detaily, které poznáte na svahu</h2>'
          '<ul><li><strong>Sněhová zástěra:</strong> pružný lem uvnitř bundy, který zabrání pronikání sněhu při pádu.</li>'
          '<li><strong>Kapsa na skipas:</strong> kapsa na rukávu, která se hodí u turniketů.</li>'
          '<li><strong>Větrání pod paží:</strong> zipy, které se otevřou při stoupání nebo na slunci.</li>'
          '<li><strong>Manžety s úpravou:</strong> suchý zip nebo pružná manžeta, která dosedá na rukavice.</li>'
          '<li><strong>Kapuce:</strong> odnímatelná nebo přes helmu, podle způsobu lyžování.</li>'
          '<li><strong>Odepínání kalhot:</strong> u některých modelů je uvnitř zip nebo patentka, kterou se bunda spojí s kalhotami.</li>'
          '<li><strong>Odepínací vnitřní vrstva:</strong> u některých modelů se dá izolace vyjmout a bunda funguje jako větrovka.</li></ul>'
          '<p>Při výběru nejde o to, aby bunda měla všechny prvky, ale aby měla ty, které opravdu využijete. Pro rodinné lyžování na sjezdovkách jsou nejdůležitější sněhová zástěra, kapsa na skipas a pevné zipy.</p>'
          '<h2>Kilpi ve srovnání s dalšími značkami lyžařských bund</h2>'
          '<p>V kategorii najdete také ' + B(('hannah', 'Hannah'), ('helly-hansen', 'Helly Hansen'), ('alpine-pro', 'Alpine Pro'), ('columbia', 'Columbia'), ('rossignol', 'Rossignol')) + '. '
          'Kilpi, Hannah a Alpine Pro jsou česky a středoevropsky orientované značky s širokou nabídkou pro rekreační lyžaře. Helly Hansen a Rossignol patří do skupiny značek s vazbou na sjezdové lyžování a vyšší technické kategorie, Columbia je americká outdoorová značka se zimními bundami s vlastní izolací. Kilpi se vyplatí hlavně lidem, kteří hledají praktickou bundu pro rekreační lyžování a uvažují i o sadě s kalhotami. Rozdíl mezi značkami je dobře vidět na střihu, barvách a nabídce funkcí, než na tom, zda bunda zvládne běžný lyžařský den.</p>'
          '<p>Chcete-li porovnat s konkurencí, otevřete <a href="/hannah-lyzarska-bunda/">Hannah lyžařská bunda</a>, <a href="/helly-hansen-lyzarska-bunda/">Helly Hansen lyžařská bunda</a>, <a href="/alpine-pro-lyzarska-bunda/">Alpine Pro lyžařská bunda</a> a <a href="/lyzarska-bunda-columbia/">Lyžařská bunda Columbia</a>.</p>'
          '<h2>Co k bundě Kilpi dokoupit</h2>'
          '<p>Bunda je jen jedna vrstva. Pod ni patří <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>, které odvádí pot od těla, na nohy <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>, případně <a href="/hannah-lyzarske-kalhoty/">Hannah lyžařské kalhoty</a>, pokud chcete porovnat nabídku. Celé sety najdete v přehledu <a href="/lyzarske-obleceni/">lyžařské a snowboardové oblečení</a>, a pokud preferujete jednodílné řešení, podívejte se na <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a>. K tomu patří <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-helmy/">helma</a>, <a href="/lyzarske-bryle/">brýle</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>. Pro přechodná období vám poslouží i <a href="/softshellove-bundy/">softshellové bundy</a> a pro městské nošení <a href="/zimni-bundy/">zimní bundy</a>.</p>'
          '<h2>Péče a impregnace</h2>'
          '<p>Lyžařské bundy se perou méně často než běžné oblečení, ale pravidelnou péči potřebují. Používejte prací prostředek určený na funkční textilie, ne běžný prášek s aviváží, který zanáší membránu. Perte při nízké teplotě podle štítku, zapněte všechny zipy a suché zipy a vyjměte baterii z vyhřívaných modelů. Po vyprání se voděodolná úprava na povrchu obnoví krátkým působením tepla, pokud to štítek povoluje. Když voda přestane stékat po povrchu a vsakuje se, je čas na novou impregnaci ve spreji nebo v pračce.</p>'
          '<ul><li>Neskladujte bundu vlhkou, může vzniknout plíseň.</li>'
          '<li>Na konci sezóny bundu vyperte a pověste na ramínko, nesbalte ji pevně do tašky.</li>'
          '<li>Nepoužívejte aviváž ani bělidlo.</li>'
          '<li>Zipy občas otřete od soli a písku a ošetřete voskem.</li>'
          '<li>Drobné trhliny v látce zalepte nálepkou nebo opravte dříve, než se zvětší.</li></ul>',
    faq=[
        ('Jaká je velikost lyžařské bundy Kilpi?',
         'Velikost se řídí tabulkou u konkrétního modelu, ve které najdete obvod hrudníku, pasu a délku. Dámské modely mají koncovku W, pánské M nebo žádnou. Vybírejte podle toho, kolik vrstev pod bundu nosíte.'),
        ('Jak fungují vyhřívané bundy Kilpi?',
         'Mají v zádech, na hrudi nebo v kapsách topné prvky, které napájí přenosná baterie. Zapínají se tlačítkem a mají několik stupňů ohřevu. Před praním baterii vždy vyndejte a kontrolujte štítek.'),
        ('Je lepší hybridní, nebo klasická zateplená bunda?',
         'Klasická zateplená bunda je teplejší a vhodná na stání a pomalejší lyžování. Hybridní model s odlišnou izolací v zónách je lehčí a prodyšnější, hodí se aktivním lyžařům, kteří se při jízdě zahřívají.'),
        ('Co znamená vodní sloupec u lyžařské bundy?',
         'Vodní sloupec v milimetrech udává odolnost materiálu proti pronikání vody. Vyšší číslo znamená lepší ochranu, ale důležitější je i prodyšnost a zalepené švy. Pro běžné sjezdovky stačí střední hodnoty.'),
        ('Jak poznám dámskou a pánskou bundu Kilpi?',
         'Podle popisu a koncovky v názvu. Dámské modely často končí písmenem W, pánské M. Přesvědčte se v tabulce velikostí, protože střih dámských modelů bývá přiléhavější v pase a pánských volnější v hrudníku.'),
        ('Jak prát lyžařskou bundu?',
         'Použijte prostředek na funkční textil bez aviváže, zapněte zipy, perte při doporučené teplotě a u vyhřívaných modelů vyjměte baterii. Obnovu voděodolného povrchu proveďte impregnací, když voda přestane stékat.'),
        ('Do jaké zimy se hodí bunda Kilpi?',
         'Záleží na izolaci a vrstvení. Zateplená bunda s termoprádlem pod ní zvládne běžné lyžařské mrazy. V extrémním chladu přidejte další vrstvu nebo zvolte vyhřívaný model a pamatujte na ochranu hlavy, rukou a nohou.'),
        ('Čím se Kilpi liší od Hannah a Alpine Pro?',
         'Všechny tři jsou střední Evropou orientované značky s podobným zaměřením na rekreační lyžaře. Liší se střihem, barevností a detaily. Rozhodnout by měla tabulka velikostí a funkce, které opravdu využijete.'),
        ('Dá se k bundě Kilpi dokoupit kalhoty?',
         'Ano, mnoho modelů lze doplnit lyžařskými kalhotami stejné značky nebo jiného výrobce. Kombinaci hledejte v kategorii lyžařských kalhot, kde najdete i přehled podle značky a velikosti.'),
        ('Jak dlouho vydrží lyžařská bunda?',
         'Při péči a rozumném používání mnoho sezón. Životnost zkracuje pot, tření batohu, nesprávné praní a skladování ve vlhku. Obnovujte impregnaci a bundu před uložením vyperte a uschovejte volně zavěšenou.')
    ])
