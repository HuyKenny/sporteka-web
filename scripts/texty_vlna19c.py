"""sporteka.cz — wave 19c (4. 11. 2026): long texts (>= 1650 words) for vetrovky, dalekohledy-a-kompasy, volejbal, elektrokola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ vetrovky
NEW['vetrovky'] = dict(long=True,
    title='Větrovky a šusťákové bundy: výběr a péče',
    desc='Větrovky a šusťáky pro běh, kolo, turistiku i město. Jak vybrat střih, materiál, kapuci a velikost a kde porovnat nabídky českých obchodů.',
    intro='<p>Větrovka je tenká vrstva, která se vejde do kapsy a přesto zastaví studený průvan. Šustivý povrch z hustě tkaného vlákna nepustí vítr k tričku, takže tělo neztrácí teplo zbytečně rychle. Právě proto sáhne po větrovce běžec, cyklista, turista i rodič na hřišti. Dobře zvolený kus váží jen zlomek zimní bundy, a přesto zabrání tomu, aby vás závan vychladil dřív, než dojdete na konec trasy.</p>'
          '<p>Na Sportece porovnáte nabídky obchodů u modelů od značek jako Fjällräven, Helikon-Tex, Columbia, Helly Hansen nebo Hannah. '
          'Pokud vás zajímá teplejší nebo naopak vodotěsnější varianta, projděte <a href="/softshellove-bundy/">softshellové bundy</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a> a <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>. '
          'Průvodce níže vysvětluje materiály, střih, velikost i to, jak větrovku vrstvit a ošetřovat.</p>',
    guide='<h2>K čemu větrovka slouží a k čemu ne</h2>'
          '<p>Větrovka řeší jediný problém: proudění vzduchu přes oděv. Když fouká, studený vzduch vytlačuje teplý polštář kolem těla a cítíte chlad i při mírné teplotě. Hustá tkanina tento proces zpomalí. Větrovka ale sama nehřeje, nemá izolaci a většinou ani nevydrží vytrvalý déšť. '
          'Lehké potahy z polyamidu nebo polyesteru snesou krátkou přeháňku díky úpravě povrchu, jenže za hodinu v dešti promoknou. Na dlouhý déšť patří do batohu nebo na záda <a href="/nepromokave-bundy/">nepromokavá bunda</a> nebo alespoň <a href="/plastenky/">pláštěnka</a>.</p>'
          '<p>Rozdíl mezi větrovkou a „šusťákem“ je spíš jazykový než technický. Šusťák označuje bundu s typicky hladkým, hlasitě šustivým povrchem a často s podšívkou ze síťoviny. Větrovka je obecnější pojem a zahrnuje i ultralehké modely, které se sbalí do vlastní kapsy.</p>'
          + T(['Vrstva', 'Úkol', 'Typický kus'], [
              ['Základní', 'odvádí pot od kůže', '<a href="/funkcni-tricka/">funkční triko</a>, <a href="/termopradlo/">termoprádlo</a>'],
              ['Střední', 'drží teplo', '<a href="/fleecove-mikiny/">fleecová mikina</a>, <a href="/sportovni-vesty/">vesta</a>'],
              ['Vnější větrná', 'blokuje proudění', 'větrovka, šusťáková bunda'],
              ['Vnější nepromokavá', 'zastaví vodu', '<a href="/nepromokave-bundy/">membránová bunda</a>']]) +
          '<h2>Materiály a povrchová úprava</h2>'
          '<p>Většina větrovek je z polyamidu (nylonu) nebo polyesteru. Polyamid je při stejné hmotnosti pevnější v oděru a příjemnější na dotek, polyester méně nasákne vodou a rychleji schne. Důležitá je i gramáž a hustota tkaní: čím hustší, tím lépe tkanina brání větru, ale tím hůř dýchá.</p>'
          '<p>Povrch často nese úpravu DWR, která nechává kapky stékat po látce. Tahle vrstva časem slábne, protože ji stírá tření a špína, a dá se obnovit pračkou i impregnací určenou pro funkční textil. Některé větrovky mají tenkou membránu nebo laminát, který zvyšuje odolnost proti větru a lehkému dešti, ale bývá teplejší. '
          'Bavlněné nebo bavlněné směsové parky a polní bundy, které najdete u značek Brandit či Helikon-Tex, patří spíš mezi <a href="/kabaty-a-parky/">kabáty a parky</a> než mezi ultralehké větrovky.</p>'
          + T(['Materiál', 'Výhody', 'Nevýhody'], [
              ['Polyamid (nylon)', 'pevný, lehký, příjemný na dotek', 'pomaleji schne, může se leskle třít'],
              ['Polyester', 'málo nasákne, rychle schne', 'o něco hlasitější, hůř odolává oděru'],
              ['Směsový s elastanem', 'pružný, volnější pohyb', 'o něco těžší, méně odolný'],
              ['Laminát s membránou', 'lepší ochrana před větrem i vlhkem', 'menší prodyšnost, vyšší váha']]) +
          '<h2>Typy větrovek podle sportu a situace</h2>'
          '<h3>Běžecké</h3>'
          '<p>Nejlehčí a nejužší modely, často s reflexními prvky a zadním větráním. Mají se vejít do kapsy nebo opasku, proto kapuce bývá sbalitelná nebo chybí. Pokud běháte s <a href="/bezecke-vesty-a-batohy/">běžeckou vestou</a>, zkontrolujte, že rukávy větrovky lze pohodlně vyhrnout a nestlačují paži pod vestou. Doplňkem jsou <a href="/bezecka-obuv/">běžecké boty</a> a <a href="/cepice-a-celenky/">čepice</a>.</p>'
          '<h3>Cyklistické</h3>'
          '<p>Mají delší záda, aby kryly beder ve skloněné poloze, a kratší přední díl, aby se nenabíral na břiše. Zip bývá až po bradu a zadní kapsa slouží k odkládání věcí. Podrobnější nabídku najdete v kategorii <a href="/cyklisticke-bundy-a-vesty/">cyklistické bundy a vesty</a>, obecný přehled pak v <a href="/cyklisticke-obleceni/">cyklistickém oblečení</a>.</p>'
          '<h3>Turistické</h3>'
          '<p>Na túru se hodí větrovka s kapucí, kapsami na zip a stahováním v pase i lemu. Ochrání při přestávce na hřebeni a zabere v batohu málo místa. Pokud nosíte větší <a href="/turisticke-batohy/">turistický batoh</a>, počítejte s tím, že popruhy a bederní pás třou o rameno, takže tenká látka musí být dostatečně odolná.</p>'
          '<h3>Městské a volnočasové</h3>'
          '<p>Značky jako Adidas, Puma, Under Armour nebo New Era dodávají větrovky se sportovním střihem a logem na hrudi, které sedí k džínám i teplákům. Pro všední dny stačí lehká podšívka a prakticky řešené kapsy, technická membrána tu není nutná.</p>'
          '<h2>Střih, velikost a kapuce</h2>'
          '<p>Větrovka se nosí přes jednu nebo dvě vrstvy, takže má sedět volněji než triko, ale ne tak, aby se plácala ve větru. Rozhodující je obvod hrudníku, délka rukávu a délka zad. Rukáv musí po zvednutí paží zakrýt zápěstí, jinak vítr fouká dovnitř. '
          'Podle délky záda se vyplatí větrovka s prodlouženým zadním dílem, ať už jezdíte na kole, nebo se hodně předklání při chůzi do kopce. Při měření si změřte hrudník na nejširším místě a porovnejte s tabulkou výrobce, protože i bundy stejné značky se mohou lišit podle řady.</p>'
          '<p>Kapuce bývá pevná, sbalitelná do límce nebo odepínací. U běžeckých a cyklistických modelů ji řada lidí nechce, protože vlaje a zvedá se jako plachta. Na túru a do města je užitečná, hlavně pokud má stahování a okrajovou výztuhu, aby vám nesklouzla do očí. '
          'Zkontrolujte, zda kapuce nepřekáží při nošení helmy, pokud ji budete používat při sportu.</p>'
          + T(['Hlavní použití', 'Délka zad', 'Kapuce', 'Další prvky'], [
              ['Běh', 'normální až mírně delší', 'spíš chybí nebo sbalitelná', 'reflexní prvky, malá kapsa'],
              ['Kolo', 'prodloužená', 'bez kapuce', 'zadní kapsa, větrací otvory'],
              ['Turistika', 'normální', 'pevná se stahováním', 'kapsy na zip, stahovací šňůra v pase'],
              ['Město', 'normální', 'podle módy', 'podšívka, praktické kapsy']]) +
          '<h2>Zip, kapsy, větrání a drobnosti</h2>'
          '<p>Dobře fungující zip je u větrovky důležitější než logo. Zip s krytkou nebo lištou zabrání pronikání větru do švu. Kapsy na zip uchrání klíče a telefon, kapsa s otvorem na sluchátka se hodí při běhu. '
          'Větrání pod rukávy a na zádech snižuje pocit zapařenosti, ale snižuje větruodolnost. Pokud se vám vyplatí lepší dýchání, poohlédněte se po modelech s malými síťkami nebo laserově děrovanou látkou. Pružné lemy u rukávů a dole drží bundu na místě a omezují vnikání vzduchu.</p>'
          '<h2>Jak větrovku vrstvit</h2>'
          '<p>Větrovka nepatří přímo na kůži. Pod ní nosíte tričko z technického materiálu, které odvádí pot, případně <a href="/merino-tricka/">merino triko</a>. V chladu se přidá lehká mikina nebo vesta, kterou větrovka překryje. Na podzim vám pomůže <a href="/funkcni-mikiny/">funkční mikina</a>, na jaře stačí samotné triko. Při zastávce si větrovku oblékněte dřív, než vychladnete, protože znovu se zahřát trvá déle než teplo udržet.</p>'
          '<p>Při intenzivním pohybu se vyplatí větrovku zapínat jen napůl, případně ji sundat a uložit. Jakmile se pocení zvýší, vlhkost se hromadí pod hustou tkaninou a oblečení se prokládá potem. Bunda s lepším větráním toleruje namáhavější sport, ale na zimní běh bude pořád potřeba doplnit <a href="/sportovni-rukavice/">rukavice</a> a čepici.</p>'
          '<h2>Péče o větrovku</h2>'
          '<p>Praní chrání funkčnost látky víc, než si lidé myslí. Pot, mastnota a prach ucpávají póry a snižují prodyšnost i vodoodpudivost. Perte při teplotě uvedené na štítku, s jemným prostředkem bez aviváže a změkčovadel. Avivážní složky zalepují vlákna a tkanina pak ztrácí odpudivost. Zip před praním zapněte, suchý zip zapněte a bundu vyjměte po skončení programu.</p>'
          '<p>Sušit je nejlepší na ramínku při pokojové teplotě. Do sušičky s vyšší teplotou bundy nepatří, tenké vlákno se může zdeformovat a laminát odlepit. Po několika sezonách, když kapky přestanou stékat, nanesete impregnaci určenou pro funkční textil a bundu krátce vyhřejete teplým vzduchem podle návodu. Pokud je látka trhlinou poškozena, zalepte ji tenkou textilní záplatou, než se roztrhne dál.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Koupě podle vzhledu:</strong> módní střih nemusí odpovídat sportu. Na běh vás omezí úzký rukáv, na kolo krátká záda.</li>'
          '<li><strong>Očekávání nepromokavosti:</strong> větrovka s úpravou DWR zvládne jen krátký déšť.</li>'
          '<li><strong>Příliš těsná velikost:</strong> bunda, která pne přes mikinu, omezuje pohyb a netěsní.</li>'
          '<li><strong>Zapomenutí na sbalení:</strong> lehká větrovka má smysl, jen když ji vezmete s sebou. Vyberte model s kapsou, do které se sbalí.</li>'
          '<li><strong>Špatná péče:</strong> aviváž a sušička zkracují život látky.</li></ul>'
          '<h2>Pro koho se větrovka hodí</h2>'
          '<p>Větrovka je rozumné rozšíření šatníku pro každého, kdo se hýbe venku mezi dubnem a říjnem. Rodiče na tribunách, děti na školním výletě, kolegové jedoucí do práce na kole nebo turisté, kteří chtějí mít rezervu v batohu, využijí stejný druh kusu. '
          'Pro studenější měsíce přemýšlejte spíš o <a href="/zimni-bundy/">zimních a péřových bundách</a> a o <a href="/outdoorove-kalhoty/">outdoorových kalhotách</a>, pro svižný sport v zimě postačí tenčí vrstva kombinovaná s teplou mikinou.</p>'
          '<h2>Jak nakupovat přes Sporteku</h2>'
          '<p>Filtrujte podle značky, pohlaví, velikosti a ceny, seřaďte podle sezóny nebo popularity a porovnejte, který obchod model skutečně drží skladem. U každého kusu si přečtěte popis materiálu a střihu, protože fotografie nepoví nic o hmotnosti a sbalitelnosti. Nehodí-li se jedna velikost, zkuste stejný model v jiné řadě téže značky, protože střih se u výrobců často liší.</p>',
    faq=[
        ('Jaký je rozdíl mezi větrovkou a softshellovou bundou?', 'Větrovka je tenká a bez izolace, jejím úkolem je zastavit vítr. Softshell bývá silnější, pružnější a hřeje víc, protože má tkaninu s úpravou a často fleecový vnitřek. Na podzim a v zimě je tedy lepší softshell, v jarním a letním větru stačí větrovka.'),
        ('Je větrovka nepromokavá?', 'Obvykle ne. Většina modelů má jen vodoodpudivou úpravu povrchu, která zvládne krátkou přeháňku. Pro delší déšť je potřeba bunda s membránou a zalepenými švy.'),
        ('Jakou velikost větrovky zvolit?', 'Změřte hrudník na nejširším místě a porovnejte s tabulkou výrobce. Pokud budete pod bundou nosit mikinu, vezměte raději volnější variantu. Rukáv by měl po zvednutí paží stále krýt zápěstí.'),
        ('Dá se větrovka prát v pračce?', 'Ano, na šetrný program při teplotě uvedené na štítku a bez aviváže. Zip zapněte a bundu nesušte na topení ani v horké sušičce, aby se nepoškodila úprava a vlákno.'),
        ('Jak obnovím vodoodpudivost?', 'Vyperte bundu čistým prostředkem pro funkční textil, naneste impregnaci určenou pro daný materiál a ošetřenou bundu zahřejte podle návodu výrobce. Impregnaci vždy nanášejte na čistý textil a řiďte se pokyny na obalu, protože některé přípravky se nanášejí na vlhký a jiné na suchý materiál.'),
        ('Co vzít na běh za chladného větru?', 'Lehkou větrovku s reflexními prvky přes funkční triko, čepici nebo čelenku a tenké rukavice. Pokud se rozběháte, můžete bundu zapnout jen napůl nebo ji svázat kolem pasu či schovat do kapsy.'),
        ('Hodí se větrovka na kolo?', 'Ano, pokud má delší záda, zip ke krku a kapsu vzadu. Dobrá cyklistická větrovka je tenká, dobře se sbalí a většinou bez kapuce, aby nevlála. Jezdíte-li za deště, potřebujete model s membránou.'),
        ('Proč větrovka šustí?', 'Šustění vzniká třením hladké a pevné tkaniny z polyamidu nebo polyesteru. Hlasitost závisí na tloušťce a úpravě. Pokud vám zvuk vadí, hledejte měkčí povrch nebo bundu s elastickým podílem.'),
        ('Je lepší větrovka s kapucí, nebo bez?', 'Pro turistiku a město je kapuce užitečná, pro běh a kolo bývá zbytečná, protože vlaje a překáží pod helmou. Rozhodněte podle toho, kde ji budete nosit nejčastěji.'),
        ('Vejde se větrovka do batohu?', 'Ultralehké modely se sbalí do kapsy nebo do sáčku velikosti ovoce a zabírají méně místa než láhev. Na túru je ideální bunda, která má kolem 100 až 200 g a drží tvar i po opakovaném sbalení.'),
    ],
)


# ------------------------------------------------------------------ dalekohledy-a-kompasy
NEW['dalekohledy-a-kompasy'] = dict(long=True,
    title='Dalekohledy, kompasy a navigace: jak vybrat',
    desc='Dalekohledy, monokuláry, buzoly a orientační pomůcky pro túry, lov i pozorování. Jak číst zvětšení a objektiv a kde porovnat nabídky obchodů.',
    intro='<p>Dobrý dalekohled přiblíží vzdálenou siluetu srnce, vrchol hřebene nebo ptáka na větvi, buzola zase ukáže směr ve chvíli, kdy ztichne telefon. Obě pomůcky vypadají jednoduše, jenže zvětšení, průměr objektivu, zorné pole i způsob nošení rozhodují o tom, zda je budete na výletě opravdu používat, nebo je necháte ležet na dně batohu.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u značek jako Levenhuk, Silva, Bushnell, Discovery, Mil-tec nebo Solognac. Pomůcky se hodí k <a href="/turisticke-batohy/">turistickým batohům</a>, <a href="/lov-a-priroda/">lovu a přírodě</a>, <a href="/lovecke-vybaveni/">loveckému vybavení</a>, <a href="/celovky-a-svitilny/">čelovkám a svítilnám</a> i k <a href="/outdoor/">outdoorové výbavě</a>. V průvodci najdete význam čísel na těle přístroje, typy optiky, orientaci podle mapy a péči o sklo.</p>',
    guide='<h2>Co znamenají čísla na dalekohledu</h2>'
          '<p>Na každém klasickém dalekohledu najdete dvojici čísel, například 8x42 nebo 10x50. První číslo říká, kolikrát se objekt přiblíží, druhé je průměr předních čoček v milimetrech. Větší objektiv nasbírá víc světla, takže obraz za šera zůstane jasnější, ale přístroj je větší a těžší. Vyšší zvětšení přiblíží detail, jenže zároveň zvýrazní chvění rukou a zúží zorné pole, tedy plochu, kterou vidíte najednou.</p>'
          + T(['Údaj', 'Co znamená', 'Praktický dopad'], [
              ['Zvětšení (první číslo)', 'kolikrát se předmět zdánlivě přiblíží', 'víc detailu, ale větší chvění obrazu'],
              ['Objektiv (druhé číslo)', 'průměr přední čočky v mm', 'jas za šera, rozměr a hmotnost'],
              ['Zorné pole', 'šířka záběru na určitou vzdálenost', 'snazší nalezení pohyblivého cíle'],
              ['Výstupní pupila', 'objektiv dělený zvětšením', 'čím větší, tím jasnější obraz za šera'],
              ['Odstup oka', 'vzdálenost oka od okuláru', 'důležitá pro nositele brýlí']]) +
          '<p>Výstupní pupilu si spočítáte sami: u přístroje 8x42 vychází zhruba 5 mm, u 10x50 rovněž 5 mm. Lidská zornice se za šera rozevře přibližně na tuto hodnotu, takže takové dvojice dobře využijí světlo. Pro denní turistiku stačí menší objektiv, který nezatíží krk.</p>'
          '<h2>Typy pozorovací optiky</h2>'
          '<h3>Binokulár s Porro hranoly</h3>'
          '<p>Klasický tvar s odsazenými tubusy. Optika bývá jednodušší, obraz plastický a cena přístupná, ale tělo je širší a objemnější. Hodí se pro pozorování z jednoho místa, třeba u rybníka nebo na vyhlídce.</p>'
          '<h3>Binokulár se střechovými hranoly</h3>'
          '<p>Rovné tubusy, štíhlejší a lépe padnoucí do ruky. Konstrukce je náročnější na výrobu, a proto kvalitní kusy stojí víc, jejich výhodou je ale úzké tělo a snadné nošení při túrách. Většinou mají pogumovaný povrch a bývají odolnější vůči vlhkosti.</p>'
          '<h3>Monokulár</h3>'
          '<p>Jedna trubice pro jedno oko. Je lehký, vejde se do kapsy a zvládne pozorování z cesty, od hřebene či při orientaci v terénu. Pro delší sledování je ale únavnější, protože druhé oko zůstává otevřené nebo přivřené.</p>'
          '<h3>Dětské a hračkové modely</h3>'
          '<p>Menší zvětšení, lehké plastové tělo a široké zorné pole. Dítě s ním rychle najde cíl, což je pro první pozorování přírody důležitější než technické parametry. Vybírejte odolné tělo a pevné poutko.</p>'
          + T(['Typ', 'Výhoda', 'Omezení'], [
              ['Binokulár Porro', 'plastický obraz, nižší náklady', 'širší a těžší tělo'],
              ['Binokulár střechový', 'štíhlý, snadné nošení', 'náročnější výroba, vyšší cena'],
              ['Monokulár', 'lehký, kapesní', 'únava při dlouhém pozorování'],
              ['Dětský dalekohled', 'odolný, široké zorné pole', 'jednodušší optika']]) +
          '<h2>Výběr podle použití</h2>'
          '<p>Na túru hledejte kompaktní přístroj kolem 8x s menším objektivem. Při pozorování ptáků nebo zvěře se vyplatí 8x42, případně 10x42, které je přesnější, ale vyžaduje klidnější ruku. Ke sledování hvězd či za šera patří větší objektivy, zatímco pro koncert, stadion nebo plachtu na lodi postačí malé a lehké modely se zvětšením kolem 8x. Dalekohled do lodi bývá ve vodotěsném provedení, protože stříkající voda a vlhkost jsou běžné.</p>'
          '<p>Při lovu navíc rozhoduje, jak přístroj sedí za šera a jak snadno se vyndává. Lovecké kolekce často přidávají popruh, pouzdro a ochranu proti odleskům. Doplňte ji o <a href="/lovecke-obleceni/">lovecké oblečení a obuv</a>, pokud vyrážíte na delší hlídku. Pro vodní sporty a plavbu si prohlédněte i <a href="/plovaci-vesty/">plovací vesty</a>.</p>'
          '<h2>Kvalita optiky: povrchy, hranoly a sklo</h2>'
          '<p>Kvalitu čoček ovlivňují povlaky proti odrazům. Označení jako coated, fully coated nebo multi-coated vyjadřuje, kolik povrchů má vrstvu, která zlepšuje průchod světla. Čím víc ploch je upraveno, tím jasnější a kontrastnější obraz, hlavně v protisvětle a při západu slunce. Další rozdíl dělá sklo a hranoly: kvalitnější sklo omezuje barevné okraje u kontrastních předmětů a drží ostrost až do okraje zorného pole.</p>'
          '<p>Praktický test v obchodě nebo doma zahrnuje pohled na vzdálený drát nebo hranu střechy. Pokud kolem objevíte výrazné barevné lemy, ostrost se rychle ztrácí od středu k okraji nebo vidíte dvě oddělené kruhové plochy, nastavení nebo optika vyhovují málo. Zkoušejte také ostření: kolečko má jít plynule, bez vůle a bez zadrhávání.</p>'
          '<h2>Nastavení dalekohledu na oči</h2>'
          '<p>Většina dvojitých dalekohledů umožňuje nastavit vzdálenost tubusů podle rozteče očí. Přístroj rozevřete tak, aby se oba kruhy sloučily v jeden. Poté zaostřete na vzdálený předmět levým okem a pravé nechte zavřené. Nakonec zavřete levé oko a dioptrickým kroužkem srovnejte ostrost u pravého. Tento postup stačí provést jednou, nastavení si zapamatujete.</p>'
          '<p>Nositelé brýlí potřebují delší odstup oka a okulár se odklopenou nebo sklopenou očnicí. Pokud brýle nosíte, očnici stáhněte dolů a přiložte brýle přímo na okulár. Jinak se zorné pole zmenší do tmavého okénka.</p>'
          '<h2>Kompasy a buzoly: základní typy</h2>'
          '<p>Buzola ukazuje magnetický sever pomocí jehly plovoucí v kapalině. Nejpraktičtější pro turistiku je deskový kompas s průhlednou základnou, otočnou lunetou, ryskou a měřítky. Značka Silva je v tomto oboru dlouhodobě známá a nabízí různé deskové modely včetně verzí pro děti či orientační běh. Jednodušší kapesní buzoly s víčkem se hodí spíše jako záloha nebo na lodní palubu.</p>'
          + T(['Typ', 'Využití', 'Poznámka'], [
              ['Deskový kompas', 'práce s mapou, turistika, orientační běh', 'otočná luneta, ryska a pravítko'],
              ['Kapesní buzola s víčkem', 'záloha, pro děti', 'méně přesné měření úhlu'],
              ['Zrcátkový kompas', 'přesné měření azimutu', 'náročnější používání'],
              ['Hodinky nebo přístroj s kompasem', 'rychlý směr', 'vyžadují baterii a kalibraci']]) +
          '<p>Při práci s mapou přiložte hranu kompasu mezi dva body, otáčením lunety srovnejte její ryskou s mřížkou mapy a pak otočte celou mapu i kompas, až jehla zapadne do sever-jih lunety. Magnetická deklinace, tedy rozdíl mezi zeměpisným a magnetickým severem, je v Česku malá, ale na delších cestách do zahraničí ji do výpočtu zahrňte. Jehla se mýlí také poblíž kovů, vedení vysokého napětí a magnetů, proto kompas nedržte blízko telefonu nebo nože.</p>'
          '<h2>Teleskopy, dálkoměry a noční vidění</h2>'
          '<p>V nabídce se objevují i hvězdářské teleskopy, dalekohledy s dálkoměrem a přístroje pro noční vidění. Hvězdářský teleskop se kupuje na oblohu a ne na túru: rozhoduje průměr objektivu a stabilní montáž, protože i malé chvění se při velkém zvětšení přenáší do obrazu. Dálkoměr se hodí při střelbě, lovu a golfu, kde potřebujete znát vzdálenost. Noční vidění je specializovaná technika a vyplatí se u ní zkontrolovat dosah a způsob napájení.</p>'
          '<h2>Navigace: GPS a mapy v mobilu</h2>'
          '<p>Elektronická navigace usnadňuje orientaci, ale závisí na baterii, signálu a dobře dostupných mapových podkladech. U turistických přístrojů sledujte výdrž, odolnost vůči vodě a způsob nabíjení. Rezervou je papírová mapa s kompasem, protože nezávisí na ničem než na vašich schopnostech. K doplnění energie se hodí <a href="/powerbanky-a-nabijeni/">powerbanky a nabíječky</a>, pro doplňkové údaje o trase i <a href="/sportovni-hodinky/">sportovní hodinky</a>.</p>'
          '<h2>Pouzdra, popruhy a doplňky</h2>'
          '<p>K přístroji patří pouzdro s měkkou vložkou, popruh na krk a krytky okulárů i objektivů. Široký popruh rozloží váhu a nebude řezat do šíje. Krytka chrání sklo před prachem, a když dalekohled zrovna nepoužíváte, zabrání vzniku škrábanců. Kapesní monokulár nosí turisté v postranní kapse, často vedle pláštěnky a čelovky. Při nepříznivém počasí se hodí <a href="/plastenky/">pláštěnka</a>, kterou přehodíte přes přístroj.</p>'
          '<h2>Péče o optiku</h2>'
          '<ul><li>Prach z čoček nejprve odfoukněte štětečkem nebo balónkem, teprve pak otřete.</li>'
          '<li>Používejte mikrovláknový hadřík a čisticí roztok určený pro optiku, nikdy tričko ani papírový kapesník.</li>'
          '<li>Po dešti přístroj usušte při pokojové teplotě, ne u radiátoru ani na slunci.</li>'
          '<li>Po moři opláchněte tělo sladkou vodou a čočky přetřete jemně navlhčenou tkaninou, aby neulpěla sůl.</li>'
          '<li>Neskladujte v zavřeném autě v létě, kde teplo rozlepuje a deformuje součásti.</li></ul>'
          '<p>Pokud se uvnitř přístroje objeví vlhkost nebo prach, nepokoušejte se jej rozebírat. Plněné dusíkem bývají jen vodotěsné modely a jejich oprava patří do servisu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Honba za nejvyšším zvětšením, přestože ruka chvění nezvládne.</li>'
          '<li>Kupování příliš těžkého přístroje, který pak zůstane doma.</li>'
          '<li>Podcenění odstupu oka u nositelů brýlí.</li>'
          '<li>Přehlédnutí ochrany proti vodě u lodních a zimních výprav.</li>'
          '<li>Spoléhání jen na mobil bez papírové mapy a buzoly.</li></ul>'
          '<h2>Pro koho jednotlivé typy sedí</h2>'
          '<p>Rodiny s dětmi ocení odolné a lehké dalekohledy do 8x, které zvládnou pád do trávy. Turisté sáhnou po kompaktním binokuláru nebo monokuláru a osvědčeném deskovém kompasu. Myslivci a pozorovatelé zvěře investují do světelnějšího přístroje s lepšími povlaky. Orientační běžci potřebují kompas, který se rychle ustálí a dobře drží na palci. Plavci a vodáci hledají pogumované a vodotěsné tělo.</p>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>Katalog nabízí přístroje od jednoduchých dětských modelů po větší binokuláry. Filtrujte podle značky a sledujte, v kterých obchodech je přístroj skladem. Před koupí si vždy ověřte zvětšení, průměr objektivu, hmotnost, zda je tělo vodotěsné a co je v balení. Při srovnání dvou podobných kusů rozhodují často drobnosti, třeba záruka, pouzdro nebo kvalita popruhu. Pokud hledáte čelovku pro večerní pozorování, podívejte se do kategorie <a href="/celovky-a-svitilny/">čelovky a svítilny</a>, a kdo vyráží na víc dní, zvolí k tomu <a href="/turisticke-stany/">turistický stan</a>.</p>',
    faq=[
        ('Jaké zvětšení dalekohledu zvolit na túry?', 'Na většinu výletů stačí zvětšení kolem 8x. Obraz je stabilní i bez stativu, zorné pole široké a přístroj zůstává lehký. Vyšší hodnoty zlepší detail, ale zvýrazní chvění rukou a vyžadují pevnější držení.'),
        ('Co znamená označení 8x42?', 'První číslo je zvětšení, tedy osmkrát bližší obraz, druhé průměr objektivu 42 milimetrů. Větší objektiv propustí víc světla, takže se hodí i za šera, ale přístroj je větší a těžší než kompaktní 8x25.'),
        ('Jak poznám kvalitní optiku?', 'Podívejte se na ostrost do okrajů, barevné lemy na kontrastních hranách a na povlaky čoček. Kvalitní přístroj má jasný obraz bez zbytečného zkreslení a plynulé ostření. Pomůže i čtení označení coated či multi-coated v popisu.'),
        ('Je lepší binokulár, nebo monokulár?', 'Binokulár poskytuje pohodlnější a plastičtější obraz při delším pozorování, monokulár je menší a lehčí. Pro rychlý pohled na túře stačí monokulár, kdo sleduje zvěř nebo ptáky delší dobu, zvolí raději dva tubusy.'),
        ('Mohu dalekohled používat s brýlemi?', 'Ano, pokud má dostatečný odstup oka a sklopné či odklopné očnice. Očnice sklopte, přiložte brýle k okuláru a zorné pole se neuřízne. U přístrojů s krátkým odstupem oka brýle obraz zužují.'),
        ('Jak funguje deskový kompas?', 'Jehla se ustálí na magnetickém severu, otočná luneta s ryskou slouží k nastavení směru podle mapy. Přiložíte kompas k mapě, nastavíte směr, zarovnáte jehlu s lunetou a jdete po ukázaném azimutu.'),
        ('Je v dnešní době buzola ještě potřeba?', 'Ano, protože nepotřebuje baterii ani signál. Mobil může vypadnout, vybít se nebo se rozbít v dešti, zatímco papírová mapa s buzolou funguje vždy. Pro delší túry mimo značené trasy je to rozumná záloha.'),
        ('Jak čistit čočky dalekohledu?', 'Prach nejprve odfoukněte, poté lehce otřete mikrovláknovou utěrkou. Mastné šmouhy odstraní čisticí roztok určený pro optiku. Nepoužívejte hrubé látky, papírové kapesníky ani agresivní čističe, které by poškrábaly povlak.'),
        ('Hodí se dalekohled pro děti?', 'Ano, pokud je lehký, odolný a má jednoduché ostření. Pro děti stačí nízké zvětšení, které zaručí široké zorné pole a rychlé nalezení cíle. Dobré jsou modely s gumovým povrchem a popruhem proti pádu.'),
        ('Na co dát pozor u dalekohledu do vlhka?', 'Hledejte označení vodotěsný nebo odolný proti stříkající vodě. Takové přístroje mají utěsněný tubus a bývají plněné suchým plynem, aby se uvnitř nerosilo sklo. Po použití je přesto vysušte a uložte na suchém místě.'),
    ],
)


# ------------------------------------------------------------------ volejbal
NEW['volejbal'] = dict(long=True,
    title='Volejbal: míče, obuv, sítě a oblečení',
    desc='Volejbalová výbava: míče, sítě, sálová obuv, kolenní chrániče a dresy. Jak vybrat pro halu, pláž i školu a kde porovnat nabídky obchodů.',
    intro='<p>Volejbal vypadá nenáročně, stačí míč, síť a pár spoluhráčů. Jenže právě drobnosti výbavy rozhodují o tom, zda vás po hodině bolí kolena, zda vám pod chodidlem neklouže parket a zda míč při podání letí tam, kam má. Jiné vybavení potřebujete v hale, jiné na písku a jiné na školním hřišti.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů a z kategorie vás dovede k <a href="/volejbalove-mice/">volejbalovým míčům a sítím</a>, <a href="/salova-obuv/">sálové obuvi</a>, <a href="/bandaze-a-ortezy/">bandážím a ortézám</a>, <a href="/dresy/">dresům</a> i <a href="/sportovni-ponozky/">sportovním ponožkám</a>. Najdete tu značky Mizuno, Asics, Gala, Mikasa, Kipsta, Molten nebo Allsix. Níže je přehled výbavy podle prostředí, postup při výběru obuvi a rady, jak se vyhnout častým zraněním.</p>',
    guide='<h2>Co ke hře potřebujete</h2>'
          '<p>Základní soubor je krátký: míč, síť s anténami a vhodná obuv. K pohodlí přibývají kolenní chrániče, ponožky s tlumením, šortky nebo legíny a dres odvádějící pot. Ve škole nebo kroužku stačí jednoduché vybavení, týmy v soutěži potřebují jednotné dresy s čísly a rezervní míče. Pláž přidává brýle, čepici a krém s UV filtrem.</p>'
          + T(['Výbava', 'K čemu slouží', 'Na co dát pozor'], [
              ['Míč', 'samotná hra', 'velikost, povrch, hala nebo pláž'],
              ['Sálová obuv', 'přilnavost a tlumení dopadů', 'podrážka, tlumení, uchycení kotníku'],
              ['Kolenní chrániče', 'ochrana při pádech a skocích', 'velikost, výška vycpávky'],
              ['Síť a stojany', 'vymezují hřiště', 'výška, upevnění, délka'],
              ['Dres a šortky', 'pohyblivost a odvod potu', 'střih, materiál, potisk']]) +
          '<h2>Volejbalový míč: halový, plážový a rekreační</h2>'
          '<p>Halový míč má šitý nebo lepený obal z kůže či syntetického materiálu a hladký povrch. Plážový je o něco větší, měkčí a s nižším tlakem, aby se líp ovládal ve větru a při hře na písku. Rekreační míče bývají odolnější a tvrdší, snesou drsný povrch hřiště i školní tělocvičnu. Značky Mikasa a Molten patří mezi široce uznávané výrobce herních míčů, Gala a Kipsta nabízejí široký sortiment pro kluby i školy.</p>'
          + T(['Typ míče', 'Prostředí', 'Charakter'], [
              ['Halový', 'tělocvična, hala', 'hladký, přesný odskok, tužší'],
              ['Plážový', 'písek, venkovní hřiště', 'měkčí, o něco větší, odolnější vůči povětří'],
              ['Rekreační', 'zahrada, tábor, škola', 'odolný, jednodušší povrch'],
              ['Dětský a mini', 'výuka, malé hráče', 'lehčí, měkčí, snazší na odbití']]) +
          '<p>Míč před hrou nahustěte na tlak, který udává výrobce na ventilku nebo v návodu. Příliš tvrdý míč bolí předloktí a odskakuje nepředvídatelně, měkký padá krátce a ztrácí rychlost. K hustění pomáhá pumpa s manometrem a jehla, kterou před zasunutím navlhčíte. Více o druzích míčů a sítí najdete v podkategorii <a href="/volejbalove-mice/">volejbalové míče a sítě</a>.</p>'
          '<h2>Sálová obuv pro volejbal</h2>'
          '<p>Halová podrážka ze světlé pryže drží na parketu a nezanechává stopy. Při volejbalu se často skáče, dopadá a rychle mění směr, proto se vyplatí obuv s tlumením v přední části i patě a stabilním uchycením kolem kotníku. Značky Mizuno a Asics mají volejbalové modely dlouhodobě v nabídce, Adidas, Joma a Kipsta pokrývají širší škálu rekreačních i klubových typů. Venkovní běžecká obuv nevyhovuje, protože tlustá patní část zvyšuje riziko podvrtnutí a tvrdá podrážka je na hladkém povrchu kluzká.</p>'
          '<p>Při zkoušce nechte před palcem asi šířku prstu, pata ať sedí pevně a při drepu nesmí sklouzávat. Šněrování dotahujte postupně od špičky ke kotníku. Příliš lepivá podrážka může při rychlém otáčení zatěžovat klouby, proto si ji vyzkoušejte přímo na povrchu, na kterém budete hrát. Navazující nabídku jiných typů najdete v kategoriích <a href="/salova-obuv/">sálová a halová obuv</a> a <a href="/sportovni-obuv/">sportovní obuv</a>.</p>'
          '<h2>Chrániče, bandáže a ortézy</h2>'
          '<p>Kolenní chrániče jsou typické pro volejbal, protože hráči padají na kolena při zachraňování míče. Měkká pěna absorbuje náraz a snižuje otlaky. Důležitá je správná velikost: příliš volný chránič sjíždí, příliš těsný omezuje ohyb. Někdo preferuje delší chrániče s vyšším krytím, jiný krátké. K ochraně kotníků a prstů slouží bandáže a stabilizační ortézy. U kloubu s předchozím zraněním se poraďte s lékařem nebo fyzioterapeutem. Univerzální bandáž nenahrazuje léčbu. Výběr je v kategorii <a href="/bandaze-a-ortezy/">bandáže a ortézy</a>.</p>'
          '<h2>Dresy, trička a šortky</h2>'
          '<p>Volejbalový dres je lehký, prodyšný a střihem nebrání v rozmachu paží. Materiály jako polyester s odvodem vlhkosti zůstanou při dlouhé hře suché. Týmové soupravy bývají v jednotné barvě, hráč libero má odlišnou barvu dresu. U pohodlných šortek hledejte pružný pas a dostatečnou délku, ale ne takovou, aby překážela při dřepu. Obecnější přehled nabízí kategorie <a href="/dresy/">dresy</a>, základní vrstvy najdete mezi <a href="/funkcni-tricka/">funkčními tričky</a> a <a href="/sportovni-kratasy/">sportovními kraťasy</a>.</p>'
          '<h2>Síť, stojany a vybavení hřiště</h2>'
          '<p>Síť o šířce zhruba jednoho metru se natahuje přes celé hřiště, bývá z uzlového nebo bezuzlového pletiva a s horním lemem. Výšku sítě upravují stojany: pro muže a ženy se liší a mládežnické kategorie mají nižší hodnoty. Pro zahradu postačí lehčí přenosná sada se zatloukanými kolíky, do haly se používají pevné stojany se závažím nebo zapuštěné v podlaze. Výrobci jako Pokorný sítě, Sedco a Acra nabízejí sítě i příslušenství pro školy a kluby.</p>'
          + T(['Prvek', 'Co vybírat', 'Poznámka'], [
              ['Síť', 'délka, šířka oka, horní lem', 'pevnost při intenzivní hře'],
              ['Stojany', 'výškové nastavení, stabilita', 'nesmí se kývat'],
              ['Antény', 'vyznačují hranici hřiště', 'nutné pro oficiální hru'],
              ['Čáry', 'pásky nebo lana', 'pro improvizované hřiště na trávě']]) +
          '<h2>Volejbal na písku</h2>'
          '<p>Plážový volejbal se hraje většinou naboso, takže obuv odpadá. Chrání ale ponožky určené na písek, brýle proti slunci a čepice. Povrch snižuje zatížení kloubů, zároveň ale zatěžuje lýtka a achilovku, protože noha se propadá. Při hře venku se hodí <a href="/plazove-doplnky/">plážové doplňky a osušky</a>, <a href="/pop-up-a-plazove-stany/">pop-up a plážové stany</a> pro stín a <a href="/panske-plavky/">pánské</a> či <a href="/damske-plavky/">dámské plavky</a> přizpůsobené pohybu. Pro delší pobyt se hodí i voda v <a href="/lahve-a-termosky/">láhvi nebo termosce</a>.</p>'
          '<h2>Výběr podle věku a úrovně</h2>'
          '<h3>Děti a začátečníci</h3>'
          '<p>Lehčí míč, nižší síť a obuv s pevnou patou. Hlavní je radost ze hry a bezpečné pohybové návyky. Dětem se vyplatí kupovat kolenní chrániče, i když zpočátku nepadají, protože si zvyknou na ně už při učení.</p>'
          '<h3>Školní a rekreační hráči</h3>'
          '<p>Odolnost proti běžnému opotřebení má přednost před špičkovými parametry. Odolný jednoduchý míč a spolehlivé boty vydrží několik sezón. K nim dobře poslouží i obyčejné <a href="/sportovni-ponozky/">sportovní ponožky</a>.</p>'
          '<h3>Klubové a soutěžní týmy</h3>'
          '<p>Důležitá je jednotnost vybavení, počet náhradních míčů a pravidelná výměna obuvi. Týmy často vybírají dresy v sadách, kterým lze potisknout čísla a jména, a míče schválené pro příslušnou soutěž. Soutěžní míč má předepsaný obvod, hmotnost a tlak.</p>'
          '<h2>Prevence zranění</h2>'
          '<p>Nejčastější problémy ve volejbale postihují kotníky, kolena, ramena a prsty. Pomáhá zahřátí před hrou, posilování lýtek a stehen, protažení ramen a správná technika dopadu s pokrčenými koleny. Opotřebovaná obuv ztrácí tlumení a tvrdé dopady se přenášejí do kloubů, proto ji vyměňte, jakmile podrážka hladká, pěna slehlá nebo se uvolňují švy. Při opakovaných bolestech kolene nebo ramene se obraťte na lékaře.</p>'
          '<h2>Péče o míč a výbavu</h2>'
          '<ul><li>Míč otřete vlhkým hadříkem a nevystavujte slunci ani mrazu.</li>'
          '<li>Při skladování ponechte lehce povolený tlak, aby se materiál neprotahoval.</li>'
          '<li>Obuv po tréninku vyvětrejte, vložky vyndejte a nesušte je na topení.</li>'
          '<li>Chrániče perte podle návodu a nechte je zavěšené, ať pěna nezestárne ve sbalené poloze.</li>'
          '<li>Síť skladujte suchou, volně složenou, bez knotů.</li></ul>'
          '<h2>Další míčové sporty a doplnění výbavy</h2>'
          '<p>Hráči často střídají volejbal s dalšími sporty. Podobnou sálovou přilnavost využijete při <a href="/florbalove-hole/">florbale</a> a obratnost s koordinací doplňkově zlepší <a href="/basketbalove-mice/">basketbal</a> nebo <a href="/fotbalove-mice/">fotbal</a>. Všechny míčové pomůcky shrnuje <a href="/micove-sporty/">kategorie míčových a raketových sportů</a>, ostatní vybavení pak <a href="/ostatni-micove-sporty/">další míčové sporty</a>. Přípravu kondice doplňte <a href="/posilovaci-gumy/">posilovacími gumami</a> a lehkými pomůckami pro <a href="/fitness-pomucky/">fitness</a>.</p>'
          '<h2>Trénink mimo hřiště</h2>'
          '<p>Volejbalový výskok roste díky silným lýtkům, stehnům a core, proto se vyplatí doplňkové cvičení doma. Skákací cviky, dřepy a jednoduchý trénink s gumou jsou vhodné pro začátečníky i pokročilé. Ramena potřebují prevenci proti přetížení při smeči a podání: cviky na lopatky a rotátorovou manžetu snižují riziko bolesti. Vždy zvyšujte zátěž postupně a po hře se protáhněte.</p>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>U volejbalových produktů rozhoduje typ, velikost a prostředí použití. Zadejte značku, u obuvi ověřte velikostní tabulku a podívejte se, kde je párů skladem. U míčů sledujte, zda jde o halový nebo plážový model a jestli je uznaný pro oficiální hru. Sítě porovnávejte podle délky, šířky a způsobu upevnění. Před koupí chrániče vždy změřte obvod kolene, aby nesjížděl.</p>',
    faq=[
        ('Jaký míč zvolit pro halu a jaký na pláž?', 'Do haly patří hladký míč s tužším odskokem, který je určen pro parket. Na písek se používá o něco větší a měkčí plážový míč, který je odolnější vůči větru a nepálí na dlaních. Rekreační modely zvládnou obě situace, ale hůř.'),
        ('Dá se hrát volejbal v běžecké obuvi?', 'Nedoporučuje se. Běžecká obuv má tlustší patu a pryž, která na parketu nedrží ideálně, takže roste riziko podvrtnutí. Sálová obuv má plošší stavbu, lepší přilnavost a tlumení přizpůsobené skokům a dopadům.'),
        ('Jak poznám správný tlak v míči?', 'Doporučené hodnoty bývají uvedeny na míči nebo v návodu. Míč by se při stlačení palcem měl lehce prohnout, ale ne zapadnout. Příliš tvrdý míč bolí předloktí, měkký padá krátce a hůř se odbíjí.'),
        ('Jsou kolenní chrániče nutné?', 'Nejsou povinné, ale pomáhají při pádech a snižují otlaky, zvlášť u hráčů v poli. Správně padnoucí chránič drží na místě a neomezuje ohyb. Při opakovaných bolestech se místo chráničů poraďte s lékařem.'),
        ('Kdy vyměnit volejbalovou obuv?', 'Jakmile podrážka ztratí přilnavost, pěna v mezipodešvi slehne nebo se bota začne deformovat. Hráč, který trénuje několikrát týdně, vymění obuv dříve než ten, kdo hraje občas. Opotřebovaná bota nechrání klouby.'),
        ('Do jaké výšky se věší volejbalová síť?', 'Ve výšce se liší muži a ženy: u mužů je to 2,43 m, u žen 2,24 m. Mládež a školní skupiny používají nižší síť podle kategorie a pravidel soutěže. Pro rekreační hru si upravte výšku podle schopností hráčů a zajistěte, aby byla síť napnutá.'),
        ('Čím se liší dámský a pánský volejbalový dres?', 'Střih bývá přizpůsoben postavě, dámské modely jsou užší v pase a mají vykrojení ramen. Materiál se obvykle neliší. Při týmovém nákupu sledujte shodné barvy, velikostní řadu a možnost potisku čísla.'),
        ('Jak se starat o plážový míč?', 'Po hře z něj setřete písek a sůl vlhkým hadříkem, nechte jej oschnout ve stínu a neskladujte na přímém slunci. Písek v ventilku poškodí jehlu i těsnění, proto ventilek při hustění vždy očistěte.'),
        ('Mohu hrát volejbal na zahradě s lehkou sadou?', 'Ano. Přenosná sada se sítí, kolíky a měkčím míčem stačí pro rodinnou nebo táborovou hru. Zkontrolujte pevnost kolíků a ukotvení, aby se síť při větru nepřevrátila, a míč volte odolný proti trávě a písku.'),
        ('Jak předejít zranění kotníku?', 'Zahřejte kloub, posilujte lýtka a stabilizační svaly, noste obuv s pevným uchycením paty a naučte se dopad na pokrčená kolena. Dříve zraněný kotník podepřete bandáží nebo ortézou, ale rozsáhlejší problém řešte s lékařem.'),
    ],
)


# ------------------------------------------------------------------ elektrokola
NEW['elektrokola'] = dict(long=True,
    title='Elektrokola: motor, baterie, typy a výběr',
    desc='Elektrokola horská, trekingová, skládací, nákladní i fatbike. Jak vybrat motor, baterii, rám a velikost a kde porovnat nabídky českých obchodů.',
    intro='<p>Elektrokolo vypadá jako běžné jízdní kolo, jenže pod rámem nebo v nábojích skrývá motor, který podpoří šlapání. Kopec, protivítr nebo cesta do práce v košili najednou přestanou být překážkou. Rozdíly mezi modely ale zásadně ovlivňují komfort: umístění motoru, kapacita baterie, geometrie rámu a hmotnost rozhodují o tom, zda vás kolo bude bavit i po roce.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u značek jako Engwe, Fafrees, Specialized, Samebike, Crussis, Trek nebo Evercross. Pohled můžete zúžit na <a href="/horska-elektrokola/">horská</a>, <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská</a>, <a href="/skladaci-elektrokola/">skládací</a>, <a href="/nakladni-elektrokola/">nákladní</a> nebo <a href="/fatbike-elektrokola/">fatbike elektrokola</a>. Průvodce vysvětluje motory, baterie, dojezd, údržbu i povinné vybavení a upozorní na chyby, které se při prvním nákupu opakují nejčastěji.</p>',
    guide='<h2>Jak elektrokolo funguje</h2>'
          '<p>Systém tvoří motor, baterie, řídicí jednotka, displej a senzor, který pozná, že šlapete. Při šlapání přidá motor sílu podle zvolené úrovně podpory. Na evropském trhu je pomoc motoru podmíněna šlapáním a končí při rychlosti 25 km/h, jmenovitý výkon se udává do 250 W. Dopravní předpisy se vztahují na silnější či rychlejší stroje jinak, proto si před koupí ověřte, do jaké kategorie model patří. Rychlejší a výkonnější stroje bývají považovány za jiná vozidla, mohou vyžadovat registraci a pojištění.</p>'
          + T(['Součást', 'Úloha', 'Co sledovat'], [
              ['Motor', 'přidává sílu při šlapání', 'umístění, točivý moment, hlučnost'],
              ['Baterie', 'zásobuje motor energií', 'kapacita ve Wh, vyjímatelnost, životnost'],
              ['Senzor', 'určuje míru podpory', 'snímač točivého momentu nebo pohybu'],
              ['Displej', 'volba podpory, údaje o jízdě', 'čitelnost na slunci'],
              ['Nabíječka', 'dobíjí baterii', 'doba nabití, kompatibilita']]) +
          '<h2>Motor: střední, zadní, přední</h2>'
          '<p>Střední motor sedí u kliky a tlačí do pohonu, takže těžiště zůstává nízko a uprostřed. Kolo se řídí přirozeněji, převody se používají obvyklým způsobem a pohon využívá i stoupání. Zadní motor v náboji vypadá nenápadněji a je často levnější, ale zatěžuje zadní kolo a při defektu je výměna složitější. Přední motor se dnes používá výjimečně, protože ovlivňuje řízení a přilnavost předního kola.</p>'
          + T(['Motor', 'Výhody', 'Nevýhody'], [
              ['Střední', 'vyvážené těžiště, přirozená jízda', 'složitější konstrukce, vyšší nároky na pohon'],
              ['Zadní', 'jednodušší konstrukce, tichý chod', 'váha na zadním kole, složitější výměna kola'],
              ['Přední', 'nenáročné doplnění kola', 'méně přirozené řízení, horší záběr']]) +
          '<p>Točivý moment v newtonmetrech vyjadřuje sílu při rozjezdu a do kopce. Vyšší hodnota pomůže na strmých úsecích a s nákladem, ale spotřebuje víc energie. Pro rovinu a město bohatě stačí umírněný motor, na horské stezky a těžký náklad hledejte silnější jednotku.</p>'
          '<h2>Baterie, kapacita a skutečný dojezd</h2>'
          '<p>Kapacita se udává ve watthodinách. Vyšší číslo znamená větší zásobu energie, ale i vyšší hmotnost baterie. Skutečný dojezd závisí na hmotnosti jezdce a nákladu, terénu, větru, teplotě, tlaku v pneumatikách a zvolené úrovni podpory. Výrobce uvádí rozsah, kterého dosáhnete jen v příznivých podmínkách, takže počítejte s menší hodnotou. V zimě kapacita klesá, protože chemické procesy v článcích zpomalí chlad.</p>'
          '<p>Baterie lze nejčastěji vyjmout a nabíjet doma, což usnadňuje život v panelákovém bytě. Integrovaná baterie v rámu vypadá čistěji, ale nabíjení vyžaduje přístup ke kolu. Dlouhodobě se baterii nedoporučuje držet úplně vybitou ani plně nabitou. Skladujte ji při pokojové teplotě a před zimou nabijte zhruba do poloviny. Při nákupu zjistěte, jak je dostupná náhradní baterie a servis.</p>'
          '<h2>Typy elektrokol podle použití</h2>'
          '<h3>Trekingová a městská</h3>'
          '<p>Pohodlná poloha, blatníky, nosič, světla a široké pláště. Vhodná na dojíždění, nákupy i dlouhé cyklostezky. Najdete je v kategorii <a href="/trekingova-a-mestska-elektrokola/">trekingová a městská elektrokola</a> a tématicky souvisejí i <a href="/mestska-elektrokola/">městská</a> a <a href="/trekingova-elektrokola/">trekingová</a> kola.</p>'
          '<h3>Horská</h3>'
          '<p>Odpružená vidlice, silnější rám, hrubý plášť a výkonnější motor. Pomáhají vyjet i prudké stezky, kde by bez pomoci došly síly. U celoodpružených modelů se zvyšuje hmotnost i cena, takže si rozmyslete, zda opravdu pojedete náročný terén. Podrobnosti najdete v kategorii <a href="/horska-elektrokola/">horská elektrokola</a>.</p>'
          '<h3>Silniční a gravel</h3>'
          '<p>Lehčí rám, úzký plášť a sportovní poloha. Motor je menší a méně znatelný, cílem je pomoc na dlouhých trasách. Modely sdružuje <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel elektrokola</a>.</p>'
          '<h3>Skládací</h3>'
          '<p>Malá kola, kloub v rámu a sklopná řídítka. Hodí se pro kombinaci s vlakem, MHD a pro nedostatek úložného prostoru. Vyšší hmotnost skládacích modelů vyvažuje flexibilita. Prohlédněte si <a href="/skladaci-elektrokola/">skládací elektrokola</a>.</p>'
          '<h3>Fatbike</h3>'
          '<p>Extra široké pláště, které zvládají písek, sníh i bahno. Pohodlně jedou po hrbolatém terénu, ale mají větší valivý odpor a váhu. Zájemci najdou nabídku v <a href="/fatbike-elektrokola/">fatbike elektrokolech</a>.</p>'
          '<h3>Nákladní</h3>'
          '<p>Prodloužený rám, nosnost pro děti a nákupy, často dvě kola vpředu nebo boxový nástavec. Při rodinném provozu nahradí druhé auto na krátké trasy. Více v kategorii <a href="/nakladni-elektrokola/">nákladní elektrokola</a>.</p>'
          '<h3>Dámská a dětská</h3>'
          '<p>Nižší horní trubka usnadňuje nasedání a hodí se při jízdě v sukni nebo s nákupem. Dětské a juniorské modely mají menší rám a omezený výkon. Viz <a href="/damska-elektrokola/">dámská elektrokola</a> a <a href="/detska-elektrokola/">dětská a juniorská elektrokola</a>.</p>'
          + T(['Typ', 'Hlavní použití', 'Typický prvek'], [
              ['Trekingové a městské', 'dojíždění, výlety', 'blatníky, nosič, světla'],
              ['Horské', 'stezky, kopce', 'odpružení, hrubý plášť'],
              ['Silniční a gravel', 'dlouhé trasy, rychlost', 'úzký plášť, lehký rám'],
              ['Skládací', 'vlak, byt, loď', 'kloub v rámu, malá kola'],
              ['Fatbike', 'písek, sníh, bahno', 'extra široká kola'],
              ['Nákladní', 'rodina, nákup', 'dlouhý rám, vysoká nosnost']]) +
          '<h2>Velikost rámu a ergonomie</h2>'
          '<p>Správná velikost se odvíjí od výšky postavy a délky nohou. Tabulky výrobců uvádějí rozsah výšek pro jednotlivé rámy. Rozhodující je komfortní postoj nad horní trubkou, mírně pokrčené koleno při spodní poloze pedálu a pohodlný dosah na řídítka. Sedlovku a představec lze nastavit, ale chybná velikost rámu se nevyřeší. Při nejistotě mezi dvěma velikostmi zvolte tu, která lépe vyhovuje typu jízdy: menší pro městský provoz, větší pro stabilitu na dlouhých trasách.</p>'
          '<h2>Hmotnost, brzdy a převody</h2>'
          '<p>Elektrokolo váží víc než běžné kolo, proto potřebuje silnější brzdy. Hydraulické kotoučové brzdy drží i při dlouhém klesání a vyžadují méně síly. Mechanické jsou jednodušší na opravu, ale slabší. Převody se dělí na vnější přehazovačku a vnitřní nábojovou převodovku. Nábojová převodovka je ochráněná před nečistotou a hodí se do města, přehazovačka nabízí širší rozsah a lehčí chod do kopce. Opotřebení pohonu je vyšší než u běžného kola, takže řetěz a kazetu vyměňujte včas. Díly pro údržbu hledejte v kategoriích <a href="/cyklo-pohon/">pohon</a>, <a href="/cyklo-brzdy/">brzdy</a> a <a href="/plaste-a-duse/">pláště a duše</a>.</p>'
          '<h2>Povinná a doporučená výbava</h2>'
          '<p>Při jízdě po komunikaci potřebujete bílé přední a červené zadní světlo, odrazky a funkční zvonek. Na ulici nesmí chybět ani brzdy v dobrém stavu. Kvalitní osvětlení najdete mezi <a href="/cyklo-svetla/">světly na kolo</a>, zvonek a zrcátko v kategorii <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a>. Přilba je pro mladší jezdce povinná, ostatním ji vřele doporučujeme, protože rychlost elektrokol je vyšší než u běžných kol. Vybírejte z <a href="/cyklisticke-helmy/">cyklistických helem</a>, městské varianty najdete v <a href="/mestske-cyklohelmy/">městských cyklohelmách</a>. Kolo je cenný majetek, zajistěte ho kvalitním <a href="/cyklo-zamky/">zámkem na kolo</a>.</p>'
          '<h2>Příslušenství, které se vyplatí</h2>'
          '<ul><li>Brašny a nosiče z kategorie <a href="/cyklo-tasky-a-nosice/">brašny, nosiče a košíky</a> pro nákupy.</li>'
          '<li>Blatníky z kategorie <a href="/cyklo-blatniky/">blatníky</a> pro ježdění za deště.</li>'
          '<li>Držák telefonu a lahev z <a href="/cyklo-lahve-a-drzaky/">lahví a držáků</a>.</li>'
          '<li>Cyklopočítač z kategorie <a href="/cyklo-computery/">cyklopočítače a navigace</a>.</li>'
          '<li>Nosič na auto z kategorie <a href="/cyklo-nosice-na-auto/">nosiče kol na auto</a>, pokud vozíte kolo na dovolenou.</li></ul>'
          '<h2>Údržba a péče</h2>'
          '<p>Elektrokolo má stejné součásti jako běžné kolo, a proto potřebuje stejnou pravidelnou péči. Mazejte řetěz, kontrolujte tlak v pláštích a stav brzdových destiček, čistěte kolo jemnou vodou a houbou. Nikdy ho nemyjte vysokotlakým proudem přímo do motoru a kontaktů baterie. Po zimě zkontrolujte kabeláž a konektory. Mazadla a čističe nabízí kategorie <a href="/cyklo-udrzba/">údržba kola</a>, pumpy a nářadí <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>. Servis motoru a baterie ponechte autorizované dílně, abyste nepřišli o záruku.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li>Orientace jen podle zveřejněného dojezdu bez ohledu na hmotnost a terén.</li>'
          '<li>Podcenění váhy při nošení do schodů nebo na nosič auta.</li>'
          '<li>Nezjištěný servis a dostupnost náhradních dílů a baterií.</li>'
          '<li>Špatná velikost rámu, kterou nezachrání žádné seřízení.</li>'
          '<li>Sleva na modelu bez uvedené kapacity baterie nebo značky motoru.</li></ul>'
          '<h2>Pro koho které elektrokolo</h2>'
          '<p>Dojíždějící potřebují blatníky, světla, odolné pláště a spolehlivou baterii, nejlépe vyjímatelnou. Rodiny s dětmi zvažují nákladní kolo nebo přívěs, k čemuž pomáhají <a href="/cyklo-sedacky-a-voziky/">dětské sedačky a vozíky za kolo</a>. Rekreační jezdci na cyklostezky spokojí trekingové modely, sportovci hledají horský nebo gravel typ. Starším lidem a návratníkům k pohybu pomůže nízký nástup a vyvážená poloha. Kdo bydlí v bytě, ocení skládací provedení.</p>'
          '<h2>Jak porovnávat nabídky na Sportece</h2>'
          '<p>Katalog sjednocuje nabídky českých obchodů a umožňuje filtrovat podle značky a typu kola. U každého modelu ověřte kapacitu baterie, umístění motoru, velikost rámu, rozměr kol a hmotnost. Porovnávejte i záruku, dostupnost servisu a to, co je v ceně, například nabíječka, blatníky nebo zámek. U neznámých značek čtěte zkušenosti ostatních uživatelů a zjistěte, zda prodejce nabízí náhradní díly a opravu. Zajímavou alternativou k celému kolu je <a href="/elektrokolobezky/">elektrokoloběžka</a>, vhodná na kratší trasy.</p>',
    faq=[
        ('Jak daleko dojedu na jedno nabití?', 'Dojezd se liší podle kapacity baterie, hmotnosti jezdce a nákladu, terénu, větru a zvolené podpory. Výrobce uvádí hodnoty za příznivých podmínek, ve skutečnosti obvykle vyjde méně. V zimě kapacita klesá a v kopcích rychle klesne podpora.'),
        ('Potřebuji na elektrokolo řidičský průkaz a pojištění?', 'Standardní elektrokolo s podporou do 25 km/h a výkonem do 250 W se v Česku posuzuje jako kolo a registraci ani pojištění nevyžaduje. Rychlejší a silnější stroje spadají do jiné kategorie, proto si ověřte parametry v návodu a platných předpisech.'),
        ('Který motor je lepší, střední, nebo zadní?', 'Střední motor dává přirozenější jízdu a lepší rozložení váhy, zadní bývá jednodušší a nenápadnější. Na kopce a horské stezky se hodí střední, na město a rovinu stačí často zadní. Rozhoduje i rozpočet a servis.'),
        ('Jak dlouho vydrží baterie?', 'Životnost se udává v počtu nabíjecích cyklů a ovlivňuje ji způsob používání, teplota a skladování. Baterii nenechávejte dlouho zcela vybitou, nevystavujte horku ani mrazu a před zimou ji nabijte zhruba do poloviny.'),
        ('Mohu jezdit na elektrokole v dešti?', 'Ano, kola jsou konstruována na běžný déšť. Nemyjte však přístroj přímým tlakem vody do motoru a kontaktů baterie. Po jízdě v mokru očistěte řetěz, vysušte konektory a promažte pohon.'),
        ('Jaká velikost rámu mi bude sedět?', 'Podívejte se na tabulku výrobce podle výšky postavy. Při stoji nad rámem by mezi rozkrokem a horní trubkou měla být rezerva, nohy při šlapání mírně pokrčené. Při nejistotě si kolo zkuste nebo kontaktujte prodejce.'),
        ('Je těžké elektrokolo problém při převozu?', 'Elektrokolo váží výrazně víc než běžné kolo. Při převozu na autě používejte nosič s dostatečnou nosností a baterii vyndejte. Do schodů nebo výtahu zvažte skládací provedení s menší hmotností.'),
        ('Dá se běžné kolo přestavět na elektrokolo?', 'Existují sady s motorem a baterií, ale kvalita provedení se liší a zásah do brzd a rámu vyžaduje odborné znalosti. Hotové elektrokolo má sladěné komponenty a záruku, doplňovací sada nabízí vyšší flexibilitu na vlastní odpovědnost.'),
        ('Jak elektrokolo správně dobíjet?', 'Používejte originální nabíječku a nabíjejte při pokojové teplotě. Baterii nenechávejte připojenou donekonečna a nenabíjejte ji bez dozoru. Při dlouhodobém skladování ji nechte částečně nabitou a kontrolujte stav každých pár týdnů.'),
        ('Na co se zaměřit u levných elektrokol?', 'Hledejte jasně uvedenou kapacitu baterie, značku motoru a komponentů, dostupnost náhradních dílů a servisu a záruku. U extrémně levných nabídek bez těchto údajů hrozí slabší brzdy, kratší životnost baterie a složité opravy.'),
    ],
)
