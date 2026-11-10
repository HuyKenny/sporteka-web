"""sporteka.cz — wave 12d (4. 11. 2026): long texts for fitness, sportovni-kratasy, lyzarske-obleceni, plavky. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ fitness
NEW['fitness'] = dict(long=True,
    title='Fitness a posilování: činky, stroje, pomůcky | Sporteka',
    desc='Fitness a posilování doma i v posilovně: činky, kettlebelly, lavice, rotopedy, gumy a hrazdy. Porovnejte nabídku českých obchodů na jednom místě.',
    intro='<p><strong>Fitness a posilování</strong> doma se dá vybavit mnoha způsoby a většina z nich končí zbytečným nákupem. Rozhodující je odpověď na tři otázky: kolik máte místa, jak často budete cvičit a zda chcete hlavně sílu, kondici, nebo mobilitu. Teprve podle toho se hodí buď sada <a href="/cinky-a-kotouce/">činek a kotoučů</a>, nebo <a href="/posilovaci-gumy/">posilovací gumy</a>, nebo <a href="/kardio-trenazery/">rotoped</a>.</p>'
          '<p>Sporteka sbírá nabídku českých e-shopů do jednoho přehledu: od <a href="/kettlebelly/">kettlebellů</a> a <a href="/posilovaci-stroje/">posilovacích strojů</a> přes <a href="/svihadla/">švihadla</a> až po <a href="/masazni-pomucky/">masážní pomůcky</a> a <a href="/bandaze-a-ortezy/">bandáže</a>. Průvodce níže vysvětluje, jak si sestavit domácí posilovnu postupně, na co se při výběru dívat a jak se vyhnout nákupům, které později leží v koutě.</p>',
    guide='<h2>Jak si postavit domácí posilovnu krok za krokem</h2>'
          '<p>Nejčastější chybou je koupit objemný stroj dřív, než se z cvičení stane zvyk. Funguje opačný postup: začněte věcmi, které zabírají málo místa a dají se využít na stovku cviků, a teprve po několika měsících pravidelného tréninku přidávejte specializované vybavení. Nadšení v lednu bývá velké, v dubnu už se ukáže, co opravdu používáte.</p>'
          + T(['Cíl', 'Co zvolit jako první', 'Kde hledat'], [
              ['Obecná kondice a zdraví', 'švihadlo, odporové gumy, podložka, malé činky', '<a href="/fitness-pomucky/">fitness pomůcky</a>'],
              ['Nárůst síly a svalů', 'nastavitelné činky, lavice, později osa a kotouče', '<a href="/cinky-a-kotouce/">činky a kotouče</a>, <a href="/posilovaci-stroje/">lavice</a>'],
              ['Spalování energie a vytrvalost', 'rotoped, eliptický trenažér, švihadlo', '<a href="/kardio-trenazery/">rotopedy a trenažéry</a>'],
              ['Pohyblivost a držení těla', 'podložka, bloky, balanční pomůcky', '<a href="/joga-a-pilates/">jóga a pilates</a>, <a href="/balancni-pomucky/">balanční pomůcky</a>'],
              ['Trénink s vlastním tělem', 'hrazda, bradla, kruhy, gumy', '<a href="/funkcni-trenink/">funkční trénink</a>'],
              ['Regenerace po zátěži', 'masážní válec, míčky, pistole', '<a href="/masazni-pomucky/">masážní pomůcky</a>']]) +
          '<h3>Činky, kotouče a kettlebelly</h3>'
          '<p>Jednoruční činky jsou nejuniverzálnější základ. Hodí se na tlaky, veslování, výpady i cviky na paže a ramena. Pevné činky jsou stabilní a nic se na nich neuvolní, nastavitelné šetří místo a zastoupí celou řadu hmotností, ale jejich výměna zabere čas při rychlých sestavách. U kotoučů sledujte průměr otvoru, protože musí odpovídat ose. Standardní a olympijský průměr nejsou zaměnitelné, a pokud koupíte špatně, kotouče na osu nenasadíte.</p>'
          '<p>Kettlebell je koule s madlem, jejíž těžiště leží mimo ruku. Proto se s ní dobře švihá, přenáší a drží nad hlavou. Kdo začíná, potřebuje spíš jednu střední váhu než celou řadu. Širší madlo se hodí pro cviky oběma rukama, hladký povrch zase nepoškodí dlaně. Veškerou nabídku shrnuje kategorie <a href="/kettlebelly/">kettlebelly</a>.</p>'
          '<h3>Lavice, stojany a posilovací stroje</h3>'
          '<p>Lavice s nastavitelným sklonem rozšíří možnosti činek na horní i dolní polohu. Rozhodující je nosnost a stabilita, ne počet poloh opěrky. Při nákupu se podívejte, zda se opěradlo zaklapne bez vůle a zda lavice nejezdí po podlaze. Stojany, věže a multifunkční stroje dávají smysl až u pravidelného tréninku. Zabírají velkou část místnosti, takže je změřte předem, včetně výšky stropu nad hlavou při tlacích. Přehled je v kategorii <a href="/posilovaci-stroje/">posilovací stroje a lavice</a>.</p>'
          '<h2>Kardio: rotopedy, trenažéry a švihadla</h2>'
          '<p>Rotoped je tichý a šetrný ke kolenům i kyčlím, eliptický trenažér zapojuje horní polovinu těla a běžecký pás nejvěrněji napodobuje chůzi a běh. Rozhodující je plynulost chodu, tichost, stabilita rámu a nastavitelnost sedla nebo řídítek. Vysoký člověk potřebuje delší rozsah posuvu, jinak se neustále hrbí. Magnetický odpor je tichý a nevyžaduje údržbu, mechanický třecí pásek je jednodušší, ale opotřebovává se.</p>'
          '<p>Švihadlo je nejlevnější a nejefektivnější způsob, jak rozproudit krevní oběh. Začátečníkovi vyhovuje delší lanko nebo lehká rukojeť, pokročilému rychlé lanko s ložisky. Délku nastavte tak, aby po došlápnutí na střed lanka končila madla zhruba v úrovni podpaží. Dopadejte na špičky na tvrdší, ale pružnou podložku, ne na beton. Najdete je v kategorii <a href="/svihadla/">švihadla</a>.</p>'
          '<h2>Pomůcky pro cvičení bez velkého vybavení</h2>'
          '<h3>Posilovací gumy a expandery</h3>'
          '<p>Odporové gumy mají tu výhodu, že odpor roste s protažením. Smyčky se hodí na nohy a hýždě, dlouhé pásy na záda a ramena, trubicové s madly napodobují kladky. Pořiďte raději dvě až tři různé tuhosti než jednu. Slabá guma slouží na zahřátí a rehabilitaci, silná na hlavní sérii. Před každým cvičením ji zkontrolujte, zda není naříznutá, protože praskající guma může zasáhnout do tváře. Vše v kategorii <a href="/posilovaci-gumy/">posilovací gumy a expandery</a>.</p>'
          '<h3>Balanční a stabilizační pomůcky</h3>'
          '<p>Balanční podložky, půlkoule a velké míče nutí hluboké svaly trupu a kolem kloubů pracovat na udržení rovnováhy. Využijete je při rehabilitaci kotníku, zlepšování stability i jako zpestření tréninku. Nepřeceňujte je jako hlavní nástroj síly, protože při nestabilním podkladu nezvednete takovou zátěž jako na pevné zemi. Prohlédněte si <a href="/balancni-pomucky/">balanční pomůcky</a>.</p>'
          '<h3>Hrazdy, bradla a funkční trénink</h3>'
          '<p>Hrazda je jedno z nejpřínosnějších zařízení do malého bytu. Zavěšená do dveří, upevněná na zeď nebo samostatně stojící umožní shyby, zavěšené zdvihy nohou i protahování zad. Rozhodující je způsob uchycení, nosnost a kvalita zdi nebo zárubně. Bradla přidávají kliky a dipy, kruhy a TRX popruhy zase cviky na nestabilním závěsu. Souhrn nabízí <a href="/funkcni-trenink/">funkční trénink a hrazdy</a> a podkategorie <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</p>'
          '<h2>Regenerace, ochrana kloubů a oblečení</h2>'
          '<p>Po tréninku pomáhají masážní válce, míčky a nástavce uvolnit napjaté partie. Tvrdší povrch působí hlouběji, ale hůře se snáší. Válec používejte pomalu, bez bolesti do kloubů a nikdy přímo na bederní páteř. Nabídku najdete v <a href="/masazni-pomucky/">masážních pomůckách</a>.</p>'
          '<p>Bandáže, ortézy a ovazy podpírají kloub, ale žádný pás nevyléčí špatnou techniku. Na zápěstí a kolena se obvykle používá elastický návlek, na bedra opasek při těžkých dřepech a mrtvých tazích. Při vleklých potížích je správná cesta k lékaři nebo fyzioterapeutovi. Přehled je v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>'
          '<p>Oblečení do posilovny má být pružné a prodyšné. Doplňte si <a href="/leginy/">legíny</a>, <a href="/sportovni-tricka/">sportovní trička</a> a <a href="/sportovni-podprsenky/">sportovní podprsenky</a> s odpovídající oporou. Obuv volte s pevnou, plochou podrážkou, třeba z kategorie <a href="/treninkova-obuv/">fitness a tréninková obuv</a>, protože měkká běžecká podrážka při těžkém dřepu nestabilizuje.</p>'
          '<h2>Výběr podle prostoru a rozpočtu času</h2>'
          '<p>Při malém prostoru se hodí vybavení, které se dá schovat do skříně: gumy, švihadlo, podložka, jeden kettlebell a hrazda do dveří. V samostatné místnosti nebo na balkoně se vyplatí stojan s osou, lavice a pár kotoučů. Změřte nejen plochu podlahy, ale i prostor kolem, protože při cvicích s osou potřebujete na každé straně volné místo, a při tlacích nad hlavou dostatečnou výšku stropu.</p>'
          '<p>Stejně důležitý jako místo je čas. Tři krátké tréninky týdně pro celé tělo jsou pro začátečníka lepší než jeden dlouhý a vyčerpávající. Rozdělte si je třeba na tlaky, tahy a nohy a mezi nimi nechte den odpočinku. Rotoped nebo švihadlo se hodí na dny mezi silovými tréninky, protože zátěž rozloží a podpoří regeneraci. Vybavení, které je po ruce a nevyžaduje dlouhou přípravu, se používá častěji než takové, které je potřeba složitě rozkládat.</p>'
          '<h3>Jak poznat, že je čas přidat zátěž</h3>'
          '<p>Pokud zvládáte všechna opakování ve všech sériích s čistou technikou a poslední série už není náročná, je čas přidat o něco málo víc. Malé kroky jsou bezpečnější než velké skoky. U nastavitelných činek je to snadné, u pevných je dobré mít mezi hmotnostmi menší rozestup. Pokud zátěž přidáváte, ale technika se kazí, vraťte se o krok zpět.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Katalog Sportek zahrnuje značky ' + B(('hms', 'HMS'), ('insportline', 'Insportline'), ('merco', 'Merco'), ('sedco', 'Sedco'), ('gymbeam', 'GymBeam'), ('sportago', 'Sportago'), ('domyos', 'Domyos'), ('hop-sport', 'Hop-sport'), ('gorilla-sports', 'Gorilla Sports')) + '. Rozdíl nehledejte jen v logu. Sledujte nosnost, materiál svarů, způsob pokovení, délku záruky a to, zda lze snadno dokoupit náhradní díly.</p>'
          '<h2>Časté chyby při nákupu a cvičení</h2>'
          '<ul><li><strong>Příliš těžké vybavení hned na začátku:</strong> technika trpí a hrozí přetížení šlach.</li>'
          '<li><strong>Nezměřený prostor:</strong> stroj se nevejde nebo zakrývá dveře.</li>'
          '<li><strong>Špatný průměr osy a kotoučů:</strong> součásti k sobě nepasují.</li>'
          '<li><strong>Vynechání rozcvičky:</strong> studené svaly a klouby jsou zranitelnější.</li>'
          '<li><strong>Jedna pomůcka na všechno:</strong> pestrost tréninku udržuje motivaci.</li>'
          '<li><strong>Chybějící podložka pod stroj:</strong> hluk a poškozená podlaha v paneláku.</li></ul>'
          '<h2>Péče o vybavení a bezpečnost</h2>'
          '<p>Kovové části otírejte od potu, protože sůl koroduje i pochromované povrchy. Šrouby na lavicích a stojanech dotahujte po prvních týdnech a pak čas od času. Pryžové kotouče a podložky skladujte mimo přímé slunce a topení. Při cvičení s velkou zátěží pomáhá spolucvičenec nebo bezpečnostní zarážky. Domácí trénink v bytě navíc počítá se sousedy: pogumované kotouče a silná podložka sníží hluk dopadu.</p>'
          '<p>Při bolestech, zdravotních omezeních nebo po delší pauze se předem poraďte s lékařem či trenérem. Rozumný plán s dostatkem spánku a odpočinku přinese víc než maximální zátěž každý den. Až budete vědět, co potřebujete, porovnejte nabídky obchodů na Sportece a vybírejte podle parametrů, ne podle slibů v popisu.</p>',
    faq=[('Čím začít s domácím posilováním?', 'Stačí podložka, odporové gumy, pár jednoručních činek nebo jeden kettlebell a švihadlo. Tahle sada zabere málo místa a pokryje celé tělo. Další vybavení kupujte až podle toho, co vám při pravidelném cvičení skutečně chybí.'),
         ('Jsou lepší pevné, nebo nastavitelné činky?', 'Pevné jsou stabilnější, rychle se mění a nic se nepovolí. Nastavitelné šetří místo a nahradí celou sadu, ale výměna kotoučů trvá. Pokud trénujete v malém bytě, vyhrají nastavitelné, v prostorné posilovně pevné.'),
         ('Jak poznám, jaký průměr osy kotouče potřebuji?', 'Změřte otvor v kotouči a průměr konce osy nebo si přečtěte parametry v popisu. Standardní a olympijský průměr se liší a nelze je zaměňovat. Kupujte osu a kotouče ze stejného systému.'),
         ('Hodí se rotoped nebo eliptický trenažér spíš?', 'Rotoped je šetrnější ke kloubům a tišší, eliptický trenažér zapojí i horní část těla. Vyzkoušejte, který z nich vám při dlouhém cvičení sedí. Důležitější než typ je to, že ho budete používat pravidelně.'),
         ('Jaká hrazda je vhodná do bytu?', 'Do dveří se hodí hrazdy bez vrtání, do zdi pevnější vrtané. Zkontrolujte nosnost, tloušťku zárubně a materiál zdi. Samostatně stojící konstrukce nepoškodí byt, ale zabere místo.'),
         ('Jak poznám správnou tuhost odporové gumy?', 'Správná guma dovolí provést zamýšlený počet opakování se zachovanou technikou a poslední jsou náročná. Pokud dokážete bez námahy dvacet opakování, zvolte silnější. Pokud se technika rozpadá už po pěti, vezměte slabší.'),
         ('Mám cvičit s bandáží a ortézou?', 'Běžně ne. Bandáž může při těžké zátěži poskytnout oporu, ale neléčí potíže. Při vleklé bolesti kloubu cvičení omezte a poraďte se s lékařem nebo fyzioterapeutem, který určí vhodnou ochranu.'),
         ('Jak často masírovat svaly válcem?', 'Válec lze použít po tréninku nebo v dny odpočinku, každou partii zhruba jednu až dvě minuty pomalým pohybem. Nemá bolet do kloubů ani do bederní páteře. Při akutním zranění ho nepoužívejte.'),
         ('Jak snížit hluk při cvičení v panelovém domě?', 'Pod činky a stroje dejte silnou pryžovou podložku, volte pogumované kotouče a nepouštějte závaží na zem z výšky. Skákací cviky a švihadlo přeneste na tlumicí podložku. Zvažte také čas, kdy sousedé odpočívají.'),
         ('Na co si dát pozor u levného vybavení?', 'Sledujte nosnost, tloušťku materiálu, kvalitu svarů a dostupnost náhradních dílů. U zařízení, na kterém stojíte nebo nad kterým zvedáte váhu, je bezpečnost důležitější než ušetřená částka. Porovnání nabídek na Sportece vám pomůže najít rozumný kompromis.')]
)

# ------------------------------------------------------------------ sportovni-kratasy
NEW['sportovni-kratasy'] = dict(long=True,
    title='Sportovní kraťasy: běžecké, fitness, outdoor | Sporteka',
    desc='Sportovní kraťasy na běh, fitness, fotbal, kolo a turistiku: střihy, délky, materiály a velikosti. Porovnejte nabídku českých obchodů a značek.',
    intro='<p><strong>Sportovní kraťasy</strong> vypadají jednoduše, ale rozdíl mezi dobrými a špatnými poznáte po prvním kilometru. Na běh potřebujete lehké a prodyšné, do posilovny pružné a neprůhledné, na turistiku odolné a rychleschnoucí a na kolo zase vycpané. Jeden pár všechny situace nepokryje, i když existují univerzální střihy, které se hodí na většinu aktivit. Vyplatí se proto vědět, co od kraťasů čekáte, ještě než otevřete první nabídku, a mít po ruce alespoň dva různé páry.</p>'
          '<p>Na Sportece najdete kraťasy z českých obchodů pohromadě a můžete je porovnat podle značky, materiálu i velikosti. Pro doplnění outfitu se hodí <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/leginy/">legíny</a> a <a href="/sportovni-ponozky/">sportovní ponožky</a>. Průvodce níže vysvětluje délky, vnitřní kalhotky, materiály, péči i nejčastější omyly, abyste vybrali pár, který vám opravdu sedne.</p>',
    guide='<h2>Jak vybrat sportovní kraťasy</h2>'
          '<p>Nejdřív si odpovězte, co v nich budete dělat. Teprve potom řešte barvu a značku. Ke každé činnosti patří jiné požadavky na střih, materiál a kapsy a právě tahle volba rozhoduje o komfortu. Kraťasy na běh mají často integrované slipy nebo vnitřní kalhotky, fitness model se naopak obejde bez nich a klade důraz na pružnou látku.</p>'
          + T(['Aktivita', 'Vhodný střih a materiál', 'Na co dát pozor'], [
              ['Běh', 'lehký polyester, někdy s vnitřními slipy, krátká až střední délka', 'švy, které neodírají, kapsa na klíče nebo telefon'],
              ['Fitness a posilovna', 'pružná tkanina, nepřetahující střih, nepropustný při dřepu', 'neprůhlednost, držení pasu'],
              ['Fotbal a týmové sporty', 'volný střih, lehký umělý materiál, často s vnitřními slipy', 'volnost pro kopání, barvy týmu'],
              ['Basketbal', 'delší volné kraťasy po kolena nebo pod ně', 'zachování volnosti ve výskoku'],
              ['Turistika a outdoor', 'rychleschnoucí pevný materiál, kapsy na zip', 'odolnost, ochrana proti oděru'],
              ['Cyklistika', 'vycpaná vložka a přiléhavý střih nebo volnější MTB kraťasy', 'vložka musí sedět k typu sedla'],
              ['Plavání a pláž', 'rychleschnoucí šortky nebo plavecké kraťasy', 'odolnost vůči chlóru a soli']]) +
          '<h3>Délka nohavice</h3>'
          '<p>Krátké kraťasy s délkou nohavice kolem poloviny stehna se hodí na běh, protože nic nebrání v kroku. Střední délka k okraji kolena je univerzální, na posilování i kolektivní hry. Dlouhé po kolena pasují k basketbalu a streetovému stylu, v lese nebo na turistice zase chrání před kopřivami a větvemi. Při výběru myslete také na to, kam sahají vaše vlastní stehna, protože stejný střih sedí každému jinak.</p>'
          '<h3>Vnitřní slipy, spandexové podkalhotky a volné kraťasy</h3>'
          '<p>Dvouvrstvé kraťasy mají vnější volnou vrstvu a vnitřní přiléhavou. Vnitřní vrstva drží tělo, zabraňuje oděru stehen a nahrazuje spodní prádlo, zatímco vnější nechává vzduch cirkulovat. Jednovrstvé kraťasy jsou lehčí a vhodné k nošení s vlastním funkčním spodním prádlem z kategorie <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>. Přiléhavé kompresní kraťasy se nosí samostatně nebo pod volnou vrstvou a podporují svaly.</p>'
          '<p>Pokud trpíte oděrem stehen na delších trasách, zvolte přiléhavý střih z hladkého materiálu a bez tlustých švů. V horku se vyplatí volnější, prodyšné kraťasy se síťovinou po stranách.</p>'
          '<h2>Materiály a vlastnosti</h2>'
          '<p>Většina sportovních kraťasů je z polyesteru, často s příměsí elastanu. Polyester rychle schne a nenasákne potem, elastan dodává pružnost, takže se kraťasy přizpůsobí pohybu. Bavlna příjemně působí v klidu, ale po zpocení zůstává těžká a vlhká, takže se hodí spíš na volný čas než na výkon. Nylon je pevný a oděruvzdorný, proto ho najdete v turistických modelech. Merino se u kraťasů objevuje zřídka, častěji u triček a ponožek.</p>'
          '<ul><li><strong>Prodyšnost:</strong> otvory nebo síťovina v bocích odvádějí teplo.</li>'
          '<li><strong>Rychleschnoucí povrch:</strong> důležitý při dešti a při několikadenní túře.</li>'
          '<li><strong>Elastický pas se šňůrkou:</strong> drží při pohybu a dá se doladit.</li>'
          '<li><strong>Kapsy se zipem:</strong> nic z nich nevypadne při běhu nebo na kole.</li>'
          '<li><strong>Reflexní prvky:</strong> uplatní se při běhání za šera.</li></ul>'
          '<h2>Kraťasy podle sportu a sezóny</h2>'
          '<h3>Běh a atletika</h3>'
          '<p>Běžec chce nejlehčí kus, který se nehýbe. U kraťasů s vnitřními slipy odpadá nutnost spodního prádla, což snižuje riziko otlaků na dlouhých tratích. Kapsa vzadu nebo na boku se hodí na klíče a gel. Širší nabídku sportu najdete v kategorii <a href="/beh/">běh, triatlon a atletika</a>.</p>'
          '<h3>Fitness a joga</h3>'
          '<p>V posilovně hlídejte hlavně neprůhlednost a pevnost tkaniny. Dřep a mrtvý tah odhalí slabou látku okamžitě. Pro cvičení na zemi pasují těsnější střihy, které se nepřetáčejí při předklonech. Po výběru dolní části doplňte <a href="/mikiny/">mikinu</a> pro cestu domů. Souvisí s tím i kategorie <a href="/fitness/">fitness a posilování</a>.</p>'
          '<h3>Kolo</h3>'
          '<p>Silniční cyklistika potřebuje přiléhavé kraťasy s vložkou, MTB volnější střih s pevnějším materiálem na kolenou a bocích. Vložka musí odpovídat délce tras a typu sedla. Samostatně se těmto kusům věnuje kategorie <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a>.</p>'
          '<h3>Hory a turistika</h3>'
          '<p>Turistické kraťasy mají pevnější materiál, kapsy se zipem a často prodloužený střih. V horách se počasí mění, takže je dobré mít po ruce i <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a> s odepínacími nohavicemi nebo lehké kalhoty do chladu. V zimě kraťasy navlečte přes <a href="/termopradlo/">funkční termoprádlo</a>, pokud trénujete venku.</p>'
          '<h3>Pláž a voda</h3>'
          '<p>Plavecké kraťasy a šortky schnou rychle a nenasákají. Pro pravidelné plavání jsou pohodlnější přiléhavé <a href="/panske-plavky/">pánské plavky</a>, v bazénech se někdy volné šortky nesmějí nosit. Pravidla si ověřte předem.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Velikost vyberte podle obvodu pasu a boků v tabulce výrobce, ne podle vlastního odhadu. Značky mají různé střihy, takže stejné označení nemusí znamenat stejnou míru. Pas by měl sedět pevně, aby nesjížděl, ale neměl by tlačit do břicha při předklonu. Zkuste v nich dřep, výpad a zvednutí kolene. V e-shopu hledejte informace o střihu, jako jsou slim, regular nebo relaxed, a zjistěte, jak dlouho můžete zboží vrátit.</p>'
          '<h2>Dámské, pánské a dětské kraťasy</h2>'
          '<p>Dámské střihy mají obvykle užší pas, širší boky a kratší nohavici, často s vysokým pasem, který drží břicho a zakryje při předklonu záda. Pánské jsou volnější v bocích a delší. Unisex modely se hodí pro týmové sporty a volný čas, ale u přesného sportovního výkonu je lepší střih určený pro vaši postavu. Při štíhlých stehnech pomůže vnitřní vrstva s pevným lemem, který neklouže, a při širších bocích zase střih s elastickým pasem, který se nezarývá.</p>'
          '<p>U dětí se vyplatí kupovat o něco větší velikost s nastavitelným pasem a pevné švy, protože při hře kraťasy zažijí víc než u dospělého. Lehká tkanina s elastanem dovolí volný pohyb při honičkách a školní tělesné výchově. Doplňte je odpovídajícími ponožkami a dresy z kategorie <a href="/dresy/">dresy</a>, pokud dítě hraje za tým.</p>'
          '<h2>Jak sestavit kompletní outfit</h2>'
          '<p>Kraťasy samy o sobě netvoří výbavu. Na chladnější dny je kombinujte s dlouhým rukávem nebo mikinou, v horku s tílkem z prodyšné syntetiky. Pro běh se hodí lehké ponožky bez švu, pro posilovnu pevnější, pro kolo vyšší. Ponožky, trička i kraťasy volte ze stejné rodiny materiálů, aby odváděly pot stejně rychle. Když kombinujete bavlněné tričko se syntetickými kraťasy, zvlhne jen horní část a tělo se může prochladit.</p>'
          '<h3>Na co se dívat při zkoušení</h3>'
          '<ul><li>V dřepu a výpadu nesjíždí pas a látka není průhledná.</li>'
          '<li>Švy nedrhnou na vnitřní straně stehen.</li>'
          '<li>Kapsa udrží telefon při poskoku a nevytahuje kraťasy dolů.</li>'
          '<li>Délka neomezuje krok ani nepřekáží při sedání na kolo.</li>'
          '<li>Gumový pas neotlačuje pokožku po půl hodině.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V katalogu jsou zastoupeny značky ' + B(('adidas', 'Adidas'), ('nike', 'Nike'), ('puma', 'Puma'), ('under-armour', 'Under Armour'), ('lotto', 'Lotto'), ('4f', '4F'), ('regatta', 'Regatta'), ('dynafit', 'Dynafit'), ('haglofs', 'Haglöfs'), ('gymbeam', 'GymBeam')) + '. Velké sportovní značky nabízejí široký výběr pro týmové sporty a fitness, outdoorové značky se zaměřují na odolnost a malou hmotnost pro hory. Nejlepší značka neexistuje, záleží na vašem střihu a použití.</p>'
          '<h2>Péče o sportovní kraťasy</h2>'
          '<p>Po tréninku je nenechávejte v taškce. Pot a vlhko podporují pach a oslabují vlákna. Perte je na doporučené teplotě, obvykle třicet až čtyřicet stupňů, s malým množstvím jemného pracího prostředku a bez aviváže, která ucpává póry v syntetice a snižuje odvod vlhkosti. Pokud mají reflexní potisk, perte je naruby. Sušte volně na vzduchu, ne na radiátoru ani v sušičce na vysokou teplotu, protože elastan ztrácí pružnost.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Bavlna na výkonový trénink:</strong> po zpocení je těžká a studí.</li>'
          '<li><strong>Příliš těsný pas:</strong> tlačí a sjíždí při pohybu.</li>'
          '<li><strong>Jeden pár na všechno:</strong> basketbalové, běžecké a cyklistické kraťasy mají jinou konstrukci.</li>'
          '<li><strong>Zapomenutá vnitřní vrstva:</strong> volné kraťasy bez spodního prádla odírají.</li>'
          '<li><strong>Aviváž při praní:</strong> funkční materiál přestane odvádět pot.</li></ul>'
          '<p>Až si vyberete, porovnejte nabídky v kategoriích <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/sportovni-sukne-a-saty/">sportovní sukně a šaty</a> a zkuste kombinovat. Někdy se hodí delší verze, jindy sukně s vnitřními šortkami. Barvu vybírejte až nakonec: tmavé skryjí pot a skvrny, světlé jsou v létě chladnější a lépe viditelné ve tmě.</p>',
    faq=[('Jaké kraťasy zvolit na běh?', 'Lehké z polyesteru s elastanem, s vnitřními slipy nebo bez, podle toho, co vám vyhovuje. Důležité jsou ploché švy, držící pas a kapsa na klíče. Pro dlouhé tratě vyzkoušejte, zda neodírají.'),
         ('Mají mít kraťasy vnitřní slipy?', 'Pro běh, fotbal a delší pohyb jsou praktické, protože drží tělo a nahrazují spodní prádlo. Do posilovny se často volí jednovrstvé s vlastním funkčním prádlem. Záleží na tom, co vám pohodlněji sedí.'),
         ('Jak dlouhé kraťasy zvolit?', 'Na běh krátké, na univerzální sport po střed stehna až kolena, na basketbal a streetový styl delší. Turistické bývají o něco delší, aby chránily před oděrem a větvemi.'),
         ('Z jakého materiálu jsou nejlepší sportovní kraťasy?', 'Z polyesteru s příměsí elastanu, protože schne a odvádí pot. Nylon je odolnější, bavlna se hodí spíš na volný čas. Rozhodují i prodyšné vsadky a kvalita švů.'),
         ('Jak vybrat správnou velikost?', 'Změřte obvod pasu a boků a porovnejte s tabulkou konkrétní značky. Pas by měl držet bez tlaku a při dřepu nebo výpadu nesjíždět. U e-shopu zjistěte, jak funguje vrácení zboží.'),
         ('Čím se liší běžecké a fitness kraťasy?', 'Běžecké jsou lehčí a prodyšnější, často s vnitřními slipy a kapsou. Fitness kraťasy jsou pevnější a pružnější, aby se při dřepu nedeformovaly a nebyly průhledné.'),
         ('Hodí se kompresní kraťasy na každodenní sport?', 'Pro mnoho lidí ano, hlavně pod volné kraťasy nebo samostatně při běhu a fitness. Dávají pocit opory svalů, ale nezabrání zranění. Nepřehánějte velikost, aby nebránily oběhu.'),
         ('Jak prát sportovní kraťasy?', 'Při teplotě do čtyřiceti stupňů, bez aviváže, naruby u potisků a bez sušičky při vysoké teplotě. Aviváž ucpává vlákna a zhoršuje odvod potu, teplo naopak poškozuje elastan.'),
         ('Na co si dát pozor u kraťasů na kolo?', 'Hlavně na vložku a na střih. Silniční model přiléhá a drží vložku na místě, MTB model je volnější a pevnější. Bez dobré vložky se dlouhé trasy špatně snášejí.'),
         ('Jak odstranit pach ze sportovního oblečení?', 'Perte hned po tréninku, ne až za několik dní. Pokud pach přetrvává, namočte kraťasy do vody s trochou octa, poté vyperte. Nenechávejte je vlhké v taškce, protože pach se tím jen zhorší.')]
)

# ------------------------------------------------------------------ lyzarske-obleceni
NEW['lyzarske-obleceni'] = dict(long=True,
    title='Lyžařské a snowboardové oblečení | Sporteka',
    desc='Lyžařské a snowboardové oblečení: bundy, kalhoty, kombinézy, rukavice, ponožky a termoprádlo. Jak se obléknout do mrazu a vlhka. Porovnání nabídek.',
    intro='<p><strong>Lyžařské a snowboardové oblečení</strong> má na svahu tři úkoly: udržet teplo, nepustit dovnitř vodu a odvést pot. Obvykle se to neřeší jedním kouskem, ale systémem vrstev. Spodní vrstva z <a href="/lyzarske-termopradlo/">termoprádla</a> odvádí vlhkost, střední zahřívá a svrchní <a href="/lyzarske-bundy/">bunda</a> s <a href="/lyzarske-kalhoty/">kalhotami</a> chrání před větrem, sněhem a vlhkem. Dobře poskládaná sada udrží komfort od rána na prvním výtahu až po poslední sjezd.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů od <a href="/lyzarske-kombinezy/">kombinéz</a> přes <a href="/lyzarske-rukavice/">rukavice</a> až po <a href="/lyzarske-ponozky/">ponožky</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice s nákrčníky</a>. Průvodce vysvětluje, jak vybírat podle sportu, počasí a velikosti, na co se u membrán a izolací dívat a jak o oblečení pečovat, aby vydrželo víc než jednu sezónu.</p>',
    guide='<h2>Systém tří vrstev na svahu</h2>'
          '<p>Nejčastější chyba na sjezdovce není špatná bunda, ale špatná kombinace pod ní. Pokud se člověk potí v bavlněném tričku, vlhkost zůstane na kůži a při první jízdě výtahem ho začne mrazit. Proto platí princip tří vrstev: každá vrstva dělá jinou práci a žádná nenahradí druhou.</p>'
          + T(['Vrstva', 'Úkol', 'Typický materiál', 'Kde hledat'], [
              ['Spodní', 'odvádí pot od kůže', 'syntetika nebo merino', '<a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a>'],
              ['Střední', 'zadržuje teplo', 'fleece, lehká izolace', '<a href="/fleecove-mikiny/">fleecové mikiny</a>'],
              ['Svrchní', 'chrání před větrem, sněhem a vodou', 'membrána, pevná tkanina', '<a href="/lyzarske-bundy/">bundy</a>, <a href="/lyzarske-kalhoty/">kalhoty</a>'],
              ['Příslušenství', 'chrání ruce, hlavu a krk', 'zateplené a vodoodpudivé díly', '<a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice</a>']]) +
          '<p>V jarním slunci na ledovci se pak počet vrstev liší od mrazivého dne v nížině. Vyplatí se vrstvit tak, aby šla jedna z nich v batohu nebo kapse sundat, nikoli nosit stejně teplé oblečení za všech podmínek.</p>'
          '<h2>Lyžařská a snowboardová bunda</h2>'
          '<p>U bundy sledujte tři parametry: vodotěsnost, prodyšnost a zateplení. Vodotěsnost se uvádí hodnotou vodního sloupce, prodyšnost množstvím vodní páry, které látka propustí. Čím vyšší hodnoty, tím lépe v extrémních podmínkách, ale také větší nároky na kvalitu zpracování. Pro rekreační lyžování ve středoevropských horách stačí střední kategorie, na freeride a snowboarding v mokrém sněhu se vyplatí výkonnější membrána. Důležité jsou i těsněné švy, protože právě jimi se voda dostane dovnitř nejdřív.</p>'
          '<ul><li><strong>Kapuce:</strong> musí jít přetáhnout přes helmu, jinak nechrání.</li>'
          '<li><strong>Sněhová sukně:</strong> nedovolí sněhu vnikat při pádu.</li>'
          '<li><strong>Větrací zipy:</strong> pod rukama umožňují regulovat teplo při výstupu.</li>'
          '<li><strong>Kapsa na skipas:</strong> na rukávu, aby šla otevřít bez svlékání.</li>'
          '<li><strong>Manžety:</strong> utěsní rukavice a zabrání průvanu.</li></ul>'
          '<h3>Zateplená, nebo skořepinová bunda</h3>'
          '<p>Zateplená bunda je jednodušší na jeden kus, ale v teplém dni se v ní snadno přehřejete. Skořepinová (shell) nemá izolaci, a proto ji můžete kombinovat s fleecem nebo péřovou vestou podle počasí. Skialpinisté a freeridisté ji volí častěji, rekreační lyžaři pro svou jednoduchost raději zateplený kus. Přehled najdete v <a href="/lyzarske-bundy/">lyžařských a snowboardových bundách</a>.</p>'
          '<h2>Kalhoty, kombinézy a overaly</h2>'
          '<p>Lyžařské kalhoty mají mít zesílenou spodní část nohavic, protože o hrany lyží a bot se rychle ošoupají. Důležité je zpevnění uvnitř kolem kotníku, gumový nebo silikonový lem proti vyjíždění nad boty a sněhové manžety. Kalhoty s laclem chrání záda lépe než ty bez něj, ale hůře se řeší cesta na toaletu. Větrací zipy na stehnech pomohou při intenzivním pohybu. Výběr je v kategorii <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>.</p>'
          '<p>Kombinéza je teplá a bez škvír, hodí se hlavně pro děti a pro lyžaře, kteří mrznou. Nevýhodou je složitější převlékání. Tuto skupinu najdete v kategorii <a href="/lyzarske-kombinezy/">kombinézy a overaly</a>. U dětí se vyplatí kupovat raději těsnější velikost s možností prodloužení nohavic, aby nešla látka při pádu pod boty.</p>'
          '<h2>Rukavice, palčáky, čepice a nákrčníky</h2>'
          '<p>Ruce mrznou první, a proto si u rukavic nešetřete pozorností. Palčáky jsou teplejší, protože prsty se navzájem zahřívají, prstové rukavice dávají větší cit. Delší manžeta přes rukáv bundy zamezí vnikání sněhu. Dlaň by měla být z odolného materiálu s protiskluzem a vnitřek z měkké izolace. Na jaře stačí tenčí kousek, v mrazu se vyplatí vložka nebo vyhřívání. Prohlédněte si <a href="/lyzarske-rukavice/">lyžařské rukavice a palčáky</a>.</p>'
          '<p>Pod helmu patří tenká čepice nebo čelenka, která nesmí vytvářet tlak. Nákrčník chrání krk a spodní část obličeje před větrem a studí. Pro lyžaře je pohodlný, protože nehrozí, že se zachytí. Nabídka je v kategorii <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a> a širší výběr v <a href="/nakrcniky-a-satky/">nákrčnících a kuklách</a>.</p>'
          '<h2>Ponožky a termoprádlo</h2>'
          '<p>Lyžařské ponožky jsou dlouhé, vyztužené na holeni a chodidle a nesmí mít silné švy. Nenoste dvojí ponožky, protože se v botě sbalí a způsobují puchýře. Merino hřeje i po zvlhnutí a málo zapáchá, syntetika rychleji schne. Vyberete je v <a href="/lyzarske-ponozky/">lyžařských ponožkách</a> nebo <a href="/merino-ponozky/">merino ponožkách</a>.</p>'
          '<p>Termoprádlo má přiléhat k tělu, jinak neodvádí pot. Tenké se hodí na jaro a sluneční dny, silnější na mráz. Nejprve vyzkoušejte, zda nedrhne švy při předklonu, protože na svahu se v tom strávíte celý den. Základní přehled je v kategorii <a href="/lyzarske-termopradlo/">lyžařské termoprádlo</a> a obecná nabídka v <a href="/termopradlo/">funkčním a termo prádle</a>.</p>'
          '<h2>Lyže, snowboard a oblečení</h2>'
          '<p>Rozdíl mezi lyžařským a snowboardovým stylem se projeví hlavně na kalhotách. Snowboardisté sedí a padají na zadek častěji, takže potřebují zesílený sed a volnější střih, lyžaři zase ocení užší kalhoty bez překážek při pohybu. Bundy se překrývají, ale snowboardový střih bývá delší. Nezapomeňte na výbavu, která s oblečením souvisí: <a href="/lyzarske-helmy/">helmu</a>, <a href="/lyzarske-bryle/">brýle</a> a <a href="/lyzarske-boty/">boty</a>. V kategorii <a href="/snowboarding/">snowboarding</a> najdete vázání, boty a desky. Chrániče najdete v kategorii <a href="/snowboardove-chranice/">chrániče páteře a boků</a>.</p>'
          '<h3>Skialpinismus, běžky a výlety</h3>'
          '<p>Při výstupu se člověk potí mnohem víc než při sjezdu, proto je na skialpech důležitá prodyšnost a možnost rychle regulovat teplo. Používejte lehčí vrstvy a na sjezd nasaďte teplejší. U běžeckého lyžování stačí tenčí a pružnější oblečení, více najdete v kategorii <a href="/bezecke-lyzovani/">běžecké lyžování</a>. Ve všech případech platí totéž: mokrá spodní vrstva je největší nepřítel. Souvisí i kategorie <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<h2>Oblečení podle typu lyžaře</h2>'
          '<p>Začátečník stráví hodně času sezením na sněhu, stáním ve frontě a vstáváním po pádech. Potřebuje proto odolnější sed a kolena, teplejší rukavice a spíš zateplenou bundu. Pokročilý sjezdař se pohybuje rychleji, vítr ho chladí víc a ocení přiléhavější střih a lepší prodyšnost. Freerider a skialpinista počítají s proměnlivým počasím, proto sázejí na skořepinu, kterou kombinují s vrstvami.</p>'
          '<p>Rodiny s dětmi by měly myslet na to, že dítě se zahřeje rychleji než dospělý, ale po pauze se také rychle ochladí. Nechte dítě mít po ruce náhradní rukavice a ponožky, protože mokré se na svahu vyměňují nejrychleji. Dospělí, kteří lyžují jen několik dní v roce, nemusí pořizovat nejvýkonnější membránu. Rozumně zvolený střední segment s kvalitním zpracováním stačí a po sezóně se dá využít i na zimní procházky.</p>'
          '<h3>Jak se obléknout podle počasí</h3>'
          + T(['Podmínky', 'Doporučená skladba'], [
              ['Sluneční jarní den kolem nuly', 'tenké termoprádlo, lehká skořepinová bunda, tenčí rukavice'],
              ['Běžný zimní den s mírným mrazem', 'středně silné termoprádlo, fleece, bunda s izolací, prstové rukavice'],
              ['Silný mráz a vítr', 'silnější termoprádlo, teplejší střední vrstva, kalhoty s laclem, palčáky, nákrčník'],
              ['Mokrý sníh a déšť', 'membránová bunda a kalhoty s těsněnými švy, rychleschnoucí spodní vrstva']]) +
          '<h2>Velikost, střih a barva</h2>'
          '<p>Zimní oblečení má sedět tak, aby pod něj šlo vrstvit, ale nemělo se ve větru zbytečně plácat. Zkuste předpažit, sednout do dřepu a otočit trup, což odhalí krátké rukávy nebo sevřený sed. U dětí se vyplatí hlídat, aby manžety zakryly rukavice a nohavice zůstaly přes boty. Světlé a výrazné barvy jsou viditelnější při mlze a pádech, takže pomáhají i bezpečnosti.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Z katalogu stojí za zmínku značky ' + B(('rossignol', 'Rossignol'), ('helly-hansen', 'Helly Hansen'), ('dare2b', 'Dare2b'), ('viking', 'Viking'), ('kilpi', 'Kilpi'), ('trespass', 'Trespass'), ('o-neill', "O'Neill"), ('protest', 'Protest'), ('loap', 'Loap'), ('ziener', 'Ziener'), ('picture', 'Picture')) + '. Některé se soustředí na výkonné sjezdové vybavení, jiné na snowboard nebo rodinné lyžování. Rozhodujte podle parametrů a střihu, ne jen podle jména.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Membránové oblečení perte speciálním prostředkem na funkční textil, ne s aviváží. Aviváž zalepuje póry a snižuje prodyšnost. Po několika sezónách pomůže obnovit impregnaci sprejem nebo prostředkem do pračky a krátké zahřátí v sušičce na nízký stupeň. Lyžařské rukavice sušte volně, ne na topení, protože se kůže a lepení poškodí. Na konci sezóny oblečení vyperte, vysušte a uložte volně, ne zmačkané v tašce.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li><strong>Bavlna pod bundou:</strong> pot zůstane na těle a tělo prochladne.</li>'
          '<li><strong>Dvě vrstvy ponožek:</strong> sbalí se a tlačí v botě.</li>'
          '<li><strong>Nevhodná velikost rukavic:</strong> příliš těsné zastavují krev, příliš volné ztrácejí cit.</li>'
          '<li><strong>Kapuce bez ohledu na helmu:</strong> na helmu nejde přetáhnout.</li>'
          '<li><strong>Praní s aviváží:</strong> membrána přestane dýchat.</li></ul>'
          '<p>Souhrn zimní nabídky najdete také v hlavní kategorii <a href="/zimni-sporty/">zimní sporty</a> a pro hrátky mimo svah v <a href="/zimni-obuv/">zimních botách a sněhulích</a>. Až si vyberete, porovnejte na Sportece obchody a zkontrolujte, zda je dostupná vaše velikost.</p>',
    faq=[('Kolik vrstev oblečení na lyže?', 'Obvykle tři: termoprádlo, střední zahřívací vrstva a svrchní bunda s kalhotami. V jarním slunci lze střední vrstvu vynechat, v mrazu ji zesílit. Důležité je, aby spodní vrstva neprosáknala potem.'),
         ('Jaká je nejdůležitější vlastnost lyžařské bundy?', 'Vodotěsnost a prodyšnost, které musí být vyvážené. Doplňte je kvalitní kapucí přes helmu, těsněnými švy a sněhovou sukní. Parametry konkrétního kousku najdete v popisu výrobce.'),
         ('Může lyžař nosit snowboardovou bundu?', 'Ano, funkčně jsou si podobné. Snowboardové střihy bývají volnější a delší, lyžařské přiléhavější. Důležité je, aby bunda nebránila pohybu a vytvořila dostatečnou ochranu před sněhem.'),
         ('Jak vybrat lyžařské rukavice?', 'Do mrazu palčáky, na aktivní lyžování prstové rukavice se zesílenou dlaní. Manžeta má jít přes rukáv bundy a vnitřní izolace nesmí tlačit. Pro děti zvolte rukavice, které půjdou snadno navléknout i s mokrými rukama.'),
         ('Proč nenosit bavlněné tričko pod lyžařskou bundu?', 'Bavlna nasákne potem a pomalu schne, takže tělo chladne. Termoprádlo ze syntetiky nebo merina odvádí vlhkost od kůže a udrží komfort i při pohybu.'),
         ('Kolik ponožek na lyžařské boty?', 'Jeden pár vhodných lyžařských ponožek. Dva páry se v botě sbalí, tlačí a způsobují otlaky. Ponožky mají být bez silných švů a bez záhybů.'),
         ('Hodí se kombinéza pro děti?', 'Ano, kombinéza chrání dítě před sněhem a nemá škvíry v pase. Na prodloužení životnosti se vyplatí mít možnost předělat délku nohavic. Pro starší děti často stačí bunda s kalhotami.'),
         ('Jak prát lyžařskou bundu?', 'Šetrně, na doporučené teplotě, s prostředkem na funkční textil a bez aviváže. Po vyprání vysušte a dle návodu obnovte impregnaci. Dodržujte štítek v oblečení.'),
         ('Čím se liší oblečení na skialpy od sjezdového?', 'Je lehčí a prodyšnější, protože výstup vyvolává velkou tvorbu potu. Důležité jsou větrací zipy a možnost sbalit bundu do batohu. Sjezdové je teplejší a odolnější proti oděru hran.'),
         ('Kdy se vyplatí kupovat lyžařské oblečení?', 'Podle potřeby kdykoli v sezóně, ale výběr velikostí bývá největší na jeho začátku. Porovnejte nabídky na Sportece a ověřte, zda je dostupná vaše velikost a jak lze zboží vrátit.')]
)

# ------------------------------------------------------------------ plavky
NEW['plavky'] = dict(long=True,
    title='Plavky: dámské, pánské, dětské na bazén i moře | Sporteka',
    desc='Plavky na bazén, moře i sport: dámské, pánské a dětské, jednodílné, dvoudílné, slipy a šortky. Porovnejte nabídku českých obchodů a značek.',
    intro='<p><strong>Plavky</strong> vybírejte podle toho, co v nich budete dělat. Na pravidelné plavání v bazénu potřebujete pevný materiál a přiléhavý střih, k moři spíš pohodlí a pěkný vzhled, na surf nebo vodní sporty zase pevné uchycení a rychlé schnutí. Stejný kus nemusí obstát ve všech situacích, a proto se vyplatí chvíli přemýšlet, kde budou plavky nejčastěji.</p>'
          '<p>Na Sportece najdete <a href="/damske-plavky/">dámské</a>, <a href="/panske-plavky/">pánské</a> i <a href="/detske-plavky/">dětské plavky</a> z českých obchodů a snadno porovnáte, kde je skladem vaše velikost. Níže najdete průvodce materiály, střihy, velikostmi a péčí, doplněný o tipy na doplňky jako <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">plavecké čepice</a>. Průvodce vás provede i častými chybami, které stojí peníze a otravují dovolenou.</p>',
    guide='<h2>Bazén, moře, nebo sport</h2>'
          '<p>Hlavní rozdíl mezi plavkami je v tom, jak snášejí vodu, v níž se pohybujete. Chlorovaná bazénová voda ničí elastická vlákna rychleji než sladká nebo mořská, proto pravidelní plavci hledají materiály výslovně označené jako odolné chlóru. Pro dovolenou stačí běžná plážová plavka, ale mořská sůl a slunce se také postarají o opotřebení.</p>'
          + T(['Využití', 'Vhodný typ plavek', 'Na co dbát'], [
              ['Pravidelné plavání', 'sportovní plavky z chlorovzdorných materiálů, přiléhavé střihy', 'odolnost materiálu, bezpečné ramínko, pevné švy'],
              ['Dovolená u moře', 'plážové plavky se vzory, jednodílné i dvoudílné, šortky', 'rychlé schnutí, UV odolnost barev, pohodlí'],
              ['Surf, paddleboard, vodní sporty', 'přiléhavé lycra trička a plavky s pevným uchycením', 'ochrana před sluncem a otěrem'],
              ['Závodní a triatlonové plavání', 'velmi přiléhavé hydrodynamické střihy', 'komfort při dlouhém použití'],
              ['Aquaaerobik a rehabilitace', 'pohodlné, pevné plavky s oporou', 'neprůhlednost při pohybu'],
              ['Děti', 'plavky s UV ochranou a snadným oblékáním', 'bezpečnost, pohodlí a jednoduchá velikost']]) +
          '<h2>Materiály a jejich vlastnosti</h2>'
          '<p>Většina plavek je ze syntetických vláken. Polyamid, často známý jako nylon, je měkký a příjemný na kůži, polyester odolává chlóru a slunci lépe a zachová si barvu. Elastan, na etiketě také jako lycra nebo spandex, zajišťuje pružnost, takže se plavky přizpůsobí tělu a po sundání se vrátí do tvaru. Podíl jednotlivých vláken najdete na štítku. Pro sport hledejte vyšší obsah polyesteru, pro pláž je pohodlnější mix polyamidu a elastanu.</p>'
          '<ul><li><strong>Podšívka:</strong> zajišťuje neprůhlednost, zejména u světlých barev.</li>'
          '<li><strong>Vyjímatelné vložky:</strong> ocení ty, kdo chtějí tvar bez pevných košíčků.</li>'
          '<li><strong>Zesílené švy:</strong> drží při plavání a nedrhnou o kůži.</li>'
          '<li><strong>UV ochrana:</strong> hodí se hlavně pro děti a při delším pobytu na slunci.</li>'
          '<li><strong>Rychlé schnutí:</strong> praktické na dovolené i při opakovaném koupání.</li></ul>'
          '<h2>Dámské plavky</h2>'
          '<p>Jednodílné plavky nejlépe drží při plavání, a proto se hodí do bazénu. Dvoudílné se hodí k opalování a rekreaci, ale pro delší plavání je vhodné zvolit horní díl s pevnějším uchycením. Při výběru sledujte typ ramínek, tvar výstřihu na zádech, podšívku a výšku kalhotek. Sportovní střih s křížením zad se nesesouvá a ramínka nepadají. Plážové kousky nabízejí vázání, volánky nebo vzory, ale často jsou méně pevné. Celý výběr najdete v kategorii <a href="/damske-plavky/">dámské plavky</a>.</p>'
          '<p>Při zkoušení vyzkoušejte předklon, otáčení trupu a zvednutí paží. Plavky mají přiléhat, ale nezařezávat se, a nikde nemají vytvářet záhyby. Jednodílné plavky mají různé délky trupu, takže vyšší osoby by měly zjistit, zda výrobce nabízí delší střih. Pokud nosíte větší košíček, ocení se pevné ramínko, širší podprsní pás a vyztužení.</p>'
          '<h2>Pánské plavky</h2>'
          '<p>Slipy jsou nejpřiléhavější a nejméně brzdí ve vodě, proto je nosí závodní plavci. Jammery sahají k polovině stehen, drží svaly a hodí se pro tréninky. Boxerky tvoří kompromis mezi komfortem a výkonem. Šortky jsou volné, rychle schnou a ocení je lidé u moře nebo na výlet, ale ve většině bazénů se nesmí nosit. Pravidla bazénu si ověřte předem. Nabídku shrnuje kategorie <a href="/panske-plavky/">pánské plavky</a>. K plavání na volné vodě se hodí i <a href="/sportovni-kratasy/">sportovní kraťasy</a>, pokud mají vnitřní podšívku a jsou určeny do vody.</p>'
          '<h2>Dětské plavky</h2>'
          '<p>U dětí rozhoduje bezpečnost a snadnost oblékání. Vybírejte plavky s měkkými švy, bez drsných štítků a s UV ochranou. Pro malé děti jsou praktické celotělové overaly nebo trička s dlouhým rukávem, protože pokožka na slunci snadno shoří. Pro plavecký výcvik pasují jednoduché sportovní střihy, které nepřekážejí. Děti rychle rostou, ale příliš velké plavky se při skoku do vody sesunou, takže hledejte nastavitelný pas nebo tkaničky. Nabízí je kategorie <a href="/detske-plavky/">dětské plavky</a>.</p>'
          '<h3>UV trička a lycra do vody</h3>'
          '<p>Přiléhavá trička s dlouhým rukávem chrání před sluncem i otěrem o prkno. Hodí se pro surfaře, paddleboardisty i děti na pláži. Na etiketě hledejte označení UV faktoru. Přehled najdete v kategorii <a href="/lycra-a-uv-tricka/">lycra a UV trička do vody</a>. I přes ochranu oblečení je rozumné používat na nezakrytou kůži opalovací krém.</p>'
          '<h2>Plavky podle postavy a stylu</h2>'
          '<p>Střih vybírejte podle toho, co budete v plavkách dělat. Vysoký pas u kalhotek sedí pevněji a zakrývá více, klasický brazilský střih nechává volnější pohyb nohou. Širší ramínka a pevný podprsní pás poskytnou větší oporu, jemná trojúhelníková ramínka se hodí na odpočinek u vody. Pro ty, kdo nechtějí odhalovat, existují jednodílné plavky s lemem nebo sukýnkou a tankiny, tedy dvoudílné s delším topem. Rozhodující je pocit pohodlí a jistoty, ne to, co je zrovna v módě.</p>'
          '<p>Pánské střihy se liší hlavně délkou nohavice. Čím kratší, tím menší odpor ve vodě. Pro pláž je pohodlnější delší, dlouhé šortky po kolena se hodí do surfu, ale ve vodě brzdí. Vzory a barvy volte podle účelu: tmavé plavky skryjí skvrny po opalovacím krému, světlé jsou na slunci chladnější. U barev neprůhlednost kontrolujte hlavně u světlých odstínů, které po zmoknutí mohou prosvítat.</p>'
          '<h2>Co si sbalit k vodě</h2>'
          '<p>Pro dovolenou se vyplatí dvoje plavky, aby jedny mohly schnout. Doplňte je lehkým oblečením na přezutí, osuškou, brýlemi a krémem s UV filtrem. Pro plavání v bazénu přidejte čepici, brýle a pytel na mokré věci. Děti potřebují náhradní plavky, protože se v mokrých prochladí. Pokud plánujete vodní sporty, vezměte lycra tričko a kraťasy se zadní kapsou na klíč. Elektroniku do vody nebrat a cennosti nechat v zavazadle.</p>'
          '<h3>Na co se zeptat před nákupem</h3>'
          '<ul><li>Pro jaké použití jsou plavky určeny: bazén, moře, nebo sport?</li>'
          '<li>Z jakých materiálů jsou vyrobeny a zda uvádějí odolnost proti chlóru?</li>'
          '<li>Jak sedí velikost podle tabulky a jaké jsou podmínky vrácení?</li>'
          '<li>Mají podšívku, vyjímatelné vložky a UV ochranu?</li>'
          '<li>Dají se kombinovat horní a spodní díl v různých velikostech?</li></ul>'
          '<h2>Velikost a střih</h2>'
          '<p>Plavky jsou oblečení, které se nevyplatí kupovat naslepo. Změřte hrudník, pas a boky a porovnejte hodnoty s tabulkou konkrétního výrobce. Velikost se mezi značkami liší a v mokrém stavu se látka lehce natáhne. Ideální plavky po nasazení jemně přiléhají, ale netlačí do kůže a nepouštějí kolem nohavic ani výstřihu. U e-shopů si zjistěte, zda lze plavky po vyzkoušení vrátit, protože z hygienických důvodů mívají specifické podmínky, například nutnost ponechat ochrannou fólii v rozkroku.</p>'
          '<h2>Doplňky k plavání</h2>'
          '<p>K plavání patří i drobnosti. <a href="/plavecke-bryle/">Plavecké brýle</a> chrání oči před chlórem a zlepšují přehled ve vodě, <a href="/plavecke-cepice/">plavecké čepice</a> drží vlasy a snižují odpor, a <a href="/plavecke-pomucky/">plavecké pomůcky</a> jako desky, bóje a ploutve pomáhají s technikou. Na pláž se hodí osuška a taška z <a href="/plazove-doplnky/">plážových doplňků</a>. Pro cestu domů mokré plavky zabalte do pytlíku a vyperte co nejdřív.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V katalogu jsou zastoupeny značky ' + B(('speedo', 'Speedo'), ('arena', 'Arena'), ('adidas', 'Adidas'), ('nike', 'Nike'), ('decathlon', 'Decathlon'), ('o-neill', "O'Neill"), ('roxy', 'Roxy'), ('4f', '4F'), ('protest', 'Protest')) + '. Některé jsou zaměřeny na plavecký sport, jiné na surf a plážový styl. Při výběru čtěte popis materiálu a parametry a nesuďte jen podle značky.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Po každém koupání opláchněte plavky sladkou vodou, aby chlór a sůl nepoškodily vlákna. Perte je ručně nebo v pračce na šetrný program při nízké teplotě, bez aviváže a bělicích prostředků. Nemačkejte je silně, jen vytlačte vodu a nechte je uschnout ve stínu, protože přímé slunce vypíná barvy a oslabuje elastan. Nesedejte v plavkách na drsné povrchy, které mohou látku poškodit.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li><strong>Plážová plavka na pravidelné plavání:</strong> chlór ji rychle zničí.</li>'
          '<li><strong>Příliš velká velikost:</strong> při skoku se sesune.</li>'
          '<li><strong>Dlouhé ponechání mokrých plavek v tašce:</strong> hrozí plíseň a zápach.</li>'
          '<li><strong>Prádlo pod plavkami:</strong> není hygienické ani pohodlné.</li>'
          '<li><strong>Zapomenutá UV ochrana u dětí:</strong> pokožka na slunci shoří rychleji, než se čeká.</li></ul>'
          '<p>Až si vyberete, porovnejte na Sportece nabídky obchodů a zkontrolujte dostupné velikosti. Při koupi na sezónu mějte po ruce dvoje plavky, abyste mohli jedny prát a druhé nosit.</p>',
    faq=[('Jaké plavky zvolit na pravidelné plavání?', 'Sportovní plavky z materiálu odolného chlóru, nejlépe s vyšším podílem polyesteru. Měly by přiléhat, mít pevné švy a při předklonu nesjíždět. Pro ženy vyhovuje jednodílný střih s pevnými ramínky, pro muže slipy, jammery nebo těsné boxerky.'),
         ('Je lepší jednodílný, nebo dvoudílný model?', 'Pro plavání je praktičtější jednodílný, protože drží a nesjíždí. Dvoudílné se hodí k opalování a na pláž, pokud nechcete mít bílé pruhy. Při vodních hrách vybírejte horní díl s pevným uchycením.'),
         ('Jak vybrat správnou velikost plavek?', 'Změřte hrudník, pas a boky a porovnejte s tabulkou výrobce. Plavky mají po nasazení přiléhat bez tlaku a nikde netvořit záhyby. Pokud váháte, vezměte spíš větší velikost, ale ne tak velkou, aby se při skoku sesunula.'),
         ('Mohu v bazénu nosit pánské šortky?', 'Řada bazénů je zakazuje z hygienických důvodů. Povolené jsou obvykle slipy, jammery nebo těsné boxerky. Pravidla zjistíte v provozním řádu konkrétního bazénu.'),
         ('Jak prát plavky?', 'Hned po koupání je opláchněte sladkou vodou, poté perte ručně nebo na šetrný program do 30 °C bez aviváže. Pak je nechte uschnout ve stínu. Tím chráníte elastan i barvu.'),
         ('Mají děti nosit UV plavky?', 'Je to rozumné, hlavně na slunné pláži. Oblečení s UV ochranou kryje větší plochu těla než klasické plavky. Odkrytou pokožku je nutné ošetřit krémem a vyhýbat se poledním hodinám.'),
         ('Proč plavky po čase ztrácejí tvar?', 'Elastická vlákna oslabují chlór, slunce, teplo a tření. Pomáhá oplachování, šetrné praní a střídání dvou párů. Plavky určené do bazénu vydrží déle, když je nenosíte při sezení na drsném povrchu.'),
         ('Jak často měnit plavky na plavání?', 'Neexistuje pevná doba. Měňte je, když látka řídne, vypíná se, prosvítá nebo přestane držet tvar. Při pravidelném plavání několikrát týdně to bývá dříve než u rekreačních plavek.'),
         ('Jak poznat plavky s dobrou UV ochranou?', 'Na štítku hledejte údaj o UV faktoru a složení materiálu. Hustěji pletená a tmavší látka propouští méně záření než řídká a světlá. Žádné oblečení nenahradí odpočinek ve stínu, krém na odkrytou kůži a přestávky mimo poledne.'),
         ('Co s mokrými plavkami po koupání?', 'Neukládejte je mokré do tašky. Vyždímejte je jemně v ručníku, zabalte do pytlíku a doma vyperte a rozvěste. Vlhko a teplo způsobují zápach a plíseň.')]
)
