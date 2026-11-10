"""sporteka.cz — wave 20a (4. 11. 2026): long texts (>= 1650 words) for lyzarske-hole, skolni-batohy, hokejove-chranice, fotbalove-chranice-a-stulpny.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-hole
NEW['lyzarske-hole'] = dict(long=True,
    title='Lyžařské hole: sjezdové, běžecké, dětské i náhradní',
    desc='Lyžařské hole sjezdové, běžecké, skialpové i dětské. Jak zvolit délku, materiál, poutko a hrot a porovnat nabídky českých obchodů.',
    intro='<p>Hole vypadají jako nenápadný doplněk, přitom ovlivňují rytmus oblouků, rovnováhu v terénu i únavu ramen na konci dne. Sjezdař je používá k odrazu a načasování zatáčky, běžkař se jimi doslova odráží vpřed a skialpinista je střídavě zapichuje do svahu při stoupání a spouští je při jízdě dolů. '
          'Stejně jako u lyží proto neplatí, že jedny hole vyhovují všem: liší se délkou, materiálem, držadlem, poutkem i talířkem na hrotu.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u holí od značek Komperdell, Leki, Head, Rossignol, Swix, Atomic nebo Oneway, včetně juniorských, teleskopických a náhradních dílů. '
          'K výběru se hodí i <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/bezecke-lyze/">běžecké lyže</a>, <a href="/skialpinismus/">skialpinismus</a> a <a href="/lyzarske-rukavice/">lyžařské rukavice</a>. '
          'Níže najdete přehled typů, pravidla pro délku a rady, na co dát pozor při nákupu.</p>',
    guide='<h2>Jaké druhy lyžařských holí existují</h2>'
          '<p>Hole se dělí především podle disciplíny. Každá z nich klade jiné nároky na tuhost, váhu a tvar rukojeti, takže zaměnit je nelze bez kompromisů. '
          'Sjezdové hole jsou krátké a odolné, běžecké dlouhé a lehké, skialpové nastavitelné a vybavené velkým talířkem. Pro rodiny jsou důležité dětské modely, které se dají prodloužit s rostoucím lyžařem.</p>'
          + T(['Typ holí', 'Hlavní znak', 'Pro koho'], [
              ['Sjezdové hole', 'kratší, pevné, malý talířek', 'lyžování na sjezdovce a ve volném terénu'],
              ['Běžecké hole', 'dlouhé, lehké, šikmý nebo sklopný hrot', 'klasika i bruslení na stopě'],
              ['Skialpové a teleskopické hole', 'dva nebo tři díly, nastavitelná délka, velký talířek', 'stoupání a sjezd v nezpevněném terénu'],
              ['Dětské a juniorské hole', 'kratší, často s prodloužením', 'rostoucí lyžaři, kurzy a rodinné lyžování'],
              ['Náhradní díly', 'talířky, rukojeti, poutka, hroty', 'oprava poškozených holí']]) +
          '<p>Další tvar představují nordic walkingové a trekové hole, které se s lyžařskými pouze částečně překrývají. Pokud chcete hole využívat i v létě na túrách, projděte si kategorii <a href="/trekove-hole/">trekové hole</a>, protože mají jinou rukojeť a hrot a lépe zvládají kameny.</p>'
          '<h2>Jak vybrat správnou délku</h2>'
          '<p>Délka je nejdůležitější parametr a dá se ověřit jednoduchou zkouškou. Při sjezdovém lyžování se hůl obrátí a uchopí pod talířkem, předloktí pak mírně svírá s paží pravý úhel. U běžeckého lyžování se délka řídí stylem: klasika vyžaduje kratší hole, bruslení delší. '
          'Rozdíly mezi výrobci se liší o několik centimetrů, proto se opřete o tabulku konkrétní značky a o svou výšku.</p>'
          + T(['Disciplína', 'Orientační pravidlo', 'Poznámka'], [
              ['Sjezdové lyžování', 'výška těla krát přibližně 0,7', 'pro prudší terén spíš kratší'],
              ['Běžecká klasika', 'výška těla krát přibližně 0,83', 'konec hole sahá k podpaží'],
              ['Běžecké bruslení', 'výška těla krát přibližně 0,89', 'konec hole sahá k ústům nebo bradě'],
              ['Skialpinismus', 'nastavitelné, na výstup delší a na sjezd kratší', 'zámek musí držet při tlaku']]) +
          '<p>Hodnoty jsou jen přibližné a berou se jako východisko pro zkoušku v botách. Začátečníci a děti volí raději o něco kratší hole, protože se s nimi snáze drží vzpřímená poloha. Pokud váháte mezi dvěma délkami, vyberte kratší a použijte skupinu holí s nastavitelnou délkou.</p>'
          '<h2>Materiál: hliník, karbon a kompozit</h2>'
          '<h3>Hliníkové hole</h3>'
          '<p>Hliník je pevný, houževnatý a lacinější na výrobu. Při nárazu se ohne, ale většinou nepřeláme a hůl se dá narovnat. Jejich nevýhodou je vyšší hmotnost, která se projeví hlavně u dlouhých běžeckých tras. Pro rodinné lyžování a jízdu mezi stromy bývá hliník praktická a odolná volba.</p>'
          '<h3>Karbonové a kompozitní hole</h3>'
          '<p>Karbon je lehčí a lépe tlumí vibrace, což oceníte při dlouhých úsecích na běžkách. Pokud se hůl příliš ohne, může prasknout bez varování, proto se nehodí do ošklivých pádů a na tvrdou práci mezi kameny. Mezi hliníkem a karbonem leží kompozitní modely, které kombinují obě vlastnosti a bývají dostupné i pro menší rozpočet.</p>'
          '<h2>Rukojeť, poutko a talířek</h2>'
          '<p>Rukojeť má sedět do dlaně v rukavici, takže se hole zkouší i s rukavicemi na rukou. Plastová rukojeť je odolná a lehká, pryžová příjemnější na dotek, korková nejlépe saje pot a tlumí chlad. '
          'Poutko drží hůl na zápěstí a při odrazu přenáší sílu. Sjezdové modely mívají poutko s bezpečnostním uvolněním, aby se při zachycení o strom nebo o branku neúrazilo zápěstí. Na sjezdovce se poutko navléká, ale při jízdě mimo trať a ve skialpech se často používá bez poutka, aby se v případě laviny hole snadno sundaly. '
          'Talířek se volí podle sněhu: malý na tvrdé sjezdovky, větší na prašan a pro stoupání. Běžecké talířky mají asymetrický tvar a na hrotu bývá tvrdokov.</p>'
          '<h2>Výběr podle úrovně a typu lyžování</h2>'
          '<ul><li><strong>Rekreační lyžaři:</strong> stačí pevné hliníkové hole s pohodlným poutkem. Kombinujte je s <a href="/sjezdove-lyze/">lyžemi</a>, <a href="/lyzarske-boty/">botami</a> a <a href="/lyzarske-helmy/">helmou</a>.</li>'
          '<li><strong>Pokročilí a závodníci:</strong> lehčí, často zahnuté hole pro slalom a obří slalom, které při jízdě těsněji přiléhají k tělu.</li>'
          '<li><strong>Freeride:</strong> pevný materiál, větší talířek a poutko, které se při pádu rychle uvolní.</li>'
          '<li><strong>Běžkaři:</strong> lehký karbon nebo kompozit, specifická délka a odpovídající poutko. Doplňte je výbavou z oddílu <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</li>'
          '<li><strong>Skialpinisté:</strong> sklopné nebo teleskopické hole s dobrým zámkem, které se vejdou na batoh. Hledejte je mezi dalším vybavením v kategoriích <a href="/skialpove-lyze/">skialpové lyže</a> a <a href="/skialpove-pasy/">skialpové pásy</a>.</li></ul>'
          '<h2>Děti a juniory</h2>'
          '<p>Malé děti často lyžují bez holí, dokud nezvládnou základní oblouk. Hole pak zavádějí jako pomůcku pro rytmus a rovnováhu. Dětský model musí být lehký a mít měkké poutko. Mezi nabídkou najdete juniorské hole i modely s možností nastavení délky, které se hodí pro rychle rostoucí děti. '
          'Starší děti, které trénují v klubu, přecházejí na stejné konstrukce jako dospělí, jen kratší a lehčí. Přehled kompletní dětské výbavy najdete také v kategoriích <a href="/detske-lyze/">dětské lyže</a> a <a href="/lyze-komplety/">lyže komplety</a>.</p>'
          '<h2>Péče, oprava a výměna dílů</h2>'
          '<p>Po sezóně hole osušte, aby uvnitř trubky nezůstala voda, a uložte je rovně. Nenechávejte je opřené v kouti na dlouhé měsíce, hliníková hůl se může trvale prohnout. Teleskopické modely občas rozeberte, vyčistěte a mírně promažte, aby se zámek neseknul. '
          'Talířky, poutka a rukojeti se dají vyměnit samostatně, takže poškozená hůl nemusí skončit v koši. Hodí se to hlavně u kvalitnějších modelů, kde výměna dílu vyjde levněji než nová dvojice. '
          'Pokud vám při lyžování zamrzají zámky, použijte podle návodu výrobce vhodný lubrikant.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě příliš dlouhých holí „pro jistotu“, které brání v držení těla.</li>'
          '<li>Zkoušení bez rukavic, takže se rukojeť později ukáže jako malá.</li>'
          '<li>Použití běžeckých holí na sjezdovku, kde jsou na tvrdý odraz příliš křehké.</li>'
          '<li>Opotřebený nebo uvolněný talířek, kvůli kterému se hůl zapichuje příliš hluboko; talířek včas vyměňte.</li>'
          '<li>Navlékání poutka na zápěstí ve volném terénu a ve skialpech, kde se hole používají bez poutka; na sjezdovce bezpečnostní poutko samozřejmostí není.</li></ul>'
                    '<h2>Technika a hole: proč záleží na držení</h2>'
          '<p>Správné držení začíná tím, že ruku provlečete poutkem zdola a sevřete rukojeť i s poutkem. Takto se zápěstí opírá o poutko a prsty nemusí hůl křečovitě svírat. Při sjezdu se hůl nese mírně před tělem a lehce vpředu, lokty zůstávají u boků. '
          'Hole se zapichují jen drobným pohybem zápěstí, nikoli celou paží. Začátečníci hůlkami často mávají, což narušuje rovnováhu, takže si je v prvních dnech raději jen přidržují. '
          'U běžeckého lyžování se naopak hole zapichují šikmo dozadu a tlak se přenáší přes poutko, takže dobře padnoucí poutko je důležitější než samotná rukojeť.</p>'
          '<h2>Hole pro nordic walking a smíšené použití</h2>'
          '<p>Někteří zájemci hledají jedny hole na zimu i na léto. Pro rekreační použití to jde, ale mezi disciplínami zůstávají rozdíly. Zimní talířky jsou větší a pro suchou zem zbytečně překážejí, zatímco letní hroty se do sněhu zabořují. Pokud hole používáte během roku, seženete si raději náhradní talířky nebo druhou dvojici. '
          'Komplet výbavy lyžaře doplňuje i oděv, třeba <a href="/lyzarske-bundy/">lyžařské bundy</a> a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, a také <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, které udrží nohy v suchu.</p>'
'<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("komperdell", "Komperdell"), ("head", "Head"), ("leki", "Leki"), ("oneway", "Oneway"), ("rossignol", "Rossignol"), ("swix", "Swix"), ("atomic", "Atomic"), ("elan", "Elan")) +
          '. Další modely nabízejí ' + B(("arcore", "Arcore"), ("fizan", "Fizan"), ("alpina", "Alpina"), ("salomon", "Salomon"), ("viking", "Viking"), ("blizzard", "Blizzard"), ("gabel", "Gabel")) + '. '
          'Komperdell a Leki jsou typičtí pro teleskopické a skialpové hole, Swix pro běžecké, Oneway a Atomic pro sjezdové a freestylové.</p>'
          '<h2>Kompletní zimní výbava a nákup</h2>'
          '<p>Hole jsou jen jedním dílem sestavy. Na hory patří i <a href="/lyzarske-bryle/">lyžařské brýle</a>, <a href="/lyzarske-obleceni/">lyžařské oblečení</a>, <a href="/lyzarske-vazani/">vázání</a> a <a href="/lyzarske-vosky/">vosky</a>. Další nápady najdete v hlavním oddílu <a href="/zimni-sporty/">zimní sporty</a> a v doplňcích <a href="/lyzarske-doplnky/">lyžařské doplňky</a>. '
          'Nejvíc obchody zlevňují po sezóně a těsně před ní, kdy uvolňují sklady, a hole se starším vzorem se nemění funkčně, takže se vyplatí sledovat starší kolekce. Na Sportece vidíte nabídky obchodů vedle sebe a ověříte, kde jsou hole ve vámi vybrané délce skladem.</p>',
    faq=[
        ('Jak dlouhé lyžařské hole potřebuji?', 'U sjezdových holí vezměte hůl obráceně pod talířek a pokud je předloktí s paží v pravém úhlu, délka sedí. Orientačně jde o výšku těla krát 0,7. U běžeckých holí délka závisí na stylu, klasika potřebuje kratší hole než bruslení.'),
        ('Mohu používat sjezdové hole na běžky?', 'Technicky ano, ale nejsou k tomu stavěné. Jsou kratší, těžší a nemají tvar talířku určený pro odraz na stopě, takže se na delší trase unavíte rychleji.'),
        ('Jsou lepší hliníkové, nebo karbonové hole?', 'Záleží na stylu. Hliník je odolnější a jednodušší, při nárazu se ohne. Karbon je lehčí a lépe tlumí vibrace, ale při přetížení může prasknout, takže se hodí spíš na stopu než do ošklivých pádů.'),
        ('K čemu je bezpečnostní poutko?', 'U některých modelů se poutko při zachycení o překážku nebo o strom uvolní, aby se snížilo riziko zranění zápěstí a ramene. Při jízdě v lavinovém terénu se hole často používají zcela bez poutka.'),
        ('Mají děti jezdit s holemi?', 'Úplní začátečníci obvykle lyžují bez nich, aby se soustředili na rovnováhu. Hole se zavádějí, až dítě zvládne základní oblouk, a mají být lehké a o něco kratší než u dospělých.'),
        ('Jak velký talířek zvolit?', 'Malý talířek stačí na tvrdou sjezdovku a závodní lyžování. Do prašanu a při stoupání ve skialpech se hodí větší, který se tolik nezanořuje do sněhu.'),
        ('Dá se rozbitá hůl opravit?', 'Lehce ohnutou hliníkovou hůl lze obvykle narovnat, ale oslabené místo už nemusí vydržet. Talířky, poutka a rukojeti se dají vyměnit samostatně, přelomenou trubku většinou ne.'),
        ('Co jsou teleskopické hole?', 'Jsou složené z několika částí, které se zasouvají do sebe a zajišťují zámkem. Hodí se pro skialpinismus a pro rodiny, protože se dají přizpůsobit růstu dítěte nebo terénu a složit do batohu.'),
        ('Jak hole skladovat přes léto?', 'Osušte je, rozevřete teleskopické části a uložte je rovně na suchém místě. Zamezíte tak korozi uvnitř trubek a trvalému prohnutí hliníku.'),
        ('Mohu hole používat i na turistiku?', 'Lyžařské hole jdou v nouzi použít, ale mají talířek určený pro sníh a rukojeť pro rukavice. V létě je pohodlnější používat trekové hole s tvrdokovovým hrotem a gumovou botkou.'),
    ])

# ------------------------------------------------------------------ skolni-batohy
NEW['skolni-batohy'] = dict(long=True,
    title='Školní batohy: aktovky, batohy pro školáky a studenty',
    desc='Školní a studentské batohy, sady, penály, sáčky na obuv a svačinové boxy. Jak vybrat objem, zádovou část a velikost a porovnat obchody.',
    intro='<p>Školní batoh nosí dítě každý den celý rok, a to po schodech, v autobuse, na tělocvik i na výlet. Proto se nevybírá jen podle obrázku na klopě, ale především podle toho, jak sedí na zádech, kolik váží prázdný a zda vydrží tři roky bez rozedraných švů. '
          'Dobrý batoh má pevná záda, pevné popruhy a prostor pro sešity formátu A4, pro svačinu i pro láhev.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u školních batohů, aktovek, sad s penálem a sáčkem na cvičky i studentských batohů pro druhý stupeň a střední školu od značek Baagl, Oxybag, Vans, Fjällräven, Fila nebo Stil. '
          'Souvisí s nimi <a href="/batohy/">batohy</a>, <a href="/mestske-batohy/">městské batohy</a>, <a href="/turisticke-batohy/">turistické batohy</a> a <a href="/lahve-a-termosky/">láhve a termosky</a>. '
          'Níže najdete přehled typů, pravidla pro velikost a rady pro bezpečnost i péči.</p>',
    guide='<h2>Co všechno spadá do kategorie</h2>'
          '<p>Kromě klasických aktovek tu najdete i další věci, které děti do školy potřebují. Dobře fungují sady, protože jejich součásti spolu ladí a rodič nemusí řešit, zda se sáček na obuv hodí k batohu. '
          'Oblíbené jsou také ledvinky, svačinové boxy a tritanové láhve, protože se vejdou do kapsy a nezatěžují záda.</p>'
          + T(['Typ', 'Pro koho', 'Co nabízí'], [
              ['Školní aktovka s pevnými zády', 'prvňáčci a nižší stupeň', 'tuhé tvarované záda, reflexní prvky, držadlo'],
              ['Batoh pro druhý stupeň', 'žáci od zhruba čtvrté třídy', 'lehčí konstrukce, větší objem, kapsy na bočnici'],
              ['Studentský batoh', 'střední škola a univerzita', 'přihrádka na notebook, objemnější, městský vzhled'],
              ['Sada s penálem a sáčkem', 'rodiče, kteří chtějí jednotný vzhled', 'batoh, penál, sáček na obuv, někdy svačinový box'],
              ['Sáček na obuv a gymsack', 'tělocvik a kroužky', 'lehký vak na stahovací šňůrky'],
              ['Ledvinka, láhev, box', 'doplněk na cestu', 'svačina a pití bez zatížení zad']]) +
          '<p>Rozdíl mezi aktovkou a batohem není jen v názvu. Aktovka má pevnější dno i záda a ve tvaru drží stálý objem, zatímco měkký studentský batoh se přizpůsobí obsahu. U menších dětí se většinou doporučují pevná záda, starší děti už preferují lehčí a ohebnější materiál.</p>'
          '<h2>Velikost a objem</h2>'
          '<p>Batoh má sedět na zádech tak, aby jeho horní hrana nepřesahovala ramena a spodní část nesahala pod pas. Dítě nesmí být zatížené větším batohem, než jaký zvládne unést, a proto se vyplatí zkoušet. Objem se udává v litrech a zároveň je lepší porovnat rozměry s formátem A4, protože sešity a učebnice mají pevný tvar.</p>'
          + T(['Věk a ročník', 'Orientační objem', 'Co se vejde'], [
              ['předškoláci a školka', 'kolem 5 až 10 litrů', 'svačina, láhev, přezůvky'],
              ['1. až 3. třída', 'zhruba 15 až 20 litrů', 'sešity, penál, sáček na cvičky, svačina'],
              ['4. až 9. třída', 'zhruba 20 až 28 litrů', 'učebnice, pracovní sešity, sportovní věci'],
              ['střední škola a studium', 'zhruba 20 až 30 litrů', 'notebook, sešity, láhev, bunda']]) +
          '<p>Hodnoty jsou orientační. Podstatné je, aby se do batohu vešel pevný sešit A4 bez ohýbání a aby dítě po naložení nedržel nahrbeně. Vyplatí se také zeptat se v družině nebo ve škole, zda je zaveden systém skříněk, a nenosit učebnice zbytečně.</p>'
          '<h2>Záda, popruhy a bezpečnost</h2>'
          '<h3>Zádová část</h3>'
          '<p>Měla by být profilovaná, mírně polstrovaná a prodyšná. Pevná záda chrání zadní část těla před hranami sešitů, ale příliš tuhá konstrukce váží víc. Profilované pěnové pásy podél páteře zajistí proudění vzduchu, a tím i menší pocení.</p>'
          '<h3>Ramenní popruhy a hrudní pás</h3>'
          '<p>Popruhy mají být široké a měkké, s nastavitelnou délkou. Hrudní pás stáhne popruhy k sobě, aby neklouzaly z ramen, a bederní pás rozloží zátěž na boky u větších batohů. Děti se často pohybují v davu, proto je dobré zvolit batoh s reflexními prvky a výraznými barvami, které zvyšují viditelnost za šera.</p>'
          '<h3>Hmotnost naloženého batohu</h3>'
          '<p>Obecně se doporučuje, aby naložený batoh netvořil víc než zhruba 10–15 % tělesné hmotnosti dítěte; jde o orientační hodnotu a přesnější radu dají dětští lékaři a fyzioterapeuti. Prázdný batoh by proto měl být co nejlehčí a rodiče by měli pravidelně kontrolovat obsah. Častým viníkem jsou zapomenuté učebnice, láhve naplněné doplna a těžké penály.</p>'
          '<h2>Materiál, švy a zipy</h2>'
          '<p>Většina školních batohů se šije z polyesteru nebo nylonu s voděodolnou úpravou. Hustota tkaniny určuje odolnost proti oděru a promáčení. Dno bývá zesílené, aby batoh vydržel postavení na mokrou zem. '
          'Rozhodují detaily: dvojité švy v rozích, masivní zipy s delší jezdcem pro malé prsty, pružná kapsa na láhev a pevné pásky u poutek. Ekologické modely se vyrábějí z recyklovaného materiálu, jejich funkce je stejná, jen se změnilo složení tkaniny. Pokud batoh přijde do kontaktu s deštěm, hodí se pláštěnka nebo vrstva na dně.</p>'
          '<h2>Rozdělení vnitřku</h2>'
          '<p>Praktický batoh má hlavní prostor pro učebnice a sešity, menší přední kapsu pro penál a klíče a boční kapsy na láhev nebo deštník. Oddělená přihrádka na svačinu chrání sešity před mastnotou a zápachem. Pro starší žáky má smysl polstrovaná kapsa na notebook nebo tablet, která snese pád. '
          'Výhodné jsou také klasické vnitřní kapsy na mobil a kartu na oběd. U menších dětí se vyplatí vyšívané jmenovky a bezpečnostní poutko s kontakty, protože věci ve škole často zůstávají na chodbě.</p>'
          '<h2>Jak vybrat podle věku</h2>'
          '<ul><li><strong>Prvňáček:</strong> pevná aktovka s širokými popruhy, reflexními prvky a snadno otevíratelnými zipy, ke které se hodí sada s penálem a sáčkem na cvičky.</li>'
          '<li><strong>Druhý stupeň:</strong> lehčí batoh se zadní přihrádkou a kapsou na láhev. Děti už chtějí vlastní vzhled, proto se neváhejte zeptat, co se jim líbí.</li>'
          '<li><strong>Střední škola:</strong> městský batoh s polstrovanou kapsou na notebook, případně model blízký <a href="/mestske-batohy/">městským batohům</a>.</li>'
          '<li><strong>Sportovci:</strong> pro tělocvik a kroužky se hodí samostatný vak nebo <a href="/sportovni-tasky/">sportovní taška</a> a pro cesty tašky <a href="/tasky-pres-rameno/">přes rameno</a>.</li>'
          '<li><strong>Výlety:</strong> pro celodenní výlet nebo školu v přírodě zvolte menší <a href="/turisticke-batohy/">turistický batoh</a> s hrudním popruhem.</li></ul>'
          '<h2>Péče a údržba</h2>'
          '<p>Vysypte obsah alespoň jednou za týden, protože drobky, rozlité pití a zapomenutá svačina snadno zničí vnitřek. Většinu batohů lze ručně vyprat jemným prostředkem a nechat uschnout na vzduchu. Ne každý model snese pračku, takže se řiďte štítkem. '
          'Zipy po vyprání očistěte od písku a při tuhosti natřete svíčkou. Před koncem školního roku batoh nechte vyvětrat a uložte ho vycpaný papírem, aby neztratil tvar. Poškozený zip nebo prasklou přezku lze nechat opravit, než se vyhodí celý kus.</p>'
                    '<h2>Bezpečnost na cestě do školy</h2>'
          '<p>Batoh by měl dítě provázet i v dopravě, a proto má na bocích a vzadu reflexní plochy. Při čekání na přechodu se vyplatí, aby dítě mělo ruce volné a nemuselo nést tašky nebo sáček v ruce. Svačinu a láhev nejlépe uložit do bočních kapes, aby se nemusel prohrabávat celý batoh. '
          'Při cestě autobusem a tramvají se hodí batoh s úchytem na horní straně, aby se dal zvednout a podržet. Rodiče by měli dítěti vysvětlit, že batoh se nenosí přes jedno rameno, protože to zatěžuje záda nerovnoměrně, a že se neodkládá do uliček, na schody ani do průchodů, kde by o něj mohl někdo zakopnout.</p>'
          '<h2>Příslušenství k batohu</h2>'
          '<p>Praktický doplněk je sáček na obuv, který drží přezůvky mimo sešity a dá se pověsit na háček v šatně. Gymsack je podobný vak na stahovací šňůrky vhodný pro sportovní oblečení. Penál patří do předního oddílu, aby se tužky nepoškodily. '
          'Ledvinky se hodí na kapesné, klíče a mobil při zájmových kroužcích, a láhev s kvalitním víčkem zabrání vylití obsahu na učebnice. Přehled dalších praktických doplňků najdete v kategoriích <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/plastenky/">pláštěnky</a>, které se hodí za deště.</p>'
'<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("baagl", "Baagl"), ("oxybag", "Oxybag"), ("vans", "Vans"), ("fjallraven", "Fjällräven"), ("stil", "Stil"), ("fila", "Fila"), ("jordan", "Jordan")) +
          '. Další nabídku mají ' + B(("real-madrid", "Real Madrid"), ("willard", "Willard"), ("boll", "Boll"), ("tommy-hilfiger", "Tommy Hilfiger"), ("champion", "Champion"), ("4f", "4F"), ("bergans", "Bergans"), ("fc-barcelona", "FC Barcelona")) + '. '
          'Baagl a Oxybag se zaměřují na školní aktovky a sady pro mladší děti, Vans, Fjällräven a Tommy Hilfiger spíš na městské studentské modely.</p>'
          '<h2>Kdy kupovat a co sledovat</h2>'
          '<p>Nejvíc se prodává v srpnu a v září, kdy se výběr vyprodává a nové dětské vzory zmizí ze skladu. Chytřejší je nakoupit v červnu a v červenci nebo na konci zimy, kdy bývá nabídka široká a obchody rády uvolňují starší kolekce. '
          'U dětí stojí za to vzít batoh do ruky a nechat si ho nasadit, ideálně s učebnicemi. Pokud nakupujete online, sledujte možnost vrácení do čtrnácti dnů. Ze Sporteky se dostanete přímo do obchodů s nabídkou a uvidíte, kde je vámi vybraný vzor skladem. '
          'K batohu přibalte <a href="/lahve-a-termosky/">láhev nebo termosku</a>, případně <a href="/chladici-boxy/">chladicí box</a> na výlety.</p>',
    faq=[
        ('Jaký objem má mít batoh pro prvňáčka?', 'Většinou stačí kolem 15 až 20 litrů, hlavně aby se do něj vešel sešit A4 bez ohýbání. Důležitější než samotné litry je tvar a nízká váha prázdného batohu.'),
        ('Je lepší aktovka s pevnými zády, nebo měkký batoh?', 'Pro mladší děti bývá vhodnější tvarovaná aktovka s pevnými zády, která drží tvar. Starší žáci obvykle dávají přednost lehčímu a ohebnějšímu batohu, který se přizpůsobí obsahu.'),
        ('Jak těžký smí být naložený batoh?', 'Doporučení se liší, ale obecně se doporučuje, aby naložený batoh tvořil jen menší část tělesné hmotnosti dítěte. Prázdný batoh má proto vážit co nejméně a obsah se má pravidelně kontrolovat.'),
        ('K čemu je hrudní pás?', 'Stáhne ramenní popruhy k sobě, aby neklouzaly dolů, a rozloží zátěž. U menších dětí je užitečný hlavně při cestě pěšky a při větším objemu batohu.'),
        ('Kolik batohů potřebuje školák?', 'Obvykle stačí jeden hlavní batoh a lehký vak nebo sáček na přezůvky a tělocvik. Sportovní kroužky mají mít samostatnou tašku, aby se učební pomůcky nepotřely špínou.'),
        ('Jak batoh vyprat?', 'Vysypte ho a vyklepejte drobky. Pak ho ručně vyperte ve vlažné vodě s jemným prostředkem, důkladně vypláchněte a sušte na vzduchu mimo topení. Pračka není vhodná pro všechny modely, takže se řiďte štítkem.'),
        ('Jak poznám dobře sedící batoh?', 'Horní hrana nesmí přesahovat ramena a spodní hrana nemá sahat pod pas. Popruhy mají přiléhat bez tlaku na klíční kost a batoh nemá při chůzi ždímat dítě dozadu.'),
        ('Co jsou reflexní prvky a proč na nich záleží?', 'Jsou to plošky nebo pásky, které odrážejí světlo reflektorů a zvyšují viditelnost dítěte za šera. Při cestě ze školy nebo z družiny v zimě mají praktický význam.'),
        ('Hodí se studentský batoh i pro děti?', 'Starší děti od druhého stupně ho často používají, protože je lehčí a má jednoduchý tvar. Mladším dětem chybí pevná záda a bezpečnostní prvky aktovky, takže se hodí méně.'),
        ('Kdy je nejlepší doba na nákup?', 'Nejširší výběr bývá před sezónou a v létě, kdy jsou skladem všechny barvy. V září se oblíbené vzory často vyprodávají, proto se vyplatí nakupovat včas.'),
    ])

# ------------------------------------------------------------------ hokejove-chranice
NEW['hokejove-chranice'] = dict(long=True,
    title='Hokejová výstroj a chrániče: rukavice, kalhoty, lokty',
    desc='Hokejové chrániče loktů, holení a ramen, kalhoty, rukavice a suspenzory pro děti i dospělé. Jak vybrat velikost a střih a porovnat obchody.',
    intro='<p>Hokej je kontaktní hra a výstroj rozhoduje o tom, zda se po pádu postavíte, nebo odjedete s modřinou na dva týdny. Chrániče musí sedět přesně, nesmí omezovat pohyb a mají se obnovovat s tím, jak dítě roste. '
          'Kupují se postupně po částech nebo jako celek podle potřeby klubu a sezóny, ale vždy platí, že každá část musí na ostatní navazovat a překrývat se s nimi bez mezer.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u rukavic, kalhot, loktů, holení, ramen, krčních chráničů a suspenzorů od značek Bauer, Winnwell, CCM, Sherwood, Knapper nebo Warrior. '
          'Výběr doplňují <a href="/hokejove-helmy-a-mrizky/">hokejové helmy a mřížky</a>, <a href="/hokejove-brusle/">hokejové brusle</a>, <a href="/hokejky/">hokejky</a> a <a href="/hokejove-tasky/">hokejové tašky</a>. '
          'Níže najdete přehled jednotlivých částí, rady pro velikost a péči.</p>',
    guide='<h2>Z čeho se skládá hokejová výstroj</h2>'
          '<p>Pod dres a přes spodní vrstvu se nosí několik součástí, které se překrývají. Každá chrání jinou část těla a hráči ji pořizují v různém pořadí. '
          'Rukavice a helma jsou zpravidla první, kalhoty a ramena následují, holení a lokty doplní výbavu. Nezapomínejte na ochranu rozkroku a krku, která bývá nejčastěji opomíjená.</p>'
          + T(['Část výstroje', 'Co chrání', 'Na co dát pozor'], [
              ['Rukavice', 'prsty, zápěstí, hřbet ruky', 'délka manžety, prodyšnost, tvar dlaně'],
              ['Hokejové kalhoty', 'boky, kostrč, stehna', 'výška pasu, délka, nastavení'],
              ['Chrániče ramen a hrudi', 'klíční kost, hrudník, ramena', 'střih podle postavy, bez sevření'],
              ['Chrániče loktů', 'loket a předloktí', 'upevnění, tvrdost skořepiny, přesah rukavice'],
              ['Chrániče holení', 'kolena a holeně', 'délka podle holeně, přesah do brusle'],
              ['Suspenzor a kalhotky', 'oblast třísel', 'velikost, materiál, povinnost v lize'],
              ['Chránič krku', 'krk a hrdlo', 'povinnost v mládežnických soutěžích']]) +
          '<p>Brankářské vybavení je samostatné. Gola a masky najdete v kategorii <a href="/hokejove-brankarske-vybaveni/">hokejové brankářské vybavení</a>, protože se parametry i konstrukce výrazně liší od výstroje hráčů v poli.</p>'
          '<h2>Rukavice</h2>'
          '<p>Rukavice musí padnout tak, aby šlo pohodlně držet hokejku a zároveň zůstala ruka chráněná. Velikost se udává v palcích a má odpovídat délce od konečků prstů k zápěstí. '
          'Špičky prstů mají jen lehce dosedat na konec rukavice a dlaň by měla být pevná, ale ne tvrdá. Tvar se dělí na tradiční s širším vnitřkem a anatomický s užším střihem. '
          'Dětské rukavice jsou kratší a obvykle lehčí. Hráči si často volí rukavice podle toho, jak hrají: obránci dávají přednost větší ochraně hřbetu, útočníci cítí raději hokejku.</p>'
          '<h2>Kalhoty</h2>'
          '<p>Hokejové kalhoty chrání boky a kostrč a vyztužují stehna. Vybírají se podle pasu a délky nohavic: spodní hrana má sahat zhruba ke střední části kolen. Kalhoty se nosí volně uvázané v pase a držené šňůrkou, pásky nebo podvazky. '
          'Příliš krátké kalhoty nechávají nechráněná stehna, příliš dlouhé sklouzávají na lýtka a brání pohybu bruslí. Dospělé verze mají často prodyšnou síťku a vložky, které se dají vyjmout a vyprat.</p>'
          '<h2>Ramena, hrudník a lokty</h2>'
          '<h3>Chrániče ramen</h3>'
          '<p>Měkké i tvrdé skořepiny rozloží náraz na hrudní koš. Jsou k dispozici s vloženou ochranou páteře a s vestou pro mladší hráče. Při zkoušce zvedněte ruce nad hlavu a ověřte, že chránič nevyjíždí nahoru a netlačí na krk.</p>'
          '<h3>Chrániče loktů</h3>'
          '<p>Chránič musí zakrývat celý loket i část předloktí a při ohnutí nesmí klouzat. Tvrdá skořepina chrání před nárazem na mantinel, měkká pěna se hodí pro mladé hráče a hokejbal. Horní okraj má dosahovat k rukávu dresu a spodní zapadat pod manžetu rukavice, aby mezi nimi nezůstala mezera.</p>'
          '<h2>Holeně a kolena</h2>'
          '<p>Chránič holení má sahat od středu kolene po horní okraj brusle, tak aby bota na chránič zasahovala. Příliš dlouhý chránič tlačí na tkaničky, příliš krátký odkryje spodek holeně. '
          'Upevňuje se lepicí páskou nebo suchým zipem. Tvrdé skořepiny drží tvar a chrání při střelách, měkčí pěnové vložky nabízejí lepší komfort při tréninku. Chrániče pro hokejbal a inline hokej bývají lehčí a větrané, protože se hrají bez ledu.</p>'
          '<h2>Chránič krku a suspenzor</h2>'
          '<p>Krk nechrání helma ani ramena, a proto se v řadě mládežnických soutěží vyžaduje chránič krku nebo límec. Mívá ochranu proti proříznutí a měkkou podšívku. Suspenzor tvoří pevnou skořepinu s kalhotkami nebo páskem a při bruslení se nosí pod hokejové kalhoty. Pravidla soutěží se liší, proto si u trenéra ověřte, co se vyžaduje.</p>'
          '<h2>Jak určit velikost</h2>'
          '<p>Každá část se označuje jinak: rukavice palci, holeně palci, kalhoty a ramena podle obvodu a výšky. Označení Youth, Junior, Intermediate a Senior se používají jako hrubé vodítko, ale značky mají rozdílné střihy. '
          'Měřte pevným krejčovským metrem, srovnejte hodnoty s tabulkou výrobce a při nákupu online vyberte obchod s možností výměny. U dětí volte velikost, která sedí dnes, ne tu, která se „doroste“. Příliš velký chránič se při pádu posune a nechrání.</p>'
          + T(['Kategorie', 'Obvykle pro', 'Typické označení'], [
              ['Youth', 'nejmenší hráči', 'YTH, Y'],
              ['Junior', 'děti a mladší dorost', 'JR'],
              ['Intermediate', 'starší dorost a menší dospělí', 'INT'],
              ['Senior', 'dospělí', 'SR']]) +
          '<h2>Výběr podle úrovně a typu hokeje</h2>'
          '<ul><li><strong>Lední hokej, začátečníci:</strong> komplet výstroje v základní třídě, kde je důležitá hlavně správná velikost a pohodlí.</li>'
          '<li><strong>Pokročilí hráči:</strong> lehčí a anatomické konstrukce s lepším odvětráním a vícevrstvými skořepinami.</li>'
          '<li><strong>Hokejbal a street hockey:</strong> lehčí chrániče bez tvrdých skořepin, zejména rukavice, lokty a holeně. Nabídku najdete i v <a href="/hokejove-pasky-a-doplnky/">hokejových páskách a doplňcích</a>.</li>'
          '<li><strong>Florbal:</strong> je to jiná disciplína a vyžaduje jiné vybavení, proto zkuste <a href="/florbal/">florbal</a> a <a href="/florbalove-hole/">florbalové hole</a>.</li>'
          '<li><strong>Pozemní hokej:</strong> chrániče pro tento sport najdete v oddílu <a href="/pozemni-hokej/">pozemní hokej</a>.</li></ul>'
          '<h2>Péče a sušení</h2>'
          '<p>Výstroj po tréninku vyndejte z tašky a nechte vyschnout na větrání. Nedávejte ji na radiátor, protože pěna ztvrdne a lepidlo povolí. Rukavice se plní volným balonem papíru nebo se používají sušáky. '
          'Vložky z kalhot i chráničů se pravidelně perou ve vlažné vodě. Pot, který zůstane uvnitř, způsobuje zápach a postupně rozkládá materiál. Pro přenos se hodí větraná taška z kategorie <a href="/hokejove-tasky/">hokejové tašky</a>. '
          'Poškozené suché zipy a pásky lze vyměnit, popraskanou skořepinu raději nahradit novou.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě „na vyrůstání“, díky které se chránič při nárazu posune a odkryje kost.</li>'
          '<li>Zanedbání přechodu mezi díly, například mezi rukavicí a loktem.</li>'
          '<li>Použití starých chráničů po starším sourozenci bez kontroly stavu pěny.</li>'
          '<li>Podcenění krčního chrániče a suspenzoru, které nejsou vždy součástí kompletu.</li>'
          '<li>Rozhodování jen podle značky, ne podle toho, jak výstroj sedí.</li></ul>'
                    '<h2>Pořadí oblékání</h2>'
          '<p>Správné pořadí zrychlí přípravu a zabrání tomu, aby se chrániče posunuly. Nejprve si oblékněte spodní prádlo a termo vrstvu, poté suspenzor a ponožky. Pak následují kalhoty, holeně připevněné pod kolenem, brusle, chrániče loktů a ramena, dres, krční chránič, helma a nakonec rukavice. '
          'Trenéři učí děti oblékat se samostatně už od nejnižších kategorií, aby si zvykly na pořadí a věděly, kam který chránič patří. Ze začátku pomáhá fotografie nebo seznam v tašce a rodiče kontrolují, zda jsou suché zipy a pásky pevně utažené.</p>'
          '<h2>Spodní vrstva a pohodlí</h2>'
          '<p>Pod výstroj se nosí funkční spodní prádlo, které odvádí pot a zmírňuje tření. Bavlna zůstává vlhká a po zápase chladí, proto se nehodí. Přemýšlejte o <a href="/termopradlo/">termoprádle</a> a o <a href="/sportovni-ponozky/">sportovních ponožkách</a> s vyztuženou patou. '
          'Hodí se dlouhé hokejové ponožky, které se přetahují přes chrániče holení. Po tréninku se hodí osprchovat a převléknout, aby se neprochladilo tělo. Dětem se vyplatí do tašky přibalit ručník a láhev, třeba z kategorie <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>'
          '<h2>Kdy chrániče vyměnit</h2>'
          '<p>Výstroj se opotřebovává zejména na místech častého nárazu. Poznáte to na proděravělé tkanině, roztržených švech, slisované pěně a prasklé skořepině. Chránič, který po stlačení prstem nevrací původní tvar, už neabsorbuje náraz. '
          'Po silném zásahu, například po střele do holeně, je vhodné chránič zkontrolovat a případně vyměnit, i když není na pohled poškozený. Dobrá zpráva spočívá v tom, že drobné součásti jako suché zipy, pásky a šňůrky se dají vyměnit levně a výstroj pak vydrží další sezónu.</p>'
'<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("bauer", "Bauer"), ("winnwell", "Winnwell"), ("ccm", "CCM"), ("sherwood", "Sherwood"), ("knapper", "Knapper"), ("warrior", "Warrior")) +
          '. Další nabídku mají ' + B(("opus", "Opus"), ("dita", "Dita"), ("grays", "Grays"), ("arcore", "Arcore"), ("lasting", "Lasting"), ("tour", "Tour")) + '. '
          'Bauer, CCM a Warrior pokrývají širokou škálu od začátečníků po profesionály, Winnwell a Knapper jsou častou volbou pro mládež a hokejbal.</p>'
          '<h2>Jak nakupovat a skládat výbavu</h2>'
          '<p>Hlavní část nákupu připadá na začátek sezóny, ale chytré je kupovat dříve, protože oblíbené velikosti se rychle vyprodávají. Při doplňování výstroje porovnejte novou položku s tím, co už máte, a nenakupujte části z různých kategorií bez zkoušky. '
          'Pro celé vybavení se hodí i <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>, <a href="/hokejove-cepele-a-nasady/">čepele a nástavce</a> a <a href="/hokejove-puky-a-branky/">puky a branky</a>. '
          'Další nabídku sportovních potřeb dává oddíl <a href="/hokej/">hokej</a>. Na Sportece uvidíte nabídky obchodů vedle sebe a můžete rychle poznat, kde je vaše velikost skladem.</p>',
    faq=[
        ('Jaké chrániče musí mít hokejista povinně?', 'Povinnosti určuje soutěž a klub, ale obvykle jde o helmu s mřížkou, rukavice, chrániče loktů a holení, kalhoty a v mládeži i krční chránič. Ověřte si to u trenéra před nákupem.'),
        ('Jak vybrat velikost hokejových rukavic?', 'Změřte délku od konečků prstů po zápěstí a porovnejte s tabulkou výrobce. Špičky prstů mají jen lehce dosedat na konec rukavice a hokejka se musí dát držet bez tlaku.'),
        ('Jaké chrániče holení zvolit?', 'Ty, které sahají od středu kolene až k hornímu okraji brusle. Příliš dlouhé tlačí na tkaničky, příliš krátké nechrání holeň.'),
        ('Mohu používat chrániče po sourozenci?', 'Ano, ale pouze pokud sedí a pěna není slisovaná. Zkontrolujte švy, suché zipy a skořepinu. Chránič, který se při pohybu posouvá, nechrání.'),
        ('Jaký je rozdíl mezi hráčskou a brankářskou výstrojí?', 'Brankář nosí větší a tužší pláty, které kryjí celou nohu a hruď, a speciální masku. Hráčskou a brankářskou výstroj nelze zaměnit, protože brankář potřebuje větší ochranu.'),
        ('Jak dlouho vydrží hokejové chrániče?', 'Záleží na četnosti hraní a péči. Děti z nich obvykle vyrostou dřív, než se zničí. Dospělým vydrží několik sezón, dokud pěna drží tvar a švy nepraskají.'),
        ('Jak se starat o rukavice a chrániče?', 'Po tréninku je vyndejte z tašky a nechte vyschnout na vzduchu, ne na radiátoru. Vyjímatelné vložky pravidelně perte ve vlažné vodě.'),
        ('Je suspenzor povinný?', 'Pravidla závisí na soutěži. U mladších hráčů se obvykle doporučuje nebo vyžaduje a u dospělých bývá volitelný, ale většina hráčů ho nosí pro jistotu.'),
        ('Hodí se hokejová výstroj i na hokejbal?', 'Do určité míry ano, ale hokejbalové chrániče bývají lehčí a větrané, protože se hraje bez ledu. Pro hokejbal stačí často rukavice, lokty a holeně.'),
        ('Jak poznám správnou velikost kalhot?', 'Zadní hrana má pokrýt kostrč a spodní hrana má sahat zhruba ke středu kolene. Kalhoty se při bruslení nesmí zvedat ani sjíždět.'),
    ])

# ------------------------------------------------------------------ fotbalove-chranice-a-stulpny
NEW['fotbalove-chranice-a-stulpny'] = dict(long=True,
    title='Fotbalové chrániče a štulpny: holeně, ponožky, pásky',
    desc='Fotbalové chrániče holení, štulpny, ponožky a pásky pro děti i dospělé. Jak vybrat velikost, tvar a materiál a porovnat nabídky obchodů.',
    intro='<p>Chrániče holení jsou jedna z mála součástí fotbalové výbavy, kterou předepisují pravidla. Bez nich se na hřiště nesmí, a to ani při tréninku v nižších soutěžích. Štulpny je drží na místě, doplňují dres do barev týmu a chrání před studenými a mokrými nohama. '
          'Dobrá volba zkombinuje ochranu, pohodlí a správnou velikost, aby se chránič při běhu neposouval.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u chráničů holení, štulpen, ponožek a pásků od značek Puma, Adidas, Merco, Hejduk, Kipsta, Nike, Joma nebo Lotto. '
          'K výbavě se hodí <a href="/kopacky/">kopačky</a>, <a href="/fotbalove-mice/">fotbalové míče</a>, <a href="/brankarske-rukavice/">brankářské rukavice</a> a <a href="/dresy/">dresy</a>. '
          'Níže najdete přehled typů chráničů, pravidla pro velikost a rady pro péči.</p>',
    guide='<h2>Z čeho se skládá výbava pro nohy</h2>'
          '<p>Chrániče holení se obvykle nosí pod štulpnami a přes ponožky. Mezi nimi a kůží je tenká vrstva látky, která zabraňuje otěru a zachycuje pot. Podle pravidel je mají hráči zakrývat, takže štulpna musí chránič skrýt celý. '
          'V nabídce najdete samostatné chrániče, sady se štulpnami, štulpny s vloženým chráničem a pásky, které drží chránič na holeni.</p>'
          + T(['Položka', 'Úloha', 'Na co dát pozor'], [
              ['Chrániče holení', 'ochrana kosti před nárazy a kopy', 'velikost, tvrdost, tvar'],
              ['Štulpny', 'zakrytí chráničů, barva týmu, teplo', 'délka, materiál, rovnoměrné natažení'],
              ['Fotbalové ponožky', 'tlumení a komfort uvnitř kopaček', 'pružnost, švy, polstrování'],
              ['Pásky a návleky', 'upevnění chráničů na holeni', 'šířka, tahový tlak'],
              ['Chrániče s kotníky', 'ochrana holeně i kotníku', 'větší pohyblivost, pro mládež']]) +
          '<p>Hráči tvrdších zápasů mají chrániče s tvrdou skořepinou, zatímco děti a rekreační kopaná zvládnou lehčí modely z měkčí pěny. Bez ohledu na tvrdost musí chránič sedět na holeni a nesmí klouzat.</p>'
          '<h2>Typy chráničů holení</h2>'
          '<h3>Tvrdé skořepiny</h3>'
          '<p>Jde o pevný plastový nebo kompozitní kryt s měkkou vrstvou zespodu. Dobře rozloží náraz a hodí se do kontaktních zápasů. Jsou lehčí než dříve, ale ne tak ohebné jako měkké modely.</p>'
          '<h3>Měkké a gelové chrániče</h3>'
          '<p>Pěnové a gelové vložky vynikají pohodlím a bývají oblíbené u dětí. Chrání hůř před tvrdým úderem, proto se používají hlavně při trénincích a v nižších věkových kategoriích.</p>'
          '<h3>Chrániče s kotníkem</h3>'
          '<p>Jsou to chrániče s rozšířenou částí, která se přikládá ke kotníku. Hodí se pro mladé hráče, kteří potřebují stabilnější ochranu, ale komplikují nasazení kopaček. Hodí se pro malé děti, protože kotníková část drží chránič na místě a není třeba doplňovat pásku.</p>'
          '<h3>Chrániče s návlekem nebo páskou</h3>'
          '<p>Upevňují se pomocí pružného návleku nebo suchého zipu. Štulpna se přetahuje navrch, takže chránič zůstane zakrytý. V hale se používají lehčí modely, které se stejně kryjí štulpnami.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Chránič má sahat zhruba od vrchní hrany kopačky, resp. od kotníku, po spodní okraj kolena. Přečnívající chránič naráží do kolene a omezuje pohyb, příliš krátký odkrývá kost. Velikost se označuje buď centimetry, nebo písmeny S, M, L a XL. '
          'Změřte délku holeně od kotníku po kolenní jamku a porovnejte s tabulkou. U dětí kupujte velikost podle současné délky holeně, ne na vyrůstání, protože příliš velký chránič tlačí na koleno a špatně drží. Zkoušejte je přímo ve štulpnách a při pohybu.</p>'
          + T(['Věk hráče', 'Obvyklá velikost', 'Poznámka'], [
              ['předškolní děti', 'XS nebo S', 'chrániče s kotníkem'],
              ['mladší žáci', 'S až M', 'lehká skořepina nebo pěna'],
              ['starší žáci a dorost', 'M až L', 'tvrdší skořepina'],
              ['dospělí', 'L až XL', 'volba podle délky holeně']]) +
          '<h2>Štulpny: délka, materiál a střih</h2>'
          '<p>Štulpna je dlouhá ponožka bez chodidla nebo s chodidlem. Verze bez chodidla se nosí přes ponožku a chrání ji před otěrem. Celá štulpna s chodidlem je pohodlnější, ale po proděravění chodidla je třeba vyměnit celý kus. '
          'Materiál je obvykle směs polyamidu nebo polyesteru a elastanu. Měla by držet tvar, neklouzat a po praní nevytahovat. Pokud štulpny nedrží, pomůže páska nebo gumička, nikdy ne těsný obvaz, který by škrtil lýtko.</p>'
          '<p>Barvy a vzory se vybírají podle týmu. V oddílech se většinou kupují po sadách, a hromadné sady mívají omezený rozsah velikostí. Děti, které rostou, často volí štulpny o číslo větší. Při výběru štulpen sledujte především to, zda přes ně chránič neprosvítá a zda mají proti pocení prodyšnou síťku.</p>'
          '<h2>Hokejové štulpny v nabídce</h2>'
          '<p>V kategorii najdete také hokejové štulpny, které se nosí přes chrániče holení a brusle. Jsou delší a pevnější než fotbalové a mají tahovou gumu nebo suchý zip. Do hokejového prostředí patří i <a href="/hokejove-chranice/">hokejová výstroj a chrániče</a> a <a href="/hokejove-dresy-a-obleceni/">hokejové dresy a oblečení</a>. Pokud hrajete hokejbal, hodí se i <a href="/hokejove-pasky-a-doplnky/">pásky a doplňky</a>.</p>'
          '<h2>Výběr podle sportu a povrchu</h2>'
          '<ul><li><strong>Fotbal na trávě:</strong> standardní chrániče pod štulpnami, odolnější proti tvrdým střetům.</li>'
          '<li><strong>Umělá tráva a hala:</strong> lehčí chrániče a pásky, protože se hraje rychle a kontakt bývá menší. Pro halu patří vedle chráničů i <a href="/sportovni-obuv/">sportovní obuv</a>.</li>'
          '<li><strong>Děti a začátečníci:</strong> měkké chrániče s kotníkem a pohodlné štulpny. Pro trénink pomůže i <a href="/sportovni-ponozky/">sportovní ponožka</a>.</li>'
          '<li><strong>Brankáři:</strong> vedle chráničů holení zvažte chrániče kolen a loktů; rukavice najdete v kategorii <a href="/brankarske-rukavice/">brankářské rukavice</a>.</li>'
          '<li><strong>Rugby a americký fotbal:</strong> vyžadují jiné chrániče, které naleznete v kategorii <a href="/ragby-a-americky-fotbal/">rugby a americký fotbal</a>.</li></ul>'
          '<h2>Pravidla a bezpečnost</h2>'
          '<p>Podle pravidel fotbalu musí být chrániče holení zakryté štulpnami a mají být z vhodného materiálu s dostatečnou ochranou. Pokud chránič praskne nebo se zdeformuje, vyměňte ho. Rozhodčí má právo hráče bez chrániče nepustit na hřiště. '
          'Rodiče by měli děti naučit chrániče nasazovat před každým tréninkem, protože se na ně rychle zapomene. Poškození holeně u dětí patří mezi časté úrazy a chrániče výrazně sníží následky. Při bolesti holeně po zásahu se obraťte na lékaře; <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> jsou jen doplněk, ne náhrada vyšetření.</p>'
          '<h2>Péče o chrániče a štulpny</h2>'
          '<p>Chrániče po zápase osušte, otřete a nechte větrat. Netahejte je na radiátor, aby se nedeformovaly. Čas od času je umyjte vlažnou vodou a jemným mýdlem. Štulpny perte při 30 stupních naruby a nechte uschnout, nedávejte je do sušičky, ztrácejí pružnost. '
          'Před sezónou zkontrolujte pěnu uvnitř chrániče a vyměňte ji, když je slisovaná nebo roztržená. Drobné poškození gumy a švů se dá spravit nitěmi, ale deformovanou skořepinu raději vyhoďte.</p>'
                    '<h2>Jak chrániče správně nasadit</h2>'
          '<p>Nejprve oblékněte ponožku nebo spodní štulpnu a upravte ji tak, aby neměla záhyby. Potom přiložte chránič na přední stranu holeně, tak aby spodní okraj ležel nad kotníkem a horní pod kolenem. Teprve pak přetáhněte štulpnu a srovnejte ji až ke kolenu. '
          'Pokud používáte pásku, zafixujte chránič v horní a dolní části a netahejte ji příliš silně. Před nasazením kopaček zkontrolujte, zda chránič při pohybu kotníku neklouže. '
          'U dětí se vyplatí vyzkoušet chůzi a krátký běh doma, aby se ověřilo, že nic netlačí. Špatně nasazený chránič se po pár minutách otočí a vůbec nechrání.</p>'
          '<h2>Chrániče pro děti a mládež</h2>'
          '<p>Dětské chrániče bývají lehčí a menší, s měkčím okrajem a často s kotníkovou částí. Pro nejmenší kategorie nejsou pevné skořepiny tolik potřeba, důležitější je pohodlí, aby je děti neodhodily. Staršímu dorostu už se hodí tvrdší modely, protože hra je rychlejší a kontaktnější. '
          'Rodiče by měli dětem vysvětlit, že chránič není nepohodlná povinnost, ale součást výbavy, bez které se nenastupuje. Pomáhá společné nakupování: dítě si vybere vzor a barvu a chránič nosí rádo. '
          'Při výběru kopaček a ponožek nezapomínejte na rostoucí chodidlo, o které se stará kategorie <a href="/kopacky/">kopačky</a>.</p>'
          '<h2>Futsal, halový fotbal a trénink</h2>'
          '<p>V hale se hraje na tvrdém povrchu bez kopaček a chrániče musí sedět ještě pevněji. Hráči často používají lehké pásky nebo návleky, které se dají sundat, aby noha dýchala. Při tréninku bývá volba volnější, ale i tam je rozumné chránit holeň, protože ke kontaktu dochází hlavně při cvičných hrách a střelbě. '
          'Hodí se vedle toho <a href="/funkcni-trenink/">funkční trénink</a> a <a href="/treninkova-obuv/">tréninková obuv</a>.</p>'
'<h2>Značky v nabídce</h2>'
          '<p>Největší zastoupení mají ' + B(("puma", "Puma"), ("adidas", "Adidas"), ("merco", "Merco"), ("hejduk", "Hejduk"), ("kipsta", "Kipsta"), ("nidelo", "Nidelo"), ("nike", "Nike"), ("joma", "Joma")) +
          '. Další nabídku mají ' + B(("sherwood", "Sherwood"), ("lotto", "Lotto"), ("lerko", "Lerko"), ("umbro", "Umbro"), ("bauer", "Bauer"), ("acra", "Acra"), ("foul", "Foul")) + '. '
          'Merco, Hejduk a Nidelo nabízejí štulpny pro týmy a hokejové oddíly, Puma, Adidas a Nike navazují na dresy a kopačky.</p>'
          '<h2>Nákup a skládání výbavy</h2>'
          '<p>Při nákupu pro tým se vyplatí sjednotit barvu štulpen a velikost podle věkové kategorie. Chrániče se kupují vždy samostatně pro každého hráče, protože odpovídají jeho holeni. '
          'Oddělení fotbalu najdete také v kategorii <a href="/fotbal/">fotbal</a>, kde jsou i další potřeby. Výhodné bývají sady s chrániči, štulpnami a taškou, ale ověřte si, zda velikost opravdu odpovídá. Sporteka ukáže nabídky obchodů vedle sebe a rychle poznáte, kde je vaše velikost skladem.</p>',
    faq=[
        ('Musí mít fotbalista chrániče holení?', 'Ano, pravidla fotbalu je vyžadují a hráč bez nich nesmí nastoupit. Chrániče musí být zakryté štulpnami a mají poskytovat přiměřenou ochranu.'),
        ('Jak vybrat velikost chráničů holení?', 'Změřte holeň od kotníku po kolenní jamku a porovnejte s tabulkou výrobce. Chránič nesmí tlačit na koleno ani odhalovat kost nad kopačkou.'),
        ('Je lepší tvrdý, nebo měkký chránič?', 'Tvrdá skořepina chrání lépe při tvrdých střetech. Měkké a gelové chrániče jsou pohodlnější a hodí se pro děti nebo trénink.'),
        ('Co jsou chrániče s kotníkem?', 'Mají rozšířenou část, která kryje kotník, a drží sama na místě. Hodí se pro menší děti, ale kopačky se s nimi nasazují o něco hůř.'),
        ('Jak držet chrániče na místě?', 'Nejlépe pomocí štulpen, které je zakryjí a stáhnou. Pokud se přesto posouvají, použijte pružný návlek nebo pásky, ale netahejte je příliš silně, aby nesvíraly lýtko.'),
        ('Jak prát štulpny?', 'Perte je naruby ve vlažné vodě a nedávejte je do sušičky. Teplo a tření snižují pružnost a štulpny se rychleji vytahují.'),
        ('Jaký je rozdíl mezi štulpnou a ponožkou?', 'Štulpna je dlouhá a obvykle bez chodidla, takže se nosí přes ponožku nebo chránič. Ponožka má chodidlo a chrání nohu uvnitř kopačky.'),
        ('Hodí se hokejové štulpny na fotbal?', 'Nedoporučuje se. Jsou delší, pevnější a určené pro hokejové chrániče a brusle. Pro fotbal si vyberte fotbalové štulpny, které lépe drží a zakryjí chránič.'),
        ('Kdy chrániče vyměnit?', 'Když praskne skořepina, pěna se slisuje nebo se chránič přestane držet na holeni. U dětí se mění hlavně s růstem.'),
        ('Mohu používat stejné chrániče na fotbal i futsal?', 'Ano, ale v hale se často používají lehčí modely nebo pásky. Důležité je, aby sedly a nebránily pohybu.'),
    ])

NEW['hokejove-chranice']['faq'].append(('Kolik času zabere oblékání a jak ho zrychlit?', 'Začátečníkům to trvá i dvacet minut, zkušeným hráčům méně. Pomůže pevné pořadí, seznam v tašce a utažení všech suchých zipů ještě před vstupem na led, aby se chrániče nepřesouvaly při první rozcvičce.'))
NEW['fotbalove-chranice-a-stulpny']['faq'].append(('Mají se chrániče nosit i při tréninku?', 'Ano, doporučuje se to, protože ke kontaktu a zásahům holeně dochází i při cvičných hrách a střelbě. U dětí je dobré vést je k tomu, aby chrániče nasazovaly automaticky před každým tréninkem, ne jen před zápasem.'))
NEW['fotbalove-chranice-a-stulpny']['faq'].append(('Je normální, že se chránič otáčí na holeni?', 'Není, signalizuje to špatnou velikost nebo uvolněnou štulpnu. Vyzkoušejte menší chránič, zkontrolujte pružnost štulpny a případně přidejte pásku v horní a dolní třetině holeně.'))
NEW['skolni-batohy']['faq'].append(('Kdy je čas na výměnu batohu?', 'Když se zadní část prohnula, zipy se přestaly zavírat nebo popruhy ztratily polstrování. U rostoucích dětí se batoh často vymění při přechodu na druhý stupeň, protože se mění objem učebnic i velikost zad.'))
