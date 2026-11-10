"""sporteka.cz — wave 20d (4. 11. 2026): long texts (>= 1650 words) for cyklo-vidlice-a-tlumice, basketbalova-obuv, trampoliny, tenisove-rakety.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklo-vidlice-a-tlumice
NEW['cyklo-vidlice-a-tlumice'] = dict(long=True,
    title='Vidlice a tlumiče na kolo: odpružení, servis, díly',
    desc='Odpružené i pevné vidlice, zadní tlumiče, servisní sady a pružiny pro MTB, trekking i freestyle. Jak vybrat zdvih, průměr kola a uchycení.',
    intro='<p>Vidlice drží přední kolo a zároveň rozhoduje o tom, jak si kolo poradí s kořeny, kameny a skoky. Odpružená vidlice pohlcuje nárazy a udržuje kolo v kontaktu s terénem, pevná je lehčí a nevyžaduje žádnou údržbu. '
          'Zadní tlumič plní stejný úkol u celoodpružených rámů. Každý díl je ale navržen pro konkrétní průměr kola, zdvih, typ osy a řízení, takže koupě naslepo končí často vrácením.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u vidlic od značek ' + B(('sr-suntour', 'SR Suntour'), ('rock-shox', 'Rock Shox'), ('marzocchi', 'Marzocchi'), ('striker', 'Striker'), ('suretti', 'Suretti'), ('force', 'Force')) + '. '
          'Najdete tu i servisní balíčky, prachovky, oleje a pružiny. Souvisí s tím <a href="/cyklo-dily/">cyklo díly</a>, <a href="/cyklo-riditka/">řídítka</a>, <a href="/cyklo-brzdy/">brzdy</a> a <a href="/horska-kola/">horská kola</a>. Níže je přehled typů, parametrů a údržby.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Jádro nabídky tvoří odpružené vidlice pro horská kola s průměrem kola 27,5 a 29 palců. Vedle nich jsou vidlice pevné, často karbonové nebo hliníkové, určené pro silniční, gravel a městská kola. '
          'Zvláštní skupinu tvoří vidlice na freestyle koloběžky a jednoduché pružinové vidlice pro dětská a městská kola. Doplňují je servisní sady, prachovky, olej, pružiny, ovladače odskoku a konverzní kity pro starší modely.</p>'
          '<p>Dětská kola, freestyle koloběžky i horská kola mají každé jiné standardy, takže vždy sledujte, pro jaký stroj je díl určen.</p>'
          '<h2>Typy vidlic</h2>'
          + T(['Typ', 'Princip', 'Typické použití'], [
              ['Pevná vidlice', 'bez odpružení, ocel, hliník nebo karbon', 'silnice, gravel, město, lehké kolo'],
              ['Pružinová odpružená', 'ocelová pružina, olejový nebo elastomerový útlum', 'rekreační trekink, vstupní MTB, e-kola'],
              ['Vzduchová odpružená', 'tlak vzduchu určuje tuhost, nastavuje se pumpičkou', 'sportovní MTB, cross-country, trail'],
              ['Dlouhozdvihová', 'silnější nohy, často vzduch a hydraulika', 'enduro, sjezd, bikepark'],
              ['Jednoduchá pružinová', 'základní pružina bez nastavení odskoku', 'rekreační, dětská a městská kola'],
              ['Freestyle vidlice', 'tuhá konstrukce pro skoky a triky', 'freestyle koloběžky, dirt']]) +
          '<h2>Zdvih podle použití</h2>'
          '<p>Zdvih je dráha, o kterou se vidlice stlačí. Větší zdvih znamená víc pohodlí v hrubém terénu, ale vyšší hmotnost a vyšší přední část kola. Pro cross-country se používají nižší hodnoty, pro trail a enduro střední a vyšší. '
          'Nejprve ověřte, kolik zdvihu váš rám snese. Příliš dlouhá vidlice změní geometrii, zvedne přední část a může zhoršit ovladatelnost.</p>'
          + T(['Disciplína', 'Charakter zdvihu', 'Poznámka'], [
              ['Cross-country a maraton', 'krátký až střední', 'lehkost a účinnost šlapání'],
              ['Trail a all-mountain', 'střední až delší', 'kompromis mezi stoupáním a sjezdem'],
              ['Enduro a bikepark', 'dlouhý', 'robustní nohy a tlumení pro prudké nárazy'],
              ['Trekink a rekreace', 'krátký', 'pohodlí na silnici a šotolině, často se zámkem']]) +
          '<h2>Průměr kola, řízení a osa</h2>'
          '<h3>Průměr kola</h3>'
          '<p>Vidlice na 26, 27,5 nebo 29 palců se nevyměňují libovolně. Menší kolo ve vidlici na větší průměr sníží přední část a změní řízení. Označení obvykle uvádí průměr kola přímo v názvu.</p>'
          '<h3>Typ řízení</h3>'
          '<p>Řízení určuje průměr krku vidlice. Nejběžnější je rovný krk o průměru 1 1/8 palce, existují i kónické krky a starší menší průměry. Rám musí mít odpovídající hlavovou trubku nebo redukční ložiska. Pokud jste nejistí, změřte vnitřní průměr misek řízení.</p>'
          '<h3>Osa a uchycení brzdy</h3>'
          '<p>Přední kolo upíná buď rychloupínák, nebo pevná osa různých průměrů a šířek nábojů. Kotoučová brzda vyžaduje odpovídající uchycení třmenu, obvykle podle velikosti kotouče. U ráfkových brzd musí vidlice mít patky nebo oka pro brzdové čelisti. Zkontrolujte tyto údaje proti náboji kola a brzdám v kategorii <a href="/cyklo-brzdy/">cyklo brzdy</a>.</p>'
          '<h2>Pružina, vzduch a nastavení</h2>'
          '<p>Pružinová vidlice je levnější a odolnější vůči chybám při nastavení, ale hůř se přizpůsobí hmotnosti jezdce. Vzduchová se nastaví tlakem, který odpovídá vaší váze a stylu jízdy, a je lehčí. '
          'Důležité je tzv. sag, tedy propad vidlice pod váhou jezdce ve stoji. Bývá to přibližně pětina až čtvrtina zdvihu podle disciplíny a doporučení výrobce. '
          'Zámek vidlice, který zpevní chod při jízdě do kopce nebo po silnici, a nastavení odskoku, které tlumí návrat do základní polohy, přinášejí větší kontrolu a hodí se zejména při delších výletech.</p>'
          '<h2>Zadní tlumiče</h2>'
          '<p>Zadní tlumič patří na celoodpružená kola. Měří se délkou mezi oky a zdvihem, případně rozměry upevnění. Při výměně musí rozměr přesně odpovídat rámu. Na vzduchových tlumičích se nastavuje tlak, na pružinových tuhost pružiny. '
          'Hledáte-li celé stroje, navštivte <a href="/celoodpruzena-horska-kola/">celoodpružená horská kola</a>. U e-kol je navíc třeba počítat s vyšší hmotností, kterou musí vidlice unést, viz <a href="/horska-elektrokola/">horská elektrokola</a>.</p>'
          '<h2>Servis a údržba</h2>'
          '<p>Vidlice je jemná mechanika, která pracuje v prachu, bahně a vodě. Pravidelný servis prodlužuje životnost a drží stabilní chod. Základem je čištění stírací manžety a nohou po každé špinavé jízdě.</p>'
          '<ul><li><strong>Prachovky:</strong> stírají nečistoty z nohou vidlice a bývají nejčastěji měněným dílem.</li>'
          '<li><strong>Olej:</strong> v dolních nohou se mění v intervalech doporučených výrobcem, podle ježdění tedy jednou či vícekrát za sezonu.</li>'
          '<li><strong>Servisní sady:</strong> obsahují těsnění a prachovky určené pro konkrétní řadu, například sady SR Suntour nebo Rock Shox.</li>'
          '<li><strong>Pružiny:</strong> měkčí či tvrdší pružina upraví vidlici podle hmotnosti jezdce, například u řady Marzocchi Bomber.</li>'
          '<li><strong>Konverzní kity:</strong> předělají starší vidlici na jiný zdvih nebo typ tlumení.</li></ul>'
          '<p>Složitější servis tlumicí kartuše nebo vzduchové komory svěřte servisu, který má potřebné nářadí a speciální oleje. Pro drobnosti využijte <a href="/cyklo-udrzba/">cyklo údržbu</a>.</p>'
          '<h2>Vidlice na freestyle koloběžky</h2>'
          '<p>Značka Striker nabízí vidlice pro freestyle koloběžky, které se označují zkratkami typu SCS nebo IHC podle způsobu komprese. Používají se do koloběžek s konkrétním průměrem hlavové trubky a šířkou osy kola. '
          'Při výběru zkontrolujte kompatibilitu s deskou, řídítky a kolem. Celé koloběžky najdete v <a href="/freestyle-kolobezky/">freestyle koloběžkách</a> a <a href="/kolobezky/">koloběžkách</a>, ochranu pro triky v <a href="/chranice-a-helmy/">chráničích a helmách</a>.</p>'
          '<h2>Pevné vidlice a upgrade kola</h2>'
          '<p>Karbonová pevná vidlice šetří hmotnost a tlumí vibrace lépe než hliník, vyžaduje ale pečlivé dotažení šroubů správným momentem. U gravel a silničních kol sledujte rozměry pro šířku pláště a typ brzdy. '
          'Chcete-li zlepšit pohodlí, začněte často <a href="/plaste-a-duse/">pláštěm</a> a jeho tlakem, nikoli výměnou vidlice. Stejně prospěšné bývá změnit <a href="/sedla-a-gripy/">sedlo a gripy</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě vidlice na jiný průměr kola, než má rám a plášť.</li>'
          '<li>Podcenění délky krku, takže vidlici nelze dostatečně ukotvit v představci.</li>'
          '<li>Nesprávné nastavení tlaku podle hmotnosti, které způsobí propadání nebo zbytečnou tuhost.</li>'
          '<li>Opomenutí uchycení kotouče, díky němuž třmen nepasuje.</li>'
          '<li>Objednání dílu podle podobného názvu bez kontroly, zda je určený pro vaše kolo a typ vidlice.</li></ul>'
          '<h2>Odpružení a typ jezdce</h2>'
          '<p>Lehký jezdec potřebuje měkčí pružinu nebo nižší tlak vzduchu, těžší jezdec naopak tužší nastavení, jinak vidlice dosedá na doraz. Výrobci uvádějí doporučené hodnoty podle hmotnosti jezdce s výbavou, takže při vážení počítejte s batohem a oblečením. '
          'Pokud vidlice při jízdě často bouchá na doraz, zvyšte tlak nebo tuhost, pokud se téměř nehýbe, tlak snižte. Odskok nastavujte tak, aby se vidlice vracela rychle, ale nepodskakovala.</p>'
          '<h2>Rekreace, trekink a město</h2>'
          '<p>Na trekingových a městských kolech se používají jednodušší pružinové vidlice s krátkým zdvihem a zámkem. Cílem není tlumit skoky, ale odfiltrovat nárazy z dlažby, kořenů a štěrku, aby jízda byla pohodlnější. '
          'Takové vidlice jsou odolné a nenáročné na údržbu. Hledáte-li celé stroje, projděte <a href="/trekingova-kola/">trekingová kola</a>, <a href="/mestska-kola/">městská kola</a> a <a href="/krosova-kola/">krosová kola</a>.</p>'
          '<h2>Montáž a kontrola po výměně</h2>'
          '<ul><li>Zkraťte krk vidlice podle výšky představce, ale nikdy ne víc, než je nutné, a vždy ponechte vzduchovou rezervu pro distanční podložky.</li>'
          '<li>Zkontrolujte, zda se po vložení ložisek řízení otáčí bez vůle a bez drhnutí.</li>'
          '<li>Namontujte kolo a kotouč, ověřte, že se třmen nedotýká rotoru, a přezkoušejte brzdu stojícím kolem.</li>'
          '<li>Šrouby utáhněte předepsaným momentem a po prvních kilometrech kontrolu zopakujte.</li></ul>'
          '<p>Pokud si nejste jistí s řezáním krku nebo lisováním ložisek, svěřte montáž servisu. Nesprávná montáž může ohrozit bezpečnost jízdy.</p>'
          '<h2>Rozdíly mezi značkami</h2>'
          '<p>SR Suntour je tradiční výrobce vidlic pro rekreační i sportovní kola s širokou nabídkou servisních sad, Rock Shox a Marzocchi mají dlouhou historii v terénní jízdě. Force nabízí pevné vidlice a díly pro každodenní jízdu, Suretti jednoduché pružinové vidlice a Striker specializované modely pro freestyle koloběžky. '
          'Při výběru nehledejte jen značku, ale především to, zda je vidlice určena pro váš průměr kola, zdvih a typ osy.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Každý produkt ukazuje ceny z několika obchodů najednou i skladovost. Do názvu se obvykle promítá průměr kola, zdvih a barva, tak je pečlivě porovnejte. Před objednávkou si uložte přesný model rámu a kola, protože u vidlic rozhodují drobné rozdíly v rozměrech a uchycení. '
          'Doplňky ke kolu hledejte v <a href="/cyklo-kola-a-rafky/">kolech a ráfcích</a>, <a href="/cyklo-pohon/">pohonu</a> nebo <a href="/cyklo-pedaly/">pedálech</a>.</p>',
    faq=[
        ('Jak poznám, jaká vidlice se hodí na moje kolo?', 'Zjistěte průměr kola, průměr krku řízení, typ osy a uchycení brzdy. Všechny čtyři údaje musí odpovídat, jinak se vidlice nenamontuje nebo bude jezdit špatně.'),
        ('Je lepší pružinová, nebo vzduchová vidlice?', 'Pružinová je jednodušší a odolná, vzduchová lehčí a lépe nastavitelná podle hmotnosti. Pro rekreaci stačí pružina, pro sportovní jízdu je vhodnější vzduch.'),
        ('Co znamená zdvih vidlice?', 'Je to maximální dráha, o kterou se vidlice stlačí. Delší zdvih je pohodlnější v hrubém terénu, ale kolo je těžší a přední část vyšší.'),
        ('Jak často servisovat vidlici?', 'Stírací manžety čistěte po každé špinavé jízdě. Olej a těsnění měňte podle doporučení výrobce, obvykle jednou za sezonu nebo po určitém počtu ujetých hodin.'),
        ('Dá se starší vidlice upravit na jiný zdvih?', 'U některých řad existují konverzní kity, které změní zdvih nebo pružinu. Vždy ověřte, že je kit určen přesně pro váš model a rok výroby.'),
        ('Můžu dát na kolo vidlici s větším zdvihem?', 'Jen pokud to výrobce rámu dovoluje. Delší vidlice zvedne přední část, změní geometrii řízení a může zhoršit stabilitu nebo narážet v rámu.'),
        ('K čemu je zámek vidlice?', 'Zpevní chod a zabrání kývání při šlapání do kopce nebo na silnici. Před technickým úsekem ho uvolněte, aby vidlice fungovala.'),
        ('Co je sag a jak ho nastavit?', 'Sag je propad vidlice pod váhou jezdce ve stoji, vyjadřuje se jako část zdvihu. Upravujete ho tlakem vzduchu nebo předpětím pružiny podle tabulky výrobce.'),
        ('Jak poznám, že vidlice odpovídá mému kolu?', 'Porovnejte průměr kola, délku a průměr řízené trubky, osu kola a typ brzd s údaji výrobce rámu. Rozhoduje i zdvih, který by měl odpovídat určení kola.'),
        ('Jde na karbonovou vidlici namontovat jakýkoli představec?', 'Použít se dá, ale utahujte vždy předepsaným momentem a případně s karbonovou montážní pastou. Příliš silné dotažení může karbon poškodit.'),
        ('Hodí se vidlice na freestyle koloběžku i na kolo?', 'Ne, mají jiné rozměry hlavové trubky, osy a nároky na pevnost. Vidlice se vybírá vždy pro stroj, pro který byla navržena.')
    ])

# ------------------------------------------------------------------ basketbalova-obuv
NEW['basketbalova-obuv'] = dict(long=True,
    title='Basketbalové boty: střih, tlumení a výběr velikosti',
    desc='Basketbalová obuv pro muže, ženy i děti: nízký, střední a vysoký střih, tlumení, podrážka do haly nebo ven. Porovnejte nabídky českých obchodů.',
    intro='<p>Basketbal je sport prudkých zastavení, výskoků, změn směru a dopadů, které zatěžují kotníky, kolena i chodidla. Specializovaná obuv proto kombinuje oporu paty, pevné držení v oblasti středu nohy, tlumení v podrážce a gumu, která na palubovce přilne. '
          'Obyčejná běžecká bota podobné boční síly nezvládá a hráč v ní více riskuje podvrtnutí.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů u modelů od značek ' + B(('nike', 'Nike'), ('jordan', 'Jordan'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('converse', 'Converse'), ('peak', 'Peak')) + '. '
          'K obuvi se hodí <a href="/basketbalove-mice/">basketbalové míče</a>, <a href="/dresy/">dresy</a>, <a href="/sportovni-ponozky/">sportovní ponožky</a> a <a href="/sportovni-obuv/">sportovní obuv</a> obecně. Níže najdete rozdíly mezi střihy, tlumením a podrážkami i rady pro velikost a péči.</p>',
    guide='<h2>Čím se basketbalová bota liší od jiných</h2>'
          '<p>Hráč při zápase většinu času nespurtuje rovně, ale brzdí, odráží se do stran a skáče. Bota proto musí zachytit boční síly, které by u běhu nevznikly. Má tužší svršek, širší základnu pro stabilitu, tlumení pod patou i předonoží a podrážku vzorovanou pro palubovku. '
          'Hmotnost bývá vyšší než u běžecké obuvi, protože ochrana a opora stojí materiál. Kategorie obsahuje pánské, dámské i dětské modely včetně signature řad slavných hráčů.</p>'
          '<h2>Nízký, střední a vysoký střih</h2>'
          + T(['Střih', 'Co nabízí', 'Pro koho'], [
              ['Nízký', 'nejvíc volnosti a nejnižší hmotnost, kotník se opírá o vlastní svaly', 'rychlí hráči, zkušení, často obránci a rozehrávači'],
              ['Střední', 'kompromis mezi opěrou a pohyblivostí', 'univerzální volba pro většinu hráčů'],
              ['Vysoký', 'kotníku poskytuje největší mechanickou oporu', 'pivoti, hráči po úrazech, začátečníci']]) +
          '<p>Zda vyšší bota skutečně brání podvrtnutí, je předmětem sporů. Důležitější než samotná výška je pevné šněrování, stabilní pata a vlastní kondice kotníku. Pokud jste měli v minulosti problémy, začněte u středního nebo vysokého střihu a doplňte posilování.</p>'
          '<h2>Tlumení a pocit z podlahy</h2>'
          '<p>Tlumení pohlcuje dopady po výskoku, ale zároveň může zhoršit pocit kontaktu s podlahou. Značky používají pěny různé tvrdosti, vzduchové vložky i kombinace. Měkčí tlumení uleví kloubům u větších hráčů, tvrdší a nižší dává větší rychlost reakcí.</p>'
          + T(['Priorita', 'Co hledat', 'Poznámka'], [
              ['Komfort a ochrana kloubů', 'silnější tlumení v patě i předonoží', 'hráči s vyšší hmotností, častý trénink'],
              ['Rychlost a kontrola', 'tenčí podešev, nižší střih', 'obránci, rozehrávači, mladší a lehčí hráči'],
              ['Všestrannost', 'středně silné tlumení', 'rekreační a školní basketbal']]) +
          '<h2>Podrážka: hala, nebo venek</h2>'
          '<p>Halová podrážka z měkčí gumy s hustým vzorem nejlépe přilne na parketu, ale na asfaltu se rychle ohladí. Pro venkovní hřiště vybírejte modely s odolnější gumou a hlubším vzorem, případně s označením pro outdoor. '
          'Na palubovce nenoste boty zablácené nebo z ulice, jinak se přilnavost sníží. Obecně sálovou obuv na jiné sporty najdete v kategorii <a href="/salova-obuv/">sálová obuv</a>, venkovní hry ve <a href="/micove-sporty/">míčových sportech</a>.</p>'
          '<h2>Pozice na hřišti a typ hráče</h2>'
          '<ul><li><strong>Rozehrávač:</strong> hodí se lehčí, nižší bota s dobrým pocitem z podlahy a rychlou reakcí.</li>'
          '<li><strong>Křídlo:</strong> střední střih, vyvážené tlumení a dobrá opora při střelbě i přihrávkách.</li>'
          '<li><strong>Pivot:</strong> robustní konstrukce, silné tlumení a vyšší opora kotníku pro dopady v souboji pod košem.</li></ul>'
          '<p>Jsou to doporučení, nikoli pravidlo. Skutečný rozdíl udělá pohodlí, tvar chodidla a styl hry.</p>'
          '<h2>Značky a řady v nabídce</h2>'
          '<p>Nike a Jordan patří k nejrozšířenějším značkám basketbalu. Jordan je samostatná řada, jejíž retro modely se nosí i jako lifestyle obuv, takže pozor, zda hledáte skutečně hrací verzi. '
          'Adidas nabízí signature řady hráčů, Puma moderní modely s výrazným tlumením, Under Armour řady Spawn nebo Lockdown a Peak čínské signature modely. Converse zastupují klasické modely i novější výkonnostní řady, například All Star BB. '
          'Dětské a levnější modely najdete také u značek Tarmak a Kipsta, které stavějí na rozumném poměru ceny a opory pro školní a klubový basketbal. U každého modelu se podívejte na popis, zda je primárně určen pro hru, nebo pro volný čas.</p>'
          '<h2>Velikost a správné nazutí</h2>'
          '<p>Měřte nohu odpoledne, kdy je lehce oteklá, a zkoušejte boty v ponožkách, v nichž budete hrát. Mezi špičkou a prsty ponechte asi šířku palce, aby prsty nenarážely při zastavení. '
          'Pata nesmí vyskakovat, přední část nesmí tlačit ze stran. Modely se liší šíří i pevností šněrování, takže se velikost napříč značkami lehce mění. U dětí počítejte s růstem, ale příliš velká bota zvyšuje riziko zakopnutí, takže rezerva zůstává malá.</p>'
          '<h2>Šněrování a zajištění paty</h2>'
          '<p>Utáhněte tkaničky od špičky k nártu rovnoměrně a poslední dírky využijte, pokud potřebujete větší oporu kotníku. Někteří hráči přidávají druhý uzel, aby se bota během hry neuvolnila. '
          'Při problémech s patou pomáhá šněrování technikou zámku, kdy se tkanička protáhne dvakrát nahoře. Správná technika zlepší stabilitu více než nákup dražší bot.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Boty po tréninku vyjměte z tašky a nechte vyschnout při pokojové teplotě. Vložky vytáhněte, aby se vlhkost neusazovala. Bělidlu a topení se vyhněte, poškodí lepení i pěnu. '
          'Halovou podrážku otřete vlhkým hadrem, aby si zachovala přilnavost. Tlumení časem ztrácí účinnost, a pokud cítíte nárůst únavy chodidel a kolen, je čas na novou obuv. Pro přepravu se hodí <a href="/sportovni-tasky/">sportovní tašky</a>.</p>'
          '<h2>Doplňky a ochrana</h2>'
          '<p>K obuvi patří funkční ponožky, které odvádějí pot a snižují riziko puchýřů. Pro nestabilní kotníky se používají ortézy a bandáže. Při tréninku může pomoct i <a href="/posilovaci-gumy/">posilovací guma</a> nebo <a href="/balancni-pomucky/">balanční pomůcky</a>, které posilují svaly kolem kotníku. '
          'Pro děti vybírejte lehčí modely a nezapomínejte na <a href="/chranice-a-helmy/">chrániče</a> při streetbalu na tvrdém povrchu.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě lifestyle verze retro modelu bez ohledu na to, že není určena pro intenzivní hru.</li>'
          '<li>Volba podle módy a barvy bez zkoušky, jak bota sedí na šířku chodidla.</li>'
          '<li>Použití halové obuvi na asfaltu, která se rychle opotřebuje.</li>'
          '<li>Příliš velká velikost, protože dítě ještě poroste.</li>'
          '<li>Zanedbání vložek a ponožek, přestože právě ony ovlivňují komfort.</li></ul>'
          '<h2>Jak poznat kvalitní basketbalovou botu</h2>'
          '<p>Kvalitní bota drží pevně patu a střed nohy, svršek se neprohýbá do stran a podrážka se nekroutí jako běžecká. Zkuste botu zkroutit v ruce, dobrá konstrukce klade odpor, zejména ve střední části. '
          'Dalším znakem je výška a tvar patního kontrafortu, který by měl obepínat patu bez tlaku na Achillovku. Zkontrolujte také jazyk, který nesmí při hře sjíždět, a stélku, jež se dá vyměnit za ortopedickou, pokud ji potřebujete.</p>'
          '<h2>Materiály svršku</h2>'
          + T(['Materiál', 'Vlastnosti', 'Poznámka'], [
              ['Kůže a syntetická kůže', 'pevná, tvarově stálá, hůř větraná', 'klasické modely, robustní opora'],
              ['Textilní síťovina', 'lehká a prodyšná', 'moderní výkonnostní modely, rychlé hráče'],
              ['Pleteninové svršky', 'přiléhavé, pružné, bez tvrdých švů', 'komfort a pocit ponožky'],
              ['Zesílení a TPU prvky', 'zpevňují boky a špičku', 'stabilita při bočním zatížení']]) +
          '<p>Prodyšné materiály se vyplatí v horké hale, ale často nabízejí menší oporu než kůže. Syntetické zesílení v bocích proto vyvažuje lehkost.</p>'
          '<h2>Lifestyle, nebo výkonnostní model</h2>'
          '<p>Mnoho basketbalových bot se nosí i mimo hřiště. Retro modely mají často stejný vzhled jako dříve, ale měkčí a méně stabilní konstrukci, vhodnou spíše pro chůzi než pro intenzivní hru. '
          'Pokud chcete hrát pravidelně, volte výkonnostní řadu, kterou výrobce označuje pro basketbal. Pokud boty potřebujete do města, najdete další možnosti v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Trénink a prevence zranění</h2>'
          '<p>Správná obuv jen část prevence. Rozcvičení kotníků, posilování lýtek a stabilizačních svalů, nácvik správného doskoku i přiměřená zátěž snižují riziko zranění víc než samotná bota. '
          'Po úrazu kotníku nechte vyjádřit lékaře nebo fyzioterapeuta a vraťte se ke hře postupně. Dobré tlumení šetří klouby, ale nezastaví přetížení při příliš častém hraní.</p>'
          '<h2>Basketbal venku a ve škole</h2>'
          '<p>Pro školní tělocvik a občasné hraní stačí jednoduchý model s pevným svrškem, protekční podrážkou a rozumnou cenou. Pokud hrajete hlavně na venkovních hřištích, počítejte s rychlejším opotřebením gumy a volte odolné modely. '
          'Míč, koš a další vybavení najdete v <a href="/basketbalove-mice/">basketbalových míčích a koších</a> a v kategorii <a href="/dresy/">dresy</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého modelu vidíte aktuální nabídky více obchodů a dostupné velikosti. Používejte filtr podle značky a sledujte, zda je model pánský, dámský nebo dětský. Pro další vybavení se podívejte na <a href="/kopacky/">kopačky</a> a ostatní <a href="/sportovni-obuv/">sportovní boty</a>, k oblečení na <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>',
    faq=[
        ('Jaký střih basketbalové boty zvolit?', 'Začátečníci a hráči po úrazech kotníku obvykle volí střední nebo vysoký střih. Rychlí hráči a obránci často preferují nízký, který nabízí více volnosti.'),
        ('Dá se v basketbalových botách chodit i běhat?', 'Dá, ale nejsou na dlouhý běh určeny. Jsou tužší a těžší než běžecká obuv, a navíc se zbytečně opotřebují mimo palubovku.'),
        ('Čím se liší halová a venkovní basketbalová obuv?', 'Halová podrážka má měkčí gumu pro maximální přilnavost na parketu. Venkovní guma je tvrdší a odolnější proti otěru o asfalt a beton.'),
        ('Jak poznám správnou velikost?', 'Zkoušejte v ponožkách ke hře a odpoledne. Prsty mají mít malou rezervu, pata nesmí vyskakovat a šířka nesmí tlačit.'),
        ('Je vysoká bota opravdu lepší proti podvrtnutí?', 'Poskytuje větší mechanickou oporu, ale důležité je také pevné šněrování a kondice kotníku. Samotná výška bot úrazům nezabrání.'),
        ('Jak často měnit basketbalovou obuv?', 'Podle intenzity hry. Když podrážka ztratila vzor, tlumení je sešlapané nebo cítíte větší únavu kloubů, je čas na novou.'),
        ('Jsou boty Jordan určené k hraní?', 'Část řady je výkonnostní a hraje se v ní, jiné modely jsou retro a spíš lifestyle. Přečtěte si popis nebo název, zda jde o basketbalovou verzi.'),
        ('Jak vybrat boty pro dítě?', 'Zvolte lehčí model správné velikosti s pevnou patou a šněrováním. Příliš velká obuv zvyšuje riziko zakopnutí, proto počítejte s rezervou jen kolem půl centimetru.'),
        ('Jak vysušit boty po zápase?', 'Vyndejte vložky, povolte tkaničky a nechte boty vyschnout při pokojové teplotě. Topení a přímé slunce poškozují lepení a pěnu.'),
        ('Hodí se basketbalové boty i na volejbal nebo florbal?', 'Pro halové sporty s prudkými změnami směru fungují, ale pro každý sport existují specializované boty. Viz kategorie sálová obuv.')
    ])

# ------------------------------------------------------------------ trampoliny
NEW['trampoliny'] = dict(long=True,
    title='Trampolíny: zahradní, vnitřní, sítě a příslušenství',
    desc='Zahradní a dětské trampolíny, ochranné sítě, kryty pružin, žebříky a kotvicí sady. Jak vybrat průměr, nosnost a bezpečné umístění.',
    intro='<p>Trampolína je jedna z nejoblíbenějších zahradních atrakcí a zároveň dobrý pohybový trénink. Skákání posiluje nohy a střed těla, zlepšuje koordinaci a děti u něj spálí spoustu energie. '
          'Zároveň jde o zařízení, u kterého rozhodují bezpečnostní prvky: ochranná síť, kryt pružin, stabilní konstrukce a správné umístění na zahradě.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u trampolín i příslušenství od značek ' + B(('insportline', 'Insportline'), ('master', 'Master'), ('springos', 'Springos'), ('marimex', 'Marimex'), ('sedco', 'Sedco'), ('berg', 'Berg'), ('domyos', 'Domyos')) + '. '
          'Zahradní vybavení hledejte také v <a href="/hry-na-zahradu/">hrách na zahradu</a>, <a href="/volny-cas/">volném čase</a>, <a href="/bazeny/">bazénech</a> a <a href="/nafukovaci-hracky/">nafukovacích hračkách</a>. Níže najdete rady k velikosti, konstrukci i údržbě.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Kromě kompletních trampolín tu jsou i náhradní díly: skákací plochy, pružiny, kryty pružin, ochranné sítě, žebříky, kotvicí sady a přístřešky. Část nabídky tvoří menší fitness trampolíny a dětské modely do bytu. '
          'Mnoho produktů patří k určité řadě, například Master Super, a vyžaduje přesný rozměr. Při opravě proto vždy zkontrolujte průměr, počet pružin a typ uchycení sítě.</p>'
          '<h2>Typy trampolín</h2>'
          + T(['Typ', 'Popis', 'Použití'], [
              ['Zahradní kruhová', 'velká skákací plocha s ocelovým rámem a pružinami', 'rodinné skákání, zahrada'],
              ['Obdélníková a oválná', 'delší plocha s předvídatelnějším odrazem', 'trénink, gymnastika, větší děti'],
              ['Vnitřní a dětská', 'menší rozměry, často s madlem', 'byt, malé děti'],
              ['Fitness trampolína', 'malý průměr, tlumené gumové lano nebo pružiny', 'cvičení, kardio, doma'],
              ['Zapuštěná', 'plocha v úrovni země', 'zahrada s vlastní jámou, nižší riziko pádu'],
              ['Se sítí vnitřní nebo vnější', 'síť brání pádu na zem', 'dětské skákání a obecně bezpečné použití']]) +
          '<h2>Průměr a velikost</h2>'
          '<p>Rozměr se u kruhových modelů udává v centimetrech nebo stopách. Menší průměry se hodí k malým zahradám a mladším dětem, větší nabídnou víc prostoru k odrazu, ale vyžadují víc místa. '
          'Kolem trampolíny musí být volný prostor bez stromů, plotů, laviček a elektrického vedení. Pamatujte i na výšku skoku, nad trampolínou nesmí viset větve ani střecha.</p>'
          '<h2>Nosnost a konstrukce</h2>'
          '<p>Každá trampolína má udanou maximální nosnost. Respektujte ji a počítejte s tím, že se na ní skáče často víc lidí najednou. Rám by měl být z pozinkované oceli odolné vůči korozi, nohy robustní a s dostatečnou plochou pro stabilitu. '
          'Skákací plocha se šije z polypropylenové tkaniny odolné vůči UV záření a pružiny se zavěšují v rovnoměrném rozestupu. Více pružin přináší plynulejší odraz a rovnoměrněji rozděluje zatížení.</p>'
          '<h2>Ochranná síť</h2>'
          '<p>Síť je nejdůležitější bezpečnostní prvek. Vnitřní síť upevněná uvnitř pružin brání vypadnutí a zabraňuje dopadu mezi pružiny. Vnější síť je umístěna mimo skákací plochu a nechává více prostoru. '
          'Zkontrolujte pevnost spojů, stav tyčí a zda se zip nebo vstup uzavírá. Poškozenou síť okamžitě vyměňte. Náhradní sítě a další díly vybírejte podle průměru a počtu pružin své trampolíny.</p>'
          '<h2>Kryt pružin a okraj</h2>'
          '<p>Kryt pružin je měkký pás přes okraj rámu. Chrání před pádem na kov a pružiny a zároveň zabraňuje zachycení prstů. Měří se podle průměru trampolíny. '
          'Po delší době na slunci kryt vyschne a rozpadá se, takže je vhodné ho vyměnit včas, i když zbytek trampolíny ještě slouží.</p>'
          '<h2>Umístění a kotvení</h2>'
          '<p>Trampolínu postavte na rovný, měkký pozemek, nejlépe na trávník, ne na beton ani dlažbu. Pod ní nesmí být tvrdé předměty. Větrné počasí může lehkou trampolínu zvednout, proto se používají kotvicí sady zatloukané do země. '
          'Neumisťujte ji v blízkosti plotu, bazénu nebo cest. Při silném větru a bouřce na trampolíně neskákejte a dbejte na to, aby byla pevně zakotvená. Děti by měly mít u skákání dohled dospělého.</p>'
          '<h2>Bezpečné skákání</h2>'
          '<ul><li>Skákat by mělo ve stejnou chvíli jen tolik lidí, kolik uvádí výrobce, u většiny dětských modelů jen jedno dítě.</li>'
          '<li>Salta a riskantní triky nepatří na rekreační trampolínu bez vedení zkušeného trenéra.</li>'
          '<li>Boty se na skákací plochu nenosí, hodí se ponožky s protiskluzem nebo bosé nohy.</li>'
          '<li>Před skákáním se vyprázdní kapsy a sundají šperky, brýle a ostré předměty.</li>'
          '<li>Dospělý zkontroluje síť, pružiny a rám před každou sezonou.</li></ul>'
          '<p>Pro další ochranu se hodí <a href="/chranice-a-helmy/">chrániče a helmy</a>, ačkoli samotná helma nenahrazuje dozor ani správnou techniku.</p>'
          '<h2>Pro koho a jak využít</h2>'
          '<p>Menší děti oceníjí nižší trampolínu s vnitřní sítí a madlem, starší děti zvládnou větší průměr. Pro dospělé je užitečná fitness trampolína, která se hodí na domácí kardio cvičení. '
          'Na cvičení doma navazují <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/balancni-pomucky/">balanční pomůcky</a> a <a href="/svihadla/">švihadla</a>. Pro skákání doplňují trénink <a href="/gymnasticke-pomucky/">gymnastické pomůcky</a> a <a href="/tanec-a-gymnastika/">tanec a gymnastika</a>.</p>'
          '<h2>Údržba po celý rok</h2>'
          '<p>Na jaře zkontrolujte pružiny, sváry a zinkování rámu, na podzim trampolínu vyčistěte od listí a vlhkosti. V zimě ji lze nechat stát, pokud výrobce nedoporučuje demontáž. '
          'Sníh zbytečně zatěžuje plochu a pružiny, proto jej odstraňujte. Skákací plochu čistěte vlažnou vodou a jemným mýdlem. Skladujte rozložené díly v suchu.</p>'
          '<h2>Náhradní díly a jak je vybrat</h2>'
          '<p>Při výměně plochy nebo sítě potřebujete průměr, počet pružin a způsob uchycení. Skákací plochy se prodávají podle počtu ok, kryty podle rozměru a sítě podle počtu tyčí. '
          'Díly od jiného výrobce někdy pasují, ale ověřte rozměry. Nejdříve porovnejte údaje na štítku původní trampolíny nebo v návodu.</p>'
          + T(['Díl', 'Co zjistit před koupí', 'Poznámka'], [
              ['Skákací plocha', 'průměr rámu, počet ok nebo pružin', 'měří se mezi uchycením pružin'],
              ['Kryt pružin', 'průměr trampolíny', 'volí se podle rozměru rámu'],
              ['Ochranná síť', 'průměr, počet tyčí, výška', 'zkontrolujte vstup a zip'],
              ['Žebřík', 'výška skákací plochy', 'usnadní nastupování dětem'],
              ['Kotvicí sada', 'typ půdy, počet kotev', 'pro trvalé umístění na zahradě']]) +
          '<h2>Dětské trampolíny a věk</h2>'
          '<p>Pro nejmenší děti existují nízké trampolíny s madlem nebo s ochranným pletivem. Většina výrobců uvádí doporučený věk a maximální nosnost, kterou je třeba dodržet. '
          'Mladší děti by neměly skákat na velkých zahradních trampolínách bez dozoru a bez vnitřní sítě. Dítě se učí nejprve zvládat základní skoky, a až poté se pouští do složitějších pohybů.</p>'
          '<h2>Pružiny, gumová lana a odraz</h2>'
          '<p>Většina zahradních trampolín používá ocelové pružiny, které dávají silný odraz. Některé fitness a dětské modely mají gumová lana, jež jsou tišší a dávají měkčí odraz, ale ten je mírnější. '
          'Pružiny časem ztrácejí sílu a rezivějí, proto je zkontrolujte po zimě. Poškozenou nebo prověšenou pružinu vyměňte celou sadou, aby se plocha zatěžovala rovnoměrně.</p>'
          '<h2>Skákání jako pohyb</h2>'
          '<p>Skákání zapojuje nohy, hýždě, střed těla i rovnováhu, takže se hodí jako zpestření domácího cvičení. Kratší trénink je dobrým doplňkem k jiným sportům a kardio lze zpestřit jednoduchými cviky. '
          'Pro rozcvičení a protahování poslouží <a href="/jogove-pomucky/">jogové pomůcky</a> a <a href="/joga-a-pilates/">jóga a pilates</a>. Každý by měl skákat podle své kondice a při bolesti přestat.</p>'
          '<h2>Co dělat při poškození</h2>'
          '<ul><li>Roztrhlou skákací plochu nebo uvolněný spoj na rámu přestaňte okamžitě používat.</li>'
          '<li>Rezavé pružiny a díly vyměňte dříve, než se roztrhnou a zraní někoho při skákání.</li>'
          '<li>Prasklý kryt pružin či sítě nahraďte novým, nesnažte se je lepit.</li>'
          '<li>Při pochybnostech o statice a poškození nosných nohou trampolínu raději vyřaďte.</li></ul>'
          '<h2>Prostor pod trampolínou a okolí</h2>'
          '<p>Skákací plocha je ve výšce, proto zvažte, co se děje pod ní. Pod trampolínou by neměly ležet hračky ani ostré předměty a zvířata se tam mohou schovávat. Trávník pod plochou trpí nedostatkem světla, a proto se doporučuje občas změnit umístění. '
          'Kolem se hodí měkký povrch, například tráva, mulč nebo kůra, který zmírní dopad při případném pádu.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Srovnání nabídek u každé položky usnadní výběr mezi obchody. Podívejte se na kompletní sadu, zda obsahuje síť, žebřík a kryt pružin, jinak je budete muset dokoupit. '
          'Pro léto se k trampolíně hodí i <a href="/bazeny/">bazény</a> a <a href="/nafukovaci-hracky/">nafukovací hračky</a>.</p>',
    faq=[
        ('Jakou velikost trampolíny vybrat?', 'Podle místa na zahradě a věku dětí. Počítejte s volným okolím alespoň několik metrů kolem a bez překážek nad skákací plochou.'),
        ('Je ochranná síť nutná?', 'Doporučuje se u všech trampolín pro děti. Síť výrazně snižuje riziko pádu na zem nebo mezi pružiny.'),
        ('Může na trampolíně skákat víc lidí najednou?', 'Jen pokud to výrobce dovoluje a nepřekročíte nosnost. Při více skokanech roste riziko kolizí, proto se doporučuje jeden.'),
        ('Jak kotvit trampolínu proti větru?', 'Pomocí kotvicí sady, kdy se kotvy zatlučou do země a pásy se upevní k rámu. Při bouřce a silném větru na trampolíně neskákejte a trampolínu mějte zakotvenou.'),
        ('Co znamená počet pružin?', 'Více pružin bývá plynulejší odraz a rovnoměrnější zatížení. U náhradní plochy musí počet odpovídat rámu.'),
        ('Jak vyměnit skákací plochu?', 'Zjistěte průměr rámu a počet pružin nebo ok, vyberte odpovídající plochu a pružiny postupně zavěste. Při montáži pracujte opatrně, pružiny jsou pod napětím.'),
        ('Dá se trampolína nechat venku přes zimu?', 'Většina zahradních trampolín to vydrží, pokud výrobce nestanoví jinak. Odstraňujte sníh a zvažte sundání sítě a krytu.'),
        ('Hodí se trampolína pro cvičení dospělých?', 'Ano, nejlépe menší fitness trampolína s tlumeným odrazem. Skákání zlepšuje kondici, koordinaci a posiluje nohy i střed těla.'),
        ('Jak dlouho vydrží kryt pružin a síť?', 'Podle slunce a počasí obvykle několik sezon. Při popraskání nebo roztřepení je vyměňte, aby neohrožovaly bezpečnost.'),
        ('Je lepší kulatá, nebo obdélníková trampolína?', 'Kulatá se hodí pro rodinné skákání. Obdélníková nabízí předvídatelnější odraz a využijí ji ti, kdo trénují.')
    ])

# ------------------------------------------------------------------ tenisove-rakety
NEW['tenisove-rakety'] = dict(long=True,
    title='Tenisové rakety: hlava, váha a vyvážení',
    desc='Tenisové rakety pro dospělé, juniory i děti: velikost hlavy, hmotnost, vyvážení, struny a grip. Porovnejte nabídky českých obchodů.',
    intro='<p>Raketa je nejdůležitější vybavení tenisty, ale nejlepší model neexistuje, existuje jen ten, který sedí vašemu stylu a síle. Lehká raketa s velkou hlavou odpouští chyby a pomáhá začátečníkům, těžší s menší hlavou dává kontrolu zkušeným hráčům. '
          'Rozhoduje také vyvážení, napnutí a délka struny, tloušťka a velikost držadla. Děti pak potřebují raketu podle výšky, nikoli podle věku.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u rakety od značek ' + B(('head', 'Head'), ('wilson', 'Wilson'), ('babolat', 'Babolat'), ('dunlop', 'Dunlop'), ('tecnifibre', 'Tecnifibre'), ('volkl', 'Volkl'), ('yonex', 'Yonex'), ('prince', 'Prince')) + '. '
          'K raketám patří <a href="/tenis/">tenis</a> obecně, <a href="/tenisova-obuv/">tenisová obuv</a>, <a href="/micove-sporty/">míčové sporty</a>, <a href="/padel/">padel</a> a <a href="/squash/">squash</a>. Níže najdete parametry, rady podle úrovně i péči o výzbroj.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Většinu nabídky tvoří dospělé rakety o délce 27 palců, doplněné dětskými a juniorskými modely, které se vyrábějí v délkách od 17 do 26 palců. Objevují se i startovní sady se dvěma raketami a míčky a kategorie obsahuje i tenisové rakety určené pro rekreační hru. '
          'Doplňky, jako jsou míče, gripy nebo struny, se v nabídce občas objeví také, širší výběr najdete v kategorii <a href="/tenis/">tenis</a>. Obecný přehled míčových her pak nabízí <a href="/micove-sporty/">míčové sporty</a>.</p>'
          '<h2>Základní parametry rakety</h2>'
          + T(['Parametr', 'Co určuje', 'Orientačně'], [
              ['Velikost hlavy', 'velikost sweet spotu, odpouštění', 'větší hlava = víc síly a tolerance, menší = víc kontroly'],
              ['Hmotnost', 'stabilita, síla úderu, zátěž paže', 'lehčí pro začátečníky, těžší pro pokročilé'],
              ['Vyvážení', 'rozložení váhy mezi hlavou a rukojetí', 'na hlavu = síla, na rukojeť = obratnost'],
              ['Struny a vzor', 'rotace, kontrola, výdrž', 'otevřený vzor = víc rotace, hustý = kontrola'],
              ['Profil ráfku', 'tuhost a pocit', 'tenčí profil = kontrola, silnější = výkon'],
              ['Délka', 'dosah a páka', 'standardně 27 palců, delší pro větší sílu']]) +
          '<h2>Hlava rakety</h2>'
          '<p>Velikost hlavy se udává ve čtverečních palcích. Rakety s velkou hlavou mají větší sweet spot, tedy místo, kde míč vyletí s největší účinností. Pomáhají začátečníkům a hráčům, kteří míč nezasahují vždy středem. '
          'Menší hlava dává přesnější kontrolu a tvrdší pocit, ale vyžaduje stabilnější úder. Střední velikost je kompromis, který volí většina klubových hráčů.</p>'
          '<h2>Hmotnost a vyvážení</h2>'
          '<p>Lehčí raketa se snadno rozpohybuje, ale hůř tlumí nárazy a je méně stabilní při tvrdých úderech. Těžší raketa míč nese a tlumí vibrace, ale unaví paži a zpomalí švih. '
          'Vyvážení na hlavu zvýší sílu úderu a pomáhá při servisu, vyvážení na rukojeť usnadní práci u sítě. Pokud trpíte bolestmi lokte, poraďte se s lékařem nebo trenérem a volte spíše měkčí rakety s tlumením vibrací než příliš tuhé.</p>'
          '<h2>Která raketa pro jakou úroveň</h2>'
          + T(['Hráč', 'Doporučení', 'Poznámka'], [
              ['Začátečník', 'lehčí raketa s větší hlavou', 'odpouští chyby a šetří paži'],
              ['Rekreační hráč', 'středně těžká raketa se střední hlavou', 'univerzální volba'],
              ['Pokročilý a klubový', 'těžší raketa s menší hlavou', 'kontrola, rotace a stabilita'],
              ['Junior', 'raketa podle výšky a délky', 'nesmí být příliš těžká']]) +
          '<h2>Dětské a juniorské rakety</h2>'
          '<p>Dítě potřebuje raketu úměrnou výšce a síle. Orientačně se volí podle výšky: menší děti mají rakety o délce 17 až 21 palců, starší 23 až 26 palců. '
          'Příliš dlouhá raketa kazí techniku a zatěžuje zápěstí. Dětské modely bývají velmi lehké z hliníku. Při přechodu na dospělou raketu zkontrolujte, zda dítě zvládne udržet vyvážení. '
          'Pro tréninky se hodí i raketa podle výšky v kombinaci s měkkými míčky. Do haly se hodí <a href="/salova-obuv/">sálová obuv</a>.</p>'
          '<h2>Struny a grip</h2>'
          '<p>Struny ovlivňují cit, kontrolu i trvanlivost. Naturální a multifilamentní struny jsou měkčí a šetří paži, polyesterové drží napětí a nabízejí rotaci, ale jsou tvrdší. '
          'Nižší napnutí zvyšuje výkon a komfort, vyšší kontrolu. Hráči, kteří hrají často, přestrunují raketu několikrát za sezonu, protože struny ztrácejí napětí i bez přetrhnutí. '
          'Grip se vybírá podle velikosti dlaně, orientačně se měří vzdálenost od ohybu prsteníku k podélné rýze dlaně. Přídavný overgrip zlepšuje přilnavost a snadno se vymění.</p>'
          '<h2>Značky a řady v nabídce</h2>'
          '<p>Head a Wilson patří k nejrozšířenějším značkám, Babolat je známý hráči pro rotaci, Tecnifibre je francouzská značka vyrábějící rakety i struny a Dunlop, Yonex a Prince nabízejí širokou škálu pro různé typy hráčů. '
          'Volkl zastupují klasické modely V-Cell. Levnější a startovní nabídku tvoří Artengo a Kuikma, tedy domácí značky Decathlonu. U každé rakety vždy kontrolujte označení, zda je pánská, dámská nebo dětská. '
          'Dámské modely bývají lehčí a vyvážené na hlavu, ale tenistky si mohou vybrat jakýkoli model.</p>'
          '<h2>Jak raketu otestovat</h2>'
          '<p>Nejlepší je půjčit si raketu nebo využít demo program v klubu. Sledujte, jak se vám švih pozná po desetiminutovém hraní, zda necítíte vibrace a zda raketa nezpomaluje servis. '
          'Při výběru podle parametrů porovnávejte hodnoty mezi značkami, protože každá je uvádí trochu jinak. Strunu si nechte napnout podle doporučeného rozmezí výrobce.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Raketu skladujte v obalu mimo extrémní teploty, ne v zavazadlovém prostoru auta, kde slunce a mráz snižují napětí strun. Po zápase otřete rám od prachu a antuky. '
          'Zkontrolujte rám, zda neukazuje trhliny, a přetáhněte grip, když začne klouzat. Struny vyměňte, jakmile ztratí pružnost nebo se začnou třepit. Pro přepravu se hodí <a href="/sportovni-tasky/">sportovní tašky</a>.</p>'
          '<h2>Zdravé paže a technika</h2>'
          '<p>Bolest lokte u tenistů často souvisí s přílišnou tuhostí rakety, nevhodným gripem a špatnou technikou. Pomáhají měkčí struny, lehčí napnutí a posilování předloktí. '
          'Pro kondici využijte <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/balancni-pomucky/">balanční pomůcky</a> a <a href="/svihadla/">švihadla</a>. K tenisu patří také <a href="/sportovni-obleceni/">sportovní oblečení</a> a <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Jiné raketové sporty</h2>'
          '<p>Padel, squash a badminton používají jiné rakety a nelze je zaměňovat s tenisovými. Padelová raketa je plná a bez strun, squashová má menší hlavu a je lehčí. '
          'Hledáte-li tyto sporty, využijte kategorie <a href="/padel/">padel</a>, <a href="/squash/">squash</a> a <a href="/stolni-tenis/">stolní tenis</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě rakety podle značky slavného hráče, aniž by odpovídala vaší síle.</li>'
          '<li>Příliš těžká raketa pro začátečníka, která vede k bolesti paže.</li>'
          '<li>Opomenutí velikosti gripu, kvůli kterému raketa klouže nebo zatěžuje zápěstí.</li>'
          '<li>Dětská raketa vybraná podle věku, nikoli podle výšky.</li>'
          '<li>Ponechání starých strun, které ztratily napětí.</li></ul>'
          '<h2>Rozdíl mezi stylem hry a raketou</h2>'
          '<p>Hráč, který hraje z konce kurtu a rád používá rotaci, ocení otevřený vzor strun a raketu se střední hmotností. Útočný hráč u sítě chce stabilitu, menší hlavu a těžší rám. '
          'Hráč s jednoruční bekhendovou úderovou technikou často preferuje jiné vyvážení než hráč s oboustranným bekhendem. Žádný z těchto údajů není pevné pravidlo, a proto má smysl raketu vyzkoušet.</p>'
          '<h2>Povrch kurtu</h2>'
          '<p>Na antuce je míč pomalejší a výměny delší, proto rotace a kontrola hrají větší roli. Na tvrdém povrchu je hra rychlejší a pomáhá raketa s vyšší stabilitou. '
          'V hale a na trávě se míč odráží nízko, ale základní výběr rakety se příliš nemění. Obuv podle povrchu najdete v kategorii <a href="/tenisova-obuv/">tenisová obuv</a>.</p>'
          '<h2>Rozdíl mezi tvrdou a měkkou raketou</h2>'
          '<p>Tuhost rámu určuje, kolik energie raketa vrací a kolik nárazu přenese do ruky. Tuhá raketa je výkonnější, ale tvrdší, měkká tlumí vibrace a hodí se pro citlivější paže. '
          'Údaj o tuhosti většina výrobců uvádí, ale číselné hodnoty nejsou plně srovnatelné mezi značkami, takže berte raději pocit při hře.</p>'
          '<h2>Co obsahuje startovní sada</h2>'
          '<p>Startovní sady spojují dvě rakety, míčky a obal. Hodí se pro rodiny a děti, které teprve zjišťují, jestli je tenis baví. Rakety bývají hliníkové a lehčí, což je pro začátek výhoda, ale po čase se vyplatí přejít na kvalitnější. '
          'Zkontrolujte, pro jaký věk je sada určena a jaká je délka rakety.</p>'
          '<h2>Příprava před zápasem</h2>'
          '<ul><li>Zkontrolujte napětí a stav strun, případně vyměňte overgrip.</li>'
          '<li>Rozcvičte rameno, loket a zápěstí a přidejte dynamické protažení nohou.</li>'
          '<li>Vezměte si náhradní raketu, pokud hrajete turnaj.</li>'
          '<li>Zkontrolujte míče, tlak v nich ovlivňuje odraz a pocit z úderu.</li></ul>'
          '<p>Další vybavení a tenisové doplňky najdete v kategorii <a href="/tenis/">tenis</a>, k tréninku se hodí i <a href="/micove-sporty/">míčové sporty</a>.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>U každého produktu vidíte nabídky více obchodů, dostupnost a velikosti gripu. Zkontrolujte, zda je raketa dodávána se strunami a obalem, protože u některých modelů se kupuje samostatně. '
          'Starší ročníky bývají dostupné se slevou a po sezoně se jejich výběr obměňuje, ale parametry zůstávají srovnatelné. Pro začínající hráče jsou praktické startovní sady.</p>',
    faq=[
        ('Jakou raketu zvolit jako začátečník?', 'Lehčí raketu s větší hlavou, která odpouští chyby a šetří paži. Příliš tuhé a těžké modely zbytečně unavují.'),
        ('Jak vybrat raketu pro dítě?', 'Podle výšky, nikoli věku. Příliš dlouhá raketa kazí techniku, proto dítě zvládne jen délku, kterou udrží kontrolovaně.'),
        ('Co znamená vyvážení rakety?', 'Rozložení váhy mezi hlavu a rukojeť. Na hlavu zvyšuje sílu, na rukojeť zlepšuje obratnost.'),
        ('Jak často přestrunovat raketu?', 'Strunám klesá napětí i bez přetržení. Aktivní hráči je mění několikrát za sezonu, rekreační alespoň jednou ročně.'),
        ('Jaké struny jsou šetrnější k paži?', 'Naturální a multifilamentní struny jsou měkčí, polyester tvrdší. Nižší napnutí také snižuje zátěž.'),
        ('Jak poznám velikost gripu?', 'Změřte vzdálenost od ohybu prsteníku k rýze dlaně nebo si raketu vyzkoušejte. Menší grip se dá zvětšit overgripem.'),
        ('Je těžší raketa lepší?', 'Dává stabilitu a sílu, ale unaví paži a zpomalí švih. Vhodnější je pro silnější hráče s dobrou technikou.'),
        ('Hodí se tenisová raketa na padel nebo squash?', 'Ne, tyto sporty mají vlastní rakety jiného tvaru a konstrukce. Najdete je v kategoriích padel a squash.'),
        ('Čím se liší dámská a pánská raketa?', 'Dámské bývají lehčí a vyvážené na hlavu, ale rozdíl je spíš marketingový. Vybírejte podle síly a stylu hry.'),
        ('Jak raketu skladovat?', 'V obalu, mimo extrémní teploty a vlhko. V kufru auta se napětí strun a lepení rámu zhoršují.'),
        ('Mám koupit startovní sadu?', 'Pro děti a rekreační hráče je to praktická volba. Sada obvykle obsahuje dvě rakety, míčky a obal.')
    ])


# ------------------------------------------------------------------ doplnění (rozšíření po kontrole počtu slov)
NEW['cyklo-vidlice-a-tlumice']['faq'].append(('Jak poznám, že vidlice potřebuje servis?', 'Typickým příznakem je olej na nohou, tvrdší nebo drhnoucí chod, cvakání při stlačení nebo vůle v řízení. Při takových projevech nejezděte dál a nechte vidlici zkontrolovat v servisu.'))
NEW['cyklo-vidlice-a-tlumice']['guide'] += ('<h2>Rychlý kontrolní seznam před koupí</h2>'
    '<p>Před objednávkou si poznamenejte průměr kola, průměr a délku krku, typ osy, uchycení brzdy a požadovaný zdvih. S těmito údaji se vyhnete nejčastějším omylům a výběr se zúží na několik modelů.</p>')
NEW['basketbalova-obuv']['faq'].append(('Jak dlouho se zabíhají nové basketbalové boty?', 'Většina modelů je pohodlná hned, ale tužší kožené svršky si zvyknou na nohu po několika trénincích. Před zápasem je proto vyzkoušejte při lehčím tréninku.'))
NEW['basketbalova-obuv']['faq'].append(('Čím nahradit vložku, když boty tlačí?', 'Zkuste jinou stélku odpovídající tvaru chodidla nebo ortopedickou vložku, pokud ji potřebujete. Pokud bota tlačí ze stran, je pravděpodobně úzká a pomůže jiný model s širší špičkou.'))
NEW['basketbalova-obuv']['faq'].append(('Jaké ponožky nosit k basketbalové obuvi?', 'Sportovní ponožky se zesílenou patou a špičkou, které odvádějí pot a nesmekají se. Bavlněné tlusté ponožky v hale při hře často způsobují puchýře a pocit zahřátí.'))
NEW['basketbalova-obuv']['guide'] += ('<h2>Rychlý kontrolní seznam před koupí</h2>'
    '<p>Rozhodněte, zda budete hrát v hale, nebo venku, vyberte střih podle zkušeností, poznamenejte si velikost a šířku chodidla a nezapomeňte, že model Jordan nebo Converse může být lifestyle verze. S těmito čtyřmi body se výběr výrazně zjednoduší a vrácení zboží bude výjimečné.</p>')
NEW['trampoliny']['intro'] += '<p>Před nákupem si také rozmyslete, kolik dětí bude skákat a zda se trampolína vejde do zahrady i s ochranným pásmem.</p>'
NEW['trampoliny']['faq'] += [
    ('Jak dlouho trvá sestavení zahradní trampolíny?', 'Většinu modelů smontují dva dospělí za několik hodin. Pozor na správné zavěšení pružin, které jsou pod napětím, a používejte rukavice a háček dodaný v balení.'),
    ('Kde trampolínu postavit?', 'Na rovný trávník mimo stromy, plot a elektrické vedení, s dostatečným volným prostorem všude kolem. Na beton ani dlažbu se nedoporučuje, protože pád by byl nebezpečnější.'),
    ('Dá se trampolína zapustit do země?', 'Ano, existují modely pro zapuštění, které snižují výšku pádu. Vyžadují jámu s odvodněním a pečlivou přípravu, aby se uvnitř nehromadila voda.')]
NEW['trampoliny']['guide'] += ('<h2>Rychlý kontrolní seznam před koupí</h2>'
    '<p>Změřte volné místo na zahradě, zjistěte nosnost a počet pružin, ověřte, zda je v ceně síť, žebřík a kryt pružin, a rozhodněte se, zda je pro vás důležitější velikost, nebo malá stopa na zahradě. '
    'U dílů sledujte shodu s průměrem a počtem pružin. Při pochybnostech porovnejte údaje s původním návodem a kontrolujte, zda díl odpovídá vašemu modelu.</p>'
    '<h2>Trampolína a sousedé</h2>'
    '<p>Trampolína stojí na zahradě na očích, proto zvažte vzdálenost od plotu a ohleduplné hodiny skákání. Při skákání se ozývá rachot pružin, který je slyšet i u sousedů. Gumová lana nebo kryty hluk částečně tlumí. '
    'Zeptejte se také pojišťovny, zda domácí trampolína nepatří mezi rizika, která je potřeba nahlásit v rámci pojištění domácnosti.</p>')
NEW['tenisove-rakety']['faq'].append(('Kolik raket si vzít na turnaj?', 'Ideálně dvě stejné rakety, aby bylo možné při přetržené struně rychle vyměnit. Obě by měly mít stejné vyvážení, hmotnost a napnutí.'))
NEW['tenisove-rakety']['faq'].append(('Jak poznám, že je grip opotřebovaný?', 'Je hladký, tvrdý nebo se loupe a raketa vám klouže v ruce. Stačí přidat nový overgrip, který je levný a vyměňuje se rychle.'))
NEW['tenisove-rakety']['guide'] += ('<h2>Rychlý kontrolní seznam před koupí</h2>'
    '<p>Určete úroveň hry, preferovanou velikost hlavy, přijatelnou hmotnost a velikost gripu a u dětí změřte výšku. Při srovnání cen sledujte, zda se jedná o nový ročník, zda je v balení obal a zda je raketa již nastrunena. '
    'Pokud se nemůžete rozhodnout mezi dvěma modely, raději vezměte lehčí a měkčí, bolest paže totiž vyléčíte hůř než zaplatíte za přestrunění.</p>')

NEW['trampoliny']['faq'].append(('Musí se trampolína před sezonou kontrolovat?', 'Ano, na jaře projděte rám, svary, pružiny, skákací plochu, síť i kryt pružin a poškozené díly vyměňte. Zkontrolujte také pevnost kotvení a stav povrchu pod trampolínou.'))
NEW['tenisove-rakety']['faq'].append(('Je lepší koupit raketu už nastrunenou?', 'U rekreačních modelů bývá raketa nastrunena z výroby a je okamžitě připravena. Pokročilí hráči si obvykle volí vlastní struny a napnutí a nechávají si raketu nastrunit v servisu.'))
NEW['tenisove-rakety']['faq'].append(('Může jedna raketa vydržet několik let?', 'Rám vydrží dlouho, pokud není poškozen. Strun a gripů se výměna týká mnohem častěji, takže při rozumné péči raketa slouží i řadu sezon.'))
