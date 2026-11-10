"""sporteka.cz — facet landing texts wave 108: bauer-hokejky, kolobezka-kostka, trampolina-marimex, jordan-teplaky.
General true facts only, no prices or counts. Brands and models verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ bauer-hokejky
NEW['bauer-hokejky'] = dict(
    title='Bauer hokejky: řady, flex, zakřivení a velikosti',
    desc='Bauer hokejky pro seniory, juniory i nejmenší hráče. Jak se orientovat v řadách Vapor, Nexus a Proto, v tuhosti, levé a pravé čepeli a patternech.',
    intro='<p>Bauer je jedna z nejrozšířenějších kanadských hokejových značek a v kategorii <a href="/hokejky/">hokejek</a> má nejširší zastoupení ze všech výrobců. Právě proto se v nabídce snadno ztratíte: stejná řada se objevuje ve čtyřech velikostních skupinách, ve dvou stranách čepele, v několika zakřiveních a každý rok v nové sezónní verzi. '
          'Na této stránce jsou hole značky Bauer od dětských modelů pro nejmenší po senior kompozity pro dospělé. Průvodce vysvětluje, jak číst názvy typu Vapor FlyPro S25 Grip Sr, co znamená číslo za velikostí hráče, kdy dává smysl starší ročník a jak Bauer vychází v porovnání s hokejkami <a href="/ccm-hokejky/">CCM</a>, <a href="/hokejka-warrior/">Warrior</a> nebo <a href="/fischer-hokejka/">Fischer</a>. Pro nejmladší hráče se hodí i samostatný výběr <a href="/detska-hokejka/">dětských hokejek</a>.</p>',
    guide='<h2>Jak číst název hokejky Bauer</h2>'
          '<p>Názvy Bauer hokejek se skládají z několika vrstev a každá z nich něco říká. Vezměte si ukázku „Vapor FlyPro S25 Grip Sr, 70, R, P92“. První část je jméno řady, tedy konstrukční koncepce. Označení S25 je sezónní ročník, v němž byla řada uvedena. Slovo Grip znamená, že násada má povrchovou úpravu pro jistější držení. Zkratka Sr určuje velikostní skupinu, číslo tuhost, písmeno L nebo R stranu čepele a kód typu P92 tvar zakřivení čepele.</p>'
          + T(['Část názvu', 'Význam', 'Na co si dát pozor'], [
              ['Vapor, Nexus, Proto, Pulse, Elite, X Series', 'řada neboli konstrukční koncepce', 'řady se po sezónách přejmenovávají a vylepšují, srovnávejte podle popisu'],
              ['S23, S24, S25', 'ročník řady', 'starší ročník bývá výhodnější, rozdíly jsou většinou v detailech'],
              ['Grip', 'upravený povrch násady', 'u modelu bez úpravy se hodí páska na horní konec'],
              ['Sr, Int, Jr, Yth, Tyke', 'velikostní skupina podle věku a výšky', 'viz tabulka níže'],
              ['Číslo (např. 40, 65, 87)', 'tuhost neboli flex', 'čím větší číslo, tím tužší hůl'],
              ['L nebo R', 'strana čepele podle držení hole', 'záměna strany je nejčastější chyba'],
              ['P92, P28, P90T', 'typ zakřivení a sklonu čepele', 'kódy jsou specifické pro Bauer, ověřte je v popisu']]) +
          '<h2>Řady Bauer v nabídce a komu se hodí</h2>'
          '<p>V katalogu se objevují řady Vapor (modely FlyPro a HyperLite 2), Nexus (Tracer a Performance), Proto (Proto R a Proto2), Pulse, Elite a X Series. Výrobce je dlouhodobě rozděluje do výkonnostní škály od lehkých špičkových kompozitů až po robustní vstupní hole. Přesné parametry se u konkrétního ročníku liší, proto se řiďte popisem u produktu. Obecně lze říct, že řada Vapor je dlouhodobě spojována s lehkou konstrukcí pro hráče, kteří chtějí rychlý odpich. Řady Nexus a Pulse bývají volbou pro pravidelné trénování bez nároků na špičkový výkon, zatímco modely označené X Series a Proto2 jsou častou volbou pro mladší hráče a juniory, kteří rostou a hůl často mění.</p>'
          '<p>Zvláštním případem je model Bauer X Pastrňák. Jméno odkazuje na českého hokejistu Davida Pastrňáka, který hraje v NHL, a edice je v nabídce především ve velikostech pro juniory a intermediate. Pro mladého hráče je to často motivační volba, ale funkčně se posuzuje stejně jako každá jiná hůl: podle délky, tuhosti a zakřivení, ne podle jména na násadě.</p>'
          '<h2>Velikostní skupiny a tuhost u Bauer</h2>'
          '<p>Bauer označuje velikost hole podle věkové skupiny a každá skupina má svůj typický rozsah tuhosti. V katalogu odpovídají přibližně těmto hodnotám:</p>'
          + T(['Skupina', 'Označení', 'Typický rozsah tuhosti v nabídce', 'Pro koho'], [
              ['Senior', 'Sr', 'od 65 do 87', 'dospělí a vzrostlí dorostenci'],
              ['Intermediate', 'Int', 'od 55 do 65', 'starší žáci a mladší dorostenci'],
              ['Junior', 'Jr', 'od 30 do 50', 'mladší a starší žáci'],
              ['Youth', 'Yth', 'kolem 20', 'děti ve školním věku, začátečníci'],
              ['Tyke', 'Tyke', 'kolem 10', 'nejmenší děti, první hodiny na ledě']]) +
          '<p>Délka hole roste spolu se skupinou. U nejmenších modelů uvádí název hodnotu ve čtyřiceti dvou palcích, u skupiny Youth ve čtyřiceti šesti a u skupiny Junior kolem padesáti dvou palců. Při výběru nejprve určete skupinu podle výšky a teprve potom ladíte tuhost. Dítě, které je vyšší než vrstevníci, patří do větší skupiny, ale s měkčím flexem, než by odpovídal jeho věku. Podrobný postup měření a doporučení tuhosti najdete v textu o <a href="/hokejky/">hokejkách</a>, zde se zaměřte jen na to, jak jednotlivé skupiny sedí u Bauer.</p>'
          '<h2>Levá, pravá a zakřivení čepele</h2>'
          '<p>Písmeno L znamená, že hráč drží hůl levou rukou níž na násadě a střílí zleva. Písmeno R platí pro opak. Jak se rozhodnout, když nevíte, kterou stranu máte? Postavte se s hokejkou, kterou máte doma, nebo s kartáčem na zametání a uvidíte, která ruka jde přirozeně dolů. Většina hráčů u nás střílí zleva, ale nabídka pravých holí je široká a rozdíl v cenách mezi stranami není. Dětem nechte volbu na zkoušení bez tlaku, protože strana se dá změnit mnohem snáz, než se přeučí technika.</p>'
          '<p>Zakřivení čepele označuje Bauer kódy typu P92, P28 nebo P90T. Kód popisuje, v jakém místě čepele je křivka nejhlubší, jak moc je čepel otevřená a jaký je její úhel k ledu. Čepel s křivkou blíž špičce se hodí hráčům, kteří rádi zdvihají puk, prostřední křivka je univerzální, zatímco rovnější čepel dává lepší jistotu při přihrávkách a práci s pukem na forhendu. Nejlepší cesta k volbě je vyzkoušet několik zakřivení u spoluhráčů nebo v obchodě a vybrat to, se kterým puk drží nejjistěji.</p>'
          '<h2>Starší ročník, nebo nejnovější série</h2>'
          '<p>Hole Bauer se u nás prodávají ve více ročnících najednou. V nabídce jsou vedle sebe ročníky S23, S24 a S25, a rozdíl je občas zásadní, jindy téměř nepatrný. Starší ročník má smysl hlavně tehdy, když kupujete pro juniora, který z hole za sezónu vyroste, nebo když potřebujete rezervní kus. Pro dospělého hráče, který hraje pravidelně a hůl používá několik sezón, se naopak vyplatí vyšší řada, i když je nejnovější ročník dražší.</p>'
          '<ul><li><strong>Porovnávejte stejnou velikost a tuhost:</strong> senior s tuhostí 70 a senior s tuhostí 77 se chovají zcela jinak.</li>'
          '<li><strong>Ověřte skladovost strany a zakřivení:</strong> u nižších řad se obchody často liší tím, které varianty drží.</li>'
          '<li><strong>Počítejte s duplicitami:</strong> stejný model se v přehledu opakuje v několika délkách a stranách čepele, proto otevřete přesně tu variantu, kterou potřebujete.</li>'
          '<li><strong>Nekupujte na vyrůstání:</strong> příliš dlouhá hůl učí špatné držení těla.</li></ul>'
          '<h2>Bauer a další značky hokejek</h2>'
          '<p>Hokejky se nejčastěji porovnávají mezi několika výrobci, kteří mají v kategorii významný podíl. Vedle Bauer jsou to ' + B(('winnwell', 'Winnwell'), ('ccm', 'CCM'), ('sherwood', 'Sherwood'), ('warrior', 'Warrior'), ('fischer', 'Fischer')) + '. Bauer a CCM patří k nejvíce zastoupeným kanadským značkám a konkurují si v celé škále od vstupních po špičkové. Winnwell se v nabídce soustředí především na hole pro začátečníky a týmy. Warrior je spojován spíš s výkonnostním sortimentem a Fischer je rakouská značka, která vedle hokeje vyrábí i lyžařské vybavení. U všech platí totéž: nekupujte značku, ale tuhost, délku a zakřivení.</p>'
          '<h2>Péče o kompozitní hokejku</h2>'
          '<p>Kompozitní hůl je lehká, ale citlivější na nárazy než dřevo. Největší riziko představuje náraz do hrany branky, šlápnutí na hůl nebo tlak v dopravě v zavazadle. Při větších nárazech vznikají vlásečnicové praskliny, které hůl při dalším výstřelu zlomí. Jak ji udržet delší dobu:</p>'
          '<ul><li>Po tréninku čepel osušte, protože vlhká páska bobtná a pod ní se čepel postupně kazí.</li>'
          '<li>Hůl při přepravě nezatěžujte jinými předměty a neukládejte ji u topení.</li>'
          '<li>Zkontrolujte povrch v okolí spoje čepele a násady, kde praskliny vznikají nejčastěji.</li>'
          '<li>Při zlomení nebo odřené čepeli zvažte výměnu čepele u dvoudílné hole, nové čepele najdete v kategorii <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>.</li></ul>'
          '<p>K hokejce patří také <a href="/hokejove-pasky-a-doplnky/">hokejové pásky a doplňky</a>, ochrana v podobě <a href="/hokejove-chranice/">chráničů</a> a <a href="/hokejove-helmy-a-mrizky/">helmy s mřížkou</a>. Hráči, kteří začínají od základů, najdou souhrn v hlavní kategorii <a href="/hokej/">hokej</a>, kde jsou i <a href="/hokejove-brusle/">brusle</a>.</p>',
    faq=[
        ('Jaké hokejky Bauer mají v nabídce hráči pro začátek?', 'Pro nejmenší jsou určeny skupiny Tyke a Youth s nízkou tuhostí a krátkou délkou. Hráči od školního věku se pak posouvají do skupiny Junior. Při prvních hodinách na ledě nemá smysl platit za lehkou kompozitní konstrukci, protože se hůl často upustí a dítě z ní rychle vyroste.'),
        ('Co znamená označení Sr, Int, Jr a Yth u hokejky Bauer?', 'Jsou to velikostní skupiny podle věku a výšky. Sr znamená senior, tedy dospělé hráče, Int intermediate, Jr junior a Yth youth. Ke skupině patří typická délka násady a rozsah tuhosti, takže hůl z vyšší skupiny je delší a tužší.'),
        ('Jaké číslo za velikostí hole je tuhost a jak ji vybrat?', 'Číslo je flex, tedy tuhost násady. Čím vyšší hodnota, tím tužší hůl. U dospělých se obvykle volí hodnota odpovídající zhruba polovině tělesné hmotnosti a děti potřebují hole měkčí. Nejjistější je vyzkoušet střelu na suchu nebo se řídit radou trenéra.'),
        ('Jak poznám, jestli potřebuji levou, nebo pravou hokejku?', 'Levá hůl je pro hráče, který drží hůl levou rukou níž na násadě. U pravé je to naopak. Pokud si nejste jistí, vyzkoušejte zametání nebo držení hole na suchu a sledujte, která ruka se přirozeně ocitne dole. Správná strana se pozná i podle toho, že se hráč nemusí naklánět.'),
        ('Co znamenají kódy P92, P28 a P90T?', 'Jde o zakřivení a sklon čepele. Liší se místem nejhlubší křivky, otevřeností čepele a úhlem k ledu. Hráči, kteří hodně zdvihají puk, tíhnou ke křivce blíž špičce, univerzální je střední zakřivení. Nejlepší je zkusit víc variant a podle pocitu zvolit stejný kód i u dalších hokejek.'),
        ('Je lepší koupit starší ročník, nebo nejnovější sérii?', 'Rozdíly mezi sousedními ročníky bývají v detailech, jako je povrch, vyvážení nebo drobné změny materiálu. Pro rostoucí děti a rezervní hole je starší ročník rozumná volba. Pro dospělého hráče, který hraje pravidelně, má smysl investovat do vyšší řady bez ohledu na ročník.'),
        ('Co je Grip a potřebuji ještě hokejovou pásku?', 'Grip je speciální povrchová úprava násady, která zlepšuje držení bez nutnosti omotávat celý horní konec. Většina hráčů přesto přidá pásku na knauf, tedy na horní konec, aby ruka neklouzala. Páska na čepeli zůstává nezbytná u všech typů holí.'),
        ('Čím se liší hokejka Bauer od CCM a ostatních značek?', 'Bauer i CCM pokrývají celou škálu od vstupních po výkonnostní kusy a rozdíl je spíše v zakřivení, vyvážení a pocitu při střele než v kvalitě. Winnwell se zaměřuje především na začátečníky a týmy, Warrior na výkon a Fischer je evropská alternativa. Kupujte podle parametrů a ne podle loga.'),
        ('Dá se kompozitní hokejka zkrátit?', 'Dá, ale zkracování mění tuhost. Kratší hůl je tužší, takže hráč, který chce zkrátit o několik centimetrů, by měl zvolit měkčí hodnotu flexu, než odpovídá jeho váze. U dětských holí je lepší vybrat správnou velikost, než zkracovat příliš dlouhý kus.'),
        ('Pro koho je hokejka Bauer X Pastrňák?', 'Edice nese jméno českého hokejisty a je v nabídce hlavně pro juniory a intermediate. Funkčně je to běžná hůl příslušné skupiny, takže ji posuzujte podle délky, tuhosti, strany a zakřivení. Pro mladého fanouška je ale často silnou motivací trénovat.'),
    ],
)

# ------------------------------------------------------------------ kolobezka-kostka
NEW['kolobezka-kostka'] = dict(
    title='Koloběžka Kostka: modely Tour, Twenty, Hill a Street',
    desc='Koloběžky Kostka pro děti i dospělé: rozdíl mezi řadami Tour, Twenty, Hill a Street, generace G5 a G6, skládací modely, velikost a doplňky.',
    intro='<p>Kostka je česká značka koloběžek, která se zaměřuje na velká kola, pohodlné řízení a jízdu na delší vzdálenosti. Nejde o triky ve skateparku ani o lehké městské skládačky, ale o koloběžky pro rodinné vyjížďky, cestu do školy a pravidelnou pohybovou aktivitu. V kategorii <a href="/kolobezky/">koloběžek</a> mají vlastní jména jednotlivých řad, a právě v nich se nejlépe vyznat. '
          'Na této stránce najdete koloběžky Kostka od dětských variant Kid po modely pro dospělé a dospívající, včetně skládacích verzí a drobného příslušenství. Průvodce vysvětluje, co naznačují názvy Tour, Twenty, Hill, Street a Travel, jak pochopit označení G5 a G6, kdy zvolit dětský model a jak se Kostka liší od značek <a href="/kolobezka-yedoo/">Yedoo</a> a <a href="/kolobezka-micro/">Micro</a>. Pro nejmenší jezdce slouží také výběr <a href="/detska-kolobezka/">dětských koloběžek</a>.</p>',
    guide='<h2>Řady Kostka podle názvu</h2>'
          '<p>Kostka pojmenovává modely podle použití a doplňuje je velikostním nebo výkonnostním přívlastkem. V nabídce jsou řady Tour Max, Tour Fun, Twenty Max, Travel Max, Hill Fun a Street Fun, každá i ve verzi Kid pro děti, a několik skládacích modelů označených Fold. Přesné parametry u konkrétního kusu vždy ověřte v popisu, ale základní orientace podle názvu pomůže zúžit výběr.</p>'
          + T(['Řada', 'Co naznačuje název', 'Komu ji doporučit'], [
              ['Tour Max, Tour Fun', 'delší vyjížďky, silnější nebo pohodlnější varianta', 'dospívající a dospělí na rovné a polní cesty'],
              ['Twenty Max', 'koloběžka s většími koly pro dospělé', 'pravidelné jezdce, kteří chtějí rychlejší jízdu'],
              ['Travel Max', 'cestovní koloběžka', 'ti, kdo koloběžku převážejí nebo ji používají na výletech'],
              ['Hill Fun', 'řada pro nerovnější terén a svahy', 'rodiny, které jezdí po lesních a parkových cestách'],
              ['Street Fun', 'každodenní jízda po městě', 'děti a mladší dospívající'],
              ['Kid', 'dětská varianta příslušné řady', 'děti, kterým větší model ještě nesedí'],
              ['Fold', 'skládací konstrukce', 'ti, kdo koloběžku nosí do vlaku, auta nebo bytu']]) +
          '<p>Koloběžky Kostka jsou určené spíš k jízdě než k trikům, a proto s nimi nezkoušejte skatepark. Pro takové použití patří do výběru <a href="/freestyle-kolobezky/">freestyle koloběžky</a>. Pokud hledáte pomoc motoru na delších trasách, otevřete <a href="/elektrokolobezky/">elektrokoloběžky</a>.</p>'
          '<h2>Co znamená G5 a G6</h2>'
          '<p>U koloběžek Kostka se na konci názvu objevuje označení G5 nebo G6. Jde o generaci modelu, tedy o konstrukční ročník, v němž výrobce upravil rám, komponenty nebo detaily. Z hlediska výběru platí tři pravidla. Nejdřív porovnávejte vždy stejné generace, protože rozdíl se nejvíc projeví na lehčích dílech a řízení. Za druhé, starší generace může být ve slevě a pro dítě, které z koloběžky rychle vyroste, je rozumnou volbou. A za třetí se při opravách dívejte na označení generace, protože součástky nemusí být zaměnitelné mezi G5 a G6.</p>'
          '<h2>Velká kola a pohodlí na delších trasách</h2>'
          '<p>Základní rozdíl mezi koloběžkou Kostka a běžnou městskou koloběžkou je velikost kol. Větší průměr kol lépe překonává nerovnosti a po jednom odrazu dojede dál. Jízda je pak klidnější a méně namáhá zápěstí. Za tuto výhodu platí delším rozvorem a větší hmotností, takže koloběžka se hůř nosí po schodech. Pokud ji budete používat především na cesty po rovině, jde o dobrý kompromis. Pokud ji budete denně nosit do patra, zvažte skládací Fold.</p>'
          '<ul><li><strong>Nafukovací kola</strong> tlumí otřesy a hodí se na polní cesty, vyžadují ale občasné dofouknutí a kontrolu ventilku.</li>'
          '<li><strong>Brzda na řídítkách</strong> je pro delší jízdu důležitější než brzda na zadním blatníku, protože ji ovládáte bez ztráty rovnováhy.</li>'
          '<li><strong>Nastavení řídítek</strong> by mělo odpovídat výšce jezdce, aby pracoval s rovnými zády a lehce pokrčenými lokty.</li>'
          '<li><strong>Nosnost a hmotnost koloběžky</strong> ověřte v popisu, jde o dvě čísla, která určují, zda vám koloběžka vyhovuje.</li></ul>'
          '<h2>Dětské modely Kid a jak dítě roste</h2>'
          '<p>Dětské varianty Kid mají nižší plošinu a řídítka, která se přizpůsobí výšce dítěte. Při výběru si všímejte tří věcí. Dítě má při stání na plošině dosáhnout oběma nohama a držet řídítka bez zvedání ramen. Koloběžka nesmí být tak těžká, aby ji dítě samo neuneslo. A řídítka musí mít rozsah nastavení pro alespoň dvě sezóny růstu. Orientační přehled podle výšky dítěte pomůže určit, kdy je čas přejít na větší model.</p>'
          + T(['Výška dítěte', 'Vhodný typ', 'Poznámka'], [
              ['do zhruba 100 cm', 'odrážedlo nebo tříkolka', 'nejdřív rovnováha, až potom koloběžka'],
              ['100–120 cm', 'dětská koloběžka Kid', 'nízké řídítka a výrazně lehčí rám'],
              ['120–140 cm', 'větší dětský model, například Street Fun nebo Hill Fun', 'rozsah řídítek nechte na špičce'],
              ['nad 140 cm', 'model pro dospívající a dospělé', 'ověřte nosnost a výšku řídítek']]) +
          '<p>Tabulka je orientační. Dítě stejné výšky může mít jiné proporce a jinou zručnost, proto se vždy rozhodujte podle zkoušky. Nejmenší děti se mohou na prvních kilometrech pohodlně opřít o <a href="/odrazedla/">odrážedlo</a>. K dětským modelům Kostka patří v nabídce také doplněk Footstep Comfort, stupátko pro dítě na koloběžku, a stojan Kid, který udrží koloběžku v bytě nebo v garáži.</p>'
          '<h2>Technika jízdy a držení těla</h2>'
          '<p>Na koloběžce s velkými koly se jezdí jinak než na malé městské. Odrážejte se střídavě oběma nohama, aby se zátěž rozložila a nebolelo stejné koleno. Stojná noha zůstává lehce pokrčená a tlumí nerovnosti, trup se mírně předklání a ramena zůstávají uvolněná. Při zatáčení se naklánějte do oblouku a řídítka jen lehce vedete, ne trháte. Z kopce přenášejte váhu mírně dozadu, brzdu stiskněte plynule a včas. Děti se techniku učí nejlépe v parku nebo na rovné cyklostezce, kde není provoz, a po několika dnech už zvládnou i delší trasu.</p>'
          '<h2>Pro koho Kostka není nejlepší volba</h2>'
          '<p>Velká koloběžka se hůř nosí, takže pokud ji potřebujete každý den vyvézt do čtvrtého patra, bude vám vadit hmotnost. Pro triky a skokánky je potřeba pevný freestyle rám a malá kola. Pro nejmenší děti, které ještě neumí udržet rovnováhu, je lepší nejdřív odrážedlo nebo tříkolka. Naopak pro pravidelné vyjížďky, cestu po cyklostezce a rodinné výlety jde o rozumnou volbu. Barva nemění technické parametry, takže ji volte až nakonec podle toho, co je skladem.</p>'
          '<h2>Doplňky, světla a bezpečnost</h2>'
          '<p>Světlo na koloběžku řeší adaptér Klicklight III, který se hodí do poslední hodiny denního světla nebo na cestu v zimě. Světlo vpředu a červené vzadu je u každé jízdy za šera nejdůležitější doplněk. Pro děti i dospělé platí, že helma a <a href="/chranice-a-helmy/">chrániče</a> patří k základní výbavě. Rukavice s chráněnou dlaní ochrání ruce při pádu a reflexní vesta zlepšuje viditelnost. U menších dětí je dobré přibalit ještě chrániče kolen a loktů, které se v prvních týdnech používají nejvíc.</p>'
          '<h2>Kostka ve srovnání s ostatními značkami</h2>'
          '<p>Mezi koloběžkami dominuje několik výrobců. ' + B(('micro', 'Micro'), ('yedoo', 'Yedoo'), ('nils-extreme', 'Nils Extreme'), ('tempish', 'Tempish')) + ' mají každý svůj charakter. Micro je známé především lehkými městskými a dětskými koloběžkami, Yedoo prodává koloběžky s velkými koly určené pro delší jízdu, a stojí tak nejblíž Kostce. Nils Extreme a Tempish nabízejí pestrý sortiment pro děti a mládež. Kostka se vyplatí, pokud potřebujete koloběžku se stabilní jízdou a velkými koly a vyhovuje vám český výrobce. Pro školní dojíždění a nošení v MHD se může hodit lehčí a menší model od jiného výrobce.</p>'
          '<h2>Údržba, aby koloběžka vydržela</h2>'
          '<ol><li>Jednou za měsíc dotáhněte šrouby řídítek, kol a skládacího mechanismu.</li>'
          '<li>Kontrolujte tlak v nafukovacích pláštích a stav brzdových špalíků.</li>'
          '<li>Po jízdě v dešti koloběžku otřete a ložiska nechte zaschnout.</li>'
          '<li>Skládací klouby občas lehce namažte a zkontrolujte, zda se při skládání nevzpříčí.</li>'
          '<li>Před delší pauzou ji uložte v suchu, nejlépe na stojanu, aby se plášť nedeformoval.</li></ol>',
    faq=[
        ('Pro koho je koloběžka Kostka vhodná?', 'Je určená pro děti, dospívající i dospělé, kteří chtějí jezdit rekreačně nebo pravidelně na delší vzdálenosti. Velká kola a stabilní konstrukce se hodí na rovné cesty, do parku nebo do školy. Pro triky ve skateparku je lepší freestyle koloběžka s pevným rámem.'),
        ('Čím se liší řady Tour, Twenty, Hill a Street?', 'Názvy naznačují použití. Tour a Travel míří na delší vyjížďky a výlety, Twenty na jezdce s většími koly, Hill na nerovnější terén a Street na každodenní jízdu po městě. Přesné parametry ověřte u produktu, protože se liší podle generace a verze.'),
        ('Co znamená označení G5 a G6?', 'Je to generace koloběžky. Novější verze přináší úpravy rámu a komponent, starší bývá ve slevě. Porovnávejte vždy stejné generace a při nákupu dílů sledujte, zda se pro vaši koloběžku hodí.'),
        ('Jak vybrat velikost koloběžky pro dítě?', 'Dítě musí na plošině stát oběma nohama a držet řídítka bez zvedání ramen. Řídítka by měla mít rozsah nastavení pro další růst. Po několika sezónách přejděte na větší model, ale nekupujte koloběžku, která je dítěti příliš velká.'),
        ('Je lepší skládací, nebo pevná koloběžka?', 'Skládací Fold je praktická, pokud ji nosíte do vlaku, auta nebo bytu. Pevná je tužší a lépe se s ní jezdí na nerovném povrchu, protože nemá kloub, který se může po čase uvolnit. Zvolte podle toho, jak často koloběžku přenášíte.'),
        ('Potřebuje koloběžka ruční brzdu?', 'Na delší jízdy a z kopce se ruční brzda na řídítkách vyplatí, protože brzdí plynuleji a umožňuje zpomalit bez sundání nohy. Dětem stačí zadní brzda na blatníku, pokud jsou zvyklé na odrážedlo a jezdí po rovině.'),
        ('Dají se ke koloběžkám Kostka koupit světla?', 'V nabídce je adaptér Klicklight III se světlem a další příslušenství, například stupátko pro dítě nebo stojan Kid. Pro jízdu za šera použijte přední bílé a zadní červené světlo, a to i na krátké trase.'),
        ('Jak často mám dofukovat kola?', 'U nafukovacích plášťů zkontrolujte tlak alespoň jednou za dva týdny a před delší jízdou. Měkká kola zvyšují odpor a rychleji se opotřebují. Doporučený tlak je uvedený na boku pláště nebo v návodu výrobce.'),
        ('Čím se Kostka liší od koloběžek Yedoo a Micro?', 'Kostka a Yedoo jsou si bližší velkými koly a jízdou na delší vzdálenosti. Micro je známé lehkými městskými a dětskými koloběžkami, které se snadno nosí. Rozhodněte se podle toho, zda potřebujete spíše pohodlí na trase, nebo nízkou hmotnost.'),
        ('Mohou na koloběžku Kostka jezdit dva lidé?', 'Ne, koloběžka je určena pro jednoho jezdce a má stanovenou nosnost. Společná jízda přetěžuje rám i brzdy a zhoršuje řízení. Maximální zatížení a návod výrobce vždy zkontrolujte v popisu produktu.'),
    ],
)

# ------------------------------------------------------------------ trampolina-marimex
NEW['trampolina-marimex'] = dict(
    title='Trampolína Marimex: díly, sítě, pružiny a rozměry',
    desc='Trampolíny Marimex a náhradní díly: jak určit průměr, počet pružin, délku pružiny a typ sítě, aby skákací plocha, kryt i ochranná síť seděly.',
    intro='<p>Marimex je česká značka zahradního vybavení, která je u nás známá hlavně bazény a trampolínami. Ve srovnání s ostatními výrobci má v nabídce zvláštnost: velkou část sortimentu netvoří celé trampolíny, ale díly k nim. Skákací plochy, pružiny, kryty, ochranné sítě, žebříky a kotvicí sady se kupují hlavně při opravě stávající trampolíny, a tam rozhoduje přesný rozměr, ne cena. '
          'Na této stránce najdete trampolíny a příslušenství značky Marimex ze všech řad od menší dětské po zahradní Premium s vnitřní sítí. Průvodce ukazuje, jak zjistit průměr a počet pružin, proč záleží na roce výroby, jak se liší vnitřní a vnější síť a kdy je lepší koupit celou novou trampolínu. Obecný přehled typů a bezpečnosti najdete v kategorii <a href="/trampoliny/">trampolíny</a>, malé děti pak ocení <a href="/detska-trampolina/">dětské trampolíny</a>.</p>',
    guide='<h2>Co všechno Marimex v nabídce nese</h2>'
          '<p>Z katalogu Marimex je vidět, že tato značka podporuje své trampolíny dlouhodobě. V nabídce jsou celé sestavy se sítí a žebříkem v různých průměrech, bezpružinová trampolína Free Jump, zapuštěná varianta Premium in-ground a velký sortiment náhradních dílů. Právě díly jsou důvod, proč si lidé trampolíny Marimex vybírají znovu: když se po sezóně roztrhne skákací plocha nebo vyprší životnost sítě, stačí vyměnit jen daný díl.</p>'
          + T(['Díl', 'Podle čeho vybrat', 'Na co si dát pozor'], [
              ['Skákací plocha', 'průměr rámu a počet pružin, tedy počet ok', 'plochy pro stejný průměr se liší počtem pružin, zaměňte jen správný kus'],
              ['Pružina', 'délka v centimetrech a průměr trampolíny', 'pružiny se prodávají pro rozsah průměrů a pro určité roky výroby'],
              ['Kryt pružin', 'průměr trampolíny a řada', 'kryt musí zakrýt celý okraj včetně uchycení tyčí'],
              ['Ochranná síť', 'průměr, počet tyčí a typ sítě', 'vnitřní a vnější síť nelze navzájem zaměnit'],
              ['Žebřík', 'výška rámu', 'ověřte, zda se hodí k vaší řadě'],
              ['Kotvicí sada', 'typ povrchu a velikost trampolíny', 'vrták a kotva musí odpovídat podkladu'],
              ['Ochranná plachta', 'průměr', 'chrání plochu v zimě a při dlouhém nepoužívání']]) +
          '<p>Většina dílů má v názvu rozměry v centimetrech, nejčastěji 244, 305, 366, 396, 427 a 457. Právě tyto údaje rozhodují, ne vzhled nebo cena. Při srovnávání obchodů dbejte, aby porovnávané nabídky měly stejný průměr, stejný počet pružin a stejný popis řady, jinak porovnáváte dva různé díly.</p>'
          '<h2>Jak změřit průměr a spočítat pružiny</h2>'
          '<p>Průměr trampolíny se měří od vnějšího okraje rámu přes střed k protilehlému okraji. U skákací plochy je rozdíl mezi průměrem rámu a průměrem plochy, protože plocha je menší, než rám, který ji obepíná. U Marimex se v názvu některých ploch objevuje právě tento údaj: například plocha pro trampolínu s průměrem rámu 366 cm má průměr plochy 318 cm. Dalším povinným údajem je počet pružin. Spočítejte je po celém obvodu rámu, stačí jedno kolo. Pak si změřte délku jedné pružiny včetně háčků, a to na odpojené nebo nezatížené pružině.</p>'
          '<ol><li>Změřte průměr rámu z vnější strany.</li>'
          '<li>Spočítejte pružiny na obvodu.</li>'
          '<li>Změřte délku jedné pružiny včetně obou háčků.</li>'
          '<li>Zjistěte rok výroby, ideálně z návodu, faktury nebo štítku na rámu.</li>'
          '<li>Teprve s těmito čtyřmi údaji vybírejte plochu, pružinu nebo síť.</li></ol>'
          '<h2>Proč záleží na roce výroby</h2>'
          '<p>V názvech dílů se objevují poznámky jako „do roku 2015“ nebo „od roku 2015“. Výrobce během let měnil rozměry rámů, uchycení pružin a tvar spojů, takže plocha nebo pružina stejného průměru z různých let si nemusí odpovídat. U průměru 366 cm se tento rozdíl projevuje nejvíc. Pokud jste při koupi nezachovali doklad, spočítejte pružiny a změřte jejich délku a podle toho zvolte díl. U pochybností raději kontaktujte prodejce s fotografií uchycení, než abyste kupovali na zkoušku.</p>'
          '<h2>Pružiny, které se opotřebovávají postupně</h2>'
          '<p>Kovová pružina se při dlouhém používání vytahuje a ztrácí sílu. Poznáte to tak, že se odraz zhoršuje nerovnoměrně, plocha se na jedné straně prohýbá víc a vznikají nebezpečné nerovnosti. V takovém případě je nutné vyměnit všechny pružiny najednou, ne jen jednu rozbitou. Smíšené staré a nové pružiny dávají nerovnoměrné napětí a plocha se brzy poškodí. Pro vyšší průměry se prodávají pružiny delší, u některých řad mají kolem 17,8 cm, a proto při objednávání dbejte, aby délka seděla.</p>'
          '<h2>Skákací plocha a krytí pružin</h2>'
          '<p>Skákací plocha má při intenzivním používání omezenou životnost. Ukazatelem jsou vydřené švy, vypadávající nitě a zvětšující se vlnění po obvodu. Plocha se vyměňuje ve chvíli, kdy se šev začne rozpárat, protože další skákání jej rozšíří a může dojít k pádu na pružiny. Kryt pružin zakrývá prostor mezi plochou a rámem, aby se do něj nedostala noha. Měl by být pevně nasazený a poškozený kryt se musí vyměnit ihned. U modelů Premium se prodává kryt i v oranžové barvě, takže si můžete vybrat viditelnější provedení.</p>'
          '<h2>Vnitřní a vnější ochranná síť</h2>'
          '<p>Ochranná síť je u trampolíny to nejdůležitější, a proto je jí v nabídce věnovaný velký prostor: najdete sítě pro různé průměry, náhradní síť pro řadu Premium a Premium in-ground i vnitřní síť k celé sestavě. Vnitřní síť je upevněná uvnitř pružin a neumožňuje dopadnout mezi ně. Vnější síť stojí mimo plochu a nechává více prostoru pro skákání, ale vyžaduje stabilní tyče. Při výběru dbejte na správný průměr a počet tyčí, protože síť pro šest tyčí nelze natáhnout na rám s osmi. Sítě stárnou vlivem slunce, proto je vyměňte při prvních trhlinách nebo když materiál zkřehne.</p>'
          '<h2>Celá nová trampolína, nebo oprava</h2>'
          '<p>Oprava má smysl, pokud je rám v pořádku a poškozen je jen jeden díl. Rez na nohách, prohnutý rám nebo uvolněné spoje jsou důvodem koupit novou trampolínu. Při rozhodování pomůže jednoduchý přehled.</p>'
          + T(['Stav trampolíny', 'Doporučení'], [
              ['natržená plocha, rám v pořádku', 'vyměnit plochu a zkontrolovat pružiny'],
              ['uvolněné nebo slabé pružiny', 'vyměnit všechny pružiny najednou'],
              ['poškozená síť nebo kryt', 'vyměnit příslušný díl okamžitě'],
              ['zkorodovaný nebo prohnutý rám', 'koupit novou trampolínu'],
              ['děti vyrostly, potřebují větší plochu', 'zvolit nový průměr, ne zvětšovat starou']]) +
          '<p>Pokud trampolínu vyměňujete celou, porovnejte i další značky: ' + B(('insportline', 'Insportline'), ('master', 'Master'), ('springos', 'Springos'), ('sedco', 'Sedco'), ('berg', 'Berg')) + '. Díly mezi výrobci nejsou zaměnitelné, takže před koupí promyslete, zda budete u značky zůstávat.</p>'
          '<h2>Zahrada, bezpečnost a bezpružinová varianta</h2>'
          '<p>Bezpružinová trampolína Free Jump nemá kovové pružiny, a proto se skáče měkčeji a riziko zachycení nohy mezi pružinami odpadá. Hodí se pro rodiny s menšími dětmi, vyžaduje ale přesné dodržení nosnosti. Zapuštěná varianta Premium in-ground zase snižuje výšku pádu, vyžaduje však výkop a odvod vody. Při umístění dbejte na rovný podklad, volný prostor kolem a výšku skoku bez větví nad hlavou. Pro další zahradní nápady zkuste <a href="/hry-na-zahradu/">hry na zahradu</a>, <a href="/nafukovaci-hracky/">nafukovací hračky</a> nebo <a href="/bazeny/">bazény</a>, kde má Marimex také silné zastoupení. Pro cvičení uvnitř stojí za pohled <a href="/fitness/">fitness</a> a <a href="/volny-cas/">volný čas</a>.</p>'
          '<h2>Zimování a roční kontrola</h2>'
          '<p>Trampolína stojí venku celý rok a nejvíc ji opotřebovává slunce a vlhkost. Na jaře ji projděte podle krátkého postupu: zkontrolujte spoje rámu, nohy a svary, zda nejeví stopy koroze, a utáhněte šrouby, které se za zimu uvolnily. Poté prohlédněte plochu, švy a pružiny, a síť s kryty. Na zimu se vyplatí sundat síť a vyčistit plochu od listí, protože vlhké listí přidržuje vodu a plocha se hůř suší. Ochranná plachta chrání plochu před sluncem a sněhem, ale nesmí na ní stát voda. Hlídejte také okolí, aby pod trampolínou nerostla vysoká tráva a nehromadila se vlhkost. Při dlouhodobém skladování uložte rozebranou síť a kryt v suchu, nejlépe v textilním pytli. Pro trénink mimo sezónu si můžete pořídit <a href="/fitness-pomucky/">fitness pomůcky</a> a skákat doma na malé trampolíně.</p>',
    faq=[
        ('Jak poznám, jaký díl potřebuji k trampolíně Marimex?', 'Změřte průměr rámu, spočítejte pružiny, změřte délku jedné pružiny a zjistěte rok výroby. S těmito údaji najdete správnou skákací plochu, pružinu nebo síť. Při pochybnostech pošlete prodejci fotografii uchycení a štítek trampolíny.'),
        ('Proč záleží na roce výroby?', 'Výrobce během let měnil rozměry a uchycení, takže stejný průměr z různých let nemusí odpovídat. U průměru 366 cm se rozdíly projevují nejvíc. Rok výroby najdete v návodu, na faktuře nebo na štítku na rámu.'),
        ('Mám vyměnit jednu pružinu, nebo všechny?', 'Pokud je pružina vytažená nebo ztratila sílu, vyměňte všechny najednou. Smíšené staré a nové pružiny dávají nerovnoměrné napětí a plocha se rychleji poškodí. Jedna rozbitá pružina ukazuje, že ostatní jsou na konci životnosti.'),
        ('Jak zjistím počet pružin na trampolíně?', 'Spočítejte pružiny po celém obvodu rámu a označte si výchozí, ať se nespletete. Počet souvisí s průměrem a řadou, takže plocha se stejným průměrem může mít jiný počet ok. Při koupi plochy sledujte, zda odpovídá váš údaj.'),
        ('Můžu použít síť od jiné značky?', 'Technicky ano, pokud sedí průměr, počet tyčí a uchycení, ale spolehlivěji funguje originální díl. Sítě od jiných výrobců mívají jiný způsob uchycení a výšku. Při výběru porovnejte průměr, počet tyčí a typ sítě, vnitřní a vnější nejsou zaměnitelné.'),
        ('Jaký je rozdíl mezi vnitřní a vnější sítí?', 'Vnitřní síť je upevněná uvnitř pružin a brání dopadu mezi pružiny nebo mimo trampolínu. Vnější síť stojí mimo skákací plochu a nechává víc prostoru, ale vyžaduje stabilní tyče. Obě mají svá specifika, takže si ověřte typ vlastní trampolíny.'),
        ('Je bezpružinová trampolína bezpečnější?', 'Odpadá riziko zachycení nohy mezi pružinami a skok je měkčí. I tak je nutné dodržovat nosnost, chránit okolí sítí a nepovolovat saltá. Bezpečnost závisí na celkovém provedení, nejen na typu odrazu.'),
        ('Kdy vyměnit skákací plochu?', 'Při rozpárání šví, vytahaných nitích nebo velkém vlnění po obvodu. Pokud se rozpáraný šev rozšíří, hrozí pád na pružiny. Vyměňte plochu včas a zároveň zkontrolujte pružiny a kryt.'),
        ('Jak zajistit trampolínu proti větru?', 'Pomůže kotvicí sada s vrtáky, která se upevní do země nebo na pevný podklad. Při silném větru je lepší sundat síť a plochu zajistit. Kotvy vybírejte podle typu povrchu, tráva a beton vyžadují jiné řešení.'),
        ('Vyplatí se oprava starší trampolíny?', 'Oprava má smysl, pokud je rám pevný a vadí jen plocha, síť nebo pružiny. Při korozi nebo prohnutí rámu je lepší koupit novou trampolínu. Zvažte také, zda děti nepotřebují větší průměr.'),
    ],
)

# ------------------------------------------------------------------ jordan-teplaky
NEW['jordan-teplaky'] = dict(
    title='Jordan tepláky: střihy, fleece, velikosti a kombinace',
    desc='Jordan tepláky pánské, dámské i dětské. Rozdíl mezi jogger, Brooklyn Fleece a track pants, velikosti podle výšky dítěte, praní a kombinace s mikinou.',
    intro='<p>Jordan vznikl jako basketbalová řada pod křídly Nike a dnes patří k nejrozpoznatelnějším sportovním značkám na ulici. Logo Jumpman, tedy skákající silueta, je na teplácích vidět na pase, stehně nebo lemu nohavice a pozná se na první pohled. V kategorii <a href="/teplaky/">tepláků</a> mají Jordan vlastní modelové řady s jasným charakterem. '
          'Na této stránce najdete Jordan tepláky pro muže, ženy i děti od kojeneckých souprav po fleecové jogger kalhoty pro dospělé. Průvodce rozebírá, v čem se liší řady Jumpman, Brooklyn Fleece a Flight, jak číst kód stylu, jak vybírat velikost u dětí a čím se Jordan odlišuje od obyčejné řady <a href="/nike-teplaky/">Nike tepláky</a>. Pokud sháníte celý outfit, nahlédněte také do výběrů <a href="/nike-mikina/">Nike mikin</a> a <a href="/jordan-kratasy/">Jordan kraťasů</a>.</p>',
    guide='<h2>Jordan jako samostatná řada v rámci Nike</h2>'
          '<p>Značka Jordan začala v osmdesátých letech jako basketbalová obuv pro hráče Michaela Jordana a postupně přerostla v samostatnou módní a sportovní linii. Oblečení Jordan vychází z basketbalového prostředí, ale dnes se nosí především v městském stylu. Tepláky se tak liší od klasické produkce Nike zejména výraznějším logem Jumpman, střihem inspirovaným street stylem a poněkud hutnějšími materiály. Z hlediska výběru proto počítejte s tím, že jde o módnější kus než čistě tréninkové kalhoty.</p>'
          '<h2>Modelové řady v nabídce</h2>'
          '<p>V katalogu se opakují názvy, které se vyplatí umět rozlišit. Každý z nich označuje jiný střih nebo materiál.</p>'
          + T(['Název řady', 'Co obvykle znamená', 'Pro koho a kdy'], [
              ['Jumpman Air Fleece Jogger', 'jogger se zúženou nohavicí a počesaným vnitřkem', 'chladnější dny, každodenní nošení'],
              ['Brooklyn Fleece', 'měkká flísová pletenina, rovnější nebo volnější střih', 'volný čas a podzimní až zimní měsíce'],
              ['Flight Fleece', 'fleecová řada ve stejném stylu', 'městský styl a doplnění mikiny'],
              ['Flight MVP Track Pants', 'kalhoty ze šusťákového nebo lehčího materiálu', 'jaro, podzim a sport v teple'],
              ['Sport Crossover', 'dámská řada s pohodlným střihem', 'trénink i volný čas'],
              ['Play Your Way Flc Jogger', 'dětský jogger z fleecové pleteniny', 'školní děti, hra a sport']]) +
          '<p>Název nikdy nenahrazuje čtení popisu, ale pomůže zúžit výběr. Fleece neboli počesaná pletenina uvnitř zahřeje, ale v teple i přehřeje. Pokud tepláky chcete nosit celý rok, hledejte lehčí materiál bez silné vrstvy uvnitř. Další rady k materiálům najdete v kategorii <a href="/sportovni-kalhoty/">sportovní kalhoty</a>.</p>'
          '<h2>Jak číst kód stylu</h2>'
          '<p>U Jordan i Nike se v názvu často objevuje kód typu DQ7890-613 nebo DA6803. První část označuje konkrétní styl, tedy střih a materiál. Číslo za pomlčkou udává barevnou variantu. Kód vám umožní najít stejný kus u různých prodejců a porovnat jeho dostupnost. Dva kusy se stejným jménem ale s jiným kódem stylu se mohou lišit materiálem i střihem. Proto při srovnávání obchodů sledujte kód přesně, zvlášť u kalhot, které se prodávají v několika barvách.</p>'
          '<h2>Pánské Jordan tepláky</h2>'
          '<p>Pánské modely tvoří jádro nabídky a nejčastěji mají jogger střih se zúženou nohavicí a manžetou u kotníku. Měkký fleece uvnitř, potisk Jumpman na stehně a pružný pas se šňůrkou tvoří klasickou kombinaci. Hnědé, vínové a modré odstíny se mezi řadami opakují, takže si před koupí ověřte přesnou barvu v popisu, protože odstín na fotografii se na každém monitoru jeví jinak. Tmavé tepláky se snadno kombinují, světlé a výrazné se hodí k jednoduchému oblečení. Při výběru velikosti počítejte s tím, že Jordan se nosí volněji, než sedí klasický sportovní střih, a proto někteří zákazníci volí o velikost menší.</p>'
          '<h2>Dámské Jordan tepláky</h2>'
          '<p>Dámské Jordan tepláky se liší hlavně střihem v pase a na bocích. Modely Brooklyn a Sport Crossover mají pohodlný, mírně volný střih, který se dobře kombinuje s krátkou mikinou. Dámské tepláky bývají i s bavlnou, která je příjemná na kůži, ale hůř odvádí pot. Pokud je budete používat na cvičení, zvolte materiál s elastanem. Pro vrstvení pod kalhotami v zimě poslouží <a href="/termopradlo/">termoprádlo</a>. Pokud sháníte vhodný horní díl, zkuste <a href="/mikiny/">mikiny</a>.</p>'
          '<h2>Dětské Jordan tepláky a soupravy</h2>'
          '<p>Dětské tepláky Jordan patří k nejpočetnější části katalogu. Najdete tu kalhoty, jogger modely i celé teplákové sady, od kojeneckých po velikosti pro školáky. Většina dětských modelů se prodává s bavlnou, která je příjemná a odolná. Při výběru neřešte věk, ale výšku dítěte, protože dětské velikosti značky Nike a Jordan se uvádějí v centimetrech výšky. Následující tabulka je orientační a vždy ověřte údaje u konkrétního kusu.</p>'
          + T(['Výška dítěte', 'Orientační označení velikosti', 'Poznámka'], [
              ['do 90 cm', 'kojenecká a batolecí řada', 'kontrolujte měkkost lemů'],
              ['90–110 cm', 'předškolní velikosti', 'pas s gumou a šňůrkou'],
              ['110–128 cm', 'mladší školáci, označení XS', 'nohavice lze podehnout'],
              ['128–147 cm', 'S až M', 'jogger a sada'],
              ['nad 147 cm', 'L a XL', 'sedí i dorostencům, ověřte tabulku']]) +
          '<p>U dětských kusů je výhodou teplákový set, tedy mikina a tepláky ze stejného materiálu. Pohodlně se nosí do školy i na ven, ale mikinu můžete nosit i samostatně. Při růstu dítěte kupujte tepláky o číslo větší, protože nohavice se podehnou a pas se stáhne šňůrkou, ale nekupujte o dvě čísla, jinak dítě šlape na nohavice.</p>'
          '<h2>Jak Jordan kombinovat</h2>'
          '<ul><li><strong>S tenisky:</strong> k Jordan teplákům patří basketbalové a retro boty, výběr najdete v kategorii <a href="/tenisky/">tenisky</a> a ve <a href="/basketbal/">basketbalu</a>.</li>'
          '<li><strong>S mikinou:</strong> stejná barva dá dojem souboru, kontrastní kus působí uvolněněji.</li>'
          '<li><strong>S bundou:</strong> zimní kombinace s <a href="/sportovni-bundy/">sportovní bundou</a> a čepicí.</li>'
          '<li><strong>Jako souprava:</strong> hotové sady najdete v kategorii <a href="/soupravy/">soupravy</a>.</li>'
          '<li><strong>Pro volný čas:</strong> jednobarevný kus do města a výraznější na ven.</li></ul>'
          '<h2>Jak zjistit, že střih sedí</h2>'
          '<p>Před koupí si změřte pas, boky a vnitřní délku nohavice u kalhot, které už nosíte rádi, a porovnejte hodnoty s tabulkou. U joggerů se řídí délka nohavice kotníkem: manžeta má těsně obepínat kotník a nesmí se zadrhávat na lýtku. Při chůzi se nemá pas sesouvat a šňůrka má být použitá pro jemné dotažení, ne jako záchrana nevhodné velikosti. Sednout si do dřepu by měl jít bez tlaku v rozkroku. Při zkoušení vezměte boty, ke kterým je budete nosit, protože délka nohavice se s teniskami chová jinak než s kotníkovou obuví. A pokud tepláky objednáváte přes internet, vyberte obchod, který dovolí vrácení nebo výměnu velikosti.</p>'
          '<h2>Jordan, Nike a ostatní značky tepláků</h2>'
          '<p>Chcete-li porovnat Jordan s ostatními, základní volbou jsou ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('champion', 'Champion'), ('under-armour', 'Under Armour')) + '. Nike je základ pro tréninkové kalhoty s lehčími materiály, Adidas a Puma nabízejí široké střihy pro každodenní nošení, Champion je typický teplákovinou v klasickém stylu. Jordan se odlišuje basketbalovým kontextem a viditelným logem. Další možnosti najdete ve výběrech <a href="/teplaky-puma/">Puma tepláky</a>, <a href="/gymbeam-teplaky/">GymBeam tepláky</a> a <a href="/teplaky-tommy-hilfiger/">tepláky Tommy Hilfiger</a>.</p>'
          '<h2>Praní a péče</h2>'
          '<ol><li>Tepláky perte naruby, aby se logo a potisk neotíraly.</li>'
          '<li>Teplota do 30 až 40 °C, jemný program a bez aviváže u funkčních směsí.</li>'
          '<li>Nesušte je v horké sušičce, fleece se zmačká a zhoustne.</li>'
          '<li>Žmolky odstraňte holicím strojkem na textil, nikoli nůžkami.</li>'
          '<li>Vraťte je do skříně suché, vlhký fleece zapáchá.</li></ol>'
          '<p>Věnujte pozornost i sezónním slevám. Tepláky se nejčastěji zlevňují po skončení zimní sezóny a při obměně kolekce a starší barvy bývají za výhodnější cenu. Sledujte hlavně kód stylu, abyste ve slevě našli totéž, co vás zajímá.</p>',
    faq=[
        ('Čím se Jordan tepláky liší od Nike?', 'Jordan je samostatná řada pod Nike s basketbalovým původem a výrazným logem Jumpman. Střih je více street a materiály hutnější. Nike tepláky jsou častěji tréninkové a lehčí, Jordan se nosí především ve volném čase.'),
        ('Co znamená Brooklyn Fleece?', 'Je to řada z měkké počesané pleteniny s příjemným vnitřkem. Hodí se na podzim a v zimě pro volný čas. Při větší aktivitě nebo v teple se v ní můžete přehřát, a proto je vhodná spíš do chladna.'),
        ('Jak poznám správnou velikost Jordan tepláků?', 'Podívejte se na tabulku u konkrétního modelu a porovnejte obvod pasu a délku nohavice. Jordan sedí volněji než klasický sportovní střih, proto se vyplatí zvážit, zda nepotřebujete menší velikost. Při pochybnostech raději nakupujte u obchodu s bezplatnou výměnou.'),
        ('Jak vybrat velikost dětských Jordan tepláků?', 'Podle výšky dítěte, ne podle věku. Dětské velikosti značky se uvádějí v centimetrech výšky, proto změřte dítě bez bot. Vybírejte o číslo větší, aby nohavice šly podehnout a pas se dal stáhnout.'),
        ('Co znamená kód u názvu, třeba DQ7890-613?', 'První část označuje styl, tedy střih a materiál, a druhá barevnou variantu. Pomocí kódu najdete stejný kus u více prodejců. Při srovnávání cen sledujte oba údaje, jinak můžete porovnávat dva různé modely.'),
        ('Jak prát tepláky s fleecem?', 'Perte je naruby při nízké teplotě na jemný program a bez aviváže. Nesušte je v horké sušičce, vlákna se slepí a fleece ztvrdne. Po vyprání je vhodné vytřepat nohavice a nechat je uschnout na vzduchu.'),
        ('Jsou Jordan tepláky vhodné na sport?', 'Hodí se na lehkou aktivitu a trénink v chladu, ale silný fleece je při intenzivním sportu teplý. Pro běh a posilovnu se víc hodí lehký polyester s elastanem, který odvádí pot. Jordan je především volnočasová řada.'),
        ('Mám volit jogger, nebo rovný střih?', 'Jogger se zúženou nohavicí a manžetou se hodí k teniskám a dobře drží. Rovný střih bez manžety působí klidněji a lépe se kombinuje s různou obuví. Záleží na tom, jaké boty nosíte nejčastěji.'),
        ('Jak poznat pravé Jordan tepláky?', 'Kupujte u obchodů ověřených v přehledu a porovnávejte kód stylu s oficiálním popisem. Neobvykle nízká cena a špatně provedený potisk jsou častým varováním. Při pochybnostech sledujte štítky s velikostní tabulkou a údajem o složení.'),
        ('Kdy se tepláky nejvíc zlevňují?', 'Nejčastěji po skončení zimní sezóny a při obměně kolekce, kdy ve slevě zůstávají starší barvy a poslední velikosti. Při slevě rozhoduje dostupnost. Pokud hledáte běžnou barvu a velikost, můžete počkat, ale oblíbené kusy mizí rychle.'),
    ],
)
