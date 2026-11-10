"""sporteka.cz — facet landing texts wave 129: fischer-hokejka, jurek-stany, panske-plavky-arena, damske-lyzarske-bryle.
General true facts only, no prices or counts. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ fischer-hokejka
NEW['fischer-hokejka'] = dict(
    title='Fischer hokejka: řady W a RC One, velikosti a flex',
    desc='Hokejky Fischer od dřevěných W po kompozitní RC One. Jak číst označení Kid, YTH, JR, INT a SR, zvolit flex, délku a zahnutí a porovnat nabídky obchodů.',
    intro='<p>Hokejky Fischer jsou hlavně dětská a juniorská volba: v nabídce převažují modely pro nejmenší hráče, žáky a dorost a teprve za nimi následují hole pro dospělé. Značka rozlišuje levné dřevěné řady W a kompozitní řady RC One, XPRO a CT950, a právě orientace v těchto názvech bývá největší překážkou při nákupu. '
          'Tato stránka vybírá z kategorie <a href="/hokejky/">hokejky</a> jen modely značky Fischer. Průvodce vysvětluje, co znamenají zkratky Kid, YTH, JR, INT a SR, jak spolu souvisí flex a délka, kdy se vyplatí dřevo a kdy kompozit a jak se Fischer liší od jiných značek, například <a href="/bauer-hokejky/">Bauer</a>, <a href="/ccm-hokejky/">CCM</a> nebo <a href="/hokejka-warrior/">Warrior</a>. Dítěti se hodí i přehled <a href="/detska-hokejka/">dětských hokejek</a>.</p>',
    guide='<h2>Jak je sortiment Fischer uspořádán</h2>'
          '<p>Fischer je rakouská značka, kterou většina lidí zná z lyžování, a hokejový sortiment staví na podobném principu jako lyže: jedna základní řada pro vstup do sportu a výše postavené řady pro ty, kdo hrají soutěžně. Názvy modelů se skládají z písmene řady a čísla, takže stačí pochopit logiku několika značení.</p>'
          + T(['Řada', 'Materiál', 'Pro koho'], [
              ['W150, W250, W350', 'dřevo', 'začátečníci, školní hokej, hra venku i na ledě'],
              ['RC One IS1', 'kompozit', 'děti a junioři, kteří trénují pravidelně'],
              ['RC One XPRO a XPRO2', 'kompozit vyšší třídy', 'soutěžní hráči, kteří chtějí nižší váhu a citlivější odpich'],
              ['RC One ULTRA2', 'kompozit nejvyšší třídy v nabídce značky', 'dospělí a dorostenci, pro které je důležitý každý gram'],
              ['CT950', 'kompozit s úpravou povrchu Grip', 'dospělí a dorost, kteří hrají pravidelně a nechtějí nejdražší hůl']]) +
          '<p>Rozdíl mezi dřevěnými a kompozitními řadami je nejvýraznější v hmotnosti a v tom, jak se hůl chová při střele. Dřevo je těžší a méně pružné, ale odpustí nárazy do mantinelu a brány. Kompozit je lehčí, ukládá při ohybu energii a vrací ji do puku, ale po tvrdém úderu může prasknout. U dětí, které hůl teprve zkoušejí, je dřevo racionální, u hráčů v lize už dává smysl kompozit.</p>'
          '<h2>Co znamenají zkratky velikostí</h2>'
          '<p>Hokejové hole se dělí do velikostních skupin podle věku a postavy hráče. Fischer používá označení, které je ve světě běžné, takže se s ním potkáte i u jiných výrobců.</p>'
          + T(['Označení', 'Význam', 'Poznámka'], [
              ['Mini a Kid', 'nejmenší děti, první kroky na ledě', 'krátká a lehká hůl, flex se neřeší nebo je minimální'],
              ['YTH (Youth)', 'mladší školáci', 'číslo za zkratkou je flex, třeba YTH 20 nebo YTH 35'],
              ['JR (Junior)', 'starší žáci', 'střední délka, flex zhruba čtyřicet'],
              ['INT (Intermediate)', 'dorostenci a menší dospělí', 'přechod mezi juniorem a seniorem, flex vyšší'],
              ['SR (Senior)', 'dospělí', 'nejdelší hole s nejvyšším flexem']]) +
          '<p>Pokud dítě stojí na rozhraní dvou velikostí, rozhodujte podle výšky a síly. Příliš dlouhá hůl se špatně ovládá a nutí hráče k hrbení, zatímco o něco kratší hůl je pro mladšího hráče zpravidla bezpečnější volba. U INT a SR modelů značka v názvu často uvádí i číslo flexu nebo délku.</p>'
          '<h2>Flex, délka a ořezávání</h2>'
          '<p>Flex je číslo, které říká, jakou silou je potřeba hůl prohnout. Čím je menší, tím je hůl měkčí. Orientační pravidlo říká, že hodnota flexu odpovídá zhruba polovině hmotnosti hráče v librách, takže lehké dítě potřebuje velmi měkkou hůl, kterou si ohne vlastní vahou. Příliš tuhá hokejka dítěti brání v nácviku střely, protože se vůbec neprohýbá a puk letí slabě a nejistě.</p>'
          '<ul><li><strong>Délka:</strong> hůl postavená na špičce čepele sahá hráči na bruslích přibližně mezi bradu a nos.</li>'
          '<li><strong>Zkrácení:</strong> kompozitní i dřevěnou hůl lze ořezat, hůl se tím ale zpevní, protože kratší tyč se ohýbá hůře.</li>'
          '<li><strong>Prodloužení:</strong> u dřevěných holí existují násady na nasazení, u kompozitu se prodlužuje obtížněji.</li>'
          '<li><strong>Styl hry:</strong> kdo střílí od modré čáry, snese delší hůl, kdo kličkuje, ocení kratší.</li></ul>'
          '<p>Při ořezu počítejte s tím, že se mění i odezva hole. Pokud hůl sdílí více dětí v kroužku, zvolte raději dřevěnou, která vydrží i hrubší zacházení.</p>'
          '<h2>Levá nebo pravá, zahnutí čepele</h2>'
          '<p>Každá hokejka je vyrobena pro hráče, který drží hůl levou nebo pravou rukou dole. V nabídkách je označena L nebo R, případně P a L. Rozhodnutí je jednoduché: představte si, jak držíte koště nebo golfovou hůl. Ruka, která je níž, určuje stranu. Většina hráčů v Česku střílí levou rukou dole, ale dítě bez zkušeností necháme vyzkoušet obě varianty v obchodě nebo doma s tenisovým míčkem.</p>'
          '<p>Zahnutí čepele, anglicky pattern, se označuje například P28 nebo PP26, a jde o tvar a otevření čepele. Otevřenější čepel usnadňuje zvedání puku, rovnější je přesnější při přihrávce. U dětských holí se většinou nabízí jedno univerzální zahnutí a o volbě nemusíte přemýšlet. Až u INT a SR modelů se vyplatí zkoumat, jaký vzor vyhovuje vašemu stylu.</p>'
          '<h2>Grip a povrch</h2>'
          '<p>Označení Grip v názvu znamená, že rukojeť má matný nebo strukturovaný povrch, který zlepšuje sevření rukavic, zvlášť při zpocených dlaních. Hladká hůl je rychlejší při posunu ruky po násadě, ale klouže. Mnoho hráčů si tak i tak omotá rukojeť páskou. Pokud ji chcete obnovit, sáhněte po pásce z kategorie <a href="/hokejove-pasky-a-doplnky/">hokejové pásky a doplňky</a>, kde najdete také vosk a vyměnitelné knoflíky.</p>'
          '<h2>Fischer a ostatní značky</h2>'
          '<p>Na trhu s hokejkami dominují Bauer a CCM, hodně se hraje také s modely Winnwell, Warrior nebo Sherwood. Fischer v tomto rozložení hraje roli solidní střední cesty, protože míří hlavně na mládež a rekreační hráče, ne na profesionály. Pro dospělé pokročilé je často zajímavější širší výběr u hlavních značek, pro dítě na začátku se však dobře hodí právě jednoduchá řada W.</p>'
          + B(('bauer', 'Bauer'), ('ccm', 'CCM'), ('winnwell', 'Winnwell'), ('warrior', 'Warrior')) +
          '<p>Chcete-li vidět i hole jiných značek, otevřete <a href="/zlata-hokejka/">zlatou hokejku</a> s vybranými nabídkami nebo přímo <a href="/hokejky/">všechny hokejky</a>. Pro doplnění výstroje se hodí také <a href="/hokejove-brusle/">hokejové brusle</a>, <a href="/hokejove-chranice/">chrániče</a> a <a href="/hokejove-tasky/">tašky</a>, souhrn celé výbavy je v kategorii <a href="/hokej/">hokej</a>.</p>'
          '<h2>Rychlý kontrolní seznam před koupí</h2>'
          '<ul><li>Zjistěte výšku hráče a vyberte velikostní skupinu od Kid po SR.</li>'
          '<li>Zkontrolujte, zda je hůl pro levou nebo pravou ruku.</li>'
          '<li>U dětí volte nižší flex a dřevo, u soutěžních hráčů kompozit.</li>'
          '<li>Počítejte s ořezem, pokud je hůl delší než potřeba.</li>'
          '<li>Porovnejte u stejného modelu více obchodů, protože se liší dostupností délek a stran.</li></ul>',
    faq=[
        ('Je Fischer dobrá značka hokejek?', 'Pro děti, juniory a rekreační hráče ano. Dřevěné řady W jsou odolné a jednoduché, kompozitní RC One nabízejí nižší hmotnost. Pro profesionální výkon se hráči spíše obracejí na největší značky, ale na kvalitní trénink a ligu mládeže Fischer postačuje.'),
        ('Co znamená YTH, JR, INT a SR u hokejek Fischer?', 'Jde o velikostní skupiny: YTH je Youth, tedy mladší školní děti, JR Junior pro starší žáky, INT Intermediate pro dorost a SR Senior pro dospělé. Kid a Mini jsou ještě menší hole pro nejmladší.'),
        ('Jaký flex zvolit pro dítě?', 'Takový, aby se hůl dala ohnout vlastní vahou při střele. Čísla u YTH jsou nižší než u juniora a seniora. Raději měkčí než tuhá hůl, protože dítě na tuhé nenacvičí správnou techniku střely.'),
        ('Mám koupit levou, nebo pravou hokejku?', 'Podle toho, která ruka je při držení hole dole. Ruka dole určuje stranu. Když si nejste jisti, nechte dítě vyzkoušet obě strany s míčkem nebo pukem, případně se zeptejte trenéra.'),
        ('Vyplatí se kompozitní hokejka pro dítě?', 'Pokud dítě hraje pravidelně a roste pomalu, ano. Kompozit je lehčí a dítěti usnadní práci s pukem. Pokud hraje jen občas nebo se rychle protahuje, vydrží déle jednoduchá dřevěná hůl, kterou lze snadno vyměnit.'),
        ('Lze hokejku Fischer zkrátit?', 'Ano, dřevěné i kompozitní hole se zkracují ořezem shora. Po zkrácení se ale hůl zpevní, takže počítejte s nižším flexem, pokud dítě potřebuje měkčí odezvu. Nikdy neřežte čepel ani spodní část.'),
        ('Co znamená Grip v názvu hokejky?', 'Matný povrch rukojeti, který zlepšuje přilnavost rukavic a omezuje sklouzávání ruky. Mnozí hráči si hůl omotají páskou i přesto, hlavně na koncovém knoflíku.'),
        ('Dá se Fischer hokejka použít na pozemní hokej nebo florbal?', 'Ne. Tyto hokejky jsou určené pro ledový hokej a mají rovnou čepel. Pozemní hokej a florbal mají jiný tvar i rozměry, najdete je v kategoriích florbalové hole a pozemní hokej.'),
        ('Jak poznám správnou délku hole?', 'Postavte hůl špičkou čepele na zem. Na bruslích má končit mezi bradou a nosem, bez bruslí přibližně u brady. Krátká hůl dává lepší kontrolu, delší větší dosah.'),
        ('Kolik hokejek potřebuje dítě během sezóny?', 'Obvykle jednu hlavní a ideálně jednu záložní, hlavně u kompozitu. Čepel se opotřebovává a kompozit praská při nárazu, takže se vyplatí mít po ruce stejný model nebo dřevěnou záložní hůl.')
    ])

# ------------------------------------------------------------------ jurek-stany
NEW['jurek-stany'] = dict(
    title='Jurek stany: turistické, expediční a kempingové modely',
    desc='Stany Jurek od lehkých turistických řad Tramp, Vandr a Alp po expediční Dome a kempingové Family. Jak vybrat model, kapacitu a stavbu a porovnat nabídky.',
    intro='<p>Stany Jurek pokrývají celé spektrum od jednoduchého turistického stanu přes expediční model až po velké kempingové stany pro rodiny. Značka staví na pojmenovaných řadách jako Tramp, Vandr, Alp, Midi, Atak či Dome, takže se v nabídce rychle ztratíte, pokud nevíte, k čemu která slouží. '
          'Na této stránce je vybraný sortiment Jurek z kategorie <a href="/stany/">stany</a>. Průvodce vysvětluje, jak se liší turistické, expediční a kempingové modely, co znamenají přívěsky v názvu jako Duo, Lite nebo XL, kolik místa skutečně získáte a jak stan ošetřit. Pro srovnání s jinými značkami slouží přehledy <a href="/husky-stany/">Husky</a> a <a href="/coleman-stany/">Coleman</a>, o výprodejích pojednává stránka <a href="/stany-vyprodej/">stany ve slevě</a>.</p>',
    guide='<h2>Řady stanů Jurek a k čemu slouží</h2>'
          '<p>Jurek je polský výrobce outdoorového vybavení a jeho stany se vyznačují tím, že každý model má vlastní jméno. Z názvu se dá odvodit určení, protože se k němu přidává obecný typ: turistický, expediční nebo kempingový. Skupiny se liší především konstrukcí, hmotností a velikostí prostoru.</p>'
          + T(['Skupina', 'Příklady řad', 'Hodí se na'], [
              ['Turistické', 'Tramp, Vandr, Alp, Midi, Atak, Top, Ulli', 'pěší túry, kola, víkend v přírodě, tábory'],
              ['Expediční', 'Dome', 'náročné počasí, výšky, delší pobyty'],
              ['Kempingové', 'Family, Hotel, Grand', 'rodiny a skupiny, auto jako dopravní prostředek'],
              ['Bivaky a lehké modely', 'Bivi', 'minimalistické přespání, jedna osoba'],
              ['Doplňky', 'podlážky a předsíně', 'ochrana stanu a více místa na věci']]) +
          '<p>Přehledná orientace je užitečná, protože názvy se v nabídce obchodů opakují i s různými přídomky. Například řada Alp se vyskytuje ve variantách Lite, Duo, XL a podobně. Přídomek Lite obvykle znamená lehčí provedení, XL větší prostor a Duo bývá označení varianty s dvojicí, jejíž přesný význam si ověřte v popisu konkrétního kusu. Čísla v názvech, třeba 2.5 nebo 3.5, jsou označení značky a nejsou jednotná mezi výrobci, takže nečekejte, že dvojka znamená dvě osoby.</p>'
          '<h2>Turistický stan na túru</h2>'
          '<p>Turistické modely jsou určeny pro přenos na zádech nebo v kajaku. Na hmotnost se dívají jak výrobci, tak kupující, protože každý kilogram navíc se na kopci počítá. Typické jsou kompaktní tunelové nebo kupolové stavby s dvěma oblouky a malou předsíní na batohy a boty. Přesné parametry jako vodní sloupec nebo hmotnost se liší u každého modelu, takže je vždy čtěte u konkrétní nabídky a porovnávejte na stejném principu.</p>'
          '<ul><li><strong>Vstup:</strong> jeden vstup je lehčí, dva vstupy dávají každému spolunocležníkovi vlastní průchod.</li>'
          '<li><strong>Předsíň:</strong> za deště na ni spoléháte při vaření a odkládání bot, čím větší, tím lépe.</li>'
          '<li><strong>Stavba:</strong> klasické oblouky mají být zasunuté do nesených kanálků a jednoduché na rozložení za tmy.</li>'
          '<li><strong>Větrání:</strong> okno nebo větrací průduch brání kondenzaci, která se v noci tvoří na vnitřní straně.</li></ul>'
          '<p>Podrobné vysvětlení parametrů najdete v kategorii <a href="/turisticke-stany/">turistické stany</a>, kde jsou modely všech značek.</p>'
          '<h2>Expediční řada Dome</h2>'
          '<p>Dome je v nabídce Jurek expediční stan. Kupolová geometrie s křížícími se oblouky drží tvar i při větru z více směrů a snáší zatížení sněhem lépe než jednoduchý tunel. Cenou za to je vyšší hmotnost a delší stavba, proto se hodí tam, kde stan stojí několik nocí na jednom místě. Pokud plánujete spíš zimní tábor nebo výpravu do hor, podívejte se i na kategorii <a href="/expedicni-stany/">expediční stany</a>.</p>'
          '<p>Při pobytu ve sněhu se vyplatí dobře zakotvit lana a použít rozšířené kolíky. Stan s tenkými hliníkovými kolíky ve sněhu nedrží, doplňky pro tyto situace jsou v kategorii <a href="/stanove-kolky/">stanové kolíky</a>.</p>'
          '<h2>Kempingové stany Family, Hotel a Grand</h2>'
          '<p>Kempingové stany jsou stavěné do prostoru, který se nenosí. Mají vysoký strop, oddělenou ložnici, často více komor a velkou předsíň, která funguje jako obývací prostor. Řady Family, Hotel a Grand jsou určené rodinám a větším skupinám, kde se počítá s autem. Cenou je váha a velikost po složení: stan se hodí do kufru, ne na záda.</p>'
          '<p>Při výběru počítejte reálně. Stan pro šest osob s úložným prostorem neznamená šest lidí s matracemi, ale šest těl těsně vedle sebe. Pokud cestujete s dětmi, přidejte k deklarované kapacitě alespoň jedno místo, a pokud chcete uvnitř trávit čas za deště, počítejte s prostornou obytnou částí. Další varianty jsou v kategoriích <a href="/rodinne-stany/">rodinné stany</a> a <a href="/pristresky-a-party-stany/">přístřešky a párty stany</a>.</p>'
          '<h2>Jak vybrat velikost a kolik místa potřebujete</h2>'
          + T(['Situace', 'Doporučení', 'Důvod'], [
              ['Sólo túra', 'stan pro jednoho nebo dva', 'prostor navíc pro batoh a věci'],
              ['Dva lidé na túru', 'dvoumístný s předsíní', 'nízká váha a rozumná pohodlnost'],
              ['Dva dospělí a dítě', 'čtyřmístný model', 'prostor pro spaní a zavazadla'],
              ['Rodinný kemp u auta', 'kempingový stan s komorami', 'výška a oddělený prostor pro denní pobyt'],
              ['Zima a vítr', 'expediční model', 'pevná kostra a odolnost proti zatížení']]) +
          '<p>Rozhodující je také to, jak často stan postavíte. Pokud ho použijete dvakrát za léto, nepotřebujete nejlehčí variantu, naopak pokud se s ním pohybujete každý víkend, stojí za zvážení lehčí modely, které jsou pohodlnější na přenos.</p>'
          '<h2>Údržba a skladování</h2>'
          '<p>Stan je třeba po použití vždy vysušit. Vlhký stan uložený v obalu plesniví během pár dnů a plíseň trvale poškodí povrchovou úpravu látky. Po kempu nechte stan rozložený venku ve stínu, protože dlouhý pobyt na přímém slunci zhoršuje UV odolnost materiálu. Zipy čistěte od písku a promazávejte silikonovým sprejem. Nepoužívejte pračku ani silné chemikálie, stačí teplá voda a houba.</p>'
          '<p>Před novou sezónou zkontrolujte švy a po delším používání obnovte impregnaci. Poškozená látka se dá zalepit opravnou záplatou, což je levnější než koupit nový stan. Pro opravy a podlážky slouží kategorie <a href="/stanove-doplnky/">stanové doplnky</a>. K pohodlnému spaní patří i <a href="/spaci-pytle/">spací pytle</a> a <a href="/karimatky-a-matrace/">karimatky a matrace</a>, celkový přehled najdete v kategorii <a href="/kemping/">kemping</a>.</p>'
          '<h2>Jurek ve srovnání s jinými značkami</h2>'
          '<p>Na českém trhu stanů se potkáte s mnoha značkami: skandinávskými, českými i asijskými. Jurek je zajímavý hlavně tím, že nabízí hodně konkrétních modelů pro stejný typ použití, takže nemusíte kombinovat různé řady. Vedle něj se vyplatí zvážit i další značky, které jsou v nabídce zastoupené.</p>'
          + B(('husky', 'Husky'), ('coleman', 'Coleman'), ('high-peak', 'High Peak'), ('hannah', 'Hannah')) +
          '<p>Při porovnání se vždy dívejte na stejné parametry: počet osob, hmotnost, vodní sloupec, konstrukci a počet vstupů. Vyhněte se rozhodování jen podle názvu řady, protože každá značka používá vlastní pojmenování.</p>',
    faq=[
        ('Jaké stany Jurek existují?', 'V nabídce jsou turistické stany, například řady Tramp, Vandr, Alp, Midi, Atak či Top, expediční Dome a velké kempingové modely Family, Hotel a Grand. Najdete i bivak Bivi pro minimalistické spaní.'),
        ('Co znamená Lite v názvu stanu?', 'Obvykle lehčí provedení téhož modelu. Rozdíl bývá v tenčích materiálech nebo menším počtu doplňků. Přesnou hmotnost a výbavu si ověřte v popisu konkrétního produktu.'),
        ('Kolik lidí se do stanu skutečně vejde?', 'Údaj výrobce říká, kolik osob se vejde těsně vedle sebe bez zavazadel. Pro pohodlí i s batohy vybírejte o jednu osobu větší stan. Rodina s dětmi by měla počítat s větším prostorem než jen podle počtu lůžek.'),
        ('Hodí se stan Jurek na zimní kempování?', 'Zimní použití dává smysl u expedičního modelu Dome, který má kupolovou konstrukci. Lehké turistické stany jsou určené hlavně na období od jara do podzimu. Pro sníh použijte široké kolíky a dobře zakotvěte lana.'),
        ('Který stan Jurek je nejlehčí?', 'Nejlehčí bývají modely označené Lite a malé turistické řady pro jednoho nebo dva lidi. Hmotnost se u každého kusu liší, proto ji porovnávejte v popisu, nikoli podle názvu řady.'),
        ('Je potřeba pod stan podlážka?', 'Doporučuje se. Podlážka chrání dno před kamínky a vlhkostí a prodlužuje životnost stanu. Měla by být o něco menší než půdorys, aby voda stékala mimo ni a netekla pod ni.'),
        ('Jak stan Jurek správně sušit a skladovat?', 'Po použití ho rozložte a nechte uschnout ve stínu. Nikdy nesbalte vlhký stan na delší dobu, protože plesniví. Skladujte ve volném obalu, ne stlačený pod těžkými věcmi.'),
        ('Dá se stan opravit, když se roztrhne?', 'Drobná poškození se opravují samolepicí záplatou nebo speciální lepicí páskou. Zlomený oblouk lze nahradit opravnou objímkou. Větší trhliny řešte u výrobce nebo v servisu.'),
        ('Jak poznám skutečnou slevu na stan?', 'Porovnejte stejný model u více obchodů, sledujte vývoj nabídek a nepodléhejte škrtnuté ceně. Pokud je model dlouhodobě ve stejné cenové hladině, sleva je spíš marketing. Výprodeje stanů bývají na konci sezóny.'),
        ('Kolik vstupů má mít stan pro dva?', 'Dva vstupy jsou praktičtější, protože každý má vlastní východ a předsíň. Jeden vstup je lehčí a levnější, vyhovuje sólo túrám nebo páru, který počítá s jednou předsíní.')
    ])

# ------------------------------------------------------------------ panske-plavky-arena
NEW['panske-plavky-arena'] = dict(
    title='Pánské plavky Arena: jammery, slipy a šortky na bazén',
    desc='Pánské plavky Arena do bazénu: jammery, slipy, aquashorty a nízké šortky. Jak vybrat střih, velikost a materiál, jak plavky udržovat a porovnat nabídky.',
    intro='<p>Arena je značka, která se soustředí na plavání, a její pánské plavky jsou stavěné především pro bazén: v nabídce převládají jammery, slipy a krátké šortky z materiálů odolných chlóru. Hodí se plavcům, kteří trénují pravidelně, ale také těm, kdo chtějí do bazénu plavky, které vydrží víc než jednu sezónu. '
          'Tato stránka vybírá z kategorie <a href="/panske-plavky/">pánské plavky</a> modely Arena. Průvodce porovnává střihy, vysvětluje, co znamenají názvy jako Powerskin, Fireflow nebo aquashort, jak zvolit velikost a materiál, jak plavky prát a kdy se hodí závodní model. Pokud hledáte srovnání, otevřete i <a href="/speedo-plavky/">plavky Speedo</a>, <a href="/arena-plavky/">všechny plavky Arena</a> nebo <a href="/plavecke-bryle-arena/">plavecké brýle Arena</a>.</p>',
    guide='<h2>Čím se sortiment Arena v pánských plavkách vyznačuje</h2>'
          '<p>Značka Arena je zaměřená na plavecký sport, a proto v ní nenajdete tolik módních pláží jako u značek pro dovolenou. Většina nabídky patří do tří skupin: jammery, slipy a šortky. Rozdíl mezi nimi určuje délka nohavičky, krytí a to, kdy se do vody opravdu hodí.</p>'
          + T(['Střih', 'Co to je', 'Pro koho'], [
              ['Jammer', 'těsný střih po kolena nebo nad ně', 'trénink, závody, vytrvalost'],
              ['Slip (brief)', 'bez nohavičky, minimální odpor', 'rychlé plavání a plavci, kteří chtějí volnost'],
              ['Aquashort', 'krátké šortky, volnější střih', 'rekreační bazén, sauna, pláž'],
              ['Nízký pas (low waist)', 'kratší šortky na bedra', 'komfort a krátké tratě'],
              ['Powerskin', 'závodní kompresní modely', 'soutěžící, vrcholový trénink']]) +
          '<p>Hlavní přednost jammerů spočívá v tom, že se po kolena přiléhavý střih nepřevrací a nenasává vodu, takže na plavání jde o nejpraktičtější volbu. Slipy jsou nejlehčí, ale dávají minimální krytí, což se hodí hlavně na plavecký kroužek nebo trénink. Aquashorty jsou kompromis mezi volnou šortkou a sportovním střihem a jsou vhodné pro ty, kdo chtějí plavat i sedět u bazénu.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>V nabídce Arena se opakuje několik slov. Některá jsou barevná, například sea turtle, jellyfish nebo desert, a označují potisk. Jiná říkají něco o konstrukci nebo o určení modelu.</p>'
          '<ul><li><strong>Performance:</strong> sportovní řada pro pravidelný trénink.</li>'
          '<li><strong>Powerskin:</strong> závodní kompresní řada, kterou si koupí hlavně soutěžící.</li>'
          '<li><strong>Carbon:</strong> v názvu Powerskin znamená uhlíkové vlákno v látce pro vyšší kompresi.</li>'
          '<li><strong>Fireflow a Hyperflow:</strong> jména tréninkových řad, které se dodávají v různých barvách.</li>'
          '<li><strong>Solid a Team:</strong> jednobarevné týmové modely vhodné do plaveckých oddílů.</li></ul>'
          '<p>Pokud nevíte, kterou řadu vybrat, začněte u klasického tréninkového jammeru nebo krátkých šortek. Závodní Powerskin má smysl až při soutěžích, protože se obléká obtížně a opotřebovává se rychleji. Vhodnou obdobou jsou startovní obleky značky <a href="/znacka/speedo/">Speedo</a> nebo kombinace od <a href="/znacka/tyr/">Tyr</a>.</p>'
          '<h2>Velikost: jak změřit a co zvolit</h2>'
          '<p>Plavky se vybírají podle obvodu pasu a boků, v řadě tabulek také podle výšky. U Arena se můžete setkat s označením velikostí v centimetrech a v britských číslech, které na sebe navazují. Číslo pro obvod pasu vypadá zpočátku divně, ale odpovídá velikostem na štítku. Pokud si nejste jisti, zvolte podle většího rozměru. Plavky by měly být těsné, ale ne tak, aby se zařezávaly, protože se po namočení ještě poněkud roztáhnou.</p>'
          '<ul><li>Změřte pas ve výši pupku a boky v nejširším místě.</li>'
          '<li>Porovnejte hodnoty s tabulkou výrobce pro konkrétní model.</li>'
          '<li>Pro jammery zvolte spíš menší velikost, protože sedí lépe a nenasávají vodu.</li>'
          '<li>U aquashortů hledejte pas s tkanicí, kterou můžete doladit.</li>'
          '<li>Pokud jste mezi velikostmi, vezměte větší a upravte tkanicí.</li></ul>'
          '<h2>Materiál a odolnost vůči chlóru</h2>'
          '<p>Bazén je pro plavky mnohem nepřátelštější než moře. Chlór rozkládá elastanová vlákna, takže plavky z klasického nylonu ztrácejí pružnost a po pár měsících se vytahují. Proto se u sportovních značek používají polyesterové materiály, které chlór lépe snášejí. Jammer z takového materiálu vydrží stovky hodin, ale levný model z elastanu se po sezóně roztáhne a začne prosvítat.</p>'
          '<p>Pokud plavete častěji než jednou týdně, vyplatí se zvolit tréninkové plavky z polyesteru a mít druhé do páru, abyste je mohli střídat a nechat vždy dokonale vyschnout. Plavky na dovolenou k moři ušetřete na jiné použití a do bazénu je nepoužívejte.</p>'
          '<h2>Péče o plavky</h2>'
          '<ul><li><strong>Vypláchněte:</strong> po bazénu je opláchněte čistou vodou, aby se odstranil chlór.</li>'
          '<li><strong>Nemačkejte:</strong> plavky nevyždímávejte a nekrouťte, jen je přitiskněte do ručníku.</li>'
          '<li><strong>Suste ve stínu:</strong> slunce a radiátor snižují pružnost vláken.</li>'
          '<li><strong>Bez sušičky:</strong> teplo zničí elastan.</li>'
          '<li><strong>Perte šetrně:</strong> v ruce nebo v pračce při nízké teplotě, bez aviváže.</li></ul>'
          '<h2>Co dalšího k plavání potřebujete</h2>'
          '<p>K plavkám patří plavecké brýle, které bezpečně těsní a nezamlžují, čepice, která chrání vlasy před chlórem, a případně pomůcky pro trénink. Najdete je v kategoriích <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/plavecke-cepice/">plavecké čepice</a> a <a href="/plavecke-pomucky/">plavecké pomůcky</a>. Pro syna nebo dceru se hodí <a href="/detske-plavky/">dětské plavky</a>, pro partnerku <a href="/damske-plavky/">dámské plavky</a>. Přehled všech druhů je v kategorii <a href="/plavky/">plavky</a>.</p>'
          '<h2>Arena a jiné značky v pánských plavkách</h2>'
          '<p>Nejčastějším konkurentem Arena v bazénových plavkách je Speedo, které má v nabídce největší výběr. Dále se setkáte s modely značek Tyr, Finis, Funky Trunks nebo Volcom. Funky Trunks jsou známé výraznými potisky, Volcom se soustředí na surf a pláž, zatímco Tyr a Finis jsou blíž plaveckému sportu.</p>'
          + B(('speedo', 'Speedo'), ('tyr', 'Tyr'), ('finis', 'Finis'), ('funky-trunks', 'Funky Trunks'), ('volcom', 'Volcom')) +
          '<p>Při srovnávání se nedívejte jen na barvu a potisk. Porovnejte střih, materiál a velikostní tabulku konkrétního modelu, protože jedna značka může mít dvě odlišné konstrukce se stejnou velikostí. Pokud zvažujete jiné značky, otevřete <a href="/plavky-nike/">plavky Nike</a> nebo <a href="/plavky-adidas/">plavky adidas</a>.</p>',
    faq=[
        ('Jaké pánské plavky Arena zvolit do bazénu?', 'Pro pravidelný trénink jammer nebo krátké šortky z polyesteru. Slip je ještě lehčí volba pro rychlé plavání, aquashort se hodí na rekreační plavání a posezení.'),
        ('Co je jammer?', 'Těsný střih plavek, který končí nad kolenem nebo pod ním. Neplave se v něm tak volně jako ve slipu, ale nesplývá a nenasává vodu. Je to nejčastější volba trénujících plavců.'),
        ('Co znamená Powerskin?', 'Je to závodní řada Arena s kompresní úpravou. Je pevná, těsná a obléká se déle. Hodí se na soutěže a vrcholový trénink, na běžné plavání rekreačních plavců je zbytečná.'),
        ('Jak vybrat velikost plavek Arena?', 'Změřte pas a boky a porovnejte s tabulkou výrobce. Pokud jste mezi velikostmi, u šortek s tkanicí vezměte větší, u jammerů o něco menší, aby sedly přiléhavě.'),
        ('Jak dlouho plavky vydrží v chlóru?', 'Polyesterové sportovní plavky vydrží i několik sezón, pokud o ně pečujete. Klasické nylonové se vytahují mnohem dřív. Střídání dvou kusů a důkladné vysoušení jejich životnost prodlouží.'),
        ('Mohu v plavkách Arena chodit i na pláž?', 'Ano, aquashorty a volnější šortky ano. Jammery a slipy jsou stavěné na vodu a po pláži se v nich chodí hůř, navíc se v písku opotřebovávají.'),
        ('Jak plavky prát?', 'Po bazénu opláchnout čistou vodou, vyprat ručně nebo na šetrný program bez aviváže a sušit ve stínu. Nikdy nepoužívejte sušičku ani radiátor, elastan v teple ztrácí pružnost.'),
        ('Proč plavky po čase prosvítají?', 'Chlór a slunce rozkládají vlákna a látka se ztenčuje. Prosvítání je signál, že je čas na nové. Kvalitnější materiály vydrží déle, ale žádné plavky nejsou věčné.'),
        ('Jaký je rozdíl mezi slipy a jammery?', 'Slipy nemají nohavičku a nabízejí nejmenší odpor, jammery pokrývají stehna a drží stabilněji. Pro většinu plavců na dlouhý trénink jsou pohodlnější jammery, slipy zvolí ti, kdo preferují volnost nebo plavou závodně krátké tratě.'),
        ('Jsou plavky Arena i pro děti?', 'Ano, značka vyrábí i dětské a juniorské modely. Najdete je v kategorii dětské plavky, kde jsou chlapecké jammery a šortky ve velikostech podle výšky.')
    ])

# ------------------------------------------------------------------ damske-lyzarske-bryle
NEW['damske-lyzarske-bryle'] = dict(
    title='Dámské lyžařské brýle: střih, čočky a pohodlí s helmou',
    desc='Dámské lyžařské brýle na menší obličej: rám, nos, helma, barvy čoček, OTG a péče. Jak vybrat model od Smith, Uvex, Alpina, Bliz či Roxy a porovnat nabídky.',
    intro='<p>Dámské lyžařské brýle jsou menší a užší než unisex střih a lépe sedí na užším obličeji a na menších nosech. Na svahu to znamená méně průvanu kolem tváří, žádné sklouzávání po nose a lepší spolupráci s helmou. '
          'Tato stránka vybírá z kategorie <a href="/lyzarske-bryle/">lyžařské brýle</a> modely určené ženám. Průvodce vysvětluje, v čem je dámský střih jiný, jak zkoušet brýle s helmou, jak zvolit barvu čočky pro ranní světlo a odpolední mlhu, kdy se hodí OTG pro nositelky dioptrií a jak předejít zamlžování. Pro pány je určený přehled <a href="/lyzarske-bryle-panske/">pánských brýlí</a>, pro dívky <a href="/detske-lyzarske-bryle/">dětské lyžařské brýle</a>.</p>',
    guide='<h2>V čem je dámský střih jiný</h2>'
          '<p>Unisex lyžařské brýle jsou navrženy na průměrnou mužskou hlavu. Ženy mají v průměru užší a kratší obličej, užší nosní kořen a menší vzdálenost mezi očima, takže stejné brýle se na nich snáze zvedají na nose, tlačí na tváře nebo nepřilnou na bocích. Dámské modely tuto geometrii řeší.</p>'
          + T(['Část brýlí', 'Dámská úprava', 'Co to přináší'], [
              ['Rám', 'menší a užší, někdy označený S', 'méně průvanu na bocích'],
              ['Nosní výřez', 'užší a nižší', 'brýle neklouzají a netlačí na kořen nosu'],
              ['Pěna', 'měkčí a tenčí', 'méně tlaku na tváře'],
              ['Popruh', 'užší, často s úpravou na culík', 'lépe sedí na helmě a nevadí vlasům'],
              ['Barevné provedení', 'širší paleta', 'výhradně estetická věc']]) +
          '<p>Označení pro ženy je pomůcka, nikoli podmínka. Žena s větším obličejem se může cítit lépe v unisex modelu, naopak dívka s drobnými rysy v dětském nebo juniorském střihu. Rozhodují vždy pohodlí a těsnost kolem obličeje, ne štítek.</p>'
          '<h2>Jak brýle zkoušet</h2>'
          '<p>Lyžařské brýle se vždy zkoušejí s helmou, kterou na svahu používáte. Rám se musí opřít o helmu bez mezery nad horním okrajem, jinak vzniká takzvaný gap, přes který proudí studený vzduch na čelo. Naopak příliš těsná kombinace tlačí na obočí a způsobuje bolest hlavy po hodině jízdy.</p>'
          '<ul><li><strong>S helmou:</strong> mezera mezi horním okrajem rámu a helmou nemá být vidět.</li>'
          '<li><strong>Nos:</strong> brýle mají pevně sedět bez přitlačení, když zhluboka vydechnete.</li>'
          '<li><strong>Tváře:</strong> pěna by se měla dotýkat po celém obvodu.</li>'
          '<li><strong>Zorné pole:</strong> nesmí se objevit stín nebo omezení při otočení hlavy.</li>'
          '<li><strong>Popruh:</strong> zvolte délku tak, aby nebyl příliš stažený na zadní straně helmy.</li></ul>'
          '<p>Pokud kupujete brýle bez helmy, vezměte si helmu s sebou nebo zjistěte, zda je výrobce uvádí jako kompatibilní. K výběru pomůže i kategorie <a href="/lyzarske-helmy/">lyžařské helmy</a>.</p>'
          '<h2>Barva čočky pro ženy a pro různé světlo</h2>'
          '<p>Barva čočky ovlivňuje jak kontrast, tak komfort. Mnoho žen preferuje růžové nebo oranžové čočky, protože zvýrazňují reliéf ve slabém světle a hodí se na odpolední mlhu. Hnědá a šedá zachovávají přirozené barvy a jsou vhodné na ostré slunce. Zrcadlové vrstvy výrazněji snižují oslnění a jsou praktické na slunečné dny, ale ve stínu stromů mohou působit příliš tmavě.</p>'
          + T(['Podmínky', 'Vhodná barva čočky', 'Poznámka'], [
              ['Silné slunce', 'šedá, hnědá, zrcadlová', 'nižší propustnost světla'],
              ['Zataženo a sněžení', 'žlutá, oranžová, růžová', 'zvýrazní nerovnosti'],
              ['Střídavé počasí', 'fotochromatická', 'sama reaguje na světlo'],
              ['Les a večer', 'světlá čirá', 'méně tmavých míst']]) +
          '<p>Pokud lyžujete při různém počasí a nechcete si nosit druhé brýle, zvolte model s výměnným zorníkem nebo magnetickým systémem. Náhradní čočky najdete v kategorii <a href="/nahradni-zorniky/">náhradní zorníky</a>, kde se hodí i pro starší modely.</p>'
          '<h2>Brýle přes dioptrie a zamlžování</h2>'
          '<p>Nositelky dioptrických brýlí potřebují OTG model s dostatečně hlubokým rámem a výřezy po stranách, které se nedotýkají obrouček. Jinak se brýle opírají o rám dioptrických a tlačí je na nos. Další možností jsou kontaktní čočky, které bývají na svahu pohodlnější, ale nesnášejí vysoušení v mrazu.</p>'
          '<p>Zamlžování vzniká, když se vlhký vzduch z dechu a z kůže setká se studenou čočkou. Dvojitý zorník vytváří izolační vrstvu a omezuje kondenzaci, odvětrávací otvory v rámu vlhkost odvádějí. Pro prevenci pomáhá nepokládat brýle na čelo, protože tam se zahřejí párou a po návratu na oči zamlží. V pauzách je raději uložte do pouzdra.</p>'
          '<h2>Co dalšího se dívat u dámských brýlí</h2>'
          '<ul><li><strong>Tvar zorníku:</strong> cylindrický je klasický, sférický dává širší pohled.</li>'
          '<li><strong>Ochrana proti UV:</strong> kvalitní brýle by měly filtrovat UV záření ve všech kategoriích, včetně světlé čočky.</li>'
          '<li><strong>Odolnost:</strong> čočka musí být z nárazuvzdorného materiálu, aby se při pádu nerozbila.</li>'
          '<li><strong>Pouzdro:</strong> měkké pouzdro chrání čočku před poškrábáním při přepravě.</li>'
          '<li><strong>Čištění:</strong> otírejte jen měkkým hadříkem, nikoli ubrouskem ani rukávem.</li></ul>'
          '<h2>Značky dámských lyžařských brýlí</h2>'
          '<p>V nabídce jsou jak specializované značky, tak módní. Smith, Oakley, Scott a Uvex patří mezi nejznámější výrobce brýlí do hor, Alpina, Bliz a Rossignol nabízejí širokou škálu pro rekreační lyžaře. Roxy se zaměřuje na ženské snowboardové a lyžařské vybavení. Relax a R2 nabízejí přehledné řady pro rekreační lyžování.</p>'
          + B(('smith', 'Smith'), ('uvex', 'Uvex'), ('alpina', 'Alpina'), ('bliz', 'Bliz'), ('roxy', 'Roxy'), ('relax', 'Relax')) +
          '<p>Pro porovnání se vyplatí podívat se na značkové přehledy <a href="/lyzarske-bryle-oakley/">Oakley</a>, <a href="/lyzarske-bryle-uvex/">Uvex</a> a <a href="/lyzarske-bryle-poc/">POC</a>. K výbavě na svah patří také <a href="/lyzarske-rukavice/">lyžařské rukavice</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a> a <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>'
          '<h2>Skladování a péče</h2>'
          '<p>Po lyžování brýle otřete, rozložte, nechte vyschnout a uložte do pouzdra. Nevystavujte je horku a nenechávejte v autě za mrazu ani za velkého horka. Kondenzát z vnitřní strany nikdy neutírejte, nechte ho vyschnout, protože antifog vrstva se snadno setře. Při přepravě je uložte tak, aby se neotlačily o pevné předměty.</p>',
    faq=[
        ('Čím se dámské lyžařské brýle liší od unisex modelů?', 'Jsou menší, užší, mají nižší nosní výřez a měkčí pěnu. Lépe sedí na užších obličejích a méně tlačí. Označení je orientační, hlavní je, aby brýle dobře těsnily kolem celého obvodu.'),
        ('Jak zjistit, že mi brýle sedí s helmou?', 'Mezi rámem a helmou nesmí být mezera a brýle nesmí tlačit na obočí. Nejlépe je zkoušet s vlastní helmou nebo si ověřit kompatibilitu u výrobce.'),
        ('Jakou barvu čočky zvolit?', 'Na slunce tmavé šedé, hnědé nebo zrcadlové, na zataženo a sněžení žluté, oranžové či růžové. Při střídavém počasí vyberte fotochromatickou čočku nebo model s výměnným zorníkem.'),
        ('Co znamená OTG?', 'Brýle, které se nosí přes dioptrické brýle. Mají hlubší rám a výřezy po stranách, aby se dioptrické brýle neotlačovaly. Hodí se těm, kdo nechtějí lyžovat v kontaktních čočkách.'),
        ('Proč se brýle zamlžují?', 'Při setkání vlhkého teplého vzduchu se studenou čočkou vzniká kondenzace. Pomáhá dvojitý zorník, odvětrávání a to, že brýle nenosíte na čele. Antifog vrstvu neotírejte.'),
        ('Je lepší cylindrický, nebo sférický zorník?', 'Sférický dává širší zorné pole a méně zkreslení, cylindrický je klasický a zpravidla jednodušší. Pro rekreační lyžaře je rozdíl malý, pro rychlou jízdu nebo freeride se sférický vyplatí.'),
        ('Dají se vyměnit zorníky na starších brýlích?', 'U modelů s výměnným systémem ano. Náhradní zorníky se kupují pro konkrétní řadu, nelze je kombinovat mezi značkami. V kategorii náhradních zorníků vyhledejte přesný název modelu.'),
        ('Jak čistit lyžařské brýle?', 'Stačí měkký mikrovláknový hadřík a čistá voda. Nepoužívejte papírové ubrousky, rukáv ani chemické čističe, které poškozují povrchovou úpravu čočky.'),
        ('Hodí se dámské brýle i pro snowboard?', 'Ano, lyžařské a snowboardové brýle jsou konstrukčně stejné. Pro snowboard se hodí modely s širším zorným polem a rámem, který dobře sedí s helmou.'),
        ('Jak poznat dobré brýle bez drahé značky?', 'Zkontrolujte kategorii čočky, ochranu proti UV, dvojitý zorník, odvětrávání a měkkou pěnu. Kvalitní model ukazuje parametry v popisu a nenechává je nejasné.')
    ])


# ------------------------------------------------------------------ doplnění sekcí
NEW['fischer-hokejka']['guide'] += (
    '<h2>Dětská hokejka: kdy měnit velikost</h2>'
    '<p>Dítě mezi šestým a dvanáctým rokem vyroste z jedné hole během jedné až dvou sezón. Znamení, že je čas přejít na větší velikost, je jednoduché: hůl postavená vedle hráče bez bruslí sahá nad bradu, nebo se dítě při vedení puku zbytečně hrbí. Naopak zbytečně dlouhá hůl, koupená na vyrůstání, mu brání v rychlém vedení puku a zhoršuje techniku. Kupujte proto vždy podle současné výšky, ne podle představy, jak vyroste.</p>'
    '<p>Praktický postup pro rodiče je tento: starou hůl, která ještě drží, nechte jako záložní na trénink venku nebo na asfalt, a novou pořiďte na led. Dřevěná řada W se k tomu hodí lépe, protože se dá dát do ruky i dalšímu sourozenci a nevadí jí kontakt s betonem. Kompozit mějte jen na led a chraňte čepel před hrubým povrchem.</p>'
    '<h2>Čepel, spoj a údržba</h2>'
    '<p>Čepel se opotřebovává hlavně na špičce a patě, protože tudy se hůl opírá o led. Obrušení můžete zpomalit páskou, která se omotává po celé délce čepele a zároveň zlepšuje cit pro puk. Pásku střídejte po několika trénincích, protože nasákne vodou a ztvrdne. Při transportu hole nenechávejte na dveřích auta ani pod zavazadly, kompozit snáší tlak v ohybu hůř než dřevo.</p>'
    '<p>Pokud po tvrdém nárazu uslyšíte praskání nebo vidíte drobné trhlinky v lakované vrstvě, hůl už nepoužívejte. Prasknutí při střele je nepříjemné a pro mladého hráče riskantní, protože kus hole může odletět. Poškozenou hůl raději vyřaďte a kupte novou, než riskovat zranění.</p>'
)
NEW['fischer-hokejka']['faq'][0] = ('Je Fischer dobrá značka hokejek?', 'Pro děti, juniory a rekreační hráče ano. Dřevěné řady W jsou odolné a jednoduché, kompozitní RC One nabízejí nižší hmotnost a lepší odpich. Pro profesionální výkon se hráči spíše obracejí na největší značky, ale na kvalitní trénink a ligu mládeže Fischer postačuje. Rozhodující je správná velikost a flex, ne jméno na čepeli, protože i nejlepší hůl ve špatné délce hráče zpomaluje.')
NEW['fischer-hokejka']['faq'][4] = ('Vyplatí se kompozitní hokejka pro dítě?', 'Pokud dítě hraje pravidelně a roste pomalu, ano. Kompozit je lehčí a dítěti usnadní práci s pukem i nácvik střely. Pokud hraje jen občas nebo se rychle protahuje, vydrží déle jednoduchá dřevěná hůl, kterou lze snadno vyměnit. Rozumný kompromis je dřevěná hůl na trénink venku a kompozit jen na led.')

NEW['jurek-stany']['guide'] += (
    '<h2>Jak stan postavit a ochránit před deštěm</h2>'
    '<p>Zkuste si stan postavit doma nebo na zahradě dřív, než s ním vyrazíte. Za tmy a za deště je rozdíl mezi stanem, který znáte, a stanem poprvé z obalu obrovský. Zkontrolujte, zda je vše v obalu: kolíky, oblouky, lanka a opravná objímka. Rozložte podlážku pod stan a nastavte ji o něco menší než půdorys, aby po okraji nestékala voda pod dno.</p>'
    '<ul><li><strong>Vyberte místo:</strong> rovné, bez kořenů a kamenů, mimo koryta, kudy při dešti stéká voda.</li>'
    '<li><strong>Orientace:</strong> vstup obraťte proti větru jen tehdy, pokud je předsíň pevně zakotvená, jinak jej obraťte po větru.</li>'
    '<li><strong>Napnutí:</strong> přepláštění se nesmí dotýkat vnitřního stanu, jinak se vlhkost přenese dovnitř.</li>'
    '<li><strong>Lanka:</strong> za větru použijte všechna kotvicí lanka, každé zatížené uvnitř zapíchnutým kolíkem.</li>'
    '<li><strong>Větrání:</strong> nechte horní průduchy lehce otevřené i za deště.</li></ul>'
    '<p>Mokrý stan při balení nepřebalujte na cestě, nejprve ho v nejbližší možné chvíli vyvěste. Pokud to není možné, doma ho co nejdřív rozložte a nechte uschnout, jak už bylo popsáno výše.</p>'
    '<h2>Příslušenství, na které se zapomíná</h2>'
    '<p>Stan je jen jedna část vybavení. K spokojenému přespání patří také izolace od země, protože i v létě odvádí studená půda teplo z těla. Samonafukovací karimatka nebo nafukovací matrace zvedne spaní nad podlahu a výrazně zlepší komfort. Vhodné je i měkké světlo, které se dá zavěsit pod strop stanu, a malé smeták pro vymetení písku a listí. Vybavení pro přespání je v kategoriích <a href="/spaci-pytle/">spací pytle</a> a <a href="/karimatky-a-matrace/">karimatky a matrace</a>, k vaření se hodí <a href="/kempingove-nadobi/">kempingové nádobí</a> a pro posezení <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</p>'
    '<p>U velkých kempingových stanů nezapomeňte na pevný zatloukač a kolíky vhodné k půdě. Do tvrdé hlíny se hodí ocelové, do písku široké, a do sněhu speciální. Základní sada, která je v balení, často stačí jen na měkkou louku.</p>'
)
NEW['jurek-stany']['faq'][1] = ('Co znamená Lite v názvu stanu?', 'Obvykle lehčí provedení téhož modelu. Rozdíl bývá v tenčích materiálech nebo menším počtu doplňků. Přesnou hmotnost, vodní sloupec a výbavu si ověřte v popisu konkrétního produktu, protože řada Lite se může lišit od základního modelu i v dostupných velikostech. Při srovnávání vždy porovnávejte stejné údaje.')
NEW['jurek-stany']['faq'][6] = ('Jak stan Jurek správně sušit a skladovat?', 'Po použití ho rozložte a nechte uschnout ve stínu, pokud možno na větru. Nikdy nesbalte vlhký stan na delší dobu, protože plesniví a plíseň trvale poškodí látku i švy. Skladujte ve volném obalu na suchém a tmavém místě, ne stlačený pod těžkými věcmi nebo v garáži u chemikálií.')

NEW['panske-plavky-arena']['guide'] += (
    '<h2>Pro koho jsou plavky Arena nejlepší volbou</h2>'
    '<p>Plavky Arena se hodí třem typům plavců. První jsou pravidelní návštěvníci bazénu, kteří chodí plavat několikrát týdně a potřebují materiál, který vydrží chlór. Druhí jsou členové plaveckých oddílů a masters týmů, pro které je důležité, aby měli jednotný vzhled a střih, který se při startu neposune. Třetí jsou rekreační plavci, kteří chtějí v bazénu pohodlnou šortku a nechtějí řešit kompresní oblek.</p>'
    '<p>Naopak pokud jedete na dovolenou k moři a bazén používáte jen občas, nemusíte sahat po technických modelech. V takovém případě vyhoví volnější šortky z kategorie <a href="/panske-plavky/">pánské plavky</a>, které lze nosit i na procházku po pláži. Plavky Arena si pořizujte tehdy, když je skutečně často namočíte v bazénové vodě.</p>'
    '<h2>Jak plavky sedí ve vodě</h2>'
    '<p>Správně zvolený jammer se po skoku do vody nenafoukne, nesklouzne a nevytváří bublinu na zadní straně. Pokud po skoku cítíte, že se plavky posouvají nebo vám nasávají vodu, jsou příliš velké. Pokud naopak zařezávají do stehen nebo omezují pohyb při kraulu, zvolte vyšší velikost nebo jiný střih. Stejné pravidlo platí pro slipy: poznáte je podle toho, že neomezují pohyb, ale drží pevně.</p>'
    '<p>Tmavé jednobarevné plavky po delším používání zestárnou méně viditelně než světlé potištěné. Naopak potisky, například geometrické vzory nebo kresby zvířat, jsou zábavné a plavec je zdaleka pozná na dráze. Tmavý podklad zároveň lépe skryje případné skvrny od chlóru.</p>'
    '<h2>Dárek, oddíl a velké objednávky</h2>'
    '<p>Při nákupu dárku zvolte jammer nebo krátké šortky v základní barvě, protože neutrální střih nezklame. Pro plavecký oddíl se vyplatí sjednotit barvu a značku, ideálně i konkrétní model. V takovém případě sledujte u stejného modelu dostupnost velikostí v několika obchodech, protože oddílové barvy bývají rozebrané dřív než módní kousky. Pokud nákup plánujete s předstihem, počítejte i s časem doručení.</p>'
)
NEW['panske-plavky-arena']['faq'][0] = ('Jaké pánské plavky Arena zvolit do bazénu?', 'Pro pravidelný trénink jammer nebo krátké šortky z polyesteru, který snáší chlór. Slip je ještě lehčí volba pro rychlé plavání, aquashort se hodí na rekreační plavání a posezení u bazénu. Pokud plavete jen občas, stačí jednodušší model, naopak při tréninku několikrát týdně se vyplatí kvalitnější polyester a druhý kus na střídání.')
NEW['panske-plavky-arena']['faq'][4] = ('Jak dlouho plavky vydrží v chlóru?', 'Polyesterové sportovní plavky vydrží i několik sezón, pokud o ně pečujete. Klasické nylonové se vytahují mnohem dřív. Střídání dvou kusů, opláchnutí po každém plavání a důkladné vysoušení jejich životnost výrazně prodlouží. Pokud plavky po pár měsících povolí v pase nebo začnou prosvítat, je materiál unavený a vyplatí se je vyměnit.')
NEW['panske-plavky-arena']['faq'][8] = ('Jaký je rozdíl mezi slipy a jammery?', 'Slipy nemají nohavičku a nabízejí nejmenší odpor, jammery pokrývají stehna a drží stabilněji. Pro většinu plavců na dlouhý trénink jsou pohodlnější jammery, slipy zvolí ti, kdo preferují volnost nebo plavou závodně krátké tratě. Rozdíl ve vodě je spíše pocitový než měřitelný, takže rozhoduje komfort a to, jak se v plavkách cítíte na dráze mezi ostatními.')

NEW['damske-lyzarske-bryle']['intro'] = NEW['damske-lyzarske-bryle']['intro'].replace('Tato stránka vybírá', 'Na stránce jsou vybrané modely, a to konkrétně ty, které výrobci řadí do dámské skupiny. Tato stránka vybírá')
NEW['damske-lyzarske-bryle']['guide'] += (
    '<h2>Culík, čelenka a vlasy pod popruhem</h2>'
    '<p>Praktická otázka, která se v katalozích neobjevuje, je, jak brýle fungují s vlasy. Culík nebo drdol umístěný na zátylku zvedá popruh brýlí a vytlačuje je z helmy. Proto se vyplatí nosit vlasy nízko nebo do copu, který se vejde pod helmu, a popruh nasadit nad culík, nikoli pod. Některé dámské modely mají výřez nebo silikonové proužky, které popruh drží na místě i na hladké helmě.</p>'
    '<p>Pokud nosíte čelenku nebo čepici pod helmou, vezměte je při zkoušení s sebou, protože zmenšují prostor kolem obočí. Brýle, které se v obchodě zdály volné, mohou na svahu zatlačit na čelo. Při dlouhém lyžování se vyplatí mít tenkou čepici nebo čelenku z funkčního materiálu.</p>'
    '<h2>Pro koho jsou dámské brýle vhodné, a kdy zvolit jiné</h2>'
    '<p>Dámský střih je nejlepší pro dospělé ženy s menším až středním obličejem. Dívky od teenagerského věku mohou nosit stejné modely, pokud jim sedí. Mladší děti potřebují <a href="/detske-lyzarske-bryle/">dětské lyžařské brýle</a>, které mají jinou velikost rámu i kratší popruh. Pro ženy s velkým obličejem nebo širokou helmou může být lepší unisex model nebo <a href="/lyzarske-bryle-panske/">pánská varianta</a>.</p>'
    '<p>Při výběru se držte praktického pravidla: brýle musí vyplnit prostor mezi helmou a nosem, ale nesmějí tlačit. Barvy, vzory a doplňky jsou až druhotné. Dobrá volba je taková, na kterou po dvou hodinách jízdy zapomenete, protože sedí, nezamlžují se a dobře vidíte.</p>'
    '<h2>Kdy brýle vyměnit</h2>'
    '<p>Brýle nejsou na celý život. Čočka se časem poškrábe, antifog vrstva se opotřebuje a pěna ztvrdne nebo ztratí tvar. Na výměnu je čas, když i po důkladném očištění vidíte rozmazaně, když pěna netěsní nebo když popruh ztratil pružnost. Pokud je poškrábaná jen čočka a rám je v pořádku, vyměňte pouze zorník, což je levnější a ekologičtější řešení. Použité brýle nikdy nepoužívejte po silném nárazu, protože rám i čočka mohou mít skryté trhliny.</p>'
)
NEW['damske-lyzarske-bryle']['faq'][0] = ('Čím se dámské lyžařské brýle liší od unisex modelů?', 'Jsou menší, užší, mají nižší nosní výřez a měkčí pěnu. Lépe sedí na užších obličejích a méně tlačí na tváře i kořen nosu. Označení je orientační, hlavní je, aby brýle dobře těsnily kolem celého obvodu a bez mezery navazovaly na helmu, kterou na svahu skutečně nosíte.')
NEW['damske-lyzarske-bryle']['faq'][3] = ('Co znamená OTG?', 'Brýle, které se nosí přes dioptrické brýle. Mají hlubší rám a výřezy po stranách, aby se dioptrické brýle neotlačovaly o nos a spánky. Hodí se těm, kdo nechtějí lyžovat v kontaktních čočkách. Před nákupem vyzkoušejte kombinaci s vlastními dioptrickými brýlemi i s helmou.')

NEW['damske-lyzarske-bryle']['faq'][8] = ('Hodí se dámské brýle i pro snowboard?', 'Ano, lyžařské a snowboardové brýle jsou konstrukčně stejné, rozdíl je hlavně v designu. Pro snowboard se hodí modely s širším zorným polem a rámem, který dobře sedí s helmou, protože při jízdě po boku se často otáčíte přes rameno. Důležité je i dobré odvětrávání, hlavně při stoupání pěšky nebo čekání na vleku.')
NEW['damske-lyzarske-bryle']['faq'][9] = ('Jak poznat dobré brýle bez drahé značky?', 'Zkontrolujte kategorii čočky, ochranu proti UV, dvojitý zorník, odvětrávání a měkkou pěnu. Kvalitní model ukazuje parametry v popisu a nenechává je nejasné. Rozhodující je také zkouška s vaší helmou: i cenově dostupnější brýle, které těsní a nezamlžují, jsou lepší než drahé, které vám nesedí na obličeji.')
NEW['damske-lyzarske-bryle']['faq'][4] = ('Proč se brýle zamlžují?', 'Při setkání vlhkého teplého vzduchu se studenou čočkou vzniká kondenzace. Pomáhá dvojitý zorník, odvětrávání a to, že brýle nenosíte na čele ani v kapuci. Antifog vrstvu neotírejte, nechte brýle volně uschnout. Při vleku a stoupání, kdy se hodně potíte, je vhodné je krátce sundat.')
