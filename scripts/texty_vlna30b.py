"""sporteka.cz — wave 30b (17. 11. 2026): long texts for rucniky, domaci-pantofle, pingpongove-stoly, masazni-valce.
General true facts only, no prices, no product counts. Table tennis: only the playing-surface size and height (ITTF rule 2.1)
and the net height; no invented norms. Massage rollers: no health or medical promises, pain or injury → physiotherapist.
Brands linked only if present in src/texts/znacky.json (speedo, decathlon, crocs, insportline); others named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ rucniky
NEW['rucniky'] = dict(long=True,
    title='Ručníky a osušky: rychleschnoucí, chladicí i do sauny',
    desc='Rychleschnoucí ručníky z mikrovlákna, plážové osušky, chladicí ručníky a ručníky do sauny. Jak vybrat materiál a velikost a kde je koupit nejvýhodněji.',
    intro='<p>Ručník je věc, o které člověk přemýšlí až ve chvíli, kdy mu chybí. Do posilovny se hodí malý a savý, na plavání a do batohu lehký <strong>rychleschnoucí ručník</strong> z mikrovlákna, k vodě velká <strong>osuška</strong>, do které se dá zabalit celé tělo. Vedle nich tu najdete chladicí ručníky pro horké dny, ručníky a kilty do sauny i klubové a fanouškovské ručníky s logy týmů. Každý typ je stavěný na jinou situaci, a proto se vyplatí vědět, co od něj čekat. Jinak se ručník chová v batohu na horách, jinak na lehátku u moře a jinak v šatně posilovny, kde ho po tréninku hodíte do tašky ještě vlhký.</p>'
          '<p>Na Sportece vidíte pohromadě nabídky z různých českých e-shopů, a jakmile si vyberete, objednávku vyřídíte přímo u daného prodejce. V kategorii se objevují ručníky značek Nils Camp, Cocoon, Sea to Summit, ' + B(('speedo', 'Speedo'), ('decathlon', 'Decathlon')) + ' a dalších. Ručníky patří mezi <a href="/plazove-doplnky/">plážové doplňky</a>, další vybavení k vodě je v sekci <a href="/vodni-sporty/">vodní sporty</a>.</p>',
    guide='<h2>Jaké druhy ručníků tu najdete</h2>'
          '<p>Pod jedním slovem se skrývá několik dost odlišných výrobků. Klasický froté ručník z bavlny je měkký, příjemný na kůži a vody pobere hodně, jenže dlouho schne a v zabaleném batohu zabírá místo. Ručník z mikrovlákna je tenký, dá se smotat do malého pouzdra a za pár desítek minut na vzduchu je zase použitelný. Chladicí ručník slouží k něčemu úplně jinému než k utírání: namočí se, vyždímá a položí na krk. Saunová osuška je delší, aby se na ni na lavici dalo lehnout celým tělem.</p>'
          + T(['Druh', 'Materiál', 'Kdy se hodí'], [
              ['froté ručník a osuška', 'bavlněné smyčky, někdy s příměsí', 'doma, na chatě, k bazénu u domu'],
              ['rychleschnoucí ručník', 'mikrovlákno (polyester a polyamid)', 'plavání, cestování, turistika, posilovna'],
              ['plážová osuška', 'froté, velur nebo mikrovlákno', 'pláž, koupaliště, ležení na slunci'],
              ['chladicí ručník', 'speciální tkanina, která drží vodu', 'běh a trénink v horku, letní práce venku'],
              ['ručník a kilt do sauny', 'bavlna, len nebo vafle', 'sauna, wellness, relaxační místnost'],
              ['fitness ručník', 'malý froté nebo mikrovlákno', 'utírání potu na lavici a stroji']]) +
          '<h2>Mikrovlákno, nebo bavlna?</h2>'
          '<p>Mikrovlákno se skládá z velmi jemných syntetických vláken, obvykle ze směsi polyesteru a polyamidu. Voda se drží hlavně mezi vlákny a ne uvnitř nich, a proto se z ručníku po vyždímání rychle odpaří. Pro cestovatele je to hlavní důvod volby: mokrý ručník ráno v batohu nezapáchá tolik jako bavlněný a do večera bývá suchý. Nevýhodou je pocit na kůži. Hladké mikrovlákno se po těle spíš roluje a tlačí, než aby se otíralo. Varianty s jemným semišovým povrchem nebo s krátkými smyčkami tenhle pocit zmírňují.</p>'
          '<p>Bavlněné froté má smyčky, které vodu nasají dovnitř vláken. Utírá se s ním příjemně a rychle, ale stejná vlastnost ho činí těžkým a pomalu schnoucím. U froté se často uvádí plošná hmotnost v gramech na metr čtvereční. Vyšší číslo znamená hustší a těžší látku, která víc nasaje a déle vydrží, nižší naopak lehčí ručník, jenž dřív uschne. Pro domácí koupelnu se vybírá spíš těžší froté, do tašky na koupaliště klidně lehčí.</p>'
          '<h2>Velikosti: ručník, osuška, plážová osuška</h2>'
          '<p>Rozměry se mezi výrobci liší, ale ustálilo se několik běžných formátů. Malý ručník na ruce a obličej, střední ručník na tělo, osuška a velká plážová osuška. U rychleschnoucích ručníků se často prodávají řady ve velikostech S až XL, kde se rozměr uvádí přímo u modelu. Před nákupem se podívejte na skutečné centimetry, ne jen na písmenko, protože L jedné značky může odpovídat M jiné.</p>'
          + T(['Formát', 'Orientační rozměr', 'Typické použití'], [
              ['malý ručník', 'kolem 30 × 50 cm', 'ruce, obličej, pot v posilovně'],
              ['ručník', 'kolem 50 × 100 cm', 'tělo po sprše, sportovní taška'],
              ['osuška', 'kolem 70 × 140 cm', 'koupel, bazén, sauna'],
              ['plážová nebo saunová osuška', 'od 90 × 180 cm výš', 'ležení na pláži, lehátko, saunová lavice']]) +
          '<p>Na pláži a u bazénu ocení dospělý osušku, na které se dá ležet bez toho, aby nohy končily v písku. Do batohu na vícedenní túru naopak stačí menší ručník z mikrovlákna, který se v kombinaci s malým ručníkem na obličej postará o všechno.</p>'
          '<h2>Rychleschnoucí ručník na cesty a k vodě</h2>'
          '<p>Při výběru cestovního ručníku sledujte čtyři věci. Hmotnost a objem po sbalení, protože přesně kvůli nim jste mikrovlákno vybrali. Pouzdro, nejlépe síťované nebo prodyšné, ve kterém ručník dosychá i během cesty. Poutko nebo karabinu na zavěšení na batoh, stan či háček ve sprše. A povrch látky, který rozhoduje o tom, jak se ručník chová na kůži. Hladší mikrovlákno se méně zachytává o písek, a proto ho lidé rádi berou k moři, hrubší povrch zase lépe utírá.</p>'
          '<p>Plavci a triatlonisté často nosí do bazénu malý ručník z mikrovlákna, který po vyždímání znovu saje, takže vystačí na celou sprchu. K <a href="/plavky/">plavkám</a> a <a href="/plavecke-pomucky/">plaveckým pomůckám</a> tak přibude jen málo místa navíc.</p>'
          '<h2>Chladicí ručník: jak funguje</h2>'
          '<p>Chladicí ručník pracuje na principu odpařování. Látka nasaje vodu, po vyždímání ji drží v tenké vrstvě a jak se voda postupně vypařuje, ručník se ochladí. Nejlépe to funguje v suchém a teplém vzduchu s mírným větrem, ve vlhkém dusnu je efekt slabší. Po vyschnutí stačí ručník znovu namočit. Mnoho modelů má návod, že se má po vyždímání několikrát prudce mávnout ve vzduchu, aby se aktivoval. Nejde o kouzlo, mávnutím se jen urychlí první odpařování.</p>'
          '<p>Chladicí ručník je vhodný na krk při běhu v létě, na tribunu, na zahradu i do auta bez klimatizace. Nenahrazuje ale pití, stín a rozumné tempo. Když se v horku objeví závrať nebo nevolnost, je potřeba přestat a zchladit se pořádně.</p>'
          '<h2>Ručník a kilt do sauny</h2>'
          '<p>Ve veřejných saunách se na lavici sedí nebo leží na vlastním ručníku tak, aby se tělo dřeva nedotýkalo. Proto se do sauny nosí delší osuška, na kterou se vejdou i chodidla. K tomu se hodí ještě jeden menší ručník nebo saunový kilt, který se omotá kolem pasu a drží na suchý zip či knoflík. Vaflová látka a len jsou v sauně oblíbené, protože jsou lehké a rychle schnou. Mikrovlákno se v horké sauně používá méně, některým lidem na rozehřáté kůži není příjemné.</p>'
          '<h2>Klubové a fanouškovské ručníky</h2>'
          '<p>Část nabídky tvoří ručníky s logy fotbalových a hokejových klubů nebo týmů NBA. Většinou jde o froté nebo velur s tištěným či tkaným motivem. U potištěných osušek se vyplatí zkontrolovat, jestli je potisk jen na jedné straně, protože ta bývá méně savá. Fanouškovské ručníky jsou oblíbený dárek a často slouží spíš jako plážová osuška než jako koupelnový ručník.</p>'
          '<h2>Jak o ručník pečovat</h2>'
          '<ul><li><strong>Mikrovlákno bez aviváže:</strong> aviváž ucpává jemná vlákna a ručník pak hůř saje.</li>'
          '<li><strong>Odděleně od bavlny:</strong> mikrovlákno na sebe chytá chlupy a vlas z jiného prádla.</li>'
          '<li><strong>Teplota podle štítku:</strong> mikrovlákno nemá rádo vysoké teploty v pračce ani v sušičce.</li>'
          '<li><strong>Froté vyprat před prvním použitím:</strong> nový ručník pak lépe saje a uvolní se z něj volná vlákna.</li>'
          '<li><strong>Sušit rozložený:</strong> smotaný mokrý ručník v tašce rychle začne zapáchat.</li>'
          '<li><strong>Mořská voda a chlor:</strong> po návratu ručník propláchněte, sůl a chlor látce dlouhodobě nesvědčí.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Bavlněná osuška na vícedenní trek, kde pak váží a nestačí uschnout.</li>'
          '<li>Výběr podle písmenka velikosti bez kontroly centimetrů.</li>'
          '<li>Očekávání, že mikrovlákno bude na kůži stejně hebké jako froté.</li>'
          '<li>Krátká osuška do sauny, na které se na lavici nedá ležet.</li>'
          '<li>Chladicí ručník jako náhrada pití při běhu v horku.</li></ul>'
          '<h2>Ručník do posilovny</h2>'
          '<p>V mnoha posilovnách je ručník na lavici a podložku povinný, protože pot na čalounění nikdo po druhém nechce. Stačí menší formát, který se přehodí přes lavici nebo přes rameno a nepřekáží mezi sériemi. Hodí se froté, které dobře saje pot z obličeje, i mikrovlákno, které po tréninku v tašce rychle uschne. Některé fitness ručníky mají na konci kapsu, kterou se nasunou na opěradlo lavice, takže při cvičení nesklouznou. Do tašky se vyplatí přibalit ještě druhý ručník na sprchu, aby ten zpocený nemusel sloužit dvakrát.</p>'
          '<h2>Ručník pro děti a na tábor</h2>'
          '<p>Na tábor, do školy v přírodě nebo na plavecký výcvik se dětem hodí osuška s kapucí nebo pončo, do kterého se po koupání rychle zabalí. Na víkendové výlety je praktičtější lehký ručník z mikrovlákna, který se do batohu vejde i s pyžamem. Ručník podepište nebo vyberte výraznou barvu či vzor, aby si ho dítě mezi ostatními snadno našlo. Doma pak stačí ručník vyprat a usušit rozložený, ne smotaný v igelitce.</p>'
          '<h2>Související kategorie</h2>'
          '<p>K ručníku se na koupaliště hodí <a href="/lycra-a-uv-tricka/">lycra a UV trička</a> a na pláž <a href="/pop-up-a-plazove-stany/">pop-up a plážové stany</a> nebo <a href="/piknikove-deky/">piknikové deky</a>. Hygienické potřeby na cesty najdete v kategorii <a href="/hygiena-a-repelenty/">hygiena a repelenty</a>, drobnosti do batohu mezi <a href="/outdoor-doplnky/">outdoorovými doplňky</a>. Ručník pak můžete sbalit do některé z <a href="/sportovni-tasky/">sportovních tašek</a> nebo <a href="/cestovni-tasky/">cestovních tašek</a>.</p>',
    faq=[
        ('Který ručník schne nejrychleji?', 'Nejrychleji schnou ručníky z mikrovlákna, protože voda zůstává hlavně mezi vlákny. Po vyždímání a pověšení na vzduch bývají suché mnohem dřív než bavlněné froté.'),
        ('Je ručník z mikrovlákna stejně savý jako bavlněný?', 'Vody pobere hodně, ale utírá se jinak. Lépe funguje přitisknout ho na kůži a vodu vysát, než jím rychle třít. Po vyždímání saje znovu.'),
        ('Jakou velikost osušky vybrat na pláž?', 'Pro dospělého, který chce na osušce ležet, se hodí formát kolem 90 × 180 cm a větší. Menší osuška stačí na utření po koupání.'),
        ('Jak dlouho chladí chladicí ručník?', 'Záleží na teplotě, vlhkosti a větru. Chladí, dokud se z něj odpařuje voda, pak stačí ho znovu namočit a vyždímat.'),
        ('Proč mikrovlákno nesmí do aviváže?', 'Aviváž obalí jemná vlákna tenkou vrstvou a ručník pak hůř nasává vodu. Perte ho jen s pracím prostředkem.'),
        ('Jaký ručník si vzít do sauny?', 'Delší osušku, na kterou si na lavici lehnete celí, a k ní menší ručník nebo kilt na cestu mezi saunou a ochlazovnou.'),
        ('Co je saunový kilt?', 'Ručník upravený do tvaru zavinovací sukně, který drží na suchý zip nebo knoflík. Nosí ho muži i ženy kolem pasu nebo pod pažemi.'),
        ('Proč ručník po koupališti zapáchá?', 'Většinou proto, že zůstal mokrý smotaný v tašce. Po návratu ho rozložte, propláchněte od chloru nebo soli a nechte uschnout.'),
        ('Kde ručník koupit nejvýhodněji?', 'Sporteka u každého ručníku seřadí nabídky českých obchodů. Nakoupíte pak přímo v obchodě, který vám nejvíc vyhovuje.'),
    ])

# ------------------------------------------------------------------ domaci-pantofle
NEW['domaci-pantofle'] = dict(long=True,
    title='Papuče a domácí pantofle pro děti, dámy i pány',
    desc='Papuče na doma, dětské papuče do školky a do školy, pánské bačkory i barefoot papuče. Jak vybrat velikost, podrážku a materiál a porovnat nabídky obchodů.',
    intro='<p><strong>Papuče</strong> nosíme doma víc hodin denně než leckteré venkovní boty, a přesto se kupují často narychlo. Pohodlné domácí pantofle drží nohy v teple, chrání je před studenou dlažbou a na schodech neklouzají. Děti potřebují <strong>papuče do školky a do školy</strong>, které se snadno obují, drží na noze a nevadí jim celodenní běhání po třídě. Dospělí volí mezi otevřenými pantoflemi, zavřenými bačkorami, plstěnými nebo kožešinovými modely a barefoot papučemi s tenkou ohebnou podrážkou. Rozhoduje hlavně pata, podrážka a materiál podšívky, protože právě ty určují, jestli budete v papučích chodit rádi celou zimu, nebo skončí po pár týdnech v botníku.</p>'
          '<p>Sporteka shromažďuje nabídky papučí z českých e-shopů, takže nemusíte procházet obchod po obchodu. Až najdete tu pravou, koupíte ji u prodejce, kterého si sami zvolíte. V kategorii jsou papuče značek Ugg, Froddo, Befado, Pegres, ' + B(('crocs', 'Crocs')) + ' a také fanouškovské bačkory s logy klubů NHL. Patří do skupiny <a href="/pantofle-a-zabky/">pantofle a žabky</a>, tenké a ohebné boty na celý den najdete mezi <a href="/barefoot-obuv/">barefoot obuví</a>.</p>',
    guide='<h2>Druhy papučí a pantoflí</h2>'
          '<p>Domácí obuv se liší hlavně tím, kolik nohy zakryje. Pantofle bez paty se obují jedním pohybem a v létě se v nich nohy tolik nepotí. Zavřené papuče s patou drží na noze pevněji a jsou bezpečnější na schodech i pro starší lidi. Bačkory s vyšším zateplením nebo kožešinou slouží hlavně do chladných domů a na chatu. Dětské přezůvky mají obvykle patu a zapínání na suchý zip, aby se samy nezouvaly.</p>'
          + T(['Typ', 'Jak vypadá', 'Pro koho a kam'], [
              ['otevřené pantofle', 'bez paty, nártový pásek nebo uzavřená špička', 'rychlé obouvání, teplejší byty'],
              ['zavřené papuče', 's patou, často s pružným lemem nebo zapínáním', 'celodenní nošení, schody, senioři'],
              ['zateplené bačkory', 'podšívka z fleecu, plsti nebo kožešiny, vyšší kotník', 'chladné podlahy, chalupa, zima'],
              ['dětské přezůvky', 'pata, suchý zip, protiskluzová podrážka', 'školka, škola, kroužky'],
              ['barefoot papuče', 'tenká ohebná podrážka, široká špička', 'kdo chce i doma chodit co nejpřirozeněji'],
              ['pantofle typu clog', 'pěnový nebo gumový nártník, někdy s vložkou', 'dům, zahrada, terasa']]) +
          '<h2>Dětské papuče do školky a do školy</h2>'
          '<p>Papuče pro školku nosí dítě celý den a obouvá si je samo. Proto by měly mít pevnou patu, zapínání na suchý zip nebo pružný lem a dost místa ve špičce. Pantofle bez paty do školky většinou nejsou vhodné, protože při běhání padají a dítě v nich snadno zakopne. Mnoho školek také uvádí, jaké přezůvky si přejí, takže se vyplatí zeptat učitelky předem.</p>'
          '<p>Při výběru velikosti nechte v papučích místo navíc v délce, protože dětská noha během školního roku roste. Příliš velké papuče ale nohu nedrží a dítě v nich šoupe. Nejjistější je obkreslit chodidlo na papír, změřit nejdelší místo a porovnat s tabulkou výrobce, kde je uvedena vnitřní délka. Podrážka by měla být protiskluzová, protože podlahy ve školách bývají hladké a často se myjí. Pokud jde papuče vyprat v pračce, ocení to každý rodič, který je na konci týdne přinese domů.</p>'
          '<p>Na papuče i ostatní věci ve školce se obvykle podepisuje jméno nebo značka dítěte. Popisovač na textil nebo nažehlovací štítek uvnitř papuče ušetří spoustu ztracených párů.</p>'
          '<h2>Barefoot papuče</h2>'
          '<p>Barefoot papuče mají tenkou, ohebnou podrážku bez zvýšené paty a širší špičku, ve které mají prsty volnost. Vyrábějí se pro děti i dospělé, třeba u českého výrobce Pegres nebo chorvatské značky Froddo. Kdo doma chodí bos nebo v ponožkách a chce jen ochranu před chladem a uklouznutím, najde v nich přirozený kompromis. U barefoot papučí dvojnásob platí, že musí správně padnout: tenká podrážka nic neodpustí a příliš úzká špička prsty utlačuje.</p>'
          '<h2>Materiály svršku a podšívky</h2>'
          + T(['Materiál', 'Vlastnosti', 'Na co si dát pozor'], [
              ['plsť a vlna', 'hřeje, dýchá, příjemná na bosou nohu', 'po vyprání se může srazit'],
              ['ovčí kožešina', 'velmi teplá, odvádí vlhkost', 'vyžaduje šetrné čištění'],
              ['fleece a plyš', 'lehký, měkký, levnější výroba', 'v teplém bytě se v něm nohy potí'],
              ['bavlna a textil', 'prodyšné, často pratelné', 'rychleji se prošlapou'],
              ['useň', 'drží tvar a vydrží dlouho', 'nesmí do pračky'],
              ['EVA pěna a guma', 'omyvatelné, lehké, nevadí jim voda', 'na bosou nohu hůř dýchají']]) +
          '<p>Podšívka rozhoduje o pohodlí víc, než se na první pohled zdá. Kdo nosí papuče naboso, ocení vlnu, kožešinu nebo bavlnu, protože odvádějí vlhkost. S teplými <a href="/sportovni-ponozky/">ponožkami</a> nebo <a href="/merino-ponozky/">merino ponožkami</a> si naopak vystačíte i s tenčí a lehčí papučí.</p>'
          '<h2>Podrážka: protiskluz a tvrdost</h2>'
          '<p>Podrážka papuče má být protiskluzová, a to platí dvojnásob pro dlažbu, laminát a schody. Tvrdší gumová podrážka umožňuje vyběhnout na balkon nebo na zahradu pro poštu, měkká textilní nebo semišová je zase tichá a nepoškrábe podlahu. Ohněte papuči v ruce: měla by se ohýbat v místě, kde se ohýbá chodidlo, tedy v přední části, ne uprostřed. Senioři by měli vybírat papuče s patou a hrubším vzorkem, které na hladké podlaze drží lépe.</p>'
          '<h2>Pánské a dámské papuče</h2>'
          '<p>Pánské papuče se vyrábějí v širších kopytech a vyšších velikostech, u některých značek najdete i čísla nad 46. Dámské modely bývají užší a často mají měkčí podšívku nebo ozdobný svršek. Rozdíl je ale hlavně v šířce, takže žena se širší nohou může klidně sáhnout po pánském modelu v menší velikosti. Oblíbeným dárkem jsou fanouškovské bačkory s logem hokejového klubu, ty ke zbytku sbírky doplníte v kategorii <a href="/hokejove-suveniry-a-karty/">hokejové suvenýry a karty</a>.</p>'
          '<h2>Péče o papuče</h2>'
          '<ul><li><strong>Podle štítku:</strong> textilní a fleecové papuče často snesou pračku na nízkou teplotu, kožené ani plstěné obvykle ne.</li>'
          '<li><strong>Sušit volně:</strong> ne na topení, kde se podrážka může zdeformovat a lepené spoje povolit.</li>'
          '<li><strong>Větrat:</strong> papuče nošené naboso potřebují přes noc vyschnout, pomůže střídat dva páry.</li>'
          '<li><strong>Vyměnitelná stélka:</strong> u modelů s vyjímatelnou vložkou stačí vyprat nebo vyměnit jen ji.</li>'
          '<li><strong>Kontrola podrážky:</strong> ochozená hladká podrážka už neplní protiskluzovou funkci.</li></ul>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Pantofle bez paty do školky nebo pro člověka, který chodí po schodech.</li>'
          '<li>Dětské papuče o několik čísel větší „na příští rok“.</li>'
          '<li>Výběr podle čísla bez kontroly vnitřní délky v tabulce výrobce.</li>'
          '<li>Kožešinové bačkory do vytopeného bytu, kde se v nich nohy přehřívají.</li>'
          '<li>Ozdoby a bambulky na dětských přezůvkách, které se dají utrhnout.</li></ul>'
          '<h2>Jak má papuče sedět</h2>'
          '<p>Dobře padnoucí papuče drží na noze bez toho, abyste museli prsty zatínat. Pata nesmí při chůzi vyklouzávat a v přední části by prsty neměly narážet na špičku. Zkoušejte je odpoledne, kdy je noha po dni trochu oteklá, a v ponožkách, ve kterých je budete nosit. U plstěných a kožešinových modelů počítejte s tím, že se podšívka během prvních týdnů trochu slehne a papuče povolí. Naopak u textilních papučí, které se perou, může po prvním praní materiál mírně srazit. Pokud stojíte mezi dvěma velikostmi, podívejte se do recenzí nebo do popisu výrobce, jestli model vychází spíš menší, nebo větší.</p>'
          '<p>Kdo má širší nohu, vysoký nárt nebo vbočený palec, ocení papuče s nastavitelným zapínáním přes nárt. Suchý zip nebo pružný pásek umožní přizpůsobit obvod a papuče pak netlačí ani po několika hodinách.</p>'
          '<h2>Papuče pro celou rodinu a jako dárek</h2>'
          '<p>Papuče patří k nejčastějším dárkům pod stromeček a není se čemu divit. Hodí se každému věku, nejsou drahou investicí a v zimě je člověk opravdu nosí. Pro dárek se vyplatí znát přesnou velikost, nejlépe z oblíbených papučí obdarovaného, a vybrat model s patou, pokud nevíte, jaké pantofle má rád. Rodinné sady ve stejném vzoru pro rodiče i děti, papuče s motivem zvířat pro nejmenší nebo bačkory s logem oblíbeného týmu jsou varianty, které potěší i toho, kdo jinak o domácí obuv nedbá.</p>'
          '<h2>Papuče pro domácí kancelář</h2>'
          '<p>Kdo pracuje z domova, stráví v papučích celý pracovní den a pohodlí se pak projeví víc než při krátkém večeru na gauči. Hodí se zavřené papuče s lehce tvarovanou stélkou a prodyšnou podšívkou, ve kterých nohy nepřehřejete ani po osmi hodinách u stolu. Když si občas odskočíte do sklepa nebo k poštovní schránce, oceníte pevnější podrážku, která snese i krátkou cestu po chodníku.</p>'
          '<h2>Papuče na chatu a do chladných domů</h2>'
          '<p>Na chalupě, kde se topí jen v kamnech a podlaha bývá studená, se osvědčí bačkory s vyšším lemem a tlustou podrážkou, která od chladu izoluje. Vlněná plsť a ovčí kožešina hřejí i ve vlhčím prostředí a nohy v nich nezapáchají tak rychle jako v syntetice. Pokud z chaty často odbíháte na dřevo nebo na zahradu, hodí se model s pevnou gumovou podrážkou, kterou krátká cesta po trávě nepromočí.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Pro chození k bazénu a do sprchy jsou určené jiné pantofle a žabky z omyvatelných materiálů, na pláž a do vody pak <a href="/obuv-do-vody/">obuv do vody</a> a v létě <a href="/sandaly/">sandály</a>. Na zimu venku najdete <a href="/snehule/">sněhule</a> a <a href="/zimni-obuv/">zimní obuv</a>. Pokud potřebujete papuči nebo botě dodat pohodlí, podívejte se na <a href="/vlozky-do-bot/">vložky do bot</a>.</p>',
    faq=[
        ('Jaké papuče vybrat do školky?', 'Papuče s pevnou patou, zapínáním na suchý zip a protiskluzovou podrážkou. Dítě si je obuje samo a při běhání mu nespadnou. Ověřte si i požadavky konkrétní školky.'),
        ('O kolik větší mají být dětské papuče?', 'Délka papuče má o něco přesahovat chodidlo, aby měly prsty místo a noha mohla růst. Moc velké papuče ale dítě ztrácí a zakopává v nich.'),
        ('Jak změřit nohu na papuče?', 'Postavte se na papír, obkreslete chodidlo a změřte nejdelší místo. Číslo porovnejte s vnitřní délkou v tabulce výrobce.'),
        ('Jsou barefoot papuče vhodné pro děti?', 'Mnoho rodičů je volí, protože mají tenkou ohebnou podrážku a širokou špičku. Musí ale dobře sedět, a pokud má dítě s chůzí potíže, poraďte se s pediatrem nebo ortopedem.'),
        ('Lze papuče prát v pračce?', 'Textilní a fleecové často ano, na nízkou teplotu a v síťce. Kožené, plstěné a kožešinové obvykle ne. Řiďte se symboly na štítku.'),
        ('Které papuče jsou nejteplejší?', 'Bačkory s podšívkou z ovčí kožešiny nebo plsti a s vyšším lemem kolem kotníku. Hodí se do chladných domů a na chalupu.'),
        ('Jaké papuče pro seniory?', 'Zavřené papuče s patou, pevným zapínáním a protiskluzovou podrážkou se vzorkem. Pantofle bez paty na schodech zbytečně zvyšují riziko pádu.'),
        ('Proč papuče zapáchají?', 'Noha se potí i doma a vlhkost zůstává v podšívce. Pomůže střídat dva páry, nechat je vyschnout a prát nebo vyměnit stélku.'),
        ('Kde koupit papuče?', 'Na Sportece porovnáte nabídky papučí z několika českých obchodů najednou. Nákup a doručení zajistí obchod, u kterého objednáte.'),
    ])

# ------------------------------------------------------------------ pingpongove-stoly
NEW['pingpongove-stoly'] = dict(long=True,
    title='Pingpongové stoly venkovní i vnitřní, skládací',
    desc='Pingpongové stoly do herny, garáže i na zahradu: vnitřní a venkovní, skládací na kolečkách. Na co se dívat u desky, konstrukce a místa kolem stolu.',
    intro='<p><strong>Pingpongový stůl</strong> je investice, která vydrží roky, a proto se vyplatí vybírat podle toho, kde bude stát. Vnitřní stoly patří do herny, garáže nebo suterénu, kde na ně neprší a nesvítí přímo slunce. Venkovní stoly mají desku a rám odolné proti vlhkosti i UV záření a hodí se na zahradu, ke chatě nebo na školní hřiště. Většina modelů pro domácnost je skládací: obě poloviny se zvednou nahoru a stůl na kolečkách odvezete ke zdi. Před nákupem si ujasněte tři věci: kolik máte místa, jestli stůl bude stát v suchu a kdo na něm bude hrát. Podle toho pak vybíráte desku, rám i výbavu.</p>'
          '<p>Na Sportece porovnáte, za kolik a kde jednotlivé stoly prodávají české e-shopy, a samotnou objednávku pak dokončíte u vybraného obchodu. V nabídce se objevují stoly značek Sponeta, ' + B(('insportline', 'inSPORTline')) + ', Sedco, Cornilleau, Kettler, Butterfly nebo Stiga. Pálky, míčky a síťky najdete v nadřazené kategorii <a href="/stolni-tenis/">stolní tenis</a>.</p>',
    guide='<h2>Rozměry stolu podle pravidel</h2>'
          '<p>Pravidla stolního tenisu stanovují hrací plochu o délce 274 cm a šířce 152,5 cm, ve výšce 76 cm nad podlahou. Síťka je vysoká 15,25 cm. Většina stolů pro domácnost i pro kluby tyto rozměry dodržuje, takže na nich hrajete stejnou hru jako v oddíle. Vedle nich se prodávají menší stoly pro děti nebo do malých místností. Jsou levnější a vejdou se i do pokoje, ale dráha míčku se na nich chová jinak, a kdo chce hrát závodně, měl by trénovat na plném rozměru.</p>'
          + T(['Údaj', 'Hodnota u stolu plného rozměru'], [
              ['délka hrací plochy', '274 cm'],
              ['šířka hrací plochy', '152,5 cm'],
              ['výška hrací plochy nad podlahou', '76 cm'],
              ['výška síťky', '15,25 cm']]) +
          '<p>Rozměr ve složeném stavu najdete u každého modelu zvlášť. Rozhoduje o tom, jestli stůl projde dveřmi a vejde se mezi auto a zeď garáže.</p>'
          '<h2>Kolik místa kolem stolu potřebujete</h2>'
          '<p>Samotný stůl je jen část prostoru. Hráči stojí za koncem stolu a při výměnách couvají, uhýbají do stran a napřahují se pálkou. Pro rekreační hru počítejte aspoň s metrem až dvěma za každým koncem a s volným místem po stranách. Čím víc prostoru, tím přirozenější hra, v úzké garáži se hraje spíš blízko stolu a krátkými údery. Myslete také na strop, protože vysoký lob v nízké místnosti narazí do světla. Rovná podlaha je důležitá, protože kolečka a nastavitelné nohy dorovnají jen drobné nerovnosti.</p>'
          '<h2>Vnitřní, nebo venkovní stůl?</h2>'
          '<p>Rozdíl není jen v barvě. Vnitřní stůl má desku z dřevotřísky nebo dřevovláknité desky s lakovaným povrchem. Ten se příjemně hraje a míček od něj odskakuje rovnoměrně, ale vlhkost a déšť desku zvlní. Venkovní stůl používá materiály, kterým voda nevadí: melaminovou pryskyřici, kompozitní desky s hliníkovou vrstvou nebo beton. Rám je pozinkovaný či práškově lakovaný, aby nerezavěl, a síťka bývá pevná, kovová nebo z odolného materiálu.</p>'
          + T(['Vlastnost', 'Vnitřní stůl', 'Venkovní stůl'], [
              ['deska', 'dřevotříska nebo MDF s lakem', 'melamin, kompozit, hliník, beton'],
              ['odolnost vůči vlhkosti', 'nízká, déšť desku poškodí', 'vysoká, snese déšť i mráz'],
              ['odskok míčku', 'obvykle rovnoměrnější', 'může být o něco méně živý'],
              ['kam se hodí', 'herna, garáž, suterén, tělocvična', 'zahrada, terasa, hřiště, kemp'],
              ['údržba', 'utírat prach, chránit před sluncem', 'plachta nebo kryt, kontrola rámu']]) +
          '<p>Vnitřní stůl postavený pod pergolou nebo do nevytápěné stodoly je častá chyba. I bez přímého deště tam působí vlhko a velké rozdíly teplot. Pokud nemáte jistotu, že místo zůstane suché, vyberte venkovní provedení.</p>'
          '<h2>Deska a odskok míčku</h2>'
          '<p>U vnitřních stolů se uvádí tloušťka desky v milimetrech. Silnější deska je tužší, méně se pruží a míček od ní odskakuje stejně na kraji jako uprostřed. Tenčí desky najdete u stolů pro rekreační hru, silné desky kolem 25 mm u stolů určených pro trénink a soutěže. Odskok si můžete vyzkoušet jednoduše: pusťte míček ze stejné výšky na různá místa stolu a sledujte, jestli vyskočí pokaždé stejně. Na mrtvých místech, typicky u spoje obou polovin nebo nad příčkou rámu, odskočí znatelně méně.</p>'
          '<h2>Konstrukce, kolečka a skládání</h2>'
          '<ul><li><strong>Rám a nohy:</strong> profil nohou a příčky určují, jak stůl drží při opření a při úderech. Stabilní stůl se při hře nekymácí.</li>'
          '<li><strong>Kolečka:</strong> větší kolečka přejedou práh a trávník, brzdy na nich drží stůl na místě.</li>'
          '<li><strong>Pojistky skládání:</strong> zvednuté poloviny musí jistit spolehlivý zámek, aby se stůl samovolně nerozložil.</li>'
          '<li><strong>Nastavitelné nohy:</strong> vyrovnají nerovnou podlahu a stůl pak stojí vodorovně.</li>'
          '<li><strong>Poloha pro trénink:</strong> jednu polovinu lze zvednout svisle a hrát míček proti ní sám.</li>'
          '<li><strong>Držák na pálky a míčky:</strong> drobnost, která šetří hledání pod stolem.</li></ul>'
          '<p>Skládací stůl je těžký a při převrácení může zranit, zvlášť děti. Nedovolte dětem, aby se na zvednuté poloviny věšely nebo stůl samy skládaly, a když ho nepoužíváte, zajistěte všechny pojistky.</p>'
          '<h2>Montáž a umístění</h2>'
          '<p>Většina stolů přijíždí rozložená v jednom nebo dvou velkých kartonech a montáž zabere pár hodin. Počítejte s druhým člověkem, protože desky jsou rozměrné a těžké. Před montáží si ověřte, že máte dost místa na rozložení dílů a že balík projde až na místo, kde bude stůl stát. Venkovní stůl postavte na rovný a pevný povrch, třeba dlažbu nebo terasu. Na měkkém trávníku nohy postupně zapadají a deska se nakloní.</p>'
          '<h2>Údržba a ochrana</h2>'
          '<p>Vnitřní stůl stačí otírat suchou nebo mírně vlhkou utěrkou a chránit před přímým sluncem, které může povrch vybělit. Venkovní stůl ocení kryt nebo plachtu na zimu i pro období, kdy se nehraje. Listí a voda pak nezůstávají na desce. Jednou za sezonu zkontrolujte šrouby, pojistky skládání a kolečka. U betonových stolů je údržba nejmenší, zato je nepřestěhujete.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Vnitřní stůl na místo, kam se dostane vlhkost.</li>'
          '<li>Koupě bez změření místnosti včetně prostoru za koncem stolu.</li>'
          '<li>Přehlédnutí rozměrů ve složeném stavu.</li>'
          '<li>Montáž na nerovném trávníku bez pevného podkladu.</li>'
          '<li>Zapomenuté pálky a míčky, které nebývají součástí balení.</li></ul>'
          '<h2>Stůl pro rodinu, nebo pro trénink?</h2>'
          '<p>Rodina, která chce o víkendu hrát pro zábavu, nepotřebuje nejtužší desku na trhu. Důležitější je stabilita, snadné skládání, bezpečné pojistky a kolečka, se kterými stůl odjede z cesty. Pro hráče, kteří chodí do oddílu nebo se na soutěže teprve připravují, je naopak deska a odskok míčku na prvním místě. Na stole s měkkou deskou si zvyknou na jiný odskok a v herně pak míček chytají pozdě. Mezi těmito skupinami stojí stoly pro pokročilé rekreační hráče, kteří hrají pravidelně, ale bez ambic na soutěže.</p>'
          + T(['Kdo bude hrát', 'Na co se zaměřit', 'Čemu se nevyhnout'], [
              ['rodina s dětmi', 'pojistky skládání, kolečka s brzdou, stabilita', 'stůl bez zajištění zvednutých polovin'],
              ['rekreační hráč', 'pevnější deska, síťka s napínáním, nastavitelné nohy', 'nejtenčí desky, které se prohýbají'],
              ['hráč z oddílu', 'tuhá deska, rovnoměrný odskok, plný rozměr', 'zmenšené stoly a měkké desky'],
              ['hřiště, škola, kemp', 'venkovní nebo betonové provedení, pevná síťka', 'skládací vnitřní stůl']]) +
          '<h2>Síťka a příslušenství</h2>'
          '<p>Síťka bývá u většiny stolů přibalená, ale ne vždy. U vnitřních stolů se nejčastěji připíná šroubovými nebo pružinovými svorkami k okraji desky, u venkovních bývá pevná a kovová, aby vydržela počasí. Síťka by měla jít napnout, protože prověšená síť mění hru a míček se v ní zachytává. Ke stolu se hodí i kryt nebo plachta, a pokud chcete trénovat sami, také robot na podávání míčků, který postavíte na protější konec stolu. Míčků kupte raději víc, protože se rychle zakutálí pod nábytek nebo do trávy.</p>'
          '<h2>Osvětlení a podlaha v herně</h2>'
          '<p>Kdo hraje večer v garáži nebo v suterénu, ocení rovnoměrné světlo nad stolem bez ostrých stínů. Světla nemají svítit hráčům do očí a nemají viset tak nízko, aby do nich narazil vysoký míček. Podlaha by neměla klouzat, zvlášť pokud se při hře rychle přešlapuje do stran. Betonová podlaha v garáži je v pořádku, jen je vhodné zamést prach a písek, na kterém podrážky ujíždějí. Tmavší stěny za stolem pomáhají bílý nebo oranžový míček lépe sledovat.</p>'
          '<h2>Pravidla hry doma</h2>'
          '<p>Doma se nemusíte řídit všemi pravidly do písmene, ale pár základních se vyplatí znát, protože hru zrychlí a předejdou sporům. Hraje se na jedenáct bodů a set musí skončit rozdílem dvou bodů. Podání se střídá vždy po dvou výměnách a míček se při podání nadhazuje z otevřené dlaně. U čtyřhry se podává z pravé poloviny stolu úhlopříčně, a proto je na desce středová čára. Kdo si tato pravidla osvojí doma, nebude v oddíle nebo na turnaji překvapený.</p>'
          '<h2>Doprava a stěhování stolu</h2>'
          '<p>Pingpongový stůl patří mezi objemné zásilky a obchody ho obvykle posílají přes dopravce, který vozí nadrozměrné balíky. Před objednávkou si ověřte, jestli řidič balík vynese, nebo jen složí před dům, a zda projde dveřmi a chodbou. Smontovaný skládací stůl přesouvejte ve složeném stavu se zajištěnými pojistkami a ideálně ve dvou, přes schody nebo práh ho raději přeneste, než ho táhnout po kolečkách.</p>'
          '<h2>Související kategorie</h2>'
          '<p>Pálky, míčky a síťky jsou v kategorii <a href="/stolni-tenis/">stolní tenis</a>, celou nabídku míčových a raketových sportů najdete v sekci <a href="/micove-sporty/">míčové sporty</a>. Na zahradu se ke stolu hodí <a href="/hry-na-zahradu/">hry na zahradu</a>, <a href="/badminton/">badminton</a> nebo <a href="/trampoliny/">trampolíny</a>, do herny zase <a href="/sipkove-terce/">šipkové terče</a>.</p>',
    faq=[
        ('Jaký je rozměr pingpongového stolu?', 'Stůl plného rozměru má hrací plochu 274 × 152,5 cm a stojí ve výšce 76 cm. Síťka je vysoká 15,25 cm.'),
        ('Kolik místa potřebuji pro pingpongový stůl?', 'K samotnému stolu připočtěte pro rekreační hru aspoň metr až dva za každým koncem a volné místo po stranách. Čím víc prostoru, tím přirozenější výměny.'),
        ('Může vnitřní stůl stát venku?', 'Nemá. Deska z dřevotřísky nebo MDF se vlhkem zvlní a lak popraská. Pro zahradu, terasu i nevytápěnou stodolu vyberte venkovní provedení.'),
        ('Z čeho jsou venkovní pingpongové stoly?', 'Deska bývá z melaminové pryskyřice, kompozitu s hliníkem nebo z betonu, rám je pozinkovaný či práškově lakovaný. Takové materiály snesou déšť i mráz.'),
        ('Proč záleží na tloušťce desky?', 'Silnější deska je tužší a míček od ní odskakuje rovnoměrněji po celé ploše. Tenčí deska stačí na rekreační hru.'),
        ('Jak trénovat stolní tenis sám?', 'Mnoho skládacích stolů umí zvednout jednu polovinu svisle. Míček pak hrajete proti ní a ona ho vrací.'),
        ('Jsou pálky a míčky součástí stolu?', 'Většinou ne. Pokud je sada přibalená, je to uvedeno v popisu. Jinak je dokoupíte v kategorii stolní tenis.'),
        ('Jak skládací stůl bezpečně uložit?', 'Zajistěte všechny pojistky, zabrzděte kolečka a nenechávejte děti, aby se na zvednuté poloviny věšely nebo stůl skládaly samy.'),
        ('Kde koupit pingpongový stůl?', 'Sporteka porovná nabídky českých e-shopů pro konkrétní model. Objednávku vyřídíte v obchodě, který si vyberete, včetně domluvy dopravy velkého balíku.'),
    ])

# ------------------------------------------------------------------ masazni-valce
NEW['masazni-valce'] = dict(long=True,
    title='Masážní válce: foam roller, Blackroll, masážní tyče',
    desc='Masážní válce hladké i s výstupky, krátké, dlouhé i vibrační, masážní tyče. Jak vybrat tvrdost, velikost a povrch a kde válec koupit.',
    intro='<p><strong>Masážní válec</strong>, často nazývaný foam roller, je pěnový nebo plastový válec, po kterém se pomalu převalujete a vlastní vahou tlačíte na svaly. Lidé ho používají před tréninkem jako součást rozcvičení, po něm v rámci zklidnění nebo jen večer, když chtějí uvolnit ztuhlá záda po dni u počítače. Válce se liší tvrdostí, délkou, povrchem i tím, jestli mají vibrační motor. Masážní válec není zdravotnická pomůcka. Pokud vás něco bolí nebo se zotavujete po zranění, poraďte se nejdřív s fyzioterapeutem. V nabídce jsou krátké válce do sportovní tašky, dlouhé válce na cvičení na zemi i masážní tyče, které se drží v rukou a přejíždí se jimi po svalech.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů pro konkrétní válec a pak nakoupíte v tom obchodě, který vám sedí. V kategorii najdete výrobky značek Blackroll, Trigger Point, Pure2Improve, Lifefit nebo ' + B(('insportline', 'inSPORTline')) + '. Míčky, duoballs a další pomůcky jsou v nadřazené kategorii <a href="/masazni-pomucky/">masážní pomůcky</a>.</p>',
    guide='<h2>Typy masážních válců</h2>'
          '<p>Nejjednodušší je hladký válec z pěny, který tlačí rovnoměrně po celé délce. Válce s výstupky, žebry nebo mřížkovým povrchem soustředí tlak do menších bodů a jsou pocitově intenzivnější. Duté válce mají pevné plastové jádro obalené pěnou, díky kterému si drží tvar i po letech. Vibrační válce mají uvnitř motor a baterii a kromě tlaku přidávají i chvění v několika stupních. Masážní tyč se naopak drží v rukou a po svalu se přejíždí, takže se hodí na lýtka nebo stehna i bez lehání na zem.</p>'
          + T(['Typ', 'Jak působí', 'Pro koho se hodí'], [
              ['hladký pěnový válec', 'rovnoměrný tlak po celé délce', 'začátečníci, citlivější lidé'],
              ['válec s výstupky nebo mřížkou', 'tlak soustředěný do menších ploch', 'kdo už s válcem pracuje a chce víc'],
              ['dutý válec s pevným jádrem', 'drží tvar, nepromačká se', 'pravidelné používání, cvičení doma i v posilovně'],
              ['vibrační válec', 'tlak doplněný vibracemi', 'kdo chce víc variant a nevadí mu hmotnost a nabíjení'],
              ['masážní tyč', 'tlak rukama, ne vlastní vahou', 'lýtka a stehna, cestování, sezení'],
              ['mini válec', 'malý průměr, přesná místa', 'chodidla, předloktí, do tašky']]) +
          '<h2>Tvrdost: měkčí není horší</h2>'
          '<p>Výrobci často odlišují tvrdost barvou, například měkký, středně tvrdý a tvrdý válec v jedné řadě. Barvy ale nejsou sjednocené mezi značkami, takže se vždy dívejte na popis u konkrétního modelu. Začátečníkům se obvykle doporučuje měkčí nebo střední válec. Kdo s válcem začíná na nejtvrdším modelu, většinou se brání, napíná svaly a cvičení ho přestane bavit. Tvrdší válec dává smysl, když na měkčím už necítíte téměř nic, a i pak se hodí mít doma oba.</p>'
          '<h2>Materiály</h2>'
          + T(['Materiál', 'Vlastnosti'], [
              ['EPP (pěnový polypropylen)', 'lehký, pevný, drží tvar, snadno se otírá'],
              ['EVA pěna', 'pružná, příjemná na dotek, často na dutých válcích'],
              ['EPE (pěnový polyetylen)', 'měkký a levný, časem se může promáčknout'],
              ['plastové jádro s pěnou', 'velmi pevné, nedeformuje se pod vahou'],
              ['pryž a plast u tyčí', 'tvrdé kotoučky nebo válečky otáčivé na ose']]) +
          '<p>Kvalitní pěna nemá po vybalení silný chemický zápach a po zatížení se vrací do původního tvaru. U levných válců z měkké pěny se časem objeví prohlubeň v místě, kde se nejčastěji leží. Pak válec tlačí nerovnoměrně a je čas ho vyměnit.</p>'
          '<h2>Délka a průměr</h2>'
          '<p>Krátké válce kolem třiceti centimetrů se dobře skladují a vejdou se do sportovní tašky. Hodí se na nohy, hýždě a boky. Dlouhé válce kolem devadesáti centimetrů jsou stabilnější a dá se na ně lehnout podélně podél páteře. To je poloha, kterou lidé využívají i k protažení hrudníku nebo k jednoduchým cvikům na rovnováhu. Menší průměr znamená menší stabilitu a cílenější tlak, větší průměr je pohodlnější pro začátek. Úplně malé válce a míčky se používají na chodidla.</p>'
          '<h2>Masážní válec na záda</h2>'
          '<p>Na záda se válec používá nejčastěji v oblasti hrudní páteře, tedy mezi lopatkami. Leží se napříč přes válec, ruce podpírají hlavu, boky jsou na zemi nebo mírně zvednuté a tělo se pomalu posouvá. Bederní páteř se zpravidla nepřeválcovává přímo, protože tam chybí opora žeber. Pro záda se hodí i dlouhý válec, na který si lehnete podélně, nebo duoball, který obejde páteř po stranách. Pokud záda bolí dlouhodobě, s ostrou nebo vystřelující bolestí, válec nepomůže určit příčinu. V takovém případě patří na řadu lékař nebo fyzioterapeut.</p>'
          '<h2>Jak s válcem začít</h2>'
          '<ul><li><strong>Pomalu:</strong> válec po svalu posouvejte klidným tempem, rychlé převalování nic nepřinese.</li>'
          '<li><strong>Bez zadržování dechu:</strong> dýchejte volně, a když se zatajujete, je tlak příliš velký.</li>'
          '<li><strong>Tlak řídí ruce a nohy:</strong> opřením o podlahu ubíráte váhu, zvednutím druhé nohy ji přidáváte.</li>'
          '<li><strong>Mimo kosti a klouby:</strong> válcuje se přes svaly, ne přes kolena, kotníky nebo přímo přes páteř.</li>'
          '<li><strong>Kratší čas, častěji:</strong> několik minut na partii stačí, delší ležení na jednom místě nic nezlepší.</li>'
          '<li><strong>Na podložce:</strong> válec po ní neklouže a kosti se neopírají o tvrdou podlahu.</li></ul>'
          '<p>Nepříjemný tlak je při práci s válcem běžný, ostrá bolest ale ne. Pokud se objeví brnění, vystřelování do končetiny nebo bolest, která po cvičení neustupuje, přestaňte a poraďte se s odborníkem. S válcem opatrně také v těhotenství, při křečových žilách, po operacích nebo při užívání léků na ředění krve. Tam o vhodnosti rozhoduje lékař.</p>'
          '<h2>Válec, nebo masážní pistole?</h2>'
          '<p>Válec a <a href="/masazni-pistole/">masážní pistole</a> se nevylučují. Válec pracuje s vlastní vahou na velké plochy, nepotřebuje elektřinu a vydrží roky. Pistole cílí menší body, dosáhne i tam, kam se na válec špatně lehá, ale je dražší a potřebuje nabíjení. Kdo začíná, obvykle si vystačí s válcem, a pistoli přidá později, pokud zjistí, že mu rychlé cílené působení vyhovuje.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Pěnový válec stačí otřít vlhkým hadříkem, případně jemným mýdlem, a nechat uschnout. Nevystavujte ho dlouho slunci ani teplu od topení, pěna pak křehne a mění tvar. Vibrační válec se nemyje pod vodou, otírá se jen povrch a nabíjí podle návodu. Krátký válec se hodí do tašky, dlouhý se nejlépe skladuje svisle v rohu místnosti.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Nejtvrdší válec s výstupky jako první kus.</li>'
          '<li>Rychlé převalování tam a zpět bez kontroly tlaku.</li>'
          '<li>Válcování přímo přes bederní páteř nebo klouby.</li>'
          '<li>Očekávání, že válec vyřeší dlouhodobou bolest bez návštěvy odborníka.</li>'
          '<li>Dlouhé ležení na jednom bolestivém místě.</li></ul>'
          '<h2>Které partie se na válci cvičí nejčastěji</h2>'
          + T(['Partie', 'Poloha na válci', 'Na co myslet'], [
              ['lýtka', 'vsedě, válec pod lýtky, ruce za tělem', 'tlak přidáte překřížením nohou'],
              ['přední strana stehen', 'na předloktích, válec pod stehny', 'břicho zpevněné, bedra neprohýbat'],
              ['zadní strana stehen', 'vsedě, válec pod stehny', 'pomalu od kolena k hýždím'],
              ['hýždě', 'vsedě na válci, kotník přes koleno druhé nohy', 'mírné naklonění na stranu'],
              ['boky a vnější strana stehna', 'vleže na boku, opora o loket a nohu', 'začínejte s menším tlakem'],
              ['horní část zad', 'vleže napříč, ruce podpírají hlavu', 'bedra vynechat, pánev na zemi']]) +
          '<p>Tabulka je jen orientační. Konkrétní cviky a jejich pořadí vám nejlépe ukáže trenér nebo fyzioterapeut, který vidí, jak se hýbete. Návody najdete i v příbalových letácích a aplikacích některých výrobců.</p>'
          '<h2>Válec před tréninkem a po něm</h2>'
          '<p>Před během, posilovnou nebo míčovou hrou se válec používá krátce a spíš svižněji, jako jedna z částí rozcvičení vedle rozchození a dynamického protažení. Nemá nahrazovat zahřátí celého těla. Po tréninku a večer se válcuje pomaleji a s menším důrazem na výkon, spíš jako klidná chvíle na zemi. Mnoho běžců nosí krátký válec nebo masážní tyč v tašce na závody a používá je v čekání na start. Kdo sedí většinu dne, může válec zařadit jako krátkou přestávku: pár minut na zádech a na hýždích po pracovním dni bývá příjemnou změnou.</p>'
          '<h2>Na co se dívat v popisu válce</h2>'
          '<ul><li><strong>Délka a průměr</strong> v centimetrech, ne jen označení mini nebo standard.</li>'
          '<li><strong>Tvrdost</strong> slovně nebo na stupnici výrobce, barva sama nic neříká.</li>'
          '<li><strong>Jádro:</strong> plný pěnový válec, nebo dutý s plastovou trubkou uvnitř.</li>'
          '<li><strong>Nosnost</strong> u dutých a vibračních válců, pokud na nich chcete i cvičit.</li>'
          '<li><strong>U vibračních modelů</strong> počet stupňů, výdrž baterie a způsob nabíjení.</li></ul>'
          '<h2>Válec jako cvičební pomůcka</h2>'
          '<p>Dlouhý válec se nevyužívá jen k masáži. V pilates a ve cvičení na stabilitu slouží jako nestabilní opora, na které se leží podélně a cvičí pohyby paží a nohou. Krátký pevný válec se dá použít i při posilování středu těla, například při plankových variantách, kdy jsou ruce nebo chodidla opřené o válec. Pro tyto účely se hodí válec s pevným jádrem, který se pod vahou nedeformuje a drží tvar, a k němu protiskluzová podložka.</p>'
          '<h2>Související kategorie</h2>'
          '<p>K válci se hodí podložka z kategorie <a href="/joga-a-podlozky/">jógové podložky</a> a další pomůcky z <a href="/jogove-pomucky/">jógových pomůcek</a> nebo <a href="/pilates-pomucky/">pilates pomůcek</a>. Na protahování a posilování po válcování navazují <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/balancni-pomucky/">balanční pomůcky</a>, další drobné vybavení na cvičení najdete mezi <a href="/fitness-pomucky/">fitness pomůckami</a>. Pro sportovce se ještě hodí <a href="/tejpy/">tejpy</a> a <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>',
    faq=[
        ('K čemu je masážní válec?', 'K automasáži, kdy se po válci pomalu převalujete a vlastní vahou tlačíte na svaly. Používá se při rozcvičení, po tréninku nebo k uvolnění po dlouhém sezení.'),
        ('Jaký masážní válec vybrat pro začátečníka?', 'Hladký válec měkké nebo střední tvrdosti v délce kolem třiceti centimetrů. Je univerzální a tlak na něm snadno ovládnete.'),
        ('Je lepší válec hladký, nebo s výstupky?', 'Hladký tlačí rovnoměrně a je mírnější, s výstupky je pocitově intenzivnější. Mnoho lidí začne hladkým a vroubkovaný přidá později.'),
        ('Lze válec použít na záda?', 'Ano, zpravidla na oblast mezi lopatkami. Přímo přes bederní páteř se nepřeválcovává. Při dlouhodobé nebo ostré bolesti zad se nejdřív poraďte s lékařem nebo fyzioterapeutem.'),
        ('Jak dlouho válcovat?', 'Obvykle stačí několik minut na jednu partii. Delší a silnější válcování na jednom místě nic navíc nepřinese.'),
        ('Co je Blackroll?', 'Značka masážních válců a pomůcek. Její válce jsou z pěnového polypropylenu, který je lehký a drží tvar. Slovo se v češtině často používá i obecně pro pěnový válec.'),
        ('Má smysl vibrační válec?', 'Pro někoho ano, protože k tlaku přidává vibrace v několika stupních. Je ale těžší, dražší a musí se nabíjet. Kdo začíná, vystačí si s obyčejným válcem.'),
        ('Kdy válec nepoužívat?', 'Na čerstvé zranění, otok, přes klouby a kosti a při ostré nebo vystřelující bolesti. Opatrnost a konzultace s lékařem jsou na místě i v těhotenství nebo po operaci.'),
        ('Kde koupit masážní válec?', 'Sporteka u každého válce ukáže nabídky několika českých e-shopů. Objednáte pak v obchodě, který si vyberete.'),
    ])
