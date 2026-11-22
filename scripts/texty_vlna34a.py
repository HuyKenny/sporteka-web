"""sporteka.cz — wave 34a (22. 11. 2026): long texts for the new categories ortezy-na-zapesti and ortezy-na-loket.
General information only, no prices, no product counts, no medical promises. Brands named from the catalogue
(wrist: GymBeam, MadMax, Power System, Spokey, HMS, Avento, 4Fizjo, Thuasne; elbow: Spokey, HMS, GymBeam, Thuasne,
4Fizjo, Power System, DBX Bushido). Brand links only for slugs in scripts/znacky_slugy.txt.
Left out (not verifiable): specific models, size tables, clinical efficacy claims, wear-time prescriptions.
"""
from texty_vlna1a import T

NEW = {}

# ------------------------------------------------------------------ ortezy-na-zapesti
NEW['ortezy-na-zapesti'] = dict(long=True,
    title='Ortézy a bandáže na zápěstí – gym i dlahové',
    desc='Ortézy a bandáže na zápěstí: elastické, neoprenové, s pásky na suchý zip i dlahové. Jak změřit velikost a kdy k lékaři. Porovnejte nabídky obchodů.',
    intro='<p><strong>Ortéza nebo bandáž na zápěstí</strong> je návlek, páska nebo pevnější pomůcka, která zápěstí obepne, zahřeje a omezí jeho krajní pohyby. Zápěstí je malý kloub složený z mnoha kůstek a při tlaku, kliku, shybu nebo úderu ho zatěžuje celá horní polovina těla. Proto po ortézách sahají lidé ve fitku, ale také hráči tenisu a padelu, horolezci, cyklisté nebo ti, kdo zápěstí zatěžují při práci u počítače.</p>'
          '<p>V kategorii najdete elastické a neoprenové bandáže, tahové pásky na zvedání činek, ortézy s upínacími pásky na suchý zip i pevné modely s dlahou. Nabízejí je značky jako <a href="/znacka/gymbeam/">GymBeam</a>, <a href="/znacka/madmax/">MadMax</a>, <a href="/znacka/power-system/">Power System</a>, <a href="/znacka/spokey/">Spokey</a>, <a href="/znacka/hms/">HMS</a>, <a href="/znacka/avento/">Avento</a>, <a href="/znacka/4fizjo/">4Fizjo</a> nebo <a href="/znacka/thuasne/">Thuasne</a>. U každého produktu uvidíte nabídky českých e-shopů. Pomůcky pro další klouby jsou v nadřazené kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>',
    guide='<h2>K čemu zápěstní ortéza slouží a k čemu ne</h2>'
          '<p>Bandáž zápěstí dělá tři věci. Stlačuje měkké tkáně kolem kloubu, takže vzniká pocit opory. Udržuje teplo, které mnoho lidí vnímá jako příjemné při ztuhlosti. A u pevnějších typů omezuje ohnutí a vyklonění ruky do krajní polohy. Žádná z těchto vlastností nic neléčí. Ortéza není náhradou za vyšetření a nezaručí, že se zápěstí zotaví nebo že se potíže nevrátí. Berte ji jako pomocníka při zátěži nebo jako opatrnou podporu, o které se vyplatí promluvit s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Typy ortéz a bandáží na zápěstí</h2>'
          + T(['Typ', 'Jak vypadá', 'Kde se používá'], [
              ['Elastická bandáž', 'tkaný nebo pletený návlek bez zpevnění', 'lehká opora, zahřátí, běžná zátěž'],
              ['Neoprenová bandáž', 'silnější materiál, často s pásem přes dlaň a palec', 'posilování, raketové sporty, aktivní den'],
              ['Tahové pásky (wrist wraps)', 'dlouhý pás se smyčkou na palec a suchým zipem', 'tlaky a zvedání činky, trénink s velkou zátěží'],
              ['Ortéza s upínacími pásky', 'návlek s pásky na suchý zip, které lze dotáhnout', 'nastavitelná fixace, delší zátěž'],
              ['Dlahová ortéza', 'pevná nebo polopevná dlaha na dlani nebo hřbetu ruky', 'omezení pohybu, doporučení lékaře']]) +
          '<p>Elastické bandáže jsou nejlehčí a nejpohodlnější. Tvar zápěstí kopírují, ale pevnou oporu nedají. Hodí se, když chcete kloub jen zahřát a mít z něj pocit jistoty, třeba při delším sezení u klávesnice nebo na turistice s holemi. Neoprenové modely drží lépe a udrží teplo, hůř ale prodýchávají, takže se v nich ruka potí. Často mají zesílenou část na palec nebo dlaň.</p>'
          '<p>Tahové pásky, které v angličtině najdete jako wrist wraps nebo lifting wraps, jsou věc posilovny. Dlouhý popruh se jednou omotá kolem zápěstí, smyčka drží palec a suchý zip zajistí konec. Při tlaku nad hlavou, benchpressu nebo dřepu s činkou na zádech brání prohnutí zápěstí dozadu a pomáhá držet kloub v ose předloktí. Nabízejí je GymBeam, MadMax, Power System i další. Nejde o zdravotnickou pomůcku, ale o sportovní doplněk, a funkčně má s dlahou málo společného.</p>'
          '<p>Dlahové ortézy mají pevný nebo polopevný prvek, nejčastěji kovovou či plastovou lištu, která vede po dlani, hřbetu ruky nebo po obou stranách. Slouží k tomu, aby zápěstí zůstalo v určité poloze. V lékárnách a zdravotnických obchodech je najdete od značek jako Thuasne. Takovou ortézu obvykle doporučuje lékař po úrazu nebo při potížích spojených s tlakem na nerv v zápěstí, tedy s tím, čemu se říká syndrom karpálního tunelu. Rozhodně ji nevybírejte jen podle obrázku. Typ dlahy, polohu zápěstí i dobu nošení určuje odborník a výrobce uvádí podrobnosti v návodu.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Většina výrobců určuje velikost podle obvodu zápěstí, u některých modelů také podle obvodu dlaně. Změřte krejčovským metrem nebo proužkem papíru místo, kde nosíte hodinky, těsně nad výstupkem kosti zápěstí. Papír pak přiložte k pravítku. Měřte hodnotu bez stahování, ruka je při měření uvolněná. Velikostní tabulka u každé značky vypadá jinak, takže S od jedné značky může být M od jiné. Spoléhejte vždy na tabulku v popisu konkrétního produktu, ne na písmeno.</p>'
          '<p>Pokud se pohybujete na hranici dvou velikostí, rozhodněte podle účelu. Na sportovní zátěž s neoprenem je lepší pevnější sevření, u elastické bandáže na delší nošení naopak volnější velikost. Tahové pásky a ortézy s upínacími pásky velikost částečně vyrovnají, protože jejich těsnost nastavíte suchým zipem.</p>'
          '<h2>Levá, pravá, nebo univerzální</h2>'
          '<p>Před koupí si proto přečtěte popis. Jednoduché návleky a tahové pásky jsou většinou univerzální, nosí se na obou rukou. Ortézy s dlahou se naopak dělají na levou a pravou ruku zvlášť, protože se tvar dlahy a vyříznutí pro palec liší. U těchto modelů zkontrolujte v popisu, pro kterou ruku jsou určené. Pokud model nabízí obě varianty, vybírejte podle ruky, kterou chcete podepřít, ne podle ruky dominantní.</p>'
          '<h2>Bandáž do posilovny</h2>'
          '<p>Ve fitku se zápěstí zatěžuje hlavně při tlacích, shybech a cvicích s činkou, kdy se zápěstí může prohnout dozadu. Tahové pásky pomáhají držet ho zpevněné, ale nenahradí správnou techniku a rozumnou zátěž. Mnoho trenérů doporučuje je nasazovat jen na nejtěžší série a ostatní práci dělat bez nich, aby se zápěstí a předloktí zpevňovaly přirozeně. Pomůcky pro lepší úchop najdete spolu s dalším vybavením v kategorii <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/cinky-a-kotouce/">činky a kotouče</a>. Pro cvičení na hrazdě pomůže i správná <a href="/sportovni-rukavice/">sportovní rukavice</a>.</p>'
          '<h2>Zápěstí v dalších sportech</h2>'
          '<ul><li><strong>Posilování a crossfit.</strong> Tahové pásky nebo neoprenová bandáž při tlacích a vzpírání, pevnější úchop při shybech.</li>'
          '<li><strong>Tenis a padel.</strong> Zápěstí při úderu snáší rázy a rotaci. Hráči nosí neoprenovou bandáž pro pocit jistoty. Vybavení pro tyto sporty najdete v kategoriích <a href="/tenis/">tenis</a> a <a href="/padel/">padel</a>.</li>'
          '<li><strong>Lezení.</strong> Zápěstí a předloktí při <a href="/horolezectvi/">lezení</a> pracují s velkou silou. Elastická bandáž dává pocit podpory, ale lezce nenahradí odpočinek a postupné zatěžování.</li>'
          '<li><strong>Cyklistika.</strong> Při dlouhém držení řídítek zápěstí trpí zejména ohnutím. Pomůže správné nastavení řídítek a vhodné <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>.</li>'
          '<li><strong>Kancelářská práce.</strong> Lidé, kteří většinu dne pracují s myší a klávesnicí, sahají po lehkých bandážích. Důležitější než bandáž bývá uspořádání pracoviště.</li></ul>'
          '<h2>Kdy ortézu nepoužívat a jít k lékaři</h2>'
          '<p>Zápěstní bandáž není vhodná na všechno. K lékaři nebo fyzioterapeutovi jděte, pokud zápěstí bolí po pádu nebo úderu, je oteklé, zdeformované nebo nejde hýbat. Totéž platí, když pociťujete mravenčení, brnění nebo necitlivost prstů, pokud bolest budí v noci nebo trvá déle než několik týdnů. Pod ortézou se mohou potíže zakrýt a pak se léčí později. Bandáž tedy nikdy nevolte místo vyšetření.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš těsná bandáž. Znamená zpomalené prokrvení, otlaky a mravenčení v prstech. Pokud brní, ihned povolte nebo sundejte.</li>'
          '<li>Špatná velikost podle písmene místo podle tabulky konkrétní značky.</li>'
          '<li>Nošení tahových pásků při každém cviku. Zápěstí pak nemá šanci pracovat samo.</li>'
          '<li>Ortéza s dlahou bez rady odborníka a bez čtení návodu.</li>'
          '<li>Nošení mokré bandáže. Pot a vlhkost dráždí kůži a materiál zapáchá.</li>'
          '<li>Ignorování bolesti v domnění, že ji bandáž „zakryje“.</li></ul>'
          '<h2>Kdy se hodí a kdy ne</h2>'
          '<p>Bandáž dává smysl jako krátkodobá podpora při konkrétní zátěži, například při tréninku, turnaji nebo celodenním výletu. Při každodenním dlouhém nošení se může stát, že si ruka zvykne na oporu a svaly předloktí dostanou méně práce. Proto je rozumné zeptat se fyzioterapeuta, zda a kdy bandáž nosit, a zároveň nezanedbat posilování a protažení předloktí. Pomůcka také nemá nahradit rozcvičku, odpočinek ani úpravu techniky, která zápěstí přetěžuje.</p>'
          '<h2>Péče a praní</h2>'
          '<p>Elastické a neoprenové návleky se obvykle perou ručně ve vlažné vodě s jemným mýdlem a suší se při pokojové teplotě, mimo radiátor a přímé slunce. Teplo materiál zdeformuje a elastika ztratí tah. Před praním zapněte suchý zip, aby nezachytil o textil. Dlahu před praním vyjměte, pokud to výrobce dovoluje. Vždy se řiďte štítkem a návodem od konkrétní značky. Bandáž s pevnou dlahou nikdy nesušte na topení, mohla by se zdeformovat a přestat držet správný tvar.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Stejný typ ortézy se prodává pod řadou názvů. Podívejte se na materiál, šířku pásku, zda je určený na levou, pravou nebo obě ruce, a na velikostní tabulku. Pokud hledáte pomůcku pro jiný kloub, srovnejte také <a href="/ortezy-na-koleno/">ortézy na koleno</a>, <a href="/ortezy-na-kotnik/">ortézy na kotník</a> nebo <a href="/ortezy-na-loket/">ortézy na loket</a>. Na detailu produktu uvidíte nabídky jednotlivých obchodů, nákup dokončíte přímo v e-shopu.</p>',
    faq=[
        ('Jaká ortéza na zápěstí je vhodná do posilovny?', 'Nejčastěji tahové pásky (wrist wraps) nebo neoprenová bandáž s upínacím páskem. Drží zápěstí v ose, ale nenahradí techniku a rozumnou zátěž.'),
        ('Jak změřit velikost ortézy na zápěstí?', 'Změřte metrem obvod zápěstí v místě, kde nosíte hodinky. Pak porovnejte číslo s tabulkou konkrétní značky, velikosti se mezi výrobci liší.'),
        ('Je lepší elastická bandáž, nebo ortéza s dlahou?', 'Elastická je lehká a dává jen mírnou oporu. Dlaha omezuje pohyb a hodí se na doporučení lékaře, třeba po úrazu.'),
        ('Můžu zápěstní bandáž nosit celý den?', 'Délku nošení určuje návod výrobce a váš lékař. Příliš těsná bandáž může brzdit prokrvení, takže při brnění ji povolte.'),
        ('Pomůže ortéza na zápěstí na bolest?', 'Bandáž kloub zahřeje a podepře, léčit ho ale neumí. Pokud bolest trvá, vrátila se nebo vás budí, nechte ji vyšetřit lékařem.'),
        ('Je ortéza na zápěstí na levou i pravou ruku?', 'Jednoduché návleky a tahové pásky jsou obvykle univerzální. Dlahové ortézy bývají zvlášť pro levou a pravou ruku, ověřte to v popisu.'),
        ('Kdy se při potížích se zápěstím obrátit na lékaře?', 'Při bolesti po úrazu, otoku, brnění či necitlivosti prstů, nočních bolestech nebo když potíže trvají déle než pár týdnů.'),
        ('Jak prát ortézu na zápěstí?', 'Většinou ručně ve vlažné vodě s jemným mýdlem a sušit volně mimo topení. Dlahu před praním vyjměte, pokud to výrobce dovoluje.'),
        ('K čemu jsou tahové pásky na zápěstí?', 'Pomáhají při tlacích a těžkých sériích udržet zápěstí zpevněné a neprohnuté. Jsou to sportovní doplněk, ne zdravotnická pomůcka.'),
    ])

