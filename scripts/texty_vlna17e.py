"""sporteka.cz — wave 17e (4. 11. 2026): long texts (>= 1650 words) for jezdectvi, detska-kola, golf, funkcni-mikiny.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ jezdectvi
NEW['jezdectvi'] = dict(long=True,
    title='Jezdectví: výbava pro jezdce a koně | Sporteka',
    desc='Jezdecká výbava: helmy, rajtky, boty, oblečení i potřeby pro koně. Průvodce výběrem a srovnání nabídek českých obchodů na jednom místě.',
    intro='<p>Jezdectví je sport, v němž se výbava dělí na dvě půlky: tu, kterou nosí člověk, a tu, kterou nese kůň. Obě musí sedět, protože špatně padnoucí třmen, uzdečka nebo rajtky '
          'dokážou zkazit hodinu v sedle stejně spolehlivě jako špatně naladěný kůň. V kategorii <strong>jezdectví</strong> najdete bezpečnostní helmy, kalhoty s výztuhou, boty, '
          'rukavice, bundy i veškeré vybavení pro péči o koně, od ohlávek po kartáče.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného zboží, takže uvidíte, kde je vaše velikost nebo barva skladem. Na rozcestí vedou podkategorie '
          '<a href="/jezdecke-helmy/">jezdecké helmy</a>, <a href="/jezdecke-kalhoty/">jezdecké kalhoty a rajtky</a>, <a href="/jezdecka-obuv/">jezdecká obuv a chapsy</a>, '
          '<a href="/jezdecke-obleceni/">jezdecké oblečení</a>, <a href="/vybaveni-pro-kone/">vybavení pro koně</a> a <a href="/jezdecke-doplnky/">jezdecké doplňky</a>. '
          'Níže najdete, na co se při nákupu soustředit a čemu se vyhnout.</p>',
    guide='<h2>Z čeho se jezdecká výbava skládá</h2>'
          '<p>Nováček si obvykle myslí, že stačí helma a kalhoty. Praxe ukáže, že výbava se vrství podle toho, jak často jezdíte, jestli máte vlastního koně a jak se u vás střídá počasí. '
          'Následující přehled pomůže určit pořadí nákupů.</p>'
          + T(['Část výbavy', 'K čemu slouží', 'Kdy ji řešit'], [
              ['Jezdecká helma', 'chrání hlavu při pádu', 'před první hodinou, patří k povinné výbavě'],
              ['Rajtky nebo jezdecké kalhoty', 'drží se v sedle, nechají se bez odření nosit celý den', 'po prvních několika lekcích'],
              ['Jezdecká obuv', 'hladká podešev s patou, aby noha nepropadla třmenem', 'hned na začátku, tenisky se nehodí'],
              ['Rukavice', 'jistý úchop otěží a ochrana dlaní', 'jakmile jezdíte pravidelně'],
              ['Bunda a spodní vrstvy', 'pohodlí v chladném počasí a v dešti', 'před zimní sezónou'],
              ['Sedlo, uzdečka, podsedlová dečka', 'ovládání koně a rozložení tlaku na hřbet', 'když přebíráte vlastního koně'],
              ['Péče a stáj', 'kartáče, hřebla, ohlávky, vodítka', 'hned s příchodem koně do stáje']]) +
          '<p>Rozhodněte se nejdřív, zda jezdíte rekreačně, v jezdeckém klubu, nebo závodně. Kdo si pronajímá koně v jízdárně, vystačí s osobní výbavou. Kdo má vlastního, musí počítat s nákupem sedla, popruhů, dek a krmiva.</p>'
          '<h2>Helma: bezpečnost na prvním místě</h2>'
          '<p>Jezdecká helma má pevnou skořepinu, tlumicí vložku a nastavitelný pásek pod bradou. Na rozdíl od cyklistické helmy bývá delší vzadu, aby chránila týl při pádu z výšky sedla. '
          'Správně padnoucí helma sedí rovně, nesmí se při kývnutí hlavou posunout a čelo nechává odkryté jen do šířky dvou prstů nad obočím. Pásek pod bradou má držet, ale nesmí škrtit.</p>'
          '<p>Po pádu na hlavu se helma vyměňuje, i když na ní není nic vidět, protože vložka mohla ztratit schopnost tlumit. Totéž platí pro helmy, které leží dlouho na slunci v autě nebo které jste upustili na tvrdou zem. '
          'Podrobnosti a velikosti najdete v kategorii <a href="/jezdecke-helmy/">jezdecké helmy</a>.</p>'
          '<h2>Rajtky, jezdecké kalhoty a legíny</h2>'
          '<p>Jezdecké kalhoty mají švy vedené tak, aby se nedřely o vnitřní stranu stehna a lýtka. Dělí se podle výztuhy, kterou má kalhota na sedací ploše a po vnitřní straně nohy.</p>'
          '<ul><li><strong>Plná výztuha</strong> pokrývá sedací část a vnitřní stranu nohou až ke kolenům a hodí se do závodu a pro dlouhé hodiny v sedle.</li>'
          '<li><strong>Kolenní výztuha</strong> zesiluje jen vnitřek kolen a hodí se na výcvik i rekreační vyjížďky.</li>'
          '<li><strong>Silikonové potisky</strong> zlepšují přilnavost a nahrazují kůži, nemají tak vysokou životnost, ale drží dobře i na hladkém sedle.</li>'
          '<li><strong>Legíny a teplé kalhoty</strong> na zimu dávají přednost pružnosti a tepelné izolaci.</li></ul>'
          '<p>Pro volbu velikosti se měří obvod pasu, boků a délka nohy. Rajtky mají být těsnější než běžné kalhoty a v kolenou se nesmí tvořit záhyby. '
          'Širší nabídku, od klasických rajtek po strečové kalhoty, mapuje kategorie <a href="/jezdecke-kalhoty/">jezdecké kalhoty a rajtky</a>. Pod ně se hodí <a href="/leginy/">legíny</a> nebo <a href="/termopradlo/">funkční termo prádlo</a>.</p>'
          '<h2>Jezdecká obuv a chapsy</h2>'
          '<p>Základem je bota s hladkou podešvou a výraznou patou. Pata zabraňuje tomu, aby noha prokluzovala dopředu třmenem, což je jedna z nejnebezpečnějších situací při pádu. '
          'Na výběr jsou vysoké jezdecké boty a krátké kotníkové boty doplněné chapsy, tedy lýtkovými návleky. Kotníkové varianty se lépe obouvají, snesou víc ve stáji a bývají praktičtější pro rekreační jezdce. '
          'Vysoké boty drží tvar a jsou typické pro soutěže.</p>'
          '<p>Při zkoušení boty si oblékněte jezdecké ponožky nebo takové, které budete nosit v sedle. Lýtko by mělo sedět těsně, ale nesmí tlačit do lýtkových svalů, a špička má být přiměřeně prostorná. '
          'Kůže potřebuje impregnaci a občasné promazání, syntetické materiály se pouze otírají vlhkým hadříkem. V kategorii <a href="/jezdecka-obuv/">jezdecká obuv a chapsy</a> najdete obojí a při chladnějším počasí se vyplatí zaměřit se i na <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>'
          '<h2>Oblečení podle ročního období</h2>'
          '<p>Jezdec sedí relativně nehybně a rychle vychladne, přitom při práci v maštali se zahřeje. Proto funguje vrstvení, které zvládne obě situace.</p>'
          '<h3>Léto</h3>'
          '<p>Tričko s krátkým rukávem nebo vzdušné funkční triko, tmavé rajtky a světlá helma s větráním. Kdo jezdí na slunci, ocení rukavice s prodyšnými vložkami.</p>'
          '<h3>Jaro a podzim</h3>'
          '<p>Přidejte lehkou softshellovou bundu nebo vestu. Z kategorie <a href="/sportovni-bundy/">sportovní bundy a vesty</a> se hodí střihy s delším zadním dílem, které zakryjí záda i v předklonu. Pod ni stačí <a href="/mikiny/">mikina</a>.</p>'
          '<h3>Zima</h3>'
          '<p>Termální spodní vrstva, teplé rajtky, zateplená bunda a čepice pod helmu. Hlavně se chraňte před studenými prsty, protože s promrzlýma rukama špatně vedete koně. Hodí se silnější <a href="/sportovni-rukavice/">rukavice</a>. Více nabízí kategorie <a href="/jezdecke-obleceni/">jezdecké oblečení</a>.</p>'
          '<h2>Vybavení pro koně</h2>'
          '<p>Část vybavení patří přímo na koně. Má-li být jízda příjemná i pro něj, musí všechno sedět na jeho tělo, ne na ideální průměr.</p>'
          '<ul><li><strong>Ohlávka a vodítko</strong> slouží pro vedení koně ze stáje na pastvu či k čištění. Ohlávka se vybírá podle velikosti hlavy.</li>'
          '<li><strong>Uzdečka s udidlem</strong> se přizpůsobuje tlamě a hlavě, nesmí škrtit ani tlačit na čelisti.</li>'
          '<li><strong>Sedlo</strong> musí odpovídat tvaru kohoutku a délce hřbetu. Špatné sedlo způsobuje tlakové body a nepříjemnosti pro koně i jezdce.</li>'
          '<li><strong>Dečky a podsedlové podložky</strong> rozkládají tlak a vstřebávají pot.</li>'
          '<li><strong>Nánožníky a bandáže</strong> chrání nohy při skocích a práci na kruhu. Zdravotní stav koně vždy konzultujte s veterinářem.</li>'
          '<li><strong>Deky</strong> se vybírají podle účelu: venkovní nepromokavé, stájové prodyšné, odpotní pro koně po zátěži.</li></ul>'
          '<p>Všechno potřebné shrnuje kategorie <a href="/vybaveni-pro-kone/">vybavení pro koně</a>, kde je přes tři sta položek. V rámci drobnějších věcí se hodí podívat do <a href="/jezdecke-doplnky/">jezdeckých doplňků</a>.</p>'
          '<h2>Péče o koně a jeho výstroj</h2>'
          '<p>Základem péče jsou kartáče, hřebla, škrabka na kopyta a houba. Každá pomůcka se používá v určitém pořadí: nejdřív hrubé hřeblo na uvolnění bláta, pak tvrdší kartáč na srst, jemný kartáč na hlavu a nakonec škrabka na kopyta. '
          'Hřebeny a kartáče na hřívu a ocas zabraňují lámání vlasu.</p>'
          '<p>Kožené výrobky, tedy sedla, uzdečky a třmenové řemeny, se po použití otřou vlhkým hadříkem a občas se ošetří mýdlem a výživným tukem. Zanedbaná kůže praská a řemeny mohou v nejhorší chvíli povolit. '
          'Tkané a nylonové popruhy se perou při nízké teplotě. Nikdy je nesušte na radiátoru, vlákna ztrácejí pevnost.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ol><li>Koupit helmu bez zkoušení, jen podle obvodu hlavy. Každá značka má jiný tvar, jednomu seděla kulatější, druhému užší.</li>'
          '<li>Použít tenisky nebo turistické boty s hlubokým vzorkem. Rýhovaná podešev zůstane ve třmenu zaseknutá.</li>'
          '<li>Kupovat sedlo předem, než znáte koně. Sedlo se měří na koni, nikoli podle katalogu.</li>'
          '<li>Podcenit zimní vrstvy a rukavice, takže se jízda stane utrpením.</li>'
          '<li>Kupovat rajtky o velikost větší kvůli pohodlí. Volné kalhoty vytvářejí záhyby, které dřou.</li></ol>'
          '<h2>Značky v nabídce</h2>'
          '<p>V katalogu jsou zastoupené například ' + B(('fouganza','Fouganza'),('galop-wear','Galop Wear'),('waldhausen','Waldhausen'),('horze','Horze'),('kerbl','Kerbl'),('qhp','QHP'),('covalliero','Covalliero'),('start','Start'),('topvet','Topvet')) +
          '. Každá z nich se zaměřuje na jinou část nabídky, jedna klade důraz na oblečení, jiná na stájové vybavení nebo krmné doplňky. Porovnávejte nabídky podle konkrétního produktu, ne podle jména na etiketě.</p>'
          '<h2>Jak vybírat na Sportece</h2>'
          '<p>V jednotlivých kategoriích filtrujte podle velikosti, značky a dostupnosti. U každého produktu vidíte všechny obchody, které jej mají, a můžete se rozhodnout podle doručení nebo možnosti vrácení. '
          'U jezdecké výbavy je vhodné ověřit, zda obchod přijímá výměnu velikostí, protože u bot a rajtek se běžně stává, že první velikost nesedne. Pokud kupujete dětem, počítejte s růstem, ale nikdy nekupujte helmu na vyrůstání.</p>',
    faq=[('Co potřebuje začínající jezdec ke koupi?', 'Pro první lekce stačí jezdecká helma, boty s hladkou podešví a pevnou patou a pohodlné kalhoty bez tlustých vnitřních švů. Rukavice, rajtky a bundu pořídíte, až zjistíte, že vás jezdectví baví. Sedlo a uzdečku neřešte, v jezdeckém klubu je dostanete k pronajatému koni.'),
         ('Jak poznám, že mi jezdecká helma správně sedí?', 'Helma má sedět rovně, těsně kolem celé hlavy a nesmí se při nakloněné hlavě sama posunout. Čelo nechává odkryté zhruba šířku dvou prstů nad obočím a pásek pod bradou drží, aniž by škrtil. Při zkoušce s ní zakývejte a pootočte hlavou, tlak má být rovnoměrný a bez bodů.'),
         ('Kdy je potřeba helmu vyměnit?', 'Po každém pádu na hlavu, i když na ní nejsou vidět škody, protože tlumicí vložka mohla ztratit funkci. Měnit ji je dobré také tehdy, když je viditelně poškozená, deformovaná nebo ji výrobce označuje jako vyřazenou. U dětí ji vyměňte, jakmile přestane padnout.'),
         ('Čím se liší jezdecké kalhoty od rajtek?', 'Rajtky bývají střihem těsné a mají výztuhu ze silikonu nebo kůže na vnitřní straně stehen a kolen. Jezdecké kalhoty je širší pojem a zahrnují i volnější střihy, legíny s výztuhou či kalhoty na zimu. Pro začátek stačí legíny bez tlustých švů, na závody přijdou na řadu plné rajtky.'),
         ('Mohu jezdit v běžných botách?', 'Nedoporučuje se to. Bota musí mít hladkou podešev a výraznou patu, aby noha neprojela třmenem a nezůstala v něm při pádu zaklíněná. Hluboký vzorek turistické boty se může ve třmenu zaseknout. Kotníkové jezdecké boty s chapsy jsou rozumný kompromis pro stáj i sedlo.'),
         ('Jak vybrat velikost uzdečky nebo ohlávky?', 'Měří se obvod nosu a délka od ucha k ústnímu koutku, často se vybírá podle velikostí pony, cob a full. Ohlávka nesmí tlačit na kosti ani škrtit, ale ani viset tak, aby se kůň mohl zachytit nohou. Pro přesnost změřte hlavu koně a porovnejte s tabulkou konkrétního výrobce.'),
         ('Jak se starat o kožené sedlo a uzdečku?', 'Po jízdě otřete pot a špínu vlhkým hadříkem a občas ošetřete kůži mýdlem a výživným přípravkem. Skladujte na suchém místě mimo přímé teplo. Poškozené švy a řemeny nechte opravit u sedláře, nenechávejte je na později, selhání při jízdě je nebezpečné.'),
         ('Jaké oblečení je nejlepší do zimy v sedle?', 'Funguje vrstvení: termální spodní prádlo, teplé jezdecké kalhoty, mikina nebo fleece a větruvzdorná bunda. Pod helmu přidejte tenkou čepici nebo čelenku a pořiďte si zateplené rukavice. Dávejte pozor, abyste nenosili příliš objemné kusy, které brání pohybu.'),
         ('Je nutné kupovat deky pro koně?', 'Ne každý kůň deku potřebuje, závisí na plemeni, srsti, ustájení a počasí. Otužilý kůň na venkovní pastvě se často bez deky obejde, stájová nebo odpotní deka se hodí po práci. Nejlepší je poradit se s veterinářem nebo zkušeným stájníkem a sledovat, zda se kůň netřese.'),
         ('Kde porovnám ceny jezdeckých potřeb?', 'Na Sportece vidíte u stejného produktu nabídky několika českých obchodů vedle sebe, včetně dostupnosti. V jednotlivých kategoriích můžete filtrovat podle značky a velikosti. Před objednávkou si ověřte podmínky vrácení, u bot a kalhot se výměna velikosti hodí.')])

# ------------------------------------------------------------------ detska-kola
NEW['detska-kola'] = dict(long=True,
    title='Dětská kola a odrážedla: výběr podle výšky',
    desc='Dětská kola, odrážedla a tříkolky: jak vybrat velikost podle výšky dítěte, brzdy, váha a bezpečnost. Srovnání nabídek českých obchodů.',
    intro='<p>První kolo dítěte je krok k samostatnosti, a také nákup, který se musí povést na první pokus. Příliš velký bicykl dítě vystraší a odradí, příliš malý ho brzy omrzí. '
          'V kategorii <strong>dětská kola a odrážedla</strong> najdete všechny stupně výbavy od prvního odrážedla přes tříkolky až po dvacetičtyřpalcová kola pro školáky těsně před dospělou velikostí.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného modelu a ukáže, kde je skladem konkrétní velikost kola. Nabídka se dělí na '
          '<a href="/odrazedla/">odrážedla</a>, <a href="/detske-trikolky/">tříkolky</a>, <a href="/detska-kola-12-14-palcu/">kola 12 a 14 palců</a>, <a href="/detska-kola-16-palcu/">16 palců</a>, '
          '<a href="/detska-kola-20-palcu/">20 palců</a> a <a href="/detska-kola-24-palcu/">24 palců</a>. Čtěte dál, jak sladit velikost, váhu, brzdy a bezpečnostní výbavu s věkem dítěte.</p>',
    guide='<h2>Od odrážedla ke kolu s přehazovačkou</h2>'
          '<p>Cesta od prvního kolečkového stroje po samostatnou jízdu na silnici trvá několik let a každá fáze potřebuje jiné vybavení. Následující přehled ukazuje, co kdy dává smysl.</p>'
          + T(['Typ', 'Orientační věk', 'Co dítě učí', 'Na co dát pozor'], [
              ['Odrážedlo', 'od 18 měsíců do čtyř až pěti let', 'rovnováha a řízení bez šlapání', 'výška sedla a váha rámu'],
              ['Tříkolka', 'od jednoho roku do tří let', 'šlapání a základy řízení', 'stabilita a madlo pro rodiče'],
              ['Kolo 12 a 14 palců', 'zhruba tři až pět let', 'šlapání a brzdění', 'pomocná kolečka jen na přechodnou dobu'],
              ['Kolo 16 palců', 'zhruba čtyři až sedm let', 'samostatná jízda a zatáčení', 'brzdy, které dítě zvládne stisknout'],
              ['Kolo 20 palců', 'zhruba šest až deset let', 'delší vyjížďky a první terén', 'váha kola a počet převodů'],
              ['Kolo 24 palců', 'zhruba osm až dvanáct let', 'přechod k dospělému kolu', 'tvar rámu a ergonomie']]) +
          '<p>Věkové údaje jsou jen orientační, protože děti rostou různě rychle. Rozhoduje výška a délka nohou, ne datum narození. Pokud váháte mezi dvěma velikostmi, nechte dítě vyzkoušet menší kolo, než přejdete na větší.</p>'
          '<h2>Odrážedla a tříkolky: první kroky</h2>'
          '<p><strong>Odrážedlo</strong> bývá nejlepší start. Dítě se odráží nohama, učí se držet rovnováhu a když si získá jistotu, přejde na kolo bez nutnosti pomocných kolek. Rám má být lehký, sedlo nastavitelné a nohy se musí dotýkat země celými chodidly. '
          'Pevné pneumatiky bez vzduchu jsou praktické na chodník a nikdy se neprobodnou, nafukovací dávají lepší tlumení v terénu. Kdo hledá model s brzdou, ocení ji u dětí, které si v kopci zvyknou jet rychle. Všechny možnosti nabízí kategorie <a href="/odrazedla/">odrážedla</a>.</p>'
          '<p><strong>Tříkolka</strong> je pro nejmenší pohodlná alternativa. Stabilita je velká, dítě se nemůže převrátit, a pokud má vodicí tyč, rodič řídí, dokud dítě nezvládne samo. Kdo plánuje přejít přímo na kolo, měl by po tříkolce zkusit odrážedlo, jinak se dítě učí rovnováhu až na dvou kolech. '
          'Přehled najdete v kategorii <a href="/detske-trikolky/">dětské tříkolky</a>.</p>'
          '<h2>Jak vybrat velikost kola</h2>'
          '<p>Velikost kola se udává v palcích a označuje průměr kola. Vybírá se podle výšky dítěte a podle toho, jak dosáhne na zem. Dítě sedící na sedle má dosáhnout alespoň špičkami, u menších dětí raději celými chodidly. '
          'Řídítka mají být v takové výšce, aby se dítě nemuselo hrbit ani příliš zvedat paže.</p>'
          + T(['Velikost kol', 'Orientační výška dítěte', 'Kategorie'], [
              ['12 a 14 palců', 'zhruba 85 až 105 cm', '<a href="/detska-kola-12-14-palcu/">kola 12 a 14 palců</a>'],
              ['16 palců', 'zhruba 100 až 120 cm', '<a href="/detska-kola-16-palcu/">kola 16 palců</a>'],
              ['20 palců', 'zhruba 115 až 135 cm', '<a href="/detska-kola-20-palcu/">kola 20 palců</a>'],
              ['24 palců', 'zhruba 130 až 150 cm', '<a href="/detska-kola-24-palcu/">kola 24 palců</a>']]) +
          '<p>Hodnoty se u výrobců liší a pokrývají se, proto se vždy řiďte tabulkou u konkrétního kola. Pokud je dítě mezi velikostmi, vybírejte menší kolo, pokud dítě bezpečně dosáhne na zem a pohodlně na brzdy. S větším kolem se dítě necítí jistě a ztrácí ochotu jezdit. Koupě kola o dvě velikosti většího s tím, že dítě doroste, vede k opaku.</p>'
          '<h2>Rám, váha a převody</h2>'
          '<p>Hmotnost kola je u dětí zásadní. Kolo, které dítě sotva uzvedne, se nenaučí rozjíždět ani zastavit. Lehké hliníkové rámy se z tohoto pohledu hodí víc než ocelové, ocel zase snáší tvrdší zacházení a je levnější na opravu. '
          'U menších velikostí má kolo obvykle jeden převod a šlape se přímo. Od 20 palců přicházejí přehazovačky a rozsah převodů se rozšiřuje. Pro začátečníky stačí tři až sedm rychlostí, protože větší počet jen komplikuje ovládání.</p>'
          '<ul><li><strong>Jedna rychlost</strong> je jednoduchá, nevyžaduje seřizování a vyhovuje městu a rovině.</li>'
          '<li><strong>Řazení otočnou rukojetí</strong> je pro děti snazší než páčky, protože se ovládá celou dlaní.</li>'
          '<li><strong>Pevná vidlice</strong> je lehčí a nepotřebuje údržbu, odpružená se hodí pro rekreační terén, ale je těžší.</li></ul>'
          '<h2>Brzdy: bezpečnost především</h2>'
          '<p>Většina dětských kol má dva druhy brzd. Zpětný šlapací chod, tedy torpédo, brzdí otočením pedálů dozadu. Je intuitivní u nejmenších, ale pomalé a málo účinné při vyšší rychlosti. Ráfkové brzdy se ovládají pákami na řídítkách a vyžadují dostatečně silnou ruku. '
          'Páky musí mít nastavitelný dosah, aby na ně dítě dosáhlo i s malými prsty. Kdo hledá spolehlivý zpětný chod i ruční brzdu, volí kombinaci obojího, což je pro děti od zhruba pěti let praktické.</p>'
          '<p>Brzdy se kontrolují pravidelně. Zjistěte, zda páky nestojí na hraně řídítek a zda lanko není natažené. Stejně důležité je správné nastavení brzdových špalíků a výměna opotřebovaných. Jednoduché nářadí najdete v kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Bezpečnostní výbava</h2>'
          '<p>Helma patří k dětskému kolu stejně jako brzdy. Dětská helma má menší skořepinu, lehčí váhu a pásek nastavitelný pod bradou. Musí sedět rovně a nezakrývat výhled. Širší výběr nabízí <a href="/detske-cyklohelmy/">dětské cyklohelmy</a> a obecná kategorie <a href="/cyklisticke-helmy/">cyklistické helmy</a>. '
          'Pro jízdu po silnici je dobré mít světla vpředu i vzadu a odrazky na kolech a pedálech. Světelné příslušenství najdete v kategorii <a href="/cyklo-svetla/">světla na kolo</a>. Začátečníkům se hodí také kolenní a loketní chrániče z oddílu <a href="/chranice-a-helmy/">chrániče a helmy</a>.</p>'
          '<p>Nezapomeňte na zvonek, blatníky a kryt řetězu, které zabrání zašpinění oblečení a zachycení nohavice. U kol bez ochrany řetězu doporučujeme upravit nohavice sponkou.</p>'
          '<h2>Údržba a seřízení</h2>'
          '<p>Dětské kolo se používá nepravidelně, často zůstane týdny stát. Před sezónou zkontrolujte tlak v pláštích, utažení šroubů, stav brzd, řetězu a světel. Řetěz čistěte hadříkem a po osušení lehce promažte. '
          'Nadměrné mazivo přitahuje špínu a nanáší ji na oblečení, takže vždy otřete přebytek. Pro péči se hodí produkty z kategorie <a href="/cyklo-udrzba/">údržba kola</a>, pro zamykání před školou nebo obchodem pak <a href="/cyklo-zamky/">zámky na kolo</a>.</p>'
          '<p>Seřízení sedla a řídítek je u dětí potřeba měnit častěji než u dospělých. Jakmile dítě povyroste, zvedněte sedlo tak, aby při šlapání měla noha v dolní poloze téměř natažená kolena. Řídítka se zvedají o stejnou výšku, aby poloha zůstala pohodlná.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ol><li>Kupovat kolo o dvě velikosti větší s plánem, že z něj dítě vyroste. Vede to k pádům a ztrátě chuti jezdit.</li>'
          '<li>Spoléhat na pomocná kolečka dlouhodobě. Brání, aby se dítě naučilo rovnováhu, a proto je lepší odrážedlo.</li>'
          '<li>Vybrat kolo jen podle barvy a motivu. Důležitější je váha, brzdy a rozměr.</li>'
          '<li>Přehlédnout nastavitelnost. Sedlo a řídítka mají jít měnit bez speciálního nářadí.</li>'
          '<li>Koupit helmu na vyrůstání. Příliš velká helma nechrání a nesmí se používat.</li></ol>'
          '<h2>Oblečení a obuv na jízdu</h2>'
          '<p>Dítě na kole se potí a zároveň rychle vychladne, když zastaví. Hodí se tričko z prodyšného materiálu a vrstva navíc, kterou lze svléknout do batohu. Kalhoty by neměly mít široké nohavice, které se zachytí o řetěz, ani příliš volné šněrovací tkaničky. '
          'Obuv potřebuje pevnou, mírně tuhou podrážku, aby noha na pedálu neprokluzovala, sandály s otevřenou špičkou nejsou dobrý nápad. Pro delší vyjížďky pomohou rukavice s krátkými prsty a v zimě čepice pod helmu. Praktické kousky najdete v kategorii <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>'
          '<h2>Jak naučit dítě jezdit</h2>'
          '<p>Nejlepší je klidná rovná plocha bez provozu, například prázdné parkoviště nebo cyklostezka v době, kdy je málo lidí. Nejprve dítě jen tlačte za sedlo a nechte ho šlapat, pak podpírejte jen lehce a nakonec pusťte. Neutíkejte vedle kola a nedržte řídítka, dítě se tím naučí jen pohybovat se podle vašeho tahu. '
          'Učte také brzdění a odstoupení z kola do strany, protože právě tyto dovednosti ušetří nejvíc drobných pádů. Trpělivost, krátké lekce a pochvala fungují lépe než dlouhé zkoušení v rozhořčení.</p>'
          '<h2>Alternativy a návaznosti</h2>'
          '<p>Když dítě z kola vyroste, pokračuje často na větší velikost, nebo přejde na <a href="/jizdni-kola/">jízdní kola</a> pro dospívající. Někdo preferuje <a href="/kolobezky/">koloběžky</a>, které se skládají do batohu. '
          'Při společných výletech pomůže <a href="/cyklo-sedacky-a-voziky/">dětská sedačka nebo vozík za kolo</a>. Celý obor shrnuje hlavní kategorie <a href="/cyklistika/">cyklistika</a>, ke které se dostanete i z menu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii jsou zastoupeny například ' + B(('dino','Dino'),('dino-bikes','Dino Bikes'),('toimsa','Toimsa'),('davi','Davi'),('acra-sport','ACRA Sport'),('author','Author'),('olpran','Olpran'),('yedoo','Yedoo'),('attabo','Attabo'),('rascal','Rascal'),('btwin','Btwin'),('kross','Kross')) +
          '. Nabídky se liší materiálem rámu, váhou a výbavou, takže porovnávejte konkrétní modely a nikoli jen název výrobce. U stejného kola často najdete několik obchodů, mezi kterými se liší doručení.</p>',
    faq=[('Kdy má dítě přejít z odrážedla na kolo?', 'Obvykle ve chvíli, kdy odrážedlem jezdí jistě, drží rovnováhu a dokáže chvíli klouzat s nohama nad zemí. To bývá kolem tří až pěti let, ale rozhoduje vývoj dítěte. Pomocná kolečka nejsou nutná, dítě se rovnováhu již naučilo.'),
         ('Jak poznám správnou velikost dětského kola?', 'Podívejte se na výšku dítěte a na to, zda dosáhne při sezení na zem alespoň špičkami. Pak zkontrolujte, že na řídítka dosáhne s mírně pokrčenými lokty a že na brzdu dosáhne prsty. Orientační tabulky výrobců pomohou, ale zkouška je spolehlivější.'),
         ('Jsou pomocná kolečka vhodná?', 'Dobré jako krátkodobé řešení pro dítě, které nejistě šlape, ale nenaučí rovnováhu. Pokud dítě odrážedlo nezná, lépe se učí bez koleček tak, že mu sedlo sníží a nechá se odrážet nohama. Po zvládnutí rovnováhy se kolečka sundají během několika dnů.'),
         ('Jaké brzdy má mít první kolo?', 'Pro nejmenší je vhodný zpětný šlapací chod, protože je intuitivní. Od zhruba pěti let se přidává ruční brzda. Páky musí mít nastavitelný dosah, aby je dítě zmáčklo celými prsty. Kombinace obou typů brzd zvyšuje jistotu na svazích.'),
         ('Hliníkový, nebo ocelový rám?', 'Hliník je lehčí a nekoroduje, proto se doporučuje pro menší děti. Ocel je pevná, tlumí otřesy a lépe snáší hrubé zacházení, ale váží víc. U kol od 20 palců se hmotnost projeví víc, takže rozdíl stojí za zvážení.'),
         ('Kolik rychlostí má mít dětské kolo?', 'Do 16 palců obvykle jedna. U 20 palců se hodí tři až sedm rychlostí, přehazovačka s otočným řazením je pro děti jednodušší. Víc rychlostí dává smysl až u 24 palců a pro děti, které jezdí v kopcovitém terénu.'),
         ('Musí dítě nosit helmu?', 'Doporučuje se u všech dětí při jakékoli jízdě na kole, odrážedle, koloběžce nebo tříkolce. V ČR platí povinnost helmy pro cyklisty do 18 let. Helma má sedět rovně, ne se kývat a pásek nesmí škrtit. Po pádu na hlavu ji vyměňte.'),
         ('Jak často kontrolovat dětské kolo?', 'Před každou sezónou a pak jednou za měsíc během jízdy. Zkontrolujte tlak v pláštích, brzdy, utažení šroubů, řetěz a světla. Kdykoli dítě povyroste, upravte výšku sedla a řídítek. Opotřebené špalíky nebo praskliny v plášti vyměňte hned.'),
         ('Hodí se kupovat použité kolo?', 'Pro rychle rostoucí děti ano, pokud je rám nepoškozený, brzdy fungují a velikost sedí. Použité kolo ale kontrolujte pečlivě, zejména brzdová lanka, plášť, řetěz a utažení vidlice. Helmu naopak pořizujte vždy novou, protože nevíte, zda neutrpěla pád.'),
         ('Jak využít Sportecu při výběru?', 'Na Sportece vidíte u stejného modelu nabídky více českých obchodů vedle sebe, včetně velikostí a dostupnosti. V jednotlivých podkategoriích můžete filtrovat podle značky nebo palců. Před objednávkou se vyplatí zkontrolovat, zda obchod dodává kolo složené a seřízené.')])

# ------------------------------------------------------------------ golf
NEW['golf'] = dict(long=True,
    title='Golf: hole, míčky, tašky, oblečení a obuv',
    desc='Golfová výbava na jednom místě: hole, míčky, tašky, vozíky, oblečení i obuv. Rady pro začátečníky a srovnání nabídek českých obchodů.',
    intro='<p>Golf je sport, ve kterém se výbava skládá z mnoha drobností a každá z nich ovlivní pohodu na hřišti. Hole určují, jak míček poletí, obuv rozhoduje o stabilitě při švihu a oblečení o tom, zda přečkáte čtyři hodiny hry na slunci, ve větru nebo v dešti. '
          'V kategorii <strong>golf</strong> najdete všechno od prvního tréninkového setu po doplňky pro zkušeného hráče.</p>'
          '<p>Sporteka srovnává nabídky českých obchodů u stejného zboží, takže ověříte, kde je skladem pravá nebo levá hůl i potřebná velikost obuvi. Nabídka se dělí na '
          '<a href="/golfove-hole/">golfové hole</a>, <a href="/golfove-micky/">golfové míčky</a>, <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a>, '
          '<a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a> a <a href="/golfove-doplnky/">golfové doplňky</a>. Níže vysvětlujeme, na co se při nákupu soustředit a v jakém pořadí vybavení doplňovat.</p>',
    guide='<h2>Základní výbava golfisty</h2>'
          '<p>Nováček často přemýšlí, zda si koupit celý set najednou. Rozumnější je postupovat po částech, protože první měsíce hry odhalí, co vám vyhovuje. Přehled vás nasměruje na to nejdůležitější.</p>'
          + T(['Část výbavy', 'K čemu slouží', 'Poznámka pro začátečníka'], [
              ['Golfové hole', 'úder míčku na různé vzdálenosti', 'začněte menším setem, ne všemi čtrnácti holemi'],
              ['Golfové míčky', 'hra a trénink', 'pořiďte víc kusů, na začátku se ztrácejí'],
              ['Taška a vozík', 'přenos holí po hřišti', 'záleží, zda půjdete pěšky, nebo se svezete'],
              ['Obuv', 'stabilita při švihu a přilnavost na trávě', 'vyzkoušejte s ponožkami, které nosíte na hřišti'],
              ['Rukavice', 'jistý úchop rukojeti', 'nosí se na jedné ruce, praváci na levé'],
              ['Oblečení', 'pohodlí a dodržení dress codu klubu', 'zjistěte pravidla hřiště předem'],
              ['Doplňky', 'tee, značkovače, ručníky, deštníky', 'drobnosti, které se hodí při každém kole']]) +
          '<p>Pokud hrajete jen občas nebo teprve zkoušíte, nemusíte kupovat vše nové. Půjčovny na hřištích nabízejí hole a vozíky a pomohou rozhodnout, co chcete vlastnit. Teprve pravidelní hráči investují do vlastního setu přizpůsobeného jejich švihu.</p>'
          '<h2>Golfové hole</h2>'
          '<p>V bagu smí být nejvýše čtrnáct holí, ale nikdo vás nenutí mít všechny. Dělí se na dřeva, železa, hybridy, wedge a patry. Dřeva se používají na dlouhé rány z odpaliště, železa na přesnější rány z fairwaye, wedge na krátké nájezdy k jamce a putter na hru na greenu.</p>'
          '<ul><li><strong>Driver</strong> je nejdelší hůl s největší hlavou, odpaluje se jím z odpaliště nejdelší vzdálenost.</li>'
          '<li><strong>Fairwayová dřeva</strong> jsou kratší a snadněji se hrají z trávy.</li>'
          '<li><strong>Hybridy</strong> spojují vlastnosti dřev a želez a pro mnoho začátečníků nahrazují dlouhá železa.</li>'
          '<li><strong>Železa</strong> se číslují, nižší číslo znamená menší sklon čela a delší ránu.</li>'
          '<li><strong>Wedge</strong> mají největší sklon a slouží k vysokým krátkým úderům a hře z bunkru.</li>'
          '<li><strong>Putter</strong> se používá na greenu a jeho výběr je velmi osobní.</li></ul>'
          '<p>Důležitá je i délka násady a materiál. Ocelové násady jsou těžší a stabilnější, grafitové lehčí a pomáhají pomalejšímu švihu. Vhodnou délku a pružnost je nejlepší ověřit na driving range (cvičném odpališti) nebo u fittera. Kompletní nabídku mapuje kategorie <a href="/golfove-hole/">golfové hole</a>.</p>'
          '<h2>Pravák, levák a pružnost násady</h2>'
          '<p>Hole se vyrábějí pro praváky i leváky a poznáte je podle strany, na které je čelo. Leváci mají v nabídce většinou méně modelů, proto se vyplatí zkontrolovat dostupnost před zamilováním se do konkrétního setu. '
          'Pružnost násady se značí písmeny od měkké po tuhou. Čím rychlejší švih, tím tužší násada. Pomalejším a starším hráčům, ženám a juniorům vyhovují měkčí. Příliš tuhá násada nepruží a míček letí nízko a krátce.</p>'
          '<h2>Míčky</h2>'
          '<p>Golfové míčky se liší konstrukcí a tvrdostí. Dvouvrstvé míčky jsou odolné a dobře létají, hodí se začátečníkům a rekreačním hráčům. Víceslojové míčky nabízejí větší kontrolu na greenu a vyhovují zkušenějším hráčům. '
          'Zbarvení bílé je klasika, žluté a oranžové se lépe hledají v trávě a v zimě na sněhu. Při nákupu se dívejte na označení čísla a na to, zda jde o nové, nebo repasované kusy. Podrobnosti najdete v kategorii <a href="/golfove-micky/">golfové míčky</a>.</p>'
          '<p>Při tréninku se hodí levnější míčky na driving range a dražší si nechte na hřiště. Míčky s vlastním potiskem poznáte na hřišti snáz, což zabrání záměně s míčkem jiného hráče.</p>'
          '<h2>Tašky a vozíky</h2>'
          '<p>Taška musí unést hole, míčky, rukavici a pláštěnku, a přitom se pohodlně nosí. Rozlišují se tři hlavní typy.</p>'
          '<ul><li><strong>Nosné tašky</strong> mají popruhy a stojan, jsou lehké a hodí se na krátké hřiště a pro hru pěšky.</li>'
          '<li><strong>Vozíkové tašky</strong> mají plochou základnu a pevný rám pro upevnění na vozík.</li>'
          '<li><strong>Tourové tašky</strong> jsou velké, s mnoha kapsami, a hodí se pro hráče, kteří jezdí v elektrickém vozíku.</li></ul>'
          '<p>Vozíky mohou být ruční tříkolové, dvoukolové skládací nebo elektrické. Ruční se skládají do kufru a jsou nenáročné na údržbu. Elektrické šetří záda, ale vyžadují nabíjení a vyšší hmotnost při přepravě. '
          'Vyberte si podle toho, zda hřiště leží v kopcovitém terénu, a jak daleko chodíte. Kategorie <a href="/golfove-tasky-a-voziky/">golfové tašky a vozíky</a> nabízí všechny druhy.</p>'
          '<h2>Oblečení a obuv</h2>'
          '<p>Většina klubů vyžaduje na hřišti polokošili s límečkem nebo golfové triko, kalhoty nebo šortky střižené do pasu a golfovou obuv. Džíny a tílka bývají zakázané. Zeptejte se předem, zda klub dress code uplatňuje. '
          'Oblečení má být elastické, protože švih vyžaduje volnost v ramenou a trupu, a rychle schnoucí, protože hra trvá několik hodin.</p>'
          '<h3>Obuv</h3>'
          '<p>Golfové boty mají plastové nebo gumové hroty, případně bezhroté podrážky s vroubkováním. Hroty drží lépe na vlhké trávě, bezhroté jsou univerzálnější a použijete je i mimo hřiště. Boty mají být pohodlné při chůzi, protože za kolo ujdete několik kilometrů. '
          'Nepromokavé varianty se hodí na jaro a podzim, vzdušné na léto. Podle toho si doplňte <a href="/sportovni-ponozky/">sportovní ponožky</a>, které odvádějí pot a nesmí tlačit.</p>'
          '<h3>Vrstvení podle počasí</h3>'
          '<p>Základem je tričko nebo polokošile. Na chladnější dny přidejte <a href="/mikiny/">mikinu</a> nebo lehkou vestu a do deště nepromokavou bundu z oddílu <a href="/sportovni-bundy/">sportovní bundy a vesty</a>. V létě pomůže <a href="/cepice-a-celenky/">kšiltovka</a> a v zimě čepice a termo rukavice. '
          'Další tipy na funkční kousky najdete v kategoriích <a href="/sportovni-tricka/">trička a tílka</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>. Kompletní nabídku golfových kousků shrnuje <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a>.</p>'
          '<h2>Doplňky, které se hodí</h2>'
          '<p>Drobnosti se na začátku podceňují. Rukavice zlepšuje úchop a chrání dlaň před puchýři. Tee zvedá míček nad zem při odpalu z odpaliště. Značkovač a vidlička na urovnání důlků po dopadu míčku patří ke slušnému chování. '
          'Ručník na hole a míčky, rangefinder pro měření vzdáleností a deštník dělají hru pohodlnější. Kategorie <a href="/golfove-doplnky/">golfové doplňky</a> je široká a hodí se k ní i pláštěnky na tašku a kryty hlav holí (headcovery).</p>'
          '<h2>Výbava podle úrovně hráče</h2>'
          '<p>Začátečník potřebuje odpouštějící hole s větší hlavou, které zvládnou i ne zcela čisté zásahy. Na hřiště zatím stačí lehká nosná taška a pár míčků. '
          'Pokročilý hráč začíná řešit shodu hole s vlastním švihem, zajímá ho spin míčku, vzdálenosti jednotlivých holí a stabilita obuvi. Mnozí si v té chvíli pořizují fitting, při kterém odborník změří rychlost švihu a doporučí vhodné násady a loft. '
          'Junioři a děti by měli používat speciální juniorské sady odpovídající výšce, protože dospělé hole jsou příliš dlouhé a těžké a učí špatné návyky. Ženy a senioři často profitují z lehčích holí s měkčími násadami.</p>'
          '<h2>Sezóna a počasí na hřišti</h2>'
          '<p>Golf se hraje od jara do podzimu a na řadě hřišť i v zimě, pokud nezmrzne. V létě vás ochrání před sluncem kšiltovka, ochranný krém a dostatek vody. Na jaře a na podzim se hodí vrstvy, které se dají snadno svléknout, a nepromokavá bunda. '
          'Mokrá tráva zhoršuje přilnavost obuvi a míčky létají kratší, proto se vyplatí kontrolovat hroty a mít po ruce ručník. V zimě pomáhá termální spodní vrstva, zahřívací vložky do rukavic a žluté míčky, které se na sněhu a v mokré trávě snáz najdou.</p>'
          '<h2>Péče o výbavu</h2>'
          '<p>Hole po každém kole otřete a očistěte drážky na čelech, protože zanesené čelo ovlivňuje rotaci míčku. Rukojeti se myjí vlažnou vodou s jemným mýdlem a opotřebovanou rukojeť vyměňte, jakmile je hladká nebo tvrdá. '
          'Tašku nechte po dešti vyschnout, vlhká by plesnivěla. Boty se čistí kartáčem, kožené se občas ošetří impregnací. Rukavice se suší volně, nikdy na topení, kůže by ztvrdla.</p>'
          '<h2>Časté chyby začátečníků</h2>'
          '<ol><li>Koupit kompletní set předem, ještě než víte, jak často budete hrát.</li>'
          '<li>Použít příliš dlouhé nebo příliš tuhé hole, které neodpovídají výšce a síle.</li>'
          '<li>Vybrat obuv jen podle vzhledu. Pohodlí při chůzi na hřišti je důležitější.</li>'
          '<li>Podcenit počasí a nemít pláštěnku nebo náhradní rukavici.</li>'
          '<li>Kupovat nejdražší míčky na učení, když ztratíte desítky kusů.</li></ol>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('inesis','Inesis'),('under-armour','Under Armour'),('adidas','Adidas'),('nike','Nike'),('taylormade','Taylormade'),('titleist','Titleist'),('footjoy','Footjoy'),('callaway','Callaway'),('new-era','New Era')) +
          '. Některé jsou zaměřené na hole a míčky, jiné na oblečení nebo obuv. Neřiďte se jen jménem, srovnávejte konkrétní modely, parametry a dostupnost. Sporteka vám ukáže nabídky několika obchodů najednou, takže si můžete vybrat podle doručení a podmínek vrácení.</p>',
    faq=[('Co si pořídit jako první, když chci začít s golfem?', 'Začněte hodinami s trenérem a půjčenými holemi, abyste zjistili, zda vás hra baví. Potom pořiďte obuv, rukavici a pár míčků, a až později menší set holí. Kompletní sadu kupujte teprve po několika měsících, kdy znáte svůj švih a styl hry.'),
         ('Kolik holí smí být v tašce?', 'Pravidla golfu povolují nejvýše čtrnáct holí v tašce během kola. Většina začátečníků hraje s menším počtem, například s driverem, hybridem, několika železy, wedgem a putterem. Víc holí není výhodou, pokud je nedokážete rozlišit.'),
         ('Jak vybrat správnou délku hole?', 'Délka závisí na výšce, délce paží a postoji. Při správné délce stojíte uvolněně, záda máte lehce skloněná a ruce visí pod rameny. Přesné měření provádí fitter, který zohlední i styl švihu. Pro děti existují speciální juniorské sady po věkových kategoriích.'),
         ('Jaký je rozdíl mezi dvouvrstvým a víceslojovým míčkem?', 'Dvouvrstvý míček má pevné jádro a odolný obal, létá rovně a vydrží víc. Víceslojový nabízí citlivější reakci na greenu, ale rychleji se opotřebuje. Začátečníkům a rekreačním hráčům stačí dvouvrstvý, víceslojový dává smysl při zlepšené technice.'),
         ('Hodí se nosná taška, nebo vozík?', 'Nosná taška je lehká a hodí se na krátká a rovná hřiště nebo hru pěšky. Vozík uleví zádům na delších a kopcovitějších hřištích a dá se použít se vozíkovou taškou. Elektrický vozík je pohodlný, ale těžší na přepravu v autě.'),
         ('Musím mít golfovou obuv?', 'Řada hřišť ji vyžaduje a pro stabilitu při švihu je užitečná. Podrážka s hroty nebo vroubkováním drží na mokré trávě a zabraňuje uklouznutí. Pro jednorázovou hru v půjčovně mohou stačit pohodlné boty s plochou podrážkou, zeptejte se na pravidla hřiště.'),
         ('Jaké oblečení je na golf vhodné?', 'Typická je polokošile s límečkem, kalhoty nebo šortky do pasu a čepice či kšiltovka. Džíny, tílka a teplákové soupravy bývají zakázané. Zvolte pružné a rychleschnoucí materiály, které se přizpůsobí švihu, a pro chladnější dny přidejte lehkou mikinu nebo bundu.'),
         ('Na které ruce se nosí golfová rukavice?', 'Pravák ji nosí na levé ruce, levák na pravé, tedy na ruce vedoucí hůl. Rukavice má padnout těsně, ale nesmí tlačit. Kožené jsou jemnější a lépe drží, syntetické odolnější vůči vlhkosti. Mnozí hráči mají dvě a střídají je podle počasí.'),
         ('Jak se starat o golfové hole?', 'Po hře otřete hlavy a drážky vlhkým hadříkem a očistěte násady. Rukojeti občas omyjte jemným mýdlem a vyměňte, když zhladnou. Hole nenechávejte v horkém autě a vozte je v tašce s kryty hlavy. Poškozené násady nechte zkontrolovat v servisu.'),
         ('Kde porovnám nabídky golfové výbavy?', 'Na Sportece vidíte u stejného zboží nabídky více českých obchodů vedle sebe. Filtrujte podle značky, velikosti nebo dostupnosti a sledujte doručení i podmínky vrácení. U holí a obuvi se vyplatí zkontrolovat, zda lze zboží vyměnit za jinou velikost nebo délku.')])

# ------------------------------------------------------------------ funkcni-mikiny
NEW['funkcni-mikiny'] = dict(long=True,
    title='Funkční mikiny: na běh, trénink i hory',
    desc='Funkční mikiny na běh, fitness, turistiku i zimní sporty. Jak vybrat materiál, střih a zip, plus srovnání nabídek českých obchodů.',
    intro='<p>Funkční mikina není obyčejná mikina z bavlny. Je navržená tak, aby odváděla pot od těla, rychle schla a při pohybu nepřekážela. Vezmete ji na běh, na trénink, na lyže nebo na podzimní procházku a poznáte rozdíl hned při prvním zpoceném úseku. '
          'V kategorii <strong>funkční mikiny</strong> najdete dámské, pánské i dětské modely pro různé sporty a roční období.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného kusu, takže ověříte, kde je skladem vaše velikost. Příbuzné kategorie jsou obecné <a href="/mikiny/">mikiny</a>, '
          '<a href="/fleecove-mikiny/">fleecové mikiny</a> a <a href="/merino-mikiny/">merino mikiny a svetry</a>. Níže vysvětlujeme materiály, střihy, vrstvení a péči, abyste vybrali mikinu, která se nezkroutí po prvním praní.</p>',
    guide='<h2>Čím se funkční mikina liší od běžné</h2>'
          '<p>Klasická bavlněná mikina nasaje pot jako houba, zůstane těžká a studená a schne několik hodin. Funkční mikina používá syntetická vlákna, případně jejich směs s elastanem nebo vlnou, která vlhkost přesouvají na vnější stranu látky. '
          'Díky tomu zůstává kůže sušší a tělo se tolik neochlazuje. Navíc je látka pružná, lehčí a lépe se s ní pohybuje.</p>'
          + T(['Vlastnost', 'Funkční mikina', 'Bavlněná mikina'], [
              ['Odvod potu', 'odvádí vlhkost na povrch', 'nasákne a zůstane vlhká'],
              ['Schnutí', 'rychlé, často během hodiny', 'pomalé, i několik hodin'],
              ['Pružnost', 'elastan a pletený vzor dovolují pohyb', 'pevnější, méně pružná'],
              ['Váha při nasáknutí', 'téměř stejná jako suchá', 'výrazně těžší'],
              ['Použití', 'sport, turistika, aktivní den', 'volný čas, chlad bez pohybu']]) +
          '<p>Neznamená to, že bavlna je špatná, jen se nehodí pro pohyb s potem. Na sezení v kanceláři nebo doma na gauči je pohodlnější měkká bavlna.</p>'
          '<h2>Materiály a jejich vlastnosti</h2>'
          '<ul><li><strong>Polyester</strong> je nejčastější. Je odolný, lehký, rychle schne a dobře udrží tvar, ale může zadržovat pachy.</li>'
          '<li><strong>Polyamid (nylon)</strong> se používá na zesílení loktů a ramen, protože dobře snáší otěr.</li>'
          '<li><strong>Elastan</strong> je pružné vlákno ve směsi, kterému mikina vděčí za strečové chování.</li>'
          '<li><strong>Fleecová úprava</strong> uvnitř vytváří vzduchové kapsy a hřeje při nízké hmotnosti.</li>'
          '<li><strong>Vlna a merino</strong> zadržuje méně pachu a hřeje i vlhká. Samostatnou nabídku najdete v kategorii <a href="/merino-mikiny/">merino mikiny a svetry</a>.</li></ul>'
          '<p>Štítek na mikině vždy ukazuje složení a postup praní. Čím vyšší podíl syntetiky, tím rychleji schne, čím víc vlny, tím lépe snáší opakované nošení bez praní.</p>'
          '<h2>Typy funkčních mikin</h2>'
          '<h3>Lehká na běh a trénink</h3>'
          '<p>Je z tenké pleteniny s malou gramáží, často se zipem v límci nebo krátkým zipem na hrudi, který pomáhá s regulací teploty. Bývá prodloužená v zádech a má zesílené švy mimo místa otěru. '
          'Hodí se na běh, kolo nebo kondiční trénink a nosí se přes <a href="/sportovni-tricka/">funkční triko</a>. Doplňte ji <a href="/leginy/">legínami</a> nebo <a href="/sportovni-kalhoty/">sportovními kalhotami</a>.</p>'
          '<h3>Střední vrstva na turistiku</h3>'
          '<p>Je silnější, často s mřížkovou nebo vlněnou vnitřní stranou, která zachytí teplý vzduch. Hřeje, ale prodýchává, takže se v ní nezapotíte při výstupu. Při změně počasí se zvládne přidat bunda. '
          'Další inspirace najdete v kategorii <a href="/outdoor/">outdoor a turistika</a> a v příbuzných <a href="/fleecove-mikiny/">fleecových mikinách</a>.</p>'
          '<h3>Na zimní sporty</h3>'
          '<p>Při běžkování nebo skialpinismu se člověk zahřeje a zároveň vystaví větru. Hodí se mikina s úzkým střihem, vyšším límcem a vnitřní stranou, která odvádí pot. Pod bundu ji nosíte bez dalších vrstev nebo s tenkým spodním prádlem. '
          'Pro chladnější dny doplníte <a href="/termopradlo/">funkční termo prádlo</a> a čepici či <a href="/nakrcniky-a-satky/">nákrčník</a>. Kategorie <a href="/zimni-sporty/">zimní sporty</a> mapuje celou výbavu.</p>'
          '<h3>Mikina s kapucí a bez ní</h3>'
          '<p>Kapuce chrání před větrem a mrholením, ale pod bundou překáží a pod helmou nemá místo. Mikina bez kapuce a s vyšším límcem je univerzálnější pro vrstvení. Kdo si chce vybrat styl pro každodenní nošení, uvítá kapuci, kdo sportuje intenzivně, nechá si ji raději doma.</p>'
          '<h2>Střih, zip a detaily</h2>'
          '<p>Správně padnoucí funkční mikina sedí přiléhavě, ale nestahuje. Rukávy mají sahat až na zápěstí i při zvednutých rukách a spodní lem se nemá vyhrnovat. U běžeckých modelů pomáhá prodloužená záda, u turistických delší rukávy s palcovými otvory. '
          'Oblíbené detaily jsou kapsa na zip na uložení klíčů, reflexní prvky pro jízdu za šera, větrací otvory v podpaží a ploché švy, které neodírají.</p>'
          '<ul><li><strong>Celý zip</strong> umožňuje rychle se ochladit a snadno mikinu svléknout.</li>'
          '<li><strong>Krátký zip</strong> je lehčí a pevnější a drží teplo při pasivním pohybu.</li>'
          '<li><strong>Palcové otvory</strong> drží rukávy na místě a chrání hřbet ruky před chladem.</li>'
          '<li><strong>Reflexní prvky</strong> zvyšují viditelnost při běhu a jízdě na kole za šera.</li></ul>'
          '<h2>Gramáž a tloušťka materiálu</h2>'
          '<p>Hustota pleteniny, označovaná jako gramáž, určuje, jak moc mikina hřeje a jak dobře dýchá. Lehké pleteniny kolem nižších stovek gramů na metr čtvereční patří na běh a rychlý pohyb, střední se hodí na turistiku a zimní procházky, těžší vyhovují spíše posezení u ohně nebo klidnému pohybu v mrazu. '
          'Údaj najdete u popisu produktu, ale ne každý výrobce ho uvádí, a pak pomůže složení a popis vnitřní strany. Příliš silná mikina při rychlém tempu přehřívá, příliš tenká zase nezahřeje při stání a čekání.</p>'
          '<h2>Pachy, antibakteriální úpravy a delší životnost</h2>'
          '<p>Syntetická vlákna mají tendenci zadržovat pach potu, proto výrobci přidávají antibakteriální úpravy, například stříbrné ionty nebo speciální impregnace. Fungují po omezený počet praní a nenahradí pravidelné praní. '
          'Životnost mikiny prodloužíte, když ji nenosíte pod těžkým batohem, který ji třením zdrsňuje, a vyhnete se kontaktu se suchým zipem, který vlákna vytahuje. Žmolky na rukávech a v podpaží lze opatrně odstranit strojkem, bez tlaku na látku. '
          'Menší díry se dají zalepit nebo zašít a opravená mikina slouží další sezónu.</p>'
          '<h2>Cestování a zabalení</h2>'
          '<p>Funkční mikina je ideální do batohu, protože je lehká, malá a rychle schne. Na vícedenní túru stačí jedna, kterou večer vyvěsíte ke stanu, další oblečení pak nemusíte nosit. Při cestě letadlem se hodí jako vrstva, která zahřeje v klimatizované kabině. '
          'Nejlepší je kus s krátkým zipem a kapsou, do které se vejde mobil nebo doklady.</p>'
          '<h2>Velikost a vrstvení</h2>'
          '<p>Rozměry se mezi značkami liší, proto si před objednávkou přečtěte tabulku velikostí a porovnejte obvod hrudníku, boků a délku rukávu. Mezi velikostmi vybírejte podle plánované vrstvy. Pod mikinu chcete jen tričko, vezměte přesnou velikost, '
          'když ale plánujete zimní spodní prádlo, vezměte jednu velikost navíc. Příliš těsná mikina brzdí pohyb a omezuje cirkulaci vzduchu.</p>'
          '<p>Základní pravidlo vrstvení zní: spodní vrstva odvádí pot, střední hřeje, vnější chrání před větrem a deštěm. Funkční mikina je typická střední vrstva. Kdo na ni plánuje ještě bundu, vybere tenčí kus. Větrovku nebo lehkou bundu najdete v kategorii <a href="/sportovni-bundy/">sportovní bundy a vesty</a>.</p>'
          '<h2>Pro koho jaká mikina</h2>'
          '<ul><li><strong>Běžec</strong> ocení nízkou váhu, prodyšnost a reflexní prvky, ideálně s krátkým zipem.</li>'
          '<li><strong>Kondiční a posilovací trénink</strong> potřebuje strečovou mikinu bez drsných švů. Podrobnosti najdete v kategorii <a href="/fitness/">fitness a posilování</a>.</li>'
          '<li><strong>Turista</strong> vybírá teplejší modely s vyšším límcem a kapsami.</li>'
          '<li><strong>Děti</strong> potřebují odolnou mikinu, která snese pískoviště i hřiště, a snadno se pere.</li>'
          '<li><strong>Cyklista</strong> by měl zvolit střih s prodlouženými zády, který se při předklonu nezvedá.</li></ul>'
          '<h2>Péče a praní</h2>'
          '<p>Syntetické materiály snesou častější praní než bavlna, ale mají svoje pravidla. Perte při nižší teplotě podle štítku, nepoužívejte aviváž, protože ucpává vlákna a snižuje schopnost odvádět vlhkost. '
          'Zipy před praním zapněte a mikinu otočte naruby. Nesušte na topení ani v horké sušičce, elastan by ztrácel pružnost. Pokud mikina zapáchá, pomůže namočení do vody s kapkou octa nebo speciálním pracím prostředkem pro sportovní prádlo.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ol><li>Zaměnit funkční a bavlněnou mikinu. Při sportu se bavlněná hodí jen na posezení po výkonu.</li>'
          '<li>Koupit příliš silnou mikinu na intenzivní pohyb. V ní se upečete, i když je venku chladno.</li>'
          '<li>Prát s aviváží a tím zhoršit schopnost odvodu potu.</li>'
          '<li>Podcenit rukávy a délku. Při zvednutých rukou se nemají vyhrnout nad zápěstí.</li>'
          '<li>Vybrat jen podle barvy, bez ověření složení a tabulky velikostí.</li></ol>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete například ' + B(('dare2b','Dare2b'),('adidas','Adidas'),('champion','Champion'),('jordan','Jordan'),('hannah','Hannah'),('regatta','Regatta'),('klimatex','Klimatex'),('swix','Swix'),('kilpi','Kilpi'),('on','On'),('progress','Progress')) +
          '. Některé jsou zaměřené na outdoor a turistiku, jiné na běh nebo styl ulice. Porovnávejte konkrétní modely podle složení, střihu a dostupnosti, ne podle logu na hrudi. Sporteka ukazuje u stejného kusu nabídky více obchodů, takže vyberete podle doručení i podmínek vrácení.</p>',
    faq=[('Čím se funkční mikina liší od bavlněné?', 'Funkční mikina je ze syntetických nebo směsových vláken, která odvádějí pot od kůže a rychle schnou. Bavlněná vlhkost nasákne, zůstane těžká a pomalu schne. Při pohybu je proto funkční mikina pohodlnější, bavlna se hodí spíš pro klidné nošení.'),
         ('Hodí se funkční mikina na běh?', 'Ano, zvlášť lehčí modely s krátkým zipem, prodlouženými zády a plochými švy. V chladném počasí se nosí přes tričko, při větru se doplní bundou. Pokud se při běhu přehříváte, zvolte tenčí materiál nebo jen tričko a mikinu si uvažte kolem pasu.'),
         ('Jak vybrat velikost funkční mikiny?', 'Porovnejte vlastní obvod hrudníku a délku rukávu s tabulkou výrobce. Sedí-li mikina příliš volně, ztrácí schopnost odvádět vlhkost, příliš těsná omezuje pohyb. Plánujete-li pod ni zimní spodní prádlo, vezměte raději o jednu velikost víc.'),
         ('Jak často lze funkční mikinu prát?', 'Po každém potním použití je lepší ji vyprat, jinak se v ní drží pachy. Perte při nízké teplotě podle štítku, bez aviváže, a nesušte na topení. Syntetika vydrží častější praní než přírodní materiály, zatímco merino zvládne několik nošení bez praní.'),
         ('Je lepší mikina s kapucí, nebo bez?', 'Bez kapuce je univerzálnější do vrstvení pod bundu nebo pod helmu. Kapuce se hodí na volný čas, procházky a při větru či mrholení. Při intenzivním pohybu překáží a při vyšší rychlosti vlaje, proto ji většina sportovců nepoužívá.'),
         ('Čím je lepší merino mikina?', 'Merino zadržuje méně pachu, hřeje i vlhké a dobře reguluje teplotu. Funkční polyester schne rychleji a je odolnější, což ocení běžci. Obě varianty se hodí do vrstvení, rozhodněte se podle intenzity pohybu a toho, jak často chcete oblečení prát.'),
         ('Hodí se funkční mikina na zimu?', 'Ano jako střední vrstva pod bundu. Ve větším mrazu ji doplňte termoprádlem a čepicí. Mikina sama větru neodolá, proto přes ni nosíte větrovku nebo membránovou bundu. Při intenzivním sportu stačí lehčí kus, při pomalé chůzi volte silnější, s vnitřní strukturou.'),
         ('Jak odstranit zápach z funkční mikiny?', 'Pomáhá okamžité vyvěšení po sportu, praní při nízké teplotě a speciální prací gel na sportovní prádlo. Zápach se může držet v polyesteru, proto zkuste namočení do vody s trochou octa. Aviváž nepoužívejte, vlákna ucpe a zápach zhorší.'),
         ('Mohu nosit funkční mikinu každý den?', 'Ano, pokud vám vyhovuje střih a materiál. Jen počítejte s tím, že syntetika nemusí být tak měkká jako bavlna, a při sezení v kanceláři se může elektrizovat. Pro volný čas se často vybírají směsi s měkčí vnitřní stranou nebo se skrytými švy.'),
         ('Kde porovnám nabídky funkčních mikin?', 'Na Sportece vidíte u stejného kusu nabídky více českých obchodů vedle sebe, včetně dostupných velikostí. V kategorii filtrujte podle značky, velikosti a dostupnosti a před objednávkou ověřte podmínky vrácení, u oblečení se výměna velikosti hodí.')])
