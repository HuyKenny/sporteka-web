"""sporteka.cz — wave 17b (4. 11. 2026): long texts (>= 1650 words) for lyzarske-bryle, stany, cyklo-brzdy, lov-a-priroda.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lyzarske-bryle
NEW['lyzarske-bryle'] = dict(long=True,
    title='Lyžařské brýle: zorník, helma, mlžení, děti',
    desc='Lyžařské a snowboardové brýle: kategorie zorníku, fotochromatické čočky, OTG, kompatibilita s helmou a péče. Nabídky českých obchodů vedle sebe.',
    intro='<p>Na svahu se oči vystavují třem věcem zároveň: ostrému slunci odraženému od sněhu, ledovému větru a při pádu i střípkům ledu. Dobré <strong>lyžařské brýle</strong> všechny tři řeší a navíc vám ukážou terén dost kontrastně, '
          'abyste včas spatřili hrbol nebo ledovou plotnu. Zároveň je to kousek výbavy, který se nejčastěji kupuje špatně, protože se lidé dívají na barvu rámu a nezkoušejí je s helmou.</p>'
          '<p>V kategorii najdete brýle s jedním i dvojitým zorníkem, modely s fotochromatickou čočkou, brýle pro nositele dioptrií, dětské střihy a pod odkazem <a href="/nahradni-zorniky/">náhradní zorníky a příslušenství</a> také vyměnitelné čočky. '
          'Sporteka srovnává nabídky českých obchodů u stejného modelu, takže uvidíte, kde je zrovna skladem vámi vybraná barva zorníku. Ke kompletu patří i <a href="/lyzarske-helmy/">lyžařské helmy</a>.</p>',
    guide='<h2>Z čeho se lyžařské brýle skládají</h2>'
          '<p>Brýle mají tři části, které se mohou posuzovat zvlášť: rám, zorník a pěnová výplň s popruhem. Rám bývá z ohebného polyuretanu či podobného plastu, který zůstane poddajný i v mrazu a při pádu se deformuje místo toho, aby praskl. '
          'Zorník je prohnutý do tvaru válce nebo koule. Válcový tvar je tradiční a bývá cenově dostupnější, kulový zorník nabízí širší výhled a méně zkreslení po okrajích. '
          'Pěnová výplň při obličeji obvykle bývá vícevrstvá: pevnější vrstva drží tvar, měkká se přimyká ke kůži a zabraňuje průvanu. Popruh má na zadní straně silikonové proužky, aby neklouzal po helmě.</p>'
          '<h2>Kategorie zorníku podle světla</h2>'
          '<p>Zorníky se dělí do pěti stupňů podle množství propuštěného světla, od čirého po velmi tmavý. Platí jednoduchá úvaha: čím méně světla, tím světlejší čočka, a naopak. Údaj najdete na rámu nebo v popisu produktu.</p>'
          + T(['Kategorie', 'Propustnost světla', 'Kdy se hodí'], [
              ['0', 'téměř čirý', 'noční lyžování, hustá mlha'],
              ['1', 'světlý', 'zataženo, sněžení, soumrak'],
              ['2', 'střední', 'proměnlivé počasí, polojasno'],
              ['3', 'tmavý', 'slunečný den na běžné sjezdovce'],
              ['4', 'velmi tmavý', 'ledovec, vysoké hory, oslnivý jas']]) +
          '<p>Barva čočky ovlivňuje kontrast. Žluté, oranžové a růžové odstíny zvýrazňují nerovnosti ve slabém světle. Šedá a hnědá zachovávají přirozené barvy a hodí se na slunce. '
          'Zrcadlový povrch odráží část světla ještě před čočkou, takže ze stejného stupně tmavosti vyrobí příjemnější pohled za jasného dne.</p>'
          '<h2>Fotochromatické a výměnné zorníky</h2>'
          '<p>Kdo lyžuje při měnícím se počasí, má dvě možnosti. Fotochromatická čočka sama ztmavne na slunci a projasní se ve stínu, takže nemusíte nic měnit. Reaguje ale s mírným zpožděním a v chladu pomaleji, což je dobré vědět. '
          'Druhou cestou jsou výměnné zorníky, kde si do batohu přibalíte náhradní čočku jiné barvy. Výměna se dělá zacvaknutím, magnety nebo posuvem pojistky, podle výrobce. '
          'Samostatné čočky najdete v kategorii <a href="/nahradni-zorniky/">náhradní zorníky</a>, kde je důležité vybrat přesně pro stejný model rámu, protože čočky se mezi řadami nedají zaměnit.</p>'
          '<h2>Jednoduchý zorník, dvojitý zorník a mlžení</h2>'
          '<p>Mlžení vzniká, když se vlhký vzduch od obličeje srazí na studené čočce. Dvojitý zorník vytváří mezi dvěma vrstvami vzduchovou komoru, která funguje jako izolace, takže vnější vrstva zůstane studená a vnitřní teplá. '
          'Proto je dvojitý zorník v chladu odolnější. Antifogová vrstva uvnitř čočky pomáhá, ale otěrem se ztrácí, a proto se zorníku uvnitř nikdy nedotýkejte prsty ani rukavicí. '
          'Větrací otvory v rámu a nad nosem odvádějí vlhkost. Nezvedejte brýle na čelo, když se zahřejete: vlhkost z čela se okamžitě usadí uvnitř čočky.</p>'
          '<h2>Kompatibilita s helmou</h2>'
          '<p>Nejčastější chyba je, že si lidé vyberou brýle zvlášť a pak mezi helmou a rámem zůstane mezera, tzv. gap. Tou táhne studený vzduch a na čele vzniká červený pruh od mrazu. '
          'Brýle se proto zkouší v helmě. Popruh se nastavuje tak, aby brýle seděly pevně, ale netlačily na nos. Většina výrobců helem i brýlí uvádí, s kterou řadou se nejlépe doplňují, a nabízí kompletní sety. '
          'Najdete je v kategoriích <a href="/lyzarske-helmy/">lyžařské helmy</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>, které musí pod helmu a pod popruh také vejít.</p>'
          '<h2>Velikost rámu a tvar obličeje</h2>'
          '<p>Rámy se vyrábějí ve třech až čtyřech velikostech: dětské, malé (S), střední (M) a velké (L, často označované jako XL). Dospělí s užším obličejem často sáhnou po malém rámu, který nedoléhá příliš do tváří. '
          'Velké rámy mají širší zorné pole a více prostoru pro dioptrické brýle, jsou ale těžší a v menší helmě mohou překážet. Při zkoušení zkontrolujte tři body: pěna musí doléhat na čelo, tváře i nos bez mezer, nos nesmí být přitlačen k čočce a zorné pole do stran musí zůstat volné.</p>'
          '<h2>Brýle pro nositele dioptrií</h2>'
          '<p>Kdo nosí dioptrické brýle, má tři cesty. Kontaktní čočky jsou nejpohodlnější. Brýle typu OTG mají hlubší rám a výřezy v pěně, takže se pod ně vejdou běžné dioptrické obruby, jen si dejte pozor na tlak popruhu na stranice. '
          'Třetí variantou je klip s dioptrickými čočkami, který se připevní dovnitř rámu. Ten je třeba objednat u optika a hodí se pro silnější dioptrie. Při zkoušce si vezměte vlastní brýle s sebou.</p>'
          '<h2>Pro koho jaké brýle</h2>'
          '<h3>Rekreační lyžaři</h3>'
          '<p>Stačí brýle s zorníkem kategorie 2 nebo 3 a rámem, který dobře sedí k vaší helmě. Pokud lyžujete jednou za rok na dovolené, vydržíte s jednodušším modelem. Pro náročnější den si přibalte čirou čočku do mlhy.</p>'
          '<h3>Snowboardisté a freeriders</h3>'
          '<p>Snowboardisté často padají na obličej a častěji sedí, takže ocení měkčí rám a větší zorné pole. Freeriders, kteří vyrážejí do neupravených svahů, vybírají čočky s dobrým kontrastem a rám s dobrou větratelností, protože při výstupu se hodně potí. Pro oba sporty hledejte i v kategoriích <a href="/snowboarding/">snowboarding</a> a <a href="/snowboardy/">snowboardy</a>.</p>'
          '<h3>Děti a začátečníci</h3>'
          '<p>Dětské brýle mají menší rám, měkčí pěnu a nastavitelný popruh. Zorník kategorie 2 až 3 je obvykle dostačující. Děti mají tendenci brýle zvedat na čelo, a proto zvolte model s dobrým odvětráním a naučte je je sundávat ve stanicích a v bufetu. Ke komplet <a href="/lyzarske-boty/">lyžařským botám</a> a <a href="/lyzarske-helmy/">helmě</a> se hodí nastavení předem doma.</p>'
          '<h3>Jízda na běžkách</h3>'
          '<p>Běžkaři při vysoké tepové frekvenci snadno zamlží běžné sjezdové brýle a obvykle sáhnou po lehčích sportovních modelech, viz <a href="/sportovni-bryle/">sportovní a sluneční brýle</a>. Sjezdové brýle se na běžky hodí, jen když jsou dobře větrané.</p>'
          '<h2>Péče o brýle</h2>'
          '<ul><li>Po jízdě je neutírejte do mokra rukavicí. Nechte je oschnout volně na vzduchu a teprve potom je uložte do měkkého pouzdra.</li>'
          '<li>Uvnitř čočky se nedotýkejte prstem. Mikrovlákno používejte jen na suchou nebo lehce navlhčenou čočku.</li>'
          '<li>Neodkládejte je v autě ani na topení. Rám i lepení zorníku by se mohlo deformovat.</li>'
          '<li>Při přepravě v batohu je vždy schovejte do pouzdra, aby je nepoškrábaly klíče a hrany.</li>'
          '<li>Před sezónou zkontrolujte popruh, pružnost pěny a stav těsnění zorníku.</li></ul>'
          '<h2>Světlo na svahu během dne</h2>'
          '<p>Ráno bývá světlo ostré a nízké, v poledne nejvíc oslňuje odraz od sněhu a odpoledne se na svazích objevují stíny, ve kterých zmizí tvary terénu. Při každé z těchto fází potřebujete trochu jiný zorník. '
          'Po ránu bývá vhodná střední kategorie, v poledne tmavší a zrcadlová, odpoledne a ve stínu lesa světlejší s dobrým kontrastem. Kdo střídá slunce a lesní úseky, ocení právě fotochromatické čočky nebo druhý zorník v batohu. '
          'Pamatujte, že i při zatažené obloze se UV záření odráží od sněhu, takže zorník by měl vždy deklarovat ochranu před UV zářením. Hledejte označení UV400 a značku CE s odkazem na normu EN ISO 12312-1.</p>'
          '<h2>Orientační postup nákupu</h2>'
          '<ol><li>Změřte si, jakou helmu máte, nebo si ji pořiďte jako první, protože podle ní se vybírá rám.</li>'
          '<li>Rozhodněte se, zda potřebujete OTG, dětský střih, nebo širší rám.</li>'
          '<li>Vyberte kategorii zorníku podle toho, kdy a kde jezdíte nejčastěji.</li>'
          '<li>Rozhodněte, zda budete mít druhý zorník s sebou, případně zvolte fotochromatický.</li>'
          '<li>Porovnejte nabídky obchodů u konkrétního modelu a barvy a ověřte vratnou lhůtu.</li></ol>'
          '<p>Takto vybrané brýle vydrží několik sezón, pokud o ně budete pečovat a pravidelně kontrolovat stav popruhu a těsnění. V případě pochybností si model vyzkoušejte přímo v prodejně a teprve potom porovnejte nabídky online.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii nejčastěji uvidíte značky ' + B(('alpina', 'Alpina'), ('uvex', 'Uvex'), ('rossignol', 'Rossignol'), ('relax', 'Relax'), ('smith', 'Smith'), ('salomon', 'Salomon'), ('bliz', 'Bliz'), ('scott', 'Scott'), ('dragon', 'Dragon'), ('meatfly', 'Meatfly')) + '. '
          'U evropských výrobců narazíte na široký výběr dětských řad a variant pro dioptrie. Americké značky bývají silné ve výměnných zorníkách a freeridu. Dílčí rozdíly dělá hlavně kvalita antifogu, konstrukce rámu a systém výměny čoček, proto porovnávejte konkrétní řady, nikoli jména.</p>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li>Zkoušení bez helmy. Pak zjistíte, že se mezi okrajem a rámem otevřela mezera.</li>'
          '<li>Výběr příliš tmavého zorníku pro celý den. Při zhoršení počasí hůř uvidíte hrbolky.</li>'
          '<li>Koupě náhradního zorníku od jiné řady, než jakou máte. Neleze to do rámu.</li>'
          '<li>Čištění papírovým kapesníkem nebo oděvem, který čočku poškrábe.</li>'
          '<li>Nastavení příliš těsného popruhu, který tlačí na nos a způsobuje bolest hlavy.</li></ul>'
          '<h2>K brýlím patří i zbytek zimní výbavy</h2>'
          '<p>Na svah se nechodí jen s brýlemi. Projděte si <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-termopradlo/">termoprádlo</a> a <a href="/lyzarske-doplnky/">lyžařské doplňky</a>. '
          'Sezónní přehled najdete v nadřazené kategorii <a href="/zimni-sporty/">zimní sporty</a>.</p>',
    faq=[('Jakou kategorii zorníku zvolit na většinu dnů?', 'Pro běžný den na sjezdovce se nejčastěji volí kategorie 2 nebo 3. Při mlze a sněžení je lepší světlejší čočka, na ledovci a při velmi ostrém slunci tmavší.'),
         ('Je lepší fotochromatický, nebo výměnný zorník?', 'Fotochromatický zorník se přizpůsobuje sám, ale reaguje s mírným zpožděním a v mrazu pomaleji. Výměnné zorníky jsou rychlejší na změnu, vyžadují ale náhradní čočku v batohu.'),
         ('Proč se mi lyžařské brýle mlží?', 'Teplý a vlhký vzduch od obličeje se sráží na studené čočce. Pomáhá dvojitý zorník, funkční větrání, nezvedání brýlí na čelo a neutírání vnitřní strany prsty.'),
         ('Jak poznám, že brýle sedí k helmě?', 'Mezi okrajem helmy a rámem brýlí nesmí vzniknout mezera. Při zkoušení vždy nasaďte helmu, nastavte popruh a ověřte, že nic netlačí a výhled do stran zůstává volný.'),
         ('Mohu v lyžařských brýlích nosit dioptrické brýle?', 'Ano, pokud zvolíte model OTG s hlubším rámem nebo klip s dioptrickými čočkami. Samotné běžné brýle se pod malý rám často nevejdou, proto je zkoušejte společně.'),
         ('Hodí se lyžařské brýle i na snowboard?', 'Ano, pro oba sporty platí stejná pravidla výběru. Snowboardisté bývají citlivější na měkčí rám, protože při pádu dopadají častěji na obličej.'),
         ('Jak vybrat brýle pro dítě?', 'Hledejte dětský rám, měkčí pěnu, nastavitelný popruh a zorník kategorie 2 až 3. Brýle musí padnout k dětské helmě, jinak se na čele otevře mezera.'),
         ('Jak čistit zorník a antifog?', 'Nechte brýle volně oschnout a pak je jemně otřete mikrovláknem. Vnitřní stranu se nedotýkejte prsty ani rukavicí, antifogová vrstva se otěrem poškodí.'),
         ('Kdy vyměnit zorník nebo celé brýle?', 'Zorník vyměňte, když je hluboce poškrábaný nebo se při světle objevují odlesky. Celé brýle měňte, jakmile je rám popraskaný, pěna rozpadlá nebo popruh ztratil pružnost.'),
         ('Jaké náhradní zorníky se k mým brýlím hodí?', 'Zorníky nejsou univerzální. Musí být určené pro stejný model a stejnou velikost rámu. Řadu najdete na rámu nebo v popisu, čočky se hledají v kategorii náhradních zorníků.')])

# ------------------------------------------------------------------ stany
NEW['stany'] = dict(long=True,
    title='Stany: turistické, rodinné, pop-up, střešní',
    desc='Stany pro turistiku, rodinné kempování, pláž i expedice: vodní sloupec, váha, počet osob, konstrukce a péče. Ceny českých obchodů vedle sebe.',
    intro='<p>Dobrý <strong>stan</strong> vás má uchránit před deštěm, větrem a komáry s co nejmenší námahou při stavění i balení. Proto se stany dělí podle toho, kam s nimi půjdete: lehké dvoulůžkové stany se nosí v batohu, rodinné stany se vozí v kufru auta, '
          'pop-up stany se rozbalí za pár vteřin na pláži a expediční stany snesou sněhové zatížení. Každá z těchto skupin řeší jiný problém, a proto nemá smysl hledat jeden univerzální model.</p>'
          '<p>V kategorii najdete <a href="/turisticke-stany/">turistické a trekové stany</a>, <a href="/rodinne-stany/">rodinné a kempingové</a>, <a href="/pop-up-a-plazove-stany/">pop-up a plážové</a>, <a href="/strechni-stany/">střešní stany</a> a mnoho dalšího. '
          'Sporteka srovnává nabídky českých obchodů u stejného modelu, takže zjistíte, kde je skladem správná velikost a barva. Kompletní přehled kempování shrnuje <a href="/kemping/">kemping</a>.</p>',
    guide='<h2>Přehled typů stanů</h2>'
          '<p>Než začnete porovnávat parametry, rozhodněte, jak budete stan přepravovat. Od toho se odvíjí váha, velikost po složení i konstrukce.</p>'
          + T(['Typ', 'Hodí se pro', 'Hlavní přednost', 'Na co dát pozor'], [
              ['Turistický a trekový', 'pěší túry, kola, kajak', 'nízká hmotnost, malý sbalený objem', 'menší vnitřní prostor, tenčí materiály'],
              ['Expediční a čtyřsezónní', 'hory, sníh, silný vítr', 'pevná kostra, odolnost proti větru', 'vyšší váha a složitější stavba'],
              ['Rodinný a kempingový', 'rodiny, pobyty na kempu', 'prostor pro stání, ložnice a předsíň', 'velký a těžký, nosí se jen z auta'],
              ['Pop-up a plážový', 'pláž, zahrada, festival', 'postavení za okamžik', 'slabší na vítr a déšť, skládání chce cvik'],
              ['Střešní, autostany a předstany', 'cestování autem či karavanem', 'stavba přímo na vozidle', 'musí odpovídat nosiči a vozu'],
              ['Týpí a lavvu', 'skupiny, táborové pobyty', 'centrální prostor, snadná ventilace', 'nižší odolnost vůči silnému větru'],
              ['Rybářský stan a bivak', 'rybáři, dlouhé výpravy', 'pevná podlážka, rychlé postavení', 'těžší a objemnější']]) +
          '<p>U každého typu najdete nabídku v podkategoriích: <a href="/expedicni-stany/">expediční a čtyřsezónní stany</a>, <a href="/tipi-a-lavvu/">týpí a lavvu</a>, <a href="/rybarske-stany/">rybářské stany a bivaky</a> nebo <a href="/detske-stany/">dětské stany</a>. '
          'Pro hromadné akce slouží <a href="/pristresky-a-party-stany/">přístřešky a párty stany</a>.</p>'
          '<h2>Počet osob a skutečný prostor</h2>'
          '<p>Údaj „pro dvě osoby“ znamená, že dvě osoby se vejdou těsně vedle sebe bez zavazadel. Pokud chcete mít uvnitř batoh a boty, vybírejte o osobu větší. Stejně tak pro dvě osoby s dítětem počítejte velikost pro čtyři. '
          'Důležitá je i výška: vysoký stan umožní sedět a převléknout se, nízký trekový ušetří váhu. Předsíň neboli apsida slouží na boty, vařič za deště a batohy. Dvě apsidy se hodí pro dvě osoby, aby měla každá vlastní vchod a odkládací prostor.</p>'
          '<h2>Vodní sloupec a kvalita materiálů</h2>'
          '<p>Vodní sloupec se uvádí v milimetrech a říká, jak vysoký sloupec vody dokáže látka vydržet, než začne propouštět. Čím vyšší číslo, tím větší odolnost vůči deštivým dnům, ovšem na dobré chování ve skutečnosti rozhodují i švy. '
          'Ty by měly být zatmelené nebo zalepené páskou. Podlážka bývá vždy odolnější než střecha, protože na ni působí tlak země a váha těla. Při vícenásobném používání se těsnění švů a impregnace opotřebovávají a je třeba je obnovit sprejem nebo tmelem, viz <a href="/stanove-doplnky/">plachty, podlážky a opravy stanů</a>.</p>'
          '<h2>Konstrukce a stavba</h2>'
          '<p>Tunelový stan má oblouky v řadě a nabízí velký prostor za nízkou hmotnost, ale musí se vždy zakotvit. Kupolový stan se vzájemně křížícími oblouky stojí sám a snáší vítr z více směrů. '
          'Geodetická kostra má více křížení a vydrží největší zátěž. Jednoduché pop-up stany využívají pružné obruče, které se při vybalení samy rozevřou. U většiny stanů se používá dvouplášťová konstrukce: vnitřní prodyšný stan a vnější nepromokavý příkrov, mezi nimiž proudí vzduch a odvádí kondenzaci. '
          'Jednoplášťové a ultralehké modely šetří váhu, ale vyžadují větší pozornost při větrání.</p>'
          '<h2>Roční období</h2>'
          '<ul><li><strong>Léto:</strong> dvouplášťový stan s velkými sítěnými okny a dobrou ventilací, protože horký vzduch a vlhkost by se uvnitř hromadily.</li>'
          '<li><strong>Jaro a podzim:</strong> pevnější kostra, pevné švy a nižší sítěná část, ať dovnitř nefouká.</li>'
          '<li><strong>Zima:</strong> expediční konstrukce s pevnými oblouky a sněžnou sukní kolem dokola. Musíte počítat s nezbytností kvalitní karimatky a spacáku.</li>'
          '<li><strong>Pláž a festival:</strong> lehký a snadno stavitelný přístřešek, který odrazí slunce a udělá stín.</li></ul>'
          '<h2>Pro koho jaký stan</h2>'
          '<h3>Pěší turisté a cyklisté</h3>'
          '<p>Na túru se vybírá podle váhy a sbaleného rozměru. Pokud jdete ve dvou, rozdělte hmotnost: jeden nese vnitřní stan, druhý příkrov a kostru. Vybírejte trekové stany s jednoduchou stavbou, kterou zvládnete i v dešti, a nezapomeňte na vhodný <a href="/turisticke-batohy/">turistický batoh</a> a <a href="/spaci-pytle/">spací pytel</a>.</p>'
          '<h3>Rodiny s dětmi</h3>'
          '<p>Rodinný stan má velký stanový prostor s oddělenými ložnicemi a stojí často po celé dovolené. Důležité je stání ve výšce dospělého, velká předsíň a pevné vchody. Dětem se líbí i malý <a href="/detske-stany/">dětský stan</a> na zahradu, který však není určen na noční spaní venku.</p>'
          '<h3>Rybáři a lovci</h3>'
          '<p>Rybářské stany a bivaky jsou pevné, často s podlážkou a velkým vchodem. Pro rybáře navazuje kategorie <a href="/rybareni/">rybaření</a> a pro lovce <a href="/lov-a-priroda/">lov a příroda</a>.</p>'
          '<h3>Cestování autem</h3>'
          '<p>Střešní stany a autostany se postaví rychle a držejí s vozem. Před koupí zkontrolujte nosnost střechy vozu a rozměry příčníků. Předstany prodlužují obytný prostor karavanu o další místnost.</p>'
          '<h2>Příslušenství, bez kterého se neobejdete</h2>'
          '<p>Ke stanu patří kolíky vhodné pro daný terén, podlážka a oprava. V kategorii <a href="/stanove-doplnky/">plachty, podlážky a opravy</a> najdete tmel, záplaty, tyčky i další náhrady. Uvnitř se hodí <a href="/kempingovy-nabytek/">kempingový nábytek</a>, <a href="/kempingove-nadobi/">kempingové nádobí</a>, <a href="/celovky-a-svitilny/">čelovky a svítilny</a> a <a href="/kempingove-doplnky/">kempingové doplňky</a>. '
          'Pro přespání v přírodě bez stanu je tu nabídka <a href="/spaci-pytle/">spacích pytlů</a> a <a href="/outdoor/">outdoorové výbavy</a>.</p>'
          '<h2>Péče o stan a skladování</h2>'
          '<ul><li>Po sbalení doma stan úplně vysušte, jinak vznikne plíseň a impregnace se rozpadne.</li>'
          '<li>Neperte ho v pračce. Čistěte měkkým kartáčem, vlažnou vodou a jemným mýdlem.</li>'
          '<li>Uložte ho volně, nikoli stlačený v obalu, a mimo přímé slunce. UV záření zeslabuje látku.</li>'
          '<li>Kolíky očistěte od hlíny a zkontrolujte zohýbané. Tyčky vždy skládejte od středu, ať se neláme gumička.</li>'
          '<li>Před sezónou stan postavte na zahradě a zkontrolujte zipy, švy i sítě.</li></ul>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li>Volba stanu podle počtu osob bez ohledu na zavazadla.</li>'
          '<li>Koupě rodinného stanu na pěší túru, protože je levný a prostorný. Každý kilogram navíc se na túře projeví.</li>'
          '<li>První stavba až na dovolené. Doma si ji vyzkoušejte, než se na místě rozprší.</li>'
          '<li>Zakoupení bez podlážky nebo jakékoli ochrany spodku v hrubém terénu.</li>'
          '<li>Podcenění větru: stan s pevnou kostrou nic nezmůže bez řádně zatlučených kolíků a stahovacích lanek.</li></ul>'
          '<h2>Jak vybrat místo a postavit stan</h2>'
          '<p>Hledejte rovnou plochu bez kamenů, kořenů a prohlubní, ve kterých by se držela voda. Vchod otočte pryč od převládajícího větru a stan stavte nejméně pár kroků od vody, kde se v noci drží vlhkost a mlha. '
          'Nejdřív rozložte podlážku, poté sestavte kostru, připevněte vnitřní stan a nakonec natáhněte příkrov. Kolíky zatloukejte šikmo od stanu a lanka napněte tak, aby plachta nepřiléhala k vnitřnímu stanu, jinak vlhkost prosákne dovnitř. '
          'Při zimní stavbě na sněhu se kolíky nahrazují zasypanými předměty nebo speciálními kotvami, protože klasické kolíky se v měkkém sněhu nedrží.</p>'
          '<h2>Kondenzace a větrání</h2>'
          '<p>Ráno bývá uvnitř stanu mokro i za sucha. Dýchání a pot vytvářejí vlhkost, která se sráží na chladné plachtě. Pomáhá větrání otevřenými průduchy ve střeše, mírně pootevřený vchod a stan postavený tak, aby plachta nikde nedosedala na vnitřní stan. '
          'Mokré oblečení a boty nenoste dovnitř, nechte je v předsíni. Ráno stan setřete a před sbalením ho nechte alespoň krátce oschnout na slunci a větru, abyste pak doma nemuseli řešit plíseň.</p>'
          '<h2>Orientační postup nákupu</h2>'
          '<ol><li>Určete, jak stan přepravíte: pěšky, na kole, nebo autem.</li>'
          '<li>Spočítejte osoby i zavazadla a přidejte rezervu jednoho místa.</li>'
          '<li>Rozhodněte, v jakém ročním období a jak často budete stan používat.</li>'
          '<li>Porovnejte hmotnost, vodní sloupec, konstrukci a počet vchodů.</li>'
          '<li>Dokupte podlážku, kolíky a opravárenskou sadu a stan si doma vyzkoušejte postavit.</li></ol>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('skandika', 'Skandika'), ('husky', 'Husky'), ('quechua', 'Quechua'), ('jurek', 'Jurek'), ('high-peak', 'High Peak'), ('hannah', 'Hannah'), ('trimm', 'Trimm'), ('pinguin', 'Pinguin'), ('3f-ul-gear', '3F UL GEAR'), ('naturehike', 'Naturehike'), ('outwell', 'Outwell'), ('coleman', 'Coleman')) + '. '
          'Mezi nimi jsou výrobci zaměření na ultralehké turistické modely, rodinné kempingové stany i dostupné pop-up řady. Při porovnání dívejte na konkrétní řadu a údaje o hmotnosti, rozměru a vodním sloupci, nikoli pouze na název značky.</p>',
    faq=[('Jaký vodní sloupec má mít stan?', 'Záleží na použití. Na letní kempování stačí nižší hodnota, na deštivé túry a hory potřebujete vyšší. Důležité jsou také zatmelené švy a kvalitní podlážka.'),
         ('Kolik osob se do stanu opravdu vejde?', 'Údaj výrobce počítá se spaním těsně vedle sebe. Pokud chcete mít uvnitř batohy a boty, vyberte stan pro o jednu osobu větší, než kolik vás je.'),
         ('Čím se liší jednoplášťový a dvouplášťový stan?', 'Dvouplášťový má vnitřní stan a vnější plachtu, mezi nimiž proudí vzduch a odvádí vlhkost. Jednoplášťový je lehčí a rychlejší na stavbu, ale víc kondenzuje.'),
         ('Jaký stan vybrat na pěší túru?', 'Nejlehčí, jaký unesete, s malým sbaleným rozměrem a snadnou stavbou. Hmotnost můžete rozdělit mezi dva turisty a stan si předem vyzkoušejte na zahradě.'),
         ('Je pop-up stan vhodný na vícedenní kempování?', 'Hodí se spíš na pláž, festival a krátké pobyty. Jeho tenčí materiály a pružná konstrukce neodolají dlouhému dešti ani silnému větru tak, jako klasický stan.'),
         ('Jak stan správně vysušit a uložit?', 'Doma ho úplně rozložte a nechte uschnout ve stínu, teprve pak složte. Uložte ho volně na suchém místě, aby se nezačala tvořit plíseň ani nerozpadla impregnace.'),
         ('Jak opravit prasklý oblouk nebo díru v plachtě?', 'Na tyčky existují rychlé spojky a manžety, na látku záplaty se samolepicí vrstvou a tmel na švy. Vše najdete v kategorii plachet, podlážek a oprav stanů.'),
         ('K čemu slouží podlážka pod stan?', 'Chrání spodek před oděrem o kameny a zeminu a zvyšuje odolnost proti zatékání zespodu. Musí být o něco menší než půdorys stanu, aby se pod ní nehromadila dešťová voda.'),
         ('Na co dát pozor u střešního stanu?', 'Na nosnost střechy auta, rozměr příčníků a způsob upevnění. Informace o maximálním zatížení najdete v návodu k vozu a v popisu stanu.'),
         ('Jak stan zajistit proti větru?', 'Zatlučte všechny kolíky šikmo do země, použijte stahovací lanka a postavte stan zadní stranou proti větru. V písku nebo sněhu se používají speciální kotvy.')])

# ------------------------------------------------------------------ cyklo-brzdy
NEW['cyklo-brzdy'] = dict(long=True,
    title='Brzdy na kolo: destičky, kotouče, lanka',
    desc='Brzdy na kolo: brzdové destičky, kotouče, třmeny, páky, hadičky a lanka. Jak poznat typ, opotřebení a výběr kompatibilního dílu. Ceny obchodů.',
    intro='<p>Brzdy jsou jediná část kola, která musí fungovat vždycky, ať je mokro, bláto, nebo dlouhý sjezd. Proto se s nimi nevyplatí improvizovat: <strong>brzdové destičky, kotouče, třmeny, páky, hadičky a lanka</strong> musí sedět přesně k systému, který máte na kole. '
          'Nejvíc nákupů se vrací kvůli záměně destiček, protože i podobně vypadající díly mají jiný tvar a jinou pryskyřici nebo kovový základ.</p>'
          '<p>Najdete tu díly pro hydraulické i lanové kotoučové brzdy, pro ráfkové brzdy typu V-brake i silniční třmeny a také příslušenství k odvzdušnění a seřízení. Sporteka porovnává nabídky českých obchodů u stejného dílu, takže vidíte, kde je skladem váš typ. '
          'Pokud hledáte i další komponenty, otevřete hlavní kategorii <a href="/cyklo-dily/">díly a pláště</a>.</p>',
    guide='<h2>Základní typy brzd na kole</h2>'
          '<p>Než začnete cokoli kupovat, zjistěte, jaký systém na kole máte. Na první pohled se rozliší podle toho, kde se brzdí: u kotoučové brzdy tlačí třmen destičky na kovový kotouč u náboje, u ráfkové brzdy tlačí špalky přímo na bok ráfku.</p>'
          + T(['Typ brzdy', 'Kde se používá', 'Výhody', 'Na co dát pozor'], [
              ['Hydraulická kotoučová', 'horská, trailová, gravel i silniční kola', 'silný a citlivý brzdný účinek, málo síly na páce', 'nutné odvzdušnění, správná kapalina, citlivost na znečištění'],
              ['Lanová kotoučová', 'trekingová, městská, dětská kola', 'jednodušší servis, dostupnost dílů', 'nutné seřizování, lanko se prodlužuje'],
              ['Ráfková typu V-brake', 'starší trekingová a městská kola', 'jednoduchost a levný provoz', 'opotřebovává ráfek, za mokra slabší'],
              ['Silniční třmeny', 'silniční kola s ráfkovými brzdami', 'nízká hmotnost', 'kompatibilita s pláštěm a ráfkem'],
              ['Torpédo a bubnové', 'městská kola s brzdou uvnitř náboje (torpédo je v zadním)', 'uzavřené, nenáročné na údržbu', 'menší výkon, teplo při dlouhém brzdění']]) +
          '<p>Jednoduché pravidlo pro rozpoznání: pokud vidíte kovový kotouč u náboje, jde o kotoučovou brzdu. Pokud je od páky vedena tenká tkanice nebo pancíř, je lanová. Pokud jdou z páky tenké hadičky plněné kapalinou, je hydraulická.</p>'
          '<h2>Brzdové destičky</h2>'
          '<p>Destičky jsou spotřební díl, který se opotřebovává nejrychleji. Skládají se z nosné ocelové desky a brzdového obložení. Existují tři základní druhy:</p>'
          '<ul><li><strong>Organické (pryskyřičné)</strong> brzdí tiše, jemně a dobře reagují hned po nasazení. Za mokra rychleji opotřebují a při dlouhém sjezdu se přehřívají.</li>'
          '<li><strong>Kovové (spékané, sintrované)</strong> vydrží déle, odolávají teplu a hodí se do náročného terénu. Mohou být hlasitější a vyžadují delší záběh.</li>'
          '<li><strong>Semi-metalické</strong> jsou kompromis mezi oběma a často se používají jako univerzální řešení.</li></ul>'
          '<p>Správné destičky poznáte podle tvaru a označení modelu brzdy. Nejdůležitější je vždy značka brzdy a konkrétní řada, protože destičky Shimano, Sram, Magura či Tektro mají odlišný tvar a nelze je zaměňovat. '
          'Naučte se číst označení na brzdovém třmenu nebo v návodu a podle něj hledejte kompatibilní díl.</p>'
          '<h2>Kotouče</h2>'
          '<p>Kotouč se vybírá podle tří údajů: průměr, upevnění a materiál. Průměr bývá u dospělých kol nejčastěji v rozmezí 140 až 203 mm. Větší kotouč má vyšší brzdný účinek a lépe odvádí teplo, menší je lehčí. '
          'Upevnění je buď šest šroubů, nebo centrální zámek (Centerlock), a na náboji musí odpovídat. Kotouč lze použít jen na náboj se stejným systémem, případně s adaptérem. '
          'Pro náročnější použití se kotouče vyrábějí z několika vrstev oceli a hliníku, které lépe odvádějí teplo. Tenký kotouč s hlubokými rýhami se po opotřebení vyměňuje, takže sledujte minimální tloušťku vyznačenou na něm.</p>'
          '<h2>Třmeny a páky</h2>'
          '<p>Třmen je část, ve které jsou písty a destičky. Hydraulický třmen má jeden až čtyři písty. Dvoupístkové třmeny stačí pro většinu kol, čtyřpístkové se používají tam, kde se brzdí dlouho a ostře. '
          'Páku musíte vybírat s ohledem na vedení hadičky a na to, která páka ovládá které kolo (v ČR bývá pravá páka zadní brzda, ale u dovezených kol to může být naopak). Na řídítkách se musí vejít spolu s řazením a případně sedlovkou.</p>'
          '<h2>Hadičky, lanka a pancíře</h2>'
          '<p>Lanové brzdy potřebují lanko a pancíř. Při výměně je dobré sladit oboje: nové lanko v opotřebovaném pancíři se zasekává. Konce pancíře opatřete koncovkou, aby se nerozstřapily a dovnitř nevnikl písek. '
          'Hydraulické brzdy mají hadičku, která se při zkrácení musí znovu odvzdušnit. Odvzdušnění se provádí speciální sadou a pro každý systém je jiné: některé brzdy používají minerální olej, jiné DOT kapalinu. '
          'Nikdy je nemíchejte. Špatná kapalina rozleptá těsnění a vyřadí brzdu z provozu.</p>'
          '<h2>Jak poznat opotřebení</h2>'
          '<ul><li>Destičky: obložení je tenké kolem 1 mm nebo vidíte kovovou základnu. Při brzdění cítíte kovové skřípění.</li>'
          '<li>Kotouč: tloušťka brzdné plochy je pod minimem vyznačeným na kotouči, případně je kotouč zkroucený nebo ožlutlý a při jízdě drhne.</li>'
          '<li>Páka: musí se táhnout bezmála až k řídítkům, případně se vrací pomalu.</li>'
          '<li>Lanko: tuhé, zrezivělé nebo roztřepené, páka se vrací těžce.</li>'
          '<li>Špalky: sjeté drážky, nerovnoměrné opotřebení, opotřebovaný ráfek.</li></ul>'
          '<h2>Výměna destiček krok za krokem</h2>'
          '<p>Vyjměte kolo, vytáhněte pojistný čep nebo šroub a opatrně vysuňte staré destičky. Písty zatlačte zpět plastovou nebo dřevěnou páčkou, nikdy ne šroubovákem na obložení. Vložte nové destičky se stejnou orientací pružinky a zajistěte čepem. '
          'Po nasazení kola několikrát stiskněte páku, aby se destičky vycentrovaly. Pak je zajeďte: opakovaně brzděte z mírné rychlosti, aby se obložení usadilo na kotouči. Na kotouč a obložení nesmí přijít olej ani mazivo. Pokud se to stane, destičky se po vyčištění stejně nemusí vrátit do původního stavu.</p>'
          '<h2>Údržba a čištění</h2>'
          '<p>Kotouče čistěte speciálním čističem na brzdy nebo isopropylalkoholem a čistým hadrem. Nikdy nepoužívejte univerzální mazací spreje v blízkosti kotouče. Údržbu najdete i v kategorii <a href="/cyklo-udrzba/">údržba kola: mazadla a čističe</a>, kde jsou čističe i odmašťovače. '
          'K seřízení se hodí kategorie <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>, zejména imbusové klíče a momentový klíč. Při pádu zkontrolujte rovnost kotouče a funkci páky.</p>'
          '<h2>Pro koho jaké brzdy</h2>'
          '<h3>Městští jezdci a dojíždějící</h3>'
          '<p>Pro každodenní jezdce je klíčová spolehlivost a nenáročný servis. Osvědčené jsou lanové kotoučové brzdy nebo odolné ráfkové. Nezapomeňte na <a href="/cyklo-svetla/">světla</a> a <a href="/cyklo-blatniky/">blatníky</a>, které ochrání brzdy před blátem.</p>'
          '<h3>Horská a trailová kola</h3>'
          '<p>Při dlouhých sjezdech se brzdy přehřívají. Volte hydraulické brzdy, kovové destičky, větší kotouče a třmeny s více písty. Vidlice a tlumiče najdete v kategorii <a href="/cyklo-vidlice-a-tlumice/">vidlice a tlumiče</a>.</p>'
          '<h3>Silniční a gravel kola</h3>'
          '<p>Na silnici se prosazují hydraulické kotoučové brzdy s menšími kotouči. Zkontrolujte, zda máte správné osy a upevnění, a pro výměnu ráfku nebo kola se podívejte do kategorie <a href="/cyklo-kola-a-rafky/">zapletená kola, ráfky a náboje</a>.</p>'
          '<h3>Rekreační a dětská kola</h3>'
          '<p>U dětí je důležitá snadná dosažitelnost páky a menší síla potřebná ke stisku. Pro rekreační jízdu na kole pomůže i kategorie <a href="/cyklo-riditka/">řídítka, představce a sedlovky</a>, kde nastavíte pozici páky.</p>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li>Koupě destiček podle vzhledu, ne podle modelu brzdy.</li>'
          '<li>Smíchání minerálního oleje s DOT kapalinou.</li>'
          '<li>Dotyk prstem na kotouč a následné mastné skvrny na třecí ploše.</li>'
          '<li>Přehlédnutí systému upevnění kotouče: šest šroubů neodpovídá Centerlocku.</li>'
          '<li>Výměna destiček bez kontroly kotouče, který pak opotřebuje nové obložení.</li>'
          '<li>Nedodržení záběhu. Nové destičky mají nižší účinek, dokud se nezajedou.</li></ul>'
          '<h2>Záběh a první kilometry</h2>'
          '<p>Nové destičky i kotouče se nejprve usadí do vzájemného tvaru. Najeďte na rovný úsek, rozjeďte se na střední rychlost a několikrát silně, ale plynule zabrzděte až na zhruba poloviční rychlost, bez zastavení. Pak totéž opakujte z vyšší rychlosti. '
          'Během záběhu se na kotouči vytvoří tenká vrstva materiálu z obložení, která zajišťuje stabilní brzdný účinek. Pokud se brzdy po záběhu stále jeví slabé nebo hlučné, zkontrolujte, zda se na kotouč nedostal tuk, a zda je třmen ustavený rovnoběžně s kotoučem.</p>'
          '<h2>Orientační postup nákupu</h2>'
          '<ol><li>Zjistěte, zda máte kotoučové, nebo ráfkové brzdy, a zda jsou lanové, nebo hydraulické.</li>'
          '<li>Přečtěte si značku a model třmenu, případně stáhněte návod výrobce.</li>'
          '<li>U kotouče si zapište průměr a typ upevnění na náboji.</li>'
          '<li>Rozhodněte, zda potřebujete spíš tichý chod, nebo vysokou odolnost proti teplu.</li>'
          '<li>Při pochybnostech nechte kontrolu na servisu, protože brzdy jsou bezpečnostní součástí kola.</li></ol>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('shimano', 'Shimano'), ('sram', 'Sram'), ('force', 'Force'), ('jagwire', 'Jagwire'), ('max1', 'Max1'), ('reverse', 'Reverse'), ('micro', 'Micro'), ('sinter', 'Sinter'), ('galfer', 'Galfer'), ('kool-stop', 'Kool Stop'), ('elvedes', 'Elvedes'), ('tempish', 'Tempish')) + '. '
          'Shimano a Sram dodávají celé systémy, Jagwire a Elvedes lanka a pancíře, Kool Stop a Galfer náhradní destičky pro více modelů. U náhradních destiček třetích stran porovnejte označení kompatibility s původním dílem.</p>'
          '<h2>Co ještě kolo potřebuje</h2>'
          '<p>Brzdy jsou jen část kola. Podívejte se i na <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklo-pedaly/">pedály</a>, <a href="/cyklo-zamky/">zámky</a> a <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>. Celý přehled najdete v kategorii <a href="/cyklistika/">cyklistika</a>.</p>',
    faq=[('Jak poznám, jaké brzdové destičky potřebuji?', 'Podle značky a modelu brzdového třmenu. Označení najdete na třmenu, v návodu nebo v popisu kola. Tvar obložení se u různých výrobců liší, takže nestačí jen zhruba podobný díl.'),
         ('Kdy vyměnit brzdové destičky?', 'Když obložení zbývá kolem 1 mm, vidíte kovovou základnu nebo brzdy skřípou kov o kov. Při dlouhém sjezdu nebo mokrém počasí se opotřebují rychleji.'),
         ('Jaký je rozdíl mezi organickými a kovovými destičkami?', 'Organické brzdí tišeji a rychleji se zahřejí, ale rychleji se opotřebují. Kovové vydrží déle a lépe snášejí teplo, jsou však hlasitější a chtějí delší záběh.'),
         ('Jak poznám, že je kotouč opotřebovaný?', 'Zkontrolujte minimální tloušťku vyznačenou na kotouči a rovnost při roztočení kola. Hluboká drážka nebo viditelné zkroucení znamená výměnu.'),
         ('Mohu smíchat DOT kapalinu s minerálním olejem?', 'Ne. Každý systém je určený pro jednu kapalinu a smíchání poškodí těsnění. Typ kapaliny najdete na třmenu, páce nebo v návodu výrobce brzd.'),
         ('Proč mi brzdy skřípou?', 'Příčinou bývá znečištěný kotouč nebo destičky, opotřebované obložení, špatné vycentrování třmenu nebo vlhkost. Pomůže vyčištění čističem na brzdy a kontrola ustavení.'),
         ('Co znamená záběh nových destiček?', 'Je to několikanásobné brzdění z mírné rychlosti, při kterém se obložení usadí na kotouči. Do té doby je brzdný účinek nižší a může být nevyrovnaný.'),
         ('Je lanová kotoučová brzda dostatečná?', 'Pro město, trekink a dětská kola ano. Pro dlouhé sjezdy v horách je výhodnější hydraulický systém, který brzdí citlivěji a s menší silou na páce.'),
         ('Jak vybrat velikost kotouče?', 'Podle upevnění a velikosti, kterou umožňuje vidlice a rám. Větší kotouč lépe odvádí teplo a brzdí silněji, menší je lehčí. Průměr musí odpovídat adaptéru na třmenu.'),
         ('Mohu brzdy vyměnit sám?', 'Výměna destiček a lanek je při dobrém nářadí zvládnutelná doma. Odvzdušnění hydrauliky a zkracování hadiček je náročnější a bezpečnější je nechat ho na servisu.')])

# ------------------------------------------------------------------ lov-a-priroda
NEW['lov-a-priroda'] = dict(long=True,
    title='Lov a příroda: oblečení, obuv, výbava',
    desc='Lovecké oblečení, obuv a výbava pro lov i pobyt v přírodě: maskování, vrstvení, dalekohledy, kamery, optika. Ceny českých obchodů vedle sebe.',
    intro='<p>Kdo tráví hodiny na posedu, v mlze nebo při přesunu lesem, ví, že výbava se hodnotí podle ticha, tepla a suchých nohou. Kategorie <strong>lov a příroda</strong> sdružuje oblečení, obuv a vybavení pro lovce, pozorovatele zvěře, fotografy přírody i ty, '
          'kdo chodí do lesa kvůli klidu. Oblečení v zeleno-hnědých barvách je pro ně praktická pracovní vrstva. Rozhodující je tichý materiál, který nešustí, dobrá izolace a barvy, které se neodlišují od okolí.</p>'
          '<p>V nabídce najdete <a href="/lovecke-obleceni/">lovecké oblečení a obuv</a> a <a href="/lovecke-vybaveni/">lovecké vybavení</a>. Sporteka srovnává nabídky českých obchodů u stejného zboží, takže uvidíte, kde je skladem vaše velikost. '
          'Příbuzné vybavení pro pobyt venku najdete v kategoriích <a href="/outdoor/">outdoor</a> a <a href="/kemping/">kemping</a>.</p>',
    guide='<h2>Co všechno v kategorii najdete</h2>'
          '<p>Nabídka se dělí na dvě velké skupiny, které se doplňují. Oblečení řeší pohodlí a maskování, vybavení řeší pozorování, přepravu a bezpečnost.</p>'
          + T(['Skupina', 'Typické zboží', 'K čemu slouží'], [
              ['Lovecké oblečení', 'bundy, kalhoty, vesty, košile, čepice', 'ochrana před zimou, deštěm a trním, maskování'],
              ['Lovecká obuv', 'holínky, gumové a kožené boty, termo boty', 'sucho a teplo při dlouhém stání či chůzi'],
              ['Optika', 'dalekohledy, monokuláry, dálkoměry', 'pozorování zvěře a odhad vzdálenosti'],
              ['Fotopasti a kamery', 'záznamové kamery do přírody, fotopasti', 'pozorování zvěře bez rušení'],
              ['Příslušenství', 'sedáky, vábničky, pouzdra, popruhy, nože', 'každodenní pohodlí a bezpečná přeprava'],
              ['Pro psy', 'výcvikové pomůcky, vodítka, reflexní vesty', 'výcvik a ochrana psa při práci']]) +
          '<p>Skupinu <a href="/lovecke-obleceni/">lovecké oblečení a obuv</a> doplňují ostatní outdoorové kategorie, například <a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, <a href="/softshellove-bundy/">softshellové bundy</a> a <a href="/trailove-boty/">trailové boty</a>. '
          'Vedle toho najdete užitečné <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoola</a>.</p>'
          '<h2>Vrstvení oblečení</h2>'
          '<p>Při pomalém stání na posedu se tělo rychle vychladí, při přesunu zase přehřeje. Proto se pracuje s vrstvami, které se dají postupně sundávat nebo přidávat.</p>'
          '<ul><li><strong>Spodní vrstva</strong> odvádí pot od těla. Vybírejte syntetiku nebo vlnu, bavlna se promočí a dlouho schne. Doplňky najdete i v kategorii <a href="/lyzarske-termopradlo/">termoprádlo</a>, které se k zimnímu lovu hodí.</li>'
          '<li><strong>Střední vrstva</strong> izoluje: fleece, prošívaná vesta nebo vlněný svetr. Čím tišší látka, tím lépe.</li>'
          '<li><strong>Vnější vrstva</strong> chrání před větrem a deštěm. Tichá membrána nebo softshell nešustí při pohybu.</li>'
          '<li><strong>Doplňky</strong> jako čepice, rukavice a nákrčník řeší teplo na okrajích těla. Zimní varianty hledejte i v <a href="/lyzarske-rukavice/">rukavicích</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepicích</a>.</li></ul>'
          '<h2>Maskování a barvy</h2>'
          '<p>Zvěř vidí barvy jinak než člověk a velmi dobře rozeznává pohyb. Barva oblečení proto pomáhá, ale ještě víc záleží na tom, jak se pohybujete. Základem jsou přírodní odstíny zelené a hnědé, listový vzor v lese a světlejší tóny na poli nebo ve sněhu. '
          'Maskovací vzory dělají siluetu nezřetelnou, aby se nedala snadno rozpoznat. Pro bezpečnost při společných honech se naopak používají výrazné vesty a čepice, pravidla k tomu stanoví místní předpisy a organizátor akce. Vždy se informujte u organizátora.</p>'
          '<h2>Obuv na posed, do terénu a do vody</h2>'
          '<p>Nohy trpí v zimě i v blátě nejvíc, proto se vyplatí věnovat jim zvláštní pozornost.</p>'
          + T(['Obuv', 'Výhody', 'Nevýhody'], [
              ['Gumové holínky', 'nepropustnost, snadné čištění', 'špatný odvod potu, nižší opora kotníku'],
              ['Neoprenové holínky', 'tepelná izolace a pružnost', 'těžší a dražší, hůř se čistí'],
              ['Kožené boty s membránou', 'dobrá opora, prodyšnost', 'vyžadují impregnaci a péči'],
              ['Termo boty se zateplením', 'teplo při nehybném sezení', 'při chůzi se rychle zpotí']]) +
          '<p>Při výběru velikosti počítejte s tlustšími ponožkami a stélkou. Obuv by měla mít prostor pro prsty, jinak se v zimě nedokrví. Ponožky jsou důležitější, než se zdá: vlněná nebo syntetická směs udrží teplo i při vlhku, bavlna ne. '
          'Podobné pravidlo platí i pro <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, které mohou posloužit v zimě.</p>'
          '<h2>Optika: dalekohledy, monokuláry a dálkoměry</h2>'
          '<p>Dalekohled se označuje dvěma čísly, například 8x42. První je zvětšení, druhé průměr předního objektivu v milimetrech. Čím větší objektiv, tím více světla, ale i vyšší hmotnost. '
          'Nižší zvětšení se lépe drží v ruce a má širší zorné pole, vyšší zvětšení přiblíží více, ale vyžaduje stabilní oporu. Pro pozorování za šera je důležitá kvalita skel a jejich vrstvení. '
          'Monokulár je lehčí a kompaktnější, ale pozorování jedním okem je namáhavější. Při koupi zkontrolujte vodotěsnost, naplnění dusíkem proti zamlžování a pogumování proti nárazům.</p>'
          '<h2>Fotopasti a pozorování zvěře</h2>'
          '<p>Fotopast je kamera s pohybovým čidlem, která se upevní ke stromu. Pomáhá zjistit, kdy a kde zvěř prochází, bez rušení. Důležité jsou rychlost spouště, dosah infračerveného přísvitu, způsob napájení a ukládání snímků na paměťovou kartu. '
          'Při umístění dodržujte právní předpisy: na cizím pozemku potřebujete souhlas majitele a nesmíte natáčet lidi bez jejich vědomí. Značky ve skupině zahrnují i výrobce fotopastí a výcvikových pomůcek pro psy.</p>'
          '<h2>Vybavení pro lov a pobyt v lese</h2>'
          '<ul><li><strong>Sedák a podložka</strong> izolují od studeného sedáku posedu.</li>'
          '<li><strong>Batoh a pouzdro</strong> musí být tiché a pohodlné. Vyberte si z kategorie <a href="/turisticke-batohy/">turistické batohy</a>.</li>'
          '<li><strong>Čelovka</strong> s červeným světlem nepřitahuje pozornost, nabídka v <a href="/celovky-a-svitilny/">čelovkách a svítilnách</a>.</li>'
          '<li><strong>Nůž a multitool</strong> do každodenní práce v terénu, viz <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoola</a>.</li>'
          '<li><strong>Termoska a stravování</strong> na dlouhé čekání, viz <a href="/outdoorova-strava/">outdoorová strava</a>.</li></ul>'
          '<h2>Pro koho jaká výbava</h2>'
          '<h3>Lovci</h3>'
          '<p>Pro lovce je základem tiché, teplé a nepromokavé oblečení, spolehlivá obuv a optika. U všeho ostatního rozhoduje, kde lovíte: na vysoké nebo nízké, v lese nebo na poli. Vždy dodržujte předpisy o lovu a bezpečnosti platné ve vaší honitbě.</p>'
          '<h3>Pozorovatelé zvěře a fotografové</h3>'
          '<p>Potřebují zejména tiché oblečení v tlumených barvách, dalekohled a sedák. Lov nemusí být cílem, často jde jen o pozorování bez rušení. Pro odpočinek pod širým nebem se hodí i <a href="/stany/">stany</a> a <a href="/spaci-pytle/">spací pytle</a>.</p>'
          '<h3>Rybáři a kempující</h3>'
          '<p>Rybáři a lidé, kteří tráví víkendy u vody, využijí tlumené barvy a nepromokavé vrstvy. Navazuje <a href="/rybareni/">rybaření</a> a <a href="/rybarske-obleceni/">rybářské oblečení</a>. Pro delší pobyty v přírodě nabízí kategorie <a href="/kemping/">kemping</a> i <a href="/kempingove-nadobi/">kempingové nádobí</a>.</p>'
          '<h3>Vojenský střih a maskování</h3>'
          '<p>Mezi značkami se objevují i výrobci vojenského a taktického oblečení. Pro lov a pozorování na nich oceníte odolnost proti otěru a množství kapes, jen dbejte na to, aby barvy a vzor splývaly s prostředím a oblečení bylo za pohybu tiché.</p>'
          '<h2>Péče o oblečení a obuv</h2>'
          '<ul><li>Impregnaci membrány obnovujte podle návodu pračkou nebo sprejem, jakmile voda přestane stékat po povrchu.</li>'
          '<li>Oblečení perte bez aviváže a bez bělicích prostředků, které zničí membránu a odstraní tlumicí vlastnosti.</li>'
          '<li>Boty po použití vyčistěte, vyjměte vložky a nechte volně vyschnout daleko od topení. Kůže se jinak zdeformuje.</li>'
          '<li>Optiku čistěte měkkým štětcem a mikrovláknem, nikdy ne hadrem na prach.</li>'
          '<li>Pachy z oblečení zmírníte větráním a praním bez parfemace, silné vůně zvěř odpuzují.</li></ul>'
          '<h2>Nejčastější chyby při koupi</h2>'
          '<ul><li>Koupě příliš těsné obuvi, do které se nevejdou teplé ponožky.</li>'
          '<li>Šustivá bunda, která prozradí každé pootočení.</li>'
          '<li>Volba velikosti dalekohledu podle zvětšení bez ohledu na světelnost a hmotnost.</li>'
          '<li>Bavlna jako spodní vrstva, která po zpocení dlouho schne a ochlazuje tělo.</li>'
          '<li>Nepočítání s tím, že při nehybném sezení se teplo ztrácí rychleji, než očekáváte.</li></ul>'
          '<h2>Jak se chovat v lese</h2>'
          '<p>Vybavení je jen jedna část, druhou je chování. Pohybujte se pomalu, zastavujte a poslouchejte, větrné počasí se hodí na přesun, bezvětří na pozorování. Postupujte proti větru, protože zvěř vnímá čichem lépe než zrakem a po větru by váš pach zachytila dřív, než vás uvidí. '
          'Odpadky odnášejte s sebou, v zemi zanechané věci narušují přírodu. Za šera je důležité mít při sobě světlo, mapu nebo telefon a dát někomu vědět, kam jdete a kdy se vrátíte. '
          'Při výpravách mimo vlastní honitbu respektujte soukromé pozemky, hospodářské zóny a chráněná území, kde platí zvláštní omezení.</p>'
          '<h2>Orientační postup nákupu</h2>'
          '<ol><li>Určete, jaké podmínky vás čekají: sezónu, výšku a typ terénu.</li>'
          '<li>Začněte obuví a spodní vrstvou, protože na nich závisí pohodlí nejvíc.</li>'
          '<li>Pak přidejte střední a vnější vrstvu a otestujte, zda šustí.</li>'
          '<li>Doplňte optiku nebo pozorovací techniku podle toho, jak daleko pozorujete.</li>'
          '<li>Porovnejte nabídky obchodů u stejného zboží a zkontrolujte velikostní tabulku.</li></ol>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii najdete značky ' + B(('solognac', 'Solognac'), ('tagart', 'Tagart'), ('jack-pyke', 'Jack Pyke'), ('mfh', 'Mfh'), ('mil-tec', 'Mil-tec®'), ('camo-systems', 'Camo Systems'), ('invadergear', 'Invadergear'), ('decathlon', 'Decathlon'), ('rothco', 'Rothco'), ('kombat', 'Kombat'), ('dogtra', 'Dogtra'), ('spypoint', 'Spypoint')) + '. '
          'Solognac a Tagart zastupují lovecké a outdoorové oblečení, Jack Pyke je britská značka venkovského oděvu, Mil-tec, Mfh a Rothco mají vojenský střih a Dogtra a Spypoint nabízejí výcvikové pomůcky pro psy a kamery do přírody. U obojků s elektrickým impulzem pozor: zákon na ochranu zvířat proti týrání jejich použití omezuje, proto vybírejte jen pomůcky bez elektrického impulzu. '
          'Při porovnání se dívejte na konkrétní řadu, materiál a velikostní tabulku.</p>',
    faq=[('Jak vybrat lovecké oblečení?', 'Podle místa a ročního období. Základem jsou vrstvy: spodní odvádí pot, střední izoluje a vnější chrání před větrem a deštěm. Látka by neměla šustit při pohybu.'),
         ('Jaké barvy jsou vhodné na lov?', 'Tlumené zelené a hnědé odstíny nebo maskovací vzory, které odpovídají prostředí. Zvěř reaguje hlavně na pohyb, takže důležité je i chování. Při společném honu platí pravidla o výrazných vestách.'),
         ('Jaká obuv se hodí na posed?', 'Nejčastěji zateplené holínky nebo termo boty, které udrží teplo při sezení. Při přesunu lesem se hodí kožená obuv s membránou. Velikost volte s rezervou na teplé ponožky.'),
         ('Co znamená označení dalekohledu 8x42?', 'První číslo je zvětšení, druhé průměr předního objektivu v milimetrech. Větší objektiv propustí více světla za šera, ale je těžší a objemnější.'),
         ('Hodí se bavlna jako spodní vrstva?', 'Moc ne. Bavlna se po zpocení dlouho suší a ochlazuje tělo. Lepší jsou syntetická vlákna nebo vlna, které odvádějí vlhkost a drží teplo i při vlhku.'),
         ('Jak funguje fotopast?', 'Pohybové čidlo spustí kameru, která zaznamená snímek nebo video na paměťovou kartu. Důležitá je rychlost spouště, dosah přísvitu a napájení. Dodržujte souhlas majitele pozemku.'),
         ('Jak obnovit impregnaci oblečení?', 'Oblečení vyperte bez aviváže, aplikujte impregnační prostředek určený pro membrány a případně teplem aktivujte vrstvu podle návodu. Obnovu proveďte, když voda přestane perlit po povrchu.'),
         ('Jak se starat o lovecké boty?', 'Po použití je očistěte, vyjměte vložky a usušte při pokojové teplotě. Kůži ošetřete impregnací nebo vazelínou, gumové holínky opláchněte a ukládejte mimo slunce.'),
         ('Hodí se vojenské oblečení na lov?', 'Může se hodit pro odolnost a kapsy, ale vzory a barvy nemusí odpovídat prostředí a v některých případech je jejich použití omezené. Zkontrolujte pravidla honitby a hlavně pohodlnost střihu.'),
         ('Co s sebou na dlouhé čekání?', 'Sedák nebo podložku, termosku, rezervní vrstvu, čelovku s červeným světlem, dalekohled a nabitý telefon. Pomůže i malé občerstvení a teplé rukavice.')])

NEW['stany']['faq'] += [
    ('Jak se zbavit kondenzace uvnitř stanu?', 'Větrejte průduchy a pootevřeným vchodem, nenoste dovnitř mokré oblečení a stavte stan tak, aby plachta nedosedala na vnitřní stan. Ráno vlhkost setřete a stan před sbalením nechte oschnout.'),
    ('Kolik váží stan na túru a co všechno se do hmotnosti počítá?', 'Výrobci často uvádějí minimální hmotnost jen kostry a stanu bez kolíků a obalu. Proto porovnávejte údaj o balení včetně všech částí, protože právě tato hodnota se opravdu nosí v batohu.'),
    ('Jak dlouho stan vydrží?', 'Záleží na četnosti používání, UV záření, uložení a péči. Impregnace a těsnění švů se s časem opotřebují a lze je obnovit, látka vystavená slunci ale slábne postupně a nevrátí se.'),
]
NEW['cyklo-brzdy']['faq'] += [
    ('Jak často se mají kontrolovat brzdy?', 'Stav destiček, kotoučů a lanek je dobré zkontrolovat před každou sezónou a po dlouhých túrách v deštivém počasí či blátě. Rychlá kontrola páky a obložení před jízdou nikdy neuškodí.'),
    ('Proč se páka brzdy propadá k řídítkům?', 'Obvykle je příčinou vzduch v hydraulice nebo opotřebované destičky. U lanových brzd se prodlouží lanko a je třeba ho dopnout. Pokud páka klesá náhle, kolo nepoužívejte a nechte brzdu zkontrolovat.'),
    ('Mohu používat destičky jiné značky než brzdu?', 'Ano, pokud mají shodný tvar a označení kompatibility s vaším třmenem. Nejlépe porovnejte číslo modelu a obrázek tvaru, protože stejná značka brzdy má více různých řad destiček.'),
]
NEW['lov-a-priroda']['faq'] += [
    ('Jak vybrat velikost lovecké bundy?', 'Počítejte s vrstvami pod ní, tedy raději o půl velikosti větší, aby se při pohybu nic nenapínalo. Zkontrolujte délku rukávů při natažených rukou a délku kolem pasu při sezení.'),
    ('Čím se liší tichá membrána od běžné?', 'Tichá membrána je laminovaná s měkkou látkou, která při pohybu nešustí. Běžná membrána na turistice bývá hlasitější. Pro lov a pozorování zvěře je proto vhodnější měkká a tlumená varianta.'),
    ('Kde najdu podobné oblečení pro každodenní outdoor?', 'Podívejte se do kategorií outdoorových kalhot, softshellových bund a trailových bot, které se hodí pro delší pobyt venku bez ohledu na lov. Rozdíl bývá hlavně v barvách a tichosti látky.'),
]
