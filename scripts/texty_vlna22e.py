"""sporteka.cz — wave 22e (4. 11. 2026): long texts (>= 1650 words) for snowboardove-sety, detske-plavky, rekreacni-brusle, golfove-obleceni-a-obuv.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ snowboardove-sety
NEW['snowboardove-sety'] = dict(long=True,
    title='Snowboardy s vázáním (sety): jak vybrat komplet',
    desc='Snowboardové sety s vázáním pro začátečníky, děti i pokročilé. Velikost podle výšky, profil prkna, flex, vázání a boty. Porovnejte nabídky obchodů.',
    intro='<p>Snowboardový set je prkno prodávané rovnou s vázáním, takže odpadá hledání kompatibilních dílů a kompletní základ máte v jedné krabici. Pro prvního snowboardistu je to nejpohodlnější cesta na svah, pro rodiče dětského jezdce často jediná rozumná volba, protože dítě z výbavy vyroste za jednu či dvě sezony. V katalogu najdete pánské, dámské, dětské i juniorské komplety různé délky a tuhosti.</p>'
          '<p>Většina sad v nabídce pochází od značek '
          + B(('raven', 'Raven'), ('gravity', 'Gravity'), ('hatchey', 'Hatchey'), ('beany', 'Beany'), ('vasa', 'Vasa'), ('ride', 'Ride'), ('bataleon', 'Bataleon')) +
          '. Sporteka vedle sebe řadí nabídky českých obchodů a pomůže vám vybrat bez ztráty času. Samostatné desky najdete v kategorii <a href="/snowboardy/">snowboardy</a>, obuv v <a href="/snowboardove-boty/">snowboardových botách</a> a širší přehled v oddílu <a href="/snowboarding/">snowboarding</a>.</p>',
    guide='<h2>Co všechno set obsahuje a co v něm chybí</h2>'
          '<p>Základem je deska a dvě vázání, obvykle už s našroubovanými disky nebo alespoň s potřebným šroubovým materiálem. Některé nabídky přidávají i obal na prkno, imbusový klíč nebo ochranné prvky, ale to se liší obchod od obchodu, proto čtěte popis u konkrétní položky. <strong>Boty se do setu zpravidla nepočítají</strong>, protože velikost chodidla je příliš individuální. Stejně tak si musíte pořídit helmu, brýle, rukavice a teplé oblečení.</p>'
          + T(['Součást', 'Je v setu?', 'Kde ji najít'], [
              ['Snowboard', 'ano', '<a href="/snowboardy/">Snowboardy</a>'],
              ['Vázání', 'ano, obvykle univerzální velikost S–L', '<a href="/snowboardova-vazani/">Snowboardová vázání</a>'],
              ['Boty', 'ne, kupují se zvlášť', '<a href="/snowboardove-boty/">Snowboardové boty</a>'],
              ['Chrániče', 'ne', '<a href="/snowboardove-chranice/">Snowboardové chrániče</a>'],
              ['Helma a brýle', 'ne', '<a href="/lyzarske-helmy/">Helmy</a>, <a href="/lyzarske-bryle/">brýle</a>'],
              ['Oblečení', 'ne', '<a href="/lyzarske-bundy/">Bundy</a>, <a href="/lyzarske-kalhoty/">kalhoty</a>']]) +
          '<h2>Pro koho jsou sety vhodné</h2>'
          '<p>Komplet se vyplatí hlavně třem skupinám. První jsou <strong>úplní začátečníci</strong>, kteří zatím nevědí, jestli je snowboarding bude bavit, a nechtějí řešit slovníček pojmů jako kamber, rocker nebo flex. Druhá skupina jsou <strong>děti a mladiství</strong>, pro které je výhodné koupit levnější sjednocenou výbavu. Třetí jsou <strong>příležitostní jezdci</strong>, kteří vyrazí několik dní v roce a nepotřebují závodní materiál.</p>'
          '<p>Pokročilí jezdci si prkno a vázání obvykle skládají zvlášť. Chtějí konkrétní tvar, tuhost a typ upínání, aby výbava seděla jejich stylu jízdy. Pokud patříte k nim, hledejte v <a href="/snowboardy/">samostatných snowboardech</a> a <a href="/snowboardova-vazani/">vázáních</a>. Set ale nemusí být kompromis ani u zkušeného jezdce, když potřebujete druhou, zálohovou nebo půjčovací sestavu pro hosty.</p>'
          '<h2>Délka prkna podle výšky a váhy</h2>'
          '<p>Správná délka je prvním rozhodnutím. Dlouhé prkno je stabilnější v rychlosti a lépe nese v hlubokém sněhu, kratší se snáz otáčí a odpouští chyby. Pro začátečníky se obvykle doporučuje prkno sahající zhruba mezi bradu a nos, když ho postavíte na špičku vedle sebe. Rozhodující je ale také hmotnost, protože tenký a lehký jezdec při stejné výšce ohne prkno jinak než silnější a těžký.</p>'
          + T(['Situace', 'Doporučení k délce'], [
              ['Začátečník, lehčí postava', 'spíše kratší prkno, snazší zatáčení'],
              ['Vyšší nebo těžší jezdec', 'delší prkno s větší nosností'],
              ['Freestyle, park', 'o něco kratší, hravější'],
              ['Rychlá jízda, freeride', 'delší, stabilní'],
              ['Dítě v růstu', 'nepřeceňujte rezervu, příliš dlouhé prkno se špatně ovládá']]) +
          '<p>Tabulky výrobců uvádějí rozmezí hmotnosti pro každou délku. Zkontrolujte je v popisu nabídky a vyberte takové prkno, jehož rozmezí vaše hodnoty pokrývá. Pokud jste na hranici mezi dvěma velikostmi, bývá pro začátečníka lepší kratší varianta.</p>'
          '<h2>Profil prkna: rocker, kamber a hybrid</h2>'
          '<p>Profil určuje, jak se prkno chová při zatáčení a v prašanu. <strong>Kamber</strong> (klasický prohnutý profil) dává přesný záběr hrany a pružnost, ale vyžaduje čistou techniku. <strong>Rocker</strong> má špičku i patu zvednutou, takže prkno méně zadrhává o hrany a je tolerantní k chybám. Hybridní profily kombinují obojí a jsou nejčastější u tohoto typu sad. Pro začínajícího jezdce je nejpříjemnější rocker nebo hybridní rocker s kamberem pod nohama.</p>'
          '<h2>Flex, tvar a šířka</h2>'
          '<p>Měkké prkno odpouští a je hravější, tvrdé drží stopu a stabilitu v rychlosti. Většina sad míří na střední až měkký flex, protože ten snáší nezkušenost. <strong>Tvar</strong> bývá oboustranný (twin) nebo směrový. Twin se hodí do parku a pro jízdu oběma směry, směrový dává víc stability při jízdě dopředu a v prašanu.</p>'
          '<p>Důležitá je i šířka. Pokud chodidla přesahují hranu prkna, hrozí zachytávání špičky nebo paty při náklonu. U velkých bot (obvykle od vyšších velikostí) proto vybírejte širší model, označovaný jako wide. Naopak úzké prkno je hbitější u menších nohou, ale pokud na něm bota přečuhuje, je to chyba.</p>'
          '<h2>Vázání v setu</h2>'
          '<p>Základní vázání bývají jednoduchá, s popruhy na kotník a přes špičku nebo s rychlým zapínáním pro větší pohodlí. U sad se často dodává univerzální velikost S–M–L podle velikosti boty. Zkontrolujte, zda se na vázání vejde vaše bota včetně zimní ponožky a zda výrobce uvádí rozsah velikostí, který odpovídá vašemu číslu. Nastavitelné prvky (highback, popruhy, délka vázání) vám umožní dolaďovat sezení.</p>'
          '<ul><li><strong>Popruhová vázání:</strong> klasika, spolehlivá a snadno nastavitelná.</li>'
          '<li><strong>Rychlé zapínání:</strong> pohodlnější pro děti a při častém opakovaném obouvání na svahu.</li>'
          '<li><strong>Highback:</strong> opěrka za lýtkem, jejíž sklon a tuhost ovlivňují odezvu prkna.</li>'
          '<li><strong>Univerzální disky:</strong> většina moderních prken má standardní šroubový vzor, ale vždy ověřte kompatibilitu.</li></ul>'
          '<h2>Postoj a nastavení po koupi</h2>'
          '<p>Před první jízdou si zjistěte, zda jste <strong>regular</strong> (levá noha vpředu) nebo <strong>goofy</strong> (pravá vpředu). Jednoduchý test: požádejte někoho, aby vás zlehka postrčil zezadu, a sledujte, kterou nohou se zachytíte. Šířku postoje nastavte přibližně na šířku ramen, úhly vázání pro začátečníka často mírně dopředu na obou nohách, aby se prkno chovalo předvídatelně. Postoj a úhly dolaďujte postupně podle pocitu na svahu.</p>'
          '<h2>Dětské a juniorské sety</h2>'
          '<p>Dětské snowboardy jsou kratší, měkčí a často mají hravé grafiky, ale hlavní je bezpečnost a pohodlí. Vybírejte vázání s jednoduchým zapínáním a prostorem na zimní boty. Značky jako Beany nebo Hatchey nabízejí juniorské komplety právě pro tyto potřeby. Protože děti rostou, vyplatí se zvolit prkno mírně delší než nejkratší možné, ale ne víc než o jednu velikost. Příliš velké prkno dítěti ztíží otáčení a může odradit od dalšího zkoušení.</p>'
          '<p>Doplňte helmu a chrániče zápěstí, případně chrániče páteře a kostrče, které najdete v <a href="/snowboardove-chranice/">snowboardových chráničích</a>. U malých dětí rodiče ocení i <a href="/sane-a-boby/">sáně a boby</a> pro dny, kdy sněhu je dost, ale nálada na svah ne.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíce setů pochází od českých a středoevropských značek Raven a Gravity, doplňují je Hatchey a Beany. Najdete i kusové nabídky Ride, Bataleon nebo Vasa. Raven a Gravity pokrývají nejširší škálu, od úzkých dámských po široké pánské modely, Hatchey zaměřuje na hravé tvary a dětské verze. Hodnoťte ale konkrétní model, ne jen jméno, protože jednotlivé řady se liší profilem i tuhostí.</p>'
          '<h2>Sezónní ročníky</h2>'
          '<p>V názvech se objevují označení ročníku jako 25/26 nebo 26/27. Starší ročník bývá stejný stroj s jinou grafikou, takže pro začátečníka je často rozumná volba. Na technických parametrech záleží víc než na vzhledu, ale ověřte, že se u prodávaného prkna shoduje popis a velikost, a že vázání patří ke stejnému setu.</p>'
          '<h2>Péče, údržba a skladování</h2>'
          '<p>Po jízdě prkno osušte, hlavně hrany, aby nerezavěly. Na konci sezony hrany a skluznici zkontrolujte, nechte je případně přebrousit a navoskovat v servisu. Vosk najdete v kategorii <a href="/lyzarske-vosky/">lyžařské vosky</a>, protože na skluznici funguje stejně. Skladujte na suchém místě, ideálně v obalu, mimo přímé slunce a radiátory. Vázání před uložením uvolněte, aby se popruhy nedeformovaly, a šrouby po první sezoně dotáhněte.</p>'
          '<h2>Co obléknout a vzít s sebou</h2>'
          '<p>Snowboardista tráví hodně času sezením a pády, proto potřebuje voděodolné kalhoty s vyztuženým zadkem a koleny. Pod ně patří <a href="/lyzarske-termopradlo/">termoprádlo</a> a <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, které nesmějí být příliš silné, jinak sevřou nohu. Rukavice ocení každý, kdo se při učení často opírá rukama o sníh, viz <a href="/lyzarske-rukavice/">lyžařské rukavice</a>. Prkno a boty se pohodlně přenášejí v <a href="/lyzarske-vaky-a-tasky/">lyžařských vacích a taškách</a>.</p>'
          '<h2>Časté chyby při nákupu setu</h2>'
          '<ul><li>Výběr podle grafiky bez kontroly délky a rozmezí hmotnosti.</li>'
          '<li>Zapomenuté boty a ochranné vybavení, které se do ceny nepočítají.</li>'
          '<li>Příliš tvrdé prkno pro začátečníka, které stále zakopává o hranu.</li>'
          '<li>Vázání nesedí na velikost boty, takže jezdec nemá kontrolu nad prknem.</li>'
          '<li>Koupě dětského setu s velkou rezervou, v němž dítě nezvládá ovládat prkno.</li>'
          '<li>Opomenutí kontroly, zda je v nabídce prkno i vázání, nebo jen samotná deska.</li></ul>'
          '<h2>Jak srovnávat nabídky na Sportece</h2>'
          '<p>U každého setu porovnejte obsah (jaké vázání, zda je v ceně obal), rozměry a ročník. Stejný set může mít u dvou obchodů odlišnou sestavu, třeba jinou velikost vázání. Prohlédněte si také doručení a vrácení zboží, protože u velkého balíku se může rozhodující stát právě logistika. Pokud váháte mezi dvěma délkami nebo tuhostí, napište obchodu a poraďte se. Širší výběr zimního vybavení najdete v oddílu <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[
        ('Co je snowboardový set?', 'Je to snowboard prodávaný spolu s vázáním, někdy i s dalším příslušenstvím, například obalem. Boty, helma a oblečení se obvykle kupují zvlášť.'),
        ('Je set lepší než samostatné prkno a vázání?', 'Pro začátečníka a dítě většinou ano, protože díly spolu sedí a nemusíte řešit kompatibilitu. Pokročilý jezdec si raději skládá výbavu podle stylu jízdy.'),
        ('Jak vybrat délku prkna?', 'Řiďte se výškou i hmotností a tabulkou výrobce. Pro začátečníka bývá vhodné prkno sahající zhruba mezi bradu a nos, při váhání o velikost kratší varianta.'),
        ('Jaký profil je nejlepší pro začátečníka?', 'Rocker nebo hybridní profil s kamberem pod nohama, protože odpouští chyby a méně zachytává hranou. Čistý kamber vyžaduje zkušenější techniku.'),
        ('Jak poznám, zda jsem regular nebo goofy?', 'Nechte se zlehka postrčit zezadu a sledujte, kterou nohou se zachytíte vpředu. Nebo si představte, kterou nohou byste sklouzli po ledu. Levá noha vpředu znamená regular, pravá goofy.'),
        ('Jsou boty součástí setu?', 'Obvykle ne. Velikost chodidla je příliš individuální, proto je nutné koupit boty zvlášť a ověřit jejich kompatibilitu s vázáním.'),
        ('Hodí se set i pro děti?', 'Ano, dětské a juniorské sety jsou kratší a měkčí a obsahují jednoduše zapínatelná vázání. Vybírejte prkno přiměřené výšce a hmotnosti, ne s velkou rezervou.'),
        ('Můžu vázání ze setu později vyměnit?', 'Ano. Většina prken používá standardní vzor šroubů, takže lze vázání vyměnit. Před nákupem však zkontrolujte kompatibilitu s konkrétním modelem.'),
        ('Jak prkno uložit přes léto?', 'Očistěte a osušte hrany, případně navoskujte skluznici, vázání uvolněte a prkno uložte v obalu na suchém, stinném místě. Nenechávejte ho u radiátoru ani na přímém slunci.'),
        ('Mám se řídit ročníkem 25/26 nebo 26/27?', 'Ročník často mění hlavně grafiku, technické parametry zůstávají podobné. Rozhodující je správná velikost, profil, tuhost a vázání. U staršího ročníku proto nemusíte nic ztratit.'),
        ('Na co si dát pozor v popisu nabídky?', 'Na délku a rozmezí váhy, profil, flex, typ a velikost vázání a také na to, zda nabídka opravdu zahrnuje vázání. Rozdíly mezi obchody se mohou lišit i u stejného modelu.'),
    ])

# ------------------------------------------------------------------ detske-plavky
NEW['detske-plavky'] = dict(long=True,
    title='Dětské plavky: chlapecké, dívčí i kojenecké',
    desc='Dětské plavky na bazén i k vodě: jammery, slipy, boardshorty, jednodílné a dvoudílné, plenkové a neoprenové. Velikost, materiál a péče.',
    intro='<p>Dětské plavky se kupují jinak než dospělé. Dítě rychle roste, v bazénu tráví hodiny a plavky musejí zvládnout chlór, slanou vodu i drhnutí o písek na pláži. Zároveň je to oblečení, které se obléká mokrýma rukama a děti ho chtějí zvládnout samy, takže praktičnost rozhoduje víc než sebelepší střih. V katalogu najdete modely pro miminka, předškoláky, školáky i závodní plavce.</p>'
          '<p>Sporteka sleduje nabídky českých obchodů u značek jako '
          + B(('arena', 'Arena'), ('speedo', 'Speedo'), ('nike', 'Nike'), ('adidas', 'Adidas'), ('splash-about', 'Splash About'), ('finis', 'Finis'), ('funkita', 'Funkita'), ('k-way', 'K-Way'), ('munich', 'Munich')) +
          '. Pro celou rodinu se hodí i <a href="/damske-plavky/">dámské plavky</a> a <a href="/panske-plavky/">pánské plavky</a>, pro vodu pak <a href="/plavecke-bryle/">plavecké brýle</a> a <a href="/plavecke-cepice/">čepice</a>.</p>',
    guide='<h2>Jaké druhy dětských plavek existují</h2>'
          '<p>Nabídka se dělí podle věku, pohlaví a účelu. Rozdíl mezi bazénovými a plážovými plavkami je větší, než se zdá: závodní střihy sedí těsně a minimalizují odpor, plážové jsou volnější a rychle schnou na slunci. Než začnete porovnávat nabídky, rozhodněte, kde bude dítě plavky nejčastěji nosit.</p>'
          + T(['Typ', 'Pro koho', 'Poznámka'], [
              ['Plenkové plavky', 'miminka a batolata', 'těsné gumy na stehnech, plenku zakrývají'],
              ['Slipy a briefs', 'chlapci v bazénu', 'minimální odpor, vyžadují jistotu při pohybu'],
              ['Jammers a aquashorts', 'školáci, tréninkové skupiny', 'delší nohavice, pevný střih, odolné proti chlóru'],
              ['Boardshorty a šortky', 'pláž, rodinné dovolené', 'volný střih, kapsy, rychleschnoucí'],
              ['Jednodílné plavky', 'dívky, trénink i pláž', 'sportovní hřbet nebo klasický střih'],
              ['Dvoudílné plavky', 'dívky na pláž a k bazénu', 'kombinace s topem nebo bikinami'],
              ['UV a lycra oblečení', 'celodenní pobyt na slunci', 'kombinuje se s plavkami'],
              ['Neoprenové oblečení', 'chladnější voda, batolata', 'zahřívá, drží tělesné teplo']]) +
          '<h2>Plavky pro kojence a batolata</h2>'
          '<p>Nejmenší děti nosí zvláštní plavky s elastickými lemy kolem stehen, které zadrží plenku. Do bazénů s veřejným provozem je plenkový model často povinný, protože běžná plenka by se v hladině nasákla. Značka Splash About nabízí kromě klasických plenkových plavek i kojenecké neoprenové kombinézy, které zahřívají a hodí se pro kratší pobyt ve vodě. Vybírejte měkké švy, snadné zapínání a co nejméně detailů, které by dítě mohlo žmoulat.</p>'
          '<p>Při pobytu s miminkem ve vodě nezapomeňte, že malé děti rychle prochladnou. Po vylezení z vody je ihned osušte a zabalte do osušky nebo pláštěnky. Nabídku najdete v kategorii <a href="/plazove-doplnky/">plážové doplňky</a>.</p>'
          '<h2>Chlapecké plavky: slipy, jammery, šortky</h2>'
          '<p>Chlapci mohou nosit nejméně tři střihy. Slipy jsou nejlehčí a nejmenší, ale u starších dětí nejsou vždy pohodlné. Jammers, které sahají k půlce stehen, drží tvar a při tréninku se nezdvihají. Plážové šortky se hodí na běhání po písku a nafukovací atrakce, ale ve vodě nasáknou a zvyšují odpor, takže na plavecký výcvik se nehodí. Dobrý střih má dostatečně vysoký pas, šňůrku nebo pevný vnitřní pás, aby se plavky nezvedaly ani nesjížděly.</p>'
          '<h2>Dívčí plavky: jednodílné, dvoudílné a závodní</h2>'
          '<p>Na plavecký výcvik, školní plavání a kroužky se vyplatí jednodílný model s úzkými ramínky, které neklouzají. Sportovní hřbet (racerback nebo zkřížená ramínka) dává pohybu ramen víc volnosti. Pro dovolenou jsou praktické i dvoudílné plavky nebo jednodílné s volnějším střihem. Modely značek Speedo, Arena, Funkita nebo Nike se vyrábí z odolné textilie vhodné i na pravidelné plavání, módnější linie pak jsou lehčí a barevnější.</p>'
          '<p>Starším dívkám sedí střihy s dobrou oporou v prsní části. Přítomnost vložek či švů si zkontrolujte u konkrétního modelu, vložky musí být lehké a schnout rychle. Pokud se dívka chystá do oddílu, ptejte se trenéra, zda existuje jednotný střih nebo barva.</p>'
          '<h2>Materiály: chlór, UV a elasticita</h2>'
          '<p>Plavky se obvykle vyrábějí z polyamidu nebo polyesteru s elastanem. Polyesterové tkaniny a takzvané chlorine-resistant materiály se s chlórem vyrovnají lépe a drží barvu i tvar, zatímco klasický polyamid s vysokým podílem elastanu je jemnější, ale při dlouhodobém plavání v bazénu se rychleji opotřebuje. Pokud dítě plave dvakrát týdně, upřednostněte plavky označené jako odolné vůči chlóru.</p>'
          '<p>Na slunci je citlivá dětská pokožka. Plavky s UV ochranou nebo lycrové tričko, které najdete v kategorii <a href="/lycra-a-uv-tricka/">lycra a UV trička</a>, významně sníží riziko spálení, ale nenahradí opalovací krém ani pobyt ve stínu. Před letní sezonou zkontrolujte, zda mají plavky stále pružnost a netrpí zeslabenými místy.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Velikostní tabulky se liší podle značky, někdy podle věku, jindy podle výšky nebo obvodu hrudníku. U zahraničních značek se můžete setkat s označením v letech nebo v cm. Plavky mají těsně sedět, ale nesmějí zarývat do kůže ani omezovat dýchání. Pokud je dítě na hranici dvou velikostí, bývá lepší menší velikost pro bazén a větší pro pláž, protože mokrá látka se poněkud natáhne.</p>'
          + T(['Zkouška', 'Co sledovat'], [
              ['Po obléknutí', 'bez záhybů a zarytí do kůže, žádný tlak v podpaží'],
              ['Při dřepu a předklonu', 'plavky se nezvedají ani neodhalují'],
              ['Při zvednutí paží', 'ramínka neklouzají, švy nedřou'],
              ['Po namočení', 'střih drží, materiál není průsvitný']]) +
          '<h2>Co se hodí do bazénu a co k vodě</h2>'
          '<p>Pro plavecké lekce a tréninkové skupiny se vyplatí plavky z kategorie sportovních značek Arena, Speedo nebo Finis. Mívají pevnější střih a lépe drží tvar. K vodě na dovolenou se hodí volnější, hravé plavky, třeba od značek K-Way nebo Gap, které se obléknou rychle a netlačí. Při koupání v moři, v jezeře nebo na skalnatém břehu se vyplatí <a href="/obuv-do-vody/">obuv do vody</a>, aby si dítě neporanilo chodidla.</p>'
          '<p>K plavkám patří i další vybavení. Prohlédněte si <a href="/plavecke-pomucky/">plavecké pomůcky</a>, <a href="/plovaci-vesty/">plovací vesty</a> a <a href="/nafukovaci-hracky/">nafukovací hračky</a>. Pomůcky ale nikdy nenahrazují dohled dospělého a plavecké dovednosti. Zvláště nafukovací doplňky nejsou záchranným prostředkem.</p>'
          '<h2>Školní plavání, kroužky a závodění</h2>'
          '<p>Při školním plavání většinou stačí jednoduché plavky bez zbytečných ozdob a vázání. Pokud dítě začne chodit do oddílu, přidá se čepice, brýle a později i závodní jammery. Plavecké čepice a brýle najdete v kategoriích <a href="/plavecke-cepice/">plavecké čepice</a> a <a href="/plavecke-bryle/">plavecké brýle</a>. U brýlí rozhoduje těsnost kolem očí, ne značka. Trenéři také obvykle doporučují mít dvoje plavky, jedny na trénink a druhé na pláž, aby se tréninkové netrhaly slaností a pískem.</p>'
          '<h2>Pláž, moře a rodinná dovolená</h2>'
          '<p>Na dovolené vydrží dítě ve vodě hodiny. Plavky by měly rychle schnout a nevadí jim písek ani slunce. Vezměte druhé plavky na převléknutí, aby dítě po koupání nezůstalo v mokrých. Mokré plavky dlouho nenechávejte zavěšené na horkém slunci, vyblednou. Vezměte do batohu též lehké tričko, pláštěnku nebo ručník pro případ větru a vyjděte z vody, jakmile se dítěti začnou třást rty.</p>'
          '<h2>Neoprenové plavky a teplé oblečení do vody</h2>'
          '<p>Chladnější voda v přírodním koupališti nebo v bazénu pro nejmenší vede k rychlému prochladnutí. Neoprenové kombinézy a vestičky udržují vrstvu vody u těla a zahřívají. Nejsou to plavky na celý den, ale pomohou při kratším pobytu. Starším dětem se hodí neopreny z kategorie <a href="/neopreny/">neopreny</a> pro vodní sporty, šnorchlování nebo SUP. Zamezte tomu, aby bylo oblečení příliš těsné, a po použití ho opláchněte sladkou vodou.</p>'
          '<h2>Péče o plavky</h2>'
          '<ul><li>Po koupání plavky vždy opláchněte čistou vodou, zbaví se chlóru a soli.</li>'
          '<li>Perte v ruce nebo v pračce na jemný program, bez aviváže a bělidel.</li>'
          '<li>Nesušte na radiátoru, v sušičce ani na přímém slunci.</li>'
          '<li>Nevyždímejte násilně, jen lehce vytlačte vodu.</li>'
          '<li>Neposazujte dítě v plavkách na hrubé povrchy, třeba na betonové okraje, látka se zdrhává.</li>'
          '<li>Ukládejte suché, ne v mokré tašce.</li></ul>'
          '<h2>Jak plavky zvolit před sezonou</h2>'
          '<p>Na jaře vyzkoušejte loňské plavky a zkontrolujte, zda se ještě vejdou, nemají zdrhaná místa a zda guma na nohavicích nepovolila. Děti vyrostou hlavně přes zimu, takže nákup těsně před prázdninami bývá pod časovým tlakem. Kdo plánuje dovolenou v zahraničí, může si prohlédnout nabídku s předstihem, aby zbyl čas na výměnu velikosti.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je koupit příliš velké plavky, aby je dítě nosilo dlouho. Ve vodě se rozšíří, sklouzávají a omezují pohyb. Další omyl je nákup módních plavek na pravidelný trénink, které se po pár týdnech v chlóru zdeformují. Pozor také na štítky a švy, které dráždí, a na plavky, které jsou ve skutečnosti oblečení do vody pro starší děti. Před koupí se ujistěte, zda nabídka obsahuje celé plavky nebo jen jejich část, protože u dívčích dvoudílných modelů se kus někdy prodává zvlášť.</p>'
          '<h2>Pro koho jsou plavky jaké</h2>'
          '<ul><li><strong>Miminko:</strong> plenkové plavky nebo neoprenová kombinéza, osuška a pláštěnka.</li>'
          '<li><strong>Předškolák:</strong> pohodlné plavky snadné k oblékání, UV tričko a obuv do vody.</li>'
          '<li><strong>Školák v plaveckém kurzu:</strong> jammery či sportovní jednodílné plavky odolné chlóru.</li>'
          '<li><strong>Závodník:</strong> specializovaný střih, který ale vybírá trenér podle disciplíny.</li>'
          '<li><strong>Dobrodruh v přírodě:</strong> boardshorty, lycra a vodní boty, případně neopren.</li></ul>'
          '<p>Pokud nakupujete pro více dětí, pomůže nákup stejných značek a velikostních řad, protože se snadno předávají mezi sourozenci. Širší výběr vodních aktivit najdete v kategoriích <a href="/plavky/">plavky</a>, <a href="/vodni-sporty/">vodní sporty</a> a <a href="/bazeny/">bazény</a>.</p>',
    faq=[
        ('Jak poznám správnou velikost dětských plavek?', 'Plavky musejí těsně sedět, aniž by zarývaly do kůže. Orientujte se podle výšky a obvodu hrudníku v tabulce výrobce, protože značky se liší.'),
        ('Z jakého materiálu jsou nejlepší plavky na bazén?', 'Nejodolnější bývají plavky z polyesteru nebo materiálu označeného jako odolný chlóru. Klasický polyamid s elastanem je měkčí, ale při častém plavání se rychleji opotřebuje.'),
        ('Potřebuje miminko speciální plavky?', 'Ano, plenkové plavky mají těsné gumy kolem stehen a zadrží plenku. Řada bazénů je pro nejmenší vyžaduje. Dítě po vodě rychle prochladne, proto mějte po ruce osušku.'),
        ('Jaký je rozdíl mezi jammery a slipy?', 'Jammers jsou delší, sahají zhruba k půlce stehen a drží tvar při tréninku. Slipy jsou nejmenší střih, mají minimální odpor, ale starším dětem často nejsou pohodlné.'),
        ('Hodí se plážové šortky do bazénu?', 'Pro krátké koupání ano, ale na plavecký výcvik nejsou ideální. Ve vodě nasáknou, zvyšují odpor a bývají zbytečně volné.'),
        ('Chrání UV plavky před sluncem úplně?', 'Ne. Snižují expozici, ale nenahrazují opalovací krém ani stín. Dítě by na přímém slunci nemělo být celé hodiny bez přestávky.'),
        ('Jak plavky prát?', 'Opláchněte je po každém koupání čistou vodou a perte jemně v ruce nebo na šetrný program bez aviváže. Nesušte je na radiátoru ani na přímém slunci.'),
        ('Mám koupit větší plavky, aby je dítě nosilo dlouho?', 'Příliš velké plavky ve vodě sklouzávají a omezují pohyb. Je lepší koupit správnou velikost a vyměnit ji, až dítě vyroste.'),
        ('Kolik plavek má dítě mít?', 'Pro pravidelné plavání se hodí dvoje, abyste mohli jedny sušit. Jedny na trénink a druhé na pláž prodlouží životnost obou.'),
        ('Jaké plavky zvolit pro plavecký kurz?', 'Jednoduché, pohodlné, bez zbytečných ozdob a ramínek, která klouzají. Hodí se jednodílné dívčí modely a jammery nebo slipy pro chlapce. Zeptejte se instruktora, zda platí nějaká pravidla.'),
        ('Proč jsou některé plavky jinak označené?', 'Značky používají různé systémy: věk, výšku nebo číselné velikosti. Vždy kontrolujte tabulku u konkrétní nabídky, nespoléhejte na zkušenost z jiné značky.'),
    ])

# ------------------------------------------------------------------ rekreacni-brusle
NEW['rekreacni-brusle'] = dict(long=True,
    title='Rekreační brusle na led: dětské, dámské, pánské',
    desc='Rekreační lední brusle pro kluziště a zamrzlé rybníky: velikost, tuhost, brusle s nastavitelnou velikostí, ostření a péče. Porovnejte obchody.',
    intro='<p>Rekreační brusle na led jsou určené pro volné bruslení na kluzišti, na zamrzlých rybnících a při rodinných výletech. Nepotřebují extrémní tuhost závodních bot ani speciální čepel pro krasobruslení. Jejich úkolem je pohodlí, stabilita kotníku a snadné ovládání, aby i začátečník pochopil bruslení bez bolesti nohou. V nabídce jsou dětské modely, dívčí bílé brusle, pánské i dámské střihy a také kusy pro hokejové amatéry.</p>'
          '<p>Najdete tu značky '
          + B(('fila', 'Fila'), ('bauer', 'Bauer'), ('arcore', 'Arcore'), ('tempish', 'Tempish'), ('roces', 'Roces'), ('k2', 'K2'), ('oxelo', 'Oxelo'), ('insportline', 'Insportline'), ('riedell', 'Riedell'), ('head', 'Head')) +
          '. Pro specializované bruslení pokračujte do kategorie <a href="/hokejove-brusle/">hokejové brusle</a> nebo <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a>. Širší přehled je v oddílu <a href="/brusle/">zimní brusle</a>.</p>',
    guide='<h2>Co znamená rekreační bruslení</h2>'
          '<p>Rekreační brusle slouží lidem, kteří na led vyrazí několikrát za zimu nebo pravidelně na veřejné bruslení. Mají měkčí a pohodlnější botu než sportovní modely a čepel s mírným prohnutím, která usnadňuje otáčení. Nejsou stavěné na tvrdé hokejové zápasy ani na skoky a piruety. Pokud se ale rozhodnete pro pokročilejší styl, v katalogu najdete i specializovanější typy.</p>'
          + T(['Typ brusle', 'Hodí se na', 'Kde hledat'], [
              ['Rekreační lední brusle', 'volné bruslení, zamrzlá voda, rodinné bruslení', 'tato kategorie'],
              ['Dětské s nastavitelnou velikostí', 'rostoucí děti, první zkoušky', 'tato kategorie'],
              ['Dívčí bílé brusle', 'volné bruslení s krasobruslařským vzhledem', 'tato kategorie, <a href="/krasobruslarske-brusle/">krasobruslařské brusle</a>'],
              ['Hokejové brusle', 'hokej, trénink, rychlejší jízda', '<a href="/hokejove-brusle/">hokejové brusle</a>'],
              ['Inline brusle', 'letní trénink na kolečkách', '<a href="/inline-brusle/">inline brusle</a>']]) +
          '<h2>Stavba brusle: bota, čepel, uchycení</h2>'
          '<p>Rekreační lední brusle mají botu z umělé kůže nebo textilu s polstrováním, na spodku plastový nebo kovový držák a ocelovou čepel. Důležitý je kotník: příliš měkká bota se zboří a nedrží nohu, příliš tvrdá bolí. Zkušení bruslaři vybírají střední tuhost, začátečníci spíš pevnější opěru kotníku, protože se s ní učí snadněji udržet rovnováhu.</p>'
          '<ul><li><strong>Boty:</strong> vrstvená konstrukce s polstrovaným jazykem a kotníkem dává noze pohodlnou oporu.</li>'
          '<li><strong>Zapínání:</strong> klasické tkaničky, kombinace tkaniček a přezek, utahovací kolečko nebo systém zapínání na přezky.</li>'
          '<li><strong>Čepel:</strong> ocelová, často s mírným prohnutím a špičkovými zuby u krasobruslařských modelů.</li>'
          '<li><strong>Podšívka:</strong> plyšová nebo fleecová vložka drží teplo i při delším bruslení na mrazu.</li></ul>'
          '<h2>Velikost a sedání</h2>'
          '<p>Rekreační brusle mívají velikosti blízké běžné obuvi, zatímco u hokejových bruslí bývá označení menší než u běžné boty. Pravidlo neplatí pro každou značku, proto nohu změřte a porovnejte ji s tabulkou výrobce. Noha má v brusli sedět pevně, ale bez bolestivého tlaku na palec a bez zdvihání paty. Příliš volná bota způsobí, že kotník kolísá a bruslař ztrácí rovnováhu.</p>'
          + T(['Příznak', 'Co to znamená'], [
              ['Pata se zvedá', 'bota je příliš velká nebo špatně zavázaná'],
              ['Pálení na palci či špičce', 'bota je příliš malá nebo úzká'],
              ['Kotník se kymácí', 'nedostatečná opora nebo volná bota'],
              ['Tlak na nártu', 'tkaničky nebo kolečko příliš utažené'],
              ['Mravenčení v noze', 'příliš těsné zavázání, zastavte a uvolněte']]) +
          '<p>Zkoušejte brusle s ponožkou, kterou na ledě opravdu použijete. Sportovní ponožky najdete v kategorii <a href="/sportovni-ponozky/">sportovní ponožky</a>, bruslařské by měly být tenké a vysoké, aby se nesbalily. Příliš silná ponožka stlačí nohu a ve skutečnosti ji zchladí.</p>'
          '<h2>Dětské brusle s nastavitelnou velikostí</h2>'
          '<p>Dětské brusle s rozsunovací botou pokryjí několik velikostí a vydrží i dvě sezony. Hodí se pro děti, které bruslí jen občas. Nevýhodou je mírně vyšší hmotnost a méně přesné držení nohy než u pevné boty. Pokud dítě začíná chodit na pravidelné lekce, vyplatí se pevná bota s dobrým kotníkem, kterou dítě lépe ovládá.</p>'
          '<p>Vyzkoušejte, zda dítě umí brusli samo obout a zapnout, nebo zda potřebujete pomoc. Utahovací kolečko a přezky šetří čas na kluzišti. Nezapomeňte na helmu, chrániče zápěstí a lokty, které najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>. První kroky na ledě jsou plné pádů, takže ochrana se vyplatí.</p>'
          '<p>Tempish a Arcore jsou častým výběrem pro děti, protože mají jednoduché zapínání a pestré barvy. Pro menší děti se hodí také pomůcky, které pomohou udržet rovnováhu, například stabilizační podpěra či opora u mantinelu. Nenuťte dítě k dlouhému bruslení, krátké a časté návštěvy kluziště jsou pro začátek příjemnější.</p>'
          '<h2>Dámské a pánské střihy</h2>'
          '<p>Dámské brusle bývají užší v patě a mají nižší kotník, pánské širší a objemnější. Unisex modely se prodávají jako univerzální řešení, ale někomu nemusí sedět. Pokud máte úzkou nohu, sáhněte po dámském nebo dívčím modelu, pokud širší, zvolte pánský nebo širší dětský. Pánské brusle Bauer, Fila nebo Head jsou častou volbou pro dospělé, dámské modely najdete u Fila, Roces či Riedell.</p>'
          '<h2>Brusle pro dospělé začátečníky</h2>'
          '<p>Dospělý začátečník by neměl šetřit na pevnosti kotníku. Měkká bota ho nutí přenášet váhu na vnitřní hranu a bolestně namáhá kotníky. Pevnější rekreační model, s kombinací tkaniček a přezek, vám dá oporu a rychle pocítíte pokrok. Doporučuje se začít na vyhrazeném veřejném bruslení, kde je klidnější led, a pomalu se zlepšovat. Pomoci mohou i první lekce s trenérem.</p>'
          '<h2>Brusle s tkaničkami, přezkami a utahovacím kolečkem</h2>'
          + T(['Zapínání', 'Výhody', 'Nevýhody'], [
              ['Tkaničky', 'přesné dotažení po celé délce', 'pomalejší, vyžadují cvik'],
              ['Přezky', 'rychlé, spolehlivé', 'méně přesné nastavení'],
              ['Kombinace', 'tkaničky dole, přezky nahoře', 'vyšší hmotnost'],
              ['Utahovací kolečko', 'rychlé dotažení jednou rukou', 'méně intuitivní údržba']]) +
          '<p>Tkaničky vyžadují trochu praxe, ale dovolují zvlášť pevně utáhnout kotník a volněji nárt. Přezky jsou pohodlné pro děti a rekreanty, kteří bruslí krátce. Utahovací kolečko se hodí tam, kde se chcete co nejrychleji obout a vydržet bez dotahování.</p>'
          '<h2>Brusle na zamrzlý rybník a přírodní led</h2>'
          '<p>Na přírodním ledě se setkáte s nerovnostmi a prasklinami. Hodí se robustnější bota a čepel, která snese drsnější povrch. Před vstupem vždy ověřte, zda je led dostatečně silný a bezpečný, případně se zeptejte místních správců. Bruslete nejlépe ve skupině, mějte po ruce suché oblečení a nikdy nechoďte na led sami. Nezapomeňte na zimní oblečení z kategorií <a href="/funkcni-mikiny/">funkční mikiny</a> a <a href="/teplaky/">tepláky</a>.</p>'
          '<h2>Brankářské a hokejové kusy v kategorii</h2>'
          '<p>V nabídce se objevují i brankářské brusle, hokejové modely značek Bauer, Winnwell a jiných výrobců, které jsou součástí širšího výběru ledních bruslí. Pro běžné bruslení nejsou ideální, protože mají tvrdší botu, jinou geometrii čepele a jsou určené pro hokejový styl. Pokud hledáte takové brusle pro hokej, použijte raději kategorii <a href="/hokejove-brusle/">hokejové brusle</a> a navazující <a href="/hokejove-brankarske-vybaveni/">brankářské vybavení</a>. Komplet ochranných pomůcek najdete v <a href="/hokejove-chranice/">hokejových chráničích</a> a <a href="/hokejove-helmy-a-mrizky/">helmách a mřížkách</a>.</p>'
          '<h2>Ostření čepelí a péče o brusle</h2>'
          '<p>Čepel se musí čas od času nabrousit, jinak brusle klouže a špatně zabírá. Frekvence závisí na tom, jak často bruslíte a na jakém ledě. Ostření nechte na odborníkovi, špatně nabroušená čepel zhorší ovládání víc než tupá. Po bruslení otřete čepel suchým hadrem a nasaďte chrániče čepelí, které najdete v kategorii <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>. Na led vstupujte vždy bez chráničů čepelí a po betonu či trávě naopak nikdy nechoďte bez nich.</p>'
          '<ul><li>Po použití sundejte brusle, vytáhněte vložky a nechte je vyschnout.</li>'
          '<li>Neskladujte v uzavřeném sáčku, vzniká rez.</li>'
          '<li>Boty čistěte vlhkým hadrem, neperte je v pračce.</li>'
          '<li>Tkaničky vyměňte, jakmile se začnou drolit.</li>'
          '<li>Čepele kontrolujte kvůli rzi a poškození zubů.</li></ul>'
          '<h2>Oblečení a ochrana na kluziště</h2>'
          '<p>Na kluziště se obléká po vrstvách. Funkční triko, lehká mikina a bunda umožní regulovat teplotu, protože při pohybu se zahřejete. Hodí se rukavice a čepice, které najdete v kategoriích <a href="/sportovni-rukavice/">sportovní rukavice</a> a <a href="/cepice-a-celenky/">čepice a čelenky</a>. Začátečníci by měli mít helmu, ideálně i chrániče zápěstí. Při dětském bruslení je helma samozřejmost a pro dospělé se silně doporučuje. Po pádech pomohou <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>'
          '<h2>První návštěva kluziště</h2>'
          '<p>Přijďte s předstihem, aby zbyl čas na obouvání bez spěchu. Brusli zavažte pevněji kolem kotníku, nárt nechte o něco volnější a před vstupem na led se několikrát projděte po gumové podlaze. Vezměte si teplé rukavice, které chrání ruce při pádu, a nechte si doma šály a dlouhé volné části oblečení, které se mohou zachytit. Na led vyrazte nejdřív bokem k mantinelu a zvykejte si na klouzání.</p>'
          '<h2>Jak se naučit bruslit</h2>'
          '<p>Začněte v lehkém předklonu, s pokrčenými koleny a rukama před tělem. Učte se jízdu rovně, brzdění a pád, teprve potom zatáčky a couvání. Pády jsou součástí učení a nejlepší je naučit se padat dopředu na ochrany kolen a rukou. Většina začátečníků se zlepší už za několik návštěv. Nebojte se zeptat trenéra nebo zkušeného bruslaře, krátká rada ušetří týdny trápení.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Příliš velká bota, v níž noha plave a kotník kolísá.</li>'
          '<li>Příliš měkká bota pro dospělého začátečníka.</li>'
          '<li>Ostré hokejové brusle pro dítě, které chce jen volně bruslit.</li>'
          '<li>Nákup bez kontroly tabulky velikostí značky.</li>'
          '<li>Opomenutí kontroly zapínání, které dítě nezvládne samo.</li>'
          '<li>Nechráněná čepel při přenášení nebo skladování.</li></ul>'
          '<h2>Jak srovnávat nabídky</h2>'
          '<p>Na Sportece porovnáte více obchodů u jednoho modelu. Všímejte si dostupných velikostí, protože velká část nabídek se rozprodá a zůstane jen několik čísel. Zkontrolujte, zda je v nabídce uvedeno zapínání, materiál a zda se brusle prodávají samostatně nebo se sadou chráničů. Pokud se hodláte věnovat bruslení pravidelně, rozšiřte nabídku o <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>, které můžete používat i v létě, nebo se podívejte do oddílu <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi rekreačními a hokejovými bruslemi?', 'Rekreační mají měkčí a pohodlnější botu a čepel pro volné bruslení. Hokejové jsou tužší, mají jinou geometrii čepele a jsou určené pro rychlejší a ostřejší jízdu.'),
        ('Jak vybrat velikost ledních bruslí?', 'Změřte nohu a porovnejte ji s tabulkou výrobce. U hokejových bruslí bývá označení menší než u běžné obuvi, u rekreačních blízké běžné obuvi, ale u každé značky se liší.'),
        ('Jsou brusle s nastavitelnou velikostí vhodné pro děti?', 'Pro občasné bruslení ano, vydrží několik velikostí. Pro pravidelné lekce je lepší pevná bota, která drží nohu přesněji.'),
        ('Co je lepší, tkaničky nebo přezky?', 'Tkaničky dovolují přesné dotažení, přezky jsou rychlejší a pohodlnější. Mnoho rekreačních modelů kombinuje obojí.'),
        ('Jak často se mají brusle ostřit?', 'Záleží na četnosti bruslení a typu ledu. Ostření nechte provést odborníkem. Tupá čepel brusli nechá bočně klouzat a ztrácí záběr, takže jezdec méně ovládá směr.'),
        ('Mám při bruslení nosit helmu?', 'U dětí doporučujeme jednoznačně, u začátečníků všech věků také. Pády na ledě mohou být nečekané a tvrdé.'),
        ('Mohu na přírodním ledě bruslit v rekreačních bruslích?', 'Ano, ale led musí být dostatečně silný a bezpečný. Počítejte s nerovnostmi a nikdy nechoďte na led sami.'),
        ('Hodí se dámské brusle i pro dívky?', 'Ano, dívčí modely bývají užší v patě a nižší na kotníku. Rozhodující je ale sedění na konkrétní noze.'),
        ('Proč se objevují v kategorii i brankářské brusle?', 'Nabídky obchodů se řadí podle typu zboží. Brankářské brusle jsou určené pro hokej, proto pro volné bruslení vybírejte rekreační model.'),
        ('Jak brusle skladovat?', 'Po použití osušte čepele i botu, vyjměte vložky a nenechte je v uzavřeném sáčku. Čepele zakryjte chrániči jen při přenášení, ne při dlouhodobém skladování.'),
        ('Mohu rekreační brusle používat celou zimu?', 'Ano, při pravidelné péči vydrží několik sezon. Hlídejte stav čepele, tkaniček a podšívky a vždy je dobře vysušte.'),
    ])

# ------------------------------------------------------------------ golfove-obleceni-a-obuv
NEW['golfove-obleceni-a-obuv'] = dict(long=True,
    title='Golfové oblečení a obuv: polo, kalhoty, boty',
    desc='Golfové polo, kalhoty, sukně, vesty, rukavice, kšiltovky a golfové boty. Dress code, materiály, sezóna, velikost a péče. Porovnejte nabídky obchodů.',
    intro='<p>Golfové oblečení a obuv jsou víc než módní doplněk. Hřiště mají dress code, kolo trvá několik hodin a počasí se mění během jediné hry. Oděv musí dovolit plný švih, odvádět pot a zároveň vypadat upraveně. Obuv zase stabilizuje postoj při úderu a drží na mokré trávě. V kategorii najdete pánské i dámské polokošile, kalhoty, sukně, vesty, čepice, rukavice a golfové boty.</p>'
          '<p>Největší zastoupení mají značky '
          + B(('under-armour', 'Under Armour'), ('adidas', 'Adidas'), ('inesis', 'Inesis'), ('footjoy', 'Footjoy'), ('new-balance', 'New Balance'), ('gregnorman', 'Gregnorman'), ('puma', 'Puma'), ('ecco', 'Ecco'), ('skechers', 'Skechers')) +
          '. Vybavení pro hru najdete v kategoriích <a href="/golfove-hole/">golfové hole</a>, <a href="/golfove-micky/">golfové míčky</a> a <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a>, drobnosti v <a href="/golfove-doplnky/">golfových doplňcích</a>.</p>',
    guide='<h2>Co všechno kategorie obsahuje</h2>'
          '<p>Kategorie je širší, než by název naznačoval. Vedle klasických polokošil a kalhot jsou tu golfové rukavice pro praváky a leváky, kšiltovky, pletené vesty, sukně se šortkami pod sebou a samozřejmě golfová obuv s hroty i bez nich. Hlavním rozdílem proti běžnému sportovnímu oblečení jsou střihy, které nebrání rotaci trupu, a pevnější boty s přilnavou podešví.</p>'
          + T(['Kus', 'Na co se hodí', 'Na co dát pozor'], [
              ['Golfové polo', 'základ pro hřiště, s límečkem', 'pružnost v ramenou, rychlé schnutí'],
              ['Kalhoty', 'celoroční hra, chladnější dny', 'střih v pase, pružná látka'],
              ['Šortky a sukně', 'léto, dámský dress code', 'délka podle pravidel klubu'],
              ['Vesta nebo svetr', 'přechodné počasí', 'volnost při švihu'],
              ['Rukavice', 'sevření hole, ochrana dlaně', 'levák nebo pravák, velikost'],
              ['Čepice a kšiltovka', 'ochrana před sluncem', 'vzdušnost, nastavitelnost'],
              ['Golfové boty', 'stabilita a přilnavost', 'hroty, voděodolnost, velikost']]) +
          '<h2>Dress code na hřištích</h2>'
          '<p>Většina klubů vyžaduje límečkové tričko nebo polo, kalhoty či šortky vhodné délky a boty bez ostrých kovových hrotů. Džíny, tílka a běžecké šortky často nejsou povoleny. Pravidla se liší podle hřiště, proto před první hrou zjistěte konkrétní požadavky klubu. Dámská polo bez límečku a sukně se mohou na některých hřištích objevit, jinde ne, a rozhodují vedle vzhledu i délka a střih.</p>'
          '<h2>Polokošile: střih, materiál, rukávy</h2>'
          '<p>Golfové polo má být pružné v ramenou a boční šev nesmí tlačit při rotaci. Materiál bývá polyester s elastanem, který odvádí pot a rychle schne. Bavlněné polo je příjemné, ale při potu se lepí a pomalu schne. U dlouhých her v horku se hodí lehká síťovaná struktura. Užitečné jsou i modely s UV ochranou, pokud trávíte hodiny na slunci. Obecný přehled polokošil najdete v kategorii <a href="/polokosile/">polokošile</a>.</p>'
          '<h2>Kalhoty, šortky a sukně</h2>'
          '<p>Golfové kalhoty mají pružnou látku a střih kolem stehen, který nebrání švihu. Rovné nohavice jsou klasika, zúžené (tapered) modely vypadají moderněji a při chůzi se méně zachytávají. Dámské sukně se šortkami pod sebou, známé jako skorty, nabízejí volnost a pohodlí. Do chladnějších dnů se hodí teplejší látky nebo kalhoty s vlnou. Širší nabídku najdete v kategoriích <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, <a href="/sportovni-kratasy/">sportovní kraťasy</a> a <a href="/sportovni-sukne-a-saty/">sukně a šaty</a>.</p>'
          + T(['Počasí', 'Doporučené vrstvy'], [
              ['Teplo a slunce', 'lehké polo, šortky či sukně, kšiltovka, UV ochrana'],
              ['Mírné jaro či podzim', 'polo, vesta nebo lehká mikina, dlouhé kalhoty'],
              ['Chladné dny', 'funkční triko pod polo, vesta, čepice, rukavice'],
              ['Déšť a vítr', 'nepromokavá bunda, kalhoty a voděodolné boty']]) +
          '<h2>Vesty, mikiny a svetry</h2>'
          '<p>Při hře je důležitá volnost paží. Vesta nechává ramena volná a zahřeje trup, proto je mezi golfisty tak oblíbená. Pletená vesta s výstřihem do V nebo zip-vesta je typickým vrstvením. Lehčí mikiny a svetry zvolte s pružným materiálem, aby se při švihu netahaly. Další inspiraci hledejte v kategoriích <a href="/sportovni-vesty/">sportovní vesty</a>, <a href="/mikiny/">mikiny</a> a <a href="/vetrovky/">větrovky</a>.</p>'
          '<h2>Golfové rukavice</h2>'
          '<p>Golfisté nosí rukavici obvykle jen na jedné ruce, na vedoucí. Pravák nosí rukavici na levé ruce, levák na pravé, a proto se nabízejí rozlišené modely. Rukavice zlepšuje sevření a snižuje riziko puchýřů. Vybírejte podle velikosti dlaně, měla by sedět těsně, ale bez záhybů. Kožené modely dávají lepší cit, syntetické vydrží déle a hůř nasáknou. Existují i varianty pro déšť a pro hru v chladu.</p>'
          '<h2>Golfová obuv: hroty a bez hrotů</h2>'
          '<p>Golfová bota musí držet nohu při úderu. Na rozdíl od tenisek má širší podešev, často s plastovými hroty nebo výčnělky, které se zabodnou do trávy. Moderní modely bez klasických hrotů se podobají sportovní obuvi a dají se nosit i mimo hřiště. Hrotové boty drží lépe na mokré trávě a svazích, ale na tvrdém povrchu hůř chodí.</p>'
          '<ul><li><strong>Hroty (výměnné):</strong> lepší přilnavost, ovšem hluk a opotřebení při chůzi po tvrdém povrchu.</li>'
          '<li><strong>Bez hrotů (spikeless):</strong> pohodlnější, univerzální, vhodné i pro rekreační hráče.</li>'
          '<li><strong>Voděodolná bota:</strong> membrána nebo kožený svršek, vhodná pro deštivé dny.</li>'
          '<li><strong>Letní lehká bota:</strong> prodyšný textil, rychleji schne.</li></ul>'
          '<p>Značky Footjoy, Ecco, New Balance, Adidas nebo Skechers nabízejí modely pro muže, ženy i juniory. Ecco se zaměřuje na kožené modely, New Balance na pohodlnou podešev. Před nákupem zkontrolujte typ hrotů (pokud jsou výměnné) a velikostní tabulku. Základní sportovní boty najdete také v <a href="/sportovni-obuv/">sportovní obuvi</a>.</p>'
          '<h2>Velikost a sedání bot</h2>'
          '<p>Golfová bota by měla pevně držet patu a dopřát prstům trochu místa. Během hry ujdete kilometry, proto zkoušejte boty odpoledne, kdy je noha mírně oteklá, a s ponožkami, které opravdu použijete. Příliš těsná bota bolí, příliš volná způsobí puchýře a ztrátu stability. Dobrou oporu poskytují vložky, které najdete v kategorii <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>. Ponožky vybírejte tenké, prodyšné, z kategorie <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>'
          '<h2>Počasí a vrstvení</h2>'
          '<p>Kolo trvá několik hodin, takže teplota se mění. Základem je vrstvení: funkční triko, polo, vesta a lehká nepromokavá bunda v tašce. Zvolte pružné materiály, které se při švihu nezadrhávají a nešustí. Bundy pro nepříznivé počasí najdete v kategorii <a href="/nepromokave-bundy/">nepromokavé bundy</a>. Pro chladné dny pomohou i <a href="/funkcni-tricka/">funkční trička</a> pod polo.</p>'
          '<h2>Dámské a pánské střihy</h2>'
          '<p>Dámské střihy mají jiné proporce pasu a boků, často kratší vnitřní délku a užší stehna. Pánské jsou širší v ramenou a delší. Unisex modely se vyskytují hlavně u čepic a rukavic. Při výběru kalhot či sukní sledujte, jak se střih chová při rotaci trupu. Zkuste švih naprázdno, kalhoty nesmějí tahat v rozkroku ani tlačit v pase.</p>'
          '<h2>Co zabalit do tašky na hřiště</h2>'
          '<p>Kromě vlastního oblečení se vyplatí mít v tašce náhradní rukavici, suché ponožky, lehkou nepromokavou bundu, čepici a ručník. Pokud hrajete celé kolo, připravte si i svačinu a láhev s pitím. Čistá náhradní polokošile se hodí po hře v horku, když se chcete převléknout před návštěvou klubovny. Tašky a vozíky najdete v kategorii <a href="/golfove-tasky-a-voziky/">golfové tašky a vozíky</a>.</p>'
          '<h2>Juniorské vybavení</h2>'
          '<p>Děti rostou rychle, takže se vyplatí volit základní kousky v praktických barvách. Junioři potřebují hlavně pohodlná polo, kalhoty a boty s dobrou přilnavostí. Rukavice nejsou nutné, ale pomáhají, pokud mají děti sklon k puchýřům. Dětské vybavení se hodí i na minigolf a podobné rodinné hry.</p>'
          '<h2>Značky a jejich profil</h2>'
          '<p>Under Armour je zastoupen nejvíc, převažují technické materiály a střihy pro aktivní hráče. Adidas a Puma dávají důraz na kombinaci s lifestylem, Inesis je jednoduchá praktická volba pro začátečníky, Footjoy a Ecco jsou spojeny s botami a rukavicemi, Gregnorman a Siroko nabízejí módnější střihy. Cobra zastupuje výrobce, který je jinak znám jako výrobce holí. Konkrétní vlastnosti ale vždy posuzujte u daného kusu.</p>'
          '<h2>Péče o golfové oblečení a boty</h2>'
          '<ul><li>Technické materiály perte na šetrný program, bez aviváže, ta ucpává vlákna a zhoršuje odvod potu.</li>'
          '<li>Boty po hře očistěte od trávy a bláta, vlhké boty nechte přirozeně vyschnout.</li>'
          '<li>Do bot vložte papír nebo vložky pohlcující vlhkost.</li>'
          '<li>Kožené boty ošetřujte krémem nebo impregnací, aby nepromokaly.</li>'
          '<li>Rukavice po hře rozložte, aby uschla bez smrštění.</li>'
          '<li>Hroty kontrolujte a vyměňujte opotřebované.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<p>Nejčastější chybou je nákup oblečení bez ohledu na dress code. Druhou jsou příliš těsné kalhoty nebo polo, které brání švihu. U bot lidé podceňují důležitost přilnavosti a stability a berou běžné tenisky, na vlhké trávě pak ztrácejí oporu. Často se zapomíná na rukavici a čepici, které na slunci pomohou víc, než by se zdálo. Pozor také na rozdíl mezi dámskou a pánskou verzí rukavice a na správnou ruku.</p>'
          '<h2>Jak srovnávat nabídky na Sportece</h2>'
          '<p>Porovnejte dostupné velikosti a barvy ve více obchodech, protože jednotlivé kusy bývají vyprodané. Zkontrolujte, zda je u bot uvedena šíře a typ podešve, u oblečení materiál a střih. Začínající hráči si mohou vybrat základní sadu: dvě polokošile, kalhoty, boty a rukavici, a postupně přidávat. Pro koupi prvních holí navštivte <a href="/golfove-hole/">golfové hole</a>, a pokud vás zajímá volnější a levnější varianta, podívejte se na <a href="/discgolf/">discgolf</a>. Přehled oboru najdete v oddílu <a href="/golf/">golf</a>.</p>',
    faq=[
        ('Jaký je dress code na golfovém hřišti?', 'Většina klubů vyžaduje límečkové polo, kalhoty či šortky vhodné délky a golfovou obuv bez ostrých kovových hrotů. Přesná pravidla se liší, takže si je před hrou ověřte u konkrétního hřiště.'),
        ('Musím mít speciální golfové boty?', 'Doporučují se, protože drží stabilitu při švihu a mají přilnavou podešev. Na mnoha hřištích jsou ostré kovové hroty zakázané a zakázané jsou i boty, které poškozují greeny.'),
        ('Jaký je rozdíl mezi botami s hroty a bez hrotů?', 'Hrotové boty se lépe drží na mokré trávě a svazích, ale hůř se chodí po tvrdém povrchu. Boty bez hrotů jsou pohodlnější a hodí se i mimo hřiště.'),
        ('Na kterou ruku se nosí golfová rukavice?', 'Obvykle na vedoucí ruku. Pravák nosí rukavici na levé, levák na pravé ruce. Proto se prodávají zvlášť pro praváky a leváky.'),
        ('Z jakého materiálu má být golfové polo?', 'Praktický je polyester s elastanem, který odvádí pot a schne. Bavlna je příjemná, ale při potu se lepí a schne pomaleji.'),
        ('Hodí se do golfu běžné sportovní kalhoty?', 'Pokud jsou pružné a střihem nebrání rotaci, mohou posloužit. Některé kluby ale vyžadují klasický golfový střih, a tak se vyplatí kalhoty vybírat s ohledem na dress code.'),
        ('Co si obléknout při dešti?', 'Nepromokavou bundu a případně kalhoty, nejlépe lehké a bezhlučné, aby nebránily švihu. Rukavice na déšť a voděodolné boty zlepší komfort.'),
        ('Jak pečovat o golfové boty?', 'Po hře je očistěte, nechte přirozeně vyschnout a kožené modely ošetřujte impregnací. Kontrolujte opotřebení hrotů a podrážky.'),
        ('Jakou velikost bot zvolit?', 'Takovou, která pevně drží patu a ponechá prstům trochu místa. Zkoušejte je s ponožkami, které budete nosit, a odpoledne, kdy je noha mírně oteklá.'),
        ('Potřebují děti speciální golfové oblečení?', 'Není nutné, ale polo, pohodlné kalhoty a boty s přilnavou podešví pomáhají. Děti rostou, proto stačí základní výbava.'),
        ('Je oblečení Under Armour a Adidas vhodné pro začátečníky?', 'Ano, nabízejí technické materiály i střihy pro každý typ hráče. Začátečníkovi ale stačí základní kousky, na nejdražší modely není důvod spěchat.'),
    ])
