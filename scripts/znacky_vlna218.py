"""sporteka.cz — brand page texts wave 218: shimano, outerstuff, northfinder, calvin-klein.
Only what follows from the catalogue categories and product names; no history, prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ shimano
NEW['shimano'] = dict(
    title='Shimano: cyklo komponenty a rybářské navijáky',
    desc='Shimano v katalogu sporteky: kazety, řetězy, brzdy, pedály, tretry a rybářské navijáky s pruty. Jak vybrat řadu, rychlost a kompatibilitu dílů.',
    intro='<p>Shimano je v našem katalogu jednou z mála značek, které potkáte u dvou naprosto odlišných koníčků. Většina nabídky patří cyklistice: kazety, řetězy, přehazovačky, řadicí páčky, brzdové destičky, středová složení, náboje a pedály. Druhá velká část míří k vodě, protože najdete i navijáky, pruty, šňůry a nástrahy. '
          'Zbytek tvoří cyklistické tretry a několik kousků posilovacího vybavení. Tato stránka vysvětluje, jak se v takové šíři zorientovat. U <a href="/cyklo-pohon/">pohonu kola</a> jde hlavně o počet rychlostí a stupňovitost řad, u <a href="/cyklo-brzdy/">brzd</a> o typ destiček a u <a href="/rybarske-navijaky/">rybářských navijáků</a> o velikost a určení. Porovnáte tu nabídku obchodů, aniž byste museli otevírat desítky e-shopů, a zjistíte, kdy se vyplatí sáhnout po vyšší řadě.</p>',
    guide='<h2>Co Shimano v katalogu nabízí</h2>'
          '<p>Podle názvů zboží i zařazení do kategorií rozpoznáte tři velké okruhy. Největší je cyklistika, kde převažuje <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a> a po něm <a href="/cyklo-pohon/">pohon</a> a <a href="/cyklo-brzdy/">brzdy</a>. Druhým okruhem je rybolov s navijáky, pruty, vlasci a nástrahami. Třetí, nejmenší, tvoří tretry, pumpy a nářadí a pár položek z fitness oddělení. Barevně dominuje vícebarevné provedení a černá, což u mechanických dílů dává smysl: o vzhledu rozhoduje povrchová úprava kovu a lakované detaily.</p>'
          + T(['Oblast', 'Typické zboží', 'Na co si dát pozor'], [
              ['Pohon kola', 'kazety, řetězy, přehazovačky, řadicí páčky, kliky', 'počet rychlostí, rozsah zubů, kompatibilita těch tří částí'],
              ['Brzdy', 'destičky, brzdové komponenty', 'typ destičky a tvar pro konkrétní třmen'],
              ['Kola a náboje', 'zapletená kola, ráfky, náboje', 'rozteč, osa, typ brzdy'],
              ['Pedály a obuv', 'pedály, tretry', 'systém zacvakávání, tvar kufru'],
              ['Rybolov', 'navijáky, pruty, vlasce, nástrahy', 'velikost, převod, dostatečná zásoba šňůry'],
              ['Nářadí', 'pumpy, klíče, výrobky na údržbu', 'ventily a tlak, určení k silnici nebo horskému kolu']]) +
          '<h2>Řady cyklistických komponentů: jak číst názvy</h2>'
          '<p>U kazet a přehazovaček uvidíte jména jako Acera, Alivio, Deore, XT nebo Dura-Ace, k nim kódy typu CS-M5100 nebo RD-M8100. Jména označují třídu komponentu, kód pak konkrétní model. Obecně platí, že vyšší řada bývá lehčí, přesněji cvaká a déle drží, zatímco nižší řady jsou levnější a pro běžné jezdění bohatě stačí. Tuto hierarchii ale berte jako orientační: stejnou třídu mají v nabídce horská i silniční sady a názvy se mezi generacemi liší. Přesné pořadí vždy ověřte ve specifikaci u produktu.</p>'
          '<p>Praktické pravidlo je jednoduché. Pro městské a trekové kolo, kde nejde o váhu, uvažujte o středních řadách, které se dobře seřizují a servis je všude dostupný. Pro horské kolo s rozsáhlejším stoupáním je výhodná široká kazeta s velkým rozdílem mezi nejmenším a největším pastorkem. Pro silnici zase hledejte jemný přírůstek mezi zuby, aby se při změně rychlosti nezměnil kadence skokem. Jestli váháte, který stupeň zvolit, porovnejte u každé řady, zda se dá doplnit i bez výměny všeho ostatního.</p>'
          '<h2>Kompatibilita pohonu: tři věci, které musí sedět</h2>'
          '<p>Nejčastější chyba při nákupu dílů je kombinace nekompatibilních prvků. Při výměně částí převodu musí souhlasit počet rychlostí na kazetě, řetězu a řadicí páčce. Devítirychlostní kazeta se jinak spáruje s řetězem pro devět rychlostí; dvanáct rychlostí má užší řetěz a jiný rozměr zubů. Druhou podmínkou je kapacita přehazovačky: její rozsah se uvádí u produktu a omezuje největší pastorek, který ještě zvládne. Třetí je těleso nábojové vložky, kam se kazeta nasouvá, a které se liší podle generace a ceny náboje.</p>'
          '<ol><li>Zjistěte počet rychlostí na stávajícím kole, nejlépe spočítáním pastorků.</li>'
          '<li>Zkontrolujte, jakou kazetu a jaký typ tělesa náboje v kole máte.</li>'
          '<li>Při přidání většího pastorku ověřte maximální kapacitu přehazovačky a délku řetězu.</li>'
          '<li>Opotřebovaný řetěz měňte spolu s kazetou, jinak se nové zuby rychle ohlodají.</li>'
          '<li>Při změně rychlostí zvolte celou skupinu, nikoli jednotlivé díly, aby řazení fungovalo hladce.</li></ol>'
          '<h2>Brzdové destičky: polymer a kov</h2>'
          '<p>V názvech destiček se objevuje označení polymerové s chladičem a kovové. Polymerové (organické) destičky brzdí tiše, dobře reagují od prvního stisknutí a méně namáhají kotouč. Kovové (sintrované) jsou odolnější proti vyhoření a na dlouhých sjezdech či v mokru drží výkon déle, bývají ale hlučnější. Chladič je hliníkové žebro na zadní straně destičky; odvádí teplo a pomáhá při dlouhé zátěži. Kód destičky určuje, do kterého třmenu patří, proto vždy porovnejte kód se stávající destičkou, nebo s popisem třmenu.</p>'
          '<p>Opotřebení poznáte podle tloušťky materiálu: když ze základní desky zbývá jen tenká vrstva, jde o poslední chvíli na výměnu. Kotouč zbytečně nezatěžujte olejem z rukou nebo z mazadla řetězu, protože mastnota brzdný účinek na dlouho zhorší. Po výměně nechte nové destičky zabrzdit několikrát střídavě z menší rychlosti, aby se k sobě přizpůsobily s kotoučem. Další díly a nářadí najdete u kategorie <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Kola, náboje a pedály</h2>'
          '<p>V kategorii <a href="/cyklo-kola-a-rafky/">zapletených kol, ráfků a nábojů</a> se Shimano objevuje hlavně jako výrobce nábojů, kolem kterých se pak plete. Při koupi si ověřte rozteč zadního náboje, typ osy (rychloupínák nebo pevná osa) a to, zda je určen pro kotoučovou, nebo ráfkovou brzdu. Pedály najdete v samostatné kategorii <a href="/cyklo-pedaly/">pedály</a> a v přehledu <a href="/shimano-pedaly/">pedály Shimano</a>. Systém zacvakávání SPD, který se objevuje u modelů s označením PD-M, slouží na horská a trekingová kola a tretry s ním jsou pohodlné i na chůzi, protože kufr je zapuštěný v podešvi. Silniční pedály fungují s odlišným typem kufru a jsou určené k čistému šlapání.</p>'
          '<p>K pedálům patří <a href="/cyklisticka-obuv/">cyklistické tretry</a>. Hledejte tvar, který odpovídá vašemu stylu: pevnější podešev je výhodná pro výkon, měkčí pro občasné pěší úseky. Při výběru velikosti počítejte s tenkou cyklistickou ponožkou a s tím, že chodidlo při jízdě mírně otéká. Zacvakávání zkoušejte v tretrách doma, než na něm začnete jezdit v dopravě.</p>'
          '<h2>Rybářské navijáky, pruty a šňůry</h2>'
          '<p>Druhá polovina nabídky patří vodě. U <a href="/rybarske-navijaky/">navijáků</a> rozhoduje velikost a určení: menší typy se hodí na lov malých ryb a na lehké nástrahy, větší na těžší návnady a dlouhé nahazování. Samostatný přehled najdete u <a href="/navijaky-shimano/">navijáků Shimano</a>. K tomu se vybírá odpovídající <a href="/rybarske-pruty/">rybářský prut</a>: akce a délka určují, jak daleko dohodíte a jak citlivě prut přenese záběr. Navijákový systém, prut a vlasec by měly tvořit sadu, kterou doplníte podle místa lovu. Vlasce a pletené šňůry zkoumejte v kategorii <a href="/vlasce-a-snury/">vlasce a šňůry</a> a nástrahy v oddíle <a href="/nastrahy-a-navnady/">nástrahy a návnady</a>.</p>'
          + T(['Typ lovu', 'Na co se zaměřit u navijáku', 'Šňůra'], [
              ['Lov na malé nástrahy', 'nízká hmotnost, plynulý chod brzdy', 'tenký vlasec nebo jemná pletená šňůra'],
              ['Přívlač dravců', 'rychlý převod, odolná brzda', 'pletená šňůra s fluorokarbonovým návazcem'],
              ['Dlouhé nahazování', 'větší cívka, dobré vedení šňůry', 'hladká šňůra, která se nezamotává'],
              ['Silný rybolov na řece', 'robustní tělo, spolehlivá brzda', 'pevnější vlasec nebo silnější šňůra']]) +
          '<p>Před koupí zvažte, kde a na koho budete lovit. Při delších trasách je lehčí zařízení pohodlnější, u těžkého zařízení zase záleží na odolnosti. Pro srovnání s konkurencí se podívejte na značky <a href="/znacka/daiwa/">Daiwa</a> a <a href="/znacka/abu-garcia/">Abu Garcia</a>, a v cyklistice na <a href="/znacka/sram/">SRAM</a>. Rozdíl mezi nimi je spíš v systému a filozofii než v jedné lepší variantě; hlavně musíte dodržet kompatibilitu v celé sestavě.</p>'
          '<h2>Péče, životnost a údržba</h2>'
          '<p>Pohon kola vydrží tím déle, čím častěji se čistí a maže. Po jízdě v bahně opláchněte řetěz, kazetu a kliky, vysušte je a naneste mazivo vhodné pro dané podmínky. Mokré mazivo drží v dešti, suché se hodí na prašné trasy, ale mizí rychleji. Řetěz kontrolujte měrkou opotřebení, protože včasná výměna ušetří dražší kazetu. Brzdové destičky měňte dříve, než odejde celá vrstva materiálu.</p>'
          '<p>Rybářský naviják opláchněte po lovu ve slané či špinavé vodě čistou vodou, nechte uschnout a lehce namažte pohyblivé díly. Brzdu cívky na konci sezóny povolte, aby se nestlačily kotoučky. Šňůru po sezóně vyměňte nebo aspoň zkraťte o opotřebený konec. Obecně platí, že mechanika, která se po každém použití ošetří, slouží násobně déle.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Cyklistické díly se obvykle zlevňují na konci sezóny, tedy na podzim a v zimě, a při přechodu na novou generaci. Rybářské vybavení bývá výhodnější před sezónou i po jejím skončení. Slevu posuzujte přes kód produktu: stejná kazeta se v obchodech prodává pod mírně odlišnými názvy, a proto se vyplatí porovnat model a počet rychlostí, nikoli celý popis. Ověřte také, zda je zboží nové v původním balení, protože v nabídce se objevují i položky bez obalu. Při větších nákupech sledujte dopravu a lhůtu na vrácení.</p>',
    faq=[
        ('Co všechno Shimano v katalogu sporteky nabízí?',
         'Největší část tvoří cyklistické komponenty: kazety, řetězy, přehazovačky, řazení, brzdové destičky, středová složení, náboje a pedály. K nim patří tretry. Druhým oborem je rybolov, kde najdete navijáky, pruty, vlasce a nástrahy, plus několik posilovacích kousků.'),
        ('Jak poznám, že se kazeta hodí na moje kolo?',
         'Zjistěte počet rychlostí, typ tělesa náboje a kapacitu přehazovačky. Kazeta musí odpovídat řetězu a řadicí páčce a největší pastorek nesmí překročit možnosti přehazovačky. Když si nejste jistí, porovnejte kódy se stávajícími díly.'),
        ('Jsou vyšší řady vždy lepší volba?',
         'Ne vždy. Vyšší řada bývá lehčí a přesnější, ale pro běžné jezdění stačí střední. Důležitější je správná kompatibilita, čistý řetěz a seřízení. Do závodu nebo náročného terénu se vyšší řada vyplatí víc než do města.'),
        ('Mám zvolit polymerové, nebo kovové brzdové destičky?',
         'Polymerové jsou tišší a šetrnější ke kotouči, kovové odolávají dlouhému zatížení a mokru. Pro běžné trasy volte polymerové, pro dlouhé sjezdy a deště spíš kovové. V každém případě sedí jen destičky s kódem určeným pro váš třmen.'),
        ('Jak často vyměňovat řetěz?',
         'Když ho měrka opotřebení označí jako natažený. Včasná výměna chrání zuby kazety a převodníku, takže vám pohon vydrží mnohem déle. Jezdíte-li často v bahně nebo dešti, kontrolujte řetěz častěji.'),
        ('Co znamená SPD u pedálů?',
         'Je to systém zacvakávání, který spojí botu s pedálem pomocí kufru zapuštěného v podešvi. Hodí se na horská a trekingová kola, protože se v takových botách dá i chodit. Silniční pedály používají jiný kufr a nejsou záměnné.'),
        ('Jak vybrat rybářský naviják?',
         'Podle lovu: menší velikost na malé nástrahy, větší na těžší návnady a dálku. Sledujte převod, plynulost brzdy a kapacitu cívky. Naviják kombinujte s prutem odpovídající akce a se šňůrou, která se hodí na dané vody.'),
        ('Lze kombinovat Shimano s komponenty jiných výrobců?',
         'Často ano, pokud souhlasí počet rychlostí a mechanické rozměry, ale u řazení a přehazovačky je vhodné držet jednu značku. Smíšené sestavy mohou řadit hůř. Před nákupem si vždy přečtěte popis kompatibility u produktu.'),
        ('Kdy se komponenty nejvíc zlevňují?',
         'Cyklistické díly obvykle na konci sezóny a při změně generace, rybářské před sezónou a po ní. Ceny se mění, proto porovnejte více obchodů a kontrolujte stav zboží, zda je nové a v obalu.'),
    ])

# ------------------------------------------------------------------ outerstuff
NEW['outerstuff'] = dict(
    title='Outerstuff: dětské týmové dresy, trička a čepice',
    desc='Outerstuff v katalogu sporteky: dětské dresy NHL a NBA, trička, mikiny a čepice týmů. Jak vybrat velikost, kategorii a hlídat sezónní slevy.',
    intro='<p>Outerstuff je v našem katalogu značka fanouškovského oblečení, která míří téměř výhradně na děti. Z názvů produktů vyplývá, že jde o dresy, trička, mikiny a čepice týmů z lig NHL a NBA, například s motivy Florida Panthers, Colorado Avalanche, Brooklyn Nets nebo Los Angeles Lakers. '
          'Nejvíc zboží spadá do <a href="/sportovni-tricka/">triček a tílek</a>, potom do kategorie <a href="/cepice-a-celenky/">čepic a kšiltovek</a>, <a href="/mikiny/">mikin</a> a <a href="/dresy/">dresů</a>. Pro dospělé je v nabídce jen malý zlomek, hlavně pánská trička s hráčskými motivy. Stránka pomáhá vybrat správnou velikost, odlišit módní dres od hráčského a najít týmový kousek, který dítě rádo ponese. Porovnáte obchody a zjistíte, kdy se vyplatí čekat na slevu.</p>',
    guide='<h2>Co je v nabídce Outerstuff</h2>'
          '<p>Značka v katalogu patří do světa licenčních fanouškovských produktů. Oblečení nese jména a loga týmů, někdy i jména hráčů, a vyrábí se pro mladé fanoušky. Mezi zbožím převažují dětské velikosti; menší skupinu tvoří pánské kousky a drobnější doplňky pro batolata, například zimní čepice. Barvy ladí s týmy, proto výrazně vystupují černá, zlatá, červená a modrá, doplněné vícebarevnými potisky.</p>'
          + T(['Kategorie', 'Co v ní čekat', 'Komu se hodí'], [
              ['Trička a tílka', 'bavlněná trička s týmovým logem, někdy s číslem hráče', 'dětem na každodenní nošení i do školy'],
              ['Čepice a kšiltovky', 'zimní čepice s bambulí, kšiltovky, čelenky', 'batolatům a dětem na zimu a venkovní zápasy'],
              ['Mikiny a fleece', 'mikiny s kapucí, fleecové mikiny s logem', 'dětem pro chladnější dny'],
              ['Dresy', 'hokejové a basketbalové fashion dresy', 'fanouškům na zápas nebo do dětského pokoje'],
              ['Tepláky a kraťasy', 'volnočasové kalhoty s týmovým prvkem', 'dětem na sport a doma']]) +
          '<h2>Pro koho je značka určena</h2>'
          '<p>Filtr katalogu ukazuje, že skoro všechno zboží je dětské. Pánských kousků je řádově méně, a hlavně jde o trička s hráčskými motivy a mikiny. Pokud tedy hledáte dospělý dres pro sebe, zkuste nejdřív <a href="/znacka/fanatics/">Fanatics</a>, <a href="/znacka/new-era/">New Era</a> nebo <a href="/znacka/mitchell-ness/">Mitchell and Ness</a>, a u dětí vyzkoušejte tuto značku. Rodiče malých fanoušků ocení, že motivů je dost a že si dítě může vybrat tým, který sleduje. Pro dospívající bývá výhodnější větší velikost, protože dětská velikostní řada má omezený rozsah.</p>'
          '<h2>Dres nebo tričko: čím se liší</h2>'
          '<p>V názvech se opakuje spojení fashion jersey. Je to módní verze dresu, tedy volnější střih ze syntetické látky, s vyšitými nebo potištěnými znaky. Na rozdíl od hráčského dresu není určen k tvrdému sportovnímu zápasu, ale k nošení z lásky k týmu. Dres se obléká přes tričko, hodí se na zápas, do školy v den s týmovou barvou nebo jako dárek. Tričko je lehčí, levnější na údržbu a lépe snáší opakované praní.</p>'
          '<p>Pro dítě, které hraje samo, je lepší koupit ve sportovním obchodě skutečný funkční dres. Fashion dres je pohodlný, ale při intenzivním pohybu se v něm dítě zpotí a látka nemusí odvádět vlhkost tak dobře. Hledáte-li pohodlné kousky na běžný pohyb, podívejte se do kategorie <a href="/detske-sportovni-obleceni/">dětské sportovní oblečení</a> a do přehledu <a href="/detske-dresy/">dětské dresy</a>.</p>'
          '<h2>Jak vybrat velikost dětského oblečení</h2>'
          '<p>Dětské velikosti se označují u různých výrobců různě: někdy slovy jako S a M, jindy číslem odpovídajícím věku nebo výšce. Spoléhat na věk je zrádné, protože děti stejného věku se výrazně liší výškou i postavou. Změřte tedy dítě od ramene po kotník, obvod hrudi a pasu a výsledek porovnejte s tabulkou u produktu. Pokud tabulka chybí, zeptejte se prodejce nebo zvolte raději o stupeň větší.</p>'
          '<ul><li><strong>Dres s volným střihem:</strong> bere se přes tričko, takže počítejte s rezervou v prsou a v délce.</li>'
          '<li><strong>Mikiny a fleece:</strong> dítě v nich roste, rukávy lze ohrnout, ale zbytečně dlouhé překážejí.</li>'
          '<li><strong>Zimní čepice pro batolata:</strong> musí zakrývat uši a zároveň nesmí škrtit pod bradou.</li>'
          '<li><strong>Trička:</strong> po praní se bavlna může lehce srazit, proto je lepší volit o něco volnější kus.</li></ul>'
          '<h2>Týmy, sezóny a motivy</h2>'
          '<p>V nabídce se objevují kluby severoamerických lig. Hokejové motivy patří týmům z NHL, například Seattle Kraken, Washington Capitals, Florida Panthers a Colorado Avalanche. Basketbalové pak týmům z NBA, mezi nimi Brooklyn Nets, Chicago Bulls a Los Angeles Lakers. Při výběru nehledejte jen jméno týmu, ale i odstín: stejné barvy mají různé týmy a odlišuje je až znak. Hráčské motivy se mění s přestupy, proto jsou starší kousky obvykle sběratelsky zajímavé a nabídka se obměňuje.</p>'
          '<p>Chcete-li doplnit dětský outfit, hodí se k dresu tepláky z kategorie <a href="/teplaky/">tepláky</a> nebo kraťasy z oddílu <a href="/sportovni-kratasy/">kraťasy</a>. Pro chladné dny doplňuje celek <a href="/nakrcniky-a-satky/">nákrčník</a> a fleecová mikina z oddílu <a href="/fleecove-mikiny/">fleecové mikiny</a>. Větrovky z oddílu <a href="/vetrovky/">větrovky</a> sedí v přechodném počasí. Sportovnější styl nabízí také <a href="/znacka/nike/">Nike</a> a <a href="/znacka/adidas/">Adidas</a>.</p>'
          '<h2>Materiály a péče</h2>'
          '<p>Trička bývají z bavlny či směsi s polyesterem, dresy z lehké syntetiky s potiskem nebo našitými znaky. Pro dlouhou životnost perte kousky naruby při nižší teplotě a nepoužívejte aviváž, která zhoršuje odvod vlhkosti. Potištěné části nežehlete přímo, ať se motiv nepokazí. Dres po prvním nošení nikdy nesušte na topení; zdeformuje se a lesklé části mohou praskat. Mikiny a fleece pere se zapnutým zipem, aby nepoškodil ostatní prádlo. Čepice nejlépe vyperte ručně a nechte vyschnout rozložené.</p>'
          '<h2>Jak sladit celý dětský outfit</h2>'
          '<p>Týmové kousky se dobře kombinují, pokud vyberete jednu dominantní věc a zbytek nechte jednoduchý. Výrazný dres nebo tričko s velkým logem doplňte neutrálními kalhotami a výrazný potisk nechte jen na jednom kusu. Dítě tak nevypadá přeplněně a týmová barva vynikne. Pro sourozence, kteří fandí stejnému týmu, se vyplatí kombinovat shodné motivy v různých velikostech, na zápas nebo na společné foto.</p>'
          '<p>Při každodenním nošení uvažujte o vrstvách. V zimě se pod mikinu hodí tenké tričko s dlouhým rukávem, v přechodném období stačí tričko s mikinou na zip, kterou dítě podle potřeby sundá. Pokud má dítě rádo zápasy venku, nezapomeňte na čepici a rukavice, které se dají pořídit v oddílech s doplňky. K dispozici jsou i drobnější kousky, například nákrčníky a kukly, které zakryjí krk i bradu při chladném větru.</p>'
          '<h2>Co dělat, když se dítě rychle vyrůstá</h2>'
          '<p>Dětské oblečení se nosí krátce, proto se nevyplatí kupovat nejdražší kousek, který bude sedět jednu sezónu. Zvolte střih, který se dá nosit s rezervou, a pořiďte raději jednodušší motiv, který dítě opravdu miluje. Zachovalé dresy a mikiny se dají předat mladšímu sourozenci, vyprat a nosit znovu. Při skladování je uložte čisté a suché, mimo přímé slunce, které vyblednou potisky. Pokud dítě fanouškovský styl brzy omrzí, pomohou základní trička jednoduchého střihu z kategorie triček, která snesou kombinaci s čímkoli.</p>'
          '<h2>Na co si dát pozor při nákupu</h2>'
          '<ul><li><strong>Motiv a tým:</strong> ověřte přesný název týmu, protože některé názvy se liší jen městem.</li>'
          '<li><strong>Jméno hráče:</strong> motivy s konkrétním hráčem stárnou, jakmile hráč změní klub.</li>'
          '<li><strong>Velikost:</strong> zkontrolujte tabulku u produktu, nikoli jen věkové označení.</li>'
          '<li><strong>Stav zboží:</strong> u starších motivů se vyplatí ověřit, že jde o nový kus v původním balení.</li>'
          '<li><strong>Doprava:</strong> menší položky se z různých obchodů sčítají, proto porovnávejte celkovou částku s dopravou.</li></ul>'
          '<h2>Jak hledat slevy a dárek</h2>'
          '<p>Týmové oblečení se prodává celoročně, ale nejvíc se nakupuje před Vánoci a na začátku sezóny. Slevy často přicházejí po skončení sezóny, kdy se vyprodávají starší motivy. Dětské velikosti jsou rychle rozebrané, proto sledujte skladovost jednotlivých rozměrů a nevolte jen podle barvy. Při nákupu dárku zvolte tým, který dítě opravdu sleduje, a raději o číslo větší velikost, aby kousek vydržel více sezón. Výhodnou cenu najdete porovnáním obchodů, ale vždy přihlédněte k dopravě a času dodání.</p>',
    faq=[
        ('Co je Outerstuff?',
         'V katalogu sporteky jde o značku licenčního fanouškovského oblečení pro děti. Z produktů vyplývá, že nese znaky týmů NHL a NBA. Nabízí trička, mikiny, dresy a čepice s týmovými motivy.'),
        ('Je oblečení určeno dětem, nebo i dospělým?',
         'Většina zboží je dětská. Pánských kousků je jen malá část, hlavně trička s hráčskými motivy a mikiny. Dospělý fanoušek najde širší výběr u jiných značek se stejným zaměřením.'),
        ('Jaký je rozdíl mezi fashion dresem a hráčským dresem?',
         'Fashion dres je volnější módní verze s motivem týmu, vhodná na nošení a na zápas z lavice fanoušků. Hráčský dres je určen pro sport a je střižen i vyroben odlišně. Fashion verze je pohodlnější, ale méně odvádí pot.'),
        ('Jak zvolit velikost pro dítě?',
         'Podle výšky a obvodu hrudi, nikoli podle věku. Změřte dítě a porovnejte rozměry s tabulkou u produktu. Při váhání zvolte větší velikost, protože dítě roste a dres se nosí přes tričko.'),
        ('Dá se dres prát v pračce?',
         'Ano, nejlépe naruby na nízkou teplotu a bez aviváže. Nesušte jej na topení ani v sušičce, jinak se potisk a lesklé části zdeformují. Přesný návod najdete na pečovacím štítku.'),
        ('Které týmy značka v nabídce zastupuje?',
         'V ukázkách se objevují například Florida Panthers, Colorado Avalanche, Seattle Kraken, Washington Capitals, Brooklyn Nets, Chicago Bulls a Los Angeles Lakers. Nabídka se obměňuje, proto se vyplatí kontrolovat aktuální stav.'),
        ('Hodí se zimní čepice pro batolata k venkovní zimě?',
         'Zimní čepice s lemem a bambulí jsou určeny pro chladné dny a kryjí uši. Důležité je, aby nesvíraly pod bradou a aby se daly snadno nasadit. Pro velmi mrazivé dny doplňte nákrčník nebo šálu.'),
        ('Kdy bývají slevy na týmové oblečení?',
         'Nejčastěji po skončení sezóny a při vyprodávání starších motivů. Před Vánoci se naopak nakupuje nejvíc a sleva bývá menší. Porovnejte obchody a nezapomeňte na dopravu.'),
        ('Dají se kousky předat mladšímu sourozenci?',
         'Ano, pokud je oblečení čisté, správně vyprané a skladované mimo přímé slunce, které vybledne potisky. Dres a mikina vydrží několik sezón. U triček kontrolujte, zda se po praní neporušil potisk.'),
        ('Jak vybrat dárek pro malého fanouška?',
         'Zjistěte, který tým dítě sleduje, a zvolte kousek, který lze nosit denně, například mikinu nebo tričko. Dres je výrazný dárek, ale volte raději o číslo větší velikost, aby vydržel víc sezón a dítě jej mohlo nosit přes tričko.'),
    ])

# ------------------------------------------------------------------ northfinder
NEW['northfinder'] = dict(
    title='Northfinder: outdoorové bundy, kalhoty a vesty',
    desc='Northfinder v katalogu sporteky: pánské a dámské bundy, softshell, lyžařské kalhoty, vesty a trička. Jak vybrat vrstvu, střih a zateplení na sezónu.',
    intro='<p>Northfinder je v našem katalogu oděvní značka zaměřená na outdoor, volný čas a zimní sporty. Největší část nabídky tvoří bundy do přechodného počasí, následují sportovní kalhoty, trička, kraťasy a outdoorové kalhoty. Mezi dalšími kategoriemi najdete skialpinismus, vesty, lyžařské kalhoty a bundy a fleecové mikiny. '
          'Zboží je rozděleno skoro rovným dílem na pánské a dámské a názvy modelů mají podobu jmen, například Antoni, Svarog nebo Abigale. Tato stránka vysvětluje, jak vybrat správnou vrstvu, kdy se hodí softshell a kdy zateplená bunda, a jak poznat, že model vydrží vaše aktivity. Porovnáte obchody, velikosti a barevná provedení a naučíte se číst popisy, které se u outdoorového oblečení často opakují.</p>',
    guide='<h2>Co Northfinder v katalogu nabízí</h2>'
          '<p>Značka pokrývá celou škálu oděvů pro pohyb venku. Největší oddíl, <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, je doplněn kalhotami, tričkem a vestou. Na zimu přibývají lyžařské a snowboardové kousky a v menší míře i oblečení pro skialpinismus. Barevně převažuje černá, za ní následují modrá, zelená, červená a růžová. To odpovídá potřebám: černá a tmavé barvy jsou praktické, jasné odstíny zlepšují viditelnost v terénu.</p>'
          + T(['Kategorie', 'Typické použití', 'Na co se zaměřit'], [
              ['Jarní a podzimní bundy', 'město, výlety, přechodné období', 'zateplení, větruodolnost, kapuce'],
              ['Sportovní kalhoty', 'sport, volný čas, cestování', 'pružnost materiálu, střih'],
              ['Outdoorové kalhoty', 'turistika, kemping, trek', 'odolnost, kapsy, odepínací nohavice'],
              ['Lyžařské kalhoty a bundy', 'sjezdovka, snowboard, zimní výlety', 'zateplení, sněhová manžeta, membrána'],
              ['Vesty', 'doplňková vrstva, která nechá ruce volné', 'prošití, teplo bez rukávů'],
              ['Skialpinismus', 'výstup i sjezd mimo sjezdovku', 'prodyšnost, lehkost, větrání']]) +
          '<h2>Pánské, dámské a unisex střihy</h2>'
          '<p>Podle filtru v katalogu je nabídka rozdělena téměř rovnoměrně na pánské a dámské modely, unisex kousky jsou ojedinělé. Dámský střih je obvykle užší v pase a delší v bocích, pánský širší v ramenou. Pokud budete bundu navlékat přes svetr nebo fleece, zvolte o číslo větší nebo model s uvolněnějším střihem. Pro aktivní sporty naopak dávejte přednost přiléhavější verzi, aby neflikala a nezachytávala vzduch. Velikost ověřte podle tabulky u každého produktu a nespoléhejte na to, že označení M znamená totéž u všech značek.</p>'
          '<h2>Softshell, zateplená bunda a parka: kdy co</h2>'
          '<p>Vzorek zboží ukazuje několik typů. Softshellová bunda je pružná, větruodolná a mírně odpuzuje vodu; je ideální pro aktivní chůzi a jarní či podzimní počasí. Zateplená bunda, často se zateplenou výplní, hřeje i při nízké teplotě, ale hůř odvádí pot při námaze. Parka je delší bunda do města a pro chladné dny, často s kapucí a se zapínáním na zip i na patenty.</p>'
          '<ul><li><strong>Softshell:</strong> pro chůzi, turistiku a mírné počasí, vždy s vrstvou pod ním při chladu.</li>'
          '<li><strong>Zateplená bunda:</strong> do zimy a pro statické činnosti, například při procházce či čekání.</li>'
          '<li><strong>Parka:</strong> městské nošení za chladu, delší střih chrání bedra.</li>'
          '<li><strong>Lyžařská bunda:</strong> membrána a zateplení, sněhová zástěra, odvětrávací zipy.</li>'
          '<li><strong>Vesta:</strong> doplňuje vrstvu, aby ruce zůstaly volné.</li></ul>'
          '<p>Chcete-li začít od základu, porovnejte přehled <a href="/softshellova-bunda-panska/">pánských softshellových bund</a> a <a href="/jarni-a-podzimni-bundy-damske/">dámských jarních a podzimních bund</a>. Zimní nabídku najdete v kategorii <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>, k tomu patří <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>'
          '<h2>Vrstvení: základ pohodlí venku</h2>'
          '<p>Třívrstvé oblékání funguje spolehlivě bez ohledu na značku. První vrstva odvádí pot od těla, druhá izoluje, třetí chrání před větrem a deštěm. Správně zvolená bunda je tou třetí, případně druhou vrstvou, která se kombinuje s funkčním tričkem nebo <a href="/fleecove-mikiny/">fleecovou mikinou</a>. K aktivnímu pohybu se hodí tenčí kus, zatímco při statických činnostech uvítáte víc izolace. Sundejte nebo rozepněte vrstvu dřív, než se zpotíte; mokré oblečení pak chladí.</p>'
          '<p>Vestu používejte, když potřebujete zahřát trup, ale rukávy by vadily. <a href="/sportovni-vesty/">Sportovní vesty</a> se nosí přes mikinu, tričko i pod bundu. Dámské vesty jsou často prošité, pánské bývají sportovnější. Podrobnější porady k oběma pohlavím najdete u přehledů <a href="/damske-vesty/">dámské vesty</a> a <a href="/panske-vesty/">pánské vesty</a>.</p>'
          '<h2>Kalhoty: outdoor, sport a zima</h2>'
          '<p>V <a href="/outdoorove-kalhoty/">outdoorových kalhotách</a> hledejte pružný materiál, zesílená kolena a kapsy se zipem. Kargo střih, který se objevuje u pánských kousků, nabízí víc úložného prostoru. <a href="/sportovni-kalhoty/">Sportovní kalhoty</a> jsou lehčí a pohodlnější, vhodné pro město a lehkou aktivitu. Zimní lyžařské kalhoty pak mají zateplení a zpevněný spodní lem, který se snese s hranami lyží. Podrobnější průvodce pro muže je ve výběru <a href="/panske-outdoorove-kalhoty/">pánské outdoorové kalhoty</a>.</p>'
          '<p>Při výběru velikosti zvažte, jaké vrstvy budete pod kalhotami nosit. Na lyžování se pod ně obléká termoprádlo, takže kalhoty nesmí být těsné. Pasy často nabízejí nastavení, ale délka nohavice rozhoduje: příliš dlouhá se rozedře, příliš krátká nechá odhalený kotník. Na zimní výlety zvažte i sněhové manžety a chránič nohavice proti kamenům.</p>'
          '<h2>Trekové boty a doplňky</h2>'
          '<p>Ke kolekci patří i <a href="/trekova-obuv/">trekové boty</a>. Při výběru počítejte s ponožkami, které budete nosit, a vyzkoušejte je odpoledne, kdy má noha největší objem. Pevná podrážka a ochrana špičky vydrží náročný terén, nízký střih zase lépe vyhovuje městu a lehčím trasám. Chcete-li srovnat s jinými značkami, mrkněte na <a href="/znacka/kilpi/">Kilpi</a>, <a href="/znacka/hannah/">Hannah</a> a <a href="/znacka/alpine-pro/">Alpine Pro</a>; podobné přehledy najdete také v přehledech <a href="/kilpi-lyzarska-bunda/">Kilpi lyžařské bundy</a> a <a href="/hannah-lyzarske-kalhoty/">Hannah lyžařské kalhoty</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Sportovní oděvy perte podle štítku, obvykle na šetrný program a bez aviváže, která zalepuje póry membrány a snižuje prodyšnost. Zapněte všechny zipy a suchý zip, aby neničily látku. Zateplenou výplň nežmoulejte při sušení, vysušte ji rozloženou. Po několika sezónách zvažte obnovu impregnace, aby voda opět stékala po povrchu. Skvrny řešte ihned a bundu skladujte zavěšenou, ne přimáčknutou ve skříni.</p>'
          '<h2>Jak číst názvy modelů a popisy</h2>'
          '<p>Modely mají jména, například Antoni, Svarog nebo Abigale, a často je zpestřují barevná označení. Jména samotná nic neříkají o vlastnostech, proto si přečtěte popis: u bund hledejte slova jako softshell, zateplená, lyžařská nebo parka, u kalhot kargo, outdoorové a trekingové. Odnímatelná kapuce je užitečná při proměnlivém počasí, protože kapuci v teplém počasí nepotřebujete. Prošívání vypovídá o výplni, zatímco pružný úplet o schopnosti sledovat pohyb.</p>'
          '<p>Několik modelů se v nabídce opakuje ve více barvách. Proto se vyplatí porovnat stejný model u více obchodů a hlídat, zda barva nese stejné označení. Stejný střih mívá jinou skladovost podle odstínu a černá se rozebírá první. Chcete-li kousek na dlouhé nošení, zvolte klidnou barvu, kterou snadno kombinujete s jiným oblečením.</p>'
          '<h2>Skialpinismus a pohyb v zimě</h2>'
          '<p>Kategorie <a href="/skialpinismus/">skialpinismu</a> je v nabídce menší, ale má své zvláštnosti. Při výstupu se tělo zahřívá, proto je důležitá prodyšnost a možnost větrání zipy v podpaží nebo na stehnech. Při sjezdu naopak chcete větrovku, která zadrží teplo. Oblečení se vrství a při přechodu z výstupu do sjezdu se přidává bunda. Lehké kousky se dají složit do batohu a vytáhnout, až když se ochladí.</p>'
          '<p>Pro běžné lyžování na sjezdovce stačí klasická lyžařská bunda a kalhoty, které se snadno čistí a zadrží sníh. Dávejte pozor na kapsy: skipas patří do zipové kapsy na rukávu, telefon do vnitřní. Nezapomeňte na ochranu před větrem v krku; vyšší límec nebo nákrčník ušetří od prochladnutí.</p>'
          '<h2>Na co se zaměřit při nákupu</h2>'
          '<ul><li><strong>Kapuce:</strong> pevná se hodí pro zimu, odnímatelná pro proměnlivé počasí.</li>'
          '<li><strong>Zipy:</strong> kvalitní vodotěsné nebo překryté zipy omezují pronikání vody.</li>'
          '<li><strong>Manžety:</strong> nastavitelné rukávy a lem drží teplo a brání větru.</li>'
          '<li><strong>Kapsy:</strong> zip a vnitřní kapsa na telefon nebo peněženku jsou praktickou drobností.</li>'
          '<li><strong>Střih:</strong> delší záda chrání bedra při předklonu nebo při sezení na kole.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní bundy a lyžařské kalhoty se zlevňují po konci sezóny, tedy na jaře, a před novou sezónou. Jarní a podzimní kousky bývají levnější na konci léta i v zimě. Protože modely nesou jména a každý má několik barev, porovnávejte podle jména a barevné varianty. Sledujte také skladové velikosti: nejčastěji se rychle vyprodají střední rozměry. Při zvažování koupě pro dospělého nezapomeňte na možnost vrácení do lhůty a kontrolu popisu zateplení.</p>',
    faq=[
        ('Co Northfinder nabízí?',
         'Především outdoorové a sportovní oblečení: jarní a podzimní bundy, kalhoty, trička, kraťasy, vesty a fleecové mikiny. V zimní nabídce jsou lyžařské a snowboardové bundy a kalhoty, v menším množství skialpinismus a trekové boty.'),
        ('Je oblečení pro muže, nebo pro ženy?',
         'Pro obě skupiny, v katalogu je poměr téměř vyrovnaný. Dámské střihy jsou užší v pase, pánské širší v ramenou. Unisex kousky jsou jen výjimečné, proto vybírejte podle tabulky velikostí.'),
        ('Kdy zvolit softshell a kdy zateplenou bundu?',
         'Softshell se hodí na aktivní pohyb v mírném počasí, protože je pružný a prodyšný. Zateplená bunda je pro chladné dny a pro stání či pomalou chůzi. Při velké námaze se v zateplené bundě snadno zpotíte.'),
        ('Jak velkou velikost vybrat?',
         'Podle tabulky u produktu a podle toho, co chcete pod bundou nosit. Pro vrstvení vezměte volnější střih, na aktivní sport přiléhavější. Pokud váháte mezi dvěma velikostmi, zvolte tu, v níž se nic nepíná v ramenou.'),
        ('Hodí se lyžařské kalhoty i na běžný zimní výlet?',
         'Ano, pokud dávají zateplení a odolávají vlhkosti. Pro pěší výlety jsou ale někdy teplé, a proto zvažte spíš outdoorové kalhoty a pod ně termoprádlo. Záleží na teplotě a na tom, jak moc se budete hýbat.'),
        ('Jak bundu správně prát?',
         'Podle štítku, šetrně a bez aviváže, se zapnutými zipy. Aviváž zalepuje póry a snižuje prodyšnost. Zateplené kousky sušte rozložené, aby se výplň nesesedla. Po několika sezónách obnovte impregnaci.'),
        ('Co znamená vesta jako samostatná vrstva?',
         'Zahřeje trup, ale nechá volné ruce. Hodí se na procházky, běh či turistiku v chladnějším počasí. Pod vestu oblékněte tričko nebo mikinu a pro větší zimu ji kombinujte s bundou.'),
        ('Kdy bývají slevy na outdoorové oblečení?',
         'Zimní kousky na konci sezóny, tedy na jaře, přechodné bundy na konci léta a v zimě. Sledujte konkrétní model a barvu, protože se obchody liší. Porovnejte také dopravu a lhůtu pro vrácení.'),
        ('Jak poznám, že je bunda opravdu vhodná do zimy?',
         'Přečtěte si popis zateplení, přítomnost kapuce, manžet a sněhové zástěry u lyžařských modelů. Zimní bunda musí zadržet teplo i vítr. Pro klidnější pohyb volte silnější výplň, pro aktivní sport raději tenčí vrstvy kombinované s fleecem.'),
        ('Který kus je nejuniverzálnější pro začátek?',
         'Pro většinu lidí je to softshellová bunda černé nebo tmavé barvy, doplněná fleecovou mikinou a funkčním tričkem. Takové vrstvy pokryjí jaro, podzim i mírnou zimu a snadno se kombinují s dalšími kousky.'),
    ])

# ------------------------------------------------------------------ calvin-klein
NEW['calvin-klein'] = dict(
    title='Calvin Klein: sportovní oblečení, tenisky a plavky',
    desc='Calvin Klein ve sporteka: mikiny, trička, tenisky, plavky, ponožky, batohy a sportovní podprsenky. Jak vybrat střih, velikost a líbivou kombinaci.',
    intro='<p>Calvin Klein je v našem katalogu módní značka, která se u nás potkává se sportem. Z nabídky vyplývá, že hlavní kategorie jsou mikiny a trička, hned za nimi tenisky a volnočasová obuv, plavky, košile a čepice. Dále najdete sportovní kalhoty, ponožky, městské batohy, tašky přes rameno, tepláky a nákrčníky. '
          'Pánských produktů je trochu víc než dámských, dětských kousků je jen pár. Barevně převažuje černá, za ní bílá, modrá, šedá a béžová, tedy klidné barvy pro každodenní nošení. Tato stránka pomáhá vybrat, co z velké šíře nabídky vám sedne: kdy zvolit sportovní řadu, jak poznat správnou velikost, jak pečovat o bavlnu a plavky a kdy sledovat slevy.</p>',
    guide='<h2>Co značka v katalogu nabízí</h2>'
          '<p>Nabídka kombinuje městský styl se sportovními prvky. Největší jsou <a href="/mikiny/">mikiny</a>, <a href="/sportovni-tricka/">trička a tílka</a> a <a href="/tenisky/">tenisky a volnočasové boty</a>. Dále <a href="/plavky/">plavky</a>, <a href="/kosile/">košile</a>, <a href="/cepice-a-celenky/">čepice</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>. Doplňky zastupují <a href="/sportovni-ponozky/">ponožky</a>, <a href="/mestske-batohy/">městské batohy</a> a <a href="/tasky-pres-rameno/">tašky přes rameno</a>. Z názvů modelů poznáte řady označené zkratkami, například WO a PW, které se u oblečení opakují a odlišují sportovní a volnočasovou řadu.</p>'
          + T(['Oblast', 'Co v ní čekat', 'Kdy se hodí'], [
              ['Mikiny a tepláky', 'mikiny s kapucí i na zip, joggery, tepláky', 'doma, v kavárně, na lehký sport'],
              ['Trička a polo', 'bavlněná trička, polokošile', 'celoročně, do práce i na volno'],
              ['Tenisky a pantofle', 'nízké kožené a textilní boty, pantofle', 'město, cestování, dovolená'],
              ['Plavky a ponožky', 'koupací šortky, dámské plavky, sportovní ponožky', 'dovolená, bazén, každodenní nošení'],
              ['Fitness', 'legíny, sportovní podprsenky, krátké kalhoty', 'cvičení, běh, jóga'],
              ['Doplňky', 'batohy, tašky, čepice', 'doplnění outfitu']]) +
          '<h2>Pro koho je značka určena</h2>'
          '<p>Filtr katalogu ukazuje převahu pánských modelů, hned za nimi dámské, unisex kousky a jen několik dětských. Pánské střihy bývají volnější v těle, dámské přiléhavější, zejména legíny a sportovní podprsenky. Pro dospívající a dospělé s menší postavou stojí za zvážení i unisex nabídka. Při nákupu pro ženy zvažte, zda hledáte volnočasovou módní verzi, nebo opravdu sportovní oblečení, a podle toho vybírejte řadu a materiál.</p>'
          '<h2>Sportovní podprsenky, legíny a plavky</h2>'
          '<p>U sportovních podprsenek rozhoduje úroveň podpory: nízká na jógu a lehkou chůzi, střední na rychlejší trénink a vysoká na běh a skákání. Označení v názvech, například high nebo med, naznačuje právě tuto úroveň. Podprsenka musí přiléhat pod prsy, ramínka nesmí řezat a prádlo se nesmí posouvat při pohybu. Vyzkoušejte si několik skoků a předklonů. Samostatný přehled najdete u <a href="/sportovni-podprsenka-calvin-klein/">sportovních podprsenek Calvin Klein</a>.</p>'
          '<p>Legíny s vysokým pasem drží lépe a nepadají při dřepech; zvolte tak tlustou látku, aby při předklonu neprosvítala. Plavky se hodí spíše na dovolenou než na pravidelné plavání, kde mívají lepší trvanlivost speciální sportovní plavky. Přehled pro ženy je v <a href="/damske-plavky-calvin-klein/">dámských plavkách Calvin Klein</a> a obecný přehled v <a href="/calvin-klein-plavky/">plavkách Calvin Klein</a>. Pánské koupací šortky rychle schnou, ale s oblíbenými kousky zacházejte šetrně.</p>'
          '<h2>Mikiny, tepláky a trička</h2>'
          '<p>Mikina je základ volnočasového šatníku. Rozhoduje materiál: hladký bavlněný úplet s mírnou příměsí syntetiky drží tvar a méně se mačká. Mikiny na zip se lépe vrství a v interiéru je snadno sundáte, mikina bez zipu působí upraveněji. Tepláky, často označované jako jogger, mají u kotníku manžetu, což dává kalhotám sportovní vzhled. <a href="/teplaky/">Tepláky</a> doplňují mikinu do kompletního outfitu.</p>'
          '<p>U triček zvažte, zda chcete čistý jednobarevný střih, nebo velké logo. Polokošile je vhodná do kanceláře s uvolněným dress codem a do města. Bavlněné modely jsou prodyšné, ale po praní se mohou srazit, proto volte raději větší velikost než minimální. Nebojte se kombinovat s jinými značkami, například <a href="/znacka/tommy-hilfiger/">Tommy Hilfiger</a>, <a href="/znacka/fila/">Fila</a> nebo <a href="/znacka/puma/">Puma</a>.</p>'
          '<h2>Tenisky a volnočasová obuv</h2>'
          '<p>Nízké tenisky s koženým svrškem jsou univerzální a hodí se k džínám i k lehkým kalhotám. Najdete také pantofle, které se nosí doma nebo na pláž. Velikosti se označují v evropských číslech; při nákupu vybírejte podle délky chodidla v centimetrech. Kožené boty se po delším nošení přizpůsobí, ale syntetické zůstanou tvarově stálejší. Pro náročné sportování nejsou určeny, tam sáhněte po kategorii sportovní obuvi, například <a href="/znacka/nike/">Nike</a> nebo <a href="/znacka/adidas/">Adidas</a>.</p>'
          '<p>Při chůzi po městě se hodí tlumená podrážka a lehký materiál. Bílá obuv se rychle špiní, černá odpustí víc. Kožené tenisky pravidelně čistěte vlhkým hadříkem a před deštěm je případně naimpregnujte. Dobré větrání a sušení po nošení prodlužuje životnost bot.</p>'
          '<h2>Batohy, tašky a čepice</h2>'
          '<p>Městský batoh poslouží na cesty do školy nebo do práce a tašky přes rameno či dokladovky na doklady, telefon a klíče. U batohu se podívejte na polstrovanou kapsu na notebook a na to, zda jsou popruhy dostatečně široké. Taška přes rameno se nosí napříč a nechává volné ruce, ale při těžší zátěži zatěžuje jedno rameno. Čepice a kšiltovky doplní outfit a chrání před sluncem. Velikost nastavte zadním pásem.</p>'
          '<h2>Péče, životnost a falešné kousky</h2>'
          '<p>Oblečení perte podle štítku, obvykle při nižší teplotě, a potištěné logo nežehlete přímo. Mikiny perte naruby, aby se omezilo žmolkování, a nesušte je na topení. Plavky po každém použití vypláchněte od chlóru a soli, nechte uschnout ve stínu a nesušte v sušičce, aby neztratily pružnost. Protože jde o oblíbenou značku, na internetu se objevují padělky. Kupujte u prodejců s jasným původem, kontrolujte kvalitu šití a kód produktu v názvu a porovnávejte informace v několika obchodech.</p>'
          '<h2>Jak kombinovat oblečení do každodenního šatníku</h2>'
          '<p>Značka patří spíš k minimalistickým volnočasovým kouskům, a tak se snadno kombinuje. Základní sestava na každý den: tričko jednoduchého střihu, mikina na zip a tepláky nebo džíny, k tomu nízké tenisky. Pokud preferujete upravenější vzhled, nahraďte mikinu polokošilí a tepláky rovnými kalhotami. Barvy volte neutrální, kdy černá, bílá a šedá spolu fungují bez rizika, a béžová nebo modrá dodá změnu.</p>'
          '<p>Pro cvičení platí jiná pravidla. Legíny a sportovní podprsenka musejí snést pohyb, zatímco mikina na zip se hodí na cestu do posilovny a z ní. Chcete-li zvýšit komfort, vyberte tričko z lehčího materiálu a k tomu měkké ponožky, které netlačí. Ponožky jsou drobnost, na kterou se zapomíná, ale právě ony rozhodují o tom, zda si botu oblíbíte.</p>'
          '<h2>Značkové oblečení a sport: jaká je realita</h2>'
          '<p>U módních značek je dobré rozlišovat, co je určeno pro sport a co pro volný čas. Oblečení označené jako sportovní, například legíny nebo podprsenky, má zpravidla pružný materiál a střih na pohyb. Mikiny a trička z bavlny se spíš nosí při volnočasových aktivitách a hůř odvádějí pot. Pro nejnáročnější tréninky tedy porovnejte i specializované značky, například <a href="/znacka/under-armour/">Under Armour</a>, a podle potřeby složte outfit z více zdrojů.</p>'
          '<h2>Na co se zaměřit při nákupu</h2>'
          '<ul><li><strong>Kód v názvu:</strong> u mnoha modelů je v názvu kód a velikost, takže snadno najdete stejný kus u jiného obchodu.</li>'
          '<li><strong>Velikostní tabulka:</strong> střihy se liší podle řady, proto ji vždy porovnejte.</li>'
          '<li><strong>Materiál:</strong> bavlna pro pohodlí, elastan pro pružnost, polyester pro rychlé schnutí.</li>'
          '<li><strong>Barva:</strong> světlé kousky snadno špiní, tmavé odpouštějí.</li>'
          '<li><strong>Vrácení:</strong> u obuvi a plavek zkontrolujte podmínky vrácení.</li></ul>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Módní zboží se zlevňuje při střídání sezón: letní plavky a trička na konci léta, mikiny a tepláky na jaře. Pomáhá srovnat identický kód u více obchodů, protože každý uvádí zboží s jinou barvou a velikostí. V nabídce se objevují i kousky s kódem a velikostí přímo v názvu, takže skladovost ověříte snadno. Sledujte také velikostní tabulku; značka může mít střih menší nebo větší, než jste zvyklí. A pokud kupujete dárek, zvolte pružné velikosti nebo si ověřte možnost výměny.</p>',
    faq=[
        ('Co Calvin Klein v katalogu sporteky nabízí?',
         'Hlavně mikiny, trička, tenisky, plavky, košile a čepice, dále sportovní kalhoty, ponožky, městské batohy, tašky přes rameno a tepláky. Je to volnočasová a sportovní módní nabídka pro dospělé.'),
        ('Je značka určena spíš pro muže, nebo pro ženy?',
         'V katalogu je mírná převaha pánských modelů, hned za nimi dámské. Unisex kousky jsou vzácné a dětských jen několik. Střihy se liší: pánské bývají volnější, dámské přiléhavější.'),
        ('Jak vybrat správnou sportovní podprsenku?',
         'Podle míry podpory: nízká na jógu, střední na rychlejší cvičení a vysoká na běh. Podprsenka musí přiléhat pod prsy a ramínka nesmí řezat. Vyzkoušejte předklon a několik poskoků, zda drží.'),
        ('Hodí se plavky Calvin Klein i na pravidelné plavání?',
         'Spíš na dovolenou a k vodě. Pro časté plavání v bazénu bývají trvanlivější speciální sportovní plavky. Po každém použití plavky vypláchněte a nesušte je v sušičce.'),
        ('Jak vybrat velikost bot?',
         'Podle délky chodidla v centimetrech a tabulky u produktu. Měřte odpoledne, kdy je noha největší. Pokud váháte, zkontrolujte, zda nabídka obsahuje možnost vrácení.'),
        ('Jak rozpoznat falešný kousek?',
         'Hledejte jasný původ prodejce, kód produktu v názvu a pečlivé zpracování švů a štítků. Porovnejte informace u více obchodů. Neobvykle nízká nabídka od neznámého prodejce je varování.'),
        ('Jak pečovat o mikiny a trička?',
         'Perte naruby na nižší teplotu, nepoužívejte aviváž a nesušte na topení. Potištěné logo nežehlete přímo. Bavlna se může lehce srazit, proto volte raději větší velikost.'),
        ('Kdy bývají slevy na módní sportovní zboží?',
         'Při střídání sezón: plavky a trička na konci léta, mikiny a tepláky na jaře. Porovnejte kód produktu u více obchodů a nezapomeňte na dopravu a lhůtu pro vrácení.'),
        ('Jak sladit mikinu s tepláky a teniskami?',
         'Zvolte jednu výraznější věc a ostatní držte v neutrálních barvách, například černé, bílé nebo šedé. Mikinu na zip doplňte jednoduchým tričkem pod ní a tenisky vyberte nízké, aby celek vypadal čistě. Pro upravenější styl nahraďte tepláky rovnými kalhotami.'),
        ('Hodí se bavlněná trička také na sport?',
         'Pro volný čas ano, pro intenzivní trénink méně. Bavlna odvádí pot hůř než syntetika a po zmoknutí dlouho schne. Na cvičení volte legíny, podprsenky nebo trička z elastického materiálu a bavlnu nechte na běžné nošení.'),
    ])
