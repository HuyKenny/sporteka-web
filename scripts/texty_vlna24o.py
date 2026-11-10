"""sporteka.cz — wave 24o (5. 11. 2026): long texts for silnicni-a-gravel-elektrokola, tanecni-obuv, tipi-a-lavvu, detske-stany.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ silnicni-a-gravel-elektrokola
NEW['silnicni-a-gravel-elektrokola'] = dict(long=True,
    title='Silniční a gravel elektrokola: motor, baterie, rám',
    desc='Silniční a gravel elektrokola s lehkým motorem. Jak vybrat rám, převody, pneumatiky a baterii a porovnat nabídky českých obchodů na jednom místě.',
    intro='<p>Silniční a gravel elektrokola spojují sportovní geometrii se štíhlým motorem, který pomáhá do kopce, ale nepůsobí jako kolo z města. Rámy jsou často z hliníku nebo karbonu, baterie bývá schovaná v trubce a hmotnost se pohybuje kolem patnácti kilogramů. Sporteka porovnává nabídky českých obchodů u silničních e-kol s úzkými pneumatikami, gravelových modelů s širším plášťem i kompletních sad s elektronickým řazením. U každého kola uvidíte, ve kterých obchodech je skladem vaše velikost rámu.</p>'
          '<p>V kategorii najdete značky ' + B(('van-rysel', 'VAN Rysel'), ('sava', 'Sava'), ('4ever', '4ever'), ('moma-bikes', 'Moma Bikes'), ('specialized', 'Specialized'), ('olpran', 'Olpran')) +
          '. Pro srovnání mrkněte na <a href="/elektrokola/">elektrokola</a> obecně, <a href="/gravel-kola/">gravel kola</a> a <a href="/silnicni-kola/">silniční kola</a> bez motoru.</p>',
    guide='<h2>Čím se liší od běžného elektrokola</h2>'
          '<p>Klasické trekingové nebo městské e-kolo má silný motor, velkou baterii a pohodlnou polohu vzpřímeného jezdce. Silniční a gravel modely jdou opačným směrem. Motor je menší a pomoc jemnější, baterie menší a rám dlouhý a nižší. Jezdec sedí předkloněný, drží se spodního madla a očekává, že kolo bude reagovat jako sportovní stroj. Pomoc motoru nemá nahradit nohy, má jen vyrovnat kopce a protivítr a prodloužit dosah běžného vyjížďkového dne.</p>'
          '<p>Díky tomu se tato kola často vyplatí lidem, kteří jezdí ve skupině s trénovanějšími kamarády, vracejí se po zranění nebo prostě nechtějí na kopcích zaostávat. Pokud ale hledáte kolo na nákupy, vozíky nebo každodenní dojíždění s brašnami, bude praktičtější <a href="/trekingova-a-mestska-elektrokola/">trekingové a městské e-kolo</a> nebo <a href="/mestska-elektrokola/">městské elektrokolo</a>.</p>'
          '<h2>Silnice nebo gravel</h2>'
          + T(['Vlastnost', 'Silniční e-kolo', 'Gravelové e-kolo'], [
              ['Povrch', 'asfalt a zpevněné silnice', 'asfalt, štěrk, polňačky, lesní cesty'],
              ['Pneumatiky', 'úzké, hladký dezén', 'širší, hrubší dezén, nižší tlak'],
              ['Řídítka', 'klasický ovinutý beran', 'beran s rozšířenými konci pro stabilitu'],
              ['Převody', 'často dvě převodníky vpředu', 'častěji jeden převodník a široká kazeta'],
              ['Poloha', 'agresivnější, nižší hlava', 'mírně vzpřímenější, delší pohodlí'],
              ['Použití', 'dlouhé rychlé vyjížďky', 'dobrodružné trasy a cestování']]) +
          '<p>Silniční geometrie je rychlejší na rovině a v zatáčkách, ale na štěrku je méně odpouštějící. Gravel verze pojme širší pneumatiky, často má závity pro nosiče a blatníky a hodí se na víkendové výlety s brašnami. V nabídce na Sportece najdete obě skupiny. Mezi gravelovými se objevují například modely s motorem Mahle X35 v zadním náboji nebo jednopřevodníkové sestavy SRAM Apex, silniční nabídka zahrnuje karbonové rámy s elektronickým řazením Shimano 105 Di2 či Ultegra Di2.</p>'
          '<h2>Motor, baterie a dojezd</h2>'
          '<p>Motory se u této kategorie dělí na dva hlavní typy. Středový motor u šlapání se pozná podle větší válcové skříně v oblasti pedálů, nabízí přirozenější pocit a lepší rozložení hmotnosti, ale bývá objemnější. Zadní nábojový motor je menší a lehčí, kolo působí skoro jako bez pomoci a snadno se vyjme zadní kolo. U obou řešení je důležité, že v motoru nemusíte slyšet žádný hluk, jinak hovoříme o špatné montáži nebo opotřebení.</p>'
          '<p>Kapacita baterie se uvádí ve watthodinách (Wh) a u sportovních modelů bývá menší než u trekingových e-kol, třeba kolem tří až pěti set Wh. Znamená to kratší dojezd, ale také nižší hmotnost. Skutečný dojezd závisí na stupni pomoci, váze jezdce, povrchu, větru, teplotě a počtu převýšení. Ideální je brát údaj výrobce jako orientační maximum při šetrném režimu. Zimní chlad kapacitu baterie dočasně snižuje, proto ji před chladnou vyjížďkou uchovávejte v teple.</p>'
          '<p>Důležitá je také možnost vyjmutí baterie. Integrovaná baterie v rámu vypadá čistě, ale nabíjíte kolo u zásuvky. Vyjímatelná baterie se nabíjí třeba v bytě a kolo může zůstat ve sklepě. Zeptejte se i na to, zda lze koupit náhradní baterii a jak dlouho je výrobce dodává.</p>'
          '<h2>Rám a velikost</h2>'
          '<p>Materiály rámu se dělí na hliník a karbon. Hliník je levnější, odolný vůči drobným nárazům a snadno se opravuje. Karbon je lehčí a tlumí vibrace z vozovky, vyžaduje ale opatrnější zacházení a po pádu je vhodná kontrola. Hmotnost celého e-kola se u sportovních modelů pohybuje typicky kolem patnácti až dvaceti kilogramů, což stále přitěžuje při nošení do schodů nebo nakládání na nosič.</p>'
          '<p>Velikost rámu se označuje buď písmeny, nebo číslem v palcích či centimetrech. U některých nabídek najdete rozsah výšky jezdce, třeba pro 190 až 205 cm. Rozhodující jsou délka horní trubky, délka představce a výška sedla. Z našich nabídek poznáte, ve kterých obchodech je skladem vaše velikost, což je při tak rozmanitém výběru nejpraktičtější filtr.</p>'
          '<h2>Převody, brzdy a pneumatiky</h2>'
          '<ul><li><strong>Jeden převodník:</strong> jednodušší, lehčí, bez přehazovačky vpředu, rozsah kazety je široký a stačí na většinu terénů.</li>'
          '<li><strong>Dva převodníky:</strong> jemnější odstupňování rychlostí pro rychlou jízdu po silnici, ale více práce se seřízením.</li>'
          '<li><strong>Elektronické řazení:</strong> řadí lehkým dotykem a přesně, vyžaduje ovšem nabíjení vlastního akumulátoru.</li>'
          '<li><strong>Kotoučové brzdy:</strong> standard u sportovních e-kol, protože větší hmotnost a vyšší rychlost zatěžují brzdný systém. Hydraulické ovládání má jemnější citlivost.</li>'
          '<li><strong>Pneumatiky:</strong> u gravelu hrají hlavní roli šířka a dezén. Širší plášť s nižším tlakem pomáhá komfortu, hladký úzký plášť zase ubírá odpor na asfaltu.</li></ul>'
          '<h2>Pro koho jsou tyto modely vhodné</h2>'
          '<ul><li><strong>Silniční nadšenec:</strong> chce delší výlety bez vyčerpání a občas vyjede se skupinou.</li>'
          '<li><strong>Gravel dobrodruh:</strong> hledá kolo na cestování, bikepacking a lesní cesty, kde nepotřebuje pérování.</li>'
          '<li><strong>Dojíždějící sportovec:</strong> do práce ujede delší vzdálenost bez zpocení.</li>'
          '<li><strong>Návrat po pauze nebo zranění:</strong> kolo pomáhá udržet rytmus, aniž by tělo zahlcovalo.</li>'
          '<li><strong>Starší jezdec:</strong> zůstává ve sportovní poloze, ale s menší únavou na kopcích.</li></ul>'
          '<h2>Co k tomu potřebujete</h2>'
          '<p>Vždy kupujte <a href="/cyklisticke-helmy/">cyklistickou helmu</a> a <a href="/silnicni-cyklohelmy/">silniční přilbu</a>, pokud jezdíte rychle po silnici. K večerním jízdám patří <a href="/cyklo-svetla/">světla</a>. Boty se zacvakávacími pedály pomáhají s přenosem síly, vybírejte z <a href="/cyklisticka-obuv/">cyklistické obuvi</a>. Pokud plánujete jezdit v terénu, zvažte také <a href="/horska-elektrokola/">horská elektrokola</a>, která mají více komfortu na hrubém povrchu, i <a href="/skladaci-elektrokola/">skládací e-kola</a> pro kombinaci s vlakem.</p>'
          '<h2>Jak s motorem jezdit chytře</h2>'
          '<p>Nejvíc dojezdu ušetříte tím, že vyšší stupně pomoci necháváte na kopce a protivítr a na rovině jedete v nejnižším režimu. Řadit je vhodné s předstihem, před stoupáním, a v tu chvíli lehce povolit tlak na pedály, aby se nezatěžoval řetěz a kazeta. Při rozjezdu na křižovatce se vyplatí zařadit nižší převod, protože motor reaguje okamžitě a prudký záběr na velkém převodu je nepříjemný i pro hardware. Zvykněte si také na to, že kolo je při stejné rychlosti těžší a brzdná dráha delší, než znáte z lehkého silničáku.</p>'
          '<h2>Výlety a bikepacking</h2>'
          '<p>Gravelové e-kolo je oblíbené na vícedenní cesty, protože motor vyrovná váhu brašen. Plánujte však trasu podle míst, kde lze dobít baterii, třeba v ubytování nebo v kavárně, a vezměte si nabíječku. Rozložte zavazadla nízko a rovnoměrně, aby se kolo nechovalo vratce, a nepřetěžujte rám nad hmotnostní limit, který výrobce udává pro jezdce i náklad. V létě si hlídejte, abyste baterii nenechávali na slunci v zavřeném autě.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Výběr podle dojezdu na papíře:</strong> údaj výrobce se vztahuje na ideální podmínky a malý stupeň pomoci.</li>'
          '<li><strong>Ignorování velikosti rámu:</strong> příliš velký nebo malý rám způsobí bolest zad a nejistou jízdu.</li>'
          '<li><strong>Hmotnost bez ověření:</strong> uvedená váha často platí pro nejmenší velikost bez pedálů.</li>'
          '<li><strong>Nečekané doplňky:</strong> blatníky, nosič a stojánek se u sportovních rámů nemusí dát namontovat.</li>'
          '<li><strong>Zapomenutý servis:</strong> motor i elektronika vyžadují prodejce, který umí diagnostiku a dodá náhradní díly.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Kolo myjte jen mírným proudem vody a vyhněte se přímému tlakovému mytí do ložisek a konektorů. Řetěz pravidelně čistěte a mažte, protože motorová podpora ho zatěžuje víc než u běžného kola. Baterii nabíjejte originální nabíječkou, nenechávejte ji dlouhodobě úplně vybitou a v zimě ji skladujte v suchu při pokojové teplotě, nejlépe s částečným nabitím. Před sezónou zkontrolujte brzdové destičky, tlak v pneumatikách a dotažení šroubů, u karbonu pak momentový klíč s předepsaným utažením.</p>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka nic neprodává, jen ukazuje, kde je produkt k dispozici. Podívejte se na shodu modelu v různých obchodech, velikost skladem, dopravu a podmínky vrácení. Vyplatí se otevřít i popis výrobce, protože u e-kol záleží na rozdílech mezi modelovými ročníky, motorem a verzí převodů. Zkontrolujte záruku na baterii i rám a kde je nejbližší servis. U vybraných produktů sledujte také vývoj ceny a slevy.</p>',
    faq=[
        ('Jaký je rozdíl mezi silničním a gravelovým elektrokolem?', 'Silniční e-kolo má úzké pneumatiky, aerodynamickou polohu a míří na asfalt. Gravelové má širší plášť, často vzpřímenější geometrii a zvládne štěrk i lesní cesty. Gravel je univerzálnější, silniční je rychlejší na rovině.'),
        ('Kolik váží silniční nebo gravelové elektrokolo?', 'Obvykle kolem patnácti až dvaceti kilogramů podle rámu, motoru a baterie. Karbonové rámy a nábojové motory vychází lehčeji, středové motory a velké baterie přidávají hmotnost.'),
        ('Je lepší středový, nebo nábojový motor?', 'Středový motor působí přirozeněji a drží těžiště nízko, ale je větší. Nábojový je lehčí a decentní, jízda bez pomoci je plynulejší. Záleží na tom, zda dáte přednost síle v kopcích, nebo lehkosti a vzhledu.'),
        ('Jak velkou baterii potřebuji?', 'Pro krátké a středně dlouhé výlety stačí kolem tří až pěti set watthodin. Na dlouhé trasy v kopcích zvažte větší nebo vyjímatelnou baterii a možnost dokoupit druhou. Dojezd závisí hodně na stupni pomoci a povrchu.'),
        ('Dá se na silniční e-kolo montovat nosič a blatníky?', 'Záleží na rámu. Gravelové modely mívají závity a výstupky pro nosič i blatníky, silniční je často nemají vůbec. Před koupí si prohlédněte specifikace nebo se zeptejte prodejce.'),
        ('Musím mít přilbu?', 'Zákon vyžaduje přilbu jen u dětí do osmnácti let, ale u rychlé sportovní jízdy ji doporučujeme všem. Zvlášť na silnici s autoprovozem a na štěrku, kde hrozí smyk.'),
        ('Co znamená, že motor pomáhá do pětadvaceti kilometrů v hodině?', 'U elektrokol v běžné legislativě motor přestává pomáhat po dosažení limitní rychlosti. Dál jedete jen vlastní silou. Přesné parametry ověřte u konkrétního modelu a s ohledem na pravidla své země.'),
        ('Jak dlouho vydrží baterie?', 'Kapacita se postupně snižuje podle počtu nabíjecích cyklů, teploty a způsobu skladování. Šetrné zacházení, nabíjení za pokojové teploty a nevybíjení do nuly životnost prodlužuje. Podmínky záruky se u výrobců liší.'),
        ('Mohu s e-kolem jezdit v dešti?', 'Ano, motory a baterie jsou konstruované odolné vůči dešti. Vyhněte se však ponoření a přímému tlakovému proudu vody na konektory a po jízdě kolo osušte.'),
        ('Můžu e-kolo vozit na nosiči na auto?', 'Ano, ale hmotnost kola musí být v limitu nosiče. Vhodné jsou nosiče s kolejnicí a nájezdem, které se nezakládají za rám. Baterii před jízdou vyjměte, odlehčíte kolo a ochráníte ji před vibracemi.'),
        ('Jak poznám správnou velikost rámu?', 'Podívejte se na tabulku výrobce, která váže velikost na výšku postavy nebo délku nohy. Důležitá je i délka horní trubky. Při pochybnostech se vyplatí zkusit kolo osobně nebo kontaktovat prodejce.'),
    ])

# ------------------------------------------------------------------ tanecni-obuv
NEW['tanecni-obuv'] = dict(long=True,
    title='Taneční obuv: salsa, standard, jazz, výběr podpatku',
    desc='Taneční boty na salsu, standardní tance, jazz i moderní tanec. Jak vybrat podrážku, podpatek a velikost a porovnat nabídky českých obchodů.',
    intro='<p>Taneční boty se od běžných liší tím, že musí držet nohu při otočkách, ale zároveň dovolit kluzký pohyb po parketu, a proto nejsou jen módním doplňkem. Typická je pružná podešev, často kožená nebo semišová, a tvar odpovídající stylu tance. Sporteka porovnává nabídky českých obchodů u bot na salsu a latino, na standardní tance, na jazz a moderní tanec a u pomůcek, jako jsou chrániče chodidel. U každého páru vidíte, ve kterých obchodech je skladem vaše velikost.</p>'
          '<p>V kategorii najdete značky ' + B(('burtan', 'Burtan'), ('starever', 'Starever'), ('papillon', 'Papillon'), ('domyos', 'Domyos')) +
          '. K tanečním botám se hodí <a href="/tanecni-obleceni/">taneční oblečení</a>, <a href="/baletni-obuv/">baletní obuv</a> a širší nabídka <a href="/tanec-a-gymnastika/">tance a gymnastiky</a>. Pro příležitostný pohyb mimo sál se hodí i <a href="/bezecka-obuv/">běžecká obuv</a>.</p>',
    guide='<h2>Proč je taneční obuv jiná než sportovní</h2>'
          '<p>Běžná sportovní obuv má pryžovou podrážku s vysokou přilnavostí, protože běh nebo tenis vyžadují jistý kontakt s povrchem. Při tanci je to naopak. Noha se musí otáčet, klouzat a vracet váhu přes špičku nebo patu, a proto potřebuje podrážku z kůže, semiše nebo speciální pružné směsi. Pokud byste tančili v běžné teniskové obuvi, riskujete zkroucené koleno, protože podrážka zachytí parket a tělo se otáčí dál.</p>'
          '<p>Druhým rozdílem je pevnost. Taneční boty mají většinou lehkou konstrukci, jemnou kůži nebo textil a pevný, ale pružný ohyb v oblasti nártu. Dobře sedí na noze jako druhá kůže, takže se vybírají spíš těsněji než běžné boty. Pro začátečníka je to nezvyk, a proto je správná velikost důležitější než jakákoli jiná vlastnost.</p>'
          '<h2>Druhy taneční obuvi podle stylu</h2>'
          + T(['Styl', 'Typické boty', 'Na co dbát'], [
              ['Salsa, bachata, kizomba', 'podpatek střední až vysoký, otevřená nebo uzavřená špička, pásky přes nárt', 'stabilní podpatek, pevné pásky, semišová podešev'],
              ['Standardní tance (valčík, tango)', 'uzavřená špička, podpatek kolem sedmi centimetrů u dam', 'pohodlí při dlouhém tanci, kluzká podešev'],
              ['Latinskoamerické tance', 'otevřená špička, užší podpatek', 'jistota při rychlých otočkách'],
              ['Jazz', 'nízký podpatek nebo bez něj, tvar lehké baleríny', 'pružnost a cit pro podlahu'],
              ['Moderní tanec', 'nízký podpatek, často volnější střih', 'pohyb po špičce a patě, ochrana chodidla'],
              ['Street dance a hip hop', 'taneční tenisky s ohebnou podešví', 'vzduch a tlumení při skocích']]) +
          '<p>Z nabídky vyniká značka Burtan, která má v katalogu boty na salsu (například modely Havana nebo Estepona), standardní tance (Vienna Ballroom, Toledo), jazz (Broadway) i moderní tanec (New York). Dále se objevují taneční boty Santiago a lehká taneční obuv Papillon. Mezi doplňky najdete chrániče chodidel pro moderní tanec, které se nosí místo bot.</p>'
          '<h2>Podpatek: výška a tvar</h2>'
          '<p>Výška podpatku se u dámských bot obvykle uvádí v centimetrech. Nižší (kolem pěti centimetrů) se hodí pro začátečnice a delší tanec, vyšší (kolem sedmi a půl centimetru) pro zkušené latino a společenský tanec, kde se tančí na špičkách. Podpatek by neměl být příliš tenký, protože stabilita se pod náporem otáček zhoršuje. U pánských bot bývá podpatek nízký a široký, jehož účelem je zlepšit rovnováhu při tanci v uzavřené poloze.</p>'
          '<p>Vyšší podpatek mění rozložení váhy, tlačí na přednoží a zkracuje lýtkové svaly. Začátečnice proto ať nezačínají nejvyšším, pokud nemají zkušenost s obuví podobného typu. Postupný přechod od nižšího k vyššímu snižuje riziko podvrtnutí.</p>'
          '<h2>Podešev: semiš, kůže, guma</h2>'
          '<ul><li><strong>Semiš:</strong> klasika pro parket. Drží, ale klouže přiměřeně. Časem se zplihne a doporučuje se ho kartáčovat drátěným kartáčem, aby si zachoval strukturu.</li>'
          '<li><strong>Kůže:</strong> kluznější, vhodná pro hladké povrchy a mazlavé otočky, hůře se chová na vlhku.</li>'
          '<li><strong>Syntetika a pryž:</strong> odolná, ale pro společenský tanec často příliš lepivá. Hodí se pro street dance a trénink na tvrdých plochách.</li>'
          '<li><strong>Dělená podešev:</strong> flexibilní, usnadňuje práci nohy mezi špičkou a patou, typická pro jazz a moderní tanec.</li></ul>'
          '<h2>Velikost a padnutí</h2>'
          '<p>Taneční boty se zkoušejí s tím, jaké ponožky nebo punčochy budete nosit. Prsty by se měly špičky téměř dotýkat, nesmějí však být stlačené. Pata nesmí vyskakovat, jinak boty rychle sklouznou a noha ztratí stabilitu. Pásky přes nárt musí sedět pevně, ale neškrtit. U dámských bot s vyšším podpatkem se noha při tanci posouvá dopředu, což je důvod, proč je vhodné nevybírat o číslo větší velikost.</p>'
          '<p>Velikosti se u různých značek liší. Jedna firma používá evropské číslování, druhá britské, u dětí zase míry v centimetrech. Proto otevřete u produktu tabulku výrobce a změřte nohu od paty po nejdelší prst. Ve srovnání na Sportece najdete u každého páru obchody, kde je ještě vaše číslo skladem, což u sezónních tanečních bot nebývá samozřejmost.</p>'
          '<h2>Povrch sálu a chodidlo</h2>'
          '<p>Stejné boty se chovají jinak na dřevěném parketu, na lepené podlaze a na kamenné dlažbě. Hladký lakovaný parket bývá kluzký, takže semiš dobře drží, zatímco na zaprášené podlaze se podešev rychle zašpiní a klouže příliš. Taneční sály proto bývají udržované a boty se v nich nosí výhradně uvnitř. Při tanci na tvrdém betonu nebo dlažbě pomáhá vložit do boty měkkou stélku, která tlumí nárazy a chrání klouby. Kdo tančí naboso nebo v ponožkách, ocení <a href="/barefoot-obuv/">barefoot obuv</a> pro běžný den, ale na parket patří lehká taneční bota.</p>'
          '<h2>Puchýře, otlaky a bolest nohou</h2>'
          '<p>Nové taneční boty je dobré rozchodit doma několik hodin před prvním tancem. Kožené modely se přizpůsobí tvaru nohy rychleji než syntetické. Pokud tlačí na patě, pomůže náplast nebo gelová podložka, na přednoží zase měkká vložka pod kuličku. Dlouhodobé bolesti kotníků, kolen nebo bérce nemají být normální a patří k lékaři nebo fyzioterapeutovi, ne k dalšímu pokusu o výdrž. Boty s nízkým podpatkem rozkládají zátěž rovnoměrněji a jsou při dlouhé hodině šetrnější.</p>'
          '<h2>Dámské, pánské a dětské provedení</h2>'
          '<p>Dámské boty jsou typicky otevřenější, s pásky a vyšším podpatkem, a pánské uzavřené, s nízkým podpatkem a pevnější špičkou. Dětské modely bývají měkčí a jednodušší, aby nebránily přirozenému vývoji nohy. Rostoucí dítě potřebuje větší velikost každých pár měsíců, takže se vyplatí vybírat levnější bezpečný pár a nehonit se za značkou. Na cestu do tanečního kurzu myslete i na přezutí, v zimě pomůže <a href="/zimni-obuv/">zimní obuv</a>, v hale zase <a href="/salova-obuv/">sálová obuv</a> při ostatních pohybových kroužcích.</p>'
          '<h2>Pro koho jsou které boty</h2>'
          '<ul><li><strong>Začátečnice na taneční kurz:</strong> střední podpatek, uzavřená špička, pohodlná stélka.</li>'
          '<li><strong>Tanečník salsy:</strong> pružná podešev, stabilní podpatek a pásky, které drží nohu při rychlých otočkách.</li>'
          '<li><strong>Soutěžní pár:</strong> speciální boty pro standardní a latinskoamerické tance, často na míru podle velikosti nohy.</li>'
          '<li><strong>Děti na kroužek:</strong> měkké jazzové nebo gymnastické cvičky, které se hodí pro začátečníky a rostoucí nohu, K domácímu procvičování se hodí <a href="/fitness-pomucky/">fitness pomůcky</a>.</li>'
          '<li><strong>Dospělí na kondiční hodiny:</strong> jazz a moderní boty s lehkou podešví.</li></ul>'
          '<h2>Péče o taneční boty</h2>'
          '<p>Taneční obuv se nenosí venku, protože špína, štěrk a voda zničí semiš i kůži. Do tanečního sálu nebo kurzu si vezměte boty zvlášť v tašce a přezujte se před vstupem na parket. Po tréninku je nechte vyschnout při pokojové teplotě, nikoli na topení, a vložte do nich papír, který nasákne vlhkost. Semišovou podrážku ošetřete drátěným kartáčem, vyhněte se mastným krémům. Kožené svršky občas přetřete jemným krémem a lehce vyleštěte. Správně uložené boty drží tvar a vydrží víc sezón. Doplňte je o <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>, třeba taštičku nebo vložky.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li><strong>Boty příliš volné:</strong> noha klouže, hrozí podvrtnutí a puchýře.</li>'
          '<li><strong>Chybný druh podešve:</strong> lepivá guma na parketu brzdí otočky a namáhá kolena.</li>'
          '<li><strong>Příliš vysoký podpatek na první hodinu:</strong> únava přichází po půl hodině a technika trpí.</li>'
          '<li><strong>Nošení venku:</strong> semišová podešev je pak za pár dnů znehodnocená.</li>'
          '<li><strong>Nesprávný styl:</strong> salsové boty se na standardní tance hodí jen omezeně a naopak.</li></ul>'
          '<h2>Jak využít srovnání na Sportece</h2>'
          '<p>Sporteka prodej nezajišťuje, jen shromažďuje nabídky českých obchodů u stejných párů. Porovnejte si dopravu, možnost výměny velikosti a to, zda obchod boty vyfotil na noze, ne jen v katalogu. U bot, které dosud nemáte vyzkoušené, volte obchod, jenž umožňuje vrácení, a před prvním tancem je vyzkoušejte doma na koberci, aby podešev zůstala čistá. Pokud kupujete pro začátečníka, zvažte i <a href="/sportovni-obuv/">sportovní obuv</a> na kondiční přípravu a <a href="/treninkova-obuv/">tréninkovou obuv</a> na posilování mimo sál.</p>',
    faq=[
        ('Čím se taneční boty liší od běžných bot?', 'Mají lehkou konstrukci, pružný ohyb a speciální podešev, nejčastěji koženou nebo semišovou, která dovoluje klouzání a otáčení. Běžná gumová podrážka při tanci zachytává parket a zatěžuje kolena.'),
        ('Jaký podpatek zvolit jako začátečnice?', 'Nižší až střední podpatek, kolem pěti centimetrů, který je stabilní a pohodlný při delším tanci. Vyšší podpatek se vyplatí teprve s technikou a silnějším lýtkem.'),
        ('Mohu v tanečních botách chodit venku?', 'Nedoporučujeme to. Venkovní povrch semišovou podešev rychle opotřebuje a zašpiní. Boty noste jen v sále a venku se přezujte.'),
        ('Jak poznám správnou velikost?', 'Změřte nohu od paty po nejdelší prst a porovnejte s tabulkou výrobce. Taneční boty mají sedět těsně, ale nesmí tlačit, a pata nesmí při kroku vyskakovat.'),
        ('Jak čistit semišovou podrážku?', 'Jemným drátěným kartáčem, kterým pročešete chlupy zpět. Nepoužívejte vodu ani mastné přípravky, protože semiš ztvrdne a ztratí kluznost.'),
        ('Hodí se boty na salsu i na standardní tance?', 'Částečně. Salsové boty mívají otevřenou špičku a nižší stabilní podpatek, standardní mají uzavřenou špičku a jiný tvar. Pro příležitostný tanec může stačit jedny, soutěžní tanečníci mají obvykle speciální páry.'),
        ('Co jsou chrániče chodidel?', 'Je to měkký návlek, který chrání přední část chodidla při tanci naboso, zejména v moderním tanci. Umožní otáčky po špičce a snižují tření o podlahu.'),
        ('Jak dlouho taneční boty vydrží?', 'Záleží na četnosti tance, povrchu a péči. Při pravidelném používání se semiš opotřebí dřív než svršek, ale podrážku lze někdy doplnit. Správné skladování a kartáčování životnost prodlužuje.'),
        ('Musí mít dětské taneční boty podpatek?', 'Pro nejmenší děti ne. Začínají v měkkých cvičkách nebo jazzových botách bez podpatku a teprve později přecházejí na nízký podpatek podle doporučení trenéra.'),
        ('Kolik párů tanečních bot potřebuji?', 'Pro kurz a občasný ples stačí jeden všestranný pár. Kdo tančí více stylů, časem přidá boty na latino a standard zvlášť. Soutěžní tanečníci mívají i záložní pár a boty na trénink.'),
        ('Jak rozchodit nové taneční boty?', 'Nosit je doma několik hodin na koberci a postupně prodlužovat dobu. Tlačící místa lze ochránit gelovou vložkou nebo náplastí. Boty nikdy nenoste hned na dlouhý večer bez zkoušky.'),
        ('Je lepší koupit boty ve stejné velikosti jako běžné?', 'Ne nutně. Taneční boty sedí těsněji a velikost se u výrobců liší, proto vždy porovnejte délku nohy s tabulkou. Při váhání mezi dvěma čísly volte menší, pokud neškrtí a prsty se nepřekrývají.'),
        ('Mohu tančit v teniskách?', 'Na street dance ano, protože se tančí na pevnější podložce. Pro společenský a latinskoamerický tanec jsou tenisky nevhodné kvůli přilnavosti podešve a riziku zkroucení kolena.'),
    ])

# ------------------------------------------------------------------ tipi-a-lavvu
NEW['tipi-a-lavvu'] = dict(long=True,
    title='Týpí a lavvu: tvar, plátno, kamna, výběr stanu',
    desc='Týpí, teepee a lavvu stany pro skupiny a glamping. Jak vybrat velikost, plátno, kamna a postavení a porovnat nabídky českých obchodů.',
    intro='<p>Týpí a lavvu jsou kuželové stany s jedním středem a dostatkem místa pro skupinu. Evropské lavvu pochází od severských pastevců a týpí od severoamerických indiánů. Dnes obě varianty používají rodiny, skauti, táborníci i ti, kdo chtějí glamping u domu. Sporteka porovnává nabídky českých obchodů u bavlněných i polyesterových modelů, od menších stanů pro čtyři osoby po obří pro dvanáct lidí. U každého produktu uvidíte obchody, ceny a dostupnost, takže snadno poznáte nejvýhodnější nabídku.</p>'
          '<p>V kategorii najdete značky ' + B(('skandika', 'Skandika'), ('helsport', 'Helsport'), ('condor', 'Condor'), ('redcliffs', 'RedCliffs'), ('vidaxl', 'Vidaxl'), ('easy-camp', 'Easy Camp')) +
          '. Vybírat můžete i mezi <a href="/stany/">stany</a> obecně, <a href="/rodinne-stany/">rodinnými stany</a> a <a href="/turisticke-stany/">turistickými stany</a>.</p>',
    guide='<h2>Týpí, teepee a lavvu: co je co</h2>'
          '<p>Slovo týpí označuje kuželový stan se zakončeným vrcholem, vyvýšeným komínovým otvorem a často dvěma větracími křídly. Podobný tvar, jen s kratší výškou a prostředním ohništěm, má severské lavvu, jež se tradičně stavělo z plachet a tyčí a mívalo otvor nahoře pro kouř. V obchodech se oba názvy často míchají, proto se do jedné kategorie dostávají i modely označené teepee nebo Tee-pee. Základní princip je ale společný: jedna tyč uprostřed nebo svazek tyčí tvoří kužel, který se rozevírá do kruhového půdorysu.</p>'
          '<p>Kužel má několik výhod. Dobře odvádí déšť a vítr, má vysoký střed pro stání a nabízí velký objem a vzdušný pocit uvnitř. Nevýhody jsou menší využitelný prostor u stěn, složitější uložení lůžek a obvykle vyšší hmotnost než u kupolového turistického stanu. Podívejte se i na <a href="/expedicni-stany/">expediční stany</a> a <a href="/pristresky-a-party-stany/">přístřešky a party stany</a>, pokud potřebujete jiný typ konstrukce.</p>'
          '<h2>Velikost a kapacita</h2>'
          + T(['Označení modelu', 'Orientační kapacita', 'Použití'], [
              ['Hetta 335 (čtyři osoby)', 'malá skupina, nižší stojná výška', 'rodinný víkend, malý tábor'],
              ['Hetta 460 (šest osob)', 'větší rodina nebo skupina', 'dovolená, glamping'],
              ['Comanche 400 (osm osob)', 'skupina přátel', 'festival, tábor'],
              ['Kota 550 (dvanáct osob)', 'velká skupina nebo oddíl', 'skautský tábor, společenský stan'],
              ['Finnmark Lavvu 6 až 8', 'větší tým nebo rodina', 'severské kempování, zimní výlet'],
              ['Seton 320 a 440 g/m²', 'odlišná tloušťka plátna', 'stálé stanoviště, dlouhý pobyt']]) +
          '<p>Kapacita u týpí se uvádí pro spaní, ale u kuželového tvaru je skutečný využitelný prostor menší než kruh. Počítejte raději s polovinou uvedeného počtu, pokud chcete mít kromě lůžek i zavazadla a místo pro stůl. Důležitá je i stojná výška, která v nabídce dosahuje u větších modelů přes tři metry, takže se uvnitř můžete pohybovat vzpřímeně.</p>'
          '<h2>Plátno: bavlna, polybavlna a polyester</h2>'
          '<p>Materiál stanu rozhoduje o komfortu, hmotnosti i péči. Bavlněné plátno dýchá, snižuje kondenzaci, v létě ochladí a v zimě je příjemnější na dotek. Je však těžší, pomalu schne a po dlouhém uskladnění mokré může plesnivět. Polyesterové provedení je lehčí, rychleji schne a lépe odolává slunci, ale hůře odvádí vlhkost, takže uvnitř se kondenzuje víc. Směsné polybavlny kombinují vlastnosti obou a patří k oblíbeným volbám. Číslo ve značení, třeba 320 nebo 440 g/m², udává gramáž tkaniny. Vyšší gramáž je silnější a těžší.</p>'
          '<p>U názvů s koncovkou Protect výrobce většinou odkazuje na vodovzdorné nebo ochranné ošetření materiálu. Konkrétní vlastnosti si vždy přečtěte v popisu u produktu, protože každá značka tuto zkratku používá po svém. Podlaha bývá u týpí buď přišitá, nebo oddělená. Bez podlahy lze v modelech, které výrobce výslovně určuje k topení (obvykle bavlněných), postavit kamna s ochranou plátna; v polyesterových stanech oheň ani kamna nepoužívejte. S podlahou je prostor čistší a suchý.</p>'
          '<h2>Kamna, oheň a bezpečnost</h2>'
          '<p>Hlavním lákadlem lavvu a týpí je možnost topit uvnitř, protože komínový otvor odvádí kouř. Helsport, který patří mezi severské značky, nabízí v kategorii i lavvu spolu se stanovými kamny. Kamna musí mít stabilní podložku, protipožární průchod či ochranu plátna a komínek pevně vyvedený. Nikdy topte na holé trávě v suchu a nenechávejte oheň bez dozoru. Uvnitř stanu je navíc nebezpečný oxid uhelnatý, takže větrání musí fungovat, vyplatí se detektor CO a ve stanu s hořícími kamny nikdy nespěte, hrozí otrava. Plátno může být ošetřené proti hoření, ale ověřte si to u výrobce; žádné plátno není nehořlavé. Pokud nevíte, zda je model pro topení určený, raději se zeptejte výrobce nebo prodejce a topení nezkoušejte.</p>'
          '<h2>Stavba a ukotvení</h2>'
          '<ul><li><strong>Najděte rovnou plochu:</strong> bez kamenů, kořenů a prohlubní, ideálně mírně vyvýšenou, aby voda odtékala.</li>'
          '<li><strong>Rozložte stan a zakolíkujte obvod:</strong> kolíky zatloukejte šikmo od stanu, aby se kuželová stěna napnula rovnoměrně.</li>'
          '<li><strong>Zvedněte střed:</strong> u modelů s jednou tyčí je lepší práce ve dvou lidech, u větších typů ve třech.</li>'
          '<li><strong>Dopněte lana:</strong> bouřkový vítr bez lan trhá kolíky, což platí i pro kuželové stany.</li>'
          '<li><strong>Zkontrolujte vrchol:</strong> otvor či komín nesmí být vystavený přímému dešti a vítr z něj nemá foukat dovnitř.</li></ul>'
          '<p>Při bourání postupujte opačně, kolíky vytahujte bez páčení za plátno a stan skládejte do ležaté čtvrtky, aby se dal vrátit do vaku bez zalomení. Označte si, který kolík patří ke kterému lanu, a nechte si u sebe náhradní lanko a kladivo či palici, protože většina modelů nemá v balení příliš rezervních dílů.</p>'
          '<h2>Léto, zima a mezisezóna</h2>'
          '<p>V létě týpí oceníte pro vysoký střed, kde stoupá teplý vzduch, a pro možnost zvednout spodní okraj plátna a pustit dovnitř průvan. Stan na slunci může být přesto horký, proto ho stavte do stínu a větrací otvory nechte otevřené. V přechodném období přijde vhod podlaha a vnitřní vrstva, která snižuje chlad od země. V zimě se kužel osvědčí díky malé ploše povrchu vůči objemu a možnosti topit, ale sníh na plátně musíte pravidelně smetat, jinak váha zatěžuje tyč i švy. Zimní kempování si žádá také silnější spací pytel a izolační podložku, protože i vyhřátý stan má u země chladno.</p>'
          '<h2>Pro koho se hodí</h2>'
          '<ul><li><strong>Skauti a oddíly:</strong> velký společný prostor na hry, setkání a deštivé večery.</li>'
          '<li><strong>Rodiny a přátelé:</strong> jeden stan místo pěti malých, k němuž se hodí <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</li>'
          '<li><strong>Glamping:</strong> pohodlné lůžko, koberec a světla, viz <a href="/kemping/">kempingové vybavení</a>.</li>'
          '<li><strong>Severské zimní výlety:</strong> lavvu s kamny pro lyžaře a rybáře.</li>'
          '<li><strong>Zahradní stan:</strong> stálá obytná místnost, kterou lze stavět na několik týdnů.</li></ul>'
          '<h2>Pro koho se nehodí</h2>'
          '<p>Týpí není stan pro batůžkáře, protože i menší model váží víc než dvoumístný turistický. Nehodí se pro jednodenní přesun a strmé terény, kde chybí rovné místo. V extrémním větru a v horách s ostrými povětrnostními výkyvy je bezpečnější tunelový nebo kupolový expediční model. Pokud hledáte spíš lehké řešení, podívejte se do kategorie <a href="/turisticke-stany/">turistických stanů</a>.</p>'
          '<h2>Spaní uvnitř a vybavení</h2>'
          '<p>Kuželový tvar nutí k jinému uspořádání než obdélníkový stan. Lůžka se skládají paprskovitě, hlavami ke stěně, nohy směřují ke středu. Střed pak zůstane volný pro kamna, stůl nebo ohniště. K lůžku patří <a href="/spaci-pytle/">spací pytel</a> s vhodným komfortním rozsahem a <a href="/karimatky-a-matrace/">karimatka nebo matrace</a>, protože i v létě táhne od země. Při vaření uvnitř používejte jen vhodné <a href="/varice-a-kartuse/">vařiče</a> s pevným stojánkem a dostatečným větráním, nejlépe však vařte před stanem.</p>'
          '<h2>Péče, sušení a skladování</h2>'
          '<p>Stan po dešti vždy rozložte a nechte úplně vyschnout, než ho složíte do vaku. Bavlněné plátno může plesnivět už po několika dnech ve vlhku, mívá charakteristický zápach a vrásčitý povrch. Při čištění použijte měkký kartáč a vlažnou vodu, bez agresivních přípravků, které poškodí impregnaci. Nové bavlněné týpí se někdy před prvním použitím zavlhčí, aby se vlákna smrštila a plátno se utěsnilo, ale postup vždy ověřte u výrobce. Kolíky a tyče očistěte od hlíny, zkontrolujte švy a v zimě sklad v suchu a v tmavé místnosti.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Podceněná hmotnost:</strong> těžký bavlněný model se nevejde do malého auta a stavba trvá déle.</li>'
          '<li><strong>Kapacita podle nálepky:</strong> uváděný počet platí pro samotné spaní, na zavazadla a sezení počítejte s rezervou.</li>'
          '<li><strong>Chybějící větrání:</strong> polyester bez průvanu rychle zkondenzuje a ráno je uvnitř vlhko.</li>'
          '<li><strong>Špatné ukotvení:</strong> kužel působí jako plachta a větru se musí stavět na odpor.</li>'
          '<li><strong>Topení bez zkušeností:</strong> oheň a kamna v plátně vyžadují přísná bezpečnostní pravidla.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Na Sportece porovnáte nabídky s přihlédnutím k tomu, zda je v ceně i tyč, kolíky a podlaha. Týpí se často prodává jako samostatný stan bez příslušenství, jak ukazuje popis modelu Condor Seton, a proto nezapomeňte přičíst kolíky, lana a případně vnitřní stan. Sledujte velikost balení, protože těžké modely se dopravují nadměrně. Pokud potřebujete stanový komplet, hledejte v <a href="/stanove-doplnky/">stanových doplňcích</a>.</p>',
    faq=[
        ('Čím se liší týpí od lavvu?', 'Týpí má strmější kužel s kouřovými klapkami, lavvu je nižší a širší a staví se na šikmých tyčích. Oba typy mají nahoře otvor pro kouř. V obchodech se názvy míchají, proto sledujte popis a rozměry.'),
        ('Kolik lidí se do týpí vejde?', 'Na papíře podle označení modelu, ale u kuželového tvaru je využitelný prostor menší. Pro pohodlí počítejte s rezervou oproti uvedenému počtu lůžek, pokud chcete ve stanu i sedět a ukládat vybavení.'),
        ('Je bavlněné plátno lepší než polyester?', 'Bavlna lépe reguluje vlhkost a vzduch, ale je těžší a pomalu schne. Polyester je lehčí a rychleji schne, ale víc kondenzuje. Záleží na tom, zda stavíte stan na delší dobu, nebo ho často přenášíte.'),
        ('Dá se v týpí topit?', 'U modelů, které jsou na to určené, ano. Je třeba stabilní kamna s ochranou plátna, komínek a dobré větrání. Nikdy nezapomínejte na oxid uhelnatý a nespěte s hořícím topením.'),
        ('Jak se týpí staví?', 'Rozloží se na rovnou plochu, zakolíkuje se obvod, zvedne se střed a stan se dopne lany. Většinu malých modelů zvládnou dva lidé, velké vyžadují více pomocníků.'),
        ('Je týpí vhodné do deště a větru?', 'Kuželový tvar dobře odvádí déšť a unese vítr, pokud je stan správně ukotven a vypnut. Při bouřce a silném větru je bezpečnější stan zbourat nebo zajistit lany.'),
        ('Má týpí podlahu?', 'Záleží na modelu. Některé mají přišitou podlahu, jiné jsou bez ní, což usnadňuje topení a stavbu kamen. Popis u produktu napoví, zda je podlaha součástí.'),
        ('Dá se týpí používat celoročně?', 'Bavlněná verze s kamny snese i chladnější měsíce. Pro hluboké mrazy a sněhovou zátěž je potřeba model určený pro zimu. Jinak je nejpohodlnější od jara do podzimu.'),
        ('Můžu týpí postavit na zahradě trvale?', 'Dočasně ano, ale bavlna dlouhodobým deštěm, sluncem a vlhkostí stárne. Pokud ho necháte stát celé léto, kontrolujte napnutí, větrání a stav švů a pravidelně plátno vysušte.'),
        ('Kolik váží větší týpí?', 'Hmotnost se liší podle plátna a velikosti, často jde o desítky kilogramů u velkých bavlněných modelů. Pro přepravu autem to obvykle nevadí, na delší pěší přesun se nehodí.'),
        ('Jak se stará o nové bavlněné týpí?', 'Před prvním použitím si přečtěte pokyny výrobce, plátno se někdy zavlhčí, aby se vlákna uzavřela. Po každém použití stan důkladně vysušte a nepoužívejte agresivní čisticí prostředky.'),
        ('Jak týpí skladovat?', 'Zcela suché, ve vaku na suchém a tmavém místě, bez sevření a daleko od zdrojů vlhkosti. Mokré plátno plesniví už po několika dnech.'),
    ])

# ------------------------------------------------------------------ detske-stany
NEW['detske-stany'] = dict(long=True,
    title='Dětské stany: hrací teepee, domeček, bezpečnost',
    desc='Dětské hrací stany a teepee do pokoje i na zahradu. Jak vybrat velikost, materiál a bezpečný tvar a porovnat nabídky českých obchodů.',
    intro='<p>Dětský stan je malé útočiště na hraní, čtení nebo odpočinek. Většinou jde o hrací domeček do pokoje či na zahradu, ne o stan na spaní v přírodě. Nejčastěji se prodávají teepee v dětské velikosti, tvarované do kuželu s textilním pláštěm a dřevěnými nebo plastovými tyčkami, a hrací stany s tunelem či zámkem. Sporteka porovnává nabídky českých obchodů u dětských teepee, hracích hradů a stanů s motivy, aby rodiče snadno viděli, ve kterém obchodě stan koupí. U každého produktu najdete obchody, dostupnost a slevy.</p>'
          '<p>V kategorii najdete značky ' + B(('springos', 'Springos'), ('master', 'Master'), ('trespass', 'Trespass')) +
          '. Pro skutečné kempování se podívejte do <a href="/stany/">stanů</a> a <a href="/rodinne-stany/">rodinných stanů</a>.</p>',
    guide='<h2>Hrací stan není kempingový stan</h2>'
          '<p>Dětské hrací stany jsou lehké, textilní a určené pro několik hodin her, nikoli pro noc venku v dešti. Plášť je obvykle z tenké bavlny nebo polyesterové tkaniny, které odolávají omyvatelnému špinění, ale ne dlouhému mokru. Nemají vodovzdorný plášť, hluboké kotvení ani stabilní konstrukci pro vítr. Pokud plánujete s dětmi přespání pod širým nebem, vybírejte raději <a href="/turisticke-stany/">turistický stan</a> nebo <a href="/rodinne-stany/">rodinný stan</a>.</p>'
          '<p>Hrací stany naopak splní všechno, co na nich děti milují. Mají tajné místo, kam se zalezou, a rodiče mají klid, že je dítě na bezpečném místě. Skvěle fungují jako herní kout v dětském pokoji, jako čtenářský koutek nebo jako stanový sleep-over při návštěvě kamarádů.</p>'
          '<h2>Druhy dětských stanů</h2>'
          + T(['Druh', 'Popis', 'Hodí se pro'], [
              ['Teepee stan', 'kuželový tvar, tyče a textilní plášť, často s otvorem na okénko', 'pokoj, čtení, chvíle odpočinku'],
              ['Hrací domeček', 'pevnější tvar s dveřmi a okny', 'zahrada nebo větší pokoj'],
              ['Hrací zámek', 'tvar hradu s věžičkami', 'děti, které si hrají na rytíře a princezny'],
              ['Tematický stan', 'indiáni, vesmír, zvířata, hvězdy', 'tematické hry a pokojíčky'],
              ['Tunel a vlezení', 'sada stanu s propojovací chodbou', 'aktivní hra a vymýšlení světů'],
              ['Stan s tunelem', 'dva stany propojené chodbou na lezení', 'rodiny s více dětmi']]) +
          '<p>V katalogu mají největší zastoupení teepee stany Springos v barevných vzorech, tedy s hvězdami, puntíky či v růžovém a šedém provedení. Značka Master nabízí hrací stany s motivy, například Pinky, Sauru nebo Indian, a Trespass hrací zámek. Teepee působí nejklidněji, hrací zámek a domeček nejvíc podněcují fantazii.</p>'
          '<h2>Velikost a věk dítěte</h2>'
          '<p>Při výběru začněte věkem a počtem dětí. Pro batole stačí nižší stan s širokým vstupem, aby se dítě mohlo samo dostat dovnitř a ven. Předškolák ocení stan, do něhož se vejde s kamarádem, a školák chce spíš prostor pro čtení a hry. Ve stanu by mělo být možné se otočit, ležet nebo sedět a mít při sobě deku a polštáře. U kuželových stanů se zmenšuje prostor směrem nahoru, takže stojná výška platí jen uprostřed.</p>'
          '<p>Před koupí si změřte místo. Dětské teepee potřebuje vedle sebe volnou plochu, aby se nedotýkalo nábytku, a u zahradní verze stabilní rovný povrch. Vždy se podívejte na údaj o výšce a průměru dna a porovnejte ho s rozměrem pokoje. Příliš velký stan zabere polovinu pokoje a v kuželovém tvaru se stojná výška směrem nahoru rychle zužuje.</p>'
          '<h2>Materiál a konstrukce</h2>'
          '<ul><li><strong>Bavlna:</strong> příjemná na dotek, prodyšná, vhodná dovnitř. Hůř se čistí a může se srážet.</li>'
          '<li><strong>Polyester:</strong> lehký, snadno se myje a rychle schne, ale může být méně příjemný na dotek.</li>'
          '<li><strong>Dřevěné tyče:</strong> pevné a stabilní, u kvalitních modelů hladké a bez třísek, ale těžší.</li>'
          '<li><strong>Plastové nebo kovové trubky:</strong> lehčí, pružné, často s plastovými spojkami.</li>'
          '<li><strong>Dno a okénko:</strong> stan s podlahou je čistší, okénko s moskytiérou nebo síťkou pomáhá s větráním.</li></ul>'
          '<h2>Bezpečnost: na co dát pozor</h2>'
          '<p>Dětský stan je hračka a měl by se chovat podle toho. Hledejte hladké hrany tyčí, zaoblené spoje a pevné zakončení. Textilie by měla být bez drobných dílů, které by dítě mohlo ukousnout, a výrobek nemá mít na viditelných místech ostré kování. Při používání v pokoji nikdy neumisťujte do stanu svíčky, lampy s horkým povrchem ani kamna a světelné řetězy volte jen takové, které jsou určené pro děti. Elektrické prodlužovačky vedoucí do stanu představují nebezpečí zakopnutí i přehřátí. Nechávejte dítě ve stanu hrát si pod dohledem, hlavně u batolat, a vstup nikdy nezamykejte ani neblokujte.</p>'
          '<p>Na zahradě stan pevně zakotvěte nebo zatěžkejte, aby ho nezvedl vítr, a nenechávejte ho venku přes noc ani během bouřky. Stan na slunci rychle vyhřeje, takže děti ve vedru hlídejte a dopřejte jim pití a stín. Kontrolujte stav tyčí, spojek a švů a poškozený stan raději vyřaďte.</p>'
          '<h2>Kde stan postavit v bytě</h2>'
          '<p>Nejlepší je stabilní rovná podlaha mimo pohyb dospělých, ideálně v dětském pokoji nebo v obývacím koutě. Pod stan patří koberec nebo měkká podložka, která tlumí pády a chrání parkety před škrábanci od tyčí. Nestavte ho přímo u topení, u okna nebo u schodů. Mějte na paměti, že kuželový stan se při opření o něj kymácí, proto jej umístěte tak, aby dítě nemohlo narazit do ostrého rohu nábytku. Stan na pevném místě funguje jako stálý koutek, ale pokud pokoj potřebujete, vyplatí se ho složit do vaku.</p>'
          '<h2>Hra, která rozvíjí</h2>'
          '<p>Děti ve stanu rády vymýšlejí příběhy, uklízejí hračky do svého domova, hrají na obchod nebo na kempování. Stan podporuje samostatnou hru i společnou hru sourozenců. Kdo chce hru podpořit, může dítěti doplnit knížky, plyšové hračky a baterku na hraní. Doplňky nemusí být drahé. Obyčejná deka a polštář z pokoje často stačí a dítě pozná, že stan je jeho místo.</p>'
          '<h2>Jak stan využít</h2>'
          '<ul><li><strong>Čtenářský koutek:</strong> měkká deka, polštáře, malá knihovnička a stolní lampa mimo dosah stanu.</li>'
          '<li><strong>Odpočinek a uklidnění:</strong> klidné místo pro chvíle, kdy se dítě potřebuje oddělit od hluku.</li>'
          '<li><strong>Hra na indiány a výpravy:</strong> doplňky jako čelenky, mapy a baterka.</li>'
          '<li><strong>Pyžamová party:</strong> pár dětí s <a href="/detske-spacaky/">dětskými spacáky</a> a svačinou.</li>'
          '<li><strong>Zahradní hrad:</strong> kombinujte se <a href="/kolobezky/">koloběžkami</a> a <a href="/detska-kola/">dětskými koly</a> jako součást odpoledne venku.</li></ul>'
          '<h2>Stan jako dárek</h2>'
          '<p>Dětský stan je oblíbený dárek k narozeninám i Vánocům, protože zabaví děti na delší dobu a nepotřebuje baterie. Při výběru zvažte vkus dítěte. Dívky často sáhnou po růžovém teepee nebo hradu, chlapci po indiánském nebo vesmírném motivu, ale mnoho dětí chce neutrální šedou nebo bílou s hvězdami, která se hodí do každého pokoje. Zvažte i to, kolik dětí bude stan používat, zda ho budou sdílet sourozenci a zda se vejde do balení pod stromeček. U vánočního nákupu počítejte s dodací lhůtou a vrácením, protože velké balíky se při dopravě mohou zdržet.</p>'
          '<h2>Spaní ve stanu uvnitř nebo na zahradě</h2>'
          '<p>Přespání v dětském hracím stanu není stejné jako kempování. Pro tuto příležitost se hodí <a href="/detske-spacaky/">dětský spacák</a> a <a href="/karimatky-a-matrace/">karimatka</a> a v zahradě také ověřená pomoc dospělého poblíž. Pro opravdové kempování s dětmi pak potřebujete odolný stan, k němuž se hodí <a href="/kempingove-doplnky/">kempingové doplňky</a> a <a href="/spaci-pytle/">spací pytle</a>. Hrací stan vás před vodou ani před vlhkem země neochrání, proto jde jen o hru.</p>'
          '<h2>Péče a skladování</h2>'
          '<p>Textilní plášť stanu čistěte vlhkým hadříkem nebo jemným přípravkem a nechte ho dobře uschnout. Neperte ho v pračce, pokud výrobce výslovně neuvádí, že to lze. Tyče po rozložení otřete a uložte do původního vaku, aby se nepoškrábaly. Stan skládejte podle návodu, protože ohnutí tyčí a zalomení textilie ho trvale poškodí. Mimo sezónu skladujte suchý a čistý, mimo dosah vlhkosti a slunečního záření.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Očekávání, že stan unese noc venku:</strong> hrací modely nejsou vodovzdorné a nemají bezpečné ukotvení.</li>'
          '<li><strong>Špatná velikost:</strong> příliš malý stan dítě omezuje, příliš velký zabere celý pokoj.</li>'
          '<li><strong>Zanedbání bezpečnosti:</strong> světlo a oheň do stanu nepatří.</li>'
          '<li><strong>Nákup podle barvy:</strong> důležitější je kvalita tyčí, spojení a švů, motiv je až druhotný.</li>'
          '<li><strong>Zapomenuté sledování dítěte:</strong> i malý stan je uzavřený prostor, kde se dítě může skrýt nebo se zaseknout.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Sporteka nic neprodává, jen porovnává nabídky obchodů. Podívejte se na rozměry, hmotnost balení a na to, zda je v ceně vše potřebné, třeba tyče nebo podložka. Otevřete popis a hledejte údaje o věku, materiálu a výrobci. Pokud kupujete jako dárek, ověřte dodací lhůtu a možnost vrácení.</p>',
    faq=[
        ('Od jakého věku se dětský stan hodí?', 'Řiďte se věkovým označením výrobce (u hraček s drobnými díly bývá obvykle od 3 let) a ověřte, že výrobek má označení CE a splňuje normu EN 71. Stan má být stabilní a dítě si v něm má hrát pod dohledem. Menším dětem se vyplatí nižší stan s širokým vstupem.'),
        ('Je dětský stan vhodný na spaní venku?', 'Ne. Hrací stany nejsou vodovzdorné, nemají pevné ukotvení a nejsou určené na noc v přírodě. Pro přespání venku zvolte turistický nebo rodinný stan.'),
        ('Dá se stan používat na zahradě?', 'Ano, na krátkou dobu hry za suchého počasí. Zakotvěte ho nebo zatěžkejte a nenechávejte venku v dešti, ve větru ani přes noc.'),
        ('Jak vybrat velikost?', 'Podle věku a počtu dětí. Dítě by se mělo uvnitř pohodlně posadit, ležet a obrátit. Změřte volné místo v pokoji nebo na zahradě a porovnejte s rozměry u produktu.'),
        ('Z čeho se dětské stany vyrábějí?', 'Plášť bývá z bavlny nebo polyesteru, rám z dřevěných nebo plastových tyček. Bavlna je příjemnější a prodyšnější, polyester snadněji se čistí a lehčí.'),
        ('Mohu do stanu dát světýlka?', 'Jen vhodná, určená pro děti, na baterie a s nízkým ohřevem. Žádné svíčky, kamna ani horké lampy a prodlužovačku do stanu nevtahujte.'),
        ('Jak stan čistit?', 'Otřít vlhkým hadříkem s jemným čisticím prostředkem a nechat uschnout. Pračku použijte jen tehdy, když výrobce uvádí, že je to možné.'),
        ('Kolik místa stan zabere?', 'Menší dětské teepee potřebuje plochu zhruba jako kruh o průměru kolem jednoho metru až metru a půl, větší hrady a domečky víc. Přesné rozměry najdete u produktu, vždy je porovnejte s místem v pokoji.'),
        ('Dá se stan složit a vzít s sebou?', 'Většina teepee se rozloží a složí do vaku, takže ho lze vzít k babičce nebo na zahradu. Tyče si pamatujte označit a při skládání postupujte podle návodu, aby se nezlomily spojky ani látka.'),
        ('Je stan náročný na sestavení?', 'Většina modelů je jednoduchá. Stačí zasunout tyče do pláště a zajistit spoje, na což stačí dospělý a pár minut. U hradů a složitějších tvarů počítejte s delší dobou.'),
        ('Čím se teepee liší od hracího domečku?', 'Teepee má kuželový tvar s tyčemi zkříženými nahoře, domeček má pevnější stěny, dveře a okna. Teepee vypadá klidněji a zabere méně místa, domeček nabízí víc herních možností.'),
        ('Co dělat, když stan poškodí vítr nebo dítě?', 'Poškozené tyče či spojky vyměňte nebo stan vyřaďte. Roztržené švy lze zašít, ale ostré hrany či nestabilní konstrukce jsou důvod koupit nový stan.'),
    ])
