"""sporteka.cz — facet landing texts wave 156: damske-tenisky, nike-tricko, damske-teplaky, sandaly-keen.
General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ damske-tenisky
NEW['damske-tenisky'] = dict(
    title='Dámské tenisky: střih, velikost a značky na každý den',
    desc='Dámské tenisky s užší patou a ženským kopytem. Jak vybrat velikost, podrážku a značku pro město, práci vstoje i cestování a porovnat nabídky obchodů.',
    intro='<p>Dámské tenisky se nedělají jen zmenšením pánského modelu. Bota je postavená na užší patě, přizpůsobená ženské šířce předonoží a často i na nižší hmotnost těla, takže se mění tuhost pěny i tvar špičky. Tady se potkávají sportovní siluety, retro nízké modely, platformy i měkké vycházkové páry, které ženy nosí do práce, na cesty i do města. '
          'Stránka vychází z kategorie <a href="/tenisky/">tenisky</a> a zobrazuje jen modely pro ženy a dívky. Průvodce vysvětluje, jak se liší stavba dámské boty, jak změřit chodidlo, kdy sáhnout po měkké pěně a kdy po tenké podešvi, a jak se značky v nabídce střihem a charakterem liší. '
          'Chcete-li zúžit výběr rovnou na značku, otevřete <a href="/nike-tenisky/">Nike</a>, <a href="/adidas-tenisky/">Adidas</a> nebo <a href="/skechers-tenisky/">Skechers</a>.</p>',
    guide='<h2>Čím se dámská bota liší od pánské</h2>'
          '<p>Ženské chodidlo má v průměru užší patu v poměru k předonoží a jinak rozložený objem nad nártem. Výrobci proto pro dámské řady používají jiné kopyto, ne jen menší čísla. Patu drží užší hrdlo, předonoží bývá o něco štíhlejší a vnitřní vložka je lehčí. Praktický důsledek je jednoduchý: žena s užší nohou v pánské bote často cítí vůli v patě, a naopak široké chodidlo se v dámském střihu může v místě palce tlačit.</p>'
          '<p>Rozdíl je znát také v hmotnosti a tuhosti. Dámské modely mívají měkčí pěnu, protože lehčí tělo ji dokáže stlačit stejně jako těžší tělo tvrdší materiál. Stejná pěna z pánské řady může působit tvrdě a na lehčí došlap nereaguje. Proto se při koupi vyplatí neřešit jen vzhled, ale i to, jestli je bota určená pro ženy výslovně.</p>'
          '<h2>Druhy dámských tenisek podle stylu</h2>'
          + T(['Styl', 'Jak vypadá', 'Pro koho a kdy'], [
              ['Retro a klasické nízké', 'plochá nebo mírně profilovaná podešev, kůže nebo imitace, čistá linka', 'město, kancelář s volnějším oblékáním, kombinace se šaty i džínami'],
              ['Chunky a platforma', 'vyšší a silnější podrážka, objemná špička', 'streetwear, ženy, které chtějí vyšší postavu bez podpatku'],
              ['Běžecký styl', 'síťovina, silná pěnová mezipodešev, měkká pata', 'celodenní chůze, cestování, práce vstoje'],
              ['Plátěné a slip-on', 'tenký textil, gumová špička, často bez šněrování', 'léto, krátké cesty, nenáročný den'],
              ['Vycházkové s tlumením', 'měkká stélka, pohodlné hrdlo, lehká konstrukce', 'delší procházky, cesty MHD, starší klienti a pohodlí na prvním místě'],
          ])
          + '<p>Platformní podešev působí výrazně, ale u modelů s vyšší podrážkou záleží na její ohebnosti. Pokud se bota v místě prstů nedá ohnout, krok vypadá toporně a po dni na nohou se unavíte víc než v nízkých teniskách.</p>'
          '<h2>Jak změřit chodidlo a vybrat velikost</h2>'
          '<p>Postavte se bosou nohou na papír, obkreslete ji a změřte vzdálenost od paty k nejdelšímu prstu. Měření opakujte večer, kdy je noha mírně oteklá. K délce přičtěte rezervu před prsty zhruba půl centimetru až centimetr a hledejte tabulku výrobce. Číslo na krabici se mezi značkami liší, proto neberte velikost z jiné obuvi jako jistotu.</p>'
          '<ul><li><strong>Úzká pata:</strong> zvolte model s měkčím hrdlem a pevnějším zadním dílem, případně šněrování, které se dá utáhnout až k patě.</li>'
          '<li><strong>Široké předonoží:</strong> hledejte širší špičku, zkuste modely značek, které nabízejí více šířek.</li>'
          '<li><strong>Vyšší nárt:</strong> boty s lehkým jazykem a více očky nad klenbou netlačí.</li>'
          '<li><strong>Otoky nohou:</strong> pružný textil nebo síťovina se chová příjemněji než pevná kůže.</li></ul>'
          '<p>Při zkoušce se projděte a sledujte patu. Pokud při kroku sjíždí nahoru, bota je velká nebo má špatný tvar hrdla. Prsty se musí mírně rozevřít, ale nesmí narážet do špičky při chůzi ze schodů.</p>'
          '<h2>Značky v nabídce a jejich charakter</h2>'
          '<p>Nabídka dámských tenisek zahrnuje velké sportovní značky i módnější a komfortnější výrobce. Každá má vlastní střih a cílovou skupinu: '
          + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('new-balance', 'New Balance'), ('asics', 'Asics')) + ' vycházejí ze sportovní tradice, '
          + B(('converse', 'Converse'), ('vans', 'Vans')) + ' ze skate a plátěné klasiky, '
          + B(('skechers', 'Skechers'), ('geox', 'Geox'), ('rieker', 'Rieker')) + ' hlavně z komfortu a vycházkové obuvi.</p>'
          '<h3>Sportovní značky</h3>'
          '<p>Nike nabízí v dámské řadě nízké kožené kousky podobné základní klasice i lehké běžecké siluety, a proto ho zvolíte, když chcete rozpoznatelný vzhled s širokou paletou barev. Adidas staví na třech proužcích a retro modelech, které se nosí k džínám i legínám. Puma se věnuje platformám a nízkým silným podešvím, New Balance a Asics se zaměřují na pohodlí a více šířek u řady modelů.</p>'
          '<h3>Plátno a skate styl</h3>'
          '<p>Converse a Vans mají ploché podešve, textilní nebo semišové svršky a málo tlumení. Hodí se na kratší chůzi, léto a styl bez sportovního podtextu. Kdo chodí hodně, přidá si samostatnou měkkou vložku nebo zvolí jiný typ boty.</p>'
          '<h3>Komfortní značky</h3>'
          '<p>Skechers se soustředí na měkké stélky a lehké pěnové podešve, takže jsou oblíbené u lidí, kteří stojí v práci celý den. Geox používá prodyšnou podešev a nese si pověst vycházkových bot pro dlouhý den ve městě. Rieker nabízí lehké, často šněrovací nebo slip-on modely, které se obouvají rychle a hodí se i na zhoršený nárt.</p>'
          '<h2>Materiály a péče</h2>'
          '<p>Kůže vydrží a časem se přizpůsobí noze, ale nesnáší dlouhé promočení. Textil a síťovina dobře dýchají, ale v dešti nasáknou a hůř se čistí. Syntetické materiály odolají vodě, jen pod nimi může být tepleji. Semiš vypadá jemně, ale vyžaduje impregnaci a kartáček.</p>'
          '<ul><li>Bílé podrážky omyjte hned po použití, špína se do gumy vtlačí a pak jde hůř.</li>'
          '<li>Boty sušte při pokojové teplotě, ne na radiátoru, který lepené spoje vysuší a svršek zdeformuje.</li>'
          '<li>Vkládací stélky pravidelně vyndavejte a nechte vyschnout, snižuje to zápach.</li>'
          '<li>Střídejte dva páry, pěna se mezi nošeními zotaví.</li></ul>'
          '<h2>Jak koupit dámské tenisky bez zbytečných kompromisů</h2>'
          '<p>Nejdřív určete hlavní použití: kancelář, chůze po městě, cestování nebo sport v lehčím tempu. Podle toho zvolte buď tenký klasický model, nebo měkčí vycházkový pár. Potom zvolte barvu, která se hodí k většině oblečení. Bílá a béžová jsou univerzální, černá nejméně špiní, růžové a pastelové tóny jsou výrazné a hodí se k jednobarevnému outfitu.</p>'
          '<p>Na Sportece porovnáte u stejného modelu více obchodů najednou a hned vidíte, zda je vaše číslo skladem. Podobné modely lze snadno srovnat i s teniskami z jiných výběrů, například <a href="/damska-sportovni-obuv/">dámskou sportovní obuví</a>, <a href="/bezecke-boty-damske/">dámskými běžeckými botami</a> nebo <a href="/barefoot-boty-damske/">dámskými barefoot botami</a>. Pro chladnější období je lepší sáhnout po <a href="/damske-zimni-boty/">zimních botách</a>, tenisky se hodí hlavně od jara do podzimu.</p>'
          '<h2>Další výběry tenisek</h2>'
          '<p>Hledáte konkrétní značku? Otevřete <a href="/new-balance-tenisky/">New Balance</a>, <a href="/puma-tenisky/">Puma</a>, <a href="/rieker-tenisky/">Rieker</a>, <a href="/tenisky-vans/">Vans</a>, <a href="/converse-tenisky/">Converse</a>, <a href="/tenisky-geox/">Geox</a> nebo <a href="/asics-tenisky/">Asics</a>. Stejnou značku najdete také v přehledu <a href="/znacka/nike/">Nike</a> a <a href="/znacka/skechers/">Skechers</a>.</p>'
          '<h2>Na co si dát pozor</h2>'
          '<p>Barvu a design často diktuje móda, ale pohodlí ne. Obuv s nevhodným tlumením vás po několika hodinách začne bolet v plosce a pod patou. Ploché podešve s minimální oporou nepoužívejte jako jedinou obuv na celý den, pokud máte problémy s klenbou. Pokud noha při chůzi padá dovnitř nebo ven, poraďte se v obchodě s funkční obuví.</p>',
    faq=[
        ('Čím se dámské tenisky liší od pánských?', 'Mají užší patu a štíhlejší předonoží, často měkčí pěnu a lehčí stavbu. Číslo na krabici se mezi značkami liší, proto si ověřte vlastní délku chodidla podle tabulky výrobce.'),
        ('Jaké tenisky vybrat na celodenní chůzi?', 'Zvolte model s měkčí pěnovou mezipodešví, lehkou konstrukcí a prodyšným svrškem. Skechers, Geox nebo běžecký styl značek Nike, Adidas a New Balance se na dlouhý den obvykle hodí víc než tenká plátěná podešev.'),
        ('Jak poznám správnou velikost?', 'Změřte chodidlo večer, přičtěte půl až celý centimetr před prsty a porovnejte s tabulkou výrobce. Pata nesmí sjíždět nahoru a špička nesmí při chůzi ze schodů narážet do předku boty.'),
        ('Jsou platformové tenisky pohodlné?', 'Záleží na ohebnosti podešve. Pokud se v místě prstů ohýbá, chůze je přirozená. Pevná a těžká platforma se hodí na krátké vzdálenosti, na celodenní nošení méně.'),
        ('Kterou barvu zvolit, aby se hodila ke všemu?', 'Bílá a béžová ladí s většinou oblečení, ale špiní se rychleji. Černá je praktická a nenápadná, šedá je kompromis. Výraznější barvy jsou vhodné, pokud zbytek outfitu držíte jednobarevný.'),
        ('Mohu v teniskách běhat?', 'Lifestylové tenisky nejsou na běh určené, protože mívají méně tlumení a jinou stavbu. Pro pravidelný běh zvolte běžecké boty. Na svižnou chůzi a rekreační pohyb ale městské tenisky bez potíží stačí.'),
        ('Jak vyčistit bílé tenisky?', 'Povrch otřete vlhkým hadříkem, skvrny odstraňte jemným mýdlem a kartáčkem. Podrážku omyjte hned po špinavé cestě. Neperte je v pračce na vysoké teplotě, lepené spoje by mohly povolit.'),
        ('Jaké tenisky na jaro a podzim?', 'Vhodné jsou modely z kůže nebo syntetiky, které snesou vlhko, případně s impregnací. V chladnějším počasí je lepší hrubší ponožka a boty o půl čísla větší. Na zimu používejte zimní obuv s pevnější podešví.'),
        ('Hodí se tenisky do kanceláře?', 'Ano, pokud firma nemá přísný dress code. Nejlépe sedí minimalistické kožené nebo semišové nízké modely v neutrální barvě, bez výrazného potisku a bez zářivé podrážky.'),
        ('Co dělat, když mě tenisky tlačí na palec?', 'Zkuste širší model nebo značku s více šířkami. Pomůže i jiné šněrování, které uvolní nárt. Pokud tlak trvá i po rozchození, boty vyměňte, dlouhodobý tlak vede k otlakům a deformacím.'),
    ],
)

# ------------------------------------------------------------------ nike-tricko
NEW['nike-tricko'] = dict(
    title='Nike tričko: řady Dri-FIT, Sportswear a Pro',
    desc='Nike trička na trénink, běh i každý den. Rozdíl mezi řadami Dri-FIT, Sportswear, Pro a Academy, střihy, velikosti a péče. Porovnejte nabídky v obchodech.',
    intro='<p>Nike tričko není jeden produkt, ale několik řad se zcela jiným určením. Dri-FIT na trénink je lehký a rychleschnoucí, Sportswear Club je bavlněný základ do města, Pro přiléhá k tělu jako druhá vrstva a Academy nebo Park cílí na týmové sporty. Značka se zaměřuje na sport, ale střihy a loga jsou tak rozpoznatelné, že se nosí i na ulici. '
          'Na stránce jsou trička a tílka značky Nike z kategorie <a href="/sportovni-tricka/">sportovních triček</a>, pánská, dámská i dětská. Průvodce vysvětluje, jak se liší jednotlivé řady, jaký materiál zvolit na jakou aktivitu, jak sedí střihy a jak tričko prát, aby barva i potisk vydržely. '
          'Další značkové výběry najdete u <a href="/adidas-tricko/">Adidas</a>, <a href="/under-armour-tricko/">Under Armour</a> a <a href="/jordan-tricko/">Jordan</a>.</p>',
    guide='<h2>Jak se liší řady Nike triček</h2>'
          '<p>Při pohledu na nabídku zaujme, že názvy řad nesou informaci o určení. Dobře to vidíte i podle toho, co obchody uvádějí v názvu: Dri-FIT, Sportswear, Pro, Academy, Park, Miler, Legend nebo Challenge. Každá řada má jiný materiál, střih a sezonu používání.</p>'
          + T(['Řada', 'Charakter', 'Kdy ji zvolit'], [
              ['Dri-FIT', 'polyesterová technická pletenina, která odvádí pot od těla, rychle schne', 'běh, posilovna, tréninky, teplé dny'],
              ['Sportswear Club a Essential', 'bavlněná nebo bavlněná směsná pletenina, volnější střih, často s logem na hrudi', 'město, škola, volný čas, cesty'],
              ['Pro', 'přiléhavý elastický materiál, často se používá jako první vrstva', 'trénink v chladu pod mikinu, kompresní styl'],
              ['Academy, Park, Challenge', 'týmové sportovní střihy, lehký polyester', 'fotbal, florbal, šatna, trénink v kolektivu'],
              ['Miler a Legend', 'běžecký a univerzální trénink, rychlé schnutí, často reflexní prvky', 'běh, kondiční tréninky'],
          ])
          + '<p>Dri-FIT je označení technologie Nike pro polyesterové tkaniny odvádějící vlhkost. Nejde o jedno konkrétní tričko, nýbrž o celou rodinu materiálů, a proto se tloušťka a pocit na kůži mezi modely liší. Cokoli, co je z poctivé bavlny, patří do volnočasové řady a při intenzivním cvičení nasákne.</p>'
          '<h2>Pro koho které tričko sedí</h2>'
          '<p>Nike nabízí trička pro muže, ženy i děti. Pánské modely mají širší ramena a rovnější linii, dámské jsou v pase užší a často kratší. U zkrácených a cropped střihů je prostor mezi hrudníkem a pasem, který se hodí k legínám s vyšším pasem, viz <a href="/nike-leginy/">Nike legíny</a>. Dětská trička mívají jednoduchou stavbu, měkké štítky a kratší délku.</p>'
          '<ul><li><strong>Tréninkové pánské:</strong> přiléhavější nebo klasické, s ventilací v zádech.</li>'
          '<li><strong>Dámské tílko a top:</strong> pro cvičení s podprsenkou, hodí se k <a href="/tilka/">tílkům a topům</a>.</li>'
          '<li><strong>Dětské:</strong> větší rezerva na růst, bavlněná směs pro každodenní nošení.</li>'
          '<li><strong>Oversize:</strong> volnější střih ve stylu streetwearu, často z těžší bavlny.</li></ul>'
          '<h2>Střih a velikost</h2>'
          '<p>Nike má různou stavbu u různých řad. Tréninkové modely sedí přiléhavěji než městské, ale to neznamená, že jsou těsné. Sportswear Club je střižen volněji a na delší zadní díl se dá spolehnout. Řada Pro si vyžaduje opravdu menší číslo než ostatní, jinak ztrácí kompresi. Pokud váháte, porovnejte šířku v ramenou a délku s tričkem, které vám sedí, a ne jen s číslem na štítku.</p>'
          '<p>Při vrstvení pod mikinu zvolte volnější střih. Při běhu naopak přiléhavý model, který nešmrdlá a nedře v podpaží. Tričko s reflexními prvky se hodí na večerní běh, protože výrazná barva zvyšuje viditelnost na silnici. U dlouhých triček platí, že delší zadní díl chrání ledviny při předklonu.</p>'
          '<h2>Nike tričko do města a na sport</h2>'
          '<p>Značka se dobře hodí do kombinací, protože loga jsou výrazná, ale nikoli rušivá. Černé a bílé tričko je nejuniverzálnější, šedá se hodí k jakékoli barvě a modrá nebo červená dodá barevný akcent. Do města zvolte bavlněnou Club řadu, na kolo nebo běh Dri-FIT.</p>'
          '<p>Tričko Nike můžete kombinovat s <a href="/nike-kratasy/">kraťasy</a>, <a href="/nike-teplaky/">tepláky</a> nebo <a href="/nike-mikina/">mikinou</a> a vytvořit sladěný outfit. Jestliže hledáte tričko jiné značky, podívejte se na <a href="/tricko-puma/">Puma</a>, <a href="/mizuno-tricko/">Mizuno</a> nebo <a href="/panska-tricka/">pánská trička</a> obecně a na <a href="/funkcni-tricka-damska/">dámská funkční trička</a>.</p>'
          '<h2>Materiál a péče</h2>'
          '<p>Technické polyesterové tričko perte při nízké teplotě, bez aviváže, která zalepí vlákna a zhorší odvod potu. Bavlněné tričko snese vyšší teplotu, ale potisk i logo perte naruby, ať se tolik neotírají. Sušte přirozeně, sušička způsobuje žmolky a u potisku praskání.</p>'
          '<ul><li>Pot a pach: tričko po cvičení nenechávejte vlhké v tašce, vypněte ho na pověšení.</li>'
          '<li>Skvrny: ošetřete je před praním, ne až po něm.</li>'
          '<li>Žehlení: potisk nežehlete přímo, tričko otočte naruby.</li>'
          '<li>Barvy: tmavé a světlé perte zvlášť, aby světlé nezešedly.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Stejné tričko má často více barevných variant a mnoho obchodů ho prodává pod jiným názvem. Sledujte kód nebo název řady, ne jen obrázek. Na Sportece vidíte, ve kterých obchodech je skladem vaše velikost, a snadno srovnáte i sezónní kousky se slevou. Nabízené jsou i věci pro vodu a plavání, ale ty najdete v samostatné kategorii.</p>'
          '<h2>Co dalšího hledat u značky Nike</h2>'
          '<p>V širší nabídce značky najdete také <a href="/polokosile/">polokošile</a>, <a href="/funkcni-tricka/">funkční trička</a> a oblečení pro volný čas. Přehled všech produktů je na stránce <a href="/znacka/nike/">Nike</a>.</p>'
          '<p>Pro lepší představu: tričko pro běh vyberte lehké a prodyšné, pro kolektivní sporty zvolte řadu s týmovým střihem a pro každý den bavlněnou základní řadu.</p>',
    faq=[
        ('Co znamená Dri-FIT na tričku Nike?', 'Je to označení materiálu, který odvádí pot od těla a rychle schne. Nejde o jednu tkaninu, ale o skupinu polyesterových materiálů, takže pocit a tloušťka se mezi modely liší. Najdete ho u tréninkových řad.'),
        ('Jaký je rozdíl mezi Sportswear a Dri-FIT?', 'Sportswear je volnočasová řada, většinou z bavlny, ve volnějším střihu. Dri-FIT je technický polyester určený na pohyb. Pro sport zvolte druhou, pro každodenní nošení první.'),
        ('Sedí Nike trička větší, nebo menší?', 'Záleží na řadě. Sportswear Club sedí volněji, tréninkové řady mírně přiléhavěji a Pro velmi těsně. Pro jistotu porovnejte šířku ramen a délku s vlastním tričkem a nespoléhejte na štítek.'),
        ('Je Nike tričko vhodné na běh?', 'Ano, pokud je to technický model, například Dri-FIT Miler nebo Legend. Bavlněné trička nejsou na běh ideální, protože nasáknou potem a otírají.'),
        ('Jak prát tričko s potiskem?', 'Naruby, při nízké teplotě a s jemným prostředkem. Nepoužívejte aviváž a vyhněte se sušičce. Žehlete naruby a nikdy přímo na potisk, jinak může zvlnit nebo popraskat.'),
        ('Hodí se Nike tričko pro děti?', 'Ano, nabídka zahrnuje dětské a juniorské velikosti. Pro každodenní hraní zvolte bavlněnou směs, na sport lehčí technickou pleteninu. Kupujte s malou rezervou, děti rychle rostou.'),
        ('Čím se liší tílko od trička Nike?', 'Tílko je bez rukávů, hodí se do tepla, k cvičení a pod volné oblečení. Tričko krátí rukáv a chrání ramena před sluncem. Pro posilovnu vybírejte podle pohybu paží a tření ramínek o batoh.'),
        ('Co je řada Nike Pro?', 'Je to přiléhavý střih, často z pružné pleteniny, který slouží jako první vrstva. Používá se pod mikinou nebo jako samostatné tréninkové tričko. Vyžaduje přesnou velikost, jinak se ztrácí efekt přilnutí.'),
        ('Jak poznám originál Nike?', 'Kupujte v ověřených obchodech, ne od neznámých prodejců. Sledujte kvalitu švů, štítek s materiálem a číslo modelu. Zjevně nízká cena u novinky bývá varováním, ne výhodou.'),
        ('Kdy se Nike trička slevují?', 'Častěji na konci sezony, při výprodejích starších řad a kolekčních změnách. Slevu poznáte porovnáním cen u více obchodů a sledováním historie nabídky, ne podle přeškrtnuté ceny.'),
    ],
)

# ------------------------------------------------------------------ damske-teplaky
NEW['damske-teplaky'] = dict(
    title='Dámské tepláky: střihy, materiály a pohodlí na každý den',
    desc='Dámské tepláky se střihem pro ženské boky a pas. Jogger, straight, oversize i tepláková souprava. Jak vybrat materiál a velikost a porovnat obchody.',
    intro='<p>Dámské tepláky se od pánských liší hlavně střihem v pase, na bocích a v délce nohavic. U žen bývá rozdíl mezi obvodem pasu a boků výraznější, proto stejná velikost na ženské postavě sedí jinak než na mužské. Do nabídky patří klasické jogger kalhoty s manžetou, rovné tepláky, volné oversize modely, tenké letní kousky i tepláky zateplené fleecem. '
          'Na této stránce vidíte tepláky z kategorie <a href="/teplaky/">tepláky</a>, které jsou určené ženám. Průvodce popisuje, jak se střih liší, jak zvolit materiál podle počasí a aktivity, jak určit délku nohavic a jak tepláky prát, aby se nežmolkovaly. '
          'Pokud hledáte i horní díl, přejděte na <a href="/damska-mikina/">dámské mikiny</a>, <a href="/soupravy/">soupravy</a> nebo <a href="/damske-leginy/">dámské legíny</a>.</p>',
    guide='<h2>Dámský střih tepláků</h2>'
          '<p>Hlavní rozdíl je v poměru pasu, boků a stehen. Dámský střih bývá užší v pase, širší na bocích a kratší v rozkroku. Dobré tepláky pro ženy mají pružný pás, který sedí na pase nebo mírně pod ním, a materiál v zadní části, který nepřitahuje pozornost vypouklinami. Kdo se vejde do pánských, často zjistí, že je pas příliš volný a nohavice moc dlouhé.</p>'
          + T(['Střih', 'Jak vypadá', 'Hodí se na'], [
              ['Jogger', 'zúžené nohavice s manžetou u kotníku', 'trénink, město, kombinace se sportovními botami'],
              ['Straight (rovné)', 'stejná šířka od kolene dolů, bez manžety', 'doma, do práce s uvolněným stylem, k teniskám'],
              ['Wide leg a barelové', 'volné nohavice, často od boků široké', 'streetwear, pohodlí, nošení s mikinou'],
              ['Oversize', 'celkově volný střih, často se šňůrkou', 'domácí pohodlí, odpočinek, módní styl'],
              ['Slim a přiléhavé', 'blízko těla, strečová pletenina', 'jóga, posilovna, pohyb bez překážení'],
              ['Tepláková souprava', 'mikina i kalhoty ve stejném materiálu a barvě', 'cesty, letiště, komplet na doma'],
          ])
          + '<p>Šířka nohavic ovlivňuje i volbu obuvi. Úzké modely vypadají dobře k teniskám a sportovním botám, rovné a široké snesou i vyšší obuv nebo sandály. Pokud nosíte tepláky ke zkrácenému topu, vyšší pas zvýrazní talii a nezvedá se při chůzi.</p>'
          '<h2>Materiály podle počasí a aktivity</h2>'
          '<ul><li><strong>Bavlněný úplet:</strong> měkký a příjemný na kůži, hodí se do bytu a na každý den, při potu těžkne.</li>'
          '<li><strong>Směs bavlny a polyesteru:</strong> drží tvar, méně se mačká a rychleji schne. Je to nejrozšířenější materiál na každodenní tepláky.</li>'
          '<li><strong>Polyester s elastanem:</strong> lehký, pružný a technický, vhodný na trénink a pohyb.</li>'
          '<li><strong>Froté a fleece zevnitř:</strong> hřeje v chladu, ale v bytě se v něm snadno přehřejete.</li>'
          '<li><strong>Tenká pletenina nebo viskóza:</strong> na léto a lehké kombinace, často s elegantnějším vzhledem.</li></ul>'
          '<p>Gramáž prozradí sezonu. Lehká teplákovina se nosí na jaro a léto, střední na většinu roku a těžká na zimu. Teplákovina nechrání před větrem a deštěm, proto v zimě venku přidejte větrovku, případně termoprádlo pod tepláky. Pokud tepláky nosíte i pro sport, zvolte materiál s elastanem a bez těžké bavlny.</p>'
          '<h2>Velikost, délka a pas</h2>'
          '<p>Změřte obvod pasu a boků a porovnejte je s tabulkou výrobce. Pokud se hodnoty pohybují mezi dvěma čísly, rozhodněte podle toho, zda chcete přiléhavý, nebo volný dojem. U oversize modelů se vybírá menší velikost, než jste zvyklá, jinak nohavice a sedák působí příliš objemně.</p>'
          '<p>Nohavice mají končit u kotníku, případně mírně nad botou. U modelů s manžetou se délka dá nabrat, rovné tepláky bez manžety se musí koupit v odpovídající délce. Vyšší ženy často hledají variantu s delším vnitřním švem, malé ženy si rovné modely zkrátí nebo zvolí jogger.</p>'
          '<p>Pas se šňůrkou umožní upravit velikost při změně objemu. Plochá guma je hladší pod tričkem, ale hůř drží, pokud kalhoty ztratily pružnost. Kapsy na zip uloží klíče, boční šité kapsy se hodí pro ruce. Zadní kapsa se hodí na kartu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V nabídce dámských tepláků jsou sportovní značky i módnější a fitness výrobci: '
          + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('fila', 'Fila'), ('champion', 'Champion'), ('4f', '4F')) + ' vycházejí ze sportu. '
          + B(('gap', 'Gap'), ('guess', 'Guess')) + ' jsou spíše módní a městské, '
          + B(('gymbeam', 'GymBeam')) + ' cílí na fitness a posilovnu.</p>'
          '<h3>Sportovní tradice</h3>'
          '<p>Adidas je typický třemi proužky na boku a velmi rozpoznatelnou siluetou, Puma často využívá velké logo a retro střih, Under Armour sází na technické materiály a pohyb a Fila nese retro estetiku. Champion je spojen s klasickými mikinami a kalhotami z těžší bavlny.</p>'
          '<h3>Městský styl a fitness</h3>'
          '<p>Gap a Guess nabízejí tepláky jako součást běžného vzhledu, nikoli čistě sportovní vybavení. GymBeam se zaměřuje na lidi, kteří cvičí a potřebují pružný materiál, který se nesklouzává. Tyto modely se pak snadno kombinují s legínami a tílky.</p>'
          '<h2>Jak tepláky kombinovat a pečovat o ně</h2>'
          '<p>Základem je jednoduchost. Tepláky zvolené v neutrální barvě sedí k bílému tričku, mikině i bundě. Šedá je univerzální, černá se nejméně špiní, béžová a hnědá se nosí ve spojení s teplými tóny. Pokud nosíte oversize tepláky, doplňte je přiléhavým topem, aby postava nezmizela.</p>'
          '<ul><li>Perte naruby při nízké teplotě, snižuje se tak tvorba žmolků.</li>'
          '<li>Nepoužívejte aviváž u technických materiálů, zalepí vlákna.</li>'
          '<li>Sušte přirozeně nebo při nízké teplotě, tvar a elastan vydrží déle.</li>'
          '<li>Při potu nenechávejte tepláky ve vlhké tašce, zapáchají.</li></ul>'
          '<h2>Další oblečení a výběry</h2>'
          '<p>Chcete-li se podívat na značky, přejděte na <a href="/nike-teplaky/">Nike tepláky</a>, <a href="/adidas-teplaky/">Adidas tepláky</a>, <a href="/under-armour-teplaky/">Under Armour tepláky</a>, <a href="/teplaky-puma/">Puma tepláky</a>, <a href="/guess-teplaky/">Guess</a> nebo <a href="/champion-teplaky/">Champion</a>. Pro pány a děti jsou stránky <a href="/panske-teplaky/">pánské</a> a <a href="/detske-teplaky/">dětské tepláky</a>. Pokud hledáte pohyblivější kalhoty, otevřete <a href="/damske-sportovni-kalhoty/">dámské sportovní kalhoty</a>.</p>'
          '<p>Na Sportece u každého páru vidíte více obchodů, které mají stejný model, a zda je vaše velikost skladem.</p>',
    faq=[
        ('Čím se dámské tepláky liší od pánských?', 'Mají užší pas, širší boky, kratší rozkrok a často kratší nohavice. Pánské modely mají rovnější linii, takže ženě v pase často vlají a nohavice jsou dlouhé.'),
        ('Jaký střih tepláků vybrat na každý den?', 'Nejuniverzálnější je jogger nebo rovný střih z bavlněné směsi ve střední gramáži. Dobře drží tvar, nezamotává se při chůzi a kombinuje se s tričkem, mikinou i teniskami.'),
        ('Jaký materiál je nejlepší na sport?', 'Lehký polyester s elastanem, který odvádí pot a pružně sleduje pohyb. Bavlna se hodí do bytu a na odpočinek, při tréninku nasákne a pomalu schne.'),
        ('Jak vybrat velikost, když jsem mezi čísly?', 'Rozhodněte podle střihu. U přiléhavých modelů zvolte větší, u oversize menší. Porovnejte obvod boků s tabulkou výrobce, protože pas se dá upravit šňůrkou.'),
        ('Co jsou barelové a wide leg tepláky?', 'Barelové mají objemné nohavice zúžené u kotníku, wide leg jsou široké po celé délce. Oba střihy se nosí volně, hodí se do města a ke krátké mikině.'),
        ('Hřejí tepláky dostatečně v zimě?', 'Zateplené s fleecem uvnitř ano, ale chrání jen před chladem, ne před větrem. Venku přidejte větrovku nebo kalhoty přes ně, případně termoprádlo pod tepláky.'),
        ('Jak zabránit žmolkům?', 'Perte naruby při nízké teplotě, bez aviváže a s podobnými tkaninami. Nesušte v sušičce. Žmolky vznikají třením, proto pomáhá i méně častá výměna povrchu a hrubší látky nepráním dohromady.'),
        ('Kdy zvolit teplákovou soupravu?', 'Pokud chcete jednotný vzhled na cesty, doma nebo na lehký trénink. Hodí se i jako dárek, protože barvy a střih jsou sladěné. Horní díl lze nosit samostatně.'),
        ('Mohu tepláky nosit do práce?', 'Záleží na pravidlech. V uvolněném prostředí funguje rovný střih z pevnější směsi v tmavé barvě s bílým tričkem nebo lehkým svetrem. Klasický sportovní jogger s logem se do práce nehodí.'),
        ('Jak dlouho tepláky vydrží?', 'Při šetrném praní několik sezón. Nejdřív se ošoupou kolena, vnitřní strana stehen a manžety. Kvalitnější směs a hustší pletenina vydrží déle než levná tenká bavlna.'),
    ],
)

# ------------------------------------------------------------------ sandaly-keen
NEW['sandaly-keen'] = dict(
    title='Sandály Keen: Newport, Clearwater, Hyperport a další modely',
    desc='Sandály Keen s uzavřenou špičkou na túry, vodu i cestování. Rozdíl mezi modely Newport, Clearwater, Hyperport, Elle a Seacamp, velikosti a péče.',
    intro='<p>Sandály Keen jsou specifické tím, že většina modelů má chráněnou špičku. Značka z Ameriky je známá pro takzvané hybridní sandály: nemají jen tenké pásky, ale kombinují prodyšný svršek s gumovým ochranným lemem, který kryje prsty před kameny a kořeny. Hodí se do vody, na túru, na dovolenou i na procházky po městě. '
          'Stránka vychází z kategorie <a href="/sandaly/">sportovních sandálů</a> a ukazuje jen sandály Keen, pánské, dámské i dětské. Průvodce vysvětluje rozdíly mezi hlavními modely, jak vybrat velikost, jak se sandály chovají ve vodě a čím se liší od jiných značek. '
          'Pokud chcete porovnat i další značky, otevřete <a href="/teva-sandaly/">Teva</a>, <a href="/merrell-sandaly/">Merrell</a> nebo <a href="/sandaly-columbia/">Columbia</a>.</p>',
    guide='<h2>V čem jsou sandály Keen jiné</h2>'
          '<p>Sportovní sandál obvykle odkrývá celé chodidlo a chrání jen podešev. Keen sází na uzavřenou nebo částečně uzavřenou špičku. Gumový lem před prsty snižuje riziko úderu o kámen a při brodění chrání před klouzáním po kamenech. Tvar špičky je obvykle širší, takže prsty mají víc místa, což ocení lidé s širším předonožím.</p>'
          '<p>Sandály se obvykle upínají pásky nebo šňůrkou kolem kotníku, takže nesklouzávají při chůzi z kopce. Stélka bývá tvarovaná a podešev má vzorek, který drží na mokrém povrchu. Právě tato kombinace činí sandály vhodné pro lidi, kteří chtějí trochu více než klasický otevřený sandál, ale nechtějí těžké trekové boty.</p>'
          '<h2>Modely v nabídce</h2>'
          + T(['Model', 'Pro koho', 'Charakter'], [
              ['Newport H2', 'muži, děti a mládež', 'klasický hybridní sandál s uzavřenou špičkou, vhodný do vody i na túru'],
              ['Clearwater CNX', 'muži', 'šňůrkový systém, lehčí a prodyšnější, vodní využití'],
              ['Hyperport H2', 'muži, ženy, děti', 'sportovnější a lehčí varianta s pásky a výraznou podešví'],
              ['Targhee III', 'muži', 'otevřený terénní sandál s pevnější podešví, inspirovaný trekovou botou'],
              ['Rapids H2', 'muži', 'lehčí sportovní sandál pro vodu a pohyb'],
              ['Elle a Whisper', 'ženy', 'dámské sandály s pásky a lehkou konstrukcí, více městské'],
              ['Seacamp II CNX', 'děti a mládež', 'dětský sandál s šňůrkou, uzavřená špička, barevné varianty'],
          ])
          + '<p>Názvy modelů se prodávají v mnoha barevných provedeních a obchody je uvádějí různě. Sledujte proto kód nebo přesný název a nezaměňujte pánský model s dětským, protože střih a velikostní řada se liší.</p>'
          '<h2>Pro koho se hodí</h2>'
          '<h3>Muži</h3>'
          '<p>Pánské Newport a Clearwater jsou tradiční modely pro vodu, jízdu na lodi nebo dovolenou, Targhee je terénní kousek bližší trekové botě. Pokud plánujete delší chůzi s batohem, hledejte pevnější podešev a stabilní uchycení paty.</p>'
          '<h3>Ženy</h3>'
          '<p>Dámské Elle a Whisper jsou lehčí a štíhlejší, hodí se na procházky, cestování a každodenní nošení. Hyperport H2 je výraznější sportovní model. Zvažte, zda chcete model do vody, nebo pohodlný sandál na delší chůzi po městě.</p>'
          '<h3>Děti</h3>'
          '<p>Dětské Newport, Seacamp a Hyperport patří mezi oblíbené letní boty pro hřiště, tábor a výlety. Uzavřená špička chrání při běhání, gumová podešev drží na mokrých kamenech. Děti rychle rostou, proto kupujte s malou rezervou a velikost kontrolujte před každou sezonou. Přehled dětských modelů najdete také v <a href="/detske-sportovni-sandaly/">dětských sportovních sandálech</a>.</p>'
          '<h2>Velikost a sedání</h2>'
          '<p>Chodidlo při teple otéká, proto sandály zkoušejte odpoledne. Prsty by měly mít malou rezervu a nesmí přesahovat okraj stélky. Pata nemá sjíždět dopředu a pásek přes nárt se má dát utáhnout bez tlaku. Pokud noha v sandálu klouže, zvolte menší číslo nebo model s pevnějším zapínáním.</p>'
          '<ul><li>Široké předonoží se v těchto modelech obvykle cítí lépe než v úzkých sandálech jiných značek.</li>'
          '<li>Úzká pata potřebuje pásek, který se dá pevně dotáhnout.</li>'
          '<li>Na dlouhé túry zvažte ponožky a zkoušejte s nimi.</li>'
          '<li>Při koupi pro děti zvolte suchý zip nebo šňůrku, kterou zvládnou samy upravit.</li></ul>'
          '<h2>Voda, bláto a zápach</h2>'
          '<p>Syntetické pásky a pěnová stélka dobře snášejí vodu a rychle schnou. Po koupání v moři opláchněte sandály sladkou vodou, sůl a písek jinak drhnou. Případný zápach pomůže odstranit vlažná voda s jemným mýdlem a důkladné vysušení na vzduchu mimo přímé slunce.</p>'
          '<p>Pěnové vložky nikdy nesušte na radiátoru ani v troubě, deformují se a ztrácejí tlumení. Pokud sandály nosíte bez ponožek, otírejte vnitřek častěji a občas je nechte vyschnout na vzduchu.</p>'
          '<h2>Srovnání s jinými značkami</h2>'
          '<p>Teva je klasikou páskových sandálů, Merrell nabízí kombinaci sandálů a lehké obuvi, Columbia se zaměřuje na outdoorové použití a Crocs na lehkou pěnovou obuv. Keen vyniká ochranou špičky a stabilním, zavřenějším střihem, kdežto jiné značky se spíš zaměřují na otevřený a lehký sandál. Podívejte se i na <a href="/sandaly-crocs/">Crocs</a> a <a href="/birkenstock-sandaly/">Birkenstock</a>, pokud hledáte pohodlí na každý den.</p>'
          '<h2>Co další hledat</h2>'
          '<p>Značka vyrábí i boty. Pro delší túry se podívejte na <a href="/keen-trekove-boty/">Keen trekové boty</a>, pro pobyty u vody na <a href="/obuv-do-vody/">obuv do vody</a> a pro volný čas na <a href="/pantofle-a-zabky/">pantofle a žabky</a>. Přehled všech produktů je na stránce <a href="/znacka/keen/">Keen</a>. Obecné sandály pro ženy a muže jsou v <a href="/damske-sportovni-sandaly/">dámských</a> a <a href="/panske-sportovni-sandaly/">pánských sportovních sandálech</a>.</p>'
          '<p>Na Sportece porovnáte u každého modelu obchody a zjistíte, zda je vaše číslo skladem. Nezapomeňte, že stejné jméno modelu mívá více barev a každá může mít jinou dostupnost.</p>',
    faq=[
        ('Čím se sandály Keen liší od ostatních?', 'Většina modelů má chráněnou špičku s gumovým lemem, nastavitelné pásky a podešev s protiskluzovým vzorkem. Prsty jsou chráněné před nárazem a chodidlo drží stabilně i v terénu.'),
        ('Hodí se Keen sandály na túru?', 'Ano, na lehčí túry v suchém terénu a u vody. Pro náročné trasy s těžkým batohem a skalnatým terénem je lepší zvolit trekovou obuv, sandály nedrží kotník.'),
        ('Který model Keen zvolit do vody?', 'Newport H2, Clearwater CNX nebo Hyperport H2 jsou postavené pro vodu. Syntetické pásky rychle schnou a podešev drží na mokrých kamenech. Po koupání opláchněte sandály sladkou vodou.'),
        ('Jsou sandály Keen pohodlné pro široké chodidlo?', 'Většina modelů má širší špičku a nastavitelné pásky, takže je v nich víc místa než v úzkých sandálech. Přesto prsty před koupí vyzkoušejte, každý model sedí trochu jinak.'),
        ('Jak vybrat velikost pro děti?', 'Změřte chodidlo a přičtěte malou rezervu, přibližně půl centimetru až centimetr. Děti rychle rostou, takže velikost kontrolujte před sezonou. Suchý zip nebo šňůrka pomohou s doladěním sedu.'),
        ('Jak čistit sandály Keen?', 'Opláchněte je vlažnou vodou, jemným mýdlem a kartáčkem odstraňte bláto. Sušte přirozeně mimo přímé slunce a radiátor. Stélku můžete vyndat, pokud jde, a nechat ji vysušit zvlášť.'),
        ('Proč sandály zapáchají?', 'Pot a vlhkost se zachytávají ve stélce a v syntetických materiálech. Pomůže pravidelné mytí, dokonalé sušení a občasné vyndání stélky. Nosit je bez ponožek je příjemné, vyžaduje ale častější péči.'),
        ('Mohu Keen sandály nosit každý den?', 'Ano, mnoho lidí je nosí na cesty, procházky a do města. Pro celodenní nošení zvolte model s měkčí stélkou a dobře dotaženými pásky. Při větší zátěži dopřejte nohám změnu obuvi.'),
        ('Jaké jsou rozdíly mezi Newport a Hyperport?', 'Newport je klasický hybridní sandál s uzavřenou špičkou a pevnější konstrukcí, Hyperport je sportovnější a lehčí. Pro delší procházku zvolte Hyperport, pro vodu a terén Newport.'),
        ('Kdy se Keen sandály slevují?', 'Nejčastěji na konci léta a u starších barevných variant. Slevu poznáte, když porovnáte stejný model ve více obchodech. Na Sportece to uvidíte najednou, včetně dostupných velikostí.'),
    ],
)


# ---- extra sections (appended to the guides)
NEW['damske-tenisky']['guide'] += (
    '<h2>Ponožky, vložky a zdraví nohou</h2>'
    '<p>Pohodlí tenisek neurčuje jen bota, ale i to, co je uvnitř. Tenké kotníkové ponožky se hodí do nízkých střihů v teplých měsících, silnější pletené se vyplatí, když chodíte hodně a potřebujete tlumení. Bavlna příjemně hřeje, ale při potu vlhne, syntetické a merino směsi vlhkost odvádějí. Při zkoušce boty vždy obujte ponožky, které budete nosit.</p>'
    '<p>Pokud máte plochou nebo naopak vysokou klenbu, hledejte botu s vyjímatelnou stélkou. Tu můžete vyměnit za individuální vložku, a bota tak zůstane tvarově stejná. Tvrdá plochá podešev dává minimální oporu, proto zvlášť u žen, které stojí v práci celý den, vychází lépe model s pěnovou mezipodešví a pevnou patní částí.</p>'
    '<h2>Tenisky na práci vstoje a na cesty</h2>'
    '<p>Prodavačky, zdravotní sestry, učitelky nebo ženy v gastronomii tráví na nohou většinu dne. Pro ně je nejdůležitější lehká konstrukce, měkký došlap a dobrá pata, která nesklouzává. Dobrou volbou jsou vycházkové modely s protiskluzovou gumou. Při cestování zase vyhrávají lehké textilní modely, které se vejdou do kufru a rychle schnou po dešti.</p>'
    '<ul><li>Rozmyslete si, zda bota snese vodu, nebo ji budete nosit jen za sucha.</li>'
    '<li>Na cestu vybírejte neutrální barvu, která se hodí k více outfitům.</li>'
    '<li>Do letadla se hodí slip-on nebo boty s pružným šněrováním, které rychle sundáte.</li></ul>'
)

NEW['nike-tricko']['guide'] += (
    '<h2>Jak číst název modelu</h2>'
    '<p>Obchody uvádějí Nike trička ve velmi stručných názvech, například Sportswear Club, Dri-FIT Park nebo W NSW Tee. Písmeno W na začátku zpravidla znamená dámský model, M pánský a Jr. nebo Kids dětský. Zkratka NSW označuje volnočasovou řadu Sportswear, kdežto slova jako Tee, Top a Tank popisují druh: tričko, top a tílko. Když se naučíte tyto zkratky, snadno poznáte, zda jde o technické, nebo bavlněné tričko, i když popis v obchodě chybí.</p>'
    '<h2>Tričko podle aktivity</h2>'
    '<ul><li><strong>Běh:</strong> lehký Dri-FIT s reflexními prvky nebo rychle schnoucí síťovinou v zádech. Hodí se i dlouhý rukáv na podzim a jaro.</li>'
    '<li><strong>Posilovna:</strong> přiléhavý střih nebo volnější tílko, aby paže ve cviku nic neomezovalo.</li>'
    '<li><strong>Fotbal a týmové sporty:</strong> řady Academy a Park mají střih na pohyb a snadnou údržbu, hodí se do šatny i na trénink.</li>'
    '<li><strong>Kolo:</strong> delší zadní díl chrání záda a trička s lehkou tkaninou odvádějí pot při jízdě.</li>'
    '<li><strong>Chůze a město:</strong> Club a Essential z bavlny, které se příjemně nosí celý den.</li></ul>'
    '<p>Pokud tričko nosíte pro oba účely, zvolte kompromis. Technický polyester ve volnějším střihu funguje při sportu i v lehkém městském outfitu, jen se hodí méně na formálnější příležitosti.</p>'
    '<h2>Barva a viditelnost</h2>'
    '<p>Černá tričko zeštíhluje a skrývá skvrny, ale v létě se více zahřívá. Bílá je svěží, avšak prosvítá a na potu je znát. Šedá dobře maskuje pot, takže se hodí na trénink. Neonové a zářivé odstíny zvyšují viditelnost, což oceníte při večerním běhu nebo jízdě na kole. Kdo trénuje na slunci, zvolí světlejší barvy, které méně hřejí.</p>'
    '<h2>Materiály a udržitelnost</h2>'
    '<p>Řada triček obsahuje recyklovaný polyester a údaj najdete na štítku se složením. Hodnotu ale posuzujte podle konkrétního štítku, ne podle obecného sloganu. Podíl bavlny zlepšuje příjemnost na kůži, podíl elastanu přidává pružnost, a naopak může zhoršit prodyšnost. Dobrý ukazatel kvality je i hustota pleteniny a čisté zpracování švů.</p>'
    '<h2>Vrstvení a sezona</h2>'
    '<p>V létě stačí lehké tričko samotné. V přechodném období se hodí jako základní vrstva pod <a href="/nike-mikina/">mikinu</a> nebo lehkou bundu, přičemž prodyšný materiál dovolí potu pryč. V zimě slouží jako první vrstva a nad ni se přidá izolační díl. Bavlněné tričko jako první vrstva při pohybu venku v mrazu nepoužívejte, vlhkost vás ochladí.</p>'
)

NEW['damske-teplaky']['guide'] += (
    '<h2>Tepláky podle ročního období</h2>'
    '<p>Na jaro a léto sáhněte po lehké pletenině nebo tenčí směsi, případně po volnějších modelech z viskózy, které se nelepí k tělu. Na podzim se hodí střední gramáž s mírně drsnější vnitřní stranou. V zimě je nejlepší zateplená varianta s fleecem, ideálně s manžetou, která brání pronikání studeného vzduchu. Nezapomeňte, že vyšší teplota v bytě znamená, že hodně zateplené tepláky se budou hodit jen venku.</p>'
    '<h2>Tepláky na jógu, běh a posilovnu</h2>'
    '<ul><li><strong>Jóga a pilates:</strong> měkký, pružný materiál bez tuhých švů v rozkroku a s nízkým pasem, který se nesvíjí.</li>'
    '<li><strong>Běh:</strong> zúžené tepláky z lehkého polyesteru, nejlépe se zipem u kotníku, aby šly přetáhnout přes boty.</li>'
    '<li><strong>Posilovna:</strong> strečový materiál, který nepřekáží při dřepu, a pas, který se nesvezme při předklonu.</li>'
    '<li><strong>Procházky:</strong> volnější střih z bavlněné směsi, případně s kapsou na zip na klíče a telefon.</li></ul>'
    '<h2>Jak poznat kvalitní teplákovinu</h2>'
    '<p>Přetáhněte materiál mezi prsty: kvalitní pletenina je hustá, nevidíte skrz ni a po natažení se vrací do tvaru. Na rubové straně se nemají tvořit smyčky, které se při praní vytahují. Švy mají být rovné, zpevněné v rozkroku a u kapes. Pas musí být dvouvrstvý, aby se nevytahoval, a šňůrka se nesmí vysouvat z otvorů. Pokud při zkoušce tepláky po chvíli sedění vytvoří velké boule na kolenou, materiál není dostatečně pružný.</p>'
    '<h2>Barvy a kombinace</h2>'
    '<p>Černá a tmavě šedá drží tvar a skrývají skvrny. Světlá šedá je klasika mezi tepláky, ale ukáže pot a skvrny. Béžová a pastelové odstíny se hodí k jednobarevným souborům, tmavě modrá a khaki se dobře kombinují s bílou. U sady z mikiny a kalhot je výhodné pořídit stejnou barvu, protože odstíny různých šarží se mohou mírně lišit.</p>'
)

NEW['sandaly-keen']['guide'] += (
    '<h2>Kdy zvolit sandály a kdy boty</h2>'
    '<p>Sandály jsou praktické v teple, u vody a na cesty, kde se hodně přezouváte. Při chůzi po sypkém terénu, při deštivém počasí a s těžkým batohem je výhodnější zavřená obuv. Keen nabízí oba světy, a proto se vyplatí rozmyslet, co budete dělat nejčastěji. Pokud chcete jedny boty na pláž, na kempování a na procházku, hybridní sandál je rozumná volba. Pro více dnů na túře zvolte raději trekovou obuv.</p>'
    '<h2>Ponožky a sandály</h2>'
    '<p>Mnoho lidí nosí hybridní sandály s ponožkami, zvlášť na chladnější dny a při delším pochodu. Tenká technická ponožka zmírní tření pásků a pohlcuje pot. Bavlněné ponožky při průchodu vodou nasáknou a těžknou, vhodnější je syntetika nebo merino. Pokud chodíte bez ponožek, kontrolujte místa, kde pásek dře, a v případě potřeby ho povolte nebo upravte.</p>'
    '<h2>Děti, voda a bezpečnost</h2>'
    '<p>Dětské sandály se hodí na hřiště, na tábor i k vodě. Gumová podešev snižuje riziko uklouznutí, ale nezaručuje ho. Na mokrých kamenech a molech vždy hlídejte děti a pro plavání zvolte jinou pomůcku. Děti si obvykle rády samy obouvají, proto je důležité, aby šly sandály jednoduše upravit.</p>'
    + T(['Věk dítěte', 'Co hlídat u sandálů'], [
        ['Batolata a předškoláci', 'rychlé zapínání, měkká podešev, dostatečná rezerva před prsty'],
        ['Mladší školáci', 'pevný pásek kolem paty, odolná špička, snadné nastavení'],
        ['Starší děti a mládež', 'stabilnější podešev, lehká konstrukce, větší šíře u rostoucího chodidla'],
    ]) +
    '<p>Dětské chodidlo roste často o jedno až dvě čísla za rok, proto sandály z minulé sezony nemusí letos sedět. Před koupí nové dvojice porovnejte vnitřní délku stélky s chodidlem a nenechte se zlákat přílišnou rezervou, která by vedla k šoupání.</p>'
    '<h2>Údržba šňůrek a pásků</h2>'
    '<p>Modely s šňůrkovým systémem mají pojistku, která šňůrku drží utaženou. Po namočení šňůrku občas rozpusťte, aby se mohla vysušit, a zkontrolujte okraje, kde se může odírat. Suchý zip čistěte kartáčkem, písek a nitě zhoršují přilnavost. Pokud pásek povolí, vyměňte ho, nebo sandály raději omezte na procházky, aby se při větší zátěži nepřetrhl.</p>'
)

# ---- second extension
NEW['nike-tricko']['guide'] += (
    '<h2>Dámské a dětské Nike trička blíže</h2>'
    '<p>Dámské modely se často dělají v kratší délce nebo se zúženým pasem, aby se daly nosit k legínám s vysokým pasem i ke kraťasům. U tílek a topů hledejte širší ramínka, pokud nosíte batoh nebo cvičíte s činkami, tenká ramínka se zařezávají. Pro děti jsou praktická trička z bavlněné směsi, která se dobře perou, a technická trička pro ty, kdo trénují několikrát týdně. Mládežnické sportovní kluby často vyžadují jednotnou barvu, proto se vyplatí zeptat se na ni před nákupem.</p>'
    '<h2>Jak poznat dobře ušité tričko</h2>'
    '<p>Podívejte se na ramenní švy: mají ležet na hraně ramene, ne u krku nebo dole na paži. Výstřih se nesmí vlnit a po natažení se musí vrátit zpět. Spodní lem má být rovný a rukávy stejně dlouhé. Technické trička mají často tisk místo štítku, který nedře za krkem. Pokud po prvním praní tričko zkrátí nebo zkroutí boční švy, kvalita pleteniny odpovídala nižší třídě.</p>'
    '<p>U oblečení se značkou hledejte i podobné modely u jiných výrobců, abyste zjistili, jestli vám střih sedí. Pokud ne, porovnejte nabídku <a href="/adidas-tricko/">Adidas</a> nebo <a href="/under-armour-tricko/">Under Armour</a>, které mají jiný poměr ramen a pasu.</p>'
)

NEW['damske-teplaky']['guide'] += (
    '<h2>Tepláky a postava</h2>'
    '<p>Každá postava má svůj ideální střih. Užší jogger s manžetou prodlužuje nohy, pokud ho kombinujete s botou v barvě kalhot. Rovné tepláky působí vyváženě na širších bocích, protože neodhalují obrys stehen. Wide leg a barelové střihy vyžadují přiléhavější horní díl, jinak se silueta ztratí. Na vyšší postavu sedí delší nohavice, na menší vypadá lépe střih s manžetou, která zkrátí délku. U vysokého pasu zvolte tenčí pas, který nevytváří rolku, a u nízkého pasu pružnější materiál.</p>'
    '<h2>Tepláky pro dospívající a po sportu</h2>'
    '<p>Pokud tepláky kupujete dospívající dívce, zvolte větší rezervu v délce a v pase, protože roste rychle a oblíbené kousky nosí často. U sportovních oddílů se vyplatí odolnější materiál na kolenou. Po tréninku se tepláky navlékají přes vlhké nohy, takže měkká vnitřní strana a zip u kotníku usnadní oblékání. Mikina a tepláky ze stejné řady vytvoří jednotný outfit na cestu do tělocvičny.</p>'
)

NEW['sandaly-keen']['guide'] += (
    '<h2>Jak se sandály nosí na dovolené a v kempu</h2>'
    '<p>Do kempu a na dovolenou potřebujete obuv, která zvládne písek, kameny, vodu i dlouhé procházky po městě. Hybridní sandál tyto situace spojuje do jednoho páru, takže ušetříte místo v zavazadle. Po dni u moře ho opláchněte a nechte vyschnout na vzduchu mimo přímé slunce, jinak se může deformovat a ztratit barvu. Do restaurace ho obujete jen tehdy, když vypadá čistě, proto ho po dni v písku omyjte.</p>'
    '<p>Do skalnatého terénu zvažte, zda budou stačit pásky, nebo si vezmete lehké boty. Sandály nechrání kotník před vyvrtnutím a při chůzi po suti není jejich stabilita tak vysoká jako u trekové obuvi. Naopak pro krátké vycházky a brodění potoků jsou nejpraktičtější.</p>'
)
NEW['sandaly-keen']['faq'] += [
    ('Mohu sandály Keen prát v pračce?', 'Výrobci obvykle doporučují ruční mytí vlažnou vodou a jemným mýdlem. Pračka a vysoká teplota mohou poškodit lepení a pěnu. Vždy zkontrolujte štítek na konkrétním modelu a sušte přirozeně.'),
]
