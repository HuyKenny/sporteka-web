"""sporteka.cz — wave 23e (4. 11. 2026): long texts (>= 1650 words) for elektrokolobezky, volejbalove-mice, lezecke-sedaky-a-pomucky, plovaci-vesty.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ elektrokolobezky
NEW['elektrokolobezky'] = dict(long=True,
    title='Elektrokoloběžky: dojezd, výkon, brzdy, dětské i dospělé',
    desc='Elektrokoloběžky pro dospělé i děti: jak vybrat dojezd, motor, brzdy, kola a hmotnost a porovnat nabídky českých obchodů na jednom místě.',
    intro='<p>Elektrokoloběžka je malé dopravní prostředky pro krátké trasy, kde by auto stálo v koloně a kolo by vás zpotilo. Skládá se z hliníkového rámu, malých kol, motoru v náboji, baterie v desce a displeje na řidítkách. Jednotlivé modely se ale liší víc, než by se z podobného tvaru zdálo: jiná je lehká skládací koloběžka na cestu do kanceláře, jiná těžký stroj s dvěma motory na kopce a jiná dětský model s nízkou rychlostí. Sporteka sbírá nabídky českých obchodů a pomáhá vám hledat podle značky, výkonu, dojezdu i vybavení.</p>'
          '<p>V kategorii najdete značky ' + B(('eljet', 'Eljet'), ('navee', 'Navee'), ('iscooter', 'Iscooter'), ('bluetouch', 'Bluetouch'), ('todimart', 'Todimart'), ('city-boss', 'City Boss'), ('hitway', 'Hitway'), ('joyor', 'Joyor'), ('segway', 'Segway')) +
          '. Přehled doplňují <a href="/kolobezky/">klasické koloběžky</a>, <a href="/chranice-a-helmy/">chrániče a helmy</a> a <a href="/cyklo-svetla/">světla</a>.</p>',
    guide='<h2>Jaké elektrokoloběžky se prodávají</h2>'
          '<p>Nabídka se dá rozdělit podle toho, komu je koloběžka určená a kolik toho má zvládnout. Rozdíly se projeví na hmotnosti, velikosti kol, kapacitě baterie a také na tom, jak komfortně se na ní jede po nerovném povrchu.</p>'
          + T(['Skupina', 'Typické vlastnosti', 'Hodí se pro'], [
              ['Lehké skládací modely', 'malá kola, nízká hmotnost, menší baterie', 'kombinaci s MHD, vlakem a schodištěm'],
              ['Městské dojezdové modely', 'větší baterie, 8,5 až 10 palců, světla a displej', 'každodenní dojíždění do práce nebo školy'],
              ['Výkonné terénní modely', 'silnější motor, odpružení, široké pneumatiky', 'kopcovité trasy, štěrk, delší výlety'],
              ['Dětské elektrické koloběžky', 'nízký výkon, omezená rychlost, často LED osvětlení', 'starší děti, které už jistě ovládají koloběžku'],
              ['Příslušenství', 'tašky na přepravu, náhradní díly, držáky', 'majitele, kteří koloběžku převážejí nebo servisují']]) +
          '<p>Každý typ má své kompromisy. Lehká koloběžka se snadno nosí, ale přenáší více otřesů a má menší dojezd. Těžký model jede stabilně, jenže jej do výtahu a na schody dostanete jen s námahou. Než začnete porovnávat konkrétní kusy, určete si, kde budete koloběžku nejčastěji používat a jak ji budete skladovat.</p>'
          '<h2>Dojezd a baterie</h2>'
          '<p>Dojezd je údaj, který se na první pohled porovnává nejsnáze, a zároveň ten, který nejvíc zavádí. Výrobci jej měří při stálé rychlosti na rovině s lehkým jezdcem. Ve městě s rozjezdy, semafory a kopci je skutečná vzdálenost znatelně kratší. Kapacita baterie se uvádí ve watthodinách, někdy se udává ve voltech a ampérhodinách, které se mezi sebou vynásobí.</p>'
          '<ul><li><strong>Kapacita:</strong> čím víc watthodin, tím delší dojezd při stejné spotřebě. Ověřte, zda údaj opravdu stojí v parametrech, a ne jen v marketingovém textu.</li>'
          '<li><strong>Hmotnost jezdce:</strong> těžší jezdec a batoh spotřebují víc energie, zejména v kopcích.</li>'
          '<li><strong>Teplota:</strong> v mrazu baterie ztrácí část kapacity a nabíjení v chladu jí neprospívá.</li>'
          '<li><strong>Rychlost:</strong> jízda na plný plyn dojezd výrazně zkracuje. Úsporný režim ho naopak prodlužuje.</li></ul>'
          '<p>Praktická rada: vyberte koloběžku s dojezdem aspoň o polovinu delším, než potřebujete na jednu trasu. Baterie se postupně opotřebovává a rezerva vám zajistí, že nedojedete na poslední kapky. Náhradní baterie či doplňky k napájení hledejte také v kategorii <a href="/ebike-baterie/">baterie pro elektrokola</a> a <a href="/powerbanky-a-nabijeni/">powerbanky</a>, i když se spolu nikdy nemíchají bez ověření kompatibility.</p>'
          '<h2>Motor, výkon a stoupání</h2>'
          '<p>Motor bývá vestavěný do předního nebo zadního kola. Zadní pohon dává lepší trakci při stoupání, protože se na zadní kolo přenáší váha jezdce. Přední pohon je jednodušší a levnější, ale na mokrém povrchu může prokluzovat. Některé výkonné modely mají motory dva a jsou určené do náročného terénu.</p>'
          + T(['Výkon motoru', 'Co můžete očekávat'], [
              ['do 250 W', 'rovinaté město, mírné sklony, nižší spotřeba'],
              ['350 až 500 W', 'běžné městské kopce, svižnější rozjezd'],
              ['nad 500 W', 'strmější stoupání, těžší jezdci, výlety mimo asfalt'],
              ['dva motory', 'maximální tah, ale vyšší hmotnost a spotřeba']]) +
          '<p>Jmenovitý výkon se liší od špičkového a údaje se mezi značkami porovnávají obtížně. Při výběru se proto soustřeďte i na maximální stoupavost a na to, zda ovladač hladce navyšuje plyn. Trhavý rozjezd je nepříjemný a na mokré dlažbě nebezpečný.</p>'
          '<h2>Kola, pneumatiky a odpružení</h2>'
          '<p>Velikost kol zásadně ovlivňuje pohodlí. Malá kola o průměru kolem osmi palců jsou lehká a obratná, jenže se bořící do spár v dlažbě a do prohlubní. Kola od deseti palců jsou stabilnější a lépe zvládají kolejnice nebo obrubníky. Nejčastěji se setkáte se třemi řešeními.</p>'
          '<ul><li><strong>Vzduchové pneumatiky:</strong> pohodlné a přilnavé, ale mohou se píchnout a vyžadují hlídání tlaku. Pumpu a lepení najdete mezi <a href="/cyklo-pumpy-a-naradi/">pumpami a nářadím</a>.</li>'
          '<li><strong>Plné pneumatiky:</strong> odolné proti defektu a bez údržby, jenže tvrdší a hlučnější.</li>'
          '<li><strong>Bezdušové pneumatiky:</strong> kombinují komfort se samotěsnicí tekutinou, jejich servis je ale náročnější.</li></ul>'
          '<p>Odpružení se vyplatí u delších tras po dlažbě a štěrku. Pružina nebo tlumič na přední vidlici a zadní kolo tlumí nárazy a zlepšují kontrolu, zároveň ale přidávají hmotnost a díly, které se opotřebovávají.</p>'
          '<h2>Brzdy a bezpečnost</h2>'
          '<p>Brzdy jsou důležitější než výkon motoru. U elektrokoloběžek se používají tři principy: kotoučová brzda, bubnová brzda a elektronická brzda motoru, která brzdí zpětným chodem. Nejlepší jsou modely, které kombinují mechanickou brzdu s elektronickou, protože při selhání jednoho systému zůstane druhý.</p>'
          '<ul><li><strong>Světla a odrazky:</strong> přední světlo, zadní červené světlo a brzdové světlo patří k základu. Doplnit je můžete o nástavné <a href="/cyklo-svetla/">cyklistické světlo</a>.</li>'
          '<li><strong>Zvonek:</strong> hodí se zejména tam, kde se jezdí mezi chodci. Zvonky najdete v <a href="/cyklo-zvonky-a-zrcatka/">kategorii zvonků a zrcátek</a>.</li>'
          '<li><strong>Helma:</strong> pevná přilba je nejdůležitější ochrana hlavy. Vybírejte z <a href="/cyklisticke-helmy/">cyklistických helem</a> nebo z <a href="/chranice-a-helmy/">kategorie chráničů a helem</a>.</li>'
          '<li><strong>Rukavice:</strong> při pádu chrání dlaně, viz <a href="/sportovni-rukavice/">sportovní rukavice</a>.</li></ul>'
          '<h2>Hmotnost, nosnost a skládání</h2>'
          '<p>Hmotnost rozhoduje o tom, jak často budete koloběžku nosit. Do vlaku nebo do bytu ve třetím patře se hodí kus, který zvednete jednou rukou. Zároveň dbejte na nosnost. Výrobce uvádí maximální zatížení, které zahrnuje jezdce i batoh. Překračovat ho nemá smysl, protože se zkracuje dojezd, namáhá rám i motor a brzdná dráha se prodlužuje.</p>'
          '<p>Skládací mechanismus je citlivé místo. Zkontrolujte, zda zámek pevně drží a nehraje, protože právě tady vzniká nejvíc závad. U modelů, které budete skládat denně, zvolte jednoduchý a rychlý systém. Pokud potřebujete převážet koloběžku autem nebo letadlem, hodí se přepravní taška, kterou v kategorii občas najdete. Podobné potřeby řeší i <a href="/skladaci-elektrokola/">skládací elektrokola</a>.</p>'
          '<h2>Dětské elektrické koloběžky</h2>'
          '<p>Dětské modely mají omezený výkon a rychlost, často i osvětlení a jednoduché ovládání. Jsou určené pro starší děti, které už samy bezpečně stojí na klasické koloběžce, umí zabrzdit a rozumějí základním pravidlům provozu. Pro malé děti je lepší <a href="/odrazedla/">odrážedlo</a> nebo klasická dětská koloběžka. Značky ' + B(('eljet', 'Eljet'), ('iscooter', 'Iscooter')) + ' tuto skupinu zastupují nejvíc.</p>'
          '<p>Rodiče by měli hlídat rychlost, brzdy a helmu. Elektrický pohon děti láká k jízdě, která je rychlejší, než zvládnou, a při pádu mají kratší reakční čas než dospělí. Dohlížejte, kde jezdí, a vybavte je kompletní ochranou, tedy helmou, chrániči loktů a kolen a rukavicemi.</p>'
          '<h2>Pravidla provozu a pojištění</h2>'
          '<p>Provoz elektrokoloběžek na komunikacích se řídí zákonem o provozu na pozemních komunikacích a pravidla se v čase upravují. Obecně platí, že vozidla s omezeným výkonem a rychlostí mají podobný režim jako kolo, výkonnější stroje už vyžadují registraci, pojištění či řidičské oprávnění. Přesné limity a povinnosti si před koupí ověřte na stránkách ministerstva dopravy nebo u obecního úřadu.</p>'
          '<p>Na chodnících se obvykle jezdí pouze s ohledem na chodce a v pěších zónách platí odlišné podmínky. Za škodu způsobenou při jízdě odpovídá jezdec, proto zvažte pojištění odpovědnosti. Informace o něm najdete u pojišťoven a často stačí rozšířit existující pojištění domácnosti.</p>'
          '<h2>Údržba a skladování</h2>'
          '<ul><li><strong>Baterie:</strong> nenechávejte ji dlouhodobě úplně vybitou ani nabitou na maximum. Při delší pauze ji skladujte částečně nabitou a v suchu.</li>'
          '<li><strong>Nabíječka:</strong> používejte originální. Nevhodná nabíječka může poškodit baterii a způsobit požár.</li>'
          '<li><strong>Pneumatiky:</strong> před jízdou zkontrolujte tlak a stav dezénu.</li>'
          '<li><strong>Brzdy:</strong> pravidelně prověřujte opotřebení destiček a seřízení lanek.</li>'
          '<li><strong>Čištění:</strong> otírejte vlhkým hadrem. Proudem vody pod tlakem nemiřte na motor, konektory a displej.</li>'
          '<li><strong>Zabezpečení:</strong> koloběžku zamykejte. Vhodné <a href="/cyklo-zamky/">zámky</a> najdete mezi cyklistickým příslušenstvím.</li></ul>'
          '<h2>Co dalšího k pohybu po městě</h2>'
          '<p>Elektrokoloběžka není jediná možnost. Pokud potřebujete větší dojezd nebo přepravu nákladu, podívejte se na <a href="/mestska-elektrokola/">městská elektrokola</a>. Chcete-li jezdit bez motoru, vyberte klasickou <a href="/kolobezky/">koloběžku</a>, na triky pak <a href="/freestyle-kolobezky/">freestyle koloběžku</a>. Pro sportovní vyžití bez baterie se hodí také <a href="/inline-brusle/">inline brusle</a> nebo <a href="/skateboardy/">skateboard</a>. Do batohu na cestu pak pomůže <a href="/mestske-batohy/">městský batoh</a> a při dešti <a href="/nepromokave-bundy/">nepromokavá bunda</a>.</p>'
          '<h2>Na co se zaměřit u nabídek obchodů</h2>'
          '<p>Stejný model se u různých prodejců liší v délce záruky, ve vybavení v balení a v dostupnosti náhradních dílů. Zeptejte se, zda je k dispozici autorizovaný servis a jak dlouho se čeká na výměnu baterie nebo ovladače. Zkontrolujte, zda je v návodu česky popsané ovládání, nabíjení a bezpečnostní upozornění. Malé koloběžky bez značky se často prodávají bez servisního zázemí, což se při první závadě projeví jako zbytečný problém. Sporteka vám ukáže více nabídek vedle sebe, takže snadno srovnáte i obchody a dostupnost.</p>'
          '<h2>Jak postupovat při výběru</h2>'
          '<ol><li>Spočítejte si délku nejdelší pravidelné trasy a přidejte rezervu.</li>'
          '<li>Určete maximální hmotnost, kterou unesete na schodech.</li>'
          '<li>Rozhodněte se podle povrchu mezi vzduchovými a plnými pneumatikami.</li>'
          '<li>Vyžadujte kvalitní brzdy, světla a pevný rám.</li>'
          '<li>Porovnejte nabídky obchodů včetně záruky a servisu a nezapomeňte na ochranné pomůcky.</li></ol>',
    faq=[('Jaký dojezd elektrokoloběžky je pro město dostačující?', 'Záleží na délce trasy. Na krátké cesty do deseti kilometrů stačí menší baterie, na dojíždění po celém městě se hodí větší s rezervou. Skutečný dojezd bývá kratší než ten uvedený výrobcem.'),
         ('Jaký výkon motoru zvolit?', 'Na rovinu stačí slabší motor, do kopců a pro těžšího jezdce hledejte vyšší výkon. Dívejte se také na stoupavost uvedenou v parametrech.'),
         ('Jsou lepší vzduchové, nebo plné pneumatiky?', 'Vzduchové pneumatiky jsou pohodlnější, plné nevyžadují údržbu a nepíchnou se. Na dlažbě a štěrku dává smysl vzduch, na hladký asfalt a pohodlí bez starostí plné kolo.'),
         ('Jaké brzdy mají elektrokoloběžky?', 'Nejčastěji kotoučové, bubnové a elektronické. Nejbezpečnější je kombinace mechanické a elektronické brzdy.'),
         ('Musím mít při jízdě helmu?', 'Povinnost se odvíjí od věku a platných předpisů, ale ochrana hlavy je rozumná vždy. Děti by měly helmu nosit pokaždé.'),
         ('Hodí se elektrokoloběžka do MHD a vlaku?', 'Ano, skládací a lehčí modely se běžně vejdou do veřejné dopravy. Přepravní podmínky ale určuje dopravce, proto si je ověřte předem.'),
         ('Jak dlouho se nabíjí baterie?', 'Obvykle několik hodin podle kapacity a výkonu nabíječky. Přesný čas najdete v návodu, nabíjejte vždy s originální nabíječkou.'),
         ('Jak o baterii pečovat v zimě?', 'Skladujte ji v teple, nenabíjejte promrzlou a po dlouhé pauze ji před uložením nabijte jen částečně. V mrazu je dojezd kratší.'),
         ('Hodí se elektrokoloběžka pro děti?', 'Pro starší děti, které bezpečně ovládají klasickou koloběžku, ano. Vybírejte model s omezenou rychlostí, dobrými brzdami a vždy s helmou.'),
         ('Jak předejít krádeži koloběžky?', 'Zamykejte ji pevným zámkem k pevnému bodu a nenechávejte ji venku přes noc. Odnímatelnou baterii a klíč berte s sebou.'),
         ('Jaká je nosnost běžné elektrokoloběžky?', 'U dospělých modelů bývá nosnost vyšší než u dětských. Vždy počítejte s vlastní váhou i batohem a nepřekračujte údaj výrobce.')],
)

# ------------------------------------------------------------------ volejbalove-mice
NEW['volejbalove-mice'] = dict(long=True,
    title='Volejbalové míče a sítě: hala, beach, děti, soutěže',
    desc='Volejbalové míče a sítě pro halu, pláž, sníh i děti. Jak vybrat velikost, povrch, šití a síť a porovnat nabídky českých obchodů.',
    intro='<p>Volejbalový míč je lehký, ale citlivý nástroj: rozdíl mezi tréninkovým kusem na zahradu a soutěžním míčem je znát při podání, příjmu i smeči. Kategorie sdružuje míče pro halu, pláž a sníh, měkké míče pro děti a začátečníky a také sítě, kterými si hřiště zřídíte na hřišti, zahradě nebo písku. Sporteka porovnává nabídky českých obchodů, takže snadno zjistíte, kde je ten váš model skladem.</p>'
          '<p>Z výrobců tu narazíte hlavně na ' + B(('mikasa', 'Mikasa'), ('gala', 'Gala'), ('molten', 'Molten'), ('kipsta', 'Kipsta'), ('merco', 'Merco'), ('mondo', 'Mondo'), ('spokey', 'Spokey'), ('avento', 'Avento'), ('sittec', 'Sittec')) +
          '. Širší výběr pro sportovce najdete v rubrice <a href="/volejbal/">volejbal</a> a mezi <a href="/micove-sporty/">míčovými sporty</a>.</p>',
    guide='<h2>Jaké typy míčů a sítí najdete</h2>'
          '<p>Volejbalový míč se vybírá podle prostředí a úrovně hráčů. Halový míč musí mít jemný povrch a stabilní let, plážový snese vítr, písek a slunce, sněhový je zesílený pro nízké teploty a děti potřebují lehčí a měkčí kus, který neubližuje rukám. Vedle míčů se v kategorii prodávají i sítě a další vybavení potřebné ke hře.</p>'
          + T(['Typ zboží', 'Čím se vyznačuje', 'Hodí se pro'], [
              ['Halový soutěžní míč', 'jemná syntetická kůže, tvrdší šití nebo lepení, stabilní tlak', 'kluby, školní soutěže, tréninky v tělocvičně'],
              ['Halový rekreační míč', 'odolnější povrch, mírná cena, širší tolerance', 'školy, kroužky, hra s přáteli'],
              ['Plážový míč', 'větší obvod, nižší tlak, voděodolný povrch', 'beachvolejbal, kemp, hřiště s pískem'],
              ['Sněžný míč', 'výrazné barvy, zesílený povrch', 'zimní turnaje, hra venku na sněhu'],
              ['Měkký a dětský míč', 'lehčí, pěnová nebo měkká vrstva', 'začátečníky, mini volejbal, malé děti'],
              ['Sítě', 'pevné lano, ocelové nebo plastové oka', 'tělocvičny, hřiště, zahrady, beach kurty']]) +
          '<p>Rozhodnout se můžete také podle toho, kolik času bude míč trávit venku. Pokud na něm hrajete denně v hale, vyplatí se kvalitnější model. Pro odlehlou chatu nebo pláž stačí jednodušší plážový kus, který bez problémů snese písek a vlhkost.</p>'
          '<h2>Velikost, hmotnost a tlak</h2>'
          '<p>Standardní míč pro dospělé a mládež od určitého věku má velikost pět, obvod zhruba 65 až 67 centimetrů a hmotnost přibližně 260 až 280 gramů. Beachvolejbalové míče mají obvod trochu větší a nižší tlak vzduchu, díky čemuž se při letu chovají jinak a hůř se odrážejí. Pro mladší děti a začátečníky se prodávají lehčí míče, které jsou na dotek měkčí a snižují riziko bolesti předloktí.</p>'
          '<ul><li><strong>Správný tlak:</strong> příliš nafouknutý míč tvrdě odskakuje, příliš měkký se nesprávně chová při podání. Tlak prověřujte tlakoměrem a nafukujte jehlou. Pumpy najdete v rubrice <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</li>'
          '<li><strong>Hmotnost:</strong> těžší míč zvyšuje namáhání prstů a zápěstí, lehčí letí nestabilně. Dodržujte doporučení pro věkovou kategorii.</li>'
          '<li><strong>Značení:</strong> na míči i na obalu hledejte údaje o tlaku, velikosti a určení pro halu či pláž.</li></ul>'
          '<h2>Povrch, konstrukce a šití</h2>'
          '<p>Rozdíl mezi levnými a drahými míči se projeví hlavně v konstrukci. Soutěžní míče jsou lepené z 18 panelů, které se přilepují na vnitřní komoru. Takový míč má stabilní tvar a letí rovně. Rekreační míče bývají šité nebo laminované, jsou odolnější a vydrží i drsnější povrch.</p>'
          + T(['Konstrukce', 'Výhoda', 'Nevýhoda'], [
              ['Lepené panely', 'přesný tvar, jemný dotek, vyvážený let', 'citlivější na drsný povrch'],
              ['Šité panely', 'odolnost, delší životnost', 'pevnější, na dotek tvrdší'],
              ['Laminované panely', 'rovnoměrný povrch, snadná údržba', 'méně jemný pocit při hře'],
              ['Pěnová vrstva', 'měkký dopad, bezpečnost pro děti', 'nehodí se na soutěže']]) +
          '<p>Povrch rozhoduje o tom, jak míč drží na prstech a jak snáší pot a vlhkost. Syntetická kůže je nejběžnější. Mikrovlákno poskytuje příjemný pocit a lepší přilnavost, ale vyžaduje opatrnější zacházení. Pokud míč budete používat na pláži, vybírejte voděodolné varianty.</p>'
          '<h2>Výběr podle věku a úrovně</h2>'
          '<ul><li><strong>Děti do osmi let:</strong> měkké a lehké míče, které se dají chytit i bez techniky. Hrát je možné i v nafukovacím provedení, podobně jako u <a href="/nafukovaci-hracky/">nafukovacích hraček</a>.</li>'
          '<li><strong>Mládež a mini volejbal:</strong> míč s mírně sníženou hmotností, který umožňuje trénovat správnou techniku odbití.</li>'
          '<li><strong>Školy a kroužky:</strong> odolný laminovaný míč, který vydrží intenzivní provoz a nepotřebuje péči.</li>'
          '<li><strong>Kluby a soutěže:</strong> míč, který odpovídá pravidlům dané soutěže. Zeptejte se trenéra, který typ se používá, abyste trénovali na stejném.</li>'
          '<li><strong>Rekreace s přáteli:</strong> univerzální míč pro hřiště nebo kemp, který snese vnější vlivy.</li></ul>'
          '<h2>Volejbalové sítě a hřiště</h2>'
          '<p>Síť je druhá polovina výbavy a často se podceňuje. Rozměry hřiště pro dospělé jsou 18 krát 9 metrů, výška sítě u mužů 2,43 metru a u žen 2,24 metru. Pro děti a mládež se síť snižuje podle věku. Při výběru sítě sledujte šířku, délku, materiál oček a způsob napínání.</p>'
          '<ul><li><strong>Uzlová síť:</strong> pevná a odolná, hodí se do tělocvičen i na hřiště.</li>'
          '<li><strong>Beachvolejbalová síť:</strong> odolná proti UV záření a vlhkosti, často s popruhem pro rychlé napnutí.</li>'
          '<li><strong>Zahradní sada:</strong> síť s tyčemi a kolíky pro rekreační hru, rychle se staví i skládá. Další tipy najdete v rubrice <a href="/hry-na-zahradu/">hry na zahradu</a>.</li>'
          '<li><strong>Doplňky:</strong> antény, lanka, pásky a obaly. U trvalých hřišť s pevnými sloupky se zeptejte na kompatibilitu.</li></ul>'
          '<p>Při stavbě sítě venku dbejte na stabilitu sloupků. Silný vítr dokáže vyvrátit i dobře zatížené tyče, a pokud se síť uvolní, může zranit hráče. Zajistěte kotvení a před deštěm síť radši sundejte.</p>'
          '<h2>Značky a jejich zaměření</h2>'
          '<p>Značky v kategorii se liší zaměřením. ' + B(('mikasa', 'Mikasa'), ('molten', 'Molten')) + ' jsou spojené se soutěžními míči a oficiálními turnaji. ' + B(('gala', 'Gala')) + ' nabízí široký rozsah od tréninkových míčů po sety pro školy. ' + B(('kipsta', 'Kipsta')) + ' a ' + B(('avento', 'Avento')) + ' cílí na rekreační hráče a kluby s menším rozpočtem. ' + B(('merco', 'Merco'), ('spokey', 'Spokey'), ('mondo', 'Mondo')) + ' zastupují cenově dostupné míče a zahradní sady. U sítí se objevují ' + B(('sittec', 'Sittec'), ('pokorny-site', 'Pokorný sítě')) + ', které se zaměřují na materiály a provedení pro hřiště.</p>'
          '<h2>Péče o míč</h2>'
          '<ul><li>Po hře míč očistěte vlhkým hadříkem a nechte přirozeně uschnout. Nesušte ho u radiátoru.</li>'
          '<li>Neskladujte ho na slunci ani v mrazu, kde se materiál smršťuje a křehne.</li>'
          '<li>Před delším uložením mírně sundejte vzduch, aby se komora zbytečně nenamáhala.</li>'
          '<li>Při nafukování používejte navlhčenou jehlu a nezasouvejte ji křivě, ventil se snadno poškodí.</li>'
          '<li>Míč, který se dostal do písku, otřete suchým hadrem, abyste neopotřebovali povrch.</li></ul>'
          '<h2>Další vybavení pro volejbal</h2>'
          '<p>Hráči potřebují kromě míče vhodnou obuv, chrániče a oblečení. Do haly se hodí lehká <a href="/sportovni-obuv/">sportovní obuv</a> s dobrou přilnavostí, při problémech s kotníky pomůže <a href="/bandaze-a-ortezy/">bandáž nebo ortéza</a>. Týmové <a href="/dresy/">dresy</a>, <a href="/sportovni-kratasy/">kraťasy</a> a <a href="/sportovni-ponozky/">ponožky</a> usnadní zápasy a na pláž přidejte <a href="/plazove-doplnky/">plážové doplňky</a>. Pro jiné míčové hry si prohlédněte <a href="/basketbalove-mice/">basketbalové</a>, <a href="/fotbalove-mice/">fotbalové</a> a <a href="/ostatni-micove-sporty/">další míčové sporty</a>, případně <a href="/hazena/">házenou</a>.</p>'
          '<h2>Jak se míč chová při jednotlivých herních činnostech</h2>'
          '<p>Při podání shora se projeví vyvážení míče. Kvalitní míč letí s minimální rotací a mírným kolísáním, což dělá podání nevyzpytatelným. Levnější míč se naopak chová nerovnoměrně a jeho dráha je hůř předvídatelná. Při příjmu na spodní odbití záleží na tvrdosti povrchu a na tlaku. Příliš tvrdý míč se odráží od předloktí nepředvídatelně a zanechává červené stopy na pažích, což začátečníky rychle odradí. Při prstovém odbití hraje roli přilnavost a jemnost materiálu, protože prsty potřebují míč ucítit a tvarovat jeho dráhu.</p>'
          '<p>Smeč zatěžuje míč nejvíc. Soutěžní kusy jsou stavěné tak, aby se při silném úderu nedeformovaly a neztrácely tvar, a proto je trenéři vyžadují i na tréninku. Pokud trénujete jen rekreačně, stačí odolnější model, který vydrží opakované údery o zem a stěnu.</p>'
          '<h2>Mini volejbal, školy a kroužky</h2>'
          '<p>Děti se začínají učit hrát nejčastěji v tělocvičnách a na školních hřištích. Zde dává smysl kombinace lehčího míče, nižší sítě a menšího hřiště, aby se děti naučily správným pohybům bez zbytečné námahy. Učitelé a trenéři ocení míče, které snášejí intenzivní provoz a nepotřebují zvláštní péči. Pokud nakupujete pro více dětí, zvažte pořízení několika kusů s různou tvrdostí, aby si každý našel ten svůj. Při výběru berte v úvahu také barvu: výrazné kombinace usnadňují sledování letu míče, což pomáhá hlavně začátečníkům.</p>'
          '<h2>Hra mimo hřiště: kemp, pláž a zahrada</h2>'
          '<p>Při rekreační hře na pláži je největším nepřítelem písek, který se dostává do povrchu a ničí ho. Plážové míče mají proto povrch, který písek snáší, a po hře stačí míč opláchnout čistou vodou a osušit. Na zahradě hrozí hlavně poškození o keře, plot a hrany. Zde se vyplatí levnější a odolný míč, který nemusíte chránit. Pokud hrajete v kempu, uložte míč před nocí do stanu nebo do auta, aby ho nezničila vlhkost a rosa.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Volba plážového míče do haly nebo naopak. Každý se chová jinak a hrát se s ním nebude dobře.</li>'
          '<li>Pořízení těžkého míče pro děti, které pak mají bolavé ruce a ztrácejí chuť hrát.</li>'
          '<li>Koupě sítě bez ohledu na rozměry hřiště.</li>'
          '<li>Podcenění tlaku vzduchu. Nový míč bývá dodán s malým množstvím vzduchu a musíte ho dofouknout.</li>'
          '<li>Přehlédnutí určení míče, takže se používá venku, přestože je určený na halu.</li></ul>'
          '<h2>Jak vybrat v pěti krocích</h2>'
          '<ol><li>Určete prostředí hry: hala, pláž, zahrada nebo sníh.</li>'
          '<li>Vyberte velikost a hmotnost podle věku hráčů.</li>'
          '<li>Zvolte konstrukci podle intenzity používání.</li>'
          '<li>Pokud stavíte hřiště, změřte plochu a vyberte síť s odpovídajícími rozměry.</li>'
          '<li>Porovnejte nabídky obchodů, skladovou dostupnost a podmínky vrácení.</li></ol>',
    faq=[('Jakou velikost volejbalového míče koupit?', 'Pro dospělé a starší mládež velikost pět. Pro děti a začátečníky existují lehčí a měkčí míče, které se lépe chytají a odbíjejí.'),
         ('Čím se liší halový a plážový míč?', 'Plážový má větší obvod, nižší tlak a voděodolný povrch. Halový je menší, tvrdší a má jemnější dotek, ale venku rychle ztrácí kvalitu.'),
         ('Lze halový míč používat venku?', 'Rekreačně ano, ale povrch se na asfaltu a v písku rychle ničí. Pro venkovní hru je lepší plážový nebo odolný rekreační míč.'),
         ('Jak správně nafouknout volejbalový míč?', 'Použijte navlhčenou jehlu a tlakoměr a držte se tlaku doporučeného výrobcem. Příliš tvrdý míč bolí, příliš měkký špatně letí.'),
         ('Jak vybrat míč pro děti?', 'Zvolte lehký a měkký míč, případně mini volejbal. Dětem nesedí těžký soutěžní model a nemají dostatek síly na správné odbití.'),
         ('Jaká je výška volejbalové sítě?', 'U mužů 2,43 metru a u žen 2,24 metru. Pro děti a mládež se síť snižuje podle věkové kategorie.'),
         ('Jak se starat o volejbalový míč?', 'Čistěte ho vlhkým hadříkem, sušte při pokojové teplotě a neskladujte ho na slunci ani v mrazu. Před dlouhým uložením trochu spusťte vzduch.'),
         ('Je lepší lepený, nebo šitý míč?', 'Lepený je přesnější a jemnější, šitý je odolnější. Na soutěže a trénink volte lepený, na školy a rekreaci šitý nebo laminovaný.'),
         ('Co potřebuji k zahradnímu volejbalu?', 'Míč, síť, tyče nebo kůly a pevné kotvení. Přesné rozměry přizpůsobte velikosti zahrady a věku hráčů.'),
         ('Existují míče pro hru na sněhu?', 'Ano, sněhové míče mají výrazné barvy a zesílený povrch. Hodí se na zimní turnaje, ale normální míč na sníh nepoužívejte.'),
         ('Kdy míč vyměnit?', 'Když se odlupují panely, míč neudrží tlak nebo letí nepravidelně. Při rekreační hře vydrží několik sezón, u klubů se mění častěji.')],
)

# ------------------------------------------------------------------ lezecke-sedaky-a-pomucky
NEW['lezecke-sedaky-a-pomucky'] = dict(long=True,
    title='Lezecké sedáky, přilby, magnézium a jisticí pomůcky',
    desc='Lezecké sedáky, přilby, pytlíky na magnézium, jisticí a slaňovací pomůcky. Jak vybrat podle stylu lezení a porovnat nabídky obchodů.',
    intro='<p>Mezi lezeckým lanem a botami je celá řada věcí, které rozhodují o bezpečí i pohodlí: sedák, přilba, jisticí zařízení, smyčky, pytlík na magnézium nebo pouzdro na lano. Tato kategorie sdružuje právě takové vybavení pro skalní lezení, sportovní lezení ve stěně, ferraty i práci ve výšce. Najdete tu také magnézium v kostkách, sypké i tekuté, a občas doplňky, které s lezením nesouvisejí, třeba magnéziová křesadla na rozdělávání ohně. Sporteka porovnává nabídky obchodů a pomáhá filtrovat podle značky a typu.</p>'
          '<p>Z výrobců se v nabídce objevují ' + B(('hms', 'HMS'), ('ocun', 'Ocún'), ('simond', 'Simond'), ('black-diamond', 'Black Diamond'), ('singing-rock', 'Singing Rock'), ('petzl', 'Petzl'), ('direct-action', 'Direct Action'), ('s-t-condor', 'S.t. Condor')) +
          '. Základ vybavení doplní <a href="/lezecke-boty/">lezečky</a> a <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>.</p>',
    guide='<h2>Co všechno kategorie obsahuje</h2>'
          '<p>Vybavení pro lezení se obecně dělí na osobní jistící prostředky, ochranu hlavy, pomůcky pro zlepšení úchopu a doplňky pro manipulaci s lanem. Některé kusy fungují jako životně důležité, jiné jen zpříjemňují lezení. Rozlišování mezi nimi je důležité i při nákupu, protože na bezpečnosti se nešetří.</p>'
          + T(['Skupina', 'Příklady', 'K čemu slouží'], [
              ['Sedáky', 'sportovní, celotělové, dětské, ferratové', 'připojení lezce k lanu a jištění'],
              ['Přilby', 'skalní, horolezecké, dětské', 'ochrana hlavy před kameny a nárazy'],
              ['Jisticí a slaňovací pomůcky', 'tuby, brzdy s asistencí, osmy', 'jištění partnera a kontrolované slaňování'],
              ['Smyčky a expresky', 'expresky, textilní smyčky, spojky', 'propojení jistících bodů a lana'],
              ['Magnézium a pytlíky', 'kostky, sypké, tekuté, chalk bagy', 'suché ruce a lepší úchop'],
              ['Pouzdra a vaky', 'lýtkové pouzdro, pytel na lano', 'přeprava a manipulace s lanem']]) +
          '<p>Sedák, přilba a jisticí zařízení patří do osobních ochranných prostředků. Musí být označené značkou CE a splňovat příslušné předpisy. Magnézium nebo pytlík na něj bezpečnostní funkci nemají, jenom vylepšují komfort. Při nákupu proto vždy rozlišujte, co kupujete do rukou a co na tělo.</p>'
          '<h2>Lezecký sedák: jak vybrat</h2>'
          '<p>Sedák je spojení mezi vámi a lanem. Má pevně sedět na pase a stehnech, nesmí tlačit a nesmí se při pádu sesunout. Správná velikost je důležitější než značka. Při zkoušení stojte, pak se zavěste do sedáku a ověřte, jak drží. Sedák musí zůstat na pase a nesmí sklouznout přes kyčle.</p>'
          '<ul><li><strong>Sportovní sedák:</strong> lehký, s minimem vycpávky, určený pro stěnu a skalní cesty, kde se hodně padá, visí a odpočívá v laně.</li>'
          '<li><strong>Víceúčelový sedák:</strong> silnější vycpávka na pasu a stehnech, vhodný pro dlouhé cesty a slaňování.</li>'
          '<li><strong>Celotělový sedák:</strong> pro malé děti a při práci, kde hrozí převrácení.</li>'
          '<li><strong>Ferratový set:</strong> sedák doplněný absorbérem a ramenními popruhy. Další výbavu najdete v kategorii <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>.</li>'
          '<li><strong>Nastavitelné nohavice:</strong> usnadňují oblékání přes zimní oblečení a kalhoty s odlišnými objemy.</li></ul>'
          '<p>Vedle velikosti se dívejte na počet a umístění materiálových smyček pro vybavení. Ženy často volí sedáky s odlišným střihem, který lépe sedí na boky. Děti potřebují modely s menšími rozměry a pevným spojením mezi pasem a nohavicemi.</p>'
          '<h2>Lezecká přilba</h2>'
          '<p>Přilba chrání hlavu před padajícími kameny a před nárazem při pádu. Ve skalách, kde je riziko pádu předmětů, je prakticky nutností. Ve stěně ji často nosí děti a začátečníci. Přilba má sedět pevně, nesmí se pohybovat do stran a nesmí zakrývat výhled. Popruhy utáhněte tak, aby pod bradou držely bez tlaku.</p>'
          '<ul><li><strong>Tvrdá skořepina:</strong> trvanlivá, odolná vůči poškrábání a nárazům, těžší.</li>'
          '<li><strong>Pěnová přilba s tenkým obalem:</strong> lehká a větraná, vhodná na sportovní lezení, ale citlivější na mechanické poškození.</li>'
          '<li><strong>Ventilace:</strong> otvory pomáhají za horka, zároveň však snižují odolnost proti ostrým předmětům.</li>'
          '<li><strong>Přichycení čelovky:</strong> praktické háčky držící svítilnu. Svítilny najdete v kategorii <a href="/celovky-a-svitilny/">čelovky a svítilny</a>.</li></ul>'
          '<p>Po silném nárazu přilbu vyřaďte, i když na ní nejsou vidět stopy. Pěnová hmota se mohla poškodit zevnitř. Při hledání alternativ se podívejte i do širší kategorie <a href="/chranice-a-helmy/">chráničů a helem</a>.</p>'
          '<h2>Jisticí a slaňovací pomůcky</h2>'
          '<p>Jisticí zařízení brzdí lano při pádu a umožňuje kontrolované spouštění. Základní tuba je jednoduché a lehké zařízení, jehož funkce závisí na správné technice. Jistítko s asistovaným brzděním pomáhá zachytit pád lezce, ale nenahrazuje pozornost jistícího a správnou techniku. Slaňovací zařízení se používá k bezpečnému sestupu na laně.</p>'
          + T(['Zařízení', 'Výhoda', 'Pozor na'], [
              ['Tuba (jednoduchá)', 'lehká, univerzální, levná', 'vyžaduje správnou techniku a pozornost jistícího'],
              ['Brzda s asistencí', 'zablokuje lano při pádu, pomáhá při jištění', 'těžší, vyžaduje trénink obsluhy'],
              ['Osmička', 'rychlé slaňování, jednoduchá konstrukce', 'zkrucuje lano, nevhodná na jištění'],
              ['Slaňovací brzda', 'plynulé spouštění, vhodná pro práce ve výšce', 'určená pro konkrétní průměry lan']]) +
          '<p>Každé zařízení má omezený rozsah průměrů lana, se kterým funguje. Proto si před nákupem ověřte, jaké lano používáte, a čtěte návod. Správné používání se neučí z internetu, ale na kurzu s instruktorem, kde si ho můžete vyzkoušet pod dohledem.</p>'
          '<h2>Expresky, smyčky a spojky</h2>'
          '<p>Expresky tvoří dvě karabiny spojené krátkou textilní smyčkou. Používají se k zavěšování lana do jistících bodů a ke sportovnímu lezení jsou nezbytné. Smyčky z textilu se hodí k prodloužení, k vytváření postupů a k vlastnímu jištění. Při výběru se zaměřte na materiál, pevnost a snadnou manipulaci s karabinami, zejména v rukavicích.</p>'
          '<ul><li>Kratší expresky se hodí na strmé cesty, delší na zakřivené, kde se lano nesmí zahýbat.</li>'
          '<li>Textilní smyčky kontrolujte před každým použitím, zda nejsou ožmoulané a nepoškozené UV zářením.</li>'
          '<li>Spojky a karabiny neskladujte pohromadě s chemikáliemi a rozpouštědly.</li></ul>'
          '<h2>Magnézium a pytlíky na magnézium</h2>'
          '<p>Magnézium zbavuje ruce potu a zlepšuje úchop na skále i v umělých stěnách. Prodává se v několika formách. Sypké magnézium se rychle nanáší, ale prášení je v hale někdy nežádoucí. Kostka se dá rozdrtit podle potřeby. Tekuté magnézium vytváří vrstvu, která zasychá a vydrží déle, a hodí se tam, kde je prášení omezeno, například v lezeckých halách s přísnými pravidly.</p>'
          + T(['Forma', 'Výhoda', 'Nevýhoda'], [
              ['Sypké', 'rychlé nanášení, pohodlné', 'prášení a spotřeba'],
              ['Kostka', 'lze drtit podle potřeby', 'zdlouhavější příprava'],
              ['Tekuté', 'dlouhá výdrž, méně prachu', 'je nutné nechat zaschnout'],
              ['Kuličky v sáčku', 'méně prachu a lepší dávkování', 'pomalejší dodávka na ruce']]) +
          '<p>Pytlík na magnézium se zavěšuje na pás a má být dostatečně široký, aby se do něj vešla celá ruka. Velikost volte podle ruky, objem pytlíku a toho, jak často chcete magnézium doplňovat. Děti mají k dispozici menší kusy s měkkým okrajem. Pro bouldering se používají větší vědra, která se položí na zem. Rádi je používají i cvičenci, kteří si chtějí vylepšit úchop u činek a hrazdy, tedy v rubrikách <a href="/hrazdy-a-bradla/">hrazdy a bradla</a> a <a href="/cinky-a-kotouce/">činky a kotouče</a>.</p>'
          '<p>V kategorii se občas objeví také potravinové doplňky s magnéziem. Nejde o lezeckou chemii, ale o výživu, a patří do <a href="/vitaminy-a-mineraly/">vitamínů a minerálů</a>. U potravinových doplňků dodržujte doporučené dávkování a v případě pochybností se poraďte s lékařem.</p>'
          '<h2>Pouzdra, vaky a ochrana lana</h2>'
          '<p>Lano je nejdražší a nejdůležitější součást výbavy. Pouzdro na lano, plachta nebo vak ho chrání před blátem a UV zářením a usnadňují manipulaci u skály. Lýtkové pouzdro na slaňovací lano pomáhá při práci ve výšce, protože lano nezamotá. Hodí se také stahovací pytle nebo batohy, které se dají rozložit jako podložka. Lano ukládejte v suchu a bez styku s chemikáliemi či ostrými hranami. Další výbavu k přenášení najdete mezi <a href="/turisticke-batohy/">turistickými batohy</a> a <a href="/batohy/">batohy</a>.</p>'
          '<h2>Pro koho a na co</h2>'
          '<ul><li><strong>Začátečník v hale:</strong> sedák, lezečky a jistítko. Většinu vybavení si půjčíte, vlastní sedák ale ocení každý, komu se vyplatí pravidelná praxe.</li>'
          '<li><strong>Sportovní lezec na skále:</strong> lehký sedák, expresky, jistítko (tuba nebo s asistovaným brzděním) a přilba.</li>'
          '<li><strong>Vícedélkové cesty a hory:</strong> víceúčelový sedák, přilba, smyčky, slaňovací pomůcky a kvalitní ochrana.</li>'
          '<li><strong>Ferraty:</strong> sedák, absorbér, přilba a rukavice. Viz <a href="/sportovni-rukavice/">sportovní rukavice</a> a <a href="/nesmeky/">nesmeky</a>.</li>'
          '<li><strong>Děti:</strong> dětský sedák s menšími popruhy a dětská přilba. Vždy pod dohledem zkušeného dospělého.</li></ul>'
          '<h2>Stěna, skála a bouldering: co kde potřebujete</h2>'
          '<p>V lezecké hale vám stačí osobní sedák, jistítko a pytlík na magnézium, protože jistící body jsou pevně osazené a trasa je ohraničená. Na skále přibývají expresky, přilba, smyčky a často i vlastní lano, protože jistící body musíte propojit sami a hrozí pád kamene. Bouldering se obejde bez sedáku i lana, ale vyžaduje velký pytlík nebo vědro s magnéziem, kartáč na úchyty a crashpad, tedy žíněnku pro měkký dopad. Při přechodu z haly na skálu se vyplatí absolvovat kurz, protože techniky jištění a komunikace s partnerem se v přírodě liší od těch, na které jste zvyklí.</p>'
          '<h2>Péče a životnost vybavení</h2>'
          '<p>Textilní prvky stárnou i bez používání. Slunce, vlhkost, pot a chemikálie zkracují jejich životnost. Výrobci uvádějí v návodech maximální dobu používání a pravidelné prohlídky. Dodržujte je a vyřaďte vše, co je poškozené nebo podezřelé. Sedák po pádu vyměňte, pokud výrobce nepovolí další používání. Vybavení čistěte vlažnou vodou a jemným mýdlem, sušte ve stínu a mimo zdroje tepla.</p>'
          '<ul><li>Kovové součásti kontrolujte na ostré hrany, praskliny a zadrhávání.</li>'
          '<li>Zapisujte si datum první použití a počet pádů.</li>'
          '<li>Nepůjčujte si cizí vybavení, jehož historii neznáte.</li>'
          '<li>Neskladujte ho v autě, kde se v létě přehřívá.</li></ul>'
          '<h2>Související kategorie</h2>'
          '<p>K lezení patří také obuv, lana a širší turistická výbava. Prohlédněte si <a href="/lezecke-boty/">lezecké boty</a>, <a href="/horolezectvi/">horolezectví a ferraty</a>, <a href="/trekove-hole/">trekové hole</a>, <a href="/prvni-pomoc/">první pomoc</a> a <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoola</a>. Pro přesuny k lezeckým oblastem se hodí <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>.</p>',
    faq=[('Jak poznám správnou velikost lezeckého sedáku?', 'Sedák musí pevně sedět na pase a nesmí se sesunout přes boky. Vyzkoušejte ho v oblečení, ve kterém budete lézt, a pověste se do něj.'),
         ('Potřebuji vlastní přilbu, když lezu v hale?', 'V hale se přilba většinou nenosí, ve skále ano. Vlastní přilba je výhodnější než půjčená, protože víte, jak se používala.'),
         ('Jaké jisticí zařízení je pro začátečníka nejlepší?', 'Rozhoduje instruktor a lano, se kterým lezete. I zařízení s asistencí vyžaduje správnou techniku jištění a tu žádný přístroj nenahradí. Vždy se řiďte návodem výrobce a pokyny instruktora.'),
         ('Jak často se mění lezecký sedák?', 'Podle návodu výrobce, stavu textilií a četnosti používání. Po pádu, poškození nebo po dlouhé době používání jej vyřaďte.'),
         ('Čím se liší sypké, kostkové a tekuté magnézium?', 'Sypké je rychlé, kostka se drtí a tekuté se nanáší a nechá zaschnout, takže méně práší. Volba závisí na pravidlech haly a osobním pocitu.'),
         ('Jaký pytlík na magnézium zvolit?', 'Dostatečně široký na celou ruku a s pevným opaskem. Děti potřebují menší a boulderisté větší vědro, které se postaví na zem.'),
         ('Mohu si koupit použité vybavení?', 'U osobních ochranných prostředků to nedoporučujeme, protože neznáte jejich historii. U doplňků jako pytlíky či pouzdra nic nebrání.'),
         ('Jak čistit sedák a smyčky?', 'Vlažnou vodou a jemným mýdlem, bez agresivních prostředků. Sušte ve stínu a mimo zdroje tepla.'),
         ('Hodí se sedák na ferraty i do skal?', 'Často ano, ale na ferratě potřebujete i absorbér pádu a ramenní popruhy. Zeptejte se v obchodě na kombinaci pro váš typ lezení.'),
         ('Jsou doplňky s magnéziem k jídlu lezecká pomůcka?', 'Ne, jde o potravinové doplňky. Patří do výživy, dodržujte doporučené dávky a při pochybnostech se poraďte s lékařem.')],
)

# ------------------------------------------------------------------ plovaci-vesty
NEW['plovaci-vesty'] = dict(long=True,
    title='Plovací a záchranné vesty: děti, dospělí, paddleboard',
    desc='Plovací a záchranné vesty pro děti, dospělé i psy. Jak vybrat vztlak, velikost a typ pro paddleboard, kajak, loď i rybaření.',
    intro='<p>Plovací vesta je nejjednodušší způsob, jak snížit riziko utonutí, a přitom ji lidé často nechávají doma, protože ji považují za zbytečnou. Správně zvolená vesta se přitom nosí pohodlně a vodní sporty vám neztíží. V kategorii najdete záchranné vesty pro dospělé, plovací vesty pro děti a kojence, neoprenové modely na paddleboard a kajak, vesty pro rybáře a posádky lodí i plovací vesty pro psy. Sporteka srovnává nabídky českých obchodů, abyste snadno našli skladové velikosti a vybrali podle značky.</p>'
          '<p>V nabídce převažují ' + B(('jobe', 'Jobe'), ('aquarius', 'Aquarius'), ('eg', 'EG'), ('lalizas', 'Lalizas'), ('decathlon', 'Decathlon'), ('hiko', 'Hiko'), ('palm', 'Palm'), ('elements-gear', 'Elements Gear'), ('plastimo', 'Plastimo')) +
          '. Kategorie je součástí rubriky <a href="/paddleboardy/">paddleboardy a kajaky</a> a doplňují ji <a href="/kajaky-a-cluny/">kajaky a čluny</a> a <a href="/vodni-sporty/">vodní sporty</a>.</p>',
    guide='<h2>Jaké vesty existují</h2>'
          '<p>Vesty se dělí podle účelu a konstrukce. Plovací vesta pomáhá udržet se nad vodou ve chvíli, kdy jste při vědomí a pohybujete se, záchranná vesta má vyšší vztlak a v ideálním případě vás otočí obličejem vzhůru. Různé jsou i materiály: pěnová vložka v textilním obalu, neopren nebo nafukovací komora. Správnou volbu určuje, kde a jak se budete pohybovat.</p>'
          + T(['Typ', 'Vlastnosti', 'Hodí se pro'], [
              ['Pěnová plovací vesta', 'pevná pěnová vložka, odolná, nevyžaduje údržbu', 'rekreační plavbu, rodinné výlety, kemp'],
              ['Neoprenová vesta', 'pružná, přiléhavá, pohodlná při pohybu', 'paddleboard, kajak, vodní lyže, plachtění'],
              ['Záchranná vesta s vyšším vztlakem', 'výrazný vztlak, límec pod hlavou', 'lodě, delší plavby, méně zkušení plavci'],
              ['Nafukovací vesta', 'lehká, kompaktní, aktivace ručně nebo automaticky', 'plachtění, rybaření, dospělí s pravidelnou údržbou'],
              ['Dětská a kojenecká vesta', 'límec, poutko, třmen mezi nohama', 'děti na lodi, u vody a na dovolené'],
              ['Vesta pro psy', 'držadlo na zádech, reflexní prvky', 'psy na lodi, paddleboardu a při koupání']]) +
          '<p>Základní pravidlo zní: vesta musí odpovídat aktivitě. Pro rychlé vodní sporty, při kterých se často padá, vybírejte pevnější model s dobrým uchycením. Při klidné plavbě na loďce stačí lehká plovací vesta. Pokud si nejste jisti, zvolte spíš vyšší vztlak.</p>'
          '<h2>Vztlak a značení</h2>'
          '<p>Vztlak se uvádí v newtonech a bývá vytištěný přímo na vestě. Čím vyšší hodnota, tím větší sílu vesta vyvíjí, aby udržela hlavu nad vodou. Označení vychází z evropských norem a obvykle se setkáte se stupni kolem 50, 100, 150 a 275 newtonů.</p>'
          + T(['Hodnota vztlaku', 'Obecné určení'], [
              ['kolem 50 N', 'plovací pomůcka pro plavce poblíž břehu nebo pomoci při vodních sportech'],
              ['kolem 100 N', 'vesta pro vnitrozemské vody a chráněné oblasti'],
              ['kolem 150 N', 'vesta pro delší plavby a náročnější podmínky'],
              ['kolem 275 N', 'výbava na otevřené moře a pro těžké oblečení']]) +
          '<p>Všechny zmíněné údaje berte jako obecnou orientaci. Přesný popis použití najdete vždy v návodu a na štítku konkrétní vesty. Pokud vestu kupujete pro dítě, zaměřte se na hmotnostní rozsah, ne na věk, protože děti stejného věku se výrazně liší.</p>'
          '<h2>Velikost a správné nasazení</h2>'
          '<p>Vesta musí sedět těsně, ale nesmí omezovat dýchání. Po zapnutí zkuste vestu zvednout za ramenní popruhy. Pokud vám sjede přes hlavu nebo vyleze k uším, je moc velká. U dětí se používá zkouška nadzvednutím: dítě má stát rovně a vesta se nesmí zvednout výš než k bradě a uším. Kromě obvodu hrudníku rozhoduje i hmotnost těla.</p>'
          '<ul><li><strong>Popruhy a přezky:</strong> pevně dotažené, ale ne škrtivé. Třmen mezi nohama zabrání vyjetí vesty nahoru.</li>'
          '<li><strong>Zip nebo zapínání:</strong> používejte vždy všechna zapínání. Odepnutý pás z vesty udělá jen ozdobu.</li>'
          '<li><strong>Zkouška ve vodě:</strong> ve vodě se ujistěte, že vesta drží tělo ve stabilní poloze a hlava se nenaklání dopředu.</li>'
          '<li><strong>Pod oblečení:</strong> pokud nosíte neopren, vybírejte velikost vesty přes něj. Neopreny najdete v kategorii <a href="/neopreny/">neopreny</a>.</li></ul>'
          '<h2>Vesta pro děti a kojence</h2>'
          '<p>Dětské vesty jsou nejdůležitější ze všech, protože děti mají vyšší hlavu v poměru k tělu a rychle ztrácejí rovnováhu. Dobrý model má límec, který podepírá hlavu, třmen mezi nohama a madlo na zátylku pro vytažení z vody. Pro nejmenší děti jsou vhodné vesty s vyšším vztlakem a výrazným límcem. Pro starší děti na paddleboardu nebo kajaku se používají volnější modely.</p>'
          '<ul><li>Vyberte vestu podle hmotnosti, ne podle věku. Příliš velká vesta se sveze, příliš malá nedrží.</li>'
          '<li>Dětskou vestu nikdy nenahrazujte nafukovacími kruhy ani rukávky. Ty mají jinou funkci a nezajistí bezpečí.</li>'
          '<li>Vestu nasazujte dítěti ještě na břehu a zkoušejte ji s ním v mělké vodě.</li>'
          '<li>Pro malé děti hledejte také <a href="/plavecke-pomucky/">plavecké pomůcky</a> a <a href="/detske-plavky/">dětské plavky</a>.</li></ul>'
          '<p>Vesta je pouze doplněk pozornosti. Dítě u vody nikdy nenechávejte bez dozoru dospělého, ani když má vestu. Značky jako ' + B(('eg', 'EG'), ('hiko', 'Hiko'), ('elements-gear', 'Elements Gear')) + ' nabízejí modely pro různé hmotnostní kategorie.</p>'
          '<h2>Paddleboard, kajak a kánoe</h2>'
          '<p>Při pádlování potřebujete volnost pohybu ramen. Proto se u těchto sportů vyplatí neoprenová nebo anatomicky střižená vesta s krátkými ramenními popruhy, které se nezaseknou o pádlo. U paddleboardů bývá velmi oblíbená nafukovací vesta, která se nosí na pasu a neomezuje pohyb, ale vyžaduje kontrolu a údržbu aktivačního mechanismu. Pasový nafukovací pás nemusí být certifikovanou plovací vestou a pro neplavce a děti se nehodí, proto si ověřte certifikaci a uvedený vztlak. Více informací najdete v rubrice <a href="/paddleboardy/">paddleboardy</a> a u <a href="/kajaky-a-cluny/">kajaků a člunů</a>.</p>'
          '<ul><li><strong>Studená voda:</strong> pád do chladné vody je nebezpečný i pro dobré plavce. Kombinujte vestu s neoprenem.</li>'
          '<li><strong>Kapsy a poutka:</strong> praktické pro píšťalku, nůž a drobnosti. Pomůže například <a href="/outdoorove-noze-a-multitoola/">outdoorový nůž</a> pro řezání lana.</li>'
          '<li><strong>Reflexní prvky:</strong> usnadňují nalezení člověka na vodě, zejména za šera.</li>'
          '<li><strong>Obuv:</strong> do vody se hodí <a href="/obuv-do-vody/">obuv do vody</a>, která chrání před kameny a mušlemi.</li></ul>'
          '<h2>Rybaření, motorové lodě a plachtění</h2>'
          '<p>Na lodi a při rybaření se často pracuje u hrany člunu, kde je pád do vody reálný. Rybáři vyhledávají pohodlné vesty s kapsami a poutky na vybavení. Rapala nebo Baltic nabízejí řešení pro tuto skupinu. Pro delší plavby jsou lepší vesty s vyšším vztlakem a s límcem, které otáčejí bezvědomého člověka obličejem vzhůru. Na plachetnicích se používají i nafukovací vesty s postrojem pro uvázání lana. Nezapomeňte na to, že vesta funguje, jen když je zapnutá. Další vybavení hledejte v rubrikách <a href="/rybareni/">rybaření</a>, <a href="/rybarske-obleceni/">rybářské oblečení</a> a <a href="/rybarske-lode-a-elektronika/">rybářské lodě a elektronika</a>.</p>'
          '<h2>Vesty pro psy</h2>'
          '<p>Většina psů plave, ale některá plemena plavou špatně a každý pes se unaví. Plovací vesta pro psa pomáhá starším jedincům, krátkonosým plemenům a těm, kteří se vozí na lodi či paddleboardu. Dobrá vesta má rychlý popruh na zátylku, výrazné barvy a vestu přitahuje k tělu popruhy pod břichem. Vybírejte podle obvodu hrudníku a hmotnosti psa. Zvykejte ho na ni postupně, nejdřív na suchu, potom v mělké vodě. Značka ' + B(('aquarius', 'Aquarius')) + ' nabízí modely pro menší i větší psy.</p>'
          '<h2>Nafukovací vesty: výhody a povinnosti</h2>'
          '<p>Nafukovací vesta má malou hmotnost a při běžném pohybu skoro nepřekáží. Po aktivaci, ručním zatažením za šňůru nebo automaticky při styku s vodou, se naplní plynem z patrony. Právě proto se hodí těm, kdo vodu používají při sportu a vadí jim objemná pěna. Má ale i nevýhody. Nehodí se pro děti ani pro neplavce, protože při selhání mechanismu nemá žádnou zálohu v podobě pěny. Patronu a spoušť je nutné pravidelně kontrolovat a po aktivaci vyměnit. Před sezonou vestu zkušebně nafoukněte a zkontrolujte, zda drží vzduch.</p>'
          '<h2>Výběr podle sezóny a dovolené</h2>'
          '<p>Na rodinnou dovolenou u jezera zvažte odolnější pěnovou vestu, která snese opakované nasazování a sušení. Pro výlety na kajaku nebo paddleboardu zvolte pohodlnou vestu s volnými rameny a malým objemem. V chladném období, třeba na jaře a na podzim, kdy je voda studená, dává smysl kombinovat vestu s neoprenem a neoprenovou obuví. Při cestování letadlem se hodí lehká a skladná vesta, která se vejde do zavazadla a nezabere místo oblečení. Pokud vyrážíte k moři, ověřte u půjčovny, jaké vesty poskytují, a vezměte si vlastní, pokud potřebujete konkrétní velikost, například pro dítě.</p>'
          '<p>Před každou sezonou udělejte domácí revizi: vyzkoušejte všechny přezky, zkontrolujte, zda zipy nezadrhávají, a dětem ověřte, zda jim vesta stále sedí. Děti rostou rychle a model, který vyhovoval loni, může být letos malý. Staré vesty, které už nesedí, neodkládejte do kouta, ale předejte je dál jen tehdy, pokud jsou nepoškozené a odpovídají hmotnosti nového uživatele.</p>'
          '<h2>Jak postupovat při nákupu</h2>'
          '<ol><li>Rozhodněte, kdo vestu bude nosit: dospělý, dítě, kojenec nebo pes.</li>'
          '<li>Určete aktivitu: plavba, paddleboard, kajak, rybaření nebo koupání.</li>'
          '<li>Vyberte vztlak podle prostředí a zkušeností a ověřte označení na štítku.</li>'
          '<li>Změřte obvod hrudníku a zjistěte hmotnost, porovnejte s tabulkou výrobce.</li>'
          '<li>Porovnejte nabídky obchodů, vyzkoušejte vestu a ověřte lhůtu pro vrácení.</li></ol>'
          '<h2>Péče o vestu</h2>'
          '<ul><li>Po použití ve slané či chlorované vodě vestu opláchněte sladkou vodou.</li>'
          '<li>Sušte ji ve stínu, mimo přímé slunce a zdroje tepla, aby pěna nezkřehla.</li>'
          '<li>Skladujte volně v suchu, ne zmáčknutou pod těžkým nákladem.</li>'
          '<li>Pravidelně kontrolujte švy, zipy, popruhy a přezky a poškozenou vestu vyřaďte.</li>'
          '<li>Nafukovací vesty nechte pravidelně prohlédnout a vyměňte patronu po použití.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupě vesty o číslo větší s tím, že dítě do ní vyroste. Sveze se a přestane chránit.</li>'
          '<li>Použití rukávků či kruhů místo vesty.</li>'
          '<li>Nezapnutá vesta nebo odepnutý třmen.</li>'
          '<li>Pěnová vesta, která je několik let stará a poškozená sluncem.</li>'
          '<li>Vesta uložená v autě na sluníčku.</li></ul>'
          '<h2>Související kategorie</h2>'
          '<p>K vodě patří plavky, brýle, ploutve a první pomoc. Prohlédněte si <a href="/plavky/">plavky</a>, <a href="/plavecke-bryle/">plavecké brýle</a>, <a href="/ploutve/">ploutve</a>, <a href="/snorchlovani/">šnorchlování</a>, <a href="/plazove-doplnky/">plážové doplňky</a>, <a href="/bazeny/">bazény</a>, <a href="/lahve-a-termosky/">láhve a termosky</a> a <a href="/prvni-pomoc/">první pomoc</a>.</p>',
    faq=[('Jaký je rozdíl mezi plovací a záchrannou vestou?', 'Plovací vesta pomáhá plavci udržet se nad hladinou, záchranná má vyšší vztlak a bývá určená i pro situace, kdy člověk plavat nedokáže. Označení najdete na štítku.'),
         ('Jak vybrat velikost dětské vesty?', 'Podle hmotnosti dítěte a obvodu hrudníku. Vesta má sedět těsně, při nadzvednutí za ramena nesmí vyjet nad uši.'),
         ('Stačí dítěti plovací kruh nebo rukávky?', 'Ne, nejsou to záchranné prostředky a mohou se převrátit nebo sklouznout. Dítě u vody vždy hlídejte a vestu doplňte dohledem dospělého.'),
         ('Co znamená údaj v newtonech?', 'Je to vztlak vesty. Vyšší hodnota znamená větší schopnost udržet hlavu nad vodou, přesné použití určuje štítek a návod.'),
         ('Hodí se neoprenová vesta na paddleboard?', 'Ano, je pružná a nebrání pohybu ramen. Ve studené vodě ji kombinujte s neoprenem.'),
         ('Jak správně nasadit vestu?', 'Zapněte všechna zapínání, dotáhněte popruhy a třmen mezi nohama. Zkontrolujte, že se vesta při zvednutí za ramena nesune přes hlavu.'),
         ('Jak často vestu měnit?', 'Když je poškozená, vybledlá nebo ztvrdlá pěna. U nafukovacích vest dodržujte revizní intervaly výrobce.'),
         ('Mám pro psa vybrat zvláštní vestu?', 'Ano, psí vesta má jiný střih a madlo na zádech pro vytažení. Vybírejte podle obvodu hrudníku a hmotnosti psa.'),
         ('Hodí se vesta pro rybáře do člunu?', 'Ano, na lodi se pohybujete u okraje a pád nelze vyloučit. Vybírejte pohodlný model s kapsami a dostatečným vztlakem.'),
         ('Jak vestu čistit a sušit?', 'Opláchněte sladkou vodou, sušte ve stínu a mimo teplo. Slunce a vysoká teplota pěnu poškozují.')],
)
