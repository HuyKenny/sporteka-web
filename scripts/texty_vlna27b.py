"""sporteka.cz — wave 27b (16. 11. 2026): long texts for tribulus, kurkuma, spirulina-chlorella, sejkry.
General true facts only. Tribulus, curcumin, spirulina, chlorella and barley grass have no authorised EU health claim
(botanical claims are on hold), so no effects are promised; no prices, no dosing advice beyond the label.
Only brand with an indexed page (znacky.json): gymbeam; other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ tribulus
NEW['tribulus'] = dict(long=True,
    title='Tribulus terrestris (kotvičník): saponiny, formy, kapsle',
    desc='Tribulus terrestris neboli kotvičník zemní v kapslích, tabletách i tinktuře. Co znamená 90 % saponinů a jak porovnat nabídky českých obchodů.',
    intro='<p>Kotvičník zemní (Tribulus terrestris) je nízká poléhavá bylina teplých a suchých oblastí, která roste i v jižní Evropě a na Balkáně. Jméno dostal podle tvrdých ostnatých plodů, které se umí zapíchnout do podrážky i do pláště kola. Pro doplňky stravy se z nadzemní části a plodů vyrábí extrakt, nejčastěji standardizovaný na obsah saponinů. Mezi bylinami prodávanými mužům a návštěvníkům posiloven patří tribulus dlouhodobě k nejznámějším.</p>'
          '<p>Sporteka ukazuje nabídky českých obchodů vedle sebe, objednávku ale dokončíte v e-shopu, který si sami vyberete. V kategorii najdete kapsle a tablety s extraktem 90 % saponinů, „bulharský“ tribulus, kombinace se zinkem a vitamínem B6, bezlihové tinktury, sypký čaj i instantní nápoje v sáčcích. Nabízejí je třeba Nutrend, BioTech USA, NOW Sports, Extrifit, VemoHerb, MOVit, Allnature, GreenFood nebo Fitsport Nutrition. Další byliny hledejte v kategorii <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>, oblíbená je například <a href="/ashwagandha/">ashwagandha</a>.</p>',
    guide='<h2>Co je tribulus a co o něm víme</h2>'
          '<p>Za pozorností, které se kotvičníku dostává, stojí hlavně steroidní saponiny. Nejčastěji zmiňovaným z nich je protodioscin. Kvůli těmto látkám se tribulus léta prodává jako bylina pro muže a silové sportovce. Výsledky studií u lidí jsou však nejednoznačné a řada z nich u zdravých mužů nezjistila zvýšení hladiny testosteronu, síly ani svalové hmoty. Pokusy se navíc lišily typem extraktu, množstvím i délkou užívání, takže se jejich závěry špatně srovnávají.</p>'
          '<p>Pro nakupujícího je podstatné, co smí stát na obalu. Evropská unie pro kotvičník neschválila žádné zdravotní tvrzení. Tvrzení u rostlinných látek, takzvaných botanicals, jsou od roku 2010 pozastavená a dosud čekají na posouzení. Nápisy typu „testosteronový booster“ nebo „pro mužskou sílu“ proto čtěte jako reklamu, ne jako ověřený účinek. Doplněk stravy navíc není lék a nenahrazuje pestrou stravu ani spánek.</p>'
          '<h2>Saponiny a standardizace: co znamená 90 %</h2>'
          '<p>Na etiketách uvidíte čísla jako 40 %, 60 % a v české nabídce nejčastěji 90 % saponinů. Údaj vyjadřuje, jakou část extraktu tvoří saponiny podle prohlášení výrobce. Vyšší procento ale samo o sobě neznamená lepší výrobek. Záleží i na tom, z jaké části rostliny a z jaké oblasti surovina pochází a jakou analytickou metodou laboratoř saponiny stanovila. Různé metody mohou u stejného vzorku vykázat odlišná čísla. Některé značky proto doplňují i obsah protodioscinu, což je konkrétnější údaj.</p>'
          '<p>Přívlastek „bulharský tribulus“ odkazuje na rostliny sbírané na Balkáně. Výrobci uvádějí, že taková surovina obsahuje víc protodioscinu než kotvičník z jiných oblastí. Rozbory vzorků z různých zemí skutečně ukazují, že se složení saponinů liší podle oblasti původu. U konkrétního výrobku se to ale dá ověřit jen podle rozboru šarže, a pokud ho značka nezveřejňuje, jde spíš o obchodní označení.</p>'
          + T(['Forma', 'Co obsahuje', 'Na co se dívat'], [
              ['Kapsle a tablety s extraktem', 'suchý extrakt, obvykle 90 % saponinů', 'množství extraktu na porci a procento saponinů'],
              ['Kombinace se zinkem a B6', 'extrakt + zinek, někdy hořčík a vitamín B6', 'schválená tvrzení patří minerálům a vitamínu, ne bylině'],
              ['Bylinné kapsle bez standardizace', 'mletá nať nebo extrakt bez udaného obsahu saponinů', 'bez procenta nelze srovnat obsah látek'],
              ['Bezlihová tinktura', 'tekutý výtažek ve vodě nebo glycerinu', 'dávkování po kapkách nebo mililitrech'],
              ['Instantní nápoj', 'prášek v sáčcích k rozmíchání', 'sladidla, aroma a obsah extraktu na sáček'],
              ['Čaj', 'sušená nať k louhování', 'obsah saponinů není standardizovaný'],
              ['„Testo“ směsi', 'kotvičník s dalšími bylinami a minerály', 'množství složek bývá skryté v proprietární směsi']]) +
          '<h2>Jak číst miligramy na obalu</h2>'
          '<p>U kotvičníku se v číslech zamotá skoro každý. Jeden výrobek nabízí 500 mg v kapsli, druhý 1000 mg, třetí 2000 mg na porci, a bez dalších údajů z toho nic nevyčtete. Rozhodující je, kolik extraktu obsahuje jedna denní porce a na kolik procent saponinů je extrakt standardizovaný. Pozor na zápis typu „odpovídá 5000 mg byliny“ nebo na poměr 10:1. Jde o přepočet na sušenou rostlinu, ze které se extrakt vyrobil, ne o skutečnou hmotnost v kapsli.</p>'
          '<ul><li><strong>Extrakt na porci:</strong> hledejte číslo v mg vztažené k celé denní porci, ne k jedné kapsli.</li>'
          '<li><strong>Počet kapslí v porci:</strong> když porci tvoří tři kapsle, vystačí balení se 120 kusy na čtyřicet dní.</li>'
          '<li><strong>Standardizace:</strong> procento saponinů, případně obsah protodioscinu.</li>'
          '<li><strong>Část rostliny:</strong> nať, plody, nebo celá nadzemní část.</li>'
          '<li><strong>Obal kapsle:</strong> rostlinná celulóza (HPMC) je vhodná pro vegany, želatina ne.</li>'
          '<li><strong>Další složky:</strong> u kombinací zkontrolujte množství zinku a vitamínu B6 v miligramech.</li></ul>'
          '<h2>Tribulus se zinkem, hořčíkem a B6</h2>'
          '<p>Velká část nabídky spojuje kotvičník se zinkem, hořčíkem a vitamínem B6, někdy pod zkratkou ZMB6. Tady se vyplatí číst pozorně, k čemu se tvrzení na obalu vztahuje. Zinek přispívá k udržení normální hladiny testosteronu v krvi a vitamín B6 přispívá k regulaci hormonální činnosti. Obě tvrzení jsou v EU schválená, patří ale minerálu a vitamínu, nikoli bylině. Pokud už samostatný <a href="/zinek/">zinek</a> nebo multivitamín užíváte, sečtěte si celkový denní příjem ze všech přípravků, ať zbytečně nepřekročíte doporučené množství.</p>'
          '<h2>Pro koho není vhodný</h2>'
          '<p>Kotvičník není určený pro těhotné a kojící ženy, děti a dospívající. Bez porady s lékařem by ho neměli užívat lidé s hormonálně podmíněným onemocněním, s potížemi s prostatou, ledvinami nebo játry, ani ti, kdo pravidelně berou léky, třeba na cukrovku, krevní tlak nebo srdce. Jako možný nežádoucí účinek se nejčastěji uvádějí zažívací potíže. Užívejte ho přesně podle dávkování na obalu, a když se objeví obtíže, přestaňte.</p>'
          '<h2>Tribulus a závodní sport</h2>'
          '<p>Samotný kotvičník na seznamu zakázaných látek Světové antidopingové agentury není. U doplňků pro sportovce ale vždy hrozí, že výrobek bude znečištěný nebo bude obsahovat látku, kterou etiketa neuvádí, a „testo“ směsi patří k rizikovějším skupinám. Závodníci, kteří podléhají dopingovým kontrolám, by měli dávat přednost výrobkům testovaným v programech typu Informed Sport nebo Kölner Liste a uschovat si šarži i doklad o koupi.</p>'
          '<h2>Kotvičník, nebo raději něco jiného?</h2>'
          '<p>Kdo hledá doplněk na období vysoké tréninkové zátěže, často porovnává kotvičník s ashwagandhou, macou nebo s minerály. Každá z těchto látek se prodává s jiným příslibem a ani u ostatních bylin nejsou zdravotní tvrzení schválená. Na výkon a regeneraci mají přitom mnohem větší vliv spánek, dostatek bílkovin a rozumně sestavený trénink než jakákoli bylinná kapsle. Přehled dalších doplňků najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>, minerály a vitamíny v sekci <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>'
          '<h2>Tribulus pro ženy</h2>'
          '<p>Část výrobků s kotvičníkem cílí i na ženy, obvykle s odkazem na libido nebo hormonální rovnováhu. Platí pro ně totéž co pro mužské varianty: zdravotní tvrzení pro kotvičník schválené není a výsledky studií nejsou jednoznačné. Ženy, které jsou těhotné, kojí nebo těhotenství plánují, by kotvičník užívat neměly. Stejně tak by se měly předem poradit s lékařem ženy, které užívají hormonální antikoncepci nebo jiné hormonální léky.</p>'
          '<h2>Užívání v cyklech</h2>'
          '<p>Řada výrobců doporučuje užívat kotvičník po určitou dobu a pak udělat pauzu, nejčastěji v řádu několika týdnů. Konkrétní délku cyklu i množství najdete na obalu daného výrobku a ty se mezi značkami liší. Obecné pravidlo pro všechny výrobky zní: nepřekračujte doporučenou denní dávku a nekombinujte víc přípravků s kotvičníkem najednou. Pokud vám doplněk nedělá dobře, nečekejte na konec cyklu a vysaďte ho hned. Při dlouhodobém užívání je rozumné zmínit doplněk při běžné prohlídce u lékaře, zvlášť pokud vám dělají krevní testy.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Výběr podle slova „booster“ nebo podle obrázku svalovce na obalu.</li>'
          '<li>Srovnávání miligramů bez ohledu na procento saponinů a na počet kapslí v porci.</li>'
          '<li>Záměna přepočtu na bylinu za skutečné množství extraktu.</li>'
          '<li>Souběžné užívání několika směsí se zinkem a vitamínem B6, které se sčítají.</li>'
          '<li>Nákup výrobku bez českého popisu a bez uvedené šarže a výrobce.</li></ul>'
          '<h2>Jak vybírat v nabídce Sporteky</h2>'
          '<p>Na kartě produktu vidíte, které české e-shopy daný kotvičník prodávají, jaké mají balení a dopravu. Stejný výrobek se často prodává v několika velikostech nebo jako zvýhodněné dvojbalení, takže si přepočítejte, na kolik dní vám balení vystačí. U bylinných extraktů se vyplatí zkontrolovat i datum minimální trvanlivosti. Pokud si nejste jistí, zda je pro vás kotvičník vhodný, zeptejte se lékárníka dřív, než ho objednáte.</p>',
    faq=[
        ('Co je Tribulus terrestris?', 'Je to latinský název kotvičníku zemního, poléhavé byliny z teplých oblastí s ostnatými plody. Doplňky stravy obsahují extrakt z nati nebo plodů, obvykle standardizovaný na obsah saponinů.'),
        ('Zvyšuje tribulus testosteron?', 'Studie u zdravých mužů to přesvědčivě nepotvrdily a EU pro kotvičník žádné zdravotní tvrzení neschválila. Nápisy jako testosteronový booster jsou marketing. Schválené tvrzení o udržení normální hladiny testosteronu má jen zinek, který bývá v kombinovaných výrobcích.'),
        ('Co znamená 90 % saponinů?', 'Že saponiny podle prohlášení výrobce tvoří 90 % hmotnosti extraktu. Číslo ale záleží i na použité laboratorní metodě, proto je užitečné, když značka uvádí také obsah protodioscinu nebo zveřejňuje rozbor šarže.'),
        ('Čím se liší bulharský tribulus?', 'Pochází z rostlin sbíraných na Balkáně a výrobci uvádějí vyšší obsah protodioscinu. Ověřit se to dá jen podle rozboru konkrétní šarže.'),
        ('Je lepší kapsle, tinktura, nebo čaj?', 'Kapsle se standardizovaným extraktem se nejsnáze porovnávají, protože mají udaný obsah saponinů. U čaje a většiny tinktur obsah účinných látek standardizovaný není. Ve všech případech se řiďte dávkováním na obalu.'),
        ('Kdo by neměl kotvičník užívat?', 'Těhotné a kojící ženy, děti a dospívající. Lidé s hormonálně podmíněným onemocněním, s potížemi s prostatou, ledvinami či játry a ti, kdo pravidelně užívají léky, by se měli nejprve poradit s lékařem.'),
        ('Je tribulus doping?', 'Kotvičník sám na seznamu zakázaných látek WADA není. Doplňky ale mohou být znečištěné, proto závodní sportovci volí výrobky testované v programech typu Informed Sport nebo Kölner Liste.'),
        ('Proč jsou v kapslích i zinek a vitamín B6?', 'Kombinace je u výrobců oblíbená a schválená tvrzení na obalu se pak vztahují k zinku a vitamínu B6, ne ke kotvičníku. Pokud užíváte i jiný doplněk se zinkem, sečtěte si celkové množství.'),
        ('Kde se kotvičník pěstuje?', 'Roste planě v teplých a suchých oblastech jižní Evropy, Asie a Afriky. Pro doplňky stravy se surovina často získává z Balkánu, Indie nebo Číny; zemi původu uvádějí jen některé značky.'),
    ])

# ------------------------------------------------------------------ kurkuma
NEW['kurkuma'] = dict(long=True,
    title='Kurkuma a kurkumin: extrakt 95 %, piperin, kapsle a formy',
    desc='Kurkuma a kurkumin v kapslích, kapkách i BIO prášku. Co znamená 95 % kurkuminoidů, proč piperin a jak porovnat nabídky českých obchodů.',
    intro='<p>Kurkuma dlouhá (Curcuma longa) je rostlina z čeledi zázvorovitých, jejíž oddenek barví kari a hořčici do žluta. Za barvou stojí kurkuminoidy, z nichž nejznámější je kurkumin. V samotném koření ho je jen několik procent, a proto doplňky stravy většinou používají koncentrovaný extrakt. Na trhu jsou kapsle, tablety, olejové kapky, gumové bonbony, shoty se zázvorem i BIO prášek do kuchyně.</p>'
          '<p>Sporteka seřadí nabídky českých obchodů na jednom místě a vy pak nakoupíte v e-shopu, který vám vyhovuje. Najdete tu extrakty s 95 % kurkuminoidů, kurkumin s piperinem z černého pepře, liposomální a tekuté formy i kombinace s boswellií, zázvorem, ostropestřcem, vitamínem D nebo kolagenem. Zastoupené jsou značky ' + B(('gymbeam', 'GymBeam')) + ', NOW Foods, Nutrend, Movit Energy, Golden Natur, MedPharma, Advance Nutraceutics, OstroVit, Scitec nebo Allnature. Příbuzné výrobky hledejte v kategoriích <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a> a <a href="/kolagen-a-klouby/">kolagen a klouby</a>.</p>',
    guide='<h2>Kurkuma, kurkumin a kurkuminoidy</h2>'
          '<p>Kurkuma je rostlina a zároveň koření z jejího sušeného mletého oddenku. Kurkuminoidy jsou skupina žlutých barviv v oddenku, kam patří kurkumin, demethoxykurkumin a bisdemethoxykurkumin. Kurkumin je mezi nimi zastoupen nejvíc. Když etiketa uvádí „kurkumin 95 %“, obvykle jde o extrakt standardizovaný na 95 % všech kurkuminoidů dohromady, ne o čistý kurkumin. Mletá kurkuma z kuchyně a standardizovaný extrakt se tedy obsahem těchto látek liší víc než o řád.</p>'
          '<p>Kurkumin se v potravinářství používá také jako barvivo E 100. Evropský úřad pro bezpečnost potravin pro něj při přehodnocení v roce 2010 potvrdil přijatelný denní příjem 3 mg na kilogram tělesné hmotnosti. Ten se týká barviva v potravinách a nelze ho číst jako doporučení pro doplňky.</p>'
          '<h2>Co smějí výrobci tvrdit</h2>'
          '<p>Kurkumin patří k nejvíce zkoumaným rostlinným látkám a laboratorní pokusy mu připisují řadu vlastností. Z výsledků na buňkách a zvířatech ale nelze odvodit, co udělá kapsle u člověka, a studie u lidí jsou zatím různorodé. Evropská unie pro kurkumu ani kurkumin žádné zdravotní tvrzení neschválila. Stejně jako u ostatních bylin jsou tvrzení pozastavená a čekají na posouzení. Slova jako „detox“, „protizánětlivý“ nebo „pro klouby“ v názvu výrobku tedy nejsou ověřeným slibem.</p>'
          '<p>Pokud výrobek obsahuje i vitamín nebo minerál v dostatečném množství, může uvádět schválené tvrzení – to se ale vztahuje k přidanému vitamínu, ne ke kurkumě. Typickým příkladem jsou kapsle s kurkuminem a <a href="/vitamin-d/">vitamínem D</a>.</p>'
          '<h2>Vstřebávání: piperin, liposomy a další formy</h2>'
          '<p>Kurkumin se ve vodě téměř nerozpouští, z trávicího traktu se ho vstřebá málo a tělo ho rychle přeměňuje. Výrobci to obcházejí několika způsoby. Nejrozšířenější je přidání piperinu, látky z černého pepře, která podle studií zpomaluje odbourávání kurkuminu. Patentovaný extrakt piperinu se prodává pod obchodním názvem BioPerine. Další cestou jsou liposomální, micelární a tekuté formy nebo kurkumin vázaný na fosfolipidy. Některé suroviny mají vlastní ochrannou známku, například C3 Complex.</p>'
          '<p>Výhody svých technologií dokládají výrobci většinou vlastními studiemi a mezi sebou se špatně srovnávají. Při výběru se proto dívejte hlavně na to, kolik kurkuminoidů obsahuje jedna porce, jakou formu výrobce použil a zda obsahuje piperin.</p>'
          + T(['Forma', 'Co to je', 'Poznámka'], [
              ['Extrakt 95 %', 'koncentrát standardizovaný na kurkuminoidy', 'nejběžnější, snadno se porovnává'],
              ['Kurkumin s piperinem', 'extrakt doplněný výtažkem z černého pepře', 'piperin může ovlivnit odbourávání léků'],
              ['Liposomální a micelární', 'kurkumin v lipidových váčcích nebo micelách', 'sledujte obsah kurkuminoidů na porci'],
              ['Tekuté kapsle a olejové kapky', 'kurkumin rozpuštěný v oleji', 'olej usnadňuje polykání i dávkování'],
              ['BIO prášek', 'mleté koření', 'kurkuminoidy jen v jednotkách procent'],
              ['Gumové bonbony a shoty', 'kurkuma se zázvorem v ochucené formě', 'obsahují cukr nebo sladidla'],
              ['Kombinace', 's boswellií, ostropestřcem, kolagenem, D3 nebo Q10', 'zkontrolujte množství každé složky']]) +
          '<h2>Jak číst etiketu</h2>'
          '<ul><li><strong>Množství extraktu na porci</strong> a procento kurkuminoidů, ze kterých si spočítáte jejich skutečný obsah.</li>'
          '<li><strong>Kurkuma, nebo kurkumin:</strong> „kurkuma 500 mg“ může znamenat obyčejné mleté koření, „kurkumin 95 %“ extrakt.</li>'
          '<li><strong>Piperin:</strong> zda je přidán a v jakém množství.</li>'
          '<li><strong>Počet kapslí v porci</strong> a tedy počet dní, na které balení vystačí.</li>'
          '<li><strong>Původ a rozbory:</strong> transparentní značky uvádějí zemi původu suroviny a výsledky testů na těžké kovy.</li>'
          '<li><strong>Obal kapsle a alergeny:</strong> želatina, nebo rostlinná celulóza, případně sója u lecitinu.</li></ul>'
          '<h2>Kombinace s dalšími látkami</h2>'
          '<p>Kurkumu výrobci rádi spojují s jinými rostlinnými extrakty. S boswellií a kolagenem bývá v přípravcích na klouby, s ostropestřcem a artyčokem v produktech označených jako „detox“, se zázvorem v nápojích a gumových bonbonech. Ani boswellie, ani ostropestřec nemají v EU schválené zdravotní tvrzení, takže kombinace nepřináší jistotu, jen víc složek. Rozumné je spočítat si, kolik každé látky v porci skutečně je. U výrobků s kolagenními peptidy, jako je Fortigel, najdete podobné výrobky i v kategorii <a href="/kolagen-a-klouby/">kolagen a klouby</a>, rybí tuk zase v sekci <a href="/omega-3/">omega-3</a>.</p>'
          '<h2>Bezpečnost a léky</h2>'
          '<p>Kurkuma použitá jako koření je pro většinu lidí v pořádku. Koncentrované extrakty jsou jiná situace. Kdo užívá léky na ředění krve nebo proti srážení krve, měl by kurkumin brát jen po poradě s lékařem, protože může jejich účinek ovlivnit. Totéž platí pro lidi se žlučovými kameny či jiným onemocněním žlučníku a jater, pro diabetiky na lécích a pro těhotné a kojící ženy. Piperin navíc může měnit, jak tělo odbourává některé léky.</p>'
          '<p>V Itálii bylo v letech 2018 a 2019 hlášeno asi dvacet případů zánětu jater spojovaných s doplňky s kurkumou. Italské ministerstvo zdravotnictví proto zavedlo povinné varování na obalech pro lidi s onemocněním jater a žlučových cest a v roce 2022 ho rozšířilo. Doporučené dávkování na obalu nepřekračujte, a pokud se objeví potíže, například bolest břicha nebo zežloutnutí kůže, doplněk vysaďte a kontaktujte lékaře.</p>'
          '<h2>Kurkuma v kuchyni, nebo v kapsli</h2>'
          '<p>Mletá kurkuma do kari, polévek, rýže nebo zlatého mléka je levná a chutná, kurkuminu v ní ale bývá málo. Pokud vám jde hlavně o chuť a barvu, stačí kvalitní BIO koření. Kapsle s extraktem kupují ti, kdo chtějí přesně daný obsah kurkuminoidů v každé porci. U koření z nespolehlivých zdrojů bylo v zahraničí, například v Bangladéši, odhaleno i přibarvování chromanem olovnatým, takže se vyplatí kupovat od značek, které uvádějí původ a rozbory. Kurkuma také silně barví plasty, textil i pracovní desku, s olejovými kapkami proto pracujte opatrně.</p>'
          '<h2>Kurkumin a sportovci</h2>'
          '<p>Mezi sportovci se kurkumin prodává hlavně jako doplněk na období po náročném tréninku nebo jako součást přípravků na klouby a šlachy. Studie na toto téma mají malý počet účastníků a liší se formou i množstvím kurkuminu, takže z nich jednoznačný závěr nevyplývá. Schválené zdravotní tvrzení pro tuto oblast neexistuje. Pro regeneraci po tréninku hraje mnohem větší roli spánek, dostatek bílkovin a energie a rozumné rozložení zátěže. Kdo chce kurkumin přesto vyzkoušet, měl by vybírat podle obsahu kurkuminoidů a formy, ne podle sportovního designu obalu.</p>'
          '<h2>Zlaté mléko a další použití v kuchyni</h2>'
          '<p>Oblíbeným způsobem, jak kurkumu zařadit do jídelníčku, je takzvané zlaté mléko: teplé mléko nebo rostlinný nápoj s kurkumou, skořicí, zázvorem a špetkou černého pepře. Kurkuma se hodí také do luštěninových jídel, rizota, pomazánek z cizrny nebo do míchaných vajec, kterým dodá barvu. Protože se kurkuminoidy rozpouštějí lépe v tucích než ve vodě, kuchaři ji obvykle nejdřív krátce osmahnou na oleji nebo másle. Běžné množství koření v jídle se obvykle za problém nepovažuje; opatrnost platí hlavně pro koncentrované extrakty. Kdo užívá léky zmíněné výše a není si jistý, ať se zeptá lékaře.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Kurkumin je citlivý na světlo, proto ho výrobci balí do neprůhledných dóz nebo tmavých lahviček. Doplňky uchovávejte v suchu, mimo dosah přímého slunce a dobře uzavřené. Olejové kapky a tekuté formy po otevření spotřebujte v době, kterou uvádí výrobce. Mletá kurkuma v kuchyni časem ztrácí barvu i vůni, takže se vyplatí kupovat menší balení, které spotřebujete do několika měsíců.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Záměna mleté kurkumy za standardizovaný extrakt kurkuminu.</li>'
          '<li>Porovnávání miligramů bez přepočtu na kurkuminoidy.</li>'
          '<li>Spoléhání na slovo „detox“ nebo „protizánětlivý“ v názvu výrobku.</li>'
          '<li>Užívání vedle léků na ředění krve bez porady s lékařem.</li>'
          '<li>Souběžné užívání několika přípravků s kurkuminem a piperinem najednou.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na stránce produktu porovnáte nabídky několika českých e-shopů a uvidíte balení i dopravu. Kurkumin se často prodává ve dvojbaleních nebo dárkových sadách, proto si přepočítejte, kolik porcí za své peníze dostanete. U gumových bonbonů a shotů hlídejte datum minimální trvanlivosti. Nakupujete vždy přímo v obchodě, který si vyberete, a reklamace i dotazy řešíte s ním.</p>',
    faq=[
        ('Jaký je rozdíl mezi kurkumou a kurkuminem?', 'Kurkuma je rostlina a koření z jejího oddenku. Kurkumin je hlavní žluté barvivo, které v koření tvoří jen několik procent. Doplňky obvykle obsahují extrakt standardizovaný na 95 % kurkuminoidů.'),
        ('Proč se ke kurkuminu přidává piperin?', 'Kurkumin se špatně vstřebává a tělo ho rychle odbourává. Piperin z černého pepře toto odbourávání podle studií zpomaluje. Zároveň ale může ovlivnit odbourávání některých léků, proto se při jejich užívání poraďte s lékařem.'),
        ('Je lepší liposomální kurkumin?', 'Výrobci uvádějí lepší vstřebávání, srovnání různých technologií je ale obtížné, protože je dokládají hlavně vlastní studie. Rozhodující je obsah kurkuminoidů v porci a forma, kterou budete pravidelně užívat.'),
        ('Má kurkumin schválená zdravotní tvrzení?', 'Nemá. Tvrzení u kurkumy i dalších bylin jsou v EU pozastavená a čekají na posouzení. Pokud je na obalu schválené tvrzení, týká se přidaného vitamínu, například vitamínu D.'),
        ('Mohu kurkumin užívat s léky na ředění krve?', 'Jen po poradě s lékařem. Kurkumin může jejich účinek ovlivnit. Opatrní by měli být i lidé s onemocněním žlučníku nebo jater, diabetici na lécích a těhotné a kojící ženy.'),
        ('Stačí kurkuma v jídle?', 'Jako koření dodá chuť a barvu, kurkuminu v ní ale je málo. Kdo chce přesně daný obsah kurkuminoidů, sáhne po standardizovaném extraktu.'),
        ('Proč kurkuma barví?', 'Kurkuminoidy jsou silná žlutá barviva, kurkumin se dokonce používá jako potravinářské barvivo E 100. Skvrny na plastu nebo textilu jdou dolů obtížně.'),
        ('Co znamená C3 Complex nebo BioPerine?', 'Jsou to obchodní názvy patentovaných surovin: C3 Complex je směs kurkuminoidů, BioPerine extrakt piperinu z černého pepře. Uvádějí je výrobci, kteří danou surovinu nakupují.'),
    ])

# ------------------------------------------------------------------ spirulina-chlorella
NEW['spirulina-chlorella'] = dict(long=True,
    title='Spirulina a chlorella: tablety, prášek, mladý ječmen, greens',
    desc='Spirulina, chlorella, mladý ječmen a směsi super greens v tabletách i prášku. Na co se dívat a jak porovnat nabídky českých obchodů.',
    intro='<p>Spirulina a chlorella patří k nejprodávanějším „zeleným“ doplňkům stravy. Spirulina je ve skutečnosti sinice (Arthrospira platensis), tedy fotosyntetizující bakterie, kdežto chlorella je jednobuněčná zelená řasa. Obě se pěstují v nádržích, suší a prodávají jako prášek nebo lisované tablety. Do stejné skupiny se řadí také mladý ječmen, pšeničná tráva a směsi „super greens“, které míchají řasy, trávy, zeleninu i ovoce v prášku.</p>'
          '<p>Sporteka sbírá nabídky českých obchodů, nakoupíte ale přímo v e-shopu, který si vyberete. V kategorii najdete tablety po stovkách kusů, BIO prášky, kapsle, kombinace spiruliny s chlorellou, modrou spirulinu i ochucené greens nápoje. Prodávají je mimo jiné ' + B(('gymbeam', 'GymBeam')) + ', Nupreme, Czech Virus, Amix, Allnature, Topnatur, MedPharma, NOW Foods, Blendea, Nutrisslim nebo USN. Vitamíny hledejte v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>, další doplňky v sekci <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>.</p>',
    guide='<h2>Spirulina, chlorella, mladý ječmen: co je co</h2>'
          '<p>Všechny tyto výrobky jsou zelené a prodávají se vedle sebe, původem se ale dost liší. Rozdíly se vyplatí znát, protože ovlivňují složení, chuť i to, na co se při nákupu dívat.</p>'
          + T(['Výrobek', 'Co to je', 'Typická podoba'], [
              ['Spirulina', 'sinice Arthrospira platensis, pěstovaná v nádržích', 'tablety, prášek, kapsle'],
              ['Chlorella', 'jednobuněčná zelená řasa s pevnou buněčnou stěnou', 'tablety „s narušenou stěnou“, prášek'],
              ['Spirulina + chlorella', 'směs obou v jedné tabletě', 'často BIO, balení po stovkách tablet'],
              ['Modrá spirulina', 'extrakt modrého barviva fykocyaninu', 'prášek k barvení smoothie a kaší'],
              ['Mladý ječmen', 'mladá ječmenná tráva nebo její sušená šťáva', 'prášek, tablety'],
              ['Super greens', 'směs řas, trav, zeleniny a ovoce', 'ochucený prášek k rozmíchání, kapsle']]) +
          '<h2>Co v nich je a co od nich nečekat</h2>'
          '<p>Sušená spirulina obsahuje vysoký podíl bílkovin, obvykle se uvádí kolem 60 % hmotnosti, dále železo, beta-karoten a modré barvivo fykocyanin. Chlorella je bohatá na chlorofyl. V denní porci tablet ale jde o několik gramů, takže jako zdroj bílkovin v jídelníčku téměř nehrají roli. Pokud řešíte příjem bílkovin, podívejte se spíš do kategorie <a href="/proteiny/">proteiny</a>.</p>'
          '<p>Častý omyl se týká vitamínu B12. Spirulina obsahuje převážně takzvaný pseudovitamín B12, který lidský organismus neumí využít. Vegani by se na ni jako na zdroj B12 spoléhat neměli. U chlorelly se obsah využitelné formy liší výrobek od výrobku, a spolehlivým zdrojem tak zůstává doplněk s vitamínem B12.</p>'
          '<p>Pro spirulinu, chlorellu ani mladý ječmen nemá EU schválené žádné zdravotní tvrzení. Tvrzení u rostlin, řas a hub jsou pozastavená a čekají na posouzení. Slova jako „detox“, „čištění organismu“ nebo „alkalizace“ jsou tedy marketing. Pokud směs obsahuje přidané vitamíny nebo minerály v dostatečném množství, smí uvádět tvrzení k nim.</p>'
          '<h2>Čistota: těžké kovy a toxiny sinic</h2>'
          '<p>Řasy a sinice snadno vážou látky z vody, ve které rostou, a kvalita proto hodně závisí na pěstování. EU stanovuje pro doplňky stravy maximální limity olova, kadmia a rtuti, dnes v nařízení (EU) 2023/915, a seriózní výrobci zveřejňují rozbory jednotlivých šarží. Dalším rizikem jsou mikrocystiny, toxiny jiných druhů sinic, které se mohou do sklizně dostat jako příměs. Týká se to hlavně sinic sbíraných z volné přírody, u kultur z kontrolovaných nádrží je riziko menší.</p>'
          '<p>Hledejte proto údaj o zemi původu a způsobu pěstování a případně si u prodejce vyžádejte certifikát rozboru. Označení BIO říká, jak se řasa pěstovala, nikoli že nemůže obsahovat těžké kovy. Spirulinu a chlorellu také nezaměňujte s mořskými chaluhami typu kelp, které mohou obsahovat velké množství jódu.</p>'
          '<h2>Chlorella a buněčná stěna</h2>'
          '<p>Chlorella má pevnou buněčnou stěnu, kterou lidské trávení rozkládá jen špatně. Výrobci proto stěnu mechanicky narušují a na obalu to uvádějí slovy „s narušenou buněčnou stěnou“, anglicky broken cell wall. U chlorelly je to údaj, který stojí za kontrolu. Spirulina celulózní stěnu nemá a její buňky se tráví snadno, proto tento údaj u ní nenajdete.</p>'
          '<h2>Tablety, prášek, nebo směs super greens</h2>'
          '<p>Tablety jsou nejpohodlnější a nemají výraznou chuť, jedna ale obvykle váží jen 250 až 500 mg. Denní porce tak může znamenat hrst tablet a balení se 750 nebo 1000 kusy vydrží kratší dobu, než se na první pohled zdá. Přepočtěte si proto obsah na gramy na porci a počet porcí v balení. Prášek je na gram obvykle výhodnější a hodí se do smoothie, má ale výraznou chuť, kterou mnoho lidí přirovnává k mořským řasám nebo k rybníku.</p>'
          '<p>Směsi super greens, například od Czech Virus, Amix nebo Blendea, jsou ochucené a dobře se pijí. Kromě řas a trav obsahují ovocné prášky, sladidla, někdy probiotika nebo enzymy. Když složení uvádí jen „proprietární směs“ s celkovou hmotností, nevíte, kolik spiruliny nebo chlorelly v porci opravdu je. Lepší jsou výrobky, které uvádějí množství každé složky.</p>'
          '<p>Modrá spirulina je jiný výrobek než klasická zelená. Jde o extrakt barviva fykocyaninu a kupuje se hlavně kvůli výrazné modré barvě smoothie bowlů, kaší nebo dezertů.</p>'
          '<h2>Mladý ječmen a pšeničná tráva</h2>'
          '<p>Mladý ječmen se sklízí jako tráva v době, kdy ještě netvoří zrno. Prodává se buď jako mletá sušená tráva, nebo jako sušená šťáva z mladého ječmene, kterou výrobci popisují jako jemnější na chuť. Rozdíl najdete ve složení. Lidé s celiakií by měli hledat výslovné označení „bez lepku“, protože u obilných trav hrozí kontaminace. Podobně se zpracovává i pšeničná tráva.</p>'
          '<h2>Kdo by měl zpozornět</h2>'
          '<ul><li><strong>Léky na ředění krve:</strong> chlorella i obilné trávy obsahují vitamín K, který může ovlivnit účinek warfarinu. Poraďte se s lékařem.</li>'
          '<li><strong>Fenylketonurie:</strong> spirulina obsahuje fenylalanin, lidé s touto poruchou by se jí měli vyhnout.</li>'
          '<li><strong>Těhotné a kojící ženy a děti:</strong> užívání konzultujte s lékařem.</li>'
          '<li><strong>Lidé užívající léky nebo s autoimunitním onemocněním:</strong> před užíváním se poraďte s lékařem nebo lékárníkem.</li></ul>'
          '<p>Nepřekračujte dávkování uvedené na obalu. Na začátku užívání se může objevit nadýmání nebo změna barvy stolice, což souvisí s vysokým obsahem chlorofylu.</p>'
          '<h2>Co dalšího je v tabletě</h2>'
          '<p>Kvalitní tablety spiruliny nebo chlorelly bývají lisované ze stoprocentní řasy bez dalších přísad. Levnější výrobky mohou obsahovat plnidla, protispékavé látky nebo pojiva, která snižují podíl samotné řasy v tabletě. Ve složení proto hledejte, zda je spirulina nebo chlorella jedinou složkou, případně kolik procent tablety tvoří. U kapslí zkontrolujte i materiál obalu, protože želatinové kapsle nejsou vhodné pro vegany a vegetariány, kteří zelené doplňky kupují velmi často.</p>'
          '<h2>Jak zelené doplňky zařadit do dne</h2>'
          '<p>Tablety se zapíjejí vodou a mnoho lidí je bere k jídlu, protože se tak lépe snášejí. Prášek se dá vmíchat do ovocného smoothie, jogurtu nebo šťávy, kde jeho chuť zanikne lépe než ve vodě. Někteří výrobci doporučují začít nižší porcí a postupně ji zvyšovat až na množství uvedené na obalu; doporučenou denní dávku ale nepřekračujte. Ochucené směsi super greens se míchají v šejkru s vodou podobně jako protein.</p>'
          '<p>Zelený doplněk nenahrazuje zeleninu a ovoce. Porce prášku nebo několika tablet obsahuje řádově méně vlákniny a tekutin než talíř zeleniny, a jídelníček chudý na zeleninu tak nevyrovná.</p>'
          '<h2>Zelené doplňky a sport</h2>'
          '<p>Sportovci kupují spirulinu a směsi greens nejčastěji jako pojistku v obdobích, kdy jedí méně čerstvé zeleniny, třeba na soustředění nebo na cestách. Na výkon ani regeneraci jim žádné schválené tvrzení nesvědčí. U směsí určených sportovcům bývají přidané vitamíny, elektrolyty nebo probiotika, a pak se vyplatí zkontrolovat, zda se jejich množství nesčítá s tím, co už užíváte v jiných doplňcích.</p>'
          '<h2>Skladování</h2>'
          '<p>Prášek ze spiruliny i chlorelly natahuje vlhkost a na vzduchu ztrácí barvu, proto ho po každém použití pečlivě uzavřete a skladujte v suchu a temnu. U sáčků se zipem kontrolujte, zda zip opravdu dovírá.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Porovnávání podle počtu tablet bez ohledu na jejich hmotnost.</li>'
          '<li>Spoléhání na spirulinu jako na zdroj vitamínu B12.</li>'
          '<li>Nákup chlorelly bez údaje o narušené buněčné stěně.</li>'
          '<li>Volba levné směsi, ve které je řas jen nepatrně a většinu tvoří ovocný prášek a sladidla.</li>'
          '<li>Přehlédnutí původu suroviny a chybějící rozbor na těžké kovy.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu porovnáte nabídky několika českých obchodů i velikosti balení. U velkých balení tablet si přepočítejte, za jak dlouho je spotřebujete, a hlídejte datum minimální trvanlivosti; otevřený prášek skladujte suchý a dobře uzavřený. Hledáte-li vitamíny a minerály v přesných dávkách, sáhněte spíš po <a href="/multivitaminy/">multivitamínech</a>. Pro chutné zdravější svačiny nahlédněte do kategorie <a href="/fit-potraviny/">fit potraviny</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi spirulinou a chlorellou?', 'Spirulina je sinice, tedy fotosyntetizující bakterie, chlorella jednobuněčná zelená řasa s pevnou buněčnou stěnou. Spirulina má vyšší podíl bílkovin a obsahuje modré barvivo fykocyanin, chlorella je bohatá na chlorofyl.'),
        ('Proč se u chlorelly uvádí narušená buněčná stěna?', 'Pevnou stěnu chlorelly lidské trávení rozkládá špatně. Výrobci ji proto mechanicky narušují, aby byl obsah buněk přístupnější. U spiruliny se tento údaj neuvádí, protože takovou stěnu nemá.'),
        ('Je spirulina dobrý zdroj vitamínu B12?', 'Není. Obsahuje převážně pseudovitamín B12, který lidské tělo nevyužije. Vegani by měli B12 doplňovat samostatným přípravkem.'),
        ('Mají spirulina a chlorella schválená zdravotní tvrzení?', 'Ne. Pro spirulinu, chlorellu ani mladý ječmen nemá EU schválené žádné zdravotní tvrzení. Nápisy jako detox nebo alkalizace jsou marketing.'),
        ('Jak poznám kvalitní spirulinu nebo chlorellu?', 'Podle uvedené země původu, způsobu pěstování a rozboru šarže na těžké kovy a mikrocystiny. Označení BIO popisuje způsob pěstování, ne výsledky rozboru.'),
        ('Co je modrá spirulina?', 'Extrakt modrého barviva fykocyaninu ze spiruliny. Používá se hlavně k barvení smoothie, kaší a dezertů a není to totéž co klasická zelená spirulina.'),
        ('Je mladý ječmen bez lepku?', 'Tráva se sklízí před tvorbou zrna, riziko kontaminace ale existuje. Lidé s celiakií by měli hledat výslovné označení bez lepku.'),
        ('Kdo by měl být se zelenými doplňky opatrný?', 'Lidé užívající warfarin kvůli vitamínu K v chlorelle a obilných travách, lidé s fenylketonurií u spiruliny, těhotné a kojící ženy, děti a všichni, kdo užívají léky. Poraďte se s lékařem.'),
    ])

# ------------------------------------------------------------------ sejkry
NEW['sejkry'] = dict(long=True,
    title='Šejkry na protein: objem, sítko, Tritan, nerez, zásobník',
    desc='Šejkry na protein od 400 do 800 ml: se sítkem, kuličkou, zásobníkem, z Tritanu i nerezu. Na co se dívat a jak porovnat nabídky českých obchodů.',
    intro='<p>Šejkr je uzavíratelná nádoba, ve které za pár vteřin rozmícháte protein, gainer nebo iontový nápoj bez hrudek. Na první pohled nejde o nic složitého, přesto se šejkry liší objemem, materiálem, způsobem míchání i tím, jak dobře těsní. Rozdíl obvykle poznáte až po několika týdnech: jestli víčko neprotéká v tašce, jestli se šejkr dá pořádně vymýt a jestli nezačne zapáchat.</p>'
          '<p>Sporteka dá nabídky českých obchodů vedle sebe, objednáváte ale přímo v e-shopu, který si vyberete. V kategorii najdete klasické plastové šejkry se sítkem, modely z Tritanu, nerezové a termo varianty, šejkry se zásobníky na prášek a tablety i licencované motivy s komiksovými hrdiny. Zastoupené jsou značky ' + B(('gymbeam', 'GymBeam')) + ', Amix, Nutrend, Scitec Nutrition, MyProtein, Extrifit, Fitforce, Smart Shake nebo Performa. Další nádoby na pití najdete v kategorii <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>',
    guide='<h2>Jaký objem zvolit</h2>'
          '<p>Nejběžnější jsou šejkry o objemu 500 až 700 ml, nabídka ale sahá od menších 400ml modelů po 800ml a větší. Při výběru vycházejte z toho, kolik tekutiny na jednu porci používáte. Množství vody nebo mléka uvádí výrobce proteinu na obalu. Nad hladinou musí zůstat volný prostor, jinak se nápoj špatně promíchá a tlačí na víčko. Pro gainer, kde se míchá víc prášku i tekutiny, se hodí větší objem. Menší šejkr je zase lehčí a lépe se vejde do sportovní tašky.</p>'
          '<p>Na boku bývá stupnice v mililitrech, často i v uncích. Vyplatí se, aby byla vylisovaná nebo dobře potištěná a čitelná i zevnitř, protože podle ní odměřujete tekutinu.</p>'
          '<h2>Sítko, kulička, nebo nic</h2>'
          '<p>Klasický šejkr má pod víčkem plastovou mřížku neboli sítko. Při třepání přes ni nápoj protéká a hrudky se rozbijí. Mřížku jde vyndat, takže šejkr poslouží i jako obyčejná láhev. Jiné modely místo sítka používají volnou míchací kuličku nebo pružinu z nerezové oceli, která se v nádobě při třepání pohybuje a prášek rozbíjí. Kulička si dobře poradí i s hustšími nápoji, zato při třepání hlasitě chrastí.</p>'
          '<p>Na trhu existují také elektrické šejkry s malým motorkem na baterii nebo s nabíjením přes USB, které nápoj rozmíchají bez třepání. Jsou těžší, dražší a mytí je složitější kvůli části s motorem. Pro většinu lidí stačí obyčejný šejkr se sítkem.</p>'
          '<h2>Materiál: plast, Tritan, nebo nerez</h2>'
          + T(['Materiál', 'Výhody', 'Na co pamatovat'], [
              ['Polypropylen (PP)', 'lehký, levný, odolný proti pádu', 'je spíš matný, časem může nasát pach'],
              ['Tritan', 'čirý jako sklo, tvrdý, bez BPA', 'vyšší cena než u běžného plastu'],
              ['Nerezová ocel', 'nenasává pach, dlouhá životnost', 'není průhledná, je těžší'],
              ['Dvoustěnná nerez (termo)', 'drží nápoj déle studený', 'mytí v myčce povoluje jen část výrobců'],
              ['Plast s potiskem', 'licencované motivy, výrazné barvy', 'potisk může v myčce časem vyblednout']]) +
          '<p>Bisfenol A obsahovaly hlavně starší polykarbonátové láhve. Polypropylen ani Tritan ho ke své výrobě nepotřebují, a výrobci je proto označují jako „BPA free“. EU navíc používání BPA v materiálech pro styk s potravinami zakázala nařízením (EU) 2024/3190. Platí od ledna 2025 a pro většinu výrobků jeho přechodné období skončilo v červenci 2026. Při nákupu hledejte symbol skleničky s vidličkou, který označuje materiál vhodný pro styk s potravinami.</p>'
          '<p>Nerezový šejkr ocení ten, kdo nesnáší pach starého proteinu nebo chce nápoj nosit déle s sebou. Má ale jednu nevýhodu: nevidíte dovnitř, takže hůř poznáte, zda je prášek rozmíchaný a nádoba čistá. Do mikrovlnné trouby nepatří kovové šejkry ani plastové s kovovou kuličkou.</p>'
          '<h2>Těsnost a víčko</h2>'
          '<p>Nejčastější stížností na šejkry je protékání. Většina modelů má šroubovací víčko a malé odklopné víčko na pití, některé i poutko na prst. Těsnost zajišťuje silikonové těsnění ve víčku nebo přesné dosednutí mřížky. Když šejkr začne téct, zkontrolujte nejprve, zda je těsnění na místě a není po mytí přetočené, a zda je správně usazené sítko. Šejkr také nepřeplňujte až po okraj.</p>'
          '<p>Horké nápoje v uzavřeném šejkru netřepejte. Teplem vzniká v nádobě tlak a víčko se může prudce otevřít a obsah vystříknout. Ze stejného důvodu se nehodí ani na sycené nápoje.</p>'
          '<h2>Zásobníky a přihrádky</h2>'
          '<p>Pro cestování a pro ty, kdo jdou do posilovny rovnou z práce, jsou praktické šejkry se zásobníky. Pod hlavní nádobou se našroubuje jedna nebo více přihrádek, do kterých si nasypete odměřenou porci proteinu nebo <a href="/kreatin/">kreatinu</a>. Některé modely mají i malou přihrádku na kapsle a tablety. Tyto šejkry jsou vyšší a mají víc závitů, a tedy víc míst, kde se může usazovat prášek, takže potřebují důkladnější mytí. Před nákupem ověřte, kolik prášku se do zásobníku vejde.</p>'
          '<h2>Mytí, myčka a zápach</h2>'
          '<p>Zbytky proteinu, zejména s mlékem, začnou v uzavřeném šejkru během pár hodin kysnout. Nejjednodušší prevencí je vypláchnout ho hned po vypití, i když ho doma umyjete pořádně. Většinu plastových šejkrů lze mýt v myčce, obvykle v horním koši; přesné pokyny najdete u výrobku. Nerezové dvoustěnné modely a šejkry s potiskem často vyžadují ruční mytí.</p>'
          '<ul><li>Po umytí nechte šejkr i víčko schnout zvlášť a otevřené.</li>'
          '<li>Na zápach pomůže namočení do teplé vody s jedlou sodou nebo octem.</li>'
          '<li>Mřížku a těsnění vyndávejte, usazuje se pod nimi nejvíc nečistot.</li>'
          '<li>Poškrábaný plast, který zapáchá i po namočení, je čas vyměnit.</li></ul>'
          '<h2>K čemu všemu šejkr poslouží</h2>'
          '<p>Kromě <a href="/proteiny/">proteinů</a> a <a href="/gainery/">gainerů</a> se v šejkru dobře míchají <a href="/iontove-napoje/">iontové nápoje</a> v prášku, aminokyseliny, instantní kaše nebo těsto na proteinové palačinky. Bez mřížky poslouží jako obyčejná láhev na vodu. Kdo potřebuje láhev do držáku na kole, najde ji spíš mezi cyklistickými láhvemi, protože šejkry mají jiný tvar a do košíku se většinou nevejdou.</p>'
          '<h2>Licencované motivy a dětské šejkry</h2>'
          '<p>V nabídce najdete i šejkry s potiskem komiksových a filmových postav, například šejkry Performa s hrdiny komiksů DC. Kupují se často jako dárek nebo pro dospívající sportovce. Funkčně se od běžných šejkrů neliší, rozhoduje stejně objem, těsnost a mytí. Potisk ale bývá citlivější na myčku a na drhnutí drátěnkou, a pokud má šejkr vydržet hezký, myjte ho raději ručně.</p>'
          '<p>Při výběru na cesty zohledněte i hmotnost a tvar. Plastový šejkr je lehký a při pádu na dlažbu většinou přežije, nerezový je těžší, ale vydrží roky. Úzký model se lépe vejde do bočních kapes batohu, široký zase snáz vymyjete rukou až na dno.</p>'
          '<h2>Šejkr, nebo mixér</h2>'
          '<p>Šejkr stačí na prášky, které se rozpouštějí ve vodě nebo v mléce. Pokud do nápoje přidáváte ovoce, ovesné vločky, arašídové máslo nebo led, šejkr si s nimi neporadí a lepší volbou je stolní mixér nebo malý smoothie mixér s lahví. Šejkr naopak vyhraje tam, kde potřebujete nápoj připravit kdekoli, třeba v šatně nebo v autě, a bez elektřiny. Mnoho lidí proto má doma obojí: mixér na snídaňové shaky a šejkr do tašky.</p>'
          '<h2>Na co se podívat před koupí</h2>'
          '<ul><li><strong>Objem</strong> podle porce, kterou obvykle připravujete.</li>'
          '<li><strong>Způsob míchání:</strong> sítko, kulička, nebo kombinace obojího.</li>'
          '<li><strong>Materiál</strong> a označení pro styk s potravinami.</li>'
          '<li><strong>Víčko:</strong> šroubovací uzávěr, těsnění a odklopné pítko.</li>'
          '<li><strong>Mytí:</strong> zda výrobce povoluje myčku a jestli se dají všechny díly rozebrat.</li>'
          '<li><strong>Doplňky:</strong> zásobník na prášek, poutko na nošení, stupnice.</li></ul>'
          '<p>Pokud trénujete několikrát týdně, vyplatí se mít šejkry dva. Zatímco jeden schne, druhý je připravený v tašce, a nemusíte nosit mokrou nádobu ani míchat v neumytém šejkru. Levnější modely navíc časem praskají v závitech nebo na pantu víčka, takže záložní kus se hodí.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš malý objem, ve kterém se porce nedá pořádně protřepat.</li>'
          '<li>Nechávání zbytku nápoje v šejkru do druhého dne.</li>'
          '<li>Třepání horkého nápoje v uzavřené nádobě.</li>'
          '<li>Mytí dekorovaného nebo dvoustěnného šejkru v myčce proti pokynům výrobce.</li>'
          '<li>Zapomenuté těsnění nebo špatně nasazené sítko, které způsobí protékání.</li></ul>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Na kartě produktu porovnáte nabídky českých obchodů, dostupné barvy a velikosti. Stejný model se často prodává v několika objemech, například 400 a 700 ml, tak si zkontrolujte, kterou variantu objednáváte. Šejkr je levná věc, proto se ho vyplatí přiobjednat k proteinu nebo k láhvi v obchodě, kde nakupujete i další zboží, a ušetřit tím na dopravě. Další nádoby najdete v kategorii <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>',
    faq=[
        ('Jaký objem šejkru zvolit?', 'Pro běžnou porci proteinu stačí 500 až 700 ml. Na gainery se hodí větší objem, protože se v nich míchá víc prášku i tekutiny. Vždy by měl zůstat volný prostor nad hladinou.'),
        ('Je lepší šejkr se sítkem, nebo s kuličkou?', 'Sítko pod víčkem rozbije hrudky u běžného proteinu a dá se vyndat. Míchací kulička nebo pružina si lépe poradí s hustšími nápoji, ale při třepání chrastí. Obojí funguje, záleží na zvyku.'),
        ('Co je Tritan?', 'Čirý a tvrdý plast bez bisfenolu A, který vypadá podobně jako sklo a je odolnější proti nárazu. Šejkry z něj bývají dražší než z běžného polypropylenu.'),
        ('Proč šejkr protéká?', 'Nejčastěji kvůli chybějícímu nebo přetočenému těsnění, špatně nasazenému sítku nebo přeplnění. Protékat může i víčko, které je poškozené nebo zdeformované vysokou teplotou.'),
        ('Mohu šejkr mýt v myčce?', 'Většinu plastových ano, obvykle v horním koši. Nerezové dvoustěnné modely a šejkry s potiskem často vyžadují ruční mytí. Řiďte se pokyny výrobce.'),
        ('Jak se zbavit zápachu ze šejkru?', 'Vypláchněte ho hned po použití, nechte ho schnout otevřený a při zápachu ho namočte do teplé vody s jedlou sodou nebo octem. Nerezový šejkr pach nenasává.'),
        ('Mohu v šejkru míchat horké nápoje?', 'Třepat horký nápoj v uzavřené nádobě se nedoporučuje. Vzniká tlak a víčko se může prudce otevřít. Totéž platí pro sycené nápoje.'),
        ('K čemu je šejkr se zásobníkem?', 'Do přihrádek pod nádobou si nasypete odměřenou porci proteinu nebo kreatinu, případně tablety. Hodí se na cesty a do práce, jen vyžaduje důkladnější mytí závitů.'),
        ('Je nerezový šejkr lepší než plastový?', 'Nerez nenasává pach, nepoškrábe se tak snadno a vydrží roky, je ale těžší a nevidíte do něj. Plastový šejkr je lehčí, levnější a průhledný. Pro běžné použití v posilovně poslouží oba stejně dobře.'),
    ])
