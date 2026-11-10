"""sporteka.cz — facet landing texts wave 123: damske-lyzarske-boty, hokejka-warrior, damske-rukavice, salomon-bezecke-boty.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ damske-lyzarske-boty
NEW['damske-lyzarske-boty'] = dict(
    title='Dámské lyžařské boty: flex, lýtko, last a velikost',
    desc='Dámské lyžařské boty: čím se liší od pánských, jaký flex zvolit, jak změřit mondo velikost, šířku lastu a lýtko. Rossignol, K2, Atomic, Nordica i Head.',
    intro='<p>Dámská lyžařská bota není jen pánský model v jiné barvě. Žena má v průměru nižší tělesnou hmotnost, štíhlejší lýtko a níže položené těžiště lýtkového svalu, a proto výrobci upravují výšku manžety, tuhost a objem skořepiny i vnitřní botičky. Správně sedící bota rozhoduje o tom, jestli vás po třetí jízdě bolí nárt, nebo jestli se na sjezdovku těšíte celý den. '
          'Na této stránce najdete ženské modely z kategorie <a href="/lyzarske-boty/">lyžařské boty</a>, od měkkých modelů pro začátečnice po sportovní boty s vyšším flexem. Průvodce vysvětluje, jak číst údaj o flexu, jak změřit chodidlo na mondo velikost, jak poznat šířku lastu a proč je u žen tak důležité lýtko. Pro srovnání s jinými skupinami se podívejte na <a href="/panske-lyzarske-boty/">pánské</a> a <a href="/detske-lyzarske-boty/">dětské lyžařské boty</a>.</p>',
    guide='<h2>V čem se dámská lyžařská bota liší</h2>'
          '<p>Většina výrobců staví dámské boty na stejné skořepině jako pánské, ale mění klíčové detaily. Nejde o marketing: lyžařka s lehčím tělem a užším lýtkem potřebuje jiné nastavení než lyžař, který tlačí do boty větší silou. Tabulka shrnuje rozdíly, které se v praxi nejvíc projeví.</p>'
          + T(['Část boty', 'Typická dámská úprava', 'Co to změní'], [
              ['Manžeta a lýtko', 'nižší a užší, někdy s možností nastavit objem lýtka', 'manžeta netlačí pod kolenem a lýtko nedře'],
              ['Flex', 'u srovnatelné třídy nižší hodnota než u pánské boty', 'lehčí lyžařka dokáže bota prohnout a zatížit lyži'],
              ['Vnitřní bota', 'užší pata a více izolace okolo lýtka a nártu', 'nohy tolik nemrznou, pata nepadá'],
              ['Poloha těžiště', 'ohyb a sklon manžety přizpůsobený kratší holeni', 'jízda v lehkém předklonu bez námahy'],
              ['Hmotnost', 'lehčí skořepina a přezky', 'menší únava při nošení a přesunech']]) +
          '<p>Označení W nebo Women na konci názvu je nejspolehlivější pomůcka. Některé řady ho nemají a ženám je nabízejí jako unisex, takže stojí za to dívat se i na tabulku flexu a na údaj o šířce lastu. Pokud vám sedí model označený jako pánský, nic se neděje, ale hlídejte hlavně lýtko a hmotnost, protože ty tvoří většinu potíží.</p>'
          '<h2>Flex: kolik tuhosti potřebujete</h2>'
          '<p>Flex vyjadřuje, jak velkou silou musíte tlačit na jazyk boty, aby se předklonila. Nižší číslo znamená měkčí botu, která odpouští chyby a je pohodlná při chůzi, vyšší číslo tuhou botu, která okamžitě přenáší pohyb na hranu. Čísla výrobců nejsou přesně srovnatelná, rozdíl mezi značkami může být deset bodů i víc. Použijte je proto jako hrubé pásmo, ne jako exaktní údaj.</p>'
          + T(['Pásmo flexu', 'Pro koho', 'Jaký je to pocit'], [
              ['do 70 (měkká)', 'začátečnice, pomalá rekreační jízda, lehčí postavy', 'bota se snadno předkloní, ale při vyšší rychlosti neposkytne oporu'],
              ['80–90 (střední)', 'rekreační lyžařky s jistou jízdou na upravených svazích', 'nejčastější volba, kompromis mezi pohodlím a přesností'],
              ['100–110 (pevná)', 'sportovně jezdící, vyšší rychlost, tvrdší sníh', 'přesné vedení lyže, vyšší nároky na techniku'],
              ['120 a více (závodní)', 'závodnice a velmi silné lyžařky', 'extrémně tuhá bota, pro rekreační jízdu nepohodlná']]) +
          '<p>Častá chyba: koupit botu s tuhostí „na vyrůstání“. U lyžařské boty to nefunguje. Příliš tuhý model se nepředkloní, lyžařka sedí v záklonu, bolí ji stehna a lyže jí ujíždí. Naopak příliš měkká bota se při větším zatížení prohne a neposkytne oporu. Správný flex pozná lyžařka tak, že při předklonu v prodejně cítí odpor, ale může se pohybovat bez námahy.</p>'
          '<h2>Mondo velikost a šířka lastu</h2>'
          '<p>Lyžařské boty se nekupují podle čísla, které nosíte u tenisek. Používá se mondopoint, tedy délka chodidla v centimetrech. Postavte se bosá patou ke zdi, označte nejdelší prst a změřte vzdálenost. Hodnota 24,5 cm odpovídá velikosti 24,5. Měřte oba chodidla a řiďte se větším, protože se často liší. Skořepina je o něco delší než chodidlo, a proto výrobci uvádějí skutečnou vnitřní délku v milimetrech.</p>'
          '<p>Druhý údaj je šířka lastu, tedy šířka skořepiny v přední části chodidla v milimetrech. Dámské boty bývají užší a nabízejí se v lastu kolem 98 až 100 mm, široká noha potřebuje spíše 102 mm a víc. Úzký last u široké nohy tlačí na kloub palce a malíku, široký u úzké nohy nedrží patu. Lyžařské boty se dají tepelně tvarovat a v servisu rozšířit, ale základ musí sedět.</p>'
          '<ul><li><strong>Nízký nárt:</strong> hodí se model s menším vnitřním objemem a přezkou, která dobře utáhne.</li>'
          '<li><strong>Vysoký nárt:</strong> potřebujete měkčí jazyk a více prostoru nad nártem, jinak bota bolí.</li>'
          '<li><strong>Silné lýtko:</strong> dívejte se na nastavení šířky manžety nebo na model s větším objemem.</li>'
          '<li><strong>Štíhlé lýtko:</strong> dobře padnou užší manžety, případně vložky pod jazyk.</li></ul>'
          '<h2>Jak zkoušet a co čekat po obutí</h2>'
          '<p>Botu si obujte s tenkou lyžařskou ponožkou, nikdy ne se silnou zimní. Dvě vrstvy ponožek zhoršují krevní oběh a zvětšují tlak. Po zapnutí přezek se předkloňte a zkuste kolenem tlačit dopředu. Pata se nesmí zvedat, prsty se mají dotýkat špičky a po minutě se mají mírně uvolnit. Lyžařskou botu zkoušejte alespoň patnáct minut a nesmí tlačit. Lehký tlak se po několika dnech uvolní, bolest nikoli. Vhodné <a href="/lyzarske-ponozky/">lyžařské ponožky</a> jsou tenké, bez švů a dosahují nad horní okraj boty.</p>'
          '<p>Mnoho žen trpí studenými chodidly. Příčinou bývá nejčastěji příliš těsná bota, která stlačuje cévy, a pak teprve slabá izolace. Pomáhají správná velikost, tenká merino ponožka a podle potřeby vyhřívané vložky nebo ponožky. Bota nikdy nesmí být naplněna silnou ponožkou.</p>'
          '<h2>Značky v nabídce a čím se profilují</h2>'
          '<p>V dámské nabídce jsou nejčastěji ' + B(('rossignol', 'Rossignol'), ('k2', 'K2'), ('atomic', 'Atomic'), ('nordica', 'Nordica'), ('head', 'Head'), ('salomon', 'Salomon')) + ' a dále ' + B(('fischer', 'Fischer'), ('dalbello', 'Dalbello'), ('tecnica', 'Tecnica'), ('lange', 'Lange')) + '. Rossignol nabízí řady Pure, s nimiž se setkáte mezi ženskými rekreačními modely, K2 zaujme modely Mindbender a systémem BOA, který nahrazuje část přezek kolečkem. Nordica má v nabídce řadu Cruise, Head modely Edge a Atomic ženské verze řad Hawx. Detailnější přehled hledejte v samostatných výběrech <a href="/lyzarske-boty-atomic/">Atomic</a>, <a href="/lyzarske-boty-head/">Head</a> a <a href="/salomon-lyzarske-boty/">Salomon</a>.</p>'
          '<p>Rozdíly mezi značkami jsou především ve tvaru lastu a objemu. Jedna značka sedí ženám s úzkou nohou, jiná těm s širším předonožím, a proto není moudré vybírat jen podle jména. Vyzkoušejte alespoň dvě značky a vyberte tu, která sedí bez zásahu.</p>'
          '<h2>Přezky, BOA a chůze v botě</h2>'
          '<p>Klasická bota má čtyři přezky, které se dají doladit po jednom zubu. Systém BOA používá ocelové lanko a kolečko, takže se utahuje plynule jednou rukou a dobře drží i při jízdě. Nevýhodou je složitější oprava, pokud lanko přeruší. Některé modely mají režim chůze, který uvolní manžetu pro pohodlné chození po schodech i po chodníku. Podrážky pro chůzi (označované jako GripWalk nebo podobně) mají vroubkovaný profil a drží na ledu i na dlažbě. Pozor: takové boty vyžadují kompatibilní vázání, jinak se do lyže nezaklapnou. Podrobnosti najdete v kategorii <a href="/lyzarske-vazani/">lyžařské vázání</a>.</p>'
          '<h2>Pro koho které boty</h2>'
          '<ul><li><strong>Začátečnice:</strong> měkčí flex, pohodlná vnitřní bota a širší manžeta, aby se bota dobře nazouvala.</li>'
          '<li><strong>Rekreační jízda několik dnů do roka:</strong> střední flex, režim chůze a snadné zapínání.</li>'
          '<li><strong>Sportovní jízda:</strong> pevnější flex, úzký last a přesné vedení hrany.</li>'
          '<li><strong>Skialpinistky a freeride:</strong> lehčí bota s režimem chůze a dobrou protiskluzovou podrážkou.</li></ul>'
          '<p>K botám se hodí <a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyzarske-hole/">lyžařské hole</a> a <a href="/lyzarske-helmy/">helma</a>. Boty přepravujte v <a href="/lyzarske-vaky-a-tasky/">tašce na lyžařské boty</a>, aby se nepoškodily podrážky. Oblečení doplníte v sekci <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Po jízdě vyndejte vnitřní botu a nechte skořepinu i botičku uschnout při pokojové teplotě. Radiátor, vyhřívaná skříň ani vysoušeč vlasů se nehodí, protože deformují materiál. Na konci sezóny přezky zavřete, aby si skořepina držela tvar, a boty uložte na suché místo mimo slunce. Pokud bota po několika sezónách ztratí oporu a vnitřní botička se rozpadá, často pomůže výměna botičky v servisu. Starší boty s oprýskanou podrážkou raději nepoužívejte, protože se mohou při zapínání do vázání chovat nepředvídatelně.</p>',
    faq=[
        ('Jaký flex zvolit jako začínající lyžařka?', 'Hledejte měkčí boty do zhruba sedmdesáti nebo střední kolem osmdesáti až devadesáti. Měkká bota odpouští chyby a pohodlně se chodí, takže ji ocení lyžařka, která jezdí pomalu a opatrně. Příliš tuhá bota by ji zbytečně unavovala a ztěžovala učení techniky.'),
        ('Jak změřit mondo velikost?', 'Postavte se bosá patou ke zdi a změřte vzdálenost k nejdelšímu prstu v centimetrech. Měřte obě nohy a použijte větší hodnotu. Výsledek zaokrouhlený na půl centimetru odpovídá mondopoint velikosti, například 24,5. Při zkoušení pak ověřte také vnitřní délku v milimetrech.'),
        ('Čím se dámská bota liší od pánské?', 'Obvykle má nižší a užší manžetu, měkčí flex, užší patu a lehčí konstrukci. Přizpůsobuje se štíhlejšímu lýtku a nižší hmotnosti. Rozdíl je největší u sportovních modelů, u měkkých rekreačních bot se projeví méně.'),
        ('Co znamená last 98, 100 nebo 102 mm?', 'Jde o šířku skořepiny v přední části chodidla. Úzký last okolo 98 mm sedí štíhlé noze, střední kolem 100 mm většině lyžařek, široký od 102 mm nohám s širším předonožím. Při nesprávném lastu tlačí botu na kloubech nebo pata nedrží.'),
        ('Mohu si koupit pánskou botu?', 'Ano, pokud vám sedí lýtko, délka i šířka. Pro ženu s širším lýtkem nebo velkou nohou bývá pánská bota dokonce pohodlnější. Hlídejte hlavně příliš vysoký flex, který je pro lehčí postavu zbytečně tuhý.'),
        ('Proč mi v lyžařských botách mrznou nohy?', 'Nejčastější příčinou je příliš těsná bota nebo silná ponožka, které omezují prokrvení. Zkuste tenkou merino ponožku, upravte tlak přezek a po jízdě bota vysušte. Pomoci mohou i vyhřívané vložky nebo ponožky, ale základem je správná velikost.'),
        ('Jaká je výhoda systému BOA?', 'Utahuje se plynule jednou rukou a lépe rozkládá tlak než jednotlivé přezky. Dobře se obsluhuje v rukavicích a drží nastavení během jízdy. Slabinou je složitější oprava při přetržení lanka.'),
        ('Pořídit boty na míru, nebo koupit hotové?', 'Většině lyžařek stačí hotová bota s vyjímatelnou vnitřní botičkou, kterou lze v servisu tepelně přizpůsobit. Úprava na míru se vyplatí u problematických nohou nebo při častém lyžování. I tak je nutné vyjít z modelu, který sedí v základní velikosti.'),
        ('Jak dlouho vydrží lyžařské boty?', 'Záleží na počtu dnů na svahu a péči. Skořepina vydrží mnoho sezón, vnitřní botička se však časem vymačká a ztrácí oporu. Pokud bota drží tvar a přezky fungují, stačí obvykle vyměnit botičku nebo vložku.'),
        ('Mohu v dámských botách chodit i po zpevněných cestách?', 'Ano, pokud mají podrážku určenou pro chůzi a režim chůze, který uvolní manžetu. Hladká klasická podrážka na dlažbě klouže a rychle se opotřebuje. Pro delší přesuny je lepší obuvi s rýhovaným profilem.'),
    ])

# ------------------------------------------------------------------ hokejka-warrior
NEW['hokejka-warrior'] = dict(
    title='Hokejka Warrior: řady Alpha, Covert, Rise a Berzerker',
    desc='Hokejka Warrior: kompozitové řady Alpha, Covert, Rise, LX3 a QR6, jak zvolit flex, délku, levou či pravou a profil čepele pro juniora i seniora.',
    intro='<p>Warrior je americká hokejová značka, která patří pod New Balance a dlouhodobě sází na kompozitové hole s výrazným designem. V nabídce se opakují jména Alpha, Covert, Rise, LX3 nebo QR6 a pro nejmenší hráče řada Berzerker. Kromě samotných holí se tu objevují i miniaturní sběratelské kousky. '
          'Na této stránce jsou hokejky Warrior z kategorie <a href="/hokejky/">hokejky</a>, a to ve velikostech senior, intermediate i junior. Průvodce vysvětluje, jak se orientovat v názvech modelů, jak vybrat flex a délku podle hmotnosti a výšky, co znamená levá a pravá a jaké je označení profilu čepele. Pro srovnání s dalšími výrobci slouží přehledy <a href="/bauer-hokejky/">Bauer</a> a <a href="/ccm-hokejky/">CCM</a>.</p>',
    guide='<h2>Jak číst názvy modelů Warrior</h2>'
          '<p>Název hole se skládá z řady, úrovně, velikostní kategorie a profilu čepele. Například „Alpha LX3 Pro Senior W03 Levá“ říká: řada Alpha, varianta LX3 Pro, dospělá velikost, čepel W03 a levý úchop. Čím lépe pojmenování rozluštíte, tím snáze porovnáte stejné modely u různých obchodů. Níže je přehled řad, které se v nabídce značky objevují.</p>'
          + T(['Řada', 'Co v názvu hledat', 'Poznámka k výběru'], [
              ['Alpha (LX3, Deluxe, Pro)', 'kompozitová hůl s označením úrovně', 'běžně se vyskytuje ve velikostech senior, intermediate a junior'],
              ['Covert (Deluxe)', 'kompozitová hůl, často v bílé variantě', 'v nabídce hlavně velikosti junior až senior'],
              ['Rise', 'kompozitní hůl se základním vybavením', 'vhodná pro rostoucí hráče a pro rekreační hru'],
              ['LX3 Comp', 'junior a intermediate kompozit', 'v názvu hledejte úroveň Comp, Pro nebo Deluxe'],
              ['QR6 (Rev)', 'starší nebo specifičtější řada', 'před koupí ověřte tvar čepele a flex'],
              ['Berzerker', 'dětské hole levé i pravé', 'ideální pro první sezónu a pro mladší děti'],
              ['Swagger Calgary', 'mini hokejka', 'sběratelský a dárkový předmět, ne pro hru']]) +
          '<p>Přípony Pro, Comp nebo Deluxe obvykle odlišují úroveň výbavy a hmotnost. Konkrétní rozdíl mezi nimi se mění podle ročníku, proto ho ověřte v popisu nabídky: u každého modelu sledujte hmotnost v gramech, materiál a údaj o flexu. Nikdy se nespoléhejte jen na barvu nebo velikost loga.</p>'
          '<h2>Velikostní kategorie a flex</h2>'
          '<p>Hokejky se dělí na kategorie podle věku a výšky: senior pro dospělé a dorost, intermediate pro mládež zhruba od vyššího věku školy, junior pro děti a youth pro nejmenší. Číslo flexu říká, jak moc je hůl tuhá, a platí pravidlo, že tuhost má odpovídat tělesné hmotnosti hráče. Orientační vodítko říká, že flex má být přibližně polovina hmotnosti v librách, tedy zhruba hmotnost v kilogramech vynásobená 1,1. Pro hráče, který hodně střílí, bývá žádoucí o něco nižší hodnota, aby se hůl dobře prohnula.</p>'
          + T(['Kategorie', 'Typický flex', 'Komu je určena'], [
              ['Youth', 'nižší, přibližně do 30', 'nejmenší děti na prvním bruslení'],
              ['Junior', 'zhruba 40 až 50', 'děti přibližně od devíti let do dorostu'],
              ['Intermediate', 'zhruba 55 až 65', 'dorostenci a lehčí dospělí'],
              ['Senior', 'zhruba 75 až 100 i víc', 'dospělí hráči a silnější dorostenci']]) +
          '<p>Hodnoty jsou orientační, každý výrobce značí tuhost trochu jinak. Nejdůležitější je zjistit, jak se hůl při kontaktu s ledem prohne. Pokud ji příliš tvrdě tlačíte a nepohne se, je pro vás moc tuhá. Pokud se jí při střele zkroutí do slabé zbraně, je naopak měkká.</p>'
          '<h2>Délka hole a zkracování</h2>'
          '<p>Při stání v botách bez bruslí má hokejka sahat zhruba k nosu, na bruslích přibližně k bradě. Vyšší hráč se špatně ohýbá, nižší hráč dělá chyby při vedení puku. Kratší hůl lépe ovládá puk, delší dává větší dosah. Zkracování je možné, ale mění flex: každý ustřižený centimetr hůl ztuhne. Proto raději vybírejte dobrou délku už při nákupu a zkracujte jen o malou hodnotu. Úpravy, násady i čepele najdete v kategorii <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>.</p>'
          '<h2>Levá, pravá a profil čepele</h2>'
          '<p>Hůl s označením L nebo Levá drží hráč levou rukou dole, ruka dole určuje stranu čepele. Poznáte to podle toho, kterou rukou se přirozeně opřete při držení koštěte nebo golfové hole. Pokud váháte, nechte dítě vyzkoušet obě varianty nebo se zeptejte trenéra. U začátečníků je dobré od začátku zvolit stranu, která sedí, protože pozdější přeučování je zdlouhavé.</p>'
          '<p>Kód typu W03 nebo W28 označuje profil čepele. Profil zahrnuje zakřivení, hloubku oblouku a úhel mezi čepelí a násadou. Hluboký oblouk usnadňuje zvedání puku, plochý profil se hodí na rychlé přihrávky a střelbu z pohybu. Profil volte podle stylu hry, a pokud ho neznáte, vezměte střední nebo ten, který hráč používal dosud.</p>'
          '<ul><li><strong>Hráč, který střílí zápěstím:</strong> střední až hlubší oblouk, který puk zvedá.</li>'
          '<li><strong>Hráč, který přihrává a obsluhuje puk:</strong> plošší profil, snadnější příjem přihrávek.</li>'
          '<li><strong>Obránce:</strong> delší hůl a rovnější čepel pro dosah a stabilní přihrávku.</li></ul>'
          '<h2>Warrior vedle Baueru, CCM a dalších</h2>'
          '<p>Značky na trhu s hokejkami se liší tím, jak široký mají sortiment. Bauer a CCM nabízejí největší výběr řad a úrovní, Warrior je užší a soustředí se na kompozit. V této nabídce je málo obchodů a modelů, takže srovnání cen mezi nimi je rychlé, ale některé kombinace flexu a profilu čepele nemusí být skladem. Pro širší výběr se podívejte na <a href="/bauer-hokejky/">hokejky Bauer</a>, <a href="/ccm-hokejky/">hokejky CCM</a> a <a href="/fischer-hokejka/">hokejky Fischer</a>. Mezi značkami v celé kategorii jsou i ' + B(('bauer', 'Bauer'), ('ccm', 'CCM'), ('winnwell', 'Winnwell'), ('sherwood', 'Sherwood'), ('fischer', 'Fischer')) + '.</p>'
          '<p>Hledáte-li dětskou variantu, projděte si <a href="/detska-hokejka/">dětské hokejky</a>. Hráči, kteří chtějí výrazný vzhled, vyberou z <a href="/zlata-hokejka/">zlatých hokejek</a>.</p>'
          '<h2>Co dalšího s holí koupit a jak ji ošetřit</h2>'
          '<p>Nová hokejka obvykle nemá omotanou čepel, takže musíte přikoupit pásku. Vrstva textilní pásky zlepšuje ovládání puku a chrání čepel před poškrábáním. Na rukojeť se hodí koncovka nebo páska pro lepší úchop. Všechno potřebné najdete v kategorii <a href="/hokejove-pasky-a-doplnky/">pásky, tkaničky a doplňky</a>. Ke hře patří i <a href="/hokejove-brusle/">brusle</a> a <a href="/hokejove-chranice/">chrániče</a>, celkový přehled je na stránce <a href="/hokej/">hokej</a>.</p>'
          '<p>Po tréninku čepel otřete a hůl nenechávejte v zavazadlovém prostoru auta při mrazu ani při silném horku. Kompozit snáší hrubé zacházení hůř, než se zdá: ostrý náraz na hranu brusle nebo dveře může vytvořit trhlinu, která se projeví až při střele. Při jakémkoli podezření na prasklinu hůl raději vyřaďte, protože prasklá hůl se může zlomit při střele.</p>'
          '<h2>Kdy se vyplatí kompozit a kdy něco jednoduššího</h2>'
          '<p>Kompozit je lehký a citlivý, ale není nejlevnější a rychle roste ztráta při poškození. Pro děti, které rychle rostou, je vhodné zvolit jednodušší model v nižší úrovni a vybírat s rezervou jedné velikosti. Pro hráče, kteří trénují několikrát týdně, se vyplatí lehčí hůl vyšší úrovně, protože pomáhá s rychlostí rukou. Rekreační hráči si obvykle vystačí s modelem střední třídy.</p>'
          '<h2>Hokejka pro dítě: na co myslet</h2>'
          '<p>U dětí se hokejka kupuje s ohledem na výšku, ne na věk. Dvě stejně staré děti mohou potřebovat zcela jiné délky. Pro nejmenší se vyplatí lehká hůl s krátkou násadou, aby se dítě nemuselo shýbat a mohlo puk vést blízko těla. Mladší hráči rostou rychle, proto sledujte délku každou sezónu a při přechodu z junior na intermediate přihlížejte hlavně k hmotnosti hráče. Při výběru levé či pravé strany nechte rozhodnout dítě a trenéra. Dětské modely a jiné značky najdete ve výběru <a href="/detska-hokejka/">dětská hokejka</a>.</p>'
          '<h2>Na co se zeptat před koupí</h2>'
          '<ul><li>Jaká je hmotnost hole v gramech a z jakého materiálu je čepel?</li>'
          '<li>Je čepel pevně spojená s násadou, nebo jde o dvoudílnou hůl s výměnnou čepelí?</li>'
          '<li>Jaký je flex a jaká je kategorie velikosti, tedy senior, intermediate nebo junior?</li>'
          '<li>Je skladem požadovaná strana a profil čepele, nebo se nabízí jen jedna varianta?</li></ul>'
          '<p>Pokud některý údaj v nabídce chybí, porovnejte ho s popisem stejného modelu v jiném obchodě. Stejný model se někdy prodává pod mírně odlišným názvem a údaje o flexu se tak ztrácejí.</p>',
    faq=[
        ('Jaký flex hokejky zvolit?', 'Orientačně polovinu tělesné hmotnosti v librách, což je přibližně hmotnost v kilogramech vynásobená 1,1. Hráč, který hodně střílí zápěstím, může zvolit mírně nižší flex. Konkrétní hodnotu vždy porovnejte s tabulkou výrobce.'),
        ('Jak poznám, jestli potřebuji levou, nebo pravou hokejku?', 'Levá hokejka se drží levou rukou dole a čepel míří doprava dopředu. Zkuste držet koště nebo golfovou hůl a všimněte si, která ruka je dole. Děti nechte vyzkoušet obě varianty na ledě nebo na podlaze.'),
        ('Kolik má hokejka měřit?', 'V botách bez bruslí má sahat k nosu, na bruslích k bradě. Vyšší hůl dává větší dosah, kratší lepší ovládání puku. Zkracování mění flex, proto se mu pokud možno vyhýbejte.'),
        ('Co znamená označení W03 nebo W28?', 'Jde o profil čepele, tedy její zakřivení a hloubku oblouku. Různé profily se hodí pro jiný styl hry. Pokud nevíte, vyberte střední profil nebo stejný, který hráč používal dosud.'),
        ('Jak poznat rozdíl mezi úrovní Pro, Comp a Deluxe?', 'Úroveň se odráží v hmotnosti, použitých materiálech a vyvážení. Přesné rozdíly se mění podle ročníku, proto čtěte popis nabídky a porovnávejte hmotnost. Pro rekreační hru nemusíte volit nejvyšší úroveň.'),
        ('Je kompozitní hokejka lepší než dřevěná?', 'Je lehčí a pružnější, takže při stejné síle vystřelí rychleji. Dřevěná hůl je odolnější proti nárazům a levnější, což oceníte u začátečníků. Pro pravidelné tréninky a zápasy se většinou volí kompozit.'),
        ('Čím se liší hokejka Berzerker?', 'Jde o dětskou řadu s levým i pravým provedením. Je určená pro začátečníky a mladší hráče, kteří potřebují odolnou a lehkou hůl. U vyšších věkových kategorií se hodí modely junior a intermediate z jiných řad.'),
        ('Je mini hokejka Warrior určená ke hře?', 'Ne. Jde o miniaturní suvenýr nebo dárek, který se hodí jako dekorace nebo sběratelský předmět. Pro skutečnou hru potřebujete plnohodnotnou hůl v odpovídající velikosti.'),
        ('Jak poznám, že je hokejka poškozená?', 'Hledejte praskliny, ohyby a odlupující se vrstvu laku, zejména v místě, kde se čepel spojuje s násadou. Při ohnutí nebo střele zazní praskání. Kompozitová hůl s trhlinou se může zlomit, proto ji raději vyměňte.'),
        ('Co koupit spolu s novou holí?', 'Pásku na čepel, pásku nebo koncovku na rukojeť a případně náhradní čepel. Ke hře patří i chrániče, brusle a helma. Při výběru hole pro dítě počítejte s růstem a každý rok zkontrolujte délku.'),
    ])

# ------------------------------------------------------------------ damske-rukavice
NEW['damske-rukavice'] = dict(
    title='Dámské rukavice: zimní, softshell, běžecké i cyklistické',
    desc='Dámské rukavice na lyže, běh, kolo i do města: jak změřit velikost, rozdíl mezi prsty a palčáky, membrána, softshell, merino a péče. Viking, Swix, Reusch.',
    intro='<p>Dámské rukavice jsou užší v dlani, mají kratší prsty a menší obvod zápěstí než pánské. Pro ženy s drobnější rukou je proto rozdíl mezi dámským a unisex modelem patrný hned při prvním nasazení: pánská rukavice se v prstech svírá a v dlani se nabírá, což zhoršuje cit i teplo. Dámská nabídka je ale široká. Najdete tu zimní rukavice na lyže, softshell na procházky, tenké běžecké modely i cyklistické a gravel rukavice. '
          'Na této stránce jsou rukavice z kategorie <a href="/sportovni-rukavice/">sportovní rukavice</a> určené ženám. Průvodce vysvětluje, jak změřit ruku, jak se liší prstové rukavice a palčáky, jak fungují membrány a které materiály volit pro jaký sport. Chcete-li porovnat s ostatními skupinami, otevřete <a href="/panske-rukavice/">pánské rukavice</a>.</p>',
    guide='<h2>Jak změřit ruku a jak sedí dámská rukavice</h2>'
          '<p>Velikost rukavic se odvozuje od obvodu dlaně. Změřte krejčovským metrem obvod otevřené dlaně těsně pod klouby prstů, bez palce. Výsledek v centimetrech vydělte hodnotou 2,54 a dostanete velikost v palcích, kterou používá většina výrobců. Dámská ruka obvykle vychází mezi šesti a devíti palci. Některé značky používají S, M, L a ve sportovním segmentu se setkáte i s číselnou stupnicí 6 až 9.</p>'
          + T(['Obvod dlaně', 'Velikost v palcích', 'Orientační označení'], [
              ['do 17 cm', '6,5', 'XS'],
              ['17 až 18 cm', '7', 'S'],
              ['18 až 19 cm', '7,5–8', 'M'],
              ['19 až 21 cm', '8,5–9', 'L'],
              ['nad 21 cm', '9,5 a víc', 'XL']]) +
          '<p>Tabulka je jen pomůcka, protože každá značka má vlastní střih. Při nákupu na dálku se řiďte tabulkou konkrétního výrobce a při pochybnostech vyberte větší velikost, pokud plánujete tenkou vložku. Správná rukavice nesmí tlačit v dlani, ale ani vytvářet záhyby v prstech. Měkká dlaň s volným prostorem pro prsty je teplejší než těsná, protože uvnitř zůstává vrstva vzduchu.</p>'
          '<h2>Prsty, nebo palčáky</h2>'
          '<p>Prstové rukavice nabízejí cit a přesnost, palčáky teplo. Když prsty leží vedle sebe, ohřívají se navzájem, a proto jsou palčáky při stejném materiálu výrazně teplejší. Volba tedy záleží na tom, co potřebujete dělat. Lyžařky s citlivými prsty často vybírají palčáky nebo kombinaci, kdy v palčáku sedí tenká prstová rukavice. Při fotografování nebo práci s telefonem se hodí tenký model s dotykovou špičkou.</p>'
          '<ul><li><strong>Palčáky:</strong> nejlepší izolace, hodí se na lyže při mrazu a pro děti, pro přesné ovládání je nevhodné.</li>'
          '<li><strong>Prstové rukavice:</strong> cit pro hole, zip, telefon, řídítka, jsou o něco chladnější.</li>'
          '<li><strong>Tříprstové (tzv. lobster):</strong> kompromis pro chladné dny na kole nebo při zimním běhu.</li></ul>'
          '<h2>Materiály: softshell, membrána, fleece, merino</h2>'
          + T(['Materiál', 'Silné stránky', 'Slabší stránky', 'Hodí se na'], [
              ['Softshell', 'pružný, prodyšný, odolný větru', 'při dlouhém dešti promoká', 'procházky, běh, kolo, podzimní lyžování'],
              ['Membrána (Gore-Tex, R-Tex a podobně)', 'nepropouští vodu, ale prodýchá', 'dražší, při nadměrném zahřátí se potí', 'lyže, mokrý sníh, sjezd'],
              ['Fleece', 'lehký, hřeje, měkký', 'nezastaví vítr ani vodu', 'vložky, procházky v suchu'],
              ['Merino', 'hřeje i vlhké, nezapáchá', 'méně odolné vůči oděru', 'tenké vložky, běh, běžky'],
              ['Kůže', 'odolná, dlouhá životnost', 'vyžaduje impregnaci a sušení', 'město, jízda, zimní lyžování']]) +
          '<p>Při výběru počítejte i s dlaní. Gumované nebo silikonové potisky zajišťují úchop, ale u lyžařských rukavic bývá dlaň vyztužená kůží nebo syntetikou proti oděru. U cyklistických rukavic je zase důležitá gelová výplň, která tlumí otřesy.</p>'
          '<h2>Rukavice podle sportu</h2>'
          '<h3>Lyže a snowboard</h3>'
          '<p>Základem je nepromokavý vrchní materiál, izolace a dlouhá manžeta, kterou lze zatáhnout přes rukáv bundy. Nejznámější značky v této oblasti jsou ' + B(('viking', 'Viking'), ('reusch', 'Reusch'), ('ziener', 'Ziener'), ('rossignol', 'Rossignol'), ('picture', 'Picture')) + '. Širší výběr najdete v <a href="/lyzarske-rukavice/">lyžařských rukavicích</a> a doplníte <a href="/lyzarske-cepice-a-nakrcniky/">čepicemi a nákrčníky</a>.</p>'
          '<h3>Běžky a běh</h3>'
          '<p>Při pohybu se ruce potí, proto jsou lepší tenké a prodyšné rukavice, ne tlusté zimní. Pro běžecké lyžování vyrábí řadu modelů například ' + B(('swix', 'Swix'), ('craft', 'Craft'), ('dynafit', 'Dynafit')) + '. Rozdíl od lyžařských rukavic spočívá v nižší izolaci, ale vyšší prodyšnosti a lepším citu pro hole. Informace o sportu najdete na stránce <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</p>'
          '<h3>Kolo a gravel</h3>'
          '<p>Cyklistické rukavice mají polstrovanou dlaň, pružný hřbet a krátké nebo dlouhé prsty podle sezóny. Značka ' + B(('silvini', 'Silvini')) + ' nabízí například gravelové modely. Pro zimu hledejte vítr odolný hřbet, pro léto prodyšnou síťovinu. Další modely jsou v <a href="/cyklisticke-rukavice/">cyklistických rukavicích</a>.</p>'
          '<h3>Město, turistika a volný čas</h3>'
          '<p>Na procházky a dojíždění stačí softshell nebo vlněná rukavice se dotykovými špičkami. Zajímavé jsou outdoorové značky jako ' + B(('the-north-face', 'The North Face'), ('columbia', 'Columbia'), ('hannah', 'Hannah'), ('loap', 'Loap'), ('trespass', 'Trespass'), ('meatfly', 'Meatfly'), ('barts', 'Barts')) + ' a sportovní jako ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('under-armour', 'Under Armour')) + '.</p>'
          '<h2>Fitness, box a brankářské rukavice</h2>'
          '<p>Kategorie Rukavice obsahuje i specializované modely. Boxerské rukavice jsou rozdělené podle váhy v uncích a vycházejí z hmotnosti hráče a typu tréninku. U <a href="/boxerske-rukavice/">boxerských</a> i <a href="/brankarske-rukavice/">brankářských rukavic</a> je klíčová velikost dlaně a ochrana kloubů. Fitness rukavice zlepšují úchop při cvičení s činkami a chrání před mozoly. Při výběru se řiďte tím, jak sport používáte, ne tím, zda je rukavice označená jako dámská.</p>'
          '<h2>Vrstvení a teplo rukou</h2>'
          '<p>Ruce chladnou rychle, protože mají velký povrch vzhledem k objemu a málo svalů. Proto se vyplatí kombinovat tenkou vložku z merina nebo fleecu s vrchní rukavicí. Vložka se dá nosit sama v mírném počasí a navíc odvádí vlhkost od kůže. Pokud vám v rukavicích přesto mrznou prsty, zkontrolujte, jestli nejsou příliš těsné a jestli manžeta těsní proti větru. Zahřívat se dá i správným oblečením trupu, protože při chladném těle organismus omezuje prokrvení rukou.</p>'
          '<p>Ke kompletu se hodí <a href="/zimni-bundy/">zimní bundy</a> a <a href="/merino-ponozky/">merino ponožky</a>. Při výběru barvy pamatujte na to, že světlé rukavice se špiní, ale na horách jsou lépe vidět. Dámské modely se často nabízejí ve více barvách než unisex řady.</p>'
          '<h2>Péče o rukavice</h2>'
          '<p>Mokré rukavice sušte při pokojové teplotě, nikdy ne na topení ani v troubě. Rukavice obrácené naruby se suší rychleji a nezačnou páchnout. Membránové rukavice po sezóně vyperte jemným prostředkem bez aviváže a obnovte impregnaci. Kožené ošetřete vhodným tukem. Pokud zip nebo suchý zip ztrácí sílu, vyčistěte ho kartáčkem. Rukavice vždy skladujte suché, jinak se v nich rozmnožují bakterie.</p>'
          '<h2>Na co si dát pozor při výběru</h2>'
          '<p>Před koupí si ujasněte, kde budete rukavice nosit nejčastěji, protože univerzální model neexistuje. Rukavice na lyže bývá příliš hrubá na telefon a lehká běžecká nepřežije mráz. Čtěte popis: zajímá vás materiál vrchní vrstvy, izolace, typ manžety a údaj o membráně. Vyhněte se nabídkám bez uvedení velikostní tabulky, protože označení S a M mají každý výrobce jiné.</p>'
          '<ul><li><strong>Manžeta:</strong> dlouhá pod bundu na lyže, krátká na běh a kolo.</li>'
          '<li><strong>Zesílená dlaň:</strong> prodlužuje životnost při držení holí a řídítek.</li>'
          '<li><strong>Poutko nebo karabinka:</strong> rukavice se neztratí a dají se spojit.</li>'
          '<li><strong>Reflexní prvky:</strong> užitečné při jízdě a běhu za šera.</li></ul>'
          '<p>Hledáte-li něco výraznějšího, projděte <a href="/u-zlate-rukavice/">zlaté rukavice</a>. Dětské velikosti hledejte spíš u <a href="/reima-rukavice/">značky Reima</a>, která se na dětské zimní oblečení specializuje.</p>'
          '<h2>Dárek a výběr v nejistotě</h2>'
          '<p>Rukavice jsou častý dárek, ale velikost se špatně hádá. Nejbezpečnější je zjistit obvod dlaně nebo půjčit rukavici, kterou dotyčná nosí. Pokud nevíte, zvolte pružnější materiál, který se přizpůsobí, a model s možností výměny velikosti u prodejce.</p>'
          '<h2>Rukavice a ostatní vybavení</h2>'
          '<p>Rukavice nikdy neladí samy o sobě. Na lyžích je ocení spolu s kvalitní bundou, kde manžeta rukavice zapadne pod rukáv nebo přes něj, podle střihu. Při běhu v zimě rukavice dobře doplní čelenka nebo čepice, protože hlava a ruce jsou místa, kde se pocit chladu projevuje první. Pro cyklistku je důležité, aby rukavice nebránila ovládání brzd a řazení, a proto zkoušejte, zda prsty dosáhnou na páčky. Ve městě nakonec rozhoduje pohodlí a barva, která ladí k bundě a šále.</p>',
    faq=[
        ('Jak změřit velikost dámských rukavic?', 'Změřte obvod otevřené dlaně těsně pod klouby, bez palce, v centimetrech. Číslo vydělte 2,54 a získáte velikost v palcích. Poté porovnejte s tabulkou výrobce, protože střihy se liší. Při nejistotě vyberte větší velikost.'),
        ('Je lepší koupit palčáky, nebo prsty?', 'Palčáky jsou teplejší, protože prsty se navzájem ohřívají. Prstové rukavice dávají cit a přesnost. Pro lyže při mrazu zvolte palčáky, pro běh, kolo a práci s telefonem prstové modely.'),
        ('Čím se liší dámská rukavice od pánské?', 'Má užší dlaň, kratší prsty a menší obvod zápěstí. Díky tomu lépe sedí na drobnější ruce, nezvrásňuje se a lépe izoluje. U unisex modelů je rozdíl menší, ale ženám sedí obvykle nižší velikostní řady.'),
        ('Jak poznám, že je rukavice nepromokavá?', 'Hledejte označení membrány (například Gore-Tex nebo R-Tex) a zalepené švy. Softshell odolá lehkému dešti, ale při déle trvajícím mokru promokne. Pro mokrý sníh vždy volte membránu.'),
        ('Proč mi v rukavicích mrznou prsty?', 'Příčinou bývá příliš těsný střih, který zhoršuje prokrvení, nebo nedostatečná izolace. Zkuste větší velikost s tenkou vložkou a zkontrolujte manžetu. Pomáhá také oblečení trupu, protože chladné tělo omezuje prokrvení rukou.'),
        ('Jaké rukavice zvolit na běh?', 'Tenké a prodyšné, ze softshellu nebo elastické pleteniny. Silné zimní se při pohybu přehřívají. Na mrazivé ráno se hodí vrstvení: vložka z merina a při zastavení vrchní rukavice.'),
        ('Fungují dotykové špičky spolehlivě?', 'Fungují, pokud jsou prsty z vodivé tkaniny a rukavice sedí těsně. Při silné vrstvě nebo v mokru reagují hůř. Pro sport s telefonem v kapse je užitečné, ale nenahrazuje kvalitní izolaci.'),
        ('Jak prát rukavice?', 'Textilní a membránové rukavice perte ručně v jemném prostředku bez aviváže a nechte je uschnout při pokojové teplotě. Kožené jen otřete vlhkým hadříkem a ošetřete tukem. Při praní v pračce hrozí poškození membrány a lepených švů.'),
        ('Kdy rukavice vyměnit?', 'Když se prodřela dlaň, uvolnily se švy nebo membrána začala propouštět vodu. Rukavice s opotřebovanou izolací už nehřeje. Opravit lze drobnou trhlinu, ale u staré membrány se oprava nevyplatí.'),
        ('Mohu použít dětské rukavice, pokud mám malou ruku?', 'Dá se to, pokud sedí obvod dlaně a délka prstů. Dětské modely mají ale často jiné střihy a méně izolace. Pro ženy s velmi malou rukou jsou obvykle lepší dámské velikosti XS a S.'),
    ])

# ------------------------------------------------------------------ salomon-bezecke-boty
NEW['salomon-bezecke-boty'] = dict(
    title='Salomon běžecké boty: Speedcross, XA Pro, Ultra Glide',
    desc='Salomon běžecké boty: trailové Speedcross a XA Pro 3D, tlumené Ultra Glide a Sense Ride, silniční Aero Glide a gravel Aero Blaze. Jak vybrat podle terénu.',
    intro='<p>Salomon je francouzská značka z Alp, která se proslavila lyžařským vybavením a později se stala jedním z nejznámějších výrobců trailové obuvi. V nabídce běžeckých bot se opakují názvy jako Speedcross, XA Pro 3D, Ultra Glide, Sense Ride nebo Aero Glide a každý míří na jiný terén. '
          'Na této stránce jsou běžecké boty značky z kategorie <a href="/bezecka-obuv/">běžecké boty</a>, a to jak pánské, tak dámské modely. Průvodce vysvětluje, v čem se jednotlivé řady liší, jak se orientovat v označení GTX a Wide, jak sedí střih a pro koho se jednotlivé modely hodí. Pro srovnání s dalšími výrobci slouží přehledy <a href="/adidas-bezecke-boty/">Adidas</a>, <a href="/nike-bezecke-boty/">Nike</a> a <a href="/bezecke-boty-hoka/">Hoka</a>.</p>',
    guide='<h2>Salomon a trailový běh</h2>'
          '<p>Značka vyrábí především obuv určenou do terénu, a proto je její nabídka vlastně opakem klasických silničních běžeckých bot. Základem je podrážka s výrazným dezénem, pevné zpevnění špičky a patní části a systém rychlého šněrování. Silniční řada je užší, ale Salomon do ní promítá stejný přístup: spíš pevnější a přilnavější než extrémně měkká. Kdo hledá nejtlumenější botu na asfalt, najde širší výběr jinde, kdo běhá po loukách, lesních cestách a v horách, bude s touto značkou spokojený.</p>'
          + T(['Řada', 'Terén', 'Charakter'], [
              ['Speedcross', 'bláto, měkká půda, mokrá tráva, sníh', 'agresivní hluboký dezén, pevné držení paty, užší střih'],
              ['XA Pro 3D', 'smíšený terén, lesní stezky, kamenité cesty', 'stabilní a odolná bota na delší túry i běh'],
              ['Sense Ride', 'kamenité a suché stezky, delší tratě', 'tlumenější bota s pohodlným chodem'],
              ['Ultra Glide', 'ultra tratě, delší vzdálenosti, měkčí povrchy', 'zaměřeno na tlumení a pohodlí'],
              ['Aero Glide, Pulsar, Genesi', 'silnice a zpevněné cesty, rychlejší běh', 'lehčí a pružnější model pro rychlejší tempo'],
              ['Aero Blaze, Aero Glide GRV', 'gravel a polní cesty', 'kombinace silničního a terénního profilu']]) +
          '<p>Takto stručné shrnutí slouží jen jako orientace. V praxi se model liší verzí a ročníkem, a proto u každé konkrétní nabídky sledujte popis, hmotnost, typ dezénu a údaj o tlumení. Před nákupem také zkontrolujte, zda jde o pánskou, dámskou nebo unisex verzi.</p>'
          '<h2>Speedcross: agresivní dezén do bláta</h2>'
          '<p>Speedcross patří k nejznámějším botám značky. Má hluboké kolíky v podrážce, které se zakusují do měkké půdy a mokrého sněhu. Na tvrdém asfaltu nebo na hladkých kamenech je takový dezén zbytečný a rychle se opotřebuje. Boty sedí poměrně těsně kolem paty a středu chodidla, což pomáhá při klesání. V nabídce existuje také široká verze Wide, která je určená pro nohy s širším předonožím. Pokud máte širší chodidlo, zkuste ji, protože úzká bota tlačí na malíku a při delším běhu způsobuje puchýře.</p>'
          '<h2>XA Pro 3D a univerzální použití</h2>'
          '<p>XA Pro 3D je bota pro hráče všestranného terénu. Dezén je mělčí než u Speedcross, takže funguje i na zpevněných cestách. Často se vyskytuje ve verzi s membránou Gore-Tex (GTX), která chrání před vodou, ale zhoršuje prodyšnost. Pro zimní běhání je to výhoda, v létě může být nohám horko. Pokud neběháte v dešti a bahnu, volte verzi bez membrány a nechte vodu odtéct.</p>'
          '<ul><li><strong>Verze s GTX:</strong> pro chladné a mokré dny, brod a sníh, zhorší se prodyšnost.</li>'
          '<li><strong>Verze bez membrány:</strong> lépe odvádí pot a rychleji schne po zaplavení.</li>'
          '<li><strong>Ponožky:</strong> při membránové botě volte tenčí, jinak se noha přehřívá.</li></ul>'
          '<h2>Tlumené boty: Ultra Glide a Sense Ride</h2>'
          '<p>Při delších trasách je důležitější pohodlí než nejnižší hmotnost. Ultra Glide a Sense Ride patří mezi tlumenější modely, které zmírňují nárazy při dlouhém běhu a klesání. Podrážka s vyšší vrstvou pěny zpravidla vyžaduje stabilní krok, protože na nerovných kamenech je bota vyšší od země a hůře ji cítíte. Pro běžce, kteří jedou ultra tratě nebo mají tendenci k bolestem kloubů, je to rozumná volba. Rychlí běžci na krátkých tratích si naopak oblíbí lehčí boty s nižším profilem.</p>'
          '<h2>Silniční a gravelové modely</h2>'
          '<p>Salomon nabízí i boty na silnici a zpevněné cesty. Řady Aero Glide, Pulsar a Genesi se obvykle hodí pro rovný povrch a rychlejší tempo, zatímco Aero Blaze a modely s označením GRV nebo GRVL míří na gravel, tedy nezpevněné cesty. Tyto boty mají podrážku, která se snáší s drobným štěrkem a nese svou váhu bez nadměrného dezénu. Kdo běhá převážně po silnici, najde širší přehled v kategorii <a href="/silnicni-bezecke-boty/">silniční běžecké boty</a>, pro terén slouží <a href="/trailove-boty/">trailové boty</a>.</p>'
          '<h2>Jak sedí Salomon a jak vybrat velikost</h2>'
          '<p>Většina bot značky má poměrně úzký střih, pevné držení paty a zpevněnou špičku. Pokud máte široké předonoží, zkuste verze Wide nebo vyberte o půl čísla větší velikost. Při běhu se noha zvětšuje a při klesání sjíždí dopředu, takže před špičkou ponechte rezervu šířky palce. Obuv zkoušejte odpoledne a se ponožkou, kterou při běhu používáte.</p>'
          '<ul><li><strong>Pata:</strong> nesmí při chůzi a běhu vyskakovat, jinak vznikají puchýře.</li>'
          '<li><strong>Špička:</strong> prsty se nesmí dotýkat špičky při klesání.</li>'
          '<li><strong>Šněrování:</strong> rychlé šněrování se dotahuje jedním tahem, ale ověřte, že tlak nevytváří na nártu bolest.</li>'
          '<li><strong>Dámský střih:</strong> bývá užší v patě a ve středu chodidla, v nabídce poznáte označení W.</li></ul>'
          '<p>Pro srovnání střihů se podívejte na další značky v kategorii, například ' + B(('hoka', 'Hoka'), ('on', 'On'), ('altra', 'Altra'), ('new-balance', 'New Balance'), ('asics', 'Asics'), ('mizuno', 'Mizuno')) + '. Altra má širší prostor pro prsty, Hoka vyšší tlumení a On pevnější podrážku, takže široké noze může víc sednout jiná značka.</p>'
          '<h2>Dámské, pánské a dětské modely</h2>'
          '<p>Značka nabízí ženskou řadu pod označením W. Je užší, lehčí a nastavená na ženskou nohu. Stejné modely se prodávají v pánské a dámské verzi a často se liší jen barvou a šířkou. Ženy s širším chodidlem tak mohou sáhnout po pánské nebo unisex verzi. Pro srovnání otevřete <a href="/bezecke-boty-damske/">dámské běžecké boty</a>, a pro děti <a href="/detske-bezecke-boty/">dětské běžecké boty</a>. Značku najdete také v lyžařském výběru <a href="/salomon-lyzarske-boty/">Salomon lyžařské boty</a>.</p>'
          '<h2>Doplňky k běhu</h2>'
          '<p>K terénnímu běhu patří <a href="/bezecke-vesty-a-batohy/">běžecká vesta</a> na pití a výbavu, <a href="/bezecke-opasky/">běžecký opasek</a> a funkční <a href="/sportovni-ponozky/">sportovní ponožky</a>. Přehled všech disciplín je na stránce <a href="/beh/">běh</a>. Při delších trasách s sebou vezměte lehkou nepromokavou bundu a hlavně vodu.</p>'
          '<h2>Péče o trailové boty</h2>'
          '<p>Po běhu v bahnu bláto smyjte vodou a kartáčkem a boty nechte uschnout při pokojové teplotě. Na topení se lepené spoje uvolňují a pěna ztrácí tvar. Z membrány vytáhněte vložku, aby uschla zvlášť. Šněrování zkontrolujte, protože rychlé šněrování se po čase uvolňuje nebo zaplňuje bahnem. Jakmile dezén ztrácí hloubku, snižuje se přilnavost a bota je vhodná už jen na silnici.</p>'
          '<h2>Počasí a roční období</h2>'
          '<p>V létě se nejlépe osvědčují prodyšné boty bez membrány, které rychle schnou po brodu. Na podzim a na jaře, kdy je půda rozmáčená, uplatníte Speedcross nebo model s membránou. V zimě se hodí vyšší nebo zateplené modely, případně návleky proti sněhu. Pamatujte, že žádná membránová bota nepřežije vodu přelitou přes okraj, a pak uvnitř zůstává vlhko. Stačí proto tenká ponožka a lehká bota, která rychle schne.</p>'
          '<h2>Kdy boty vyměnit a jak je střídat</h2>'
          '<p>Běžecká bota ztrácí tlumení dřív, než je vidět na vnějšku. Pokud po běhu pociťujete bolest v kolenou nebo chodidle, kterou jste dřív neměli, může být pěna vyčerpaná. Střídání dvou párů prodlužuje životnost obou a umožňuje obuvi vyschnout. Kdo běhá po silnici i v terénu, ušetří trailové boty tím, že na asfalt obuje druhý pár. Nová bota se rozbíhá postupně, nejdřív na kratších trasách. Při přechodu z jiné značky počítejte s tím, že rozdíl v tlumení a v pevnosti paty si noha musí zvyknout, a proto první týdny nepřehánějte délku výběhů.</p>',
    faq=[
        ('Jakou řadu Salomon zvolit na blátivý terén?', 'Speedcross, protože má hluboký agresivní dezén, který se zakusuje do měkké půdy a mokrého sněhu. Na zpevněných cestách se rychle opotřebuje a je tam zbytečný. Při širší noze zvolte verzi Wide.'),
        ('Je XA Pro 3D vhodná i na silnici?', 'Na krátký asfaltový úsek mezi stezkami ano, ale není na ni optimalizovaná. Dezén se na tvrdém povrchu opotřebovává a bota je tužší než silniční modely. Na delší běh po silnici zvolte Aero Glide nebo jiný silniční model.'),
        ('Co znamená GTX v názvu?', 'Označení GTX značí membránu Gore-Tex, která chrání před vodou. Zhoršuje ale prodyšnost, takže se hodí do chladného a mokrého počasí. V létě volte verzi bez membrány, která lépe odvádí pot.'),
        ('Jsou Salomon boty úzké?', 'Většina modelů má poměrně úzký střih s pevným držením paty. Pro širší chodidlo existují verze Wide nebo můžete vybrat o půl čísla větší velikost. Před koupí vždy ověřte šířku předonoží.'),
        ('Jak vybrat velikost běžecké boty?', 'Ponechte před palcem rezervu zhruba šířky palce, aby se nezarážel při klesání. Zkoušejte odpoledne a v ponožce, kterou při běhu používáte. Pata nesmí vyskakovat a bota nemá tlačit na bocích.'),
        ('Co je rychlé šněrování?', 'Je to systém s tenkou šňůrkou, která se dotahuje jedním tahem a zajišťuje se zámkem. Ušetří čas a šněrování se neuvolňuje. Při závodech a běhu v bahně ale dohlédněte, aby se šňůrka nezanesla.'),
        ('Hodí se Ultra Glide na delší trasy?', 'Ano, patří mezi tlumenější modely a je navržená pro delší vzdálenosti. Vyšší podrážka tlumí nárazy, ale hůře cítíte nerovnosti. Pro krátké závody nebo techničtější kamenitý terén se hodí spíš nižší bota.'),
        ('Čím se liší gravelové modely Aero Blaze?', 'Mají podrážku určenou pro štěrkové a polní cesty s mírným dezénem. Jsou ideální, pokud střídáte silnici a nezpevněný povrch. Pro bahnitý terén zvolte raději Speedcross.'),
        ('Jak dlouho vydrží trailové boty?', 'Záleží na terénu, váze a stylu běhu. Pěna v podrážce ztrácí tlumení dřív než dezén. Pokud boty přestanou tlumit nebo dezén zmizí, je čas na výměnu, jinak se zvyšuje riziko zranění.'),
        ('Mohu v trailových botách běhat po asfaltu?', 'Můžete, ale dezén se rychle opotřebuje a tvrdý povrch je méně pohodlný. Pro pravidelný běh po silnici je lepší pořídit zvlášť silniční boty a trailové si ponechat do terénu.'),
    ])
