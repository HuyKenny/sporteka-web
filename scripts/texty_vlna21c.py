"""sporteka.cz — wave 21c (4. 11. 2026): long texts (>= 1650 words) for golfove-doplnky, bivaky-a-kresla, balancni-pomucky, hokejove-brankarske-vybaveni.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ golfove-doplnky
NEW['golfove-doplnky'] = dict(long=True,
    title='Golfové doplňky: rukavice, kšiltovky, dálkoměry, tee',
    desc='Golfové doplňky pro hřiště: rukavice, kšiltovky, tee, dálkoměry, ručníky a oblečení. Jak vybrat velikost a materiál a porovnat obchody.',
    intro='<p>Golfové kolo trvá často čtyři hodiny i déle a za tu dobu se vystřídá slunce, vítr, vlhká tráva i drobný déšť. Hole a míčky jsou jen základ, o pohodlí a jistotě úderu rozhoduje i to, co máte na rukou, na hlavě a v kapsách tašky. '
          'Rukavice zlepšuje úchop, kšiltovka chrání zrak, tee a značkovač patří na každé jamkoviště a dálkoměr ušetří dohadování o vzdálenosti k praporku.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u golfových doplňků od značek Inesis, New Era, Under Armour, Nike, Adidas, Celio, Garmin, Callaway nebo Taylormade. '
          'K výběru se hodí i <a href="/golfove-hole/">golfové hole</a>, <a href="/golfove-micky/">golfové míčky</a>, <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a> a <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a>. Níže je přehled typů, velikostí a častých chyb.</p>',
    guide='<h2>Co všechno patří mezi golfové doplňky</h2>'
          '<p>Kategorie sdružuje drobnosti, které se do tašky vejdou vedle holí, ale hru znatelně zpříjemňují. V nabídce najdete rukavice, kšiltovky a čepice, tee, značkovače, nástroje na opravu důlků, ručníky, dálkoměry, ale také sportovní oblečení s golfovou tematikou, například mikiny, vesty, šortky a kalhoty. '
          'Část sortimentu tvoří dětské sety a obuv, takže si tu rodiny pořídí vše potřebné na první výlet na cvičnou loučku.</p>'
          + T(['Doplněk', 'K čemu slouží', 'Na co dát pozor'], [
              ['Golfová rukavice', 'pevnější úchop a ochrana dlaně před otlaky', 'přesná velikost, materiál, počasí'],
              ['Kšiltovka a čepice', 'ochrana před sluncem nebo chladem', 'velikost, nastavení, prodyšnost'],
              ['Tee a značkovač', 'podložka pro míček a označení polohy na greenu', 'délka tee, množství v balení'],
              ['Nástroj na důlky', 'oprava stopy po dopadu míčku na greenu', 'pevný hrot, malá velikost'],
              ['Ručník', 'čištění holí, míčku a rukou', 'savost, karabina na tašku'],
              ['Dálkoměr', 'změření vzdálenosti k praporku', 'pravidla soutěže, dosah, baterie'],
              ['Oblečení', 'pohyblivost a ochrana při švihu', 'střih v ramenou, vrstvení']]) +
          '<h2>Golfová rukavice: velikost, materiál a počasí</h2>'
          '<p>Golfová rukavice se nosí obvykle jen na jedné ruce, a to na té, která drží hůl blíž k hlavě. Praváci ji tedy mají na levé ruce, leváci na pravé. Důvod je praktický: horní ruka přenáší větší část síly a bez rukavice by při švihu snadno prokluzovala. '
          'Někteří hráči nosí rukavici na obou rukou, hlavně v chladnu a vlhku, ale pro běžnou hru stačí jedna.</p>'
          '<h3>Jak vybrat velikost</h3>'
          '<p>Rukavice musí sedět jako druhá kůže. Špičky prstů mají dosáhnout až na konec rukavice a v dlani se nesmí tvořit záhyby, protože ty tlačí a při dlouhé hře způsobují puchýře. Příliš velká rukavice se na rukojeti kroutí a ztrácí smysl, příliš malá omezuje pohyb. '
          'Velikostní tabulky se liší podle výrobce, proto změřte obvod dlaně a porovnejte ho s údajem konkrétní značky. Dámské modely mají užší prsty, dětské jsou kratší a mají jednodušší zapínání.</p>'
          '<h3>Kůže, syntetika a kombinace</h3>'
          '<ul><li><strong>Kožená rukavice:</strong> měkká, citlivá, dobře drží na rukojeti. Vlhkostí a potem se rychleji opotřebuje, po sezóně bývá potřeba ji vyměnit.</li>'
          '<li><strong>Syntetická rukavice:</strong> odolnější, snáší pot a občasné promáčení a lépe drží tvar po vyprání.</li>'
          '<li><strong>Kombinace:</strong> kůže v dlani, prodyšný elastický materiál na hřbetu a mezi prsty. Zajišťuje cit i pohodlí při dlouhém kole.</li>'
          '<li><strong>Dešťová rukavice:</strong> při namočení drží lépe než klasická, a proto se nosí v páru.</li></ul>'
          '<p>Rukavici po hře nenechávejte zmačkanou v tašce. Rozprostřete ji, nechte vyschnout při pokojové teplotě a ukládejte rovně, aby neztvrdla. Nepoužívejte radiátor ani fén.</p>'
          '<h2>Kšiltovky, čepice a ochrana před počasím</h2>'
          '<p>Kšiltovka patří k golfu stejně jako hole. Stíní oči před nízkým sluncem a pomáhá udržet hlavu v klidu při pohledu na míček. Značky New Era, Under Armour, Nike, Adidas nebo Callaway nabízejí modely s prodyšnými panely, pohlcujícím potítkem a nastavitelným zapínáním. '
          'Rovný kšilt a zahnutý kšilt jsou otázkou vkusu, funkčně se příliš neliší. V horkých dnech zvolte světlou barvu a lehčí materiál, v chladu se hodí čelenka nebo pletená čepice, která udrží teplo, ale nemění úder.</p>'
          '<p>Při proměnlivém počasí se vyplatí vrstvení: lehká mikina nebo vesta se zipem, nepromokavá bunda zabalená v tašce a v zimě termo spodní vrstva. '
          'Funkční prádlo najdete v kategoriích <a href="/termopradlo/">termoprádlo</a>, <a href="/sportovni-bundy/">sportovní bundy</a> a <a href="/cepice-a-celenky/">čepice a čelenky</a>. Pro golfisty je podstatný volný střih v ramenou, aby oblečení nebránilo plnému otočení trupu.</p>'
          '<h2>Tee, značkovače a nástroje na péči o green</h2>'
          '<p>Tee je malá podložka, na kterou se při prvním úderu na jamce položí míček. Dřevěná nebo bambusová tee se při úderu často zlomí, plastová vydrží déle. Délka se volí podle hole: kratší tee pro železa a delší pro driver, kde má míček ležet nad horní hranou hlavy hole. '
          'Do tašky patří zásoba tee v balení po desítkách a několik náhradních, protože se snadno ztratí v trávě. Bambusová tee v hromadném balení bývá nejlevnější způsob, jak mít dost na celý rok.</p>'
          '<p>Značkovač je malý disk nebo mince, kterou na greenu položíte za míček, než ho zvednete. Díky němu míček očistíte a neblokujete dráhu ostatním. Mnoho značkovačů je magnetických a drží na čepičce nebo na nástroji na důlky. '
          'Nástroj na opravu důlků je vidlička nebo dvouzubý hrot, kterým se stopa po dopadu míčku zatlačí do vyrovnané plochy. Neopravený důlek na greenu znamená nerovnou dráhu pro další hráče, proto jde o základ golfové etikety.</p>'
          '<h2>Dálkoměry a GPS hodinky</h2>'
          '<p>Přesná vzdálenost k praporku usnadňuje výběr hole. Laserový dálkoměr zaměří cíl přes optiku, GPS přístroj a hodinky zobrazují vzdálenost k přední a zadní části greenu podle uložené mapy hřiště. Na trhu se objevují modely značek Garmin a dalších výrobců, například řada Approach. '
          'Dalekohled s dálkoměrem je přesnější na praporek, GPS rychlejší na orientaci a lépe zobrazí překážky. Před nákupem zvažte, zda jej chcete použít v turnaji. Podle pravidel golfu se měřiče vzdálenosti smějí používat, pokud to místní pravidla nezakazují, a funkce, které počítají například sklon nebo vítr, bývají v soutěžích vypnuté. Informace si ověřte u pořadatele.</p>'
          '<h2>Golfové oblečení a obuv v kategorii</h2>'
          '<p>Golfové oblečení se liší od běžného sportovního tím, že dovoluje široký švih a v chladu drží teplo. Pánské i dámské šortky, kalhoty, polokošile a mikiny z pružných materiálů, které odvádějí pot, ale zároveň neškrtí v loktech. Bundy a vesty z lehkých tkanin se skládají do tašky. '
          'Dětská nepromokavá bunda a lehké kalhoty se vyplatí kvůli častému sezení v trávě. Obuv se zde objevuje jako golfové tenisky se spikes i bez nich. Bezhrotové modely vyhovují na cestu na hřiště i do města, hrotové drží lépe na mokré trávě. '
          'Širší nabídku najdete v kategorii <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a> a v <a href="/sportovni-ponozky/">sportovních ponožkách</a>. Lehké vrstvy hledejte také mezi <a href="/mikiny/">mikinami</a> a <a href="/sportovni-kratasy/">sportovními kraťasy</a>.</p>'
          '<h2>Ručníky a péče o vybavení</h2>'
          '<p>Ručník na tašce je nenápadný, ale užitečný. Vlhkou rukojeť i čepel hole osušíte, míček očistíte a ruce utřete před úderem. Ručníky s karabinou nebo očkem se přichytí k tašce a nepadají do trávy. Nejlepší je froté z bavlny, která saje, a druhý, čistý, na ruce. '
          'Vlhké hole nemají zůstat v tašce přes noc, hlavně chrom a rukojeti. Po hře je očistěte kartáčem a suchým hadrem, rukojeti občas omyjte vlažnou vodou s jemným mýdlem a nechte uschnout.</p>'
          '<h2>Výběr podle hráče a sezóny</h2>'
          '<ul><li><strong>Začátečníci:</strong> rukavice, zásoba tee, značkovač, nástroj na důlky a ručník. Na prvních kolech zbytečně neutrácejte za drahé přístroje. Základ doplňte <a href="/golfove-hole/">golfovým setem</a>, <a href="/golfove-micky/">míčky</a> a <a href="/golfove-tasky-a-voziky/">taškou</a>.</li>'
          '<li><strong>Pravidelní hráči:</strong> dvě rukavice na střídání, kšiltovka do slunce, dálkoměr nebo GPS a oblečení do proměnlivého počasí.</li>'
          '<li><strong>Turistické golfování a dovolená:</strong> lehké oblečení, skládací bunda a malá taška na drobnosti. Pomohou i <a href="/lahve-a-termosky/">lahve a termosky</a>, protože hřiště nemá vždy vodu poblíž.</li>'
          '<li><strong>Děti:</strong> kratší tee, dětská rukavice a nepromokavá bunda. Dětské sety s holemi a taškou jsou praktické pro první zkoušky.</li>'
          '<li><strong>Dárky:</strong> sady tee a značkovačů, kšiltovky nebo rukavice. Velikosti ověřte předem, nebo zvolte univerzální doplněk.</li></ul>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupě rukavice o číslo větší „kvůli pohodlí“. Na rukojeti pak klouže a mačká se.</li>'
          '<li>Rukavice na špatné ruce. Pravák ji nosí vlevo, levák vpravo.</li>'
          '<li>Příliš dlouhá tee pro železa, díky čemuž míček létá příliš vysoko a ztrácí dosah.</li>'
          '<li>Dálkoměr s funkcemi, které jsou v turnaji zakázané, aniž by si hráč ověřil pravidla.</li>'
          '<li>Neprodyšná čepice v létě, ve které hlava přehřívá.</li>'
          '<li>Skladování mokré rukavice v tašce, kde ztvrdne a zplesniví.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U drobností jako tee a značkovačů rozhoduje cena za kus a poštovné, protože se vyplatí kupovat větší balení nebo nakupovat spolu s dalším zbožím. '
          'U rukavic a čepic porovnávejte velikost, barvu a materiál, protože stejný model se prodává ve více variantách. Dálkoměry a GPS hodinky srovnejte podle záruky a toho, zda obchod uvádí české pokyny. '
          'Sporteka ukazuje nabídky více obchodů na jednom místě, takže snadno poznáte, kde je zboží skladem a kolik stojí doprava.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Golfové doplňky a oblečení nabízejí značky {B(("inesis", "Inesis"), ("new-era", "New Era"), ("under-armour", "Under Armour"), ("nike", "Nike"), ("adidas", "Adidas"), ("celio", "Celio"), ("garmin", "Garmin"), ("callaway", "Callaway"), ("taylormade", "Taylormade"), ("gregnorman", "Gregnorman"))}. '
          'Inesis nabízí pestrou škálu základního vybavení vhodného pro začátek, Under Armour a Nike sázejí na pružné materiály a New Era na kšiltovky a oblečení s klubovou tematikou. Garmin je zastoupen dálkoměry a GPS přístroji.</p>',
    faq=[('Na kterou ruku se nosí golfová rukavice?', 'Praváci ji nosí na levé ruce, leváci na pravé. Rukavice je na ruce, která drží hůl blíž k hlavě, protože právě ta přenáší větší část síly.'),
         ('Kolik golfových rukavic potřebuji?', 'Pro začátek stačí jedna. Pravidelní hráči mívají dvě a střídají je, aby jedna mohla vyschnout. V dešti se hodí speciální rukavice, které při namočení drží lépe.'),
         ('Jak poznám správnou velikost rukavice?', 'Špičky prstů mají dosahovat na konec rukavice a v dlani se nesmí tvořit záhyby. Změřte obvod dlaně a porovnejte ho s tabulkou výrobce, protože se velikosti liší.'),
         ('Jak dlouhá má být tee?', 'Pro driver delší, aby míček ležel nad horní hranou hlavy hole, pro železa kratší nebo jen mírně zapíchnutá. Stačí mít v tašce dvě délky.'),
         ('Co je značkovač a proč ho používat?', 'Je to malý disk nebo mince, kterou položíte na green za míček předtím, než ho zvednete a očistíte. Neblokuje dráhu ostatním a míček pak vrátíte na stejné místo.'),
         ('Proč opravovat důlky po dopadu míčku?', 'Neopravený důlek vytvoří nerovnost, která mění dráhu následujících míčků. Oprava vidličkou trvá chvíli a je součástí golfové etikety.'),
         ('Smím v turnaji používat dálkoměr?', 'Podle pravidel golfu je obvykle povolen, pokud ho místní pravidla nezakazují. Funkce, které měří sklon nebo vítr, bývají v soutěžích nepovolené. Ověřte si to u pořadatele.'),
         ('Jak se starat o koženou golfovou rukavici?', 'Po hře ji rozložte a nechte uschnout při pokojové teplotě, ne na topení. Ukládejte ji rovně a nenechávejte zmačkanou v tašce, jinak ztvrdne.'),
         ('Hodí se golfové oblečení i na jiný sport?', 'Ano, pružné polokošile, mikiny a kalhoty zvládnou i běžnou turistiku a volný čas. Při výběru ale sledujte střih v ramenou, aby nebránil švihu.'),
         ('Co koupit začátečníkovi na první kolo?', 'Rukavici, zásobu tee, značkovač, nástroj na důlky a ručník. Dálkoměr a drahé oblečení přijdou na řadu až po několika odehraných kolech.'),
         ('Na co se dívat u golfové obuvi?', 'Na přilnavost podešve, vodovzdornost a pohodlí při chůzi. Bezhrotové boty se hodí na cvičiště i do města, hrotové držejí líp na mokré trávě.')])

# ------------------------------------------------------------------ bivaky-a-kresla
NEW['bivaky-a-kresla'] = dict(long=True,
    title='Rybářské bivaky, lehátka a křesla: výběr podle lovu',
    desc='Rybářské bivaky, přístřešky, lehátka, křesla a stoličky. Jak vybrat velikost, nosnost a vodní sloupec a porovnat ceny obchodů.',
    intro='<p>Při několikadenním lovu kapra nebo při dlouhé feederové výpravě se z břehu stane malý tábor. Nejde jen o pohodlí: kdo spí v suchu a sedí zpříma, vydrží u vody déle, má víc soustředění a lépe zareaguje na záběr. '
          'Proto se v této kategorii potkávají bivaky a přístřešky, lehátka s nohama i bez nich, rybářská křesla, stoličky a drobné příslušenství, jako jsou podlážky, boční plata, kolíky a organizéry.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u značek Fox, Mivardi, Trakker, Mikado, Anaconda, Delphin, Giants Fishing, Suretti, Zfish nebo NGT. '
          'K výběru se hodí i <a href="/rybarske-stany/">rybářské stany</a>, <a href="/rybarske-spacaky/">rybářské spacáky</a>, <a href="/rybarske-tasky/">rybářské tašky</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>. Níže je přehled typů a kritérií výběru.</p>',
    guide='<h2>Jaké vybavení kategorie obsahuje</h2>'
          '<p>Základem jsou tři skupiny: úkryt před počasím, místo na spaní a místo na sezení. Úkryt tvoří bivak (uzavřený stan s podlahou a vchodem), přístřešek (shelter) bez podlahy nebo se zadní stěnou a plachta s kolíky. '
          'Spaní zajišťuje lehátko, v rybářské terminologii bedchair, často s nastavitelnými nohami a možností uložení spacáku. Posezení doplňují křesla, skládací stoličky a stolky. K tomu přibývají doplňky pro jednotlivé modely, třeba prodloužení, čelní panely a boční plata.</p>'
          + T(['Typ', 'Hlavní výhoda', 'Pro koho'], [
              ['Bivak', 'úplná ochrana, vlastní podlaha, prostor pro lehátko', 'vícedenní lov, noční rybaření, podzim a zima'],
              ['Přístřešek (shelter)', 'rychlé postavení, dobrá ventilace', 'jednodenní lov a krátké noční výpravy'],
              ['Lehátko', 'spaní a odpočinek nad zemí', 'kapraři a přívlačáři na delším lovu'],
              ['Rybářské křeslo', 'pohodlné sezení s opěradly a loketními opěrkami', 'feeder, položená a dlouhé sezení'],
              ['Skládací stolička', 'nízká váha, snadný přenos', 'krátké výlety, přívlač, pohyb po břehu'],
              ['Příslušenství', 'kolíky, podlážky, boční plata, organizéry', 'doplnění vybavení a opravy']]) +
          '<h2>Bivak a přístřešek: jak se liší</h2>'
          '<p>Bivak je uzavřená konstrukce na jednoho až dva rybáře, někdy s rozšiřitelným předním dílem. Díky pevné podlaze a vchodu vás chrání před vlhkem a hmyzem, ale obvykle je těžší a postavení trvá déle. '
          'Přístřešek je lehčí a otevřenější, často bez podlahy, a hodí se pro hlídání prutů, krátké noční výpravy i letní lov. Mnoho modelů, například <strong>Quick Set</strong> nebo <strong>Base Station</strong>, jde postavit v několika minutách. Pokud lovíte za deště, vybírejte přístřešek s čelním panelem, který se zavírá zipem.</p>'
          '<h3>Vodní sloupec, materiál a ventilace</h3>'
          '<p>Odolnost proti vodě se udává ve vodním sloupci v milimetrech. Vyšší hodnota znamená, že látka snese větší tlak vody, ale samotné číslo nezaručí suchý interiér. Důležitější jsou přelepené švy, pevná podlaha a správné napnutí střechy. '
          'Při noční výpravě se uvnitř bivaku sráží pára, proto potřebujete ventilační průduchy nebo větrací okénka. U jednovrstvých stanů se kondenzace tvoří častěji, dvouvrstvé a modely s dobrou vzduchovou mezerou sráží méně. '
          'Camo barevnost pomáhá splynout s okolím a nerušit ostatní rybáře, odstíny zelené a hnědé fungují u většiny vod.</p>'
          '<h3>Velikost, hmotnost a postavení</h3>'
          '<p>Označení jako 1 Man, 2 Men nebo King Size popisuje počet osob, nikoli skutečné pohodlí. Do jednomístného bivaku se vejde lehátko a jedna taška, ve dvoumístném už můžete položit i ukládací box. Vždy porovnejte rozměr lehátka s rozměrem bivaku. '
          'Hmotnost řeší hlavně ti, kdo přenášejí vybavení daleko od auta. Jinak se vyplatí tužší konstrukce s lepší stabilitou ve větru. Pevné kolíky a zajišťovací lana jsou důležitější než další centimetr výšky.</p>'
          '<h2>Lehátka (bedchair)</h2>'
          '<p>Lehátko je středobodem kaprařského tábora. Vybírejte podle délky, šířky a nosnosti, podle toho, zda má čtyři, šest nebo osm nohou, a podle možnosti nastavit výšku. '
          'Osmnohé modely, jako je kategorie 8-Leg, stojí stabilněji na nerovném břehu, protože zatížení rozloží na více bodů. Důležité je i opěradlo, které se naklání, a rám, který se nezaboří do měkké hlíny.</p>'
          '<ul><li><strong>Rám:</strong> hliník je lehčí a nekoroduje, ocel pevnější a obvykle těžší.</li>'
          '<li><strong>Matrace:</strong> hustší molitan nebo vzduchová vrstva izoluje od studeného rámu.</li>'
          '<li><strong>Nohy:</strong> nastavitelné a s větší stopou, aby se nebořily do bahna.</li>'
          '<li><strong>Doplňky:</strong> boční kapsy, příčné popruhy na spacák a přídavná kapsa na lehátko.</li>'
          '<li><strong>Skládací rozměr:</strong> musí se vejít do auta a do transportní tašky.</li></ul>'
          '<p>Na lehátko patří vhodný spací systém. Nabídku najdete v kategorii <a href="/rybarske-spacaky/">rybářské spacáky</a> a v <a href="/spaci-pytle/">spacích pytlích</a>. Bivakovací pytle ze tří vrstev slouží jako přídavná ochrana v extrémních podmínkách, nikoli jako náhrada stanu.</p>'
          '<h2>Křesla a stoličky</h2>'
          '<p>Rybářské křeslo se vyznačuje opěradlem, loketními opěrkami a nastavitelnými nohami. Při feederovém rybaření, kde se u prutu dlouho sedí a čeká na záběr, si pohodlný sed rychle oblíbíte. '
          'Modely typu Chair Deluxe nebo Armchair mívají široké sedadlo, nosnost výrazně vyšší než běžná stolička a polstrování s potahem, který snese vlhkost. Při přenášení vás potěší, když se křeslo složí do tvaru, který vejde do vaší tašky. '
          'Nízké křeslo je vhodné pro kapraře, vyšší pro feedristu, který potřebuje rychle vstát. Stolička je lehčí, ale bez opěradla a pro dlouhé sezení méně pohodlná. Hodí se k přívlači, kde se pohybujete po břehu.</p>'
          + T(['Parametr', 'Co sledovat', 'Proč'], [
              ['Nosnost', 'rezerva nad vaší hmotností', 'konstrukce se méně namáhá'],
              ['Výška sedu', 'nízká pro kapra, vyšší pro feeder', 'záda a kolena'],
              ['Nohy', 'nastavitelné, s širokou botkou', 'stabilita na svahu'],
              ['Skládání', 'rozměr po složení', 'přenos a uložení v autě'],
              ['Potah', 'rychle schnoucí, snadno omyvatelný', 'vlhko a bláto']]) +
          '<h2>Příslušenství a doplňky bivaku</h2>'
          '<p>Základní bivak často potřebuje další díly, aby se zvýšila jeho užitná hodnota. <strong>Podlážka</strong> chrání před vlhkem a nechtěnými ostrými předměty. <strong>Prodloužení</strong> a <strong>čelní panel</strong> zakryjí vchod před deštěm. '
          '<strong>Boční plata</strong> zvětší vnitřní prostor, <strong>organizéry</strong> udrží drobnosti pohromadě a <strong>kolíky</strong>, často delší pro bivak, drží stan v měkké půdě. Při nákupu vždy ověřte, zda příslušenství pasuje na váš model, protože různé řady mají různé rozměry. '
          'Pro osvětlení večer použijte <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, pro nápoje <a href="/lahve-a-termosky/">lahve a termosky</a>.</p>'
          '<h2>Výběr podle stylu rybaření</h2>'
          '<ul><li><strong>Kapraři na několik dní:</strong> bivak s dobrou ventilací, osmnohé lehátko, spací systém a podlážka. Doplňte <a href="/rybarske-pruty/">pruty</a>, <a href="/rybarske-navijaky/">navijáky</a> a <a href="/nastrahy-a-navnady/">nástrahy a návnady</a>.</li>'
          '<li><strong>Feederisté:</strong> pohodlné křeslo, stolek, organizér a taška na drobnosti, <a href="/rybarske-tasky/">rybářské tašky</a>.</li>'
          '<li><strong>Jednodenní rybáři:</strong> lehký přístřešek a skládací stolička.</li>'
          '<li><strong>Podzim a zima:</strong> uzavřený bivak, izolace pod lehátkem a vrstvy oblečení. Pomůže <a href="/rybarske-obleceni/">rybářské oblečení</a>.</li>'
          '<li><strong>Letní noci:</strong> prodyšný přístřešek s moskytiérou a lehký spací pytel.</li></ul>'
          '<h2>Péče a skladování</h2>'
          '<p>Bivak sbalený mokrý zplesniví, proto ho doma rozložte a nechte uschnout. Před uložením odstraňte bláto a jehličí a zkontrolujte švy. Zipy občas očistěte kartáčkem a zasuňte do nich vhodný lubrikant. '
          'Kolíky umyjte a ohnuté narovnejte. Lehátko a křeslo opláchněte, po vyschnutí zkontrolujte šrouby a nýty a rám uložte suchý. Při dlouhém skladování stan nestlačujte a nedávejte ho do silně zahřátého prostoru.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Bivak vybraný jen podle počtu osob, bez ohledu na rozměr lehátka.</li>'
          '<li>Nákup s důrazem na vodní sloupec, ale bez přelepených švů a dobré ventilace.</li>'
          '<li>Lehátko s nedostatečnou stopou nohou, které se na měkkém břehu bortí.</li>'
          '<li>Zapomenuté zajišťovací kolíky a lana, takže přístřešek odnese vítr.</li>'
          '<li>Příslušenství koupené bez ověření, že pasuje na daný model.</li>'
          '<li>Stan zabalený mokrý a uložený v autě.</li></ul>'
          '<h2>Organizace tábora u vody</h2>'
          '<p>Dobře rozmístěné vybavení šetří pohyb a ruch na břehu. Lehátko se staví tak, aby hlava mířila od vody a nohy ke vchodu, a pruty mají být na dosah ruky, ale mimo prostor, kudy chodíte. Křeslo nebo stolek patří k boku bivaku, ne před vchod. '
          'Mokré boty a vlhké oblečení nechte v předsíni přístřešku, aby se vlhkost nenesla k lehátku. Velké nárazy větru zmírníte postavením zadní stěny proti převládajícímu proudění. Před večerem si připravte osvětlení, vodu a věci na noc, abyste po setmění nehledali v tašce.</p>'
          '<h2>Stolky a organizace drobností</h2>'
          '<p>K lehátku a křeslu se často přidává skládací stolek, na který se odloží nádobí, vařič, mobil i krabička s návazci. Důležitá je pevná deska a nohy, které se nezabořují do země. Organizéry a sady vnitřních kapes pověsíte na tyče bivaku, takže nic nemizí na zemi. '
          'Nezapomeňte na pytel na odpadky: čistý břeh je podmínkou, aby tam rybáře majitelé vod trpěli i příště. Citlivější vybavení, jako jsou elektronika a doklady, uložte do vodotěsné tašky v zadní části přístřešku.</p>'
          '<h2>Jak nakupovat</h2>'
          '<p>Rozměrné zboží se vyplatí kupovat v obchodě, který vám sdělí cenu dopravy a dostupnost. Pokud si nejste jistí, vyberte model, který má v nabídce i příslušenství. Porovnejte záruku, popis rozměrů a fotografie vnitřku. Sporteka zobrazuje nabídky více obchodů, takže snadno zjistíte, kdo má skladem právě vaše lehátko nebo přístřešek.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V kategorii najdete značky {B(("fox", "Fox"), ("mivardi", "Mivardi"), ("trakker-products", "Trakker Products"), ("mikado", "Mikado"), ("anaconda", "Anaconda"), ("delphin", "Delphin"), ("giants-fishing", "Giants Fishing"), ("suretti", "Suretti"), ("zfish", "Zfish"), ("ngt", "NGT"))}. '
          'Fox a Trakker jsou známé kaprařskými bivaky a lehátky, Mivardi a Mikado širokým sortimentem příslušenství, Anaconda a Zfish stany a lehátka pro kapraře, Delphin pestrým výběrem pro různé styly lovu.</p>',
    faq=[('Čím se liší bivak od přístřešku?', 'Bivak je uzavřený stan s podlahou a vchodem, přístřešek bývá otevřenější a lehčí, často bez podlahy. Bivak chrání lépe, přístřešek se staví rychleji.'),
         ('Co znamená vodní sloupec u bivaku?', 'Je to odolnost látky proti tlaku vody v milimetrech. Vyšší hodnota znamená větší odolnost, ale suchý interiér závisí také na přelepených švech a správném napnutí.'),
         ('Kolik lidí se vejde do bivaku 2 Men?', 'Označení udává přibližnou kapacitu. Uvnitř se často vejde jedno lehátko s taškou a druhá osoba se pohybuje stěží. Proto porovnejte rozměr lehátka s vnitřním prostorem.'),
         ('Jaké lehátko je pro kapraře nejvhodnější?', 'Stabilní, s širší stopou nohou, nastavitelnou výškou a naklápěcím opěradlem. Osmnohé modely se lépe drží na nerovném břehu a měkké půdě.'),
         ('Hodí se křeslo na feeder lépe než stolička?', 'Při dlouhém sezení ano, protože má opěradlo a loketní opěrky. Stolička je lehčí a hodí se pro krátké výlety a přívlač.'),
         ('Proč se uvnitř bivaku sráží voda?', 'Při dýchání a ve vlhkém prostředí se uvnitř tvoří pára, která se na chladné látce sráží. Pomáhá větrání, ventilační otvory a stan s dvěma vrstvami.'),
         ('Mám koupit podlážku k bivaku?', 'Podlážka se hodí, pokud bivak podlahu nemá, nebo ji chcete chránit před nečistotami a vlhkem. Ověřte rozměr daného modelu.'),
         ('Jak uskladnit stan po rybolovu?', 'Vždy ho doma rozložte, nechte uschnout a teprve pak zabalte. Mokrý stan zplesniví a látka ztratí vlastnosti.'),
         ('Jaké kolíky se hodí na měkký břeh?', 'Delší a širší kolíky, které se nezaboří po zatížení a drží i při větru. Do písku nebo bláta se hodí zvlášť dlouhé typy.'),
         ('Hodí se bivak i na zimní rybaření?', 'Ano, uzavřený bivak chrání před větrem a vlhkem, ale zima vyžaduje vrstvené oblečení, izolaci od země a spacák na nižší teploty.'),
         ('Co všechno potřebuji k nocování u vody?', 'Úkryt, lehátko nebo karimatku, spací pytel, osvětlení, nápoje a vrstvené oblečení. Detaily doplňte podle ročního období.')])

# ------------------------------------------------------------------ balancni-pomucky
NEW['balancni-pomucky'] = dict(long=True,
    title='Balanční pomůcky: podložky, desky, stepy a půlkoule',
    desc='Balanční podložky, desky, půlkoule, stepy a klouzavé disky na cvičení doma. Jak vybrat velikost a nosnost a porovnat nabídky obchodů.',
    intro='<p>Rovnováha se trénuje stejně jako síla: opakováním a postupným zvyšováním obtížnosti. Nestabilní podklad nutí hluboké svaly kolem kotníků, kolen a trupu pracovat, aniž byste zvedali velké zátěže. '
          'Proto se balanční pomůcky používají při rehabilitaci, v přípravě fotbalistů, hokejistů a lyžařů, při józe, pilates i při běžném cvičení doma.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u balančních podložek, desek, půlkoulí, stepů, klouzavých disků i dětských senzorických pomůcek od značek HMS, Sedco, Sportago, Merco, Insportline, Epicstar, Jakobs nebo Lifefit. '
          'K výběru se hodí i <a href="/fitness-pomucky/">fitness pomůcky</a>, <a href="/posilovaci-gumy/">posilovací gumy</a>, <a href="/funkcni-trenink/">funkční trénink</a> a <a href="/joga-a-pilates/">jóga a pilates</a>. Níže najdete typy, pravidla výběru a rady pro bezpečné cvičení.</p>',
    guide='<h2>Jaké balanční pomůcky existují</h2>'
          '<p>Společnou vlastností je nestabilní nebo pohyblivý povrch. Liší se tvarem, tuhostí a mírou obtížnosti, takže jedna pomůcka začátečníkovi pomůže, jiná je zpočátku frustrující. '
          'V kategorii najdete také stepy a bedýnky, které nejsou nestabilní, ale používají se spolu s nimi v aerobiku a rehabilitaci.</p>'
          + T(['Pomůcka', 'Princip', 'Hodí se na'], [
              ['Balanční podložka (pad)', 'měkká pěna, mírně nestabilní povrch', 'stoj na jedné noze, rehabilitace kotníku'],
              ['Balanční deska', 'plocha na kulatém nebo hranatém podstavci', 'dřepy, výpady, rovnováha vestoje'],
              ['Půlkoule', 'nafukovací nebo pryžová, vlastní plocha i kopec', 'cviky pro trup a nohy, push-upy'],
              ['Balanční míč', 'velký nafukovací míč', 'sed, plank, mobilita, posilování trupu'],
              ['Step a bedýnka', 'stabilní výšková platforma', 'aerobik, nášlapy, rehabilitační chůze'],
              ['Klouzavé disky', 'plochý disk, který klouže po podlaze', 'plank, výpady, posilování středu těla'],
              ['Pojízdná deska', 'deska na kolečkách', 'hra a trénink koordinace, i pro děti']]) +
          '<h2>Balanční podložky a pěnové pady</h2>'
          '<p>Podložka z TPE nebo z pěny je nejjednodušší způsob, jak přidat nestabilitu. Stoj na jedné noze, pomalé dřepy nebo přenášení váhy na ní provádějí hluboké svaly kolem kotníku. '
          'Je široká, často má drsný povrch pro lepší přilnavost a hodí se do bytu. Tvrdší pěna je stabilnější, měkká těžší na ovládání. Nejde o drahou pomůcku, ale o časté první kroky při rehabilitaci kotníku, a proto bývá běžným základem; vhodný postup vám doporučí fyzioterapeut.</p>'
          '<h2>Balanční desky</h2>'
          '<p>Balanční deska se vyznačuje kruhovou, oválnou nebo hranatou plochou, která se naklání na podstavci. Některé modely se kývají jen na jednu stranu, jiné všemi směry. Modely s kuličkami nebo s vlnou se používají na senzorický trénink a pro děti. '
          'Při volbě sledujte nosnost, protiskluzovou plochu a velikost, aby se vešla pod obě chodidla. Začátečníci zvolí nižší nebo kývavou jen jedním směrem, pokročilí desku s větším rozsahem. Dřevěné modely jsou pevné a tiché, plastové lehké a s odolným povrchem. '
          'Skateboardisté, snowboardisté a surfaři často využívají podobné desky jako suchou přípravu na sezónu.</p>'
          '<h2>Půlkoule a balanční míče</h2>'
          '<p>Nafukovací půlkoule má na jedné straně měkký povrch a na druhé pevnou plochu. Tlak vzduchu určuje obtížnost: méně vzduchu znamená větší stabilitu, více vzduchu větší nestabilitu, takže začátečník začíná s méně nafouknutou. Používá se otočená dolů k dřepům a výpadům nebo otočená nahoru k plankům a klikům. '
          'Menší pryžové půlkoule s výstupky slouží k senzorickému cvičení a ke cvičení v bosých nohou. Balanční míč, často v průměru kolem šedesáti až sedmdesáti centimetrů, hodí se k sezení, plank, mostu a protažení. Výšku míče vyberte podle postavy: při sedu na něm mají kolena zhruba v pravém úhlu.</p>'
          '<h2>Stepy, bedýnky a můstky</h2>'
          '<p>Step je stabilní plošina s nastavitelnou výškou, nejčastěji ve dvou nebo třech stupních. Využívá se v aerobiku, při kardiu i při cvičení pro posílení nohou. Bedýnky a můstky se hodí v rehabilitaci, kde nahrazují schod. '
          'Vybírejte model s protiskluzovým povrchem, pevnými nohami a nosností odpovídající vaší hmotnosti. Nízká výška je vhodná pro začátečníky, vyšší zvyšuje zátěž kloubů. Stepy navazují na <a href="/kardio-trenazery/">kardio trenažery</a> a <a href="/svihadla/">švihadla</a>, ale zabírají minimum místa.</p>'
          '<h2>Klouzavé disky</h2>'
          '<p>Klouzavé disky se podkládají pod ruce nebo nohy a využívají se na hladkých podlahách nebo na koberci, podle toho, jak jsou konstruované. Posilují střed těla v plancích, výpadech do stran a horolezeckých cvicích. Fungují jako doplněk, ne jako náhrada klasického posilování. '
          'Pokud je cvičíte na dřevěné podlaze, zvolte měkčí stranu, aby nezanechávaly škrábance.</p>'
          '<h2>Pro koho se balanční pomůcky hodí</h2>'
          '<ul><li><strong>Sportovci:</strong> fotbalisté, hokejisté, běžci a lyžaři využívají nestabilní povrch jako doplněk silové přípravy. Podobně pomáhá <a href="/funkcni-trenink/">funkční trénink</a> a <a href="/posilovaci-gumy/">posilovací gumy</a>.</li>'
          '<li><strong>Po zranění:</strong> stoj na podložce po uzdravení kotníku, ale jen podle doporučení lékaře nebo fyzioterapeuta.</li>'
          '<li><strong>Senioři:</strong> jednoduché cviky s oporou, například u zdi nebo židle, zlepší stabilitu při chůzi.</li>'
          '<li><strong>Děti:</strong> senzorické desky a kolečkové desky zlepšují koordinaci a baví.</li>'
          '<li><strong>Kancelářská práce:</strong> míč nebo podložka pod nohama aktivuje svaly během pauz.</li>'
          '<li><strong>Jóga a pilates:</strong> pomáhají s držením těla a stabilitou trupu. Přehled najdete v kategoriích <a href="/joga-a-pilates/">jóga a pilates</a> a <a href="/joga-a-podlozky/">jóga a podložky</a>.</li></ul>'
          '<h2>Jak cvičit bezpečně</h2>'
          '<p>Začněte na stabilním podkladě a pomůcku používejte u zdi nebo u pevné opory. Oboustranný stoj, pak stoj na jedné noze a postupně oči zavřené, to je přirozená cesta. Cvičte bosi nebo v protiskluzových ponožkách, protože hladká obuv na desce klouže. '
          'Vybírejte rovnou podlahu bez prahů a zajistěte dostatek místa kolem sebe. Při závratích, bolesti kloubu nebo po nedávném zranění cvičení přerušte. Délku cvičení zvyšujte po desítkách sekund, ne po minutách, aby se neunavil kotník.</p>'
          '<h2>Základní cviky</h2>'
          '<ul><li><strong>Stoj na jedné noze</strong> na podložce, 20 až 30 sekund na stranu.</li>'
          '<li><strong>Poloviční dřep</strong> na desce s oporou o zeď.</li>'
          '<li><strong>Plank</strong> na půlkouli nebo na míči pro střed těla.</li>'
          '<li><strong>Výpady do stran</strong> s klouzavým diskem pod jednou nohou.</li>'
          '<li><strong>Přenášení váhy</strong> z paty na špičku na kývavé desce.</li>'
          '<li><strong>Nášlapy</strong> na step jako zahřátí a kardio blok.</li></ul>'
          '<h2>Balanční trénink podle sportu</h2>'
          '<p>Každý sport zatěžuje trochu jiné řetězce svalů, a proto se liší i výběr pomůcky. Fotbalisté a florbalisté trénují změny směru a dopady po skoku, takže jim vyhovuje deska s mírným rozsahem a stoj na jedné noze s přihrávkou míče. '
          'Hokejisté mají při bruslení stabilitu v kotnících i bocích a rádi cvičí na půlkouli nebo na klouzavých discích, které napodobují skluz. Běžci využijí podložku pro posílení chodidla a kotníku, což doplní <a href="/bezecka-obuv/">běžecká obuv</a> s vhodným tlumením. '
          'Cvičení stability kotníků a kolen se hodí i hráčům míčových sportů, třeba <a href="/fotbal/">fotbalu</a>, <a href="/florbal/">florbalu</a> a <a href="/hokej/">hokeje</a>. Lyžaři a snowboardisté si před sezónou procvičují hluboký dřep na nestabilní ploše a kladou důraz na pomalé, kontrolované zatížení.</p>'
          '<h2>Jak zvyšovat obtížnost</h2>'
          '<p>Progrese má logiku: nejdřív pevná opora, pak žádná opora, potom zavřené oči, nakonec pohyb končetin nebo házení míče. Obtížnost se mění také výběrem pomůcky, měkčí pěna a více nafouknutá půlkoule jsou náročnější. Nepřidávejte dvě změny najednou a cvičte jen tehdy, když zvládáte předchozí stupeň čistě a bez napětí v ramenou.</p>'
          '<h2>Jednoduchá patnáctiminutová sestava</h2>'
          '<p>Pro domácí cvičení stačí malý prostor a jedna pomůcka. Začněte dvěma minutami chůze na místě nebo nášlapů na step, pak zařaďte stoj na jedné noze na podložce, vždy dvakrát po třiceti sekundách na každou stranu. '
          'Následují poloviční dřepy na desce s oporou, tři série po osmi až deseti opakováních, a plank na půlkouli, zpočátku dvacet sekund. Zakončete protažením lýtek a stehen a krátkým uvolněním kotníků. '
          'Jakmile cviky zvládáte bez opory, přidejte pohyb paží nebo míč. Zátěž zvyšujte postupně a dbejte na kvalitu pohybu, ne na počet opakování.</p>'
          '<h2>Materiál, nosnost a údržba</h2>'
          '<p>Pěna a TPE se čistí vlhkým hadrem, bez agresivních prostředků. Nafukovací pomůcky nepoužívejte na ostrém podkladu a před cvičením zkontrolujte tlak. Dřevěná deska nesmí být vystavena vlhku a plasty by neměly ležet na slunci, kde křehnou. '
          'U každé pomůcky najdete údaj o nosnosti a doporučené velikosti, který respektujte. Skladujte vodorovně nebo zavěšené, aby se pěna nedeformovala.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš náročná pomůcka na začátku, která vede ke ztrátě jistoty a zraněním.</li>'
          '<li>Cvičení v kluzké obuvi nebo na kluzké podlaze.</li>'
          '<li>Podcenění opory: bez ní se cviky neučí.</li>'
          '<li>Příliš nafouknutý míč nebo půlkoule, na které se nedá stát.</li>'
          '<li>Nákup podle barvy a ceny bez kontroly nosnosti.</li>'
          '<li>Cvičení bez zahřátí a protažení.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Rozhodněte se, zda hledáte pomůcku pro dospělého, dítě nebo seniora, a podle toho vyberte velikost a nosnost. U nafukovacích modelů hledejte v balení pumpičku. '
          'Sporteka porovnává nabídky více obchodů, takže uvidíte skladovost i dopravu, což se u rozměrnějších balíků vyplatí. Při výběru stepů a můstků sledujte i počet nastavitelných výšek. U dětských pomůcek ověřte věkové určení a to, zda jsou povrchy bezpečné a neklouzavé, a zvažte i hmotnost balení při dopravě.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr mají značky {B(("hms", "HMS"), ("sedco", "Sedco"), ("sportago", "Sportago"), ("merco", "Merco"), ("merc-sport", "Merc sport"), ("insportline", "Insportline"), ("epicstar", "Epicstar"), ("jakobs", "Jakobs"), ("lifefit", "Lifefit"), ("gymbeam", "GymBeam"), ("sharp-shape", "Sharp Shape"))}. '
          'HMS a Sedco jsou silné ve stepech a podložkách, Sportago a Merco v deskách a míčích, Epicstar v dřevěných deskách a Jakobs v senzorických pomůckách.</p>',
    faq=[('K čemu slouží balanční podložka?', 'Zlepšuje stabilitu kotníků, kolen a trupu, protože nestabilní povrch nutí hluboké svaly neustále korigovat polohu. Používá se při cvičení doma i v rehabilitaci.'),
         ('Jak často mám s balančními pomůckami cvičit?', 'Pro začátek stačí dvě až tři krátké jednotky týdně po deseti až patnácti minutách. Pomůcku můžete zařadit do zahřátí nebo na konec tréninku.'),
         ('Co je lepší, deska, nebo podložka?', 'Podložka je jednodušší a pro začátečníky bezpečnější, deska vyžaduje víc kontroly a nabízí širší škálu cviků. Mnoho lidí začne podložkou a později přidá desku.'),
         ('Jaký balanční míč zvolit podle výšky postavy?', 'Při sedu mají být kolena zhruba v pravém úhlu a chodidla na zemi. Nižší lidé volí menší průměr, vyšší větší. Údaje najdete u výrobce.'),
         ('Hodí se balanční pomůcky pro děti?', 'Ano, senzorické desky, půlkoule s výstupky a pojízdné desky podporují koordinaci a hru. Dítě má cvičit pod dohledem na rovné podlaze.'),
         ('Může balanční cvičení pomoci po zranění kotníku?', 'Často se používá v rehabilitaci, ale začátek, intenzitu a frekvenci určí lékař nebo fyzioterapeut. Sami cvičení při bolesti nezačínejte.'),
         ('Jak nafouknout půlkouli?', 'Podle návodu pumpičkou. Méně vzduchu znamená větší stabilitu, více vzduchu větší nestabilitu. Začněte méně nafouknutou a tlak zvyšujte postupně.'),
         ('K čemu je step a jak vysoký má být?', 'Slouží k aerobiku, nášlapům a posílení nohou. Začátečníci volí nižší polohu, pokročilí přidávají podložky pod konce a zvyšují zátěž.'),
         ('Jaké jsou klouzavé disky a na jakém povrchu fungují?', 'Jsou to ploché disky, které pod rukou nebo nohou kloužou. Většina modelů má jednu stranu na koberec a druhou na hladkou podlahu. Dřevěnou podlahu před poškrábáním chraňte.'),
         ('Mohu cvičit v botách?', 'Lepší je cvičit bosi nebo v protiskluzových ponožkách, protože podrážka na desce klouže a znemožňuje vnímání podkladu.'),
         ('Jak balanční pomůcky čistit?', 'Vlhkým hadrem a jemným mýdlem. Nepoužívejte rozpouštědla, nenechávejte je na slunci a před uložením nechte uschnout.')])

# ------------------------------------------------------------------ hokejove-brankarske-vybaveni
NEW['hokejove-brankarske-vybaveni'] = dict(long=True,
    title='Brankářská výstroj: masky, betony, lapačky, hokejky',
    desc='Hokejová brankářská výstroj: masky, chrániče nohou, lapačky, vyrážečky, brusle a hokejky. Jak vybrat velikost a porovnat nabídky obchodů.',
    intro='<p>Brankář je v hokeji samostatné povolání. Stojí na jediném místě, střely mu létají do těla i do hlavy a výstroj musí chránit, ale zároveň dovolit rychlý pohyb v kolenou, v bocích a v rukou. '
          'Proto se brankářské vybavení výrazně liší od výbavy hráče v poli: větší chrániče, speciální lapačka, vyrážečka, maska, brusle s jinou čepelí i hokejka s širokou lopatkou.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u brankářské výstroje od značek Bauer, Winnwell, CCM, Sherwood, Warrior, Salming nebo Opus, včetně juniorských a dětských řad. '
          'K výběru se hodí i <a href="/hokej/">hokejové vybavení</a>, <a href="/hokejove-helmy-a-mrizky/">helmy a mřížky</a>, <a href="/hokejove-brusle/">hokejové brusle</a> a <a href="/hokejove-chranice/">hokejové chrániče</a>. Níže je přehled částí výstroje, pravidla pro velikost a rady pro začátek.</p>',
    guide='<h2>Z čeho se brankářská výstroj skládá</h2>'
          '<p>Kompletní brankářská sada obsahuje deset a více částí, které na sebe navazují. Důležité je, aby se při pohybu nepřekrývaly a nevytvářely mezery. '
          'U dětí se často nakupuje po částech, protože rostou, a vybavení musí odpovídat tělesné stavbě i věkové skupině.</p>'
          + T(['Část výstroje', 'Úkol', 'Na co dát pozor'], [
              ['Maska', 'ochrana hlavy, obličeje a krku', 'velikost hlavy, typ mřížky, certifikace'],
              ['Chrániče nohou (betony)', 'ochrana nohou a pokrytí branky', 'výška podle délky nohy, tuhost, hmotnost'],
              ['Lapačka', 'chytání střel a puků', 'velikost, strana, ohebnost dlaně'],
              ['Vyrážečka', 'vyrážení a usměrnění střel', 'velikost, uvolnění zápěstí'],
              ['Náprsník a chrániče paží', 'ochrana trupu a ramen', 'střih podle hrudi, pohyblivost'],
              ['Brankářské kalhoty', 'ochrana boků a stehen', 'velikost v pase a délce'],
              ['Brusle', 'pohyb před brankou', 'tvar čepele, tuhost boty'],
              ['Hokejka', 'držení puku a zpracování střel', 'výška, úhel, strana'],
              ['Chránič krku a rozkroku', 'doplňková ochrana', 'dětské a juniorské velikosti'],
              ['Dres a spodní vrstva', 'komfort, odvod potu', 'střih, odolnost']]) +
          '<h2>Maska a chránič krku</h2>'
          '<p>Brankářská maska je jednou z nejdůležitějších částí. Nosí se buď jako kombinace plastové helmy s mřížkou, nebo jako jednodílná varianta z laminátu, často s kovovou mřížkou. '
          'Typ <strong>Cat Eye</strong> označuje mřížku s širokým výhledem a minimem vodorovných prvků v zorném poli. Velikost určujete podle obvodu hlavy, kterou změříte nad obočím. '
          'Maska má těsně sedět, nesmí se pohybovat při předklonu a nesmí tlačit na týl. Chránič krku se připíná k masce nebo nosí zvlášť a výrazně snižuje riziko zranění hrdla. U dětí je užitečný chránič krku v dětských velikostech, například modely Opus pro mládež.</p>'
          '<p>Stejné pravidlo jako u helem platí i zde: po silném zásahu nebo po prasknutí je třeba masku vyměnit. Neopravujte ji doma lepidlem a nepřemalovávejte ji, protože barva může narušit materiál. Přehled běžných helem najdete v kategorii <a href="/hokejove-helmy-a-mrizky/">hokejové helmy a mřížky</a>.</p>'
          '<h2>Chrániče nohou, kalhoty a náprsník</h2>'
          '<p>Chrániče nohou, hovorově betony, jsou největší a nejtěžší součástí výstroje. Jejich výška se měří od středu kolena po kotník, případně se vychází z délky holeně a stehna. Příliš vysoké omezují pohyb při dřepu, příliš nízké neuzavřou mezeru pod kolenem. '
          'Tuhost jádra ovlivňuje odraz puku: tvrdší jádro puk vrací rychleji, měkčí ho tlumí. Na ledě se používají jiné modely než na inline hokej nebo hokejbal, které bývají lehčí a s odlišnými popruhy. '
          'Brankářské kalhoty kryjí boky a stehna. Mají být delší a širší než kalhoty hráče a mají zakrývat horní okraje betonů. Náprsník, někdy složený z chráničů ramen, paží a hrudi, má pokrýt trup bez zbytečného objemu v podpaží. Podívejte se i na <a href="/hokejove-chranice/">chrániče hráčů</a>, abyste je nezaměnili.</p>'
          '<h2>Lapačka a vyrážečka</h2>'
          '<p>Lapačka je rukavice ve tvaru kapsy, která chytá puky. Vyrážečka je pevná ploška na druhé ruce, kterou se střely odrážejí stranou. Brankář s hokejkou v pravé ruce nosí lapačku na levé a naopak, takže verzi lapačky kupujete podle ruky, v níž držíte hokejku. '
          'Lapačku vybírejte podle obvodu a délky dlaně a vyzkoušejte, zda se zavírá bez velké námahy. Příliš tuhá se musí rozlámat, příliš měkká neochrání. U dětí je důležitější lehkost než maximální velikost. '
          'Vyrážečka se volí podle šířky ruky a hmotnosti, přičemž musí kopírovat pohyb zápěstí. Odlišné jsou i <a href="/brankarske-rukavice/">brankářské rukavice</a> pro fotbal a florbal, takže si je nepleťte. Fotbalový brankářský dres s chrániči loktů či kalhoty s vycpávkami je lehčí a patří do jiné výbavy než hokejová sada.</p>'
          '<h2>Brusle a hokejka brankáře</h2>'
          '<p>Brankářské brusle mají nižší a tužší botu, ochranný plast na přední části a rovnější čepel, která se hodí k posunům do stran. Pro brankáře není důležitá rychlost, ale stabilita ve dřepu a odolnost vůči nárazu puku. '
          'Vybírejte podle velikosti chodidla a šířky. Modely se doporučuje nechat ostřit podle brankářského profilu, což bývá méně agresivní než u hráče v poli. Přehled bruslí najdete v kategorii <a href="/hokejove-brusle/">hokejové brusle</a>.</p>'
          '<p>Brankářská hokejka má širší lopatku, silnější dolní část násady a rovnější čepel pro zakrytí ledu před brankou. Nabízí se v dětských, juniorských, intermediate a senior velikostech, v pravém i levém provedení. '
          'Pokud potřebujete vyměnit jen část, hledejte v kategoriích <a href="/hokejky/">hokejky</a> a <a href="/hokejove-cepele-a-nasady/">čepele a násady</a>. Lopatku obmotejte hokejovou páskou podle vlastního stylu, aby lépe držela puk a omezila opotřebení.</p>'
          '<h2>Velikosti: Youth, Junior, Intermediate a Senior</h2>'
          '<p>Brankářská výstroj se prodává v řadách Youth (YTH), Junior (JR), Intermediate (INT) a Senior (SR). Řady jsou dány výškou postavy a velikostí těla, a tak se mohou lišit podle výrobce. '
          'Dítě v růstu vyroste z výstroje obvykle za dvě až tři sezóny, proto se mnohé týmy dělí o použité kusy. Při koupi vždy vyzkoušejte celou sadu spolu, protože se musí překrývat bez mezer. Zkoušejte ve dřepu, v rozkroku a při zvedání paží, ne jen ve stoje.</p>'
          '<h2>Jak sestavit výbavu začínajícího brankáře</h2>'
          '<ol><li>Začněte maskou s chráničem krku, protože ochrana hlavy je nejdůležitější.</li>'
          '<li>Přidejte chrániče nohou a kalhoty, které se k sobě hodí velikostí.</li>'
          '<li>Doplňte lapačku, vyrážečku a náprsník.</li>'
          '<li>Pořiďte brusle s tuhým jazykem a brankářskou hokejku.</li>'
          '<li>Nezapomeňte na <a href="/hokejove-tasky/">hokejovou tašku</a>, která výstroj unese.</li></ol>'
          '<p>Mnoho oddílů zapůjčuje základní kusy, proto se před nákupem zeptejte trenéra. Pokud začínáte, nemusíte hned kupovat vrcholové modely, ale maska s certifikací a chránič krku patří k základu bez ohledu na úroveň hry.</p>'
          '<h2>Příprava brankáře mimo led</h2>'
          '<p>Brankář nestačí jen chytat. Potřebuje pohyblivé kyčle, silné nohy a rychlé reakce, proto se mimo led věnuje protažení a posilování. Doma se hodí gumy, balanční desky a míčky na koordinaci, například z kategorií <a href="/posilovaci-gumy/">posilovací gumy</a> a <a href="/balancni-pomucky/">balanční pomůcky</a>. '
          'Samostatně lze trénovat reakce s tenisovým míčkem o zeď a zpracování puku na zemi. Před zápasem se vyplatí důkladné rozcvičení, protože studené svaly v hlubokém dřepu snadno protestují.</p>'
          '<h2>Nastavení výstroje před zápasem</h2>'
          '<p>Správně nasazená výstroj se kontroluje zrcadlem a krátkým pohybem. Popruhy chráničů se dotahují tak, aby se noha neotáčela, ale aby šlo pohodlně ohnout koleno. Kalhoty mají zakrývat horní okraj betonů a lapačka má při zavření zůstat uvolněná. '
          'Před každým zápasem zkontrolujte upevnění mřížky, stav popruhů a čepelí bruslí, a také zda se vám v tašce nepoztrácely drobnosti. Čisté a suché vybavení vydrží déle a zlepšuje pohodlí. Pokud výstroj sdílíte s jiným brankářem, domluvte si pravidelné čištění a kontrolu popruhů, protože cizí nastavení často neodpovídá vaší postavě. Před sezónou si doma celou sadu oblékněte a zkontrolujte, zda se vše zapíná bez zbytečného tlaku.</p>'
          '<h2>Florbal, inline a street hockey</h2>'
          '<p>V kategorii se vyskytuje i výbava pro florbalové brankáře, například dresy, masky a rukavice značek Salming nebo Freez, a pro street a inline hokej, například lehčí betony. Florbalový brankář nosí méně ochrany a pohybuje se spíše po zemi, proto je výstroj lehčí. '
          'Více o hře najdete v kategoriích <a href="/florbal/">florbal</a> a <a href="/hokejove-puky-a-branky/">hokejové puky a branky</a>. Při výběru se řiďte pravidly své soutěže a doporučením trenéra.</p>'
          '<h2>Péče o brankářskou výstroj</h2>'
          '<p>Brankářská výstroj nasákne potem a vlhkostí z ledu, a proto ji po tréninku vyndejte z tašky a nechte vyschnout. Použijte stojan nebo rozložte jednotlivé části, aby se vzduch dostal i do podšívky. '
          'Nesušte na topení ani na přímém slunci, kde kůže praská a pěna křehne. Lapačku vyklepejte, popruhy zkontrolujte a pohyblivé spoje občas natřete vhodným přípravkem. Masku otřete vlhkým hadrem a mřížku kontrolujte, zda není ohnutá. '
          'Brusle po hře osušte a vložte do chráničů čepelí. Při přepravě výstroj složte tak, aby se těžké části nemačkaly na lapačku.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Kupování větší výstroje „na růst“, díky níž se chrániče posouvají a vznikají mezery.</li>'
          '<li>Zkoušení jen vestoje, ačkoliv brankář hraje ve dřepu a v rozkroku.</li>'
          '<li>Nákup masky podle designu bez ověření velikosti hlavy.</li>'
          '<li>Použití výstroje na inline hokej na ledě, nebo naopak.</li>'
          '<li>Ignorování stavu popruhů a ukládání vlhké výstroje do tašky.</li>'
          '<li>Neposouzení, zda je lapačka a vyrážečka pro správnou ruku.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr mají značky {B(("bauer", "Bauer"), ("winnwell", "Winnwell"), ("ccm", "Ccm"), ("sherwood", "Sherwood"), ("warrior", "Warrior"), ("salming", "Salming"), ("opus", "Opus"), ("hejduk", "Hejduk"), ("blindsave", "Blindsave"), ("bosport", "Bosport"), ("kipsta", "Kipsta"))}. '
          'Bauer pokrývá hokejky, masky i brusle, Winnwell sází na dostupné juniorské sady, Salming nabízí florbalovou brankářskou výstroj a Opus chrániče krku a doplňky pro mladé hráče.</p>',
    faq=[('Jak změřit velikost brankářské masky?', 'Změřte obvod hlavy nad obočím a vyberte podle tabulky výrobce. Maska musí sedět pevně, neposouvat se při předklonu a netlačit na týl.'),
         ('Jak vybrat výšku chráničů nohou?', 'Podle délky nohy od středu kolena po kotník a podle tabulky výrobce. Příliš vysoké omezují dřep, příliš nízké nechávají mezeru pod kolenem.'),
         ('Co je lapačka a co vyrážečka?', 'Lapačka je rukavice ve tvaru kapsy, která chytá puky. Vyrážečka je pevná plocha na druhé ruce, kterou střely odrážíte stranou.'),
         ('Kdy dítě vyroste z brankářské výstroje?', 'U rostoucích dětí obvykle za dvě až tři sezóny, ale záleží na růstu. Proto se často nakupuje po částech a využívá bazar.'),
         ('Jsou brankářské brusle jiné než hráčské?', 'Ano. Mají nižší a tužší botu, ochranu přední části a rovnější profil čepele, aby se lépe posouvaly do stran.'),
         ('Hodí se brankářská výstroj na florbal?', 'Ne, florbalový brankář nosí lehčí vybavení. Hokejové betony a lapačky jsou těžší a podle pravidel se v soutěži mohou lišit.'),
         ('Jak sušit brankářskou výstroj?', 'Rozložit po tréninku, nechat vyschnout na vzdušném místě mimo topení a slunce. Vlhká výstroj v tašce zapáchá a poškozuje materiál.'),
         ('Kdy vyměnit brankářskou masku?', 'Po silném zásahu, při prasknutí skořepiny nebo ohnutí mřížky, případně když přestane těsnit. Poškozenou masku neopravujte lepidlem.'),
         ('Co koupit začínajícímu brankáři jako první?', 'Masku s chráničem krku, potom chrániče nohou a kalhoty. Základní kusy si lze zapůjčit v oddíle, proto se předem zeptejte trenéra.'),
         ('Na kterou ruku nosit lapačku?', 'Na tu, kterou chytáte puky, což je obvykle opačná ruka než ta, která drží hokejku. Podle toho se kupuje pravá nebo levá verze.'),
         ('Mohu kombinovat výstroj od různých značek?', 'Ano, ale je důležité, aby se chrániče navzájem překrývaly bez mezer a aby velikosti odpovídaly. Zkoušejte celou sadu najednou.')])
