"""sporteka.cz — wave 18b (4. 11. 2026): long texts (>= 1650 words) for lezecka-lana-a-karabiny, cyklo-svetla, cyklisticke-rukavice, masazni-pomucky.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lezecka-lana-a-karabiny
NEW['lezecka-lana-a-karabiny'] = dict(long=True,
    title='Lana, karabiny a ferraty: výběr a srovnání',
    desc='Lezecká lana, karabiny, expresky, ferratové sady a smyčky. Jak vybrat správný průměr lana a typ karabiny a na co dbát při bezpečném používání.',
    intro='<p>Kategorie <strong>lana, karabiny a ferraty</strong> sdružuje vybavení, které při lezení a na zajištěných cestách tvoří základ záchranného řetězce. Najdete tu dynamická i statická lana, '
          'karabiny různých tvarů a uzávěrů, expresky, smyčky a pásky, ferratové sety, ale také odlehčené pomocné karabiny na klíče a batohy, které k lezení vůbec nepatří. Právě tohle rozlišení je pro nákup nejdůležitější.</p>'
          '<p>Sporteka porovnává nabídku českých obchodů u stejné položky vedle sebe, takže snadno vidíte dostupnost délek, barev a variant. Do širšího oboru <a href="/horolezectvi/">horolezectví a ferrat</a> patří i '
          '<a href="/lezecke-boty/">lezecké boty</a> a <a href="/lezecke-sedaky-a-pomucky/">sedáky a pomůcky</a>. Dál rozebereme typy lan, karabin, výběr podle způsobu lezení, péči a chyby, kterým se vyhnout. '
          'Texty jsou jen obecným vodítkem; rozhodující jsou vždy pokyny výrobce a vaše zkušenosti nebo kurz s instruktorem.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Sortiment je pestrý a ne všechno, co vypadá jako karabina, je určeno k jištění osob. Proto nejdřív přehled skupin a toho, k čemu se používají.</p>'
          + T(['Skupina', 'K čemu slouží', 'Na co se zaměřit'], [
              ['Dynamická lana', 'jištění při lezení, lano se při pádu natahuje', 'průměr, délka, určení (jednoduché, polovičaté, dvojité)'],
              ['Statická lana', 'slaňování, výstupy po laně, zásahové práce, jeskyně', 'nízká tažnost, plášť, použití podle výrobce'],
              ['Karabiny HMS a jistící', 'jištění parťáka a spojení v kotvě', 'hruškovitý tvar, šroubovací nebo automatický uzávěr'],
              ['Lehké karabiny a expresky', 'postupové jištění na skále a v ledu', 'rovná a zahnutá brána, délka smyčky'],
              ['Smyčky, pásky, šňůry', 'kotvení, prodlužování, stavba stanovišť', 'šířka, materiál, nosnost uvedená výrobcem'],
              ['Ferratové sety', 'zajištění na zajištěných cestách', 'tlumič pádu, rozpětí ramen, karabiny s velkým otvorem'],
              ['Doplňkové karabiny', 'zavěšení věcí, tábořiště, pověsit lahev', 'neslouží k jištění lidí']]) +
          '<p>Základní pravidlo zní, že pro jištění osob se používá výhradně vybavení, které je k tomu výrobcem určeno a nese příslušné značení. Ozdobné či zavěšovací karabiny z hobbymarketu mohou vypadat podobně, ale nejsou určeny k nesení člověka. '
          'Značení na těle karabiny a na štítku lana ověřte při každém nákupu a před prvním použitím si přečtěte návod, který je součástí balení.</p>'
          '<h2>Lana: dynamická a statická</h2>'
          '<p>Dynamické lano je vyrobeno tak, aby se při zachycení pádu natáhlo a energii pohltilo. Statické lano se naopak natahuje minimálně a hodí se tam, kde se nepředpokládá pád, například ke slaňování nebo výstupu po laně. '
          'Obě skupiny se nesmějí zaměňovat; statické lano se k jištění lezce, který může odpadnout, nepoužívá. Uvnitř lana je jádro nesoucí zátěž a okolo něj plášť, který jádro chrání před otěrem a nečistotou.</p>'
          + T(['Typ dynamického lana', 'Princip', 'Typické použití'], [
              ['Jednoduché (single)', 'jedno lano prochází všemi jištěními', 'sportovní lezení, jištění shora, horské cesty'],
              ['Polovičaté (half)', 'dvě tenčí lana střídavě v jištění', 'klasické cesty s klikatou linií, delší výstupy'],
              ['Dvojité (twin)', 'dvě lana vždy společně v každém jištění', 'ledovcové túry, delší horské cesty']]) +
          '<p>Průměr a délka se volí podle toho, kam chodíte. Tenčí lano je lehčí a lépe prokluzuje, ale rychleji se otírá a bývá náročnější na jištění. Silnější lano je trvanlivější a vhodné pro začátečníky a pro výuku. '
          'U délky vezměte v úvahu výšku nejdelších cest, kde lezete, a kolik metrů potřebujete na spuštění. Obecně se nejčastěji používají lana kolem šedesáti metrů, ale to je jen orientační údaj a vždy rozhoduje konkrétní terén. '
          'Značky, které v kategorii najdete, jsou například ' + B(('beal', 'Beal'), ('edelrid', 'Edelrid'), ('petzl', 'Petzl'), ('singing-rock', 'Singing Rock')) + '.</p>'
          '<h3>Úprava a ochrana lana</h3>'
          '<p>Lano je nutné chránit před otěrem, chemikáliemi a vlhkostí. Na skále se používá plachta nebo lanový vak, který zabrání zašpinění a přenášení kamínků do pláště. '
          'Praní provádějte jen podle návodu výrobce a nikdy nepoužívejte agresivní čisticí prostředky. Skladujte vcelku, v suchu, mimo slunce a mimo výpary z akumulátorů nebo rozpouštědel. '
          'Pokud lano zažilo větší pád, má poškozený plášť, je v něm tuhé místo nebo výrazně změnilo průměr, přestane se používat a pořídí se nové. Při pochybnostech nikdy nezkoušejte, jestli ještě „vydrží“.</p>'
          '<h2>Karabiny: tvary a uzávěry</h2>'
          '<p>Karabina je kovový oválný nebo D-profilový prvek s pohyblivou bránou. Při výběru sledujte tvar, typ uzávěru, otvor brány a hmotnost. Tvar ovlivňuje, jak je zatížení rozloženo. '
          'Karabina je nejpevnější ve směru hlavní osy při zavřené bráně, takže není vhodné ji zatěžovat napříč nebo s otevřenou bránou.</p>'
          + T(['Typ karabiny', 'Vlastnost', 'Typické použití'], [
              ['HMS (hruškovitá)', 'široká na jedné straně, vejde se do ní jistící prvek i uzel', 'jištění, slaňování, stanoviště'],
              ['Symetrická D', 'pevná, kompaktní, menší vnitřní prostor', 'expresky, smyčky, kotvy'],
              ['Karabina na expres s rovnou bránou', 'snazší zavěšení do nýtu', 'spodní konec expresky'],
              ['Karabina se zahnutou bránou', 'snadné zacvaknutí lana', 'horní konec expresky'],
              ['Karabina s velkým otvorem', 'snadná manipulace v rukavicích', 'ferrata, stanoviště, horské cesty']]) +
          '<p>Uzávěr může být bez pojistky, šroubovací, nebo automatický dvoufázový. Šroubovací je jednoduchý a spolehlivý, ale je třeba na něj nezapomenout. '
          'Automatický uzávěr se zavře sám a snižuje riziko, že zůstane otevřený, ale může se zaseknout v písku a ledu. V každém případě se brána kontroluje po každém použití a spolu s partnerem se provádí vzájemná kontrola před výstupem.</p>'
          '<p>Vhodné karabiny a komplety najdete mezi nabídkou značek ' + B(('ocun', 'Ocún'), ('edelweiss', 'Edelweiss'), ('petzl', 'Petzl')) + '. Porovnávejte nejen hmotnost, ale i tvar brány a kvalitu uzávěru.</p>'
          '<h2>Expresky, smyčky a pásky</h2>'
          '<p>Expresky tvoří dvojice karabin spojená krátkou smyčkou. Ve sportovním lezení se používá krátká smyčka, protože ušetří výšku a drží pohromadě. Dlouhé prodloužení se hodí pro klikatou linii, aby lano netřelo o hranu. '
          'Při výběru zkontrolujte, zda smyčka drží karabinu v poloze, která usnadňuje cvaknutí. Smyčky a pásky se vyrábějí z různých materiálů; materiály se liší hmotností, pevností a odolností vůči otěru, a proto je vždy čtěte na štítku. '
          'Uzel na smyčce nebo pásku sníží pevnost, kterou udává výrobce pro nezavázaný pásek, proto dodržujte pokyny k používání uzlů.</p>'
          '<h2>Ferratové sety a zajištěné cesty</h2>'
          '<p>Via ferrata je trasa vybavená ocelovým lanem, stupačkami a žebříky. Ferratový set slouží k zajištění lezce na ocelovém laně a musí obsahovat tlumič pádu. '
          'Zvláštní lano s obyčejnými karabinami ho nenahradí, protože při pádu by na tělo působily nebezpečné síly. Set se skládá z lana s tlumičem, dvou ramen s karabinami a často i z dalších prvků, které se uvedou v návodu.</p>'
          '<ul><li>Používejte jen set, který odpovídá hmotnosti, uvedené výrobcem, a velikosti sedáku.</li>'
          '<li>Při přestupu mezi úseky musí být vždy zacvaknuté aspoň jedno rameno.</li>'
          '<li>Postupujte podle návodu výrobce setu a nikdy nezatěžujte ramena způsobem, který návod nepopisuje.</li>'
          '<li>Děti a začátečníci patří na lehké trasy s dohledem zkušeného dospělého.</li></ul>'
          '<p>K ferratám patří <a href="/lezecke-sedaky-a-pomucky/">sedák</a>, přilba a pevné boty. Pro přístupovou cestu poslouží <a href="/turisticke-batohy/">turistický batoh</a> a v zimě i <a href="/sportovni-rukavice/">rukavice</a>, které chrání dlaně před ocelovým lanem.</p>'
          '<h2>Výběr podle způsobu lezení</h2>'
          '<h3>Sportovní lezení na skále a v hale</h3>'
          '<p>Nejčastěji se používá jedno dynamické lano, sada expresek a jistící karabina s jistícím prvkem. Pro začátečníky je lepší mírně silnější lano, které déle vydrží. Expresky nakupujte raději v kompletní sadě, aby sedělo vybavení k sobě.</p>'
          '<h3>Vícedélkové a horské cesty</h3>'
          '<p>Přibývají smyčky, pásky, vlastní jištění a často polovičatá lana. Důležitá je hmotnost celé sestavy, protože nesete všechno na zádech. Ale lehčí neznamená bezpečnější; tenčí lano vyžaduje zkušenost.</p>'
          '<h3>Ferraty a turistické zajištěné cesty</h3>'
          '<p>Stačí ferratový set, sedák a přilba. Vybavení je jednoduché, ale chyby se tady trestají stejně jako při lezení. Pokud nevíte, jak set správně používat, zúčastněte se kurzu u kvalifikovaného instruktora.</p>'
          '<h2>Časté chyby při nákupu a používání</h2>'
          '<ul><li><strong>Dekorativní karabina místo jistící.</strong> Značení a certifikace patří na tělo karabiny.</li>'
          '<li><strong>Lano bez ochrany.</strong> Šlapání po laně a pískový podklad zkracují jeho život.</li>'
          '<li><strong>Zapomenutá kontrola uzávěru.</strong> Šroubovací brána se sama nezavře.</li>'
          '<li><strong>Použité vybavení neznámého původu.</strong> Historii zátěže nelze z pohledu poznat.</li>'
          '<li><strong>Neověřená kompatibilita.</strong> Jistící prvek, lano a karabina se mají k sobě hodit.</li>'
          '<li><strong>Přeceňování vlastních sil.</strong> Kurz a zkušený parťák nejsou luxus.</li></ul>'
          '<h2>Životnost a kontrola vybavení</h2>'
          '<p>Textilní součásti stárnou i ve skříni vlivem světla, vlhkosti a chemikálií. Výrobci proto uvádějí maximální dobu používání a skladování; najdete ji v návodu. Karabiny prohlédněte kvůli zářezům, ostrým hranám nebo ztuhlé bráně. '
          'Pohyblivé části karabin lehce promažte podle pokynů výrobce, nikdy agresivními oleji. Vybavení, které spadlo z velké výšky nebo má trhliny či deformace, se vyřazuje. U vybavení, které by mohlo mít skryté poškození, je lepší nic neriskovat.</p>'
          '<h2>Co s sebou kromě lan a karabin</h2>'
          '<p>Při lezení se hodí <a href="/celovky-a-svitilny/">čelovka</a>, když se vracíte za šera, a <a href="/outdoorove-noze-a-multitoola/">multitool</a> nebo nůž na řezání smyček v nouzi. Kdo přespává pod skálou, ocení <a href="/turisticke-stany/">turistický stan</a> z kategorie <a href="/kemping/">kemping</a>. '
          'Na tejpování a ochranu kloubů slouží <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>. Pomocný výběr drobností najdete v kategorii <a href="/outdoor-doplnky/">outdoor doplňky</a> a v širší nabídce <a href="/outdoor/">outdooru</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Filtrujte podle značky a typu, otevřete detail produktu a porovnejte nabídky různých obchodů. U lan ověřte délku, průměr a typ, u karabin uzávěr a tvar a u setů velikost. '
          'Před platbou si přečtěte popis na stránce obchodu a při nejasnostech se zeptejte prodejce, protože u bezpečnostní výbavy je lepší zeptat se dvakrát. Při nákupu pro děti nebo začátečníky zvažte kurz, kde vám instruktor vybavení vysvětlí a vyzkoušíte si ho pod dohledem.</p>',
    faq=[
        ('Jaký je rozdíl mezi dynamickým a statickým lanem?', 'Dynamické lano se při pádu natáhne a pohltí část energie, a proto slouží k jištění lezce. Statické lano se téměř netáhne a používá se ke slaňování, výstupu po laně nebo k manipulaci s břemeny, nikoli k jištění pádu lezce.'),
        ('Jaký průměr lana si vybrat na začátek?', 'Začátečníkům se obecně doporučuje silnější jednoduché lano, protože déle vydrží a lépe se s ním jistí. Konkrétní doporučení najdete v návodu výrobce a nejlépe ho probrat s instruktorem nebo zkušeným lezcem.'),
        ('Kolik metrů lana potřebuji?', 'Odvíjí se od nejdelší cesty, na kterou chcete lézt, a od toho, kolik lana potřebujete na spuštění dolů. Zjistěte délku cest v průvodci a připočítejte rezervu; nejčastěji se na sportovní lezení používají lana kolem šedesáti metrů.'),
        ('Jak poznám, že karabina je určena k jištění?', 'Na těle karabiny je vyražené značení, údaje o pevnosti a certifikace. Karabina bez takového označení, třeba ozdobná na klíče, k jištění osob určena není. Údaje si vždy ověřte u výrobce.'),
        ('Je lepší šroubovací, nebo automatický uzávěr?', 'Záleží na použití. Šroubovací je jednoduchý a spolehlivý, ale uživatel ho musí sám zavřít. Automatický zvyšuje komfort, ale může se zanášet pískem. Ať zvolíte jakýkoli, vždy kontrolujte, že je brána zavřená.'),
        ('Jak dlouho lano vydrží?', 'Dobu nelze obecně určit, závisí na intenzitě používání, pádech, skladování a čištění. Výrobci uvádějí maximální dobu v návodu. Lano s poškozeným pláštěm nebo tuhým místem se přestává používat bez ohledu na stáří.'),
        ('Jak lano správně skladovat?', 'Čisté a suché, volně složené nebo v lanovém vaku, mimo přímé slunce a chemikálie. Neskladujte ho v autě, kde teplota kolísá, ani vedle akumulátorů, rozpouštědel a barev.'),
        ('Mohu na ferratu použít obyčejné lano a karabiny?', 'Ne. Ferratový set má tlumič pádu, který snižuje sílu působící na tělo. Obyčejné lano se dvěma karabinami by tuto funkci neplnilo a při pádu hrozí vážné zranění. Používejte jen k tomu určený set.'),
        ('Kdy vybavení vyřadit?', 'Pokud vykazuje poškození, špatně fungující uzávěr, trhliny, deformace, nebo po velkém pádu, případně když uplyne doba životnosti, kterou výrobce stanovil. Nelze-li o stavu rozhodnout, nahraďte kus novým.'),
        ('Mám kupovat použité vybavení?', 'Raději ne. U použitých lan a smyček neznáte historii zatížení, a to se zvenku často nepozná. U bezpečnostního vybavení je jistota původu důležitější než úspora.'),
        ('Potřebuji kurz, než začnu lézt s lanem?', 'Rozhodně se doporučuje. Práce s lanem a jištění se učí pod vedením kvalifikovaného instruktora nebo v lezecké škole, protože chyby v technice mohou mít vážné následky.'),
    ])

# ------------------------------------------------------------------ cyklo-svetla
NEW['cyklo-svetla'] = dict(long=True,
    title='Světla na kolo: přední, zadní a sady',
    desc='Světla na kolo přední i zadní, USB nabíjecí a na baterie. Jak vybrat svítivost, režimy, uchycení a sadu pro město, silnici i terén.',
    intro='<p>Dobrá světla na kolo rozhodují o tom, zda vás řidiči včas uvidí a zda vy sami uvidíte na cestu. V kategorii <strong>světla na kolo</strong> najdete přední i zadní svítilny, sady, '
          'světla na přilbu a řídítka, nabíjecí modely přes USB i varianty na baterie. Liší se svítivostí, režimy svícení, odolností proti vodě, způsobem upevnění a dobou provozu.</p>'
          '<p>Sporteka porovnává nabídku českých obchodů a u stejného světla ukáže, kde je skladem. Doplňkem jsou <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>, odrazky a <a href="/cyklisticke-helmy/">helmy</a>, '
          'celé téma zastřešuje <a href="/cyklo-prislusenstvi/">příslušenství pro kola</a>. Níže vysvětlíme, jaký typ světla se hodí do města, na silnici i do lesa, jak číst údaje na krabičce a čeho se vyvarovat.</p>',
    guide='<h2>Typy světel na kolo</h2>'
          '<p>Světla se dělí podle pozice, určení a způsobu napájení. Než začnete porovnávat konkrétní kusy, ujasněte si, kde a kdy budete jezdit nejčastěji.</p>'
          + T(['Typ světla', 'Hlavní úkol', 'Pro koho'], [
              ['Přední svítilna do města', 'být vidět a ukázat směr jízdy', 'denní dojíždění po osvětlených ulicích'],
              ['Přední svítilna s vyšším výkonem', 'osvětlit cestu mimo veřejné osvětlení', 'silniční i gravelová jízda za šera, trénink'],
              ['Světlo do terénu', 'silný kužel světla, často uchycení na řídítka i helmu', 'noční jízda na horském kole'],
              ['Zadní světlo', 'označit cyklistu vzadu, často s blikáním', 'všechny jezdci, bez výjimky'],
              ['Sady přední a zadní', 'komplet na jedno nabíjení', 'začátečníky a běžné používání'],
              ['Dynamo a náboj', 'světlo bez baterie', 'cestovatelé a ti, kdo jezdí denně']]) +
          '<p>Přední světlo má kolo osvětlovat, zadní je určeno k označení. Pokud jezdíte jen po městě, stačí slabší světlo, které vás zviditelní. Jakmile vyjedete z osvětleného prostoru, potřebujete výkonnější kužel, který ukáže výmoly a překážky. Kolo je ve tmě v mnohem horší situaci než auto, proto se vyplatí nešetřit na kvalitě.</p>'
          '<h2>Svítivost a jak ji číst</h2>'
          '<p>Na obalu najdete údaj v lumenech. Je to míra světelného toku vyzařovaného zdrojem, ale ne to, kolik světla skutečně dopadne na vozovku. O tom rozhoduje také optika, tedy tvar čočky a reflektoru. '
          'Dvě světla se stejným číslem mohou svítit zcela jinak: jedno vytvoří široký rovnoměrný kužel, druhé úzký a ostrý paprsek. Při porovnávání dbejte i na to, že výrobci uvádějí maximum, které svítí jen krátkou dobu, a nikoli to, co světlo vydrží celou jízdu.</p>'
          + T(['Využití', 'Orientační přístup k výkonu'], [
              ['Viditelnost ve městě', 'stačí nižší výkon s dobrým rozptylem'],
              ['Silniční jízda mimo osvětlené úseky', 'střední výkon s kuželem zaměřeným dopředu'],
              ['Gravel a lesní cesty', 'vyšší výkon a široký kužel'],
              ['Noční horská kola', 'nejvyšší výkon, často dvě světla (řídítka a helma)']]) +
          '<p>Obecně platí, že čím rychleji jedete a čím temnější je terén, tím víc světla potřebujete. Nezapomeňte však, že oslňování ostatních účastníků provozu je nebezpečné. Světlo na silnici se nastavuje mírně dolů, aby nesvítilo protijedoucím do očí.</p>'
          '<h2>Režimy svícení</h2>'
          '<p>Většina světel nabízí několik režimů: stálé světlo ve vyšší a nižší intenzitě, blikání, pulzování a úsporný režim. Blikání zvyšuje pozornost okolí, ale na tmavé silnici může ztížit odhad vzdálenosti a rychlosti. '
          'Proto se přední světlo často používá ve stálém režimu a zadní v pulzujícím, případně obojí podle pravidel platných ve vaší zemi. Světla s režimem automatického přizpůsobení podle okolního světla ocení ti, kdo nechtějí ovládat tlačítko za jízdy. Režim s pamětí si pamatuje poslední nastavení.</p>'
          '<h2>Napájení: USB, baterie, dynamo</h2>'
          '<p>Většina dnešních světel má vestavěný akumulátor, který se nabíjí kabelem USB. Je to praktické a levné na provoz, jen je třeba nezapomenout dobít před jízdou. '
          'Varianty na výměnné baterie jsou užitečné na delší výlety, kde není kde nabíjet. Dynamo v náboji kola dodává proud po celou dobu jízdy a světlo svítí i po zastavení díky kondenzátoru. Takové řešení se hodí pro dojíždění nebo cestování, kde nechcete myslet na nabíjení.</p>'
          '<ul><li><strong>USB akumulátor:</strong> pohodlný, často s indikací stavu nabití.</li>'
          '<li><strong>Tužkové baterie:</strong> snadno vyměnitelné, ale produkují odpad.</li>'
          '<li><strong>Externí baterie:</strong> pro dlouhé noční jízdy s výkonným světlem.</li>'
          '<li><strong>Dynamo:</strong> bez nabíjení, vyžaduje kompatibilní svítilnu a elektroinstalaci.</li></ul>'
          '<p>Doba provozu se udává pro konkrétní režim. Údaj pro nejsilnější režim bývá kratší, než byste čekali, takže si vždy přečtěte tabulku výrobce. Za mrazu kapacita akumulátoru klesá, proto pro zimní jízdu počítejte s rezervou.</p>'
          '<h2>Upevnění a kompatibilita</h2>'
          '<p>Světlo musí držet pevně i při jízdě po hrbolech. Nejčastěji se upevňuje gumovou páskou nebo plastovou objímkou na řídítka, zadní světlo na sedlovku nebo sedlový rámeček. Silikonové pásky jsou rychlé, ale časem se rozpínají. Pevná objímka se šroubem je spolehlivější. '
          'Světla pro terén se často dají přichytit na helmu, takže svítí tam, kam se díváte. Před nákupem zkontrolujte průměr řídítek a sedlovky; u aerodynamických tvarů budete potřebovat speciální držák. '
          'Zadní světlo nesmí být zakryté brašnou, pláštěnkou ani batohem. Pokud na kole vozíte <a href="/cyklo-tasky-a-nosice/">tašky a nosiče</a>, přidejte světlo na místo, které nebude zakryté.</p>'
          '<h2>Odolnost proti vodě a povětrnosti</h2>'
          '<p>Světlo, které selže v dešti, je k ničemu. Na krabičce hledejte údaj o krytí, nejčastěji ve tvaru IPX a číslice. Vyšší číslice znamená odolnost vůči silnějším vlivům vody, ale test se provádí za laboratorních podmínek. '
          'Praktický význam je prostý: pokud jezdíte v každém počasí, hledejte přesně označené krytí a neoteklé vstupy. Po jízdě v dešti světlo otřete a USB port nechte oschnout dříve, než ho nabijete. Ve sněhu a bahně pomáhá robustní tělo z hliníku nebo odolného plastu.</p>'
          '<h2>Pravidla provozu a bezpečnost</h2>'
          '<p>Za snížené viditelnosti musí mít kolo funkční přední a zadní světlo i odrazky. Konkrétní požadavky najdete v zákoně o provozu na pozemních komunikacích; platí, že přední světlo má být bílé a zadní červené. '
          'Pro vlastní bezpečnost se vyplatí jezdit se světly i ve dne, zvlášť na rychlých silnicích a v tunelech. Zadní světlo se nasazuje tak, aby bylo vidět z odstupu, a zkontrolujte ho před každou jízdou. '
          'Světlo nikdy nepovažujte za náhradu opatrnosti. Doplňte ho <a href="/cyklisticke-bundy-a-vesty/">vestou s reflexními prvky</a> a <a href="/cyklisticke-helmy/">přilbou</a>, která je pro děti v ČR povinná.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<h3>Město a dojíždění</h3>'
          '<p>Stačí lehké světlo s širším rozptylem a zadní světlo s pulzováním. Praktický je rychlý držák, který se snadno sundá, aby světlo nikdo neukradl. Hodí se i <a href="/cyklo-zamky/">zámek</a> a sada, kterou nabíjíte z notebooku v práci.</p>'
          '<h3>Silnice a gravel</h3>'
          '<p>Hledejte kuželové světlo s dosvitem dopředu a rozumným výdrží, zadní světlo s vysokou svítivostí a menší tělo, které nekazí aerodynamiku. Světla do tmy jsou důležitá při zimním tréninku, kdy se rychle stmívá.</p>'
          '<h3>Horská kola a noční jízdy</h3>'
          '<p>Potřebujete výkonné světlo na řídítka a druhé na helmu. Dvě světla vám dají jistotu, když jedno vypoví službu nebo se vybije. Důležitý je pevný držák, protože hrboly a otřesy zbaví světlo polohy.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>Nabídku pokrývají značky jako ' + B(('rockbros', 'Rockbros'), ('force', 'Force'), ('topeak', 'Topeak'), ('lezyne', 'Lezyne'), ('knog', 'Knog'), ('sigma', 'Sigma'), ('axa', 'Axa'), ('author', 'Author')) + '. '
          'Rozdíly bývají v optice, kvalitě držáků a ve způsobu nabíjení. Neznačkové sady mohou být cenově lákavé, ale u údajů o svítivosti a výdrži buďte opatrní a hledejte recenze od uživatelů.</p>'
          '<h2>Světla na dětském kole a na elektrokole</h2>'
          '<p>Děti na kole potřebují světla stejně jako dospělí, jen jejich kola mají méně místa na uchycení. Zvolte malé světlo s jednoduchým ovládáním, které zvládne ovládat jedním tlačítkem. '
          'U elektrokol existují modely napájené přímo z baterie pohonu, takže odpadá nabíjení světel; ověřte ale kompatibilitu s konkrétním pohonem. '
          'Pokud kolo používáte jako dopravní prostředek na dojíždění, zvažte pevně instalované osvětlení, které lze jen zapnout a nemusíte ho při každém parkování odmontovávat.</p>'
          '<h2>Údržba a časté chyby</h2>'
          '<ul><li><strong>Nenabité světlo.</strong> Zvykněte si nabíjet po každé delší jízdě a mít kabel na stálém místě.</li>'
          '<li><strong>Špatný sklon světla.</strong> Příliš nahoru oslní, příliš dolů neosvětlí cestu.</li>'
          '<li><strong>Zadní světlo pod brašnou.</strong> Přemístěte ho na sedlovku nebo přilbu.</li>'
          '<li><strong>Povolený držák.</strong> Po hrbolech světlo klesne a svítí do země.</li>'
          '<li><strong>Nulová rezerva.</strong> Vezměte malé záložní světlo, které se vejde do kapsy.</li>'
          '<li><strong>Zapomenuté čištění.</strong> Špinavá čočka a kontakty snižují svit.</li></ul>'
          '<p>Akumulátory nenechávejte dlouhodobě úplně vybité a světlo skladujte v suchu při pokojové teplotě. Pokud světlo vlivem otřesů bliká, zkontrolujte kontakty a držák.</p>'
          '<h2>Co dalšího se hodí k jízdě za tmy</h2>'
          '<p>Světla jsou jen jedním dílem. Pomůže <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> s reflexními prvky, <a href="/cyklisticke-bryle/">cyklistické brýle</a> s čirým sklem proti hmyzu a větru a <a href="/cyklo-pumpy-a-naradi/">pumpa a nářadí</a> pro opravu defektu ve tmě. '
          'Při noční jízdě v lese se vám hodí i <a href="/celovky-a-svitilny/">čelovka</a> na opravu kola. <a href="/cyklo-udrzba/">Péče o kolo</a> udrží vše v provozu. Základem je promyšlená výbava pro <a href="/cyklistika/">cyklistiku</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Vyberte pozici světla, filtrujte podle značky a porovnejte nabídky obchodů u stejného modelu. U sad ověřte, zda jsou v balení oba kusy i držáky a USB kabel. Čtěte parametry konkrétního režimu, ne jen maximum, a ověřte typ uchycení pro vaše řídítka. '
          'Při nákupu pro více lidí dává smysl sjednotit značku, protože si půjčíte kabel i držák.</p>',
    faq=[
        ('Jaká světla jsou na kole povinná?', 'Za snížené viditelnosti musí mít kolo přední bílé a zadní červené světlo a také odrazky. Podrobnosti najdete v zákoně o provozu na pozemních komunikacích. Pro bezpečnost se vyplatí světla používat i ve dne.'),
        ('Kolik lumenů potřebuji?', 'Záleží na terénu a rychlosti. Ve městě stačí nižší hodnoty, mimo osvětlené úseky více a na noční horskou jízdu nejvíc. Vedle lumenů rozhoduje i optika, takže se řiďte i recenzemi a popisem kuželu.'),
        ('Jak dlouho světlo vydrží na jedno nabití?', 'Udává se pro konkrétní režim. Nejsilnější režim bývá krátký, úsporný vydrží několik hodin. Za mrazu kapacita klesá, počítejte proto s rezervou a nabíjejte předem.'),
        ('Je lepší blikání, nebo stálé svícení?', 'Blikání lépe upoutá pozornost, ale může ztěžovat odhad vzdálenosti. Přední světlo se často používá stálé a zadní pulzující. Zkontrolujte, co povolují předpisy ve vaší zemi.'),
        ('Co znamená označení IPX?', 'Je to míra krytí proti vodě. Vyšší číslice znamená větší odolnost, ale zkoušky probíhají za standardních podmínek. Pokud jezdíte v dešti, vybírejte světla s uvedeným krytím.'),
        ('Jak světlo správně nastavit?', 'Přední světlo mírně sklopte dolů, aby kužel dopadal na vozovku několik metrů před kolem a neoslňoval protijedoucí. Zadní umístěte tak, aby bylo vidět z odstupu a nic ho nezakrývalo.'),
        ('Dá se používat jedno světlo pro kolo i helmu?', 'Některá světla mají univerzální držáky, ale pevné uchycení na řídítka a na přilbu je lepší řešit zvlášť. Kdo jezdí v terénu, ocení světlo na obou místech.'),
        ('Co je lepší, USB nabíjení, nebo baterie?', 'USB je pohodlné a levné na provoz, baterie umožní rychlou výměnu na cestách bez zásuvky. Pro dlouhé výlety se hodí kombinace nebo záložní zdroj.'),
        ('Jak pečovat o akumulátor světla?', 'Nenechávejte ho dlouho úplně vybitý, skladujte při pokojové teplotě a používejte vhodnou nabíječku. Čistěte kontakty a USB konektor, aby se neusazovala vlhkost.'),
        ('Jaké značky světel najdu?', 'V nabídce jsou například Rockbros, Force, Topeak, Lezyne, Knog, Sigma, Axa nebo Author. Rozhoduje vždy konkrétní model a jeho parametry.'),
        ('Hodí se do města dynamo?', 'Pro každodenní jízdu ano. Světlo svítí bez nabíjení a nevybije se. Vyžaduje ale vhodný náboj nebo přívěsný dynamický zdroj a kompatibilní svítilnu.'),
    ])

# ------------------------------------------------------------------ cyklisticke-rukavice
NEW['cyklisticke-rukavice'] = dict(long=True,
    title='Cyklistické rukavice: krátké, dlouhé, zimní',
    desc='Cyklistické rukavice na silnici, MTB i do města. Krátké, dlouhé a zimní, vložky, velikosti a materiály. Jak vybrat a pečovat o své rukavice.',
    intro='<p>Cyklistické rukavice patří k věcem, které si většina jezdců zamiluje po prvním delším výletu. Tlumí otřesy z řídítek, chrání dlaně při pádu a zlepšují úchop, když jsou ruce zpocené nebo mokré. '
          'V kategorii <strong>cyklistické rukavice</strong> najdete krátké letní modely, dlouhé přechodové, zimní vyhřívané i izolované, a také pevnější rukavice pro downhill a enduro.</p>'
          '<p>Sporteka porovnává nabídku českých obchodů u stejných modelů, takže zjistíte, kde je skladem vaše velikost. Rukavice jsou součástí oblečení pro cyklisty, spolu s <a href="/cyklisticke-dresy/">dresy</a>, '
          '<a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy a kalhotami</a> a <a href="/cyklisticke-ponozky/">ponožkami</a>. Dál vysvětlíme typy, velikosti, vložky, materiály i péči a nejčastější chyby při nákupu, aby výběr nebyl loterie.</p>',
    guide='<h2>Typy cyklistických rukavic</h2>'
          '<p>Rukavice se liší střihem, tloušťkou a určením. Dobrý výběr začíná otázkou, kdy a kde je budete nosit.</p>'
          + T(['Typ', 'Kdy se hodí', 'Typické rysy'], [
              ['Krátké (bez prstů)', 'léto, silnice, město, rekreační jízda', 'prodyšný hřbet, vložka na dlani'],
              ['Dlouhé tenké', 'jaro, podzim, chladnější rána', 'plné prsty, lehká izolace, větruodolný hřbet'],
              ['Zimní', 'nízké teploty, vítr a vlhko', 'zateplení, membrána, delší manžeta'],
              ['MTB a enduro', 'terénní jízda, kořeny, kameny', 'zesílené prsty, ochranné vložky, poutko na stahování'],
              ['Downhill a BMX', 'rychlé sjezdy, skoky', 'robustní materiál, vyztužené klouby'],
              ['Dětské', 'rodinné výlety, první kola', 'menší velikosti, jednoduché zapínání']]) +
          '<p>Krátké rukavice nabízejí nejvíc volnosti a chlad letního větru. Dlouhé rukavice chrání prsty před zimou a při pádu je kryjí lépe. Zimní modely bývají větší a mají výraznější izolaci, ale ztrácejí cit, což se dá vyřešit tenkými vnitřními rukavicemi. '
          'Kdo se vydává na delší výlety, často vozí v kapse dva páry a vybírá podle teploty.</p>'
          '<h2>Proč rukavice nosit</h2>'
          '<p>Na řídítkách ruce nesou značnou část tíhy horní poloviny těla. Rukavice s dlaní vyztuženou gelem nebo pěnou rozloží tlak a omezí otlaky a necitlivost prstů. '
          'Při pádu se člověk instinktivně opře o ruce, takže dlaň rukavice chrání před odřením. Navíc látka na hřbetu často slouží k otírání potu z čela a nosu, a proto bývá na palci měkký froté pásek. '
          'Rukavice také zlepšují úchop, když jsou řídítka mokrá, a ve větru drží teplo. Nemají ale nahradit helmu ani vhodnou techniku.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Správně padnoucí rukavice leží na dlani bez záhybů a na prstech netlačí. Příliš velké se krčí pod řídítky a vytvářejí otlaky, příliš malé škrtí a omezují prokrvení. Velikost se určuje podle obvodu dlaně pod klouby nebo podle délky ruky; každý výrobce má vlastní tabulku, a proto ji vždy čtěte u konkrétního modelu.</p>'
          + T(['Kontrolní bod', 'Jak to má vypadat'], [
              ['Konečky prstů', 'dosahují ke švu, nejsou stlačené'],
              ['Dlaň', 'bez záhybů, vložka sedí na správném místě'],
              ['Zápěstí', 'zapnutí na suchý zip drží, ale nesvírá'],
              ['Ohnutí v kloubech', 'prsty se dají plně sevřít bez napnutí švů']]) +
          '<p>Zkoušejte rukavice při sevřené pěsti a s rukama na pomyslných řídítkách. Pokud nakupujete online, změřte ruku krejčovským metrem a porovnejte s tabulkou. Přihlédněte i k tomu, že rukavice se časem trochu přizpůsobí ruce, hlavně kožené a z umělé kůže.</p>'
          '<h2>Materiály</h2>'
          '<p>Hřbet se nejčastěji šije z elastických tkanin, které se přizpůsobí pohybu prstů, a z mřížky pro odvětrání. Dlaň bývá ze syntetické kůže (nejčastěji polyuretan), z mikrovlákna nebo z pravé kůže. '
          'Syntetika je lehčí, snáze se pere a dobře drží v mokru. Pravá kůže je pevná a příjemná, ale pomaleji schne. U zimních modelů se objevují izolace z flísu nebo syntetických vláken a vnější větruodolné či voděodolné vrstvy. '
          'Membránové rukavice zadrží vodu, ale prodyšnost je horší, takže se do nich ruce potí a při dlouhé jízdě mohou zvlhnout zevnitř.</p>'
          '<h3>Vložky v dlani</h3>'
          '<p>Vložky z gelu nebo pěny se liší tloušťkou a umístěním. Silnější vložka tlumí víc, ale zhoršuje cit a může rušit při brzdění, které vyžaduje přesnost. Na silnici na delší vzdálenosti bývá tlumení výraznější, v terénu ocení jezdci naopak tenčí dlaň s lepším citem. '
          'Důležité je, aby vložka seděla v místě, kde se opírá dlaň u kosti zápěstí, nikoli uprostřed dlaně.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<h3>Silnice a gravel</h3>'
          '<p>Na delších trasách se osvědčují lehké krátké rukavice s dobrým tlumením a měkkým palcem na otírání potu. V chladnějších měsících přijdou vhod tenké dlouhé, které se dají složit do kapsy dresu. Pokud jedete rychle, ocení jezdci aerodynamický střih bez vlajících součástí.</p>'
          '<h3>Horská kola</h3>'
          '<p>Na kořenech a kamenech se hodí zesílené prsty a prodloužená ochrana hřbetu ruky. Dlouhé rukavice se používají často i v létě, protože při pádu chrání prsty. Tenká dlaň zachovává cit na brzdové páce, což v technickém terénu pomáhá.</p>'
          '<h3>Město a rekreace</h3>'
          '<p>Stačí jednoduché rukavice s mírným tlumením. Při každodenním dojíždění v zimě se vyplatí větruodolné se zateplením, které se dají použít i při běhu nebo procházce. Praktické je reflexní logo nebo prvek.</p>'
          '<h3>Děti</h3>'
          '<p>Dětské rukavice musí padnout, aby je dítě nevnímalo jako překážku, jinak je sundá. Kratší prsty a snadné zapínání ocení rodiče i děti. Pro nejmenší jezdce se hodí i <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</p>'
          '<h2>Zimní jízda a vrstvení</h2>'
          '<p>Ruce chladnou rychleji než jiné části těla, protože mají malý objem a při jízdě jsou vystaveny větru. Zimní rukavice proto musí mít větruodolnou vrstvu a delší manžetu, která zajede pod rukáv bundy. '
          'Ve velmi chladných dnech funguje vrstvení: tenká vnitřní rukavice odvádí vlhkost a teplejší vnější izoluje. Příliš těsná rukavice zhoršuje prokrvení a ruce zmrznou dříve, proto vybírejte o něco volnější, ale ne přehnaně. '
          'Pro chlad se hodí také <a href="/cyklisticke-bundy-a-vesty/">bundy a vesty</a> a <a href="/cyklisticke-navleky/">návleky</a> na ruce a nohy. Lyžařské modely najdete v kategorii <a href="/lyzarske-rukavice/">lyžařské rukavice</a>, ale pro kolo jsou obvykle příliš objemné.</p>'
          '<h2>Střih, švy a drobné detaily</h2>'
          '<p>Kvalitu rukavice poznáte i podle věcí, kterých si při prvním pohledu nevšimnete. Švy na prstech mají být ploché a umístěné tak, aby netlačily na kůži při sevření řídítek. '
          'Poutko na stažení z ruky usnadní sundávání, zejména když jsou prsty vlhké. Reflexní proužky na hřbetu pomáhají při odbočování, protože řidiči vidí gesto ruky. '
          'Někteří výrobci šijí špičky ukazováčku a palce z materiálu vhodného pro ovládání dotykového displeje, což ocení každý, kdo za jízdy vytahuje telefon. '
          'Manžeta může být krátká na suchý zip nebo delší z elastické příze; delší lépe drží teplo, krátká je pohodlnější v létě. Jakmile rukavice při jízdě sklouzávají, zkontrolujte, zda není povolený suchý zip nebo zda nemáte větší velikost, než potřebujete.</p>'
          '<h2>Rukavice po pádu a kdy je vyměnit</h2>'
          '<p>Po pádu rukavice prohlédněte: potrhaná látka na dlani, roztržený šev nebo sedřená vrstva znamená, že další ochrana bude horší. Stejně tak vyměňte rukavice s propadlou vložkou, kde se látka protřela do průhledna. '
          'Sezónní výměna bývá rozumný zvyk; jaro a podzim jsou ideální chvíle, kdy si projdete obě sady a vyřadíte poškozené kusy.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>Nabídku tvoří značky jako ' + B(('rockbros', 'Rockbros'), ('r2', 'R2'), ('silvini', 'Silvini'), ('haven', 'Haven'), ('etape', 'Etape'), ('ziener', 'Ziener'), ('tsg', 'TSG'), ('fox', 'Fox')) + '. '
          'Rozdíly bývají v střihu, tloušťce dlaně a kvalitě zpracování, takže vždy čtěte parametry u konkrétního kusu, ne jen název značky.</p>'
          '<h2>Péče o rukavice</h2>'
          '<p>Rukavice se potí, a proto je třeba je pravidelně prát. Většinu syntetických modelů zvládne praní v ruce nebo v pračce na šetrný program, ale vždy sledujte štítek. Nepoužívejte aviváž, protože zhoršuje odvod vlhkosti, a nesušte na topení ani na přímém slunci. '
          'Suché zipy před praním zapněte, aby nepoškodily látky. Zimní membránové rukavice perte podle pokynů výrobce, ošetření impregnací bývá jednou za čas potřeba. Kožené dlaně promažte podle návodu a nenechte je vyschnout do tuhosti. '
          'Do kapsy po jízdě rukavice neukládejte mokré, jinak začnou zapáchat; nejlépe je rozložte a nechte vyvětrat.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Špatná velikost.</strong> Příliš velká rukavice vytváří záhyby a otlaky.</li>'
          '<li><strong>Tlustá dlaň na technický terén.</strong> Ztratíte cit pro brzdu.</li>'
          '<li><strong>Zimní rukavice jen podle teploty.</strong> Důležité je i krytí proti větru a vlhku.</li>'
          '<li><strong>Zanedbání praní.</strong> Pot a nečistota zkracují životnost materiálu.</li>'
          '<li><strong>Jízda v opotřebovaných rukavicích.</strong> Prodřená dlaň ztrácí funkci a může klouzat.</li>'
          '<li><strong>Záměna s fitness či zahradními rukavicemi.</strong> Nemají střih ani vložky pro řídítka.</li></ul>'
          '<h2>Co se hodí k rukavicím</h2>'
          '<p>Ochranu doplňuje <a href="/cyklisticke-helmy/">helma</a> a <a href="/cyklisticke-bryle/">cyklistické brýle</a>. V terénu přidejte <a href="/cyklo-chranice/">chrániče</a>. Ucelené oblečení najdete v kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>, '
          'rukavice na jiné sporty v kategorii <a href="/sportovni-rukavice/">sportovní rukavice</a>. Světla a zvonek pro bezpečnost jízdy jsou v kategoriích <a href="/cyklo-svetla/">světla na kolo</a> a <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Vyberte typ podle sezóny, filtrujte podle značky a otevřete detail, kde uvidíte nabídky obchodů. Velikostní tabulku si přečtěte dřív než cenu a zkontrolujte, zda je v nabídce vaše velikost. '
          'Pokud váháte mezi dvěma, zvolte tu, která lépe sedí v prstech. Při nákupu na zimu si raději pořiďte dvě sady, tenčí a silnější, protože jedny rukavice se nepoužijí všude.</p>',
    faq=[
        ('Potřebuji cyklistické rukavice, když jezdím jen rekreačně?', 'Nepotřebujete je, ale pomohou. Tlumí tlak na dlaně a chrání při pádu. Na delších výletech omezují otlaky a otírají pot. Pro krátké projížďky po městě může stačit jednoduchý model.'),
        ('Jak vybrat správnou velikost?', 'Změřte obvod dlaně pod klouby a porovnejte s tabulkou výrobce u konkrétního modelu. Rukavice má sedět bez záhybů a nesmí tlačit v prstech, i když je pěst sevřená.'),
        ('Čím se liší krátké a dlouhé rukavice?', 'Krátké nechávají prsty volné a jsou prodyšné, hodí se do tepla. Dlouhé kryjí prsty před chladem a při pádu chrání víc. V terénu je používá mnoho jezdců i v létě.'),
        ('Co udělá gelová vložka v dlani?', 'Rozloží tlak z řídítek a tlumí část otřesů. Příliš silná vložka ale zhoršuje cit, proto na technický terén bývá vhodnější tenčí dlaň.'),
        ('Jaké rukavice na zimu?', 'Větruodolné, s izolací a delší manžetou. Při velmi nízkých teplotách se vyplatí vrstvení s tenkou vnitřní rukavicí. Příliš těsné rukavice zhoršují prokrvení a ruce zmrznou dřív.'),
        ('Mohu používat lyžařské rukavice na kole?', 'Dá se, ale bývají objemné a sníží cit pro brzdění a řazení. Lepší jsou speciální zimní cyklistické rukavice s tenčí dlaní a protiskluzovým povrchem.'),
        ('Jak rukavice prát?', 'Podle štítku, nejčastěji šetrně v ruce nebo v pračce na nízkou teplotu. Nepoužívejte aviváž a nesušte na topení. Suché zipy zapněte, ať neničí tkaniny.'),
        ('Jak dlouho rukavice vydrží?', 'Záleží na četnosti jízdy, materiálu a péči. Když je dlaň prodřená nebo vložka propadlá, ztrácí rukavice funkci a je čas na novou.'),
        ('Jsou vhodné i pro děti?', 'Ano, existují dětské velikosti. Dbejte na to, aby seděly, jinak je dítě odmítne nosit. Důležité je jednoduché zapínání.'),
        ('Které značky najdu v kategorii?', 'Například Rockbros, R2, Silvini, Haven, Etape, Ziener, TSG nebo Fox. Vždy se řiďte parametry konkrétního modelu.'),
    ])

# ------------------------------------------------------------------ masazni-pomucky
NEW['masazni-pomucky'] = dict(long=True,
    title='Masážní pomůcky: válce, míčky a pistole',
    desc='Masážní válce, míčky, pistole, hole a podložky na doma i do tělocvičny. Jak vybrat tvrdost, velikost a typ pomůcky a jak ji správně používat.',
    intro='<p>Masážní pomůcky se v posledních letech staly běžnou součástí domácího i profesionálního vybavení sportovců. V kategorii <strong>masážní pomůcky</strong> najdete pěnové válce, masážní míčky a dvojité míčky, '
          'masážní hole a válečky, pistole, akupresurní podložky i malé pomůcky na chodidla, záda a ruce. Liší se tvrdostí, povrchem, velikostí a způsobem použití.</p>'
          '<p>Sporteka porovnává nabídku českých obchodů u stejných pomůcek vedle sebe. Patří do oboru <a href="/fitness/">fitness a posilování</a> a doplňují <a href="/fitness-pomucky/">fitness pomůcky</a>, <a href="/joga-a-podlozky/">jógu a podložky</a> a '
          '<a href="/funkcni-trenink/">funkční trénink</a>. Texty nenahrazují radu lékaře ani fyzioterapeuta; při bolesti, úrazu nebo zdravotním omezení se poraďte s odborníkem. Dál probereme typy pomůcek, výběr, bezpečné používání a péči.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Slovo masáž v názvu je široké a kryje skutečně různé předměty. Aby se v nich dalo vyznat, rozdělíme je podle toho, jak se používají.</p>'
          + T(['Typ pomůcky', 'Jak se používá', 'Na co se zaměřit'], [
              ['Pěnový válec', 'tělo se po něm pomalu kutálí', 'tvrdost, průměr, délka, povrch (hladký či s výstupky)'],
              ['Masážní míček', 'opře se o něj tělo o stěnu nebo podlahu', 'tvrdost, průměr, povrch'],
              ['Dvojitý míček (peanut)', 'dva spojené míčky, páteř zůstává mezi nimi', 'rozměr, materiál, tvrdost'],
              ['Masážní pistole', 'ruční přístroj s kmitající hlavicí', 'síla, hlučnost, výdrž akumulátoru, nástavce'],
              ['Masážní hůl a váleček', 'ruční válení po svalech', 'délka, pevnost, madla'],
              ['Podložky a rohože s hroty', 'ležení či stání na výstupcích', 'hustota hrotů, materiál, velikost'],
              ['Pomůcky na chodidla a ruce', 'malé míčky, válečky, ježci', 'velikost, určení']]) +
          '<p>Nejčastěji se kupuje pěnový válec, protože je univerzální a levný na provoz. Míčky jsou přesnější a přenosné, takže je pohodlně vezmete do tašky. '
          'Pistole poskytují rychlou a pohodlnou stimulaci a hodí se tam, kde nelze použít váleček, například na zadní část stehen. Elektrické přístroje jsou dražší a vyžadují nabíjení.</p>'
          '<h2>Pěnové válce a jejich tvrdost</h2>'
          '<p>Válec se liší hustotou pěny. Měkčí válec povolí víc, je příjemný pro začátečníky a pro citlivější tělo. Tvrdší válec vyvíjí větší tlak, hodí se pro zkušené cvičence, kteří vědí, co chtějí. '
          'Hladký povrch je univerzální. Válce s výstupky nebo drážkami působí lokálněji, ale mohou být nepříjemné. Délka se volí podle toho, kam chcete válec nosit: krátký, třeba třicet centimetrů, se vejde do tašky, delší se hodí na záda a celé tělo.</p>'
          + T(['Vlastnost', 'Měkčí válec', 'Tvrdší válec'], [
              ['Pocit při použití', 'jemný, rozložený tlak', 'výraznější, lokální tlak'],
              ['Vhodný pro', 'začátečníky, úvodní seznámení', 'zkušené cvičence'],
              ['Trvanlivost', 'dříve ztrácí tvar', 'déle drží tvar']]) +
          '<p>Při používání válec nepřebíhejte; pomalé kutálení a krátké zastavení na citlivém místě je běžná technika. Pokud pocítíte ostrou nebo vystřelující bolest, přestaňte. Nikdy nerolujte přímo po kloubech a po bederní páteři válec nepoužívejte, pokud to nedoporučil odborník.</p>'
          '<h2>Masážní míčky</h2>'
          '<p>Míček umožní zacílit na malé plochy, kam válec nedosáhne: lopatku, hýždě, chodidlo, předloktí. Existují tvrdé gumové, měkčí pěnové a míčky s výstupky. Tvrdší míček působí intenzivněji, a tak ho volte se zvýšenou opatrností. '
          'Dvojitý míček tvoří dvě koule spojené s mezerou, kudy prochází páteř, takže tlak se přenáší na svaly vedle ní. Při práci o stěnu je zátěž mírnější než na podlaze, a proto se tato varianta hodí pro začátek.</p>'
          '<h2>Masážní pistole a elektrické přístroje</h2>'
          '<p>Masážní pistole rychle kmitá hlavicí a vyvíjí pulzy do svalu. Při výběru se sleduje amplituda (jak daleko hlavice vyjede), počet stupňů rychlosti, hlučnost, hmotnost a kapacita akumulátoru. '
          'Výměnné nástavce mají různé tvary: kulatý pro velké svaly, plochý pro širší plochy, špičatý pro bodové působení. Přístroj se přikládá lehce a pohybuje se po svalu, nesmí se tlačit nadměrnou silou. '
          'Nepoužívejte ho přímo na kosti, klouby, krk a obličej a řiďte se pokyny výrobce, včetně doporučené doby na jedno místo. Lidé s onemocněním, v těhotenství nebo s implantáty by se měli před použitím poradit s lékařem.</p>'
          '<p>Domácí přístroje, například od značek ' + B(('beurer', 'Beurer'), ('insportline', 'Insportline'), ('hms', 'HMS')) + ', se liší nejen výkonem, ale i ergonomií, takže zvažte hmotnost a tvar držadla.</p>'
          '<h2>Pomůcky pro konkrétní části těla</h2>'
          '<h3>Záda a lopatky</h3>'
          '<p>Nejpoužívanější je dlouhý válec nebo míček o stěnu. Dvojitý míček obchází páteř a působí na svaly kolem ní, hodí se do kanceláře i na cesty. Dlouhá hůl umožní dosáhnout bez cizí pomoci mezi lopatky.</p>'
          '<h3>Nohy a chodidla</h3>'
          '<p>Chodidla se kutálí po malém míčku nebo ježkovi, lýtka a stehna po válci. Po běhu nebo kole je to obvyklé zpestření. Pro běžce je užitečná i <a href="/bezecka-obuv/">běžecká obuv</a>, která pomáhá chránit nohy při dalším tréninku.</p>'
          '<h3>Ruce, předloktí a krk</h3>'
          '<p>Malé míčky a pružné válečky se hodí pro ruce a předloktí, tedy pro lezce, cyklisty a lidi sedící u počítače. Krk a hlavu se snažte masírovat opatrně a krátce; zde se nedoporučují silné nástroje.</p>'
          '<h2>Kdy a jak pomůcky používat</h2>'
          '<p>Nejčastěji se používají před tréninkem jako součást rozcvičky a po něm jako zklidnění. Před výkonem stačí krátké a svižné válení, po výkonu klidnější a o něco delší. '
          'Délka jedné části těla se obvykle pohybuje v řádu desítek vteřin až několika minut, ale přesná doporučení najdete u výrobce nebo fyzioterapeuta. Pomůcky nejsou náhradou za protažení, spánek, pitný režim a plánování tréninku.</p>'
          '<ul><li>Dýchejte pravidelně, nezadržujte dech.</li>'
          '<li>Nepoužívejte na čerstvé zranění, otok nebo zanícené místo.</li>'
          '<li>Pohybujte se pomalu a zastavte u citlivého místa jen krátce.</li>'
          '<li>Při bolesti, brnění nebo necitlivosti přestaňte.</li>'
          '<li>Při dlouhodobých potížích vyhledejte odborníka.</li></ul>'
          '<h2>Výběr podle sportu a životního stylu</h2>'
          '<p>Běžci a cyklisté využijí válec na stehna a lýtka a malý míček na chodidla. Silový trénink si žádá robustní válec, který neztratí tvar při většině zátěže, a pistoli na velké svalové skupiny. '
          'Jóga a pilates se pojí s měkčími a přívětivějšími pomůckami, viz <a href="/joga-a-pilates/">jóga a pilates</a> a <a href="/pilates-pomucky/">pilates pomůcky</a>. '
          'Lezci obvykle sahají po malých míčcích a válečcích na předloktí. Kdo sedí v kanceláři, ocení dvojitý míček nebo hůl.</p>'
          '<h2>Cestování a práce v kanceláři</h2>'
          '<p>Kdo hodně sedí nebo cestuje, ocení malé pomůcky, které se vejdou do kabelky nebo zavazadla: míček velikosti tenisáku, skládací hůl či kompaktní pistoli s pouzdrem. '
          'V letadle a ve vlaku se hodí měkčí míček, který nikomu nevadí a nepůsobí příliš intenzivně. Pamatujte, že přístroje s akumulátorem se při letecké přepravě řídí pravidly dopravce, a proto si je předem ověřte. '
          'V práci stačí krátká pauza každou hodinu a pár pomalých pohybů; pomůcka je jen doplněk změny polohy.</p>'
          '<h2>Značky v kategorii</h2>'
          '<p>V nabídce jsou například ' + B(('hms', 'HMS'), ('insportline', 'Insportline'), ('4fizjo', '4FIZJO'), ('merco', 'Merco'), ('beurer', 'Beurer'), ('sportago', 'Sportago'), ('spokey', 'Spokey'), ('lifefit', 'Lifefit')) + '. '
          'Liší se materiálem, zpracováním a tím, jak dlouho pomůcka drží tvar. Při srovnávání se zaměřte na rozměry, tvrdost a poznámky o použití, ne na slibný název.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Pěnové válce a míčky otírejte vlhkým hadříkem a občas použijte jemný čisticí prostředek. Nenechávejte je na přímém slunci ani u topení, kde se pěna deformuje. '
          'Elektrické přístroje čistěte suchým hadrem, hlavici a nástavce dezinfikujte podle návodu a akumulátor nabíjejte předepsaným kabelem. Skladujte v suchu a mimo dosah dětí. Pokud válec ztratil tvar, nebo se začal drolit, je čas na nový.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Příliš tvrdá pomůcka hned na začátku.</strong> Začněte jemněji a postupně přidávejte.</li>'
          '<li><strong>Dlouhé setrvání na jednom místě.</strong> Zbytečně vyvolává podráždění.</li>'
          '<li><strong>Masáž kloubů a kostí.</strong> Pomůcky jsou určeny pro svalové partie.</li>'
          '<li><strong>Spoléhání na přístroj místo pohybu.</strong> Je to doplněk, ne náhrada.</li>'
          '<li><strong>Ignorování bolesti.</strong> Silná bolest je důvod přestat a poradit se.</li>'
          '<li><strong>Nákup podle designu.</strong> Důležitější než barva je tvrdost a rozměr.</li></ul>'
          '<h2>Jak si domácí kout uspořádat</h2>'
          '<p>Nejlépe se pomůcky používají na pevné a čisté podložce, kde se nic neklouže. Válec, míček a hůl uložte na dohled, třeba do koše u gauče, protože to, co je vidět, se používá častěji. '
          'Pokud cvičíte v tělocvičně, vezměte si malý míček a krátký válec do tašky; zabírají málo místa a nahradí vybavení, které v tělocvičně není. '
          'Pro společné používání v rodině se vyplatí pomůcky popsat podle tvrdosti, aby každý sáhl po té, která mu vyhovuje. Pokud máte malý byt, zvolte skládací nebo dutý válec, do kterého se dají uschovat menší míčky.</p>'
          '<h2>Co se hodí k regeneraci</h2>'
          '<p>Vedle masážních pomůcek se vyplatí <a href="/bandaze-a-ortezy/">bandáže a ortézy</a> pro podporu kloubů při zátěži, <a href="/sportovni-vyziva/">sportovní výživa</a> a pravidelný pitný režim. '
          'Domácí cvičení rozšíříte o <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/cinky-a-kotouce/">činky a kotouče</a>. Pro cvičení na podlaze se hodí <a href="/joga-a-podlozky/">podložky</a>. Případně se podívejte na širší nabídku <a href="/funkcni-trenink/">funkčního tréninku</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Rozhodněte se, zda hledáte válec, míček nebo přístroj, a filtrujte podle značky. U každého kusu zkontrolujte rozměry, tvrdost a materiál, u pistole i výdrž akumulátoru a nástavce. '
          'V detailu produktu porovnejte nabídky několika obchodů a přečtěte si podmínky vrácení. Pokud kupujete poprvé, zvolte spíše střední tvrdost a osvědčené rozměry a až po zkušenosti přejděte na intenzivnější typ.</p>',
    faq=[
        ('K čemu masážní válec slouží?', 'Používá se jako pomůcka při rozcvičce a po cvičení; tělo se po něm pomalu kutálí a působí tlakem na svalové partie. Neslouží k léčbě a při potížích se poraďte s odborníkem.'),
        ('Jak vybrat tvrdost válce?', 'Začátečníkům se hodí měkčí válec, který působí jemněji. Zkušenější cvičenci často volí tvrdší. Tvrdost volte tak, abyste mohli dýchat klidně a nebyla vám nepříjemná.'),
        ('Je lepší válec, nebo míček?', 'Válec se hodí na velké svalové skupiny, míček na menší a hůře dostupná místa. Mnoho lidí používá obojí, protože se doplňují.'),
        ('Kdy použít masážní pistoli?', 'Hodí se před cvičením i po něm na velké svaly. Používejte ji lehce, nepřikládejte na kosti, klouby a krk a řiďte se návodem. Při zdravotních potížích se nejdřív poraďte s lékařem.'),
        ('Jak dlouho se má válet jedno místo?', 'Obecně stačí od několika desítek vteřin po pár minut. Přesné doporučení závisí na člověku a pomůcce. Řiďte se pokyny výrobce nebo fyzioterapeuta.'),
        ('Mohu válcovat páteř?', 'Přímo po páteři se neroluje; dvojitý míček je navržen tak, aby páteř zůstala mezi koulemi. Pokud máte potíže se zády, nechte si poradit od odborníka.'),
        ('Co dělat při bolesti při použití?', 'Přestaňte a nezkoušejte se přes bolest. Mírný tlak je běžný, ostrá nebo vystřelující bolest, brnění a necitlivost ne. Při opakovaných potížích navštivte lékaře.'),
        ('Jak pomůcky čistit?', 'Vlhkým hadříkem a jemným čisticím prostředkem. Nenechávejte je na slunci ani u topení. Elektrický přístroj čistěte jen podle návodu výrobce.'),
        ('Jaké značky najdu v kategorii?', 'Mezi značkami jsou HMS, Insportline, 4FIZJO, Merco, Beurer, Sportago, Spokey nebo Lifefit. Porovnávejte konkrétní parametry, ne jen název.'),
        ('Hodí se masážní pomůcky i pro děti?', 'Obecně jsou určeny dospělým. Pro děti je lepší nejdřív konzultace s lékařem nebo trenérem a používání pod dohledem dospělého.'),
    ])
