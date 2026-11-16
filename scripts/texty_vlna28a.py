"""sporteka.cz — wave 28a (16. 11. 2026): long texts for ksiltovky, teplakove-soupravy, crop-topy, perove-bundy.
General true facts only, no prices, no product counts. New Era line names (59FIFTY, 9FORTY, 39THIRTY, 9FIFTY) described in general terms;
down fill power and RDS explained without invented figures. Brands linked only if present in src/texts/znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ ksiltovky
NEW['ksiltovky'] = dict(long=True,
    title='Kšiltovky: New Era, snapback, trucker i běžecké',
    desc='Kšiltovky New Era 59FIFTY, 9FORTY i 39THIRTY, snapbacky, truckery a běžecké kšiltovky. Jak změřit velikost a porovnat nabídky českých e-shopů.',
    intro='<p><strong>Kšiltovka</strong> stíní oči a obličej, drží vlasy při běhu a pro mnoho lidí je hlavně doplňkem, kterým dávají najevo, komu fandí. Mezi kšiltovkami jsou ale velké rozdíly. Pevná kšiltovka s rovným kšiltem a přesnou velikostí sedí jinak než nastavitelný snapback s plastovou přezkou, trucker se síťovinou vzadu nebo lehká běžecká čepice z funkční tkaniny, která váží pár desítek gramů.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů na jednom místě a objednávku pak dokončíte u obchodu, který si vyberete. V katalogu jsou zastoupeny například ' + B(('new-era', 'New Era'), ('47-brand', "'47"), ('under-armour', 'Under Armour'), ('calvin-klein', 'Calvin Klein'), ('lacoste', 'Lacoste')) + '; u New Era a \'47 převažují licencované modely týmů NFL, NHL a MLB. Kšiltovky spadají pod <a href="/cepice-a-celenky/">čepice a čelenky</a>, k letním sportům se hodí také <a href="/sportovni-bryle/">sportovní brýle</a>.</p>',
    guide='<h2>Typy kšiltovek podle zapínání</h2>'
          '<p>Na první pohled se kšiltovky liší barvou a logem, při nošení ale rozhoduje hlavně to, jak se nastavuje obvod. Podle toho se také hledají v obchodech, proto se vyplatí znát základní názvy.</p>'
          + T(['Typ', 'Jak se nastavuje', 'Typický příklad'], [
              ['Fitted (uzavřená)', 'nijak, kupuje se přesná velikost', 'New Era 59FIFTY'],
              ['Snapback', 'plastová přezka s kolíčky vzadu', 'New Era 9FIFTY, většina truckerů'],
              ['Strapback', 'textilní nebo kožený pásek se sponou', 'nízké bavlněné kšiltovky, část modelů 9FORTY'],
              ['Stretch fit', 'pružný pruh v obvodu, velikosti v rozpětí', 'New Era 39THIRTY'],
              ['Suchý zip', 'páska na suchý zip, rychlé nastavení', 'běžecké a dětské kšiltovky'],
              ['Elastická bez zapínání', 'celá kšiltovka je pružná', 'sportovní modely z funkční tkaniny']]) +
          '<p>Uzavřená kšiltovka vypadá nejčistěji, protože vzadu nemá žádný otvor ani přezku. Musí ale přesně sedět. Snapback a strapback odpustí nepřesný odhad velikosti a dají se půjčit i někomu dalšímu. Stretch fit je kompromis: zezadu je zavřený, a přitom pokryje rozpětí asi dvou velikostí.</p>'
          '<h2>New Era: co znamenají čísla 59FIFTY, 9FORTY a 39THIRTY</h2>'
          '<p>New Era označuje své střihy čísly a pod nimi se kšiltovky také nejčastěji hledají. <strong>59FIFTY</strong> je klasická uzavřená kšiltovka s vysokým zpevněným čelem a rovným kšiltem. Prodává se v kloboukových velikostech, například 7 1/8 nebo 7 3/8, a právě tento střih nosí na hřišti hráči baseballové ligy MLB. Kdo ho kupuje poprvé, musí si změřit hlavu, protože bez nastavení se nic nedá doladit.</p>'
          '<p><strong>9FORTY</strong> má nižší korunu a předem zahnutý kšilt. Vzadu je nastavitelná, podle provedení páskem se sponou nebo přezkou, a obvykle se prodává v jedné univerzální velikosti. Pro většinu lidí je to nejjednodušší volba bez měření. <strong>39THIRTY</strong> je zavřená zezadu, ale pružná, s rovněž zahnutým kšiltem, a velikosti se značí rozpětím S–M, M–L nebo L–XL. <strong>9FIFTY</strong> kombinuje vysoké čelo a rovný kšilt modelu 59FIFTY se snapbackovou přezkou. Vedle nich existuje měkká, nevyztužená 9TWENTY z prané bavlny, střihem blízká oblíbeným „dad caps“.</p>'
          '<p>Na kšiltu nových kusů New Era bývá zlatá nebo stříbrná nálepka s velikostí. Někdo ji strhne hned, jiný ji nechává jako součást stylu. Je to čistě otázka vkusu, na funkci nemá vliv.</p>'
          '<h2>Jak změřit velikost hlavy</h2>'
          '<p>Krejčovský metr veďte kolem hlavy zhruba centimetr nad obočím a nad ušima, tedy tam, kde bude sedět spodní okraj kšiltovky. Měřte volně, bez utahování, a výsledek zaokrouhlete nahoru. Americké kloboukové velikosti vycházejí z průměru hlavy v palcích, takže se k nim dá obvod přepočítat. Přesný převod má každý výrobce ve vlastní tabulce, orientačně platí:</p>'
          + T(['Obvod hlavy', 'Klobouková velikost', 'Rozpětí stretch fit'], [
              ['kolem 55 cm', '6 7/8', 'S–M'],
              ['kolem 56 cm', '7', 'S–M'],
              ['kolem 57 cm', '7 1/8', 'S–M / M–L'],
              ['kolem 58 cm', '7 1/4', 'M–L'],
              ['kolem 59 cm', '7 3/8', 'M–L / L–XL'],
              ['kolem 60 cm', '7 1/2', 'L–XL'],
              ['kolem 61 cm', '7 5/8', 'L–XL']]) +
          '<p>Pokud jste přesně na hranici dvou velikostí, u uzavřené kšiltovky sáhněte spíš po větší. Těsná fitted kšiltovka se nepovolí a po hodině začne tlačit na spáncích. U stretch fit se naopak menší rozpětí lépe drží. Dětské a juniorské kšiltovky mívají vlastní velikosti nebo jsou nastavitelné, aby vydržely víc než jednu sezónu.</p>'
          '<h2>Materiály a konstrukce</h2>'
          '<p>Nejčastějším materiálem je bavlněný kepr, pevná a příjemná tkanina, která snese i častější nošení. Strukturované modely mají čelní díly vyztužené pevnou vložkou, takže drží tvar i na věšáku. Polyester se objevuje u sportovních kšiltovek i u části lifestylových řad, rychleji schne a méně bledne. Zimní varianty bývají z vlny, manšestru nebo s fleecovou podšívkou a některé mají sklopné klapky na uši.</p>'
          '<p>Trucker má vpředu pěnový nebo textilní panel a zbytek tvoří plastová síťovina, která dobře větrá. Proto ho nosí řidiči, rybáři a kdokoli tráví den venku v horku. Běžecké kšiltovky jsou z tenké funkční tkaniny, často s perforací, měkkým kšiltem, který se dá složit do kapsy, a reflexními prvky. Uvnitř všech kšiltovek je potní páska, kterou se vyplatí čas od času vyprat.</p>'
          '<h2>Rovný, nebo zahnutý kšilt</h2>'
          '<p>Rovný kšilt patří ke streetwearu, k modelům 59FIFTY a 9FIFTY, a dobře vynikne na něm výšivka nebo spodní barva. Zahnutý kšilt lépe stíní oči ze stran a na sport bývá praktičtější. Mírný oblouk si můžete vytvarovat rukama, kšilt ale nelamte do ostrého úhlu. Uvnitř je plastová výztuha, která při prudkém ohnutí praskne, a kšiltovka pak už nikdy nebude vypadat jako nová.</p>'
          '<h2>Kšiltovka na sport a na slunce</h2>'
          '<p>Na běh a cyklistiku bez helmy volte lehký model, který rychle schne a vzadu má pružný nebo nastavitelný pásek. Ženy ocení otvor nad přezkou, kterým se provlékne culík. Pro turistiku se prodávají kšiltovky se zadní plachetkou přes krk, případně stačí kombinace kšiltovky a šátku z kategorie <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a>. Golfisté najdou kšiltovky a kšilty bez koruny mezi <a href="/golfove-obleceni-a-obuv/">golfovým oblečením</a>.</p>'
          '<p>Kšiltovka chrání čelo, oči a část obličeje, uši a krk ale nechává na slunci. V létě proto nepřestávejte používat opalovací krém a do hor nebo k vodě přidejte brýle s UV filtrem. Tmavá kšiltovka se na přímém slunci víc zahřeje, světlá odráží víc světla, a proto se v horku nosí příjemněji.</p>'
          '<h2>Licencované kšiltovky NFL, NHL a MLB</h2>'
          '<p>Velká část nabídky jsou kšiltovky s logy amerických týmů. Licencovaný kus nese oficiální logo ligy a týmu a výrobce za jeho použití platí. U modelů New Era a \'47 najdete týmy baseballu, amerického fotbalu i hokeje, často v několika barevných verzích, se sezonními motivy nebo ke draftu. Při výběru dárku zkontrolujte nejen tým, ale i to, zda jde o fitted, nebo nastavitelný model. Hokejoví fanoušci najdou další předměty v kategorii <a href="/hokejove-suveniry-a-karty/">hokejové suvenýry a karty</a>, týmová trička a dresy v kategorii <a href="/dresy/">dresy</a>.</p>'
          '<h2>Jak kšiltovku čistit</h2>'
          '<ul><li><strong>Strukturované kšiltovky do pračky nepatří.</strong> Pračka zdeformuje vyztužené čelo a kšilt, i když ji obchod neoznačuje jako zakázanou.</li>'
          '<li><strong>Ruční praní:</strong> vlažná voda, trocha jemného prostředku a měkký kartáček. Potní pásku vydrhněte zvlášť, právě tam se drží skvrny.</li>'
          '<li><strong>Sušení:</strong> volně na vzduchu, nejlépe navlečené na misce nebo míči, aby držely tvar. Radiátor ani sušička nejsou vhodné.</li>'
          '<li><strong>Nevyztužené bavlněné a sportovní modely</strong> mnohdy pračku snesou; řiďte se štítkem uvnitř.</li>'
          '<li><strong>Skladování:</strong> kšiltovky ukládejte na sebe, ne zmačkané v batohu, a sbírkové kusy mimo přímé slunce, které barvy vybledí.</li></ul>'
          '<h2>Dětské kšiltovky</h2>'
          '<p>Dětská hlava roste rychle, proto se pro děti hodí hlavně nastavitelné kšiltovky na suchý zip nebo přezku. Uzavřené modely se prodávají v dětských a juniorských velikostech, dítě z nich ale může vyrůst během jediné sezóny. Na léto u vody a na horách volte světlou barvu, lehký materiál a ideálně plachetku přes krk, protože dětská kůže se na slunci spálí rychleji. U malých dětí zkontrolujte, zda kšiltovka nemá drobné ozdoby, které by šly utrhnout a vložit do pusy.</p>'
          '<h2>Kšiltovka jako dárek</h2>'
          '<p>Kšiltovka patří k častým dárkům pro fanoušky, protože se dá vybrat podle oblíbeného týmu. Bez znalosti velikosti je nejbezpečnější nastavitelný model typu 9FORTY nebo snapback. Uzavřenou 59FIFTY kupujte jen tehdy, když víte, jakou velikost obdarovaný nosí, nebo když vám obchod velikost vymění. Pomůže i nenápadný pohled do šatníku: velikost bývá vyšitá nebo natištěná na štítku uvnitř kšiltovky, kterou dotyčný už nosí. Před objednávkou si zkontrolujte lhůtu pro vrácení, protože běží od doručení, ne od předání dárku.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Objednání uzavřené kšiltovky bez změření hlavy.</li>'
          '<li>Záměna 9FORTY a 59FIFTY, které mají jiný tvar i velikostní systém.</li>'
          '<li>Volba těžké bavlněné kšiltovky na běh v horku.</li>'
          '<li>Spoléhání na kšilt jako jedinou ochranu před sluncem.</li>'
          '<li>Praní vyztužené kšiltovky v pračce.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>U každé kšiltovky vidíte nabídky různých obchodů vedle sebe a podle toho si vyberete, kde je váš tým a velikost skladem. Licencované modely se často vyrábějí jen v omezené sérii a po vyprodání se nemusí vrátit. Porovnejte proto rovnou i dopravu a podmínky vrácení, objednávku dokončíte v e-shopu. Na zimu vám v nadřazené kategorii poslouží <a href="/cepice-a-celenky/">čepice a čelenky</a>, pro lyžaře jsou určeny <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi 59FIFTY a 9FORTY?', '59FIFTY je uzavřená kšiltovka s vysokým čelem, rovným kšiltem a přesnou velikostí. 9FORTY má nižší korunu, zahnutý kšilt a vzadu se nastavuje, takže se obvykle prodává v jedné univerzální velikosti.'),
        ('Co znamená snapback?', 'Kšiltovka s plastovou přezkou vzadu, která se zacvakává do řady otvorů. Obvod se dá nastavit v širokém rozpětí, proto ji pohodlně nosí většina lidí.'),
        ('Jak zjistím velikost kšiltovky?', 'Změřte obvod hlavy krejčovským metrem asi centimetr nad obočím a nad ušima. Výsledek porovnejte s tabulkou výrobce, například 7 1/4 odpovídá obvodu kolem 58 cm.'),
        ('Co je 39THIRTY?', 'Pružná kšiltovka New Era zavřená zezadu, se zahnutým kšiltem. Velikosti se uvádějí v rozpětí S–M, M–L a L–XL a každé pokryje přibližně dvě kloboukové velikosti.'),
        ('Mohu kšiltovku vyprat v pračce?', 'Vyztužené kšiltovky raději ne, pračka deformuje čelo i kšilt. Perte je ručně ve vlažné vodě a nechte uschnout na vzduchu. Měkké sportovní modely se řídí štítkem.'),
        ('Čím se liší trucker od běžné kšiltovky?', 'Trucker má vpředu pevný panel a zbytek tvoří síťovina, která dobře větrá. Obvykle se zapíná přezkou typu snapback.'),
        ('Jakou kšiltovku koupit jako dárek, když neznám velikost?', 'Nastavitelnou, například 9FORTY, snapback nebo model s páskem. Uzavřenou 59FIFTY volte jen se znalostí velikosti nebo s možností výměny v obchodě.'),
        ('Je kšiltovka dostatečná ochrana před sluncem?', 'Chrání čelo a oči, uši a krk ale ne. V létě ji doplňte opalovacím krémem, šátkem na krk a brýlemi s UV filtrem.'),
    ])

# ------------------------------------------------------------------ teplakove-soupravy
NEW['teplakove-soupravy'] = dict(long=True,
    title='Teplákové soupravy: pánské, dámské i dětské, Nike a Adidas',
    desc='Teplákové soupravy pánské, dámské i dětské: bavlněné, šusťákové i tréninkové. Materiály, střihy a velikosti. Porovnejte nabídky českých e-shopů.',
    intro='<p><strong>Tepláková souprava</strong> spojuje mikinu nebo bundu s tepláky ze stejného materiálu a ve stejném stylu. Nosí se na trénink a cestu na zápas, domů na gauč i do města, kde dnes nikoho nepřekvapí. Rozdíl mezi soupravami je hlavně v materiálu: hřejivá počesaná bavlna, hladká polyesterová pletenina, ze které se šijí tréninkové soupravy klubů, nebo lehký šusťák proti větru. Podle toho se liší i to, kam se který komplet hodí.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů a nákup dokončíte v e-shopu, jehož nabídka vás zaujme. Najdete tu pánské, dámské i dětské soupravy od ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('guess', 'Guess')) + ' nebo Leone 1947. Nadřazenou kategorií jsou <a href="/soupravy/">soupravy</a>, samostatné kusy najdete mezi <a href="/teplaky/">tepláky</a> a <a href="/mikiny/">mikinami</a>.</p>',
    guide='<h2>Jaké teplákové soupravy existují</h2>'
          '<p>Slovo souprava zahrnuje několik dost odlišných věcí. Před nákupem si ujasněte, zda hledáte něco hřejivého na doma, komplet na trénink, nebo oblečení na cesty, které bude vypadat upraveně.</p>'
          + T(['Typ', 'Materiál', 'Kam se hodí'], [
              ['Bavlněná (fleece)', 'bavlna nebo bavlna s polyesterem, uvnitř počesaná', 'doma, na procházku, chladnější dny'],
              ['Z froté pleteniny', 'bavlna s nepočesanými smyčkami na rubu', 'jaro a podzim, celoroční nošení'],
              ['Tréninková (tricot)', 'hladká polyesterová pletenina', 'trénink, cesta na zápas, týmové oblečení'],
              ['Šusťáková', 'lehká tkanina z polyesteru nebo polyamidu, často s podšívkou', 'vítr, rozcvička venku, retro styl'],
              ['Velurová a semišová', 'jemný vlas na povrchu', 'volný čas, móda'],
              ['Funkční', 'pružné syntetické materiály s elastanem', 'běh v chladu, posilovna, cestování']]) +
          '<h2>Bavlna, polyester a jejich směsi</h2>'
          '<p>Bavlněná souprava je příjemná na kůži, dobře saje vlhkost a nehřeje „umělým“ teplem. Počesaný rub, kterému se v obchodech říká fleece, hřeje víc a hodí se do chladných dnů. Nevýhodou čisté bavlny je, že při pocení nasákne a pomalu schne, takže na intenzivní trénink není ideální. Většina pánských i dámských souprav proto kombinuje bavlnu s polyesterem. Směs se méně mačká, méně se sráží a rychleji schne, ale časem na ní mohou vznikat žmolky, hlavně v místech, kde se tře o tašku nebo bok.</p>'
          '<p>Hladká polyesterová pletenina je typická pro tréninkové soupravy fotbalových a dalších týmů, například řady Adidas Tiro nebo Nike Academy. Je lehká, neprofoukne se tak snadno jako bavlna, rychle schne a vydrží časté praní. Na první dotek je chladnější a méně hřeje, proto se pod ni v zimě obléká funkční tričko nebo termoprádlo.</p>'
          '<h2>Střihy tepláků a mikin</h2>'
          '<p>U kalhot je hlavní rozdíl ve spodním lemu. Jogger má zúženou nohavici a pružný manžetový lem, takže tepláky nestojí na botách a dobře vypadají s teniskami. Rovný střih s otevřeným lemem padá volně a hodí se k vyšší obuvi. Tréninkové tepláky mívají u kotníků zipy, aby šly přetáhnout přes kopačky nebo boty. Pas bývá pružný, se šňůrkou, a kapsy na zip ocení každý, kdo s sebou nosí klíče a telefon.</p>'
          '<p>Horní díl je buď mikina na zip, mikina přes hlavu s kapucí, nebo bunda se stojáčkem. Varianta na zip se lépe svléká a obléká, třeba při rozcvičce, a dá se nosit rozepnutá. Mikina přes hlavu bývá teplejší a nemá zip, který by se mohl porouchat. Střih se uvádí jako regular, slim nebo oversize; dnešní dámské kolekce často pracují s volnějšími, kratšími mikinami a širšími kalhotami.</p>'
          '<h2>Pánské teplákové soupravy</h2>'
          '<p>Pánské soupravy se nejčastěji kupují jako kombinace mikiny na zip a joggerů. Nike Club Fleece nebo Adidas Essentials se třemi pruhy patří mezi klasiku, která nevyjde z módy. Kdo chce soupravu i do posilovny, ať sáhne po pružné směsi s elastanem nebo po polyesterové pletenině, která neomezuje v dřepu. Pro sport v zimě může být praktičtější samostatná bunda a kalhoty, které se dají kombinovat. Velikosti pánských souprav se uvádějí v mezinárodních značkách S až XXL; u amerických značek sedí obvykle volněji než u evropských.</p>'
          '<h2>Dámské teplákové soupravy</h2>'
          '<p>Dámské soupravy mají užší ramena, kratší rukávy a pas posazený výš. Vedle sportovních kompletů je tu velká skupina souprav na volný čas, v pastelových barvách, ze sametu nebo s krátkou mikinou a širokými kalhotami. Takové soupravy nosí ženy na cesty, na doma i do města s bundou a teniskami. Na cvičení je výhodnější kratší mikina se zipem nebo souprava s legínami; přímo tréninkové kousky najdete mezi <a href="/leginy/">legínami</a> a <a href="/funkcni-mikiny/">funkčními mikinami</a>.</p>'
          '<h2>Dětské teplákové soupravy</h2>'
          '<p>Dětské soupravy se značí podle výšky postavy v centimetrech, například 128, 140 nebo 152, případně podle věku. Dítě poroste, proto se vyplatí rezerva jedné velikosti, ne však víc; příliš dlouhé nohavice se zašlapávají a dítě v nich zakopává. Na dětské soupravě oceníte pevnější kolena, pružný pas bez tvrdých knoflíků a materiál, který snese praní na vyšší teplotu. Šňůrky v kapuci u menších dětí mohou být nebezpečné, proto u nejmenších volte modely bez nich. Do školky a na hřiště jsou vhodnější tmavší barvy a materiál, který se nežmolkuje.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<ul><li><strong>Délka nohavic:</strong> u joggerů má manžeta končit nad kotníkem, u rovného střihu lem jemně dosedá na botu.</li>'
          '<li><strong>Rukávy:</strong> mají sahat k zápěstí i po zvednutí paží, jinak se při každém protažení vyhrnou.</li>'
          '<li><strong>Velikostní tabulka:</strong> značky se liší, proto porovnejte obvod hrudníku a pasu, ne jen písmeno.</li>'
          '<li><strong>Bavlna se po prvním praní trochu srazí:</strong> u čisté bavlny počítejte s malou rezervou.</li>'
          '<li><strong>Oversize střih:</strong> je záměrně volnější, nekupujte ho o číslo větší.</li></ul>'
          '<h2>Péče a praní</h2>'
          '<p>Soupravu perte naruby, se zapnutými zipy a odděleně od ručníků a věcí, ze kterých se uvolňují vlákna. Většina výrobců uvádí praní na 30 nebo 40 °C. Aviváž u bavlny nevadí, u polyesterových a funkčních souprav ale ucpává vlákna a zhoršuje odvod potu, takže ji tam vynechte. Sušička zkracuje životnost pružných lemů a u bavlny podporuje srážení. Potisk a nažehlená loga nežehlete přímo, pouze z rubu. Žmolky se dají odstranit odžmolkovačem, nejlépe dřív, než se jich nahromadí hodně.</p>'
          '<h2>Šusťákové soupravy a retro styl</h2>'
          '<p>Šusťáková souprava dostala jméno podle zvuku, který lehká tkanina při pohybu vydává. Svrchní látka z polyesteru nebo polyamidu dobře zastaví vítr i krátkou přeháňku, uvnitř bývá síťovinová podšívka, která drží látku od těla. V devadesátých letech ji nosil skoro každý na hřišti i na sídlišti a dnes se vrací v barevných retro kolekcích. Pro sport je praktická na rozcvičku venku nebo jako svrchní vrstva na kolo. Nepromokavá ale není a při delším dešti promokne. Přes bavlněnou mikinu se nosí pohodlně, protože po ní podšívka dobře klouže.</p>'
          '<h2>Soupravy pro týmy a kluby</h2>'
          '<p>Sportovní kluby obvykle objednávají soupravy z polyesterové pleteniny, protože vydrží časté praní a dobře se na ně tiskne. Výrobci mají týmové řady, které zůstávají v nabídce několik sezón, takže se dají později dokoupit pro nové hráče. Při nákupu pro celý tým ověřte, zda je model k mání v dětských i dospělých velikostech a zda se prodávají samostatně horní a spodní díly. Potisk jmen a čísel zajišťují specializované dílny nebo některé obchody, proto počítejte s delší dobou dodání.</p>'
          '<h2>Souprava na cestování</h2>'
          '<p>Na dlouhou cestu autem, vlakem nebo letadlem je tepláková souprava pohodlná, protože nic neškrtí v pase ani v kolenou. Hodí se materiál, který se nemačká, například směs bavlny s polyesterem nebo pružná funkční pletenina. Mikina na zip se snadno sundá, když se v kupé oteplí. Kapsy na zip udrží doklady a telefon, i když v sedadle usnete.</p>'
          '<h2>Kdy se souprava nehodí</h2>'
          '<p>Tepláková souprava není zimní oblečení na hory. Bavlna v mrazu a vlhku rychle ztrácí tepelné vlastnosti a nepromokne jen do prvního deště. Na turistiku, běžky nebo lyže proto patří vrstvené oblečení: <a href="/termopradlo/">termoprádlo</a>, fleece a nepromokavá svrchní vrstva. Souprava naopak skvěle poslouží po tréninku, cestou autobusem na zápas nebo při regeneraci, kdy se tělo nemá rychle zchladit.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr bavlněné soupravy na intenzivní trénink, při kterém se hodně potíte.</li>'
          '<li>Koupě dětské soupravy o dvě a víc velikostí větší.</li>'
          '<li>Spoléhání na písmeno velikosti bez kontroly tabulky výrobce.</li>'
          '<li>Praní funkčních souprav s aviváží.</li>'
          '<li>Přehlédnutí, že souprava se prodává jen jako horní díl nebo jen kalhoty.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte, které obchody mají soupravu v nabídce a v jakých velikostech, a objednávku pak dokončíte v e-shopu. Některé obchody prodávají soupravu jako jeden kus, jiné nabízejí horní a spodní díl zvlášť a k nim můžete dokoupit chybějící velikost. Před koupí si proto přečtěte popis. Samostatné kalhoty najdete v kategorii <a href="/teplaky/">tepláky</a>, sportovní kraťasy na léto v kategorii <a href="/sportovni-kratasy/">sportovní kraťasy</a>.</p>',
    faq=[
        ('Z jakého materiálu vybrat teplákovou soupravu?', 'Na doma a volný čas bavlnu nebo bavlnu s polyesterem, na trénink hladkou polyesterovou pleteninu nebo pružnou funkční směs. Šusťák se hodí proti větru.'),
        ('Co znamená fleece u teplákové soupravy?', 'Pleteninu s počesaným vnitřkem, který je měkký a hřeje víc. Nejčastěji jde o směs bavlny a polyesteru.'),
        ('Jakou velikost zvolit pro dítě?', 'Dětské soupravy se značí podle výšky v centimetrech. Rezerva jedné velikosti je rozumná, větší ne, protože dlouhé nohavice se zašlapávají.'),
        ('Srazí se bavlněná souprava po praní?', 'Čistá bavlna se po prvním praní může mírně srazit. Směsi s polyesterem se srážejí méně. Perte podle štítku a nepoužívejte sušičku na vysokou teplotu.'),
        ('Jaký je rozdíl mezi joggery a rovnými tepláky?', 'Joggery mají zúženou nohavici s pružnou manžetou u kotníku. Rovné tepláky mají otevřený lem a volně padají na botu.'),
        ('Mohu teplákovou soupravu použít na hory?', 'Jako vrstvu na cestu nebo po návratu ano, na samotnou turistiku či lyže ne. Bavlna ve vlhku a mrazu přestává hřát a nepromokne.'),
        ('Co je šusťáková souprava?', 'Souprava z lehké tkaniny z polyesteru nebo polyamidu, která při pohybu šustí. Chrání před větrem a krátkou přeháňkou, nepromokavá ale není.'),
        ('Jsou soupravy Nike a Adidas velikostně stejné?', 'Ne vždy. Každá značka má vlastní tabulku a střihy se liší i mezi řadami. Porovnejte obvod hrudníku a pasu s tabulkou konkrétního modelu.'),
        ('Proč se na soupravě dělají žmolky?', 'Vznikají třením vláken, hlavně u směsí bavlny s polyesterem. Pomáhá praní naruby, oddělení od ručníků a odžmolkovač.'),
    ])

# ------------------------------------------------------------------ crop-topy
NEW['crop-topy'] = dict(long=True,
    title='Crop topy: sportovní, na jógu i do fitka, s podprsenkou',
    desc='Crop topy na jógu, fitness i běh: s integrovanou podprsenkou, bezešvé, merino i bavlna. Jak vybrat oporu a velikost, nabídky českých e-shopů.',
    intro='<p><strong>Crop top</strong> je zkrácený top nebo tričko, které končí nad pasem nebo v jeho úrovni a nechává odhalený kus břicha. Ve sportu se zabydlel hlavně díky józe, fitness a tanci: nic se nevyhrnuje, nepřekáží v předklonu a s legínami s vysokým pasem tvoří pohodlný celek. Mezi crop topy ale najdete jak lehké tričko na trénink, tak top s vlastní podprsenkou, bezešvý pružný model nebo volný oversize kousek do města.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů, nákup proběhne přímo v obchodě. Mezi značkami jsou ' + B(('under-armour', 'Under Armour'), ('adidas', 'Adidas'), ('icebreaker', 'Icebreaker'), ('craft', 'Craft'), ('gap', 'Gap')) + ' nebo Nebbia. Crop topy jsou součástí kategorie <a href="/tilka/">tílka</a>; když hledáte hlavně oporu prsou, otevřete rovnou <a href="/sportovni-podprsenky/">sportovní podprsenky</a>.</p>',
    guide='<h2>Crop top, nebo sportovní podprsenka?</h2>'
          '<p>Hranice mezi oběma kategoriemi je tenká a obchody je často míchají. Sportovní podprsenka je postavená na oporu: má pevný pružný lem pod prsy, tvarované nebo vyjímatelné vycpávky a často nastavitelná ramínka. Crop top je především oblečení. Může mít vestavěnou lehkou podprsenku, ale nemusí, a i tak mívá menší oporu. Pro jógu, pilates, strečink a chůzi to obvykle stačí. Na běh, skákání nebo aerobik, zvlášť u větších velikostí, se vyplatí podprsenka s vyšší oporou a crop top přes ni.</p>'
          + T(['Druh crop topu', 'Opora', 'Vhodné aktivity'], [
              ['Crop tričko z bavlny nebo funkční tkaniny', 'žádná, nosí se přes podprsenku', 'posilovna, volný čas, tanec'],
              ['Crop top s integrovanou podprsenkou', 'lehká až střední', 'jóga, pilates, chůze, lehký trénink'],
              ['Bezešvý pružný crop top', 'lehká, tvaruje přilnavostí', 'jóga, fitness, každodenní nošení'],
              ['Crop top s dlouhým rukávem', 'podle střihu, spíš lehká', 'chladnější studio, běh na jaře'],
              ['Volný oversize crop', 'žádná', 'přes sportovní podprsenku, do města'],
              ['Merino crop top', 'lehká', 'outdoor, cestování, vrstvení']]) +
          '<h2>Jak poznat míru opory</h2>'
          '<p>Výrobci sportovního prádla dělí oporu obvykle na lehkou, střední a vysokou. U crop topů se nejčastěji setkáte s lehkou oporou, výjimečně se střední. Údaj bývá v popisu produktu, někdy jako ikona s jednou až třemi tečkami. Opora závisí na pevnosti spodního lemu, na tom, zda top prsy stlačuje k tělu, nebo je drží každé zvlášť v košíčku, a také na šířce ramínek. Pokud v popisu nic není, počítejte s lehkou oporou.</p>'
          '<p>Vyjímatelné vycpávky jsou praktické, protože si sami zvolíte, zda je chcete. Po praní se ale rády zmačkají nebo posunou, proto je před pračkou vyndejte a sušte zvlášť. U topů bez vycpávek pomáhá vícevrstvá přední část.</p>'
          '<h2>Materiály</h2>'
          '<p>Většina sportovních crop topů je z polyamidu nebo polyesteru s elastanem. Tyto směsi jsou pružné, drží tvar a rychle schnou, takže se hodí i na pocení v posilovně. Bezešvé topy se pletou na kruhových strojích do jednoho kusu, takže nedřou a dobře sedí i pod volnějším tričkem. Bavlněné crop topy jsou příjemné na doma a do města, při intenzivním tréninku ale nasáknou potem.</p>'
          '<p>Merino vlna se uplatní u topů na hory a na cesty. Izolovat umí i vlhká, příjemně se nosí ve větším rozmezí teplot a pomaleji než syntetika chytá pach, takže vydrží víc nošení mezi praními. Icebreaker nebo Craft ji obvykle kombinují s nylonem nebo elastanem kvůli pevnosti. Merino je jemnější materiál, proto vyžaduje šetrné praní a nesnáší sušičku. Další kousky z této vlny najdete v kategorii <a href="/merino-tricka/">merino trička</a>.</p>'
          '<h2>Délka a střih</h2>'
          '<ul><li><strong>Krátký crop</strong> končí těsně pod prsy a hodí se k legínám s vysokým pasem.</li>'
          '<li><strong>Delší crop</strong> sahá k pupíku nebo těsně nad pas a zakryje víc i při normálních kalhotách.</li>'
          '<li><strong>Racerback</strong> má ramínka spojená mezi lopatkami a dává pažím volnost, oblíbený je v józe a na tenisu.</li>'
          '<li><strong>Křížená ramínka</strong> vypadají zajímavě a lépe drží na místě, nasazují se ale přes hlavu obtížněji.</li>'
          '<li><strong>Kulatý výstřih nebo vyšší límec</strong> zakryje víc a v předklonu nic neodhaluje.</li>'
          '<li><strong>Dlouhý rukáv</strong> se hodí do chladnějšího sálu nebo pod vestu na běh.</li></ul>'
          '<h2>Velikost a sezení</h2>'
          '<p>Crop top má sedět těsně, ale nesmí zařezávat pod prsy ani na ramenou. Spodní lem nemá při pohybu rukou nahoru vyjíždět přes prsa. Pokud se zvedá, je top buď velký, nebo jeho lem není dost pevný. Velikosti se uvádějí v mezinárodních značkách XS až XL, některé značky nabízejí i velikosti podle obvodu hrudníku pod prsy. Velikostní tabulka konkrétní značky je vždy přesnější než písmeno. Při nákupu na internetu si zkontrolujte, zda obchod umožní vrácení, i když je top zkoušený; prádlo bývá z vrácení někdy vyloučené, jakmile se poruší hygienická ochrana.</p>'
          '<h2>Kombinace s dalším oblečením</h2>'
          '<p>Crop top nejlépe funguje s legínami nebo šortkami s vysokým pasem, které zakryjí část odhaleného břicha a zároveň drží celé oblečení na místě. Na jógu a pilates se přes něj nic dalšího nenosí. Ve fitku se hodí volné tričko, které můžete sundat po rozcvičce. Na běh ve městě, na kolo nebo do hor s ním počítejte jako s první vrstvou pod mikinou nebo bundou. Legíny, šortky i lehké mikiny najdete v kategoriích <a href="/leginy/">legíny</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/funkcni-tricka/">funkční trička</a>.</p>'
          '<h2>Crop top na jógu, pilates a tanec</h2>'
          '<p>V józe se tělo často ocitá hlavou dolů, v předklonu nebo v záklonu, a delší tričko přitom sjíždí k bradě. Crop top tenhle problém nemá, a proto ho cvičitelky i cvičenky nosí tak rády. Pro jógu je důležité, aby měl hladké švy na zádech, protože se na nich leží, a aby ramínka nesjížděla v pozicích s rukama nad hlavou. Na pilates se hodí top s vyšším výstřihem, který při cvicích na podložce nic neodhalí. Tanečnice ocení pružné bezešvé modely, které kopírují pohyb a nikde nepřekážejí.</p>'
          '<h2>Crop top na běh a do fitka</h2>'
          '<p>Při běhu se prsa pohybují nahoru a dolů i do stran, a čím jsou větší, tím víc potřebují oporu. Crop top s lehkou oporou proto obvykle stačí jen na krátký a pomalý běh. Na delší trať je rozumnější nosit ho přes sportovní podprsenku, nebo zvolit model, který výrobce označuje jako střední oporu. V posilovně je situace jednodušší, protože při dřepech a mrtvém tahu se tělo tolik nehoupe. Hodí se tkanina, která odvádí pot a rychle schne, a hladký zadní díl, který nedře o lavici.</p>'
          '<h2>Barvy a průsvitnost</h2>'
          '<p>Světlé barvy, zvlášť bílá a béžová, mohou po navlhnutí prosvítat. Pokud chodíte cvičit do skupiny, vyzkoušejte top doma před zrcadlem v ostrém světle. Tmavé a vzorované topy lépe skryjí propocená místa i skvrny od deodorantu. Neonové barvy jsou vidět na běhu za šera, reflexní prvky ale nenahradí.</p>'
          '<h2>Pro koho je crop top</h2>'
          '<p>Crop top není jen pro štíhlé tanečnice. Nosí ho ženy všech postav, kterým vyhovuje, že nic nepřekáží v pohybu a nevyhrnuje se při cvicích hlavou dolů. Kdo nechce ukazovat břicho, zvolí delší crop a kalhoty s vyšším pasem, které odhalí jen pár centimetrů. Větší prsa potřebují pevnější oporu, takže v takovém případě je lepší nosit crop top jako svrchní vrstvu přes podprsenku se střední nebo vysokou oporou. Dívky v pubertě často začínají právě s crop topem, protože je méně svazuje než klasická podprsenka.</p>'
          '<h2>Péče</h2>'
          '<p>Sportovní crop topy perte na 30 °C, naruby a ideálně v pracím sáčku, aby se nezachytily o zipy jiných kusů. Aviváž vynechte, protože usazená vrstva zhoršuje odvod potu a podporuje zápach. Sušička škodí elastanu, který se teplem rychleji unaví a top se vytahá. Sušte volně, mimo radiátor a přímé slunce. Propocený top neházejte zmačkaný do koše na několik dní; zápach se pak drží i po vyprání. Když se zápach usadí, pomůže namočení ve vodě s octem nebo prostředek na sportovní oblečení.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Spoléhání na crop top s lehkou oporou při běhu a skákání.</li>'
          '<li>Výběr bavlněného topu na intenzivní trénink.</li>'
          '<li>Koupě velikosti, ve které se spodní lem zvedá nebo zařezává.</li>'
          '<li>Praní s aviváží a sušení v sušičce.</li>'
          '<li>Přehlédnutí, že vycpávky nejdou vyjmout, když je nechcete.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>U každého crop topu vidíte nabídky obchodů vedle sebe a zjistíte, kde mají právě vaši velikost a barvu. Porovnejte i dopravu a podmínky vrácení, protože u prádla se mezi obchody liší. Samotná objednávka proběhne v e-shopu. K topu si můžete rovnou vybrat i podložku a doplňky z kategorie <a href="/joga-a-podlozky/">jóga a podložky</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi crop topem a sportovní podprsenkou?', 'Sportovní podprsenka je postavená na oporu prsou. Crop top je oblečení, které může mít lehkou vestavěnou podprsenku, ale obvykle drží méně. Na náročné aktivity je lepší podprsenka.'),
        ('Mohu v crop topu běhat?', 'Při menších prsou a lehkém běhu to může stačit. Na delší běh a skákání se doporučuje sportovní podprsenka se střední nebo vysokou oporou, případně crop top přes ni.'),
        ('Z jakého materiálu vybrat crop top na jógu?', 'Z pružné směsi polyamidu nebo polyesteru s elastanem, případně bezešvý model. Dobře drží, rychle schne a v předklonu se neposouvá.'),
        ('Jak poznám míru opory?', 'Výrobci ji uvádějí v popisu jako lehkou, střední nebo vysokou. Když údaj chybí, počítejte s lehkou oporou.'),
        ('Proč mají crop topy vyjímatelné vycpávky?', 'Abyste si mohly zvolit tvar a krytí. Před praním je vyndejte, jinak se mohou zmačkat nebo posunout.'),
        ('Jak prát sportovní crop top?', 'Naruby na 30 °C, ideálně v pracím sáčku, bez aviváže a bez sušičky. Sušte volně mimo radiátor.'),
        ('S čím crop top kombinovat?', 'Nejlépe s legínami nebo šortkami s vysokým pasem. Ve fitku se přes něj hodí volné tričko, venku mikina nebo bunda.'),
        ('Hodí se crop top i pro plnoštíhlé ženy?', 'Ano, crop top nosí ženy všech postav. Při větších prsou je ale lepší brát ho jako svrchní vrstvu přes podprsenku se střední nebo vysokou oporou.'),
        ('Proč je bílý crop top po tréninku průsvitný?', 'Světlé tenké tkaniny po navlhnutí prosvítají. Vyzkoušejte top předem v ostrém světle nebo zvolte tmavší barvu.'),
        ('Je merino crop top vhodný na sport?', 'Ano, hlavně na hory a na cesty. Merino izoluje i vlhké a pomaleji chytá pach. Je ale jemnější a potřebuje šetrné praní.'),
    ])

# ------------------------------------------------------------------ perove-bundy
NEW['perove-bundy'] = dict(long=True,
    title='Péřové bundy: dámské, pánské i ultralehké péřovky',
    desc='Péřové bundy dámské, pánské i ultralehké péřovky. Plnivost cuin, poměr peří 90/10, certifikace RDS a péče. Porovnejte nabídky českých e-shopů.',
    intro='<p><strong>Péřová bunda</strong> hřeje díky vzduchu zachycenému mezi jemnými chomáčky prachového peří. Žádná jiná izolace nenabízí tolik tepla při tak malé hmotnosti a zároveň se dá stlačit do malého vaku. Proto péřovky nosí horolezci, skialpinisté i lidé, kteří v zimě čekají na tramvaj. Péřové bundy se ale navzájem hodně liší kvalitou peří, množstvím náplně, konstrukcí komor i odolností svrchní látky, a tedy i tím, kam se hodí.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů, objednávku pak dokončíte v e-shopu. Mezi značkami jsou ' + B(('kilpi', 'Kilpi'), ('trespass', 'Trespass'), ('decathlon', 'Decathlon')) + ', Salewa, Superdry nebo Burton, a to v dámských, pánských i dětských střizích. Péřové bundy patří do kategorie <a href="/zimni-bundy/">zimní bundy</a>. Pro chladné noci pod stanem se hodí také <a href="/perove-spacaky/">péřové spacáky</a>, které fungují na stejném principu.</p>',
    guide='<h2>Jak péřová izolace funguje</h2>'
          '<p>Teplo neudržuje samotné peří, ale vzduch, který mezi sebou drží. Prachové peří, tedy jemné chomáčky bez pevného brku z podbřišku kachen a hus, vytvoří při rozložení velký objem. Čím víc se chomáčky po stlačení vrátí do původního tvaru, tím víc vzduchu zachytí a tím lépe bunda hřeje. Pevnější peří s brkem se do náplně přidává kvůli tvaru a ceně, samo ale hřeje méně a je těžší.</p>'
          '<h2>Plnivost: co znamená cuin</h2>'
          '<p>Kvalita peří se udává plnivostí, anglicky fill power, v jednotkách cuin. Číslo říká, jaký objem v kubických palcích zaujme jedna unce peří za stanovených podmínek. Vyšší plnivost znamená, že stejné teplo zajistí menší hmotnost náplně, a bunda je tedy lehčí a lépe se sbalí. Běžné městské péřovky mívají plnivost kolem 550 až 650 cuin, outdoorové modely 700 až 800 a nejlehčí expediční kusy ještě víc. Metodiky měření se v Evropě a v USA trochu liší, takže čísla od různých výrobců nejsou vždy přímo srovnatelná.</p>'
          '<p>Plnivost ale neříká, kolik peří v bundě je. Druhým údajem je hmotnost náplně v gramech. Bunda s plnivostí 800 cuin a malým množstvím peří může hřát méně než městská péřovka s 600 cuin a dvojnásobkem náplně. Kdo porovnává teplo, má sledovat obě čísla zároveň.</p>'
          '<h2>Poměr prachového peří a peří: 90/10, 80/20</h2>'
          '<p>Na štítku najdete poměr jako 90/10 nebo 80/20. První číslo udává podíl prachového peří, druhé podíl drobného peří s brkem. Náplň 90/10 je lehčí a lépe se vrací do tvaru, 80/20 je o něco těžší, ale pořád kvalitní. U levnějších bund se setkáte i s poměrem 70/30 nebo s náplní, kde peří převažuje, což znamená méně tepla na stejnou hmotnost a brky, které mohou prolézat látkou.</p>'
          + T(['Údaj na štítku', 'Co znamená', 'Na co se dívat'], [
              ['Plnivost (cuin, fill power)', 'objem, který zaujme unce peří', 'vyšší číslo = lehčí bunda pro stejné teplo'],
              ['Poměr 90/10, 80/20', 'podíl prachového peří a peří s brkem', 'čím víc prachového peří, tím lépe'],
              ['Hmotnost náplně', 'kolik gramů peří bunda obsahuje', 'spolu s plnivostí určuje teplo'],
              ['Husí, nebo kachní', 'původ peří', 'husí chomáčky bývají větší, rozhoduje ale plnivost'],
              ['RDS nebo jiný standard', 'certifikovaný původ peří', 'peří bez živého škubání a nucené vykrmování'],
              ['Hydrofobní úprava', 'peří ošetřené proti vlhkosti', 'pomaleji nasákne, ale vodu nevydrží']]) +
          '<h2>Certifikace RDS: odkud peří pochází</h2>'
          '<p>Peří je vedlejší produkt chovu kachen a hus na maso. Problémem bylo škubání peří z živých ptáků a nucené vykrmování. Standard Responsible Down Standard, zkráceně RDS, tyto praktiky zakazuje a ověřuje celý dodavatelský řetězec od farmy po hotový výrobek. Podobné vlastní standardy mají i někteří výrobci. Pokud je pro vás původ peří důležitý, hledejte v popisu RDS nebo jiný nezávisle ověřený certifikát. Recyklované peří z použitých výrobků je další možnost, která se objevuje u řady značek.</p>'
          '<h2>Peří a vlhko</h2>'
          '<p>Slabinou peří je voda. Mokré chomáčky se slepí, ztratí objem a přestanou hřát, a schnou pomalu. Péřová bunda proto není ideální do deště nebo na dlouhou fyzickou aktivitu, při které se hodně potíte. Hydrofobně upravené peří vydrží vlhko o něco lépe, nepromokavou bundu ale nenahradí. Svrchní látka bývá ošetřená vodoodpudivou úpravou DWR, která zvládne sníh a mrholení. Do deště přes péřovku oblékněte <a href="/nepromokave-bundy/">nepromokavou bundu</a> nebo zvolte syntetickou izolaci, která hřeje i navlhlá.</p>'
          '<h2>Konstrukce komor</h2>'
          '<p>Peří je rozdělené do komor, aby se neshromáždilo dole. U prošívané konstrukce je svrchní a vnitřní látka sešitá přímo k sobě. Je lehká a levnější na výrobu, v místech švů ale chybí izolace a táhne tam chlad. Komorová konstrukce má mezi oběma látkami tenké přepážky, takže náplň má všude stejnou výšku. Je teplejší, ale těžší a dražší, proto ji najdete hlavně u expedičních bund. Některé modely kombinují peří se syntetickou výplní v ramenou a na rukávech, kde se vlhko drží nejvíc.</p>'
          '<h2>Typy péřových bund</h2>'
          '<ul><li><strong>Ultralehká péřovka:</strong> tenká, často bez kapuce, sbalitelná do vlastní kapsy. Slouží jako zateplovací vrstva na túru, do batohu nebo pod zimní kabát.</li>'
          '<li><strong>Městská péřová bunda:</strong> delší střih, kapuce, často s kožíškem, pevnější svrchní látka. Hřeje při chůzi i při čekání.</li>'
          '<li><strong>Péřový kabát:</strong> sahá pod zadek nebo ke kolenům, kryje i stehna; podobné střihy najdete i v kategorii <a href="/kabaty-a-parky/">kabáty a parky</a>.</li>'
          '<li><strong>Outdoorová a skialpová péřovka:</strong> nízká hmotnost, kapuce pod helmu, odolnější látka v ramenou.</li>'
          '<li><strong>Péřová vesta:</strong> zahřeje trup a nechává volné paže, dobrá na přechodné období.</li>'
          '<li><strong>Lyžařská péřová bunda:</strong> se sněžným pásem a kapsou na skipas, k vidění například u Burtonu nebo Kilpi.</li></ul>'
          '<h2>Dámské a pánské péřové bundy</h2>'
          '<p>Dámské péřovky mají užší ramena, vypasovaný střih a často delší délku. Dámská péřová bunda do města se proto běžně prodává ve variantě ke kolenům, zatímco pánská bývá kratší, k bokům. U obou se vyplatí vyzkoušet, zda pohodlně zvednete ruce a zda se pod bundu vejde mikina. Péřovka má sedět spíš přiléhavě, protože každý zbytečný prostor uvnitř se musí zahřát. Zároveň ale nesmí být tak těsná, aby stlačovala náplň.</p>'
          '<h2>Dětské péřové bundy</h2>'
          '<p>Děti se ve sněhu válejí, kloužou po zadku a při běhání se potí, takže péřová bunda u nich dostává zabrat. Hodí se odolnější svrchní látka, prodloužený zadní díl a kapuce, kterou lze odepnout. Na hraní ve sněhu bývá praktičtější kombinace péřovky s nepromokavými kalhotami, případně syntetická zimní bunda, které nevadí ani mokré rukávy.</p>'
          '<h2>Péřovka, nebo syntetická izolace</h2>'
          '<p>Syntetické izolace, například PrimaLoft nebo vlastní výplně výrobců, napodobují strukturu peří z polyesterových vláken. Při stejném teple jsou těžší a hůř se sbalí, zato si ve vlhku udrží větší část izolační schopnosti a rychleji schnou. Také se snáz perou. Pro mokrou zimu v nížinách nebo pro aktivity s velkým pocením proto může být syntetika praktičtější. Peří vyhrává tam, kde rozhoduje hmotnost a objem v batohu, a v suchém mrazu.</p>'
          '<h2>Péřovka ve vrstvení</h2>'
          '<p>Při intenzivním pohybu se péřová bunda většinou nenosí, protože se v ní člověk rychle zpotí. Na túře ji vytáhnete z batohu na zastávce, na vrcholu nebo v táboře a obléknete ji přes funkční vrstvu, případně pod nepromokavou bundu, pokud fouká nebo sněží. Ve městě je to jinak: tam péřovka slouží jako hlavní zimní bunda, protože pohyb je pomalý a mezi vytápěnými místnostmi se jde jen krátce. Pod ni se hodí <a href="/termopradlo/">termoprádlo</a> nebo tenká mikina, ne silný svetr, který by náplň stlačil.</p>'
          '<h2>Péče o péřovou bundu</h2>'
          '<p>Péřovou bundu nepereme často. Když je to potřeba, použijte prostředek určený na peří a program pro jemné prádlo nebo péřové výrobky s nízkou teplotou, obvykle 30 °C, a několik máchání. Běžný prací prášek peří odmašťuje a snižuje jeho plnivost. Sušení je nejdůležitější část: v sušičce na nízkou teplotu s několika tenisovými nebo sušicími míčky, které chomáčky rozbijí, a dokud bunda není úplně suchá. Peří uvnitř schne i několik hodin a nedosušené začne zapáchat. Bez sušičky ji sušte rozloženou a pravidelně ji protřepávejte.</p>'
          '<p>Na léto ji nenechávejte stlačenou v malém vaku. Uložte ji volně zavěšenou nebo v prostorném obalu, aby si peří udrželo pružnost. Malou dírku zalepte opravnou páskou na nylon dřív, než se jí začne peří ztrácet. Vodoodpudivou úpravu svrchní látky obnoví prostředky z kategorie <a href="/impregnace/">impregnace</a>.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Porovnávání bund jen podle plnivosti, bez hmotnosti náplně.</li>'
          '<li>Výběr péřovky na celodenní pobyt v dešti.</li>'
          '<li>Příliš těsná bunda, ve které se náplň stlačí a přestane hřát.</li>'
          '<li>Praní běžným pracím práškem a nedostatečné sušení.</li>'
          '<li>Dlouhodobé skladování ve stlačeném stavu.</li></ul>'
          '<h2>Nákup přes Sporteku</h2>'
          '<p>Na kartě produktu vidíte nabídky více obchodů vedle sebe, takže snadno zjistíte, kde je vaše velikost a barva skladem. Objednávku dokončíte v e-shopu. Před nákupem si v popisu ověřte plnivost, poměr peří a hmotnost náplně; pokud údaje chybí, bývá to signál méně kvalitní náplně. Pro aktivní pohyb v zimě zvažte také <a href="/softshellove-bundy/">softshellové bundy</a>, které lépe dýchají, a na lyže <a href="/lyzarske-bundy/">lyžařské bundy</a> s membránou.</p>',
    faq=[
        ('Co znamená plnivost 700 cuin?', 'Jedna unce peří zaujme za stanovených podmínek objem 700 kubických palců. Vyšší číslo znamená, že stejné teplo zajistí menší hmotnost peří. Teplo ale závisí i na množství náplně.'),
        ('Co znamená poměr 90/10?', 'Náplň tvoří z 90 % prachové peří a z 10 % drobné peří s brkem. Vyšší podíl prachového peří znamená lehčí a pružnější izolaci.'),
        ('Co je certifikace RDS?', 'Responsible Down Standard ověřuje, že peří nepochází ze škubání živých ptáků ani z nuceného vykrmování, a sleduje celý řetězec od farmy po výrobek.'),
        ('Je péřová bunda nepromokavá?', 'Obvykle ne. Svrchní látka má vodoodpudivou úpravu na sníh a mrholení, do deště ale přes péřovku patří nepromokavá bunda.'),
        ('Jak vyprat péřovou bundu?', 'Prostředkem na peří, na šetrný program s nízkou teplotou a několikerým mácháním. Sušte v sušičce na nízkou teplotu s tenisovými míčky, dokud není úplně suchá.'),
        ('Co je ultralehká péřovka?', 'Tenká péřová bunda s malým množstvím náplně, která se sbalí do kapsy nebo vaku. Slouží jako zateplovací vrstva na túry nebo pod kabát.'),
        ('Je lepší péřová, nebo syntetická bunda?', 'Peří hřeje víc při nižší hmotnosti a lépe se sbalí. Syntetika je těžší, ale ve vlhku si udrží víc tepla a rychleji schne.'),
        ('Husí, nebo kachní peří?', 'Husí chomáčky bývají větší, kvalitu ale lépe popisuje plnivost a poměr peří. Kvalitní kachní peří může hřát stejně jako průměrné husí.'),
    ])
