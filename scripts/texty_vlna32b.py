"""sporteka.cz — wave 32b (18. 11. 2026): long texts for karabiny, horolezecka-lana, cepiny-a-macky, nordic-walking-hole,
hrudni-pasy, solarni-nabijecky.

General true facts only, no prices, no product counts. Climbing gear (carabiners, ropes, ice axes, crampons) always comes with
the note that safe use needs a course or an experienced instructor and that the text does not replace it; norms are named only
where verified. Heart-rate straps are described as sports sensors, not medical devices. Solar chargers without exaggeration:
the panel rating is a lab figure and real output depends on sun, angle, heat and clouds.
Brands linked only if present in src/texts/znacky.json (mammut, salewa, insportline, garmin), the rest plain text.
The `viking` brand page belongs to a different Viking than Viking Technology (power banks), so it is not linked.

Sources:
- SATRA, EN 12275:2013 Connectors: classes B, H, K, Q, X and minimum static strength (B 20/7/7 kN, H 20/6/7 kN,
  K 25/8/7 kN, X 18/5/7 kN; major axis closed / gate open / minor axis); Edelrid EN 12275 extract (marking of H, K, X)
- Edelrid EN 892 summary (labels: maker, year, length, diameter, symbol single 1 / half 1/2 / twin infinity);
  UIAA 101 (2025): "UIAA Water Repellent" means weight gain < 5 % in the water test
- Petzl FAQ "What is the lifetime of my Petzl equipment": textile products max. 10 years from manufacture, metal products
  unlimited, an exceptional event can retire a product after one use; Teufelberger table (up to 10 / 7 / 5 years by use)
- Sterling Rope, rope.com, ropesdirect: EN 1891 static ropes type A/B, not for lead climbing
- vandernet "EN 13089 explained", Grivel and Salewa ice-axe manuals: type 1 (formerly B, basic, unmarked) and type 2
  (formerly T, technical, marked T); EN 893 crampons, manual must state compatible boots
- Alpkit, Scarpa UK, Ellis Brigham crampon guides: boots B0-B3, crampons C1-C3, boot rating must match or exceed crampon rating,
  B0 takes no crampons, C1 strap-on, C2 heel lever + toe cradle, C3 step-in with toe and heel welts
- Decathlon, Ordnance Survey, Luontoon (Metsähallitus) on Nordic walking poles: height x 0.68, beginners about x 0.62,
  arm slightly over 90 degrees, choose the shorter length when between two sizes
- Polar support: H10 uses CR2025 (CR2032 must not be used), strap machine-washed at 40 °C without the connector, no dryer,
  no softener, moisten electrodes; H10 two Bluetooth connections plus ANT+
- Garmin HRM-Dual specs and manual: CR2032, 1 ATM, does not transmit while swimming, rinse after each use, machine wash after
  every seventh use; Garmin HRM 600: rechargeable battery (retailer pages)
- Goal Zero "Solar ratings explained" and other solar sources: STC 1000 W/m2, 25 °C cell temperature; output falls with heat,
  angle, clouds, shade
- IATA batteries guidance: power banks under 100 Wh in cabin baggage, 100-160 Wh with airline approval, over 160 Wh not allowed
Left out (not verifiable or too variable): ice-axe length formula, impact-force limits of EN 892, exact rope diameters
of individual models, panel counts of individual solar power banks, battery life of individual straps, 2027 airline rules.
"""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ karabiny
NEW['karabiny'] = dict(long=True,
    title='Karabiny lezecké, HMS, ferratové i na klíče',
    desc='Lezecké karabiny HMS, D a oválné, se zámkem i bez, ferratové i drobné karabinky na klíče. Značení kN, typy zámků a péče.',
    intro='<p><strong>Karabina</strong> je kovová spojka s pružným zámkem, kterou se v lezení propojuje lano, sedák, kotvení a jisticí pomůcky. Stejným slovem se ale říká i malému kroužku na klíče nebo na láhev, který s lezením nemá nic společného. Rozdíl je zásadní: lezecká karabina je osobní ochranný prostředek, prošla zkouškami podle normy a na hřbetu má vyražené pevnosti v kilonewtonech. Doplňková karabinka na batoh takové zkoušky nemá a k jištění se nesmí použít.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů u karabin se zámkem i bez zámku, u HMS karabin na jištění, oválných karabin, ferratových karabin i u drobných karabinek na klíče. Mezi výrobci jsou Petzl, Black Diamond, Ocún, Singing Rock, Edelrid, Camp nebo '
          + B(('mammut', 'Mammut'), ('salewa', 'Salewa')) +
          '. Karabiny patří do kategorie <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>. Text slouží k orientaci při nákupu a kurz lezení ani zaškolení instruktorem nenahrazuje.</p>',
    guide='<h2>Lezecká karabina a karabinka na klíče</h2>'
          '<p>První otázka při nákupu zní, k čemu karabinu potřebujete. Pokud na ní bude viset člověk, musí jít o certifikovanou lezeckou karabinu. Pozná se podle značení na těle: jméno výrobce, symbol normy a tři čísla s šipkami, která udávají pevnost v kilonewtonech. U výrobků prodávaných v Evropě se objevuje norma EN 12275, u mnoha karabin také označení UIAA.</p>'
          '<p>Doplňkové karabinky na klíče, láhve, hrnky nebo na připnutí bundy k batohu bývají z tenčího hliníku a často mají přímo na sobě nápis „not for climbing“ nebo piktogram s přeškrtnutým lezcem. Jsou levné, lehké a šikovné, ale ke slanění, jištění ani k zavěšení houpačky nepatří. Značky jako Munkees nebo Nite Ize vyrábějí hlavně tento druh. Stejně tak karabina na psím vodítku nebo na kšandě vojenského batohu není lezecké vybavení.</p>'
          '<h2>Co znamenají čísla na hřbetu</h2>'
          '<p>Na certifikované karabině najdete obvykle tři hodnoty v kN. Největší číslo patří zatížení v podélné ose se zavřeným zámkem, tedy směru, ve kterém má karabina pracovat. Druhé číslo udává pevnost v příčné ose, kdy síla tahá karabinu do šířky. Třetí hodnota je pevnost v podélné ose s otevřeným zámkem. Pro představu: jeden kilonewton odpovídá síle, kterou na zem působí zhruba sto kilogramů.</p>'
          '<p>Norma EN 12275 dělí karabiny do tříd a pro každou stanovuje minimální pevnosti. Základní karabina typu B musí v podélné ose vydržet aspoň 20 kN, s otevřeným zámkem 7 kN a v příčné ose 7 kN. U karabin HMS je minimum 20, 6 a 7 kN, u ferratových karabin typu K 25, 8 a 7 kN. Oválné karabiny typu X mají minimum 18, 5 a 7 kN. Skutečné hodnoty konkrétní karabiny bývají vyšší a jsou vyražené na ní.</p>'
          + T(['Třída podle EN 12275', 'Typické použití', 'Minimum podélně / otevřená / příčně'], [
              ['B (základní)', 'expresky, běžné spojování', '20 / 7 / 7 kN'],
              ['H (HMS)', 'jištění, slaňování, kotvení', '20 / 6 / 7 kN'],
              ['K (ferratová)', 'ferratový set', '25 / 8 / 7 kN'],
              ['X (oválná)', 'kladky, blokanty, pomůcky', '18 / 5 / 7 kN'],
              ['Q (šroubovací spojka)', 'maillon, trvalé spoje', '25 kN podélně, 10 kN příčně']]) +
          '<p>Z tabulky je vidět, proč záleží na tom, jak karabina pracuje. Karabina zatížená přes zámek nebo napříč přes hranu skály má zlomek pevnosti, se kterou počítá výrobce. Proto se lezci učí karabinu správně orientovat a hlídat, aby se v průběhu lezení neotočila.</p>'
          '<h2>Tvary: HMS, D a ovál</h2>'
          '<p><strong>HMS karabina</strong> má tvar hrušky se širokým koncem. Zkratka pochází z němčiny a označuje jištění polovičním lodním uzlem, kterému se v Česku říká i UIAA uzel. Široký oblouk umožňuje, aby uzel v karabině volně přeskakoval, a vejde se do ní i víc lan nebo smyček. Proto se HMS karabiny používají k jisticí pomůcce, ke kotvení a jako hlavní karabina na sedáku. Na hřbetu nesou značku H.</p>'
          '<p><strong>Karabina tvaru D</strong> nebo asymetrické D posouvá zatížení blíž k pevnému hřbetu, takže na stejnou pevnost vychází lehčí. Je nejčastější v expreskách a jako univerzální karabina na sedák. <strong>Oválná karabina</strong> drží předměty uprostřed a nenechá je sklouznout do rohu. Hodí se pro kladky, blokanty a práci s lany na stromech nebo při záchraně, kde je ovál standardem. Ferratové karabiny bývají velké, s širokým otvorem a samozamykacím zámkem, aby šly ovládat jednou rukou v rukavici. Více o nich najdete u kategorie <a href="/via-ferrata/">via ferrata</a>.</p>'
          '<h2>Zámky a pojistky</h2>'
          '<p>Karabiny bez pojistky mají buď plný zámek, nebo drátěný. Drátěný zámek je lehčí, méně zamrzá a méně kmitá při pádu, proto se často používá na expreskách. Plný zámek se lépe drží prsty. Nos karabiny může mít klasický háček, nebo hladký tvar keylock, který se nezachytává o smyčky a jištění.</p>'
          '<p>Kde nesmí dojít k náhodnému otevření, používá se karabina s pojistkou:</p>'
          '<ul><li><strong>Šroubovací pojistka (screwgate):</strong> objímku zatočíte rukou. Je jednoduchá a levná, ale musíte myslet na to, abyste ji opravdu zašroubovali, a v provozu se může sama povolit.</li>'
          '<li><strong>Automatická pojistka (twistlock):</strong> po puštění se sama otočí a zamkne. Otevírá se otočením a zatlačením.</li>'
          '<li><strong>Trojitá pojistka (triple lock):</strong> vyžaduje tři pohyby, takže ji téměř nelze otevřít nechtěně. Hodí se pro kotvení a práci ve výšce.</li>'
          '<li><strong>Magnetické a další systémy:</strong> výrobci mají vlastní řešení, která se ovládají jednou rukou a zavírají se sama.</li></ul>'
          '<p>Automatické pojistky jsou pohodlné, ale v blátě, písku nebo mrazu se mohou zasekávat. Šroubovací karabina se v zimě ovládá lépe v rukavici. Rozhoduje hlavně zvyk a to, co vás naučili v kurzu.</p>'
          '<h2>Materiál, hmotnost a velikost</h2>'
          '<p>Většina lezeckých karabin je z hliníkové slitiny. Ocelové karabiny jsou těžší, ale odolnější vůči oděru, a proto se objevují v lezeckých stěnách na trvalých kotvách nebo v pracovních setech. Lehké karabiny šetří gramy na dlouhých cestách, mívají ale užší profil, který lano víc ohýbá a rychleji se opotřebuje. Na jištění je praktičtější větší HMS karabina, do které se lano dobře vejde a kterou snáz ovládnete.</p>'
          '<p>Rozměr otvoru zámku rozhoduje o tom, jak snadno karabinu zacvaknete do kotvy nebo do lana. Na expreskách se proto spodní karabina dělá s větším otvorem pro lano. Barevné odlišení pomáhá v orientaci na sedáku, třeba aby karabina k jisticí pomůcce byla vždy stejná.</p>'
          '<h2>Kontrola a životnost</h2>'
          '<p>Kovová karabina nemá podle výrobců pevně danou životnost, rozhoduje její stav. Pravidelně kontrolujte, zda zámek dosedá a pruží, zda pojistka nedrhne a zda na těle nejsou hluboké rýhy. Ostré zářezy od lana nebo od ocelových kotev mohou lano poškodit a takovou karabinu je lepší vyřadit. Karabinu, která spadla z velké výšky na skálu nebo na beton, vyřaďte i tehdy, když na ní nic nevidíte, pokud výrobce neuvádí jinak.</p>'
          '<p>Po lezení u moře nebo v blátě karabiny opláchněte čistou vodou, nechte je uschnout a mechanismus zámku podle návodu ošetřete. Nepatří do blízkosti kyselin a chemikálií, například autobaterie. Na karabiny nic nevyrývejte ani nepilujte, oslabíte tím materiál. K označení slouží barevná páska nebo lak na místa, kde to výrobce povoluje.</p>'
          '<h2>Jak sestavit základní sadu</h2>'
          '<p>Začátečník ve skalách nebo na stěně obvykle potřebuje jednu HMS karabinu se zámkem k jisticí pomůcce, jednu nebo dvě karabiny se zámkem na odsedávání a kotvení a sadu expresek. Kolik expresek, záleží na délce cest v oblasti. Na ferraty se kupuje hotový ferratový set s tlumičem, ne samostatné karabiny se smyčkou. Výběr konzultujte s instruktorem a na stěně si nechte ukázat, jak se s jednotlivými typy pracuje. Ke karabinám se hodí <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky a pomůcky</a> a <a href="/horolezecka-lana/">horolezecká lana</a>.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U lezeckých karabin hledejte v popisu tvar, typ zámku a pojistky, hmotnost a hlavně pevnosti v kN. Pokud nabídka pevnosti a normu neuvádí, jde nejspíš o doplňkovou karabinku. Sady více kusů bývají výhodné u expresek a drobných karabinek, u HMS karabin se obvykle kupuje jeden kus. Pozor na podobné názvy: „karabina D“ může být lezecká i kempingová. Pokud si nejste jistí, otevřete stránku výrobce a zkontrolujte značení. Kempingové hrnky a lahve s karabinou najdete v kategorii <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>',
    faq=[
        ('Mohu karabinku na klíče použít k lezení?', 'Ne. Doplňkové karabinky nemají zkoušky podle lezeckých norem a často nesou nápis „not for climbing“. K jištění, slaňování a kotvení slouží jen certifikované lezecké karabiny.'),
        ('Co znamenají čísla v kN na karabině?', 'Udávají pevnost v podélné ose se zavřeným zámkem, v příčné ose a v podélné ose s otevřeným zámkem. Jeden kilonewton odpovídá síle zhruba sta kilogramů.'),
        ('Jaký je rozdíl mezi HMS a D karabinou?', 'HMS má tvar hrušky se širokým koncem a hodí se pro jištění polovičním lodním uzlem, k jisticí pomůcce a ke kotvení. D karabina je lehčí a používá se hlavně v expreskách.'),
        ('Šroubovací, nebo automatická pojistka?', 'Šroubovací je jednoduchá a dobře se ovládá v rukavicích, ale musíte ji zašroubovat. Automatická se zamkne sama, v blátě a mrazu ale může drhnout.'),
        ('K čemu slouží oválná karabina?', 'Drží předměty uprostřed, takže se hodí pro kladky, blokanty a práci s lany. Minimální pevnost oválných karabin je podle normy nižší než u karabin tvaru D.'),
        ('Jak dlouho vydrží lezecká karabina?', 'Kovové karabiny nemají pevně danou životnost. Vyřaďte je při hlubokých rýhách, ostrých hranách, nefunkčním zámku nebo po pádu z velké výšky na tvrdý povrch.'),
        ('Mohu na ferratu použít obyčejné karabiny se smyčkou?', 'Ne. Na ferratu patří hotový ferratový set s tlumičem pádu a ferratovými karabinami. Smyčka bez tlumiče pád nezbrzdí.'),
        ('Proč je pevnost s otevřeným zámkem tak nízká?', 'Když je zámek otevřený, nese zatížení jen hřbet a otevřená část. Proto se lezci učí hlídat, aby se zámek o skálu neotevřel a karabina pracovala ve správné ose.'),
        ('Jak karabiny čistit?', 'Opláchněte je čistou vodou, nechte uschnout a mechanismus zámku ošetřete podle návodu výrobce. Chraňte je před kyselinami a chemikáliemi.'),
        ('Kde koupit lezecké karabiny?', 'Na Sportece vidíte nabídky českých e-shopů u jednotlivých karabin a sad. Objednávku dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ horolezecka-lana
NEW['horolezecka-lana'] = dict(long=True,
    title='Horolezecká lana dynamická i statická',
    desc='Dynamická lana jednoduchá, poloviční a dvojitá i statická lana. Průměr, délka, impregnace, značení podle norem a životnost.',
    intro='<p><strong>Horolezecké lano</strong> je hlavní článek jisticího řetězce. Dynamické lano se při pádu natáhne a zbrzdí lezce tak, aby síla, která na něj a na jištění působí, zůstala v únosných mezích. Statické lano se naopak natahuje jen málo a slouží ke slaňování, výstupu po laně, práci ve výšce nebo jako pevné zábradlí. Záměna těchto dvou typů může mít vážné následky.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých obchodů u jednoduchých, polovičních a dvojitých dynamických lan i u statických lan. Prodávají je například Beal, Tendon, Edelrid, Simond, Camp nebo '
          + B(('mammut', 'Mammut'), ('salewa', 'Salewa')) +
          '. Lana najdete v kategorii <a href="/lezecka-lana-a-karabiny/">lana, karabiny a ferraty</a>, pod kterou spadá i <a href="/horolezectvi/">horolezectví</a>. Lezení na laně se učí v kurzu nebo pod vedením instruktora. Tento text je jen pomůcka k výběru a výcvik nenahrazuje.</p>',
    guide='<h2>Dynamické a statické lano</h2>'
          '<p>Dynamická lana se vyrábějí podle normy EN 892 a UIAA 101. Jsou stavěná na to, aby zachytila pád prvolezce, při kterém může lezec spadnout i několik metrů pod poslední jištění. Lano při tom pohltí velkou část energie protažením. Statická lana s nízkou průtažností spadají pod normu EN 1891 a dělí se na typ A a typ B. Na lezení s horním jištěním se statické lano někdy použít dá, na lezení s dolním jištěním ne. Pád do statického lana by přenesl na lezce i kotvení mnohem větší sílu.</p>'
          '<p>Statické lano se uplatní ve speleologii, při práci ve výšce, při záchraně, na stavbu zábradlí na expedicích nebo jako lano na slaňování ze skal. Má pevný oplet, méně se kroutí a při výstupu po laně neprokluzuje tolik jako lano dynamické.</p>'
          '<h2>Jednoduché, poloviční a dvojité</h2>'
          '<p>Dynamická lana se dělí podle toho, jak se s nimi leze. Druh je vyznačený na koncích lana symbolem v kroužku.</p>'
          + T(['Typ', 'Značka na konci', 'Jak se používá', 'Kde se hodí'], [
              ['Jednoduché', '1', 'samotné jedno lano', 'lezecké stěny, sportovní lezení, většina skal'],
              ['Poloviční', '½', 'dva prameny, každý se cvaká do jiného jištění', 'vícedélkové a horské cesty, led, kličkující cesty'],
              ['Dvojité', '∞', 'dva prameny se cvakají vždy společně', 'horské túry, ledopády, slanění na plnou délku'],
              ['Statické', 'podle EN 1891 (typ A, B)', 'slaňování, výstup po laně, kotvení', 'jeskyně, práce ve výšce, zábradlí']]) +
          '<p>Některá tenká lana mají certifikaci pro všechny tři způsoby. Dá se s nimi lézt jako s jednoduchým lanem a v jiné situaci použít ve dvojici. Výhodou dvou pramenů je menší tření v kličkující cestě, možnost slanit na plnou délku lana a záloha pro případ, že by jeden pramen přeřízla hrana. Nevýhodou je složitější manipulace a nutnost znát správnou techniku jištění.</p>'
          '<h2>Průměr a hmotnost</h2>'
          '<p>Jednoduchá lana se pohybují zhruba kolem devíti až deseti a půl milimetru. Silnější lano déle vydrží oděr a dobře se drží v ruce, proto se hodí na lezecké stěny a na nacvičování cest, kde lano hodně trpí. Tenčí jednoduché lano je lehčí a lépe se s ním cvaká, ale rychleji se opotřebuje a klade vyšší nároky na jisticí pomůcku. Poloviční lana mívají kolem sedmi a půl až osmi a půl milimetru, dvojitá jsou ještě tenčí.</p>'
          '<p>Před nákupem zkontrolujte, pro jaký rozsah průměrů je určená vaše jisticí pomůcka. Výrobci jisticích pomůcek to uvádějí v návodu. Tenké lano ve starší pomůcce nemusí brzdit tak, jak by mělo. U hmotnosti se v popisu udává hmotnost jednoho metru v gramech, což usnadní porovnání různých lan.</p>'
          '<h2>Délka lana</h2>'
          '<p>Délka se volí podle toho, kde budete lézt. Na lezecké stěně často stačí lano kolem třiceti až čtyřiceti metrů, pokud stěna není vyšší. Pro skály se dnes běžně kupuje šedesát metrů, v oblastech s dlouhými cestami sedmdesát i víc. Pravidlo je jednoduché: lano musí stačit na to, abyste lezce z vrcholu cesty spustili zpět na zem. Při spouštění musí být lano dvakrát delší než cesta.</p>'
          '<p>Na každý konec lana se při spouštění a slaňování dělá uzel, aby lano nemohlo projet jisticí pomůckou. Tento zvyk se učí v každém kurzu a zabránil mnoha nehodám. Mnoho lan má barevně označený střed nebo změnu vzoru opletu v polovině délky, což pomáhá při slaňování.</p>'
          '<h2>Impregnace a suchá lana</h2>'
          '<p>Lano, které nasákne vodou, je těžší, hůř se s ním pracuje a v mrazu zamrzne. Proto výrobci lana impregnují. Některá mají ošetřený jen oplet, jiná oplet i jádro. Výrobci pro to používají vlastní názvy jako dry, dry cover nebo complete shield. Nezávislým měřítkem je označení „UIAA Water Repellent“. Takové lano smí při normované zkoušce nasáknout méně než pět procent své hmotnosti.</p>'
          '<p>Pro lezení na stěně a v teplých skalách impregnace nutná není. Pro horolezectví, lezení v ledu, zimní túry nebo výpravy, kde lano může zmoknout, má smysl. Impregnace také trochu zpomaluje špinění a opotřebení opletu.</p>'
          '<h2>Značení a co čtete na štítku</h2>'
          '<p>Podle EN 892 musí být na laně nebo na štítku výrobce, rok výroby, délka, průměr a symbol typu lana. Kromě toho výrobci uvádějí počet normovaných pádů, rázovou sílu, průtažnost a posuv opletu. Tyto hodnoty jsou užitečné pro srovnání lan stejného typu. Vyšší počet normovaných pádů obvykle znamená odolnější lano, nižší rázová síla měkčí zachycení. Mezi typy lan je ale nesrovnávejte, protože se zkoušejí jinak.</p>'
          '<h2>Životnost a vyřazení</h2>'
          '<p>Textilní vybavení stárne i ve skříni. Petzl u textilních výrobků uvádí maximální životnost deset let od data výroby. Jiní výrobci mají tabulky podle intenzity používání: lano používané jen párkrát za rok vydrží déle než lano, se kterým lezete každý víkend. Při častém lezení na stěně nebo při nacvičování cest se lano opotřebuje mnohem dřív a výměna může přijít po jedné sezóně.</p>'
          '<p>Lano vyřaďte hned, když je oplet prodřený a prosvítá jádro, když na něm nahmatáte měkké nebo ztvrdlé místo, když přišlo do kontaktu s kyselinou nebo když zachytilo mimořádně tvrdý pád. Výrobci výslovně uvádějí, že výjimečná událost může vést k vyřazení i po jediném použití. Pokud si stavem lana nejste jistí, poraďte se se zkušeným lezcem nebo s výrobcem.</p>'
          '<h2>Péče a skladování</h2>'
          '<ul><li>Nešlapte na lano a nenechávejte ho v písku. Zrnka se dostanou do opletu a lano zevnitř brousí.</li>'
          '<li>Používejte plachtu nebo vak na lano, ve kterém lano nosíte i rozkládáte.</li>'
          '<li>Špinavé lano perte ve vlažné vodě s jemným prostředkem podle návodu výrobce a sušte ho volně ve stínu, ne na topení.</li>'
          '<li>Skladujte ho v suchu, mimo přímé slunce, chemikálie a zdroje tepla. Nikdy ne v kufru auta vedle baterie nebo kanystru.</li>'
          '<li>Veďte si záznam, kdy lano vzniklo, jak často s ním lezete a jaké pády zachytilo.</li></ul>'
          '<h2>První lano: na co myslet</h2>'          '<p>Kdo si kupuje první lano, obvykle už prošel kurzem a leze s partou nebo s oddílem. Většinou začíná na stěně a v nižších skalách, kde se hodí jednoduché lano střední tloušťky bez zbytečných specialit. Tenká a velmi lehká lana jsou určená pro zkušené lezce, kteří umějí jistit citlivě a mají k tomu vhodnou pomůcku. Začátečníkovi tenké lano v ruce klouže a jištění je pak náročnější.</p>'          '<p>Barva lana není jen otázka vkusu. Pokud lezete ve dvojici lan nebo máte doma víc lan různých délek, pomůže výrazné barevné odlišení. Na skalách s pískovcem a v místech, kde lano leží na zemi, se světlé lano rychleji ušpiní, ale je na něm lépe vidět poškození. Délku si zapište na štítek nebo na pásku u konce lana, po zkrácení kvůli poškozenému konci se to snadno zapomene.</p>'          '<h2>Vak, plachta a sbalení</h2>'          '<p>Vak na lano s rozkládací plachtou chrání lano před pískem, blátem a jehličím. Lano se do vaku jen volně skládá a před lezením se nemusí přebírat. Na túry se lano nosí sbalené do motouzu přes ramena nebo přivázané pod víkem batohu. Smotávání lana přes loket a dlaň lano kroutí, proto se v kurzech učí skládat ho do tvaru motýla. Po lezení na mokrém skalním podkladu lano doma rozložte a nechte uschnout, než ho uklidíte.</p>'
          '<h2>Co lano nenahradí</h2>'
          '<p>V nabídkách obchodů se slovo lano objevuje i u úplně jiných věcí. Lano na šplh, posilovací battle rope, švihadlo nebo dětské lano na prolézačky nejsou horolezecká lana a k jištění se nehodí. Stejně tak kotvicí lano na loď nebo kempingová šňůra. Horolezecké lano poznáte podle normy EN 892 nebo EN 1891 v popisu a na štítku.</p>'
          '<p>K lanu budete potřebovat sedák, jisticí pomůcku a karabiny. Najdete je v kategoriích <a href="/lezecke-sedaky-a-pomucky/">lezecké sedáky a pomůcky</a> a <a href="/karabiny/">karabiny</a>. Na lezení se hodí i <a href="/lezecke-boty/">lezecké boty</a>.</p>',
    faq=[
        ('Jaké lano koupit na lezeckou stěnu?', 'Jednoduché dynamické lano s průměrem kolem deseti milimetrů vydrží na stěně hodně oděru. Délku zvolte podle výšky stěny, často stačí třicet až čtyřicet metrů.'),
        ('Mohu lézt s dolním jištěním na statickém laně?', 'Ne. Statické lano při pádu skoro nepruží a přenese na lezce i kotvení velkou sílu. K lezení s dolním jištěním slouží dynamická lana podle EN 892.'),
        ('Jaký je rozdíl mezi polovičním a dvojitým lanem?', 'S polovičními lany cvakáte každý pramen do jiného jištění. Dvojitá lana se cvakají vždy oba prameny společně. Typ je vyznačený symbolem na koncích lana.'),
        ('Je potřeba impregnované lano?', 'Na stěnu a do suchých skal ne. Pro hory, led a zimu má smysl, protože impregnované lano nasákne méně vody a v mrazu méně zamrzá.'),
        ('Co znamená UIAA Water Repellent?', 'Lano s tímto označením při normované zkoušce nasáklo méně než pět procent své hmotnosti. Je to nezávislé měřítko, na rozdíl od obchodních názvů výrobců.'),
        ('Jak dlouho horolezecké lano vydrží?', 'Záleží na četnosti používání. Petzl uvádí u textilních výrobků nejvýš deset let od výroby. Při častém lezení se lano opotřebuje mnohem dřív.'),
        ('Kdy lano vyřadit?', 'Když je prodřený oplet, lano má měkká nebo ztvrdlá místa, přišlo do styku s chemikáliemi nebo zachytilo mimořádný pád. Při pochybnostech se poraďte se zkušeným lezcem.'),
        ('Jak dlouhé lano potřebuji do skal?', 'Běžně šedesát metrů, v oblastech s dlouhými cestami sedmdesát. Lano musí být dvakrát delší než cesta, aby šlo lezce spustit.'),
        ('Jak lano prát?', 'Ve vlažné vodě s jemným prostředkem podle návodu výrobce. Sušte ho volně ve stínu, ne na topení ani na přímém slunci.'),
        ('Je lano na šplh horolezecké lano?', 'Ne. Lano na šplh, battle rope nebo lodní lano nejsou certifikovaná k jištění. Horolezecké lano má v popisu normu EN 892 nebo EN 1891.'),
    ])

# ------------------------------------------------------------------ cepiny-a-macky
NEW['cepiny-a-macky'] = dict(long=True,
    title='Cepíny a mačky na hory, skialpy i led',
    desc='Turistické a technické cepíny, mačky košíkové, poloautomatické i automatické. Kompatibilita s botami, materiály a péče.',
    intro='<p><strong>Cepín</strong> a <strong>mačky</strong> jsou základní vybavení pro pohyb po sněhu a ledu v horách. Cepín slouží jako opora při chůzi, k sekání stupů a hlavně k zastavení pádu na sněhovém svahu. Mačky se připínají na boty a dávají jim záběr tam, kde by podrážka klouzala. Obojí ale funguje jen tehdy, když s tím umíte zacházet. Brzdění cepínem nebo chůze v mačkách se nacvičují v kurzu a v bezpečném terénu, ne až ve chvíli, kdy jde o život.</p>'
          '<p>Na Sportece porovnáte nabídky českých e-shopů u turistických i technických cepínů, lehkých skialpových cepínů, maček všech typů i u nesmeků na zimní chůzi. Vyrábějí je Petzl, Black Diamond, Grivel, Camp, Climbing Technology, Simond nebo '
          + B(('salewa', 'Salewa'), ('dynafit', 'Dynafit')) +
          '. Spadají do kategorie <a href="/horolezectvi/">horolezectví</a>. Text je pomůcka k nákupu, výcvik ani zkušeného průvodce nenahrazuje.</p>',
    guide='<h2>K čemu cepín slouží</h2>'
          '<p>Klasický cepín má rovnou nebo mírně prohnutou násadu, hrot na spodním konci a hlavu se zobákem a lopatkou. Při chůzi do svahu se drží za hlavu jako hůl a zapichuje se do sněhu. Lopatkou se vysekávají stupy, zobák slouží k brzdění pádu a k zaseknutí do tvrdého sněhu a ledu. Technické cepíny pro lezení v ledu mají naopak silně zahnutou násadu a ostrý zobák, protože se jimi leze nad hlavou.</p>'
          '<p>Norma EN 13089 rozlišuje dva typy. Typ 1, dříve označovaný B, je základní cepín pro sníh a led s menší zátěží. Typ 2, dříve T, snese větší namáhání a je určený i pro technické lezení. Cepín typu 2 nese na hlavě nebo na násadě písmeno T, typ 1 se nijak neoznačuje.</p>'
          + T(['Druh cepínu', 'Násada', 'Použití'], [
              ['Turistický a horský', 'rovná nebo mírně prohnutá', 'chůze po ledovci, sněhová pole, výstupy normálkami'],
              ['Lehký skialpový', 'krátká, často hliníková hlava', 'skialpinismus, závody, rychlé túry'],
              ['Technický', 'zahnutá, ergonomická rukojeť', 'strmý sníh, kombinovaný terén, horolezecké cesty'],
              ['Ledovcový nástroj', 'výrazně tvarovaná, bez lopatky nebo s kladívkem', 'lezení v ledu a drytooling']]) +
          '<h2>Jak vybrat cepín</h2>'
          '<p>Na túry po ledovci a na výstupy po sněhu se hodí klasický cepín s rovnou nebo jen lehce zahnutou násadou. Delší cepín je lepší jako opora při chůzi, kratší se snáz ovládá ve strmém terénu a méně překáží na batohu. Výrobci nabízejí jednotlivé modely v několika délkách a v návodu nebo na webu uvádějí, jak délku vybrat. Pokud si nejste jistí, poraďte se s instruktorem nebo v odborné prodejně.</p>'
          '<p>Skialpinisté často volí velmi lehké cepíny s hlavou z hliníkové slitiny. Do sněhu jsou dostačující, na tvrdý led a skálu se ale hliníkový zobák rychle otupí nebo poškodí. Ocelová hlava je těžší, zato vydrží víc. Kdo se chystá na kombinovaný terén nebo led, potřebuje technický cepín typu 2 s ocelovým zobákem.</p>'
          '<p>Poutko nebo smyčka zabrání tomu, aby vám cepín při pádu ujel po svahu. Moderní technické nástroje se často používají bez poutka nebo s pružnou smyčkou připnutou k sedáku. Chránič na zobák a lopatku je praktický při přenášení v batohu, aby hroty nic nepoškodily.</p>'
          '<h2>Druhy maček</h2>'
          '<p>Mačky se liší způsobem připevnění k botě a počtem a tvarem hrotů. Prodejci a výrobci bot používají pro orientaci značení C1 až C3 u maček a B0 až B3 u bot. Nejde o normu, ale o zavedený systém, podle kterého se snáz hledá kompatibilita.</p>'
          + T(['Typ maček', 'Upevnění', 'Potřebná bota'], [
              ['C1 košíkové', 'plastové košíky vpředu i vzadu a popruh', 'B1 a tužší, bez nutnosti lemu'],
              ['C2 poloautomatické', 'přední košík a zadní páka', 'B2 a B3 se zadním lemem'],
              ['C3 automatické', 'přední drátěný třmen a zadní páka', 'B3 s předním i zadním lemem']]) +
          '<p>Platí jednoduché pravidlo: kategorie boty musí být stejná nebo vyšší než kategorie maček. Tuhá bota B3 unese i košíkové mačky C1, ale do měkké turistické boty B1 automatické mačky nedáte. Do bot B0, tedy běžných ohebných treků a nízkých bot, se mačky nehodí vůbec. Mačka by na ohebné podrážce praskla nebo se uvolnila.</p>'
          '<h2>Hroty, materiál a antibot</h2>'
          '<p>Turistické a horské mačky mívají deset až dvanáct hrotů, z toho dva přední vodorovné. Ty se hodí na sníh a mírný led. Technické mačky pro lezení v ledu mají přední hroty svislé, někdy jen jeden hrot uprostřed, kterému se říká monopoint. Ocelové mačky jsou odolné a vhodné na led i skálu. Hliníkové jsou výrazně lehčí a oblíbené mezi skialpinisty, na kamení se ale rychle obrušují.</p>'
          '<p>Antibot, plastová nebo gumová deska pod mačkou, brání nalepování mokrého sněhu. Bez ní se pod botou vytvoří sněhová koule a mačky ztratí záběr. U většiny kvalitních maček je antibot součástí balení nebo se dá dokoupit.</p>'
          '<h2>Mačky a nesmeky nejsou totéž</h2>'
          '<p>V zimě se často prodávají lehké nesmeky, tedy pryžové návleky s řetízky a krátkými hroty. Hodí se na zledovatělé cesty, lesní stezky a uklouzané chodníky. Na strmé sněhové svahy, ledovec nebo horolezecké výstupy nestačí, krátké hroty v hlubším sněhu nedrží a do tvrdého ledu se nezakousnou. Pokud jdete do vysokých hor, potřebujete skutečné mačky a boty, které je unesou.</p>'
          '<h2>Kompatibilita s botou</h2>'
          '<p>Před nákupem vezměte mačky do obchodu na boty, se kterými je budete nosit, nebo si porovnejte kategorie podle výrobce. Mačky musí sedět bez vůle, přední hroty by měly přesahovat špičku boty jen o málo a popruh nesmí tlačit. Délka se nastavuje posuvným můstkem, ten se u dlouhých bot někdy musí vyměnit za delší. Norma EN 893 předepisuje, aby návod k mačkám uváděl vhodné boty, takže tam informaci najdete.</p>'
          '<p>Vhodné boty najdete mezi <a href="/vysoke-trekove-boty/">vysokými trekovými botami</a> a v kategorii <a href="/zimni-obuv/">zimní obuv</a>, ke skialpům se hodí <a href="/skialpove-boty/">skialpové boty</a>. Na kategorii boty se ptejte výrobce nebo prodejce, ne každá zimní bota má lem pro poloautomatické mačky.</p>'
          '<h2>Cepín a mačky na skialpech</h2>'          '<p>Skialpinisté nesou cepín a mačky často jen pro případ, že výstup přejde v tvrdý žlab nebo zledovatělý hřeben. Proto u nich hraje velkou roli hmotnost. Lehké hliníkové mačky se upínají na skialpové boty s předními a zadními úchyty a na batohu skoro nezatěžují. Na delší ledové úseky jsou ale ocelové mačky jistější. Pro výstupy po zmrzlém svahu na lyžích slouží jiná pomůcka, takzvané haršajzny, které se připínají k vázání. Mačky na botách nahrazují až tam, kde se lyže sundají a jde se pěšky.</p>'          '<p>Krátký skialpový cepín se dá nosit v držáku na boku batohu, odkud ho vytáhnete bez sundávání. Některé závodní modely mají násadu tak krátkou, že jako opora při chůzi neslouží. Kdo kombinuje skialpy s horolezeckým výstupem na vrchol, často volí univerzální cepín střední délky.</p>'          '<h2>Jak cepín a mačky nosit</h2>'          '<p>Většina horských batohů má na zadní straně poutko a gumu na upevnění cepínu, hlavou dolů a s chráničem zobáku. Mačky patří do obalu nebo pevného vaku, který se dá připnout na batoh nebo vložit dovnitř nahoru. Hroty nesmějí mířit ven, při pádu nebo v přeplněné chatě mohou někoho zranit. Na ledovci se cepín drží v ruce, na batohu je k ničemu ve chvíli, kdy ho potřebujete na zastavení pádu.</p>'
          '<h2>Výcvik a bezpečnost</h2>'
          '<p>Brzdění cepínem po pádu na zádech, hlavou dolů nebo na břiše je dovednost, kterou nikdo nezvládne bez nácviku. Stejně tak chůze v mačkách: kdo se v nich neumí pohybovat, zakopne o vlastní hroty nebo si roztrhne kalhoty. Začněte proto kurzem zimní turistiky nebo vysokohorským kurzem a nejdřív trénujte na mírném svahu s bezpečným dojezdem. Na ledovec patří i lano, sedák a znalost záchrany z trhliny. Vždy sledujte lavinovou předpověď a podmínky na horách.</p>'
          '<h2>Péče a kontrola</h2>'
          '<ul><li>Po túře mačky i cepín osušte a odstraňte nečistoty, aby nekorodovaly.</li>'
          '<li>Pravidelně kontrolujte popruhy, páky a šrouby. Uvolněný šroub nebo prasklý košík vyměňte podle návodu výrobce.</li>'
          '<li>Hroty brouste ručním pilníkem, ne brusným kotoučem, který ocel přehřeje a změkčí.</li>'
          '<li>Mačky převážejte v obalu, aby neprořízly batoh ani oblečení.</li>'
          '<li>Cepín nebo mačky s prasklinou nebo ohnutým dílem vyřaďte.</li></ul>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Při porovnání cepínů sledujte typ podle EN 13089, délku, materiál hlavy a hmotnost. U maček kategorii C, materiál, počet a tvar předních hrotů a to, zda je v balení antibot a obal. Náhradní díly, například delší můstek nebo jiný přední košík, bývají v nabídce zvlášť. K zimnímu vybavení patří i <a href="/trekove-hole/">trekové hole</a> a pro skialpinisty kategorie <a href="/skialpinismus/">skialpinismus</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi cepínem typu 1 a typu 2?', 'Podle EN 13089 je typ 1 základní cepín pro sníh a led. Typ 2 je technický, snese větší zátěž a nese značku T.'),
        ('Pasují mačky na každou botu?', 'Ne. Kategorie boty B musí být stejná nebo vyšší než kategorie maček C. Do ohebných bot B0 se mačky nedávají vůbec.'),
        ('Jaké mačky na zimní turistiku?', 'Na sněhová pole a ledovec se hodí košíkové mačky C1 na botu B1 nebo tužší. Na zledovatělé cesty v lese stačí nesmeky.'),
        ('Jsou nesmeky náhrada maček?', 'Ne. Nesmeky mají krátké hroty a hodí se na zledovatělé stezky. Na strmý sníh, ledovec a horolezecké výstupy potřebujete mačky.'),
        ('Hliníkové, nebo ocelové mačky?', 'Hliníkové jsou lehčí a oblíbené na skialpy, na kamení se ale rychle obrušují. Ocelové jsou odolnější a hodí se na led i skálu.'),
        ('K čemu slouží antibot?', 'Brání nalepování mokrého sněhu pod mačku. Bez něj se pod botou tvoří sněhová koule a mačky ztrácejí záběr.'),
        ('Jak dlouhý cepín vybrat?', 'Delší cepín je lepší opora při chůzi, kratší se snáz ovládá ve strmém terénu. Doporučení k délce uvádějí výrobci u konkrétních modelů.'),
        ('Naučím se brzdit cepínem sám?', 'Brzdění cepínem se nacvičuje v kurzu pod dohledem instruktora, na mírném svahu s bezpečným dojezdem. Tento text výcvik nenahrazuje.'),
        ('Jak brousit hroty maček?', 'Ručním pilníkem podle návodu výrobce. Brusný kotouč ocel přehřeje a hroty změknou.'),
        ('Kde koupit cepín a mačky?', 'Sporteka u každého cepínu a maček ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ nordic-walking-hole
NEW['nordic-walking-hole'] = dict(long=True,
    title='Nordic walking hole pevné i nastavitelné',
    desc='Hole na nordic walking pevné i teleskopické, z hliníku i karbonu. Jak určit délku, poutka s rukavičkou, botičky a hroty.',
    intro='<p><strong>Nordic walking</strong> je rychlá chůze s holemi, při které se paže aktivně odráží a pracuje i horní polovina těla. Na rozdíl od trekových holí, o které se člověk spíš opírá, se nordic walking hole zapichují šikmo za tělo a ruka je na konci odrazu pouští. Proto mají speciální poutko podobné rukavičce, lehkou násadu a pryžovou botičku se zkosením dozadu. Rozšířil se z Finska a dnes ho chodí lidé všech věkových skupin v parku, v lese i na asfaltu.</p>'
          '<p>Na Sportece najdete nabídky českých obchodů u pevných i nastavitelných holí. Prodávají se od značek Leki, Fizan, Gabel, Swix, Silva, Nils nebo '
          + B(('insportline', 'Insportline')) +
          '. Kategorie spadá pod <a href="/trekove-hole/">trekové a nordic walking hole</a>. Správnou techniku je dobré si nechat ukázat od instruktora, protože špatně držené hole ruce spíš unavují.</p>',
    guide='<h2>Čím se liší od trekových holí</h2>'
          '<p>Trekové hole slouží k opoře na horách. Mají dlouhou pěnovou rukojeť, jednoduché poutko, často tlumič a široké talířky do sněhu a bláta. Při chůzi se zapichují před tělo. Nordic walking hole se zapichují za tělo, pracuje se jimi rytmicky a odraz jde přes poutko, ne přes stisk rukojeti. Proto mají úzké rukojeti, poutko kolem dlaně a botičku, která na asfaltu nesklouzne.</p>'
          '<p>Chodit nordic walking s trekovými holemi se dá, ale pohodlné to není. Ruka musí hůl stále svírat a zápěstí se rychle unaví. Opačně to funguje jen částečně: na krátkou túru se nordic walking hole hodí, do strmého terénu a na sníh však trekové hole nenahradí.</p>'
          + T(['Vlastnost', 'Nordic walking hole', 'Trekové hole'], [
              ['Poutko', 'rukavička nebo polorukavice, často odepínací', 'jednoduchý pásek'],
              ['Rukojeť', 'úzká, bez dlouhého pěnového nástavce', 'širší, často s prodlouženou pěnou'],
              ['Délka', 'pevná nebo nastavitelná v malém rozsahu', 'skládací, s velkým rozsahem'],
              ['Spodní konec', 'hrot a zkosená botička na asfalt', 'hrot a talířek do sněhu a bláta'],
              ['Pohyb', 'odraz za tělem', 'opora před tělem']]) +
          '<h2>Jak určit délku hole</h2>'
          '<p>Nejčastěji uváděné orientační pravidlo zní: výška postavy v centimetrech krát 0,68. Člověk měřící 170 cm tak vychází na hole kolem 115 cm. Začátečníkům a lidem, kteří chodí spíš pomaleji, se někdy doporučuje koeficient nižší, kolem 0,62 až 0,65. Pokud vyjde délka mezi dvěma velikostmi, výrobci i prodejci obvykle radí vzít kratší.</p>'
          '<p>Vzorec je jen začátek. Lidé mají různě dlouhé paže a různou techniku. Při kontrole se postavte rovně, hůl držte svisle vedle těla s hrotem na zemi. Loket by měl být ohnutý v úhlu mírně nad devadesát stupňů a předloktí zhruba vodorovně. Kdo chodí rychle a dlouhým krokem, často časem přejde na o něco delší hole.</p>'
          + T(['Výška postavy', 'Orientační délka (× 0,68)'], [
              ['155 cm', 'asi 105 cm'],
              ['165 cm', 'asi 110–115 cm'],
              ['175 cm', 'asi 120 cm'],
              ['185 cm', 'asi 125 cm'],
              ['195 cm', 'asi 130–135 cm']]) +
          '<h2>Pevná, nebo nastavitelná délka</h2>'
          '<p>Hole s pevnou délkou jsou z jednoho kusu. Jsou lehčí, tužší a při došlapu nevibrují ani necvakají. Nic se na nich nemůže povolit. Nevýhodou je, že je musíte koupit v přesné velikosti a hůř se převážejí. Pevné hole se prodávají po pěti centimetrech, proto se délka podle vzorce zaokrouhluje.</p>'
          '<p>Nastavitelné hole mají dva nebo tři díly a zámek. Hodí se, když hole sdílí víc lidí v rodině, když ještě nevíte, jaká délka vám bude vyhovovat, nebo když je chcete brát na cesty. Na trh se dostaly hole s rychlozámkem i se šroubovacím systémem. Rychlozámek se nastavuje snáz a na zimu se ovládá i v rukavicích. U levných teleskopických holí se zámek může časem povolit, proto ho občas dotáhněte.</p>'
          '<h2>Materiál: hliník a karbon</h2>'
          '<p>Hliníkové hole jsou odolné, levnější a při silném nárazu se spíš ohnou, než aby praskly. Hodí se pro začátečníky a pro chůzi v kamenitém terénu. Karbonové nebo kompozitní hole s podílem uhlíkových vláken jsou lehčí a lépe tlumí vibrace, takže zápěstí a lokty dostanou méně otřesů. Výrobci často uvádějí procento karbonu v násadě, čím vyšší podíl, tím lehčí a tužší hůl.</p>'
          '<p>Karbon ale hůř snáší boční ránu o kámen nebo zábradlí. Poškrábaná karbonová hůl s hlubokým zářezem může při zatížení prasknout. Kdo chodí po skalnatých stezkách, často zůstane u hliníku.</p>'
          '<h2>Poutka a rukavičky</h2>'
          '<p>Poutko je u nordic walking holí nejdůležitější část. Obepíná dlaň i palec jako polorukavice a umožňuje hůl na konci odrazu pustit, aniž by vypadla z ruky. Hůl se pak sama vrátí do dlaně. Poutka se vyrábějí v několika velikostech nebo se nastavují suchým zipem. Mnoho výrobců má systém, kterým se poutko od hole jedním stiskem odepne, třeba když potřebujete použít telefon nebo se napít. Leki ho nazývá Shark, jiné značky mají vlastní názvy.</p>'
          '<p>Na poutku záleží víc než na hmotnosti hole. Pokud tlačí, odírá nebo je volné, chůze nebude příjemná. Pokud je to možné, vyzkoušejte si hole v ruce, nebo si vyberte model s nastavitelným poutkem. Některé obchody prodávají poutka jako náhradní díl.</p>'
          '<h2>Hroty a botičky</h2>'
          '<p>Na konci hole je ocelový nebo tvrdokovový hrot, který drží v trávě, na lesní cestě i na zmrzlé zemi. Na asfalt, dlažbu a beton se na hrot nasazuje pryžová botička, často zkosená dozadu. Tlumí náraz, nehlučí a nesklouzává. Botičky se opotřebují, proto je dobré mít náhradní. Na zimu se prodávají talířky do sněhu.</p>'
          '<p>Při chůzi po asfaltu botičku nasazujte šikmou plochou dozadu. Na měkkém terénu ji sundejte, jinak hůl nedrží. Kdo chodí hodně po městě, ocení botičky s výměnnou pryží.</p>'
          '<h2>Pár slov k technice</h2>'
          '<p>Hůl jde vždy s opačnou nohou, podobně jako ruce při běžné chůzi. Zapichuje se zhruba v úrovni paty přední nohy, šikmo dozadu. Ruka tlačí hůl dozadu kolem boku a na konci se dlaň otevře. Ramena zůstávají uvolněná. Kdo hole jen nese nebo je klade před sebe, z chůze s holemi moc nemá. Instruktoři nordic walkingu pořádají úvodní lekce, které se vyplatí i lidem, kteří už chodí. Pokud máte potíže s klouby, srdcem nebo jiné zdravotní omezení, poraďte se o vhodné zátěži s lékařem.</p>'
          '<h2>Pro koho jsou nordic walking hole</h2>'          '<p>Chůze s holemi je nenáročná na vybavení a dá se začít v jakémkoli věku. Chodí ji lidé, kteří chtějí víc pohybu bez běhání, běžci v obdobích odpočinku i senioři, kterým hole dodávají jistotu na nerovném povrchu. Kdo má hole hlavně kvůli stabilitě, většinou chodí pomaleji a s kratšími holemi. Kdo s nimi trénuje, chodí rychle a hole jsou delší. Obě skupiny používají stejný typ holí, liší se nastavením a technikou.</p>'          '<p>Hole se hodí do parku, na polní a lesní cesty i na cyklostezky. Na úzkém chodníku s lidmi ohrožují hroty a zkosené botičky ostatní chodce méně než trekové hole, i tak je dobré dávat pozor. V horách s velkým převýšením a v kamení jsou lepší trekové hole s talířkem a pěnovou rukojetí.</p>'          '<h2>Údržba holí</h2>'          '<ul><li>Teleskopické hole po dešti rozložte a nechte díly uschnout, jinak zámek může zarezavět nebo se zaseknout.</li>'          '<li>Botičky kontrolujte a sjeté vyměňte, než se prochodí až na kov.</li>'          '<li>Poutka občas vyperte ve vlažné vodě s mýdlem, pot a nečistoty je časem zatvrdí.</li>'          '<li>Ohnutou hliníkovou hůl nerovnejte, kov v místě ohybu je oslabený. Karbonovou hůl s hlubokým zářezem vyřaďte.</li>'          '<li>Hrot z tvrdokovu vydrží dlouho, ale po čase se otupí. U většiny výrobců se dá vyměnit jako náhradní díl.</li></ul>'
          '<h2>Oblečení a doplňky</h2>'
          '<p>Na nordic walking stačí pohodlné oblečení na pohyb a obuv s dobrou podrážkou. Hodí se lehké <a href="/nizke-trekove-boty/">nízké trekové boty</a> nebo běžecké boty do terénu. V chladu oceníte tenké <a href="/sportovni-rukavice/">sportovní rukavice</a>, které se vejdou do poutka. Kdo si chce hlídat tempo, použije <a href="/sportovni-hodinky/">sportovní hodinky</a>.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Nabídky porovnávejte podle délky, typu (pevná nebo nastavitelná), materiálu, hmotnosti páru, typu poutka a toho, co je v balení. Botičky by měly být součástí. U pevných holí se ujistěte, že kupujete správnou velikost, výměna kvůli délce je zbytečná komplikace. Hole se prodávají v páru, u některých obchodů ale i po kusech jako náhrada.</p>',
    faq=[
        ('Jak dlouhé nordic walking hole potřebuji?', 'Orientačně výška postavy v centimetrech krát 0,68. Začátečníci volí spíš kratší. Při držení hole by měl být loket ohnutý mírně nad devadesát stupňů.'),
        ('Pevné, nebo nastavitelné hole?', 'Pevné jsou lehčí a tužší, ale musíte trefit délku. Nastavitelné se hodí pro víc uživatelů, na cesty nebo když hledáte svou délku.'),
        ('Mohu na nordic walking použít trekové hole?', 'Jde to, ale pohodlné to není. Trekové hole nemají poutko jako rukavičku, takže je musíte stále svírat a zápěstí se unaví.'),
        ('Karbon, nebo hliník?', 'Karbonové hole jsou lehčí a lépe tlumí vibrace. Hliníkové jsou odolnější proti nárazům a hodí se do kamenitého terénu.'),
        ('K čemu jsou gumové botičky?', 'Na asfalt a dlažbu. Tlumí náraz, nehlučí a nesklouzávají. V lese a na trávě je sundejte, aby hrot držel.'),
        ('Proč mají nordic walking hole poutko jako rukavici?', 'Poutko umožňuje hůl na konci odrazu pustit a zase ji chytit, aniž by vypadla. Odraz jde přes poutko, ne přes stisk rukojeti.'),
        ('Pomáhá nordic walking při zdravotních potížích?', 'Je to sportovní aktivita, ne léčba. Pokud máte potíže s klouby, srdcem nebo jiné zdravotní omezení, poraďte se o vhodné zátěži s lékařem.'),
        ('Mám se naučit techniku od instruktora?', 'Vyplatí se to. Špatně držené hole ruce unavují a z chůze s nimi pak nemáte velký užitek. Úvodní lekce trvá jen chvíli.'),
        ('Jak poznat, že je hůl moc dlouhá?', 'Ramena se zvedají, paže je při zapichování příliš vysoko a odraz za tělem je krátký. Kratší hůl se ovládá snáz.'),
        ('Kde koupit nordic walking hole?', 'Sporteka u každého páru holí ukáže nabídky českých e-shopů. Objednávku dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ hrudni-pasy
NEW['hrudni-pasy'] = dict(long=True,
    title='Hrudní pásy a snímače tepu na trénink',
    desc='Hrudní pásy a snímače tepové frekvence s Bluetooth a ANT+. Rozdíl proti optickému měření, kompatibilita, baterie a praní pásu.',
    intro='<p><strong>Hrudní pás</strong> je snímač, který měří tep přímo na hrudi a posílá ho do hodinek, cyklopočítače, mobilu nebo trenažéru. Skládá se z textilního nebo pryžového pásku s elektrodami a z malého vysílače, který se na pásek zacvakne. Měří elektrický signál srdce, a proto při intervalech, sprintech a v chladu reaguje rychleji a spolehlivěji než optický snímač na zápěstí. Sportovci ho používají na trénink podle zón, na kole, na běžeckém pásu i ve fitness.</p>'
          '<p>Na Sportece porovnáte nabídky českých obchodů u hrudních pásů s Bluetooth a ANT+, u starších analogových 5kHz pásů pro posilovací stroje i u náhradních popruhů. Najdete tu pásy Polar, Suunto, Tunturi, Sigma nebo '
          + B(('garmin', 'Garmin')) +
          '. Kategorie patří pod <a href="/sportovni-hodinky/">sportovní hodinky</a>. Hrudní pás je sportovní pomůcka, ne zdravotnický prostředek, a nehodí se k diagnostice.</p>',
    guide='<h2>Hrudní pás, nebo měření na zápěstí</h2>'
          '<p>Většina chytrých a sportovních hodinek dnes měří tep opticky. Na spodní straně svítí diody do kůže a senzor sleduje, jak se mění průtok krve. Při klidném běhu nebo chůzi to funguje dobře. Problém nastává, když se hodinky na ruce hýbou, když je zima a prsty a zápěstí jsou méně prokrvené, při posilování s pevným stiskem nebo při rychlých změnách tempa. Optický senzor pak reaguje se zpožděním nebo ukazuje nesmysly. Ovlivnit ho může i tetování na zápěstí.</p>'
          '<p>Hrudní pás měří elektrický signál srdce podobně jako elektrody na EKG, jen v mnohem jednodušší podobě. Údaj je stabilní i při prudkých změnách zátěže. Proto ho používají lidé, kteří trénují podle tepových zón, jezdí intervaly na kole nebo chtějí přesná data pro analýzu tréninku.</p>'
          + T(['', 'Hrudní pás', 'Optický snímač na zápěstí'], [
              ['Princip', 'elektrický signál srdce', 'změny průtoku krve pod kůží'],
              ['Rychlé změny tepu', 'zachytí rychle', 'často se zpožděním'],
              ['Pohodlí', 'musíte si ho nasadit', 'nosíte ho stále'],
              ['Rušivé vlivy', 'suché elektrody, statická elektřina', 'pohyb hodinek, chlad, tetování'],
              ['Použití', 'trénink v zónách, intervaly, kolo', 'celodenní sledování, klidné aktivity']]) +
          '<h2>Bluetooth a ANT+</h2>'
          '<p>Moderní hrudní pásy vysílají dvěma bezdrátovými standardy. <strong>Bluetooth</strong> (Bluetooth Smart, Bluetooth Low Energy) umí každý mobil a většina hodinek. Počet současných spojení je u Bluetooth omezený: některé pásy umějí jen jedno, Polar H10 například dvě. <strong>ANT+</strong> je protokol rozšířený hlavně u cyklopočítačů, sportovních hodinek a trenažérů a signál z jednoho pásu může přijímat víc zařízení najednou.</p>'
          '<p>Před nákupem zkontrolujte, co podporují vaše hodinky, cyklopočítač nebo aplikace. Pás, který umí oba standardy, je univerzálnější. Párování se dělá v nabídce senzorů v hodinkách nebo v aplikaci, pás je při tom potřeba mít nasazený nebo alespoň navlhčené elektrody, jinak se nezapne. Po výměně baterie se u některých modelů musí pás spárovat znovu. Pokud v posilovně nebo na závodě vidíte v seznamu víc pásů, vybírejte podle čísla zařízení, které je u mnoha modelů napsané na vysílači. Pokud chcete posílat tep zároveň do hodinek a do aplikace na trenažéru, hodí se pás s ANT+ nebo se dvěma Bluetooth spojeními.</p>'
          '<h2>Analogové pásy 5 kHz</h2>'
          '<p>Starší a levnější pásy vysílají analogový signál na frekvenci 5 kHz. Přijímají ho hlavně posilovací a kardio stroje ve fitness centrech, některé <a href="/behaci-pasy/">běžecké pásy</a>, rotopedy a starší sporttestery. Mobil ani moderní hodinky tento signál nepřijmou. Pokud si pás kupujete k domácímu trenažéru, ověřte v návodu stroje, jaký příjem podporuje. Některé pásy umějí analogový i digitální přenos najednou.</p>'
          '<h2>Funkce navíc</h2>'
          '<p>Základní pás posílá jen tep a intervaly mezi údery, ze kterých hodinky nebo aplikace počítají variabilitu srdečního rytmu. Dražší modely mají vlastní paměť, takže zaznamenají trénink i bez spárovaného zařízení a data se později nahrají. To se hodí například při plavání, protože Bluetooth pod vodou nefunguje. Garmin uvádí, že model HRM-Dual při plavání tep nevysílá. Některé pásy měří i běžecké parametry, jako je kmitání těla nebo doba kontaktu se zemí, ty ale zobrazí jen kompatibilní hodinky.</p>'
          '<h2>Baterie</h2>'
          '<p>Většina pásů má výměnnou knoflíkovou baterii. Typ se mezi modely liší a výrobci ho uvádějí v návodu. Polar u modelu H10 používá baterii CR2025 a výslovně upozorňuje, že CR2032 se do něj dávat nesmí. Garmin HRM-Dual naopak používá CR2032. Před nákupem náhradní baterie se proto podívejte do návodu nebo na víčko vysílače.</p>'
          '<p>Novější modely mají i nabíjecí akumulátor, například Garmin HRM 600. Odpadá výměna baterie, ale pás je potřeba občas nabít. Výdrž se u různých modelů liší od desítek hodin po roky běžného tréninku a závisí na tom, jak často pás používáte.</p>'
          '<h2>Jak pás nasadit</h2>'
          '<p>Pásek se nasazuje pod prsní svaly, vysílač je uprostřed hrudi. Musí sedět pevně, aby se při pohybu neposouval, ale nesmí omezovat dýchání. Před startem navlhčete elektrody vodou nebo gelem, zvlášť v suchém a chladném počasí. Bez vlhkosti pás na začátku tréninku ukazuje chybné hodnoty, dokud se nezačnete potit.</p>'
          '<p>Nepřesná čísla způsobuje i statická elektřina z některých syntetických triček v suchém vzduchu nebo uvolněný pásek. Ženy obvykle nosí pás pod sportovní podprsenkou, některé podprsenky mají pro vysílač vlastní úchyt.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Pot obsahuje soli, které časem poškozují elektrody i kontakty. Výrobci proto radí pásek po každém použití opláchnout a pravidelně prát. Polar u textilních pásů doporučuje praní v pračce na 40 °C, vždy bez vysílače, bez bělidla a aviváže, ideálně v pracím sáčku. Nižší teplota podle Polaru nečistoty z elektrod neodstraní, vyšší pásek poškodí. Garmin u HRM-Dual uvádí oplachování po každém použití a praní v pračce zhruba po každém sedmém tréninku.</p>'
          '<ul><li>Vysílač před praním vždy odpojte, do pračky nepatří.</li>'
          '<li>Pásek nesušte v sušičce ani na topení, nechte ho volně uschnout.</li>'
          '<li>Neskladujte vlhký pásek s nasazeným vysílačem, baterie se zbytečně vybíjí.</li>'
          '<li>Kontakty vysílače otírejte suchým hadříkem.</li></ul>'
          '<p>Textilní pásek se opotřebuje dřív než vysílač. Když začne ukazovat nesmyslné hodnoty i po vyprání a s novou baterií, obvykle pomůže nový popruh. Ověřte si, že je kompatibilní s vaším vysílačem.</p>'
          '<h2>Tepové zóny a trénink</h2>'          '<p>Hlavní důvod, proč si lidé hrudní pás kupují, je trénink podle tepových zón. Zóny se počítají z maximální tepové frekvence nebo z prahových hodnot a hodinky je pak během tréninku hlídají. Odhady maximálního tepu podle věku jsou jen hrubé a u konkrétního člověka se mohou výrazně lišit. Přesnější hodnoty dává zátěžový test u sportovního lékaře nebo v laboratoři. Kdo s tréninkem podle tepu začíná, měl by si nechat nastavení zón poradit od trenéra.</p>'          '<p>Hrudní pás pomáhá hlavně v tom, že ukáže okamžitou reakci na zátěž. Při intervalech je vidět, jak rychle tep vyskočí a jak rychle se vrací. Při dlouhém klidném výběhu zase pás pohlídá, abyste nepřekračovali zvolenou intenzitu. Data se ukládají do aplikace, kde se dají porovnávat mezi tréninky.</p>'          '<h2>Na kole a na trenažéru</h2>'          '<p>Cyklisté si hrudní pás páruje s cyklocomputerem a často i s chytrým trenažérem nebo aplikací na virtuální jízdu. Výkon se na kole měří wattmetrem, tep k němu doplňuje, jak tělo zátěž snáší. Optický snímač na zápěstí trpí na kole otřesy řídítek a pevným úchopem, proto je pás na kole častější volbou. Pokud používáte trenažér a zároveň hodinky, hodí se pás s ANT+ nebo se dvěma Bluetooth kanály. Na běžeckých pásech a rotopedech v posilovně se zase uplatní pás s analogovým přenosem.</p>'          '<h2>Velikost a pohodlí</h2>'          '<p>Popruh se nastavuje přezkou. U větších nebo menších postav se někdy musí dokoupit popruh jiné velikosti, výrobci je prodávají ve dvou až třech délkách. Měkký textilní popruh je pohodlnější než starší pryžové pásy a méně dře. Nový pás se může první tréninky zdát nezvyklý, většina lidí si na něj ale rychle zvykne. Pokud pás dře pod prsními svaly, zkontrolujte, zda není utažený příliš, nebo použijte trochu vazelíny na kraje popruhu, ne na elektrody.</p>'
          '<h2>Co hrudní pás neumí</h2>'
          '<p>Hrudní pás pro sport není lékařský přístroj a nehodnotí, zda je srdeční rytmus v pořádku. Pokud vám hodnoty připadají zvláštní, máte bušení srdce, závratě, bolest na hrudi nebo dušnost, přerušte trénink a obraťte se na lékaře. Kdo má srdeční onemocnění nebo kardiostimulátor, měl by se o používání pásu a o tréninkové zátěži poradit s lékařem.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>Porovnávejte podporované přenosy (Bluetooth, ANT+, 5 kHz), počet současných spojení, vlastní paměť, typ baterie, vodotěsnost a velikost pásku. Některé pásy se prodávají ve velikostech S až XXL, jindy se dodává univerzální délka. Pás se hodí i k <a href="/chytre-hodinky/">chytrým hodinkám</a> a ke <a href="/cyklo-computery/">cyklocomputerům</a>.</p>',
    faq=[
        ('Je hrudní pás přesnější než hodinky?', 'Při rychlých změnách tempa, intervalech a v chladu obvykle ano, protože měří elektrický signál srdce. Při klidné aktivitě jsou rozdíly menší.'),
        ('Funguje hrudní pás s mobilem?', 'Ano, pokud vysílá přes Bluetooth. Analogové 5kHz pásy s mobilem nefungují, ty jsou určené pro posilovací a kardio stroje.'),
        ('Co je ANT+?', 'Bezdrátový protokol rozšířený u sportovních hodinek, cyklopočítačů a trenažérů. Signál z jednoho pásu může přijímat víc zařízení najednou.'),
        ('Jakou baterii má hrudní pás?', 'Záleží na modelu. Polar H10 používá CR2025, Garmin HRM-Dual CR2032. Některé novější modely mají nabíjecí akumulátor.'),
        ('Jak prát hrudní pás?', 'Bez vysílače, podle návodu výrobce. Polar doporučuje u textilních pásů pračku na 40 °C bez aviváže, sušení volně, ne v sušičce.'),
        ('Proč pás na začátku ukazuje nesmysly?', 'Elektrody jsou suché. Navlhčete je před startem vodou nebo gelem. Vadit může i volný pásek nebo statická elektřina z trička.'),
        ('Funguje hrudní pás při plavání?', 'Bluetooth pod vodou nefunguje. Některé pásy ukládají data do paměti a nahrají je po plavání, jiné při plavání tep nevysílají.'),
        ('Je hrudní pás zdravotnický prostředek?', 'Ne. Je to sportovní snímač a nehodí se k diagnostice. Při potížích se srdcem nebo zvláštních hodnotách se obraťte na lékaře.'),
        ('Mohu koupit jen nový popruh?', 'Ano, popruhy se prodávají zvlášť. Ověřte si, že je kompatibilní s vaším vysílačem.'),
        ('Kde koupit hrudní pás?', 'Na Sportece vidíte nabídky českých e-shopů u jednotlivých pásů. Objednávku dokončíte v obchodě, který si vyberete.'),
    ])

# ------------------------------------------------------------------ solarni-nabijecky
NEW['solarni-nabijecky'] = dict(long=True,
    title='Solární nabíječky, panely a powerbanky',
    desc='Rozkládací solární panely, solární powerbanky a přenosné nabíjecí stanice. Kolik reálně dodají, výkon ve wattech a kapacita.',
    intro='<p><strong>Solární nabíječka</strong> mění sluneční světlo na elektřinu, kterou nabijete telefon, hodinky, čelovku nebo powerbanku tam, kde není zásuvka. Pod tímto názvem se prodávají tři dost odlišné věci: rozkládací solární panely s USB výstupem, powerbanky s malým solárním článkem na krytu a velké přenosné nabíjecí stanice, ke kterým se panel připojuje kabelem. Každá se hodí na něco jiného a od každé se dá čekat jiný výkon.</p>'
          '<p>Sporteka staví vedle sebe nabídky českých e-shopů u solárních panelů, solárních powerbank i sad nabíjecí stanice s panelem. Najdete tu výrobky značek Viking Technology, Bluetti, Anker, Sandberg nebo Xtorm. Solární nabíječky jsou součástí kategorie <a href="/powerbanky-a-nabijeni/">powerbanky a nabíjení</a> a hodí se na <a href="/kemping/">kemping</a>, chatu i na delší túry. Počítejte s tím, že skutečný výkon závisí na počasí a slunci víc než na údaji na krabici.</p>',
    guide='<h2>Tři druhy solárních nabíječek</h2>'
          + T(['Typ', 'Co to je', 'Kdy dává smysl'], [
              ['Rozkládací solární panel', 'několik článků v textilním obalu, USB nebo DC výstup', 'vícedenní túry, kemping, nabíjení powerbanky přes den'],
              ['Solární powerbanka', 'běžná powerbanka s malým panelem na krytu', 'nouzové dobití, hlavně se nabíjí ze sítě'],
              ['Nabíjecí stanice s panelem', 'velká baterie se zásuvkami 230 V a vstupem pro panel', 'karavan, chata, delší pobyt bez elektřiny']]) +
          '<p>Rozdíl mezi typy je hlavně v ploše panelu. Výkon panelu roste s jeho plochou, takže malý článek na powerbance velikosti telefonu dá jen zlomek toho, co rozložený panel velikosti cestovní mapy. U nabíjecí stanice se zase pracuje s panely o výkonu desítek až stovek wattů.</p>'
          '<h2>Co znamená výkon ve wattech</h2>'
          '<p>Výkon panelu se uvádí ve wattech a měří se v laboratoři za standardních podmínek: osvit 1000 W na metr čtvereční, teplota článků 25 °C a slunce kolmo na panel. Venku se tyto podmínky sejdou jen výjimečně, v létě kolem poledne a při ideálním natočení. Skutečný výkon je proto obvykle nižší. Panel se na slunci zahřívá a s teplotou výkon klesá. V oblačném dni může spadnout na malý zlomek štítkové hodnoty.</p>'
          '<p>Při plánování proto nepočítejte s nominálními watty, ale s tím, kolik energie panel dodá za celý den. Uvádí se ve watthodinách (Wh). Pokud panel dodá v průměru polovinu svého výkonu po dobu několika hodin, dostanete realistický odhad. V zimě, ve stínu stromů nebo pod mraky to bude méně.</p>'
          '<h2>Kolik energie potřebujete</h2>'
          '<p>Kapacita powerbank se uvádí v mAh, což pro porovnání s panelem není praktické. Převod na watthodiny je jednoduchý: mAh vynásobte napětím článku, obvykle 3,6 nebo 3,7 V, a vydělte tisícem. Powerbanka 10 000 mAh tak má zhruba 37 Wh. Telefon má baterii obvykle v rozsahu desítek watthodin podle modelu, hodinky a čelovky mnohem méně.</p>'
          + T(['Kapacita powerbanky', 'Přibližná energie', 'Co z toho plyne'], [
              ['10 000 mAh', 'asi 37 Wh', 'malý panel na krytu ji ze slunce plní mnoho hodin'],
              ['20 000 mAh', 'asi 74 Wh', 'na túru se hodí rozkládací panel'],
              ['nabíjecí stanice', 'stovky Wh', 'potřeba velkého panelu a celého slunečného dne']]) +
          '<p>Z tabulky je vidět, proč solární powerbanky nelze brát jako náhradu nabíječky do zásuvky. Malý článek na krytu má výkon jednotek wattů a ještě méně v praxi. Výrobci je navrhují tak, že se powerbanka plní hlavně přes USB doma a slunce slouží k přilepšení na cestě.</p>'
          '<p>Při počítání nezapomeňte na ztráty. Powerbanka při nabíjení telefonu převádí napětí a část energie se změní v teplo. Plná powerbanka proto nabije telefon méněkrát, než by vyšlo z prostého podílu kapacit. Podobné ztráty vznikají i mezi panelem a powerbankou a u nabíjecí stanice při převodu na 230 V. Rozumné je počítat s rezervou a energii šetřit: vypnout v telefonu, co nepotřebujete, a na noc ho dát do letového režimu.</p>'
          '<h2>Rozkládací panely na túry</h2>'
          '<p>Pro túry se prodávají skládací panely s několika články, často s oky nebo karabinami na připevnění k batohu nebo stanu. Obvyklý je výstup USB-A, novější panely mají i USB-C s funkcí Power Delivery. Elektronika v panelu hlídá napětí, ale při přechodu mraku se nabíjení přerušuje a telefon pak může nabíjení zastavit nebo restartovat. Praktičtější je proto přes den nabíjet powerbanku a z ní večer telefon.</p>'
          '<ul><li><strong>Natočte panel ke slunci:</strong> každá odchylka od kolmého směru snižuje výkon. Během dne ho občas otočte za sluncem.</li>'
          '<li><strong>Chraňte ho před stínem:</strong> i stín větve nebo popruhu na části panelu může výkon výrazně snížit.</li>'
          '<li><strong>Nenechávejte nabíjená zařízení na slunci:</strong> telefon i powerbanka se přehřejí a nabíjení se zpomalí nebo zastaví. Schovejte je do stínu pod panel.</li>'
          '<li><strong>Panel na batohu:</strong> nabíjí jen tehdy, když jdete s panelem ke slunci. V lese nebo při chůzi na sever toho moc nedodá.</li></ul>'
          '<h2>Přenosné nabíjecí stanice</h2>'
          '<p>Nabíjecí stanice je velká baterie se zásuvkami 230 V, USB porty a často i výstupem 12 V do auta. Kapacita se pohybuje od zhruba dvou set watthodin po několik kilowatthodin. Uvnitř mají regulátor, který z panelu odebírá co nejvíc energie. U sad s panelem se vyplatí zkontrolovat, jaký maximální příkon ze slunce stanice přijme a jaké napětí panelu snese.</p>'
          '<p>Novější stanice často používají články LiFePO4, které podle výrobců snesou víc nabíjecích cyklů než běžné lithium-iontové články, jsou ale těžší. Stanice s kapacitou kolem tisíce watthodin váží přes deset kilogramů, takže na batoh se nehodí. Využijete ji v karavanu, na chatě, při rybaření nebo jako zálohu při výpadku proudu. Elektrospotřebiče s velkým příkonem, jako je varná konvice nebo vařič, ji vybijí rychle.</p>'
          '<h2>Odolnost a provoz venku</h2>'
          '<p>Panely do terénu bývají potažené odolnou tkaninou a články jsou chráněné fólií. Krytí proti vodě se uvádí kódem IP. Panel snese déšť, ale konektory a elektronika ve sběrné kapse vodu nemají rády. Po dešti panel otřete a nechte uschnout rozložený. Ostré předměty, přehnutí přes články a trvalé ležení na rozpáleném autě mu škodí.</p>'
          '<p>Baterie neskladujte dlouhodobě úplně vybité ani na sto procent v horku. Lithiové články nemají rády mráz při nabíjení a teplo nad běžné letní teploty. Výrobci nabíjecích stanic obvykle radí stanici občas dobít, i když ji zrovna nepoužíváte.</p>'
          '<h2>Kabely, konektory a nabíjení</h2>'          '<p>U panelů na túry zkontrolujte, jaké kabely jsou v balení a zda pasují k vašim zařízením. Starší panely mají jen USB-A, k telefonu s USB-C pak potřebujete redukci nebo kabel. Panely s USB-C Power Delivery dokážou nabíjet rychleji, ale jen tehdy, když na ně svítí dost slunce. Pokud chcete panelem nabíjet nabíjecí stanici, potřebujete výstup DC nebo konektor, který stanice podporuje. Výrobci obvykle uvádějí, s jakými panely jsou jejich stanice kompatibilní.</p>'          '<p>Kvalita kabelu má vliv i na nabíjení ze slunce. Dlouhý a tenký kabel ztrácí víc energie, proto je lepší mít panel blízko powerbanky. Kabely k panelu v batohu upevněte tak, aby se při chůzi nevytrhly z konektoru.</p>'          '<h2>Časté chyby</h2>'          '<ul><li>Očekávání, že malý panel na powerbance ji nabije za jeden den.</li>'          '<li>Panel položený naplocho na zemi v ranním nebo večerním slunci, kdy dodá jen malou část výkonu.</li>'          '<li>Telefon připojený přímo k panelu na rozpáleném slunci.</li>'          '<li>Nákup podle nejvyššího čísla ve wattech bez ohledu na plochu a hmotnost panelu.</li>'          '<li>Nabíjecí stanice vybraná bez spočítání spotřeby spotřebičů, které na ni chcete připojit.</li></ul>'
          '<h2>Powerbanky v letadle</h2>'
          '<p>Kdo letí na dovolenou se solární powerbankou, musí ji mít v příručním zavazadle, do odbavených zavazadel lithiové baterie nepatří. Podle pravidel IATA se powerbanky do 100 Wh obvykle převážet smějí. Mezi 100 a 160 Wh je potřeba souhlas letecké společnosti a nad 160 Wh se na palubu nesmějí. Letecké společnosti mohou mít přísnější pravidla, proto si je před cestou ověřte. Velké nabíjecí stanice do letadla nepatří.</p>'
          '<h2>Jak porovnávat nabídky</h2>'
          '<p>U panelů porovnávejte jmenovitý výkon ve wattech, typ a počet výstupů, rozměry po složení, hmotnost a krytí IP. U solárních powerbank kapacitu v mAh i Wh, výstupní výkon a to, zda umí rychlonabíjení. Výkon panelu na krytu brát jako doplněk. U nabíjecích stanic sledujte kapacitu ve Wh, výkon střídače, typ článků, maximální solární vstup a hmotnost. Sada stanice s panelem bývá praktická, protože konektory k sobě pasují.</p>'
          '<p>Na túry se k solární nabíječce hodí <a href="/celovky-a-svitilny/">čelovky a svítilny</a> nabíjené přes USB, na delší pobyt venku <a href="/stany/">stany</a> a <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</p>',
    faq=[
        ('Nabije solární panel telefon i pod mrakem?', 'Pod mraky výkon výrazně klesne, často na malý zlomek štítkové hodnoty. Nabíjení bude pomalé nebo se bude přerušovat.'),
        ('Kolik reálně dodá solární panel?', 'Méně než výkon na štítku, který platí pro laboratorní podmínky. Záleží na úhlu ke slunci, teplotě panelu, oblačnosti a stínu.'),
        ('Vyplatí se solární powerbanka?', 'Jako powerbanka s nouzovým dobíjením ano. Malý článek na krytu ji ale ze slunce plní mnoho hodin, hlavně se nabíjí ze zásuvky.'),
        ('Jak převést mAh na Wh?', 'Kapacitu v mAh vynásobte napětím článku, obvykle 3,6 nebo 3,7 V, a vydělte tisícem. Powerbanka 10 000 mAh má zhruba 37 Wh.'),
        ('Mám nabíjet telefon přímo z panelu?', 'Jde to, ale při přechodu mraku se nabíjení přerušuje. Praktičtější je nabíjet přes den powerbanku a z ní večer telefon.'),
        ('Jakou nabíjecí stanici na chatu?', 'Podle spotřeby. Spočítejte watthodiny, které denně potřebujete, a vyberte stanici s rezervou. Hlídejte i maximální solární vstup.'),
        ('Mohu si vzít solární powerbanku do letadla?', 'Jen v příručním zavazadle. Podle IATA powerbanky do 100 Wh obvykle ano, 100 až 160 Wh se souhlasem dopravce, nad 160 Wh ne.'),
        ('Je solární panel vodotěsný?', 'Záleží na krytí IP. Články déšť obvykle snesou, konektory a elektronika ale vodu nemají rády. Po dešti panel osušte.'),
        ('Proč se telefon na slunci přestane nabíjet?', 'Přehřeje se a ochrana nabíjení zpomalí nebo zastaví. Nabíjené zařízení dejte do stínu, na slunci nechte jen panel.'),
        ('Kde koupit solární nabíječku?', 'Sporteka u každého panelu, powerbanky a stanice ukáže nabídky českých e-shopů. Nákup dokončíte v obchodě, který si vyberete.'),
    ])
