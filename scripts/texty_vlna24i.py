"""sporteka.cz — wave 24i (5. 11. 2026): long texts for detska-kola-24-palcu, pozemni-hokej, krosova-kola, nahradni-zorniky.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ detska-kola-24-palcu
NEW['detska-kola-24-palcu'] = dict(long=True,
    title='Dětská kola 24 palců: velikost, váha, převody, výběr',
    desc='Dětská a juniorská kola s koly 24 palců pro školáky. Jak vybrat rám, váhu, brzdy a převody a porovnat nabídky českých obchodů na jednom místě.',
    intro='<p>Kolo s 24palcovými koly je typická volba pro školáka, který odrostl dvacítku, ale na dospělý rám je ještě malý. Obvykle ho dostane kolem deseti až dvanácti let a pojede na něm několik sezón, takže se vyplatí vybírat s rozmyslem. Rozhoduje především výška dítěte a délka jeho nohou, hmotnost kola, kvalita brzd a rozsah převodů. Sporteka porovnává nabídky českých obchodů u dívčích, chlapeckých i unisex modelů od městských po horské.</p>'
          '<p>V kategorii najdete značky ' + B(('rascal', 'Rascal'), ('olpran', 'Olpran'), ('davi', 'Davi'), ('canellini', 'Canellini'), ('canull', 'Canull'), ('early-rider', 'Early Rider'), ('attabo', 'Attabo'), ('stahoo', 'Stahoo'), ('dino-bikes', 'Dino Bikes')) +
          '. Mladším dětem se hodí <a href="/detska-kola-20-palcu/">kola 20 palců</a>, starším už spíš <a href="/horska-kola/">horská kola</a> nebo <a href="/krosova-kola/">krosová kola</a>. Celý přehled je v kategorii <a href="/detska-kola/">dětská kola a odrážedla</a>.</p>',
    guide='<h2>Pro koho je kolo 24 palců</h2>'
          '<p>Průměr kola se udává v palcích a u dětských kol je to nejjednodušší vodítko, které velikosti se dítě blíží. Dvacet čtyři palců je poslední dětská velikost před kolem pro dospělé, a proto se dělí na dva různé světy. Jedním jsou lehké dětské a juniorské modely s malým rámem a krátkými klikami, druhým kola, která se dospělým strojům podobají téměř ve všem kromě rozměrů rámu.</p>'
          + T(['Výška dítěte', 'Orientačně věk', 'Doporučená velikost kol'], [
              ['do cca 115 cm', '4 až 5 let', '<a href="/detska-kola-16-palcu/">16 palců</a>'],
              ['cca 115 až 130 cm', '6 až 8 let', '<a href="/detska-kola-20-palcu/">20 palců</a>'],
              ['cca 130 až 150 cm', '8 až 12 let', '24 palců'],
              ['nad cca 150 cm', 'od 11 až 12 let', '26 až 27,5 palce nebo dospělý rám S']]) +
          '<p>Hodnoty jsou jen orientační. Věk je špatný ukazatel, protože děti stejného věku se liší o hlavu. Spolehlivější je zkouška: dítě na kole musí na sedle dosáhnout alespoň špičkami obou nohou na zem, při šlapání mít mírně pokrčené koleno a při chytání řídítek lehce pokrčené lokty. Nikdy nekupujte kolo o číslo větší s tím, že do něj dítě dorůstá. Příliš velký rám znamená špatnou ovladatelnost, nejisté brzdění a hlavně strach z pádu.</p>'
          '<h2>Typy dětských kol 24 palců</h2>'
          '<p>Podle terénu a výbavy se dají kola rozdělit do několika skupin. Dítě, které jezdí do školy po chodníku a dvakrát týdně na hřiště, potřebuje jiný stroj než malý závodník nebo výletník.</p>'
          '<h3>Horská (MTB) kola</h3>'
          '<p>Nejčastější typ v této velikosti. Mají hrubší pláště, odpruženou nebo pevnou vidlici a pevný rám. V nabídce jsou chlapecké modely s ostrou grafikou i dívčí s košíkem a blatníky, které se od sebe liší většinou jen barvou a výbavou. Skutečně terénní jízdu zvládnou lépe modely s lehkým rámem, vyšší kvalitou brzd a širším rozsahem převodů.</p>'
          '<h3>Městská a trekingová výbava</h3>'
          '<p>Některá kola mají blatníky, nosič, stojánek, osvětlení a zvonek, takže se hodí na dojíždění do školy i výlety po cyklostezkách. Naopak sportovní modely bývají prodávány bez těchto doplňků a je potřeba je dokoupit, viz <a href="/cyklo-blatniky/">blatníky</a>, <a href="/cyklo-svetla/">světla</a> a <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>.</p>'
          '<h3>Odlehčená kola pro děti</h3>'
          '<p>Několik výrobců se zaměřuje na kola, jejichž hmotnost je výrazně nižší než u obvyklých obchodních řetězců. V názvech modelů se objevuje slovo ultralight a hmotnost kolem jedenácti kilogramů. U dítěte to hraje obrovskou roli: když váží kolo třetinu váhy jezdce, bude mu těžko zatáčet, přenášet ho přes obrubník nebo vytlačit do kopce. Lehčí kolo je zábavnější a dítě na něm jezdí víc.</p>'
          '<h3>Dětské BMX a sportovní modely</h3>'
          '<p>V této velikosti se objevují i kola pro závodnější a freestylovou jízdu. Jsou kratší, mají jednu rychlost a pevné vidlice. Pro běžné používání na silnici nejsou ideální, ale pro dětský pumptrack nebo skatepark se hodí. Příbuznou kategorii najdete u <a href="/bmx-a-dirt-kola/">BMX a dirt kol</a>.</p>'
          '<h2>Na co se zaměřit před nákupem</h2>'
          '<h3>Hmotnost</h3>'
          '<p>Je to nejdůležitější parametr po velikosti. Levná kola bývají těžká, protože mají ocelový rám, plná kola a masivní komponenty. Dítě si je nemusí všimnout při koupi, ale pozná to při první delší cestě do kopce. Porovnávejte hmotnost uvedenou v popisu a ověřte, zda jde o hmotnost bez pedálů, nebo se všemi doplňky.</p>'
          '<h3>Brzdy</h3>'
          '<p>Dětská ruka má menší sílu stisku. Důležité jsou proto krátké páky nastavitelné do blízkosti řídítek a brzdy, které reagují bez velkého úsilí. U ráfkových brzd (V-brake) kontrolujte, že se páky dají dosáhnout i malou rukou. Kotoučové brzdy dávají stálejší brzdný účinek v dešti a vyžadují menší sílu, ale jsou náročnější na seřízení. Více o jejich typech a výměně se dočtete v části <a href="/cyklo-brzdy/">brzdy</a>.</p>'
          '<h3>Převody</h3>'
          '<p>Většina kol má přehazovačku a sedm až dvacet jedna rychlostí. Pro dítě je důležitější jednoduché řazení než vysoký počet převodů. Měnič, který se dá ovládat otočnou rukojetí nebo malou páčkou, se učí rychle. Když dítě jezdí jen po rovině, stačí i několik převodů a nižší hmotnost. Pro kopcovitý terén se hodí širší rozsah s lehkým převodem do kopce.</p>'
          '<h3>Vidlice a odpružení</h3>'
          '<p>Odpružená vidlice na levném dětském kole často jen přidává váhu a přitom dobře nefunguje, protože ji dítě svou hmotností nestlačí. Pevná vidlice je lehčí a spolehlivější. Odpružení má smysl až u dražších modelů s nastavitelnou tuhostí, viz <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>.</p>'
          '<h3>Pedály, kliky a sedlo</h3>'
          '<p>Krátké kliky a menší sedlo dělají kolo příjemnější než zmenšený model dospělého kola. Pedály s větší plochou drží botu lépe, pro děti které jezdí v tenisce se hodí základní plastové nebo kovové s hroty. Na výměnu se podívejte do kategorie <a href="/cyklo-pedaly/">pedály</a> a <a href="/cyklo-sedacky-a-voziky/">sedla</a>.</p>'
          '<h2>Povinná výbava a bezpečnost</h2>'
          '<p>Základem je <a href="/detske-cyklohelmy/">dětská cyklistická helma</a>, která dobře sedí, nesklouzává do čela a má utažený podbradní pásek. Do šera a tmy patří přední bílé a zadní červené světlo, odrazky a reflexní prvky na oblečení, viz <a href="/cyklo-svetla/">cyklo světla</a>. Zamykání kola před školou nebo obchodem zajišťují <a href="/cyklo-zamky/">zámky</a>. Při jízdě mimo silnici se hodí <a href="/cyklisticke-rukavice/">cyklistické rukavice</a> a pro sjezdy i chrániče kolen a loktů, viz <a href="/cyklo-chranice/">chrániče</a>.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Kolo dítěte není tak namáhané jako dospělé, ale pravidelnou kontrolu potřebuje. Před sezónou zkontrolujte tlak v pláštích, utažení šroubů, stav brzdových destiček a promazání řetězu. Dítě se do kola učí posadit samo, takže je dobré, když ho dokáže i obsloužit: dofouknout, uzamknout, zkontrolovat zvonek. Použijte <a href="/cyklo-pumpy-a-naradi/">pumpičku a základní nářadí</a> a na údržbu řetězu <a href="/cyklo-udrzba/">čistící a mazací prostředky</a>. Když dítě poroste, posuňte sedlo a řídítka, a pokud už nestačí, kolo předejte mladšímu sourozenci. Kvalitnější kola si drží hodnotu i při prodeji z druhé ruky.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Kolo „na dorost“.</strong> Příliš velký rám dítěti ztěžuje brzdění a zvyšuje riziko pádu.</li>'
          '<li><strong>Výběr podle počtu rychlostí.</strong> Vyšší počet nic neříká o kvalitě, důležité je řazení a hmotnost.</li>'
          '<li><strong>Zbytečné odpružení.</strong> U levných modelů přidává váhu a málokdy pracuje.</li>'
          '<li><strong>Zapomenuté doplňky.</strong> Helma, světla a zámek by měly být součástí rozpočtu od začátku.</li>'
          '<li><strong>Bez vyzkoušení.</strong> Dítě by si mělo kolo alespoň posadit a zkusit sáhnout na brzdové páky.</li></ul>'
          '<h2>Co dál</h2>'
          '<p>Až dítě přeroste 24 palců, přejde na dospělá kola v nejmenších rámech: <a href="/damska-kola/">dámská kola</a>, <a href="/mestska-kola/">městská kola</a> nebo nižší horská kola. Pokud chcete dítěti usnadnit kopce, existuje i <a href="/detska-elektrokola/">dětské elektrokolo</a>. A když dítě chce dopravní prostředek na kratší vzdálenosti, hodí se <a href="/kolobezky/">koloběžky</a>.</p>',
    faq=[('Kolik let má dítě na kole 24 palců?', 'Nejčastěji se bere věk kolem 8 až 12 let, ale rozhoduje výška dítěte a délka nohou. Dítě mezi 130 a 150 cm obvykle vyhovuje právě tato velikost.'),
         ('Jak poznám, že je kolo správně velké?', 'Dítě sedí na sedle a špičkami dosáhne na zem, při šlapání má mírně pokrčené koleno a lokty při držení řídítek nejsou natažené. Při stání nad rámem by mělo zbýt několik centimetrů místa.'),
         ('Mám koupit kolo o číslo větší, aby vydrželo déle?', 'Ne. Příliš velké kolo je hůř ovladatelné a hrozí pády. Lepší je pořídit kvalitní kolo správné velikosti a po dětech ho předat dál.'),
         ('Jaká hmotnost je pro dětské kolo vhodná?', 'Čím nižší, tím lépe. Lehká kola, často označená jako ultralight, váží kolem 11 kg, zatímco obchodní řetězce nabízejí i podstatně těžší modely. Hmotnost je u malého jezdce vidět v kopcích i při přenášení kola.'),
         ('Hodí se odpružená vidlice na dětské kolo?', 'Jen u kvalitnějších modelů s nastavitelnou tuhostí. U levných kol bývá odpružení málo funkční a přidává hmotnost, pevná vidlice je spolehlivější.'),
         ('Jaké brzdy zvolit pro dítě?', 'Důležitý je dosah páky pro malou ruku a lehký chod. Ráfkové brzdy jsou jednodušší, kotoučové mají stálejší účinek v dešti, ale vyžadují správné seřízení.'),
         ('Kolik převodů dítě potřebuje?', 'Na rovinu a město stačí několik rychlostí, do kopců se hodí širší rozsah. Důležitější než jejich počet je snadné ovládání řazení malou rukou.'),
         ('Jaké doplňky k dětskému kolu nezapomenout?', 'Helmu, přední a zadní světlo, odrazky, zvonek a zámek. Podle použití přibývají blatníky, nosič a rukavice.'),
         ('Jak často kolo kontrolovat?', 'Před sezónou a pak průběžně: tlak v pláštích, utažení šroubů, brzdy a promazání řetězu. Rychlou kontrolu stojí za to udělat před delší trasou.'),
         ('Je lepší dívčí, nebo chlapecké kolo?', 'Rozdíl je většinou v barvě a výbavě, jako je košík nebo blatníky. Rám bývá nižší u modelů s otevřeným předním trojúhelníkem, což usnadňuje nasedání. Vyberte podle velikosti a použití, ne podle označení.'),
         ('Kdy dítě přejde na větší kolo?', 'Když sedlo vysunuté na maximum nestačí a kolena při šlapání narážejí do řídítek. Pak je čas na 26 nebo 27,5 palce, případně nejmenší dospělý rám.')],
)

# ------------------------------------------------------------------ pozemni-hokej
NEW['pozemni-hokej'] = dict(long=True,
    title='Pozemní hokej: hole, boty, rukavice, výstroj a míčky',
    desc='Vybavení na pozemní hokej: hole, boty na umělku nebo do haly, rukavice, masky, míčky a tašky. Jak vybrat a porovnat nabídky českých obchodů.',
    intro='<p>Pozemní hokej se hraje na umělém trávníku, v hale i na hřišti s pískem a výbava je odlišná od ledního hokeje i florbalu. Hráč potřebuje hůl s rovnou stranou, tvrdý míček, boty s vhodnou podrážkou, chránič zubů, často rukavici na levou ruku a chrániče holení. Sporteka srovnává nabídky českých obchodů na hole, obuv, rukavice, masky pro obranu na rohy, míčky, tašky, batohy a oblečení klubů. V nabídce je i drobné příslušenství jako karty pro rozhodčí nebo trenérské tabule.</p>'
          '<p>Najdete zde značky ' + B(('korok', 'Korok'), ('balling', 'Balling'), ('grays', 'Grays'), ('adidas', 'Adidas'), ('osaka', 'Osaka'), ('dita', 'Dita'), ('asics', 'Asics')) +
          '. Společné prvky s lednim sportem popisují <a href="/hokej/">hokej</a>, příbuznou halovou hru najdete v <a href="/florbal/">florbalu</a> a obuv shrnuje <a href="/salova-obuv/">sálová obuv</a>.</p>',
    guide='<h2>Čím se pozemní hokej liší od jiných hokejových sportů</h2>'
          '<p>Pozemní hokej je starší než lední i florbal a základní pravidla jsou jiná. Míček se hraje jen plochou stranou hole, hůl se nesmí zvednout nad ramena a hráči nejsou chráněni jako na ledě. Míček je tvrdý a při vysoké rychlosti zraňuje, a proto pozemní hokej vyžaduje vlastní ochranu. Nemůžete ho nahradit florbalovou holí ani bruslařskými chrániči. Do hry patří dvě hlavní varianty: venkovní na umělé trávě a halová na parketách, kde se používají jiné boty a holí se hraje jinak.</p>'
          + T(['Varianta', 'Povrch', 'Obuv', 'Poznámka'], [
              ['Venkovní', 'umělý trávník, písková umělka', 'podrážka s malými nopy nebo vzorkem', 'standardní míček, chránič zubů, holeně'],
              ['Halová', 'parkety, sportovní podlahy', 'plochá hladká podrážka', 'rukavice a často hladký míček'],
              ['Trénink a rekreace', 'hřiště, školní tělocvična', 'univerzální tréninková obuv', 'podle způsobu hry, ochranu nepodceňovat']]) +
          '<h2>Pozemní hokejky</h2>'
          '<p>Hůl pro pozemní hokej má zakřivený tvar s rovnou stranou a hodí se pro hru plochou stranou. Vyrábí se z dřeva, kompozitu, skelných vláken a uhlíku. Dřevěné hole jsou levnější a spíš pro děti a začátečníky, kompozity jsou lehčí, tužší a vhodné pro rychlejší hru. Délka se volí tak, aby hůl při postavení na zem sahala k pasu až k hornímu okraji stehna. Obránci často volí o něco delší hůl, útočníci spíše kratší. Rozdílné křivky čepele (late bow, mid bow, low bow) ovlivňují, jak snadno se zvedá míček a jak jde zpracovávat kličky. V nabídce se objevují modely pro dospělé, například řada označená jako World Cup.</p>'
          '<h3>Obaly a tašky na hole</h3>'
          '<p>Hole chrání obal, do kterého se vejde i rukavice a míček. Malý obal pojme jednu hůl, větší taška i několik holí, boty a ochranné pomůcky. Pro mladé hráče jsou k dispozici <a href="/sportovni-tasky/">sportovní tašky</a> a <a href="/batohy/">batohy</a> v klubových barvách.</p>'
          '<h2>Boty na pozemní hokej</h2>'
          '<p>Správná obuv je pro pozemní hokej klíčová. Při rychlých obratech a zastavování se zatěžuje kotník i koleno, a špatná podrážka zvyšuje riziko skluzu. V nabídce jsou dětské modely na suchý zip i šněrování, pánské a dámské boty pro dospělé a samostatné sálové boty.</p>'
          '<ul><li><strong>Venkovní boty:</strong> mají gumovou podrážku s drobnými nopy nebo vroubkem, které drží na umělé trávě. Nejsou vhodné do haly, kde by zanechávaly stopy.</li>'
          '<li><strong>Sálové boty:</strong> hladká a lehce lepivá podrážka z gumy pro parkety. Podobné jsou u <a href="/salova-obuv/">sálové obuvi</a>.</li>'
          '<li><strong>Univerzální tréninková obuv:</strong> pro školní hodiny a rekreační hru, viz <a href="/treninkova-obuv/">tréninková obuv</a>.</li></ul>'
          '<p>Při měření nohy vždy počítejte s ponožkou a zhruba půl centimetru místa před palcem. Děti rostou rychle, takže velikost kontrolujte před každou sezónou. Boty od různých značek mají jiný střih: Asics sedí odlišně než Adidas nebo Osaka, a proto se vyplatí zkoušet. Více k výběru najdete v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Rukavice a ochrana rukou</h2>'
          '<p>Většina hráčů nosí rukavici na levé ruce, která drží hůl nahoře a je při hře nejvíc odkrytá. Nabízejí se krátké rukavice s ochranou hřbetu, dlouhé s ochranou celých prstů a speciální halové s tenkou pěnou. Rukavice na ochranu dvou článků prstů přináší vyšší bezpečnost, ale omezuje jemný pohyb. Pro obránce při krátkých rozích se hodí tužší ochrana, pro útočníky něco tenčího. Rukavice se prodávají na levou i pravou ruku, takže při koupi ověřte, pro kterou je určena. Souvisejí s ní <a href="/sportovni-rukavice/">sportovní rukavice</a> a pro jiné hokejové ochranné pomůcky <a href="/hokejove-chranice/">hokejové chrániče</a>, ale ne vždy jsou vzájemně zaměnitelné.</p>'
          '<h2>Masky a ochranné pomůcky</h2>'
          '<p>Při obraně krátkých rohů (penalty corner) stojí hráči před míčkem letícím vysokou rychlostí a ochranná maska se silně doporučuje, v mnoha soutěžích je povinná. Obličejová maska chrání oči, nos a zuby, vyrábí se z PVC nebo kovové mřížky. Zubní chránič patří do výbavy každého hráče bez ohledu na věk. Chrániče holení jsou povinné v mnoha ligách, a pokud nejsou, jsou silně doporučeny. Brankář má odlišnou a rozsáhlejší výstroj, kterou v této kategorii nehledejte; podobné prvky popisují <a href="/hokejove-brankarske-vybaveni/">hokejové brankářské vybavení</a>, ale nejsou zaměnitelné.</p>'
          '<h2>Míčky</h2>'
          '<p>Míček je tvrdý plastový a různé typy se liší povrchem. Hladký míček se používá na zápasech na umělé trávě, často bílý nebo žlutý, aby byl vidět. Míček s pozvolným vzorkem, na zápasy a tréninky, drží lépe stopu při hře na písku a v hale. Halové míčky bývají lehčí a pružnější. Existují i dekorativní míčky se třpytkami, které se hodí pro mladé hráče. Míčky se opotřebovávají nárazy a ztrácí kulatost, a proto jich mějte víc než jeden.</p>'
          '<h2>Oblečení a oddíl</h2>'
          '<p>Pozemní hokej se hraje v sukních, kraťasech a dresech s vlastním designem klubu. Dívčí a dámské sukně zajišťují volný pohyb nohou, kraťasy se prodávají v chlapeckém i pánském střihu. K tréninku se hodí tepláky, bundy a ponožky, které dobře odvádějí pot. Pokud hledáte obecné oblečení, projděte <a href="/sportovni-sukne-a-saty/">sportovní sukně a šaty</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/teplaky/">tepláky</a>.</p>'
          '<h2>Příslušenství pro trenéry a rozhodčí</h2>'
          '<p>V kategorii najdete také trenérské tabule k nácviku taktiky a karty pro rozhodčí (zelená, žlutá a červená). Trenér má pomůcku, ze které rychle vysvětlí rozestavení, a rozhodčí karty, které jasně ukazují udělený trest. Zápasové pomůcky doplňují píšťalky a stopky v kategorii <a href="/hokej/">hokej</a>.</p>'
          '<h2>Péče o výstroj</h2>'
          '<p>Po tréninku boty vyndejte z tašky a nechte vyschnout, nikdy je nesušte na topení. Hole utírejte, kontrolujte konce a čepel na třísky. Rukavice větrejte a při silném zápachu perte podle pokynů výrobce. Obal na hůl chrání hůl i před sluncem v autě, kde se přehřívá. Míčky skladujte mimo přímé slunce.</p>'
          '<h2>Nejčastější chyby začátečníků</h2>'
          '<ul><li><strong>Hokejka od jiného sportu.</strong> Florbalová hůl ani lední hokejka pro hru nevyhovují.</li>'
          '<li><strong>Chybějící ochrana.</strong> Zubní chránič a ochrana holení by měly být samozřejmostí.</li>'
          '<li><strong>Špatná obuv.</strong> Hladké tenisky na umělé trávě kloužou, venkovní boty v hale zanechávají šmouhy.</li>'
          '<li><strong>Příliš dlouhá hůl.</strong> Zhoršuje kontrolu míčku a drží hráče ve špatné poloze.</li></ul>',
    faq=[('Čím se liší pozemní hokej od ledního hokeje?', 'Hraje se na trávě nebo v hale, míček je tvrdý a hraje se jen plochou stranou hole. Hůl má jednostranně zakřivenou čepel a nesmí se zvedat nad ramena.'),
         ('Jak vybrat délku hole na pozemní hokej?', 'Hůl postavená na zem by měla sahat zhruba k pasu až k horní části stehna. Obránci často volí delší, útočníci kratší hůl.'),
         ('Jaké boty na pozemní hokej koupit?', 'Na umělou trávu boty s malými nopy nebo vroubkem, do haly boty s plochou hladkou podrážkou. Univerzální tréninková obuv se hodí pro rekreaci.'),
         ('Na kterou ruku patří rukavice?', 'Nejčastěji na levou, protože drží hůl nahoře a je při hře nejvíc odkrytá. Prodávají se i modely pro pravou ruku, takže při koupi ověřte stranu.'),
         ('K čemu slouží maska při pozemním hokeji?', 'Chrání obličej při obraně krátkých rohů, kdy míček letí vysokou rychlostí. Nehodí se pro celou hru, ale pro dané situace se silně doporučuje a v mnoha soutěžích je povinná.'),
         ('Jaké míčky se používají?', 'Hladké míčky na zápasy na umělé trávě, míčky se vzorkem na tréninky a halové varianty do tělocvičen. Liší se rozměry povrchu a pružností.'),
         ('Je zubní chránič povinný?', 'V mnoha soutěžích ano a vždy se doporučuje. Míček a hole zraňují zuby i při běžné hře.'),
         ('Hodí se florbalová hůl na pozemní hokej?', 'Ne. Florbalová hůl je lehčí, má jinou čepel a není určena na tvrdý míček. Pozemní hokej vyžaduje vlastní hůl.'),
         ('Co všechno potřebuje začátečník?', 'Hůl, boty vhodné pro povrch, zubní chránič, chrániče holení, rukavici a míček. Další výstroj přidáte podle role a úrovně hry.'),
         ('Jak se starat o hůl?', 'Utírat po tréninku, chránit před teplem v autě a kontrolovat čepel. Praskliny kompozitu a třísky na dřevěné hole jsou důvod k výměně.'),
         ('Pro koho jsou dětské boty a rukavice?', 'Pro mladé hráče v klubech a školních kroužcích. Dětská výbava má menší rozměry a u bot se vyskytují zavírání na suchý zip pro snazší obouvání.')],
)

# ------------------------------------------------------------------ krosova-kola
NEW['krosova-kola'] = dict(long=True,
    title='Krosová kola: crossová, fitness a cyklokros, výběr',
    desc='Krosová a crossová kola na silnici, cyklostezky i šotolinu, včetně cyklokrosových. Jak vybrat rám, brzdy a převody a porovnat nabídky obchodů.',
    intro='<p>Krosové kolo, často psané crossové, je rychlá a univerzální volba pro jízdu po silnici, cyklostezkách a zpevněných cestách. Má rovné řídítko, 28palcová kola a užší pláště než horské kolo, takže jede lehce a udrží vyšší tempo. Do stejné kategorie se řadí i trekingové varianty s výbavou a cyklokrosová kola s beranem a širšími plášti. Sporteka srovnává nabídky českých obchodů u dámských a pánských modelů a ukazuje, které velikosti jsou skladem.</p>'
          '<p>Najdete zde značky ' + B(('kellys', 'Kellys'), ('kross', 'Kross'), ('author', 'Author'), ('specialized', 'Specialized'), ('attabo', 'Attabo'), ('van-rysel', 'VAN Rysel'), ('cyclision', 'Cyclision'), ('olpran', 'Olpran')) +
          '. Podobné jsou <a href="/trekingova-kola/">trekingová kola</a>, <a href="/mestska-kola/">městská kola</a>, <a href="/horska-kola/">horská kola</a> a <a href="/gravel-kola/">gravel kola</a>.</p>',
    guide='<h2>Kdy se krosové kolo hodí</h2>'
          '<p>Krosové kolo využijete, když jezdíte převážně po zpevněném povrchu a chcete víc rychlosti než nabízí horské kolo, ale pohodlnější sed než na silničce. Typicky jde o cestu do práce, rekreační výlety po cyklostezkách, fitness jízdu a delší vyjížďky po okreskách. Na kořeny a kameny není stavěné. Pro terén mají lepší pneumatiky a geometrii <a href="/horska-kola/">horská kola</a>, pro dlouhé cesty s bagáží lépe poslouží <a href="/trekingova-kola/">trekingová kola</a>. Hranice mezi nimi je neostrá a stejný model se někdy v obchodech nazývá městský, crossový nebo trekingový.</p>'
          + T(['Typ kola', 'Řídítka', 'Pláště', 'Nejlepší využití'], [
              ['Krosové / fitness', 'rovné', 'užší, cca 32 až 45 mm', 'silnice, cyklostezky, šotolina'],
              ['Trekingové', 'rovné nebo mírně zahnuté', 'střední až širší', 'dlouhé výlety s bagáží'],
              ['Městské', 'rovné, často vyšší sed', 'širší, odolné', 'krátká dojíždění po městě'],
              ['Cyklokrosové', 'beran', 'úzké pláště s hrubým vzorkem', 'závody v blátě, trénink, rychlé terénní jízdy'],
              ['Gravel', 'beran', 'širší než silnice, užší než MTB', 'dlouhé trasy po silnici i šotolině']]) +
          '<h2>Typy krosových kol</h2>'
          '<h3>Klasická crossová kola</h3>'
          '<p>Nejpočetnější skupina. Mají hliníkový rám, přední vidlici (pevnou nebo odpruženou), 28palcová kola a výbavu odpovídající ceně. Mnoho modelů je k dispozici v pánském rámu a v dámské variantě s nižší horní trubkou. V nabídce jsou kola s hmotností zhruba mezi čtrnácti a šestnácti kilogramy podle výbavy.</p>'
          '<h3>Fitness a lehké modely</h3>'
          '<p>Důraz na nízkou hmotnost, tenké pláště a pevné vidlice. Jsou rychlejší, ale méně odpouštějí nerovnosti. Hodí se, když chcete jezdit tempo na silnici a nepotřebujete nosič ani blatníky. Pokud tuto jízdu považujete za sport, zvažte i <a href="/silnicni-kola/">silniční kola</a>.</p>'
          '<h3>Cyklokrosová kola</h3>'
          '<p>Ve výběru se objevují i cyklokrosová kola, která mají jiné určení než crossová. Mají beran jako silničky, pláště s hrubším vzorkem, volnější rám pro blátivou trať a často kotoučové brzdy. Používají se na závody v blátě a písku, ale zároveň se dají využít jako všestranný stroj pro rychlé jízdy po šotolině. V nabídce jsou modely s elektronickým řazením, které patří mezi nejvýkonnější. Podobné využití mají <a href="/gravel-kola/">gravel kola</a> a <a href="/silnicni-a-gravel-kola/">silniční a gravel kola</a>.</p>'
          '<h2>Rám a velikost</h2>'
          '<p>Rám se udává v palcích nebo písmeny (S, M, L, XL) a odpovídá výšce postavy a délce nohou. Výrobci často uvádějí rozmezí výšky, třeba 168 až 180 cm pro rám M s 19 palci, a je lepší se jím řídit než hádat.</p>'
          + T(['Výška postavy', 'Orientační rám', 'Písmeno'], [['do 165 cm', '15 až 17"', 'S'], ['165 až 178 cm', '17 až 19"', 'M'], ['178 až 188 cm', '19 až 21"', 'L'], ['nad 188 cm', '21 až 23"', 'XL']]) +
          '<p>Při zkoušce byste měli při stání nad horní trubkou mít několik centimetrů odstup a při šlapání mírně pokrčené koleno. Příliš dlouhý rám nutí přetahovat ruce, příliš krátký tlačí kolena k řídítkům. Pokud se pohybujete na hranici dvou velikostí, vybírejte podle délky trupu a pohodlí. Nastavit se dá výška sedla a představce, ale rám se již nezmění. Víc o sedle najdete v části <a href="/cyklo-sedacky-a-voziky/">sedla</a> a o řídítkách v části <a href="/cyklo-riditka/">řídítka</a>.</p>'
          '<h2>Pláště a kola</h2>'
          '<p>Většina krosových kol je na 28" kolech (zhruba 700C). Úzký plášť je rychlejší na asfaltu a hůře snáší šotolinu, širší dává komfort a trakci a je pomalejší. Poradí se s výrobcem, jaký největší plášť se do rámu vejde. Pláště a duše jsou spotřební díl a dobře se vyplatí kontrolovat tlak, protože tlak v pláštích ovlivňuje odpor i pohodlí. Nabídku najdete v <a href="/plaste-a-duse/">pláštích a duších</a> a <a href="/cyklo-kola-a-rafky/">kolech a ráfcích</a>.</p>'
          '<h2>Brzdy, převody a vidlice</h2>'
          '<h3>Brzdy</h3>'
          '<p>Hydraulické kotoučové brzdy se prosadily, protože brzdí stejně v suchu i v dešti a páky se ovládají lehce. Mechanické kotoučové jsou levnější a jednodušší na údržbu, ráfkové jsou nejlehčí a nejlevnější, ale v mokru ztrácejí účinek. Při jízdě s nákladem a ve sjezdech jsou kotoučové jednoznačná volba. Viz <a href="/cyklo-brzdy/">brzdy</a>.</p>'
          '<h3>Převody</h3>'
          '<p>Krosová kola mají od několika rychlostí po široké rozsahy kolem dvaceti sedmi. Pro rovinu a město stačí méně převodů, pro kopce hledejte větší kazetu vzadu. Moderní uspořádání s jedním předním převodníkem je jednodušší na ovládání a méně náchylné k poruchám. Kompletní přehled souvisí s <a href="/cyklo-pohon/">pohonem</a>.</p>'
          '<h3>Vidlice</h3>'
          '<p>Pevná vidlice je lehčí a bez údržby, odpružená tlumí nárazy na hrubším povrchu. Na hladkém asfaltu se odpružení většinou nevyplatí, v nerovném městě a na šotolině ano. Více v části <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>.</p>'
          '<h2>Výbava na dojíždění a výlety</h2>'
          '<p>Chcete-li krosové kolo používat jako dopravní prostředek, zvažte <a href="/cyklo-blatniky/">blatníky</a>, <a href="/cyklo-tasky-a-nosice/">nosiče a brašny</a>, <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zamky/">zámek</a>, zvonek a stojánek. Mnoho modelů má závity na nosič a blatníky, což ověříte v popisu. Pro sport doplňte <a href="/cyklo-computery/">cyklocomputer</a>, <a href="/cyklo-lahve-a-drzaky/">láhev a držák</a> a <a href="/cyklisticke-helmy/">helmu</a>, případně <a href="/cyklisticka-obuv/">cyklistickou obuv</a> a <a href="/cyklo-pedaly/">pedály</a>.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Kolo jezdící denně potřebuje pravidelnou péči. Mazejte řetěz po dešti a každých několik set kilometrů, kontrolujte brzdové destičky a tlak v pláštích a utahujte šrouby. Po zimě zkontrolujte lanka a pláště. Základní sada nářadí a pumpa patří do brašny, viz <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> a <a href="/cyklo-udrzba/">údržba</a>. Opotřebovaný řetěz poškozuje kazetu, proto ho měňte včas.</p>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li><strong>Špatná velikost rámu.</strong> Výška postavy a délka nohou jsou důležitější než vzhled.</li>'
          '<li><strong>Odpružení za každou cenu.</strong> Na asfaltu je zbytečné a přidává váhu.</li>'
          '<li><strong>Zbytečně mnoho rychlostí.</strong> Počet nic neříká o kvalitě komponent.</li>'
          '<li><strong>Ignorování brzd.</strong> Při dojíždění v dešti jsou kotoučové brzdy znatelně jistější.</li>'
          '<li><strong>Nákup bez doplňků.</strong> Světla, zámek a helma patří do rozpočtu hned.</li></ul>'
          '<h2>Pro koho je kolo ideální</h2>'
          '<p>Pro lidi, kteří chtějí jedno kolo na všechno zpevněné. Dojíždění, víkendové okruhy, rekreační sport. Pokud preferujete delší cestování s bagáží, vyberte spíš <a href="/trekingova-kola/">trekingové kolo</a>. Pro silniční závodění se hodí <a href="/silnicni-kola/">silnička</a>, na terén <a href="/horska-kola/">horské kolo</a>. Kdo hledá pomoc do kopců, najde ji v <a href="/elektrokola/">elektrokolech</a> a <a href="/trekingova-elektrokola/">trekingových elektrokolech</a>.</p>',
    faq=[('Čím se liší krosové kolo od trekingového?', 'Krosové je lehčí a svižnější a obvykle má menší výbavu. Trekingové mívá nosič, blatníky a světla od výrobce a je určeno na delší výlety s bagáží.'),
         ('Hodí se krosové kolo do terénu?', 'Na zpevněné cesty, šotolinu a lehký terén ano. Na kořeny, kameny a prudké sjezdy je lepší horské kolo.'),
         ('Jaké pláště jsou na krosovém kole?', 'Obvykle 32 až 45 mm široké na 28" kolech. Užší jsou rychlejší na asfaltu, širší pohodlnější a lépe drží na šotolině.'),
         ('Jak vybrat velikost rámu?', 'Podle výšky postavy a délky nohou. Výrobci uvádějí rozmezí výšek pro každou velikost. Při stání nad horní trubkou má zbýt několik centimetrů odstupu.'),
         ('Co je cyklokrosové kolo a proč je v této kategorii?', 'Je to kolo s beranem, širšími plášti s hrubým vzorkem a prostorným rámem pro blátivou trať. Používá se na závody i jako všestranný stroj na šotolinu a řadí se sem pro podobné využití.'),
         ('Jsou lepší kotoučové, nebo ráfkové brzdy?', 'Kotoučové brzdí stejně v suchu i v mokru a vyžadují menší sílu stisku. Ráfkové jsou lehčí a levnější, ale v dešti slabší.'),
         ('Kolik rychlostí potřebuji?', 'Na rovinu stačí méně převodů, do kopců se hodí širší rozsah kazety. Důležitější než počet je snadné a spolehlivé řazení.'),
         ('Mohu na krosové kolo namontovat nosič a blatníky?', 'Většina modelů má závity pro nosič a blatníky. Ověřte to v popisu konkrétního modelu, u sportovních verzí někdy chybějí.'),
         ('Je dámské krosové kolo jiné než pánské?', 'Má nižší horní trubku nebo otevřený rám, což usnadňuje nasedání, a bývá vybaveno jiným sedlem. Technické vlastnosti jsou jinak podobné.'),
         ('Jak se starat o krosové kolo při každodenním používání?', 'Pravidelně mazat řetěz, kontrolovat tlak v pláštích a brzdové destičky a po dešti kolo otřít. Před sezónou zkontrolujte lanka a pláště.'),
         ('Kdy zvolit elektrokolo místo krosového?', 'Když jezdíte do kopců nebo delší vzdálenosti a nechcete se zpotit. Elektrokolo je těžší a dražší na údržbu, ale podpora motoru ulehčí výjezdy.')],
)

# ------------------------------------------------------------------ nahradni-zorniky
NEW['nahradni-zorniky'] = dict(long=True,
    title='Náhradní zorníky a čočky do lyžařských brýlí, výběr',
    desc='Náhradní zorníky, čočky a pouzdra k lyžařským brýlím. Jak zvolit zorník ke svému modelu, kategorii podle počasí a porovnat nabídky českých obchodů.',
    intro='<p>Zorník je nejzranitelnější část lyžařských brýlí. Poškrábe se o řemínek, přilbu nebo při pádu a zhorší výhled právě tam, kde potřebujete jasný kontrast. Náhradní zorník vyřeší tento problém bez nákupu celých brýlí a umožní vám přizpůsobit brýle počasí: pro mlhu jiný, pro ostré slunce jiný. Sporteka porovnává nabídky českých obchodů u náhradních čoček a zorníků, pouzder i několika kompletních brýlí, které se v kategorii objevují s příslušenstvím.</p>'
          '<p>V nabídce jsou značky ' + B(('r2', 'R2'), ('relax', 'Relax'), ('rossignol', 'Rossignol'), ('worker', 'Worker'), ('helios', 'Helios'), ('smith', 'Smith')) +
          '. Brýle samotné najdete v kategorii <a href="/lyzarske-bryle/">lyžařské brýle</a>, ochranu hlavy v <a href="/lyzarske-helmy/">lyžařských helmách</a> a ostatní výbavu v <a href="/lyzarske-doplnky/">lyžařských doplňcích</a>.</p>',
    guide='<h2>Proč měnit zorník</h2>'
          '<p>Poškrábaný, zamlžený nebo odřený zorník způsobuje nepříjemné odlesky a zhoršuje vnímání terénu. Při rychlé jízdě a nerovném sněhu je dobrý kontrast základ bezpečnosti. Zorník také slouží jako ochrana očí před UV zářením, větrem a sněhovým prachem. Druhý důvod pro koupi je počasí: světlejší zorník se hodí do mlhy a šera, tmavší na ostré slunce. Mnoho lyžařů proto nosí v batohu dva zorníky a mění je podle podmínek.</p>'
          '<h2>Jak zorník najít pro své brýle</h2>'
          '<p>Nejdůležitější pravidlo zní: zorník musí být určen přesně pro váš model brýlí. Brýle různých řad se liší tvarem rámu, způsobem uchycení a zakřivením čočky. I v rámci jedné značky může mít model z jiného roku jiný zorník. Hledejte proto podle názvu modelu a označení řady, například v nabídce jsou čočky pro modely Contest, Stream, Cross, X-Fighter, Flow, Dragonfly, Hornet, Nordic nebo Cro. Výrobci značí kódy zorníků (například řady HTGL u značky Relax nebo ATG u R2), které přesně odpovídají modelu. Podívejte se na štítek uvnitř rámu nebo do návodu k brýlím a porovnejte kód.</p>'
          + T(['Údaj', 'Kde ho najdete', 'Proč je důležitý'], [
              ['Značka a model brýlí', 'štítek uvnitř rámu nebo návod', 'zorník je pro každý model jiný'],
              ['Kód zorníku', 'popis produktu, často na okraji čočky', 'rozlišuje barvy a verze'],
              ['Způsob uchycení', 'popis brýlí a zorníku', 'magnet, patenty, drážka v rámu'],
              ['Velikost', 'štítek nebo popis', 'junior a dospělé rámy se liší']]) +
          '<h2>Kategorie zorníků podle světla</h2>'
          '<p>Lyžařské zorníky se dělí do kategorií podle propustnosti světla, označených S0 až S4. Čím vyšší číslo, tím tmavší zorník.</p>'
          + T(['Kategorie', 'Propustnost', 'Typické podmínky'], [
              ['S0', 'velmi světlý, skoro čirý', 'noční lyžování, silná mlha'],
              ['S1', 'světlý', 'zataženo, sněžení, šero'],
              ['S2', 'středně tmavý', 'proměnlivé počasí, polojasno'],
              ['S3', 'tmavý', 'slunečný den, odražené světlo od sněhu'],
              ['S4', 'velmi tmavý', 'ledovec a vysoká hora, silné záření']]) +
          '<p>Pro běžné lyžování v Česku a v Alpách vystačíte se zorníkem S2 nebo S3 a světlejším do mlhy. S4 se na sjezdovkách většinou nepoužívá a není vhodný pro jízdu v lese nebo za šera. Kategorie je uvedena na čočce nebo v popisu, ale nemusí být u každé nabídky.</p>'
          '<h2>Typy zorníků a povrchových úprav</h2>'
          '<ul><li><strong>Barevné čiré:</strong> základní zorník v různých odstínech, od oranžové po hnědou a šedou. Oranžové a růžové zesilují kontrast v šeru, šedé nezkreslují barvy.</li>'
          '<li><strong>Zrcadlové:</strong> mají odrazivou vrstvu, která snižuje množství světla v oku. Dobře fungují na ostrém slunci a v obecném světle vypadají atraktivně. Zrcadlová vrstva je citlivější na škrábance.</li>'
          '<li><strong>Zrcadlově kouřové:</strong> kombinace tmavého základu a zrcadla, určená pro svitě slunce.</li>'
          '<li><strong>Dvouvrstvé (dvojité) zorníky:</strong> mezi dvěma vrstvami je vzduchová mezera, která omezuje zamlžování.</li>'
          '<li><strong>Polarizační a fotochromatické:</strong> polarizace tlumí odlesky z vodní hladiny a ledu. Fotochromatický zorník mění propustnost podle intenzity světla. Nemusí se nabízet pro každý model.</li></ul>'
          '<h2>Způsob uchycení a výměna</h2>'
          '<p>Brýle mají několik systémů. Magnetické zorníky se přichytí k rámu magnety a stahují se jediným tahem. Patentové zorníky mají výstupky, které zapadají do otvorů v rámu. Zorníky vsazované do drážky se zasunou po ohnutí rámu. Při každé výměně pracujte v suchu, s čistýma rukama a nedotýkejte se vnitřní strany čočky, kde je protimlžící vrstva. Netlačte na střed, ale držte zorník za okraje. Pokud nejde vyjmout bez tlaku, zkontrolujte, zda jste uvolnili všechny zámky.</p>'
          '<h2>Protimlžící vrstva a péče</h2>'
          '<p>Vnitřní strana zorníku má ochrannou vrstvu proti zamlžení. Utírání hrubou látkou, rukavicí nebo ubrouskem ji poškodí. Po jízdě zorník nechte vyschnout na vzduchu bez otírání, zvlášť vnitřní stranu s protimlžící vrstvou. Vnější stranu lze jemně utřít měkkým mikrovláknem. Čistěte jen vodou nebo přípravkem určeným pro brýle. Zorník skladujte v pouzdru, ideálně tvrdém nebo s měkkou výstelkou, aby se neodíral o jiné věci v batohu. V nabídce jsou i samostatná pouzdra na náhradní zorník, často tvarovaná pro konkrétní model. Brýle se vyplatí skladovat mimo dosah tepla a přímého slunce.</p>'
          '<h2>Zorníky pro děti a juniory</h2>'
          '<p>Dětské a juniorské brýle mají menší rám a výrobci pro ně vyrábějí vlastní zorníky. Pro děti zvolte zorník s kategorií S2 až S3 a dobrou odolností proti poškrábání. Dítě málokdy brýle ošetřuje a rozbije je rychleji než dospělý, takže se vyplatí mít náhradní zorník doma. Dětská výbava souvisí s kategoriemi <a href="/detske-lyze/">dětské lyže</a> a <a href="/lyzarske-helmy/">lyžařské helmy</a>.</p>'
          '<h2>Zorník nebo nové brýle</h2>'
          '<p>Pokud je poškozen jen zorník a rám je v pořádku, vyplatí se koupit náhradní zorník. Když je zdeformovaný rám, praskl pěnový okraj nebo povolil řemínek, ztrácí oprava smysl a je rozumnější vybrat nové <a href="/lyzarske-bryle/">lyžařské brýle</a>. Starší modely se někdy přestanou vyrábět a zorníky pro ně se hledají obtížně, proto zvažte i tuto možnost. Pokud brýle používáte i na jiné sporty, zajímají vás <a href="/sportovni-bryle/">sportovní brýle</a>, ale lyžařské zorníky nejsou zaměnitelné.</p>'
          '<h2>Kde se zorníky hodí kromě sjezdovky</h2>'
          '<p>Zorníky řeší stejný problém u snowboardistů, běžkařů i skialpinistů, ale každý model brýlí má vlastní zorník, takže vždy vybírejte podle modelu svých brýlí. Pro dlouhé výstupy se hodí světlejší zorník, který nezatemní výhled při chůzi, a pro sjezd v otevřené krajině naopak tmavší. Viz také <a href="/snowboarding/">snowboarding</a> a <a href="/skialpinismus/">skialpinismus</a>. Proti zamlžení pomáhá větrání brýlí a to, že je nenosíte na čele, kde se zahřívají a vlhnou.</p>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li><strong>Zorník od jiného modelu.</strong> Tvar a uchycení se často liší, i když jde o stejnou značku.</li>'
          '<li><strong>Špatná kategorie.</strong> Tmavý zorník do mlhy je nebezpečný, světlý na ledovci neochrání oči dostatečně.</li>'
          '<li><strong>Čištění nevhodnou látkou.</strong> Ruší protimlžící vrstvu a škrábe povrch.</li>'
          '<li><strong>Skladování bez pouzdra.</strong> Zorník v batohu se poškrábe rychleji než při jízdě.</li>'
          '<li><strong>Dotyk na vnitřní stranu.</strong> Otisky prstů rozmazávají obraz a odírají vrstvu.</li></ul>',
    faq=[('Jak poznám správný náhradní zorník?', 'Podle modelu brýlí a kódu zorníku, který výrobce uvádí. Zorníky různých řad se obvykle nedají zaměnit, protože se liší tvarem a uchycením.'),
         ('Jaká kategorie zorníku je vhodná do mlhy?', 'Světlejší, tedy S0 nebo S1. Zvyšují kontrast ve slabém světle a umožňují lépe vnímat terén.'),
         ('Jaký zorník na slunečný den?', 'Kategorie S3, případně zrcadlový zorník. Tmavší S4 se hodí spíš na ledovec a do vysokých hor.'),
         ('Jak vyměnit zorník?', 'Záleží na systému brýlí. U magnetických jej stačí odtáhnout, u ostatních uvolnit patenty nebo zasunout do drážky. Vždy se dotýkejte jen okraje.'),
         ('Jak čistit zorník?', 'Nechte ho po jízdě vyschnout na vzduchu, vnitřní stranu neotírejte. Vnější stranu lze jemně utřít měkkým mikrovláknem. Nepoužívejte rukavice, ubrousky ani agresivní čističe, které poškodí protimlžící vrstvu.'),
         ('Hodí se zorníky i na snowboardové brýle?', 'Ano, zorníky se vyrábějí pro lyžařské i snowboardové brýle stejným způsobem. Ať jezdíte na čemkoli, zorník vždy vybírejte podle konkrétního modelu brýlí.'),
         ('Co znamená zrcadlový zorník?', 'Má odrazivou vrstvu, která snižuje množství světla vstupujícího do oka. Hodí se na ostré slunce, ale vrstva je citlivější na škrábance.'),
         ('Kdy koupit nový zorník a kdy nové brýle?', 'Když je poškozen jen zorník, vyplatí se zorník. Při prasklém rámu, nefunkčním uchycení nebo starém modelu bez zorníků zvažte nové brýle.'),
         ('Jak chránit náhradní zorník v batohu?', 'Ukládejte ho do pouzdra, které chrání před otěrem, tlakem a vlhkostí. V nabídce jsou i pouzdra přímo na zorníky.'),
         ('Existují zorníky pro děti?', 'Ano, juniorské brýle mají menší rám a vlastní zorníky. Hodí se S2 až S3 s dobrou odolností proti poškrábání.'),
         ('Zabrání zorník s protimlžící vrstvou úplně zamlžení?', 'Ne úplně. Vrstva omezuje zamlžování, ale pomáhá i větrání brýlí, nošení mimo čelo a nechávání brýlí vyschnout. Hrubé čištění vrstvu poškodí.')],
)


# ------------------------------------------------------------------ extra sections (appended to the guides)
NEW['detska-kola-24-palcu']['guide'] += (
    '<h2>Nákup krok za krokem</h2>'
    '<p>Nejdřív změřte dítě: výšku postavy a vnitřní délku nohy od rozkroku k zemi, pokud možno bez bot. Tuto druhou míru výrobci často používají při doporučení výšky rámu a pomůže vám zvolit mezi dvěma blízkými velikostmi. Potom si ujasněte, kde bude dítě jezdit nejčastěji. Pro cestu do školy po městě je užitečnější blatník, zvonek a odolné pláště, pro prázdniny na šotolině spíš lehký rám a rozumné převody. Na Sportece pak přepněte řazení podle toho, co hledáte, a v nabídkách porovnejte hmotnost, velikost rámu, typ brzd a to, zda je v ceně výbava.</p>'
    '<p>Dalším krokem je obchod: u kola z internetu zkontrolujte, v jakém stavu se kolo dodává. Často přichází částečně smontované, s nenastavenými brzdami a s volnými pedály. Pokud si nejste jistí, nechte kolo před první jízdou zkontrolovat v servisu. Správně utažený představec, upnuté sedlo, funkční brzdy a vyfouknuté, ale pevné pláště jsou důležitější než další značka na rámu.</p>'
    '<h2>Rám pro dívky a pro chlapce</h2>'
    '<p>Rámy s nízkým nástupem se vyrábí hlavně jako dívčí. Pomáhají menším dětem při nasedání a hodí se i pro kluky, kteří jsou na rám nízcí. Chlapecké rámy mají rovnou horní trubku a vyšší stand-over, tedy menší prostor mezi dítětem a trubkou při stání. Je dobré to zkontrolovat, protože při nešťastném sesednutí hrozí úder o trubku.</p>'
    '<h2>Kdy kolo vyměnit za větší</h2>'
    '<p>Signálem je sedlo vysunuté k maximální značce, kolena narážející do řídítek nebo dítě, které sedí příliš sevřeně. Obvykle dítě přeroste 24 palců po několika sezónách. Kolo, které se přestalo hodit, nemusí skončit v garáži: dá se prodat nebo předat mladšímu sourozenci. Pokud bylo správně udržováno, vymění se pouze pláště, řetěz a destičky a poslouží dál.</p>')

NEW['pozemni-hokej']['guide'] += (
    '<h2>Jak začít s pozemním hokejem</h2>'
    '<p>Začátečník nemusí kupovat vše najednou. V klubech i školních kroužcích bývají k zapůjčení hole, míčky a ochranné pomůcky, a proto se vyplatí nejdřív vyzkoušet hru a koupit si základ. Z vlastní výbavy přednostně pořiďte obuv, která sedí, zubní chránič a rukavici. Hůl vyberte až poté, co zjistíte, jakou délku a křivku vám trenér doporučí. Dětem se hodí lehká dřevěná nebo skelná hůl, protože ji unesou a snadněji s ní ovládají míček. Dospělí hráči postupně přecházejí na kompozitní modely s větším podílem uhlíku.</p>'
    '<h2>Role na hřišti a výbava</h2>'
    '<p>Útočníci a záložníci potřebují hlavně lehkou hůl a rychlou obuv. Obránci častěji stojí v pozici, kde hrozí zásah míčkem, a proto volí větší ochranu rukou a holení. Při obraně krátkého rohu se přidává maska a někdy i chránič hrudníku a hrdla. Brankář je odlišný: má vlastní přilbu, chrániče nohou, kopačky a rukavice, které se prodávají samostatně a nejsou součástí této nabídky.</p>'
    '<h2>Tréninkové pomůcky</h2>'
    '<p>Pro domácí trénink se hodí hladké míčky, mety a branky, viz <a href="/hokejove-puky-a-branky/">hokejové puky a branky</a>. Kdo trénuje i v zimě, může využít sálu a míček určený pro halu. Rozcvičku a kondici doplňují <a href="/funkcni-trenink/">funkční trénink</a> a <a href="/fitness-pomucky/">fitness pomůcky</a>. Trenérská tabule pomáhá vysvětlit nácvik standardních situací, jako jsou rohy, penalty a volné údery, a děti ji berou jako hru.</p>'
    '<h2>Značky a jejich zaměření</h2>'
    '<p>Výrobci v této oblasti se profilují různě. Některé nabízejí širokou řadu holí, další jsou silné v obuvi a rukavicích, další v klubovém oblečení a taškách. Při srovnání proto porovnávejte konkrétní parametry, nikoli jen jméno výrobce: materiál hole, typ podrážky, rozměr rukavice a pod. Výběr se zjednoduší, když víte, na jakém povrchu a v jaké soutěži budete hrát.</p>')

NEW['krosova-kola']['guide'] += (
    '<h2>Dámské a pánské modely</h2>'
    '<p>Dámské krosové kolo má obvykle nižší horní trubku, lehčí nástup a sedlo, které odpovídá širší pánevní kosti. Nejde jen o design, ale i o to, že u menších rámů je geometrie upravena tak, aby se jezdkyně nemusela příliš natahovat. Pánský rám má vyšší horní trubku a bývá tužší. Rozdíl je menší než kdysi, a proto vyberte spíš podle pohodlí a velikosti než podle označení. Mnoho žen zvolí pánský nebo unisex rám, pokud jim sedí.</p>'
    '<h2>Hmotnost a materiál</h2>'
    '<p>Rámy z hliníku převažují, protože jsou lehké, odolné proti korozi a cenově dostupné. Karbonové rámy jsou lehčí a tlumí vibrace, ale jsou citlivější na nárazy. Ocel je odolná a pohodlná, ale těžší. Hmotnost celého kola se mění s výbavou: blatníky, nosič a odpružená vidlice přidávají, kotoučové brzdy mírně také. Pokud často nosíte kolo po schodech, vyplatí se hmotnost sledovat.</p>'
    '<h2>Zimní a celoroční používání</h2>'
    '<p>Krosové kolo je vhodné i do chladnějších měsíců, pokud má dobré brzdy, blatníky a světla. Pro zimu se hodí <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>, <a href="/cyklisticke-navleky/">návleky</a> a rukavice. Pneumatiky s vloženou ochranou proti defektu a šířkou nad čtyřicet milimetrů ocení každý, kdo jezdí po rozbitém městském povrchu. Sůl na silnicích napadá řetěz a komponenty, a proto po zimě kolo umyjte a promažte.</p>'
    '<h2>Kolo na sport a trénink</h2>'
    '<p>Pro sportovní jízdu dává smysl lehčí rám, pevná vidlice a užší pláště. Doplňte <a href="/cyklisticke-dresy/">cyklistické dresy</a>, <a href="/cyklisticke-kratasy-a-kalhoty/">kraťasy</a> a <a href="/cyklisticke-bryle/">brýle</a>. Kdo plánuje delší vyjížďky, ocení sedlo vhodné pro dlouhé sezení a ergonomické rukojeti, které snižují tlak na dlaně.</p>')

NEW['nahradni-zorniky']['guide'] += (
    '<h2>Zorník pro různé terény a denní doby</h2>'
    '<p>Podmínky na svahu se mění víc, než se zdá. Ráno ve stínu, po poledni na slunci a odpoledne v oblacích potřebujete jiné světlo. Zorník oranžové a žluté barvy zvyšuje kontrast při slabém osvětlení a hodí se na sněžení a večer. Hnědé a měděné odstíny jsou pro slunečné počasí, protože dobře vnímají strukturu sněhu. Šedé zorníky věrně předávají barvy a hodí se pro dlouhé jízdy za silného slunce. V bílé krajině při plochém světle se ztrácejí stíny a hrboly není vidět, proto pomáhá zorník s růžovým či oranžovým nádechem, který strukturu povrchu zvýrazní. Pokud nechcete měnit zorníky, vyberte kompromis kategorie S2.</p>'
    '<h2>Kompatibilita s helmou a ventilace</h2>'
    '<p>Zorník nepracuje sám. Brýle musí dobře sedět na obličeji a s <a href="/lyzarske-helmy/">lyžařskou helmou</a>, jinak vznikají mezery, kudy proudí vzduch, nebo se brýle odtlačí a zorník se zamlžuje. Zorníky s větracími otvory a pěnovým těsněním snižují zamlžení. Nový zorník vložený do starého rámu nevyřeší špatné těsnění ani opotřebovaný pěnový lem, proto před výměnou rám prohlédněte.</p>'
    '<h2>Kdy zorník vyměnit</h2>'
    '<ul><li><strong>Hluboké škrábance</strong> v zorném poli, které se při jízdě proti slunci rozsvěcují.</li>'
    '<li><strong>Odlupující se vrstva</strong> zrcadlová nebo protimlžící, kterou už nelze obnovit.</li>'
    '<li><strong>Prasklina</strong> kolem upevňovacích otvorů, která se při pádu může rozšířit.</li>'
    '<li><strong>Změna podmínek:</strong> chcete-li lyžovat v mlze nebo večer, potřebujete světlejší zorník, než jaký máte.</li></ul>'
    '<h2>Doplňky k brýlím</h2>'
    '<p>K zorníkům patří řemínek, pěnové těsnění a čisticí látka z mikrovlákna. K lyžování se hodí také <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a> a <a href="/lyzarske-rukavice/">rukavice</a>, které chrání před chladem a vlhkem. Správně nastavená výbava pomáhá i zorníku, protože se brýle méně zamlžují při dobré ventilaci a méně namáhají při pádu.</p>')

NEW['pozemni-hokej']['guide'] += (
    '<h2>Hra v hale a na venkovním hřišti</h2>'
    '<p>Halová verze se hraje na menším hřišti s nižšími mantinely nebo lavičkami a míček se nezvedá tak často. Tým je menší a hra rychlejší, proto vzniká víc kontaktu s míčkem než na velkém trávníku. Hráči si většinou berou tenčí rukavici a kratší hůl, aby se snáz manipulovalo s míčkem na místě. Naopak ve venkovní hře se uplatní delší záběr a silnější úder. Pokud hrajete obojí, počítejte se dvěma páry obuvi.</p>'
    '<h2>Doprava a uložení výbavy</h2>'
    '<p>Hole jsou dlouhé a při cestě městskou dopravou překážejí, takže praktický je obal s popruhem přes rameno. Boty se nosí zvlášť, aby nezašpinily ostatní věci, a vlhké oblečení patří do větratelné kapsy. Dětský batoh s oddělením na boty a lahev na pití vydrží celé sezóny, pokud ho po tréninku vyvětráte.</p>')

NEW['krosova-kola']['guide'] += (
    '<h2>Jak zkoušet kolo při nákupu</h2>'
    '<p>Pokud máte možnost kolo vyzkoušet, projeďte si krátký úsek a všímejte si tří věcí: jak sedíte, zda se vám pohodlně dosahuje na brzdové páky a zda řazení pracuje plynule. Zkuste i prudké brzdění a zatáčení. U kola z e-shopu zkontrolujte po rozbalení, zda jsou kola vystředěná, šrouby utažené a pláště správně nahuštěné, případně nechte kolo seřídit v servisu. Pamatujte, že dobře seřízené levnější kolo jede lépe než špatně seřízené drahé.</p>'
    '<h2>Dojíždění do práce</h2>'
    '<p>Pro každodenní cestu do práce počítejte s kolem, které nevadí venku zamknout, a se zámkem, který se nedá snadno přeřezat. Brašna místo batohu zabrání propocenému zádům a světla s dobíjením z USB se snadno doplňují. Na parkování se hodí kolo, které nevypadá příliš lákavě pro zloděje, a odnímatelné příslušenství jako světla a computer vždy berte s sebou.</p>')

NEW['nahradni-zorniky']['guide'] += (
    '<h2>Jak číst označení zorníku v nabídce</h2>'
    '<p>Názvy v obchodech bývají zkrácené a plné kódů. Za označením řady a modelu najdete obvykle písmenné a číselné kódy, které popisují barvu čočky a povrch. Rozlišujte, zda jde o samotný zorník, o kompletní brýle s přibaleným pouzdrem, nebo o pouzdro samotné. Některé nabídky v kategorii mají v názvu právě komplet brýlí s příslušenstvím, a proto vždy zkontrolujte, co přesně kupujete. Pokud název neobsahuje model brýlí, nechte výběr na doplňujících informacích v popisu, případně porovnejte fotografii s tvarem svých brýlí.</p>'
    '<h2>Zorník, UV ochrana a oslnění</h2>'
    '<p>Kvalitní lyžařský zorník filtruje ultrafialové záření bez ohledu na barvu. Na horách je záření silnější než v údolí a sníh ho dál odráží, takže chránit oči je nutné i za oblačného počasí. Tmavost čočky s UV filtrem nesouvisí, takže světlý zorník s UV filtrem chrání před ultrafialovým zářením stejně jako tmavý. Liší se ale ochranou před oslněním: světlý zorník na ostrém slunci nebo na ledovci oči zbytečně namáhá, proto se tam volí tmavší kategorie. Naopak v šeru a mlze tmavý zorník zhorší viditelnost nerovností. Poškrábaný zorník nicméně rozptyluje světlo, a pokud se zhoršuje vidění, vyměňte jej.</p>'
    '<h2>Servis a odborná rada</h2>'
    '<p>Při pochybnostech o kompatibilitě se obraťte na prodejce nebo značku s modelem a ročníkem brýlí. Odpověď je často v návodu a u zorníku s kódem se dá shodnost rychle ověřit.</p>')
