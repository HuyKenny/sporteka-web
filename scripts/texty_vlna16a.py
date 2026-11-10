"""sporteka.cz — wave 16a (4. 11. 2026): long texts (>= 1650 words) for hokejky, vareni-v-prirode, cyklo-riditka, sipkove-doplnky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ hokejky
NEW['hokejky'] = dict(long=True,
    title='Hokejky: kompozit, dřevo, dětské i seniorské',
    desc='Hokejky pro děti, juniory i dospělé: kompozit, dřevo, flex, zahnutí čepele a délka. Návod na výběr a nabídky českých obchodů vedle sebe.',
    intro='<p>Hokejka je jediná část výstroje, kterou hráč drží v rukou celý zápas, a proto na ní záleží víc než na většině ostatních kousků. '
          'Od ní se odvíjí, jak jistě povedete puk, jak silně vystřelíte a jak rychle se vám unaví zápěstí. V kategorii <strong>hokejky</strong> najdete jednodílné kompozity, '
          'dřevěné hole pro děti i dospělé, dvoudílné sestavy s výměnnou čepelí a také hole na florbal či pozemní hokej, které se na první pohled podobají, ale hrají se jinak.</p>'
          '<p>Sporteka nabídky českých obchodů srovnává u stejného modelu, takže vidíte, kde je daná délka a levá nebo pravá čepel skladem. Ke hře patří také '
          '<a href="/hokejove-cepele-a-nasady/">čepele a násady</a>, <a href="/hokejove-pasky-a-doplnky/">pásky a doplňky</a> a <a href="/hokejove-brusle/">brusle</a>. '
          'Celý obor shrnuje hlavní kategorie <a href="/hokej/">hokej</a>. Níže najdete postup, jak z desítek parametrů vybrat tu správnou hůl.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Hokejky se dělí podle konstrukce, materiálu a velikostní řady. Rozdíly nejsou jen kosmetické, každý typ se hodí pro jiného hráče a jinou fázi vývoje.</p>'
          + T(['Typ', 'Pro koho', 'Hlavní přednost', 'Na co dát pozor'], [
              ['Dřevěná jednodílná', 'děti, začátečníci, hobby hráči', 'odolnost a pevná konstrukce', 'vyšší hmotnost, méně citlivý odpich'],
              ['Kompozitní jednodílná', 'pokročilí a soutěžní hráči', 'nízká váha a pružnost', 'při nárazu na hranu brány či mantinelu praská'],
              ['Dvoudílná (násada a čepel)', 'hráči, kteří chtějí ladit sestavu', 'výměnná čepel, nižší náklady na opravu', 'spoj musí sedět a nesmí se viklat'],
              ['Dětské a minihokejky', 'nejmenší hráči na ledě i na ulici', 'malá váha a krátká délka', 'rychle se z nich vyroste, ale kupovat na vyrůstání se nevyplácí'],
              ['Brankářské hole', 'brankáři', 'široká násada a rozšířená čepel', 'liší se tvarem i vyvážením od hole hráče'],
              ['Florbalové a hokejbalové hole', 'školní a rekreační hra', 'lehkost a krátká čepel', 'na led se nehodí, patří do sálu nebo na asfalt']]) +
          '<p>Pokud hledáte florbalovou hůl, otevřete raději <a href="/florbal/">florbal</a>, kde jsou hole s plastovou čepelí a vlastním značením tuhosti. '
          'Obdobná pravidla platí pro <a href="/pozemni-hokej/">pozemní hokej</a>, jenže tam je hůl zakřivená jen na jedné straně a má jiné rozměry.</p>'
          '<h2>Délka hokejky</h2>'
          '<p>Nejčastější rada zní, že hůl postavená na špičce čepele má při stání na bruslích končit mezi bradou a nosem. Bez bruslí sahá obvykle po bradu. '
          'Kratší hůl dává lepší kontrolu nad pukem a snazší práci v těsném prostoru, delší zase větší dosah a páku při střele. Hráči v obraně často volí o něco delší hole, '
          'útočníci kratší. Velký rozdíl dělá i způsob hry: kdo hodně kličkuje, ocení krátkou, kdo střílí od modré čáry, tu delší. '
          'Prodloužit dřevěnou hůl lze nástavcem, zkrátit ji řezem, ale u kompozitu každé zkrácení mění jeho ohebnost a hůl se po něm chová tužeji.</p>'
          '<h2>Flex neboli tuhost</h2>'
          '<p>Flex udává sílu potřebnou k ohnutí násady o určitou vzdálenost a vyjadřuje se číslem na násadě. Čím vyšší číslo, tím tužší hůl. Orientačně se volí hodnota odpovídající zhruba polovině tělesné hmotnosti hráče v librách (kg × 2,2 ÷ 2), takže při 80 kg vychází flex kolem 85, '
          'což platí hlavně u dospělých. Děti a mladší junioři potřebují hole měkčí, jinak je nedokážou při střele prohnout a ztratí energii. Pokročilí střelci volí o něco tužší hole kvůli rychlejšímu zpětnému výskoku, '
          'zatímco hráči, kteří se opírají o přesnost, preferují měkčí a citlivější hole.</p>'
          + T(['Velikostní řada', 'Typický věk či výška', 'Flex'], [
              ['Mini a dětské', 'nejmenší děti, začátky na ledě', 'velmi měkký, kolem nízkých desítek'],
              ['Youth', 'mladší školní věk', 'měkký'],
              ['Junior', 'starší děti a mladí hráči', 'střední až vyšší podle váhy'],
              ['Intermediate', 'dorost a drobnější dospělí', 'střední až vyšší'],
              ['Senior', 'dospělí hráči', 'široké rozpětí podle síly a stylu']]) +
          '<p>Tabulka je jen orientační. Výrobci mají vlastní značení a mezi řadami se podle modelu překrývá, proto vždy porovnejte údaj na konkrétní holi s vlastní váhou a výškou.</p>'
          '<h2>Zahnutí čepele a levá či pravá ruka</h2>'
          '<p>Čepel hokejky je zakřivená. Zakřivení neboli zahnutí určuje, jak puk vedete a jak vysoko vzlétá při střele. Větší zahnutí usnadňuje zvedání puku, mělčí zahnutí pomáhá s přesnými přihrávkami a střelou po ledě. '
          'Značení vzorů se liší podle výrobce, ale pro začátečníky platí jednoduché pravidlo: začněte středním zahnutím a měňte, až poznáte, co vám chybí.</p>'
          '<p>Levá a pravá hůl se určuje podle toho, která ruka je při držení dole. Kdo drží hůl levou rukou níže, hraje s levou čepelí. Většina hráčů zjistí svou stranu intuitivně, '
          'přesto se vyplatí nechat dítě vyzkoušet obě. Nejčastější chyba u dětí je, že si rodiče zvolí stranu podle psací ruky, ačkoli dítě drží hůl přirozeněji opačně.</p>'
          '<h2>Materiál, váha a vyvážení</h2>'
          '<ul><li><strong>Dřevo</strong> se dělá z vrstvených desek a laminuje se. Je těžší a méně pružné, zato odolné proti nárazům a dobře snáší tréninkový provoz.</li>'
          '<li><strong>Kompozit</strong> z uhlíkových a skleněných vláken je lehký, má rychlý odpich a stabilní chování. Nevýhodou je křehkost čepele a hran při nárazu.</li>'
          '<li><strong>Bodový odpich</strong> znamená, že se hůl nejvíc prohýbá v určité části násady. Nízký bod se hodí pro rychlé zápěstní střely, vysoký pro slapshoty.</li>'
          '<li><strong>Vyvážení</strong> určuje, zda je hůl těžší u čepele, nebo u rukojeti. Lehká hůl s těžším koncem u čepele se vede stabilněji.</li></ul>'
          '<h2>Pro koho jaká hokejka</h2>'
          '<h3>Děti a začátečníci</h3>'
          '<p>Pro první sezóny stačí dřevěná hůl správné délky. Dítě ji nepoškodí tak rychle, dá se snadno ořezat a při pádech nepraskne. Jakmile dítě začne pravidelně trénovat, zvažte lehčí kompozit se správným flexem.</p>'
          '<h3>Pokročilí a soutěžní hráči</h3>'
          '<p>Kdo hraje ligu, bere kompozity se zvolenou zahnutou čepelí a tuhostí vyladěnou podle střelecké techniky. Mnozí si drží dvě až tři stejné hole, aby mohli při zlomení pokračovat bez změny pocitu.</p>'
          '<h3>Rekreační a amatérští hráči</h3>'
          '<p>Hrajete-li jednou týdně rekreačně na večerním ledu, ušetříte u dřevěné nebo základní dvoudílné hole. Výkonový kompozit se vám nevyplatí, protože rozdíl ve výkonu uvidíte až u rychlých a technických střel.</p>'
          '<h3>Brankáři</h3>'
          '<p>Brankářské hole mají zvláštní tvar násady a čepele a pro ně platí jiná pravidla výběru. Doplňující vybavení najdete v <a href="/hokejove-brankarske-vybaveni/">brankářské výstroji</a>.</p>'
          '<h2>Čepele, nástavce a náhrady</h2>'
          '<p>U dvoudílných holí se opotřebovává hlavně čepel. V <a href="/hokejove-cepele-a-nasady/">čepelích a násadách</a> najdete jak samostatné čepele, tak násady, z nichž si můžete složit vlastní kombinaci. '
          'Při koupi dbejte, aby čepel pasovala na stejný systém spojení jako násada. Mezi výrobci se liší tvar zástrčky i délka zapuštění, proto se nedá kombinovat cokoli s čímkoli. '
          'Poškozenou čepel poznáte podle odštípnutých hran, odlupující se vrstvy nebo změklého místa, které při tlaku pruží.</p>'
          '<h2>Páska, vosk a údržba</h2>'
          '<p>Černá nebo bílá páska chrání čepel před poškrábáním a lépe drží puk. Vyměňuje se podle potřeby, u aktivních hráčů i po každém zápase. Rukojeť se obaluje páskou nebo tkanicí, která zabraňuje klouzání v rukavici. '
          'Širší nabídku najdete v kategorii <a href="/hokejove-pasky-a-doplnky/">hokejové pásky, tkaničky a doplňky</a>. '
          'Po tréninku hůl osušte, zejména u dřevěné se voda může dostat pod lamináty. Kompozit nenechávejte přes noc v mrazivém autě, extrémní teplota materiál zbytečně namáhá. '
          'Pravidelně kontrolujte trhliny, hlavně u hrany čepele a v místě spoje.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii nejčastěji narazíte na značky ' + B(('bauer', 'Bauer'), ('winnwell', 'Winnwell'), ('ccm', 'CCM'), ('sherwood', 'Sherwood'), ('balling', 'Balling'), ('freez', 'Freez'), ('fischer', 'Fischer'), ('warrior', 'Warrior'), ('unihoc', 'Unihoc')) + '. '
          'U Bauer, CCM a Warrior převažují kompozity pro různé úrovně. Winnwell a Sherwood jsou známé jako nabídka dostupnějších holí. Fischer, Unihoc a Balling zasahují i do florbalu či minihokeje. Porovnání mezi značkami dělejte podle konkrétní řady, ne podle jména na násadě.</p>'
          '<h2>Co ještě k hokejce patří</h2>'
          '<p>Správná hůl je jen začátek. Chcete-li si složit kompletní výbavu, projděte si <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>, '
          '<a href="/hokejove-chranice/">hokejovou výstroj a chrániče</a>, <a href="/hokejove-dresy-a-obleceni/">dresy a oblečení</a> a <a href="/hokejove-tasky/">tašky a batohy</a>. '
          'Na trénink doma pomohou <a href="/hokejove-puky-a-branky/">puky, branky a tréninkové pomůcky</a>. Sběratele zajímají <a href="/hokejove-suveniry-a-karty/">karty a suvenýry</a>.</p>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li>Příliš dlouhá hůl „na vyrůstání“. Dítě s ní nezvládá techniku a rychle se zničí návyky.</li>'
          '<li>Příliš tuhý flex. Hráč hůl neprohne, střela je slabá a ruce se zbytečně namáhají.</li>'
          '<li>Záměna levé a pravé čepele. Vrácení v obchodě se u zboží vyzkoušeného na ledě nemusí uznat.</li>'
          '<li>Kupovat podle ceny bez ohledu na váhu a vyvážení. Rozdíl pocítíte po první třetině zápasu.</li>'
          '<li>Nezkontrolovat systém spojení u dvoudílné hole a čepele.</li>'
          '<li>Opomenout údržbu: promáčená lamina a prasklá čepel se objeví ve chvíli, kdy ji nejméně potřebujete.</li></ul>'
          '<h2>Jak si hůl vyzkoušet</h2>'
          '<p>Nejlepší zkouška je v obchodě v postoji hráče: lehce pokrčená kolena, hůl před tělem a hlava nad pukem. Zkuste imitovat vedení i střelu, zda se rukojeť nedře o rukavici a zda hůl nepůsobí vpředu příliš těžce. '
          'Při nákupu online si změřte vlastní výšku s bruslemi a porovnejte ji s tabulkou velikostí u konkrétního modelu, protože značení délek se u výrobců liší o několik centimetrů.</p>'
          '<h2>Kdy hokejku kupovat</h2>'
          '<p>Největší výběr velikostí bývá před zahájením sezóny, vzácné velikosti se ale rozeberou dřív než ostatní. Mimo sezónu se hůl nakupuje v klidu a s možností porovnat nabídky několika obchodů. '
          'Sledujte skladovost podle levé nebo pravé strany, protože se prodává nerovnoměrně, a u dětí nechte rezervu jen v délce nástavce, nikoli v celé holi.</p>',
    faq=[('Jak dlouhá má být hokejka?', 'Na bruslích má hůl postavená na špičce končit mezi bradou a nosem, bez bruslí zhruba u brady. Při váhání zvolte kratší, protože se s ní lépe vede puk.'),
         ('Co znamená číslo flexu na hokejce?', 'Číslo udává tuhost násady. Čím je vyšší, tím víc síly je potřeba k ohnutí. U dospělých se obvykle volí hodnota blízká polovině tělesné hmotnosti v librách, tedy při 80 kg zhruba 85.'),
         ('Jak poznám, zda potřebuji levou, nebo pravou hokejku?', 'Podívejte se, kterou rukou držíte hůl níže. Pokud levou, jde o levou čepel. Nejlepší je vyzkoušet obě a vybrat tu, která se drží přirozeněji.'),
         ('Je lepší dřevěná, nebo kompozitová hokejka?', 'Dřevo je odolnější a vhodné pro děti a rekreační hráče. Kompozit je lehčí a pružnější, hodí se pro pravidelné soutěžní hraní, ale vyžaduje šetrné zacházení.'),
         ('Kdy vyměnit čepel hokejky?', 'Když jsou na čepeli trhliny, odštěpené hrany nebo hůl při střele ztrácí pevnost. U dvoudílných hokejek stačí vyměnit čepel, násada zůstává.'),
         ('Jakou hokejku koupit pro dítě?', 'Dětskou dřevěnou nebo základní kompozitovou v odpovídající délce a s měkkým flexem. Nekupujte na vyrůstání, příliš dlouhá hůl zhoršuje techniku.'),
         ('Hodí se florbalová hůl na led?', 'Ne. Florbalová hůl je lehká, plastová a určená pro míček v sále. Na ledě by se rychle zničila a nemá správné rozměry ani čepel.'),
         ('Jak pečovat o hokejku po tréninku?', 'Osušte ji, zejména u dřeva, oklepejte sníh z čepele a obměňujte pásku. Nenechávejte hůl v mrazu v autě ani u topení a pravidelně kontrolujte praskliny.'),
         ('Proč je u hokejek důležité zahnutí čepele?', 'Zahnutí ovlivňuje, jak puk vedete a jak vysoko vzlétá při střele. Větší zahnutí usnadňuje zvedání, mělčí pomáhá přesným přihrávkám a střelám po ledě.'),
         ('Jak najít nejvýhodnější nabídku stejné hokejky?', 'Na Sportece otevřete konkrétní model a porovnejte obchody podle skladovosti, délky a strany čepele. Nejlevnější nabídka nemusí mít rozměr, který potřebujete.')],
)


# ------------------------------------------------------------------ vareni-v-prirode
NEW['vareni-v-prirode'] = dict(long=True,
    title='Vaření v přírodě: vařiče, kartuše, nádobí',
    desc='Vybavení pro vaření na túře a v kempu: vařiče, kartuše, hrnce, příbory a termosky. Jak vybrat podle trasy, počtu lidí a paliva.',
    intro='<p>Teplé jídlo po celém dni venku dokáže zachránit náladu, jenže polovina úspěchu leží v tom, co vezete v batohu. '
          'Kategorie <strong>vaření v přírodě</strong> sdružuje <a href="/varice-a-kartuse/">vařiče a kartuše</a>, <a href="/kempingove-nadobi/">kempingové nádobí a příbory</a>, '
          'ale i ohniště, rošty, litinové nádoby, kávové sady a doplňky na přípravu jídla pod širým nebem. Vybavení pro ultralehkou túru se výrazně liší od toho, co postavíte u auta na kempu, '
          'a právě tomuto rozdílu se věnuje celý průvodce.</p>'
          '<p>Na Sportece najdete nabídky českých obchodů vedle sebe a můžete porovnat konkrétní model plynového vařiče, hrnce nebo sady příborů. '
          'Spolu s vařením se hodí zvážit také <a href="/stany/">stany</a>, <a href="/spaci-pytle/">spací pytle</a> a <a href="/kempingovy-nabytek/">kempingový nábytek</a>. Obecný přehled najdete v kategorii <a href="/kemping/">kemping</a>.</p>',
    guide='<h2>Jak se liší vaření na túře a v kempu</h2>'
          '<p>Než začnete vybírat, ujasněte si styl. Na trek, kde nesete všechno na zádech, počítá každý gram i každý centimetr místa v batohu. Při autokempingu naopak hmotnost řešit nemusíte a dává smysl pořídit větší hrnce, rošty, dvouplamenný vařič nebo litinový kotlík. '
          'Mezi tím je kompromis pro cyklisty a pro rodiny, které se k místu přesouvají pěšky jen několik stovek metrů.</p>'
          + T(['Styl', 'Typické vybavení', 'Na co dbát'], [
              ['Ultralehká túra', 'malý plynový vařič nebo lihový, titanový hrnek, lžíce', 'hmotnost, skládací rozměry a spotřeba paliva'],
              ['Vícedenní trek', 'plynový vařič s kartuší, hliníkový nebo titanový hrnec, termoska', 'dostupnost kartuší, odolnost proti větru'],
              ['Autokemping', 'dvouplamenný vařič, pánev, kotlík, rošt, sada nádobí', 'stabilita, snadné čištění, zásoba paliva'],
              ['Rodina s dětmi', 'plastové či smaltované nádobí, termosky, jídelní sady', 'bezpečnost povrchů, odolnost a mytí'],
              ['Bushcraft a ohniště', 'litina, pánve na oheň, ocelové hrnce, rukavice', 'váha, péče o nádobí, předpisy o rozdělávání ohně']]) +
          '<h2>Typy vařičů a paliv</h2>'
          '<p>Vařič je jádro systému. Nejrozšířenější jsou plynové vařiče na závitové kartuše, které se zapálí jedním pohybem a dobře se ovládají. '
          'Existují i modely s integrovaným hrncem, jež sjednocují vařič, hrnec a odvod tepla do jedné sestavy a vodu přivádějí k varu rychleji než samostatné kombinace. Lihové vařiče jsou tiché a jednoduché, ale pomalejší a citlivější na vítr. '
          'Benzinové a multifuel vařiče se hodí do mrazu a na expedice, kde je plyn nepraktický. Pevná paliva v tabletách stačí na ohřev jídla v nouzi.</p>'
          '<ul><li><strong>Plyn:</strong> pohodlné ovládání, čisté spalování, za mrazu klesá výkon a kartuše je nutné chránit teplem.</li>'
          '<li><strong>Líh:</strong> tichý, bez tlaku, vhodný pro ultralehké sestavy, citlivý na vítr.</li>'
          '<li><strong>Benzín a multifuel:</strong> spolehlivé v extrémních podmínkách, vyžadují údržbu a předehřev.</li>'
          '<li><strong>Dřevo a ohniště:</strong> bez nákladů na palivo, zato s ohledem na místní pravidla a požární riziko.</li></ul>'
          '<p>Podrobnější přehled s konkrétními modely a kartušemi najdete v kategorii <a href="/varice-a-kartuse/">vařiče a kartuše</a>.</p>'
          '<h2>Kartuše: na co dát pozor</h2>'
          '<p>Plynové kartuše se dodávají s různými závity a směsmi. Nejrozšířenější jsou kartuše se šroubovacím ventilem (EN 417). Propichovací a bajonetové systémy se s nimi nedají zaměňovat, proto vždy zkontrolujte, že vařič a kartuše jsou stejného systému. '
          'Směsi propan, butan a isobutan se liší chováním v chladu: s vyšším podílem isobutanu a propanu fungují lépe za nižších teplot. '
          'Vždy si spočítejte, kolik plynu vám vystačí na plánovanou dobu, a přibalte rezervu. Prázdnou kartuši nikdy nevhazujte do ohně ani do běžného odpadu, odevzdává se do sběru kovů podle místních pravidel. '
          'Vařič s kartuší patří do dobře větraného prostoru a nikdy do stanu, hrozí požár a otrava oxidem uhelnatým.</p>'
          '<h2>Nádobí na túru</h2>'
          '<p>Při výběru hrnce rozhoduje materiál a objem. Hliník dobře vede teplo a je lehký, tenké stěny se ale snadno přepalují a jídlo se na nich připaluje, pokud nemíchate. '
          'Titan je velmi lehký a odolný, vede ale teplo hůř, takže se hodí hlavně na vaření vody. Nerez je těžší, ale dobře snáší nárazy a dlouhodobé používání. '
          'Povrchová úprava proti připalování usnadňuje mytí, jenže se při hrubém zacházení poškrábe.</p>'
          + T(['Materiál', 'Výhody', 'Nevýhody'], [
              ['Hliník', 'nízká hmotnost, dobré vedení tepla', 'méně odolný proti poškrábání a promáčknutí'],
              ['Titan', 'velmi nízká hmotnost, vysoká pevnost', 'nerovnoměrný ohřev, hodí se na vodu'],
              ['Nerez', 'odolnost, snadná údržba', 'vyšší hmotnost, delší ohřev'],
              ['Litina', 'vynikající udržení tepla, delší život', 'velká hmotnost, nutná péče o povrch'],
              ['Silikon a plast', 'skladnost, bezpečné pro děti', 'nehodí se k přímému ohni']]) +
          '<p>Kompletní nabídku hrnců, mís, příborů a hrnků najdete v kategorii <a href="/kempingove-nadobi/">kempingové nádobí a příbory</a>. '
          'Praktické jsou sady, které se do sebe vloží jako matrjošky, a skládací misky a hrnky ze silikonu, které v batohu zaberou minimum místa.</p>'
          '<h2>Příbory, nože a drobnosti</h2>'
          '<p>Na túru stačí lžíce s dlouhou rukojetí, která dosáhne na dno sáčku s lyofilizovaným jídlem. Kdo vaří z čerstvých surovin, ocení malý nůž a dřevěnou obracečku. '
          'Spork, tedy kombinace lžíce a vidličky, je oblíbený kompromis. Vhodné nože a multitoolly najdete v kategorii <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoolly</a>. '
          'Nezapomeňte na zapalovač a rezervní sirky v nepromokavém obalu, otvírák na konzervy, hadřík na uchopení horkého hrnce a malou houbičku na mytí.</p>'
          '<h2>Voda, termosky a čištění</h2>'
          '<p>Vaření není jen vařič a hrnec. Teplý nápoj z termosky šetří palivo a nahrazuje druhé vaření během dne. Vhodné modely najdete v kategorii <a href="/lahve-a-termosky/">láhve a termosky</a>. '
          'Pro čištění vody a hygienu v kempu se hodí <a href="/hygiena-a-repelenty/">hygiena, repelenty a úprava vody</a>. Na jídlo, které se nesmí zkazit, myslete na <a href="/chladici-boxy/">chladicí boxy a tašky</a>. '
          'Nádobí myjte co nejdál od vodních zdrojů, odpadní vodu vylévejte na zem s rozptylem a zbytky jídla odneste.</p>'
          '<h2>Jídlo, které se vyplatí vzít</h2>'
          '<p>Nejjednodušší cesta jsou jídla, která stačí zalít vroucí vodou. Hotové sáčky s lyofilizovanou stravou se prodávají v <a href="/outdoorova-strava/">outdoorové a lyofilizované stravě</a>. '
          'Rychlé energie na cestu doplní sušené ovoce, ořechy, instantní kaše a těstoviny s krátkou dobou vaření. Při vícedenním vaření zvažujte, kolik vody a paliva jídlo spotřebuje, protože těstoviny a rýže si vyžádají víc plynu než instantní kaše.</p>'
          '<h2>Jak plánovat jídelníček a množství</h2>'
          '<p>Praktický postup je rozepsat si jídla po dnech a ke každému připsat, kolik vody je potřeba přivést k varu. Snídaně a večeře bývají teplé, oběd na túře často studený, aby se šetřilo palivo. '
          'Pro jednu osobu stačí na dvě jídla denně menší hrnec, pro dva lidi si vezměte větší nádobu nebo dva menší kusy, jinak budete vařit na dvakrát. '
          'Přebytečné balení z potravin vyhoďte předem a jídlo přesypte do lehkých sáčků. Šetří to místo i hmotnost a v kempu se méně zanáší okolí obaly.</p>'
          '<h2>Kávový a čajový rituál</h2>'
          '<p>Kdo chce ráno pořádnou kávu, má na výběr skládací dripper, malý kovový filtr, hliníkovou moka konvičku nebo french press z odolného plastu. '
          'Na vodu stačí menší hrnec a při větším počtu hrnků se vyplatí termokonvice. Čaj z lístků zvládne sítko přímo v hrnku. Zvažte i izolované hrnky, ve kterých nápoj vydrží teplý a ruce se nepopálí.</p>'
          '<h2>Skladování a údržba po cestě</h2>'
          '<p>Po návratu nádobí důkladně umyjte a nechte uschnout, než jej složíte, jinak se v zákoutích usadí zápach a plíseň. Vařič zbavte zbytků jídla a zkontrolujte těsnění u závitu. '
          'Kartuše skladujte v suchu a při pokojové teplotě mimo dosah dětí. Litinu natřete tenkou vrstvou oleje, nerez a titan vydrží bez ošetření. Před další cestou vyzkoušejte vařič doma na balkoně, abyste na trase nezjistili, že chybí těsnění nebo že se zadrhává ventil, a ověřte, že zapalovač stále jiskří.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například značky ' + B(('petromax', 'Petromax'), ('thermos', 'Thermos'), ('primus', 'Primus'), ('stanley', 'Stanley'), ('kambukka', 'Kambukka'), ('sea-to-summit', 'Sea to Summit'), ('fire-maple', 'Fire-maple'), ('jetboil', 'Jetboil'), ('light-my-fire', 'Light my fire'), ('eurotrail', 'Eurotrail')) + '. '
          'Petromax je známý litinovým nádobím na oheň, Primus a Jetboil vařiči a kartušemi, Thermos, Stanley a Kambukka izolovanými lahvemi a hrnky, Sea to Summit a Light my fire skladným a lehkým nádobím.</p>'
          '<h2>Bezpečnost a ohleduplnost</h2>'
          '<ul><li>Vařič stavte na rovný a nehořlavý povrch, mimo suchou trávu a jehličí.</li>'
          '<li>Kartuši nikdy nezahřívejte přímo, riziko výbuchu je skutečné.</li>'
          '<li>Při vaření nenechávejte plamen bez dozoru a mějte po ruce vodu.</li>'
          '<li>Rozdělávání ohně je v mnoha oblastech zakázané nebo omezené, informujte se u správy chráněného území.</li>'
          '<li>Veškerý odpad odneste s sebou, včetně spálených zbytků a prázdných kartuší.</li></ul>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Kupovat vařič, aniž byste zjistili, jaké kartuše se u vás shánějí.</li>'
          '<li>Podcenit vítr. Vařič bez ochrany spotřebuje výrazně víc paliva.</li>'
          '<li>Brát příliš velký hrnec na jednoho. Zbytečná váha a delší ohřev.</li>'
          '<li>Zapomenout na čištění a pak připalovat jídlo na odřený povrch.</li>'
          '<li>Nepočítat se spotřebou paliva na celou trasu.</li></ul>'
          '<h2>Co si zabalit dohromady</h2>'
          '<p>K vaření se hodí stabilní zázemí, proto zvažte také <a href="/kempingove-doplnky/">kempingové doplňky</a>, <a href="/hamaky/">hamaky</a> a lehký sedák nebo skládací <a href="/karimatky-a-matrace/">karimatku</a>. '
          'Pro noční vaření a úklid pomůže <a href="/celovky-a-svitilny/">čelovka</a> a pro nošení všeho dohromady <a href="/turisticke-batohy/">turistický batoh</a>. První pomoc při popálení řeší <a href="/prvni-pomoc/">lékárnička</a>.</p>',
    faq=[('Jaký vařič zvolit na vícedenní túru?', 'Nejčastěji plynový vařič na závitovou kartuši. Je lehký, snadno se ovládá a kartuše se dají koupit i v menších obchodech. V mrazu uvažujte o multifuel modelu.'),
         ('Jak dlouho vydrží plynová kartuše?', 'Záleží na velikosti kartuše, výkonu vařiče a počasí. Při větru nebo za chladu spotřeba roste, proto počítejte s rezervou a vařte v závětří.'),
         ('Je titan lepší než hliník?', 'Titan je lehčí a pevnější, ale špatně vede teplo, a hodí se hlavně na vodu. Hliník je levnější a zahřívá rovnoměrněji, jen je méně odolný.'),
         ('Můžu vařit uvnitř stanu?', 'Ne. Hrozí požár a otrava oxidem uhelnatým. Vařte venku s odstupem od látky stanu a nikdy ne v předsíni ani uvnitř stanu.'),
         ('Co všechno patří do základní sady na vaření?', 'Vařič, kartuše, hrnec nebo kotlík s víkem, lžíce či spork, hrnek, zapalovač, houbička na mytí a termoska. Podle trasy přidejte nůž a filtr na vodu.'),
         ('Jak čistit připálený kempingový hrnec?', 'Zalijte ho vodou s trochou jaru a nechte odmočit, pak použijte měkkou houbu. Hrubé škrabky ničí nepřilnavou vrstvu a zkracují životnost nádobí.'),
         ('Hodí se litinové nádobí na túru?', 'Na pěší túru ne, je těžké. Skvěle ale funguje v autokempu a u ohniště, kde se využije schopnost udržet teplo. Po použití je nutné ho vysušit a ošetřit olejem.'),
         ('Jak vyřešit vítr při vaření?', 'Stavte vařič do závětří za batoh nebo kameny a používejte větrnou clonu k tomu určenou. Clonu ale nepřibližujte ke kartuši, mohla by ji nebezpečně zahřát.'),
         ('Jak odnášet odpad z vaření?', 'Zbytky jídla a obaly zabalte do pytlíku a odneste k odpadkovému koši. Odpadní vodu vylévejte daleko od vodních toků a prázdné kartuše odevzdejte do sběru kovů.'),
         ('Jak porovnat ceny vařičů a nádobí?', 'Na Sportece otevřete konkrétní model a prohlédněte si nabídky obchodů vedle sebe. U sad se podívejte, co přesně obsahují, protože stejně pojmenované sady se liší počtem dílů.')],
)


# ------------------------------------------------------------------ cyklo-riditka
NEW['cyklo-riditka'] = dict(long=True,
    title='Řídítka, představce a sedlovky na kolo',
    desc='Řídítka, představce a sedlovky pro MTB, silnici i město: průměry, délky, materiály a kompatibilita. Návod na výběr a ceny z českých obchodů.',
    intro='<p>Řídítka, představec a sedlovka jsou tři díly, které určují posed, tedy to, jak na kole sedíte a jak se opíráte o řídítka. Právě proto se u nich vyplatí přemýšlet víc než u většiny ostatních součástí. '
          'Špatná šířka řídítek, příliš dlouhý představec nebo sedlovka v nesprávné výšce nebo délce vedou k bolesti zad, zápěstí i kolen, a to dřív, než si začnete stěžovat na samotné kolo.</p>'
          '<p>V kategorii <strong>řídítka, představce a sedlovky</strong> najdete rovná i zvednutá řídítka pro horská kola, zahnutá řídítka na silnici a gravel, '
          'městské a trekingové modely, představce různých délek i sedlovky pevné nebo výsuvné. Porovnání cen z českých obchodů pomůže u shodných rozměrů. '
          'Navazují <a href="/sedla-a-gripy/">sedla, gripy a potahy</a>, <a href="/cyklo-brzdy/">brzdy</a> a obecná skupina <a href="/cyklo-dily/">díly a pláště</a>.</p>',
    guide='<h2>Řídítka: typy podle kola</h2>'
          '<p>Tvar řídítek určuje posed, a tím i styl jízdy. Existuje pět hlavních typů, každý se hodí k jinému typu kola.</p>'
          + T(['Typ řídítek', 'Pro jaká kola', 'Hlavní vlastnost'], [
              ['Rovná (flat bar)', 'horská kola XC, trail a levnější trekingová kola', 'přímé ovládání, široký posed'],
              ['Riser (zvednutá)', 'horská kola, enduro, downhill, městská kola', 'zvýšený střed, vzpřímenější posed'],
              ['Beran (drop bar)', 'silniční a gravel kola', 'více poloh rukou, aerodynamický posed'],
              ['Motýlková (trekking)', 'dálkové cestovní kolo', 'mnoho poloh úchopu pro dlouhé dny v sedle'],
              ['Městská a retro', 'městská kola, holandky', 'hodně zvednutá, vzpřímený postoj']]) +
          '<p>Horské riser řídítka se dělí podle zdvihu, tedy výšky zvednutí středu, a podle zahnutí do stran, které ovlivňuje pozici zápěstí. '
          'Na silnici a gravelu je zásadní šířka podle ramen a hloubka beranu, tedy vzdálenost od horní části k nejnižšímu místu. Gravelová řídítka mívají rozevřené konce, které dávají stabilitu na nezpevněném povrchu.</p>'
          '<h2>Šířka a průměr řídítek</h2>'
          '<p>Šířka se vybírá podle šířky ramen na silnici a podle stylu jízdy v terénu. Příliš úzká řídítka dusí dýchání a snižují kontrolu, příliš široká zatěžují ramena a ztěžují průjezd mezi stromy či při jízdě v davu. '
          'U horských kol dnes převládají širší řídítka, které v případě potřeby půjde zkrátit pilkou, u silnice jsou typické užší modely.</p>'
          '<p>Důležitější než šířka je <strong>průměr sevření</strong>, tedy tloušťka řídítek v místě, kde je drží představec. Nejčastější rozměry jsou 25,4 mm u starších a městských kol, '
          '31,8 mm u moderních horských a silničních kol a 35 mm u náročnějšího terénu. Představec a řídítka musí mít shodný průměr, jinak se nedají bezpečně uchytit. Redukční podložky se u náročné jízdy nedoporučují, bezpečnější je kombinace dílů se shodným průměrem.</p>'
          '<h2>Představce: délka, úhel a průměr</h2>'
          '<p>Představec propojuje řídítka s vidlicí. Má tři parametry: délku, úhel zdvihu a rozměry sevření. '
          'Delší představec protáhne posed a stabilizuje řízení při rychlosti, kratší ho zpřímí a zrychlí reakci řízení. Úhel určuje, zda řídítka uvedete výš, nebo níž než hlavovou část rámu. '
          'Při změně o malé hodnoty se zlepší pohodlí, při větších změnách může zasáhnout do geometrie, proto je dobré vždy měnit jednu věc.</p>'
          '<ul><li><strong>Průměr řídítek:</strong> sevření na středu řídítek musí odpovídat jejich průměru.</li>'
          '<li><strong>Průměr krkové trubky:</strong> nejčastější standard je 1 1/8 palce, existují i užší a kónické systémy, které vyžadují jiný představec.</li>'
          '<li><strong>Typ upevnění:</strong> čelní sevření s několika šrouby je dnes standardem, starší typy se utahují shora do trubky vidlice.</li>'
          '<li><strong>Materiál:</strong> hliník je odolný a dostupný, karbon lehčí a tlumivější, ale vyžaduje přesné dotahování momentovým klíčem.</li></ul>'
          '<h2>Sedlovky: pevné, odpružené a výsuvné</h2>'
          '<p>Sedlovka vede sedlo a upravuje jeho výšku. Většina kol má pevnou sedlovku z hliníku nebo karbonu, kterou je potřeba nastavit podle vašeho rozkroku. '
          'U horských kol se rozšířily <strong>výsuvné sedlovky</strong>, které se ovládají páčkou na řídítkách a během sjezdu snižují sedlo, aby se jezdec mohl volněji pohybovat. '
          'Odpružené sedlovky tlumí nárazy na městských a trekingových kolech a vyplatí se pro pohodlí na dlouhých trasách.</p>'
          '<p>Při koupi se řídí tři rozměry: průměr trubky, délka a u výsuvných sedlovek zdvih. Mezi běžné průměry patří 27,2 mm, 30,9 mm, 31,6 mm a 34,9 mm. '
          'Správný údaj najdete vyražený na stávající sedlovce nebo ho změříte posuvným měřidlem na dolním konci. Do sedlové trubky by sedlovka měla zasahovat nejméně do vyznačené minimální hloubky. '
          'U rámů s vnitřním vedením lanka výsuvné sedlovky potřebují odpovídající průchod.</p>'
          + T(['Sedlovka', 'Pro koho', 'Na co dát pozor'], [
              ['Pevná hliníková', 'městská a trekingová kola, začátečníci', 'správný průměr a délka'],
              ['Pevná karbonová', 'silniční a XC kola', 'nešroubovat bez karbonové pasty a momentového klíče'],
              ['Výsuvná (dropper)', 'trail, enduro, all-mountain', 'zdvih, vedení lanka a průměr'],
              ['Odpružená', 'město, trekking, dlouhé trasy', 'vyšší hmotnost, nastavení tuhosti']]) +
          '<h2>Jak se vybírá správná velikost</h2>'
          '<p>Výšku sedla nastavte tak, aby noha při spodní poloze pedálu zůstala lehce pokrčená. Pro vodorovné polohování sedla vpřed či vzad si pomůžete měřením, ale nejpřesnější je vyzkoušet pár týdnů jízdy a posunovat po milimetrech. '
          'Délku představce zvolte tak, aby se při úchopu na řídítka nezkracovaly ani neprotahovaly paže. Jako výchozí bod dobře poslouží původní rozměr kola a pak se jen mírně upravuje. '
          'Když kolo kupujete pro dítě nebo pro odlišně vysokého jezdce, změřte nejdřív rozměry původních dílů na <a href="/jizdni-kola/">jízdním kole</a> a podle nich vybírejte náhradu.</p>'
          '<h2>Materiály: hliník, ocel a karbon</h2>'
          '<p>Hliník je nejrozšířenější. Je dostupný, odolný a lehce opravitelný. Ocel se vyskytuje u retro a městských sestav. Karbon nabízí nízkou hmotnost a lepší tlumení vibrací, ale reaguje citlivěji na přetažení šroubů a nesmí se poškrábat hluboko do vlákna. '
          'Po pádu je u karbonových dílů nutná důkladná kontrola, praskliny se často skrývají pod lakem. Pokud si nejste jistí, raději díl vyměňte.</p>'
          '<h2>Montáž krok za krokem</h2>'
          '<ol><li>Vyfotografujte stávající nastavení, abyste měli referenční polohu.</li>'
          '<li>Povolte šrouby představce a sundejte čelní víčko, uvolněte řídítka.</li>'
          '<li>U karbonových dílů naneste na styčné plochy montážní pastu s třením, u hliníku stačí čistý povrch.</li>'
          '<li>Šrouby dotahujte křížem po malých krocích do doporučeného utahovacího momentu uvedeného na dílu.</li>'
          '<li>Zkontrolujte, zda řídítka nepromlouvají a zda se vidlice otáčí bez vůle.</li>'
          '<li>Po první jízdě šrouby zkontrolujte znovu.</li></ol>'
          '<p>Pokud nemáte momentový klíč ani zkušenost, svěřte montáž servisu. Chyba při dotahování představce nebo sedlovky patří k bezpečnostně nejzávažnějším.</p>'
          '<h2>Ergonomie a bolest rukou</h2>'
          '<p>Brní vám prsty nebo bolí zápěstí? Často za tím stojí kombinace příliš nízkého představce, špatně natočených řídítek a nastavení pák. Řídítka natočte tak, aby zápěstí zůstalo v přímé linii s předloktím, a páky brzd nasměrujte zhruba do prodloužení rukou. '
          'Když se tělo při delší jízdě sune dopředu, sedlo je pravděpodobně moc vpředu nebo nakloněné dolů. Drobné úpravy po několika milimetrech jsou účinnější než jedna velká změna a obvykle nestojí nic víc než čas s imbusovým klíčem.</p>'
          '<h2>Spacery a úprava výšky řídítek</h2>'
          '<p>Výšku řídítek měníte pomocí podložek pod představcem. Přebytečná trubka vidlice se při dostatečném zkrácení nechává jen v rozsahu, který výrobce povoluje, a řez se dělá až poté, co si jistě ověříte nejpohodlnější polohu. '
          'Dokud se nerozhodnete, ponechte podložky nad představcem, aby šlo posun vrátit. U karbonových vidlic používejte jemný pilový list a důsledně dodržujte pokyny výrobce, trubka nesmí být poškozená.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii se objevují například značky ' + B(('rockbros', 'Rockbros'), ('ritchey', 'Ritchey'), ('reverse', 'Reverse'), ('force', 'Force'), ('race-face', 'Race Face'), ('max1', 'Max1'), ('easton-cycling', 'Easton Cycling'), ('fsa', 'FSA'), ('topeak', 'Topeak'), ('redshift', 'Redshift')) + '. '
          'Ritchey, Race Face, FSA a Easton jsou tradiční výrobci kokpitů a sedlovek pro silnici a terén, Reverse a Force pokrývají střední třídu, Rockbros a Max1 dostupnější sortiment. Redshift se zaměřuje na odpružené nebo nastavitelné součástky.</p>'
          '<h2>Související díly a vybavení</h2>'
          '<p>Kokpit nekončí u řídítek. K nim patří <a href="/sedla-a-gripy/">gripy a omotávky</a>, <a href="/cyklo-brzdy/">brzdy a destičky</a>, <a href="/cyklo-pohon/">řazení a pohon</a> a '
          '<a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>. Na zakončení řídítek zapadají <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a> a <a href="/cyklo-svetla/">světla</a>. '
          'Držák telefonu či bidon řeší <a href="/cyklo-lahve-a-drzaky/">láhve a držáky</a>. Komfort jízdy ovlivňují i <a href="/plaste-a-duse/">pláště a duše</a>. '
          'U <a href="/elektrokola/">elektrokol</a> se kvůli vyšší hmotnosti a rychlosti vyplatí pevnější kokpit a sedlovka s dostatečnou nosností.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Záměna průměrů. Řídítka 31,8 mm nepasují do sevření 35 mm a naopak.</li>'
          '<li>Příliš krátká sedlovka. Musí zasahovat do rámu nejméně po značku minimálního zasunutí a ta nesmí být vidět.</li>'
          '<li>Karbonový díl dotažený bez momentového klíče nebo s hrubou silou.</li>'
          '<li>Nevhodná šířka řídítek, často jen proto, že byla na jiném kole.</li>'
          '<li>Výsuvná sedlovka bez ověření vedení lanka v rámu.</li>'
          '<li>Měnit víc rozměrů kokpitu najednou, takže nevíte, co za změnu pocitu může.</li></ul>'
          '<h2>Pro koho je tato kategorie</h2>'
          '<p>Pro každého, kdo chce kolo přizpůsobit sobě. Začátečníci sem zamíří, když jim kolo po pár jízdách nesedí. Pokročilí tu hledají lehčí karbon, výsuvnou sedlovku nebo jiný tvar řídítek. '
          'Servisní techniky zajímají přesné rozměry pro opravy a rodiče dětem vybírají kratší představec a užší řídítka. Při rozhodování pomůže i zápis rozměrů původních dílů, do telefonu nebo do sešitu, abyste při koupi náhrady nemuseli měřit znovu. Pokud potřebujete doplnit nářadí k montáži, najdete ho v <a href="/cyklo-pumpy-a-naradi/">pumpách a nářadí</a>.</p>',
    faq=[('Jaký průměr řídítek mám zvolit?', 'Průměr sevření musí odpovídat představci. U starších a městských kol se objevuje 25,4 mm, u moderních horských a silničních kol nejčastěji 31,8 mm a u terénních 35 mm.'),
         ('Jak poznám správný průměr sedlovky?', 'Údaj bývá vyražený na spodní části sedlovky. Pokud tam není, změřte posuvným měřidlem průměr trubky. Nejčastější hodnoty jsou 27,2, 30,9, 31,6 a 34,9 mm.'),
         ('Jak dlouhý představec koupit?', 'Začněte rozměrem, který máte na kole. Delší představec protahuje posed a stabilizuje řízení, kratší zrychluje reakci a zpřímí tělo. Měňte jej po malých krocích.'),
         ('Je výsuvná sedlovka potřeba?', 'Pro sjezdový trail a enduro velmi užitečná, protože sedlo během jízdy snížíte. Na silnici, ve městě a na běžném trekingu ji většina jezdců nepotřebuje.'),
         ('Co znamená zdvih výsuvné sedlovky?', 'Je to vzdálenost, o kterou se sedlo sníží z plné výšky. Zdvih musí zapadat do délky sedlové trubky vašeho rámu a do výšky, kterou potřebujete.'),
         ('Je karbonové řídítko bezpečné?', 'Ano, pokud se správně montuje a po pádu zkontroluje. Dotahujte jen předepsaným momentem, používejte montážní pastu a při jakékoli prasklině díl vyměňte.'),
         ('Jaká řídítka na silniční a gravel kolo?', 'Beranová řídítka. Pro silnici užší s menší hloubkou, pro gravel s mírně rozevřenými konci pro lepší kontrolu na nezpevněném povrchu.'),
         ('Jak často kontrolovat šrouby představce?', 'Po první jízdě po montáži a potom pravidelně při servisu nebo před delší jízdou. Šrouby se mohou uvolnit působením vibrací, proto je dobré je občas prohlédnout.'),
         ('Mohu zkrátit horská řídítka?', 'Hliníková řídítka lze zkrátit pilkou na kov nebo speciálním nástrojem. Karbonová jen tehdy, když to výrobce výslovně povoluje, jinak je nezkracujte, protože řez poškodí vlákna a zanikne záruka. Zkracujte symetricky a ověřte, že vedení brzd a řazení stále pohodlně dosáhne.'),
         ('Kde najdu srovnání cen?', 'Na Sportece otevřete konkrétní díl s přesným rozměrem a porovnejte nabídky obchodů. Při srovnání vždy zkontrolujte průměr, délku a typ upevnění.')],
)


# ------------------------------------------------------------------ sipkove-doplnky
NEW['sipkove-doplnky'] = dict(long=True,
    title='Šipky: letky, násadky, hroty a pouzdra',
    desc='Doplňky k šipkám: letky, násadky, hroty, barely a pouzdra pro steel i soft. Jak vybrat tvar, délku a materiál a nabídky českých obchodů.',
    intro='<p>Šipka se skládá ze čtyř částí a každou z nich lze vyměnit. Právě tohle dělá z doplňků nenápadný, ale důležitý díl hry: s jinou letkou nebo kratší násadkou se šipka chová jinak, aniž byste museli kupovat novou sadu. '
          'Kategorie <strong>letky, násadky, hroty a pouzdra na šipky</strong> obsahuje všechny náhradní a ladicí součástky, od základních plastových letek po barely z wolframu, ocelové hroty, plastové softy, pružné kroužky a ochranné tuby.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u shodných položek a snadno najdete tvar letky nebo délku násadky, kterou potřebujete. '
          'Pokud ještě nemáte cíl, podívejte se na <a href="/sipkove-terce/">šipkové terče a stojany</a>. Celý obor shrnuje kategorie <a href="/sipky/">šipky</a>, '
          'širší nabídku her najdete ve skupině <a href="/volny-cas/">hry a volný čas</a>.</p>',
    guide='<h2>Z čeho se šipka skládá</h2>'
          '<p>Než začnete vybírat doplňky, ujasněte si názvosloví. Šipka má <strong>hrot</strong> (špičku), <strong>barel</strong> (tělo), <strong>násadku</strong> (stonek) a <strong>letku</strong>. '
          'Hrot se zasekává do terče, barel drží ruka, násadka propojuje barel s letkou a letka zajišťuje stabilitu letu. Změna kterékoli části mění těžiště, odpor vzduchu i pocit v ruce.</p>'
          + T(['Část', 'Co dělá', 'Co lze měnit'], [
              ['Hrot', 'zaráží se do terče', 'ocelový nebo plastový, délka, drsnost povrchu'],
              ['Barel', 'drží se v ruce, nese váhu', 'hmotnost, materiál, tvar, rýhování'],
              ['Násadka', 'spojuje barel a letku', 'délka, materiál, pevnost, otvor pro uchycení letky'],
              ['Letka', 'stabilizuje let', 'tvar, velikost, tloušťka, materiál']]) +
          '<h2>Steel, nebo soft: nejdřív typ terče</h2>'
          '<p>První rozhodnutí je, jakou šipku vlastně hrajete. Steel tip, tedy šipky s kovovým hrotem, se házejí na tradiční terč ze sisalových vláken. '
          'Soft tip se používá na elektronické terče s otvory, do kterých se plastový hrot zasune. Hroty a závity se nedají libovolně kombinovat. U šipky s ocelovým hrotem hrozí na elektronickém terči poškození, a naopak plastový hrot se na sisalu rychle zlomí. '
          'Správný typ terče najdete v kategorii <a href="/sipkove-terce/">šipkové terče a stojany</a>. Pro orientaci: steel šipky bývají obvykle o něco těžší a štíhlejší, soft o něco lehčí a s kratším barelem.</p>'
          '<h2>Letky: tvar, velikost, tloušťka</h2>'
          '<p>Letka je to, co se nejčastěji lámá a vyměňuje, a také to, co nejrychleji změní chování šipky. Větší plocha letky brzdí let a stabilizuje šipku, menší dává přímější let a vyšší rychlost. '
          'Tvary mají obvyklé názvy:</p>'
          '<ul><li><strong>Standardní:</strong> klasický tvar s velkou plochou, vhodný pro začátečníky a šipky hozené s menší silou.</li>'
          '<li><strong>Slim (úzká):</strong> užší profil pro přímý let a lepší seskupování šipek vedle sebe v terči.</li>'
          '<li><strong>Kite (drak):</strong> čtyřhranný tvar, ustálený a tolerantní.</li>'
          '<li><strong>Pear (hruška):</strong> hybrid mezi standardní a úzkou letkou.</li>'
          '<li><strong>Mini a malé:</strong> pro rychlé hráče a krátké násadky.</li></ul>'
          '<p>Důležitá je i tloušťka. Standardní fólie se snáze ohýbá a rychle se zničí, silnější tvrdí a drží tvar déle, za cenu hlučnějšího odrazu o terč. Zkoušejte jednu změnu najednou, aby bylo poznat, co se změnilo.</p>'
          '<h2>Násadky: délka a materiál</h2>'
          '<p>Násadka reguluje dráhu letu. Delší násadka posouvá letku dál od těžiště a šipka letí stabilněji a při dopadu se víc „zvedá“, kratší zrychluje a snižuje šipku. '
          'Délky se značí slovy: velmi krátká, krátká, střední a dlouhá (někdy v milimetrech). Hráči, kteří házejí ostře rovným obloukem, často berou krátké. Hráči s obloukovým letem volí delší.</p>'
          + T(['Materiál násadky', 'Vlastnosti', 'Vhodné pro'], [
              ['Nylon a plast', 'pružný, levný, lehce se zlomí', 'začátečníci, domácí hra'],
              ['Hliník', 'pevný, nízká hmotnost, snadno se ohne', 'hráči s pravidelným tréninkem'],
              ['Karbon a kompozit', 'lehký a pevný, odolný proti ohnutí', 'ambiciózní hráči'],
              ['Titan a ocel', 'vysoká odolnost, vyšší hmotnost', 'těžší šipky a silný hod'],
              ['Rotující násadky', 'otáčí se, šetří letku', 'hráči, kterým se letky rychle ničí']]) +
          '<p>Nejčastější starost začátečníků je uvolňování letek a násadek. Pomáhají pružné <strong>O-kroužky</strong> na závitu nebo kroužek pod barelem. Tyto drobnosti se dobře kupují ve více kusech.</p>'
          '<h2>Hroty a barely</h2>'
          '<p>Ocelový hrot se vyrábí hladký, rýhovaný nebo s drsnějším povrchem a bývá z kalené oceli. Pokud se zakřiví nebo ztupí, vyměňte jej. Delší hrot dopadá hlouběji, kratší odráží. '
          'Plastové soft hroty se mačkají a lámou, proto se prodávají ve velkých baleních. Správný závit je nutné zkontrolovat před koupí, protože se liší u různých typů a rozměrů.</p>'
          '<p>Barely se vyrábějí z mosazi, nikl-stříbra nebo wolframu v různém podílu. Wolfram je hustý, takže barel je štíhlejší při stejné hmotnosti, a to umožňuje hustější seskupení šipek v terči. '
          'Mosazné barely jsou levnější a o něco objemnější. Rýhování, vroubkování a kroužky na povrchu určují úchop. Hmotnost se udává v gramech a volí se podle pocitu: příliš těžké šipky unavují, příliš lehké se chovají nestabilně.</p>'
          '<h2>Pouzdra a ochrana</h2>'
          '<p>Pouzdro nebo peněženka chrání šipky před poškozením, hlavně při přepravě. Tvrdé plastové tuby jsou vhodné pro jednu sadu, látková pouzdra zvládnou víc šipek a drobné doplňky. '
          'Rozdělené kapsy zabrání, aby se hroty dotýkaly letek. Před cestou vždy zkontrolujte, zda je pouzdro zamčené. Pro domácí hru si pořiďte nástěnnou polici nebo držák, aby šipky neležely v šuplíku s hroty nahoru.</p>'
          '<p>Ochranné kroužky a ochranné chrániče letek (flight protectors) prodlužují život letky a zabraňují ohnutí hrotu o sousední šipku. Hodí se i brousek na hroty nebo brusná fólie na zpracování drsnosti, ale nikdy je nepřebrušujte, ostrost snadno zvýší riziko odrazu.</p>'
          '<h2>Jak doplňky zkoušet</h2>'
          '<p>Nejlepší postup je změnit jednu věc a házet alespoň několik desítek hodů. Pro porovnání zapisujte, kam šipky dopadají. Nejprve se vyzkouší letky, potom délka násadky, a až nakonec váha a tvar barelu. '
          'Pokud šipky zavěšují hrot dolů, zkuste delší násadku nebo větší letku. Pokud „plavou“ do stran, zkraťte násadku nebo zmenšete letku. Nepřehánějte to: při každé změně potřebuje ruka čas přizpůsobit se.</p>'
          '<h2>Údržba šipek mezi hrami</h2>'
          '<p>Barel čas od času otřete suchým hadříkem, aby se z rýhování odstranil pot a mastnota, protože kluzký úchop mění hod víc, než byste čekali. Závity občas projděte zrakem: zanesený nebo oděrkou poškozený závit se špatně utahuje a násadka se pak uvolňuje. '
          'Hroty prohlédněte proti světlu, ohnutý hrot poznáte okamžitě. Šipky skladujte hrotem nahoru nebo v pouzdře, nikdy ne volně na dně tašky, kde se letky mačkají. Letky, které se po jemném ohnutí vracejí do původního tvaru, můžete ještě chvíli používat, roztřepené vyměňte.</p>'
          '<h2>Kde hrát a jak šipky přepravovat</h2>'
          '<p>Domácí hra potřebuje pevnou stěnu, ochranu zdi kolem terče a dostatečný odstup, o který se postará <a href="/sipkove-terce/">stojan nebo závěs</a>. Na výlety a turnaje stačí lehké pouzdro, které se vejde do <a href="/sportovni-tasky/">sportovní tašky či ledvinky</a>. '
          'V kempu a na zahradě zafunguje soft sada nebo magnetické provedení, k nimž se hodí i další hry z kategorie <a href="/hry-na-zahradu/">hry na zahradu a pláž</a>. Pro pár hodin zábavy pod střechou je to jednoduchá volba bez velké přípravy.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('mission', 'Mission'), ('harrows', 'Harrows'), ('bull-s', "Bull's"), ('condor', 'Condor'), ('winmau', 'Winmau'), ('designa', 'Designa'), ('target-darts', 'Target'), ('red-dragon', 'Red Dragon'), ('shot', 'Shot'), ('unicorn', 'Unicorn')) + '. '
          'Winmau, Unicorn a Target patří mezi tradiční výrobce terčů a šipek. Harrows, Red Dragon a Mission jsou silné v nabídce letek, násadek a ladicích doplňků, Bull\'s a Condor v dostupném sortimentu pro rekreační hráče, Designa a Shot v doplňcích a sadách pro domácí použití.</p>'
          '<h2>Jak poznat, že je čas na změnu</h2>'
          '<p>Signály jsou jednoduché. Šipky se v terči pravidelně vyklánějí stejným směrem, letky se při dopadu často lámou, šipka odskakuje nebo se při vytahování z terče ohýbá násadka. '
          'Každý z těchto příznaků má obvykle jednoduchou příčinu: nevhodná délka násadky, příliš měkká letka, opotřebovaný hrot nebo špatný úchop. Než začnete měnit barely, vyzkoušejte levnější a rychlejší úpravy na letkách, násadkách a hrotech.</p>'
          '<h2>Pro koho jaký výběr</h2>'
          '<h3>Začátečník</h3>'
          '<p>Stačí pár sad standardních letek, střední násadky z nylonu a trvalejší hroty. Do pouzdra vložte pár náhradních kusů a sledujte, co se opotřebovává nejdřív.</p>'
          '<h3>Pravidelný hráč</h3>'
          '<p>Přejděte na hliníkové nebo kompozitní násadky, kvalitní letky a kroužky proti uvolnění. Vyplatí se mít v zásobě několik tvarů letek a více délek násadek.</p>'
          '<h3>Soutěžní hráč</h3>'
          '<p>Ladí se vše po milimetrech: barely s přesnou hmotností, násadky konkrétní délky, speciální hroty, případně pouzdra na cesty. Stejnou kombinaci si nechte i v záloze, pro případ zlomení.</p>'
          '<h3>Rodiny a zahrada</h3>'
          '<p>Pro děti a rodinné hraní volte soft šipky s elektronickým terčem nebo magnetické varianty. Doplněk zahradního vybavení najdete také ve skupině <a href="/hry-na-zahradu/">hry na zahradu a pláž</a>.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Kupovat hroty a letky bez ověření závitu a typu šipky.</li>'
          '<li>Zkoušet několik změn najednou a pak nevědět, co pomohlo.</li>'
          '<li>Používat zdeformované hroty, které odrážejí nebo se zasekávají.</li>'
          '<li>Nechat šipky volně v tašce bez pouzdra.</li>'
          '<li>Podceňovat zásobu levných drobností: letky, kroužky a plastové hroty se opotřebují nejdřív.</li>'
          '<li>Házet na špatně zavěšený terč. Správné rozměry a vzdálenost popisuje kategorie <a href="/sipkove-terce/">šipkové terče a stojany</a>.</li></ul>'
          '<h2>Další volnočasové hry</h2>'
          '<p>Kdo si zahrál šipky a hledá další zábavu, může zkusit <a href="/lukostrelba/">lukostřelbu</a>, <a href="/discgolf/">discgolf a frisbee</a> nebo <a href="/trampoliny/">trampolíny</a> pro děti. '
          'Společné hraní dovedností přináší podobný pocit soutěže, jen v jiném prostředí.</p>',
    faq=[('Jaký je rozdíl mezi steel a soft šipkami?', 'Steel šipky mají kovový hrot a hrají se na sisalový terč. Soft šipky mají plastový hrot a používají se na elektronické terče. Doplňky obou typů se nemají míchat.'),
         ('Jak často měnit letky?', 'Když se ohnou, roztřepí nebo ztratí tvar. U pravidelných hráčů to může být po několika sezeních, u příležitostných vydrží déle. Držte si zásobu náhradních letek.'),
         ('Jakou délku násadky zvolit?', 'Začněte střední. Krátká násadka dává rychlejší a rovnější let, dlouhá stabilnější. Pokud šipky padají hrotem dolů, zkuste delší, pokud plavou do stran, kratší.'),
         ('Z čeho se vyrábí barely?', 'Nejčastěji z mosazi, nikl-stříbra nebo wolframu. Wolframové barely jsou hustší, takže jsou při stejné váze štíhlejší, mosazné jsou levnější a objemnější.'),
         ('Proč se mi uvolňují násadky a letky?', 'Pomáhají O-kroužky pod násadkou, správně dotažený závit a kvalitnější násadky. Zkontrolujte také, zda není závit poškozený.'),
         ('Jak vybrat tvar letky?', 'Standardní tvar je tolerantní a vhodný na začátek. Úzký (slim) dává přímější let a umožňuje těsné seskupení šipek, kite a pear leží mezi nimi.'),
         ('Hodí se karbonová násadka?', 'Je lehká a pevná, těžko se ohne, a proto je oblíbená u pravidelných hráčů. Pro začátečníka stačí nylon, který je levnější a vydrží běžný provoz.'),
         ('Co patří do pouzdra na šipky?', 'Šipky, náhradní letky a násadky, pár hrotů, kroužky a případně brousek. Rozdělené kapsy brání poškození letek při přepravě.'),
         ('Mohu ostřit ocelové hroty?', 'Jemné obroušení zbaví hrot otřepů, ale přílišné zostření zvyšuje riziko odrazu. Poškozený hrot je lepší vyměnit za nový.'),
         ('Jak porovnat doplňky v obchodech?', 'Na Sportece otevřete konkrétní letku, násadku nebo hrot a porovnejte obchody. U drobností sledujte počet kusů v balení, protože se liší.')],
)
