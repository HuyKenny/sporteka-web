"""sporteka.cz — facet landing texts wave 135: decathlon-badminton, gymbeam-teplaky, lyzarske-rukavice-panske, horska-kola-vyprodej.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ decathlon-badminton
NEW['decathlon-badminton'] = dict(
    title='Decathlon badminton: rakety, míčky a sítě pro hru',
    desc='Decathlon badminton: rekreační rakety BR1, sady Discover, plastové míčky PSC, sítě a čáry na hřiště. Jak vybrat pro děti, zahradu i školní tělocvik.',
    intro='<p>Badmintonové zboží pod značkou Decathlon míří hlavně na rekreační hráče: rodiny, školy, kroužky, kempy a lidi, kteří si chtějí zahrát bez investice do závodní rakety. V nabídce najdete jednoduché rakety řady BR, dětské sady Discover, plastové a péřové míčky řady PSC, přenosné sítě i modulární čáry na hřiště. '
          'Stránka sbírá právě tyto produkty z kategorie <a href="/badminton/">badminton</a> a vysvětluje, co se za jednotlivými názvy skrývá, kdy stačí set a kdy se vyplatí samostatná raketa. Průvodce dále ukazuje, jak vybrat míčky pro halu a pro zahradu, na co dát pozor u sítí a kdy je rozumné přejít k výkonnostním raketám značek <a href="/znacka/yonex/">Yonex</a> nebo <a href="/znacka/babolat/">Babolat</a>. Souvisí s tím i <a href="/tenis/">tenis</a>, <a href="/squash/">squash</a> a <a href="/salova-obuv/">sálová obuv</a>.</p>',
    guide='<h2>Co v badmintonu od Decathlonu najdete</h2>'
          '<p>Decathlon je zároveň obchod i výrobce vlastních sportovních řad, takže jeho badmintonová nabídka je uzavřený systém: raketa, míčky, síť i vyznačení hřiště si k sobě pasují a dají se pořídit najednou. To je rozdíl proti značkám, které vyrábějí převážně rakety a ostatní vybavení řeší jiní dodavatelé. Přehled toho, co v nabídce potkáte, shrnuje tabulka.</p>'
          + T(['Typ zboží', 'Označení v nabídce', 'Pro koho'], [
              ['Samostatná raketa', 'řada BR, například BR 1', 'rekreační hra, školní hodiny, začátečníci'],
              ['Sady pro děti a rodiny', 'Discover, Easy Set', 'zahrada, dovolená, první seznámení se hrou'],
              ['Plastové míčky', 'řada PSC s čísly 100, 130, 500, 900', 'hra venku, škola, trénink v hale'],
              ['Přenosné sítě', 'Fun, Discover Set, Speednet', 'zahrada, hřiště, sál bez stálé sítě'],
              ['Sloupky a oficiální síť', 'síť se sloupky na standardní rozměr', 'klub, škola, pravidelný domácí kurt'],
              ['Čáry na hřiště', 'modulární Fun Line', 'trávník, dvorek, nezpevněný povrch'],
              ['Air badminton', 'sada sloupků a sítě na písek a trávník', 'pláž, kemp, větrné prostředí']]) +
          '<p>Nabídka se mění podle sezóny a dostupnosti, takže se vyplatí otevřít detail a zkontrolovat, co přesně balení obsahuje. U sad bývá nejčastější záměna počet raket, počet míčků a to, zda je v ceně i síť. Označení BR1 se v názvech opakuje u samostatné rakety, u dětské sady i u sady pro dva hráče, proto čtěte celý název, ne jen začátek.</p>'
          '<h2>Rekreační raketa BR: co od ní čekat</h2>'
          '<p>Rekreační rakety se nedělají na maximální rychlost smeče, ale na to, aby odpouštěly chyby a nebolela po nich ruka. Rám bývá z lehkého kovu nebo kompozitu, násada je spíše pružná a rukojeť má jednoduchý povrch, který se dobře drží i dětem. Pro pár výměn na zahradě nebo hodinu týdně v tělocvičně to bohatě stačí. Výkonnostní hráč by naopak poznal menší přesnost a větší chvění při tvrdém úderu.</p>'
          '<ul><li><strong>Váha:</strong> lehká raketa se snáze rozmává, a proto unaví méně i při delší hře.</li>'
          '<li><strong>Vyvážení:</strong> u rekreačních modelů bývá blízko středu, takže se s nimi dobře vítá i obrana.</li>'
          '<li><strong>Rukojeť:</strong> tlustší a hladší rukojeť pohodlněji padne do malé dlaně, tenčí do větší; ladit lze omotávkou, tedy grip páskou.</li>'
          '<li><strong>Odolnost:</strong> rám snese občasný náraz do země, ale přesto s raketou nenarážejte do podlahy.</li>'
          '<li><strong>Struny:</strong> u základních modelů jsou předpjaté z výroby a nedoporučuje se je přepínat, výměna by stála víc než celá raketa.</li></ul>'
          '<h2>Sady Discover a Easy Set: jak je číst</h2>'
          '<p>Sada je rozumná volba, pokud jde o první badmintonové vybavení v domácnosti. Obvykle obsahuje dvě rakety, jeden nebo dva míčky a často přenosnou síť s držáky. Dětská varianta má rakety kratší a lehčí, aby je zvládlo i malé dítě; dospělá raketa může mít podle pravidel délku nejvýš 68 centimetrů a ta dětská zůstává hluboko pod tímto limitem.</p>'
          '<p>Než sadu koupíte, ujasněte si, kdo bude hrát. Pro mladší školáky se hodí lehká dětská sada, pro rodinnou hru dospělých a dětí raději dvě normální rakety a pár míčků navíc. Dospívající hráč, který chodí do oddílu, ze sady brzy vyroste a bude chtít samostatnou raketu. Takový přechod usnadní srovnání s kategorií <a href="/badminton/">badminton</a>, kde jsou rakety řazené podle váhy a vyvážení.</p>'
          '<h2>Míčky PSC: plast, peří a čísla v názvu</h2>'
          '<p>Řada PSC zahrnuje plastové míčky různých tříd. Číslo v názvu zpravidla ukazuje stupnici od základních po nejnáročnější: sto je určeno pro volnou hru, pětistovka pro pravidelný trénink a devítistovka pro vyšší nároky na stabilitu letu. Označení Medium popisuje rychlost letu, tedy to, jak daleko míček doletí při stejné síle úderu; konkrétní sezónu a prostředí si ověřte u produktu.</p>'
          + T(['Vlastnost', 'Plastový míček', 'Péřový míček'], [
              ['Trvanlivost', 'vydrží opakované smeče a pády', 'peří se láme, míček je dřív opotřebovaný'],
              ['Chování v letu', 'předvídatelný, mírně těžší', 'citlivější, přesnější na úder'],
              ['Vítr a venek', 'snáší lépe', 'vítr ho hodně vychyluje'],
              ['Použití', 'škola, zahrada, rodinná hra', 'klubový trénink, soutěž v hale'],
              ['Údržba', 'téměř žádná', 'občas vyrovnat peří prsty'],
              ['Cena za hodinu hry', 'nižší díky životnosti', 'vyšší kvůli rychlé spotřebě']]) +
          '<p>Některé míčky z řady PSC jsou označené jako Nite nebo mají světelný prvek pro večerní hru. Hodí se na zahradu a do kempu; bez ohledu na to vybírejte velikost balení podle toho, kolik hodin hrajete. Míčky se ztrácejí v křoví a rozbíjejí se o strop, tak počítejte s rezervou.</p>'
          '<h2>Sítě: oficiální, přenosná a multisportovní</h2>'
          '<p>Při nákupu sítě rozhoduje, kde bude stát. Oficiální síť se sloupky pro klub nebo školní tělocvičnu má hřiště pro čtyřhru široké 6,1 metru, proto se i rozměr sítě a zavěšení řídí touto hodnotou. Pro dvouhru je kurt užší, ale síť zůstává stejná. Nezpevněný terén naopak potřebuje přenosnou síť s širokou podstavou nebo kolíky, jinak ji nárazy větru převrátí.</p>'
          '<p>Zajímavou skupinu tvoří multisportovní sítě typu Speednet, které se používají pro badminton, tenis i pickleball. Každý z těchto sportů má jinou výšku sítě: badminton ji vyvěšuje výš než tenis a pickleball je ještě o něco nižší, takže dobrá multisportovní síť musí mít nastavitelné napětí a výšku. Při koupi se podívejte, jak rychle se síť staví, zda se vejde do auta a jestli jsou v sadě všechny kolíky a tyče.</p>'
          '<h2>Hra venku a čáry na hřiště</h2>'
          '<p>Venkovní badminton je jiná hra než sálový. Vítr mění dráhu míčku, slunce oslňuje a nerovný povrch mění pohyb. Proto se doporučuje hrát přes síť s menšími výměnami a bez soutěžního tlaku. Modulární čáry Fun Line pomáhají označit hřiště na trávníku nebo na dvorku tak, abyste věděli, kde je za čárou, a hra dostala pravidla. Pro pláž a trávu slouží varianta air badminton, která má těžší, proti větru odolnější míček a vlastní pravidla.</p>'
          '<p>Pokud chcete mít na zahradě víc her, prohlédněte si také <a href="/hry-na-zahradu/">hry na zahradu</a>. U dětí funguje lépe rodinná soutěž o počet výměn než klasické počítání bodů, protože malý hráč zažije úspěch dřív.</p>'
          '<h2>Pro děti, školu a kroužky</h2>'
          '<p>Učitelé tělesné výchovy a trenéři dětí vybírají hlavně podle odolnosti a snadnosti. Lehká raketa, plastový míček a nízká síť zjednoduší první hodiny a umožní, aby se do hry zapojila celá třída. Dětem mezi sedmi a deseti lety stačí hřiště zmenšené o část délky. Pokud kroužek sdílí vybavení, kupujte rakety stejné značky a váhy, aby výměna rakety nemusela znamenat nové zvykání.</p>'
          '<ul><li><strong>Škola:</strong> více raket stejného typu, plastové míčky, přenosná síť.</li>'
          '<li><strong>Oddíl:</strong> košík míčků do hodiny tréninku, rezervní grip pásky, tašky.</li>'
          '<li><strong>Rodina:</strong> sada se sítí a dvěma raketami, rezerva míčků.</li>'
          '<li><strong>Kemp:</strong> lehká síť, kolíky, plast místo peří.</li></ul>'
          '<h2>Kdy přejít k výkonnostním raketám</h2>'
          '<p>Signálem je chvíle, kdy hrajete pravidelně a cítíte, že raketa limituje úder. Pokud vám často praskají struny, pokud rám po pádu praskne nebo když chcete trénovat smeč a přesnou hru u sítě, patří vám raketa s grafitovým rámem. Z výkonnostních značek na Sportece najdete <a href="/znacka/yonex/">Yonex</a>, <a href="/znacka/victor/">Victor</a>, <a href="/znacka/babolat/">Babolat</a>, <a href="/znacka/carlton/">Carlton</a> a <a href="/znacka/talbot-torro/">Talbot Torro</a>; pro srovnání ceny i parametrů je dobré dívat se na váhu, vyvážení a tuhost. Zůstat můžete i u dostupnějších značek jako <a href="/znacka/nils/">Nils</a>, jejichž sety stojí mezi rekreační a klubovou úrovní.</p>'
          '<h2>Péče o vybavení</h2>'
          '<p>K raketě patří i ochrana při přenášení: <a href="/sportovni-tasky/">sportovní taška</a> nebo termopouzdro ochrání rám před nárazy. Rakety skladujte v pouzdře, ne v mrazu a ne v rozpáleném autě, protože teplota ničí rám i strunu. Míčky mějte v původní tubě nebo krabici, plastové po vlhké hře osušte. Síť po použití nechte uschnout a svinujte ji volně, jinak se v ní vytvoří uzly. Grip omotávku měňte, jakmile se začne klouzat nebo trhat; jde o nejlevnější způsob, jak vrátit raketě pocit z nové.</p>'
          '<h2>Raketové sporty a přenos dovedností</h2>'
          '<p>Kdo si oblíbí badminton, často zkouší i další raketové hry. Reflexy a práce zápěstí se dají přenést na <a href="/squash/">squash</a> a <a href="/padel/">padel</a>, kde se hraje v uzavřeném prostoru, nebo na <a href="/tenisove-rakety/">tenisové rakety</a> a hru na dvorci. Jejich rakety jsou však těžší a dlouhé zápěstní pohyby z badmintonu je třeba přizpůsobit. Pro děti je střídání her užitečné, protože rozvíjí koordinaci bez jednotvárnosti.</p>'
          '<h2>Rychlý kontrolní seznam před koupí</h2>'
          '<ol><li>Rozhodněte, zda potřebujete sadu, nebo samostatnou raketu.</li>'
          '<li>Zjistěte, kde budete hrát, a podle toho zvolte plast nebo peří.</li>'
          '<li>Zkontrolujte, zda je v balení síť, kolíky a míčky.</li>'
          '<li>U dětí volte kratší a lehčí raketu než pro dospělé.</li>'
          '<li>Porovnejte stejný produkt v několika obchodech včetně dopravy.</li></ol>',
    faq=[
        ('Jsou badmintonové rakety Decathlonu vhodné pro začátečníky?', 'Ano, rakety řady BR jsou stavěné právě pro začátečníky a rekreační hráče. Jsou lehké, odpouštějí chyby a rukojeť se dobře drží i v malé ruce. Pro pravidelný klubový trénink budete po čase chtít přesnější raketu, ale na první sezónu jsou zcela dostačující.'),
        ('Co obsahuje sada Discover?', 'Obvykle několik raket, míčky a síť nebo její část. Konkrétní složení se mezi verzemi liší, proto zkontrolujte popis produktu. Hledejte počet raket, počet míčků, zda je v balení síť a jestli jsou součástí kolíky a pouzdro.'),
        ('Jaký míček zvolit pro hru venku?', 'Plastový. Snáší pády, tvrdé údery a mokrou trávu lépe než peří a letí předvídatelněji. Peřové míčky vítr vychyluje a po pár výměnách se poškodí, takže se vyplatí jen pro hru v hale.'),
        ('Co znamenají čísla v názvu míčků PSC?', 'Číslo obvykle řadí míčky od jednodušších po náročnější třídy. Nižší číslo je určeno pro volnou hru, vyšší pro stabilnější let a trénink. Přesné parametry vždy čtěte u konkrétního produktu, protože označení se může lišit mezi sériemi.'),
        ('Jak vysoko má viset badmintonová síť?', 'Podle pravidel kolem sloupků asi 1,55 metru a uprostřed o něco níž. Pro zahradní hru nejde o přesnou míru, ale s nižší sítí se hra rozběhne snáz. Multisportovní sítě mají nastavitelnou výšku, aby se daly použít i na tenis a pickleball.'),
        ('Dá se hrát badminton na trávníku?', 'Dá, jen musíte počítat s rozdíly. Míček se hůř odráží, vítr hru ovlivňuje a nohy se na trávě pohybují pomaleji. Pomůžou přenosné čáry, těžší plastový míček a síť s pevnou podstavou. Pro větrné prostředí existuje i varianta air badminton.'),
        ('Jak vybrat raketu pro dítě?', 'Podle délky a váhy. Dětské rakety jsou kratší a lehčí, aby dítě zvládlo švih bez námahy. Nekupujte raketu na vyrůstání, protože příliš dlouhá raketa ničí techniku a unavuje. Pro předškoláky stačí lehká plastová sada, pro školáky raketa s lehkým kovovým rámem.'),
        ('Mám raději sadu, nebo samostatné rakety?', 'Pokud hrajete nárazově s rodinou, je sada nejpohodlnější. Pro pravidelnou hru dvou dospělých je lepší dvě samostatné rakety a krabice míčků, protože nejsou omezeny kvalitou nejslabšího kusu v setu. U dětí zase sada dává smysl, dokud nezačnou trénovat v oddíle.'),
        ('Kdy se vyplatí přejít na Yonex nebo Babolat?', 'Když hrajete pravidelně a chcete lepší kontrolu úderu, nižší váhu a citlivější vyvážení. Výkonnostní raketa má většinou grafitový rám a tužší násadu, což oceníte při smeči a hře u sítě. Pro občasnou hru zůstává rekreační raketa praktičtější a odolnější.'),
        ('Jak dlouho vydrží rekreační raketa a míčky?', 'Raketa vydrží roky, pokud ji nenecháte v mrazu ani v horkém autě a nebudete jí narážet do podlahy. Plastové míčky vydrží řádově víc než peřové, ale po vlhké hře je osušte. Nejdřív se opotřebuje grip, který se dá levně vyměnit.'),
    ])

# ------------------------------------------------------------------ gymbeam-teplaky
NEW['gymbeam-teplaky'] = dict(
    title='GymBeam tepláky: střihy, modely a velikosti',
    desc='GymBeam tepláky pánské i dámské: oversized, slim, jogger a zvonové střihy, řady Relay, Limitless, TRN. Jak vybrat velikost a materiál.',
    intro='<p>GymBeam je značka z fitness světa, která se z doplňků a výživy rozrostla i do oblečení, a tepláky patří k jejím nejviditelnějším kouskům. Najdete mezi nimi úzké slim střihy do posilovny, volné oversized tepláky na každý den, joggery s manžetou i zvonové dámské modely. '
          'Stránka sbírá GymBeam produkty z kategorie <a href="/teplaky/">tepláky</a> a vysvětluje, jak se liší jednotlivé řady, jak vybrat velikost u volných střihů a co se nosí v posilovně, doma a ve městě. Porovnat můžete také <a href="/nike-teplaky/">Nike</a>, <a href="/teplaky-puma/">Pumu</a> nebo <a href="/jordan-teplaky/">Jordan</a>, doplnit outfit o <a href="/gymbeam-leginy/">legíny GymBeam</a> a <a href="/gymbeam-kratasy/">kraťasy</a> a nezapomeňte ani na <a href="/mikiny/">mikiny</a>, které se k teplákům nosí nejčastěji. Průvodce shrnuje také praní, materiály a rozdíly mezi pánskými a dámskými řadami, aby výběr nebyl jen otázkou barvy.</p>',
    guide='<h2>Co je pro GymBeam tepláky typické</h2>'
          '<p>Značka vyrostla v prostředí posilovny a to je na jejích teplácích poznat. Pasy bývají široké a pevné, aby při dřepu neklouzaly, kapsy hluboké a materiál pružný. Zároveň má nabídka vyhraněný módní rozměr: oversized siluety, výrazné barvy v duchu písku, eukalyptu nebo fíku a pojmenování kolekcí, které se sbírají do sad s mikinami a topy. U každého modelu proto sledujte nejen pohlaví, ale i řadu, ve které je vyroben.</p>'
          + T(['Řada', 'Střih a pocit', 'Pro koho a kam'], [
              ['Relay', 'volnější, oversized, pro muže i ženy', 'město, volný čas, cesta do posilovny'],
              ['Limitless', 'jogger s manžetou, jednoduchý design', 'trénink i každodenní nošení'],
              ['Urban', 'klasický, střední objem', 'základní tepláky, denní nošení'],
              ['Slimfit a Agile', 'úzké nohavice, přiléhavé', 'posilovna, běh, funkční trénink'],
              ['TRN', 'pružný materiál, sportovní střih', 'tréninkový režim, kardio'],
              ['Aura, Base a Unity', 'oversized a regular fit', 'volnočasový styl, kombinace s mikinou'],
              ['GymBabe, Mochi, NEO', 'dámské střihy, někdy zvonové nebo bokové', 'ženy, módní i sportovní využití']]) +
          '<p>Názvy kolekcí se mohou obměňovat a modely se vracejí v nových barvách, takže uvedené řady berte jako orientační mapu. Spolehlivá je vždy tabulka velikostí a popis střihu u konkrétního kusu.</p>'
          '<h2>Střihy: slim, regular, oversized a zvonové</h2>'
          '<p>U GymBeam se střih popisuje několika slovy, která se hodí pochopit. <strong>Slim fit</strong> přiléhá k noze, a tak je praktický pro dynamické cviky; v něm se nic nezachytí o činku a vidíte linii nohy. <strong>Regular fit</strong> je střední varianta bez zvláštních efektů a zvládne téměř všechno. <strong>Oversized</strong> záměrně nabízí víc prostoru v hrudi, stehnech i nohavicích; je to styl, ne chyba v číslování. <strong>Zvonové</strong> dámské tepláky jsou na kolenou užší a od lýtek se rozšiřují, což se hodí k botám a pro styl, méně pro kardio, kde by nohavice překážely.</p>'
          '<ul><li><strong>Posilovna a dřepy:</strong> slim nebo regular s pružným materiálem a pevným pasem.</li>'
          '<li><strong>Běh a kardio:</strong> lehčí a přiléhavější modely, ne těžké froté.</li>'
          '<li><strong>Město a škola:</strong> oversized nebo regular v klidných barvách.</li>'
          '<li><strong>Doma a na cesty:</strong> měkké a volné střihy, které se nemačkají.</li>'
          '<li><strong>S botami:</strong> manžeta u kotníku se hodí k teniskám, zvonové k plochým podrážkám.</li></ul>'
          '<h2>Jak vybrat velikost u volných střihů</h2>'
          '<p>Nejčastější chyba je přenášet na oversized tepláky svou běžnou velikost a čekat stejný výsledek jako u klasických modelů. U volného střihu se výrobce počítá s tím, že nohavice jsou širší a pas sedí níž. Pokud chcete záměrně volný efekt, držte se své běžné velikosti. Pokud je chcete spíš pohodlné a ne příliš objemné, zvažte o stupeň menší, ale pouze tehdy, že tabulka potvrzuje dostatečný obvod boků a stehen.</p>'
          + T(['Míra', 'Kde ji změřit', 'Na co ji porovnat'], [
              ['Obvod pasu', 'nad pupkem, v nejužším místě', 'rozměr pasu v tabulce, u pružného pasu s rezervou'],
              ['Obvod boků', 'v nejširším místě', 'u slim střihu nejdůležitější míra'],
              ['Délka vnitřního švu', 'od rozkroku ke kotníku', 'délka nohavice, zvlášť u joggerů'],
              ['Výška postavy', 'bez bot', 'orientačně u oversized střihů']]) +
          '<p>Nejjistější způsob je změřit tepláky, které vám sedí, a porovnat je s rozměry produktu. Pokud obchod rozměry uvádí v centimetrech, je to nejspolehlivější vodítko, protože označení S, M a L se mezi značkami liší.</p>'
          '<h2>Materiál: bavlna, směsi a pružnost</h2>'
          '<p>Většina modelů GymBeam spojuje bavlnu s polyesterem a často i elastanem. Bavlna dává měkkost a příjemný pocit na kůži, polyester přidává tvarovou stálost a rychlejší schnutí, elastan pružnost. Směs funguje v posilovně i na ulici a není tak citlivá na praní jako čistá bavlna. Hustší teplákovina s vnitřní plyšovou stranou zahřeje, tenčí pletenina se hodí na jaro a léto. Při koupi si všímejte popisu gramáže, pokud je uvedena, a toho, zda jde o hladkou nebo žebrovanou manžetu.</p>'
          '<p>Světlé a pastelové barvy, kterými je GymBeam proslulý, se rychleji zašpiní a u bavlněných směsí mohou po praní zešednout. Praní naruby, ve studené vodě a bez aviváže prodlouží život barvě i vláknu. Aviváž navíc u funkčních materiálů zanáší vlákno a zhoršuje odvod vlhkosti.</p>'
          '<h2>Pánské, dámské a unisex</h2>'
          '<p>Dámské modely mají obvykle užší pas a výraznější linii boků, zatímco pánské jsou rovnější. Oversized tepláky ale často nosí oba pohlaví, a tak se vyplatí číst popis střihu místo spoléhání na štítek. Dámské řady jako GymBabe nebo Mochi zahrnují kromě kalhot i teplákové šortky a bokové střihy, které se hodí do léta. Dámské modely najdete i v hlavní kategorii <a href="/teplaky/">tepláky</a>, kde je lze porovnat s ostatními značkami.</p>'
          '<h2>Jak tepláky zapadnou do outfitu</h2>'
          '<p>Značka často prodává kalhoty a mikiny jako sladěnou sadu. Když je kupujete odděleně, hlídejte, aby se shodovala barva a odstín, protože stejný název barvy se může mezi šaržemi mírně lišit. Pro posilovnu jsou praktické tepláky ve tmavé barvě, které nehlásí pot, pro město se kombinují světlé tóny s tričkem a mikinou. K teplákům patří také <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/leginy/">legíny</a>, mezi kterými si vyberete podle teploty v posilovně.</p>'
          '<h2>Kde GymBeam narazí na konkurenci</h2>'
          '<p>Sportovní velikány jako <a href="/znacka/nike/">Nike</a>, <a href="/znacka/adidas/">Adidas</a> nebo <a href="/znacka/puma/">Puma</a> stavějí na dlouholeté historii a široké nabídce od fotbalu po lifestyle. GymBeam se zaměřuje na lidi, kteří chodí do posilovny a mají rádi výrazný vzhled. Proto jsou jeho tepláky často pružnější a s více kapsami, zatímco klasické značky nabízejí tradičnější střihy a větší sortiment velikostí pro děti. Rozhodnutí tedy závisí na tom, zda hledáte funkci pro trénink, nebo klasický styl.</p>'
          '<h2>Doplňky z GymBeam, které k teplákům patří</h2>'
          '<p>GymBeam není jen oblečení, a proto se na něm dobře ukazuje, jak sportovní výbava drží pohromadě. Kdo trénuje pravidelně, často řeší i výživu a regeneraci a stejná značka nabízí <a href="/gymbeam-proteiny/">proteiny</a> a <a href="/gymbeam-kreatin/">kreatin</a>. Tepláky tak můžete kupovat spolu s dalším fitness zbožím, ale i tak se vyplatí porovnat dopravu v několika obchodech, protože balíky se skládají jinak.</p>'
          '<h2>Sezónnost: kdy tepláky pomáhají a kdy ne</h2>'
          '<p>Tepláky se nosí celý rok, ale každé roční období chce jiný materiál. Na podzim a v zimě oceníte hustší pleteninu a vnitřní plyš, na jaře a v létě tenčí pleteninu, popřípadě teplákové šortky. Na ranní běh v chladu se hodí přiléhavé tepláky pod větrovku, v posilovně s klimatizací volnější model. Pokud chodíte do posilovny v zimě pěšky, počítejte s tím, že se tepláky mohou zvenku zavlhčit, a mějte náhradní pár. Mokrá teplákovina se na kůži rychle ochlazuje a vyžaduje čas na vyschnutí.</p>'
          '<h2>Chyby, které se při nákupu opakují</h2>'
          '<ul><li><strong>Koupě podle fotografie:</strong> model na postavě vypadá jinak než na vašem těle, proto vždy ověřte rozměry.</li>'
          '<li><strong>Ignorování délky:</strong> u vyšších lidí bývají nohavice u joggerů krátké, u nižších se hromadí na kotnících.</li>'
          '<li><strong>Zaměňování střihů:</strong> oversized a regular nejsou totéž a stejná velikost sedí jinak.</li>'
          '<li><strong>Nevšímání si složení:</strong> čistá bavlna se po praní chová jinak než směs s polyesterem.</li>'
          '<li><strong>Špatná barva do posilovny:</strong> světlá barva ukazuje pot a otěr od lavice.</li></ul>'
          '<h2>Praní a péče</h2>'
          '<ol><li>Perte při nízké teplotě, na rubu, aby se nepoškodil potisk nebo vyšívané logo.</li>'
          '<li>Nepoužívejte aviváž, která zhoršuje odvod potu.</li>'
          '<li>Sušte volně nebo na nízkou teplotu, aby se materiál nesmrštil.</li>'
          '<li>Světlé a tmavé kusy perte odděleně.</li>'
          '<li>Před praním zavřete zipy a odstraňte předměty z kapes.</li></ol>'
          '<p>Správná péče má význam hlavně u světlých barev, které si žádají jemnější režim než černé nebo šedé modely.</p>',
    faq=[
        ('Jsou GymBeam tepláky vhodné do posilovny?', 'Ano, GymBeam vznikl pro fitness prostředí. Hledejte modely označené jako slim nebo jogger s pružným materiálem, pevným pasem a kapsami. Volné oversized tepláky jsou naopak spíš volnočasové a při cvicích mohou překážet.'),
        ('Jak vybrat velikost u oversized střihu?', 'Pokud chcete volný efekt, držte se své běžné velikosti. Chcete-li menší objem, zvolte o stupeň menší, ale ověřte si obvod boků a stehen. Nejspolehlivější je porovnat rozměry v tabulce s tepláky, které vám sedí.'),
        ('Čím se liší pánské a dámské tepláky GymBeam?', 'Dámské mají užší pas a tvarované boky, pánské jsou rovnější. U oversized střihů se ale rozdíly stírají a oba pohlaví nosí oboje. Proto čtěte popis střihu, ne jen štítek, a porovnejte rozměry.'),
        ('Z čeho jsou GymBeam tepláky vyrobené?', 'Nejčastěji z bavlny smíchané s polyesterem, často s příměsí elastanu. Bavlna dává měkkost, polyester tvarovou stálost a elastan pružnost. Přesné složení je uvedeno u každého produktu a je lepší si ho přečíst než spoléhat na název řady.'),
        ('Srážejí se tepláky po praní?', 'Bavlněné směsi se mohou mírně srazit, zvlášť při vysoké teplotě a sušení v sušičce. Perte při nízké teplotě a sušte volně. U modelů s vysokým podílem elastanu je problém menší, ale i ty tepla nesnášejí.'),
        ('Co jsou zvonové tepláky?', 'Dámské tepláky, které jsou nahoře přiléhavé a od kolen se rozšiřují. Nosí se hlavně jako módní doplněk a k plochým botám. Na běh a dynamické cviky se hodí méně, protože širší nohavice překáží a mohou se zachytit.'),
        ('Dají se GymBeam tepláky nosit do města?', 'Ano. Oversized, regular a jogger střihy v klidných barvách zapadnou do každodenního outfitu. Pro formálnější prostředí je lepší tmavý odstín a jednoduchý střih bez výrazného potisku.'),
        ('Jak poznám, že je model pánský, nebo dámský?', 'Podle názvu produktu a popisu, často je v něm uvedeno Pánské, Dámské nebo Women. Některé modely jsou unisex, což se pozná podle popisu střihu a tabulky. V případě pochybností vyberte obchod, který uvádí rozměry v centimetrech.'),
        ('Jak prát světlé tepláky, aby nešedly?', 'Perte je naruby ve studené vodě s jemným prostředkem, bez aviváže a odděleně od tmavých kusů. Sušte stranou od přímého slunce. Silné odstíny jako písek nebo eukalyptus mohou po opakovaném praní vyblednout, proto šetrnější režim vyplatí.'),
        ('Kde se dají porovnat ceny GymBeam tepláků?', 'U každého produktu vidíte nabídky více obchodů vedle sebe i s dopravou. Stejný model se může lišit v dostupných velikostech, proto porovnávejte nejen cenu, ale i to, zda je u obchodu právě vaše velikost skladem.'),
    ])

# ------------------------------------------------------------------ lyzarske-rukavice-panske
NEW['lyzarske-rukavice-panske'] = dict(
    title='Lyžařské rukavice pánské: velikost, teplo a konstrukce',
    desc='Pánské lyžařské rukavice: velikost podle obvodu dlaně, Gore-Tex, kůže, izolace a délka manžety. Jak vybrat pro lyžování, snowboard i mrazivé dny.',
    intro='<p>Pánská lyžařská rukavice se od dámské a dětské liší hlavně proporcemi: širší dlaní, delšími prsty a většími velikostmi, které se hledají hůř, než by se zdálo. Přitom na svahu právě ruce chladnou jako první, protože držení holí zpomaluje prokrvení. '
          'Stránka sbírá pánské modely z kategorie <a href="/lyzarske-rukavice/">lyžařské rukavice a palčáky</a> a vysvětluje, jak vybrat velikost podle obvodu dlaně, kdy sáhnout po kůži a kdy po membráně, a v čem se liší rukavice pro sjezd, skialp a běžky. Další varianty najdete pod <a href="/detske-lyzarske-rukavice/">dětskými</a> a <a href="/damske-rukavice/">dámskými rukavicemi</a>. Na výbavu navazují <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice</a>, <a href="/lyzarske-helmy/">helmy</a> a <a href="/zimni-sporty/">další zimní sporty</a>. Průvodce vysvětluje i péči, vrstvení a rozdíly mezi značkami, aby výběr nebyl jen o velikosti.</p>',
    guide='<h2>V čem se pánská rukavice liší</h2>'
          '<p>Pánské střihy počítají s širší dlaní a delšími prsty. Dlaň se v nich nezužuje tak výrazně v zápěstí a manžeta je často širší, aby se vešla přes rukáv objemnější bundy. Opačným problémem trpí štíhlejší muži: příliš velká rukavice lépe nehřeje, protože vzduch uvnitř cirkuluje a prsty nedosáhnou do špiček. V takovém případě může být lepší unisex nebo menší pánská velikost.</p>'
          + T(['Vlastnost', 'Pánský střih', 'Na co dát pozor'], [
              ['Šířka dlaně', 'širší, rovnější', 'u štíhlé ruky zvolte menší velikost'],
              ['Délka prstů', 'delší', 'konečky se mají dotýkat špiček, nikoli se mačkat'],
              ['Zápěstí a manžeta', 'širší, přes bundu', 'musí jít dotáhnout, aby nepouštěla sníh'],
              ['Rozsah velikostí', 'většinou od M do XXL', 'u velikostí nad XL je výběr užší'],
              ['Kůže na dlani', 'častěji zesílená', 'dobrý úchop hole a odolnost proti otěru']]) +
          '<p>Pánské rukavice se označují jako pánské, ale některé výrobní řady jsou unisex a sedí oběma pohlavím. Čtěte proto tabulku velikostí, ne jen štítek.</p>'
          '<h2>Velikost podle obvodu dlaně</h2>'
          '<p>Základem je obvod dlaně změřený kolem kloubů čtyř prstů bez palce. Metr nebo krejčovský pásek stačí. Výsledek v centimetrech se porovná s tabulkou výrobce; často se zaokrouhluje na palce. Pokud jste mezi velikostmi, rozhoduje typ rukavice: u hřejivé vyplněné rukavice zvolte raději větší, aby izolace nebyla stlačená, u tenké prstové menší, aby seděla jako druhá kůže.</p>'
          + T(['Obvod dlaně', 'Velikost', 'Poznámka'], [
              ['cca 20–21 cm', 'S', 'štíhlejší pánská ruka'],
              ['cca 22–23 cm', 'M', 'nejčastější pro menší muže'],
              ['cca 23–25 cm', 'L', 'střední až širší dlaň'],
              ['cca 25–26 cm', 'XL', 'větší a širší ruka'],
              ['nad 26 cm', 'XXL', 'tabulky ověřte, výběr bývá užší']]) +
          '<p>Hodnoty jsou jen orientační, protože se mezi značkami liší. Pro přesnost se vyplatí podívat se na tabulku konkrétního výrobce, například <a href="/znacka/viking/">Viking</a>, <a href="/znacka/rossignol/">Rossignol</a> nebo <a href="/znacka/ziener/">Ziener</a>, kde bývají přesnější než univerzální rady.</p>'
          '<h2>Kůže, nebo syntetika</h2>'
          '<p>Kožené rukavice jsou odolné, dobře drží hůl a časem se přizpůsobí ruce. Vyžadují ale impregnaci a po promoknutí pomalu schnou. Syntetické materiály jsou lehčí, rychleji schnou a snášejí vlhko bez péče, ale dlaň se rychleji obrousí. Kombinace obojího je nejčastější: kůže na dlani a prstech, syntetika na hřbetu. Součástí kategorie jsou i modely s vlastností Kůže, kdy kůže tvoří vnější vrstvu, a modely softshellové, které jsou prodyšnější a vhodnější pro aktivní pohyb než pro stání ve frontě.</p>'
          '<h2>Gore-Tex, membrána a izolace</h2>'
          '<p>Značka membrány Gore-Tex patří mezi nejznámější způsoby, jak zabránit promoknutí a přitom nezadržovat pot. U pánských rukavic se vyskytuje častěji než u levnějších dětských modelů. Samotná membrána ale nehřeje, od mrazu chrání izolace uvnitř. Syntetická výplň, například typu PrimaLoft, se nezhroutí při navlhnutí; peří je lehčí a teplejší, ale potřebuje suché prostředí. Vyhřívané rukavice s baterií řeší extrémní mráz, mají však vyšší hmotnost a vyžadují nabíjení.</p>'
          '<ul><li><strong>Teplý den, aktivní jízda:</strong> tenčí prstová rukavice, případně softshell.</li>'
          '<li><strong>Mráz a vítr:</strong> rukavice s membránou a silnou izolací nebo palčáky.</li>'
          '<li><strong>Mokrý sníh a jaro:</strong> syntetická izolace, vodotěsná membrána, delší manžeta.</li>'
          '<li><strong>Dlouhé čekání na lanovku:</strong> palčáky s vložkou nebo chemický ohřívač do kapsy.</li></ul>'
          '<h2>Sjezd, skialp a běžky: tři různé potřeby</h2>'
          '<p>Rukavice pro sjezd musí vydržet statické stání i prudké pády, mít zesílenou dlaň a dobře chránit palec, který se při pádu nejčastěji zraní. Skialpinista při stoupání se potí, proto potřebuje tenčí a prodyšnou rukavici a na sjezd si bere druhý, teplejší pár; viz kategorie <a href="/skialpinismus/">skialpinismus</a>. Snowboardista nosí rukavice delší, často s chrániči zápěstí, protože při pádech na ruce dopadá častěji než lyžař. Běžkař potřebuje lehkou rukavici s dobrým citem pro hůlky, jak ukazují modely značky <a href="/znacka/leki/">Leki</a>. U pánského výběru proto sledujte i označení, pro jaký sport je rukavice určena, a ne jen to, že je zimní.</p>'
          '<h2>Prstové, nebo palčáky</h2>'
          '<p>Muži častěji volí prstové rukavice, protože potřebují cit pro zip, mobil a připínání přilby. Palčáky jsou teplejší, protože prsty sdílejí teplo, a jsou vhodnější pro lidi, kterým rychle mrznou ruce, nebo pro mrazivé dny. Praktickým kompromisem jsou rukavice s oddělitelným vnitřkem. Pokud lyžujete v proměnlivém počasí, může se hodit sada dvou: tenká rukavice a objemný vnější palčák.</p>'
          '<h2>Značky v pánském výběru</h2>'
          '<p>Mezi pánskými rukavicemi jsou nejvíc zastoupeny značky <a href="/znacka/viking/">Viking</a> a <a href="/znacka/rossignol/">Rossignol</a>, dále <a href="/znacka/ziener/">Ziener</a>, <a href="/znacka/roeckl/">Roeckl</a>, <a href="/znacka/leki/">Leki</a>, <a href="/znacka/level/">Level</a>, <a href="/znacka/dare2b/">Dare2b</a>, <a href="/znacka/reusch/">Reusch</a>, <a href="/znacka/cairn/">Cairn</a> a <a href="/znacka/oakley/">Oakley</a>. Každá má trochu jiný střih, a proto stejné číslo velikosti nemusí odpovídat. Viking a Rossignol se zaměřují na univerzální lyžařské a outdoorové rukavice, Roeckl a Ziener mají dlouhou tradici v rukavicích, Leki je spojen s holemi a běžeckým lyžováním. Při srovnání dvou značek vždy porovnejte materiál, membránu a izolaci, ne jen jméno.</p>'
          '<h2>Vrstvení: rukavice v systému oblečení</h2>'
          '<p>Ruce se zahřejí lépe, pokud je zahřeje celé tělo. Dobře zateplené tělo posílá krev do končetin, zatímco prochladlé ji stahuje do středu. Proto se vyplatí kombinovat rukavice s kvalitní <a href="/lyzarske-bundy/">lyžařskou bundou</a>, termoprádlem a <a href="/lyzarske-cepice-a-nakrcniky/">čepicí nebo nákrčníkem</a>. Rukáv bundy se přetahuje přes manžetu rukavice, nebo naopak rukavice leze přes rukáv; rozhodujte se podle sněhu a stylu lyžování. V hlubším prašanu je výhodnější dlouhá manžeta přes rukáv, na upravené sjezdovce stačí zasunout rukavici pod rukáv.</p>'
          '<h2>Co se děje s rukama při lyžování</h2>'
          '<p>Při sjezdu je ruka v pevném sevření, což zpomaluje prokrvení, a zároveň ji ofukuje protivítr. Mokrá rukavice chladí mnohem rychleji než suchá, protože voda odvádí teplo. Pot je druhý důvod, proč rukavice nehřeje: příliš silná rukavice při usilovném pohybu zapotí ruku, a ta pak v klidu zmrzne. Proto má smysl vybírat podle intenzity pohybu, ne podle nejsilnější vrstvy v nabídce.</p>'
          '<h2>Rezerva a příslušenství</h2>'
          '<p>Zkušení lyžaři nosí druhý pár rukavic, nejlépe tenký, který se vloží do batohu. Mokré rukavice neohřejí nic a výměna za suché je rychlejší než čekání v bufetu. Užitečné jsou i chemické ohřívače, které se vkládají na hřbet ruky, nebo vložky s fleecem pro mrazivé dny. K výbavě patří i další doplňky z kategorie <a href="/lyzarske-doplnky/">lyžařské hole a doplňky</a>, kde najdete poutka a úchyty.</p>'
          '<h2>Péče a zimní provoz</h2>'
          '<p>Mokré rukavice sušte při pokojové teplotě, ne na radiátoru, protože vysoká teplota poškozuje kůži, lepené švy i membránu. Vnitřní vložku vyndejte, aby uschla zvlášť. Kůži občas natřete impregnací a syntetiku postříkejte vodoodpudivým sprejem. Před sezónou otestujte zipy, suché zipy a poutka na zápěstí; ztracená rukavice na lanovce je obyčejná, ale nepříjemná situace, proti které pomáhá zápěstní pásek.</p>'
          '<ol><li>Změřte obvod dlaně a porovnejte s tabulkou výrobce.</li>'
          '<li>Rozhodněte, zda potřebujete prsty, nebo palčáky.</li>'
          '<li>Vyberte podle počasí membránu a izolaci.</li>'
          '<li>Zkontrolujte délku manžety vzhledem k bundě.</li>'
          '<li>Porovnejte nabídky obchodů a velikosti skladem.</li></ol>',
    faq=[
        ('Jak změřit velikost pánských lyžařských rukavic?', 'Změřte obvod dlaně kolem kloubů čtyř prstů bez palce a výsledek porovnejte s tabulkou výrobce. Konečky prstů se mají dotýkat špiček rukavice, ale nesmí být stlačené. Mezi dvěma velikostmi volte větší u silně vyplněných rukavic a menší u tenkých.'),
        ('Jsou lepší prstové rukavice, nebo palčáky?', 'Záleží na tom, co od rukavice čekáte. Prstové dávají cit a úchop, palčáky jsou při stejné izolaci teplejší. Pro mrazivé dny a lidi s chladnýma rukama jsou lepší palčáky, pro aktivní lyžování a práci se zipy prstové.'),
        ('Je Gore-Tex v rukavicích nutný?', 'Nutný není, ale chrání před promoknutím a zároveň odvádí pot. Existují i jiné membrány a kvalitní vodoodpudivé materiály, které stačí na suchý sníh. Na mokrý jarní sníh a delší dny na svahu je membrána praktičtější než pouhá impregnace.'),
        ('Kůže, nebo syntetika?', 'Kůže je odolnější a dobře drží hůl, ale vyžaduje péči a pomalu schne. Syntetika je lehčí a schne rychleji, hůř snáší oděr. Většina rukavic kombinuje kůži na dlani a syntetiku na hřbetu, což je dobrý kompromis.'),
        ('Čím se liší rukavice na sjezd a na běžky?', 'Sjezdové rukavice jsou silnější, mají zesílenou dlaň a chrání při pádu. Běžkařské jsou tenčí, prodyšné a mají větší citlivost pro hůlky, protože při pohybu se hodně potíte. Do sjezdu bývají běžecké rukavice málo teplé.'),
        ('Mohu používat dámské rukavice, pokud mám užší ruku?', 'Pokud máte štíhlou ruku, může vám dámská nebo unisex velikost sedět líp než pánské M. Rozhodující je obvod dlaně a délka prstů. Vyzkoušejte, zda se prsty dotýkají špiček a zda manžeta pasuje k bundě.'),
        ('Jak dlouhá má být manžeta?', 'Dlouhá manžeta se natahuje přes rukáv a chrání před sněhem, hodí se pro hlubší sníh a snowboard. Krátká se schová pod rukáv a je pohodlná na sjezdovce. Důležitější než délka je možnost ji dotáhnout stahovačem nebo suchým zipem.'),
        ('Jak sušit lyžařské rukavice?', 'Při pokojové teplotě, vložku vyndejte zvlášť a nepokládejte je přímo na radiátor. Vysoká teplota poškozuje kůži, lepené švy i membránu. Rukavice sušte hned po použití, aby se nehromadil pach a vlhkost.'),
        ('Vyplatí se vyhřívané rukavice?', 'Pro lidi, kterým ruce mrznou i v dobrých rukavicích, nebo pro velmi mrazivé podmínky ano. Mají ale vyšší hmotnost a vyžadují nabíjení baterií. Pro běžné lyžování obvykle stačí kvalitní palčáky s dobrou izolací a chemický ohřívač do kapsy.'),
        ('Kde porovnat pánské lyžařské rukavice?', 'U každého produktu vidíte nabídky obchodů vedle sebe, včetně dopravy a velikostí skladem. U rukavic je důležité ověřit, zda je právě vaše velikost dostupná, protože výběr v největších velikostech bývá menší než ve středních.'),
    ])

# ------------------------------------------------------------------ horska-kola-vyprodej
NEW['horska-kola-vyprodej'] = dict(
    title='Horská kola výprodej: jak poznat skutečnou slevu',
    desc='Horská kola ve slevě: kdy se vyprodává, jak ověřit skutečnou slevu, na co dát pozor u starších modelů a velikostí a co zkontrolovat před nákupem.',
    intro='<p>Horské kolo ve slevě může být výhodná koupě, ale také pasti: starší ročník, nevhodná velikost rámu nebo záměrně navýšená původní cena. Výprodej se obvykle týká modelů, které obchod chce uvolnit před příchodem nové sezóny, a právě tento okamžik dává smysl využít. '
          'Stránka sbírá kola z kategorie <a href="/horska-kola/">horská kola</a>, u kterých obchody uvádějí slevu. Průvodce vysvětluje, kdy se kola vyprodávají, jak ověřit slevu srovnáním obchodů a jaké vlastnosti nesmíte přehlédnout u kola z předchozí sezóny. Podíváte se na <a href="/celoodpruzena-horska-kola/">celoodpružená</a> modely, <a href="/fatbiky/">fatbiky</a> a také <a href="/horska-kola-trek/">Trek</a> a <a href="/author-horska-kola/">Author</a>. Zmíněna je i velikost rámu, protože právě ta rozhoduje o tom, zda se sleva vyplatí, a také doplňky, které by se v rozpočtu neměly ztratit.</p>',
    guide='<h2>Kdy se horská kola vyprodávají</h2>'
          '<p>Cyklistický rok má jasný rytmus. Nové modely se představují na přelomu léta a podzimu, kdy se začíná prodávat další ročník. Obchody se pak zbavují kol ze starší sezóny, aby uvolnily sklad. Druhá vlna přichází po zimě, před jarní sezónou, kdy se čistí zbytky velikostí. Nejlepší výběr bývá na začátku výprodeje, nejhlubší slevy ale přicházejí později, kdy zbývá málo velikostí.</p>'
          + T(['Období', 'Co se děje', 'Co to znamená pro kupce'], [
              ['Konec léta a podzim', 'výrobci představují nový ročník', 'starší modely zlevňují, výběr velikostí je ještě široký'],
              ['Zima', 'nízká poptávka, plné sklady', 'možnost vyjednat slevu, rychlé dodání méně jisté'],
              ['Předjaří', 'doprodej zbytků', 'největší slevy, ale zbývají krajní velikosti'],
              ['Sezóna', 'plná poptávka', 'slevy bývají menší a krátké'],
              ['Akční dny a výprodeje obchodů', 'plošné snížení cen', 'nutné ověřit původní cenu a ročník']]) +
          '<p>Praktické pravidlo: pokud hledáte konkrétní velikost, je lepší koupit na začátku výprodeje; pokud je pro vás rozhodující cena a velikost není problém, čekejte na poslední slevy.</p>'
          '<h2>Jak poznat skutečnou slevu</h2>'
          '<p>Procento slevy samo o sobě nic neříká. Důležité je, vůči čemu se počítá. Některé obchody uvádějí jako původní cenu doporučenou cenu výrobce, kterou kolo reálně nikdy nestálo, a jiné cenu z doby před navýšením. Nejjistější metodou je srovnat jeden model napříč více obchody. Pokud kolo stojí podobně ve všech a jeden obchod ho nabízí o desítky procent levněji, je sleva reálná. Pokud všechny obchody mají podobnou „zlevněnou“ cenu, jde o standardní ceník a procento je marketing.</p>'
          '<ul><li><strong>Porovnejte více obchodů:</strong> srovnávač vám ukáže stejný model vedle sebe.</li>'
          '<li><strong>Zkontrolujte ročník:</strong> model z loňska má jiné součástky než letošní.</li>'
          '<li><strong>Ověřte skladem:</strong> sleva na nedostupnou velikost nemá cenu.</li>'
          '<li><strong>Čtěte specifikaci:</strong> výbava se mezi ročníky mění, i když název zůstává.</li>'
          '<li><strong>Sledujte dopravu:</strong> velký balík stojí víc a špatně se vrací.</li></ul>'
          '<h2>Starší ročník: výhoda, nebo nevýhoda</h2>'
          '<p>Kolo z minulé sezóny bývá rozumná volba. Rám a základní geometrie se mění pomalu, takže rozdíl proti novému modelu často tvoří barva a drobná změna součástek. Pozor ale na standardy, které se vyvíjejí: osa zadního kola, průměr kol, délka zdvihu vidlice nebo způsob vedení lanek. Starší kolo může mít jiný standard a při výměně součástek hledáte kompatibilní náhrady. Dnes převládá velikost kol 29 palců, menší rámy často používají 27,5 palce, a je dobré vědět, který rozměr kolo má.</p>'
          '<h2>Velikost rámu rozhoduje víc než sleva</h2>'
          '<p>Nejhorší koupě je kolo ve správné ceně a špatné velikosti. Pokud je rám příliš velký, nedosáhnete pohodlně na řídítka a brzdy; pokud malý, budete mít kolena u hrudi. Velikost rámu a výšku postavy ukazuje tabulka výrobce, kterou najdete u produktu. Nezáleží jen na centimetrech, ale i na délce rámu, která se mezi značkami liší. Mezi kusy ve výprodeji jsou často nejméně žádané velikosti, a proto se tam vyskytují krajní hodnoty, jako XS a XXL, které pasují malé skupině lidí.</p>'
          '<h2>Typy kol ve slevě</h2>'
          '<p>Na výprodeji najdete různé typy. Hardtail je nejčastější a nejméně náročný na údržbu. <a href="/celoodpruzena-horska-kola/">Celoodpružená kola</a> mají víc pohyblivých částí a při koupi staršího kusu je dobré zjistit stav ložisek a tlumiče. Dámské a juniorské modely jsou menší, často 26 nebo 27,5 palce. Fatbiky jsou sezónní zboží a v létě se prodávají se slevou, protože poptávka klesá. Elektrokola mají vlastní kategorii, viz <a href="/horska-elektrokola/">horská elektrokola</a>, a baterie se mezi ročníky liší.</p>'
          '<h2>Značky ve výprodeji</h2>'
          '<p>V nabídce s přeškrtnutou cenou se opakují značky <a href="/znacka/specialized/">Specialized</a>, <a href="/znacka/davi/">Davi</a> a <a href="/znacka/olpran/">Olpran</a>, vedle nich i <a href="/znacka/trek/">Trek</a>, <a href="/znacka/author/">Author</a> či <a href="/znacka/kellys/">Kellys</a>. Značky vyšší třídy často zlevňují modely s karbonovým rámem a elektronickým řazením z minulého ročníku, česká výrobní kola zase kompletní základní řady. Při srovnávání dvou značek se dívejte na komponenty, ne na logo: typ přehazovačky, brzd, vidlice a materiál rámu jsou rozhodující.</p>'
          '<h2>Co zkontrolovat u kola z výprodeje</h2>'
          '<ol><li>Rok výroby a specifikaci komponent.</li>'
          '<li>Velikost rámu a doporučenou výšku postavy.</li>'
          '<li>Typ brzd, zda jsou kotoučové, a stav kotoučů.</li>'
          '<li>Vidlici: zdvih, způsob odpružení a možnost uzamčení.</li>'
          '<li>Zda je kolo nové, nebo vystavené či vrácené zboží.</li>'
          '<li>Záruku a podmínky vrácení u prodejce.</li></ol>'
          '<h2>Co dokoupit k novému kolu</h2>'
          '<p>Základem je přilba, viz <a href="/cyklisticke-helmy/">cyklistické helmy</a> a vedle nich <a href="/mtb-a-integralni-helmy/">MTB helmy</a> pro náročnější terén. Dále se vyplatí zámek, světla, pumpa a základní nářadí. Pokud kolo nemá pedály, najdete je v kategorii <a href="/cyklo-pedaly/">pedály</a>. Slevu na kolo je rozumné nepromrhat na zbytečnostech: spíš investujte do kvalitní přilby a servisu před první sezónou.</p>'
          '<h2>Rozpočet: co všechno kolo stojí kromě kola</h2>'
          '<p>Rozumný plán počítá s tím, že kolo je jen začátek. Přilba, zámek, světla, pumpa, nářadí a první servis dohromady tvoří znatelnou část nákladu, a když ji nezapočítáte, sleva se rychle rozpustí. Pokud kupujete kolo pro dospívajícího, uvažujte i o tom, že za dvě sezóny vyroste. Pro mladší děti jsou <a href="/detska-kola-24-palcu/">dětská kola 24 palců</a> mezistupněm před 26 a 27,5 palcem. Dámské modely najdete v kategorii <a href="/damska-kola/">dámská kola</a>.</p>'
          '<h2>Vidlice, brzdy a pohon v nižších a vyšších třídách</h2>'
          '<p>Cena kola se rozděluje zhruba mezi rám, vidlici, pohon a brzdy. U levnějších kol se šetří na vidlici, často pružinové s menší tuhostí, a na brzdách; u dražších je rozdíl v lehčím rámu, vzduchové vidlici a kvalitnějším pohonu. Hydraulické kotoučové brzdy mají lepší dávkování než mechanické a v mokru se snáz drží. Pro rekreační jízdu vybírejte vidlici podle zdvihu a nastavení a pohon podle toho, zda potřebujete lehké převody do kopce. Díly najdete v kategoriích <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a> a <a href="/cyklo-brzdy/">brzdy</a>.</p>'
          '<h2>Jak nenaletět na hmotnost a marketing</h2>'
          '<p>Hmotnost kola v popisu bývá uvedena u konkrétní velikosti, často bez pedálů. Dvě kola s podobnou hmotností se mohou lišit v kvalitě komponent; naopak těžší kolo s lepšími součástkami může být lepší koupě. Podívejte se na značky komponent, na to, zda jde o hliníkový, nebo karbonový rám, a na počet rychlostí. Více převodů neznamená lepší kolo, ale širší rozsah, a ten se vyplatí jen tehdy, když opravdu stoupáte do kopců.</p>'
          '<h2>První servis a záruka</h2>'
          '<p>Kolo z e-shopu se často dodává složené jen zčásti. Před první jízdou je potřeba zkontrolovat dotažení šroubů, tlak v plášťích, seřízení brzd a řazení. Pokud tyto práce nezvládáte, nechte si je udělat v servisu a počítejte s tím do rozpočtu. Záruka se obvykle vztahuje na rám a základní součásti, ale ne na opotřebení, jako jsou pláště, řetěz a brzdové destičky.</p>',
    faq=[
        ('Kdy je nejlepší doba na nákup horského kola ve slevě?', 'Nejširší výběr bývá na konci léta a na podzim, kdy výrobci přicházejí s novými modely. Nejhlubší slevy přicházejí v předjaří, ale zůstávají hlavně krajní velikosti. Pokud potřebujete konkrétní rám, kupujte na začátku výprodeje.'),
        ('Jak poznám, že je sleva skutečná?', 'Porovnejte stejný model ve více obchodech. Pokud ostatní prodávají za podobnou cenu a jeden nabízí výrazně méně, sleva je reálná. Jestliže mají všechny stejnou zlevněnou cenu, procento je jen marketing a nic neušetříte.'),
        ('Je kolo z minulé sezóny horší než nové?', 'Obvykle ne. Rám i geometrie se mění pomalu, rozdíl tvoří barva a drobné změny v komponentech. Ověřte standardy, jako je osa kola nebo typ vidlice, a podívejte se na specifikaci, zda odpovídá vašim potřebám.'),
        ('Co když je v nabídce jen krajní velikost?', 'Neváhejte, zda se vám vejde. Pokud nejste na hranici, bývá lepší počkat na jiný kus než koupit kolo, které nesedí. Nesprávná velikost způsobuje bolest zad, ramen a kolen a žádná sleva ji nevyrovná.'),
        ('Mám koupit hardtail, nebo celoodpružené kolo ve slevě?', 'Pro většinu jezdců je lepší hardtail: je lehčí, jednodušší a levnější na údržbu. Celoodpružené kolo se vyplatí pro technický terén a delší sjezdy, ale u staršího kusu zkontrolujte stav tlumiče a ložisek.'),
        ('Dají se výprodejová kola vrátit?', 'Při nákupu na dálku máte obvykle právo odstoupit od smlouvy ve stanovené lhůtě, pokud kolo nepoužíváte. Podmínky určuje obchod, proto si je přečtěte předem. Velký balík se hůř vrací, takže ověřte dopravu a náklady na zpětný odvoz.'),
        ('Je kolo ve výprodeji nové?', 'Většinou ano, jde o nová kola z minulé sezóny. Někdy se ale nabízí vystavený nebo vrácený kus. Informace bývá v popisu, a pokud ne, zeptejte se obchodu. U vystaveného kusu se může změnit záruka nebo stav lakování.'),
        ('Na co si dát pozor u levných kol z nepoznané značky?', 'Hledejte kotoučové brzdy, kvalitní vidlici a rozumnou hmotnost. Velmi levná kola mívají těžký rám a základní součástky, které rychle selhávají. Spíš než nejnižší cenu hledejte rozumný poměr kvality a ověřené značky.'),
        ('Je sleva na elektrokola stejná jako na klasická?', 'Ne. Elektrokolo má baterii, která stárne i bez použití, takže ročník je důležitější než u klasického kola. Ověřte stáří baterie a dostupnost náhradních dílů. Na klasické horské kolo se stáří projevuje méně.'),
        ('Co zkontrolovat po doručení?', 'Zkontrolujte rám a lak, dotažení šroubů, tlak v pláštích, brzdy a řazení. Pokud něco nesedí, reklamujte hned. Před první jízdou doporučujeme servis, zvlášť u kol, která přišla zčásti složená.'),
    ])
