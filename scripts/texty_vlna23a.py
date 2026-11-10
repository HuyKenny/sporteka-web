"""sporteka.cz — wave 23a (4. 11. 2026): long texts for hokejove-tasky, hokejove-dresy-a-obleceni, odrazedla, skialpinismus.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ hokejove-tasky
NEW['hokejove-tasky'] = dict(long=True,
    title='Hokejové tašky a batohy: velikosti, kolečka, výběr',
    desc='Hokejové tašky, batohy a vaky na výstroj. Jak vybrat velikost podle věku, kolečka, přihrádky a materiál a porovnat nabídky českých obchodů.',
    intro='<p>Hokejová výstroj je objemná, těžká a po tréninku mokrá, takže taška je její nedílná součást. Dobrá taška pojme brusle, helmu, chrániče i hokejky, ustojí tahání po šatnách a nenechá uvnitř zahnívat vlhkost. Sporteka porovnává nabídky českých obchodů u tašek s kolečky, přenosných vaků, batohů, tašek pro rozhodčí i obalů na oděv a drobností, jako jsou ochranné obaly na masku. U každé nabídky sledujte rozměry a objem, abyste věděli, pro jakou věkovou kategorii a množství výstroje je taška určená.</p>'
          '<p>V nabídce najdete značky ' + B(('bauer', 'Bauer'), ('grit', 'Grit'), ('winnwell', 'Winnwell'), ('fischer', 'Fischer'), ('ccm', 'CCM'), ('sherwood', 'Sherwood'), ('adidas', 'Adidas'), ('knapper', 'Knapper')) +
          '. K tašce se hodí <a href="/hokejove-brusle/">hokejové brusle</a>, <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>, <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a> a <a href="/hokejky/">hokejky</a>.</p>',
    guide='<h2>Jaké druhy hokejových tašek existují</h2>'
          '<p>Základní rozdělení vychází z toho, jak taška cestuje a kolik výstroje má pojmout. Hráč, který chodí na zimák pěšky nebo ho vozí rodiče, zvolí něco jiného než hráč, který cestuje s týmem autobusem. Rozhodčí a brankáři mají zase vlastní nároky na tvar a velikost.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Taška s kolečky', 'tuhé dno, výsuvné držadlo, velký objem', 'dospělé a starší děti s kompletní výstrojí'],
              ['Přenosná taška bez koleček', 'lehčí, ramenní popruhy nebo dvě držadla', 'mladší děti a krátké cesty'],
              ['Hokejový batoh', 'kompaktní, často s kolečky nebo bez nich', 'ledníky, doplňky, dojíždění po městě'],
              ['Taška na oděv', 'dlouhý obal na dres a civilní oblečení', 'týmy, trenéři a fanoušci při výjezdech'],
              ['Taška pro rozhodčí', 'užší, přihrádky na píšťalky a doplňky', 'rozhodčí, pomocný personál'],
              ['Brankářský vak', 'delší a širší, vyztužená konstrukce', 'brankářské betony a velké chrániče'],
              ['Hokejbalová taška', 'střední velikost, odlehčená', 'hokejbal, florbal a podobné sporty']]) +
          '<p>Poznámka k hokejbalu: kategorie obsahuje i tašky určené pro příbuzné sporty, třeba hokejbalové modely značky Knapper. Hokejová výstroj je ovšem objemnější a těžší, proto se tyto tašky na plnou výstroj nemusí hodit.</p>'
          '<h2>Velikost a objem podle věku hráče</h2>'
          '<p>Hokejové tašky se označují zkratkami podle věku: YTH nebo Youth pro nejmenší, JR pro juniory a SR pro seniory. Rozdíly jsou zřetelné, protože dětské chrániče, helma i brusle jsou menší a lehčí. Taška, která je pro dítě příliš velká, se špatně táhne a obtěžuje v šatně, ale příliš malá taška se nezavře a výstroj se v ní promačkává.</p>'
          '<ul><li><strong>Youth (nejmenší děti):</strong> kompaktní taška s kolečky nebo batoh, který zvládne unést samo dítě. Výstroj je malá a hlavně lehká.</li>'
          '<li><strong>Junior (zhruba školní věk):</strong> střední taška, která se dá zvednout i do kufru auta. S růstem dítěte se objem vyplatí volit s rezervou jedné velikosti.</li>'
          '<li><strong>Senior (dospělí a dorostenci):</strong> velká taška s koly a vyztuženým dnem, kde se vedle výstroje vejde i hokejka nebo dvě.</li>'
          '<li><strong>Brankáři:</strong> chrániče nohou a lapačka potřebují delší a širší prostor, takže se jim hodí výrazně větší model než hráči v poli.</li></ul>'
          '<p>Při hledání se řiďte rozměry v centimetrech a objemem v litrech, ne jen označením S, M a L. Pokud váháte, přiložte rozměry k délce svých chráničů nebo je rozložte na zem a změřte. Dlouhé hokejky se do běžné tašky nevejdou celé, proto si délku porovnejte s rozměry tašky; samostatné hokejky a čepele najdete v kategorii <a href="/hokejove-cepele-a-nasady/">hokejové čepele a násady</a>.</p>'
          '<h2>Kolečka, držadla a popruhy</h2>'
          '<p>Kolečka jsou největší rozdíl mezi taškami. Taška s koly se nemusí nosit, což u plně naložené výstroje ocení hlavně mladší hráči a rodiče. Pozor na kvalitu koleček a rámu: levné plastové nápravy se na schodech a venku rychle zničí a opravit je často nelze.</p>'
          '<ul><li><strong>Kolečka:</strong> větší a gumové jsou tišší a snáz překonají obrubníky a sníh. Úzké kluzáky stačí pro hladkou podlahu zimáku.</li>'
          '<li><strong>Výsuvné držadlo:</strong> musí zůstat pevné i při zátěži. U dětských modelů je kratší, aby se ho dítě dosáhlo.</li>'
          '<li><strong>Ramenní popruhy:</strong> některé tašky se dají nosit jako batoh, což pomůže při schodech nebo na zastávce.</li>'
          '<li><strong>Madla po stranách:</strong> usnadňují nakládání do auta a do podpalubí autobusu.</li></ul>'
          '<h2>Materiál a konstrukce</h2>'
          '<p>Hokejová výstroj je ostrá a těžká, brusle mají kovové nože a hokejka může látku protrhnout. Nejodolnější tašky mají vyztužené dno, plastový rám nebo kombinaci tvrdého a měkkého nylonu. Hrubá balistická tkanina vydrží víc, ale je těžší. Lehčí polyester se hodí pro děti a pro příležitostné hráče.</p>'
          '<p>Zipy jsou nejčastější slabé místo. Dvoucestný zip s velkými zoubky vydrží i při nacpané tašce a nezadrhává se o oblečení. Kontrolujte také šev u koleček a držadel, protože tam je největší namáhání. U kvalitnějších značek se dá koupit náhradní kolečko nebo držadlo, což prodlouží životnost.</p>'
          '<h2>Větrání a péče o vlhkou výstroj</h2>'
          '<p>Po tréninku je výstroj promočená potem a špatně uložená zápach zahnívá během jedné noci. Proto mnoho tašek má větrací otvory, síťované kapsy nebo oddělenou přihrádku na mokré věci. Samo o sobě to ale nestačí: nejlepší prevencí je po příjezdu domů vše vyndat a nechat vyschnout.</p>'
          '<ul><li>Vyndejte chrániče, helmu a rukavice z tašky a rozložte je v místnosti s oběhem vzduchu.</li>'
          '<li>Taškou otočte dnem vzhůru, rozepněte všechny zipy a nechte ji vysušit.</li>'
          '<li>Brusle vyndejte z obalů a vyjměte vložky, aby se jádro vysušilo. Podrobnosti o péči najdete v kategorii <a href="/hokejove-brusle/">hokejové brusle</a>.</li>'
          '<li>Taška se dá vyprat ručně vlažnou vodou s jemným mýdlem, pračku ale nepoužívejte, pokud ji výrobce výslovně nedovoluje.</li>'
          '<li>Do tašky vložte vysoušecí sáčky nebo kousek novin, které nasají vlhkost.</li></ul>'
          '<h2>Přihrádky a organizace uvnitř</h2>'
          '<p>Dobrá taška má víc než jedno velké hlavní oddělení. Boční kapsy se hodí na hokejové pásky, mouthguard, lahev nebo klíče, zadní plochá kapsa na doklady a zvenčí přišité pouzdro na hokejky. Samostatné spodní oddělení na brusle zabrání tomu, aby si nože nepoškodily kapsy a oblečení. Brankářské verze mívají pevné přihrádky pro lapačku a vyrážečku.</p>'
          '<p>Pokud máte hodně drobností, pořiďte si menší tašku nebo batoh jako doplněk. Hokejové pásky, tkaničky a další spotřební zboží najdete v kategorii <a href="/hokejove-pasky-a-doplnky/">hokejové pásky, tkaničky a doplňky</a>.</p>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Mladý hráč v klubu:</strong> menší taška s koly a dobře uchopitelným držadlem. Vyplatí se barva, kterou dítě pozná v šatně mezi ostatními.</li>'
          '<li><strong>Dorostenec a dospělý:</strong> velký model s vyztuženým dnem. Pokud jezdíte na výjezdy, zvažte i tašku na oděv.</li>'
          '<li><strong>Brankář:</strong> speciální dlouhý vak, který pojme dlouhé chrániče bez zalamování.</li>'
          '<li><strong>Rekreační hráč:</strong> lehčí taška bez koleček nebo batoh, pokud nosíte jen brusle, helmu a rukavice.</li>'
          '<li><strong>Rozhodčí:</strong> užší taška, kde se vejdou brusle, píšťalka, oblečení a dokumenty.</li>'
          '<li><strong>Fanoušek a trenér:</strong> taška na oděv nebo cestovní batoh, který nemusí pojmout celou výstroj.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie nejsou jen hokejové tašky. Najdete tu městské a školní batohy hokejových značek, tašky na doplňky a obuv, drobné obaly na masku brankáře a také termoobaly na svačinu a pití. Z hlediska značek převládají Bauer a Grit, dále Winnwell, Fischer, CCM a Sherwood. V menším počtu se objevují tašky Adidas, Warrior, Merco i české značky.</p>'
          '<p>Pokud hledáte pouze sportovní tašku bez hokejového motivu, procházejte raději širší kategorii <a href="/sportovni-tasky/">sportovní tašky a ledvinky</a> nebo <a href="/batohy/">batohy</a>. Cestovní vaky na lyže a lyžařské boty najdete v kategorii <a href="/lyzarske-vaky-a-tasky/">vaky a tašky na lyže a boty</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Taška příliš malá:</strong> výstroj se rozbaluje a zvlášť u dětí, které rostou, vyžaduje větší prostor už po jedné sezoně.</li>'
          '<li><strong>Taška příliš velká pro dítě:</strong> dítě ji neunese a tahá po zemi, což ničí látku i kolečka.</li>'
          '<li><strong>Zapomenuté větrání:</strong> uzavřená taška s mokrými chrániči je ideální prostředí pro plísně a zápach.</li>'
          '<li><strong>Nekontrolované zipy:</strong> zip s malými zuby při plné tašce rychle praskne. Raději volte robustní.</li>'
          '<li><strong>Taška bez ochrany nožů:</strong> brusle bez krytů poškodí látku a mohou ublížit.</li></ul>'
          '<h2>Cestování s hokejovou taškou</h2>'
          '<p>Na výjezdy a turnaje se taška nakládá do autobusu nebo kufru auta, kde ji nic nemá tlačit. Před cestou zkontrolujte, zda jsou brusle v krytech, helma nahoře a lahev uzavřená. Taška, která drží tvar díky tuhému dnu, se lépe skládá vedle ostatních. Do tašky nepatří cennosti, které by mohly zůstat v šatně bez dozoru, a doklady raději nosit zvlášť. Popiště si ji jménem a číslem dresu, protože v šatně stojí dvacet podobných černých tašek.</p>'
          '<p>Pro děti se osvědčilo označit tašku výraznou stuhou nebo nášivkou, aby ji poznaly ze všech. Pokud se bojíte ztráty, vložte dovnitř kartičku s kontaktem na rodiče.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejné tašky, zobrazujeme dostupné barvy a velikosti a upozorňujeme na výprodejové kusy, které se prodávají v jedné barvě nebo jedné velikosti. Před koupí si ověřte rozměry v popisu obchodu a porovnejte je s tím, co plánujete do tašky dát. U zboží z doprodeje počítejte s tím, že se model už nemusí vrátit do prodeje.</p>',
    faq=[
        ('Jakou velikost hokejové tašky zvolit pro dítě?', 'Podle věkové kategorie označené jako YTH, JR nebo SR a podle rozměrů výstroje. Mladší děti potřebují lehčí menší model, který unesou samy, a se vzrůstem se velikost mění po jedné až dvou sezonách.'),
        ('Je lepší taška s kolečky, nebo bez nich?', 'Taška s koly je pohodlnější u plné výstroje a delší cesty, bez koleček je lehčí a dá se nosit po schodech. Pro rekreační hráče a menší děti často stačí lehká taška nebo batoh.'),
        ('Pojme hokejová taška i hokejky?', 'Většina velkých tašek má vnější úchyty nebo kapsu na hokejky, ale hokejka se uvnitř zpravidla nevejde celá. Vždy ověřte délku tašky a případné popruhy.'),
        ('Jak odstranit zápach z hokejové tašky?', 'Vše vyndejte, taškou otočte a nechte ji důkladně vyschnout. Pak ji vymyjte vlažnou vodou s jemným mýdlem nebo octem, opláchněte a znovu vysušte na vzduchu.'),
        ('Dá se hokejová taška prát v pračce?', 'Jen pokud to výslovně dovoluje výrobce, jinak hrozí poškození kolečkových mechanismů i tvarové výztuže. Bezpečnější je ruční praní kartáčem a vlažnou vodou.'),
        ('Čím se liší brankářská taška od hráčské?', 'Je delší a širší, aby se do ní vešly objemné chrániče nohou, lapačka a vyrážečka bez zalamování. Mívá vyztužené dno a přihrádky na jednotlivé části.'),
        ('Co znamenají zkratky YTH, JR a SR?', 'Označují věkové a velikostní řady, tedy Youth pro nejmenší, Junior pro starší děti a Senior pro dospělé. Menší označení znamená kratší rozměry a nižší objem.'),
        ('Hodí se hokejové batohy do školy?', 'Ano, mnoho z nich vyhovuje jako městský batoh, ale mají tvarové a barevné řešení pro sportovce. Zkontrolujte vnitřní organizaci a zádovou část, zda je dostatečně polstrovaná.'),
        ('Na co si dát pozor u výprodejových tašek?', 'Na dostupnost barvy a velikosti, protože výprodejové kusy se často prodávají jen v jedné variantě. Zkontrolujte také popis zipů a koleček, abyste věděli, co kupujete.'),
        ('Jak dlouho taška vydrží?', 'Záleží na materiálu a zacházení. Vyztužené dno, silný zip a kvalitní kolečka prodlouží životnost na několik sezon, pokud výstroj po každém tréninku vysušíte.'),
    ],
)

# ------------------------------------------------------------------ hokejove-dresy-a-obleceni
NEW['hokejove-dresy-a-obleceni'] = dict(long=True,
    title='Hokejové dresy a oblečení: reprezentace, tréninkové',
    desc='Hokejové dresy, trika, ribana a ponožky. Fandresy, tréninkové dresy i spodní vrstvy. Jak vybrat velikost a péči a porovnat obchody.',
    intro='<p>Hokejové oblečení se dělí na dresy, které hráči nosí nad chrániči, a na spodní vrstvy, ribana, trika a ponožky, které s nimi tvoří základ pod výstrojí. K tomu přibývají fandresy reprezentace, retro repliky, mikiny i klubové čepice. Sporteka porovnává nabídky českých obchodů u tréninkových i zápasových dresů, dětských a juniorských velikostí a hokejového textilu pro fanoušky. U každého kusu rozlišujeme, zda je určený na led, nebo do ulice.</p>'
          '<p>V kategorii převažují značky ' + B(('ccm', 'CCM'), ('merco', 'Merco'), ('winnwell', 'Winnwell'), ('sherwood', 'Sherwood'), ('nike', 'Nike'), ('bauer', 'Bauer'), ('sportteam', 'SportTeam'), ('strida', 'Střída')) +
          '. K dresu se hodí <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>, <a href="/hokejove-brusle/">hokejové brusle</a> a <a href="/hokejove-tasky/">hokejové tašky</a>.</p>',
    guide='<h2>Co všechno spadá do hokejového oblečení</h2>'
          '<p>Kategorie je širší, než by se zdálo. Kromě klasických dresů zahrnuje spodní vrstvy, které se nosí pod chrániči, i fanouškovské textilie, které s ledem nemají nic společného. Proto je dobré se u každého výrobku podívat na popis a rozlišit, zda jde o výkonnostní a ochranný kus, nebo o módu.</p>'
          + T(['Druh', 'Popis', 'Hodí se'], [
              ['Tréninkový dres', 'volnější střih, odolný pletený materiál', 'tréninky, přátelská utkání, rekreační hokej'],
              ['Zápasový dres', 'delší střih, výztuž v ramenou, klubový design', 'oficiální zápasy a turnaje'],
              ['Fandres reprezentace', 'replika oficiálního dresu, lehčí materiál', 'fanoušci, ulice, tribuna'],
              ['Retro replika', 'dresy z historických turnajů, často s potiskem jména', 'sběratelé a nostalgici'],
              ['Ribano (jednodílné)', 'těsný spodní overal bez rukávů nebo s nimi', 'pod chrániče pro lepší odvod potu'],
              ['Funkční triko', 'krátký nebo dlouhý rukáv, kompresní střih', 'pod výstroj i na běžný trénink'],
              ['Hokejové ponožky', 'dlouhé, přes holeň, barevné tak, aby ladily s dresem', 'zápasy a tréninky'],
              ['Mikina a tričko s logem', 'běžné oblečení, hokejové motivy', 'fanoušci a volný čas']]) +
          '<p>Pokud kupujete pro hráče, který pokračuje v oddílu, zeptejte se na klubová pravidla. Kluby často předepisují barvy, číslování a sponzorské potisky, ale mnohé tréninkové dresy dovolují vlastní volbu.</p>'
          '<h2>Dres pro hráče a dres pro fanouška</h2>'
          '<p>Rozdíl poznáte po prvním dotyku. Dres určený na led je odolný, často s dvojitým šitím v ramenou a na loktech, protože spodní strana při pádu a při tahání soupeře trpí. Fandres je lehčí a volnější, vyrábí se pro nošení v ulici nebo na tribuně, ne pro hru. Při hře na ledě ho nepotřebujete, na tribuně je ideální.</p>'
          '<p>U reprezentačních replik narazíte na dva rozlišitelné typy: obchodní fandres a autentickou verzi, která se vyrábí v řadě pro hráče a má střih, který odpovídá profesionální variantě. Autentický dres má obvykle přiléhavější střih, odlišné švy a často výšivku nebo našité znaky místo potisku. Hledáte-li kus na led, zkontrolujte popis: fandres se tam obvykle nehodí.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Hokejové dresy mají záměrně volný střih, protože se oblékají přes ramenní a hrudní chrániče. Pokud kupujete dres na led, vezměte si velikost větší, než nosíte na běžné oblečení, nebo vyzkoušejte dres přímo přes chrániče. Při koupi fandresu naopak postačí běžná velikost, případně o něco volnější, pokud se dres nosí přes mikinu.</p>'
          '<ul><li><strong>Dětské velikosti (YTH):</strong> pro nejmenší, často označené věkem nebo výškou. Dres by měl sahat po boky a rukáv po zápěstí.</li>'
          '<li><strong>Juniorské (JR):</strong> dospívající, kteří se rychle mění. Raději volte rezervu, ale ne tolik, aby rukávy překážely při držení hokejky.</li>'
          '<li><strong>Seniorské (SR):</strong> dospělí a dorostenci, od S po 3XL podle značky.</li>'
          '<li><strong>Dámské střihy:</strong> u některých fandresů existují užší dámské verze s kratšími rukávy.</li></ul>'
          '<p>Velikostní tabulky se liší mezi značkami, takže vždy porovnejte rozměry v centimetrech. U kusů, které se prodávají s upozorněním, že jde o poslední velikost, je potřeba ověřit, zda daná velikost skutečně sedí.</p>'
          '<h2>Materiál a úprava</h2>'
          '<p>Většina hokejových dresů se šije z polyesteru nebo polyesterového pleteniva, které odvádí pot a rychle schne. Zápasové dresy mají hustší tkaninu a někdy síťovinu v bocích pro větrání. Fandresy bývají lehčí a mají často potisk místo výšivky. Znaky a čísla jsou buď vyšité, nebo nažehlené, přičemž výšivka vydrží víc praní.</p>'
          '<p>Spodní vrstvy jsou zpravidla z elastického polyesteru s elastanem, někdy s antibakteriální úpravou. Cílem je odvádět pot od kůže, aby chrániče nebyly mokré a zápach se nezdržoval. Kompresní střih drží svalstvo a snižuje otěr, ale nesmí tlačit v podpaží a v lýtkách.</p>'
          '<h2>Ribano a spodní vrstvy</h2>'
          '<p>Jednodílné ribano je specifikum hokeje. Je to elastický overal, který se obléká pod chrániče a po tréninku se dá snadno vyprat, takže zbytek výstroje se nemusí prát tak často. Mnoho hráčů ho nosí jen proto, že se k němu dají připnout návleky a štulpny. Dětem se osvědčuje, protože se oblékání výstroje zjednoduší na jeden krok.</p>'
          '<ul><li><strong>S rukávy nebo bez:</strong> dlouhé rukávy chrání před otěrem od chráničů, bez rukávů je komfortnější při vysokých teplotách.</li>'
          '<li><strong>Vložky a poutka:</strong> poutka na kotnících a lýtkách drží návleky na štulpny a nepřekážejí v bruslích.</li>'
          '<li><strong>Antibakteriální úprava:</strong> pomáhá proti zápachu, ale nenahradí pravidelné praní.</li>'
          '<li><strong>Střih po tělo:</strong> příliš volné ribano se v chráničích sklouzává a tlačí.</li></ul>'
          '<h2>Ponožky a štulpny</h2>'
          '<p>Hokejové ponožky jsou dlouhé a sahají nad kolena, kde se připevňují k ribanu nebo k suspenzorům. Sladění barev s dresem je v týmu povinné. Pro lepší pohodlí v bruslích hledejte ponožky s vyztužením na pátě a nártu a s protiskluzovou strukturou. Tenčí tkaniny snižují tlak v bruslích a zlepšují cit.</p>'
          '<p>Chrániče holení a kolen s ponožkami souvisejí v kategorii <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a>.</p>'
          '<h2>Reprezentační a retro dresy</h2>'
          '<p>Reprezentační dresy se mění obvykle každý rok nebo před velkými turnaji. Starší kolekce bývají ve slevě, ale vzácné velikosti dojdou rychle. Retro repliky odkazují na historické turnaje a jsou zpravidla vyráběné ve formě fandresů s vyšitými znaky. Mnoho obchodů nabízí možnost potisku vlastního jména a čísla, takže si každý vytvoří originální kus.</p>'
          '<p>Při objednávce potisku kontrolujte, zda zboží lze vrátit. Zakázkově upravený výrobek se většinou nevrací, a proto si předem ověřte velikost a pravopis jména. Pokud hledáte hokejový dres jako dárek, přečtěte si hodnocení velikosti a raději volte nepotištěný model, který se dá případně vyměnit.</p>'
          '<h2>Péče o dresy a spodní vrstvy</h2>'
          '<ul><li>Dres perte naruby při 30 °C šetrným prostředkem bez aviváže, která zalepuje vlákna a snižuje odvod potu.</li>'
          '<li>Nažehlené a potištěné části nežehlete přímo a nesušte v sušičce na vysokou teplotu, aby se nesloupaly.</li>'
          '<li>Spodní vrstvy perte po každém tréninku, protože pot a bakterie se v nich zdržují.</li>'
          '<li>Dres sušte rozložený na vzduchu, mimo topení a přímé slunce, které by vyblednulo barvy.</li>'
          '<li>Při praní zapněte suché zipy, aby se látka neškrábala a nezachytávala.</li></ul>'
          '<h2>Výběr podle situace</h2>'
          '<ul><li><strong>Dítě v klubu:</strong> klubový dres podle pokynů trenéra, tréninkový dres pro volné bruslení a ribano pro snadné oblékání.</li>'
          '<li><strong>Rekreační hráč:</strong> tréninkový dres, funkční spodní vrstva a pár hokejových ponožek.</li>'
          '<li><strong>Fanoušek:</strong> fandres reprezentace nebo oblíbeného klubu, případně mikina s logem.</li>'
          '<li><strong>Sběratel:</strong> retro repliky a autentické dresy s přesným střihem, nejlépe neupravené.</li>'
          '<li><strong>Dárek:</strong> dresy bez potisku, případně dárková sada s trikem a čepicí.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie je směs. Největší část tvoří produkty CCM, od tréninkových dresů přes spodní prádlo až po fandresy české reprezentace a trička s hokejovými motivy. Dále se zde objevují Merco s retro repliky, Winnwell s tréninkovými dresy a Sherwood s ribany. Ze značek, které se věnují také běžné módě, jsou zastoupeny Nike a 47 Brand.</p>'
          '<p>Pro další oblečení nebo pro zboží, které se dá nosit i mimo led, procházejte kategorie <a href="/mikiny/">mikiny</a> a <a href="/funkcni-mikiny/">funkční mikiny</a>. Spodní prádlo najdete také v kategorii <a href="/termopradlo/">funkční a termo prádlo</a>.</p>'
          '<h2>Co sledovat při nákupu pro rostoucí dítě</h2>'
          '<p>Dětské dresy a spodní vrstvy rostou s dítětem, a proto se vyplatí neutrácet za nejdražší kusy. Pro nejmenší stačí jednoduchý tréninkový dres, který se po sezoně předá mladšímu sourozenci. Důležitější je, aby ribano bylo správně dlouhé a nedřelo v rozkroku, a aby ponožky držely na místě. Rodiče uvítají, když dres drží barvu i po stovce praní a švy nevyplétají nitě. Vždy ověřte, zda daná velikost sedí podle věku a výšky, protože označení YTH, JR a SR nemusí u různých značek odpovídat stejně.</p>'
          '<p>Při koupi na výrost zvolte dres jen o jednu velikost větší, aby rukávy nepřekážely při držení hokejky a dítě se v něm neztratilo. Starší sourozenci často dresy předávají dál, takže raději vybírejte neutrální barvy bez jména a čísla, které se dají nosit na trénincích několik sezon po sobě.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného dresu, zobrazujeme dostupné velikosti a barvy a odlišujeme výprodejové kusy. U doprodejů se prodává často jediná velikost, takže si ji předem ověřte. U dresů reprezentace sledujte, zda jde o aktuální, nebo starší ročník, a zda je v popisu uveden materiál a typ střihu.</p>',
    faq=[
        ('Jaký je rozdíl mezi zápasovým dresem a fandresem?', 'Zápasový dres je odolnější, delší a určený přes chrániče, zatímco fandres je lehčí a volnější a není určený pro těžký provoz na ledě. Autentická verze se přibližuje profesionálnímu dresu.'),
        ('Jakou velikost dresu zvolit na led?', 'Dres se obléká přes chrániče, takže se obvykle volí o velikost větší než běžné oblečení. Nejlepší je zkusit ho přes výstroj nebo porovnat rozměry v tabulce.'),
        ('K čemu slouží jednodílné ribano?', 'Obléká se pod chrániče, odvádí pot a zjednodušuje oblékání. Díky poutkám drží návleky na štulpny a po tréninku se dá snadno vyprat.'),
        ('Jak prát hokejový dres?', 'Perte ho naruby při nízké teplotě bez aviváže a suste rozložený na vzduchu. Potištěné části nežehlete přímo a nepoužívejte sušičku na vysokou teplotu.'),
        ('Dá se na dres nechat potisknout jméno a číslo?', 'Mnoho obchodů potisk nabízí, ale zakázkově upravené zboží se obvykle nevrací. Před objednávkou ověřte velikost a pravopis jména.'),
        ('Mohu fandres nosit na trénink?', 'Dá se použít při lehčí aktivitě, ale na led je vhodnější tréninkový dres, který odolá otěru a tahání. Fandres je primárně do ulice a na tribunu.'),
        ('Čím se liší dětské velikosti od juniorských?', 'Dětské YTH jsou pro nejmenší hráče, juniorské JR pro starší děti a dorost, a seniorské SR pro dospělé. Střih a délka rukávů se u každé řady liší.'),
        ('Proč jsou hokejové dresy tak volné?', 'Protože se nosí přes ramenní a hrudní chrániče. Volný střih umožní pohyb paží a pohodlné oblečení bez tlaku na výstroj.'),
        ('Hodí se ribano pro začátečníky?', 'Ano, zjednodušuje oblékání a chrání kůži před otěrem od chráničů. U dětí se osvědčilo hlavně kvůli rychlosti převlékání v šatně.'),
        ('Jak poznám autentický dres reprezentace?', 'Podle popisu výrobce, přiléhavějšího střihu, vyšitých znaků a označení pro hráčskou řadu. Fandres je obvykle lehčí a s potištěnými znaky.'),
    ],
)

# ------------------------------------------------------------------ odrazedla
NEW['odrazedla'] = dict(long=True,
    title='Odrážedla pro děti: velikost, brzda, materiál a výběr',
    desc='Dětská odrážedla dřevěná, kovová i plastová. Jak vybrat velikost kol, hmotnost, brzdu a sedlo a porovnat nabídky českých obchodů.',
    intro='<p>Odrážedlo je první kolo, které se dítě učí ovládat. Odráží se nohama od země, nasbírá rychlost, a tím se postupně naučí udržet rovnováhu, což je hlavní dovednost při jízdě na kole. Sporteka porovnává nabídky českých obchodů u dřevěných, kovových, hliníkových i plastových modelů, od klasických odrážedel po balanční kola s brzdou. Pro každé odrážedlo uvádíme velikost kol, váhu a vlastnosti, které rozhodují, zda ho dítě zvládne.</p>'
          '<p>V nabídce převažují značky ' + B(('yedoo', 'Yedoo'), ('cariboo', 'Cariboo'), ('baby-mix', 'Baby MIX'), ('lionelo', 'Lionelo'), ('falk', 'Falk'), ('btwin', 'Btwin'), ('olpran', 'Olpran'), ('hypermotion', 'Hypermotion')) +
          '. Navazují <a href="/detska-kola/">dětská kola a odrážedla</a>, <a href="/detska-kola-12-14-palcu/">dětská kola 12 a 14 palců</a>, <a href="/detske-cyklohelmy/">dětské cyklohelmy</a> a <a href="/detske-trikolky/">dětské tříkolky</a>.</p>',
    guide='<h2>K čemu odrážedlo slouží</h2>'
          '<p>Hlavním úkolem odrážedla je naučit dítě rovnováhu dřív, než dostane pedály. Dítě sedí v sedle, nohama se odráží a v zatáčce se učí naklánět a řídit. Po několika týdnech zvládne klouzat s nohama nad zemí, a když pak sedne na kolo bez pomocných kolečka, naučí se jezdit mnohem rychleji než dítě, které začínalo na tříkolce. Odrážedlo je navíc lehké, takže ho dítě zvedne samo po pádu.</p>'
          '<p>Většina dětí začíná mezi druhým a třetím rokem, někdy dříve, pokud dosáhnou na zem. Rozhodující není věk, ale výška a chuť. Dítě, které se bojí, nenuťte. Raději chvíli počkejte a odrážedlo mu nechte stát v obývacím pokoji, aby si zvyklo.</p>'
          '<h2>Jaké typy odrážedel existují</h2>'
          + T(['Typ', 'Vlastnosti', 'Hodí se pro'], [
              ['Dřevěné odrážedlo', 'jednoduché, tiché, často se vzorem, těžší', 'nejmenší děti a hraní doma i venku'],
              ['Kovové (ocel, hliník)', 'pevné, často nastavitelné, brzda i na řídítkách', 'aktivní děti, delší jízdy a kopce'],
              ['Plastové a kompozitní', 'lehké, odolné proti vodě, pestré barvy', 'batolata a předškoláci'],
              ['Odrážedlo s brzdou', 'ruční brzda na řídítkách, vzduchové pneumatiky', 'děti, které jezdí venku na rovinách i z kopce'],
              ['Odrážedlo s třetím kolem', 'stabilnější, tříkolový podvozek', 'začátečníci, kteří se ještě bojí'],
              ['Skládací odrážedlo', 'rychle složitelné, kompaktní', 'rodiny, které cestují a potřebují malý kufr'],
              ['Odrážedlo se zvukem a světly', 'zábavné hračky, často bez nastavení sedla', 'hraní doma a na zahradě']]) +
          '<p>Rozdíl mezi hračkou a sportovním náčiním je důležitý. Hračková odrážedla bývají těžší a bez brzdy, sportovní lehčí a s nastavitelnými částmi. Pokud má dítě jezdit venku, doporučujeme zvolit sportovnější typ, který se dá později nahradit klasickým kolem.</p>'
          '<h2>Velikost kol, sedlo a rám</h2>'
          '<p>Nejdůležitější parametr je výška sedla. Dítě musí v sedle dosáhnout na zem celými chodidly a mít mírně pokrčená kolena. Pokud se špičkami sotva dotýká, nemůže se odrážet a vyvolá to strach. Naopak příliš nízké sedlo způsobí, že dítě sedí s koleny nahoře a neodrazí se pořádně.</p>'
          '<ul><li><strong>Vnitřní délka nohavice:</strong> změřte od rozkroku k zemi a porovnejte s minimální výškou sedla v popisu.</li>'
          '<li><strong>Průměr kol:</strong> nejmenší modely mají kola kolem deseti palců, větší dvanáct, a ty největší slouží už jako přechod ke kolu.</li>'
          '<li><strong>Nastavení sedla a řídítek:</strong> odrážedlo by mělo růst s dítětem. Podívejte se, zda nástavba stačí na jednu, nebo dvě sezony.</li>'
          '<li><strong>Rozvor a tvar rámu:</strong> nízký nástupní bod usnadní nasedání a zmenšuje hrozbu pádu.</li></ul>'
          '<p>Až dítě odroste největší odrážedlo, nastoupí klasické kolo. Podle výšky navazují kategorie <a href="/detska-kola-12-14-palcu/">dětská kola 12 a 14 palců</a> a <a href="/detska-kola-16-palcu/">16 palců</a>.</p>'
          '<h2>Hmotnost a materiál</h2>'
          '<p>Odrážedlo by nemělo vážit více než třetinu hmotnosti dítěte, ideálně méně. Těžší model se těžko zvedá po pádu a špatně se obrací. Výrobci uvádějí hmotnost v kilogramech, takže porovnání je snadné. Nejlehčí modely z hliníku nebo hořčíkové slitiny se pohybují kolem tří až pěti kilogramů, dřevěné bývají těžší.</p>'
          '<ul><li><strong>Dřevo:</strong> příjemné na dotek, tiché, s přírodním vzhledem. Je těžší a při dešti musí být ošetřeno.</li>'
          '<li><strong>Ocel:</strong> pevná, levnější, ale těžší a může rezavět, pokud se poškodí lak.</li>'
          '<li><strong>Hliník a hořčík:</strong> lehké a odolné vůči korozi, ale dražší.</li>'
          '<li><strong>Plast a kompozit:</strong> odolný proti vodě, často v pestrých barvách a lehký.</li></ul>'
          '<h2>Pneumatiky: pěnové, plné, nafukovací</h2>'
          '<p>Kola jsou podstatná pro komfort a bezpečí. Plastová kola s malou pryží jsou nejlevnější a vhodná na rovnou dlažbu. Pěnová kola (EVA) jsou lehká, neprorazí se a nezanechávají stopy v bytě. Nafukovací pneumatiky mají nejlepší záběr a tlumí nárazy, ale vyžadují čerpadlo a případné lepení.</p>'
          '<p>Pro nerovný terén, trávu a zahradu se hodí vzduchové pneumatiky. Pro byt a hladké povrchy stačí pěnové. Pokud dítě odrážedlo používá na chodnících, vyplatí se kvalitnější pneumatika s dezénem, která při zatáčení nesklouzává. Pokud hledáte větší kolo, přečtěte si kategorie <a href="/jizdni-kola/">jízdní kola</a>.</p>'
          '<h2>Brzda a bezpečnost</h2>'
          '<p>Brzda na odrážedle je spor mezi rodiči. Dítě se v počátcích brzdí chodidly, proto brzda není nutná, ale při jízdě z kopce nebo na silnějších modelech je výhodná. Ruční brzda na zadním kole se dítě učí používat a při přechodu na klasické kolo je to velký bonus. Ovládání musí být nastavené tak, aby ho dítě dosáhlo malou rukou.</p>'
          '<ul><li><strong>Helma:</strong> i na odrážedle je důležitá. Vyberte ze sortimentu <a href="/detske-cyklohelmy/">dětských cyklohelem</a> takovou, která se dá nastavit na obvod hlavy.</li>'
          '<li><strong>Chrániče:</strong> kolena a lokty v kategorii <a href="/cyklo-chranice/">chrániče pro cyklisty</a> zmírní následky pádu na asfaltu.</li>'
          '<li><strong>Pevná obuv:</strong> dítě se odráží nohama, takže sandály a pantofle nestačí. Zavřená bota chrání prsty.</li>'
          '<li><strong>Prostředí:</strong> jezděte jen na bezpečných plochách, ne na silnici a v blízkosti schodů a vody.</li></ul>'
          '<h2>Jak naučit dítě jezdit</h2>'
          '<p>Nejlepší metoda je nechat dítě objevovat. Začněte na rovné ploše bez provozu, kde si dítě sedne, odrazí se a postupně zvedá nohy. Netlačte a nepodpírejte ho za sedlo, protože se tím učí spoléhat na vaši pomoc a ztrácí cit pro rovnováhu. Pochvala za každý pokus zvýší jistotu. Když dítě zvládne klouzat s nohama nahoře, zkuste mírný svah a zatáčky.</p>'
          '<p>Zkušenější děti rády závodí a zkouší překážky. V té chvíli vyhovuje odrážedlo s větším kolem a brzdou. Pokud dítě přestane odrážedlo bavit, vyzkoušejte <a href="/kolobezky/">koloběžky</a> nebo <a href="/detske-trikolky/">tříkolky</a>, které trénují jiné dovednosti.</p>'
          '<h2>Odrážedlo nebo tříkolka, koloběžka a kolo</h2>'
          '<ul><li><strong>Odrážedlo:</strong> trénuje rovnováhu a koordinaci. Dítě se po něm obvykle snáze naučí jezdit na kole bez pomocných kolečka.</li>'
          '<li><strong>Tříkolka:</strong> je stabilnější a hodí se pro nejmenší, rovnováhu ale netrénuje. Pro děti, které potřebují hodně opory.</li>'
          '<li><strong>Koloběžka:</strong> rozvíjí jinou rovnováhu a hodí se od předškolního věku. Dá se kombinovat s odrážedlem.</li>'
          '<li><strong>Kolo s pedály:</strong> následuje, až dítě zvládne rovnováhu. Pomocná kolečka už nejsou potřeba.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie obsahuje odrážedla různých typů: dřevěná, kovová, plastová, se zvukem i balanční kola s brzdou. Mezi výrobci vynikají Yedoo, Cariboo a Baby MIX, dále Lionelo, Falk, Btwin a Olpran. Najdete tu i hračková odrážedla, jako zvířátka a čtyřkolky se zvukem, která se používají hlavně doma. Doplňky, jako náhradní kola nebo košíčky, se objevují zřídka.</p>'
          '<p>Pokud hledáte odrážedlo s extra funkcemi, hledejte podle popisu: sklopné, nastavitelné nebo odlehčené. Zařazené jsou i výprodejové kusy, které se prodávají v jedné barvě, takže si před koupí ověřte dostupnost.</p>'
          '<h2>Péče a údržba</h2>'
          '<ul><li>Po jízdě v dešti odrážedlo otřete a nechte uschnout, aby neoxidovaly šrouby a kolečka.</li>'
          '<li>Jednou za čas zkontrolujte dotažení šroubů na sedle a řídítkách a upravte výšku podle růstu dítěte.</li>'
          '<li>Nafukovací pneumatiky dohustěte na tlak uvedený na plášti.</li>'
          '<li>Dřevěné odrážedlo skladujte v suchu a při poškrábání jej přebruste a ošetřete.</li>'
          '<li>Uložte jej mimo přímé slunce a mráz, které poškozují plast i lak.</li></ul>'
          '<h2>Odrážedlo jako dárek</h2>'
          '<p>Odrážedlo patří mezi nejoblíbenější dárky k druhým a třetím narozeninám. Při výběru zvažte nejen barvu a design, ale hlavně to, zda se dá sedlo nastavit dost nízko pro současnou výšku dítěte a dost vysoko pro příští rok. Pokud kupujete bez znalosti míry, zeptejte se rodičů na vnitřní délku nohavice nebo přiložte měřidlo k dítěti u příležitosti oslavy. Doplňte dárek helmou a rukavicemi, případně obálkou na jednu návštěvu bezpečného dětského hřiště.</p>'
          '<p>Hračkářské modely se zvukem a světly zabaví doma, ale sportovnější kus s kvalitními koly je vhodný i pro venkovní jízdu a vydrží déle. U použitých odrážedel zkontrolujte, zda se nepovolilo sedlo, nejsou prasklá kolečka a zda jsou řídítka pevná.</p>'
          '<h2>Jak dítě ukládat a převážet</h2>'
          '<p>Odrážedlo se vejde do kufru auta, přesto stojí za to ho před nakládáním zbavit bláta. Skládací modely přijdou vhod při cestování nebo když v bytě chybí místo. Pro výlety do přírody vezměte pumpičku, pokud jsou kola nafukovací, a malý šroubovák na dotažení sedla. Nechávat odrážedlo celou zimu na balkoně není vhodné, protože mráz poškozuje plast i dřevěné povrchy. Uložte je raději do chodby nebo sklepa, kde je sucho.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného odrážedla, zobrazujeme dostupné barvy a odlišujeme výprodejové kusy. Před koupí si ověřte minimální výšku sedla, hmotnost, velikost kol a to, zda je v ceně i brzda nebo zvonek. U dárku volte raději větší model s nastavitelným sedlem, který dítěti vydrží další rok.</p>',
    faq=[
        ('Od kolika let může dítě jezdit na odrážedle?', 'Obvykle od druhého roku věku, záleží ale spíš na výšce a zájmu. Dítě musí v sedle dosáhnout na zem celými chodidly, aby se mohlo odrážet.'),
        ('Jak vybrat správnou velikost odrážedla?', 'Změřte vnitřní délku nohavice a porovnejte ji s minimální výškou sedla v popisu. Sedlo má být tak nízko, aby dítě stálo oběma chodidly na zemi.'),
        ('Potřebuje odrážedlo brzdu?', 'Není nutná, protože se dítě brzdí chodidly, ale u rychlejších modelů a z kopce je užitečná. Dítě se s ní učí používat ruční brzdu před přechodem na kolo.'),
        ('Jaké kolo je lepší: pěnové, nebo nafukovací?', 'Pěnová jsou lehká a nepotřebují údržbu, hodí se na hladké povrchy. Nafukovací mají lepší záběr a tlumí nárazy, ale vyžadují čerpadlo.'),
        ('Je odrážedlo lepší než tříkolka?', 'Pro učení rovnováhy ano, protože dítě trénuje to, co potřebuje na kole. Tříkolka je stabilnější pro nejmenší, ale rovnováhu netrénuje.'),
        ('Má dítě na odrážedle nosit helmu?', 'Ano, i při pomalé jízdě se dítě může dostat do pádu. Vybírejte helmu s nastavitelným obvodem a pevným zapínáním.'),
        ('Jak těžké má být odrážedlo?', 'Ideálně méně než třetina hmotnosti dítěte. Lehčí modely se snáze zvedají po pádu a lépe se řídí, ale bývají dražší.'),
        ('Kdy přejít z odrážedla na kolo?', 'Když dítě bezpečně klouže s nohama ve vzduchu a zatáčí, zpravidla kolem čtyř až pěti let. Pomocná kolečka u kola pak většinou nejsou potřeba.'),
        ('Jaký materiál odrážedla je nejlepší?', 'Dřevo je tiché a příjemné, ocel pevná, hliník a plast lehčí. Volbu určí váha, budget a místo, kde se bude jezdit.'),
        ('Mohu odrážedlo používat i v zimě?', 'Na suchém povrchu ano, ale kolo musí být vhodné pro nízké teploty. Sníh a led dětem nedoporučujeme, hrozí smyk. Po jízdě odrážedlo osušte.'),
    ],
)

# ------------------------------------------------------------------ skialpinismus
NEW['skialpinismus'] = dict(long=True,
    title='Skialpinismus: lyže, boty, vázání a pásy na skialp',
    desc='Skialpinistická výbava: lyže, boty, tech vázání, pásy, cepíny a oblečení. Jak vybrat hmotnost a lavinovou výbavu a porovnat obchody.',
    intro='<p>Skialpinismus je výstup na lyžích s pásy a následný sjezd v neupraveném terénu. Výbava proto musí být lehká na výstup a dost spolehlivá na sjezd. Sporteka porovnává nabídky českých obchodů u <a href="/skialpove-lyze/">skialpových lyží</a>, <a href="/skialpove-boty/">skialpových bot</a>, <a href="/skialpove-vazani/">tech vázání</a> a <a href="/skialpove-pasy/">stoupacích pásů</a>, ale také u skialpového oblečení, cepínů, maček a drobností, jako je lepidlo na pásy. U každého typu se vyplatí ověřit, pro jaký styl túr je určený.</p>'
          '<p>V kategorii najdete například značky ' + B(('dynafit', 'Dynafit'), ('northfinder', 'Northfinder'), ('pomoca', 'Pomoca'), ('fischer', 'Fischer'), ('wedze', 'Wedze'), ('simond', 'Simond'), ('kastle', 'Kästle'), ('atomic', 'Atomic')) +
          '. Související výběr najdete v kategoriích <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyzarske-helmy/">lyžařské helmy</a>, <a href="/lyzarske-bryle/">lyžařské brýle</a> a <a href="/lyzarske-hole/">lyžařské hole</a>.</p>',
    guide='<h2>Jak skialpinismus funguje</h2>'
          '<p>Skialpinista stoupá s lyžemi na nohou. Na skluznici jsou nalepené stoupací pásy, které dovolují klouzat dopředu, ale brání zacouvání dozadu. Pata boty je při výstupu uvolněná, takže se noha přirozeně zvedá. Na vrcholu se pásy sundají, pata zajistí a následuje sjezd. Celé to funguje díky vázání, které se přepíná mezi režimem chůze a sjezdu, a díky botám s režimem chůze.</p>'
          '<p>Výstup trvá obvykle déle než sjezd, proto se klade důraz na hmotnost. Každých sto gramů na noze se během tisíců kroků projeví. Na druhou stranu příliš lehká výbava je při sjezdu méně stabilní. Proto se skialpové vybavení dělí na kategorie od závodní přes lehkou až po freeridovou, kde se dává přednost výkonu ve sjezdu.</p>'
          '<h2>Základní výbava a její role</h2>'
          + T(['Část výbavy', 'Co dělá', 'Na co se dívat'], [
              ['Skialpové lyže', 'nesou jezdce při výstupu a sjezdu', 'hmotnost, šířka pod botou, délka'],
              ['Skialpové boty', 'přenášejí sílu, mají režim chůze', 'hmotnost, rozsah pohybu, kompatibilita s vázáním'],
              ['Vázání', 'drží botu na lyži, přepíná výstup a sjezd', 'typ (tech/pin, rám), hmotnost, uvolnění při pádu'],
              ['Stoupací pásy', 'umožňují stoupání po sněhu', 'šířka, délka, lepidlo, materiál'],
              ['Hole', 'pomáhají při výstupu a sjezdu', 'teleskopické, nastavitelná délka'],
              ['Helma a brýle', 'chrání při pádu a při slunci', 'lehká helma, odolná proti nárazu'],
              ['Lavinová výbava', 'vyhledávač, sonda, lopata', 'kurz a lavinová předpověď']]) +
          '<p>Důležité upozornění: vybavení nestačí, ke skialpu patří znalost terénu a lavinové problematiky. Kurzy pořádají horské služby a profesionální průvodci a patří k základu každé túry mimo upravené trasy.</p>'
          '<h2>Skialpové lyže</h2>'
          '<p>Skialpové lyže jsou lehčí než sjezdové a mívají jádro z lehkých materiálů. Rozhodují šířka pod botou a délka. Úzké lyže kolem osmdesáti milimetrů jsou ideální pro stoupání po upravených nebo zledovatělých svazích, širší kolem stovky nesou lépe v hlubokém sněhu. Pro začátečníky se hodí střední šířka, která funguje v různých podmínkách.</p>'
          '<ul><li><strong>Délka:</strong> obvykle od brady po čelo, lehčí lyže bývají o něco delší.</li>'
          '<li><strong>Závodní a ultralehké:</strong> pro závodníky, kteří chtějí dosáhnout co nejnižší hmotnosti na úkor stability.</li>'
          '<li><strong>Univerzální:</strong> střední šířka, dobrý poměr hmotnosti a výkonu, nejčastější volba.</li>'
          '<li><strong>Freeride-touring:</strong> širší a těžší, stabilnější ve sjezdu a pro hluboký sníh.</li></ul>'
          '<p>Kategorie obsahuje i kompletní sety, tedy lyže s vázáním a někdy i pásy, které jsou pro začátečníky výhodné, protože dílčí části jsou vzájemně sladěné. Podrobněji se lyžím věnuje kategorie <a href="/skialpove-lyze/">skialpové lyže</a>.</p>'
          '<h2>Skialpové boty</h2>'
          '<p>Skialpová bota je kompromis mezi tuhostí pro sjezd a pohyblivostí pro výstup. Má mechanismus, který uvolní manžetu, takže se noha může přirozeně ohýbat v kotníku. Boty se liší hmotností, počtem přezek a rozsahem pohybu. Lehčí modely se hodí na dlouhé túry a závody, těžší nabízejí lepší kontrolu ve sjezdu.</p>'
          '<ul><li><strong>Tuhost (flex):</strong> vyšší hodnoty jsou vhodné pro těžší a agresivnější jezdce, nižší pro pohodlí při stoupání.</li>'
          '<li><strong>Rozsah pohybu:</strong> větší rozsah ulehčuje stoupání do strmých svahů.</li>'
          '<li><strong>Vnitřní botička:</strong> tepelně tvarovatelná se přizpůsobí noze a zlepší pohodlí.</li>'
          '<li><strong>Kompatibilita s vázáním:</strong> boty musí mít tech vložky na špičce a patě, pokud chcete tech vázání.</li></ul>'
          '<p>Velikost se u skialpových bot udává v mondopointu, tedy délce chodidla v centimetrech. Při měření se řiďte tabulkou výrobce a zkoušejte boty odpoledne, kdy je noha lehce oteklá. Více v kategorii <a href="/skialpove-boty/">skialpové boty</a>. Dámské modely mají užší a nižší střih a jinak tvarovanou manžetu.</p>'
          '<h2>Vázání: tech, nebo rám</h2>'
          '<p>Nejrozšířenější jsou tech vázání, nazývaná také pin vázání. Používají se kovové čepy, které se zasouvají do vložek na botě. Jsou velmi lehká a efektivní při výstupu. Nevýhodou je menší opora při sjezdu a nutnost správného nastavení uvolnění při pádu. Rámová vázání připomínají klasická sjezdová, jsou těžší, ale pohodlnější a přenáší sílu stabilněji.</p>'
          '<ul><li><strong>Závodní tech:</strong> nejlehčí varianta, bez brzd a často s jedinou polohou výstupu.</li>'
          '<li><strong>Univerzální tech:</strong> s brzdou, dvěma polohami výstupu a nastavitelným uvolněním, vhodné na většinu túr.</li>'
          '<li><strong>Hybridní a rámové:</strong> těžší, pro freeridové túry a pro ty, kdo preferují jistotu před hmotností.</li>'
          '<li><strong>Brzda nebo leash:</strong> brzda zastaví lyži po vyskočení z vázání, pojistný popruh ji drží u nohy.</li></ul>'
          '<p>Montáž vázání patří do rukou servisu, protože špatná montáž znamená riziko při pádu. Více informací najdete v kategorii <a href="/skialpove-vazani/">skialpová vázání</a>.</p>'
          '<h2>Stoupací pásy</h2>'
          '<p>Pásy jsou z mohéru, nylonu nebo jejich směsi. Mohér klouže lépe a je lehčí, nylon vydrží víc a lépe se drží na strmém svahu. Směsné pásy kombinují obojí. Pásy se lepí na skluznici lepidlem, které časem slábne a je nutné ho obnovit. Pro přepravu se skládají lepivými stranami k sobě nebo se používají ochranné fólie.</p>'
          '<ul><li><strong>Šířka:</strong> pás má být o několik milimetrů užší než lyže, aby hrany zůstaly odkryté a lyže se mohla opřít o hranu.</li>'
          '<li><strong>Střih na míru:</strong> pásy se dají zkrátit nůžkami podle šířky lyží.</li>'
          '<li><strong>Lepidlo:</strong> v nabídce jsou lepidla v tubě na obnovení. Před nalepením plochu odmastěte.</li>'
          '<li><strong>Skladování:</strong> na suchém místě v obalu, aby lepidlo nepřijalo prach a vlhkost.</li></ul>'
          '<p>Další informace najdete v kategorii <a href="/skialpove-pasy/">skialpové stoupací pásy</a>.</p>'
          '<h2>Oblečení pro skialp</h2>'
          '<p>Při výstupu se zahřejete, ale na vrcholu a při sjezdu je zima. Oblečení se proto vrství a musí odvádět vlhkost. Základem je funkční spodní vrstva, která odvádí pot, druhá izolační vrstva a vrchní bunda, která chrání proti větru a sněhu. V nabídce se objevují i speciální kousky pro skialpinismus, například zateplené sukně a šortky z izolace Polartec a Primaloft, které zahřejí při zastávce a nebrání pohybu.</p>'
          '<ul><li><strong>Spodní vrstva:</strong> viz <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>, které rychle schne.</li>'
          '<li><strong>Izolace:</strong> lehká bunda nebo vesta do batohu pro zastávky.</li>'
          '<li><strong>Vrchní vrstva:</strong> prodyšná bunda a kalhoty z <a href="/lyzarske-bundy/">lyžařských bund</a> a <a href="/lyzarske-kalhoty/">lyžařských kalhot</a>.</li>'
          '<li><strong>Rukavice a čepice:</strong> dva páry rukavic, tenké na výstup a silnější na sjezd, viz <a href="/lyzarske-rukavice/">lyžařské rukavice</a>.</li></ul>'
          '<h2>Batoh a doplňky</h2>'
          '<p>Skialpový batoh má poutka na lyže, kapsu na lavinovou výbavu a prostor na vrstvy a svačinu. Důležité je, aby při nošení lyží nevyboulel a při sjezdu nelétal. Dále se hodí lavinový batoh s airbagem, i když ten nenahrazuje základní výbavu. Pomůckami jsou také ochranné kryty bot, pásky na pásy a opravárenský kit. V kategorii najdete i cepíny, mačky, úvazky a lopaty, které se používají při lezení na strmých traverzech nebo při záchranných akcích. Další batohy hledejte v kategorii <a href="/turisticke-batohy/">turistické batohy</a>.</p>'
          '<h2>Lavinová bezpečnost</h2>'
          '<p>Základem je lavinový vyhledávač, sonda a lopata, které se vždy nosí společně a každý člen skupiny je musí umět používat. Pečlivě sledujte lavinovou předpověď, plánujte trasu podle sklonu a expozice svahů a nikdy nechoďte sami do rizikového terénu. Absolvujte kurz u horské služby nebo licencovaného horského vůdce. Žádná výbava nenahradí znalosti, úsudek a ochotu otočit se, když podmínky nejsou dobré.</p>'
          '<h2>Výběr podle zkušeností</h2>'
          '<ul><li><strong>Začátečník:</strong> univerzální set lyží s vázáním, střední šířka a boty s dobrým pohodlím. Nepřeplácejte lehkost.</li>'
          '<li><strong>Pokročilý jezdec:</strong> lehké univerzální lyže, tech vázání s brzdou a tvarovatelné boty.</li>'
          '<li><strong>Závodník:</strong> závodní lyže, minimalistické vázání a lehké boty, které ukrojí gramy.</li>'
          '<li><strong>Freerider:</strong> širší lyže, stabilnější boty a vázání, ochota nést víc hmotnosti kvůli sjezdu.</li>'
          '<li><strong>Dámy:</strong> dámské boty s užší lýtkovou částí a lehčími lyžemi.</li></ul>'
          '<h2>Co v kategorii skutečně najdete</h2>'
          '<p>Kategorie sdružuje čtyři podkategorie, tedy lyže, boty, vázání a pásy, a navíc další zboží. Největší část tvoří značka Dynafit, dále Northfinder, Pomoca, Fischer, Wedze a Simond. Najdete tu i použité sety, skialpové sukně, šortky, legíny, úvazky, cepíny a mačky. Zboží ze sekce horolezectví najdete také v kategorii <a href="/horolezectvi/">horolezectví a ferraty</a>.</p>'
          '<h2>Péče o skialpovou výbavu</h2>'
          '<ul><li>Po túře lyže osušte, aby se nezačala tvořit koroze na hranách, a sundejte pásy.</li>'
          '<li>Pásy složte lepivými stranami k sobě nebo na ochrannou fólii a skladujte v suchu.</li>'
          '<li>Boty vyndejte botičky a nechte je vyschnout při pokojové teplotě.</li>'
          '<li>Vázání občas zkontrolujte, zda se v něm nenashromáždil led nebo nečistota.</li>'
          '<li>Skluznice nechte pravidelně namazat voskem, viz <a href="/lyzarske-vosky/">vosky a mazání</a>.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Porovnáváme nabídky českých obchodů u stejného modelu, zobrazujeme dostupné velikosti a odlišujeme výprodejové a použité kusy. U lyží ověřte délku a šířku, u bot mondopoint, u vázání kompatibilitu s botou a rozsah uvolnění. Při koupi použité výbavy si ověřte stav hran, skluznice a vázání.</p>',
    faq=[
        ('Co potřebuji na skialpinismus?', 'Skialpové lyže, boty s režimem chůze, tech nebo rámové vázání, stoupací pásy, hole, helmu, vrstvené oblečení a lavinovou výbavu v podobě vyhledávače, sondy a lopaty.'),
        ('Jaké vázání na skialp zvolit?', 'Tech vázání jsou lehká a efektivní při výstupu, rámová pohodlnější a stabilnější při sjezdu. Univerzální tech s brzdou je pro většinu túr nejlepší.'),
        ('Jak vybrat skialpové boty?', 'Podle velikosti v mondopointu, hmotnosti, tuhosti a rozsahu pohybu v režimu chůze. Musí být kompatibilní s typem vázání a zkoušet se odpoledne, kdy je noha lehce oteklá.'),
        ('Jakou délku skialpových lyží zvolit?', 'Obvykle od brady po čelo, lehčí a užší lyže bývají o něco delší. Závisí na terénu, váze jezdce a stylu.'),
        ('Jak dlouho vydrží lepidlo na stoupacích pásech?', 'Záleží na používání a skladování, ale po několika sezonách ztrácí přilnavost a je nutné ho obnovit. Pásy skladujte lepivými stranami k sobě nebo na fólii.'),
        ('Je lavinová výbava povinná?', 'Zákon ji obecně nepředepisuje, ale při pohybu v lavinovém terénu je vyhledávač, sonda a lopata základ. Bez znalosti jejího použití a lavinové předpovědi ale nestačí.'),
        ('Čím se liší skialpové boty od sjezdových?', 'Jsou lehčí a mají režim chůze, který uvolní manžetu pro přirozený krok. Sjezdové boty jsou tužší, ale nepoužívají se k výstupům.'),
        ('Mohu na skialp použít sjezdové lyže?', 'Se sjezdovým vázáním a botami se na skialp vyjít nedá, protože pata je pevně uchycená. Potřebujete vázání s uvolněnou patou, boty s režimem chůze a stoupací pásy a lehčí skialpové lyže výstup ještě usnadní.'),
        ('Jak pečovat o stoupací pásy?', 'Po túře je osušte, složte lepivými stranami k sobě nebo na ochrannou fólii a skladujte v suchu. Před lepením plochu odmastěte.'),
        ('Co je mondopoint?', 'Je to velikostní systém udávaný v centimetrech podle délky chodidla. U skialpových bot se používá a doplňuje se tabulkou výrobce.'),
    ],
)
