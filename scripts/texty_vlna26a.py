"""sporteka.cz — wave 26a (16. 11. 2026): long texts for vitamin-d, vitamin-c, zinek, glutamin.
General true facts only, health claims only in the wording of authorised EU claims, no prices, no dosing advice.
Only brand with an indexed page (znacky.json): gymbeam; other brands are named without a link."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ vitamin-d
NEW['vitamin-d'] = dict(long=True,
    title='Vitamín D3: formy, dávka v IU a µg, D3+K2, kapky',
    desc='Vitamín D a D3 v kapslích, tabletách i kapkách. Jak číst IU a µg, čím se liší D3 od D2, kdy dává smysl D3+K2, a porovnat nabídky českých obchodů.',
    intro='<p>Vitamín D si tělo umí vyrobit samo, ale jen když kůži zasáhne dost slunečního záření. V českých zemích se to mezi říjnem a březnem děje jen omezeně: slunce stojí nízko, dny jsou krátké a většinu času trávíme uvnitř. Právě proto patří vitamín D k doplňkům, které si lidé v chladné polovině roku kupují nejčastěji. Variant je ale na trhu tolik, že se v nich snadno ztratíte.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů, nakupujete ale vždy přímo v e-shopu, který si vyberete. V kategorii najdete kapsle, tablety, žvýkací formy pro děti, kapky v oleji i kombinace s vitamínem K2, hořčíkem nebo vápníkem. Zastoupené jsou značky jako ' + B(('gymbeam', 'GymBeam')) + ', Amix, Nutrend, Terezia, Viridian, Vitar, Complex nebo Czech Virus. Příbuzné doplňky hledejte v kategoriích <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>, <a href="/horcik/">hořčík</a> a <a href="/omega-3/">omega-3</a>.</p>',
    guide='<h2>K čemu vitamín D slouží</h2>'
          '<p>Vitamín D patří mezi vitamíny rozpustné v tucích. Podle schválených tvrzení Evropského úřadu pro bezpečnost potravin přispívá k udržení normálního stavu kostí a zubů, k normální funkci svalů a k normální funkci imunitního systému. Přispívá také k normálnímu vstřebávání a využití vápníku a fosforu a k udržení normální hladiny vápníku v krvi. Doplněk stravy nenahrazuje pestrou stravu a nic z toho neslibuje, že vám konkrétní tableta pomůže. Tvrzení jen popisují roli, kterou vitamín D v těle plní.</p>'
          '<p>Z potravy ho získáte jen málo. Obsahují ho mastné ryby, vaječný žloutek a některé obohacené potraviny, běžný jídelníček ale potřebu obvykle nepokryje. Hlavním zdrojem tak zůstává slunce – a to je od podzimu do jara slabé.</p>'
          '<h2>Proč se o něm mluví hlavně v zimě</h2>'
          '<p>Vitamín D vzniká v kůži působením UVB záření. Toho je v našich zeměpisných šířkách mezi říjnem a březnem málo, protože slunce nevystoupá dost vysoko nad obzor. Připočtěte práci v kanceláři, oblečení zakrývající většinu těla a opalovací krémy, které UVB zachycují. Mnoho lidí proto prožije zimní měsíce s nízkou zásobou. Kdo si chce vitamín D doplňovat, řeší to obvykle právě na podzim, a tehdy také zájem o tuto kategorii roste.</p>'
          '<p>Kolik vitamínu D potřebujete a zda ho vůbec doplňovat, je individuální. Těhotné a kojící ženy, děti, senioři a lidé, kteří užívají léky nebo mají zdravotní potíže, by se měli poradit s lékařem nebo lékárníkem. Hladinu v krvi umí zjistit jen laboratorní vyšetření.</p>'
          '<h2>D3 a D2: co je na obalu</h2>'
          '<p>Vitamín D se v doplňcích vyskytuje ve dvou podobách. Cholekalciferol, tedy vitamín D3, vzniká v kůži člověka a v doplňcích se získává nejčastěji z lanolinu z ovčí vlny. Existuje i rostlinná varianta D3 z lišejníků, kterou ocení vegani. Ergokalciferol, tedy vitamín D2, se vyrábí z kvasinek nebo hub. Obchody s doplňky stravy dnes prodávají převážně D3; ve složení ho poznáte podle slova „cholekalciferol“.</p>'
          + T(['Označení', 'Co to je', 'Poznámka'], [
              ['Vitamín D3 (cholekalciferol)', 'forma, kterou tvoří lidská kůže', 'nejběžnější v doplňcích, existuje i veganská z lišejníků'],
              ['Vitamín D2 (ergokalciferol)', 'rostlinná forma z hub nebo kvasinek', 'v nabídce méně častá'],
              ['D3 + K2', 'kombinace s menachinonem, často MK-7', 'dvě složky v jedné kapsli'],
              ['D3 s hořčíkem nebo vápníkem', 'kombinovaný přípravek', 'zkontrolujte množství každé složky zvlášť'],
              ['Kapky v oleji', 'D3 rozpuštěné v oleji', 'snadné dávkování po kapkách'],
              ['Liposomální', 'D3 zabalené v lipidových váčcích', 'výrobci slibují lepší vstřebání, rozhodující je dávka na porci'],
              ['Žvýkací tablety a gumoví medvídci', 'chutnější formy pro děti i dospělé', 'bývají v nich sladidla a aroma']]) +
          '<h2>IU, nebo µg? Jak přepočítat jednotky</h2>'
          '<p>Na českých obalech se setkáte se dvěma jednotkami: s mezinárodními jednotkami (zkratka IU nebo m. j.) a s mikrogramy (µg nebo mcg). Platí jednoduchý převod: 1 µg vitamínu D odpovídá 40 IU. 1000 IU je tedy 25 µg, 2000 IU odpovídá 50 µg. Evropská referenční hodnota příjmu, kterou obaly uvádějí v procentech, je 5 µg, což je 200 IU. Vysoká čísla na obalech proto nejsou překlep, jen jiná jednotka. Při porovnávání dvou výrobků se vždy ujistěte, že srovnáváte údaje ve stejné jednotce.</p>'
          '<p>Hodnotu si vždy přepočítejte na jednu porci. U některých kapek je množství uvedeno na jednu kapku, u jiných na dávkovač nebo na mililitr; u kapslí záleží na tom, zda se užívá jedna, nebo dvě denně. Řiďte se doporučeným dávkováním na obalu a nepřekračujte ho. Vitamín D se ukládá v tukové tkáni, takže se při dlouhodobém předávkování může v těle hromadit.</p>'
          '<h2>Vitamín D3 s K2: kdy to dává smysl</h2>'
          '<p>Vitamín K2, nejčastěji ve formě menachinonu MK-7, se k vitamínu D často přidává do jedné kapsle. Vitamín K přispívá k udržení normálního stavu kostí a k normálnímu srážení krve. Právě kvůli druhému tvrzení musí lidé, kteří užívají léky na ředění krve, užívání vitamínu K vždy probrat s lékařem. Kombinovaný doplněk ocení ten, kdo chce vitamín D i K2 a nechce polykat dvě tobolky. Pokud vás zajímá jen vitamín D, kombinace není nutná. Sledujte, kolik K2 přípravek obsahuje a zda je množství uvedeno v mikrogramech.</p>'
          '<h2>Jak číst složení</h2>'
          '<ul><li><strong>Forma:</strong> cholekalciferol znamená D3, ergokalciferol D2.</li>'
          '<li><strong>Množství na porci:</strong> sledujte, kolik kapslí, tablet nebo kapek tvoří jednu porci.</li>'
          '<li><strong>Počet dávek v balení:</strong> pokud se denně užívají dvě tobolky, 90 kapslí neznamená 90 dávek.</li>'
          '<li><strong>Nosný olej:</strong> vitamín D je rozpustný v tucích, proto ho většina výrobců rozpouští v oleji, třeba olivovém nebo MCT.</li>'
          '<li><strong>Doplňkové látky:</strong> u tablet bývá ztužidlo, u gumových medvídků cukr nebo sladidlo, u kapslí obal ze želatiny nebo celulózy.</li>'
          '<li><strong>Certifikace a původ:</strong> uvedený výrobce, šarže a země výroby svědčí o transparentní značce.</li></ul>'
          '<h2>Kapky, kapsle, tablety nebo žvýkačky</h2>'
          '<p>Výhodou kapek je jemné dávkování: hodí se pro děti od narození, pro seniory a pro všechny, kdo nechtějí polykat tobolky. U dětských kapek bývá obsah uveden na mililitr a obvykle i na jednu kapku. Kapsle se hodí na cesty a mají neutrální chuť. Tablety bývají nejlevnější na jednu dávku, ale obsahují pojiva. Žvýkací varianty jsou pohodlné pro děti, které odmítají tobolky, jen si zkontrolujte množství cukru. Dětem dávejte vitamín D pouze v dávce, kterou doporučil pediatr nebo výrobce na obalu pro daný věk.</p>'
          '<h2>Kdy vitamín D užívat</h2>'
          '<p>Protože je rozpustný v tucích, doporučuje se užívat ho společně s jídlem, které tuk obsahuje. Na hodině nezáleží, důležitější je pravidelnost. Mnoha lidem pomáhá brát kapsli vždy ke snídani nebo k obědu. Doplněk nenahrazuje pobyt venku a pestrou stravu.</p>'
          '<h2>Vitamín D a sport</h2>'
          '<p>Sportovce vitamín D zajímá proto, že s ním v pozadí počítají svaly i kosti. Vitamín D přispívá k normální funkci svalů a k udržení normálního stavu kostí a zubů. Pokud trénujete většinu roku v hale, v posilovně nebo na běžeckém pásu, vystavujete se slunci méně než ti, kdo trénují venku. Doplněk je tak spíš pojistka za chybějící slunce než sportovní výživa. Další doplňky pro sportovce najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>; vitamín D mezi nimi nepodceňujte, ale ani nepřeceňujte.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Porovnávání IU s µg bez přepočtu.</li>'
          '<li>Výběr podle nejvyšší dávky místo podle toho, co na obalu doporučuje výrobce.</li>'
          '<li>Spoléhání na to, že kombinace s hořčíkem a vápníkem pokryje vše, bez kontroly množství jednotlivých složek.</li>'
          '<li>Přehlédnutí, že přípravky pro děti a pro dospělé mají jiné dávkování.</li>'
          '<li>Dlouhodobé užívání vysokých dávek bez konzultace s lékařem.</li></ul>'
          '<h2>Jak nakupovat v nabídce Sporteky</h2>'
          '<p>Na kartě produktu uvidíte nabídky více českých e-shopů a můžete porovnat balení, dopravu a dostupnost. U doplňků stravy sledujte také datum minimální trvanlivosti, protože sezónní zboží se někdy prodává ze starších zásob. Zkontrolujte, zda je výrobek skutečně doplněk stravy s českým popisem. Má-li výrobek dlouhou trvanlivost, vyplatí se větší balení – ovšem jen tehdy, když ho stihnete včas spotřebovat.</p>'
          '<p>Chcete-li doplnit i další látky, začněte v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>. Z podzimních doplňků se nabízí ještě <a href="/vitamin-c/">vitamín C</a> a <a href="/zinek/">zinek</a>, které mají jiné funkce a <a href="/horcik/">hořčík</a>, který přispívá k normální činnosti svalů a ke snížení míry únavy a vyčerpání.</p>',
    faq=[
        ('Jaký je rozdíl mezi vitamínem D3 a D2?', 'D3 (cholekalciferol) je forma, kterou tvoří lidská kůže, a v doplňcích stravy je nejběžnější. D2 (ergokalciferol) je rostlinného původu z hub nebo kvasinek. V nabídce obchodů převažuje D3, existuje i veganská varianta z lišejníků.'),
        ('Kolik µg je 1000 IU vitamínu D?', 'Platí převod 1 µg = 40 IU, takže 1000 IU odpovídá 25 µg. Evropská referenční hodnota příjmu na obalech je 5 µg, tedy 200 IU.'),
        ('Proč se vitamín D užívá hlavně na podzim a v zimě?', 'Tělo ho tvoří v kůži působením UVB záření. V Česku ho mezi říjnem a březnem vzniká málo, protože slunce stojí nízko a víc času trávíme uvnitř. Zda ho vůbec doplňovat, je dobré probrat s lékařem nebo lékárníkem.'),
        ('Je lepší vitamín D v kapkách, nebo v kapslích?', 'Záleží na pohodlí. Kapky se hodí pro děti a pro ty, kdo nechtějí polykat tobolky, kapsle jsou praktické a mají jednotné dávkování. Důležitější než forma je obsah D3 na jednu porci a pravidelnost.'),
        ('Má smysl kombinace D3 s K2?', 'Vitamín K přispívá k udržení normálního stavu kostí a k normálnímu srážení krve. Kombinace se hodí, pokud chcete obě složky v jedné kapsli. Kdo užívá léky ovlivňující srážlivost krve, musí se předem poradit s lékařem.'),
        ('Kdy a s čím vitamín D užívat?', 'Je rozpustný v tucích, proto se obvykle užívá s jídlem, které tuk obsahuje. Na hodině nezáleží, důležitější je pravidelnost a dodržení dávkování na obalu.'),
        ('Mohu se vitamínem D předávkovat?', 'Ano, vitamín D se ukládá v těle, a proto nepřekračujte doporučené dávkování na obalu. Těhotné a kojící ženy, děti a lidé užívající léky by se měli před užíváním poradit s lékařem nebo lékárníkem.'),
        ('Je vitamín D3 vhodný pro vegany?', 'Klasický D3 se vyrábí z lanolinu z ovčí vlny, takže veganský není. Na trhu je veganská varianta z lišejníků, kterou poznáte podle označení na obalu.'),
        ('Je vitamín D dobrý pro sportovce?', 'Vitamín D přispívá k normální funkci svalů a k udržení normálního stavu kostí. Smysl má hlavně pro ty, kdo trénují uvnitř a na slunce se dostanou méně. Nenahrazuje pestrou stravu ani trénink.'),
    ])

# ------------------------------------------------------------------ vitamin-c
NEW['vitamin-c'] = dict(long=True,
    title='Vitamín C: formy, šípky, liposomální, kapsle a tablety',
    desc='Vitamín C v tabletách, kapslích, liposomální i se šípky a acerolou. Jak číst složení, porovnat formy a množství a najít nabídky českých obchodů.',
    intro='<p>Vitamín C neboli kyselina askorbová patří k nejznámějším vitamínům a zároveň k nejčastěji kupovaným doplňkům. Je rozpustný ve vodě, tělo si ho nedokáže vyrobit ani dlouhodobě ukládat, a proto ho musíme přijímat potravou. V jídelníčku ho dodává hlavně ovoce a zelenina, zejména paprika, citrusy, černý rybíz a kysané zelí; část lidí si ho ale doplňuje i tabletami.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů, nákup dokončíte přímo v e-shopu, který si vyberete. V kategorii najdete čistý vitamín C, přípravky se šípky, rakytníkem nebo acerolou, liposomální formy, žvýkací tablety, kapsle s postupným uvolňováním i kombinace s echinaceou, zinkem a vitamínem D. Prodávají je značky jako ' + B(('gymbeam', 'GymBeam')) + ', Nutrend, Amix, MaxxWin, Movit Energy, MedPharma, Vitar nebo Terezia. Další doplňky najdete v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>',
    guide='<h2>Co vitamín C dělá</h2>'
          '<p>Schválených tvrzení EU má vitamín C poměrně hodně. Vitamín C přispívá k normální funkci imunitního systému, ke snížení míry únavy a vyčerpání a k normálnímu energetickému metabolismu. Přispívá také k normální tvorbě kolagenu pro normální funkci cév, kostí, chrupavek, dásní, kůže a zubů a k ochraně buněk před oxidativním stresem. Zvyšuje rovněž vstřebávání železa. Nic z toho neznamená, že vás tableta ochrání před nachlazením. Tvrzení popisují roli, kterou vitamín C v těle hraje, a platí při příjmu v souladu s doporučením.</p>'
          '<h2>Formy vitamínu C v doplňcích</h2>'
          '<p>Základní látkou je kyselina askorbová. Kromě ní se používají její soli, tedy askorbáty, které jsou šetrnější k žaludku. Přírodní zdroje jako šípky, acerola, rakytník nebo černý rybíz se do přípravků přidávají jako extrakty a jejich podíl na celkovém množství vitamínu C bývá různý. Přírodní zdroj přitom není automaticky lepší, jen rostlina obsahuje i další látky, například flavonoidy.</p>'
          + T(['Forma', 'Co to je', 'Poznámka'], [
              ['Kyselina askorbová', 'základní, nejběžnější forma', 'kyselá, citlivějším žaludkům může vadit'],
              ['Askorbát sodný nebo vápenatý', 'pufrovaná sůl kyseliny', 'jemnější k žaludku, pozor na sodík u sodné soli'],
              ['Se šípky', 'kombinace s extraktem ze šípků', 'část vitamínu C pochází z rostliny'],
              ['Acerola', 'přírodní extrakt z jihoamerické třešně', 'zdroj vitamínu C v rostlinné podobě'],
              ['Liposomální', 'vitamín C v lipidových váčcích', 'výrobci uvádějí šetrnost k žaludku, porovnejte množství na porci'],
              ['S postupným uvolňováním', 'tableta nebo kapsle uvolňuje látku po delší dobu', 'hodí se, pokud nechcete jednorázovou velkou dávku'],
              ['Žvýkací a na cucání', 'chutnější forma, často pro děti', 'obsahuje cukr nebo sladidlo'],
              ['Kombinace', 's echinaceou, zinkem, vitamínem D nebo železem', 'zkontrolujte množství každé složky']]) +
          '<h2>Kapsle, tablety, prášek nebo kapky</h2>'
          '<p>Tablety bývají nejlevnější na jednu porci, ale obsahují pojiva a protispékavé látky. Kapsle jsou pohodlné a mají neutrální chuť. Prášek se rozpouští v nápoji a hodí se, pokud chcete množství přesně upravit, ale je kyselý a zbytek balení musíte chránit před vlhkem. Žvýkací varianty a tablety na cucání jsou u dětí oblíbené, ale často obsahují cukr. Liposomální přípravky se prodávají jako kapsle nebo jako tekutina v sáčku.</p>'
          '<h2>Liposomální vitamín C: co od něj čekat</h2>'
          '<p>Liposomální technologie uzavírá vitamín C do drobných váčků z fosfolipidů, nejčastěji ze slunečnicového nebo sójového lecitinu. Výrobci tvrdí, že je tak šetrnější k žaludku a lépe se vstřebává. Jak velký je rozdíl oproti běžné formě u zdravého člověka, na tom se odborníci neshodnují. Při porovnávání se proto nedívejte jen na označení „liposomální“, ale na množství vitamínu C v jedné porci a na to, kolik porcí balení obsahuje. U kapslí se navíc vyplatí přepočítat, kolik jich na jednu porci potřebujete.</p>'
          '<h2>Jak číst složení</h2>'
          '<ul><li><strong>Množství na porci:</strong> uvedené v miligramech, často i jako procento referenční hodnoty příjmu.</li>'
          '<li><strong>Zdroj vitamínu C:</strong> kyselina askorbová, askorbát, extrakt ze šípků nebo aceroly. U extraktů hledejte údaj, kolik vitamínu C v nich skutečně je.</li>'
          '<li><strong>Počet porcí v balení:</strong> přepočtěte, kolik tablet nebo kapslí tvoří jednu porci.</li>'
          '<li><strong>Doplňkové látky:</strong> sladidla, barviva, aroma a protispékavé látky, zejména u žvýkacích forem.</li>'
          '<li><strong>Alergeny:</strong> sója u lecitinu, případně lepek či mléko u některých směsí.</li></ul>'
          '<h2>Kolik je dost a kdy dát pozor</h2>'
          '<p>Vitamín C se vylučuje močí, takže jeho nadbytek tělo většinou rychle odvádí. Vyšší množství ale může způsobit zažívací potíže, nadýmání nebo průjem. U citlivějších lidí se může objevit pálení žáhy, protože kyselina askorbová je kyselá. Řiďte se doporučeným dávkováním na obalu a nepřekračujte ho. Těhotné a kojící ženy, děti, lidé s ledvinovými kameny nebo poruchami metabolismu železa a ti, kdo užívají léky, by se měli předem poradit s lékařem nebo lékárníkem.</p>'
          '<h2>Vitamín C ve sportu</h2>'
          '<p>Vitamín C přispívá k normální funkci imunitního systému a ke snížení míry únavy a vyčerpání. Sportovci proto po doplňku sahají, když hodně trénují nebo když jedí málo čerstvé zeleniny. Vitamín C ale dobře dodají i potraviny, například paprika, brokolice, kiwi nebo bobuloviny, které se do jídelníčku snadno zařadí. Doplněk je pojistka, nikoli náhrada. Širší přehled najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>, doplnit si můžete i <a href="/horcik/">hořčík</a> a <a href="/omega-3/">omega-3</a>.</p>'
          '<h2>Vitamín C a železo</h2>'
          '<p>Vitamín C zvyšuje vstřebávání železa z potravy, což je schválené tvrzení. Proto vznikají kombinované přípravky se železem a vitamínem C. Železo užívejte jen po dohodě s lékařem, protože jeho nadbytek je stejně nežádoucí jako nedostatek. Kombinovaný přípravek není vhodný pro každého a neměl by to být nahodilý nákup.</p>'
          '<h2>Přípravky s echinaceou, zinkem a vitamínem D</h2>'
          '<p>Na podzim se v nabídce objevují kombinace vitamínu C s echinaceou, zinkem nebo vitamínem D. Výhodou je pohodlí, nevýhodou menší kontrola nad jednotlivými složkami. Zkontrolujte, kolik které látky tableta obsahuje, a porovnejte to s doporučeným příjmem. Pokud vám jde jen o jednu složku, bývá výhodnější samostatný doplněk, například <a href="/zinek/">zinek</a> nebo <a href="/vitamin-d/">vitamín D3</a>.</p>'
          '<h2>Vitamín C v jídelníčku</h2>'
          '<p>Než sáhnete po doplňku, stojí za to podívat se, kolik vitamínu C dostáváte z jídla. Hodně ho obsahuje čerstvá paprika, petržel, brokolice, zelí, kiwi, citrusové plody, jahody a černý rybíz. Nejvíc ho ubývá při dlouhém vaření a skladování, protože je citlivý na teplo, světlo a vzdušný kyslík. Syrová zelenina a ovoce jsou proto lepší volbou než dlouho vařená jídla. Kdo jí denně několik porcí zeleniny a ovoce, běžně přijímá dost. Doplněk se hodí hlavně tehdy, když je jídelníček jednotvárný, v období zvýšené zátěže nebo když chcete mít jistotu.</p>'
          '<h2>Vitamín C a kouření, stres a trénink</h2>'
          '<p>Kuřáci mají obecně nižší hladiny vitamínu C v krvi a odborná doporučení pro ně počítají s vyšším příjmem než pro nekuřáky. Tvrdý trénink a dlouhodobý stres zvyšují potřebu živin celkově, ale není to důvod k velkým dávkám. Rozumnější je zaměřit se na pestrost jídelníčku, dostatek spánku a regeneraci. Vitamín C podle schváleného tvrzení přispívá k ochraně buněk před oxidativním stresem; víc očekávání než to, co tvrzení skutečně říká, do něj ale nevkládejte.</p>'
          '<h2>Alergie a snášenlivost</h2>'
          '<p>Čistá kyselina askorbová je pro většinu lidí bezproblémová. Citlivější žaludek ale někdy reaguje na vyšší porce nebo na užití nalačno. V takovém případě se vyplatí zkusit pufrovaný askorbát nebo přípravek s postupným uvolňováním. U kombinovaných přípravků kontrolujte alergeny, hlavně sóju v lecitinu a případné rostlinné extrakty. Echinacea patří mezi hvězdnicovité rostliny a lidé alergičtí na pyl těchto rostlin ji nemusí snášet. Při pochybnostech se zeptejte lékárníka.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Výběr podle hmotnosti balení místo podle množství na porci.</li>'
          '<li>Očekávání, že přírodní extrakt ze šípků dodá vitamín C ve stejném množství jako čistá kyselina askorbová.</li>'
          '<li>Podcenění množství cukru ve žvýkacích tabletách a tabletách na cucání.</li>'
          '<li>Nákup velkého balení, které nestihnete spotřebovat před koncem trvanlivosti.</li>'
          '<li>Souběžné užívání více přípravků, které všechny obsahují vitamín C.</li></ul>'
          '<h2>Jak nakupovat v nabídce Sporteky</h2>'
          '<p>Na kartě produktu porovnáte nabídky několika českých obchodů a zkontrolujete dopravu a dostupnost. U vitamínu C se vyplatí sledovat datum minimální trvanlivosti: je to látka citlivá na světlo, teplo a vlhkost, takže vždy zvolte dobře uzavřené balení. Doma ho skladujte v suchu, ne na okenním parapetu ani v koupelně. Na obalu hledejte jednoznačné označení „doplněk stravy“ a české označení výrobce nebo distributora.</p>',
    faq=[
        ('Jaký vitamín C je nejlepší: kyselina askorbová, askorbát, nebo ze šípků?', 'Žádná forma není automaticky nejlepší. Kyselina askorbová je nejběžnější, askorbát je šetrnější k žaludku a šípky nebo acerola přidávají rostlinný zdroj. Rozhoduje obsah vitamínu C na porci a snášenlivost.'),
        ('Je liposomální vitamín C lepší než obyčejný?', 'Výrobci uvádějí šetrnost k žaludku a lepší vstřebávání, ale rozdíl u zdravého člověka není jednoznačný. Srovnávejte hlavně množství vitamínu C na porci a počet porcí v balení.'),
        ('Mohu užívat vitamín C na prázdný žaludek?', 'Kyselina askorbová je kyselá, a proto může u citlivějších lidí způsobit pálení žáhy. Pomůže užít ji s jídlem nebo zvolit pufrovanou formu, tedy askorbát.'),
        ('Je možné se vitamínem C předávkovat?', 'Přebytek se vylučuje močí, ale vyšší množství může způsobit zažívací potíže nebo průjem. Řiďte se doporučeným dávkováním na obalu. Těhotné a kojící ženy, děti a lidé užívající léky by se měli poradit s lékařem nebo lékárníkem.'),
        ('K čemu vitamín C přispívá?', 'Podle schválených tvrzení EU přispívá k normální funkci imunitního systému, ke snížení míry únavy a vyčerpání, k normální tvorbě kolagenu a k ochraně buněk před oxidativním stresem. Zvyšuje také vstřebávání železa.'),
        ('Jak poznám, kolik vitamínu C je v přípravku se šípky?', 'Na obalu hledejte údaj o množství vitamínu C na porci v miligramech. Extrakt ze šípků může být jen malou částí celkového množství, zbytek tvoří přidaná kyselina askorbová.'),
        ('Jak vitamín C skladovat?', 'Na suchém a tmavém místě, v dobře uzavřeném obalu, mimo teplo a vlhkost. Vitamín C je citlivý na světlo a vzdušný kyslík.'),
        ('Hodí se žvýkací vitamín C pro děti?', 'Je to oblíbená forma, ale často obsahuje cukr nebo sladidla. U dětí dodržujte dávkování určené výrobcem pro příslušný věk a v případě pochybností se poraďte s pediatrem.'),
    ])

# ------------------------------------------------------------------ zinek
NEW['zinek'] = dict(long=True,
    title='Zinek: bisglycinát, glukonát, chelát, citrát a další formy',
    desc='Zinek v tabletách a kapslích: bisglycinát, glukonát, citrát, pikolinát i liposomální. Jak číst obsah zinku a vybrat formu, a porovnat české obchody.',
    intro='<p>Zinek je minerál, který tělo potřebuje jen ve stopovém množství, zato pro celou řadu procesů. Nemá pro něj zásobárnu, ze které by mohlo pravidelně čerpat, takže ho musí dostávat z potravy: z masa, vnitřností, mořských plodů, vajec, luštěnin, ořechů, semínek a celozrnných obilovin. Lidem, kteří jedí méně živočišných potravin, a sportovcům, kteří zinek ztrácejí potem, se vyplatí vědět, jakou formu doplňku vybrat.</p>'
          '<p>Nabídky českých obchodů za vás srovná Sporteka, nakupujete pak přímo v e-shopu, který si zvolíte. V kategorii najdete samostatné přípravky se zinkem ve formě glukonátu, bisglycinátu, citrátu, pikolinátu nebo síranu, liposomální varianty i kombinace se selenem, biotinem, vápníkem, hořčíkem a vitamínem C. Nabízejí je značky jako ' + B(('gymbeam', 'GymBeam')) + ', MedPharma, Amix, Nupreme, Trec Nutrition, Extrifit, Weider, Nutricius nebo Viridian. Další minerály včetně <a href="/horcik/">hořčíku</a> najdete v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>',
    guide='<h2>K čemu zinek v těle slouží</h2>'
          '<p>Zinek patří mezi minerály s nejvíce schválenými tvrzeními. Přispívá k normální funkci imunitního systému, k normální syntéze DNA a bílkovin, k normální funkci buněčného dělení a k ochraně buněk před oxidativním stresem. Přispívá také k udržení normálního stavu vlasů, nehtů a pokožky, k udržení normální hladiny testosteronu v krvi, k normální plodnosti a tvorbě spermií, k normálnímu zraku a k normální kognitivní funkci. Je to souhrn funkcí, které zinek v organismu plní, nikoli příslib výsledku z jedné tablety.</p>'
          '<h2>Formy zinku v doplňcích</h2>'
          '<p>Zinek se v doplňcích nikdy neprodává čistý. Je vázaný na další látku a ta se uvádí v názvu: glukonát, citrát, pikolinát, oxid, síran nebo bisglycinát. Rozhodující je, kolik samotného zinku jedna porce obsahuje. Mnoho výrobců proto uvádí zvlášť hmotnost soli a zvlášť množství elementárního zinku. Pro srovnání hledejte vždy údaj „zinek“ v miligramech, nikoli „glukonát zinečnatý“.</p>'
          + T(['Forma', 'Co to je', 'Poznámka'], [
              ['Glukonát zinečnatý', 'sůl kyseliny glukonové', 'běžná, osvědčená forma ve většině tablet'],
              ['Citrát zinečnatý', 'sůl kyseliny citronové', 'neutrální chuť, často v tabletách na cucání'],
              ['Pikolinát zinečnatý', 'vazba na kyselinu pikolinovou', 'v kapslích, výrobci uvádějí dobrou využitelnost'],
              ['Bisglycinát (chelát)', 'zinek vázaný na dvě molekuly glycinu', 'šetrný k žaludku, často v kapslích'],
              ['Oxid zinečnatý', 'anorganická sůl', 'levná a koncentrovaná, hůře se rozpouští'],
              ['Síran zinečnatý', 'anorganická sůl', 'běžná, může dráždit žaludek'],
              ['Liposomální', 'zinek v lipidových váčcích', 'výrobci uvádějí šetrnost, porovnejte množství na porci'],
              ['Kombinace', 'se selenem, vitamínem C, hořčíkem a vápníkem', 'zkontrolujte množství každé složky']]) +
          '<h2>Chelát a bisglycinát: co znamenají</h2>'
          '<p>Slovo chelát označuje vazbu minerálu na organickou molekulu, nejčastěji aminokyselinu. Bisglycinát zinečnatý má zinek navázaný na dvě molekuly glycinu. Výrobci o něm říkají, že se dobře snáší a že se v těle využívá lépe než oxid. Jak velký je rozdíl mezi formami, se v literatuře liší podle studie a podmínek, takže marketingové údaje berte s rezervou. Při citlivém žaludku stojí chelát za vyzkoušení, ale nic nezaručuje.</p>'
          '<h2>Jak číst složení</h2>'
          '<ul><li><strong>Množství zinku na porci:</strong> v miligramech, často s procentem referenční hodnoty příjmu.</li>'
          '<li><strong>Forma:</strong> glukonát, citrát, bisglycinát nebo jiná. U každé z nich přepočítejte obsah čistého zinku.</li>'
          '<li><strong>Počet porcí v balení:</strong> jedna porce může být jedna tableta, ale i dvě kapsle, takže balení se stejným počtem kusů nemusí mít stejný počet dávek.</li>'
          '<li><strong>Další složky:</strong> selen, měď, vitamín C, vitamín B6 nebo extrakty, které se přidávají k zinku.</li>'
          '<li><strong>Doplňkové látky:</strong> sladidla, barviva a aroma u tablet na cucání, obal u kapslí.</li></ul>'
          '<h2>Kdy zinek užívat a na co si dát pozor</h2>'
          '<p>Zinek na prázdný žaludek někomu způsobuje nevolnost, proto ho mnoho lidí užívá s jídlem. Potraviny bohaté na vlákninu, fytáty a vápník mohou jeho vstřebávání mírně snížit. Dlouhodobý nadbytek zinku může narušit vstřebávání mědi, a proto je rozumné nepřekračovat dávku uvedenou na obalu. Pokud užíváte železo, vápník nebo léky, zeptejte se lékárníka na vhodný časový odstup. Těhotné a kojící ženy, děti a lidé s chronickým onemocněním by se měli před zahájením užívání poradit s lékařem.</p>'
          '<h2>Zinek ve sportu</h2>'
          '<p>Sportovci zinek často řeší, protože ho tělo ztrácí potem a náročný trénink zatěžuje imunitní systém, k jehož normální funkci zinek přispívá. Zároveň přispívá k normálnímu metabolismu makroživin a k udržení normální hladiny testosteronu v krvi. Zinek je proto součástí mnoha doplňků pro sportovce a také takzvaných ZMA směsí, tedy kombinace zinku, hořčíku a vitamínu B6. Doplněk nemá nahrazovat pestrý jídelníček, jen ho doplnit, když v něm chybí dost masa, luštěnin nebo semínek. Navazující doplňky najdete v kategoriích <a href="/sportovni-vyziva/">sportovní výživa</a> a <a href="/horcik/">hořčík</a>.</p>'
          '<h2>Zinek a vegetariáni</h2>'
          '<p>Rostlinné zdroje zinku, tedy luštěniny, ořechy, semínka a celozrnné obiloviny, obsahují také fytáty, které vstřebávání zinku omezují. Vegetariáni a vegani proto někdy potřebují o něco vyšší příjem než lidé, kteří jedí maso. Namáčení luštěnin, kvašení a klíčení fytáty částečně odbourává. Pokud zvažujete doplněk, zeptejte se lékaře nebo dietologa – posoudí, zda ho skutečně potřebujete.</p>'
          '<h2>Zinek v kombinaci s vitamínem C a vitamínem D</h2>'
          '<p>Na podzim a v zimě přibývá směsí, v nichž je zinek spolu s vitamínem C, echinaceou a vitamínem D. Hodí se pro ty, kdo chtějí jednu tabletu místo tří. Nevýhodou je, že množství jednotlivých složek je pevně dané. Pokud chcete množství zinku volit samostatně, zvolte jednosložkový přípravek a přidejte si <a href="/vitamin-c/">vitamín C</a> nebo <a href="/vitamin-d/">vitamín D3</a> zvlášť.</p>'
          '<h2>Zinek v jídelníčku</h2>'
          '<p>Nejvíc zinku obsahují ústřice, hovězí maso, vnitřnosti a vejce. Z rostlinných surovin ho najdete v dýňových semínkách, sezamu, luštěninách, ořeších a celozrnných výrobcích. Vstřebává se ale hůř než ze živočišných zdrojů. Pestrý jídelníček s masem, mléčnými výrobky a luštěninami běžnou potřebu obvykle pokryje. Doplněk dává smysl hlavně tehdy, když je jídelníček omezený nebo když ho doporučí lékař. Žádná tableta nenahradí rozmanitou stravu.</p>'
          '<h2>Jak rozumět procentům referenční hodnoty</h2>'
          '<p>Na obalech doplňků stravy najdete u zinku údaj v miligramech a vedle něj procento referenční hodnoty příjmu. Ta slouží jako orientační měřítko, nikoli jako doporučení. Číslo přes sto procent neznamená, že je přípravek lepší, často jen obsahuje víc, než je pro běžnou denní potřebu nutné. U zinku je rozumné držet se doporučeného dávkování, protože dlouhodobě vysoký příjem zinku může snižovat vstřebávání mědi. Sledujte proto zejména, zda neužíváte zinek ve dvou či třech přípravcích zároveň, třeba v multivitamínu, v kombinaci pro imunitu a v samostatné tabletě.</p>'
          '<h2>Zinek a další minerály</h2>'
          '<p>Zinek soupeří o vstřebávání s dalšími minerály, zejména s mědí, železem a vápníkem. Proto výrobci často přidávají malé množství mědi nebo používají chelátové formy. Pokud užíváte více minerálů, pomůže rozložit je během dne, například hořčík večer a zinek k obědu. Konkrétní rozvrh ale proberte s lékárníkem a řekněte mu i o lécích, které užíváte. Souvisejícím látkám se věnují kategorie <a href="/horcik/">hořčík</a> a <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Srovnávání hmotnosti soli místo obsahu čistého zinku.</li>'
          '<li>Souběžné užívání několika přípravků, které zinek obsahují všechny.</li>'
          '<li>Dlouhodobé užívání vysokých dávek bez porady s odborníkem.</li>'
          '<li>Očekávání, že zinek vyřeší problém s pokožkou, vlasy nebo nehty bez ohledu na ostatní faktory.</li>'
          '<li>Nákup tablet na cucání, které obsahují cukr nebo sladidla, když chcete jen minerál.</li></ul>'
          '<h2>Příznaky, které nepatří do e-shopu</h2>'
          '<p>Vypadávání vlasů, lámavé nehty, časté infekce nebo zhoršené hojení ran mohou mít celou řadu příčin a zinek je jen jednou z nich. Pokud tyto potíže trvají, domluvte si vyšetření u lékaře a nehádejte, jaký doplněk je potřeba. Laboratoř zjistí hladinu zinku v krvi a lékař posoudí, zda je doplněk na místě, v jaké formě a na jak dlouho. Doplňky stravy slouží k doplnění jídelníčku, ne k léčbě.</p>'
          '<h2>Jak zinek skladovat</h2>'
          '<p>Tablety a kapsle uchovávejte v původním uzavřeném obalu na suchém místě, mimo dosah dětí, ne v koupelně. Tablety na cucání se mohou na vlhku slepit a kapsle změknout. Po otevření dodržte dobu spotřeby, kterou výrobce uvádí na obalu.</p>'
          '<h2>Jak nakupovat v nabídce Sporteky</h2>'
          '<p>Na kartě produktu porovnáte nabídky několika českých e-shopů a hned vidíte dopravu i dostupnost. U zinku sledujte zejména přepočet na jednu porci a počet porcí v balení. Dvě balení se stejným počtem tablet mohou obsahovat odlišné množství zinku a různou formu. Doma ho skladujte v suchu a mimo dosah dětí. Pokud chcete doplnit víc látek najednou, začněte v kategorii <a href="/vitaminy-a-mineraly/">vitamíny a minerály</a>.</p>',
    faq=[
        ('Která forma zinku je nejlepší?', 'Žádná není absolutně nejlepší. Glukonát je běžná a osvědčená, bisglycinát (chelát) bývá šetrný k žaludku, oxid je koncentrovaný, ale hůř se rozpouští. Porovnávejte hlavně obsah čistého zinku na porci a to, jak vám forma sedí.'),
        ('Co znamená chelát nebo bisglycinát zinečnatý?', 'Je to zinek navázaný na dvě molekuly aminokyseliny glycinu. Výrobci uvádějí dobrou snášenlivost. Přesný rozdíl oproti jiným formám se ve studiích liší, proto berte marketingová tvrzení s rezervou.'),
        ('K čemu zinek přispívá?', 'Podle schválených tvrzení přispívá k normální funkci imunitního systému, k udržení normálního stavu vlasů, nehtů a pokožky, k normální syntéze DNA a bílkovin, k normálnímu zraku a k udržení normální hladiny testosteronu v krvi.'),
        ('Mohu užívat zinek na lačno?', 'Někomu způsobuje nevolnost, proto se obvykle užívá s jídlem. Vstřebávání může mírně snížit vláknina, fytáty a vápník, takže ho neužívejte s jídlem, které jich obsahuje hodně.'),
        ('Je možné se zinkem předávkovat?', 'Ano. Dlouhodobý nadbytek může narušit vstřebávání mědi. Řiďte se doporučeným dávkováním na obalu a nepřekračujte ho. Těhotné a kojící ženy, děti a lidé užívající léky by se měli poradit s lékařem nebo lékárníkem.'),
        ('Čím se liší zinek v tabletách na cucání od kapslí?', 'Tablety na cucání se rozpouštějí v ústech a často jsou doplněné příchutí, sladidlem nebo vitamínem C. Kapsle mají neutrální chuť a bývají bez cukru. Důležitý je obsah zinku na porci.'),
        ('Je zinek vhodný pro vegetariány a vegany?', 'Rostlinné zdroje zinku obsahují fytáty, které vstřebávání omezují. Vegetariáni a vegani proto zinek sledují pozorněji. Zda doplněk potřebujete, vám řekne lékař nebo dietolog.'),
        ('Co je ZMA?', 'Je to kombinace zinku, hořčíku a vitamínu B6, kterou sportovci často užívají večer. Rozhodujte podle složení a množství jednotlivých látek na porci, ne podle zkratky.'),
    ])

# ------------------------------------------------------------------ glutamin
NEW['glutamin'] = dict(long=True,
    title='Glutamin (L-glutamin): prášek, kapsle a jak číst složení',
    desc='L-glutamin v prášku, kapslích i tabletách. Co to je, jak ho sportovci používají, co o něm víme a jak porovnat nabídky českých obchodů.',
    intro='<p>Glutamin je aminokyselina, kterou si tělo vyrábí samo a která je zároveň nejhojnější volnou aminokyselinou v krvi i ve svalech. Najdete ho v mase, mléčných výrobcích, vejcích i v luštěninách, a proto zdravý člověk s pestrou stravou nedostatkem netrpí. Sportovci po něm přesto sahají už desítky let, hlavně proto, že od něj čekají podporu regenerace po tréninku.</p>'
          '<p>Hned na začátku je třeba říct, že glutamin nemá žádné schválené zdravotní tvrzení EU a důkazy o jeho vlivu na výkon nebo svalový růst u zdravých sportovců jsou omezené. Tato stránka popisuje, co to je a jak se používá, ne co vám zaručí. Sporteka srovnává nabídky českých e-shopů, nákup pak dokončíte přímo v tom, který si vyberete. Glutamin vyrábí například ' + B(('gymbeam', 'GymBeam')) + ', Nutrend, Amix, Reflex Nutrition, Prom-In, Scitec Nutrition, MyProtein, BioTech USA nebo MaxxWin. Najdete ho v kategorii <a href="/aminokyseliny-bcaa/">aminokyseliny a BCAA</a>, vedle níž stojí i <a href="/proteiny/">proteiny</a> a <a href="/kreatin/">kreatin</a>.</p>',
    guide='<h2>Co je glutamin</h2>'
          '<p>L-glutamin patří mezi proteinogenní aminokyseliny, tedy mezi stavební kameny bílkovin. Odborně se označuje jako podmíněně esenciální: zdravé tělo ho zvládne vyrobit, ale při velké zátěži, nemoci nebo úrazu se jeho spotřeba může zvýšit. Hojně ho využívají buňky střeva a imunitní buňky a ve svalech tvoří významnou část volných aminokyselin. V těle tedy hraje svou roli bez ohledu na to, zda nějaké doplňky užíváte.</p>'
          '<h2>Co o glutaminu víme a co ne</h2>'
          '<p>Glutamin se prodává jako doplněk pro regeneraci, ochranu svalů a podporu imunity při tvrdém tréninku. Řada těchto představ vychází z toho, že koncentrace glutaminu v krvi po velmi náročné zátěži klesá. Z toho ale automaticky neplyne, že její doplňování zlepší výkon nebo zrychlí růst svalů. Studie na zdravých sportovcích přinášejí smíšené výsledky a odborníci se k němu staví spíše zdrženlivě. Pro srovnání: u kreatinu je účinek dobře doložen, u glutaminu to neplatí.</p>'
          '<p>Poctivě je tedy třeba říct, že jde o doplněk, který si lidé kupují na základě osobní zkušenosti a který má jen doplňovat celkový jídelníček. Pokud máte omezený rozpočet, je rozumnější nejprve upravit příjem bílkovin, spánek a trénink. Glutamin je nadstavba, nikoli základ.</p>'
          '<h2>Formy glutaminu v nabídce</h2>'
          + T(['Forma', 'Popis', 'Poznámka'], [
              ['Prášek bez příchutě', 'čistý L-glutamin v prášku', 'nejběžnější, jedna složka a snadné porovnání'],
              ['Příchuť (ovoce, citron)', 'prášek s aromatem a sladidlem', 'chutnější, obsahuje další složky'],
              ['Kapsle', 'glutamin v tobolkách', 'pohodlné na cesty, méně látky na kus'],
              ['Tablety', 'lisovaný glutamin', 'levnější na jednu porci, obsahují pojiva'],
              ['Peptidy (glutamin peptidy)', 'glutamin vázaný v krátkých řetězcích', 'výrobci uvádějí lepší rozpustnost'],
              ['Fermentovaný', 'vyrobený fermentací', 'vyhledávaný vegany, zdroj je rostlinný'],
              ['Směs s BCAA nebo EAA', 'glutamin spolu s dalšími aminokyselinami', 'zkontrolujte poměr složek']]) +
          '<h2>Prášek, kapsle, nebo tablety</h2>'
          '<p>Nejvíc smyslu dává prášek: balení je levnější na jednu porci, množství si upravíte odměrkou a snadno ho zamícháte do vody, šejku nebo proteinového nápoje. Chuť čistého glutaminu je mírně nasládlá a neutrální. Rozpouští se pomaleji než jiné aminokyseliny, proto pomůže teplejší tekutina. Kapsle a tablety jsou pohodlné, ale na jednu porci jich potřebujete víc, protože obsah jedné kapsle je malý. Proto si ověřte, kolik kapslí tvoří doporučenou denní porci.</p>'
          '<h2>L-glutamin, peptidy a směsi</h2>'
          '<p>Na obalu hledejte označení „L-glutamin“, tedy přirozenou formu používanou v těle. Glutamin peptidy jsou krátké řetězce, v nichž je glutamin navázán na další aminokyseliny. Výrobci o nich říkají, že jsou stabilnější v roztoku a lépe se rozpouštějí. Rozdíl pro běžného sportovce je ale těžko měřitelný. Směsi s BCAA nebo EAA obsahují více látek najednou, což je pohodlné, ale množství samotného glutaminu v nich bývá nižší než v čistém přípravku. Porovnávejte vždy množství na porci, nikoli velikost balení.</p>'
          '<h2>Jak číst složení</h2>'
          '<ul><li><strong>Obsah glutaminu na porci:</strong> uvedený v gramech, u směsí zvlášť pro každou aminokyselinu.</li>'
          '<li><strong>Počet porcí v balení:</strong> hmotnost balení vydělená velikostí odměrky.</li>'
          '<li><strong>Doplňkové látky:</strong> sladidla, aroma, barviva a protispékavé látky u příchutí. U čistého prášku by měl být ve složení jen L-glutamin.</li>'
          '<li><strong>Původ:</strong> fermentovaný glutamin je rostlinného původu, což vítají vegani.</li>'
          '<li><strong>Testy kvality:</strong> výsledky kontroly na zakázané látky, pokud je výrobce zveřejňuje, ocení hlavně ti, kdo závodí.</li></ul>'
          '<h2>Jak sportovci glutamin používají</h2>'
          '<p>Nejčastěji se glutamin míchá do vody nebo do šejku po tréninku nebo před spaním. Jediné správné pravidlo pro to neexistuje, takže se řiďte doporučeným dávkováním na obalu a nepřekračujte ho. Kdo trénuje často a náročně, mívá doplněk v rutině spolu s <a href="/proteiny/">proteinem</a> nebo <a href="/kreatin/">kreatinem</a>. Na začátek zvolte menší balení a velké kupujte, až když víte, že vám doplněk vyhovuje.</p>'
          '<h2>Pro koho a kdy dát pozor</h2>'
          '<p>Glutamin je u zdravých dospělých obvykle dobře snášen. Při vyšších množstvích se mohou objevit zažívací potíže. Těhotné a kojící ženy, děti a lidé s onemocněním jater nebo ledvin, s poruchami nervové soustavy nebo ti, kdo užívají léky, by se měli před užíváním poradit s lékařem nebo lékárníkem. Lidé s onemocněním jater nebo ledvin by se měli poradit s lékařem vždy, protože jde o aminokyselinu, kterou tělo zpracovává právě těmito orgány.</p>'
          '<h2>Glutamin a jiné doplňky</h2>'
          '<p>Glutamin se často srovnává s BCAA nebo EAA a s kreatinem. BCAA tvoří tři větvené aminokyseliny, EAA všech devět esenciálních, zatímco glutamin není esenciální. Pokud jde o příjem bílkovin, bývá obvykle praktičtější kvalitní protein z mléka nebo rostlin. Glutamin je přitom součástí většiny bílkovin, takže ho dostanete i ze samotného proteinu. Přehled doplňků najdete v kategorii <a href="/sportovni-vyziva/">sportovní výživa</a>, kde si vyberete, co se k vašemu tréninku hodí nejvíc.</p>'
          '<h2>Glutamin v jídelníčku</h2>'
          '<p>Jako součást většiny bílkovin se glutamin vyskytuje v mase, rybách, vejcích, mléčných výrobcích, tofu, fazolích a dalších luštěninách. Při pestré stravě s dostatkem bílkovin tedy přijímáte několik gramů denně bez jakéhokoli doplňku. Právě proto se vyplatí nejdřív zkontrolovat celkový příjem bílkovin a teprve pak zvažovat samostatný přípravek. Pro mnoho lidí je účelnější <a href="/proteiny/">protein</a> než samostatná aminokyselina.</p>'
          '<h2>Glutamin a zažívání</h2>'
          '<p>Buňky tenkého střeva glutamin využívají jako zdroj energie, a proto se o něm hodně mluví i mimo sport. Pro zdravé lidi to ale neznamená, že doplněk něco zlepší. Zdravotní problémy se zažíváním patří k lékaři, ne do nákupního košíku s doplňky. Pokud vás trápí dlouhodobé potíže, nepokoušejte se je řešit aminokyselinami na vlastní pěst.</p>'
          '<h2>Dopingové a bezpečnostní hledisko</h2>'
          '<p>Čistý L-glutamin nepatří mezi zakázané látky, ale u doplňků stravy obecně platí, že nekvalitní výrobek může obsahovat nečistoty. Soutěžící sportovci by proto měli vybírat přípravky od výrobců, kteří uvádějí šarži, původ a nechávají výrobky testovat, a řídit se seznamy antidopingových organizací. Rekreačním sportovcům stačí vybrat známou značku s jasným složením a datem trvanlivosti.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Očekávání zázračných výsledků od doplňku, který nemá schválené zdravotní tvrzení.</li>'
          '<li>Srovnávání cen podle hmotnosti balení, ne podle obsahu glutaminu na porci.</li>'
          '<li>Koupě drahé směsi, kde je glutaminu málo.</li>'
          '<li>Zbytečný nákup velkého balení hned při prvním vyzkoušení.</li>'
          '<li>Zanedbávání bílkovin, spánku a regenerace ve prospěch doplňků.</li></ul>'
          '<h2>Kdy se bez glutaminu obejdete</h2>'
          '<p>Většina rekreačních cvičenců, kteří trénují třikrát týdně a jedí dost bílkovin, doplněk nepotřebuje. Peníze, které by šly na glutamin, bývají lépe využité na kvalitní jídlo, na protein, pokud ho v jídelníčku chybí, nebo na kreatin, jehož účinek je lépe doložen. Smysl může mít glutamin pro ty, kdo trénují velmi často, dodržují přísnou dietu s nízkým příjmem bílkovin nebo prostě chtějí vyzkoušet, zda jim doplněk sedí. I v takovém případě ho berte jako zkoušku, ne jako nezbytnost.</p>'
          '<h2>Jak ho zamíchat a skladovat</h2>'
          '<p>Prášek rozmíchejte ve vodě, šťávě nebo v proteinovém nápoji. Neochucený glutamin nemá výraznou chuť, takže ho můžete přimíchat i do jogurtu nebo ovesné kaše. Balení uchovávejte dobře uzavřené v suchu a nikdy do něj nesahejte mokrou odměrkou. Po otevření dodržujte dobu spotřeby uvedenou na obalu.</p>'
          '<h2>Jak nakupovat v nabídce Sporteky</h2>'
          '<p>Na kartě produktu porovnáte nabídky několika českých obchodů včetně dopravy a dostupnosti. U prášku sledujte datum minimální trvanlivosti a to, zda jde balení pevně uzavřít, protože vlhkem prášek hrudkovatí. Doma ho uchovávejte v suchu, mimo slunce a vždy se suchou odměrkou. Porovnávejte nejprve čisté L-glutaminy a teprve potom směsi s dalšími látkami, protože ve směsích se skutečné množství glutaminu snadno ztratí.</p>',
    faq=[
        ('Co je glutamin?', 'Je to aminokyselina, kterou si tělo vytváří samo a která tvoří významnou část volných aminokyselin ve svalech. Přijímáme ji i z jídla, třeba z masa, mléčných výrobků a vajec. V doplňcích se prodává jako L-glutamin.'),
        ('Pomáhá glutamin při růstu svalů?', 'Důkazy jsou omezené. Studie na zdravých sportovcích mají smíšené výsledky a pro glutamin neexistuje schválené zdravotní tvrzení EU. Základem zůstává dostatek bílkovin, trénink a spánek.'),
        ('Je lepší glutamin v prášku, nebo v kapslích?', 'Prášek bývá levnější na porci a snadno se dávkuje odměrkou. Kapsle jsou pohodlné, ale k jedné porci jich potřebujete víc. Porovnávejte množství glutaminu na porci.'),
        ('Co jsou glutamin peptidy?', 'Jsou to krátké řetězce aminokyselin obsahující glutamin. Výrobci uvádějí dobrou rozpustnost a stabilitu. Pro běžného sportovce není rozdíl oproti L-glutaminu zřetelný.'),
        ('Kdy se glutamin užívá?', 'Nejčastěji po tréninku nebo před spaním, ale pevné pravidlo neexistuje. Řiďte se doporučeným dávkováním na obalu a nepřekračujte ho.'),
        ('Má glutamin nežádoucí účinky?', 'U zdravých dospělých bývá dobře snášen, vyšší množství může způsobit zažívací potíže. Těhotné, kojící, děti a lidé s onemocněním jater, ledvin nebo užívající léky by se měli poradit s lékařem nebo lékárníkem.'),
        ('Čím se glutamin liší od BCAA?', 'BCAA jsou tři esenciální aminokyseliny – leucin, isoleucin a valin. Glutamin je samostatná aminokyselina, která esenciální není. Směsi obsahují obojí, ale množství glutaminu v nich bývá menší než v samostatném přípravku.'),
        ('Je glutamin vhodný pro vegany?', 'Záleží na výrobě. Fermentovaný glutamin je rostlinného původu a obvykle se hodí pro vegany. Zkontrolujte označení na obalu, zejména u směsí s dalšími látkami.'),
    ])
