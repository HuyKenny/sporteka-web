"""sporteka.cz — wave 14e (4. 11. 2026): long texts (>= 1650 words) for barefoot-obuv, kolobezky, nepromokave-bundy, fotbal.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ barefoot-obuv
NEW['barefoot-obuv'] = dict(long=True,
    title='Barefoot boty: tenisky, sandály i zimní obuv | Sporteka',
    desc='Barefoot boty pro děti i dospělé: tenisky, sandály, zimní a trailová obuv. Průvodce přechodem na naboso a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Barefoot boty</strong> mají tenkou ohebnou podešev, nulový nebo minimální rozdíl mezi patou a špičkou a prostornou špičku, ve které se prsty mohou roztáhnout. Cílem je nechat chodidlo pracovat tak, jak je příroda navrhla, a nepodpírat ho tvrdou stélkou. Nejde o módní výstřelek jedné sezóny, ale o jinou filozofii obouvání, která vyžaduje trochu trpělivosti.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů na jednom místě. Najdete tu městské modely, <a href="/tenisky/">tenisky</a>, <a href="/sandaly/">sandály</a>, <a href="/zimni-obuv/">zimní obuv</a>, <a href="/holinky/">holínky</a> i lehké boty na <a href="/beh/">běh</a> a lehkou turistiku. Pomůžeme vám vybrat správnou velikost, materiál a postup, jak chodidlo přivyknout bez bolesti. Dětské i dospělé modely jsou rozdělené podle značek, takže snadno porovnáte, kdo nabízí ten nejširší střih.</p>',
    guide='<h2>Co dělá botu barefoot</h2>'
          '<p>Slovo barefoot se dnes používá volně, a proto se vyplatí znát znaky, podle kterých pravou minimalistickou botu poznáte. Žádný z nich sám o sobě nestačí, rozhoduje jejich kombinace. Podívejte se do popisu produktu a zkontrolujte, zda výrobce uvádí parametry, nebo jen slovo v názvu.</p>'
          + T(['Znak', 'Proč je důležitý', 'Jak ho ověřit'], [
              ['Nulový drop', 'pata je ve stejné výšce jako špička, chodidlo stojí ploše', 'údaj o rozdílu v milimetrech v popisu'],
              ['Široká špička', 'prsty se mohou volně roztáhnout, což mnozí uživatelé vnímají jako stabilnější postoj', 'špička je široká jako chodidlo, ne zúžená'],
              ['Tenká podešev', 'chodidlo cítí povrch a reaguje na něj', 'tloušťka podrážky v milimetrech'],
              ['Ohebnost', 'bota se dá srolovat a zkroutit rukama', 'zkuste ji ohnout, pokud ji máte v ruce'],
              ['Lehká konstrukce', 'chodidlo není zatěžováno zbytečnou hmotností', 'hmotnost páru v popisu']]) +
          '<p>Barefoot nemusí znamenat úplně tenkou podrážku. Některé modely mají o něco silnější podešev kvůli tvrdému terénu nebo studené zemi, přesto zůstávají ohebné a bez zdvihu paty. Vyšší tloušťka tedy neznamená automaticky ztrátu barefoot vlastností, ale kompromis mezi cítěním a ochranou.</p>'
          '<h2>Pro koho jsou barefoot boty vhodné</h2>'
          '<p>Hodí se lidem, kteří chtějí zkusit přirozenější došlap a ocení volnost pro prsty; přínos pro chodidlo je individuální, proto přecházejte postupně. Děti se s nimi často sžijí snadněji, protože jejich chodidlo ještě roste a nemá zafixované návyky. Dospělí, kteří celý život nosili tuhé boty s výrazným tlumením, by měli přecházet opatrněji.</p>'
          '<ul><li><strong>Děti:</strong> široká špička nechá prsty růst bez tlaku, ohebná podešev nebrání pohybu.</li>'
          '<li><strong>Dospělí v běžném provozu:</strong> městské tenisky a polobotky nahradí klasickou obuv do kanceláře i na procházky.</li>'
          '<li><strong>Cvičenci:</strong> při cvičení na podlaze a při silovém tréninku oceníte kontakt s povrchem.</li>'
          '<li><strong>Turisté a běžci:</strong> lehké modely se hodí na zpevněné stezky a trasy v lese.</li></ul>'
          '<p>Pokud máte diagnostikovanou vadu chodidla, zraněnou Achillovu šlachu nebo problémy s plochou nohou, poraďte se před přechodem s ortopedem nebo fyzioterapeutem. Barefoot obuv není lék a každému nesedí stejně.</p>'
          '<h2>Jak na přechod: pomalu a po částech</h2>'
          '<p>Nejčastější chyba je přechod ze dne na den. Svaly chodidla a lýtka byly léta zvyklé na oporu a potřebují se přizpůsobit. První týdny noste nové boty jen na krátké procházky a postupně prodlužujte dobu. Bolest v lýtkách nebo v chodidle je signál ke zpomalení, ne k vytrvání.</p>'
          '<ol><li>První týden jen pár hodin denně, nejlépe po hladkém povrchu.</li>'
          '<li>Střídejte barefoot a klasické boty, dokud nepocítíte, že chodidlo je silnější.</li>'
          '<li>Při chůzi dopadejte měkce, na střed chodidla, ne tvrdě na patu.</li>'
          '<li>K běhu přistupujte až po několika týdnech chůze a začněte krátkými úseky.</li>'
          '<li>Doplňte cviky: zvedání prstů, stoj na jedné noze, chůze po špičkách a po patách.</li></ol>'
          '<h2>Typy barefoot obuvi podle příležitosti</h2>'
          '<p>Nabídka je dnes široká a pokrývá téměř všechny situace. Kategorie na Sportece se prolíná s dalšími obuvnickými sekcemi, takže se vyplatí porovnat více pohledů.</p>'
          + T(['Situace', 'Doporučený typ', 'Související kategorie'], [
              ['Město a kancelář', 'kožené polobotky nebo textilní tenisky v neutrální barvě', '<a href="/tenisky/">tenisky</a>'],
              ['Léto a voda', 'otevřené sandály s pásky, lehké obuv do vody', '<a href="/sandaly/">sandály</a>, <a href="/obuv-do-vody/">obuv do vody</a>'],
              ['Zima a mráz', 'zateplené kotníčkové boty s membránou nebo vlněnou vložkou', '<a href="/zimni-obuv/">zimní obuv</a>'],
              ['Déšť a bláto', 'gumové nebo neoprenové boty s ohebnou podešví', '<a href="/holinky/">holínky</a>'],
              ['Běh po zpevněném povrchu', 'lehká silniční bota s nízkým dropem', '<a href="/bezecka-obuv/">běžecká obuv</a>'],
              ['Lehká turistika', 'bota se silnější podešví a výraznějším vzorkem', '<a href="/trekova-obuv/">trekové boty</a>'],
              ['Cvičení a trénink', 'plochá bota s minimálním tlumením', '<a href="/treninkova-obuv/">tréninková obuv</a>']]) +
          '<h3>Městské a každodenní boty</h3>'
          '<p>Pro celý den v kanceláři se hodí elegantnější kožené modely, které mají tenkou podešev a pohodlné prostorné špičky. Kdo chodí hodně pěšky, ocení pevnější zadní část a pružnou stélku, která se nepromačkne. Pozor na příliš měkkou kůži, která se při častém nošení roztahuje a ztrácí tvar.</p>'
          '<h3>Zimní a nepromokavé modely</h3>'
          '<p>Tenká podešev přenáší chlad ze země, a proto zimní barefoot obuv potřebuje silnější izolaci mezi chodidlem a povrchem. Zkontrolujte, zda je v botě vložka z vlny nebo jiného izolačního materiálu a zda je horní díl dostatečně vysoký. Mokrým ponožkám se snáze vyhnete s membránou, ale prodyšnost je pak o něco nižší. Zimní obuv vždy zkoušejte s ponožkami, které budete nosit venku.</p>'
          '<h3>Dětské barefoot boty</h3>'
          '<p>Chodidlo dítěte roste rychle, a proto kupujte velikost s rezervou, ale ne přehnanou. Prostor před palcem by měl být okolo centimetru, aby bota nepřekážela. Dětské modely mají často suchý zip nebo pružnou tkaničku, takže si je dítě obuje samo. Mezi značkami s dětským sortimentem najdete ' + B(('froddo', 'Froddo'), ('reima', 'Reima'), ('be-lenka', 'Be Lenka'), ('pegres', 'Pegres')) + '.</p>'
          '<h2>Jak vybrat velikost a šířku</h2>'
          '<p>U barefoot bot nestačí znát velikost z jiných bot. Různí výrobci mají různé střihy a rozdíly mohou činit i celou velikost. Nejspolehlivější je změřit chodidlo ve stoje, ve večerních hodinách, kdy je mírně opuchlé, a porovnat údaj s tabulkou výrobce. Měření provádějte na obou nohách, protože se často liší.</p>'
          '<ul><li>Postavte se na papír, obkreslete chodidlo a změřte vzdálenost od paty ke špičce nejdelšího prstu.</li>'
          '<li>Přidejte rezervu zhruba jeden centimetr pro dospělého, u dětí o něco více.</li>'
          '<li>Změřte i šířku v nejširším místě a porovnejte s údajem v tabulce.</li>'
          '<li>Pokud jste mezi velikostmi, zvolte větší a doplňte tenčí ponožky.</li></ul>'
          '<p>Při zkoušení dbejte na to, aby se prsty nedotýkaly přední části boty a aby pata držela. Jestliže pata sklouzává, je bota moc velká nebo má nesprávný tvar. Vracení je u botů z internetu běžné, proto zkontrolujte lhůtu a podmínky v e-shopu.</p>'
          '<h2>Materiály a konstrukce</h2>'
          '<p>Horní díl bývá z kůže, textilu nebo syntetické tkaniny. Kůže je odolná a tvaruje se podle nohy, ale potřebuje péči a je těžší. Textil je lehký, prodyšný a rychle schne, hodí se na léto a sport. Syntetické materiály se čistí snadno, ale hůře dýchají. Podešev bývá z gumy nebo lehké pěny, přičemž guma lépe drží na mokru a déle vydrží.</p>'
          '<p>Stélka může být vyjímatelná. To se hodí, pokud potřebujete vložit ortopedickou vložku nebo prostě vyprat. Zkontrolujte také, jak je bota sešitá. Slabá nit v místě ohybu se při častém používání poruší dřív než podešev. U sandálů sledujte přezky, které se nesmí časem uvolňovat.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete ' + B(('be-lenka', 'Be Lenka'), ('vivobarefoot', 'Vivobarefoot'), ('skinners', 'Skinners'), ('barebarics', 'Barebarics'), ('shapen', 'Shapen'), ('leguano', 'Leguano'), ('froddo', 'Froddo'), ('pegres', 'Pegres'), ('victoria', 'Victoria'), ('merrell', 'Merrell'), ('geox', 'Geox'), ('reima', 'Reima')) + '. Značky se liší střihem, šířkou i filozofií. Specialisté na minimalistickou obuv nabízejí celé řady od města po terén, tradiční obuvnické značky přidávají do portfolia několik modelů s barefoot prvky. Čtěte parametry, ne jen název kolekce.</p>'
          '<h2>Péče o barefoot boty</h2>'
          '<p>Tenká podešev a lehký horní díl vyžadují šetrnou péči. Boty po použití vysušte při pokojové teplotě, nikdy na topení, které by lepidlo a kůži poškodilo. Hrubé nečistoty odstraňte kartáčem a skvrny vytřete vlhkým hadrem. Kožené modely jednou za čas ošetřete krémem nebo voskem. Textilní boty můžete prát ručně v teplé vodě, pračka je pro ně obvykle příliš tvrdá.</p>'
          '<p>Pravidelně kontrolujte stav podrážky. Zabroušená guma na jednom místě znamená, že došlo ke změně způsobu došlapu, což se hodí zaznamenat. Ponožky zvolte tenké a bez silných švů, nejlépe z <a href="/merino-ponozky/">merina</a> nebo syntetiky, které odvádějí vlhkost. Další tipy najdete v sekci <a href="/doplnky-k-obuvi/">doplňky k obuvi</a> a mezi <a href="/sportovni-ponozky/">sportovními ponožkami</a>.</p>'
          '<h2>Nejčastější chyby při nákupu a používání</h2>'
          '<ul><li>Kupovat podle názvu „barefoot“ bez kontroly drop, šířky špičky a ohebnosti.</li>'
          '<li>Přejít na minimalistickou obuv přes noc a zaplatit za to bolestí lýtek.</li>'
          '<li>Volit příliš malou velikost, aby bota držela, a stlačit prsty.</li>'
          '<li>Nosit tenkou podešev na ostrém štěrku nebo na mrazu, kde chybí ochrana.</li>'
          '<li>Pokračovat v běhu v těsné obuvi kvůli kamarádům, kteří „to zvládli“.</li>'
          '<li>Zapomenout na změnu techniky: chůze a běh na střed chodidla jsou základ.</li></ul>'
          '<h2>Kdy barefoot nepoužívat</h2>'
          '<p>Na stavbě, v dílně nebo v jiných provozech s rizikem pádu předmětů potřebujete obuv s ochranným prvkem a ten barefoot modely většinou nemají. Stejně tak na dlouhé túry s těžkým batohem a ostrým skalním terénem zvolte raději klasickou <a href="/trekova-obuv/">trekovou obuv</a> nebo <a href="/nizke-trekove-boty/">nízké trekové boty</a>. Barefoot je nástroj pro určité situace, nikoli univerzální řešení.</p>',
    faq=[('Jak poznám skutečnou barefoot botu?', 'Má nulový nebo minimální drop, širokou špičku, tenkou ohebnou podešev a nízkou hmotnost. Parametry by měl výrobce uvést; jen slovo v názvu nestačí.'),
         ('Jak dlouho trvá přechod na barefoot?', 'Obvykle několik týdnů až měsíců, podle toho, jak často boty nosíte. Důležité je zvyšovat zátěž postupně a poslouchat tělo.'),
         ('Hodí se barefoot boty pro děti?', 'Ano, široká špička a ohebná podešev nebrání přirozenému růstu chodidla. Kupujte s rezervou zhruba centimetr před prsty a sledujte, zda se dítě v botách pohybuje bez omezení.'),
         ('Jsou barefoot boty vhodné na běh?', 'Ano, ale po postupném zvykání. Nejprve se naučte chodit a teprve potom zařazujte krátké běžecké úseky. Měkký došlap na střed chodidla je důležitější než obuv.'),
         ('Hřejí barefoot boty v zimě?', 'Záleží na modelu. Zimní verze mají izolační vložku a vyšší horní díl; tenká podešev přenáší chlad, proto je potřeba silnější izolace nebo teplejší ponožky.'),
         ('Jak vybrat velikost barefoot bot?', 'Změřte chodidlo ve stoje a porovnejte s tabulkou konkrétního výrobce. Přidejte rezervu okolo centimetru a v nejasném případě zvolte větší velikost.'),
         ('Mohu v barefoot botách chodit celý den?', 'Až si zvyknete, ano. V prvních týdnech je ale nosíte jen na část dne a střídáte s jinou obuví.'),
         ('Jak prát barefoot boty?', 'Textilní ručně v teplé vodě bez aviváže a nechat zvolna oschnout. Kožené jen otírat a ošetřovat krémem. Sušení na topení lepidlo poškozuje.'),
         ('Jsou barefoot boty vhodné pro lidi s plochou nohou?', 'Mohou pomoci posílit chodidlo, ale u diagnostikované vady je lepší konzultace s ortopedem nebo fyzioterapeutem před změnou obuvi.'),
         ('Proč mají barefoot boty tak širokou špičku?', 'Aby se prsty mohly roztáhnout a podílet se na stabilitě. Úzká špička klasických bot prsty stlačuje a časem může vést k deformacím.')],
)

# ------------------------------------------------------------------ kolobezky
NEW['kolobezky'] = dict(long=True,
    title='Koloběžky: dětské, městské, freestyle, elektro | Sporteka',
    desc='Koloběžky pro děti i dospělé: tříkolky, městské, skládací, freestyle a elektrické. Průvodce výběrem a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Koloběžka</strong> patří k nejjednodušším dopravním prostředkům. Nemá převody, nemusíte udržovat řetěz a naučí se na ní jezdit skoro každý během několika minut. Přesto je mezi modely obrovský rozdíl: dvouletá holka na tříkolce má jiné potřeby než student, který jezdí do školy a nosí ji do MHD, nebo teenager v skateparku. Proto se vyplatí vybírat podle účelu.</p>'
          '<p>Na Sportece najdete <a href="/freestyle-kolobezky/">freestyle koloběžky</a>, <a href="/elektrokolobezky/">elektrokoloběžky</a> i klasické dětské a městské modely z českých obchodů. K tomu patří <a href="/chranice-a-helmy/">chrániče a helmy</a>, <a href="/odrazedla/">odrážedla</a> pro nejmenší nebo <a href="/inline-brusle/">inline brusle</a> jako alternativa pro starší jezdce. Níže najdete přehled typů, parametrů, velikostí a tipů na údržbu, abyste neutratili za koloběžku, která bude do měsíce zbytečná. Čtěte také části o bezpečnosti a o tom, kdy je lepší zvolit jiný dopravní prostředek.</p>',
    guide='<h2>Typy koloběžek podle použití</h2>'
          '<p>Nejdřív si ujasněte, kdo bude jezdit a kde. Teprve potom řešte barvu a značku. Základní rozdělení vypadá takto.</p>'
          + T(['Typ', 'Pro koho', 'Typické vlastnosti'], [
              ['Tříkolka', 'děti od zhruba dvou let', 'široký rozvor, nízká plošina, často naklápěcí řízení'],
              ['Dětská dvoukolka', 'děti od čtyř až pěti let', 'nastavitelná řídítka, brzda na zadní blatník'],
              ['Městská a skládací', 'dospívající a dospělí na dojíždění', 'větší kola, hliníkový rám, skládací mechanismus'],
              ['Freestyle', 'jezdci na triky ve skateparku', 'pevný rám, malá kola, bez skládání, pevné řídítko'],
              ['Terénní', 'výlety po lese a polních cestách', 'nafukovací kola, kvalitní brzda, odpružení'],
              ['Elektrická', 'delší trasy bez odrážení', 'motor, baterie, displej, vyšší hmotnost']]) +
          '<h2>Dětské koloběžky a růst dítěte</h2>'
          '<p>U dětí je klíčová stabilita a výška řídítek. První koloběžka by měla být taková, aby dítě stálo oběma nohama pevně na plošině a dosáhlo na řídítka bez zvedání ramen. Tříkolky s naklápěním učí dítě zatáčet přenášením váhy a jsou jednodušší než model s pevným řízením. Později přijde dvoukolka, kde už je nutné držet rovnováhu.</p>'
          '<ul><li>Zkontrolujte maximální nosnost a rozsah výšky řídítek, aby koloběžka vydržela růst.</li>'
          '<li>Hmotnost by měla být taková, aby ji dítě samo zvedlo a mohlo s ní manipulovat.</li>'
          '<li>Protiskluzový povrch plošiny je důležitější než barva a nálepky.</li>'
          '<li>Brzda na zadním blatníku je pro děti nejjednodušší, protože se aktivuje došlapem.</li></ul>'
          '<p>Pokud je dítě ještě mladší nebo nejisté, začněte <a href="/odrazedla/">odrážedlem</a>, které učí rovnováhu bez pedálů a brzd. Pro starší děti zvažte přechod na <a href="/detska-kola/">dětská kola</a>, ale koloběžka zůstane výborným doplňkem pro cestu do školy.</p>'
          '<h2>Městské a skládací koloběžky</h2>'
          '<p>Na dojíždění je rozhodující velikost kol a kvalita ložisek. Větší kola lépe překonávají nerovnosti a obrubníky, malá kola jsou obratnější, ale na hrubším povrchu drncají. Skládací modely se vejdou do kufru i pod stůl v kanceláři, takže si poradíte s kombinací koloběžky a MHD. Zkontrolujte, jak pevně drží skládací kloub, protože právě ten je nejnamáhanější místo.</p>'
          + T(['Parametr', 'Co určuje', 'Na co si dát pozor'], [
              ['Průměr kol', 'pohodlí a rychlost na nerovném povrchu', 'příliš malá kola drncají na dlažbě'],
              ['Nosnost', 'maximální hmotnost jezdce včetně batohu', 'počítejte s rezervou'],
              ['Hmotnost', 'snadnost nošení', 'při skládání do MHD je každý kilogram znát'],
              ['Brzda', 'bezpečné zastavení', 'zadní blatník nebo kotoučová brzda'],
              ['Výška řídítek', 'držení těla', 'nastavitelnost nebo teleskopická trubka'],
              ['Ložiska a kolečka', 'plynulost jízdy', 'kvalitní ložiska a odolná pryž']]) +
          '<h2>Freestyle koloběžky pro skatepark</h2>'
          '<p>Freestyle koloběžky mají pevnější konstrukci, menší kola z tvrdého polyuretanu a nemají skládací kloub. Jsou určené pro skoky, otáčky a jízdu po rampách. Důležitými součástmi jsou řídítka, vidlice, kompresní systém a ráfky. Bezpečnost řeší především helma a chrániče, protože pády patří k učení. Nový jezdec by měl začít na hladkém povrchu a postupně přecházet na rampy. Více se dozvíte v kategorii <a href="/freestyle-kolobezky/">freestyle koloběžky</a>.</p>'
          '<p>Při výběru sledujte výšku řídítek vzhledem k výšce jezdce. Příliš vysoká řídítka ztěžují kontrolu, příliš nízká nutí k nepohodlnému předklonu. Komplet koloběžky pro začátečníky je rozumnější než sestavování dílů, zkušenější jezdci si naopak často vyměňují jednotlivé komponenty.</p>'
          '<h2>Elektrokoloběžky</h2>'
          '<p>Elektrokoloběžka nahradí odrážení motorem a hodí se na delší trasy a kopcovitý terén. Rozhodují kapacita baterie, výkon motoru, hmotnost a typ pneumatik. Čím větší baterie, tím delší dojezd, ale také vyšší hmotnost. Před nákupem si prostudujte pravidla pro provoz na pozemních komunikacích, protože podmínky se liší podle výkonu a rychlosti. Podrobnosti najdete v kategorii <a href="/elektrokolobezky/">elektrokoloběžky</a>.</p>'
          '<ul><li>Zjistěte reálný dojezd, ne maximální údaj uváděný za ideálních podmínek.</li>'
          '<li>Zkontrolujte brzdy, nejlépe dvojité, a osvětlení pro jízdu za šera.</li>'
          '<li>Počítejte s vyšší hmotností při nošení do výtahu nebo schodů.</li>'
          '<li>Ověřte dostupnost servisu a náhradních dílů.</li></ul>'
          '<h2>Bezpečnost: helma, chrániče a viditelnost</h2>'
          '<p>Koloběžka je pomalejší než kolo, ale pád může skončit stejně vážně. Základem je helma, která sedí těsně a nemá vůli. Chrániče kolen a loktů ocení děti i začátečníci a ve skateparku patří téměř k povinnosti. Pro večerní jízdu přidejte světlo a reflexní prvky, abyste byli vidět. Velký rozdíl dělá i vhodná obuv s pevnou podrážkou, na které noha nepodkluzuje, například <a href="/tenisky/">tenisky</a>.</p>'
          '<p>Vybavení najdete v kategoriích <a href="/chranice-a-helmy/">chrániče a helmy</a>, doplňky pro sportovní zábavu v sekci <a href="/volny-cas/">volný čas</a> a související kategorii <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>.</p>'
          '<h2>Velikost podle výšky jezdce</h2>'
          '<p>Koloběžka musí odpovídat výšce jezdce, jinak se rychle unaví záda i zápěstí. Řídítka by měla končit zhruba v úrovni pasu až spodních žeber, aby se paže držely v mírném ohnutí a jezdec stál vzpřímeně. U dětí se výška řídítek nastavuje často, proto zvolte model s rychloupínákem, který se přenastaví bez nářadí. Délka plošiny určuje, zda se na ni vejdou obě nohy za sebou. Dospělý jezdec s větší obuví potřebuje delší plošinu než dospívající.</p>'
          '<ul><li>Dospělí nad běžnou výšku ocení teleskopická řídítka s vyšším rozsahem.</li>'
          '<li>Menší jezdci potřebují nízkou plošinu, aby se snadno odráželi.</li>'
          '<li>Teleskopická trubka musí mít spolehlivou pojistku, aby se při nárazu nezasunula.</li></ul>'
          '<h2>Koloběžka, kolo nebo brusle</h2>'
          '<p>Koloběžka vyhrává tam, kde je nutné se často zastavovat, skládat nebo vést vedle sebe. Na delší trasy mimo město je pohodlnější <a href="/trekingova-kola/">trekingové kolo</a> nebo <a href="/mestska-kola/">městské kolo</a>, protože převody a sedlo ulevují nohám. Brusle vyžadují více techniky a hladký povrch, ale nabízejí vyšší rychlost. Pro děti je koloběžka vhodný přechod mezi odrážedlem a kolem a posiluje koordinaci i stabilitu.</p>'
          '<h2>První jízdy a technika</h2>'
          '<p>Správná technika šetří síly. Odrážejte se střídavě oběma nohama, protože jednostranné odrážení může vést k nerovnoměrné zátěži těla. Váhu držte nad plošinou a kolena lehce pokrčená, což tlumí otřesy. Před zatáčkou zpomalte a zatáčejte plynule, ne trhaně. Začátečníci by měli nejdřív vyzkoušet brzdu na rovné ploše bez provozu a naučit se zastavit včas, než vyjedou mezi chodce.</p>'
          '<h2>Převoz a uskladnění</h2>'
          '<p>Před nákupem si změřte kufr auta a místo v předsíni. Skládací koloběžka má po složení délku okolo jednoho metru, pevný model zabírá víc. Zkontrolujte, zda je zámek skládání samosvorný, a vždy před jízdou ověřte jeho zajištění. Koloběžku nenechávejte přes noc venku, protože déšť a mráz poškozují ložiska i brzdu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Najdete zde značky ' + B(('micro', 'Micro'), ('core', 'Core'), ('divine', 'Divine'), ('urbis', 'URBiS'), ('striker', 'Striker'), ('nils-extreme', 'Nils Extreme'), ('raven', 'Raven'), ('ethic', 'Ethic'), ('yedoo', 'Yedoo'), ('chilli', 'Chilli'), ('slamm', 'Slamm'), ('tempish', 'Tempish'), ('arcore', 'Arcore'), ('addict', 'Addict')) + '. Některé jsou zaměřené na děti a městské jezdce, jiné na freestyle a komunitu ve skateparcích. Před nákupem se zaměřte na konkrétní parametry modelu, ne jen na značku.</p>'
          '<h2>Údržba koloběžky</h2>'
          '<p>Koloběžka je nenáročná, ale několik minut péče prodlouží její životnost. Po každé jízdě v mokru ji otřete a nechte vyschnout, jinak začnou rezavět šrouby a ložiska. Pravidelně kontrolujte dotažení všech šroubů, zejména u řídítek a vidlice. Opotřebovanou brzdu nebo kolečka vyměňte včas, protože slabá brzda je největší riziko u dětských modelů.</p>'
          '<ul><li>Ložiska občas vyčistěte a namažte vhodným mazivem.</li>'
          '<li>Zkontrolujte, zda se kolečka rovnoměrně opotřebovávají, a případně je prohoďte.</li>'
          '<li>U nafukovacích kol hlídejte tlak a stav plášťů.</li>'
          '<li>Skládací mechanismus udržujte čistý a bez písku.</li>'
          '<li>Koloběžku skladujte v suchu, nejlépe uvnitř, ne celoročně venku.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupit příliš velkou koloběžku „na vyrůstání“, na které dítě ztrácí kontrolu.</li>'
          '<li>Vybrat hračku z hypermarketu s křehkým rámem a nepořádnou brzdou.</li>'
          '<li>Podcenit nosnost, především u dospělých s batohem.</li>'
          '<li>Pořídit freestyle model pro dojíždění, kde se osvědčí větší kola a skládání.</li>'
          '<li>Zapomenout na helmu a chrániče, které se kupují zároveň s koloběžkou.</li>'
          '<li>Neověřit, zda se koloběžka vejde do kufru nebo na místo, kde bude uložená.</li></ul>'
          '<h2>Koloběžka jako rodinný dopravní prostředek</h2>'
          '<p>Na výlety s dětmi se osvědčila kombinace: rodič jede na městské koloběžce, dítě na dvoukolce nebo tříkolce, a když se unaví, vezme se do kufru auta. Domluvte předem trasu s hladkým povrchem a bez příkrých kopců, protože děti se rychle unaví. Pro cestu do školy vybírejte model, který dítě samo unese do třídy, a nezapomeňte na zámek, pokud ji necháte před budovou.</p>'
          '<h2>Kdy koloběžku vyměnit</h2>'
          '<p>Děti z dětských modelů vyrostou za jeden až dva roky, proto zvažte nákup použité koloběžky nebo předání mladšímu sourozenci. Při praskání rámu, ohýbání řídítek nebo vůli v hlavovém složení koloběžku raději vyřaďte. Bezpečnostní prvky se nesmějí improvizovat, protože na koloběžce jezdí lidé po dlažbě, silnici i v parku.</p>',
    faq=[('Jakou koloběžku koupit dítěti ve třech letech?', 'Tříkolku s nízkou plošinou, širokým rozvorem a naklápěcím řízením. Dítě na ní stojí stabilně a učí se zatáčet přenášením váhy.'),
         ('Od kdy může dítě jezdit na dvoukolce?', 'Zpravidla od čtyř až pěti let, podle motoriky a odvahy. Rozhodující je, aby dítě zvládlo udržet rovnováhu a ovládat brzdu.'),
         ('Jak velká kola má mít městská koloběžka?', 'Čím větší, tím lépe překonají nerovnosti a obrubníky. Malá kola jsou obratnější, ale na dlažbě mnohem více drncají.'),
         ('Vejde se skládací koloběžka do MHD?', 'Většinou ano, pokud je dostatečně lehká a skládací mechanismus drží pevně. Zkontrolujte pravidla dopravce a rozměry po složení.'),
         ('Čím se liší freestyle koloběžka?', 'Má pevný rám bez skládání, malá kola z tvrdého materiálu a odolnější řídítka. Je určena pro skatepark a triky, ne na dojíždění.'),
         ('Potřebuji helmu na koloběžku?', 'Ano. Helma chrání před nejčastějším vážným zraněním, zvláště u dětí. Doplňte ji chrániči kolen a loktů, pokud jezdíte na triky.'),
         ('Jakou nosnost má mít koloběžka pro dospělého?', 'Alespoň o několik kilogramů víc, než je vaše váha s batohem. Rezerva prodlužuje životnost rámu i ložisek.'),
         ('Jak často kontrolovat šrouby na koloběžce?', 'Nejlépe jednou za pár týdnů při pravidelné jízdě a po každém větším nárazu nebo pádu. Uvolněné řídítka jsou častý zdroj úrazů.'),
         ('Hodí se elektrokoloběžka na dojíždění?', 'Pro delší trasy ano, ale musíte počítat s vyšší hmotností a pravidly provozu. Zajímejte se o reálný dojezd baterie a dostupnost servisu.'),
         ('Jak koloběžku uskladnit přes zimu?', 'Suché místo bez mrazu, očistěná a s promazanými ložisky. U elektrických modelů dodržte doporučení výrobce pro baterii.')],
)

# ------------------------------------------------------------------ nepromokave-bundy
NEW['nepromokave-bundy'] = dict(long=True,
    title='Nepromokavé a outdoorové bundy | Sporteka',
    desc='Nepromokavé bundy s membránou pro túry, kolo i město. Průvodce vodním sloupcem, prodyšností, péčí a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Nepromokavá bunda</strong> je vrstva, která zastaví vodu a vítr, ale zároveň pustí ven vlhkost z těla. Právě druhá část úkolu je těžší. Bunda, která dokonale odpuzuje déšť, ale nedýchá, vás uvnitř promočí potem. Proto se při výběru neřeší jen „nepromokavost“, ale celý systém: materiál, švy, zipy, kapuci a střih.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a vyberete si podle sportu i počasí. Související kategorie najdete u <a href="/softshellove-bundy/">softshellových bund</a>, <a href="/vetrovky/">větrovek</a>, <a href="/zimni-bundy/">zimních bund</a> a <a href="/sportovni-bundy-jaro-podzim/">bund na jaro a podzim</a>. Níže vysvětlíme parametry, typy konstrukce, velikosti, péči a nejčastější chyby, kterých se kupující dopouštějí. Pokud si nejste jistí, zda stačí lehká záložní bunda do batohu, nebo potřebujete plnohodnotnou horskou, pomůže vám přehled podle sportu a podle konstrukce.</p>',
    guide='<h2>Jak nepromokavá bunda funguje</h2>'
          '<p>Většina kvalitních bund využívá membránu, tedy tenkou fólii s mikroskopickými póry. Ty jsou menší než kapka vody, ale větší než molekula vodní páry. Kapka tak zůstane venku, pára z těla projde ven. Membrána je buď laminovaná k vnější tkanině, nebo vložená mezi ni a podšívku. Vnější látka je ošetřená impregnací, díky které voda perlí a nenasákne. Jakmile impregnace slábne, tkanina se zaplní vodou a bunda přestane dýchat, i když membrána stále drží.</p>'
          '<h3>Jak číst parametry</h3>'
          + T(['Parametr', 'Co říká', 'Poznámka'], [
              ['Vodní sloupec', 'odolnost látky proti pronikání vody v milimetrech', 'vyšší číslo znamená vyšší odolnost, ale neříká vše o švech'],
              ['Prodyšnost', 'schopnost odvádět vodní páru', 'udává se v gramech za den nebo jiných jednotkách; srovnávejte jen stejné metody'],
              ['Zatmelené švy', 'zalepené místa sešití', 'bez nich může voda proniknout i přes dobrou látku'],
              ['Impregnace DWR', 'povrchová úprava, ze které voda stéká', 'časem slábne a dá se obnovit'],
              ['Hmotnost a skladnost', 'jak se vejde do batohu', 'důležité u lehkých záložních bund']]) +
          '<p>Vodní sloupec se uvádí v milimetrech a vyšší hodnota znamená, že látka vydrží větší tlak vody. Pro běžný déšť stačí menší hodnoty, pro dlouhý liják v horách nebo pod batohem se vyplatí vyšší. Nezapomínejte, že tlak vody se zvyšuje tam, kde se tkanina tře: na ramenou pod popruhy batohu a v místech sedu.</p>'
          '<h2>Typy bund podle konstrukce</h2>'
          '<p>Různé konstrukce se hodí pro různé aktivity. Rozdíl je v počtu vrstev a v tom, co je k membráně přidáno.</p>'
          '<ul><li><strong>Dvouvrstvá bunda:</strong> membrána je laminovaná k vnější tkanině a uvnitř je volná podšívka. Příjemná na dotek, vhodná na běžné nošení a města.</li>'
          '<li><strong>Dvou a půlvrstvá bunda:</strong> místo podšívky je tenká ochranná vrstva, bunda je lehká a skladná, ideální na záložní déšť.</li>'
          '<li><strong>Třívrstvá bunda:</strong> membrána je zalaminovaná mezi vnější tkaninu a vnitřní podšívku. Robustní, odolná, nejlepší pro hory a dlouhé túry.</li>'
          '<li><strong>Pláštěnka a pončo:</strong> jednoduchá ochrana bez prodyšnosti, vhodná na kratší výlety a festivaly.</li>'
          '<li><strong>Zateplená nepromokavá bunda:</strong> kombinuje membránu a izolaci, vhodná na chladné a mokré dny.</li></ul>'
          '<h2>Výběr podle sportu a situace</h2>'
          '<p>Intenzita aktivity určuje, kolik prodyšnosti potřebujete. Na pomalou procházku stačí jednoduchá bunda, při stoupání nebo běhu se potíte víc a bez větrání se uvnitř zahřejete jako v sauně.</p>'
          + T(['Aktivita', 'Co je důležité', 'Tip'], [
              ['Pěší turistika', 'prodyšnost, kapuce, větrací zipy', 'třívrstvá nebo dvou a půlvrstvá bunda s kapucí upravitelnou pro čepici nebo helmu'],
              ['Horolezectví a ferraty', 'odolnost materiálu, kapuce přes helmu', 'výztuže na ramenou a loktech'],
              ['Cyklistika', 'delší záda, zip pod paží, reflexní prvky', 'vyberte střih pro předklon, viz <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>'],
              ['Běh', 'nízká hmotnost, skladnost', 'lehká bunda do kapsy nebo <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a>'],
              ['Město a dojíždění', 'střih, barva, kapuce a kapsy', 'může stačit dvouvrstvá bunda'],
              ['Rybaření a práce venku', 'odolnost, kapsy, delší střih', 'zvažte i <a href="/rybarske-obleceni/">rybářské oblečení</a>'],
              ['Lyžování', 'zateplení a sněhová sukně', 'raději <a href="/lyzarske-bundy/">lyžařské bundy</a>']]) +
          '<h3>Kapuce, límec a manžety</h3>'
          '<p>Dobrá kapuce se přizpůsobí hlavě stahováním ve třech směrech a má výztuhu kšiltu, který odvádí vodu z obličeje. Ověřte, že se vejde přes čepici nebo helmu a že při otáčení hlavy neomezuje výhled. Límec by měl chránit krk bez škrcení. Manžety se suchým zipem nebo elastickým lemem se přizpůsobí rukavicím a brání vniknutí vody ke zápěstí.</p>'
          '<h3>Zipy a kapsy</h3>'
          '<p>Vodotěsné zipy mají pogumovaný povrch a kryt, který zabraňuje vniknutí vody. Klasické zipy jsou lehčí, ale vyžadují lištu nebo chlopeň. Větrací zipy pod pažemi umožní prodyšnost bez sundání bundy. Kapsy by měly být dostatečně hluboké a zapínané, aby se obsah neztratil a nenasákl. Vnitřní kapsa na doklady a telefon se hodí v dešti nejvíc.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Nepromokavá bunda se nosí přes další vrstvy, a proto by měla mít prostor. Příliš těsná bunda zhorší prodyšnost a znemožní vrstvení, příliš volná propouští vítr a vlhkost. Při zkoušení ji oblékněte přes mikinu nebo <a href="/funkcni-mikiny/">funkční mikinu</a> a prověřte, zda se pohybuje s tělem. Zvedněte ruce nad hlavu a ověřte, že se spodní lem nezvedá nad pas.</p>'
          '<ul><li>Pro sport si zvolte delší záda, aby se při předklonu nevyhrnula.</li>'
          '<li>Pro děti kupujte s malou rezervou, ale ne přehnanou, protože příliš velká bunda překáží.</li>'
          '<li>Dámské střihy respektují užší ramena a boky, pánské jsou rovnější.</li>'
          '<li>Vždy zkontrolujte tabulku velikostí konkrétní značky, rozdíly jsou značné.</li></ul>'
          '<h2>Vrstvení pod bundou</h2>'
          '<p>Bunda sama nehřeje, pouze chrání. Teplo vzniká pod ní. Nejlépe funguje trojvrstvový systém: spodní vrstva odvádí pot, střední zahřívá a vnější chrání. Pro první vrstvu volte <a href="/termopradlo/">termoprádlo</a> nebo <a href="/merino/">merino</a>, pro střední <a href="/fleecove-mikiny/">fleecové mikiny</a> a pro chladné počasí lehkou zateplenou vestu z kategorie <a href="/sportovni-vesty/">sportovní vesty</a>. Bavlna pod nepromokavou bundou je špatná volba, protože drží vlhkost a rychle chladne.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Ve výběru najdete značky ' + B(('trespass', 'Trespass'), ('regatta', 'Regatta'), ('dare2b', 'Dare2b'), ('viking', 'Viking'), ('columbia', 'Columbia'), ('helly-hansen', 'Helly Hansen'), ('reima', 'Reima'), ('northfinder', 'Northfinder'), ('kilpi', 'Kilpi'), ('quechua', 'Quechua'), ('haglofs', 'Haglöfs'), ('husky', 'Husky'), ('trimm', 'Trimm'), ('the-north-face', 'The North Face'), ('didriksons', 'Didriksons'), ('fjallraven', 'Fjällräven')) + '. Najdete tu jak specializované horské značky, tak výrobce s dětským sortimentem a dostupnější modely pro každodenní použití. Srovnávejte konkrétní parametry, nikoli pověst značky.</p>'
          '<h2>Nepromokavé kalhoty a doplňky</h2>'
          '<p>Bunda chrání horní polovinu těla, ale voda stéká po nohou do bot. Při dlouhém dešti se vyplatí lehké nepromokavé kalhoty, které se vejdou do batohu a navléknou se přes <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>. Důležité jsou zipy po stranách nohavic, aby je šlo obléknout přes boty. Ruce a hlavu chrání <a href="/sportovni-rukavice/">rukavice</a> a <a href="/cepice-a-celenky/">čepice</a>. Batoh v dešti ochraňte pláštěnkou nebo vodotěsným vakem, protože <a href="/turisticke-batohy/">turistické batohy</a> většinou nejsou zcela nepromokavé.</p>'
          '<h2>Dětské nepromokavé bundy</h2>'
          '<p>Děti se v dešti pohybují, skáčou do kaluží a lezou po hřišti, takže potřebují bundu odolnou a pohodlnou. Hledejte pružnější materiál, odnímatelnou kapuci pro bezpečnost při šplhání a reflexní prvky. Bunda s fleecovou podšívkou je vhodná na podzim, tenká jednovrstvá na jaro a léto. Pozor na délku rukávů, ať nezakrývají prsty, a na zipy, které děti zvládnou samy.</p>'
          '<h2>Skladování a balení do batohu</h2>'
          '<p>Záložní bunda patří na dno batohu nebo do horní kapsy, aby byla po ruce, když přijde bouřka. Pokud je skladná, srolujte ji do vlastní kapsy a nenechávejte ji stlačenou týdny, protože membrána trpí na místech ostrých ohybů. Po použití bundu rozevřete a nechte oschnout, než ji uložíte.</p>'
          '<h2>Péče a impregnace</h2>'
          '<p>Membrána i impregnace potřebují péči. Špína, pot a mastnota ucpávají póry a snižují prodyšnost. Bundu perte podle štítku speciálním prostředkem pro funkční textil, ne běžným práškem a nikdy s aviváží. Aviváž zanechává film, který membránu zalepí. Po vyprání se hodí krátké vyhřátí v sušičce na nízkou teplotu, pokud to štítek dovoluje, protože teplo oživí povrchovou úpravu.</p>'
          '<ul><li>Zavřete všechny zipy a suché zipy, než bundu vložíte do pračky.</li>'
          '<li>Perte při nízké teplotě a s dodatečným máchacím cyklem.</li>'
          '<li>Když voda přestane perlit, obnovte impregnaci sprejem nebo prostředkem do pračky.</li>'
          '<li>Skladujte bundu vyvěšenou, ne stlačenou ve sbaleném stavu.</li>'
          '<li>Poškozené místo lze opravit samolepicí záplatou nebo opravit v servisu.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Vybrat podle vodního sloupce a ignorovat prodyšnost a švy.</li>'
          '<li>Koupit bundu „na deštivé dny“ do města a použít ji na namáhavou túru.</li>'
          '<li>Podcenit kapuci, která pak neudrží tvar nebo neleze přes helmu.</li>'
          '<li>Prát bundu s aviváží nebo ji žehlit.</li>'
          '<li>Očekávat, že jedna bunda zvládne zimu i léto bez vrstvení.</li>'
          '<li>Nechat bundu zabalenou mokrou v batohu.</li></ul>'
          '<h2>Barva a viditelnost</h2>'
          '<p>Za špatného počasí a v šeru se vyplatí výrazná barva nebo reflexní doplňky. Na horách usnadní záchranářům hledání a ve městě zvyšuje bezpečnost chodce a cyklisty. Tmavé bundy jsou praktičtější z hlediska špíny, ale pro večerní aktivity zvažte reflexní proužky na zádech a rukávech. Zkontrolujte, zda reflexní potisk nepraská po praní, to je častá slabina levnějších modelů.</p>'
          '<h2>Kdy bundu vyměnit</h2>'
          '<p>Pokud po obnovení impregnace stále propouští, vrstva membrány se začíná odlupovat uvnitř nebo švy pouštějí, nastal čas na novou. Délka životnosti závisí na intenzitě používání a péči. Pro nenáročné využití vydrží bunda mnoho let, při každodenním tahu s batohem se opotřebovává rychleji. Staré ještě funkční kusy se hodí jako záložní vrstva do kufru auta.</p>',
    faq=[('Co znamená vodní sloupec?', 'Výška sloupce vody v milimetrech, kterou tkanina vydrží, než ji voda začne propouštět. Čím vyšší hodnota, tím větší odolnost vůči dešti a tlaku, ale roli hrají i švy a zipy.'),
         ('Jaký je rozdíl mezi nepromokavou a voděodolnou bundou?', 'Nepromokavá má membránu nebo laminaci a zatmelené švy a zastaví vytrvalý déšť. Voděodolná zvládne pouze lehkou mží a krátký déšť.'),
         ('Jak často je potřeba bundu impregnovat?', 'Když voda přestane perlit a tkanina nasákne. U pravidelně používaných bund to bývá po několika praních, u zřídka nošených déle.'),
         ('Mohu nepromokavou bundu prát v pračce?', 'Ano, podle štítku, s prostředkem na funkční textil, bez aviváže a při nižší teplotě. Před praním zapněte všechny zipy.'),
         ('Je Gore-Tex nutný?', 'Ne. Kvalitní membrány mají i jiné značky a řada výrobců vyvíjí vlastní. Důležité jsou parametry, konstrukce a zatmelené švy, ne pouze jméno membrány.'),
         ('Proč se uvnitř bundy potím?', 'Bunda nestačí odvádět pot při vysoké aktivitě, nebo je pod ní špatná vrstva. Pomůže větrání zipy, lehčí spodní vrstva a nebavlněné oblečení.'),
         ('Jakou bundu na kolo?', 'S delšími zády, reflexními prvky, větracími zipy a kapucí, která se vejde pod nebo přes helmu. Prodyšnost je při šlapání zásadní.'),
         ('Hodí se nepromokavá bunda i v zimě?', 'Ano, jako vnější vrstva spolu s teplou střední vrstvou. Na silný mráz hledejte zateplené modely nebo lyžařské bundy.'),
         ('Jak velkou bundu vybrat?', 'Takovou, pod kterou se vejde mikina nebo fleece a která se při zvednutí rukou nestáhne nad pas. Řiďte se tabulkou velikostí výrobce.'),
         ('Dá se bunda opravit?', 'Drobné díry lze zalepit záplatou, poškozené zipy nebo švy opraví servis. Pokud se membrána odlupuje celoplošně, oprava většinou nedává smysl.')],
)

# ------------------------------------------------------------------ fotbal
NEW['fotbal'] = dict(long=True,
    title='Fotbal: míče, rukavice, chrániče a oblečení | Sporteka',
    desc='Fotbalová výbava: míče, brankářské rukavice, chrániče, štulpny, dresy a kopačky. Průvodce výběrem a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Fotbal</strong> je hra, která vypadá jednoduše: míč, hřiště, dva týmy. Jenže kdo někdy hrál na mokré trávě v nevhodné obuvi nebo s příliš těžkým míčem, ví, že vybavení rozhoduje o zábavě a o riziku zranění. Dobrá výbava navíc nemusí být nejdražší, ale musí odpovídat věku, povrchu a úrovni hráče.</p>'
          '<p>Na Sportece najdete fotbalové vybavení z českých obchodů na jednom místě: <a href="/kopacky/">kopačky</a>, <a href="/fotbalove-mice/">fotbalové míče</a>, <a href="/brankarske-rukavice/">brankářské rukavice</a>, <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>, <a href="/dresy/">dresy</a> a <a href="/teplaky/">tepláky</a>. Pomůžeme vám vybrat velikost míče, povrch pro kopačky i ochranu pro začátečníky a děti. Najdete tu i vybavení pro brankáře, tréninkové oblečení a doplňky, které se vám hodí cestou na zápas i zpět domů.</p>',
    guide='<h2>Základní výbava fotbalisty</h2>'
          '<p>Fotbalová výbava se dá rozdělit do tří vrstev: to, co potřebuje každý hráč, to, co potřebuje brankář, a to, co potřebuje trenér nebo rodič. Začínající hráč vystačí s kopačkami, štulpnami, chrániči a dresem. Kdo hraje pravidelně, přidává trénink v teplákách, tašku na vybavení a náhradní míč.</p>'
          + T(['Kus výbavy', 'Pro koho', 'Poznámka'], [
              ['Kopačky', 'všichni hráči v poli', 'podle povrchu, viz <a href="/kopacky/">kopačky</a>'],
              ['Chrániče holení', 'všichni hráči, povinné v zápase', 'velikost podle délky holeně'],
              ['Štulpny', 'všichni hráči', 'drží chrániče na místě'],
              ['Dres a trenýrky', 'zápas i trénink', 'funkční materiál odvádí pot'],
              ['Brankářské rukavice', 'brankáři', 'velikost, střih a materiál dlaně'],
              ['Míč', 'trénink i zápas', 'velikost podle věku'],
              ['Tepláky a bunda', 'rozcvička a chladné dny', 'viz <a href="/teplaky/">tepláky</a> a <a href="/sportovni-bundy/">sportovní bundy</a>']]) +
          '<h2>Fotbalové míče: velikost a typ</h2>'
          '<p>Míč se vybírá podle věku a účelu. Příliš velký a těžký míč dítěti kazí techniku a může způsobit bolest při odrazu. Zápasové míče mají jemnější povrch a přesnější tvar, tréninkové jsou odolnější a lépe snášejí hrubý povrch. Pro volnou hru na hřišti a na kopání s kamarády se hodí robustní míč.</p>'
          + T(['Velikost', 'Typické použití'], [
              ['Velikost 3', 'nejmladší děti a základní cvičení'],
              ['Velikost 4', 'děti v mládežnických kategoriích'],
              ['Velikost 5', 'děti zhruba od 12 let a dospělí'],
              ['Futsal', 'menší míč s nižším odrazem pro halu'],
              ['Plážový fotbal', 'lehčí míč pro písek']]) +
          '<p>Při koupi se dívejte na konstrukci: lepené nebo šité panely, typ vnitřního měchýře a odolnost povrchu. Šité míče jsou odolnější a lépe drží tvar, lepené mají hladší povrch. Míč před použitím nafoukněte na tlak uvedený na ventilku nebo v návodu, příliš tvrdý nebo měkký míč se chová nepředvídatelně. Podrobnější nabídku najdete v kategorii <a href="/fotbalove-mice/">fotbalové míče</a>.</p>'
          '<h2>Kopačky podle povrchu</h2>'
          '<p>Kopačky jsou nejdůležitější kus výbavy a špatný povrch je častou příčinou zranění kotníku a kolena. Základní pravidlo: čím měkčí a mokřejší povrch, tím delší a řidší kolíky. Na tvrdé umělé trávě naopak potřebujete spoustu krátkých výstupků nebo plochou podrážku. Přehled a další informace najdete v kategorii <a href="/kopacky/">kopačky</a> a pro sál v <a href="/salova-obuv/">sálové obuvi</a>.</p>'
          + T(['Povrch', 'Typ podrážky', 'Poznámka'], [
              ['Přírodní tráva, suchá', 'lisované kolíky', 'univerzální volba pro pevný terén'],
              ['Přírodní tráva, mokrá nebo bahnitá', 'vyměnitelné kolíky', 'větší záběr, ale vyšší riziko pro kotník na tvrdém'],
              ['Umělá tráva', 'mnoho krátkých výstupků', 'rozkládají zátěž, bezpečnější pro klouby'],
              ['Tvrdý povrch, antuka', 'plochá nebo mírně profilovaná podrážka', 'hodí se i do přírodních podmínek bez trávy'],
              ['Hala, sál', 'plochá světlá podrážka', 'nesmí zanechávat stopy na podlaze']]) +
          '<p>Při zkoušení kopaček nechte před špičkou zhruba půl centimetru prostoru, ale pata musí sedět pevně. Kopačky mají být uzavřené v kotníku a nesmí tlačit v prstech. Děti rostou rychle, proto kupujte rozumně a ne „na vyrůstání“, kdy by kopačka klouzala a způsobovala puchýře. Při dlouhodobém používání dbejte na čištění a sušení pokojové teploty, ne na topení.</p>'
          '<h2>Brankářské rukavice</h2>'
          '<p>Brankář je jediný hráč, který smí míč chytat do rukou, a rukavice jsou jeho hlavní nástroj. Dlaň z latexu poskytuje přilnavost, ale rychle se opotřebovává a vlhne. Střih určuje, jak rukavice sedí a jak velká je ochrana prstů. Prstní výztuhy omezují zaklesnutí a přeohnutí prstů dozadu, ale snižují citlivost. Začínající brankáři často volí rukavice bez výztuh, které jsou lehčí a snadněji se ovládají.</p>'
          '<p>K tréninku patří i skládací a pevné branky, sítě, kužely, figuríny a další tréninkové pomůcky. U branek sledujte rozměr, stabilitu konstrukce a kotvení, u kuželů a značek barvu a odolnost.</p>'
          '<ul><li><strong>Velikost:</strong> změřte obvod dlaně a porovnejte s tabulkou výrobce. Příliš těsná rukavice zpomaluje, příliš volná sklouzává.</li>'
          '<li><strong>Střih:</strong> klasický, negativní nebo hybridní; liší se prostorem mezi prsty a pevností sevření.</li>'
          '<li><strong>Povrch:</strong> měkčí latex má lepší přilnavost, tvrdší vydrží déle.</li>'
          '<li><strong>Zapínání:</strong> pevné suché zipy a manžeta zlepšují fixaci zápěstí.</li></ul>'
          '<p>Po tréninku rukavice opláchněte, vymačkejte vodu a nechte je přirozeně oschnout. Nikdy nepoužívejte horký vzduch, latex by ztvrdl. Více najdete v kategorii <a href="/brankarske-rukavice/">brankářské rukavice</a>.</p>'
          '<h2>Chrániče a štulpny</h2>'
          '<p>Chrániče holení jsou v zápase povinné a v tréninku silně doporučené. Rozhodující je velikost: správně vybraný chránič pokrývá holeň od kotníku po spodní okraj kolene a nepohybuje se. Dětské modely se nosí s upevněním pod štulpnou, starší hráči často volí pevnější skořepiny. Štulpny drží chrániče na místě a chrání proti odřeninám. Prohlédněte si kategorii <a href="/fotbalove-chranice-a-stulpny/">chrániče a štulpny</a>.</p>'
          '<ul><li>Chránič má sedět tak, aby se nehýbal při běhu.</li>'
          '<li>Pro děti zvolte lehčí a měkčí modely, aby neomezovaly pohyb.</li>'
          '<li>Štulpny perte při nízké teplotě, vysoká teplota poškozuje elastické vlákno.</li>'
          '<li>Chrániče po silném nárazu zkontrolujte, zda nepraskly.</li></ul>'
          '<h2>Dresy, trenýrky a tréninkové oblečení</h2>'
          '<p>Fotbalový dres je z lehkého syntetického materiálu, který odvádí pot a rychle schne. Zápasové střihy sedí těsněji, fanouškovské volněji. Při výběru sledujte prodyšné zóny na zádech a v podpaží a velikost pro sportovní pohyb. Pro trénink v chladu zvolte dres s dlouhým rukávem nebo ho kombinujte s funkčním spodním prádlem. Dresy najdete v kategorii <a href="/dresy/">dresy</a> a pro chladnější dny v sekci <a href="/teplaky/">tepláky</a>, <a href="/mikiny/">mikiny</a> a <a href="/sportovni-bundy/">sportovní bundy</a>.</p>'
          '<p>Na trénink v chladu funguje vrstvení: funkční <a href="/termopradlo/">termoprádlo</a>, dres, tepláková souprava nebo <a href="/soupravy/">souprava</a> pro rozcvičku. Pro teplé dny stačí lehký dres a <a href="/sportovni-kratasy/">sportovní kraťasy</a>. Péče o oblečení je jednoduchá: perte na nízké teplotě, bez aviváže a nežehlete potisk.</p>'
          '<h2>Výbava podle věku a úrovně</h2>'
          '<p>Děti potřebují především bezpečné a lehké vybavení. Měkčí míč velikosti 3 nebo 4, lehké chrániče a pohodlné kopačky s širší špičkou. Starší mládež už zohledňuje povrch a polohu na hřišti. Dospělí rekreanti se zaměří na kombinaci komfortu a odolnosti, protože hrají často na různých površích. Profesionální vybavení má smysl až při pravidelném hraní několikrát týdně.</p>'
          '<h2>Taška, láhev a drobnosti</h2>'
          '<p>Výbavu je potřeba na trénink odnést a po zápase vysušit. Prostorná <a href="/sportovni-tasky/">sportovní taška</a> s oddělenou přihrádkou na obuv oddělí špinavé kopačky od čistého oblečení. K pití se hodí <a href="/lahve-a-termosky/">láhev nebo termoska</a> s dobře těsnícím uzávěrem. Neodmyslitelnou součástí jsou náhradní tkaničky, ručník a náhradní ponožky. V zimě přidejte <a href="/cepice-a-celenky/">čepici</a> a <a href="/sportovni-rukavice/">rukavice</a> na rozcvičku.</p>'
          '<h2>Trénink v zimě a za deště</h2>'
          '<p>Hráči netrénují jen za slunného počasí. Na mokré trávě potřebujete delší kolíky, v mrazu měkčí obuv, která nepraská, a na tělo více vrstev. Pod dres obléknete <a href="/funkcni-tricka/">funkční tričko</a> s dlouhým rukávem, přes něj <a href="/funkcni-mikiny/">funkční mikinu</a> a při dešti lehkou <a href="/vetrovky/">větrovku</a>. Po tréninku se rychle převlékněte do suchého oblečení, abyste se nenachladili. Míč v blátě otřete a po zápase vysušte, jinak se mu zhorší odraz.</p>'
          '<h2>Příprava mimo hřiště</h2>'
          '<p>Hráč, který chce být rychlejší a odolnější, neměl by spoléhat jen na tréninky s míčem. Doma pomohou <a href="/fitness-pomucky/">fitness pomůcky</a>, <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/svihadla/">švihadla</a>. Cviky na stabilitu kotníku a kolen snižují riziko zranění. Po zátěži se hodí <a href="/masazni-pomucky/">masážní pomůcky</a> pro uvolnění svalů.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Na Sportece najdete značky ' + B(('puma', 'Puma'), ('adidas', 'Adidas'), ('powershot', 'Powershot'), ('nike', 'Nike'), ('kipsta', 'Kipsta'), ('merco', 'Merco'), ('select', 'Select'), ('reusch', 'Reusch'), ('hejduk', 'Hejduk'), ('umbro', 'Umbro'), ('joma', 'Joma'), ('acra-sport', 'ACRA Sport'), ('nidelo', 'Nidelo'), ('forza', 'Forza')) + '. Světové sportovní značky pokrývají celé spektrum od kopaček po dresy, specialisté nabízejí míče, rukavice nebo chrániče. Porovnávejte parametry a recenze konkrétních modelů, ne jen logo.</p>'
          '<h2>Péče o fotbalovou výbavu</h2>'
          '<ul><li>Kopačky po zápase očistěte od hlíny a trávy, vyndejte vložky a nechte vyschnout při pokojové teplotě.</li>'
          '<li>Míče nenechávejte na slunci ani v mrazu, tlak se mění a materiál stárne rychleji.</li>'
          '<li>Dresy perte naruby, aby se chránily potisky a znaky.</li>'
          '<li>Rukavice po tréninku opláchněte a nesušte na topení.</li>'
          '<li>Tašku na vybavení větrejte, aby se nedržel pach a plíseň.</li></ul>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Koupit kopačky na jiný povrch, než na jakém se hraje.</li>'
          '<li>Vybrat dětem příliš velký míč nebo „na vyrůstání“ velké kopačky.</li>'
          '<li>Hrát bez chráničů nebo s těmi, které se při běhu posouvají.</li>'
          '<li>Pořídit brankářské rukavice bez kontroly velikosti a střihu.</li>'
          '<li>Kupovat podle módy značky a ignorovat sedění a parametry.</li>'
          '<li>Opomíjet drobné doplňky, jako jsou náhradní tkaničky nebo jehla na dofouknutí míče.</li></ul>'
          '<h2>Jak často trénovat a co sledovat</h2>'
          '<p>Rekreační hráč si vystačí s jedním až dvěma tréninky týdně, mládež trénuje častěji. Po každém tréninku zkontrolujte, zda nejsou kopačky opotřebované, kolíky nejsou ulomené a míč neztrácí tlak. Drobná kontrola ušetří zranění i peníze za předčasnou výměnu.</p>'
          '<h2>Jak sestavit výbavu postupně</h2>'
          '<p>Nemusíte koupit všechno najednou. Začněte tím, co přímo ovlivňuje bezpečnost: kopačky a chrániče. Potom doplňte funkční dres a štulpny. Míč pro trénink, případně brankářské rukavice a tepláky přidejte v další fázi. Sledujte, co skutečně používáte, a nakupujte podle toho. Pokud hrajete i v hale, doplňte sálovou obuv, protože jedny kopačky nezvládnou všechny povrchy.</p>',
    faq=[('Jakou velikost míče koupit pro dítě?', 'Velikost 3 pro nejmladší, 4 pro děti v mládežnických kategoriích a 5 pro děti zhruba od 12 let a dospělé. Příliš velký míč kazí techniku a zvyšuje riziko bolesti.'),
         ('Jaké kopačky zvolit na umělou trávu?', 'Takové, které mají mnoho krátkých výstupků nebo speciální podrážku pro umělý povrch. Rozkládají zátěž a snižují zatížení kloubů.'),
         ('Jak vybrat velikost brankářských rukavic?', 'Změřte obvod dlaně a porovnejte s tabulkou výrobce. Rukavice mají sedět pevně, ale nesmí omezovat pohyb prstů.'),
         ('Jsou chrániče holení povinné?', 'V zápase ano, pro trénink je silně doporučujeme. Chrání holeň před nárazem a kopnutím a nic nestojí za rizikem zlomeniny.'),
         ('Jak velké chrániče koupit?', 'Chránič má pokrývat holeň od kotníku po spodní okraj kolene a nesmí se při běhu posouvat. Velikost se řídí délkou holeně, ne věkem.'),
         ('Jak prát fotbalový dres?', 'Naruby, při nízké teplotě, bez aviváže a bez žehlení potisku. Tím se prodlouží životnost znaků a čísel.'),
         ('Co je futsal a čím se liší míč?', 'Futsal je sálová varianta fotbalu. Míč je menší a má nižší odraz, aby se na hladké podlaze lépe kontroloval.'),
         ('Jak často měnit kopačky?', 'Podle opotřebení a růstu nohy. Děti často každou sezónu, dospělí tehdy, když povolí upevnění, popraská podrážka nebo se zničí kolíky.'),
         ('Jak uchovávat míč?', 'Mimo mráz a přímé slunce, nafouknutý na doporučený tlak. Před použitím zkontrolujte tlak a případně dofoukněte.'),
         ('Co všechno potřebuje začínající fotbalista?', 'Kopačky odpovídající povrchu, chrániče, štulpny, dres a kraťasy. Další věci, jako rukavice pro brankáře nebo tepláky, doplníte podle potřeby.')],
)
