"""sporteka.cz — wave 14b (4. 11. 2026): long texts (>= 1650 words) for tenisova-obuv, sportovni-rukavice, cyklisticke-helmy, treninkova-obuv.
General true facts only, no prices. Brands and subcategories verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ tenisova-obuv
NEW['tenisova-obuv'] = dict(long=True,
    title='Tenisová obuv: antuka, tvrdý povrch, hala | Sporteka',
    desc='Tenisová obuv pánská, dámská i dětská. Průvodce výběrem podle povrchu, stylu hry a velikosti a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Tenisová obuv</strong> je jediná část výbavy, která pracuje s každým krokem na kurtu. Při hře se střídá krátký sprint, prudké zabrzdění, výpad do strany a vzápětí návrat do středu. Obyčejná běžecká bota je stavěná na pohyb vpřed, a proto při bočním zatížení povoluje přesně tam, kde ji potřebujete. Tenisová bota má pevnější boky, odolnější špičku a podrážku přizpůsobenou povrchu.</p>'
          '<p>Na Sportece najdete pánské, dámské i dětské modely od značek ' + B(('adidas', 'Adidas'), ('head', 'Head'), ('k-swiss', 'K-Swiss'), ('asics', 'Asics'), ('mizuno', 'Mizuno'), ('lotto', 'Lotto'), ('wilson', 'Wilson'), ('yonex', 'Yonex'), ('babolat', 'Babolat')) + '. Nabídky českých obchodů jsou seřazené vedle sebe, takže hned vidíte, kde je váš rozměr skladem. Související výbavu najdete v kategoriích <a href="/tenis/">tenis</a> a <a href="/tenisove-rakety/">tenisové rakety</a>.</p>',
    guide='<h2>Proč nestačí běžná sportovní obuv</h2>'
          '<p>Pohyb na tenisovém kurtu je z velké části boční. Chodidlo se při zastavení opírá o vnější hranu a bota tuto sílu musí udržet, jinak se kotník překlopí. Proto má tenisová obuv zesílené boky, širší základnu a pevnější patní část. Špička bývá vyztužená, protože hráči při podání a při dotažení úderu často tahají nohu po povrchu. Běžecká bota s měkkým bokem a vysokou pěnou pod patou se při takovém zatížení houpe a nabízí méně jistoty.</p>'
          '<p>Druhým rozdílem je podrážka. U běhu hledá výrobce co nejplynulejší odvinutí, u tenisu naopak kontrolovaný skluz. Na některých površích je skluz žádoucí, na jiných je třeba bota, která se okamžitě zachytí. O tom rozhoduje vzor a směs gumy, proto se dál dělí obuv podle povrchu.</p>'
          '<h2>Povrch kurtu rozhoduje o podrážce</h2>'
          + T(['Povrch', 'Co má podrážka umět', 'Na co si dát pozor'], [
              ['Antuka', 'drobný vzor ve tvaru rybí kosti, který se nezanáší a umožňuje řízený skluz', 'hustý a hladký vzor drží málo, příliš hrubý se ucpává'],
              ['Tvrdý povrch (akryl)', 'odolná guma a tlumení v mezipodešvi', 'brusný povrch rychle ničí měkké směsi, hlavně v oblasti špičky'],
              ['Hala (koberec, parkety)', 'hladší a měkčí guma s dobrým záběrem', 'hrubá venkovní podrážka může na palubovce zanechat stopy'],
              ['Umělá tráva a písek', 'drobné výstupky nebo zjemněný vzor', 'na antukových botách je skluz nepředvídatelný'],
              ['Přírodní tráva', 'hustě rozmístěné nopky', 'na tvrdém povrchu se nopky rychle sbrousí']]) +
          '<p>Pokud hrajete na více površích, nejlepší kompromis nabízí obuv označovaná jako univerzální (all court). Hodí se pro rekreační hráče, kteří střídají kurty podle toho, který je volný. Při pravidelné hře ale vyplatí mít zvlášť boty na antuku a zvlášť na tvrdý povrch, protože každý typ povrchu zatěžuje podrážku jinak.</p>'
          '<h2>Styl hry a konstrukce boty</h2>'
          '<p>Hráč, který většinu času stráví za základní čárou a běhá od jednoho rohu ke druhému, potřebuje hlavně boční oporu a odolnou špičku. Hráč útočného stylu, který chodí k síti, více ocení lehkost a pohyblivost, protože krátké a rychlé kroky vyžadují snadné odpíchnutí. Hráči čtyřhry zase často mění směr a ocení pevný střed boty. Pomocí následujících bodů rychle zjistíte, na co se zaměřit.</p>'
          '<ul><li><strong>Boční opora:</strong> stabilizační prvky na vnější straně chodidla brání překlopení kotníku. Čím víc se pohybujete do stran, tím důležitější jsou.</li>'
          '<li><strong>Tlumení:</strong> pomáhá při dopadech po skocích a při dlouhých zápasech. Příliš měkká pěna však snižuje stabilitu, takže hledejte rovnováhu.</li>'
          '<li><strong>Odolnost špičky:</strong> zesílení z gumy nebo pevné syntetiky vydrží tažení nohy po povrchu, hlavně u podání.</li>'
          '<li><strong>Prodyšnost svršku:</strong> síťovina chladí chodidlo, ale hůř odolává otěru. Kombinace sítě a zpevněných překrytí bývá praktická.</li>'
          '<li><strong>Hmotnost:</strong> lehká bota je svižná, těžší bývá odolnější a stabilnější. Žádná varianta není ideální pro všechny.</li></ul>'
          '<h2>Velikost a šířka</h2>'
          '<p>Tenisová obuv sedí těsněji než volnočasové boty. Pata musí být pevně uchycená a prsty mají mít před špičkou rezervu v řádu pár milimetrů, aby se při brzdění nezarážely. Chodidlo je odpoledne a po zátěži větší, proto zkoušejte boty v tuto dobu a v ponožkách, které nosíte na kurt. Pokud tlačí v šířce, vyberte model s širší kopytní částí nebo jinou značku, protože výrobci mají odlišné tvary. Na velikostní tabulky se sice můžete spolehnout jako na první odhad, nejspolehlivější je ale vnitřní délka stélky v centimetrech, kterou většina obchodů uvádí.</p>'
          + T(['Situace', 'Doporučení'], [
              ['Pata při zabrzdění sjíždí', 'zkuste menší velikost nebo model s lepším fixačním systémem v oblasti paty'],
              ['Prsty narážejí do špičky', 'vyberte o půl čísla větší nebo model s vyšší špičkou'],
              ['Tlačí malíček', 'hledejte širší střih nebo měkčí svršek'],
              ['Bota je v klidu pohodlná, ale na kurtu povoluje', 'zpevněte šněrování a ověřte oporu v bocích']]) +
          '<h2>Pánská, dámská a dětská obuv</h2>'
          '<p>Dámské modely mají obvykle užší patu a menší objem v přední části, protože ženské chodidlo je v průměru užší. Pánské boty bývají širší a nabízejí více místa v prstech. Rozdíl není absolutní, takže pokud vám sedí opačná řada, klidně ji použijte. Děti rostou rychle a obuv do tenisu by měla mít pružnou podrážku a dobré šněrování, nikoliv extrémní hmotnost. Kupovat boty o dvě čísla větší, aby vydržely déle, se nevyplácí, protože se noha v botě pohybuje a roste riziko podvrtnutí. Pro dětské hráče je užitečné pravidelně kontrolovat, zda jim prsty nenarážejí na špičku.</p>'
          '<h2>Příbuzné sporty a obuv</h2>'
          '<p>Padel se hraje na umělém povrchu s pískem a vyžaduje jiný vzor podrážky než antuka, proto má vlastní kategorii <a href="/padel/">padel</a>. U squashe a badmintonu se používá lehká halová obuv, informace najdete u <a href="/squash/">squashe</a>, <a href="/badminton/">badmintonu</a> a v kategorii <a href="/salova-obuv/">sálová obuv</a>. Pro stolní tenis stačí nízká a lehká bota s dobrým záběrem, viz <a href="/stolni-tenis/">stolní tenis</a>. Pokud potřebujete boty i na jiné sporty, projděte nabídku <a href="/sportovni-obuv/">sportovní obuvi</a> nebo <a href="/treninkova-obuv/">tréninkové obuvi</a>. Na běh je lepší <a href="/bezecka-obuv/">běžecká obuv</a> a na košíkovou <a href="/basketbalova-obuv/">basketbalová obuv</a>.</p>'
          '<h2>Ponožky, vložky a péče</h2>'
          '<p>Při tenisu se noha potí a tře, takže volte funkční <a href="/sportovni-ponozky/">sportovní ponožky</a> s vyztuženou patou a špičkou. Bavlna nasákne potem a podporuje puchýře. Vložku z výroby můžete po několika měsících vyměnit, protože ztrácí tlumení dřív než podrážka. V kategorii <a href="/doplnky-k-obuvi/">doplňky k obuvi</a> najdete stélky, tkaničky a impregnaci. Po hře boty vyndejte z tašky, vyvětrejte je a očistěte podrážku od antuky nebo prachu. Nesušte je na topení, vysoká teplota poškozuje lepené spoje. Střídání dvou párů prodlouží životnost obou, protože pěna v mezipodešvi se mezi zápasy znovu rozepne. Nejste-li si jistí zdravím kotníku, zvažte <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>, ale vždy po konzultaci s lékařem nebo fyzioterapeutem.</p>'
          '<h2>Kdy vyměnit boty</h2>'
          '<p>Znaky opotřebení se poznají dobře. Vzor na podrážce je sjetý, zejména v oblasti špičky a vnější hrany. Mezipodešev je ztvrdlá a při dopadu cítíte tvrdší náraz než dřív. Svršek je protržený nebo se boky bortí dovnitř. Při pravidelné hře několikrát týdně tak může být třeba obuv obnovit po několika měsících, rekreačnímu hráči vydrží déle. Hraní ve starých botách je častou příčinou bolesti kolen a kotníků.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Výběr podle barvy a vzhledu bez ohledu na povrch, na kterém budete hrát.</li>'
          '<li>Zkoušení bot v dopoledních hodinách a v tenkých ponožkách.</li>'
          '<li>Hra v obuvi na antuku na tvrdém povrchu, kde se podrážka ničí zrychleně.</li>'
          '<li>Nošení tenisové obuvi na denní chození, kdy se podrážka opotřebuje dřív, než ji využijete na kurtu. Na každodenní nošení slouží <a href="/tenisky/">tenisky</a>.</li>'
          '<li>Ignorování šířky boty a následné puchýře nebo zatuhlé prsty.</li></ul>'
          '<h2>Jak nakupovat na Sportece</h2>'
          '<p>Katalog sbírá nabídky českých e-shopů. U každé boty vidíte dostupné velikosti u jednotlivých prodejců, takže nemusíte obcházet stránky jednu po druhé. Pro srovnání si otevřete detail produktu a porovnejte obchody, dopravu a podmínky vrácení. Ještě před objednávkou si změřte délku chodidla a porovnejte ji s tabulkou výrobce. Pokud si nejste jistí, objednejte dva sousední rozměry a ten nevhodný vraťte, což je u většiny obchodů v zákonné lhůtě možné. K tašce na kurt se může hodit i <a href="/sportovni-tasky/">sportovní taška</a> s oddělenou přihrádkou na boty, aby neznečistily oblečení.</p>',
    faq=[('Mohu hrát tenis v běžeckých botách?', 'Dá se to, ale nedoporučuje se. Běžecká obuv má měkčí boky a vyšší pěnu pod patou, takže při bočním zatížení nedrží chodidlo stabilně. Hrozí překlopení kotníku a rychlé sjetí podrážky.'),
         ('Jaká obuv je nejlepší na antuku?', 'Hledejte podrážku se vzorem ve tvaru rybí kosti, která umožní řízený skluz a nezanáší se. Hladká halová podrážka na antuce klouže a hrubá tvrdokurtová se ucpává.'),
         ('Lze používat antukovou obuv na tvrdém povrchu?', 'Technicky ano, ale gumová podrážka antukových modelů se na brusném akrylu rychle sjíždí. Pokud hrajete na obou površích, kupte si raději dva páry nebo univerzální model.'),
         ('Jak často měnit tenisovou obuv?', 'Záleží na četnosti hry, váze hráče a povrchu. Vyměňte boty, když je vzor podrážky sjetý, mezipodešev ztvrdlá nebo se boky boty bortí dovnitř.'),
         ('Jsou tenisové boty vhodné i na padel?', 'Pro občasnou hru stačí, ale padelová obuv má podrážku přizpůsobenou umělému povrchu s pískem. Tenisová antuková bota na takovém kurtu může klouzat.'),
         ('Jak poznat správnou velikost?', 'Měřte chodidlo odpoledne, v ponožkách pro tenis. Pata musí sedět pevně a prsty se mají před špičkou lehce hýbat. Orientujte se podle vnitřní délky stélky v centimetrech.'),
         ('Jaký je rozdíl mezi pánskou a dámskou obuví?', 'Dámské modely mají obvykle užší patu a menší objem, pánské jsou širší. Rozdíl není pevný, takže vyberte tu řadu, která vám pohodlně sedí.'),
         ('Hodí se tenisová obuv na každodenní nošení?', 'Použít ji můžete, ale podrážka se opotřebuje dřív, než ji využijete na kurtu. Na běžné chození jsou vhodnější klasické tenisky nebo volnočasová obuv.'),
         ('Jak o boty pečovat?', 'Po hře je vyvětrejte, očistěte podrážku od antuky a nesušte je na topení ani na přímém slunci. Pokud hrajete často, střídejte dva páry, aby se mezipodešev stihla uvolnit.'),
         ('Kolik párů potřebuje začátečník?', 'Pro začátek stačí jeden pár univerzální obuvi na povrch, na kterém budete hrát nejčastěji. Další kupujte až tehdy, když začnete pravidelně střídat povrchy.')],
)

# ------------------------------------------------------------------ treninkova-obuv
NEW['treninkova-obuv'] = dict(long=True,
    title='Fitness a tréninková obuv do posilovny | Sporteka',
    desc='Fitness a tréninková obuv pro posilovnu, crossfit, HIIT a skupinové lekce. Průvodce výběrem, velikostí a péčí a nabídky českých e-shopů.',
    intro='<p><strong>Tréninková obuv</strong> je určená pro cvičení v interiéru: silový trénink, kruhové tréninky, skupinové lekce, crossfit nebo funkční cvičení. Na rozdíl od běžecké boty nemusí zvládat dlouhé tempo na asfaltu. Důležitější je stabilní podrážka, pevné držení paty a odolnost vůči bočnímu zatížení. Ve správné obuvi cvičíte jistěji a lépe přenášíte sílu z chodidla do země.</p>'
          '<p>Na Sportece najdete modely značek ' + B(('skechers', 'Skechers'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('joma', 'Joma'), ('puma', 'Puma'), ('asics', 'Asics'), ('new-balance', 'New Balance'), ('under-armour', 'Under Armour'), ('on', 'On'), ('mizuno', 'Mizuno')) + '. Můžete porovnat nabídky českých obchodů a hlídat dostupné velikosti. Pokud trénujete i venku, mrkněte také na <a href="/bezecka-obuv/">běžeckou obuv</a> a širší výběr v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>.</p>',
    guide='<h2>Co dělá tréninkovou obuv tréninkovou</h2>'
          '<p>Při dřepu, mrtvém tahu nebo výpadu tlačí chodidlo proti podlaze velkou silou. Pokud je podrážka měkká a vysoká, pěna se pod zátěží stlačuje nerovnoměrně a bota se kymácí. Tréninková obuv proto mívá nižší a pevnější podrážku, širší patu a svršek, který drží chodidlo na místě. Při skocích a změnách směru ocení cvičenec také boční oporu, kterou běžecká bota většinou nemá. Naopak na dlouhé kardio na pásu zvládne tréninková bota méně než specializovaná běžecká, protože není stavěná na rytmické odvíjení kroku.</p>'
          '<h2>Typ cvičení určuje typ boty</h2>'
          + T(['Cvičení', 'Co hledat', 'Čemu se vyhnout'], [
              ['Silový trénink s činkami', 'tvrdá plochá podrážka, široká pata, pevné šněrování', 'vysoká měkká pěna pod patou'],
              ['Crossfit a HIIT', 'odolný svršek, vyztužená špička a boky, střední tlumení', 'příliš jemná síťovina, která se roztrhne při lanech'],
              ['Aerobik, zumba, taneční lekce', 'lehká bota s dobrou boční oporou a hladším středem podrážky', 'hrubé podrážky, které se zasekávají o podlahu'],
              ['Kruhový a funkční trénink', 'univerzální bota s mírným tlumením a stabilním tvarem', 'extrémně lehké modely bez opory'],
              ['Kardio na stroji', 'lehká obuv s dobrým odvíjením', 'tvrdé ploché boty na delší vytrvalost']]) +
          '<p>Pokud cvičíte všechno dohromady, vyberte kompromis: středně tvrdou podrážku, pevný svršek a nízkou až střední výšku podešve. Při pravidelném těžkém tréninku sílových disciplín může dávat smysl druhý pár s plochou podrážkou jen na dřepy a tahy. Pro doplňkové aktivity se hodí kategorie <a href="/fitness/">fitness</a> a <a href="/funkcni-trenink/">funkční trénink</a>.</p>'
          '<h2>Na co se dívat při výběru</h2>'
          '<ul><li><strong>Stabilita paty:</strong> široká patní část a pevná zadní opěrka drží chodidlo i při těžkém zatížení.</li>'
          '<li><strong>Tlumení:</strong> pro skoky a krátké úseky potřebujete mírné, pro čistě silový trénink naopak minimální.</li>'
          '<li><strong>Odolnost materiálu:</strong> při lezení po laně a švihadle se svršek otírá, vyztužení z gumy nebo syntetiky vydrží déle než síťovina.</li>'
          '<li><strong>Prodyšnost:</strong> v zahřáté posilovně se noha potí, vzdušný svršek omezuje pocení.</li>'
          '<li><strong>Šněrování:</strong> pevné tkaničky dovolují dotáhnout botu na nártu, suchý zip nebo rychlošněrování bývá pohodlnější, ale drží méně spolehlivě.</li>'
          '<li><strong>Záběr podrážky:</strong> guma musí zabírat na gumové podlaze i na parketách, aniž by se zasekávala při otáčení.</li></ul>'
          '<h2>Velikost a pohodlí</h2>'
          '<p>Při cvičení se nohy roztahují a příjemný dojem z obchodu může po hodině zmizet. Proto zkoušejte obuv v odpoledních hodinách a ve stejných ponožkách, v jakých cvičíte. Před špičkou nechte rezervu asi na šířku palce, ale zároveň zkontrolujte, že pata nesjíždí při zvednutí na špičky. Při skocích prsty nesmějí narážet do přední části boty. Na šířku se neobávejte využít úzké nebo široké varianty, pokud je výrobce nabízí. Některé značky nabízejí širší tvar, jiné užší, proto se při změně značky vyplatí zkusit sousední velikost.</p>'
          '<h2>Pro koho jaká bota</h2>'
          '<p>Začátečníkovi do posilovny stačí univerzální model s pevnou podrážkou, nemusí hned kupovat specializované boty. Pravidelný silový sportovec ocení bot s plochou a tvrdou podrážkou, která zajišťuje přímý přenos síly. Návštěvníci skupinových lekcí potřebují lehčí obuv s ohebným předním dílem, aby mohli skákat a otáčet se. Ženám se často hodí užší patní část a nižší hmotnost, mužům širší špička, ovšem rozdíly nejsou pravidlem. Děti a mladiství potřebují obuv s pružnou podrážkou a pevnou patou, která drží nohu na místě. Pokud trénujete jen občas a chcete jednu botu na všechno, vyberte univerzální tréninkový model a doplňte jej kvalitními <a href="/sportovni-ponozky/">sportovními ponožkami</a>.</p>'
          '<h2>Barefoot a minimalistická obuv</h2>'
          '<p>Barefoot boty mají tenkou, ohebnou podrážku a širokou špičku, aby chodidlo pracovalo přirozeněji. Někteří cvičenci je používají při silovém tréninku pro lepší cit k podlaze. Přechod na minimalistickou obuv by měl být postupný, protože svaly chodidla a lýtek potřebují čas na přizpůsobení. Více se dozvíte v kategorii <a href="/barefoot-obuv/">barefoot obuv</a>. Pro cvičení na podložce a jógu často stačí cvičit naboso nebo v ponožkách, viz <a href="/joga-a-pilates/">jóga a pilates</a>.</p>'
          '<h2>Doplňky k tréninku</h2>'
          '<p>Správná obuv je jen jedna část výbavy. Dobře padnoucí <a href="/sportovni-kalhoty/">sportovní kalhoty</a> nebo <a href="/leginy/">legíny</a>, funkční <a href="/sportovni-tricka/">tričko</a> a vhodná <a href="/sportovni-tasky/">sportovní taška</a> zajistí pohodlí. Při rizikových cvicích pomohou <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>. Pro trénink doma nebo ve skupinovém studiu se hodí <a href="/fitness-pomucky/">fitness pomůcky</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</p>'
          '<h2>Péče o obuv</h2>'
          '<p>Tréninkovou obuv používejte pouze uvnitř, aby se podrážka nezanášela venkovním pískem a nepoškozovala podlahy v hale. Po tréninku boty vyndejte z tašky a nechte je vyvětrat při pokojové teplotě. Mokré boty nesušte na radiátoru a na přímém slunci, lepidlo se tím zjemní a podrážka se může oddělit od svršku. Vložky pravidelně vyndavejte a nechte je zvlášť uschnout. Pokud trénujete několikrát týdně, střídání dvou párů prodlouží životnost, protože pěna se stihne uvolnit.</p>'
          '<h2>Kdy je čas na nový pár</h2>'
          '<p>Vyměňte boty, jakmile se podrážka vyrovná a ztratí vzor, svršek se protrhne v místě ohybu prstů nebo bota začne po tréninku bolet chodidla či kolena. Také pata, která se už nedrží pevně a bota se při zatížení kývá, je signálem ke koupi nové. S ohledem na zdraví nesetrvávejte v obuvi, která už nedrží, protože riziko zranění roste.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Cvičení s těžkými činkami v měkkých běžeckých botách, které se pod zátěží vyhýbají.</li>'
          '<li>Nákup příliš velké obuvi kvůli pohodlí, která při skocích nedrží pevně patu.</li>'
          '<li>Používání té samé obuvi venku i v hale.</li>'
          '<li>Podcenění ponožek, bavlněné nasáknou potem a způsobují puchýře.</li>'
          '<li>Jeden pár na všechno u pravidelných cvičenců, u kterých se vyplatí rozdělení na silový a skokový trénink.</li></ul>',
    faq=[('Mohu v tréninkové obuvi běhat?', 'Na kratší úseky v rámci tréninku ano, ale na delší běh je lepší běžecká obuv. Tréninková bota je tužší a nemá odvíjení stavěné na dlouhé tempo.'),
         ('Jaká obuv je nejlepší na dřepy a mrtvé tahy?', 'Ta s nízkou, tvrdou a plochou podrážkou, která stabilně drží chodidlo. Měkká vysoká pěna pod patou se pod zátěží stlačuje a zhoršuje stabilitu.'),
         ('Je lepší cvičit v botách, nebo naboso?', 'Záleží na cvičení a zkušenostech. Obuv chrání chodidlo před pády činek a nabízí oporu, naboso lze cvičit na čisté podložce nebo v minimalistické obuvi po postupném zvykání.'),
         ('Jak poznat správnou velikost?', 'Zkoušejte odpoledne v ponožkách pro trénink. Před špičkou nechte rezervu asi na šířku palce a ověřte, že pata nesjíždí při stoupání na špičky.'),
         ('Hodí se tréninková obuv do skupinových lekcí?', 'Ano. Pro aerobik, zumbu a podobné lekce hledejte lehčí botu s ohebným předkem a boční oporou, která nezpomaluje otáčení.'),
         ('Jak často měnit tréninkovou obuv?', 'Vyměňte ji, když se podrážka vyrovná, svršek roztrhne nebo bota přestane držet patu. Při pravidelném tréninku několikrát týdně dojde k opotřebení dřív.'),
         ('Mohu tréninkovou obuv nosit i na ulici?', 'Můžete, ale podrážka se zbytečně opotřebuje a zanese venkovním pískem. Do haly a posilovny je vhodné mít samostatný pár.'),
         ('Je potřeba speciální obuv na crossfit?', 'Univerzální tréninkový model s odolným svrškem stačí většině cvičenců. Specializované boty mají vyztužení pro lano a mírné tlumení pro skoky.'),
         ('Jak čistit tréninkové boty?', 'Povrch otřete vlhkým hadříkem, vložky vyndejte a nechte uschnout zvlášť. Nesušte je na topení ani na slunci a vyhněte se praní v horké vodě.'),
         ('Jsou barefoot boty vhodné do posilovny?', 'Mnoho cvičenců je používá pro lepší cit k podlaze při silovém tréninku. Přecházet je vhodné postupně, aby si chodidlo a lýtka zvykly.')],
)

# ------------------------------------------------------------------ sportovni-rukavice
NEW['sportovni-rukavice'] = dict(long=True,
    title='Sportovní rukavice: lyžařské, běžecké, zimní | Sporteka',
    desc='Sportovní rukavice na lyže, běh, kolo i trénink. Průvodce materiály, velikostí a péčí a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Sportovní rukavice</strong> jsou malá část výbavy, jejíž selhání pocítíte ihned. Zmrzlé prsty znamenají konec lyžování, mokré rukavice zkazí výlet a špatná velikost zhorší cit při tréninku. Každý sport klade jiné nároky. Běžec chce lehkou a prodyšnou vrstvu, lyžař izolaci a voděodolnost, cyklista polstrování dlaně a pracovník v terénu odolnost proti oděru.</p>'
          '<p>Na Sportece najdete rukavice značek ' + B(('viking', 'Viking'), ('rossignol', 'Rossignol'), ('force', 'Force'), ('swix', 'Swix'), ('dynafit', 'Dynafit'), ('reusch', 'Reusch'), ('mechanix-wear', 'Mechanix Wear®'), ('silvini', 'Silvini'), ('reima', 'Reima')) + '. Nabídky českých obchodů jsou seřazené vedle sebe a u každého produktu uvidíte, ve kterých velikostech je skladem. Pro konkrétní sporty se podívejte také do kategorií <a href="/lyzarske-rukavice/">lyžařské rukavice</a> a <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>.</p>',
    guide='<h2>Jak rozlišit typy sportovních rukavic</h2>'
          '<p>Základní rozdělení vychází z použití. Zimní rukavice se liší od letních především izolací a vodotěsností, sportovní od pracovních vyztužením dlaně a střihem. Následující tabulka pomůže najít správnou skupinu.</p>'
          + T(['Sport', 'Klíčové vlastnosti', 'Typické materiály'], [
              ['Běh a rychlá turistika', 'nízká hmotnost, prodyšnost, citlivé prsty, dotykové špičky', 'tenký fleece, elastický úplet, jemný syntetický materiál'],
              ['Sjezdové lyžování a snowboarding', 'izolace, nepromokavost, vyztužená dlaň, dlouhá manžeta', 'membrána, syntetické plnění, kůže nebo syntetická kůže na dlani'],
              ['Běžecké lyžování', 'větruodolnost na hřbetu, prodyšnost dlaně, lehkost', 'tenký softshell, fleece, prodyšné membrány'],
              ['Skialpinismus a trek', 'rychlé schnutí, odolnost při práci s lyžemi a holemi', 'softshell, kůže, tenká izolace'],
              ['Cyklistika', 'polstrování dlaně, prodyšnost, nepoklouznutí na řidítkách', 'síťovina, gel, jemná syntetika'],
              ['Fitness a trénink', 'ochrana dlaní, přilnavost, ohebnost', 'kůže, neopren, jemná textilie'],
              ['Práce a taktické použití', 'odolnost, přesnost úchopu, ochrana kloubů', 'syntetická kůže, vyztužení z gumy']]) +
          '<h2>Prstové rukavice, palčáky a hybridy</h2>'
          '<p>Palčáky jsou teplejší, protože prsty se navzájem zahřívají a plocha vystavená chladu je menší. Prstové rukavice nabízejí lepší cit a obratnost, hodí se tedy tam, kde se pracuje s popruhy, zipy nebo telefonem. Hybridní řešení spojuje obojí: tenká prstová rukavice uvnitř a nepromokavý přetahovací palčák navrch. V horách s proměnlivým počasím tak můžete podle potřeby jednu vrstvu sundat. Pro děti jsou prakticky vhodnější palčáky, protože se do nich snadno oblékají a hřejí víc, ale ke sjezdovým rukavicím existují i varianty s oddělenými prsty pro starší děti.</p>'
          '<h2>Izolace a vodotěsnost</h2>'
          '<p>Teplo v rukavici zajišťuje vzduch uvězněný v izolační vrstvě. Syntetická izolace funguje i za vlhka a dobře schne, přírodní peří má výborný poměr tepla k váze, ale mokré přestává izolovat. Membrána brání pronikání vody zvenčí, propouští však vodní páru z potu. Při lyžování se ruce potí, proto je lépe vybírat modely s membránou a prodyšnou podšívkou. Sama vodotěsnost nestačí, pokud je manžeta krátká a sníh se dostává dovnitř. U sjezdových rukavic sledujte dlouhou manžetu, která se dá zatáhnout přes rukáv bundy.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Rukavice musí sedět tak, aby prsty dosahovaly konců a zároveň nebyly stlačené. Příliš těsný střih stahuje cévy a ruce rychleji zmrznou, příliš volný snižuje cit a prsty v prázdných špičkách zábou. Pro přesnou volbu změřte obvod dlaně těsně pod klouby bez palce a délku nejdelšího prstu od kořene k špičce. Hodnoty porovnejte s tabulkou výrobce, protože střihy se liší.</p>'
          + T(['Problém', 'Příčina', 'Řešení'], [
              ['Prsty zmrzají i v zimních rukavicích', 'příliš těsná velikost nebo vlhká podšívka', 'zkuste větší velikost nebo model s volnější izolací'],
              ['Rukavice kloužou z ruky', 'krátká manžeta nebo velké číslo', 'zvolte užší zápěstí s uchycením na suchý zip'],
              ['Špička prstu je prázdná', 'rukavice je příliš velká nebo má krátké prsty', 'změřte délku prstů a hledejte jiný střih'],
              ['Švy tlačí v dlani', 'nevhodný tvar pro tvar ruky', 'zkuste jinou značku nebo model s anatomickým střihem']]) +
          '<h2>Doplňky k ochraně rukou</h2>'
          '<p>Při zimních sportech doplňují rukavice čepice a krkní doplňky, viz <a href="/cepice-a-celenky/">čepice a čelenky</a>, <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a> a <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a>. Pro lyžaře je důležitý celek, proto sledujte i <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/lyzarske-helmy/">helmy</a> a <a href="/lyzarske-bryle/">brýle</a>. Pod silnou rukavici lze oblékat tenké spodní rukavice, které přidají několik stupňů tepla a umožňují krátké sundání vnější vrstvy. Na dlouhé túry s vodou a sněhem se vyplatí náhradní pár. K řidítkům patří <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>, k trekům <a href="/trekove-hole/">trekové hole</a>, ke sportům v zimě <a href="/zimni-sporty/">zimní sporty</a>.</p>'
          '<h2>Sporty mimo zimu</h2>'
          '<p>Rukavice se používají i v teplém počasí. Cyklisté chrání dlaně před tlakem na řidítkách a při pádu před odřením, rukavice s odkrytými prsty větrají. Posilovači a cvičenci potřebují přilnavost a ochranu před mozoly, ale cítí-li se v nich nejistě, mohou cvičit i bez. Boxeři a bojové sporty používají specializované vybavení, viz <a href="/boxerske-rukavice/">boxerské rukavice</a> a <a href="/chranice-bojove-sporty/">chrániče pro bojové sporty</a>. Brankáři mají vlastní kategorii <a href="/brankarske-rukavice/">brankářské rukavice</a>. Pracovní a taktické rukavice, například od značek Mechanix Wear® nebo Mil-tec®, jsou stavěné na přesný úchop a ochranu kloubů.</p>'
          '<h2>Jak o rukavice pečovat</h2>'
          '<p>Mokré rukavice nechte uschnout při pokojové teplotě, nikdy na topení a ne na kamnech. Vysoká teplota poškozuje membránu, lepené spoje a kůži. Rukavice sundejte z bundy a vyndejte vnitřní díl, pokud je vyjímatelný. Syntetické modely lze většinou prát šetrně pomocí přípravku na funkční textil, bez aviváže, která zhoršuje prodyšnost a nasákne do izolace. Kožené ošetřete impregnací nebo vazelínou na kůži, aby neztvrdly. Před sezonou zkontrolujte švy a manžety a vyměňte pár, jehož dlaň je sjetá, protože promáčení a ztráta citu zhoršuje bezpečnost.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Nákup příliš těsných rukavic kvůli pocitu přesného sedu, které pak zhoršují prokrvení.</li>'
          '<li>Použití jednoho páru na všechny sporty bez ohledu na intenzitu a vlhkost.</li>'
          '<li>Opomenutí manžety, takže sníh nebo vítr proniká k zápěstí.</li>'
          '<li>Sušení na radiátoru a rychlé zničení membrány.</li>'
          '<li>Opomenutí náhradního páru na celodenní túře.</li></ul>'
          '<h2>Nákup přes Sportecu</h2>'
          '<p>Katalog sbírá nabídky českých e-shopů, takže jednotlivé varianty porovnáte bez přecházení mezi stránkami. Využijte filtry podle značky, velikosti a sportu a u každého produktu zkontrolujte dostupné rozměry. Pokud váháte, objednejte dvě sousední velikosti a nevhodnou vraťte v zákonné lhůtě. Sezónní kusy se obvykle vyprodávají od podzimu, proto hlídejte svůj rozměr dřív.</p>',
    faq=[('Jaké rukavice zvolit na běhání?', 'Lehké, prodyšné a tenké, například z fleecové nebo elastické pleteniny. Při chladném větru pomůže model s větruodolným hřbetem a při telefonování dotyková špička.'),
         ('Palčáky, nebo prstové rukavice?', 'Palčáky jsou teplejší, protože prsty se navzájem zahřívají. Prstové dávají lepší cit a obratnost. Hybridní model kombinuje obojí.'),
         ('Jak poznám správnou velikost?', 'Změřte obvod dlaně pod klouby a délku nejdelšího prstu. Výsledek porovnejte s tabulkou výrobce. Prsty mají dosahovat konců, aniž by byly stlačené.'),
         ('Jaká rukavice na lyže?', 'Nepromokavá, izolovaná, s vyztuženou dlaní a dlouhou manžetou, která se zatáhne přes rukáv bundy. Vhodná je i prodyšná podšívka.'),
         ('Kolik vrstev oblékat na ruce?', 'Při mírném mrazu stačí jedna kvalitní rukavice. V silnějším mrazu se hodí tenká spodní rukavice a izolovaná vrchní vrstva, kterou lze sundat při nutnosti jemné práce.'),
         ('Jak prát sportovní rukavice?', 'Držte se pokynů na štítku. Většinu syntetických modelů lze šetrně prát pomocí přípravku na funkční textil, bez aviváže. Kožené ošetřete impregnací.'),
         ('Jak sušit mokré rukavice?', 'Při pokojové teplotě, rozložené a podle možností s vyndanou vnitřní vrstvou. Nikdy ne na radiátoru ani u kamen, vysoké teploty poškozují materiál.'),
         ('Hodí se rukavice s dotykovými špičkami?', 'Ano, pokud často používáte telefon nebo hodinky. Dotyková vrstva ale nahrazuje vyjmutí rukavice jen částečně, zimní izolované modely ji mívají jen na vybraných prstech.'),
         ('Potřebuji speciální rukavice na kolo?', 'Cyklistické rukavice mají polstrování na dlani, které tlumí tlak na řidítkách, a chrání při pádu. Pro delší jízdy jsou praktické.'),
         ('Kdy rukavice vyměnit?', 'Vyměňte je, když je dlaň sjetá, švy povolují, membrána propouští vodu nebo zateplení slehlo a přestalo hřát. Opotřebené rukavice zhoršují cit i bezpečnost.')],
)

# ------------------------------------------------------------------ cyklisticke-helmy
NEW['cyklisticke-helmy'] = dict(long=True,
    title='Cyklistické helmy: silniční, MTB, dětské | Sporteka',
    desc='Cyklistické helmy pro dospělé i děti: silniční, MTB, městské a dětské. Průvodce velikostí, konstrukcí a péčí a nabídky českých e-shopů vedle sebe.',
    intro='<p><strong>Cyklistická helma</strong> je nejdůležitější ochranný prvek při jízdě na kole. Při pádu chrání hlavu před nárazem a odřením a zvyšuje šanci vyváznout bez následků. Do 18 let je její nošení při jízdě na kole v Česku povinné, dospělým se doporučuje. Přilba ale chrání jen tehdy, když sedí, je správně nastavená a není poškozená.</p>'
          '<p>Na Sportece najdete helmy značek ' + B(('alpina', 'Alpina'), ('rockbros', 'Rockbros'), ('abus', 'Abus'), ('uvex', 'Uvex'), ('ked', 'KED'), ('met', 'Met'), ('giro', 'Giro'), ('bell', 'Bell'), ('cratoni', 'Cratoni')) + '. Nabídky českých obchodů jsou seřazené vedle sebe, takže hned vidíte, kde je vaše velikost skladem. Podle použití vyberte z podkategorií <a href="/silnicni-cyklohelmy/">silniční a gravel helmy</a>, <a href="/mtb-a-integralni-helmy/">MTB, enduro a integrální helmy</a>, <a href="/mestske-cyklohelmy/">městské helmy</a> a <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>.</p>',
    guide='<h2>Jak helma chrání</h2>'
          '<p>Vnitřek helmy tvoří pěna, která se při nárazu rozdrtí a pohltí část energie. Vnější skořepina drží pěnu pohromadě a umožňuje, aby helma klouzala po povrchu, místo aby se zasekla. Popruhy a nastavení na zátylku zajišťují, aby se přilba při pádu neposunula. Vyšší cena nebo dražší vzhled sám o sobě bezpečnost nezaručí, rozhoduje sedící velikost, správně seřízené popruhy a nepoškozená konstrukce. Jakmile helma zažije silný náraz, vyměňte ji, i když vypadá neporušeně, protože pěna už nemusí tlumit stejně.</p>'
          '<h2>Typy helem podle jízdy</h2>'
          + T(['Typ', 'Pro koho', 'Charakteristika'], [
              ['<a href="/silnicni-cyklohelmy/">Silniční a gravel</a>', 'rychlá jízda na asfaltu a štěrku', 'lehká, hodně větracích otvorů, aerodynamický tvar, krátký kšilt nebo bez něj'],
              ['<a href="/mtb-a-integralni-helmy/">MTB a enduro</a>', 'terén, bikeparky, technické sjezdy', 'delší záda hlavy, kšilt, hlubší pokrytí spánků a zátylku'],
              ['Integrální', 'sjezd, enduro, bikepark', 'kryje čelist a obličej, zpravidla těžší'],
              ['<a href="/mestske-cyklohelmy/">Městské</a>', 'dojíždění, běžné jízdy', 'odolná skořepina, často se světlem nebo odrazkami, uvolněnější tvar'],
              ['<a href="/detske-cyklohelmy/">Dětské</a>', 'děti od prvních jízd', 'menší velikosti, jednoduchá regulace, veselé barvy, odrazky']]) +
          '<p>Pokud jezdíte různě, vyberte univerzální model a zaměřte se na pohodlí a správný sed. U MTB, kde se jezdí v terénu a hrozí pád do větví, jsou lepší modely s hlubším krytím zátylku. Silničáři a gravelisté ocení větrání a nízkou hmotnost. U městských helem lze sledovat integrované blikačky nebo reflexní prvky pro lepší viditelnost.</p>'
          '<h2>Velikost a nastavení krok za krokem</h2>'
          '<p>Měření začíná obvodem hlavy. Pásek nebo krejčovský metr obtočte asi centimetr nad obočím a nad ušima, přes nejširší část hlavy. Výsledek v centimetrech porovnejte s tabulkou výrobce, protože velikosti S, M a L se mezi značkami liší. Nejlepší je helmu doma vyzkoušet a správně seřídit.</p>'
          '<ul><li><strong>Poloha:</strong> helma sedí vodorovně, přední okraj leží asi dva prsty nad obočím. Nesmí být posunutá do týlu a odkrývat čelo.</li>'
          '<li><strong>Kolečko na zátylku:</strong> dotáhněte tak, aby helma při zatřesení hlavou neklouzala, ale netlačila.</li>'
          '<li><strong>Popruhy kolem uší:</strong> tvoří pod ušima V, spodní spona leží pod bradou.</li>'
          '<li><strong>Řemínek pod bradou:</strong> pod bradou zůstane místo na jeden až dva prsty, při otevření úst cítíte jemný tah.</li>'
          '<li><strong>Zkouška:</strong> zatlačte na helmu dopředu a dozadu. Pokud se pohybuje o víc než kousek, seřiďte ji nebo zkuste jinou velikost.</li></ul>'
          '<h2>Konstrukce a prvky, na které se dívat</h2>'
          '<p>Větrání je důležité, protože hlava se při jízdě potí. Čím víc otvorů, tím lépe, ale u levnějších modelů může jejich počet snížit odolnost skořepiny. Síťka proti hmyzu v otvorech brání pronikání vos a much. Vnitřní vložky z pěny nebo látky by měly být vyjímatelné a pratelné. Kšilt pomáhá před sluncem a deštěm a u MTB chrání před větvemi, u silničních helem bývá odnímatelný. Dále existují helmy s technologií snižující rotační síly při šikmém nárazu, například systémy MIPS, které nabízejí více výrobců. Ptejte se, jaký typ ochrany model nabízí, a porovnávejte popisy u jednotlivých obchodů.</p>'
          '<h2>Dětské helmy</h2>'
          '<p>Dětská helma musí především sedět. Děti rostou, takže se velikost mění rychle, ale kupovat helmu o dvě čísla větší se nevyplácí, protože by při pádu seděla špatně. Pomůže model s kolečkem pro jemné nastavení a výměnnými vložkami, které se dají přizpůsobit růstu hlavy. Kluci a holky mají k dispozici barvy a motivy, díky nimž se helma lépe nosí. Zkontrolujte, zda je na helmě odrazka nebo světlo, pokud jezdí děti i za horšího světla. Menší děti na odrážedlech a tříkolkách ochranu potřebují stejně jako starší, viz <a href="/odrazedla/">odrážedla</a>, <a href="/detska-kola/">dětská kola</a> a <a href="/detske-trikolky/">dětské tříkolky</a>. Podobný postup platí i pro <a href="/kolobezky/">koloběžky</a> a <a href="/kolobezky-a-brusle/">brusle</a>, u kterých existuje kategorie <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<h2>Doplňky ke kolu a helmě</h2>'
          '<p>K helmě patří další výbava. <a href="/cyklisticke-bryle/">Cyklistické brýle</a> chrání oči před prachem, hmyzem a sluncem. <a href="/cyklisticke-rukavice/">Rukavice</a> tlumí tlak na řidítkách a chrání dlaně při pádu. <a href="/cyklisticke-obleceni/">Cyklistické oblečení</a> a <a href="/cyklisticka-obuv/">obuv</a> zajišťují pohodlí na delších trasách. Pro bezpečnost v provozu používejte <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>, a pokud ke kolu patří i odkládání, <a href="/cyklo-zamky/">zámky</a>. Podle typu kola pak vybírejte <a href="/horska-kola/">horská kola</a>, <a href="/silnicni-kola/">silniční kola</a> nebo <a href="/trekingova-kola/">trekingová kola</a>.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Helmu čistěte vlažnou vodou a jemným mýdlem, žádná agresivní rozpouštědla, protože poškozují pěnu a lepidla. Vnitřní vložky vyperte podle návodu a nechte uschnout. Helmu nenechávejte v rozpáleném autě ani na topení, vysoká teplota zhoršuje vlastnosti pěny. Při převozu ji nepřetěžujte a neukládejte pod těžké věci. Sleduj praskliny, ohnuté spony a opotřebované popruhy. Výrobci obvykle doporučují vyměnit helmu po několika letech používání, přesný interval najdete v návodu značky. Po jakémkoli silném nárazu helmu vyměňte, i když škody nejsou vidět.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Helma posunutá do týlu, která odkrývá čelo.</li>'
          '<li>Nedotažené popruhy, které umožní při pádu sjetí helmy.</li>'
          '<li>Použití starší helmy po pádu nebo mnoholeté helmy s popraskanou skořepinou.</li>'
          '<li>Nákup podle barvy a ceny bez změření obvodu hlavy.</li>'
          '<li>Půjčení helmy po sourozenci bez nového nastavení.</li>'
          '<li>Ukládání helmy na slunci nebo v rozpáleném autě.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Na Sportece je pohodlné srovnat nabídky českých e-shopů. U každé helmy vidíte, které velikosti jsou skladem, a můžete srovnat dopravu a podmínky vrácení. Nejdřív si změřte obvod hlavy, pak vyberte typ podle jízdy a nakonec značku. Pokud si nejste jistí, objednejte dvě sousední velikosti, správnou si nechte a druhou vraťte v zákonné lhůtě. Sezónní slevy se objevují zpravidla na konci léta, ale oblíbené velikosti se vyprodávají dříve.</p>',
    faq=[('Je cyklistická helma povinná?', 'V Česku musí helmu nosit cyklisté do 18 let, ať jedou po silnici, nebo mimo ni. Dospělým se používání silně doporučuje, ale zákon jim ho neukládá.'),
         ('Jak změřit velikost helmy?', 'Změřte obvod hlavy asi centimetr nad obočím a nad ušima. Hodnotu v centimetrech porovnejte s tabulkou výrobce, protože velikosti S, M a L se mezi značkami liší.'),
         ('Jak správně nasadit helmu?', 'Seďte rovně, přední okraj má být dva prsty nad obočím. Kolečko na zátylku dotáhněte tak, aby helma neklouzala, a řemínek pod bradou nastavte na jeden až dva prsty místa.'),
         ('Kdy helmu vyměnit?', 'Po každém silnějším nárazu, i když nejsou vidět škody, a také když je skořepina popraskaná nebo popruhy rozedrané. Výrobci navíc doporučují obměnu po několika letech používání.'),
         ('Jaký je rozdíl mezi silniční a MTB helmou?', 'Silniční je lehčí a aerodynamická s množstvím větracích otvorů. MTB helma má delší záda, kšilt a lépe kryje zátylek a spánky, protože v terénu hrozí pády do překážek.'),
         ('K čemu slouží systém proti rotačnímu nárazu?', 'Například systém MIPS má snížit přenos rotačních sil na hlavu při šikmém nárazu. Nabízí ho více značek, informace najdete v popisu produktu.'),
         ('Jak vybrat helmu pro dítě?', 'Změřte obvod hlavy a vyberte velikost s regulací. Helma musí sedět už nyní, ne s rezervou na růst. Hodí se barvy a odrazky, které zlepšují viditelnost.'),
         ('Jak čistit cyklistickou helmu?', 'Vlažnou vodou a jemným mýdlem. Žádná rozpouštědla, protože poškozují pěnu a lepidla. Vnitřní vložky vyperte a nechte uschnout při pokojové teplotě.'),
         ('Hodí se městská helma i na sport?', 'Pro krátké a klidné jízdy ano. Na dlouhé a rychlé trasy je lepší větrání silniční helmy a v terénu pevnější krytí MTB modelu.'),
         ('Je lepší dražší helma?', 'Nejdůležitější je správná velikost a nastavení. Dražší modely nabízejí lepší větrání, nižší hmotnost a pohodlnější vložky, ale základní ochranu poskytují i jednodušší přilby.')],
)

# ------------------------------------------------------------------ extensions (extra sections appended to guides)
NEW['tenisova-obuv']['guide'] += (
    '<h2>Poškození, které bota prozradí</h2>'
    '<p>Podle toho, jak se bota opotřebovává, lze odhadnout, zda byla vybraná správně. Sjetá vnější hrana ve špičce ukazuje na hráče, který hodně tahá nohu při podání nebo při pohybu u základní čáry, a hodí se odolnější model s vyztuženou špičkou. Rychle zničená podrážka uprostřed signalizuje nevhodný povrch. Roztržený svršek na boku v místě malíku znamená, že boční opora nestačila a je třeba pevnější konstrukce. Pokud vás po hře bolí chodidla nebo kolena, zkuste novou vložku nebo jinou značku, protože tvar boty se mezi výrobci výrazně liší.</p>'
    '<h2>Sezóna a skladování</h2>'
    '<p>Přes zimu se hraje v hale, přes léto na venkovních kurtech, takže mnoho hráčů střídá dva páry podle období. Boty skladujte na suchém a vzdušném místě, ne v zavřené tašce v autě, kde vlhko podporuje plíseň a zápach. Do vyvětrané boty vložte papír, který nasaje zbytky vlhkosti. Před novou sezónou ověřte stav tkaniček, vložek a lepených spojů, protože malá oprava vyjde levněji než předčasná koupě nových bot.</p>')

NEW['treninkova-obuv']['guide'] += (
    '<h2>Podrážka, mezipodešev a svršek</h2>'
    '<p>Každá část boty plní jinou roli. Podrážka přenáší sílu do podlahy a její směs určuje záběr na různých površích. Mezipodešev, tedy vrstva pěny mezi podrážkou a chodidlem, rozhoduje o tlumení: tenký a pevný přenáší sílu přímo, silný a měkký chrání klouby při skocích, ale zhoršuje stabilitu. Svršek drží chodidlo a chrání je před otěrem. Síťovina je vzdušná a lehká, ale rychleji se prodře, syntetika s tkaným překrytím je odolnější a hůře prodýchává. Pro silový trénink proto upřednostněte odolnost, pro skupinové lekce lehkost a vzdušnost.</p>'
    '<h2>Zahřátí, zotavení a prevence</h2>'
    '<p>Dobrá obuv nenahradí zahřátí. Před tréninkem rozhýbejte kotníky a lýtka, protože obuv s oporou nezabrání přetížení studených svalů. Po tréninku boty vyndejte z tašky a nechte vychladnout. Pokud pocítíte opakovanou bolest v patě, v klenbě nebo kolenou, zkuste jiný typ vložky a poraďte se s odborníkem. Kvalitní vložka někdy pomůže víc než nová bota. Pravidelně kontrolujte šněrování a utáhněte tkaničky tak, aby chodidlo nebylo stlačené, ale ani se nepohybovalo.</p>'
    '<h2>Obuv podle místa tréninku</h2>'
    '<p>Doma na koberci nebo podložce vystačíte s lehčí botou nebo naboso. V komerční posilovně s gumovou podlahou funguje většina tréninkových modelů bez omezení. Na umělém povrchu a v tělocvičně s parketami dbejte, aby podrážka nezanechávala stopy a nebyla příliš hrubá. Pro venkovní workout, například na hřišti s hrazdami, se hodí odolnější podrážka. K domácímu tréninku se hodí i <a href="/svihadla/">švihadla</a> nebo <a href="/kettlebelly/">kettlebelly</a>, u kterých stabilní obuv s pevnou patou oceníte nejvíc; na <a href="/hrazdy-a-bradla/">hrazdy a bradla</a> se zase hodí obuv, která nesklouzává.</p>')

NEW['sportovni-rukavice']['guide'] += (
    '<h2>Vrstvení na ruce podle teploty</h2>'
    '<p>Ruce se chladí rychleji než trup, protože krev v nich teče tenkými cévami a povrch je v poměru k objemu velký. Při teplotách kolem nuly stačí jedna lehčí rukavice, při silném mrazu se vyplatí kombinace tenké spodní a silnější vnější vrstvy. Hodně záleží i na tom, jak se pohybujete: při běhu a běžkování ruce hřejí samy a silná izolace vede k přehřátí a zpocení, při sjezdovém lyžování a na vleku naopak stojíte a ruce chladnou rychleji. Pokud zjistíte, že vám ruce během aktivity zpotily, vyměňte pár nebo ho vysušte, protože vlhkost zhoršuje izolaci. Proto se vyplatí v batohu nosit suchý náhradní pár.</p>'
    '<h2>Rukavice pro děti</h2>'
    '<p>Dětské rukavice musí vydržet vlhkost, protože děti hrají se sněhem a rukavice často promoknou. Hledejte modely s voděodolným povrchem, delší manžetou a gumičkou nebo poutkem, aby je dítě neztrácelo. Pro menší děti jsou lepší palčáky, starší děti už zvládnou prstové rukavice, pokud jsou dobře padnoucí. Zkontrolujte, zda se rukavice dají snadno obléknout a svléknout, jinak je dítě odmítne nosit. Dětské rukavice pořizujte v přiměřené velikosti: příliš velké kloužou a prsty se v nich ztrácejí.</p>'
    '<h2>Sezónní nákup a ověření kvality</h2>'
    '<p>Nejvíc rukavic se prodává od října do prosince. Kvalitní model poznáte podle rovných a pevných švů, spolehlivých zipů nebo suchých zipů a stejnoměrného zateplení bez prázdných míst. Zkontrolujte popis materiálu, kolik vrstev rukavice mají, a zda je u membrány uvedeno, jak je prodyšná. Pokud je nabídka obchodů rozdílná, vyberte tu s jasnou specifikací, aby se předešlo zklamání po doručení. Rukavice lze také zkoušet doma s telefonem v ruce, protože i dotykové špičky se mezi modely liší.</p>')

NEW['cyklisticke-helmy']['guide'] += (
    '<h2>Počasí, viditelnost a sezóna</h2>'
    '<p>Helmu lze používat po celý rok, ale chování se mění s počasím. V létě se vyplatí hodně větracích otvorů a světlá barva, která se méně zahřívá. V chladných měsících pomůže tenká čepice pod helmu nebo model s uzavřenější skořepinou, ovšem čepice nesmí měnit sed popruhů. Na kratší dny je užitečné, aby měla helma světlé barvy, odrazky nebo místo pro blikačku, protože viditelnost řidičům výrazně pomáhá. Při dešti se hodí kšilt, který chrání oči před kapkami. Pokud jezdíte za šera, doplňte helmu <a href="/cyklo-svetla/">světly</a> na kole.</p>'
    '<h2>Helma pro jednotlivé typy kol</h2>'
    '<p>Na <a href="/elektrokola/">elektrokolech</a> se jezdí rychleji, než jezdec čeká, proto někteří výrobci nabízejí helmy s delším krytím zátylku a spánků, které jsou určené pro vyšší tempo. Na <a href="/fatbiky/">fatbicích</a> a v zimě na sněhu je praktické kombinovat helmu s tenkou čapkou. Pro jízdu na <a href="/gravel-kola/">gravelu</a> se používá lehčí silniční helma, na <a href="/bmx-a-dirt-kola/">BMX a dirtu</a> robustnější model s plnější skořepinou. U <a href="/detska-kola/">dětských kol</a> pak dbejte hlavně na jednoduché nastavení a viditelné barvy. Pro převoz kola autem pomohou <a href="/cyklo-nosice-na-auto/">nosiče</a>, helmu však vozte v kabině nebo v zavazadlovém prostoru mezi měkkými věcmi a nikdy ne v rozpáleném autě.</p>'
    '<h2>Rutina před nasazením helmy</h2>'
    '<p>Při nasazování helmy si zvykněte na rutinu: před jízdou zkontrolovat sponu, vyzkoušet zatažení řemínků a ověřit, že helma nemá viditelné praskliny. Brýle a helma se při nasazení nesmí vzájemně rušit, zkuste je kombinovat už v obchodě nebo doma. Pokud nosíte dlouhé vlasy, zvolte model s vyšším zadním otvorem pro culík, případně kolečko, které se dá posunout. Pro děti vždy dohlédněte, aby si helmu nasadily samy a zvykly si na ni jako na součást jízdy. Nejlepší motivací je příklad dospělých, kteří helmu nosí také.</p>')

# ------------------------------------------------------------------ extensions 2
NEW['treninkova-obuv']['guide'] += (
    '<h2>Jak zkoušet obuv doma</h2>'
    '<p>Po doručení boty nejdřív vyzkoušejte na čistém koberci, aby šly případně vrátit. Obujte je s ponožkami na cvičení, zašněrujte od špičky k nártu a projděte se po bytě. Pak si dřepněte, zvedněte se na špičky a udělejte pár výpadů vpřed i do strany. Pata nemá sjíždět a prsty se nemají tlačit do špičky. Zkuste také krátký skok a dopad, protože při něm se ukáže, zda tlumení stačí. Teprve když nic netlačí a bota drží, vyražte do posilovny. Mnoho obchodů umožňuje vrácení v zákonné lhůtě, takže pár minut zkoušky stojí za to.</p>'
    '<h2>Dámské, pánské a dětské modely</h2>'
    '<p>Dámské tréninkové boty mají obvykle užší patu a lehčí konstrukci, pánské širší kopyto a vyšší stabilitu. Rozdíl není pevný a mnoho cvičenců si volí opačnou řadu, pokud jim lépe sedí. Dětské modely mají ohebnou podrážku, protože dětské chodidlo se vyvíjí a potřebuje se přirozeně pohybovat. Pro mladé sportovce v kroužcích je praktické šněrování nebo pevný suchý zip, který děti zvládnou obléknout samy. Menší děti často vyrostou boty dřív, než se opotřebují, proto hlídejte, zda prsty neztratily rezervu před špičkou.</p>'
    '<h2>Kde obuv skladovat a jak ji převážet</h2>'
    '<p>Do sportovní tašky vkládejte boty do samostatné kapsy nebo sáčku, aby nešpinily oblečení a ručník. Nenechávejte je v autě, kde se v létě zahřívají a v zimě zmrznou. Správné uskladnění prodlužuje život lepidla a pěny. Pokud se vám v botě drží zápach, pomůže vyvětrání, vyměnitelná vložka nebo sáček s pohlcovačem vlhkosti. Pravidelné čištění ušetří peníze a zlepší pohodlí, protože čisté a suché boty méně zapáchají a vydrží déle. Sundané boty vždy nechte oschnout, než je zavřete do tašky nebo skříňky.</p>')

NEW['sportovni-rukavice']['guide'] += (
    '<h2>Jak vybrat podle sportu krok za krokem</h2>'
    '<p>Nejdřív si ujasněte, kolik času budete trávit venku a jak intenzivně se budete hýbat. Pokud půjde o procházky se psem a běžné chození, postačí tenká fleecová rukavice. Při lyžování a snowboardu nepodceňujte nepromokavost, protože pády a práce s vázáním znamenají kontakt se sněhem. Skialpinisté ocení rukavice, které rychle schnou a mají odolnou dlaň, aby ji nepoškodily hrany lyží. Pro běžecké lyžování zvolte tenčí a prodyšnější model, jinak se ruce zpotí. Pro krátké dojíždění na kole stačí dlaně s tenkým polstrováním, na dlouhé trasy delší manžeta a gel. Všechny kategorie najdete v hlavní nabídce <a href="/sportovni-obleceni/">sportovního oblečení</a>.</p>'
    '<h2>Rukavice a technologie</h2>'
    '<p>U moderních rukavic se můžete setkat s mnoha označeními. Membrána brání prostupu vody, ale potřebuje péči, aby neztratila funkci. Zesílení na dlani prodlužuje životnost a zvyšuje přilnavost na holích nebo řidítkách. Mnohé modely mají vylisované nebo zesílené oblasti na prstech pro lepší úchop. Dotykové špičky umožňují ovládat telefon bez sundání rukavice, ale jejich citlivost bývá nižší než u holé ruky. Poutka na zápěstí a karabinky umožňují připevnit rukavice na bundu nebo batoh, aby se neztratily. Zvažte, které prvky potřebujete, protože s každým přibývá komplexnost a někdy i hmotnost.</p>'
    '<h2>Zdravotní a bezpečnostní rady</h2>'
    '<p>Pokud vám ruce v zimě často mrznou nebo bílají, rukavice pomůžou, ale poraďte se také s lékařem, protože může jít o poruchu prokrvení. Při dlouhém pobytu v mrazu kontrolujte prsty, a pokud ztrácí cit nebo se zbarvují, vraťte se do tepla. Nikdy nepoužívejte mokré rukavice déle, než je nutné, protože vlhkost urychluje prochladnutí. Děti kontrolujte častěji než dospělé, protože si nemusí stěžovat včas. Rukavice nesmí omezovat ovládání řidítek, brzdových páček ani lyžařských holí.</p>')

NEW['cyklisticke-helmy']['guide'] += (
    '<h2>Rozdíly mezi značkami</h2>'
    '<p>Značky se liší tvarem skořepiny a vnitřním tvarem. Některé helmy sedí lépe na delší oválnější hlavě, jiné na kulatější. Proto se může stát, že velikost M jedné značky vám padne a u jiné ne, i když má stejný obvod. Pokud už víte, který tvar vám vyhovuje, držte se podobných modelů. Nabídka na Sportece zahrnuje známé evropské značky i levnější varianty. U všech si prohlédněte popis, uváděný rozsah obvodu v centimetrech a počet větracích otvorů. Zkušenosti jiných kupujících jsou užitečné, ale rozhodnout musí vaše hlava a pohodlí.</p>'
    '<h2>Tipy pro nošení během dne</h2>'
    '<p>Nasazujte helmu při každé jízdě, i krátké. K pádu může dojít kdykoli, i na krátké a dobře známé trase. Pokud si helmu odkládáte v kanceláři nebo škole, připněte ji na batoh nebo na zámek kola a nepokládejte ji na zem, kde se může poškodit. Ani dlouhé nošení nevadí, pokud je helma správně nastavená a nese ji celá hlava rovnoměrně. Pokud vás tlačí, nepřestávejte ji nosit, ale změňte nastavení nebo model. Při pohybu v týmu vzájemně kontrolujte, že mají všichni popruhy správně dotažené.</p>')