# ------------------------------------------------------------------ ortezy-na-loket
NEW['ortezy-na-loket'] = dict(long=True,
    title='Ortézy a bandáže na loket – tenisový loket',
    desc='Ortézy a bandáže na loket: návleky, pásky na tenisový loket, neopren. Jak vybrat velikost a kdy k lékaři. Porovnejte nabídky českých obchodů.',
    intro='<p><strong>Ortéza nebo bandáž na loket</strong> je návlek či pásek, který loketní kloub obepne a zahřeje, nebo kolem předloktí vytvoří tlak. Loket zatěžují údery raketou, tahy při lezení, zvedání činek i práce s myší nebo nářadím. Nejznámější potíž se nazývá tenisový loket (epikondylitida), tedy bolest na zevní straně lokte u úponu šlach předloktí. Postihuje daleko víc lidí než jen tenisty, často třeba ty, kdo celý den opakují stejný pohyb zápěstím.</p>'
          '<p>V kategorii najdete elastické a neoprenové návleky na celý loket, užší pásky na horní část předloktí určené právě pro tenisový nebo golfový loket a pevnější modely se zpevněním. Nabízejí je <a href="/znacka/spokey/">Spokey</a>, <a href="/znacka/hms/">HMS</a>, <a href="/znacka/gymbeam/">GymBeam</a>, <a href="/znacka/thuasne/">Thuasne</a>, <a href="/znacka/4fizjo/">4Fizjo</a>, <a href="/znacka/power-system/">Power System</a> nebo <a href="/znacka/dbx-bushido/">DBX Bushido</a>. U každého produktu uvidíte nabídky českých e-shopů. Pomůcky pro ostatní klouby najdete v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>',
    guide='<h2>Co ortéza na loket dělá a co ne</h2>'
          '<p>Bandáž lokte má tři úkoly. Stlačuje tkáň kolem kloubu a dává pocit opory. Udržuje teplo, které při ztuhlosti mnoho lidí vnímá jako příjemné. A pásek na předloktí rozkládá tah svalů na jiné místo než úpon šlachy, takže zátěž při pohybu je trochu jinak rozložená. Nic z toho loket nevyléčí. Ortéza není náhradou za diagnózu a neslibuje, že potíže zmizí ani že se nevrátí. Je to doplněk, který může pomoci s pohodlím při zátěži, a o dalším postupu rozhoduje lékař nebo fyzioterapeut.</p>'
          '<h2>Typy ortéz a bandáží na loket</h2>'
          + T(['Typ', 'Jak vypadá', 'Pro koho'], [
              ['Elastický návlek', 'tkaná nebo pletená rukávová bandáž přes loket', 'lehká opora a zahřátí při běžné zátěži'],
              ['Neoprenový návlek', 'silnější materiál, někdy s výztuží', 'posilování, raketové sporty, aktivnější zátěž'],
              ['Pásek na tenisový loket', 'užší popruh na horní části předloktí, často s polštářkem', 'opakované pohyby zápěstím a předloktím'],
              ['Ortéza s upínacími pásky', 'návlek s nastavitelnými pásky na suchý zip', 'pevnější fixace a individuální utažení'],
              ['Pevná ortéza s kloubem', 'dlahy po stranách a pohyblivý kloub', 'omezení pohybu na doporučení lékaře']]) +
          '<p>Elastické návleky jsou nejlehčí a pod oblečením skoro nejsou vidět. Opora je mírná, takže se hodí hlavně pro zahřátí a pocit jistoty. Neoprenové modely drží lépe, udrží teplo a často mají zesílení, ale hůř odvádějí pot. V horkém počasí a při delším cvičení proto mnohé lidi tlačí a svědí.</p>'
          '<p>Pásek na tenisový loket je jiný typ pomůcky. Neobepíná kloub, ale nasazuje se na předloktí těsně pod loket a utáhne se přes sval. Tím mění směr přenosu síly do úponu šlach. Anglicky se označuje jako epicondylitis strap nebo tennis elbow band. Na zevní straně lokte bývá polštářek, někdy gelový, který tlačí na sval. Nejlépe se nastavuje u modelů se suchým zipem, kde si míru utažení určíte sami. Odborníci ale upozorňují, že důkazy o jeho účinnosti nejsou jednoznačné a každému nemusí vyhovovat, takže od něj nečekejte zázrak.</p>'
          '<p>Pevné ortézy s kloubem nebo dlahami se používají po úrazech, operacích nebo při nestabilitě kloubu. Dělají je zdravotnické značky, mezi nimi Thuasne. Takovou ortézu doporučuje lékař, který určí její typ, nastavení rozsahu pohybu i dobu nošení. Samostatně a bez rady ji vybírat nelze, spoléhejte se na návod výrobce a odborníka.</p>'
          '<h2>Tenisový a golfový loket</h2>'
          '<p>Tenisový loket (laterální epikondylitida) je bolest na vnější straně lokte, golfový loket (mediální epikondylitida) na vnitřní straně. Oba názvy označují podráždění úponů šlach, které se opakovaně přetěžují při úchopu, rotaci nebo úderu. Potíže se objevují nejen u sportovců, ale také u lidí, kteří celý den pracují s nářadím, myší nebo nosí těžká zavazadla. Vlastní bolest ale nemusí mít stejnou příčinu, a proto je rozumné ji nechat vyšetřit. Bandáž může být jen jedním doplňkem, často spolu s úpravou zátěže a cvičením, které doporučí fyzioterapeut.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Návleky na celý loket se vybírají podle obvodu paže nad loktem, někdy také podle obvodu předloktí. Změřte krejčovským metrem uvolněnou ruku, obvykle několik centimetrů nad a pod kloubem, přesné body najdete v návodu výrobce. U pásku na tenisový loket se měří obvod předloktí v nejsilnějším místě a hodnota se porovná s tabulkou. Velikosti se u značek liší, takže S od jedné značky nemusí odpovídat S od druhé.</p>'
          '<p>Pokud jste mezi velikostmi, rozhodněte podle zátěže. Neoprenový návlek na sport má sedět pevně, ale nesmí tlačit. Elastický návlek na delší nošení raději o něco volnější. Pásky s nastavitelným suchým zipem velikost částečně vyrovnají, protože jejich těsnost doladíte sami.</p>'
          '<h2>Levý, pravý, nebo univerzální</h2>'
          '<p>Před koupí si přečtěte popis produktu. Většina elastických návleků a pásků je univerzální a nosí se na obou rukou. Ortézy s dlahami nebo výztuží někdy bývají dělané zvlášť pro levou a pravou ruku. Údaj najdete v popisu produktu. Pokud je volba, vybírejte podle ruky, kterou chcete podepřít, ne podle ruky dominantní.</p>'
          '<h2>Loket ve sportu</h2>'
          '<ul><li><strong>Tenis, padel, squash.</strong> Údery a rotace zatěžují šlachy předloktí. Správná velikost a vyvážení rakety i technika úderu bývají důležitější než bandáž. Vybavení najdete v kategoriích <a href="/tenis/">tenis</a>, <a href="/padel/">padel</a> a <a href="/tenisove-rakety/">tenisové rakety</a>.</li>'
          '<li><strong>Golf.</strong> Golfový loket bývá spojen s opakovanými švihy. Vybavení a doplňky najdete v kategorii <a href="/golf/">golf</a>.</li>'
          '<li><strong>Posilování a crossfit.</strong> Loket pracuje při shybech, bicepsových zdvizích i tlacích. Neoprenový návlek dává pocit tepla a opory. Cviky a pomůcky jsou v kategoriích <a href="/cinky-a-kotouce/">činky a kotouče</a> a <a href="/hrazdy-a-bradla/">hrazdy a bradla</a>.</li>'
          '<li><strong>Lezení.</strong> Opakované tahy namáhají úpony na předloktí. Elastický návlek nebo pásek může při zátěži pomáhat, odpočinek ani postupné zvyšování zátěže ale nenahradí. Vybavení najdete v <a href="/horolezectvi/">horolezectví</a>.</li>'
          '<li><strong>Cyklistika.</strong> Při dlouhých jízdách s ohnutým loktem se hodí správné nastavení řídítek a <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>.</li>'
          '<li><strong>Práce a každodenní zátěž.</strong> Při dlouhé práci s myší nebo nářadím pomůže spíš úprava pracoviště a přestávky než bandáž sama.</li></ul>'
          '<h2>Kdy k lékaři</h2>'
          '<p>Vyhledejte lékaře nebo fyzioterapeuta, pokud loket bolí po pádu nebo úderu, je oteklý, zarudlý, deformovaný nebo nelze plně natáhnout či ohnout. Totéž platí při mravenčení nebo necitlivosti prstů, při bolesti, která budí v noci, nebo když trvá déle než několik týdnů i při šetření. Bandáž může potíže zakrýt a oddálit správnou péči, takže ji nepoužívejte místo vyšetření.</p>'
          '<h2>Jak správně nasadit</h2>'
          '<p>Návlek natáhněte na pokrčenou ruku tak, aby střed přišel na loket a okraje nikde nepřehýbaly. Pásek na předloktí utáhněte tak, aby pod ním šel provléknout prst, a po nasazení zkuste ruku několikrát ohnout a zatnout pěst. Pokud se objeví brnění, tlak do žil nebo bolest, utažení povolte. Kůže pod ortézou má zůstat suchá a bez otlaků.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš těsný návlek nebo pásek. Způsobí brnění, studené prsty a otlaky. Při prvních příznacích povolte nebo sundejte.</li>'
          '<li>Pásek na tenisový loket nasazený přímo na kloub místo na sval pod ním.</li>'
          '<li>Výběr velikosti podle písmene bez tabulky výrobce.</li>'
          '<li>Spoléhání se na ortézu a pokračování v zátěži, která potíže způsobuje.</li>'
          '<li>Neoprenový návlek na mokré kůži. Pot dráždí kůži a materiál zapáchá.</li>'
          '<li>Svépomocné vybírání pevné ortézy s kloubem bez rady lékaře.</li></ul>'
          '<h2>Kdy se hodí a kdy ne</h2>'
          '<p>Návlek nebo pásek dává smysl jako podpora při konkrétní zátěži, třeba při tréninku, turnaji nebo dni strávenému prací s nářadím. Dlouhodobé nošení bez konzultace není ideální, protože svaly předloktí potřebují pracovat. Zeptejte se fyzioterapeuta, jak pomůcku zařadit, a nezanedbejte úpravu techniky, vhodné vybavení, rozcvičku a odpočinek, které při přetěžování lokte často rozhodují víc než samotná ortéza.</p>'
          '<h2>Péče a praní</h2>'
          '<p>Elastické a neoprenové návleky se většinou perou ručně ve vlažné vodě s jemným mýdlem a suší se volně mimo topení a přímé slunce. Vysoká teplota poškodí elastická vlákna i lepené spoje. Před praním zapněte suchý zip, aby nezachytil o textil. Vždy se řiďte štítkem a návodem konkrétní značky.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Při srovnání sledujte typ pomůcky (návlek, pásek, ortéza), materiál, velikostní tabulku a to, zda je určená na levou, pravou nebo obě ruce. Pokud řešíte jiný kloub, mrkněte také na <a href="/ortezy-na-zapesti/">ortézy na zápěstí</a>, <a href="/ortezy-na-koleno/">ortézy na koleno</a> nebo <a href="/ortezy-na-kotnik/">ortézy na kotník</a>. Při potřebě zahřát a podepřít svaly po zátěži se hodí i <a href="/tejpy/">tejpy</a>. Na detailu produktu uvidíte nabídky obchodů, nákup dokončíte přímo v e-shopu.</p>',
    faq=[
        ('Jaká ortéza na loket je vhodná při tenisovém loktu?', 'Většinou se používá pásek na předloktí pod loktem nebo neoprenový návlek. Na vlastní potíž je rozumné se předem poradit s lékařem nebo fyzioterapeutem.'),
        ('Pomůže ortéza na tenisový loket vyléčit potíže?', 'Ne, bandáž nic neléčí. Může zlepšit pocit opory při zátěži, o léčbě rozhoduje lékař nebo fyzioterapeut.'),
        ('Jak změřit velikost ortézy na loket?', 'Změřte metrem obvod paže nebo předloktí podle návodu výrobce a porovnejte s tabulkou konkrétní značky. Velikosti se mezi značkami liší.'),
        ('Kam se nasazuje pásek na tenisový loket?', 'Na horní část předloktí těsně pod loket, přes sval. Návod výrobce říká přesné místo, pásek nepatří přímo na kloub.'),
        ('Je lepší neoprenový, nebo elastický návlek?', 'Neopren drží pevněji a víc hřeje, hůř ale prodýchává. Elastický je lehčí a pohodlnější na delší nošení, opora je slabší.'),
        ('Kdy se při bolesti lokte obrátit na lékaře?', 'Při bolesti po úrazu, otoku, deformaci, brnění prstů, nočních bolestech nebo když potíže trvají déle než pár týdnů.'),
        ('Můžu ortézu na loket nosit celý den?', 'Délku nošení určuje návod výrobce a lékař. Pokud se objeví brnění, studené prsty nebo otlaky, ortézu povolte nebo sundejte.'),
        ('Je ortéza na loket na levou i pravou ruku?', 'Jednoduché návleky a pásky bývají univerzální. Modely s dlahami mohou být zvlášť pro levou a pravou ruku, ověřte to v popisu.'),
        ('Jak prát ortézu na loket?', 'Většinou ručně ve vlažné vodě s jemným mýdlem a sušit volně mimo radiátor. Řiďte se štítkem od výrobce.'),
    ])
