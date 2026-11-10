"""sporteka.cz — facet landing texts wave 136: panska-elektrokola, helly-hansen-lyzarska-bunda,
panska-sportovni-obuv, real-madrid-dresy. General true facts only, no prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ panska-elektrokola
NEW['panska-elektrokola'] = dict(
    title='Pánská elektrokola: rám, velikost a výběr podle jízdy',
    desc='Pánské elektrokolo: jak vybrat velikost rámu, typ motoru, baterii a brzdy podle tras. Porovnejte nabídku více obchodů a zvolte kolo na dojíždění i výlety.',
    intro='<p>Slovo „pánské“ u elektrokola neříká nic o výkonu motoru, týká se hlavně rámu. Pánský rám má obvykle vodorovnou nebo mírně skloněnou horní trubku, která kolo zpevňuje, a sedlo i řidítka bývají nastavené pro vyšší postavu s delšíma rukama. Na této stránce jsou elektrokola z kategorie <a href="/elektrokola/">elektrokola</a>, která výrobci označují jako pánská, tedy městská, trekingová, horská i skládací. '
          'Průvodce vysvětluje, jak vybrat velikost rámu podle výšky a délky nohou, kdy se vyplatí rám s nízkým nástupem i pro muže, jak poznat kvalitní baterii a motor a čím se liší kolo na dojíždění od stroje do terénu. Najdete tu také přehled běžných chyb, které se u prvního elektrokola opakují, a odpovědi na otázky, na které se kupující nejčastěji ptají. Nabídky více obchodů vidíte vedle sebe, takže snadno poznáte, kde je vaše velikost skladem.</p>',
    guide='<h2>Co znamená pánský rám u elektrokola</h2>'
          '<p>Pánský rám se odborně nazývá diamantový nebo klasický. Má horní trubku, která spojuje hlavovou část s podsedlovou, a díky tomu je tuhý a lehčí než rám s nízkým průvlekem. U elektrokola to platí dvojnásob, protože na rámu visí baterie a často i motor, takže tuhost určuje, jak stabilně kolo drží stopu při rychlém sjezdu nebo plné zátěži. Horní trubka však znamená, že při nasedání musíte zvednout nohu přes sedlo nebo přes ni, což při košíku s nákupem nebo brašnami není příjemné.</p>'
          '<p>Kategorie pánských elektrokol proto není uzavřená. Řada výrobců dělá stejný model ve dvou provedeních, s horní trubkou a s nízkým nástupem. Pro starší jezdce, pro lidi po úrazu kolena nebo pro ty, kdo kolo často zastavují v provozu, je nízký nástup rozumnější volba, i když je formálně označený jako dámský. Podobně může nízkou nebo střední trubku preferovat každý, kdo vozí děti v sedačce. V nabídce proto nechte rozhodovat pohodlí, ne štítek. Variantu s nízkým průvlekem najdete také v kategorii <a href="/damska-elektrokola/">dámská elektrokola</a>.</p>'
          + T(['Typ rámu', 'Hlavní výhoda', 'Slabina'], [
              ['Diamantový, vodorovná horní trubka', 'tuhost a nízká hmotnost rámu', 'vyšší nástup, horší při nákladu'],
              ['Skloněná horní trubka', 'kompromis, nižší průvlek než u klasiky', 'o něco menší prostor pro rámový batoh'],
              ['Nízký průvlek (step-through)', 'pohodlný nástup a sesedání', 'nižší tuhost, větší hmotnost'],
              ['Skládací rám', 'úschova v bytě a v autě', 'menší kola, jiné jízdní vlastnosti'],
              ['Nákladní a prodloužený rám', 'nosnost a stabilita při zátěži', 'délka a velká hmotnost']]) +
          '<h2>Velikost rámu podle výšky a délky nohou</h2>'
          '<p>Velikost rámu se nejčastěji uvádí v palcích nebo v písmenech S až XL. Čísla v palcích označují délku sedlové trubky, písmena jsou orientační a každá značka je definuje trochu jinak. Pro první orientaci poslouží přehled níže, ale rozhodující je tabulka konkrétního výrobce. Druhým měřítkem je délka vnitřní strany nohy: stoupněte si bez bot ke zdi, vložte mezi nohy knihu a změřte vzdálenost od podlahy po horní hranu knihy. Rámy s horní trubkou by měly mít po nasednutí na kolo rozestup mezi trubkou a rozkrokem alespoň několik centimetrů.</p>'
          + T(['Výška postavy', 'Orientační velikost', 'Poznámka'], [
              ['do 170 cm', 'S, přibližně 16–17 palců', 'u horských kol zkontrolujte, zda lze sedlo snížit'],
              ['170–180 cm', 'M, přibližně 18–19 palců', 'nejčastější volba pro průměrnou postavu'],
              ['180–190 cm', 'L, přibližně 20–21 palců', 'ověřte délku horní trubky, aby se nesedělo příliš natažený'],
              ['nad 190 cm', 'XL a výš', 'nabídka se zužuje, hledejte vyšší rámy nebo delší sedlovku']]) +
          '<p>Jde o hrubý odhad. Člověk s dlouhýma nohama a krátkým trupem sedí lépe na menším rámu s delší sedlovkou, člověk s krátkýma nohama na větším rámu s kratším představcem. Když kupujete na dálku, vždy si poznamenejte nejen velikost, ale i uváděnou výšku jezdce a kolo po doručení před prvním výletem nastavte. Řidítka by měla být ve výšce sedla nebo mírně nad ní, kolena se při šlapání nesmějí natahovat do úplného propnutí.</p>'
          '<h2>Motor: kde sedí a co to znamená při jízdě</h2>'
          '<p>Pro muže, kteří jezdí delší trasy nebo do kopců, je největší rozdíl mezi motorem u středového složení a motorem v zadním kole. Střední motor, který najdete u značek jako ' + B(('specialized', 'Specialized'), ('trek', 'Trek'), ('crussis', 'Crussis')) + ', sedí u kliky, takže těžiště zůstává nízko a využívají se převody. Hodí se do kopců a do terénu. Motor v zadním náboji je jednodušší, kolo působí přirozeně a na rovině dobře táhne, ale ve strmém stoupání se přehřívá dřív. Přední motor se dnes u kvalitních kol vyskytuje zřídka, protože přidává tah do předního kola a snižuje přilnavost.</p>'
          '<p>Točivý moment motoru se uvádí v newtonmetrech. Vyšší číslo znamená silnější rozjezd a stoupání, ne vyšší rychlost, protože pomoc se u evropských kol vypíná při dosažení zákonné hranice. Pokud jezdíte po rovině a stačí vám dojet do práce, bohatě vystačí motor s nižším momentem a menší baterie. Pokud máte v okolí kopce nebo vozíte náklad, hledejte vyšší moment a střední motor.</p>'
          '<h2>Baterie: kapacita, umístění a péče</h2>'
          '<p>Kapacita baterie se správně udává ve watthodinách, tedy součinem napětí a kapacity v ampérhodinách. Sama hodnota ampérhodin bez napětí je zavádějící, protože dvě baterie s různým napětím ukládají různé množství energie. U dojezdu uváděného v reklamě počítejte s ideálními podmínkami: rovina, nízká podpora, lehký jezdec, teplé počasí. Skutečný dojezd klesá s vyšší hmotností jezdce, protivětrem, studeným počasím a vyšším stupněm asistence.</p>'
          '<ul><li><strong>Vyjímatelná baterie</strong> se dobíjí v bytě a při zimní přestávce se dá skladovat v teple. Vestavěná baterie v rámu vypadá čistěji, ale dobíjí se přímo na kole.</li>'
          '<li><strong>Zámek baterie</strong> chrání před odcizením, když kolo necháte před obchodem.</li>'
          '<li><strong>Skladování:</strong> baterii nenechávejte měsíce zcela vybitou ani plně nabitou, ideální je stav někde uprostřed a suché místo bez mrazu.</li>'
          '<li><strong>Servis:</strong> ověřte, že výrobce nabízí náhradní baterie i za několik let, ne jen celé kolo.</li></ul>'
          '<h2>Typ kola podle způsobu jízdy</h2>'
          '<p>Než porovnáte konkrétní modely, rozhodněte se, kde budete nejvíc jezdit. Na dojíždění po asfaltu stačí městské nebo trekingové kolo s blatníky, nosičem a světly. Na lesní a polní cesty se hodí horské kolo s odpružením, na smíšený terén i s odpružením jen vpředu. Pro ty, kdo kolo vozí v autě nebo bydlí v paneláku, existují skládací modely, které zabírají málo místa. Pro těžký náklad a rodinné jízdy jsou tu nákladní kola s delším rámem.</p>'
          + T(['Kategorie', 'Typické použití', 'Na co se zaměřit'], [
              ['<a href="/trekingova-a-mestska-elektrokola/">Trekingová a městská</a>', 'dojíždění, výlety po silnicích a cyklostezkách', 'blatníky, nosič, světla, pohodlné držení těla'],
              ['<a href="/horska-elektrokola/">Horská</a>', 'lesní trasy, kopce, singltreky', 'střední motor, odpružení, kvalitní brzdy'],
              ['<a href="/silnicni-a-gravel-elektrokola/">Silniční a gravel</a>', 'rychlejší dlouhé trasy, štěrk', 'nízká hmotnost, širší záběr převodů'],
              ['<a href="/fatbike-elektrokola/">Fatbike</a>', 'písek, sníh, bláto', 'velmi široké pneumatiky, vyšší hmotnost'],
              ['<a href="/skladaci-elektrokola/">Skládací</a>', 'kombinace s vlakem, autem, bytem', 'mechanismus skládání, hmotnost při nošení'],
              ['<a href="/nakladni-elektrokola/">Nákladní</a>', 'rodina, nákupy, převoz zboží', 'nosnost, brzdy, stabilita ve stoje']]) +
          '<h2>Brzdy, převody a pneumatiky</h2>'
          '<p>Elektrokolo je těžší než obyčejné kolo a jede rychleji, proto na brzdy nešetřete. Hydraulické kotoučové brzdy dávkují sílu jemněji a při zatáčení na mokru nevyžadují velkou sílu v prstech. Mechanické kotoučové brzdy jsou levnější a snadněji se opravují, ale vyžadují častější seřízení. Čelisťové brzdy se u pánských kol objevují už jen u nejjednodušších modelů a při dlouhém sjezdu s nákladem se unaví nejdřív.</p>'
          '<p>Převody se liší podle způsobu pohonu. Řetěz s přehazovačkou a kazetou je nejběžnější a nejefektivnější, dobře se servisuje. Převodník v zadním náboji je odolný proti nečistotám, hodí se pro dojíždění po zimě a soli. Pneumatiky by měly být přizpůsobené terénu: hladké a užší pro silnici, s profilem a širším průřezem pro pole a les. Při jízdě s nízkým tlakem se tlumí otřesy, ale roste riziko průrazu. Správný tlak vždy najdete na boku pláště a řídí se hmotností jezdce.</p>'
          '<h2>Hmotnost, nosnost a legislativa</h2>'
          '<p>Pánské elektrokolo váží podle typu od menší hodnoty u silničního kola po velmi vysokou u fatbiku s velkou baterií. Při nošení po schodech nebo zdvihání do auta to ucítíte, proto si před koupí představte, jak kolo budete skladovat. U nosnosti sledujte nejen údaj o maximální hmotnosti jezdce, ale i souhrn s nákladem. Překročení mezí poškozuje ráfky, paprsky a rám. V provozu se kolo s motorem pomáhajícím do zákonné hranice rychlosti a s omezeným výkonem považuje za jízdní kolo. Stroje s vyšším výkonem nebo rychlostí patří jinam, často vyžadují registraci a řidičské oprávnění, takže parametry si před koupí přečtěte.</p>'
          '<h2>Chyby při výběru prvního elektrokola</h2>'
          '<ol><li>Řídí se dojezdem z reklamy místo kapacity baterie ve watthodinách.</li>'
          '<li>Podcení velikost rámu a doufají, že sedlo a řidítka všechno vyrovnají.</li>'
          '<li>Vyberou kolo bez ověřeného servisu a při závadě čekají týdny.</li>'
          '<li>Šetří na brzdách a pneumatikách, které musí nést vyšší hmotnost.</li>'
          '<li>Zapomenou na zámek, helmu a blatníky, které se do rozpočtu často nezapočítají.</li></ol>'
          '<p>Výběr usnadní porovnání více modelů stejné kategorie. U výrobců jako ' + B(('engwe', 'Engwe'), ('fafrees', 'Fafrees'), ('samebike', 'Samebike'), ('van-rysel', 'Van Rysel'), ('rockrider', 'Rockrider')) + ' se nabídky liší typem motoru i velikostí baterie, proto je dobré porovnávat modely podle technických údajů, ne podle názvu. Sezónní slevy sledujte ve výběru <a href="/elektrokola-vyprodej/">elektrokola ve výprodeji</a> a značkové kousky najdete na stránce <a href="/elektrokola-crussis/">elektrokola Crussis</a>. K bezpečné jízdě patří i <a href="/cyklisticke-helmy/">cyklistická helma</a>, další vybavení je v kategorii <a href="/cyklistika/">cyklistika</a>.</p>'
          '<h2>Údržba a péče po koupi</h2>'
          '<p>Elektrokolo vyžaduje stejnou péči jako běžné kolo a navíc kontrolu elektrické části. Řetěz se maže častěji, protože motor přenáší větší sílu. Brzdové destičky se opotřebují dřív, proto je kontrolujte po každých několika stovkách kilometrů. Konektory a kontakty baterie nesmí být mokré ani zkorodované. Kolo nemyjte tlakovou vodou přímo na motor nebo displej, použijte houbu a kartáč. Před zimní přestávkou baterii vyjměte a uložte ji v teple na suchém místě. Kvalitní servis ročně prověří dotažení šroubů, opotřebení řetězu a stav ložisek.</p>',
    faq=[
        ('Čím se pánské elektrokolo liší od dámského?', 'Hlavně tvarem rámu. Pánský má horní trubku, takže je tužší, ale nasedání je náročnější. Dámský má nízký průvlek a pohodlnější nástup. Motor, baterie a brzdy bývají stejné.'),
        ('Mám jako muž koupit dámské elektrokolo?', 'Pokud vám dělá potíže nasedání, často zastavujete nebo vozíte náklad, je rám s nízkým průvlekem praktičtější. Pro sportovní jízdu a těžší terén dáte přednost tužšímu rámu s horní trubkou.'),
        ('Jakou velikost rámu mám zvolit?', 'Řiďte se tabulkou výrobce podle výšky a délky nohou. Při výšce 170 až 180 cm se nejčastěji hodí velikost M. Rozdíl pak doladíte výškou sedla a délkou představce.'),
        ('Jaký dojezd mohu čekat?', 'Záleží na kapacitě baterie, hmotnosti jezdce, terénu, počasí a zvolené podpoře. Údaj z reklamy platí za ideálních podmínek, ve skutečném provozu bývá nižší. Spolehlivěji porovnáte kapacitu ve watthodinách.'),
        ('Je lepší střední, nebo zadní motor?', 'Střední motor je výhodnější do kopců, do terénu i pro přirozené řízení. Zadní motor je jednodušší a hodí se na rovinu a do města. Hodnotu momentu a hmotnost motoru porovnávejte u konkrétních kol.'),
        ('Potřebuji na elektrokolo řidičák nebo pojištění?', 'U běžných elektrokol s pomocí do zákonné hranice rychlosti a s omezeným výkonem ne, jedou jako jízdní kola. Rychlejší a silnější stroje se posuzují jinak, proto si parametry před koupí zkontrolujte.'),
        ('Jak dlouho vydrží baterie?', 'Délku života určují nabíjecí cykly, teplota a způsob skladování. Při šetrném zacházení se kapacita snižuje velmi pomalu. Baterii nenechávejte vybitou ani za mrazu a nabíjejte ji původní nabíječkou.'),
        ('Dá se elektrokolo skládat nebo vozit v autě?', 'Skládací modely ano, jsou k tomu stavěné. Běžné elektrokolo je těžké, takže pro nosič na autě ověřte nosnost a hmotnost. Před zdvihnutím vždy vyjměte baterii.'),
        ('Kde elektrokolo servisovat?', 'Nejjistější je servis, který zná motor daného výrobce a má náhradní díly. Před koupí ověřte, kdo opravu zajistí, a zda výrobce nabízí náhradní baterie i po letech.'),
        ('Jak poznám, že je kolo opravdu pánské?', 'Podle popisu výrobce a tvaru rámu. Štítek „pánské“ nese hlavně rám s horní trubkou. Označení unisex znamená, že kolo sedí oběma pohlavím, a rozhoduje pak velikost.'),
    ],
)

# ------------------------------------------------------------------ helly-hansen-lyzarska-bunda
NEW['helly-hansen-lyzarska-bunda'] = dict(
    title='Helly Hansen lyžařská bunda: střih, vrstvení a výběr',
    desc='Helly Hansen lyžařská bunda pro muže, ženy i děti: norská značka pro svah i horský provoz. Jak vybrat model, velikost a vrstvení a porovnat obchody.',
    intro='<p>Helly Hansen je norská značka, která se od počátku věnuje oblečení pro náročné počasí, nejdřív pro rybáře a námořníky, později pro svah a hory. To je znát na bundách: bývají střižené s ohledem na pohyb ve vrstvách, mají praktické kapuce přes helmu a zipy, které se dobře ovládají v rukavicích. Na této stránce jsou lyžařské bundy Helly Hansen z kategorie <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>, pánské, dámské i juniorské. '
          'Průvodce ukazuje, jak se bundy značky řadí podle použití, jak se liší zateplená a skořepinová varianta, jak zvolit velikost podle vrstev pod ní a v čem se Helly Hansen liší od jiných značek. Dozvíte se také, jak na údržbu, aby bunda vydržela několik sezón. Nabídky obchodů vidíte vedle sebe, takže poznáte, kde je váš střih ještě skladem.</p>',
    guide='<h2>Kdo je Helly Hansen a pro koho jsou jeho bundy</h2>'
          '<p>Značku založil norský kapitán na konci devatenáctého století a její zaměření na ochranu před deštěm, větrem a chladem se dodnes promítá do sortimentu. Zimní řada míří k lyžařům, snowboardistům, skialpinistům i návštěvníkům horských středisek, kteří potřebují bundu do mrazu i do mokrého sněhu. Oproti značkám zaměřeným na nejnižší cenu se klade důraz na střih, kvalitní zipy a detaily, které se projeví při dlouhém dni na svahu.</p>'
          '<p>V nabídce převažují bundy pro dospělé a juniory. Pánské střihy jsou o něco delší a širší v ramenou, dámské užší v pase a bocích, juniorské ponechávají rezervu na růst. Dětské bundy se vyplatí kupovat s prodlužovacími manžetami, které se dají rozepnout a nahradí tak další velikost. Podle toho, co od bundy očekáváte, se hodí rozdělit nabídku do tří skupin.</p>'
          + T(['Typ bundy', 'Pro koho', 'Hlavní předpoklad'], [
              ['Zateplená lyžařská bunda', 'rekreační lyžaři, rodiny, dlouhé dny u vleku', 'jedna vrstva navíc nepotřebujete, teplo drží i při stání'],
              ['Skořepinová bunda bez zateplení', 'freeride, skialpinismus, jaro', 'vrstvíte podle teploty, vyšší prodyšnost'],
              ['Lehká dvojvrstvá bunda', 'jaro, aktivní jízda, plusové teploty', 'nízká hmotnost, málo izolace'],
              ['Juniorská bunda', 'děti na lyžích a snowboardu', 'rezerva na růst, výrazné barvy, odolné materiály']]) +
          '<h2>Zateplená, nebo skořepinová bunda</h2>'
          '<p>Rozhodnutí závisí na vašem stylu. Zateplená bunda se obléká jednoduše, stačí pod ni jedno funkční tričko a lehká mikina. Po vlekové linii a v horské restauraci je to nejpohodlnější řešení. Nevýhodou je, že při náročném výstupu nebo na jaře se přehřejete a zateplení nelze sundat. Skořepinová bunda, často označovaná jako hardshell nebo softshell, dává jen ochranu proti větru a vodě. Teplo si řešíte vrstvami pod ní, takže jedna bunda zvládne nejen mráz, ale i jarní slunce.</p>'
          '<p>Pro dětské lyžování je zateplená varianta prakticky bez výjimky lepší, protože děti se zastavují, chodí do sněhu a často se dotýkají mokrého povrchu. Pro dospělé, kteří jezdí rychle a v kopcích, může být lepší skořepina s vlastním středním oblečením. Obě varianty mívají větrací zipy pod pažemi, které odvádějí nahromaděné teplo, a stačí je v případě potřeby pootevřít.</p>'
          '<h2>Co sledovat u konkrétního modelu</h2>'
          '<p>Základní parametry bundy se u značky hodnotí podle toho, co vám může při jízdě nejvíc vadit. Nepromokavost se udává ve vodním sloupci, prodyšnost v množství vodní páry, kterou materiál propustí. Vyšší hodnoty znamenají lepší výkon, ale taky obvykle vyšší hmotnost a tuhost. Pro běžnou rekreační jízdu na upravených sjezdovkách nepotřebujete extrémní hodnoty. Pro dlouhé dny ve vlhku a pro freeride se vyplatí vyšší.</p>'
          '<ul><li><strong>Sněhová sukně:</strong> uvnitř bundy zabrání vniknutí sněhu při pádu, ideálně se zapíná na kalhoty.</li>'
          '<li><strong>Kapuce přes helmu:</strong> musí být nastavitelná a nesmí omezovat výhled do stran.</li>'
          '<li><strong>Kapsy:</strong> alespoň jedna na skipas na rukávu a jedna vnitřní na telefon, aby baterie vydržela v teple.</li>'
          '<li><strong>Zipy a chlopně:</strong> větrací zipy zakryté chlopní, zip hlavního zapínání s uchopitelnými jezdci do rukavic.</li>'
          '<li><strong>Manžety:</strong> pružné nebo suchým zipem, které těsní nad rukavicí.</li>'
          '<li><strong>Délka:</strong> záda kratší než kolena, aby nezavazela při sedu na sedačce a v kolejích.</li></ul>'
          '<h2>Velikost a vrstvení pod bundou</h2>'
          '<p>Jednotná tabulka pro všechny značky neexistuje, proto vždy použijte tabulku výrobce. Obecně platí, že bunda by měla být oblečená přes funkční spodní vrstvu a středovou mikinu nebo fleece, bez napínání v ramenou a v rukávech. Při předklonu a natažení paží nesmí rukávy vyjíždět nad zápěstí. Příliš velká bunda se vlní a propouští vzduch, příliš těsná omezuje pohyb a zhoršuje izolaci, protože komprimovaná izolace hřeje hůř.</p>'
          + T(['Vrstva', 'Úloha', 'Vhodný materiál'], [
              ['Spodní', 'odvádí pot od kůže', 'merino nebo syntetika, ne bavlna'],
              ['Střední', 'drží teplo', 'fleece, lehká izolační bunda'],
              ['Vnější', 'chrání před větrem a mokrem', 'lyžařská bunda s membránou']]) +
          '<p>Při výběru na dálku si zkontrolujte, jak značka označuje velikosti dětí: podle výšky (například 140, 152), nebo podle věku. U dívek a chlapců se střih mírně liší v pase a délce rukávů, ale hlavní je růst. Dítě by mělo mít v ramenou volnost, aby pod bundu uneslo svetr, ale nemělo bundu až na kolena.</p>'
          '<h2>Helly Hansen ve srovnání s jinými značkami</h2>'
          '<p>Na stránkách najdete i jiné značky lyžařských bund. Pro srovnání se podívejte na výběry <a href="/kilpi-lyzarska-bunda/">Kilpi</a>, <a href="/hannah-lyzarska-bunda/">Hannah</a>, <a href="/alpine-pro-lyzarska-bunda/">Alpine Pro</a> nebo <a href="/lyzarska-bunda-columbia/">Columbia</a>. České a slovenské značky jako Kilpi, Hannah a Alpine Pro nabízejí širokou škálu pro rekreační jízdu a děti. Columbia je americká značka s důrazem na izolaci Omni-Heat. Helly Hansen sází na norskou tradici v ochraně před vlhkem a na střihy pro aktivní pohyb.</p>'
          '<p>Rozdíly se projeví hlavně v detailech: kvalita zipů, tvar kapuce, množství větracích otvorů a barevné provedení. Pokud se rozhodujete mezi několika značkami, ověřte u každé nepromokavost, hmotnost a velikostní tabulku, ne jen název.</p>'
          '<h2>Barva a viditelnost na svahu</h2>'
          '<p>Barva bundy není jen otázka vzhledu. Výrazná barva vás na svahu lépe odliší, což oceníte při sjezdu s dětmi a při rychlé jízdě v zástupu. Bílé a světlé bundy v mlze splývají se sněhem, proto je lepší doplnit je barevnou helmou. Tmavé bundy lépe vypadají ve městě, v horské restauraci a hřejí na slunci, ale na jaře se přehřívají. Dětské bundy volte vždy výrazné, ať vás nepřehlédnou rodiče ani lyžařští instruktoři.</p>'
          '<h2>Údržba a skladování</h2>'
          '<p>Bundu s membránou perte jemným pracím prostředkem určeným pro funkční oblečení, bez aviváže a bez bělidla. Aviváž zalepí póry a snižuje prodyšnost. Po vyprání bunda často znovu získá vodoodpudivost po krátkém ošetření teplým vzduchem nebo po impregnaci sprejem. Před uložením přes léto bundu vyperte, vysušte a pověste na ramínko, ne do pytle, aby izolace neztratila objem. Zip a kapsy občas zkontrolujte, drobné opravy dělá krejčí i servis značky.</p>'
          '<p>K bundě patří i další vybavení: <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-helmy/">helma</a> a <a href="/lyzarske-bryle/">brýle</a>. Pokud sledujete celou značku, podívejte se na stránku <a href="/znacka/helly-hansen/">Helly Hansen</a>.</p>',
    faq=[
        ('Pro koho jsou lyžařské bundy Helly Hansen vhodné?', 'Pro rekreační lyžaře, snowboardisty i náročnější jezdce, kteří chtějí bundu do mokra a mrazu. Značka nabízí střihy pro muže, ženy i děti a řadu určenou pro freeride i klasické sjezdovky.'),
        ('Mám zvolit zateplenou, nebo skořepinovou bundu?', 'Zateplená se hodí na dlouhé dny, k dětem a do zimy. Skořepina je univerzálnější na jaro a aktivní jízdu, ale vyžaduje vrstvení pod ní. Při nejistotě volte zateplenou.'),
        ('Jak poznám správnou velikost?', 'Podle tabulky značky, nikoli podle jiných výrobců. Bunda má pohodlně sedět přes dvě vrstvy, rukávy nesmí při předklonu vyjíždět a záda se nesmějí zvedat nad pas.'),
        ('Jak vybrat bundu pro dítě?', 'Podle výšky dítěte, s rezervou na růst a s nastavitelnými manžetami. Zateplená bunda s kapucí přes helmu a výraznou barvou je pro děti nejlepší volba.'),
        ('Liší se pánské a dámské střihy?', 'Ano. Pánské jsou širší v ramenou a delší, dámské užší v pase a bocích. Pokud vám dámský střih sedí lépe, můžete jej zvolit bez ohledu na označení.'),
        ('Je bunda vhodná i na každodenní nošení?', 'Ano. Zateplená lyžařská bunda hřeje i ve městě. Při nošení v teple se ale snadno přehřejete, proto vybírejte model s možností odvětrání zipy.'),
        ('Jak bundu prát?', 'Šetrně, podle štítku, s tekutým prostředkem na funkční textilie a bez aviváže. Po vyprání ji dobře vysušte, aby si zachovala vodoodpudivou úpravu.'),
        ('Čím se liší od jiných značek v nabídce?', 'Hlavně norským původem, důrazem na ochranu před vlhkem a střihem pro aktivní pohyb. České značky jako Kilpi nebo Hannah často nabízejí širší výběr barev a modelů pro rekreaci.'),
        ('Mohu bundu použít na snowboard?', 'Ano, lyžařské a snowboardové bundy jsou si konstrukčně velmi podobné. Snowboardisté obvykle preferují volnější střih a delší zadní část, která chrání při sezení ve sněhu.'),
        ('Co dělat, když bunda přestane odpuzovat vodu?', 'Vyperte ji a obnovte vodoodpudivou úpravu teplým vzduchem nebo impregnačním sprejem. Pokud problém trvá, může být poškozená membrána, což se řeší servisem.'),
    ],
)

# ------------------------------------------------------------------ panska-sportovni-obuv
NEW['panska-sportovni-obuv'] = dict(
    title='Pánská sportovní obuv: střih, šířka a výběr podle sportu',
    desc='Pánská sportovní obuv: jak vybrat velikost, šířku a podrážku pro běh, fitness, tenisky i kopačky. Porovnejte značky a obchody a ověřte skladové velikosti.',
    intro='<p>Pánské boty se od dámských liší hlavně kopytem: bývají širší v přední části, mají objemnější patu a vyšší vazbu. Pro muže s větším chodidlem to znamená víc místa pro prsty, pro ty se štíhlou nohou naopak riziko, že bota příliš plave. Na této stránce jsou boty z kategorie <a href="/sportovni-obuv/">sportovní obuv</a> určené mužům, od běžeckých a tréninkových přes tenisky až po kopačky a sálovou obuv. '
          'Průvodce vysvětluje, jak vybrat velikost a šířku, jak poznat správnou podrážku pro svůj sport, jak se liší střih u hlavních značek a jak poznat dobře seděnou botu bez zkoušení. Najdete tu i základní postupy péče a skladování, aby boty vydržely déle. U každého páru vidíte nabídky více obchodů a rozhodnout se můžete podle skladových velikostí.</p>',
    guide='<h2>V čem se pánská sportovní obuv liší</h2>'
          '<p>Rozdíly mezi pánskou a dámskou obuví nejsou jen v barvách. Dámská kopyta bývají užší v patě i přes nárt a mají často nižší výšku jazyku. Pánská obuv obvykle začíná od středních velikostí a pokračuje do vysokých čísel, kde se u některých modelů mění i proporce podrážky, aby noha stála stabilně. Pokud má muž štíhlé chodidlo, může se mu lépe hodit unisex nebo dámský střih, a naopak. Označení pohlaví je vodítko, nikoli pravidlo.</p>'
          + T(['Prvek', 'Pánská obuv', 'Co z toho plyne'], [
              ['Šířka přední části', 'širší prostor pro prsty', 'u úzké nohy volte pevné šněrování nebo užší značku'],
              ['Pata', 'objemnější, vyšší opora', 'dobře drží pevnější nohu, štíhlá pata může klouzat'],
              ['Podrážka', 'robustnější, větší plocha', 'lepší stabilita při větší hmotnosti'],
              ['Rozsah velikostí', 'od středních po velké', 'u nejvyšších čísel je nabídka užší, počítejte s předstihem'],
              ['Barvy', 'více tlumených a tmavých', 'tmavá obuv méně ukáže špínu při denním nošení']]) +
          '<h2>Jak změřit nohu a vybrat velikost</h2>'
          '<p>Nohu měřte odpoledne nebo večer, kdy je mírně oteklá, na papíře opřený o stěnu. Označte nejdelší bod, změřte vzdálenost od paty a připočtěte rezervu pro prsty. U sportovní obuvi se doporučuje mít před špičkou asi šířku palce. Při běhu a sjezdu z kopce se noha v botě posouvá dopředu, takže těsná bota způsobuje černé nehty. Zkoušejte vždy s ponožkou, ve které budete sportovat, a oběma botami, protože jedna noha bývá větší.</p>'
          '<p>Velikostní systémy se liší. Evropská čísla se v Česku používají nejčastěji, ale americké a britské tabulky u značek jako Nike a Asics se od nich mohou o půl až celou číslici lišit. Pokud kupujete na dálku, vždy použijte délku vložky v centimetrech, kterou výrobce uvádí. Je to nejspolehlivější způsob, jak předejít vrácení.</p>'
          '<h2>Podrážka a typ povrchu</h2>'
          '<p>Nejdůležitější rozdíl mezi sportovními botami leží ve spodní části. Podrážka pro asfalt musí tlumit nárazy, ta pro trávu a kolíky zajišťovat záběr, ta pro halu držet na parketu bez zanechávání stop. Sálová obuv má světlou, často krepovou podrážku, kopačky kolíky nebo drobné výstupky. Pokud ji použijete na špatném povrchu, rychle se opotřebuje a hrozí zranění.</p>'
          + T(['Sport', 'Typ obuvi', 'Na co se zaměřit'], [
              ['Běh po silnici', '<a href="/bezecka-obuv/">běžecká obuv</a>', 'tlumení, odvalení chodidla, prodyšnost'],
              ['Fitness a posilovna', '<a href="/treninkova-obuv/">tréninková obuv</a>', 'plochá stabilní podrážka, boční opora'],
              ['Fotbal', '<a href="/kopacky/">kopačky</a>', 'typ kolíků podle povrchu, těsné uložení'],
              ['Hala, florbal, volejbal', '<a href="/salova-obuv/">sálová obuv</a>', 'světlá protiskluzová podrážka, flexibilita'],
              ['Turistika', '<a href="/trekova-obuv/">trekové boty</a>', 'hrubý profil, výztuž špičky, vodotěsnost'],
              ['Každodenní nošení', '<a href="/tenisky/">tenisky</a>', 'pohodlná stélka, styl, lehká váha'],
              ['Tenis', '<a href="/tenisova-obuv/">tenisová obuv</a>', 'zpevněné boky, odolná špička']]) +
          '<h2>Značky a rozdíly ve střihu</h2>'
          '<p>Každý výrobce používá vlastní kopyto, a proto stejné číslo nemusí sedět stejně. Častý popis: Asics a New Balance dávají víc místa v přední části, Nike bývá užší, Adidas středně široký a Puma spíše štíhlejší. Skechers klade důraz na měkký a pohodlný podešev pro dlouhou chůzi. Na tomto principu stojí i další značky v nabídce: ' + B(('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('new-balance', 'New Balance'), ('asics', 'Asics'), ('hoka', 'Hoka'), ('skechers', 'Skechers'), ('saucony', 'Saucony'), ('joma', 'Joma'), ('converse', 'Converse')) + '. Jde o obecné tendence, výjimky existují u každého modelu.</p>'
          '<p>Pokud máte nohu širokou, hledejte u modelů označení „wide“ nebo „extra wide“ a zkuste značky s přirozeným tvarem špičky. Pokud je naopak štíhlá, použijte šněrování s dodatečným očkem a pevnější jazyk, který chodidlo přidrží.</p>'
          '<h2>Stélka, tlumení a opora klenby</h2>'
          '<p>Stélka rozhoduje o pohodlí při dlouhém nošení. Pěnové stélky tlumí rychle, ale časem se stlačí. Gelové a dvouvrstvé drží tvar déle. Pokud trpíte plochou nohou nebo vyšší klenbou, zvažte vložky na míru, které se do většiny sportovních bot vejdou po vyjmutí původní stélky. Tlumení nezvyšujte nad potřebu: příliš měkká podrážka snižuje stabilitu a při bočním pohybu hrozí podvrtnutí.</p>'
          '<ul><li><strong>Jazyk:</strong> měkký a polstrovaný chrání nárt proti tlaku tkaniček.</li>'
          '<li><strong>Pata:</strong> pevný kontrafort drží patu, aby neklouzala.</li>'
          '<li><strong>Svršek:</strong> síťovina je prodyšná, kůže a syntetika lépe odolávají vodě.</li>'
          '<li><strong>Šněrování:</strong> klasické se dá doladit, rychlé zapínání je pohodlné, ale nenahradí pevné uložení.</li></ul>'
          '<h2>Boty na každodenní nošení a na sport</h2>'
          '<p>Sportovní obuv se často nosí i ve městě, ale není stejné, co dobře vypadá v kavárně a co bude fungovat na hřišti. Lifestylové modely mají jemnější tlumení a jsou stavěné pro chůzi, ne pro dynamické změny směru. Pokud chcete jedny boty na všechno, volte univerzální tréninkový model s pevnou podrážkou. Pro pravidelný běh je lepší samostatný pár, protože běžecká obuv ztrácí tlumení dřív, než se jeví opotřebovaná.</p>'
          '<p>Zimní provoz vyžaduje jiné materiály: vodoodpudivý svršek, hrubší profil a teplejší podšívku. Zimní boty najdete v kategorii <a href="/zimni-obuv/">zimní obuv</a>, na léto a pobyt u vody pak <a href="/sandaly/">sandály</a> a <a href="/pantofle-a-zabky/">pantofle a žabky</a>. Pro přirozené našlapování je tu <a href="/barefoot-obuv/">barefoot obuv</a>, pro basketbal <a href="/basketbalova-obuv/">basketbalová obuv</a>. Pro dámy je určená stránka <a href="/damska-sportovni-obuv/">dámská sportovní obuv</a>.</p>'
          '<h2>Péče o obuv a životnost</h2>'
          '<p>Boty po sportu vyndejte z tašky a nechte vyschnout při pokojové teplotě, ne u radiátoru, který lepidlo a pěnu poškozuje. Do mokrých bot dejte nemačkaný papír, který nasaje vlhkost. Stélky občas vyjměte a vyvětrejte. Špinavé boty čistěte kartáčem a vlažnou vodou, bez agresivních prostředků, a v pračce je perte jen tehdy, pokud to povoluje výrobce. Střídáním dvou párů prodloužíte životnost obou, protože pěna v podrážce potřebuje čas na regeneraci. Příslušenství jako tkaničky, vložky a impregnace najdete v kategorii <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>',
    faq=[
        ('Jak poznám správnou velikost sportovní obuvi?', 'Změřte nohu odpoledne a podle délky vložky v centimetrech vyberte velikost s rezervou přibližně šířky palce před špičkou. Zkoušejte s ponožkou, ve které sportujete.'),
        ('Je pánská sportovní obuv vždy širší než dámská?', 'Obvykle ano, ale ne vždy. Záleží na výrobci a modelu. Štíhlá mužská noha může pohodlněji sedět v unisex nebo dámském střihu.'),
        ('Mohu běhat v teniskách na každý den?', 'Krátce ano, ale lifestylové tenisky nemají tlumení a oporu nutnou pro pravidelný běh. Pro běhání zvolte specializovanou obuv.'),
        ('Jak často měnit sportovní boty?', 'Záleží na zátěži. Běžecká obuv ztrácí tlumení po stovkách kilometrů, i když vypadá dobře. Při bolesti kloubů nebo viditelně sešlapané podrážce je čas na nový pár.'),
        ('Čím se liší tréninková obuv od běžecké?', 'Tréninková má plochou stabilní podrážku a boční oporu pro posilování. Běžecká má měkčí tlumení a zvednutou patu pro odvalování při běhu.'),
        ('Které značky jsou širší?', 'Asics a New Balance se obecně považují za prostornější v přední části. Nike bývá užší. Jde však o tendenci, zkoušejte konkrétní model.'),
        ('Jak vybrat kopačky pro muže?', 'Podle povrchu: kolíky na trávu, umělou trávu nebo halové provedení. Kopačka má sedět těsně bez prostoru, ale nesmí tlačit na prsty.'),
        ('Jak sportovní obuv prát?', 'Nejlépe ručně vlažnou vodou a jemným mýdlem. Pračka a sušička zkracují životnost pěny a lepidla, takže ji použijte jen u modelů, kde to výrobce povoluje.'),
        ('Dá se obuv vracet, když nesedí?', 'Obvykle ano v zákonné lhůtě pro nákup na dálku, pokud nebyla nošená venku. Podmínky vždy najdete u konkrétního obchodu.'),
        ('Jak poznám, že boty příliš plavou?', 'Pata při chůzi vyskakuje, prsty tlačí do špičky a nárt se zdá volný. Pomůže pevnější šněrování, užší model nebo tenká vložka.'),
    ],
)

# ------------------------------------------------------------------ real-madrid-dresy
NEW['real-madrid-dresy'] = dict(
    title='Real Madrid dresy: domácí, venkovní, dětské a tréninkové',
    desc='Real Madrid dresy pro dospělé i děti: domácí bílý, venkovní, tréninkové soupravy a jména hráčů. Jak vybrat velikost a střih a porovnat obchody.',
    intro='<p>Bílý dres Realu Madrid patří k nejznámějším fotbalovým dresům na světě, a proto se na něm hodně liší výrobky podle toho, jestli jsou určené do hlediště, na trénink nebo pro děti. V nabídce najdete domácí dresy, venkovní provedení, tréninkové soupravy i drobnější fanouškovské kousky. Stránka vychází z kategorie <a href="/dresy/">dresy</a> a ukazuje oblečení spojené s madridským klubem. '
          'Průvodce vysvětluje, jak se liší domácí a venkovní dresy, co obnáší tisk jména a čísla hráče, jak vybrat velikost pro dítě a dospělého a jak dres správně prát, aby dlouho vydržel. Řeší také rozdíl mezi fanouškovskou replikou a hráčskou verzí a jak se v nabídce vyznat, když se sezóny střídají. Nabídky více obchodů vidíte vedle sebe, takže poznáte, kde je váš střih ještě skladem.</p>',
    guide='<h2>Domácí, venkovní a další dresy Realu</h2>'
          '<p>Klub nastupuje na domácích zápasech v bílém, což je jeho historická barva a důvod přezdívky „Los Blancos“. Venkovní dres se každou sezónu mění a bývá tmavý nebo výrazně barevný. K nabídce se obvykle přidává třetí dres, který se hraje v méně obvyklých zápasech. Každá sezóna má nové provedení, takže starší kusy se stávají sběratelskými. Při nákupu proto vždy zkontrolujte, pro kterou sezónu je dres určený.</p>'
          + T(['Typ', 'Kdy se hodí', 'Poznámka'], [
              ['Domácí dres', 'zápasy, hlediště, každodenní nošení fanouška', 'nejznámější bílé provedení, nejširší nabídka velikostí'],
              ['Venkovní dres', 'fanoušci, kteří chtějí odlišnou barvu', 'mění se každou sezónu, starší bývají vzácnější'],
              ['Třetí dres', 'sběratelé a ti, kdo chtějí originální kus', 'menší nabídka velikostí'],
              ['Tréninková souprava', 'sport, volný čas, běžné nošení', 'volnější střih, praktické materiály'],
              ['Dětský dres a souprava', 'děti a mladí fanoušci', 'odolný a pratelný materiál, rezerva na růst']]) +
          '<h2>Fanouškovská replika, nebo hráčská verze</h2>'
          '<p>Výrobci vyrábějí dresy ve dvou provedeních. Replika je určená fanouškům: střih je uvolněnější, materiál odolný proti praní a znak je obvykle vyšitý nebo našitý. Hráčská verze má přiléhavější střih, lehčí materiál pro rychlý pohyb a znak je často tepelně nalepen kvůli nízké hmotnosti. Je dražší, ale není vhodná pro každodenní nošení, protože se rychleji poškodí.</p>'
          '<p>Pro většinu fanoušků je replika lepší volba. Bez problémů vydrží praní, zápas na hřišti i dlouhý den ve městě. Hráčská verze se hodí těm, kdo chtějí přesně stejný střih jako hráči, a sběratelům. Pokud nevíte, kterou variantu máte, najdete označení v popisu produktu a podle střihu.</p>'
          '<h2>Jména a čísla hráčů</h2>'
          '<p>Častou položkou nabídky jsou dresy se jménem a číslem konkrétního hráče. Při výběru dbejte na to, zda je potisk součástí výrobku, nebo je třeba jej objednat zvlášť. Hráči se mění: někteří odcházejí, jiní přicházejí a čísla se přesouvají. V nabídce se objevují dětské dresy se jmény Kylian Mbappé a Jude Bellingham, takže je dobré vybrat dres, který vydrží i po sezóně. Pokud kupujete dítěti, hrají roli oblíbenost hráče a jeho dlouhodobé působení v klubu. Jméno bez čísla nebo čistý dres s klubovým znakem je bezpečnější volba, když fanoušek ještě nemá jasného favorita.</p>'
          '<ul><li><strong>Oficiální potisk</strong> bývá z jednotného materiálu a odpovídá písmu používanému v lize.</li>'
          '<li><strong>Neoficiální potisk</strong> může mít jiné písmo a rychleji se loupe, ale bývá levnější.</li>'
          '<li><strong>Potisk na zádech</strong> neovlivňuje velikost, ale vyhněte se žehlení a praní na vysoké teplotě.</li></ul>'
          '<h2>Velikost dresu pro dospělé a děti</h2>'
          '<p>Dospělé velikosti od S do XXL se řídí šířkou hrudníku. Replika obvykle sedí volněji, takže při váhání berte menší velikost, pokud nechcete volný střih. Hráčská verze je přiléhavá, proto zvolte raději o číslo větší. Dres by měl končit zhruba v půli stehen a rukávy ve středu paže. Pro orientaci změřte hrudník a porovnejte jej s tabulkou konkrétního výrobce.</p>'
          + T(['Výška dítěte', 'Orientační označení', 'Poznámka'], [
              ['110–116 cm', 'zhruba 5–6 let', 'rezerva v délce, aby vydržel další sezónu'],
              ['122–128 cm', 'zhruba 7–8 let', 'rukávy se dají podehnout'],
              ['134–140 cm', 'zhruba 9–10 let', 'střih se blíží dospělé velikosti XS'],
              ['146–152 cm', 'zhruba 11–12 let', 'dobré ověřit tabulku, přechod k dospělé velikosti'],
              ['158–164 cm', 'zhruba 13–14 let', 'často stejná jako dospělá XS nebo S']]) +
          '<p>Děti rostou rychle, proto se vyplatí zvolit velikost s malou rezervou. Příliš velký dres ale nesluší a překáží při hře. Dětské soupravy obvykle obsahují dres a šortky, někdy i ponožky. Chcete-li dres využít při sportu, ověřte, že materiál prodýchá.</p>'
          '<h2>Materiál a praní</h2>'
          '<p>Většina moderních dresů je z polyesteru, který rychle schne a odvádí pot. Bavlněné fanouškovské trička jsou příjemnější na dotek, ale po vyprání se mohou srazit a potisk se rychleji opotřebí. Dres perte naruby při nízké teplotě, bez aviváže, která zalepí póry materiálu. Nežehlete přímo přes potisk a nesušte v sušičce, teplo deformuje znak i číslo. Sušení na vzduchu zachová tvar, barvu i potisk. Bílý dres perte zvlášť s bílým prádlem, aby neztratil jas.</p>'
          '<h2>Sběratelské hledisko a rozpoznání pravosti</h2>'
          '<p>U dresů slavných klubů se objevují padělky. Poznáte je podle nepřesného znaku, rozdílných písem, nekvalitního šití nebo chybějících štítků výrobce. Originální dres má výrobní štítek s kódem produktu, jednotné šití a znak vyvedený přesně podle klubového vzoru. Při nákupu u ověřených obchodů je riziko minimální. Sběratelé uchovávají dresy v ochranném obalu mimo slunce, které bílou barvu žloutne.</p>'
          '<h2>Co dál ke dresu</h2>'
          '<p>K dresu se hodí další oblečení klubu a obecná výbava pro fotbalisty. Pro hru na hřišti využijete <a href="/kopacky/">kopačky</a> a další vybavení z kategorie <a href="/fotbal/">fotbal</a>. Chcete-li srovnat s jiným výrobcem, podívejte se na stránku <a href="/nike-dresy/">Nike dresy</a>. Pro mladé fanoušky je tu stránka <a href="/detske-dresy/">dětské dresy</a>. Pro volný čas přijdou vhod <a href="/teplaky/">tepláky</a> a <a href="/sportovni-tricka/">sportovní trička</a>. Všechny položky klubu najdete na stránce <a href="/znacka/real-madrid/">Real Madrid</a>.</p>'
          '<h2>Jak číst nabídku obchodů</h2>'
          '<p>Při porovnání obchodů sledujte, zda je dres z aktuální sezóny, zda jde o originální produkt a jaké velikosti jsou skladem. U populárních modelů se velikosti rychle vyprodají a nové zásoby často nepřijdou do začátku další sezóny. Zkontrolujte také, zda cena zahrnuje potisk, nebo se platí zvlášť, a jak dlouho trvá doručení. Pokud chcete dres k danému zápasu, objednávejte s rezervou.</p>',
    faq=[
        ('Jaký je rozdíl mezi domácím a venkovním dresem Realu Madrid?', 'Domácí dres je bílý a hraje se na domácích zápasech. Venkovní se každou sezónu mění a bývá tmavý nebo výrazně barevný.'),
        ('Je lepší fanouškovská replika, nebo hráčská verze?', 'Pro běžné nošení a praní je lepší replika. Hráčská verze sedí přiléhavěji a je lehčí, ale hůř snáší časté praní.'),
        ('Jak vybrat velikost dětského dresu?', 'Podle výšky dítěte a tabulky výrobce, s malou rezervou na růst. Příliš velký dres překáží, příliš malý vydrží jen krátce.'),
        ('Je potisk jména součástí dresu?', 'Záleží na produktu. U některých je potisk již nanesen, jinde se objednává zvlášť. Informace najdete v popisu konkrétního kusu.'),
        ('Jak dres prát?', 'Naruby při nízké teplotě, bez aviváže a bez sušičky. Potisk nežehlete a sušte na vzduchu.'),
        ('Jak poznám originální dres?', 'Podle výrobního štítku, přesného znaku, kvalitního šití a ověřeného prodejce. Nepřesná písma a hrubé nitě jsou známkou padělku.'),
        ('Hodí se dres na sport?', 'Polyesterové dresy a tréninkové soupravy ano, odvádějí pot. Hráčská verze je lehčí, replika odolnější.'),
        ('Mění se dresy každý rok?', 'Ano, nová kolekce přichází zpravidla každou sezónu. Starší dresy se stávají sběratelskými a bývají skladem omezeně.'),
        ('Co obsahuje dětská tréninková souprava?', 'Obvykle tričko nebo dres a šortky nebo tepláky, někdy i ponožky. Přesný obsah je uveden v popisu výrobku.'),
        ('Kde najdu další oblečení klubu?', 'V kategorii dresy a také v tepláku, trikách a doplňcích. Stránka značky Real Madrid shrnuje všechny položky.'),
    ],
)


# ---- additions (length)
NEW['helly-hansen-lyzarska-bunda']['guide'] += (
    '<h2>Bunda pro snowboard, freeride a skialpinismus</h2>'
    '<p>Snowboardisté obvykle vyhledávají volnější střih, delší záda a vyztužené kapsy, které se nezachytí při sezení ve sněhu. Freeridoví jezdci hledají skořepinu s vysokým zipem, velkou kapucí přes helmu a prostornou kapsou na lavinové vybavení či mapu. Skialpinisté se zaměřují na nízkou hmotnost a prodyšnost, protože při výstupu se tělo zahřívá a bunda musí vodní páru odvádět. Pokud se věnujete rekreačnímu lyžování, tyto speciální vlastnosti nepotřebujete a vystačíte si s klasickou zateplenou bundou.</p>'
    '<h2>Jak bundu kombinovat s kalhotami a doplňky</h2>'
    '<p>Bunda a kalhoty by měly mít podobnou úroveň ochrany, jinak slabší kus omezí celek. Sněhová sukně se zapíná na pasu kalhot, takže ověřte, že se obě součásti k sobě hodí délkou a velikostí. Barevně lze kombinovat jednobarevnou bundu s kontrastními kalhotami, nebo naopak, aby se nevytratila viditelnost na svahu. Rukavice se zasouvají pod manžety bundy, brýle se opírají o kapuci, proto zkoušejte celou výbavu pohromadě.</p>'
    '<h2>Kdy nakupovat a na co si dát pozor</h2>'
    '<p>Nová kolekce přichází koncem léta, ale výběr velikostí je nejširší na začátku sezóny. Na konci zimy zůstávají často nejvýraznější barvy a některé velikosti. Pokud nespěcháte, sledujte více obchodů a porovnejte, který nabízí vaši velikost. U starších kolekcí se střih může lišit od aktuální tabulky, proto při nákupu na dálku vždy ověřte rozměry. Zkontrolujte také, zda bunda patří do lyžařské řady, nebo jde o městský model bez sněhové sukně a se slabší nepromokavostí.</p>'
)
NEW['panska-sportovni-obuv']['guide'] += (
    '<h2>Jak v obchodě poznat dobře sedící botu</h2>'
    '<p>Při zkoušení se postavte, projděte se a zkuste několik kroků po schodech nebo po zvýšené hraně. Pata nesmí vyskakovat, prsty se musí dát pohnout a nárt nesmí tlačit pod šněrováním. Zkontrolujte i boky: pokud noha přesahuje přes okraj podrážky, bota bude při zatáčení nestabilní. Test jednoduše zopakujte na druhé noze, protože rozdíly mezi levou a pravou bývají větší, než čekáte. U nákupu na dálku si změřte vnitřní délku vložky a porovnejte ji s údajem výrobce, abyste se vyhnuli zbytečné výměně.</p>'
    '<h2>Pánská obuv podle sezóny</h2>'
    '<p>V létě vítáte prodyšnou síťovinu a lehkou podrážku, v zimě naopak potřebujete vodoodpudivý svršek a hrubší profil, který neklouže na ledu. Přechodné období je ideální pro tenisky s měkkou membránou, které odolají kapkám a louži. Při dojíždění na kole se vyplatí tvrdší podrážka, která dobře přenáší sílu do pedálu. Pro cestování zvolte lehký pár, který zabere málo místa v zavazadle a rychle schne. Pokud sportujete několikrát týdně, rozdělte obuv mezi trénink a běžné nošení, každý pár pak vydrží výrazně déle.</p>'
    '<h2>Časté chyby u mužů</h2>'
    '<ul><li><strong>Příliš malá velikost</strong> z obavy, že větší bota bude plavat, vede k tlaku na prsty.</li>'
    '<li><strong>Jedna bota na všechno:</strong> univerzální pár dělá kompromis v každé disciplíně.</li>'
    '<li><strong>Přehlížení šířky:</strong> stejné číslo se u dvou značek liší o centimetr v obvodu.</li>'
    '<li><strong>Čekání na úplné rozpadnutí:</strong> tlumení mizí dřív, než se podrážka viditelně sešlape.</li></ul>'
)
NEW['real-madrid-dresy']['guide'] += (
    '<h2>Klub, stadion a bílá barva</h2>'
    '<p>Real Madrid vznikl na počátku dvacátého století a svůj domov má na stadionu Santiago Bernabéu v Madridu. Bílá barva patří k identitě klubu od počátku, jména hráčů a sponzorů se na dresu střídají, ale základní vzhled zůstává. Každý nový dres tak navazuje na tradici a zároveň přidává drobný designový prvek, například límec, pruh nebo detail na rukávu. Právě ty rozhodují, který kus fanoušci považují za povedený.</p>'
    '<h2>Jak dres nosit i mimo stadion</h2>'
    '<p>Fotbalový dres se dá nosit ve městě stejně jako sportovní tričko. Bílý domácí dres se hodí k džínám a teniskám, tmavý venkovní k černým kalhotám. Přes dres lze obléct <a href="/mikiny/">mikinu</a>, v chladnějších měsících pomůže bunda ze <a href="/sportovni-obleceni/">sportovního oblečení</a>. Při zápase v hospodě nebo na tribuně vás zahřeje dlouhý rukáv pod dresem. Tréninková souprava je volnější a hodí se i na lehké cvičení nebo na procházky.</p>'
    '<h2>Dres jako dárek</h2>'
    '<p>Při nákupu pro někoho jiného ověřte, kterého hráče a kterou sezónu dotyčný preferuje. Jméno oblíbeného hráče potěší, ale pokud si nejste jistí, zvolte čistý dres bez potisku. Velikost raději trochu větší než menší, protože dres se dá ladit nošením a praním. U dětí kupujte s rezervou, ale ne s příliš velkou. Při zamýšleném dárku zkontrolujte lhůtu vrácení a výměny, aby se případně dalo velikost změnit.</p>'
    '<h2>Dětské dresy a tréninkové soupravy</h2>'
    '<p>Pro děti jsou nejpraktičtější soupravy z lehkého polyesteru, které se snadno perou a rychle schnou. Stačí je vložit do pračky, rozložit a druhý den jsou suché. Dětem se líbí jména oblíbených hráčů, rodiče by však měli pamatovat, že potisk po několika desítkách praní bledne. V <a href="/detske-dresy/">dětských dresech</a> najdete i další kluby a sporty. Pro hru na hřišti doplňte dres o <a href="/fotbal/">fotbalovou výbavu</a>, chrániče a vhodné boty.</p>'
)

NEW['panska-sportovni-obuv']['guide'] += (
    '<h2>Jak si vybrat podle hmotnosti a stylu pohybu</h2>'
    '<p>Těžší běžec nebo člověk, který stráví na nohou celý den, potřebuje pevnější mezipodešev a širší stopu podrážky, protože měkká pěna se pod větší zátěží rychle stlačí. Lehčí jezdec či běžec naopak ocení pružnější podrážku a nižší hmotnost boty. Pokud našlapujete na vnější hranu chodidla, hledejte neutrální model s dobrým tlumením. Při našlapování dovnitř pomáhá model s pevnější vnitřní stranou. Neznáte-li svůj styl, nechte si krátce zhodnotit běh na videu v odborném obchodě a podle něj upravte výběr.</p>'
)
NEW['real-madrid-dresy']['guide'] += (
    '<h2>Dres v zápase a při sběratelské péči</h2>'
    '<p>Kdo chce dres nosit při hře, vybere lehký polyester a střih, který nebrání pohybu paží. Fanoušci do hlediště upřednostní volnější repliku, ve které se dá sedět dvě hodiny bez tlaku. Sběratelé ukládají dresy rozložené v krabici s hedvábným papírem, aby se nezlámaly a nezežloutly. Potisk se nepřikládá k jinému potisku, protože by se mohl slepit. Starší dres zbavíte zápachu větráním, ne agresivním pracím prostředkem.</p>'
)
